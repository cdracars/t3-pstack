---
name: pstack-correct
description: Find repeated agent mistakes in a project and prevent their recurrence with architecture, types, checks or behavior tests grounded in actual past failures.
license: MIT
---

# Prevent repeated mistakes

Read [the runtime adapter](references/runtime.md). Inspect the scoped recent changes, reversions, review findings and agent instructions. A recurring class needs at least two concrete instances. Do not turn a single preference or a hypothetical hazard into a global rule.

Choose a small, frequent class to address within the task. First consider whether one state owner, one supported API, a derived inventory or a better boundary removes the mistake. Then consider type constraints, a deterministic lint or CI check, and a behavioral regression test. Prefer an existing project tool over new infrastructure. Write prose rules for the judgment that remains.

Prove the enforcement fails on a real past mistake or a faithful isolated reproduction, then passes on the intended behavior. Explain what it cannot detect. Keep fixtures and experiments away from the user's active state. Do not claim the new rule prevents all variants from one example.

If the repo maintains a rule-to-check table, update it. Otherwise document the check beside the code or existing contributor guidance where it is actually needed. Preserve the project's standards and exception process. Do not invent mandatory expiry dates or human approvals.

Return the mistake class, its two evidence pointers, the selected enforcement, the failing and passing results, and any remaining judgment. Matt retro can identify candidates; this skill implements a demonstrated correction when the request authorizes it.
