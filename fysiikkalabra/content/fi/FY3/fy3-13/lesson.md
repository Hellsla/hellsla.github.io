# Absoluuttisen nollapisteen määrittäminen

> **Miksi** alin mahdollinen lämpötila voidaan määrittää koulun laboratoriossa, vaikka lämpömittari ei ulotu lähellekään sitä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratoriopöydällä on kolme astiaa: jäävesi, huoneenlämpöinen vesi ja kuumalla levyllä kiehuva vesi. Keskimmäisessä hauteessa on suljettu lasipullo, joka on letkulla yhdistetty painemittariin." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy313h-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#ffffff"/>
  <line x1="0" y1="0" x2="0" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="80" y1="0" x2="80" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="0" x2="160" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="0" x2="240" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320" y1="0" x2="320" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="0" x2="400" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="480" y1="0" x2="480" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="560" y1="0" x2="560" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="640" y1="0" x2="640" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="720" y1="0" x2="720" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="0" x2="800" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="880" y1="0" x2="880" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="0" x2="960" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1040" y1="0" x2="1040" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1120" y1="0" x2="1120" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1200" y1="0" x2="1200" y2="420" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="0" x2="1200" y2="0" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="80" x2="1200" y2="80" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="160" x2="1200" y2="160" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="240" x2="1200" y2="240" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="320" x2="1200" y2="320" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="400" x2="1200" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="0" y="420" width="1200" height="26" fill="#c9c2b2" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="446" width="1200" height="154" fill="#e3dccb"/>
  <path d="M80,250 V410 Q80,420 90,420 H270 Q280,420 280,410 V250" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M83,290 H277 V410 Q277,417 270,417 H90 Q83,417 83,410 Z" fill="url(#fy313h-water)" stroke-linejoin="round"/>
  <path d="M80,250 V410 Q80,420 90,420 H270 Q280,420 280,410 V250" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="110" y="300" width="36" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="160" y="296" width="36" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="210" y="304" width="36" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="140" y="330" width="36" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="190" y="336" width="36" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <path d="M450,220 V410 Q450,420 460,420 H740 Q750,420 750,410 V220" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M453,260 H747 V410 Q747,417 740,417 H460 Q453,417 453,410 Z" fill="url(#fy313h-water)" stroke-linejoin="round"/>
  <path d="M450,220 V410 Q450,420 460,420 H740 Q750,420 750,410 V220" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M600,250 V150" fill="none" stroke="#1f2933" stroke-width="14" stroke-linejoin="round"/>
  <path d="M600,250 V150" fill="none" stroke="#eef5f9" stroke-width="8" stroke-linejoin="round"/>
  <circle cx="600" cy="320" r="70" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <circle cx="600" cy="320" r="70" fill="none" stroke="#a9d1f0" stroke-width="2"/>
  <path d="M600,150 Q600,96 680,96 H790" fill="none" stroke="#1f2933" stroke-width="10" stroke-linejoin="round"/>
  <circle cx="860" cy="120" r="76" fill="#ffffff" stroke="#1f2933" stroke-width="4"/>
  <line x1="815.5" y1="157.5" x2="808" y2="163.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="803.5" y1="134" x2="794" y2="136.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="803.5" y1="108" x2="793.5" y2="106" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="814.5" y1="84.5" x2="806.5" y2="78" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="834.5" y1="68" x2="830" y2="59" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="860" y1="62" x2="860" y2="52" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="885.5" y1="68" x2="890" y2="59" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="905.5" y1="84.5" x2="913.5" y2="78" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="916.5" y1="108" x2="926.5" y2="106" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="916.5" y1="134" x2="926" y2="136.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="904.5" y1="157.5" x2="912" y2="163.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M860,120 L900,72" fill="none" stroke="#1f2933" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="860" cy="120" r="8" fill="#1f2933"/>
  <rect x="780" y="120" width="12" height="300" fill="#6c757d"/>
  <rect x="740" y="408" width="92" height="12" rx="3" fill="#6c757d"/>
  <rect x="930" y="400" width="220" height="20" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <ellipse cx="1040" cy="400" rx="120" ry="10" fill="#c92a2a" fill-opacity="0.8"/>
  <path d="M960,230 V380 Q960,392 972,392 H1108 Q1120,392 1120,380 V230" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M963,270 H1117 V380 Q1117,389 1108,389 H972 Q963,389 963,380 Z" fill="url(#fy313h-water)" stroke-linejoin="round"/>
  <circle cx="1002.5" cy="301" r="8.59979" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="1082.5" cy="299.5" r="5.42734" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="1045" cy="371.5" r="6.07636" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="979.5" cy="338.5" r="6.54663" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="989" cy="361" r="4.53706" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="1009.5" cy="324" r="6.95633" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="1101.5" cy="357" r="5.6087" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="1030.5" cy="295" r="6.65335" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="975.5" cy="365.5" r="5.99641" fill="#ffffff" stroke="#2f74b5" stroke-width="1.5"/>
  <path d="M960,230 V380 Q960,392 972,392 H1108 Q1120,392 1120,380 V230" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1000,224 c14,-24 -14,-40 0,-70" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M1000,224 c14,-24 -14,-40 0,-70" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1060,224 c14,-24 -14,-40 0,-70" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M1060,224 c14,-24 -14,-40 0,-70" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

## Ydinajatus
Suljetussa jäykässä astiassa kaasun tilavuus ja ainemäärä eivät muutu, joten paine riippuu vain lämpötilasta. Kaasulämpömittarissa lasipullo on vesihauteessa. Hauteen lämpötila $\theta$ luetaan lämpömittarista ja kaasun paine $p$ painemittarista, kun haude lämpenee.

<svg viewBox="0 0 600 372" role="img" aria-label="Kaasulämpömittari: suljettu lasipullo, jossa on ilmaa, on vesihauteessa, jota lämmitetään. Pullon kaasun tilavuus ei muutu. Vesihauteen lämpötila luetaan lämpömittarista ja kaasun paine painemittarista. Kuva on kaavio eikä mittakaavassa." style="max-width:100%;font-size:24px">
<defs><linearGradient id="fy313-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy313-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
<path d="M60,140 V296 Q60,312 76,312 H284 Q300,312 300,296 V140 Z" fill="#eef5f9"/>
<path d="M62,170 Q90,162 118,170 T174,170 T230,170 T286,170 L298,170 V296 Q298,310 284,310 H76 Q62,310 62,296 Z" fill="url(#fy313-water)"/>
<path d="M64,170 Q90,163 118,170 T174,170 T230,170 T296,170" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-opacity="0.8"/>
<path d="M60,140 V296 Q60,312 76,312 H284 Q300,312 300,296 V140" fill="none" stroke="#1f2933" stroke-width="3"/>
<rect x="192" y="60" width="246" height="16" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
<path d="M192,76 V196.6 A50,50 0 1 0 208,196.6 V76" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
<rect x="194" y="73" width="12" height="6" fill="#eef5f9"/>
<circle cx="176" cy="236" r="4" fill="#6b7480"/>
<circle cx="200" cy="224" r="4" fill="#6b7480"/>
<circle cx="222" cy="240" r="4" fill="#6b7480"/>
<circle cx="188" cy="262" r="4" fill="#6b7480"/>
<circle cx="214" cy="270" r="4" fill="#6b7480"/>
<circle cx="168" cy="274" r="4" fill="#6b7480"/>
<circle cx="238" cy="262" r="4" fill="#6b7480"/>
<circle cx="200" cy="248" r="4" fill="#6b7480"/>
<circle cx="230" cy="286" r="4" fill="#6b7480"/>
<circle cx="184" cy="286" r="4" fill="#6b7480"/>
<line x1="176" y1="236" x2="164" y2="242" stroke="#6b7480" stroke-width="2"/>
<line x1="222" y1="240" x2="234" y2="232" stroke="#6b7480" stroke-width="2"/>
<line x1="214" y1="270" x2="224" y2="280" stroke="#6b7480" stroke-width="2"/>
<line x1="168" y1="274" x2="158" y2="266" stroke="#6b7480" stroke-width="2"/>
<line x1="200" y1="224" x2="204" y2="212" stroke="#6b7480" stroke-width="2"/>
<rect x="100" y="122" width="10" height="158" rx="5" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
<g stroke="#6b7480" stroke-width="1.5"><line x1="110" y1="140" x2="116" y2="140"/><line x1="110" y1="156" x2="116" y2="156"/><line x1="110" y1="172" x2="116" y2="172"/><line x1="110" y1="188" x2="116" y2="188"/><line x1="110" y1="204" x2="116" y2="204"/><line x1="110" y1="220" x2="116" y2="220"/><line x1="110" y1="236" x2="116" y2="236"/><line x1="110" y1="252" x2="116" y2="252"/><line x1="110" y1="268" x2="116" y2="268"/></g>
<rect x="103" y="196" width="4" height="86" fill="#c92a2a"/><circle cx="105" cy="288" r="11" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
<foreignObject x="75" y="84" width="60" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\theta$</div></foreignObject>
<circle cx="490" cy="68" r="52" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
<line x1="457.5" y1="100.5" x2="464.5" y2="93.5" stroke="#6b7480" stroke-width="2.5"/>
<line x1="445.6" y1="79.9" x2="455.2" y2="77.3" stroke="#6b7480" stroke-width="2.5"/>
<line x1="445.6" y1="56.1" x2="455.2" y2="58.7" stroke="#6b7480" stroke-width="2.5"/>
<line x1="457.5" y1="35.5" x2="464.5" y2="42.5" stroke="#6b7480" stroke-width="2.5"/>
<line x1="478.1" y1="23.6" x2="480.7" y2="33.2" stroke="#6b7480" stroke-width="2.5"/>
<line x1="501.9" y1="23.6" x2="499.3" y2="33.2" stroke="#6b7480" stroke-width="2.5"/>
<line x1="522.5" y1="35.5" x2="515.5" y2="42.5" stroke="#6b7480" stroke-width="2.5"/>
<line x1="534.4" y1="56.1" x2="524.8" y2="58.7" stroke="#6b7480" stroke-width="2.5"/>
<line x1="534.4" y1="79.9" x2="524.8" y2="77.3" stroke="#6b7480" stroke-width="2.5"/>
<line x1="522.5" y1="100.5" x2="515.5" y2="93.5" stroke="#6b7480" stroke-width="2.5"/>
<line x1="490" y1="68" x2="515.7" y2="37.4" stroke="#1f2933" stroke-width="3.5" stroke-linecap="round"/><circle cx="490" cy="68" r="5" fill="#1f2933"/>
<foreignObject x="460" y="126" width="60" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$p$</div></foreignObject>
<foreignObject x="380" y="166" width="220" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{painemittari}$</div></foreignObject>
<rect x="60" y="316" width="240" height="14" rx="3" fill="#6c757d"/>
<path d="M105,362 V348 H98 L110,334 L122,348 H115 V362 Z" fill="url(#fy313-heat)"/>
<path d="M175,362 V348 H168 L180,334 L192,348 H185 V362 Z" fill="url(#fy313-heat)"/>
<path d="M245,362 V348 H238 L250,334 L262,348 H255 V362 Z" fill="url(#fy313-heat)"/>
<foreignObject x="316" y="334" width="50" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$Q$</div></foreignObject>
<foreignObject x="320" y="206" width="160" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{vesihaude}$</div></foreignObject>
<line x1="316" y1="226" x2="272" y2="226" stroke="#1f2933" stroke-width="2"/>
<foreignObject x="320" y="250" width="270" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{ilma},\ V=\text{vakio}$</div></foreignObject>
<line x1="316" y1="270" x2="254" y2="270" stroke="#1f2933" stroke-width="2"/>
</svg>

Kun mittaustulokset piirretään kuvaajaan, pisteet asettuvat lähes suoralle: paine kasvaa lähes yhtä paljon jokaista celsiusastetta kohti. Todellisissa mittaussarjoissa pisteet eivät silti yleensä ole täsmälleen samalla suoralla mittausepävarmuuden vuoksi. Mittausepävarmuus kuvaa mittaustulokseen liittyvää epävarmuutta. Se ei yleensä tarkoita ehdotonta suurinta mahdollista poikkeamaa oikeasta arvosta. Tässä paineen lukeman epävarmuudeksi on arvioitu $\pm 1\,\text{kPa}$. Valmistajan mittarille ilmoittama virheraja on eri asia: se on laitteen ominaisuus, ja mittauksen epävarmuuteen vaikuttavat lisäksi esimerkiksi lukeminen ja hauteen lämpötilan tasaantuminen. Suora piirretään siksi pisteiden joukon keskeltä niin, että se kulkee epävarmuusvälien kautta, ei välttämättä jokaisen pisteen kautta.

Suoraa jatketaan mittausalueen ulkopuolelle kohti kylmempää, kunnes paine on nolla. Tätä sanotaan ekstrapoloinniksi: tulos saadaan alueelta, jolla ei ole mitattu mitään. Mikromallin mukaan paine syntyy hiukkasten törmäyksistä seinään. Ideaalikaasun mallissa paine olisi nolla siinä lämpötilassa, jossa hiukkasten keskimääräinen liike-energia on pienimmillään. Lämpötila, jossa suora osuu nollapaineeseen, on kokeen antama arvio absoluuttiselle nollapisteelle. Se on vain arvio: todellinen kaasu nesteytyy jo ennen sitä, ja jatke on malli.

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

## Esimerkki
Esimerkkiaineistossa on suljetun pullon ilman paine seitsemässä lämpötilassa, kuten kaasulämpömittarilla mitattaisiin. Arvot on laskettu ideaalikaasumallista ja niihin on lisätty mittausepätarkkuutta vastaavaa hajontaa; ne eivät ole oikean mittauksen tuloksia. Paineen lukeman epävarmuudeksi on arvioitu $\pm 1\,\text{kPa}$.

| θ (°C) | p (kPa) |
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

**Tunnetut ja kysytty.** Parhaalta suoralta luetaan kaksi pistettä kaukana toisistaan: $(\theta_1, p_1) = (0\,{}^\circ\text{C};\ 101{,}3\,\text{kPa})$ ja $(\theta_2, p_2) = (100\,{}^\circ\text{C};\ 138{,}0\,\text{kPa})$. Lämpötila $0\,{}^\circ\text{C}$ on mittausalueen ulkopuolella, joten piste 1 luetaan suoran jatkeelta: se ei ole mittaus vaan jo vähän ekstrapolointia. Ääriviivoilla on $p_0 = 100{,}1\,\text{kPa}$, $k = 0{,}387\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ ja $p_0 = 102{,}3\,\text{kPa}$, $k = 0{,}347\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$. Kysytään nollapaineen lämpötilaa $\theta_0$ ja sen epävarmuutta $\Delta\theta_0$.

<!-- vaihe -->

**Periaate.** Pullo on suljettu ja jäykkä, joten kaasun ainemäärä ja tilavuus pysyvät vakioina ja paine on mittausalueella lämpötilan lineaarinen funktio $p = p_0 + k\theta$. Siksi suoraa voi jatkaa kohtaan, jossa $p = 0$. Epävarmuus saadaan ääriviivoista: ne kulkevat kaikkien epävarmuusjanojen kautta, joten ne sopivat aineistoon yhtä hyvin kuin paras suora, ja niiden nollakohdat rajaavat välin, jolla todellinen nollapiste todennäköisesti on.

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

**Yksikkömuunnokset.** Muunnoksia ei tarvita: paineet ovat kilopascaleina, joten osamäärässä $p_0/k$ kPa supistuu ja jäljelle jää celsiusaste, jota kysytään. Lämpötilaero $100\,{}^\circ\text{C} - 0\,{}^\circ\text{C} = 100\,{}^\circ\text{C}$ on sama kelvineinä, ja nollapaineen lämpötila ilmoitetaan celsiusasteina.

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

**Tulos.** Absoluuttinen nollapiste on $\theta_0 = -276 \pm 18\,{}^\circ\text{C}$. Epävarmuus ilmoitetaan kahdella merkitsevällä numerolla ($18{,}08 \approx 18$), koska ääriviivojen nollapisteet $-259\,{}^\circ\text{C}$ ja $-295\,{}^\circ\text{C}$ tunnetaan kolmella numerolla ja niiden erotus $36\,{}^\circ\text{C}$ vain kahdella. Tulos pyöristetään samaan tarkkuuteen eli yhden asteen tarkkuuteen.

<!-- vaihe -->

**Järkevyys.** Hyväksytty arvo $-273{,}15\,{}^\circ\text{C}$ kuuluu välille $-294\,{}^\circ\text{C}\ldots -258\,{}^\circ\text{C}$, joten tulos sopii yhteen sen kanssa; poikkeama on noin $3\,{}^\circ\text{C}$ ja epävarmuus $18\,{}^\circ\text{C}$. Arvio päässä: paine kasvaa noin $0{,}37\,\text{kPa}$ astetta kohti, joten $101\,\text{kPa}$ loppuu noin $101/0{,}37 \approx 270$ asteessa. Epävarmuus on suuri, koska mittaus tehtiin yli $270\,{}^\circ\text{C}$:n päässä nollapaineesta ja pisteiden epävarmuus $1\,\text{kPa}$ on noin yksi prosentti lukemasta.

## Yleinen virhekäsitys
Moni ajattelee, että nollapiste on mitattu, koska se on kuvaajassa. Mitattuja ovat vain seitsemän pistettä välillä 10–$100\,{}^\circ\text{C}$; loppu on suoran jatketta, ja jatke on oletus siitä, että paine käyttäytyy samoin kylmemmässä. Toinen virhe on pitää tulosta epäonnistuneena, jos se ei ole täsmälleen $-273{,}15\,{}^\circ\text{C}$. Tulos $-276\,{}^\circ\text{C}$ poikkeaa hyväksytystä arvosta noin 3 astetta, kun epävarmuus on 18 astetta, eli se sopii yhteen arvon kanssa. Kolmas virhe on vetää suora kaikkien pisteiden kautta mutkitellen: pisteiden vaihtelu ylös ja alas johtuu mittausepävarmuudesta, ja suora kuuluu vetää pisteiden joukon keskeltä.

## Tiivistelmä
- Suljetussa jäykässä astiassa harvan kaasun paine on mittausalueella lineaarinen funktio lämpötilasta: $p = p_0 + k\theta$. Mittausaineisto muuttuu suoraksi piirtämällä $p$ lämpötilan funktiona ja vetämällä suora pisteiden joukon keskeltä.
- Mittausepävarmuus kuvaa mittaustulokseen liittyvää epävarmuutta, eikä se yleensä ole ehdoton suurin mahdollinen poikkeama oikeasta arvosta. Suoran ei tarvitse osua jokaiseen pisteeseen vaan kulkea epävarmuusvälien kautta.
- Ekstrapolointi jatkaa suoraa mittausalueen ulkopuolelle: nollapaineen lämpötila on $\theta_0 = -p_0/k$.
- Epävarmuus arvioidaan ääriviivoista: $\Delta\theta_0 = (\theta_{0,\text{max}} - \theta_{0,\text{min}})/2$. Tulos $\theta_0 \pm \Delta\theta_0$ sopii yhteen hyväksytyn arvon $-273{,}15\,{}^\circ\text{C}$ kanssa, jos se kuuluu väliin.
