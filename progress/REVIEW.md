# Weekly review

Initial diagnostic is in progress: BFSI-01 and JAVA-01 completed as assisted learning; no question mastered yet. Current question: CON-01. Initial week: 1.

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

- JAVA-01 second response predicts the failed lookup correctly but confuses hash/bucket changes with self-equality. Instructor probe executed successfully on Java 17.0.9 and used to correct the mechanism; stable-key redesign remains pending.

- JAVA-01 third response proposes stable identity hashing. Conditional validity clarified against the existing value-based equals; a distinct-but-equal key lookup is the next probe. No new experiment or mastery recorded.

- JAVA-01 fourth response correctly predicts the distinct-equal-key lookup failure. Corrected different-hash versus different-bucket overgeneralization using stored-hash screening. Next: stable accountId value-key design; no new runtime experiment or independent pass.

- JAVA-01 clarification: taught binary masking and where hashCode/equals participate, at learner request. No new attempt or mastery recorded. Check equal-hash unequal-key lookup next, then resume the stable-key design.

- JAVA-01 fifth response correctly explains null for equal-hash unequal keys: both reference identity and equals fail. Positive supported application; stable-key design resumes. No independent pass or mastery.

- JAVA-01 sixth response reaches constructor-only ID initialization as the core fix. Instructor adds private-final enforcement. Final check: mutation of a field excluded from equals/hashCode. Keep this assisted; no independent mastery yet.

- JAVA-01 completed after seventh response: correct status-only mutation prediction; refine unchanged methods to unchanged relevant inputs. Overall 2/4, H3, learning; retrieval 2026-11-11. Recap consolidated. CON-01 starts with zero responses, H0 and no score; no counter experiment executed.

- CON-01 first response correctly predicts 1 or 2 at H0. Next: explain a concrete ordering ending at 1 (H1 focus on reads/writes). No misconception, overall score, independent pass, or executed experiment recorded.

- CON-01 second response correctly explains both threads reading 0 and writing 1. Lost-update timeline established with H1 focus; next scenario changes only the field to volatile. Volatile understanding remains unassessed; no experiment or independent pass.
