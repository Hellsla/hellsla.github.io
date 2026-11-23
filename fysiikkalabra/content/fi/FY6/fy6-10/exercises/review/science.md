VERDICT: PASS
CONTENT-HASH: 7165b6789e1e247e
SCOPE: delta numbers from d545a6f33a79d74d base 3076572
Delta review of the Kaava steps, which now start from the basic equations (queue 8g). Categories and base come from `reviews.py` scope for science.

## Blocking

## Polish
- solutions.md:115 — the zero-force point: $F_1 = k\,Q_1 q : x^2$ is a magnitude, but the principle says $q$ may have either sign. Writing $\lvert q \rvert$, as the L3 outside-point solution does with $\lvert q_1 \rvert$, keeps both forces non-negative. The result does not change.

## Checked
- The hash was 7165b6789e1e247e at the start and at the end. I judged only the diff: 14 Kaava lines in solutions.md.
- Each new chain starts from the basic law: charge conservation $Q_1 + Q_2 = Q + Q$, Coulomb's law for each force, $F_\text{e} = G$ with $G = mg$, $F_1 = F_2$, $T\cos\theta = mg$ and $T\sin\theta = F$. Each is then solved in symbols to the form that is substituted. Every algebraic step is right.
- Hanging balls: the tension components and the electric force give $\tan\theta = F : mg$ without double counting, and $r = 2L\sin\theta$ is right.
- The ratio steps ($F_2 : F_1 = r_1^2 : r_2^2$; $q_\text{A} : r_\text{A}^2 = q_\text{B} : r_\text{B}^2$; $F_\text{B} : F_\text{A} = q_\text{B} : 20\,\text{nC}$) follow from the law, with $k$ and the common charge cancelling.
- The notation matches the brief: $F = k\,\lvert q_1 q_2 \rvert : r^2$, $k$, $\overline{F}$ for vectors, magnitudes plain. $G$ means weight in one task and the gravitational constant in a separate task, and each is clear in its own context.
- I recomputed the unchanged substitutions in one script, and all agree with the solutions: 4,0 nC; 6,36 cm; 0,576 mN; 0,202 mN; 36,9 nC; 0,719 mN; 2,27·10³⁹; 8,0 cm; 24,7 nC; 69,8 nC; 33,85 cm; 40,9 nC; 30,0 nC; 80 nC.
- No answer, unit, tolerance or task text changed.
