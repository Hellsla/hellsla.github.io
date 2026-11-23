VERDICT: PASS
CONTENT-HASH: bbb119c55d2a3d4c

## Blocking
- none

## Polish
- none

## Checked
- g = Δv/Δt = v/t used only in tasks whose text says the body starts from rest at t = 0 (L1-01, 02, 03, 05, 09, L2-01, 02, L3-02); L3-05, where the clock runs before the drop, keeps g = (v₂ − v₁)/(t₂ − t₁).
- L3-02 Kaava now ends at t₂ = v₂/g and Sijoitus computes g first: consistent.
- Delta: every changed Kaava step checked against the old one: the new rows start from the basic equation (definition or ratio) and solve symbolically to the same final form the Sijoitus substitutes into; no sign, symbol or condition changed.
- Numeric tokens of the removed and added lines compared by script: no number lost or changed (only added exponents or symbols of the new rows).
- answer, unit and tolerance of every exercise identical to the Finnish set (content/fi), all ids present; answers.py rerun, every answer within rounding of its json value (unchanged since the passed version).
- Paragraph splits of Mallivastaus/Vastaus/Periaate texts: same sentences, same numbers.
- Teacher-approved pictures and figures in the diff not re-judged (teacher-figure).
