VERDICT: FAIL
CONTENT-HASH: bca89d9de1f19d26

## Blocking
- inquiry.json (exp-1 `names.alpha`, exp-2 `names.alpha`: "kulma α") — the Unicode α is shown as plain text in the Alkutila box ("kulma α = 0 °") and in the table header "kulma α" (390 and 1280 px captures), while m, G_x, F_μ are LaTeX; teacher's rule 2026-10-26: every label LaTeX — fix: "kulma $\\alpha$" in both `names` (and "0 °" without the stray space in the Alkutila line).

## Polish
- inquiry.json johtopaatos/reflect — the question and model answer claim the *limit angle* is mass-independent (and reflect asks about "täysi ja tyhjä laatikko", never introduced in Pohdinta), but exp-2 locks α = 35° and the box always slides, so no measurement shows it — fix: add to exp-2 a step at 26° and 27° (or rephrase the question to acceleration only) and name the full/empty box in the hook.
- Sim at 390 and 1280 px — the force diagram is a small box with 9–11 px labels in a mostly empty panel; at α = 10° arrows are tiny; the Tutki sim is 508 px tall on a phone so the slider and the *Kirjaa mittaus* button are a scroll apart — fix: scale the diagram to fill its panel.
- lesson.md Ydinajatus "Kalteva taso" — components and "dashed" are explained with no picture; the figure comes only after the Kaava paragraph — fix: move or repeat the small figure after that paragraph.
- Notation — lepokitka is $F_{\mu 0}$ in Kaava but $\overline{F}_\mu$ in every figure, the sim and solutions — fix: say once that the diagram's $F_\mu$ is the static friction at rest.
- Hero shows the box staying only; the steeper case of the Miksi question is not pictured. Task text wraps ":n kulmassa" onto its own line (shared template, example card at 390 px).

## Checked
- Opening question answered (Ydinajatus, johtopäätös); hero matches the Miksi at FY3 detail; chapter names, no ids shown.
- Predictions refutable by exp-1/exp-2; locks, 2 experiments, one hour of core path.
- Force diagrams (docs/force-diagrams.md): select, error, draw, equations all practised; each distractor has one error with feedback naming it; descriptions list arrows without verdicts; diagram precedes equations in every solution.
- Example staged in 8 steps, symbolic before numeric; figures legible at 390 px; layout 360/768/1280 clean.
- Finnish and terms fine; exit ticket tests the core ideas.
