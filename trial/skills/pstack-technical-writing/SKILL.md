---
name: pstack-technical-writing
description: Write or review technical documentation with a clear purpose, exact procedures and reader-appropriate explanations, including tutorials, reference and PR descriptions.
license: MIT
---

# Technical writing

Read [the runtime adapter](references/runtime.md). Follow the project's product, voice and documentation conventions. Apply the installed unslop skill when available.

Choose the document's purpose before drafting. A tutorial teaches through a working result. A how-to solves a concrete task. Reference describes facts for lookup. Explanation develops the reasons and tradeoffs. Split and link material when these purposes compete. A tutorial does not replace reference coverage.

For procedures, name prerequisites and conditions before the affected step. Give one instruction per sentence and show the expected visible result. Use the actual UI label, command, file or flag. Verify commands against the repo or current primary documentation. Mark unrun steps rather than implying they were tested.

Use plain words and active sentences with a clear actor. Define necessary domain terms once and reuse the same names. Split sentences that carry unrelated thoughts. Keep exact technical identifiers even when a simpler synonym sounds smoother. Remove filler, invented jargon, praise and generic conclusions. Preserve the human author's intent and voice.

Keep reference complete and dry. Keep explanations bounded and cite the record behind design claims. Label an inference when the source does not state the reason. Date claims about changing behavior or bind them to a version when that matters.

A PR description explains the concrete problem, resulting behavior, relevant verification and material limits. Link long logs instead of pasting them. Do not mix internal implementation notes into product instructions unless the reader needs them to act.

Before delivery, check links, identifiers, instructions and claims of coverage. Report substantive edits and verification succinctly.
