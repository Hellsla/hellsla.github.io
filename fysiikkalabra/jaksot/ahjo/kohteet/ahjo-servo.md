## Pikastartti

Saat servon kääntymään potentiometrillä noin kymmenessä minuutissa. Arduino IDE:ssä on valmis esimerkkiohjelma File → Examples → Servo → Knob, ja alla on sama asia lyhyempänä ohjelmana. Tee kytkennät aina USB-johto irrotettuna.

1. Kytke potentiometrin reunimmaiset jalat Arduinon 5V- ja GND-pinniin ja keskimmäinen jalka A0-tuloon alla olevan kuvan mukaan.
2. Kytke servon punainen johto 5V:iin, ruskea tai musta johto GND:hen ja oranssi tai keltainen johto pinniin 9.
3. Kytke USB-johto, avaa ohjelma ja lataa se painikkeella Upload.
4. Käännä potentiometriä. Servon varsi kääntyy samaan tahtiin.

### Kokeile

Saa servo kääntymään potentiometrillä.

### Muokkaa

Rajaa servon liike omaan tarpeeseesi, esimerkiksi välille 30–150 astetta, tai tee servosta osoitin, jonka taustalle piirrät oman asteikon.

### Haasta itsesi

Liitä servo omaan rakennelmaasi, esimerkiksi portiksi, viuhkaksi tai liikkuvaksi hahmoksi, ja testaa, kestääkö kiinnitys sata edestakaista liikettä.

## Haaste

Saat ensimmäisen liikkeen aikaan ohjelmalla. Potentiometri on säädettävä vastus, jonka asennon Arduino lukee jännitteenä. Ohjelma muuttaa lukeman kulmaksi, ja servo kääntyy siihen kulmaan. Samalla periaatteella liikkuvat monet robotin osat, esimerkiksi tarttujat ja ohjattavat pyörät.

Työ kestää yhden 75 minuutin tunnin.

## Oppimistavoitteet

Työn jälkeen osaat

- kytkeä potentiometrin jännitteenjaoksi ja servon Arduinoon
- muuttaa lukeman kulmaksi komennolla `map()` ja kääntää servoa komennolla `write()`
- rajata servon liikkeen ohjelmassa
- kiinnittää servon rakennelmaan niin, että varsi ei joudu väkisin vääntymään.

## Lähtötaso ja ennakkotaidot

Sinun on hyvä osata ladata ohjelma Arduinolle. Kertaa tarvittaessa [Arduinon ensiaskeleet](ahjo-arduino.html). Analogisen lukeman lukemista harjoitellaan ohjeessa [Valoanturi ja sarjaplotteri](ahjo-sarjaplotteri.html).

## Laitteet ja materiaalit

Ahjon laitteisto on vasta hankinnassa, joten tarvikkeiden mallit tarkentuvat myöhemmin.

| Tarvike | Määrä |
|---|---|
| Arduino Uno ja USB-kaapeli | 1 |
| Koekytkentälevy ja kytkentäjohtimia | 1 + 6 |
| Potentiometri, esimerkiksi $10\,\text{k}\Omega$ | 1 |
| Pieni harrasteservo, esimerkiksi SG90-kokoluokka | 1 |
| Servon varsi ja ruuvi (servon mukana) | 1 |
| Pahvia, teippiä tai kuumaliimaa rakennelmaan (Haasta itsesi) | tarpeen mukaan |
| Tietokone, jossa on Arduino IDE | 1 |

## Turvallisuus ja perehdytys

