# Kappaleiden välinen gravitaatiovoima

> **Miksi** pudonnut omena syöksyy Maata kohti, mutta Maa ei näytä liikahtavankaan omenaa kohti?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: omenapuu kesäillan hämärässä niityllä. Yksi omena on irronnut oksasta ja on puolivälissä matkalla maahan; sen perässä on liikeviivoja. Taivaalla, puun oikealla puolella, paistaa täysikuu." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Isaac Newton päätteli 1600-luvulla, että sama vuorovaikutus, joka saa omenan putoamaan, pitää myös Kuun radallaan. Tätä vuorovaikutusta kutsutaan **gravitaatioksi**: jokainen kappale, jolla on massaa, vetää jokaista muuta kappaletta puoleensa. Sinä ja pulpettisi vedätte toisianne, samoin kaksi vierekkäin istuvaa opiskelijaa. Arjessa tätä ei huomaa, koska voima on hyvin pieni, ellei toinen kappaleista ole valtava. Kahden ihmisen, $70\,\text{kg}$ ja $60\,\text{kg}$, välinen gravitaatiovoima metrin etäisyydellä on vain noin $0{,}28\,\mu\text{N}$. Maan veto saman ihmisen kohdalla on lähes $700\,\text{N}$.

Gravitaatio on vuorovaikutus, joten siihen pätee Newtonin kolmas laki. Maa vetää omenaa voimalla $\overline{F}_1$, ja omena vetää Maata yhtä suurella mutta vastakkaissuuntaisella voimalla $\overline{F}_2$. Suurempi kappale ei vedä pienempää voimakkaammin kuin pienempi suurempaa: voimat ovat aina yhtä suuret, $F_1 = F_2$.

<svg data-fig="vuorovaikutus" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: vasemmalla Maa, oikealla omena. Maa vetää omenaa voimalla F1, joka osoittaa omenasta kohti Maata, ja omena vetää Maata yhtä suurella voimalla F2, joka osoittaa Maan keskipisteestä kohti omenaa. Nuolet ovat yhtä pitkät. Omenan kiihtyvyys on 9,8 metriä sekunnissa toiseen, Maan kiihtyvyys noin 3 kertaa 10 potenssiin miinus 25 metriä sekunnissa toiseen." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-vuorovaikutus.webp" x="2.5" y="0" width="597" height="365.7" preserveAspectRatio="none"/>
  <foreignObject x="187.5" y="125.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <foreignObject x="417.5" y="125.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <foreignObject x="59.5" y="315.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{Maa: } a \approx 3 \cdot 10^{-25}\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="465" y="205.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{omena}$</div></foreignObject>
  <foreignObject x="433.5" y="315.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$a = 9{,}8\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="265" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F_1 = F_2$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/artemis2-earthset.webp" alt="Kuun kraatterien peittämä pinta kuvan alaosassa ja sen takana mustaa avaruutta vasten laskeva sininen Maa."><figcaption>Maa laskee Kuun horisontin taakse. Artemis II -miehistö otti kuvan Orion-aluksesta huhtikuussa 2026, kun alus ohitti Kuun. Maa ja Kuu vetävät toisiaan yhtä suurella gravitaatiovoimalla.</figcaption></figure>

Ero on kiihtyvyyksissä. Newtonin toisen lain mukaan kappaleen kiihtyvyys on $a = \tfrac{F}{m}$. Kun $0{,}20\,\text{kg}$:n omenaan vaikuttaa noin $1{,}96\,\text{N}$:n voima, omenan kiihtyvyys on noin $9{,}8\,\text{m/s}^2$. Sama voima antaa Maalle, jonka massa on $5{,}97 \cdot 10^{24}\,\text{kg}$, kiihtyvyyden noin $3 \cdot 10^{-25}\,\text{m/s}^2$. Maa todella liikahtaa omenaa kohti, mutta niin vähän, ettei sitä voi mitata.

```pysahdy
Maa ja Kuu vetävät toisiaan yhtä suurella gravitaatiovoimalla. Kumpi kiihtyy enemmän?
---
Kuu. Kiihtyvyys on $a = \tfrac{F}{m}$, ja samalla voimalla pienempimassainen Kuu kiihtyy enemmän kuin Maa.
```

