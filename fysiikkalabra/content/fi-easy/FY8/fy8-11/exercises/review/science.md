VERDICT: PASS
CONTENT-HASH: ce912ff12996becd

## Blocking

## Polish
- exercises/exercises.json L3-04 c) — the task says the fuel must be isolated "tuhansia vuosia", the lesson and the solution of L3-03 say "satojatuhansia vuosia" (Pu-239 to a thousandth in 240 000 a) — write "satojatuhansia vuosia" in the task.
- exercises/solutions.md L2-01, L2-04 — the solution's answer is given with two figures ($1{,}5\,\text{kg}$, $4{,}1\,\%$) while the stored answer has three (1.51, 4.11); both are inside the tolerance, but the page shows one and the solution the other — give the same figures in both.
- exercises/exercises.json L1-07 (feedback) and solutions.md L1-07 — "lyhyen kantaman ydinvoimat" for what the lesson calls "vahva vuorovaikutus"; in a chapter about ydinvoima the word reads as nuclear power — use "vahva vuorovaikutus".
- exercises/exercises.json L2-05 a) — "alikriittinen" and "ylikriittinen" are used in the question, but the brief's lesson defines only "kriittinen" ($k = 1$) — add "($k < 1$)" and "($k > 1$)" to the question.
- exercises/exercises.json L2-01 — "polttoaineen massa pienenee" is the energy $E = Pt$ leaving the core as heat; say "reaktorin sydämen massa pienenee energiaa vastaavan määrän" so that it is not read as fuel consumed (L3-01 gives 4,5 kg of U-235 per day for the same reactor).

## Checked
- All 17 numeric answers recomputed from the task texts with my own formulas: each agrees with answers.py and the stored answer inside its tolerance (4,7834; 178,38; 348,68; 3,2690; 939,57; 3,204; 1,5087; 3,3735; 184,68; 4,1056; 1859,6; 34,642; 4,5257; 8,9438; 2,4018; 249,73; 542,99).
- Reaction energies use atomic masses with the Z sum conserved, so the electrons cancel; in L3-02 four hydrogen atoms minus one helium atom gives the full 26,73 MeV, and the neutrino share is covered by the stated assumption.
- L2-03: mass number gives x = 2; charge 92 = 54 + 38.
- L3-04: least-squares fit of ln A: λ = 0,02285 1/a, A0 = 30 060 TBq/t, half-life 30,3 a, 249,7 a; two far points give 251 a, inside ±5 %; the extrapolation 50 → 250 a is said, and the solution says the model covers fission products only.
- L3-05: 1536 MW thermal, 1029 MW to the cooling water, 4,457 · 10^16 J, 1,54 · 10^6 t of coal, mass ratio 2,8 · 10^6; assumptions stated in the task.
- L2-08: 92,16 MeV → 84,888 MeV, Q = −7,27 MeV; one correct answer and one correct reason; the other reasons are wrong for the stated causes.
- L1-06, L1-07, L2-07: exactly one correct option; each distractor's feedback names the real error.
- L2-05: ratios 1,009–1,016, k = 1,01248 from the first and last value; L2-06 sum 4394 MW.
- Reasonableness checks recomputed (1,3 kg; 1,041^40 = 4,99; 1,0125^55 = 1,98; 30 000 : 256 = 117; 82 GJ/g).
- Units and scaled answer units (10^-11 J, 10^14 J/kg, 10^37 1/s, 10^5 a, TWh) are consistent; scope stays within FY8 (reaction energy, chain reaction, decay law).
