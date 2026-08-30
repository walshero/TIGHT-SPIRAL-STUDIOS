#!/usr/bin/env python3
"""
NO WALLS — one pass, one write per file.

Batch 1 (2026-08-29) spent 3-4 connector commits per surface. That is why a run
takes an hour and why batch 2 stalled. This does the whole edit locally, proves
it with comfort-gate, and leaves ONE file to push.

THE DISTINCTION THAT BINDS (CLAUDE.md): the WALL is the UI that asks. The KERNEL
is the CSS that answers `data-light`. Nothing here touches a :root token, a
data-light rule, a hue, or the <html data-light> attribute. Only markup and the
handlers bound to it come out.

DEFECT FOUND AND CLOSED 2026-08-30: the first version bracketed the comfort panel
with `<div[^>]*id="sePanel".*?</div>` non-greedy, which stops at the FIRST inner
</div> — the .se-row that holds the light buttons. It left the whole lower half of
the panel standing and the leftover check refused all 40 files. A nested block
needs a matcher, not a lazy quantifier. The refusal is the reason nothing shipped
broken; keep it.

Skips, loudly, rather than guessing.
"""
import re, sys

HOME_RE = re.compile(r'<a class="se-home" href="index\.html"[^>]*>\s*Home\s*</a>')
NEWNAV  = ('<a class="se-home" href="index.html" aria-label="The studio">Studio</a>'
           '<a class="se-home" href="arcade.html" aria-label="The cabinet">Cabinet</a>')
BTN_RE  = re.compile(r'[ \t]*<button[^>]*id="seEyes"[^>]*>.*?</button>[ \t]*\n?', re.S)
TAG_RE  = re.compile(r'</?div\b', re.I)


def cut_div(src, anchor):
    """Remove the <div> whose open tag matches `anchor`, matching nesting."""
    m = re.search(anchor, src)
    if not m:
        return src, 0
    start = m.start()
    depth = 0
    for t in TAG_RE.finditer(src, start):
        depth += 1 if t.group(0)[1] != '/' else -1
        if depth == 0:
            end = t.end()
            end = src.find('>', end) + 1
            # take a preceding HTML comment and the trailing newline with it
            head = src.rfind('<!--', 0, start)
            if head != -1 and src.find('-->', head) < start and \
               src[src.find('-->', head) + 3:start].strip() == '':
                start = head
            line_start = src.rfind('\n', 0, start) + 1
            if src[line_start:start].strip() == '':
                start = line_start
            while end < len(src) and src[end] in ' \t':
                end += 1
            if end < len(src) and src[end] == '\n':
                end += 1
            return src[:start] + src[end:], 1
    return src, 0


def cut_handler(src, needle):
    """Remove one `[].forEach.call(document.querySelectorAll('[needle]') ...);});`
    statement, plus its own comment line, by balancing parentheses."""
    m = re.search(r'\[\]\.forEach\.call\(document\.querySelectorAll\(\'\[' +
                  re.escape(needle) + r'\]\'\)', src)
    if not m:
        return src, 0
    start = m.start()
    i = src.index('(', start)
    depth = 0
    while i < len(src):
        if src[i] == '(':
            depth += 1
        elif src[i] == ')':
            depth -= 1
            if depth == 0:
                break
        i += 1
    end = i + 1
    if src[end:end + 1] == ';':
        end += 1
    line_start = src.rfind('\n', 0, start) + 1
    if src[line_start:start].strip() == '':
        start = line_start
    prev = src.rfind('\n', 0, start - 1) + 1
    if src[prev:start].strip().startswith('//'):
        start = prev
    while end < len(src) and src[end] in ' \t':
        end += 1
    if end < len(src) and src[end] == '\n':
        end += 1
    return src[:start] + src[end:], 1


