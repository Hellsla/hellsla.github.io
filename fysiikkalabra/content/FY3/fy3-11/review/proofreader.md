VERDICT: FAIL
CONTENT-HASH: ff7e8aec21368766

## Blocking
- sim.js:20 (and sim-spec.md:1) — the car-engine output flow is labelled "mekaaninen työ" but carries a value in kW; work is in J, power in kW, and the lesson, exercises and exit ticket all say "mekaaninen teho" — change `use: 'mekaaninen työ'` to `'mekaaninen teho'` (diff below). Side effect for the fixer: tests/sims/fy3-11.json line 501 expects the label string `mekaaninen työ 18,0 kW` and must become `mekaaninen teho 18,0 kW`.

## Polish
- exercises.json L2-01 and solutions.md L2-01: "3 830 MWh" is grouped with a space while other four-digit values are not ("4300 MW", "1200 kW", "3600 s"); pick one style. Not in the diff because the lint may read the number from the text.
- solutions.md L1-03: **Vastaus:** 37 % while exercises.json has answer 37.2 and Sijoitus gives 37,2 %; for the producer or physicist to decide which significant figures to show.
- glossary.json: "hukkalämpö", "kaukolämpö" and "lauhdevoimalaitos" are used throughout but have no entry (CLAUDE.md: add missing terms).
- lesson.md:30, 106, 6 and the exercise wordings in the diff: clearer or less colloquial phrasing ("Lukua sanotaan" with no number named, "kuten pitää", "tekee mäntään", "jota sulkee", "ottaa ... ja hoitaisi", "1,5-kertaisesti", "Jos työn lisäisi, saisi").

