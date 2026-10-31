VERDICT: PASS
CONTENT-HASH: 1639b5fd020dc273

## Blocking
- None.

## Polish
- Figure `sheet`: the calculated column shows 0,81 / 1,21 / 1,6129 — mixed precision in one column. GA shows one displayed precision per column (step 2 tells the student to set it), so a student may find the picture confusing. Either show all three to the same number of decimals (0,8100 / 1,2100 / 1,6129) or say in the text what the unrounded value illustrates.
- Step 8: "Kiihtyvyydestä saat näin nopeuden" — add the condition stated in tvt-nopeus-datasta: the computed velocity starts at 0, so it is correct when the motion starts from rest (and after zero correction). Also `integral("v","t")` gives the displacement, which is the distance only for motion in one direction.
- Step 6: G = mg example is fine; "Jos ohjelma ei hyväksy desimaalipistettä, kokeile pilkkua" is a reasonable hedge.

## Checked
- UI names all in ga-facts.md: Manual Entry, Sensor Data Collection, Column Options (name, unit, displayed precision), double-click a cell, Add Manual Column, Add Calculated Column, Delete Column, Data Set Options > Add New Data Set / Rename Data Set, Export data as csv, .gambl, CSV open, Ctrl/Cmd C–V; custom expressions marked Pro; Pro list (expressions, manual fit, fit uncertainty, video) matches TIL 12770.
- Expression syntax matches TIL 11314: quoted column names, `"T"^2`, `sqrt("h")`, `1/"r"^2` (precedence correct), no parameters A/B, radians; delta (first row empty), sum (cumulative), integral (cumulative strip areas).
- Figure numbers: T for l = 0,200/0,300/0,400 m is 0,90/1,10/1,27 s (2π√(l/g)), T^2 correct (1,27^2 = 1,6129); labelled "esimerkkiarvoja"; measured vs calculated columns shown; no overlaps.
- Measured values kept, excluded points recorded with reason, not deleted.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Bold Finnish UI names checked against Lauri's GA v6.2.1 screenshots (cropped assets/pics/tvt/*.png and the uncropped originals in /mnt/project-files/ga-pro-kuvat/); English names in brackets checked against ga-facts.md. No invented Finnish names found.
- Verified: **Manuaalinen syöttö**, **Mittaa antureilla**, **Valitse tiedosto** (ga-aloitus.png); **Sarakkeen ominaisuudet**, **Lisää tyhjä sarake**, **Lisää laskettu sarake** (ga-sarakevalikko.png); **Näytettävä tarkkuus**, **Ota käyttöön** and the fields Nimi, Yksiköt (ga-sarakkeen-ominaisuudet.png). English: Export data as csv, Add New Data Set, Rename Data Set, Delete Column (ga-facts).
- Expressions consistent: "T"^2, sqrt("h"), 1/"r"^2 (^ binds before /), "m"*9.81; integral("a","t") = change of velocity (velocity only from rest), integral("v","t") = displacement. Correct.
- The hedge "Jos ohjelma ei hyväksy desimaalipistettä, kokeile pilkkua" is justified: Lauri's originals show a point in the result box but commas on the axes, so the locale is mixed.
