VERDICT: PASS
CONTENT-HASH: 3257751b7ee72922

# Proofreader, fy3-1, round 5 (first pass)

## Blocking
None.

## Polish
- exercises.json:98, solutions.md:90 — "näyttää kilogrammoina voiman jaettuna arvolla 9,81 m/s²" reads clumsily (a quantity cannot be shown "jaettuna") — "näyttää kilogrammoina luvun, joka saadaan jakamalla voima arvolla 9,81 m/s²" (in the diff).
- solutions.md:95 — not language, for the mathematician: "26 kg / 0,38 ≈ 69 kg" is 68,4 with the rounded 0,38 (the exact ratio gives 68,75). Suggest using the unrounded ratio 3,71/9,81 or "noin 68-69 kg". I did not touch the number.

## Diff
```diff
--- a/exercises.json
+++ b/exercises.json
@@ -95,7 +95,7 @@
     {
       "id": "fy3-1-L3-03",
       "level": 3,
-      "text": "Voimamittarin asteikko on tehty Maassa niin, että se näyttää kilogrammoina voiman jaettuna arvolla 9,81 m/s². Marsissa (g = 3,71 m/s²) mittari näyttää siihen ripustetulle kappaleelle 26 kg. Mikä on kappaleen massa?",
+      "text": "Voimamittarin asteikko on tehty Maassa niin, että se näyttää kilogrammoina luvun, joka saadaan jakamalla voima arvolla 9,81 m/s². Marsissa (g = 3,71 m/s²) mittari näyttää siihen ripustetulle kappaleelle 26 kg. Mikä on kappaleen massa?",
       "answer": 69,
       "unit": "kg",
       "tolerance": 0.02
--- a/solutions.md
+++ b/solutions.md
@@ -87,7 +87,7 @@
 **Järkevyys:** Massa on noin kuusinkertainen Maahan verrattuna, koska paino on Kuussa noin kuudesosa.
 
 ## fy3-1-L3-03
-**Annettu:** lukema 26 kg, g_Mars = 3,71 m/s²; mittarin asteikko näyttää kilogrammoina voiman jaettuna arvolla 9,81 m/s²
+**Annettu:** lukema 26 kg, g_Mars = 3,71 m/s²; mittarin asteikko näyttää kilogrammoina luvun, joka saadaan jakamalla voima arvolla 9,81 m/s²
 **Kysytty:** m
 **Kaava:** lukema = G / 9,81 m/s², joten G = lukema · 9,81 m/s²; Marsissa G = m g_Mars, joten m = G / g_Mars
 **Sijoitus:** G = 26 kg · 9,81 m/s² = 255,06 N; m = 255,06 N / 3,71 m/s² ≈ 68,75 kg
```

## Checked
- lesson.md:22 new sentence "Kuu on paljon pienempi taivaankappale kuin Maa, ja Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, joten astronautti painaa Kuussa vähemmän" is grammatical; no property of mass is described as changing.
- lesson.md:38 "(1,62/9,81 ≈ 0,17 ≈ 1/6)" correct rounding (0,165 and 0,1667), decimal commas, "kuudesosa" correct.
- Summary "on 9,81 N" without "noin" is consistent with the lesson's exact g = 9,81 m/s² (line 29 too); acceptable.
- L3-03 in exercises.json and solutions.md: inflections (mittari näyttää ... 26 kg, Marsissa), units with space, decimal comma, "lukema" and "mittari" used consistently; g in m/s² only.
- lesson.md lines 1-55 (rest): decimal commas, unit spacing, ”…” quotes, N:ksi/N:n inflections, "painaa" colloquialism explained on line 50, glossary terms (paino, massa, voima, vuorovaikutus, voimamittari, newton, putoamiskiihtyvyys) correct.
- Other 11 exercise texts, solutions.md, exit-ticket.json (N:sta, N:iin, ”vesi painaa puolitoista kiloa”): correct; sim.js strings and sim-spec.md: correct.
- lint_lesson.py: 0 errors, 0 warnings. Hash at start and end: 3257751b7ee72922. Diff dry-run applies with patch -p1.
