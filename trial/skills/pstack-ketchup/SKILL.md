---
name: pstack-ketchup
description: Catch the user up on changes in the current conversation since their last message, with current status and any decisions only they can make.
license: MIT
---

# Catch the user up

Read [the runtime adapter](references/runtime.md). Keep this pass read-only. Summarize changes since the last message the user wrote before asking for this catch-up. Agent notifications and tool results do not reset that window.

Collect completed work, open work and reports received. Check current PR or task status with available read-only tools when the conversation touched them. Distinguish observed state from a worker's unverified report. Correct any changed number before repeating it. Use only existing evidence for visuals.

Explain what changed in plain language, briefly enough to read at a glance. Give deeper context only where the user needs it to decide. Name projects and PRs by recognizable titles and link the actual artifacts. Keep hashes, test counts and internal paths out unless they help the user act.

List every still-pending decision that requires the user, including older unresolved ones. For each, explain the options, your recommendation, the evidence and any unknown that changes the choice. Never invent an approval or ask the user to do work the agent can already complete. State remaining agent work separately. If no decision is waiting on the user, say so or omit the decision list.

Use unslop when installed. For context across prior conversations, use pstack-recall instead.
