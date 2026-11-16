VERDICT: PASS
CONTENT-HASH: 300bb0101bde0453
Round 3: delta against the version round 2 reviewed (one sentence in s7 d).

## Blocking
- (none)

## Polish
- C, `sovella/tasks.json` s7 d: the task text calls the source "testin tulossivu"; "Testin raportin mukaan" names the same source with a new word. "Testin tulossivun mukaan" would keep one name. Understandable as it is.
- C (round 2), s7 c, criterion 4: could end as the solution does, "jokainen kilometri vaatii akusta enemmän energiaa".
- C (round 1), s7 a solution: the sentence about three significant figures after whole per cents.

## Checked
- `git diff c502cb9e26 -- content/*/units/fy9-energia`: three files, one line each (`sovella/tasks.json` line 818); nothing else changed outside `review/`.
- s7 d, new sentence: "Testin raportin mukaan pisimmälle ajaneen auton toimintamatka jäi suhteellisesti eniten jälkeen ilmoitetusta." The claim is now attributed to the test's own report, so it no longer rests on the three cars of the task's table; it agrees with part a's result (Lucid Air 45,8 %, the largest of the three) and with the solution of d.
- "jäi ... jälkeen ilmoitetusta" is the usual idiom (my round-2 Polish, now done).
- Both criteria of d (use of the temperature data; the cars did not drive in the same conditions) are untouched and still assess exactly what the part asks. The attribution discloses nothing of the answer: the student must still find the reason in the source.
- Situation first, instruction last; one sentence each.
- Hash identical at start and end.
