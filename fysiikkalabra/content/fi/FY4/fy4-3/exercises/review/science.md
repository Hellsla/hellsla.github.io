VERDICT: PASS
CONTENT-HASH: 1b72d20a59f51860

## Blocking

## Polish
- solutions.md:424-430 (L3-01) — C/B, drawn sum. $F_\text{v}$ = 270 N is 5,8 % of G, so it is lifted to the 15 % floor. Measured lengths: G 100, $F_\text{n}$ 94, $F_\text{v}$ 15. The drawn upward total is 109 against 100 downward, with a = 0 and $\overline{v}$ down. It follows the stated rule, and the text alternative says so, but it is the one drawn sum in the set that does not balance, and the balance is the point of the task. Suggested fix in fbdspec.py: when the floor lifts a force collinear with others, shorten the largest same-direction force by the same amount so the sum still shows (here $F_\text{n}$ 85 + $F_\text{v}$ 15 = G 100).
- solutions.md:316-324 (L1-04) and L1-03, L2-02 — The split scale (horizontal largest drawn at 0,6 of G) is stated only in the aria-label. A sighted reader sees $\overline{F}$ at 0,6·G with no note. Add a visible note under split-scale figures.
- solutions.md L1-03 — Carried over: state "jää oletetaan kitkattomaksi".

## Checked
- Round-1 blocking item (L1-04) is resolved. G = N = 12 000 N, realistic for a car. On the split scale the measured lengths are F 60, $F_\text{i}$ 37, $F_\text{r}$ 23, and 37 + 23 = 60 matches 620 = 380 + 240. G = N = 100, and the text alternative states the split.
- All 12 diagrams were rendered (`fbdspec.py show`), screenshotted, and their arrow lengths measured from the SVG. All proportions are on one scale:
  - L2-01: 61,5 / 38,5 / 100.
  - L2-04: 65 / 35 / 100.
  - L3-02: 50 / 50 / 100.
  - L3-03: 21 / 79 / 100.
  - The equal pairs (L1-01, L1-02, L1-05, L2-03) are 100 / 100.
- Split scales: L1-03 (90 vs 590 N) and L2-02 (65 vs 720 N). In each, the horizontal forces are mutually correct (L2-02: 60 = 60).
- No diagram contradicts its Voimakuvio sentence or its motion. a = 0 wherever the velocity is constant. In L1-03 $\overline{a}$ points away from the wall.
- Third-law partners stay off every diagram.
- I recomputed all 12 answers in one script. Each is within tolerance: 18; 850; 90; 240; 6,38; 13; 65; 834; 8,94; 0,27; 0,60; 1,9.
- The hash was the same at the start and at the end.
