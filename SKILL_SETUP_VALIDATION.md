# Skill Setup Validation

Validation date: 2026-05-26

## Scope

Validated the golden skill setup installed from `mattpocock/skills` into `/Users/tkhan/.codex/skills`, plus the repo and global policy files that make the workflow bounded and human-accountable.

## Mechanical Checks

Result: PASS

Checked 19 installed skills:

- `setup-matt-pocock-skills`
- `grill-with-docs`
- `zoom-out`
- `diagnose`
- `tdd`
- `prototype`
- `to-prd`
- `to-issues`
- `handoff`
- `write-a-skill`
- `improve-codebase-architecture`
- `triage`
- `review`
- `setup-pre-commit`
- `git-guardrails-claude-code`
- `agency-workflow-task-decomposition-coach`
- `agency-persistent-memory-steward`
- `agency-stalled-work-diagnostician`
- `agency-bounded-iteration-driver`

Checks performed:

- Every installed skill has `SKILL.md`.
- Every `SKILL.md` has frontmatter.
- Frontmatter `name` matches the installed directory name.
- Descriptions exist and include trigger language where expected.
- Local markdown links in skill bodies resolve.
- Companion files copied correctly.

## Guardrail Checks

Result: PASS

The Claude Code git guardrail script is executable and blocks dangerous git commands:

```text
git push origin main -> BLOCKED, exit=2
```

Note: this guardrail script is for Claude Code hooks. Codex is protected primarily through global/repo instructions and its permission model, not this hook.

## Policy-Fit Fixes Applied

The initial validation found a few instructions that were too eager for the bounded workflow. These were fixed in both the installed copies and the cloned source copies.

| Skill | Fix |
| --- | --- |
| `setup-pre-commit` | Removed automatic staging/commit instruction. Now commits only when explicitly requested. |
| `to-prd` | Changed from automatic publishing to draft-first, publish-with-approval unless explicitly requested. |
| `triage` | Added confirmation gate before issue tracker mutations unless directly requested. |
| `review` | Added fallback for environments without sub-agents. |
| `setup-matt-pocock-skills` | Tightened description trigger language for discovery. |

Follow-up search confirmed no remaining problematic phrases like automatic staging, automatic publishing, or sub-agent-only review.

## Repo Setup Checks

Result: PASS

Created and verified non-empty:

- `AGENTS.md`
- `docs/agents/issue-tracker.md`
- `docs/agents/triage-labels.md`
- `docs/agents/domain.md`
- `docs/adr/README.md`
- `GOLDEN_SKILL_SETS.md`

Global policy updated:

- `/Users/tkhan/.codex/AGENTS.md`

## Behavioral Validation Matrix

| Scenario | Expected behavior | Status |
| --- | --- | --- |
| Ambiguous feature request | Use planning/orientation first; ask or run `grill-with-docs` before edits. | Configured |
| Unfamiliar code path | Use `zoom-out` before implementation. | Configured |
| Bug report or regression | Use `diagnose`: repro loop, hypotheses, instrumentation, regression test. | Configured |
| Behavior implementation | Prefer `tdd` and behavior-focused tests through public interfaces. | Configured |
| PRD creation | Draft first; publish only with approval unless explicitly requested. | Fixed |
| Issue triage | Confirm before labels, closure, `wontfix`, or `ready-for-agent`. | Fixed |
| Pre-commit setup | Do not stage/commit unless explicitly requested. | Fixed |
| Architecture improvement | Advisory by default; implementation requires approval. | Configured |
| Review workflow | Standards and Spec reviews remain separate; sub-agent fallback exists. | Fixed |

## Remaining Runtime Check

Codex needs to be restarted before newly installed skills are visible in the active skill list. After restart, validate by asking a lightweight prompt such as:

```text
Use zoom-out on this repo and summarize how the agent skill setup fits together. Do not edit files.
```

Expected result: Codex should load `zoom-out`, read the repo policy/docs, and produce a high-level map without making edits.

## Golden Scenario Validation

The repo now includes a scenario validation layer:

```sh
./scripts/validate-golden.sh
```

Current result:

```text
checked 6 scenarios
status PASS
```
