VERDICT: PASS
CONTENT-HASH: 0bf68f3809480a6d

## Blocking
- (none)

## Polish
- (none)

## Checked
- Round-3 finding fixed (commit bf5de15e, the only content change): in the electromagnet figure (lesson.md:319–320, figures.py:146) the current arrow now points right, toward the battery's bottom (−) terminal. The nub, which marks +, is on top. The circuit runs from + up through the closed switch, into the top of the coil, down through the coil and back along the bottom lead to −, and the arrow agrees with that path. In the render (shots/fy7-3-fig-13-390.png) the arrowhead ends at the battery lead and I is centred under it. The open-switch panel has no current arrow, which is correct.
- One script with my own formulas, the coil field summed loop by loop rather than the closed form, printed beside lesson-answers.py. Every value matches. Sim on load: 1,232 mT, against 1,257 mT from the long-coil formula. Koe 1: 4,67/2,46/1,66/1,25 mT. Koe 2: 2,46/2,41/1,25 mT, and 0,363 mT 2 cm outside the end.
- Least-squares fit: A = 2,4651 mT/A, B₀ = 0,0352 mT, ΔA = 0,0121 mT/A. This gives μ₀ = 1,2326·10⁻⁶ Vs/(Am) with a relative uncertainty of 1,74 %. The finite-coil factor is 0,983, so the corrected value is 1,254. Mistake values 123 and 1233 match the slips they name.
- Worked example 12,57 mT and 251×. Etsi virhe 5,0·10⁻⁵ T against 5,03 mT. Siirto 0,2653 A, with mistakes 26,5 and 3,33. Check 2 1,5 mT, with mistakes 0,015 and 9,42. Exit ticket ×1. Wire graph 200/100/50 µT. Hook: a 3 A wire about 1 cm away turns the compass about 76° when Earth's horizontal field is about 15 µT, which fits "lähes poikittain".
- Directions:
  - wire-field top view: counterclockwise, with the compass N ends tangent.
  - Right-hand rule text and check 1: consistent with the wire-field figure.
  - coil-field: the • and × marks put N on the right.
  - coil-dims: B points to the right.
  - Sim: dir = 1 puts N on the right, and the field lines outside run from N to S.
  - Exit ticket 2: correct.
- Choice items: each has exactly one correct option, and every distractor's feedback is physically right.
- Conditions are stated where they are used: a long wire with other conductors far away, a long coil with air inside measured far from the ends, and about half the centre value at the ends. The sim states its limits (axis only, no iron, no Earth's field, its values are model values).
- Experiments: each locks everything but its varied parameter, and simState provides B and n.
- Scope: FY7 only, with no self-induction and no para- or diamagnetism.
- Hash recomputed at the start and at the end: unchanged.
