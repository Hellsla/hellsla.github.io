# Energiantuotanto, ympäristö ja ilmastonmuutos

> **Miksi** sähkön tuotantotavan valinta ratkaisee, kuinka paljon hiilidioksidia ilmakehään päätyy, vaikka kodin pistorasiasta tulee aina samanlaista sähköä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keskellä talo, johon sähkö tulee voimalinjaa pitkin. Vasemmalla hiilivoimala, jonka savupiipusta nousee tumma savu harmaalle taivaalle; oikealla tuulivoimaloita kirkkaan taivaan alla. Talon seinässä on pistorasia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Aurinko lämmittää maanpintaa säteilemällä sille energiaa, näkyvänä valona ja lähi-infrapunasäteilynä. Ilmakehä päästää tämän säteilyn suurelta osin läpi. Lämmin maanpinta lähettää energiaa takaisin avaruuteen lämpösäteilynä, ja sitä ilmakehän **kasvihuonekaasut** imevät. Tärkeimpiä niistä ovat vesihöyry, hiilidioksidi $\text{CO}_2$ ja metaani $\text{CH}_4$. Ne säteilevät energian uudelleen joka suuntaan, joten osa siitä palaa takaisin maanpinnalle.

Kasvihuonekaasut siis päästävät auringon säteilyn läpi mutta hidastavat lämpösäteilyn pääsyä pois. Maanpinta pysyy lämpimämpänä kuin ilman niitä. Maan yksinkertaisesta säteilytasapainomallista saadaan efektiiviseksi säteilylämpötilaksi noin $-18\,{}^\circ\text{C}$, mutta maanpinnan keskilämpötila on noin $+15\,{}^\circ\text{C}$. Ero havainnollistaa **kasvihuoneilmiön** merkitystä. Lukua $-18\,{}^\circ\text{C}$ ei kuitenkaan pidä lukea täsmälliseksi ennusteeksi pintalämpötilasta, jos kasvihuonekaasut poistettaisiin, sillä silloin muuttuisivat myös esimerkiksi pilvet ja jääpeite. Luonnollinen kasvihuoneilmiö pitää maapallon asuttavana, sillä ilman sitä merien vesi olisi jäässä.

```pysahdy
Mikä kasvihuonekaasuissa saa maanpinnan pysymään lämpimänä, vaikka ne päästävät auringon säteilyn läpi?
---
Ne hidastavat maanpinnan lähettämän lämpösäteilyn pääsyä avaruuteen ja säteilevät osan energiasta takaisin maanpinnalle.
```

<svg data-fig="greenhouse" viewBox="0 0 600 440" role="img" aria-label="Periaatekuva, ei mittakaavassa: kasvihuoneilmiö. Auringon säteily (oranssi nuoli), näkyvä valo ja lähi-infrapuna, kulkee suurelta osin ilmakehän läpi ja lämmittää maanpinnan. Lämmin maanpinta lähettää lämpösäteilyä ylöspäin (punaiset nuolet), ja ilmakehän kasvihuonekaasut imevät sen. Kaasut säteilevät energian uudelleen: osa palaa takaisin alas maanpinnalle ja osa karkaa avaruuteen. Nuolten paksuus havainnollistaa suuntaa, ei tarkkoja energioita." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-8-greenhouse.webp" x="-1.3" y="-1.3" width="603" height="449.7" preserveAspectRatio="none"/>
  <foreignObject x="173" y="175.5" width="290" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilmakehä (kasvihuonekaasut)}$</div></foreignObject>
  <foreignObject x="230" y="389.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maanpinta}$</div></foreignObject>
  <foreignObject x="12" y="277.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{auringon}$</div></foreignObject>
  <foreignObject x="12" y="307.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{säteily}$</div></foreignObject>
  <foreignObject x="312" y="285.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämpö-}$</div></foreignObject>
  <foreignObject x="312" y="315.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{säteily}$</div></foreignObject>
  <foreignObject x="488" y="275.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{takaisin}$</div></foreignObject>
  <foreignObject x="488" y="305.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{alas}$</div></foreignObject>
  <foreignObject x="288" y="97.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{avaruuteen}$</div></foreignObject>
</svg>

