VERDICT: FAIL
CONTENT-HASH: e4ffabd1fd9d9a25

## Blocking
- lesson.md:535 (figure `kone`, figures.py:255) — **A** (drawing rule). The drag arrow $\overline{F}_\text{v}$ runs 96 units left from x = 381. It crosses the divider at x = 300 and ends at x = 285, beside the nose of the pictured airliner (276, 176), with its label over that nose. This mixes the force diagram into the tilannekuva, so the arrow reads as a force drawn on the pictured plane (docs/force-diagrams.md, Representations). Fix: keep the diagram right of x = 300, e.g. `FBD(f, 0.8, …)` with `cx = 470, w = 110`. The drag tip then lands at about x = 338, and the lengths stay in proportion.

## Polish
- figures.py:252 — Lift is labelled $\overline{F}_\text{noste}$, the symbol docs/force-diagrams.md reserves for buoyancy. The exercises also use "noste" for buoyancy. Use a separate symbol, e.g. $\overline{F}_\text{nosto}$.
- sim.js:19 — The comment says "600 x 720", but the code sets H = 740.

## Checked
- The round-2 sim change is layout only. The physics code and `simState` are unchanged. A run at 390 px gives mat s = 1,125 m and t = 0,75 s, and its force diagram is right in each phase: during the push F, F_μ, G and N; while sliding only G, N and F_μ; one scale throughout. Velocity is drawn blue and off the body.
- tests-weakened: the 600×400 assertion now applies only to the wide layout. This is a layout constraint; no physics assertion is affected.
- Recomputed in one script: push forces 130/110/100/90 N; slide distances 1,125/2,25/4,5 m and times 0,75/1,5/3,0 s; frictionless 12 m in 4,0 s; exp-1 9,0 m; worked example 96 kN; siirto 680 N; collision data mirror at ±4,0 N.
- Worked example: thrust by the third law, then $2F_1 - F_\text{v} = 0$ by the first law; lift balances weight. It is solved symbolically first with 2 significant figures, and the figure's arrow lengths balance.
- Definitions agree across theory, summary, feedback, exit ticket and sim boxes.
- Every choice item has exactly one correct option, and every distractor's feedback is right.
- Force diagrams checked: curling, skaters (third-law pair on separate diagrams), car, lamp model and sim. Each uses a rectangle body; G is drawn from the centre and N from the contact surface; friction starts at a corner; no point particles.
- Scope stays within FY4.
