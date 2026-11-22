# Kuuman veden jäähtyminen

> **Tutkimuskysymys:** Miten kuuman veden lämpötila muuttuu ajan funktiona, kun vesi jäähtyy huoneessa, ja kuinka hyvin Newtonin jäähtymislaki kuvaa jäähtymistä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on korkkialustan päällä lasiastia, jossa on kuumaa vettä. Vedestä nousee höyryä. Veteen on upotettu lämpötila-anturi, jonka johto kulkee pöydällä olevaan mittauslaitteeseen. Sivummalla pöydällä seisoo toinen lämpömittari huoneilmassa. Taustalla on ikkuna, ja pöydän reunalla on vedenkeitin." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-jaahtyminen-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Kahvikuppi, saunan kiuas ja kuumasta suihkusta tullut iho jäähtyvät kaikki kohti ympäristön lämpötilaa. Tässä tutkimuksessa mittaat, miten kuuman veden lämpötila muuttuu ajan kuluessa, etsit mittaustuloksiin sopivan matemaattisen mallin ja vertaat sitä Newtonin jäähtymislakiin. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten veden lämpötila muuttuu ajan funktiona sen jäähtyessä, millainen matemaattinen malli kuvaa mittaustuloksia, mitä Newtonin jäähtymislaki tarkoittaa ja kuinka hyvin sen ennuste vastaa mittauksiasi, sekä jäähtymistä kuvaava vakio $k$ tai puoliintumisaika epävarmuuksineen.

**Päätät itse** (osittain ohjattu ja itsenäinen työtapa): astian ja vesimäärän, veden alkulämpötilan, mittauksen keston ja mittausvälin, sen, miten ja missä mittaat veden ja huoneen lämpötilan, tavan, jolla testaat mallia kuvaajan avulla, sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa työtavassa sivu kiinnittää nämä valinnat puolestasi, osittain ohjatussa se antaa niihin tukea, ja itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, yhden tekijän vaikutus jäähtymiseen, kuuluu työhösi: suunnittele vertailu itse ja vertaa tuloksia epävarmuuksineen. Newtonin jäähtymislain kuvauksen löydät esimerkiksi fysiikan oppikirjoista ja korkeakoulujen fysiikan oppimateriaaleista hakusanalla Newtonin jäähtymislaki; kerro raportissa, mistä lähteestä lain otit.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Luonnostele, millainen on veden lämpötilan kuvaaja ajan funktiona. Jäähtyykö vesi joka minuutti yhtä monta astetta?
2. Mitä lämpötilaa kohti vesi jäähtyy, ja laskeeko sen lämpötila koskaan sen alle?
3. Millä tavoilla vesi luovuttaa energiaa ympäristöön? Mikä niistä voisi olla avoimessa astiassa merkittävin?
4. Jos laitat astiaan kannen, käärit sen eristeeseen tai otat kaksi kertaa enemmän vettä, miten jäähtyminen muuttuu?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Jäähtymisen nopeutta ei voi lukea suoraan mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitkä suureet mittaat, jotta saat selville, miten jäähtyminen etenee?
2. Miksi jäähtymistä tutkittaessa tarvitaan myös huoneen lämpötila?
3. Mitä pidät vakiona koko mittauksen ajan?

## Teoriaa lyhyesti

Kuuma vesi luovuttaa energiaa ympäristöön lämpönä, kunnes se on samassa lämpötilassa kuin ympäristö. Lämpöä siirtyy johtumalla astian seinien ja pohjan läpi, konvektiona eli ilman ja veden virtauksina sekä lämpösäteilynä. Avoimen astian pinnalta vettä myös haihtuu, ja haihtuminen sitoo energiaa. [[apua:fy3-12|Lämmön siirtymistavat]]

