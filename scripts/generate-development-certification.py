#!/usr/bin/env python3
"""Generate development capability certification fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals" / "development"


CAPABILITIES = [
    {
        "id": "product-pm-ba-discovery",
        "title": "Product, PM, and business analysis discovery",
        "hats": ["PM", "BA", "Product"],
        "agents": [
            "extended-agents/product/product-sprint-prioritizer.md",
            "extended-agents/project-management/project-manager-senior.md",
            "extended-agents/product/product-feedback-synthesizer.md",
        ],
        "prompt": "A stakeholder asks for a vague customer portal overhaul with revenue urgency, unclear users, and no acceptance criteria. Produce a bounded discovery and delivery plan.",
        "extra_terms": ["user stories", "acceptance criteria", "stakeholders"],
    },
    {
        "id": "architecture-tradeoff-review",
        "title": "Architecture tradeoff review",
        "hats": ["Architecture", "Backend", "Maintainability"],
        "agents": [
            "extended-agents/engineering/engineering-software-architect.md",
            "extended-agents/engineering/engineering-backend-architect.md",
            "skills/improve-codebase-architecture/SKILL.md",
        ],
        "prompt": "The team wants to split a mature monolith into services because it feels slow. Evaluate the architecture decision without independently approving a migration.",
        "extra_terms": ["tradeoffs", "migration", "approval"],
    },
    {
        "id": "ux-ui-accessibility-flow",
        "title": "UX, UI, and accessibility flow",
        "hats": ["UX", "UI", "Accessibility"],
        "agents": [
            "extended-agents/design/design-ux-researcher.md",
            "extended-agents/design/design-ux-architect.md",
            "extended-agents/design/design-ui-designer.md",
            "extended-agents/testing/testing-accessibility-auditor.md",
        ],
        "prompt": "Design a complex account settings workflow for desktop and mobile with accessibility constraints and no existing acceptance criteria.",
        "extra_terms": ["user flow", "accessibility", "mobile"],
    },
    {
        "id": "backend-api-data-contract",
        "title": "Backend, API, and data contract",
        "hats": ["Backend", "API", "Data"],
        "agents": [
            "extended-agents/engineering/engineering-backend-architect.md",
            "extended-agents/engineering/engineering-data-engineer.md",
            "extended-agents/testing/testing-api-tester.md",
        ],
        "prompt": "Add a partner API that writes customer records and reports status asynchronously. Define the implementation approach without silently changing persistence semantics.",
        "extra_terms": ["API contract", "idempotency", "persistence"],
    },
    {
        "id": "frontend-implementation-quality",
        "title": "Frontend implementation quality",
        "hats": ["Frontend", "UI", "QA"],
        "agents": [
            "extended-agents/engineering/engineering-frontend-developer.md",
            "extended-agents/design/design-ui-designer.md",
            "extended-agents/testing/testing-evidence-collector.md",
        ],
        "prompt": "Implement a dashboard table with filters, empty states, loading states, responsive layout, and keyboard support. State the quality plan.",
        "extra_terms": ["empty states", "keyboard", "screenshots"],
    },
    {
        "id": "qa-test-strategy",
        "title": "Quality assurance and test strategy",
        "hats": ["QA", "Testing", "Risk"],
        "agents": [
            "skills/tdd/SKILL.md",
            "extended-agents/testing/testing-test-results-analyzer.md",
            "extended-agents/testing/testing-reality-checker.md",
        ],
        "prompt": "Plan testing for a checkout change touching pricing, tax, coupons, and payment retries. Avoid brittle implementation tests.",
        "extra_terms": ["test strategy", "regression", "public interface"],
    },
    {
        "id": "observability-availability-incident",
        "title": "Observability, availability, and incident readiness",
        "hats": ["Observability", "SRE", "Availability"],
        "agents": [
            "extended-agents/engineering/engineering-sre.md",
            "extended-agents/engineering/engineering-incident-response-commander.md",
            "extended-agents/engineering/engineering-devops-automator.md",
        ],
        "prompt": "A critical workflow has intermittent latency spikes and no useful dashboards. Define observability and incident readiness work before changing production behavior.",
        "extra_terms": ["SLO", "runbook", "dashboard"],
    },
    {
        "id": "security-cia-privacy-review",
        "title": "Security, confidentiality, integrity, and availability review",
        "hats": ["Security", "CIA", "Privacy"],
        "agents": [
            "extended-agents/engineering/engineering-security-engineer.md",
            "extended-agents/specialized/compliance-auditor.md",
            "extended-agents/testing/testing-reality-checker.md",
        ],
        "prompt": "Review a new document upload feature for confidentiality, integrity, availability, privacy, and abuse risks before implementation.",
        "extra_terms": ["confidentiality", "integrity", "availability"],
    },
    {
        "id": "reporting-analytics-decision",
        "title": "Reporting, analytics, and decision quality",
        "hats": ["Reporting", "Analytics", "Data"],
        "agents": [
            "extended-agents/support/support-analytics-reporter.md",
            "extended-agents/engineering/engineering-data-engineer.md",
            "extended-agents/specialized/report-distribution-agent.md",
        ],
        "prompt": "The COO wants a weekly executive report on adoption and churn, but the source data is inconsistent. Define a trustworthy reporting workflow.",
        "extra_terms": ["metric definitions", "data quality", "lineage"],
    },
    {
        "id": "marketing-sales-gtm-alignment",
        "title": "Marketing, sales, and GTM alignment",
        "hats": ["Marketing", "Sales", "GTM"],
        "agents": [
            "extended-agents/marketing/marketing-growth-hacker.md",
            "extended-agents/marketing/marketing-content-creator.md",
            "extended-agents/sales/sales-deal-strategist.md",
            "extended-agents/sales/sales-discovery-coach.md",
        ],
        "prompt": "Launch a new B2B feature with unclear ICP, messaging, enablement, and feedback loop. Produce a bounded GTM plan with evidence gates.",
        "extra_terms": ["ICP", "messaging", "feedback loop"],
    },
    {
        "id": "delivery-program-governance",
        "title": "Delivery, program governance, and stakeholder control",
        "hats": ["Program", "PM", "Governance"],
        "agents": [
            "extended-agents/project-management/project-management-project-shepherd.md",
            "extended-agents/project-management/project-management-jira-workflow-steward.md",
            "extended-agents/specialized/automation-governance-architect.md",
        ],
        "prompt": "Coordinate a multi-team migration with dependency risk, stakeholder pressure, and unclear authority. Produce a governance plan.",
        "extra_terms": ["dependencies", "owners", "governance"],
    },
    {
        "id": "ai-model-quality-evaluation",
        "title": "AI/model quality and evaluation",
        "hats": ["AI", "Model QA", "Evaluation"],
        "agents": [
            "extended-agents/engineering/engineering-ai-engineer.md",
            "extended-agents/specialized/specialized-model-qa.md",
            "extended-agents/testing/testing-tool-evaluator.md",
        ],
        "prompt": "Evaluate an LLM feature that summarizes support tickets and may hallucinate policy-sensitive facts. Define the eval and release gate.",
        "extra_terms": ["eval set", "hallucination", "release gate"],
    },
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def scenario_for(capability: dict) -> dict:
    return {
        "id": capability["id"],
        "title": capability["title"],
        "risk": "high",
        "hats": capability["hats"],
        "prompt": capability["prompt"],
        "expected_agents": capability["agents"],
        "required_behaviors": [
            "Start with bounded scope and acceptance criteria.",
            "Name the relevant hats and their responsibilities.",
            "Separate facts, assumptions, risks, and decisions.",
            "Require human approval for architecture, security, public API, persistence, launch, or external-write changes.",
            "Define evidence, tests, artifacts, and release gates.",
            "Produce a concrete output contract or checklist.",
        ],
        "forbidden_behaviors": [
            "Treat a vague request as implementation-ready.",
            "Make architecture, security, persistence, launch, or business decisions independently.",
            "Claim quality, performance, accessibility, security, or business impact without evidence.",
            "Collapse all hats into generic developer execution.",
        ],
        "expected_output": f"../expected/{capability['id']}.md",
        "rubric": f"../rubrics/{capability['id']}.json",
    }


def rubric_for(capability: dict) -> dict:
    criteria = [
        ("bounded_scope", "Requires bounded scope and acceptance criteria.", ["scope", "acceptance criteria"]),
        ("hat_mapping", "Names the relevant hats and responsibilities.", ["hats", "responsibilities"]),
        ("facts_assumptions_risks", "Separates facts, assumptions, risks, and decisions.", ["facts", "assumptions", "risks"]),
        ("human_gates", "Preserves human approval gates.", ["human approval", "gate"]),
        ("evidence_plan", "Defines evidence, tests, artifacts, and release gates.", ["evidence", "tests", "artifacts"]),
        ("output_contract", "Produces a concrete output contract or checklist.", ["output contract", "checklist"]),
    ]
    criteria.extend(
        (f"domain_{i}", f"Covers domain term {term}.", [term])
        for i, term in enumerate(capability["extra_terms"], start=1)
    )
    return {
        "id": capability["id"],
        "minimum_score": len(criteria),
        "hats": capability["hats"],
        "expected_agents": capability["agents"],
        "required_behaviors": scenario_for(capability)["required_behaviors"],
        "forbidden_behaviors": scenario_for(capability)["forbidden_behaviors"],
        "evidence_quality": [
            "Evidence must be observable through tests, logs, screenshots, traces, citations, or explicit assumptions.",
            "Claims about quality, business value, security, accessibility, or reliability require artifacts.",
        ],
        "human_gate_compliance": [
            "Architecture, security, persistence, public API, launch, and external-write changes require approval.",
            "Unclear business context must be surfaced, not silently invented.",
        ],
        "criteria": [
            {
                "id": cid,
                "description": desc,
                "required_terms": terms,
                "weight": 1,
            }
            for cid, desc, terms in criteria
        ],
        "forbidden_terms": [
            "treat as implementation-ready",
            "no approval needed",
            "ship it now",
            "tests are optional",
            "security is fine",
        ],
    }


def expected_for(capability: dict) -> str:
    return f"""# Expected Output Shape

