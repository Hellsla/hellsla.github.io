# Paikka, nopeus ja tasainen liike kuvaajina

> **Miksi** pyöräilijän kuljettu matka voi olla neljä kilometriä, vaikka hänen siirtymänsä on nolla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: ylhäältä vinosti nähty järvi, jonka ympäri kiertää polku. Lähtöpaikalla on lippu, ja polulla ajaa pyöräilijä, joka on kiertämässä järven ympäri takaisin lähtöpaikkaan. Nuolet näyttävät kiertosuunnan." class="fig-hero" style="max-width:100%;font-size:24px">
  <rect x="0" y="0" width="1200" height="600" fill="#b2f2bb"/>
  <circle cx="89.5" cy="558.5" r="17.3452" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="140" cy="487" r="23.7322" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1076" cy="490" r="14.176" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1049" cy="500" r="16.3263" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="273.5" cy="515.5" r="15.2448" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1094" cy="263.5" r="19.0694" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1059.5" cy="426.5" r="21.3652" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="170" cy="213" r="19.9795" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="151" cy="210.5" r="23.4346" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1008" cy="152.5" r="22.1629" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="220.5" cy="483" r="23.3067" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="76" cy="274" r="20.65" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="100" cy="380.5" r="18.7499" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="600" cy="340" rx="430" ry="200" fill="none" stroke="#d9b26a" stroke-width="40"/>
  <ellipse cx="600" cy="340" rx="430" ry="200" fill="none" stroke="#e9c98a" stroke-width="2" stroke-dasharray="2 10"/>
  <ellipse cx="600" cy="340" rx="370" ry="156" fill="#a9d1f0" stroke="#2f74b5" stroke-width="3"/>
  <path d="M430,300 q16,-8 32,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"/>
  <path d="M500,318 q16,-8 32,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"/>
  <path d="M570,300 q16,-8 32,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"/>
  <path d="M640,318 q16,-8 32,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"/>
  <path d="M710,300 q16,-8 32,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round"/>
  <line x1="865" y1="498.5" x2="814" y2="513.5" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M800,518 L813,506.5 L817,520.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="345" y1="502" x2="296" y2="482" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M282,476 L299.5,475.5 L294,489 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="189.5" y1="275" x2="228" y2="238.5" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M239,228 L232.5,244.5 L222.5,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="646.5" y1="140.5" x2="699" y2="145" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M714,146.5 L697.5,152.5 L699,138 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="976.5" y1="239.5" x2="1011.5" y2="279.5" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M1021,291 L1005,283.5 L1016,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="600" y1="540" x2="600" y2="450" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M600,450 l50,14 l-50,14 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <ellipse cx="600" cy="540" rx="16" ry="6" fill="#6c757d"/>
  <circle cx="944" cy="452" r="22" fill="none" stroke="#1f2933" stroke-width="4"/>
  <circle cx="1016" cy="452" r="22" fill="none" stroke="#1f2933" stroke-width="4"/>
  <path d="M944,452 L972,452 L998,416 L962,416 Z M972,452 L958,406 M1016,452 L1002,402" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round" stroke-linejoin="round"/>
  <path d="M958,402 L978,352" fill="none" stroke="#1971c2" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M976,360 L1004,398" fill="none" stroke="#1971c2" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M958,402 L976,428 L972,452" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="986" cy="336" r="13" fill="#f1dfb5"/>
  <path d="M972,332 Q984,316 1000,332 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
</svg>

## Ydinajatus
Liikkeen kuvaaminen alkaa sopimuksesta. Valitaan suora, jota pitkin kappale liikkuu, ja sille origo ja positiivinen suunta: tämä on $x$-akseli. **Paikka** $x$ kertoo, missä kappale on origoon nähden. Etumerkki kertoo puolen: paikka $x = -3\,\text{m}$ on kolme metriä origosta negatiiviseen suuntaan. Aika $t$ mitataan kellolla, ja liike kuvataan kertomalla paikka jokaisella hetkellä.

Kun kappale siirtyy paikasta $x_1$ paikkaan $x_2$, sen **siirtymä** on paikan muutos $\Delta x = x_2 - x_1$. Siirtymä on vektorisuure: sillä on suuruus ja suunta, ja suoralla suunta ilmoitetaan etumerkillä. Plus tarkoittaa positiivista suuntaa ja miinus vastakkaista. Siirtymä ei ole sama asia kuin kuljettu matka $s$. Matka on reitin pituus eikä se voi olla negatiivinen. Jos pyöräilijä ajaa kaupalle ja takaisin, matka on neljä kilometriä, mutta siirtymä on nolla, koska loppupaikka on sama kuin alkupaikka.