Lämpöä siirtyy sitä suuremmalla teholla, mitä suurempi on lämpötilaero kappaleen ja ympäristön välillä: esimerkiksi talon seinän läpi johtuva teho on suoraan verrannollinen sisä- ja ulkolämpötilan erotukseen. Kun vesi luovuttaa lämmön $Q$, sen lämpötila laskee yhtälön $Q = cm\Delta T$ mukaisesti. Mitä suuremmalla teholla lämpöä siirtyy, sitä nopeammin veden lämpötila siis laskee. [[apua:fy3-6|Aineen lämpeneminen ja jäähtyminen]]

**Newtonin jäähtymislaki** on kokeellinen malli, joka rakentuu näille periaatteille. Selvitä, mitä se tarkoittaa ja millä oletuksilla se pätee, ja testaa mittauksillasi, kuvaako se jäähtymistä.

::: tuki O OO
**Newtonin jäähtymislaki.** Laki olettaa, että veden luovuttama lämpöteho on suoraan verrannollinen lämpötilaeroon $T - T_\text{huone}$, missä $T$ on veden lämpötila ja $T_\text{huone}$ huoneen lämpötila. Silloin myös veden lämpötilan muutosnopeus on suoraan verrannollinen lämpötilaeroon: kun ero on puolet pienempi, vesi jäähtyy puolet hitaammin. Tästä seuraa, että lämpötilaero pienenee yhtä pitkissä aikaväleissä aina samassa suhteessa. Tällaista riippuvuutta kuvaa eksponenttifunktio:

```latex
T - T_\text{huone} = (T_0 - T_\text{huone})\cdot e^{-kt}
```

missä $T_0$ on veden lämpötila hetkellä $t = 0$, $k$ on jäähtymistä kuvaava vakio, jonka yksikkö on $\dfrac{1}{\text{min}}$ tai $\dfrac{1}{\text{s}}$, ja $e \approx 2{,}718$ on Neperin luku. Kun $t$ kasvaa, $e^{-kt}$ pienenee kohti nollaa, joten veden lämpötila lähestyy huoneen lämpötilaa mutta ei mallin mukaan laske sen alle. Mitä suurempi $k$, sitä nopeammin vesi jäähtyy.

Malli pätee vain, jos sen oletukset ovat voimassa: huoneen lämpötila pysyy vakiona, vesi on kauttaaltaan saman lämpöistä, astia lämpenee ja jäähtyy veden mukana ja lämpöteho on suoraan verrannollinen lämpötilaeroon. Viimeinen oletus on vain likimäärin tosi. Haihtuminen, lämpösäteily ja ilman luonnollinen konvektio kasvavat lämpötilaeron kasvaessa jyrkemmin kuin suoraan verrannollisesti, joten aivan kuumalla vedellä, varsinkin avoimessa astiassa, mittaukset voivat poiketa mallista.

