VERDICT: PASS
CONTENT-HASH: 9e418b3b567bd336

## Blocking
(none)

## Polish
- inquiry.json johtopaatos model — "P2 ei kasvanut koko ajan" on epätarkka: kun R2 = 4, 8, 16 Ω, mallin P2 on 9,0, 8,0 ja 5,8 W eli pienenee, vaikka R2 > R1 (P2 > P1 pysyy). Kirjoita: "P2 pieneni, kun R2 kasvoi yli R1:n, koska yhteinen virta pieneni; silti P2 > P1." Hyvä ristiriita, nosta se esiin.
- inquiry.json koe-1 intro/measure — johtopäätöksen kriteeri 4 (tehot yhteensä lähteen teho) koskee molempia kytkentöjä, mutta vain koe-2 pyytää laskemaan P1 + P2 ja mittaa P:n; lisää koe-1:een "Laske P1 + P2" ja P mittauksiin.
- inquiry.json koe-1/koe-2 — ennuste kysyy, kumpi lasi lämpenee nopeammin, mutta taulukko kirjaa vain tehoja; lisää "kirjaa myös lämpötilat hetkellä t" tai sano, että tehojen suhde ratkaisee lämpenemisen.
- lesson.md "Vastuksen lämpeneminen tasaantuu" — oppimistavoite luetaan, ei tutkita (sim ei mallinna häviöitä, mikä sanotaan); hyväksyttävä yhden tunnin työmäärässä.

## Checked
- Polku: P = UI johdetaan J/C ja C/s, sitten Joulen laki, sarja/rinnan, paahdin; alun kysymykseen vastataan (Paahdin ja sen johto, tarkistus-3); luvut 59 Ω, 3,9 A, 0,8 W, 1200 oikein.
- Ennusteet 1 ja 2 ennen todisteita; väärien vaihtoehtojen palaute korjaa virhekäsityksen, koe voi kumota ennusteen (R2 = 4/8/16 Ω); U, R1 ja kytkentä lukittu.
- Mallin arvot erotettu mittauksista (sim-malli ja johtopäätöksen mallivastaus).
- Kuvat (hero, energia, jako, lampo, graafi) tunnistettavia ja luettavia 390 px:llä, värit eivät ainoa koodaus; kuvaukset antavat saman tiedon.
- Esimerkki porrastettu seitsemään vaiheeseen, ei hyppyjä; ei toista harjoituksia.
- Etsi virhe paljastaa virheen energian säilymisellä; siirto (37 min) kolmella vihjeellä ja todellisilla virheillä (2235, 77,6, 447 tarkistettu).
- Tarkista: käsite (40/100 W lamput), laskenta, selitys kriteereineen; lähtölippu (5,0 A, nelinkertainen) testaa ydinideaa.
- Suomi ja sijamuodot ($12\,\text{V}$:n, $5{,}0\,\text{min}$:ssa) kunnossa; puhelinnäkymä: ohjaimet ja lukema mahtuvat 390 px:ssä.
- Työmäärä: ydinpolku noin yksi tunti; valinnaiset kertaus, pohdi ja tarkistus-3 pois ydinpolulta.
