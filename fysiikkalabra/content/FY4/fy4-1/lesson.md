# Paikka, nopeus ja tasainen liike kuvaajina

> **Miksi** pyöräilijän kuljettu matka voi olla neljä kilometriä, vaikka hänen siirtymänsä on nolla?

## Ydinajatus
Liikkeen kuvaaminen alkaa sopimuksesta. Valitaan suora, jota pitkin kappale liikkuu, ja sille origo ja positiivinen suunta: tämä on x-akseli. **Paikka** $x$ kertoo, missä kappale on origoon nähden. Etumerkki kertoo puolen: paikka $x = -3\,\text{m}$ on kolme metriä origosta negatiiviseen suuntaan. Aika $t$ mitataan kellolla, ja liike kuvataan kertomalla paikka jokaisella hetkellä.

Kun kappale siirtyy paikasta $x_1$ paikkaan $x_2$, sen **siirtymä** on paikan muutos $\Delta x = x_2 - x_1$. Siirtymä on vektorisuure: sillä on suuruus ja suunta, ja suoralla suunta ilmoitetaan etumerkillä. Plus tarkoittaa positiivista suuntaa ja miinus vastakkaista. Siirtymä ei ole sama asia kuin kuljettu matka $s$. Matka on reitin pituus eikä se voi olla negatiivinen. Jos pyöräilijä ajaa kaupalle ja takaisin, matka on neljä kilometriä, mutta siirtymä on nolla, koska loppupaikka on sama kuin alkupaikka.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva kahdesta siirtymästä x-akselilla. Ylhäällä kappale siirtyy paikasta x1 = 2 m paikkaan x2 = 8 m, joten siirtymä on +6 m ja osoittaa oikealle. Alhaalla kappale siirtyy paikasta x1 = 8 m paikkaan x2 = 3 m, joten siirtymä on −5 m ja osoittaa vasemmalle." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <foreignObject x="175" y="0" width="260" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\Delta x = +6\,\text{m}$</div></foreignObject>
  <line x1="182" y1="52" x2="440" y2="52" stroke="currentColor" stroke-width="5"/>
  <polygon points="458,52 436,42 436,62" fill="currentColor"/>
  <line x1="80" y1="84" x2="560" y2="84" stroke="currentColor" stroke-width="3"/>
  <line x1="90" y1="76" x2="90" y2="92" stroke="currentColor" stroke-width="3"/>
  <line x1="182" y1="76" x2="182" y2="92" stroke="currentColor" stroke-width="3"/>
  <line x1="274" y1="76" x2="274" y2="92" stroke="currentColor" stroke-width="3"/>
  <line x1="366" y1="76" x2="366" y2="92" stroke="currentColor" stroke-width="3"/>
  <line x1="458" y1="76" x2="458" y2="92" stroke="currentColor" stroke-width="3"/>
  <line x1="550" y1="76" x2="550" y2="92" stroke="currentColor" stroke-width="3"/>
  <circle cx="182" cy="84" r="9" fill="currentColor"/>
  <circle cx="458" cy="84" r="9" fill="currentColor"/>
  <text x="8" y="94" fill="currentColor">x (m)</text>
  <text x="90" y="120" text-anchor="middle" fill="currentColor">0</text>
  <text x="182" y="120" text-anchor="middle" fill="currentColor">2</text>
  <text x="274" y="120" text-anchor="middle" fill="currentColor">4</text>
  <text x="366" y="120" text-anchor="middle" fill="currentColor">6</text>
  <text x="458" y="120" text-anchor="middle" fill="currentColor">8</text>
  <text x="550" y="120" text-anchor="middle" fill="currentColor">10</text>
  <foreignObject x="157" y="128" width="50" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$x_1$</div></foreignObject>
  <foreignObject x="433" y="128" width="50" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$x_2$</div></foreignObject>
  <foreignObject x="215" y="164" width="260" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\Delta x = -5\,\text{m}$</div></foreignObject>
  <line x1="458" y1="214" x2="250" y2="214" stroke="currentColor" stroke-width="5"/>
  <polygon points="228,214 252,204 252,224" fill="currentColor"/>
  <line x1="80" y1="246" x2="560" y2="246" stroke="currentColor" stroke-width="3"/>
  <line x1="90" y1="238" x2="90" y2="254" stroke="currentColor" stroke-width="3"/>
  <line x1="182" y1="238" x2="182" y2="254" stroke="currentColor" stroke-width="3"/>
  <line x1="274" y1="238" x2="274" y2="254" stroke="currentColor" stroke-width="3"/>
  <line x1="366" y1="238" x2="366" y2="254" stroke="currentColor" stroke-width="3"/>
  <line x1="458" y1="238" x2="458" y2="254" stroke="currentColor" stroke-width="3"/>
  <line x1="550" y1="238" x2="550" y2="254" stroke="currentColor" stroke-width="3"/>
  <circle cx="458" cy="246" r="9" fill="currentColor"/>
  <circle cx="228" cy="246" r="9" fill="currentColor"/>
  <text x="8" y="256" fill="currentColor">x (m)</text>
  <foreignObject x="173" y="256" width="110" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$x_2 = 3$</div></foreignObject>
  <foreignObject x="403" y="256" width="110" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$x_1 = 8$</div></foreignObject>
