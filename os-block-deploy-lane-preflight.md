# OS BLOCK — DEPLOY LANE PRE-FLIGHT

**Status:** locked 2026-07-10
**Origin:** the GitHub push in the Funny Boney's playtest session burned four turns and a screenshot on a dead/underpermissioned token — discovered only *after* clone, commit, and a failed push. This is not a one-off: **the container filesystem resets every session, so the token must be re-pasted every session.** That friction is now permanent unless it's systematized. This block systematizes it.
**Folds into:** OS §6 pipeline (deploy stage) + the session-open card. Not a new system — a gate on an existing lane.

---

## THE RULE

**Test the token before you use it.** Never clone-commit-push and discover the permission at the failure. One API call, ten seconds, run *first*:

```
curl -s -H "Authorization: Bearer $TOKEN" \
  https://api.github.com/repos/walshero/TIGHT-SPIRAL-STUDIOS \
  | python3 -c "import sys,json; print('push:', json.load(sys.stdin).get('permissions',{}).get('push'))"
```

Read the result:
- **`push: True`** → lane is open. Clone, commit, push, POST-TICK.
- **`push: None` / `push: False`** → token is alive but **underpermissioned**. Contents is read-only. Send the founder to the recipe below.
- **`401`** → token is **dead** (revoked, regenerated, or invalid). New token needed.

Do not proceed on anything but `push: True`.

## THE TOKEN RECIPE (founder-facing, exact)

When a new token is needed, give these steps — never make the founder hunt the settings screen twice.

**Path:** github.com → **avatar (top-right)** → **Settings** → left sidebar, scroll to bottom → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**

**Four settings, in the order they appear on the page:**

1. **Resource owner:** `walshero`
2. **Expiration:** **No expiration** — founder ruling 2026-07-10. He revokes manually rather than get locked out mid-deploy. Do not re-litigate; do not "recommend" 30 days again.
3. **Repository access:** **Only select repositories** → `walshero/TIGHT-SPIRAL-STUDIOS`
   *(Never "Public repositories" — that option is read-only by design and will always 403 on push, regardless of permissions set below. This is the trap that cost the first token.)*
4. **Permissions:** this section starts at **zero** and is easy to miss. Click **"+ Add permissions"** (right side of the Permissions bar) → add **Contents** → set its dropdown to **Read and write**. Metadata auto-adds as read-only; leave it.

**Then:** green **Generate token** button at the **bottom** of the page (long scroll past the permission list). GitHub shows the string **once** — copy it immediately.

## TOKEN HANDLING (hard floor)

- Token lives **in the chat only**. Never written to memory, never to a file, never committed.
- Container resets between sessions → **founder re-pastes each session**. This is expected, not a failure.
- Revocable anytime at the same Fine-grained tokens screen. Founder's chosen safety model: no expiry + manual kill.

## THE PUSH (once `push: True`)

1. Clone with token in the HTTPS remote
2. Copy file from `/mnt/user-data/outputs`
3. Commit, `git push origin main`
4. **POST-TICK, non-negotiable:** `curl` the file back from `raw.githubusercontent.com` and **md5-match against local**. "Pushed" is never proof. Byte-match is proof.

## SHIP GATE STILL GOVERNS

Pushing to the repo ≠ shipping. A file may live at its URL for cold play while **remaining unlinked from `index.html`** (the student front door) until GATE 1 (founder cold phone play) and GATE 2 (Studio Eyes) both clear. Unlisted is not the same as shipped.

---

## FOLD-IN: CONVENING VISIBILITY (session-open card)

Separate fix, same session, same root — **silence hid a miss.**

The Product Convening is supposed to auto-fire on the words *game / build / make / playtest*. In the Funny Boney's session it **never fired**, and nothing said so, because the convening runs silent when it has no fork to surface. Silent-and-ran and never-fired look identical.

**Fix:** the session-open card states the convening's status in one line, always:

> `Convening: ran clean` — or — `Convening: skipped — medium pre-decided by founder (wrap existing v3)`

One line. Founder can then veto a skip. Silence may mean "no fork," never "never fired."

---

*Both fixes are folds into existing blocks, not new systems. Read this before any deploy.*
