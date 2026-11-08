## Haaste

Saa LED vilkkumaan Arduinolla niin, että tiedät, miksi se vilkkuu. Kytket LEDin ja etuvastuksen koekytkentälevylle, mitoitat vastuksen itse, kirjoitat ohjelman ja mittaat lopuksi, kulkeeko piirissä se virta, jonka laskit. Valmis työ on ensimmäinen palikka monelle Ahjon projektille: sama kytkentä ohjaa myöhemmin merkkivaloja, summereita ja moottorinohjaimia.

Työ kestää noin 75 minuuttia. Jatkotehtävään tarvitset toisen kerran.

## Oppimistavoitteet

Työn jälkeen osaat

- kytkeä LEDin ja etuvastuksen koekytkentälevylle oikein päin ja selittää, miksi levyn pystyrivit yhdistävät komponentit
- laskea etuvastuksen resistanssin Ohmin laista ja valita lähimmän sopivan vakioarvon
- kirjoittaa, tallentaa ja ladata Arduino-ohjelman, jossa on `setup()`, `loop()`, `pinMode()`, `digitalWrite()` ja `delay()`
- mitata virran yleismittarilla ja verrata mittausta laskettuun arvoon
- etsiä vian järjestelmällisesti oire kerrallaan.

## Lähtötaso ja ennakkotaidot

Et tarvitse aiempaa ohjelmointikokemusta. Sinun on hyvä tietää, mitä jännite, virta ja resistanssi tarkoittavat. Kertaa tarvittaessa luvut [Virtapiiri, sähkövirta ja jännite](fy6-1.html) ja [Resistanssi ja Ohmin laki](fy6-3.html). LEDin toiminnasta kerrotaan tarkemmin luvussa [Puolijohteet, diodi, LED ja aurinkokenno](fy6-14.html).

## Laitteet ja materiaalit

Ahjon perussarjoissa käytetään Arduino Uno -levyä. Laitteisto on vasta hankinnassa, joten muiden tarvikkeiden mallit tarkentuvat myöhemmin.

| Tarvike | Määrä |
|---|---|
| Arduino Uno ja USB-kaapeli | 1 |
| Koekytkentälevy (vähintään puolikas) | 1 |
| Punainen LED, halkaisija $5\,\text{mm}$ | 1 |
| Vastus $330\,\Omega$ (värirenkaat oranssi, oranssi, ruskea, kulta) | 1 |
| Kytkentäjohtimia (uros–uros) | 2–4 |
| Yleismittari | 1 |
| Painonappi ja toinen LED (jatkotehtävä) | 1 + 1 |
| Tietokone, jossa on Arduino IDE | 1 |

## Turvallisuus ja perehdytys

