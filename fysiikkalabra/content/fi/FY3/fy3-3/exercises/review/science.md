VERDICT: PASS
CONTENT-HASH: 1fa2d7945c0c3eaf

## Blocking

## Polish
- solutions.md:188 (fy3-3-L3-02) and :201 (fy3-3-L3-03): the Kaava ends with two rows. Each could add one combined row, $\tfrac{\theta_2}{{}^\circ\text{C}} = \tfrac{T_1}{\text{K}}\tfrac{p_2}{p_1} - 273{,}15$ and $\tfrac{\theta_2}{{}^\circ\text{C}} = \tfrac{T_1}{2\,\text{K}} - 273{,}15$. The physics is right as it stands.
- exercises.json (fy3-3-L1-10), carried over: liquid nitrogen boils at −196 °C only at normal pressure.

## Checked
- The packet's diff shows the `aligned` blocks flattened. I read the real multi-row blocks on disk (solutions.md:15–298), one equation per row.
- Kelvin conversions (L1-02, L1-03, L1-05, L2-01, L2-04) start from $T/\text{K} = \theta/{}^\circ\text{C} + 273{,}15$ and solve for $\theta$. They are correct, and the signs are right for negative results.
- L1-04: the new derivation is right. The two $+273{,}15$ terms cancel, so $\Delta T/\text{K} = (\theta_2-\theta_1)/{}^\circ\text{C}$.
- L2-02: $p = p_1 + \frac{p_2-p_1}{\theta_2-\theta_1}\theta$ uses $\theta_1 = 0\,{}^\circ\text{C}$, and that condition is stated on the row.
- L2-08: $\theta = (p-p_0)/k$ is correct.
- L3-01 and L3-02: $p \propto T$ is used in kelvins, with constant volume and amount of gas stated in the Periaate. This meets the guardrail condition.
- L3-03: the task itself states $E \propto T$ (thin gas). Halving $T$ in kelvins is right.
- I evaluated each final form again with the task data: 76,85 °C, −195,75 °C, 25 K, −270,45 °C, 59,85 °C, 101,6 kPa, 3,9955, 320,8 kPa, 127 °C, −126,6 °C and 90,9 °C. All match the unchanged Sijoitus and answers.
- L3-05: the Vastaus paragraph split changes no claim. Total pressure, not overpressure, is proportional to $T$; I recomputed 797 kPa, 696 kPa, 145,5 °C and 13,6 %.
- The hash was the same at the start and the end.
