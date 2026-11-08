## Pikastartti

Teet kortin, jonka kuva syttyy, kun painat kulmaa. Ensimmäinen valo syttyy noin kymmenessä minuutissa, ja tarvitset vain kartonkia, kuparinauhaa, nappipariston ja LEDin. Laitteita ei käytetä, joten laiteperehdytystä ei tarvita.

1. Taita kartonki kahtia. Piirrä lyijykynällä avatun kortin sisäpuolelle kaksi rataa alla olevan kuvan mukaan.
2. Liimaa kuparinauha radoille. Laita nappiparisto miinusradan päähän plusnapa ylöspäin ja taita kortin kulma sen päälle.
3. Taivuta LEDin jalat sivuille ja teippaa ne radoille niin, että pitkä jalka on plusradalla ja lyhyt miinusradalla.
4. Paina kulmaa. LED syttyy.

### Kokeile

Saa LED syttymään, kun painat kortin kulmaa.

### Muokkaa

Piirrä tai leikkaa kortin kanteen kuva, jonka läpi valo näkyy: tähti, ikkuna, majakka tai oma hahmo.

### Haasta itsesi

Lisää toinen LED rinnan ensimmäisen kanssa ja vertaa kirkkautta. Selitys on alla Opi lisää -osassa.

## Haaste

Tee kortti, jossa valo on osa kuvaa. Rakennat paperille virtapiirin, jossa kuparinauha on johdin, nappiparisto jännitelähde ja kortin taitettu kulma kytkin. Kun ymmärrät paperipiirin, ymmärrät jokaisen virtapiirin perusajatuksen: virta kulkee vain suljetussa piirissä.

Työ kestää noin 30 minuuttia. Kuvitukseen voit käyttää niin paljon aikaa kuin haluat.

## Oppimistavoitteet

Työn jälkeen osaat

- rakentaa suljetun virtapiirin, jossa on jännitelähde, kytkin ja LED
- kytkeä LEDin oikein päin ja selittää, miksi se syttyy vain yhteen suuntaan
- tehdä kytkimen paperista ja kuparinauhasta
- kytkeä kaksi LEDiä rinnan ja selittää havaintosi.

## Lähtötaso ja ennakkotaidot

Et tarvitse aiempaa kokemusta. Jos haluat tietää enemmän virtapiiristä, lue luku [Virtapiiri, sähkövirta ja jännite](fy6-1.html). LEDin toiminnasta kerrotaan luvussa [Puolijohteet, diodi, LED ja aurinkokenno](fy6-14.html).

## Laitteet ja materiaalit

| Tarvike | Määrä |
|---|---|
| Kartonki, A5 tai A4 taitettuna | 1 |
| Kuparinauha, jossa on johtava liima, leveys noin $5\,\text{mm}$ | noin $40\,\text{cm}$ |
| Nappiparisto CR2032 ($3\,\text{V}$) | 1 |
| LED, punainen tai keltainen, halkaisija $3\,\text{mm}$ tai $5\,\text{mm}$ | 1–2 |
| Teippi, sakset, lyijykynä ja värit | 1 sarja |

Punainen ja keltainen LED syttyvät nappipariston $3\,\text{V}$:n jännitteellä varmimmin. Valkoinen ja sininen LED tarvitsevat lähes koko pariston jännitteen, joten ne voivat jäädä himmeiksi.

## Turvallisuus ja perehdytys

Työ ei vaadi laiteperehdytystä. Noudata kuitenkin näitä varotoimia:

- Nappiparisto on vaarallinen, jos sen nielaisee. Pidä paristot rasiassa ja palauta ne opettajalle tunnin lopussa.
- Älä yhdistä pariston napoja kuparinauhalla suoraan toisiinsa. Oikosulku tyhjentää pariston ja lämmittää sitä.
- Käytä tässä työssä vain nappiparistoa. Isompi paristo antaa niin suuren virran, että LED tarvitsee etuvastuksen.

## Työvaiheet

1. Taita kartonki kahtia niin, että saat kortin. Avaa se ja käännä sisäpuoli ylöspäin.
2. Piirrä lyijykynällä kaksi rataa kuvan mukaan. Miinusrata kulkee kortin alakulmasta, pariston paikalta, kuvan kohdalle. Plusrata kulkee kuvan kohdalta taitettavaan kulmaan niin, että kulman taittuessa sen pää osuu pariston päälle.
3. Leikkaa kuparinauhasta palat ja liimaa ne radoille. Jos rata kääntyy, älä leikkaa nauhaa vaan taita se kulman kohdalla. Taitettu kohta johtaa paremmin kuin kaksi päällekkäistä palaa.
4. Laita nappiparisto miinusradan alkuun plusnapa ylöspäin. Plusnapa on pariston leveä puoli, jossa on merkki $+$, ja pariston reuna kuuluu myös plusnapaan. Pariston alapinta on miinusnapa, ja se koskettaa miinusrataa. Kiinnitä paristo teipillä niin, että teippi ei peitä pariston yläpintaa.
5. Taita kortin kulma pariston päälle. Kulmassa olevan plusradan pään pitää osua pariston yläpintaan, eikä se saa koskettaa miinusrataa. Tämä on kytkin.
6. Taivuta LEDin jalat sivuille. Pitkä jalka on anodi ja menee plusradalle, lyhyt jalka on katodi ja menee miinusradalle. Teippaa jalat tiukasti kuparinauhaa vasten.
7. Paina kulmaa. LEDin pitäisi syttyä. Jos ei syty, katso alta kohta Jos jokin ei toimi.
8. Piirrä tai leikkaa kortin kanteen kuva niin, että LED on sen kohdalla.

