## Pikastartti

Saat anturin lukemat käyräksi noin kymmenessä minuutissa. Ohjelma on valmiina [aloitusaineistona](ahjo-aloitus/sarjaplotteri.ino), ja sama koodi on alla tässä ohjeessa. Tee kytkennät aina USB-johto irrotettuna.

1. Kytke valovastus ja $10\,\text{k}\Omega$:n vastus sarjaan Arduinon 5V- ja GND-pinnin väliin alla olevan kuvan mukaan.
2. Vie johto valovastuksen ja $10\,\text{k}\Omega$:n vastuksen välistä Arduinon A0-tuloon.
3. Kytke USB-johto, avaa ohjelma Arduino IDE:ssä ja lataa se painikkeella Upload.
4. Avaa Tools → Serial Plotter ja valitse nopeudeksi 9600 baud. Peitä anturi kädelläsi: käyrä laskee.

### Kokeile

Saa anturin lukemat näkymään sarjaplotterissa ja tallenna ne.

### Muokkaa

Tee anturista soitin tai valo, joka reagoi ympäristöön. Esimerkiksi summerin sävel voi nousta, kun valoa on enemmän. Koodi on alla Jatkotehtävä-osassa.

### Haasta itsesi

Muunna lukemat jännitteeksi, kerää mittaussarja ja piirrä kuvaaja yksiköineen.

## Haaste

Teet mittalaitteen, joka piirtää. Valovastus muuttaa resistanssiaan valon mukaan, ja Arduino mittaa sen jännitteenä. Sarjaplotteri näyttää lukemat käyränä heti, kun ympäristö muuttuu. Samalla tavalla luetaan monia muitakin antureita, esimerkiksi lämpö-, kosteus- ja voima-antureita.

Työ kestää yhden 75 minuutin tunnin.

## Oppimistavoitteet

Työn jälkeen osaat

- kytkeä anturin jännitteenjakoon ja analogiatuloon
- lukea anturin arvon komennolla `analogRead()` ja lähettää sen tietokoneelle komennolla `Serial.println()`
- avata sarjaplotterin ja tulkita sen käyrää
- muuntaa lukeman jännitteeksi ja tallentaa mittaussarjan.

## Lähtötaso ja ennakkotaidot

Sinun on hyvä osata ladata ohjelma Arduinolle. Kertaa tarvittaessa [Arduinon ensiaskeleet](ahjo-arduino.html). Jännitteenjaosta ja resistanssista kerrotaan luvussa [Resistanssi ja Ohmin laki](fy6-3.html).

## Laitteet ja materiaalit

Ahjon laitteisto on vasta hankinnassa, joten tarvikkeiden mallit tarkentuvat myöhemmin.

| Tarvike | Määrä |
|---|---|
| Arduino Uno ja USB-kaapeli | 1 |
| Koekytkentälevy ja kytkentäjohtimia | 1 + 4 |
| Valovastus (LDR) | 1 |
| Vastus $10\,\text{k}\Omega$ (ruskea, musta, oranssi, kulta) | 1 |
| Passiivinen summeri tai LED ja $330\,\Omega$:n vastus (Muokkaa) | 1 |
| Tietokone, jossa on Arduino IDE | 1 |

## Turvallisuus ja perehdytys

