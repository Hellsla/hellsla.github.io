VERDICT: PASS
CONTENT-HASH: af663775e9c7ad21

## Blocking
(none)

## Polish
- exercises.json:L2-01 — "auton tallissa" reads as "in the car's stable"; use "autotallissa" (in diff).
- exercises.json:L1-04 — "tyhjä ... muovitynnyri" contradicts "siinä on 8,40 mol ilmaa"; "tyhjä" dropped (in diff).
- lesson.md:45 — "tuhat tai miljoona kertaa väärä" is ungrammatical; "tuhat- tai miljoonakertaisesti väärä" (in diff).
- exit-ticket.json:Q3 — "mikromallin oletuksia ideaalikaasumalliin" is back to front; "oletuksia ideaalikaasun mikromalliin" (in diff).
- Not language, for the content reviewers: lesson.md:38 shows n ≈ 0,21 mol and line 40 then uses 0,207 mol. Add "0,207" to the display or write 0,21 consistently. Also consider adding "yhdistetty kaasulaki" to glossary.json (new term, not in meta.glossary).

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -42,7 +42,7 @@
 Samankokoisessa ilmapallossa on samassa paineessa ja lämpötilassa yhtä paljon eli 0,21 mol ilmaa, mutta sen massa on noin 6,0 g, koska ilman moolimassa on 29 g/mol. Tulos on järkevä: litrassa kaasua on huoneenlämmössä noin 0,04 mol.
 
 ## Yleinen virhekäsitys
-Yleisin virhe on käyttää tilanyhtälössä celsiusasteita. Esimerkiksi 0 °C antaisi nollan, mutta kaasulla on paine myös jäätymispisteessä. Lämpötila muutetaan aina kelvineiksi. Toinen virhe on sijoittaa paine kilopascaleina ja tilavuus litroina. Silloin tulos on tuhat tai miljoona kertaa väärä, ellei yksiköitä muuteta perusyksiköiksi. Kolmas virhe on ajatella, että raskaampaa kaasua mahtuu samaan tilavuuteen vähemmän moolia. Ainemäärä riippuu vain paineesta, tilavuudesta ja lämpötilasta, ei kaasun laadusta. Massa sen sijaan riippuu moolimassasta.
+Yleisin virhe on käyttää tilanyhtälössä celsiusasteita. Esimerkiksi 0 °C antaisi tulokseksi nollan, mutta kaasulla on paine myös jäätymispisteessä. Lämpötila muutetaan aina kelvineiksi. Toinen virhe on sijoittaa paine kilopascaleina ja tilavuus litroina. Silloin tulos on tuhat- tai miljoonakertaisesti väärä, ellei yksiköitä muuteta perusyksiköiksi. Kolmas virhe on ajatella, että raskaampaa kaasua mahtuu samaan tilavuuteen vähemmän moolia. Ainemäärä riippuu vain paineesta, tilavuudesta ja lämpötilasta, ei kaasun laadusta. Massa sen sijaan riippuu moolimassasta.
 
 ## Tiivistelmä
 - Ideaalikaasun tilanyhtälö on $pV = nRT$, missä $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ ja T on kelvineinä.
