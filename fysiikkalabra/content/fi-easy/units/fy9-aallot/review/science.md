VERDICT: PASS
CONTENT-HASH: 56c058a7e6212ab4
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 20cd0c5ea68aaf63.

## Blocking
(none)

## Polish
1. inquiry.json (dB task) and sovella/solutions.md: the symbol $\beta = 10\,\text{dB}$ ("desibeliasteikon kerroin") is the merge's own; the unit text and its kaavat fence write $L = 10\lg(I/I_0)\,\text{dB}$ without a symbol. No contradiction, but some books use $\beta$ for the level itself; writing $10\,\text{dB}$ directly in the symbolic step would match the formula box.

## Checked
Every hunk of the fi-easy merge diff for this unit: the new symbolic steps (solving for the asked quantity before numbers) against the existing substitutions, answers and unit formula names/notation of #522; LaTeX balanced. Content hash recomputed with scripts/units.py (matches). Recomputed: $r_2 = 20\sqrt{10^{1,9}}\,\text{m} = 178\,\text{m}$; fret $d = L - v/(2f') = 70{,}8\,\text{mm}$; pendulum $l_0 = -b/k = -1{,}39\,\text{cm}$, $l = 0{,}977\,\text{m}$; bungee $x = 21{,}59\,\text{m}$, $d = 39{,}6\,\text{m}$. Symbolic forms agree with the substitutions; no unit-text formula name contradicted.
