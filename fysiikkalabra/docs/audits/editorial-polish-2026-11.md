# Ruukkilabra – koko oppikirjasarjan toimituksellinen viimeistelyauditointi

**Päiväys:** 13.11.2026  
**Tarkastettu lähtötaso:** `Hellsla/hellsla.github.io` / `main`, commit `761b6673e1c9cd5a00d4a8d7cf1ece7e95c9427e`.  
**Tämä on vain VAIHE 1: riippumaton toimituksellinen auditointi.** Tiedosto on tarkoitettu opettajan hyväksyttäväksi, ei automaattisesti sovellettavaksi korjaussarjaksi.

## 1. Kokonaisarvio ja johtopäätös

Ruukkilabran nykyisessä aineistossa on laajasti kustannustoimituksellisesti käyttökelpoista ydinsisältöä: fysiikan mallien ehdot ilmoitetaan usein selvästi, numeerisissa esimerkeissä on periaate–kaava–sijoitus–tulos–järkevyys-rakenne, ja ongelmanratkaisuun liittyy sekä kokeellisia että käsitteellisiä tehtäviä. Merkittävimmät jäljellä olevat heikkoudet **eivät ole jokaisessa luvussa**, eivätkä edellytä oppikirjan uudelleenkirjoittamista. Ne keskittyvät (a) 75 minuutin ydinpolun kestoon, (b) ennusteen ennenaikaiseen paljastamiseen, (c) harhaanjohtaviin absoluuttisiin ilmauksiin ja (d) joissakin tutkimuksissa liian moneen selvitettävään muuttujaan.

**Julkaisukelpoisuuden päätelmä:** FY4-1, FY4-2, FY5-9, FY5-16 ja FY6-13 eivät nykyisessä pakollisen tuntipolun muodossaan ole vielä riittävän selkeitä yhden 75 minuutin tunnin oppikirjajaksoiksi. FY9:n 21–39 aktiviteetin pakolliset kertauspolut kaipaavat erityisesti harjoitusten priorisointia. Käsitteellisiä täsmennyksiä tarvitaan rajatuissa kohdissa (esim. FY7-11, FY7-13, FY8-12), mutta tämän kierroksen perusteella **ei ole vahvistettu P0-luokan lasku- tai fysiikkavirhettä**.

### Menetelmä ja rehellinen kattavuusrajaus

- Luettu repositorion `CLAUDE.md`, `NOTES.md`, `docs/EDITORIAL_QUALITY_STANDARD.md`, `docs/physics-guardrails.md` sekä aiemmat FY1–FY3-fysiikan ja FY1–FY4-työmäärän auditoinnit. Erottelu `main`-haaran ja avoinna olevien PR:ien välillä on tärkeää: erityisesti PR #521, #522 ja #523 koskettavat samanaikaisesti materiaaleja/merkintöjä.
- Kartoitettu **kaikkien 113 FY1–FY8-luvun** `lesson.md`-tekstien rakenne, `inquiry.json`-vaiheet ja `exercises/exercises.json`-tehtävälajit; tarkastettu myös kaikkien 113 luvun `solutions.md`-tiedostojen vastausosioiden lukumäärä. Kaikissa osioita oli yhtä monta kuin tehtäviä (yleensä 21, yhdessä FY8-luvussa 22). Tämä on **rakenne- ja kattavuustarkistus**, ei väite kaikkien yksittäisten lukuarvojen laskemisesta uudelleen.
- Luettu tarkemmin priorisoitujen lukujen teoriaa, tutkimusasetelmia ja valittuja malliratkaisuja. FY9:n 16 yksikön rakenteet sekä FY10:n 27 tutkimustekstin sisältörakenne käytiin läpi; FY14:n 29 englanninkielisen yksikön teemat ja valitut fysiikkakohdat tarkastettiin.
- Ahjo 1, Ahjo 2 ja Dronelabra tarkastettiin `jaksot/ahjo/jakso.json`-tuntirakenteista. Käännösten vastaavuutta verrattiin kansiorakenteiden ja valittujen `inquiry.json`-näytteiden tasolla. FY1-8:sta viisi pistokoetta (FY1-7, FY2-5, FY4-1, FY7-11, FY8-12) tuottivat samat aktiviteetti-ID:t ja pakollisuusvalinnat suomessa, englannissa ja selkosuomessa. Täydellistä lausekohtaista käännöstarkistusta ei tehty.
- Simulaatioiden laskentaa, renderöintiä, oikeaa laitteistoa tai `reviews.py verify` -ketjua **ei ajettu**. Raportti ei muuta yhtäkään sisältö- tai kuva-/simulaatiotiedostoa. Sen havainnot ovat tarkistettavia toimituksellisia ehdotuksia, eivät automaattisesti hyväksyttyjä korjauksia.

### Merkittävimmät vahvuudet

1. Opiskelijan aktiivinen ennuste, mittaus/aineisto, teoria ja arviointi on sisäänrakennettu suurimpaan osaan luvuista.
2. FY1–FY8-tehtäväsarjat sisältävät käsitteellisiä, graafisia, data-, virhe-, malli- ja päättelytehtäviä eivätkä muodostu vain sijoituslaskuista.
3. Mallivastausten kattavuus on rakenteellisesti hyvä, ja fysiikan periaatteen perustelu toistuu johdonmukaisena ratkaisuvaiheena.
4. FY10:n tutkimuksissa erotetaan jo ohjattu, osittain ohjattu ja itsenäinen työtapa. Esimerkiksi pariston oikosulkua ja mikroaaltouunin käyttöä koskevat turvarajaukset on kirjoitettu nimenomaisesti.
5. FY14 erottaa ITERin plasmahyötysuhteen `Q`:n koko voimalaitoksen sähköenergiataseesta ja ilmoittaa suunnitelmien päivämäärät.

