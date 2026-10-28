VERDICT: PASS
CONTENT-HASH: d990e0039cdcf7a7

Round 2: re-check of round-1 Blocking items against the fix diff.

## Blocking

## Polish
- content/fi/FY3/fy3-9/lesson.md:124 — the isochoric pressure rise still gets no mechanism in the theory (pred-2's feedback has it: faster particles hit more often and harder); one clause would close the causal chain. The isochoric sentence relies on the condition stated in the sentence before it ("Kun kaasun määrä pysyy samana ja kaasu on harvaa"), which reads correctly.

## Checked
- Round-1 item 1 resolved: the condition "suljettu / kaasun määrä pysyy samana, harva kaasu" is now in the theory (:124), the formula section (:340) and the summary (:480), matching inquiry.json's contribution and prior; the extrapolation is marked "Jatke on mallin ennuste: todellinen kaasu tiivistyy nesteeksi ennen kuin 0 K saavutetaan" — physically right.
- Round-1 item 2 resolved: check-3's prompt now asks "Mitä muuta koejärjestelyssä on varmistettava?", so the fourth criterion (no leak, fixed amount of gas) asks only what the task asks; the model answer already covers it.
- The changed lines are grammatical Finnish, carry no numbers, and change no correct option, answer or feedback.
- The rest of the lesson is unchanged since my full review at bff7149aaf35caf4 (all numbers recomputed then: example 1,036 l, pred-1 200 kPa, pred-2 60,2 ml, ruisku 5430 vs 5040 kPa·ml, siirto 1,07 l, check-2 120 kPa, exit ticket 160 kPa and ×1,1).
- Simulation, experiments and figures unchanged and consistent with the model.
- Hash identical at start and end.
