# FY9: adaptiivinen YO-valmentaja, kartoitus ja kehityssuunnitelma

Opettajan tehtävä 14.11.2026: kehitetään FY9-kertauskurssista (Fysiikan ylioppilaskertaus) adaptiivinen,
osaamiseen perustuva YO-valmentaja. **Ehdoton rajoitus:** opiskelijoiden käyttö ei aiheuta jatkuvia kielimallien
API-kuluja. Ei pilvipohjaista tekoälyarviointia eikä opiskelijakohtaisia maksullisia kutsuja.

Tämä on suunnitelma hyväksyttäväksi, ei toteutus. Mitään tässä ei ole vielä tehty, eikä tämä pull request muuta
muita tiedostoja kuin tämän. Hyväksytyt osat kirjataan myöhemmin työjonoon (`docs/tyojono.md`) omiksi kohdikseen.
FY9:n moduulisivun edistymiskorttien leveyskorjaus on jo työjonossa (kohta 11, U5), eikä sitä suunnitella tässä.

Lähtökohdat: repositorion tila 14.11.2026 (main `3230ad8`), `docs/FY9_PLAN.md`, `CLAUDE.md`, työjonon kohdat 13–14
ja opettajan yleislinja 14.11.: **käyttöliittymään ei lisätä tekstiä, ja uusi otsikko, ohjerivi, laskuri tai selite
vaatii opettajan luvan.** Siksi jokainen tämän suunnitelman uusi käyttöliittymäteksti on lueteltu kunkin PR:n kohdalla
ja on avoin päätös, kunnes opettaja hyväksyy sen. Julkaistuja oppikirjoja ei käytetä eikä mainita, eikä opettajan
yksityisiä referenssikokeita kopioida eikä mukailla.

Sisältö: 1 Nykytila · 2 Puutteet · 3 Arkkitehtuuri · 4 Skeemamuutokset · 5 Suosittelualgoritmi · 6 Etusivu ja
harjoittelupolku · 7 Riskit · 8 PR-järjestys · 9 Hyväksymiskriteerit ja testit · 10 YTL- ja Abitti-tietojen tarkistus ·
11 Avoimet päätökset.

## 1. Nykytilan analyysi: mitä on jo olemassa

FY9 on pidemmällä kuin tehtävänanto olettaa. Lähes kaikki tarvittava sisältö on jo olemassa ja katselmoitu; puuttuu
lähinnä *näytön kirjaaminen* ja sen *käyttö*.

### 1.1 Sisältö

| Osa | Missä | Määrä (fi) | Huomio |
|---|---|---|---|
| 16 oppituntia | `content/<kieli>/units/fy9-*/`, `local-courses.json` `FY9` | 16 + en 16 + fi-easy 16 | kuusi lukua (alla), kolme kieliversiota julkaistu |
| Lähtötasotestit | jokaisen kertaustunnin Ennusta, `lt-1`…`lt-6` | 90 monivalintaa | jokaisella vaihtoehdolla oma palaute, joka korjaa virhekäsityksen ja nimeää kerrattavan luvun |
| Koko kurssin diagnoosi | `fy9-koe` Esimerkit, `testi-1`…`testi-24` | 12 monivalintaa + 12 numeerista | kattaa FY1–FY8 |
| Lyhyet tehtävät | Esimerkit (`sovella`) ja Testaa ja arvioi (`tarkista`) | 179 monivalintaa, 86 numeerista, 15 selitystä | numeerisilla `answer`, `unit`, `tolerance`, `hints` (83/86), `mistakes` (86/86) |
| Pitkät YO-tyyliset tehtävät | `sovella/tasks.json` + `solutions.md` | 98 tehtävää, 367 osaa (202 calc, 137 word, 28 graph) | jokaisella `skills` (lukujen id:t), `links` (osaaminen → luku), kohtakohtaiset pisteytyskriteerit, mallivastaus, Yleisiä virheitä, Hyväksytään myös |
| Harjoituskoe | `fy9-harjoituskoe` | Osa I (10 kohtaa, 20 p) + 7 × 15 p + 3 × 20 p | 6 h, 120 p, aikasuunnitelma, itsearviointiohje |
| Koe ja vastaustekniikka | `fy9-koe` `unit.md` | – | kokeen rakenne, ajankäyttö, tehtävien valinta, täydellisen ratkaisun seitsemän vaihetta, kuvaajat ja kaavat koneella |
| YO-sekoitin | `scripts/mixer.py`, `site/yo-sekoitin.html` | 126 tehtävää (98 FY9 + 28 moduulien Sovella itsenäisesti) | haku, suodatus moduulin, osaamisen ja tehtävätyypin mukaan, "Arvo kolme tehtävää" |
| TVT-ohjeet | `content/<kieli>/tvt/` | 9 ohjetta | kuvaaja, sovitus, kulmakerroin, epävarmuus, taulukkolaskenta, mittausohjelma, videoanalyysi, nopeus datasta, työselostus |

FY9:n kuusi lukua: Koe ja kokeellisuus · Energia ja lämpö · Liike ja vuorovaikutus · Värähtely ja aallot · Sähkö ja
magnetismi · Moderni fysiikka (sekä Harjoituskoe omana rivinään).

**Kuusi osaamisaluetta** ovat `competencies.json`:n kuusi osaamista, joita FY9:n pisteytyskriteerit jo käyttävät:
Käsitteellinen ymmärrys (`concept`), Matemaattinen ratkaisu (`math`), Kuvaajat ja aineiston analyysi (`graph`),
Kokeellinen päättely (`experiment`), Fysikaalinen selittäminen (`communication`), Mallin valinta ja soveltaminen
(`transfer`). Jokainen pitkän tehtävän kriteeri on avain (`fbd_forces` …), jonka osaaminen luetaan `competencies.json`
`criteria`-kartasta. Tulkinta on avoin päätös P1 (kohta 11): sisältöaiheina toimivat kurssin kuusi lukua ja 16 tuntia.

### 1.2 Arviointi ja palaute, jotka ovat jo olemassa

- **Automaattinen tarkistus** (`lesson.js` osa 1, `inquiry.js`): numeerinen vastaus hyväksytään ±2 % tai puoli
  yksikköä näytetyn vastauksen viimeisessä numerossa (suurempi), 2–5 % on "Lähellä". Yritä ensin -lukko: vastaus ja
  ratkaisu avautuvat vasta yhden yrityksen jälkeen.
- **Virhekäsityspalaute on jo deterministinen**: monivalinnan jokaisella vaihtoehdolla on oma palaute, ja numeerisen
  tehtävän `mistakes` tunnistaa tyypillisen väärän arvon (esim. "kiihtyvyyden suunta väärin") ja näyttää siihen
  kirjoitetun palautteen. Tämä on juuri tehtävänannon "palaute tuotetaan etukäteen osana sisällöntuotantoa".
- **Vihjeet** ovat näkyvissä ja vapaasti avattavissa (opettaja 4.11.).
- **Avoimet vastaukset** (selitys, pitkät tehtävät) arvioi opiskelija itse mallivastausta ja kriteerejä vasten
  (`selfassess.js`: pisteet kriteeri kerrallaan, osapisteet sallittu; alle puolet pisteistä saanut osaaminen näyttää
  linkit lukuihin). Järjestelmä ei väitä arvioivansa avointa vastausta, eikä sen pidä alkaa väittää.
- **Kertausohjaus**: Testaa ja arvioi -vaiheen väärän vastauksen jälkeen ehdotus, missä harjoitella (`practice`).

### 1.3 Tallennus selaimessa (vain tämä laite, mitään ei lähetetä)