## Kaava: Newtonin gravitaatiolaki
Kahden kappaleen välinen gravitaatiovoima on sitä suurempi, mitä suuremmat massat kappaleilla on, ja sitä pienempi, mitä kauempana ne ovat toisistaan. Newtonin gravitaatiolaki kertoo, että voima on suoraan verrannollinen kumpaankin massaan ja kääntäen verrannollinen etäisyyden neliöön:

```kaavat
Newtonin gravitaatiolaki :: F = \gamma \frac{m_1 m_2}{r^2}
```

missä $F$ on kumpaankin kappaleeseen vaikuttavan gravitaatiovoiman suuruus (N), $m_1$ ja $m_2$ kappaleiden massat (kg), $r$ kappaleiden keskipisteiden välinen etäisyys (m) ja $\gamma$ gravitaatiovakio, $\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$. Voima vaikuttaa kumpaankin kappaleeseen kohti toista kappaletta. Henry Cavendish määritti vuonna 1798 Maan keskitiheyttä mittaamalla lyijypallojen välistä heikkoa gravitaatiovuorovaikutusta. Hänen tuloksestaan voidaan johtaa gravitaatiovakion arvo.

<svg data-fig="kaava" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva: kaksi palloa, vasemmalla suurempi massa m1 ja oikealla pienempi massa m2. Pallojen keskipisteiden välinen etäisyys r on merkitty mittajanalla pallojen alle. Kumpaankin palloon vaikuttaa yhtä suuri gravitaatiovoima kohti toista palloa: F1 vasemmasta pallosta oikealle ja F2 oikeasta pallosta vasemmalle." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-kaava.webp" x="14.6" y="11" width="585.4" height="304.9" preserveAspectRatio="none"/>
  <foreignObject x="133.5" y="21.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="453.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <foreignObject x="221.5" y="85.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <foreignObject x="353.5" y="85.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <foreignObject x="290" y="253.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
</svg>

Laki pätee sellaisenaan pistemäisille kappaleille. Se pätee myös tasa-aineisille palloille ja muille pallosymmetrisille kappaleille, kuten planeetoille ja tähdille, kun $r$ mitataan keskipisteiden välillä: tällainen kappale vetää ulkopuolisia kappaleita ikään kuin sen koko massa olisi keskipisteessä. Maan pinnalla seisovan ihmisen etäisyys Maan keskipisteestä on siis Maan säde.

```pysahdy
Ihminen seisoo Maan pinnalla. Mikä etäisyys $r$ pitää sijoittaa gravitaatiolakiin, kun lasketaan Maan ja ihmisen välistä voimaa?
---
Etäisyys Maan keskipisteestä eli Maan säde, noin $6378\,\text{km}$. Etäisyys Maan pinnasta ei kelpaa, koska $r$ mitataan keskipisteiden välillä.
```

