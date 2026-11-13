VERDICT: PASS
CONTENT-HASH: 1cc9fe9daf7c7ebf
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 2ed8859154e6b841.

## Blocking
(none)

## Polish
- inquiry `desibelit`: $\beta = 10\,\text{dB}$ "desibeliasteikon kerroin (määritelmä)" is a symbol the unit text never introduces; its kaavat line writes $10\lg(\dots)\,\text{dB}$. It does no harm, but writing $10\,\text{dB}$ directly, as in the version passed, matches the unit.

## Checked
- inquiry `desibelit` solution: $r_2 = r_1\sqrt{10^{(L_1-L_2)/\beta}}$, 19 dB gives 79.43 and $r_2 = 178$ m, so 180 m. The symbolic form agrees with the unit's $L = 10\lg(I/I_0)\,\text{dB}$ (#522 name).
- s1 b: $d = L - v/(2f') = 70.8$ mm. s4 pendulum: $l_0 = -b/k = -0.014$ m, $l = (T^2-b)/k = 0.977$ m. s6 bungee: $x = 21.59$ m, $d = L_0 + x = 39.6$ m.
Every number in the changed lines was recomputed with an independent script (scratchpad fy9merge/sci_fi.py); `units.py hash` gave the same value at the start and the end. LaTeX in all added lines has balanced `$` and braces.
