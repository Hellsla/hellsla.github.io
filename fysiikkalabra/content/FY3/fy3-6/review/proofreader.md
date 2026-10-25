VERDICT: PASS
CONTENT-HASH: e05069f43e022d7c

## Blocking
(none)

## Polish
- lesson.md:102 — "mikä on paljon enemmän kuin kappaleen 0,200 kg · 374,6 J/(kg·K)" leaves "lämpökapasiteetti" implicit; read as a sentence it compares a heat capacity with a mass-and-c product — add the word (hunk below).

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -102,1 +102,1 @@
-Huomaa myös, että vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti on 0,300 kg · 4190 J/(kg·K) = 1257 J/K, mikä on paljon enemmän kuin kappaleen 0,200 kg · 374,6 J/(kg·K) ≈ 75 J/K.
+Huomaa myös, että vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti on 0,300 kg · 4190 J/(kg·K) = 1257 J/K, mikä on paljon enemmän kuin kappaleen lämpökapasiteetti 0,200 kg · 374,6 J/(kg·K) ≈ 75 J/K.
```

## Checked
- lesson.md:115 (35 °C note): "Kuuma vesi on vasemmalla puolella kuten yleisessä yhtälössä. Kolmannella rivillä yhtälö on jaettu puolittain kilogrammalla ja sulut on kerrottu auki." is correct Finnish and matches the working (rows 1-2 first equation, row 3 divided by kg and expanded); "jaettu puolittain" and "kerrottu auki" are idiomatic
- lesson.md:115 weighted-mean sentence: "Sama tulos saadaan painotetulla keskiarvolla: T = (3,0 kg · 20 °C + 1,0 kg · 80 °C) / 4,0 kg = 35 °C." correct case, decimal comma, spaced units
- lesson.md:100-102 split paragraphs: "Tulos ilmoitetaan kahdella merkitsevällä numerolla ...", "selittyy lukematarkkuudella tai sillä, että todellisuudessa osa lämmöstä siirtyi myös kalorimetrin astiaan ja ilmaan" grammatical, no meaning error; 24,6 °C:seen, 0,200 kg:n, 0,1 K, 75,5 K inflection and spacing right
- lesson.md c_\text{metalli} (rows 79-91): Finnish word in \text, consistent in both displays; no number or LaTeX judged
- solutions.md:53 (L2-02 "ΔT = 95 °C − 15 °C = 80 K.") and solutions.md:87 ("Tulos on yläraja: todellinen nousu on pienempi, koska osa energiasta kuluu haihtumiseen ja säteilee yöllä pois.") correct, minus sign U+2212, terms consistent with L3-02 task text
- Rest of lesson.md, solutions.md, exercises.json, exit-ticket.json, sim-spec.md, sim.js strings and meta glossary re-read: no errors; terms (ominaislämpökapasiteetti, lämpökapasiteetti, kalorimetri, lämpötasapaino, tasapainolämpötila) match glossary.json; unchanged since round 2
- lint_lesson.py fy3-6: 0 errors, 0 warnings (not repeated)
- Proofreader hash identical at start and end (e05069f43e022d7c)
