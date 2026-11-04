VERDICT: FAIL
CONTENT-HASH: 5de57c6f45f43e68

## Blocking
- [Major] solutions.md fy1-6-L1-08, Vastaus (capture open-exercises-1280-8) — the answer line reads "35 km/h sekunnissa, kolme merkitsevää numeroa kuten luvussa 9,81", but 35 has two significant figures (and the chain above ends in 35,316) — the stated rounding contradicts the stated answer, and the checker's reference value is 35,316 — fix: "$35{,}3\,\text{km/h}$ sekunnissa, kolme merkitsevää numeroa kuten luvussa $9{,}81$." and set the expected answer shown in the task card to 35,3 km/h (answers.py/exercises.json answer 35.316 with its tolerance can stay).

## Polish
- [Minor] solutions.md fy1-6-L3-05, Vastaus — "käyttää kellon lukemaa $1{,}65\,\text{s}$ ajan pudotuksen alusta paikalla" is garbled — write "käyttää kellon lukemaa $1{,}65\,\text{s}$ ajaksi pudotuksen alusta".
- [Minor] exercises.json fy1-6-L3-05 text — the quotation uses straight " " around the student's calculation, while the other tasks use ” — use ”…” and move the full stop inside as elsewhere.
- [Minor] solutions.md fy1-6-L3-04, Sijoitus (open-exercises-L3-1280-5) — the long percent chain wraps with "· 100 %" dangling on the next line; put the chain in an aligned block, breaking at "=".
- [Minor] L2-05, L2-06, L3-04 — "Piirrä kuvaaja" tasks have no plotted example in the solution; optional.
- [Minor] solutions.md L2-05 — "kaksi merkitsevää numeroa" but the line shows "9,75" (three) in Sijoitus and "noin 9,3–10,2" in the range — optional: state "9,7" after the chain.

## Checked
- Captures opened (1280 px): open-exercises-1280-7, -8 (L1-07, L1-08), L2-1280-8, -9 (L2-06, L2-07), L3-1280-4 to -6 (L3-04, L3-05); no 360 px exercise capture exists.
- Source text of all eight new tasks and solutions read: maths in LaTeX with decimal comma, upright units, tables show the decimal comma, MC feedback and solutions open inside the cards without overflow.
- Not opened: L1-06 (MC) and L2-05 captures (judged from source).
- Science question for the science reviewer: L2-07 solution says t = 0,575 s gate times with a "pudotushetki tuntematon" — fine; no doubts.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