### Kymmenen merkittävintä toistuvaa ongelmatyyppiä (ei laskennallinen frekvenssiranking)

| # | Ongelmatyyppi | Varmennettu esimerkki | Yhteinen ratkaisu |
|---|---|---|---|
| 1 | Liian monta pakollista tutkimusta | FY4-1, FY4-2, FY5-9 | Yksi päämittaus tunnille, muu valinnaiseksi |
| 2 | Ennusteen selitys näkyy ennen näyttöä | FY1-7, FY2-5 ja FY2-7 | `reveal.after` todelliseen havaintoon |
| 3 | Ehdottomat sanat mallin ulkopuolella | FY4-8 `aina`, FY7-11 `aina`, FY8-12 `läpäisee` | Mallin ehdot jo Miksi-kysymykseen |
| 4 | Yksittäisen tunnin sisällöllinen kaksoisaihe | FY5-16, FY7-16 | Selkeä ydinpolku ja syventävä polku |
| 5 | Kertauspolun kaikki tehtävät merkitty pakollisiksi | FY9-liike, FY9-koe | Diagnostiikasta 2–3 ydintehtävää |
| 6 | Tutkimuskysymys lupaa mitata ominaisuuden, jota mitataan vain epäsuorasti | FY10-lammonjohtuminen | Nimeä mitattava suure ja mallin rajat |
| 7 | Tutkimuksessa liian monta eri tavoitetta | FY10-heiluri, FY10-muuntaja | Yksi ensisijainen riippuvuus, toinen laajennukseen |
| 8 | Sama selitys heti Ennusta-, Tutki- ja Teoria-vaiheessa | FY2-5, FY3-12 | Säilytä ennuste, lykätty palaute ja yksi varsinainen selitys |
| 9 | Arjen termi epätarkempi kuin opetettu käsite | FY6-14, FY8-14 | Luonnollinen mutta fysikaalisesti täsmällinen termi |
| 10 | Oppimis- tai laitejärjestelyn kesto piilossa | Ahjo 2 tunti 2, Dronelabra tunti 4 | Kirjaa valmistelu, vaihtoehtoinen toteutus ja kotityö |

### Tuntityömäärän toimituksellinen vertailuarvo

`75 min` ei tarkoita, että kaikki harjoitustehtävät tehtäisiin tunnilla. Suositeltu **tarkastuksen vertailupolku**, ei kaikille tunneille määrätty aikataulu: Pohdinta 5 min; Ennusta 6 min; Tutki ja yhteinen havainto 22 min; Teoria 12 min; malliesimerkki 10 min; kaksi ydintehtävää 15 min; Testaa ja arvioi 5 min. Loput ydintehtävät voidaan osoittaa kotityöksi tai itsenäisen harjoittelun poluksi, mikäli sivuston pakollisuusmerkinnät eivät johda harhaan.

## 2. Moduulikohtainen arvio ja korjaustyön laajuus

Arviot ovat karkea toimituksellisen **hyväksyttyjen ehdotusten toteutuksen** henkilötyöaika; fysiikan erillinen tarkastus, käännökset, testit ja PR-prosessi lisäävät työmäärää. **Ei arvio koko moduulin uudelleenkirjoittamisesta.**

| Kokonaisuus | Rakennekattavuus | Toimituksellinen tilanne | Arvio (h) |
|---|---|---|---:|
| FY1 | 8/8 lukua, tehtävät ja vastausosiot | Hyvä perusta; yksi pitkä tutkimuspolku ja viivästetty palaute | 3–5 |
| FY2 | 8/8 | Mallien kielellinen täsmällisyys, ennusteet ennen tietoa | 3–5 |
| FY3 | 16/16 | Pääosin jäsennelty; ilmastoteeman paljastus ja toisto | 3–5 |
| FY4 | 16/16 | **Suurin tuntikuormitusriski** alkuosan perusmekaniikassa | 7–11 |
| FY5 | 17/17 | Värähtelyjen mittausmäärä ja melun laajuus | 6–9 |
| FY6 | 16/16 | Kondensaattorin kuormitus; sähköasioiden turvallisuutta ei pidä supistaa | 3–6 |
| FY7 | 16/16 | Dispersio- ja hilaesimerkkien sanallinen täsmällisyys | 4–6 |
| FY8 | 16/16 | Hyvä fysikaalinen taso, mutta keskeiset aloituskysymykset korjattava | 4–7 |
| FY9 | 16 kertausyksikköä | **Pakollisuusmerkinnät tekevät kertauksesta liian raskaan** | 6–9 |
| FY10 | 27 tutkimusta | Kokeellisen tutkimuksen tavoitteiden rajaaminen | 6–10 |
| FY14 | 29 englanninkielistä yksikköä | Hyvä käsitteellinen erotus; ajankohtaiset aikataulut pidettävä keskitettyinä | 2–4 |
| Ahjo 1 ja 2 | 16 + 16 tuntia | Materiaali- ja projektipolut selkeitä; käyttäjätyön kalenterointi | 2–4 |
| Dronelabra | 16 tuntia | Turvallisuusroolit vahvuus, kokoamisen aikataulu vaatii realismia | 3–5 |

**Kieliversiot:** FY1–FY8:n moduulirunko ja tarkistetut aktiviteetti-ID:t vastaavat toisiaan. Suomenkielisen korjauksen jälkeen muutettujen merkitysten pitää siirtyä englantiin ja selkosuomeen; niille ei tehdä tässä yleistä stilististä uudelleenkirjoitusta. FY10 on tässä repossa lähtökohtaisesti suomenkielinen tutkimuskokoelma, ja FY14:n varsinainen sisältö on englanninkielinen; puuttuvaa muun kielistä rinnakkaistiedostoa ei pidä automaattisesti luokitella virheeksi.

## 3. Tarkat muutoshavainnot

