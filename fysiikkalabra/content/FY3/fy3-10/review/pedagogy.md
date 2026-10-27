VERDICT: PASS
CONTENT-HASH: fdcab429ebd8dd6e

## Blocking

## Polish
- inquiry.json laske-r solution, Vastaus — the limiting datum is "heliumin massa 0,83 g", but the Annettu line and the prompt give only n = 0,2075 mol. A student who has forgotten the punnitus table cannot see where 0,83 g comes from. Add "m = 0,83 g (punnituksesta)" to Annettu, or say "punnituksen massa 0,83 g" in Vastaus.
- laske-r Vastaus — the student computes 8,302 and the line says 8,3 (two figures) while the next sentence calls the pressure and volume three-figure. Add one clause: "tulos on yhtä tarkka kuin heikoin lähtötieto" so the drop from 8,302 to 8,3 reads as a rule, not a surprise.
- Carried from round 1 and still open (not touched by this diff): bare "josta" in the rearrangements of the example and L1-02..L2-02; "1/24 mol/l" in Järkevyys; clipped fraction in L3-01 at 390 px; L2-03 Vastaus wording; Level 3 "Perustele" prompts check only the number.

## Checked
- Delta is two solutions only (laske-r, balloon L3-0x); the rest is unchanged from the version I passed.
- laske-r: the stages stay in order, answer 8,3 with tolerance 0,02 accepts the student's 8,30 or 8,302; hints and mistake values (121,7; 8302; 0,008302) match the stage-by-stage solution.
- Balloon solution: 2644,8 kg in Sijoitus now rounds to the stated 2,64 · 10³ kg (the earlier 2645 gave an ambiguous rounding); 91 200 mol · 0,0290 kg/mol = 2644,8 recomputed.
- Balloon Järkevyys (1,2 kg/m³ estimate, scaled by 293/373, about 700 kg lighter) remains independent of the calculation and followable.
- Hash identical at start and end.
