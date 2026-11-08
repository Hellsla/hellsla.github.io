## Pikastartti

Teet pienen robotin, joka liikkuu ilman ohjelmaa. Se lähtee liikkeelle noin kymmenessä minuutissa, ja tarvitset vain hammasharjan pään, värinämoottorin, nappipariston ja kaksipuolista teippiä. Laitteita ei käytetä, joten laiteperehdytystä ei tarvita.

1. Kiinnitä kaksipuolisella teipillä värinämoottori harjan pään selkään, lähelle harjan etupäätä.
2. Teippaa nappiparisto moottorin taakse plusnapa ylöspäin niin, että moottorin toinen johto jää pariston alle.
3. Taivuta moottorin toinen johto pariston yläpinnalle ja paina se paikalleen pienellä teipinpalalla. Moottori alkaa väristä.
4. Laske robotti pöydälle. Se lähtee liikkeelle.

### Kokeile

Saa robotti liikkumaan pöydällä.

### Muokkaa

Anna robotille oma ulkoasu ja rakenna sille rata tai areena paperista tai pahvista.

### Haasta itsesi

Mittaa robotin nopeus kolmella toistolla ja selvitä, miten harjasten kulma vaikuttaa siihen. Ohje on alla Opi lisää -osassa.

## Haaste

Rakenna robotti, joka liikkuu tärisemällä. Värinämoottorin akselissa on epäkeskopaino, joka saa koko robotin värisemään. Kun harjakset ovat vinossa, jokainen värähdys työntää robottia hieman eteenpäin. Pieni robotti näyttää, miten moottori muuttaa sähköenergian liikkeeksi ja miten rakenne ohjaa liikettä.

Työ kestää noin 30 minuuttia. Areenan rakentamiseen ja kilpailuun kannattaa varata toinen puolituntinen.

## Oppimistavoitteet

Työn jälkeen osaat

- kytkeä moottorin paristoon ja katkaista virran
- selittää, miten epäkeskopaino ja vinot harjakset saavat robotin liikkumaan
- muuttaa robotin rakennetta ja havaita muutoksen vaikutuksen
- mitata nopeuden kolmella toistolla ja laskea keskiarvon.

## Lähtötaso ja ennakkotaidot

Et tarvitse aiempaa kokemusta. Nopeuden laskeminen kaavalla $v = \dfrac{s}{t}$ auttaa haasteessa. Kertaa tarvittaessa luku [Tasainen liike – nopeus, paikka ja kuvaajat](fy1-5.html).

## Laitteet ja materiaalit

| Tarvike | Määrä |
|---|---|
| Hammasharjan pää, jonka varsi on katkaistu | 1 |
| Värinämoottori, nappimalli tai sylinterimalli, $3\,\text{V}$ | 1 |
| Nappiparisto CR2032 ($3\,\text{V}$) | 1 |
| Kaksipuolinen teippi ja tavallinen teippi | 1 rulla |
| Viivain tai mittanauha ja sekuntikello | 1 + 1 |
| Koristeluun piippurassit, paperi tai tarrat | vapaasti |

Opettaja katkaisee hammasharjojen varret valmiiksi. Värinämoottorin johdot on usein valmiiksi kuorittu.

## Turvallisuus ja perehdytys

Työ ei vaadi laiteperehdytystä. Noudata kuitenkin näitä varotoimia:

- Nappiparisto on vaarallinen, jos sen nielaisee. Pidä paristot rasiassa ja palauta ne opettajalle tunnin lopussa.
- Älä yhdistä moottorin johtoja toisiinsa pariston päällä. Oikosulku tyhjentää pariston ja lämmittää sitä.
- Kun lopetat, irrota moottorin johto paristosta, jotta paristo ei tyhjene.

## Työvaiheet

1. Tarkista, että hammasharjan pään varsi on katkaistu ja reuna on sileä. Jos reuna on terävä, pyydä opettajaa hiomaan se.
2. Leikkaa kaksipuolista teippiä harjan pään selän kokoinen pala ja kiinnitä se.
3. Kiinnitä värinämoottori teipille harjan etupäähän. Jos moottorissa on pyörivä epäkeskopaino näkyvissä, sen täytyy päästä pyörimään vapaasti.
4. Taivuta moottorin johdot niin, että toinen kulkee pariston paikan alle ja toinen jää ylös.
5. Laita nappiparisto teipille moottorin taakse plusnapa ylöspäin niin, että alempi johto jää pariston alle. Pariston alapinta on miinusnapa.
6. Taivuta ylempi johto pariston yläpinnalle eli plusnavalle ja kiinnitä se pienellä teipinpalalla. Moottori alkaa väristä. Värinämoottori pyörii kumpaan suuntaan tahansa, joten johtojen järjestyksellä ei ole väliä.
7. Laske robotti tasaiselle pöydälle. Jos se kaatuu, siirrä paristoa niin, että painopiste on harjan keskellä.
8. Kun lopetat, irrota ylempi johto pariston päältä.

