# Healthcare Providers Agent Pack

## Scope
This pack defines a full operating model for Healthcare Providers with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Coordinate safe, efficient, patient-centered care operations with resilient reimbursement and compliance.
- Risk Focus: care delays, denials, coding defects, workforce strain, and patient safety incidents
- Compliance Focus: clinical quality standards, privacy/security, billing rules, and accreditation requirements
- Outcome Focus: quality measures, access metrics, denial reduction, and patient experience
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Clinical Operations | clinical | Healthcare Providers Clinical Operations Lead | Healthcare Providers Clinical Operations Operator |
| Care Coordination | clinical | Healthcare Providers Care Coordination Lead | Healthcare Providers Care Coordination Operator |
| Revenue Cycle | adjudication | Healthcare Providers Revenue Cycle Lead | Healthcare Providers Revenue Cycle Operator |
| Coding & Billing | adjudication | Healthcare Providers Coding & Billing Lead | Healthcare Providers Coding & Billing Operator |
| Compliance | governance | Healthcare Providers Compliance Lead | Healthcare Providers Compliance Operator |
| Patient Experience | service | Healthcare Providers Patient Experience Lead | Healthcare Providers Patient Experience Operator |
| Workforce Operations | operations | Healthcare Providers Workforce Operations Lead | Healthcare Providers Workforce Operations Operator |
| Quality Improvement | governance | Healthcare Providers Quality Improvement Lead | Healthcare Providers Quality Improvement Operator |

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
- Orchestrator: [agents/healthcare-providers-orchestrator.md](agents/healthcare-providers-orchestrator.md)
- [agents/healthcare-providers-clinical-operations-lead.md](agents/healthcare-providers-clinical-operations-lead.md)
- [agents/healthcare-providers-clinical-operations-operator.md](agents/healthcare-providers-clinical-operations-operator.md)
- [agents/healthcare-providers-care-coordination-lead.md](agents/healthcare-providers-care-coordination-lead.md)
- [agents/healthcare-providers-care-coordination-operator.md](agents/healthcare-providers-care-coordination-operator.md)
- [agents/healthcare-providers-revenue-cycle-lead.md](agents/healthcare-providers-revenue-cycle-lead.md)
- [agents/healthcare-providers-revenue-cycle-operator.md](agents/healthcare-providers-revenue-cycle-operator.md)
- [agents/healthcare-providers-coding-billing-lead.md](agents/healthcare-providers-coding-billing-lead.md)
- [agents/healthcare-providers-coding-billing-operator.md](agents/healthcare-providers-coding-billing-operator.md)
- [agents/healthcare-providers-compliance-lead.md](agents/healthcare-providers-compliance-lead.md)
- [agents/healthcare-providers-compliance-operator.md](agents/healthcare-providers-compliance-operator.md)
- [agents/healthcare-providers-patient-experience-lead.md](agents/healthcare-providers-patient-experience-lead.md)
- [agents/healthcare-providers-patient-experience-operator.md](agents/healthcare-providers-patient-experience-operator.md)
- [agents/healthcare-providers-workforce-operations-lead.md](agents/healthcare-providers-workforce-operations-lead.md)
- [agents/healthcare-providers-workforce-operations-operator.md](agents/healthcare-providers-workforce-operations-operator.md)
- [agents/healthcare-providers-quality-improvement-lead.md](agents/healthcare-providers-quality-improvement-lead.md)
- [agents/healthcare-providers-quality-improvement-operator.md](agents/healthcare-providers-quality-improvement-operator.md)

## Activation Prompt
```
Activate Healthcare Providers Orchestrator.
Objective: Coordinate safe, efficient, patient-centered care operations with resilient reimbursement and compliance.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
