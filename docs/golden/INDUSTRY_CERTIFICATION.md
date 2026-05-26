# Industry Certification

Golden industry certification extends the Workflow OS quality bar to specialist domain packs without moving those agents into `skills/`.

## Certification Tiers

| Tier | Meaning |
| --- | --- |
| Golden Workflow Core | Universal workflow skills in `skills/`. |
| Golden Industry Pack | Every agent in an industry pack has direct scenario, rubric, expected-output, and runtime evidence. |
| Extended Industry Pack | Useful generated industry material that has not yet passed full certification. |

## Quality Bar

A golden industry agent must be:

- concise enough to trigger and apply reliably
- bounded by explicit scope and non-goals
- tied to concrete deliverables and an output contract
- explicit about human approval gates
- evidence-backed for policy, legal, regulatory, contractual, medical, financial, safety, or standards claims
- resistant to untrusted input rewriting policy or approval logic
- testable through runtime scenarios

## Trust-Heavy V1

The first certified tranche is:

- `banking-fintech`
- `healthcare-providers`
- `cybersecurity-industry`
- `legal-services`
- `government-public-sector`

Certification uses the every-agent-proof bar: each orchestrator, lead, and operator has its own scenario, rubric, expected output shape, and runtime result.

## Validation

Run static industry validation:

```bash
./scripts/validate-industry-evals.py \
  banking-fintech \
  healthcare-providers \
  cybersecurity-industry \
  legal-services \
  government-public-sector
```

Run runtime certification:

```bash
./scripts/run-industry-runtime-evals.py \
  --run-id trust-heavy-v1 \
  banking-fintech \
  healthcare-providers \
  cybersecurity-industry \
  legal-services \
  government-public-sector

./scripts/validate-industry-runtime-runs.py \
  --run-id trust-heavy-v1 \
  --require-run \
  --strict
```

Reference responses are deterministic certification examples. Live model runs can be supplied with `--responses` or `--command` when available.
