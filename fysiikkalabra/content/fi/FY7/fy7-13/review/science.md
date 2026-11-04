VERDICT: PASS
CONTENT-HASH: b49f619380cd340e

## Blocking

## Polish
- content/fi/FY7/fy7-13/lesson.md:318 (figure "pattern") — alt text still calls the grating peaks "korkeita" although each curve is normalised to its own maximum — say so, or drop "korkeita" (carried over from round 1, not requested).
- content/fi/FY7/fy7-13/inquiry.json:19 — hook "tasavälisiä" dots holds only at small angles (x = L tan θ) — optionally "lähes tasavälisiä" (carried over).
- Slot täsmennys names thin films; not treated here — confirm the thin-film chapter covers it (carried over).

## Checked
- Round-1 fixes: hila paragraph now "kun rakojen väli on sama" (correct condition); "Kuinka monta maksimia" now kλ < d with the edge case kλ = d explained, consistent with sim, inquiry and exercises.
- Figure "geometry" after shortening the rays (Lr 200): rays parallel at θ, foot of the perpendicular (56,9 px along the upper ray) still on the drawn ray, right angle, both θ marks and Δs = d sin θ correct; capture #15 re-taken and checked.
- inquiry.json: only the unit label N "1/mm" -> "viivaa/mm"; no number, option or feedback changed.
- lesson-answers.py: stale setup-x1/x2 keys removed; comments 11,245° and 15,664° now right.
- Recomputed in one script with my own formulas: 600/532 nm θ₁ = 18,61°, x₁ = 33,68 cm; 600/650 nm d : λ = 2,56 (five maxima); example λ = 647,4 nm (tangent 660 nm); white light 6,89° and 12,12°. All agree with the text.
- Rest of the lesson unchanged since my round-1 full review (all inquiry numerics, mistakes, predictions, sim simState and limits passed then).
