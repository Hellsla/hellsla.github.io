# Kehitys ilman kirjautumista: ohjeet työjonon kohdalle 17

Opettaja 15.11.2026: Ruukkilabran tulee olla paras digitaalinen fysiikan oppimisympäristö, ja pysyvä rajoite on, että
sivustolle ei kirjauduta. Kymmenestä ideasta opettaja valitsi kuusi ja hyväksyi samana päivänä päätökset K1–K9
(taulukko lopussa). Tämä tiedosto on ohjeet niiden tekemiseen; työjonon kohta 17 viittaa tänne.

Ei tehdä (opettaja 15.11.): puhelin mittalaitteena ("tähän on omat softat"). Valitsematta jäivät myös sivun oma
kuvaaja- ja sovitustyökalu, symbolisen vaiheen tarkistus ja tehtäväpaketti linkkinä.

## Kaikille osille yhteistä

- **Ei palvelinta, ei tunnuksia, ei seurantaa, ei kielimallia ajon aikana.** Kaikki tila on opiskelijan selaimessa tai
  hänen omassa tiedostossaan (`fysiikkalabra/CLAUDE.md` "Never").
- **Jokainen osa on oma työntekijäketjunsa, haaransa ja luonnos-PR:nsä.** Lähes kaikki muuttavat jaettuja tiedostoja
  (`scripts/`, `templates/`, `lang/`, `.github/workflows/`), joten ne tehdään yksin, yksi kerrallaan, ja yhdistetään
  ennen sisältö-PR:iä (juuren `CLAUDE.md` sääntö 3).
- **Käyttöliittymätekstit:** opettaja hyväksyi 15.11. sen, mitä tekstejä saa tulla (K1–K9). Tarkat sanamuodot ketju
  luettelee PR:n kuvauksessa kolmella kielellä, ja opettaja hyväksyy ne yhdistämällä. Muita tekstejä ei lisätä.
- **Tallennusavaimia, tiedostomuotoja ja korttien id:itä ei muuteta eikä kirjoiteta uudelleen.** Uusi tieto on uusi
  kenttä tai uusi avain; vanha tietue luetaan sellaisenaan.
- **Kielet:** jokainen uusi teksti kaikkiin kolmeen (`lang/fi.json`, `en.json`, `fi-easy.json`), `check_i18n.py`.
- **Testit ja CI:** uusi selaintesti saa omat jobinsa (`scripts/ci_parallel.py`), ja jokainen uusi tiedostolaji, joka
  muuttaa sivua, saa rivinsä `scripts/ci_scope.py`:hen. Mergen jälkeen katsotaan `main`in ajo.
- **Tietosuojasivu** (`tietosuoja.html`) päivitetään samassa PR:ssä, kun selaimeen tallentuu jotain uutta.

## Nykytila, johon osat nojaavat (tarkistettu koodista 15.11.2026)

