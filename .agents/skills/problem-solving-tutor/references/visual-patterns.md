# Select a visual that helps reasoning

Use only the pattern relevant to the active problem. The learning goal is a prediction or explanation, not a polished picture. Start with a few labeled elements and add detail as the learner's model improves.

| Problem | Useful representation | What to ask the learner |
|---|---|---|
| Threads or database transactions | Two lanes and numbered operations; distinguish local observations from stored state | Which operation could happen next, and what would it observe? |
| Object references and collections | References pointing to objects or buckets | Which object changes, and which references can observe it? |
| Spring interception | Caller, proxy, target, and resource boundaries | Which boundary does this invocation actually cross? |
| SQL joins or aggregation | Tiny input tables and a partial output; label duplicate and NULL rows | Which row appears next, and why? |
| An index or query plan | Query predicates beside a small ordered-key sketch | Which part of the data must still be examined? |
| Kafka processing | Event identity, partition order, consumer position, and external effects on separate tracks | What has completed at the marked crash point? |
| Payment lifecycle | State diagram with explicit transition labels | Is this transition permitted under the stated assumptions? |
| DSA | A trace table of indices, data structure contents, and the invariant | What must remain true after the next step? |
| System design | One request flow with ownership and failure boundaries | Which component knows enough to decide after this failure? |

## Progressive disclosure

1. Draw the initial state or one worked analogous case.
2. Mark one unresolved operation or boundary.
3. Ask for a prediction and wait.
4. Reveal or measure that step, explain discrepancies, and update the drawing.
5. Change one input, ordering, or failure point after the basic model is secure.

If a learner lacks the underlying concept, provide the explanation before step 2. Do not use a partly blank diagram to disguise an unsupported guessing exercise.

## Presentation and limits

Label actors and stored state clearly. Make arrow direction meaningful; specify whether it represents a call, response, dependency, or state change. Use text labels as well as color. Keep code readable and diagrams small enough for chat. Pair every diagram with a plain-language explanation or trace fallback.

Treat a sequence diagram as one possible schedule unless the constraints establish that it is mandatory. A diagram is not evidence that a program or database behaves that way. Likewise, a successful demonstration does not prove all concurrent schedules are safe.

Do not turn syntax examples from a diagram library into security, database-modeling, or architecture recommendations. Verify technical semantics separately. Do not install renderers, publish diagrams, or add network dependencies merely because an upstream reference shows those options.
