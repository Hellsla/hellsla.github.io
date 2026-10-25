VERDICT: PASS
CONTENT-HASH: c6e0cf48e132742e

## Blocking
(none)

## Polish
- lesson.md:51 — the last sentence ("sukeltaja ei tunne sitä, koska sama paine vaikuttaa kämmenen molemmilta puolilta") contradicts the task, where only air pressure acts on the other side of the palm. This is a content/physics matter outside the language domain, so it is not in the diff. Refer it to the physics and pedagogy reviewers.
- lesson.md:54 — "vettä on samaan korkeuteen" is clumsy, and "naulan" is inconsistent with "nasta" in Ydinajatus and the exit ticket. Both fixed in the diff.
- exit-ticket.json q1 — "vaikka sormi työntää kantaa aivan yhtä suurella voimalla" has no referent for "yhtä suurella". Reworded in the diff. q3 — a compound subject takes a plural verb ("ovat"). Fixed in the diff.
- exercises.json L3-03 — "on 1,60 m vettä" is a quantity without a unit noun, and the NOTES rule recommends the "1,60 m:n kerros vettä" form. L1-05 — "on vettä, ja veden syvyys" is redundant. Both fixed in the diff.
- sim-spec.md — "kuolleenmeren" should be a proper noun, as in sim.js. sim.js:34 — "lisää painetta ρg" lacks an inflected ending. Both fixed in the diff.

