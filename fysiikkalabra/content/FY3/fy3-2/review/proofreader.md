VERDICT: FAIL

Reviewer: proofreader. Scope: lesson.md, exercises.json (text only), solutions.md, exit-ticket.json, sim-spec.md, sim.js (Finnish strings). No lesson file was edited; proposed fixes are in the diff below (copies in scratchpad/proofread/, diffed with `diff -u` against the originals). Numbers, formulas, LaTeX and JSON values are unchanged; exercises.json still parses.

FAIL reason: real grammar/word errors (items 1-3 below).

## Issue kinds

1. Case-ending errors on number+unit modifiers (real grammar errors). A numeral with a unit symbol in an attribute position needs the genitive with a colon: "25 m matka" should be "25 m:n matka", "80 N voimalla" "80 N:n voimalla", "1,2 m korkeudelle" "1,2 m:n korkeudelle", "36 kJ työn" "36 kJ:n työn", "850 kg betonielementtiä" "850 kg:n betonielementtiä", "180 W tehon" "180 W:n tehon". Also "12 s aikana" and "30 s aikana" are changed to "sekunnissa". Files: exercises.json L1-01, L1-02, L1-04, L2-03, L3-03.
2. Non-word: lesson.md tiivistelmä "nollatyötä" is not a Finnish word. Reworded (kannatteleva voima tekee työtä nolla joulea).
3. Wrong or unclear terminology and wording:
   - lesson.md "painoa paikallaan ... työtä painoon": "paino" is a force in physics (glossary-wise), so it is reworded to "painavaa esinettä / esineeseen".
   - "Työtä syntyy" is changed to "Työtä tehdään", because the lesson itself says work transfers energy.
   - "kaksinkertainen virhe" is changed to "kaksi kertaa liian suuri".
   - "siihen kuluneella ajalla" is changed to "sen tekemiseen kuluneella ajalla".
   - The sentence fragment "Liike-energia ... jotka tulivat tutuiksi FY2-moduulissa:" is now a complete sentence.
   - solutions L2-04: "hetkellinen teho" contradicts the task, which asks for keskimääräinen teho. The word is removed.
4. Awkward or ungrammatical sanity-check sentences in solutions.md: L1-02 "Täsmää." (now "Tulos täsmää."), L1-03 "saman kuin ... Tuntuu oikealta rauhallisesta vauhdista", L1-05 "nostaisi" and a bare fragment, L2-01 "kolaritarkasteluista" (an odd word), L2-03 "tavallinen nosturin nopeus", L3-02 "josta" with a plural antecedent. All reworded.
5. Typographic nits (PASS-level, not changed):
   - All spaces before units are ordinary spaces, not thin spaces (U+202F). The gold lesson does the same, so a bulk conversion is left to the human or the build step.
   - lesson.md uses "20 cm" (L34) while the rest is SI (0,20 m). The conversion-free wording is fine for a first read, but SI-only is stated in CLAUDE.md.
   - solutions L2-04 compares with "hevosvoima", a non-SI unit. It is only a side comparison.
   - The heading "Kaavat" differs from the gold "Kaava". This is structural, not mine to change.
   - No Finnish quotation marks are used anywhere, so nothing to fix.
   - The decimal comma is correct in all prose. sim.js uses the fi() helper for the decimal comma in the readouts.
6. Checked and OK:
   - exit-ticket.json, sim-spec.md and the sim.js Finnish strings ("Vedä", "Voima F", "Matka s", "Aika t", "Tehty työ tähän mennessä", "W = pinta-ala") contain no errors.
   - Terms match glossary.json: työ, energia, teho, liike-energia, potentiaalienergia.
   - The lesson says "matka", where the glossary definition of työ says "siirtymä". This is acceptable within the FY3 scope (W = Fs).
   - Reading level is suitable for ages 16-19.

## Diff

