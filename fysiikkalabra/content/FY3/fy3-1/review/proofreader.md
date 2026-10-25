VERDICT: PASS
CONTENT-HASH: 28956a3df07f9f05

Scope: lesson.md, exercises.json (text), solutions.md, exit-ticket.json, sim-spec.md, sim.js (Finnish strings), glossary.json entries for fy3-1 (massa, newton, paino, voima, vuorovaikutus).

Hash note: the first hash was da9ba5eb24ac7a54. The hash later moved (3444d0df4b2f6a39, then 28956a3df07f9f05) only because another agent edited tests/sims/fy3-1.json (it is part of the hash and has no Finnish text). The lesson files were not touched (mtimes unchanged, last edit 2026-10-24). The review below applies to the current hash.

No spelling, grammar or terminology errors found. Checked and correct: number-plus-unit case forms (12 N:n paino, 6,0 N:n painolla, 15 N:n voimalla, 0,20 kg:n massa, 22,0 kg:n massan, 29 N:sta, 4,9 N:iin, 690 N:n painoa, 3,0 kg:na), decimal commas, units separated by a space, Marsissa/Jupiterissa/Kuussa/Maassa, vaa'alle, Mars-kulkija, "paino" used only as a force, glossary terms (voima, vuorovaikutus, paino, massa, newton) used as defined, reading level suitable for ages 16-19.

Issue kinds (all minor, none blocking):
1. Punctuation: straight quotes "painan 70 kiloa" instead of Finnish ”…” (lesson.md line 50, exit-ticket.json q3). Fix in diff. This is the only convention deviation I would ask to be fixed.
2. Punctuation (glossary.json, "massa"): comma needed before "toisin kuin paino". Fix in diff.
3. Nits (no diff, optional):
   - sim-spec.md: "kankaan alla" (canvas) could be "piirtoalueen alla".
   - lesson.md "Tässä oppitunnissa" could be "Tällä oppitunnilla".
   - lesson.md/solutions.md use "jousivaaka" while the rest uses "voimamittari"; "jousivaaka" is not in glossary.json (consider adding it or saying "voimamittari").
   - exercises.json L3-02: "nostaa 22,0 kg:n massan" is colloquial; "kappaleen" would be more precise, but it is not wrong.
   - lesson.md Tiivistelmä: "Massa on aineen määrä" is loose physics wording (not a language error).

Unified diff (a = original, b = proposed; numbers, formulas, LaTeX and JSON values untouched; the edited JSON files still parse):

```diff
--- content/FY3/fy3-1/lesson.md	2026-10-25 04:17:02.228447163 +0000
+++ content/FY3/fy3-1/lesson.md	2026-10-25 04:17:02.257513873 +0000
@@ -47,7 +47,7 @@
 Robotin massa on molemmissa paikoissa 120 kg. Vain paino muuttuu, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin.
 
 ## Yleinen virhekäsitys
-Arkikielessä sanotaan "painan 70 kiloa", mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että jousivaaka mittaa voimaa, ei massaa: sen lukema muuttuu, kun se viedään toiseen paikkaan.
+Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että jousivaaka mittaa voimaa, ei massaa: sen lukema muuttuu, kun se viedään toiseen paikkaan.
 
 ## Tiivistelmä
 - Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
--- content/FY3/fy3-1/exit-ticket.json	2026-10-25 04:17:02.228491742 +0000
+++ content/FY3/fy3-1/exit-ticket.json	2026-10-25 04:17:02.257681706 +0000
@@ -8,7 +8,7 @@
     "a": "6,0 cm. Venymä on suoraan verrannollinen voimaan, ja voima kolminkertaistuu."
   },
   {
-    "q": "Miksi lause \"painan 70 kiloa\" on fysiikan kannalta epätarkka?",
+    "q": "Miksi lause ”painan 70 kiloa” on fysiikan kannalta epätarkka?",
     "a": "Kilogramma on massan yksikkö, mutta paino on voima ja sen yksikkö on newton. Massa 70 kg tarkoittaa noin 690 N:n painoa Maassa."
   }
 ]
--- glossary.json	2026-10-25 04:17:02.228513759 +0000
+++ glossary.json	2026-10-25 04:17:02.257809053 +0000
@@ -98,7 +98,7 @@
   },
   {
     "term": "massa",
-    "definition": "Massa kertoo, kuinka paljon ainetta kappaleessa on. Massan yksikkö on kilogramma (kg), ja massa on sama kaikkialla toisin kuin paino.",
+    "definition": "Massa kertoo, kuinka paljon ainetta kappaleessa on. Massan yksikkö on kilogramma (kg), ja massa on sama kaikkialla, toisin kuin paino.",
     "lessons": [
       "fy3-1"
     ],
```
