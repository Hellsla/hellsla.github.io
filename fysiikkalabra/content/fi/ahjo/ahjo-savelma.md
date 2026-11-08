## Pikastartti

Saat Arduinon soittamaan sävelmän noin kymmenessä minuutissa, eikä sinun tarvitse kirjoittaa koodia itse. Opettaja on asentanut Arduino IDE:n ja tallentanut valmiin ohjelman. Tee kytkennät aina USB-johto irrotettuna.

1. Kytke pietsosummerin plusjalka tai punainen johto Arduinon pinniin 8 ja toinen jalka GND-pinniin.
2. Kytke USB-johto ja avaa opettajan valmis ohjelma tai kopioi alla oleva esimerkkikoodi.
3. Valitse levyksi Arduino Uno ja oikea portti, ja paina Upload.
4. Summeri soittaa Ukko Nooan alun.

### Kokeile

Saa summeri soittamaan valmiilla ohjelmalla.

### Muokkaa

Vaihda sävelet ja niiden kestot ja tee oma melodia, tunnari tai hälytysääni. Muuta tempoa.

### Haasta itsesi

Laske duuriasteikon taajuudet kaavalla ja soita asteikko. Ohje on alla Opi lisää -osassa.

## Haaste

Ohjelmoi Arduino soittamaan oma sävelmä. Pietsosummeri värähtelee samassa tahdissa kuin pinnin jännite vaihtelee, ja värähtelyn taajuus kuuluu äänenkorkeutena. Kun tiedät, miten taajuus ja äänenkorkeus liittyvät toisiinsa, voit laskea minkä tahansa sävelen taajuuden.

Työ kestää noin 30 minuuttia. Oman melodian säveltämiseen voi käyttää niin paljon aikaa kuin haluaa.

## Oppimistavoitteet

Työn jälkeen osaat

- kytkeä summerin Arduinoon ja soittaa sävelen komennolla `tone()`
- tallentaa melodian taulukoihin ja soittaa sen silmukassa
- selittää, miten taajuus ja äänenkorkeus liittyvät toisiinsa
- laskea sävelen taajuuden tasavireisen viritysjärjestelmän kaavalla.

## Lähtötaso ja ennakkotaidot

Olet tehnyt [Arduinon ensiaskeleet](ahjo-arduino.html) tai osaat ladata ohjelman Arduinoon. Äänestä ja taajuudesta kerrotaan luvussa [Ääni aaltona: korkeus, sointiväri ja Dopplerin ilmiö](fy5-14.html).

## Laitteet ja materiaalit

| Tarvike | Määrä |
|---|---|
| Arduino Uno ja USB-kaapeli | 1 |
| Passiivinen pietsosummeri | 1 |
| Kytkentäjohtimia (uros–uros) tai koekytkentälevy | 2 |
| Tietokone, jossa on Arduino IDE | 1 |

Käytä passiivista summeria. Aktiivinen summeri soittaa vain omaa kiinteää ääntään eikä noudata `tone()`-komennon taajuutta. Passiivisen summerin tunnistaa usein siitä, että sen alapuolelta näkyy piirilevy, ja se vain naksahtaa, kun sen kytkee suoraan $5\,\text{V}$:n jännitteeseen.

## Turvallisuus ja perehdytys

