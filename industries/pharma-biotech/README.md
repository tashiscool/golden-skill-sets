# Pharma & Biotech Agent Pack

## Scope
This pack defines a full operating model for Pharma & Biotech with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Advance assets from discovery through commercialization with scientific rigor and regulatory readiness.
- Risk Focus: trial delays, safety signal handling, CMC constraints, and access barriers
- Compliance Focus: GxP controls, trial governance, adverse event reporting, and submission standards
- Outcome Focus: milestone velocity, study quality, approval readiness, and launch uptake
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Discovery | knowledge | Pharma & Biotech Discovery Lead | Pharma & Biotech Discovery Operator |
| Preclinical | knowledge | Pharma & Biotech Preclinical Lead | Pharma & Biotech Preclinical Operator |
| Clinical Trials | clinical | Pharma & Biotech Clinical Trials Lead | Pharma & Biotech Clinical Trials Operator |
| Regulatory Affairs | governance | Pharma & Biotech Regulatory Affairs Lead | Pharma & Biotech Regulatory Affairs Operator |
| Pharmacovigilance | clinical | Pharma & Biotech Pharmacovigilance Lead | Pharma & Biotech Pharmacovigilance Operator |
| Manufacturing | operations | Pharma & Biotech Manufacturing Lead | Pharma & Biotech Manufacturing Operator |
| Medical Affairs | clinical | Pharma & Biotech Medical Affairs Lead | Pharma & Biotech Medical Affairs Operator |
| Market Access | strategy | Pharma & Biotech Market Access Lead | Pharma & Biotech Market Access Operator |

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
- Orchestrator: [agents/pharma-biotech-orchestrator.md](agents/pharma-biotech-orchestrator.md)
- [agents/pharma-biotech-discovery-lead.md](agents/pharma-biotech-discovery-lead.md)
- [agents/pharma-biotech-discovery-operator.md](agents/pharma-biotech-discovery-operator.md)
- [agents/pharma-biotech-preclinical-lead.md](agents/pharma-biotech-preclinical-lead.md)
- [agents/pharma-biotech-preclinical-operator.md](agents/pharma-biotech-preclinical-operator.md)
- [agents/pharma-biotech-clinical-trials-lead.md](agents/pharma-biotech-clinical-trials-lead.md)
- [agents/pharma-biotech-clinical-trials-operator.md](agents/pharma-biotech-clinical-trials-operator.md)
- [agents/pharma-biotech-regulatory-affairs-lead.md](agents/pharma-biotech-regulatory-affairs-lead.md)
- [agents/pharma-biotech-regulatory-affairs-operator.md](agents/pharma-biotech-regulatory-affairs-operator.md)
- [agents/pharma-biotech-pharmacovigilance-lead.md](agents/pharma-biotech-pharmacovigilance-lead.md)
- [agents/pharma-biotech-pharmacovigilance-operator.md](agents/pharma-biotech-pharmacovigilance-operator.md)
- [agents/pharma-biotech-manufacturing-lead.md](agents/pharma-biotech-manufacturing-lead.md)
- [agents/pharma-biotech-manufacturing-operator.md](agents/pharma-biotech-manufacturing-operator.md)
- [agents/pharma-biotech-medical-affairs-lead.md](agents/pharma-biotech-medical-affairs-lead.md)
- [agents/pharma-biotech-medical-affairs-operator.md](agents/pharma-biotech-medical-affairs-operator.md)
- [agents/pharma-biotech-market-access-lead.md](agents/pharma-biotech-market-access-lead.md)
- [agents/pharma-biotech-market-access-operator.md](agents/pharma-biotech-market-access-operator.md)

## Activation Prompt
```
Activate Pharma & Biotech Orchestrator.
Objective: Advance assets from discovery through commercialization with scientific rigor and regulatory readiness.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
