# Medical Devices Agent Pack

## Scope
This pack defines a full operating model for Medical Devices with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Design, validate, and scale device portfolios with strict quality systems and post-market reliability.
- Risk Focus: verification/validation delays, quality escapes, service failures, and submission risk
- Compliance Focus: QMS obligations, validation traceability, submission rigor, and complaint handling
- Outcome Focus: release readiness, defect rates, field reliability, and service compliance

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Product Engineering | Medical Devices Product Engineering Lead | Medical Devices Product Engineering Operator |
| Clinical Validation | Medical Devices Clinical Validation Lead | Medical Devices Clinical Validation Operator |
| Quality Systems | Medical Devices Quality Systems Lead | Medical Devices Quality Systems Operator |
| Regulatory Submissions | Medical Devices Regulatory Submissions Lead | Medical Devices Regulatory Submissions Operator |
| Manufacturing | Medical Devices Manufacturing Lead | Medical Devices Manufacturing Operator |
| Field Service | Medical Devices Field Service Lead | Medical Devices Field Service Operator |
| Training | Medical Devices Training Lead | Medical Devices Training Operator |
| Post-Market Surveillance | Medical Devices Post-Market Surveillance Lead | Medical Devices Post-Market Surveillance Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/medical-devices-orchestrator.md](agents/medical-devices-orchestrator.md)
- [agents/medical-devices-product-engineering-lead.md](agents/medical-devices-product-engineering-lead.md)
- [agents/medical-devices-product-engineering-operator.md](agents/medical-devices-product-engineering-operator.md)
- [agents/medical-devices-clinical-validation-lead.md](agents/medical-devices-clinical-validation-lead.md)
- [agents/medical-devices-clinical-validation-operator.md](agents/medical-devices-clinical-validation-operator.md)
- [agents/medical-devices-quality-systems-lead.md](agents/medical-devices-quality-systems-lead.md)
- [agents/medical-devices-quality-systems-operator.md](agents/medical-devices-quality-systems-operator.md)
- [agents/medical-devices-regulatory-submissions-lead.md](agents/medical-devices-regulatory-submissions-lead.md)
- [agents/medical-devices-regulatory-submissions-operator.md](agents/medical-devices-regulatory-submissions-operator.md)
- [agents/medical-devices-manufacturing-lead.md](agents/medical-devices-manufacturing-lead.md)
- [agents/medical-devices-manufacturing-operator.md](agents/medical-devices-manufacturing-operator.md)
- [agents/medical-devices-field-service-lead.md](agents/medical-devices-field-service-lead.md)
- [agents/medical-devices-field-service-operator.md](agents/medical-devices-field-service-operator.md)
- [agents/medical-devices-training-lead.md](agents/medical-devices-training-lead.md)
- [agents/medical-devices-training-operator.md](agents/medical-devices-training-operator.md)
- [agents/medical-devices-post-market-surveillance-lead.md](agents/medical-devices-post-market-surveillance-lead.md)
- [agents/medical-devices-post-market-surveillance-operator.md](agents/medical-devices-post-market-surveillance-operator.md)

## Activation Prompt
```
Activate Medical Devices Orchestrator.
Objective: Design, validate, and scale device portfolios with strict quality systems and post-market reliability.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
