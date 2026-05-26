# Books & Publishing Agent Pack

## Scope
This pack defines a full operating model for Books & Publishing with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Acquire, produce, and scale profitable title portfolios across print, digital, and audio channels.
- Risk Focus: acquisition miss-rate, title launch slippage, rights disputes, and inventory imbalance
- Compliance Focus: rights chain-of-title, contract terms, metadata standards, and market-specific regulations
- Outcome Focus: sell-through, margin by title, release predictability, and author/list growth
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Acquisitions | strategy | Books & Publishing Acquisitions Lead | Books & Publishing Acquisitions Operator |
| Editorial | creative | Books & Publishing Editorial Lead | Books & Publishing Editorial Operator |
| Design & Typesetting | creative | Books & Publishing Design & Typesetting Lead | Books & Publishing Design & Typesetting Operator |
| Production | operations | Books & Publishing Production Lead | Books & Publishing Production Operator |
| Rights & Licensing | governance | Books & Publishing Rights & Licensing Lead | Books & Publishing Rights & Licensing Operator |
| Sales & Distribution | growth | Books & Publishing Sales & Distribution Lead | Books & Publishing Sales & Distribution Operator |
| Publicity | growth | Books & Publishing Publicity Lead | Books & Publishing Publicity Operator |
| Author Relations | service | Books & Publishing Author Relations Lead | Books & Publishing Author Relations Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, source map, and scope boundaries.
2. Planning: roadmap, owners, dependencies, acceptance criteria, and eval set definition.
3. Execution: lead/operator delivery loops by division using structured handoffs.
4. Validation: QA, approval, citation, and policy checks with evidence artifacts.
5. Launch/Ops: handover completeness, live monitoring, and rollback or escalation readiness.

## Reliability Rules
- Consequential actions require human approval according to the agent prompt.
- Policy, regulatory, legal, medical, or contractual claims require source, jurisdiction, and effective date when applicable.
- Final outputs should follow the structured contracts embedded in each agent file.
- Every prompt, model, tool, or policy change should trigger reevaluation before rollout.

## Agent Files
- Orchestrator: [agents/books-publishing-orchestrator.md](agents/books-publishing-orchestrator.md)
- [agents/books-publishing-acquisitions-lead.md](agents/books-publishing-acquisitions-lead.md)
- [agents/books-publishing-acquisitions-operator.md](agents/books-publishing-acquisitions-operator.md)
- [agents/books-publishing-editorial-lead.md](agents/books-publishing-editorial-lead.md)
- [agents/books-publishing-editorial-operator.md](agents/books-publishing-editorial-operator.md)
- [agents/books-publishing-design-typesetting-lead.md](agents/books-publishing-design-typesetting-lead.md)
- [agents/books-publishing-design-typesetting-operator.md](agents/books-publishing-design-typesetting-operator.md)
- [agents/books-publishing-production-lead.md](agents/books-publishing-production-lead.md)
- [agents/books-publishing-production-operator.md](agents/books-publishing-production-operator.md)
- [agents/books-publishing-rights-licensing-lead.md](agents/books-publishing-rights-licensing-lead.md)
- [agents/books-publishing-rights-licensing-operator.md](agents/books-publishing-rights-licensing-operator.md)
- [agents/books-publishing-sales-distribution-lead.md](agents/books-publishing-sales-distribution-lead.md)
- [agents/books-publishing-sales-distribution-operator.md](agents/books-publishing-sales-distribution-operator.md)
- [agents/books-publishing-publicity-lead.md](agents/books-publishing-publicity-lead.md)
- [agents/books-publishing-publicity-operator.md](agents/books-publishing-publicity-operator.md)
- [agents/books-publishing-author-relations-lead.md](agents/books-publishing-author-relations-lead.md)
- [agents/books-publishing-author-relations-operator.md](agents/books-publishing-author-relations-operator.md)

## Activation Prompt
```
Activate Books & Publishing Orchestrator.
Objective: Acquire, produce, and scale profitable title portfolios across print, digital, and audio channels.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
