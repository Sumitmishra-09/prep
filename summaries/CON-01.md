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

## Pending

A colleague changes only the shared field to volatile int value = 0, leaving increment() as value++ and joining both workers before reading. Does this guarantee a final value of 2? Explain using the two-thread timeline.

The changed-scenario answer and fixes are not yet supplied. Volatile knowledge is unassessed. See [lesson 3](../sessions/2026-11-10-lesson-03.md).
