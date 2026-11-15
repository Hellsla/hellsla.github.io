VERDICT: PASS
CONTENT-HASH: 1de1e6f9b64da513
SCOPE: delta added-exercise from d4cac7da6f13b625 base f6ae5d507c79

## Blocking
(none)

## Polish
(none)

## Checked
- I recomputed fy8-2-L2-09 with my own script: E = hc/λ at 436 nm gives 4.556e-19 J = 2.844 eV. That matches answers.py (2.844029) and the JSON (2.84 eV). Readings of 433–439 nm give 2.825–2.864 eV, so a tolerance of 0.03 fits a few nm of reading error.
- I recomputed fy8-2-L3-06. E_v(405 nm) = 3.0617 eV and E_g(546 nm) = 2.2711 eV, so ΔE = 0.7907 eV. That matches answers.py and the JSON (0.79 eV). Readings 2 nm either way give 0.77–0.81 eV, inside the tolerance of 0.05.
- L3-06 physics: both transitions start from the same upper state, so E_u cancels and the difference of the photon energies is the difference of the lower levels. The model answer for c is right: the two photons are alternative transitions of one atom, not consecutive steps, and a sum would count E_u twice.
- The L3-06 data matches real mercury levels. 7s ³S₁ (7.730 eV) → 6p ³P₀ (4.667 eV) gives 404.8 nm and → ³P₂ (5.461 eV) gives 546.4 nm. The lower levels differ by 0.794 eV, which agrees with 0.79 to two significant figures as the solution says.
- The corrected 1570 nm remark is right: 1240 eV nm / 0.79 eV ≈ 1570 nm (1561 nm from 0.794 eV), which is infrared. It is worded as a conditional ("if an atom could move…"), so it does not claim such a line exists.
- The figure has lines at 405, 436, 546, 577 and 579 nm on a 380–720 nm scale, small ticks every 10 nm and numbers every 50 nm. The 436 nm line is drawn blue (Bruton colour, b = 1, r ≈ 0.07). The figure gives every value both tasks need, and its description carries the same information. Neither gives away an answer.
- Both solutions are complete. Each states the principle with its reason, gives the formula symbolically before substituting (ΔE = E_v − E_g derived from the two transition equations), shows conversions and substitution with units, justifies the rounding by the reading uncertainty (3 s.f. and 2 s.f.), and checks reasonableness against the 1240 eV nm shortcut, line ordering and tabulated levels.
- Scope: E = hf with eV conversion and transitions between quantised states fall within FY8's central contents and the lesson's brief. Notation and constants (h, c, e) are the FY8 conventions. The English text uses decimal points.
- Hash 1de1e6f9b64da513 at start and end.
