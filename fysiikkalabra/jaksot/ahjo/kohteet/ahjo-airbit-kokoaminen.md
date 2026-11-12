## Pikastartti

Air:bit 2 on rakennussarja, josta kootaan micro:bitillä toimiva nelikopteri. Kokoat sen valmistajan rakennusohjeen mukaan. Tämä sivu kertoo, missä järjestyksessä työ tehdään Dronelabrassa ja mitä tarkastetaan ennen kuin akku kytketään.

1. Lajittele osat ja tarkista ne ohjeen osaluettelosta.
2. Kokoa runko ja kiinnitä moottorit ja ohjainkortti ohjeen mukaan.
3. **Jätä potkurit kiinnittämättä.** Valmistajan ohjeessa potkurit ovat kokoamisluvun lopussa, mutta ne kiinnitetään vasta lentotunnilla.
4. Pyydä opettajan tarkastus ja kytke akku vasta sen jälkeen.

### Kokeile

Kokoa drone ilman potkureita ja käynnistä se tasaisella alustalla. Kirjaa, mitkä kirjaimet näyttö näyttää.

### Muokkaa

Tee moottoritesti ilman potkureita ja merkitse osakarttaasi, mikä moottori on missäkin kulmassa ja kumpaan suuntaan sen potkurin kuuluu pyöriä.

### Haasta itsesi

Kirjoita vianetsintäkortti kahdelle käynnistysvirheelle: mitä tarkistat ensin ja missä järjestyksessä?

## Haaste

Drone lentää vain, jos jokainen osa on oikeassa paikassa: kaksi potkuria pyörii myötäpäivään ja kaksi vastapäivään, ja ohjainkortin ja micro:bitin välillä on hyvä sähköinen yhteys. Tavoite on koota drone niin huolellisesti, että se käynnistyy ensimmäisellä kerralla ja läpäisee moottoritestin.

Valmistaja arvioi kokoamiseen kahdesta kolmeen tuntia, joten työ jakautuu kahdelle oppitunnille.

## Oppimistavoitteet

Työn jälkeen osaat

- nimetä dronen osat ja kertoa niiden tehtävät
- koota dronen ohjeen mukaan ja tarkastaa työn
- ladata akun valvotusti
- käynnistää dronen ja tulkita näytön ilmoitukset.

## Lähtötaso ja ennakkotaidot

Aiempaa kokemusta ei tarvita. Ennen akun kytkemistä pitää olla käyty [Dronelabran turvallisuusperehdytys](ahjo-drone-perehdytys.html).

## Laitteet ja materiaalit

Tiedot ovat valmistajan rakennusohjeesta. Tarkista oman sarjasi sisältö ohjeen osaluettelosta.

| Osa | Mitä se tekee |
|---|---|
| Runko, kuusikerroksista koivuvaneria | Pitää osat paikoillaan ja kestää törmäyksiä. |
| Ohjainkortti (musta), jossa on latauspiiri | Mittaa asentoa gyroskoopilla, ohjaa moottoreita ja lataa akun. |
| 4 moottoria, kahta eri tyyppiä | Pyörittävät potkureita. Kaksi pyörii myötäpäivään ja kaksi vastapäivään. |
| 4 potkuria ja 4 varapotkuria, halkaisija $65\,\text{mm}$ | Tuottavat nostovoiman. Suunta on merkitty potkurin napaan. |
| Litiumpolymeeriakku, 1 kenno, $3{,}7\,\text{V}$, $800\,\text{mAh}$ | Antaa virran moottoreille ja kortille. |
| micro:bit dronessa (valmistaja suosittelee versiota V2) | Laskee vakautuksen ja vastaanottaa radiokomennot. |
| micro:bit ohjaimessa ja paristokotelo | Lähettää ohjauskomennot radiolla. |
| Pieni ristipääruuvitaltta ja hylsyavain | Kokoamiseen. Hylsyavain on sarjassa. |

Micro:bitit, paristokotelo ja USB-kaapeli myydään yleensä erikseen.

## Turvallisuus ja perehdytys

