# Aineen lämpeneminen ja jäähtyminen: Q = cmΔT

> **Miksi** uimarannan hiekka polttaa jalkapohjia jo aamupäivällä, kun vesi on vielä viileää, vaikka aurinko on paistanut molempiin yhtä kauan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: järven uimaranta aamupäivällä. Aurinko paistaa sekä hiekkaan että veteen. Hiekan yllä väreilee kuumuus, ja hiekkaan pistetyn lämpömittarin punainen pylväs on korkealla. Rantaveteen pistetyn lämpömittarin pylväs on matalalla, koska vesi on vielä viileää." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy36h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy36h-lake" gradientUnits="userSpaceOnUse" x1="0" y1="300" x2="0" y2="600"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy36h-sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy36h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><pattern id="fy36h-grain" width="22" height="16" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.8" fill="#a97a35"/><circle cx="15" cy="11" r="1.4" fill="#a97a35"/><circle cx="12" cy="3" r="1" fill="#8a5f22"/></pattern></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy36h-sky)"/>
  <circle cx="250" cy="118" r="96" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M319.5,144 L350.5,145 L323.5,130.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M297.5,175.5 L323.5,191.5 L307.5,165.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M262.5,191.5 L277,218.5 L276,187.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M224,187.5 L223,218.5 L237.5,191.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M192.5,165.5 L176.5,191.5 L202.5,175.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M176.5,130.5 L149.5,145 L180.5,144 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M180.5,92 L149.5,91 L176.5,105.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M202.5,60.5 L176.5,44.5 L192.5,70.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M237.5,44.5 L223,17.5 L224,48.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M276,48.5 L277,17.5 L262.5,44.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M307.5,70.5 L323.5,44.5 L297.5,60.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M323.5,105.5 L350.5,91 L319.5,92 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="250" cy="118" r="60" fill="url(#fy36h-sun)"/>
  <path d="M670,112 Q668,78 708,82 Q724,46 764,58 Q800,38 820,76 Q856,80 852,112 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M947,164 Q945.5,140 973.5,143 Q985,118 1013,126 Q1038,112 1052,139 Q1077,141.5 1074.5,164 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,292 L11,264.5 L22.5,292 L32.5,268 L42.5,292 L57,253.5 L72,292 L81.5,270.5 L90.5,292 L103,261.5 L115,292 L124.5,270 L134,292 L143,271 L152.5,292 L169,247 L185.5,292 L198.5,258.5 L211.5,292 L228.5,246 L245,292 L260,253.5 L274.5,292 L289.5,251 L305,292 L321,249 L337,292 L349.5,260.5 L362,292 L372.5,266 L383.5,292 L400,247 L416.5,292 L431,254 L445.5,292 L455,270 L464.5,292 L477,259 L490,292 L500,267.5 L510.5,292 L521.5,265.5 L532.5,292 L547,253 L562,292 L575,259 L587.5,292 L598,267.5 L608,292 L622.5,255 L636.5,292 L646,269 L656,292 L668,263 L679.5,292 L693.5,255.5 L707.5,292 L724,246.5 L741,292 L750.5,269.5 L760,292 L775,252.5 L790,292 L804,254.5 L818.5,292 L828,269.5 L837.5,292 L851,257 L864.5,292 L875.5,266 L886,292 L901.5,251 L917,292 L931.5,253 L946.5,292 L956.5,269 L966,292 L978.5,260 L991,292 L1002.5,264 L1014,292 L1030,248.5 L1046.5,292 L1062.5,247.5 L1079,292 L1091,262.5 L1102.5,292 L1118.5,249.5 L1134,292 L1147.5,258 L1160.5,292 L1172,263.5 L1183.5,292 L1194,267.5 L1204,292 V322 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M0,306 L7.5,289.5 L14.5,306 L25,281 L35,306 L47,274.5 L59.5,306 L66.5,290 L73.5,306 L81,290 L88,306 L96.5,286 L105,306 L114,285 L122.5,306 L132.5,282 L142.5,306 L149.5,290.5 L156.5,306 L167,280.5 L177,306 L190,272 L203,306 L214.5,276.5 L226,306 L238.5,273.5 L251,306 L261,282 L271,306 L278.5,289 L286,306 L293,290.5 L300,306 L312.5,273 L325.5,306 L333,288.5 L340.5,306 L348,290 L355,306 L366.5,277.5 L377.5,306 L385,290.5 L392,306 L401.5,282.5 L411,306 L418.5,290 L425.5,306 L438,274 L450.5,306 L462,277 L473.5,306 L483.5,281.5 L493.5,306 L506,272.5 L519,306 L528,285.5 L536.5,306 L545,286 L553.5,306 L561.5,288.5 L569,306 L578,284 L587,306 L596,284.5 L605,306 L616.5,276.5 L628,306 L635.5,289.5 L643,306 L654.5,276 L666.5,306 L676,282 L686,306 L697.5,276 L709.5,306 L720.5,278 L731.5,306 L744.5,272.5 L757.5,306 L765,288.5 L773,306 L785,274 L797.5,306 L809.5,276 L821,306 L834,272 L847,306 L858,277.5 L869.5,306 L881,276 L893,306 L903.5,279.5 L914,306 L923.5,283 L933,306 L945.5,272.5 L958.5,306 L969.5,278 L980.5,306 L988,289.5 L995.5,306 L1003,288.5 L1010.5,306 L1019.5,284.5 L1028.5,306 L1036.5,287.5 L1044.5,306 L1055.5,278 L1066.5,306 L1077,280 L1088,306 L1095.5,288.5 L1103,306 L1113.5,280 L1124,306 L1133.5,282.5 L1143,306 L1151.5,287 L1159.5,306 L1169,284 L1178,306 L1189,277.5 L1200.5,306 V336 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <rect x="0" y="300" width="1200" height="300" fill="url(#fy36h-lake)"/>
  <path d="M640,340 q22.5,-6 45,0 t45,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <path d="M860,330 q30,-6 60,0 t60,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <path d="M1040,362 q20,-6 40,0 t40,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <path d="M760,392 q35,-6 70,0 t70,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <path d="M980,428 q27.5,-6 55,0 t55,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <path d="M900,500 q37.5,-6 75,0 t75,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <path d="M1080,540 q22.5,-6 45,0 t45,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <path d="M0,330 C260,336 470,402 610,470 C700,514 760,560 790,600 H0 Z" fill="#d9b26a" stroke-linejoin="round"/>
  <path d="M0,340 C250,348 450,410 585,474 C670,516 726,562 752,600 H0 Z" fill="url(#fy36h-sand)" stroke-linejoin="round"/>
  <path d="M0,340 C250,348 450,410 585,474 C670,516 726,562 752,600 H0 Z" fill="url(#fy36h-grain)" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M0,330 C260,336 470,402 610,470 C700,514 760,560 790,600" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <ellipse cx="318" cy="590" rx="13" ry="7" transform="rotate(-22 318 590)" fill="#a97a35" fill-opacity="0.45"/>
  <ellipse cx="392" cy="560" rx="13" ry="7" transform="rotate(-22 392 560)" fill="#a97a35" fill-opacity="0.45"/>
  <ellipse cx="420" cy="532" rx="13" ry="7" transform="rotate(-22 420 532)" fill="#a97a35" fill-opacity="0.45"/>
  <ellipse cx="496" cy="506" rx="13" ry="7" transform="rotate(-22 496 506)" fill="#a97a35" fill-opacity="0.45"/>
  <ellipse cx="524" cy="484" rx="13" ry="7" transform="rotate(-22 524 484)" fill="#a97a35" fill-opacity="0.45"/>
  <path d="M40,486 L220,470 L262,540 L70,562 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M46,501 L228.5,484 L233.5,492.5 L49.5,510.5 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M53.5,520 L239,501.5 L244,510 L57,529.5 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M61,539 L249.5,519 L254.5,527.5 L64.5,548.5 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M40,486 L220,470 L262,540 L70,562 Z" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M230,446 q-12,-16 0,-32 t0,-32 t0,-32" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M300,446 q-12,-16 0,-32 t0,-32 t0,-32" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M370,446 q-12,-16 0,-32 t0,-32 t0,-32" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <rect x="441" y="350" width="18" height="150" rx="9" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="450" cy="500" r="16" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <rect x="446" y="372" width="8" height="128" fill="#c92a2a"/>
  <line x1="459" y1="480" x2="467" y2="480" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="460" x2="467" y2="460" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="440" x2="467" y2="440" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="420" x2="467" y2="420" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="400" x2="467" y2="400" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="380" x2="467" y2="380" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="450" cy="504" rx="40" ry="12" fill="#d9b26a"/>
  <ellipse cx="450" cy="500" rx="30" ry="8" fill="url(#fy36h-grain)"/>
  <rect x="871" y="370" width="18" height="150" rx="9" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="880" cy="520" r="16" fill="#f2a69c" stroke="#1f2933" stroke-width="3"/>
  <rect x="876" y="454" width="8" height="66" fill="#f2a69c"/>
  <line x1="889" y1="500" x2="897" y2="500" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="889" y1="480" x2="897" y2="480" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="889" y1="460" x2="897" y2="460" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="889" y1="440" x2="897" y2="440" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="889" y1="420" x2="897" y2="420" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="889" y1="400" x2="897" y2="400" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="840" y="482" width="80" height="118" fill="url(#fy36h-lake)" fill-opacity="0.8"/>
  <ellipse cx="880" cy="482" rx="30" ry="6" fill="none" stroke="#ffffff" stroke-width="3"/>
</svg>

## Ydinajatus
Kun kappaleeseen siirtyy lämpöä, sen sisäenergia kasvaa ja lämpötila nousee. Kokeissa havaitaan, että tarvittava lämpömäärä on suoraan verrannollinen sekä lämpötilan muutokseen että kappaleen massaan: kaksi kertaa suurempi lämpötilan nousu vaatii kaksinkertaisen lämpömäärän, ja kaksinkertainen vesimäärä vaatii kaksinkertaisen lämpömäärän. Lisäksi lämpömäärä riippuu aineesta. Kilogramman veden lämmittäminen yhdellä asteella vaatii noin 4,2 kJ, mutta kilogramman raudan lämmittäminen vain noin 0,45 kJ. Aineelle ominainen kerroin on ominaislämpökapasiteetti $c$, jonka yksikkö on J/(kg·K). Se kertoo, kuinka paljon energiaa tarvitaan yhden kilogramman lämmittämiseen yhdellä kelvinillä, ja sama määrä vapautuu, kun aine jäähtyy yhden kelvinin.

Tärkeä syy on, että veden ominaislämpökapasiteetti on poikkeuksellisen suuri: vesi lämpenee auringossa hitaasti ja jäähtyy illalla hitaasti, kun taas hiekka, jonka $c$ on noin viidesosa veden arvosta, kuumenee samalla energialla moninkertaisesti enemmän. Lisäksi aurinko lämmittää vain hiekan ohutta pintakerrosta, kun taas vedessä lämpeneminen ulottuu syvemmälle. Suuren ominaislämpökapasiteettinsa vuoksi järvet tasaavat rannikon lämpötiloja ja vesi on hyvä lämmönsiirtoaine lämmitysputkissa.

<svg data-fig="water-sand" viewBox="0 0 600 384" role="img" aria-label="Kaavakuva: yhtä suuriin massoihin vettä ja hiekkaa siirtyy sama lämpömäärä Q, mitä kuvaavat yhtä pitkät nuolet. Veden lämpömittarin lukema nousee vähän, hiekan noin viisi kertaa enemmän, koska hiekan ominaislämpökapasiteetti 800 J/(kg·K) on noin viidesosa veden arvosta 4190 J/(kg·K). Lämpötilan nousut on piirretty mittakaavassa ja korostettu punaisella. Hiekkaa on astiassa tilavuutena vähemmän, koska se on tiheämpää kuin vesi." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy36-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy36-sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><pattern id="fy36-grain" width="14" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.4" fill="#a97a35"/><circle cx="10" cy="8" r="1.1" fill="#a97a35"/><circle cx="8" cy="2" r="0.8" fill="#8a5f22"/></pattern><linearGradient id="fy36-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <foreignObject x="221" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sama } Q \text{ ja sama } m$</div></foreignObject>
  <line x1="300" y1="56" x2="300" y2="372" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <path d="M115,140 V250 Q115,262 127,262 H258 Q270,262 270,250 V140 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M117,172 Q136,165 155,172 T193,172 T231,172 T268,172 V250 Q268,260 258,260 H127 Q117,260 117,250 Z" fill="url(#fy36-water)" stroke-linejoin="round"/>
  <path d="M120,172 Q136,166 155,172 T193,172 T231,172 T265,172" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-opacity="0.8"/>
  <path d="M115,140 V250 Q115,262 127,262 H258 Q270,262 270,250 V140" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M184,56 H200 V112 H212 L192,140 L172,112 H184 Z" fill="url(#fy36-heat)" stroke-linejoin="round"/>
  <foreignObject x="216" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <rect x="85" y="64" width="14" height="206" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="99" y1="86" x2="105" y2="86" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="101" x2="105" y2="101" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="116" x2="105" y2="116" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="131" x2="105" y2="131" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="146" x2="105" y2="146" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="161" x2="105" y2="161" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="176" x2="105" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="191" x2="105" y2="191" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="206" x2="105" y2="206" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="221" x2="105" y2="221" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="236" x2="105" y2="236" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="251" x2="105" y2="251" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="89" y="236" width="6" height="36" fill="#f2a69c"/>
  <circle cx="92" cy="276" r="13" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <rect x="89" y="216" width="6" height="20" fill="#c92a2a"/>
  <line x1="77" y1="236" x2="107" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="4 3"/>
  <path d="M69,216 H63 V236 H69" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="24" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\Delta T$</div></foreignObject>
  <foreignObject x="163" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
  <foreignObject x="107" y="317" width="170" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$c = 4190\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}$</div></foreignObject>
  <path d="M435,140 V250 Q435,262 447,262 H578 Q590,262 590,250 V140 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M437,218 L455,213 L473,217 L492,212 L511,216 L531,211 L551,215 L588,212 V250 Q588,260 578,260 H447 Q437,260 437,250 Z" fill="url(#fy36-sand)" stroke-linejoin="round"/>
  <path d="M437,218 L455,213 L473,217 L492,212 L511,216 L531,211 L551,215 L588,212 V250 Q588,260 578,260 H447 Q437,260 437,250 Z" fill="url(#fy36-grain)" stroke-linejoin="round" fill-opacity="0.6"/>
  <path d="M435,140 V250 Q435,262 447,262 H578 Q590,262 590,250 V140" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M504,56 H520 V112 H532 L512,140 L492,112 H504 Z" fill="url(#fy36-heat)" stroke-linejoin="round"/>
  <foreignObject x="536" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <rect x="405" y="64" width="14" height="206" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="419" y1="86" x2="425" y2="86" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="101" x2="425" y2="101" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="116" x2="425" y2="116" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="131" x2="425" y2="131" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="146" x2="425" y2="146" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="161" x2="425" y2="161" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="176" x2="425" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="191" x2="425" y2="191" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="206" x2="425" y2="206" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="221" x2="425" y2="221" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="236" x2="425" y2="236" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="419" y1="251" x2="425" y2="251" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="409" y="236" width="6" height="36" fill="#f2a69c"/>
  <circle cx="412" cy="276" r="13" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <rect x="409" y="131" width="6" height="105" fill="#c92a2a"/>
  <line x1="397" y1="236" x2="427" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="4 3"/>
  <path d="M389,131 H383 V236 H389" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="307" y="168.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\approx 5\,\Delta T$</div></foreignObject>
  <foreignObject x="470.5" y="279.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hiekka}$</div></foreignObject>
  <foreignObject x="427" y="317" width="170" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$c = 800\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}$</div></foreignObject>
</svg>

Kun kuuma ja kylmä kappale laitetaan yhteen eristettyyn astiaan, lämpöä siirtyy kuumemmasta kylmempään, kunnes molemmilla on sama lämpötila. Tätä tilaa sanotaan lämpötasapainoksi. Energia säilyy: kuuman kappaleen luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama. Eristettyä astiaa, jossa tämä mitataan, sanotaan kalorimetriksi, ja mittausta kalorimetriseksi mittaukseksi. Sillä voidaan määrittää tuntemattoman aineen ominaislämpökapasiteetti, kun veden ominaislämpökapasiteetti tunnetaan.

<svg data-fig="calorimeter" viewBox="0 0 600 432" role="img" aria-label="Kalorimetri ennen ja jälkeen lämpötasapainon, periaatekuva, ei mittakaavassa. Ennen: eristetyssä astiassa on 0,300 kg vettä 20,0 °C:ssa ja sen yläpuolella langasta roikkuu 0,200 kg:n metallikappale 100,0 °C:ssa. Jälkeen: kappale on vedessä, ja sekä vesi että kappale ovat lämpötilassa 24,5 °C. Metallin luovuttama lämpömäärä on yhtä suuri kuin veden vastaanottama." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy36-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy36-sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><pattern id="fy36-grain" width="14" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.4" fill="#a97a35"/><circle cx="10" cy="8" r="1.1" fill="#a97a35"/><circle cx="8" cy="2" r="0.8" fill="#8a5f22"/></pattern><linearGradient id="fy36-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><pattern id="fy36-insul" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" stroke="#6b7480" stroke-width="2"/></pattern></defs>
  <foreignObject x="115" y="7.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="402.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jälkeen}$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="316" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <path d="M58,168 V300 Q58,312 70,312 H230 Q242,312 242,300 V168 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M72,204 Q98,198 126,204 T174,204 T228,204 V298 H72 Z" fill="url(#fy36-water)" stroke-linejoin="round"/>
  <path d="M74,204 Q98,198 126,204 T174,204 T226,204" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-opacity="0.8"/>
  <path d="M58,168 V300 Q58,312 70,312 H230 Q242,312 242,300 V168 H228 V298 H72 V168 Z" fill="url(#fy36-insul)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M72,168 V298 H228 V168" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="105" y1="48" x2="105" y2="84" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="105" cy="48" r="3" fill="#1f2933"/>
  <rect x="83" y="84" width="44" height="46" rx="5" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="137" y="77.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$T_\text{m} = 100{,}0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="137" y="107.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m_\text{m} = 0{,}200\,\text{kg}$</div></foreignObject>
  <foreignObject x="50" y="317.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$T_\text{v} = 20{,}0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="50" y="351.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_\text{v} = 0{,}300\,\text{kg}$</div></foreignObject>
  <path d="M358,168 V300 Q358,312 370,312 H530 Q542,312 542,300 V168 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M372,204 Q398,198 426,204 T474,204 T528,204 V298 H372 Z" fill="url(#fy36-water)" stroke-linejoin="round"/>
  <path d="M374,204 Q398,198 426,204 T474,204 T526,204" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-opacity="0.8"/>
  <path d="M358,168 V300 Q358,312 370,312 H530 Q542,312 542,300 V168 H528 V298 H372 V168 Z" fill="url(#fy36-insul)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M372,168 V298 H528 V168" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="388" y="246" width="44" height="46" rx="5" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M438,276 L470,276 L470,284 L494,269 L470,254 L470,262 L438,262 Z" fill="url(#fy36-heat)" stroke-linejoin="round"/>
  <foreignObject x="456" y="221.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$Q$</span></div></foreignObject>
  <foreignObject x="350" y="317.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T = 24{,}5\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="340" y="351.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sama } T \text{ kaikkialla}$</div></foreignObject>
  <line x1="12" y1="394" x2="588" y2="394" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="130" y="399.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q_\text{luovutettu} = Q_\text{vastaanotettu}$</div></foreignObject>