## Diff
```diff
--- a/exercises.json
+++ b/exercises.json
@@ -3,7 +3,7 @@
     {
       "id": "fy3-11-L1-01",
       "level": 1,
-      "text": "Museorautatien höyryveturin sylinteriin virtaa kattilasta höyryä, joka työntää mäntää. Männän liikkuessa höyryn paine pysyy 480 kPa:na, ja höyryn tilavuus sylinterissä kasvaa 0,0250 m³. Kuinka suuren työn höyry tekee mäntään? Anna vastaus kilojouleina.",
+      "text": "Museorautatien höyryveturin sylinteriin virtaa kattilasta höyryä, joka työntää mäntää. Männän liikkuessa höyryn paine pysyy 480 kPa:na, ja höyryn tilavuus sylinterissä kasvaa 0,0250 m³. Kuinka suuren työn höyry tekee männän liikkuessa? Anna vastaus kilojouleina.",
       "answer": 12.0,
       "unit": "kJ",
       "tolerance": 0.02
@@ -61,7 +61,7 @@
     {
       "id": "fy3-11-L2-03",
       "level": 2,
-      "text": "Fysiikan tunnilla sylinterissä on ilmaa, jota sulkee kevyesti liikkuva mäntä. Ilmaa lämmitetään, jolloin siihen siirtyy lämpömäärä 700 J. Ilma laajenee niin, että sen paine pysyy 125 kPa:na ja tilavuus kasvaa 1,60 litraa. Kuinka paljon ilman sisäenergia muuttuu? Käytä ensimmäistä pääsääntöä ΔU = Q + W, jossa W on ympäristön ilmaan tekemä työ. Anna vastaus etumerkkeineen.",
+      "text": "Fysiikan tunnilla sylinterissä on ilmaa, jonka kevyesti liikkuva mäntä sulkee. Ilmaa lämmitetään, jolloin siihen siirtyy lämpömäärä 700 J. Ilma laajenee niin, että sen paine pysyy 125 kPa:na ja tilavuus kasvaa 1,60 litraa. Kuinka paljon ilman sisäenergia muuttuu? Käytä ensimmäistä pääsääntöä ΔU = Q + W, jossa W on ympäristön ilmaan tekemä työ. Anna vastaus etumerkkeineen.",
       "answer": 500,
       "unit": "J",
       "tolerance": 0.02
@@ -87,7 +87,7 @@
     {
       "id": "fy3-11-L3-02",
       "level": 3,
-      "text": "Omakotitalon lämmittämiseen kuluu vuodessa 16,0 MWh lämpöä. Talossa on nyt suora sähkölämmitys, jossa sähkövastukset muuttavat kaiken sähkön lämmöksi. Omistaja harkitsee lämpöpumppua, joka ottaa lämpöä ulkoilmasta ja hoitaisi koko lämmityksen. Pumpun lämpökerroin on vuoden keskiarvona 2,50. Kuinka monta megawattituntia sähköä pumppu säästäisi vuodessa? Kuinka paljon lämpöä se ottaisi vuoden aikana ulkoilmasta? Perustele energian säilymisen avulla, miksi pumppu ei ole ikiliikkuja, vaikka se luovuttaa taloon enemmän lämpöä kuin käyttää sähköä.",
+      "text": "Omakotitalon lämmittämiseen kuluu vuodessa 16,0 MWh lämpöä. Talossa on nyt suora sähkölämmitys, jossa sähkövastukset muuttavat kaiken sähkön lämmöksi. Omistaja harkitsee lämpöpumppua, joka ottaisi lämpöä ulkoilmasta ja hoitaisi koko lämmityksen. Pumpun lämpökerroin on vuoden keskiarvona 2,50. Kuinka monta megawattituntia sähköä pumppu säästäisi vuodessa? Kuinka paljon lämpöä se ottaisi vuoden aikana ulkoilmasta? Perustele energian säilymisen avulla, miksi pumppu ei ole ikiliikkuja, vaikka se luovuttaa taloon enemmän lämpöä kuin käyttää sähköä.",
       "answer": 9.6,
       "unit": "MWh",
       "tolerance": 0.02
--- a/exit-ticket.json
+++ b/exit-ticket.json
@@ -1,6 +1,6 @@
 [
   {
-    "q": "Sylinterissä olevan kaasun paine pysyy 200 kPa:na, kun sen tilavuus kasvaa 0,50 litraa. Kuinka suuren työn kaasu tekee mäntään?",
+    "q": "Sylinterissä olevan kaasun paine pysyy 200 kPa:na, kun sen tilavuus kasvaa 0,50 litraa. Kuinka suuren työn kaasu tekee männän liikkuessa?",
     "a": "W = pΔV = 200 000 Pa · 0,000 50 m³ = 100 J."
   },
   {
--- a/lesson.md
+++ b/lesson.md
@@ -3,7 +3,7 @@
 > **Miksi** lämpövoimalaitos saa polttoaineen energiasta sähköksi vain alle puolet, ja minne loput energiasta menee?
 
 ## Ydinajatus
-Kun kaasu laajenee ja työntää mäntää, se tekee työtä. Kaasu painaa mäntää voimalla F = pA, missä A on männän pinta-ala. Jos mäntä liikkuu matkan s ja paine pysyy samana, kaasun tekemä työ on oppitunnin fy3-2 tapaan voima kertaa matka: W = Fs = pAs. Tulo As on kaasun tilavuuden muutos ΔV, joten työ on pΔV. (V, p)-kuvaajassa työ on kuvaajan ja V-akselin väliin jäävä pinta-ala, samoin kuin (s, F)-kuvaajassa. Kun kaasua puristetaan, ympäristö tekee työtä kaasuun. Termodynamiikan ensimmäisessä pääsäännössä ΔU = Q + W työ W tarkoittaa ympäristön kaasuun tekemää työtä, joten laajenevalle kaasulle se on −pΔV.
+Kun kaasu laajenee ja työntää mäntää, se tekee työtä. Kaasu painaa mäntää voimalla F = pA, missä A on männän pinta-ala. Jos mäntä liikkuu matkan s ja paine pysyy samana, kaasun tekemä työ on oppitunnin fy3-2 tapaan voima kertaa matka: W = Fs = pAs. Tulo As on kaasun tilavuuden muutos ΔV, joten työ on pΔV. (V, p)-kuvaajassa työ on kuvaajan ja V-akselin väliin jäävä pinta-ala, samoin kuin (s, F)-kuvaajassa. Kun kaasua puristetaan, ympäristö tekee työtä kaasuun. Termodynamiikan ensimmäisessä pääsäännössä (ΔU = Q + W) työ W tarkoittaa ympäristön kaasuun tekemää työtä, joten laajenevalle kaasulle se on −pΔV.
 
 Lämpövoimakone muuttaa lämpöä jatkuvasti työksi. Höyryvoimalaitoksessa vesi kiehuu kattilassa, kuuma höyry laajenee turbiinissa ja pyörittää generaattoria, ja turbiinista tuleva höyry tiivistyy jälleen vedeksi lauhduttimessa, jota merivesi jäähdyttää. Työaine kiertää samaa rataa yhä uudelleen, joten kierroksen lopussa sen sisäenergia on sama kuin alussa. Energia säilyy: koneeseen kuumasta lähteestä tullut lämpö Q₁ on yhtä suuri kuin koneen tekemä työ W ja kylmempään ympäristöön luovutettu lämpö Q₂ yhteensä. Kokemus osoittaa, ettei lämpövoimakone voi muuttaa kaikkea saamaansa lämpöä työksi, vaan osa on aina luovutettava kylmempään ympäristöön. Tämä on termodynamiikan toisen pääsäännön sisältö. Mitä suurempi on kuuman lähteen ja kylmän ympäristön lämpötilaero, sitä suuremman osan lämmöstä kone voi muuttaa työksi.
 
@@ -27,7 +27,7 @@
 
 Hyötysuhde kertoo, kuinka suuri osa koneeseen tuodusta energiasta saadaan hyödyksi. Suomalainen lauhdevoimalaitos, joka tuottaa vain sähköä, saa polttoaineen energiasta sähköksi noin 40 %, ja ydinvoimalaitos noin 35 %. Loput siirtyvät lauhduttimen kautta mereen. Automoottorin hyötysuhde on noin 30 %, ja loput energiasta poistuu pakokaasujen ja jäähdyttimen mukana. Sähkön ja lämmön yhteistuotannossa lauhduttimesta tuleva lämpö johdetaan kaukolämpöverkkoon kaupungin taloihin, joten polttoaineen energiasta saadaan hyödyksi sähkönä ja lämpönä yhteensä 85–90 %. Tämä vastaa alun kysymykseen: sähköksi saadaan alle puolet, mutta loput eivät katoa, vaan siirtyvät lämpönä ympäristöön tai kaukolämpöverkkoon.
 
-Jäähdytyskone ja lämpöpumppu toimivat päinvastoin kuin lämpövoimakone: ne käyttävät työtä, yleensä sähköä, ja siirtävät sen avulla lämpöä kylmästä paikasta lämpimään. Jääkaappi siirtää lämpöä kaapin sisältä huoneeseen, ja ilmalämpöpumppu ulkoilmasta sisälle. Sisälle luovutettu lämpö on ulkoa otetun lämmön ja käytetyn sähkön summa, joten pumppu voi lämmittää taloa esimerkiksi kolminkertaisella teholla käyttämäänsä sähkötehoon verrattuna. Lukua sanotaan lämpökertoimeksi. Pumppu ei luo energiaa, vaan siirtää sitä.
+Jäähdytyskone ja lämpöpumppu toimivat päinvastoin kuin lämpövoimakone: ne käyttävät työtä, yleensä sähköä, ja siirtävät sen avulla lämpöä kylmästä paikasta lämpimään. Jääkaappi siirtää lämpöä kaapin sisältä huoneeseen, ja ilmalämpöpumppu ulkoilmasta sisälle. Sisälle luovutettu lämpö on ulkoa otetun lämmön ja käytetyn sähkön summa, joten pumppu voi lämmittää taloa esimerkiksi kolminkertaisella teholla käyttämäänsä sähkötehoon verrattuna. Tätä lämpötehon ja sähkötehon suhdetta sanotaan lämpökertoimeksi. Pumppu ei luo energiaa, vaan siirtää sitä.
 
 ## Kaava
 Kun kaasun paine pysyy vakiona, kaasun tekemä työ on
@@ -103,7 +103,7 @@
 ```
 
 <!-- vaihe -->
