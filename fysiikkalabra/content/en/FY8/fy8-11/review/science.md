VERDICT: PASS
CONTENT-HASH: f042f38356a8f6fc

## Blocking

## Polish
- inquiry.json:377 (tarkistus-2 solution, hint 3) — the lesson's curve gives 8.56 MeV at A = 118, so a careful reading is 8.55–8.6, not "about 8.5"; 217–236 MeV stays inside the 15 % tolerance — write "about 8.5–8.6 MeV".
- lesson.md:577 — the Onkalo dates (STUK statement August 2026, licence 22 October 2026 until 2070) are later than this reviewer can verify; confirm against the Government/STUK release and name the source.
- inquiry.json:18 (hook) — 12 000 t of coal per day holds only at an efficiency of 0.40 (14 400 t at 0.33); the assumption is unstated.
- inquiry.json:348 (tarkistus-1, electric-energy distractor) — the feedback refutes the option for fusion only; in fission the repulsion does accelerate the fragments. Say that the option fails for fusion.
- The packet says check_lesson.py had not been run: no lint physics warnings were available to judge.

## Checked
- Own recomputation: worked example 0.1860220 u, 173.28 MeV, 0.079 %; Find the error -0.8226429 u, -766 MeV.
- D–T 0.0188829 u, 17.59 MeV; 3.52 vs 0.85 MeV per nucleon; 1 g U-235: 2.56e21 nuclei, 82 GJ, 2.83 t coal.
- Binding-energy figure: seven points match values from atomic masses at the drawn coordinates (to scale); Onkalo depth scale gives 430 m.
- Simulation: seeded generator re-run independently: N20 = 39 387 / 934 / 7 at s = 0 / 25 / 50 %; k = 1.04 gives 1000, 1437, 1987, 3264; the koe-1 capture shows the same.
- sim.js implements the stated model (k = 1.2 - 0.008 s, rod loss 0.0032 s consistent); its limits are stated.
- Experiments isolate the varied parameter; simState supplies k, N, model.
- Predictions: exactly one correct option; feedback numbers right (1.04^30 = 3.24, 176 generations, about 80 per generation).
- ITER transfer 1.7734e20 1/s; mistakes 1 773 351 and 0.156; 1.48 mg per second.
- Facts: delayed neutrons, enrichment, residual heat, half-lives, IPCC 12 g/kWh, plant table, ITER figures.
- Scope inside FY8; theory, summary, exit ticket and model answers agree.