```diff
--- a/lesson.md
+++ b/lesson.md
@@ -18,13 +18,13 @@
 
 Jos voima muuttuu matkan aikana, työ on (s,F)-kuvaajassa voiman käyrän ja s-akselin väliin jäävä pinta-ala. Vakiovoimalla pinta-ala on suorakulmio F · s, joten sama kaava toimii molemmissa tapauksissa.
 
-Liike-energia ja painovoiman potentiaalienergia, jotka tulivat tutuiksi FY2-moduulissa:
+Liike-energian ja painovoiman potentiaalienergian kaavat ovat tuttuja FY2-moduulista:
 ```latex
 E_k = \tfrac{1}{2} m v^2 \qquad E_p = m g h
 ```
 missä m on massa (kg), v nopeus (m/s), g = 9,81 m/s² ja h korkeus valitusta nollatasosta (m).
 
-Teho on työ jaettuna siihen kuluneella ajalla. Tasaisessa liikkeessä teho voidaan laskea myös voiman ja nopeuden tulona, koska s/t = v:
+Teho on työ jaettuna sen tekemiseen kuluneella ajalla. Tasaisessa liikkeessä teho voidaan laskea myös voiman ja nopeuden tulona, koska s/t = v:
 ```latex
 P = \frac{W}{t} = F v
 ```
@@ -52,13 +52,13 @@
 
 Sama tulos saadaan keskimääräisellä voimalla 20 N: $W = 20\ \text{N} \cdot 0{,}20\ \text{m} = 4{,}0\ \text{J}$. Jos venytys kestää 0,50 s, teho on $P = 4{,}0\ \text{J} / 0{,}50\ \text{s} = 8{,}0\ \text{W}$.
 
-Huomaa, että jousen loppupään voimalla 40 N laskettu $40\ \text{N} \cdot 0{,}20\ \text{m} = 8{,}0\ \text{J}$ olisi kaksinkertainen virhe: voima ei ollut 40 N koko matkalla.
+Huomaa, että jousen loppupään voimalla 40 N laskettu $40\ \text{N} \cdot 0{,}20\ \text{m} = 8{,}0\ \text{J}$ olisi kaksi kertaa liian suuri: voima ei ollut 40 N koko matkalla.
 
 ## Yleinen virhekäsitys
-Työ ei ole sama asia kuin ponnistelu. Kun pidät painoa paikallaan tai kannat sitä tasaisella lattialla, et tee fysiikan tarkoittamaa työtä painoon, vaikka väsyt. Työtä syntyy vain, kun voima siirtää kappaletta omaan suuntaansa. Toinen yleinen virhe on sotkea työ ja teho: suuri teho ei tarkoita suurta työtä, vaan nopeasti tehtyä työtä.
+Työ ei ole sama asia kuin ponnistelu. Kun pidät painavaa esinettä paikallaan tai kannat sitä tasaisella lattialla, et tee fysiikan tarkoittamaa työtä esineeseen, vaikka väsyt. Työtä tehdään vain, kun voima siirtää kappaletta omaan suuntaansa. Toinen yleinen virhe on sotkea työ ja teho: suuri teho ei tarkoita suurta työtä, vaan nopeasti tehtyä työtä.
 
 ## Tiivistelmä
 - Liikkeen suuntainen vakiovoima tekee työn $W = F s$. Muuttuvalla voimalla työ on (s,F)-kuvaajan pinta-ala.
-- Voima, joka ei siirrä kappaletta omaan suuntaansa, ei tee työtä. Kantaminen tasaisella alustalla on fysiikassa nollatyötä.
+- Voima, joka ei siirrä kappaletta omaan suuntaansa, ei tee työtä. Kun kannat kappaletta tasaisella alustalla, kannatteleva voima tekee työtä nolla joulea.
 - Työ siirtää energiaa: tehty työ kasvattaa kappaleen liike- tai potentiaalienergiaa.
 - Teho on työ aikayksikössä, $P = W/t$. Yksiköt: 1 J = 1 N·m, 1 W = 1 J/s.
--- a/exercises.json
+++ b/exercises.json
@@ -1,20 +1,20 @@
 {
   "level1": [
-    { "id": "fy3-2-L1-01", "level": 1, "text": "Mopoa työnnetään 25 m matka 80 N voimalla liikkeen suuntaan. Kuinka suuren työn työntävä voima tekee?", "answer": 2.0, "unit": "kJ", "tolerance": 0.05 },
-    { "id": "fy3-2-L1-02", "level": 1, "text": "Kirjahylly (m = 15 kg) nostetaan lattialta 1,2 m korkeudelle. Kuinka paljon hyllyn potentiaalienergia kasvaa?", "answer": 177, "unit": "J", "tolerance": 0.02 },
+    { "id": "fy3-2-L1-01", "level": 1, "text": "Mopoa työnnetään 25 m:n matka 80 N:n voimalla liikkeen suuntaan. Kuinka suuren työn työntävä voima tekee?", "answer": 2.0, "unit": "kJ", "tolerance": 0.05 },
+    { "id": "fy3-2-L1-02", "level": 1, "text": "Kirjahylly (m = 15 kg) nostetaan lattialta 1,2 m:n korkeudelle. Kuinka paljon hyllyn potentiaalienergia kasvaa?", "answer": 177, "unit": "J", "tolerance": 0.02 },
     { "id": "fy3-2-L1-03", "level": 1, "text": "Pyöräilijän ja pyörän yhteinen massa on 85 kg ja nopeus 6,0 m/s. Laske liike-energia.", "answer": 1530, "unit": "J", "tolerance": 0.02 },
-    { "id": "fy3-2-L1-04", "level": 1, "text": "Hissin moottori tekee 36 kJ työn 12 s aikana. Mikä on moottorin teho?", "answer": 3.0, "unit": "kW", "tolerance": 0.05 },
+    { "id": "fy3-2-L1-04", "level": 1, "text": "Hissin moottori tekee 36 kJ:n työn 12 sekunnissa. Mikä on moottorin teho?", "answer": 3.0, "unit": "kW", "tolerance": 0.05 },
     { "id": "fy3-2-L1-05", "level": 1, "text": "Vesipumpun teho on 1,5 kW. Kuinka suuren työn pumppu tekee 4,0 minuutissa?", "answer": 360, "unit": "kJ", "tolerance": 0.02 }
   ],
   "level2": [
     { "id": "fy3-2-L2-01", "level": 2, "text": "Henkilöauto (m = 1200 kg) kiihdytetään levosta nopeuteen 90 km/h. Kuinka suuren työn kiihdyttävä voima tekee autoon?", "answer": 375, "unit": "kJ", "tolerance": 0.02 },
     { "id": "fy3-2-L2-02", "level": 2, "text": "Sähkökiukaan teho on 6,0 kW. Kuinka paljon sähköenergiaa kiuas käyttää 45 minuutin lämmityksen aikana? Anna vastaus megajouleina.", "answer": 16.2, "unit": "MJ", "tolerance": 0.02 },
-    { "id": "fy3-2-L2-03", "level": 2, "text": "Nosturi nostaa 850 kg betonielementtiä tasaisella nopeudella. Nosturin teho on 12 kW. Kuinka korkealle elementti nousee 30 s aikana?", "answer": 43.2, "unit": "m", "tolerance": 0.02 },
+    { "id": "fy3-2-L2-03", "level": 2, "text": "Nosturi nostaa 850 kg:n betonielementtiä tasaisella nopeudella. Nosturin teho on 12 kW. Kuinka korkealle elementti nousee 30 sekunnissa?", "answer": 43.2, "unit": "m", "tolerance": 0.02 },
     { "id": "fy3-2-L2-04", "level": 2, "text": "Juoksija (m = 62 kg) juoksee portaat ylös 12 sekunnissa. Korkeusero on 15 m. Mikä on juoksijan keskimääräinen teho painovoimaa vastaan?", "answer": 760, "unit": "W", "tolerance": 0.02 }
   ],
   "level3": [
     { "id": "fy3-2-L3-01", "level": 3, "text": "Hiihtäjä (m = 75 kg) laskee levosta mäen, jonka korkeusero on 40 m, ja saavuttaa mäen juurella nopeuden 20 m/s. Kuinka paljon energiaa kitka ja ilmanvastus veivät laskun aikana?", "answer": 14.4, "unit": "kJ", "tolerance": 0.02 },
     { "id": "fy3-2-L3-02", "level": 3, "text": "Kuorma-auto vetää perävaunua tasaisella nopeudella 80 km/h. Vetovoima on 4,5 kN. Kuinka suuri on vetovoiman teho? Perustele kaava, jota käytät.", "answer": 100, "unit": "kW", "tolerance": 0.02 },
-    { "id": "fy3-2-L3-03", "level": 3, "text": "Mökin aurinkopaneeli tuottaa keskimäärin 180 W tehon. Kuinka monta minuuttia paneelin pitää tuottaa sähköä, jotta energia riittäisi pumppaamaan 1000 kg vettä 50 m korkeammalla olevaan säiliöön? Oleta, että kaikki energia menee veden nostamiseen.", "answer": 45.4, "unit": "min", "tolerance": 0.02 }
+    { "id": "fy3-2-L3-03", "level": 3, "text": "Mökin aurinkopaneeli tuottaa keskimäärin 180 W:n tehon. Kuinka monta minuuttia paneelin pitää tuottaa sähköä, jotta energia riittäisi pumppaamaan 1000 kg vettä 50 m korkeammalla olevaan säiliöön? Oleta, että kaikki energia menee veden nostamiseen.", "answer": 45.4, "unit": "min", "tolerance": 0.02 }
   ]
 }
--- a/solutions.md
+++ b/solutions.md
@@ -12,7 +12,7 @@
 **Kaava:** E_p = m g h
 **Sijoitus:** ΔE_p = 15 kg · 9,81 m/s² · 1,2 m = 176,58 J
 **Vastaus:** 177 J
-**Järkevyys:** Hylly painaa noin 150 N; sen nostaminen reilun metrin vaatii alle 200 J. Täsmää.
+**Järkevyys:** Hylly painaa noin 150 N; sen nostaminen reilun metrin vaatii alle 200 J. Tulos täsmää.
 
 ## fy3-2-L1-03
 **Annettu:** m = 85 kg, v = 6,0 m/s
@@ -20,7 +20,7 @@
 **Kaava:** E_k = ½ m v²
 **Sijoitus:** E_k = ½ · 85 kg · (6,0 m/s)² = 1530 J
 **Vastaus:** 1530 J
-**Järkevyys:** Reilun kilojoulen verran, eli saman kuin pyöräilijän nostaminen noin 1,8 m. Tuntuu oikealta rauhallisesta vauhdista.
+**Järkevyys:** Noin puolitoista kilojoulea, eli yhtä paljon kuin pyöräilijän nostaminen noin 1,8 m korkeammalle. Luku sopii rauhalliseen vauhtiin.
 
 ## fy3-2-L1-04
 **Annettu:** W = 36 kJ = 36 000 J, t = 12 s
@@ -36,7 +36,7 @@
 **Kaava:** P = W / t ⇒ W = P t
 **Sijoitus:** W = 1500 W · 240 s = 360 000 J
 **Vastaus:** 360 kJ
-**Järkevyys:** Tällä energialla nostaisi 1000 kg vettä noin 37 m. Neljä minuuttia pumppausta, uskottavaa.
+**Järkevyys:** Tällä energialla voisi nostaa 1000 kg vettä noin 37 m. Neljän minuutin pumppaukselle tulos on uskottava.
 
 ## fy3-2-L2-01
 **Annettu:** m = 1200 kg, v₀ = 0, v = 90 km/h = 25 m/s
@@ -44,7 +44,7 @@
 **Kaava:** W = ΔE_k = ½ m v² − ½ m v₀²
 **Sijoitus:** W = ½ · 1200 kg · (25 m/s)² − 0 = 375 000 J
 **Vastaus:** 375 kJ
-**Järkevyys:** Nopeuden muunnos 90 km/h = 90/3,6 m/s = 25 m/s. Satojen kilojoulien liike-energia maantienopeudessa on tuttu luku kolaritarkasteluista.
+**Järkevyys:** Nopeuden muunnos 90 km/h = 90/3,6 m/s = 25 m/s. Maantienopeudella ajavan auton liike-energia on satoja kilojoulea, joten tulos on uskottava.
 
 ## fy3-2-L2-02
 **Annettu:** P = 6,0 kW = 6000 W, t = 45 min = 2700 s
@@ -60,7 +60,7 @@
 **Kaava:** W = P t ja W = m g h ⇒ h = P t / (m g)
 **Sijoitus:** h = 12 000 W · 30 s / (850 kg · 9,81 m/s²) = 43,17 m
 **Vastaus:** 43,2 m
-**Järkevyys:** Nousunopeus on noin 1,4 m/s, mikä on tavallinen nosturin nopeus. Kerrostalon katolle puolessa minuutissa, uskottavaa.
+**Järkevyys:** Nousunopeus on noin 1,4 m/s, mikä on nosturille tavallinen nopeus. Kerrostalon katolle noustaan puolessa minuutissa, joten tulos on uskottava.
 
 ## fy3-2-L2-04
 **Annettu:** m = 62 kg, h = 15 m, t = 12 s, g = 9,81 m/s²
@@ -68,7 +68,7 @@
 **Kaava:** W = m g h, P = W / t
 **Sijoitus:** W = 62 kg · 9,81 m/s² · 15 m = 9123 J; P = 9123 J / 12 s = 760 W
 **Vastaus:** 760 W
-**Järkevyys:** Noin yksi hevosvoima (746 W). Kova mutta mahdollinen hetkellinen teho kuntoilijalle.
+**Järkevyys:** Noin yksi hevosvoima (746 W). Kova mutta mahdollinen teho kuntoilijalle.
 
 ## fy3-2-L3-01
 **Annettu:** m = 75 kg, h = 40 m, v₀ = 0, v = 20 m/s, g = 9,81 m/s²
@@ -84,7 +84,7 @@
 **Kaava:** P = W / t = F s / t = F v, koska s / t = v tasaisessa liikkeessä ja voima on liikkeen suuntainen
 **Sijoitus:** P = 4500 N · 22,2 m/s = 100 000 W
 **Vastaus:** 100 kW
-**Järkevyys:** Kuorma-auton moottorin teho on satoja kilowatteja, josta osa kuluu auton omaan vastukseen. 100 kW perävaunun vetoon on järkevä.
+**Järkevyys:** Kuorma-auton moottorin teho on satoja kilowatteja, ja siitä osa kuluu auton omaan vastukseen. Perävaunun vetoon 100 kW on järkevä.
 
 ## fy3-2-L3-03
 **Annettu:** P = 180 W, m = 1000 kg, h = 50 m, g = 9,81 m/s²
```
