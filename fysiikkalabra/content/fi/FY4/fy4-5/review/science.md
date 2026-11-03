VERDICT: PASS
CONTENT-HASH: df3ef99aaf2cf768

## Blocking

## Polish
- sim.js:57 — v is still capped silently at 12 m/s while the readout keeps showing a > 0 (carried over). Either say in the sim box that the model stops speeding up at 12 m/s, or stop the run at the cap.
- lesson.md (Ydinajatus) — "Liikkeen ratkaisee … kokonaisvoima" would be safer as "Liikkeen muutoksen ratkaisee" (carried over).
- lesson.md (Yleinen virhekäsitys) — "vinossa työnnössä suurempi": add "alaspäin", because a push slanted upward lowers N (carried over).
- inquiry.json solution diagrams with `pinta` — the surface is hatched inside the voimakuvio, but the text says no surfaces are drawn there. This comes from the tool, not the lesson (carried over).
- lesson.md hero / inquiry.json hook — the hero is set on snow while the inquiry is set on ice. The physics is unaffected (carried over).

## Checked
- Reason for this review: sim.js changed only its scale (S 0.32 → 0.34), the rectangle's size and position, and the label size. The physics (forces(), simState, adapter) is unchanged.
- At the new scale the extreme cases fit the canvas: push with F = 150 N, α = 80°, m = 40 kg gives N = 540 N, which is 184 px and so the top of the arrow at y ≈ 61. G = 392 N reaches y ≈ 361. 150 sin 80° = 148 N < 196 N, so the sled never leaves the ice.
- The sim screenshot at 1280 px matches the model: G = 196 N, N = 146 N, F_x = 87 N, |F_y| = 50 N and a = 4,33 m/s², and the N arrow is shorter than the G arrow.
- One script recomputed the worked example, pred-1, pred-2, exp-1 at 0°, 30° and 60°, exp-2, aineisto, siirto, check-2, check-3 and every mistake value. All agree with lesson-answers.py and the text.
- The esimerkki SVG is to scale at 1,15 px/N for G, N, T, F_μ, T_x and T_y, and T is drawn at 35,1°. In the tilanne figure N + T_y = G (84 + 29 = 113 px), with T drawn at 30°.
- Option figures (checked in figures.py and the renders): hissi-a has N = 1,3 G and is right. b (N = G), c (v drawn as a red force) and d (N < G) each carry one error, and their feedback names it correctly. virhe's only error is the forward F.
- Exactly one option is correct in every choice item. The distractor feedback, the explain model answers and the exit ticket agree with the theory.
- exp-1 locks tapa, F and m and varies α. simState gives N, Fx and a at those settings.
- "FAIL sims" does not reproduce: scripts/test_sims.py fy4-5 passes for fi, en and fi-easy.
- The hash was the same at the start and the end.
