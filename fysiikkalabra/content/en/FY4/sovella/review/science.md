VERDICT: PASS
CONTENT-HASH: 2ef567fe6edbae93

## Blocking

## Polish
- solutions.md (fy4-s3 d, Principle) — "The velocity of an object changes only when a force acts on it (Newton's first law)" — "only when the net force on it is not zero".
- solutions.md (fy4-s3 c, Reasonableness) — "It is large but typical for a rear-end collision, and … the body can withstand it" has no basis in the task or a source — "it is large; the force is spread over the whole seat back, and the peak force is larger than the average", without the claims of typicality and tolerance.
- solutions.md (fy4-s2 c, Formula) — the step opens with the combined equation "as in part b"; one clause "$E_{\text{p}0} + W = E_\text{k}$ with $W = -F_\text{res}s$, the same work as in b" would keep the basic-equation order of part b.

## Checked
- Hash 2ef567fe6edbae93 at start and end. Captures: none opened (en judged from the text and the packet).
- Recomputed in one script: line fits pass through $(0; 2.105)$–$(8; 5.221)$ and $(0; 1.899)$–$(8; 3.856)$, so the read points are on the lines; $\mu_\text{A} = 0.0301$, $\mu_\text{B} = 0.0449$; the accepted slope ranges give $0.028$–$0.032$ and $0.043$–$0.046$, inside the tolerances; $a_0 = 0.449$, $\mu_\text{A0} = 0.0241$, accepted $a_0$ range inside its tolerance.
- s1: the drag constant $k = 0.00432\,\text{s}^{-2}\text{m}^{-1}$ matches $\tfrac12\rho C_\text{d}A/m$ ($0.5\,\text{m}^2$, $72\,\text{kg}$); air resistance overestimates $\mu_\text{A}$ more (faster run), so the conclusion holds; the angle uncertainty $\pm 0.1^\circ$ gives $0.0017$; the FBD fence agrees with the data.
- s1 Kaava: $\Sigma F = ma$, $F_\mu = \mu N$, $N = mg\cos\alpha$, then $\mu = (g\sin\alpha - a)/(g\cos\alpha)$; symbolic to the end.
- s2: $v = 17.16\,\text{m/s} = 61.8\,\text{km/h}$; $F_\text{res} = 29.08\,\text{N}$ (4.8 % of the weight, 57 % of $E_\text{p}$ lost); $13.57\,\text{m/s}$; energy principle written with signed $W = -F_\text{res}s$; the cable force does no work (perpendicular); part d's separation of wheel friction and air resistance is right.
- s3: $v' = 7.86\,\text{m/s}$ from $W = -\mu mgs$; $v_\text{B} = 13.64\,\text{m/s} = 49.1\,\text{km/h}$; kinetic energy lost $42\,\%$ $= m_\text{A}/(m_\text{A} + m_\text{B})$; $F_\text{avg} = 4455\,\text{N} = 6.7\,mg$; friction impulse at most 11 % of $p_\text{B}$, $v_\text{B} \le 15.2\,\text{m/s}$; directions of the assumptions in e right.
- Tolerances and rounding: every answer inside its tolerance with the data's figures; "Hyväksytään myös" ranges stay inside.