## Kuvat ja esimerkkikoodi

Harjarobotti sivulta. Moottori on edessä ja paristo sen takana. Vinot harjakset ohjaavat liikettä.

<svg data-fig="robotti"></svg>

Tässä työssä ei ohjelmoida. Tunnilla 11 opit ohjaamaan moottoria Arduinolla.

## Testaa ja mittaa

- Toimintaperiaate: moottorin akselissa on epäkeskopaino, jonka massakeskipiste ei ole akselin kohdalla. Kun paino pyörii, se heiluttaa koko robottia ylös ja alas. Joka kerta kun robotti kevenee, vinot harjakset joustavat ja työntävät sitä harjasten kallistuksen suuntaan.
- Merkitse pöytään $50\,\text{cm}$:n matka. Mittaa, kauanko robotilla kestää kulkea matka, ja toista kolme kertaa. Laske nopeus $v = \dfrac{s}{t}$ jokaiselle toistolle ja niiden keskiarvo.
- Haasta itsesi: vertaa kahta harjaa, joiden harjakset ovat eri kulmassa, tai leikkaa toisen harjan harjakset lyhyemmiksi. Mittaa kummankin nopeus kolmella toistolla ja esitä tulokset taulukkona. Miten harjasten kulma vaikuttaa nopeuteen?

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| Moottori ei käynnisty | Johto ei kosketa pariston napaa | Paina johto tiukemmin teipillä. Tarkista, että alempi johto on kuorittu kohdasta, joka on pariston alla. |
| Moottori ei käynnisty | Epäkeskopaino osuu teippiin | Siirrä moottoria niin, että paino pyörii vapaasti. |
| Robotti pyörii ympyrää | Paino on toisella sivulla | Siirrä paristoa tai moottoria keskemmälle. |
| Robotti kaatuu | Painopiste on liian korkealla | Laita paristo mahdollisimman matalalle ja keskelle. |
| Robotti värisee paikallaan | Harjakset ovat suorassa | Kallista harjaksia samaan suuntaan painamalla harjaa pöytää vasten ja vetämällä taaksepäin. |

## Jatkotehtävä

1. Kytkin. Lisää robottiin paperinen kytkin kuten [Valokortissa](ahjo-valokortti.html), jotta virran voi katkaista irrottamatta johtoa.
2. Robottiareena. Rakenna ryhmän kanssa pahvista areena, jossa on esteitä. Kuka saa robotin kulkemaan reitin läpi muuttamalla vain sen rakennetta?
3. Kahden moottorin robotti. Mieti, miten kahden harjan ja kahden moottorin robottia voisi ohjata kääntymään. Luonnostele ratkaisu ennen rakentamista.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valokuva tai lyhyt video robotista liikkeessä
- mittaustulokset taulukkona: matka, aika ja nopeus jokaisesta toistosta sekä keskiarvo
- yksi rakenteen muutos ja mitä siitä seurasi.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ei ole kokeiltu Ahjossa. Rakenna yksi robotti itse ennen tuntia ja tarkista, että valitsemasi värinämoottori käynnistyy CR2032-paristolla.
- Katkaise hammasharjojen varret valmiiksi sivuleikkureilla tai pienellä sahalla ja hio terävät reunat. Opiskelijat eivät tarvitse tässä työssä leikkaavia työkaluja.
- Värinämoottoreita on kahta tyyppiä: litteä nappimoottori ja sylinterimoottori, jonka akselin päässä on näkyvä epäkeskopaino. Molemmat käyvät. Sylinterimallilla liike on usein voimakkaampi.
- Jaa nappiparistot tunnin alussa ja kerää ne pois lopussa. Nielaistu nappiparisto on hengenvaarallinen, joten säilytä ne lukitussa rasiassa.
- Työ sopii Ahjo 1:n tunnille 11 vaihtoehtoiseksi tehtäväksi tai lisähaasteeksi. Se yhdistää työn muotoiluun ja fysiikan lukuun [Tasainen liike – nopeus, paikka ja kuvaajat](fy1-5.html).
- Harjarobotti on yleinen makerspace-aloitustyö. Ohjeen teksti ja kuva on tehty Ruukkilabraan.
