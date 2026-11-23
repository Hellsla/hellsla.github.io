# Hajoamislaki ja puoliintumisaika

> **Miksi** sairaalan teknetiumvalmisteen aktiivisuus puolittuu aina noin kuudessa tunnissa, vaikka kukaan ei voi ennustaa, milloin yksittäinen ydin hajoaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: sairaalan isotooppilaboratorio. Puupöydällä on paksuseinäinen lyijysuoja, jonka sisällä on pieni lasipullo radioaktiivista lääkettä. Pullon yllä leijuu suurennettuna joukko ytimiä: osa on oransseja hajoamattomia, osa harmaita renkaita eli jo hajonneita, ja kahdesta lähtee juuri säde. Vieressä on säteilymittari, jonka anturi osoittaa pulloa ja jonka viisari värähtää. Seinällä on kello." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-9-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

<figure class="unit-photo"><img src="pics/fy8/cloud-chamber-radon.webp" alt="Mustalla pohjalla paljon lyhyitä, paksuja valkoisia jälkiä satunnaisissa kohdissa ja suunnissa."><figcaption>Radonin hajoamisia sumukammiossa. Jokainen paksu jälki on yhden ytimen lähettämä alfahiukkanen. Ei voi ennustaa, mikä ydin hajoaa seuraavaksi, mutta suuressa joukossa hajoamisia tapahtuu tasaisesti.</figcaption></figure>

### Yksittäisen ytimen hajoaminen on satunnaista
Radioaktiivinen ydin hajoaa ja muuttuu toiseksi ytimeksi (luku *Atomiydin ja radioaktiivinen hajoaminen*), mutta hajoamishetkeä ei voi ennustaa. Kahdesta samanlaisesta ytimestä toinen voi hajota heti ja toinen vasta vuosien päästä. Ennustaa voi vain sen, kuinka todennäköisesti ydin hajoaa tietyn ajan kuluessa. Tämä todennäköisyys on sama kaikille saman isotoopin ytimille, eikä se käytännössä riipu ympäristön lämpötilasta, paineesta tai kemiallisista sidoksista. Se ei riipu myöskään ytimen iästä: ydin ei vanhene. Pitkään hajoamatta säilynyt ydin hajoaa seuraavan sekunnin aikana yhtä todennäköisesti kuin juuri syntynyt.

```pysahdy
Näytteessä on aluksi $8000$ ydintä, ja puoliintumisaika on $T_{1/2}$. Yksittäinen ydin on säilynyt hajoamatta kaksi puoliintumisaikaa. Millä todennäköisyydellä se hajoaa seuraavan puoliintumisajan aikana? Päättele näytteen ytimien määristä.
---
Kahden puoliintumisajan jälkeen näytteessä on $8000 \cdot \left(\tfrac{1}{2}\right)^2 = 2000$ ydintä. Kolmannen puoliintumisajan aikana niistä hajoaa puolet eli $1000$. Todennäköisyys on $\tfrac{1000}{2000} = 0{,}50$, sama kuin juuri syntyneellä ytimellä.
```

### Suuri joukko ytimiä käyttäytyy säännöllisesti
Koska jokaisella ytimellä on sama hajoamistodennäköisyys, tietyssä ajassa hajoaa aina suunnilleen sama *osuus* jäljellä olevista ytimistä. Kuvassa samoista sadasta ytimestä on yhden puoliintumisajan jälkeen jäljellä noin puolet ja kahden jälkeen noin neljäsosa, mutta hajonneet ytimet ovat sattumanvaraisissa kohdissa. Pienessä joukossa sattuma näkyy: osuus voi poiketa puolesta selvästi. Tavallisessa näytteessä on kuitenkin esimerkiksi $10^{15}$ ydintä, ja silloin suhteelliset poikkeamat ovat niin pieniä, ettei niitä huomaa.

