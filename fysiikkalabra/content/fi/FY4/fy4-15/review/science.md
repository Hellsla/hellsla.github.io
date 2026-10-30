VERDICT: PASS
CONTENT-HASH: f9b250176d97a909

## Blocking

## Polish
- lesson.md:426 (Esimerkki, Järkevyys) — "2,1 · 1,0 MW ≈ 2,2 MW": the chain as written gives 2,1 MW; the 2,2 comes from the unrounded 2,14 · 1,017. Fix: "≈ 2,14 · 1,02 MW ≈ 2,2 MW" or write "≈ 2,1 MW".
- lessons/FY4/fy4-15/lesson-answers.py:389 — the comment "(text: noin 130 MW)" refers to a sentence the lesson no longer has. Fix: drop it.
- lesson.md:300 — "Noin 13 m/s:n tuulesta alkaen teho pysyy 1650 kW:ssa" holds up to the curve's end (20 m/s, cut-out). C at this level; "tehokäyrän loppuun asti" would be exact.
- tehokayra figures — the plotted points at 13–20 m/s are every 1 m/s, the table lists 13, 16, 20; all 1650 kW, so no wrong number, only a mismatch in what is shown.

## Checked
- Round-1 Blocking (vesi-data max power vs mean flow) fixed: the 900 m³/s full-power flow is now stated and labelled calculated (η ≈ 0,90); recomputed 906 / 900 m³/s; siirto's check (354 m³/s, ≈ 55× less flow) now uses a number the student has seen.
- Round-1 Polish items done: check-3 steady wind, exit ticket 3 no longer V82-specific, pressure turbines noted (C).
- Recomputed every number of lesson.md, inquiry.json and the exit ticket in one script with my own formulas (8,92; 6,42 m³/s and its three mistakes; 800 kW and its two mistakes; 2,32 MW, 5,15 MW wind power; 8,0 / 7,9 MW/m; 235 kJ; (8:6)³ = 2,37; 55,6 MW and 5,6 MW). All agree with the text and lesson-answers.py.
- Derivations of ρQgh and ½ρAv³, their conditions (small KE in upper/lower water; constant η below rated power) and units are correct.
- Efficiency wording matches the guardrail; Betz 59 %, real turbines under half (V82 η 0,35–0,45 from the curve) correct.
- 8,9-fold rise explained by η 0,35 → 0,39: correct.
- Every choice item has exactly one correct option; each distractor's feedback is physically right.
- Explain criteria and model answers (johtopäätös, check-3) match the theory and state the conditions.
- Power-curve figures: to scale, model curve with η = 0,45 meets 1650 kW at 10,4 m/s.
- Hash identical at start and end.
