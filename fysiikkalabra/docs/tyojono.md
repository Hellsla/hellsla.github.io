# Työjono

Opettajan päättämät tulevat työt, joita ei ole vielä aloitettu. Jokainen kohta tehdään omana pull requestinaan;
valmis kohta poistetaan tästä samassa pull requestissa ja sen lyhyt yhteenveto lisätään `tyojono-loki.md`:hen.

Tämä on ainoa työjono (opettaja 2026-11-13): ei GitHub Issuesia eikä erillisiä listoja. Kohdat ovat
`docs/ROADMAP.md`:n järjestyksessä. Kohdan ottava ketju katsoo ensin avoimet pull requestit, merkitsee kohtaan
ensimmäisessä commitissaan `Varattu: <haara>` ja avaa luonnos-PR:n heti, jotta muut ketjut näkevät varauksen
(repon juuren `CLAUDE.md`). Saman kurssin kohdat tehdään peräkkäin, eri kurssien yleensä enintään kolme rinnakkain
(nyt enintään viisi, opettaja 2026-11-16); kun opettaja sanoo työn kiireelliseksi, ei ylärajaa (opettaja 2026-11-15).
Jonon pitää pysyä lyhyenä (alle 200 riviä): tässä on vain se, mitä tekijä tarvitsee aloittaakseen; täysi vanha teksti,
tehdyt kurssit ja opit ovat `docs/tyojono-loki.md`:ssä ("loki §N"), kirjatut päätökset `docs/decisions/tyojono-paatokset.md`:ssä.

## 0. Päivitystyön tehostaminen (opettaja 2026-11-17: "Laita kaikki seuraavaksi työjonoon")

Tehdään ennen uusia kurssikohtaisia läpikäyntejä. Tehty: 0a (`scripts/round.py`, #670), 0b (ohjetiedostot, #673), 0c (esitystapaluokka, #677; loki §0c), 0d (CI:n selain pilvi-istuntoihin; ei ympäristömuutosta, `ci_env.py` käynnistää Dockerin itse; `round.py` tarkistaa matalan kloonin ja riippuvuudet).
Osat 0e ja 0g muuttavat jaettuja tiedostoja: ne tehdään yksin, yksi kerrallaan, tässä järjestyksessä, ja yhdistetään
ennen sisältö-PR:iä. Jokainen osa raportoi PR:ssä, mitä se säästi (vuorot, tokenit, yhdistykset, katselmoinnit ennen ja jälkeen).

### 0e. Ulkoasun delta vain suomeksi, kun muutos on kielineutraali
Opettajan päätös 2026-11-17 (hyväksytty jonoon; sääntöteksti hyväksytään yhdistämällä PR). Kun muutos on esitystapaluokkaa
(0c) ja `check_i18n.py` toteaa saman rakenteen kaikilla kielillä, ulkoasukatselmoija katsoo vain suomenkielisen sivun;
en ja fi-easy saavat ulkoasun PASS:n carryna, jos `check_layout.py` menee niillä läpi kaikilla leveyksillä avatuin
ratkaisuin. Muu muutos (sanat, käännös, kuvat) katselmoidaan kieli kerrallaan kuten ennen. `reviews.py` RULES, `verify`,
`test_reviews.py`, `docs/QUALITY.md` ja komentotiedostot samassa PR:ssä. 0c:n jälkeen.

### 0f. Yksi läpikäynti per kurssi (työtapa, ei koodia)
Sama kurssi on käyty läpi erikseen kohdissa 5d, 8c, 8l-b, 18 ja 19, ja 8g ja 8j ovat tulossa; jokainen läpikäynti tuo
omat ulkoasukatselmointinsa kolmella kielellä, `site/`-rakennuksensa ja mainin yhdistyksensä. Tästä eteenpäin kurssin
avoimet kohdat tehdään yhdessä PR:ssä (laajennus kohdan 19 päätökseen 16.11. "jos saat yhdisteltyä PR niin tee"):
mekaaniset muutokset (8c, 8l-b:n jäännös, 5d:n tähteet) samaan PR:ään kurssin seuraavan sisältömuutoksen (8g, 8j)
kanssa, jonka katselmoinnit kattavat ne. Ei koskaan jo katselmoitavana olevaan PR:ään. Koordinaattori kirjaa jokaiselle
kurssille (FY1–FY9) yhden rivin: mitkä kohdat ovat auki ja missä PR:ssä ne tehdään. Voimaan heti; ei odota muita osia.

### 0g. `site/` pois sisältö-PR:istä (ensin suunnitelma, pysähdys opettajan hyväksyntään)
Jokainen yhdistetty PR vanhentaa kaikkien avoimien PR:ien `site/`-kopion, joten jokainen haara yhdistää mainin ja
rakentaa `site/`:n uudelleen keskimäärin 1,6 kertaa (juuren `CLAUDE.md` sääntö 4). Tavoite: sisältö-PR ei sisällä
`site/`-muutoksia; CI rakentaa sivuston ja `ruukkilabra-deploy.yml` julkaisee rakennetun version mainin ajon jälkeen.
Ensin pelkkä suunnitelma (`docs/audits/`), ei koodia: (1) miten `ci_scope.py` päättelee muuttuneet sivut ilman
committoitua `site/`-diffiä (kahden rakennuksen vertailu tai lähteistä); (2) miten "committoitu `site/` vastaa tuoretta
rakennusta" -tarkistus korvataan; (3) miten opettaja näkee PR:n vaikutuksen sivuihin ennen yhdistämistä (esikatselu
CI:n artefaktina tai `reviews.py impact`); (4) säilyykö `site/` repossa CI:n kirjoittamana vai poistuuko se kokonaan;
(5) julkaisun palautus virhetilanteessa; (6) siirtymä avoimille PR:ille. Julkaisusääntö ei muutu: sivulle pääsee vain
katselmoitu sisältö, ja yhdistäminen on opettajan julkaisupäätös. Toteutus omina PR:inään vasta hyväksynnän jälkeen.

