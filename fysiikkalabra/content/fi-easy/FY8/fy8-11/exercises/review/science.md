VERDICT: PASS
CONTENT-HASH: ce912ff12996becd

## Blocking

## Polish
- exercises/exercises.json L3-04 c) — the task says "eristettävä tuhansia vuosia"; the lesson and L3-03 say "satojatuhansia vuosia" (Pu-239 to a thousandth in 240 000 a) — use the same words.
- exercises/solutions.md L2-01, L2-04 — the solution answers with two figures (1,5 kg; 4,1 %), the stored answer has three (1.51; 4.11); inside the tolerance, but give the same figures in both.
- exercises/exercises.json L1-07 feedback and solutions.md L1-07 — "lyhyen kantaman ydinvoimat" for the lesson's "vahva vuorovaikutus"; in this chapter the word reads as nuclear power — use the lesson's term.
- exercises/exercises.json L2-05 a) — "alikriittinen" and "ylikriittinen" are asked, the lesson defines only "kriittinen" — add (k < 1) and (k > 1) to the question.
- exercises/exercises.json L2-01 — "polttoaineen massa pienenee" can be read as fuel consumed (L3-01: 4,5 kg of U-235 per day in the same reactor) — say the mass decreases by the amount that corresponds to the released energy.

## Checked
- All 17 numeric answers recomputed from the task texts with my own formulas; each agrees with answers.py and the stored answer inside its tolerance (4,7834; 178,38; 348,68; 3,2690; 939,57; 3,204; 1,5087; 3,3735; 184,68; 4,1056; 1859,6; 34,642; 4,5257; 8,9438; 2,4018; 249,73; 542,99).
- Atomic masses are used with the Z sum conserved; in L3-02 four hydrogen atoms minus one helium atom gives 26,73 MeV, the neutrino share covered by the stated assumption.
- L2-03: x = 2 from the mass numbers; 92 = 54 + 38.
- L3-04: least squares of ln A: λ = 0,02285 1/a, A0 = 30 060 TBq/t, half-life 30,3 a, 249,7 a; two far points give 251 a (inside ±5 %); extrapolation 50 → 250 a is said.
- L3-05: 1536 MW, 1029 MW to cooling water, 4,457 · 10^16 J, 1,54 · 10^6 t of coal, ratio 2,8 · 10^6; assumptions stated in the task.
- L2-08: 92,16 → 84,888 MeV, Q = −7,27 MeV; one correct answer and one correct reason.
- L1-06, L1-07, L2-07: exactly one correct option; each distractor's feedback names the real error.
- L2-05: ratios 1,009–1,016, k = 1,01248; L2-06: 4394 MW.
- Reasonableness checks recomputed (1,3 kg; 1,041^40 = 4,99; 1,0125^55 = 1,98; 30 000 : 256 = 117).
- Units and scaled answer units consistent; scope within FY8.
