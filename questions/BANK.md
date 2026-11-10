# Question bank — 155 original practice prompts

Research date: 2026-11-10. These are instructor-authored scenarios, not a claim that employers asked these exact questions. Evidence tags identify why a topic is included; candidate reports are unverified anecdotes. See [source definitions](../research/SOURCES.md). Follow-up columns are prompts for later exploration, not an answer key. The instructor should reveal them only after the initial attempt.

Priority: **P0** core readiness; **P1** next depth; **P2** role-dependent. All start unassessed. Use a named Java/Spring/database version when behavior depends on it. The [hotlist](HOTLIST.md) selects the first 25; work on diagnostic gaps before trying to finish every row.

## Java fundamentals — JAVA

Evidence: R3 candidate topic report; T1 official language/API reference. Original extensions for senior depth.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| JAVA-01 | P0 | A HashMap key was inserted but can no longer be found. How would you investigate? | What if a field used for equality changes? |
| JAVA-02 | P0 | How would you reason about HashMap performance under collisions and growth? | Which claims depend on the JDK implementation? |
| JAVA-03 | P0 | Design a Money value object for two supported currencies. What contracts matter? | Compare numerically equal values with different decimal scales. |
| JAVA-04 | P0 | A stream pipeline returns different results when parallelized. How do you locate the cause? | What if the accumulator mutates shared state? |
| JAVA-05 | P1 | Design an API that accepts related account types using generics. | Where would wildcards help, and what does erasure prevent? |
| JAVA-06 | P0 | How would you design exceptions across controller, service, and integration layers? | Preserve a root cause without leaking internal details. |
| JAVA-07 | P1 | How do you choose List, Set, Map, or a sorted collection for reconciliation? | What if ordering and uniqueness use different rules? |
| JAVA-08 | P1 | When would a record be suitable for a request or domain object? | Is a record containing a mutable list immutable? |
| JAVA-09 | P1 | How would you model payment outcomes with modern Java language features? | How do new states affect old consumers and exhaustive handling? |
| JAVA-10 | P1 | An API has Optional values, null fields, and resources that need closing. How would you simplify its contracts? | What happens if both processing and close fail? |

## Concurrency — CON

Evidence: R3 reported executors/thread questions; R1 production requirements; T1/T2 version references.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| CON-01 | P0 | Two threads increment one shared counter. Which outcomes would you predict? | How would you force an interleaving without relying on sleep? |
| CON-02 | P0 | A worker never observes a stop flag changing. How would you reason about it? | Does visibility also make a multi-step update atomic? |
| CON-03 | P0 | Is a get-check-put sequence safe on ConcurrentHashMap? | What if initialization calls a slow external service? |
| CON-04 | P0 | Choose an executor for concurrent downstream calls with bounded resources. | What happens when producers outrun consumers? |
| CON-05 | P0 | Combine three CompletableFuture calls with a deadline and one optional result. | What really stops when the combined result times out? |
| CON-06 | P0 | Two transfers lock accounts in opposite directions and stop progressing. How do you diagnose it? | Distinguish deadlock, starvation, and livelock. |
| CON-07 | P1 | Design a producer-consumer queue with shutdown behavior. | What happens to blocked threads and unfinished work? |
| CON-08 | P0 | A service moves to virtual threads. What workload assumptions would you test? | Compare Java 21 with later JDK behavior; what remains scarce? |
| CON-09 | P1 | Request identifiers disappear or leak across thread-pool tasks. What would you inspect? | How do async boundaries change context lifetime? |
| CON-10 | P1 | Choose between synchronized, explicit locks, atomics, and immutable state for a workload. | How would contention, fairness, and compound invariants change your choice? |

## JVM and performance — JVM