Katso aiheet [potkurit ja moottorit](ahjo-turvallisuus.html#drone-potkurit) ja [akut](ahjo-turvallisuus.html#drone-akut). Ne ovat valmisteilla, kunnes koulu on hyväksynyt ne.

- Potkureita ei kiinnitetä kokoamistunneilla. Moottorien käynnistys ja pysäytys kokeillaan ensin ilman niitä.
- Akku kytketään vasta opettajan tarkastuksen jälkeen ja irrotetaan aina, kun drone ei ole käytössä. Kytkettynä akku voi purkautua liian tyhjäksi.
- Akku ladataan ohjainkortin micro-USB-liitännästä, ei micro:bitin liitännästä. Punainen valo tarkoittaa, että akku latautuu, ja vihreä, että lataus on valmis. Lataus kestää noin tunnin. Akkua ei ladata ilman valvontaa.
- Älä taivuta, paina tai avaa akkua. Vaurioitunut tai turvonnut akku viedään opettajalle.

## Työvaiheet

1. Lajittele osat ja vertaa niitä ohjeen osaluetteloon. Kerro opettajalle, jos jotain puuttuu.
2. Kokoa runko ja kiinnitä moottorit ohjeen mukaan. Tarkista jokaisen moottorin tyyppi ja paikka ennen kiinnitystä.
3. Kiinnitä ohjainkortti. Kortin viisi mutteria kiristetään kevyesti: ne johtavat sähköisen signaalin korttien välillä, joten löysä mutteri estää dronea toimimasta.
4. Kiinnitä micro:bit paikalleen.
5. Tarkasta työ parin kanssa osakartan avulla. Pyydä opettajan tarkastus.
6. Aseta drone tasaiselle alustalle ja kytke akku. Älä liikuta dronea käynnistyksen aikana.
7. Lue näyttö: kirjaimet G, M ja C kertovat, että gyroskooppi löytyi, moottoriohjain löytyi ja kalibrointi on valmis.
8. Tee moottoritesti ohjaimella ilman potkureita: käynnistä moottorit, lisää kaasua ja pysäytä ne ravistamalla ohjainta.
9. Irrota akku.

## Kuvat ja esimerkkikoodi

Rakennusohjeen kuvat ovat valmistajan ohjeessa, jonka opettaja jakaa. Piirrä oma osakartta: dronen ääriviiva ylhäältä, neljä moottoria ja niiden pyörimissuunnat, ohjainkortti, micro:bit ja akku sekä nuolet, jotka näyttävät, mistä virta ja ohjaus kulkevat.

Dronen ohjelma ladataan micro:bitille valmiina. Sitä tutkitaan ohjeessa [Air:bit 2:n radio-ohjain ja ohjausohjelma](ahjo-airbit-ohjaus.html).

## Testaa ja mittaa

- Näkyvätkö käynnistyksessä kirjaimet G, M ja C?
- Käynnistyvätkö kaikki neljä moottoria, ja pysähtyvätkö ne ravistuksesta?
- Punnitse drone ilman akkua ja akun kanssa. Kuinka suuri osa massasta on akkua?

Kirjaa tulokset. Dronen massaa tarvitaan, kun lasket leijuntaan tarvittavan nostovoiman.

## Jos jokin ei toimi

Ohjeet ovat valmistajan vianetsinnästä.

| Havainto | Kokeile |
|---|---|
| Näyttö ilmoittaa, että gyroskooppia ei löydy | Kiristä kortin viisi mutteria kevyesti, irrota akku ja kytke se uudelleen. |
| Näyttö ilmoittaa, että moottoriohjainta ei löydy | Irrota USB-kaapeli ja akku ja kytke sitten vain akku. |
| Moottorit eivät käynnisty | Tarkista, että ohjain ja drone ovat samalla radioryhmällä ja että ohjaimen näytön pisteet liikkuvat, kun kallistat sitä. Kokeile valmistajan valmista ohjainohjelmaa. |
| micro:bit näyttää virhenumeron | Avaa ohjelma MakeCodessa ja lataa se sieltä uudelleen. |
| Kalibrointi ei onnistu | Drone ei ole tasaisella alustalla tai sitä liikutettiin. Irrota akku ja aloita alusta. |
| Ohjainkortin valo on punainen | Akku pitää ladata. Älä yritä lentää. |

## Jatkotehtävä

Laske akun energia sen merkinnöistä: $E = QU$, kun varaus $Q$ on ilmoitettu milliampeeritunteina ja jännite $U$ voltteina. Montako joulea akkuun mahtuu? Vertaa tulosta puhelimesi akkuun.

## Dokumentoi

Liitä projektipäiväkirjaan

- osakartta
- valokuva kootusta dronesta ilman potkureita
- käynnistyksen vaiheet ja moottoritestin tulos
- yksi asia, jonka tekisit kokoamisessa toisin.

## Opettajalle: valmistelu

- Lataa valmistajan rakennus- ja ohjelmointiohje (*Airbit 2 – Building and coding*) sivulta [Air:bit-dokumentit](https://www.makekit.no/en/docs/airbit-docs/). Käytä mustan kortin (Air:bit 2) ohjeita, älä sinisen kortin (Air:bit 1).
- Valmistajan aika-arvio on 2–3 tuntia kokoamiseen ja 3–4 tuntia ohjaimen ohjelmointiin.
- Ohjeen sivujärjestyksessä potkurit kiinnitetään ennen ohjelmointia, mutta ohjeen turvallisuussivu neuvoo kiinnittämään ne vasta, kun rakentaminen ja ohjelmointi on tehty ja moottorien käynnistys ja pysäytys on kokeiltu. Pidä potkurit itselläsi lentotunteihin asti.
- Lataa droneohjelma micro:biteille etukäteen ja numeroi sarjat, micro:bitit ja radioryhmät ryhmittäin.
- Koulun sarjoissa on potkurisuojat. Ne kiinnitetään valmistajan ohjeen mukaan lentotunnilla samalla kuin potkurit.
- Sarjoja on 10 ja micro:bitejä 20, eli kaksi jokaista sarjaa kohti. Micro:bitit ovat versiota V2.
- Eniten kuluvat potkurit ja moottorit. Varaa varaosia.
- Dronen massaa ja lentoaikaa valmistaja ei ilmoita: ne mitataan itse.
- Tiedot on luettu valmistajan ohjeesta 12.11.2026.
