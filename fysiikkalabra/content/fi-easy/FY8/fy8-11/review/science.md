VERDICT: PASS
CONTENT-HASH: d48f72278c373b27

## Blocking

## Polish
- lesson.md:676 — the Onkalo licence facts (STUK statement August 2026, licence 22 October 2026 to the end of 2070) could not be checked here (no network) — confirm against STUK's or the ministry's release and name the source.
- assets/sims/fy8/fy8-11/sim.js:204 — in Koe 1 the generation is locked at g = 20, but Käynnistä still runs the chain to g = 30, so a row can be recorded at another generation — keep a locked g from changing (shared experiment component).
- inquiry.json:818 — "noin 12 000 tonnia hiiltä joka päivä" assumes an efficiency of 40 % and 29 MJ/kg (11 900 t); say the efficiency.
- lesson.md:275,554 — the fission and fusion figures label the neutron with an italic n, the text uses upright n — one notation.
- lesson-answers.py:2042,2077 — stale comments ("6-7 %", "seitsemäskymmenesosa") differ from the text (6 %, 1,5 %).

## Checked
- Worked example recomputed: 0,1860220 u → 173,28 MeV, 0,079 % of the mass; D–T 0,0188829 u → 17,59 MeV; 3,52 and 0,85 MeV per nucleon, ratio 4,2.
- Miksi: 2,56 · 10^21 nuclei, 82,1 GJ, 2,83 t of coal.
- Simulation re-run with my own port of the generator: 39 387 / 934 / 7 at s = 0 / 25 / 50 % (g = 20); 1000, 1437, 1987, 3264 at s = 20 %; k = 1,2 − 0,008 s; feedback and conclusion quote these as model values.
- Predictions: one correct option each; 1,04^30 = 3,24, 176 generations to a million, about 80 per generation at g = 20.
- Experiments: Koe 1 varies only s, Koe 2 only g; simState gives k, N, model; the capture shows the set state.
- Siirto: 1,7734 · 10^20 1/s; mistakes 1 773 351 and 0,156; 1,48 mg of fuel.
- Tarkista 2: curve 7,64 and 8,56 MeV; 236 · 0,9 = 212 MeV inside ±15 %; mistakes 0,9 and 106. Etsi virhe: −0,8226429 u → −766 MeV.
- Figures: binding-energy points to scale (1,12; 7,07; 7,68; 8,78; 8,52; 8,33; 7,58 MeV), Onkalo scale 430 m, balance and chain figures agree with the text.
- Conditions and causes: electrons cancel when the Z sum is conserved, nucleon number conserved, moderator, delayed neutrons, decay heat 6 % → 1–2 %, enrichment, Cs-137 to a thousandth in 300 a, IPCC 12 g/kWh = 1,5 % of coal.
