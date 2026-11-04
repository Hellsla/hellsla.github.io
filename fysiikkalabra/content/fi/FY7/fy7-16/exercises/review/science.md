VERDICT: FAIL
CONTENT-HASH: 5482f5dd781ef9bd

## Blocking
- content/fi/FY7/fy7-16/exercises/solutions.md:154 (L2-05 Vastaus) with exercises.json fy7-16-L2-05 tolerance 0.04 — A (assessment): the solution says a graph reading of "12–13 mm on yhtä hyvä", but the box accepts only 12,34–13,37 mm, so 12 mm is marked wrong. A smooth (convex) curve also crosses 50 % slightly before the 12,86 mm chord value. — Fix: either raise the tolerance to 0.07 (≈ 12,0–13,8 mm), or change the text to "noin 12,5–13 mm".

## Polish
- solutions.md:197 (L3-05) and task text — the model P = e₀²/(2R) says that a lower R heats more. The lesson says aluminium and copper (the lowest R) heat poorly; that is because for them the neglected eddy-current field dominates (here ωL ≈ 0,07 Ω, comparable to R). Add to the c) model answer: "Hyvin johtavassa pohjassa (alumiini, kupari) pyörrevirran oma kenttä kumoaa suuren osan vuosta, joten malli ei päde niille; teräksen ferromagnetismi taas lisää lämpenemistä."
- L1-06 — the plan asks about glass or aluminium versus steel; only glass is covered. That is acceptable, but aluminium could appear in a distractor.
- L3-05 a) overlaps existing L3-02 (same loop model); b) and c) justify it.

## Checked
- One script recomputed all 19 numeric answers: new ones 0,5036 mW; 15,05 km; 12,857 mm; A = 2,147/3,885/6,108/7,925/10,049 dB, origin-fit slope 0,2003 dB/km (point ratios 0,194–0,215); 1,0 % (80 % ↔ 0,97 dB); Φ_min 0,1061 µWb → 13,28 mm (130 kHz: 15,0 mm; 20 turns ×1,33 vs 1,30); e₀ 14,39 V, P 2,59/2,07/1,29 kW, f_C 42,43 kHz. All match exercises.json and answers.py (ran it).
- L1-06 MC: exactly one correct option, and the feedback on each distractor is right (field passes glass, Lenz gives direction, not cancellation).
- L2-06: the line through the origin is justified physically. The slope is read from the fitted line. The fit sentence is in the guardrail's wording.
- L2-07: dB vs percent explained correctly, the student's 80 % checked against ~1 dB.
- L3-04: e₀ = N·2πf·Φ₀ with flux held fixed, as stated; c) reasoning (slower change, more turns) correct.
- Notation (A, a, L, P₀, e₀, Φ₀) matches the lesson; the counts are 8/7/5 and the plan is followed; every new solution is complete and symbolic first.
- 1280 px render of the L3 solutions checked: no overflow.