## Diff
```diff
--- a/exercises.json
+++ b/exercises.json
@@ -35,7 +35,7 @@
     {
       "id": "fy3-4-L1-05",
       "level": 1,
-      "text": "Saunan vesisaavissa on vettä, ja veden syvyys on 0,45 m. Kuinka suuri on hydrostaattinen paine saavin pohjalla? Veden tiheys on 1000 kg/m³.",
+      "text": "Saunan vesisaavissa veden syvyys on 0,45 m. Kuinka suuri on hydrostaattinen paine saavin pohjalla? Veden tiheys on 1000 kg/m³.",
       "answer": 4400,
       "unit": "Pa",
       "tolerance": 0.02
@@ -95,7 +95,7 @@
     {
       "id": "fy3-4-L3-03",
       "level": 3,
-      "text": "Huoltoaseman öljynerotuskaivon pohjalla on 1,60 m vettä ja sen päällä 0,40 m:n kerros öljyä, jonka tiheys on 850 kg/m³. Kuinka suuri on ylipaine kaivon pohjalla? Veden tiheys on 1000 kg/m³. Anna vastaus kilopascaleina.",
+      "text": "Huoltoaseman öljynerotuskaivon pohjalla on 1,60 m:n kerros vettä ja sen päällä 0,40 m:n kerros öljyä, jonka tiheys on 850 kg/m³. Kuinka suuri on ylipaine kaivon pohjalla? Veden tiheys on 1000 kg/m³. Anna vastaus kilopascaleina.",
       "answer": 19,
       "unit": "kPa",
       "tolerance": 0.02
--- a/exit-ticket.json
+++ b/exit-ticket.json
@@ -1,6 +1,6 @@
 [
   {
-    "q": "Nastaa painetaan seinään sormella. Miksi terävä kärki uppoaa seinään, vaikka sormi työntää kantaa aivan yhtä suurella voimalla?",
+    "q": "Nastaa painetaan seinään sormella. Miksi terävä kärki uppoaa seinään, vaikka kärkeen ja kantaan kohdistuu sama voima?",
     "a": "Kärjen pinta-ala on hyvin pieni, joten sama voima jakautuu pienelle alalle ja paine p = F/A on suuri. Kannassa sama voima jakautuu suurelle alalle, joten paine jää pieneksi."
   },
   {
@@ -8,7 +8,7 @@
     "a": "ρgh = 1000 kg/m³ · 9,81 m/s² · 5,0 m ≈ 49 kPa. Kokonaispaine on 101 kPa + 49 kPa ≈ 150 kPa."
   },
   {
-    "q": "Kapea pystyputki ja leveä allas on täytetty vedellä 1,0 m:n korkeuteen. Kummassa pohjan paine on suurempi?",
+    "q": "Kapea pystyputki ja leveä allas ovat täynnä vettä 1,0 m:n korkeuteen. Kummassa pohjan paine on suurempi?",
     "a": "Paine on sama. Hydrostaattinen paine riippuu vain syvyydestä, nesteen tiheydestä ja pinnan paineesta, ei astian muodosta eikä veden määrästä."
   }
 ]
--- a/lesson.md
+++ b/lesson.md
@@ -51,7 +51,7 @@
 Kämmeneen vaikuttaa vain ylipaine, koska ilmanpaine vaikuttaa molemmin puolin. Pinta-ala on $150\,\text{cm}^2 = 0{,}015\,\text{m}^2$, joten voima on $F = pA = 118\,\text{kPa} \cdot 0{,}015\,\text{m}^2 \approx 1{,}8\,\text{kN}$. Se vastaa noin 180 kg:n massan painoa, mutta sukeltaja ei tunne sitä, koska sama paine vaikuttaa kämmenen molemmilta puolilta vedessä ja kehon sisäinen paine tasaantuu.
 
 ## Yleinen virhekäsitys
-Moni ajattelee, että paine pohjassa riippuu siitä, kuinka paljon vettä astiassa on. Kapeassa putkessa ja leveässä altaassa, joissa vettä on samaan korkeuteen, pohjan paine on sama, vaikka altaassa on tuhatkertainen määrä vettä. Paine riippuu vain syvyydestä, tiheydestä ja pinnan paineesta. Toinen virhe on sekoittaa paine ja voima: naulan terävä kärki ei tuota suurempaa voimaa kuin kanta, vaan jakaa saman voiman pienemmälle alalle, jolloin paine on suurempi. Kolmas virhe on unohtaa ilmanpaine: kaavan p = ρgh antaa vain ylipaineen, ja kokonaispaine veden alla on aina sitä suurempi.
+Moni ajattelee, että paine pohjassa riippuu siitä, kuinka paljon vettä astiassa on. Kapeassa putkessa ja leveässä altaassa, joissa vesi ulottuu samaan korkeuteen, pohjan paine on sama, vaikka altaassa on tuhatkertainen määrä vettä. Paine riippuu vain syvyydestä, tiheydestä ja pinnan paineesta. Toinen virhe on sekoittaa paine ja voima: nastan terävä kärki ei tuota suurempaa voimaa kuin kanta, vaan jakaa saman voiman pienemmälle alalle, jolloin paine on suurempi. Kolmas virhe on unohtaa ilmanpaine: kaavan p = ρgh antaa vain ylipaineen, ja kokonaispaine veden alla on aina sitä suurempi.
 
 ## Tiivistelmä
 - Paine on voima pinta-alaa kohti: $p = F/A$. Yksikkö on pascal, 1 Pa = 1 N/m², ja 1 kPa = 1000 Pa.
--- a/sim-spec.md
+++ b/sim-spec.md
@@ -1 +1 @@
-Nesteen paine syvyyden funktiona. Vasemmalla on vedellä täytetty allas, jossa painemittari laskeutuu liukusäätimellä valittuun syvyyteen 0–20 m; nestepinnan yläpuolella on ilma. Toisella liukusäätimellä valitaan nesteen tiheys 700–1300 kg/m³ (bensiini noin 720, vesi 1000, merivesi 1025, kuolleenmeren vesi 1240); ilmanpaine pinnalla on kiinteä 101 kPa. Oikealla on (h, p)-kuvaaja, jossa suora alkaa ilmanpaineesta p₀ ja jonka kulmakerroin ρg muuttuu tiheyden mukana; mittarin nykyinen piste on korostettu. Tekstinä kankaan alla: syvyys, tiheys, hydrostaattinen paine ρgh kilopascaleina, kokonaispaine p₀ + ρgh ja kuinka moninkertainen kokonaispaine on ilmanpaineeseen verrattuna. Valintaruutu ”Näytä vain ylipaine” piirtää kuvaajan ilman vakiotermiä, jotta suoran origon kautta kulkeva muoto näkyy. simState sisältää h, rho, pOver, pTotal ja ratio. Ei satunnaisuutta.
+Nesteen paine syvyyden funktiona. Vasemmalla on nesteellä täytetty allas, jossa painemittari laskeutuu liukusäätimellä valittuun syvyyteen 0–20 m; nestepinnan yläpuolella on ilma. Toisella liukusäätimellä valitaan nesteen tiheys 700–1300 kg/m³ (bensiini noin 720, vesi 1000, merivesi 1025, Kuolleenmeren vesi 1240); ilmanpaine pinnalla on kiinteä 101 kPa. Oikealla on (h, p)-kuvaaja, jossa suora alkaa ilmanpaineesta p₀ ja jonka kulmakerroin ρg muuttuu tiheyden mukana; mittarin nykyinen piste on korostettu. Tekstinä kankaan alla: syvyys, tiheys, hydrostaattinen paine ρgh kilopascaleina, kokonaispaine p₀ + ρgh ja kuinka moninkertainen kokonaispaine on ilmanpaineeseen verrattuna. Valintaruutu ”Näytä vain ylipaine” piirtää kuvaajan ilman vakiotermiä, jotta suoran origon kautta kulkeva muoto näkyy. simState sisältää h, rho, pOver, pTotal ja ratio. Ei satunnaisuutta.
--- a/sim.js
+++ b/sim.js
@@ -31,7 +31,7 @@
     const lc = p.createElement('label').parent(controls).style('flex-direction', 'row').style('align-items', 'center').style('gap', '.6rem').style('min-height', '40px');
     cb = p.createElement('input').attribute('type', 'checkbox').parent(lc).style('width', '24px').style('height', '24px').style('margin', '0');
     p.createSpan('Näytä vain ylipaine').parent(lc);
-    p.createP('Paine kasvaa syvyyden mukana tasaisesti: jokainen metri lisää painetta ρg. Suoran kulmakerroin riippuu tiheydestä, mutta pinnalla paine on aina ilmanpaine.')
+    p.createP('Paine kasvaa syvyyden mukana tasaisesti: jokainen metri lisää painetta ρg:n verran. Suoran kulmakerroin riippuu tiheydestä, mutta pinnalla paine on aina ilmanpaine.')
       .parent('sim-root').class('note');
     p.textFont('Arial');
   };
```

## Checked
- lint_lesson.py fy3-4: 0 errors, 0 warnings; not repeated here.
- Decimal comma in all Finnish text, decimal point in JSON; no stray decimal points in prose.
- Case after number plus unit: "12 m:n syvyydessä", "0,800 m:n syvyydessä", "4,0 m:n korkeuteen", "180 kg:n massan" are all correct.
- Terminology matches glossary.json: paine, pascal, hydrostaattinen paine, ilmanpaine, tiheys, ylipaine, paino.
- g is written as 9,81 m/s² everywhere; N/kg does not appear.
- Quotation marks ”Näytä vain ylipaine” are Finnish style; en dashes in ranges; minus via fi() in sim.js.
- Partitive forms ("vajaata kahta ilmanpainetta", "1,98 kertaa ilmanpaine") and the sim readout strings are correct.
- Reading level is suitable for 16–19-year-olds; solutions.md has no language errors.
- Numbers, LaTeX and JSON values are untouched in the diff; the diff applies cleanly (patch --dry-run -p1).
