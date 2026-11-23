# Vetyatomin energiatasot ja Bohrin malli

> **Miksi** vetyä sisältävän lampun valo hajoaa hilassa vain neljäksi selvästi näkyväksi värilliseksi viivaksi, ja miksi juuri aallonpituuksille $656\,\text{nm}$, $486\,\text{nm}$, $434\,\text{nm}$ ja $410\,\text{nm}$?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pimennetyssä luokassa pöydällä on vetyä sisältävä purkausputki jännitelähteen telineessä. Putki hehkuu vaaleanpunaisen violettina. Sen edessä on telineessä hila, ja hilan takana valkoisella varjostimella näkyy tummaa taustaa vasten neljä erillistä värillistä viivaa: punainen, syaani, sininen ja violetti." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Vetyatomin energia on kvantittunut
Vetyatomissa on yksi protoni ja yksi elektroni. Atomin energia eli elektronin liike-energian ja sähköisen potentiaalienergian summa voi saada vain tiettyjä arvoja, **energiatasoja**. Tasot numeroidaan kokonaisluvulla $n = 1, 2, 3, \ldots$ Energian nollakohdaksi valitaan tilanne, jossa elektroni on levossa kaukana protonista eli irti atomista. Sidotun elektronin energia on siksi negatiivinen: elektronin irrottaminen vaatii energiaa.

Alin taso $n = 1$ on **perustila**, jonka energia on $-13{,}6\,\text{eV}$. Ylemmät tasot $n = 2, 3, \ldots$ ovat **viritystiloja**. Ne tihenevät ylöspäin ja lähestyvät nollaa. Energia, joka tarvitaan elektronin irrottamiseen perustilasta, on vedyn **ionisaatioenergia** $13{,}6\,\text{eV}$. Viritystilassa atomi pysyy tavallisesti vain noin $10^{-8}\,\text{s}$ ja palaa sitten alemmalle tasolle.

<svg data-fig="levels" viewBox="0 0 600 400" role="img" aria-label="Vetyatomin energiatasokaavio. Pystysuunnassa energia; tasot n = 2, 3, 4, 5 ja 6 sekä energia nolla ylimpänä ovat mittakaavassa, mutta tasojen n = 1 ja n = 2 väliä on lyhennetty, mikä on merkitty katkoviivalla. Tasojen energiat: n = 1: −13,6 eV, n = 2: −3,40 eV, n = 3: −1,51 eV, n = 4: −0,85 eV, ylimpänä 0 eV, jossa elektroni on irti atomista. Tasot tihenevät ylöspäin. Kaksi mustaa nuolta kuvaa siirtymiä tasoille n = 1 (Lymanin sarja, ultraviolettia), neljä värillistä nuolta siirtymiä tasoilta 3, 4, 5 ja 6 tasolle n = 2 (Balmerin sarja, näkyvää valoa: punainen, syaani, sininen ja violetti)." style="max-width:100%;font-size:24px">
  <line x1="26" y1="384" x2="26" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M26,34 L32,47 L20,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="36" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <path d="M18,350 L34,344 M18,360 L34,354" fill="none" stroke="#ffffff" stroke-width="6" stroke-linejoin="round"/>
  <path d="M18,350 L34,344 M18,360 L34,354" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="150" y1="70" x2="430" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 5"/>
  <line x1="150" y1="301" x2="430" y2="301" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="173" x2="430" y2="173" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="128" x2="430" y2="128" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="107" x2="430" y2="107" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="95.5" x2="430" y2="95.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="366" x2="430" y2="366" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="95" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n \to \infty$</div></foreignObject>
  <foreignObject x="70" y="82.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 5, 6$</div></foreignObject>
  <foreignObject x="95" y="116.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 4$</div></foreignObject>
  <foreignObject x="95" y="158.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 3$</div></foreignObject>
  <foreignObject x="95" y="286.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 2$</div></foreignObject>
  <foreignObject x="95" y="351.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 1$</div></foreignObject>
  <foreignObject x="440" y="55.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="116.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-0{,}85\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="158.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-1{,}51\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="286.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-3{,}40\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="351.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-13{,}6\,\text{eV}$</div></foreignObject>
  <line x1="176" y1="301" x2="176" y2="352" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M176,365 L169.5,351 L182.5,351 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="206" y1="173" x2="206" y2="352" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M206,365 L199.5,351 L212.5,351 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="216" y="318.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Lyman (UV)}$</div></foreignObject>
  <line x1="262" y1="173" x2="262" y2="286" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M262,300 L255,285 L269,285 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="302" y1="128" x2="302" y2="286" stroke="#1098ad" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M302,300 L295,285 L309,285 Z" fill="#1098ad" stroke-linejoin="round"/>
  <line x1="342" y1="107" x2="342" y2="286" stroke="#4263eb" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M342,300 L335,285 L349,285 Z" fill="#4263eb" stroke-linejoin="round"/>
  <line x1="382" y1="95.5" x2="382" y2="286" stroke="#7048e8" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M382,300 L375,285 L389,285 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="392" y="223.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Balmer (näkyvä)}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/hydrogen-discharge-tube.webp" alt="Pitkä lasiputki mustalla pohjalla. Putken kapea keskiosa hehkuu vaaleanpunaisena ja päät sinertävinä."><figcaption>Vetyä sisältävä kaasupurkausputki. Sähkövirta virittää vetyatomeja, ja kun ne siirtyvät alemmille energiatasoille, syntyy vedyn spektriviivojen valo.</figcaption></figure>

