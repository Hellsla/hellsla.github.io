VERDICT: FAIL
CONTENT-HASH: f8c679679d08ccc9

## Blocking
- content/fi/FY8/fy8-7/exercises/solutions.md:336 (fy8-7-L2-08, Kuvaajan lukeminen) — A: the graph reading step contradicts itself and the figure. It says the vertical grid spacing is $0{,}5$ (true: rate-task has grid lines at 0,5, 1, …, 5) and then that the point is "hieman alle neljännen vaakaviivan (arvo $4{,}0$)". With 0,5 spacing the fourth line above the axis is 2,0, and the 4,0 line is the eighth. A student who follows the count reads 2,0 and gets half the power. The value read (3,9) and the answer are right. — fix: name the line by its value, not by a count ("hieman alle vaakaviivan $4{,}0$", or "kahdeksannen vaakaviivan (arvo $4{,}0$)").

## Polish
- solutions.md:370 (L3-06) — the counts are right on its 1-unit grid ("seitsemännen", "neljännen"). Naming the lines by their values here too would keep the two reading descriptions alike.
- L3-06 tolerance ±4 % — reading each point to ±0,1 on a 1-unit grid moves the ratio by about 2–4 % (6,7/4,1 → 2,91; 6,9/3,9 → 3,15), so a careful reading can just fall into "Lähellä". Acceptable; ±5 % would be safer.

## Checked
- L1-10: $N/t = P\lambda/(hc)$ with MAFY $h = 6{,}626\,070\,15 \cdot 10^{-34}$ J s (docs/mafy-arvot.tsv, VERIFIED, Luonnonvakiot) and the given c: 6,7455e15 1/s → 6,7e15; with h = 6,626e-34 it is the same to 0,001 %. Tolerance 2 % is enough. Two significant figures from 2,0 mW are right. The checks (3,0e-19 J per photon; 532 nm 5,0 mW → 1,3e16) are right.
- L2-08: figure point (520 nm, 3,927 units) = a 1,5 mW laser. Reading 3,9 → 1,490 mW → 1,5 mW, and a reading of 3,85–3,95 stays inside ±3 %. The photon energy is 3,8201e-19 J ≈ 2,38 eV, and 1,0 mW gives 2,62e15 1/s.
- L3-06: the points X (450 nm, 6,796) and Y (800 nm, 4,027) are 3,0 mW and 1,0 mW. The solution's readings give 1,70 · 1,7778 = 3,022 → 3,0, and the exact ratio is 3,000. hc cancels. The photon energies 4,41e-19 J and 2,48e-19 J and the separate powers 3,0 mW and 1,0 mW are right.
- answers.py lines for the three tasks reproduce 6,745547e15, 1,5 and 3,0. The other answers are unchanged.
- Figure SVGs regenerated from figures.py: the point positions match their values and the vertical grid lines (100 nm) match the solutions' counts. The descriptions give the values a reader needs without giving away the power.
- Physics and scope: P = (N/t)hf as in the lesson's Kaava, used symbolically first. Nothing goes beyond FY8.
- Hash f8c679679d08ccc9 at start and end.