</svg>

## Kaava: Lämpömäärä ja lämpötasapaino
Lämpömäärä, joka tarvitaan massan $m$ lämmittämiseen tai joka vapautuu sen jäähtyessä, on
```latex
\begin{aligned}
Q &= c m \Delta T \\
\Delta T &= T_\text{loppu} - T_\text{alku}
\end{aligned}
```
missä $Q$ on lämpömäärä (J), $c$ aineen ominaislämpökapasiteetti (J/(kg·K)), $m$ massa (kg) ja $\Delta T$ lämpötilan muutos (K) eli loppulämpötila $T_\text{loppu}$ miinus alkulämpötila $T_\text{alku}$. Lämpötilan muutos on sama kelvineinä ja celsiusasteina, joten $\Delta T$ voidaan laskea suoraan celsiuslämpötiloista. Lämmetessä $\Delta T$ ja $Q$ ovat positiivisia, jäähtyessä negatiivisia.

Koko kappaleen lämpökapasiteetti
```latex
C = c m
```
kertoo, kuinka monta joulea kappaleen lämpötilan nostaminen yhdellä kelvinillä vaatii. $C$ on lämpökapasiteetti (J/K), $c$ ominaislämpökapasiteetti ja $m$ massa. Kappale, jonka lämpökapasiteetti on suuri, lämpenee ja jäähtyy hitaasti.