-**Järkevyys.** Sähköä saadaan yhteistuotannossa vähemmän, koska höyry lauhdutetaan korkeammassa lämpötilassa, jotta sen lämpö kelpaa kaukolämmöksi. Polttoaineen energia käytetään silti paljon paremmin hyödyksi, ja kumpikin hyötysuhde jää alle 100 %:n, kuten pitää.
+**Järkevyys.** Sähköä saadaan yhteistuotannossa vähemmän, koska höyry lauhdutetaan korkeammassa lämpötilassa, jotta sen lämpö kelpaa kaukolämmöksi. Polttoaineen energia käytetään silti paljon paremmin hyödyksi, ja kumpikin hyötysuhde jää alle 100 %:n, kuten pitääkin.
 
 ## Yleinen virhekäsitys
 Moni ajattelee, että parempi tekniikka voisi tehdä lämpövoimakoneesta lähes täydellisen, niin että kaikki lämpö muuttuisi työksi. Kitkan ja muiden häviöiden vähentäminen auttaa, mutta osa lämmöstä on aina luovutettava kylmempään ympäristöön, joten hyötysuhde jää selvästi alle 100 %:n. Toinen virhe on pitää lämpöpumppua ikiliikkujana, koska se luovuttaa enemmän lämpöä kuin käyttää sähköä. Ylimääräinen lämpö tulee ulkoilmasta, eikä energiaa synny tyhjästä. Kolmas virhe on ajatella, että paineistettu kaasu tekee työtä jo sillä, että sen paine on suuri. Työtä tehdään vain, kun tilavuus muuttuu ja mäntä liikkuu.
