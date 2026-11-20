# Notice

The namespaced skills under `trial/skills/` are adaptations by cdracars of Lauren
Tan's pstack workflows, informed by pmwoz's T3 port. Their exact source files and
hashes are recorded in `trial/sources.json`; bundled references carry the same
provenance and both licenses. `trial/runtime.md` is the fork's shared adapter.
The full plugin and pinned upstream snapshots remain available separately.

t3-pstack redistributes files from [cursor/plugins](https://github.com/cursor/plugins), with the changes listed in `drift.json`.

| Files | Source | License |
|---|---|---|
| `plugins/pstack/` except the files below | `pstack/` | MIT, Copyright (c) 2026 Lauren Tan. `plugins/pstack/LICENSE` |
| `plugins/pstack/skills/deslop`, `control-cli`, `control-ui` | `cursor-team-kit/skills/` | MIT, Copyright (c) 2026 Cursor. `plugins/pstack/LICENSE-cursor-team-kit` |
| `t3/contract/` | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | MIT, see that repository. Kept as a reference snapshot, not shipped in the plugin. |

The files this port adds (`tools/`, the T3 adapter, the hooks, and the manifests) are MIT licensed under `LICENSE`.
