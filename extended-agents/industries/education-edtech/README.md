# Education & EdTech Agent Pack

## Scope
This pack defines a full operating model for Education & EdTech with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Deliver measurable learner outcomes through robust curriculum, platform reliability, and student support.
- Risk Focus: outcome gaps, content quality drift, low completion, and support bottlenecks
- Compliance Focus: accreditation standards, privacy requirements, accessibility rules, and assessment integrity
- Outcome Focus: completion, mastery gains, retention, and satisfaction
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Curriculum | knowledge | Education & EdTech Curriculum Lead | Education & EdTech Curriculum Operator |
| Instructional Design | knowledge | Education & EdTech Instructional Design Lead | Education & EdTech Instructional Design Operator |
| Assessment | knowledge | Education & EdTech Assessment Lead | Education & EdTech Assessment Operator |
| Student Success | service | Education & EdTech Student Success Lead | Education & EdTech Student Success Operator |
| Admissions | adjudication | Education & EdTech Admissions Lead | Education & EdTech Admissions Operator |
| Platform & Product | technical | Education & EdTech Platform & Product Lead | Education & EdTech Platform & Product Operator |
| Compliance & Accreditation | governance | Education & EdTech Compliance & Accreditation Lead | Education & EdTech Compliance & Accreditation Operator |
| Outcomes Analytics | analytics | Education & EdTech Outcomes Analytics Lead | Education & EdTech Outcomes Analytics Operator |

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
- Orchestrator: [agents/education-edtech-orchestrator.md](agents/education-edtech-orchestrator.md)
- [agents/education-edtech-curriculum-lead.md](agents/education-edtech-curriculum-lead.md)
- [agents/education-edtech-curriculum-operator.md](agents/education-edtech-curriculum-operator.md)
- [agents/education-edtech-instructional-design-lead.md](agents/education-edtech-instructional-design-lead.md)
- [agents/education-edtech-instructional-design-operator.md](agents/education-edtech-instructional-design-operator.md)
- [agents/education-edtech-assessment-lead.md](agents/education-edtech-assessment-lead.md)
- [agents/education-edtech-assessment-operator.md](agents/education-edtech-assessment-operator.md)
- [agents/education-edtech-student-success-lead.md](agents/education-edtech-student-success-lead.md)
- [agents/education-edtech-student-success-operator.md](agents/education-edtech-student-success-operator.md)
- [agents/education-edtech-admissions-lead.md](agents/education-edtech-admissions-lead.md)
- [agents/education-edtech-admissions-operator.md](agents/education-edtech-admissions-operator.md)
- [agents/education-edtech-platform-product-lead.md](agents/education-edtech-platform-product-lead.md)
- [agents/education-edtech-platform-product-operator.md](agents/education-edtech-platform-product-operator.md)
- [agents/education-edtech-compliance-accreditation-lead.md](agents/education-edtech-compliance-accreditation-lead.md)
- [agents/education-edtech-compliance-accreditation-operator.md](agents/education-edtech-compliance-accreditation-operator.md)
- [agents/education-edtech-outcomes-analytics-lead.md](agents/education-edtech-outcomes-analytics-lead.md)
- [agents/education-edtech-outcomes-analytics-operator.md](agents/education-edtech-outcomes-analytics-operator.md)

## Activation Prompt
```
Activate Education & EdTech Orchestrator.
Objective: Deliver measurable learner outcomes through robust curriculum, platform reliability, and student support.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
