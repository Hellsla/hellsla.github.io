VERDICT: PASS
CONTENT-HASH: 94a25355702d3770

## Blocking

## Polish
- inquiry.json solution diagrams with `pinta` — the floor or ice is hatched inside the voimakuvio, but lesson.md:166 and the suunnat caption say no surfaces are drawn. This comes from the tool (fbdspec), not the lesson; the text or the tool should change so they agree.
- lesson.md:166 — "Liikkeen ratkaisee … kokonaisvoima" is safer as "Liikkeen muutoksen".
- lesson.md:445 — "vinossa työnnössä suurempi": add "alaspäin" (an upward slanted push lowers N).
- sim.js:59 — v is still capped silently at 12 m/s while the readout shows a > 0 (carried over).
- lesson.md:5 / inquiry.json:18 — the hero is on snow while the inquiry is on ice, and the handle "osoittaa vinosti alaspäin" (carried over; the physics is unaffected).

## Checked
- Round-1 fix: exp-2 now says "kun kulma α > 0°", which agrees with N = G at the student's α = 0° row.
- The sled: ice throughout the inquiry, and friction neglected with that stated. Pull gives N = G − F sin α, push N = G + F sin α, consistently in sim.js, the calc box, sim-spec and the feedback.
- 50 N = 196 − 146 from whole-newton readouts (good to about 1 N), confirmed by F sin 30°. The mistakes (146, 87) and the 3 % tolerance are right.
- One script recomputed the worked example, pred-2, exp-1, aineisto, siirto, check-2, check-3 and every mistake value. All agree with lesson-answers.py and the text.
- Lesson figures measured from their SVG coordinates are on one linear scale, and their sums close (N + T_y = G; F_noste = G + N; slope friction = G sin 25°). The four inquiry diagrams, rendered, are to scale with correct directions, and a and v are drawn off the body.
- Option figures: virhe's only error is the forward F. hissi-a is right, and b, c and d each have one error with correct feedback. malli-tyonto matches the check-3 model (N = 147,7 N, F_μ = 52 N).
- Sim: one fixed scale, and 150 sin 80° = 148 N < 196 N. simState has N, Fx and a. exp-1 locks tapa, F and m and varies α.
- Exactly one option is correct in every choice item; the exit ticket is correct.
- "FAIL sims" does not reproduce: test_sims.py fy4-5 passes for fi, en and fi-easy.
- The hash was the same at start and end.
