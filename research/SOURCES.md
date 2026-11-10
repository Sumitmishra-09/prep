# Research ledger

Checked **2026-11-10**. This is a curated sample, not a census of interviews. Public candidate reports are self-reported and may be incomplete; official job requirements establish role relevance but do not prove that a particular question is asked. No reliable frequency percentage or salary guarantee is inferred. Question priorities are instructor judgments tailored to this learner.

## Hiring and interview evidence

| ID | Source and date | What the source supports | Limits |
|---|---|---|---|
| R1 | [Empower: Sr Engineer Software, Bengaluru](https://jobs.empower.com/job/bengaluru/sr-engineer-software/42743/102373232800), posted 2026-11-03 | Java/Spring, Kafka, AWS, financial-services modernization, resiliency, database integration, troubleshooting, and mentoring | Employer requirements; no interview transcript or India pay band |
| R2 | [PayU Payments: Senior Software Engineer](https://careers.payu.in/PayU/job/Bengaluru-Senior-Software-Engineer/53282180/), page dated 2026-10-31 | Java/Spring Boot, algorithms/complexity, relational and NoSQL databases, AWS, scalable services, communication, and team contribution | Employer requirements; publication can change as a role is reposted |
| R3 | [Accenture senior Java interview candidate account](https://www.jointaro.com/interviews/companies/accenture/experiences/senior-software-engineer-java-developer-pune-maharashtra-may-13-2026-no-offer-positive-aac46bbd/), displayed 2026-05-14 | Candidate reports collections, thread/executor questions, dependency injection, transactions, ORM/JDBC, SQL joins, and design patterns | Anonymous anecdote on a hosting platform; interview occurrence not independently verified; ignore site-wide success-rate claims derived from one account |
| R4 | [Six-year backend developer's interview account](https://www.reddit.com/r/interviewpreparations/comments/1qiqtjk/recent_backend_java_developer_interview_experience/), search metadata dated 2026-01-21 | Candidate reports locking, transactional boundaries, MySQL composite indexes, rate limiting, Spring events, and project-specific depth | Anonymous first-person anecdote; AI/ML questions followed that candidate's project and are not evidence of a universal Java requirement |
| R5 | [Amazon official SDE III interview preparation](https://amazon.jobs/content/en/how-we-hire/sde-iii-interview-prep), undated page accessed 2026-11-10 | Coding, system design, behavioral evidence, robust code, and leadership; prepares for a senior loop | Official process for this role, not a universal process for all employers or levels |
| R6 | [Amazon senior SDE role, India](https://amazon.jobs/en/jobs/10529736/sr-software-development-engineer-amazon), accessed 2026-11-10; posting date not established | Architecture, distributed systems, mentoring, delivery, and operational ownership | Role-scope example; no inference that seven years automatically qualifies someone at this level |

### Resulting preparation priorities — our inference

Prepare both foundational depth and practical senior-level scenarios. Maintain Java/Spring/SQL fluency; practice concurrency, ambiguous outcomes, messaging failures, performance investigation, coding, design, and ownership stories. BFSI examples make the exercises relevant to the learner's experience. The bank's exact scenarios and follow-up variations are authored for this curriculum, not copied interview transcripts.

Do not treat “recent” as “new technology only.” Do not assume every employer uses the same DSA weighting. Product-role coding and design requirements justify sustained coding practice; actual target-job evidence should refine the allocation.

## Primary technical references

Read a focused section after an attempt or when requesting a hint. These verify technical behavior, not question frequency. Current-documentation URLs move; record the concrete version when running an exercise.

| ID | Reference | Use |
|---|---|---|
| T1 | [Oracle JDK 25 documentation](https://docs.oracle.com/en/java/javase/25/) | Language/API reference, diagnostics, migration, and JVM documentation; switch to the actual exercise JDK where necessary |
| T2 | [Oracle Java 21 announcement](https://blogs.oracle.com/java/the-arrival-of-java-21) and [Oracle JDK 24 migration guide](https://docs.oracle.com/en/java/javase/24/migrate/jdk-migration-guide.pdf) | Version-aware virtual-thread study; do not teach one release's limitations as timeless facts |
| T3 | [Spring transaction annotations](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) | Verify transaction interception and configuration assumptions against the relevant Framework version |
| T4 | [Spring Boot system requirements](https://docs.spring.io/spring-boot/system-requirements.html) | Verify the target release's Java/build/runtime requirements before upgrading; the fetched page identified Boot 4.1.2 |
| T5 | [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | A concrete database's isolation semantics; not proof of MySQL or Oracle behavior |
| T6 | [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) | Plan reading and measurement for the SQL lab |
| T7 | [Apache Kafka 4.1 design documentation](https://kafka.apache.org/41/design/design/) | Messaging guarantees and design concepts; version-pinned reference, not a claim that 4.1 is newest |
| T8 | [Stripe idempotent request API](https://docs.stripe.com/api/idempotent_requests) | A real API contract to compare after designing our own; do not generalize one provider/API version to all providers |
| T9 | [Spring Security method authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html) | Validate method and request authorization assumptions against the selected version |

The OpenJDK JEP 444 and JEP 491 pages returned HTTP 403 during this research. Oracle primary references were used instead. A JPMC lead-role search result was relevant but its page had no readable body, so it is not used to substantiate detailed curriculum requirements. Paywalled/reposted “real question” lists were not treated as verified employer evidence.

## Refresh procedure

Before each employer-specific preparation week, inspect the actual job description and recruiter-confirmed interview format. Record source URL, access date, role/location, original date when available, evidence type, and which priority changes follow. Verify release-sensitive claims in official documentation. If discussing current regulatory requirements, consult the relevant regulator's current primary documents; this curriculum does not establish those requirements.
