VERDICT: PASS
CONTENT-HASH: d4c0c6a3efea8e95

## Blocking
(none)

## Polish
- lesson.md:31 — "Loput imeytyy" (monikko + yksikön verbi) — "Loppu imeytyy"
- lesson.md:52 — "Tätä on ilmastonmuutos." ei ole kieliopillinen — "Tätä sanotaan ilmastonmuutokseksi."
- lesson.md:78 — "kuinka paljon energiaa se on vuorokaudessa" epäselvä — "se siirtää vuorokaudessa"
- solutions.md:79 — "on illalla noin 70 °C:sta" kieliopillisesti väärä — "on illalla vielä noin 70 °C:n lämpöistä"
- solutions.md:47, exercises.json L3-01 ja L3-03 — "Kylmemmällä" → "Kylmemmällä säällä"; "Mitä kautta" → "Minkä kautta"; "keskiarvona 2,8" → "lämmityskaudella keskimäärin 2,8"

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -28,7 +28,7 @@
 
 Talon lämmitysenergiasta suuri osa kuluu siihen, että lämpö johtuu seinien, katon, ikkunoiden ja lattian läpi ulos. Rakennusosan lämmöneristävyyttä kuvaa U-arvo eli lämmönläpäisykerroin, joka kertoo, kuinka monta wattia lämpötehoa siirtyy yhden neliömetrin läpi, kun sisä- ja ulkolämpötilan ero on yksi kelvin. Mitä pienempi U-arvo, sitä paremmin rakenne eristää. Nykyaikaisen seinän U-arvo on noin 0,17 W/(m²·K), mutta hyvänkin ikkunan noin 1,0 W/(m²·K), joten pieni ikkuna päästää läpi yhtä paljon lämpöä kuin moninkertainen ala seinää. Hyvä eristys säästää energiaa ja vähentää lämmityksen päästöjä.
 
-Kappaleen lämpötila pysyy vakiona, kun siihen tulee yhtä suuri teho kuin siitä lähtee. Tätä sanotaan energiatasapainoksi. Maapallo saa energiaa Auringon säteilynä, josta noin 30 % heijastuu suoraan takaisin avaruuteen pilvistä, jäästä ja vaaleista pinnoista. Loput imeytyy, ja maapallo säteilee saman tehon pois pitkäaaltoisena lämpösäteilynä. Ilman ilmakehää tasapaino asettuisi noin −18 °C:n keskilämpötilaan. Ilmakehän vesihöyry, hiilidioksidi ja metaani kuitenkin päästävät auringonvalon lähes esteettä läpi mutta imevät maanpinnan lähettämää lämpösäteilyä ja säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta, ja tasapaino asettuu noin +15 °C:een. Tätä sanotaan kasvihuoneilmiöksi, ja se vastaa alun kysymykseen.
+Kappaleen lämpötila pysyy vakiona, kun siihen tulee yhtä suuri teho kuin siitä lähtee. Tätä sanotaan energiatasapainoksi. Maapallo saa energiaa Auringon säteilynä, josta noin 30 % heijastuu suoraan takaisin avaruuteen pilvistä, jäästä ja vaaleista pinnoista. Loppu imeytyy, ja maapallo säteilee saman tehon pois pitkäaaltoisena lämpösäteilynä. Ilman ilmakehää tasapaino asettuisi noin −18 °C:n keskilämpötilaan. Ilmakehän vesihöyry, hiilidioksidi ja metaani kuitenkin päästävät auringonvalon lähes esteettä läpi mutta imevät maanpinnan lähettämää lämpösäteilyä ja säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta, ja tasapaino asettuu noin +15 °C:een. Tätä sanotaan kasvihuoneilmiöksi, ja se vastaa alun kysymykseen.
 
 <svg viewBox="0 0 600 300" role="img" aria-label="Maapallon energiatasapaino: Auringosta tuleva säteily, josta osa heijastuu takaisin ja osa imeytyy maanpintaan. Maanpinta säteilee lämpösäteilyä ylöspäin, ja ilmakehän kasvihuonekaasut säteilevät osan siitä takaisin alas." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
   <rect x="20" y="230" width="560" height="50" fill="currentColor" fill-opacity="0.25"/>
@@ -49,7 +49,7 @@
   <text x="484" y="206" fill="currentColor">takaisin</text>
 </svg>
 
