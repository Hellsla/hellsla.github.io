# Magneetit, magneettinen dipoli ja magneettikenttä

> **Miksi** kompassin neula osoittaa metsässä aina pohjoiseen, mutta kääntyy heti muualle, kun sen viereen tuodaan magneetti?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: suunnistuskartta kivellä kuusimetsässä. Kartan päällä on kompassi, ja sen vieressä sauvamagneetti, jonka punertava ja sininen pää näkyvät. Kompassin neula on kääntynyt kohti magneettia eikä osoita kartan pohjoisnuolen suuntaan." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy71h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy71h-moss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#e9c98a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="380" fill="url(#fy71h-sky)"/>
  <path d="M779,114 Q777,83.5 813,87 Q827.5,54.5 863.5,65.5 Q896,47.5 914,81.5 Q946.5,85 943,114 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M246,82 Q245,61.5 269,64 Q278.5,42.5 302.5,49.5 Q324,37.5 336,60.5 Q357.5,63 355,82 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,300 L10.5,267.5 L21.5,300 L32.5,265.5 L44,300 L57.5,254.5 L71.5,300 L85,255.5 L98.5,300 L117.5,232.5 L136.5,300 L151.5,248 L167,300 L182.5,246.5 L198.5,300 L214,246.5 L229.5,300 L245,246.5 L261,300 L276.5,246.5 L292,300 L306,254 L320,300 L338.5,233 L357.5,300 L375,237 L393,300 L405,261 L417.5,300 L434.5,239.5 L452,300 L468.5,243 L485,300 L504,231.5 L523,300 L538,251 L552.5,300 L571,233 L590,300 L605,249 L620,300 L635.5,248.5 L650.5,300 L665.5,249.5 L680.5,300 L692,264.5 L703.5,300 L714.5,265 L726,300 L740,252.5 L754,300 L772.5,234.5 L791,300 L806.5,246.5 L822.5,300 L834,263 L846,300 L861.5,247.5 L877,300 L894.5,239 L911.5,300 L922.5,268 L933,300 L949,244 L965.5,300 L976,267 L987,300 L1001,253.5 L1015,300 L1027.5,261 L1039.5,300 L1056.5,240.5 L1073.5,300 L1090.5,240.5 L1107.5,300 L1125.5,237.5 L1143,300 L1158,250.5 L1172.5,300 L1187,251.5 L1201.5,300 V330 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M0,330 L10,296 L20,330 L34,276 L48.5,330 L61,285 L73,330 L81.5,302 L90.5,330 L99.5,299.5 L108.5,330 L119,294 L129.5,330 L145,271 L160,330 L171.5,289 L183,330 L191.5,303 L200,330 L212,286.5 L224,330 L236.5,284 L249,330 L263,278.5 L276.5,330 L289.5,282 L302.5,330 L311,302.5 L319.5,330 L331,289 L342.5,330 L353.5,291.5 L364,330 L374.5,295 L384.5,330 L396.5,287.5 L408,330 L419,292 L429.5,330 L444.5,273.5 L459.5,330 L473.5,276 L488,330 L499.5,289 L511,330 L526,271.5 L541.5,330 L553,289 L564.5,330 L578.5,277 L592.5,330 L604,288.5 L616,330 L631,271 L646.5,330 L658,289.5 L669,330 L681.5,285 L694,330 L706.5,284.5 L719,330 L729,295 L739,330 L750.5,289.5 L761.5,330 L777,271 L792.5,330 L801,303 L809.5,330 L824,275.5 L838,330 L851,281.5 L864.5,330 L878,278.5 L891.5,330 L902,294.5 L912.5,330 L925,284 L937.5,330 L947.5,295.5 L957.5,330 L971.5,276 L986,330 L997.5,288.5 L1009,330 L1021.5,284 L1034,330 L1045,293 L1055.5,330 L1065,298 L1074.5,330 L1089,274 L1104,330 L1117,280.5 L1130.5,330 L1144,280 L1157.5,330 L1167.5,294 L1178,330 L1188,295.5 L1198,330 L1207.5,298 L1217,330 V360 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <rect x="0" y="350" width="1200" height="250" fill="url(#fy71h-moss)"/>
  <rect x="79.5" y="439" width="21" height="31" fill="#b8622d"/>
  <path d="M-3.5,444 L90,340 L183.5,444 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,340 L183.5,444 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M17,387 L90,283 L163,387 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,283 L163,387 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M38,329.5 L90,210 L142,329.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,210 L142,329.5 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="182" y="406" width="16" height="24" fill="#b8622d"/>
  <path d="M118,410 L190,330 L262,410 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,330 L262,410 H190 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M134,366 L190,286 L246,366 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,286 L246,366 H190 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M150,322 L190,230 L230,322 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,230 L230,322 H190 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1000" y="430" width="20" height="30" fill="#b8622d"/>
  <path d="M920,435 L1010,335 L1100,435 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1010,335 L1100,435 H1010 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M940,380 L1010,280 L1080,380 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1010,280 L1080,380 H1010 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M960,325 L1010,210 L1060,325 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1010,210 L1060,325 H1010 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1111.5" y="405" width="17" height="25" fill="#b8622d"/>
  <path d="M1044.5,409 L1120,325 L1195.5,409 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1120,325 L1195.5,409 H1120 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1061,363 L1120,279 L1179,363 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1120,279 L1179,363 H1120 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1078,316.5 L1120,220 L1162,316.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1120,220 L1162,316.5 H1120 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="294" y="382" width="12" height="18" fill="#b8622d"/>
  <path d="M246,385 L300,325 L354,385 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M300,325 L354,385 H300 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M258,352 L300,292 L342,352 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M300,292 L342,352 H300 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M270,319 L300,250 L330,319 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M300,250 L330,319 H300 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="894.5" y="378" width="11" height="17" fill="#b8622d"/>
  <path d="M849.5,381 L900,325 L950.5,381 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M900,325 L950.5,381 H900 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M861,350 L900,294 L939,350 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M900,294 L939,350 H900 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M872,319.5 L900,255 L928,319.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M900,255 L928,319.5 H900 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M330,560 Q300,470 380,420 Q520,360 700,368 Q860,372 900,450 Q930,520 880,566 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M380,420 Q520,360 700,368 Q860,372 900,450 Q760,410 600,414 Q470,418 380,420 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <g transform="rotate(-6 620 440)">
  <rect x="470" y="380" width="300" height="170" rx="3" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M500,470 q30,-30 70,-12 q30,14 20,40 q-30,24 -66,8 q-30,-14 -24,-36 Z" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M640,400 q50,10 90,40 q20,30 -10,52" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M620,420 q46,12 76,40 q12,22 -10,40" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M690,500 q30,-6 60,10" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <rect x="700" y="392" width="60" height="40" fill="#b2f2bb"/>
  <line x1="500" y1="382" x2="500" y2="548" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="560" y1="382" x2="560" y2="548" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="620" y1="382" x2="620" y2="548" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="680" y1="382" x2="680" y2="548" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="740" y1="382" x2="740" y2="548" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  </g>
  <rect x="560" y="404" width="96" height="150" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5" fill-opacity="0.85"/>
  <circle cx="608" cy="470" r="40" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="608" y1="437" x2="608" y2="432" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="624.5" y1="441.5" x2="627" y2="437" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="636.5" y1="453.5" x2="641" y2="451" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="641" y1="470" x2="646" y2="470" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="636.5" y1="486.5" x2="641" y2="489" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="624.5" y1="498.5" x2="627" y2="503" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="608" y1="503" x2="608" y2="508" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="591.5" y1="498.5" x2="589" y2="503" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="579.5" y1="486.5" x2="575" y2="489" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="575" y1="470" x2="570" y2="470" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="579.5" y1="453.5" x2="575" y2="451" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="591.5" y1="441.5" x2="589" y2="437" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="608" cy="470" r="34" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M638.5,475.5 L607,474.5 L609,465.5 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M607,474.5 L583,468 L584,463.5 L609,465.5 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="608" cy="470" r="2.2" fill="#1f2933"/>
  <path d="M700,486 L800,470 L806,504 L706,520 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M800,470 L900,454 L906,488 L806,504 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
</svg>

## Ydinajatus

### Magneetin navat
Magneetin vaikutus on voimakkain sen päissä, joita sanotaan magneetin navoiksi. Kun sauvamagneetti ripustetaan langasta niin, että se pääsee kääntymään vapaasti, se asettuu pohjois–eteläsuuntaan. Pohjoiseen kääntyvä pää on magneetin **pohjoisnapa** $\text{N}$ ja etelään kääntyvä pää **etelänapa** $\text{S}$. Kahden magneetin samannimiset navat hylkivät toisiaan ja erinimiset navat vetävät toisiaan puoleensa. Magneetit vaikuttavat toisiinsa myös koskematta toisiinsa, ja vaikutus heikkenee nopeasti, kun magneetit loittonevat toisistaan.

### Magneettinen dipoli
Kun sauvamagneetti katkaistaan kahtia, kummastakin palasta tulee kokonainen magneetti, jolla on sekä pohjoisnapa että etelänapa. Sama toistuu, vaikka paloja pilkottaisiin yhä pienemmiksi. Magneetin navat esiintyvät siis aina pareittain: magneetti on **magneettinen dipoli**. Tässä magneettinen vuorovaikutus eroaa sähköisestä. Positiivisen ja negatiivisen sähkövarauksen voi erottaa toisistaan, mutta yksittäistä magneettinapaa ei ole koskaan havaittu.

<svg data-fig="cut-magnet" viewBox="0 0 600 300" role="img" aria-label="Periaatekuva: sauvamagneetti katkaistaan ensin kahtia ja sitten neljään osaan. Jokaisessa palassa on edelleen sekä pohjoisnapa N että etelänapa S samassa järjestyksessä kuin alkuperäisessä magneetissa. Erillistä yksittäistä napaa ei synny." style="max-width:100%;font-size:24px">
  <path d="M115,28 H300 V72 H115 Q110,72 110,67 V33 Q110,28 115,28 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M300,28 H485 Q490,28 490,33 V67 Q490,72 485,72 H300 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="110" y="28" width="380" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="300" y1="28" x2="300" y2="72" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="195" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="385" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="50" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <line x1="300" y1="80" x2="300" y2="120" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <path d="M115,128 H200 V172 H115 Q110,172 110,167 V133 Q110,128 115,128 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M200,128 H285 Q290,128 290,133 V167 Q290,172 285,172 H200 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="110" y="128" width="180" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="200" y1="128" x2="200" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="145" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="235" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M315,128 H400 V172 H315 Q310,172 310,167 V133 Q310,128 315,128 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M400,128 H485 Q490,128 490,133 V167 Q490,172 485,172 H400 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="310" y="128" width="180" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="400" y1="128" x2="400" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="345" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="435" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="50" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$2$</div></foreignObject>
  <line x1="300" y1="180" x2="300" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <path d="M115,228 H150 V272 H115 Q110,272 110,267 V233 Q110,228 115,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M150,228 H185 Q190,228 190,233 V267 Q190,272 185,272 H150 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="110" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="228" x2="150" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="120" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="160" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M215,228 H250 V272 H215 Q210,272 210,267 V233 Q210,228 215,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M250,228 H285 Q290,228 290,233 V267 Q290,272 285,272 H250 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="210" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="250" y1="228" x2="250" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="220" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="260" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M315,228 H350 V272 H315 Q310,272 310,267 V233 Q310,228 315,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M350,228 H385 Q390,228 390,233 V267 Q390,272 385,272 H350 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="310" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="350" y1="228" x2="350" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="320" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="360" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M415,228 H450 V272 H415 Q410,272 410,267 V233 Q410,228 415,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M450,228 H485 Q490,228 490,233 V267 Q490,272 485,272 H450 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="410" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="450" y1="228" x2="450" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="420" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="460" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="50" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$4$</div></foreignObject>
</svg>

### Ferromagnetismi ja alkeisalueet
Magneetti vetää puoleensa rautaa, nikkeliä, kobolttia ja monia niiden seoksia, kuten terästä. Näitä aineita sanotaan **ferromagneettisiksi**. Jokainen niiden atomi on pieni magneettinen dipoli. Ferromagneettisessa aineessa vierekkäisten atomien dipolit asettuvat samansuuntaisiksi, ja aine jakautuu tyypillisesti mikrometrien kokoisiin **alkeisalueisiin**, joissa kaikki atomidipolit osoittavat samaan suuntaan. Magnetoimattomassa raudassa alkeisalueiden suunnat vaihtelevat, joten niiden vaikutukset kumoavat toisensa eikä kappale ole magneetti.

Kun rautakappale tuodaan magneetin lähelle, magneetin kenttä kääntää alkeisalueiden suuntia ja kasvattaa niitä alkeisalueita, joiden suunta on kentän suuntainen. Rauta **magnetoituu**: siitä tulee magneetti, jonka magneetin puoleinen pää on erinimisen navan kaltainen. Siksi magneetti vetää magnetoimatontakin rautanaulaa. Pehmeä rauta menettää magnetoitumansa lähes kokonaan, kun magneetti viedään pois, mutta kovassa teräksessä ja neodyymimagneetin seoksessa alkeisalueet jäävät järjestykseen. Niistä tehdään **kestomagneetteja**.

Kuumennus riittävän korkeaan lämpötilaan, raudalla noin $770\,{}^\circ\text{C}$:n lämpötilaan, sekoittaa järjestyksen, ja ferromagnetismi katoaa.

<svg data-fig="domains" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa: rautakappaleen alkeisalueet. Vasemmalla magnetoimaton rauta, jonka alkeisalueiden magneettiset suunnat, valkoiset nuolet, osoittavat eri suuntiin, joten niiden vaikutukset kumoavat toisensa. Oikealla rautakappaleen viereen on tuotu magneetti pohjoisnapa N edellä. Magneetin kenttä kääntää alkeisalueet ja kasvattaa niitä, joilla on kentän suunta, joten lähes kaikki nuolet osoittavat magneetista poispäin. Rauta on magnetoitunut: sen magneetin puoleinen pää on etelänapa S, ja magneetti vetää sitä." style="max-width:100%;font-size:24px">
  <foreignObject x="20" y="11.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magnetoimaton rauta}$</div></foreignObject>
  <foreignObject x="330" y="11.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magnetoitu rauta}$</div></foreignObject>
  <line x1="300" y1="14" x2="300" y2="326" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="40" y="70" width="220" height="200" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <path d="M101,72 L87,142 L102,210 L92,268" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M156,72 L142,142 L157,210 L147,268" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M211,72 L197,142 L212,210 L202,268" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M42,132.5 L128,143.5 L194,130.5 L258,139.5" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M42,199.5 L128,210.5 L194,197.5 L258,206.5" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M83.5,94.5 L61,102.5 L59,98 L50.5,109.5 L64.5,113 L63,108 L85.5,100 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M119,121.5 L127.5,98.5 L132,100.5 L128.5,86.5 L117,95 L121.5,96.5 L113.5,119 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M162,94 L180,109.5 L177,113.5 L191.5,115 L187,101 L184,105 L165.5,89.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M247.5,114 L230.5,97 L234,93.5 L220,90.5 L222.5,104.5 L226,101 L243,118 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M51,177.5 L74,171.5 L75.5,176 L85,165.5 L71,160.5 L72.5,165.5 L49.5,172 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M126,152 L117.5,174.5 L113,173 L116.5,187 L128,178.5 L123.5,176.5 L131.5,154 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M168.5,154 L176.5,176.5 L172,178.5 L183.5,187 L187,173 L182.5,174.5 L174,152 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M238.5,187 L234.5,163.5 L239.5,162.5 L229.5,152.5 L223.5,165.5 L228.5,164.5 L232.5,188 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M85.5,235 L62,233 L62,228 L49.5,235 L61,244 L61.5,239 L85,241 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M110.5,250.5 L129,235 L132,239 L136.5,225 L122,226.5 L125,230.5 L107,246 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M187,221 L171.5,239.5 L167.5,236 L166,250.5 L180,246.5 L176,243 L191.5,225 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M214.5,233.5 L237,241.5 L235.5,246 L249.5,243 L241,231 L239,236 L216.5,227.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M317,148 H344 V192 H317 Q312,192 312,187 V153 Q312,148 317,148 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M344,148 H371 Q376,148 376,153 V187 Q376,192 371,192 H344 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="312" y="148" width="64" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="344" y1="148" x2="344" y2="192" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="318" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="350" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <rect x="386" y="70" width="194" height="200" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <path d="M440.5,72 L426.5,142 L441.5,210 L431.5,268" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M489,72 L475,142 L490,210 L480,268" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M537.5,72 L523.5,142 L538.5,210 L528.5,268" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M388,132.5 L463.5,143.5 L522,130.5 L578,139.5" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M388,199.5 L463.5,210.5 L522,197.5 L578,206.5" fill="none" stroke="#c4ccd4" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M392,106.5 L416,106.5 L416,111.5 L428,103.5 L416,95.5 L416,100.5 L392,100.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M441.5,109 L465,105.5 L466,110.5 L476.5,101 L463.5,94.5 L464.5,99.5 L440.5,103 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M489,104.5 L513,107 L512.5,112 L525,105 L514,96 L513.5,101 L489.5,98.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M538,106.5 L562,106.5 L562,111.5 L574,103.5 L562,95.5 L562,100.5 L538,100.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M392.5,174 L416.5,172.5 L417,177.5 L428,168.5 L415.5,161.5 L416,166.5 L392,168.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M441,173 L465,173 L465,178 L477,170 L465,162 L465,167 L441,167 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M489,170 L512.5,174 L512,179 L525,173 L514.5,163 L513.5,168 L490,164 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M538,173 L562,173 L562,178 L574,170 L562,162 L562,167 L538,167 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M392.5,241.5 L416.5,239 L417,244 L428,235 L415.5,228 L416,233 L392,235.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M441,239.5 L465,239.5 L465,244.5 L477,236.5 L465,228.5 L465,233.5 L441,233.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M489,238.5 L513,240 L512.5,245 L525,238 L514,229 L513.5,234 L489.5,232.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M538,239.5 L562,239.5 L562,244.5 L574,236.5 L562,228.5 L562,233.5 L538,233.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <foreignObject x="390" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="556" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
</svg>

Useimmat muut aineet, kuten alumiini, kupari, puu, muovi ja vesi, eivät tartu magneettiin: niiden magneettiset vaikutukset ovat niin heikkoja, ettei niitä arkisilla magneeteilla huomaa.

### Magneettikenttä ja kenttäviivat
Magneetti muuttaa ympäröivää tilaa niin, että toinen magneetti tai rautakappale kokee siinä voiman. Tätä magneetin ympärille syntyvää tilaa sanotaan **magneettikentäksi**. Kentän suunta jossakin pisteessä on se suunta, johon pisteeseen asetetun kompassin neulan pohjoispää osoittaa. Kompassi on siis pieni koetinmagneetti, jolla kentän suunnan voi selvittää paikka kerrallaan.

Kenttää havainnollistetaan **kenttäviivoilla**. Kenttäviivan suunta kussakin pisteessä on kentän suunta. Magneetin ulkopuolella kenttäviivat kulkevat pohjoisnavasta etelänapaan ja magneetin sisällä etelänavasta pohjoisnapaan, joten jokainen viiva on suljettu silmukka. Missä viivat ovat tiheässä, kenttä on voimakas. Kenttäviivat eivät koskaan leikkaa toisiaan, koska kentällä on kussakin pisteessä vain yksi suunta.

<svg data-fig="bar-field" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva sauvamagneetin magneettikentästä ylhäältä nähtynä. Vihreät kenttäviivat lähtevät magneetin pohjoisnavasta N, kaartuvat magneetin ympäri ja palaavat etelänapaan S; magneetin sisällä viivat jatkuvat etelänavasta pohjoisnapaan, joten jokainen viiva on suljettu silmukka. Nuolenkärjet näyttävät kentän suunnan. Neljä kompassia magneetin ympärillä kääntyy kenttäviivojen suuntaisiksi: kompassin pohjoispää osoittaa kentän suuntaan. Navoilla viivat ovat tiheimmillään, joten kenttä on siellä voimakkain." style="max-width:100%;font-size:24px">
  <polyline points="387.5,184.5 389.5,184 391.5,183.5 393.5,183.5 395,183 397,182.5 399,182 401,181.5 403,181 405,180.5 407,180 409,180 411,179.5 413,179 414.5,178.5 416.5,178 418.5,177.5 420.5,177 422.5,176.5 424.5,176 426.5,175.5 428.5,175 430.5,174.5 432,174 434,173.5 436,173 438,172.5 440,172 442,171.5 444,171 446,170.5 447.5,170 449.5,169.5 451.5,169 453.5,168.5 455.5,168 457.5,167.5 459.5,167 461.5,166.5 463,166 465,165.5 467,165 469,164.5 471,164 473,163.5 475,163 476.5,162.5 478.5,162 480.5,161.5 482.5,160.5 484.5,160 486.5,159.5 488,159 490,158.5 492,158 494,157.5 496,157 498,156 499.5,155.5 501.5,155 503.5,154.5 505.5,154 507.5,153.5 509.5,153 511,152 513,151.5 515,151 517,150.5 519,150 521,149 522.5,148.5 524.5,148 526.5,147.5 528.5,147 530.5,146 532,145.5 534,145 536,144.5 538,143.5 540,143 541.5,142.5 543.5,142 545.5,141 547.5,140.5 549.5,140 551,139.5 553,138.5 555,138 557,137.5 559,137 560.5,136 562.5,135.5 564.5,135 566.5,134 568,133.5 570,133 572,132 574,131.5 576,131 577.5,130 579.5,129.5 581.5,129 583.5,128 585,127.5" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M513,151.5 L503,160.5 L500,150 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="15,127.5 16.5,128 18.5,129 20.5,129.5 22.5,130 24,131 26,131.5 28,132 30,133 32,133.5 33.5,134 35.5,135 37.5,135.5 39.5,136 41,137 43,137.5 45,138 47,138.5 49,139.5 50.5,140 52.5,140.5 54.5,141 56.5,142 58.5,142.5 60,143 62,143.5 64,144.5 66,145 68,145.5 69.5,146 71.5,147 73.5,147.5 75.5,148 77.5,148.5 79,149 81,150 83,150.5 85,151 87,151.5 89,152 90.5,153 92.5,153.5 94.5,154 96.5,154.5 98.5,155 100.5,155.5 102,156 104,157 106,157.5 108,158 110,158.5 112,159 113.5,159.5 115.5,160 117.5,160.5 119.5,161.5 121.5,162 123.5,162.5 125,163 127,163.5 129,164 131,164.5 133,165 135,165.5 137,166 138.5,166.5 140.5,167 142.5,167.5 144.5,168 146.5,168.5 148.5,169 150.5,169.5 152.5,170 154,170.5 156,171 158,171.5 160,172 162,172.5 164,173 166,173.5 168,174 169.5,174.5 171.5,175 173.5,175.5 175.5,176 177.5,176.5 179.5,177 181.5,177.5 183.5,178 185.5,178.5 187,179 189,179.5 191,180 193,180 195,180.5 197,181 199,181.5 201,182 203,182.5 205,183 206.5,183.5 208.5,183.5 210.5,184 212.5,184.5" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M100.5,155.5 L87,157.5 L90.5,147 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="387.5,195.5 389.5,196 391.5,196.5 393.5,196.5 395,197 397,197.5 399,198 401,198.5 403,199 405,199.5 407,200 409,200 411,200.5 413,201 414.5,201.5 416.5,202 418.5,202.5 420.5,203 422.5,203.5 424.5,204 426.5,204.5 428.5,205 430.5,205.5 432,206 434,206.5 436,207 438,207.5 440,208 442,208.5 444,209 446,209.5 447.5,210 449.5,210.5 451.5,211 453.5,211.5 455.5,212 457.5,212.5 459.5,213 461.5,213.5 463,214 465,214.5 467,215 469,215.5 471,216 473,216.5 475,217 476.5,217.5 478.5,218 480.5,218.5 482.5,219.5 484.5,220 486.5,220.5 488,221 490,221.5 492,222 494,222.5 496,223 498,224 499.5,224.5 501.5,225 503.5,225.5 505.5,226 507.5,226.5 509.5,227 511,228 513,228.5 515,229 517,229.5 519,230 521,231 522.5,231.5 524.5,232 526.5,232.5 528.5,233 530.5,234 532,234.5 534,235 536,235.5 538,236.5 540,237 541.5,237.5 543.5,238 545.5,239 547.5,239.5 549.5,240 551,240.5 553,241.5 555,242 557,242.5 559,243 560.5,244 562.5,244.5 564.5,245 566.5,246 568,246.5 570,247 572,248 574,248.5 576,249 577.5,250 579.5,250.5 581.5,251 583.5,252 585,252.5" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M513,228.5 L500,230 L503,219.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="15,252.5 16.5,252 18.5,251 20.5,250.5 22.5,250 24,249 26,248.5 28,248 30,247 32,246.5 33.5,246 35.5,245 37.5,244.5 39.5,244 41,243 43,242.5 45,242 47,241.5 49,240.5 50.5,240 52.5,239.5 54.5,239 56.5,238 58.5,237.5 60,237 62,236.5 64,235.5 66,235 68,234.5 69.5,234 71.5,233 73.5,232.5 75.5,232 77.5,231.5 79,231 81,230 83,229.5 85,229 87,228.5 89,228 90.5,227 92.5,226.5 94.5,226 96.5,225.5 98.5,225 100.5,224.5 102,224 104,223 106,222.5 108,222 110,221.5 112,221 113.5,220.5 115.5,220 117.5,219.5 119.5,218.5 121.5,218 123.5,217.5 125,217 127,216.5 129,216 131,215.5 133,215 135,214.5 137,214 138.5,213.5 140.5,213 142.5,212.5 144.5,212 146.5,211.5 148.5,211 150.5,210.5 152.5,210 154,209.5 156,209 158,208.5 160,208 162,207.5 164,207 166,206.5 168,206 169.5,205.5 171.5,205 173.5,204.5 175.5,204 177.5,203.5 179.5,203 181.5,202.5 183.5,202 185.5,201.5 187,201 189,200.5 191,200 193,200 195,199.5 197,199 199,198.5 201,198 203,197.5 205,197 206.5,196.5 208.5,196.5 210.5,196 212.5,195.5" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M100.5,224.5 L90.5,233 L87,222.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="384.5,177 386,176 388,175 389.5,174 391.5,173 393,172 395,171 396.5,169.5 398,168.5 400,167.5 401.5,166.5 403,165.5 405,164.5 406.5,163.5 408.5,162 410,161 411.5,160 413.5,159 415,157.5 416.5,156.5 418,155.5 420,154.5 421.5,153 423,152 425,151 426.5,149.5 428,148.5 429.5,147.5 431.5,146 433,145 434.5,144 436,142.5 437.5,141.5 439.5,140 441,139 442.5,138 444,136.5 445.5,135.5 447,134 448.5,133 450.5,131.5 452,130.5 453.5,129 455,128 456.5,126.5 458,125.5 459.5,124 461,122.5 462.5,121.5 464,120 465.5,119 467,117.5 468.5,116 470,115 471.5,113.5 473,112 474.5,111 476,109.5 477.5,108 479,107 480.5,105.5 482,104 483.5,102.5 485,101.5 486.5,100 488,98.5 489.5,97 490.5,96 492,94.5 493.5,93 495,91.5 496.5,90 498,89 499,87.5 500.5,86 502,84.5 503.5,83 505,81.5 506,80 507.5,78.5 509,77 510,75.5 511.5,74.5 513,73 514.5,71.5 515.5,70 517,68.5 518.5,67 519.5,65.5 521,64 522.5,62.5 523.5,61 525,59.5 526,58 527.5,56.5 529,54.5 530,53 531.5,51.5 532.5,50 534,48.5 535,47 536.5,45.5 537.5,44 539,42.5 540,41 541.5,39 542.5,37.5 544,36 545,34.5 546,33 547.5,31.5 548.5,29.5 550,28 551,26.5 552,25 553.5,23.5 554.5,21.5 556,20 557,18.5 558,17 559,15" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M502,84.5 L497.5,97 L489.5,89 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="41,15 42,17 43,18.5 44,20 45.5,21.5 46.5,23.5 48,25 49,26.5 50,28 51.5,29.5 52.5,31.5 54,33 55,34.5 56,36 57.5,37.5 58.5,39 60,41 61,42.5 62.5,44 63.5,45.5 65,47 66,48.5 67.5,50 68.5,51.5 70,53 71,54.5 72.5,56.5 74,58 75,59.5 76.5,61 77.5,62.5 79,64 80.5,65.5 81.5,67 83,68.5 84.5,70 85.5,71.5 87,73 88.5,74.5 90,75.5 91,77 92.5,78.5 94,80 95,81.5 96.5,83 98,84.5 99.5,86 101,87.5 102,89 103.5,90 105,91.5 106.5,93 108,94.5 109.5,96 110.5,97 112,98.5 113.5,100 115,101.5 116.5,102.5 118,104 119.5,105.5 121,107 122.5,108 124,109.5 125.5,111 127,112 128.5,113.5 130,115 131.5,116 133,117.5 134.5,119 136,120 137.5,121.5 139,122.5 140.5,124 142,125.5 143.5,126.5 145,128 146.5,129 148,130.5 149.5,131.5 151.5,133 153,134 154.5,135.5 156,136.5 157.5,138 159,139 160.5,140 162.5,141.5 164,142.5 165.5,144 167,145 168.5,146 170.5,147.5 172,148.5 173.5,149.5 175,151 177,152 178.5,153 180,154.5 182,155.5 183.5,156.5 185,157.5 186.5,159 188.5,160 190,161 191.5,162 193.5,163.5 195,164.5 197,165.5 198.5,166.5 200,167.5 202,168.5 203.5,169.5 205,171 207,172 208.5,173 210.5,174 212,175 214,176 215.5,177" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M108,94.5 L95.5,89.5 L103,82 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="384.5,203 386,204 388,205 389.5,206 391.5,207 393,208 395,209 396.5,210.5 398,211.5 400,212.5 401.5,213.5 403,214.5 405,215.5 406.5,216.5 408.5,218 410,219 411.5,220 413.5,221 415,222.5 416.5,223.5 418,224.5 420,225.5 421.5,227 423,228 425,229 426.5,230.5 428,231.5 429.5,232.5 431.5,234 433,235 434.5,236 436,237.5 437.5,238.5 439.5,240 441,241 442.5,242 444,243.5 445.5,244.5 447,246 448.5,247 450.5,248.5 452,249.5 453.5,251 455,252 456.5,253.5 458,254.5 459.5,256 461,257.5 462.5,258.5 464,260 465.5,261 467,262.5 468.5,264 470,265 471.5,266.5 473,268 474.5,269 476,270.5 477.5,272 479,273 480.5,274.5 482,276 483.5,277.5 485,278.5 486.5,280 488,281.5 489.5,283 490.5,284 492,285.5 493.5,287 495,288.5 496.5,290 498,291 499,292.5 500.5,294 502,295.5 503.5,297 505,298.5 506,300 507.5,301.5 509,303 510,304.5 511.5,305.5 513,307 514.5,308.5 515.5,310 517,311.5 518.5,313 519.5,314.5 521,316 522.5,317.5 523.5,319 525,320.5 526,322 527.5,323.5 529,325.5 530,327 531.5,328.5 532.5,330 534,331.5 535,333 536.5,334.5 537.5,336 539,337.5 540,339 541.5,341 542.5,342.5 544,344 545,345.5 546,347 547.5,348.5 548.5,350.5 550,352 551,353.5 552,355 553.5,356.5 554.5,358.5 556,360 557,361.5 558,363 559,365" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M502,295.5 L489.5,291 L497.5,283 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="41,365 42,363 43,361.5 44,360 45.5,358.5 46.5,356.5 48,355 49,353.5 50,352 51.5,350.5 52.5,348.5 54,347 55,345.5 56,344 57.5,342.5 58.5,341 60,339 61,337.5 62.5,336 63.5,334.5 65,333 66,331.5 67.5,330 68.5,328.5 70,327 71,325.5 72.5,323.5 74,322 75,320.5 76.5,319 77.5,317.5 79,316 80.5,314.5 81.5,313 83,311.5 84.5,310 85.5,308.5 87,307 88.5,305.5 90,304.5 91,303 92.5,301.5 94,300 95,298.5 96.5,297 98,295.5 99.5,294 101,292.5 102,291 103.5,290 105,288.5 106.5,287 108,285.5 109.5,284 110.5,283 112,281.5 113.5,280 115,278.5 116.5,277.5 118,276 119.5,274.5 121,273 122.5,272 124,270.5 125.5,269 127,268 128.5,266.5 130,265 131.5,264 133,262.5 134.5,261 136,260 137.5,258.5 139,257.5 140.5,256 142,254.5 143.5,253.5 145,252 146.5,251 148,249.5 149.5,248.5 151.5,247 153,246 154.5,244.5 156,243.5 157.5,242 159,241 160.5,240 162.5,238.5 164,237.5 165.5,236 167,235 168.5,234 170.5,232.5 172,231.5 173.5,230.5 175,229 177,228 178.5,227 180,225.5 182,224.5 183.5,223.5 185,222.5 186.5,221 188.5,220 190,219 191.5,218 193.5,216.5 195,215.5 197,214.5 198.5,213.5 200,212.5 202,211.5 203.5,210.5 205,209 207,208 208.5,207 210.5,206 212,205 214,204 215.5,203" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M108,285.5 L103,298 L95.5,290.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="378.5,170 380,168.5 381,167 382.5,165.5 383.5,164 385,162 386,160.5 387.5,159 388.5,157.5 389.5,156 391,154 392,152.5 393,151 394,149 395.5,147.5 396.5,146 397.5,144.5 398.5,142.5 400,141 401,139 402,137.5 403,136 404,134 405,132.5 406,130.5 407,129 408,127 409,125.5 410,123.5 411,122 412,120 412.5,118.5 413.5,116.5 414.5,115 415.5,113 416.5,111 417,109.5 418,107.5 419,106 419.5,104 420.5,102 421,100.5 422,98.5 422.5,96.5 423.5,94.5 424,93 425,91 425.5,89 426.5,87 427,85.5 427.5,83.5 428.5,81.5 429,79.5 429.5,78 430,76 430.5,74 431.5,72 432,70 432.5,68 433,66 433.5,64.5 434,62.5 434.5,60.5 435,58.5 435,56.5 435.5,54.5 436,52.5 436.5,50.5 437,48.5 437,46.5 437.5,44.5 438,43 438,41 438.5,39 438.5,37 439,35 439,33 439.5,31 439.5,29 440,27 440,25 440,23 440,21 440.5,19 440.5,17 440.5,15" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M430.5,74 L432,87 L422,83.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="159.5,15 159.5,17 159.5,19 160,21 160,23 160,25 160,27 160.5,29 160.5,31 161,33 161,35 161.5,37 161.5,39 162,41 162,43 162.5,44.5 163,46.5 163,48.5 163.5,50.5 164,52.5 164.5,54.5 165,56.5 165,58.5 165.5,60.5 166,62.5 166.5,64.5 167,66 167.5,68 168,70 168.5,72 169.5,74 170,76 170.5,78 171,79.5 171.5,81.5 172.5,83.5 173,85.5 173.5,87 174.5,89 175,91 176,93 176.5,94.5 177.5,96.5 178,98.5 179,100.5 179.5,102 180.5,104 181,106 182,107.5 183,109.5 183.5,111 184.5,113 185.5,115 186.5,116.5 187.5,118.5 188,120 189,122 190,123.5 191,125.5 192,127 193,129 194,130.5 195,132.5 196,134 197,136 198,137.5 199,139 200,141 201.5,142.5 202.5,144.5 203.5,146 204.5,147.5 206,149 207,151 208,152.5 209,154 210.5,156 211.5,157.5 212.5,159 214,160.5 215,162 216.5,164 217.5,165.5 219,167 220,168.5 221.5,170" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M173.5,87 L164.5,77.5 L175,74 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="378.5,210 380,211.5 381,213 382.5,214.5 383.5,216 385,218 386,219.5 387.5,221 388.5,222.5 389.5,224 391,226 392,227.5 393,229 394,231 395.5,232.5 396.5,234 397.5,235.5 398.5,237.5 400,239 401,241 402,242.5 403,244 404,246 405,247.5 406,249.5 407,251 408,253 409,254.5 410,256.5 411,258 412,260 412.5,261.5 413.5,263.5 414.5,265 415.5,267 416.5,269 417,270.5 418,272.5 419,274 419.5,276 420.5,278 421,279.5 422,281.5 422.5,283.5 423.5,285.5 424,287 425,289 425.5,291 426.5,293 427,294.5 427.5,296.5 428.5,298.5 429,300.5 429.5,302 430,304 430.5,306 431.5,308 432,310 432.5,312 433,314 433.5,315.5 434,317.5 434.5,319.5 435,321.5 435,323.5 435.5,325.5 436,327.5 436.5,329.5 437,331.5 437,333.5 437.5,335.5 438,337 438,339 438.5,341 438.5,343 439,345 439,347 439.5,349 439.5,351 440,353 440,355 440,357 440,359 440.5,361 440.5,363 440.5,365" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M430,304 L421.5,294.5 L431.5,291 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="159.5,365 159.5,363 159.5,361 160,359 160,357 160,355 160,353 160.5,351 160.5,349 161,347 161,345 161.5,343 161.5,341 162,339 162,337 162.5,335.5 163,333.5 163,331.5 163.5,329.5 164,327.5 164.5,325.5 165,323.5 165,321.5 165.5,319.5 166,317.5 166.5,315.5 167,314 167.5,312 168,310 168.5,308 169.5,306 170,304 170.5,302 171,300.5 171.5,298.5 172.5,296.5 173,294.5 173.5,293 174.5,291 175,289 176,287 176.5,285.5 177.5,283.5 178,281.5 179,279.5 179.5,278 180.5,276 181,274 182,272.5 183,270.5 183.5,269 184.5,267 185.5,265 186.5,263.5 187.5,261.5 188,260 189,258 190,256.5 191,254.5 192,253 193,251 194,249.5 195,247.5 196,246 197,244 198,242.5 199,241 200,239 201.5,237.5 202.5,235.5 203.5,234 204.5,232.5 206,231 207,229 208,227.5 209,226 210.5,224 211.5,222.5 212.5,221 214,219.5 215,218 216.5,216 217.5,214.5 219,213 220,211.5 221.5,210" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M174.5,291 L175.5,304 L165.5,300.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="370,165.5 370.5,163.5 371,161.5 371.5,159.5 372,157.5 372.5,155.5 373,153.5 373.5,151.5 374,150 374.5,148 375,146 375,144 375.5,142 376,140 376,138 376.5,136 376.5,134 377,132 377,130 377.5,128 377.5,126 377.5,124 377.5,122 378,120 378,118 378,116 378,114 378,112 378,110 378,108 377.5,106 377.5,104 377.5,102 377,100 377,98 376.5,96 376.5,94 376,92 375.5,90 375.5,88 375,86.5 374.5,84.5 374,82.5 373.5,80.5 373,78.5 372.5,76.5 371.5,74.5 371,73 370.5,71 369.5,69 369,67 368,65.5 367,63.5 366.5,62 365.5,60 364.5,58 363.5,56.5 362.5,55 361.5,53 360.5,51.5 359,49.5 358,48 357,46.5 355.5,45 354.5,43.5 353,42 351.5,40.5 350.5,39 349,37.5 347.5,36 346,35 344.5,33.5 343,32 341.5,31 339.5,30 338,28.5 336.5,27.5 334.5,26.5 333,25.5 331,24.5 329.5,23.5 327.5,23 326,22 324,21 322,20.5 320,20 318.5,19.5 316.5,19 314.5,18.5 312.5,18 310.5,17.5 308.5,17.5 306.5,17 304.5,17 302.5,17 300.5,16.5 298.5,16.5 296.5,17 294.5,17 292.5,17 290.5,17.5 288.5,17.5 286.5,18 284.5,18.5 282.5,19 281,19.5 279,20 277,21 275,21.5 273.5,22.5 271.5,23 269.5,24 268,25 266,26 264.5,27 263,28 261,29 259.5,30.5 258,31.5 256.5,33 255,34 253.5,35.5 252,37 250.5,38 249,39.5 247.5,41 246.5,42.5 245,44 244,45.5 242.5,47.5 241.5,49 240,50.5 239,52 238,54 237,55.5 236,57.5 235,59 234,61 233.5,62.5 232.5,64.5 231.5,66.5 231,68 230,70 229.5,72 228.5,73.5 228,75.5 227.5,77.5 227,79.5 226.5,81.5 226,83.5 225.5,85.5 225,87 224.5,89 224,91 224,93 223.5,95 223,97 223,99 223,101 222.5,103 222.5,105 222.5,107 222,109 222,111 222,113 222,115 222,117 222,119 222,121 222.5,123 222.5,125 222.5,127 223,129 223,131 223,133 223.5,135 223.5,137 224,139 224.5,141 224.5,143 225,145 225.5,147 226,149 226,150.5 226.5,152.5 227,154.5 227.5,156.5 228,158.5 228.5,160.5 229,162.5 229.5,164.5 230,166 231,168 231.5,170" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M290.5,17 L302,11 L303,22 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="370,214.5 370.5,216.5 371,218.5 371.5,220.5 372,222.5 372.5,224.5 373,226.5 373.5,228.5 374,230 374.5,232 375,234 375,236 375.5,238 376,240 376,242 376.5,244 376.5,246 377,248 377,250 377.5,252 377.5,254 377.5,256 377.5,258 378,260 378,262 378,264 378,266 378,268 378,270 378,272 377.5,274 377.5,276 377.5,278 377,280 377,282 376.5,284 376.5,286 376,288 375.5,290 375.5,292 375,293.5 374.5,295.5 374,297.5 373.5,299.5 373,301.5 372.5,303.5 371.5,305.5 371,307 370.5,309 369.5,311 369,313 368,314.5 367,316.5 366.5,318 365.5,320 364.5,322 363.5,323.5 362.5,325 361.5,327 360.5,328.5 359,330.5 358,332 357,333.5 355.5,335 354.5,336.5 353,338 351.5,339.5 350.5,341 349,342.5 347.5,344 346,345 344.5,346.5 343,348 341.5,349 339.5,350 338,351.5 336.5,352.5 334.5,353.5 333,354.5 331,355.5 329.5,356.5 327.5,357 326,358 324,359 322,359.5 320,360 318.5,360.5 316.5,361 314.5,361.5 312.5,362 310.5,362.5 308.5,362.5 306.5,363 304.5,363 302.5,363 300.5,363.5 298.5,363.5 296.5,363 294.5,363 292.5,363 290.5,362.5 288.5,362.5 286.5,362 284.5,361.5 282.5,361 281,360.5 279,360 277,359 275,358.5 273.5,357.5 271.5,357 269.5,356 268,355 266,354 264.5,353 263,352 261,351 259.5,349.5 258,348.5 256.5,347 255,346 253.5,344.5 252,343 250.5,342 249,340.5 247.5,339 246.5,337.5 245,336 244,334.5 242.5,332.5 241.5,331 240,329.5 239,328 238,326 237,324.5 236,322.5 235,321 234,319 233.5,317.5 232.5,315.5 231.5,313.5 231,312 230,310 229.5,308 228.5,306.5 228,304.5 227.5,302.5 227,300.5 226.5,298.5 226,296.5 225.5,294.5 225,293 224.5,291 224,289 224,287 223.5,285 223,283 223,281 223,279 222.5,277 222.5,275 222.5,273 222,271 222,269 222,267 222,265 222,263 222,261 222,259 222.5,257 222.5,255 222.5,253 223,251 223,249 223,247 223.5,245 223.5,243 224,241 224.5,239 224.5,237 225,235 225.5,233 226,231 226,229.5 226.5,227.5 227,225.5 227.5,223.5 228,221.5 228.5,219.5 229,217.5 229.5,215.5 230,214 231,212 231.5,210" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M290.5,363 L303,358 L302,369 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="358.5,164.5 358,162.5 357.5,160.5 357,158.5 356.5,156.5 356.5,154.5 356,152.5 355,150.5 354.5,148.5 354,147 353.5,145 353,143 352,141 351.5,139 350.5,137.5 350,135.5 349,133.5 348,132 347,130 346.5,128.5 345.5,126.5 344,125 343,123.5 342,121.5 341,120 339.5,118.5 338.5,117 337,115.5 335.5,114 334,112.5 332.5,111 331,110 329.5,108.5 328,107.5 326.5,106 325,105 323,104 321.5,103 319.5,102.5 317.5,101.5 316,101 314,100 312,99.5 310,99 308,98.5 306,98.5 304,98 302,98 300,98 298,98 296,98 294,98.5 292,98.5 290,99 288.5,99.5 286.5,100 284.5,100.5 282.5,101.5 281,102 279,103 277,104 275.5,105 274,106 272,107 270.5,108.5 269,109.5 267.5,111 266,112.5 264.5,114 263,115 262,116.5 260.5,118 259.5,120 258,121.5 257,123 256,124.5 255,126.5 254,128 253,130 252,131.5 251,133.5 250.5,135.5 249.5,137 248.5,139 248,141 247.5,142.5 246.5,144.5 246,146.5 245.5,148.5 245,150.5 244.5,152.5 244,154 243.5,156 243,158 242.5,160 242,162 241.5,164 241.5,166 241,168 240.5,170 240.5,172" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M290,98.5 L301.5,92 L302.5,103 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="358.5,215.5 358,217.5 357.5,219.5 357,221.5 356.5,223.5 356.5,225.5 356,227.5 355,229.5 354.5,231.5 354,233 353.5,235 353,237 352,239 351.5,241 350.5,242.5 350,244.5 349,246.5 348,248 347,250 346.5,251.5 345.5,253.5 344,255 343,256.5 342,258.5 341,260 339.5,261.5 338.5,263 337,264.5 335.5,266 334,267.5 332.5,269 331,270 329.5,271.5 328,272.5 326.5,274 325,275 323,276 321.5,277 319.5,277.5 317.5,278.5 316,279 314,280 312,280.5 310,281 308,281.5 306,281.5 304,282 302,282 300,282 298,282 296,282 294,281.5 292,281.5 290,281 288.5,280.5 286.5,280 284.5,279.5 282.5,278.5 281,278 279,277 277,276 275.5,275 274,274 272,273 270.5,271.5 269,270.5 267.5,269 266,267.5 264.5,266 263,265 262,263.5 260.5,262 259.5,260 258,258.5 257,257 256,255.5 255,253.5 254,252 253,250 252,248.5 251,246.5 250.5,244.5 249.5,243 248.5,241 248,239 247.5,237.5 246.5,235.5 246,233.5 245.5,231.5 245,229.5 244.5,227.5 244,226 243.5,224 243,222 242.5,220 242,218 241.5,216 241.5,214 241,212 240.5,210 240.5,208" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M288,281 L301,277.5 L299.5,288 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="346,169.5 344.5,168 343.5,166.5 342,165 340.5,163.5 339,162 338,161 336.5,159.5 335,158 333.5,157 331.5,155.5 330,154.5 328.5,153 327,152 325,151 323.5,150 321.5,149 320,148 318,147 316.5,146.5 314.5,146 312.5,145 310.5,144.5 308.5,144 306.5,144 304.5,143.5 302.5,143.5 300.5,143.5 298.5,143.5 296.5,143.5 294.5,143.5 292.5,144 290.5,144.5 289,145 287,145.5 285,146 283,146.5 281.5,147.5 279.5,148.5 277.5,149.5 276,150 274,151.5 272.5,152.5 271,153.5 269.5,154.5 267.5,156 266,157 264.5,158.5 263,160 261.5,161 260.5,162.5 259,164 257.5,165.5 256,167 255,168.5 253.5,170" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M292.5,143.5 L304.5,137.5 L305,148.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="346,210.5 344.5,212 343.5,213.5 342,215 340.5,216.5 339,218 338,219 336.5,220.5 335,222 333.5,223 331.5,224.5 330,225.5 328.5,227 327,228 325,229 323.5,230 321.5,231 320,232 318,233 316.5,233.5 314.5,234 312.5,235 310.5,235.5 308.5,236 306.5,236 304.5,236.5 302.5,236.5 300.5,236.5 298.5,236.5 296.5,236.5 294.5,236.5 292.5,236 290.5,235.5 289,235 287,234.5 285,234 283,233.5 281.5,232.5 279.5,231.5 277.5,230.5 276,230 274,228.5 272.5,227.5 271,226.5 269.5,225.5 267.5,224 266,223 264.5,221.5 263,220 261.5,219 260.5,217.5 259,216 257.5,214.5 256,213 255,211.5 253.5,210" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M292.5,236.5 L305,231.5 L304.5,242.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="380,190 586,190" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="14,190 220,190" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M225,170 H300 V210 H225 Q220,210 220,205 V175 Q220,170 225,170 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M300,170 H375 Q380,170 380,175 V205 Q380,210 375,210 H300 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="220" y="170" width="160" height="40" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="300" y1="170" x2="300" y2="210" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="250" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="330" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <line x1="230" y1="179" x2="366" y2="179" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <path d="M374,179 l-9,-4.5 v9 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="230" y1="201" x2="366" y2="201" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <path d="M374,201 l-9,-4.5 v9 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="480" cy="190" r="18" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M495,190 L480,194.5 L480,185.5 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M480,194.5 L468,192 L468,188 L480,185.5 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="480" cy="190" r="2.2" fill="#1f2933"/>
  <circle cx="120" cy="112" r="18" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M131.5,121.5 L117,115.5 L123,108.5 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M117,115.5 L109.5,106 L112.5,102.5 L123,108.5 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="120" cy="112" r="2.2" fill="#1f2933"/>
  <circle cx="300" cy="82" r="18" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M285,82 L300,77.5 L300,86.5 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M300,77.5 L312,80 L312,84 L300,86.5 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="300" cy="82" r="2.2" fill="#1f2933"/>
  <circle cx="300" cy="300" r="18" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M285,300 L300,295.5 L300,304.5 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M300,295.5 L312,298 L312,302 L300,304.5 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="300" cy="300" r="2.2" fill="#1f2933"/>
</svg>

### Maan magneettikenttä
Maapallolla on magneettikenttä, joka muistuttaa sauvamagneetin kenttää. Se syntyy Maan ulkoytimen sulan raudan liikkeistä ja niihin liittyvistä sähkövirroista. Kompassin neulan pohjoispää kääntyy kohti maantieteellistä pohjoista. Koska erinimiset navat vetävät toisiaan, maantieteellisen pohjoisnavan lähellä on Maan magneettinen **etelänapa** $\text{S}$, ja maantieteellisen etelänavan lähellä on magneettinen pohjoisnapa $\text{N}$.

Magneettiset navat eivät ole täsmälleen maantieteellisten napojen kohdalla, ja ne vaeltavat hitaasti. Siksi kompassi poikkeaa todellisesta pohjoisesta: Suomessa nykyään etelässä noin $10^\circ$ ja Lapissa noin $15^\circ$ itään. Suomessa kenttäviivat myös painuvat jyrkästi maata kohti, noin $73^\circ$–$79^\circ$ vaakatason alapuolelle. Tätä kulmaa sanotaan **inklinaatioksi**.

<svg data-fig="earth-field" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva, ei mittakaavassa: Maa ja sen magneettikenttä. Maan sisään on piirretty kuviteltu sauvamagneetti, joka on noin kymmenen astetta kallellaan pyörimisakseliin nähden. Sen etelänapa S on maantieteellisen pohjoisnavan lähellä ja pohjoisnapa N maantieteellisen etelänavan lähellä. Vihreät kenttäviivat lähtevät eteläiseltä pallonpuoliskolta ja kaartuvat avaruuden kautta pohjoiselle pallonpuoliskolle. Pohjoisella pallonpuoliskolla oleva kompassi osoittaa pohjoiseen ja viivat painuvat siellä jyrkästi maahan." style="max-width:100%;font-size:24px">
  <circle cx="300" cy="192" r="104" fill="#a9d1f0"/>
  <path d="M270,96 q40,-8 70,10 q22,22 6,46 q-26,10 -36,34 q-20,8 -40,-10 q-26,-24 -24,-50 q4,-22 24,-30 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M310,212 q30,4 40,30 q2,30 -20,48 q-22,6 -30,-20 q-10,-30 10,-58 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="300" cy="192" r="104" fill="none" stroke="#1f2933" stroke-width="3"/>
  <polyline points="381,257 382.5,257 383.5,257 385,256.5 386.5,256.5 387.5,256.5 389,256 390,256 391.5,255.5 392.5,255.5 393.5,255 395,254.5 396,254.5 397.5,254 398.5,253.5 399.5,253 401,252.5 402,252.5 403,252 404.5,251.5 405.5,251 406.5,250 407.5,249.5 408.5,249 409.5,248.5 410.5,248 411.5,247 412.5,246.5 413.5,246 414.5,245 415.5,244.5 416.5,243.5 417.5,243 418.5,242 419,241 420,240.5 421,239.5 421.5,238.5 422.5,238 423,237 424,236 424.5,235 425.5,234 426,233 426.5,232.5 427,231.5 427.5,230.5 428.5,229.5 429,228.5 429.5,227.5 430,226.5 430.5,225 430.5,224 431,223 431.5,222 432,221 432,220 432.5,219 432.5,217.5 433,216.5 433,215.5 433.5,214.5 433.5,213 433.5,212 433.5,211 434,210 434,208.5 434,207.5 434,206.5 434,205.5 433.5,204 433.5,203 433.5,202 433.5,201 433,199.5 433,198.5 432.5,197.5 432.5,196.5 432,195 432,194 431.5,193 431,192 430.5,191 430.5,189.5 430,188.5 429.5,187.5 429,186.5 428.5,185.5 427.5,184.5 427,183.5 426.5,182.5 426,181.5 425,180.5 424.5,179.5 424,178.5 423,177.5 422.5,176.5 421.5,175.5 421,174.5 420,173.5 419,173 418.5,172 417.5,171 416.5,170.5 415.5,169.5 414.5,168.5 413.5,168 412.5,167 411.5,166.5 410.5,165.5 409.5,165 408.5,164 407.5,163.5 406.5,163 405.5,162 404,161.5 403,161 402,160.5 401,159.5 399.5,159 398.5,158.5" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M434,208.5 L438,221 L427,219.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="201.5,225.5 200.5,225 199,224.5 198,223.5 197,223 196,222.5 194.5,222 193.5,221 192.5,220.5 191.5,220 190.5,219 189.5,218.5 188.5,217.5 187.5,217 186.5,216 185.5,215.5 184.5,214.5 183.5,213.5 182.5,213 181.5,212 181,211 180,210.5 179,209.5 178.5,208.5 177.5,207.5 177,206.5 176,205.5 175.5,204.5 175,203.5 174,202.5 173.5,201.5 173,200.5 172.5,199.5 171.5,198.5 171,197.5 170.5,196.5 170,195.5 169.5,194.5 169.5,193 169,192 168.5,191 168,190 168,189 167.5,187.5 167.5,186.5 167,185.5 167,184.5 166.5,183 166.5,182 166.5,181 166.5,180 166,178.5 166,177.5 166,176.5 166,175.5 166,174 166.5,173 166.5,172 166.5,171 166.5,169.5 167,168.5 167,167.5 167.5,166.5 167.5,165 168,164 168,163 168.5,162 169,161 169.5,160 169.5,159 170,157.5 170.5,156.5 171,155.5 171.5,154.5 172.5,153.5 173,152.5 173.5,151.5 174,151 174.5,150 175.5,149 176,148 177,147 177.5,146 178.5,145.5 179,144.5 180,143.5 181,143 181.5,142 182.5,141 183.5,140.5 184.5,139.5 185.5,139 186.5,138 187.5,137.5 188.5,137 189.5,136 190.5,135.5 191.5,135 192.5,134.5 193.5,134 194.5,133 195.5,132.5 197,132 198,131.5 199,131.5 200.5,131 201.5,130.5 202.5,130 204,129.5 205,129.5 206.5,129 207.5,128.5 208.5,128.5 210,128 211,128 212.5,127.5 213.5,127.5 215,127.5 216.5,127 217.5,127 219,127" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M168.5,161.5 L171,174.5 L160.5,172 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="368.5,270.5 370.5,271 372.5,271.5 375,272 377,272.5 379.5,273 381.5,273.5 383.5,274 386,274 388,274.5 390.5,274.5 392.5,274.5 395,274.5 397,274.5 399.5,274.5 401.5,274.5 403.5,274.5 406,274.5 408,274 410.5,274 412.5,273.5 414.5,273 416.5,272.5 419,272 421,271.5 423,271 425,270 427,269.5 429,268.5 431,268 433,267 435,266 436.5,265 438.5,264 440,263 442,262 443.5,260.5 445.5,259.5 447,258 448.5,257 450,255.5 451.5,254 453,253 454.5,251.5 455.5,250 457,248 458,246.5 459.5,245 460.5,243.5 461.5,242 462.5,240 463.5,238.5 464.5,236.5 465,235 466,233 466.5,231 467,229.5 467.5,227.5 468,225.5 468.5,223.5 469,222 469.5,220 469.5,218 469.5,216 470,214 470,212 470,210 470,208 469.5,206.5 469.5,204.5 469,202.5 468.5,200.5 468.5,198.5 468,196.5 467.5,194.5 466.5,193 466,191 465.5,189 464.5,187 463.5,185.5 463,183.5 462,182 461,180 459.5,178.5 458.5,176.5 457.5,175 456,173.5 455,171.5 453.5,170 452,168.5 450.5,167 449,165.5 447.5,164 446,162.5 444,161.5 442.5,160 441,158.5 439,157.5 437,156 435.5,155 433.5,154 431.5,153 429.5,152 427.5,151 425.5,150 423.5,149 421.5,148 419.5,147.5 417.5,146.5 415.5,146 413,145.5 411,145 409,144.5 406.5,144 404.5,143.5 402,143 400,142.5 398,142.5 395.5,142 393.5,142 391,142" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M470,216 L473.5,228.5 L462.5,227 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="209,242 206.5,242 204.5,242 202,241.5 200,241.5 198,241 195.5,240.5 193.5,240 191,239.5 189,239 187,238.5 184.5,238 182.5,237.5 180.5,236.5 178.5,236 176.5,235 174.5,234 172.5,233 170.5,232 168.5,231 166.5,230 164.5,229 163,228 161,226.5 159,225.5 157.5,224 156,222.5 154,221.5 152.5,220 151,218.5 149.5,217 148,215.5 146.5,214 145,212.5 144,210.5 142.5,209 141.5,207.5 140.5,205.5 139,204 138,202 137,200.5 136.5,198.5 135.5,197 134.5,195 134,193 133.5,191 132.5,189.5 132,187.5 131.5,185.5 131.5,183.5 131,181.5 130.5,179.5 130.5,177.5 130,176 130,174 130,172 130,170 130.5,168 130.5,166 130.5,164 131,162 131.5,160.5 132,158.5 132.5,156.5 133,154.5 133.5,153 134,151 135,149 135.5,147.5 136.5,145.5 137.5,144 138.5,142 139.5,140.5 140.5,139 142,137.5 143,136 144.5,134 145.5,132.5 147,131 148.5,130 150,128.5 151.5,127 153,126 154.5,124.5 156.5,123.5 158,122 160,121 161.5,120 163.5,119 165,118 167,117 169,116 171,115.5 173,114.5 175,114 177,113 179,112.5 181,112 183.5,111.5 185.5,111 187.5,110.5 189.5,110 192,110 194,109.5 196.5,109.5 198.5,109.5 200.5,109.5 203,109.5 205,109.5 207.5,109.5 209.5,109.5 212,109.5 214,110 216.5,110 218.5,110.5 220.5,111 223,111.5 225,112 227.5,112.5 229.5,113 231.5,113.5" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M132,156.5 L135,169 L124.5,167 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="355.5,280 358.5,281.5 361.5,283.5 364.5,285 368,287 371,288.5 374.5,290 377.5,291.5 381,293 384.5,294 387.5,295.5 391,296.5 394.5,297.5 398,298.5 402,299 405.5,300 409,300.5 412.5,301 416,301.5 420,302 423.5,302 427,302.5 431,302.5 434.5,302 438,302 441.5,301.5 445,301.5 448.5,301 452,300 455.5,299.5 459,298.5 462.5,297.5 466,296.5 469,295.5 472.5,294 475.5,292.5 478.5,291.5 482,289.5 485,288 487.5,286 490.5,284.5 493,282.5 496,280.5 498.5,278 501,276 503.5,273.5 505.5,271.5 507.5,269 509.5,266.5 511.5,264 513.5,261 515.5,258.5 517,255.5 518.5,253 519.5,250 521,247 522,244 523,241 524,238 524.5,235 525.5,231.5 526,228.5 526,225.5 526.5,222.5 526.5,219 526.5,216 526.5,212.5 526,209.5 525.5,206.5 525,203 524.5,200 523.5,197 522.5,194 521.5,191 520.5,187.5 519,184.5 517.5,182 516,179 514.5,176 512.5,173 510.5,170.5 508.5,167.5 506.5,165 504,162.5 502,160 499.5,157.5 497,155 494.5,152.5 491.5,150.5 489,148.5 486,146.5 483,144.5 480,142.5 477,140.5 474,139 470.5,137.5 467.5,136 464,134.5 460.5,133 457,132 453.5,130.5 450,129.5 446.5,129 443,128 439.5,127 436,126.5 432.5,126 428.5,125.5 425,125.5 421.5,125 418,125 414,125 410.5,125 407,125 403.5,125.5 400,125.5 396,126 392.5,126.5 389,127 386,128 382.5,128.5" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M526.5,222.5 L530.5,235 L520,234 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <polyline points="217.5,255.5 214,256 211,257 207.5,257.5 204,258 200,258.5 196.5,258.5 193,259 189.5,259 186,259 182,259 178.5,259 175,258.5 171.5,258.5 167.5,258 164,257.5 160.5,257 157,256 153.5,255 150,254.5 146.5,253.5 143,252 139.5,251 136,249.5 132.5,248 129.5,246.5 126,245 123,243.5 120,241.5 117,239.5 114,237.5 111,235.5 108.5,233.5 105.5,231.5 103,229 100.5,226.5 98,224 96,221.5 93.5,219 91.5,216.5 89.5,213.5 87.5,211 85.5,208 84,205 82.5,202 81,199.5 79.5,196.5 78.5,193 77.5,190 76.5,187 75.5,184 75,181 74.5,177.5 74,174.5 73.5,171.5 73.5,168 73.5,165 73.5,161.5 74,158.5 74,155.5 74.5,152.5 75.5,149 76,146 77,143 78,140 79,137 80.5,134 81.5,131 83,128.5 84.5,125.5 86.5,123 88.5,120 90.5,117.5 92.5,115 94.5,112.5 96.5,110.5 99,108 101.5,106 104,103.5 107,101.5 109.5,99.5 112.5,98 115,96 118,94.5 121.5,92.5 124.5,91.5 127.5,90 131,88.5 134,87.5 137.5,86.5 141,85.5 144.5,84.5 148,84 151.5,83 155,82.5 158.5,82.5 162,82 165.5,82 169,81.5 173,81.5 176.5,82 180,82 184,82.5 187.5,83 191,83.5 194.5,84 198,85 202,85.5 205.5,86.5 209,87.5 212.5,88.5 215.5,90 219,91 222.5,92.5 225.5,94 229,95.5 232,97 235.5,99 238.5,100.5 241.5,102.5 244.5,104" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M76.5,143.5 L79,156.5 L68.5,153.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M297.5,132.5 L323,137 L313,194.5 L287,189.5 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M287,189.5 L313,194.5 L302.5,251.5 L277,247 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="295" y="148" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="285" y="207" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <line x1="300" y1="54" x2="300" y2="330" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="130" y="15.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maantieteellinen pohjoisnapa}$</div></foreignObject>
  <foreignObject x="140" y="337.5" width="320" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maantieteellinen etelänapa}$</div></foreignObject>
  <circle cx="357" cy="85" r="15" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M349.5,94.5 L353,82.5 L360.5,88 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M353,82.5 L361,76 L364.5,79 L360.5,88 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="357" cy="85" r="2.2" fill="#1f2933"/>
</svg>

## Kaava: Magneettikenttien yhteisvaikutus
Magneettikentän voimakkuutta ja suuntaa kuvaa vektorisuure **magneettivuon tiheys** $\overline{B}$. Sen suunta on kentän suunta ja sen suuruus $B$ kertoo, kuinka voimakas kenttä on. Magneettivuon tiheyden yksikkö on **tesla** $\text{T}$. Teslan määritelmä perustuu magneettikentän voimaan liikkuvaan varaukseen, ja se esitellään luvussa *Varattu hiukkanen sähkö- ja magneettikentässä*. Tesla on suuri yksikkö, joten arkisia kenttiä ilmoitetaan usein millitesloina, $1\,\text{mT} = 10^{-3}\,\text{T}$, tai mikrotesloina, $1\,\mu\text{T} = 10^{-6}\,\text{T}$.

| Kohde | $B$ |
| --- | --- |
| Maa, Etelä-Suomi | noin $52\,\mu\text{T}$ |
| jääkaappimagneetti | noin $5\,\text{mT}$ |
| neodyymimagneetti | noin $0{,}5\,\text{T}$ |
| magneettikuvaus | $1{,}5$–$3\,\text{T}$ |
| laboratoriomagneetti | yli $45\,\text{T}$ |

Maan kentän arvo ($52$–$53\,\mu\text{T}$ Etelä-Suomessa) on World Magnetic Model 2025 -mallista (NOAA ja British Geological Survey), sairaaloiden magneettikuvauslaitteiden kentät ovat tavallisesti $1{,}5\,\text{T}$ tai $3\,\text{T}$, ja yli $45\,\text{T}$:n jatkuvia kenttiä tuotetaan tutkimuslaboratorioissa, esimerkiksi National High Magnetic Field Laboratoryn hybridimagneetilla Yhdysvalloissa. Magneettien arvot ovat suuruusluokkia magneetin pinnalla.

Kun samaan pisteeseen vaikuttaa kaksi magneettikenttää, kokonaiskenttä on niiden vektorisumma:
```latex
\overline{B} = \overline{B}_1 + \overline{B}_2
```
missä $\overline{B}_1$ ja $\overline{B}_2$ ovat kenttien magneettivuon tiheydet (T) ja $\overline{B}$ kokonaiskenttä (T). Kompassin neula kääntyy kokonaiskentän suuntaiseksi. Kun kentät ovat kohtisuorassa toisiaan vastaan, kokonaiskentän suuruus saadaan Pythagoraan lauseesta ja suunta tangentista:
```latex
\begin{aligned}
B &= \sqrt{B_1^2 + B_2^2} \\
\tan\theta &= \frac{B_2}{B_1}
\end{aligned}
```
missä $\theta$ on kokonaiskentän ja kentän $\overline{B}_1$ välinen kulma.

Tätä käytetään kompassimittauksessa. Kompassin kohdalla Maan kentän vaakakomponentti $\overline{B}_\text{h}$ osoittaa pohjoiseen. Kun magneetti asetetaan niin, että sen kenttä $\overline{B}_\text{m}$ on kompassin kohdalla itään, neula kääntyy pohjoisesta itään kulman $\theta$, jolle $\tan\theta = B_\text{m} : B_\text{h}$. Magneetin kentän voi siis mitata kompassilla, kun Maan kentän vaakakomponentti tunnetaan.

<svg data-fig="vector-sum" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva mittakaavassa, ylhäältä nähtynä: kompassin kohdalla Maan magneettikentän vaakakomponentti B_h = 14 µT osoittaa pohjoiseen eli ylöspäin ja magneetin kenttä B_m = 20 µT itään eli oikealle, kohti oikealla olevan magneetin etelänapaa S. Kenttien summa B on suorakulmion lävistäjä, ja kompassin neula kääntyy sen suuntaiseksi kulman θ verran pohjoisesta itään." style="max-width:100%;font-size:24px">
  <line x1="150" y1="182" x2="290" y2="182" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="290" y1="280" x2="290" y2="182" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="150" y1="280" x2="150" y2="196" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M150,182 L157,197 L143,197 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="150" y1="280" x2="276" y2="280" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M290,280 L275,287 L275,273 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="150" y1="280" x2="277" y2="191" stroke="#2b8a3e" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,182 L280.5,198 L271.5,185.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="150" cy="280" r="28" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M170.5,265.5 L152.5,283.5 L147.5,276.5 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M152.5,283.5 L135,293.5 L132.5,289.5 L147.5,276.5 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.2" stroke-linejoin="round"/>
  <circle cx="150" cy="280" r="2.2" fill="#1f2933"/>
  <path d="M150,218 A62,62 0 0 1 201,244.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="170" y="183.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="93" y="216.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\overline{B}_\text{h}$</div></foreignObject>
  <foreignObject x="217.5" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{B}_\text{m}$</div></foreignObject>
  <foreignObject x="302" y="151.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{B}$</div></foreignObject>
  <path d="M385,260 H455 V300 H385 Q380,300 380,295 V265 Q380,260 385,260 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M455,260 H525 Q530,260 530,265 V295 Q530,300 525,300 H455 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="380" y="260" width="150" height="40" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="455" y1="260" x2="455" y2="300" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="482.5" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <line x1="560" y1="130" x2="560" y2="73" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M560,60 L566.5,74 L553.5,74 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="456" y="19.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{pohjoinen}$</div></foreignObject>
</svg>

Maan kenttä osoittaa Suomessa vinosti maahan. Kompassin neula kääntyy vain vaakatasossa, joten vain kentän vaakakomponentti kääntää sitä. Kun kentän suuruus on $B$ ja inklinaatio $I$, komponentit ovat
```latex
\begin{aligned}
B_\text{h} &= B\cos I \\
B_\text{v} &= B\sin I
\end{aligned}
```
missä $B_\text{h}$ on vaakakomponentti ja $B_\text{v}$ pystykomponentti. Etelä-Suomessa $B \approx 52\,\mu\text{T}$ ja $I \approx 74^\circ$, joten vaakakomponentti on vain noin $14\,\mu\text{T}$ ja pystykomponentti noin $50\,\mu\text{T}$. Nämä ovat kurssin pyöristetyt arvot: tarkempi malli antaa Helsingissä vaakakomponentiksi noin $15\,\mu\text{T}$.

<svg data-fig="inclination" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva mittakaavassa, sivulta nähtynä: Etelä-Suomessa Maan magneettikenttä B = 52 µT osoittaa pohjoiseen ja 74 astetta vaakatason alapuolelle. Kentän vaakakomponentti B_h on noin 14 µT ja pystykomponentti B_v noin 50 µT. Kompassi kääntyy vain vaakakomponentin mukaan." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy71-soil" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="14" y="92" width="572" height="234" fill="url(#fy71-soil)"/>
  <line x1="14" y1="92" x2="586" y2="92" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="456" y="55.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{maanpinta}$</div></foreignObject>
  <line x1="260" y1="92" x2="260" y2="302" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="200" y1="302" x2="260" y2="302" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="200" y1="92" x2="248" y2="92" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M260,92 L247,98 L247,86 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="200" y1="92" x2="200" y2="288" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M200,302 L193,287 L207,287 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="200" y1="92" x2="256" y2="286.5" stroke="#2b8a3e" stroke-width="4" stroke-linecap="butt"/>
  <path d="M260,302 L248,287.5 L263,283.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M244,92 A44,44 0 0 1 212,134.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="244" y="107.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="207.5" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{B}_\text{h}$</div></foreignObject>
  <foreignObject x="143" y="197.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\overline{B}_\text{v}$</div></foreignObject>
  <foreignObject x="274" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{B}$</div></foreignObject>
  <line x1="380" y1="40" x2="457" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M470,40 L456,46.5 L456,33.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="236" y="25.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{pohjoinen}$</div></foreignObject>
</svg>

## Esimerkki
Kompassi on vaakasuoralla pöydällä Etelä-Suomessa, missä Maan magneettikentän vaakakomponentti on $14\,\mu\text{T}$. Pöydälle asetetaan sauvamagneetti kompassin itäpuolelle itä–länsi-suuntaisesti niin, että magneetin etelänapa $\text{S}$ on kompassia kohti. Kompassin neula kääntyy $52^\circ$ pohjoisesta itään. Kuinka suuri on magneetin magneettivuon tiheys kompassin kohdalla?

<!-- vaihe -->

**Tunnetut ja kysytty.** Maan kentän vaakakomponentti $B_\text{h} = 14\,\mu\text{T}$ pohjoiseen ja neulan kääntymiskulma $\theta = 52^\circ$ itään. Kysytään magneetin magneettivuon tiheyttä $B_\text{m}$ kompassin kohdalla.

<!-- vaihe -->

**Periaate.** Kompassin neula kääntyy kokonaiskentän suuntaiseksi. Magneetin kenttä osoittaa kompassin kohdalla kohti magneetin etelänapaa eli itään, joten se on kohtisuorassa pohjoiseen osoittavaa Maan kentän vaakakomponenttia vastaan. Kokonaiskenttä on suorakulmion lävistäjä, ja kulman $\theta$ tangentti on vastaisen ja viereisen kateetin suhde.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
\tan\theta &= \frac{B_\text{m}}{B_\text{h}} \\
B_\text{m} &= B_\text{h}\tan\theta
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: $\tan\theta$ on pelkkä luku, joten $B_\text{m}$ saadaan samassa yksikössä kuin $B_\text{h}$ eli mikrotesloina. Tarvittaessa $1\,\mu\text{T} = 10^{-6}\,\text{T}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
B_\text{m} &= B_\text{h}\tan\theta \\
&= 14\,\mu\text{T} \cdot \tan 52^\circ \\
&= 14\,\mu\text{T} \cdot 1{,}280 \\
&= 17{,}9\,\mu\text{T}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Magneetin magneettivuon tiheys kompassin kohdalla on noin $18\,\mu\text{T} = 1{,}8 \cdot 10^{-5}\,\text{T}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska vaakakomponentti $14\,\mu\text{T}$ ja kulma $52^\circ$ tunnetaan kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Kulmalla $45^\circ$ magneetin kenttä olisi yhtä suuri kuin $B_\text{h}$. Kulma on yli $45^\circ$, joten $B_\text{m}$ on suurempi kuin $14\,\mu\text{T}$, kuten tulos. Kokonaiskenttä on $\sqrt{(14\,\mu\text{T})^2 + (17{,}9\,\mu\text{T})^2} \approx 22{,}7\,\mu\text{T}$, ja saman antaa $B_\text{h} : \cos 52^\circ$. Kenttä on Maan kentän suuruusluokkaa, mikä sopii magneetille, joka on noin kymmenen senttimetrin päässä.

## Yleinen virhekäsitys
Moni ajattelee, että maantieteellisen pohjoisnavan lähellä on Maan magneettinen pohjoisnapa, koska kompassi osoittaa sinne. Kompassin neulan pohjoispää on kuitenkin magneetin pohjoisnapa, ja sitä vetää puoleensa eriniminen napa. Maantieteellisen pohjoisnavan lähellä on siis magneettinen etelänapa.

Toinen virhe on luulla, että magneetin navat voi erottaa katkaisemalla magneetin keskeltä. Katkaisukohtaan syntyy kaksi uutta napaa, ja kummastakin palasta tulee kokonainen dipoli. Kolmas virhe on ajatella, että magneetti vetää kaikkia metalleja. Alumiinitölkki tai kuparikolikko ei tartu magneettiin, koska ne eivät ole ferromagneettisia.

Laskuissa yleisin virhe on laskea kohtisuorat kentät yhteen kuin lukuja. Kentät $14\,\mu\text{T}$ pohjoiseen ja $18\,\mu\text{T}$ itään antavat kokonaiskentän $\sqrt{(14\,\mu\text{T})^2 + (18\,\mu\text{T})^2} \approx 23\,\mu\text{T}$, ei $32\,\mu\text{T}$.

## Tiivistelmä
- Magneetilla on aina kaksi napaa, pohjoisnapa $\text{N}$ ja etelänapa $\text{S}$: se on magneettinen dipoli. Samannimiset navat hylkivät ja erinimiset vetävät toisiaan, eikä yksittäistä napaa ole havaittu.
- Ferromagneettisissa aineissa, kuten raudassa, atomidipolit muodostavat alkeisalueita. Magneetin kenttä järjestää ne, jolloin aine magnetoituu ja magneetti vetää sitä.
- Magneettikentän suunta on se, johon kompassin neulan pohjoispää osoittaa. Kenttäviivat kulkevat magneetin ulkopuolella pohjoisnavasta etelänapaan, ja niiden tiheys kertoo kentän voimakkuuden.
- Maantieteellisen pohjoisnavan lähellä on Maan magneettinen etelänapa. Suomessa Maan kenttä on noin $52\,\mu\text{T}$ ja osoittaa jyrkästi maahan.
- Magneettivuon tiheys $\overline{B}$ on vektori, jonka yksikkö on tesla $\text{T}$. Kentät lasketaan yhteen vektoreina: kohtisuorille kentille $B = \sqrt{B_1^2 + B_2^2}$ ja $\tan\theta = B_2 : B_1$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: jääkaapin ovi, jossa magneetit pitävät kiinni lapsen piirustusta ja kauppalistaa. Oven teräslevy vetää magneetteja puoleensa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy71s-door" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="#f1dfb5"/>
  <rect x="150" y="14" width="300" height="332" rx="14" fill="url(#fy71s-door)" stroke="#1f2933" stroke-width="3"/>
  <rect x="420" y="120" width="14" height="120" rx="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="120" x2="450" y2="120" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <rect x="190" y="150" width="120" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M210,260 V220 L240,196 L270,220 V260 Z" fill="#b8622d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="285" cy="172" r="12" fill="#f2a69c"/>
  <rect x="330" y="170" width="80" height="120" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="342" y1="195" x2="398" y2="195" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="342" y1="215" x2="398" y2="215" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="342" y1="235" x2="398" y2="235" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="342" y1="255" x2="398" y2="255" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="234" y="137" width="16" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <rect x="250" y="137" width="16" height="18" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <rect x="354" y="155" width="16" height="18" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <rect x="370" y="155" width="16" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <rect x="204" y="41" width="16" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <rect x="220" y="41" width="16" height="18" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <rect x="344" y="51" width="16" height="18" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <rect x="360" y="51" width="16" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
</svg>
