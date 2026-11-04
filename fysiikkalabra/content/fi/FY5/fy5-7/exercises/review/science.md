VERDICT: PASS
CONTENT-HASH: adeddfca1934989d

## Blocking

## Polish
- fy5-7/exercises/solutions.md:194 (L3-05) — the rounding reason "kolme merkitsevää numeroa kuten ääriarvoissa" ignores the really limiting datum T = 1,6 s (read from a 0,2 s table step), and the solution's own c) shows that T = 1,62 s moves the prediction by 1,1 cm — give 44 cm (two figures, limited by T and by the extrapolation) or justify three; the 2 % tolerance accepts both.
- fy5-7/exercises/solutions.md:177 (L3-04) — "levossa kuudes piikki 4,96 s": with beat 0 at 0 s this is the seventh R-peak (lyönti 6) — write "lyönti 6" or "kuudennen lyöntivälin loppu".
- fy5-7/exercises/solutions.md:131 (L2-06) — the part b) answer (half range, ±0,03 s, why ten swings) sits under Järkevyys; move it to Vastaus so the b) model answer is where students look (wording of the scatter estimate already follows the guardrails: "hajonnan arvio", not uncertainty of the mean).
- fy5-7/exercises/exercises.json:362 (L3-05) — kind "graph" while the task has a table and no figure; either drop "graph" or ask for the (t, d) plot in a).
- docs/exercise-bank/FY5.md plan, level 2 "vaimenevan värähtelyn amplitudit" is not among the new tasks; fine as damping is not taught in this chapter's brief, but update the plan line so plan and set agree.

## Checked
- Recomputed all 8 new answers in one script from the task data: L1-07 25 s, L2-05 1,639 Hz, L2-06 1,51 s, L2-07 1,342 Hz, L3-04 79,06 %, L3-05 44,24 cm — all equal answers.py and exercises.json.
- L2-05 intervals 0,59…0,62 s, five periods between peaks 1 and 6; L2-07 alternating directions, two periods 0,00→1,49 s.
- L3-04 beat intervals 0,81…0,85 s and 0,45…0,48 s; pulses 72,6 and 130 1/min realistic; "likimain tasaisesti" stated.
- L3-05 table matches 40,0 + 6,0 sin(2πt/1,6 s) within ±0,14 cm (noisy, not exact); c) check T = 1,62 s → 43,1 cm correct.
- L1-06 and L1-08: exactly one correct option, every distractor's feedback right.
- Models and symbols (f = 1/T, x = A sin(2πt/T), D + A sin) as in the lesson; radian mode stated.
- Scope: period, frequency, amplitude, sine fit only; no ω, no later physics.
- No duplicate of an existing task; levels plausible (L3-04 is at the light end of level 3).
- Hash identical at start and end.
