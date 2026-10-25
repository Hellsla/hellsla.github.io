VERDICT: PASS
CONTENT-HASH: ec606fdba190ce8d

## Blocking
(none)

## Polish
- lesson.md:90 — "kaasun koko painetta" is clumsy — "kaasun kokonaispainetta" (diff).
- lesson.md:94 — the laws are not named in this paragraph, so "laeissa" has no antecedent — "tapauksissa" (diff).
- lesson.md:10 (aria-label) — "kaasupatsaiden" is unusual — "kaasutilan korkeudet" (diff).
- solutions.md:31, :87 and sim.js:57 — "Siksi lämpötilat ovat kelvineinä" is unclear, "lukeman 0 renkaassakin" is awkward, "sitä suurempi paine" lacks a verb (diff).
- lesson.md:177 — heading "Yleinen virhekäsitys" over a list of three misconceptions; leave as is (fixed section name).

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -7,7 +7,7 @@
 
 Mikromallin mukaan kaasun paine syntyy hiukkasten törmäyksistä astian seinämiin. Jos kaasu puristetaan puoleen alkuperäisestä tilavuudesta ja lämpötila pysyy samana, hiukkaset liikkuvat yhtä nopeasti kuin ennen, mutta ne osuvat seinämiin kaksi kertaa niin usein. Paine kaksinkertaistuu.
 
-<svg viewBox="0 0 600 300" role="img" aria-label="Mikromalli Boylen laista, kaaviokuva. Vasemmalla sylinterissä on kahdeksan kaasuhiukkasta tilavuudessa V ja paineessa p. Oikealla samat kahdeksan hiukkasta on puristettu mäntää painamalla puoleen tilavuuteen V/2 samassa lämpötilassa. Nopeusnuolet ovat yhtä pitkät, mutta männän ja pohjan osumamerkkejä on kaksi kertaa niin monta, joten paine on 2p. Kaasupatsaiden korkeudet ovat suhteessa 2 : 1." style="max-width:100%;font-family:system-ui,sans-serif;font-size:26px">
+<svg viewBox="0 0 600 300" role="img" aria-label="Mikromalli Boylen laista, kaaviokuva. Vasemmalla sylinterissä on kahdeksan kaasuhiukkasta tilavuudessa V ja paineessa p. Oikealla samat kahdeksan hiukkasta on puristettu mäntää painamalla puoleen tilavuuteen V/2 samassa lämpötilassa. Nopeusnuolet ovat yhtä pitkät, mutta männän ja pohjan osumamerkkejä on kaksi kertaa niin monta, joten paine on 2p. Kaasutilan korkeudet ovat suhteessa 2 : 1." style="max-width:100%;font-family:system-ui,sans-serif;font-size:26px">
   <rect x="40" y="30" width="160" height="220" fill="currentColor" fill-opacity="0.08"/>
   <polyline points="40,14 40,250 200,250 200,14" fill="none" stroke="currentColor" stroke-width="4"/>
   <rect x="43" y="16" width="154" height="14" fill="currentColor" fill-opacity="0.55"/>
@@ -87,11 +87,11 @@
   <text x="410" y="288" text-anchor="middle" fill="currentColor">V/2 ja 2p</text>
 </svg>
 
