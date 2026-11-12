## Pikastartti

Saat LEDin syttymään noin viidessä minuutissa ilman ohjelmaa. Arduino toimii tässä vain virtalähteenä: sen 5V-pinnissä on jännite aina, kun USB-johto on kytketty. Tee kytkennät aina USB-johto irrotettuna.

1. Laita LED ja $330\,\Omega$:n vastus koekytkentälevylle alla olevan kuvan mukaan. LEDin pitkä jalka tulee vastuksen puolelle.
2. Vedä johto Arduinon 5V-pinnistä vastuksen vapaaseen päähän ja toinen johto GND-pinnistä LEDin lyhyen jalan pystyriville.
3. Kytke USB-johto tietokoneeseen tai USB-laturiin. LED syttyy heti.

### Kokeile

Rakenna piiri kuvan mukaan ja saa LED syttymään.

### Muokkaa

Lisää toinen LED ensin sarjaan ja sitten rinnan. Rinnankytkennässä jokainen LED saa oman $330\,\Omega$:n vastuksen. Vertaa, kummassa kytkennässä LEDit loistavat kirkkaammin.

### Haasta itsesi

Mitoita etuvastus Ohmin lailla ja mittaa piirin virta yleismittarilla. Vertaa mitattua virtaa laskemaasi.

## Haaste

Rakennat ensimmäisen oman virtapiirin: LED, etuvastus ja jännitelähde. Kun piiri toimii, lisäät toisen LEDin ensin sarjaan ja sitten rinnan ja selvität, miksi LEDit loistavat eri kirkkaudella. Sama piiri on myöhemmin monen Ahjo-projektin merkkivalo, ja tunnilla 9 ohjaat sitä ohjelmalla.

Työ kestää yhden 75 minuutin tunnin.

## Oppimistavoitteet

Työn jälkeen osaat

- kytkeä LEDin ja etuvastuksen koekytkentälevylle oikein päin
- selittää, miksi LED tarvitsee etuvastuksen
- tunnistaa sarjaan- ja rinnankytkennän ja selittää, miksi rinnankytkennän jokainen LED tarvitsee oman vastuksen
- laskea etuvastuksen Ohmin laista ja mitata virran yleismittarilla.

## Lähtötaso ja ennakkotaidot

Et tarvitse aiempaa elektroniikkakokemusta. Jännitteestä, virrasta ja resistanssista kerrotaan luvuissa [Virtapiiri, sähkövirta ja jännite](fy6-1.html) ja [Resistanssi ja Ohmin laki](fy6-3.html).

## Laitteet ja materiaalit

Ahjon laitteisto on vasta hankinnassa, joten tarvikkeiden mallit tarkentuvat myöhemmin.

| Tarvike | Määrä |
|---|---|
| Arduino Uno ja USB-kaapeli | 1 |
| Koekytkentälevy | 1 |
| Punainen LED, halkaisija $5\,\text{mm}$ | 2 |
| Vastus $330\,\Omega$ (oranssi, oranssi, ruskea, kulta) | 2 |
| Kytkentäjohtimia (uros–uros) | 4–6 |
| Yleismittari (Haasta itsesi) | 1 |

## Turvallisuus ja perehdytys

