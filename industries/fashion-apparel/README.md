# Fashion & Apparel Agent Pack

## Scope
This pack defines a full operating model for Fashion & Apparel with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Plan and execute seasonal assortments from concept to sell-through with brand consistency and margin control.
- Risk Focus: forecast misses, sourcing delays, quality defects, and markdown pressure
- Compliance Focus: supplier compliance, product safety, labeling, and sustainability disclosures
- Outcome Focus: full-price sell-through, margin, delivery adherence, and category growth

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Trend Research | Fashion & Apparel Trend Research Lead | Fashion & Apparel Trend Research Operator |
| Design | Fashion & Apparel Design Lead | Fashion & Apparel Design Operator |
| Sourcing | Fashion & Apparel Sourcing Lead | Fashion & Apparel Sourcing Operator |
| Sampling | Fashion & Apparel Sampling Lead | Fashion & Apparel Sampling Operator |
| Manufacturing | Fashion & Apparel Manufacturing Lead | Fashion & Apparel Manufacturing Operator |
| Merchandising | Fashion & Apparel Merchandising Lead | Fashion & Apparel Merchandising Operator |
| Retail & E-commerce | Fashion & Apparel Retail & E-commerce Lead | Fashion & Apparel Retail & E-commerce Operator |
| Brand & PR | Fashion & Apparel Brand & PR Lead | Fashion & Apparel Brand & PR Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

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
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
