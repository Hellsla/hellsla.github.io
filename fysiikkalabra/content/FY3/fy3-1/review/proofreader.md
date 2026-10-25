VERDICT: PASS
CONTENT-HASH: 8fb367b0d6fd83e0

# Proofreader, fy3-1, round 3 (final)

Checked: lesson.md, exercises.json (text fields), solutions.md, exit-ticket.json, sim-spec.md, Finnish strings in sim.js, glossary.json entries for this lesson (massa, newton, paino, voima, voimamittari, vuorovaikutus). Hash verified at start and end: 8fb367b0d6fd83e0 (unchanged). No lesson file was edited.

No spelling, grammar or terminology errors found. Verified in particular: decimal comma everywhere in Finnish text, units after a space, case after number-plus-unit modifiers (4,0 N:n paino, 12 N:n painolla, 0,20 kg:n kappale, 22,0 kg:n massan, 3,0 kg:na, 29 N:sta, 4,9 N:iin, 1 N:ksi), Finnish quotation marks ”painan 70 kiloa”, place cases (Kuussa, Marsissa, Maassa, Jupiterissa, Marsiin), "mitä lukemaa", glossary terms used consistently, reading level suitable for 16-19-year-olds. Numbers, formulas, LaTeX and JSON values untouched.

## Nits (optional, none blocks the PASS)
1. lesson.md line 21: "Jupiterilla" is inconsistent with "Jupiterissa" used elsewhere (exercises, other bodies in the lesson use the inessive).
2. lesson.md misconception paragraph: "sen lukema muuttuisi, jos se vietäisiin toiseen paikkaan" has an unclear "se"; reworded.
3. solutions.md L2-01 and L2-02 sanity checks: "Noin 10 N painaa yhtä kilogrammaa" and "Noin 100 g painaa 1 N" invert subject and object (a force does not weigh a mass) in the very area the lesson warns about; reworded. Not published, so low impact.
4. sim.js canvas label: "0 – 2480 N" with spaced en dash; Finnish range style is "0–2480 N".

## Unified diff (nits only, copies in scratchpad/proofread-fy31c/)

```diff
--- content/FY3/fy3-1/lesson.md	2026-10-25 04:31:21.328495762 +0000
+++ content/FY3/fy3-1/lesson.md	2026-10-25 04:31:21.344461155 +0000
@@ -18,7 +18,7 @@
 ```latex
 G = m g
 ```
-missä G on paino (N), m massa (kg) ja g painovoiman voimakkuus massayksikköä kohti (N/kg). Luku g kertoo, kuinka suuri on yhden kilogramman massan paino: Maan pinnalla g = 9,81 N/kg, joten 1 kg:n massan paino on 9,81 N. Luku 9,81 on sama kuin FY1:n putoamiskiihtyvyys 9,81 m/s². Tällä kurssilla g:lle käytetään yksikköä N/kg, ja syy lukujen yhtäsuuruuteen selviää FY4:ssä. Muualla g on erilainen. Taulukon arvot koskevat taivaankappaleen pintaa (Jupiterilla pilvien yläpinnan tasoa):
+missä G on paino (N), m massa (kg) ja g painovoiman voimakkuus massayksikköä kohti (N/kg). Luku g kertoo, kuinka suuri on yhden kilogramman massan paino: Maan pinnalla g = 9,81 N/kg, joten 1 kg:n massan paino on 9,81 N. Luku 9,81 on sama kuin FY1:n putoamiskiihtyvyys 9,81 m/s². Tällä kurssilla g:lle käytetään yksikköä N/kg, ja syy lukujen yhtäsuuruuteen selviää FY4:ssä. Muualla g on erilainen. Taulukon arvot koskevat taivaankappaleen pintaa (Jupiterissa pilvien yläpinnan tasoa):
 
 | Taivaankappale | g pinnalla (N/kg) |
 | --- | --- |
@@ -49,7 +49,7 @@
 Marsissa paino on pienempi, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin.
 
 ## Yleinen virhekäsitys
-Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuisi, jos se vietäisiin toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima luvulla 9,81 N/kg. Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.
+Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima luvulla 9,81 N/kg. Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.
 
 ## Tiivistelmä
 - Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
--- content/FY3/fy3-1/solutions.md	2026-10-25 04:31:21.328628864 +0000
+++ content/FY3/fy3-1/solutions.md	2026-10-25 04:31:21.345082212 +0000
@@ -44,7 +44,7 @@
 **Kaava:** G = m g, joten m = G / g
 **Sijoitus:** m = 49 N / 9,81 N/kg = 4,995 kg
 **Vastaus:** 5,0 kg
-**Järkevyys:** Noin 10 N painaa yhtä kilogrammaa, joten 49 N vastaa noin 5 kg.
+**Järkevyys:** Yhden kilogramman paino on noin 10 N, joten 49 N vastaa noin 5 kg:n massaa.
 
 ## fy3-1-L2-02
 **Annettu:** m = 60 g = 0,060 kg, g = 9,81 N/kg
@@ -52,7 +52,7 @@
 **Kaava:** G = m g
 **Sijoitus:** G = 0,060 kg · 9,81 N/kg = 0,5886 N
 **Vastaus:** 0,59 N
-**Järkevyys:** Noin 100 g painaa 1 N, joten 60 g painaa noin 0,6 N.
+**Järkevyys:** Noin 100 g:n kappaleen paino on 1 N, joten 60 g:n kappaleen paino on noin 0,6 N.
 
 ## fy3-1-L2-03
 **Annettu:** m = 145 kg, g_Maa = 9,81 N/kg, g_Kuu = 1,62 N/kg
--- content/FY3/fy3-1/sim.js	2026-10-25 04:31:21.328739744 +0000
+++ content/FY3/fy3-1/sim.js	2026-10-25 04:31:21.345232291 +0000
@@ -85,7 +85,7 @@
     const title = 'Sama massa, paino eri paikoissa', titleMax = 2 * (600 - (BARS.x + BARS.w / 2)) - 10;
     if (p.textWidth(title) > titleMax) p.textSize(ts(13) * titleMax / p.textWidth(title));
     p.text(title, BARS.x + BARS.w / 2, BARS.y - ts(12));
-    p.fill(60); p.textSize(ts(11)); p.text('asteikko 0 – 2480 N', BARS.x + BARS.w / 2, BARS.y + ts(2));
+    p.fill(60); p.textSize(ts(11)); p.text('asteikko 0–2480 N', BARS.x + BARS.w / 2, BARS.y + ts(2));
   };
 
   const fi = (x, d) => x.toFixed(d).replace('.', ',');         // Finnish decimal comma
```
