VERDICT: PASS
CONTENT-HASH: 7e97e3c17fba5c23

## Blocking

## Polish
- lesson.md (Osittainen heijastuminen) — "Siksi järven pinta peilaa iltaisin rannan puut": the reason is the large angle of incidence (looking across the lake at grazing angles) together with the bright shore and the dark water below. "Iltaisin" suggests that the time of day is the cause. Fix: "kun katsoo pintaa loivasti kauas" (C if left as it is).

## Checked
- Round-1 blocker fixed. The hook now says "katso lasia vinosti ylhäältä". Näennäinen syvyys states the oblique view through the surface and links the raised image to the sideways shift. Both agree with tarkistus-3 and the depth figure, where the apparent coin is raised and displaced toward the eye.
- Both round-1 polish items are done: "samalla tulokulmalla", and "näkyvälle valolle läpinäkyvissä aineissa" for n > 1. "Mitä suurempi tulokulma … pintaa hipoen" is correct: the unpolarised Fresnel R rises monotonically with the angle for every pair of materials in the sim, which I checked numerically.
- I recomputed every number independently in one script: the example (38,02°, 2,256·10⁸ m/s), R 4,3 %/2,0 %, ennuste-1 28,9°, ennuste-2 22,1°→40,6° (1,84×), the koe-1 angle ratios 1,36/1,48, koe-2 35,2/30,9/30,3/18,5°, virhe 0,651 → 40,6°, siirto 41,68° (25,94° in the glass, mistakes 22,08 and 39,9), tarkistus-2 1,470 (0,680; 1,592), nopeus 2,013 (4,47), and the exit ticket β = 25°, 50° and n = 1,33.
- The mittaus least-squares fit reproduces A = 1,4895, B = −0,0041 and ΔA = 0,0162. The read point (0,60; 0,89) is on the line. The mistakes 0,671 = 1 : A and 1,79 = 70 : 39 are right, and so are the single-row ratios 1,42 and 1,49.
- The figures are to scale. Interface: 49,9° → 35,2°. Depth: two rays obey Snell within 0,2°, and their back-extensions meet at the drawn apparent position. Graph end points: 48,8° and 24,4°.
- sim.js: β = α₁, Snell, the TIR condition, Fresnel rs/rp and T = 1 − R. The 390 px capture shows 28,9° and R = 2,4 % at 40°. The simState keys cover every measure. The locks isolate α (koe-1) and m₂ (koe-2), and TIR cannot occur in either. The model box states its limits and says the readings are model values.
- Each choice item has exactly one correct option, and each distractor's feedback names the actual error. Wavefront causality, the unchanged frequency and λ shortened 1,33-fold are all correct.
- The scope fits the LOPS FY7 content "valon heijastuminen, taittuminen", and total internal reflection is deferred to its own chapter. The CRC 97th ed. (2016) is named.
