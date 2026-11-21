# Paikka, nopeus ja tasainen liike kuvaajina

> **Miksi** pyöräilijän kuljettu matka voi olla neljä kilometriä, vaikka hänen siirtymänsä on nolla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: järvi metsän keskellä nähtynä vinosti ylhäältä. Järven ympäri kiertää hiekkapolku. Polun lähtöpaikalla on lippu ja lähtöviiva. Etualalla pyöräilijä ajaa polkua kohti lähtöpaikkaa. Hän on kiertänyt järven ympäri. Polun nuolet näyttävät kiertosuunnan." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Liikkeen kuvaaminen alkaa sopimuksesta. Valitaan suora, jota pitkin kappale liikkuu. Suoralle valitaan origo eli nollakohta ja positiivinen suunta. Tämä suora on $x$-akseli. **Paikka** $x$ kertoo, missä kappale on origoon nähden. Etumerkki kertoo, kummalla puolella kappale on. Paikka $x = -3\,\text{m}$ on kolme metriä origosta negatiiviseen suuntaan. Aika $t$ mitataan kellolla. Liike kuvataan kertomalla paikka jokaisella hetkellä.

Kappale voi siirtyä paikasta $x_1$ paikkaan $x_2$. Silloin sen **siirtymä** on paikan muutos $\Delta x = x_2 - x_1$. Siirtymä on **vektorisuure**. Vektorisuureella on sekä suuruus että suunta. Esimerkiksi tuulen nopeus on vektorisuure: pitää tietää, kuinka kovaa tuulee ja mihin suuntaan. Suoralla suunta kerrotaan etumerkillä. Plus tarkoittaa positiivista suuntaa ja miinus vastakkaista suuntaa. Siirtymä ei ole sama asia kuin kuljettu matka $s$. Matka on reitin pituus. Matka ei voi olla negatiivinen. Pyöräilijä voi ajaa kaupalle ja takaisin. Silloin matka on neljä kilometriä. Siirtymä on nolla, koska loppupaikka on sama kuin alkupaikka.

<svg data-fig="displacement" viewBox="0 0 600 392" role="img" aria-label="Kaavakuva kahdesta siirtymästä x-akselilla. Akseli on piirretty mittakaavassa. Ylhäällä kappale siirtyy paikasta x1 = 2 m paikkaan x2 = 8 m. Siirtymä on +6 m ja osoittaa oikealle. Alhaalla kappale siirtyy paikasta x1 = 8 m paikkaan x2 = 3 m. Siirtymä on −5 m ja osoittaa vasemmalle." style="max-width:100%;font-size:24px">
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
  <foreignObject x="242.5" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta x = -5\,\text{m}$</div></foreignObject>
  <line x1="390" y1="262" x2="209" y2="262" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <path d="M190,262 L210,253 L210,271 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="390" cy="304" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="190" cy="304" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="373.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="173.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
</svg>

<svg data-fig="round-trip" viewBox="0 0 600 322" role="img" aria-label="Kaavakuva, ei mittakaavassa. Pyöräilijä ajaa kotoa kauppaan, kaksi kilometriä, ja takaisin kotiin, toiset kaksi kilometriä. Kuljettu matka on s = 2 km + 2 km = 4 km. Loppupaikka on sama kuin alkupaikka, joten siirtymä on nolla." style="max-width:100%;font-size:24px">
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
  <line x1="410" y1="184" x2="129" y2="184" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <path d="M110,184 L130,175 L130,193 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="168.5" y="199.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paluumatka } 2\,\text{km}$</div></foreignObject>
  <line x1="24" y1="238" x2="576" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="196" y="251.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s = 2\,\text{km} + 2\,\text{km} = 4\,\text{km}$</div></foreignObject>
  <foreignObject x="233.5" y="285.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta x = x_2 - x_1 = 0$</div></foreignObject>
</svg>

```pysahdy
Pyöräilijä ajaa kaupalle ja takaisin. Miksi hänen siirtymänsä on nolla, vaikka hän ajoi monta kilometriä?
---
Siirtymä kertoo vain alkupaikan ja loppupaikan eron. Ne ovat samat. Matka on reitin pituus, joten se on silti neljä kilometriä.
```

**Nopeus** kertoo, kuinka nopeasti paikka muuttuu ja mihin suuntaan. Nopeus on myös vektorisuure. Sen etumerkki kertoo suunnan. Nopeuden itseisarvo $|v|$ on vauhti. Vauhti on nopeuden suuruus ilman etumerkkiä. Tasaisessa liikkeessä nopeus pysyy vakiona. Silloin paikka muuttuu yhtä paljon jokaisessa yhtä pitkässä aikavälissä.

