# Kiihtyvyys ja tasaisesti kiihtyvä liike

> **Miksi** sillalta pudotettu kivi kulkee jokaisen sekunnin aikana pidemmän matkan kuin edellisen sekunnin aikana?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kevyen liikenteen silta joen yllä kesäpäivänä. Sillan keskellä nuori pudottaa kiven kaiteen yli. Rannalla ystävä kuvaa putoamista puhelimella. Kivi on piirretty viiteen kohtaan yhtä pitkin aikavälein. Välit kasvavat alaspäin suhteessa 1 : 3 : 5 : 7. Kiven vieressä oleva sininen nopeusnuoli pitenee joka kerta yhtä paljon. Oikealla oleva mittatikku näyttää viisi korkeutta. Sen vuorotellen sävytetyt osat ovat kiven kulkemat matkat, ja ne kasvavat suhteessa 1 : 3 : 5 : 7. Alimmassa kohdassa kivi osuu veteen ja vesi roiskuu. Mittakaava ei ole tarkka, mutta välien suhteet ovat oikein." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Kiihtyvyys kertoo, miten nopeus muuttuu
Luvussa *Paikka, nopeus ja tasainen liike kuvaajina* nopeus pysyi vakiona. Useimmissa liikkeissä se kuitenkin muuttuu: auto lähtee liikennevaloista, pyöräilijä jarruttaa ja pudotettu kivi putoaa yhä nopeammin. **Kiihtyvyys** $a$ kertoo, kuinka paljon nopeus muuttuu yhdessä sekunnissa. Sen yksikkö on $\tfrac{\text{m/s}}{\text{s}} = \text{m/s}^2$. Kiihtyvyys $2{,}0\,\text{m/s}^2$ tarkoittaa, että nopeus kasvaa joka sekunti $2{,}0\,\text{m/s}$.

Kiihtyvyys on vektorisuure $\overline{a}$ niin kuin nopeus $\overline{v}$. Vektorilla on suuruus ja suunta. Suoralla radalla suunta kerrotaan etumerkillä, plussalla tai miinuksella. Kun kiihtyvyys ja nopeus osoittavat samaan suuntaan, vauhti kasvaa. Kun ne osoittavat vastakkaisiin suuntiin, vauhti pienenee. Negatiivinen kiihtyvyys ei siis aina tarkoita hidastumista. Jos kappale liikkuu negatiiviseen suuntaan ja $a < 0$, sen vauhti kasvaa. Kiihtyvyys voi olla olemassa silloinkin, kun nopeus on hetken nolla.

<svg data-fig="strobe" viewBox="0 0 600 368" role="img" aria-label="Kaavakuva kahdesta kärrystä. Kärryt on kuvattu yhden sekunnin välein, ja välit ovat mittakaavassa. Ylhäällä kärry lähtee levosta ja kiihtyy. Välit kasvavat, sininen nopeusnuoli pitenee joka sekunti yhtä paljon, ja oranssi kiihtyvyysnuoli osoittaa liikkeen suuntaan ja pysyy samanpituisena. Alhaalla kärry hidastuu. Välit lyhenevät, nopeusnuoli lyhenee ja kiihtyvyysnuoli osoittaa liikettä vastaan. Viimeisessä kuvassa kärry on hetken paikallaan, mutta kiihtyvyysnuoli on yhä sama." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-2-strobe.webp" x="-1.3" y="0" width="603" height="379.4" preserveAspectRatio="none"/>
  <foreignObject x="24" y="9.5" width="357" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kiihtyvä liike}\text{, kuvat } 1\,\text{s} \text{ välein}$</div></foreignObject>
  <foreignObject x="521" y="41.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="526" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="24" y="194.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hidastuva liike}\text{, kuvat } 1\,\text{s} \text{ välein}$</div></foreignObject>
  <foreignObject x="71" y="223.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="76" y="337.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

```pysahdy
Kärry liikkuu negatiiviseen suuntaan, ja sen kiihtyvyys on $a < 0$. Kasvaako vai pieneneekö kärryn vauhti?
---
Vauhti kasvaa, koska nopeus ja kiihtyvyys osoittavat samaan suuntaan (molemmat ovat negatiivisia).
```

