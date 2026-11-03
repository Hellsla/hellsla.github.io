VERDICT: PASS
CONTENT-HASH: 47e5964342e7a136

## Blocking

## Polish
- lesson.md:456: "lääketieteessä käytetty ... röntgen- ja elektronisäteily ... energia ei riitä muuttamaan ytimiä" is true for sterilisation, which is limited to 10 MeV electrons and 5 MeV X-rays, and for diagnostics. Radiotherapy linacs at 15–18 MV do produce photoneutrons and a little activation in the machine head. This is not a misleading picture at this level (C to B), and "lähinnä neutronisäteily" softens it. — If wanted, write "Steriloinnissa ja diagnostiikassa käytetty ...".

## Checked
- The round-1 blocker is fixed. lesson.md:456 now limits the claim to gamma, X-ray and electron radiation used in sterilisation and medicine, and leaves alpha out. inquiry.json:947 ("alfa ... ei muuta kudoksen ytimiä radioaktiivisiksi") and exit-ticket.json:3 / the exit answer (gamma does not change nuclei, Co-60 and Cs-137 energies are below photonuclear thresholds) are correct.
- inquiry.json:117: the model now says it ignores the alpha's energy loss in air and in the window. That is correct and honest.
- inquiry.json:64: "4 ja 9 ... satunnaisvaihtelun rajoissa taustasäteilyn tasoa" is acceptable. With a Poisson mean of 4, P(N ≥ 9) is about 2 %.
- inquiry.json:329 and exit-ticket.json:3: "suurin energia / suurimmillaan noin 60 keV" is correct, and d½ = 0,12 mm (XCOM Pb 60 keV: 0,122 mm) stays consistent. Siirto: 0,5^(0,50/0,12) = 5,57 %.
- Ennuste 2 (inquiry.json:95): 0,5^(10/5,5) = 0,284 matches "hieman yli neljäsosan" and the model's 171/586 = 0,29. Exactly one option is correct, and each distractor's feedback is right.
- The sim model values (5/550/577, 9/4/535, 590/332/175/89/57) and net values (586, 328, 171) are unchanged and consistent.
- No new errors in the edited sentences. Decimal comma, \cdot and LaTeX units are kept.
