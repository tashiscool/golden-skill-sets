# Expected Output Shape

## Feedback Loop

- Identify the fastest deterministic repro path: test, script, trace replay, browser flow, or captured payload.
- Ask for missing artifacts if production-only context is required.

## Reproduction

- Confirm the symptom matches the user's conversion regression, not a nearby failure.

## Hypotheses

- Provide 3-5 ranked falsifiable hypotheses.
- State what evidence would confirm or falsify each one.

## Fix Plan

- Instrument narrowly.
- Write or identify a regression test at the correct seam.
- Apply the smallest fix after reproduction.
- Rerun the original loop.

## Done Means

- Original repro no longer fails.
- Regression test passes.
- Debug instrumentation is removed.
- Remaining risk is stated.
