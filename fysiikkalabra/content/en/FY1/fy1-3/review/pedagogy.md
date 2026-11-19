VERDICT: FAIL
CONTENT-HASH: d2c20fc1e0f44698

## Blocking
- inquiry.json check-2 (numeric, answer 2.08, tolerance 0.05) — the model solution's final answer is "2 %" (one significant figure, like the error estimate 0.05 s), but 2 is 0.08 outside 2.08 ± 0.05, so a student who follows the solution's rounding is marked wrong; the house rule is that a student rounding to the stated figures stays inside the tolerance — fix: answer 2.1 with tolerance ≥ 0.1 and let the solution say "2 %" (calculator value 2.08 %), or make the answer 2 with tolerance 0.1; keep the "forgot to halve" mistake value 4.2 and the "not yet percent" value 0.021 distinct.

## Polish
- lesson.md:302 (Key idea, 139 words), :309 (Gross error, 118), :312 (Random error, 117), :416 (error-estimate paragraph, 136), :578 (misconception, 125) — over the ~120-word paragraph limit; the Key idea and the error-estimate paragraphs each carry several ideas (error vs uncertainty vs "not a largest possible deviation"; half-range vs mean uncertainty vs method limits) — split into short paragraphs.
- Workload is above one lesson: three error kinds, repeatability/accuracy, mean, half-range, rounding rule, reading uncertainty, resolution, relative uncertainty, zero correction. The slot's goals are error sources and repeatability; make the rounding rule, half-scale-division and resolution optional, or move them to the next lesson, and mark the resolution check (check-c2) `optional` so the lesson has three checks, not four.
- The LIGO photo (pics/fy1/ligo-hanford.webp) follows "Repeatability and accuracy" but no sentence refers to it or to measurement reliability; either tie it to a sentence (very small uncertainty relative to the result) or drop it. The caliper photo is fine.
- exp-3 hint 3 already gives both table values (0.525 s and 0.0850 s), leaving only a division; point to the table rows instead of quoting the numbers.
- Hook asks "how can they know the stopwatch is not wrong in the same way for everyone"; the first fully worked answer (ice water) comes only in the data task, so say in the reflect prompt that the answer is a reference value, or keep the wording as is but check that reflect's model answer names it.

## Checked
- Learning path follows from fy1-2; hook question is answered only after commitment (predictions) and returns in reflect.
- Predictions can be refuted by the simulation; each wrong option's feedback repairs a named misconception; correct answers are not systematically the longest or first.
- Simulation results emerge from a fixed random series; numbers are called model values in the conclusion's model answer; experiments lock sat/sys and vary n (exp-1, exp-2) with min 3.
- Arithmetic checked: worked example (sum 19.09 s, mean 3.18 s, 0.12 s, 3.8 %), gross-error item (0.09 s vs 0.62 s, mean shift about 0.2 s), siirto (5.44 g), exit ticket (19.9 g, 2 %), exp-3 ratio 6.2.
- Worked example has seven stages, one step each, symbolic before numeric, with a reasonableness check that notes the result 3.31 s falls outside the interval.
- Thermometer data task checks the core idea (systematic error found only by reference) and its feedback repairs each distractor.
- Exit ticket tests the core idea (mean damps random but not systematic error) and a calculation.
- Exercises are not judged here (reviewed separately); screenshots not opened.
