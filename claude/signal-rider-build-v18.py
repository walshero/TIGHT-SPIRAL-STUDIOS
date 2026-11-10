#!/usr/bin/env python3
"""Signal Rider v0.18. Founder 2026-11-10 16:04: "My end of game summary said I travelled 0 in 0."
Cause: in v0.10 a '//' comment was appended mid-line after the speedometer, which commented
out the distance and time counting on the same line. Since v0.10 run.realM and run.realMs never
moved: the HUD trip line read 0.00 m, 0.0 ms all ride, and the end card said 0 in 0.
Fix: the comment gets its own line. Base: canon v0.17 (a979d599)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('a979d599'), 'base is not canon v0.17'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)
rep('<title>Signal Rider v0.17</title>', '<title>Signal Rider v0.18</title>')
rep('<span class="chip">v0.17</span>', '<span class="chip">v0.18</span>')
rep("  var vReal=Math.min(120,run.v/(6.5*S.speed*rampF())*75); // the speedometer reads the fiber, not the onramp var mPer=L.realM/L.len;",
    "  // the speedometer reads the fiber, not the onramp\n  var vReal=Math.min(120,run.v/(6.5*S.speed*rampF())*75); var mPer=L.realM/L.len;")
open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
