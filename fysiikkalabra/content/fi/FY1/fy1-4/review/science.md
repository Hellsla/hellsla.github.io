VERDICT: PASS
CONTENT-HASH: e0edff6ef10318e0

## Blocking

## Polish
- inquiry.json:94 (ennuste-2, third option feedback) — 0,79 g/ml → ≈ 63 g vs 0,80 g/ml and ≈ 61 g elsewhere (0,79 = LS slope, not wrong) — use 0,80 g/ml (≈ 62 g) or "noin 61–63 g".
- inquiry.json:90 (ennuste-2, correct option feedback) — "vakiotermi on noin 61 g (noin 1 g)" reads as if b were 1 g — write "…noin 61 g, jolloin d ≈ 1 g".
- lesson.md:88 (slope figure aria-label) — screen-reader text still has `k = Δy/Δx = 0,5` — `k = Δy : Δx` for consistency with the notation rule.
- inquiry.json:38–39 (kertaus) — "Moka"; use the chapter's term (*karkea virhe*) if that is what *Mittaaminen ja mittauksen luotettavuus* calls it.

## Checked
- Round-1 blocker fixed: tarkistus-2 Järkevyys now `25 km : 3,0 km/h ≈ 8,3 h` with units.
- Notation sweep (lesson.md, inquiry.json, exit-ticket.json, sim.js labels): no ×/\times, products with \cdot, operation divisions with `:` (Δs : Δt, (s − b) : k, Δt : Δs), slashes only in unit fractions (m/s, g/ml, °C/min) and one aria-label (polish).
- One script: dataset 1 d(k = 0,30/0,50/0,60 m/s, b = 0) = 0,76/0,12/0,44 m, best k through origin 0,49 m/s; dataset 2 d(b = 0) = 61 g, best b at k = 0,80 → 61,3 g, d = 1,2 g; dataset 3 at b = 80 °C min d = 5,80 °C at k ≈ −1,90 °C/min; LS residuals +/−/−/−/−/+/+ as the koe-3 answer says.
- Worked example: k = 8,0 °C/min, b = 20 °C, t = 2,5 min, symbolic first; residuals ≤ 0,8 °C, three each side; LS 7,85 °C/min agrees with the eye fit; reasonableness check is real (between 36,5 and 43,8 °C).
- kuvaajasta 15 km/h (mistakes 16,7 and 0,067), siirto 20 vrk (25, 16), tarkistus-2 7,0 h (8,3, 5,5), exit ticket k = 1,5 m/s, b = 2,0 m: all correct.
- Etsi virhe: consecutive slopes 0,2/0,8/0,5/0,3/0,5 m/s, s : t = 0,60/0,40/0,53 m/s correct.
- All four SVG figures to scale point by point (scatter, slope, kettle, kuvaajasta).
- sim.js: RMS d and least-squares fit correct; koe-1/3 lock b, koe-2 locks k; simState gives d; limits (example data, error only in y, dataset 3 curved) stated in Mallin oletukset.
