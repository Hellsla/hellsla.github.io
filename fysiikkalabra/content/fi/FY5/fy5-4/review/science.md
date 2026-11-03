VERDICT: PASS
CONTENT-HASH: 06bdeb9e2e13b206

## Blocking

## Polish
- assets/sims/fy5/fy5-4/sim.js:`advance()` — in the phone layout, the stop test checks the panel's top edge (`sy < 40`, 185 px from the centre) almost exactly at the asphalt's outer edge (`reuna`, 185.4 px at 366 px width). If a slide starts at a track angle that heads for the top edge, the car may stop right on the asphalt edge rather than visibly past it. The new tests start the slide at θ = 0 and so do not cover this. Optional fix: stop only on `out > R + 46U`, or clamp to the panel instead of stopping.

## Checked
- Round 1 blocking item (the slide claim) is fixed. I ported `advance()` to Python again and ran the new settings:
  - r = 50 m on dry asphalt in both the desktop layout and the phone layout (330–480 px).
  - At 25 m/s the heading turns 51–56° before the car leaves the track, with dmax 65–68 m against reuna 57–63 m.
  - At 30 m/s it turns 30–33°, with dmax 67–70 m.
  - At 20 m/s the car still stays on the asphalt (dmax 52.0 m). The texts no longer send the student there, and sim-spec.md and the sim.js header now say this.
  - pred-2 options, the johtopäätös model answer and sim-spec.md now say "loivemmin kuin rata, sitä suoremmin mitä suurempi nopeus", which matches the sim.
- `simState.reuna = r(R + halfW)/R` is the outer edge of the drawn asphalt in metres, and `dmax` is updated every sim step. The two new tests in tests/sims/fy5-4.json check what experiment 1 now asks for (25 and 30 m/s).
- The new explanation of why a_n grows with v² (a longer velocity arrow, and the same angle turned in less time) is correct at this level. The pred-1 feedback says the same.
- lesson.md:139 now states its conditions (level road, no air resistance). lesson.md:280 now handles the boundary correctly: N = 0 when v²/r = g, and the car leaves the road only when v²/r > g.
- muutos figure: the velocity arrows are now about 68 px long in both panels, as the caption says. The hero no longer shows the path the car would take when grip fails, so it does not give the prediction away.
- esimerkki figure (centre on the right): friction comes from the right bottom corner toward the centre, N = G, and x points right. It matches the force diagrams in the solutions.
- Unchanged numbers, recomputed again:
  - worked example: 6000 N, μ0 ≥ 0.510
  - experiment 1: v_max = 19.81, with the mistake values 22.15 and 392.4
  - experiment 2: ratio 0.920
  - siirto: 15.34, check-2: 148.0, check-3: 0.765 N
  - graph points: unchanged
- lesson-answers.py gives slide radii of 79.6 and 114.7 m. That is v²/(μ0 g), the same model as the sim.
