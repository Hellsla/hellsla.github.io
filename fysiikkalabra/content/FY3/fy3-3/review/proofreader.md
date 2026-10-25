VERDICT: FAIL
CONTENT-HASH: 9c6ecf76a631b766

Proofreader review of fy3-3 (hash unchanged at start and end). Files checked: lesson.md, exercises.json (text), solutions.md, exit-ticket.json, sim-spec.md, sim.js (Finnish strings), glossary.json entries for fy3-3, meta.json title. check_latex.py: ok. No numbers, formulas, LaTeX or JSON values were touched in the diff.

Errors (cause of FAIL)
1. lesson.md line 13: "Celsius-lämpötilan" is a spelling error (lowercase, no hyphen) and contradicts the glossary form "celsiuslämpötila". Fixed to "Celsiuslämpötilan".
2. solutions.md lines 23 and 39: "77 astetta" / "muutaman asteen" above absolute zero. The lesson (line 17) says kelvins are not "asteita", so this is a terminology error against the lesson's own rule. Fixed to "77 kelviniä" / "muutaman kelvinin".
3. solutions.md line 47: "15 K nousu" lacks the genitive on a number-plus-unit modifier. Fixed to "15 K:n nousu".

Minor / nits (also in the diff)
4. lesson.md line 10: "Asteikkojen yksi aste on yhtä suuri" implies kelvin is an "aste" (same tension as item 2). Reworded to "Celsiusasteen ja kelvinin suuruus on sama" (matches solutions.md wording).
5. lesson.md line 30 (svg aria-label): "celsiusasteessa" is clumsy. Reworded to "lämpötila-alueella 0–100 °C ... lämpötilassa noin −270 °C".
6. exercises.json L2-04: "päivänpuolen" changed to the standard "päiväpuolen".
7. solutions.md L3-02: "tasaisella suoralla", "jokaisella 20 °C:n välillä" and "tulos on absoluuttinen nollapiste" reworded (samalla suoralla; paine nousee 19 kPa jokaista 20 °C:n lämpötilan nousua kohti; tulos vastaa absoluuttista nollapistettä).
8. sim-spec.md: "seinämiin törmäysten perusteella" changed to "seinämiin kohdistuvien törmäysten perusteella".

Checked, no change needed
- Case after number-plus-unit: 21 °C, 20 °C:sta 45 °C:een, 283 K:sta 293 K:iin, 0 °C:ta, 288 K:sta 303 K:iin, 10 °C:sta 20 °C:een are all correct.
- Decimal comma in Finnish text, Finnish quotation marks ”…”, minus sign −, spaces before units: ok.
- Glossary terms systeemi, tilanmuuttuja, lämpötila, kelvin, absoluuttinen nollapiste used consistently; glossary entries for this lesson read correctly.
- sim.js Finnish strings (labels, readout, note) are grammatical; "× 300 K:n keskinopeus" and "1,0 dm³" vs spec "1,00 dm³" are style only.
- Reading level suits 16-19-year-olds.

Notes for the orchestrator (outside proofreading scope)
- glossary.json: tilanmuuttuja lists see_also "paine", which has no glossary entry (CLAUDE.md: add missing terms). Not changed.
- The diff paths a/ = original, b/ = proposed; apply by the fixer to the files in content/FY3/fy3-3/ (glossary.json unchanged).

