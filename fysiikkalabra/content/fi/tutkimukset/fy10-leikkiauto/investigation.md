# Leikkiauton nopeus ja lähtökorkeus

> **Tutkimuskysymys:** Miten rataa alas laskevan leikkiauton nopeus riippuu lähtökorkeudesta, ja vastaavatko mittaukset energiaperiaatteeseen perustuvaa mallia?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: leikkiauto on kaltevan radan yläpäässä. Auton paikka on piirretty tasaisin aikavälein: rinteessä välit kasvavat, kun auton vauhti kasvaa. Radan alapäässä on vaakasuora osa, jolla auto kulkee valoportin läpi. Valoportti on kytketty pöydällä olevaan tietokoneeseen. Radan päässä on pysäytin." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10lh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10lh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10lh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10lh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="426" width="150" height="44" rx="4" fill="#a9d1f0" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="34" y="382" width="150" height="44" rx="4" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="30" y="338" width="150" height="44" rx="4" fill="#b2f2bb" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="34" y="294" width="150" height="44" rx="4" fill="#ffe8a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="30" y="250" width="150" height="44" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="34" y="206" width="150" height="44" rx="4" fill="#a9d1f0" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M70,196 L690,440 H1150 V454 H694 L100,222 L70,210 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="1150" y="410" width="22" height="44" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="750" y="454" width="20" height="16" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="990" y="454" width="20" height="16" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <g transform="translate(135,221.5) rotate(21.48)" opacity="1.0"><rect x="-6" y="-74" width="12" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-26,-34 L-16,-50 H20 L30,-34 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-46" y="-36" width="92" height="22" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-28" cy="-10" r="10" fill="#1f2933"/><circle cx="-28" cy="-10" r="4" fill="#c4ccd4"/><circle cx="28" cy="-10" r="10" fill="#1f2933"/><circle cx="28" cy="-10" r="4" fill="#c4ccd4"/></g>
  <g transform="translate(159.5,231.5) rotate(21.48)" opacity="0.35"><rect x="-6" y="-74" width="12" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-26,-34 L-16,-50 H20 L30,-34 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-46" y="-36" width="92" height="22" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-28" cy="-10" r="10" fill="#1f2933"/><circle cx="-28" cy="-10" r="4" fill="#c4ccd4"/><circle cx="28" cy="-10" r="10" fill="#1f2933"/><circle cx="28" cy="-10" r="4" fill="#c4ccd4"/></g>
  <g transform="translate(233.5,260.5) rotate(21.48)" opacity="0.35"><rect x="-6" y="-74" width="12" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-26,-34 L-16,-50 H20 L30,-34 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-46" y="-36" width="92" height="22" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-28" cy="-10" r="10" fill="#1f2933"/><circle cx="-28" cy="-10" r="4" fill="#c4ccd4"/><circle cx="28" cy="-10" r="10" fill="#1f2933"/><circle cx="28" cy="-10" r="4" fill="#c4ccd4"/></g>
  <g transform="translate(356.5,308.5) rotate(21.48)" opacity="0.35"><rect x="-6" y="-74" width="12" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-26,-34 L-16,-50 H20 L30,-34 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-46" y="-36" width="92" height="22" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-28" cy="-10" r="10" fill="#1f2933"/><circle cx="-28" cy="-10" r="4" fill="#c4ccd4"/><circle cx="28" cy="-10" r="10" fill="#1f2933"/><circle cx="28" cy="-10" r="4" fill="#c4ccd4"/></g>
  <g transform="translate(528.5,376.5) rotate(21.48)" opacity="0.35"><rect x="-6" y="-74" width="12" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-26,-34 L-16,-50 H20 L30,-34 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-46" y="-36" width="92" height="22" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-28" cy="-10" r="10" fill="#1f2933"/><circle cx="-28" cy="-10" r="4" fill="#c4ccd4"/><circle cx="28" cy="-10" r="10" fill="#1f2933"/><circle cx="28" cy="-10" r="4" fill="#c4ccd4"/></g>
  <g transform="translate(753,440) rotate(0.00)" opacity="0.35"><rect x="-6" y="-74" width="12" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-26,-34 L-16,-50 H20 L30,-34 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-46" y="-36" width="92" height="22" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-28" cy="-10" r="10" fill="#1f2933"/><circle cx="-28" cy="-10" r="4" fill="#c4ccd4"/><circle cx="28" cy="-10" r="10" fill="#1f2933"/><circle cx="28" cy="-10" r="4" fill="#c4ccd4"/></g>
  <rect x="999" y="368" width="10" height="72" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="991" y="360" width="26" height="30" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="1004" cy="378" r="3.5" fill="#ffffff"/>
  <g transform="translate(1004,440) rotate(0.00)" opacity="1.0"><rect x="-6" y="-74" width="12" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-26,-34 L-16,-50 H20 L30,-34 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-46" y="-36" width="92" height="22" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-28" cy="-10" r="10" fill="#1f2933"/><circle cx="-28" cy="-10" r="4" fill="#c4ccd4"/><circle cx="28" cy="-10" r="10" fill="#1f2933"/><circle cx="28" cy="-10" r="4" fill="#c4ccd4"/></g>
  <path d="M1017,370 C1094,370 1110,450 1090,488" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="1020" y="488" width="140" height="80" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1030" y="498" width="120" height="60" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <path d="M1010,568 H1170 L1160,580 H1020 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
