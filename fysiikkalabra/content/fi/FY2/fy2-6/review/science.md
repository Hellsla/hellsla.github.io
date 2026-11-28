VERDICT: PASS
CONTENT-HASH: a49e621fe4bda732

## Blocking

## Polish
- lesson.md:290 — the summary says the average power is the annual energy divided by "vuoden tuntimäärällä 8760 h" with no condition, while theory line 153 states the ordinary-year condition and the leap-year case; adding "ordinary year" to the summary would match the theory and the 2024 task (C, not a finding).
- inquiry.json data-fi — answer 2.3 with tolerance 0.02 also accepts 2.31 GW (8760 h); a fair leniency, since the 0.3 % difference is below the data's precision.

## Checked
- Hash identical at start and end.
- Recomputed in one script: 2024 is a leap year, 366 · 24 h = 8784 h; 20.2·10⁹ kWh : 8784 h = 2 299 636 kW = 2.2996 GW → 2.30 GW (old 8760 h value 2.306 GW); within tolerance of the stored 2.3.
- lesson-answers.py tuuli-keskiteho_GW = 2.299636, agrees with my value and the solution's 2 299 636 kW.
- Significant figures: three, from 20.2 TWh; 8784 h exact for the calendar year (the statistic is for calendar 2024). Reason stated in the solution.
- Solution complete: given, asked, principle E = Pt, symbolic P = E/t, conversions TWh→kWh and kW→GW, substitution, answer, estimate check (20·10⁹ : 8800 ≈ 2.3 GW) and the rated-vs-average power remark, all physically right.
- Mistake 2300 (MW): 2299.6 MW = 2.30 GW, feedback right. Mistake 0.0023 (10⁶ slip): 20.2·10⁶ : 8784 = 0.0023 GW, feedback right.
- Hint 3 divides by 8784 h, consistent with the prompt and solution.
- No 2.31 / 2306 left; the other 8760 h uses (worked example 14 GWh, its check, summary) are generic years, not 2024 data, so nothing contradicts the task. "Muut lähteet" 0.8 TWh unchanged and right.
- Scope: P = E : t and kWh in FY2's central contents; no later-course physics added.