Evidence: R1 troubleshooting expectations; T1 diagnostic references. All scenarios are instructor extensions.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| JVM-01 | P0 | A JVM process uses much more memory than its configured heap. How do you investigate? | What if the container is killed without a Java exception? |
| JVM-02 | P0 | Memory use rises throughout the day. How do you distinguish a leak from a legitimate cache? | Which objects keep the retained data reachable? |
| JVM-03 | P0 | API tail latency rises during collection activity. What evidence would you gather? | When would changing collector settings address the wrong cause? |
| JVM-04 | P0 | CPU remains high with little throughput. How would you isolate the hot path? | How would lock contention and busy spinning differ? |
| JVM-05 | P1 | Design an experiment comparing two Java implementations. | How could warmup, dead-code elimination, or allocation mislead you? |
| JVM-06 | P1 | A class initialization fails once, then later requests fail differently. How do you debug it? | How can class loaders or dependency conflicts enter the story? |
| JVM-07 | P1 | Choose diagnostics for blocked requests: thread dumps, JFR, heap dump, or metrics. | What does each artifact fail to prove? |
| JVM-08 | P1 | Why might increasing heap size improve one metric while harming another? | Consider latency, throughput, and container headroom. |
| JVM-09 | P2 | Would native compilation help a long-running payment service? | Compare startup, steady-state behavior, build constraints, and diagnostics. |
| JVM-10 | P1 | A warm service is fast but each deployment causes a latency spike. What hypotheses would you test? | How do warmup and readiness interact? |

## Spring and Spring Boot — SPR

Evidence: R1/R2 requirements, R3/R4 reported themes; T3/T4 official references.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| SPR-01 | P0 | Explain how a Spring Boot application becomes ready to serve requests. | Where would a bean ambiguity or circular dependency surface? |
| SPR-02 | P0 | A starter unexpectedly changes application behavior. How do you trace why? | What makes an auto-configuration apply or back off? |
| SPR-03 | P0 | A transactional method is called through the same object. What determines the behavior? | Vary the call path, visibility, and proxy configuration. |
| SPR-04 | P0 | A method throws an exception but its database work remains. How would you investigate? | Compare checked exceptions, caught exceptions, and configured rollback rules. |
| SPR-05 | P0 | An inner operation fails while an outer transaction continues. What outcomes are possible? | Vary propagation, savepoints, and connection-pool capacity. |
| SPR-06 | P0 | Walk through an HTTP request from arrival to a validated response. | Where should malformed input and domain failure be handled? |
| SPR-07 | P0 | A singleton service holds request-specific mutable data. What could go wrong? | How would a two-request test expose it? |
| SPR-08 | P1 | Async work started inside a transaction sees surprising data. How do you reason about timing? | What state crosses the thread boundary? |
| SPR-09 | P1 | How would you test controller, business, persistence, and integration behavior efficiently? | Which defect would a fully mocked test miss? |
| SPR-10 | P1 | Plan a Boot 3-to-4 upgrade with a Java version change. | How do dependency compatibility, configuration, rollout, and rollback affect the plan? |

## ORM and persistence — ORM

Evidence: R3 ORM/JDBC report; original practice extensions. Verify details in the deployed provider documentation.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| ORM-01 | P0 | Explain what happens to an entity as it is loaded, changed, flushed, and committed. | Does flush establish durability? |
| ORM-02 | P0 | A list endpoint performs more queries as its output grows. How do you investigate? | How might pagination complicate a proposed fetch strategy? |
| ORM-03 | P0 | Two requests edit the same entity and one change disappears. How would you reproduce it? | Compare a version conflict with a business-rule conflict. |
| ORM-04 | P0 | Lazy data access works locally but fails after a service returns. What would you inspect? | What other problems could leaving a session open introduce? |
| ORM-05 | P1 | When would you use a projection, entity, native SQL, or JDBC? | How would batch size and memory change your answer? |
| ORM-06 | P1 | A bulk update runs, but already-loaded entities show old data. How do you reason about this? | What should a subsequent read in the same context mean? |
| ORM-07 | P1 | Model account ownership and cascading persistence operations. | How could deletion or an orphan rule remove too much? |
| ORM-08 | P1 | How would generated IDs affect equality and hash collections? | Compare new, managed, detached, and proxied entities. |
| ORM-09 | P1 | An import of a million rows becomes slower over time. What would you measure? | Consider batching, persistence-context size, and partial failure. |
| ORM-10 | P1 | Can a cache serve stale account information after a transaction commits? | Distinguish local entity state, shared cache, and database replicas. |

