VERDICT: FAIL
CONTENT-HASH: 65a72267ecdbb241
Review of the recognition chart (queue 9c) and the term change against the version passed at 28a3c34741ddd22d; full on the chart, delta on the rest.

## Blocking
- **Term, unit.md line 239 (Formula section): "In free-body diagrams $\overline{F}_\mu$ stands for either kind of friction, static or kinetic."** The rename left this one "kinetic"; the same paragraph and the chart now say sliding friction. Fix: "static or sliding".

## Polish
- Row 9 "air resistance, speed levels off → $F_\text{v} = G$" holds for a vertical fall (as the Formula section's terminal velocity); "falling" in the sign would rule out a cyclist or car.

## Checked
- Every row: $a = 0 \Rightarrow \Sigma\overline{F} = \overline{0}$; $a \neq 0 \Rightarrow \Sigma\overline{F} = m\overline{a}$; $\Sigma M = 0$ for a rod; one equation $\Sigma F_i = m_ia_i$ per body on a rope; frictionless $F_\mu = 0$; sliding friction $F_\mu = \mu N$; static friction $F \leq F_{\mu_0}$; just about to slide: fully developed static friction = limiting friction $F_{\mu_0} = \mu_0N$. Agree with the Formula section.
- The aria-label matches the chart.
- Term change (inquiry.json 12, solutions.md 17, tasks.json 5, unit.md 3, figures.json, answers.py comment): each is "kinetic" -> "sliding" and every one refers to a body that slides; no formula, number or answer changed; no other "kinetic friction" is left in any en FY9 unit.
- The en chart (docs/figures/fy9-tunnistus/fy9-voimat-en-360.png) and the hash, taken at the start and the end (65a72267ecdbb241).
