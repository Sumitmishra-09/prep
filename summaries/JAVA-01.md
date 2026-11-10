# JAVA-01: a HashMap lookup stops finding an entry

Status: **partial recap; question in progress**. Updated 2026-11-10. Java 17 is the reference version. No experiment has been run yet.

## Established so far

The learner correctly identified `hashCode()` as a relevant first inspection point for a failed HashMap lookup. This is a useful hypothesis, not yet a demonstrated root cause.

Terminology clarification: HashMap is a hash-table-based map, but a stored entry retains the key reference and associated value; the key is not replaced by a unique hash identifier. The key class can override `hashCode()` to return an integer used in locating candidate entries. Candidate matching also considers the stored hash and key identity/equality. `get(key)` returns the mapped value, not the key.

## What the instructor is adding

A small lookup model: key -> hash calculation -> candidate bucket -> hash and identity/equality matching -> value. This deliberately omits tree-bin and resizing details. Equal objects must have equal hash codes; sharing a hash code does not alone establish equality. These are concepts to apply, not proof the original bug was caused by mutation.

References: [Object hashCode contract](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) and [OpenJDK 17 HashMap implementation](https://github.com/openjdk/jdk17u/blob/master/src/java.base/share/classes/java/util/HashMap.java).

## Pending prediction — leave the result unresolved

For a toy `AccountKey`, assume `hashCode()` returns its integer `accountId`, and `equals()` compares `accountId`:

```java
AccountKey key = new AccountKey(101);
map.put(key, "ACTIVE");
key.setAccountId(202);
String result = map.get(key);
```

Does passing the same key object guarantee the lookup still finds the value? Reason from the hash used at insertion and at lookup before executing the example.

No outcome, fix, score, or mastery is recorded yet. The [lesson log](../sessions/2026-11-10-lesson-02.md) preserves the learner's actual response.