</svg>

Mäenlaskija, vuoristoradan vaunu ja leikkiauto saavat vauhtinsa samasta lähteestä: korkeuserosta. Tässä tutkimuksessa et aloita mittaamisesta vaan ennusteesta. Muotoilet ensin energiaperiaatteen avulla hypoteesin ja mallin siitä, miten auton nopeus riippuu lähtökorkeudesta, ja testaat mallin sitten mittaamalla. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten auton nopeus radan tietyssä kohdassa riippuu lähtökorkeudesta, vastaavatko mittaustulokset energiaperiaatteesta johdettua mallia ja kuinka suuri osa auton potentiaalienergiasta näkyy auton nopeudessa, epävarmuuksineen.

**Päätät itse:** hypoteesin ja mallin perusteluineen, lähtökorkeudet ja niiden määrän, toistojen määrän, sen, miten mittaat korkeuden ja nopeuden, kuvaajan akselit perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa ja osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, mittaus toisella autolla tai lisäkuormalla, kuuluu työhösi: vertaa sen tulosta päämittauksen tulokseen.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Jos lähtökorkeus kaksinkertaistuu, mitä arvelet auton nopeudelle tapahtuvan radan alaosassa? Kaksinkertaistuuko nopeus, vai muuttuuko se jotenkin muuten?
2. Luonnostele kuvaaja, jossa nopeus on lähtökorkeuden funktiona. Millainen kuvaaja on?
3. Saako raskaampi auto samalta korkeudelta suuremman nopeuden kuin kevyempi?
4. Mihin osa auton energiasta voi joutua matkalla, ja tuleeko mitattu nopeus siksi suuremmaksi vai pienemmäksi kuin ennustit?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Hypoteesista malliksi

Hypoteesi on perusteltu ennuste, jonka mittaus voi osoittaa vääräksi. Tässä tutkimuksessa hypoteesista tehdään malli: yhtälö, joka kertoo, millaisia mittaustuloksia pitäisi tulla, jos hypoteesi pitää paikkansa. Ennen kuin luet eteenpäin, kirjaa:

1. Mitkä energiamuodot muuttuvat toisikseen, kun auto laskee rataa alas? Kirjoita energiaperiaatteen avulla yhtälö, joka liittää nopeuden lähtökorkeuteen, kun energiaa ei mene muualle.
2. Millaisen kuvaajan pitäisi mallisi mukaan olla origon kautta kulkeva suora? Mitä sen kulmakertoimen pitäisi olla?
3. Mitä mittaamalla saat nopeuden ja korkeuden selville, ja mistä kohdasta autoa korkeus kannattaa mitata?

## Teoriaa lyhyesti