<svg data-fig="ydin" viewBox="0 0 600 330" role="img" aria-label="Kolme ruudukkoa vierekkäin: samat 100 radioaktiivista ydintä kolmella hetkellä. Hajoamaton ydin on oranssi täysi ympyrä, hajonnut ydin harmaa rengas. Hetkellä t = 0 kaikki 100 ovat hajoamattomia. Yhden puoliintumisajan kuluttua hajoamattomia on 52 ja kahden puoliintumisajan kuluttua 28. Hajonneet ytimet ovat sattumanvaraisissa kohdissa ruudukkoa, eikä ytimen paikka tai ikä ennusta sen hajoamista." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-9-ydin.webp" x="10.7" y="2.4" width="568.7" height="322.3" preserveAspectRatio="none"/>
  <foreignObject x="82.5" y="15.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 0$</div></foreignObject>
  <foreignObject x="70" y="237.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$N = 100$</div></foreignObject>
  <foreignObject x="253.5" y="15.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = T_{1/2}$</div></foreignObject>
  <foreignObject x="266" y="237.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$N = 52$</div></foreignObject>
  <foreignObject x="437.5" y="15.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 2T_{1/2}$</div></foreignObject>
  <foreignObject x="456" y="237.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$N = 28$</div></foreignObject>
  <foreignObject x="82" y="285.5" width="436" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{oranssi: hajoamaton,\ harmaa: hajonnut}$</div></foreignObject>
</svg>

### Puoliintumisaika
**Puoliintumisaika** $T_{1/2}$ on aika, jonka kuluessa puolet näytteen hajoamattomista ytimistä hajoaa. Seuraavan puoliintumisajan aikana hajoaa puolet *jäljellä olevista*, joten kahden puoliintumisajan kuluttua jäljellä on neljäsosa eikä mitään. Puoliintumisaika on isotoopin ominaisuus, joka ei riipu näytteen koosta eikä siitä, milloin ajanotto aloitetaan. Taulukossa on puoliintumisaikoja; yksikkö $\text{d}$ on vuorokausi ja $\text{a}$ vuosi.

```pysahdy
Näytteessä on aluksi $8000$ hajoamatonta ydintä ja sen puoliintumisaika on $2\,\text{h}$. Noin kuinka monta hajoamatonta ydintä on jäljellä $6\,\text{h}$:n kuluttua?
---
$6\,\text{h}$ on kolme puoliintumisaikaa, joten määrä puolittuu kolme kertaa: $8000 \cdot \left(\tfrac{1}{2}\right)^3 = 1000$.
```

| Isotooppi | $T_{1/2}$ | Missä |
| --- | --- | --- |
| barium-$137\text{m}$ | $2{,}55\,\text{min}$ | koulun hajoamiskoe |
| fluori-18 | $110\,\text{min}$ | PET-kuvaus |
| teknetium-$99\text{m}$ | $6{,}01\,\text{h}$ | isotooppikuvaus |
| radon-222 | $3{,}82\,\text{d}$ | sisäilman radon |
| jodi-131 | $8{,}02\,\text{d}$ | kilpirauhashoito |
| cesium-137 | $30{,}1\,\text{a}$ | Tšernobylin laskeuma |
| hiili-14 | $5700\,\text{a}$ | radiohiiliajoitus |
| uraani-238 | $4{,}47 \cdot 10^{9}\,\text{a}$ | kallioperä |

Lähde: kirjallisuusarvot NNDC NuDat 3 -tietokannasta (Brookhaven National Laboratory), pyöristetty kolmeen merkitsevään numeroon. Jodi-131:lle käytetään vakiintunutta arvoa $8{,}02\,\text{d}$. Eri arvioinneissa sen puoliintumisaika on noin $8{,}021$–$8{,}025\,\text{d}$, joten pyöristys voi antaa myös $8{,}03\,\text{d}$. Tämän luvun laskuissa käytetään arvoa $8{,}02\,\text{d}$; tarkempi arvo muuttaisi tuloksia vain kolmannessa merkitsevässä numerossa.

