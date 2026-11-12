# CON-01: two threads increment a shared counter

Status: guided diagnostic completed on 2026-11-12; assisted learning, not mastery. Overall 2/4, highest support H3. Retrieval due 2026-11-13. Java 17 reference version. No counter experiment was executed.

## Assumptions

A shared Counter instance starts with int value = 0. Each of two worker threads calls increment() once; that method executes value++. There is no synchronization around the increment. The main thread successfully joins both workers before reading value.

## Established so far

The learner correctly predicts "1 or 2" and then explains the value-1 case: both threads can read 0, compute 1 and write 1. The outcome prediction was H0; the causal explanation followed an H1 focusing prompt. No misconception has been observed.

## Resolved timeline and recap

| Step | T1 | T2 | Shared value |
|---|---|---|---|
| 1 | Reads 0 | | 0 |
| 2 | | Reads 0 | 0 |
| 3 | Computes 0 + 1; writes 1 | | 1 |
| 4 | | Computes 0 + 1; writes 1 | 1 |

Both calls execute, but the second write stores the same result rather than adding to the first result. This is a lost update. The instructor adds the term and explains that value++ comprises reading, adding, and writing; it is not one atomic operation merely because it is one Java statement. A valid ordering yielding 2 has T1 read 0/write 1 and T2 then read 1/write 2. The table is a reasoning trace, not observed runtime output.

Reference: [Oracle thread interference tutorial](https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html). The tutorial targets JDK 8; this basic increment behavior also applies to our Java 17 example.

## Volatile-only increment: resolved follow-up

The learner correctly rejects a guarantee of 2 after changing only the field to volatile. Their reason is correct: both threads may read the initial 0 before either writes 1. They also associate volatile with visibility.

Instructor precision: visibility is a guarantee under Java's ordering rules, not merely a chance of observing a new value. A volatile read observes the most recent preceding write to the same field in synchronization order, and a volatile write happens-before subsequent reads of that field. It does not refresh a value already read or make the whole read/add/write operation atomic.

The existing read-0/read-0/write-1/write-1 timeline remains valid with volatile: 0 is the current value at both reads. This establishes why better visibility alone does not solve the lost update. The answer was reasoned about, not executed.

Reference: [JLS 17 memory-model rules](https://docs.oracle.com/javase/specs/jls/se17/html/jls-17.html#jls-17.4.5), including synchronization-order consistency in section 17.4.7.

## Synchronized method: correct fix, monitor misconception repaired

The learner proposes synchronizing increment(), which is correct for the one shared Counter instance, but also proposes a second lock on value in case both threads enter. The latter is unnecessary: an instance synchronized method acquires the receiver's monitor (this) before executing the body. Two different threads can attempt calls together, but only one can hold that monitor and execute the increment at a time in this example.

Resolved method change:

```java
synchronized void increment() {
    value++;
}
```

This is an explanatory snippet of the learner-proposed fix, not an executed implementation. T1 acquires the shared counter's monitor, reads 0 and writes 1; T2 waits outside the body. T1 releases the monitor; T2 acquires it, sees the first write, reads 1 and writes 2. Either thread can win first. Releasing and then acquiring the same monitor also provides the visibility guarantee. After both completed joins, main observes 2 under the original assumptions.

Java locks objects. If "synchronizing value" means synchronized(value), the primitive int cannot be used as the required lock object. An inner synchronized(this) block would be redundant in this method, not extra protection. The general requirement is that cooperating accesses protect the full operation with the same monitor; locking does not automatically stop unrelated unsynchronized code from touching the field.

References: [Oracle synchronized methods](https://docs.oracle.com/javase/tutorial/essential/concurrency/syncmeth.html) and [Intrinsic locks](https://docs.oracle.com/javase/tutorial/essential/concurrency/locksync.html). These JDK 8 tutorial rules also apply to this Java 17 exercise.

At this Nov 10 stage, support became H3 and retrieval was scheduled for Nov 11. The correct method choice was learner-proposed; its precise locking behavior was taught. The diagnostic was subsequently completed on Nov 12; the current assessment and review date are below.

## Static field, different receiver instances: resolved follow-up

The learner correctly recognizes that the static field is shared across instances of this class and ends by proposing that the method also be static. The instructor distinguishes the original code from this proposed correction.

| Method used | T1 locks | T2 locks | Same monitor? |
|---|---|---|---|
| Instance synchronized increment on counterA / counterB | counterA | counterB | No |
| Static synchronized increment declared in Counter | Counter.class | Counter.class | Yes |

The original method is still an instance method even though it accesses a static field. Different receiver monitors do not exclude each other, so both increments can overlap and lose an update; 2 is not guaranteed. Static storage and class initialization do not serialize later modifications.

The learner's proposed repair is valid for the given shared counter:

```java
static synchronized void increment() {
    value++;
}
```

Both calls acquire the monitor of the Counter Class object. With the original assumptions of two completed increments from 0 and no other writers, final value is 2. This guarantee comes from the common monitor protecting the whole increment, not from the field being static alone. The method declaration chooses the implicit monitor; the fields used in the body do not choose it.

Reference: [JLS 17.1](https://docs.oracle.com/javase/specs/jls/se17/html/jls-17.html#jls-17.1). The snippet is explanatory, not executed. H3 support remains; no independent mastery is inferred from the learner's proposed fix.

## Mixed static and instance methods: resolved follow-up

On Nov 12, the learner correctly explains that static synchronized increment() locks Counter.class while instance synchronized reset() locks the receiver. These are different objects, so the method bodies can execute concurrently and access the same static field without mutual exclusion between those two paths. This is a correct explanation in the learner's own words after the earlier monitor teaching; it is not a fresh full independent assessment.

The rule is to identify the actual monitor for every access path to the shared state. Merely seeing synchronized on both methods does not establish mutual exclusion. This resolves the final explored branch.

## Interview-ready recap

An increment of a shared int is a read-modify-write operation. Two threads may both read 0 and write 1, losing an update. Volatile provides visibility and ordering, but does not make the complete increment atomic. A synchronized instance method acquires its receiver's monitor before its body; for the original shared instance this protects the full increment and yields 2 after both workers finish and are joined. For a shared static field accessed through different instances, those receiver monitors do not coordinate; the proposed static synchronized method instead uses the declaring Class object's monitor. Static and instance synchronized methods use different monitors, so they can overlap even when accessing the same field. Determine whether the competing operations use the same monitor and cover the whole operation.

## Assessment and later retrieval

- Correctness: initial outcomes, lost-update timeline, volatile limitation, and final mixed-monitor application correctly explained. The last answer on Nov 12 correctly names both monitor objects and the consequence.
- Reasoning: initially proposed extra locking inside an already synchronized method and needed clarification of instance versus class monitors. H3 teaching was required; later application was correct.
- Edge cases: explored different receiver instances, static storage and mixed synchronized methods. Broader alternatives and deterministic experiment design remain unassessed.
- Communication: final explanation connects monitor identity directly to concurrent access. No study duration invented.
- Overall: 2/4, learning; no independent pass or mastery. The lesson spans Nov 10 and Nov 12. No counter implementation or experiment was executed.
- Retrieval due Nov 13: give a 60-120 second explanation without notes, then reason through a fresh monitor-identity or increment variant. Future lab work should include forcing an interleaving without relying on sleep; it has not been completed.

Historical reasoning: [lesson 3](../sessions/2026-11-10-lesson-03.md). Closing response and next checkpoint: [lesson 4](../sessions/2026-11-12-lesson-04.md).
