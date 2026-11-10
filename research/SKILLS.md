# Skills for visual, problem-solving lessons

Reviewed and added on 2026-11-10. Skills improve teaching consistency and the available presentation methods; installing them does not establish faster learning or interview readiness. Check improvement through fresh problems, fewer hints, accurate reasoning, and later recall.

## Included

| Skill | Source | Purpose |
|---|---|---|
| [problem-solving-tutor](../.agents/skills/problem-solving-tutor/SKILL.md) | Original repository-specific skill | Explain missing concepts, use visual models and experiments, correct errors, and test transfer to corner cases |
| [mermaid-diagrams](../.agents/skills/mermaid-diagrams/SKILL.md) | [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit/tree/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/mermaid-diagrams) | Syntax and examples for sequence, state, class, ER, and architecture diagrams |

The Mermaid skill was installed with the skill-installer helper at upstream commit `3027f20f3181758385a1bb8c022d4041dfb4de84`. Its Markdown files are preserved as installed; the upstream [MIT license](../.agents/skills/mermaid-diagrams/LICENSE) is included. The installed payload consists of documentation and examples, not an executable plugin. Optional installation/export commands in its references were not executed.

Repository teaching instructions take precedence over upstream broad defaults such as always creating diagrams for certain tasks. Treat its examples as diagram syntax, not endorsed application architecture or security guidance. Rendering depends on the chat/editor; provide a plain-text trace or table if needed. No public diagram hosting or paid service is required for this setup.

## Considered but not installed

- [OpenAI curated skills](https://github.com/openai/skills/tree/main/skills/.curated): inspected the live catalog. Notebook, PDF, and browser tooling may help particular tasks, but adding those does not supply the requested adaptive tutoring. Playwright is already available in this environment for future browser-based exercises.
- [AI Socratic Tutor](https://github.com/bstellato/ai-teaching-skills/blob/6d3f85726e7b0fedacc8a078e174161293777044/ai-socratic-tutor/SKILL.md): inspected its instructions. It constrains each reply to one form and avoids direct correctness endorsements. Those choices conflict with this learner's request for active explanation and clear correction, so it was not installed.
- [Visual Explainer](https://github.com/nicobailon/visual-explainer): its repository describes rich HTML diagrams and slide decks. This remains an option for a specific interactive or presentation need; the full package was not installed or comprehensively audited. Chat diagrams provide a smaller starting point for the current request.

## Portability and activation

Canonical skills live in `.agents/skills/`. Small Claude entry points in `.claude/skills/` refer to those same files, so there is one maintained source. `AGENTS.md` and `CLAUDE.md` explicitly route the instructor to these skills; manual reading of those instructions remains a fallback if a client does not discover project skills automatically.

Clone or pull this repo on the other laptop. No separate global skill download is needed for these two skills. The installer reports the installed skill as available on the next turn; use the explicit repository entry points if a running client has not refreshed discovery.

## Lesson behavior

The instructor chooses when to teach, draw, demonstrate, ask, and test. A typical lesson moves through a short explanation or baseline attempt, a visible model, one prediction, an experiment or trace, correction, and a changed scenario. The learner can say "show me visually", "explain from basics", or "help me debug" without choosing a skill or editing files.

No new technical answers or mastery were inferred from this tooling setup. BFSI-01 remains pending.

## Validation performed

Repository state, question tracking, and local Markdown links passed validation. All four skill entry points passed the skill-creator structural validator. The ten bundled upstream files, including LICENSE, matched Git blob hashes at the pinned commit. These checks establish packaging and provenance; no interactive lesson, renderer, or learning outcome has been tested yet.

Upstream Markdown contains trailing whitespace. It is retained to preserve the verified source exactly; whitespace checks for repository-authored changes exclude that bundled directory.