<figure class="unit-photo"><img src="pics/fy8/geiger-counter.webp" alt="Vanha beigenvärinen säteilymittari valkoisella pöydällä: laatikossa on viisarinäyttö ja säätönuppi, ja kierrejohdolla siihen on liitetty pyöreä anturi kädensijassa."><figcaption>Geigerin ja Müllerin mittari laskee anturiin osuvia ionisoivia hiukkasia. Kun mittari pidetään samassa kohdassa, pulssitaajuus on taustan vähentämisen jälkeen verrannollinen lähteen aktiivisuuteen.</figcaption></figure>

### Aktiivisuus
Näytteen **aktiivisuus** $A$ on siinä tapahtuvien hajoamisten määrä aikayksikössä. Sen yksikkö on becquerel: $1\,\text{Bq}$ on yksi hajoaminen sekunnissa eli $1\,\tfrac{1}{\text{s}}$. Koska jokainen ydin hajoaa yhtä todennäköisesti, aktiivisuus on suoraan verrannollinen hajoamattomien ytimien määrään: kun ytimistä on jäljellä puolet, myös aktiivisuus on puolittunut. Säteilymittari ei mittaa aktiivisuutta suoraan, vaan se laskee pulsseja anturiin osuvista ionisoivista hiukkasista ja fotoneista. Pulssimäärä on verrannollinen aktiivisuuteen, mutta siihen lisätään aina myös ympäristön **taustasäteily**.

## Kaava: Hajoamislaki

### Puoliintumisaika lain muodossa
Jos näytteessä on alussa $N_0$ hajoamatonta ydintä, jokainen puoliintumisaika kertoo määrän luvulla $\tfrac{1}{2}$. Ajan $t$ kuluttua hajoamattomia ytimiä on
```latex
N = N_0 \left(\frac{1}{2}\right)^{t/T_{1/2}}
```
missä $N$ on hajoamattomien ytimien määrä hetkellä $t$, $N_0$ niiden määrä hetkellä $t = 0$ ja $T_{1/2}$ puoliintumisaika. Eksponentti $\tfrac{t}{T_{1/2}}$ kertoo, kuinka monta puoliintumisaikaa on kulunut, eikä sen tarvitse olla kokonaisluku. Ajalla $t$ ja puoliintumisajalla on oltava sama yksikkö. Laki kuvaa suuren ydinjoukon käyttäytymistä: pienessä joukossa todellinen $N$ poikkeaa siitä satunnaisesti.

