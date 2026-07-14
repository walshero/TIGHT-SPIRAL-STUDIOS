#!/usr/bin/env python3
"""
COMFORT SWEEP — graft the canonical five-stop control onto every build.

THE DRIFT THIS FIXES (measured 2026-07-14, not remembered)
-----------------------------------------------------------
Across 33 files: ELEVEN different comfort-stop names.
    softer (16 files) · warm (13) · on (3) · revealing (3) · daylight (2)
    a11y-contrast (2) · bigtext (2) · a11y-large-text · warmdark · hc · big

Across the six front-page games: SIX DIFFERENT SYSTEMS.
    the-console          only "big"          — no comfort stop at all
    choose-your-leader   softer, daylight
    the-tell             softer, warm        — the only file with a "Comfort" button
    the-viscosity        NONE
    cliche-cowpaths      NONE — no :root, no tokens, nothing
    funny-boneys         softer, daylight + a SEPARATE Motion knob, ABOVE the scene

And four different names for the ground token: void · paper · bg · surface.

A control that means something different in every room is not a control. It is a
thing the player must relearn on every page, and relearning is friction, and
friction on an interface is the tax this studio exists to abolish.

WHY THIS IS A SCRIPT AND NOT A FIND-AND-REPLACE
-----------------------------------------------
A blind graft would break four of the six. Each game names its ground differently.
Writing `--paper` into a file whose ground is `--void` produces a control that
looks correct, passes a naive check, and renders invisible.

So this reads EACH FILE'S OWN TOKENS and adapts to them. And where it cannot
understand a file, it REFUSES — it does not guess. An auditor that guesses is the
disease (BUG 7: Studio Eyes measured a 1.1:1 defect correctly and then filed it as
a suspicion, so an unreadable file passed the floor).

    A file this script cannot read is a file a human must open. That is not a
    failure of the script. That is the script telling the truth.

USAGE
    python3 comfort-sweep.py <file.html> [--write]     # one file; dry-run by default
    python3 comfort-sweep.py --list                    # what each file currently has
"""

import sys, os, re, glob

# ── THE FIVE STOPS. The same five, everywhere, forever. ──────────────────────
STOPS_JS = """  var STOPS = [
    { cls:"",             label:"Default"      },
    { cls:"softer",       label:"Softer"       },
    { cls:"warmdark",     label:"Warm dark"    },
    { cls:"daylight",     label:"Daylight"     },
    { cls:"clear-reader", label:"Clear Reader" }
  ];"""


def tokens_of(src):
    """Read the file's OWN :root. Never assume a name."""
    css = ''.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', src, re.I))
    m = re.search(r':root\s*\{([^}]*)\}', css)
    if not m:
        return None
    return dict(re.findall(r'--([\w-]+)\s*:\s*([^;]+);', m.group(1)))


def ground_token(v):
    """Which token is this file's PAGE BACKGROUND? Ask the file, don't guess."""
    for k in ('paper', 'bg', 'surface', 'void', 'canvas', 'base', 'page'):
        if k in v:
            return k
    return None


def ink_token(v):
    for k in ('ink', 'text', 'fg', 'ink-1', 'foreground'):
        if k in v:
            return k
    return None


