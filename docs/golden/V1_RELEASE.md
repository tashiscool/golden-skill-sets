# Evidence V1 Release

Evidence v1 is the first public credibility milestone for Golden Skill Sets. It presents the repo as a small Workflow OS for bounded, human-accountable agentic coding, not as a giant autonomous agent catalog.

## V1 Promise

- The 19 skills in `skills/` are the curated golden workflow core.
- Extended Agency agents and industry packs remain available under `extended-agents/`.
- The core can be installed into Codex from the repo with `./scripts/sync-installed-skills.sh`.
- Static validation runs through `./scripts/validate-golden.sh`.
- Runtime eval evidence is published as a GitHub Release artifact for the high-risk scenarios.

## Limits

- Runtime scoring is deterministic and intentionally simple.
- Passing scores are evidence, not a guarantee of correctness in a real production codebase.
- Humans still own architecture, security, correctness, maintainability, and release decisions.
- Extended-agent lint warnings are accepted in v1 when they are warnings rather than errors.

## Release Gate

Run:

```bash
./scripts/validate-skills.py
./scripts/validate-golden-evals.py
./scripts/validate-runtime-runs.py
./scripts/lint-agents.sh
./scripts/validate-golden.sh
```

For installed-skill drift:

```bash
./scripts/sync-installed-skills.sh
./scripts/check-installed-skills.sh
```

For runtime evidence:

```bash
./scripts/run-runtime-evals.py \
  --run-id high-risk-v1 \
  --responses tmp/runtime-responses \
  ambiguous-legacy-refactor \
  production-regression-diagnosis \
  issue-triage-human-gate

./scripts/validate-runtime-runs.py --run-id high-risk-v1 --require-run --strict
```

## Release Artifact

The release should attach `golden-skill-sets-runtime-evals-v1.zip`, containing:

- `prompt.md`
- `response.md`
- `score.json`
- `summary.md`

The release notes should include the commit SHA, CI status, validation summary, and a reminder that human review remains required.
