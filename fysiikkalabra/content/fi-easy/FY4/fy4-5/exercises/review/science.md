VERDICT: PASS
CONTENT-HASH: 0006451fe6b8af50
## Blocking

## Polish
- content/fi-easy/FY4/fy4-5/exercises/solutions.md:357 (L2-08 Vastaus, unchanged line) — "kulmaan $53^\circ x$-akselista" runs the angle and the axis name together in one formula — write $53^\circ$ $x$-akselista.
- content/fi-easy/FY4/fy4-5/exercises/solutions.md:300-302 (vinoveto multiple choice) — the new paragraph opens "Se on juuri niin suuri …", whose referent (tukivoima) is in the previous paragraph — start it "Tukivoima on juuri niin suuri …".
- content/fi-easy/FY4/fy4-5/exercises/solutions.md:318 (L2-05 Kaava) — "Newtonin toinen laki: $\Sigma F = ma$" is written as magnitudes; for the two-axis balance $\Sigma F_x = 0$ and $\Sigma F_y = 0$ (as in the other rewritten steps) says it more exactly.
- content/fi-easy/FY4/fy4-5/exercises/solutions.md:42-46 (kirja seinää vasten) — the friction holding a book at rest is lepokitka, "juuri niin suuri kuin paikallaan pysyminen vaatii" (the Järkevyys says so); naming it lepokitka once, as fy4-6 does, would match physics-guardrails (Friction).

## Checked
- Delta only: nineteen Kaava rewrites and three paragraph splits; no number, answer, tolerance, task or id changed.
- Every rewritten Kaava step now starts from $\Sigma F_y = ma_y$ / $\Sigma F_x = ma_x$ or from the vector sum $\Sigma\overline{F} = \overline{F}_1 + \dots$, states $a = 0$ where the body is at rest or moves uniformly, and solves symbolically before Sijoitus.
- Component $T_x = T\cos\alpha$ from the right triangle, $\cos\alpha = T_x/T$: right.
- Perpendicular forces: $a = \sqrt{F_1^2 + F_2^2}/m = 50/50 = 1{,}0\,\text{m/s}^2$ recomputed; substitution now into the last symbolic form.
- L2-08: $a = \sqrt{(F_{1x} + F_{2x})^2 + (F_{1y} + F_{2y})^2}/m = 10/2{,}5 = 4{,}0\,\text{m/s}^2$ recomputed; direction $53^\circ$ from $+x$.
- Friction decelerations: $-F_\mu = m a_x$, $F_\mu = m(v_0 - v)/\Delta t = 1{,}9\,\text{N}$ and $a = 30/12 = 2{,}5\,\text{m/s}^2$ recomputed; signs right.
- L2-05 ring: dividing $F_\text{B}\sin\alpha = F_\text{C}$ by $F_\text{B}\cos\alpha = F_\text{A}$ gives $\tan\alpha = F_\text{C}/F_\text{A}$: the added step is right.
- Elevator phases: $T - mg = ma_y$, $mg = 784{,}8\,\text{N}$, phase means 880,7 / 784,7 / 689,7 N recomputed.
- Pulled sled from data: $a = 4{,}01/5{,}0 = 0{,}802\,\text{m/s}^2$; $N = mg - T\sin\alpha$ with $a_y = 0$ stated.
- Captures opened: none (judged from the text and the packet).