## 4. FY10:n tutkimusten ja TVT-ohjeiden korjaukset (opettaja 2026-11-13)
Auditointi tehty (#536), Major-korjaukset ja sisältöosa tehty (#549, #645; loki §4). Jäljellä, opettajan päätettävä: erä 1
(jaetut komponentit: taulukoiden otsakkeet ja tyhjät rivit 390 px:ssä, listojen numerointi, laskurivit listoissa, apulinkit,
tyhjät 28×28 px:n kaappaukset; ajetaan yksin), Minor-erä ja yhteinen kuvasääntö (nimiöt vähintään noin 12 px 390 px:ssä,
mallikuvaajan akseleilla suure ja yksikkö, kaaviokuvan kuvateksti sanoo sen kaaviokuvaksi, malliksi merkitty luonnoskuvaaja).
Kuviin ei kosketa: opettaja piirtää ne itse.

## 5b. Leikkautuva kaava: avoimet päätökset (opettaja päättää)
Tarkistus ja `reflow`-carry tehty (#594). Auki: (1) lasketaanko vierityslinjalle jäävä inline-kaava leikkautuneeksi (nyt
kyllä), ja korjataanko vanha lista jaetulla komponentilla vai sivu kerrallaan; (2) tehdäänkö täysi CI-pohjainen lista
(koko sivuston ajo, noin 20 ydintuntia). Lista: `docs/clipped-formulas/<kurssi>.tsv` (rivejä vain poistetaan).

## 5c. ElevenLabs-ääneenluku FY1 ja FY2 (opettaja 2026-11-15)
Varattu: claude/elevenlabs-readaloud
Ääni Oskari - Finnish; mp3-tiedostot repoon Hellsla/ruukkilabra-audio, päärepossa vain manifestit. FY1:n luvut fy1-1…fy1-8
äänitetty; FY2 odottaa opettajan päätöstä. Sääntö: `CLAUDE.md` "Parts specified…", `docs/decisions/oppituntisivun-osat.md`. Tarkka toimeksianto: loki §5c.

## 5d. Leikkautuvat kaavat omalle rivilleen (opettaja 2026-11-15)
Tehty kaikille kursseille FY1–FY9 (loki §5d: kurssikohtaiset luvut, opit ja listalle jääneet rivit). Jäljellä vain
`docs/clipped-formulas/`:n tähderivit; ne tehdään 0c:n jälkeen ilman täysiä katselmointeja. Menetelmä: loki §5d "Opit".

## 6. Kuvatehtävät ja taulukkotehtävät FY8 ja FY9 (opettaja 2026-11-13…15)
Kaksi kuvatehtävää per luku hyväksytty kustannuksesta huolimatta (noin 300 k per luku); FY10:een ja FY14:ään ei. Jokaisessa
luvussa vähintään kaksi kuvatehtävää ja taulukkotehtävä noin joka kolmannessa; arvot vain `docs/mafy-arvot.tsv`:stä, uudet rivit
lähde-URL:n kanssa. FY8 yksi luku per PR; tehty fy8-1, fy8-3, fy8-7, fy8-8 (#669), fy8-9 (#674), fy8-10 (#678), fy8-11 (#682), fy8-12 (#685), fy8-13 (#688; ei taulukkotehtävää: ei VERIFIED-riviä, MAFY-taulukkoa ei löytynyt), fy8-14 (#692; ei taulukkotehtävää: mafy-arvot.tsv:ssä ei FY8-riviä); tila: `python scripts/exercise_bank.py FY8`.
Jäljellä fy8-2 (kuva `fy8-2/lamp-spectrum`; tiedekatselmoinnin löydös elohopean tasoista: loki §6), fy8-4…fy8-6 (tarkista tila), fy8-15, fy8-16 ja FY9.
Kehittäjä jakaa pitkät sijoitusketjut (hc omaksi vaiheekseen, energia jouleina ennen eV-muunnosta) jo ensimmäisessä
versiossa. Tämä kohta jää, kunnes FY8 ja FY9 on tehty.

## 8. Virhekäsitys omana komponenttinaan; virhekäsitys ja tiivistelmä avattaviin laatikoihin (opettaja 2026-11-13)
Teoria-vaiheeseen toistuva osa: väite yhdellä lauseella, sitten miksi se ei päde (`docs/audits/2026-11-10-vaiheiden-kayttoliittyma.md` 5.2).
"Yleinen virhekäsitys" ja Tiivistelmä omiin suljettuihin `<details>`-laatikkoihinsa (näppäimistöllä avattavat); sivupohjan
muutos, ei katselmointeja; tarkista käsitekorttien alleviivaus ja sirut laatikon sisällä (`test_home.py`). Sisältötyö luku kerrallaan sen jälkeen.

## 8c. Kappalejako esimerkkien ja ratkaisujen vaiheisiin (opettaja 2026-11-13)
Sääntö NOTES.md §3 "Paragraphs in stages and steps", luokka `md-paragraphs` (tiede ja pedagogiikka carry, visual delta), lint varoittaa.
Tehty: FY1, FY2 (luvut ja Sovella, claude/fy2-lapikaynti, PR #676; FY2:n esimerkkikokeessa ei ollut jaettavaa), FY4, FY5 (Sovella ja koe mukana, 0f-PR #671), FY6 (Sovella ja koe mukana), FY7 (Sovella ja koe mukana, 0f-PR #681). Jäljellä
järjestyksessä FY8 → FY3 loput → FY9 → FY10. Kurssi kerrallaan, kaikki kielet
(`/quality-audit --fix`), kuten loki §8c. Sääntö osamerkeille: katko osamerkin eteen, ei osan keskelle. Kohta 0f: tehdään kurssin
muiden avointen kohtien kanssa samassa PR:ssä.

## 8d. Käsitekorttien pitkät otsikot katkeavat keskeltä sanaa (opettaja 2026-11-13)
"Ominaislämpökapasiteet|ti": korjaus kerran `templates/kortit.js`:ssä tavutuksella (pehmeät tavuviivat tai `hyphens:auto` + `lang`),
niin että katko osuu tavurajalle viivalla; koskee myös kasitteet.html, Kertauspakka ja Varmista käsitteet; `test_home.py`: 360 ja 1280 px. Sivupohja, ei katselmointeja.

## 8e. Kuvien asettelu (opettaja 2026-11-13) — toteutetaan kohdan 11 U3:n osana
Turha pystyväli kuvan vierellä, kuva ja pieni taulukko tai kaksi pientä taulukkoa vierekkäin, kuva aina selittämänsä kappaleen
viereen, valokuva kuvateksteineen oikealle palstalle (`build.py fig_rows`, site.css, `check_layout.py`). Ennen/jälkeen-kuvat: fy3-8, fy4-3, fy1-1 (1280, 1440, 1920 px). Täysi kuvaus: loki §8e.

## 8f. Animoitu kuva (opettaja 2026-11-13, pilotti fy3-8)
Pilotti tehty (#649, `Fig(anim=True)`/`vibrate()`); odottaa opettajan hyväksyntää (`reviews.py approve-figures fy3-8` vasta sen jälkeen). Muut luvut vasta hyväksynnän jälkeen. Vaatimukset: loki §8f.

## 8g. Mallivastaukset perusperiaatteesta (opettaja 2026-11-13)
Tehtävien, Sovellan ja kokeiden mallivastausten Kaava-vaihe alkaa perusyhtälöistä ($\eta = E_\text{hyöty}/E$, $E = Pt$, $Q = rm$, energiatase),
sitten johdettu kaava, symbolinen sievennys loppuun, vasta sitten sijoitus. Kurssi kerrallaan `/exercises`- ja `/practice`-putkella; yhdistetään saman kurssin
kesken olevaan tehtäväkatselmointiin (FY5, FY6, FY7), ei rinnakkain.

## 8j. Pohdinnan kertaustehtävä liittyy pohdinnan ilmiöön (opettaja 2026-11-13)
Tehty: FY4 (#647), FY5 (#661 ja 0f-PR #671: fy5-7, fy5-11, fy5-17; `docs/audits/2026-11-17-8j-FY5.md`), FY1 (0f-PR #679: fy1-2, -5, -6, -7; `docs/audits/2026-11-17-8j-FY1.md`), FY6 (0f-PR #675: fy6-2…14; `docs/audits/2026-11-17-8j-FY6.md`).
FY2 tehty paitsi fy2-1 (ei kertaustehtävää; kysymys opettajalle, `docs/audits/2026-11-17-8j-FY2.md`; PR #676).
Jäljellä FY1:n fy1-1 ja fy1-8 (kertaus paljastaisi Ennusta-vastauksen; kysymys opettajalle, FY1-audit), FY3, FY7, FY8 (ja fy2-1). Sääntö: `herata`-vaiheen retrieval-`choice` kysyy pohjatietoa saman ilmiön kautta. Lopuksi sivupohjan muutos:
Pohdinnan järjestys ilmiö → kertaustehtävä → pohdintakysymys (`inquiry.py`/js; kirjataan `docs/inquiry.md`:hen).

## 8k. Opettajan hyväksymä tekstimuutos ohittaa katselmoinnin (opettaja 2026-11-13)
Uusi kategoria `teacher-text` kuten `teacher-figure`: `reviews.py approve-text <id> [--lang]` kirjaa hyväksytyn diffin (esim. `docs/teacher-text.tsv`),
`scope` antaa none/carry, `verify` johtaa uudelleen. Vain opettajan nimenomaisesta hyväksynnästä. Jaettu (`scripts/reviews.py`, testit): yksin.

## 8l-b. "Esimerkkiaineisto" pois otsikoista (opettaja 2026-11-16)
`caption-label` tunnistaa kaikki muodot (#658); poistettu FY1, FY2, FY4, FY6, FY7. FY5 tehty (0f-PR #671). Jäljellä FY8 (fy8-2), fi, fi-easy, en:
otsikot `reviews.caption_label_free`-funktiolla ja `reviews.py carry <id> --exercises [--lang]`; tehdään kurssin muiden töiden mukana (0f).

## 8q. `reviews.translation_differs`: alaindeksisana ja yksikkökaava yksin (jaettu `scripts/`; 2026-11-17)
Varattu: claude/reviews-translation-units
Tausta: 0c (#677) ja 8p (#684) ovat mainissa, mutta fy8-13:n (#688) en ja fi-easy eivät silti siirry carryllä: pelkkä `$\text{ka}$`
(en `$\text{avg}$`) ja fi-easyn pelkkä yksikkökaava `$\text{mSv}$` (fi: sana "millisieverteinä") lasketaan eri kaavoiksi.
Korjaus: (a) tunnetut alaindeksiparit (ka↔avg, alku↔initial, loppu↔final…), (b) pelkkä `\text{sana}`-kaava ei lisää kaavamäärää
vaan vertautuu toisen tekstin sanaan, (c) testit `test_reviews.py`:ssä, (d) `reviews.py verify` ja fy8-13 palauttaa None.
Yksiköt (kg, N, mSv…) luvun kanssa pysyvät tiukkoina. Yhdistetään yksin.

## 10. Simulaatioiden käyttöliittymä (opettaja 2026-11-14)
Mittaus ja päätökset `docs/audits/2026-11-14-simulaatioiden-kayttoliittyma.md`. PR 1–4b tehty (#563, #588, #591, #648, #652). Jäljellä
**PR 5** (jaettu, yksin): canvasin nimi ja kuvaus, valintaruudut 40 px:n kohteiksi, näkyvä kohdistus. Myöhemmin kurssi kerrallaan luvun seuraavan
sisältömuutoksen yhteydessä: tyyppi D (fy6-5, fy6-6, fy6-9, fy6-12, fy6-13, fy6-14), fy1-2:n säätimien ryhmittely, näppäinvaihtoehto raahaukselle,
nimien yhtenäistäminen (Toisto / Tauko / Alusta), toistuvien seliterivien poisto. Ei muuta sim.js-tiedostoja eikä fysiikkaa PR 5:ssä; 1366×650:n lisähuomiot: loki §10.

## 11. Tehtävänäkymä ja teorian taitto (opettaja 2026-11-14, UI/UX-auditointi)
Yleislinja (CLAUDE.md "General UI line"): käyttöliittymään ei lisätä tekstiä. U4 (#561) ja U5 (#582) tehty. U1–U3 jaettuja (`templates/`, `scripts/`, `site.css`, `lang/`):
yksin, järjestyksessä U1, U2, U3, kohdan 10 PR 5:n jälkeen; ennen/jälkeen-kuvat PR:ään ja pysähdys opettajan hyväksyntään. Fysiikkaan, vastauksiin,
toleransseihin, tallennusavaimiin ja palautustiedostoon ei kosketa. Täysi määrittely: loki §11.
- **U1 Ydintehtävät auki Tehtävät-vaiheen alkuun**: luvun ydintehtävät (`build.py core_ids`, tasot 1 ja 2, ei tasoa 3) näkyvät auki otsikon alla yhdessä kortissa,
  tason merkki **Perus**/**Soveltava** (hyväksytty teksti), muut tehtävät suljetuissa tasolaatikoissa niiden alla; ei uutta otsikkoa, laskuria eikä ohjeriviä;
  `level_lead_1/2` poistetaan. Ehdot: tehtävä DOM:ssa kerran, id, `data-num`, tarkistus, vihjeet, ratkaisut ja Yritä ensin ennallaan; `palautus_tasks.py` lukee
  tason uudesta `data-level`-tiedosta; `lesson.js`:n tasolaskuri, pakollisten vastausten sääntö, teorian vieressä -tila ja koko näytön tila päivitetään; toimii ilman JS:ää.
  Testit: `test_progress`, `test_palautus`, `test_tehty`, `test_writepad`, `test_koko`, `check_layout`, `palautus_tasks.py --check`, `check_a11y`. Samassa PR:ssä CLAUDE.md:n Lesson page 8 korjataan.
- **U2 Tehtäväkortin järjestys** (U1:n jälkeen): numero ja merkit; tilanne ja kysymys; kuva; vastauskenttä + Tarkista (täytetty päänappi) + Kirjoita ratkaisu; palaute; erotinviivan alla Vihjeet, Vastaus, Näytä ratkaisu, lukko. Ei uusia tekstejä.
- **U3 Teorian taitto, vaihtoehto B** (kohta 8e): 38 rem:n palsta säilyy; teksti kuvarivin yläreunaan, valokuva viereen, kaksi pientä taulukkoa vierekkäin, korkea kuva alle tai seuraava kappale viereen.
- Ei tehdä: Aloita-riviä, "Näytä kaikki tehtävät" -toimintoa, etusivun ryhmäotsikoita, marginaalipalstaa tai keskitettyä lukupalstaa, yhden luvun julkaistua pilottia.

## 11b. FY9: adaptiivinen YO-valmentaja (opettaja 2026-11-14)
Suunnitelma `docs/FY9_ADAPTIVE_PLAN.md` (#566), hyväksytty P1–P12. PR 1 (YTL/Abitti-tietojen tarkistus, sisältö) voi alkaa heti; PR 2–8 jaettuja, yksin, kohdan 10 PR 5:n ja U1:n jälkeen;
PR 9 Abitti 2 -ohje; PR 10 kielimallin selvitys. Ei palvelinta, ei tekoälyrajapintaa; jokainen uusi käyttöliittymäteksti hyväksytään PR kerrallaan. Arvio 2,5–3,5 M tokenia.

## 17. Kehitys ilman kirjautumista (opettaja 2026-11-15)
Ohjeet ja päätökset K1–K9: `docs/audits/2026-11-15-kehitys-ilman-kirjautumista.md`. Jokainen osa oma PR, yksin; uudet käyttöliittymätekstit PR:n kuvauksessa. Tallennusavaimia, tiedostomuotoja ja korttien id:itä ei muuteta.
Osat: 17a verkoton käyttö (service worker, manifesti, moduuli laitteelle), 17b koko työ yhteen tiedostoon, 17c yleisvirheiden tunnistus, 17d ajoitettu kertaus, 17e luokan yhteenveto, 17f hakemistot ja haku.
Järjestys: 17a PR 1–2, 17b PR 1, 17f PR 1–2, 17c PR 1, 17e, 17d PR 1, sitten 17f PR 3, 17a PR 3, 17b PR 2. Osien sisältö: loki §17.

## 18. Oikoluvun korjaukset FY1–FY9 (opettaja 2026-11-15)
Kaikki kurssit tehty (loki §18). Jäljellä vain `docs/physics-phrases-known/`:n rivit (FY5, FY6, FY9): korjaus poistaa rivin; samat virkkeet fi-easy ja en samalla.
Päätökset P1–P9: `docs/audits/2026-11-15-oikoluku.md`; raja-arvotehtävien tarkistus hyväksyy poikkeaman molempiin suuntiin.

## 19. 45 soveltavaa aineistotehtävää FY1–FY9: tehty (loki §19)
Kaikki 45 tehty (FY1–FY9, A1–A5). Avoin vain: opettaja avaa Tukesin kaksi linkkiä (FY6 A3, A4) selaimessa ennen yhdistämistä. Poistetaan, kun se on tehty.

## 13. Englanninkieliset käsitekortit FY6 ja FY8 (opettaja 2026-11-13; kohdan 18 jälkeen, ennen kohtaa 15)
`kortit/en/fy6.json` ja `fy8.json` puuttuvat, joten englanninkielisillä FY6- ja FY8-sivuilla ei ole kortteja eikä alleviivauksia.

## 15. Kustannustoimituksellinen lopputarkistus FY1–FY8 (opettaja 2026-11-14, kevennetty 2026-11-16)
Toiseksi viimeinen: kohtien 17, 18, 13 jälkeen, sen jälkeen 14 ja viimeisenä 16. Ensin pelkkä raportti (`docs/audits/`), korjaukset vasta opettajan luettua. Kevennetty:
(1) automaattiset läpikäynnit (concepts.py, coverage.py --all, physics_phrases, check_a11y; yksi raportti); (2) otos: täysi tarkistus yhdelle luvulle per kurssi, raportti opettajalle;
(3) laajennus vain, jos otos löytää kriittisiä virheitä. LOPS 2019 vertailuperusta; julkaistuja oppikirjoja ei käytetä; virheitä ei oleteta; tunnisteita, vastauksia ja tallennusmuotoja
ei muuteta ilman todettua virhettä; lähdekoodia ei muokata. Raportin rakenne ja kahdeksan tarkistuskohtaa: loki §15.

## 14. Ahjo ja LUMA-tutor yhteiseen jaksopohjaan (opettaja 2026-11-13; juuri ennen vihkoja)
Siirretään `ahjo.py` ja `lumatutor.py` jaksopohjan lohkoiksi niin, että sivut pysyvät tavulleen samoina kuten Kilparobotiikassa; puuttuvat lohkot yhteiseen kirjastoon. Jaettu: yksin.

## 16. Vihkot FY1–FY8 (opettaja 2026-11-13; jonon viimeinen)
A5-vihkot kaikille kursseille tiiviillä asettelulla (`python scripts/print_book.py <C> --lang fi|en --publish`); FY1–FY4 tehdään uudelleen, FY5–FY8 uusia. Vasta kohtien 3, 17 ja 18
jälkeen; rakenna sivusto vihkojen jälkeen (Vihkot-sivu).
