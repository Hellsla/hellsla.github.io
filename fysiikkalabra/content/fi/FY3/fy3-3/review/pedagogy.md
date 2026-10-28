VERDICT: PASS
CONTENT-HASH: a8c5706f60d4138d
## Blocking

## Polish
- lesson.md paragraph "Lämpötilaa mitataan celsiusasteikolla …" — about 125 words with four ideas (two scales, absolute zero, p ∝ T, Ek ∝ T) — split after "celsiusasteen ja kelvinin suuruus on sama …" into a scale paragraph and a "Kaasun paine ja kelvinlämpötila" paragraph (or a ### heading).
- inquiry.json (pred-2, exp-2 intro, virhe, siirto, check-2) — numbers with units such as "2,0 dm³", "1,0 dm³", "120 kPa", "128 kPa", "101 kPa" stay plain while neighbouring values are LaTeX; the page shows two number styles. Convert to `$120\,\text{kPa}$` etc.
- inquiry.json check-2 hints — `\text{°C}` (e.g. `27\,\text{°C}`) differs from `{}^\circ\text{C}` used everywhere else; use one form.
- inquiry.json siirto solution last sentence "kansi painuu ulospäin" — a lid on a rigid jar does not visibly "painu"; write "kanteen kohdistuu ulospäin suurempi voima kuin ulkoa" or drop it.
## Checked
- Path: hook (tyre in cold and heat, same air) -> retrieval -> three predictions -> sim with locked V / varied T -> conclusion -> theory -> staged example -> checks; the opening question is answered in Johtopäätös, reflect and exit ticket 1; slot goals met, no extra.
- Experiments can refute the predictions: pressure is counted from collisions (emergent), pred-1/3 are revealed after exp-1 (min 2), pred-2 after the optional exp-2 and is itself optional, so no dead gate.
- Each choice item has exactly one correct option after the LaTeX edits (pred 1-3, virhe, check-1); wrong-option feedback repairs the misconception (celsius ratio, "heat is matter", particles swell, additive error).
- Numbers verified: 27->327 °C ratio 2 and 12,1; 120·313,15/293,15 ≈ 128; 101·353,15/293,15 = 121,67 ≈ 122 (distractors 404, 83,8 match); check-2 gives -273; example k = 0,37, θ0 = -270 (sig. figs. explained).
- Worked example: seven stages, one step each, figure after the paragraph it explains, independent reasonableness check via 273,15 K.
- Guardrail edits (Mallin rajat, "verrannollinen … harvalle kaasulle", "ei kaksinkertaistu") read clearly and are consistent between lesson, check-3 model answer and exit ticket.
- Finnish: case endings after math spans (`$300\,\text{K}$:ssa`, `$10\,{}^\circ\text{C}$:sta`) are correct; glossary terms used.
- Exercise set not judged (separate review).