Ahjon turvallisuusohjeet ovat vielä valmisteilla. Katso aihe [Juottaminen ja elektroniikkatyöskentely](ahjo-turvallisuus.html#elektroniikka), ja noudata opettajan antamaa perehdytystä.

- Tee ja muuta kytkentöjä vain, kun USB-kaapeli on irti.
- Summerin ääni on lähellä korvaa voimakas. Pidä summeri pöydällä äläkä vie sitä korvan viereen.
- Sovi ryhmän kanssa, milloin soitetaan. Kymmenen summeria yhtä aikaa on rankka äänimaisema.

## Työvaiheet

1. Kytke USB-kaapeli irti. Kytke summerin plusjalka tai punainen johto pinniin 8 ja toinen jalka GND-pinniin. Jos summerissa ei ole merkintää, sen voi kytkeä kumpin päin tahansa.
2. Tarkista kytkentä kuvasta ja kytke sitten USB-kaapeli.
3. Avaa Arduino IDE ja kirjoita tai kopioi alla oleva ohjelma.
4. Valitse levyksi Arduino Uno ja oikea portti, ja lataa ohjelma painikkeella Upload. Summeri soittaa melodian, pitää kahden sekunnin tauon ja aloittaa alusta.
5. Muuta vakion `TEMPO` arvoa ja lataa ohjelma uudelleen. Mitä tapahtuu?
6. Muuta taulukoita `melodia` ja `kestot` ja tee oma melodia. Kummassakin taulukossa pitää olla yhtä monta lukua, ja vakion `N` pitää olla sama luku.

## Kuvat ja esimerkkikoodi

Kytkentäkaavio: summeri on pinnin 8 ja maan välissä.

<svg data-fig="kytkenta"></svg>

Esimerkkiohjelma soittaa kansanlaulun Ukko Nooa alun. Taajuudet on pyöristetty kokonaisiksi hertseiksi.

```cpp
// Sävelmä pietsosummerilla: pinni 8 -> summeri -> GND
const int SUMMERI = 8;   // pinni, johon summeri on kytketty
const int TEMPO = 350;   // yhden iskun kesto millisekunteina

// sävelten taajuudet hertseinä (C4 = 262, D4 = 294, E4 = 330, F4 = 349)
int melodia[] = {262, 262, 262, 330, 294, 294, 294, 349, 330, 330, 294, 294, 262};
int kestot[]  = {1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2};  // iskuina
const int N = 13;        // sävelten määrä

void setup() {
}

void loop() {
  for (int i = 0; i < N; i++) {
    int ms = kestot[i] * TEMPO;
    tone(SUMMERI, melodia[i], ms * 9 / 10);  // sävel soi 90 % ajasta, jotta sävelet erottuvat
    delay(ms);                               // odotetaan, kunnes sävel on soinut
  }
  noTone(SUMMERI);
  delay(2000);                               // tauko ennen uutta kierrosta
}
```

`tone(pinni, taajuus, kesto)` saa pinnin jännitteen vaihtelemaan $0\,\text{V}$:n ja $5\,\text{V}$:n välillä annetulla taajuudella. Komento ei odota sävelen loppumista, joten perään tarvitaan `delay()`.

## Testaa ja mittaa

- Toimintaperiaate: kun pinnin jännite vaihtelee, summerin pietsosähköinen levy taipuu edestakaisin samalla taajuudella. Levy saa ilman värähtelemään, ja korva kuulee värähtelyn äänenä. Mitä suurempi taajuus, sitä korkeampi ääni.
- Oktaavin päässä oleva sävel on taajuudeltaan kaksinkertainen. Soita $262\,\text{Hz}$ ja $523\,\text{Hz}$ peräkkäin ja kuuntele, kuulostavatko ne samalta säveleltä eri korkeudella.
- Haasta itsesi: tasavireisessä viritysjärjestelmässä oktaavi jakautuu kahteentoista yhtä suureen puolisävelaskeleeseen. Sävelen, joka on $n$ puolisävelaskelta A4-sävelen yläpuolella, taajuus on

$$f = 440\,\text{Hz} \cdot 2^{n/12}.$$

  Esimerkiksi C4 on 9 puolisävelaskelta A4:n alapuolella, joten $f = 440\,\text{Hz} \cdot 2^{-9/12} \approx 262\,\text{Hz}$. Duuriasteikon askeleet ovat koko, koko, puoli, koko, koko, koko ja puoli, eli 2, 2, 1, 2, 2, 2 ja 1 puolisävelaskelta. Laske C-duuriasteikon taajuudet C4:stä C5:een ja soita asteikko.

## Jos jokin ei toimi

| Oire | Todennäköinen syy | Korjaus |
|---|---|---|
| Ääntä ei kuulu | Johto on väärässä pinnissä | Tarkista, että johto on pinnissä 8. |
| Ääntä ei kuulu | Ohjelma ei latautunut | Tarkista levy ja portti Tools-valikosta ja lataa uudelleen. |
| Kuuluu vain yksi sama ääni | Summeri on aktiivinen | Vaihda passiiviseen summeriin. |
| Ääni on hyvin hiljainen | Summeri on kytketty väärin päin tai se on rikki | Käännä summeri. Jos ääni ei voimistu, vaihda summeri. |
| Ohjelma ei käänny | Taulukoissa on eri määrä lukuja tai puolipiste puuttuu | Laske taulukoiden luvut ja tarkista virheilmoituksen rivi. |
| Melodia on sekava | `N` ei vastaa taulukoiden pituutta | Muuta `N` samaksi kuin taulukoiden lukujen määrä. |

## Jatkotehtävä

1. Laskettu asteikko. Laske taajuudet ohjelmassa: `440.0 * pow(2.0, n / 12.0)`. Soita silmukalla kaikki 13 säveltä C4:stä C5:een.
2. Painikesoitin. Kytke kaksi painonappia pinneihin 2 ja 3 kuten [Arduinon ensiaskeleiden](ahjo-arduino.html) jatkotehtävässä ja tee soitin, jossa kumpikin nappi soittaa eri sävelen.
3. Valotheremin. Lue valovastuksen lukema analogiapinnistä ja muuta se taajuudeksi komennolla `map()`. Äänenkorkeus muuttuu, kun liikutat kättä anturin päällä. Tämä sopii tunnille 10.

## Dokumentoi

Kirjaa projektipäiväkirjaan

- valokuva kytkennästä ja oma kytkentäkaavio
- melodiasi taulukot ja lyhyt äänite tai video
- yksi asia, joka ei aluksi toiminut, ja miten korjasit sen
- jos teit haasteen, laskemasi taajuudet taulukkona.

## Opettajalle: valmistelu

- Tämä on luonnos: ohjetta ei ole kokeiltu Ahjon omilla laitteilla. Testaa ohjelma ja summeri ennen tuntia.
- Hanki passiivisia pietsosummereita. Aktiiviset summerit eivät noudata `tone()`-komennon taajuutta. Merkitse passiiviset, jos samassa laatikossa on molempia.
- Tallenna esimerkkiohjelma valmiiksi koulun koneille, jotta pikastartti onnistuu ilman kirjoittamista.
- Työ sopii Ahjo 1:n tunnille 9 vaihtoehtoiseksi tehtäväksi tai lisähaasteeksi. Se yhdistää työn musiikkiin ja fysiikan lukuun [Ääni aaltona: korkeus, sointiväri ja Dopplerin ilmiö](fy5-14.html).
- Kansanlaulu Ukko Nooa on vapaasti käytettävissä. Ohjeen teksti, kuva ja koodi on kirjoitettu Ruukkilabraan.
