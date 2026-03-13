# Advertising & Creative Agency Agent Pack

## Scope
This pack defines a full operating model for Advertising & Creative Agency with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Deliver campaign outcomes across brand and performance work with predictable margin and client trust.
- Risk Focus: strategy-to-execution gaps, media inefficiency, creative misses, and client churn
- Compliance Focus: brand safety, disclosure requirements, data-usage constraints, and contract SLAs
- Outcome Focus: campaign ROI, client retention, utilization, and gross margin
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Strategy | strategy | Advertising & Creative Agency Strategy Lead | Advertising & Creative Agency Strategy Operator |
| Creative | creative | Advertising & Creative Agency Creative Lead | Advertising & Creative Agency Creative Operator |
| Copy | creative | Advertising & Creative Agency Copy Lead | Advertising & Creative Agency Copy Operator |
| Media Planning | growth | Advertising & Creative Agency Media Planning Lead | Advertising & Creative Agency Media Planning Operator |
| Media Buying | growth | Advertising & Creative Agency Media Buying Lead | Advertising & Creative Agency Media Buying Operator |
| Performance Marketing | growth | Advertising & Creative Agency Performance Marketing Lead | Advertising & Creative Agency Performance Marketing Operator |
| Production | operations | Advertising & Creative Agency Production Lead | Advertising & Creative Agency Production Operator |
| Client Services | service | Advertising & Creative Agency Client Services Lead | Advertising & Creative Agency Client Services Operator |

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
- Orchestrator: [agents/advertising-creative-agency-orchestrator.md](agents/advertising-creative-agency-orchestrator.md)
- [agents/advertising-creative-agency-strategy-lead.md](agents/advertising-creative-agency-strategy-lead.md)
- [agents/advertising-creative-agency-strategy-operator.md](agents/advertising-creative-agency-strategy-operator.md)
- [agents/advertising-creative-agency-creative-lead.md](agents/advertising-creative-agency-creative-lead.md)
- [agents/advertising-creative-agency-creative-operator.md](agents/advertising-creative-agency-creative-operator.md)
- [agents/advertising-creative-agency-copy-lead.md](agents/advertising-creative-agency-copy-lead.md)
- [agents/advertising-creative-agency-copy-operator.md](agents/advertising-creative-agency-copy-operator.md)
- [agents/advertising-creative-agency-media-planning-lead.md](agents/advertising-creative-agency-media-planning-lead.md)
- [agents/advertising-creative-agency-media-planning-operator.md](agents/advertising-creative-agency-media-planning-operator.md)
- [agents/advertising-creative-agency-media-buying-lead.md](agents/advertising-creative-agency-media-buying-lead.md)
- [agents/advertising-creative-agency-media-buying-operator.md](agents/advertising-creative-agency-media-buying-operator.md)
- [agents/advertising-creative-agency-performance-marketing-lead.md](agents/advertising-creative-agency-performance-marketing-lead.md)
- [agents/advertising-creative-agency-performance-marketing-operator.md](agents/advertising-creative-agency-performance-marketing-operator.md)
- [agents/advertising-creative-agency-production-lead.md](agents/advertising-creative-agency-production-lead.md)
- [agents/advertising-creative-agency-production-operator.md](agents/advertising-creative-agency-production-operator.md)
- [agents/advertising-creative-agency-client-services-lead.md](agents/advertising-creative-agency-client-services-lead.md)
- [agents/advertising-creative-agency-client-services-operator.md](agents/advertising-creative-agency-client-services-operator.md)

## Activation Prompt
```
Activate Advertising & Creative Agency Orchestrator.
Objective: Deliver campaign outcomes across brand and performance work with predictable margin and client trust.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
