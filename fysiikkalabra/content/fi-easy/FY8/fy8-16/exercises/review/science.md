VERDICT: PASS
CONTENT-HASH: 2314041f626411b2
Mode: delta

## Blocking
- none

## Polish
- content/fi-easy/FY8/fy8-16/exercises/solutions.md:299 — L3-06 Vastaus "$4{,}2 \cdot 10^{2}\,\text{Mpc}$ eli noin $416\,\text{Mpc}$" puts a two-figure result next to a three-figure one, and the Järkevyys line repeats "$416\,\text{Mpc}$". 420 is inside the tolerance (0,9 %), so nothing breaks — give one rounding, e.g. "$4{,}2 \cdot 10^{2}\,\text{Mpc}$ (laskettu $416{,}4\,\text{Mpc}$)".

## Checked
- Hash at start and end identical (2314041f626411b2, `--exercises --lang fi-easy`).
- One script recomputed L2-09 from the task text: z = 15,3/434,0 = 0,03525, v = 10 569 km/s, H0 = 18 000/250 = 72,0 km/s/Mpc, d = 146,8 Mpc. answers.py gives 146,791475, the same. Tolerance 0,02 accepts 147 (0,14 %).
- Recomputed L3-06: d = 0,10·2,998·10^5 / 72,0 = 416,4 Mpc, the same as answers.py. Both 416 and 420 fall inside the tolerance.
- Figure hubble-t: H = t2-H0 = 72,0 (lesson-answers.py). The line from (0,0) to (291,7 Mpc, 21 000 km/s) passes through the grid point (250, 18 000), and the figure description says so. A least-squares fit through the origin of the nine points gives 72,4, so the line fits the data. The figure gives H0 by reading the slope, which the task asks for. It does not give d away.
- Conditions: both tasks state the z < 0,1 limit of v = cz. L2-09 has z = 0,035. The figure's top edge, 21 000 km/s, is z = 0,070, so every point of the figure meets the condition. L3-06 c) keeps two things apart: extrapolating v = H0 d past 285 Mpc (about 1,5 times the data's reach) and v = cz failing at large z. The z = 3,00 → 3c example is correct.
- Järkevyys checks are real: the points (120 Mpc, 8300 km/s) and (160 Mpc, 11 900 km/s) are in the figure data and bracket the L2-09 result, and the products check the answers by multiplying back.
- Each solution solves for the unknown in symbols before substituting (d = cz/H0). No conversions are needed because the units are km/s and Mpc, and the solution says so. The sig-fig reasons are right for L2-09 (15,3 nm and 449,3/434,0 have three figures) and for L3-06 (0,10 has two).
- Notation (z, λ0, Δλ, H0, v = H0 d) and scope (Hubblen ja Lemaîtren laki, punasiirtymä) match the lesson brief.
- "(esimerkkiaineisto)" removed from the L2 and L3 captions. This follows the house rule against provenance badges on invented data. No caption or task calls the data measured, so it does not break the guardrail.
