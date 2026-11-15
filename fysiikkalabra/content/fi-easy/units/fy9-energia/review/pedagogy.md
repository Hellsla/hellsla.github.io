VERDICT: PASS
CONTENT-HASH: 3c8c8618ecbaa2da
Round 3: delta against the version round 2 reviewed (one sentence in s7 d).

## Blocking
- (none)

## Polish
- C `sovella/tasks.json` s7 d: "suhteellisesti" is still a hard word for plain language; "jäi prosentteina eniten jälkeen ilmoitetusta toimintamatkasta" is easier (round 2, partly done: "jälkeen" added). The task text calls the source "tulossivu"; "raportti" is a second name for it.
- A (round 2) s7 c, criterion 4: could mirror the solution: "Siksi jokainen kilometri vaatii akusta enemmän energiaa, ja toimintamatka lyhenee."
- B (round 2, outside this delta) `sovella/solutions.md` s4: the inline formula for $T$ is wider than a 360 px screen; break it into an `aligned` display.

## Checked
- `git diff c502cb9e26 -- content/*/units/fy9-energia`: three files, one line each (`sovella/tasks.json` line 818); nothing else changed outside `review/`.
- s7 d, new sentence: "Testin raportin mukaan pisimmälle ajaneen auton toimintamatka jäi suhteellisesti eniten jälkeen ilmoitetusta." The claim is attributed to the test's own report and no longer rests on the table's three cars; it agrees with part a (Lucid Air 45,8 %) and with the solution of d.
- The two following sentences ("Tästä ei voi päätellä ...", "Selitä aineiston avulla, miksi ei.") are untouched; the part stays three short sentences, situation first, instruction last.
- Both criteria of d are untouched and assess what the part asks; nothing of the answer is disclosed.
- Hash identical at start and end.
