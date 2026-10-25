VERDICT: PASS
CONTENT-HASH: 969b944091a972e5

## Blocking
(none)

## Polish
- exercises.json:72 (L2-04) — two questions in a row (volume of the heated air, then volume pushed out), but only the second has the answer 890 m³; a student may type 3690 — ask only the second (in diff).
- exercises.json:82 (L3-01) — "kuplan ilmaa liukene" has a definite subject in the partitive; use "kuplan ilma liukene" (in diff).
- exercises.json:90 (L3-02) — "20 °C:n lämpimässä tallissa" is clumsy; "20 °C:n tallissa" (in diff).
- lesson.md:52 — the parenthesis "(tarkemmin 1,04 l)" gives a volume inside a sentence about growth; reword (in diff).
- sim.js:119 — button name without quotes; sim-spec.md uses ”Tallenna mittaus”, use the same (in diff). Also solutions.md:63 "Tulojen pV arvot" -> "Tulon pV arvot" and solutions.md:79 "samassa paineessa" -> "kuin ympäröivä vesi" (in diff).

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -49,7 +49,7 @@
 &\approx 1{,}0\,\text{l}
 \end{aligned}
 ```
-Ilman tilavuus kasvaa noin kolmanneksella (tarkemmin 1,04 l). Jos pussi on valmiiksi lähes täynnä, se pullistuu kireäksi. Tulos on järkevä: paine pienenee, joten tilavuuden täytyy kasvaa, ja kasvukerroin on painesuhde 101/78 ≈ 1,3.
+Ilman tilavuus kasvaa noin kolmanneksella, ja tarkemmin laskettuna uusi tilavuus on 1,04 l. Jos pussi on valmiiksi lähes täynnä, se pullistuu kireäksi. Tulos on järkevä: paine pienenee, joten tilavuuden täytyy kasvaa, ja kasvukerroin on painesuhde 101/78 ≈ 1,3.
 
 ## Yleinen virhekäsitys
 Moni ajattelee, että kääntäen verrannollisuus tarkoittaa laskevaa suoraa. Kun tilavuus kaksinkertaistuu, paine puolittuu, joten (V, p)-kuvaaja on kaari, joka lähestyy akseleita mutta ei koskaan kohtaa niitä. Suora syntyy vasta, kun p piirretään 1/V:n funktiona. Toinen virhe on käyttää celsiusasteita kaavoissa, joissa on lämpötilojen suhde. Kun ilma lämpenee 10 °C:sta 20 °C:seen, sen tilavuus ei kaksinkertaistu, vaan kasvaa kertoimella 293 K / 283 K eli vain noin 3,5 %. Kolmas virhe on ajatella, että kaasun paine johtuu kaasun painosta. Suljetussa astiassa paine syntyy hiukkasten törmäyksistä, ja se on yhtä suuri kaikkialla astiassa.
--- a/exercises.json
+++ b/exercises.json
@@ -69,7 +69,7 @@
     {
       "id": "fy3-9-L2-04",
       "level": 2,
-      "text": "Kuumailmapallon kuoren tilavuus on 2800 m³, ja kuoren alaosassa on aukko. Kuori on täynnä 10 °C:n ilmaa, joka lämmitetään polttimella 100 °C:seen. Paine kuoren sisällä pysyy ulkoilman paineena. Kuinka suuren tilavuuden alun perin kuoressa ollut ilma veisi lämmettyään? Laske, kuinka monta kuutiometriä ilmaa on tämän vuoksi työntynyt ulos aukosta.",
+      "text": "Kuumailmapallon kuoren tilavuus on 2800 m³, ja kuoren alaosassa on aukko. Kuori on täynnä 10 °C:n ilmaa, joka lämmitetään polttimella 100 °C:seen. Paine kuoren sisällä pysyy ulkoilman paineena. Laske, kuinka monta kuutiometriä ilmaa on työntynyt ulos aukosta, kun alun perin kuoressa ollut ilma on lämmennyt.",
       "answer": 890,
       "unit": "m³",
       "tolerance": 0.02
@@ -79,7 +79,7 @@
     {
       "id": "fy3-9-L3-01",
       "level": 3,
-      "text": "Sukeltaja on järvessä 20,0 m:n syvyydessä ja puhaltaa ilmakuplan, jonka tilavuus on 2,0 cm³. Kupla nousee pintaan. Ilmanpaine on 101 kPa ja veden tiheys 1000 kg/m³. Oleta, että veden lämpötila on sama koko matkalla, eikä kuplan ilmaa liukene veteen. Mikä on kuplan tilavuus pinnalla? Perustele tuloksen avulla, miksi paineilmalla sukeltava ei saa pidättää hengitystään noustessaan pintaan.",
+      "text": "Sukeltaja on järvessä 20,0 m:n syvyydessä ja puhaltaa ilmakuplan, jonka tilavuus on 2,0 cm³. Kupla nousee pintaan. Ilmanpaine on 101 kPa ja veden tiheys 1000 kg/m³. Oleta, että veden lämpötila on sama koko matkalla, eikä kuplan ilma liukene veteen. Mikä on kuplan tilavuus pinnalla? Perustele tuloksen avulla, miksi paineilmalla sukeltava ei saa pidättää hengitystään noustessaan pintaan.",
       "answer": 5.9,
       "unit": "cm³",
       "tolerance": 0.02
@@ -87,7 +87,7 @@
     {
       "id": "fy3-9-L3-02",
       "level": 3,
-      "text": "Auton renkaat täytetään 20 °C:n lämpimässä tallissa, ja rengaspainemittari näyttää 250 kPa. Mittari näyttää ylipainetta eli sitä, kuinka paljon renkaan ilman paine on ilmanpainetta suurempi. Ilmanpaine on 101 kPa. Yöllä auto seisoo pihalla, ja renkaan ilma jäähtyy −20 °C:seen. Renkaan tilavuus pysyy käytännössä samana, eikä ilmaa pääse ulos. Mitä mittari näyttää pakkasaamuna? Perustele, miksi mittarin lukemaa ei voi sijoittaa suoraan kaavaan p₁/T₁ = p₂/T₂.",
+      "text": "Auton renkaat täytetään 20 °C:n tallissa, ja rengaspainemittari näyttää 250 kPa. Mittari näyttää ylipainetta eli sitä, kuinka paljon renkaan ilman paine on ilmanpainetta suurempi. Ilmanpaine on 101 kPa. Yöllä auto seisoo pihalla, ja renkaan ilma jäähtyy −20 °C:seen. Renkaan tilavuus pysyy käytännössä samana, eikä ilmaa pääse ulos. Mitä mittari näyttää pakkasaamuna? Perustele, miksi mittarin lukemaa ei voi sijoittaa suoraan kaavaan p₁/T₁ = p₂/T₂.",
       "answer": 202,
       "unit": "kPa",
       "tolerance": 0.02
--- a/solutions.md
+++ b/solutions.md
@@ -60,7 +60,7 @@
 **Kaava:** p = pV · (1/V), joten (1/V, p)-kuvaajan kulmakerroin on pV
 **Sijoitus:** 1/V = 0,100; 0,0800; 0,0667; 0,0500; 0,0400; 0,0333 1/ml. Pisteet ovat origon kautta kulkevalla suoralla. Suora kulkee esimerkiksi pisteen (0,100 1/ml; 201 kPa) kautta, joten kulmakerroin on 201 kPa / (0,100 1/ml) ≈ 2010 kPa·ml. Koska 1 kPa · 1 ml = 1000 Pa · 0,000001 m³ = 0,001 J, pV ≈ 2,0 J.
 **Vastaus:** 2,0 J
-**Järkevyys:** Tulojen pV arvot ovat 1980–2030 kPa·ml, joten ne ovat lähes vakioita, ja Boylen laki pätee mittaustarkkuuden rajoissa.
+**Järkevyys:** Tulon pV arvot ovat 1980–2030 kPa·ml, joten ne ovat lähes vakioita, ja Boylen laki pätee mittaustarkkuuden rajoissa.
 
 ## fy3-9-L2-04
 **Annettu:** V₁ = 2800 m³, θ₁ = 10 °C, θ₂ = 100 °C, paine vakio
@@ -76,7 +76,7 @@
 **Kaava:** p₁ = p₀ + ρgh ja p₁V₁ = p₀V₂
 **Sijoitus:** ρgh = 1000 kg/m³ · 9,81 m/s² · 20,0 m = 196 200 Pa = 196,2 kPa, joten p₁ = 101 kPa + 196,2 kPa = 297,2 kPa. V₂ = 297,2 kPa · 2,0 cm³ / 101 kPa = 5,885 cm³ ≈ 5,9 cm³
 **Vastaus:** 5,9 cm³
-**Järkevyys:** Paine putoaa lähes kolmasosaan, joten tilavuus lähes kolminkertaistuu. Keuhkojen ilma on syvällä samassa paineessa. Jos sukeltaja pidättää hengitystä noustessaan, ilma pyrkii laajenemaan lähes kolminkertaiseksi ja voi repiä keuhkokudosta. Siksi noustessa hengitetään ulos.
+**Järkevyys:** Paine putoaa lähes kolmasosaan, joten tilavuus lähes kolminkertaistuu. Keuhkojen ilma on syvällä samassa paineessa kuin ympäröivä vesi. Jos sukeltaja pidättää hengitystä noustessaan, ilma pyrkii laajenemaan lähes kolminkertaiseksi ja voi repiä keuhkokudosta. Siksi noustessa hengitetään ulos.
 
 ## fy3-9-L3-02
 **Annettu:** ylipaine 250 kPa, p₀ = 101 kPa, θ₁ = 20 °C, θ₂ = −20 °C, tilavuus vakio
--- a/sim.js
+++ b/sim.js
@@ -116,7 +116,7 @@
       const Vm = r.V * 1e6, pr = r.p / 1000;
       h += `<tr>${td}${fi(Vm, 1)}</td>${td}${fs(1 / Vm)}</td>${td}${fi(pr, 1)}</td>${td}${fi(r.T, 2)}</td>${td}${fi(cFn(Vm, pr, r.T), cDec)}</td></tr>`;
     }
-    if (!rows.length) h += '<tr><td colspan="5" style="padding:.4rem .25rem">Ei mittauksia. Paina Tallenna mittaus.</td></tr>';
+    if (!rows.length) h += '<tr><td colspan="5" style="padding:.4rem .25rem">Ei mittauksia. Paina ”Tallenna mittaus”.</td></tr>';
     h += '</tbody></table>';
     if (table.elt.innerHTML !== h) table.elt.innerHTML = h;
     window.simState = { mode, V: V * 1e-6, p: pk * 1000, T, constant: c * (iso ? 1e-3 : mode === 'isobaarinen' ? 1e-6 : 1e3),
```

## Checked
- Lint run first: 0 errors, 0 warnings; not repeated.
- Glossary terms (tilanmuutos, isoterminen, isobaarinen, isokoorinen, Boylen laki, kelvin, absoluuttinen nollapiste, ylipaine, ilmanpaine) used as defined; no invented synonyms.
- Case after number+unit (101 kPa:n, 22 °C:n, 20,0 m:n, 280 kPa:iin, 7 kN:n, 10 °C:sta ... 20 °C:seen, 280 K:stä 308 K:iin) correct in all files.
- Decimal comma in all text; no decimal points outside JSON values and SVG; space before units and % everywhere; minus sign U+2212 in sim.js fi().
- No unspaced number+unit, no hyphen-minus before numbers in text.
- Sim strings (labels, options, readout, note, table, empty row) and sim-spec.md read for grammar and terminology; consistent with lesson.
- Exit ticket and solutions: language and sanity-check sentences read; numbers not changed.
- Reading level suitable for 16-19 year olds; lesson.md:10 and :12 are long but clear.
- Hash re-run at the end: unchanged (969b944091a972e5).
