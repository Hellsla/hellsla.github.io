VERDICT: FAIL

Proofreader report for fy3-2 (Työ ja energia). Files checked: lesson.md, exercises.json (text fields), solutions.md, exit-ticket.json, sim-spec.md, sim.js (Finnish strings), against glossary.json. No numbers, formulas, LaTeX or JSON values were changed in the diff. Working copies are in /tmp/claude-0/-home-user-hellsla-github-io/1d51c594-3563-5c38-9136-caaa788c1662/scratchpad/proofread2/ (a = original, b = proposed).

## Issue kinds

Real errors (cause of FAIL):
1. Number-plus-unit modifier missing genitive: lesson.md line 10 "Kiukaan 6 kW teho" -> "6 kW:n teho".
2. Wrong subject / semantics: exercises.json L3-03 "paneelin pitää paistaa" (a panel does not shine) -> "auringon pitää paistaa paneeliin".
3. Compound numeral: solutions.md L1-02 "kahden sadan joulen" -> "kahdensadan joulen".
4. Missing case on number-plus-unit: solutions.md L3-01 "pysyy 40 N matkalla" -> "pysyy 40 N:ssä matkalla" (matches the exercise text).
5. Wrong case form: sim.js note "vakiovauhtia" -> "vakiovauhdilla" (lesson uses "tasaisella vauhdilla").
6. Misused term: exercises.json L3-02 and solutions.md L3-02 "veden lämpömääräksi" / "muuttuu lämpömääräksi" (energy is transferred to the water as heat, it does not become a "lämpömäärä" of the water); also clumsy "painon menettämä nostotyön suuruinen energia" simplified.

Wording / reading level (fixed in diff):
7. "koko matkan ajan" and "matkan 0–2,0 m ajan" (matka is not a time span) -> "koko matkalla", "matkalla 0–2,0 m" (exercises L1-04, L2-04).
8. "vetovoima" can be read as gravitational attraction; replaced by "vetävä voima" in exercises L1-05 and sim.js note.
9. solutions.md: sentence fragment "Neljä minuuttia pumppausta, uskottavaa." and hard-to-read "Neljännesmegajoulen työ" rewritten; "reilun metrin" -> "reilun metrin korkeuteen".

Nits, NOT in the diff (PASS-level, for the human to decide):
- Space before units is a normal space everywhere (lesson, exercises, solutions, sim.js); CLAUDE.md asks for a thin space. The gold lesson also uses normal spaces, so left alone. If the build does not convert them, a site-wide pass is needed.
- exercises.json L1-01 "25 metrin matkan" (genitive) vs L1-04 "6,0 m:n matka" (nominative) in a passive sentence; both acceptable, inconsistent. Unit written out "metrin" in L1-01 but "m" elsewhere.
- "paino" is used both for the force G (N) and for the falling weight in Joule's experiment ("2,0 kg:n paino", lesson.md line 8 "putoavan painon", "eri painoilla"). Consider "punnus" for the object. Not changed because it touches several sentences and the glossary has no entry.
- "lämpömäärä" (exercises/solutions) is not in glossary.json while lesson.md says "lämpö"; consider adding the term to the glossary.
- sim-spec.md (written by the human): "animoi laatikko liikkumaan matkan s ajassa t Vedä-napista" is understandable but awkward ("Vedä-napin painalluksesta"). Left unchanged.
- solutions.md L3-03 sanity check uses kWh (not SI per CLAUDE.md); content decision, not changed.
- sim.js note "kitka ottaa vastaan ... työn" is physically loose wording; physics reviewer's call.
- Decimal commas, case endings of "N:n", "N:iin", "N:sta", "kJ:n", "m:n", "kg:n", "m/s:n", glossary terms (työ, energia, teho, joule) and JSON validity all checked and correct otherwise. exercises.json still parses after the edits.

## Unified diff (originals vs. proposed; paths relative to content/FY3/fy3-2/)