<figure class="unit-photo"><img src="pics/fy4/highway-light-trails.webp" alt="Kaartuva moottoritie yöllä. Tiellä on punaisia ja valkoisia valoviivoja."><figcaption>Kuva on otettu yöllä pitkällä valotusajalla. Autojen valot näkyvät viivoina. Punaiset viivat ovat takavaloja ja valkoiset ajovaloja.</figcaption></figure>

Liike voidaan piirtää **$(t,x)$-kuvaajaksi**. Vaaka-akselilla on aika ja pystyakselilla paikka. Tasaisen liikkeen kuvaaja on suora. Suoran kulmakerroin on nopeus. Mitä suurempi kulmakertoimen itseisarvo on, sitä suurempi on kappaleen vauhti. Kulmakertoimen etumerkki kertoo liikkeen suunnan. Nouseva suora tarkoittaa liikettä positiiviseen suuntaan. Laskeva suora tarkoittaa liikettä negatiiviseen suuntaan. Vaakasuora suora tarkoittaa, että kappale on paikallaan. Kuvaaja ei ole kuva kappaleen reitistä. Nouseva viiva ei tarkoita ylämäkeä. Se tarkoittaa, että paikka kasvaa.

```pysahdy
Paikka–aika-kuvaajassa suora laskee oikealle. Liikkuuko kappale ylämäkeen, alamäkeen vai johonkin muuhun suuntaan?
---
Kuvaaja ei näytä reittiä. Laskeva suora tarkoittaa, että paikka $x$ pienenee. Silloin kappale liikkuu negatiiviseen suuntaan.
```

## Kaava: Keskinopeus ja tasaisen liikkeen yhtälö
Paikka voi muuttua määrän $\Delta x$ aikavälillä $\Delta t = t_2 - t_1$. Silloin keskinopeus on siirtymä jaettuna ajalla:
```kaavat
keskinopeus :: v_\text{k} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}
```
missä $v_\text{k}$ on keskinopeus (m/s), $\Delta x$ siirtymä (m), $\Delta t$ kulunut aika (s) ja $x_1$ ja $x_2$ paikat (m) hetkillä $t_1$ ja $t_2$. Vektorina nopeus kirjoitetaan $\overline{v}$ ja siirtymä $\Delta\overline{x}$. Suoralla käytetään niiden komponentteja $v$ ja $\Delta x$. Niiden etumerkki kertoo suunnan.

Tasaisessa liikkeessä keskinopeus on sama millä tahansa aikavälillä. Sitä kutsutaan nopeudeksi $v$. Epätasaisessa liikkeessä keskinopeus kertoo vain yhden asian. Se kertoo vakionopeuden, jolla sama siirtymä tehtäisiin samassa ajassa. Kappale voi olla hetkellä $t = 0$ paikassa $x_0$. Silloin kaavasta saadaan paikka ajan funktiona eli paikka millä tahansa hetkellä:
```latex
x = x_0 + v\,t
```
missä $x$ on paikka hetkellä $t$ (m), $x_0$ alkupaikka (m), $v$ nopeus (m/s) ja $t$ aika (s). Tämä on $(t,x)$-kuvaajan suoran yhtälö. Luku $x_0$ on kohta, jossa suora leikkaa paikka-akselin. Nopeus $v$ on suoran kulmakerroin.

<svg data-fig="graph-slope" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kahdesta (t,x)-kuvaajasta ilman lukuarvoja. Vasemmalla suora nousee alkupaikasta x0. Suoralta on valittu kaksi pistettä. Aikaväli Δt ja paikan muutos Δx muodostavat kolmion. Sen avulla nopeus v on Δx jaettuna Δt:lla. Oikealla on kolme suoraa samasta alkupaikasta. Nouseva suora on nopeus v suurempi kuin nolla. Vaakasuora suora on nopeus nolla. Laskeva suora on nopeus pienempi kuin nolla." style="max-width:100%;font-size:24px">
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
  <polyline points="340,180 490,246" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v < 0$</div></foreignObject>
  <circle cx="340" cy="180" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="297" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x_0$</div></foreignObject>
</svg>

Kulmakerroin lasketaan näin. Valitaan suoralta kaksi pistettä, jotka ovat kaukana toisistaan. Paikan muutos jaetaan ajan muutoksella. Mittauspisteistä piirretään kuvaaja. Siihen sovitetaan suora niin, että pisteet jäävät tasaisesti suoran molemmille puolille. Kulmakerroin lasketaan suoralta. Sitä ei lasketa kahdesta vierekkäisestä mittauspisteestä, koska jokaisessa mittauksessa on pieni virhe.