Eristetyssä astiassa kuuman kappaleen $1$ luovuttama lämpömäärä on yhtä suuri kuin kylmän kappaleen $2$ vastaanottama:
```latex
c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)
```
missä $T_1$ ja $T_2$ ovat kappaleiden alkulämpötilat ja $T$ yhteinen loppulämpötila eli tasapainolämpötila. Yhtälön molemmat puolet ovat positiivisia lämpömääriä: kuumalle kappaleelle lasketaan alkulämpötila miinus loppulämpötila, kylmälle loppulämpötila miinus alkulämpötila. Yhtälöstä voidaan ratkaista mikä tahansa suure, kun muut tunnetaan: loppulämpötila, massa tai tuntematon ominaislämpökapasiteetti.

Tasapainolämpötila $T$ esiintyy yhtälössä kahdessa termissä. Se ratkaistaan kertomalla sulut auki, keräämällä $T$:tä sisältävät termit samalle puolelle ja ottamalla $T$ yhteiseksi tekijäksi:
```latex
\begin{aligned}
&c_1 m_1 T_1 - c_1 m_1 T \\
&\quad = c_2 m_2 T - c_2 m_2 T_2 \\[6pt]
&c_1 m_1 T_1 + c_2 m_2 T_2 \\
&\quad = c_1 m_1 T + c_2 m_2 T \\
&\quad = (c_1 m_1 + c_2 m_2)\,T
\end{aligned}
```
Kun yhtälö jaetaan puolittain summalla $c_1 m_1 + c_2 m_2$, saadaan
```latex
T = \frac{c_1 m_1 T_1 + c_2 m_2 T_2}{c_1 m_1 + c_2 m_2}
```
Tasapainolämpötila on siis alkulämpötilojen painotettu keskiarvo, jossa painoina ovat kappaleiden lämpökapasiteetit $c_1 m_1$ ja $c_2 m_2$. Tavallinen keskiarvo saadaan vain, kun lämpökapasiteetit ovat yhtä suuret.

