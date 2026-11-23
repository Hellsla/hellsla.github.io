# Liike kuvaajina

> **Miksi** raitiovaunun nopeuskuvaajasta voi päätellä pysäkkien välisen matkan, vaikka kuvaajassa ei ole yhtään metriä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kaupungin katu kesäaamuna. Kadun keskellä kulkee raitiovaunu kiskoja pitkin oikealle, ja sen takana on liikeviivoja. Vasemmalla ja oikealla on lasiset raitiovaunupysäkit. Vaunun yllä kulkee ajojohdin pylväiden välissä. Taustalla on kerrostaloja ja koivuja. Kuvassa ei ole tekstiä eikä ihmisiä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-liike-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Liike kuvataan aina valitussa koordinaatistossa: suora $x$-akseli, origo, positiivinen suunta ja kello. **Paikka** $x$ kertoo, missä kappale on, **siirtymä** $\Delta x$ paikan muutoksen ja **nopeus** $v$ sen, kuinka nopeasti ja mihin suuntaan paikka muuttuu. **Kiihtyvyys** $a$ kertoo, kuinka nopeasti nopeus muuttuu. Siirtymän, nopeuden ja kiihtyvyyden etumerkki kertoo suunnan. Matka on reitin pituus, eikä se ole koskaan negatiivinen.

Sama liike voidaan esittää kolmena kuvaajana: $(t,x)$, $(t,v)$ ja $(t,a)$. Kuvaajien välillä liikutaan kahdella tavalla. Alaspäin: kuvaajan **kulmakerroin** on seuraavan suureen arvo, eli $(t,x)$-kuvaajan kulmakerroin on nopeus ja $(t,v)$-kuvaajan kulmakerroin kiihtyvyys. Ylöspäin: kuvaajan ja aika-akselin välinen **pinta-ala** on edellisen suureen muutos, eli $(t,v)$-kuvaajan pinta-ala on siirtymä.

```pysahdy
Mitä $(t,x)$-kuvaajan kulmakerroin kertoo ja mitä $(t,v)$-kuvaajan pinta-ala?
---
$(t,x)$-kuvaajan kulmakerroin on nopeus ja $(t,v)$-kuvaajan pinta-ala siirtymä.
```

<svg data-fig="kartta" viewBox="0 0 380 724" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Katso, mitä tehtävässä tiedetään tai mikä kuvaaja on annettu. Vakionopeus: paikka ajan mukaan on x on x nolla plus v t. Kiihtyvyys on vakio: nopeus ajan mukaan on v on v nolla plus a t. Kiihtyvyys on vakio ja matkaa kysytään: paikka on x nolla plus v nolla t plus puolet a t toiseen. Vakiokiihtyvyys, a ei tiedossa: keskinopeus, jolloin siirtymä on alku- ja loppunopeuden keskiarvo kertaa aika. Nopeus paikkakuvaajasta: kulmakerroin, v on delta x per delta t. Kiihtyvyys nopeuskuvaajasta: kulmakerroin, a on delta v per delta t. Matka nopeuskuvaajasta: kuvaajan ja aika-akselin väliin jäävä pinta-ala." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="680" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{kuvaaja vai kaava? katso, mitä tiedät}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{vakionopeus}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{paikka ajan mukaan}$</div></foreignObject>
  <rect x="246" y="142" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="144" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$x = x_0 + vt$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kiihtyvyys on vakio}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{nopeus ajan mukaan}$</div></foreignObject>
  <rect x="246" y="228" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="230" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = v_0 + at$</div></foreignObject>
  <line x1="14" y1="321" x2="30" y2="321" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kiihtyvyys on vakio, matka?}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{paikka ajan mukaan}$</div></foreignObject>
  <rect x="142" y="343" width="220" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="146" y="346" width="212" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$x = x_0 + v_0 t + \tfrac12 at^2$</div></foreignObject>
  <line x1="14" y1="422" x2="30" y2="422" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="386" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="396.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{vakiokiihtyvyys, a ei tiedossa}$</div></foreignObject>
  <line x1="40" y1="426" x2="362" y2="426" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="431" width="154" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{keskinopeus}$</div></foreignObject>
  <rect x="212" y="430" width="150" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="432" width="142" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta x = \tfrac{v_0 + v}{2}\,t$</div></foreignObject>
  <line x1="14" y1="508" x2="30" y2="508" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="472" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="482.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{nopeus paikkakuvaajasta}$</div></foreignObject>
  <line x1="40" y1="512" x2="362" y2="512" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="517" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kulmakerroin}$</div></foreignObject>
  <rect x="238" y="516" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="518" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = \Delta x/\Delta t$</div></foreignObject>
  <line x1="14" y1="594" x2="30" y2="594" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="558" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="568.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kiihtyvyys nopeuskuvaajasta}$</div></foreignObject>
  <line x1="40" y1="598" x2="362" y2="598" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="603" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kulmakerroin}$</div></foreignObject>
  <rect x="238" y="602" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="604" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$a = \Delta v/\Delta t$</div></foreignObject>
  <line x1="14" y1="680" x2="30" y2="680" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="644" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="654.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{matka nopeuskuvaajasta}$</div></foreignObject>
  <line x1="40" y1="684" x2="362" y2="684" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="689" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kuvaajan alla}$</div></foreignObject>
  <rect x="246" y="688" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="690" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\text{pinta-ala}$</div></foreignObject>
