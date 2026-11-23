VERDICT: PASS
CONTENT-HASH: f341f3b768cc86fe

## Blocking

## Polish
- content/en/FY8/fy8-10/exercises/solutions.md (fy8-10-L3-04 Formula a): the aligned block wraps m_final and Q by hand (`\quad + 3\,m_\text{n}`, `\quad - m_\text{Kr}`), against the "never split by hand" rule. The physics is fine; the visual reviewer can judge it.

## Checked
- I compared the removed text with the added text outside the Formula lines, ignoring whitespace. Only two Formula steps changed (L3-04 and L3-05). The rest is paragraph breaks, plus L3-04's parts b) and c) moved to a line of their own. No number, answer or tolerance changed.
- L3-04 a) starts from Q = (m_initial − m_final)c², with m_initial = m_U + m_n and m_final = m_Ba + m_Kr + 3m_n. It simplifies symbolically to (m_U − m_Ba − m_Kr − 2m_n)c², which agrees with the substitution. Atomic masses are allowed, because the electrons balance (92 = 56 + 36). Parts b) and c) are unchanged.
- L3-05:
  - a) E = Lt and E = Δm_yr c² give Δm_yr = Lt/c².
  - b) Δm = 4m_H − m(He-4) and f = Δm/(4m_H).
  - c) Δm_yr = f·m_hydrogen, inverted correctly.
  - d) the share = 10⁹·m_hydrogen/(0.70 M).
  - Every step is right and in FY8 scope (mass–energy equivalence).
- I recomputed both in one script with my own formulas. L3-04: 0.186033 u → 173.29 MeV, N = 2.562e21, E = 7.1135e10 J. L3-05: Δm_yr = 3.511e18 kg, f = 0.007119, m = 4.932e20 kg. Both agree with answers.py and with the JSON answers 7.11 and 4.9 inside their tolerance. Every other answer in the set is still inside its tolerance, against answers.py.
- The hash was f341f3b768cc86fe at the start and at the end.
