VERDICT: PASS
CONTENT-HASH: 5c47178de9581cdf
SCOPE: delta numbers from 005ee7bc5d2c433f base 3076572
Delta (queue 8g): the Kaava step of fourteen solutions now starts from the basic equations (Coulomb's law per force, charge conservation, force balance) and solves the unknown in aligned rows. No data, substitution or answer changed.

## Blocking
- none

## Polish
- solutions.md fy6-10 L3 zero point between the charges and L3 zero point beyond q₂, Kaava: the third charge enters as $q$ in $F_1 = k\,Q_1 q : x^2$. The Periaate says its sign does not matter, so a negative $q$ would give a negative "magnitude". Fix: write $\lvert q \rvert$ as the lesson's $\lvert q_1 q_2 \rvert$ does.
- solutions.md L3 zero point beyond q₂, Kaava: the step from $F_1 = F_2$ to $\tfrac{x}{x-d} = \sqrt{\cdot}$ skips the row $\tfrac{\lvert q_1 \rvert}{x^2} = \tfrac{\lvert q_2 \rvert}{(x-d)^2}$ that the other zero-point solution shows. Fix: add that row.
- solutions.md weight-balance task, Kaava: $G$ is the weight here, and in the electron–proton task $G$ is the gravitational constant. Both are correct in their own task, but a reader moving between them could mix them up. Fix (optional): keep $G = mg$, and name it "paino" in the Periaate, which already does so.

## Checked
- Every new Kaava chain is algebraically right, and each one ends in the formula its unchanged substitution uses.
- Contact sharing: $Q_1 + Q_2 = Q + Q$ states charge conservation, which matches the lesson summary.
- Hanging balls: $T\cos\theta = mg$ and $T\sin\theta = F$ with θ measured from the vertical (half the apex angle) give $F = mg\tan\theta$, the right force balance.
- L2-09: $F = kq^2 \cdot \tfrac{1}{r^2}$ makes it explicit why the slope of the $(1 : r^2, F)$ line is $s = kq^2$.
- Ratio tasks: $F_\text{B} : F_\text{A} = q_\text{B} : 20\,\text{nC}$ and $q_\text{A} : r_\text{A}^2 = q_\text{B} : r_\text{B}^2$ are correct, with $k$ and the common charge cancelled.
- One Python script recomputed every substitution: 4,0 nC; 6,36 cm; 0,576 mN; 0,202 mN; 36,9 nC; 0,719 mN; 2,27·10³⁹; 8,0 cm; 33,85 cm; 40,9 nC; 30 nC; 80 nC; 24,7 nC; 69,8 nC. All agree with the solutions, and answers.py is unchanged.
- Notation follows the lesson: $k$, $\lvert q_1 q_2 \rvert$, $r$, overline-free magnitudes.
- Content hash checked at the start and the end.
