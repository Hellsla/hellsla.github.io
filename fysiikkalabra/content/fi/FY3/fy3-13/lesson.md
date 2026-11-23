# Absoluuttisen nollapisteen määrittäminen

> **Miksi** alin mahdollinen lämpötila voidaan määrittää koulun laboratoriossa, vaikka lämpömittari ei ulotu lähellekään sitä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratoriopöydällä on kolme astiaa: jäävesi, huoneenlämpöinen vesi ja kuumalla levyllä kiehuva vesi. Keskimmäisessä hauteessa on suljettu lasipullo, joka on letkulla yhdistetty painemittariin." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-13-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Suljetussa jäykässä astiassa kaasun tilavuus ja ainemäärä eivät muutu, joten paine riippuu vain lämpötilasta. Kaasulämpömittarissa lasipullo on vesihauteessa. Hauteen lämpötila $\theta$ luetaan lämpömittarista ja kaasun paine $p$ painemittarista, kun haude lämpenee.

<svg data-fig="thermometer" viewBox="0 0 600 372" role="img" aria-label="Kaasulämpömittari: suljettu lasipullo, jossa on ilmaa, on vesihauteessa, jota lämmitetään. Pullon kaasun tilavuus ei muutu. Vesihauteen lämpötila luetaan lämpömittarista ja kaasun paine painemittarista. Kuva on kaavio eikä mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-13-thermometer.webp" x="0" y="0" width="600" height="378.8" preserveAspectRatio="none"/>
  <foreignObject x="75" y="91" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\theta$</div></foreignObject>
  <foreignObject x="460" y="133" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p$</div></foreignObject>
  <foreignObject x="380" y="174" width="220" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{painemittari}$</div></foreignObject>
  <foreignObject x="316" y="341" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$Q$</div></foreignObject>
  <foreignObject x="320" y="214" width="160" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{vesihaude}$</div></foreignObject>
  <foreignObject x="320" y="258" width="270" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{ilma},\ V=\text{vakio}$</div></foreignObject>
</svg>

Kun mittaustulokset piirretään kuvaajaan, pisteet asettuvat lähes suoralle: paine kasvaa lähes yhtä paljon jokaista celsiusastetta kohti. Todellisissa mittaussarjoissa pisteet eivät silti yleensä ole täsmälleen samalla suoralla mittausepävarmuuden vuoksi. Mittausepävarmuus kuvaa mittaustulokseen liittyvää epävarmuutta. Se ei yleensä tarkoita ehdotonta suurinta mahdollista poikkeamaa oikeasta arvosta. Tässä paineen lukeman epävarmuudeksi on arvioitu $\pm 1\,\text{kPa}$. Valmistajan mittarille ilmoittama virheraja on eri asia: se on laitteen ominaisuus, ja mittauksen epävarmuuteen vaikuttavat lisäksi esimerkiksi lukeminen ja hauteen lämpötilan tasaantuminen. Suora piirretään siksi pisteiden joukon keskeltä niin, että se kulkee epävarmuusvälien kautta, ei välttämättä jokaisen pisteen kautta.

```pysahdy
Suora piirretään pisteparven keskeltä. Pitääkö sen kulkea jokaisen pisteen kautta?
---
Ei. Sen pitää kulkea epävarmuuspalkkien kautta, ei välttämättä jokaisen pisteen, koska mittausepävarmuus saa pisteet hajoamaan.
```

<figure class="unit-photo"><img src="pics/fy3/liquid-nitrogen-dish.webp" alt="Käsi pitelee lasimaljaa, jossa on nestemäistä typpeä. Maljan ympäriltä valuu valkoista sumua tummaa taustaa vasten."><figcaption>Nestemäistä typpeä lasimaljassa tiedefestivaalilla vuonna 2025. Valkoinen sumu on kylmän typpihöyryn ympärille tiivistyneitä vesipisaroita.</figcaption></figure>