</svg>

Kokeen liiketehtävä alkaa siitä, että valitset koordinaatiston ja tunnistat liikkeen lajin: onko nopeus vakio vai kiihtyvyys vakio? Vasta sitten kirjoitat yhtälön.

Tästä saadaan vastaus alun kysymykseen. Nopeus kertoo, montako metriä vaunu kulkee sekunnissa, joten nopeuden ja ajan tulo on metrejä. $(t,v)$-kuvaajan alle jäävä pinta-ala on juuri tämä tulo laskettuna yhteen koko matkalta, siis siirtymä. Tutki-tehtävän raitiovaunu kulki pysäkiltä toiselle $450\,\text{m}$.

## Kaava: Liikkeen yhtälöt ja kuvaajat

### Tasainen liike

Keskinopeus on siirtymä jaettuna siihen kuluneella ajalla:

```kaavat
keskinopeus :: \overline{v}_\text{k} = \frac{\Delta\overline{x}}{\Delta t}
```

missä $\Delta\overline{x}$ on siirtymä ($\text{m}$) ja $\Delta t$ kulunut aika ($\text{s}$). Suoraviivaisessa liikkeessä riittää etumerkillinen siirtymä $\Delta x = x_2 - x_1$, ja keskinopeus on $v_\text{k} = \tfrac{\Delta x}{\Delta t}$. Kun nopeus $v$ on vakio ja kappale on hetkellä $t = 0$ paikassa $x_0$,

```latex
x = x_0 + v\,t
```

Tämä on $(t,x)$-kuvaajan suora: $x_0$ on leikkauskohta paikka-akselilla ja $v$ kulmakerroin. Paikka on suoraan verrannollinen aikaan vain, kun $x_0 = 0$.

### Tasaisesti kiihtyvä liike

Kiihtyvyys on nopeuden muutos aikaa kohti:

```kaavat
keskikiihtyvyys :: \overline{a}_\text{k} = \frac{\Delta\overline{v}}{\Delta t}
```

missä $\Delta\overline{v}$ on nopeuden muutos ($\text{m/s}$), $\Delta t$ kulunut aika ($\text{s}$) ja $\overline{a}_\text{k}$ keskikiihtyvyys ($\text{m/s}^2$). Suoraviivaisessa liikkeessä riittää etumerkillinen kiihtyvyys $a = \tfrac{\Delta v}{\Delta t}$, ja vakiokiihtyvyydellä keskikiihtyvyys on sama kuin hetkellinen.

Kun kiihtyvyys on vakio ja liike suoraviivaista, nopeus ja paikka hetkellä $t$ ovat

```kaavat
nopeus tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: v = v_0 + a\,t
paikka tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
```

missä $v_0$ on alkunopeus ($\text{m/s}$) ja $a$ kiihtyvyys ($\text{m/s}^2$). Vauhti kasvaa, kun $a$ ja $v$ ovat samansuuntaiset, ja pienenee, kun ne ovat vastakkaissuuntaiset. Vapaassa pudotuksessa $a = g = 9{,}81\,\text{m/s}^2$ alaspäin, kun ilmanvastus on pieni.

