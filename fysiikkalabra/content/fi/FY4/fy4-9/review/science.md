VERDICT: PASS
CONTENT-HASH: c474b60ee95b8098

## Blocking

## Polish
- content/fi/FY4/fy4-9/lesson.md:490 — F_ka = |Δp|/Δt is named "keskimääräinen voima". The impulse principle makes it the average *net* force, which equals one force only when the others are negligible (the example states this for weight). Write "keskimääräinen kokonaisvoima" here, to match the new hook answer, which separates net force from the surface force.
- lesson.md:566 (Tiivistelmä) — "pienentävät voimaa" → "pienentävät keskimääräistä voimaa", as in the theory.
- lesson.md:271 — "raskaan kappaleen nopeuden muuttaminen vaatii suuremman voiman" needs "yhtä nopeasti" or "samassa ajassa".

## Checked
- The new hook answer is right: same Δp, same net-force impulse; the average normal force = average net force + weight, and both fall as Δt grows; lower force means less strain and lower injury risk. The same wording is in check-3's model answer.
- Recomputed with my own formulas: Δt = (π/2)√(m/k), F_max = v√(km), I = −2F_maxΔt/π = −mv for k = 1600/400/100 N/m (0,0393/0,0785/0,157 s; 80/40/20 N; −2,00 N·s), bounce −4,00 N·s, exp-3 28,3/40,0/56,6 N; example 870 N, 1529×, 145 N; transfer 80 N and its mistakes; check-2 12 m/s, 43 km/h, 450 N; retrieval 1,5 m/s; error-spotting −4,0; Ydinajatus figure 9,0/9,0/−4,5 kg·m/s.
- Ran model.js in node for every experiment: I = Δp independently, crush depth < bumper, the longest contact 0,444 s fits the graph.
- The pulse kinematics in model.js (v, c) integrate correctly. The 0,64 F_max mean is right.
- Figures (pulse curves, 900 N / 12 ms triangle) match figures.py.
- Every choice has exactly one correct option, and each distractor's feedback is right. Signs follow +x throughout.
- The experiments lock m, v and type correctly, and the simState keys exist. The model box states no friction and an ideal spring.
