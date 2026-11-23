VERDICT: PASS
CONTENT-HASH: e76de909aec34e7f

## Blocking
- none

## Polish
- none

## Checked
- Cooling-rate rows (L2 rate difference, L3 measuring time): r = −ΔT/Δt = (T_alku − T_loppu)/(t_loppu − t_alku) is now sign-consistent (positive rate of fall); r₁ = 2,4, r₂ = 1,0, Δr = 1,4 K/min and r = 2,0 K/min, T_lasku ≥ 20 K, t ≥ 10 min recomputed.
- v = Δs/Δt, n = (t_kok − t_val)/(N t_toisto), ε ≤ ε_max → t ≥ Δt/ε_max rows correct; hypothesis wording (overlap shows no difference, does not prove equality) kept.
- Delta: every changed Kaava step checked against the old one: the new rows start from the basic equation (definition or ratio) and solve symbolically to the same final form the Sijoitus substitutes into; no sign, symbol or condition changed.
- Numeric tokens of the removed and added lines compared by script: no number lost or changed (only added exponents or symbols of the new rows).
- answer, unit and tolerance of every exercise identical to the Finnish set (content/fi), all ids present; answers.py rerun, every answer within rounding of its json value (unchanged since the passed version).
- Paragraph splits of Mallivastaus/Vastaus/Periaate texts: same sentences, same numbers.
- Teacher-approved pictures and figures in the diff not re-judged (teacher-figure).