-Isotermisessä tilanmuutoksessa paine on siis kääntäen verrannollinen tilavuuteen, ja paineen ja tilavuuden tulo pysyy vakiona. Tätä sanotaan Boylen laiksi. Se pätee hyvin ilmaan ja muihin kaasuihin tavallisissa paineissa ja lämpötiloissa, kunhan kaasun määrä pysyy samana ja paineena käytetään kaasun koko painetta eikä mittarin näyttämää ylipainetta. Tämä vastaa alun kysymykseen: lentokoneen matkustamossa ilmanpaine on noin 78 kPa, joten suljetussa pussissa oleva ilma laajenee, kunnes pussin sisäpuolinen paine on yhtä suuri kuin ulkopuolinen.
+Isotermisessä tilanmuutoksessa paine on siis kääntäen verrannollinen tilavuuteen, ja paineen ja tilavuuden tulo pysyy vakiona. Tätä sanotaan Boylen laiksi. Se pätee hyvin ilmaan ja muihin kaasuihin tavallisissa paineissa ja lämpötiloissa, kunhan kaasun määrä pysyy samana ja paineena käytetään kaasun kokonaispainetta eikä mittarin näyttämää ylipainetta. Tämä vastaa alun kysymykseen: lentokoneen matkustamossa ilmanpaine on noin 78 kPa, joten suljetussa pussissa oleva ilma laajenee, kunnes pussin sisäpuolinen paine on yhtä suuri kuin ulkopuolinen.
 
 Boylen laki voidaan todentaa kokeellisesti. Ruiskuun suljetaan ilmaa, ja ruisku liitetään painemittariin. Mäntää painetaan vaiheittain, ja jokaisella tilavuudella luetaan paine. Mittaus tehdään hitaasti, jotta ilman lämpötila ehtii palata huoneenlämpöön. Kun tulokset piirretään (V, p)-koordinaatistoon, pisteet asettuvat laskevalle kaarelle, josta on vaikea nähdä, onko kyse juuri kääntäen verrannollisuudesta. Siksi taulukkoon lasketaan uusi sarake 1/V ja piirretään p 1/V:n funktiona. Jos laki pätee, pisteet ovat origon kautta kulkevalla suoralla, ja suoran kulmakerroin on vakio pV. Kokeile simulaatiossa: tallenna mittauksia eri tilavuuksilla ja valitse ”Piirrä p 1/V:n funktiona”.
 
-Kun kaasua lämmitetään, sen hiukkaset liikkuvat nopeammin. Jos mäntä pääsee liikkumaan niin, että paine pysyy vakiona (isobaarinen tilanmuutos), kaasu laajenee, ja sen tilavuus on suoraan verrannollinen kelvinlämpötilaan. Jos tilavuus taas pidetään vakiona (isokoorinen tilanmuutos), paine kasvaa, ja se on suoraan verrannollinen kelvinlämpötilaan. Molemmissa laeissa lämpötila on ilmoitettava kelvineinä, koska verrannollisuus alkaa absoluuttisesta nollapisteestä.
+Kun kaasua lämmitetään, sen hiukkaset liikkuvat nopeammin. Jos mäntä pääsee liikkumaan niin, että paine pysyy vakiona (isobaarinen tilanmuutos), kaasu laajenee, ja sen tilavuus on suoraan verrannollinen kelvinlämpötilaan. Jos tilavuus taas pidetään vakiona (isokoorinen tilanmuutos), paine kasvaa, ja se on suoraan verrannollinen kelvinlämpötilaan. Molemmissa tapauksissa lämpötila on ilmoitettava kelvineinä, koska verrannollisuus alkaa absoluuttisesta nollapisteestä.
 
 ## Kaava
 Isotermisessä tilanmuutoksessa eli Boylen lain mukaan
--- a/solutions.md
+++ b/solutions.md
@@ -28,7 +28,7 @@
 **Kaava:** V₁/T₁ = V₂/T₂ (T kelvineinä), josta V₂ = V₁T₂ / T₁
 **Sijoitus:** T₁ = (22 + 273,15) K = 295,15 K ja T₂ = (−18 + 273,15) K = 255,15 K. V₂ = 3,0 l · 255,15 K / 295,15 K = 2,593 l ≈ 2,6 l
 **Vastaus:** 2,6 l
-**Järkevyys:** Pallo kutistuu noin 14 %, mikä näkyy ryppyisenä kumina. Celsiusasteilla laskettu V₂ = 3,0 l · (−18)/22 olisi negatiivinen, mikä on mahdotonta. Siksi lämpötilat ovat kelvineinä.
+**Järkevyys:** Pallo kutistuu noin 14 %, mikä näkyy ryppyisenä kumina. Celsiusasteilla laskettu V₂ = 3,0 l · (−18)/22 olisi negatiivinen, mikä on mahdotonta. Siksi lämpötilat on käytettävä kelvineinä.
 
 ## fy3-9-L1-05
 **Annettu:** p₁ = 101 kPa, θ₁ = 22 °C, θ₂ = −18 °C, tilavuus vakio
