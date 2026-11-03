VERDICT: FAIL
CONTENT-HASH: 13e12af1756aa91b

## Blocking
- exercises/solutions.md:12, :17, :42, :47, :52, :57, :59, :72, :77, :79, :82, :87, :89, :92, :97, :102, :107; lessons/FY6/fy6-10/answers.py:8 — (A, course constant) Coulomb's constant is $8{,}99 \cdot 10^{9}$, but the FY6 rule is $k = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N} \cdot \text{m}^2}{\text{C}^2}$ — use 8,988 in the Annettu lines, the substitutions and answers.py. The rounded answers do not change; update the shown intermediates (e.g. L2-01 $r^2 = 4{,}045 \cdot 10^{-3}\,\text{m}^2$, L2-04 $mg : k = 5{,}457 \cdot 10^{-13}$) and the exercises.json answers from the re-run answers.py.

## Polish
- solutions.md L3-02 Vastaus — "kolme merkitsevää numeroa kuten vakiossa $k$": with $k = 8{,}988 \cdot 10^{9}$ the limiting data are G, mₑ, mₚ, e (4 digits); say three digits as a chosen precision, or give $2{,}268 \cdot 10^{39}$.
- solutions.md L1-02 Järkevyys refers to the simulation's 20 nC spheres; the exercise set is reviewed apart from the lesson — the check stands on its own estimate already, so the sim sentence can go.

## Checked
- All 12 answers recomputed independently (k = 8,99 and 8,988): 3,995·10¹⁰; 2,107 mN; 25 kA; +4,0 nC; 0,288 N; 6,36 cm; 0,576 mN; 0,202 mN; 36,9 nC; 0,719 mN; 2,27·10³⁹; 8,0 cm — match answers.py and exercises.json within tolerance.
- Charge sharing of identical touching spheres (L1-04, L2-03) uses conservation and equal split; sign of the result right.
- L3-01 direction: both forces on q₃ point towards q₂, sum not difference; L3-03 balance point independent of the third charge's size and sign, between the charges.
- L3-02 ratio independent of r (both ∝ 1/r²), constants and units consistent.
- Symbolic solving first in every solution; unit conversions (nC, µC, cm, ms, g) correct; rounding tied to the limiting datum.
- Level 3 stays within Coulomb's law and charge (FY6 scope); gravitation law given in the task text.
