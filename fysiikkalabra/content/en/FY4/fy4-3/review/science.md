VERDICT: PASS
CONTENT-HASH: 1c324da62fb38c8b

## Blocking
None. (The packet header says 9b120b28b5a1ba41; `reviews.py hash` gave 1c324da62fb38c8b at start and end. The packet text matches the current lesson.)

## Polish
1. Figure systeemit, right panel: the arrow for G_A+G_B is the same length (108 px) as G_A alone in the left panel. The two panels are separate diagrams, but a reader may compare them, and the combined weight must be larger. Draw it longer, or say the panels are not to the same scale. N_A+N_B has the same issue. (class C)
2. systeemit aria-label says "support force"; the lesson everywhere else says "normal force". Use one term.
3. Section "Two ways to choose the system": "Only now do the forces belong to the same system" is vague. Better: "Only when A and B are one system can the two forces be added".
4. Siirto solution: the text calls the air resistance F_a, but the formula uses F_d. The voimakuvio block uses the label F_i (Finnish). Check that it renders as F_d in the English lesson.

## Checked
- New subsection and systeemit: the system A alone has F_BA as an external force, drawn on A, pointing left from B on the right. The system A+B has the pair internal and not drawn, and F_AB+F_BA = 0 as a vector sum of forces on different bodies. That is valid only for the system, and the text says so. With friction neglected, the weights and normal forces are external and equal in the vertical direction. Arrow geometry in the SVG matches the text: F_BA tip at A's right face, G_A and N_A equal (108 px). Consistent with the earlier "not drawn in the diagram of the same object" and the third-law formula. Guardrails 1-3 and 6: no error.
- Sim and model values recomputed: G = 98.1 N. Slide distance v²m/(2F) = 1.125, 2.25 and 4.5 m, times 0.75, 1.5 and 3.0 s. Push force m·v0²/(2d)+F_μ gives 110 N on wood. Frictionless: 12 m in 4.0 s at 3.0 m/s. Experiment 1: v0 locked at 3.0 and surface varied, so the setup isolates the variable. simState has s, tl and vl. Numeric answer F·s = 45 N·m gives 9.0 m. The mistakes (2.25, 4.5, 5.625) are plausible and their feedback is right.
- Predictions: each has exactly one correct option and the feedback physics is right. Collision data recomputed: peak about 4.0 N at 0.10 s, 1.37 and 1.31 N at 0.07 s, contact 0.05-0.15 s. Equal within scatter.
- Worked example: F_d = 2F_1 = 96 kN. Third law (thrust) and first law correctly separated. Speed unused. Reasonableness remark is correct.
- Siirto: 420+260 = 680 N. Third law applied to the hook correct. Check-1 (conveyor, no friction at constant velocity), check-2 (reaction of N) and the lamp task are correct. Exit ticket correct. Horse-cart feedback correct.
- Curling and car figures: forces and directions correct, no forward force drawn, velocity not drawn as a force.
