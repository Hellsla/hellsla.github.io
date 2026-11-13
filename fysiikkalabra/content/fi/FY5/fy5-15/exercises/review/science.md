VERDICT: PASS
CONTENT-HASH: bbbf95c2fad03835
SCOPE: delta added-exercise from 32ef02d3f3cb74d2 base 81db4a6fd727

## Blocking

## Polish
- fy5-15/exercises/solutions.md (L1-09, Vastaus) — The 2 significant figures are justified "kuten kuulokynnys 1,0·10⁻¹²". I₀ is a defined reference level. The precision comes from the read level 74,0 dB, which gives I to about 3 figures (2,51·10⁻⁵). Base the rounding on the reading, or simply say 2 significant figures suffice.
- fy5-15/exercises/solutions.md (L1-09 and L2-09, Järkevyys) — The two checks trade answers. L1-09's check computes I(2 m) = 1,0·10⁻⁴ W/m², the first step of L2-09. L2-09's check computes I(4 m) = 2,51·10⁻⁵ W/m², L1-09's answer. Both sit behind the solution buttons, so this is harmless, but the checks could use the 8 m point instead.

## Checked
- Figure data: P = 4π·2²·1,0·10⁻⁴ W ≈ 5,03 mW. The recomputed levels are 80,00, 73,98 and 67,96 dB at 2, 4 and 8 m, and the figure writes them as 80,0, 74,0 and 68,0. The values are printed in the figure, so they are read exactly. The alt text gives the same three values.
- L1-09: I = I₀·10^(L/10 dB) = 2,51·10⁻⁵ W/m², against the answer 2,5·10⁻⁵ with 3 % tolerance (recomputed).
- L2-09: P = 4πr²I = 5,03 mW. The 4 m point gives 5,05 mW, within 1 %. Both the stated 5,0 mW and 5,03 mW pass the 3 % tolerance.
- L2-09 states the point-source, even-spreading and no-reflection model in the task. L1-09 needs no model.
- Neither task gives the other's answer in its text. The figure shows no power or intensity.
- The notation L = 10 dB · lg(I/I₀) and I = P/(4πr²) matches the lesson. answers.py agrees with exercises.json.
- The hash was the same at the start and at the end.
