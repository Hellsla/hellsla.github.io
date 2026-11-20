VERDICT: PASS
CONTENT-HASH: 3f85c11d16edeafb

## Blocking

## Polish

## Checked
- Pysähdy 1 (Ydinajatus, rivi 141): narun jokainen kohta värähtelee lähteen taajuudella $2{,}0\,\text{Hz}$, kun aalto on saavuttanut sen; vastaus mainitsee viiveen, joten "kohta liikkuu myöhemmin, mutta taajuus ei muutu" on oikea kuva (ideaalinen naru, vakiotila). Vastattavissa juuri luetusta kappaleesta ("narun jokainen kohta värähtelee samalla taajuudella $f$ kuin käsi").
- Pysähdy 2 (tyyppikuvan jälkeen, rivi 358): kierrokset värähtelevät etenemissuunnan suuntaisesti, aalto pitkittäinen, kierros heilahtelee paikallaan: sama kuin teoria ja sanasto. Sijoitettu heti kappaleen ja sen kuvan jälkeen.
- Pysähdy 3 (rivi 415): $v = \lambda/T = 0{,}50\,\text{m}/0{,}25\,\text{s} = 2{,}0\,\text{m/s}$ laskettu uudelleen omalla skriptillä (myös $f\lambda$ = $4{,}0\,\text{Hz}\cdot0{,}50\,\text{m}$); symbolinen muoto ensin, yksikkö ja kaksi merkitsevää numeroa oikein, kaava on juuri edellä esitetty.
- Ei paljasta myöhempää: Ennusta-kohdat (ennuste-1 kohdan P liike, ennuste-2) tulevat sivulla ennen teoriaa; tarkistus-1 (taajuus säilyy rajapinnassa), tarkistus-3 (ilmamolekyyli) ja tarkistus-2/siirto käyttävät eri tilanteita ja lukuja, ja teoria toteaa ne joka tapauksessa.
- Ei ristiriitaa luvun muun sisällön kanssa; laajuus FY5-paikan mukainen.
- Renderöinti: build ja layout 360/390/768/1280 px läpi (deterministiset tarkistukset); sisältö-hash sama alussa ja lopussa.

## Vanhan sisällön löydökset
- inquiry.json koe-2/koe-3: λ-lukema lasketaan sim.js:ssä `v / f`, joten "fλ = v joka rivillä" toteutuu rakenteeltaan; vertailu viivoittimeen olisi itsenäinen näyttö (Polish aiemmin).
- lesson-answers.py:1295: kommentti mainitsee "440 Hz", jota luku ei käytä.
