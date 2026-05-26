# Runtime Evals

Runtime evals turn the golden standard into saved evidence. They are not a replacement for human review; they make review concrete by preserving the prompt, response, score, and summary for each scenario.

## Output Format

Each run writes:

```text
evals/runs/<timestamp>/<scenario-id>/prompt.md
evals/runs/<timestamp>/<scenario-id>/response.md
evals/runs/<timestamp>/<scenario-id>/score.json
evals/runs/<timestamp>/summary.md
```

Run directories are ignored by git by default because they are generated evidence. Promote selected reviewed runs manually only when they are useful as release artifacts.

## Static Gate

Always start with:

```bash
./scripts/validate-golden.sh
```

This checks skill structure, scenario fixtures, rubric metadata, saved runtime run shape, and extended-agent linting.

## Dry Run

Use dry run mode to verify artifact generation without claiming model behavior:

```bash
./scripts/run-runtime-evals.py --dry-run
./scripts/validate-runtime-runs.py --require-run
```

Dry runs are marked pending and should not be treated as proof.

## Recorded Responses

To score real responses, collect one Markdown file per scenario:

```text
tmp/runtime-responses/ambiguous-legacy-refactor.md
tmp/runtime-responses/production-regression-diagnosis.md
tmp/runtime-responses/issue-triage-human-gate.md
```

Then run:

```bash
./scripts/run-runtime-evals.py \
  --run-id high-risk-recorded \
  --responses tmp/runtime-responses \
  ambiguous-legacy-refactor \
  production-regression-diagnosis \
  issue-triage-human-gate

./scripts/validate-runtime-runs.py --run-id high-risk-recorded --require-run --strict
```

## Command-Generated Responses

The harness can call a command that prints a response. The command receives a prompt file path:

```bash
./scripts/run-runtime-evals.py \
  --command 'codex exec < {prompt_file}' \
  ambiguous-legacy-refactor
```

Use this only when the local Codex CLI is configured for non-interactive execution. If the command exits non-zero, the response is saved and marked pending for review.

## Scoring

Rubrics live in `evals/rubrics/`. Each criterion has required terms and a weight. A response passes when:

- it is not pending
- it meets the minimum score
- it contains no forbidden terms

The deterministic score is intentionally simple. The human reviewer still owns the final judgment, especially for business context, security, correctness, and maintainability.

## High-Risk Smoke Set

Run these before a release:

- `ambiguous-legacy-refactor`
- `production-regression-diagnosis`
- `issue-triage-human-gate`

Then run the full suite before publishing a major update.