| Asia | Missä | Huomio |
|---|---|---|
| Verkoton käyttö | ei ole | sivustolla ei ole service workeria eikä web-sovelluksen manifestia |
| Sivuston koko | `site/` 243 Mt | suomen sivut 49 Mt (290 sivua), `en/` 48 Mt, `fi-easy/` 45 Mt, `pics/` 23 Mt, `vendor/` 5 Mt, `sims/` 1,9 Mt; yksi 16 luvun moduuli noin 4,5 Mt HTML:ää |
| Versiointi | `build.py` | omat skriptit viitataan muodossa `lesson.js?v=<tiiviste>`; sivuilla ja `vendor/`-tiedostoilla ei ole versiota |
| Ääneenluvun malli | `readaloud.js` | omassa Cache Storage -välimuistissaan `fl-tts-supertonic3-v1` |
| Moduulin työtiedosto | `palautus.js` `courseWork`, muoto `ruukkilabra-tyo` v1 | kokoaa yhden moduulin avaimet ja ratkaisut; sama tiedosto on myös palautus opettajalle |
| Ratkaisujen vienti | `padstore.js`, muoto `ruukkilabra-ratkaisut` v1 | editorin ratkaisut (IndexedDB) |
| Mikään tiedosto ei sisällä | | `ruukkilabra:kortit`, `ruukkilabra:kortit-suunta`, `ruukkilabra:viimeisin` (koko sivuston avaimia) |
| Virhepalaute | `inquiry.json` `mistakes` `{value, feedback}`, `inquiry.js` osa 4 | vain luvun omissa laskutehtävissä (129 lukua ja yksikköä); `exercises.json`-tehtävissä ei ole |
| Laskutehtävän tarkistus | `lesson.js` osa 1; `build.py` kirjoittaa `data-answer`, `data-tol`, `data-step` | tulos `ok` / `close` (Lähellä) / `no`; tapahtuma `fl:attempt {id, kind, state}` |
| Korttipakka | `kortit.js`, `ruukkilabra:kortit` `{id: {tila, osasinPutki, muokattu}}` | kolme "Osasin" peräkkäin poistaa kortin pakasta, eikä se palaa |
| Kertausväli FY9:ssä | `docs/FY9_ADAPTIVE_PLAN.md` 5.3 | 2 → 5 → 10 → 20 vrk; hyväksytty, ei vielä rakennettu |
| Arviointisivu | `palautus/apps-script/Code.gs`, `Review.html`, `paikallinen/local-backend.js`; generoi `palautus_tasks.py` | opiskelijakohtainen pistetaulukko on; tehtävä- tai tavoitekohtaista luokan näkymää ei ole |
| Haku | `mixer.py` (YO-sekoitin), `invfilter.js` (FY10) | koko sivuston hakua ei ole |
| Kaavojen nimet | `docs/<moduuli>/kaavanimet.tsv` (FY1–FY9) | sarakkeet `tunti, rivi, kaava, kaava_en, nimi, name_en, lähde, MAFY-sivu, huomio` |

## 17a. Verkoton käyttö ja asennus

**Miksi:** koulun verkko katkeilee ja opiskelija lukee bussissa. Lisäksi Safari voi tyhjentää sivuston tallennuksen,
jos sivustolla ei käydä viikkoon; kotivalikkoon asennettu sivusto on tiettävästi poikkeus. PR 1 tarkistaa tämän
WebKitin omasta dokumentaatiosta ja kirjaa lähteen tähän tiedostoon ennen kuin mitään perustellaan sillä.

**PR 1: käydyt sivut toimivat verkotta.**
- `templates/sw.js`, jonka `build.py` kirjoittaa `site/sw.js`:ksi sivuston juureen (kattaa myös `en/` ja `fi-easy/`),
  sekä pieni `templates/offline.js`, joka rekisteröi sen vain `https:`-osoitteessa ja localhostissa (ei `file://`,
  ei `preview/`). Molemmat templatet (`page.html`, `lesson.html`) lataavat sen.
- Säännöt: HTML-sivu haetaan ensin verkosta (noin 3 s aikaraja), ja vasta sitten välimuistista, jotta verkossa oleva
  opiskelija saa aina uusimman julkaisun. `?v=`-versioidut skriptit ja tyylit ensin välimuistista. Muut saman
  alkuperän GET-pyynnöt (`vendor/`, `pics/`, `sims/`, `kortit/`, `brand/`, fontit) välimuistista ja päivitys taustalla.
  Kyselyosa (`?ratkaisut=1`, `?simloop=1`) ei saa estää sivun löytymistä välimuistista.
- Ei välimuistiin: `models/` (ääneenluvulla on omansa), `audio/`-mp3:t ja kaikki muiden alkuperien pyynnöt.
- Yläraja välimuistin koolle ja vanhimpien poisto; uusi `sw.js` korvaa vanhan ja siivoaa sen välimuistit.
- Hätäkatkaisu: dokumentoi tähän tiedostoon, miten rikkinäinen service worker poistetaan julkaisemalla itsensä
  purkava `sw.js`, ja testaa se.
- `scripts/deploy_site.py`: varmista, että `sw.js` julkaistaan juureen ja että sen tarkistukset pätevät siihen.
- K1: Tietosuoja-sivulle yksi lause siitä, että avatut sivut tallentuvat laitteelle verkotonta käyttöä varten. Muuta
  uutta tekstiä ei tule.
