VERDICT: PASS
CONTENT-HASH: 246a981427da374e

## Blocking

## Polish
- figures.py:252 — The lift label is still $\overline{F}_\text{noste}$. docs/force-diagrams.md reserves this symbol for buoyancy, and the exercises use it that way. Use e.g. $\overline{F}_\text{nosto}$.
- sim.js:19 — The comment says "600 x 720", but the code sets H = 740.

## Checked
- Round-3 diff (d22358db..HEAD): only figure `kone` (lesson.md:535, figures.py) changed. The physics text, inquiry, answers and sim are unchanged since round 2.
- `kone`: the body rect is x 415–525, and the whole force diagram stays right of the divider at x = 300. The drag tip is at x = 338 and its label at x = 307.5–352.5, clear of the pictured plane's nose (x = 276).
- `kone` proportions: G 80 = lift 80; F1 + F2 = 2 × 38.5 = 77 = drag 77. This matches $2F_1 - F_\text{v} = 0$ and lift = weight. Thrust starts from the front edge, drag from the rear edge and G from the centre. The aria-label agrees.
- Recomputed: worked example drag 2 × 48 kN = 96 kN; siirto 420 + 260 = 680 N. The other numbers were recomputed in round 2 and are unchanged: push forces, slide distances and times, the frictionless case, exp-1 and the collision data.
- Definitions, every choice item's single correct option and its distractor feedback, the other force diagrams (curling, skaters, car, lamp, sim), and the FY4 scope: unchanged and passed in round 2.
