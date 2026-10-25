VERDICT: PASS
CONTENT-HASH: 01702f620343cee1
## Blocking
(none)
## Polish
- lesson.md:6,46,50 — straight quotes " " — use Finnish ”…” (in diff)
- lesson.md:6 — "sisällä lämpöä, vaan energiaa" — "sisäenergiaa", the lesson's own term (in diff)
- lesson.md:46 — "kuuma kipinä on tuhansia asteita" — "kuuman kipinän lämpötila on …" (in diff)
- lesson.md:49 — "vuorovaikutusenergian" is not a glossary term — match the definition in Ydinajatus (in diff)
- solutions.md:11 — "−8,4 kJ + 0" — unit on the zero (in diff)
## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -3,7 +3,7 @@
 > **Miksi** polkupyörän pumppu kuumenee, kun rengasta pumpataan, vaikka pumppua ei lämmitetä millään?
 
 ## Ydinajatus
-Edellisillä oppitunneilla työ todettiin tavaksi siirtää energiaa, ja Joulen koe näytti, että mekaaninen työ voi lämmittää vettä. Vesi ei kuitenkaan sisällä "lämpöä", vaan energiaa. Systeemin sisäenergia U on sen hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Mikromallin mukaan lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, joten kun kaasun tai nesteen lämpötila nousee, sen sisäenergia kasvaa. Sisäenergia riippuu myös aineen määrästä: iso järvi sisältää paljon enemmän sisäenergiaa kuin kuppi kuumaa teetä, vaikka järvi on kylmempi.
+Edellisillä oppitunneilla työ todettiin tavaksi siirtää energiaa, ja Joulen koe näytti, että mekaaninen työ voi lämmittää vettä. Vesi ei kuitenkaan sisällä ”lämpöä”, vaan sisäenergiaa. Systeemin sisäenergia U on sen hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Mikromallin mukaan lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, joten kun kaasun tai nesteen lämpötila nousee, sen sisäenergia kasvaa. Sisäenergia riippuu myös aineen määrästä: iso järvi sisältää paljon enemmän sisäenergiaa kuin kuppi kuumaa teetä, vaikka järvi on kylmempi.
 
 Systeemin sisäenergiaa voi muuttaa kahdella tavalla. Ensimmäinen on työ: kun pumpun mäntä puristaa ilmaa, ympäristö tekee kaasuun työtä, ja kaasun sisäenergia kasvaa. Siksi pumppu kuumenee. Toinen on lämpö: kun kaksi eri lämpötilassa olevaa kappaletta koskettavat, energiaa siirtyy itsestään kuumemmasta kylmempään, kunnes lämpötilat ovat samat. Näin siirtynyttä energiaa sanotaan lämmöksi, ja siirtyneen energian määrä on lämpömäärä Q. Lämpö on siis energian siirtymistä, ei aineen ominaisuus: kappaleella on lämpötila ja sisäenergia, mutta ei lämpöä.
 
@@ -43,10 +43,10 @@
 Ilman sisäenergia kasvaa 110 J, joten sen lämpötila nousee. Jos puristus tehtäisiin niin hitaasti, että kaikki työn tuoma energia ehtisi siirtyä lämpönä pois, olisi Q = −150 J ja ΔU = 0, eikä lämpötila muuttuisi.
 
 ## Yleinen virhekäsitys
-Arkikielessä sanotaan, että kappaleessa "on lämpöä" tai että lämpö "varastoituu". Fysiikassa lämpö on energian siirtymistä lämpötilaeron vuoksi, ja se, mikä kappaleeseen varastoituu, on sisäenergiaa. Toinen virhe on pitää lämpötilaa ja sisäenergiaa samana asiana: kuuma kipinä on tuhansia asteita, mutta sen sisäenergia on pieni, koska siinä on vähän ainetta. Kolmas virhe on ajatella, että sisäenergiaa voi muuttaa vain lämmittämällä. Pumpun ilma kuumenee ilman mitään lämmönlähdettä, koska siihen tehdään työtä.
+Arkikielessä sanotaan, että kappaleessa ”on lämpöä” tai että lämpö ”varastoituu”. Fysiikassa lämpö on energian siirtymistä lämpötilaeron vuoksi, ja se, mikä kappaleeseen varastoituu, on sisäenergiaa. Toinen virhe on pitää lämpötilaa ja sisäenergiaa samana asiana: kuuman kipinän lämpötila on tuhansia asteita, mutta sen sisäenergia on pieni, koska siinä on vähän ainetta. Kolmas virhe on ajatella, että sisäenergiaa voi muuttaa vain lämmittämällä. Pumpun ilma kuumenee ilman mitään lämmönlähdettä, koska siihen tehdään työtä.
 
 ## Tiivistelmä
-- Sisäenergia U on systeemin hiukkasten liike-energian ja vuorovaikutusenergian summa. Se kasvaa, kun lämpötila nousee, ja riippuu myös aineen määrästä.
-- Lämpö on energian siirtymistä kuumemmasta kylmempään lämpötilaeron vuoksi; siirtynyt energia on lämpömäärä Q. Kappaleella ei "ole lämpöä".
+- Sisäenergia U on systeemin hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Se kasvaa, kun lämpötila nousee, ja riippuu myös aineen määrästä.
+- Lämpö on energian siirtymistä kuumemmasta kylmempään lämpötilaeron vuoksi; siirtynyt energia on lämpömäärä Q. Kappaleella ei ”ole lämpöä”.
 - Sisäenergiaa muuttavat lämpö ja työ: $\Delta U = Q + W$. Sisään siirtyvä energia on positiivista, ulos siirtyvä negatiivista.
 - Energia säilyy: tämä on termodynamiikan ensimmäinen pääsääntö. Eristetyn systeemin sisäenergia pysyy vakiona.
--- a/solutions.md
+++ b/solutions.md
@@ -10,7 +10,7 @@
 **Annettu:** systeemi on kahvi; Q = −8,4 kJ (lämpöä siirtyy kahvista pois), W = 0
 **Kysytty:** ΔU
 **Kaava:** ΔU = Q + W
-**Sijoitus:** ΔU = −8,4 kJ + 0 = −8,4 kJ
+**Sijoitus:** ΔU = −8,4 kJ + 0 kJ = −8,4 kJ
 **Vastaus:** −8,4 kJ
 **Järkevyys:** Sisäenergia pienenee, joten kahvin lämpötila laskee. Energia ei katoa, vaan sama 8,4 kJ siirtyy pöytään ja huoneen ilmaan.
 
```
## Checked
- Lint: 0 errors, 0 warnings, not repeated
- Glossary terms (sisäenergia, lämpö, lämpömäärä, systeemi, työ, termodynamiikan ensimmäinen pääsääntö) used consistently; lämpö vs lämpömäärä correct
- Unit inflection (0,20 m:n, 300 N:n, 2,0 kW:n, 250 W:n, 5,0 kg:n, 0,15 m:n) correct in exercises
- Case endings and partitive/illative in all 12 exercise texts, solutions.md and exit-ticket.json fine
- Decimal comma and minus sign (−) in Finnish text; decimal point only in JSON
- Sign convention ΔU = Q + W stated consistently, in text, exercises, solutions and exit ticket
- Reading level suits 16–19-year-olds; sentences short enough
- exit-ticket.json already uses ”…” quotes
- Diff dry-run applied cleanly with patch -p1; no numbers, LaTeX or JSON touched