<svg data-fig="model" viewBox="0 0 600 400" role="img" aria-label="Kuvaaja: veden lämpötila T ajan t funktiona Newtonin jäähtymislain mukaan. Lämpötila lähtee alkulämpötilasta T nolla ja laskee aluksi jyrkästi, sitten yhä loivemmin, ja lähestyy katkoviivalla merkittyä huoneen lämpötilaa T huone mutta ei laske sen alle. Kolme pystysuoraa janaa näyttää veden ja huoneen lämpötilaeron kolmena hetkenä, jotka ovat yhtä pitkän ajan t puoli päässä toisistaan: jana on joka kerta puolet edellisestä. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="340" x2="494" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,340 L493,346 L493,334 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="341" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="345.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="325.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <polyline points="90,284 480,284" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,88 93,91.5 96.5,95.5 100,99 103,102.5 106,106 109.5,109.5 113,112.5 116,116 119,119 122.5,122 126,125.5 129,128.5 132,131 135.5,134 139,137 142,140 145,142.5 148.5,145 152,148 155,150.5 158,153 161.5,155.5 165,158 168,160.5 171,162.5 174.5,165 178,167 181,169.5 184,171.5 187.5,173.5 191,176 194,178 197,180 200.5,182 204,184 207,185.5 210,187.5 213.5,189.5 217,191 220,193 223,194.5 226.5,196.5 230,198 233,199.5 236,201.5 239.5,203 243,204.5 246,206 249,207.5 252.5,209 256,210.5 259,211.5 262,213 265.5,214.5 269,215.5 272,217 275,218.5 278.5,219.5 282,220.5 285,222 288,223 291.5,224.5 295,225.5 298,226.5 301,227.5 304.5,228.5 308,229.5 311,231 314,232 317.5,233 321,233.5 324,234.5 327,235.5 330.5,236.5 334,237.5 337,238.5 340,239 343.5,240 347,241 350,241.5 353,242.5 356.5,243.5 360,244 363,245 366,245.5 369.5,246.5 373,247 376,247.5 379,248.5 382.5,249 386,249.5 389,250.5 392,251 395.5,251.5 399,252.5 402,253 405,253.5 408.5,254 412,254.5 415,255 418,255.5 421.5,256.5 425,257 428,257.5 431,258 434.5,258.5 438,259 441,259.5 444.5,259.5 447.5,260 451,260.5 454,261 457,261.5 460.5,262 464,262.5 467,263 470,263 473.5,263.5 476.5,264 480,264.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="397" y="291.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$T_\text{huone}$</div></foreignObject>
  <line x1="83" y1="88" x2="90" y2="88" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="73.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$T_0$</div></foreignObject>
  <line x1="121" y1="284" x2="121" y2="121" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <line x1="238.5" y1="284" x2="238.5" y2="202.5" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <line x1="356.5" y1="284" x2="356.5" y2="243" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <line x1="125" y1="266" x2="234.5" y2="266" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="151" y="233.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$t_{1/2}$</div></foreignObject>
  <line x1="242.5" y1="266" x2="352.5" y2="266" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="268.5" y="233.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$t_{1/2}$</div></foreignObject>
  <foreignObject x="129" y="82.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{lämpötilaero}$</div></foreignObject>
  <foreignObject x="246.5" y="164" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{puolet}$</div></foreignObject>
  <foreignObject x="364.5" y="204.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{neljännes}$</div></foreignObject>
</svg>

**Mallin tunnusmerkki ilman logaritmeja.** Mallin mukaan lämpötilaero puolittuu aina yhtä pitkässä ajassa $t_{1/2}$, jota kutsutaan puoliintumisajaksi, aloitetaan tarkastelu mistä hetkestä tahansa. Tämän voit testata suoraan lämpötilan kuvaajasta.

**Mallin muuttaminen suoraksi.** Kun yhtälön molemmista puolista otetaan luonnollinen logaritmi $\ln$, saadaan

```latex
\begin{aligned}\ln(T - T_\text{huone}) &= \ln(T_0 - T_\text{huone}) \\ &\quad - k\cdot t\end{aligned}
```

joten kuvaaja, jonka pystyakselilla on $\ln(T - T_\text{huone})$ ja vaaka-akselilla aika $t$, on mallin mukaan laskeva suora, jonka kulmakerroin on $-k$. Logaritmi otetaan lämpötilaeron lukuarvosta celsiusasteina; lämpötilaero on sama celsiusasteina ja kelvineinä. Puoliintumisaika ja vakio $k$ liittyvät toisiinsa yhtälöllä $t_{1/2} = \dfrac{\ln 2}{k} \approx \dfrac{0{,}69}{k}$. Jos luonnollinen logaritmi ei ole vielä tuttu matematiikasta, käytä puoliintumisaikaa tai ohjelman eksponenttisovitusta.

<svg data-fig="linear" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja: lämpötilaeron T miinus T huone luonnollinen logaritmi ajan t funktiona Newtonin jäähtymislain mukaan. Kuvaaja on laskeva suora, joka alkaa pystyakselilta kohdasta luonnollinen logaritmi T nolla miinus T huone ja jonka kulmakerroin on miinus k. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="300" x2="484" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,300 L483,306 L483,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\ln(T - T_\text{huone})$</div></foreignObject>
  <polyline points="90,93.5 451,252" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="90" cy="93.5" r="5" fill="#6b7480" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="109" y="45" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\ln(T_0 - T_\text{huone})$</div></foreignObject>
  <foreignObject x="295" y="134.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } {-k}$</div></foreignObject>