| Avain | Kirjoittaja | Sisältö |
|---|---|---|
| `ruukkilabra:<sivu>` | `lesson.js` osa 2 | tehdyt vaiheet `done`, `of` (Jatka-rivi, vaihepalkki) |
| `ruukkilabra:viimeisin` | `lesson.js` | viimeksi avattu luku ja vaihe |
| `ruukkilabra:tarkistettu` | `lesson.js` 1b | `{tehtävä: {parts, of, done}}`: mitkä kohdat on tarkistettu, **ei tulosta** |
| `ruukkilabra:ratkaistu` | `padstore.js` | ratkaisun ensimmäinen tallennus |
| `ruukkilabra:vastaukset:<sivu>` | `lesson.js` | kirjoitetut vastaukset, valinnat |
| `ruukkilabra:itsearvio:<luku>` | `inquiry.js` osa 8 | tavoitteiden tasot a–d/x historioineen |
| `fl:<sivu>:<rubriikki>` | `selfassess.js` | itsearvioidut kriteeripisteet, **ilman aikaleimaa** |
| `ruukkilabra:tehty` | `tehty.js` | annettujen tehtävien Tehty-rastit lokeineen |
| `ruukkilabra:kortit` | `kortit.js` | käsitekorttien kertauspakka (kolme Osasin peräkkäin) |
| IndexedDB | `padstore.js` | ratkaisueditorin ratkaisut (Digabi-editori, kaavat, kuvat) |

**Varmuuskopio on jo olemassa:** moduulisivun ja jokaisen luvun *Tallenna työ tiedostoon* / *Avaa tallennettu työ*
(`palautus.js` `courseWork`, muoto `ruukkilabra-tyo` v1) kokoaa opintojakson kaikki avaimet, joiden nimessä on
`fy9-…`, sekä ratkaisut yhteen tiedostoon ja palauttaa ne toisella laitteella. Lisäksi ratkaisueditorilla on oma
vienti (`ruukkilabra-ratkaisut` v1). Tietosuojasivu (`site/tietosuoja.html`) kuvaa tallennuksen.

**Valmiit edistymisnäkymät FY9:n sivulla:** Jatka-rivi ja luvun "3/7 vaihetta" (`jatka.js`), Oma eteneminen
(`tehty.js`: tehdyt tehtävät, kuvaaja), Oma itsearvio (`omaarvio.js`: tavoitteiden "sormenjälki"), tasojen "3/8 tehty".
Nämä mittaavat *tekemistä*, eivät *osaamista*, ja juuri tämä ero puuttuu.

### 1.4 Tapahtumaväylä, jota voi hyödyntää

Jokainen yritys lähettää jo tapahtuman `fl:attempt` `{id, kind: check|choice|done, state: ok|close|no|done}`
(`lesson.js`). Uusi koodi voi kuunnella sitä koskematta tehtäviin. Tapahtumasta puuttuvat: mikä `mistakes`-arvo tai
vaihtoehto osui, oliko yritys ensimmäinen, ja onko vihje avattu.

### 1.5 Kieliversiot, katselmointi ja CI

- fi, en ja fi-easy: tehtävien id:t ovat samat kaikissa kielissä (`test_unit_i18n.py`), joten näyttö voidaan avata
  kielestä riippumattomilla avaimilla, kuten itsearvio jo tekee.
- Katselmointi: yksikön sisältötiivisteeseen kuuluvat `inquiry.json`, `unit.md`, `sovella/` ja kuvat. Mikä tahansa
  muutos niissä vanhentaa katselmoinnit, ja `reviews.py scope` päättää, kuka katsoo uudelleen (delta tai täysi).
  Skriptit, templatet, `lang/` ja konfiguraatio eivät vanhenna katselmointeja. Sivutiedosto sisältöhakemistojen
  ulkopuolella (kuten `example-names.json` ja `kortit/`) ei vanhenna mitään.
- CI: jaettu muutos (`scripts/`, `templates/`, `lang/`) testaa PR:ssä koko sivuston selaintestit, mainissa SMOKE-otoksen
  ja nimetyt sivut; viikkoajo testaa kaiken. Olemassa: `test_progress`, `test_jatka`, `test_tehty`, `test_palautus`,
  `test_practice`, `test_unit_i18n`, `test_writepad`, `check_layout` (8 leveyttä), `check_a11y`, `test_home`.

## 2. Puutelista: mitä pitää aidosti rakentaa

| # | Puute | Miksi | Koko |
|---|---|---|---|
| A | **Näyttöloki**: tulos (oikein / lähellä / väärin / itsearvioidut pisteet), ensimmäinen yritys, vihjeen käyttö, osunut virhearvo, aika | nyt tallentuu vain "tarkistettu", ei tulosta; ilman tätä ei voi erottaa avaamista, yrittämistä ja osaamista | keskikokoinen, jaettu |
| B | **Kielestä riippumaton tehtävätunniste** `<yksikkö>#<id>` | lyhyiden tehtävien id:t (`lt-1`, `tarkistus-2`) toistuvat joka yksikössä, ja `ruukkilabra:tarkistettu` käyttää paljasta id:tä: 16 yksikön `lt-1` sekoittuvat samaksi avaimeksi (tarkistettava, ks. riski R9) | pieni |
| C | **Tehtäväindeksi** (koneluettava luettelo kaikista FY9-tehtävistä: yksikkö, osaaminen, tyyppi, arvioitu aika, tarkistustapa, julkaisutila kielittäin) | suosittelija tarvitsee tehtävät yhdestä paikasta; sekoitin listaa vain pitkät tehtävät HTML:nä | pieni, build-skripti |
| D | **Osaamisnäkymä** kuudelle osaamisalueelle ja kuudelle luvulle, sanallinen ja epävarmuuden näyttävä | ei ole | keskikokoinen |
| E | **Suosittelija** (enintään 3 tehtävää, syy näkyvissä, deterministinen) | sekoittimen "Arvo kolme" on satunnainen | keskikokoinen |
| F | **Vaikean ratkaisuvaiheen ilmoitus** (seitsemän vaiheen kiinteä sanasto) | ei ole | pieni, UI-tekstiä |
| G | **Koetila ja minikokeet 30 / 60 min**: ajastin, vihjeet ja mallivastaukset lukossa loppuun asti, tehtävien valinta, ajankäytön kirjaus | harjoituskokeessa ohje on vain tekstinä ("älä avaa mallivastauksia"), ei teknistä lukkoa eikä ajanottoa | suurin osa |
| H | **Kertauspolku 2 / 4 viikkoa**, päivän kohtuullinen määrä, kertausvälit | ei ole | keskikokoinen |
| I | **Abitti 2 -taidot**: ajantasainen ohje ja harjoitukset kokeen työkaluilla | `fy9-koe` kuvaa kaavaeditorin ja kuvaajat yleisesti; Abitti 2:n työkalut on tarkistettava (kohta 10) | sisältö, täysi katselmointi |
| J | **YTL-tietojen tarkistus** `fy9-koe`:ssa ja harjoituskokeessa lähteineen | teksti on jo varovainen ("tarkista ajantasainen rakenne"), mutta lähdettä ei ole kirjattu | pieni sisältö, delta |
| K | Paikallisen kielimallin **selvitys** (ei toteutusta) | tehtävänanto 6 | pelkkä dokumentti |

**Ei rakenneta uudelleen:** tehtäviä, mallivastauksia, kriteerejä, virhekäsityspalautteita, vihjeitä, YO-sekoitinta,
varmuuskopiota (työtiedosto riittää, kun uusi avain nimetään oikein), Jatka-riviä, käsitekorttien kertauspakkaa,
harjoituskoetta sinänsä, ratkaisueditoria.

**Pieni sisältöpuute:** kolmelta numeeriselta tehtävältä puuttuvat vihjeet (83/86). Ei vaadi omaa PR:ää; korjataan,
kun kyseinen yksikkö muuttuu muutenkin.

## 3. Suositeltu tekninen arkkitehtuuri

Periaate: **staattinen sivusto, build-vaiheen indeksi, yksi selainmoduuli, kaikki tila selaimessa.** Ei palvelinta,
ei tunnuksia, ei API-avaimia, ei kielimallia ajon aikana. Kaikki toimii GitHub Pagesissa sellaisenaan.

