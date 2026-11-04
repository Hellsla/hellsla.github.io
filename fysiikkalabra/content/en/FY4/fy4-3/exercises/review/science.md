VERDICT: FAIL
CONTENT-HASH: d621ebf2af8ee180

## Blocking
- solutions.md:264 (L3-04, Force diagram step) — A, the name in the text does not match the figure. The step still says "the force of the road $\overline{F}_\text{road}$ forwards", but the diagram right below it labels this force $\overline{F}_\text{t}$ (figures.json no longer maps F_t→F_road), and Find, Formula and Substitution all use $F_\text{t}$. — Write $\overline{F}_\text{t}$ in that sentence.

## Polish
- solutions.md:265–279 (L3-04) — each diagram has its own scale, and the 40 N and 30 N forces are drawn at the minimum length. So T (450 N) is 232 units long on the cart and 197 on the horse. A shared scale would show that the pair is equal.
- solutions.md:265–279 (L3-04) — only horizontal forces are drawn. Add "the weight and the normal force of the road cancel each other and are not drawn", as in L1-04.
- solutions.md:227 (L1-08) — "that is, against the child" is unclear; "(the rope pulls the child backwards)" is clearer.

## Checked
- Round 3. figures.json has no F_t, F_k or F_h map, so the diagrams show T, F_r, F_k and F_t, T, F_h. Given defines F_r = 410 N, F_k = 40 N (air resistance on the cart) and F_h = 30 N (air resistance on the horse). Formula and Substitution use the same symbols. The only mismatch is line 264.
- Physics: cart 450 − 410 − 40 = 0 and horse 480 − 450 − 30 = 0, with a = 0. The road's force on the hooves is friction, pointing forward. The third-law pair T is on different bodies. Answers: 450 N and 480 N, as in answers.py.
- The arrowheads and labels lie inside the figure (round 2, unchanged).
- The rest of the set is unchanged since rounds 1–2, and the answers recomputed there still hold.
- The hash was the same at the start and at the end.
