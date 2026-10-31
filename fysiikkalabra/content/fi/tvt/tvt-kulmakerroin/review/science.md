VERDICT: PASS
CONTENT-HASH: 9b63d475ee4eca47

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