</svg>

**Nopeus** kertoo, kuinka nopeasti ja mihin suuntaan paikka muuttuu. Se on myös vektorisuure, ja sen etumerkki kertoo suunnan. Nopeuden itseisarvo $|v|$ on vauhti. Tasaisessa liikkeessä nopeus pysyy vakiona: paikka muuttuu yhtä paljon jokaisessa yhtä pitkässä aikavälissä.

Liike voidaan esittää **(t,x)-kuvaajana**, jossa vaaka-akselilla on aika ja pystyakselilla paikka. Tasaisen liikkeen kuvaaja on suora. Suoran jyrkkyys eli kulmakerroin on nopeus: jyrkempi suora tarkoittaa suurempaa nopeutta, vaakasuora suora paikallaan oloa ja laskeva suora liikettä negatiiviseen suuntaan. Kuvaaja ei ole kuva kappaleen radasta: nouseva viiva ei tarkoita ylämäkeä, vaan sitä, että paikka kasvaa.

## Kaava
Kun paikka muuttuu aikavälillä $\Delta t = t_2 - t_1$ määrän $\Delta x$, keskinopeus on siirtymä jaettuna ajalla:
```latex
v_\text{ka} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}
```
missä $v_\text{ka}$ on keskinopeus (m/s), $\Delta x$ siirtymä (m), $\Delta t$ kulunut aika (s) ja $x_1$ ja $x_2$ paikat (m) hetkillä $t_1$ ja $t_2$. Vektorina nopeus kirjoitetaan $\mathbf{v}$ ja siirtymä $\Delta\mathbf{x}$. Suoralla käytetään niiden komponentteja $v$ ja $\Delta x$, joiden etumerkki kertoo suunnan.