```diff
--- content/FY3/fy3-2/lesson.md	2026-10-24 14:49:52.068641224 +0000
+++ content/FY3/fy3-2/lesson.md	2026-10-24 14:49:52.084874506 +0000
@@ -7,7 +7,7 @@
 
 Työ on tapa siirtää energiaa. Tämän osoitti James Prescott Joule 1840-luvulla antamalla putoavan painon pyörittää siipipyörää vedessä. Paino teki työn, ja vesi lämpeni mitattavan verran. Kun koetta toistettiin eri painoilla ja pudotuskorkeuksilla, lämpeneminen oli aina verrannollinen tehtyyn työhön. Tämä kokeellinen tulos perustelee työn määritelmän, ja siksi työ ja lämpö mitataan samalla yksiköllä, joulella.
 
-Kun teet kappaleeseen työtä, energiaa siirtyy: nostetun kappaleen energia kasvaa, jousi venyy ja tallentaa energiaa, ja kitkaa vastaan tehty työ lämmittää pintoja. Energia ei katoa, vaan vaihtaa muotoa. Teho kertoo, kuinka nopeasti työ tehdään. Portaat ylös kävellen ja juosten teet saman työn, mutta juosten teho on suurempi. Kiukaan 6 kW teho tarkoittaa, että se muuttaa sähköenergiaa lämmöksi 6000 joulea joka sekunti.
+Kun teet kappaleeseen työtä, energiaa siirtyy: nostetun kappaleen energia kasvaa, jousi venyy ja tallentaa energiaa, ja kitkaa vastaan tehty työ lämmittää pintoja. Energia ei katoa, vaan vaihtaa muotoa. Teho kertoo, kuinka nopeasti työ tehdään. Portaat ylös kävellen ja juosten teet saman työn, mutta juosten teho on suurempi. Kiukaan 6 kW:n teho tarkoittaa, että se muuttaa sähköenergiaa lämmöksi 6000 joulea joka sekunti.
 
 ## Kaavat
 Kun vakiovoima on liikkeen suuntainen, voiman tekemä työ on voiman ja matkan tulo:
--- content/FY3/fy3-2/exercises.json	2026-10-24 14:49:52.068690561 +0000
+++ content/FY3/fy3-2/exercises.json	2026-10-24 14:49:52.085017043 +0000
@@ -27,7 +27,7 @@
     {
       "id": "fy3-2-L1-04",
       "level": 1,
-      "text": "Kelkkaa vedetään 6,0 m:n matka. Vetävä voima on koko matkan ajan 35 N ja liikkeen suuntainen, joten (s,F)-kuvaaja on vaakasuora jana. Laske voiman tekemä työ kuvaajan pinta-alana.",
+      "text": "Kelkkaa vedetään 6,0 m:n matka. Vetävä voima on koko matkalla 35 N ja liikkeen suuntainen, joten (s,F)-kuvaaja on vaakasuora jana. Laske voiman tekemä työ kuvaajan pinta-alana.",
       "answer": 210,
       "unit": "J",
       "tolerance": 0.02
@@ -35,7 +35,7 @@
     {
       "id": "fy3-2-L1-05",
       "level": 1,
-      "text": "Hiihtäjä vetää pulkkaa tasaisella 3,0 m/s:n nopeudella liikkeen suuntaisella 20 N:n voimalla. Mikä on vetovoiman teho?",
+      "text": "Hiihtäjä vetää pulkkaa tasaisella 3,0 m/s:n nopeudella liikkeen suuntaisella 20 N:n voimalla. Mikä on vetävän voiman teho?",
       "answer": 60,
       "unit": "W",
       "tolerance": 0.02
@@ -69,7 +69,7 @@
     {
       "id": "fy3-2-L2-04",
       "level": 2,
-      "text": "Vaunua työnnetään liikkeen suuntaisella voimalla. Voima on ensin 10 N matkan 0–2,0 m ajan. Sen jälkeen voima kasvaa tasaisesti 10 N:sta 30 N:iin matkalla 2,0–6,0 m. Laske voiman tekemä kokonaistyö (s,F)-kuvaajan pinta-alana.",
+      "text": "Vaunua työnnetään liikkeen suuntaisella voimalla. Voima on ensin 10 N matkalla 0–2,0 m. Sen jälkeen voima kasvaa tasaisesti 10 N:sta 30 N:iin matkalla 2,0–6,0 m. Laske voiman tekemä kokonaistyö (s,F)-kuvaajan pinta-alana.",
       "answer": 100,
       "unit": "J",
       "tolerance": 0.02
@@ -87,7 +87,7 @@
     {
       "id": "fy3-2-L3-02",
       "level": 3,
-      "text": "Joulen kokeessa 2,0 kg:n paino putoaa 1,5 m ja pyörittää siipipyörää vedessä. Koe toistetaan 20 kertaa nostamalla paino aina takaisin ylös. Oleta, että painon menettämä nostotyön suuruinen energia siirtyy kokonaan veden lämpömääräksi. Kuinka suuri lämpömäärä veteen on siirtynyt?",
+      "text": "Joulen kokeessa 2,0 kg:n paino putoaa 1,5 m ja pyörittää siipipyörää vedessä. Koe toistetaan 20 kertaa nostamalla paino aina takaisin ylös. Oleta, että painon menettämä energia siirtyy kokonaan veteen lämpönä. Kuinka suuri lämpömäärä veteen on siirtynyt?",
       "answer": 590,
       "unit": "J",
       "tolerance": 0.02
@@ -95,7 +95,7 @@
     {
       "id": "fy3-2-L3-03",
       "level": 3,
-      "text": "Mökin aurinkopaneeli antaa auringonpaisteessa 180 W:n tehon. Kuinka monta minuuttia paneelin pitää paistaa, jotta energia riittää nostamaan 1000 kg vettä 50 m:n korkeuteen? Oleta, että kaikki energia menee veden nostamiseen.",
+      "text": "Mökin aurinkopaneeli antaa auringonpaisteessa 180 W:n tehon. Kuinka monta minuuttia auringon pitää paistaa paneeliin, jotta energia riittää nostamaan 1000 kg vettä 50 m:n korkeuteen? Oleta, että kaikki energia menee veden nostamiseen.",
       "answer": 45,
       "unit": "min",
       "tolerance": 0.02
--- content/FY3/fy3-2/solutions.md	2026-10-24 14:49:52.068728707 +0000
+++ content/FY3/fy3-2/solutions.md	2026-10-24 14:49:52.085093849 +0000
@@ -12,7 +12,7 @@
 **Kaava:** W = G h
 **Sijoitus:** W = 150 N · 1,2 m = 180 J
 **Vastaus:** 180 J
-**Järkevyys:** Alle kahden sadan joulen työ vastaa suunnilleen 15 kg:n hyllyn nostamista reilun metrin.
+**Järkevyys:** Alle kahdensadan joulen työ vastaa suunnilleen 15 kg:n hyllyn nostamista reilun metrin korkeuteen.
 
 ## fy3-2-L1-03
 **Annettu:** W = 36 kJ = 36 000 J, t = 12 s
@@ -52,7 +52,7 @@
 **Kaava:** P = W / t, joten W = P t
 **Sijoitus:** W = 1500 W · 240 s = 360 000 J
 **Vastaus:** 360 kJ
-**Järkevyys:** Tällä työllä voisi nostaa 1000 kg:n vesimäärän noin 37 m:n korkeuteen. Neljä minuuttia pumppausta, uskottavaa.
+**Järkevyys:** Tällä työllä voisi nostaa 1000 kg:n vesimäärän noin 37 m:n korkeuteen. Neljän minuutin pumppaukselta tämä on uskottava tulos.
 
 ## fy3-2-L2-03
 **Annettu:** m = 850 kg, h = 30 m, g = 9,81 m/s²
@@ -60,7 +60,7 @@
 **Kaava:** G = m g ja W = G h
 **Sijoitus:** G = 850 kg · 9,81 m/s² = 8338,5 N; W = 8338,5 N · 30 m = 250 155 J
 **Vastaus:** 250 kJ
-**Järkevyys:** Elementti painaa yli 8 kN, ja 30 m on kymmenkerroksisen talon korkeus. Neljännesmegajoulen työ on uskottava.
+**Järkevyys:** Elementti painaa yli 8 kN, ja 30 m on kymmenkerroksisen talon korkeus. Työ on noin 0,25 MJ, ja se on nosturille uskottava.
 
 ## fy3-2-L2-04
 **Annettu:** F = 10 N matkalla 0–2,0 m; F kasvaa 10 N:sta 30 N:iin matkalla 2,0–6,0 m
@@ -71,7 +71,7 @@
 **Järkevyys:** Keskimääräinen voima on 100 J / 6,0 m ≈ 17 N, mikä on 10 N:n ja 30 N:n välissä.
 
 ## fy3-2-L3-01
-**Annettu:** voima nousee 0 → 40 N matkalla 0,50 m, pysyy 40 N matkalla 1,0 m ja laskee 40 N → 0 matkalla 0,50 m; kokonaismatka 2,0 m
+**Annettu:** voima nousee 0 → 40 N matkalla 0,50 m, pysyy 40 N:ssä matkalla 1,0 m ja laskee 40 N → 0 matkalla 0,50 m; kokonaismatka 2,0 m
 **Kysytty:** keskimääräinen voima F_ka
 **Kaava:** W = kuvaajan pinta-ala, W = F_ka s, joten F_ka = W / s
 **Sijoitus:** W = ½ · 40 N · 0,50 m + 40 N · 1,0 m + ½ · 40 N · 0,50 m = 10 J + 40 J + 10 J = 60 J; F_ka = 60 J / 2,0 m = 30 N
@@ -81,7 +81,7 @@
 ## fy3-2-L3-02
 **Annettu:** m = 2,0 kg, h = 1,5 m, 20 pudotusta, g = 9,81 m/s²
 **Kysytty:** veteen siirtynyt lämpömäärä Q
-**Kaava:** yhden pudotuksen työ W₁ = m g h; kaikki työ muuttuu lämpömääräksi, joten Q = 20 W₁
+**Kaava:** yhden pudotuksen työ W₁ = m g h; kaikki työ siirtyy veteen lämpönä, joten Q = 20 W₁
 **Sijoitus:** W₁ = 2,0 kg · 9,81 m/s² · 1,5 m = 29,43 J; Q = 20 · 29,43 J = 588,6 J
 **Vastaus:** 590 J
 **Järkevyys:** Alle 600 J on pieni energiamäärä, joten lämpötilan muutos oli pieni ja vaati tarkkaa mittausta. Siksi Joule toisti pudotuksia monta kertaa.
--- content/FY3/fy3-2/sim.js	2026-10-24 14:49:52.068854910 +0000
+++ content/FY3/fy3-2/sim.js	2026-10-24 14:49:52.085192175 +0000
@@ -27,7 +27,7 @@
     [sT, lT] = slider(controls, 1, 20, 5, 0.5);      // aika t (s)
     btn = p.createButton('Vedä').parent(controls);
     btn.mousePressed(() => { u = 0; running = true; });
-    p.createP('Laatikko liikkuu vakiovauhtia: kitka ottaa vastaan vetovoiman tekemän työn, ja energia muuttuu lämmöksi.')
+    p.createP('Laatikko liikkuu vakiovauhdilla: kitka ottaa vastaan vetävän voiman tekemän työn, ja energia muuttuu lämmöksi.')
       .parent('sim-root').class('note');
     p.textFont('Arial');
   };
```
