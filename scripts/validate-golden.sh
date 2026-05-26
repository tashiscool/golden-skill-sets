#!/usr/bin/env bash
# Authoritative validation for the canonical golden-skill-sets repo.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

./scripts/validate-skills.py
./scripts/validate-golden-evals.py
./scripts/validate-industry-evals.py
./scripts/validate-runtime-runs.py
./scripts/validate-industry-runtime-runs.py
./scripts/lint-agents.sh

if [[ "${CHECK_INSTALLED_SKILLS:-0}" == "1" ]]; then
  ./scripts/check-installed-skills.sh
fi
