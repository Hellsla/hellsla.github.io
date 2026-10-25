VERDICT: FAIL
CONTENT-HASH: 307c0dfc144588a5

Proofreader re-review of fy3-1 after the g paragraph was converted to m/s². Checked lesson.md, exercises.json, solutions.md, exit-ticket.json, sim-spec.md, sim.js Finnish strings, glossary entries (massa, newton, paino, voima, voimamittari, vuorovaikutus). Clean: decimal commas, unit spacing, case after number+unit (N:n, kg:n, N:ksi), ”…” quotes, new g paragraph in lesson.md (grammar and terminology correct; g always in m/s²), exercise texts, exit ticket, sim strings.

Issue kinds
1. grammar/terminology (blocking), solutions.md L2-01 Järkevyys: "Noin 10 N painaa yhtä kilogrammaa" has subject and object reversed (a force "weighs" a mass). The same colloquial "painaa" for kilograms/grams appears in L1-01 ("Yksi kilogramma painaa noin 10 N") and L2-02 ("Noin 100 g painaa 1 N"), which contradicts the lesson's own massa/paino misconception section. Fixed in diff with "massan paino on noin ...".
2. terminology/wording (should fix), lesson.md Tiivistelmä last bullet: "g = 9,81 m/s²: yhden kilogramman massan paino Maassa" equates g (m/s²) with a weight. Reworded in diff; no numbers changed (9,81 already appears in the lesson).
3. Nits (no change made):
   - lesson.md uses "Jupiterilla" (table note), exercises use "Jupiterissa"; Marsissa is used everywhere. Pick one.
   - g is called "painovoiman voimakkuus" in the formula text and "putoamiskiihtyvyys" next to it; neither is in glossary.json. Consider adding one glossary entry.
   - "1180 N" and "2480 N": Finnish convention allows a thin space in thousands ("1 180 N"); optional.
   - L3-03 "Mitä lukemaa mittari näyttää" is acceptable; "Mikä on mittarin lukema kilogrammoina?" is more standard.
   - Heading "paino G = mg" vs "G = m g" in body; sim-spec phrase "muuten nuolen pituus ei sisällä vakiotermiä" is terse.

Unified diff (made on copies in scratchpad/proofread-fy31d, paths relabelled)

```diff
--- content/FY3/fy3-1/solutions.md	2026-10-25 05:13:47.324456206 +0000
+++ content/FY3/fy3-1/solutions.md	2026-10-25 05:13:47.345379773 +0000
@@ -4,7 +4,7 @@
 **Kaava:** G = m g
 **Sijoitus:** G = 4,0 kg · 9,81 m/s² = 39,24 N
 **Vastaus:** 39 N
-**Järkevyys:** Yksi kilogramma painaa noin 10 N, joten 4 kg painaa noin 40 N.
+**Järkevyys:** Yhden kilogramman massan paino on noin 10 N, joten 4 kg:n massan paino on noin 40 N.
 
 ## fy3-1-L1-02
 **Annettu:** 4,0 N → 2,0 cm, kysytty venymä painolla 12 N
@@ -44,7 +44,7 @@
 **Kaava:** G = m g, joten m = G / g
 **Sijoitus:** m = 49 N / 9,81 m/s² = 4,995 kg
 **Vastaus:** 5,0 kg
-**Järkevyys:** Noin 10 N painaa yhtä kilogrammaa, joten 49 N vastaa noin 5 kg.
+**Järkevyys:** Yhden kilogramman massan paino on noin 10 N, joten 49 N vastaa noin 5 kg:n massaa.
 
 ## fy3-1-L2-02
 **Annettu:** m = 60 g = 0,060 kg, g = 9,81 m/s²
@@ -52,7 +52,7 @@
 **Kaava:** G = m g
 **Sijoitus:** G = 0,060 kg · 9,81 m/s² = 0,5886 N
 **Vastaus:** 0,59 N
-**Järkevyys:** Noin 100 g painaa 1 N, joten 60 g painaa noin 0,6 N.
+**Järkevyys:** Sadan gramman massan paino on noin 1 N, joten 60 g:n massan paino on noin 0,6 N.
 
 ## fy3-1-L2-03
 **Annettu:** m = 145 kg, g_Maa = 9,81 m/s², g_Kuu = 1,62 m/s²
--- content/FY3/fy3-1/lesson.md	2026-10-25 05:13:47.324513507 +0000
+++ content/FY3/fy3-1/lesson.md	2026-10-25 05:13:47.345545845 +0000
@@ -54,4 +54,4 @@
 ## Tiivistelmä
 - Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
 - Paino on voima: $G = m g$. Massa on aineen määrä, ja se on sama kaikkialla.
-- $g = 9{,}81\,\text{m/s}^2$: yhden kilogramman massan paino Maassa. Kuussa $g = 1{,}62\,\text{m/s}^2$ ja Marsissa $3{,}71\,\text{m/s}^2$.
+- $g = 9{,}81\,\text{m/s}^2$ Maassa, joten yhden kilogramman massan paino Maassa on 9,81 N. Kuussa $g = 1{,}62\,\text{m/s}^2$ ja Marsissa $3{,}71\,\text{m/s}^2$.
```
