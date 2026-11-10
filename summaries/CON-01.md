# CON-01: two threads increment a shared counter

Status: partial recap; question in progress. Correct initial prediction at H0; highest support now H3 after teaching monitor semantics. No overall score or experiment. Java 17 reference version.

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

Support is H3 after the monitor explanation. The correct method choice was learner-proposed; its precise locking behavior was taught. Review due 2026-11-11; no overall score or independent pass yet.

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

## Pending

In Counter, static synchronized void increment() executes value++, while instance synchronized void reset() executes value = 0; both access the same static int value. T1 calls Counter.increment() and T2 calls counterA.reset(). Can the two method bodies execute at the same time? Explain in your own words which object each call locks.

The mixed-method scenario has not been answered. See [lesson 3](../sessions/2026-11-10-lesson-03.md).
