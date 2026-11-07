VERDICT: PASS
CONTENT-HASH: 5d3cb5c270e9d347

## Blocking

## Polish
- solutions.md s3 d — the task now says to use the added mass determined in part c, but Annettu/Periaate/Sijoitus still use $m_\text{s}/3 = 15$ g as the task's model and 'Hyväksytään myös' lists c's intercept value 14 g as the alternative; make c's added mass (≈ 14 g ≈ $m_\text{s}/3$) the main path. Both give 0,43 m/s (recomputed 0,434 and 0,433 m/s), so no score changes.
- tasks.json s3 c/d — d presupposes a numeric added mass from c, but c's text asks only what the deviation can be due to (the number appears only in c's error_sources criterion); c could ask to estimate the added mass from the intercept.

## Checked
- light delta review (teacher 2026-11-07), after fixes: HEAD~1 diff of tasks.json s3: source note no longer states the m_s/3 answer of c; d now says to use the hanging mass plus c's added mass; criterion 1 says the same with the model m_eff = m + m_s/3. Recomputed fit: slope 1.982 s²/kg, k = 19.9 N/m, intercept 0.0278 s², added mass 14.0 g; v_max 0.434 m/s (14 g) / 0.433 m/s (15 g), massless 0.446 m/s (outside 3 % tolerance, 2-point partial credit still fits the three criteria). Physics correct; rubric consistent, Polish only.