Auto päästetään liikkeelle levosta. Kun se laskee rataa alas, sen potentiaalienergia muuttuu liike-energiaksi. Osa liike-energiasta on pyörien pyörimisen energiaa: se kuuluu mekaaniseen energiaan, mutta se ei näy auton nopeudessa. Jos mekaaninen energia säilyisi ja pyörien pyörimisen energia olisi pieni, auton koko potentiaalienergian muutos näkyisi sen nopeudessa. Todellisuudessa osa energiasta muuttuu lisäksi kitkan, vierintävastuksen ja ilmanvastuksen vuoksi sisäenergiaksi. [[apua:fy4-8|Mekaanisen energian säilyminen]]

::: tuki O OO
Tarkista kirjauksesi tästä. Merkitään **lähtökorkeutta** $h$: se on auton tietyn kohdan, esimerkiksi auton kylkeen tehdyn merkin, pystysuora korkeusero lähtökohdan ja valoportin kohdan välillä. Auton nopeus valoportin kohdalla on $v$.

<svg data-fig="setup" viewBox="0 0 600 380" role="img" aria-label="Kaaviokuva. Vasemmalla ylhäällä leikkiauto on levossa kaltevan radan yläpäässä. Autossa on merkki. Rata jatkuu alhaalla vaakasuorana, ja sen kohdalla on valoportti, jonka läpi auto kulkee. Korkeus h on auton merkin pystysuora korkeusero lähtökohdan ja valoportin välillä. Auton katolla oleva liuska katkaisee valoportin säteen. Liuskan leveys on L." style="max-width:100%;font-size:24px">
  <path d="M40,120 L300,300 H470 V310 H303 L40,132 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="470" y="278" width="14" height="32" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <g transform="translate(77,145.5) rotate(34.70)" opacity="1.0"><rect x="-9" y="-55.5" width="18" height="19.5" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-19.5,-25.5 L-12,-37.5 H15 L22.5,-25.5 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-34.5" y="-27" width="69" height="16.5" rx="4.5" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-21" cy="-7.5" r="7.5" fill="#1f2933"/><circle cx="-21" cy="-7.5" r="3" fill="#c4ccd4"/><circle cx="21" cy="-7.5" r="7.5" fill="#1f2933"/><circle cx="21" cy="-7.5" r="3" fill="#c4ccd4"/><circle cx="0" cy="-19" r="4" fill="#ffffff" stroke="#1f2933" stroke-width="2"/></g>
  <rect x="375" y="243.5" width="10" height="56.5" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="369" y="235.5" width="22" height="30" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="380" cy="253.5" r="3.5" fill="#ffffff"/>
  <g transform="translate(380,300) rotate(0.00)" opacity="1.0"><rect x="-9" y="-55.5" width="18" height="19.5" fill="#ffffff" stroke="#1f2933" stroke-width="2"/><path d="M-19.5,-25.5 L-12,-37.5 H15 L22.5,-25.5 Z" fill="#dbe4ea" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/><rect x="-34.5" y="-27" width="69" height="16.5" rx="4.5" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/><circle cx="-21" cy="-7.5" r="7.5" fill="#1f2933"/><circle cx="-21" cy="-7.5" r="3" fill="#c4ccd4"/><circle cx="21" cy="-7.5" r="7.5" fill="#1f2933"/><circle cx="21" cy="-7.5" r="3" fill="#c4ccd4"/><circle cx="0" cy="-19" r="4" fill="#ffffff" stroke="#1f2933" stroke-width="2"/></g>
  <line x1="95.5" y1="130" x2="555" y2="130" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="388" y1="281" x2="555" y2="281" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="545" y1="130" x2="545" y2="281" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="535" y1="130" x2="555" y2="130" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="535" y1="281" x2="555" y2="281" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="513" y="191" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$h$</div></foreignObject>
  <line x1="371" y1="206.5" x2="371" y2="240.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="389" y1="206.5" x2="389" y2="240.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="371" y1="214.5" x2="389" y2="214.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="345" y="200" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$L$</div></foreignObject>
  <foreignObject x="313.5" y="331.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{valoportti}$</div></foreignObject>
  <foreignObject x="57" y="51" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{lähtö levosta}$</div></foreignObject>