```pysahdy
Kappale liikkuu positiiviseen suuntaan ja sen kiihtyvyys on negatiivinen. Kasvaako vai pieneneekö vauhti?
---
Vauhti pienenee, koska nopeus ja kiihtyvyys ovat vastakkaissuuntaiset.
```

### Kulmakerroin ja pinta-ala

Kaarevan $(t,x)$-kuvaajan hetkellinen nopeus on tangentin kulmakerroin $k$. Kahden käyrän pisteen kautta laskettu suhde on keskinopeus. Siirtymä on $(t,v)$-kuvaajan ja aika-akselin välinen pinta-ala, ja akselin alapuolinen osa lasketaan negatiivisena.

```pysahdy
Osa $(t,v)$-kuvaajasta on aika-akselin alapuolella. Miten tämä osa vaikuttaa siirtymään?
---
Alapuolinen pinta-ala lasketaan negatiivisena, joten se pienentää siirtymää.
```

<svg data-fig="kuvaajat" viewBox="0 0 440 650" role="img" aria-label="Kaavakuva yhdestä liikkeestä kahtena kuvaajana, joilla on sama aika-akseli. Alhaalla nopeuden kuvaaja: nopeus kasvaa nollasta tasaisesti hetkeen t1, pysyy vakiona hetkeen t2 ja pienenee tasaisesti nollaan hetkellä t3. Kuvaajan alle jäävä alue on väritetty vihreäksi, ja sen pinta-ala on siirtymä Δx. Ylhäällä paikan kuvaaja: ensin ylöspäin kaartuva käyrä, sitten nouseva suora ja lopuksi käyrä, joka loivenee vaakasuoraksi. Paikka kasvaa koko liikkeen ajan yhteensä Δx. Käyrän pisteeseen P on piirretty sininen tangentti, jonka kulmakerroin k on nopeus v_P; sama arvo on merkitty alempaan kuvaajaan." style="max-width:100%;font-size:21px">
  <line x1="49" y1="280" x2="370" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,280 L369,286 L369,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="281" x2="50" y2="60" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,48 L56,61 L44,61 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="127.5" y1="280" x2="127.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="244" y1="280" x2="244" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="321" y1="280" x2="321" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="267.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="40" y="19.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$x$</div></foreignObject>
  <line x1="49" y1="590" x2="370" y2="590" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,590 L369,596 L369,584 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="591" x2="50" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,388 L56,401 L44,401 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="127.5" y1="590" x2="127.5" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="244" y1="590" x2="244" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="321" y1="590" x2="321" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="577.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="40" y="359.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$v$</div></foreignObject>
  <polygon points="50,590 127.5,451.5 244,451.5 321,590" fill="#b2f2bb" fill-opacity="0.8"/>
  <line x1="127.5" y1="241" x2="127.5" y2="451.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="244" y1="124.5" x2="244" y2="451.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="321" y1="85.5" x2="321" y2="590" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="50,280 52.5,280 54.5,280 57,279.5 59,279.5 61.5,279 63.5,279 66,278.5 68,278 70.5,277.5 72.5,276.5 75,276 77,275 79.5,274.5 81.5,273.5 84,272.5 86,271.5 88.5,270.5 90.5,269.5 93,268 95,267 97.5,265.5 99.5,264 102,262.5 104,261 106.5,259.5 109,257.5 111,256 113.5,254 115.5,252 118,250 120,248 122.5,246 124.5,244 127,242 129,239.5 131.5,237 133.5,235 136,232.5 138,230.5 140.5,228 142.5,226 145,223.5 147,221.5 149.5,219 151.5,217 154,214.5 156,212.5 158.5,210 161,207.5 163,205.5 165.5,203 167.5,201 170,198.5 172,196.5 174.5,194 176.5,192 179,189.5 181,187.5 183.5,185 185.5,183 188,180.5 190,178 192.5,176 194.5,173.5 197,171.5 199,169 201.5,167 203.5,164.5 206,162.5 208,160 210.5,158 213,155.5 215,153.5 217.5,151 219.5,149 222,146.5 224,144 226.5,142 228.5,139.5 231,137.5 233,135 235.5,133 237.5,130.5 240,128.5 242,126 244.5,124 246.5,121.5 249,119.5 251,117.5 253.5,115.5 255.5,113.5 258,111.5 260,109.5 262.5,108 264.5,106 267,104.5 269.5,103 271.5,101.5 274,100 276,99 278.5,97.5 280.5,96.5 283,95 285,94 287.5,93 289.5,92 292,91 294,90.5 296.5,89.5 298.5,89 301,88 303,87.5 305.5,87 307.5,86.5 310,86.5 312,86 314.5,86 316.5,85.5 319,85.5 321,85.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="321,85.5 352,85.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="50,590 127.5,451.5 244,451.5 321,590 352,590" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90.5,270.5 158.5,223" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <line x1="104" y1="261" x2="104" y2="493" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="104" cy="261" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="73" y="244.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$P$</div></foreignObject>
  <foreignObject x="164.5" y="238.5" width="52" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px;color:#1971c2">$k = v_\text{P}$</div></foreignObject>
  <circle cx="104" cy="493" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="62" y="466.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$v_\text{P}$</div></foreignObject>
  <foreignObject x="170.5" y="515" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
  <line x1="350" y1="280" x2="356" y2="280" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="350" y1="85.5" x2="356" y2="85.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="356" y1="280" x2="356" y2="85.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="364" y="170.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
  <foreignObject x="112.5" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_1$</div></foreignObject>
  <foreignObject x="229" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_2$</div></foreignObject>
  <foreignObject x="306" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_3$</div></foreignObject>
  <foreignObject x="21" y="597.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
  <foreignObject x="21" y="287.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