```
build (python, CI)                                  selain (opiskelijan laite)
-------------------                                 ---------------------------------------------
content/*/units/fy9-*  ─┐                           FY9-yksikön sivu ── fl:attempt, vihje, rubriikki ─┐
kertaus/FY9.json ───────┼─ scripts/valmentaja.py ─> site/<kieli>/valmentaja/fy9.json (tehtäväindeksi)  │
competencies.json ──────┘    (check, build)                    │                                       v
                                                               └──> templates/valmentaja.js <── ruukkilabra:fy9-valmentaja
                                                                    (kirjaus · osaamismalli · suosittelu · polku · koetila)
                                                                    näkymät: FY9.html (yksi rivi), FY9-valmentaja.html,
                                                                    fy9-minikoe-*.html, harjoituskokeen koetila
```

### 3.1 Osat

1. **`kertaus/FY9.json`** (uusi sivutiedosto, sisältöhakemistojen ulkopuolella kuten `kortit/`, ei vanhenna
   katselmointeja): vain se metatieto, jota ei voi päätellä olemassa olevasta sisällöstä (kohta 4). Opettaja hyväksyy
   sen PR:n yhdistämisellä; `valmentaja.py check` tarkistaa sen deterministisesti.
2. **`scripts/valmentaja.py`**: lukee yksiköt, `competencies.json`:n ja sivutiedoston ja kirjoittaa jokaiselle kielelle
   tehtäväindeksin `site/<kieli>/valmentaja/fy9.json` (vain kyseisessä kielessä julkaistut yksiköt, kuten
   `mixer.items` jo tekee). `check` epäonnistuu, jos sivutiedosto viittaa tehtävään, jota ei ole, tai jos minikokeen
   aika- tai pistebudjetti ei täsmää. Arvioitu koko noin 380 tehtävää × ~200 tavua ≈ 80 kt per kieli (gzip ~15 kt).
3. **`templates/valmentaja.js`** (yksi moduuli, neljä osaa, kuten muutkin templatet):
   (a) *kirjaus* FY9-yksikön sivuilla: kuuntelee `fl:attempt`-tapahtumaa, vihjeen avausta (`.hints details.hint` `toggle`),
   rubriikin muutosta ja "Olen tehnyt ratkaisun" -rastia ja kirjoittaa näyttölokiin;
   (b) *osaamismalli* ja (c) *suosittelu*: puhtaita funktioita (syöte: loki + indeksi + päivämäärä; tulos: tilat ja
   suositukset), joita testit ajavat kiinteillä aineistoilla;
   (d) *näkymät*: FY9-sivun rivi, valmentajasivu, koetila. Ilman JavaScriptiä sivut ovat kuten nyt.
4. **Pienet lisäykset olemassa olevaan** (jaettuja, eivät muuta käytöstä): `fl:attempt`-tapahtuman `detail`iin
   `first` (ensimmäinen yritys), `mistake` (osuneen `mistakes`-rivin indeksi) ja `choice` (valitun vaihtoehdon indeksi);
   `selfassess.js` lähettää `fl:rubric {id, got, max, crit}`. Tapahtuman nykyiset kentät ja kaikki tallennusavaimet
   pysyvät ennallaan.
5. **Tallennus**: yksi uusi avain **`ruukkilabra:fy9-valmentaja`**. Nimi on valittu niin, että nykyinen työtiedosto
   (`palautus.js` `KEY_RE`, joka poimii `…:fy9-…`) ottaa sen mukaan ilman muutosta: vienti ja tuonti toimivat heti, ja
   testi varmistaa sen. Mitään vanhaa avainta ei kirjoiteta uudelleen eikä muunneta.

### 3.2 Miksi näin

- **Sisältöä ei kosketa** kirjaukseen, malliin eikä suositteluun: tehtävien hyväksytyt tiede-, pedagogiikka- ja
  visuaaliset katselmoinnit pysyvät voimassa. Ainoat sisältömuutokset ovat J (YTL-tiedot), I (Abitti 2) ja mahdolliset
  uudet jatkotehtävät, ja niille `reviews.py scope` antaa delta- tai täyden katselmoinnin.
- **Selitettävyys**: malli ja suosittelu ovat muutaman kymmenen rivin aritmetiikkaa, jonka jokainen luku näkyy
  opiskelijalle syynä ("viimeksi 9 päivää sitten", "kaksi kolmesta väärin") ja testeissä kiinteänä odotusarvona.
- **Kustannus nolla ajon aikana**: kaikki laskenta selaimessa, data staattisena tiedostona.
- **Kieliversiot**: indeksi on kielittäin, näyttö kielestä riippumaton (`<yksikkö>#<id>`), joten fi-easy- tai
  en-sivulla tehty tehtävä näkyy samassa osaamisnäkymässä.
- **Laajennettavuus**: sama moduuli voi myöhemmin palvella moduulien Sovella itsenäisesti -tehtäviä (sekoittimen 28
  tehtävää), mutta ensimmäinen versio rajataan FY9:ään.

## 4. Tehtävä- ja osaamistietojen skeemamuutokset

**Tavoite: ei pakollisia muutoksia `inquiry.json`- tai `tasks.json`-skeemaan.** Lähes kaikki päätellään olemassa
olevasta, ja loput kirjataan sivutiedostoon.

### 4.1 Päätellään (ei uutta kenttää)

| Tieto | Mistä |
|---|---|
| tehtävän tunniste | `<yksikkö>#<activity id>` tai pitkän tehtävän `fy9-<yksikkö>-s<n>` (+ `#<osa>`) |
| aihe | yksikkö ja sen luku `local-courses.json` `FY9.chapters` |
| osaaminen, pitkä tehtävä | kohtien kriteeriavaimet → `competencies.json` `criteria` (pisteillä painotettuna) |
| osaaminen, lyhyt tehtävä | oletus tyypistä: `choice` → `concept`, `numeric` → `math`, `interpret` → `graph`, `explain` → `communication` |
| tarkistustapa | `numeric`, `choice` → automaattinen; `explain`, pitkät → itsearvio |
| kokeen osa | pitkä tehtävä 15 p → Osa II -tyyppi, 20 p → Osa III -tyyppi; lyhyet → Osa I -tyyppi |
| arvioitu aika | pitkä: pisteet × 3 min (6 h / 120 p; YTL-tarkistus kohta 10); numeerinen 4 min, monivalinta 2 min, selitys 5 min |
| kerrattavat luvut | `skills`, `links`, `practice` ja palautteen lukulinkit |
| virhekäsitys | valittu vaihtoehto tai osunut `mistakes`-rivi; palautteen teksti on jo olemassa |

### 4.2 Sivutiedosto `kertaus/FY9.json` (uusi, ei katselmointitiivisteessä)

```json
{
  "version": 1,
  "items": {
    "fy9-koe#testi-7":      { "unit": "fy9-voimat" },
    "fy9-voimat#lt-3":      { "competencies": ["concept", "transfer"] },
    "fy9-voimat#nosturi":   { "minutes": 6, "followups": ["fy9-voimat#vinoveto", "fy9-sailymislait#tarkistus-2"] }
  },
  "misconceptions": {
    "voima-liikkeen-suuntaan": { "items": ["fy9-voimat#lt-1/1", "fy9-liike#lt-4/2"] }
  },
  "minikokeet": [
    { "id": "m30-liike", "minutes": 30, "short": ["fy9-liike#tarkistus-2", "…"], "long": [], "choose": null },
    { "id": "m60-1", "minutes": 60, "short": ["…"], "long": ["fy9-voimat-s2", "fy9-energia-s3"], "choose": 1 }
  ],
  "plans": { "2": { "days": 14 }, "4": { "days": 28 } }
}
```

- `items`: vain poikkeukset päätelmistä. Diagnoositehtävät (`fy9-koe#testi-n`) tarvitsevat `unit`-kentän, koska ne
  kertaavat muita yksiköitä.