<svg data-fig="kuvaaja" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja mittakaavassa: hajoamattomien ytimien määrä N ajan funktiona. Vaaka-akselilla aika puoliintumisaikoina nollasta viiteen, pystyakselilla N, asteikko nollasta alkumäärään N nolla neljäsosin. Käyrä alkaa arvosta N nolla ja laskee yhä loivemmin. Katkoviivat näyttävät, että yhden puoliintumisajan kohdalla jäljellä on puolet, kahden kohdalla neljäsosa ja kolmen kohdalla kahdeksasosa alkumäärästä. Käyrä ei koskaan saavuta nollaa." style="max-width:100%;font-size:24px">
  <line x1="178" y1="312" x2="178" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256.5" y1="312" x2="256.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="334.5" y1="312" x2="334.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="412.5" y1="312" x2="412.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="491" y1="312" x2="491" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="253" x2="530" y2="253" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="194.5" x2="530" y2="194.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="135.5" x2="530" y2="135.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="77" x2="530" y2="77" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="544" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M556,312 L543,318 L543,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="178" y1="312" x2="178" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="149" y="321.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_{1/2}$</div></foreignObject>
  <line x1="256.5" y1="312" x2="256.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="221.5" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2T_{1/2}$</div></foreignObject>
  <line x1="334.5" y1="312" x2="334.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="299.5" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3T_{1/2}$</div></foreignObject>
  <line x1="412.5" y1="312" x2="412.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="377.5" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4T_{1/2}$</div></foreignObject>
  <line x1="491" y1="312" x2="491" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="456" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5T_{1/2}$</div></foreignObject>
  <line x1="93" y1="253" x2="100" y2="253" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="238.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{4}N_0$</div></foreignObject>
  <line x1="93" y1="194.5" x2="100" y2="194.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="180" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{2}N_0$</div></foreignObject>
  <line x1="93" y1="135.5" x2="100" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="121" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{3}{4}N_0$</div></foreignObject>
  <line x1="93" y1="77" x2="100" y2="77" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="62.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$N_0$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="562" y="297.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N$</div></foreignObject>
  <polyline points="100,77 103.5,84 107,91.5 111,98 114.5,105 118,111.5 121.5,117.5 125,123.5 128.5,129.5 132,135.5 136,141 139.5,146 143,151.5 146.5,156.5 150,161.5 154,166 157.5,170.5 161,175 164.5,179 168,183.5 171.5,187.5 175,191.5 179,195 182.5,198.5 186,202.5 189.5,205.5 193,209 197,212.5 200.5,215.5 204,218.5 207.5,221.5 211,224 214.5,227 218,229.5 222,232 225.5,234.5 229,237 232.5,239.5 236,241.5 240,244 243.5,246 247,248 250.5,250 254,252 257.5,254 261,255.5 265,257.5 268.5,259 272,261 275.5,262.5 279,264 283,265.5 286.5,267 290,268.5 293.5,269.5 297,271 300.5,272.5 304,273.5 308,274.5 311.5,276 315,277 318.5,278 322,279 326,280 329.5,281 333,282 336.5,283 340,284 343.5,285 347,285.5 351,286.5 354.5,287.5 358,288 361.5,289 365,289.5 369,290.5 372.5,291 376,291.5 379.5,292.5 383,293 386.5,293.5 390,294 394,294.5 397.5,295 401,295.5 404.5,296 408,296.5 412,297 415.5,297.5 419,298 422.5,298.5 426,299 429.5,299.5 433,299.5 437,300 440.5,300.5 444,301 447.5,301 451,301.5 455,302 458.5,302 462,302.5 465.5,303 469,303 472.5,303.5 476,303.5 480,304 483.5,304 487,304.5 490.5,304.5 494,305 498,305 501.5,305.5 505,305.5 508.5,305.5 512,306 515.5,306 519,306.5 523,306.5 526.5,306.5 530,307" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="178" y1="194.5" x2="178" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="194.5" x2="178" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="178" cy="194.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="256.5" y1="253" x2="256.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="253" x2="256.5" y2="253" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="256.5" cy="253" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="334.5" y1="282.5" x2="334.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="282.5" x2="334.5" y2="282.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="334.5" cy="282.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="100" cy="77" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="356.5" y="236" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\tfrac{1}{8}N_0$</div></foreignObject>
  <foreignObject x="213.5" y="86" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$</span></div></foreignObject>
</svg>

### Hajoamisvakio ja aktiivisuus
Ytimen hajoamistodennäköisyyttä aikayksikköä kohti kuvaa **hajoamisvakio** $\lambda$, jonka yksikkö on $\tfrac{1}{\text{s}}$. Kun ytimiä on $N$, sekunnissa hajoaa keskimäärin $\lambda N$ ydintä, joten aktiivisuus on
```kaavat
aktiivisuus :: A = \lambda N
```
missä $A$ on aktiivisuus ($\text{Bq}$), $\lambda$ hajoamisvakio ($\tfrac{1}{\text{s}}$) ja $N$ hajoamattomien ytimien määrä. Hajoamislaki voidaan kirjoittaa myös luonnollisen eksponenttifunktion avulla:
```kaavat
hajoamislaki :: N = N_0 e^{-\lambda t}
```
Puoliintumisajan kohdalla $N = \tfrac{1}{2}N_0$, joten $e^{-\lambda T_{1/2}} = \tfrac{1}{2}$ eli $\lambda T_{1/2} = \ln 2$. Hajoamisvakio ja puoliintumisaika liittyvät siis toisiinsa yhtälöllä
```kaavat
hajoamisvakio :: \lambda = \frac{\ln 2}{T_{1/2}}
```
missä $\ln 2 \approx 0{,}693$. Esimerkiksi teknetium-$99\text{m}$:lle $\lambda = \tfrac{0{,}693}{6{,}01 \cdot 3600\,\text{s}} \approx 3{,}20 \cdot 10^{-5}\,\tfrac{1}{\text{s}}$: miljoonasta ytimestä hajoaa sekunnissa keskimäärin noin $32$. Koska $A = \lambda N$ ja $\lambda$ on vakio, aktiivisuus pienenee samaa lakia kuin ytimien määrä:
```latex
A = A_0 \left(\frac{1}{2}\right)^{t/T_{1/2}}
```
missä $A_0$ on aktiivisuus hetkellä $t = 0$. Samoin pienenee hajoamattoman aineen massa, koska se on verrannollinen ytimien määrään.

