# Takomo – miten Kiviruukissa opitaan

Interaktiivinen verkkokokemus, joka kertoo, miten oppiminen Kiviruukin lukiossa
toimii. Ei koulun kotisivu, vaan yksi tarina: *lukioon voi tulla tietämättä
tarkalleen, mikä itsestä tulee.* Suuntia voi kokeilla, ja oma polku rakentuu
vähitellen.

Pääviesti: **Meillä taotaan tulevaisuuksia.**

Tiedostot

| Tiedosto | Sisältö |
|---|---|
| `takomo/KONSEPTI.md` | Tämä dokumentti: informaatioarkkitehtuuri, vuorovaikutuskonsepti ja kuvakäsikirjoituksen teksti |
| `takomo/storyboard.html` | Visuaalinen kuvakäsikirjoitus, 9 ruutua |
| `takomo/index.html` | Toimiva responsiivinen prototyyppi |
| `brand/ahjo-makerspace-logo.png` | Ahjon alkuperäinen tunnus (toimitettu tiedosto, ei muokattu) |
| `brand/kiviruukin-lukio-logo-valkoinen.svg` | Kiviruukin lukion alkuperäinen tunnus |

---

## 1. Informaatioarkkitehtuuri

Kokemus on yksi vieritettävä sivu, jonka keskellä on vuorovaikutteinen
**polkukartta**. Kaikki muu kiertyy sen ympärille. Rakenteessa ei ole
alasivuja: syvemmät sisällöt (diplomipolut, Ahjo, yhteistyö) avautuvat
kartan solmuista ja omista jaksoistaan samalla sivulla.

```
TAKOMO  (takomo/index.html)
│
├─ 0  KIPINÄ ····················· hero
│     Meillä taotaan tulevaisuuksia.
│     "Lukioon ei tarvitse tulla valmiina." – valitse kipinä (kiinnostus)
│
├─ 1  KARTTA ····················· pääinteraktio
│     Kolme suuntaa kolmen vuoden yli, kaikki risteävät Ahjossa
│       • Yleislinja – leveä pohja, kaikkien alla
│       • Tiede & teknologia
│       • Talous & yrittäjyys
│     Solmut (klikattavia): projektit · tutkimus · korkeakoulu- ja
│       yritysyhteistyö · Ahjo · diplomityö · Kiviruukkipäivä
│     Esimerkkireitit + oma reitti
│
├─ 2  ETENEMINEN ················· tarinan rytmi
│     kiinnostu → tutki → kokeile → opi → rakenna → yhdistä → luo → näytä
│     kipinä kuumenee ja muotoutuu askel askeleelta
│
├─ 3  AHJO ······················· yhteinen solmu
│     Kiviruukin Makerspace: paikka, jossa ideasta tehdään jotain käsin
│     kosketeltavaa. Säteet: luonnontieteet · matematiikka · ohjelmointi ·
│     muotoilu · yrittäjyys · käytännön valmistaminen
│
├─ 4  DIPLOMIPOLUT ·············· tutkittavissa, ei hallitseva
│     Tiede- ja teknologia -diplomi  |  Talous- ja yrittäjyysdiplomi
│     yhteinen ydin: innovaatiot · tekoäly · korkeakoulu- ja yritysyhteistyö
│
├─ 5  YHTEISÖ ··················· et tee sitä yksin
│     opettajat ja ohjaus · VTT Bioruukki samassa rakennuksessa ·
│     kansainväliset projektit · Hype-areena · Cleantech Garden
│
└─ 6  OMA POLKU ················· yhteenveto
      kartalla koottu reitti piirretään yhdeksi "taotuksi" viivaksi.
      "Tämä on yksi mahdollinen polku. Niitä on monta." → aloita alusta
```

### Sisältöinventaario ja lähteet

Jokainen väite on jäljitettävissä toimitettuun aineistoon. Uusia
opintolinjoja, lukuja tai väitteitä ei ole lisätty.

