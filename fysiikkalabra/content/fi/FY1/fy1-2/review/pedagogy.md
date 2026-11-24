VERDICT: PASS
CONTENT-HASH: 3b3df2a745260fbd

## Blocking
(none)

## Polish
- inquiry.json `voyager-malli` (between koe-1 and koe-2; lab-1280 capture) — the table under Koe 1 shows 144,9 AU and 20,1 h for 2026 and 157,8 AU for 2030, the same quantities koe-2 asks the student to record, so koe-2 no longer produces anything new and ennuste-1's answer (about 20 h) is visible before the experiment — move `voyager-malli` after koe-2, or make its table other dates.
- inquiry.json `johtopaatos` model and criteria — the opening question ("miksi sama etäisyys ilmoitetaan eri yksiköillä") is answered on the core path only as "yksikön paikalle kirjoitetaan sen arvo"; why a unit is chosen (a convenient number: km too big, AU as the Earth's distance, light time as delay) is only in the optional `pohdi` and `tarkistus-3` — add a criterion and one sentence of the model answer on convenience.
- inquiry.json `koe-1` — the simulation only evaluates t = d/c, so the experiment checks arithmetic and exponent handling, not a physical result; ennuste-2's prompt already supplies "33 s". Acceptable for a units lesson, but a prefix or conversion step (read d in km, AU and s and convert between them) would serve the slot's goal (muunnokset, etuliitteet) better.
- inquiry.json `voyager-malli` — the correct option is by far the longest and hedged; the other two are one-liners. Shorten it and move the JPL comparison into the feedback only.
- lesson.md hero and `siirto` — "valotunteina" is never explained; `siirto` uses the unit AU/a, but "a" for year is not introduced: write "AU/vuosi" or add "1 a = 1 vuosi" to the prompt.

## Checked
- Learning path: prior knowledge (powers of ten, scales) matches fy1-1; goals (suure, SI, etuliitteet, merkitsevät numerot, muunnokset) all covered; sig figs only in the optional `merkitsevat` plus check 1 and the exercises, acceptable.
- Predictions can be argued and refuted by the model values; each wrong option's feedback repairs a named misconception (exponent as factor, constant speed means constant time).
- Model values are labelled as model values with source (voyager-malli, johtopaatos); workload about one lesson with optional items marked.
- Worked example: seven stages, one step each, symbolic before numeric, reasonableness check; numbers verified (4,503·10^9 km, 4,17 h).
- Etsi virhe (km² to m²) and siirto distractors/mistake feedback are real misconceptions; siirto answer 3,236 AU/a verified.
- Tarkista: concept, representation and calculation checks with misconception distractors; the explain criteria are observable.
- Sim at 390 px and 1280 px: controls and readout readable, text behind Käyttöohje/Mallin oletukset/Laskennan selitys; experiment locks the date.
- Exit ticket tests suure/yksikkö and prefix conversion, the core ideas.
- Finnish read through; no case or term errors found beyond the polish items.
- Exercises not judged (reviewed apart).