- `followups`: jatkoharjoitus, joka suositellaan virheen jälkeen ennen muita. Viittaa vain olemassa oleviin tehtäviin.
- `misconceptions`: valinnainen ryhmittely, jolla sama virhekäsitys tunnistetaan eri tehtävissä
  (`<tehtävä>/<vaihtoehdon tai mistakes-rivin indeksi>`). **Ei uutta opiskelijalle näkyvää tekstiä**: näkymä näyttää
  osuneen vaihtoehdon olemassa olevan, katselmoidun palautteen. Siksi tiedosto ei tarvitse tiede- tai
  pedagogiikkakatselmointia; opettaja hyväksyy ryhmittelyn PR:ssä.
- `minikokeet`: kiinteät koekoosteet (kohta 6.4); `check` laskee aika- ja pistebudjetin.
- `plans`: polkujen pituudet; päiväkohtainen sisältö lasketaan (kohta 5.4).

### 4.3 Valinnaiset sisältömuutokset (katselmoidaan)

- **Ratkaisuvaiheet**: ei tehtäväkohtaista dataa. Opiskelija valitsee vaikean vaiheen kiinteästä sanastosta, joka on
  kurssin jo opettama täydellisen ratkaisun seitsemän vaihetta (`fy9-koe`, CLAUDE.md Lesson form 7): annetut ja
  kysytty · periaate · yhtälö symboleilla · yksikkömuunnokset · sijoitus · vastaus ja tarkkuus · järkevyys. Lisäksi
  "tehtävän tulkinta" ja "kuvaaja". Tekstit `lang/<kieli>.json`:iin kerran (UI-teksti, opettajan lupa).
- **Uudet jatkotehtävät** vain, jos `valmentaja.py report` osoittaa aiheen ja osaamisen solun, jossa ei ole yhtään
  automaattisesti tarkistettavaa tehtävää. Ne kirjoitetaan normaalisti yksikön `inquiry.json`:iin olemassa olevalla
  skeemalla, ja katselmointi on delta (`reviews.py scope`).
- **Virhekäsitysten tunnisteet sisältöön** (esim. `mistakes[].id`) eivät ole tarpeen; sivutiedosto riittää eikä
  vanhenna katselmointeja.

### 4.4 Näyttölokin muoto (`ruukkilabra:fy9-valmentaja`)

```json
{ "v": 1,
  "log": [["2026-11-20T18:04Z", "fy9-voimat#nosturi", "a", "ok", 1, 0, null, "p"]],
  "cells": { "fy9-voimat|math": { "next": "2026-11-23", "step": 2 } },
  "steps": { "fy9-voimat-s1#b": ["sijoitus"] },
  "plan": { "days": 28, "start": "2026-11-20", "perDay": 40, "weekdays": [1,2,3,4,6] },
  "exams": [{ "id": "m60-1", "start": "…", "end": "…", "chosen": ["fy9-energia-s3"], "times": {"…": 1260} }] }
```

Lokirivi: aika, tehtävä, tapa (`a` automaattinen, `s` itsearvio), tulos (`ok`/`close`/`no` tai pisteosuus 0–1),
ensimmäinen yritys (1/0), vihjeitä avattu (lukumäärä), osunut virhe (indeksi tai `null`), tila (`p` harjoitus, `k`
koe). Loki rajataan 3 000 riviin; vanhimmat tiivistetään `cells`-yhteenvetoon. Ei nimeä, ei laitetunnistetta, ei
tekstisisältöä, ei IP:tä: vain se, mitä malli tarvitsee.

## 5. Adaptiivisen suosittelualgoritmin toimintaperiaate

Deterministinen, muutama sääntö, jokainen luku näkyvissä syynä. Ei satunnaisuutta (tasapelit ratkaistaan
järjestyksellä), ei koneoppimista, ei tekoäly-API:a.

### 5.1 Näytön paino yhdelle yritykselle

| Tilanne | Tulos *r* | Luotettavuus *w* |
|---|---|---|
| automaattinen, ensimmäinen yritys oikein, ei vihjettä | 1,0 | numeerinen 1,0 · monivalinta 0,7 (arvaus mahdollinen) |
| automaattinen, oikein vihjeen jälkeen | 0,6 | kuten yllä |
| numeerinen "Lähellä" | 0,5 | 1,0 |
| automaattinen, väärin | 0 | kuten yllä |
| monivalinta, oikein vasta toisella valinnalla | 0,2 | 0,7 |
| itsearvioitu rubriikki | saadut / enimmäispisteet | 0,6 |
| selitystehtävän kriteerit (oma rasti) | rastitut / kaikki | 0,4 |
| koetila (ei vihjeitä, aikaraja) | kuten yllä | × 1,2 |
| sama tehtävä uudelleen (7 vrk sisällä) | kuten yllä | × 0,5 |

Vain ensimmäinen yritys kirjataan tulokseksi; myöhemmät yritykset ovat harjoittelua, eivät uutta näyttöä
(muuten oikea vastaus palautteen jälkeen nostaisi osaamista perusteetta).

### 5.2 Osaamisen tila solulle (aihe × osaaminen)

Solu on yksi 16 yksiköstä × yksi kuudesta osaamisesta. *W* = solun painojen summa (viimeiset 6 yritystä), *M* =
painotettu keskiarvo (uusin paino 1, sitä edeltävät 0,8, 0,64, …).

| Tila (ehdotettu sana, UI-teksti) | Ehto |
|---|---|
| Ei vielä näyttöä | *W* = 0 |
| Näyttöä vähän | 0 < *W* < 2 |
| Harjoittele | *W* ≥ 2 ja *M* < 0,5 |
| Kehittyy | *W* ≥ 2 ja 0,5 ≤ *M* < 0,8 |
| Vahva | *W* ≥ 3, *M* ≥ 0,8, näyttö vähintään kahtena eri päivänä **ja** vähintään yksi automaattinen tai koetilan tulos |
| Vahva, kertaa pian | Vahva, mutta kertauspäivä on ohitettu |

- **Ei prosentteja eikä arvosanoja.** Näkymä näyttää sanan ja sen, mihin se perustuu ("5 tehtävää, 3 päivänä").
- **Pelkkä itsearvio ei koskaan riitä tilaan Vahva**; itsearvioon perustuva tila merkitään "oman arvion mukaan".
- **Osaamisalueen yhteenveto** (kuusi riviä): kuinka monessa aiheessa alue on Vahva, Kehittyy, Harjoittele tai ilman
  näyttöä. Ei keskiarvoa yli aiheiden, koska se kätkisi juuri puutteet.

### 5.3 Kertausväli

Kun solun uusin tulos on *r* ≥ 0,8, kertausväli kasvaa portaittain 2 → 5 → 10 → 20 vrk; kun *r* < 0,5, väli palaa
1 vrk:een; muuten väli pysyy. Neljän viikon polkuun mahtuu siten 3–4 kertausta samasta asiasta, kahden viikon
polkuun 2–3. Käsitekorttien oma kertauspakka (`kortit.js`) jää ennalleen; valmentaja voi linkittää siihen.

### 5.4 Suosittelu: enintään kolme tehtävää

Ehdokkaat: tämän kielen indeksin tehtävät, joita ei ole tehty 7 vrk:n sisällä ja joiden arvioitu aika mahtuu päivän
jäljellä olevaan aikaan. Jokaiselle ehdokkaalle *i* (solu *c*):

```
tarve(c)     = 1 − M(c);  jos W(c) = 0: 0,6   (tuntematon on keskitasoa, ei tärkein)
erääntynyt(c)= 1, jos kertauspäivä on tänään tai ohi; muuten 0
polku(i)     = 1, jos yksikkö kuuluu tämän päivän polkuun; muuten 0
jatko(i)     = 1, jos i on followup tehtävälle, joka meni väärin viimeisen 3 vrk:n aikana
uusi(i)      = 1 tekemätön · 0,3 tehty yli 7 vrk sitten
pisteet(i)   = 3·tarve + 2·erääntynyt + 1,5·polku + 2·jatko + 1·uusi
```