Ongelma on ilmiön voimistuminen. Kun ihminen lisää ilmakehään hiilidioksidia ja metaania, lämpösäteily pääsee pois entistä hitaammin ja maapallon keskilämpötila nousee. Tätä pitkäaikaista muutosta sanotaan **ilmastonmuutokseksi**. Hiilidioksidin pitoisuus ilmakehässä on kasvanut noin $280\,\text{ppm}$:stä (ennen teollistumista) noin $424\,\text{ppm}$:ään (maailmanlaajuinen keskiarvo vuonna 2024, WMO:n kasvihuonekaasutiedote 2025). Hiilidioksidia on silti alle puoli promillea ilmasta. Pieni osuus riittää, koska ilman pääkaasut typpi ja happi eivät juuri ime lämpösäteilyä: juuri harvat kasvihuonekaasumolekyylit ratkaisevat, kuinka helposti lämpösäteily pääsee pois.

Kasvihuoneilmiötä käsitellään laskemalla FY3-kurssilla luvussa *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*. Tässä riittää ymmärtää, mitä kaasut tekevät säteilylle ja mistä lisäkaasut tulevat.

<figure class="unit-photo wide"><img src="pics/fy2/gistemp-2025-anomaly-map.webp" alt="Maailmankartta, jonka värit vaihtelevat vaaleasta tummanpunaiseen. Tummin punainen on pohjoisilla alueilla. Kartan alla on väriasteikko sinisestä punaiseen."><figcaption>Vuoden 2025 keskilämpötila verrattuna vuosien 1951–1980 keskiarvoon NASAn GISTEMP-aineiston mukaan. Punainen tarkoittaa vertailujaksoa lämpimämpää ja sininen kylmempää. Harmaa väri (selitteessä ”no data”) tarkoittaa, että alueelta ei ole mittauksia. Kartta on mittausaineistosta tehty visualisointi, ei valokuva.</figcaption></figure>

### Polttoaineet yhdistävät energian ja ilmaston
Fossiilinen polttoaine, kuten kivihiili, öljy tai maakaasu, on muinaisten eliöiden kemiallista energiaa: kivihiili on syntynyt enimmäkseen kasveista, öljy ja maakaasu meren planktonista. Kun tällainen hiiltä sisältävä polttoaine palaa täydellisesti, sen hiili yhtyy hapen kanssa: $\text{C} + \text{O}_2 \rightarrow \text{CO}_2$. Kemiallinen energia vapautuu lämpönä (luku *Polttoaineet ja lämpöarvo*), ja hiilidioksidi poistuu savukaasujen mukana ilmakehään. Mitä enemmän energiaa otetaan polttamalla hiilipitoisia polttoaineita, sitä enemmän hiilidioksidia vapautuu. Kaikissa polttoaineissa ei ole hiiltä: esimerkiksi vedyn palaessa syntyy vain vettä.

```pysahdy
Miksi vedyn polttaminen ei lisää ilmakehän hiilidioksidia?
---
Vety ei sisällä hiiltä, joten palaessa ei synny $\text{CO}_2$:ta vaan vettä.
```

Fossiilisen polttoaineen hiili on ollut maan alla miljoonia vuosia, joten sen polttaminen lisää ilmakehän hiilidioksidia. Biomassan, esimerkiksi puun, hiili on sitoutunut kasveihin vasta vuosikymmenten aikana. Biomassan poltto ei silti ole päästötöntä: polton hiilidioksidi on ilmakehässä, kunnes uusi kasvu sitoo sen takaisin, mikä kestää vuosikymmeniä ja edellyttää, että kasvusto todella kasvaa uudelleen. Lisäksi viljely, korjuu ja kuljetus aiheuttavat omia päästöjä.

<figure class="unit-photo"><img src="pics/fy2/europe-at-night.webp" alt="Yöllinen Eurooppa ylhäältä: tummalla maalla on tiheästi oransseja valopisteitä ja suurten kaupunkien kirkkaita valoalueita."><figcaption>Luoteis-Eurooppa yöllä kansainväliseltä avaruusasemalta kuvattuna vuonna 2011. Kaupunkien valot näkyvät avaruuteen asti.</figcaption></figure>

### Tuotantotapoja verrataan elinkaaren päästöillä
Päästöjä syntyy muustakin kuin polttamisesta. Voimala on rakennettava teräksestä, betonista ja kuparista, polttoaine on kaivettava tai kerättävä ja kuljetettava, ja lopuksi voimala puretaan. Siksi tuotantotapoja verrataan **elinkaaren päästöillä**: kaikkien vaiheiden päästöt lasketaan yhteen ja jaetaan koko elinkaarella tuotetulla energialla.

```pysahdy
Tuulivoimala ei polta mitään. Miksi sen elinkaaren päästöt eivät silti ole nolla?
---
Päästöjä syntyy voimalan rakentamisessa, kuljetuksissa ja purkamisessa, vaikka tuotannon aikana ei synny savukaasuja.
```