-Fossiilisten polttoaineiden käyttö on nostanut ilmakehän hiilidioksidipitoisuuden noin 280 miljoonasosasta yli 420 miljoonasosaan. Kun kasvihuonekaasuja lisätään, avaruuteen pääsee hetkellisesti vähemmän energiaa kuin Auringosta tulee. Ero on nykyään noin 1 W jokaista maapallon neliömetriä kohti. Ylimääräinen energia lämmittää valtameriä, maata ja ilmaa, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan. Tätä on ilmastonmuutos. Pieneltä näyttävä tehoero on koko maapallon alalla valtava, ja suurin osa siitä varastoituu meriin, joiden suuri lämpökapasiteetti hidastaa lämpenemistä mutta myös pitää sen käynnissä pitkään. Energiaratkaisut, kuten eristäminen, lämpöpumput ja päästöttömät voimalaitokset, ovat siksi myös eettisiä valintoja, jotka vaikuttavat tuleviin sukupolviin.
+Fossiilisten polttoaineiden käyttö on nostanut ilmakehän hiilidioksidipitoisuuden noin 280 miljoonasosasta yli 420 miljoonasosaan. Kun kasvihuonekaasuja lisätään, avaruuteen pääsee hetkellisesti vähemmän energiaa kuin Auringosta tulee. Ero on nykyään noin 1 W jokaista maapallon neliömetriä kohti. Ylimääräinen energia lämmittää valtameriä, maata ja ilmaa, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan. Tätä sanotaan ilmastonmuutokseksi. Pieneltä näyttävä tehoero on koko maapallon alalla valtava, ja suurin osa siitä varastoituu meriin, joiden suuri lämpökapasiteetti hidastaa lämpenemistä mutta myös pitää sen käynnissä pitkään. Energiaratkaisut, kuten eristäminen, lämpöpumput ja päästöttömät voimalaitokset, ovat siksi myös eettisiä valintoja, jotka vaikuttavat tuleviin sukupolviin.
 
 ## Kaava
 Rakennusosan läpi johtuva lämpöteho on
@@ -75,7 +75,7 @@
 
 
 ## Esimerkki
-Omakotitalon seinien pinta-ala on 120 m² ja U-arvo 0,17 W/(m²·K), ja ikkunoiden pinta-ala on 20 m² ja U-arvo 1,0 W/(m²·K). Sisällä on 21 °C ja ulkona −15 °C. Kuinka suuri lämpöteho johtuu seinien ja ikkunoiden läpi, ja kuinka paljon energiaa se on vuorokaudessa?
+Omakotitalon seinien pinta-ala on 120 m² ja U-arvo 0,17 W/(m²·K), ja ikkunoiden pinta-ala on 20 m² ja U-arvo 1,0 W/(m²·K). Sisällä on 21 °C ja ulkona −15 °C. Kuinka suuri lämpöteho johtuu seinien ja ikkunoiden läpi, ja kuinka paljon energiaa se siirtää vuorokaudessa?
 
 <!-- vaihe -->
 **Lämpötilaero.** Lämpötilaero on sama kelvineinä ja celsiusasteina:
--- a/solutions.md
+++ b/solutions.md
@@ -44,7 +44,7 @@
 **Kaava:** Rinnakkaisten osien häviö on yhtä suuri kuin patterien teho: P = (U_s A_s + U_y A_y)(T_sisä − T_ulko), joten T_ulko = T_sisä − P / (U_s A_s + U_y A_y)
 **Sijoitus:** U_s A_s + U_y A_y = 0,50 W/(m²·K) · 70 m² + 0,30 W/(m²·K) · 50 m² = 50 W/K. T_ulko = 20 °C − 2000 W / (50 W/K) = 20 °C − 40 K = −20 °C
 **Vastaus:** −20 °C
-**Järkevyys:** Kylmemmällä häviö ylittää 2,0 kW, ja mökki jäähtyy, kunnes tasapaino asettuu alempaan sisälämpötilaan.
+**Järkevyys:** Kylmemmällä säällä häviö ylittää 2,0 kW, ja mökki jäähtyy, kunnes tasapaino asettuu alempaan sisälämpötilaan.
 
 ## fy3-12-L2-02
 **Annettu:** A = 130 m², U = 0,090 W/(m²·K), ΔT = 21 K, t = 230 vrk, hinta h = 0,11 €/kWh
@@ -76,7 +76,7 @@
 **Kaava:** Kahvin luovuttama lämpö on karannut energia: cmΔT = Pt, joten ΔT = Pt / (cm)
 **Sijoitus:** t = 10 · 3600 s = 36 000 s. ΔT = 1,4 W · 36 000 s / (4190 J/(kg·K) · 0,60 kg) = 50 400 J / (2514 J/K) ≈ 20,0 K
 **Vastaus:** 20 K. Tyhjiössä ei ole hiukkasia, joten lämpö ei johdu eikä kulkeudu konvektiolla seinästä toiseen. Kiiltävät pinnat heijastavat lämpösäteilyn takaisin. Lämpöä karkaa pääosin johtumalla pullon kaulan ja korkin kautta.
-**Järkevyys:** Aamulla 90 °C:n kahvi on illalla noin 70 °C:sta, kuten hyvässä termospullossa.
+**Järkevyys:** Aamulla 90 °C:n kahvi on illalla vielä noin 70 °C:n lämpöistä, kuten hyvässä termospullossa.
 
 ## fy3-12-L3-02
 **Annettu:** I = 1,0 W/m², A = 5,1 · 10¹⁴ m², f = 0,90, m = 2,6 · 10²⁰ kg, c = 4,0 · 10³ J/(kg·K), t_v = 365 vrk
