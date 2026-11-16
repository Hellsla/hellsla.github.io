VERDICT: FAIL
CONTENT-HASH: 73148e61b87edd84

## Blocking
- [Critical] inquiry.json, "Find the error" task (A student calculates …) — two equations are merged into one chain: `A = 6.0 cm²` / `= 0.060 m²|e|` / `= NΔB·A/Δt` / `= 200 · 0.30 T · 0.060 m²/0.050 s` / `= 72 V` (seen at 390 px at this hash, at 390 and 1280 px at the previous one; the source row is unchanged: `&= 0.060\,\text{m}^2 |e| \\`). The left side `|e|` is glued to the area's value and the area appears to equal 72 V: broken notation that changes the meaning of the task. Fix: `\begin{aligned} A &= 6.0\,\text{cm}^2 \\ &= 0.060\,\text{m}^2 \\[6pt] |e| &= \frac{N \Delta B \cdot A}{\Delta t} \\ &= \frac{200 \cdot 0.30\,\text{T} \cdot 0.060\,\text{m}^2}{0.050\,\text{s}} \\ &= 72\,\text{V} \end{aligned}`. Check fi and fi-easy for the same merge.

## Polish
- none

## Checked
- batch delta review: queue 5d reflow. The content changed twice during the review (7e4ba8466f, 5cf5c8668b); this report judges the hash above: the page was rebuilt (build.py) and its five aligned blocks of inquiry.json captured from preview/en/fy7-5.html at 390 px with every box, hint, solution and feedback forced open, and read; box overflow measured at 390 and 1280 px (none). review/shots is stale for this hash. Figures were not re-judged.
