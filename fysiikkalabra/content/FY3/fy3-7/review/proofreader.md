VERDICT: FAIL
CONTENT-HASH: 46da849c4583fb46
## Blocking
- lesson.md:8 — "Höyrystyessä sama energia vapautuu, kun höyry tiivistyy" reads as if energy is released during evaporation (it is absorbed), and "sama" has no referent — "Veden höyrystyessä sitoutunut energia vapautuu takaisin, kun höyry tiivistyy" (in diff)
## Polish
- lesson.md:6 — "mitä tapahtuu pakkasella kuivuvalle pyykille" is clumsy — "kuten pakkasella kuivuvassa pyykissä"; lesson.md:12 — "alle 100 °C:ssa" — "alle 100 °C:n lämpötilassa" (in diff)
- solutions.md:31, :39 — "yli 50 K", "lämmittäminen 18 K vaatii" lack the case ending — "50 K:lla", "18 K:lla"; solutions.md:79 — "juoma jäisi noin 21 °C:seen" is wrong case/subject, reworded (in diff)
- exercises.json L2-02 "jotta jää lämpenee ... sulaa" — "jotta" takes the conditional: "lämpenisi ... sulaisi"; L2-01 "Kuinka kauan kestää, että" — "ennen kuin"; L2-04 "kiehumispisteeseen 100 °C:seen" — "eli" (in diff)
- lesson.md:45 vs :47 — displayed result "≈ 2,3 MJ/kg" but text says "2,34 MJ/kg" (300/0,128 = 2,344); not a language issue and numbers are not mine to change, left for the fixer or physics reviewer to align the figures
## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -3,13 +3,13 @@
 > **Miksi** kiehuvan veden lämpötila ei nouse yli 100 °C:n, vaikka liesi on täysillä ja kattilaan siirtyy koko ajan energiaa?
 
 ## Ydinajatus
-Aine esiintyy kolmessa olomuodossa: kiinteänä, nesteenä ja kaasuna. Mikromallin mukaan kiinteässä aineessa hiukkaset värähtelevät paikoillaan toistensa sitomina, nesteessä ne liikkuvat toistensa ohi mutta pysyvät yhdessä, ja kaasussa ne liikkuvat vapaasti ja törmäilevät vain harvoin. Olomuodon muutoksessa hiukkasten keskinäinen sidos muuttuu: sulamisessa kiinteän aineen järjestys purkautuu, ja höyrystymisessä hiukkaset irtoavat kokonaan toisistaan. Vastakkaiset muutokset ovat jähmettyminen ja tiivistyminen. Jää voi myös sublimoitua suoraan höyryksi, mitä tapahtuu pakkasella kuivuvalle pyykille.
+Aine esiintyy kolmessa olomuodossa: kiinteänä, nesteenä ja kaasuna. Mikromallin mukaan kiinteässä aineessa hiukkaset värähtelevät paikoillaan toistensa sitomina, nesteessä ne liikkuvat toistensa ohi mutta pysyvät yhdessä, ja kaasussa ne liikkuvat vapaasti ja törmäilevät vain harvoin. Olomuodon muutoksessa hiukkasten keskinäinen sidos muuttuu: sulamisessa kiinteän aineen järjestys purkautuu, ja höyrystymisessä hiukkaset irtoavat kokonaan toisistaan. Vastakkaiset muutokset ovat jähmettyminen ja tiivistyminen. Jää voi myös sublimoitua suoraan höyryksi, kuten pakkasella kuivuvassa pyykissä.
 
-Olomuodon muutos vaatii energiaa, mutta ei nosta lämpötilaa. Kun jäätä lämmitetään, sen lämpötila nousee 0 °C:seen asti. Sitten lämpötila pysyy vakiona, kunnes kaikki jää on sulanut, vaikka energiaa siirtyy koko ajan: energia kuluu hiukkasten sidosten purkamiseen eli hiukkasten välisen vuorovaikutusenergian kasvattamiseen, ei niiden liikkeen kiihdyttämiseen. Samasta syystä kiehuva vesi pysyy 100 °C:ssa, vaikka liesi on täysillä: kaikki siirtyvä energia kuluu veden höyrystämiseen. Mitä suurempi teho, sitä nopeammin vesi kiehuu pois, mutta ei sitä kuumemmaksi. Höyrystyessä sama energia vapautuu, kun höyry tiivistyy, ja siksi 100-asteinen höyry polttaa pahemmin kuin 100-asteinen vesi.
+Olomuodon muutos vaatii energiaa, mutta ei nosta lämpötilaa. Kun jäätä lämmitetään, sen lämpötila nousee 0 °C:seen asti. Sitten lämpötila pysyy vakiona, kunnes kaikki jää on sulanut, vaikka energiaa siirtyy koko ajan: energia kuluu hiukkasten sidosten purkamiseen eli hiukkasten välisen vuorovaikutusenergian kasvattamiseen, ei niiden liikkeen kiihdyttämiseen. Samasta syystä kiehuva vesi pysyy 100 °C:ssa, vaikka liesi on täysillä: kaikki siirtyvä energia kuluu veden höyrystämiseen. Mitä suurempi teho, sitä nopeammin vesi kiehuu pois, mutta ei sitä kuumemmaksi. Veden höyrystyessä sitoutunut energia vapautuu takaisin, kun höyry tiivistyy, ja siksi 100-asteinen höyry polttaa pahemmin kuin 100-asteinen vesi.
 
 Sulamiseen ja höyrystymiseen tarvittava lämpömäärä on suoraan verrannollinen massaan. Kertoimet ovat aineelle ominaisia: ominaissulamislämpö s kertoo, kuinka paljon energiaa yhden kilogramman sulattaminen vaatii, ja ominaishöyrystymislämpö r, kuinka paljon yhden kilogramman höyrystäminen vaatii. Vedelle s = 334 kJ/kg ja r = 2260 kJ/kg. Höyrystäminen vaatii siis lähes seitsemän kertaa enemmän energiaa kuin sulattaminen ja yli viisi kertaa enemmän kuin veden lämmittäminen 0 °C:sta 100 °C:seen.
 