Tasaisessa liikkeessä keskinopeus on sama millä tahansa aikavälillä, ja sitä kutsutaan nopeudeksi $v$. Epätasaisessa liikkeessä keskinopeus kertoo vain sen vakionopeuden, jolla sama siirtymä tehtäisiin samassa ajassa. Jos kappale on hetkellä $t = 0$ paikassa $x_0$, kaava ratkaistuna paikalle antaa paikan ajan funktiona:
```latex
x = x_0 + v\,t
```
missä $x$ on paikka hetkellä $t$ (m), $x_0$ alkupaikka (m), $v$ nopeus (m/s) ja $t$ aika (s). Tämä on (t,x)-kuvaajan suoran yhtälö: $x_0$ on suoran leikkauskohta paikka-akselilla ja $v$ sen kulmakerroin.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva kahdesta (t,x)-kuvaajasta. Vasemmalla suora nousee alkupaikasta x0, ja suoralta on valittu kaksi pistettä: aikaväli Δt ja paikan muutos Δx muodostavat kolmion, jonka avulla nopeus v on Δx jaettuna Δt:lla. Oikealla kolme suoraa samasta alkupaikasta: nouseva suora on nopeus v suurempi kuin nolla, vaakasuora suora nopeus nolla ja laskeva suora nopeus pienempi kuin nolla." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="50" y1="262" x2="290" y2="262" stroke="currentColor" stroke-width="3"/>
  <line x1="50" y1="262" x2="50" y2="34" stroke="currentColor" stroke-width="3"/>
  <polygon points="50,22 42,40 58,40" fill="currentColor"/>
  <polygon points="300,262 282,254 282,270" fill="currentColor"/>
  <text x="62" y="32" fill="currentColor">x</text>
  <text x="250" y="292" fill="currentColor">t</text>
  <line x1="50" y1="210" x2="262" y2="89" stroke="currentColor" stroke-width="5"/>
  <circle cx="50" cy="210" r="6" fill="currentColor"/>
  <circle cx="110" cy="176" r="7" fill="currentColor"/>
  <circle cx="230" cy="107" r="7" fill="currentColor"/>
  <line x1="110" y1="176" x2="230" y2="176" stroke="currentColor" stroke-width="3" stroke-dasharray="8 6"/>
  <line x1="230" y1="176" x2="230" y2="107" stroke="currentColor" stroke-width="3" stroke-dasharray="8 6"/>
  <foreignObject x="135" y="182" width="70" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\Delta t$</div></foreignObject>
  <foreignObject x="236" y="124" width="60" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\Delta x$</div></foreignObject>
  <foreignObject x="2" y="192" width="46" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$x_0$</div></foreignObject>
  <foreignObject x="84" y="12" width="150" height="58"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$v = \tfrac{\Delta x}{\Delta t}$</div></foreignObject>
  <line x1="350" y1="262" x2="580" y2="262" stroke="currentColor" stroke-width="3"/>
  <line x1="350" y1="262" x2="350" y2="34" stroke="currentColor" stroke-width="3"/>
  <polygon points="350,22 342,40 358,40" fill="currentColor"/>
  <polygon points="592,262 574,254 574,270" fill="currentColor"/>
  <text x="362" y="32" fill="currentColor">x</text>
  <text x="545" y="292" fill="currentColor">t</text>
  <line x1="350" y1="150" x2="560" y2="46" stroke="currentColor" stroke-width="5"/>
  <line x1="350" y1="150" x2="560" y2="150" stroke="currentColor" stroke-width="5"/>
  <line x1="350" y1="150" x2="560" y2="214" stroke="currentColor" stroke-width="5"/>
  <text x="430" y="40" fill="currentColor">v &gt; 0</text>
  <text x="470" y="136" fill="currentColor">v = 0</text>
  <text x="470" y="252" fill="currentColor">v &lt; 0</text>
</svg>

Kulmakerroin lasketaan valitsemalla suoralta kaksi toisistaan kaukana olevaa pistettä ja jakamalla paikan muutos ajan muutoksella. Mittauspisteistä piirretyssä kuvaajassa suora sovitetaan pisteiden läpi niin, että pisteet jäävät tasaisesti suoran molemmille puolille. Kulmakerroin lasketaan suoralta, ei kahdesta vierekkäisestä mittauspisteestä, koska jokaisessa mittauksessa on pieni virhe.

## Esimerkki
Hölkkääjän liike on tasaista. Kuvaajasta luetaan, että hän on hetkellä $t = 0$ paikassa $20\,\text{m}$ ja hetkellä $t = 40\,\text{s}$ paikassa $120\,\text{m}$. Mikä on hölkkääjän nopeus, ja missä paikassa hän on hetkellä $t = 60\,\text{s}$?

