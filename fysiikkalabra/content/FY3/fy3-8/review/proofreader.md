VERDICT: PASS
CONTENT-HASH: 24391ddb179146fb

## Blocking
(none)

## Polish
- lesson.md:6 — "kauemmas poispäin naapuristaan" is redundant — "kauemmas naapuristaan".
- lesson.md:12 — "sitä tarkastellaan oppitunnilla fy3-9" can read as referring to the pressure or the gas volume ambiguously — "siihen palataan oppitunnilla fy3-9".
- lesson.md:70 — the quoted fragment ”reiän sisäänpäin” is hard to parse for a 16-year-old — "koska levy muka laajenee reunoiltaan reiän puolelle".
- exercises.json:L2-04 — "kaikki · 10⁻⁶ 1/K" reads like a product — "kaikki yksikössä 10⁻⁶ 1/K".

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -3,13 +3,13 @@
 > **Miksi** pitkän sillan päässä on kampamainen teräsliitos, jonka yli auton renkaat kolahtavat?
 
 ## Ydinajatus
-Lähes kaikki aineet laajenevat lämmetessään ja kutistuvat jäähtyessään. Ilmiötä sanotaan lämpölaajenemiseksi. Mikromalli selittää sen. Kiinteässä aineessa hiukkaset värähtelevät tasapainoasemiensa ympärillä. Kun lämpötila nousee, värähtely voimistuu. Hiukkasten on helpompi loitota toisistaan kuin puristua lähemmäs toisiaan: lähekkäin puristuvat hiukkaset hylkivät toisiaan voimakkaasti, mutta loittonevien hiukkasten välinen veto heikkenee vähitellen. Siksi hiukkanen heilahtaa kauemmas poispäin naapuristaan kuin lähemmäs sitä, ja voimakkaammin värähtelevien hiukkasten keskimääräinen etäisyys kasvaa. Kun kaikki hiukkasvälit kasvavat, koko kappale laajenee.
+Lähes kaikki aineet laajenevat lämmetessään ja kutistuvat jäähtyessään. Ilmiötä sanotaan lämpölaajenemiseksi. Mikromalli selittää sen. Kiinteässä aineessa hiukkaset värähtelevät tasapainoasemiensa ympärillä. Kun lämpötila nousee, värähtely voimistuu. Hiukkasten on helpompi loitota toisistaan kuin puristua lähemmäs toisiaan: lähekkäin puristuvat hiukkaset hylkivät toisiaan voimakkaasti, mutta loittonevien hiukkasten välinen veto heikkenee vähitellen. Siksi hiukkanen heilahtaa kauemmas naapuristaan kuin lähemmäs sitä, ja voimakkaammin värähtelevien hiukkasten keskimääräinen etäisyys kasvaa. Kun kaikki hiukkasvälit kasvavat, koko kappale laajenee.
 
 Muutos on pieni mutta voimakas. Teräksinen sauva pitenee vain noin sadastuhannesosan pituudestaan jokaista kelviniä kohti, mutta jos sauvan päät on kiinnitetty, laajeneva teräs työntää niitä valtavalla voimalla. Siksi pitkissä rakenteissa on liikuntasaumoja. Sillan teräskansi on talvipakkasella lyhyempi kuin kesähelteellä, ja kampamainen liitos sillan päässä antaa kannen liikkua vapaasti. Samasta syystä sähkölinjat roikkuvat helteellä alempana kuin pakkasella.
 
 Kappale laajenee kaikkiin suuntiin samassa suhteessa kuin valokuvaa suurennettaessa. Myös reikä levyssä suurenee, kun levy lämpenee. Tätä käytetään kutistusliitoksessa: kuumennettu teräsrengas pujotetaan akselille, ja jäähtyessään se puristuu tiukasti kiinni. Eri aineet laajenevat eri tavalla. Kaksoismetalliliuska, jossa kaksi eri metallia on liitetty toisiinsa, taipuu lämmetessään, koska toinen metalli pitenee enemmän. Sellainen liuska avaa ja sulkee virtapiirin vanhanmallisissa termostaateissa.
 
-Nesteet laajenevat yleensä selvästi enemmän kuin kiinteät aineet, ja kaasut vielä paljon enemmän. Nesteen hiukkaset eivät pysy paikoillaan, ja niiden väliset sidokset ovat heikompia kuin kiinteässä aineessa, joten lämpötilan nousu loitontaa niitä toisistaan enemmän. Kaasun hiukkaset ovat kaukana toisistaan ja lähes vapaita, joten vakiopaineessa kaasun tilavuus kasvaa paljon enemmän. Kaasun tilavuus riippuu myös paineesta, ja sitä tarkastellaan oppitunnilla fy3-9. Nestelämpömittari perustuu nesteen laajenemiseen: kun lämpötila nousee, nestepatsas kohoaa ohuessa putkessa. Vesi on poikkeus: 0 °C:n ja 4 °C:n välillä se kutistuu lämmetessään, joten sen tiheys on suurin noin 4 °C:ssa. Tihein, 4-asteinen vesi painuu pohjalle, ja kylmempi vesi jää pinnalle ja jäätyy. Siksi järvi jäätyy pinnalta alkaen, ja pohjalla on talvellakin noin 4-asteista vettä, jossa kalat selviävät.
+Nesteet laajenevat yleensä selvästi enemmän kuin kiinteät aineet, ja kaasut vielä paljon enemmän. Nesteen hiukkaset eivät pysy paikoillaan, ja niiden väliset sidokset ovat heikompia kuin kiinteässä aineessa, joten lämpötilan nousu loitontaa niitä toisistaan enemmän. Kaasun hiukkaset ovat kaukana toisistaan ja lähes vapaita, joten vakiopaineessa kaasun tilavuus kasvaa paljon enemmän. Kaasun tilavuus riippuu myös paineesta, ja siihen palataan oppitunnilla fy3-9. Nestelämpömittari perustuu nesteen laajenemiseen: kun lämpötila nousee, nestepatsas kohoaa ohuessa putkessa. Vesi on poikkeus: 0 °C:n ja 4 °C:n välillä se kutistuu lämmetessään, joten sen tiheys on suurin noin 4 °C:ssa. Tihein, 4-asteinen vesi painuu pohjalle, ja kylmempi vesi jää pinnalle ja jäätyy. Siksi järvi jäätyy pinnalta alkaen, ja pohjalla on talvellakin noin 4-asteista vettä, jossa kalat selviävät.
 
 ## Kaava
 Kun kappaleen lämpötila muuttuu ΔT, sen pituus muuttuu
