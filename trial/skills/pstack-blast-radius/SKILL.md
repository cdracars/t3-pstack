---
name: pstack-blast-radius
description: Review what a change can break beyond its diff, following runtime and data boundaries and testing the key fact its safety depends on.
license: MIT
---

# Check the blast radius

Read [the runtime adapter](references/runtime.md). Pin the change's base and head or working-tree scope. This is a review unless the user also requested fixes.

Read changed symbols, callers, producers and consumers. Follow effects a symbol search misses: serialized data, database contracts, pinned library behavior, feature flags, lifecycle ordering, another service or language, and cached state. Trace the actual dependency version and local patches when their semantics matter.

Find the one or two factual assumptions that clear the important risks. Try to disprove them by walking the failure path and running the smallest check against real code. Prefer existing tests or a disposable script at the actual public boundary. A toy reimplementation of the function is not proof of its behavior.

For each conclusion, identify its evidence level: reasoning alone, cited source, traced failure path, executed real-code check, or reproduced app behavior. Runtime proof is preferred where cheap and in scope. If permissions, setup or tooling prevent it, mark the assumption unproven instead of escalating the workflow automatically.

Return what changed, the critical safety fact and its evidence, confirmed risks, checked-and-cleared risks, and the cheapest remaining pre-merge check. Each risk names a concrete mechanism and source location. Avoid speculative caller lists. Add a review panel only when explicitly requested or allowed and its likely value justifies it.