@@ -84,7 +84,7 @@
 **Kaava:** p₁/T₁ = p₂/T₂ kokonaispaineelle p = Δp + p₀, josta p₂ = p₁T₂ / T₁ ja lukema Δp₂ = p₂ − p₀
 **Sijoitus:** p₁ = 250 kPa + 101 kPa = 351 kPa, T₁ = 293,15 K ja T₂ = 253,15 K. p₂ = 351 kPa · 253,15 K / 293,15 K = 303,1 kPa. Δp₂ = 303,1 kPa − 101 kPa = 202 kPa
 **Vastaus:** 202 kPa
-**Järkevyys:** Ylipaine ei ole verrannollinen lämpötilaan: lukeman 0 renkaassakin on ilmaa 101 kPa:n paineessa. Lukemalla laskettuna tulos olisi 216 kPa. Lukema laskee lähes viidenneksen, joten renkaat kannattaa tarkistaa pakkasella.
+**Järkevyys:** Ylipaine ei ole verrannollinen lämpötilaan: renkaassa, jonka lukema on 0, on silti ilmaa 101 kPa:n paineessa. Lukemalla laskettuna tulos olisi 216 kPa. Lukema laskee lähes viidenneksen, joten renkaat kannattaa tarkistaa pakkasella.
 
 ## fy3-9-L3-03
 **Annettu:** sylinterin pituus L₁ = 40,0 cm, p₁ = p₀ = 101 kPa, ylipaine Δp = 300 kPa, lämpötila vakio
--- a/sim.js
+++ b/sim.js
@@ -54,7 +54,7 @@
     readout = p.createDiv('').parent('sim-root').class('readout');
     p.createP('Paine lasketaan yhtälöstä pV/T = vakio. Hiukkasten nopeus on verrannollinen √T:hen, kun T on kelvineinä. ' +
               'Kaasun väri kertoo lämpötilan (sininen kylmä, oranssi lämmin; väriasteikko on lämpömittarin vieressä). ' +
-              'Välähdykset ovat hiukkasten törmäyksiä seiniin: mitä tiheämmin ja kovemmin ne osuvat, sitä suurempi paine. ' +
+              'Välähdykset ovat hiukkasten törmäyksiä seiniin: mitä tiheämmin ja kovemmin ne osuvat, sitä suurempi paine on. ' +
               'Isobaarisessa muutoksessa punnus pitää paineen vakiona, isokoorisessa mäntä on lukittu. ' +
               'Kuvaajan haalea viiva on teoria, katkoviiva jatkaa suoraa origoon, siniset pisteet ovat tallennetut mittaukset ja punainen piste on nykyinen tila.')
       .parent('sim-root').class('note');
```

## Checked
- Lint run first (0 errors, 0 warnings), not repeated; no paragraph over 91 words, stage markers untouched.
- Changed lesson.md text (new Ydinajatus split, bullet list, five example stages, new sentences before the isobaric figure): grammar, case after number+unit (101 kPa:n, 10 °C:sta ... 20 °C:seen), decimal comma, minus sign U+2212 and spaces before units all correct.
- Three SVG aria-labels and visible labels (osuma, T vakio, V ja p, V/2 ja 2p, jatke, T (K)) are correct Finnish; "kaaviokuva" and "mittakaavassa" state schematic or to-scale as NOTES.md section 4 asks.
- Example stage lead-ins (Tunnetut ja kysytty, Kaava ratkaistuna, Sijoitus, Tulos, Järkevyys) are consistent; the text before each display introduces it correctly.
- solutions.md new symbolic Kaava lines and Sijoitus sentences (including T kelvineinä and Δp wording) read correctly; numbers, formulas and LaTeX untouched.
- sim.js: canvas labels (punnus, kPa, T = ... K, V = ... ml, axis names), readout, select options, table header, empty row and the longer DOM note read correctly; ”Tallenna mittaus” quotes are right.
- Terms match glossary.json (tilanmuutos, isoterminen, isobaarinen, isokoorinen, Boylen laki, kelvin, absoluuttinen nollapiste, ylipaine); no invented synonyms.
- exercises.json, exit-ticket.json, sim-spec.md re-read: unchanged since round 1 and correct.
- Reading level suits 16-19-year-olds.
- Hash re-run at the end: ec606fdba190ce8d (unchanged from start).
