/* ============================================================================
   TSP MOBILE — Tight Spiral Studios shared mobile controls + navigation
   ----------------------------------------------------------------------------
   One drop-in file. Include on any game page:

       <script>
         window.TSP_MOBILE = {
           home: "index.html",              // where "Home" goes (default: index.html)
           back: "cliche-cowpaths.html",    // optional "Back" target
           controls: [                       // optional on-screen gamepad
             { label:"◀", key:"ArrowLeft",  hold:true, side:"left"  },
             { label:"▶", key:"ArrowRight", hold:true, side:"left"  },
             { label:"THRUST", key:"ArrowUp", hold:true, side:"right" },
             { label:"FIRE", key:" ", side:"right" }   // no hold => tap
           ]
         };
       </script>
       <script src="tsp-mobile.js" defer></script>

   What it does
   ------------
   • Detects touch / coarse-pointer / small-screen devices and tags <html>
     with .tsp-touch / .tsp-mobile so CSS (this file's or yours) can adapt.
   • Renders an on-screen gamepad on touch devices whose buttons dispatch
     SYNTHETIC keyboard events matching each game's existing key handlers —
     so no game logic has to be rewritten. "hold" buttons fire keydown on
     press and keyup on release (movement / thrust); tap buttons fire a
     quick keydown+keyup (fire / rotate / drop).
   • Injects a consistent Home / Back navigation chip on every page, so no
     game is a dead end on a phone.

   Safe to include everywhere: if a page sets no `controls`, only the nav
   chip appears. Everything is a no-op-friendly progressive enhancement.
   ========================================================================= */