<svg viewBox="0 0 600 300" role="img" aria-label="(t,x)-kuvaaja mittakaavassa: suora nousee paikasta 20 metriä hetkellä 0 paikkaan 120 metriä hetkellä 40 sekuntia ja jatkuu katkoviivana paikkaan 170 metriä hetkellä 60 sekuntia" style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="70" y1="250" x2="560" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="70" y1="250" x2="70" y2="30" stroke="currentColor" stroke-width="3"/>
  <polygon points="70,20 62,38 78,38" fill="currentColor"/>
  <polygon points="572,250 554,242 554,258" fill="currentColor"/>
  <text x="82" y="30" fill="currentColor">x (m)</text>
  <text x="524" y="284" fill="currentColor">t (s)</text>
  <line x1="70" y1="226" x2="350" y2="106" stroke="currentColor" stroke-width="5"/>
  <line x1="350" y1="106" x2="490" y2="46" stroke="currentColor" stroke-width="5" stroke-dasharray="10 8"/>
  <line x1="350" y1="106" x2="350" y2="250" stroke="currentColor" stroke-opacity="0.5" stroke-width="2" stroke-dasharray="6 6"/>
  <line x1="70" y1="106" x2="350" y2="106" stroke="currentColor" stroke-opacity="0.5" stroke-width="2" stroke-dasharray="6 6"/>
  <circle cx="70" cy="226" r="8" fill="currentColor"/>
  <circle cx="350" cy="106" r="8" fill="currentColor"/>
  <text x="60" y="234" text-anchor="end" fill="currentColor">20</text>
  <text x="60" y="114" text-anchor="end" fill="currentColor">120</text>
  <line x1="70" y1="46" x2="490" y2="46" stroke="currentColor" stroke-opacity="0.5" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="60" y="54" text-anchor="end" fill="currentColor">170</text>
  <text x="350" y="282" text-anchor="middle" fill="currentColor">40</text>
  <text x="490" y="282" text-anchor="middle" fill="currentColor">60</text>
</svg>

<!-- vaihe -->

**Tunnetut ja kysytty.** Kuvaajasta: $t_1 = 0$, $x_1 = 20\,\text{m}$, $t_2 = 40\,\text{s}$ ja $x_2 = 120\,\text{m}$. Kysytään nopeutta $v$ ja paikkaa $x$ hetkellä $t = 60\,\text{s}$.

<!-- vaihe -->

**Nopeus symbolisesti.** Liike on tasaista, joten nopeus on paikan muutos jaettuna ajan muutoksella:
```latex
\begin{aligned}
v &= \frac{\Delta x}{\Delta t} \\
&= \frac{x_2 - x_1}{t_2 - t_1}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
&= \frac{120\,\text{m} - 20\,\text{m}}{40\,\text{s} - 0\,\text{s}} \\
&= 2{,}5\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Paikka hetkellä 60 s.** Käytetään tasaisen liikkeen paikan kaavaa alkupaikasta $x_0 = 20\,\text{m}$ lähtien:
```latex
\begin{aligned}
x &= x_0 + v\,t \\
&= 20\,\text{m} + 2{,}5\,\text{m/s} \cdot 60\,\text{s} \\
&= 170\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Järkevyys.** Ensimmäisten 40 sekunnin aikana paikka kasvoi 100 m, joten seuraavien 20 sekunnin aikana se kasvaa puolet siitä, 50 m. Paikka on $120\,\text{m} + 50\,\text{m} = 170\,\text{m}$, eli sama tulos. Nopeus 2,5 m/s on noin 9 km/h, joka on hölkän vauhti. Nopeus on positiivinen, koska kuvaaja nousee.

## Yleinen virhekäsitys
(t,x)-kuvaaja ei ole kuva kappaleen radasta: nouseva viiva ei tarkoita ylämäkeä, vaan sitä, että paikka kasvaa. Toinen virhe on pitää negatiivista nopeutta hitaana nopeutena. Etumerkki kertoo vain suunnan: nopeus $-3\,\text{m/s}$ on suuruudeltaan suurempi kuin $+2\,\text{m/s}$. Kolmas virhe on päätellä paikasta nopeus: kappale voi olla edellä ja liikkua silti hitaammin.

## Tiivistelmä
- Paikka $x$ kertoo, missä kappale on origoon nähden. Siirtymä $\Delta x = x_2 - x_1$ on paikan muutos, ja sen etumerkki kertoo suunnan. Matka on reitin pituus eikä ole negatiivinen.
- Nopeus $v = \Delta x / \Delta t$ on vektorisuure. Tasaisessa liikkeessä se on vakio, ja paikka on $x = x_0 + v\,t$.
- (t,x)-kuvaajassa tasaisen liikkeen viiva on suora. Kulmakerroin on nopeus, ja sen etumerkki kertoo suunnan.
- Mittausaineistosta sovitetaan suora, ja nopeus lasketaan suoralta valituista kaukana toisistaan olevista pisteistä.
- Edestakaisen liikkeen keskinopeus voi olla nolla, vaikka matka ei ole nolla.