EYES_START = re.compile(r'[ \t]*var eyes\s*=\s*(?:document\.getElementById|\$)\(\'seEyes\'\)[^\n]*\n')
GUARD      = re.compile(r'[ \t]*if\s*\(\s*eyes\s*&&\s*panel\s*\)\s*\{')
# A FOURTH DIALECT, found 2026-08-30 by the JS check and not by the string check:
# trail-notes.html guards with `if(!eyes||!panel) return;`. The var line came out,
# the guard stayed, and the page threw "eyes is not defined" on load — while every
# leftover-string test passed, because the strings seEyes/sePanel had gone with the
# var line. A wall can be gone from the markup and still break the page. Consume any
# following one-line statement that still names eyes, panel or setOpen.
PLAIN      = re.compile(
    r'[ \t]*(?:'
    r'if\s*\(\s*!\s*eyes\s*\|\|\s*!\s*panel\s*\)[^\n]*'      # early-return guard
    r'|function setOpen[^\n]*'
    r'|eyes\.[^\n]*'
    r'|panel\.[^\n]*'
    r'|document\.addEventListener\([^\n]*(?:panel|eyes)[^\n]*'  # outside-click / Escape
    r')\n')


def cut_eyes_js(src):
    """Remove the panel open/close wiring. Three dialects in the corpus:
    a flat run of statements, and a `if(eyes&&panel){ ... }` guarded block —
    which the flat pattern silently missed on 12 files. Balance the brace."""
    m = EYES_START.search(src)
    if not m:
        return src, 0
    start, end = m.start(), m.end()
    g = GUARD.match(src, end)
    if g:
        i = src.index('{', g.start())
        depth = 0
        while i < len(src):
            if src[i] == '{':
                depth += 1
            elif src[i] == '}':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        end = i + 1
        while end < len(src) and src[end] in ' \t\n':
            end += 1
            if src[end - 1] == '\n':
                break
    else:
        while True:
            p = PLAIN.match(src, end)
            if not p:
                break
            end = p.end()
    return src[:start] + src[end:], 1


def clean(src):
    notes, out = [], src
    if 'class="se-chrome"' not in out:
        return None, ['no se-chrome header — hand-set']

    if 'aria-label="The cabinet"' in out:
        notes.append('cabinet already there')
    else:
        out, n = HOME_RE.subn(NEWNAV, out, count=1)
        if not n:
            return None, ['se-chrome does not carry the standard Home link — hand-set']
        notes.append('top rail: Studio | Cabinet')

    out, n = BTN_RE.subn('', out)
    if n: notes.append('comfort button')

    out, n = cut_div(out, r'<div[^>]*id="sePanel"[^>]*>')
    if n: notes.append('comfort panel')

    out, n = cut_eyes_js(out)
    if n: notes.append('open/close')

    for needle in ('data-light-set', 'data-text', 'data-tog'):
        while True:
            out, n = cut_handler(out, needle)
            if not n:
                break
            notes.append(needle)

    leftover = [t for t in ('seEyes', 'sePanel', 'data-light-set', 'data-text=', 'data-tog')
                if t in out]
    if leftover:
        return None, ['wall fragments survive: ' + ', '.join(leftover)]

    # THE KERNEL MUST BE BYTE-IDENTICAL. Not "mostly the same" — identical.
    # Counting tokens does not work here: se-a1 / se-contrast / data-light live in
    # BOTH the CSS (kernel, keep) and the handlers (wall, cut), so a count check
    # refuses every file. Compare the <style> blocks and the <html> attributes.
    styles = lambda s: re.findall(r'<style[^>]*>.*?</style>', s, re.S)
    if styles(src) != styles(out):
        return None, ['KERNEL TOUCHED (style block changed) — refused']
    htmltag = lambda s: re.search(r'<html[^>]*>', s, re.I)
    if (htmltag(src) and htmltag(out) and
            htmltag(src).group(0) != htmltag(out).group(0)):
        return None, ['KERNEL TOUCHED (html data-light attribute) — refused']

    if out == src:
        return None, ['already clean']
    return out, notes


if __name__ == '__main__':
    for path in sys.argv[1:]:
        src = open(path, encoding='utf-8').read()
        new, notes = clean(src)
        if new is None:
            print(f'SKIP  {path:42s} {"; ".join(notes)}')
            continue
        open(path, 'w', encoding='utf-8').write(new)
        print(f'CUT   {path:42s} {len(src)} -> {len(new)}  ({"; ".join(notes)})')
