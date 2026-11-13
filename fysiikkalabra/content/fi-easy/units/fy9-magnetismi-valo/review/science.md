VERDICT: PASS
CONTENT-HASH: 5755edad4011f77c
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at da59d2b57a4936df.

## Blocking
(none)

## Polish
1. Fibre task s2: the a-part uses $\beta_\text{max}$ for the angle to the axis, and the c-part now uses $\beta = 10\,\text{dB}$ for the decibel coefficient in the same task. The subscript separates them, but one symbol for two quantities in one task is avoidable; write $10\,\text{dB}$ directly as in the unit's formula $L = 10\lg(\dots)\,\text{dB}$.

## Checked
Every hunk of the fi-easy merge diff for this unit: the new symbolic steps (solving for the asked quantity before numbers) against the existing substitutions, answers and unit formula names/notation of #522; LaTeX balanced. Content hash recomputed with scripts/units.py (matches). Recomputed: $P_\text{h}/P = RP/U^2 = 6{,}0 \cdot 150\,000/20\,000^2 = 0{,}225\,\%$ (equals $RI^2/P$); at $400\,\text{V}$ $RI^2 = 844\,\text{kW}$; $U_1 = 400\,\text{V}$ agrees with the primary of the b-part ($375\,\text{A}$). Fibre $A = aL + N_\text{j}A_\text{j} = 3{,}48\,\text{dB}$, $P = 0{,}897\,\text{mW}$. Grating $d = 1/N$ with $N$ per length is dimensionally right; $\lambda = 533{,}0$ and $532{,}2\,\text{nm}$.