| Aine | $c$ (J/(kg·K)) |
| --- | --- |
| vesi | 4190 |
| jää | 2100 |
| alumiini | 900 |
| hiekka | 800 |
| rauta | 450 |
| kupari | 385 |

<svg data-fig="c-bars" viewBox="0 0 600 350" role="img" aria-label="Vaakapylväskaavio ominaislämpökapasiteeteista yksikössä J/(kg·K): vesi 4190, jää 2100, alumiini 900, hiekka 800, rauta 450 ja kupari 385. Pylväiden pituudet ovat mittakaavassa: veden pylväs on noin viisi kertaa hiekan pylvään pituinen." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy36-sandbar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#e9c98a"/></linearGradient></defs>
  <foreignObject x="130" y="9.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$c\ \left(\text{J/(kg}\cdot\text{K)}\right)$</div></foreignObject>
  <line x1="223.5" y1="50" x2="223.5" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="316.5" y1="50" x2="316.5" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="50" x2="410" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="503.5" y1="50" x2="503.5" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="130" y="52" width="391" height="28" rx="3" fill="#2f74b5"/>
  <foreignObject x="62" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
  <foreignObject x="529" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4190$</div></foreignObject>
  <rect x="130" y="94" width="196" height="28" rx="3" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="1.5"/>
  <foreignObject x="75" y="93.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{jää}$</div></foreignObject>
  <foreignObject x="334" y="93.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2100$</div></foreignObject>
  <rect x="130" y="136" width="84" height="28" rx="3" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="12" y="135.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{alumiini}$</div></foreignObject>
  <foreignObject x="222" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$900$</div></foreignObject>
  <rect x="130" y="178" width="74.5" height="28" rx="3" fill="url(#fy36-sandbar)" stroke="#a97a35" stroke-width="1.5"/>
  <foreignObject x="37" y="177.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{hiekka}$</div></foreignObject>
  <foreignObject x="212.5" y="177.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800$</div></foreignObject>
  <rect x="130" y="220" width="42" height="28" rx="3" fill="#6c757d"/>
  <foreignObject x="50" y="219.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{rauta}$</div></foreignObject>
  <foreignObject x="180" y="219.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$450$</div></foreignObject>
  <rect x="130" y="262" width="36" height="28" rx="3" fill="#b8622d"/>
  <foreignObject x="37" y="261.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kupari}$</div></foreignObject>
  <foreignObject x="174" y="261.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$385$</div></foreignObject>
  <line x1="130" y1="304" x2="517" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M529,304 L516,310 L516,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="130" y1="46" x2="130" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="120" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <line x1="223.5" y1="304" x2="223.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="194.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1000$</div></foreignObject>
  <line x1="316.5" y1="304" x2="316.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="287.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2000$</div></foreignObject>
  <line x1="410" y1="304" x2="410" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="381" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$3000$</div></foreignObject>
  <line x1="503.5" y1="304" x2="503.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="474.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$4000$</div></foreignObject>
