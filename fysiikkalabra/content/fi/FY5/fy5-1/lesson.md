# Voiman momentti ja kappaleen kiertyminen

> **Miksi** tiukkaan juuttunut pyöränmutteri aukeaa pitkällä avaimella, vaikka lyhyellä avaimella yhtä suuri voima ei saa sitä liikkumaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: autotalli. Auton takapyörän vanteessa on viisi pyöränmutteria. Yhteen mutteriin on asetettu pitkä ristiavain, jonka varsi ulottuu kauas vasemmalle, ja sen päätä painetaan alaspäin punaisella voimanuolella. Lattialla renkaan oikealla puolella on lyhyt kiintoavain." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51h-floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy51h-car" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy51h-rim" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy51h-steel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="40" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="86" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="132" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="178" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="224" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="270" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="316" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="362" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="408" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy51h-floor)"/>
  <rect x="0" y="466" width="1200" height="6" fill="#c9c2b2"/>
  <path d="M520,80 H1200 V330 H975 A205,205 0 0 0 565,330 H520 Q500,330 500,300 V110 Q500,80 520,80 Z" fill="url(#fy51h-car)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M560,120 H1180" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="980" y="170" width="80" height="18" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="770" cy="360" r="182" fill="#1f2933"/>
  <line x1="938" y1="360" x2="950" y2="360" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="932.5" y1="403.5" x2="944" y2="406.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="915.5" y1="444" x2="926" y2="450" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="889" y1="479" x2="897.5" y2="487.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="854" y1="505.5" x2="860" y2="516" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="813.5" y1="522.5" x2="816.5" y2="534" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="770" y1="528" x2="770" y2="540" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="726.5" y1="522.5" x2="723.5" y2="534" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="686" y1="505.5" x2="680" y2="516" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="651" y1="479" x2="642.5" y2="487.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="624.5" y1="444" x2="614" y2="450" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="607.5" y1="403.5" x2="596" y2="406.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="602" y1="360" x2="590" y2="360" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="607.5" y1="316.5" x2="596" y2="313.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="624.5" y1="276" x2="614" y2="270" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="651" y1="241" x2="642.5" y2="232.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="686" y1="214.5" x2="680" y2="204" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="726.5" y1="197.5" x2="723.5" y2="186" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="770" y1="192" x2="770" y2="180" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="813.5" y1="197.5" x2="816.5" y2="186" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="854" y1="214.5" x2="860" y2="204" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="889" y1="241" x2="897.5" y2="232.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="915.5" y1="276" x2="926" y2="270" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="932.5" y1="316.5" x2="944" y2="313.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="770" cy="360" r="120" fill="url(#fy51h-rim)" stroke="#8a96a3" stroke-width="4"/>
  <path d="M755,403.5 L723,457.5 L692,434.5 L733,387.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M724,359.5 L663,345.5 L675,309 L732.5,333.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M756.5,316 L750.5,253.5 L789.5,253.5 L783.5,316 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M807.5,333.5 L865,309 L877,345.5 L816,359.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M807,387.5 L848,434.5 L817,457.5 L785,403.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <circle cx="770" cy="360" r="34" fill="#c4ccd4" stroke="#8a96a3" stroke-width="3"/>
  <polygon points="763,306.5 750,314 737,306.5 737,291.5 750,284 763,291.5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="750" cy="299" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polygon points="835,330 822,337.5 809,330 809,315 822,307.5 835,315" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="822" cy="322.5" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polygon points="835,405 822,412.5 809,405 809,390 822,382.5 835,390" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="822" cy="397.5" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polygon points="763,428.5 750,436 737,428.5 737,413.5 750,406 763,413.5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="750" cy="421" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <path d="M706,349 L306,349 L306,371 L706,371 Z" fill="url(#fy51h-steel)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="306" cy="360" r="11" fill="url(#fy51h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="706" cy="360" r="32" fill="url(#fy51h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <polygon points="725,371 706,382 687,371 687,349 706,338 725,349" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="706" cy="360" r="9.24" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="344" width="90" height="32" rx="14" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <line x1="344" y1="210" x2="344" y2="311" stroke="#c92a2a" stroke-width="7" stroke-linecap="butt"/>
  <path d="M344,340 L330.5,310 L357.5,310 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M1010,532 H1140 V548 H1010 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="1010" cy="540" r="20" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="1010" cy="540" r="9" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1140" cy="540" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
</svg>

## Ydinajatus
Voima voi muuttaa kappaleen liikettä, mutta se voi myös kiertää kappaletta. Kun kappale on kiinni akselissa, kuten ovi saranoissaan, mutteri pultissa tai keinulauta tuessaan, se ei pääse siirtymään vaan voi vain kiertyä akselin ympäri. Tätä akselia kutsutaan **kiertoakseliksi**. Voiman kykyä kiertää kappaletta kiertoakselin ympäri kutsutaan **vääntövaikutukseksi**, ja sen suuruutta mitataan **momentilla** (voiman momentti). Vääntövaikutus ei riipu pelkästään voiman suuruudesta. Siihen vaikuttavat myös voiman suunta ja se, mihin kohtaan kappaletta voima vaikuttaa.

### Ovi ja voiman otekohta
Ovea on helppo avata työntämällä kahvasta, joka on kaukana saranoista. Jos samansuuruisella voimalla työnnetään läheltä saranaa, ovi kääntyy paljon vaikeammin. Jos taas työnnetään oven päästä oven suuntaisesti kohti saranaa, ovi ei käänny lainkaan, vaikka voima on yhtä suuri. Kuvan kolme voimaa $\overline{F}_1$, $\overline{F}_2$ ja $\overline{F}_3$ ovat siis yhtä suuria, mutta niiden vääntövaikutukset saranan suhteen ovat aivan erilaiset.

<svg data-fig="ovi" viewBox="0 0 600 330" role="img" aria-label="Ovi ylhäältä katsottuna. Vasemmalla seinä ja sarana, josta ovi lähtee vaakasuorana lautana oikealle. Kolme yhtä pitkää punaista voimanuolta: F1 kahvan kohdalla kohtisuoraan ovea vastaan, F2 lähellä saranaa samoin kohtisuoraan ja F3 oven päässä oven suuntaisesti kohti saranaa. Katkoviivainen kaari näyttää, mihin suuntaan ovi aukeaa. Kaavakuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-ovi-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy51-ovi-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="24" y="200" width="40" height="110" fill="url(#fy51-ovi-wall)" stroke="#1f2933" stroke-width="2"/>
  <line x1="26" y1="214" x2="62" y2="204" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="234" x2="62" y2="224" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="254" x2="62" y2="244" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="274" x2="62" y2="264" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="294" x2="62" y2="284" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <foreignObject x="9" y="167.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{seinä}$</div></foreignObject>
  <path d="M524,250 A440,440 0 0 0 486,71" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-dasharray="7 6"/>
  <rect x="84" y="242" width="440" height="16" rx="2" fill="url(#fy51-ovi-wood)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="84" cy="250" r="11" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="68.5" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{sarana}$</div></foreignObject>
  <rect x="452" y="258" width="26" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="430" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kahva}$</div></foreignObject>
  <line x1="465" y1="242" x2="465" y2="167" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M465,150 L473,168 L457,168 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="403" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <line x1="150" y1="242" x2="150" y2="167" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,150 L158,168 L142,168 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="167" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <line x1="622" y1="250" x2="547" y2="250" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,250 L548,242 L548,258 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="547.5" y="207.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_3$</div></foreignObject>
  <foreignObject x="183.5" y="15.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ylhäältä katsottuna}$</div></foreignObject>
</svg>

### Voiman varsi
Vääntövaikutuksen ratkaisee voiman **vaikutussuora** eli suora, joka kulkee voiman otekohdan (kohdan, jossa voima vaikuttaa kappaleeseen) kautta voiman suuntaan. **Voiman varsi** $r$ on kiertoakselin kohtisuora etäisyys voiman vaikutussuorasta. Kun voima on kohtisuorassa avaimen vartta vastaan, varsi on sama kuin otekohdan etäisyys $d$ akselista. Kun voima on vinossa, varsi on lyhyempi kuin $d$. Jos vaikutussuora kulkee kiertoakselin kautta, varsi on nolla, eikä voima kierrä kappaletta lainkaan. Siksi oven suuntainen voima $\overline{F}_3$ ei avaa ovea.

<svg data-fig="varsi" viewBox="0 0 600 340" role="img" aria-label="Kiintoavain mutterin ympärillä. Mutterin keskellä on kiertoakseli O. Avaimen varsi osoittaa vaakasuoraan oikealle, ja käsi vetää sitä kohdassa, joka on etäisyyden d päässä akselista. Voima F osoittaa vinosti ylös oikealle, 60 asteen kulmassa varren jatkeeseen nähden. Voiman vaikutussuora on piirretty katkoviivalla molempiin suuntiin. Akselista vaikutussuoralle piirretty kohtisuora jana on voiman varsi r, ja se on lyhyempi kuin d. Kaavakuva." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-varsi-steel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <line x1="308" y1="284" x2="493" y2="-36.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="398" y1="128" x2="468" y2="128" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <path d="M118,138 L404,138 L404,118 L118,118 Z" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="404" cy="128" r="10" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="118" cy="128" r="32" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <polygon points="137,139 118,150 99,139 99,117 118,106 137,117" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="118" cy="128" r="9.24" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="118" y1="128" x2="328" y2="249" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M322,259.5 L311.5,253.5 L317.5,243" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="328" cy="249" r="3.5" fill="#1f2933"/>
  <foreignObject x="191" y="192" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <line x1="118" y1="82" x2="398" y2="82" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="118" y1="74" x2="118" y2="90" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398" y1="74" x2="398" y2="90" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="248" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <line x1="398" y1="128" x2="445.5" y2="45.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M454,31 L452,50.5 L438,42.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="461.5" y="20.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M438,128 A40,40 0 0 0 418,93.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="442" y="87" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <circle cx="398" cy="128" r="4" fill="#1f2933"/>
  <foreignObject x="68" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="313" y="264.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{vaikutussuora}$</div></foreignObject>
</svg>

## Kaava: Voiman momentti
Voiman momentti kiertoakselin suhteen on voiman suuruuden ja voiman varren tulo:
```latex
M = F r
```
missä $M$ on voiman momentti ($\text{Nm}$), $F$ voiman suuruus ($\text{N}$) ja $r$ voiman varsi eli kiertoakselin kohtisuora etäisyys voiman vaikutussuorasta ($\text{m}$). Momentin yksikkö on newtonmetri $\text{Nm}$. Se ei ole sama asia kuin energian yksikkö joule, vaikka molemmat ovat newtonin ja metrin tulo: momentissa etäisyys on kohtisuorassa voimaa vastaan, työssä se on voiman suuntainen siirtymä.

### Kiertosuunta ja etumerkki
Momentilla on suuruuden lisäksi kiertosuunta. Tässä kirjassa vastapäivään kiertävä momentti on positiivinen ja myötäpäivään kiertävä negatiivinen. Kun kappaleeseen vaikuttaa monta voimaa, niiden momentit lasketaan yhteen etumerkkeineen. Saadaan **kokonaismomentti**:
```latex
\Sigma M = M_1 + M_2 + M_3 + \ldots
```
missä $\Sigma M$ on kokonaismomentti ($\text{Nm}$) ja $M_1$, $M_2$, … yksittäisten voimien momentit saman valitun kiertoakselin suhteen ($\text{Nm}$). Jos kiinteän akselin ympäri kiertyvään, levossa olevaan kappaleeseen vaikuttava kokonaismomentti ei ole nolla, kappale alkaa kiertyä kokonaismomentin suuntaan. Milloin kappale pysyy paikallaan, tutkitaan tarkemmin luvussa *Tasapaino kiertymisen suhteen*.

<svg data-fig="suunta" viewBox="0 0 600 320" role="img" aria-label="Kaksi tilannetta vierekkäin. Kummassakin vaakasuora sauva on kiinni akselissa O vasemmasta päästään. Vasemmalla voima F vaikuttaa sauvan oikeaan päähän ylöspäin, ja kaarinuoli akselin ympärillä kiertää vastapäivään: momentti on positiivinen. Oikealla voima vaikuttaa sauvan päähän alaspäin, ja kaarinuoli kiertää myötäpäivään: momentti on negatiivinen." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-suunta-44" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy51-suunta-344" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="300" y1="14" x2="300" y2="306" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="70" y="157" width="200" height="18" rx="4" fill="url(#fy51-suunta-44)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="70" cy="166" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="258" y1="157" x2="258" y2="87" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M258,70 L266,88 L250,88 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="263.5" y="67.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M113,150.5 A46,46 0 0 0 30,143.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M27,150.5 L25.5,136 L36.5,140 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="66" y="19.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vastapäivään}$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M > 0$</div></foreignObject>
  <foreignObject x="34" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <rect x="370" y="157" width="200" height="18" rx="4" fill="url(#fy51-suunta-344)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="370" cy="166" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="558" y1="175" x2="558" y2="245" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M558,262 L550,244 L566,244 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="563.5" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M327,150.5 A46,46 0 0 1 410,143.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M413,150.5 L403.5,140 L414.5,136 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="366" y="19.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{myötäpäivään}$</div></foreignObject>
  <foreignObject x="366" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M < 0$</div></foreignObject>
  <foreignObject x="334" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
</svg>

### Vinon voiman varsi
Usein tiedetään otekohdan etäisyys $d$ kiertoakselista ja kulma $\alpha$, jonka voima muodostaa akselista otekohtaan kulkevan suoran (esimerkiksi avaimen varren jatkeen) kanssa. Akseli, otekohta ja varren kantapiste muodostavat suorakulmaisen kolmion, jonka hypotenuusa on $d$. Varsi on kulman $\alpha$ vastainen kateetti:
```latex
r = d\sin\alpha
```
missä $r$ on voiman varsi ($\text{m}$), $d$ otekohdan etäisyys kiertoakselista ($\text{m}$) ja $\alpha$ voiman ja varren jatkeen välinen kulma. Kun $\alpha = 90^\circ$, $r = d$ ja momentti on suurin. Kun $\alpha = 0^\circ$ tai $\alpha = 180^\circ$, $r = 0$.

<svg data-fig="kulma" viewBox="0 0 600 340" role="img" aria-label="Suorakulmainen kolmio, jonka kärjet ovat kiertoakseli O, voiman otekohta ja akselista vaikutussuoralle piirretyn kohtisuoran kantapiste. Hypotenuusa on akselin ja otekohdan välinen etäisyys d. Kateetti akselista kantapisteeseen on voiman varsi r. Vaikutuskohdan kulma on alfa, sama kulma kuin voiman ja varren jatkeen välillä. Siksi r on d kertaa sini alfa." style="max-width:100%;font-size:24px">
  <path d="M92,104 L422,104 L228.5,266.5 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <line x1="201" y1="289.5" x2="514" y2="27" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="422" y1="104" x2="486" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="92" y1="104" x2="422" y2="104" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="92" y1="104" x2="228.5" y2="266.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M217.5,275.5 L208.5,265 L219.5,256" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="422" y1="104" x2="485.5" y2="50.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M498.5,39.5 L490,57.5 L479.5,45 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="508" y="41" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <circle cx="92" cy="104" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="422" cy="104" r="4.5" fill="#1f2933"/>
  <foreignObject x="56" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="247" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="128" y="186.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <path d="M378,104 A44,44 0 0 0 388.5,132.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="352" y="111.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <path d="M460,104 A38,38 0 0 0 451,79.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="466.5" y="69.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="385" y="271.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r = d\sin\alpha$</div></foreignObject>
</svg>

## Esimerkki
Juuttunutta mutteria avataan kiintoavaimella. Käsi tarttuu varteen $0{,}35\,\text{m}$:n etäisyydellä mutterin keskeltä, joka on kiertoakseli. Käsi vetää vartta $240\,\text{N}$:n voimalla, joka on $65^\circ$:n kulmassa varren jatkeeseen nähden ja kiertää mutteria aukeamissuuntaan. Mutteri aukeaa vasta, kun momentti on vähintään $80\,\text{Nm}$. Kuinka suuri on käden voiman momentti mutterin akselin suhteen, ja aukeaako mutteri?

<!-- vaihe -->

**Tunnetut ja kysytty.** $F = 240\,\text{N}$, $d = 0{,}35\,\text{m}$, $\alpha = 65^\circ$ ja mutterin vaatima momentti $80\,\text{Nm}$. Kysytään voiman momenttia $M$ ja sitä, riittääkö se.

<!-- vaihe -->

**Periaate.** Mutteri voi vain kiertyä akselinsa ympäri, joten voiman vääntövaikutuksen kertoo sen momentti $M = Fr$. Voima on vinossa varteen nähden, joten varsi $r$ on lyhyempi kuin etäisyys $d$: se saadaan suorakulmaisesta kolmiosta, $r = d\sin\alpha$.

<!-- vaihe -->

**Kaava ratkaistuna.** Sijoitetaan varren lauseke momentin kaavaan:
```latex
\begin{aligned}
&M = F r \\
&M = F d\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: voima on newtoneina ja etäisyys metreinä, joten momentti saadaan newtonmetreinä.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
M &= F d\sin\alpha \\
&= 240\,\text{N}\cdot 0{,}35\,\text{m}\cdot\sin 65^\circ \\
&\approx 76{,}1\,\text{Nm}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Voiman momentti on $M \approx 76\,\text{Nm}$, kahden merkitsevän numeron tarkkuudella kuten etäisyys $0{,}35\,\text{m}$. Se on pienempi kuin mutterin vaatima $80\,\text{Nm}$, joten mutteri ei aukea.

<!-- vaihe -->

**Järkevyys.** Jos sama voima vaikuttaisi kohtisuoraan vartta vastaan, varsi olisi koko $0{,}35\,\text{m}$ ja momentti $240\,\text{N}\cdot 0{,}35\,\text{m} = 84\,\text{Nm}$. Vino veto antaa vähemmän, koska $\sin 65^\circ \approx 0{,}91 < 1$. Mutteri aukeaisi siis samalla voimalla, jos vedettäisiin kohtisuoraan vartta vastaan.

## Yleinen virhekäsitys
Momenttia ei saada kertomalla voima etäisyydellä otekohtaan, vaan etäisyydellä vaikutussuoraan. Etäisyys $d$ ja varsi $r$ ovat yhtä suuret vain, kun voima on kohtisuorassa akselista otekohtaan kulkevaa suoraa vastaan. Toinen virhe on ajatella, että pitkä avain lisää voimaa. Käden voima on sama, mutta pitkällä avaimella sen varsi on pidempi, joten momentti on suurempi. Mutterin aukeaminen ei vaadi tiettyä voimaa vaan tietyn momentin.

## Tiivistelmä
- Voiman vääntövaikutusta kiertoakselin suhteen mitataan momentilla $M = Fr$, ja sen yksikkö on newtonmetri $\text{Nm}$.
- Voiman varsi $r$ on kiertoakselin kohtisuora etäisyys voiman vaikutussuorasta, ei etäisyys otekohtaan.
- Vinon voiman varsi on $r = d\sin\alpha$. Voima, jonka vaikutussuora kulkee akselin kautta, ei kierrä kappaletta.
- Vastapäivään kiertävä momentti on positiivinen ja myötäpäivään kiertävä negatiivinen. Kokonaismomentti on momenttien summa etumerkkeineen.
- Jos akselin ympäri kiertyvään, levossa olevaan kappaleeseen vaikuttava kokonaismomentti ei ole nolla, kappale alkaa kiertyä.