Ahjon turvallisuusohjeet ovat vielä valmisteilla. Katso aihe [Juottaminen ja elektroniikkatyöskentely](ahjo-turvallisuus.html#elektroniikka), ja noudata opettajan perehdytystä.

Piirissä on vain USB-väylän $5\,\text{V}$:n jännite, joten sähköiskun vaaraa ei ole. Komponentteja voi silti rikkoa:

- Tee ja muuta kytkentöjä vain, kun USB-johto on irti.
- Älä kytke LEDiä ilman etuvastusta. Liian suuri virta polttaa LEDin.
- Älä yhdistä 5V-pinniä suoraan GND-pinniin. Se on oikosulku.
- Jos jokin kuumenee tai haisee, irrota USB-johto heti ja kerro opettajalle.

## Työvaiheet

1. Tunnista LEDin jalat. Pitkä jalka on anodi ja lyhyt jalka katodi. Katodin puolella LEDin reunassa on usein tasainen kohta.
2. Irrota USB-johto. Aseta LED koekytkentälevylle niin, että jalat ovat eri pystyriveillä.
3. Aseta vastus niin, että sen toinen pää on samalla pystyrivillä kuin LEDin pitkä jalka. Vastuksella ei ole suuntaa.
4. Vie johto Arduinon 5V-pinnistä vastuksen toiseen päähän ja johto GND-pinnistä LEDin lyhyen jalan pystyriville.
5. Tarkista kytkentä kuvasta ja kytke USB-johto. LED syttyy.
6. Sarjaankytkentä. Irrota USB-johto. Lisää toinen LED ensimmäisen perään niin, että virta kulkee molempien kautta peräkkäin. Vastuksia on edelleen yksi. Kytke USB-johto ja katso kirkkautta.
7. Rinnankytkentä. Irrota USB-johto. Rakenna toinen haara: oma $330\,\Omega$:n vastus ja oma LED 5V-johdon ja GND-johdon väliin. Kytke USB-johto ja vertaa kirkkautta sarjaankytkentään.

## Kuvat ja esimerkkikoodi

Ensimmäisessä kaaviossa virta kulkee 5V-pinnistä vastuksen ja LEDin kautta maahan. Ohjelmaa ei tarvita.

<svg data-fig="kytkenta"></svg>

Sarjaankytkennässä virralla on yksi reitti. Rinnankytkennässä kummallakin LEDillä on oma haara ja oma vastus.

<svg data-fig="sarja-rinnan"></svg>

Miksi rinnan kytketyt LEDit tarvitsevat omat vastukset? Kahden LEDin jännite ei ole koskaan täsmälleen sama. Jos haarat jakaisivat yhden vastuksen, suurin osa virrasta kulkisi sen LEDin kautta, jonka jännite on pienempi. Se LED palaisi kirkkaasti ja toinen himmeästi, ja pahimmillaan ensimmäinen LED vaurioituisi.

## Testaa ja mittaa

- Laske yhden LEDin virta. Punaisen LEDin yli jää noin $2{,}0\,\text{V}$, joten vastuksen yli jää $3{,}0\,\text{V}$:
  $$I = \frac{3{,}0\,\text{V}}{330\,\Omega} \approx 9{,}1\,\text{mA}.$$
- Sarjaan kytkettyjen LEDien yli jää yhteensä noin $4{,}0\,\text{V}$, joten vastuksen yli jää vain noin $1{,}0\,\text{V}$ ja virta on noin $3\,\text{mA}$. Siksi sarjaan kytketyt LEDit ovat himmeämpiä.
- Rinnankytkennässä kummassakin haarassa kulkee noin $9\,\text{mA}$, ja Arduinosta otetaan yhteensä noin $18\,\text{mA}$.
- Haasta itsesi: mittaa virta kytkemällä yleismittari sarjaan 5V-johdon tilalle. Valitse virran mittausalue $\text{mA}$. Mittaustavasta kerrotaan luvussa [Mittaukset virtapiirissä](fy6-2.html).

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| LED ei syty | LED on väärin päin | Käännä LED: pitkä jalka vastuksen puolelle. |
| LED ei syty | Johto on väärällä pystyrivillä | Vertaa jokaista kytkentää kuvaan. |
| Sarjaan kytketyt LEDit eivät syty | LEDien jännite on liian suuri | Käytä punaisia LEDejä. Sininen ja valkoinen LED tarvitsevat noin $3\,\text{V}$, eivätkä kaksi niistä syty sarjassa $5\,\text{V}$:n jännitteellä. |
| Rinnan kytketyistä LEDeistä vain toinen palaa | Haaroilla on yhteinen vastus tai toinen LED on väärin päin | Anna kummallekin haaralle oma vastus ja tarkista LEDien suunta. |
| Arduinon valo ei pala | USB-johto ei anna virtaa | Kokeile toista johtoa tai USB-porttia. |

## Jatkotehtävä

1. Kokeile, miten vastuksen koko vaikuttaa kirkkauteen. Vaihda $330\,\Omega$:n vastuksen tilalle $1\,\text{k}\Omega$:n vastus ja vertaa.
2. Lisää piiriin painonappi LEDin ja vastuksen väliin. Nyt LED palaa vain, kun nappia painetaan.
3. Siirrä 5V-johto pinniin 13 ja jatka tunnilla 9 [Arduinon ensiaskeleet](ahjo-arduino.html) -ohjeella. Silloin ohjelma päättää, milloin LED palaa.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valokuva kytkennästä ja oma piirros kytkentäkaaviosta
- havainto: kummassa kytkennässä LEDit olivat kirkkaampia, ja miksi
- Haasta itsesi: laskemasi ja mittaamasi virta sekä niiden ero
- yksi vika, joka tuli vastaan, ja miten löysit sen.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ei ole vielä kokeiltu Ahjon omilla laitteilla. Levyksi on valittu Arduino Uno.
- Arduino toimii tässä vain $5\,\text{V}$:n virtalähteenä. Sen tilalla voi käyttää myös USB-laturiin kytkettyä virtalähdemoduulia tai 3 × AA -paristokoteloa.
- Varaa punaisia LEDejä, sillä sarjaankytkentä ei toimi sinisillä tai valkoisilla LEDeillä $5\,\text{V}$:n jännitteellä.
- Laita varalle ylimääräisiä LEDejä ja vastuksia. Tarkista, että yleismittarien virta-alueen sulakkeet ovat ehjät.
- Teksti, kuvat ja laskut on kirjoitettu Ruukkilabraan.