## SQL and relational databases — SQL

Evidence: R3/R4 reported themes; R1/R2 requirements; T5/T6 references. Use synthetic account and transaction fixtures.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| SQL-01 | P0 | Find accounts without a successful payment in a given period. | What changes with NULLs, a missing row, and filters after a LEFT JOIN? |
| SQL-02 | P0 | Return the latest successful transaction per account. | Define ties, empty accounts, and deterministic ordering. |
| SQL-03 | P0 | Find the top three customers by monthly volume within each branch. | Do ties produce exactly three rows or more? |
| SQL-04 | P0 | Calculate a running balance from ordered account entries. | Consider equal timestamps, reversals, and opening balance. |
| SQL-05 | P0 | Propose an index for account, status, and time-filtered transaction searches. | How do selectivity, ordering, write cost, and optional filters affect it? |
| SQL-06 | P0 | A query ignores an index and becomes slow after data growth. How do you investigate? | How do estimates differ from measured execution? |
| SQL-07 | P0 | Two sessions read and change the same balance. Predict behavior at a chosen isolation level. | Can a multi-row invariant fail without a same-row write conflict? |
| SQL-08 | P0 | Diagnose a database deadlock and design a retry boundary. | Is retrying one statement equivalent to retrying the business operation? |
| SQL-09 | P1 | Design pagination over an account's rapidly growing transaction history. | What happens when new rows arrive between pages? |
| SQL-10 | P0 | Reconcile internal postings with a settlement file, finding missing and mismatched records. | Include duplicates, NULLs, late records, currencies, and a safe schema migration. |

## Distributed services — DIST

Evidence: R1/R2 requirements, R4 scenario themes; T8 API example. Original failure scenarios.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| DIST-01 | P0 | A payment request times out. What does the caller actually know? | Draw outcomes with failure before and after remote commit. |
| DIST-02 | P0 | Define the contract for safely retrying a payment API. | What if the same key arrives concurrently or with a different payload? |
| DIST-03 | P0 | A database write succeeds but publishing its event fails. What choices do you have? | Where can duplicates or missing work appear after a crash? |
| DIST-04 | P0 | Order, payment, and inventory services must coordinate a purchase. How would you reason about failure? | Can every completed business action be undone? |
| DIST-05 | P0 | Choose timeout and retry behavior across a chain of services. | What happens when every layer retries independently? |
| DIST-06 | P0 | One slow dependency causes unrelated endpoints to fail. How would you isolate it? | How should overload and recovery differ from ordinary errors? |
| DIST-07 | P0 | A cached balance differs from the database after an update. How would you define acceptable behavior? | Can invalidation and concurrent cache fills race? |
| DIST-08 | P1 | Choose consistency requirements during a network partition. | Which operations can safely remain available? |
| DIST-09 | P1 | A distributed lock expires while its owner is still working. What could happen? | What must the protected resource be able to distinguish? |
| DIST-10 | P1 | Decide whether to split a monolith into services. | What would make a modular monolith a better intermediate state? |

## Kafka and messaging — MSG

