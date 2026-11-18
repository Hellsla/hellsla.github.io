VERDICT: PASS
CONTENT-HASH: 36a3fdd60977dd35
SCOPE: delta (work queue 8g round 2: "pieneneminen" in fy4-10-L2-02 Kaava) from previous PASS 504b94a242b0ab65

## Blocking
None.

## Polish
- solutions.md:63-64 (fy4-10-L2-02 Kaava) — capital letter after the semicolon is still there ("…; Liike-energian pieneneminen"); fix: "…; liike-energian pieneneminen on …" (earlier polish, not fixed by this change).
- Same task, Kysytty — "muiksi energiamuodoiksi muuttuva liike-energia $\Delta E$" is fine, but the course wording is "sisäenergiaksi ja ääneksi"; optional: "sisäenergiaksi ja ääneksi muuttuva liike-energia".
- Packet checks list `layout 360 px` and `layout 390 px` as FAIL (lesson-level checks.txt, written 15:57); not caused by this diff and not re-run here, but a clipped row at phone width must be cleared before the visual review.
- Earlier polish on fy4-10-L2-10 (wording "häviää", two results on one source line) not part of this diff and stands.

## Checked
- Round 1 blocking fix verified: $\Delta E = E_\text{k,ennen} - E_\text{k,jälkeen}$ is now called "pieneneminen", which matches its sign (positive $717{,}2\,\text{J}$ = decrease) and the Kysytty line; the old word "muutos" would have implied a negative value.
- Arithmetic: $v' = 85 \cdot 6{,}0 / 160 = 3{,}1875\,\text{m/s}$; $\tfrac12 \cdot 85 \cdot 36 = 1530\,\text{J}$; $\tfrac12 \cdot 160 \cdot 3{,}1875^2 = 812{,}8\,\text{J}$; difference $717{,}2\,\text{J}$ correct.
- Kaava order unchanged and good: $p_\text{ennen} = p_\text{jälkeen}$, symbolic $v'$, then symbolic $\Delta E$ before substitution.
- Finnish in the changed word correct; glossary and energy wording consistent (energy to other forms, not "häviää").
- No number, answer, tolerance, task, id or figure changed; text-only change.
- Captures opened: none (the available shots are 1280 px, and the change is one word).
