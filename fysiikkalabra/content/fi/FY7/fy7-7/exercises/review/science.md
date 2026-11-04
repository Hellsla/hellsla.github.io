VERDICT: PASS
CONTENT-HASH: bd0c326a9688e130

## Blocking

## Polish
- exercises.json:30 (L1-04) — 1500 r/min is a typical steam-turbine (four-pole) speed; hydro generators usually turn far slower. Call it "voimalaitoksen" or "lämpövoimalan generaattori", or use a hydro speed such as 150 r/min.
- exercises.json:97 / solutions.md:112 (L3-03) — "generaattorin jännite ∝ f" holds for the induced (no-load) voltage; adding "tyhjäkäynnissä" or "käämiin indusoituvan jännitteen" in the task would state the condition (C at this level).
- solutions.md:82 (L2-04) — the 2-significant-figure reason ("data has three figures and the result is an estimate") is weak; the real reason is that the year-end capacity is not the year's mean capacity, as the Järkevyys already says.

## Checked
- All 12 answers recomputed from the task text with own formulas: identical to answers.py and exercises.json (e.g. L2-02 0,1273 T, L2-04 26,97 %, L3-03 414 V).
- Figure fy7-7/trace: peak 12 V on a 3 V grid line, period 40 ms on a 10 ms grid; description gives the same values and not the answer; solution reads it correctly.
- Effective/peak used the right way round in every task (L1-02, L1-03, L2-03, L3-02); L1-05 resistor in phase so P = UI.
- L3-01 e = e₀ sin 30° = 10,0 V with the zero at the max-flux position, as the lesson defines.
- L3-02 P = U₀²/2R = 20 W, peak power 40 W check right.
- Units, conversions (cm² → m², r/min → Hz, TWh/h → W), symbolic solving before substitution, tolerances fit the significant figures.
- Every solution complete with a real reasonableness check; notation matches the lesson.