Etäisyys on kaavassa toisessa potenssissa. Kun etäisyys kaksinkertaistuu, voima pienenee neljäsosaan, ja kun etäisyys kolminkertaistuu, yhdeksäsosaan. Kun taas toinen massa kaksinkertaistuu, myös voima kaksinkertaistuu. Gravitaatiovoima pienenee etäisyyden kasvaessa nopeasti, mutta se ei koskaan muutu tarkalleen nollaksi. Kuvaaja näyttää voiman, kun kummankin kappaleen massa on $10\,\text{t}$.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: vaaka-akselilla kappaleiden keskipisteiden etäisyys r metreinä nollasta kymmeneen, pystyakselilla gravitaatiovoima F mikronewtoneina nollasta 1800:aan, kun kummankin kappaleen massa on 10 tonnia. Laskevan käyrän pisteet ovat r = 2 m, F = 1670 µN; r = 4 m, F = 417 µN; r = 6 m, F = 185 µN; r = 8 m, F = 104 µN ja r = 10 m, F = 66,7 µN. Katkoviivat näyttävät, että kun etäisyys kaksinkertaistuu kahdesta neljään metriin, voima pienenee neljäsosaan." style="max-width:100%;font-size:24px">
  <line x1="173" y1="306" x2="173" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="249.5" y1="306" x2="249.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326.5" y1="306" x2="326.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="403" y1="306" x2="403" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="306" x2="480" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="228" x2="480" y2="228" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="150" x2="480" y2="150" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="72" x2="480" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="306" x2="494" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,306 L493,312 L493,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="307" x2="96" y2="58" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,46 L102,59 L90,59 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="173" y1="306" x2="173" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="163" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="249.5" y1="306" x2="249.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="239.5" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="326.5" y1="306" x2="326.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="316.5" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="403" y1="306" x2="403" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="393" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="480" y1="306" x2="480" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="463.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="228" x2="96" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="213.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="89" y1="150" x2="96" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="135.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1200$</div></foreignObject>
  <line x1="89" y1="72" x2="96" y2="72" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="57.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1800$</div></foreignObject>
  <foreignObject x="66" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="291.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{m})$</div></foreignObject>
  <foreignObject x="86" y="15.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\mu\text{N})$</div></foreignObject>
  <polyline points="173,89 175.5,103 178,115.5 180.5,126.5 183,137 185.5,146.5 188,155.5 190.5,163.5 193.5,171 196,177.5 198.5,184 201,190 203.5,195.5 206,200.5 208.5,205 211,209.5 214,213.5 216.5,217.5 219,221.5 221.5,224.5 224,228 226.5,231 229,234 231.5,236.5 234,239 237,241.5 239.5,244 242,246 244.5,248 247,250 249.5,252 252,253.5 254.5,255 257.5,257 260,258.5 262.5,260 265,261 267.5,262.5 270,264 272.5,265 275,266 278,267.5 280.5,268.5 283,269.5 285.5,270.5 288,271.5 290.5,272 293,273 295.5,274 298,274.5 301,275.5 303.5,276 306,277 308.5,277.5 311,278.5 313.5,279 316,279.5 318.5,280 321.5,281 324,281.5 326.5,282 329,282.5 331.5,283 334,283.5 336.5,284 339,284.5 342,285 344.5,285.5 347,285.5 349.5,286 352,286.5 354.5,287 357,287 359.5,287.5 362,288 365,288.5 367.5,288.5 370,289 372.5,289.5 375,289.5 377.5,290 380,290 382.5,290.5 385.5,290.5 388,291 390.5,291 393,291.5 395.5,291.5 398,292 400.5,292 403,292.5 406,292.5 408.5,293 411,293 413.5,293.5 416,293.5 418.5,293.5 421,294 423.5,294 426,294.5 429,294.5 431.5,294.5 434,295 436.5,295 439,295 441.5,295.5 444,295.5 446.5,295.5 449.5,295.5 452,296 454.5,296 457,296 459.5,296.5 462,296.5 464.5,296.5 467,296.5 470,297 472.5,297 475,297 477.5,297 480,297.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="173" y1="89" x2="173" y2="306" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="89" x2="173" y2="89" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="249.5" y1="252" x2="249.5" y2="306" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="252" x2="249.5" y2="252" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="173" cy="89" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="249.5" cy="252" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="326.5" cy="282" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="403" cy="292.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="480" cy="297.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="187" y="76.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="261.5" y="211.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\tfrac{F}{4}$</div></foreignObject>
  <foreignObject x="306" y="77.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$m_1 = m_2 = 10\,\text{t}$</span></div></foreignObject>
  <foreignObject x="325" y="115.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$2r \;\Rightarrow\; \tfrac{1}{4}F$</span></div></foreignObject>
</svg>

```pysahdy
Kuvaajan mukaan voima on $417\,\mu\text{N}$, kun etäisyys on $4\,\text{m}$. Mikä se on, kun etäisyys on $8\,\text{m}$?
---
Etäisyys kaksinkertaistuu, joten voima pienenee neljäsosaan: $417\,\mu\text{N} : 4 \approx 104\,\mu\text{N}$. Sama arvo luetaan kuvaajasta.
```

