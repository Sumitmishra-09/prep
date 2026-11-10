# Senior Java / BFSI interview preparation

Personal interview coaching for a Java, Spring Boot, and SQL developer with seven years of experience, currently a tech lead in BFSI. Target: roles paying at least INR 40 lakh annually; fixed pay versus total CTC remains to be clarified.

**Commitment: 8 weeks, 27 hours/week, approximately 216 hours.** Start with a diagnostic; experience and self-confidence are not scores. The plan changes with demonstrated gaps and actual interview dates.

## Start or resume

Open this repository in Claude Code or Codex and say:

> Continue my interview preparation. Read the instructor instructions and progress/state.json. Guide the lesson in chat, explain concepts I am missing, and help me reason through one question at a time.

Claude instructions: [CLAUDE.md](CLAUDE.md). Codex instructions: [AGENTS.md](AGENTS.md). Both use the same [coaching protocol](INSTRUCTOR.md).

## Your preparation map

| Resource | Purpose |
|---|---|
| [Eight-week curriculum](CURRICULUM.md) | Weekly hours, milestones, and mock interviews |
| [First-priority questions](questions/HOTLIST.md) | The first 25 questions to master |
| [Full question bank](questions/BANK.md) | Stable question IDs, scenarios, and follow-up probes; no solutions |
| [Diagnostic](sessions/DIAGNOSTIC.md) | Establish your baseline without a lecture |
| [Practice labs](practice/LABS.md) | Small experiments and a payment-service capstone |
| [Research and references](research/SOURCES.md) | Dated market evidence and primary technical references |
| [Visual teaching skills](research/SKILLS.md) | Portable tutoring and diagram skills; reviewed sources and usage |
| [Role strategy](career/STRATEGY.md) | Role selection, project stories, applications, and compensation |
| [Current state](progress/state.json) | Exact checkpoint for the next instructor |
| [Question tracker](progress/questions.csv) | Attempts, hint use, scores, and next review dates |
| [Git sync guide](SYNC.md) | Continue from another laptop |

## How lessons work

The instructor leads the entire lesson in chat: chooses the topic, explains missing concepts, supplies useful short readings or examples, assesses your reasoning, and corrects mistakes. You do not need to navigate the question bank or figure out the syllabus alone. The repository is the instructor's planning and memory system.

Lessons can include request timelines, object diagrams, small SQL result tables, payment state machines, and algorithm traces. The instructor explains the picture, asks for a prediction, helps test it, and changes one constraint. The bundled skills support this workflow across laptops; no additional learning platform is required. Say `show me visually` or `help me debug` whenever useful.

One question at a time. You explain a hypothesis, we test it, and the instructor adapts the support. Saying “I don't know” triggers a clear mini-lesson and an analogous example, followed by a smaller application question. After your answer, we examine failure cases and changed constraints, then you explain the result in interview form. Full worked answers to the active exercise require your explicit request; teaching concepts does not.

You can say `continue`, `teach me from basics`, `give me a short reading`, `hint`, `smaller example`, `let me code`, `challenge my answer`, `mock interview`, `review due questions`, or `pause and save`. These are conversational requests, not installed CLI commands.

Progress lives in files, not chat history. Each completed session records evidence and the exact next prompt, then commits and attempts to push to the configured GitHub remote. A failed push must be reported honestly. There is no background sync while the instructor is offline.

Research checked: **2026-11-10**. “Hotlist” means preparation priority, not a measured frequency ranking or guaranteed interview question. No curriculum can guarantee an offer or compensation.
