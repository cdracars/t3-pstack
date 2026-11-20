---
name: pstack-show-me-your-work
description: Keep an evidence-linked decision trail during long or unattended work so another person can review choices, results and unresolved limits.
license: MIT
---

# Record a decision trail

Read [the runtime adapter](references/runtime.md). Use the project's existing decision log if it already serves this purpose. Otherwise keep a task-local decisions.tsv outside disposable worktrees; commit it only when the task's delivery needs it.

Use one row per consequential decision or checkpoint. Columns are ts, phase, decision, why, evidence and result. Store an ISO timestamp, a short phase, the choice, the reason, evidence pointers and the observed outcome. Use the log helper at scripts/log.py:

```text
python <this-skill-directory>/scripts/log.py <log-path> <phase> <decision> <why> <evidence> <result>
```

The helper writes one TSV row, rejects a mismatched existing header, removes embedded tabs/newlines and escapes spreadsheet formula prefixes. Quote arguments for the actual shell. Keep credentials and private payloads out of cells.

Log a fork chosen, verified unit, pivot, revert, blocker or changed assumption. Skip routine tool calls. Start each new agent run with a start row naming that run and the earlier rows it is building on. Read the latest rows before appending when another run could have written since. Use an existing single writer or isolated per-worker logs; a TSV append is not a concurrency-control mechanism.

Append corrections as new rows that name the superseded entry. Preserve the original evidence and distinguish verified, unverified and inconclusive results. Before handback, compare this run's rows with the actual transcript and artifacts. Confirm each pointer resolves and supports the claim. Record missing consequential decisions and corrections honestly.

Use an independent reviewer when requested or justified and authorized by the host; report whether that review ran. Do not claim cross-model review if it was unavailable. Return the log path and the few decisions or limits that need attention. A readable summary complements the trail; it does not replace it.