-Kiehumispiste riippuu paineesta. Faasikaavio esittää, missä olomuodossa aine on kussakin lämpötilassa ja paineessa: sen käyrät ovat sulamis-, kiehumis- ja sublimoitumispisteet eri paineissa. Vuorella, jossa ilmanpaine on pienempi, vesi kiehuu alle 100 °C:ssa, ja painekattilassa paine nostaa kiehumispisteen yli 100 °C:n, jolloin ruoka kypsyy nopeammin.
+Kiehumispiste riippuu paineesta. Faasikaavio esittää, missä olomuodossa aine on kussakin lämpötilassa ja paineessa: sen käyrät ovat sulamis-, kiehumis- ja sublimoitumispisteet eri paineissa. Vuorella, jossa ilmanpaine on pienempi, vesi kiehuu alle 100 °C:n lämpötilassa, ja painekattilassa paine nostaa kiehumispisteen yli 100 °C:n, jolloin ruoka kypsyy nopeammin.
 
 ## Kaava
 Massan m sulattamiseen tai höyrystämiseen tarvittava lämpömäärä on
--- a/solutions.md
+++ b/solutions.md
@@ -28,7 +28,7 @@
 **Kaava:** Q = r m (tiivistyessä vapautuu sama lämpömäärä, joka höyrystymiseen tarvitaan)
 **Sijoitus:** Q = 2260 kJ/kg · 0,030 kg = 67,8 kJ ≈ 68 kJ
 **Vastaus:** 68 kJ
-**Järkevyys:** 68 kJ riittää lämmittämään noin 0,3 kg maitoa yli 50 K, joten pieni höyrymäärä lämmittää kannullisen maitoa. Samasta syystä höyry polttaa ihoa pahemmin kuin yhtä kuuma vesi.
+**Järkevyys:** 68 kJ riittää lämmittämään noin 0,3 kg maitoa yli 50 K:lla, joten pieni höyrymäärä lämmittää kannullisen maitoa. Samasta syystä höyry polttaa ihoa pahemmin kuin yhtä kuuma vesi.
 
 ## fy3-7-L1-05
 **Annettu:** lämpenemiskäyrän vaakasuora osa 0 °C:ssa alkaa kohdasta 19 kJ ja päättyy kohtaan 186 kJ
@@ -36,7 +36,7 @@
 **Kaava:** vaakasuoralla osalla jää sulaa vakiolämpötilassa, Q = s m; käyrästä Q luetaan energia-akselin muutoksena
 **Sijoitus:** Q = 186 kJ − 19 kJ = 167 kJ
 **Vastaus:** 167 kJ
-**Järkevyys:** Jää sulaa, joten lämpötila pysyy 0 °C:ssa, vaikka energiaa siirtyy. Jään massa on m = Q/s = 167 kJ / 334 kJ/kg = 0,50 kg, ja tällaisen jään lämmittäminen 18 K vaatii 2100 J/(kg·K) · 0,50 kg · 18 K ≈ 19 kJ, kuten käyrän alussa.
+**Järkevyys:** Jää sulaa, joten lämpötila pysyy 0 °C:ssa, vaikka energiaa siirtyy. Jään massa on m = Q/s = 167 kJ / 334 kJ/kg = 0,50 kg, ja tällaisen jään lämmittäminen 18 K:lla vaatii 2100 J/(kg·K) · 0,50 kg · 18 K ≈ 19 kJ, kuten käyrän alussa.
 
 ## fy3-7-L2-01
 **Annettu:** P = 2,0 kW = 2000 W, höyrystyvä vesi m = 0,50 kg, r = 2260 kJ/kg = 2 260 000 J/kg
@@ -76,7 +76,7 @@
 **Kaava:** mehun luovuttama lämpö = jään sulaminen + sulamisveden lämpeneminen: c m₁ (25 °C − T) = s m₂ + c m₂ (T − 0 °C)
 **Sijoitus:** T = (c m₁ · 25 °C − s m₂) / (c (m₁ + m₂)) = (36 662,5 J − 20 040 J) / (4190 J/(kg·K) · 0,41 kg) ≈ 9,7 °C
 **Vastaus:** 9,7 °C
