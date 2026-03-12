# Healthcare Providers Agent Pack

## Scope
This pack defines a full operating model for Healthcare Providers with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Coordinate safe, efficient, patient-centered care operations with resilient reimbursement and compliance.
- Risk Focus: care delays, denials, coding defects, workforce strain, and patient safety incidents
- Compliance Focus: clinical quality standards, privacy/security, billing rules, and accreditation requirements
- Outcome Focus: quality measures, access metrics, denial reduction, and patient experience

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Clinical Operations | Healthcare Providers Clinical Operations Lead | Healthcare Providers Clinical Operations Operator |
| Care Coordination | Healthcare Providers Care Coordination Lead | Healthcare Providers Care Coordination Operator |
| Revenue Cycle | Healthcare Providers Revenue Cycle Lead | Healthcare Providers Revenue Cycle Operator |
| Coding & Billing | Healthcare Providers Coding & Billing Lead | Healthcare Providers Coding & Billing Operator |
| Compliance | Healthcare Providers Compliance Lead | Healthcare Providers Compliance Operator |
| Patient Experience | Healthcare Providers Patient Experience Lead | Healthcare Providers Patient Experience Operator |
| Workforce Operations | Healthcare Providers Workforce Operations Lead | Healthcare Providers Workforce Operations Operator |
| Quality Improvement | Healthcare Providers Quality Improvement Lead | Healthcare Providers Quality Improvement Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

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
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
