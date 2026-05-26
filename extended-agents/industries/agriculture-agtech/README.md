# Agriculture & AgTech Agent Pack

## Scope
This pack defines a full operating model for Agriculture & AgTech with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Increase yield and profitability through better agronomy, operations, and market execution.
- Risk Focus: weather volatility, input inefficiency, harvest loss, and price risk
- Compliance Focus: input handling standards, food traceability, labor/safety rules, and export compliance
- Outcome Focus: yield per acre, cost per acre, harvest efficiency, and realized margin
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Agronomy | knowledge | Agriculture & AgTech Agronomy Lead | Agriculture & AgTech Agronomy Operator |
| Farm Operations | operations | Agriculture & AgTech Farm Operations Lead | Agriculture & AgTech Farm Operations Operator |
| Inputs Procurement | operations | Agriculture & AgTech Inputs Procurement Lead | Agriculture & AgTech Inputs Procurement Operator |
| Irrigation | operations | Agriculture & AgTech Irrigation Lead | Agriculture & AgTech Irrigation Operator |
| Harvest Logistics | operations | Agriculture & AgTech Harvest Logistics Lead | Agriculture & AgTech Harvest Logistics Operator |
| Commodity Sales | growth | Agriculture & AgTech Commodity Sales Lead | Agriculture & AgTech Commodity Sales Operator |
| Traceability | governance | Agriculture & AgTech Traceability Lead | Agriculture & AgTech Traceability Operator |
| Yield Analytics | analytics | Agriculture & AgTech Yield Analytics Lead | Agriculture & AgTech Yield Analytics Operator |

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
- Orchestrator: [agents/agriculture-agtech-orchestrator.md](agents/agriculture-agtech-orchestrator.md)
- [agents/agriculture-agtech-agronomy-lead.md](agents/agriculture-agtech-agronomy-lead.md)
- [agents/agriculture-agtech-agronomy-operator.md](agents/agriculture-agtech-agronomy-operator.md)
- [agents/agriculture-agtech-farm-operations-lead.md](agents/agriculture-agtech-farm-operations-lead.md)
- [agents/agriculture-agtech-farm-operations-operator.md](agents/agriculture-agtech-farm-operations-operator.md)
- [agents/agriculture-agtech-inputs-procurement-lead.md](agents/agriculture-agtech-inputs-procurement-lead.md)
- [agents/agriculture-agtech-inputs-procurement-operator.md](agents/agriculture-agtech-inputs-procurement-operator.md)
- [agents/agriculture-agtech-irrigation-lead.md](agents/agriculture-agtech-irrigation-lead.md)
- [agents/agriculture-agtech-irrigation-operator.md](agents/agriculture-agtech-irrigation-operator.md)
- [agents/agriculture-agtech-harvest-logistics-lead.md](agents/agriculture-agtech-harvest-logistics-lead.md)
- [agents/agriculture-agtech-harvest-logistics-operator.md](agents/agriculture-agtech-harvest-logistics-operator.md)
- [agents/agriculture-agtech-commodity-sales-lead.md](agents/agriculture-agtech-commodity-sales-lead.md)
- [agents/agriculture-agtech-commodity-sales-operator.md](agents/agriculture-agtech-commodity-sales-operator.md)
- [agents/agriculture-agtech-traceability-lead.md](agents/agriculture-agtech-traceability-lead.md)
- [agents/agriculture-agtech-traceability-operator.md](agents/agriculture-agtech-traceability-operator.md)
- [agents/agriculture-agtech-yield-analytics-lead.md](agents/agriculture-agtech-yield-analytics-lead.md)
- [agents/agriculture-agtech-yield-analytics-operator.md](agents/agriculture-agtech-yield-analytics-operator.md)

## Activation Prompt
```
Activate Agriculture & AgTech Orchestrator.
Objective: Increase yield and profitability through better agronomy, operations, and market execution.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
