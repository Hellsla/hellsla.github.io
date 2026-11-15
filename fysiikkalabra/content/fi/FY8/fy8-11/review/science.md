VERDICT: PASS
CONTENT-HASH: 016d0a52584ddcac

## Blocking

## Polish
- inquiry.json:365,377 (tarkistus-2 hint 3 and solution) — the drawn trend curve is at about 8,56 MeV for A = 118 and 7,64 MeV for A = 236, while the text reads "8,5" and "7,6" and claims a reading accuracy of 0,05 MeV; the result (212–217 MeV) stays inside the tolerance — write "noin 8,5–8,6 MeV" or read 8,55 and 7,65.
- lesson.md:577 (Onkalo) — STUK's statement "elokuussa 2026" and the licence of 22.10.2026 to the end of 2070 could not be checked by the reviewer (no network; developer.md names Yle and Posiva 22.10.2026) — add the source line as for the other Finnish figures.
- inquiry.json:348 (tarkistus-1, electric-energy option) — the feedback answers only for fusion; in fission the fragments do get their kinetic energy through electric repulsion, so say that the option fails because of "kummassakin" (fusion must work against the repulsion).
- lesson-answers.py:113 and the decay-heat comment — the comments say "seitsemäskymmenesosa" and "6–7 %", the lesson says 1,5 % and 6 %; align the comments.

## Checked
- Own recomputation (one script): E_B/A of the seven plotted nuclei, example Q = 173,28 MeV (Δm 0,1860220 u, 0,079 %), D–T 0,0188829 u → 17,59 MeV, 3,5 vs 0,85 MeV per nucleon (ratio 4,2), 1 g U-235 → 2,56·10^21 nuclei, 82 GJ, 2,83 t coal, hook 11 900 t/d; all agree with the text.
- Sim chain rerun in node from sim.js's own generator: koe 1 N20 = 39 387 / 934 / 7 at k = 1,20 / 1,00 / 0,80; koe 2 N = 1000, 1437, 1987, 3264; every feedback and model answer quotes these values and calls them model values.
- sim.js implements the stated model (P_f = k/2,5, 2 or 3 neutrons, rod share 0,0032 s, total loss consistent); limits (no delayed neutrons, temperature, burn-up, time) said in Mallin oletukset; simState gives k, N, model; slider step 5 reaches 0, 20, 25, 50.
- Experiments isolate the varied parameter (koe 1: s with g and series locked; koe 2: g with s and series locked).
- Predictions: exactly one correct option each; 1,04^30 = 3,24, 176 generations to 10^6, about 80 per generation at g = 20.
- Etsi virhe: −0,8226429 u, −766 MeV; one correct option, distractor feedback right.
- Siirto: 1,7734·10^20 1/s; mistake values 1 773 351 and 0,156; 1,48 mg of fuel per second.
- Figures: sidosenergia points and axes to scale (pixel check), Onkalo depth scale gives 430 m, massat and ketju numbers, fusion nucleon counts.
- Finnish plant data, licences, half-lives, decay heat (6 %, 258 MW for OL3), IPCC 12 vs 820 g/kWh, ITER Q = 10 and D–T 2039: consistent with known sources.
- Scope: inside FY8 central contents; atomic masses in u with 931,5 MeV; conservation of A and Z shown; no force diagrams.