</svg>

Lähtökohdassa auto on levossa, joten sen liike-energia on nolla. Valitaan potentiaalienergian nollataso valoportin kohdalle. Jos mekaaninen energia säilyy ja pyörien pyörimisen energia on niin pieni, että se jätetään huomiotta, lähtökohdan potentiaalienergia on valoportilla kokonaan auton etenemisliikkeen liike-energiaa:

```latex
mgh = \frac{1}{2}mv^2
```

missä $m$ on auton massa ja $g$ putoamiskiihtyvyys. Massa supistuu pois, ja nopeudeksi saadaan

```latex
v = \sqrt{2gh}
```

Nopeus on siis mallin mukaan verrannollinen lähtökorkeuden neliöjuureen. Kun korkeus kaksinkertaistuu, nopeus kasvaa vain kertoimella $\sqrt{2}$. Kuvaaja $v$ lähtökorkeuden $h$ funktiona on kaareva, ja kaarevan kuvaajan muodosta on vaikea nähdä, sopivatko pisteet malliin.

<svg data-fig="model-v" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: auton nopeus v lähtökorkeuden h funktiona energiaperiaatteen mallin mukaan. Kuvaaja alkaa origosta ja kaartuu loivemmaksi korkeuden kasvaessa: nopeus on verrannollinen korkeuden neliöjuureen. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polyline points="90,280 93,261 96,253.5 99,247.5 102,242.5 105,238 108,234 111,230.5 114,227 117,223.5 120,220.5 123,218 126,215 129,212.5 132,210 135,207.5 138,205 141,202.5 144,200.5 147,198 150,196 153,194 156,192 159,190 162,188 165,186 168,184.5 171,182.5 174,180.5 177,179 180,177 183.5,175.5 186.5,174 189.5,172 192.5,170.5 195.5,169 198.5,167.5 201.5,166 204.5,164.5 207.5,163 210.5,161.5 213.5,160 216.5,158.5 219.5,157 222.5,155.5 225.5,154 228.5,152.5 231.5,151.5 234.5,150 237.5,148.5 240.5,147.5 243.5,146 246.5,144.5 249.5,143.5 252.5,142 255.5,141 258.5,139.5 261.5,138.5 264.5,137 267.5,136 270.5,134.5 273.5,133.5 276.5,132 279.5,131 282.5,130 285.5,128.5 288.5,127.5 291.5,126.5 294.5,125 297.5,124 300.5,123 303.5,122 306.5,121 309.5,119.5 312.5,118.5 315.5,117.5 318.5,116.5 321.5,115.5 324.5,114.5 327.5,113 330.5,112 333.5,111 336.5,110 339.5,109 342.5,108 345.5,107 348.5,106 351.5,105 354.5,104 357.5,103 361,102 364,101 367,100 370,99 373,98 376,97 379,96 382,95 385,94 388,93.5 391,92.5 394,91.5 397,90.5 400,89.5 403,88.5 406,87.5 409,87 412,86 415,85 418,84 421,83 424,82.5 427,81.5 430,80.5 433,79.5 436,78.5 439,78 442,77 445,76 448,75.5 451,74.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="372" y="85.5" width="83" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v = \sqrt{2gh}$</div></foreignObject>
</svg>

Siksi malli kannattaa **linearisoida** eli kirjoittaa muotoon, jossa kuvaaja on suora. Kun yhtälön molemmat puolet korotetaan toiseen, saadaan

```latex
v^2 = 2g \cdot h
```

Nopeuden neliö on suoraan verrannollinen lähtökorkeuteen. Kuvaaja $v^2$ lähtökorkeuden $h$ funktiona on mallin mukaan origon kautta kulkeva suora, jonka kulmakerroin on $2g$.