-**Järkevyys:** Jää ottaa sulaessaan 20 kJ ennen kuin alkaa lämmetä. 0-asteinen vesi ottaisi vain lämpenemisen osuuden, ja juoma jäisi noin 21 °C:seen.
+**Järkevyys:** Jää ottaa sulaessaan 20 kJ ennen kuin sulamisvesi alkaa lämmetä. Pelkkä 0-asteinen vesi ottaisi vain lämpenemiseen tarvittavan energian, ja juoman lämpötila olisi noin 21 °C.
 
 ## fy3-7-L3-02
 **Annettu:** vesi m = 0,25 kg, 20 °C → 100 °C, c = 4190 J/(kg·K), r = 2 260 000 J/kg; kivet m_k = 30 kg, c_k = 800 J/(kg·K)
--- a/exercises.json
+++ b/exercises.json
@@ -45,7 +45,7 @@
     {
       "id": "fy3-7-L2-01",
       "level": 2,
-      "text": "Mökin sähköhellan keittolevyn teho on 2,0 kW. Levyllä on kattila, jossa vesi kiehuu, ja kattila unohtuu liedelle. Kuinka kauan kestää, että kattilasta on kiehunut pois 0,50 kg vettä? Oleta, että kaikki levyn energia siirtyy veteen. Anna vastaus minuutteina.",
+      "text": "Mökin sähköhellan keittolevyn teho on 2,0 kW. Levyllä on kattila, jossa vesi kiehuu, ja kattila unohtuu liedelle. Kuinka kauan kestää, ennen kuin kattilasta on kiehunut pois 0,50 kg vettä? Oleta, että kaikki levyn energia siirtyy veteen. Anna vastaus minuutteina.",
       "answer": 9.4,
       "unit": "min",
       "tolerance": 0.02
@@ -53,7 +53,7 @@
     {
       "id": "fy3-7-L2-02",
       "level": 2,
-      "text": "Pakastimesta otetaan 750 g jäätä, jonka lämpötila on −18 °C. Kuinka suuri lämpömäärä tarvitaan, jotta jää lämpenee 0 °C:seen ja sulaa kokonaan 0-asteiseksi vedeksi? Jään ominaislämpökapasiteetti on 2100 J/(kg·K). Anna vastaus kilojouleina.",
+      "text": "Pakastimesta otetaan 750 g jäätä, jonka lämpötila on −18 °C. Kuinka suuri lämpömäärä tarvitaan, jotta jää lämpenisi 0 °C:seen ja sulaisi kokonaan 0-asteiseksi vedeksi? Jään ominaislämpökapasiteetti on 2100 J/(kg·K). Anna vastaus kilojouleina.",
       "answer": 280,
       "unit": "kJ",
       "tolerance": 0.02
@@ -69,7 +69,7 @@
     {
       "id": "fy3-7-L2-04",
       "level": 2,
-      "text": "Pastan keittämistä varten kattilaan laitetaan 2,0 kg vettä, jonka lämpötila on 15 °C. Vesi lämmitetään kiehumispisteeseen 100 °C:seen, ja sitä keitetään, kunnes kattilasta on höyrystynyt 0,10 kg vettä. Kuinka suuri lämpömäärä veteen siirtyy kaikkiaan? Anna vastaus megajouleina.",
+      "text": "Pastan keittämistä varten kattilaan laitetaan 2,0 kg vettä, jonka lämpötila on 15 °C. Vesi lämmitetään kiehumispisteeseen eli 100 °C:seen, ja sitä keitetään, kunnes kattilasta on höyrystynyt 0,10 kg vettä. Kuinka suuri lämpömäärä veteen siirtyy kaikkiaan? Anna vastaus megajouleina.",
       "answer": 0.94,
       "unit": "MJ",
       "tolerance": 0.02
```
## Checked
- lint_lesson.py fy3-7: 0 errors, 0 warnings (not repeated)
- Decimal comma in prose and sim readout (fi helper), decimal point in JSON values
- Space before units throughout; thousands separated by space in solutions and sim (fj)
- Minus sign is U+2212 everywhere (−18 °C, −20 °C, axis labels); no hyphen-minus numbers
- Finnish quotation marks ”Lämmitä” and ”Nollaa” in sim-spec.md correct
- Case after number plus unit (80 N:n style): 1000 W:n, 0,50 kg:n, 100 °C:seen, 0 °C:ssa, 0 °C:sta correct elsewhere
- Terminology against glossary: olomuoto, ominaissulamislämpö, ominaishöyrystymislämpö, lämpenemiskäyrä, faasikaavio, lämpömäärä, kuumennin used consistently; no synonyms invented
- sim.js Finnish strings (PHASE_TEXT, CONTENT, readout, labels), exit-ticket.json and sim-spec.md read: no errors
- Reading level suitable for 16-19-year-olds; no numbers, LaTeX or JSON values touched; diff dry-run applies with patch -p1 and exercises.json stays valid JSON
- Hash before and after review identical (unchanged during review)
