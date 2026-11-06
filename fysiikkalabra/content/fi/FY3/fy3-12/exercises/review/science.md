VERDICT: PASS
CONTENT-HASH: 83748953571d3f72
Round: 2

## Blocking
(none)

## Polish
- solutions.md:206 — the Arvio still checks only the largest and smallest; the close pair could be checked too, e.g. "yläpohja 0,09 · 80 ≈ 7 W/K < ikkunat 1,2 · 8 ≈ 10 W/K". Optional, carried over.

## Checked
- Round-1 Polish resolved: the roof is now $U = 0{,}090\,\text{W/(m}^2\cdot\text{K)}$, so "U-arvot on annettu kahdella [numerolla]" (solutions.md:206) is true and the 2-figure values 60, 220, 290, 460 W are justified.
- Recomputed: ΔT = 30 K; P = 60 W, 216 W, 288 W, 459 W; order ovi < yläpohja < ikkunat < seinä unchanged and right.
- Task text now ends "…ja vertaa niitä"; the `prompt` still names P and the direction (smallest to largest), so the ordering task is unambiguous.
- Commit 6bbde30c5 changes only this line in fy3-12; answers.py, the solution and the other tasks unchanged.
- Text only this round: I did not open the new captures; the change adds one digit.
- Hash identical at start and end.
