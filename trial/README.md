# Focused pstack trial

Nine adapted workflows for T3, Codex and Claude on Windows. The full pstack plugin
remains in `plugins/pstack/`; this trial installs only the selected standalone
skills, with no hooks, schedules or model-role settings. Skill discovery follows
the host's normal behavior. Names have a `pstack-` prefix to keep Matt's skills
and the existing `unslop` installation distinct.

| Skill | First experiment |
| --- | --- |
| `pstack-recall` | Recall the current state of one project from its notes and recent chats. |
| `pstack-create-verification-skill` | Prove one real CLI or app journey and leave reusable instructions. |
| `pstack-maintain-verification-skill` | Audit an existing verification skill against source and runtime. |
| `pstack-technical-writing` | Review a guide for tutorial, how-to and reference confusion. |
| `pstack-show-me-your-work` | Keep an evidence-linked decision log during a longer task. |
| `pstack-ketchup` | Give a short catch-up after an agent has worked for a while. |
| `pstack-correct` | Prevent a mistake that has occurred at least twice. |
| `pstack-blast-radius` | Review downstream effects of a specific change. |
| `pstack-automate-me` | Draft a small personal convention skill from scoped evidence. |

In Codex, select a skill with `$pstack-recall` or its name in the skill picker.
In Claude, use `/pstack-recall`. Start a fresh session if a host has cached its
catalog. For example:

```text
Use pstack-recall to catch me up on FT EMS work from the last seven days.
Verify current files and refs. Return the next concrete action. Read-only.
```

## Package and install

`trial/runtime.md` is the maintained adapter. The source skill bodies live under
`trial/skills/`. The build copies the shared adapter, licenses and provenance
into each package so individual installations are self-contained.

```powershell
python tools/trial.py build
python tools/trial.py check
python -m unittest discover -s tools -p test_trial.py -v
bun test tools --timeout 180000
```

Install these nine paths from this fork at a reviewed commit with the host's
skill installer. Target `~/.codex/skills` for Codex and `~/.claude/skills` for
Claude. Existing destinations must be preserved and reviewed before an update.
Do not run the full plugin installer merely to install this subset.

## Adaptation choices

Read [runtime.md](runtime.md) for current tool-routing rules. The trial follows
the active host instead of assuming Cursor tools, Unix paths, the author's
machine, model substitutions or mandatory review panels. It narrows implicit
publishing and always-on orchestration. It preserves the substantive goals of
the selected workflows and the distinction between source review and runtime
proof. Upstream and port source hashes live in [sources.json](sources.json).

The tests validate packaging and the decision-log helper. Trial use is still
needed to evaluate agent decisions. No claim is made that every workflow has
been behaviorally exercised on a live project.

Windows fixture copies can exceed Bun's five-second default test timeout. Use
the timeout above for the full tool suite. The unchanged full plugin's POSIX
hook tests are skipped when `sh` is absent; those hooks are not in this trial.
