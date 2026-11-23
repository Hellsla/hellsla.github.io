VERDICT: PASS
CONTENT-HASH: 6e8c288a49a9ffda

## Blocking

## Polish
- solutions.md:237 (L3-04 Kaava): $r$ stands first for the measurement distance ($P = 4\pi r^2 I$) and then for the unknown ($r^2 = \tfrac{P}{4\pi I_\text{raja}}$). Name the unknown $r_\text{raja}$, as L3-05 does.

## Checked
- The diff rewrites the Kaava steps into aligned chains that start from $L = 10\lg(I/I_0)\,\text{dB}$, $I = P/A$ with $A = 4\pi r^2$, or $I = I_1 + I_2$, and it splits some paragraphs. The files on disk hold proper `aligned` blocks; the packet's diff dropped `&` and `\\`. Sijoitus, answers and tolerances are unchanged.
- L1-03 and L1-09: the solution goes from the level equation to $\lg(I/I_0) = L/(10\,\text{dB})$ to $I = I_0\cdot10^{L/(10\,\text{dB})}$, as the lesson does.
- L1-05: the difference of two levels gives $10\,\text{dB}\cdot\lg(I_2/I_1)$, because $I_0$ cancels. Right.
- L2-01 and L2-02: these are right, and adding intensities is the rule for independent sources the lesson states.
- L2-03, L2-06 and L3-02, inverse square: $I_2/I_1 = r_1^2/r_2^2$ from $I = P/(4\pi r^2)$ with the same $P$. The signs are right, including $L_\text{malli} - L_1 = -10\,\text{dB}\cdot\lg[(r_2/r_1)^2]$.
- L2-04 ($I = NI_1$, so $N = 10^{\Delta L/(10\,\text{dB})}$), L3-01 (the crowd plus the announcement, by summing intensities) and L2-07 ($k = 10^{\Delta L_\text{ka}/(10\,\text{dB})}$) are right.
- L3-05: $I_2$ is scaled by $(r_2/r)^2$, $Ir^2 = I_\text{raja}r_\text{raja}^2$, and the sum falls off as $1/r^2$ because both terms do. Right.
- L2-05 Periaate: the distance sequence now sits in a display block. This is layout only; the count of 4 doublings is unchanged.
- Recomputed in one script: 3,16·10⁻³; 2,55·10⁻⁴; 86,45; 89,76; 72,96; 3,98; 82,79 and 84,62; 15,8 m; 2,51·10⁻⁵; 5,03 mW; L3-05 84,93 dB and 44,6 m. All agree with the solutions.
- Hash 6e8c288a49a9ffda at the start and at the end.