- Testi `scripts/test_offline.py` (sivusto http-palvelimelta kuten `test_home.py`): avaa luku, odota service worker,
  katkaise verkko (Playwright `set_offline`), lataa uudelleen. Sivu, kaavat, simulaatio ja tehtävän tarkistus toimivat;
  käymätön sivu epäonnistuu selaimen omalla virhesivulla; uusi versio korvaa vanhan.

**PR 2: asennettava sivusto ja pysyvä tallennus (ei uutta tekstiä).**
- `manifest.webmanifest` kullekin kielelle (`start_url` sen kielen etusivu), `<link rel="manifest">` ja `theme-color`
  templateihin. Kuvakkeet 192 ja 512 px sekä maskable-versio tehdään `brand/ruukkilabra-symboli.svg`:stä; logoa ei
  piirretä uudelleen.
- `navigator.storage.persist()` kutsutaan, kun opiskelija on tallentanut ensimmäisen vastauksensa, ja vain selaimissa,
  jotka eivät näytä siitä lupakyselyä (selvitä selaimittain; kysely olisi uutta käyttöliittymää).
- Asennuspainiketta ei tehdä: selaimen oma "Lisää kotivalikkoon" riittää.

**PR 3: moduuli laitteelle (pilotti FY3, pysähtyy opettajan hyväksyntään).**
- `build.py` kirjoittaa `site/<kieli>/offline/<MODUULI>.json`: moduulin sivujen ja niiden tiedostojen osoitteet ja
  koot, poimittuna rakennetuista sivuista (`src`, `href`), ei käsin ylläpidettynä listana.
- Moduulisivun painike hakee listan tiedostot välimuistiin erissä, näyttää edistymisen ja tarkistaa tilan
  (`navigator.storage.estimate()`). Arvio: 5–10 Mt moduulia ja kieltä kohti.
- K2: painikkeen tekstit (nimi, edistyminen, valmis, koko) ja paikka moduulisivulla ehdotetaan PR:n kuvauksessa.

### 17a PR 1: toteutus ja hätäkatkaisu (työntekijä 2026-11-18)

- **Tiedostot:** `templates/sw.js` → `site/sw.js` (juuri, kattaa `en/` ja `fi-easy/`), `templates/offline.js` (rekisteröi vain
  `https:`-osoitteessa ja localhostissa, ei `file://`, ei `preview/`; ensimmäisen asennuksen jälkeen kertoo työntekijälle jo ladatut
  tiedostot, jotta ensimmäinen käynti toimii heti verkotta), `templates/sw-kill.js` (hätäkatkaisu). Molemmat sivupohjat lataavat `offline.js`:n.
- **Välimuistit:** `fl-sw-1-pages` (HTML, enintään 120 sivua) ja `fl-sw-1-static` (muut, enintään 1500 tiedostoa); vanhimmat poistuvat
  ensin, ja kun `navigator.storage.estimate()` näyttää yli 80 % käytetystä, poistetaan 20 vanhinta. Vain etuliitteellä `fl-sw-` alkavat
  välimuistit ovat työntekijän omia: ääneenluvun `fl-tts-supertonic3-v1` jää koskematta. Uusi `sw.js` (sen teksti sisältää jaettujen
  skriptien tiivisteen) korvaa vanhan ja poistaa muut `fl-sw-`-välimuistit; skeeman vaihto = `SCHEMA`-vakion muutos.
- **Säännöt:** HTML verkosta ensin, 3 s kuluttua välimuistin kopio (verkon vastaus päivittää kopion silti); `?v=`-tiedostot ensin
  välimuistista; muut saman alkuperän GET-pyynnöt välimuistista ja päivitys taustalla; kyselyosa ei vaikuta sivun löytymiseen. Ei
  välimuistiin: `models/`, `audio/`, Range-pyynnöt, ohjatut vastaukset ja muut alkuperät.