Suoraa jatketaan mittausalueen ulkopuolelle kohti kylmempää, kunnes paine on nolla. Tätä sanotaan ekstrapoloinniksi: tulos saadaan alueelta, jolla ei ole mitattu mitään. Mikromallin mukaan paine syntyy hiukkasten törmäyksistä seinään. Ideaalikaasun mallissa paine olisi nolla siinä lämpötilassa, jossa hiukkasten keskimääräinen liike-energia on pienimmillään. Lämpötila, jossa suora osuu nollapaineeseen, on kokeen antama arvio absoluuttiselle nollapisteelle. Se on vain arvio: todellinen kaasu nesteytyy jo ennen sitä, ja jatke on malli.

```pysahdy
Miksi lämpötila, jossa suora osuu nollapaineeseen, on vain arvio absoluuttisesta nollapisteestä?
---
Se saadaan ekstrapoloimalla alueelle, jolla ei ole mitattu mitään, ja todellinen kaasu nesteytyy jo ennen tuota pistettä. Jatke on malli.
```

## Kaava: Nollapaineen lämpötila
Mittausalueella kaasun paine on lämpötilan lineaarinen funktio:
```latex
p = p_0 + k\theta
```
missä $p$ on paine (kPa), $p_0$ suoran paine lämpötilassa $0\,{}^\circ\text{C}$ (kPa), $k$ suoran kulmakerroin (kPa/°C) ja $\theta$ lämpötila celsiusasteina. Kulmakerroin lasketaan kahdesta pisteestä, jotka luetaan piirretyltä suoralta kaukana toisistaan:
```latex
k = \frac{p_2 - p_1}{\theta_2 - \theta_1}
```
missä $(\theta_1, p_1)$ ja $(\theta_2, p_2)$ ovat suoran pisteitä. Nollapaine saadaan, kun $p = 0$. Silloin lämpötila on $\theta_0$, ja yhtälö ratkeaa:
```latex
\begin{aligned}
0 &= p_0 + k\theta_0 \\
\theta_0 &= -\frac{p_0}{k}
\end{aligned}
```
Sama tulos saadaan mistä tahansa suoran pisteestä $(\theta_1, p_1)$, kun yhtälöön $p = p_1 + k(\theta - \theta_1)$ sijoitetaan $p = 0$:
```latex
\theta_0 = \theta_1 - \frac{p_1}{k}
```

Epävarmuus arvioidaan piirtämällä kaksi ääriviivaa, jotka vielä kulkevat kaikkien epävarmuusvälien kautta: jyrkin ja loivin. Kummastakin lasketaan nollapaineen lämpötila, ja pienempi ja suurempi arvo antavat välin. Tulos ilmoitetaan keskikohdan ja puolen välin avulla:
```latex
\Delta\theta_0 = \frac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}
```
missä $\theta_{0,\text{max}}$ on suurempi (vähemmän negatiivinen) ja $\theta_{0,\text{min}}$ pienempi nollapaineen lämpötila. Tulos on muotoa $\theta_0 \pm \Delta\theta_0$. Väli on arvio, ei taattu raja: se ottaa huomioon pisteiden epävarmuuden mutta ei sitä, pysyykö riippuvuus suorana mittausalueen ulkopuolella.

