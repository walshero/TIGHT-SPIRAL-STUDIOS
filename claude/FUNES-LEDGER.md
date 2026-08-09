# NOT THE LEDGER. This path is a pointer, and it refuses on purpose.

**Canon is `FUNES-LEDGER.md` at repo root. Append there. Never here.**

## Why this file exists at all

The standing instructions tell every session to diff against the FUNES ledger *at this
path*. No file was here, in any lane the repo could reach, so the instruction resolved to
nothing every time it was followed. Belt tick 8 (`scope-gate.py`, armed 2026-08-09) measured
it and named this as one of three citations in the standing instructions that pointed at
files the trunk could not fetch. This file closes the address without forking the record.

## Why it is a pointer and not a mirror

**This exact shape has already destroyed appends once.** A shelf copy of the ledger existed
as a "mirror." Gates wrote the mirror instead of the repo. On 2026-08-05 two `en195-arcade`
rows landed on the mirror and nowhere else; the repo copy held three rows while the mirror
held five, and the divergence was not found until the Aleph pass of 2026-08-06 union-merged
them. An append-only file lost appends. That is the worst thing a ledger can do, and it was
caused by a second writable copy at a second address — this address.

So there is no second ledger. Two appendable ledgers is unrecoverable: they do not conflict,
they simply both look correct, and the union is only discoverable if somebody thinks to
look. The founder authorized the write lane; the write lane does not get a second ledger.

## What to actually do

- **Appending a row?** `FUNES-LEDGER.md` at repo root, via the git lane, byte-verified in the
  same turn. `stage-push.py` closes the transit path.
- **Diffing against the ledger at session start?** Read root. It is authoritative and it is
  the only copy that is.
- **Holding a shelf or Drive copy?** It is a cache. It lags. Compute canon from the repo.

## Do not "fix" this file by pasting the ledger into it

If a future session finds this pointer inconvenient and replaces it with rows, it will have
reproduced the 2026-08-05 defect deliberately, and the rows written here will be invisible
to every gate that routes to root. The inconvenience is the feature.
