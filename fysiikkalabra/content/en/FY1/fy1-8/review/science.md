VERDICT: PASS
CONTENT-HASH: 267bbdac252cae3d
Mode: delta (three new pysahdy checks in lesson.md; worked-example "Given and unknown" split into two paragraphs; inquiry.json presentation only)

## Blocking
- none

## Polish
- content/en/FY1/fy1-8/lesson.md:617 — the answer writes $t = \Delta t/\varepsilon_\text{max}$ for the shortest time, while the formula section (564) and the worked example (640) write $t \ge \ldots$ and $t_\text{min}$ — write $t_\text{min} = \Delta t/\varepsilon_\text{max}$ to match.

## Checked
- Recomputed: $0.2\,\text{s}/0.020 = 10\,\text{s}$ (exact, no rounding needed); worked example $s_\text{min} = v\Delta t/\varepsilon_\text{max} = 0.42 \cdot 0.2/0.050 = 1.68\,\text{m}$, which is unchanged.
- The third pysahdy uses the same relation $\varepsilon = \Delta t/t$, $t \ge \Delta t/\varepsilon_\text{max}$ and the same $\Delta t = 0.2\,\text{s}$ as the formula section and the summary (680).
- Hypothesis pysahdy: "distance doubles → time doubles" is testable and falsifiable, which matches the glossary definition and the $s = vt$ example in the text; the model answer is right.
- Variables pysahdy: changing both distance and batteries confounds the cause; the answer matches the fair-test paragraph just before it (29) and the glossary entry for *muuttuja*.
- Worked-example stage split: the text is the same and the question now stands last on its own; physics unchanged.
- inquiry.json: presentation-only change, so the predictions, feedback and model answers are unchanged.
