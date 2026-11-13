VERDICT: PASS
CONTENT-HASH: de002e4a7676e5f2
SCOPE: delta added-exercise from 89a47ad1ed9999a9 base 89bcb63b7431

## Blocking

## Polish
- exercises/solutions.md (fy3-4-L1-10, Periaate) — as in round 1: "Sukeltaja tuntee veden painon ja … ilman painon". A pressure is not a weight the diver feels. Clearer: "paine syntyy sukeltajan yläpuolella olevan veden ja ilman painosta".
- exercises/solutions.md (fy3-4-L2-08, Vastaus) — "1450–1600 kg/m³ hyväksytään" does not match the stored tolerance 0,04 (1468–1590 kg/m³). Also, the reason for two figures is that a graph reading is only as good as the drawing, not that the values lie on grid lines: the line ends exactly on a grid crossing. Align the range and the reason.

## Checked
- Round-1 blocker fixed: the task and the solution now give the depth $25{,}0\,\text{m}$, so three significant figures are justified by $h$, $p_0 = 101\,\text{kPa}$ and $\rho = 1{,}02 \cdot 10^3\,\text{kg/m}^3$.
- L1-10 recomputed: $p = 101\,\text{kPa} + 1020 \cdot 9{,}81 \cdot 25{,}0\,\text{Pa} = 351{,}2\,\text{kPa}$ (answers.py gives 351,2); with ρ = 1025 or 1030 kg/m³ 352,4 or 353,6 kPa, inside tolerance 0,04.
- L1-10 model: a liquid at rest with $p_0$ at the surface and total pressure asked, as in the chapter. The formula is already solved, the kPa/Pa conversions are given, and the check (about 1 atm per 10 m) is a real one.
- L2-08 unchanged since round 1: $k_\text{B} = 15\,\text{kPa/m}$ read at grid crossings, $\rho_\text{B} = k_\text{B}/g = 1529\,\text{kg/m}^3$, which matches answers.py. The unit derivation and the cross-check with liquid A are right.
- Figure description lists the points, not the densities; nothing gives the answer away.
- In FY3 scope; rest of the set unchanged since PASS; hash same at start and end.
