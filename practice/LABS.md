# Practice labs — requirements, no solutions

The learner writes the key code and queries. The instructor asks for predictions, helps isolate failures, and reviews evidence. Use synthetic data only. Create each lab in its own directory when starting it; do not prebuild the capstone or install an entire stack before the diagnostic.

## Lab 1 — Concurrent money updates

Related: BFSI-01, CON-01, SQL-07, ORM-03. Budget: 3–4 hours over weeks 1–3.

Reproduce competing withdrawal requests, first with a small Java state model, then with the chosen SQL engine. Write the business invariant before changing implementation. Capture a deterministic interleaving, distinguish final balance from business outcomes, and propose your own alternatives. Compare a same-process case with two independent service instances.

Evidence: learner code, a reproducible failing test, a concurrency timeline, proposed fixes with tradeoffs, and a changed scenario that still meets the invariant. No success claim based only on one lucky concurrent run.

## Lab 2 — Transaction boundaries and persistence

Related: SPR-03 through SPR-05, ORM-01 through ORM-04. Budget: 4 hours in week 2.

Build the smallest example that lets you predict behavior for different call paths, exception types, propagation settings, and flush/commit timing. Explain the transaction manager and proxy assumptions. Inspect actual database state, not just return values. Add an ORM list endpoint and measure query counts under different result sizes.

Evidence: predictions made before execution, integration tests against the selected database, observed queries, and an explanation of one surprising outcome. State the actual Java, Spring, ORM, and database versions.

## Lab 3 — SQL workbook

Related: SQL-01 through SQL-10. Budget: 6 hours spread across weeks 1–3.

Create synthetic tables for accounts, customers, transactions, and settlement records. Choose constraints and types yourself. Include accounts with no transactions; duplicate timestamps; multiple currencies; failed, pending, and successful records; NULL optional values; reversed items; and mismatched settlement entries.

Solve joins/anti-joins, ranking, running totals, latest-per-group, monthly aggregation, duplicate detection, and reconciliation. Explain normalization choices, keys/constraints, WHERE versus HAVING, UNION versus UNION ALL, CTEs, and window frames as they arise. Compare at least two query shapes and their execution plans on enough synthetic data to expose a difference. Do not assume an index is useful merely because it exists.

Evidence: schema, fixtures, learner queries, expected results for edge cases, plan observations, and dialect notes. Test modifying statements only in disposable local fixtures; execution plans that execute statements are not read-only.

## Lab 4 — Payment-service capstone

Related: DIST, MSG, SYS, LLD, BFSI. Budget: approximately 18 hours across weeks 2–7, within the curriculum's applied allocation. This is a small demonstration of reasoning, not a production banking platform.

Define API contracts for initiating a synthetic payment, reading its status, and processing a simulated provider callback. State money invariants, allowed transitions, ownership checks, and retry semantics before implementation. Start with one service and a database. Add messaging only after the local correctness model is clear.

Requirements to reason about:

- Two distinct payments compete for the same funds.
- The same request is submitted concurrently and after a timeout.
- A retry uses an old request identifier with different input.
- A provider accepts a payment but the response is lost.
- A callback is duplicated, delayed, reordered, or unauthenticated.
- The process crashes around persistence, publication, and event acknowledgement.
- An event is replayed after a bug fix.
- A partial refund competes with another refund.
- A daily settlement source disagrees with local state.
- An authenticated user requests another customer's data.

Deliver incrementally: API and schema decisions; executable tests; one failure timeline per scenario; a short architecture decision record comparing alternatives; observable operational signals; a recovery/reconciliation procedure; and a five-minute project walkthrough. Use a fake external provider and synthetic identifiers. Keep unfinished guarantees explicit.

## Lab 5 — Diagnose and roll out safely

Related: JVM-01 through JVM-07, OPS-01 through OPS-09. Budget: 4–5 hours in week 6.

Introduce a controllable slow dependency or inefficient query in the capstone. Predict which measurements distinguish CPU saturation, waiting, connection exhaustion, and allocation pressure. Use appropriate diagnostics and record what they show. Propose a backwards-compatible schema change and a rollout/rollback exercise.

Evidence: symptom timeline, hypotheses with discriminating measurements, mitigation choice, root-cause evidence, and a prevention test. “Restart fixed it” is not a diagnosis.

## Lab 6 — Timed machine coding

Related: LLD-03, LLD-04, LLD-10. Budget: three 90-minute attempts in weeks 5–8, including debrief time allocated elsewhere in those weeks.

Choose one of a rate limiter, notification dispatcher, or small transfer API. Agree on a bounded contract. Work without instructor code generation during the timed attempt. Reserve time to run tests and explain limitations. Repeat later with a changed constraint instead of memorizing the first implementation.

## Stack selection

Java 17 is available on the current laptop, so initial fundamentals need no upgrade. Confirm the production stack and target job descriptions before pinning the Spring/database lab versions. Virtual-thread experiments require a suitable newer JDK. Maven and Docker executables were discovered, but dependency availability and daemon state have not been tested. Once a lab starts, record reproducible run commands and versions in its README. No lab has been executed during curriculum setup.