## Painovoima ja gravitaatiokenttä
Kappaleen paino $G = mg$ on Maan kappaleeseen kohdistama gravitaatiovoima. Kun Maan massa on $M$ ja säde $R$, gravitaatiolaki antaa saman voiman, joten $mg = \gamma \tfrac{Mm}{R^2}$. Kappaleen massa $m$ supistuu pois, ja putoamiskiihtyvyydeksi jää $g = \gamma \tfrac{M}{R^2}$. Siksi kaikki kappaleet putoavat Maan pinnalla samalla kiihtyvyydellä, kun ilmanvastus jätetään huomiotta: raskaampaan kappaleeseen vaikuttaa suurempi voima, mutta sitä on myös vaikeampi kiihdyttää.

### Gravitaatiokentän voimakkuus
**Syventävä osio.** Gravitaatiokentän voimakkuus ei kuulu tämän kurssin keskeisiin sisältöihin, joten tämä alaluku ja sitä seuraava *Kenttä eri taivaankappaleilla* ovat syventävää sisältöä. Ydinpolulle riittävät Newtonin gravitaatiolaki ja se, että kappaleen paino on Maan pinnalla kappaleeseen vaikuttava gravitaatiovoima.

Maa muuttaa ympäristöään niin, että jokaisessa pisteessä on valmiina tietty veto: siihen tuotuun kappaleeseen vaikuttaa voima $\overline{F} = m\overline{g}$. Tätä kutsutaan Maan **gravitaatiokentäksi**. Kentän voimakkuus etäisyydellä $r$ kappaleen keskipisteestä on

```latex
g = \gamma \frac{M}{r^2}
```

missä $M$ on kentän synnyttävän kappaleen massa (kg) ja $r$ etäisyys sen keskipisteestä (m). Kentän suunta on kohti kappaleen keskipistettä, ja voimakkuuden yksikkö on $\text{m/s}^2$. Jos kappaleeseen vaikuttaa vain gravitaatio, sen kiihtyvyys on Newtonin toisen lain mukaan $a = \tfrac{F}{m} = \tfrac{mg}{m} = g$. Gravitaatiokentän voimakkuus on siis sama asia kuin vapaasti putoavan kappaleen kiihtyvyys siinä kohdassa.

<svg data-fig="kentta" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: Maa keskellä. Kahden Maan säteen etäisyydellä keskipisteestä on katkoviivalla piirretty ympyrä, jonka seitsemästä pisteestä lähtee yhtä pitkä oranssi nuoli g kohti Maan keskipistettä. Ympyrän oikeassa reunassa on pieni kappale, johon vaikuttaa punainen voima F = mg kohti Maan keskipistettä." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-kentta.webp" x="1.2" y="1.2" width="597" height="384.3" preserveAspectRatio="none"/>
  <foreignObject x="374.5" y="61" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{g}$</div></foreignObject>
  <foreignObject x="426" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="376" y="225.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F} = m\overline{g}$</div></foreignObject>
  <foreignObject x="221" y="9.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r = 2R$</div></foreignObject>
</svg>

### Kenttä eri taivaankappaleilla
Taulukon kentän voimakkuudet on laskettu kaavasta $g = \gamma \tfrac{M}{R^2}$ NASAn planeettataulukon (Planetary Fact Sheet) massoista ja päiväntasaajan säteistä. Maan arvo $9{,}80\,\text{m/s}^2$ on laskettu ilman Maan pyörimisen vaikutusta; mitattu arvo on hieman erilainen, ja tämän kirjan tehtävissä käytetään arvoa $9{,}81\,\text{m/s}^2$. Kappaleen massa on sama kaikkialla, mutta sen paino riippuu siitä, minkä taivaankappaleen kentässä se on.

| Kappale | massa $M$ (kg) | säde $R$ (km) | $g$ ($\text{m/s}^2$) |
|---|---|---|---|
| Kuu | $7{,}35 \cdot 10^{22}$ | $1738$ | $1{,}62$ |
| Mars | $6{,}42 \cdot 10^{23}$ | $3396$ | $3{,}71$ |
| Maa | $5{,}97 \cdot 10^{24}$ | $6378$ | $9{,}80$ |
| Jupiter | $1{,}90 \cdot 10^{27}$ | $71\,492$ | $24{,}8$ |
| Aurinko | $1{,}99 \cdot 10^{30}$ | $695\,700$ | $274$ |

