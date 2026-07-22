#!/usr/bin/env python3
# STUDIO EYES SWEEP — the executable organ. Tight Spiral Productions.
# Belt beat 2 runs this by name: python3 studio-eyes-sweep.py [directory]
# Element-aware tier-1.5: a color is judged against ITS OWN element's background
# (merged across same-selector rules) before falling back to the page background.
# This kills the dark-text-on-bright-button false-positive class (2026-07-03 lesson).
#
# HALT classes:
#   H1 invisible/low text in any comfort stop (element-aware, WCAG AA 4.5 / large 3.0)
#   H2 charcoal floor: pure #000 bg or #fff ink in a dark stop
#   H3 silent skip: a dark class is referenced but its palette can't be parsed
#   H4 offline break: fetch/XHR/localStorage/sessionStorage/external resources
# WARN classes: missing :focus-visible, missing scroll-reset, emoji in visible text.
# Allowlist below: files that legitimately name banned tokens (auditors) or are
# institutional-lane (offline floor exempt per founder call — pending).

import re, sys, glob, os

ALLOWLIST_OFFLINE = {"studio-eyes-auditor.html"}  # names the tokens it hunts
INSTITUTIONAL = {"confluence-TRUNK.html", "confluence-TRUNK-2026-06-23.html",
                 "confluence-walkthrough.html"}   # exemption PENDING founder call
FOUNDER_OPS = {"live.html"}  # founder testing lane: reads same-origin version.json by design (founder call 2026-07-22)
DARK_CLASSES = ["warmdark", "warm", "dark"]        # canon call open: pick one

def hex2rgb(h):
    h = h.lstrip('#')
    if len(h) == 3: h = ''.join(c*2 for c in h)
    if len(h) != 6: return None
    try: return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except ValueError: return None

def lum(rgb):
    def f(c):
        c /= 255
        return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(rgb[0]) + 0.7152*f(rgb[1]) + 0.0722*f(rgb[2])

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def parse_vars(block):
    return dict(re.findall(r'--([\w-]+)\s*:\s*([^;]+);', block))

def resolve(val, palette, depth=0):
    val = val.strip()
    if depth > 3: return val
    m = re.match(r'var\(--([\w-]+)\)', val)
    if m and m.group(1) in palette:
        return resolve(palette[m.group(1)], palette, depth+1)
    return val

def rules(css):
    # yield (selector, propdict) merging same-selector blocks.
    #
    # BUG (found 2026-07-11): the flat regex `([^{}]+){([^{}]*)}` cannot see
    # inside an at-rule. Rules nested in @media / @supports were parsed with the
    # at-rule prelude glued onto the selector, so '.mh' inside a @media block was
    # never a key — and every color grounded against it fell through to the page
    # and HALTed as invisible. Unwrap at-rules first, then parse.
    css = strip_at_rules(strip_comments(css))
    merged = {}
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        sel = ' '.join(m.group(1).split())
        props = dict(re.findall(r'([\w-]+)\s*:\s*([^;]+)', m.group(2)))
        merged.setdefault(sel, {}).update(props)
    # grouped selectors must be individually findable for grounding
    merged.update(split_groups(merged))
    return merged

def strip_comments(css):
    """Remove /* ... */ comments.

    BUG (found 2026-07-11) — THE ROOT CAUSE of the phantom-HALT class:
    the rule regex `([^{}]+){...}` captures everything between the previous '}'
    and the next '{'. That INCLUDES any preceding comment. So

        /* MASTHEAD */
        .mh { background: var(--pine); }

    parsed as the selector "/* MASTHEAD */ .mh" — not ".mh". The key never
    matched, so every descendant grounding against .mh fell through to the page
    background and HALTed as INVISIBLE. White-on-dark-green read as 1.1:1.

    Any selector preceded by a comment was silently unfindable. This corrupted
    grounding across the whole shelf and manufactured false HALTs that trained
    the founder to distrust the auditor.
    """
    return re.sub(r'/\*[\s\S]*?\*/', ' ', css)

