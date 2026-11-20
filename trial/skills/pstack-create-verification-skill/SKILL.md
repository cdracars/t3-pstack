---
name: pstack-create-verification-skill
description: Build and run a project-local verification skill that launches an app, exercises a real user journey, records evidence and cleans up its own state.
license: MIT
---

# Create an app verification skill

Read [the runtime adapter](references/runtime.md) before choosing drivers and tool calls. Read the installed skill-creator or writing-for-agents guidance before authoring the new skill.

Inspect the repo for its primary user interface, startup command, dependencies, seed data, authentication, readiness signal, existing harness and isolation options. Prefer the current documented path. Ask only for information or access that cannot be discovered. A broken startup is a concrete blocker or a separately authorized repair, not a reason to invent a procedure.

Create a verify-app skill in the project's established skill directory. Determine the directory from the target host and repo conventions; do not assume a Cursor path. Give it valid name and description frontmatter and these operational parts:

- Launch and teardown with exact local commands, isolated data and owned process identity.
- Doctor checks for the expected build, instance, usable seed state and required access.
- Drive instructions with actual commands or stable selectors from this app.
- Evidence paths for the action, resulting state and observable side effects.
- Cleanup that removes only owned processes and scratch state while preserving proof.

Start a feature map covering the top three to five user-facing features. Each entry explains the user's goal, entry path, prerequisites, drive steps and observable success. Use existing deterministic checks where they cover a journey. An unmet prerequisite remains visible; do not weaken the check until it passes.

Follow the generated instructions end to end for one feature. Capture the action and result, verify side effects, run cleanup and confirm that the evidence remains. A mock or stand-in must name what it leaves unverified. If the real journey cannot run, label the skill a draft and give the exact blocker. Hand back the skill path, command, proven journey and coverage limits. Suggest pstack-maintain-verification-skill after the first working map exists, without scheduling it.
