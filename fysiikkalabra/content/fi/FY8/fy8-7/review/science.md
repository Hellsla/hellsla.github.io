VERDICT: PASS
CONTENT-HASH: 70c44750233f7ee3

## Blocking

## Polish
- assets/sims/fy8/fy8-7/sim.js:82 — the readout shows `P_ulos` with no decimals, so at 1,5 W it reads 13 mW (1,3 W: 4 mW) while simState, the experiment table and the feedback of ennuste-1 and johtopaatos say 12,5 mW — show one decimal (`tx(S.Pout, 1)`).
- inquiry.json:403 (siirto) — "Kuinka paljon lämpöä kuituun syntyy" after the same sentence says the energy stays as sisäenergia; guardrails: heat is energy in transfer — ask "kuinka paljon energiaa muuttuu kuidun sisäenergiaksi sekunnissa", and say that all pump light is absorbed (the solution assumes it).
- lesson.md:124 — "lähes yksiväristä, koska fotonit syntyvät samassa siirtymässä": spontaneous light of one transition is also one line; the reason that separates the laser is that each stimulated photon copies the incoming photon's energy (and the mirrors select it) — add that half sentence.
- inquiry.json (ennuste-1 feedbacks) — they cite model values at 0,5 W and 4,0 W (125 mW), which koe-1 does not ask the student to record — add them to the intro's list or cite only 1,0–3,0 W.
- lesson.md:89 — "Siksi tasolle E2 ehtii kertyä enemmän atomeja kuin perustilaan jää" holds only when the pumping is strong enough (the sim shows it: below 1,0 W no inversion) — add "kun pumppaus on riittävän voimakas".

## Checked
- All numbers recomputed with own formulas in one script: graph points 2,04 / 2,68 / 3,27 · 10^15 1/s, example 3,1848 · 10^15 1/s and 632,65 nm, 1,91 / 3,06 / 1,89 / 1,79 eV, CdSe 713 nm, dot energies 2,58–2,00 eV; all agree with lesson-answers.py.
- Rate graph and dot figure are to scale as stated (pixel positions of the three points and the line end; dot radii 2:3:4:5:6).
- Sim rate equations: three levels n2 = w/(1+w), clamp at 55 %, P_ulos = 100 mW·(0,45w − 0,55), threshold 1,22 W; two levels n2 = w/(1+2w) < 50 %; sim.js, lesson-answers.py, the calc box and sim-spec agree; values 12,5 / 35 / 80 / 125 / 170 mW and 33,3 / 40,0 / 45,5 % confirmed.
- Experiments: levels and mirrors locked, only P varied; simState gives n2, inv, Pout; inv = 0 exactly at 1,0 W, inversion without beam at 1,1–1,2 W matches the threshold text.
- Predictions: exactly one correct option each; every distractor false in the model and its feedback numbers right.
- Kertaus (1,89 eV, 656 nm), Etsi virhe (1,34 · 10^25 vs 1,34 · 10^16; 5 MW), siirto (96,3 W; mistakes 87,9 and 1096 W), tarkistus-2 (532,19 nm; 397 and 228 nm).
- Worked example: seven stages, symbolic first, units, two significant figures from 1,0 mW, real reasonableness check.
- Causality: stimulated emission conserves energy (atom gives E2 − E1), two-level limit, threshold = gain against losses, laser hazard = beam concentration; consistent in theory, summary, feedback, exit ticket and glossary.
- Facts: Einstein 1917, ruby 694 nm and ms lifetime, He-Ne 633 nm, Nobel 2023 (chemistry) and 2025 (physics), tunnelling applications.
- Scope: inside FY8 central contents; no de Broglie wavelength, quantum-dot size relation qualitative, tunnelling optional as the slot says.
