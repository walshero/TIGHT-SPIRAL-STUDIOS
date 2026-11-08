#!/usr/bin/env python3
"""Signal Rider v0.13 (was Down the Nerve). Founder 2026-11-08 14:37: "Rename signal rider".
File path stays lab/down-the-nerve.html so bookmarks keep working. Base: canon v0.12 (853de9f4)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('853de9f4'), 'base is not canon v0.12'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)
rep('<title>Down the Nerve v0.12</title>', '<title>Signal Rider v0.13</title>')
rep('aria-label="Down the Nerve: you are a spark', 'aria-label="Signal Rider: you are a spark')
rep('<span class="name">Down the Nerve</span><span class="chip">v0.12</span>', '<span class="name">Signal Rider</span><span class="chip">v0.13</span>')
assert 'Down the Nerve' not in s
open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