Evidence: R1 explicitly requires Kafka; T7 official design reference. Original practice scenarios.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| MSG-01 | P0 | Choose partition keys for account events. | What happens to ordering, hot accounts, and later repartitioning? |
| MSG-02 | P0 | Predict behavior as consumers join and leave a group. | How does a long-running handler affect progress? |
| MSG-03 | P0 | A consumer writes to a database, crashes, then sees the same event. What can happen? | Move the crash to either side of offset acknowledgement. |
| MSG-04 | P0 | Explain the scope of an exactly-once claim in a messaging pipeline. | Does an external payment call belong to that scope? |
| MSG-05 | P0 | Choose producer durability and retry settings for financial events. | What can a successful acknowledgement prove about downstream effects? |
| MSG-06 | P0 | Consumer lag grows sharply after a release. How would you diagnose it? | Distinguish throughput limits, poison records, and a skewed partition. |
| MSG-07 | P1 | Design retry and quarantine behavior for one malformed event. | What happens to ordering and operational visibility? |
| MSG-08 | P1 | Change an event schema while old consumers still run. | Compare missing fields, changed meanings, and replay of old events. |
| MSG-09 | P1 | Replay last week's events after fixing a bug. How do you make the plan safe? | Which effects must be suppressed or reconciled? |
| MSG-10 | P1 | Compare log retention and compaction for an account event topic. | Is the topic an audit ledger, a state view, or both? |

## High-level system design — SYS

Evidence: R1/R2/R5/R6 role and interview requirements. These system prompts are original exercises.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| SYS-01 | P0 | Design a money-transfer service. Start with requirements and invariants. | Introduce a retry, concurrent debit, and regional failure separately. |
| SYS-02 | P0 | Design payment initiation plus asynchronous status updates. | What if the provider times out and later sends contradictory callbacks? |
| SYS-03 | P0 | Design an account statement and transaction-history service. | Compare fresh reads, replica lag, and long historical queries. |
| SYS-04 | P0 | Design a high-volume notification system. | Define what duplicate prevention means at the external provider boundary. |
| SYS-05 | P0 | Design a distributed API rate limiter. | Consider bursts, hot tenants, clock behavior, and store failure. |
| SYS-06 | P1 | Design settlement reconciliation for daily files and live events. | How do reruns, partial files, and late corrections affect correctness? |
| SYS-07 | P1 | Design an immutable audit history with controlled access. | How would retention, correction, and tamper evidence work? |
| SYS-08 | P1 | Design a fraud-screening integration in a payment path. | What happens if screening is unavailable or too slow? |
| SYS-09 | P1 | Estimate capacity and find the first bottleneck in your design. | Change peak load by 10x without assuming average load scales uniformly. |
| SYS-10 | P0 | Design recovery from losing a database region. | Define acceptable loss and downtime, then describe how you test them. |

## Low-level design and machine coding — LLD

Evidence: R3 design-pattern themes, R5 design/coding expectations; original assignments.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| LLD-01 | P0 | Model a payment lifecycle and allowed operations. | How do invalid transitions and duplicate commands behave? |
| LLD-02 | P0 | Design a fee-calculation component for several payment types. | Add a new rule without scattering conditionals or overengineering. |
| LLD-03 | P0 | Implement a small in-memory rate limiter with a testable clock. | Define thread safety and boundary behavior. |
| LLD-04 | P0 | Design a notification dispatcher with interchangeable providers. | How do timeouts, retries, and provider-specific errors enter the contract? |
| LLD-05 | P1 | Implement a bounded cache and its eviction behavior. | What makes a concurrent version harder? |
| LLD-06 | P1 | Design a reconciler that reads different input formats. | Separate parsing, matching, business rules, and reporting. |
| LLD-07 | P1 | Model a scheduler for recurring jobs. | What does cancellation mean if execution already began? |
| LLD-08 | P0 | Refactor a large service into components with explicit invariants. | Explain where an interface or design pattern adds real value. |
| LLD-09 | P1 | Design a reusable client for several bank integrations. | How do you prevent generic abstractions from hiding important differences? |
| LLD-10 | P0 | Build a small transfer API in a 90-minute exercise. | State what you can prove with tests and what remains outside the exercise. |

## Data structures and algorithms in Java — DSA