Jokaisessa havaintorivissä polku on **suhteessa `fysiikkalabra/`-hakemistoon**. Tekstimuutokset ovat opettajan hyväksyntää odottavia ehdotuksia. Rakennemuutoksissa nykyinen pakollisuusmerkintä on osa havaittua tekstiä ja uusi arvo on täsmällinen toteutusohje.

### 01 · FY1 — fy1-3 Mittaaminen ja mittauksen luotettavuus · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY1/fy1-3/inquiry.json → activities[id=exp-2]`
- **Nykyinen teksti/rakenne:** Koe 2: systemaattinen virhe ei kumoudu; optional puuttuu (pakollinen).
- **Ehdotettu korvaus:** Säilytä tutkimus, mutta merkitse exp-2 valinnaiseksi opettajan näyttämäksi toiseksi tutkimukseksi (optional: true); pidä ydinpolussa simulaatio, exp-1 ja aineisto.
- **Perustelu:** Ydinpolussa 20 aktiviteettia, kaksi pakollista koetta ja useita tulkintoja. Yksi huolellinen mittaus ja sen tulkinta riittävät varsinaiselle oppitunnille.
- **Hyväksyntäluokka:** B

### 02 · FY1 — fy1-7 Tiheys · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY1/fy1-7/inquiry.json → activities[id=ennuste-1], choices[].feedback, reveal`
- **Nykyinen teksti/rakenne:** Ennuste 1: kolminkertainen pala; oikean vastauksen feedback alkaa 'Oikein. Kun massa on suoraan verrannollinen tilavuuteen ...'. reveal-määrittely puuttuu.
- **Ehdotettu korvaus:** Lisää ennusteelle reveal: {after: 'johtopaatos', pending: 'Palaa vastaukseesi, kun olet tutkinut massan ja tilavuuden aineiston.'}; näytä vaihtoehdon oikeellisuus ja selitys vasta tutkimuksen jälkeen.
- **Perustelu:** Välitön mallivastaus tekee aineistoon perustuvasta ennusteesta tarkistustehtävän. Ennusteen perustelu on arvokas juuri ennen tutkimusta.
- **Hyväksyntäluokka:** B

### 03 · FY2 — fy2-5 Polttoaineet ja lämpöarvo · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY2/fy2-5/inquiry.json → activities[id=ennuste-1], choices[].feedback`
- **Nykyinen teksti/rakenne:** Ennuste 1: bensiini ja polttopuu; palautteessa jo ennen taulukkoa 'Bensiinin lämpöarvo on noin 43 MJ/kg ja ilmakuivan puun noin 15 MJ/kg ...'; reveal puuttuu.
- **Ehdotettu korvaus:** Siirrä lukuarvot sisältävä palaute avautumaan vasta activities[id=taulukko]-aineiston jälkeen (reveal.after: 'taulukko'). Näytä alkuvaiheessa vain opiskelijan tallentama ennuste.
- **Perustelu:** Ennustevaihe ei saa paljastaa juuri niitä arvoja, jotka opiskelijan on tarkoitus päätellä tutkimusaineistosta.
- **Hyväksyntäluokka:** B

### 04 · FY2 — fy2-7 Energian siirtäminen · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY2/fy2-7/inquiry.json → activities[id=ennuste-2], choices[].feedback`
- **Nykyinen teksti/rakenne:** Ennuste 2: miksi korkea jännite; palaute kertoo jo ennen tutkimusta, että 'sama teho saadaan pienellä virralla, ja häviö on paljon pienempi'; reveal puuttuu.
- **Ehdotettu korvaus:** Ajoita vaihtoehtojen perustelut vasta activities[id=jannite]-tutkimuksen ja johtopäätöksen jälkeen (reveal.after: 'johtopaatos').
- **Perustelu:** Tavoite on ensin ennustaa häviöiden riippuvuus ja vasta sitten perustella se luvuilla; nykyinen järjestys oikaisee päättelyn.
- **Hyväksyntäluokka:** B

### 05 · FY2 — fy2-8 Energiantuotanto, ympäristö ja ilmastonmuutos · P2

- **Lähdetiedosto ja kohta:** `content/fi/FY2/fy2-8/lesson.md → Ydinajatus, kasvihuoneilmiö`
- **Nykyinen teksti/rakenne:** Kasvihuonekaasut siis päästävät auringon säteilyn läpi mutta hidastavat lämpösäteilyn pääsyä pois.
- **Ehdotettu korvaus:** Ilmakehä päästää suuren osan Auringon säteilystä maanpinnalle, mutta kasvihuonekaasut absorboivat tehokkaasti maanpinnan lähettämää lämpösäteilyä ja säteilevät energiaa myös takaisin maanpintaa kohti.
- **Perustelu:** Vältetään vaikutelma, että ilmakehä olisi Auringon säteilylle täysin läpinäkyvä; FY3-12 selittää myös lyhytaaltoisen säteilyn absorptiota.
- **Hyväksyntäluokka:** B

### 06 · FY3 — fy3-12 Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY3/fy3-12/inquiry.json → activities[id=pred-2], choices[].feedback`
- **Nykyinen teksti/rakenne:** Ennuste 2: kun hiilidioksidia lisätään; reveal-määrittely puuttuu, vaikka valinnan palaute ohjaa jo 'Tutki-vaiheen toisessa taulukossa ...'.
- **Ehdotettu korvaus:** Lisää reveal: {after: 'epatasapaino', pending: 'Tarkista arviosi lämpötilan muuttumisesta vasta energiatasapainon tutkimisen jälkeen.'}.
- **Perustelu:** Tasapainon muodostuminen on luvun keskeinen oivallus, jonka opiskelijan tulee ensin perustella aineistosta.
- **Hyväksyntäluokka:** B