### Tasaisesti kiihtyvä liike ja $(t,v)$-kuvaaja
Liike on **tasaisesti kiihtyvää**, kun kiihtyvyys pysyy vakiona. Silloin nopeus muuttuu yhtä paljon jokaisessa yhtä pitkässä aikavälissä. **$(t,v)$-kuvaajassa** vaaka-akselilla on aika ja pystyakselilla nopeus. Tasaisesti kiihtyvässä liikkeessä kuvaaja on suora. Suoran kulmakerroin eli jyrkkyys on kiihtyvyys. Nouseva suora tarkoittaa positiivista kiihtyvyyttä. Vaakasuora suora tarkoittaa tasaista liikettä. Laskeva suora tarkoittaa negatiivista kiihtyvyyttä.

<svg data-fig="tv-graph" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kahdesta (t,v)-kuvaajasta, ei lukuarvoja. Vasemmalla suora nousee alkunopeudesta v0. Suoralta on valittu kaksi pistettä, jotka rajaavat kolmion: aikaväli Δt ja nopeuden muutos Δv. Niiden suhde on kiihtyvyys a. Oikealla on kolme suoraa samasta alkunopeudesta. Nouseva suora tarkoittaa, että kiihtyvyys a on suurempi kuin nolla. Vaakasuora suora tarkoittaa, että kiihtyvyys on nolla eli liike on tasaista. Laskeva suora tarkoittaa, että kiihtyvyys on pienempi kuin nolla." style="max-width:100%;font-size:24px">
  <line x1="49" y1="290" x2="250" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M262,290 L249,296 L249,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="291" x2="50" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,44 L56,57 L44,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="268" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="40" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polyline points="50,246 236,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="106,206.5 199,206.5 199,140.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="50" cy="246" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="106" cy="206.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="199" cy="140.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="136" y="216" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="211" y="159" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta v$</div></foreignObject>
  <foreignObject x="7" y="231.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="61" y="72" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$a = \dfrac{\Delta v}{\Delta t}$</div></foreignObject>
  <line x1="316" y1="30" x2="316" y2="300" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="359" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="360" y1="291" x2="360" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M360,44 L366,57 L354,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="532" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="350" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polyline points="360,180 500,103" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="88.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$a > 0$</div></foreignObject>
  <polyline points="360,180 500,180" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="165.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <polyline points="360,180 500,257" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="242.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a < 0$</div></foreignObject>
  <circle cx="360" cy="180" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="317" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
</svg>

### Hetkellinen nopeus on tangentin kulmakerroin
Kun nopeus kasvaa, paikka muuttuu jokaisessa sekunnissa enemmän kuin edellisessä. Siksi $(t,x)$-kuvaaja ei ole suora vaan käyrä, joka jyrkkenee. Nopeus tietyllä hetkellä on **hetkellinen nopeus**. Se saadaan käyrän tangentista. Tangentti on suora, joka vain koskettaa käyrää siinä pisteessä. Tangentilta valitaan kaksi kaukana toisistaan olevaa pistettä. Hetkellinen nopeus on niiden välinen paikan muutos jaettuna ajan muutoksella. Jos laskisit suhteen kahden käyrän pisteen kautta, saisit vain keskinopeuden niiden välillä.