| Sisältö | Lähde |
|---|---|
| Lukio aloittaa syksyllä 2027, ~1200 opiskelijaa, Espoon suurin; yleislinja n. 370 aloituspaikkaa kevään 2027 yhteishaussa | Mediatiedote 10/2025 |
| Yleislinja on vastuullisuuden ja maailmankansalaisuuden pohja; laaja tarjonta erikoistuneita opintoja | Mediatiedote 10/2025 |
| Cleantech Garden 1, VTT Bioruukki samassa rakennuksessa, yhteistyö-, vierailu- ja projektityö | Mediatiedote 10/2025 |
| Digitaalisen valmistamisen verstas: 3D-tulostus, laser- ja vinyylileikkaus, robotiikka, elektroniikka; STEAM-projektit yli oppiainerajojen | Mediatiedote 10/2025 |
| N. 10 kansainvälistä projektia vuodessa, YK-koulu, Model UN, englanninkielinen linja (lupa haettu), Hype-areena, Kivenlahden metroasema | Mediatiedote 10/2025 |
| Ahjo: Kiviruukin Makerspace, oppiainerajat ylittävä STEAM-oppimisympäristö; luonnontieteet, matematiikka, ohjelmointi, muotoilu, yrittäjyys ja käytännön valmistaminen yhdistyvät projekteiksi ja diplomitöiksi; Suunnittele · Kokeile · Rakenna · Kehitä; robotiikka, elektroniikka, 3D-mallinnus, 3D-tulostus, prototypointi; Ahjoa käytetään eri oppiaineiden opintojaksoilla; tukee sekä TT-polkua että yrittäjyysdiplomin innovaatio- ja prototyyppitöitä | Lukiodiplomit-esitys, dia 3 |
| Nuori rakentaa oman suunnan lukio-opintojen, projektien, yritys- ja korkeakouluyhteistyön ja käytännön tekemisen kautta; kiinnostus riittää; valintaa ei tarvitse tehdä ennen lukion alkua | Lukiodiplomit-esitys, dia 1 |
| TT-diplomi: Rakenna. Koodaa. Tutki. Näytä. Luonnontieteet, matematiikka ja teknologia; ohjelmointi, data, tekoäly, robotiikka ja prototypointi; oma prototyyppi, sovellus tai tutkimus | Lukiodiplomit-esitys, dia 2 |
| TY-diplomi: Ideoi. Kokeile. Verkostoidu. Kasva. Talous, työelämätaidot, yrittäjyys ja innovointi; markkinointi, sijoittaminen, verkostot ja yritysyhteistyö; pitchaus, liikeidea tai kehittämistehtävä | Lukiodiplomit-esitys, dia 2 |
| Molemmat: vähintään 6 op polkuun soveltuvia opintoja + 2 op diplomikurssi, voi rakentaa laajemmaksi; sama perusidea; diplomityö Kiviruukkipäivässä; polku ei ole valintakoe eikä lukkoon lyötyjä opintoja vaan omasta kiinnostuksesta rakentuva kokonaisuus | Lukiodiplomit-esitys, dia 2 |
| Eteneminen: 1. vuosi kokeile → 2. vuosi syvennä → diplomityö → 3. vuosi Kiviruukkipäivä | Lukiodiplomit-esitys, dia 2 |
| Tunnus kipinänä ja liekkinä, idean syttymisen symboli; ruukkien maailma modernilla muotokielellä; Espoon brändipaletin päävärit | Graafinen ohjeisto (Miltton) |
| Ruukki: paikka, jossa taottiin rautaa ja jonka ympärille kasvoi kylä; Kiviruukissa taotaan tietoa; kipinät sinkoilevat ideoista, oivalluksista ja uteliaisuudesta; lujan yhteisön osana jokaisen kipinä voi kasvaa liekiksi; pääviesti *Meillä taotaan tulevaisuuksia* | Brändin taustatarina |
| Ahjon tunnus (Marjapuuro + Yönsininen) | Toimitettu logotiedosto, sama kuva kuin esityksen diassa 3 |

Sisällöt, joita toimitetussa aineistossa *ei* ole ja joita ei siksi käytetä:
aiemmilla sivuilla näkyneet opintojaksolistat (esim. kyberturvallisuus,
bioteknologia, Global Business, Vuosi yrittäjänä), opintopistekoodit ja
Tiedemessut-nimi. Ne voi lisätä, kun ne vahvistuvat.

---

## 2. Vuorovaikutuskonsepti

### Metafora

Sivu on takomo. **Kipinä** on kiinnostus. Kipinä kuumenee **ahjossa**, saa
muodon **alasimella** ja lopulta **näytetään**. Yhteisö on takomon väki: kukaan ei
tao yksin. Kolme suuntaa ovat kolme hehkuvaa nauhaa, jotka kulkevat saman ahjon
läpi, eivät kolme erillistä putkea.

### Kolme periaatetta

