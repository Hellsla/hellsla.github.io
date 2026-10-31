VERDICT: PASS
CONTENT-HASH: 805d1699396c2a38

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
