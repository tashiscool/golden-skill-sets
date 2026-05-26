# Cybersecurity Agent Pack

## Scope
This pack defines a full operating model for Cybersecurity with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Reduce threat exposure and response time through integrated prevention, detection, and recovery operations.
- Risk Focus: control gaps, alert fatigue, delayed containment, and policy drift
- Compliance Focus: security frameworks, audit requirements, incident reporting, and identity governance
- Outcome Focus: risk reduction, detection/response speed, control coverage, and audit pass rate
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Threat Intelligence | analytics | Cybersecurity Threat Intelligence Lead | Cybersecurity Threat Intelligence Operator |
| Security Engineering | technical | Cybersecurity Security Engineering Lead | Cybersecurity Security Engineering Operator |
| SOC | operations | Cybersecurity SOC Lead | Cybersecurity SOC Operator |
| Incident Response | operations | Cybersecurity Incident Response Lead | Cybersecurity Incident Response Operator |
| GRC | governance | Cybersecurity GRC Lead | Cybersecurity GRC Operator |
| IAM | technical | Cybersecurity IAM Lead | Cybersecurity IAM Operator |
| AppSec | technical | Cybersecurity AppSec Lead | Cybersecurity AppSec Operator |
| Security Education | service | Cybersecurity Security Education Lead | Cybersecurity Security Education Operator |

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
- Orchestrator: [agents/cybersecurity-industry-orchestrator.md](agents/cybersecurity-industry-orchestrator.md)
- [agents/cybersecurity-industry-threat-intelligence-lead.md](agents/cybersecurity-industry-threat-intelligence-lead.md)
- [agents/cybersecurity-industry-threat-intelligence-operator.md](agents/cybersecurity-industry-threat-intelligence-operator.md)
- [agents/cybersecurity-industry-security-engineering-lead.md](agents/cybersecurity-industry-security-engineering-lead.md)
- [agents/cybersecurity-industry-security-engineering-operator.md](agents/cybersecurity-industry-security-engineering-operator.md)
- [agents/cybersecurity-industry-soc-lead.md](agents/cybersecurity-industry-soc-lead.md)
- [agents/cybersecurity-industry-soc-operator.md](agents/cybersecurity-industry-soc-operator.md)
- [agents/cybersecurity-industry-incident-response-lead.md](agents/cybersecurity-industry-incident-response-lead.md)
- [agents/cybersecurity-industry-incident-response-operator.md](agents/cybersecurity-industry-incident-response-operator.md)
- [agents/cybersecurity-industry-grc-lead.md](agents/cybersecurity-industry-grc-lead.md)
- [agents/cybersecurity-industry-grc-operator.md](agents/cybersecurity-industry-grc-operator.md)
- [agents/cybersecurity-industry-iam-lead.md](agents/cybersecurity-industry-iam-lead.md)
- [agents/cybersecurity-industry-iam-operator.md](agents/cybersecurity-industry-iam-operator.md)
- [agents/cybersecurity-industry-appsec-lead.md](agents/cybersecurity-industry-appsec-lead.md)
- [agents/cybersecurity-industry-appsec-operator.md](agents/cybersecurity-industry-appsec-operator.md)
- [agents/cybersecurity-industry-security-education-lead.md](agents/cybersecurity-industry-security-education-lead.md)
- [agents/cybersecurity-industry-security-education-operator.md](agents/cybersecurity-industry-security-education-operator.md)

## Activation Prompt
```
Activate Cybersecurity Orchestrator.
Objective: Reduce threat exposure and response time through integrated prevention, detection, and recovery operations.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
