# Oppitunnin vaiheiden käyttöliittymä pedagogisen tarkoituksen mukaan

Opettajan linjaus 10.11.2026: Ruukkilabran tavoite ei ole näyttää painetulta oppikirjalta vaan olla fysiikan
oppimisympäristö, jota painetulla kirjalla ei voisi toteuttaa. Kolme periaatetta yhdessä:

- **B, oppikirja:** selkeys, luettavuus, johdonmukaisuus.
- **C, virtuaalilaboratorio:** vuorovaikutteisuus, kokeellisuus, tutkiva oppiminen.
- **A, käytettävyys:** orientaatio ja oppimisen etenemisen näkyminen.

Tämä muistio arvioi jokaisen seitsemästä vaiheesta erikseen: mikä on vaiheen pedagoginen tehtävä, mitä nykyinen
toteutus tekee, mikä periaate vaiheessa painaa eniten ja mitä kannattaa muuttaa. Se korvaa auditoinnin (10.11.2026)
suosituksen yhdestä oppikirjamaisesta asettelusta koko oppitunnille. Mitään tässä ei ole vielä toteutettu; jokainen
ehdotus on oma pieni pull request, ja kohdassa 9 on järjestys.

Havainnot perustuvat tuotantosivuston tarkastukseen (fy1-3, fy5-4, fy9-liike, fy10-heiluri, en/fy14-plasma,
fi-easy/fy1-3) leveyksillä 390, 820, 1440 ja 1920 px. Opiskelijoilla ei ole testattu mitään; kohdat, jotka pitää
testata ennen toteutusta, on merkitty.

## 1. Yhteenveto

| Vaihe | Pedagoginen tehtävä | Painottuva periaate | Nykytila | Suurin muutos |
|---|---|---|---|---|
| 1 Pohdinta | herättää kysymys, aktivoida aiempi tieto | B + C | hyvä | ilmiö näkyviin ennen tekstiä, yksi oma vastaus |
| 2 Ennusta | sitoutua ennusteeseen ennen näyttöä | C | hyvä, mutta piilossa | ennuste kulkee mukaan Tutki-vaiheeseen |
| 3 Tutki | hankkia näyttö itse | C | hyvä työpöydällä, heikko puhelimella | laboratorionäkymä: kuva pysyy, mittaukset kertyvät |
| 4 Teoria | rakentaa malli näytöstä | B | hyvä | lukupalsta ennallaan, linkit omaan näyttöön |
| 5 Esimerkit | mallintaa ratkaisu, häivyttää tuki | B + A | erinomainen | ei rakenteellista muutosta |
| 6 Tehtävät | harjoitella itsenäisesti | A | toimiva, raskas | ydinpolku näkyviin, ohjainten järjestys |
| 7 Itsearvio | tarkistaa ja arvioida | A | sekava järjestys | lopputesti ensin, arvio sen perusteella |

Johtopäätös: vain Teoria ja Esimerkit hyötyvät oppikirjamaisesta lukupalstasta. Ennusta ja Tutki ovat laboratoriotyötä
ja tarvitsevat leveän, tilaa pitävän näkymän. Tehtävät ja Itsearvio ovat työkalu, jossa ratkaisee nopeus ja tilan
näkyminen. Yhtenäisyys syntyy yhteisistä osista (typografia, värit, painikkeet, palaute, vaihepalkki), ei siitä, että
jokainen vaihe on samanlevyinen palsta.

## 2. Pohdinta

**Tehtävä.** Tehdä ilmiöstä kysymys, johon opiskelija haluaa vastauksen, ja nostaa esiin se, mitä hän jo tietää tai
luulee tietävänsä.

**Nyt.** Otsikko, Miksi-kysymys, avauskuvitus, Tällä tunnilla opit, Pohjatiedot linkkeineen, selite ydinpolusta, sitten
lyhyt tilannekuvaus ja kysymys. Kuvitus ja kysymys ovat hyviä. Ennen itse pohdintaa on kuitenkin viisi lohkoa
orientoivaa tietoa, ja pohdintakysymykseen ei vastata mitenkään: opiskelija voi vierittää ohi.

