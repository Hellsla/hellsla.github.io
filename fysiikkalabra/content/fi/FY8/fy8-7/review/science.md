VERDICT: PASS
CONTENT-HASH: 70c44750233f7ee3

## Blocking

## Polish
- assets/sims/fy8/fy8-7/sim.js:82 — the readout shows `P_ulos` without decimals, so at 1,5 W it reads 13 mW while simState, the experiment table and the feedback say 12,5 mW — use `tx(S.Pout, 1)`.
- inquiry.json:403 (siirto) — "kuinka paljon lämpöä kuituun syntyy" right after "jää kuituun sisäenergiaksi" (guardrails: heat is energy in transfer) — ask how much energy becomes the fibre's internal energy per second, and state that all pump light is absorbed (the solution assumes it).
- lesson.md:124 — "lähes yksiväristä, koska fotonit syntyvät samassa siirtymässä": spontaneous light of one transition is one line too — add that each stimulated photon copies the incoming photon's energy.
- inquiry.json (ennuste-1 feedback) — cites model values at 0,5 W and 4,0 W, which koe-1 does not ask the student to record — add them to the intro's list or cite 1,0–3,0 W only.
- lesson.md:89 — "tasolle E2 ehtii kertyä enemmän atomeja kuin perustilaan jää" holds only with strong enough pumping (the sim: none below 1,0 W) — add "kun pumppaus on riittävän voimakas".

## Checked
- Every number recomputed with own formulas in one script (graph 2,04 / 2,68 / 3,27 · 10^15 1/s, example 3,1848 · 10^15 1/s and 632,65 nm, photon energies, CdSe 713 nm, dot table 2,58–2,00 eV); agrees with lesson-answers.py.
- Rate graph and dot figure are to scale as they state (pixel positions; radii 2:3:4:5:6).
- Sim rate equations: n2 = w/(1+w), clamp 55 %, P_ulos = 100 mW·(0,45w − 0,55), threshold 1,22 W; two levels n2 = w/(1+2w) < 50 %; sim.js, calc box, sim-spec and feedback values agree.
- Experiments: levels and mirrors locked, only P varied; simState gives n2, inv, Pout; inversion without a beam at 1,1–1,2 W fits the threshold text.
- Predictions and checks: exactly one correct option each, distractors false, feedback numbers right.
- Kertaus, Etsi virhe (10^25 vs 1,34 · 10^16; 5 MW), siirto (96,3 W; mistakes 87,9 and 1096 W), tarkistus-2 (532,19 nm; 397, 228 nm).
- Worked example: seven stages, symbolic first, units, rounding from 1,0 mW, real reasonableness check.
- Causality: energy in stimulated emission, two-level limit, threshold as gain against losses, laser hazard; same in theory, summary, feedback, exit ticket.
- Facts: Einstein 1917, ruby 694 nm, He-Ne 633 nm, Nobel 2023 and 2025, tunnelling applications.
- Scope: FY8 central contents; no de Broglie wavelength; tunnelling optional.