Ahjon turvallisuusohjeet ovat vielä valmisteilla. Katso aihe [Juottaminen ja elektroniikkatyöskentely](ahjo-turvallisuus.html#elektroniikka), ja noudata opettajan perehdytystä.

- Tee ja muuta kytkentöjä vain, kun USB-johto on irti.
- Älä yhdistä 5V-pinniä suoraan GND-pinniin. Valovastus ja $10\,\text{k}\Omega$:n vastus ovat aina sarjassa näiden välissä.
- Jos jokin kuumenee tai haisee, irrota USB-johto heti ja kerro opettajalle.

## Työvaiheet

1. Irrota USB-johto. Aseta valovastus ja $10\,\text{k}\Omega$:n vastus koekytkentälevylle niin, että niillä on yksi yhteinen pystyrivi. Se on jännitteenjaon keskikohta.
2. Vie johto 5V-pinnistä valovastuksen vapaaseen päähän ja johto GND-pinnistä $10\,\text{k}\Omega$:n vastuksen vapaaseen päähän.
3. Vie johto keskikohdan pystyriviltä A0-tuloon.
4. Kytke USB-johto. Avaa ohjelma, valitse levyksi Arduino Uno ja oikea portti, ja lataa ohjelma.
5. Avaa Tools → Serial Plotter ja valitse 9600 baud. Käyrän pitäisi liikkua, kun peität anturin tai osoitat sitä puhelimen valolla.
6. Tallenna mittaussarja. Avaa Tools → Serial Monitor, peitä anturi välillä ja kopioi lukemat taulukkolaskentaan.

## Kuvat ja esimerkkikoodi

Valovastus ja $10\,\text{k}\Omega$:n vastus muodostavat jännitteenjaon. Mitä enemmän valoa, sitä pienempi on valovastuksen resistanssi ja sitä suurempi on jännite A0-tulossa.

<svg data-fig="kytkenta"></svg>

Esimerkkiohjelma lukee A0-tulon 20 kertaa sekunnissa ja lähettää lukeman tietokoneelle. Teksti `valo:` antaa käyrälle nimen sarjaplotterissa.

```cpp
const int SENSOR_PIN = A0;      // jännitteenjaon keskikohta

void setup() {
  Serial.begin(9600);           // sama nopeus kuin sarjaplotterissa
}

void loop() {
  int value = analogRead(SENSOR_PIN);   // 0...1023 vastaa 0...5 V
  Serial.print("valo:");
  Serial.println(value);
  delay(50);                            // 20 lukemaa sekunnissa
}
```

Lukema on kokonaisluku 0–1023. Sen voi muuntaa jännitteeksi:
$$U = \frac{\text{lukema}}{1023} \cdot 5{,}0\,\text{V}.$$

## Testaa ja mittaa

- Katso lukemaa huoneen valossa, kädellä peitettynä ja puhelimen valossa. Kirjaa kolme lukemaa ja muunna ne jännitteiksi.
- Mittaa A0-tulon jännite myös yleismittarilla. Vastaako se lukemasta laskemaasi jännitettä?
- Haasta itsesi: vertaa lukemia puhelimen valoisuussovelluksen luksilukemiin samassa paikassa ja piirrä kuvaaja. Sovelluksen lukema on vain suuntaa antava.

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| Sarjaplotteri on tyhjä | Väärä nopeus | Valitse plotterista 9600 baud. |
| Sarjaplotteri on tyhjä | Ohjelma ei latautunut | Lataa ohjelma uudelleen ja tarkista levy ja portti. |
| Lukema on koko ajan 0 tai 1023 | A0-johto on väärällä pystyrivillä | Vie A0-johto keskikohtaan, valovastuksen ja vastuksen väliin. |
| Lukema hyppii satunnaisesti | A0-johto on irti | Paina johto kunnolla reikään. |
| Käyrä nousee, kun anturi peitetään | Valovastus ja vastus ovat vaihtaneet paikkaa | Kytkentä toimii silti. Huomaa vain, että suunta on toisin päin. |
| Lataus ei onnistu | Sarjamonitori tai plotteri varaa portin | Sulje ne ja lataa uudelleen. |

## Jatkotehtävä

1. Valosoitin. Kytke passiivinen summeri pinnin 8 ja GND:n väliin ja lisää ohjelman `loop()`-osaan rivi, joka muuttaa lukeman säveleksi:
   ```cpp
   tone(8, map(value, 0, 1023, 200, 2000));   // enemmän valoa, korkeampi sävel
   ```
2. Yövalo. Kytke LED ja $330\,\Omega$:n vastus pinniin 13. Sytytä LED, kun lukema on pienempi kuin valitsemasi raja-arvo. Valitse raja-arvo mittaustesi perusteella.
3. Toinen anturi. Kokeile samaa ohjelmaa toisella anturilla, esimerkiksi potentiometrillä tai lämpöanturilla, jos sellainen on saatavilla.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valokuva kytkennästä ja kuvakaappaus sarjaplotterin käyrästä
- kolme lukemaa eri valaistuksessa ja niitä vastaavat jännitteet
- miten teit anturista soittimen, valon tai muun laitteen
- yksi vika, joka tuli vastaan, ja miten löysit sen.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ja aloitusaineiston ohjelmaa ei ole vielä kokeiltu Ahjon omilla laitteilla. Kokeile ohjelma ennen tuntia opettajan koneella.
- Sarjaplotteri löytyy Arduino IDE:n versioista 1.6.6 alkaen. Arduino IDE 2:ssa sen saa auki myös ikkunan oikean yläkulman painikkeesta.
- Valovastuksen resistanssi vaihtelee mallin mukaan. Jos lukemat jäävät kapealle alueelle, kokeile $10\,\text{k}\Omega$:n tilalla $4{,}7\,\text{k}\Omega$:n tai $47\,\text{k}\Omega$:n vastusta.
- Tunnin 10 Muokkaa-tasolla voi käyttää myös etäisyysanturia, jos sellainen on hankittu. Sille tarvitaan oma ohjelma, jota tässä ohjeessa ei ole.
- Teksti, kuvat ja koodi on kirjoitettu Ruukkilabraan.
