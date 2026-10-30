VERDICT: FAIL
CONTENT-HASH: bca89d9de1f19d26

## Blocking
- content/fi/FY4/fy4-6/lesson.md:424, :418, :197 — **B.** "Rinteellä … $N = mg\cos\alpha$" (Tiivistelmä, virhekäsitys) and "Kohtisuoran komponentin mukana pienenee tukivoima" have no condition. The prerequisite chapter teaches angled pulls, which change $N$. — Fix: add "kun pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima eikä kappale kiihdy siinä suunnassa". The glossary's *kalteva taso* entry needs the same.
- lessons/FY4/fy4-6/figures.py:197, :223, :265 (*kalteva*, *esimerkki*, *valitse-a…d*) — **A, drawing rule.** The tail of $\overline{N}$ is put where the $\overline{G}$ shaft crosses the bottom face (gaps 4.5, 0.3 and 0.2 units), so N seems to grow out of G. This breaks "N from the contact surface, apart from G", and *valitse-a* is the model answer. — Fix: start N on the uphill side, about bc + 16·t, as *virhe*, *malli-veto* and the simulation do. Extend fbd.py's separation check to this crossing point.

## Polish
- inquiry.json:270 vs :178 — wood's friction coefficient is given as 0,3–0,5 in one place and 0,3–0,6 in the other. Use one range.
- inquiry.json:442 — check-2's *Järkevyys* mixes kinetic and static friction ("liukuminen alkaisi").
- inquiry.json:119, :193 — "kulma α" uses a plain Unicode α. Write "kulma $\alpha$".
- lesson.md, *Kitka ei aina vastusta liikettä* — "Ainoa vaakasuora voima" comes before air resistance is set aside. Add the condition in the sentence.

## Checked
- Every number in the lesson and inquiry recomputed in one script with my own formulas: all agree, and each stays inside its tolerance when rounded.
- The 26°/27° slip pair is consistent with μ₀ = 0,50, and both bracketing tangents pass.
- sim.js implements the stated model and its boxes state its limits. Exp-1 and exp-2 each isolate their varied parameter, and simState gives the measured keys.
- Force-diagram checklist on every figure and the simulation: rectangles, G from the centre, friction at the outline, dashed components, F red, v blue, a orange, equations match the axes. Each distractor has exactly one error.
- Notation uses \overline and \cdot; no ×, \vec or \mathbf.
- Exactly one correct option in every choice item, with correct feedback. The exit ticket and model answers agree with the theory.