--- a/exercises.json
+++ b/exercises.json
@@ -79,7 +79,7 @@
     {
       "id": "fy3-12-L3-01",
       "level": 3,
-      "text": "Hiihtoretkelle pakataan termospulloon 0,60 kg kuumaa kahvia. Pullossa on kaksi sisäkkäistä seinää, joiden välistä on poistettu ilma, ja seinien pinnat ovat kiiltävät. Selitä, mitä lämmön siirtymistapoja tyhjiö ja kiiltävät pinnat estävät ja miten. Mitä kautta lämpöä silti karkaa? Pullosta karkaa lämpöä keskimäärin 1,4 W:n teholla. Kuinka monta kelviniä kahvi jäähtyy 10 tunnissa? Kahvin ominaislämpökapasiteetti on sama kuin veden, 4190 J/(kg·K).",
+      "text": "Hiihtoretkelle pakataan termospulloon 0,60 kg kuumaa kahvia. Pullossa on kaksi sisäkkäistä seinää, joiden välistä on poistettu ilma, ja seinien pinnat ovat kiiltävät. Selitä, mitä lämmön siirtymistapoja tyhjiö ja kiiltävät pinnat estävät ja miten. Minkä kautta lämpöä silti karkaa? Pullosta karkaa lämpöä keskimäärin 1,4 W:n teholla. Kuinka monta kelviniä kahvi jäähtyy 10 tunnissa? Kahvin ominaislämpökapasiteetti on sama kuin veden, 4190 J/(kg·K).",
       "answer": 20,
       "unit": "K",
       "tolerance": 0.02
@@ -95,7 +95,7 @@
     {
       "id": "fy3-12-L3-03",
       "level": 3,
-      "text": "Omakotitaloa lämmittää ilma-vesilämpöpumppu, jonka lämpökerroin on lämmityskauden keskiarvona 2,8. Yläpohjaan puhalletaan lisää eristevillaa, jolloin sen U-arvo pienenee 0,35 W/(m²·K):sta 0,10 W/(m²·K):iin. Yläpohjan pinta-ala on 100 m². Lämmityskausi kestää 5800 h, ja sisä- ja ulkolämpötilan ero on sen aikana keskimäärin 19 K. Kuinka monta kilowattituntia sähköä lisäeristys säästää lämmityskaudessa? Naapurin mielestä eristämisellä ei ole lämpöpumpun omistajalle väliä, koska pumppu ottaa lämmön ilmaiseksi ulkoilmasta. Perustele, miksi eristäminen silti kannattaa.",
+      "text": "Omakotitaloa lämmittää ilma-vesilämpöpumppu, jonka lämpökerroin on lämmityskaudella keskimäärin 2,8. Yläpohjaan puhalletaan lisää eristevillaa, jolloin sen U-arvo pienenee 0,35 W/(m²·K):sta 0,10 W/(m²·K):iin. Yläpohjan pinta-ala on 100 m². Lämmityskausi kestää 5800 h, ja sisä- ja ulkolämpötilan ero on sen aikana keskimäärin 19 K. Kuinka monta kilowattituntia sähköä lisäeristys säästää lämmityskaudessa? Naapurin mielestä eristämisellä ei ole lämpöpumpun omistajalle väliä, koska pumppu ottaa lämmön ilmaiseksi ulkoilmasta. Perustele, miksi eristäminen silti kannattaa.",
       "answer": 984,
       "unit": "kWh",
       "tolerance": 0.02
```

## Checked
- lint_lesson.py fy3-12: 0 errors, 0 warnings (not repeated)
- Decimal comma, thin-space-free unit spacing (plain space, as in the gold lesson), U+2212 minus in text; no hyphen-minus or decimal points in prose
- Case after number+unit: 96 W:n, 210 W:n, 3,5 kW:n, 1,4 W:n, 30 %:sta, 0,35 W/(m²·K):sta all correct
- Terms vs glossary.json: johtuminen, konvektio, lämpösäteily, energiatasapaino, kasvihuoneilmiö, U-arvo, lämpökerroin, ominaislämpökapasiteetti consistent; SVG label "säteily" is an acceptable short form of lämpösäteily
- Stage markers, LaTeX, numbers, JSON values untouched; diff dry-run applies cleanly with patch -p1
- Reading level and paragraph length fine for 16-19 year olds; stage lead-ins (Kaava ratkaistuna, Sijoitus, Järkevyys) well formed
- SVG aria-labels and text labels (heijastuu, takaisin, eriste, sisällä, ulkona) correct Finnish; "takaisin" kept short on purpose (longer label would leave the 600 px viewBox)
