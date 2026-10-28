VERDICT: PASS
CONTENT-HASH: a3a64a7608c7dd0a
## Blocking

## Polish
- exercises.json L2-01 "300 N:n", L3-01 "120 N:n", L2-04/L2-02 "90 sekunnin", L3-02 "12 kertaa" — the N values stay plain while neighbouring m, J, kW are LaTeX; convert N (`$300\,\text{N}$:n`) for one number style.
- solutions.md L3-03 Periaate — "ideaalikaasussa vuorovaikutusten energia on merkityksetön" is correct but the new sentence is long; split after "liike-energia on sama." for readability.
## Checked
- Delta judged in context: the text edits are unit-to-LaTeX conversions with correct Finnish case endings (`$0{,}20\,\text{m}$:n`, `$250\,\text{W}$:n teholla, `$5{,}0\,\text{kg}$:n`).
- L3-03 now states its ideal-gas premise in the task, which removes the earlier hidden assumption; "ideaalikaasu" is defined inline in the same sentence.
- Answers re-derived: L1 570 J, -8,4 kJ, 250 J, -500 J, -70 J; L2 -15 J, 160 kJ, 800 J, 40 s; L3 -18 J, 1,7 m (1000/(12·5,0·9,81)), 310 J.
- Levels 5/4/3; none repeats the lesson example (compression with heat loss); everyday contexts; situation first, question last.
- Solutions keep all seven steps; reasonableness checks now consistently use LaTeX units.
- Round 2: re-check of round-1 Blocking items against the fix diff. None were open (PASS). fy3-5-L3-01 now states "ilmaa voi pitää ideaalikaasuna" in the task, so the first Polish item (premise missing from the task) is solved; the term is not defined there (L3-03 defines it inline), a minor remainder. Answer -18 J and the solution are unchanged and consistent.