Valinta: suurimmat pisteet; korkeintaan yksi tehtävä samasta solusta ja kaksi samasta yksiköstä; jos jonkin solun
tarve ≥ 0,5, joukossa on vähintään yksi automaattisesti tarkistettava tehtävä (nopea palaute). Tasapelit:
yksikön järjestys kurssilla, sitten tehtävän järjestys sivulla. Jokaisella suosituksella näkyy yksi syy, suurimman
termin mukaan, kiinteästä listasta: "Kertaus: edellisestä 9 päivää", "Edellinen yritys meni väärin", "Tämän päivän
aihe", "Et ole vielä tehnyt tätä aihetta". **Ensimmäisellä käyttökerralla** ei suositella mitään ennen
diagnoosia: tarjotaan `fy9-koe`:n 24 kohdan diagnoosi tai yksikön lähtötasotesti.

**Vapaa harjoittelu säilyy aina**: jokaisen suosituksen vieressä on linkki YO-sekoittimeen ja kurssin kaikkiin
tunteihin. Suositus ei lukitse mitään.

### 5.5 Kertauspolku

Syöte: kesto 14 tai 28 vrk (tai koepäivä), harjoituspäivät viikossa, minuutit päivässä (20 / 40 / 60). Polku jakaa
15 kertaustuntia (2–15) päiville luvuittain: ensin diagnoosissa heikoimmat luvut, sitten loput kurssin järjestyksessä,
viimeisellä viikolla vain kertauksia ja minikokeet. Esimerkki, 28 vrk, 5 päivää viikossa, 40 min:

| Viikko | Sisältö |
|---|---|
| 1 | diagnoosi (30 min) · heikoimmat 4 tuntia: lähtötasotesti + Esimerkit + 1 pitkä tehtävä · minikoe 30 min |
| 2 | seuraavat 5 tuntia · erääntyneet kertaukset · minikoe 30 min |
| 3 | viimeiset 5 tuntia · kertaukset · minikoe 60 min |
| 4 | vain kertaukset ja suositukset · minikoe 60 min · harjoituskoe (6 h, erillinen päivä) |

Päivän määrä: tehtäviä lisätään, kunnes arvioitu aika ylittäisi päivän minuutit; suosituksia on silti enintään
kolme kerrallaan. Väliin jäänyt päivä ei kasaa rästejä: polku siirtyy, ja erääntyneet kertaukset priorisoituvat.
Ei ilmoituksia, ei sähköpostia, ei tunnuksia.

## 6. FY9-opiskelijan etusivu ja harjoittelupolku

Lähtökohta: FY9.html pysyy rauhallisena (yleislinja: ei lisätekstiä). Valmentaja saa oman sivun, ja kurssisivulle
tulee vain yksi rivi ja yksi laatta.

### 6.1 Kurssisivu `FY9.html`

- Jatka-rivin paikalle (tai sen alle, avoin päätös P4) yksi rivi, kuten Jatka: **"Tänään: 3 tehtävää · ~35 min"** ja
  painike, joka avaa valmentajan. Ennen ensimmäistä yritystä rivi tarjoaa diagnoosia. Ei mitään ennen kuin opiskelija on
  aloittanut, kuten Jatka-rivillä.
- Moduulin loppulaattoihin (Kertauspakkasi, Esimerkkikoe …) yksi laatta **Valmentaja** samalla kuvituksen ja koon
  säännöllä (`build.py end_tiles`). Kuvitus `assets/shared/module-end/` -tyyliin; opettaja hyväksyy kuvan.
- Lukukortit, Oma eteneminen ja Oma itsearvio pysyvät ennallaan. U5 (korttien leveys) tehdään erikseen.

### 6.2 Valmentajasivu `FY9-valmentaja.html` (myös `en/`, `fi-easy/`)

Yksi lukupalsta, ylhäältä alas, puhelimella sama järjestys:

1. **Seuraavaksi** (enintään 3 korttia): tehtävän nimi, tunti ("Luku 3.2 Newtonin lait ja voimakuvio"), arvioitu aika,
   syy yhdellä rivillä, linkki suoraan tehtävään (`fy9-voimat.html#nosturi`). Alla linkki **Harjoittele vapaasti**
   (YO-sekoitin ja kurssin tunnit).
2. **Osaamisalueet** (suljettu laatikko, avautuu): kuusi riviä, jokaisella sana ja peruste. Avattuna rivistä näkyvät
   aiheet ja niiden tilat ruudukkona (16 × 6, värit + sana + kuvio, ei pelkkä väri). Solua napauttamalla saa sen
   tehtävät.
3. **Toistuvat virheet** (suljettu laatikko, näkyy vain kun on): sama virhekäsitys vähintään kahdesti; näyttää osuneen
   vaihtoehdon olemassa olevan palautteen ja linkin lukuun.
4. **Kertauspolku**: kesto, päivät, minuutit (kolme valintaa) → tämän viikon päivät listana. Muokattavissa ja
   poistettavissa.
5. **Minikokeet**: 30 ja 60 minuutin koosteet ja harjoituskoe, kustakin viimeisin suoritus (päivä, oma pistemäärä,
   ajankäyttö osittain).
6. **Tietosi**: "Tallenna työ tiedostoon" / "Avaa tallennettu työ" (olemassa oleva komponentti) ja *Tyhjennä
   valmentajan tiedot* vahvistuksella.

### 6.3 Yksikön sivulla (pieni)

- Pitkän tehtävän ja numeerisen tehtävän ratkaisun avauduttua rivi **"Mikä vaihe oli vaikea?"** kiinteällä
  sirulistalla (kohta 4.3), valinnainen, ei pakota mitään. Tallentuu `steps`-kenttään ja näkyy valmentajassa.
- Kirjaus toimii näkymättömästi; sivun ulkoasu ei muutu.

### 6.4 Minikokeet ja koetila

| Kooste | Rakenne | Pisteet | Harjoittelee |
|---|---|---|---|
| 30 min, "Osa I" | 6 lyhyttä kohtaa (monivalinta, väite, lyhyt lasku), vastaa viiteen | 10 p | nopeat kohdat, ohittaminen |
| 30 min, aihe | yhden luvun 5 lyhyttä kohtaa (kuusi koostetta, yksi per luku) | 10 p | heikon luvun kertaus koeoloissa |
| 60 min | 3 lyhyttä kohtaa + valitse 1 kahdesta Osa II -tyypin tehtävästä | 6 + 15 p | tehtävän valinta, 40 min tehtävä |
| 60 min, aineisto | valitse 1 kahdesta Osa III -tyypin aineistotehtävästä | 20 p | kuvaaja, sovitus, työkalut |
| 6 h | nykyinen harjoituskoe koetilassa | 120 p | koko koe |

Pistemäärät noudattavat suhdetta 3 min/p (tarkistettava, kohta 10). Koosteet ovat **kiinteitä** (sivutiedosto),
eivät satunnaisia: ne voi tarkistaa, testata ja katselmoida kerran, ja opiskelija voi tehdä saman uudelleen.

Koetila (yhteinen harjoituskokeelle ja minikokeille):

- Aloita-painike → ajastin (näkyvä, pysäytettävä, ei äänimerkkiä; `prefers-reduced-motion`), tehtävien luku ja valinta
  ensin. Valinta merkitään ennen vastaamista; valitsemattomien tehtävien mallivastauksia ei voi laskea mukaan.
- **Vihjeet, Lähellä-palaute, virhepalaute ja mallivastaukset eivät ole käytössä ennen kuin opiskelija painaa
  Lopeta koe tai aika loppuu.** Mallivastaukset ovat sivulla `<template>`-elementeissä, jotka lisätään näkyviin vasta
  lopussa (ilman JavaScriptiä sivu näyttää ohjeen, ettei koetila ole käytössä).
- Ajankäyttö: jokaisella tehtävällä *Aloita tämä* / siirtyminen kirjaa ajan tehtävälle; lopussa taulukko "suunniteltu /
  käytetty" kuten harjoituskokeen aikasuunnitelma jo neuvoo kirjaamaan käsin.
