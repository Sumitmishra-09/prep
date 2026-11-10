# JAVA-01: a HashMap lookup stops finding an entry

Status: **partial recap; question in progress**. Updated 2026-11-10. Java 17 is the reference version. An instructor-authored experiment has now been executed after the learner's prediction.

## Established so far

The learner correctly identified `hashCode()` as a relevant first inspection point for a failed HashMap lookup. This is a useful hypothesis, not yet a demonstrated root cause.

Terminology clarification: HashMap is a hash-table-based map, but a stored entry retains the key reference and associated value; the key is not replaced by a unique hash identifier. The key class can override `hashCode()` to return an integer used in locating candidate entries. Candidate matching also considers the stored hash and key identity/equality. `get(key)` returns the mapped value, not the key.

## What the instructor is adding

A small lookup model: key -> hash calculation -> candidate bucket -> hash and identity/equality matching -> value. This deliberately omits tree-bin and resizing details. Equal objects must have equal hash codes; sharing a hash code does not alone establish equality. These are concepts to apply, not proof the original bug was caused by mutation.

References: [Object hashCode contract](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) and [OpenJDK 17 HashMap implementation](https://github.com/openjdk/jdk17u/blob/master/src/java.base/share/classes/java/util/HashMap.java).

## Key-mutation prediction and result

For a toy `AccountKey`, assume `hashCode()` returns its integer `accountId`, and `equals()` compares `accountId`:

```java
AccountKey key = new AccountKey(101);
map.put(key, "ACTIVE");
key.setAccountId(202);
String result = map.get(key);
```

The learner predicted a failed lookup, which was correct, but attributed it to equality changing while the hash and bucket remained the same. In this toy class, the hash actually changes from 101 to 202. With the selected map's 16-bucket OpenJDK 17 layout, the derived bucket index changes from 5 to 10.

The original entry is not automatically moved after key mutation. It keeps its insertion-time hash metadata and a reference to the same now-mutated object. Correct `equals()` remains reflexive: the object equals itself. The map has not saved an independent copy of the old key state for an old-versus-new equality comparison.

Observed using Oracle Java / HotSpot 17.0.9: lookup result `null`, zero calls to `equals()` during that lookup, map size still 1, and iteration still sees the value ACTIVE. The [probe and run instructions](../practice/java/README.md) preserve the exact output. Bucket indices were calculated from the source algorithm, not measured through reflection.

## Mini-recap

- Correct prediction: the lookup can fail even when the same key reference is supplied.
- Correction: this example changes the hash and search bucket; it does not fail because the same object becomes unequal to itself.
- Extra concept: a map entry can remain present and iterable while a hash-based lookup fails after unsafe key mutation.
- API qualification: mutating equality-relevant key state while stored in a Map has unspecified behavior; this is an implementation-specific demonstration. See the [Map documentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html).

## Still open

The learner proposes using Object's identity-based hash to keep it stable. This can be consistent when equality is also identity-based. Changing only the hash while retaining accountId-based equality does not guarantee that equal objects have equal hashes. Identity hashes are not guaranteed unique. See the [Object contract](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html).

Next prediction: create two distinct AccountKey objects with accountId 101. Keep equality based on accountId, but use Object's hash implementation and assume these two objects receive different hashes. After storing ACTIVE with the first object, what happens when looking up with the second? This variation has not been executed or answered yet. Stable-key redesign remains incomplete.

No overall score, independent pass, or mastery is recorded yet. The [lesson log](../sessions/2026-11-10-lesson-02.md) preserves the learner's actual response and distinguishes observed output from instructor explanation.
