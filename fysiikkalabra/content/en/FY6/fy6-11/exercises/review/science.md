VERDICT: PASS
CONTENT-HASH: c8602335ddec9591

## Blocking

## Polish
- exercises.json:267 (fy6-11-L2-08) — the task text and feedback name the electric force $\overline{F}_\text{e}$, but the option figures (`_pick` in lessons/FY6/fy6-11/figures.py) label it $\overline{F}_\text{s}$ (the Finnish subscript) — check the English figures; if they show $\overline{F}_\text{s}$, use one symbol in text and figure.
- solutions.md (fy6-11-L3-03 Reasonableness) — "about one fifth of the weight": $\tan 10^\circ = 0.18$, nearer one sixth — write "under a fifth".
- exercises/review/packet-science.md — the exercise brief is empty, and the lesson's terms (electric field, field line, test charge…) are not yet in glossary.json, so notation was checked against internal consistency only (consistent apart from the item above).

## Checked
- All 19 numeric answers recomputed in one script with my own formulas ($E = F/q$, $E = U/d$, $qU/d = mg$, $v = \sqrt{2eU/m}$, $q = mg\tan\alpha/E$, $y = \tfrac{1}{2}a(L/v_0)^2$): all agree with exercises.json and answers.py.
- L2-05: products $E d$ = $408$, $393$, $408$, $390$, $408$, $394\,\text{V}$, mean $400\,\text{V}$; L2-07 deviations $0.7$, $1.2$, $2.0$, $3.7$, $45\,\%$, uniform points $x \le 6\,\text{cm}$, mean $2.98 \cdot 10^{4}\,\text{V/m}$ vs $U : d = 3.0 \cdot 10^{4}\,\text{V/m}$.
- L3-04 Millikan: charges $3.20$, $4.84$, $1.59$, $6.38$, $4.83 \cdot 10^{-19}\,\text{C}$, $n = 2, 3, 1, 4, 3$, ratios $1.60$–$1.61$, $e = 1.60 \cdot 10^{-19}\,\text{C}$; sign negative (force up towards the positive top plate): correct.
- L3-05: $F/G \approx 1.4 \cdot 10^{3}$, $a = 1.33 \cdot 10^{4}\,\text{m/s}^2$, $y = 1.67\,\text{mm} < 2.5\,\text{mm}$; doubled voltage hits at $8.7\,\text{mm} < 10\,\text{mm}$: correct.
- L1-09 MAFY lookup: air $3.0\,\text{kV/mm}$ gives $7.5\,\text{kV}$, no rounding across the limit (P7 c).
- P7: L3-01 $338\,\text{V}$ to three s.f. from $450\,\text{V}$; L3-02 two s.f. from $50\,\text{V}$, $1.0\,\text{cm}$; every rounded answer within tolerance.
- L2-08 against the force-diagram checklist: interactions Earth and field only (vacuum), negative charge gives $\overline{F}$ against $\overline{E}$; $F_\text{e} : G = 2.04$ matches the drawn arrow ratio 2; exactly one correct (B); A (force along field), C (velocity drawn as force, forces otherwise right) and D (weight omitted) each carry one error, the one their feedback names.
- L1-06, L1-07: one correct option each; feedback right (field-line density, $\overline{F} = q\overline{E}$ for negative $q$, plates' signs).
- Figure fq-graph: fitted line through the origin (physical reason stated) at $30\,\mu\text{N/nC}$, crossing $(4.0\,\text{nC};\ 120\,\mu\text{N})$; least-squares $29.9$; alt text carries the points.
- Scope: Coulomb force, uniform field, $E = U/d$ within FY6; FY4 kinematics and Newton's second law used as prerequisites; magnitudes realistic (membrane $70\,\text{mV}$, electron $1.4\,\%$ of $c$).