- **Hätäkatkaisu (rikkinäinen service worker pois):** rakenna ja julkaise sivusto komennolla `FL_SW_KILL=1 python scripts/build.py`
  (tai kopioi `templates/sw-kill.js` tiedostoksi `site/sw.js`). Se on sama osoite, joten selain hakee sen seuraavalla käynnillä
  (enintään 24 h, GitHub Pages -välimuistilla tyypillisesti minuuteissa), poistaa kaikki `fl-sw-`-välimuistit, poistaa rekisteröinnin ja
  lataa avoimet sivut uudelleen. Sen jälkeen julkaistaan tavallinen `sw.js` takaisin, kun vika on korjattu. `test_offline.py` testaa
  katkaisun. Opiskelijan tallentamat työt (localStorage, IndexedDB) eivät ole välimuistissa eikä katkaisu koske niitä.
- **Safarin tallennuksen poisto (WebKit):** lähdettä ei saatu tarkistettua tässä istunnossa, koska `webkit.org` ei ole ympäristön
  verkkolistalla. Mitään ei perustella sillä: PR 1 ei tee oletusta siitä, että kotivalikkoon asennettu sivusto säilyy. Tarkistus tehdään
  PR 2:n alussa (WebKitin blogi "Full Third-Party Cookie Blocking and More", 7 päivän raja ja kotivalikon poikkeus) ja lähde kirjataan tähän.

## 17b. Koko työ yhteen tiedostoon

**Miksi:** moduulin työtiedosto on jo olemassa, mutta kolmen moduulin opiskelija tallentaa kolme tiedostoa, eikä
korttipakka ole missään tiedostossa. Puhelimesta tiedostoa on hankala saada koneelle.

**PR 1: koko sivuston varmuuskopio.**
- Irrota `palautus.js`:n `courseWork`ista kokoamis- ja palautusfunktiot yhteiseen käyttöön muuttamatta
  `ruukkilabra-tyo` v1:n muotoa, tiivistettä tai tuonnin sääntöjä (lue nykyinen tuonti ja pidä sama yhdistämissääntö).
- Uusi muoto `ruukkilabra-kaikki` v1: jokaisen moduulin `store` (kuten työtiedostossa) sekä koko sivuston avaimet
  `ruukkilabra:kortit`, `ruukkilabra:kortit-suunta`, `ruukkilabra:viimeisin`. Kuvaus `palautus/TIEDOSTOMUOTO.md`:hen.
- K3: tallennus ja avaus ovat Tietosuoja-sivun kohdassa "Mitä selaimeesi tallentuu?"; tekstit ehdotetaan PR:n
  kuvauksessa.
- Varmuuskopio ei ole palautus: arviointisivun tuonnin pitää hylätä se selkeällä viestillä (`Code.gs` `rlValidate_`),
  ja testi varmistaa sen. Moduulin työtiedostoon ei lisätä mitään, koska se menee opettajalle (opettaja 14.11.:
  näyttöloki vain varmuuskopioon, ei palautukseen).
- Testit: vienti ja tuonti toiseen selainprofiiliin palauttaa vaiheet, vastaukset, ratkaisut, itsearviot, Tehty-rastit
  ja korttipakan; rikkinäinen tai vieras tiedosto ei muuta mitään (`test_palautus.py`, `test_koko.py`).

**PR 2: jakaminen puhelimesta.**
- Kun `navigator.canShare({files})` on tosi, tallennus tarjoaa laitteen jakovalikon (AirDrop, Drive, sähköposti);
  muuten lataus kuten nyt.
- K4 (tulkinta): jakovalikko tulee samaan painikkeeseen, ei omaa painiketta eikä uutta tekstiä.

**Ei tehdä nyt:** QR-siirto (ilman palvelinta se toimii käytännössä vain koneelta puhelimeen, ja koodiin mahtuu noin
2 kt; tiedosto ja jakovalikko kattavat tarpeen) ja itsestään päivittyvä työtiedosto (toimii vain Chromium-selaimissa
ja vaatii luvan joka istunnossa).

## 17c. Yleisvirheiden tunnistus laskutehtäviin

