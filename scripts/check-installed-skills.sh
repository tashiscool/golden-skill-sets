#!/usr/bin/env bash
#
# Verify local installed Codex skills match the canonical repo skills.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"

"$REPO_ROOT/scripts/validate-skills.py"

status=0

for skill_dir in "$REPO_ROOT"/skills/*; do
  [[ -d "$skill_dir" ]] || continue
  skill="$(basename "$skill_dir")"
  installed="$DEST/$skill"

  if [[ ! -d "$installed" ]]; then
    echo "ERROR missing installed skill: $installed"
    status=1
    continue
  fi

  if ! diff -qr "$skill_dir" "$installed" >/dev/null; then
    echo "ERROR installed skill drift: $skill"
    diff -qr "$skill_dir" "$installed" || true
    status=1
  fi
done

if [[ "$status" == "0" ]]; then
  echo "installed skills match repo core"
fi

exit "$status"
