VERDICT: FAIL
CONTENT-HASH: 9971f42a92ccaa34
SCOPE: delta: new tasks s7 (Liukukitkan mittaus) and s8 (Käämin magneettikenttä ja virhelähteet) and the changed intro; older tasks s1-s6 untouched

## Blocking
- **s8 b, criterion 3 and Järkevyys (A, causality; 7, assessment).** The point is given for "Ei voi tietää, pysyykö riippuvuus suorana, esimerkiksi käämin lämmetessä", and the solution says the line may stop being straight because "suuri virta lämmittää käämin johdinta ja kasvattaa sen resistanssia". The graph is $B$ against the current $I$ itself. For a long air-core coil $B = \mu_0 n I$ (stated in the task) has no saturation, and a higher resistance changes the voltage needed for a given current, not $B$ at that current. A student who says "with no iron the law stays linear, so $4{,}9\,\text{A}$ is a sound estimate if the coil and supply can carry it" is right and loses the point. Fix: the point goes for noting that $4{,}9\,\text{A}$ is outside the measured range, so the coil (heating, insulation) and the supply must be able to give it, and the estimate is checked by measuring. Heating is a risk to the coil and supply, not a reason for nonlinearity.
- **s8 Yleisiä virheitä, second item (A, assessment).** "virraksi lasketaan $12 : 6{,}2 \cdot 2{,}5\,\text{A}$" is listed as a mistake, but $(12/6{,}2) \cdot 2{,}5\,\text{A} = 4{,}84\,\text{A}$ is a correct proportion for a line through the origin, and Hyväksytään myös accepts $4{,}8\text{–}5{,}0\,\text{A}$. Remove it or replace it with a real mistake (for example $I = kB$, or $I = 12 / 6{,}2\,\text{A}$).

## Polish
- s8 d (criterion 3 and model answer): "virta lämmittää käämiä ja muuttaa sen resistanssia" names no effect on the result. The effect is real only if the supply sets the voltage, so the current drifts between reading $I$ and $B$, or if the sensor drifts with temperature. Say which one.
- s8 a Vastaus: "luetut arvot ovat kaksi- tai kolminumeroisia". All four values read ($1{,}0$; $2{,}5$; $2{,}5$; $6{,}2$) have two figures.
- s7 a: the model answer's "vähintään nollakohdan osalta" is right. A scale (calibration) error would also leave the line through the origin. One clause saying so would stop "no systematic error" from reading as absolute.

## Checked
- One script (scratchpad rc.py) recomputed from the figure sources (fy4-6 `MITTAUS`, fy7-3 `DATA_I/DATA_B/FIT`) beside answers.py. s7: ratios 0,22/0,21/0,22/0,21/0,216, mean 0,2152, half-range 0,005; LSQ fit k = 0,214, b = 0,010 N (intercept ≈ 0, as a says); residuals ≤ 0,09 N; c 0,24 / 0,21 / 14,3 %; d 4,5 % and 0,93 %. s8: k = 2,467 mT/A (fit 2,465), n = 1963 1/m; b 4,86 A (4,85 with the offset); B(0,5 A) = 1,27 mT; c 3,08 % and 0,645 %. All agree, and the tolerances accept the two-figure and one-figure roundings.
- Physics: $F_\mu = \mu N$ at constant pulling speed; zero error shifts the points and leaves the slope; current reversal cancels a constant field; the Earth's field (~0,05 mT) is a plausible cause of 0,04 mT; the model's conditions (long, air-core, centre) are stated. Terms liukukitka(kerroin) are right. Scope FY1/FY4/FY7.
- Points: s7 3+4+4+3, s8 4+3+4+3, and the criteria add up to the part points. Intro: "Kahdeksan" matches 8 tasks.
- Figures: s7 shows points only, no line (alt text says so); s8 shows six points and the fitted line, with no slope written.
- `practice.py check` OK; hash the same at start and end.