Ahjon turvallisuusohjeet ovat vielä valmisteilla. Katso aihe [Juottaminen ja elektroniikkatyöskentely](ahjo-turvallisuus.html#elektroniikka), ja noudata opettajan perehdytystä. Kuumaliimapistoolia käytetään vain opettajan luvalla.

- Tee ja muuta kytkentöjä vain, kun USB-johto on irti.
- Pidä sormet poissa servon varren tieltä, kun ohjelma on käynnissä.
- Älä käännä servon vartta käsin väkisin. Servon sisällä olevat hammasrattaat voivat rikkoutua.
- Pieni servo toimii USB-johdon 5 V:n jännitteellä. Isompi servo tai useampi servo tarvitsee oman virtalähteen. Kysy opettajalta, ja muista silloin yhdistää virtalähteen ja Arduinon GND-pinnit.
- Jos servo surisee pitkään paikallaan, kuumenee tai haisee, irrota USB-johto heti ja kerro opettajalle.

## Työvaiheet

1. Irrota USB-johto. Aseta potentiometri koekytkentälevylle niin, että sen kolme jalkaa ovat eri pystyriveillä.
2. Vie johto 5V-pinnistä potentiometrin toiseen reunajalkaan ja johto GND-pinnistä toiseen reunajalkaan.
3. Vie johto potentiometrin keskimmäisestä jalasta A0-tuloon.
4. Kytke servon punainen johto samaan 5V-riviin, ruskea tai musta johto GND-riviin ja oranssi tai keltainen johto pinniin 9.
5. Kiinnitä servon varsi, mutta älä vielä ruuvaa sitä rakennelmaan. Liike pitää ensin nähdä vapaana.
6. Kytke USB-johto, valitse levyksi Arduino Uno ja oikea portti, ja lataa ohjelma.
7. Käännä potentiometri ääriasennosta toiseen. Katso, mihin kulmiin varsi pysähtyy, ja kirjaa ne.

## Kuvat ja esimerkkikoodi

Potentiometri on jännitteenjako, jonka keskikohtaa liukuri siirtää. Servossa on kolme johtoa: kaksi virtaa varten ja yksi ohjausta varten.

<svg data-fig="kytkenta"></svg>

Ohjelma lukee potentiometrin, muuttaa lukeman 0–1023 kulmaksi 0–180 astetta ja kääntää servon siihen.

```cpp
#include <Servo.h>

const int POT_PIN = A0;     // potentiometrin keskimmäinen jalka
const int SERVO_PIN = 9;    // servon ohjausjohto

Servo servo;

void setup() {
  servo.attach(SERVO_PIN);
}

void loop() {
  int value = analogRead(POT_PIN);          // 0...1023
  int angle = map(value, 0, 1023, 0, 180);  // 0...180 astetta
  servo.write(angle);
  delay(15);                                 // servo ehtii kääntyä
}
```

Muokkaa-tasolla liikettä rajataan vaihtamalla rivin `map()` kaksi viimeistä lukua, esimerkiksi `map(value, 0, 1023, 30, 150)`.

## Testaa ja mittaa

- Kirjaa, mihin kulmiin varsi pysähtyy potentiometrin ääriasennoissa. Vastaavatko ne ohjelman lukuja 0 ja 180?
- Kun servo on kiinni rakennelmassa, käännä potentiometriä hitaasti ja katso, mistä kohdasta liike alkaa takkuilla. Rajaa liike ohjelmassa sen sisäpuolelle.
- Haasta itsesi: kirjoita ohjelma, joka liikuttaa servoa edestakaisin sata kertaa, ja tarkista sen jälkeen kiinnitys. Pitikö se? Mikä löystyi?

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| Servo ei liiku lainkaan | Ohjausjohto on väärässä pinnissä | Vie oranssi tai keltainen johto pinniin 9. |
| Servo ei liiku lainkaan | Ohjelma ei latautunut | Lataa ohjelma uudelleen ja tarkista levy ja portti. |
| Servo nykii tai Arduino käynnistyy uudelleen | Servo ottaa liikaa virtaa USB-johdosta | Kokeile pienempää servoa tai kysy opettajalta erillistä virtalähdettä. |
| Servo kääntyy vain vähän | Potentiometrin johto on irti tai väärässä jalassa | Tarkista, että keskimmäinen jalka menee A0-tuloon. |
| Varsi surisee ääriasennossa | Rakennelma estää liikkeen | Rajaa liike ohjelmassa rivillä `map()`. |
| Liike on väärään suuntaan | Potentiometrin reunajalat ovat toisin päin | Vaihda 5V- ja GND-johdot keskenään tai vaihda lukujen 0 ja 180 paikat. |

## Jatkotehtävä

1. Osoitinmittari. Yhdistä tämä ohje ja [valoanturi](ahjo-sarjaplotteri.html): servon varsi näyttää valon määrää omalla asteikollasi.
2. Kaksi asentoa. Korvaa potentiometri painonapilla. Kun nappia painetaan, servo kääntyy toiseen asentoon.
3. Liikkuva hahmo. Tee pahvista hahmo tai mekanismi, jota servo liikuttaa, ja esittele se muille ryhmille.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valokuva tai lyhyt video kytkennästä ja liikkeestä
- servon ääriasennot ja miten rajasit liikettä
- miten kiinnitit servon ja kestikö kiinnitys
- yksi vika, joka tuli vastaan, ja miten löysit sen.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ja ohjelmaa ei ole vielä kokeiltu Ahjon omilla laitteilla. Kokeile kytkentä ennen tuntia samalla servomallilla, jota oppilaat käyttävät.
- Servo-kirjasto tulee Arduino IDE:n mukana. Esimerkkiohjelma Knob löytyy valikosta File → Examples → Servo.
- Pieni harrasteservo toimii yleensä USB-johdon jännitteellä, mutta virrankulutus vaihtelee mallin mukaan. Jos Arduino käynnistyy uudelleen, käytä servolle omaa virtalähdettä ja yhteistä GND-pinniä.
- Kuumaliiman käytöstä päätetään Ahjon turvallisuusohjeissa, jotka ovat vielä valmisteilla.
- Teksti, kuvat ja koodi on kirjoitettu Ruukkilabraan.