```pysahdy
Aineen B puoliintumisaika on kaksinkertainen aineen A puoliintumisaikaan verrattuna. Kumman hajoamisvakio on suurempi, ja kuinka monta kertaa suurempi?
---
Aineen A hajoamisvakio on kaksinkertainen, koska $\lambda = \tfrac{\ln 2}{T_{1/2}}$ on kääntäen verrannollinen puoliintumisaikaan.
```

### Eksponenttifunktion sovitus mittausaineistoon
Puoliintumisaika määritetään mittaamalla näytteen pulssimäärää tasaisin väliajoin. Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen mallin käyrällä hajoamisen satunnaisuuden ja mittausepävarmuuden vuoksi. Siksi pisteisiin sovitetaan malli
```latex
y = A\,e^{-Ct} + B
```
missä $y$ on pulssimäärä mittausjaksossa, $C$ hajoamisvakio $\lambda$ ja $B$ taustasäteilyn pulssimäärä samassa jaksossa. Ohjelman kerroin $A$ on pulssimäärä hetkellä $t = 0$ ilman taustaa, ei aktiivisuus. Puoliintumisaika saadaan sovituksen kertoimesta: $T_{1/2} = \tfrac{\ln 2}{C}$.

Graphical Analysis Prossa sovitus tehdään näin:

1. Valitse aloitusikkunasta **Manuaalinen syöttö** ja kirjoita taulukkoon aika (s) ja pulssimäärä.
2. Avaa kuvaajatyökalujen valikko kuvaajan vasemman alakulman kuvakkeesta ja valitse **Käyrän sovitus**.
3. Valitse pudotusvalikosta eksponenttisovitus, jonka yhtälö on muotoa $A \cdot \exp(-C \cdot x) + B$ (englanninkielisessä versiossa *Natural Exponent*), ja hyväksy painikkeella **Ota käyttöön**.
4. Lue tulosruudusta kertoimet $A$, $B$ ja $C$. Ohjelma kirjoittaa ne desimaalipisteellä; kirjoita raporttiin desimaalipilkku.

Kuvan aineisto on simuloitu barium-$137\text{m}$:n hajoamiskokeesta. Sovitus antaa $C = 0{,}004564\,\tfrac{1}{\text{s}}$, joten $T_{1/2} = 0{,}6931 : 0{,}004564\,\tfrac{1}{\text{s}} \approx 152\,\text{s}$. Kirjallisuusarvo on $2{,}552\,\text{min} = 153\,\text{s}$, joten ero on alle prosentin. Sovituksen kerroin $B \approx 4{,}8$ pulssia $10\,\text{s}$:n jaksossa on taustasäteilyn taso, jota kohti pisteet lähestyvät.