<svg data-fig="planeetat" viewBox="0 0 600 360" role="img" aria-label="Kuva, nuolten pituudet mittakaavassa: neljä pintaa vierekkäin, Kuu, Mars, Maa ja Jupiter. Kunkin pinnan yllä on pieni pallo ja siitä alaspäin oranssi nuoli, jonka pituus on gravitaatiokentän voimakkuus eli putoamiskiihtyvyys pinnalla: Kuu 1,62, Mars 3,71, Maa 9,80 ja Jupiter 24,8 metriä sekunnissa toiseen." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-planeetat.webp" x="1.2" y="-2.5" width="597" height="366.9" preserveAspectRatio="none"/>
  <foreignObject x="61.5" y="311.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Kuu}$</div></foreignObject>
  <foreignObject x="24" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$1{,}62\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="199" y="311.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Mars}$</div></foreignObject>
  <foreignObject x="168" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$3{,}71\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="349.5" y="311.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maa}$</div></foreignObject>
  <foreignObject x="312" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$9{,}80\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="468.5" y="311.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Jupiter}$</div></foreignObject>
  <foreignObject x="456" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$24{,}8\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="530" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{g}$</div></foreignObject>
</svg>

Maan pinnalla mitattu putoamiskiihtyvyys vaihtelee välillä $9{,}78\text{–}9{,}83\,\text{m/s}^2$, koska Maa pyörii ja on hieman litistynyt. Tässä kirjassa käytetään arvoa $g = 9{,}81\,\text{m/s}^2$, kun putoamiskiihtyvyys Maan pinnalla tarvitaan.

## Gravitaatio maailmankaikkeudessa
Gravitaatio on perusvuorovaikutuksista heikoin, mutta suurissa mittakaavoissa se on ratkaiseva. Sähköiset voimat ovat paljon voimakkaampia, mutta positiiviset ja negatiiviset varaukset kumoavat toistensa vaikutukset, joten suuret kappaleet ovat lähes sähköisesti neutraaleja. Gravitaatio taas on aina vetävä: jokainen massa lisää vetoa, eikä mikään kumoa sitä. Lisäksi gravitaation vaikutus ulottuu kauas, koska $\tfrac{1}{r^2}$ pienenee mutta ei koskaan muutu nollaksi.

<svg data-fig="rakenteet" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kolmessa vaiheessa vasemmalta oikealle, ei mittakaavassa. Ensin lähes tasainen kaasu- ja pölypilvi, jossa on hieman tiheämpi kohta. Sitten tiheämmät kohdat ovat kasvaneet, ja nuolet näyttävät ympäröivän aineen virtaavan niitä kohti. Lopuksi tiheimpään kohtaan on syntynyt tähti, jonka ympärillä kiertää litteä kiekko ja pieniä planeettoja. Vaiheiden välillä on aikaa kuvaavat nuolet." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-rakenteet.webp" x="0" y="1.2" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="33.5" y="275.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasupilvi}$</div></foreignObject>
  <foreignObject x="233.5" y="275.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymiä}$</div></foreignObject>
  <foreignObject x="465" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tähti}$</div></foreignObject>
</svg>

Varhainen maailmankaikkeus oli lähes tasainen kaasupilvi. Kohdat, joissa ainetta oli hieman keskimääräistä enemmän, vetivät ympäröivää ainetta voimakkaammin puoleensa, joten ne tihenivät entisestään. Tihentymät kasvoivat kaasupilviksi, joiden keskiosat luhistuivat oman painonsa alla. Luhistuessaan kaasu tiivistyi ja kuumeni, kunnes sen keskustassa käynnistyivät ydinreaktiot ja syntyi tähti. Tähteä ympäröivään litteään kiekkoon jäänyt aine kasautui planeetoiksi. Gravitaatio kokoaa myös tähdet galakseiksi ja galaksit galaksijoukoiksi, ja se pitää planeetat radoillaan tähtensä ympärillä.

## Esimerkki
Kuinka suurella voimalla Maa ja Kuu vetävät toisiaan? Maan massa on $5{,}97 \cdot 10^{24}\,\text{kg}$, Kuun massa $7{,}35 \cdot 10^{22}\,\text{kg}$ ja niiden keskipisteiden keskimääräinen etäisyys $3{,}84 \cdot 10^{5}\,\text{km}$.

