#!/bin/bash
# Install the founder gate as a pre-push hook.
# Run once per clone:   bash founder-gate/install-hook.sh
#
# Hooks are NOT versioned by git — a fresh clone has none. So this must be run
# at the top of any session that will push. It is one line and it is idempotent.

REPO="$(git rev-parse --show-toplevel)"
cp "$REPO/founder-gate/pre-push" "$REPO/.git/hooks/pre-push"
chmod +x "$REPO/.git/hooks/pre-push"
echo "founder gate ARMED — no push may carry an unauthorized deletion."
