VERDICT: PASS
CONTENT-HASH: 5f41f190068800fe

## Blocking

## Polish
- assets/sims/fy4/fy4-1/sim.js:1123 — the readout and slider label always use the decimal comma (`0,0 m`), also on the English page, where the inquiry uses decimal points; a student copying `4,0` into a numeric answer may be confused — follow the page language in `tx()` (presentation, not physics).
- lessons/FY4/fy4-1/lesson-answers.py — the mistake value 0.67 (Δt/Δx in `data`), the meeting point 6 s / 12 m (pred-3 feedback) and the exit-ticket Δx = −8 m are not computed there; add them so every inquiry number is generated.
- inquiry.json `check-3` model — "a rising part on the way to the shop and a falling part on the way back": the hook has a stop at the shop, so the graph also has a horizontal part; one clause would make the model answer match the hook (C, not a finding).
- lesson.md hero — the picture shows a loop around a lake while the text and figures use a straight there-and-back ride; both give Δx = 0, so no error, but the 1-D x-axis story is cleaner with the shop ride.

## Checked
- Recomputed in one script with my own formulas: 15 km/h (and distractors 7.5, 0.25), v_B = 4.0, v_D = −3.0 m/s, A–D meeting at 6 s and 12 m, robot data slope 1.494 ± 0.029 m/s (LSQ, intercept 4.10 m, line at 10 s 19.04 m), mistakes 1.9, 1.3, 0.67, cart E Δx = 0 and s = 16 m, virhe −3.0 m/s, sled 5.0 m/s, x0 = −11 m, 39 m (mistakes 50, 74, 5.0), check-2 13 m (origin at 4.8 s), jogger 2.5 m/s = 9 km/h, 170 m, exit Δx = −8 m: all agree with the text and lesson-answers.py.
- Definitions of position, displacement (vector, sign = direction), distance, velocity, speed, average velocity match the glossary and are used consistently in theory, summary, options, feedback and exit ticket.
- Model conditions stated: uniform motion for x = x0 + vt; average velocity's meaning for non-uniform motion; the sim's "full speed at once, no friction, case 4 exception" in its model box.
- Figures to scale where they say so: displacement axis (40 px/m), jogger graph, data graph (points and fitted line at 4.1→19.1 m), cart E graph; slope triangle points lie on the line.
- Sim code implements x = x0 + vt per case (A 2 m/s; B 4; C x0 20, v 2; D x0 30, v −3; E out 4 s, rest 2 s, back 4 s); `simState` gives `xA`, `x2` at every slider value (0.5 s steps), so exp-1…3 isolate t with the case locked.
- Every choice item has exactly one correct option; each distractor is really wrong and its feedback names the reason correctly; "ahead" in pred-2 is stated with the positive direction (guardrail).
- Fitting guidance follows the guardrails: slope from two far points on the fitted line, not neighbouring raw points; the ±0.03 m/s slope uncertainty is right.
- Worked example and all numeric solutions have the seven stages, symbolic first, with justified rounding.
- Scope: FY4.1 bridge content (position, displacement, signed velocity, (t,x) graphs) only.
- Hash checked at start and end: unchanged.
