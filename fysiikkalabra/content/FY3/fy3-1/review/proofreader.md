VERDICT: PASS
CONTENT-HASH: 5c94e4e4c798d64e

# Proofreader, fy3-1, review round 3 (first pass)

## Blocking
None.

## Polish
1. sim-spec.md:1 — "(m · 24,8 N)" and "(0–m · 24,8 N eli" write the Jupiter g as 24,8 N per kg in disguise (kg · N); the house rule says g is m/s² — fix: "m · 24,8 m/s²" (in diff; same wording in the English comment at sim.js:6, not language, left to the fixer/physics-expert).
2. lesson.md:52 — "Massa on aineen määrä": "aineen määrä" is the name of the quantity n (mol, FY3-3 tilanmuuttuja) — fix: "Massa kertoo, kuinka paljon ainetta kappaleessa on" (matches glossary and line 22).
3. lesson.md:8, 48; exercises.json L3-03; solutions.md L3-03 — "kunkin massa on", "jakamalla luvulla 9,81 m/s²" — a quantity with a unit is not a "luku" — fix: "kunkin massa" -> "joiden kunkin massa", "arvolla" (in diff).
4. lesson.md:8 — the calibration paragraph is about 170 words in one block; consider splitting after "...2,5 N venyttää sitä 1,0 cm." for 16-year-olds. Also "putoamiskiihtyvyys" (line 29) is not in glossary.json.
5. lesson.md:3, 22 — "astronautti painaa Kuussa" is colloquial verb use while line 48 warns about "painan 70 kiloa"; not wrong (force, no unit), optional: "astronautin paino Kuussa on vain kuudesosa".

