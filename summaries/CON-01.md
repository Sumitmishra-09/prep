# CON-01: two threads increment a shared counter

Status: initial prompt only; no answer, score, or experiment yet. Java 17 reference version.

## Assumptions

A shared Counter instance starts with int value = 0. Each of two worker threads calls increment() once; that method executes value++. There is no synchronization around the increment. The main thread successfully joins both workers before reading value.

## Pending

In Java 17, a shared Counter object has int value = 0 and increment() executes value++. Two worker threads each call increment() exactly once, without synchronization. The main thread successfully joins both workers before reading value. What final values are possible, and how could the threads produce them?

No outcome or solution is recorded before the learner attempts it. See [lesson 3](../sessions/2026-11-10-lesson-03.md).
