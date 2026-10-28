# Concept reports: internal-energy, temperature, phase-change (fi), science reviewer 2026-10-28

## internal-energy
1. content/fi/FY3/fy3-15/inquiry.json (tyypit.question.choices[0].feedback; johtopaatos.model) — "häviöt tulevat vain kitkasta ja sähköisistä häviöistä" vs choices[3].feedback "kitkaa ja virtaushäviöitä" — fix: "häviöt tulevat vain kitkasta, virtaushäviöistä ja sähköisistä häviöistä" (johtopaatos likewise).
2. content/fi/FY3/fy3-3/lesson.md (line ~222) — "vaikka vedessä on enemmän energiaa" drops equal mass — fix: "vaikka samamassaisessa vedessä on enemmän sisäenergiaa kuin jäässä".
3. content/fi/FY2/fy2-7/inquiry.json (tarkistus-1.choices[3].feedback) — "sen lämpö siirtyy" — fix: "Vesi pysyy putkessa, mutta siitä siirtyy energiaa lämpönä putken seinän ja eristeen läpi ympäristöön."
4. content/fi/FY2/fy2-1/exercises/exercises.json (fy2-1-L2-04.text), solutions.md (~line 92) — "siirtyy veteen lämpöenergiana" — fix: "… siirtyy veteen lämpönä, ja loppu lämmittää keitintä ja ympäristöä." / "veteen lämpönä siirtyvä energia $E_\text{vesi} = 331\,\text{kJ}$".
5. content/fi/FY3/fy3-11/exercises/exercises.json (fy3-11-L3-02.text), solutions.md (~line 146) — "muuttavat kaiken sähkön lämmöksi" — fix: "sähkövastukset muuttavat käytännössä kaiken sähköenergian sisäenergiaksi, joka siirtyy lämpönä huoneeseen".
6. content/fi/FY3/fy3-15/exercises/solutions.md (~line 157) — "muuttaisi sähkön lämmöksi" — fix: "muuttaisi sähköenergian vastuksen sisäenergiaksi, joka siirtyy lämpönä huoneeseen" (but see efficiency/fuel report: also say the heat pump delivers outdoor heat PLUS the electricity used).
7. content/fi/FY3/fy3-15/lesson.md (~line 107) — "jossa sen lämpötila on niin matala" (energy given a temperature) — fix: "se siirtyy lämpönä mereen tai ilmaan, jonka lämpötila on niin lähellä ympäristön lämpötilaa, ettei siitä voi enää saada työtä eikä sähköä."
8. content/fi/FY3/fy3-15/exercises/solutions.md (~line 26) — "loput häviää kitkaan ja sähköhäviöihin" — fix: "loput muuttuu kitkassa ja sähköisissä häviöissä sisäenergiaksi, joka siirtyy lämpönä ympäristöön."

## temperature
9. content/fi/FY3/fy3-8/inquiry.json (olomuodot.question.choices[0] text and feedback, choices[1–2].feedback) — "vahvojen sidosten pitäminä, nesteen sidokset ovat heikompia" calls the forces between particles bonds; fy3-7 says "vuorovaikutukset" — fix: "Kiinteän aineen hiukkaset värähtelevät tasapainoasemiensa ympärillä naapuriensa vetovoimien pitäminä, nesteen hiukkaset pysyvät yhdessä mutta liikkuvat toistensa ohi, ja kaasun hiukkaset liikkuvat lähes vapaasti." (use "vuorovaikutukset" for "sidokset" in the option and the other feedback; keep exactly one correct option).
10. content/fi/FY3/fy3-12/lesson.md (line ~6) — conduction only as vibrating particles — fix: add "Metalleissa energiaa kuljettavat lisäksi ja pääosin vapaat elektronit."

## phase-change
11. content/fi/FY3/fy3-14/inquiry.json (ennuste-1.choices[2].feedback) — "Kun veden lämpötila ylittää 26,6 °C, kaikki jää sulaa" vs "≥" — fix: "Kun veden lämpötila on vähintään 26,6 °C, kaikki jää sulaa; tasan 26,6 °C:ssa lopputila on 0 °C."
12. content/fi/FY3/fy3-14/lesson.md (~line 101) — "Lopputilanteita on kolme" vs sim howto (four), line ~274 and L3-03 (−3,5 °C) — fix: "Lopputilanteita on neljä." and add: "Jos jää on hyvin kylmää ja vettä on vähän, osa vedestä tai kaikki vesi jäätyy; vasta kun kaikki vesi on jäätynyt, lämpötila on alle 0 °C."
13. content/fi/FY3/fy3-3/inquiry.json (prior[0]) and exercises/solutions.md (~line 22) — "kiehuu 100 °C:ssa" / "kiehumispiste on 373 K" without pressure — fix: "… kiehuu 100 °C:ssa normaalipaineessa" / "Veden kiehumispiste normaalipaineessa on 373 K".
14. content/fi/FY3/fy3-16/lesson.md (~line 199, step 4) — only the "ei riitä" branch — fix: "Jos se ei riitä, muutos jää kesken ja lämpötila on sulamispiste. Jos se riittää juuri ja juuri, muutos ehtii loppuun ja lämpötila on tasan sulamispiste."
15. content/fi/FY3/fy3-14/inquiry.json (simulaatio.howto) — "vesi ei riitä sulattamaan kaikkea jäätä" lacks the temperature — fix: "… ja seos on 0 °C:ssa".
16. content/fi/FY3/fy3-14/lesson.md (~lines 101, 168) — "veden lämpö riittää" gives water heat — fix: "Jos vesi voi jäähtyessään luovuttaa tarpeeksi lämpöä kaiken jään sulattamiseen" / "kunnes veden luovuttama lämpö riittää sulattamaan jään".
17. content/fi/FY3/fy3-16/exercises/solutions.md (~line 42) — "rikkoo jään rakenteen" — fix: "muuttaa hiukkasten keskinäisiä vuorovaikutuksia: jään säännöllinen järjestys purkautuu ja hiukkasten välinen vuorovaikutusenergia kasvaa".