</svg>
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä mittaat, miten ja kuinka pitkään, ja mitä pidät vakiona.

::: tuki O
**Ohjattu.** Mittaat veden lämpötilaa $T$ ajan $t$ funktiona ja huoneen lämpötilaa $T_\text{huone}$ mittauksen alussa ja lopussa. Käytä noin $1\,\text{dl}$ vettä lasiastiassa, jonka alla on eristävä alusta, ja aloita, kun veden lämpötila on noin $60\,{}^\circ\text{C}$. Tallenna lämpötila anturilla esimerkiksi $10\,\text{s}$ välein ja jatka mittausta, kunnes veden ja huoneen lämpötilaero on pudonnut noin neljäsosaan alkuperäisestä. Jos käytät lämpömittaria ja kelloa, lue lämpötila minuutin välein. Pidä astia, vesimäärä ja paikka samoina koko mittauksen ajan, äläkä siirrä astiaa.
:::

::: tuki OO
**Osittain ohjattu.** Mitattavat suureet ovat veden lämpötila ajan funktiona ja huoneen lämpötila. Päätä itse astia, vesimäärä, alkulämpötila, mittauksen kesto ja mittausväli. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
<svg data-fig="setup" viewBox="0 0 600 380" role="img" aria-label="Kaaviokuva. Lasiastiassa on kuumaa vettä eristävän alustan päällä. Lämpötila-anturin kärki on veden keskellä, irti astian pohjasta ja seinistä, ja se mittaa veden lämpötilan T. Anturin johto kulkee mittauslaitteeseen. Sivussa, irti astiasta, on toinen lämpömittari, joka mittaa huoneen lämpötilan T huone." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-jaahtyminen-setup.webp" x="0" y="-1.2" width="600" height="386.2" preserveAspectRatio="none"/>
  <foreignObject x="306" y="240.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="336" y="83.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{mittauslaite}$</div></foreignObject>
  <foreignObject x="387" y="215.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$T_\text{huone}$</div></foreignObject>
  <foreignObject x="118.5" y="341.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{eristävä alusta}$</div></foreignObject>
</svg>

Mieti ainakin näitä:

- Mihin kohtaan veden lämpötila-anturi kannattaa sijoittaa, ja miksi se ei saa koskea astian pohjaa tai seinää?
- Missä huoneen lämpötila mitataan, jotta kuuma astia ei lämmitä mittaria? Muuttuuko huoneen lämpötila mittauksen aikana?
- Kuinka kauan mittauksen pitää kestää, jotta voit testata mallia? Kuinka paljon lämpötilaeron pitää pienentyä, jotta näet, hidastuuko jäähtyminen, ja jotta voit verrata jäähtymistä mittauksen alussa ja lopussa?
- Sekoitatko vettä mittauksen aikana? Jos sekoitat, tee se joka kerta samalla tavalla.
:::

::: tuki O
**Vihje anturiin.** Tarkista ennen mittausta, että molemmat mittarit näyttävät samassa huoneilmassa saman lukeman. Jos lukemat eroavat, kirjaa ero ylös: se vaikuttaa lämpötilaeroon $T - T_\text{huone}$ juuri silloin, kun ero on pieni.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon tai tallenna ne ohjelmaan heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa. Jos anturi tallentaa satoja lukemia, tee lasketut sarakkeet ohjelmassa ja liitä raporttiin taulukosta ote.

| $t\,(\text{min})$ | $T\,({}^\circ\text{C})$ | $T - T_\text{huone}\,({}^\circ\text{C})$ | $\ln(T - T_\text{huone})$ |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