<svg data-fig="displacement" viewBox="0 0 600 392" role="img" aria-label="Kaavakuva kahdesta siirtymästä x-akselilla, akseli piirretty mittakaavassa. Ylhäällä kappale siirtyy paikasta x1 = 2 m paikkaan x2 = 8 m, joten siirtymä on +6 m ja osoittaa oikealle. Alhaalla kappale siirtyy paikasta x1 = 8 m paikkaan x2 = 3 m, joten siirtymä on −5 m ja osoittaa vasemmalle." style="max-width:100%;font-size:24px">
  <line x1="50" y1="104" x2="482" y2="104" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,104 L481,110 L481,98 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="100" x2="70" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="150" y1="100" x2="150" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="230" y1="100" x2="230" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="310" y1="100" x2="310" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="390" y1="100" x2="390" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="470" y1="100" x2="470" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="502" y="89.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="222.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\Delta x = +6\,\text{m}$</div></foreignObject>
  <line x1="150" y1="62" x2="371" y2="62" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M390,62 L370,71 L370,53 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="150" cy="104" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="390" cy="104" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="133.5" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="373.5" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
  <line x1="24" y1="198" x2="576" y2="198" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <line x1="50" y1="304" x2="482" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,304 L481,310 L481,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="300" x2="70" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="150" y1="300" x2="150" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="230" y1="300" x2="230" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="310" y1="300" x2="310" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="390" y1="300" x2="390" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="470" y1="300" x2="470" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="502" y="289.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="242.5" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\Delta x = -5\,\text{m}$</div></foreignObject>
  <line x1="390" y1="262" x2="209" y2="262" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M190,262 L210,253 L210,271 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="390" cy="304" r="9" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="190" cy="304" r="9" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="373.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="173.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
</svg>

<svg data-fig="round-trip" viewBox="0 0 600 322" role="img" aria-label="Kaavakuva, ei mittakaavassa: pyöräilijä ajaa kotoa kauppaan, kaksi kilometriä, ja takaisin kotiin, toiset kaksi kilometriä. Kuljettu matka on s = 2 km + 2 km = 4 km, mutta loppupaikka on sama kuin alkupaikka, joten siirtymä on nolla." style="max-width:100%;font-size:24px">
  <line x1="50" y1="120" x2="468" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M480,120 L467,126 L467,114 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="116" x2="110" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="100" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="260" y1="116" x2="260" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="410" y1="116" x2="410" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="400" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="488" y="105.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{km})$</div></foreignObject>
  <rect x="90" y="96" width="40" height="24" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M84,96 L110,76 L136,96 Z" fill="#b8622d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="386" y="90" width="48" height="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="382" y="90" width="56" height="10" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="110" y1="64" x2="391" y2="64" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M410,64 L390,73 L390,55 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="175" y="15.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{menomatka } 2\,\text{km}$</div></foreignObject>
  <line x1="410" y1="184" x2="129" y2="184" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M110,184 L130,175 L130,193 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="168.5" y="199.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{paluumatka } 2\,\text{km}$</div></foreignObject>
  <line x1="24" y1="238" x2="576" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="196" y="251.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s = 2\,\text{km} + 2\,\text{km} = 4\,\text{km}$</div></foreignObject>
  <foreignObject x="233.5" y="285.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta x = x_2 - x_1 = 0$</div></foreignObject>
</svg>

**Nopeus** kertoo, kuinka nopeasti ja mihin suuntaan paikka muuttuu. Se on myös vektorisuure, ja sen etumerkki kertoo suunnan. Nopeuden itseisarvo $|v|$ on vauhti. Tasaisessa liikkeessä nopeus pysyy vakiona: paikka muuttuu yhtä paljon jokaisessa yhtä pitkässä aikavälissä.

Liike voidaan esittää **$(t,x)$-kuvaajana**, jossa vaaka-akselilla on aika ja pystyakselilla paikka. Tasaisen liikkeen kuvaaja on suora. Suoran jyrkkyys eli kulmakerroin on nopeus: jyrkempi suora tarkoittaa suurempaa nopeutta, vaakasuora suora paikallaan oloa ja laskeva suora liikettä negatiiviseen suuntaan. Kuvaaja ei ole kuva kappaleen radasta: nouseva viiva ei tarkoita ylämäkeä, vaan sitä, että paikka kasvaa.

## Kaava: Keskinopeus ja tasaisen liikkeen yhtälö
Kun paikka muuttuu aikavälillä $\Delta t = t_2 - t_1$ määrän $\Delta x$, keskinopeus on siirtymä jaettuna ajalla:
```latex
v_\text{ka} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}
```
missä $v_\text{ka}$ on keskinopeus (m/s), $\Delta x$ siirtymä (m), $\Delta t$ kulunut aika (s) ja $x_1$ ja $x_2$ paikat (m) hetkillä $t_1$ ja $t_2$. Vektorina nopeus kirjoitetaan $\mathbf{v}$ ja siirtymä $\Delta\mathbf{x}$. Suoralla käytetään niiden komponentteja $v$ ja $\Delta x$, joiden etumerkki kertoo suunnan.