def build_css(ground, ink, existing):
    """The four palette stops, written in THIS FILE'S token names.

    Only Clear Reader is universal — it overrides everything by force, because it
    is not a palette, it is the design being taken OFF.
    """
    has = lambda n: n in existing
    ink2 = 'ink-2' if has('ink-2') else ('ink-soft' if has('ink-soft') else None)
    ink3 = 'ink-3' if has('ink-3') else ('muted' if has('muted') else None)

    def stop(cls, pairs, note):
        lines = [f"body.{cls}{{  /* {note} */"]
        for k, val in pairs:
            if k:
                lines.append(f"  --{k}: {val};")
        lines.append("}")
        return "\n".join(lines)

    softer = stop("softer", [
        (ground, "#f6f3ec"), (ink, "#24292f"),
        (ink2, "#48505c"), (ink3, "#5f6875"),
    ], "STOP 2 — same design, calmer. Lower push, still far above floor.")

    warmdark = stop("warmdark", [
        (ground, "#16150f"), (ink, "#f2ede0"),
        (ink2, "#d3cbb8"), (ink3, "#a89f89"),
    ], "STOP 3 — warm charcoal, never #000. Max contrast BLOOMS on an RP retina.")

    daylight = stop("daylight", [
        (ground, "#ffffff"), (ink, "#000000"),
        (ink2, "#1a1a1a"), (ink3, "#333333"),
    ], "STOP 4 — maximum legibility. Bright rooms, projectors, bad screens.")

    return f"""
/* ═══ THE COMFORT STOPS — canonical, swept 2026-07-14 ═══════════════════════
   One button. Five stops. The same five in every room in the studio.
   Written in THIS FILE'S token names ({ground} / {ink}) — a graft, not a clobber.
   ═════════════════════════════════════════════════════════════════════════ */
{softer}

{warmdark}

{daylight}

/* ═══ STOP 5 — CLEAR READER ═════════════════════════════════════════════════
   Not a palette. The design taken OFF.

   What survives is what a screen reader actually receives: headings, lists,
   links, in document order. A sighted person has never seen that document —
   they do not know whether the thing they built has a spine, or whether the
   layout was doing all the work.

   Tap it, and the game becomes its own outline. If it is unplayable here, it is
   unplayable with a screen reader. No plugin, no expertise. One tap, and you are
   looking at the truth.

   MAKE THE INVISIBLE STRUCTURE VISIBLE. That is every game in this studio. This
   is that engine, pointed at the studio's own interface.
   ═════════════════════════════════════════════════════════════════════════ */
body.clear-reader{{
  background:#fff !important; color:#000 !important;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif !important;
  font-size:19px !important; line-height:1.65 !important;
  max-width:38em !important; margin:0 auto !important;
  padding:24px 20px 90px !important;
}}
body.clear-reader *:not(.cr-note):not(.cr-note *):not(.comfort):not(.comfort *){{
  all:revert;
  font-family:inherit !important;
  color:#000 !important; background:#fff !important; border-color:#767676 !important;
  box-shadow:none !important; text-shadow:none !important;
  animation:none !important; transition:none !important;
  position:static !important; float:none !important; max-width:100% !important;
}}
/* Decoration is not meaning. If it carries no information, it goes. */
body.clear-reader svg, body.clear-reader canvas, body.clear-reader video,
body.clear-reader [aria-hidden="true"]{{ display:none !important; }}
/* Structure must be VISIBLE — that is the entire point of this stop. */
body.clear-reader h1{{ font-size:30px !important; margin:24px 0 10px !important;
  border-bottom:3px solid #000 !important; padding-bottom:5px !important; }}
body.clear-reader h2{{ font-size:24px !important; margin:22px 0 8px !important;
  border-bottom:1px solid #767676 !important; padding-bottom:3px !important; }}
body.clear-reader h3{{ font-size:20px !important; margin:18px 0 6px !important; }}
body.clear-reader p, body.clear-reader li{{ font-size:19px !important; margin:0 0 13px !important; }}
body.clear-reader ul, body.clear-reader ol{{ padding-left:26px !important; margin:0 0 16px !important; }}
body.clear-reader li{{ list-style:disc !important; }}
body.clear-reader ol li{{ list-style:decimal !important; }}
body.clear-reader a{{ color:#0000ee !important; text-decoration:underline !important; }}
body.clear-reader a:visited{{ color:#551a8b !important; }}
body.clear-reader button, body.clear-reader select, body.clear-reader input{{
  font-size:18px !important; padding:11px 16px !important;
  border:2px solid #000 !important; border-radius:0 !important;
  background:#fff !important; color:#000 !important;
  margin:0 8px 8px 0 !important; display:inline-block !important;
  min-height:44px !important; cursor:pointer !important;
}}
body.clear-reader button[aria-pressed="true"]{{ background:#000 !important; color:#fff !important; font-weight:700 !important; }}
body.clear-reader :focus-visible{{ outline:4px solid #0000ee !important; outline-offset:2px !important; }}
body.clear-reader .cr-note{{
  display:block !important; border:3px solid #000 !important; background:#fff !important;
  color:#000 !important; padding:15px 17px !important; margin:0 0 26px !important;
  font-size:17px !important; line-height:1.5 !important;
}}
.cr-note{{ display:none; }}

/* ═══ THE BUTTON — a CORNER control. Never a wall. ═════════════════════════
   It lives bottom-right, over the scene, always reachable and never in front of
   it. The rule (locked 2026-06-29): the first screen is the SCENE. You change
   the comfort BECAUSE you have seen something and want to see it differently —
   not before you have seen anything at all, when the choice is meaningless.
   ═════════════════════════════════════════════════════════════════════════ */
.comfort{{
  position:fixed; right:14px; bottom:14px; z-index:9999;
  font:700 12.5px/1 ui-monospace,SFMono-Regular,Menlo,monospace;
  letter-spacing:.05em; padding:12px 15px; min-height:44px;
  background:var(--{ground}); color:var(--{ink});
  border:2px solid var(--{ink}); border-radius:2px; cursor:pointer;
  box-shadow:0 2px 10px rgba(0,0,0,.16);
}}
.comfort:focus-visible{{ outline:4px solid #0000ee; outline-offset:3px; }}
body.clear-reader .comfort{{
  position:static !important; display:block !important;
  margin:0 0 20px !important; box-shadow:none !important;
}}
@media (prefers-reduced-motion: reduce){{
  *{{ animation:none !important; transition:none !important; }}
}}
"""