Jos osa energiasta ei näy auton nopeudessa, suora on loivempi. Näin käy, kun energiaa muuttuu sisäenergiaksi, mutta myös ilman häviöitä, jos pyörien pyörimisen energia ei ole pieni. Jos häviävä osuus on sama kaikilla korkeuksilla, malli on $v^2 = kh$, missä kulmakerroin $k$ on pienempi kuin $2g$. Silloin osuus, joka auton potentiaalienergiasta näkyy sen nopeudessa, on

```latex
\frac{E_k}{E_p} = \frac{\frac{1}{2}mv^2}{mgh} = \frac{k}{2g}
```

Pätevätkö malli ja sen oletukset, selviää vasta mittaamalla.

<svg data-fig="model-v2" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: nopeuden neliö v toiseen lähtökorkeuden h funktiona mallin mukaan. Katkoviivalla on origon kautta kulkeva suora v toiseen yhtä kuin 2 g h, joka vastaa liikettä ilman energiahäviöitä. Yhtenäinen suora on loivempi, ja sen kulmakerroin k on pienempi kuin 2 g: se vastaa tilannetta, jossa osa energiasta ei näy auton nopeudessa. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="291" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v^2$</div></foreignObject>
  <polyline points="90,290 451,71.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,290 451,138" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="250" y="68.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$v^2 = 2gh$</div></foreignObject>
  <foreignObject x="318" y="215.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v^2 = kh,\ k < 2g$</div></foreignObject>
</svg>
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona.

::: tuki O
**Ohjattu.** Muutat lähtökorkeutta $h$ siirtämällä lähtökohtaa ylemmäs samalla kaltevalla radalla. Mittaat jokaiselta korkeudelta ajan $t$, jonka auton katolla oleva liuska katkaisee valoportin säteen, ja lasket nopeuden $v = \dfrac{L}{t}$, missä $L$ on liuskan leveys. Vakiona pidät auton, radan kaltevuuden, valoportin paikan ja tavan, jolla päästät auton liikkeelle. Käytä ainakin kuutta lähtökorkeutta mahdollisimman laajalta alueelta ja päästä auto jokaiselta korkeudelta ainakin kolme kertaa.
:::

::: tuki OO
**Osittain ohjattu.** Muuttuja on lähtökorkeus. Päätä itse, mitä korkeuksia käytät, montako toistoa teet kullakin korkeudella ja miten mittaat korkeuden ja nopeuden. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Mistä kohdasta autoa mittaat korkeuden, ja miksi kohdan on oltava sama lähtökohdassa ja valoportilla?
- Miten varmistat, että auto lähtee levosta eikä saa vauhtia sormesta?
- Missä kohdassa rataa valoportti kannattaa pitää, ja miksi sen paikka ei saa muuttua mittausten välillä?
- Kulkeeko auto suoraan, vai osuuko se radan reunoihin? Miten se voisi näkyä tuloksissa?
- Muutatko korkeutta siirtämällä lähtökohtaa samalla kaltevuudella vai muuttamalla kaltevuutta, ja miksi sillä on väliä?
:::

::: tuki O
**Vihje nopeuden mittaamiseen.** Valoportti mittaa ajan, jonka säde on katkaistuna. Nopeus $v = \dfrac{L}{t}$ on auton keskinopeus sinä aikana, kun liuska kulkee säteen läpi. Kun valoportti on radan vaakasuoralla osalla, auton nopeus ei juuri muutu tänä aikana, ja keskinopeus kuvaa hyvin nopeutta portin kohdalla. Mittaa liuskan leveys $L$ huolellisesti, esimerkiksi työntömitalla. Jos valoportin ohjelma laskee nopeuden itse, tarkista, mitä leveyttä se käyttää. Jos valoporttia ei ole, voit kuvata auton hidastettuna videona mitta-asteikon edessä ja määrittää nopeuden kuljetusta matkasta ja kuvien välisestä ajasta.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana: jokainen toisto omaan sarakkeeseensa ja niistä lasketut suureet niiden oikealle puolelle.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa. Kirjaa liuskan leveys $L$ taulukon yläpuolelle.

| $h\ (\text{m})$ | $t\ (\text{s})$, 1. | $t\ (\text{s})$, 2. | $t\ (\text{s})$, 3. | $\bar{t}\ (\text{s})$ | $v\ (\text{m/s})$ | $v^2\ (\text{m}^2/\text{s}^2)$ |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