## Diff
```diff
--- a/exercises.json
+++ b/exercises.json
@@ -95,7 +95,7 @@
     {
       "id": "fy3-1-L3-03",
       "level": 3,
-      "text": "Voimamittarin asteikko on tehty Maassa niin, että se näyttää kilogrammoina voiman jaettuna luvulla 9,81 m/s². Mittariin ripustetaan Kuussa (g = 1,62 m/s²) kappale, jonka massa on 6,0 kg. Minkä lukeman mittari näyttää kilogrammoina?",
+      "text": "Voimamittarin asteikko on tehty Maassa niin, että se näyttää kilogrammoina voiman jaettuna arvolla 9,81 m/s². Mittariin ripustetaan Kuussa (g = 1,62 m/s²) kappale, jonka massa on 6,0 kg. Minkä lukeman mittari näyttää kilogrammoina?",
       "answer": 0.99,
       "unit": "kg",
       "tolerance": 0.02
--- a/lesson.md
+++ b/lesson.md
@@ -5,7 +5,7 @@
 ## Ydinajatus
 Kun kaksi kappaletta vaikuttaa toisiinsa, ne ovat vuorovaikutuksessa. Esimerkiksi Maa vetää omenaa puoleensa. Voima kertoo, kuinka voimakas vuorovaikutus on: mitä suurempi voima, sitä voimakkaampi vuorovaikutus. Voiman yksikkö on newton (N), ja noin 1 N on sadan gramman omenan paino Maassa. Tässä vaiheessa kiinnostaa vain voiman suuruus, ja kuvissa nuoli näyttää, mihin suuntaan voima osoittaa.
 
-Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa. Venymä on suoraan verrannollinen voimaan, kun jousta ei venytetä liikaa: kaksinkertainen voima venyttää jousta kaksinkertaisen matkan. Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta, kuten FY1:n suoraan verrannollisissa malleissa, esimerkiksi tasaisen liikkeen $s = v t$. Jos 5,0 N venyttää jousta 2,0 cm, niin 10 N venyttää sitä 4,0 cm ja 2,5 N venyttää sitä 1,0 cm. Asteikko kalibroidaan ripustamalla jouseen samanlaisia pieniä kappaleita, joiden massa on kunkin noin 100 g eli paino noin 1 N. Yksi kappale venyttää jousta tietyn matkan, ja kohta merkitään 1 N:ksi. Kukin kappale vetää jousta yhtä voimakkaasti, joten kaksi kappaletta vetää sitä kaksinkertaisella voimalla ja venyttää sitä kaksinkertaisen matkan; kohta merkitään 2 N:ksi, ja niin edelleen. Sen jälkeen venymästä voi lukea voiman suoraan newtoneina.
+Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa. Venymä on suoraan verrannollinen voimaan, kun jousta ei venytetä liikaa: kaksinkertainen voima venyttää jousta kaksinkertaisen matkan. Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta, kuten FY1:n suoraan verrannollisissa malleissa, esimerkiksi tasaisen liikkeen $s = v t$. Jos 5,0 N venyttää jousta 2,0 cm, niin 10 N venyttää sitä 4,0 cm ja 2,5 N venyttää sitä 1,0 cm. Asteikko kalibroidaan ripustamalla jouseen samanlaisia pieniä kappaleita, joiden kunkin massa on noin 100 g eli paino noin 1 N. Yksi kappale venyttää jousta tietyn matkan, ja kohta merkitään 1 N:ksi. Kukin kappale vetää jousta yhtä voimakkaasti, joten kaksi kappaletta vetää sitä kaksinkertaisella voimalla ja venyttää sitä kaksinkertaisen matkan; kohta merkitään 2 N:ksi, ja niin edelleen. Sen jälkeen venymästä voi lukea voiman suoraan newtoneina.
 
 <svg viewBox="0 0 600 300" role="img" aria-label="Voimamittari: jousi venyy, kun siihen ripustetaan kappale; kappaleen paino G osoittaa alas" style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
   <rect x="150" y="20" width="100" height="14" fill="currentColor"/>
@@ -45,9 +45,9 @@
 Marsissa paino on pienempi, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin.
 
 ## Yleinen virhekäsitys
-Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima luvulla 9,81 m/s². Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.
+Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima arvolla 9,81 m/s². Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.
 
 ## Tiivistelmä
 - Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
-- Paino on voima: $G = m g$. Massa on aineen määrä, ja se on sama kaikkialla.
+- Paino on voima: $G = m g$. Massa kertoo, kuinka paljon ainetta kappaleessa on, ja se on sama kaikkialla.
 - $g = 9{,}81\,\text{m/s}^2$ Maan pinnalla, joten yhden kilogramman massan paino Maassa on noin 9,81 N. Kuussa $g = 1{,}62\,\text{m/s}^2$ ja Marsissa $3{,}71\,\text{m/s}^2$.
--- a/sim-spec.md
+++ b/sim-spec.md
@@ -1 +1 @@
-Voimamittari ja taivaankappale. Pudotusvalikosta valitaan taivaankappale (Kuu, Mars, Maa, Jupiter) ja liukusäätimellä kappaleen massa 1–100 kg. Näytetään voimamittariin ripustettu kappale: jousen venymä ja painon nuolen pituus ovat suoraan verrannollisia painoon G = m g samalla kiinteällä asteikolla, jonka täysi arvo on suurin mahdollinen paino (100 kg Jupiterissa, 2480 N, jolloin nuolen pituus on 110 px). Palkkikaavion palkit ovat verrannollisia painoon valitulla massalla: asteikon täysi arvo on tämän massan paino Jupiterissa (m · 24,8 N), ja asteikko on kirjoitettu kaavion yläpuolelle, joten neljän taivaankappaleen vertailu näkyy aina luettavassa koossa. Siksi jousi venyy ja nuoli pitenee näkyvästi, kun massaa kasvatetaan, ja paino-ero eri taivaankappaleiden välillä näkyy palkeissa; palkkien lukuarvot ja asteikko kasvavat massan mukana. Piirrossa jousella on kiinteä lepopituus, palkilla varmuuden vuoksi vähintään kahden pikselin korkeus ja nuolella vähintään kolmen pikselin pituus, jotta pienimmät painot pysyvät näkyvissä; muuten nuolen pituus ei sisällä vakiotermiä. simState.stretch ja simState.arrow ovat puhtaasti verrannollisia G:hen. Palkkikaaviossa on saman massan paino kaikilla neljällä taivaankappaleella ja valittu korostettuna. Tekstinä kankaan alla: massa (sama kaikkialla), g, paino G = m g ja rivi, joka kertoo palkkikaavion asteikon (0–m · 24,8 N eli tämän massan paino Jupiterissa).
+Voimamittari ja taivaankappale. Pudotusvalikosta valitaan taivaankappale (Kuu, Mars, Maa, Jupiter) ja liukusäätimellä kappaleen massa 1–100 kg. Näytetään voimamittariin ripustettu kappale: jousen venymä ja painon nuolen pituus ovat suoraan verrannollisia painoon G = m g samalla kiinteällä asteikolla, jonka täysi arvo on suurin mahdollinen paino (100 kg Jupiterissa, 2480 N, jolloin nuolen pituus on 110 px). Palkkikaavion palkit ovat verrannollisia painoon valitulla massalla: asteikon täysi arvo on tämän massan paino Jupiterissa (m · 24,8 m/s²), ja asteikko on kirjoitettu kaavion yläpuolelle, joten neljän taivaankappaleen vertailu näkyy aina luettavassa koossa. Siksi jousi venyy ja nuoli pitenee näkyvästi, kun massaa kasvatetaan, ja paino-ero eri taivaankappaleiden välillä näkyy palkeissa; palkkien lukuarvot ja asteikko kasvavat massan mukana. Piirrossa jousella on kiinteä lepopituus, palkilla varmuuden vuoksi vähintään kahden pikselin korkeus ja nuolella vähintään kolmen pikselin pituus, jotta pienimmät painot pysyvät näkyvissä; muuten nuolen pituus ei sisällä vakiotermiä. simState.stretch ja simState.arrow ovat puhtaasti verrannollisia G:hen. Palkkikaaviossa on saman massan paino kaikilla neljällä taivaankappaleella ja valittu korostettuna. Tekstinä kankaan alla: massa (sama kaikkialla), g, paino G = m g ja rivi, joka kertoo palkkikaavion asteikon (0–m · 24,8 m/s² eli tämän massan paino Jupiterissa).
--- a/solutions.md
+++ b/solutions.md
@@ -87,7 +87,7 @@
 **Järkevyys:** Massa on noin kuusinkertainen Maahan verrattuna, koska paino on Kuussa noin kuudesosa.
 
 ## fy3-1-L3-03
-**Annettu:** m = 6,0 kg, g_Kuu = 1,62 m/s²; mittarin asteikko näyttää kilogrammoina voiman jaettuna luvulla 9,81 m/s²
+**Annettu:** m = 6,0 kg, g_Kuu = 1,62 m/s²; mittarin asteikko näyttää kilogrammoina voiman jaettuna arvolla 9,81 m/s²
 **Kysytty:** mittarin lukema
 **Kaava:** mittari mittaa painoa G = m g_Kuu; lukema = G / 9,81 m/s²
 **Sijoitus:** G = 6,0 kg · 1,62 m/s² = 9,72 N; lukema = 9,72 N / 9,81 m/s² = 0,991 kg
```

## Checked
- lint_lesson.py: 0 errors, 0 warnings.
- lesson.md Ydinajatus (3 paragraphs): calibration, FY1 link s = vt, Moon's mass; inflections (1 N:ksi, 5,0 N, 2,0 cm), decimal commas OK.
- lesson.md:29 g paragraph: putoamiskiihtyvyys in m/s², "1 N = 1 kg·m/s²", no N/kg anywhere in lesson, table, exercises, solutions, exit ticket, sim readout.
- exercises.json L1-02 and L1-04 (rewritten): grammar, N:n, cm, nominative number-plus-unit all correct.
- solutions.md: all sanity checks (L1-02, L1-04, L2-03, L3-02 etc.) read correctly; kg:n, kuudesosa, 5/6 eli 83 %.
- exit-ticket.json Q3: Finnish quotes ”…”, "1,5 kg", "N:sta/N:iin" inflections correct.
- sim.js strings (labels, note, title, readout "g = … m/s²") and sim-spec.md readout clause: Finnish correct.
- Terminology paino/massa/voima/vuorovaikutus/voimamittari consistent with glossary.json; reading level fine.
- Hash checked at start and end: 5c94e4e4c798d64e.