<!-- vaihe -->

**Tunnetut ja kysytty.** Maan massa $M = 5{,}97 \cdot 10^{24}\,\text{kg}$, Kuun massa $m = 7{,}35 \cdot 10^{22}\,\text{kg}$, etäisyys $r = 3{,}84 \cdot 10^{5}\,\text{km}$ ja gravitaatiovakio $\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$.

Kysytään gravitaatiovoiman suuruutta $F$.

<!-- vaihe -->

**Periaate.** Maa ja Kuu ovat lähes pallosymmetrisiä, joten niiden välistä voimaa voidaan laskea Newtonin gravitaatiolailla, kun $r$ on keskipisteiden välinen etäisyys. Newtonin kolmannen lain mukaan sama voima vaikuttaa sekä Kuuhun että Maahan.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty voima on jo ratkaistuna:

```latex
F = \gamma \frac{M m}{r^2}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Etäisyys muutetaan metreiksi: $r = 3{,}84 \cdot 10^{5}\,\text{km} = 3{,}84 \cdot 10^{5} \cdot 10^{3}\,\text{m} = 3{,}84 \cdot 10^{8}\,\text{m}$. Massat ovat jo kilogrammoina.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:

```latex
\begin{aligned}
&F = \gamma \frac{M m}{r^2} \\
&= 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\
&\quad \cdot \frac{5{,}97 \cdot 10^{24}\,\text{kg} \cdot 7{,}35 \cdot 10^{22}\,\text{kg}}{(3{,}84 \cdot 10^{8}\,\text{m})^2} \\
&\approx 1{,}99 \cdot 10^{20}\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Maa ja Kuu vetävät toisiaan voimalla $F \approx 1{,}99 \cdot 10^{20}\,\text{N}$. Vastaus annetaan kolmella merkitsevällä numerolla, koska massat ja etäisyys on annettu kolmen numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Pyöristetyillä luvuilla $7 \cdot 10^{-11} \cdot \tfrac{6 \cdot 10^{24} \cdot 7 \cdot 10^{22}}{(4 \cdot 10^{8})^2}\,\text{N} \approx 1{,}8 \cdot 10^{20}\,\text{N}$, joten suuruusluokka on oikea. Voima on valtava, mutta Kuun kiihtyvyys on silti vain $a = \tfrac{F}{m} \approx 2{,}7 \cdot 10^{-3}\,\text{m/s}^2$, koska Kuun massa on suuri.

## Yleinen virhekäsitys
”Maa vetää Kuuta voimakkaammin kuin Kuu Maata, koska Maa on paljon suurempi.” Gravitaatio on vuorovaikutus, joten Newtonin kolmannen lain mukaan voimat ovat aina yhtä suuret ja vastakkaissuuntaiset. Massojen ero näkyy kiihtyvyyksissä: sama voima kiihdyttää kevyempää kappaletta enemmän. Toinen yleinen käsitys on, että gravitaatio loppuu ilmakehän yläpuolella. Se kuitenkin vain heikkenee etäisyyden kasvaessa: esimerkiksi $300\,\text{km}$:n korkeudella kentän voimakkuus on vielä noin $8{,}9\,\text{m/s}^2$.

## Tiivistelmä
- Kaikki kappaleet vetävät toisiaan puoleensa gravitaatiovoimalla $F = \gamma \tfrac{m_1 m_2}{r^2}$, missä $r$ on keskipisteiden välinen etäisyys ja $\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$.
- Kahden kappaleen väliset gravitaatiovoimat ovat yhtä suuret ja vastakkaissuuntaiset; kevyempi kappale kiihtyy enemmän.
- Kun etäisyys kaksinkertaistuu, voima pienenee neljäsosaan.
- Kappaleen paino on Maan pinnalla siihen vaikuttava gravitaatiovoima, $G = mg$.
- Syventävä: gravitaatiokentän voimakkuus $g = \gamma \tfrac{M}{r^2}$ on vapaasti putoavan kappaleen kiihtyvyys, yksikkö $\text{m/s}^2$.
- Gravitaatio on aina vetävä ja ulottuu kauas, joten se kokoaa ainetta tähdiksi, planeetoiksi ja galakseiksi.
