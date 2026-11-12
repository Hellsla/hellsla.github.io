## Pikastartti

Lentokokeiden tulokset käsitellään Pythonilla. Ohjelma lukee mittaukset tiedostosta, laskee jokaiselle sarjalle keskiarvon ja keskihajonnan ja piirtää kuvaajan. Lentämistä ei tarvita: tämän työn voi tehdä aina, kun dronet ovat toisen ryhmän käytössä.

1. Lataa tunnin sivulta ohjelma `lentoanalyysi.py` ja esimerkkiaineisto.
2. Aja ohjelma esimerkkiaineistolla.
3. Kirjoita omat mittauksesi samanlaiseen tiedostoon.
4. Aja ohjelma omalla tiedostollasi ja tulkitse kuvaaja.

### Kokeile

Laske ja piirrä oman ryhmäsi yhden mittaussarjan keskiarvo ja keskihajonta.

### Muokkaa

Vertaa kahta sarjaa samassa kuvaajassa ja kirjoita yksi lause siitä, onko niiden ero suurempi kuin vaihtelu sarjan sisällä.

### Haasta itsesi

Mittaa dronen paikka videolta ja laske Pythonilla sen nopeus eri hetkillä.

## Haaste

Viisi lukua taulukossa ei vielä kerro, kumpi asetus oli parempi. Kuvaaja, jossa näkyvät kaikki mittaukset, keskiarvo ja hajonta, kertoo sen yhdellä silmäyksellä. Tavoite on kuvaaja, jonka toinen ryhmä ymmärtää ilman selitystä.

## Oppimistavoitteet

Työn jälkeen osaat

- tallentaa mittaukset tiedostoon, jonka ohjelma osaa lukea
- laskea keskiarvon ja keskihajonnan Pythonilla
- piirtää kuvaajan, jossa on akselien nimet ja yksiköt
- perustella johtopäätöksen kuvaajalla.

## Lähtötaso ja ennakkotaidot

Pythonia ei tarvitse osata etukäteen: aloitat valmiista ohjelmasta ja muutat sitä. Kuvaajan piirtämisen periaatteet ovat ohjeessa [Mittauspisteiden kuvaaja](tvt-kuvaaja.html) ja nopeuden laskeminen ohjeessa [Nopeuden ja matkan määrittäminen mittausdatasta](tvt-nopeus-datasta.html).

## Laitteet ja materiaalit

| Tarvike | Huomaa |
|---|---|
| Raspberry Pi 5 tai muu tietokone | Tarvitset Pythonin ja kuvaajia varten matplotlib-kirjaston. |
| Näyttö, näppäimistö ja hiiri | Raspberry Pitä varten. |
| Ryhmän mittaukset | Lentopöytäkirjasta. |
| Lentovideo | Vain Haasta itsesi -tehtävään. |

Raspberry Pi on tässä tietokone, jolla käsitellään dataa. Se ei ohjaa dronea, eikä sitä kiinnitetä droneen.

## Turvallisuus ja perehdytys