**Miksi:** väärästä luvusta sivu sanoo nyt vain, että se on väärin. Yleisin virhe on yksikkömuunnos, ja sen voi
tunnistaa luvusta ilman tehtäväkohtaista sisältöä.

**PR 1: yleinen tunnistus (jaettu; ei muuta yhtään tehtävää, joten katselmoinnit eivät vanhene).**
- Uusi puhdas funktio, esimerkiksi `templates/virhe.js` → `window.flMistake(arvo, vastaus, toleranssi, yksikkö)`,
  jota `lesson.js` osa 1 kutsuu, kun tulos on `no` eikä tehtävän oma `mistakes` osunut. Sama funktio kopioidaan
  arviointisivulle generoinnissa (17e), joten lähde on yksi.
- Säännöt tässä järjestyksessä, jokainen samalla toleranssilla kuin tarkistus, ei koskaan kun vastaus on 0:
  1. etumerkki: arvo ≈ −vastaus;
  2. kertaluokka: arvo / vastaus ≈ 10^k, k = ±1 … ±9 (etuliite tai yksikkömuunnos);
  3. aika ja nopeus: suhde ≈ 3,6, 60 tai 3600 tai niiden käänteisluku;
  4. kelvin ja celsius: |arvo − vastaus| ≈ 273,15, vain kun yksikkö on K tai °C.
- Ei yleisessä kerroksessa: asteet ja radiaanit, unohtunut neliö tai puolikas. Ne vaativat tehtävän kaavan (PR 2).
- K5 (tulkinta): palaute käskee tarkistamaan (yksikkömuunnokset ja etuliitteet, etumerkki ja suunta, ajan yksikkö,
  kelvinit ja celsiusasteet) eikä sano, että numerot ovat oikein. Neljä sanamuotoa ehdotetaan PR:n kuvauksessa.
- `fl:attempt`-tapahtuman `detail`iin kenttä `mistake`. FY9-valmentajan PR 3 (kohta 11b) lisää saman kentän
  tehtäväkohtaisen `mistakes`-rivin indeksinä: sovi yksi muoto (indeksi tehtäväkohtaiselle, merkkijono yleiselle);
  ensin yhdistettävä PR määrää sen ja kirjaa `FY9_ADAPTIVE_PLAN.md`:hen.
- Testit: funktion yksikkötestit selaimessa; ajo kaikkien julkaistujen laskutehtävien yli (oikea vastaus ei koskaan
  laukaise sääntöä, vastaus × 1000 laukaisee kertaluokan); `test_inquiry.py`: tehtävän oma `mistakes` voittaa yleisen.

**PR 2: tehtäväkohtaiset virheet tehtäväpankkiin (sisältöä; pilotti yksi luku, pysähtyy opettajan hyväksyntään).**
- `answers.py` laskee tehtävän tyypilliset väärät arvot (asteet/radiaanit, neliö unohtui, halkaisija säteenä, grammat
  kilogrammoina) ja `exercises.json` saa `"mistakes": [{"value", "key"}]`. Palautetekstit ovat yhteisiä avaimia
  `lang/`-tiedostoissa, ei tehtäväkohtaista tekstiä (token economy). `build.py` kirjoittaa ne kuten `inquiry.py`.
- Tarkistus: jokainen virhearvo on toleranssin ulkopuolella oikeasta vastauksesta ja muista virhearvoista.
- K6 (tulkinta): koordinaattori ehdottaa pilottiluvun, ja pilotti katselmoidaan täysin (`reviews.py scope`). Kevyempää
  katselmointia (uusi `reviews.py`-luokka) ehdotetaan opettajalle erikseen vasta pilotin jälkeen.
- Yleistys kurssi kerrallaan kunkin tehtäväsarjan seuraavan sisältömuutoksen yhteydessä, ei omana kierroksenaan.

## 17d. Ajoitettu kertaus