Evidence: R2/R5 explicitly require coding and algorithms. These are standard-pattern exercises, not claimed company questions. Discuss a baseline, invariant, complexity, code, and tests.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| DSA-01 | P0 | Find the longest contiguous subarray summing to K; values may be negative. | What changes if all values are positive or the sum overflows int? |
| DSA-02 | P0 | Find the longest substring with at most K distinct symbols. | Define a symbol, empty input, and K=0. |
| DSA-03 | P0 | Merge overlapping time intervals. | Do touching endpoints overlap under your contract? |
| DSA-04 | P0 | Find the top K most frequent account IDs in an event batch. | Define ties and extend to a stream larger than memory. |
| DSA-05 | P0 | Search a sorted sequence for the first qualifying value. | Prove boundaries for empty input and duplicate values. |
| DSA-06 | P0 | Detect a cycle in a linked structure and locate its entry. | Explain why your method terminates without modifying the structure. |
| DSA-07 | P0 | Validate nested delimiters with useful error positions. | How would quoted strings change the parser contract? |
| DSA-08 | P0 | Traverse a tree by level and compute a requested aggregate. | Handle skewed trees and recursion depth. |
| DSA-09 | P0 | Determine whether a binary tree satisfies a search-order contract. | Are duplicates permitted, and can sentinel bounds overflow? |
| DSA-10 | P0 | Find a shortest path in an unweighted dependency graph. | What changes with weighted edges or unreachable nodes? |
| DSA-11 | P0 | Produce a valid execution order for tasks with prerequisites. | How do you report a cycle or isolated tasks? |
| DSA-12 | P1 | Find connected groups in a stream of pairwise relationships. | Compare batch traversal with incremental connectivity. |
| DSA-13 | P1 | Generate all valid combinations that meet a target. | Avoid duplicates and explain pruning without missing results. |
| DSA-14 | P1 | Minimize the number of denominations required to reach an amount. | Why might a locally best choice fail? |
| DSA-15 | P1 | Find the length of a longest increasing subsequence. | Explain a simple approach before optimizing; define strictness. |

## Production, cloud, and delivery — OPS

Evidence: R1/R2/R6 production and ownership requirements. Original incident drills.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| OPS-01 | P0 | Payment API p99 rises from 200ms to 5s after a rollout. What do you investigate first? | How do you separate mitigation from root-cause proof? |
| OPS-02 | P0 | All request threads wait for database connections. What hypotheses would you test? | Could enlarging the pool worsen the incident? |
| OPS-03 | P0 | Define useful service health signals and alerts for payments. | Why might successful HTTP responses hide a business outage? |
| OPS-04 | P0 | Design a backward-compatible service and schema release. | How does rollback work after new-format data is written? |
| OPS-05 | P1 | Configure readiness, liveness, startup, and graceful termination for a service. | What happens to in-flight requests during a rollout? |
| OPS-06 | P1 | Choose cloud components for a resilient Java service. | Explain network access, identity, backup, zone failure, and cost. |
| OPS-07 | P0 | Design unit, integration, contract, and load checks for a transfer flow. | Which assumptions require the real database engine? |
| OPS-08 | P1 | A request fails intermittently before reaching your application. How do you investigate? | Distinguish DNS, TCP, TLS, proxy, and server failures. |
| OPS-09 | P1 | A service scales out but throughput stops improving. Why might that happen? | Look at shared bottlenecks and resource limits. |
| OPS-10 | P1 | Use AI-generated code in a critical service without outsourcing your judgment. | How would you test plausible but incorrect transaction or security behavior? |

## Security and API correctness — SEC