### Siirtymässä syntyy tai katoaa fotoni
Kun elektroni siirtyy ylemmältä tasolta alemmalle, atomin energia pienenee ja erotus lähtee yhtenä fotonina. Energia säilyy, joten fotonin energia on tasojen erotus. Koska tasoja on vain tiettyjä, myös erotuksia on vain tiettyjä: vety lähettää vain tiettyjä aallonpituuksia, ja sen spektri on viivaspektri.

Siirtymät samalle alemmalle tasolle muodostavat sarjan. Tasolle $n = 1$ päättyvät siirtymät (Lymanin sarja) ovat suuria energiaharppauksia, ja niiden fotonit ovat ultraviolettia. Tasolle $n = 2$ päättyvät siirtymät (Balmerin sarja) tuottavat vedyn neljä kirkasta näkyvää viivaa; seuraavat viivat ($397\,\text{nm}$, $389\,\text{nm}$, …) ovat himmeitä ja näkyvän valon violetilla reunalla, jossa silmä on epäherkkä. Tasolle $n = 3$ päättyvät (Paschenin sarja) ovat infrapunaa.

Absorptio on käänteinen tapahtuma. Atomi absorboi fotonin vain, jos fotonin energia on täsmälleen jonkin tasoparin erotus: elektroni siirtyy silloin ylemmälle tasolle. Muun energian fotoni menee atomin ohi absorboitumatta. Poikkeus on ionisaatio: fotoni, jonka energia on vähintään ionisaatioenergia, voi irrottaa elektronin, ja ylimääräinen energia jää vapaan elektronin liike-energiaksi. Kaikki tasoparien väliset siirtymät eivät kuitenkaan ole yhtä todennäköisiä, joten osa mahdollisista spektriviivoista on hyvin heikkoja.

<svg data-fig="absorption" viewBox="0 0 600 400" role="img" aria-label="Kolme tilannetta vierekkäin, energia-asteikko mittakaavassa. Kussakin on vetyatomin tasot n = 1, 2 ja 3 sekä katkoviivana energia nolla, ja elektroni on aluksi perustilassa n = 1. Vasemmalla tulee fotoni, jonka energia on 10,2 eV, täsmälleen tasojen 1 ja 2 erotus: fotoni absorboituu ja elektroni siirtyy tasolle 2. Keskellä fotonin energia on 11,0 eV, joka ei ole minkään tasoparin erotus: fotoni menee läpi, ja elektroni jää tasolle 1. Oikealla fotonin energia on 14,0 eV, enemmän kuin ionisaatioenergia 13,6 eV: elektroni irtoaa atomista." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-3-absorption.webp" x="1.2" y="0" width="597" height="406.7" preserveAspectRatio="none"/>
  <foreignObject x="32" y="263" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="32" y="100" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="32" y="69.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="32" y="39.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="33.5" y="321.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = 10{,}2\,\text{eV}$</div></foreignObject>
  <foreignObject x="27.5" y="357.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{absorboituu}$</div></foreignObject>
  <foreignObject x="233.5" y="321.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = 11{,}0\,\text{eV}$</div></foreignObject>
  <foreignObject x="240" y="357.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{menee läpi}$</div></foreignObject>
  <foreignObject x="433.5" y="321.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = 14{,}0\,\text{eV}$</div></foreignObject>
  <foreignObject x="452.5" y="357.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ionisoi}$</div></foreignObject>
</svg>