### 07 · FY4 — fy4-1 Paikka, nopeus ja tasainen liike kuvaajina · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY4/fy4-1/inquiry.json → activities[id=exp-3], optional`
- **Nykyinen teksti/rakenne:** Koe 3: vastakkaiset suunnat; optional puuttuu. Yhteensä 21/21 aktiviteettia ydinpolussa.
- **Ehdotettu korvaus:** Merkitse exp-3 valinnaiseksi (optional: true). Säilytä ennuste-3 sekä lyhyt opettajan yhteinen negatiivisen nopeuden demonstraatio ennen teoriaa.
- **Perustelu:** Kolmas täydellinen aineistonkeruu, sitä seuraava lasku ja kaksi muuta koetta ovat 75 minuutin tunnilla päällekkäisiä. Etumerkkiajatus tulee silti opettaa.
- **Hyväksyntäluokka:** A

### 08 · FY4 — fy4-2 Kiihtyvyys ja tasaisesti kiihtyvä liike · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY4/fy4-2/inquiry.json → activities[id=exp-3], optional`
- **Nykyinen teksti/rakenne:** Koe 3: tangentti ja hetkellinen nopeus; optional puuttuu. Yhteensä 20/20 aktiviteettia ydinpolussa.
- **Ehdotettu korvaus:** Merkitse exp-3 valinnaiseksi syventäväksi kuvaajatutkimukseksi (optional: true). Jätä exp-1 ja exp-2 ydinpolkuun, esitä tangentti teoriana tai opettajan lyhyenä demonstrointina.
- **Perustelu:** Kaksi mittausta, kuvaajamallit ja tangenttiharjoitus kuormittavat samaa tuntia. Tangentin kulmakertoimen lukeminen vaatii jo omaa työskentelyaikaa.
- **Hyväksyntäluokka:** A

### 09 · FY4 — fy4-8 Mekaanisen energian säilyminen ja energiaperiaate · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY4/fy4-8/lesson.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi vuoristoradan ensimmäinen mäki on aina radan korkein, vaikka junaa ei sen jälkeen enää vedetä ylös?
- **Ehdotettu korvaus:** Miksi perinteisen, vain alussa nostettavan vuoristoradan ensimmäinen mäki on yleensä radan korkein?
- **Perustelu:** 'Aina' ei päde esimerkiksi laukaistaviin tai radalla lisää energiaa saaviin vuoristoratoihin. Luvun mekaniikan energiamalli pätee määritellyssä järjestelmässä.
- **Hyväksyntäluokka:** A

### 10 · FY5 — fy5-6 Satelliitit ja planeetat ympyräradalla · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY5/fy5-6/inquiry.json → activities[id=koe-2], optional`
- **Nykyinen teksti/rakenne:** Koe 2: vaikuttaako satelliitin massa? (pakollinen); lisäksi kolme ennustetta ja kolme erillistä teoria-aktiviteettia.
- **Ehdotettu korvaus:** Merkitse koe-2 valinnaiseksi (optional: true). Säilytä massasta riippumattomuus teoria- ja johtopäätöstekstissä sekä ennusteen vastauksen käsittelyssä.
- **Perustelu:** Ratanopeutta koskeva varsinainen koe-1 ja aineisto antavat riittävän perustan mallille; massavertailu voidaan ratkaista teoriasta.
- **Hyväksyntäluokka:** B

### 11 · FY5 — fy5-9 Jousivärähtelijä ja heiluri · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY5/fy5-9/inquiry.json → activities[id=koe-3], optional`
- **Nykyinen teksti/rakenne:** Koe 3: heilurin massa muuttuu; optional puuttuu, vaikka samassa Tutki-vaiheessa on yhteensä neljä pakollista koetta.
- **Ehdotettu korvaus:** Merkitse koe-3 valinnaiseksi (optional: true), ja tarkista heilurin massariippumattomuus ennusteen, teoriakappaleen ja yhteisen tulosten vertailun avulla.
- **Perustelu:** Molempien värähtelijöiden itsenäinen muuttujatutkimus on yhdessä 75 minuutin tunnissa liian suuri kokonaisuus.
- **Hyväksyntäluokka:** A

### 12 · FY5 — fy5-10 Aaltojen synty ja eteneminen · P2

- **Lähdetiedosto ja kohta:** `content/fi/FY5/fy5-10/exercises/exercises.json → level1, id=fy5-10-L1-04`
- **Nykyinen teksti/rakenne:** Uimahallin aaltoaltaan kone tekee aaltoja, joiden jaksonaika on 2,5 s ja aallonpituus 4,0 m. Kuinka suurella nopeudella aallot etenevät?
- **Ehdotettu korvaus:** Uimahallin aaltoaltaassa havaitaan, että aallonharjojen väli on 4,0 m ja jaksonaika 2,5 s. Koneen taajuus kaksinkertaistetaan, mutta aallon etenemisnopeus oletetaan samaksi. Mitä tapahtuu aallonpituudelle? Perustele ensin sanallisesti ja laske sitten.
- **Perustelu:** Tason 1 tehtävissä on jo useita suoria v = fλ -sijoituksia. Yhden tehtävän muuttaminen suureiden välistä riippuvuutta kysyväksi vähentää reseptitoistoa lisäämättä tehtävien määrää. Päivitettävä myös malliratkaisu.
- **Hyväksyntäluokka:** B

### 13 · FY5 — fy5-16 Melu, akustiikka ja äänentoisto · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY5/fy5-16/inquiry.json → activities[id=teoria-1..teoria-4], optional`
- **Nykyinen teksti/rakenne:** Neljä pakollista teoriaosaa, mm. 'Kaiutin ja mikrofoni', ja yhteensä 19/20 pakollista aktiviteettia.
- **Ehdotettu korvaus:** Erota tunnin ydinpoluksi melualtistus ja sen laskenta. Tee teoriasta 'Kaiutin ja mikrofoni' (teoria-4) valinnainen jatko-osa (optional: true) ja anna opettajalle vaihtoehto käsitellä se myöhemmin.
- **Perustelu:** Melualtistuksen turvallisuusasiaa ei pidä karsia, mutta äänen tuotannon sovellus ei mahdu realistisesti samaan ydinpolkuun.
- **Hyväksyntäluokka:** A

