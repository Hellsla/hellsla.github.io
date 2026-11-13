VERDICT: FAIL
CONTENT-HASH: 5ee2e458834a4d0e

## Blocking
- exercises/solutions.md (fy3-4-L1-10, Vastaus) — A (rounding): "kolme merkitsevää numeroa kuten ilmanpaineessa ja tiheydessä" ignores the limiting datum, the depth $25\,\text{m}$ (two figures). The term $\rho g h = 250\,\text{kPa}$ is then known only to about $\pm 5\,\text{kPa}$, so $351\,\text{kPa}$ claims more than the data give; the brief's own worked example names the depth among the data that set the figures. — Fix: give the depth as $25{,}0\,\text{m}$ in the task and solution (then 351 kPa and the reason stand once the depth is named), or answer $3{,}5 \cdot 10^2\,\text{kPa}$ with the depth as the reason.

## Polish
- exercises/solutions.md (fy3-4-L1-10, Periaate) — "Sukeltaja tuntee veden painon ja veden pinnalla olevan ilman painon": pressure is not weight felt; clearer as "paine syntyy sukeltajan yläpuolella olevan veden ja ilman painosta" (C, wording).
- exercises/solutions.md (fy3-4-L2-08) — "kaksi merkitsevää numeroa, koska kuvaajan arvot on luettu ruudukon viivoilta": the line ends exactly on a grid crossing, so the reading itself is exact; the real reason is that a graph reading is only as good as the drawing. Optional rewording.

## Checked
- MAFY value verified on mafytaulukot.fi (*Tiheyksiä*): merivesi $1{,}02 \cdot 10^3\,\text{kg/m}^3$, as the solution uses.
- L1-10 recomputed: $p = p_0 + \rho g h = 101 + 250{,}2 = 351{,}2\,\text{kPa}$ (answers.py agrees); with $\rho = 1025$ or $1030\,\text{kg/m}^3$ 352–354 kPa, inside tolerance 0,04. Model (liquid at rest, $p_0$ at the surface) is the chapter's.
- L1-10 solution: symbolic formula, kPa/Pa conversions, reasonableness estimate (~1 atm per 10 m) real.
- L2-08 recomputed from the figure code: B through (0; 100 kPa) and (10 m; 250 kPa) on grid crossings (grid 1 m, 25 kPa, 250 labelled), $k_\text{B} = 15\,\text{kPa/m}$, $\rho_\text{B} = k_\text{B}/g = 1529\,\text{kg/m}^3$; answers.py agrees; $1{,}5 \cdot 10^3$ is 1,9 % off, inside tolerance.
- L2-08 unit derivation $\frac{\text{Pa/m}}{\text{m/s}^2} = \text{kg/m}^3$ right; check via liquid A ($\approx 1020\,\text{kg/m}^3$, seawater-like) consistent.
- Figure description lists points, not densities or slopes; nothing gives the answer away.
- Both in FY3 scope (hydrostatic pressure, linear model with constant term).
- Rest of the set unchanged since PASS; hash same at start and end.
