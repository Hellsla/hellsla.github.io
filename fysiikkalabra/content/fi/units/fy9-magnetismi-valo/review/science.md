VERDICT: PASS
CONTENT-HASH: 0944d5d3eb93fbe8
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at e02ff82901bd9b74.

## Blocking
(none)

## Polish
- s2: part a uses $\beta_\text{max}$ for the angle to the fibre axis, and part c now uses $\beta = 10\,\text{dB}$ for the decibel factor in the same task. Writing $10\,\text{dB}$ directly (as in the unit's kaavat) would avoid the clash.

## Checked
- s1 c: $P_\text{h}/P = RP/U^2 = 0.225$ %, and 843.75 kW at 400 V. $U_1$ and $U_2$ match part a/b's names (generator 400 V, line 20.0 kV).
- s2 c: $A = aL + N_\text{j}A_\text{j} = 3.48$ dB and $P = 0.897$ mW. s7 grating: $\lambda = \sin(\tan^{-1}(x/L))/(kN)$ gives 533.0 and 532.2 nm.
Every number in the changed lines was recomputed with an independent script (scratchpad fy9merge/sci_fi.py); `units.py hash` gave the same value at the start and the end. LaTeX in all added lines has balanced `$` and braces.
