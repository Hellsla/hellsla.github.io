VERDICT: PASS
CONTENT-HASH: bd8bb8dc576c084a

## Blocking

## Polish
- lessons/FY1/fy1-3/answers.py:31, lesson-answers.py:31,35 — comments still say "relative error" for Δx/x̄·100 %, which the lesson now names relative uncertainty — rename in the comments (shared with fi; no number changes).

## Checked
- Measurement, measurement error (x − x_true, signed), measurement uncertainty (positive estimate, not a guaranteed limit), resolution and the three kinds of error are kept apart as in docs/physics-guardrails.md; "every measurement result has uncertainty" and "relative uncertainty" match the Finnish source (lesson, worked example, check 3, exit ticket, solutions).
- Half the range is called an estimate of scatter, a cautious estimate for the mean and not a general uncertainty method; repeating reduces random error only; scale reading d/2 is worded per the guardrail with the method/instrument caveat; hand-timing 0.01 s resolution vs ~0.2 s uncertainty stated.
- Outlier handling (check, repeat, remove only with a found and recorded cause) is the same in theory, summary, misconception, the gross-error item and its feedback.
- Worked example recomputed: Σ = 19.09 s, x̄ = 3.1817 s, Δt = 0.12 s, ε = 3.77 % → 3.8 %; interval 3.06–3.30 s excludes 3.31 s as stated; rounding rule applied consistently.
- Simulation (reading = round(T + Δt_sys + Δt_ran·g_i, 0.01 s), T = 2.40 s) recomputed from the fixed series: exp-1 n=1 −0.22 s, n=40 −0.0005 s, half-range 0.25/0.26 s; exp-2 n=40 mean 2.6995 s → 0.30 s; exp-3 0.525/0.085 = 6.18 → 6.2 (mistake 6 outside the 3 % tolerance, as intended). Feedback numbers match.
- Siirto 5.44 g and its mistakes 5.6, 27.2, 4.8, 28 g; check 3: 2.08 % (answer 2.1, a student's "2 %" is inside the 5 % relative tolerance); thermometer data mean 1.5 °C, half-range 0.1 °C, ratio 15; gross-error numbers (shift ≈ 0.19 s, Δt 0.09 → 0.62 s, ≈7×).
- Exactly one correct option in every choice item; each distractor's feedback gives the right reason. Experiments lock sat/sys and vary only n or sat.
- Exit ticket: 19.9 g, Δm = 0.1 g; 0.09/4.52 = 1.99 % → 2 %.
- All numbers and correct flags of inquiry.json, exit-ticket.json and meta.json agree with content/fi (scripted comparison); lesson.md says the same physics as the Finnish lesson.
- Hash 05a807976aacb0fe at start; re-checked after the mid-review edit (git diff: names.sat → "random error", exp-3 unit → "times", labels only): bd8bb8dc576c084a at end.
