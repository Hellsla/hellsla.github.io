VERDICT: DONE

Drafted fy3-15 (round 1); `check_lesson.py fy3-15` is all ok, lint has 0 errors and 0 warnings, and the layout check passes at 360, 768, 1280 and 1920 px.

- meta.json: glossary list extended (hukkalämpö, kaukolämpö, energiaketju, kokonaishyötysuhde).
- lesson.md: Ydinajatus with a to-scale Sankey of a condensing plant and a stacked CHP chart (sähkö, kaukolämpö, hukkalämpö; 400 MW fuel). Kaava: Voimalaitoksen hyötysuhde (chain product, η_kok, P_h = c q_m ΔT) with a waterfall figure and a condenser figure. Staged example (5 stages), misconception, summary. Every figure label is LaTeX in a fig-tex box.
- inquiry.json: hook, retrieval, two predictions (no sim, so feedback is gated on commitment), three interpret tasks (chain table, CHP interpolation, plant-type comparison), theory, reflection, error-spotting, transfer, three checks, exit ticket.
- exercises.json, answers.py, solutions.md, exit-ticket.json: 5/4/3 original tasks, answers computed first.
- sim-spec.md: states why there is no simulation.
- glossary.json: two small insertions (energiaketju, kokonaishyötysuhde).

Environment: I pip-installed markdown and playwright to run the checks. The scratchpad is shared between developers; my generators are in scratchpad/fy315/.

Not fixable here: none.
