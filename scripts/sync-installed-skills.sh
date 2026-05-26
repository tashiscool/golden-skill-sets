#!/usr/bin/env bash
#
# Sync the canonical repo skills into the local Codex skill directory.
# This is the only supported way to update installed golden skills.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"

skills=(
  setup-matt-pocock-skills
  grill-with-docs
  zoom-out
  diagnose
  tdd
  prototype
  to-prd
  to-issues
  handoff
  write-a-skill
  improve-codebase-architecture
  triage
  review
  setup-pre-commit
  git-guardrails-claude-code
  agency-workflow-task-decomposition-coach
  agency-persistent-memory-steward
  agency-stalled-work-diagnostician
  agency-bounded-iteration-driver
)

"$REPO_ROOT/scripts/validate-skills.py"

mkdir -p "$DEST"

for skill in "${skills[@]}"; do
  rm -rf "$DEST/$skill"
  cp -R "$REPO_ROOT/skills/$skill" "$DEST/$skill"
  echo "synced $skill -> $DEST/$skill"
done

echo "Restart Codex to pick up synced skills."
