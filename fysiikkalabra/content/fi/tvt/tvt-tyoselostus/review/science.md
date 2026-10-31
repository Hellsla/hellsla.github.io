VERDICT: PASS
CONTENT-HASH: b7d259b4446ba947

## Blocking
- None.

## Polish
- Step 4: "Show units in linear fit parameters" is a Pro setting (ga-facts.md, and marked "(Pro)" in tvt-kulmakerroin); add "(Pro)" here too for consistency.
- Step 4: GA's fit box lists the coefficients (m, b) under the equation rather than printing "y = 4,05x + 0,02" literally; "esimerkiksi" covers it, but "tietolaatikon kertoimet, esimerkiksi kulmakerroin 4,05 ja vakiotermi 0,02" would match the screen better.
- Figure label $T^2 = k \cdot l$ is the proportional model while the text example has an intercept (0,02 s^2); fine for a schematic, or write $T^2 = k \cdot l + b$.

## Checked
- Table: quantity and unit in every header, raw data left and derived quantities right, consistent precision (0,450 m), one extra digit in intermediates; figure number and caption, text reference.
- Line equation with quantities and units: $T^2 = 4{,}05\,\text{s}^2/\text{m} \cdot l + 0{,}02\,\text{s}^2$ dimensionally correct and consistent with the k = 4,05 s^2/m used in tvt-kulmakerroin and tvt-epavarmuus; model calculation symbolic first; result $g = (9{,}7 \pm 0{,}4)\,\text{m/s}^2$ consistent with tvt-epavarmuus.
- UI names: Export graph as png, Export data as csv, Show units in linear fit parameters — in ga-facts.md; image export rather than screenshot.
- Figure matches figures.py; sections 4–6 of the FY10 template; grey bars for student content; labels LaTeX, no overlaps.
