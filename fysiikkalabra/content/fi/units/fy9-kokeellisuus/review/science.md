VERDICT: FAIL
CONTENT-HASH: d8caf555a4e34ae3
Review of the recognition chart (queue 9c) and the term change against the version passed at 4fca163bc3ac2f29; full on the chart, delta on the rest.

## Blocking
- B (row 7 and ARIA_KARTTA): "suora ei kulje origon kautta → systemaattinen virhe, b ≠ 0". A non-zero intercept points to a systematic error only when the model says the line should pass through the origin; in a model with a constant term (x = x_0 + vt, p = p_0 + ρgh, v = v_0 + at, the unit's own y = kx + b) b ≠ 0 is physics, not an error. The unit states the condition twice ("vaikka mallin mukaan sen pitäisi"; "Jos mallin mukaan suoran pitäisi kulkea origon kautta mutta b poikkeaa selvästi nollasta"); the chart and the aria-label drop it, so the rule of thumb is wrong as given. Fix: e.g. "mallin suora kulkee origon kautta, mittausten ei" (and "selvästi").

## Polish
- C: "tulos kulmakertoimesta → kaukaiset pisteet": the points are on the fitted line, not data points; the aria-label says "suoran kahdesta … pisteestä", the chart only "kaukaiset pisteet". Adding "suoran" in the chart would remove the ambiguity.

## Checked
- Rows against the Kaava section: many results → x̄ = Σx_i/n (MAFY form of mafy-tunnukset.tsv); spread → Δx = (x_max − x_min)/2 ("tässä kurssissa", as the Kaava); final result → x̄ ± Δx; is the uncertainty small → ε = Δx/x̄; linear dependence → fit y = kx + b (Kaava: "Kun mallin mukaan … lineaarisesti"); slope → k = Δy/Δx; intercept (above).
- Rendered PNG (1280): formulas as in figures.py.
- ARIA_KARTTA: same seven rows, same order and physics.
- Term change in sovella/solutions.md (two lines): liikekitka → liukukitka; the physics is unchanged (pulling at constant speed measures sliding friction, grip means static friction just before slipping; wheels that do not slip need static friction). Consistent with glossary liukukitka; lepokitka kept.
- unit.md: only the figure.
