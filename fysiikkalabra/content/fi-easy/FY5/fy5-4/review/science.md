VERDICT: PASS
CONTENT-HASH: f368ccd18e65ea2e

## Blocking

## Polish
- inquiry.json pred-2 correct feedback — "Kitka osoittaa yhä kohti keskipistettä" holds only at the instant the grip fails; in the model the friction stays perpendicular to the velocity, towards the centre of the car's own wider turn (sim.js `psi += w*h`) — "Kitka osoittaa yhä kohtisuoraan nopeutta vastaan, kaarroksen sisäpuolelle".
- inquiry.json pred-1 `reveal.min` 3 — the exp-1 intro lists 5, 10, 15, 20 … m/s, so after three rows the 20 m/s row the feedback quotes ($12\,\text{kN}$) may not have been recorded yet — make it 4 (or say the order 10, 20 first).
- lessons/FY5/fy5-4/lesson-answers.py `siirto-v-1` comment "N taken as 2G" — the fed-back mistake is ΣF = mg; align the comment (no student-visible effect). The `sim-an/sim-F` loop could also print 25 and 30 m/s now that exp-1 records them.

## Checked
- Round-1 polish on lähtökitka resolved: the `calc` box now names "täysin kehittynyt lepokitka eli lähtökitka … $\mu_0 N = \mu_0 mg$" (guardrail P8).
- One script recomputed every number from the task texts with my own formulas, matching lesson-answers.py: example $F_\mu = 6000\,\text{N}$, $\mu_0 \ge 0{,}5097 \to 0{,}51$ (rounded up); Koe 1 $750/3000/6750/12\,000/18\,750/27\,000\,\text{N}$ vs $11\,772\,\text{N}$, pito 1,1,1,0,0,0; $v_\text{max} = 19{,}81\,\text{m/s}$, mistakes $22{,}15$, $392{,}4$; Koe 2 ratio $0{,}920$; siirto $15{,}34$ ($18{,}79$, $10{,}85$); check-2 $148\,\text{N}$ ($47{,}12$, $294{,}3$); check-3 $T = 0{,}765\,\text{N}$, $N = 1{,}67\,\text{N}$; exit ticket 9; graph 2/8/18 and 1/4/9 m/s².
- New exp-1 rows: slider 5–30 step 1 reaches 25 and 30; `min` 6 equals the six listed speeds, and pred-2 reveals only after them.
- Slide emulated with sim.js's integrator (r = 50 m, dry): slide radius $v^2/(\mu_0 g)$ = 51, 80, 115 m; greatest distance from centre 52 m at 20 m/s (stays on asphalt, edge 57,3 m), 67,7 m at 25 and 30 m/s (crosses the edge, stops at the 67,7 m limit). So the instruction to press Käynnistä at 25 and 30 m/s shows the predicted motion; spec and comments agree.
- Koe 1 locks r, m, surface and varies v; Koe 2 locks r, surface, v and varies m; simState carries an, Ftarve, Fmax, pito.
- Exactly one correct option in kertaus, pred-1–3, virhe, valitse, check-1; distractor feedback is right physics.
- Force diagrams (kaarre, nyppylä/notko, example, solution blocks, check-3 criteria): only real forces, N = G with horizontal a, N < G on a crest, N > G in a dip; acceleration drawn apart in orange.
- Scope: no angular quantities; centrifugal force treated as a misconception, rotating-frame fictitious force correctly limited.
- Hash at start and end: f368ccd18e65ea2e.
