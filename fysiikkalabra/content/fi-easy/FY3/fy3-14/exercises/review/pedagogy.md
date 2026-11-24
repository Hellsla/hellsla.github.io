VERDICT: PASS
CONTENT-HASH: fac43d3c5888a291
## Blocking
(none)
## Polish
- solutions.md fy3-14-L2-04 Sijoitus — "Hakasulkeiden lauseke" no longer matches the Kaava, where the quantity is named K. Fix: "Lauseke $K$ on".
- solutions.md fy3-14-L3-03 Kaava — the step from the two Q rows to "N = ..." skips the rearrangement, and the closing sentence after the block has no full stop. Add one line, for example "kun termit kerätään", and the full stop.
## Checked
- Delta: the array numerators are replaced by named intermediate quantities (K, N) in L2-04, L3-03 and L3-04. Each row is a short step.
- L2-04: K = m_v(T_v − T) − m_j T and s = c_v K / m_j agree with the Sijoitus step (3,975 kg·K).
- L3-03: N = c_v m_v ΔT_v + s m_v + c_j m_j T_j and T = N / (c_j(m_j + m_v)) agree with the numerator terms in Sijoitus.
- L3-04: K, N and s = N/m_j agree with the case ΔT_j = 0 in a).
- The symbolic form is reached before any substitution, and no bracket is broken inside an array.
- Judged from the diff and the solutions file on disk. Hash unchanged at start and end.
