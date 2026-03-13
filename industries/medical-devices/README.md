# Medical Devices Agent Pack

## Scope
This pack defines a full operating model for Medical Devices with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Design, validate, and scale device portfolios with strict quality systems and post-market reliability.
- Risk Focus: verification/validation delays, quality escapes, service failures, and submission risk
- Compliance Focus: QMS obligations, validation traceability, submission rigor, and complaint handling
- Outcome Focus: release readiness, defect rates, field reliability, and service compliance
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Product Engineering | technical | Medical Devices Product Engineering Lead | Medical Devices Product Engineering Operator |
| Clinical Validation | clinical | Medical Devices Clinical Validation Lead | Medical Devices Clinical Validation Operator |
| Quality Systems | governance | Medical Devices Quality Systems Lead | Medical Devices Quality Systems Operator |
| Regulatory Submissions | governance | Medical Devices Regulatory Submissions Lead | Medical Devices Regulatory Submissions Operator |
| Manufacturing | operations | Medical Devices Manufacturing Lead | Medical Devices Manufacturing Operator |
| Field Service | service | Medical Devices Field Service Lead | Medical Devices Field Service Operator |
| Training | service | Medical Devices Training Lead | Medical Devices Training Operator |
| Post-Market Surveillance | governance | Medical Devices Post-Market Surveillance Lead | Medical Devices Post-Market Surveillance Operator |

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
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