<svg data-fig="tangent" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva (t,x)-kuvaajasta, ei lukuarvoja. Levosta kiihtyvän kärryn kuvaaja on ylöspäin kaartuva käyrä, joka jyrkkenee koko ajan. Käyrän pisteeseen P on piirretty katkoviivana tangentti eli suora, joka koskettaa käyrää siinä kohdassa. Tangentilta on valittu kaksi kaukana toisistaan olevaa pistettä. Niiden aikaväli Δt ja paikan muutos Δx muodostavat kolmion. Tangentin kulmakerroin Δx jaettuna Δt:llä on kärryn hetkellinen nopeus sillä hetkellä, jota P vastaa." style="max-width:100%;font-size:24px">
  <line x1="69" y1="300" x2="454" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M466,300 L453,306 L453,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="301" x2="70" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M70,38 L76,51 L64,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="472" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="60" y="7.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="70,300 73,300 76,300 79,300 82,300 85,299.5 88,299.5 90.5,299.5 93.5,299 96.5,299 99.5,298.5 102.5,298 105.5,298 108.5,297.5 111.5,297 114.5,296.5 117.5,296 120.5,295.5 123.5,295 126,294.5 129,294 132,293.5 135,292.5 138,292 141,291.5 144,290.5 147,290 150,289 153,288 156,287.5 159,286.5 162,285.5 164.5,284.5 167.5,283.5 170.5,282.5 173.5,281.5 176.5,280.5 179.5,279.5 182.5,278 185.5,277 188.5,276 191.5,274.5 194.5,273.5 197.5,272 200,271 203,269.5 206,268 209,266.5 212,265 215,263.5 218,262 221,260.5 224,259 227,257.5 230,256 233,254.5 236,252.5 238.5,251 241.5,249 244.5,247.5 247.5,245.5 250.5,244 253.5,242 256.5,240 259.5,238 262.5,236 265.5,234 268.5,232 271.5,230 274,228 277,226 280,224 283,221.5 286,219.5 289,217.5 292,215 295,213 298,210.5 301,208 304,205.5 307,203.5 310,201 312.5,198.5 315.5,196 318.5,193.5 321.5,191 324.5,188.5 327.5,185.5 330.5,183 333.5,180.5 336.5,177.5 339.5,175 342.5,172 345.5,169.5 348,166.5 351,163.5 354,161 357,158 360,155 363,152 366,149 369,146 372,143 375,140 378,136.5 381,133.5 384,130.5 386.5,127 389.5,124 392.5,120.5 395.5,117 398.5,114 401.5,110.5 404.5,107 407.5,103.5 410.5,100 413.5,97 416.5,93 419.5,89.5 422,86 425,82.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="181,300 432.5,107.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 7"/>
  <polyline points="255,243.5 418,243.5 418,119" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="255" cy="243.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="418" cy="119" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="292" cy="215" r="8" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="258" y="178.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="320" y="253" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="430" y="166.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta x$</div></foreignObject>
  <foreignObject x="440.5" y="107" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{tangentti}$</div></foreignObject>
  <foreignObject x="85" y="73" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v = \dfrac{\Delta x}{\Delta t}$</div></foreignObject>
</svg>

```pysahdy
Vedät suoran $(t,x)$-käyrän kahden pisteen kautta. Mitä suoran kulmakerroin kertoo?
---
Se kertoo keskinopeuden näiden pisteiden välillä. Se ei kerro hetkellistä nopeutta kummassakaan pisteessä.
```

### Vapaa pudotus
Kun ilmanvastus on pieni, kaikki kappaleet putoavat samalla kiihtyvyydellä. Massa ei vaikuta siihen. Tämä **putoamiskiihtyvyys** on Maan pinnalla $g = 9{,}81\,\text{m/s}^2$, ja se osoittaa alaspäin. Pudotetun kiven nopeus kasvaa siis joka sekunti noin $9{,}8\,\text{m/s}$. Siksi kivi kulkee jokaisessa sekunnissa pidemmän matkan kuin edellisessä. Kappale lähtee levosta. Sen kulkemat matkat peräkkäisinä yhtä pitkinä aikaväleinä suhtautuvat kuin $1 : 3 : 5 : 7$.

```pysahdy
Pudotat tennispallon ja teräskuulan samalta korkeudelta. Ilmanvastus on pieni. Kumpi osuu maahan ensin?
---
Ne osuvat maahan yhtä aikaa, koska putoamiskiihtyvyys ei riipu massasta.
```