Tässä työssä ei lennätetä. Katso aihe [kuvaaminen ja yksityisyys](ahjo-turvallisuus.html#drone-yksityisyys). Se on valmisteilla, kunnes koulu on hyväksynyt sen.

- Käsittele videoita vain koulun laitteilla. Älä siirrä niitä omaan puhelimeesi äläkä julkaise niitä.
- Jos videossa näkyy ihmisiä, kerro opettajalle ennen kuin käytät sitä.

## Työvaiheet

1. Avaa pääte ja siirry kansioon, jossa tiedostot ovat.
2. Aja ohjelma esimerkkiaineistolla: `python lentoanalyysi.py lentodata-esimerkki.csv`.
3. Lue tulostus: jokaiselta sarjalta mittausten määrä, keskiarvo, keskihajonta ja vaihteluväli.
4. Avaa esimerkkiaineisto tekstieditorissa ja katso, miten se on kirjoitettu: ensimmäisellä rivillä sarakkeiden nimet, sen jälkeen yksi mittaus rivillä.
5. Tee oma tiedosto samalla rakenteella. Kirjoita kolmannen sarakkeen otsikkoon suure ja yksikkö, esimerkiksi `ajautuminen_cm`.
6. Aja ohjelma omalla tiedostollasi.
7. Katso kuvaajaa: menevätkö sarjojen mittaukset päällekkäin vai ovatko ne selvästi erillään?
8. Kirjoita johtopäätös yhdellä lauseella.

## Kuvat ja esimerkkikoodi

Mittaustiedosto on tekstitiedosto, jossa sarakkeet on erotettu puolipisteellä. Alla olevat luvut ovat keksitty harjoitusaineisto.

```
sarja;toisto;etaisyys_cm
lahto 2 m;1;12,5
lahto 2 m;2;18,0
lahto 4 m;1;21,0
lahto 4 m;2;30,5
```

Ohjelman ydin lukee rivit ja laskee tunnusluvut:

```python
import csv
import statistics

sarjat = {}
with open("lentodata-esimerkki.csv", encoding="utf-8") as f:
    rivit = [r for r in csv.reader(f, delimiter=";") if r and not r[0].startswith("#")]
for sarja, toisto, arvo in rivit[1:]:
    sarjat.setdefault(sarja, []).append(float(arvo.replace(",", ".")))

for nimi, arvot in sarjat.items():
    print(nimi, statistics.mean(arvot), statistics.stdev(arvot))
```

Keskiarvo on $\bar{x} = \dfrac{x_1 + x_2 + \dots + x_n}{n}$. Keskihajonta kertoo, kuinka kaukana mittaukset tyypillisesti ovat keskiarvosta.

Nopeus videolta lasketaan kahden peräkkäisen paikan avulla: $v = \dfrac{\Delta x}{\Delta t}$, missä $\Delta x$ on paikan muutos ja $\Delta t$ kuvien välinen aika.

## Testaa ja mittaa

- Laske yhden sarjan keskiarvo laskimella ja vertaa ohjelman tulokseen.
- Lisää tiedostoon yksi selvästi poikkeava mittaus. Miten keskiarvo ja keskihajonta muuttuvat?
- Näytä kuvaaja toiselle ryhmälle ilman selitystä. Päättelevätkö he saman kuin sinä?

## Jos jokin ei toimi

- **Ohjelma ei löydä tiedostoa:** tarkista, että olet samassa kansiossa ja että tiedoston nimi on kirjoitettu oikein.
- **Virhe luvun muuntamisessa:** jollakin rivillä on tekstiä luvun paikalla tai sarakkeita on väärä määrä.
- **Kuvaajaa ei piirretä:** matplotlib-kirjasto puuttuu. Pyydä opettajaa asentamaan se. Tunnusluvut tulostuvat silti.
- **Keskihajontaa ei voi laskea:** sarjassa on vain yksi mittaus. Tarvitset vähintään kaksi.

## Jatkotehtävä

Muuta ohjelmaa niin, että se piirtää mittaukset järjestyksessä toiston mukaan. Näkyykö kuvaajassa oppimista: paranevatko tulokset sarjan loppua kohti?

## Dokumentoi

Liitä projektipäiväkirjaan

- kuvaaja, jossa on akselien nimet ja yksiköt
- tunnusluvut taulukkona
- johtopäätös yhdellä lauseella
- mitä mittaisit toisin seuraavalla kerralla.

## Opettajalle: valmistelu

- Asenna Python ja matplotlib ja aja aloitusohjelma esimerkkiaineistolla ennen tuntia. Ohjelma on kokeiltu esimerkkiaineistolla ilman kuvaajakirjastoa; kuvaajan piirto kannattaa kokeilla koulun koneella.
- Raspberry Pi 5 tarvitsee virtalähteen, muistikortin, näytön, näppäimistön ja hiiren. Jos niitä ei ole, työn voi tehdä millä tahansa koneella, jossa on Python.
- Konenäköprojekti tarvitsee kameran, joka on erillinen hankinta.
- Kokoa ryhmien mittaustiedostot yhteiseen kansioon, jotta ryhmät voivat verrata tuloksia.
- Videoanalyysiin sopii video, jossa kamera pysyy paikallaan, drone liikkuu kuvan tasossa ja kuvassa näkyy mittakaava.