**PR 1: kortit palaavat pakkaan (vain `kortit.js`, `test_home.py` ja tämän säännön lause `CLAUDE.md`:ssä).**
- Tietueeseen kaksi uutta kenttää: kertausporras ja eräpäivä. Kolmannen "Osasin"-merkinnän jälkeen kortti poistuu
  pakasta kuten nyt, mutta tulee takaisin 5, sitten 10, sitten 20 vuorokauden päästä (K7; sama porrastus kuin
  `FY9_ADAPTIVE_PLAN.md` 5.3, jotta sivustolla on yksi sääntö). Palannut kortti etenee yhdellä "Osasin"-merkinnällä;
  "Kertaa myöhemmin" palauttaa sen alkuun. Viimeisen portaan jälkeen kortti jää pois.
- K7: ennen muutosta pakasta poistuneita kortteja ei ajoiteta; vain muutoksen jälkeen merkityt palaavat.
- Eräpäivä lasketaan, kun pakka luetaan; ajastimia ei ole. Vanha tietue ilman uusia kenttiä luetaan sellaisenaan.
- Moduulisivun laatan ja Kertauspakkasi-osion lukumäärä sisältää palanneet kortit; uutta tekstiä ei tarvita.
- Korttipakka kulkee laitteelta toiselle vasta 17b:n varmuuskopiossa.

**PR 2: sekoitettu kertaus FY1–FY8:lle (myöhemmin).**
- Tämä on FY9-valmentajan laajennus, ei oma järjestelmänsä (opettaja 14.11.: laajennus muihin moduuleihin myöhemmin).
  Aloitetaan vasta, kun kohdan 11b PR 4 on yhdistetty ja opettaja on käyttänyt sitä.
- Ensin yhden sivun suunnitelma-PR: mitä `valmentaja.py` ja `valmentaja.js` yleistetään (`kertaus/<MODUULI>.json`,
  avain `ruukkilabra:<moduuli>-valmentaja`, jonka moduulin työtiedosto poimii nimensä perusteella), ja mistä tehtävät
  tulevat (Testaa ja arvioi -tehtävät ja tasojen 1–2 ydintehtävät, vain sivun itse tarkistamat). Koodia ei ennen sitä.

## 17e. Luokan yhteenveto arviointisivulle

**Miksi:** opettaja näkee nyt pisteet opiskelija kerrallaan, mutta ei sitä, mikä tehtävä tai tavoite oli koko
ryhmälle vaikea.

**PR 1 (tiedostot `palautus/`, `scripts/palautus_tasks.py`; arviointisivu generoidaan uudelleen).**
- Uusi näkymä yhdelle ryhmälle ja lukuvälille. K8: se näytetään oletuksena lukumäärinä ilman nimiä, jotta sen voi
  näyttää luokalle; näkymän nimi ehdotetaan PR:n kuvauksessa.
  - tehtävittäin: palauttaneet, vastanneet, annettujen pisteiden jakauma ja keskiarvo, järjestys heikoimmasta;
  - tavoitteittain: itsearvion tasojen a–d ja x lukumäärät moduulisivun sormenjäljen väreissä;
  - laskutehtävittäin: oikein, lähellä ja väärin, ja väärien virhelaji 17c:n funktiolla, kun se on yhdistetty.
- Selvitä ensin, mitä `Tehtavat.gs` ja työtiedoston `chapters` jo sisältävät. Laskutehtävän oikea vastaus ja toleranssi
  lisätään generointiin tarvittaessa (ne ovat jo julkisia sivun `data-answer`-attribuutissa).
- Valintojen jakauma tehdään vain, jos tiedosto jo sisältää valinnat. Tiedostomuotoa ei muuteta tässä PR:ssä.
- Laskenta `Code.gs`:ään, jotta Apps Script -versio ja paikallinen sivu pysyvät samana koodina.
- Testit keksityillä palautuksilla: `palautus/test`, `test_palautus.py`, `palautus_tasks.py --check`.

## 17f. Hakemistot ja haku

**PR 1: kaavahakemisto.** `kaavat.py index` (tai oma skripti) lukee `docs/<moduuli>/kaavanimet.tsv`-tiedostot ja
kirjoittaa sivun `kaavat.html` joka kielelle: moduuleittain nimetyt kaavat (vain MAFY-nimet, kuten sääntö on), kaava
LaTeXina ja linkit lukuihin, joissa se esitetään. Vain kyseisessä kielessä julkaistut luvut. Nykyiset `.kaavat`-tyylit.

