VERDICT: PASS
CONTENT-HASH: 328979ec82ec54f4
Mode: delta (round 2, commit f9cecc6 since 8b7dd5d78)

## Blocking

## Polish
- inquiry.json (prediction feedback ~58/62/179, check-3 model ~337): "roottorin läpi virtaa kaksi kertaa enemmän ilmaa" is still true as a proportion (C); "pyyhkäisypinta-alan läpi" would match the theory's wording.
- Carried over: Järkevyys "2,1 · 1,0 MW ≈ 2,2 MW" (2,14 · 1,017).

## Checked
- Round-1 Blocking fixed: the ilmalierio text alternative (lesson.md:253, generated from figures.py/figures.json) now says the undisturbed wind *would carry* the air through the swept area and the mass *would be* m = ρAvt. This agrees with the paragraph saying the mass flow at the rotor is not ρAv.
- The literal `\n\n` is gone: real paragraph breaks in the reference-power and three-ranges passages; the rebuilt preview has no "\n\n".
- Paragraph content unchanged: reference power ½ρAv³, η = P : P_tuuli, Betz 59 % of the reference, cubic law only with roughly constant η, cut-in 3–4 m/s, rated 1650 kW from ~13 m/s, cut-out stop, V82 caption (1,225 kg/m³, 10-min hub-height means).
- Recomputed: 5,15 MW reference, 2,32 MW electric, (120:82)² = 2,14.
- Hash identical at start and end.
