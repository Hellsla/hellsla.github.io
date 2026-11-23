VERDICT: PASS
CONTENT-HASH: 364279c08bcfaf40
SCOPE: delta (work queue 8g: Kaava step of the model solutions; paragraph breaks)

## Blocking

## Polish
- content/en/FY8/fy8-11/exercises/solutions.md (L2-02, L2-03 Formula): as in fy8-10, the aligned rows are wrapped by hand with `\quad`. This is a layout point only.

## Checked
- I compared the removed text with the added text outside the Formula lines, ignoring whitespace. They are identical: the rest of the diff is paragraph breaks only. No number, answer or tolerance changed.
- In every rewritten step Q = Δm c² comes first, then Δm = m_initial − m_final with both sides listed, and only then the combined form:
  - L1-01, Li-6 + n → He-4 + T: (m_Li + m_n − m_He − m_T)c².
  - L1-04, D + D → He-3 + n: (2m_D − m_He − m_n)c².
  - L2-03: x = 2 neutrons, then (m_n + m_U − m_Xe − m_Sr − 2m_n)c².
  - L1-02: Δm is given, which is stated.
  - Each combined form is correct.
- L2-02: E/m = Q/(m_D + m_T) per reaction is right.
- L3-01: E = Pt = NQ and m = N·m_U give m = Pt·m_U/Q. This is right.
- L3-02: Q = (4m_H − m_He)c² from atomic masses, with N/t = P/Q, gives the total energy including positron annihilation. This is acceptable at FY8 level and unchanged from before.
- I recomputed the touched answers in one script with my own formulas: L1-01 4.7834 MeV, L1-02 178.38 MeV, L1-04 3.2690 MeV, L2-01 1.5087 kg, L2-02 3.374e14 J/kg, L3-01 4.525 kg, L3-02 8.942e37 1/s. All agree with answers.py and lie inside their tolerance. All 19 answers in the set are still inside their tolerance against answers.py.
- The hash was 364279c08bcfaf40 at the start and at the end.
