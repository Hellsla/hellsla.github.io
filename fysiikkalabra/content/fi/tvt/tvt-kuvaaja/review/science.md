VERDICT: PASS
CONTENT-HASH: a93f2b4f234781de

## Blocking
- None.

## Polish
- Figure `good-bad`: only the lower panel says "esimerkkiaineisto"; the upper panel uses the same invented data (the aria-label says so). Optional: note it in the step-5 sentence ("Kuvan kummassakin kuvaajassa on sama keksitty esimerkkiaineisto").
- Step 5: "Graphical Analysis Prossa epävarmuusjanat ovat Pro-ominaisuus" is slightly redundant (the guide is for GA Pro); "Epävarmuusjanat ovat Pro-ominaisuus" would do. The hedge (no menu path, ask the teacher) is correct: the location is not verified.

## Checked
- Every UI name is in ga-facts.md: column/x-axis label pick, Column Options, Graph Tools > Edit Graph Options, Automatic / Always Show 0 / Manual, Zoom to all Data, Points / Lines / Both (Lines as the sensor default), Plot Manager > Point Symbols, Graph Legend, Export graph as png; error bars marked Pro.
- Physics: axis choice (independent variable horizontal, linearising axes T^2 vs l), units of a calculated quantity (s^2), broken line is not a model, error bar from y − Δy to y + Δy, when to show zero.
- Figure data match figures.py (DATA in both panels; good panel y 0..3, error bars ±0,15 s^2); the six points are plausible for T^2 = 4π^2 l / g with scatter; labels do not overlap; all labels LaTeX; "esimerkkiaineisto" on the panel with numbers.
- LaTeX: units in maths with \, and {,} (60 °C as $60\,{}^\circ\text{C}$); no \times; guides.py check passes (figures equal figures.py).

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Bold Finnish UI names checked against Lauri's GA v6.2.1 screenshots (cropped assets/pics/tvt/*.png and the uncropped originals in /mnt/project-files/ga-pro-kuvat/); English names in brackets checked against ga-facts.md. No invented Finnish names found.
- Verified: **Sarakkeen ominaisuudet**, **Näytä virhepalkit**, **Kuvaajan selite** (toggle in ga-kuvaajatyokalut.png). Axis-title buttons V (cm3) and m (g) and the lower-left magnifier icon are in ga-taulukko-kuvaaja.png. English: Edit Graph Options, Automatic, Always Show 0, Manual, Zoom to all Data, Points, Lines, Both, Plot Manager, Point Symbols, Export graph as png (all in ga-facts).
- Error-bar description (y − Δy … y + Δy, per-column setting) is correct. No physics changed otherwise.
- Note: the screenshot data (0,16,31,45,63,86 g) curve upward; it is labelled esimerkkiarvoja and used only to show the UI, so no problem here.