def split_groups(merged):
    """Explode grouped selectors: '.a,.b{...}' must be findable as '.a' and '.b'.
    Without this, a background declared on a comma group is invisible to lookup."""
    out = {}
    for sel, props in merged.items():
        for part in sel.split(','):
            part = ' '.join(part.split())
            if part:
                out.setdefault(part, {}).update(props)
    return out

def strip_at_rules(css):
    """Remove @media/@supports wrappers, keeping their inner rules at top level.
    Brace-matched, so nested at-rules unwrap correctly."""
    out, i, n = [], 0, len(css)
    while i < n:
        m = re.compile(r'@(media|supports|layer|container)[^{]*\{').search(css, i)
        if not m:
            out.append(css[i:]); break
        out.append(css[i:m.start()])          # everything before the at-rule
        depth, j = 1, m.end()
        while j < n and depth:                # brace-match to the at-rule's close
            if css[j] == '{': depth += 1
            elif css[j] == '}': depth -= 1
            j += 1
        inner = css[m.end(): j-1 if depth == 0 else n]
        out.append(strip_at_rules(inner))     # recurse: nested at-rules
        i = j
    return "".join(out)

# ---------------------------------------------------------------------------
# DOM-GROUNDED ANCESTRY  (repair 2026-07-11)
#
# The 2026-07-05 repair walked the ancestor chain by SPLITTING THE SELECTOR ON
# WHITESPACE. That grounds descendant selectors ('.foot a' -> '.foot') and
# nothing else. A single-token selector like '.mh-name' has no whitespace, so
# the loop `range(len(toks)-1, 0, -1)` is EMPTY and the walk never runs — the
# color falls through to the page background and HALTs as invisible.
#
# But '.mh-name' IS inside '.mh { background: var(--pine) }' in the DOM. The
# relationship is a BEM prefix, not a descendant combinator. No amount of
# string-splitting can see that. The selector string is not the DOM.
#
# FIX: ground against the ACTUAL rendered tree. Parse the HTML, find the
# elements a selector matches, walk their real parents, and take the nearest
# ancestor that paints a background. Falls back to the old string walk only
# when the DOM can't answer.
# ---------------------------------------------------------------------------
def build_dom_index(src):
    """Map each class -> the list of elements carrying it, for real-parent lookup."""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        return None
    soup = BeautifulSoup(src, 'html.parser')
    idx = {}
    for el in soup.find_all(True):
        for c in (el.get('class') or []):
            idx.setdefault(c, []).append(el)
    return {'soup': soup, 'byclass': idx}

def sel_key_class(sel):
    """The class a rule hangs on: last simple class token, pseudo/attr stripped."""
    last = sel.split()[-1] if sel.split() else sel
    last = re.split(r'[:\[]', last)[0]          # .mh-tab:hover -> .mh-tab
    m = re.findall(r'\.([\w-]+)', last)
    return m[-1] if m else None

def bem_prefix_chain(sel):
    """Infer ancestry from a BEM-ish prefix when the DOM can't answer.

    JS-injected nodes are not in the static HTML, so dom_ancestor_bgs() returns
    [] for them. Rather than silently ground to the page (which manufactures a
    false INVISIBLE HALT), fall back to the naming convention: '.mh-mark' is
    almost certainly inside '.mh'. Longest prefix first.
    """
    cls = sel_key_class(sel)
    if not cls: return []
    parts = cls.split('-')
    return ['.' + '-'.join(parts[:k]) for k in range(len(parts)-1, 0, -1)]

def family_bgs(sel, R):
    """Last resort: a component's own family names its ground.

    '.lum-poem' has no DOM node (JS-injected) and '.lum' declares no background,
    but its sibling '.lum-hero' paints var(--pine). Components paint their
    container, and every child sits on it. Prefer the longest shared prefix, and
    return the DARKEST candidate — grounding a light text against a light
    sibling would invent a HALT, which is the failure we are trying to kill.
    """
    cls = sel_key_class(sel)
    if not cls or '-' not in cls: return []
    root = cls.split('-')[0]
    fam = []
    for k, props in R.items():
        kc = sel_key_class(k)
        if not kc or not kc.startswith(root + '-'): continue
        if k == sel: continue
        if props.get('background') or props.get('background-color'):
            fam.append(k)
    return fam