<svg viewBox="0 0 600 368" role="img" aria-label="Kaasun paine lämpötilan funktiona koko lämpötila-alueella −300 °C … 100 °C. Mittauspisteet ovat vain alueella 10–100 °C. Paras suora ja sen katkoviivajatke ekstrapoloivat nollapaineeseen, joka on lämpötilassa θ₀ ≈ −276 °C. Jyrkin ja loivin ääriviiva osuvat p = 0 -akselille lämpötiloissa noin −259 °C ja −295 °C, mikä antaa epävarmuusvälin. Kuva on mittakaavassa; ±1 kPa:n virhejanat ovat pisteiden kokoisia." style="max-width:100%;font-size:24px">
<line x1="78.0" y1="270.0" x2="78.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="202.0" y1="270.0" x2="202.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="326.0" y1="270.0" x2="326.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="450.0" y1="270.0" x2="450.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="574.0" y1="270.0" x2="574.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="190.0" x2="574.0" y2="190.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="110.0" x2="574.0" y2="110.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="30.0" x2="574.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="270.0" x2="582.0" y2="270.0" stroke="#1f2933" stroke-width="3"/>
<line x1="78.0" y1="270.0" x2="78.0" y2="22.0" stroke="#1f2933" stroke-width="3"/>
<foreignObject x="43" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">${-}300$</div></foreignObject>
<foreignObject x="167" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">${-}200$</div></foreignObject>
<foreignObject x="291" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">${-}100$</div></foreignObject>
<foreignObject x="415" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$0$</div></foreignObject>
<foreignObject x="530" y="274" width="68" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$100$</div></foreignObject>
<foreignObject x="6" y="173" width="64" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$50$</div></foreignObject>
<foreignObject x="6" y="93" width="64" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$100$</div></foreignObject>
<foreignObject x="6" y="13" width="64" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$150$</div></foreignObject>
<foreignObject x="424" y="226" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\theta\ (^\circ\text{C})$</div></foreignObject>
<foreignObject x="86" y="0" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$p\ (\text{kPa})$</div></foreignObject>
<line x1="128.9" y1="270.0" x2="462.4" y2="103.6" stroke="#6b7480" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="84.0" y1="270.0" x2="462.4" y2="100.7" stroke="#6b7480" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="107.6" y1="270.0" x2="462.4" y2="102.1" stroke="#1f2933" stroke-width="3" stroke-dasharray="10 7"/>
<line x1="462.4" y1="102.1" x2="574.0" y2="49.3" stroke="#1f2933" stroke-width="4"/>
<circle cx="462.4" cy="102.0" r="4" fill="#1f2933"/>
<circle cx="481.0" cy="94.0" r="4" fill="#1f2933"/>
<circle cx="499.6" cy="84.4" r="4" fill="#1f2933"/>
<circle cx="518.2" cy="74.8" r="4" fill="#1f2933"/>
<circle cx="536.8" cy="66.8" r="4" fill="#1f2933"/>
<circle cx="555.4" cy="58.8" r="4" fill="#1f2933"/>
<circle cx="574.0" cy="49.2" r="4" fill="#1f2933"/>
<path d="M84.0,314.0 V322.0 H128.9 V314.0" fill="none" stroke="#c92a2a" stroke-width="3"/>
<circle cx="107.6" cy="270.0" r="6" fill="#c92a2a"/>
<foreignObject x="4" y="324" width="210" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\theta_0 \pm \Delta\theta_0$</div></foreignObject>
<foreignObject x="204" y="76" width="200" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{ekstrapolointi}$</div></foreignObject><line x1="264" y1="114" x2="264" y2="184" stroke="#1f2933" stroke-width="1.5"/><foreignObject x="300" y="6" width="152" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{mittausalue}$</div></foreignObject><path d="M462,48 V32 H574 V48" fill="none" stroke="#1f2933" stroke-width="2"/>
</svg>

Kuva on piirretty mittakaavassa. Ääriviivat kulkevat lähellä toisiaan mittausalueella mutta eroavat ekstrapoloitaessa, joten epävarmuus kasvaa jatkettaessa. Epävarmuutta pienentävät tarkempi painemittari, useampi mittauspiste ja leveämpi mittausalue. Kun tulos tunnetaan, kelvinasteikon nollapiste asetetaan siihen: lämpötila kelvineinä on $T = \theta - \theta_0$.

```pysahdy
Ääriviivat eroavat toisistaan, kun suoraa jatketaan. Mitä se tarkoittaa lämpötilan $\theta_0$ epävarmuudelle?
---
Mitä pidemmälle suoraa jatketaan, sitä suurempi lämpötilan $\theta_0$ epävarmuus on.
```

## Esimerkki
Esimerkkiaineistossa on suljetun pullon ilman paine seitsemässä lämpötilassa, kuten kaasulämpömittarilla mitattaisiin. Arvot on laskettu ideaalikaasumallista ja niihin on lisätty mittausepätarkkuutta vastaavaa hajontaa; ne eivät ole oikean mittauksen tuloksia. Paineen lukeman epävarmuudeksi on arvioitu $\pm 1\,\text{kPa}$.