Tasaisessa liikkeessä keskinopeus on sama millä tahansa aikavälillä, ja sitä kutsutaan nopeudeksi $v$. Epätasaisessa liikkeessä keskinopeus kertoo vain sen vakionopeuden, jolla sama siirtymä tehtäisiin samassa ajassa. Jos kappale on hetkellä $t = 0$ paikassa $x_0$, kaava ratkaistuna paikalle antaa paikan ajan funktiona:
```latex
x = x_0 + v\,t
```
missä $x$ on paikka hetkellä $t$ (m), $x_0$ alkupaikka (m), $v$ nopeus (m/s) ja $t$ aika (s). Tämä on $(t,x)$-kuvaajan suoran yhtälö: $x_0$ on suoran leikkauskohta paikka-akselilla ja $v$ sen kulmakerroin.

<svg data-fig="graph-slope" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kahdesta (t,x)-kuvaajasta, ei lukuarvoja. Vasemmalla suora nousee alkupaikasta x0, ja suoralta on valittu kaksi pistettä: aikaväli Δt ja paikan muutos Δx muodostavat kolmion, jonka avulla nopeus v on Δx jaettuna Δt:lla. Oikealla kolme suoraa samasta alkupaikasta: nouseva suora on nopeus v suurempi kuin nolla, vaakasuora suora nopeus nolla ja laskeva suora nopeus pienempi kuin nolla." style="max-width:100%;font-size:24px">
  <line x1="49" y1="290" x2="264" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M276,290 L263,296 L263,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="291" x2="50" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,44 L56,57 L44,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="282" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="40" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="50,246 250,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="110,206.5 210,206.5 210,140.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="50" cy="246" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="110" cy="206.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="210" cy="140.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="143.5" y="216" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="222" y="159" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta x$</div></foreignObject>
  <foreignObject x="7" y="231.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x_0$</div></foreignObject>
  <foreignObject x="62" y="76" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v = \dfrac{\Delta x}{\Delta t}$</div></foreignObject>
  <line x1="339" y1="290" x2="504" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M516,290 L503,296 L503,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="340" y1="291" x2="340" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M340,44 L346,57 L334,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="522" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="330" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="340,180 490,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v > 0$</div></foreignObject>
  <polyline points="340,180 490,180" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="165.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$v = 0$</div></foreignObject>
  <polyline points="340,180 490,246" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$v < 0$</div></foreignObject>
  <circle cx="340" cy="180" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="297" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x_0$</div></foreignObject>
</svg>

Kulmakerroin lasketaan valitsemalla suoralta kaksi toisistaan kaukana olevaa pistettä ja jakamalla paikan muutos ajan muutoksella. Mittauspisteistä piirretyssä kuvaajassa suora sovitetaan pisteiden läpi niin, että pisteet jäävät tasaisesti suoran molemmille puolille. Kulmakerroin lasketaan suoralta, ei kahdesta vierekkäisestä mittauspisteestä, koska jokaisessa mittauksessa on pieni virhe.

## Esimerkki
Hölkkääjän liike on tasaista. Kuvaajasta luetaan, että hän on hetkellä $t = 0$ paikassa $20\,\text{m}$ ja hetkellä $t = 40\,\text{s}$ paikassa $120\,\text{m}$. Mikä on hölkkääjän nopeus, ja missä paikassa hän on hetkellä $t = 60\,\text{s}$?

<svg data-fig="jogger-graph" viewBox="0 0 600 340" role="img" aria-label="(t,x)-kuvaaja mittakaavassa: suora nousee paikasta 20 metriä hetkellä 0 paikkaan 120 metriä hetkellä 40 sekuntia ja jatkuu katkoviivana paikkaan 170 metriä hetkellä 60 sekuntia." style="max-width:100%;font-size:24px">
  <line x1="200" y1="296" x2="200" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308" y1="296" x2="308" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="296" x2="416" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="272.5" x2="470" y2="272.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="155.5" x2="470" y2="155.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="97" x2="470" y2="97" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="296" x2="484" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,296 L483,302 L483,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="297" x2="92" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,36 L98,49 L86,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="200" y1="296" x2="200" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="183.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="308" y1="296" x2="308" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="291.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="416" y1="296" x2="416" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="399.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="85" y1="272.5" x2="92" y2="272.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="258" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="155.5" x2="92" y2="155.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="141" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <line x1="85" y1="97" x2="92" y2="97" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="82.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$170$</div></foreignObject>
  <foreignObject x="62" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="281.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="82" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <polyline points="92,272.5 308,155.5" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="308,155.5 416,97" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <line x1="308" y1="155.5" x2="308" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="155.5" x2="308" y2="155.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="416" y1="97" x2="416" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="97" x2="416" y2="97" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="92" cy="272.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="308" cy="155.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="416" cy="97" r="7" fill="#ffffff" stroke="#1971c2" stroke-width="3"/>
