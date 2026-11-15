VERDICT: PASS
CONTENT-HASH: 91a1941d77b81148

## Blocking

## Polish
- exercises/solutions.md:70 and :136 (L2-01, L2-04) — Vastaus says "1,5 kg, kaksi merkitsevää numeroa" and "noin 4,1 %", but exercises.json stores 1.51 and 4.11 (inside the tolerance) — store the two-figure value or justify three figures.
- exercises/solutions.md:212–213 (L2-05) — the extrapolation from 5 to 50 generations is not named: the consecutive ratios 1,009–1,016 would give about 1700–2000 neutrons — add a sentence that N_50 is far beyond the data and sensitive to k.
- exercises/exercises.json:101 and solutions.md:192–193 (L1-07) — "lyhyen kantaman ydinvoimat" where the lesson says "vahva vuorovaikutus"; ambiguous in a chapter about ydinvoima — use "vahva vuorovaikutus".
- exercises/exercises.json:126 (L2-02) — "kilogramma deuterium–tritium-seosta" assumes equal numbers of both nuclei, as the solution does — say so in the task.

## Checked
- All 17 numeric answers recomputed in one script with my own formulas from the task texts: all agree with answers.py and lie inside the stored tolerances.
- L3-04: own least squares of ln A gives λ = 0,02285 1/a, A0 = 30 058 TBq/t, T½ = 30,3 a, t = 249,7 a; a two-point reading gives 251 a (inside 5 %); the extrapolation 50 → 250 a and its limit (Pu-239) are stated.
- L3-05: 1536 MW, 1029 MW to cooling water, 4,457·10^16 J, 543,0 kg, 1,54·10^6 t coal; assumptions stated in the task.
- L3-02: 26,73 MeV per helium nucleus; the assumption that all energy becomes radiation is stated.
- L2-08: 92,16 → 84,888 MeV, Q = −7,27 MeV; one correct choice and one correct reason.
- L1-06, L1-07, L2-07: exactly one correct option, every distractor wrong, feedback physically right.
- L2-06: 4394 MW, 34,64 TWh; source and year given; capacity factor marked as an assumption.
- A and Z conserved (L1-01, L1-04, L2-03, x = 2); electron masses cancel as the solutions say.
- Solutions: symbolic form before substitution, conversions right, reasonableness checks real; notation Q, k, N_g as in the brief.
- Scope inside FY8; example data labelled esimerkkiaineisto; hash identical at start and end.
