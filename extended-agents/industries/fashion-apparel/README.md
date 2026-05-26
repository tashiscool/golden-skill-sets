# Fashion & Apparel Agent Pack

## Scope
This pack defines a full operating model for Fashion & Apparel with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Plan and execute seasonal assortments from concept to sell-through with brand consistency and margin control.
- Risk Focus: forecast misses, sourcing delays, quality defects, and markdown pressure
- Compliance Focus: supplier compliance, product safety, labeling, and sustainability disclosures
- Outcome Focus: full-price sell-through, margin, delivery adherence, and category growth
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Trend Research | analytics | Fashion & Apparel Trend Research Lead | Fashion & Apparel Trend Research Operator |
| Design | creative | Fashion & Apparel Design Lead | Fashion & Apparel Design Operator |
| Sourcing | operations | Fashion & Apparel Sourcing Lead | Fashion & Apparel Sourcing Operator |
| Sampling | operations | Fashion & Apparel Sampling Lead | Fashion & Apparel Sampling Operator |
| Manufacturing | operations | Fashion & Apparel Manufacturing Lead | Fashion & Apparel Manufacturing Operator |
| Merchandising | strategy | Fashion & Apparel Merchandising Lead | Fashion & Apparel Merchandising Operator |
| Retail & E-commerce | growth | Fashion & Apparel Retail & E-commerce Lead | Fashion & Apparel Retail & E-commerce Operator |
| Brand & PR | growth | Fashion & Apparel Brand & PR Lead | Fashion & Apparel Brand & PR Operator |

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
- Orchestrator: [agents/fashion-apparel-orchestrator.md](agents/fashion-apparel-orchestrator.md)
- [agents/fashion-apparel-trend-research-lead.md](agents/fashion-apparel-trend-research-lead.md)
- [agents/fashion-apparel-trend-research-operator.md](agents/fashion-apparel-trend-research-operator.md)
- [agents/fashion-apparel-design-lead.md](agents/fashion-apparel-design-lead.md)
- [agents/fashion-apparel-design-operator.md](agents/fashion-apparel-design-operator.md)
- [agents/fashion-apparel-sourcing-lead.md](agents/fashion-apparel-sourcing-lead.md)
- [agents/fashion-apparel-sourcing-operator.md](agents/fashion-apparel-sourcing-operator.md)
- [agents/fashion-apparel-sampling-lead.md](agents/fashion-apparel-sampling-lead.md)
- [agents/fashion-apparel-sampling-operator.md](agents/fashion-apparel-sampling-operator.md)
- [agents/fashion-apparel-manufacturing-lead.md](agents/fashion-apparel-manufacturing-lead.md)
- [agents/fashion-apparel-manufacturing-operator.md](agents/fashion-apparel-manufacturing-operator.md)
- [agents/fashion-apparel-merchandising-lead.md](agents/fashion-apparel-merchandising-lead.md)
- [agents/fashion-apparel-merchandising-operator.md](agents/fashion-apparel-merchandising-operator.md)
- [agents/fashion-apparel-retail-e-commerce-lead.md](agents/fashion-apparel-retail-e-commerce-lead.md)
- [agents/fashion-apparel-retail-e-commerce-operator.md](agents/fashion-apparel-retail-e-commerce-operator.md)
- [agents/fashion-apparel-brand-pr-lead.md](agents/fashion-apparel-brand-pr-lead.md)
- [agents/fashion-apparel-brand-pr-operator.md](agents/fashion-apparel-brand-pr-operator.md)

## Activation Prompt
```
Activate Fashion & Apparel Orchestrator.
Objective: Plan and execute seasonal assortments from concept to sell-through with brand consistency and margin control.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
