## Haaste

Suunnittele pidike, joka kiinnittyy pöydän reunaan ilman ruuveja ja pitää laturin johdon paikallaan. Pidike on onnistunut, jos se menee pöydän reunaan käsin painamalla, pysyy paikallaan eikä naarmuta pöytää. Tämä onnistuu vain, jos mittaat tarkasti ja jätät mittoihin oikean välyksen.

Työ kestää yhden noin 75 minuutin kerran. Malli tulostetaan [3D-tulostuksen aloitusohjeen](ahjo-3d-tulostus.html) mukaan.

## Oppimistavoitteet

Työn jälkeen osaat

- mitata kappaleen työntömitalla ja kirjata mitat yksiköineen
- rakentaa mallin perusmuodoista lisäämällä ja poistamalla kappaleita
- selittää, mitä välys tarkoittaa ja miksi tulostettavan osan mitat eivät voi olla täsmälleen samat kuin vastakappaleen
- tallentaa mallin tulostettavaan muotoon (STL tai 3MF)
- arvioida kappaleen tilavuuden ja massan ennen tulostamista.

## Lähtötaso ja ennakkotaidot

Et tarvitse aiempaa kokemusta 3D-mallinnuksesta. Tarvitset Tinkercad-tunnukset, jotka opettaja antaa tai joilla kirjaudut koulun ohjeen mukaan. Pinta-alan ja tilavuuden laskeminen sekä tiheyden käsite (luku [Tiheys](fy1-7.html)) auttavat massan arvioinnissa.

## Laitteet ja materiaalit

Mallinnetaan Tinkercadilla, joka toimii selaimessa eikä vaadi asennusta. Kun perusteet ovat hallussa, jatketaan Onshapella, joka sekin toimii selaimessa ja jossa mitat voi antaa muuttujina (jatkotehtävä 2). Fusion on vaihtoehto niille, jotka haluavat asennettavan ohjelman. Ahjon tietokoneet ovat vasta hankinnassa.

| Tarvike | Määrä |
|---|---|
| Tietokone ja hiiri, jossa on rullapainike | 1 |
| Tinkercad-tunnus (jatkossa Onshape-tunnus) | 1 |
| Työntömitta | 1 |
| Ruutupaperia ja kynä luonnokseen | 1 |
| Pöytä tai levy, johon pidike tehdään | 1 |

## Turvallisuus ja perehdytys

