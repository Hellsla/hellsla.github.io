VERDICT: FAIL
CONTENT-HASH: 2d365219ba2e0aa3

## Blocking
- content/fi/FY1/fy1-3/exercises/solutions.md:135 (L1-07, A) — "Tulos 5,4283 cm olisi väärin": the unrounded mean is 27,14 cm / 5 = 5,428 cm exactly (line 134 says so too), so 5,4283 is an invented digit. — Fix: "Tulos 5,428 cm olisi liian tarkka, koska se antaisi ymmärtää tietävän leveyden tuhannesosien tarkkuudella, vaikka virhe-arvio on sadasosia."

## Polish
- content/fi/FY1/fy1-3/exercises/solutions.md:185 (L3-04) — "if no cause were found" ends with "mittaus toistettaisiin". It should also say that the result stays in the data (mean with it 2,48 s) and the deviation is reported, following the outlier guardrail. At line 186, "joten se on karkea virhe" rests on the size alone; base it on the recorded cause.
- content/fi/FY1/fy1-3/exercises/solutions.md:164–165 (L2-06) — "kaksi merkitsevää numeroa kuten tuloksissa" gives the wrong reason: the results have three figures. The hundredths follow from ΔV_A = 0,15 ml. Also, "joten poikkeama ei ole satunnaista" is too certain: say *todennäköisesti* and base it on 0,94 ml ≫ 0,15 ml.
- content/fi/FY1/fy1-3/exercises/exercises.json:186 (L2-06) — a graduated pipette with five times the scatter of a measuring cylinder is the wrong way round for real glassware. Swap the instruments, or use two measuring cylinders.
- content/fi/FY1/fy1-3/exercises/solutions.md:155 (L2-05) — "noin 33 kierrosta minuutissa … sopii": the standard 33⅓ rpm gives 1,800 s, just outside 1,820 ± 0,015 s. Either say "noin 1,8 s" without a claim of agreement, or note that the difference could be a systematic error (a slow turntable or the timing).

## Checked
- Recomputed all 19 numeric answers in one script: all agree (e.g. L2-05 1,820 ± 0,015 s; L2-06 +0,94 ml, ΔA 0,15, ΔB 0,55; L2-07 13,3 → 14).
- L1-06: exactly one correct option (zero offset). The distractors (random reaction time, varying parallax, mis-recorded value) and their feedback are right, and the terms are those of the guardrails.
- L1-08: the guardrail's scale-reading wording is used, with the total-uncertainty caveat.
- L2-05: ΔT/10 is right for an exact count, and the two-figure Δ rule is applied.
- L2-07: the task states the assumption (0,2 s independent of the duration); N is rounded up with a reason.
- L3-05: non-overlapping intervals are judged as a difference larger than the estimated uncertainties, and "ei todista kummankaan vääräksi" is said.
- Old 12: unchanged apart from the typography.
