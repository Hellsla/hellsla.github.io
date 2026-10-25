VERDICT: PASS
CONTENT-HASH: 69d12376298ae428

## Blocking

## Polish
- solutions.md L1-03 Järkevyys — "18 g, mikä on tavallisen patruunan koko": common automatic-lifejacket cartridges hold about 24–38 g CO₂, so 18 g is on the small side; "pienen patruunan koko" or drop the claim (carried over from round 2, file line unchanged).
- solutions.md L2-01 Järkevyys — the sentence names both molecular size and attraction, then gives a pressure that is too high; at 288 K and about 180 bar attraction wins (Z < 1). An optional "vetovoima on tässä hallitseva" would make the direction self-explanatory. Not an error.

## Checked
- Hash 69d12376298ae428 at start and end.
- Reused (round 2, files unchanged): all 12 answers recomputed with independent formulas; answers.py, exercises.json and mine agree within 0,5 % (tolerance 2 %).
- Reused: exit ticket (0,601 mol), worked example (0,2073 mol, 0,829 g, air 6,01 g, 24,1 l/mol), SVG numbers, solution side-checks, formulas, conditions and FY3 scope.
- Reused: sim.js physics p = NkT/A, P_REF computed from it; Playwright 8 slider states ratio 0,95–1,05; 300-window statistics (N = 20 sd 5,5 %, N = 100 sd 2,5 %).
- New, lesson.md: reference state N = 100, T = 300 K, V = 100 %, p/p_ref = 1 matches sim.js (P_REF = 100·kT/(LXMAX·LY), prediction (N/100)(T/300)/Vrel, slider defaults 100/300/100).
- New, sim.js volume handling: sync() only rescales x positions of particles outside the new wall and sets Lx; step() reflects off the wall as a static wall, velocities never scaled by volume. So "tilavuuden muutos ei muuta hiukkasten nopeuksia, joten lämpötila pysyy samana" is true of the code (isothermal model).
- New, solutions.md L2-01: given density 240 kg/m³ at 288 K, O₂ (Tc 155 K, pc 50 bar; Tr ≈ 1,86, pr ≈ 3,4) has Z ≈ 0,94–0,95, so the real pressure is about 170 bar and the ideal 179,6 bar is about 5–6 % too high. "Noin 6 % liian suuren paineen" is defensible and the direction is right; answer 180 bar correctly kept as the ideal-gas value asked for.
- New, sim.js note text: reference state, isothermal clause and adaptive-scale sentence are correct; particle dynamics, measurement and scaling code as in round 2.
- Screenshot fy3-10-sim-1280.png (newer than sim.js): bars 0,99 / 1,00 with labelled ticks 0–2,0, dashed reference at 1, axis name p/p_ref with the new label "asteikko mukautuu"; gauge and ratio strip consistent.