```pysahdy
Perustilassa oleva vetyatomi absorboi fotonin, jonka energia on $15{,}0\,\text{eV}$. Mitä atomille tapahtuu?
---
Atomi ionisoituu, koska $15{,}0\,\text{eV}$ on enemmän kuin ionisaatioenergia $13{,}6\,\text{eV}$. Vapaalle elektronille jää liike-energiaa $15{,}0\,\text{eV} - 13{,}6\,\text{eV} = 1{,}4\,\text{eV}$.
```

### Bohrin malli historiallisena välivaiheena
Tanskalainen Niels Bohr esitti vuonna 1913 mallin, jossa elektroni kiertää protonia ympyräradalla, mutta vain tietyillä sallituilla radoilla. Sallitulla radalla elektroni ei säteile, vaikka klassisen fysiikan mukaan kiertävän varauksen pitäisi menettää energiaa säteilynä. Valoa syntyy vain, kun elektroni siirtyy radalta toiselle, ja fotonin energia on ratojen energioiden erotus. Radan säde kasvaa kuten $n^2$: perustilan säde on noin $0{,}053\,\text{nm}$, radan $n = 2$ neljä kertaa ja radan $n = 3$ yhdeksän kertaa suurempi.

<svg data-fig="bohr" viewBox="0 0 600 360" role="img" aria-label="Bohrin malli vetyatomista. Keskellä ydin eli protoni, sen ympärillä elektronin sallitut ympyräradat n = 1, 2 ja 3, joiden säteet ovat mittakaavassa suhteessa 1 : 4 : 9. Elektroni siirtyy radalta n = 3 radalle n = 2, ja atomista lähtee fotoni, jonka energia hf on tasojen energioiden erotus E3 − E2." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-3-bohr.webp" x="1.2" y="0" width="597" height="366.9" preserveAspectRatio="none"/>
  <foreignObject x="197.5" y="127.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="435.5" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf$</div></foreignObject>
  <foreignObject x="398" y="221.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = E_3 - E_2$</div></foreignObject>
  <foreignObject x="163.5" y="213.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 2$</div></foreignObject>
  <foreignObject x="163.5" y="281.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 3$</div></foreignObject>
  <foreignObject x="16" y="25.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n = 1$</div></foreignObject>
  <foreignObject x="207" y="169.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$p^+$</div></foreignObject>
</svg>

Malli oli suuri edistysaskel. Siitä saadut vedyn energiatasot ovat samat, jotka spektriviivoista mitataan, ja se selitti vetyatomin koon ja ionisaatioenergian. Mallilla on kuitenkin rajansa. Se toimii vain atomeille ja ioneille, joissa on yksi elektroni, eikä se kerro, miksi jotkin spektriviivat ovat kirkkaampia kuin toiset. Elektronilla ei myöskään ole todellisuudessa rataa: luvussa *Aaltomekaaninen atomimalli ja orbitaalit* elektronin paikkaa kuvataan todennäköisyyksillä. Energiatasot säilyvät uudessakin mallissa, mutta kiertoradat jäävät pois.

<figure class="unit-photo"><img src="pics/fy8/orion-nebula.webp" alt="Kaasusumu avaruudessa: punertavia, violetteja ja ruskeita pilviä, joiden keskellä on kirkkaita tähtiä."><figcaption>Orionin sumu Hubble-avaruusteleskoopin kuvassa. Osa sumun hehkusta on vedyn punaista $656\,\text{nm}$:n valoa, joka syntyy, kun elektroni siirtyy tasolta $n = 3$ tasolle $n = 2$.</figcaption></figure>

## Kaava: Vetyatomin energiatasot ja siirtymän fotoni
Vetyatomin energiatasot ovat
```kaavat
elektronin energia vetyatomissa :: E_n = -\frac{13{,}6\,\text{eV}}{n^2}
```
missä $E_n$ on tason $n$ energia ja $n = 1, 2, 3, \ldots$ on tason järjestysluku. Lauseke on tässä annettu tieto, joka vastaa mitattua vedyn spektriä.

Kun elektroni siirtyy tasolta, jonka energia on $E_\text{y}$, alemmalle tasolle, jonka energia on $E_\text{a}$, syntyvän fotonin energia ja aallonpituus ovat
```latex
\begin{aligned}
hf &= E_\text{y} - E_\text{a} \\
\lambda &= \frac{hc}{E_\text{y} - E_\text{a}}
\end{aligned}
```
missä $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ on Planckin vakio, $f$ fotonin taajuus, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$ valon nopeus ja $\lambda$ aallonpituus. Absorptiossa samat kaavat antavat fotonin, joka nostaa elektronin tasolta $E_\text{a}$ tasolle $E_\text{y}$. Energiat lasketaan ensin elektronivoltteina, ja erotus muunnetaan jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

