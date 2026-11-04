VERDICT: PASS
CONTENT-HASH: 381dad5d20fd70b0

## Blocking

## Polish
- inquiry.json ennuste-rako, correct option feedback (carried over) — the slit-tube fall time is 1,8 times the plastic tube's, not 2 times. — "lähes kaksinkertainen" / "nearly twice" would be more exact.
- lesson.md and glossary `induktiojarru` (carried over) — "the force grows with speed" holds only below the brake's critical speed. — Add "at low speeds", or keep it as a level-appropriate simplification.

## Checked
- Only change since the passed version: the siirto (braking-car) model solution's Sijoitus/Substitution step is split into two equations (git diff). Nothing else is changed.
- Step 1: v1² − v2² = (25 m/s)² − (10 m/s)² = 525 m²/s². My script gets 525.
- Step 2: F = 2400 kg · 525 m²/s² : (2 · 30 m) = 21 000 N = 21 kN. My script gets 21 000 N.
- This matches the Kaava step F = m(v1² − v2²) : (2s) symbol for symbol, with the 2s denominator kept as 2 · 30 m. Units reduce to kg·m/s² = N.
- The Vastaus (21 kN, 2 s.f.) and Järkevyys (a = 8,75 ≈ 8,8 m/s², ΔEk = 630 kJ) still agree with the substitution.
- The numeric answer of 21 kN and the mistakes 25, 9 and 42 kN are unchanged and still consistent.
- check_layout.py fy7-6 --width 340: OK in fi, en and fi-easy. I re-ran the screenshots.
- Physics, models and assessment are as in the earlier PASS. The diff touches no definition, model, option or feedback.