1. **Monta reittiä, ei yhtä.** Jokainen kartan solmu on tavoitettavissa jokaisesta
   suunnasta. Käyttöliittymä ei koskaan sano "valitse linja ensin".
2. **Tila ennen tekstiä.** Käyttäjä ymmärtää rakenteen katsomalla, miten nauhat
   leikkaavat ja missä ne kohtaavat. Teksti on korttien sisällä, yksi solmu
   kerrallaan.
3. **Teot ovat verbejä.** Eteneminen (kiinnostu → näytä) näkyy tilana, ei
   luettelona: kipinä muuttuu askel askeleelta hehkuvaksi kappaleeksi.

### Pääinteraktio: polkukartta

* **Näkymä.** Vaakasuuntainen kenttä (mobiilissa pystysuuntainen), vasemmalla
  "Tulet Kiviruukkiin", oikealla "Näytä". Kolme nauhaa: Yleislinja leveänä
  pohjana koko matkan, Tiede & teknologia ja Talous & yrittäjyys kapeampina,
  ne eroavat, risteävät ja palaavat yhteen. Keskellä hehkuva Ahjo-solmu,
  jonka läpi molemmat kulkevat.
* **Solmut.** Kahdeksan klikattavaa solmua: Yleislinjan opinnot, Projekti,
  Tutkimus, Ahjo, Yritys- ja korkeakouluyhteistyö, Kansainvälinen projekti,
  Diplomityö, Kiviruukkipäivä. Klikkaus avaa pienen kortin: mitä solmussa
  tehdään, mitkä suunnat sitä käyttävät, mihin se voi johtaa seuraavaksi.
* **Kipinän valinta** (hero): käyttäjä valitsee yhden kiinnostuksen
  ("Haluan tietää miten asiat toimivat", "Minulla on idea", "Haluan tehdä käsillä",
  "En vielä tiedä"). Valinta korostaa yhden *esimerkkireitin* kartalla
  himmeänä ehdotuksena, mutta kaikki solmut pysyvät avoimina. "En vielä tiedä"
  korostaa Yleislinjan ja ensimmäisen vuoden kokeilusolmut.
* **Oma reitti.** Solmun kortista "Lisää polkuuni". Reitti piirtyy kuumana
  viivana solmujen läpi siinä järjestyksessä kuin ne lisättiin. Viiva saa
  vaihtaa suuntaa vapaasti: tiede → yrittäjyys → Ahjo → diplomityö on yhtä
  hyvä reitti kuin suora. Jos reitti kulkee molempien diplominauhojen läpi,
  kartta nostaa esiin "Yhdistit" -merkinnän.
* **Esimerkkireitit.** Neljä valmista reittiä (Kokeilija, Tutkija,
  Tekijä, Yhdistelijä) näyttävät nopeasti, että polut risteävät. Nämä ovat
  havainnollistuksia, eivät opintoputkia, ja niin ne myös nimetään.
* **Eteneminen seuraa reittiä.** Kun solmuja lisätään, osion 2 verbit
  syttyvät: ensimmäinen solmu sytyttää "kiinnostu" ja "tutki", Ahjo
  "kokeile" ja "rakenna", diplomityö "luo", Kiviruukkipäivä "näytä".

### Toissijaiset interaktiot

* **Ahjo-säteet.** Kuusi sädettä konvergoivat Ahjon tunnuksen muotoon.
  Osoitin tai kosketus säteellä kertoo, mitä kyseinen ala tuo ahjoon.
* **Diplomipolut.** Kaksi korttia, joista vain yksi on auki kerrallaan.
  Välissä yhteinen ydin, joka pysyy näkyvissä kummassakin tilassa. Vuosirytmi
  (tutustu – syvennä – esittele) on yhteinen ja piirretty kerran.
* **Oma polku -yhteenveto.** Reitti piirretään uudelleen yhdeksi taotuksi
  viivaksi ja sen alle listataan käytetyt verbit. "Aloita alusta" tyhjentää
  reitin ja palauttaa karttaan.

### Saavutettavuus ja laitteet

* Kaikki solmut ovat painikkeita; kortit ovat `dialog`-tyyppisiä alueita, jotka
  sulkeutuvat Esc-näppäimellä. Reitin tila luetaan ruudunlukijalle `aria-live`-alueelta.
* `prefers-reduced-motion`: kipinät ja hehku pysähtyvät, siirtymät lyhenevät.
* Mobiili (alle 760 px): kartta kääntyy pystyyn, nauhat kulkevat ylhäältä alas,
  kortit avautuvat alareunan paneelina.
