VERDICT: PASS
CONTENT-HASH: 5d6ddd44c4b68caf

## Blocking

## Polish
- lessons/FY4/fy4-3/figures.py:208 (lesson.md:474 aria-label) — the auto figure's description says $\overline{F}_\text{v}$ "lähtee keulasta", but it is drawn from the car's rear side pointing back (figures.py:228) — say "lähtee auton takasivulta taaksepäin" (drawing is right: an arrow from the front face would cross the body).
- inquiry.json:84 — "Massa ei määrää vuorovaikutuksen voimaa" overstates: the masses do affect how large the collision force is, only not which cart gets more — write "Massa ei tee voimista erisuuria".
- inquiry.json:300 (siirto, Järkevyys) — "Auton moottorin on voitettava … 680 N": in this lesson's own model the forward force on the car is the road's force on the tyres — "tien voiman renkaisiin on kumottava …".
- lesson.md:365 — "kiveen vaikuttavat vain Maa ja jää" omits air (fair at this speed, C); optional "(ilmanvastus on hyvin pieni)".

## Checked
- Definitions (vuorovaikutus, voima, I and III law, inertia, kokonaisvoima, vakionopeus incl. rest) correct and consistent across theory, summary, glossary, feedback, exit ticket.
- Worked example (jet, 2·48 kN = 96 kN): third law for thrust, first law horizontally, lift vs weight stated; symbolic first, sig figs right.
- Sim recomputed: push a = 9,0 m/s², F = 130/110/100/90 N; slide s = 1,125/2,25/4,5 m, t = 0,75/1,5/3,0 s; frictionless 12 m in 4,0 s; F_μ·s = 45 J → 9,0 m for 5,0 N. Code matches; exp-1 locks v0, varies pinta, simState gives s, tl, vl.
- Collision data (figures.py): mirror readings, peak ≈ ±4 N at 0,10 s, ≈ ±1,4 N at 0,07 s; all three feedbacks right; sign convention right (B pushed right).
- Every choice item: exactly one correct; distractor feedback correct (horse–cart, book N/G pair, conveyor belt no friction).
- siirto 680 N and mistakes 160/420/0 right.
- Force diagrams (curling, luistelijat, auto, malli-lamppu, sim): rectangle bodies, G from centre, N from contact surface beside G, friction/drive at bottom corner, pushes ending at the body, third-law pair on separate diagrams, no point particles; forces red, velocity thin blue, nothing drawn as a force.
- Notation: vectors \overline{…}, \cdot, symbols in LaTeX (experiment labels render via KaTeX, checked in capture).
- Scope: FY4 "vuorovaikutus ja voima sekä Newtonin lait"; second law only referenced forward.
