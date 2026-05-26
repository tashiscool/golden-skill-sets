# Construction & AEC Agent Pack

## Scope
This pack defines a full operating model for Construction & AEC with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Plan and deliver projects safely, on schedule, and on budget with strong quality outcomes.
- Risk Focus: scope changes, safety incidents, procurement delays, and schedule/cost overrun
- Compliance Focus: building codes, safety requirements, contract terms, and inspection standards
- Outcome Focus: schedule adherence, cost variance, safety performance, and punchlist closure
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Estimating | analytics | Construction & AEC Estimating Lead | Construction & AEC Estimating Operator |
| Design | technical | Construction & AEC Design Lead | Construction & AEC Design Operator |
| BIM | technical | Construction & AEC BIM Lead | Construction & AEC BIM Operator |
| Procurement | operations | Construction & AEC Procurement Lead | Construction & AEC Procurement Operator |
| Site Operations | operations | Construction & AEC Site Operations Lead | Construction & AEC Site Operations Operator |
| Safety | governance | Construction & AEC Safety Lead | Construction & AEC Safety Operator |
| QA/QC | governance | Construction & AEC QA/QC Lead | Construction & AEC QA/QC Operator |
| Project Controls | analytics | Construction & AEC Project Controls Lead | Construction & AEC Project Controls Operator |

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
- Orchestrator: [agents/construction-aec-orchestrator.md](agents/construction-aec-orchestrator.md)
- [agents/construction-aec-estimating-lead.md](agents/construction-aec-estimating-lead.md)
- [agents/construction-aec-estimating-operator.md](agents/construction-aec-estimating-operator.md)
- [agents/construction-aec-design-lead.md](agents/construction-aec-design-lead.md)
- [agents/construction-aec-design-operator.md](agents/construction-aec-design-operator.md)
- [agents/construction-aec-bim-lead.md](agents/construction-aec-bim-lead.md)
- [agents/construction-aec-bim-operator.md](agents/construction-aec-bim-operator.md)
- [agents/construction-aec-procurement-lead.md](agents/construction-aec-procurement-lead.md)
- [agents/construction-aec-procurement-operator.md](agents/construction-aec-procurement-operator.md)
- [agents/construction-aec-site-operations-lead.md](agents/construction-aec-site-operations-lead.md)
- [agents/construction-aec-site-operations-operator.md](agents/construction-aec-site-operations-operator.md)
- [agents/construction-aec-safety-lead.md](agents/construction-aec-safety-lead.md)
- [agents/construction-aec-safety-operator.md](agents/construction-aec-safety-operator.md)
- [agents/construction-aec-qa-qc-lead.md](agents/construction-aec-qa-qc-lead.md)
- [agents/construction-aec-qa-qc-operator.md](agents/construction-aec-qa-qc-operator.md)
- [agents/construction-aec-project-controls-lead.md](agents/construction-aec-project-controls-lead.md)
- [agents/construction-aec-project-controls-operator.md](agents/construction-aec-project-controls-operator.md)

## Activation Prompt
```
Activate Construction & AEC Orchestrator.
Objective: Plan and deliver projects safely, on schedule, and on budget with strong quality outcomes.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