* Ei ulkoisia kirjastoja: yksi HTML-tiedosto, inline-SVG, vanilla JS.

### Visuaalinen järjestelmä (graafisen ohjeiston mukaan)

* Värit: Yönsininen `#012169`, Marjapuuro `#FCA5C7`, valkoinen. Samat kolme
  väriä kuin Ahjon tunnuksessa ja Kiviruukin lukion tunnuksen käyttöohjeissa.
  Tiede & teknologia erotetaan valkoisella, Talous & yrittäjyys Marjapuurolla,
  Yleislinja vaalealla Yönsinisen sävyllä. Hehku on aina Marjapuuro.
* Typografia: Lato (otsikot, 900) ja Work Sans (leipäteksti), kuten muissa
  Kiviruukin sivuissa.
* Tunnukset: Kiviruukin lukion tunnus (alkuperäinen SVG) ja Ahjon tunnus
  (alkuperäinen PNG) käytetään sellaisenaan, riittävällä suoja-alueella,
  aina Yönsinisellä tai valkoisella pohjalla. Tunnuksen säteet jatkuvat
  taustalle *sädekehänä*, kuten ohjeiston sovelluksissa; itse tunnusta ei piirretä
  uudelleen.
* Tunnelma: moderni, rohkea, optimistinen, älykäs, hiukan teollinen, mutta
  lämmin: lyhyet lauseet, isot verbit, hehkua ja käsin tekemisen sanastoa,
  ei teknologista kiiltoa.

---

## 3. Kuvakäsikirjoitus

Visuaalinen versio: `takomo/storyboard.html`. Alla ruudut ja niiden tarkoitus.

| # | Ruutu | Mitä näkyy | Mitä käyttäjä tekee | Mitä hän ymmärtää |
|---|---|---|---|---|
| 1 | Kipinä | Yönsininen pohja, tunnuksen sädekehä nousee alareunasta. Iso otsikko *Meillä taotaan tulevaisuuksia.* Alla neljä kipinä-nappia. | Valitsee kipinän (tai ohittaa). | Tänne saa tulla keskeneräisenä. |
| 2 | Kartta avautuu | Kolme nauhaa vierivät näkyviin vasemmalta. Yleislinja leveänä pohjana, kaksi kapeampaa nauhaa sen päällä. Ahjo hehkuu keskellä. | Vierittää, katsoo. | Kolme suuntaa, yksi yhteinen paikka. |
| 3 | Solmu avautuu | Käyttäjä koskee *Tutkimus*-solmua. Kortti: mitä, kenelle, mihin johtaa. Nappi *Lisää polkuuni*. | Lisää solmun. | Solmut ovat tekoja, eivät kursseja. |
| 4 | Reitti risteää | Kuuma viiva kulkee Tiede-nauhalta Ahjon kautta Yrittäjyys-nauhalle. Kartta näyttää merkinnän *Yhdistit kaksi suuntaa.* | Lisää lisää solmuja, vaihtaa suuntaa. | Suunnat eivät ole putkia. |
| 5 | Eteneminen | Kahdeksan verbiä vaakarivissä, kipinä → hehkuva kappale. Reitin solmut ovat sytyttäneet osan verbeistä. | Vierittää; verbit syttyvät. | Oppiminen etenee tekemällä. |
| 6 | Ahjo | Ahjon tunnus keskellä, kuusi sädettä konvergoi siihen. Yksi säde korostettuna. | Koskee säteitä. | Ahjo on paikka, jossa ideasta tulee esine. |
| 7 | Diplomipolut | Kaksi korttia rinnakkain, yhteinen ydin välissä, vuosirytmi alla. Vain yksi kortti auki. | Avaa toisen, sitten toisen. | Diplomi on yksi tapa syventää, ei ainoa. |
| 8 | Yhteisö | Kuvia ei ole: sanat ja viivat. *Et tee sitä yksin.* Opettajat, VTT Bioruukki, kansainväliset projektit, Hype-areena. | Lukee. | Takomossa on väkeä. |
| 9 | Oma polku | Reitti piirretään yhdeksi taotuksi viivaksi, verbit alla. *Tämä on yksi mahdollinen polku. Niitä on monta.* | Aloittaa alusta tai jakaa. | Polku on oma, ja sen saa taoa uudelleen. |