--- a/sim-spec.md
+++ b/sim-spec.md
@@ -1 +1 @@
-Energiavirrat lämpövoimakoneessa ja lämpöpumpussa. Valikosta tilanne: lauhdevoimalaitos, yhteistuotantovoimalaitos, automoottori ja ilmalämpöpumppu; valinta asettaa säätimille tyypilliset alkuarvot (lauhde 1000 MW ja 40 %, yhteistuotanto 1000 MW, 30 % sähköä ja 55 % kaukolämpöä, automoottori 60 kW ja 30 %, lämpöpumppu 1,0 kW sähköä ja lämpökerroin 3,0). Lämpövoimakoneissa säätimet ovat syötetty polttoaineteho ja hyötysuhde 10–60 %, yhteistuotannossa lisäksi kaukolämmöksi saatava osuus; lämpöpumpussa säätimet ovat sähköteho ja lämpökerroin 1,5–5,0. Kankaalle piirretään virtauskaavio, jonka nuolten leveys on verrannollinen tehoon: lämpövoimakoneessa kuumasta lähteestä tuleva teho jakautuu hyötytehoksi (sähkö tai mekaaninen työ), mahdolliseksi kaukolämmöksi ja ympäristöön siirtyväksi hukkalämmöksi; lämpöpumpussa ulkoilmasta otettu lämpö ja sähkö yhdistyvät sisälle luovutetuksi lämmöksi. Nuolten tehot luetaan myös tekstinä kaavion vieressä. Tekstinä kankaan alla kunkin virran teho, energian säilymisen tarkistus (sisään = ulos) ja hyötysuhde tai kokonaishyötysuhde; lämpöpumpussa lämpökerroin ja selitys, että pumppu siirtää lämpöä eikä luo energiaa. simState sisältää mode, Pin, eta, Puse, Pheat, Pwaste, etaTotal ja lämpöpumpulle Pel, cop, Pout ja Pambient. Ei satunnaisuutta.
+Energiavirrat lämpövoimakoneessa ja lämpöpumpussa. Valikosta tilanne: lauhdevoimalaitos, yhteistuotantovoimalaitos, automoottori ja ilmalämpöpumppu; valinta asettaa säätimille tyypilliset alkuarvot (lauhde 1000 MW ja 40 %, yhteistuotanto 1000 MW, 30 % sähköä ja 55 % kaukolämpöä, automoottori 60 kW ja 30 %, lämpöpumppu 1,0 kW sähköä ja lämpökerroin 3,0). Lämpövoimakoneissa säätimet ovat syötettävä polttoaineteho ja hyötysuhde 10–60 %, yhteistuotannossa lisäksi kaukolämmöksi saatava osuus; lämpöpumpussa säätimet ovat sähköteho ja lämpökerroin 1,5–5,0. Kankaalle piirretään virtauskaavio, jonka nuolten leveys on verrannollinen tehoon: lämpövoimakoneessa kuumasta lähteestä tuleva teho jakautuu hyötytehoksi (sähkö tai mekaaninen teho), mahdolliseksi kaukolämmöksi ja ympäristöön siirtyväksi hukkalämmöksi; lämpöpumpussa ulkoilmasta otettu lämpö ja sähkö yhdistyvät sisälle luovutetuksi lämmöksi. Nuolten tehot luetaan myös tekstinä kaavion vieressä. Tekstinä kankaan alla kunkin virran teho, energian säilymisen tarkistus (sisään = ulos) ja hyötysuhde tai kokonaishyötysuhde; lämpöpumpussa lämpökerroin ja selitys, että pumppu siirtää lämpöä eikä luo energiaa. simState sisältää mode, Pin, eta, Puse, Pheat, Pwaste, etaTotal ja lämpöpumpulle Pel, cop, Pout ja Pambient. Ei satunnaisuutta.
--- a/sim.js
+++ b/sim.js
@@ -17,7 +17,7 @@
   const MODES = {
     lauhdevoimalaitos: { unit: 'MW', P: [100, 2000, 10, 1000], eta: 40, use: 'sähkö' },
     yhteistuotanto: { text: 'yhteistuotantovoimalaitos', unit: 'MW', P: [100, 2000, 10, 1000], eta: 30, heat: 55, use: 'sähkö' },
-    automoottori: { unit: 'kW', P: [10, 200, 1, 60], eta: 30, use: 'mekaaninen työ' },
+    automoottori: { unit: 'kW', P: [10, 200, 1, 60], eta: 30, use: 'mekaaninen teho' },
     ilmalämpöpumppu: { unit: 'kW', P: [0.5, 5, 0.1, 1], cop: 3 } };
   let sel, sP, lP, sE, lE, sH, lH, sC, lC, readout, mode = '', last = 'eta', t = 0, k = 1, boxes = {};
 
