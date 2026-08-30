# CREDENTIAL GRAVEYARD — a watch registry, not a vault

Built 2026-08-30. Supersedes nothing. Companion to the exposed-PAT item that has
been open in HANDOFF.md since mid-July.

## What this replaces

A reminder. The PAT rotation has been an open line item for roughly six weeks and
has already survived one nag. A second nag is not a new intervention. What follows
is a check: something that fires on its own and stops firing when the problem is
actually gone.

## The mechanism, and why it is honest

The question "did Matt rotate the token" is not computable from here. The question
"is the leaked token still alive" is. `GET https://api.github.com/user` with a
credential in the Authorization header returns 200 while that credential works and
401 once it does not.

Zapier halts a Zap run on a 4xx. So the notification step is only reachable while
the leak persists. Dead credential, dead Zap, silence. No filter, no state, no
bookkeeping — the absence of the alarm *is* the all-clear.

This was verified by execution, not assumed. An unauthenticated GET to that endpoint
through Webhooks by Zapier returned `Requires authentication` and errored the step.
That error is the whole load-bearing behavior.

Also verified by execution: Webhooks by Zapier is a Premium app and it runs on this
account. It was enabled and it executed a live request.

## Why a sheet and not a Zap per credential

Because the second leaked credential should be a row, not a build. The registry is
the durable object; the Zap is a loop over it. That is the only version of this
worth maintaining.

## The sheet

Title: CREDENTIAL GRAVEYARD — TSP watch registry
Drive ID: 1g3uhyoL5NtuzC_DWdYCtenS2yI-8aCrMhlA0Nb8PJA4
Owner: walshero@gmail.com (My Drive root)

Columns, row 1: label, exposure_date, owner, status, endpoint, auth_header_name,
auth_scheme, secret_ref, last_checked, last_status, notes

Row 2 is a banner, not data. It reads: THIS SHEET HOLDS NO SECRETS. It has no
exposure_date, so the filter described below skips it. That is deliberate — the
guard does real work on day one, which is how you find out whether it works.

Row 3 is the deploy PAT.

### The one rule this sheet has, and its check

A row belongs here only if the credential is already burned and awaiting confirmed
death. This is a graveyard, not an inventory. The failure mode of any registry like
this is that it quietly becomes the place where live credentials get parked, and
then a Drive doc that syncs to a laptop and is one share-link from public is holding
production secrets.

The rule that stops that is arithmetic, not prose: **exposure_date is required**, and
the Zap filters on it. A credential with no exposure date has nothing to be exposed
about and does not belong in a graveyard. A live credential someone tries to park
here has no exposure date, gets no row that passes the filter, and gets no watch —
so parking it here buys nothing.

### Where the secret actually lives

Not in the sheet. `secret_ref` names a Zapier Storage key; the value sits in Storage
by Zapier. The sheet stays safe to open, safe to share, safe to sync.

## Building the Zap

Seven steps. Build it at zapier.com/app/zaps, "Create" button at the top left of the
left-hand rail.

1. **Trigger — Schedule by Zapier, Every Week.** Pick a weekday and an hour. Weekly,
   not daily: a check that pings you every day is a check you learn to ignore, and
   the thing being watched changes state at most once.

2. **Google Sheets — Get Many Spreadsheet Rows.** Spreadsheet: CREDENTIAL GRAVEYARD.
   Worksheet: Sheet1. Columns: A:K. First row: 2. Row count: 50.
   Google Sheets is **not currently connected to your Zapier account** — this step
   will prompt you to sign in the first time. That prompt appears as a "Sign in"
   button inside the step panel on the right side of the editor; it opens a Google
   consent window. If your display scaling is above 125 percent the consent window's
   Allow button can land below the fold — scroll the window itself, not the page.

3. **Looping by Zapier — Create Loop From Line Items.** Feed it the label,
   endpoint, auth_header_name, auth_scheme, secret_ref and exposure_date line-item
   outputs from step 2. Everything after this runs once per row.

4. **Filter by Zapier.** Only continue if `exposure_date` **exists**. This is the
   guard described above. It is one condition; do not add more.

5. **Storage by Zapier — Get Value.** Key: the loop's `secret_ref`. This returns the
   cr