Evidence: R5 coding-quality expectations; T9 official authorization reference. Original BFSI preparation extensions, not a regulatory checklist.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| SEC-01 | P0 | Explain the responsibilities of OAuth2, OIDC, and an access token in your API. | What must be validated besides token signature? |
| SEC-02 | P0 | An authenticated user substitutes another account ID in a request. What determines access? | What if the service is called through a different entry point? |
| SEC-03 | P0 | Design authorization boundaries for multiple tenants. | Can caches, queries, or asynchronous work cross the boundary? |
| SEC-04 | P1 | Explain when CSRF and CORS matter for your application. | Change credential transport from a bearer header to a cookie. |
| SEC-05 | P0 | Review how user-controlled values reach SQL and external URLs. | Which inputs cannot be handled as ordinary bound values? |
| SEC-06 | P0 | Decide which payment information may appear in logs and traces. | How would you preserve diagnosability and auditability? |
| SEC-07 | P1 | Rotate a signing key or service credential without an outage. | How do stale clients and emergency revocation affect the plan? |
| SEC-08 | P0 | Verify an incoming payment-provider callback. | Consider replay, duplicate delivery, timestamps, and malformed payloads. |
| SEC-09 | P1 | Design stable API error and validation contracts. | Compare malformed input, forbidden actions, and transient failures. |
| SEC-10 | P1 | Prevent a valid API client from exhausting service resources. | How do quotas differ from input validation and authentication? |

## BFSI domain and correctness — BFSI

Evidence: R1/R2 financial-services context; T8 external API example. Domain scenarios are instructor-authored, not statements of legal requirements.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| BFSI-01 | P0 | INR 1,000 is available; two distinct INR 700 withdrawals both succeed. How could that occur? | Draw the interleaving before proposing any fix. |
| BFSI-02 | P0 | Model available balance, posted balance, and a payment hold. | How do expiry, capture, and concurrent spending interact? |
| BFSI-03 | P0 | Define ledger invariants for a transfer between accounts. | What makes a correction different from deleting history? |
| BFSI-04 | P0 | Process a partial refund followed by another refund request. | What if concurrent refunds exceed the original captured amount? |
| BFSI-05 | P0 | Handle a transfer reported pending locally and successful by a provider. | Who is authoritative, and how is ambiguity resolved? |
| BFSI-06 | P0 | Design reconciliation between internal records and a settlement source. | Distinguish missing, duplicated, late, and amount-mismatched entries. |
| BFSI-07 | P0 | Choose money precision, rounding, and currency representation. | What happens when rounding each item differs from rounding the total? |
| BFSI-08 | P1 | Model business dates and cutoff windows across time zones. | How do holidays, late arrivals, and daylight-saving changes affect processing? |
| BFSI-09 | P1 | Design a maker-checker approval flow for sensitive changes. | Prevent the same actor or stale approval from bypassing the intended control. |
| BFSI-10 | P1 | Design auditability, retention, and recovery for a financial workflow. | Which details require confirmation with compliance and the actual regulator's current rules? |

## Leadership, project depth, and hiring — LEAD

Evidence: R1/R2/R5/R6 ownership, communication, mentoring, and behavioral expectations. Original prompts.

| ID | Priority | Initial question | Later probe |
|---|---|---|---|
| LEAD-01 | P0 | Explain a system you owned and one difficult decision you personally made. | Which metrics can you substantiate, and what did others own? |
| LEAD-02 | P0 | Describe a production incident you helped resolve. | What changed afterwards, and how do you know it helped? |
| LEAD-03 | P0 | Describe a technical disagreement with a peer or architect. | What evidence changed the decision, including your own view? |
| LEAD-04 | P0 | Describe a deadline that conflicted with a correctness requirement. | What did you reduce, escalate, or measure? |
| LEAD-05 | P0 | Give an example of helping another engineer become more independent. | How did you avoid taking over their work? |
| LEAD-06 | P0 | Explain a design or estimate that turned out wrong. | How did you communicate and recover? |
| LEAD-07 | P1 | Prioritize technical debt against a business feature. | Show consequences and an incremental plan. |
| LEAD-08 | P1 | Describe coordination across multiple teams or external partners. | How did you handle unclear ownership or a blocked dependency? |
| LEAD-09 | P0 | Explain why you want this role and how your BFSI experience transfers. | Identify a genuine gap and your evidence of learning it. |
| LEAD-10 | P0 | Evaluate an offer against your INR 40+ LPA objective. | Separate fixed cash, variable pay, equity, one-off payments, and conditions. |