- Lopussa: automaattisesti tarkistettavat kohdat tarkistetaan (vain ensimmäinen vastaus), pitkät arvioidaan nykyisellä
  rubriikilla; tulokset lokiin tilalla `k`.
- Vastaukset kirjoitetaan nykyiseen ratkaisueditoriin (Digabi-editori, `lesson.js` osa 6), joten kaavaeditorin käyttö
  harjoittuu samalla.
- Minikoesivut `fy9-minikoe-<id>.html` rakennetaan olemassa olevilla renderöijillä vain julkaistusta, katselmoidusta
  sisällöstä (kuten sekoitin), eikä tehtävätekstiä kopioida mihinkään lähteeseen.

### 6.5 Abitti 2 -taidot

Ei omaa simulaatiota Abitista. Kaksi osaa, molemmat vasta YTL- ja Abitti-tietojen tarkistuksen (kohta 10) jälkeen:

1. Uusi TVT-ohje (`content/<kieli>/tvt/`, katselmoidaan kuten muut) *Fysiikan koe Abitti 2:ssa*: vastauksen rakenne,
   kaavaeditori, kuvaajan teko ja sovitus kokeen ohjelmilla, kuvakaappauksen liittäminen, taulukot ja
   kaavakokoelma, ajanhallinta. Linkitetään `fy9-koe`:sta ja aineistotehtävistä; olemassa olevat ohjeet (kuvaaja,
   sovitus, taulukkolaskenta) linkitetään, ei kopioida.
2. 60 minuutin aineistominikoe ohjeistetaan tehtäväksi kokeen työkaluilla (ilmainen GeoGebra ja taulukkolaskenta
   omalla koneella; Abitti 2 -harjoitusympäristö, jos koulu sen tarjoaa), ja koetilan lopussa itsearvioidaan myös
   "kuvaaja tehty ohjelmalla, akselit ja yksiköt".

### 6.6 Opiskelijan polku yhdellä silmäyksellä

```
FY9.html ── "Aloita: diagnoosi" ──> fy9-koe (24 kohtaa) ──> Valmentaja: tilat, 3 suositusta, polku
     ^                                                            │
     └──── päivittäin: "Tänään: 3 tehtävää" ── tehtävä yksikön sivulla ── loki ──┘
                                      viikoittain: minikoe 30/60 ── lopussa: harjoituskoe 6 h
```

## 7. Riskit

### 7.1 Tietosuoja

| Riski | Torjunta |
|---|---|
| R1 jaettu koulukone: seuraava käyttäjä näkee edellisen tiedot | Tyhjennä-painike valmentajassa; tietosuojasivulle maininta; ei nimiä, ei tekstisisältöä lokissa |
| R2 uusi tallennus muuttaa tietosuojasivun sisältöä | tietosuojasivu päivitetään samassa PR:ssä kuin kirjaus (luettelo tallennettavasta) |
| R3 työtiedosto opettajalle palautettaessa sisältää nyt myös näyttölokin | lokissa ei ole henkilötietoja; tietosuojasivu ja `palautus/TIEDOSTOMUOTO.md` kertovat sen; avoin päätös P6, otetaanko loki palautukseen vai vain varmuuskopioon |
| R4 tuotu tiedosto on haitallinen tai rikki | olemassa olevan työtiedoston validointi; loki tarkistetaan skeemaa vasten, ei koskaan `innerHTML`, kokoraja |
| R5 "Never add tracking": loki voisi näyttää seurannalta | mitään ei lähetetä; ei analytiikkaa; CI-testi, että valmentaja.js ei kutsu `fetch`/`XMLHttpRequest`/`sendBeacon` muuhun kuin omaan indeksiin |

### 7.2 Virheellinen osaamisen arviointi

| Riski | Torjunta |
|---|---|
| R6 arvattu monivalinta näyttää osaamiselta | paino 0,7, vain ensimmäinen yritys, Vahva vaatii kaksi päivää ja vähintään 3 painopistettä |
| R7 itsearvion yliarviointi | paino 0,6; pelkkä itsearvio ei anna tilaa Vahva; merkintä "oman arvion mukaan" |
| R8 tehtävän ulkoa muistaminen | uusinta 7 vrk sisällä painolla 0,5, suosittelija välttää tehtyä tehtävää |
| R9 tunnistetörmäys: `lt-1` 16 yksikössä | uusi loki käyttää aina `<yksikkö>#<id>`; nykyisen `ruukkilabra:tarkistettu`-avaimen törmäys tarkistetaan PR 2:ssa ja korjataan tarvittaessa omana pienenä PR:nä (vanhaa avainta ei kirjoiteta uudelleen) |
| R10 osaamisen tila koetaan arvosanaksi | ei prosentteja, ei arvosanoja, sanat ja peruste; teksti "perustuu tähän laitteeseen tehtyihin tehtäviin" |
| R11 väärä osaamistunniste (esim. monivalinta, joka on oikeasti `transfer`) | oletukset + sivutiedoston poikkeukset; `valmentaja.py report` listaa solut opettajan tarkistettaviksi |
| R12 toleranssi hyväksyy väärän tai hylkää oikean | olemassa oleva toleranssisääntö ja `answers.py`; valmentaja ei muuta tarkistusta |
| R13 suosittelija jumittuu yhteen aiheeseen | enintään yksi per solu ja kaksi per yksikkö; polku pakottaa uuden aiheen; testi kiinteillä lokeilla |

### 7.3 Testaus

- Algoritmi testataan **kiinteillä lokeilla** (golden-tiedostot): annettu loki ja päivämäärä → täsmälleen odotetut
  tilat ja kolme suositusta syineen. Muutos painoihin näkyy testin muutoksena, ei huomaamatta.
- Selain ilman tallennusta (yksityinen tila, estetty localStorage, kiintiö täynnä): sivu toimii, valmentaja sanoo,
  ettei tietoja voi tallentaa.
- Kaksi välilehteä (`storage`-tapahtuma), kellonajan vaihtuminen yön yli, aikavyöhyke (päivä paikallisena päivänä).
- Koetilan lukot: testi, että vihjeet, Lähellä-palaute ja mallivastaukset eivät ole DOM:ssa näkyvinä ennen Lopeta.
- `check_layout` kaikilla kahdeksalla leveydellä valmentajasivulle, minikoesivuille ja muuttuneille yksikkösivuille;
  `check_a11y` (näppäimistö, kohdistus, `aria-live` ajastimelle harvoin, ruudukko taulukkona).
- Riski: jaettu muutos ajaa koko sivuston selaintestit; siksi jaetut PR:t pidetään pieninä ja yksi kerrallaan.

### 7.4 Kustannukset

| Kustannus | Arvio |
|---|---|
| Opiskelijan käyttö | **0 €**: staattiset tiedostot GitHub Pagesissa, ei API-kutsuja, ei palvelinta |
| Siirto | indeksi ~15 kt gzip per kieli, `valmentaja.js` ~20 kt; ei merkittävä |
| Kehitys (Claude Code) | noin 150–350 k tokenia per jaettu PR, sisältö-PR:t (I, J) katselmointeineen 300–600 k; yhteensä noin 2,5–3,5 M tokenia, ks. kohta 8 |
| CI | jokainen jaettu PR ajaa täydet selaintestit (~20 ydintuntia); 7 jaettua PR:ää ≈ 140 ydintuntia |
| Ylläpito | uusi tehtävä tulee indeksiin automaattisesti; sivutiedostoon vain poikkeukset |

## 8. Kehitysjärjestys: erilliset, hallittavat pull requestit

Kaikki PR:t 2–8 muuttavat jaettuja tiedostoja (`scripts/`, `templates/`, `lang/`), joten ne tehdään **yksin, yksi
kerrallaan** (juuren `CLAUDE.md` sääntö 3) ja sovitetaan työjonon kohtien 13 ja 14 (simulaatioiden käyttöliittymä,
U1–U3) väliin; ne muuttavat samoja tiedostoja (`lesson.js`, `site.css`). Avoin päätös P7: aloitetaanko vasta kohdan 14
jälkeen. PR 1 ja PR 9 ovat FY9:n sisältöä ja voivat kulkea jaettujen välissä.

