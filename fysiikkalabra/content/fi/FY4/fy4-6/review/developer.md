VERDICT: DONE

Draft, round 1. Every line of check_lesson.py fy4-6 says ok.

- `lesson.md`: hero (moving van, box at rest on a loading ramp). Ydinajatus covers paino, lepokitka and liikekitka (a graph of F_μ against the pull), the kalteva taso, friction that is not against the motion (a box on an accelerating pickup bed, walking: example J) and noste or väliaineen vastus in one paragraph. `## Kaava: Kitkavoima ja kalteva taso` gives G = mg, F_μ = μN, F_μ0 ≤ μ0N, G_x and G_y, tan α ≤ μ0 and how the coefficient is found by experiment. The worked example (box sliding down a 25° ramp) has 8 stages, including Voimakuvio. Then the misconception and the summary.
- `inquiry.json`: two predictions (static friction rising with the angle; mass and acceleration). New sim with exp-1 (slip angle → μ0, numeric) and exp-2 (mass). Then the conclusion, an optional spring-scale table, error/select/draw fbd tasks, a conveyor-belt transfer task (friction acting in the direction of motion) and three checks.
- `exercises/` 5/4/3 with complete solutions; `exit-ticket.json` 3; `answers.py`, `lesson-answers.py`, `figures.py` (every FBD with fbd.py), `sim-spec.md`.
- `assets/sims/fy4/fy4-6/sim.js`: a box on a tilting plank, a force diagram and an (α, F_μ) trail graph. It stacks on a phone. `tests/sims/fy4-6.json` has 23 assertions; `lang/fi.json` `sims.fy4-6`.
- `glossary.json`: kitka, lepokitka, liikekitka, kitkakerroin, kalteva taso; fy4-6 added to paino.

Lint: 7 warnings, all false positives ("μ0 N" is read as "0 N").

## Round 1 fix
- N moved uphill in kalteva, esimerkki, valitse-a..d; N = mg cos α conditions stated (lesson, virhekäsitys, Tiivistelmä, glossary); new figure kalteva-ydin after the components paragraph.
- Inquiry: α as LaTeX, one wood μ range, check-2 wording, limit-angle claim now argued from the formula (not measured), hook names empty/full box.
- Exercises: rounded answers, L2-01 varied, L2-04 asks the margin, L3-03 reasoning, L1-01/L1-05 diagram line, L2-03 provenance.
- Sim: larger diagram (per-mass scale, 13/14 px labels), shorter phone layout. Hero: steeper-ramp inset.
- Not changed: air resistance wording in L1-02/03, L2-02 (fair simplification C).