</svg>

## Esimerkki
Kalorimetrissä on 0,300 kg vettä, jonka lämpötila on 20,0 °C. Siihen upotetaan 0,200 kg:n metallikappale, joka on kuumennettu kiehuvassa vedessä 100,0 °C:n lämpötilaan. Sekoituksen jälkeen lämpötila asettuu arvoon 24,5 °C. Mikä on metallin ominaislämpökapasiteetti? Kalorimetrin oma lämpökapasiteetti ja lämpöhäviöt ympäristöön jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** Vesi: $c_\text{v} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, $m_\text{v} = 0{,}300\,\text{kg}$, $T_\text{v} = 20{,}0\,{}^\circ\text{C}$. Metalli: $m_\text{m} = 0{,}200\,\text{kg}$, $T_\text{m} = 100{,}0\,{}^\circ\text{C}$. Tasapainolämpötila $T = 24{,}5\,{}^\circ\text{C}$. Kysytään metallin ominaislämpökapasiteettia $c_\text{m}$. Metalli jäähtyy 75,5 K ja vesi lämpenee 4,5 K.

<!-- vaihe -->

**Kaava ratkaistuna.** Metallin luovuttama lämpömäärä on yhtä suuri kuin veden vastaanottama. Ratkaistaan yhtälöstä $c_\text{m}$:
```latex
\begin{aligned}
&c_\text{m} m_\text{m} (T_\text{m} - T) \\
&\quad = c_\text{v} m_\text{v} (T - T_\text{v}) \\[6pt]
&c_\text{m} = \frac{c_\text{v} m_\text{v} (T - T_\text{v})}{m_\text{m} (T_\text{m} - T)}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin osoittaja eli veden vastaanottama lämpömäärä $Q_\text{v}$ ja jaetaan se sitten:
```latex
\begin{aligned}
&Q_\text{v} = c_\text{v} m_\text{v} (T - T_\text{v}) \\
&= 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}300\,\text{kg} \cdot 4{,}5\,\text{K} \\
&= 5656{,}5\,\text{J} \\[6pt]
&c_\text{m} = \frac{Q_\text{v}}{m_\text{m} (T_\text{m} - T)} \\
&= \frac{5656{,}5\,\text{J}}{0{,}200\,\text{kg} \cdot 75{,}5\,\text{K}} \\
&= 374{,}6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \\
&\approx 3{,}7 \cdot 10^2\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Metallin ominaislämpökapasiteetti on noin $3{,}7 \cdot 10^2\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska veden lämpötilan muutos 4,5 K tunnetaan vain kahden numeron tarkkuudella: jos loppulukema olisi 0,1 K suurempi eli 24,6 °C, tulos olisi 383 J/(kg·K).

