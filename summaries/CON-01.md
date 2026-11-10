# CON-01: two threads increment a shared counter

Status: partial recap; question in progress. Correct initial prediction at H0; highest support now H1 for the reasoning follow-up. No overall score or experiment. Java 17 reference version.

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

## Pending

How would you change this shared counter so that, after both threads finish, the value is always 2? Choose one approach and explain why it prevents the read-0/read-0/write-1/write-1 sequence.

A concrete fix has not yet been proposed or implemented. See [lesson 3](../sessions/2026-11-10-lesson-03.md).