## Kaava: Tasaisesti kiihtyvän liikkeen yhtälöt
Keskikiihtyvyys on nopeuden muutos jaettuna ajalla, joka muutokseen kului:
```kaavat
keskikiihtyvyys :: a_\text{k} = \frac{\Delta v}{\Delta t}
```
missä $a_\text{k}$ on keskikiihtyvyys ($\text{m/s}^2$), $\Delta v = v_2 - v_1$ on nopeuden muutos ($\text{m/s}$) ja $\Delta t$ on siihen kulunut aika ($\text{s}$). Jos kiihtyvyys on vakio, se on joka hetki sama kuin keskikiihtyvyys: $a = a_\text{k}$. Oletetaan, että kiihtyvyys on vakio ja ajanotto alkaa hetkestä $t = 0$. Silloin nopeus on $v_0$, ja se muuttuu joka sekunti määrän $a$:
```kaavat
nopeus tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: v = v_0 + a\,t
```
missä $v$ on nopeus hetkellä $t$ ($\text{m/s}$), $v_0$ on alkunopeus ($\text{m/s}$), $a$ on kiihtyvyys ($\text{m/s}^2$) ja $t$ on aika ($\text{s}$).

### Siirtymä on $(t,v)$-kuvaajan ja aika-akselin välinen pinta-ala
Tasaisessa liikkeessä siirtymä $v\,t$ on $(t,v)$-kuvaajan alle jäävän suorakulmion pinta-ala. Sama pätee, kun nopeus muuttuu. Siirtymä on kuvaajan ja aika-akselin väliin jäävä pinta-ala. Aika-akselin alapuolinen osa ($v < 0$) lasketaan negatiivisena. Tasaisesti kiihtyvässä liikkeessä alue jakautuu kahteen osaan. Toinen osa on suorakulmio, jonka ala on $v_0\,t$. Toinen osa on kolmio, jonka korkeus on nopeuden kasvu $a\,t$ ja leveys $t$. Kolmion ala on $\tfrac{1}{2} \cdot a\,t \cdot t = \tfrac{1}{2}\,a\,t^2$.

<svg data-fig="area" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva (t,v)-kuvaajasta, ei lukuarvoja. Nopeus kasvaa suoraan alkunopeudesta v0 hetkellä 0 nopeuteen v hetkellä t. Suoran alle jäävä alue on jaettu kahteen osaan. Sininen suorakulmio on osa, jonka korkeus on v0 ja leveys t. Sen päällä on oranssi kolmio, jonka korkeus on nopeuden kasvu at ja leveys t. Suorakulmion ala on v0 kertaa t. Kolmion ala on puolet a t:n ja t:n tulosta. Yhdessä ne ovat siirtymä Δx." style="max-width:100%;font-size:24px">
  <line x1="79" y1="300" x2="444" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,300 L443,306 L443,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="301" x2="80" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,38 L86,51 L74,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="462" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="70" y="7.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polygon points="80,300 395,300 395,217.5 80,217.5" fill="#d0e6fb" fill-opacity="0.9"/>
  <polygon points="80,217.5 395,217.5 395,99.5" fill="#ffc078" fill-opacity="0.75"/>
  <polyline points="80,217.5 395,99.5" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="395,300 395,99.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="80,217.5 395,217.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="80" cy="217.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395" cy="99.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="37" y="203" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="50" y="85" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v$</div></foreignObject>
  <line x1="73" y1="99.5" x2="80" y2="99.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="80" y1="99.5" x2="395" y2="99.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="385" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="208.5" y="244" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$v_0\,t$</div></foreignObject>
  <foreignObject x="234" y="160.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\tfrac{1}{2}\,a t\cdot t$</div></foreignObject>
  <foreignObject x="407" y="144" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$a t$</div></foreignObject>
  <foreignObject x="407" y="244" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_0$</div></foreignObject>
</svg>

Kappale on hetkellä $t = 0$ paikassa $x_0$. Sen paikka on silloin alkupaikka plus siirtymä:
```kaavat
paikka tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
```
missä $x$ on paikka hetkellä $t$ ($\text{m}$) ja $x_0$ on alkupaikka ($\text{m}$). Muut symbolit ovat samat kuin edellä. Jos kysytään aikaa, tästä tulee toisen asteen yhtälö. Sen ratkaisuista valitaan se, joka sopii tilanteeseen.