| PR | Nimi | Tyyppi | Riippuu | Arvio (tokenia) |
|---|---|---|---|---|
| 0 | Tämä suunnitelma | docs | – | – |
| 1 | YTL- ja Abitti-tietojen tarkistus ja korjaus `fy9-koe`:ssa ja harjoituskokeessa | sisältö, delta | – | 200–300 k |
| 2 | Tehtäväindeksi: `kertaus/FY9.json`, `valmentaja.py check/build/report` | jaettu (scripts) | – | 150–250 k |
| 3 | Näytön kirjaus: `valmentaja.js` (a), `fl:attempt`-tarkennukset, `fl:rubric`, tietosuojasivu | jaettu | 2 | 200–300 k |
| 4 | Osaamisnäkymä ja suositukset: valmentajasivu, FY9-rivi ja -laatta | jaettu, UI | 3 | 250–350 k |
| 5 | Vaikea ratkaisuvaihe ja toistuvat virheet | jaettu, UI | 4 | 120–200 k |
| 6 | Koetila ja minikokeet 30/60 min, harjoituskokeen koetila | jaettu, UI | 4 | 300–450 k |
| 7 | Kertauspolku 2/4 viikkoa | jaettu, UI | 4 | 150–250 k |
| 8 | Käännökset en/fi-easy: uudet UI-tekstit tarkistetaan (tehdään jo kussakin PR:ssä; tämä on lopputarkistus) | lang | 4–7 | 60–100 k |
| 9 | Abitti 2 -ohje (TVT) ja aineistominikokeen ohjeistus | sisältö, täysi | 1, 6 | 350–550 k |
| 10 | Paikallisen kielimallin selvitys (vain dokumentti) | docs | 4–7 käytössä | 80–150 k |

Perustelu järjestykselle: PR 1 korjaa ensin sen, mitä opiskelija jo nyt lukee kokeesta. PR 2–3 ovat näkymättömiä ja
keräävät näyttöä ennen kuin mitään näytetään, joten PR 4:n näkymää voidaan kokeilla oikealla datalla (opettajan oma
selain). Koetila (6) on suurin ja riskialttein, joten se tulee vasta, kun malli on vakaa. Polku (7) käyttää kaikkea
edellistä. Jokainen PR on hyödyllinen yksinään: jos työ pysähtyy PR 4:n jälkeen, opiskelija saa silti osaamisnäkymän
ja suositukset.

## 9. Kunkin PR:n hyväksymiskriteerit ja testit

Kaikille yhteiset: CI vihreä; olemassa olevia testejä ei heikennetä eikä ohiteta; mikään katselmoitu sisältö ei
vanhene ilman, että `reviews.py scope` sen vaatii; fi, en ja fi-easy; puhelin ja tietokone; ennen/jälkeen-kuvat
(390 ja 1280 px) UI-PR:issä; uudet UI-tekstit listattu PR:n kuvauksessa opettajan hyväksyttäviksi; CLAUDE.md:n
kuvaus päivitetään samassa PR:ssä; mainin CI-ajo katsotaan yhdistämisen jälkeen.

**PR 1 – YTL- ja Abitti-tiedot.** Hyväksytään, kun: jokainen kokeen rakenteesta, pisteistä, apuvälineistä ja
ohjelmista esitetty väite on tarkistettu kohdan 10 lähteestä ja lähde kirjattu `review/developer.md`:hen;
epävarmat kohdat on muotoiltu ohjaamaan virallisiin ohjeisiin; harjoituskokeen rakenne vastaa ajantasaista määräystä tai
poikkeama on sanottu. Testit: `check_lesson`/`units.py check`, `check_i18n`, `test_unit_i18n`, `check_layout`;
katselmointi `reviews.py scope`:n mukaan (odotus: tiede ja pedagogiikka delta, visuaalinen delta).

**PR 2 – Tehtäväindeksi.** Hyväksytään, kun: `valmentaja.py build` kirjoittaa indeksin jokaiselle julkaistulle
kielelle; jokaisella FY9-tehtävällä on tunniste, yksikkö, osaaminen, tarkistustapa, aika ja href; `check` hylkää
viittauksen olemattomaan tehtävään ja väärän koebudjetin; `report` listaa solut, joissa ei ole automaattista tehtävää;
yksikään sivu ei muutu (paitsi uusi JSON). Testit: uusi `test_valmentaja.py` (skeema, kaikki id:t olemassa, kielten
pariteetti, deterministisyys: kaksi buildia → sama tiedosto), `build.py`-tarkistus, että committattu `site/` täsmää.
Selvitetään R9 (`ruukkilabra:tarkistettu`-törmäys) ja kirjataan tulos.

**PR 3 – Näytön kirjaus.** Hyväksytään, kun: FY9-yksikön sivulla ensimmäinen yritys, tulos, vihjeiden määrä, osunut
virhe ja itsearvioidut pisteet tallentuvat `ruukkilabra:fy9-valmentaja`-avaimeen kohdan 4.4 muodossa; vanhat avaimet
ja `fl:attempt`-tapahtuman vanhat kentät ennallaan; sivun ulkoasu ei muutu; työtiedosto vie ja tuo avaimen (todistettu
testillä); tietosuojasivu päivitetty; ei verkkokutsuja. Testit: uusi `test_valmentaja_log.py` (Playwright: yritys →
lokirivi; toinen yritys ei uusi tulos; vihje laskee; estetty tallennus ei kaada sivua; kaksi välilehteä), laajennettu
`test_palautus.py` (avain mukana työtiedostossa, palautus toisessa selaimessa), `test_progress`, `test_tehty`,
`test_writepad` ennallaan, R5-testi (ei `fetch`-kutsuja ulos).

**PR 4 – Osaamisnäkymä ja suositukset.** Hyväksytään, kun: valmentajasivu kolmella kielellä; enintään kolme
suositusta, jokaisella syy kiinteästä listasta; tilat ja säännöt kohtien 5.1–5.4 mukaan; ei prosentteja; tyhjällä
lokilla vain diagnoositarjous; vapaa harjoittelu aina linkitettynä; FY9-sivun rivi ja laatta; toimii ilman
JavaScriptiä (sivu kertoo, että valmentaja tarvitsee JavaScriptin, ja linkittää tunteihin ja sekoittimeen).
Testit: golden-lokit (vähintään 12 tapausta: tyhjä, vain itsearvio, arvaaja, heikko yksi aihe, erääntyneet kertaukset,
kaikki vahvaa, monikielinen loki, tasapeli, jatkotehtävä, päivän aika loppuu, jumittumisen esto, yön yli);
`check_layout` 8 leveyttä; `check_a11y`; `test_home` (laatta), `test_jatka` ennallaan.

**PR 5 – Vaikea vaihe ja toistuvat virheet.** Hyväksytään, kun: siru-rivi näkyy vasta ratkaisun avauduttua, on
valinnainen ja näppäimistöllä käytettävä; valinnat näkyvät valmentajassa; toistuva virhe näytetään vain, kun sama
virhekäsitys on osunut vähintään kahdesti, ja näytetty teksti on olemassa olevaa palautetta. Testit: Playwright
(valinta tallentuu, poistettavissa), `palautus_tasks.py --check` (rivi ei vuoda opettajan arviointinäkymään),
`check_layout` avoimissa tiloissa.

