# CON-01: two threads increment a shared counter

Status: partial recap; question in progress. Correct initial prediction at H0; highest support now H1 for the reasoning follow-up. No overall score or experiment. Java 17 reference version.

## Assumptions

A shared Counter instance starts with int value = 0. Each of two worker threads calls increment() once; that method executes value++. There is no synchronization around the increment. The main thread successfully joins both workers before reading value.

## Established so far

The learner predicts "1 or 2", which is correct under the stated assumptions. This establishes a correct outcome prediction, not yet an explanation of the concurrent execution. No misconception is inferred from the brief response.

## Pending

Starting with value = 0, show one ordering of T1 and T2 that leaves the counter at 1 after both threads finish. State what each thread reads and what it writes.

The causal timeline and fixes remain unanswered and are not included in this recap. See [lesson 3](../sessions/2026-11-10-lesson-03.md).
