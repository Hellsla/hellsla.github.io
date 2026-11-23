VERDICT: PASS
CONTENT-HASH: 87f70b122b0e9621

## Blocking
- none

## Polish
- none

## Checked
- New fy1-5-L1-09: MAFY water 20 °C 1482,3 m/s · 2,0 s = 2964,6 m = 2,96 km, recomputed; 3,0 km inside tol 0,04.
- Rearranged rows (Δs = s − s₀, 2d = ct, meeting-time v₂t₀ = (v₂ − v₁)t, area = vt) algebraically correct.
- Delta: every changed Kaava step checked against the old one: the new rows start from the basic equation (definition or ratio) and solve symbolically to the same final form the Sijoitus substitutes into; no sign, symbol or condition changed.
- Numeric tokens of the removed and added lines compared by script: no number lost or changed (only added exponents or symbols of the new rows).
- answer, unit and tolerance of every exercise identical to the Finnish set (content/fi), all ids present; answers.py rerun, every answer within rounding of its json value (unchanged since the passed version).
- Paragraph splits of Mallivastaus/Vastaus/Periaate texts: same sentences, same numbers.
- Teacher-approved pictures and figures in the diff not re-judged (teacher-figure).
