VERDICT: PASS
CONTENT-HASH: 41ba9b76f7a3dc91

## Blocking
- None.

## Polish
- Step 7 (and the common-error line): "Jos vakiotermi on epävarmuuksien rajoissa nolla" — the student needs the intercept's uncertainty for that; add a link to [[ohje:tvt-epavarmuus|…]] (fit-parameter uncertainty, Pro, or the steepest/shallowest lines, whose intercepts give a range).
- Step 8 list: the toy-car line $v^2 = 2g \cdot h$ holds only when friction (and the wheels' rotation) is negligible; a few words ("kun kitka on pieni") would state the condition (guardrails B). Cooling line: the model is Newton's cooling law; optional to name it.
- Step 4: "RMSE kertoo, kuinka kaukana pisteet ovat keskimäärin suorasta" is a fair simplification (root-mean-square, not mean) — keep, or say "neliöllisesti keskimäärin".

## Checked
- Least squares described correctly: vertical residuals, minimum sum of squares; line not through first/last point; points "yleensä" not exactly on the line (guardrails wording).
- Linear (with intercept) vs Proportional (y = kx); fit Linear first, Proportional only with a physical reason; r near ±1 does not prove the model; residual pattern check; outlier wording is the guardrails sentence; extrapolation rule.
- UI names: Graph Tools > Apply Curve Fit, Linear, Proportional, region selection by dragging, fit box with coefficients, RMSE and r (Linear) — all in ga-facts.md.
- Linearisations correct: T^2 vs l, v^2 vs h, E vs 1/r^2, ln(T − T_huone) vs t.
- Figures match figures.py: `fit` line is the computed least-squares line, residuals vertical; `linearise` left panel's LSQ line is above the points at the ends and below in the middle, exactly as the text and aria-label say; no overlaps; schematic, no numbers.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Bold Finnish UI names checked against Lauri's GA v6.2.1 screenshots (cropped assets/pics/tvt/*.png and the uncropped originals in /mnt/project-files/ga-pro-kuvat/); English names in brackets checked against ga-facts.md. No invented Finnish names found.
- Verified: **Käyrän sovitus**, **Lineaarinen**, **Ota käyttöön** (ga-kuvaajatyokalut.png, ga-kayran-sovitus.png); "Valittu väli näkyy sinisenä… viereen avautuu valikko… Käyrän sovitus" is confirmed by Lauri's original k_yr_n_sovitus2.png; LINEAARINEN, y = mx + b, m, b, r, RMSE match ga-tulosruutu.png. English: Proportional (ga-facts).
- m = k, b = intercept, decimal point 1.671 → 1,671: correct. RMSE description (typical vertical distance in y-units) and the warning that r near ±1 does not prove the model are correct; the screenshot data itself is a mild upward curve with r = 0.9961, which illustrates that warning.