Metaani ja muut kasvihuonekaasut muutetaan vertailua varten hiilidioksidiekvivalenteiksi ($\text{CO}_2$-ekv.), eli sellaiseksi hiilidioksidin määräksi, jolla on sama lämmittävä vaikutus.

### Päästöt eivät ole ainoa peruste
Ilmastovaikutuksen lisäksi tuotantotapoja punnitaan maankäytön, kuljetusten, jätteen ja turvallisuuden kannalta:

- **Kivihiili ja maakaasu:** suurimmat päästöt. Polttoaineet kaivetaan ja kuljetetaan laivoilla, junilla tai putkissa, ja savukaasut sisältävät myös muita epäpuhtauksia.
- **Biomassa:** vie metsä- ja peltoalaa. Biomassa on tilavaa ja sen energiasisältö massaa kohti on pieni, joten sitä ei kannata kuljettaa kauas.
- **Aurinko- ja tuulivoima:** tarvitsevat paljon pinta-alaa tuotettua energiaa kohti, ja tuulivoima vaikuttaa maisemaan ja linnustoon. Tuotanto riippuu säästä, joten tarvitaan säätövoimaa tai varastointia.
- **Vesivoima:** padot ja altaat muuttavat jokiympäristöä ja estävät kalojen kulun, mutta tuotantoa voi säätää.
- **Ydinvoima:** pinta-alaa kuluu vähän, ja polttoainetta tarvitaan massana vähän, joten kuljetuksia on vähän. Käytetty polttoaine on radioaktiivista jätettä, joka on eristettävä pitkäksi aikaa, ja onnettomuuden seuraukset voisivat olla vakavia, vaikka riski on pieni.

**Kestävä energiatalous** tuottaa ja käyttää energiaa niin, ettei nykyisten tarpeiden tyydyttäminen vie tulevilta sukupolvilta mahdollisuuksia. Parasta voimalaa ei ole: valinnassa punnitaan ilmastovaikutusta, maankäyttöä, jätettä, turvallisuutta, hintaa ja sitä, että sähköä on aina saatavilla (luku *Energiantuotantotavat ja niiden vertailu*).

## Kaava: Hiilidioksidipäästö
Päästö saadaan kertomalla käytetty tai tuotettu energia päästökertoimella:

```latex
m = e \cdot E
```
missä $m$ on päästö ($\text{g}$ tai $\text{kg}$ hiilidioksidiekvivalenttia), $e$ **päästökerroin** ($\text{g/kWh}$) ja $E$ energia ($\text{kWh}$).

Päästökerroin kertoo, montako grammaa hiilidioksidiekvivalenttia syntyy yhtä kilowattituntia kohti. Yksikkö kulkee mukana: kun $\text{g/kWh}$ kerrotaan kilowattitunneilla, jäljelle jäävät grammat. Kilowattitunti on energian yksikkö, $1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}$. Samalla tavalla lasketaan myös polttoaineen päästö, kun kerroin on esimerkiksi $\text{g/MJ}$ ja energia megajoulina.

| Tuotantotapa | $e\ (\text{g/kWh})$ |
|---|---|
| Kivihiili | 820 |
| Maakaasu | 490 |
| Biomassa | 230 |
| Aurinkosähkö | 41–48 |
| Vesivoima | 24 |
| Ydinvoima | 12 |
| Tuulivoima | 11–12 |

Taulukon lähde on IPCC:n viides arviointiraportti (AR5, 2014), työryhmä III, liite III: elinkaaren päästöjen mediaanit pyöristettyinä, yksikkö gramma hiilidioksidiekvivalenttia kilowattituntia kohti. Aurinkosähkön alaraja on kattopaneeleille, yläraja voimalaitoskokoluokalle; tuulivoiman alaraja on maalla, yläraja merellä. Biomassan luku koskee energiaa varten kasvatettua biomassaa. Siinä ovat viljelyn, korjuun, kuljetusten ja voimalan päästöt, mutta polton hiilidioksidi on laskettu nollaksi, koska uusi kasvu sitoo hiiltä takaisin. Tämä on päästövertailussa käytetty laskentaoletus, ei väite siitä, ettei biomassan poltossa vapautuisi hiilidioksidia. Todellinen ilmastovaikutus riippuu myös biomassan alkuperästä, hiilivarastojen muutoksista ja siitä, kuinka nopeasti hiili sitoutuu takaisin kasvillisuuteen. Luku ei siis näytä sitä, että sitoutuminen kestää vuosikymmeniä.