<svg data-fig="sovitus" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja mittakaavassa, simuloitu esimerkkiaineisto: barium-137m-näytteen pulssimäärä 10 sekunnin jaksoissa ajan funktiona, aika nollasta 900 sekuntiin, 16 mittauspistettä 60 sekunnin välein. Ensimmäisessä jaksossa on 249 pulssia, ja määrä pienenee eksponentiaalisesti kohti taustasäteilyn tasoa, noin 5 pulssia 10 sekunnissa. Pisteiden läpi on piirretty sovitettu käyrä A kertaa e potenssiin miinus C t plus B, ja taustasäteilyn taso B on vaakasuora katkoviiva. Pisteet ovat käyrän molemmin puolin." style="max-width:100%;font-size:24px">
  <line x1="162.5" y1="312" x2="162.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="225.5" y1="312" x2="225.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="288" y1="312" x2="288" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350.5" y1="312" x2="350.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="413.5" y1="312" x2="413.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="312" x2="476" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="263" x2="476" y2="263" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="214.5" x2="476" y2="214.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="165.5" x2="476" y2="165.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="116.5" x2="476" y2="116.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="68" x2="476" y2="68" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="490" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,312 L489,318 L489,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="162.5" y1="312" x2="162.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="225.5" y1="312" x2="225.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="203" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="288" y1="312" x2="288" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="265.5" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$450$</div></foreignObject>
  <line x1="350.5" y1="312" x2="350.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="328" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="413.5" y1="312" x2="413.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="391" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$750$</div></foreignObject>
  <line x1="476" y1="312" x2="476" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$900$</div></foreignObject>
  <line x1="93" y1="263" x2="100" y2="263" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="248.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="93" y1="214.5" x2="100" y2="214.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="200" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="165.5" x2="100" y2="165.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="93" y1="116.5" x2="100" y2="116.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="102" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="93" y1="68" x2="100" y2="68" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="53.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="508" y="297.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="165" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{pulssia}\ /\ 10\,\text{s}$</div></foreignObject>
  <polyline points="100,307.5 476,307.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="106.5" y="275" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$B$</div></foreignObject>
  <polyline points="100,63.5 103,71.5 106.5,79.5 109.5,87 112.5,94.5 115.5,101.5 119,108.5 122,115.5 125,122 128,128 131.5,134 134.5,140 137.5,145.5 140.5,151 144,156 147,161.5 150,166 153.5,171 156.5,175.5 159.5,180 162.5,184.5 166,188.5 169,192.5 172,196.5 175,200 178.5,203.5 181.5,207 184.5,210.5 187.5,214 191,217 194,220 197,223 200.5,225.5 203.5,228.5 206.5,231 209.5,233.5 213,236 216,238.5 219,241 222,243 225.5,245.5 228.5,247.5 231.5,249.5 234.5,251.5 238,253 241,255 244,257 247.5,258.5 250.5,260 253.5,261.5 256.5,263.5 260,265 263,266 266,267.5 269,269 272.5,270 275.5,271.5 278.5,272.5 281.5,274 285,275 288,276 291,277 294.5,278 297.5,279 300.5,280 303.5,281 307,282 310,282.5 313,283.5 316,284.5 319.5,285 322.5,286 325.5,286.5 328.5,287.5 332,288 335,288.5 338,289 341.5,290 344.5,290.5 347.5,291 350.5,291.5 354,292 357,292.5 360,293 363,293.5 366.5,294 369.5,294.5 372.5,295 375.5,295.5 379,295.5 382,296 385,296.5 388.5,297 391.5,297 394.5,297.5 397.5,298 401,298 404,298.5 407,299 410,299 413.5,299.5 416.5,299.5 419.5,300 422.5,300 426,300.5 429,300.5 432,301 435.5,301 438.5,301.5 441.5,301.5 444.5,301.5 448,302 451,302 454,302 457,302.5 460.5,302.5 463.5,302.5 466.5,303 469.5,303 473,303 476,303.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="100" cy="68.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="125" cy="111" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="150" cy="171.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="175" cy="195" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="200.5" cy="233" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="225.5" cy="242.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="250.5" cy="263" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="275.5" cy="274" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="300.5" cy="276" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="325.5" cy="291.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="350.5" cy="291.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="375.5" cy="289.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="401" cy="298.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="426" cy="301.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="451" cy="303" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="476" cy="302" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="217" y="97" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$y = A\,e^{-Ct} + B$</span></div></foreignObject>
</svg>

## Esimerkki
Kilpirauhassyövän hoitoon valmistetun jodi-131-kapselin aktiivisuus on valmistushetkellä $550\,\text{MBq}$. Jodi-131:n puoliintumisaika on $8{,}02\,\text{d}$. Kuinka suuri kapselin aktiivisuus on $20{,}0\,\text{d}$ myöhemmin?

<!-- vaihe -->

