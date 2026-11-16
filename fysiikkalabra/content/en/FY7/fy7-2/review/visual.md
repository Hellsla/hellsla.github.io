VERDICT: FAIL
CONTENT-HASH: d01fdd009e97a42c

## Blocking
- [Critical] inquiry.json, Example 2 "Find the error" task (She writes …) — the follow-up re-break merged three separate equations into one chain: the page shows `qU = mv²v` / `= √(qU/m)` / `= 4.38 · 10⁵ m/sr` / `= mv/(qB)` / `= 4.57 cm` at 390 and 1280 px. The symbols `v` and `r` that start the second and third equations are glued to the end of the previous rows ("mv²v", "m/sr"), so the notation is broken and the student's three steps read as one false equality. Fix: one equation per group, e.g. `\begin{aligned} qU &= mv^2 \\[6pt] v &= \sqrt{\frac{qU}{m}} \\ &= 4.38 \cdot 10^{5}\,\text{m/s} \\[6pt] r &= \frac{mv}{qB} \\ &= 4.57\,\text{cm} \end{aligned}` (or the version before 7e4ba8466f). Check fi and fi-easy for the same merge.

## Polish
- [Minor] solution, `v = √(…)` (untouched): the numerator breaks before `· 20 000 V`, right-aligned under the radical.

## Checked
- batch delta review: queue 5d reflow. The content changed during the review (commit 7e4ba8466f); this report judges the new hash: the page was rebuilt (build.py) and recaptured. review/shots is stale for this hash and has no phone captures of opened states, so every aligned formula of inquiry.json and exit-ticket.json (3 rendered blocks) was captured from preview/en/fy7-2.html at 390 px and 1280 px with every box, hint, solution and choice feedback forced open, and each capture was read; box overflow measured at 390 and 1280 px. Figures and the formula-name / teacher-figure categories were not re-judged.