| $\theta$ (°C) | $p$ (kPa) |
| --- | --- |
| 10 | 105 |
| 25 | 110 |
| 40 | 116 |
| 55 | 122 |
| 70 | 127 |
| 85 | 132 |
| 100 | 138 |

Määritä absoluuttinen nollapiste ekstrapoloimalla ja arvioi tuloksen epävarmuus. Pisteisiin sovitettu paras suora on kuvassa yllä; sen jyrkin ja loivin vaihtoehto, jotka vielä kulkevat kaikkien epävarmuusvälien kautta, ovat $p = 100{,}1\,\text{kPa} + 0{,}387\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ ja $p = 102{,}3\,\text{kPa} + 0{,}347\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$. Jyrkin koskettaa epävarmuusjanojen päitä lämpötiloissa $10\,{}^\circ\text{C}$ ja $85\,{}^\circ\text{C}$, loivin lämpötiloissa $25\,{}^\circ\text{C}$ ja $100\,{}^\circ\text{C}$.

<!-- vaihe -->

**Tunnetut ja kysytty.** Parhaalta suoralta luetaan kaksi pistettä kaukana toisistaan:

- $(\theta_1, p_1) = (0\,{}^\circ\text{C};\ 101{,}3\,\text{kPa})$ ja
- $(\theta_2, p_2) = (100\,{}^\circ\text{C};\ 138{,}0\,\text{kPa})$.

Lämpötila $0\,{}^\circ\text{C}$ on mittausalueen ulkopuolella, joten piste 1 luetaan suoran jatkeelta: se ei ole mittaus vaan jo vähän ekstrapolointia.

Ääriviivoilla on

- $p_0 = 100{,}1\,\text{kPa}$, $k = 0{,}387\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja
- $p_0 = 102{,}3\,\text{kPa}$, $k = 0{,}347\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$.

Kysytään nollapaineen lämpötilaa $\theta_0$ ja sen epävarmuutta $\Delta\theta_0$.

<!-- vaihe -->

**Periaate.** Pullo on suljettu ja jäykkä, joten kaasun ainemäärä ja tilavuus pysyvät vakioina ja paine on mittausalueella lämpötilan lineaarinen funktio $p = p_0 + k\theta$. Siksi suoraa voi jatkaa kohtaan, jossa $p = 0$.

Epävarmuus saadaan ääriviivoista: ne kulkevat kaikkien epävarmuusjanojen kautta, joten ne sopivat aineistoon yhtä hyvin kuin paras suora, ja niiden nollakohdat rajaavat välin, jolla todellinen nollapiste todennäköisesti on.

<!-- vaihe -->