def dom_ancestor_bgs(sel, dom):
    """Real ancestors (nearest-first) of every element this selector matches."""
    if not dom: return []
    cls = sel_key_class(sel)
    if not cls: return []
    chains = []
    for el in dom['byclass'].get(cls, [])[:6]:   # sample; identical in practice
        chain = []
        p = el.parent
        while p is not None and getattr(p, 'name', None):
            for c in (p.get('class') or []):
                chain.append('.' + c)
            if p.name in ('body', 'html'):
                break
            p = p.parent
        chains.append(chain)
    if not chains: return []
    # nearest-first, de-duplicated, preserving order
    seen, flat = set(), []
    for c in chains[0]:
        if c not in seen:
            seen.add(c); flat.append(c)
    return flat

def sweep(path):
    name = os.path.basename(path)
    src = open(path, errors='replace').read()
    out = {"H1": [], "H2": [], "H3": [], "H4": [], "H6": [], "H7": [], "H8": [], "WARN": []}
    DOM = build_dom_index(src)
    # BUG (found 2026-07-11): the sweep read only the FIRST <style> block.
    # Any file with a second style block had those rules INVISIBLE to every
    # check — no contrast, no stop, nothing. Concatenate all of them.
    css = "\n".join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', src, re.I))

    # --- H4 offline floor ---
    if name not in ALLOWLIST_OFFLINE and name not in INSTITUTIONAL and name not in FOUNDER_OPS:
        for tok in ['localStorage', 'sessionStorage', 'XMLHttpRequest', 'fetch(']:
            if tok in src: out["H4"].append(f"uses {tok}")
        for m in re.finditer(r'(?:src|href)="(https?://[^"]+)"', src):
            if not m.group(1).startswith('https://drive.google'):
                out["H4"].append(f"external resource {m.group(1)[:60]}")
    if name in INSTITUTIONAL and 'localStorage' in src:
        out["WARN"].append("institutional-lane offline break (exemption pending founder call)")

    # --- palettes per stop ---
    rm = re.search(r':root\s*\{([^}]*)\}', css)
    root = parse_vars(rm.group(1)) if rm else {}
    stops = {"default": dict(root)}
    referenced_dark = bool(re.search(r"['\"](warmdark|warm|dark)['\"]", src)) or bool(re.search(r'body\.(warmdark|warm|dark)\b', css))
    dark_found = None
    for cls in DARK_CLASSES + ["softer", "soft", "daylight", "light"]:
        bm = re.search(r'body\.' + cls + r'\s*\{([^}]*)\}', css)
        if bm:
            p = dict(root); p.update(parse_vars(bm.group(1)))
            stops[cls] = p
            if cls in DARK_CLASSES and dark_found is None: dark_found = cls
    if referenced_dark and not dark_found and root:
        out["H3"].append("dark class referenced but no parseable dark palette — stop is UNTESTED (silent-skip)")

    R = rules(css)
    for stopname, pal in stops.items():
        bg_page = None
        for key in ('paper', 'bg'):
            if key in pal:
                bg_page = hex2rgb(resolve(pal[key], pal)); break
        if not bg_page: continue
        is_dark = lum(bg_page) < 0.2
        # H2 charcoal floor
        if stopname != "default" and is_dark:
            for key in ('paper', 'bg'):
                v = resolve(pal.get(key, ''), pal)
                if v.lower() in ('#000', '#000000'):
                    out["H2"].append(f"[{stopname}] pure black background")
            if resolve(pal.get('ink', ''), pal).lower() in ('#fff', '#ffffff'):
                out["H2"].append(f"[{stopname}] pure white ink")
        # H1 element-aware contrast
        for sel, props in R.items():
            # only evaluate rules active in this stop (default rules + this stop's overrides)
            if 'body.' in sel:
                if stopname == "default" or f'body.{stopname}' not in sel: continue
            if 'color' not in props: continue
            # cascade: if this stop overrides the same selector-tail with its own color,
            # the base rule is not what renders in this stop — skip it (else false HALT).
            if stopname != "default" and 'body.' not in sel:
                overridden = any(
                    s.startswith(f'body.{stopname} ') and s.split(f'body.{stopname} ',1)[1]==sel
                    and ('color' in R.get(s, {}))
                    for s in R)
                if overridden: continue
            fg = hex2rgb(resolve(props['color'], pal))
            if not fg: continue
            # element's own background: same-selector first, then walk the ancestor
            # chain (nearest styled ancestor grounds a descendant selector), then page.
            own_bg = None
            def bg_of(cand):
                props_c = R.get(cand, {})
                # Prefer an explicit background-color; then try the background shorthand.
                # A gradient/url shorthand won't hex-resolve, so fall through to
                # background-color rather than failing to page (gradient+solid-fallback bug).
                for key in ('background-color', 'background'):
                    bgv = props_c.get(key)
                    if not bgv: continue
                    c = hex2rgb(resolve(bgv.split()[0], pal))
                    if c: return c
                return None
            # 1: the selector itself
            own_bg = bg_of(sel)
            grounded_by = 'own' if own_bg else None

            # 1b: the element's OWN BASE RULE.
            #
            # BUG 6 (found 2026-07-11). Evaluating 'body.warm .tool .brasstag', the
            # sweep found no background on that full selector and walked to the
            # ancestor '.tool' (dark --surface) — reporting near-black ink as
            # INVISIBLE at 1.2:1. But the element paints ITSELF: the base rule
            # '.brasstag' declares background:var(--brass-d), which the warm stop
            # redefines to #f0c357 (light gold). True contrast: 11.6:1. Fine.
            #
            # An element's own background always wins over any ancestor. Check the
            # base rule (last simple token, pseudo/state stripped) before walking up.
            # The base rule may be written bare ('.brasstag') OR as a descendant
            # ('.tool .brasstag'). Match by TAIL: any rule whose own key-class is the
            # same and which paints a background is this element painting itself.
            if not own_bg:
                base_cls = sel_key_class(sel)
                if base_cls:
                    for cand in ('.' + base_cls,):
                        own_bg = bg_of(cand)
                        if own_bg: grounded_by = f'base:{cand}'; break
                    if not own_bg:
                        for k in R:
                            if k == sel: continue
                            if sel_key_class(k) != base_cls: continue
                            if 'body.' in k: continue          # stop-specific, not base
                            # BUG 7 (2026-07-13, Funny Boney's). Same key-class does NOT
                            # mean same element. Two guards, or the sweep invents HALTs
                            # and trains the studio to break working files:
                            #
                            # (a) STATE BOUNDARY. '.lens-btn' declares the UNPRESSED text
                            #     colour; '.lens-btn[aria-pressed=true]' paints the PRESSED
                            #     background. They never coexist. Grounding base text on a
                            #     state background reported hand-tuned 12:1 buttons as 1.4:1.
                            if ('[' in k) != ('[' in sel): continue
                            if (':' in k) != (':' in sel):  continue
                            # (b) COMPOUND vs DESCENDANT. '.part .pred' (a caption div) and
                            #     '.fill.pred' (a progress-bar fill) collide on key-class
                            #     'pred' and are unrelated elements. A compound selector
                            #     (.a.b, no space) cannot ground a descendant one (.a .b).
                            if (' ' in k.strip()) != (' ' in sel.strip()): continue
                            c = bg_of(k)
                            if c:
                                own_bg, grounded_by = c, f'base:{k}'
                                break

            # 2: REAL DOM ancestors (nearest-first). Catches BEM prefixes
            #    ('.mh-name' inside '.mh') that a string walk can never see.
            if not own_bg:
                for anc in dom_ancestor_bgs(sel, DOM):
                    own_bg = bg_of(anc)
                    if own_bg:
                        grounded_by = f'dom:{anc}'
                        break

            # 2b: BEM-prefix fallback for JS-injected nodes the static DOM can't see.
            if not own_bg:
                for anc in bem_prefix_chain(sel):
                    own_bg = bg_of(anc)
                    if own_bg:
                        grounded_by = f'bem:{anc}'
                        break

            # 2c: WITHDRAWN. A component-family guess ('.lum-poem' grounded against
            #     sibling '.lum-hero') is UNSOUND: it grounds against a background the
            #     element may never sit on, and it INVENTED 20+ new false HALTs when
            #     tried (2026-07-11). An auditor must not guess. When ancestry is
            #     genuinely unknowable from static analysis, say so — see UNGROUNDED.

            # 3: string walk — descendant selectors ('.foot a' -> '.foot').
            #    Kept as fallback for when the DOM can't answer (JS-injected nodes).
            if not own_bg:
                toks = sel.split()
                for k in range(len(toks)-1, 0, -1):
                    anc = " ".join(toks[:k])
                    own_bg = bg_of(anc)
                    if own_bg: grounded_by = f'sel:{anc}'; break
                    if not own_bg:
                        own_bg = bg_of(toks[k-1])
                        if own_bg: grounded_by = f'sel:{toks[k-1]}'; break

            # 4: BODY. The bottom of the cascade.
            #
            # BUG 7 (found 2026-07-14, by canary). The walk checked the selector,
            # the base rule, DOM ancestors, BEM prefixes, and descendant strings —
            # and NEVER CHECKED `body`. So an element sitting DIRECTLY on the page
            # background (the single most common case in a single-file page) found
            # no ancestor, fell to 'page?', and was downgraded to a WARN.
            #
            # The canary was `.note { color: var(--ghost) }` on `body { background:
            # var(--paper) }` — white-on-white, 1.1:1, declared three lines apart in
            # plain CSS. The sweep MEASURED it correctly at 1.1:1 INVISIBLE and then
            # filed it as an unproven suspicion. A brand-new file with unreadable
            # text passed the floor.
            #
            # `body` is not a GUESS. It is the cascade. If nothing between the
            # element and the root paints a background, the body paints it. That is
            # not an assumption about a JS-injected node — it is how CSS works.
            #
            # The honesty rule (below) is RIGHT and stays. But it was firing on
            # grounds that were never actually unknowable, which turned real HALTs
            # into warnings. TICK 4 warned about exactly this: "a gate that stops
            # false-positiving by becoming blind is not repaired; it is broken in
            # the other direction." It was. This is that repair.
            if not own_bg:
                for cand in ('body', 'html', ':root'):
                    own_bg = bg_of(cand)
                    if own_bg:
                        grounded_by = 'body'
                        break

            # HONESTY RULE (2026-07-11). If no ancestor could be resolved, the
            # element's true background is UNKNOWN — most often a JS-injected node
            # sitting on a painted container the static tree cannot show us.
            # Asserting the page background there is a GUESS, and that guess is
            # what manufactured the phantom-HALT flood that trained the founder to
            # distrust this auditor. An auditor that cries wolf is worse than none.
            #
            # So: a failure we can PROVE (grounded) is an H1 HALT.
            # A failure we merely SUSPECT (ungrounded) is a WARN, named as unproven.
            ground = own_bg if own_bg else bg_page
            if not own_bg: grounded_by = 'page?'
            r = ratio(fg, ground)
            if r < 4.5:
                sev = "INVISIBLE" if r < 2 else "low"
                line = f"[{stopname}] {sel[:50]} color {props['color'].strip()[:18]} = {r:.1f}:1 ({sev}, ground={grounded_by})"
                if own_bg:
                    out["H1"].append(line)            # PROVEN against a real ground
                else:
                    out["WARN"].append("UNGROUNDED " + line + " — background unresolved (likely JS-injected); verify by eye")

    # --- H6: REFERENCE-STALENESS (TICK 3, locked 2026-07-11) ---
    #
    # Confluence rendered SIX institutional outcomes. MassBay publishes SEVEN — and the
    # six it named were a pre-revision set, two revisions stale. Right format, plausible
    # names, real-sounding, completely wrong. Nothing in the file or the pipeline knew the
    # data had expired, because nothing ever asked.
    #
    # Any file carrying institutional reference data must name its SOURCE and a
    # LAST-VERIFIED date, in-file. A file that cannot say where its facts came from and
    # when cannot be trusted to be current.
    # Institution-specific markers only. Generic words ('outcome', 'policy') appear in
    # games and fire falsely — warriors-fantasy-arcade tripped the first draft of this
    # check. The signal is a file asserting facts ABOUT AN INSTITUTION.
    REF_MARKERS = (
        'islo', 'slo ', 'graduation competency', 'graduation competencies',
        'learning outcome', 'course outcome', 'program outcome',
        'rubric', 'syllab', 'prerequisite', 'accreditation', 'norming',
    )
    vis_txt = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', src).lower()
    carries_ref = sum(vis_txt.count(m) for m in REF_MARKERS) >= 6
    if carries_ref:
        has_src  = re.search(r'data-source\s*=|source:\s*|\bsource\b\s*[:=]', src, re.I)
        has_date = re.search(
            r'data-verified\s*=|last[- ]verified|verified[: ]\s*20\d\d|as of\s+\w+\s+20\d\d',
            src, re.I)
        if not (has_src and has_date):
            missing = []
            if not has_src:  missing.append('source')
            if not has_date: missing.append('last-verified date')
            out["H6"].append(
                "institutional reference data with no " + " and no ".join(missing) +
                " — cannot be trusted to be current (TICK 3)")

    # --- H7: OFFLINE FLOOR (locked 2026-07-11) ---
    #
    # Dad Energy shipped on the public internet for WEEKS pulling Google Fonts from a CDN.
    # Single-file-offline is studio law. On a plane, on bad campus wifi, or the day the CDN
    # changes an API, the file degrades. Nobody caught it: the game lived on a lane nothing
    # swept, in a silo nothing checked.
    #
    # ARITHMETIC, not judgment: count external hosts. Any is a HALT.
    ext = set()
    for m in re.finditer(r"""(?:href|src)\s*=\s*["']https?://([^/"'\s]+)""", src):
        ext.add(m.group(1))
    for m in re.finditer(r"""fetch\s*\(\s*["']https?://([^/"'\s]+)""", src):
        ext.add(m.group(1))
    for h in sorted(ext):
        out["H7"].append("OFFLINE FLOOR BROKEN - external host " + h + " (single-file-offline is law)")

    # --- H8: THE FILE DISAGREES WITH ITSELF (locked 2026-07-11) ---
    #
    # Confluence v44's in-file banner still reads "v43" - the commit changed content without
    # bumping the banner. A human reading the file is lied to BY THE FILE. The md5 cannot lie;
    # a hand-typed banner can. Two different version banners in one file means at least one
    # is wrong.
    ban = set(re.findall(r"\bv(\d{1,3})\s*\(20\d\d-\d\d-\d\d\)", src))
    if len(ban) > 1:
        out["H8"].append("FILE DISAGREES WITH ITSELF - conflicting version banners: v"
                         + ", v".join(sorted(ban)))

    # --- WARN class ---
    if css and ':focus-visible' not in css and ':focus' not in css:
        out["WARN"].append("no focus style")
    if '<script' in src and 'scrollTo(0' not in src:
        out["WARN"].append("no scroll-reset")
    vis = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', src)
    if re.search(r'[\U0001F000-\U0001FAFF\u2600-\u26FF]', vis):
        out["WARN"].append("emoji in visible text")
    return out

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else '/mnt/project'
    files = sorted(glob.glob(os.path.join(target, '*.html')))
    halts = 0
    for f in files:
        r = sweep(f)
        issues = [(k, v) for k, v in r.items() if v]
        if not issues: continue
        hard = any(k.startswith('H') for k, v in issues if v)
        if hard: halts += 1
        print(f"\n{'HALT' if hard else 'warn'}  {os.path.basename(f)}")
        for k, msgs in issues:
            for m in msgs[:6]:
                print(f"   {k}: {m}")
            if len(msgs) > 6: print(f"   {k}: (+{len(msgs)-6} more)")
    print(f"\n=== {halts} files at HALT of {len(files)} swept ===")

if __name__ == '__main__':
    main()