## Kuvat ja esimerkkikoodi

Avattu kortti sisältä. Kuparinauhat ovat oranssit, ja taitettava kulma on merkitty katkoviivalla.

<svg data-fig="kortti"></svg>

Tässä työssä ei ohjelmoida. Saman piirin voi myöhemmin liittää Arduinoon, jolloin valo voi vilkkua.

## Testaa ja mittaa

- Toimintaperiaate: kun painat kulmaa, plusrata koskettaa pariston plusnapaa ja piiri sulkeutuu. Virta kulkee pariston plusnavalta plusradaa pitkin LEDin anodille, LEDin läpi ja katodilta miinusradaa pitkin takaisin pariston miinusnavalle. Kun päästät irti, piiri aukeaa ja valo sammuu.
- LED päästää virran läpi vain yhteen suuntaan, anodilta katodille. Siksi väärin päin oleva LED ei syty.
- Nappiparistolla on sisäinen resistanssi, tyypillisesti noin $10\text{–}20\,\Omega$. Se rajoittaa virtaa, joten tässä työssä ei tarvita erillistä etuvastusta.
- Haasta itsesi: kytke toinen LED rinnan, eli sen pitkä jalka plusradalle ja lyhyt miinusradalle. Vertaa kirkkautta yhden LEDin korttiin. Koska pariston sisäinen resistanssi rajoittaa kokonaisvirtaa, se jakautuu kahdelle LEDille, ja kumpikin on yleensä hieman himmeämpi. Jos LEDit ovat eriväriset, pienemmän kynnysjännitteen LED (punainen) voi viedä lähes koko virran.

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| LED ei syty | LED on väärin päin | Käännä LED: pitkä jalka plusradalle. |
| LED ei syty | Jalka ei kosketa nauhaa | Teippaa jalka tiukemmin tai paina sitä kynsellä. |
| LED ei syty | Radat ovat yhdessä jatkettuja paloja | Paina jatkoskohta tiukasti tai lisää jatkoksen päälle teippiä. Varmin on yhtenäinen, taitettu nauha. |
| LED palaa koko ajan | Plusrata koskettaa paristoa ilman painallusta | Lisää kulman alle pala kartonkia välikkeeksi niin, että kosketus syntyy vasta painettaessa. |
| LED on himmeä | Valkoinen tai sininen LED, tai paristo on vanha | Vaihda punaiseen tai keltaiseen LEDiin tai uuteen paristoon. |
| Paristo lämpenee | Oikosulku: radat koskettavat toisiaan, tai miinusrata koskettaa pariston reunaa | Irrota paristo heti ja etsi kohta, jossa radat koskettavat. Pariston reuna on plusnapa, joten miinusrata ei saa ulottua pariston ohi. |

## Jatkotehtävä

1. Kaksi kytkintä. Tee kortti, jossa valo syttyy vain, kun painat kahta kulmaa yhtä aikaa. Piirrä ensin kytkentäkaavio. Kytkimet ovat sarjassa.
2. Kirkkauden vertailu. Tee kaksi samanlaista korttia, toiseen yksi ja toiseen kaksi rinnankytkettyä LEDiä. Kuvaa ne puhelimella samoissa oloissa ja vertaa kuvia.
3. Arduino-kortti. Liitä kortin LED Arduinon pinniin $330\,\Omega$:n vastuksen kautta, kuten [Arduinon ensiaskeleissa](ahjo-arduino.html), ja tee siitä vilkkuva.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valokuva valmiista kortista avattuna ja suljettuna
- oma kytkentäkaavio: paristo, kytkin ja LED
- yksi asia, joka ei aluksi toiminut, ja miten korjasit sen
- jos teit haasteen, havaintosi yhden ja kahden LEDin kirkkaudesta.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ei ole kokeiltu Ahjossa. Kokeile yksi kortti itse ennen tuntia valitsemillasi LEDeillä ja kuparinauhalla.
- Hanki kuparinauhaa, jossa on johtava liima. Tavallisessa kuparinauhassa liima ei johda, jolloin jatkoskohdat eivät toimi.
- Varaa punaisia ja keltaisia LEDejä. Ne toimivat CR2032-paristolla varmimmin.
- Jaa nappiparistot tunnin alussa ja kerää ne pois lopussa. Nielaistu nappiparisto on hengenvaarallinen, joten säilytä ne lukitussa rasiassa.
- Työ sopii Ahjo 1:n ensimmäiselle tunnille vaihtoehtoiseksi tehtäväksi tai lisähaasteeksi. Se yhdistää työn kuvataiteeseen ja fysiikan lukuun [Virtapiiri, sähkövirta ja jännite](fy6-1.html).
- Paperipiirit ovat yleinen makerspace-tekniikka. Ohjeen teksti ja kuva on tehty Ruukkilabraan.