**Arvio.** Vaihe on enimmäkseen B:tä (lyhyt, hyvin ladottu teksti), mutta sen teho syntyy C:stä: opiskelijan pitää
sanoa jotain itse. Nykyinen toteutus on luettava muttei sitouta.

**Ehdotus.**
1. Pohdintakysymyksen alle yksi vapaa tekstikenttä, "Mitä arvelet?", joka tallentuu kuten ennusteet ja näytetään
   uudelleen Teorian lopussa kohdassa Palaa ennusteisiisi. Ei tarkistusta, ei pisteitä. *Testattava:* kirjoittavatko
   opiskelijat siihen vai ohittavatko.
2. Pohjatiedot ja ydinpolun selite avattavaan riviin "Ennen kuin aloitat". Ne ovat tarpeen harvalle, ja nyt ne
   viivästyttävät kysymystä kaikilta.
3. Fontti sama kuin muualla oppitunnissa; Fraunces vain Miksi-kysymykseen (auditoinnin ongelma 6).

**Ei muuteta.** Avauskuvitus, Miksi-kysymys, tavoitteiden muoto.

## 3. Ennusta

**Tehtävä.** Sitoutunut ennuste ennen näyttöä. Oppiminen tapahtuu, kun ennuste ja havainto kohtaavat, joten ennusteen
pitää olla näkyvissä sillä hetkellä, kun havainto tehdään.

**Nyt.** Suljettu laatikko "Tee ennusteet ennen tutkimista, 3 kysymystä". Avattuna monivalinta ja vapaaehtoinen
perustelu, vastaus lukitaan. Tämä on pedagogisesti oikein. Ennuste kuitenkin jää laatikkoon: Tutki-vaiheessa
opiskelija ei näe, mitä ennusti, ja vertailu tapahtuu vasta Teorian lopussa kohdassa Palaa ennusteisiisi.

**Arvio.** Puhdas C. Painetussa kirjassa ennustetta ei voi lukita eikä kuljettaa mukana; tässä voi.

**Ehdotus.**
1. Kun ennuste on annettu, se näkyy Tutki-vaiheessa sen kokeen kohdalla, jota se koskee: "Ennustit: neljä kertaa
   niin suuri kitka". Kun koe on tehty, opiskelija merkitsee itse "piti / ei pitänyt". Sivu ei arvostele ennustetta.
2. Laatikko on suljettu, kunnes opiskelija tulee vaiheeseen ensimmäisen kerran; sen jälkeen se pysyy auki, kunnes
   ennusteet on annettu. Nyt suljettu laatikko näyttää valinnaiselta, vaikka se on ydinpolkua. *Testattava:* kuinka
   moni avaa laatikon nyt. Tieto on jo selaimessa (vaiheen tehty-merkki), mutta sitä ei kerätä, joten tämä selviää
   vain luokassa.

**Ei muuteta.** Sitoutuminen ennen palautetta, perustelukenttä, yksi lukitus.

## 4. Tutki

**Tehtävä.** Opiskelija hankkii näytön itse: muuttaa yhtä suuretta, pitää muut vakioina, kirjaa mittaukset ja näkee
säännönmukaisuuden.

**Nyt.** Työpöydällä koeohje ja mittaustaulukko vasemmalla, simulaatio oikealla tarttuvana. Simulaatiossa kuva,
voimakuvio, säätimet, lukemat ja kolme suljettua selitettä. Tämä on jo laboratorio, ja "Kirjaa mittaus" on juuri
oikea idea. Ongelmat:
- Puhelimella kuva, säätimet ja lukemat ovat allekkain eivätkä mahdu yhdelle näytölle, joten säätäessä kuva vierii
  pois. Syy ja seuraus eivät näy yhtä aikaa.
