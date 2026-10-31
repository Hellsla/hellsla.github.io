VERDICT: PASS
CONTENT-HASH: c05c1b51f1ef1680

## Blocking

## Polish
- solutions.md:189 (L3-01) — The asked force comes from the pulley's balance, yet the pulley's diagram ("kaksi $T$ alas, $F_\text{akseli}$ ylös") is the only one left in words. — Add a third spec block (`---`): the pulley as a body, both rope forces down, $F_\text{akseli}$ up, `a 0`.
- solutions.md:102–111 (L2-01) — Both forces on the lower crate are enlarged under the 40 % rule: $T_2$ is drawn 27,5 px and $G_2$ 26,5 px, against a true ratio of 1,12. The upward net force is barely visible. The order is kept and the text claims no lengths here, so nothing is wrong; fbd.py's enlargement could keep the ratios within one body.
- Earlier polish (two rope ends both named $T_2$ in L2-01; "voima köydestä … akseliin" in L3-01): still open, and the diff does not touch it.

## Checked
- All 12 new `voimakuvio` blocks rendered (fbdspec.draw) without error. I viewed them in a screenshot and measured every arrow from the SVG.
- Every spec value recomputed from the task text: L1-01 14,715 and 3,0; L1-02 5,886 and 4,686; L1-03 9,81, 3,924 and 2,803; L1-04 29,43 twice; L1-05 9,81, 19,62, 12 and 8,0; L2-01 880,8, 490,5, 330,3 and 294,3; L2-02 4,905, 9,81 and 6,54; L2-03 29,43, 19,62, 20 and 8,0; L2-04 5,886, 8,901 and 7,086; L3-01 7848, 11 772 and 9418; L3-02 9,81, 4,321 and 3; L3-03 14,715, 4,905 and 3,679. Each body's forces sum to m·a along its drawn a.
- Directions and a-arrows match each step's positive direction. The lighter hanging body accelerates up and the heavier one down.
- Equal tensions are drawn equal across bodies on one scale. $T_1$ is the longest arrow in L2-01 (T₁/G₁ drawn 1,79, true 1,80).
- In L2-01, $T_2$ acts down from the upper crate's bottom face, offset from $G_1$, and up at the lower crate's top face.
- Each body has its own rectangle diagram. No third-law pair sits on one diagram, and a is drawn off the body.
- A normal force appears only where `pinta` gives a surface, never on a hanging body.
- The generated descriptions name the same forces as the step texts.
- Text and answers are unchanged since the PASS.
- Hash c05c1b51f1ef1680 at the start and at the end.
