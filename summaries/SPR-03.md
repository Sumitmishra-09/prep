# SPR-03: transaction behavior across method calls

Status: initial prompt on 2026-11-12; unassessed. H0, zero responses, no score, no runtime experiment.

## Assumptions

Spring Framework 6.2 is the exercise reference, not the learner's confirmed production stack. Proxy-based transaction management and a suitable transaction manager are correctly configured. A controller calls transfer() on an injected TransferService bean with no existing transaction. transfer() directly calls public debit() on the same object. Only debit() has Spring's @Transactional annotation and performs two JDBC updates using the configured DataSource.

## Pending

Assume Spring Framework 6.2 with proxy-based transaction management correctly configured and no existing transaction. A controller calls transfer() on its injected TransferService bean. transfer() is not annotated and directly calls debit() on the same object. debit() is public, annotated with Spring @Transactional, and performs two JDBC updates. Does the annotation on debit() start a Spring-managed transaction for this call? Explain the call path.

The outcome and fixes are not supplied before the learner's attempt. See the code and checkpoint in [lesson 4](../sessions/2026-11-12-lesson-04.md).
