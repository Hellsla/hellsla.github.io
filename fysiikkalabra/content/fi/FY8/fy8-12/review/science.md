VERDICT: FAIL
CONTENT-HASH: 4c3e81cd3dc1c6cd

## Blocking
- lesson.md:456 — B: "Alfa-, beeta-, gamma- ja röntgensäteily ... ei muuta ytimiä" is stated as universal, but alpha particles do cause nuclear reactions (Rutherford's N → O transmutation, Chadwick's α + Be → n, Am–Be neutron sources), and that belongs to the FY8 content on nuclear reactions. The conclusion about sterilisation is right. — Fix: limit the claim to the case meant, e.g. "Steriloinnissa ja lääketieteessä käytetty gamma-, röntgen- ja beetasäteily ionisoi atomeja mutta ei muuta ytimiä", or add "käytännössä" and remove alfa from the list.

## Polish
- inquiry.json:117 — the model puts the source $3\,\text{cm}$ from the window. A $5{,}49\,\text{MeV}$ alpha has only about $1\,\text{cm}$ of air range (about $1{,}3\,\text{mg/cm}^2$) left there, and a typical end window ($1{,}5$–$2\,\text{mg/cm}^2$) would stop most of them. — Say that the model ignores the alpha's energy loss in air and in the window, or use a distance of about $1\,\text{cm}$.
- inquiry.json:64 — "alfalähteestä vain ... $9$, mikä on taustasäteilyn tasoa": 9 is more than twice the mean background of 4 (a 2 % fluctuation in the model). A student may read it as alpha getting through aluminium. — Add "satunnaisvaihtelun rajoissa", or pick a seed that gives a more typical value.
- inquiry.json:329, exit-ticket.json:3 — "hammasröntgenin fotonien energia noin $60\,\text{keV}$": about $60\,\text{kV}$ is the tube voltage, so it is the maximum photon energy; the mean is about half. The $d_{1/2} = 0{,}12\,\text{mm}$ fits 60 keV, so the task is consistent. — Write "suurimmillaan noin" or "jännitteellä noin $60\,\text{kV}$".

## Checked
- Recomputed all lesson-answers.py values. The sim model values (koe 1–3: 5/550/577, 9/4/535, 590/332/175/89/57) match the seeded generator, and the feedback and model-answer numbers match them (net 586, 328, 171; ratio 0,29).
- Half-value thicknesses from XCOM at 662 keV: Pb 5,50 mm, Fe 12,0 mm, Al 34,4 mm, concrete 39,1 mm, water 80,9 mm. Concrete about 7 × lead is correct. Paper 100 mm is correct for density 0,8.
- W = 34 eV (ICRU 33,97); water 12,6 eV; Am-241 5,49 MeV; Geiger's rule gives 4,09 cm in air; 1,6 · 10⁵ ion pairs, about 3900 per mm; tissue about 0,04 mm; mass ratio 7294.
- Beta model: E_max 2,28 MeV (Y-90 in Sr-90 equilibrium); Katz–Penfold range 1,10 g/cm², which is about 4 mm Al; μ = 17 · E^-1,14 = 6,6 cm²/g. Paper sheet 0,008 g/cm².
- GM tube about 500 V, wire positive, the avalanche and equal-sized pulses: correct at this level (C). The gamma detection-efficiency simplification is stated in the model text.
- Worked example 23,77 → 24 mm, with checks at 22 and 27,5 mm. Siirto 5,57 % and its three mistake values. XCOM Pb at 60 keV gives d½ = 0,122 mm.
- Figures: energy axis positions (12,6 eV, 60 keV, 662 keV, visible light) and the attenuation curves (Pb 5,5/11/16,5 mm; Al 0,60 at 25 mm) are to scale. Tarkista 2 graph: 800 → 400 at 12 mm, 50 at 48 mm.
- Each distractor in Ennuste 1–2, Etsi virhe and Tarkista 1 is wrong, and its feedback says why correctly.
- No de Broglie wavelength anywhere. Decimal comma, \cdot and LaTeX units throughout.
- Exercise findings are in exercises/review/science.md.
