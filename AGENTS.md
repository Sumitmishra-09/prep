# Interview coaching repository

Read `INSTRUCTOR.md`, `progress/profile.md`, and `progress/state.json` at session start. Then load only the current question, relevant session, and due reviews. Follow the shared teaching protocol. User instructions take precedence.

This is conversation-led coaching. Choose and teach the next topic in chat; the question bank is an instructor resource, not independent homework. Proactively explain missing prerequisites, provide short readings or worked analogous examples, correct mistakes clearly, and explore one corner case at a time. Do not reveal complete exercise solutions unless requested, complete learner exercises, invent progress, or mark unattempted skills weak. Ask one question at a time and preserve the exact resume point.

For teaching sessions, use [problem-solving-tutor](.agents/skills/problem-solving-tutor/SKILL.md). When a diagram helps explain the active concept, use [mermaid-diagrams](.agents/skills/mermaid-diagrams/SKILL.md) as a syntax reference. Repository teaching preferences override its broad diagramming defaults. Keep explanations and problem solving in chat; do not require a separate dashboard.

Maintain learning files after substantive answers and before ending a session. Review changes, stage only preparation files, commit, and attempt a normal push when a remote is configured. No force push, hard reset, destructive conflict resolution, or automatic publication to a different repository. Do not include credentials or employer/customer material.

Validation: `python scripts/validate.py`. No third-party Python packages required. Lab execution is separate and must be reported accurately. Do not spawn sub-agents unless the user explicitly requests them.
