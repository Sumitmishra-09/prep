# Eight-week curriculum: 216 hours

27 hours each week, confirmed by the learner. Suggested cadence: three hours on each weekday and six hours on each weekend day. This is adjustable; protect breaks within long study blocks. Weeks are relative to the first study week, not assumed interview dates.

## Weekly allocation

Every row totals 27 hours. Coding/SQL, retrieval, and mocks are included, not extra homework.

| Week | Main study and experiments | Coding + SQL | Applied lab/design | Retrieval + assessment | Career evidence | Total |
|---|---:|---:|---:|---:|---:|---:|
| 1: Diagnostic, Java, concurrency | 8 | 7 | 4 | 6 | 2 | 27 |
| 2: Spring, transactions, ORM | 8 | 6 | 6 | 5 | 2 | 27 |
| 3: SQL, isolation, performance | 7 | 7 | 6 | 5 | 2 | 27 |
| 4: Distributed systems, Kafka | 8 | 5 | 7 | 5 | 2 | 27 |
| 5: HLD, LLD, BFSI correctness | 7 | 5 | 8 | 5 | 2 | 27 |
| 6: JVM, production, security, cloud | 7 | 5 | 7 | 6 | 2 | 27 |
| 7: Integrated practice, gap repair | 4 | 6 | 6 | 8 | 3 | 27 |
| 8: Employer-specific preparation and mocks | 3 | 5 | 4 | 12 | 3 | 27 |

Main-study hours are active problem solving and targeted reading after an attempt, not uninterrupted video watching. The 155-question bank is coverage, not a requirement to rush through 155 answers. A question may consume multiple sessions. P0 questions and demonstrated gaps take precedence.

## Weekly outcomes

### Week 1 — Establish a truthful baseline

Spread `sessions/DIAGNOSTIC.md` across two sessions (about three hours total including debrief). Java: object contracts, collections, generics, immutability, exceptions, streams; concurrency: atomicity, visibility, locks, executors. Begin array/hash/sliding-window coding and SQL joins/aggregation.

Deliver: diagnostic evidence; two learner-authored Java experiments; one project ownership story; initial role shortlist. Exit check: explain a shared-state failure with a timeline, and implement one unseen easy/medium coding problem with tests. Failure changes week 2's allocation; it is not a reason to fake a pass.

### Week 2 — Explain what Spring actually does

Dependency injection, lifecycle, auto-configuration, proxies, transaction boundaries/propagation/rollback, MVC request flow, validation, async context, configuration, JPA persistence context, fetch plans, optimistic locking. Begin payment capstone API and transaction design without introducing messaging yet. Coding: linked structures, stacks, binary search; SQL: NULL and joins.

Deliver: reproduce and explain a transaction-boundary bug; compare ORM query counts; code a small testable business rule. Exit check: a 45-minute Java/Spring mock and a fresh concurrency follow-up.

### Week 3 — Make SQL and money updates defensible

Window functions, rankings/ties, running totals, CTEs, EXISTS/NULL, composite indexes, execution plans, statistics, pagination, MVCC, isolation, locks, deadlocks, constraints, migrations. Separate PostgreSQL exercise behavior from Oracle/MySQL production behavior; verify each dialect before making claims. Coding: trees/heaps/intervals.

Deliver: a query workbook with self-generated edge-case fixtures; before/after plan evidence; a two-session concurrent update experiment. Exit check: solve an unseen SQL task and show why a proposed money update survives competing transactions.

### Week 4 — Survive retries and partial failure

Deadlines, bounded retries, idempotency, service boundaries, sagas, outbox/CDC, cache consistency, Kafka ordering/partition keys, offsets, rebalance, delivery guarantees, schema changes, poison records, replay. Coding: BFS/DFS and topological sort.

Deliver: capstone failure timeline and messaging extension; tests for duplicate input and consumer restart. Exit check: explain every crash window between database update, event publication, processing, and acknowledgement. Do not claim end-to-end exactly-once without identifying its boundary.

### Week 5 — Design as a senior engineer

Requirements and estimates, APIs/data models, consistency, scaling, hot keys, partitioning, overload, observability, recovery; LLD interfaces, invariants, state transitions, testability and patterns. Deep scenarios: payments, ledger, reconciliation, refunds, notifications, rate limiting. Coding: backtracking and basic dynamic programming.

Deliver: two 45-minute system designs with explicit tradeoffs; one 90-minute machine-coding exercise; capstone money invariants and reconciliation cases. Exit check: adapt the design to a changed failure or workload constraint without redesigning everything by name-dropping technologies.

### Week 6 — Operate and secure what you build

JVM memory/GC/JFR/thread dumps, CPU/latency/connection-pool incidents, HTTP/TLS/DNS, container resources, Kubernetes health and rollout behavior, AWS building blocks/IAM, CI/CD, integration/contract/load testing, OAuth2/OIDC/JWT, authorization and tenant isolation. Modernization awareness: Java 17/21/25 and Boot 3/4 differences tied to an actual target version; optional reactive/native-image depth only when the role needs it.

Deliver: incident investigation notes with measurements; capstone authorization tests and runbook; a backwards-compatible schema rollout plan. Exit check: a timed incident diagnosis and an explanation of a safe release/rollback path.

### Week 7 — Integrate and repair

Run a coding round, Java/Spring/SQL depth round, HLD round, LLD exercise, and behavioral round across the week. Debrief each, repair the two highest-impact gaps, then test a changed variant. Finish a demonstrable capstone slice; don't expand its feature count.

Deliver: recorded rubric scores, a five-minute project walkthrough, six truthful leadership stories, a reviewed resume draft, and a recruiter-verified shortlist. Start or continue applications with the learner's explicit authorization; the instructor does not apply or send messages independently.

### Week 8 — Rehearse the actual hiring loop

Use real job descriptions and recruiter-confirmed interview formats. Complete two different mock loops, each including coding, backend depth, design, and leadership; allow debrief/recovery between rounds. Review due items and rehearse compensation questions. Keep the final day before a real interview light.

Deliver: final gap list, two-page personal recall sheet written by the learner, interview-specific question set, and compensation comparison template. Prioritize sleep and clear explanations over a new framework.

## Session rhythm

A typical three-hour block: 20 minutes due retrieval, 60 minutes guided technical reasoning, 60 minutes coding/SQL/lab, 25 minutes edge-case challenge and teach-back, 15 minutes logging and planning. Adapt these buckets to the weekly allocation. Weekend blocks include breaks and a mock or larger lab.

## Readiness gates

These are our coaching criteria, not employer cutoffs:

- Coding: two unseen medium-level problems on separate days, each within about 40 minutes with correct code, complexity, and tests.
- Java/Spring/SQL: two fresh mixed rounds scoring >=3/4, with transaction/concurrency claims supported by reasoning or experiments.
- Design: two unseen 45-minute designs scoring >=3/4, covering requirements, failure behavior, data correctness, scale, and tradeoffs.
- LLD: a small runnable design with meaningful tests within 90 minutes; no need for an elaborate framework.
- Leadership: six truthful examples demonstrating personal decisions, consequences, and learning; distinguish team impact from individual contribution.
- Critical payment correctness, authorization, and recovery misconceptions must be repaired before treating the overall average as readiness.

If a gate fails, spend the next available elective block repairing it. Do not discard coding/SQL maintenance. DSA-heavy targets receive more coding time; bank backend-depth targets receive more transaction/SQL/project time after their actual interview format is confirmed.