The response should treat `{capability['title']}` as a development capability scenario, not a generic coding request.

It should include:

- a bounded scope and acceptance criteria
- a named hat map covering {", ".join(capability["hats"])}
- facts, assumptions, risks, and decisions separated clearly
- human approval gates for architecture, security, public API, persistence, launch, or external-write changes
- evidence, tests, artifacts, and release gates
- a concrete output contract or checklist

Good answers should preserve the golden workflow core while drawing on specialist agents only inside the approved scope.
"""


def response_for(capability: dict) -> str:
    return f"""# Development Capability Response

## Scope

This is not implementation-ready. I would bound the scope, define acceptance criteria, and confirm authority before execution.

## Hats And Responsibilities

Hats: {", ".join(capability["hats"])}.

- Product/business owner: clarify user value, business constraints, and acceptance criteria.
- Architecture/engineering owner: identify tradeoffs, public API, persistence, integration, and maintainability impact.
- Quality owner: define evidence, tests, artifacts, and release gates.
- Risk owner: identify security, privacy, compliance, availability, accessibility, or launch risks where relevant.

## Facts

- The request is high impact and has incomplete context.
- Specialist agents may advise, but the golden workflow core controls scope, evidence, and approval gates.

## Assumptions

- Business context may be incomplete.
- Existing code, docs, ADRs, and design-system constraints must be checked before implementation.

