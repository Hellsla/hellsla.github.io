## Haaste

Tulosta mallisi niin, että ensimmäinen kerros tarttuu alustaan, kappale kestää käytön ja tiedät, mitä tuloste maksoi. Kun osaat valita tulostusasennon ja tarkistaa ensimmäisen kerroksen, suurin osa epäonnistuneista tulosteista jää syntymättä.

Esimerkkinä tulostetaan [3D-mallinnuksen alkeissa](ahjo-3d-mallinnus.html) suunniteltu pidike. Valmistelu kestää noin 30 minuuttia. Itse tulostus kestää kappaleen koosta riippuen puolesta tunnista useaan tuntiin.

## Oppimistavoitteet

Työn jälkeen osaat

- viedä mallin viipalointiohjelmaan ja tarkistaa sen mittakaavan
- valita tulostusasennon niin, että kappale kestää kuormituksen
- valita kerroskorkeuden, täytön ja tukirakenteet ja perustella valintasi
- tarkkailla ensimmäistä kerrosta ja keskeyttää tulostuksen, jos se epäonnistuu
- laskea tulosteen materiaalikustannuksen ja testata sen lujuuden.

## Lähtötaso ja ennakkotaidot

Sinulla on valmis malli STL- tai 3MF-muodossa. Olet käynyt opettajan perehdytyksen siihen tulostimeen, jota käytät. Ilman perehdytystä tulostinta ei käytetä.

## Laitteet ja materiaalit

Ahjon tulostimet ovat vasta hankinnassa. Ohje on kirjoitettu tavalliselle FDM-tulostimelle, joka tulostaa sulatetusta muovilangasta kerros kerrallaan. Laitekohtaiset asetukset tarkentuvat, kun tulostimet on hankittu.

| Tarvike | Määrä |
|---|---|
| 3D-tulostin, jolla saat tulostaa | 1 |
| Viipalointiohjelma PrusaSlicer | 1 |
| PLA-tulostuslanka | noin $10\,\text{g}$ |
| Lasta tulosteen irrottamiseen | 1 |
| Työntömitta | 1 |
| Punnukset ja koukku lujuustestiin | 1 sarja |
| Suojalasit lujuustestiin | 1 |

## Turvallisuus ja perehdytys

