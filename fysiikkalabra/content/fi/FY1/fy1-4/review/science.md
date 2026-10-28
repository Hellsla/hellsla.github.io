VERDICT: FAIL
CONTENT-HASH: b1b91cc01b5e20a2

## Blocking
- inquiry.json:416 (tarkistus-2 solution, Järkevyys) — division written with a slash as an operation, `$25 / 3{,}0 \approx 8{,}3\,\text{h}$`, against the notation rule (2026-10-28), and without units — write `$25\,\text{km} : 3{,}0\,\tfrac{\text{km}}{\text{h}} \approx 8{,}3\,\text{h}$`.

## Polish
- inquiry.json:38–39 (kertaus) — the third error type is called "Moka"; the teacher asks for the term *karkea virhe* — rename it consistently with the chapter *Mittaaminen ja mittauksen luotettavuus*.
- lesson.md:88 (slope figure aria-label) — `k = Δy/Δx` in the screen-reader text — `k = Δy : Δx` for consistency.
- lesson.md:346 — the equation is given with `+ 20 °C` although b = 20,0 °C was computed; fine for two significant figures, but say so or write 20 °C in the substitution too.
- inquiry.json ennuste-2, third option feedback — the extrapolation gives ≈ 63 g while the other feedbacks and the model answer say ≈ 61 g (locked k = 0,80 g/ml); use k = 0,80 there, giving 78,5 g − 16 g ≈ 62 g, or say "noin 61–63 g".

## Checked
- Recomputed in one script: dataset 1 d(0,30/0,50/0,60 m/s) = 0,76/0,12/0,44 m; dataset 2 d(b=0) = 61 g, best b ≈ 61,3 g (d ≈ 1,2 g); dataset 3 with b = 80 °C min d = 5,8 °C at k ≈ −1,9 °C/min, residual pattern +/−/+ as stated.
- Kettle example: k = 8,0 °C/min, b = 20 °C, t = 2,5 min; residuals ≤ 0,8 °C, three on each side; LS gives 7,85 °C/min, consistent with the eye fit.
- kuvaajasta 15 km/h (mistakes 16,7 and 0,067), siirto 20 vrk (25, 16), tarkistus-2 7,0 h (8,3, 5,5), Etsi virhe slopes 0,2…0,5 and 0,60/0,40/0,53 m/s: all correct.
- All four SVG figures checked to scale point by point (scatter, slope, kettle, kuvaajasta).
- sim.js: RMS deviation and least-squares fit correct; experiments lock the right parameter; limits (example data, error only in y, dataset 3 curved) stated.
- Notation sweep: no ×, \times or δ; every other colon division (Δs : Δt, s : t, (s − b) : k) reads unambiguously.
