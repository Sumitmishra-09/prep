# Initial diagnostic

Purpose: determine depth, not judge confidence. All skills start unassessed. Ask these individually, not as a questionnaire. Suggested budget: 150–180 minutes across two study sessions including debrief. An incomplete diagnostic is resumed, not marked failed.

| Order | ID | Initial task | Approx. minutes |
|---|---|---|---:|
| 1 | BFSI-01 | An account has INR 1,000. Two distinct INR 700 withdrawals arrive together and both requests return success. Is that possible in a Spring Boot service, and how? Explain your assumed request/database timeline before suggesting a fix. | 10 |
| 2 | JAVA-01 | A key can be inserted into a HashMap but later cannot be found. What would you inspect and how would you reproduce your hypothesis? | 10 |
| 3 | CON-01 | Two worker threads increment a shared counter. Predict possible results and design a small experiment. | 10 |
| 4 | SPR-03 | A method with @Transactional calls another method on the same object. What facts do you need before predicting transaction behavior? | 10 |
| 5 | SQL-02 | Produce the latest successful transaction per account, including a stated tie rule and accounts with no successful transaction. | 15 |
| 6 | DSA-01 | Find the longest contiguous subarray with sum K; values may be negative. Think aloud and then code in Java. | 30 |
| 7 | ORM-02 | An endpoint gets slower as its result list grows. How would you establish whether ORM access is responsible? | 10 |
| 8 | MSG-03 | A consumer changes a database row, crashes, and receives the same event again. Predict the possible outcomes. | 10 |
| 9 | SYS-01 | Outline a money-transfer service after first establishing requirements and invariants. | 15 |
| 10 | OPS-01 | Payment API p99 goes from 200ms to 5s after a rollout. What do you investigate first, and why? | 10 |
| 11 | SEC-02 | A validly authenticated user changes an account ID in a request. How do you assess the outcome? | 5 |
| 12 | LEAD-01 | Walk through a system you personally owned and a difficult decision you made, with evidence of impact. | 15 |

Ask about production Java/Spring/SQL versions during the relevant task. Do not assume the laptop's Java version is the production version. Do not disclose fixes or named mechanisms before the learner has attempted a model.
