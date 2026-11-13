VERDICT: PASS
CONTENT-HASH: d3680dc9c54e00c7
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at d3680dc9c54e00c7.

## Blocking
(none)

## Polish
1. sovella c): the reason for two significant figures, "$0{,}46\,\text{s}^2$ on kahden numeron luku", applies the multiplication rule to a difference: $3{,}68 - 0{,}46 = 3{,}22$ keeps three digits. Two figures are right, but because of the reading uncertainty that the Järkevyys line itself gives ($\pm 0{,}05\,\text{s}^2$ gives $\pm 0{,}3\,\text{m/s}^2$). Suggested: "koska kuvaajalta lukemisen epävarmuus muuttaa tulosta noin $\pm 0{,}3\,\text{m/s}^2$".

## Checked
Every hunk of the fi-easy merge diff for this unit: the new symbolic steps (solving for the asked quantity before numbers) against the existing substitutions, answers and unit formula names/notation of #522; LaTeX balanced. Content hash recomputed with scripts/units.py (matches). Recomputed $k = 3{,}22/0{,}800 = 4{,}025\,\text{s}^2/\text{m}$, $g = 9{,}81\,\text{m/s}^2$, range with $\pm 0{,}05\,\text{s}^2$ at each point $9{,}5$...$10{,}1$. unit.md: the new sentence (exact numbers and conversion factors do not limit precision) is correct and agrees with fy9-mittaaminen.
