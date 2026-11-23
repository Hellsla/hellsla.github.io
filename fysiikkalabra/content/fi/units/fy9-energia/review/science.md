VERDICT: PASS
CONTENT-HASH: db20474744c40f0e
SCOPE: full: unit.md (three new `pysahdy` boxes judged first; hero and ketju now raster images), inquiry.json, teacher.md, Sovella tasks s1–s9 with solutions, answers.py, figures.py.

## Blocking
- (none)

## Polish
- s8 a, Järkevyys: "Sisäenergiaa syntyy suunnilleen yhtä paljon kummallakin osamatkalla, mikä sopii kitkan tasaiseen vaikutukseen" is still not supported, because the task gives no lengths for the A–B and B–C parts of the path (carried over from the last review). Drop the clause.
- s7 d: the report text does say Lucid had the largest gap (46 %). But the page's own chart data give Opel Grandland 262/484 = −45,9 % and Lucid 520/960 = −45,8 %, so the two are effectively tied. "Testin raportin mukaan" attributes the claim correctly; "yksi suurimmista" would be safer.
- teacher.md: "Kaikki aineistot ovat keksittyjä esimerkkejä, eivät tilastoja" contradicts s7, which uses real NAF data. "muut viisi tehtävää" is out of date now that the set has nine tasks.
- s2 c, Järkevyys: a saving of 0,29 is "lähes kolmannes" or "noin 30 %", not "noin kolmannes".
- Inquiry `lataus`, feedback on the correct option: 600 Wh : 120 W = 5,0 h holds only if 120 W is the power that goes into the battery. If 120 W is the charger's input power and η < 1, the time is 5,0 h/η. The ratio and the correct option are unaffected.
- `prior` writes E = Hm while the Kaava section writes Q = Hm. Harmless.

## Checked
- Hash at start and at end: db20474744c40f0e.
- Pysähdy boxes: (1) teho tells how fast and hyötysuhde how large a share: correct, and matches Ydinajatus. (2) kWh is a unit of energy, 1 kWh = 3,6 MJ, kW is a unit of power: correct, and matches the conversion above it. (3) 0,90 · 0,45 · 0,98 = 0,397 < 0,45: each factor is below 1, so the product is below the smallest factor. The reasoning is correct and agrees with the johda box and the figure.
- Ketju figure (now webp): I measured the bands from the image at 0,347 px/MW: 500, 450, 198 MW and losses 50, 247,5, 4 MW. All agree within a pixel, so the claim that it is drawn to scale holds. The labels match 500·0,90·0,45·0,98 = 198 MW.
- One script recomputed every number in the unit text (320 MJ ≈ 90 kWh, 17 h), lt-1…lt-6, aineisto (bar heights 400/350/150/140 MW from the SVG; 42,86 % and every listed mistake value), sauna, sahkoauto, pelletti, hissi, tarkistus-1…3, the teacher.md −8 °C sum, and s1–s9 including every intermediate value and "hyväksytään myös" value. All agree with tasks.json, solutions.md and answers.py. Least squares for s3 gives −4,89 kWh/°C and 204 W/K.
- s7 data checked against the NAF page and its range-test article (fetched today): all three cars' ranges, the 24-car mean of −37,8 %, the 2025 figure of 18 % (−6…+8 °C), Inster stopping at −16 °C, Folldal −32 °C, and consumptions of 21,16 and 21,6 kWh/100 km all match.
- Energy wording follows P1 throughout. Rubric points match the tasks. Each choice question has exactly one correct option, and every distractor's feedback is correct.
