# Kuvituksen auditointi: yhteenveto

Tila 2026-11-11: **kesken**. Tämä on arvio ja ehdotus; yhtään kuvaa, `figures.py`-tiedostoa tai yhteistä työkalua ei
ole muutettu. Jokaisen kuvan kohdalla opettajan päätös on ODOTTAA.

## Mistä mikäkin löytyy

- Arviointiluettelot kursseittain: [FY1](FY1.md), [FY2](FY2.md), [FY3](FY3.md), [FY4](FY4.md), [FY5](FY5.md),
  [FY6](FY6.md), [FY7](FY7.md), [FY8](FY8.md). Lukumäärät: [COUNTS.md](COUNTS.md).
- Kuvakatalogi: `catalog/<KURSSI>.html`. Avaa tiedosto selaimessa repositorion paikallisesta kopiosta (se lukee
  tyylit ja KaTeXin hakemistosta `site/`). Painikkeet: kaikki, uudelleen piirrettävät ja korvattavat ensin, vain
  muutosehdotukset, puhelinleveys 360 px.
- Tärkeimmät ehdotukset: [PRIORITY.md](PRIORITY.md).
- Päätökset: kirjoita kuvan tunniste ja päätös, tai täytä rivin viimeinen sarake tiedostossa `data/<KURSSI>.tsv`.
  `python docs/illustration-audit/build.py` tuottaa luettelot ja katalogit uudelleen.

## Laajuus

Piirrettyjä opetuskuvia on kuvaluettelossa (`docs/figures/catalog.json`) 896 kursseissa FY1–FY8. Valokuvia (147) ei
auditoida. Luettelon ulkopuolella on lisäksi noin 290 piirrettyä kuvaa: kokeelliset tutkimukset (FY10, noin 105),
FY9:n kertausyksiköt (noin 55), FY14 (noin 70), yksiköiden soveltavat tehtävät (noin 34), TVT-ohjeet (10) ja
Ahjo-sivut (10).

| Kohde | Tila |
|---|---|
| FY1, FY2, FY3, FY4 | Kaikki kuvat katsottu renderöityinä ja arvioitu (366 kuvaa) |
| FY5–FY8 | Avauskuvat arvioitu (65 kuvaa). Kaaviot, kuvaajat ja tehtäväkuvat arvioimatta (465 kuvaa) |
| FY9, FY10, FY14, TVT, Ahjo | Arvioimatta (noin 290 kuvaa) |

Kuvat on katsottu noin 500 px:n levyisinä sivuston tyyleillä ja KaTeX-merkinnöillä; epäilyttävät kuvat lisäksi
suurempina. Erillistä 360 px:n tarkistusta ei ole tehty kuva kuvalta: katalogin puhelinleveys-painike on sitä varten.

## Havainto ohjeista

`scripts/figstyle.py` ja kahdeksan FY1:n `figures.py`-tiedostoa viittaavat tiedostoon `docs/illustration-style.md`,
jota ei ole repositoriossa. Talotyyli on nyt kirjattu vain `figstyle.py`:n alkukommenttiin ja NOTES.md:n lukuun 3.
Arvio nojaa niihin ja FY1:n kuviin.

## Tulos tähän asti (431 arvioitua kuvaa)

Pidä 306, kevyt korjaus 120, piirrä uudelleen 3, korvaa uudella 2, fysiikan virhe 0.

Fysiikan virheitä ei löytynyt. Mittakaavassa olevat kuvat ovat mittakaavassa (tarkistettu laskemalla mm.
fy1-6/free-fall, fy1-7/graph, fy2-2/tikapuut, fy3-1/weight-mass, fy3-3/kelvin-scale, fy4-9/liikemaara, fy4-11/tF),
voimakuvioiden pituudet vastaavat kiihtyvyyksiä ja komponentit on piirretty katkoviivalla.

## Vahvuudet

1. Kuva kantaa fysiikan, ei vain kuvita sitä: fy1-3/hero (kymmenen kelloa, eri lukemat), fy3-1/scene (sama punnus
   Maassa ja Kuussa), fy4-2/strobe, fy4-10/tarra.
2. Tilannekuva ja siitä erotettu voimakuvio rinnakkain koko FY4:n läpi (malli: fy4-11/jarrutus, fy4-16/esimerkki).
3. Laitteet piirretään laitteina: fy1-6/light-gates, fy3-2/joule, fy3-13/~lesson-2, fy4-15/vesivoimala.
4. Kuvat sanovat itse, ovatko ne mittakaavassa vai kaavamaisia.
5. Väri ei kanna tietoa yksin: rasterit, hakasulkeet ja nimet toistavat sen.

## Yleisimmät ongelmat

1. **Sama asia piirretään eri luvuissa eri tavalla.** Energiavirtakaaviot neljällä tavalla (fy2-2, fy2-4, fy2-7,
   fy3-15), voimanuolen väri FY3:ssa kolmella tavalla (punainen, oranssi, musta), ilmanvastus kahdella tavalla
   (fy4-3 ja fy4-14), hissin matkustaja kolmella, Aurinko kahdella (sädekehä 16 kuvassa, talotyylin kiekko muissa),
   kasvihuoneilmiö kahdella (fy2-8, fy3-12).
2. **Tekstit törmäävät.** Merkintä toisen merkinnän, viivan tai kuvan reunan päällä noin 30 kuvassa. Korkeissa
   kuvaajissa akselin nimi ulottuu kuva-alan yläreunan yli (yhteinen syy, yksi korjaus).
3. **Soveltavien tehtävien ja kokeiden kuvaajat** on piirretty eri tyylillä kuin lukujen kuvaajat (musta data,
   paksummat akselit, yksiköt pystymurtoina).
4. **Vanhaa paksua viivatyyliä** on vastausvaihtoehtokuvissa (fy3-1/pick-*, fy4-5/hissi-*), ja FY3:n lopun kuvat
   (luvut 13–16) on upotettu käsin tekstiin eikä piirretty `figures.py`:ssä, joten talotyyli ei ulotu niihin.
5. **Avauskuvien aiheet toistuvat.** Voimalaitosmaisema kahdeksassa kuvassa, leivänpaahdin kolmessa FY6:n kuvassa,
   Aurinko ja luotain kahdessa FY1:n kuvassa.

## Viisi periaatetta jatkoon

1. Yksi esitystapa per asia koko sarjassa: päätä malli (energiavirta: fy2-4/lamp; voimakuvio: fy4-16/esimerkki;
   Aurinko: kiekko) ja käytä sitä kaikkialla.
2. Voima on aina punainen ja alkaa kappaleesta; energian ja lämmön virta on oranssi; nopeus sininen. Päätä erikseen,
   piirretäänkö työntävä voima kärki pinnassa.
3. Jokainen merkintä saa oman tilansa: ei tekstiä viivan, toisen tekstin tai reunan päällä, ja yksikkö samassa
   muodossa kuin leipätekstissä.
4. Toistuva kohde (ihminen, hissi, Maa, lämpömittari, vaunu) piirretään yhdellä yhteisellä piirrolla.
5. Kaikki kuvat `figures.py`:n kautta talotyylillä, myös tutkimusvaiheen ja kokeiden kuvaajat.
