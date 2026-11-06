VERDICT: PASS
CONTENT-HASH: 3327555d5e0791a2

## Blocking

## Polish
- solutions.md:350–382 (L2-08) — the boxes B and D are solved from ΣF_x = 0 with no force diagram or axis; one sentence ("rinteen suuntainen akseli alas rinnettä: F_μD − mg sin α = 0") or a small diagram would follow the chapter's fbd rule that the diagram comes before the equation (pedagogy's call).
- solutions.md:382 (L2-08) — add a one-line Järkevyys like the set's other solutions, e.g. "D:n kitka 123 N < yläraja 149 N ja B:n 30 N < 196 N, joten levossa olevat pysyvät levossa".
- Carried over: L2-05/L2-03 overlap; L3-05 fbd tag `error`.

## Checked
- Recomputed in one call: A μmg = 58,9 N; C 44,1 N; B static, F_μ = F = 30 N (bound 196 N); D mg sin 30° = 122,6 N (bound μ₀mg cos 30° = 148,7 N, so D really stays at rest). Order B < C < A < D is right and unique; answer string matches (1,2·10² N, 2 sf like 0,70 and 25 kg).
- Distractor logic catches the chapter's own warned mistake: taking static friction as μ₀N makes B the largest (196 N); ordering by mass or by μ gives other orders, as the solution says.
- The prompt names the quantity and direction ("kitkavoiman suuruuden mukaan pienimmästä suurimpaan"), as docs/exercise-types.md requires for Järjestäminen.
- Assumptions stated in the task: only weight, normal force and friction (B also a horizontal push), no air resistance; N = mg on the floor justified in the Periaate.
- Uses only fy4-6 content (μN, static friction up to μ₀N, slope components) and fy4-4/fy4-5 equilibrium.
- Rendered (preview build, 390 px, solution forced open, own script): no KaTeX span over 260 px, no overflow. Physics from text.
- Hash 3327555d5e0791a2 at the start and at the end.