Ahjon 3D-tulostuksen turvallisuusohje on valmisteilla: katso aihe [3D-tulostuksen turvallisuus](ahjo-turvallisuus.html#3d-tulostus). Ennen kuin se on hyväksytty, noudata opettajan perehdytystä ja ainakin näitä varotoimia:

- Suutin on käytön aikana noin $200\,{}^\circ\text{C}$ ja alusta noin $60\,{}^\circ\text{C}$. Älä koske kumpaankaan, ja odota, että alusta jäähtyy ennen kuin irrotat tulosteen.
- Älä kurota tulostimeen sen liikkuessa. Hiukset kiinni ja korut pois.
- Sulava muovi vapauttaa ilmaan pienhiukkasia. Tulosta vain tilassa, jonka ilmanvaihto on kunnossa, äläkä istu koko tulostusta tulostimen vieressä.
- Irrota tuloste lastalla itsestäsi poispäin.
- Lujuustestissä katkeava kappale voi sinkoutua. Käytä suojalaseja, äläkä seiso punnusten alla.

## Työvaiheet

1. Avaa viipalointiohjelma PrusaSlicer ja valitse siitä oikea tulostin ja materiaali (PLA).
2. Tuo malli ohjelmaan. Tarkista mitat: jos pidike näyttää sata kertaa liian pieneltä tai suurelta, malli on tallennettu väärässä yksikössä.
3. Valitse tulostusasento. Tulostettu kappale on lujin, kun kuormitus kulkee kerrosten suuntaisesti, ja heikoin, kun kuormitus yrittää repiä kerroksia irti toisistaan. Aseta pidike kyljelleen niin, että U-muotoinen poikkileikkaus on alustan suuntainen. Silloin haarat kestävät taivutusta. Kuva alla näyttää eron.
4. Valitse kerroskorkeus $0{,}2\,\text{mm}$ ja täyttö $20\,\%$. Ohuempi kerros tekee pinnasta sileämmän, mutta tulostus kestää kauemmin. Suurempi täyttö tekee kappaleesta lujemman ja painavamman.
5. Tarkista, tarvitaanko tukirakenteita. Jos jokin osa kappaleesta on tyhjän päällä tai sen kaltevuus on yli noin $45^\circ$ pystysuorasta, se tarvitsee tuen. Kyljellään oleva pidike ei tarvitse tukia.
6. Viipaloi malli. Kirjaa muistiin ohjelman arvioimat tulostusaika ja massa.
7. Esikatsele kerrokset. Selaa kerroksia alusta alkaen ja tarkista, että ensimmäinen kerros koskettaa alustaa koko kappaleen alalta.
8. Varmista, että alusta on puhdas, ja aloita tulostus opettajan ohjeen mukaan.
9. Seuraa ensimmäistä kerrosta alusta loppuun. Vertaa sitä alla olevaan kuvaan. Jos lanka ei tartu tai suutin raapii alustaa, keskeytä tulostus heti ja kerro opettajalle.
10. Kun tulostus on valmis, odota, että alusta jäähtyy. Irrota tuloste ja poista mahdolliset reunukset tai tuet varovasti.

## Kuvat ja esimerkkikoodi

Sama palkki kahdessa tulostusasennossa. Ohuet viivat ovat tulostuskerroksia, ja punainen nuoli on palkkiin vaikuttava voima.

<svg data-fig="suunta"></svg>

Ensimmäinen kerros leikkauskuvana kolmella suuttimen korkeudella. Hyvässä ensimmäisessä kerroksessa langat ovat hieman litistyneitä ja koskettavat toisiaan.

<svg data-fig="ensikerros"></svg>

## Testaa ja mittaa

- Laske materiaalikustannus. Jos viipalointiohjelma arvioi massaksi $m = 5\,\text{g}$ ja lanka maksaa $25\,\text{€}$ kilolta eli $0{,}025\,\text{€/g}$, materiaali maksaa $5\,\text{g} \cdot 0{,}025\,\text{€/g} \approx 0{,}13\,\text{€}$. Laske sama omalle tulosteellesi.
- Punnitse tuloste ja vertaa massaa ohjelman arvioon.
- Lujuustesti: tulosta kaksi samanlaista suoraa palkkia, toinen makuulleen ja toinen pystyyn. Kiinnitä palkin toinen pää ja ripusta toiseen päähän punnuksia vähitellen lisäten, kunnes palkki taipuu selvästi tai katkeaa. Kirjaa suurin massa, jonka kumpikin kesti. Laske vastaava paino $G = mg$. Esimerkiksi $2{,}0\,\text{kg}$:n massaan kohdistuva paino on $G = 2{,}0\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 20\,\text{N}$. Painosta kerrotaan luvussa [Paino, kitka ja kalteva taso](fy4-6.html).

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| Lanka ei tartu alustaan | Suutin on liian korkealla tai alusta on rasvainen | Pysäytä tulostus. Pyydä opettajaa säätämään ensimmäisen kerroksen korkeus, ja puhdista alusta. |
| Suutin raapii ja lanka on ohut ja uurteinen | Suutin on liian matalalla | Pysäytä tulostus ja pyydä opettajaa säätämään korkeus. |
| Kappaleen kulmat nousevat irti | Kappale kutistuu jäähtyessään | Lisää reunus (brim) ja vältä vetoa tulostimen ympärillä. |
| Ilmaan tulostuva osa roikkuu | Tukirakenne puuttuu | Lisää tuet tai käännä kappaletta. |
| Tulosteessa on rihmoja | Suutin vuotaa siirtymissä | Pienet rihmat voi poistaa jälkikäsittelyssä. Jos niitä on paljon, kerro opettajalle. |
| Tulostin pysähtyy kesken | Lanka loppui tai juuttui | Älä yritä avata tulostinta itse. Kerro opettajalle. |

## Jatkotehtävä

1. Täytön vaikutus. Tulosta sama palkki täytöillä $10\,\%$, $20\,\%$ ja $40\,\%$. Tee lujuustesti ja piirrä kuvaaja, jossa on suurin kestetty massa täytön funktiona. Onko riippuvuus lineaarinen?
2. Ajan ja laadun vaihtokauppa. Viipaloi sama malli kerroskorkeuksilla $0{,}1\,\text{mm}$, $0{,}2\,\text{mm}$ ja $0{,}3\,\text{mm}$, ja kirjaa tulostusajat. Milloin hitaampi tulostus kannattaa?
3. Kestävä valinta. Selvitä, mitä Ahjossa tehdään epäonnistuneille tulosteille. Laske, paljonko materiaalia luokkasi epäonnistuneisiin tulosteisiin kuluu jakson aikana.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valitsemasi tulostusasento, kerroskorkeus, täyttö ja tukirakenteet sekä perustelut niille
- ohjelman arvioima ja punnittu massa, tulostusaika ja materiaalikustannus
- valokuva ensimmäisestä kerroksesta ja valmiista tulosteesta
- lujuustestin tulokset taulukkona
- jos tulostus epäonnistui: kuva, todennäköinen syy ja mitä muutit. Hyvin dokumentoitu epäonnistuminen on arvokas tulos.

## Opettajalle: valmistelu

- Tämä on luonnos: Ahjon tulostimia ei ole vielä valittu, eikä ohjetta ole kokeiltu niillä. Viipalointiin käytetään PrusaSliceria. Täydennä tulostinkohtaiset profiilit ja asetukset sekä tulostusjonon käytäntö, kun laitteet on hankittu.
- Ohjeen turvallisuuskohdat ovat yleisiä varotoimia. Ne eivät korvaa koulun hyväksymää 3D-tulostuksen turvallisuusohjetta, joka on vielä valmisteilla.
- Tarkista ilmanvaihto tulostinten sijoituspaikassa ja se, voiko tulostimen jättää käymään valvomatta.
- Tulosta lujuustestin palkit valmiiksi, jos tulostusaikaa on vähän. Varaa punnukset, joiden yhteismassa on vähintään $3\,\text{kg}$.
- Lujuustesti ja kustannuslaskelma yhdistävät työn fysiikkaan (paino, luku [Paino, kitka ja kalteva taso](fy4-6.html)) ja yrittäjyyteen (tuotteen hinta Ahjo 2 -projekteissa).
- Ohjeen rakenne on saanut vaikutteita Prusan opetusmateriaalien projektipohjasta. Teksti ja kuvat on tehty Ruukkilabraan.