</svg>

Tasaisesti kiihtyvässä liikkeessä nopeus muuttuu ajassa $t$ ($\text{s}$) tasaisesti alkunopeudesta $v_0$ loppunopeuteen $v$ ($\text{m/s}$). Silloin $(t,v)$-kuvaaja on suora, ja sen alle jäävä alue on puolisuunnikas.

<svg data-fig="puolisuunnikas" viewBox="0 0 440 330" role="img" aria-label="Kaavakuva tasaisesti kiihtyvän liikkeen nopeuden kuvaajasta, ei lukuarvoja. Nopeus kasvaa tasaisesti alkunopeudesta v0 hetkellä 0 nopeuteen v hetkellä t, joten kuvaaja on nouseva suora. Kuvaajan ja aika-akselin väliin jää vihreä puolisuunnikas, jonka pinta-ala on siirtymä Δx. Puolisuunnikkaan yhdensuuntaiset sivut ovat v0 ja v, ja niiden välimatka on t." style="max-width:100%;font-size:21px">
  <line x1="59" y1="280" x2="370" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,280 L369,286 L369,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="281" x2="60" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M60,28 L66,41 L54,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="317" y1="280" x2="317" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="267.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="50" y="-0.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$v$</div></foreignObject>
  <polygon points="60,280 60,206 317,94.5 317,280" fill="#b2f2bb" fill-opacity="0.8"/>
  <line x1="317" y1="94.5" x2="317" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="60" y1="94.5" x2="317" y2="94.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="60,206 317,94.5" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="60" cy="206" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="317" cy="94.5" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="18" y="193.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$v_0$</div></foreignObject>
  <foreignObject x="29" y="82" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$v$</div></foreignObject>
  <foreignObject x="307.5" y="291.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="31" y="287.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
  <foreignObject x="173.5" y="223" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
</svg>

