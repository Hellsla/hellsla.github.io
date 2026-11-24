VERDICT: PASS
CONTENT-HASH: 76e86f953efa066e

## Blocking
None.

## Polish
- fy3-s3-c Principle: stray bracket "(part d) estimates the effect of warming)"; reword to "part d estimates the effect of warming".
- fy3-s3-d: the third bullet carries the closing conclusion ("rough estimate, not a guarantee, leave a reserve") and the ideal-gas note. Move the conclusion out of the bullet into its own paragraph, since the rubric awards a point for it.
- fy3-s3-c Formula: "Δp_tank V_tank = nRT" is the amount of air used, not nRT of the whole tank. Name it in the Principle ("the air used") so students do not read it as the tank's total.
- fy3-s1-c Formula: the P_o, P_a, eta rows are a chain of definitions. They are fine, but "P_a = P" could have a short word label.
- fy3-s2 has no source line for the table, although source_note exists. Check that the page shows it.

## Checked
- Changed Formula steps only. Every Formula step now starts from the basic law and solves symbolically to the end, as the read-through rule requires.
  - s1-b: Q = PΔt, Q = cmΔT, then P.
  - s1-d: Q = cmΔT, P = P_water + P_loss, then P_loss.
  - s2-c: E = Pt, ηE, Q = rm, then m.
  - s2-d: Q_released = Q_received, then m_v/m.
  - s3-a: p_1, p_2, pV = nRT, then V_2.
  - s3-c: from Δp V = nRT, then V, then t.
- No Formula step substitutes numbers early. Conversions and Substitution follow separately, and each chain's first row names its quantity.
- Tasks are unchanged and still demand independent application: no heading or prompt names a formula, and there is source data (the table and the temperature series) to interpret.
- Rubrics are specific, with no points for irrelevant things. Each task rises in demand and has an assumptions or evaluation part.
- Common mistakes are real, such as gauge versus total pressure, K/min versus K/s, and Celsius versus kelvins.
- Workload fits a 2-credit module: three tasks, with s1-a graphing as the heaviest.
- Variety is good: graph and data analysis, phase change with a table, and gas laws with a safety conclusion.
- Hash confirmed with practice.py hash FY3 --lang en. practice.py check: OK.