**PR 6 – Koetila ja minikokeet.** Hyväksytään, kun: koosteet sivutiedostosta, `check` hyväksyy budjetit; ennen
Lopeta-painiketta vihjeet, Lähellä- ja virhepalaute sekä mallivastaukset eivät ole näkyvissä eivätkä avattavissa;
valinta tehdään ennen vastaamista; ajastin ei estä mitään vaan kertoo; ajankäyttö kirjautuu tehtävittäin; lopussa
tarkistus ja rubriikit; tulokset lokiin tilalla `k`; harjoituskoe toimii ennallaan ja koetila on sen valinnainen tila
(sisältö ei muutu, katselmoinnit pysyvät). Testit: uusi `test_koetila.py` (lukot, aika loppuu, keskeytys ja
uudelleenlataus jatkaa ajastinta, valinnan raja, pisteiden summa enintään max), `test_practice`, `test_writepad`,
`check_layout` kaikissa tiloissa, `check_a11y` (ajastin ei vie ruudunlukijan huomiota jatkuvasti).

**PR 7 – Kertauspolku.** Hyväksytään, kun: 14 ja 28 vrk, 3–7 päivää viikossa, 20/40/60 min; päivän arvioitu aika ei
ylitä valintaa; väliin jäänyt päivä ei kasaa rästejä; polku muokattavissa ja poistettavissa; ei ilmoituksia. Testit:
golden-polut (diagnoosi eri tuloksin → odotettu järjestys), päivämäärälogiikka (karkausvuosi, kesäaika), layout.

**PR 8 – Kielten lopputarkistus.** Hyväksytään, kun: `check_i18n` ja `test_i18n` vihreät, fi-easy-tekstit NOTES.md
§12:n mukaan, en-tekstit samat avaimet; puhuttu luku (`readaloud`) lukee uudet näkymät oikein.

**PR 9 – Abitti 2 -ohje.** Hyväksytään, kun: ohje perustuu vain kohdan 10 tarkistettuihin lähteisiin (luettelo PR:ssä),
vanhentuvat kohdat on päivätty; kolme katselmointia PASS; linkitetty `fy9-koe`:sta ja aineistominikokeesta. Testit:
`guides.py check`, `check_layout`, `check_i18n`.

**PR 10 – Paikallisen kielimallin selvitys.** Vain dokumentti `docs/audits/`: pedagoginen tarve (mitä malli tekisi,
mitä nykyinen deterministinen palaute ei tee), tekninen (WebGPU-tuki puhelimissa, mallin koko, suomen laatu,
latausaika, akku), riskit (hallusinaatio fysiikassa, arvioinnin näennäinen luotettavuus), vertailu nykyiseen
ääneenluvun selainmalliin (`readaloud.js`, ~145 Mt, onnxruntime-web) ennakkotapauksena. **Ei toteutusta**, eikä
mikään muu ominaisuus saa riippua siitä. Päätös toteutuksesta vasta opettajan erillisen arvion jälkeen.

## 10. YTL- ja Abitti-tietojen tarkistus

Tässä ympäristössä tehtiin verkkohaku 14.11.2026, mutta alkuperäisiä asiakirjoja ei luettu kokonaan. Alla oleva on
**hakutulosten perusteella tarkistettavaa**, ei varmistettua tietoa. PR 1 lukee jokaisen lähteen ja kirjaa
lukupäivän.

| Tarkistettava asia | Nykyinen teksti sivustolla | Haun viite | Lähde |
|---|---|---|---|
| tehtävien määrä 11, vastataan 7:ään | `fy9-koe`, harjoituskoe | reaaliaineiden määräykset mainitsevat fysiikalle 11 / 7 | YTL: Reaaliaineiden kokeiden määräykset ja ohjeet (ylioppilastutkinto.fi, `fi_reaaliaineiden_kokeiden_maaraykset.pdf`) |
| osat I–III, 20 / 15 / 20 p, Osa III "2 kolmesta" | `fy9-koe`, harjoituskoe | hyvän vastauksen piirteet 2023–2025 näyttävät kolmiosaisen rakenteen ja Osa III:n kaksi kolmesta | tiedostot.ylioppilastutkinto.fi: fysiikan kokeiden hyvän vastauksen piirteet (K2023, S2023, K2025) |
| Osan I muoto (monivalinnat, väitteet, lyhyet) | `fy9-koe` | vaihtelee kokeittain | sama |
| 6 h, 120 p | `fy9-koe`, harjoituskoe | ei vahvistettu haussa | määräykset, kohta "kokeen rakenne ja pisteet" |
| arvioinnin kohteet (tieto, soveltaminen, kokeellinen tiedonhankinta) | `fy9-koe` | mainittu hyvän vastauksen piirteissä | sama |
| Abitti 2:n ohjelmat: kaavaeditori, Collabora (taulukkolaskenta), GeoGebra, Draw.io | `fy9-koe` "Kuvaajat ja kaavat koneella" | mainittu Abitti-sivuilla; osa uutisista vanhoja | abitti.fi, ylioppilastutkinto.fi "Abitti 2" |
| MAFY-taulukot, MAOL digitaulukot, TI ExamCalc Abitti 2:ssa | ei mainittu | mainittu suunniteltuina tai lisättyinä eri aikoina | abitti.fi uutiset; ylioppilastutkinto.fi ajankohtaista |
| liitetiedostot oheisohjelmissa, aineisto HTML-taulukkona | ei mainittu | mainittu rajoitukseksi (päivämäärä epäselvä) | abitti.fi "Kokeen laatiminen" |
| siirtymäaikataulu (Abitti 2 ylioppilaskokeissa) | ei mainittu | ei selvitetty | ylioppilastutkinto.fi "Abitti 2" |

Periaate: sivusto ei esitä muistinvaraista tai vanhentunutta tietoa varmana. Kokeen rakenteesta kerrotaan yleiset
asiat ja ohjataan YTL:n ajantasaisiin määräyksiin, kuten `fy9-koe` jo tekee. Harjoitusten pisteet ja ajat (3 min/p)
ovat harjoittelun mitoitus, eivät väite oikean kokeen pisteytyksestä, ja se sanotaan sivulla.

## 11. Avoimet päätökset (opettajalle)

| # | Päätös | Suositus |
|---|---|---|
| P1 | "Kuusi osaamisaluetta" = `competencies.json`:n kuusi osaamista vai kurssin kuusi lukua? | osaamiset osaamisalueina, luvut ja tunnit aiheina (ruudukko 16 × 6) |
| P2 | Tilojen sanat (Ei vielä näyttöä · Näyttöä vähän · Harjoittele · Kehittyy · Vahva · Vahva, kertaa pian) | hyväksy tai muotoile; ei prosentteja |
| P3 | Valmentaja omalla sivulla vai FY9-sivulla | oma sivu + yksi rivi ja yksi laatta FY9-sivulla |
| P4 | FY9-sivun rivi Jatka-rivin korvaajana vai sen alla | korvaa Jatka-rivin FY9-sivulla (yksi rivi) |
| P5 | Uudet UI-tekstit (yleislinja 14.11.): luettelo kussakin PR:ssä | hyväksytään PR kerrallaan |
| P6 | Tuleeko näyttöloki opettajalle palautettavaan työtiedostoon vai vain varmuuskopioon | vain varmuuskopioon; palautukseen erillisellä päätöksellä |
| P7 | Jaetut PR:t 2–8 työjonon kohtien 13 ja 14 jälkeen vai väliin | kohdan 13 PR 1–5 ja kohdan 14 U1 ensin, sitten valmentaja (samat tiedostot) |
| P8 | Minikokeiden koosteet: agentti ehdottaa, opettaja hyväksyy | kyllä; 6 aihekoostetta + 2 × 30 min + 2 × 60 min + 2 aineistokoostetta |
| P9 | Mitoitus 3 min/p ja tehtävien arvioidut ajat | hyväksy alustavaksi, tarkistetaan PR 1:ssä |
| P10 | Laajennetaanko myöhemmin moduulien Sovella itsenäisesti -tehtäviin (sekoittimen 28) | myöhemmin, kun FY9 on käytössä |
| P11 | Abitti 2 -ohje omana TVT-ohjeena vai `fy9-koe`:n osana | oma TVT-ohje, linkitetään |
| P12 | Paikallinen kielimalli: selvitetäänkö lainkaan | selvitys vasta, kun PR 4–7 ovat käytössä; ei toteutusta ilman erillistä arviota |