- Mittaustaulukko on koeohjeen sisällä pienenä. Kertyvä aineisto on vaiheen tärkein tuotos, mutta se näyttää
  sivuseikalta, eikä siitä piirry kuvaajaa.
- Simulaation tekstit ovat eri fonttia kuin säätimet.

**Arvio.** Tässä vaiheessa oppikirjamainen palsta olisi virhe. Vaiheen pitää olla leveä työtaso.

**Ehdotus.**
1. **Puhelin:** simulaation kuva tarttuu lohkon yläreunaan (enintään 40 % näytön korkeudesta), säätimet vierivät sen
   alla, tärkein lukema kuvan päällä. Tämä on koko muistion suurin yksittäinen parannus puhelinkäyttäjälle.
   *Testattava* oikealla puhelimella jokaisessa simulaatiossa; korkeudet vaihtelevat.
2. **Mittaukset näkyviksi:** kirjatut mittaukset piirtyvät pisteinä pieneen kuvaajaan taulukon viereen sitä mukaa kuin
   niitä kirjataan (esim. kitka nopeuden funktiona). Säännönmukaisuus löytyy omasta datasta ennen kuin Teoria kertoo
   sen. Tämä on uusi ominaisuus ja vaatii simulaatiokohtaisen tiedon siitä, mitkä suureet ovat akseleilla; aloitetaan
   yhdestä luvusta.
3. Oma ennuste näkyy kokeen kohdalla (kohta 3).

**Ei muuteta.** Työpöydän rinnakkaisasettelu (simulaatio on jo leveämpi puoli), kokeen rakenne (alkutila, vakiot,
muutettava suure), Aseta alkutila, kolme selitelaatikkoa, koko
näytön tila, simulaatioiden fysiikka.

## 5. Teoria

**Tehtävä.** Rakentaa malli siitä, mitä opiskelija juuri näki, ja antaa sille nimet, kaavat ja rajat.

**Nyt.** Lukupalsta, kuvat kappaleen vieressä, kaavat omissa laatikoissaan, virhekäsitys, tiivistelmä ja käsitekortit.
Tämä on sivuston vahvin osa. Ongelmat ovat pieniä: otsikkotasot 18 ja 17 px eivät erotu, yksittäiset kappaleet ovat
liian pitkiä (virhekäsitys 180 sanaa), ja teoria ei viittaa opiskelijan omaan näyttöön, vaikka se on kahden
vierityksen päässä.

**Arvio.** Puhdas B. Tässä oppikirjan keinot ovat oikeat, ja nykyinen 38 rem:n palsta on hyvä. Leveämpää
kahden raidan asettelua en enää suosittele koko oppitunnille: se hyödyttäisi vain tätä vaihetta, ja nykyinen "kuva
vieressä, kun se on kappaleen korkuinen" tekee saman vähemmällä.

**Ehdotus.**
1. Otsikkoasteikko: alaotsikko 20 px, sen alaotsikko 17 px, ja ylempään selvästi enemmän tilaa yläpuolelle.
2. Virhekäsitys omaksi toistuvaksi osakseen: väite yhdellä lauseella, sitten miksi se ei päde. Sisältötyötä, luku
   kerrallaan tarkastusten kautta.
3. Kaavan kohdalle linkki "Kokeile simulaatiossa", joka avaa simulaation samaan näkymään kuin tehtävät nyt avautuvat
   teorian viereen. Malli ja näyttö samalle näytölle. Tämä on C:tä B:n sisällä, eikä sitä voi tehdä paperilla.
4. Palaa ennusteisiisi näyttää ennusteen, pohdinnan vastauksen ja oman merkinnän siitä, pitikö ennuste.

**Ei muuteta.** Palstan leveys, kaavalaatikot, kuvien sijoittelu, käsitekortit, ääneen luku.

## 6. Esimerkit

**Tehtävä.** Näyttää asiantuntijan ratkaisu vaihe vaiheelta ja siirtää vastuu opiskelijalle: ensin seurataan, sitten
valitaan, sitten ratkaistaan vihjeiden kanssa.

