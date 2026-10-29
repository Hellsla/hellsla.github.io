VERDICT: FAIL
CONTENT-HASH: 9ea0a6d10fb17aff

## Blocking
- inquiry.json:177, 280 — the measure label `"ΣF_x (N)"` is plain text and shows raw on the page as "ΣF_x" with a visible underscore; this breaks the teacher's rule that all symbols are LaTeX — write `"$\\Sigma F_x$ (N)"` and likewise the a_x, v_x and m labels.
- lesson.md:597 (Yleinen virhekäsitys) — B: "Ylöspäin heitetty pallo nousee, vaikka siihen vaikuttaa vain alaspäin osoittava paino" holds only without air resistance; check-1 states the condition, this text does not — add "kun ilmanvastus jätetään huomiotta".

## Polish
- assets/sims/fy4/fy4-4/sim.js:113 — the string is drawn sloping from the cart top down to the winch, while the model and diagram say a horizontal pull; draw it at one height (e.g. both ends at `TOP - 9`).
- lesson.md:434 — units "(N)", "(kg)", "(m/s²)" in prose are plain text, while the rest of the lesson writes units in LaTeX; use `$\text{m/s}^2$`.
- inquiry.json:404, 410 — "yksikköön m/s" plain text; `$\text{m/s}$` to match the rest.

## Checked
- Recomputed in one script: worked example a = 1,02 m/s² (G = 4708,8 N, wrong-route 10,8), siirto 7000 N and its three mistake values, check-2 1,0 (1,67/2,33), check-3 1,7 m/s² and N = 11,8 N: all agree.
- Sim: a = ±F/m, constant force, no friction stated in `model`; exp-3 (1,5 m/s, 2,0 N left, 1,0 kg) stops at 0,75 s and reverses within the 1,0 s run, so pred-3 feedback holds; right pull ends at 0,754 s, exp-1/exp-2 runs within the track; fitted slope exact; simState gives sumFx, a, v, m.
- Experiments isolate the varied parameter (locked alku/suunta/m, alku/suunta/F, alku/F/m).
- Figure "kokonaisvoima" to scale: T/G = 0,765 (60/78,5), F_μ = T/3, ΣF = 2/3 T, drawn apart and green; "esimerkki" T/G = 1,10; "nosturi" lengths agree with each state.
- Valitse: exactly one correct (T > G while slowing down going down); b, c, d each carry one error, feedback right.
- Force diagrams per docs/force-diagrams.md: rectangle body everywhere (also sim), G from centre, N from the contact face apart from G, T from the top or side, friction from the bottom edge; no point-particle diagram; v blue, a orange, forces red; vectors \overline{F}; \cdot, no ×.
- Truck explanation names the road's forward force on the tyres and mass, not weight; condition "same force" stated.
- Exit ticket answers correct.
