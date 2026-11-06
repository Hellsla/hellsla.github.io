VERDICT: PASS
CONTENT-HASH: 02aacafbb23bb84d

## Blocking

## Polish
- exercises.json:303 (L2-08, option a_A = 4 a_B) — the diagnosis is not coherent: if the heavier asteroid pulled the lighter one harder, the lighter one would accelerate more, not the heavier. Name the real mistake, e.g. "Tässä kiihtyvyys on ajateltu kasvavan kappaleen oman massan mukana, vaikka $a = \tfrac{F}{m}$."
- exercises.json:327 (L2-08, reason 4) — the force grows as the asteroids approach because $r$ is in the denominator; the square says how fast it grows. Suggested: "…koska etäisyys on kaavan nimittäjässä."

## Checked
- Diff against HEAD~1: only L2-08 (type 1, Perustelumonivalinta) is new.
- answers.py run once; all numeric answers inside tolerance.
- Recomputed: $F = 4{,}27\cdot 10^{7}\,\text{N}$, $a_\text{A} = 5{,}34\cdot 10^{-6}\,\text{m/s}^2$ and $a_\text{B} = 2{,}14\cdot 10^{-5}\,\text{m/s}^2$, ratio 4. This matches the solution.
- Data are realistic: at about 2000 kg/m³ the radii are about 1,0 km and 0,6 km, well under the 5,0 km separation, so the spherical model holds. The condition "kaukana muista" is stated.
- Exactly one correct choice and one correct reason. The correct choice's feedback ("Valitse seuraavaksi perustelu") does not give the reason away.
- The four reasons are of similar length and none is hedged, so the correct one is not identifiable by form.
- Reason 1 is the chapter's own warned mistake. Reason 2's feedback (each body sits in the other's field and $g_\text{A} < g_\text{B}$) is right.
- The solution's aligned blocks are broken into short lines (text check only).