Unified diff
```diff
diff -u a/exercises.json b/exercises.json
--- content/FY3/fy3-3/exercises.json	2026-10-25 04:34:19.786754210 +0000
+++ content/FY3/fy3-3/exercises.json	2026-10-25 04:34:29.052567870 +0000
@@ -69,7 +69,7 @@
     {
       "id": "fy3-3-L2-04",
       "level": 2,
-      "text": "Kuun yöpuolen lämpötila on −173 °C ja päivänpuolen 127 °C. Kuinka suuri lämpötilaero on kelvineinä?",
+      "text": "Kuun yöpuolen lämpötila on −173 °C ja päiväpuolen 127 °C. Kuinka suuri lämpötilaero on kelvineinä?",
       "answer": 300,
       "unit": "K",
       "tolerance": 0.02
diff -u a/lesson.md b/lesson.md
--- content/FY3/fy3-3/lesson.md	2026-10-25 04:34:19.781814959 +0000
+++ content/FY3/fy3-3/lesson.md	2026-10-25 04:34:29.052427989 +0000
@@ -7,10 +7,10 @@
 
 Miksi näin käy, selittää aineen mikromalli. Kaasu koostuu hiukkasista, jotka liikkuvat jatkuvasti joka suuntaan ja törmäilevät toisiinsa ja astian seinämiin. Lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta: mitä kuumempaa kaasu on, sitä nopeammin hiukkaset keskimäärin liikkuvat. Paine syntyy, kun hiukkaset törmäävät seinämään ja jokainen törmäys työntää seinää hieman. Kun lämpötila nousee mutta tilavuus pysyy samana, hiukkaset osuvat seinään useammin ja kovempaa, joten paine kasvaa. Tästä syystä rengas tuntuu kesällä kovemmalta.
 
-Lämpötilaa mitataan celsiusasteikolla, jossa 0 °C on veden jäätymispiste ja 100 °C kiehumispiste, ja kelvinasteikolla. Kelvinasteikon nollapiste on absoluuttinen nollapiste, alin mahdollinen lämpötila. Siinä hiukkasten keskimääräinen liike-energia on pienimmillään, eikä kylmempää voi olla. Asteikkojen yksi aste on yhtä suuri, joten lämpötilaero on sama kelvineinä ja celsiusasteina.
+Lämpötilaa mitataan celsiusasteikolla, jossa 0 °C on veden jäätymispiste ja 100 °C kiehumispiste, ja kelvinasteikolla. Kelvinasteikon nollapiste on absoluuttinen nollapiste, alin mahdollinen lämpötila. Siinä hiukkasten keskimääräinen liike-energia on pienimmillään, eikä kylmempää voi olla. Celsiusasteen ja kelvinin suuruus on sama, joten lämpötilaero on sama kelvineinä ja celsiusasteina.
 
 ## Kaava
-Celsius-lämpötilan θ muunnos kelvineiksi on:
+Celsiuslämpötilan θ muunnos kelvineiksi on:
 ```latex
 T = \theta + 273{,}15
 ```
@@ -27,7 +27,7 @@
 
 Pisteet asettuvat suoralle:
 
-<svg viewBox="0 0 600 300" role="img" aria-label="Kaasun paine lämpötilan funktiona suljetussa astiassa: mittapisteet 0–100 celsiusasteessa asettuvat suoralle, ja suora ekstrapoloituna leikkaa nollapaineen noin −270 celsiusasteessa" style="max-width:100%;font-family:system-ui,sans-serif;font-size:18px">
+<svg viewBox="0 0 600 300" role="img" aria-label="Kaasun paine lämpötilan funktiona suljetussa astiassa: mittapisteet lämpötila-alueella 0–100 °C asettuvat suoralle, ja ekstrapoloitu suora kohtaa nollapaineen lämpötilassa noin −270 °C" style="max-width:100%;font-family:system-ui,sans-serif;font-size:18px">
   <line x1="70" y1="250" x2="590" y2="250" stroke="currentColor" stroke-width="2"/>
   <line x1="70" y1="250" x2="70" y2="30" stroke="currentColor" stroke-width="2"/>
   <line x1="107" y1="250" x2="445" y2="100" stroke="currentColor" stroke-width="2" stroke-dasharray="7 6"/>
diff -u a/sim-spec.md b/sim-spec.md
--- content/FY3/fy3-3/sim-spec.md	2026-10-25 04:34:19.799719991 +0000
+++ content/FY3/fy3-3/sim-spec.md	2026-10-25 04:34:29.052667307 +0000
@@ -1 +1 @@
-Kaasun mikromalli. Suorakulmaisessa astiassa liikkuu 80 hiukkasta, jotka kimpoavat seinistä. Liukusäätimet: lämpötila 100–600 K ja tilavuus 0,50–2,00 dm³ (astian leveys muuttuu). Hiukkasten nopeus kasvaa lämpötilan mukana. Näytä tekstinä kankaan alla lämpötila kelvineinä ja celsiusasteina, tilavuus, hiukkasten keskinopeus suhteessa 300 K:n nopeuteen sekä seinämiin törmäysten perusteella mitattu paine suhteellisena lukuna (100 vastaa tilannetta 300 K ja 1,00 dm³). Piirrä viereen lämpömittari. Alkutilanne on toistettava eli satunnaislukujen siemen on kiinteä.
+Kaasun mikromalli. Suorakulmaisessa astiassa liikkuu 80 hiukkasta, jotka kimpoavat seinistä. Liukusäätimet: lämpötila 100–600 K ja tilavuus 0,50–2,00 dm³ (astian leveys muuttuu). Hiukkasten nopeus kasvaa lämpötilan mukana. Näytä tekstinä kankaan alla lämpötila kelvineinä ja celsiusasteina, tilavuus, hiukkasten keskinopeus suhteessa 300 K:n nopeuteen sekä seinämiin kohdistuvien törmäysten perusteella mitattu paine suhteellisena lukuna (100 vastaa tilannetta 300 K ja 1,00 dm³). Piirrä viereen lämpömittari. Alkutilanne on toistettava eli satunnaislukujen siemen on kiinteä.
diff -u a/solutions.md b/solutions.md
--- content/FY3/fy3-3/solutions.md	2026-10-25 04:34:19.790963659 +0000
+++ content/FY3/fy3-3/solutions.md	2026-10-25 04:34:29.052629406 +0000
@@ -20,7 +20,7 @@
 **Kaava:** θ = T − 273,15
 **Sijoitus:** θ = 77 − 273,15 = −196,15 °C
 **Vastaus:** −196 °C
-**Järkevyys:** Nestemäinen typpi on hyvin kylmää: 77 K on vain noin 77 astetta absoluuttisen nollapisteen yläpuolella.
+**Järkevyys:** Nestemäinen typpi on hyvin kylmää: 77 K on vain 77 kelviniä absoluuttisen nollapisteen yläpuolella.
 
 ## fy3-3-L1-04
 **Annettu:** θ₁ = 20 °C, θ₂ = 45 °C
@@ -36,7 +36,7 @@
 **Kaava:** θ = T − 273,15
 **Sijoitus:** θ = 2,7 − 273,15 = −270,45 °C
 **Vastaus:** −270 °C
-**Järkevyys:** Lämpötila on vain muutaman asteen absoluuttisen nollapisteen yläpuolella.
+**Järkevyys:** Lämpötila on vain muutaman kelvinin absoluuttisen nollapisteen yläpuolella.
 
 ## fy3-3-L2-01
 **Annettu:** T = 303 K
@@ -44,7 +44,7 @@
 **Kaava:** θ = T − 273,15
 **Sijoitus:** θ = 303 − 273,15 = 29,85 °C
 **Vastaus:** 30 °C
-**Järkevyys:** Alkulämpötila 288 K on 15 °C, ja 15 K nousu antaa 30 °C.
+**Järkevyys:** Alkulämpötila 288 K on 15 °C, ja 15 K:n nousu antaa 30 °C.
 
 ## fy3-3-L2-02
 **Annettu:** (0 °C, 100 kPa), (100 °C, 137 kPa); lineaarinen riippuvuus
@@ -84,7 +84,7 @@
 **Kaava:** k = Δp / Δθ ja p = 0 kohdassa θ = θ₁ − p₁ / k
 **Sijoitus:** k = (326 − 269) kPa / 60 °C = 0,95 kPa/°C; θ = 10 °C − 269 kPa / 0,95 kPa/°C = 10 °C − 283,2 °C = −273,2 °C
 **Vastaus:** −273 °C
-**Järkevyys:** Pisteet ovat tasavälein ja tasaisella suoralla (nousu 19 kPa jokaisella 20 °C:n välillä), ja tulos on absoluuttinen nollapiste.
+**Järkevyys:** Pisteet ovat tasavälein ja samalla suoralla (paine nousee 19 kPa jokaista 20 °C:n lämpötilan nousua kohti), ja tulos vastaa absoluuttista nollapistettä.
 
 ## fy3-3-L3-03
 **Annettu:** θ₁ = 20 °C, E₂ = ½ E₁; E on suoraan verrannollinen T:hen
```
