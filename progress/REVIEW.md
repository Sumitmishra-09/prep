# Weekly review

First guided technical assessment is in progress; no question mastered yet. Initial week: 1.

At the end of each week append: actual hours, questions independently solved, questions requiring hints, due retrievals, strongest evidence, two highest-priority gaps, mock results, and next week's reallocation. Preserve a 27-hour budget. Do not report question coverage as mastery.

## Week 1 starting point

- Progress: setup complete; initial diagnostic pending.
- Strengths: Java/Spring/SQL/BFSI experience reported, depth not yet assessed.
- Gaps: unknown.
- Next: BFSI-01, then the rest of the diagnostic over two study sessions.
- Coaching clarification: sessions are instructor-led in chat, including mini-lessons, readings, correction, and incremental corner cases. Start BFSI-01 with a single-request baseline. No technical answer or assessment yet.
- Added portable visual problem-solving skills and preserved the pending diagnostic. Tooling work is not learning evidence; no mastery or score changed.

## First technical evidence, 2026-11-10

- BFSI-01: learner recognized the funds check and concurrency risk, and named read locking / repeatable read as possible approaches.
- Repair targets: exact-balance boundary; precise lock semantics; distinction between read stability and transaction correctness.
- Support: prerequisite explanation and a shared-lock upgrade scenario. No score or independent pass yet.
- Next: reason through the lock-upgrade timeline; return for retrieval on 2026-11-11. Other areas remain unassessed.

- Second response revealed a specific gap: sequential waiting versus circular waiting during shared-to-exclusive lock upgrade. Instructor provides a wait trace; learner's revised acquisition approach is pending.

- Third response proposed synchronized mutual exclusion. A valid local direction under shared-monitor/transaction-scope conditions; multi-instance behavior remains to be assessed.

- Fourth response proposes database row locking and requests explanation. Teaching now covers acquiring the row write lock during the initial read, transaction scope, and the limits of deadlock avoidance. A rollback prediction is pending; no independent mastery credited.

- Fifth response correctly predicts rollback visibility (INR 1,000) and explains undo plus lock release without a further hint. Positive local evidence; overall concurrency mastery still unestablished. Next challenge: consistent lock ordering for two-account transfers.

- Learner requested post-question answer/detour summaries. Created a partial BFSI-01 revision note and added the recurring recap protocol. The two-row ordering question remains open.

- Sixth response correctly proposes consistent account-lock ordering. Qualified its scope and updated the question recap. Next: a short synthesis of the original withdrawal problem before closing this guided diagnostic question.

- Seventh response correctly names row locking by account ID in a brief synthesis. A focused second-withdrawal outcome probe will check the remaining connection to the business rule; omissions are not treated as proven misconceptions.

- BFSI-01 guided diagnostic completed: 2/4 assisted learning, H3 support, no independent pass/mastery. Learner correctly connects updated balance with rejection; statement resumption and exception/return rollback semantics corrected. Review scheduled 2026-11-11. Next active question: JAVA-01, unattempted.

- JAVA-01 first response correctly identifies hashCode as a diagnostic starting point. Key/hash/value terminology clarified; a concrete key-mutation prediction is pending. No score or mastery recorded. Partial recap saved.