<svg data-fig="emissions" viewBox="0 0 600 450" role="img" aria-label="Vaakapylväskaavio sähköntuotannon elinkaaren päästökertoimista yksikössä g hiilidioksidiekvivalenttia kilowattituntia kohti (IPCC AR5, työryhmä III, liite III, pyöristetyt mediaanit): kivihiili 820, maakaasu 490, biomassa 230, aurinkosähkö 41–48, vesivoima 24, ydinvoima 12 ja tuulivoima 11–12. Pylväiden pituudet ovat mittakaavassa: kivihiilen pylväs on noin 70 kertaa ydinvoiman pylvään pituinen. Fossiilisten polttoaineiden pylväät ovat tummanharmaita, muiden tuotantotapojen vaaleanharmaita; selite on kuvan alla." style="max-width:100%;font-size:24px">
  <foreignObject x="150" y="9.5" width="360" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e\ \left(\text{g}\ \text{CO}_2\text{-ekv.}/\text{kWh}\right)$</div></foreignObject>
  <line x1="238" y1="52" x2="238" y2="352" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326" y1="52" x2="326" y2="352" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414" y1="52" x2="414" y2="352" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="502" y1="52" x2="502" y2="352" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="150" y="56" width="361" height="28" rx="2" fill="#6c757d"/>
  <foreignObject x="15" y="55.5" width="125" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kivihiili}$</div></foreignObject>
  <foreignObject x="519" y="55.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$820$</div></foreignObject>
  <rect x="150" y="98" width="215.5" height="28" rx="2" fill="#6c757d"/>
  <foreignObject x="15" y="97.5" width="125" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{maakaasu}$</div></foreignObject>
  <foreignObject x="373.5" y="97.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$490$</div></foreignObject>
  <rect x="150" y="140" width="101" height="28" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="15" y="139.5" width="125" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{biomassa}$</div></foreignObject>
  <foreignObject x="259" y="139.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$230$</div></foreignObject>
  <rect x="150" y="182" width="20" height="28" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="15" y="181.5" width="125" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{aurinko}$</div></foreignObject>
  <foreignObject x="178" y="181.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$41\text{–}48$</div></foreignObject>
  <rect x="150" y="224" width="10.5" height="28" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="15" y="223.5" width="125" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesivoima}$</div></foreignObject>
  <foreignObject x="168.5" y="223.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$24$</div></foreignObject>
  <rect x="150" y="266" width="5.5" height="28" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="15" y="265.5" width="125" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ydinvoima}$</div></foreignObject>
  <foreignObject x="163.5" y="265.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$12$</div></foreignObject>
  <rect x="150" y="308" width="5.5" height="28" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="15" y="307.5" width="125" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{tuuli}$</div></foreignObject>
  <foreignObject x="163.5" y="307.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$11\text{–}12$</div></foreignObject>
  <line x1="150" y1="352" x2="530" y2="352" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M542,352 L529,358 L529,346 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="150" y1="50" x2="150" y2="354" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="120" y="365.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <line x1="238" y1="352" x2="238" y2="359" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="208" y="365.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$200$</div></foreignObject>
  <line x1="326" y1="352" x2="326" y2="359" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="296" y="365.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$400$</div></foreignObject>
  <line x1="414" y1="352" x2="414" y2="359" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="384" y="365.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$600$</div></foreignObject>
  <line x1="502" y1="352" x2="502" y2="359" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="472" y="365.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$800$</div></foreignObject>
  <rect x="150" y="413" width="28" height="22" rx="2" fill="#6c757d"/>
  <foreignObject x="186" y="409.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{fossiilinen}$</div></foreignObject>
  <rect x="350" y="413" width="28" height="22" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="386" y="409.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{muu}$</div></foreignObject>
</svg>

Kuvassa kaikki pylväät on piirretty samaan mittakaavaan. Tummat pylväät ovat fossiilisia polttoaineita, vaaleat muita tuotantotapoja. Kivihiilen päästökerroin on noin $70$-kertainen ydin- ja tuulivoimaan verrattuna ($820 : 12 \approx 68$). Ydin- ja tuulivoiman pylväät ovat kapeita mutta eivät nollia: niidenkin elinkaareen kuuluu rakentamista ja kuljetuksia.

## Esimerkki
Esimerkkiperhe käyttää sähköä $4800\,\text{kWh}$ vuodessa. Sähkö tuotetaan maakaasulla, jonka elinkaaren päästökerroin on $490\,\text{g/kWh}$. Kuinka monta tonnia hiilidioksidiekvivalenttia perheen sähkönkäytöstä syntyy vuodessa? (Perhe on keksitty esimerkki, ei tilasto.)

<!-- vaihe -->

