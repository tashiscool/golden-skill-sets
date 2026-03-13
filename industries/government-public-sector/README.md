# Government & Public Sector Agent Pack

## Scope
This pack defines a full operating model for Government & Public Sector with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Deliver citizen services with transparency, policy alignment, and operational accountability.
- Risk Focus: service delays, procurement friction, budget variance, and audit findings
- Compliance Focus: public procurement rules, records requirements, accessibility standards, and policy mandates
- Outcome Focus: service-level attainment, budget adherence, audit closure, and constituent satisfaction
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Policy | governance | Government & Public Sector Policy Lead | Government & Public Sector Policy Operator |
| Program Delivery | operations | Government & Public Sector Program Delivery Lead | Government & Public Sector Program Delivery Operator |
| Procurement | governance | Government & Public Sector Procurement Lead | Government & Public Sector Procurement Operator |
| Case Management | adjudication | Government & Public Sector Case Management Lead | Government & Public Sector Case Management Operator |
| Digital Services | technical | Government & Public Sector Digital Services Lead | Government & Public Sector Digital Services Operator |
| Finance | governance | Government & Public Sector Finance Lead | Government & Public Sector Finance Operator |
| Audit | governance | Government & Public Sector Audit Lead | Government & Public Sector Audit Operator |
| Public Communications | service | Government & Public Sector Public Communications Lead | Government & Public Sector Public Communications Operator |

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
- Orchestrator: [agents/government-public-sector-orchestrator.md](agents/government-public-sector-orchestrator.md)
- [agents/government-public-sector-policy-lead.md](agents/government-public-sector-policy-lead.md)
- [agents/government-public-sector-policy-operator.md](agents/government-public-sector-policy-operator.md)
- [agents/government-public-sector-program-delivery-lead.md](agents/government-public-sector-program-delivery-lead.md)
- [agents/government-public-sector-program-delivery-operator.md](agents/government-public-sector-program-delivery-operator.md)
- [agents/government-public-sector-procurement-lead.md](agents/government-public-sector-procurement-lead.md)
- [agents/government-public-sector-procurement-operator.md](agents/government-public-sector-procurement-operator.md)
- [agents/government-public-sector-case-management-lead.md](agents/government-public-sector-case-management-lead.md)
- [agents/government-public-sector-case-management-operator.md](agents/government-public-sector-case-management-operator.md)
- [agents/government-public-sector-digital-services-lead.md](agents/government-public-sector-digital-services-lead.md)
- [agents/government-public-sector-digital-services-operator.md](agents/government-public-sector-digital-services-operator.md)
- [agents/government-public-sector-finance-lead.md](agents/government-public-sector-finance-lead.md)
- [agents/government-public-sector-finance-operator.md](agents/government-public-sector-finance-operator.md)
- [agents/government-public-sector-audit-lead.md](agents/government-public-sector-audit-lead.md)
- [agents/government-public-sector-audit-operator.md](agents/government-public-sector-audit-operator.md)
- [agents/government-public-sector-public-communications-lead.md](agents/government-public-sector-public-communications-lead.md)
- [agents/government-public-sector-public-communications-operator.md](agents/government-public-sector-public-communications-operator.md)

## Activation Prompt
```
Activate Government & Public Sector Orchestrator.
Objective: Deliver citizen services with transparency, policy alignment, and operational accountability.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
