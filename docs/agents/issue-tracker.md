# Issue Tracker: GitHub

Issues and PRDs for this repo live as GitHub issues. Use the `gh` CLI for issue operations.

## Conventions

- Create an issue: `gh issue create --title "..." --body "..."`
- Read an issue: `gh issue view <number> --comments`
- List issues: `gh issue list --state open --json number,title,body,labels,comments`
- Comment on an issue: `gh issue comment <number> --body "..."`
- Apply labels: `gh issue edit <number> --add-label "..."`
- Remove labels: `gh issue edit <number> --remove-label "..."`
- Close an issue: `gh issue close <number> --comment "..."`

Infer the repo from `git remote -v`; `gh` handles this automatically from inside the clone.

## Skill Semantics

When a skill says "publish to the issue tracker", create a GitHub issue.

When a skill says "fetch the relevant issue", run `gh issue view <number> --comments`.

Do not close issues, mark work `wontfix`, or mark work `ready-for-agent` without explicit human confirmation unless the user directly asked for that exact transition.
