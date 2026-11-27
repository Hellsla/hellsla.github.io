VERDICT: PASS
CONTENT-HASH: e9bfb56e0d27391c

## Blocking
None.

## Polish
- Lint (not science): lesson.md:68 has a 20 px figure label (the "systeemit" sum label `F_AB + F_BA = 0`), which fails the lint (needs 24 px or more). The visual reviewer and developer should fix it. It is not a physics issue.
- Optional, class C: the Kaava section says "vuorovaikutusparin voimat eivät kumoa toisiaan", and the new subsection says their sum is zero for the system A+B. The subsection's "Vasta nyt voimat kuuluvat samaan systeemiin" already separates the two readings, so there is no contradiction. One clause could say that this sum does not stop either skater from accelerating, because each skater's motion depends only on the forces on that skater.

## Checked
Round 2: the revised subsection "Kaksi tapaa rajata systeemi" and figure "systeemit" were checked in fi, en and fi-easy. The three versions agree.
- Round-1 findings are fixed.
  - The internal-force reason comes first: the pair forces are internal, so the diagram of a system shows only external forces.
  - The sum $\overline{F}_{AB}+\overline{F}_{BA}=\overline{0}$ is tied to the pair belonging to one system.
  - The text states "Kitka jätetään huomiotta".
- Figure "systeemit":
  - Left (system A): $\overline{G}_A$ and $\overline{N}_A$ are equal, and $\overline{F}_{BA}$ points left. A accelerates left, which is consistent.
  - Right (system A+B): only the external forces $\overline{G}_A+\overline{G}_B$ and $\overline{N}_A+\overline{N}_B$ are drawn, with equal arrows. The net external force is zero, so the system's centre of mass stays at rest. This agrees with the skaters starting from rest.
  - The pair forces are not drawn as arrows. This is correct, because internal forces do not belong in the diagram.
  - The force diagrams show the right forces, with no velocity or acceleration drawn as a force.
- Third-law pairs: the support force pairs with the book's push on the table, and the weight pairs with the book's pull on the Earth. Both are correct in check-2, in the common-misconception box and in the lamp model answer.
- Recomputed from the task data:
  - Sliding distances: $s = v_0^2 m/(2F_\mu)$ gives $1{,}125$, $2{,}25$ and $4{,}5\,\text{m}$.
  - $F_\mu s = 45\,\text{N}\cdot\text{m}$, so $F_\mu = 5{,}0\,\text{N}$ gives $9{,}0\,\text{m}$ (exp-1 answer correct).
  - Hand force $m a + F_\mu = 90\,\text{N} + F_\mu$, which gives $110\,\text{N}$ on wood.
  - Sliding times $0{,}75$, $1{,}5$ and $3{,}0\,\text{s}$; frictionless run $4{,}0\,\text{s}$ at $3{,}0\,\text{m/s}$.
  - Worked example: $F_\text{v} = 2\cdot 48 = 96\,\text{kN}$.
  - Trailer task: $420+260 = 680\,\text{N}$, and all three mistake values (160, 420, 0) are really wrong.
- Predictions: each has exactly one correct option, and the feedback on the wrong options is right.
- The sim implements the stated model. It states its limits: constant friction, no air resistance, and a frictionless surface as a thought experiment. `simState` holds `s`, `tl` and `vl` at $v_0 = 3{,}0\,\text{m/s}$.
- Scope: stays within FY4 Newton 1 and 3; the full force diagram comes later.
- Class C only: Newton's first law is given without stating "inertial frame". This is acceptable at this level.
