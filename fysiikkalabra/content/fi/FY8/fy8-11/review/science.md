VERDICT: PASS
CONTENT-HASH: 016d0a52584ddcac

## Blocking

## Polish
- inquiry.json:365,377 (tarkistus-2 hint 3, solution) — the drawn curve is at about 8,56 MeV (A = 118) and 7,64 MeV (A = 236); the text reads "8,5" and "7,6" yet claims 0,05 MeV reading accuracy; result 212–217 MeV stays inside the tolerance — write "noin 8,5–8,6 MeV" or read 8,55 and 7,65.
- lesson.md:577 (Onkalo) — STUK's statement "elokuussa 2026" and the licence of 22.10.2026 to the end of 2070 could not be checked (no network; developer.md names Yle and Posiva) — add a source line as for the other Finnish figures.
- inquiry.json:348 (tarkistus-1, electric-energy option) — the feedback answers only for fusion; in fission the fragments do gain kinetic energy through electric repulsion — say the option fails because of "kummassakin".
- lesson-answers.py:113 and the decay-heat comment — comments say "seitsemäskymmenesosa" and "6–7 %", the lesson 1,5 % and 6 % — align.

## Checked
- Own recomputation in one script: E_B/A of the seven plotted nuclei, example Q = 173,28 MeV (0,1860220 u, 0,079 %), D–T 17,59 MeV, 3,5 vs 0,85 MeV per nucleon, 1 g U-235 → 2,56·10^21 nuclei, 82 GJ, 2,83 t coal, hook 11 900 t/d: all agree.
- Sim chain rerun in node with sim.js's generator: koe 1 N20 = 39 387 / 934 / 7 (k = 1,20 / 1,00 / 0,80); koe 2 N = 1000, 1437, 1987, 3264; feedback and model answers quote these as model values.
- sim.js implements the stated model (P_f = k/2,5, 2 or 3 neutrons, rod share 0,0032 s); limits said in Mallin oletukset; simState gives k, N, model; slider step reaches 0, 20, 25, 50.
- Experiments isolate the varied parameter (s with g and series locked; g with s and series locked).
- Predictions: one correct option each; 1,04^30 = 3,24, 176 generations to 10^6, about 80 per generation at g = 20.
- Etsi virhe: −0,8226429 u, −766 MeV; one correct option, distractor feedback right.
- Siirto: 1,7734·10^20 1/s; mistakes 1 773 351 and 0,156; 1,48 mg fuel per second.
- Figures: sidosenergia points to scale (pixel check), Onkalo scale gives 430 m, massat, ketju and fusion nucleon counts.
- Plant data, licences, half-lives, decay heat, IPCC 12 vs 820 g/kWh, ITER Q = 10 and D–T 2039: consistent with known sources.
- Scope inside FY8; A and Z conserved; no force diagrams.
