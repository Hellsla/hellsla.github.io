## Pikastartti

Air:bit 2:ta ohjataan toisella micro:bitillä, joka lähettää komennot radiolla. Ohjaimen ohjelmoit itse MakeCodessa. Dronen oma ohjelma on valmis, ja sitä opetellaan lukemaan.

1. Avaa MakeCode ja tee uusi projekti.
2. Aseta radioryhmäksi ryhmäsi oma numero.
3. Lähetä kallistus, kaasu ja käynnistyslupa radiolla nimettyinä arvoina.
4. Testaa pöydällä toisella micro:bitillä, että arvot tulevat perille.

### Kokeile

Ohjelmoi ohjain, joka lähettää kallistuksen ja kaasun. Näytä vastaanottavalla micro:bitillä, että arvot muuttuvat.

### Muokkaa

Lisää käynnistysvarmistus: A ja B yhtä aikaa vaihtaa käynnistysluvan ja nollaa kaasun. Lisää ravistus, joka pysäyttää moottorit.

### Haasta itsesi

Lue dronen ohjelmasta, miten se jakaa tehon neljälle moottorille, ja selitä, miksi drone kallistuu eteenpäin.

## Haaste

Ohjain ja drone eivät tunne toisiaan: ne vain lähettävät ja kuuntelevat samaa radioryhmää. Jos kaksi ryhmää käyttää samaa numeroa, toisen ohjain ohjaa toisen dronea. Tavoite on ohjain, joka toimii luotettavasti ja jonka tilan näet yhdellä vilkaisulla.

Valmistaja arvioi ohjaimen ohjelmointiin kolmesta neljään tuntia. Jos oma ohjelma ei valmistu, käytössä on valmistajan valmis ohjainohjelma.

## Oppimistavoitteet

Työn jälkeen osaat

- lähettää ja vastaanottaa arvoja micro:bitin radiolla
- ohjelmoida ohjaimen, jossa on kaasu, kallistus, käynnistysvarmistus ja hätäpysäytys
- kertoa, mitä dronen ohjelman pääosat tekevät
- kuvata vakautuksen takaisinkytkentänä.

## Lähtötaso ja ennakkotaidot

MakeCoden lohko-ohjelmointi riittää. Muuttujat ja ehtolause kerrataan tunnilla. Drone pitää olla koottu ohjeen [Air:bit 2:n kokoaminen ja toimintakokeet](ahjo-airbit-kokoaminen.html) mukaan ennen kuin ohjainta kokeillaan sillä.

## Laitteet ja materiaalit

| Tarvike | Määrä |
|---|---|
| micro:bit ohjaimeksi (V1 tai V2) ja paristokotelo | 1 |
| micro:bit vastaanottajaksi pöytätestiin | 1 |
| Tietokone, jossa MakeCode toimii selaimessa | 1 |
| USB-kaapeli | 1 |
| Koottu Air:bit 2 ilman potkureita | 1 |

## Turvallisuus ja perehdytys

