VERDICT: PASS
CONTENT-HASH: 2eca79ed0e1b7452

## Blocking

## Polish
- s3 b: also mark the point $(2{,}0;\ 1{,}86)$ in the figure. s3 d: say that $36\,\text{cm}$ is extrapolated. s5 d: criteria 3 and 4 overlap. (All carried from earlier rounds.)
- s2 c: "satoja miljoonia kilogrammoja" uraania. $3{,}5\,\text{kg} \cdot 5{,}1 \cdot 10^{7} \approx 1{,}8 \cdot 10^{8}\,\text{kg}$, so "noin $10^{8}\,\text{kg}$" would be exact.

## Checked
- Hash 1664e18128b1e37b at the start, 2eca79ed0e1b7452 at the end. The edit in between (f7ec48a4b7, s3 d Vastaus and its conclusion criterion) is better physics. At $36\,\text{cm}$ the net rate equals the background, which can still be told apart. Beyond that the background's random variation hides it. The solution and the criterion say the same. This was a full review. Since 64d4935, solutions.md changed (Kaava blocks, split paragraphs) and the s3 d criterion changed. answers.py is unchanged.
- One script recomputed 23 values from the task data with my own formulas (s1 a, b, d; s2 a, b, d, e, c; s3 $\tfrac{1}{\sqrt{R}}$, $K$, $r$, $H$; s4 a–d; s5 a, c, d). All of them match answers.py and the text.
- The new Kaava derivations are right: $Q = \Delta m\,c^2$; $P = AQ$ and $A = \lambda N$; $E = NQ$ with $N = At$; $R = \tfrac{K}{(r+d)^2} = R_\text{t}$; $Y = \tfrac{M_\text{He}}{M} = \tfrac{2N_n}{N_n+N_p}$ (equal nucleon masses, stated); $N_n + N_p = 7$, conserved because each decaying neutron becomes a proton; $E = Pt$.
- Physics and scope: the O I levels (1,97 eV and 4,19 eV) and their lifetimes are real. The Pu-238 alpha energy, $w_\text{R} = 20$ and $w_\text{T} = 0{,}12$ are right. The $\sqrt{N}$ counting statistics and the background per minute are right. The weak interaction, $d \to u$, the ratio 1:6 at 1 s and $T_{1/2} = 609\,\text{s}$ are right. The Oklo values (0,440 %, 100 kW, 150 000 a) and Pu-239 → U-235 are right. Everything is inside FY8's contents.
- Rubrics: every criterion asks only what its part gives and asks, and practice.py check reports the points add up. Hyväksytään myös accepts the other correct methods ($e^{-\lambda t}$, $r+d$ for the dose, $hc = 1240\,\text{eV nm}$, energy in joules).
- No data is presented as real measurement without a source. s3 is a class measurement inside the task's story, and the source notes name NIST, NASA, AME2020 and NNDC.
- The split paragraphs keep every claim. The rounding reasons hold.