### Putoamiskiihtyvyyden määrittäminen mittauksista
Putoavan kappaleen paikka mitataan monella hetkellä, esimerkiksi videolta tai valoporteilla. Mittauspisteisiin sovitetaan toisen asteen polynomi $s = A\,t^2 + B\,t + C$ laskimella tai taulukkolaskennalla. Oikeissa mittauksissa pisteet eivät yleensä ole täsmälleen samalla käyrällä, koska mittauksessa on aina epävarmuutta. Siksi sovitus käyttää kaikkia pisteitä yhtä aikaa. Verrataan polynomia paikan yhtälöön. Termin $t^2$ kertoimet ovat samat, $A = \tfrac{1}{2}\,a$:
```latex
a = 2A
```
missä $A$ on sovitetun polynomin $t^2$-termin kerroin ($\text{m/s}^2$). Kerroin $B$ on alkunopeus ja kerroin $C$ on alkupaikka.

<figure class="unit-photo"><img src="pics/fy4/gull-takeoff-multiple-exposure.webp" alt="Sama lokki kolme kertaa samassa kuvassa, kun se lähtee lentoon veden pinnalta."><figcaption>Lokki lähtee lentoon. Sama lintu on kuvattu samaan kuvaan kolme kertaa peräkkäin.</figcaption></figure>

## Esimerkki
Pyöräilijä tulee mäen alkuun nopeudella $4{,}0\,\text{m/s}$ ja lopettaa polkemisen. Alamäessä hänen kiihtyvyytensä on $0{,}50\,\text{m/s}^2$. Mäkeä on $60\,\text{m}$. Kuinka kauan alamäen laskeminen kestää? Mikä on nopeus mäen alla?

<!-- vaihe -->

**Tunnetut ja kysytty.** Alkunopeus on $v_0 = 4{,}0\,\text{m/s}$ ja kiihtyvyys on $a = 0{,}50\,\text{m/s}^2$. Siirtymä on $\Delta x = x - x_0 = 60\,\text{m}$ liikkeen suuntaan. Liikkeen suunta valitaan positiiviseksi.

Kysytään aikaa $t$ ja nopeutta $v$ mäen alla.

<!-- vaihe -->

**Periaate.** Kiihtyvyys on vakio, joten liike on tasaisesti kiihtyvää. Siirtymä on silloin $\Delta x = v_0\,t + \tfrac{1}{2}\,a\,t^2$. Aika on tuntematon. Se esiintyy yhtälössä sekä ensimmäisessä että toisessa potenssissa, joten saadaan toisen asteen yhtälö. Kun aika tiedetään, nopeus saadaan yhtälöstä $v = v_0 + a\,t$.

<!-- vaihe -->

**Kaava ratkaistuna.** Kirjoitetaan yhtälö muotoon $\tfrac{1}{2}\,a\,t^2 + v_0\,t - \Delta x = 0$. Ratkaistaan se toisen asteen yhtälön ratkaisukaavalla. Positiivinen ratkaisu on
```latex
t = \frac{-v_0 + \sqrt{v_0^2 + 2a\,\Delta x}}{a}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Kaikki suureet ovat SI-yksiköissä (m, m/s, m/s²), joten muunnoksia ei tarvita. Juuren alla yksikkö on $\text{m}^2/\text{s}^2$. Siksi juuri on yksikössä $\text{m/s}$ ja aika tulee sekunteina.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin juuren alla oleva lauseke ja sen neliöjuuri. Sitten lasketaan aika ja nopeus:
```latex
\begin{aligned}
&v_0^2 + 2a\,\Delta x \\
&= (4{,}0\,\text{m/s})^2 \\
&\quad + 2 \cdot 0{,}50\,\text{m/s}^2 \cdot 60\,\text{m} \\
&= 76\,\text{m}^2/\text{s}^2
\\[4pt]
&\sqrt{76\,\text{m}^2/\text{s}^2} \approx 8{,}72\,\text{m/s}
\\[4pt]
&t = \frac{-4{,}0\,\text{m/s} + 8{,}72\,\text{m/s}}{0{,}50\,\text{m/s}^2} \\
&\approx 9{,}44\,\text{s}
\\[4pt]
&v = v_0 + a\,t \\
&= 4{,}0\,\text{m/s} + 0{,}50\,\text{m/s}^2 \cdot 9{,}44\,\text{s} \\
&\approx 8{,}72\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Alamäen laskeminen kestää noin $9{,}4\,\text{s}$. Nopeus mäen alla on noin $8{,}7\,\text{m/s}$. Vastauksessa on kaksi merkitsevää numeroa, koska alkunopeus $4{,}0\,\text{m/s}$ ja kiihtyvyys $0{,}50\,\text{m/s}^2$ on annettu kahdella merkitsevällä numerolla. Matka $60\,\text{m}$ on tarkka arvo. Ratkaisukaavan toinen ratkaisu $t \approx -25\,\text{s}$ hylätään, koska liike alkaa hetkellä $t = 0$.

