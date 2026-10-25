VERDICT: PASS
CONTENT-HASH: 59049efa6569183c

## Blocking

## Polish
- lesson.md:36–37 — the hook (line 3) promises "kuudesosan", but the lesson never links that number to the table. Only line 48 says "noin kuudesosan" in passing. Fix: after the table add "Kuun g on noin kuudesosa Maan arvosta (1,62/9,81 ≈ 0,17), joten sama massa painaa Kuussa noin kuudesosan siitä, mitä Maassa."
- lesson.md:8 — the paragraph holds two ideas: spring proportionality, then calibration. Fix: start a new paragraph at "Asteikko kalibroidaan …".
- exercises.json fy3-1-L3-03 — lesson.md:48 already states the result ("Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta"), so the task reduces to one multiplication and is closer to level 2 than level 3. Fix: move it to a new place and turn it round, e.g. "Marsissa (g = 3,71 m/s²) Maassa kalibroitu vaaka näyttää 26 kg. Mikä on henkilön massa, ja mitä vaaka näyttää Maassa?" Update answers.py to give 68,7 kg (answer 69 kg) and the same value for the Earth reading.

## Checked
- The hash was the same at the start and at the end. The lint reports 0 errors and 0 warnings.
- Previous polish 1–5 were applied correctly: 100 g calibration bodies with the doubling argument (:8), s = vt (:8), the Moon's mass (:22), L1-02 wording, L1-04 turned round (7,5 N), and exit ticket 3 as a transfer item (15 N).
- The line 29 explanation of g in m/s² follows NOTES.md. 1 N = 1 kg·m/s² is stated and deferred to FY4. The unit N/kg appears nowhere, and weight is never given as the cause of a motion.
- "Putoamiskiihtyvyys" is a thematic link in FY1 (MAOL guide), so naming it is not a prerequisite gap.
- Each paragraph adds at most one new idea, apart from :8 (polish). The motivating question is one students actually ask.
- Scope: Newton's laws and vectors do not appear (FY4).
- Levels match the rubric: 5 one-formula L1 tasks, 4 L2 tasks and 3 L3 tasks (see polish for L3-03).
- No exercise repeats the worked example (120 kg robot, Earth and Mars).
- I recomputed every exercise and exit-ticket answer. All are correct to the data's significant figures.
- Exit ticket: q1 tests mass vs weight, q2 spring proportionality and q3 transfers the kilogram/newton distinction to a new item. All three test core ideas, not details.