**PR 2: simulaatiogalleria.** `simulaatiot.html`: jokainen julkaistu luku, jolla on simulaatio (`meta.json` `sim`),
omana laattanaan (`cardgrid.py`) moduuleittain, linkki suoraan luvun Tutki-vaiheeseen. Erillisiä simulaatiosivuja ei
tehdä: simulaatio pysyy luvussaan.

**PR 3: haku.** Rakennusvaiheen indeksi `site/<kieli>/haku.json` rakennetuista sivuista: luvut (otsikko,
Miksi-kysymys, väliotsikot, luvun tärkeät käsitteet), käsitekortit, kaavat, simulaatiot, tutkimukset, TVT-ohjeet ja
yksiköt. Sivu `haku.html` ja `templates/haku.js` ilman kirjastoa; haku sietää suomen taivutuspäätteet kuten
käsitekorttien merkintä. Katso ensin `mixer.py`:n haku, jotta sivustolla on yksi hakukomponentti. Arvio noin 300 kt
kieltä kohti, pakattuna alle 100 kt.

K9 (tulkinta): uusille sivuille pääsee linkeistä Käsitteet- ja Näin opiskelet -sivuilla; valikkoon ei lisätä kohtia.
Linkkitekstit ehdotetaan PR:n kuvauksessa.

Kaikki kolme ovat generoituja sivuja: ei katselmoitavaa fysiikkaa, mutta uusi julkaistu sivu, jonka opettaja katsoo
ennen yhdistämistä.

## Järjestys (ehdotus; opettaja hyväksyy yhdistämällä)

1. 17a PR 1 ja PR 2: suojaavat kaiken, mitä selaimeen tallentuu.
2. 17b PR 1: koko työn varmuuskopio.
3. 17f PR 1 ja PR 2: generoituja sivuja, pieni riski.
4. 17c PR 1, sitten 17e (käyttää samaa funktiota).
5. 17d PR 1.
6. 17f PR 3, 17a PR 3, 17b PR 2.
7. 17c PR 2 kurssi kerrallaan sisältömuutosten yhteydessä; 17d PR 2 kohdan 11b PR 4:n jälkeen.

`lesson.js`:ää muuttava 17c PR 1 aloitetaan vasta, kun kohdan 10 PR 2–PR 5 ja kohdan 11 U1–U3 on yhdistetty (sama
tiedosto), kuten kohta 11b.

## Päätökset (opettaja 15.11.2026)

| # | Osa | Päätös |
|---|---|---|
| K1 | 17a PR 1 | Kyllä: Tietosuoja-sivulle lause verkotonta käyttöä varten tallentuvista sivuista. |
| K2 | 17a PR 3 | Kyllä: moduulin latauspainike moduulisivulle; tekstit ja paikka PR:n kuvauksessa, pilotti FY3. |
| K3 | 17b PR 1 | Kyllä: koko työn tallennus ja avaus Tietosuoja-sivun kohtaan "Mitä selaimeesi tallentuu?". |
| K4 | 17b PR 2 | Kyllä; tulkinta: jakovalikko samaan painikkeeseen. |
| K5 | 17c PR 1 | Kyllä; tulkinta: palaute käskee tarkistamaan eikä sano, että numerot ovat oikein. |
| K6 | 17c PR 2 | Kyllä; tulkinta: koordinaattori ehdottaa pilottiluvun, pilotti täydellä katselmoinnilla. |
| K7 | 17d PR 1 | Kyllä: portaat 5, 10 ja 20 vrk; aiemmin poistuneita kortteja ei ajoiteta. |
| K8 | 17e | Kyllä: luokan yhteenveto oletuksena ilman nimiä; nimi PR:n kuvauksessa. |
| K9 | 17f | Kyllä; tulkinta: linkit Käsitteet- ja Näin opiskelet -sivuilta, ei uusia valikon kohtia. |