<!-- vaihe -->

**Järkevyys.** Nopeus kasvaa tasaisesti, joten keskinopeus on alku- ja loppunopeuden keskiarvo $$\begin{aligned} &(4{,}0\,\text{m/s} + 8{,}72\,\text{m/s}) : 2 \\ &\approx 6{,}36\,\text{m/s} \end{aligned}$$. Lasketaan matka: $6{,}36\,\text{m/s} \cdot 9{,}44\,\text{s} \approx 60\,\text{m}$. Se on mäen pituus. Loppunopeus $8{,}7\,\text{m/s} \approx 31\,\text{km/h}$ on alamäessä tavallinen pyöräilyvauhti.

## Yleinen virhekäsitys
Moni ajattelee, että kiihtyvyys on nolla aina, kun nopeus on nolla. Ylös heitetty pallo on lakipisteessä hetken paikallaan. Sen nopeus muuttuu silti koko ajan. Juuri ennen lakipistettä pallo liikkuu ylöspäin, ja heti sen jälkeen alaspäin. Kun ilmanvastus on pieni, kiihtyvyys on koko lennon ajan $g = 9{,}81\,\text{m/s}^2$ alaspäin.

Toinen virhe on ajatella, että negatiivinen kiihtyvyys on aina hidastumista. Vauhti pienenee vain, kun kiihtyvyys ja nopeus ovat vastakkaissuuntaiset. Kolmas virhe on ajatella, että raskas kappale putoaa nopeammin kuin kevyt. Kun ilmanvastus on pieni, molemmat putoavat samalla kiihtyvyydellä.

## Tiivistelmä
- Keskikiihtyvyys $a_\text{k} = \tfrac{\Delta v}{\Delta t}$ kertoo nopeuden muutoksen sekunnissa. Yksikkö on $\text{m/s}^2$. Jos kiihtyvyys on vakio, $a = a_\text{k}$. Kiihtyvyys on vektorisuure, ja suoralla etumerkki kertoo suunnan.
- Vauhti kasvaa, kun kiihtyvyys ja nopeus ovat samansuuntaiset. Vauhti pienenee, kun ne ovat vastakkaissuuntaiset.
- Tasaisesti kiihtyvässä liikkeessä $(t,v)$-kuvaaja on suora. Sen kulmakerroin on kiihtyvyys. Suoran ja aika-akselin väliin jäävä etumerkillinen pinta-ala on siirtymä. Aika-akselin alapuolinen osa ($v < 0$) lasketaan negatiivisena.
- Yhtälöt ovat $v = v_0 + a\,t$ ja $x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$. $(t,x)$-kuvaaja on käyrä. Hetkellinen nopeus on käyrän tangentin kulmakerroin.
- Vapaassa pudotuksessa kiihtyvyys on $g = 9{,}81\,\text{m/s}^2$ alaspäin. Sen voi määrittää sovittamalla mittauspisteisiin toisen asteen polynomin: $a = 2A$.