--- a/solutions.md
+++ b/solutions.md
@@ -36,7 +36,7 @@
 **Kaava:** η = W / Q₁
 **Sijoitus:** η = 2,6 kWh / 12 kWh = 0,217 = 21,7 % ≈ 22 %
 **Vastaus:** 22 %
-**Järkevyys:** Yksiköt supistuvat, joten kilowattitunteja ei tarvitse muuttaa jouleiksi. Pieni moottori jää automoottorin noin 30 %:sta. Loput 9,4 kWh siirtyy lämpönä ympäristöön.
+**Järkevyys:** Yksiköt supistuvat, joten kilowattitunteja ei tarvitse muuttaa jouleiksi. Pieni moottori jää alle automoottorin noin 30 %:n. Loput 9,4 kWh siirtyy lämpönä ympäristöön.
 
 ## fy3-11-L2-01
 **Annettu:** W = 3 830 MWh, Q₁ = 33,6 TJ = 3,36 · 10¹³ J, 1 MWh = 10⁶ W · 3600 s = 3,6 · 10⁹ J
@@ -60,7 +60,7 @@
 **Kaava:** Laajeneva ilma tekee työn pΔV, joten ympäristön ilmaan tekemä työ on W = −pΔV ja ΔU = Q + W = Q − pΔV
 **Sijoitus:** ΔU = 700 J − 125 000 Pa · 0,00160 m³ = 700 J − 200 J = 500 J
 **Vastaus:** 500 J, eli sisäenergia kasvaa.
-**Järkevyys:** Lämmöstä 200 J kuluu männän työntämiseen ja loput nostaa ilman lämpötilaa. Jos työn lisäisi, saisi 900 J, enemmän kuin ilmaan tuli lämpöä, vaikka ilma luovuttaa energiaa työntäessään mäntää.
+**Järkevyys:** Lämmöstä 200 J kuluu männän työntämiseen ja loput nostaa ilman lämpötilaa. Jos työ lisättäisiin lämpöön, tulokseksi tulisi 900 J, enemmän kuin ilmaan tuli lämpöä, vaikka ilma luovuttaa energiaa työntäessään mäntää.
 
 ## fy3-11-L2-04
 **Annettu:** P_mek = 480 kW, η = 40 % = 0,40
@@ -68,7 +68,7 @@
 **Kaava:** η = P_mek / P_in, joten P_in = P_mek / η ja P_hukka = P_in − P_mek
 **Sijoitus:** P_in = 480 kW / 0,40 = 1200 kW, joten P_hukka = 1200 kW − 480 kW = 720 kW
 **Vastaus:** 720 kW
-**Järkevyys:** Hukkaan menee 60 % ja hyödyksi 40 %, joten hukkalämpöä on 1,5-kertaisesti mekaaniseen tehoon verrattuna. Osa hukkalämmöstä voidaan käyttää matkustamon lämmittämiseen.
+**Järkevyys:** Hukkaan menee 60 % ja hyödyksi 40 %, joten hukkalämpöä on 1,5 kertaa niin paljon kuin mekaanista tehoa. Osa hukkalämmöstä voidaan käyttää matkustamon lämmittämiseen.
 
 ## fy3-11-L3-01
 **Annettu:** P_pa = 320 MW, P_s = 96 MW, P_kl = 180 MW, η_l = 40 % = 0,40, η_k = 90 % = 0,90
```

## Checked
- Decimal comma, space before units and %, case after number-plus-unit (480 kPa:na, 125 kPa:na, 100 %:n, 30 %:n, 80 km/h:n) in all text files: consistent.
- Minus sign U+2212 and en dash in ranges (85–90 %, 5–10 %): correct; no decimal points in Finnish text.
- Glossary terms (lämpövoimakone, hyötysuhde, kaasun tekemä työ, lämpökerroin, lämpöpumppu, jäähdytyskone, yhteistuotanto, lämpöarvo, ensimmäinen pääsääntö) used as defined.
- Stage markers: five `<!-- vaihe -->` stages, all kept; no paragraph over 105 words; no paragraph or stage structure touched by the diff.
- Sim strings (labels, readout, note, legend, "Energia säilyy" lines): grammar and decimal comma fine apart from the Blocking item.
- No numbers, formulas, LaTeX or JSON values changed in the diff.
