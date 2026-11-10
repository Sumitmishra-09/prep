# BFSI-01: withdrawals, locks, and transaction boundaries

Status: **guided question completed; independent mastery not established**. Updated 2026-11-10. Guided-learning score: **2/4**, highest support H3. Scenario: INR 1,000 balance, positive INR 700 withdrawals, no overdraft, fees, or minimum-balance requirement. Database-specific examples use PostgreSQL 18 at READ COMMITTED unless explicitly stated otherwise. The learner's actual database is not yet confirmed.

## Correct answers established so far

| Question or branch | Correct answer and reasoning |
|---|---|
| What funds check permits a withdrawal? | Under the stated assumptions, `balance >= withdrawalAmount`. Strict `>` incorrectly rejects withdrawing the exact available balance. Input validation and money representation have not yet been covered. |
| Can two retained shared row locks simply upgrade and write sequentially? | In the specified upgrade scenario, each blocks the other's exclusive-lock request. This creates a circular wait. The system needs an intervention, such as aborting a transaction, to break it. |
| Can a Java synchronized block help? | Yes, for participating operations using the same monitor within one JVM, with protection covering the relevant transaction through commit. Separate JVMs have separate monitors, so this alone does not coordinate all application instances. |
| How can a database lock avoid that particular upgrade cycle? | Use a locking read such as `SELECT ... FOR UPDATE` before making the funds decision. Keep the locking read, check, update, and commit in one transaction. In the single-row example, one transaction can proceed while the other waits. |
| What does the waiting locking read receive after a commit? | In our PostgreSQL READ COMMITTED example, it can return the updated row after the first transaction ends. This is a claim about the locking read, not every ordinary read or isolation level. |
| What if the first transaction rolls back? | With no other writers, the waiting request receives INR 1,000. The uncommitted change to INR 300 was rolled back, and the row lock was released. |
| What happens to the second INR 700 withdrawal after the first commits? | Its waiting locking read completes with INR 300, so the funds check fails and it must not debit. A new application-issued SELECT is not required for this waiting statement to complete. |
| Does rejecting a withdrawal automatically roll back the transaction? | No. A business rejection and transaction rollback are different outcomes. If this transaction has only read and locked the row, it may return a rejection and commit without a debit. A normal return does not itself request rollback; exception and explicit rollback behavior depend on the transaction framework/configuration. |
| How do opposite-direction transfers avoid the illustrated two-row deadlock? | Acquire the required account-row write locks in one consistent order, such as ascending account ID, in every participating transaction. Descending also works if universally chosen. Lock order is independent of which account is debited. This prevents the shown cycle, not every possible deadlock involving other resources or upgrades. |