```pysahdy
Vetyatomin elektroni siirtyy tasolta $n = 5$ tasolle $n = 3$. Kuinka suuri on tasojen energiaero ja minkä aallonpituuden fotoni syntyy?
---
$E_5 = -13{,}6\,\text{eV}/25 = -0{,}544\,\text{eV}$ ja $E_3 = -13{,}6\,\text{eV}/9 = -1{,}511\,\text{eV}$, joten erotus on $0{,}967\,\text{eV}$. Aallonpituus on $\lambda = hc/\Delta E \approx 1240\,\text{eV nm}/0{,}967\,\text{eV} \approx 1{,}28 \cdot 10^{3}\,\text{nm}$, eli infrapunaa.
```

| Sarja | Alempi taso | Alue | $\lambda$ (nm) |
| --- | --- | --- | --- |
| Lyman | $n = 1$ | ultravioletti | $91{,}2$–$122$ |
| Balmer | $n = 2$ | näkyvä ja lähi-UV | $365$–$656$ |
| Paschen | $n = 3$ | infrapuna | $821$–$1876$ |

Kunkin sarjan pisin aallonpituus tulee siirtymästä lähimmältä ylemmältä tasolta ja lyhin eli sarjan raja siirtymästä, joka alkaa vapaasta elektronista. Koska tasot tihenevät ylöspäin, sarjan viivat tihenevät rajaa kohti.

<svg data-fig="spectrum" viewBox="0 0 600 300" role="img" aria-label="Vedyn näkyvä emissiospektri mittakaavassa aallonpituusakselilla 350–700 nm: tummalla pohjalla neljä viivaa, 410 nm violetti (siirtymä 6 → 2), 434 nm sininen (5 → 2), 486 nm syaani (4 → 2) ja 656 nm punainen (3 → 2). Katkoviiva kohdassa 365 nm on sarjan raja, siirtymä äärettömyydestä tasolle 2. Viivat tihenevät lyhyitä aallonpituuksia kohti." style="max-width:100%;font-size:24px">
  <rect x="40" y="80" width="430" height="66" rx="3" fill="#1f2933"/>
  <line x1="58" y1="84" x2="58" y2="142" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <rect x="413.5" y="82" width="6" height="62" fill="#c92a2a"/>
  <line x1="416.5" y1="70" x2="416.5" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="204.5" y="82" width="6" height="62" fill="#1098ad"/>
  <line x1="207.5" y1="70" x2="207.5" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="140.5" y="82" width="6" height="62" fill="#4263eb"/>
  <line x1="143.5" y1="70" x2="143.5" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="111" y="82" width="6" height="62" fill="#7048e8"/>
  <line x1="114" y1="70" x2="114" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="58" y1="70" x2="58" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$410$</div></foreignObject>
  <foreignObject x="121" y="13.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$434$</div></foreignObject>
  <foreignObject x="185" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$486$</div></foreignObject>
  <foreignObject x="394" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$656$</div></foreignObject>
  <foreignObject x="35.5" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$365$</div></foreignObject>
  <line x1="40" y1="160" x2="480" y2="160" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M492,160 L479,166 L479,154 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="101.5" y1="160" x2="101.5" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="79" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$400$</div></foreignObject>
  <line x1="224.5" y1="160" x2="224.5" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="202" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$500$</div></foreignObject>
  <line x1="347" y1="160" x2="347" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324.5" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$600$</div></foreignObject>
  <line x1="470" y1="160" x2="470" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$700$</div></foreignObject>
  <foreignObject x="498" y="145.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <line x1="114" y1="202" x2="128" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="105.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6 \to 2$</div></foreignObject>
  <line x1="143.5" y1="202" x2="204" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="181.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5 \to 2$</div></foreignObject>
  <line x1="207.5" y1="202" x2="280" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="257.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4 \to 2$</div></foreignObject>
  <line x1="416.5" y1="202" x2="416.5" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="394" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3 \to 2$</div></foreignObject>
  <line x1="58" y1="202" x2="52" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="29.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\infty \to 2$</div></foreignObject>
</svg>

```pysahdy
Kuinka suuri on vetyatomin tason $n = 5$ energia?
---
$E_5 = -\tfrac{13{,}6\,\text{eV}}{5^2} = -\tfrac{13{,}6\,\text{eV}}{25} \approx -0{,}54\,\text{eV}$
```

