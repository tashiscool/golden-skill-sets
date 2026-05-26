# Development Capability Certification

The golden workflow core is not enough by itself. Real product development requires switching hats deliberately without letting any specialist hat override scope, evidence, or human accountability.

## Certified Hats

Development capability certification covers:

- Product, PM, and business analysis
- Architecture and backend tradeoffs
- UX, UI, and accessibility
- Backend, API, and data contracts
- Frontend implementation quality
- QA and test strategy
- Observability, availability, and incident readiness
- Security, confidentiality, integrity, availability, and privacy
- Reporting, analytics, and decision quality
- Marketing, sales, and GTM alignment
- Delivery, program governance, and stakeholder control
- AI/model quality and evaluation

These are not all literal skills. They are capability lenses that combine the golden workflow core with the relevant specialist agents.

## Quality Bar

Every certified development capability must:

- start from bounded scope and acceptance criteria
- name the hats involved and their responsibilities
- separate facts, assumptions, risks, and decisions
- preserve human approval gates for architecture, security, public API, persistence, launch, and external-write changes
- define evidence, tests, artifacts, and release gates
- produce a concrete output contract or checklist

## Validation

Run:

```bash
./scripts/validate-development-evals.py
./scripts/run-development-runtime-evals.py --run-id development-capabilities-v1
./scripts/validate-development-runtime-runs.py --run-id development-capabilities-v1 --require-run --strict
```

The runtime reference responses are deterministic examples. Live model evidence can be supplied with `--responses` or `--command`.
