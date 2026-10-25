VERDICT: PASS
CONTENT-HASH: 59c67ca3278e9491

## Blocking
(none)

## Polish
- lesson.md:57 — "koska oletus ei pidä täysin" is not idiomatic; "ei pidä täysin paikkaansa". Also "tarkka muutaman prosentin sisällä" reworded (in diff).
- lesson.md:60 — "ottaa sulaessaan sulamislämmön": the glossary term sulamislämpö is the specific quantity (J/kg), not an amount of energy; "paljon energiaa" (in diff).
- exit-ticket.json:3 — "hiukkasmallilla" vs the lesson and glossary term "mikromalli" (in diff).
- solutions.md:79 — "enemmän kuin sulamisen 20 040 J" is elliptical; "sulamiseen tarvittava" (in diff).
- lesson.md:12 — "sen käyrät ovat sulamis-, kiehumis- ja sublimoitumispisteet" says curves "are" points (copied from the glossary of faasikaavio); "yhdistävät ... pisteet" would be better, but it should then be changed in glossary.json as well, so not in the diff.

## Diff
```diff
diff exit-ticket.json
--- a/exit-ticket.json
+++ b/exit-ticket.json
@@ -1,6 +1,6 @@
 [
   {
-    "q": "Jäämurskaa lämmitetään. Lämpötila nousee 0 °C:seen ja pysyy sitten 0 °C:ssa, kunnes kaikki jää on sulanut, vaikka energiaa siirtyy koko ajan. Selitä hiukkasmallilla, mihin energia kuluu.",
+    "q": "Jäämurskaa lämmitetään. Lämpötila nousee 0 °C:seen ja pysyy sitten 0 °C:ssa, kunnes kaikki jää on sulanut, vaikka energiaa siirtyy koko ajan. Selitä mikromallilla, mihin energia kuluu.",
     "a": "Energia kuluu hiukkasten välisten sidosten purkamiseen eli hiukkasten välisen vuorovaikutusenergian kasvattamiseen. Hiukkasten liike-energia ei kasva, joten lämpötila ei nouse, ennen kuin kaikki jää on sulanut."
   },
   {
diff lesson.md
--- a/lesson.md
+++ b/lesson.md
@@ -54,10 +54,10 @@
 ```latex
 r = \frac{Q}{\Delta m} = \frac{300\,\text{kJ}}{0{,}128\,\text{kg}} \approx 2{,}34\,\text{MJ/kg}
 ```
-Tulos 2,34 MJ/kg on hieman taulukkoarvoa 2,26 MJ/kg suurempi, koska oletus ei pidä täysin. Astia ei enää lämpene, koska vesi on jo kiehumispisteessä, mutta osa kuumentimen energiasta siirtyy astian kautta ympäröivään ilmaan eikä höyrystä vettä. Mittaus on silti tarkka muutaman prosentin sisällä.
+Tulos 2,34 MJ/kg on hieman taulukkoarvoa 2,26 MJ/kg suurempi, koska oletus ei pidä täysin paikkaansa. Astia ei enää lämpene, koska vesi on jo kiehumispisteessä, mutta osa kuumentimen energiasta siirtyy astian kautta ympäröivään ilmaan eikä höyrystä vettä. Tulos on silti muutaman prosentin tarkkuudella oikea.
 
 ## Yleinen virhekäsitys
-Moni luulee, että lämmön lisääminen nostaa aina lämpötilaa. Olomuodon muutoksessa lämpötila pysyy vakiona, vaikka energiaa siirtyy paljon: jään sulattaminen vaatii yhtä paljon energiaa kuin saman veden lämmittäminen 0 °C:sta 80 °C:seen. Toinen virhe on pitää 0-asteista jäätä ja 0-asteista vettä samanarvoisina jäähdyttäjinä. Jää viilentää juomaa paljon tehokkaammin, koska se ottaa sulaessaan sulamislämmön ennen kuin alkaa lämmetä. Kolmas virhe on ajatella, että vesi kiehuu aina 100 °C:ssa: kiehumispiste riippuu paineesta.
+Moni luulee, että lämmön lisääminen nostaa aina lämpötilaa. Olomuodon muutoksessa lämpötila pysyy vakiona, vaikka energiaa siirtyy paljon: jään sulattaminen vaatii yhtä paljon energiaa kuin saman veden lämmittäminen 0 °C:sta 80 °C:seen. Toinen virhe on pitää 0-asteista jäätä ja 0-asteista vettä samanarvoisina jäähdyttäjinä. Jää viilentää juomaa paljon tehokkaammin, koska se ottaa sulaessaan paljon energiaa ennen kuin alkaa lämmetä. Kolmas virhe on ajatella, että vesi kiehuu aina 100 °C:ssa: kiehumispiste riippuu paineesta.
 
 ## Tiivistelmä
 - Olomuodot ovat kiinteä, neste ja kaasu. Mikromallissa olomuodon muutos tarkoittaa hiukkasten välisten sidosten purkautumista tai muodostumista.
diff solutions.md
--- a/solutions.md
+++ b/solutions.md
@@ -76,7 +76,7 @@
 **Kaava:** mehun luovuttama lämpö = jään sulaminen + sulamisveden lämpeneminen: c m₁ (25 °C − T) = s m₂ + c m₂ (T − 0 °C)
 **Sijoitus:** T = (c m₁ · 25 °C − s m₂) / (c (m₁ + m₂)) = (36 662,5 J − 20 040 J) / (4190 J/(kg·K) · 0,41 kg) ≈ 9,7 °C
 **Vastaus:** 9,7 °C
-**Järkevyys:** Kaikki jää sulaa, sillä mehun jäähtyminen 0 °C:seen vapauttaisi 36 662,5 J, enemmän kuin sulamisen 20 040 J. Pelkkä 0-asteinen vesi ottaisi vain lämpenemiseen tarvittavan energian, ja juoman lämpötila olisi noin 21 °C.
+**Järkevyys:** Kaikki jää sulaa, sillä mehun jäähtyminen 0 °C:seen vapauttaisi 36 662,5 J, enemmän kuin sulamiseen tarvittava 20 040 J. Pelkkä 0-asteinen vesi ottaisi vain lämpenemiseen tarvittavan energian, ja juoman lämpötila olisi noin 21 °C.
 
 ## fy3-7-L3-02
 **Annettu:** vesi m = 0,25 kg, 20 °C → 100 °C, c = 4190 J/(kg·K), r = 2 260 000 J/kg; kivet m_k = 30 kg, c_k = 800 J/(kg·K)
```

