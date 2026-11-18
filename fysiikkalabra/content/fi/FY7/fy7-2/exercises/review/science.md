VERDICT: FAIL
CONTENT-HASH: 70bd4c5cd298028f

## Blocking
- solutions.md L2-04 Kaava — **A.** The block opens with $\Sigma F = 0$, which claims the magnetic force and the weight cancel. The task asks only that the magnitudes be equal, and the Periaate says the same ("merkitsemällä nämä yhtä suuriksi"). In Finland a proton moving perpendicular to the nearly vertical Earth field (I ≈ 74°) feels a mostly horizontal magnetic force, so the two forces cannot cancel and the proton is not in equilibrium. — Fix: drop the $\Sigma F = 0$ row and start from $F_\text{m} = G$, then $qvB = mg$ and $v = mg/(qB)$.

## Polish
- solutions.md L3-03 (r_α : r_p) Kaava: the block jumps from $qvB = mv^2/r$ to $r = \tfrac{1}{B}\sqrt{2mU/q}$. The rows $v = \sqrt{2qU/m}$ and $r = mv/(qB)$ (as in L3-01) would show the substitution.

## Checked
- Delta (8g): every rewritten Kaava checked.
- Circular motion (L1-01, L1-03, L1-04, L2-02, L2-05, L2-06, L3-02, L3-05, L1-x electron, L2-10 b): $\Sigma F = ma_\text{n}$, $F_\text{m} = mv^2/r$, $|q|vB = mv^2/r$. Every rearrangement is correct.
- $T = 2\pi m/(qB)$ and $f = qB/(2\pi m)$: v cancels correctly.
- Velocity selector (L1-02, L2-03): $\Sigma F = 0$, $qE = qvB$ is right there, because the forces are opposite. $v = U/(dB)$ is right.
- L3-01: $r = \tfrac{1}{B}\sqrt{2mU/q}$ follows from $v = \sqrt{2qU/m}$. Recomputed Δd = 4,006 cm.
- L3-04: $r^2 = 2mU/(qB^2)$ and $m = qB^2k/2$ are correct.
- L3-cyclotron: $E_\text{k} = nqU$ and $t = (n/2)T$.
- L2-06: $d = 2r = (2v/(qB))\,m$, so the mass ratio equals the distance ratio.
- Recomputed: L2-04 2,049 mm/s, r_α/r_p = 1,409. These are unchanged and agree with answers.py.
- Other changes are paragraph splits and a caption marker removal. Their physics is unchanged.
- Hash identical at start and end.
