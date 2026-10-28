VERDICT: PASS
CONTENT-HASH: 33a9fce30d742d8f

## Blocking

## Polish
- lesson.md:181 (Esimerkki, Tulos) — the rounding cites significant figures, but this is a subtraction, and the transfer task and L1-04 use the right rule (the least precise datum decides). Justify "kymmenen kilojoulen tarkkuudella"; the answer stays.
- inquiry.json:181 (ketju solution, Vastaus) — the same: "kaksi merkitsevää numeroa kuten tiedoissa $34\,\text{MJ}$" for a difference.
- lesson.md:98 — "Kun kahden energian kertaluku on hyvin erilainen, vertailuun riittää yksi jakolasku" is followed by $32\,\text{MJ}$ against $10\,\text{MJ}$, which are about the same order of magnitude. Reword it.
- lang/fi.json:247 `n_jaristys` — "M 9" is a plain numeral in the readout. Add a `t_jaristys` such as `\text{maanjäristys,}\ M\,9`, as was done for the other numbered names.

## Checked
- Hash 33a9fce30d742d8f at start and end. All round-2 blocking items are fixed: ennuste-1 ratio in LaTeX, tarkistus-2 mistakes $0{,}1$ and $0{,}01$ in LaTeX, and `t_*` TeX names used in the readout and the canvas (koe-2 capture checked).
- One script recomputed every lesson-answers.py value and matched each one: 340 kJ, 3,2, $6{,}25 \cdot 10^{20}\,\text{J}$ (625 EJ, given as 620), 41 days, 600 kJ, 1800 kJ, 66 MJ, 51 GJ, 100, 2500 J. The numeric mistakes and their feedback are right.
- All 28 sim values recomputed from their stated sources and found right: photon, AA cell, banana, petrol, LPG, OL3, Finland's electricity a day and a year, Finland's total energy, sunlight on Earth, M 9, the Sun's output.
- Sim code: prefixes and rungs are right from $10^{-19}$ to $10^{26}$, lg() places objects correctly, and the dot means source and the ring means estimate. The model box says the values are rounded orders of magnitude.
- Experiments: initial `kohde` names match the `n_*` strings. simState gives E_MJ 10 and 32, and E_EJ 620 for both koe-2 objects.
- Predictions: the right options are correct, and the "tuhat vuotta" feedback is right ($6 \cdot 10^{23}\,\text{J}$, about 40 days of sunlight).
- Figures are to scale: the ladder is 33,2 px a decade with 1,6 GJ and 140 TJ placed right, and the Sankey widths are 96 = 24 + 72 for 800 = 200 + 600.
- The worked example, siirto and tarkistus-2 are solved symbolically first, with conversions by substitution and real checks.
- Scope: no $E_k$, $E_p$, work, force, $Q = cm\Delta T$ or efficiency products.
- House rules: no ×, written division with a colon, and no plain numbers with units outside LaTeX (scripted scan).