**Tunnetut ja kysytty.** Alkuaktiivisuus $A_0 = 550\,\text{MBq}$, puoliintumisaika $T_{1/2} = 8{,}02\,\text{d}$ ja aika $t = 20{,}0\,\text{d}$.

Kysytään aktiivisuutta $A$ hetkellä $t$.

<!-- vaihe -->

**Periaate.** Aktiivisuus on verrannollinen hajoamattomien ytimien määrään, $A = \lambda N$, joten se noudattaa samaa hajoamislakia: jokainen puoliintumisaika puolittaa sen. Kapselissa on valtavasti ytimiä, joten satunnaiset poikkeamat laista ovat merkityksettömiä.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty aktiivisuus saadaan suoraan hajoamislaista:
```latex
A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: aika ja puoliintumisaika ovat molemmat vuorokausina, joten niiden suhde on paljas luku, ja aktiivisuus saadaan samassa yksikössä kuin $A_0$ eli megabecquereleinä.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}} \\
&= 550\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{20{,}0\,\text{d} / 8{,}02\,\text{d}} \\
&= 550\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{2{,}4938} \\
&= 550\,\text{MBq} \cdot 0{,}17754 \\
&\approx 97{,}6\,\text{MBq}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kapselin aktiivisuus on $20{,}0\,\text{d}$:n kuluttua noin $97{,}6\,\text{MBq}$, kolme merkitsevää numeroa kuten puoliintumisajassa $8{,}02\,\text{d}$ ja ajassa $20{,}0\,\text{d}$.

<!-- vaihe -->

**Järkevyys.** Aikaa kului vajaat kaksi ja puoli puoliintumisaikaa. Kahden puoliintumisajan jälkeen aktiivisuus olisi $550\,\text{MBq} : 4 \approx 138\,\text{MBq}$ ja kolmen jälkeen $550\,\text{MBq} : 8 \approx 69\,\text{MBq}$. Tulos $97{,}6\,\text{MBq}$ on näiden välissä, kuten pitää.

## Yleinen virhekäsitys
Moni ajattelee, että jos puolet ytimistä hajoaa yhdessä puoliintumisajassa, loput hajoavat seuraavassa, ja kahden puoliintumisajan jälkeen näyte on tyhjä. Hajoaminen ei kuitenkaan etene tasaisella nopeudella. Jokaisessa puoliintumisajassa hajoaa puolet *jäljellä olevista* ytimistä, joten jäljellä on neljäsosa, sitten kahdeksasosa ja niin edelleen. Aktiivisuus pienenee samassa tahdissa, koska hajoamisia on sitä vähemmän, mitä vähemmän ytimiä on jäljellä.

Toinen virhe on ajatella, että pitkään säilynyt ydin on "vuorossa" ja hajoaa siksi todennäköisemmin. Ytimellä ei ole muistia: sen hajoamistodennäköisyys seuraavan sekunnin aikana on aina sama, ja siksi jäljellä olevista ytimistä hajoaa jokaisessa puoliintumisajassa sama osuus.

## Tiivistelmä
- Yksittäisen ytimen hajoamishetkeä ei voi ennustaa. Jokaisella saman isotoopin ytimellä on sama hajoamistodennäköisyys aikayksikössä, eikä se riipu ytimen iästä.
- Puoliintumisaika $T_{1/2}$ on aika, jonka kuluessa puolet hajoamattomista ytimistä hajoaa: $N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}} = N_0 e^{-\lambda t}$.
- Hajoamisvakio on $\lambda = \tfrac{\ln 2}{T_{1/2}}$, ja aktiivisuus on $A = \lambda N$, yksikkönä $1\,\text{Bq} = 1\,\tfrac{1}{\text{s}}$. Aktiivisuus pienenee samaa hajoamislakia kuin ytimien määrä.
- Puoliintumisaika määritetään sovittamalla mittauspisteisiin funktio $y = A\,e^{-Ct} + B$: $C$ on hajoamisvakio ja $B$ taustasäteily, ja $T_{1/2} = \tfrac{\ln 2}{C}$.
