VERDICT: PASS
CONTENT-HASH: 99322ddd2a419363
Round 3: delta against the version round 2 reviewed (one sentence in s7 d).

## Blocking
- (none)

## Polish
- C: sovella/tasks.json s7 d: the task text calls the source "the results page of the test"; "the test report" is a second name for it. Understandable as it is.
- C (round 2): s7 c, criterion "Electricity": two lettered alternatives would read more easily.
- C (round 1): s7 a and e: "Tell also how": "say" reads more naturally.

## Checked
- `git diff c502cb9e26 -- content/*/units/fy9-energia`: three files, one line each (sovella/tasks.json line 818); nothing else changed outside `review/`.
- s7 d, new sentence: "According to the test report, the range of the car that drove the furthest fell short of its stated range by the largest percentage." The claim is attributed to the test's own report, so it no longer depends on the three cars of the task's table; it agrees with part a (Lucid Air 45.8 %, the largest of the three) and with the solution of d.
- The sentence is grammatical and unambiguous; "in the test" was dropped without loss, because the opening phrase carries it.
- Both criteria of d are untouched and still assess what the part asks; the attribution gives nothing of the answer away.
- Situation first, instruction last.
- Hash identical at start and end.