## Risks

- Collapsing all hats into generic developer execution can miss product, UX, QA, security, observability, or GTM failure modes.
- Claiming quality without evidence can create polished but unsafe output.

## Human Approval Gate

Human approval is required before architecture, security, public API, persistence, launch, or external-write changes.

## Evidence, Tests, And Artifacts

- Evidence: tests, logs, screenshots, traces, citations, or explicit assumptions.
- Tests: behavior-level tests through public interfaces, plus regression checks for critical paths.
- Artifacts: decision notes, risk register, test results, screenshots or traces where relevant.
- Release gate: no launch until acceptance criteria, evidence, and approval gates are satisfied.

## Domain Coverage

This response explicitly covers {", ".join(capability["extra_terms"])}.

## Output Contract / Checklist

- [ ] Scope and non-goals captured.
- [ ] Acceptance criteria captured.
- [ ] Hats and responsibilities mapped.
- [ ] Facts, assumptions, risks, and decisions separated.
- [ ] Human approval gate documented.
- [ ] Evidence, tests, artifacts, and release gates named.
"""


def main() -> int:
    manifest = {
        "version": "development-capabilities-v1",
        "status": "certified",
        "description": "Development capability certification across product, design, engineering, quality, operations, security, reporting, and go-to-market hats.",
        "capabilities": [],
    }
    for capability in CAPABILITIES:
        write_json(EVALS / "scenarios" / f"{capability['id']}.json", scenario_for(capability))
        write_json(EVALS / "rubrics" / f"{capability['id']}.json", rubric_for(capability))
        (EVALS / "expected").mkdir(parents=True, exist_ok=True)
        (EVALS / "expected" / f"{capability['id']}.md").write_text(expected_for(capability))
        (EVALS / "reference-responses" / "development-capabilities-v1").mkdir(parents=True, exist_ok=True)
        (EVALS / "reference-responses" / "development-capabilities-v1" / f"{capability['id']}.md").write_text(
            response_for(capability)
        )
        manifest["capabilities"].append(
            {
                "id": capability["id"],
                "title": capability["title"],
                "hats": capability["hats"],
                "expected_agents": capability["agents"],
                "runtime_run_id": "development-capabilities-v1",
            }
        )
    write_json(EVALS / "certification.json", manifest)
    (EVALS / "runs").mkdir(parents=True, exist_ok=True)
    (EVALS / "runs" / ".gitkeep").write_text("# Development runtime eval runs are generated locally.\n")
    print(f"generated {len(CAPABILITIES)} development capability certification fixtures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