**Kaava ratkaistuna.** Kulmakerroin, nollapaineen lämpötila (kun $p_0 = p_1$, koska piste 1 on lämpötilassa $0\,{}^\circ\text{C}$) ja epävarmuus välin puolikkaana:
```latex
\begin{aligned}
&k = \frac{p_2 - p_1}{\theta_2 - \theta_1} \\
&\theta_0 = -\frac{p_0}{k} \\
&\Delta\theta_0 \\
&= \frac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunnoksia ei tarvita: paineet ovat kilopascaleina, joten osamäärässä $p_0/k$ kPa supistuu ja jäljelle jää celsiusaste, jota kysytään.

Lämpötilaero $100\,{}^\circ\text{C} - 0\,{}^\circ\text{C} = 100\,{}^\circ\text{C}$ on sama kelvineinä, ja nollapaineen lämpötila ilmoitetaan celsiusasteina.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin kulmakerroin ja sitten nollapaineen lämpötila:
```latex
\begin{aligned}
&k = \frac{p_2 - p_1}{\theta_2 - \theta_1} \\
&= \frac{(138{,}0 - 101{,}3)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} \\
&= 0{,}367\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \\[6pt]
&\theta_0 = -\frac{p_0}{k} \\
&= -\frac{101{,}3\,\text{kPa}}{0{,}367\,\text{kPa}/{}^\circ\text{C}} \\
&= -276{,}02\,{}^\circ\text{C}
\end{aligned}
```
Ääriviivoille $\theta_{0,\text{max}} = -\tfrac{100{,}1}{0{,}387}\,{}^\circ\text{C} = -258{,}66\,{}^\circ\text{C}$ ja $\theta_{0,\text{min}} = -\tfrac{102{,}3}{0{,}347}\,{}^\circ\text{C} = -294{,}81\,{}^\circ\text{C}$, joten $\Delta\theta_0 = \tfrac{-258{,}66 - (-294{,}81)}{2}\,{}^\circ\text{C} = 18{,}08\,{}^\circ\text{C}$.

<!-- vaihe -->

**Tulos.** Absoluuttinen nollapiste on $\theta_0 = -276 \pm 18\,{}^\circ\text{C}$.

Epävarmuus ilmoitetaan kahdella merkitsevällä numerolla ($18{,}08 \approx 18$), koska ääriviivojen nollapisteet $-259\,{}^\circ\text{C}$ ja $-295\,{}^\circ\text{C}$ tunnetaan kolmella numerolla ja niiden erotus $36\,{}^\circ\text{C}$ vain kahdella.

Tulos pyöristetään samaan tarkkuuteen eli yhden asteen tarkkuuteen.

<!-- vaihe -->

**Järkevyys.** Hyväksytty arvo $-273{,}15\,{}^\circ\text{C}$ kuuluu välille $-294\,{}^\circ\text{C}\ldots -258\,{}^\circ\text{C}$, joten tulos sopii yhteen sen kanssa; poikkeama on noin $3\,{}^\circ\text{C}$ ja epävarmuus $18\,{}^\circ\text{C}$.

Arvio päässä: paine kasvaa noin $0{,}37\,\text{kPa}$ astetta kohti, joten $101\,\text{kPa}$ loppuu noin $101/0{,}37 \approx 270$ asteessa.

Epävarmuus on suuri, koska mittaus tehtiin yli $270\,{}^\circ\text{C}$:n päässä nollapaineesta ja pisteiden epävarmuus $1\,\text{kPa}$ on noin yksi prosentti lukemasta.

## Yleinen virhekäsitys
Moni ajattelee, että nollapiste on mitattu, koska se on kuvaajassa. Mitattuja ovat vain seitsemän pistettä välillä 10–$100\,{}^\circ\text{C}$; loppu on suoran jatketta, ja jatke on oletus siitä, että paine käyttäytyy samoin kylmemmässä. Toinen virhe on pitää tulosta epäonnistuneena, jos se ei ole täsmälleen $-273{,}15\,{}^\circ\text{C}$. Tulos $-276\,{}^\circ\text{C}$ poikkeaa hyväksytystä arvosta noin 3 astetta, kun epävarmuus on 18 astetta, eli se sopii yhteen arvon kanssa. Kolmas virhe on vetää suora kaikkien pisteiden kautta mutkitellen: pisteiden vaihtelu ylös ja alas johtuu mittausepävarmuudesta, ja suora kuuluu vetää pisteiden joukon keskeltä.

## Tiivistelmä
- Suljetussa jäykässä astiassa harvan kaasun paine on mittausalueella lineaarinen funktio lämpötilasta: $p = p_0 + k\theta$. Mittausaineisto muuttuu suoraksi piirtämällä $p$ lämpötilan funktiona ja vetämällä suora pisteiden joukon keskeltä.
- Mittausepävarmuus kuvaa mittaustulokseen liittyvää epävarmuutta, eikä se yleensä ole ehdoton suurin mahdollinen poikkeama oikeasta arvosta. Suoran ei tarvitse osua jokaiseen pisteeseen vaan kulkea epävarmuusvälien kautta.
- Ekstrapolointi jatkaa suoraa mittausalueen ulkopuolelle: nollapaineen lämpötila on $\theta_0 = -p_0/k$.
- Epävarmuus arvioidaan ääriviivoista: $\Delta\theta_0 = (\theta_{0,\text{max}} - \theta_{0,\text{min}})/2$. Tulos $\theta_0 \pm \Delta\theta_0$ sopii yhteen hyväksytyn arvon $-273{,}15\,{}^\circ\text{C}$ kanssa, jos se kuuluu väliin.