Mallintaminen on näyttötyötä. Pidä tauko noin puolen tunnin välein ja säädä tuoli ja näyttö sopivalle korkeudelle. Työntömitan kärjet ovat teräviä, joten käsittele sitä varoen. Ahjon turvallisuusohjeet ovat valmisteilla, ja tulostamisen turvallisuudesta kerrotaan aiheessa [3D-tulostuksen turvallisuus](ahjo-turvallisuus.html#3d-tulostus).

## Työvaiheet

1. Mittaa pöytälevyn paksuus työntömitalla kolmesta eri kohdasta ja laske keskiarvo. Kirjaa tulos kymmenesosamillimetrin tarkkuudella, esimerkiksi $t = 18{,}0\,\text{mm}$.
2. Valitse välys $v$. Kun kaksi kappaletta liitetään toisiinsa, väliin tarvitaan rako, koska tulostin ei tee mittoja täsmälleen oikein ja tulostettu muovi on usein hieman suunniteltua leveämpää. Kokeile aluksi arvoa $v = 0{,}4\,\text{mm}$. Jos haluat varmistaa sopivan välyksen, tulosta ensin sovitekoe (jatkotehtävä 1).
3. Laske pidikkeen haarojen väli:
   $$\begin{aligned}&a = t + v\\ &= 18{,}0\,\text{mm} + 0{,}4\,\text{mm}\\ &= 18{,}4\,\text{mm}.\end{aligned}$$
4. Piirrä ruutupaperille pidikkeen poikkileikkaus ja merkitse siihen mitat: haarojen pituus $30\,\text{mm}$, seinämän paksuus $4\,\text{mm}$, haarojen väli $a$ ja pidikkeen leveys $20\,\text{mm}$. Kuvassa alla näet, miltä poikkileikkaus näyttää.
5. Tee mallinnusohjelmassa umpinainen särmiö, joka on pidikkeen ulkomittojen kokoinen: syvyys $30\,\text{mm}$, korkeus $a + 2 \cdot 4\,\text{mm} = 26{,}4\,\text{mm}$ ja leveys $20\,\text{mm}$.
6. Tee toinen särmiö, joka on haarojen välin korkuinen: korkeus $a = 18{,}4\,\text{mm}$, syvyys $30\,\text{mm}$ ja leveys $24\,\text{mm}$. Se on pidikettä leveämpi, jotta se menee varmasti sivujen läpi. Muuta se reiäksi eli poistettavaksi kappaleeksi (Tinkercadissa valitse muodon asetuksista Reikä).
7. Aseta reikä niin, että sen alareuna on $4\,\text{mm}$ ensimmäisen särmiön alareunan yläpuolella, se ulottuu $2\,\text{mm}$ kummankin sivun yli ja sen takareunan taakse jää $4\,\text{mm}$ paksu seinämä. Reiän etupää jää silloin pidikkeen ulkopuolelle. Valitse molemmat ja ryhmitä ne (Tinkercadissa Ryhmitä tai Ctrl + G). Nyt sinulla on U-muotoinen pidike.
8. Lisää johdolle koukku: pieni lieriö pidikkeen yläpintaan, josta poistetaan johdon paksuinen lieriö ja kapea rako johdon sisään painamista varten. Mittaa johdon halkaisija ja lisää siihenkin välys.
9. Pyöristä tai viistä pöydän puoleiset reunat, jos ohjelmassa on siihen työkalu. Terävä reuna naarmuttaa pöytää.
10. Tarkista mitat ohjelman mittatyökalulla ja tallenna malli STL- tai 3MF-muodossa. Nimeä tiedosto niin, että siitä näkee tekijän ja version, esimerkiksi `pidike_v1_meikalainen.stl`.

## Kuvat ja esimerkkikoodi

Useimmissa mallinnusohjelmissa reikä tehdään kappaleena, joka vähennetään toisesta. Reikäkappale kannattaa tehdä hieman pidemmäksi kuin kappale, josta se poistetaan. Silloin reikä menee varmasti läpi eikä pintaan jää ohutta kalvoa.

<svg data-fig="csg"></svg>

Pidikkeen poikkileikkaus pöydän reunassa. Välys on piirretty kuvaan liioitellun suureksi.

<svg data-fig="pidike"></svg>

Sovitekokeessa samaan kappaleeseen tehdään useita eri kokoisia reikiä. Reikiin kokeillaan tappia, ja näin selviää, mikä välys toimii juuri tällä tulostimella.

<svg data-fig="sovitekoe"></svg>

## Testaa ja mittaa

- Arvioi pidikkeen tilavuus ennen tulostamista. Jaa poikkileikkaus suorakulmioiksi: kaksi haaraa ($30\,\text{mm} \cdot 4\,\text{mm}$) ja niiden välinen seinämä ($18{,}4\,\text{mm} \cdot 4\,\text{mm}$). Kerro poikkileikkauksen pinta-ala pidikkeen leveydellä. Tilavuudeksi tulee noin $6{,}3\,\text{cm}^3$.
- Laske, paljonko umpinainen pidike painaisi PLA-muovista, jonka tiheys on $\rho = 1{,}24\,\text{g/cm}^3$. Vertaa tulosta viipalointiohjelman arvioon, kun tulostat pidikkeen. Miksi ohjelman arvio on pienempi?
- Kun pidike on tulostettu, mittaa sen haarojen väli työntömitalla ja vertaa suunnittelemaasi arvoon $a$. Kirjaa ero muistiin. Se kertoo, kuinka tarkasti tulostin tekee mitat.

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| Reikä ei näy mallissa | Kappaleita ei ole ryhmitetty, tai reikäkappale ei ole reikä | Valitse molemmat ja ryhmitä. Tarkista, että poistettava kappale on merkitty reiäksi. |
| Reiän pohjaan jää ohut kalvo | Reikä on täsmälleen yhtä pitkä kuin kappale | Pidennä reikäkappaletta niin, että se menee yli molemmista päistä. |
| Pidike ei mahdu pöydän reunaan | Välys on liian pieni tai paksuus on mitattu väärin | Mittaa uudelleen. Kasvata välystä $0{,}2\,\text{mm}$ kerrallaan. |
| Pidike on löysä | Välys on liian suuri | Pienennä välystä tai tee haaroihin pieni kohouma, joka puristaa levyä. |
| Malli on väärän kokoinen tulostusohjelmassa | Yksikkö on vaihtunut tallennuksessa | Tarkista, että ohjelmassa on käytössä millimetrit. |

## Jatkotehtävä

1. Sovitekoe. Mallinna koekappale, jossa on neljä reikää halkaisijoiltaan $10{,}0\,\text{mm}$, $10{,}2\,\text{mm}$, $10{,}4\,\text{mm}$ ja $10{,}6\,\text{mm}$, sekä tappi, jonka halkaisija on $10{,}0\,\text{mm}$. Tulosta ne ja kirjaa, mikä reikä on tiukka, mikä sopiva ja mikä löysä.
2. Parametrinen malli Onshapessa. Piirrä pidikkeen U-muotoinen poikkileikkaus luonnokseksi ja pursota se $20\,\text{mm}$:n levyiseksi. Tee mitoista muuttujia ($t$, $v$, seinämän paksuus). Silloin saat saman pidikkeen eri pöytiin vaihtamalla yhden luvun.
3. Käyttäjälähtöinen suunnittelu. Kysy luokkatoverilta, mitä hän pitäisi pöydän reunassa: kuulokkeita, laukkua vai puhelinta. Muokkaa pidikettä hänen tarpeensa mukaan.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- mitatut paksuudet, niiden keskiarvo ja valitsemasi välys perusteluineen
- luonnoksesi mittoineen ja kuvakaappaus valmiista mallista
- tilavuus- ja massa-arviosi laskuineen
- tulosteen mitattu haarojen väli ja ero suunniteltuun
- mitä muuttaisit seuraavaan versioon ja miksi.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ei ole vielä kokeiltu Ahjon koneilla. Ohjelmiksi on valittu Tinkercad aloitukseen ja Onshape jatkoon (molemmat selaimessa, ei asennusta). Tarkista ennen ensimmäistä kertaa kummankin ohjelman käyttöehdot ja ikärajat sekä se, miten opiskelijat kirjautuvat (esimerkiksi Tinkercadin opettajan luokkatila).
- Varaa työntömittoja vähintään yksi kahta opiskelijaa kohti.
- Jos tulostusaikaa on vähän, tulosta sovitekoe valmiiksi yhdellä tulostimella ja anna opiskelijoille sopiva välys valmiina.
- Massan arviointi yhdistää työn fysiikan lukuun [Tiheys](fy1-7.html), ja kappaleen käyttäjälähtöinen kehittäminen johdattaa Ahjo 2 -opintojakson suunnitteluprosessiin.
- Ohjeen rakenne on saanut vaikutteita Prusan opetusmateriaalien projektipohjasta. Teksti ja kuvat on tehty Ruukkilabraan.