**Nyt.** Esimerkki 1 avautuu seitsemässä vaiheessa, Esimerkki 2 etsii virheen, Esimerkki 3 valitsee oikean kuvion,
Esimerkki 4 on laskettava vihjeillä. Tuki häivytetään juuri niin kuin pitää.

**Arvio.** B + A, ja toteutus on erinomainen. En ehdota rakenteellista muutosta.

**Ehdotus.** Vain kaksi pientä asiaa: vaiheittain avautuvassa esimerkissä "Vaihe 3/7" saa ohuen etenemisviivan, ja
vaiheen alun selittävä harmaa lause poistuu, kun vaiheiden väliin tulee "Seuraavaksi"-rivi (kohta 8).

## 7. Tehtävät

**Tehtävä.** Itsenäinen harjoittelu kolmella tasolla, välitön tarkistus, ratkaisu vasta oman yrityksen jälkeen.

**Nyt.** Kolme suljettua tasoa (8 + 8 + 5 tehtävää). Tehtävän rivillä tunniste, Ydintehtävä-merkki, Vastaus,
lukittu Näytä ratkaisu ja laajennuspainike ennen tehtävänantoa; sen alla Kirjoita ratkaisu, vastauskenttä ja
Tarkista. Tarkistus, vihjeet ja lukitus toimivat hyvin. Ongelmat: vastauksen paljastavat ohjaimet ovat ennen
kysymystä, ensisijainen painike vaihtuu (Esimerkeissä Tarkista, täällä Kirjoita ratkaisu), ja 21 tehtävän joukosta
ei näe, mitkä kuuluvat ydinpolkuun, ennen kuin avaa tason.

**Arvio.** Puhdas A. Tämä on työkalu, jota käytetään kymmeniä kertoja; jokainen ylimääräinen ohjain ja epäselvä tila
maksaa.

**Ehdotus.**
1. Järjestys: tehtävänanto → vastauskenttä ja Tarkista → toissijainen rivi (Kirjoita ratkaisu, Vastaus, Ratkaisu).
   Lukon viereen teksti "avautuu yrityksen jälkeen". *Riski:* tehtäväskriptit ja palautus lukevat nykyistä
   rakennetta; tehdään yhdessä luvussa ensin ja ajetaan palautus- ja tarkistustestit.
2. Vaiheen alkuun yksi rivi tilasta: "Ydintehtävät 2/4 tehty". Tieto on jo tallessa.
3. Tasojen otsikoihin tehtyjen määrä ("Taso 1 · 3/8").

**Ei muuteta.** Tasot, tarkistuksen toleranssit, vihjeet, Yritä ensin -lukitus, teorian viereen avautuva näkymä,
tehtävien numerointi, palautus.

## 8. Itsearvio

**Tehtävä.** Tarkistaa, osaako opiskelija luvun ydinasiat ilman tukea, ja saada hänet arvioimaan osaamisensa sanallista
kriteeriä vasten.

**Nyt.** Ensin tavoitearviot 1–3, sitten neljä tehtävää (Pohdinta-, Käsite-, Lasku- ja Selitystehtävä), jokaisen alla
oma arviointirivi. Arviointiasteikko sai 10.11.2026 näkyvät nimet. Jäljelle jää järjestys: opiskelija arvioi
tavoitteet ennen kuin on tehnyt tehtävät, joiden perusteella ne voisi arvioida, ja vaiheessa on 7–8 arviointiriviä.

**Arvio.** A. Arvion pitää perustua näyttöön, ja näyttö on juuri tehdyt tehtävät.

**Ehdotus.**
1. Järjestys käännetään: ensin tehtävät, sitten tavoitearviot. Vaiheen nimi "Testaa ja arvioi" (navigaatiossa
   edelleen lyhyt). *Huom.* vaiheen nimi on opettajan päätös 6.11.2026; muutos vaatii hänen hyväksyntänsä.
