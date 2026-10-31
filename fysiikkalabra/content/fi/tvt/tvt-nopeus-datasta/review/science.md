VERDICT: PASS
CONTENT-HASH: 432de54e086d7ae9

## Blocking
- None.

## Polish
- Step 1: "Siksi nopeutta ei lasketa peräkkäisten rivien erotuksista" is stronger than needed; add "kohinaisesta datasta" (as the common-error line does) so it is not read as a rule for clean, sparse data.
- Common error "Suora on sovitettu koko kuvaajaan … Kulmakerroin on liian pieni": true when the non-uniform part is the slower start (falling ball before terminal speed); add "esimerkiksi kun mukana on kiihdytysvaihe" (guardrails B).
- Step 8 writes the offset error as $\delta a$; NOTES.md §1 names a measurement error $\Delta x$. Here Δ already means a change in the same guide, so δ avoids a clash — acceptable, but the lead may want one sentence saying δa is the constant offset of the readings.

## Checked
- Mean velocity Δx/Δt, noise amplified on short intervals; centred `firstDerivative("x","t",7)` (Pro, 3/5/7 points, more smoothing rounds fast changes) as in TIL 11314/1011; Tangent under Graph Tools; slope of a fitted line for uniform motion; sign vs speed.
- Photogate example recomputed: 0,010 m : 0,020 s = 0,50 m/s; unit conversion stressed.
- Area under (t, v) as strips Δs ≈ v·Δt, displacement vs distance; View Integral; `integral("v","t")` starts at 0; a→v→s with the at-rest condition stated; offset error grows as δa·t and ½·δa·t^2 (correct); zero from the rest-period mean with View Statistics; check v returns to 0.
- Figure matches figures.py: trapezoidal strips under a start–cruise–stop profile, highlighted strip and Δt bracket, labels LaTeX, no overlaps; schematic without numbers.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Bold Finnish UI names checked against Lauri's GA v6.2.1 screenshots (cropped assets/pics/tvt/*.png and the uncropped originals in /mnt/project-files/ga-pro-kuvat/); English names in brackets checked against ga-facts.md. No invented Finnish names found.
- Verified: **Tangentti** (toggle), **Integraali**, **Tilastotiedot** (ga-kuvaajatyokalut.png; the menu beside a selection is confirmed in Lauri's original k_yr_n_sovitus2.png). English: Speed Through Gate (ga-facts).
- Integral wording now correct: integral("a","t") = change of velocity from the start, equal to velocity only from rest; integral("v","t") = displacement, equal to distance only for one-way motion. Zero-offset drift δa·t and ½·δa·t² correct.
- Column names: the guide says its names are t, x, v, a and tells the student to copy the names from the table header; consistent with taulukkolaskenta.
