# Java reasoning experiments

## MutableKeyProbe

Instructor-authored demonstration after the learner predicted the result; it is not learner-written code or an independently completed exercise.

Run from the repository root with Java 17 or newer:

```powershell
java practice/java/MutableKeyProbe.java
```

Executed on 2026-11-10 with Oracle Java / HotSpot 17.0.9. Observed output:

```text
Before mutation: hash=101, get=ACTIVE
After mutation: hash=202
key.equals(key)=true
Lookup result=null
equals calls during lookup=0
Map size=1
Iteration sees accountId=202, value=ACTIVE
```

This separates a failed lookup from an entry being removed, and shows that `equals()` was not called during the failed lookup. The counter is reset after the explicit self-equality call, so that call is not included in the lookup count.

For this map's 16-bucket OpenJDK 17 layout, the implementation's spread-and-mask calculation places hashes 101 and 202 at indices 5 and 10. These indices are derived from the source algorithm and the example's allocation; the probe does not inspect private map storage. The stored entry retains insertion-time hash metadata while the key reference still points to the mutated object.

References: [OpenJDK 17 HashMap implementation](https://github.com/openjdk/jdk17u/blob/master/src/java.base/share/classes/java/util/HashMap.java), [Object equality contract](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), and [Map mutable-key warning](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html).

Changing a key in a way that affects equality while it is in a map is outside the Map interface's specified behavior. This observed result explains the selected implementation and example; it is not a portable guarantee that every unsafe mutation on every map returns null. The learner's stable-key redesign remains open.
