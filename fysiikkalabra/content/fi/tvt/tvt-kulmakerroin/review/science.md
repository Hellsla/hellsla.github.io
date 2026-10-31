VERDICT: PASS
CONTENT-HASH: dd68b9034e7f878c

## Blocking
- None.

## Polish
- The symbol $k$ is both the slope and the spring constant in step 6 ("kulmakerroin on suoraan jousivakio") — fine, but one clause ("jousen $k$ on silloin kulmakerroin") could make the double use explicit.
- The worked example's $k = 4{,}05\,\text{s}^2/\text{m}$ is a different invented data set from the tvt-kuvaaja figure (whose LSQ slope is about 3,97 s^2/m); harmless since both are labelled invented, but the same numbers across guides would read better.

## Checked
- Slope from two far-apart points on the fitted line (never raw points); Δ explicitly a change, not an uncertainty; values read in quantity units, not paper cm.
- Units: slope = y-unit / x-unit (N/m, s^2/m), intercept = y-unit; $g = 4\pi^2 : 4{,}05\,\text{s}^2/\text{m} \approx 9{,}75\,\text{m/s}^2$ recomputed (9,748); unit check correct.
- Intercept causes correct: length measured to the bob's top gives T^2 = k(l + r), positive intercept, unchanged slope; spring hanger inconsistency gives an intercept; T^2(m) intercept from the spring's own mass; "epävarmuuksien rajoissa nolla" wording.
- UI: Apply Curve Fit, "Show units in linear fit parameters" marked Pro — in ga-facts.md.
- Figure matches figures.py (LSQ line, slope triangle, b at the intercept); labels LaTeX, no overlaps; schematic without numbers.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Bold Finnish UI names checked against Lauri's GA v6.2.1 screenshots (cropped assets/pics/tvt/*.png and the uncropped originals in /mnt/project-files/ga-pro-kuvat/); English names in brackets checked against ga-facts.md. No invented Finnish names found.
- Verified: **Käyrän sovitus**, **Lineaarinen**; tulosruutu text "y = mx + b", "m: 1.671 g/cm3" and the gear icon match ga-tulosruutu.png. English: Show units in linear fit parameters (ga-facts).
- m = slope k, b = intercept, and 1.671 g/cm3 → k = 1,671 g/cm³ are correct (I recomputed the least-squares fit of the screenshot data: m = 2925/1750 = 1.6714, b = -1.619). Unit check slope = y-unit / x-unit is right.
- Polish: "Ohjelma käyttää desimaalipistettä" is too general: the tulosruutu uses a point, but the axis labels in Lauri's start-screen original show commas (0,9; 1,0). Say "Tulosruudussa ohjelma käyttää desimaalipistettä".
