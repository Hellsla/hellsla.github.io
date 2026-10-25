VERDICT: PASS
CONTENT-HASH: 913ef7425cccfe05

## Blocking
(none)

## Polish
- lesson.md:10 — "Siksi pullon kyljessä olevasta alimmasta reiästä..." : "Siksi" follows the equal-in-all-directions sentence, but the jet strength follows from pressure growing with depth; the bottle is also not introduced ("pullon" out of nowhere) — rewritten in the diff.
- lesson.md:12 — "Se on ... , ja se vaikuttaa ... ja välittyy sen kautta": three pronouns "se/sen" in one sentence, "sen" ambiguous — split in the diff.
- lesson.md:14 — "ylipaine" is used here for the first time but only defined at line 27 (Δp = p − p₀); a short "eli paineen ilmanpainetta suurempi osa" at first use fixes it. The next "Se" is replaced by "Ylipaine" for clarity.
- glossary.json — "kokonaispaine" is used throughout (lesson, sim, solutions) but has no entry; consider adding one (not a language defect).

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -7,11 +7,11 @@
 
 Kaasun paine syntyy mikromallin mukaan hiukkasten törmäyksistä astian seinämään. Nesteen paine syntyy nesteen omasta painosta: jokaisen vesikerroksen yllä on vettä, joka painaa sitä. Mitä syvemmällä ollaan, sitä enemmän vettä on yläpuolella ja sitä suurempi paine on. Levossa olevassa nesteessä pinnan alla olevaan vaakasuoraan pintaan, jonka pinta-ala on A, kohdistuu sen yläpuolisen vesipatsaan paino. Patsaan korkeus on syvyys h ja tilavuus V = Ah. Tiheys ρ on massa tilavuutta kohti (m = ρV), joten patsaan massa on ρAh ja paino G = mg = ρAhg. Paine on paino jaettuna alalla, joten pinta-ala supistuu pois ja jäljelle jää ρgh. Tätä nesteen painosta syntyvää painetta sanotaan hydrostaattiseksi paineeksi. Se ei riipu astian muodosta eikä veden kokonaismäärästä, vaan ainoastaan syvyydestä ja nesteen tiheydestä.
 
-Paine ei ole voima vaan voiman ja alan suhde, ja levossa olevassa nesteessä paine vaikuttaa joka suuntaan yhtä suurena. Jos paine sivulle olisi pienempi kuin alaspäin, vesi valuisi sivuun eikä pysyisi levossa. Siksi pullon kyljessä olevasta alimmasta reiästä vesi suihkuaa voimakkaimmin. Paineen aiheuttama voima on aina kohtisuorassa pintaa vastaan: padon pystysuoraan seinään voima osoittaa vaakasuoraan, sukeltajan kehoon joka puolelta. Siksi voima voidaan tässä laskea pelkkänä suuruutena, suunta tulee pinnasta.
+Paine ei ole voima vaan voiman ja alan suhde, ja levossa olevassa nesteessä paine vaikuttaa joka suuntaan yhtä suurena. Jos paine sivulle olisi pienempi kuin alaspäin, vesi valuisi sivuun eikä pysyisi levossa. Jos pullon kylkeen tekee reikiä usealle korkeudelle, alimmasta reiästä vesi suihkuaa voimakkaimmin, koska paine kasvaa syvyyden mukana. Paineen aiheuttama voima on aina kohtisuorassa pintaa vastaan: padon pystysuoraan seinään voima osoittaa vaakasuoraan, sukeltajan kehoon joka puolelta. Siksi voima voidaan tässä laskea pelkkänä suuruutena, suunta tulee pinnasta.
 
-Veden pinnalla vaikuttaa jo ilmakehän paine eli ilmanpaine, joka on merenpinnan tasolla noin 101 kPa. Se on ilmapatsaan paino pinta-alaa kohti, ja se vaikuttaa myös veden pintaan ja välittyy sen kautta syvyyteen. Veden alla kokonaispaine on siis ilmanpaineen ja hydrostaattisen paineen summa. Kymmenen metrin syvyydessä hydrostaattinen paine on jo suunnilleen yhden ilmanpaineen suuruinen.
+Veden pinnalla vaikuttaa jo ilmakehän paine eli ilmanpaine, joka on merenpinnan tasolla noin 101 kPa. Se on ilmapatsaan paino pinta-alaa kohti. Ilmanpaine vaikuttaa myös veden pintaan ja välittyy veden kautta syvyyteen. Veden alla kokonaispaine on siis ilmanpaineen ja hydrostaattisen paineen summa. Kymmenen metrin syvyydessä hydrostaattinen paine on jo suunnilleen yhden ilmanpaineen suuruinen.
 
-Tämä vastaa alun kysymykseen. Ilmanpaine vaikuttaa padon muuriin molemmilta puolilta, joten muuria kuormittaa vain veden ylipaine. Se on yläreunassa nolla ja kasvaa syvyyden mukana tasaisesti: 30 metrin syvyydessä se on noin 290 kPa, eli jokaiseen muurin neliömetriin kohdistuu noin 290 kN:n voima. Siksi muurin alaosan on kestettävä paljon suurempi voima kuin yläosan, ja muuri tehdään pohjalta paksuksi.
+Tämä vastaa alun kysymykseen. Ilmanpaine vaikuttaa padon muuriin molemmilta puolilta, joten muuria kuormittaa vain veden ylipaine eli paineen ilmanpainetta suurempi osa. Ylipaine on yläreunassa nolla ja kasvaa syvyyden mukana tasaisesti: 30 metrin syvyydessä se on noin 290 kPa, eli jokaiseen muurin neliömetriin kohdistuu noin 290 kN:n voima. Siksi muurin alaosan on kestettävä paljon suurempi voima kuin yläosan, ja muuri tehdään pohjalta paksuksi.
 
 ## Kaava
 Paine on pintaa vastaan kohtisuora voima jaettuna pinta-alalla:
```

## Checked
- New derivation (lesson.md:8): grammar, case endings and logic ("V = Ah", "m = ρV", "G = mg = ρAhg", "pinta-ala supistuu pois") correct and readable for 16–19-year-olds.
- Dam paragraph (lesson.md:14): "290 kN:n voima", "30 metrin syvyydessä", register and tone fine; hook at line 3 answered.
- Δp notation consistent between lesson.md:27, solutions.md (L1-02, L1-05, L2-02, L2-03, L3-02, L3-03) and glossary.json "ylipaine" (definition is correct Finnish).
- Example closing sentences (lesson.md:53): "180 kg:n massan painoa, vaikka ikkuna on pieni", "kehon nesteet välittävät sen", "Vain kehon ilmatilojen ... paine on tasattava" are correct.
- Misconception paragraph (lesson.md:56) "pelkkä ρgh antaa vain ylipaineen" is clear and consistent with the terminology.
- sim.js Finnish strings (labels, readout, note, "Näytä vain ylipaine", "ylipaine ρgh (kPa)", "kertaa ilmanpaine", en dash in "0–200") and sim-spec.md, exit-ticket.json, exercises.json texts: spelling, decimal comma, minus sign (fi() uses −) correct.
- Number-plus-unit case endings (12 m:n, 150 cm², 180 kg:n, 290 kN:n, 4,0 m:n) correct; no "80 N voimalla" type slips.
- Terminology matches glossary.json (paine, pascal, hydrostaattinen paine, ilmanpaine, ylipaine, tiheys); meta.json glossary list includes ylipaine; glossary.json parses.
- lint_lesson.py fy3-4: 0 errors, 0 warnings. Diff applies cleanly (patch --dry-run). Hash unchanged between start and end of review.