CR_NOTE = """<div class="cr-note" role="note"><b>Clear Reader.</b> The design is off. This is the
document underneath &mdash; headings, lists, links, in the order a screen reader receives them.
<b>If this is hard to follow, it is hard to follow with a screen reader too.</b> Press the button
again to bring the design back.</div>
"""

BUTTON = """<button class="comfort" id="comfort">Comfort: <span id="comfort-label">Default</span></button>
"""

SCRIPT = """<script>
(function(){
  "use strict";
""" + STOPS_JS + """
  var i = 0;
  var btn = document.getElementById("comfort");
  var lab = document.getElementById("comfort-label");
  function apply(){
    for(var k=0;k<STOPS.length;k++){ if(STOPS[k].cls) document.body.classList.remove(STOPS[k].cls); }
    if(STOPS[i].cls) document.body.classList.add(STOPS[i].cls);
    lab.textContent = STOPS[i].label;
    /* A button announces what it will DO, not what it is. A screen-reader user
       pressing this needs to know where it takes them. */
    var next = STOPS[(i+1) % STOPS.length].label;
    btn.setAttribute("aria-label",
      "Comfort setting: " + STOPS[i].label + ". Press to switch to " + next + ".");
  }
  btn.addEventListener("click", function(){ i = (i+1) % STOPS.length; apply(); });
  /* NO STORAGE. Single-file, offline, zero-persistence is studio law. */
  apply();
})();
</script>
"""


def graft(path, write=False):
    src = open(path, encoding='utf-8', errors='replace').read()
    name = os.path.basename(path)

    if 'id="comfort"' in src and 'clear-reader' in src:
        return (name, "SKIP", "already swept")

    v = tokens_of(src)
    if not v:
        return (name, "REFUSE", "no :root — this file has no token system. "
                                "A human must open it. I do not guess.")
    g = ground_token(v)
    k = ink_token(v)
    if not g or not k:
        return (name, "REFUSE", f"cannot find ground/ink tokens (have: {list(v)[:5]}). "
                                f"I do not guess.")

    # 1. strip the OLD comfort machinery so two controls never coexist
    out = src
    out = re.sub(r'<button[^>]*class="[^"]*\bknob\b[^"]*"[\s\S]*?</button>\s*', '', out)
    out = re.sub(r'<div class="knobs"[\s\S]*?</div>\s*', '', out)

    # 2. CSS — append to the LAST style block so it wins the cascade
    css_add = build_css(g, k, v)
    m = None
    for m in re.finditer(r'</style>', out, re.I):
        pass
    if not m:
        return (name, "REFUSE", "no </style> — cannot place the stops")
    out = out[:m.start()] + css_add + out[m.start():]

    # 3. the note goes FIRST inside body; the button goes LAST. Never the reverse:
    #    a control above the content is a WALL.
    bm = re.search(r'<body[^>]*>', out, re.I)
    if not bm:
        return (name, "REFUSE", "no <body>")
    out = out[:bm.end()] + "\n" + CR_NOTE + out[bm.end():]

    sm = re.search(r'<script', out, re.I)
    ins = sm.start() if sm else out.lower().rfind('</body>')
    if ins < 0:
        return (name, "REFUSE", "nowhere to place the button")
    out = out[:ins] + BUTTON + "\n" + SCRIPT + "\n" + out[ins:]

    if write:
        open(path, 'w', encoding='utf-8').write(out)
    return (name, "SWEPT", f"ground=--{g} ink=--{k}  ({len(out)-len(src):+,} B)")


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--list':
        for f in sorted(glob.glob('*.html')):
            s = open(f, encoding='utf-8', errors='replace').read()
            css = ''.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', s))
            st = sorted(set(re.findall(r'body\.([\w-]+)\s*\{', css)))
            print(f"  {f:<36} {','.join(st) if st else '(no stops)'}")
        sys.exit(0)

    write = '--write' in a
    files = [x for x in a if x.endswith('.html')]
    for f in files:
        n, verdict, why = graft(f, write)
        print(f"  {verdict:<7} {n:<34} {why}")
    if not write:
        print("\n  DRY RUN. Add --write to apply.")