## Esimerkki
Vetylampun punainen viiva syntyy, kun vetyatomin elektroni siirtyy tasolta $n = 3$ tasolle $n = 2$. Laske syntyvän fotonin aallonpituus.

<!-- vaihe -->

**Tunnetut ja kysytty.** Ylempi taso $n = 3$, alempi taso $n = 2$, tasojen energiat $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$.

Kysytään fotonin aallonpituutta $\lambda$.

<!-- vaihe -->

**Periaate.** Energia säilyy: atomin energia pienenee tasojen erotuksen verran, ja juuri tämän energian vie mukanaan yksi fotoni. Fotonin energia on $hf = \tfrac{hc}{\lambda}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Merkitään fotonin energia tasojen erotukseksi ja ratkaistaan aallonpituus:
```latex
\begin{aligned}
&\frac{hc}{\lambda} = E_3 - E_2 \\
&\lambda = \frac{hc}{E_3 - E_2}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Tasojen energiat ovat elektronivoltteina, mutta $h$ on yksikössä $\text{J}\,\text{s}$. Energiaero muunnetaan siksi jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin energiaero ja sitten aallonpituus:
```latex
\begin{aligned}
&E_3 - E_2 \\
&= -\frac{13{,}6\,\text{eV}}{9} + \frac{13{,}6\,\text{eV}}{4} \\
&= 1{,}8889\,\text{eV} \\
&= 1{,}8889 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} \\
&= 3{,}0260 \cdot 10^{-19}\,\text{J} \\[6pt]
&hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \\
&\quad \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} \\
&= 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m} \\[6pt]
&\lambda = \frac{hc}{E_3 - E_2} \\
&= \frac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{3{,}0260 \cdot 10^{-19}\,\text{J}} \\
&= 6{,}5647 \cdot 10^{-7}\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Aallonpituus on $\lambda \approx 6{,}56 \cdot 10^{-7}\,\text{m} = 656\,\text{nm}$. Tulos ilmoitetaan kolmella merkitsevällä numerolla, koska perustilan energia $13{,}6\,\text{eV}$ tunnetaan kolmen numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Aallonpituus $656\,\text{nm}$ on punaista valoa, ja juuri sellainen viiva vedyn spektrissä näkyy. Fotonin energia $1{,}89\,\text{eV}$ on näkyvän valon fotonien välillä $1{,}7$–$3{,}3\,\text{eV}$. Pienin Balmerin sarjan energiaero antaa sarjan pisimmän aallonpituuden, kuten pitääkin.

## Yleinen virhekäsitys
Moni laskee fotonin energian yhden tason energiasta, esimerkiksi siirtymälle $4 \to 2$ arvosta $|E_4| = 0{,}85\,\text{eV}$. Silloin aallonpituudeksi tulisi noin $1460\,\text{nm}$, vaikka siirtymä tuottaa syaanin viivan $486\,\text{nm}$. Fotoni ei kanna tason energiaa vaan **tasojen erotuksen** $E_\text{y} - E_\text{a}$. Negatiivinen tason energia ei myöskään tarkoita, että energiaa puuttuisi: se kertoo, kuinka paljon energiaa elektronin irrottaminen vaatii.

Toinen virhe on pitää Bohrin ratoja todellisina kiertoratoina, joilla elektroni kiertää kuin planeetta. Bohrin malli antaa vedylle oikeat energiat, mutta elektronin rataa ei voi havaita, eikä sitä nykyisessä atomimallissa ole.

## Tiivistelmä
- Vetyatomin energia on kvantittunut: $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$. Perustila on $n = 1$, viritystilat $n \geq 2$, ja ionisaatioenergia perustilasta on $13{,}6\,\text{eV}$.
- Siirtymässä ylemmältä tasolta alemmalle syntyy fotoni, jonka energia on tasojen erotus: $hf = E_\text{y} - E_\text{a}$ ja $\lambda = \tfrac{hc}{E_\text{y} - E_\text{a}}$.
- Atomi absorboi vain fotonin, jonka energia on tasojen erotus, tai ionisoituu fotonista, jonka energia on vähintään ionisaatioenergia.
- Tasolle $n = 2$ päättyvät siirtymät (Balmerin sarja) antavat vedyn näkyvät viivat $656\,\text{nm}$, $486\,\text{nm}$, $434\,\text{nm}$ ja $410\,\text{nm}$; tasolle $n = 1$ päättyvät ovat ultraviolettia.
- Bohrin malli (1913) selitti vedyn spektrin sallituilla radoilla, mutta se toimii vain yhden elektronin atomeille. Aaltomekaaninen malli säilyttää energiatasot ja hylkää radat.