</svg>

<!-- vaihe -->

**Tunnetut ja kysytty.** Kuvaajasta luetaan kaksi pistettä: $(t_1;\, x_1) = (0\,\text{s};\, 20\,\text{m})$ ja $(t_2;\, x_2) = (40\,\text{s};\, 120\,\text{m})$. Kysytään nopeutta $v$ ja paikkaa $x$ hetkellä $t = 60\,\text{s}$.

<!-- vaihe -->

**Periaate.** Hölkkääjän liike on tasaista, joten nopeus pysyy vakiona ja $(t, x)$-kuvaaja on suora. Silloin nopeus on suoran kulmakerroin eli paikan muutos jaettuna ajan muutoksella. Kun nopeus tunnetaan, paikan saa alkupaikasta lisäämällä nopeuden ja ajan tulon.

<!-- vaihe -->

**Kaava ratkaistuna.** Nopeus ja paikka ratkaistaan symbolisesti ennen lukuja:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
x &= x_1 + v\,t
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Paikat ovat metreinä ja ajat sekunteina, joten nopeus tulee suoraan yksikössä $\text{m/s}$. Muunnoksia ei tarvita. Alkupaikka on $x_1 = 20\,\text{m}$ hetkellä $t_1 = 0$, joten ajaksi $t$ kelpaa suoraan $60\,\text{s}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
&= \frac{120\,\text{m} - 20\,\text{m}}{40\,\text{s} - 0\,\text{s}} \\
&= 2{,}5\,\text{m/s}
\\[4pt]
x &= x_1 + v\,t \\
&= 20\,\text{m} + 2{,}5\,\text{m/s} \cdot 60\,\text{s} \\
&= 20\,\text{m} + 150\,\text{m} \\
&= 170\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Nopeus on $v = 2{,}5\,\text{m/s}$ ja paikka hetkellä $60\,\text{s}$ on $x = 170\,\text{m}$ eli $1{,}7 \cdot 10^2\,\text{m}$. Nopeudessa on kaksi merkitsevää numeroa, koska aikaväli $40\,\text{s}$ on kahdella numerolla. Paikassa tulo $2{,}5\,\text{m/s} \cdot 60\,\text{s} = 150\,\text{m}$ on myös kahdella numerolla, joten summa $20\,\text{m} + 150\,\text{m}$ tunnetaan vain kymmenien metrien tarkkuudella: $x = 1{,}7 \cdot 10^2\,\text{m}$.

<!-- vaihe -->

**Järkevyys.** Ensimmäisten 40 sekunnin aikana paikka kasvoi $100\,\text{m}$, joten seuraavien 20 sekunnin aikana se kasvaa puolet siitä, $50\,\text{m}$. Paikka on $120\,\text{m} + 50\,\text{m} = 170\,\text{m}$, eli sama tulos. Nopeus $2{,}5\,\text{m/s}$ on noin $9\,\text{km/h}$, joka on hölkän vauhti. Nopeus on positiivinen, koska kuvaaja nousee.

## Yleinen virhekäsitys
$(t,x)$-kuvaaja ei ole kuva kappaleen radasta: nouseva viiva ei tarkoita ylämäkeä, vaan sitä, että paikka kasvaa. Toinen virhe on pitää negatiivista nopeutta hitaana nopeutena. Etumerkki kertoo vain suunnan: nopeus $-3\,\text{m/s}$ on suuruudeltaan suurempi kuin $+2\,\text{m/s}$. Kolmas virhe on päätellä paikasta nopeus: kappale voi olla edellä ja liikkua silti hitaammin.

## Tiivistelmä
- Paikka $x$ kertoo, missä kappale on origoon nähden. Siirtymä $\Delta x = x_2 - x_1$ on paikan muutos, ja sen etumerkki kertoo suunnan. Matka on reitin pituus eikä ole negatiivinen.
- Nopeus $v = \Delta x / \Delta t$ on vektorisuure. Tasaisessa liikkeessä se on vakio, ja paikka on $x = x_0 + v\,t$.
- $(t,x)$-kuvaajassa tasaisen liikkeen viiva on suora. Kulmakerroin on nopeus, ja sen etumerkki kertoo suunnan.
- Mittausaineistosta sovitetaan suora, ja nopeus lasketaan suoralta valituista kaukana toisistaan olevista pisteistä.
- Edestakaisen liikkeen keskinopeus voi olla nolla, vaikka matka ei ole nolla.