### 14 · FY6 — fy6-13 Kondensaattori ja sen energia · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY6/fy6-13/inquiry.json → activities[id=koe-5], optional`
- **Nykyinen teksti/rakenne:** Koe 5: läpilyönti ilmassa; optional puuttuu. Tutki-vaiheessa neljä pakollista koetta ja yksi valinnainen.
- **Ehdotettu korvaus:** Merkitse koe-5 valinnaiseksi (optional: true) ja säilytä läpilyöntilujuuden käsite teoriassa sekä turvallisuusperusteluissa.
- **Perustelu:** Läpilyönti on kiinnostava sovellus mutta ei edellytys kapasitanssin ja kondensaattorin energian päättelylle; muutos lyhentää tuntia ilman tietosisällön menetystä.
- **Hyväksyntäluokka:** B

### 15 · FY6 — fy6-14 Puolijohteet, diodi, LED ja aurinkokenno · P2

- **Lähdetiedosto ja kohta:** `content/fi/FY6/fy6-14/lesson.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi LED syttyy vain toisin päin kytkettynä, ja miksi LEDin virtaa pitää rajoittaa, vaikka hehkulampun voi kytkeä paristoon suoraan?
- **Ehdotettu korvaus:** Miksi LED syttyy vain oikeansuuntaisella kytkennällä, ja miksi sen läpi kulkevaa virtaa on rajoitettava?
- **Perustelu:** 'Toisin päin' on suhteellinen ilmaus ilman vertailukohtaa. Lyhyempi kysymys kohdistuu diodin tasasuuntaavaan toimintaan ja virranrajoitukseen.
- **Hyväksyntäluokka:** B

### 16 · FY7 — fy7-11 Dispersio: prisma ja sateenkaari · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY7/fy7-11/lesson.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi sateenkaaressa punainen on aina ulkoreunalla ja violetti sisäreunalla ...?
- **Ehdotettu korvaus:** Miksi pääsateenkaaressa punainen näkyy ulkoreunalla ja violetti sisäreunalla, ja miksi sen näkemiseksi Auringon on oltava katsojan selän takana?
- **Perustelu:** Samassa luvussa kerrotaan sivusateenkaaren käänteisestä värijärjestyksestä. Ehdoton 'aina' on siis ristiriidassa luvun oman oikean selityksen kanssa.
- **Hyväksyntäluokka:** A

### 17 · FY7 — fy7-13 Valon interferenssi ja diffraktio · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY7/fy7-13/lesson.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi laserosoittimen säde piirtää seinälle kokonaisen rivin valopisteitä, kun se kulkee ohuen läpinäkyvän kalvon läpi?
- **Ehdotettu korvaus:** Miksi laserosoittimen valo muodostaa seinälle rivin valopisteitä, kun se kulkee läpinäkyvän, tiheäviivaisen hilan läpi?
- **Perustelu:** Tavallinen ohut läpinäkyvä kalvo ei yksin selitä pistemäistä diffraktiomaksimien riviä. Luvun teoria määrittelee hilan viivalliseksi levyksi tai kalvoksi.
- **Hyväksyntäluokka:** A

### 18 · FY7 — fy7-16 Induktion sovelluksia: langaton lataus ja valokuitu · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY7/fy7-16/inquiry.json → activities[id=ennuste-kuitu], optional`
- **Nykyinen teksti/rakenne:** Ennuste 4: valo 100 kilometrin kuidussa; pakollinen neljäs ennuste samassa tunnissa, jossa jo tutkitaan latauskäämejä.
- **Ehdotettu korvaus:** Merkitse ennuste-kuitu valinnaiseksi (optional: true) ja tee siitä optisen kuidun teoriakappaleen aloituskysymys itsenäiselle opiskelijalle.
- **Perustelu:** Langattoman latauksen sähkömagneettinen induktio ja kuituvaimennuksen logaritminen malli ovat kaksi eri ilmiötä; molempia ei tarvitse tutkia täysimittaisesti samalla tunnilla.
- **Hyväksyntäluokka:** B

### 19 · FY8 — fy8-12 Ionisoiva säteily ja elimistö · P1

- **Lähdetiedosto ja kohta:** `content/fi/FY8/fy8-12/lesson.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi paperiarkki pysäyttää alfasäteilyn mutta gammasäteily läpäisee koko ihmisen kehon ...?
- **Ehdotettu korvaus:** Miksi paperiarkki pysäyttää alfasäteilyn mutta osa gammasäteilystä voi kulkea ihmisen kehon läpi, ja miksi alfasäteilyä lähettävä aine on erityisen haitallinen elimistön sisällä?
- **Perustelu:** Gammafotoneja myös absorboituu ja siroaa kehossa. Ehdoton 'läpäisee koko ihmisen kehon' on ristiriidassa saman luvun vaimenemismallin kanssa.
- **Hyväksyntäluokka:** A

### 20 · FY8 — fy8-14 Säteily lääketieteessä ja teknologiassa · P2

- **Lähdetiedosto ja kohta:** `content/fi/FY8/fy8-14/lesson.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi PET-kuvauksessa potilaaseen ruiskutetaan radioaktiivista sokeria ...?
- **Ehdotettu korvaus:** Miksi PET-kuvauksessa potilaalle annetaan radioaktiivisella fluori-18-isotoopilla merkittyä glukoosin kaltaista merkkiainetta, ja miten laite paikantaa säteilyn lähteen?
- **Perustelu:** Teorialuvussa puhutaan oikein FDG:stä, mutta aloituskysymyksen 'radioaktiivinen sokeri' antaa epätarkan kuvan käytetystä lääkeaineesta.
- **Hyväksyntäluokka:** B

