VERDICT: PASS
CONTENT-HASH: 8e38a43298c1653c

## Blocking
(none)

## Polish
- solutions.md fy8-s3 a/b (carried over) — Cs-137 also emits beta particles, which air absorbs over tens of centimetres. One clause saying the tube is taken to count the 662 keV gamma photons (or that the capsule stops the betas) would make the condition of the inverse-square model explicit.

## Checked
- Hash 8e38a43298c1653c (`practice.py hash FY8 --lang en`) at the start and the end.
- Since my last report (c355f45d310c2f53, commit 4fd1ee4d0c), git diff shows only two lines of content changed, both the fy8-s3 d conclusion:
  - solutions.md:382 now reads "farther out it is soon lost in the random variation of the background with this counting time".
  - The tasks.json conclusion rubric detail says the same.
  - No number, answers.py line or figure changed.
- The fix is correct. Recomputed: $R_\text{b} = 112/5.0 = 22.4\,\tfrac{1}{\text{min}}$, $r = \sqrt{K/R_\text{b}} - d = 37.5 - 1.3 = 36.2\,\text{cm}$, $H = 0.229\,\mu\text{Sv/h}$.
- At 36 cm, a 1.0 min count gives a net rate of 22.4 ± 7.0 1/min, about 3σ, so the source is still detectable there, as the new text implies. At twice that distance the net rate is 5.8 ± 5.7 1/min, about 1σ, so it really is lost in the background's random variation. A student who says the source is still measurable at 36 cm is no longer penalised.
- The Finnish version (content/fi solutions.md:334 and its rubric) uses the same wording.
- The rest is unchanged since the full review that passed every other recomputation (s1, s2, s3 a–c, s4, s5), the scope, the significant figures, the rubric sums (15, 20, 17, 16, 16) and the alternative methods. Those results still hold.