The PostgreSQL-specific locking and deadlock behavior is documented in [row-level locks](https://www.postgresql.org/docs/18/explicit-locking.html#LOCKING-ROWS) and [deadlocks](https://www.postgresql.org/docs/18/explicit-locking.html#LOCKING-DEADLOCKS). The value returned after a competing update depends on [READ COMMITTED behavior](https://www.postgresql.org/docs/18/transaction-iso.html#XACT-READ-COMMITTED).

## What you got right

- Identified a funds check before changing the balance.
- Recognized concurrent requests as a correctness concern.
- Correctly associated repeatable read with preventing nonrepeatable reads.
- Suggested mutual exclusion and then database row locking as possible coordination mechanisms.
- Correctly explained the rollback outcome: INR 1,000 is visible after undo and lock release. This follow-up needed no additional hint.
- Proposed ordering account-lock acquisition ascending or descending to prevent the two-row circular wait. The instructor clarified that every participant must use the same chosen order and qualified the scope of the guarantee.
- In the synthesis, identified row locking by account ID and correctly concluded that the second request receives the updated balance and fails its funds check.

## Corrections and qualifications

- Include the equality boundary when the account may reach zero.
- Shared locks do not guarantee that one competing upgrader can finish. Inspect what each transaction holds and waits for.
- `synchronized` depends on monitor identity and scope; it is not a database-wide lock.
- A stable read view does not by itself establish the complete withdrawal guarantee. In particular, PostgreSQL repeatable read may abort a conflicting same-row update and require transaction retry; do not claim it universally permits both stale writes. See [repeatable read](https://www.postgresql.org/docs/18/transaction-iso.html#XACT-REPEATABLE-READ).
- Consistent account ordering prevents the illustrated account-lock cycle. It does not prove an entire application deadlock-free if other resources or lock upgrades participate. All relevant code paths must follow the same convention and acquire the needed lock mode from the outset.
- The blocked locking statement can finish after the conflicting transaction ends; this does not require issuing another SELECT from the application.
- Exiting a SQL block or normally returning from a Java method is not equivalent to rollback. With standard Spring declarative defaults, an unhandled RuntimeException/Error escaping the transactional boundary triggers rollback; checked exceptions need matching configuration. Normal return ordinarily allows commit unless rollback-only or another transaction condition changes the result. See [Spring rollback rules](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/rolling-back.html).

## Detours and extra concepts explored

- Ordinary waiting versus circular waiting, and why lock upgrades can deadlock.
- The distinction between Java object monitors and database row locks.
- Coordination across separate Spring Boot instances.
- Why transaction completion matters to lock lifetime.
- How rollback affects the next waiting request's observed balance.
- Why acquiring a write lock upfront for one row is not a guarantee against every multi-resource deadlock.
- A consistent lock-acquisition order breaks the illustrated two-account circular wait; lock order and money-transfer direction are separate decisions.
- Business rejection versus database rollback; a rejected operation can finish a transaction without making a debit.
- Default Spring rollback rules depend on the exception type and whether it escapes the transactional boundary. Catching or returning does not automatically imply rollback.

## Transfer follow-up recap

Choose ascending IDs for this example. T1 acquires 101. T2 also attempts 101 and waits without first holding 202. T1 can acquire 202, perform its transfer, and commit; T2 can then acquire both locks in the same order. Either transfer direction uses the same acquisition sequence. This is why no cycle forms in the specified two-row example. The consistent-order recommendation is supported by the [PostgreSQL deadlock discussion](https://www.postgresql.org/docs/18/explicit-locking.html#LOCKING-DEADLOCKS).

Interview phrasing: I acquire the required account-row locks in a consistent order across all transfer paths, independent of debit direction. This prevents opposite-order account-lock cycles. I still account for other resources and transaction failures instead of claiming that row ordering eliminates every database deadlock.

## Interview-ready answer for the covered single-account approach

For a positive withdrawal, I would read the account with `SELECT FOR UPDATE` in a database transaction and check that the returned balance is at least the requested amount. I would debit and commit in that same transaction when allowed. In our PostgreSQL READ COMMITTED example, the other instance's locking read waits; after the first INR 700 withdrawal commits, it receives INR 300 and rejects its own INR 700 withdrawal without debiting. The transaction must finish to release its locks. For multi-account operations, all participants acquire the needed locks in a consistent order. I would still handle transaction failure and avoid claiming that this removes every possible deadlock.

This is a scoped approach taught during the lesson, not a complete production withdrawal design. Retries, idempotency, external effects, and exact Spring/JPA integration remain unexplored. Only a brief introduction to Spring rollback defaults has been given.

## Assessment and remaining review

This guided question is complete for now. The learner correctly reasoned about rollback visibility, consistent ordering, and the second request's failed funds check. The instructor taught the locking mechanism and corrected equality, upgrade-deadlock, and transaction-completion details. This supports a 2/4 assisted-learning score, not an independent pass. The original unsafe no-lock interleaving was not independently reconstructed; include it in later retrieval.

Review transaction completion and exception rules in the Spring module. Re-test the overall withdrawal model on a fresh scenario before increasing the score or claiming mastery. Next diagnostic topic: JAVA-01, a HashMap lookup that stops finding an inserted key.

## Retrieval and evidence

Next planned review: 2026-11-11. Reconstruct the single-row waiting scenario without reading this note, then predict what changes if the first transaction commits versus rolls back. The instructor should select a fresh variation when reviewing.

No Java or SQL experiment has been executed. Several mechanisms were taught with H3 support; recognizing this summary is not independent mastery. The chronological evidence is in [the lesson log](../sessions/2026-11-10-lesson-01.md).
