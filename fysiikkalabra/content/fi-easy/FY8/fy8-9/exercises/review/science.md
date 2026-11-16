VERDICT: PASS
CONTENT-HASH: 2492493ba54a8626

## Blocking

## Polish
- exercises/solutions.md:148 (fy8-9-L2-05 Vastaus) — nettomäärän 64 vaihteluksi otetaan $\sqrt{64}$; vaihtelu tulee mitatusta määrästä ($\sqrt{72} \approx 8{,}5$), ja myös alkuarvon 283 vaihtelu (noin 6 %) vaikuttaa, joten "noin ±8 %" on hieman alakanttiin (lähempänä 10 %) — kirjoita $\sqrt{72}$ ja "noin 10 %" tai sano, että arvio on karkea.
- exercises/solutions.md (fy8-9-L3-04 a) — $\ln(71{,}2 : 32{,}8) = 0{,}7751$ antaa $64{,}39\,\text{h}$, ratkaisussa $64{,}38\,\text{h}$; vastaus $2{,}68\,\text{d}$ ei muutu — korjaa välitulos.
- exercises/solutions.md:229 (fy8-9-L3-05 c) — $\left(\tfrac{1}{2}\right)^{8{,}0/8{,}02} = 0{,}5009$, ei $0{,}5008$; tulos $50{,}1\,\%$ on oikein.
- exercises/solutions.md:180 (fy8-9-L3-01) — kolmen merkitsevän numeron perustelu nojaa vain osuuteen $38{,}0\,\%$; $5700\,\text{a}$:n tarkkuus on epäselvä — sano, että puoliintumisaika tulkitaan vähintään kolmen numeron tarkkuudella.
- packet — the deterministic checks of this packet say "check_lesson.py has not been run"; run them before the gate if it needs them.

## Checked
- All 19 numeric answers recomputed from the fi-easy task texts and tables with own formulas (one script): every one agrees with exercises.json and answers.py, well inside its tolerance; units and tolerances fit the data.
- The clearer-language texts keep every number, table, condition, step and justification of the solutions; "vaihtelu" for the scatter $\sqrt{N}$ is a fair simplification and used consistently.
- L2-05: net counts, two-point 149 s vs log-linear fit of all points 150 s (inside 6 %); L2-06 net data follow 60 s, the student's 70 s reproduced; L2-07 sum 80, 5,4 %.
- L3-04: table consistent with 800 MBq (6,0 h) + 200 MBq (64,4 h); short-lived part 0,012 MBq at 96 h; other point pairs inside 5 %.
- L3-05: $T_\text{eff} = 3{,}06\,\text{d}$, $T_\text{bio} = 4{,}96\,\text{d}$, decay constants add to 0,2262 1/d; the additive model and the meaning of the effective half-life are stated in the task.
- L1-06 and L1-09: exactly one correct option; each distractor wrong for the reason its feedback gives; graph functions give 400/200/100/50 kBq (C), 294/108/15 kBq (D), zero at 4 h (A) and 2,8 h (B).
- Half-lives realistic; Co-60 $\lambda$ matches 5,27 a; Am-241 mass 0,29 µg.
- Conditions stated in the tasks: no new radon or strontium, daughter decays excluded, constant background, activity per gram of carbon.
- Notation ($N$, $A$, $\lambda$, $T_{1/2}$) as in the fi-easy lesson brief; symbolic solution before substitution; scope inside the FY8 decay law.