**Tunnetut ja kysytty.**

- $E = 4800\,\text{kWh}$ ja
- $e = 490\,\text{g/kWh}$.

Kysytään päästöä $m$ tonneina.

<!-- vaihe -->

**Periaate.** Päästö on suoraan verrannollinen tuotettuun energiaan, ja päästökerroin kertoo päästön yhtä kilowattituntia kohti. Koko elinkaaren päästö saadaan siis kertomalla energia päästökertoimella.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
m = e \cdot E
```

<!-- vaihe -->

**Yksikkömuunnokset.** Kilowattitunnit supistuvat, joten tulos tulee grammoina. Grammat muutetaan tonneiksi: $1\,\text{g} = 0{,}001\,\text{kg}$ ja $1\,\text{kg} = 0{,}001\,\text{t}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
m &= e \cdot E \\
&= 490\,\text{g/kWh} \cdot 4800\,\text{kWh} \\
&= 2\,352\,000\,\text{g} \\
&= 2\,352\,000 \cdot 0{,}001\,\text{kg} \\
&= 2352\,\text{kg} \\
&= 2352 \cdot 0{,}001\,\text{t} \\
&= 2{,}352\,\text{t}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Päästö on $m \approx 2{,}4\,\text{t}$ hiilidioksidiekvivalenttia vuodessa, kahden merkitsevän numeron tarkkuudella kuten päästökertoimessa $490\,\text{g/kWh}$.

<!-- vaihe -->

**Järkevyys.** Pyöristetyillä luvuilla $500\,\text{g/kWh} \cdot 5000\,\text{kWh} = 2\,500\,000\,\text{g} = 2\,500\,000 \cdot 10^{-6}\,\text{t} = 2{,}5\,\text{t}$, mikä on lähellä tulosta. Jos sama sähkö tuotettaisiin tuulivoimalla, päästö olisi $12\,\text{g/kWh} \cdot 4800\,\text{kWh} = 57\,600\,\text{g} = 57\,600 \cdot 0{,}001\,\text{kg} \approx 58\,\text{kg}$, noin $41$ kertaa pienempi ($490 : 12 \approx 41$).

## Yleinen virhekäsitys
**"Tuuli-, aurinko- ja ydinvoima ovat päästöttömiä."** Ne ovat pienipäästöisiä, eivät päästöttömiä: voimaloiden rakentaminen, polttoaineen valmistus ja kuljetukset aiheuttavat päästöjä, tuulivoimalla ja ydinvoimalla noin $12\,\text{g/kWh}$. Kivihiilellä luku on noin $820\,\text{g/kWh}$.

**"Kasvihuoneilmiö on haitallinen ilmiö."** Luonnollinen kasvihuoneilmiö on välttämätön, sillä ilman sitä maanpinta olisi paljon nykyistä kylmempi: yksinkertainen säteilytasapainomalli antaa Maalle vain noin $-18\,{}^\circ\text{C}$:n efektiivisen säteilylämpötilan. Ongelma on ilmiön voimistuminen, kun ilmakehään lisätään hiilidioksidia ja metaania.

## Tiivistelmä
- Kasvihuonekaasut päästävät auringon säteilyn suurelta osin läpi mutta hidastavat maanpinnan lämpösäteilyn pääsyä pois. Maan yksinkertaisesta säteilytasapainomallista saatu efektiivinen säteilylämpötila on noin $-18\,{}^\circ\text{C}$, mutta maanpinnan keskilämpötila on noin $+15\,{}^\circ\text{C}$. Ero havainnollistaa luonnollisen kasvihuoneilmiön merkitystä.
- Fossiilisten polttoaineiden polttaminen lisää ilmakehän hiilidioksidia, voimistaa kasvihuoneilmiötä ja johtaa ilmastonmuutokseen.
- Päästö on päästökerroin kertaa energia: $m = e \cdot E$. Tuotantotapoja verrataan elinkaaren päästökertoimilla, jotka vaihtelevat noin $12\,\text{g/kWh}$:sta (ydin- ja tuulivoima) noin $820\,\text{g/kWh}$:iin (kivihiili).
- Biomassan päästökertoimessa polton hiilidioksidi on laskentaoletuksena nolla; todellinen ilmastovaikutus riippuu biomassan alkuperästä, hiilivarastojen muutoksista ja siitä, kuinka nopeasti hiili sitoutuu takaisin.
- Päästökerroin ei kerro kaikkea: maankäyttö, kuljetukset, jäte, turvallisuus ja sähkön saatavuus punnitaan erikseen, kun etsitään kestävää energiataloutta.
