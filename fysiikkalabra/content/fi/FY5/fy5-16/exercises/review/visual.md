VERDICT: FAIL
CONTENT-HASH: da6046c3a1ee90f4

## Blocking
- [Major] fy5-16-L2-07 shown answer (capture #65, contact-6) — the green answer pill under the task reads "2^8 = 256", not the answer "1,9 min" — the student sees a wrong final answer (a number with no unit, for a minutes task) before the solution — cause: scripts/answers_shown.py `shown()` takes the first formula in the Vastaus step whose number agrees with 1,9 within the rounding of its last digit; `2^{\,8}` has mantissa 2, within 0,5 of 1,9, so a) "ajan pitää jakaa luvulla $2^{\,8} = 256$" wins over b). Confirmed by calling shown() on the block. — fix (content, not mine to apply): in the Vastaus step write no formula with a leading number before the b-value (for example "luvulla $256$" in plain maths, or put b first: "b) Sallittu aika on noin $1{,}9\,\text{min}$ ... a) ..."), or tighten shown() to match a unit.

## Polish
- [Minor] fy5-16-L2-07 Järkevyys — the check chain ends "7,5 min → 3,75 min → 1,875 min"; "3,75" is cut off at the card edge in capture #66 ("→ 3,75" then the sentence continues on the next line) — the chain wraps at the arrow, fine, but confirm the last term 1,875 min is visible at 360 px (the chain shows only up to 3,75 in the capture).

## Checked
- L2-07 numbers: 109 - 85 = 24 dB = 8 steps; student 8 h : 8 = 1,0 h = 60 min; correct 8 h / 2^8 = 480 min / 256 = 1,875 min, about 1,9 min; 60 / 1,875 = 32 (stated); answer 1,9 min, tolerance 0,02 accepts 1,875. The earlier 80 min Minor is gone.
- No repeat: 109 dB, 24 dB and 1,9 min appear nowhere else in the lesson or other tasks; 7,5 min occurs only as an intermediate step of the halving chain (it is the inquiry's answer, not a task answer here).
- Captures opened: contact-6 (#65 task, answer pill, #66 solution) after the retake: the solution chain 8 h / 2^8 = 480 min / 256 = 1,875 min ≈ 1,9 min reads well, units upright.
- Wording unchanged (opiskelija), fluent; rest of the set unchanged.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 3
