# Sports Agent Pack

## Scope
This pack defines a full operating model for Sports with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Optimize team and business performance across competition, fan growth, and commercial operations.
- Risk Focus: injury/availability risk, roster inefficiency, event-day failures, and sponsor underperformance
- Compliance Focus: league rules, medical standards, event safety, and sponsorship contract obligations
- Outcome Focus: competitive performance, attendance, fan engagement, and commercial yield

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Team Operations | Sports Team Operations Lead | Sports Team Operations Operator |
| Coaching & Performance | Sports Coaching & Performance Lead | Sports Coaching & Performance Operator |
| Medical & Recovery | Sports Medical & Recovery Lead | Sports Medical & Recovery Operator |
| Scouting & Recruiting | Sports Scouting & Recruiting Lead | Sports Scouting & Recruiting Operator |
| Media & Content | Sports Media & Content Lead | Sports Media & Content Operator |
| Sponsorship | Sports Sponsorship Lead | Sports Sponsorship Operator |
| Ticketing | Sports Ticketing Lead | Sports Ticketing Operator |
| Fan Engagement | Sports Fan Engagement Lead | Sports Fan Engagement Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/sports-orchestrator.md](agents/sports-orchestrator.md)
- [agents/sports-team-operations-lead.md](agents/sports-team-operations-lead.md)
- [agents/sports-team-operations-operator.md](agents/sports-team-operations-operator.md)
- [agents/sports-coaching-performance-lead.md](agents/sports-coaching-performance-lead.md)
- [agents/sports-coaching-performance-operator.md](agents/sports-coaching-performance-operator.md)
- [agents/sports-medical-recovery-lead.md](agents/sports-medical-recovery-lead.md)
- [agents/sports-medical-recovery-operator.md](agents/sports-medical-recovery-operator.md)
- [agents/sports-scouting-recruiting-lead.md](agents/sports-scouting-recruiting-lead.md)
- [agents/sports-scouting-recruiting-operator.md](agents/sports-scouting-recruiting-operator.md)
- [agents/sports-media-content-lead.md](agents/sports-media-content-lead.md)
- [agents/sports-media-content-operator.md](agents/sports-media-content-operator.md)
- [agents/sports-sponsorship-lead.md](agents/sports-sponsorship-lead.md)
- [agents/sports-sponsorship-operator.md](agents/sports-sponsorship-operator.md)
- [agents/sports-ticketing-lead.md](agents/sports-ticketing-lead.md)
- [agents/sports-ticketing-operator.md](agents/sports-ticketing-operator.md)
- [agents/sports-fan-engagement-lead.md](agents/sports-fan-engagement-lead.md)
- [agents/sports-fan-engagement-operator.md](agents/sports-fan-engagement-operator.md)

## Activation Prompt
```
Activate Sports Orchestrator.
Objective: Optimize team and business performance across competition, fan growth, and commercial operations.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
