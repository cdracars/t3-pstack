---
name: pstack-maintain-verification-skill
description: Audit an existing project verification skill and feature map against source and real app behavior, repairing proven documentation or harness drift.
license: MIT
---

# Maintain an existing verification skill

Read [the runtime adapter](references/runtime.md). Locate the project's verification skill and feature map. If several match, ask which one; if none exists, report that and suggest pstack-create-verification-skill.

Keep edits inside the verification skill and its owned helpers. A product regression is a finding, not permission to change the app or rewrite expected behavior around a bug.

Check that the feature index matches its files. For each mapped feature, trace source entry points and derive one user journey. Inspect recent changes for omitted features with concrete source evidence. Group journeys that can share a valid starting state. Use one controlled app driver at a time for shared state.

Exercise every mapped feature using the skill's own readiness, launch and cleanup rules. Recheck health after surprising behavior. Reset a wedged session rather than continuing from an unknown state. Capture unreachable prerequisites and the attempted path. Preserve evidence even when a drive fails.

Classify findings as documentation drift, a harness gap or a product gap. Repair proven documentation and harness drift within scope, then rerun the affected journey. If a map correction would conceal a regression, report the regression instead. Reconcile coverage against every feature entry.

Return clean, changed or blocked, with feature coverage, evidence, edits and remaining limits. Clean requires source and live coverage for the mapped features. Partial coverage is explicit. Follow the user's existing delivery policy; do not create a PR merely because the source skill describes one.