Mittaa lähtökorkeudet satunnaisessa järjestyksessä, älä pienimmästä suurimpaan. Silloin vähittäinen muutos, esimerkiksi radan tukien painuminen tai renkaiden lämpeneminen, ei näy kuvaajassa järjestelmällisenä vinoumana.
:::

Muista mittausepävarmuus: arvioi, kuinka tarkasti mittaat lähtökorkeuden ja nopeuden määrittämiseen tarvittavat suureet, ja kirjaa arviot ylös. Toistomittausten hajonta kertoo, kuinka paljon auton nopeus vaihtelee samalta korkeudelta. [[apua:fy1-3|Toistomittausten keskiarvo ja epävarmuus]]

## Käsittele tulokset

Testaa mallisi: piirrä mittaustuloksista kuvaaja, jonka pitäisi mallisi mukaan olla origon kautta kulkeva suora, ja määritä sen kulmakerroin. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin suora. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Piirrä ensin kuvaaja, jossa pystyakselilla on nopeus $v$ ja vaaka-akselilla lähtökorkeus $h$, ja katso sen muotoa. Laske sitten jokaiselle korkeudelle nopeuden neliö $v^2$ ja piirrä toinen kuvaaja, jossa pystyakselilla on $v^2$ ja vaaka-akselilla $h$. Sovita suora tähän kuvaajaan.
:::

Kirjoita sovitetun suoran yhtälö ja vastaa:

1. Ovatko pisteet suoralla? Jos eivät, millä lähtökorkeuksilla ne poikkeavat, ja mihin suuntaan?
2. Mikä on kulmakertoimen yksikkö? Vertaa kulmakerrointa mallin ennustamaan arvoon.
3. Kulkeeko suora origon kautta? Jos ei, mistä vakiotermi voi johtua?
4. Kuinka suuri osa auton potentiaalienergiasta näkyy sen nopeudessa?

::: tuki O OO
**Miksi juuri nämä akselit?** Malli $v^2 = 2g \cdot h$ on suoran yhtälö $y = ax$, kun pystyakselille valitaan $v^2$ ja vaaka-akselille $h$. Silloin kulmakertoimen yksikkö on $\dfrac{\text{m}^2/\text{s}^2}{\text{m}} = \text{m/s}^2$, kiihtyvyyden yksikkö, ja häviöttömässä tilanteessa kulmakerroin olisi $2g$. Jos kulmakerroin $k$ on pienempi, osuus $\dfrac{k}{2g}$ potentiaalienergiasta näkyy auton nopeudessa.

**Vakiotermi.** Jos auto kulkee ennen valoporttia matkan vaakasuoraa rataa, se menettää tällä matkalla energiaa saman verran joka korkeudelta. Silloin suora leikkaa vaaka-akselin hieman origon oikealla puolella: auto tarvitsee pienen lähtökorkeuden päästäkseen ylipäätään portille. Vakiotermi voi johtua myös siitä, että korkeus on mitattu lähtökohdassa ja valoportilla auton eri kohdista.

**Kaartuvat pisteet.** Ilmanvastus kasvaa nopeuden kasvaessa, joten se voi taivuttaa suurimpien korkeuksien pisteitä suoran alapuolelle. Jätä sovituksesta pois vain pisteet, joiden poikkeamalle löydät fysikaalisen syyn, ja kerro se raportissa.
:::

Kuvaajan sovitukseen ja $v^2$-sarakkeen laskemiseen voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukkolaskenta]].

## Epävarmuus ja luotettavuus

Ilmoita kulmakerroin muodossa $k \pm \Delta k$ ja sen avulla nopeudessa näkyvän energian osuus epävarmuuksineen. Perustele, miten arvioit epävarmuudet.

::: tuki O OO
Kulmakertoimen epävarmuuden voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta k$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $k_\text{max}$ ja $k_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta k = \dfrac{k_\text{max} - k_\text{min}}{2}$.

