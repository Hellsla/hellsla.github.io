VERDICT: PASS
CONTENT-HASH: 6a0a33a715c949de
SCOPE: delta added-exercise fy1-7-L2-09, fy1-7-L2-10 (work queue 19), round 2

## Blocking

## Polish
- content/fi/FY1/fy1-7/exercises/solutions.md:284 — The solution says Saturn's density is "noin puolet" of Neptune's. The ratio is 687/1638 = 0,42 (carried over from round 1; recorded in the PR) — "alle puolet".
- content/fi/FY1/fy1-7/exercises/solutions.md:282 — "koska se pyörii hitaammin" names only one cause. A rotating body flattens in proportion to ω²R³/(GM), so the Earth's higher density also plays a part. This is acceptable at FY1 level (C).

## Checked
- Hash 6a0a33a715c949de at the start and at the end. The packet was missing, so I generated it with `scripts/review_packet.py fy1-7 --role science --exercises`.
- Round-1 Blocking fixed. Model answer c) now says the Earth is slightly flattened by its rotation, less than Saturn, and that the flattening is mostly why the Earth's difference is small. The incorrect rounding explanation and the "jäykkä kivipallo" claim are gone.
- The flattening explanation checks out numerically:
  - 5493 · 6378/6357 = 5511 kg/m³.
  - The remaining 0,04 % comes from rounding the mass (5,9722 → 5,97), which brings the value to about 5514 kg/m³, NASA's figure.
  - For Saturn, 619 · 60 268/54 364 = 687 kg/m³.
- I recomputed both answers again:
  - L2-09: ρ = 6m/(πd³) = 5493,3 kg/m³, the same as answers.py and the key 5493 (−0,38 % from NASA).
  - L2-10: the fit through the origin gives 2699,7 kg/m³ (key 2700), and the prediction is 2,70 · 9,26 = 25,0 kg.
- Nothing else in the two exercises changed since round 1. The rest stands as judged then: the fact-sheet values, the PhET ranges and the shared Glass/Aluminium mark.
