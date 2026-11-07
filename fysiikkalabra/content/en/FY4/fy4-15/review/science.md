VERDICT: FAIL
CONTENT-HASH: a2697420968d3d19
Mode: delta (editorial round 2026-11-07: undisturbed-wind reference power, η as its fraction, cubic law condition, cut-in/rated/cut-out, V82 caption)

## Blocking
- lesson.md:253 (ilmalierio aria-label) — B, internal consistency: the text alternative still says "In time t the air flowing through the rotor fills a cylinder … m = ρAvt". The new paragraph two lines above (lesson.md:251) says that the air at the rotor is slower than v and its mass flow is *not* ρAv; the figure description now contradicts the corrected model. — Fix: "In time t the undisturbed wind would carry through the swept area the air that fills a cylinder …", and "ilman massa olisi m = ρAvt".

## Polish
- lesson.md:251 and lesson.md:302 — a literal `\n\n` stands between two paragraphs (seen in the built preview as text "\n\nTodellisuudessa…"/"\n\nIn reality…"). Not physics, but it is visible on the page. Fix: a real blank line.
- inquiry.json (prediction feedback ~58/62/179 and check-3 model ~337) — "roottorin läpi virtaa kaksi kertaa enemmän ilmaa" / "osuus roottorin läpi virtaavan ilman liike-energiasta": still true as proportionality (C), but "pyyhkäisypinta-alan läpi" would match the new wording.
- Carried over: Järkevyys "2,1 · 1,0 MW ≈ 2,2 MW" (2,14 · 1,017).

## Checked
- Recomputed: ½ρAv³ = 5,15 MW → 5,2 MW; 0,45 · = 2,32 MW → 2,3 MW; (120:82)² = 2,14; 2·4 = 8; curve 5→10 m/s ×8,9.
- Undisturbed-wind derivation (m = ρAvt, ½ρAv³t) correct; "reference power, η = P : P_tuuli" is the standard power-coefficient definition; Betz 59 % of that reference correct.
- Cubic law stated only for roughly constant η (theory and Tiivistelmä agree).
- Cut-in 3–4 m/s agrees with the curve (3 m/s 0 kW, 4 m/s 28 kW); rated 1650 kW from ~13 m/s; cut-out stop correctly described, and the caption says the graph does not show it.
- V82 caption: standard density 1,225 kg/m³ and 10-min hub-height means correct; model 1,25 vs 1,225 called approximate, right.
- Example task and Periaate now define η the same way as the theory; exit ticket 3 adds cut-out correctly.
- Hash identical at start and end.
