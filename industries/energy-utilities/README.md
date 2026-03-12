# Energy & Utilities Agent Pack

## Scope
This pack defines a full operating model for Energy & Utilities with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Balance reliability, safety, and cost while modernizing generation, grid, and customer operations.
- Risk Focus: outage risk, asset failures, compliance penalties, and demand/supply volatility
- Compliance Focus: grid reliability standards, market rules, safety obligations, and ESG reporting
- Outcome Focus: service reliability, outage duration, operating cost, and compliance performance

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Generation | Energy & Utilities Generation Lead | Energy & Utilities Generation Operator |
| Grid Operations | Energy & Utilities Grid Operations Lead | Energy & Utilities Grid Operations Operator |
| Field Service | Energy & Utilities Field Service Lead | Energy & Utilities Field Service Operator |
| Asset Reliability | Energy & Utilities Asset Reliability Lead | Energy & Utilities Asset Reliability Operator |
| Trading | Energy & Utilities Trading Lead | Energy & Utilities Trading Operator |
| Customer Operations | Energy & Utilities Customer Operations Lead | Energy & Utilities Customer Operations Operator |
| Regulatory Affairs | Energy & Utilities Regulatory Affairs Lead | Energy & Utilities Regulatory Affairs Operator |
| Sustainability & ESG | Energy & Utilities Sustainability & ESG Lead | Energy & Utilities Sustainability & ESG Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/energy-utilities-orchestrator.md](agents/energy-utilities-orchestrator.md)
- [agents/energy-utilities-generation-lead.md](agents/energy-utilities-generation-lead.md)
- [agents/energy-utilities-generation-operator.md](agents/energy-utilities-generation-operator.md)
- [agents/energy-utilities-grid-operations-lead.md](agents/energy-utilities-grid-operations-lead.md)
- [agents/energy-utilities-grid-operations-operator.md](agents/energy-utilities-grid-operations-operator.md)
- [agents/energy-utilities-field-service-lead.md](agents/energy-utilities-field-service-lead.md)
- [agents/energy-utilities-field-service-operator.md](agents/energy-utilities-field-service-operator.md)
- [agents/energy-utilities-asset-reliability-lead.md](agents/energy-utilities-asset-reliability-lead.md)
- [agents/energy-utilities-asset-reliability-operator.md](agents/energy-utilities-asset-reliability-operator.md)
- [agents/energy-utilities-trading-lead.md](agents/energy-utilities-trading-lead.md)
- [agents/energy-utilities-trading-operator.md](agents/energy-utilities-trading-operator.md)
- [agents/energy-utilities-customer-operations-lead.md](agents/energy-utilities-customer-operations-lead.md)
- [agents/energy-utilities-customer-operations-operator.md](agents/energy-utilities-customer-operations-operator.md)
- [agents/energy-utilities-regulatory-affairs-lead.md](agents/energy-utilities-regulatory-affairs-lead.md)
- [agents/energy-utilities-regulatory-affairs-operator.md](agents/energy-utilities-regulatory-affairs-operator.md)
- [agents/energy-utilities-sustainability-esg-lead.md](agents/energy-utilities-sustainability-esg-lead.md)
- [agents/energy-utilities-sustainability-esg-operator.md](agents/energy-utilities-sustainability-esg-operator.md)

## Activation Prompt
```
Activate Energy & Utilities Orchestrator.
Objective: Balance reliability, safety, and cost while modernizing generation, grid, and customer operations.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