@@ -67,7 +67,7 @@
 Kansi pitenee kesään mennessä lähes yhdeksän senttimetriä. Se on vain 0,07 % kannen pituudesta, mutta ilman liikuntasaumaa laajeneva teräs työntäisi sillan päitä niin suurella voimalla, että rakenteet vaurioituisivat. Siksi sillan päässä on kampamainen liitos, jonka hampaat liukuvat toistensa lomassa.
 
 ## Yleinen virhekäsitys
-Moni ajattelee, että lämmetessä hiukkaset itse kasvavat. Mikromallissa hiukkaset pysyvät samankokoisina, ja vain niiden keskimääräiset etäisyydet kasvavat. Toinen virhe on luulla, että levyn reikä pienenee, kun levy laajenee ”reiän sisäänpäin”. Reikä suurenee samassa suhteessa kuin levy muutenkin. Kolmas virhe on olettaa, että kaikki aineet laajenevat aina lämmetessään: vesi kutistuu 0 °C:n ja 4 °C:n välillä, ja jäätyessään se laajenee. Siksi jää kelluu ja järvet jäätyvät pinnalta.
+Moni ajattelee, että lämmetessä hiukkaset itse kasvavat. Mikromallissa hiukkaset pysyvät samankokoisina, ja vain niiden keskimääräiset etäisyydet kasvavat. Toinen virhe on luulla, että levyn reikä pienenee, koska levy muka laajenee reunoiltaan reiän puolelle. Reikä suurenee samassa suhteessa kuin levy muutenkin. Kolmas virhe on olettaa, että kaikki aineet laajenevat aina lämmetessään: vesi kutistuu 0 °C:n ja 4 °C:n välillä, ja jäätyessään se laajenee. Siksi jää kelluu ja järvet jäätyvät pinnalta.
 
 ## Tiivistelmä
 - Lämmetessä hiukkasten värähtely voimistuu ja niiden keskimääräinen etäisyys kasvaa, joten aine laajenee.
--- a/exercises.json
+++ b/exercises.json
@@ -69,7 +69,7 @@
     {
       "id": "fy3-8-L2-04",
       "level": 2,
-      "text": "Kerrostalon julkisivussa on 3,00 m pitkä metallinen lista. Aamulla listan lämpötila on 12 °C, ja iltapäivällä aurinko on lämmittänyt sen 42 °C:seen. Mittausten mukaan lista on pidentynyt 2,07 mm. Laske listan pituuden lämpötilakerroin α yksikössä 10⁻⁶ 1/K ja päättele oppitunnin taulukosta, mistä metallista lista on tehty (teräs 12, alumiini 23, kupari 17, kaikki · 10⁻⁶ 1/K).",
+      "text": "Kerrostalon julkisivussa on 3,00 m pitkä metallinen lista. Aamulla listan lämpötila on 12 °C, ja iltapäivällä aurinko on lämmittänyt sen 42 °C:seen. Mittausten mukaan lista on pidentynyt 2,07 mm. Laske listan pituuden lämpötilakerroin α yksikössä 10⁻⁶ 1/K ja päättele oppitunnin taulukosta, mistä metallista lista on tehty (teräs 12, alumiini 23, kupari 17, kaikki yksikössä 10⁻⁶ 1/K).",
       "answer": 23,
       "unit": "10⁻⁶ 1/K",
       "tolerance": 0.02
```

## Checked
- Lint 0 errors, 0 warnings; hash taken at start and end of review is identical.
- Round-1 additions in lesson.md (lines 6, 12, 19, 25: why particles move apart, liquids and gases, meaning of α, 4-degree water, γ ≈ 3α): grammar, cases, terminology OK.
- Worked example (lesson.md:58-67), split aligned rows and the 0,07 % claim: language OK.
- L1-03 (dial gauge, "mittakello", "jäävedellä", "pitenee eli ... lukema muuttuu") and its solution: OK.
- L1-05 "9,0 · 10⁻⁶ 1/K" and L2-04 unit "10⁻⁶ 1/K": decimal comma, spaces, case endings OK.
- solutions.md L1-04 (γ at 20 °C), L2-03 (ΔL/2, both neighbouring rails), L2-04: wording and case endings OK.
- exit-ticket.json Q3 (micro model, "Eivät ... Hiukkaset pysyvät samankokoisina"): consistent with lesson and glossary.
- Terms match glossary.json (lämpölaajeneminen, pituuden/tilavuuden lämpötilakerroin, kelvin); no hyphen minus, no decimal points in text.
- sim.js Finnish strings (buttons, note, readout labels, canvas text) and sim-spec.md: unchanged in wording, OK.
