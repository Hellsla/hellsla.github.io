VERDICT: FAIL
CONTENT-HASH: 129dcdd5c074199d

## Blocking
- inquiry.json pred-3 feedback (Aino, Bea and Cem options) — all three refer to "Teoriatiivistelmä" / "Teoriatiivistelmässä", but the stage is named *Teoria* (CLAUDE.md "Lesson page" 5; the interface has no "Teoriatiivistelmä"). The student is sent to a heading that does not exist. — Write "luvun Teoria-osassa" / "Teoria-osassa" in all three.

## Polish
- inquiry.json pred-1 feedback ("Mittauksesi näyttävät…") and johtopäätös prompt ("mittaustesi perusteella", model "Oikeat syvyysmittarit tukevat mallia") — the values are model values from the simulation, which the Mallin oletukset box says itself. Use "mallin arvot" / "lukemasi" consistently.
- inquiry.json check-c2 repeats pred-3 (tube and pool, same reasoning, only 2,0 m changed to 1,0 m). As a check it tests recall, not transfer. Change the context (for example a lake and a bathtub at the same depth, or a tilted vessel).
- inquiry.json pred-3 is the only prediction that no experiment tests; the simulation cannot vary the vessel's width, so the misconception "more water means more pressure" is settled only by the derivation in the theory. That is acceptable, but the text could say so ("tämän todistaa johto, ei koe").
- lesson.md, the `scene` figure after Tiivistelmä: a second diver picture that explains nothing, and it comes after a list it does not illustrate. Drop it or move it beside the diver paragraph.
- The simulation readout prints the finished sum "p = p₀ + ρgh = 101 + 98,1 = 199,1", so pred-1 can be answered by copying the number. The numeric task still demands the difference, so this is not blocking.

## Checked
- The path follows from G = mg and the state variables. The opening dam question is answered in "Ilmanpaine ja ylipaine". The slot goals are met: p₀ as the constant term, the slope ρg, and force as a scalar because it is perpendicular to the surface.
- Pred-1 and exp-1 can refute the prediction. Only h varies, ρ is locked, and the pressure is read from the model. The misconception feedback names the p₀ constant.
- The worked example has seven stages, one step each, with the diagram-free chain symbolic first, units converted and a reasonableness check.
- The mercury barometer transfer has three progressive hints and real mistakes (water density, kPa).
- The graph task check-2 reads the slope and the intercept correctly. The distractor 2180 is realistic.
- The exit ticket tests p = F/A and ρgh, p₀. The workload is about an hour, since optional items are marked.
- The 390 px simulation capture is legible, and the text sits behind the Käyttöohje, Mallin oletukset and Laskennan selitys boxes.
- The formula row name "hydrostaattinen paine" is the teacher-approved exception and is not a finding.
- Not judged: the exercise set (reviewed apart). The hash was unchanged at the end of the review.
