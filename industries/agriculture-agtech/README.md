# Agriculture & AgTech Agent Pack

## Scope
This pack defines a full operating model for Agriculture & AgTech with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Increase yield and profitability through better agronomy, operations, and market execution.
- Risk Focus: weather volatility, input inefficiency, harvest loss, and price risk
- Compliance Focus: input handling standards, food traceability, labor/safety rules, and export compliance
- Outcome Focus: yield per acre, cost per acre, harvest efficiency, and realized margin

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Agronomy | Agriculture & AgTech Agronomy Lead | Agriculture & AgTech Agronomy Operator |
| Farm Operations | Agriculture & AgTech Farm Operations Lead | Agriculture & AgTech Farm Operations Operator |
| Inputs Procurement | Agriculture & AgTech Inputs Procurement Lead | Agriculture & AgTech Inputs Procurement Operator |
| Irrigation | Agriculture & AgTech Irrigation Lead | Agriculture & AgTech Irrigation Operator |
| Harvest Logistics | Agriculture & AgTech Harvest Logistics Lead | Agriculture & AgTech Harvest Logistics Operator |
| Commodity Sales | Agriculture & AgTech Commodity Sales Lead | Agriculture & AgTech Commodity Sales Operator |
| Traceability | Agriculture & AgTech Traceability Lead | Agriculture & AgTech Traceability Operator |
| Yield Analytics | Agriculture & AgTech Yield Analytics Lead | Agriculture & AgTech Yield Analytics Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

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
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
