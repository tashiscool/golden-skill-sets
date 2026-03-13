# Nonprofit & NGO Agent Pack

## Scope
This pack defines a full operating model for Nonprofit & NGO with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Maximize mission impact while maintaining funding resilience and governance discipline.
- Risk Focus: program drift, grant non-compliance, donor churn, and operating instability
- Compliance Focus: grant reporting obligations, donor restrictions, safeguarding standards, and audit controls
- Outcome Focus: program outcomes, funding diversification, retention, and overhead efficiency
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Program Design | strategy | Nonprofit & NGO Program Design Lead | Nonprofit & NGO Program Design Operator |
| Grants | governance | Nonprofit & NGO Grants Lead | Nonprofit & NGO Grants Operator |
| Fundraising | growth | Nonprofit & NGO Fundraising Lead | Nonprofit & NGO Fundraising Operator |
| Donor Relations | service | Nonprofit & NGO Donor Relations Lead | Nonprofit & NGO Donor Relations Operator |
| Volunteer Operations | operations | Nonprofit & NGO Volunteer Operations Lead | Nonprofit & NGO Volunteer Operations Operator |
| Monitoring & Evaluation | analytics | Nonprofit & NGO Monitoring & Evaluation Lead | Nonprofit & NGO Monitoring & Evaluation Operator |
| Advocacy | strategy | Nonprofit & NGO Advocacy Lead | Nonprofit & NGO Advocacy Operator |
| Finance & Compliance | governance | Nonprofit & NGO Finance & Compliance Lead | Nonprofit & NGO Finance & Compliance Operator |

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
- Orchestrator: [agents/nonprofit-ngo-orchestrator.md](agents/nonprofit-ngo-orchestrator.md)
- [agents/nonprofit-ngo-program-design-lead.md](agents/nonprofit-ngo-program-design-lead.md)
- [agents/nonprofit-ngo-program-design-operator.md](agents/nonprofit-ngo-program-design-operator.md)
- [agents/nonprofit-ngo-grants-lead.md](agents/nonprofit-ngo-grants-lead.md)
- [agents/nonprofit-ngo-grants-operator.md](agents/nonprofit-ngo-grants-operator.md)
- [agents/nonprofit-ngo-fundraising-lead.md](agents/nonprofit-ngo-fundraising-lead.md)
- [agents/nonprofit-ngo-fundraising-operator.md](agents/nonprofit-ngo-fundraising-operator.md)
- [agents/nonprofit-ngo-donor-relations-lead.md](agents/nonprofit-ngo-donor-relations-lead.md)
- [agents/nonprofit-ngo-donor-relations-operator.md](agents/nonprofit-ngo-donor-relations-operator.md)
- [agents/nonprofit-ngo-volunteer-operations-lead.md](agents/nonprofit-ngo-volunteer-operations-lead.md)
- [agents/nonprofit-ngo-volunteer-operations-operator.md](agents/nonprofit-ngo-volunteer-operations-operator.md)
- [agents/nonprofit-ngo-monitoring-evaluation-lead.md](agents/nonprofit-ngo-monitoring-evaluation-lead.md)
- [agents/nonprofit-ngo-monitoring-evaluation-operator.md](agents/nonprofit-ngo-monitoring-evaluation-operator.md)
- [agents/nonprofit-ngo-advocacy-lead.md](agents/nonprofit-ngo-advocacy-lead.md)
- [agents/nonprofit-ngo-advocacy-operator.md](agents/nonprofit-ngo-advocacy-operator.md)
- [agents/nonprofit-ngo-finance-compliance-lead.md](agents/nonprofit-ngo-finance-compliance-lead.md)
- [agents/nonprofit-ngo-finance-compliance-operator.md](agents/nonprofit-ngo-finance-compliance-operator.md)

## Activation Prompt
```
Activate Nonprofit & NGO Orchestrator.
Objective: Maximize mission impact while maintaining funding resilience and governance discipline.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