## Checked
- Lint: 0 errors, 0 warnings; not repeated.
- New lesson.md text (slope sentence before the SVG, "sulaa, Q = sm", "Oletetaan, että …", "Vakiopaineessa", Δm, constants table): grammar, case endings (0 °C:seen, 100 °C:n, 80 °C:seen) and decimal commas correct.
- Terminology against glossary.json (olomuoto, sulamislämpö, höyrystymislämpö, lämpenemiskäyrä, faasikaavio, lämpömäärä, ominaislämpökapasiteetti): consistent apart from the polish items above.
- exercises.json: all 12 texts, new L3-03 (two-power measurement) and L1-05 read well; no "80 N voimalla" type case errors; decimal comma and minus signs correct in text.
- solutions.md L3-01 (melting check) and L3-02 (units on every factor), L3-03: language correct.
- exit-ticket.json: new particle-model Q1 and its answer are correct Finnish, reading level suits 16–19-year-olds.
- sim.js strings (note "höyry pysyy astiassa", slider labels, readout, phase texts, canvas labels) and sim-spec.md ("höyryn oletetaan pysyvän astiassa", locked sliders): genitive + infinitive correct, Finnish decimal comma and minus via fi().
- SVG labels and aria-label in lesson.md: correct Finnish.
- Diff checked with patch --dry-run against the lesson folder: applies cleanly.
- Hash unchanged at start and end of review.