## Esimerkki
Hölkkääjän liike on tasaista. Kuvaajasta luetaan, että hän on hetkellä $t = 0$ paikassa $20\,\text{m}$. Hetkellä $t = 40\,\text{s}$ hän on paikassa $120\,\text{m}$. Mikä on hölkkääjän nopeus? Missä paikassa hän on hetkellä $t = 60\,\text{s}$?

<svg data-fig="jogger-graph" viewBox="0 0 600 340" role="img" aria-label="(t,x)-kuvaaja mittakaavassa. Suora nousee paikasta 20 metriä hetkellä 0 paikkaan 120 metriä hetkellä 40 sekuntia. Se jatkuu katkoviivana paikkaan 170 metriä hetkellä 60 sekuntia." style="max-width:100%;font-size:24px">
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

**Tunnetut ja kysytty.** Kuvaajasta luetaan kaksi pistettä: $(t_1;\, x_1) = (0\,\text{s};\, 20\,\text{m})$ ja $(t_2;\, x_2) = (40\,\text{s};\, 120\,\text{m})$.

Kysytään nopeutta $v$ ja paikkaa $x$ hetkellä $t = 60\,\text{s}$.

<!-- vaihe -->

**Periaate.** Hölkkääjän liike on tasaista. Siksi nopeus pysyy vakiona ja $(t, x)$-kuvaaja on suora. Nopeus on suoran kulmakerroin. Se on paikan muutos jaettuna ajan muutoksella. Kun nopeus tunnetaan, paikan saa näin: alkupaikkaan lisätään nopeuden ja ajan tulo.

<!-- vaihe -->

**Kaava ratkaistuna.** Nopeus ja paikka ratkaistaan ensin symbolein. Lukuja ei vielä käytetä:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
x &= x_1 + v\,t
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Paikat ovat metreinä ja ajat sekunteina. Siksi nopeus tulee suoraan yksikössä $\text{m/s}$. Muunnoksia ei tarvita. Alkupaikka on $x_1 = 20\,\text{m}$ hetkellä $t_1 = 0$. Siksi ajaksi $t$ kelpaa suoraan $60\,\text{s}$.

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

**Tulos.** Nopeus on $v = 2{,}5\,\text{m/s}$. Paikka hetkellä $60\,\text{s}$ on $x = 170\,\text{m}$. Kuvaajasta luetut kokonaisluvut $0\,\text{s}$, $40\,\text{s}$, $20\,\text{m}$ ja $120\,\text{m}$ tulkitaan tarkoiksi arvoiksi. Siksi tuloksia ei tarvitse pyöristää. Ne ovat tämän mallin tarkkoja arvoja.

<!-- vaihe -->

**Järkevyys.** Ensimmäisten $40\,\text{s}$:n aikana paikka kasvoi $100\,\text{m}$. Seuraavien $20\,\text{s}$:n aikana se kasvaa puolet siitä, $50\,\text{m}$. Paikka on $120\,\text{m} + 50\,\text{m} = 170\,\text{m}$. Tulos on sama. Nopeus $2{,}5\,\text{m/s}$ on noin $9\,\text{km/h}$. Se on hölkän vauhti. Nopeus on positiivinen, koska kuvaaja nousee.

## Yleinen virhekäsitys
$(t,x)$-kuvaaja ei ole kuva kappaleen reitistä. Nouseva viiva ei tarkoita ylämäkeä. Se tarkoittaa, että paikka kasvaa. Toinen virhe on pitää negatiivista nopeutta hitaana nopeutena. Etumerkki kertoo vain suunnan. Nopeus $-3\,\text{m/s}$ on suuruudeltaan suurempi kuin $+2\,\text{m/s}$. Kolmas virhe on päätellä paikasta nopeus. Kappale voi olla edellä ja liikkua silti hitaammin.

## Tiivistelmä
- Paikka $x$ kertoo, missä kappale on origoon nähden. Siirtymä $\Delta x = x_2 - x_1$ on paikan muutos. Sen etumerkki kertoo suunnan. Matka on reitin pituus. Matka ei ole negatiivinen.
- Nopeus $v = \Delta x / \Delta t$ on vektorisuure. Tasaisessa liikkeessä se on vakio. Paikka on $x = x_0 + v\,t$.
- Tasaisen liikkeen viiva $(t,x)$-kuvaajassa on suora. Kulmakerroin on nopeus. Sen etumerkki kertoo suunnan.
- Mittausaineistoon sovitetaan suora. Nopeus lasketaan suoralta valituista pisteistä, jotka ovat kaukana toisistaan.
- Edestakaisen liikkeen keskinopeus voi olla nolla, vaikka matka ei ole nolla.