Kaada kuuma vesi astiaan, aseta anturi paikalleen ja odota hetki, että anturi ja astia ovat lämmenneet veden lämpöisiksi, ennen kuin aloitat ajanoton. Aivan ensimmäisten lukemien aikana lämpötila laskee nopeasti myös siksi, että vesi lämmittää astiaa ja anturia.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti mittarit näyttävät lämpötilan, ja mittaa huoneen lämpötila sekä mittauksen alussa että lopussa. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä mittaustuloksista veden lämpötila ajan funktiona. Merkitse akseleille suureet ja yksiköt, ja merkitse kuvaajaan myös huoneen lämpötila. Testaa sitten, sopiiko Newtonin jäähtymislaki mittaustuloksiisi, ja määritä jäähtymistä kuvaava vakio. [[apua:fy1-4|Kuvaajan laatiminen ja suoran sovittaminen]]

::: tuki O
Tee kaksi kuvaajaa. Ensimmäisessä on pystyakselilla $T$ ja vaaka-akselilla $t$. Laske toiseen kuvaajaan sarake $\ln(T - T_\text{huone})$ ja piirrä se ajan $t$ funktiona. Sovita toiseen kuvaajaan suora: kulmakerroin on $-k$. Jos logaritmi ei ole tuttu, lue ensimmäisestä kuvaajasta, kuinka kauan kestää, että lämpötilaero puolittuu, ja toista lukeminen kolmesta eri aloituskohdasta.
:::

Vastaa:

1. Onko lämpötilan kuvaaja suora vai kaareva? Missä vaiheessa jäähtyminen on nopeinta?
2. Kuvaako malli mittauksiasi koko mittausalueella? Jos ei, millä aikavälillä tai millä lämpötiloilla mittaukset poikkeavat mallista, ja mihin suuntaan?
3. Mikä on jäähtymistä kuvaavan vakion $k$ tai puoliintumisajan arvo ja yksikkö?

::: tuki O OO
**Kolme tapaa testata mallia.** Osittain ohjatussa työtavassa valitse niistä itse ja perustele valintasi.

- **Puoliintumisaika.** Lue lämpötilan kuvaajasta, kuinka kauan lämpötilaeron puolittuminen kestää, eri aloituskohdista. Jos ajat ovat mittausepävarmuuden rajoissa samat, malli on sopusoinnussa mittausten kanssa.
- **Linearisointi.** Kuvaaja $\ln(T - T_\text{huone})$ ajan funktiona on mallin mukaan suora. Suoruuden näkee silmällä helpommin kuin sen, onko käyrä juuri eksponenttifunktio. Kulmakertoimesta saat vakion $k$.
- **Eksponenttisovitus.** Monilla ohjelmilla voi sovittaa mittauspisteisiin suoraan eksponenttifunktion. Sovita lämpötilaan $T$ funktio, jossa on vakiotermi, muotoa $A\cdot e^{-Bt} + C$, tai sovita funktio $A\cdot e^{-Bt}$ lämpötilaeroon $T - T_\text{huone}$. Pelkkä $A\cdot e^{-Bt}$ lämpötilaan $T$ sovitettuna antaa väärän vakion, koska sen käyrä lähestyy lämpötilaa $0\,{}^\circ\text{C}$ eikä huoneen lämpötilaa. Selvitä, mitä sovitettavan funktion vakiot tarkoittavat, ja vertaa niitä mallin yhtälön suureisiin. Tarkista, osuvatko pisteet käyrälle koko alueella vai poikkeavatko ne järjestelmällisesti jossain kohdassa.

Jos $\ln$-kuvaaja on alussa suora mutta kaartuu lopussa, tarkista ensin huoneen lämpötila: pienikin virhe lukemassa $T_\text{huone}$ muuttaa lämpötilaeroa suhteellisesti eniten silloin, kun ero on pieni. Pisteet, joissa lämpötilaero on mittausepävarmuuden suuruinen, eivät kerro mallista enää mitään: jätä ne pois sovituksesta ja kerro se raportissa.
:::

Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita jäähtymistä kuvaava vakio epävarmuuksineen ja yksiköineen ja perustele, miten arvioit epävarmuuden.

