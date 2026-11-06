VERDICT: PASS
CONTENT-HASH: fb4c9e7694ba0259
Round: 1

## Blocking
(none)

## Polish
- solutions.md:261-265 (L2-08) — "ratkaistaan paine tilavuudella $V_2$" then sets $V_2 = 20$ ml, while the task's end volume is 10 ml (named $p_3$). Name the intermediate point differently (e.g. $p$ at $V = 20$ ml) or say that 20 ml is a check point read off every graph.
- solutions.md:147 (L2-05) — mirror reason for B (fixed air amount) still optional. Carried over.
- L1-07 is still the third plain Boyle compression at level 1; exercise-bank plan line 70 still names "ruiskumittaus → linearisointi" instead of L2-07. Carried over.

## Checked
- New task L2-08 (kuvaajan valinta), recomputed: pV = 4000 kPa·ml → 100/200/400 kPa at 40/20/10 ml; option B is the only curve through these points.
- figures.py pick-*: all four on one grid (V 0–45 ml, p 0–450 kPa, to scale as stated). A: line (40;100)–(10;400) gives 300 kPa at 20 ml, as the feedback says; C: constant 100 kPa; D: (10;25)–(40;100) passes the origin, i.e. p ∝ V, as its feedback says.
- Exactly one correct option; each distractor really wrong and catches a named mistake: A is the lesson's own warned one ("kääntäen verrannollisuus ei ole laskeva suora"), C constant T read as constant p, D dependence read the wrong way.
- Conditions stated in the task: tip closed (fixed amount), pushed slowly, temperature constant; solution Periaate states both conditions; feedback C mechanism (more wall collisions) right.
- Option texts are "Kuvaaja A–D" only; figure descriptions give the same values as the graphs; nothing in form reveals B beyond the physics.
- Within fy3-9 (Boyle, (V,p) graph shape); level 2 fits.
- Renders: checked L2 screenshots 12–13 at 1280 px (option graphs legible; A and B share end points as intended; solution formulas short). Phone width not rendered: the inline chains (≈ "p₂ = 100 kPa·40 ml / 20 ml, eli p₂ = 200 kPa") judged from text to fit ~300 px.
- answers.py and the other tasks unchanged since the round-3 PASS (commit touches exercises.json, solutions.md, figures.py only).
- Hash identical at start and end.
