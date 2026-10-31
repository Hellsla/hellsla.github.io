VERDICT: PASS
CONTENT-HASH: cbae440bb7b5b0d1

## Blocking

## Polish
- lessons/FY1/fy1-3/lesson-answers.py:31,35 — the code comments still say "relative error" for Δt/t̄·100 % — rename them to "relative uncertainty" to match the lesson's new term (comment only, no number changes).
- lesson.md:282 / inquiry.json contribution — "Mittaustulos on arvio, jossa on virhe" is fine, but the Ydinajatus now says "jokaiseen mittaustulokseen liittyy epävarmuutta"; you could word the contribution the same way (style).

## Checked
- Full review against content/fi/FY1/fy1-3: the same definitions, models, formulas and conclusions. Only the expression is plainer. The new wording "Jokaiseen mittaustulokseen liittyy epävarmuutta, myös taitavan mittaajan tulokseen" is right, and so is "suhteellinen epävarmuus" ε = Δx/x̄·100 % in the theory, the example, check-2, the hints and the exit ticket. No "suhteellinen virhe" is left in any student text.
- Guardrails (measurement): virhe has a sign and is unknown. Epävarmuus is a positive estimate, not a hard limit. Resoluutio is kept apart from uncertainty (hand timing about 0,2 s). Half the range is called a simple scatter estimate and a cautious estimate for the mean, never the uncertainty of the mean. The outlier procedure is worded as the guardrail says (karkea, check-1 options and feedback).
- Recomputed in one script: the example (19,09 s; 3,1817 s; 0,12 s; 3,8 %), the figures (error-types means 2,407 s and 2,594 s, so Δt_sys ≈ 0,19 s; zero-scale 47,5 g), karkea (the mean shifts by 0,19 s, Δt goes from 0,09 s to 0,62 s), the ice data (1,5 °C and 0,1 °C), the coins (5,44 g and the mistakes 5,6, 27,2 and 4,8 g), check-2 (2,08 %, mistake 4,2 %) and the exit ticket (19,9 g; 1,99 %).
- Sim: the readings round(T + sys + sat·G_i, 0,01 s) agree with lesson-answers.py. Exp-1 at n = 1, 5 and 40 gives an error of −0,22 s, +0,076 s and −0,0005 s, with half-ranges 0, 0,25 and 0,26 s. Exp-2 at n = 40 gives 2,6995 s, so 0,30 s. Exp-3 gives 0,085, 0,26 and 0,525 s, a ratio of 6,18; the mistake 6 lies outside the 3 % tolerance. The simState keys mean, puoli and vir exist. The locked parameters isolate n or sat.
- Every choice has exactly one correct option, and every distractor's feedback says why it is wrong.