Katso aihe [potkurit ja moottorit](ahjo-turvallisuus.html#drone-potkurit). Se on valmisteilla, kunnes koulu on hyväksynyt sen.

- Jokainen uusi tai muutettu ohjelma testataan ensin pöydällä ja sitten dronella **ilman potkureita**.
- Käynnistysvarmistus ja ravistuspysäytys pidetään ohjelmassa aina.
- Dronen ohjelmasta ei muuteta lentoon vaikuttavia arvoja ilman opettajan lupaa. Alkuperäinen ohjelma tallennetaan ennen muutoksia.

## Työvaiheet

Ohjain lähettää viisi arvoa. Valmistajan muistisääntö on PARTY.

| Kirjain | Arvo | Alue | Miten ohjaimella |
|---|---|---|---|
| P | pitch, kallistus eteen ja taakse | $-45$ … $45$ | kallista ohjainta |
| A | arm, käynnistyslupa | 0 tai 1 | A ja B yhtä aikaa |
| R | roll, kallistus sivulle | $-45$ … $45$ | kallista ohjainta |
| T | throttle, kaasu | 0 … 100 | A pienentää, B kasvattaa |
| Y | yaw, kääntö pystyakselin ympäri | $-30$ … $30$ | lisätehtävä |

1. Tee muuttujat käynnistysluvalle, kaasulle ja kallistuksille.
2. Aseta radioryhmä ohjelman alussa ja näytä numero näytöllä.
3. A-nappi pienentää kaasua viidellä ja B-nappi kasvattaa viidellä. Kun kaasu on yli 40, askel on yksi: leijuntaa säädetään tarkasti.
4. A ja B yhtä aikaa vaihtaa käynnistysluvan arvojen 0 ja 1 välillä ja nollaa kaasun.
5. Ravistus asettaa käynnistysluvan ja kaasun nollaan. Tämä on hätäpysäytys.
6. Lue kallistukset micro:bitin asentoanturista ja rajaa ne taulukon alueelle.
7. Lähetä arvot ikuisessa silmukassa nimettyinä arvoina, kullakin oma iso kirjaimensa.
8. Näytä tila näytöllä: käynnistyslupa, kaasun taso ja kallistuksen piste.
9. Testaa pöydällä vastaanottavalla micro:bitillä, sitten dronella ilman potkureita.

## Kuvat ja esimerkkikoodi

Aloitusohjelman saat tunnin 5 sivulta. Tässä on sen ydin. Liitä ohjelma MakeCoden JavaScript-näkymään, niin näet sen myös lohkoina.

```typescript
let radioGroup = 7      // vaihda ryhmäsi omaksi numeroksi
let arm = 0
let throttle = 0

radio.setGroup(radioGroup)

input.onButtonPressed(Button.AB, function () {
    arm = arm == 0 ? 1 : 0
    throttle = 0
})

input.onGesture(Gesture.Shake, function () {
    arm = 0
    throttle = 0
})

basic.forever(function () {
    radio.sendValue("A", arm)
    radio.sendValue("T", throttle)
    radio.sendValue("P", Math.constrain(input.rotation(Rotation.Pitch), -45, 45))
    radio.sendValue("R", Math.constrain(input.rotation(Rotation.Roll), -45, 45))
})
```

### Miten dronen ohjelma toimii

Air:bit 2:ssa vakautus lasketaan micro:bitissä, ja ohjelma on avointa MakeCode-koodia. Sen pääsilmukka toistaa samat vaiheet monta kertaa sekunnissa:

1. **Mittaa.** Ohjelma lukee ohjainkortin gyroskoopin ja kiihtyvyysanturin ja laskee niistä dronen asennon.
2. **Vertaa.** Ohjelma vertaa mitattua asentoa siihen asentoon, jota ohjain pyytää. Ero on virhe.
3. **Korjaa.** Säädin laskee virheestä korjauksen jokaiselle akselille.
4. **Jaa teho.** Ohjelma laskee jokaisen moottorin tehon kaasusta ja korjauksista. Kun drone kallistuu eteenpäin, kaksi takamoottoria saa lisää tehoa ja kaksi etumoottoria vähemmän.
5. **Varmista.** Moottorit käyvät vain, kun käynnistyslupa on annettu ja anturit toimivat.

Tämä on takaisinkytkentä: mittaus vaikuttaa ohjaukseen, ja ohjaus muuttaa sitä, mitä seuraavaksi mitataan.

## Testaa ja mittaa

- Pöytätesti: muuttuvatko vastaanottajan näyttämät arvot, kun kallistat ohjainta ja painat nappeja?
- Kantama: kuinka kaukaa viesti vielä tulee perille luokassa? Mittaa etäisyys.
- Dronetesti ilman potkureita: käynnistyvätkö moottorit vain käynnistysluvalla, ja pysähtyvätkö ne ravistuksesta joka kerta kymmenestä?

## Jos jokin ei toimi

- **Arvot eivät tule perille:** tarkista, että kummassakin micro:bitissä on sama radioryhmä.
- **Naapuriryhmän ohjain vaikuttaa droneesi:** teillä on sama radioryhmä. Vaihda omaanne.
- **Drone reagoi väärään suuntaan:** vaihda kallistusarvon etumerkki ohjaimen ohjelmassa ja testaa uudelleen ilman potkureita.
- **Kaasu hyppii:** tarkista, ettei A-napin ja B-napin käsittelijä laukea myös silloin, kun painat molempia.
- **Oma ohjelma ei valmistu:** lataa valmistajan valmis ohjainohjelma ja jatka omaa ohjelmaa myöhemmin.

## Jatkotehtävä

Valmistajan lisätehtävässä kääntö (Y) tehdään kosketusnapeilla. Suunnittele oma tapa antaa kääntökomento ja testaa se pöydällä. Toinen vaihtoehto: tee micro:bitistä vastaanotin, joka piirtää ohjaimen lähettämät arvot kuvaajaksi MakeCoden datanäkymään.

## Dokumentoi

Liitä projektipäiväkirjaan

- kuvakaappaus ohjainohjelmasta
- ryhmän radioryhmän numero
- pöytätestin ja dronetestin tulokset
- lukukartta dronen ohjelman vaiheista.

## Opettajalle: valmistelu

- Valmiit ohjelmat ovat valmistajan sivulla [Air:bit-dokumentit](https://www.makekit.no/en/docs/airbit-docs/): ohjaimen hex-tiedosto ja dronen ohjelma. Avaa dronen ohjelma MakeCodessa koulun koneella ennen tuntia.
- Jaa jokaiselle ryhmälle oma radioryhmä väliltä 0–255. Valmiin ohjelman oletus on 7.
- Valmistajan ohje ei sisällä säätöarvojen muuttamista. Dronen ohjelman lukeminen ja vakauskokeet ovat koulun omia tehtäviä: kokeile ne itse ja päätä, mitä arvoja opiskelijat saavat muuttaa ja kuinka paljon. Säätöarvoja ei ole kirjattu tähän ohjeeseen, koska ne voivat muuttua ohjelman version mukana.
- Aloitusohjelma on testaamaton luonnos. Kokeile se ilman potkureita ja tarkista kallistuksen suunta.
- Python: valmistaja tarjoaa Air:bit 2:lle Python-version vain ohjaimesta, ei dronen ohjelmasta.
- Tiedot on luettu valmistajan ohjeesta 12.11.2026.
