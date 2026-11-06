VERDICT: PASS
CONTENT-HASH: 19c4b1112a3292c3

## Blocking

## Polish
- fy5-11/exercises/exercises.json:238 and solutions.md:250 (L2-08) — C (λ/b ≈ 1,3) and B (2,5) both have λ > b. In both, the wave already spreads over the whole half-plane behind the slit, so "C leviää heikommin kuin B" is the weakest step in the order. Suggest b_C = 25 mm, which gives λ/b = 0,80. The order D, A, C, B is unchanged and now goes through b < λ only at B. The mm unit trap stays.

## Checked
- New task L2-08 (type 9, order). λ = v/f gives 3,0 / 5,0 / 2,0 / 6,0 cm. λ : b gives A 0,50, B 2,5, C 1,33 and D 0,25. Ascending is D, A, C, B, which matches `order` and the answer.
- The prompt names the quantity and the direction ("heikoimmasta voimakkaimpaan").
- The constant speed at every frequency is stated as an assumption in the task, which is needed because a ripple tank is dispersive.
- The solution explains why neither b alone (C is the narrowest) nor λ alone (D is the longest) decides the order. This fits the lesson's warned "only a narrow slit diffracts" idea.
- The scope is v = fλ from fy5-10 and the diffraction criterion from this chapter.
- The solution chains are one fraction per line. From the text they fit 300 px. I did not render them.
- answers.py ran once. All numeric answers agree with exercises.json within tolerance.
- The hash was the same at the start and at the end.
