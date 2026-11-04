VERDICT: PASS
CONTENT-HASH: c8529fc08d8728d3

## Blocking

## Polish
- Packet (tooling) — the "Exercise brief" block is still empty in the English packet (section extraction by Finnish headings); fix the packet tool, not the exercises (carried).
- Packet — `check_lesson.py has not been run` for the translation; run the deterministic checks before release (carried).

## Checked
- Delta re-review: the only change since the passed version is commit fd2e54e95 in exercises/solutions.md (360 px narrowing); hash c8529fc08d8728d3 equals the packet's, at start and end. No task, answer, unit, tolerance or other file changed.
- solutions.md:89 (L2-04 reasonableness) — `96 → 48 → 24 → 12 → 6 → 3` then (in $\mu\text{Sv/h}$): the unit now applies to the whole chain instead of only the last entry, which is if anything more correct; 96/2⁵ = 3 µSv/h, both `$…$` pairs closed, sentence reads correctly.
- solutions.md:95 (L3-01 formula) — inside `\left[…\right]` only `\left(\dfrac{r_1}{r_\text{A}}\right)^2` → `\left(\tfrac{r_1}{r_\text{A}}\right)^2`: same fraction, text-size only; braces and \left/\right pairs balanced (scripted check); H_A − H_B = Ḣ₁ t[(r₁/r_A)² − (½)^{d/d½}] still equals the two terms stated before it.
- Previous review's recomputation of all 12 answers and its other checks stand (content unchanged).
