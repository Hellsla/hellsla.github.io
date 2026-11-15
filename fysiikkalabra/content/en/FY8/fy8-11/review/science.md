VERDICT: PASS
CONTENT-HASH: f042f38356a8f6fc

## Blocking

## Polish
- inquiry.json:377 (tarkistus-2 solution, hint 3) — the lesson's curve gives 8.56 MeV at A = 118 (7.63 at A = 236), so a careful reading on a 0.1 MeV grid is 8.55–8.6, not "about 8.5"; the result 217–236 MeV stays inside the 15 % tolerance (178–242) — say "about 8.5–8.6 MeV" or note that either reading is accepted.
- lesson.md:577 — the Onkalo dates (STUK statement August 2026, operating licence 22 October 2026 until the end of 2070) are later than anything this reviewer can verify; confirm against the Government/STUK release and name the source as the plant table does.
- inquiry.json:18 (hook) — 12 000 t of coal per day follows only with an efficiency of 0.40 (11 900 t; 14 400 t at 0.33); the assumption is unstated. Suits the level, but "about" carries it.
- inquiry.json:348 (tarkistus-1, electric-energy distractor) — the feedback refutes the option only for fusion; in fission the electric repulsion does accelerate the fragments. One clause ("the option fails for fusion, where the repulsion must be overcome") keeps it exact.
- Packet says check_lesson.py had not been run; no lint physics warnings were available to judge.

## Checked
- Recomputed with own formulas: worked example 236.0525931 u, 235.8665711 u, 0.1860220 u, 173.28 MeV, 0.079 %; Find the error -0.8226429 u, -766 MeV.
- D–T: 0.0188829 u, 17.59 MeV; 3.52 vs 0.85 MeV per nucleon, ratio 4.2; 1 g U-235: 2.56e21 nuclei, 82 GJ, 2.83 t coal.
- Binding-energy figure: all seven points match values computed from atomic masses (1.11, 7.07, 7.68, 8.79, 8.51, 8.33, 7.59 MeV) at the drawn coordinates; figure is to scale. Onkalo depth scale gives 430 m.
- Simulation: re-ran the seeded generator independently: N20 = 39 387 / 934 / 7 at s = 0 / 25 / 50 %; k = 1.04 gives 1000, 1437, 1987, 3264; capture of koe-1 shows the same k, N and model 38 338.
- sim.js implements the stated model (P_f = (1.2 - 0.008 s)/2.5, 2 or 3 neutrons, k = 1.2 - 0.008 s; rod loss 0.0032 s consistent); limits (no delayed neutrons, temperature, burn-up, generations not time) are stated.
- Experiments isolate the varied parameter (g and series locked in koe-1; s and series locked in koe-2); simState supplies k, N, model.
- Predictions: one correct option each; distractor feedback numbers right (1.04^30 = 3.24, 176 generations to 10^6, about 80 per generation at g = 20).
- ITER transfer: 1.7734e20 1/s; mistakes 1 773 351 and 0.156; 1.48 mg of fuel per second.
- Facts: delayed neutrons 0.65 %, enrichment, residual heat 6 % and 1–2 %, half-lives, IPCC 12 g/kWh = 1.5 % of coal, plant powers and years, ITER figures.
- Scope: inside FY8 central contents; reaction energy from atomic masses with 931.5 MeV/c^2 as the scope notes require; theory, summary, glossary, exit ticket and model answers agree.
