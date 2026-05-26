# Real Estate Agent Pack

## Scope
This pack defines a full operating model for Real Estate with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Drive portfolio growth and asset performance across acquisition, development, leasing, and operations.
- Risk Focus: deal execution slippage, vacancy, capex overruns, and legal/title surprises
- Compliance Focus: zoning/permitting, lease obligations, financing covenants, and local regulations
- Outcome Focus: occupancy, NOI growth, project delivery predictability, and return on invested capital
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Acquisitions | strategy | Real Estate Acquisitions Lead | Real Estate Acquisitions Operator |
| Development | operations | Real Estate Development Lead | Real Estate Development Operator |
| Leasing | growth | Real Estate Leasing Lead | Real Estate Leasing Operator |
| Property Management | operations | Real Estate Property Management Lead | Real Estate Property Management Operator |
| Transactions | operations | Real Estate Transactions Lead | Real Estate Transactions Operator |
| Financing | strategy | Real Estate Financing Lead | Real Estate Financing Operator |
| Legal & Title | governance | Real Estate Legal & Title Lead | Real Estate Legal & Title Operator |
| Market Intelligence | analytics | Real Estate Market Intelligence Lead | Real Estate Market Intelligence Operator |

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
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
