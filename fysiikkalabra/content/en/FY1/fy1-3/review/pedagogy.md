VERDICT: PASS
CONTENT-HASH: 6b5fc5bd9373a765

## Blocking
(none)

## Polish
- lesson.md:146 (Formula section, "In this course the scatter…") — one paragraph of about 140 words carries five ideas: half of the range, uncertainty versus error, the "rough, not a strict limit" caveat, the uncertainty of the mean, and a note on method. It is over the 120-word rule. Fix: split it into "Half of the range", "How to read the error estimate" and a short note about the mean. The Key idea paragraph (line 99) is also about 130 words; split it after "…the measurement error."
- inquiry.json `pr-numerot` — the feedback on the wrong options ("the precision of the reading is not a hundredth when the time is taken by hand") gives away the hand-timing point that the lesson is about to investigate. Fix: keep the feedback on significant figures only, and leave the hand-timing point to the hook and experiment 1.
- inquiry.json `exp-2` question — after prediction 2 the student already knows the answer is 0.30 s, so the task is only a subtraction. Fix: ask for the mean at n = 10 as well and whether the gap to T changes, or ask which number in the table would show a systematic error if T were unknown.
- inquiry.json Tarkista has four checks (concept, resolution, calculation, explain), where the house form has three. The resolution check is good, because it repairs the "display digits equal uncertainty" misconception, but it adds workload. Fix: mark `check-c2` optional, or fold it into `check-1`.
- inquiry.json `siirto` — the third hint gives the whole method, including the formula. This is acceptable as the last hint, but state the zero-correction step as a question in hint 2 so the student still has to choose it.

## Checked
- Learning path: it follows the slot goals (error kinds, repeatability, mean and half of the range) and ends with a systematic-error correction that uses a reference value. It does not go past FY1 scope.
- The opening question is answered only after commitment. The hook gets back to the class in `reflect`.
- pred-1 and pred-2 target real misconceptions: "repeats remove all error" and "the mean grows away". Experiments 1 and 2 can refute them, since the mean, range and difference columns are measured per n with the errors locked.
- The simulation is justified: the mean settling emerges from a fixed noisy series, and the numbers are called model values. The lead text is short, and the three closed boxes are present (captures #2, #40).
- Worked example: seven stages, one step each. I checked the numbers (mean 3.18 s, ±0.12 s, 3.8 %, five of six in the interval). Rounding is justified and the reasonableness stage is honest about the 3.31 s result.
- The gross-error task: the feedback figures (0.19 s shift, 0.09 s to 0.62 s) are correct, and it does not teach "drop outliers".
- Figures in captures #3–#6 are legible and sit next to the text they explain. The theory figure `error-types` shows the contrast without an answer attached to any task.
- The explain criteria are observable and match the prompts. The exit ticket tests the core idea (zero correction, mean versus systematic error, relative uncertainty).
- Phone captures at 390 px: no clipping, controls understandable. 1280 px: the simulation sits beside the experiments.
- Not judged: the exercise set (reviewed apart). The packet reported that `check_lesson.py` had not been run. The hash at the start and the end was 6b5fc5bd9373a765.
