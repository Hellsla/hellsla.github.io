VERDICT: PASS
CONTENT-HASH: 010cc9be0b649006

## Blocking

## Polish
- exercises/solutions.md:801 (fy8-9-L2-05 Vastaus) — nettomäärän 64 hajonnaksi otetaan $\sqrt{64}$; hajonta tulee mitatusta määrästä ($\sqrt{72} \approx 8{,}5$), ja myös alkuarvon 283 hajonta (noin 6 %) vaikuttaa, joten "noin ±8 %" on hieman alakanttiin (lähempänä 10 %) — kirjoita $\sqrt{72}$ ja "noin 10 %" tai sano, että arvio on karkea.
- exercises/solutions.md:862 (fy8-9-L3-04 a) — $\ln(71{,}2 : 32{,}8) = 0{,}7751$ antaa $64{,}39\,\text{h}$, ratkaisussa $64{,}38\,\text{h}$; vastaus $2{,}68\,\text{d}$ ei muutu — korjaa välitulos.
- exercises/solutions.md:882 (fy8-9-L3-05 c) — $\left(\tfrac{1}{2}\right)^{8{,}0/8{,}02} = 0{,}5009$, ei $0{,}5008$; tulos $50{,}1\,\%$ on oikein.
- exercises/solutions.md:833 (fy8-9-L3-01) — kolmen merkitsevän numeron perustelu nojaa osuuteen $38{,}0\,\%$; $5700\,\text{a}$:n tarkkuus on tekstissä epäselvä (2–4 numeroa) — mainitse, että puoliintumisaika tulkitaan vähintään kolmen numeron tarkkuudella.

## Checked
- All 19 numeric answers recomputed from the task text with own formulas (one script): every one agrees with exercises.json and answers.py, well inside its tolerance; units and tolerances fit the data.
- Table tasks: L2-05 net counts, two-point 149 s vs log-linear fit of all points 150 s (inside 6 %); L2-06 net data follow $T_{1/2} = 60\,\text{s}$, the student's 70 s reproduced from the raw totals; L2-07 sum 80, 5,4 %.
- L3-04: table consistent with 800 MBq (6,0 h) + 200 MBq (64,4 h); short-lived part 0,012 MBq at 96 h, so the late points isolate the long-lived nuclide; other point pairs stay inside 5 %.
- L3-05: $T_\text{eff} = 3{,}06\,\text{d}$, $T_\text{bio} = 4{,}96\,\text{d}$, $\lambda$ sum 0,2262 1/d; the additive-rate model is stated in the task.
- Multiple choice L1-06 and L1-09: exactly one correct option, each distractor wrong for the reason its feedback gives; figure functions give 400/200/100/50 kBq (C), 294/108/15 kBq (D), zero at 4 h (A) and 2,8 h (B).
- Half-lives realistic (Tc-99m, Rn-222, Cs-137, Co-60, Sr-90, I-131, F-18, Am-241, C-14); Co-60 $\lambda$ matches 5,27 a; Am-241 mass 0,29 µg.
- Conditions stated in the tasks: no new radon, daughter decays excluded (L3-03), constant background, activity per gram of carbon (L3-01).
- Solutions solve symbolically before substitution; notation ($N$, $A$, $\lambda$, $T_{1/2}$) as in the lesson brief; scope inside FY8 hajoamislaki.
