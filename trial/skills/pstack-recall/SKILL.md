---
name: pstack-recall
description: Reconstruct project context from prior chats, notes and current artifacts before resuming work, including open decisions and the next concrete action.
license: MIT
---

# Recall project work

Read [the runtime adapter](references/runtime.md) for history discovery and tool routing.

Use the user's topic and time window. If none is given, state a seven-day window within the active project and proceed. A request for all history retains that scope. If the user supplied a complete current-state brief, use it instead of mining the same material again.

Search the project wiki, handoffs and relevant transcripts. Identify the goal, decisions, attempted fixes, reversions, remaining work and source artifacts. Separate original user statements from agent suggestions, relays and duplicate imports. Keep work and personal records within their existing boundaries.

For a named feature or defect, also inspect the available shared record: relevant commits, PR discussions, issues, incident notes or error reports. Read only sources that bear on the topic. Unavailable sources are coverage limits. Check the actual files and refs before assigning current status. A past agent report is a lead, not proof that a change shipped.

Return a brief with the overall state, one line per workstream, recurring unresolved problems, and the single most useful next action. Distinguish planned, in progress, verified locally, open PR, merged and reverted. Attach evidence pointers to substantive claims. Say when live status could not be verified. Do not edit notes or resume implementation unless the request includes that work.
