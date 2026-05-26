# Gaming Agent Pack

## Scope
This pack defines a full operating model for Gaming with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Ship and operate high-retention game experiences with healthy live operations and monetization.
- Risk Focus: scope creep, quality regressions, liveops instability, and economy imbalance
- Compliance Focus: platform certification, content/rating standards, privacy obligations, and anti-cheat policy
- Outcome Focus: retention, ARPDAU, release quality, and live-service stability
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Game Design | strategy | Gaming Game Design Lead | Gaming Game Design Operator |
| Engineering | technical | Gaming Engineering Lead | Gaming Engineering Operator |
| Art & Animation | creative | Gaming Art & Animation Lead | Gaming Art & Animation Operator |
| Narrative & Audio | creative | Gaming Narrative & Audio Lead | Gaming Narrative & Audio Operator |
| QA | governance | Gaming QA Lead | Gaming QA Operator |
| LiveOps | operations | Gaming LiveOps Lead | Gaming LiveOps Operator |
| Monetization | growth | Gaming Monetization Lead | Gaming Monetization Operator |
| Community | service | Gaming Community Lead | Gaming Community Operator |

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
- Orchestrator: [agents/gaming-orchestrator.md](agents/gaming-orchestrator.md)
- [agents/gaming-game-design-lead.md](agents/gaming-game-design-lead.md)
- [agents/gaming-game-design-operator.md](agents/gaming-game-design-operator.md)
- [agents/gaming-engineering-lead.md](agents/gaming-engineering-lead.md)
- [agents/gaming-engineering-operator.md](agents/gaming-engineering-operator.md)
- [agents/gaming-art-animation-lead.md](agents/gaming-art-animation-lead.md)
- [agents/gaming-art-animation-operator.md](agents/gaming-art-animation-operator.md)
- [agents/gaming-narrative-audio-lead.md](agents/gaming-narrative-audio-lead.md)
- [agents/gaming-narrative-audio-operator.md](agents/gaming-narrative-audio-operator.md)
- [agents/gaming-qa-lead.md](agents/gaming-qa-lead.md)
- [agents/gaming-qa-operator.md](agents/gaming-qa-operator.md)
- [agents/gaming-liveops-lead.md](agents/gaming-liveops-lead.md)
- [agents/gaming-liveops-operator.md](agents/gaming-liveops-operator.md)
- [agents/gaming-monetization-lead.md](agents/gaming-monetization-lead.md)
- [agents/gaming-monetization-operator.md](agents/gaming-monetization-operator.md)
- [agents/gaming-community-lead.md](agents/gaming-community-lead.md)
- [agents/gaming-community-operator.md](agents/gaming-community-operator.md)

## Activation Prompt
```
Activate Gaming Orchestrator.
Objective: Ship and operate high-retention game experiences with healthy live operations and monetization.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