Koska $2g$ tunnetaan paljon tarkemmin kuin $k$, osuuden $\dfrac{k}{2g}$ suhteellinen epävarmuus on sama kuin kulmakertoimen: $\dfrac{\Delta k}{k}$. Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.

**Liuskan leveys.** Virhe liuskan leveydessä $L$ ei näy pisteiden hajontana, vaan muuttaa kaikkia nopeuksia samassa suhteessa. Koska nopeus korotetaan toiseen, kulmakertoimen suhteellinen virhe on kaksi kertaa leveyden suhteellinen virhe. Sovitus ei sisällä tätä virhettä, joten lisää se sovituksesta saatuun suhteelliseen epävarmuuteen: $\dfrac{\Delta k}{k} = \left(\dfrac{\Delta k}{k}\right)_\text{sovitus} + 2\cdot\dfrac{\Delta L}{L}$.
:::

Pohdi sitten luotettavuutta konkreettisesti: johtuiko toistojen hajonta mittaamisesta vai siitä, että auto todella kulki eri tavalla, esimerkiksi osui radan reunaan? Mitkä virheet olivat satunnaisia ja mitkä systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet kulmakerrointa? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Tukevatko mittaukset mallia, jossa nopeuden neliö on suoraan verrannollinen lähtökorkeuteen? Onko kulmakerroin epävarmuuksineen sopusoinnussa häviöttömän mallin kanssa, vai näkyykö tuloksissa energiahäviöitä, ja mihin auton potentiaalienergia silloin joutui? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 2 nähdään, että …". Vertaa tulosta ennusteeseesi ja hypoteesiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla (kuvaajista ja tuloksista ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]) ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Hypoteesi ja teoria:** hypoteesisi ja se, miten johdit mallin energiaperiaatteesta ennen mittaamista.
- **Koejärjestely ja menetelmä:** mitä muutit, mitä mittasit ja mitä pidit vakiona, mistä kohdasta autoa mittasit korkeuden ja miten määritit nopeuden.
- **Tulosten käsittely:** miksi valitsit juuri nämä akselit ja miten linearisointi testaa mallia.
- **Tulos:** kulmakerroin ja nopeudessa näkyvän energian osuus epävarmuuksineen oikein pyöristettyinä.
- **Johtopäätökset ja luotettavuus:** tukivatko mittaukset hypoteesia, ja mitkä konkreettiset epävarmuuden lähteet ja energiahäviöt selittävät poikkeamat mallista.

## Laajennus: toinen auto tai lisäkuorma

Häviöttömän mallin mukaan auton massa supistuu pois, eikä nopeus riipu massasta. Se, kuinka suuri osa energiasta ei näy auton nopeudessa, voi kuitenkin riippua autosta. Renkaiden kitka ja ilmanvastus muuttavat energiaa sisäenergiaksi, ja pyörien pyörimisen energia ei ole hävinnyt, mutta se ei näy auton nopeudessa. Nämä eivät ole kaikilla autoilla samanlaisia.

Toista mittaus toisella autolla tai samalla autolla, johon on kiinnitetty lisäkuorma. Muotoile ensin hypoteesi: muuttuuko kulmakerroin, ja mihin suuntaan? Punnitse autot. Määritä uusi kulmakerroin epävarmuuksineen ja vertaa sitä päämittauksen kulmakertoimeen: ovatko tulokset sopusoinnussa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Jos kulmakertoimet eroavat, mikä energiahäviö voisi selittää eron?

::: tuki O OO
**Vihjeitä.** Kiinnitä lisäkuorma tukevasti ja auton keskelle, ettei se siirry eikä auto ala kulkea vinosti. Pidä rata, valoportin paikka ja lähtökorkeudet samoina kuin päämittauksessa, jotta vain auto muuttuu. Jos vaihdat autoa, kiinnitä siihen samanlevyinen liuska tai mittaa uuden liuskan leveys.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Kirjoititko hypoteesin ja mallin ennen mittaamista, ja muuttuivatko ne työn aikana?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Mitä tekisit toisin, jos aloittaisit alusta?