(function () {
  "use strict";

  var d = document, root = d.documentElement, cfg = window.TSP_MOBILE || {};

  /* ---- Device detection --------------------------------------------------- */
  var hasTouch = ("ontouchstart" in window) ||
                 (navigator.maxTouchPoints > 0) ||
                 (navigator.msMaxTouchPoints > 0);
  var coarse   = !!(window.matchMedia && matchMedia("(pointer: coarse)").matches);
  var narrow   = Math.min(screen.width || 9999, screen.height || 9999) < 820;
  var isMobile = hasTouch && (coarse || narrow);

  root.classList.add(hasTouch ? "tsp-touch" : "tsp-no-touch");
  if (isMobile) root.classList.add("tsp-mobile");

  /* ---- Synthetic keyboard dispatch --------------------------------------- */
  // Games listen on window (or document) for keydown/keyup and read e.key.
  var evTarget = (cfg.target === "document") ? d : window;

  function dispatchKey(type, key) {
    var ev;
    try {
      ev = new KeyboardEvent(type, {
        key: key, code: codeFor(key),
        bubbles: true, cancelable: true, view: window
      });
    } catch (e) {
      // Legacy fallback
      ev = d.createEvent("Event");
      ev.initEvent(type, true, true);
      try { ev.key = key; } catch (_) {}
    }
    evTarget.dispatchEvent(ev);
  }

  function codeFor(key) {
    switch (key) {
      case "ArrowLeft":  return "ArrowLeft";
      case "ArrowRight": return "ArrowRight";
      case "ArrowUp":    return "ArrowUp";
      case "ArrowDown":  return "ArrowDown";
      case " ":          return "Space";
      case "Enter":      return "Enter";
      case "Shift":      return "ShiftLeft";
      default:
        if (key && key.length === 1) return "Key" + key.toUpperCase();
        return "";
    }
  }

  /* ---- Styles (injected once) -------------------------------------------- */
  function injectStyles() {
    if (d.getElementById("tsp-mobile-style")) return;
    var css = [
      /* Navigation chip — always available, subtle on desktop */
      ".tsp-nav{position:fixed;top:max(10px,env(safe-area-inset-top));left:max(10px,env(safe-area-inset-left));",
        "z-index:2147483000;display:flex;gap:8px;font-family:'Helvetica Neue',Arial,sans-serif}",
      ".tsp-nav a{display:inline-flex;align-items:center;gap:.4em;text-decoration:none;",
        "padding:.5em .85em;border-radius:999px;font-size:13px;font-weight:600;letter-spacing:.04em;",
        "color:#f4f1e8;background:rgba(20,18,15,.66);border:1px solid rgba(255,207,90,.45);",
        "-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);line-height:1;",
        "box-shadow:0 4px 14px rgba(0,0,0,.35);transition:background .15s,border-color .15s,transform .08s}",
      ".tsp-nav a:hover,.tsp-nav a:focus-visible{background:rgba(40,34,24,.9);border-color:#ffcf5a;outline:none}",
      ".tsp-nav a:active{transform:translateY(1px)}",
      "@media (min-width:900px) and (pointer:fine){.tsp-nav{opacity:.55}.tsp-nav:hover{opacity:1}}",

      /* Nav integrated into the studio's shared .topbar (no overlap) */
      ".tsp-barnav{display:inline-flex;align-items:center;gap:.35rem;margin-right:.25rem;flex:none}",
      ".tsp-barnav a{display:inline-flex;align-items:center;gap:.3em;text-decoration:none;color:inherit;",
        "font-family:inherit;font-weight:800;font-size:.82rem;letter-spacing:.02em;line-height:1;",
        "padding:.4em .7em;border-radius:999px;border:1px solid currentColor;opacity:.85;",
        "background:transparent;white-space:nowrap;transition:opacity .12s,background .12s}",
      ".tsp-barnav a:hover,.tsp-barnav a:focus-visible{opacity:1;background:rgba(127,127,127,.18);outline:none}",
      ".tsp-barnav a:active{transform:translateY(1px)}",
      /* Keep the shared bar on one row once Home/Back are added: title ellipsizes */
      ".tsp-touch .topbar{gap:.4rem}",
      ".tsp-touch .topbar .wm{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0;flex:1 1 auto}",

      /* Gamepad — only rendered on touch devices */
      ".tsp-pad{position:fixed;left:0;right:0;bottom:0;z-index:2147482000;",
        "display:flex;justify-content:space-between;align-items:flex-end;pointer-events:none;",
        "padding:0 max(14px,env(safe-area-inset-left)) max(16px,env(safe-area-inset-bottom)) max(14px,env(safe-area-inset-right));",
        "font-family:'Helvetica Neue',Arial,sans-serif;touch-action:none}",
      ".tsp-cluster{display:flex;gap:12px;pointer-events:none;align-items:flex-end;flex-wrap:wrap;max-width:46vw}",
      ".tsp-cluster.right{justify-content:flex-end}",
      ".tsp-btn{pointer-events:auto;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none;",
        "touch-action:none;min-width:62px;min-height:62px;padding:0 14px;border-radius:16px;",
        "display:flex;align-items:center;justify-content:center;text-align:center;",
        "font-size:15px;font-weight:700;letter-spacing:.03em;color:#f4f1e8;",
        "background:rgba(24,20,15,.6);border:1.5px solid rgba(255,207,90,.5);",
        "-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);",
        "box-shadow:0 6px 18px rgba(0,0,0,.4);transition:background .06s,transform .06s;cursor:pointer}",
      ".tsp-btn.big{min-width:82px;min-height:82px;font-size:16px}",
      ".tsp-btn:active,.tsp-btn.on{background:rgba(255,207,90,.9);color:#1a0d09;transform:scale(.94)}",
      /* Hide gamepad on non-touch so desktop keeps keyboard feel */
      ".tsp-no-touch .tsp-pad{display:none}",

      /* Rotate-for-more-room hint — canvas games only, portrait phones only */
      ".tsp-rot{position:fixed;left:50%;transform:translateX(-50%);top:calc(72px + env(safe-area-inset-top));",
        "z-index:2147482500;display:none;align-items:center;gap:.55em;padding:.5em .55em .5em .9em;",
        "border-radius:999px;background:rgba(24,20,15,.86);color:#f4f1e8;",
        "border:1px solid rgba(255,207,90,.5);white-space:nowrap;",
        "font:600 12px/1 'Helvetica Neue',Arial,sans-serif;letter-spacing:.02em;",
        "-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);box-shadow:0 4px 14px rgba(0,0,0,.4)}",
      ".tsp-rot .rk{font-size:14px;color:#ffcf5a}",
      ".tsp-rot button{background:none;border:none;color:inherit;font-size:16px;line-height:1;",
        "padding:0 .15em;margin:0;cursor:pointer;opacity:.65}",
      ".tsp-rot button:active{opacity:1}",
      "@media (orientation:portrait){.tsp-touch .tsp-rot{display:inline-flex}}",
      ".tsp-rot-dismissed .tsp-rot{display:none!important}"
    ].join("");
    var s = d.createElement("style");
    s.id = "tsp-mobile-style";
    s.textContent = css;
    d.head.appendChild(s);
  }

  /* ---- Navigation (Home / Back) ------------------------------------------ */
  function makeLink(href, label, aria) {
    var a = d.createElement("a");
    a.href = href; a.innerHTML = label;
    a.setAttribute("aria-label", aria);
    return a;
  }

  function buildNav() {
    if (cfg.nav === false) return;
    if (d.querySelector(".tsp-nav, .tsp-barnav")) return;

    var home = cfg.home === undefined ? "index.html" : cfg.home;
    var links = [];
    if (cfg.back) links.push(makeLink(cfg.back, "‹ Back", "Back"));
    if (home)     links.push(makeLink(home, "⌂ Home", "Home"));
    if (!links.length) return;

    // Prefer integrating into the studio's shared sticky header if present —
    // avoids overlapping page titles and matches each page's palette.
    var bar = cfg.floatNav ? null : d.querySelector(".topbar");
    if (bar) {
      var wrap = d.createElement("span");
      wrap.className = "tsp-barnav";
      links.forEach(function (l) { wrap.appendChild(l); });
      bar.insertBefore(wrap, bar.firstChild);
      return;
    }

    // Otherwise: floating chip, and reserve top space on scrollable pages so
    // it never covers the header/title.
    var nav = d.createElement("nav");
    nav.className = "tsp-nav";
    nav.setAttribute("aria-label", "Site navigation");
    links.forEach(function (l) { nav.appendChild(l); });
    d.body.appendChild(nav);
    reserveTopSpace();
  }

  function reserveTopSpace() {
    if (!hasTouch) return;                 // desktop keeps its exact layout
    // Skip full-viewport apps (canvas games, fixed overlays) — the chip sits
    // in their letterbox margin and body padding would distort them.
    var cs = getComputedStyle(d.body);
    if (cs.overflowY === "hidden" || cs.overflowX === "hidden") return;
    var scrolls = root.scrollHeight > (window.innerHeight + 4);
    if (!scrolls) return;
    var pad = parseFloat(cs.paddingTop) || 0;
    d.body.style.paddingTop = (pad + 58) + "px";
  }

  /* ---- Gamepad ------------------------------------------------------------ */
  function buildPad() {
    if (!hasTouch) return;                       // keyboard devices skip it
    if (!cfg.controls || !cfg.controls.length) return;
    if (d.querySelector(".tsp-pad")) return;

    var pad = d.createElement("div");
    pad.className = "tsp-pad";
    var left  = d.createElement("div"); left.className  = "tsp-cluster left";
    var right = d.createElement("div"); right.className = "tsp-cluster right";
    pad.appendChild(left); pad.appendChild(right);

    cfg.controls.forEach(function (c) {
      var btn = d.createElement("button");
      btn.type = "button";
      btn.className = "tsp-btn" + (c.big ? " big" : "");
      btn.innerHTML = c.label || "";
      btn.setAttribute("aria-label", c.aria || c.label || c.key);
      bindButton(btn, c);
      (c.side === "left" ? left : right).appendChild(btn);
    });

    d.body.appendChild(pad);
  }

  function bindButton(btn, c) {
    var key = c.key, held = false;

    function press(e) {
      if (e) { e.preventDefault(); e.stopPropagation(); }
      if (c.hold) {
        if (held) return;
        held = true;
        btn.classList.add("on");
        dispatchKey("keydown", key);
      } else {
        // tap: quick down/up so edge-triggered actions (fire/rotate/drop) fire once
        btn.classList.add("on");
        dispatchKey("keydown", key);
        setTimeout(function () { dispatchKey("keyup", key); }, 24);
        setTimeout(function () { btn.classList.remove("on"); }, 90);
      }
    }
    function release(e) {
      if (e) e.preventDefault();
      if (c.hold && held) {
        held = false;
        btn.classList.remove("on");
        dispatchKey("keyup", key);
      }
    }

    if (window.PointerEvent) {
      btn.addEventListener("pointerdown", function (e) {
        try { btn.setPointerCapture(e.pointerId); } catch (_) {}
        press(e);
      });
      btn.addEventListener("pointerup", release);
      btn.addEventListener("pointercancel", release);
      btn.addEventListener("lostpointercapture", release);
    } else {
      btn.addEventListener("touchstart", press, { passive: false });
      btn.addEventListener("touchend", release);
      btn.addEventListener("touchcancel", release);
      btn.addEventListener("mousedown", press);
      btn.addEventListener("mouseup", release);
      btn.addEventListener("mouseleave", release);
    }
    // Safety: releasing a held key if the page loses focus
    window.addEventListener("blur", release);
  }

  /* ---- Rotate hint -------------------------------------------------------- */
  function buildRotateHint() {
    if (!hasTouch) return;
    if (cfg.rotateHint === false) return;
    if (!cfg.controls || !cfg.controls.length) return;   // canvas games only
    if (d.querySelector(".tsp-rot")) return;
    var hint = d.createElement("div");
    hint.className = "tsp-rot";
    hint.setAttribute("role", "note");
    hint.innerHTML = '<span class="rk">↻</span>' +
      '<span>Turn sideways for more room</span>' +
      '<button type="button" aria-label="Dismiss">×</button>';
    hint.querySelector("button").addEventListener("click", function () {
      root.classList.add("tsp-rot-dismissed");
    });
    d.body.appendChild(hint);
  }

  /* ---- Boot --------------------------------------------------------------- */
  function boot() {
    injectStyles();
    buildNav();
    buildPad();
    buildRotateHint();
  }

  if (d.readyState === "loading") {
    d.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  // Expose a tiny API for pages that want to toggle the pad (e.g. hide on menus)
  window.TSPMobile = {
    isTouch: hasTouch,
    isMobile: isMobile,
    press: function (key) { dispatchKey("keydown", key); dispatchKey("keyup", key); },
    showPad: function (v) {
      var p = d.querySelector(".tsp-pad");
      if (p) p.style.display = v === false ? "none" : "";
    }
  };
})();
