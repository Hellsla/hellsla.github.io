VERDICT: PASS
CONTENT-HASH: 272340bdf157de82

## Blocking

## Polish
- solutions.md fy7-14-L3-04 Answer c) — "in a thicker place the colour reflected most strongly is reflected about 5.8 %": the thin-film formula used in figures.py gives 5.67 % (the multiple-reflection denominator 1 + r₁r₂). 5.8 % is (|r₁| + |r₂|)² without that denominator. The conclusion "almost three times" (2.8×) still stands — write "about 5.7 %".
- solutions.md fy7-14-L2-08 Principle — "No light is lost in the coating" assumes a non-absorbing coating. Optional: "(the coating does not absorb light)".

## Checked
- One script recomputed all 21 numeric answers from the task text with my own model (path difference 2nd, a half-wave shift at a reflection into higher n, λₙ = λ/n). They agree with answers.py and exercises.json. Tolerances hold the rounded answers (L2-05 1.3, L3-05 12 µm, L2-08 70 %).
- L2-08: modelled R(λ) of the figure (d = 90 nm) has its minimum 1.26 % at 497 nm, and bare glass is 4.26 %. Reading 1.3 % and 4.3 % gives 69.8 %, inside the 3 % tolerance of 70.4 %. The cause of the residual reflection is right: n = 1.38 > √1.52 ≈ 1.23, so the two reflected amplitudes are unequal and cannot cancel completely.
- L3-04: one shift (1.00 < 1.47 > 1.33). In a), 2nd = 1323 nm, the only visible maximum is 529 nm, and 661.5 and 441 nm are missing, so the point is green. In b), 360 nm (2.5λ → 2λ). In c), the thin-limit R = 2.01 % equals bare water, and the amplitudes 0.19 and 0.05 are right. The opposite-phase cancellation that is not complete is explained correctly.
- L2-07: the R table equals the exact thin-film model at d = 97.83 nm (λ = 540 nm). The purple explanation (both ends reflect more) is right.
- L3-06 soap-curve (350 nm): the extrema are at 466 nm (R ≈ 0) and 621 nm (7.7 %), as the solution reads. k = 2, d = 350 nm.
- L1-06: exactly one correct option, and the feedback of each distractor is right. L1-09: λ/(2n) is right, and each distractor's feedback names the actual mistake.
- L3-05 air wedge: the shift at the lower (air → glass) surface is right, and the contact line is dark with k = 0. The fitted slope is 1.896 mm, so D = 12.4 µm.
- L3-02: 0.987⁸ = 90.06 %. The bare comparison 0.9574⁸ = 70.6 % is right.
- L2-05: the fit slope is 5.26, so n = 1.315 with k = 0. The rejection of k = 1 (n ≈ 3.9) is sound.
- Scope: thin films and anti-reflection coatings, inside the slot's clarification. The wedge and the extension tasks are labelled.