<!-- vaihe -->

**Järkevyys.** Arvo on lähellä kuparin ominaislämpökapasiteettia 385 J/(kg·K), joten kappale on luultavasti kuparia. Häviöttömässä kalorimetrissä 0,200 kg:n kuparikappale nostaisi veden 24,6 °C:seen (kokeile simulaatiossa); mitattu 0,1 K pienempi lukema selittyy lukematarkkuudella tai sillä, että todellisuudessa osa lämmöstä siirtyi myös kalorimetrin astiaan ja ilmaan. Vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti on $0{,}300\,\text{kg} \cdot 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} = 1257\,\tfrac{\text{J}}{\text{K}}$, mikä on paljon enemmän kuin kappaleen lämpökapasiteetti $0{,}200\,\text{kg} \cdot 374{,}6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \approx 75\,\tfrac{\text{J}}{\text{K}}$.

## Yleinen virhekäsitys
Moni ajattelee, että lämpömäärä ja lämpötila ovat sama asia, tai että samaan lämpötilaan lämmitetyt kappaleet ovat saaneet saman määrän energiaa. Kilon veden ja kilon raudan lämmittäminen 20 °C:sta 60 °C:seen vaatii vedelle lähes kymmenkertaisen energian. Toinen virhe on laskea tasapainolämpötila keskiarvona. Kun 1,0 kg 80-asteista vettä kaadetaan 3,0 kg:aan 20-asteista vettä, veden ominaislämpökapasiteetti $c$ on yhtälön molemmilla puolilla ja supistuu pois:
```latex
\begin{aligned}
&1{,}0\,\text{kg} \cdot (80\,{}^\circ\text{C} - T) \\
&\quad = 3{,}0\,\text{kg} \cdot (T - 20\,{}^\circ\text{C}) \\[6pt]
&80\,{}^\circ\text{C} - T = 3T - 60\,{}^\circ\text{C} \\
&140\,{}^\circ\text{C} = 4T \\
&T = 35\,{}^\circ\text{C}
\end{aligned}
```
Kuuma vesi on vasemmalla puolella kuten yleisessä yhtälössä. Kolmannella rivillä yhtälö on jaettu puolittain kilogrammalla ja sulut on kerrottu auki. Lopputulos ei siis ole 50 °C vaan 35 °C, koska kylmää vettä on kolme kertaa enemmän kuin kuumaa. Sama tulos saadaan painotetulla keskiarvolla: $T = \tfrac{3{,}0\,\text{kg} \cdot 20\,{}^\circ\text{C} + 1{,}0\,\text{kg} \cdot 80\,{}^\circ\text{C}}{4{,}0\,\text{kg}} = 35\,{}^\circ\text{C}$.

