# Real Estate Agent Pack

## Scope
This pack defines a full operating model for Real Estate with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Drive portfolio growth and asset performance across acquisition, development, leasing, and operations.
- Risk Focus: deal execution slippage, vacancy, capex overruns, and legal/title surprises
- Compliance Focus: zoning/permitting, lease obligations, financing covenants, and local regulations
- Outcome Focus: occupancy, NOI growth, project delivery predictability, and return on invested capital

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Acquisitions | Real Estate Acquisitions Lead | Real Estate Acquisitions Operator |
| Development | Real Estate Development Lead | Real Estate Development Operator |
| Leasing | Real Estate Leasing Lead | Real Estate Leasing Operator |
| Property Management | Real Estate Property Management Lead | Real Estate Property Management Operator |
| Transactions | Real Estate Transactions Lead | Real Estate Transactions Operator |
| Financing | Real Estate Financing Lead | Real Estate Financing Operator |
| Legal & Title | Real Estate Legal & Title Lead | Real Estate Legal & Title Operator |
| Market Intelligence | Real Estate Market Intelligence Lead | Real Estate Market Intelligence Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/real-estate-orchestrator.md](agents/real-estate-orchestrator.md)
- [agents/real-estate-acquisitions-lead.md](agents/real-estate-acquisitions-lead.md)
- [agents/real-estate-acquisitions-operator.md](agents/real-estate-acquisitions-operator.md)
- [agents/real-estate-development-lead.md](agents/real-estate-development-lead.md)
- [agents/real-estate-development-operator.md](agents/real-estate-development-operator.md)
- [agents/real-estate-leasing-lead.md](agents/real-estate-leasing-lead.md)
- [agents/real-estate-leasing-operator.md](agents/real-estate-leasing-operator.md)
- [agents/real-estate-property-management-lead.md](agents/real-estate-property-management-lead.md)
- [agents/real-estate-property-management-operator.md](agents/real-estate-property-management-operator.md)
- [agents/real-estate-transactions-lead.md](agents/real-estate-transactions-lead.md)
- [agents/real-estate-transactions-operator.md](agents/real-estate-transactions-operator.md)
- [agents/real-estate-financing-lead.md](agents/real-estate-financing-lead.md)
- [agents/real-estate-financing-operator.md](agents/real-estate-financing-operator.md)
- [agents/real-estate-legal-title-lead.md](agents/real-estate-legal-title-lead.md)
- [agents/real-estate-legal-title-operator.md](agents/real-estate-legal-title-operator.md)
- [agents/real-estate-market-intelligence-lead.md](agents/real-estate-market-intelligence-lead.md)
- [agents/real-estate-market-intelligence-operator.md](agents/real-estate-market-intelligence-operator.md)

## Activation Prompt
```
Activate Real Estate Orchestrator.
Objective: Drive portfolio growth and asset performance across acquisition, development, leasing, and operations.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