```johda
Kappale liikkuu tasaisesti kiihtyvästi suoraa rataa, ja sen nopeus muuttuu ajassa $t$ alkunopeudesta $v_0$ nopeuteen $v$. Johda kappaleen siirtymä $\Delta x$ nopeuksien $v_0$ ja $v$ sekä ajan $t$ avulla.
---
Siirtymä on $\Delta x = x - x_0$. Paikka tasaisesti kiihtyvässä suoraviivaisessa liikkeessä antaa sen alkunopeuden, kiihtyvyyden ja ajan avulla:

$$\Delta x = x - x_0 = v_0\,t + \tfrac{1}{2}\,a\,t^2$$

Kysytyssä tuloksessa ei ole kiihtyvyyttä, joten se lausutaan nopeuksien avulla. Nopeus tasaisesti kiihtyvässä suoraviivaisessa liikkeessä on $v = v_0 + a\,t$, joten

$$a\,t = v - v_0$$

Kirjoitetaan viimeinen termi muotoon $\tfrac{1}{2}\,(a\,t)\,t$ ja sijoitetaan siihen $a\,t$:

$$\Delta x = v_0\,t + \tfrac{1}{2}\,(v - v_0)\,t$$

Puretaan sulkeet ja yhdistetään alkunopeuden termit:

$$\Delta x = \tfrac{1}{2}\,v_0\,t + \tfrac{1}{2}\,v\,t = \frac{v_0 + v}{2}\,t$$

Sama tulos saadaan $(t,v)$-kuvaajan pinta-alana: puolisuunnikkaan yhdensuuntaiset sivut ovat $v_0$ ja $v$, korkeus on $t$, ja ala on sivujen keskiarvo kertaa korkeus. Tasaisesti kiihtyvässä liikkeessä keskinopeus on siis alku- ja loppunopeuden keskiarvo.
```

### Kaksi kappaletta ja mittausaineisto

Kahden kappaleen paikat kirjoitetaan samassa koordinaatistossa, ja ne kohtaavat, kun

```latex
x_\text{A}(t) = x_\text{B}(t)
```

$(t,x)$-kuvaajassa kohtaaminen on viivojen leikkauspiste. Ylempänä oleva viiva tarkoittaa suurempaa paikkakoordinaattia. Kun takana oleva kappale on aluksi hitaampi ja kiihtyy, välimatka on suurimmillaan silloin, kun nopeudet ovat yhtä suuret.

Mittauspisteisiin sovitetaan suora tai toisen asteen polynomi $x = A\,t^2 + B\,t + C$. Polynomin kertoimesta saadaan kiihtyvyys $a = 2A$.

## Yleisiä virheitä {Virheet}

- **$(t,x)$-kuvaaja luetaan kuvana radasta.** Nouseva viiva tarkoittaa, että paikka kasvaa, ei ylämäkeä.
- **Nopeus luetaan $x : t$, kun pitää lukea $\Delta x : \Delta t$.** Alkupaikka ei ole nopeutta.
- **Kulmakerroin kahdesta vierekkäisestä mittauspisteestä.** Lue se sovitetulta suoralta tai tangentilta kahdesta kaukana toisistaan olevasta pisteestä.
- **Negatiivinen kiihtyvyys luetaan aina hidastumiseksi.** Vauhti pienenee vain, kun kiihtyvyys ja nopeus ovat vastakkaissuuntaiset.
- **Lakipisteessä kiihtyvyys on nolla.** Nopeus on hetken nolla, mutta kiihtyvyys on yhä $g$ alaspäin.
- **$(t,v)$-kuvaajien leikkauspiste luetaan kohtaamiseksi.** Siinä nopeudet ovat yhtä suuret; kohtaamisessa yhtä suuria ovat paikat.
- **Yksiköt sekaisin.** Muunna ennen sijoitusta sijoittamalla: $$
\begin{aligned}
&72\,\text{km/h} \\
&= \dfrac{72 \cdot 1000\,\text{m}}{3600\,\text{s}} \\
&= 20\,\text{m/s}
\end{aligned}
$$.

## Kertaa tarvittaessa {Kertaa}

- Tasainen liike, $x = x_0 + vt$ ja yksikkömuunnokset: [*Tasainen liike – nopeus, paikka ja kuvaajat*](fy1-5.html).
- Paikka, siirtymä, keskinopeus ja $(t,x)$-kuvaajan kulmakerroin: [*Paikka, nopeus ja tasainen liike kuvaajina*](fy4-1.html).
- Kiihtyvyys, tangentti, pinta-ala ja vapaa pudotus: [*Kiihtyvyys ja tasaisesti kiihtyvä liike*](fy4-2.html).
- Kohtaaminen, ohitus ja suurin välimatka: [*Kahden kappaleen liikkeiden vertailu*](fy4-12.html).
- Suoran sovittaminen ja kulmakerroin aineistosta: [*Graafinen esitys ja suoran sovittaminen*](fy1-4.html). Mittausepävarmuus: [*Mittaaminen ja mittauksen luotettavuus*](fy1-3.html).