### 21 · FY8 — fy8-15 Standardimalli: perushiukkaset ja vuorovaikutukset · P2

- **Lähdetiedosto ja kohta:** `content/fi/FY8/fy8-15/lesson.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi vapaa neutroni hajoaa keskimäärin noin vartissa, mutta protonin hajoamista ei ole havaittu koskaan, vaikka molemmat koostuvat samoista hiukkasista?
- **Ehdotettu korvaus:** Miksi vapaa neutroni hajoaa keskimäärin noin vartissa mutta protonin hajoamista ei ole havaittu, vaikka molemmat koostuvat ylös- ja alaskvarkeista?
- **Perustelu:** Protonissa on kaksi ylös- ja yksi alaskvarkki, neutronissa päinvastoin: 'samat hiukkaset' voi tulkita virheellisesti identtiseksi kvarkkikoostumukseksi.
- **Hyväksyntäluokka:** B

### 22 · FY9 — fy9-liike Liike kuvaajina (toistuva FY9-malli) · P1

- **Lähdetiedosto ja kohta:** `content/fi/units/fy9-liike/inquiry.json → activities[id=lt-1..lt-6] sekä muut lähtötasokysymykset`
- **Nykyinen teksti/rakenne:** Lähtötaso 1: vaakasuora viiva ... Lähtötaso 6: pinta-ala; kaikki 21 aktiviteettia ovat ydinpolussa (optional puuttuu).
- **Ehdotettu korvaus:** Valitse lähtötasosta kaksi pakollista eri osaamisalueen kysymystä (esim. lt-1 ja lt-6) ja merkitse loput neljä valinnaisiksi; säilytä muut tehtävät saatavilla kertauspolussa. Sovella ratkaisua FY9:n muihin vastaaviin 22-aktiviteetin yksiköihin tapauskohtaisesti.
- **Perustelu:** Lähtötason tarkoitus on diagnosoida ja ohjata kertaukseen, ei vaatia kuuden erillisen ennakkotehtävän suorittamista joka tunnilla.
- **Hyväksyntäluokka:** A

### 23 · FY9 — fy9-koe Ylioppilaskoe ja vastaustekniikka · P1

- **Lähdetiedosto ja kohta:** `content/fi/units/fy9-koe/inquiry.json → activities[id=pred-1..pred-6], activities[id=testi-1..] sekä muut`
- **Nykyinen teksti/rakenne:** 39/39 aktiviteettia pakollisia; kuusi lähtötasokysymystä, 13 numeerista harjoitusta ja 19 monivalintaa samassa polussa.
- **Ehdotettu korvaus:** Merkitse vähintään pred-4..pred-6 ja myöhemmät soveltavat koetehtävät valinnaisiksi (optional: true). Määrittele ydinpoluksi ratkaisutavan perustelu + yksi graafinen tehtävä + yksi laskullinen mallivastaus + palaute.
- **Perustelu:** Tämä ei ole realistinen 75 minuutin oppitunti sellaisenaan; soveltavat koetehtävät voivat olla itseopiskelua tai erillinen harjoituskoe.
- **Hyväksyntäluokka:** A

### 24 · FY9 — fy9-moderni Kvantti-ilmiöt, ydin ja säteily · P1

- **Lähdetiedosto ja kohta:** `content/fi/units/fy9-moderni/unit.md → Miksi-kysymys, rivi 3`
- **Nykyinen teksti/rakenne:** Miksi kasvihuoneen kirkkaat punaiset kasvivalot eivät vaurioita kasvien eivätkä puutarhurin DNA:ta, vaikka niiden teho on kilowatteja, mutta heikkokin röntgensäteily voi vaurioittaa?
- **Ehdotettu korvaus:** Miksi punaiset kasvatusvalot eivät ionisoi soluja samalla tavoin kuin röntgensäteily, vaikka valaisimien kokonaisteho voi olla suuri?
- **Perustelu:** Fotonin energia ja kokonaissäteilyteho ovat eri asioita; lisäksi 'eivät vaurioita DNA:ta' on liian ehdoton väite kaikenlaisista vaikutusmekanismeista.
- **Hyväksyntäluokka:** A

### 25 · FY10 — fy10-lammonjohtuminen Lämmön johtuminen lämpökameralla · P1

- **Lähdetiedosto ja kohta:** `content/fi/tutkimukset/fy10-lammonjohtuminen/investigation.md → Tutkimuskysymys, rivi 3; Teoriaa lyhyesti`
- **Nykyinen teksti/rakenne:** Mikä tutkittavista materiaaleista johtaa lämpöä tehokkaimmin, ja miten sen voi päätellä lämpökameralla mitatuista lämpötiloista?
- **Ehdotettu korvaus:** Miten lämpötila muuttuu eri materiaaleista tehdyissä samanmuotoisissa kappaleissa, ja millä varauksilla lämpenemisen nopeutta voi käyttää lämmönjohtavuuden vertailuun?
- **Perustelu:** Lämpötilan muutosnopeus riippuu lämmönjohtavuuden lisäksi lämpökapasiteetista, tiheydestä, pinnasta ja lämmityksestä. Luvussa tämä jo tunnustetaan, mutta alkuperäinen tutkimuskysymys on liian suora.
- **Hyväksyntäluokka:** A

### 26 · FY10 — fy10-heiluri Putoamiskiihtyvyyden määrittäminen heilurin avulla · P1

- **Lähdetiedosto ja kohta:** `content/fi/tutkimukset/fy10-heiluri/investigation.md → Tutkimuskysymys ja Mittaa`
- **Nykyinen teksti/rakenne:** Mistä heilurin jaksonaika riippuu, ja kuinka suuri on putoamiskiihtyvyys mittauspaikallasi? Lisäksi Mittaa pyytää vaihtelemaan sekä kuulan massaa että lähtökulmaa.
- **Ehdotettu korvaus:** Rajaa ohjatun tutkimuksen kysymys muotoon: 'Miten heilurin jaksonaika riippuu pituudesta, ja mitä mittauksista saadaan putoamiskiihtyvyydeksi?' Siirrä massan ja heilahduskulman vaikutuksen tutkiminen itsenäiseen laajennukseen.
- **Perustelu:** Kolmen ominaisuuden systemaattinen mittaaminen, suoran sovitus, epävarmuusarvio ja raportointi eivät ole mielekäs yhden oppitunnin ydinpolku.
- **Hyväksyntäluokka:** B

### 27 · FY10 — fy10-muuntaja Muuntajan tutkiminen · P1

- **Lähdetiedosto ja kohta:** `content/fi/tutkimukset/fy10-muuntaja/investigation.md → Tutkimuskysymys ja Laajennus`
- **Nykyinen teksti/rakenne:** Miten muuntajan toisiojännite riippuu käämien kierroslukujen suhteesta, kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksia, ja kuinka suuri on muuntajan hyötysuhde?
- **Ehdotettu korvaus:** Ohjatun työn pääkysymys: 'Miten muuntajan toisiojännite riippuu käämien kierroslukujen suhteesta, ja kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksia?' Siirrä hyötysuhteen määritys laajennukseen kuormitetulle muuntajalle.
- **Perustelu:** Jännitteen suhdelain ja kuormitetun muuntajan hyötysuhteen mittaaminen vaativat eri järjestelyjä ja johtopäätöksiä; erottelu parantaa tutkimuksellista fokusta.
- **Hyväksyntäluokka:** B

### 28 · FY14 — Road to Fusion: ITERin aikataulu kolmessa yksikössä · P3

- **Lähdetiedosto ja kohta:** `content/en/units/fy14-iter-project/unit.md → The plan that changed; fy14-iter-media/unit.md → ITER then and now; fy14-fusion-society/unit.md → Results, plans and claims`
- **Nykyinen teksti/rakenne:** The 2024 baseline plans research operation in 2034 and D–T operation in 2039. Aikataulu toistuu kolmessa itsenäisessä yksikössä.
- **Ehdotettu korvaus:** Säilytä varsinainen taulukko ja ajantasainen lähde yksikössä fy14-iter-project. Korvaa kahden muun yksikön pitkä aikataulukertaus yhdellä päivätyllä viittauksella, esim. 'ITER’s 2024 baseline places research operation in 2034 and D–T operation in 2039; see ITER: why, where and who for the dated plan.'
- **Perustelu:** Suunnitelmien muuttuminen on opetuksellinen sisältö, mutta päivitettävä aikataulutieto kannattaa pitää yhdessä ensisijaisessa paikassa. Päivämäärät ovat suunnitelmia, eivät tuloksia.
- **Hyväksyntäluokka:** C

### 29 · Ahjo 2 — AHJO2 tunti 2 Ongelman määrittely · P2

- **Lähdetiedosto ja kohta:** `jaksot/ahjo/jakso.json → courses[code=AHJO2].lessons[1].example`
- **Nykyinen teksti/rakenne:** Selvitä käyttäjien tarve. Haastattele vähintään kolmea käyttäjää, tai jos se sopii projektiinne paremmin, havainnoi käyttötilannetta ...
- **Ehdotettu korvaus:** Selvitä käyttäjien tarve. Valmistele kysymykset tunnilla ja haastattele mahdollisuuksien mukaan kolme käyttäjää ennen seuraavaa tapaamista. Jos haastattelut eivät ole mahdollisia, havainnoi käyttötilannetta tai perustele muu tiedonhankintatapa.
- **Perustelu:** Kolmen ulkopuolisen henkilön tavoittaminen ja haastattelu 75 minuutissa ei ole kaikille ryhmille mahdollista. Ennakkotehtävä pitää käyttäjälähtöisen tavoitteen ennallaan.
- **Hyväksyntäluokka:** B

### 30 · Dronelabra — DRONELABRA tunti 4 Dronen kokoaminen ja toimintakokeet · P1

- **Lähdetiedosto ja kohta:** `jaksot/ahjo/jakso.json → courses[code=DRONELABRA].lessons[3].levels.try ja teacher.time`
- **Nykyinen teksti/rakenne:** Kokoa drone ohjeen mukaan, mutta jätä potkurit kiinnittämättä. Käynnistä drone ... Tuntijako: 'kokoaminen 40 min, käynnistys- ja moottoritesti 15 min'.
- **Ehdotettu korvaus:** Ohjattu ydinpolku: 'Kokoa runko ja kiinnitä moottorit opettajan työvaiheohjeella. Tarkista kytkennät opettajan kanssa. Tee käynnistys- ja moottoritesti ilman potkureita vasta, kun kokoaminen on valmis; tarvittaessa käytä valmiiksi koottua laitetta tai jatka seuraavalla tunnilla.' Merkitse valmisteluaika ja vaihtoehdot opettajan ohjeeseen.
- **Perustelu:** Air:bit 2 -rakennussarjan ensimmäinen kokoaminen voi ylittää 40 minuuttia. Turvallisuutta ei saa nopeuttaa aikataulun vuoksi; ennakkoon koottu yksilö turvaa oppimistavoitteen.
- **Hyväksyntäluokka:** A

## 4. Yhteiset ohjeet, joilla ratkaistaan toistuvat ongelmat

**Ohje Y1 – Ennuste ei ole monivalintatesti.** Jokainen ennustetehtävä on opiskelijan ennen tutkimusta tekemä perusteltu arvio. Oikea/virheellinen-palaute ja fysiikan oikea selitys avautuvat vasta asiaan liittyvän havainnon ja johtopäätöksen jälkeen. Varmista `reveal.after`-viitteen olemassaolo; älä näytä käsitteellistä oikeaa vastausta jo ennustekortissa. Kaikki ennusteet eivät tarvitse numeerista oikeaa vastausta.

**Ohje Y2 – Pakollisen 75 minuutin ydinpolun budjetti.** Yhdellä tunnilla on pääsääntöisesti yksi riittävän perusteellinen mittaus tai simulaatiokokonaisuus. Vertailututkimukset, toiset parametrisarjat ja lisäsovellukset voivat olla valinnaisia. Lause `tehtävät`-vaiheessa EI tarkoita kaikkia 21 tehtävää tunnilla; erottele tunnin minimit, itsenäinen eteneminen ja kotiin sopivat tehtävät.

**Ohje Y3 – Ehdoton väite vaatii ehdottoman fysiikan.** Etsi `aina`, `ei koskaan`, `kaikki`, `ei vaurioita`, `läpäisee` sekä vastaavat ilmaukset aloituskysymyksistä ja tiivistelmistä. Korvaa ehdollisuudella vain, kun fysiikan mallin rajoitus sitä todella edellyttää. Älä muuta oikeita yleislakeja varovaisiksi vain varovaisuuden vuoksi.

**Ohje Y4 – Tutkimuskysymyksessä yksi mitattava riippuvuus.** Kokeellisessa tehtävässä erota havaittu suure, sen avulla pääteltävä malli ja mallin rajoitukset. Toiset suureet ja eri mittausjärjestelyt laajennukseen; säilytä epävarmuuden arvio ja aineistoon perustuva johtopäätös.

**Ohje Y5 – Malliratkaisu ei saa muuttua lomakkeen täyttämiseksi.** Säilytä fysiikan periaate, kaavan ratkaiseminen, yksiköt ja vastaus. Käytä `järkevyys`-vaiheessa vain oikeasti toista arviointiperustetta tai tilanteeseen sopivaa suuruusluokkaa. Älä toista edeltävää sijoitusta eri sanoin. Älä muuta sovittuja MAFY-/taulukkokirjan merkintätapoja tämän auditoinnin yhteydessä.

**Ohje Y6 – Kieliversioiden merkityssynkronointi.** Kun suomenkielisen tehtävän fysiikan malli, oikea vaihtoehto, pakollisuus tai vaiheistus muuttuu, vertaa vastaavat `id`-kohdat `content/en`- ja `content/fi-easy`-tiedostoihin sekä niiden mallivastauksiin. Ahjo-tunneilla vertaa `courses[].lessons[]` vastaavan koodin ja numeron perusteella. FY14:n päivättävät tiedot pidetään lähdeviitteineen yhdessä ensisijaisessa paikassa.

## 5. Priorisoitu hyväksyntäehdotus

### A. Välttämättömät ennen yhden oppitunnin ydinpolun julkaisuviimeistelyä

- FY4-1 ja FY4-2: pakollisten kokeiden vähentäminen (havainnot 7–8).
- FY4-8, FY7-11, FY7-13, FY8-12 ja FY9-moderni: harhaanjohtavien ehdottomien aloitusväitteiden täsmennys (havainnot 9, 16–17, 19, 24).
- FY5-9 ja FY5-16: realistinen pakollinen tuntipolku (havainnot 11, 13).
- FY9 kertauspolun pakollisuudet ja FY10:n lämpökameratutkimuksen suureiden tulkinta (havainnot 22–23, 25).
- Dronelabran kokoamisen aikataulu ja turvallinen vaihtoehtoinen eteneminen (havainto 30).

### B. Laadun kannalta selvästi hyödylliset muutokset

- Ennusteiden palautteen oikea ajoitus FY1–FY3:ssa (havainnot 2–4, 6).
- FY1-3, FY5-6, FY6-13 ja FY7-16 valinnaisuuden rajaus (havainnot 1, 10, 14 ja 18).
- FY2-8:n kasvihuoneilmiön täsmennys, FY5-10:n tehtävätyypin vaihto, FY6-14:n, FY8-14:n ja FY8-15:n termit (havainnot 5, 12, 15, 20–21).
- FY10:n heiluri- ja muuntajatyön selkeämpi ydin (havainnot 26–27) sekä Ahjo 2:n haastattelujen ajallinen erottaminen (havainto 29).

### C. Vapaaehtoinen viimeistely

- FY14:n aikataulukertauksen keskittäminen ja päivättyjen suunnitelmatietojen yhdenmukaistus (havainto 28). Älä heikennä lukujen luettavuutta itsenäisinä kokonaisuuksina.

**Korjausten toteutustapa hyväksynnän jälkeen:** muuta vain hyväksytyt `content/`- ja `jaksot/`-lähdetiedostot, päivitä niihin sidotut ratkaisut ja tarvittavat kieliversiot, suorita fysiikan, pedagogiikan sekä toimituksellinen tarkastus ja repositorion normaalit testit ja `reviews.py verify`. Älä merkitse hyväksyntöjä suoritetuiksi ilman toteutusta. Tee muutos-PR:t moduuleittain erilleen; **älä yhdistä automaattisesti**.

## 6. Opettajan hyväksyntä

- [ ] A: Hyväksyn välttämättömät korjaukset.
- [ ] B: Hyväksyn myös selvästi laatua parantavat korjaukset.
- [ ] C: Hyväksyn myös vapaaehtoisen viimeistelyn.
- [ ] Rajaan pois seuraavat havaintotunnukset: ______
- [ ] Huomioita ja korvaavia linjauksia: ______

**Pysähdy tähän. Tämä PR sisältää vain auditointiraportin; oppimateriaaleihin ei ole tehty muutoksia.**
