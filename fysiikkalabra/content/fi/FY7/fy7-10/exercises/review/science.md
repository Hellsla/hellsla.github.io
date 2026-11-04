VERDICT: FAIL
CONTENT-HASH: 40525b228243b454

## Blocking
- exercises.json:230 (fy7-10-L3-04) — B: a) asks the student to derive x = h′ tan α₂, which needs the apparent position to lie on the vertical through the object. The task never says so, and for oblique viewing it is a model choice, not a fact. — Fix: add to the task "Oletetaan, että esine näyttää olevan suoraan todellisen paikkansa yläpuolella", and say the same in solutions.md:181 Periaate.

## Polish
- solutions.md:182 (L3-04) — the heading "Kuvaajan lukeminen" sits over a table and no graph. — Use "Taulukon lukeminen" (or the house label for tables).
- solutions.md:196 (L3-05) — "kolme merkitsevää numeroa", but the glass thickness 6,0 mm has two. — Add that its term (3,8 mm) is small, so the 20,0 mm term limits the result.
- exercises.json:182 (L2-06) — the case is the same as the lesson's misconception paragraph (air→water at 60°, which gives 40,6°), so the answer is printed in the lesson. — Use another angle, for example 50,0°.
- Plan drift for pedagogy: the plan's L3 "sädeleveys" became a horizontal displacement in L3-05, and the plan's L2 error case (α₁/α₂) became "angle divided by n". Both are physically sound.

## Checked
- One script recomputed all 20 answers with my own formulas. All agree with exercises.json/answers.py: new 416,4 nm; 25,50°; 1,4985 (least squares through origin); 40,63°; Δn 0,0379; 1,3301; 19,474 mm.
- L1-06 MC: exactly one option is correct. Each distractor is really wrong, and its feedback is right: the frequency is unchanged, and the speed is what turns the wavefronts.
- L1-07: λ = λ₀/n is derived from f constant and v = fλ, correctly.
- L2-05: the 14 sines are right and the per-point ratios are 1,465–1,536. The fit-line wording follows the guardrails (yleensä; slope from the fitted line, not raw points; the origin justified).
- L2-07: n = 1,506, n_max 1,545, n_min 1,469 with the extremes combined correctly. The half-range is called an estimate.
- L3-04: α₁ 7,52/14,88/22,01/28,98°, and n 1,3274/1,3319/1,3344/1,3268. The small-angle limit d/n = 45,1 cm is a real check. The c) reasoning is right.
- L3-05: n sin α is constant across parallel layers, so the glass drops out of the angle in water (38,02°), and this is correctly argued. Tangent terms 3,839 + 15,636 mm.
- The hash was the same at the start and at the end.
