VERDICT: FAIL
CONTENT-HASH: 109dbcc240d94859

## Blocking
1. lesson.md:53 — Lähteet-kappale sanoo bensiinistä "IPCC 2006: $44{,}3\,\text{MJ/kg}$, tyypillinen arvo pyöristettynä: $43$". 44,3 ei pyöristy lukuun 43; opiskelija voi tarkistaa ja huomaa virheen (taulukko ja kaikki tehtävät käyttävät 43). Kierroksen 2 selitys (kotimaisessa bensiinissä on etanolia) oli oikea ja poistui. Korjaus: palauta se, esim. "kotimaisessa bensiinissä on etanolia, joten taulukossa käytetään arvoa $43$", tai kirjoita "taulukon arvo $43$ on tyypillinen suomalaisen bensiinin arvo". Tieteellinen arvo on science-reviewerin; tässä virhe on opiskelijan nähtävissä.

## Polish
1. lesson.md:53 — Lähteet on yhä tiheä; yksityiskohdat suljetun laatikon taakse (kuten kierroksella 2).
2. inquiry.json (ennuste-2, rakenna) ja lesson.md (kuva 1, Yleinen virhekäsitys) — kierroksen 2 huomautukset 1, 2, 3 ja 5 ennallaan, eivät estä.

## Checked
- Diff: $\text{MJ/kg}$, $\text{kJ}$ ja $100\,\text{g}$ LaTeX-muotoon (exit-ticket, inquiry, taulukon otsikko) — johdonmukaista, ei muuta sisältöä.
- Taulukon otsikko $H\ (\text{MJ/kg})$ mahtuu 360 px:ään (layout-testit ok).
- lesson-answers.py: tark3 (170/430 MJ, suhde 2,5), 129 MJ ja lippu 75 MJ / 15 MJ/kg vastaavat tekstiä ja poistumislippua.
- Poistumislipun tehtävä (1500 kJ / 100 g) ja vastaus ennallaan ja seurattavissa.
- Polku, esimerkki, ennusteet ja palautteet kuten kierroksella 2 (PASS).
