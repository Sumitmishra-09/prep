# JAVA-01: a HashMap lookup stops finding an entry

Status: **guided diagnostic completed; assisted learning, not mastery**. Updated 2026-11-10. Score 2/4, highest support H3; retrieval due 2026-11-11. Java 17 is the reference version. One instructor-authored mutation experiment was executed after the learner's prediction; later variations were discussed without execution.

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

## Identity hashing and equal-but-distinct keys

The learner proposes using Object's identity-based hash to keep it stable. This can be consistent when equality is also identity-based. Changing only the hash while retaining accountId-based equality does not guarantee that equal objects have equal hashes. Identity hashes are not guaranteed unique. See the [Object contract](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html).

For two distinct AccountKey objects with accountId 101, accountId-based equality, and explicitly different identity hashes, the learner correctly predicts that get(k2) returns null after put(k1, ACTIVE). They correctly identify hash screening before equality, but assume different hashes necessarily imply different buckets.

Correction: bucket selection compresses the hash into a limited index range. With 16 buckets, illustrative hash values 1 and 17 (unchanged by OpenJDK 17 spreading) both yield index 1. Even in the same bucket, the stored hash must match the lookup hash before the candidate can match by identity/equals. This is a source-based explanation, not a newly executed Java experiment. Identity hashes are not assumed to actually be 1 and 17.

Recap: hash stability within one object is insufficient when separate objects can be logically equal; their hashes must agree too. Bucket collisions do not bypass the stored-hash check.

## Requested detour: bit masking and the lookup flow

The learner asked how hashes 1 and 17 both select bucket 1, then where hashCode() and equals() enter the process. The explanation below is instructor-taught. The learner subsequently applied the identity/equality matching steps correctly in the follow-up below; binary masking has not been separately assessed.

With 16 buckets, valid indices are 0 through 15. OpenJDK 17 uses `(capacity - 1) & spreadHash`. Its allocated table length is a power of two. Integer `&` is bitwise AND: an output bit is 1 only when both input bits are 1. Only five bits are shown here; omitted leading bits are zero.

```text
  1 = 00001          17 = 10001
 15 = 01111          15 = 01111
      -----               -----
  & = 00001 = 1        & = 00001 = 1
```

The mask 15 retains the lowest four bits and clears higher bits. Both hashes end in 0001, so they select the same bucket. For these nonnegative values, this also equals the remainder on division by 16. This power-of-two mask rule is not a general replacement for modulo with any capacity.

For a non-null key, HashMap calls key.hashCode(), then computes `h ^ (h >>> 16)` to spread bits. The small positive values 1 and 17 remain unchanged. It uses this spread hash both to select the bucket and as stored node metadata.

On put, matching an existing key replaces its value; otherwise a new entry is stored. On get, it recomputes the search key's spread hash, selects a bucket, and looks for a candidate with a matching stored hash and either the same key reference or a successful searchKey.equals(storedKey) comparison. A different stored hash rejects that candidate without equals; matching references also avoid an equals call. Thus equal hashes do not alone establish equal keys. These steps describe the relevant matching conditions without detailing tree-bin navigation.

Source: [OpenJDK 17 HashMap](https://github.com/openjdk/jdk17u/blob/master/src/java.base/share/classes/java/util/HashMap.java). This was a source-checked worked explanation, not a new Java experiment.

## Equal hashes, unequal keys: resolved follow-up

For distinct keys k1 and k2 that both return 17 from hashCode(), with k2.equals(k1) false, a map containing only k1 -> ACTIVE returns null for get(k2). The learner correctly explains that neither key-reference identity nor equals succeeds. Matching hashes allow the candidate to be considered; they do not establish a key match. After the hash match, either reference identity OR equals can establish a match; both need not be true.

This is correct application immediately after instruction, not independent mastery. No additional Java experiment was executed.

## Stable accountId design: core fix reached

The learner proposes removing the setter and setting the key only through the constructor. This addresses the original mutation problem if the primitive accountId has no other write path. Removing a setter alone does not prevent another class method from assigning the field.

Instructor refinement: declare `private final int accountId;` and assign it in the constructor. Private limits direct access; final prevents reassignment after initialization in ordinary Java code. Keep the existing accountId-based equals/hashCode definitions consistent. See [JLS 17 final variables](https://docs.oracle.com/javase/specs/jls/se17/html/jls-4.html#jls-4.12.4).

Precision: hashCode returns a stable integer for this fixed ID; equals returns a boolean for a comparison with another object. For two such keys, the same ID means equals true and equal hash codes. The learner's phrase "continue to return same value" is interpreted as stability, not as a claim that the two methods return the same type or that equals is always true.

Interview recap of the resolved core: inspect fields used by equals/hashCode for changes after insertion. A node retains its insertion-time hash and key reference; changing the ID can make lookup miss the still-present entry. Keep the key's ID stable from construction, with hashing consistent with value equality. Constructor-only initialization was learner-proposed; the private-final enforcement was instructor-taught. No new implementation or runtime experiment was performed.

## Non-key-field mutation: resolved follow-up

The learner correctly predicts that changing status from OPEN to FROZEN leaves get(key) returning ACTIVE, because equals/hashCode depend only on the unchanged accountId. Their wording was "2 menthods are unchanged". Precision: the relevant inputs are unchanged; method implementations also stayed unchanged in the original broken example, where accountId changed. In the same-reference lookup, the stored hash matches and reference identity establishes the match without calling equals.

The general rule is stability of the data used for hashing and equality while a key is stored. An unrelated mutable field does not by itself break this lookup. This does not establish general thread safety or recommend mutable domain entities as keys.

## Interview-ready recap

I would inspect a missing HashMap key's equals/hashCode implementation and whether their input fields changed after insertion. OpenJDK stores the insertion-time spread hash and the key reference. Mutating the account ID can change the lookup hash while the entry retains its old hash, so an entry can remain iterable but no longer be found through get. Equal keys must have equal hashes; sharing a bucket or hash does not establish equality. In this example I would set the primitive account ID only during construction and make it private final, while preserving accountId-based equals/hashCode. Mutating status is harmless to lookup when neither method uses it.

## Assessment and next retrieval

- Correctness: core fix reached; equal-hash unequal-key and non-key-field outcomes correctly explained after teaching.
- Reasoning: earlier hash, bucket, and self-equality confusion required an executed instructor demonstration and explanations. Constructor-only initialization was learner-proposed; final-field enforcement was taught.
- Edge cases: supported application demonstrated; learner-generated corner cases and independent transfer remain unassessed.
- Communication: predictions are concise; refine "methods unchanged" to "hash/equality inputs unchanged".
- Overall: 2/4, H3, learning. No independent pass or mastery. No study duration invented.
- Retrieval on 2026-11-11: explain the lookup mechanism and stable-key design in 60-120 seconds without notes, then reason through a fresh variant. Revisit the distinction between hash and bucket; binary-mask calculation has not been independently assessed. Mutable referenced fields and defensive copying remain future coverage, not demonstrated knowledge.

The [lesson log](../sessions/2026-11-10-lesson-02.md) preserves responses and teaching support. Next diagnostic: CON-01, initially unassessed.
