# Työjono

Opettajan päättämät tulevat työt, joita ei ole vielä aloitettu. Jokainen kohta tehdään omana pull requestinaan;
valmis kohta poistetaan tästä samassa pull requestissa.

Tämä on ainoa työjono (opettaja 2026-11-13): ei GitHub Issuesia eikä erillisiä listoja. Kohdat ovat
`docs/ROADMAP.md`:n järjestyksessä. Kohdan ottava ketju katsoo ensin avoimet pull requestit, merkitsee kohtaan
ensimmäisessä commitissaan `Varattu: <haara>` ja avaa luonnos-PR:n heti, jotta muut ketjut näkevät varauksen
(repon juuren `CLAUDE.md`). Saman kurssin kohdat tehdään peräkkäin, eri kurssien enintään kolme rinnakkain.

## 1. Main vihreäksi: en/fy1-1:n ratkaisueditori 360 px:ssä (2026-11-13)

`test_writepad.py` kaatuu mainissa #528:n jälkeen: sivu on 35 px näkymää leveämpi (395 px / 360 px), editori ja
painikkeet ovat kunnossa. Ei toistu paikallisesti. Ensin diagnostiikka (testi nimeää ylivuotavat elementit), sitten
pienin korjaus samaan PR:ään. Testiä ei löysätä.

## 2. Tehtäväsarjojen katselmoinnit: FY1, fy4-8, FY5, FY6, FY7 (opettaja 2026-11-13: tässä järjestyksessä)

Sarjat ovat luonnoksina eivätkä näy opiskelijoille (`python scripts/reviews.py status`): FY1 8, fy4-8 1, FY5 13,
FY6 15, FY7 14, kukin fi, en ja fi-easy. Katselmointi `/exercises`-putken vaiheilla (`reviews.py scope <id>
--exercises`, kolme katselmoijaa) kuten FY4:ssä (#531). Yksi kurssi per PR; kurssin MAFY-kaavat (kohta 3) samassa
ketjussa tai heti perään, ei rinnakkain.

## 3. Kaavat MAFY-muotoon FY5–FY8, FY10 ja FY14

FY1–FY4 ja FY9 on tehty (#501, #522, #527, #529). Keskinopeuden tunnus on kaikkialla $v_\text{k}$, ei $v_\text{ka}$
(opettaja 2026-11-13).

## 4. Ensimmäinen ulkoasukatselmointi: FY10:n tutkimukset ja TVT-ohjeet (2026-11-13)

36 osaa on sivustolla visual baselinen varassa (`python scripts/reviews.py baseline`): 27 tutkimusta ja 9 TVT-ohjetta.
`/quality-audit <id> --audit-only`, sitten `--fix`. Voi kulkea rinnakkain kohdan 2 kanssa.

## 5. CI:n toistettavuus (2026-11-13)

Tapa ajaa selaintarkistukset CI:n kontissa (`mcr.microsoft.com/playwright/python:v1.65.0-noble`) paikallisesti, ja
layout-testien virheilmoitukset nimeämään ylivuotava elementti (`docs/QUALITY.md` aukot 1–2). Jaettuja tiedostoja:
tehdään yksin ja yhdistetään ennen muita.

## 6. Kuva- ja MAFY-taulukkotehtävät FY8, FY9, FY10 ja FY14 (opettaja 2026-11-13)

Sama tahti kuin FY4:stä alkaen: jokaisessa luvussa vähintään kaksi kuvatehtävää ja MAFY-taulukkotehtävä noin joka
kolmannessa luvussa (#521, #528). Arvot vain `docs/mafy-arvot.tsv`:stä, uudet rivit lähde-URL:n kanssa. Aloitetaan,
kun kohdan 2 katselmoinnit on tehty, jotta katselmoimattomien sarjojen jono ei kasva.

## 7. Työpöytäasettelu: keskitetty tekstiraita ja marginaaliraita (opettaja 2026-11-13)

Isoin jäljellä oleva rakenteellinen UI-muutos. Työpöydällä lukupalsta keskitetään, ja sen viereen tulee
marginaaliraita (kuvat, kaavat, huomautukset). Jaettuja tiedostoja (`templates/`, `site.css`, `check_layout.py`):
tehdään yksin ja yhdistetään ennen muita. Ennen toteutusta vaiheittainen arvio ja vertailukuvat opettajalle
(CLAUDE.md "Where direction B goes": ei laajaa uudistusta yhdellä kertaa).

## 8. Virhekäsitys omana komponenttinaan (opettaja 2026-11-13)

Toistuva osa Teoria-vaiheeseen: väite yhdellä lauseella, sitten miksi se ei päde
(`docs/audits/2026-11-10-vaiheiden-kayttoliittyma.md` kohta 5.2). Komponentti kerran, sitten sisältötyö luku
kerrallaan: lukujen sisältö muuttuu, joten jokainen luku tarvitsee tiede-, pedagogiikka- ja ulkoasukatselmoinnin.

## Puute: englanninkieliset käsitekortit FY6 ja FY8 (opettaja 2026-11-13: tehdään myöhemmin)

`kortit/en/` ei sisällä tiedostoja `fy6.json` ja `fy8.json`, joten englanninkielisillä FY6- ja FY8-sivuilla ei ole
käsitekortteja eikä alleviivauksia.

## Kirjattu päätös: luvut ilman käsitekortteja (opettaja 2026-11-13)

Luvut fy3-13, fy3-14, fy3-16 ja fy4-16 jäävät ilman omia kortteja ja alleviivauksia (#526:n siirtojen jälkeen).
Kortteja ei lisätä niihin.