Kolmas virhe on muuntaa $\Delta T$ kelvineiksi lisäämällä 273: lämpötilan muutos on sama kummallakin asteikolla.

## Tiivistelmä
- Lämpömäärä on verrannollinen massaan ja lämpötilan muutokseen: $Q = c m \Delta T$. Ominaislämpökapasiteetti $c$ riippuu aineesta, ja vedellä se on suuri, 4190 J/(kg·K).
- Lämpökapasiteetti $C = cm$ kertoo, kuinka monta joulea koko kappaleen lämmittäminen yhdellä kelvinillä vaatii.
- Eristetyssä astiassa kuuman luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama: $c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)$. Tasapainolämpötila $T$ ratkaistaan keräämällä $T$:n termit samalle puolelle; se on lämpökapasiteeteilla painotettu keskiarvo eikä yleensä alkulämpötilojen tavallinen keskiarvo.
- Kalorimetrisellä mittauksella määritetään tuntemattoman aineen ominaislämpökapasiteetti veden avulla.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: saunan kiuas. Kuumille kiville heitetään kauhalla vettä, ja kivistä nousee löylyhöyryä. Taustalla on puiset lauteet." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy36s-fire" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="#e9c98a"/>
  <line x1="0" y1="0" x2="600" y2="0" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="30" x2="600" y2="30" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="60" x2="600" y2="60" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="90" x2="600" y2="90" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="120" x2="600" y2="120" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="150" x2="600" y2="150" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="180" x2="600" y2="180" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="210" x2="600" y2="210" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="240" x2="600" y2="240" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="270" x2="600" y2="270" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="300" x2="600" y2="300" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="330" x2="600" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <rect x="330" y="150" width="270" height="22" fill="#d9b26a" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="330" y="172" width="270" height="188" fill="#f1dfb5"/>
  <line x1="330" y1="172" x2="330" y2="360" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="384" y1="172" x2="384" y2="360" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="438" y1="172" x2="438" y2="360" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="492" y1="172" x2="492" y2="360" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="172" x2="546" y2="360" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <rect x="330" y="250" width="270" height="18" fill="#d9b26a" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="100" y="200" width="170" height="150" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="130" y="270" width="110" height="50" rx="4" fill="#1f2933"/>
  <rect x="140" y="280" width="90" height="30" rx="3" fill="url(#fy36s-fire)"/>
  <circle cx="120" cy="194" r="18" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="152" cy="186" r="20" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="186" cy="192" r="19" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="220" cy="186" r="21" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="250" cy="196" r="16" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="136" cy="168" r="17" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="172" cy="164" r="19" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="206" cy="166" r="18" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="238" cy="172" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="188" cy="144" r="16" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <path d="M330,70 L250,120" fill="none" stroke="#d9b26a" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M226,112 q24,30 48,6 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="232" cy="136" r="3" fill="#2f74b5"/>
  <circle cx="238" cy="142" r="3" fill="#2f74b5"/>
  <circle cx="244" cy="148" r="3" fill="#2f74b5"/>
  <circle cx="250" cy="154" r="3" fill="#2f74b5"/>
  <circle cx="256" cy="160" r="3" fill="#2f74b5"/>
  <path d="M150,140 c14,-24 -14,-40 0,-64 s-14,-40 0,-60" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M150,140 c14,-24 -14,-40 0,-64 s-14,-40 0,-60" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M196,140 c14,-24 -14,-40 0,-64 s-14,-40 0,-60" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M196,140 c14,-24 -14,-40 0,-64 s-14,-40 0,-60" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M236,140 c14,-24 -14,-40 0,-64 s-14,-40 0,-60" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M236,140 c14,-24 -14,-40 0,-64 s-14,-40 0,-60" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
</svg>