2. Tehtäväkohtaiset arviointirivit pois automaattisesti tarkistetuista tehtävistä (sivu kertoo jo, menikö oikein) ja
   säilyvät vain kirjoitetuissa vastauksissa, joita verrataan mallivastaukseen. *Riski:* opettajan arviointityökalu
   lukee nämä rivit; tarkistettava ennen muutosta, eikä vanhoja arvioita poisteta.
3. Tavoitearvion viereen näkyviin, miten tavoitteeseen liittyvät tehtävät menivät.

**Ei muuteta.** Asteikon arvot ja tallennus, tehtävätyypit, kertausehdotus väärän vastauksen jälkeen.

## 9. Vaiheiden välinen liima

Nämä koskevat kaikkia vaiheita ja ovat A:ta:

1. **Vaihepalkki puhelimella** tiivistyy muotoon "3/7 Tutki ▾", josta aukeaa koko lista tehtyine merkkeineen. Nyt
   palkista näkyy kolme vaihetta seitsemästä.
2. **Seuraavaksi-rivi** jokaisen vaiheen lopussa: "Seuraavaksi: Teoria". Sama osa kuin Jatka-rivi.
3. **Leveä näyttö (≥ 1600 px):** pohjafonttikoko kasvaa portaattomasti, jotta luokan takarivi näkee. Simulaatioiden
   17 px:n oletus pitää tarkistaa erikseen.

## 10. Ehdotettu järjestys

Jokainen rivi on oma pull request. Aiempi rivi ei riipu myöhemmästä, ellei toisin sanota.

| # | Muutos | Vaihe | Riski | Riippuu | Testattava ensin |
|---|---|---|---|---|---|
| 1 | Otsikkoasteikko ja yksi leipätekstifontti | 1, 4 | pieni (CSS) | – | ei |
| 2 | Vaihepalkki puhelimella + Seuraavaksi-rivi | kaikki | keskisuuri | – | puhelimella |
| 3 | Tarttuva simulaatiokuva puhelimella | 3 | keskisuuri | – | jokainen simulaatio |
| 4 | Tehtävän ohjainten järjestys, ydinpolun tila | 6 | keskisuuri | – | yksi luku ensin |
| 5 | Itsearvion järjestys | 7 | keskisuuri | opettajan päätös nimestä | arviointityökalu |
| 6 | Ennuste näkyy Tutki-vaiheessa | 2, 3 | keskisuuri | – | – |
| 7 | Pohdinnan oma vastaus, Ennen kuin aloitat | 1 | pieni | 6 (sama tallennus) | luokassa |
| 8 | Mittaukset kuvaajaksi | 3 | suuri (uusi ominaisuus) | – | yksi luku |
| 9 | Kokeile simulaatiossa -linkki teoriasta | 4 | keskisuuri | – | – |
| 10 | Virhekäsitysosa | 4 | pieni tekninen, suuri sisältötyö | – | – |

Auditoinnin moduulisivua koskevat ehdotukset (teemat omiksi lohkoikseen, loppukortit riveiksi) eivät kuulu tähän
muistioon. Ne muuttaisivat opettajan päätöksiä 4.–10.11.2026 (Kuvalaatat, yhtenäinen ruudukko, loppukorttien
kuvitukset), joten niistä tarvitaan erillinen päätös ennen kuin niihin kosketaan.

## 11. Mitä ei tehdä

- Oppituntia ei pilkota erillisiksi sivuiksi eikä kolmeen päävaiheeseen: seitsemän vaihetta säilyy.
- Koko oppitunnille ei tehdä yhtä oppikirjamaista kahden raidan asettelua.
- Leipätekstifonttia ei vaihdeta antiikvaan ilman vertailua opiskelijoilla.
- Fysiikan sisältöön, laskujen tarkistukseen, simulaatioiden malleihin, tallennusavaimiin, palautukseen ja opettajan
  työkaluihin ei kosketa näissä muutoksissa. Jos jokin muutos vaatii sitä, se sanotaan pull requestissa erikseen.