--- a/exercises.json
+++ b/exercises.json
@@ -27,7 +27,7 @@
     {
       "id": "fy3-10-L1-04",
       "level": 1,
-      "text": "Mökin laiturilla on tyhjä tummanvärinen muovitynnyri, jonka kansi on kiinni. Tynnyrin tilavuus on 0,200 m³, ja siinä on 8,40 mol ilmaa. Aurinkoisena iltapäivänä ilman paine tynnyrissä on 1,13 · 10⁵ Pa. Mikä on ilman lämpötila tynnyrissä kelvineinä? Käytä arvoa R = 8,31 J/(mol·K).",
+      "text": "Mökin laiturilla on tummanvärinen muovitynnyri, jonka kansi on kiinni. Tynnyrin tilavuus on 0,200 m³, ja siinä on 8,40 mol ilmaa. Aurinkoisena iltapäivänä ilman paine tynnyrissä on 1,13 · 10⁵ Pa. Mikä on ilman lämpötila tynnyrissä kelvineinä? Käytä arvoa R = 8,31 J/(mol·K).",
       "answer": 324,
       "unit": "K",
       "tolerance": 0.02
@@ -45,7 +45,7 @@
     {
       "id": "fy3-10-L2-01",
       "level": 2,
-      "text": "Ensihoitoauton happipullon tilavuus on 10,0 l. Täydessä pullossa hapen paine on 200 bar (1 bar = 100 kPa), ja auton tallissa lämpötila on 15 °C. Kuinka monta kilogrammaa happea pullossa on? Hapen moolimassa on 32 g/mol. Käytä arvoa R = 8,31 J/(mol·K) ja oleta, että happi noudattaa ideaalikaasun tilanyhtälöä.",
+      "text": "Ensihoitoauton happipullon tilavuus on 10,0 l. Täydessä pullossa hapen paine on 200 bar (1 bar = 100 kPa), ja autotallissa lämpötila on 15 °C. Kuinka monta kilogrammaa happea pullossa on? Hapen moolimassa on 32 g/mol. Käytä arvoa R = 8,31 J/(mol·K) ja oleta, että happi noudattaa ideaalikaasun tilanyhtälöä.",
       "answer": 2.7,
       "unit": "kg",
       "tolerance": 0.02
@@ -79,7 +79,7 @@
     {
       "id": "fy3-10-L3-01",
       "level": 3,
-      "text": "Levossa ihminen hengittää yhdellä sisäänhengityksellä keuhkoihinsa ilmaa, joka vie keuhkoissa 37 °C:n lämpöisenä tilavuuden 0,55 l. Ilman paine keuhkoissa on 101 kPa. Kuinka monta molekyyliä yhdessä hengenvedossa on? Avogadron vakio on 6,022 · 10²³ 1/mol ja R = 8,31 J/(mol·K). Anna vastaus muodossa a · 10²². Perustele, miksi laskussa ei tarvita tietoa siitä, mistä kaasuista ilma koostuu.",
+      "text": "Levossa ihminen hengittää yhdellä sisäänhengityksellä keuhkoihinsa ilmaa, joka vie 37 °C:n lämpöisenä tilavuuden 0,55 l. Ilman paine keuhkoissa on 101 kPa. Kuinka monta molekyyliä yhdessä hengenvedossa on? Avogadron vakio on 6,022 · 10²³ 1/mol ja R = 8,31 J/(mol·K). Anna vastaus muodossa a · 10²². Perustele, miksi laskussa ei tarvita tietoa siitä, mistä kaasuista ilma koostuu.",
       "answer": 1.3,
       "unit": "· 10²²",
       "tolerance": 0.02
--- a/solutions.md
+++ b/solutions.md
@@ -36,7 +36,7 @@
 **Kaava:** n = m / M
 **Sijoitus:** n = 425 g / 44 g/mol = 9,659 mol ≈ 9,7 mol
 **Vastaus:** 9,7 mol
-**Järkevyys:** Gramma ja gramma supistuvat, joten yksiköksi jää mooli. Pullossa hiilidioksidi on suuren paineen vuoksi osittain nesteenä, mutta ainemäärä kertoo molekyylien määrän olomuodosta riippumatta. Huoneen paineessa ja lämpötilassa kaasu veisi noin 9,7 · 24 l ≈ 230 l.
+**Järkevyys:** Grammat supistuvat, joten yksiköksi jää mooli. Pullossa hiilidioksidi on suuren paineen vuoksi osittain nesteenä, mutta ainemäärä kertoo molekyylien määrän olomuodosta riippumatta. Huoneen paineessa ja lämpötilassa kaasu veisi noin 9,7 · 24 l ≈ 230 l.
 
 ## fy3-10-L2-01
 **Annettu:** V = 10,0 l = 0,0100 m³, p = 200 bar = 2,00 · 10⁷ Pa, θ = 15 °C, M = 32 g/mol = 0,032 kg/mol
--- a/exit-ticket.json
+++ b/exit-ticket.json
@@ -8,7 +8,7 @@
     "a": "Moolimäärä on sama, koska n = pV/(RT) ei riipu kaasun laadusta. Hiilidioksidipallo on raskaampi, koska hiilidioksidin moolimassa 44 g/mol on paljon suurempi kuin heliumin 4,0 g/mol."
   },
   {
-    "q": "Mitä mikromallin oletuksia ideaalikaasumalliin sisältyy, ja milloin malli alkaa pettää?",
+    "q": "Mitä oletuksia ideaalikaasun mikromalliin sisältyy, ja milloin malli alkaa pettää?",
     "a": "Hiukkasilla ei oleteta olevan tilavuutta eikä vuorovaikutusta törmäysten välillä. Malli pettää suurissa paineissa ja matalissa lämpötiloissa, kun hiukkaset ovat lähellä toisiaan ja kaasu on lähellä nesteytymistä."
   }
 ]
--- a/sim.js
+++ b/sim.js
@@ -109,7 +109,7 @@
     readout.html(`N = ${N}, T = ${T} K, V = ${fi(Vrel * 100, 0)} % (vertailutila: N = 100, T = 300 K, V = 100 %)` +
       `<br>Mitattu paine p/p<sub>ref</sub> = <strong>${fi(pm, 2)}</strong> (keskiarvo ${fi(tAvg, 1)} s:n ajalta)` +
       `<br>Tilanyhtälön ennuste p/p<sub>ref</sub> = (N/100) · (T/300 K) · (100 %/V) = <strong>${fi(pp, 2)}</strong>` +
-      `<br>Suhde mitattu/ennuste = pV/(NT) vertailutilaan verrattuna = <strong>${fi(ratio, 2)}</strong>`);
+      `<br>Suhde mitattu/ennuste (= pV/(NT) suhteessa vertailutilaan) = <strong>${fi(ratio, 2)}</strong>`);
 
     const k = Math.max(1, 600 / (document.getElementById('sim-root').clientWidth || 600));   // keep canvas text legible when scaled
     const ts = (n) => Math.round(n * k);
```

## Checked
- Lint clean (0 errors, 0 warnings); not repeated.
- Terms match glossary.json: ideaalikaasu, tilanyhtälö, ainemäärä, mooli, moolinen kaasuvakio, moolimassa, Avogadron vakio, ylipaine, ilmanpaine, kelvin.
- Case after number plus unit: 37 °C:n, 250 °C:n, 1,00 l:n, 20 °C:n, 101 kPa:n, 2 s:n all inflected correctly; no "80 N voimalla" pattern.
- Decimal comma in all Finnish text (sim.js fi() also gives comma and U+2212 minus); decimal point only in JSON values.
- Minus sign is U+2212 (−30 °C, −273,15); en dash in ranges (20–200).
- Units follow numbers with a space, as in the existing lessons (no thin spaces used anywhere in the repo, so none required).
- "Paino" not misused; no weight or N/kg for g.
- Sim strings (button, sliders, readout, note, canvas labels) and sim-spec.md agree with each other and with the lesson wording ("Nollaa mittaus", "mitattu", "ennuste").
- Reading level suits 16 to 19-year-olds; sentences short, new terms defined at first use.
- Section headings match the gold structure (Ydinajatus, Kaava, Esimerkki, Yleinen virhekäsitys, Tiivistelmä).
- Hash unchanged at start and end of review (af663775e9c7ad21).