::: tuki O OO
Ilmoita tulos muodossa arvo $\pm$ epävarmuus ja yksikkö, esimerkiksi vakiolle $k$ yksikössä $\dfrac{1}{\text{min}}$ ja puoliintumisajalle $\bar{t}_{1/2} \pm \Delta t_{1/2}$ minuutteina. Epävarmuuden voit arvioida esimerkiksi näin:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen tai sovitetun vakion keskivirheen. Käytä sitä epävarmuutena $\Delta k$.
- **Jyrkin ja loivin suora.** Piirrä $\ln$-kuvaajaan jyrkin ja loivin suora, jotka vielä sopivat pisteisiin. Määritä niiden kulmakertoimien itseisarvot $k_\text{max}$ ja $k_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta k = \dfrac{k_\text{max} - k_\text{min}}{2}$.
- **Toistetut puoliintumisajat.** Laske eri aloituskohdista luettujen puoliintumisaikojen keskiarvo $\bar{t}_{1/2}$ ja arvioi epävarmuus vaihteluvälin puolikkaana.

Lämpötilaero on kahden lukeman erotus, joten sen epävarmuus on lukemien epävarmuuksien summa: $\Delta(T - T_\text{huone}) = \Delta T + \Delta T_\text{huone}$. Kun lämpötilaero on pieni, sama epävarmuus on siitä suuri osa, joten mittauksen loppupään pisteet ovat suhteellisesti epätarkimpia. Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä tekijät vaikuttivat jäähtymisnopeuteen ja mittaustulosten luotettavuuteen? Pysyivätkö mittausolosuhteet samoina koko mittauksen ajan? Olivatko epävarmuuden lähteet satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Miten veden lämpötila muuttuu ajan funktiona? Kuvaako Newtonin jäähtymislaki mittauksiasi hyvin, ja missä mallin ja mittausten välillä näkyy poikkeamia? Mistä poikkeamat voivat johtua? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 2 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** Newtonin jäähtymislaki omin sanoin, sen oletukset ja se, miten mallia testataan kuvaajan avulla.
- **Koejärjestely ja menetelmä:** astia, vesimäärä, alkulämpötila, anturin paikka, miten ja missä mittasit huoneen lämpötilan sekä mitä pidit vakiona.
- **Mittaustulokset:** alkuperäiset lukemat ja niiden oikealla puolella lasketut sarakkeet; pitkästä datasta ote.
- **Tulos:** jäähtymistä kuvaava vakio tai puoliintumisaika epävarmuuksineen oikein pyöristettynä ja kuvaaja, josta se määritettiin.
- **Luotettavuus:** missä malli ja mittaukset poikkeavat toisistaan, konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: yhden tekijän vaikutus jäähtymiseen

Tutki, miten yksi tekijä vaikuttaa jäähtymiseen. Voit valita esimerkiksi astian materiaalin, eristeen astian ympärillä, kannen, vesimäärän tai veden pinta-alan, kun vesimäärä pysyy samana. Muuta vain valitsemaasi tekijää ja pidä kaikki muu samana, myös alkulämpötila. Määritä jäähtymistä kuvaava vakio kummassakin tilanteessa ja vertaa tuloksia epävarmuuksineen: mahtuvatko ne toistensa epävarmuusväleihin? Päällekkäiset välit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että tekijällä ei olisi vaikutusta. Kirjaa ennen mittausta ennuste ja perustelu, ja vertaa tulosta siihen.

::: tuki O OO
**Vihjeitä.** Jos sinulla on kaksi anturia, voit mitata kumpaakin tilannetta yhtä aikaa samassa huoneessa, jolloin huoneen lämpötila on molemmissa sama. Aloita molemmat mittaukset samasta lämpötilasta, koska malli ei välttämättä päde yhtä hyvin aivan kuumalla vedellä. Mieti ennen mittausta, vaikuttaako valitsemasi tekijä siihen, kuinka suurella teholla lämpöä siirtyy, vai siihen, kuinka paljon energiaa veden lämpötilan muuttamiseen tarvitaan, vai kumpaankin.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
