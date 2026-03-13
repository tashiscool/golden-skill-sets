# Food & Beverage (CPG) Agent Pack

## Scope
This pack defines a full operating model for Food & Beverage (CPG) with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Develop and scale profitable CPG portfolios while maintaining food safety and in-stock performance.
- Risk Focus: recall exposure, forecast error, shelf disruption, and promotional inefficiency
- Compliance Focus: food safety plans, labeling/claims controls, retailer standards, and traceability
- Outcome Focus: distribution breadth, velocity, margin, and safety performance
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| R&D | knowledge | Food & Beverage (CPG) R&D Lead | Food & Beverage (CPG) R&D Operator |
| Regulatory & Labeling | governance | Food & Beverage (CPG) Regulatory & Labeling Lead | Food & Beverage (CPG) Regulatory & Labeling Operator |
| Procurement | operations | Food & Beverage (CPG) Procurement Lead | Food & Beverage (CPG) Procurement Operator |
| Manufacturing | operations | Food & Beverage (CPG) Manufacturing Lead | Food & Beverage (CPG) Manufacturing Operator |
| Distribution | operations | Food & Beverage (CPG) Distribution Lead | Food & Beverage (CPG) Distribution Operator |
| Sales | growth | Food & Beverage (CPG) Sales Lead | Food & Beverage (CPG) Sales Operator |
| Trade Marketing | growth | Food & Beverage (CPG) Trade Marketing Lead | Food & Beverage (CPG) Trade Marketing Operator |
| QA & Food Safety | governance | Food & Beverage (CPG) QA & Food Safety Lead | Food & Beverage (CPG) QA & Food Safety Operator |

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
- Orchestrator: [agents/food-beverage-cpg-orchestrator.md](agents/food-beverage-cpg-orchestrator.md)
- [agents/food-beverage-cpg-r-d-lead.md](agents/food-beverage-cpg-r-d-lead.md)
- [agents/food-beverage-cpg-r-d-operator.md](agents/food-beverage-cpg-r-d-operator.md)
- [agents/food-beverage-cpg-regulatory-labeling-lead.md](agents/food-beverage-cpg-regulatory-labeling-lead.md)
- [agents/food-beverage-cpg-regulatory-labeling-operator.md](agents/food-beverage-cpg-regulatory-labeling-operator.md)
- [agents/food-beverage-cpg-procurement-lead.md](agents/food-beverage-cpg-procurement-lead.md)
- [agents/food-beverage-cpg-procurement-operator.md](agents/food-beverage-cpg-procurement-operator.md)
- [agents/food-beverage-cpg-manufacturing-lead.md](agents/food-beverage-cpg-manufacturing-lead.md)
- [agents/food-beverage-cpg-manufacturing-operator.md](agents/food-beverage-cpg-manufacturing-operator.md)
- [agents/food-beverage-cpg-distribution-lead.md](agents/food-beverage-cpg-distribution-lead.md)
- [agents/food-beverage-cpg-distribution-operator.md](agents/food-beverage-cpg-distribution-operator.md)
- [agents/food-beverage-cpg-sales-lead.md](agents/food-beverage-cpg-sales-lead.md)
- [agents/food-beverage-cpg-sales-operator.md](agents/food-beverage-cpg-sales-operator.md)
- [agents/food-beverage-cpg-trade-marketing-lead.md](agents/food-beverage-cpg-trade-marketing-lead.md)
- [agents/food-beverage-cpg-trade-marketing-operator.md](agents/food-beverage-cpg-trade-marketing-operator.md)
- [agents/food-beverage-cpg-qa-food-safety-lead.md](agents/food-beverage-cpg-qa-food-safety-lead.md)
- [agents/food-beverage-cpg-qa-food-safety-operator.md](agents/food-beverage-cpg-qa-food-safety-operator.md)

## Activation Prompt
```
Activate Food & Beverage (CPG) Orchestrator.
Objective: Develop and scale profitable CPG portfolios while maintaining food safety and in-stock performance.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