Ahjon turvallisuusohjeet ovat vielä valmisteilla. Katso aihe [Juottaminen ja elektroniikkatyöskentely](ahjo-turvallisuus.html#elektroniikka), ja noudata opettajan antamaa perehdytystä.

Tässä työssä käytetään vain USB-väylän $5\,\text{V}$:n jännitettä, joten sähköiskun vaaraa ei ole. Laitteita voi silti rikkoa:

- Tee ja muuta kytkentöjä vain, kun USB-kaapeli on irti.
- Älä koskaan kytke LEDiä ilman etuvastusta. Liian suuri virta polttaa LEDin ja voi vaurioittaa levyn pinniä.
- Älä yhdistä $5\,\text{V}$:n tai $3{,}3\,\text{V}$:n pinniä suoraan GND-pinniin. Se on oikosulku.
- Jos jokin komponentti kuumenee tai haisee, irrota USB-kaapeli heti ja kerro opettajalle.

Verkkovirran turvallisuudesta kerrotaan luvussa [Sähköturvallisuus kotona ja työssä](fy6-15.html).

## Työvaiheet

1. Mitoita etuvastus ennen kytkentää. Arduinon pinni antaa tilassa HIGH jännitteen $U = 5{,}0\,\text{V}$. Punaisen LEDin yli jää noin $U_\text{LED} = 2{,}0\,\text{V}$, ja sopiva virta on $I = 10\,\text{mA}$. Vastuksen yli jää loput jännitteestä, joten
   $$\begin{aligned}&R = \frac{U - U_\text{LED}}{I}\\ &= \frac{5{,}0\,\text{V} - 2{,}0\,\text{V}}{0{,}010\,\text{A}}\\ &= 300\,\Omega.\end{aligned}$$
   Lähin yleinen vakioarvo, joka ei ole tätä pienempi, on $330\,\Omega$. Suurempi resistanssi pienentää virtaa, joten LED on turvassa.
2. Laske, mikä virta $330\,\Omega$:n vastuksella kulkee: $I = \dfrac{3{,}0\,\text{V}}{330\,\Omega} \approx 9{,}1\,\text{mA}$. Kirjoita arvo projektipäiväkirjaasi. Tarkistat sen mittaamalla vaiheessa 9.
3. Tunnista LEDin jalat. Pitkä jalka on anodi ja lyhyt jalka katodi. Katodin puolella LEDin reunassa on usein myös tasainen kohta.
4. Kytke USB-kaapeli irti. Aseta LED koekytkentälevylle niin, että katodi on reiässä a5 ja anodi reiässä a6.
5. Aseta vastus reikien b6 ja b10 väliin. Vastuksella ei ole suuntaa.
6. Vie johdin Arduinon pinnistä 13 reikään e10 ja toinen johdin GND-pinnistä reikään e5. Vertaa kytkentää kuvaan ja kytkentäkaavioon.
7. Avaa Arduino IDE, kirjoita alla oleva ohjelma ja tallenna se. Valitse valikosta oikea levy ja portti, ja lataa ohjelma painikkeella Upload.
8. Kytke USB-kaapeli. LEDin pitäisi palaa sekunnin ja olla sekunnin pimeänä vuorotellen.
9. Mittaa virta. Irrota USB-kaapeli, ota pinnin 13 johdin pois reiästä e10 ja kytke yleismittari sarjaan sen tilalle: mittarin toinen johto pinniin 13 ja toinen reikään e10. Valitse virran mittausalue $\text{mA}$. Kytke USB ja lue arvo, kun LED palaa. Mittaustavasta kerrotaan lisää luvussa [Mittaukset virtapiirissä](fy6-2.html).

## Kuvat ja esimerkkikoodi

Kytkentäkaaviossa näkyy, missä järjestyksessä virta kulkee pinnistä 13 vastuksen ja LEDin kautta maahan.

<svg data-fig="kytkenta"></svg>

Koekytkentälevyllä saman pystyrivin viisi reikää on yhdistetty toisiinsa levyn sisällä. Kuvassa keltaisella merkityt pystyrivit 5, 6 ja 10 kuljettavat virran komponentilta toiselle.

<svg data-fig="koekytkentalevy"></svg>

Esimerkkiohjelma. Kaksi kauttaviivaa aloittaa kommentin, jota Arduino ei suorita.

```cpp
// Vilkkuva LED: pinni 13 -> 330 ohmin vastus -> LED -> GND
const int LED_PIN = 13;        // pinni, johon vastus on kytketty
const int ON_MS = 1000;        // kuinka kauan LED palaa (ms)
const int OFF_MS = 1000;       // kuinka kauan LED on pimeänä (ms)

void setup() {
  pinMode(LED_PIN, OUTPUT);    // pinni toimii lähtönä
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // pinniin 5 V: LED syttyy
  delay(ON_MS);
  digitalWrite(LED_PIN, LOW);  // pinniin 0 V: LED sammuu
  delay(OFF_MS);
}
```

`setup()` suoritetaan kerran, kun levy käynnistyy. `loop()` toistuu niin kauan kuin levyssä on virta.

## Testaa ja mittaa

- Muuta vakioiden `ON_MS` ja `OFF_MS` arvoja. Millä vilkkumistaajuudella et enää erota vilkkumista? Kirjoita havainto ja käyttämäsi arvot muistiin.
- Vertaa mittaamaasi virtaa vaiheessa 2 laskemaasi arvoon $9{,}1\,\text{mA}$. Laske suhteellinen ero. Mieti, mistä ero voi johtua: vastuksen toleranssi on tyypillisesti $\pm 5\,\%$, LEDin jännite ei ole tarkalleen $2{,}0\,\text{V}$, eikä pinnin jännite ole tarkalleen $5{,}0\,\text{V}$.
- Mittaa jännite LEDin ja vastuksen yli erikseen. Onko niiden summa sama kuin pinnin ja GND:n välinen jännite?

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| LED ei syty lainkaan | LED on väärin päin | Käännä LED: pitkä jalka reikään a6. |
| LED ei syty lainkaan | Johdin on väärällä pystyrivillä | Vertaa jokaista reikää kuvaan. |
| Ohjelman lataus ei onnistu | Väärä levy tai portti | Tarkista Tools-valikko. Kokeile toista USB-kaapelia, sillä osa kaapeleista lataa vain virtaa. |
| Portti ei näy lainkaan | Kaapeli tai USB-portti ei toimi | Kokeile toista USB-porttia ja kaapelia. Jos portti ei vieläkään näy, kerro opettajalle. |
| LED palaa koko ajan | Ohjelma ei ole latautunut tai johdin on väärässä pinnissä | Lataa ohjelma uudelleen ja tarkista, että johdin on pinnissä 13. |
| LED palaa himmeästi | Liian suuri vastus | Tarkista värirenkaat: $330\,\Omega$ on oranssi, oranssi, ruskea. |
| Mittari näyttää nollaa | Mittari on rinnan eikä sarjassa, tai sulake on palanut | Kytke mittari virran kulkureitille ja tarkista mittausalue. |

## Jatkotehtävä

1. SOS-merkki. Muuta ohjelmaa niin, että LED vilkuttaa morsemerkin SOS: kolme lyhyttä, kolme pitkää ja kolme lyhyttä välähdystä. Kirjoita lyhyelle ja pitkälle välähdykselle omat aliohjelmat.
2. Painonappi. Kytke painonappi pinnin 2 ja GND:n väliin, ja ota käyttöön levyn sisäinen ylösvetovastus komennolla `pinMode(2, INPUT_PULLUP)`. Nyt `digitalRead(2)` antaa arvon LOW, kun nappi on painettuna. Tee ohjelma, jossa LED syttyy vain napin ollessa painettuna.
3. Kaksi LEDiä. Lisää toinen LED ja vastus pinniin 12 ja tee liikennevalon kaltainen vuorottelu. Laske, kuinka suuri virta Arduinosta otetaan yhteensä.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valokuva valmiista kytkennästä ja oma piirros kytkentäkaaviosta
- vastuksen laskusi ja valitsemasi vakioarvo
- mitattu virta, laskettu virta ja niiden ero
- ohjelmakoodi tai linkki siihen sekä yksi asia, jota muutit, ja mitä siitä seurasi
- yksi vika, joka sinulle tuli vastaan, ja miten löysit sen. Epäonnistuminen on hyvää dokumentoitavaa, kun kerrot, mitä siitä opit.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ei ole vielä kokeiltu Ahjon omilla laitteilla. Levyksi on valittu Arduino Uno. Tarkista ennen ensimmäistä kertaa, että Arduino IDE on asennettu koulun koneisiin ja tunnistaa levyn.
- Varaa yksi levy, kaapeli ja komponenttisarja paria kohti. Laita varalle ylimääräisiä LEDejä ja vastuksia, koska niitä katoaa ja rikkoutuu.
- Tarkista, että yleismittarien virta-alueen sulakkeet ovat ehjät.
- Tavallisin pysähdyskohta on ohjelman lataaminen. Kokeile lataus jokaisella koneella etukäteen.
- Työ sopii Ahjo 1 -opintojakson elektroniikkajaksoon sekä kilparobotiikan alkuun. Fysiikan teoriaan voit viitata luvuissa FY6.1–FY6.3 ja FY6.14.
- Ohjeen rakenne on saanut vaikutteita SparkFunin kokeiluoppaasta (SIK) ja Arduinon omista esimerkeistä. Teksti, kuvat ja koodi on kirjoitettu Ruukkilabraan.
