# Mekaanisen energian säilyminen ja energiaperiaate

> **Miksi** vuoristoradan ensimmäinen mäki on aina radan korkein, vaikka junaa ei sen jälkeen enää vedetä ylös?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: huvipuiston vuoristorata kesäpäivänä. Vasemmalla nousee radan ensimmäinen ja korkein mäki, jonka huipulle punainen juna on juuri noussut. Sen jälkeen rata laskee syvään laaksoon ja nousee toiselle mäelle, joka on selvästi matalampi, ja sen jälkeen vielä matalammalle kolmannelle mäelle. Radan alla on valkoiset tukipylväät, ja taustalla on kuusimetsää." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy48h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy48h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy48h-grass" gradientUnits="userSpaceOnUse" x1="0" y1="500" x2="0" y2="900"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="540" fill="url(#fy48h-sky)"/>
  <circle cx="1060" cy="100" r="83" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M1120.5,123.5 L1147.5,123.5 L1124,110 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1100.5,150.5 L1124,164 L1110.5,140.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1070,164 L1083.5,187.5 L1083.5,160.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1036.5,160.5 L1036.5,187.5 L1050,164 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1009.5,140.5 L996,164 L1019.5,150.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M996,110 L972.5,123.5 L999.5,123.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M999.5,76.5 L972.5,76.5 L996,90 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1019.5,49.5 L996,36 L1009.5,59.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1050,36 L1036.5,12.5 L1036.5,39.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1083.5,39.5 L1083.5,12.5 L1070,36 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1110.5,59.5 L1124,36 L1100.5,49.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1124,90 L1147.5,76.5 L1120.5,76.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="1060" cy="100" r="52" fill="url(#fy48h-sun)"/>
  <path d="M140,110 Q138,76 178,80 Q194,44 234,56 Q270,36 290,74 Q326,78 322,110 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M692.5,85 Q691,59.5 721,62.5 Q733,35.5 763,44.5 Q790,29.5 805,58 Q832,61 829,85 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,470 L13,434 L26,470 L40,429 L54.5,470 L67.5,433 L80.5,470 L99.5,413 L118,470 L134,422.5 L150,470 L169,413 L187.5,470 L204,420.5 L221,470 L232.5,439 L244,470 L262,415 L280,470 L291,441 L302.5,470 L315.5,433.5 L328.5,470 L345.5,418.5 L363,470 L379,422 L395,470 L407,438.5 L418.5,470 L429.5,441 L440.5,470 L453,436 L465.5,470 L480.5,427 L495,470 L509.5,428.5 L524,470 L536,438 L548,470 L559,442 L569.5,470 L581,438.5 L593,470 L609,422.5 L625,470 L642.5,417 L660.5,470 L672.5,436.5 L685,470 L697,437 L709,470 L720.5,440 L731.5,470 L751,410 L770.5,470 L781.5,440.5 L793,470 L810.5,416.5 L828.5,470 L842.5,430 L856.5,470 L873.5,418 L891,470 L909,415.5 L927,470 L942,426.5 L957,470 L969,438 L980.5,470 L994.5,430 L1008.5,470 L1025.5,420 L1042,470 L1061,412.5 L1080,470 L1091.5,438.5 L1103.5,470 L1120,421 L1136.5,470 L1150,431 L1164,470 L1178,431 L1191.5,470 L1208,421 L1224.5,470 V500 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <rect x="0" y="500" width="1200" height="100" fill="url(#fy48h-grass)"/>
  <line x1="120" y1="479.5" x2="120" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="120" y1="479.5" x2="120" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="446" x2="160" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="160" y1="446" x2="160" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="200" y1="402.5" x2="200" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="200" y1="402.5" x2="200" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="452" x2="200" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="508" x2="200" y2="452" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="352.5" x2="240" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="240" y1="352.5" x2="240" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="200" y1="408.5" x2="240" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="200" y1="508" x2="240" y2="408.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="280" y1="299.5" x2="280" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="280" y1="299.5" x2="280" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="358.5" x2="280" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="508" x2="280" y2="358.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320" y1="247.5" x2="320" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="320" y1="247.5" x2="320" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="280" y1="305.5" x2="320" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="280" y1="508" x2="320" y2="305.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="360" y1="200.5" x2="360" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="360" y1="200.5" x2="360" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320" y1="253.5" x2="360" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320" y1="508" x2="360" y2="253.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="161.5" x2="400" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="400" y1="161.5" x2="400" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="360" y1="206.5" x2="400" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="360" y1="508" x2="400" y2="206.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="440" y1="134" x2="440" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="440" y1="134" x2="440" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="167.5" x2="440" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="508" x2="440" y2="167.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="480" y1="120" x2="480" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="480" y1="120" x2="480" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="440" y1="140" x2="480" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="440" y1="508" x2="480" y2="140" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="520" y1="128" x2="520" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="520" y1="128" x2="520" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="480" y1="134" x2="520" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="480" y1="508" x2="520" y2="134" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="560" y1="199.5" x2="560" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="560" y1="199.5" x2="560" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="520" y1="205.5" x2="560" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="520" y1="508" x2="560" y2="205.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="313" x2="600" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="600" y1="313" x2="600" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="560" y1="319" x2="600" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="560" y1="508" x2="600" y2="319" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="640" y1="420" x2="640" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="640" y1="420" x2="640" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="426" x2="640" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="508" x2="640" y2="426" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="680" y1="475.5" x2="680" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="680" y1="475.5" x2="680" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="720" y1="458.5" x2="720" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="720" y1="458.5" x2="720" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="760" y1="385.5" x2="760" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="760" y1="385.5" x2="760" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="720" y1="464.5" x2="760" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="720" y1="508" x2="760" y2="464.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="299" x2="800" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="800" y1="299" x2="800" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="760" y1="391.5" x2="800" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="760" y1="508" x2="800" y2="391.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="840" y1="250" x2="840" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="840" y1="250" x2="840" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="305" x2="840" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="508" x2="840" y2="305" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="880" y1="277.5" x2="880" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="880" y1="277.5" x2="880" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="840" y1="283.5" x2="880" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="840" y1="508" x2="880" y2="283.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="920" y1="374" x2="920" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="920" y1="374" x2="920" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="880" y1="380" x2="920" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="880" y1="508" x2="920" y2="380" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="444.5" x2="960" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="960" y1="444.5" x2="960" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="920" y1="450.5" x2="960" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="920" y1="508" x2="960" y2="450.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1000" y1="432" x2="1000" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="1000" y1="432" x2="1000" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="450.5" x2="1000" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="508" x2="1000" y2="450.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1040" y1="379" x2="1040" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="1040" y1="379" x2="1040" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1000" y1="438" x2="1040" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1000" y1="508" x2="1040" y2="438" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1080" y1="340" x2="1080" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="1080" y1="340" x2="1080" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1040" y1="385" x2="1080" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1040" y1="508" x2="1080" y2="385" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1120" y1="353.5" x2="1120" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="1120" y1="353.5" x2="1120" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1080" y1="359.5" x2="1120" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1080" y1="508" x2="1120" y2="359.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1160" y1="401.5" x2="1160" y2="508" stroke="#ffffff" stroke-width="6" stroke-linecap="butt"/>
  <line x1="1160" y1="401.5" x2="1160" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1120" y1="407.5" x2="1160" y2="508" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1120" y1="508" x2="1160" y2="407.5" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <path d="M40,500 L44,500 L48,499.5 L52,499.5 L56,499 L60,498 L64,497.5 L68,496.5 L72,495.5 L76,494 L80,493 L84,491.5 L88,489.5 L92,488 L96,486 L100,484 L104,481.5 L108,479.5 L112,477 L116,474.5 L120,471.5 L124,469 L128,466 L132,463 L136,459.5 L140,456.5 L144,453 L148,449.5 L152,445.5 L156,442 L160,438 L164,434 L168,430 L172,426 L176,422 L180,417.5 L184,413 L188,408.5 L192,404 L196,399.5 L200,394.5 L204,390 L208,385 L212,380 L216,375.5 L220,370.5 L224,365.5 L228,360 L232,355 L236,350 L240,344.5 L244,339.5 L248,334 L252,329 L256,323.5 L260,318.5 L264,313 L268,307.5 L272,302.5 L276,297 L280,291.5 L284,286.5 L288,281 L292,276 L296,270.5 L300,265.5 L304,260 L308,255 L312,250 L316,244.5 L320,239.5 L324,234.5 L328,230 L332,225 L336,220 L340,215.5 L344,210.5 L348,206 L352,201.5 L356,197 L360,192.5 L364,188 L368,184 L372,180 L376,176 L380,172 L384,168 L388,164.5 L392,160.5 L396,157 L400,153.5 L404,150.5 L408,147 L412,144 L416,141 L420,138.5 L424,135.5 L428,133 L432,130.5 L436,128.5 L440,126 L444,124 L448,122 L452,120.5 L456,118.5 L460,117 L464,116 L468,114.5 L472,113.5 L476,112.5 L480,112 L484,111 L488,110.5 L492,110.5 L496,110 L500,110 L504,110.5 L508,111.5 L512,113.5 L516,116.5 L520,120 L524,124 L528,129 L532,134.5 L536,141 L540,148 L544,155.5 L548,164 L552,172.5 L556,182 L560,191.5 L564,201.5 L568,212.5 L572,223 L576,234.5 L580,246 L584,257.5 L588,269 L592,281 L596,293 L600,305 L604,316.5 L608,328.5 L612,340 L616,351.5 L620,362.5 L624,373 L628,383.5 L632,393.5 L636,403 L640,412 L644,420.5 L648,428.5 L652,435.5 L656,442.5 L660,448.5 L664,453.5 L668,458 L672,462 L676,465 L680,467.5 L684,469 L688,470 L692,470 L696,469 L700,468 L704,465.5 L708,463 L712,459.5 L716,455.5 L720,450.5 L724,445.5 L728,439.5 L732,433 L736,426 L740,419 L744,411 L748,403 L752,395 L756,386 L760,377.5 L764,368.5 L768,359.5 L772,350.5 L776,341.5 L780,332.5 L784,324 L788,315 L792,307 L796,299 L800,291 L804,284 L808,277 L812,270.5 L816,264.5 L820,259.5 L824,254.5 L828,250.5 L832,247 L836,244.5 L840,242 L844,241 L848,240 L852,240 L856,241 L860,243.5 L864,246.5 L868,251 L872,256 L876,262.5 L880,269.5 L884,277 L888,285.5 L892,294.5 L896,304 L900,314 L904,324.5 L908,335 L912,345 L916,355.5 L920,366 L924,376 L928,385.5 L932,394.5 L936,403 L940,410.5 L944,417.5 L948,424 L952,429 L956,433.5 L960,436.5 L964,439 L968,440 L972,440 L976,439.5 L980,438 L984,436.5 L988,434 L992,431 L996,427.5 L1000,424 L1004,419.5 L1008,415 L1012,410 L1016,404.5 L1020,399 L1024,393.5 L1028,388 L1032,382 L1036,376.5 L1040,371 L1044,365.5 L1048,360 L1052,355 L1056,350.5 L1060,346 L1064,342.5 L1068,339 L1072,336 L1076,333.5 L1080,332 L1084,330.5 L1088,330 L1092,330 L1096,330.5 L1100,332 L1104,333.5 L1108,336 L1112,338.5 L1116,342 L1120,345.5 L1124,349.5 L1128,354 L1132,358.5 L1136,363.5 L1140,368.5 L1144,373.5 L1148,379 L1152,384 L1156,389 L1160,393.5 L1164,398 L1168,402.5 L1172,406.5 L1176,410 L1180,413 L1184,415.5 L1188,417.5 L1192,419 L1196,419.5 L1200,420" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round"/>
  <path d="M40,498 L44,498 L48,497.5 L52,497.5 L56,497 L60,496 L64,495.5 L68,494.5 L72,493.5 L76,492 L80,491 L84,489.5 L88,487.5 L92,486 L96,484 L100,482 L104,479.5 L108,477.5 L112,475 L116,472.5 L120,469.5 L124,467 L128,464 L132,461 L136,457.5 L140,454.5 L144,451 L148,447.5 L152,443.5 L156,440 L160,436 L164,432 L168,428 L172,424 L176,420 L180,415.5 L184,411 L188,406.5 L192,402 L196,397.5 L200,392.5 L204,388 L208,383 L212,378 L216,373.5 L220,368.5 L224,363.5 L228,358 L232,353 L236,348 L240,342.5 L244,337.5 L248,332 L252,327 L256,321.5 L260,316.5 L264,311 L268,305.5 L272,300.5 L276,295 L280,289.5 L284,284.5 L288,279 L292,274 L296,268.5 L300,263.5 L304,258 L308,253 L312,248 L316,242.5 L320,237.5 L324,232.5 L328,228 L332,223 L336,218 L340,213.5 L344,208.5 L348,204 L352,199.5 L356,195 L360,190.5 L364,186 L368,182 L372,178 L376,174 L380,170 L384,166 L388,162.5 L392,158.5 L396,155 L400,151.5 L404,148.5 L408,145 L412,142 L416,139 L420,136.5 L424,133.5 L428,131 L432,128.5 L436,126.5 L440,124 L444,122 L448,120 L452,118.5 L456,116.5 L460,115 L464,114 L468,112.5 L472,111.5 L476,110.5 L480,110 L484,109 L488,108.5 L492,108.5 L496,108 L500,108 L504,108.5 L508,109.5 L512,111.5 L516,114.5 L520,118 L524,122 L528,127 L532,132.5 L536,139 L540,146 L544,153.5 L548,162 L552,170.5 L556,180 L560,189.5 L564,199.5 L568,210.5 L572,221 L576,232.5 L580,244 L584,255.5 L588,267 L592,279 L596,291 L600,303 L604,314.5 L608,326.5 L612,338 L616,349.5 L620,360.5 L624,371 L628,381.5 L632,391.5 L636,401 L640,410 L644,418.5 L648,426.5 L652,433.5 L656,440.5 L660,446.5 L664,451.5 L668,456 L672,460 L676,463 L680,465.5 L684,467 L688,468 L692,468 L696,467 L700,466 L704,463.5 L708,461 L712,457.5 L716,453.5 L720,448.5 L724,443.5 L728,437.5 L732,431 L736,424 L740,417 L744,409 L748,401 L752,393 L756,384 L760,375.5 L764,366.5 L768,357.5 L772,348.5 L776,339.5 L780,330.5 L784,322 L788,313 L792,305 L796,297 L800,289 L804,282 L808,275 L812,268.5 L816,262.5 L820,257.5 L824,252.5 L828,248.5 L832,245 L836,242.5 L840,240 L844,239 L848,238 L852,238 L856,239 L860,241.5 L864,244.5 L868,249 L872,254 L876,260.5 L880,267.5 L884,275 L888,283.5 L892,292.5 L896,302 L900,312 L904,322.5 L908,333 L912,343 L916,353.5 L920,364 L924,374 L928,383.5 L932,392.5 L936,401 L940,408.5 L944,415.5 L948,422 L952,427 L956,431.5 L960,434.5 L964,437 L968,438 L972,438 L976,437.5 L980,436 L984,434.5 L988,432 L992,429 L996,425.5 L1000,422 L1004,417.5 L1008,413 L1012,408 L1016,402.5 L1020,397 L1024,391.5 L1028,386 L1032,380 L1036,374.5 L1040,369 L1044,363.5 L1048,358 L1052,353 L1056,348.5 L1060,344 L1064,340.5 L1068,337 L1072,334 L1076,331.5 L1080,330 L1084,328.5 L1088,328 L1092,328 L1096,328.5 L1100,330 L1104,331.5 L1108,334 L1112,336.5 L1116,340 L1120,343.5 L1124,347.5 L1128,352 L1132,356.5 L1136,361.5 L1140,366.5 L1144,371.5 L1148,377 L1152,382 L1156,387 L1160,391.5 L1164,396 L1168,400.5 L1172,404.5 L1176,408 L1180,411 L1184,413.5 L1188,415.5 L1192,417 L1196,417.5 L1200,418" fill="none" stroke="#c92a2a" stroke-width="5" stroke-linejoin="round"/>
  <line x1="40" y1="502" x2="40" y2="509" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="60" y1="500" x2="60" y2="507" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="80" y1="495" x2="80" y2="502" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="100" y1="486" x2="100" y2="493" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="473.5" x2="120" y2="480.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="140" y1="458.5" x2="140" y2="465.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="160" y1="440" x2="160" y2="447" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="180" y1="419.5" x2="180" y2="426.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="200" y1="396.5" x2="200" y2="403.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="220" y1="372.5" x2="220" y2="379.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="240" y1="346.5" x2="240" y2="353.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="260" y1="320.5" x2="260" y2="327.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="280" y1="293.5" x2="280" y2="300.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="300" y1="267.5" x2="300" y2="274.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="320" y1="241.5" x2="320" y2="248.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="340" y1="217.5" x2="340" y2="224.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="360" y1="194.5" x2="360" y2="201.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="380" y1="174" x2="380" y2="181" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="400" y1="155.5" x2="400" y2="162.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="420" y1="140.5" x2="420" y2="147.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="128" x2="440" y2="135" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="460" y1="119" x2="460" y2="126" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="480" y1="114" x2="480" y2="121" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="500" y1="112" x2="500" y2="119" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="520" y1="122" x2="520" y2="129" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="540" y1="150" x2="540" y2="157" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="560" y1="193.5" x2="560" y2="200.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="580" y1="248" x2="580" y2="255" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="600" y1="307" x2="600" y2="314" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="620" y1="364.5" x2="620" y2="371.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="640" y1="414" x2="640" y2="421" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="660" y1="450.5" x2="660" y2="457.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="680" y1="469.5" x2="680" y2="476.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="700" y1="470" x2="700" y2="477" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="720" y1="452.5" x2="720" y2="459.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="740" y1="421" x2="740" y2="428" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="760" y1="379.5" x2="760" y2="386.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="780" y1="334.5" x2="780" y2="341.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="800" y1="293" x2="800" y2="300" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="820" y1="261.5" x2="820" y2="268.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="840" y1="244" x2="840" y2="251" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="860" y1="245.5" x2="860" y2="252.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="880" y1="271.5" x2="880" y2="278.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="900" y1="316" x2="900" y2="323" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="920" y1="368" x2="920" y2="375" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="940" y1="412.5" x2="940" y2="419.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="960" y1="438.5" x2="960" y2="445.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="980" y1="440" x2="980" y2="447" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1000" y1="426" x2="1000" y2="433" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1020" y1="401" x2="1020" y2="408" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1040" y1="373" x2="1040" y2="380" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1060" y1="348" x2="1060" y2="355" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1080" y1="334" x2="1080" y2="341" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1100" y1="334" x2="1100" y2="341" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1120" y1="347.5" x2="1120" y2="354.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1140" y1="370.5" x2="1140" y2="377.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1160" y1="395.5" x2="1160" y2="402.5" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1180" y1="415" x2="1180" y2="422" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1200" y1="422" x2="1200" y2="429" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <rect x="52" y="456" width="90" height="50" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <path d="M44,456 L97,424 L150,456 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="84" y="474" width="26" height="32" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="425.5" cy="122" r="5.76" fill="#1f2933"/>
  <circle cx="449.5" cy="109" r="5.76" fill="#1f2933"/>
  <path d="M415.5,123.5 L456.5,102 L445.5,82 L405,103.5 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="415.5" cy="88.5" r="7.68" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="429.5" cy="81" r="7.68" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="473" cy="101" r="5.76" fill="#1f2933"/>
  <circle cx="500.5" cy="98" r="5.76" fill="#1f2933"/>
  <path d="M463.5,99 L509.5,94 L507,71 L461,76.5 Z" fill="#e8590c" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="476" cy="66" r="7.68" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="492" cy="64.5" r="7.68" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="525.5" cy="110.5" r="5.76" fill="#1f2933"/>
  <circle cx="542" cy="133" r="5.76" fill="#1f2933"/>
  <path d="M523,101.5 L549.5,139 L568.5,125.5 L541.5,88 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="557.5" cy="96.5" r="7.68" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="567" cy="109.5" r="7.68" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="300" cy="520" r="9" fill="#f1dfb5"/>
  <rect x="292" y="530" width="16" height="30" rx="5" fill="#1971c2"/>
  <line x1="296" y1="560" x2="296" y2="578" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="304" y1="560" x2="304" y2="578" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="340" cy="520" r="9" fill="#f1dfb5"/>
  <rect x="332" y="530" width="16" height="30" rx="5" fill="#e8590c"/>
  <line x1="336" y1="560" x2="336" y2="578" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="344" y1="560" x2="344" y2="578" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="378" cy="520" r="9" fill="#f1dfb5"/>
  <rect x="370" y="530" width="16" height="30" rx="5" fill="#2b8a3e"/>
  <line x1="374" y1="560" x2="374" y2="578" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="382" y1="560" x2="382" y2="578" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <rect x="1144" y="542" width="12" height="18" fill="#b8622d"/>
  <path d="M1096,545 L1150,485 L1204,545 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,485 L1204,545 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1108,512 L1150,452 L1192,512 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,452 L1192,512 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1120,479 L1150,410 L1180,479 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,410 L1180,479 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="635.5" y="527" width="9" height="13" fill="#b8622d"/>
  <path d="M600.5,529 L640,485 L679.5,529 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M640,485 L679.5,529 H640 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M609,505 L640,461 L671,505 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M640,461 L671,505 H640 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M618,480.5 L640,430 L662,480.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M640,430 L662,480.5 H640 Z" fill="#1f2933" fill-opacity="0.18"/>
</svg>

## Ydinajatus

### Mekaaninen energia vaihtaa muotoaan
Luvussa *Liike-energia, potentiaalienergia ja mekaaninen energia* opit, että kappaleen mekaaninen energia on sen liike-energian ja potentiaalienergian summa, $E_\text{mek} = E_\text{k} + E_\text{p}$. Kun vuoristoradan vaunu rullaa laaksoon, sen korkeus pienenee ja nopeus kasvaa: potentiaalienergiaa muuttuu liike-energiaksi. Kun vaunu nousee vastakkaista rinnettä, liike-energiaa muuttuu takaisin potentiaalienergiaksi. Jos kitkaa ja ilmanvastusta ei ole, vaunu nousee täsmälleen lähtökorkeudelleen ja pysähtyy siellä hetkeksi. Mekaaninen energia on silloin joka hetki yhtä suuri, vaikka sen muoto vaihtuu. Tätä sanotaan **mekaanisen energian säilymiseksi**.

<svg data-fig="laakso" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: vuoristoradan vaunu kaarevassa laaksossa ilman kitkaa ja ilmanvastusta. Vaunu lähtee levosta vasemmalta korkeudelta h (kohta 1), ohittaa puolen korkeuden (kohta 2) ja laakson pohjan (kohta 3) ja pysähtyy oikealla samalle korkeudelle h (kohta 4). Siniset nuolet ovat vaunun nopeus, pohjalla suurin. Alla kunkin kohdan energiapalkit: vihreä potentiaalienergia ja sininen liike-energia. Kohdassa 1 ja 4 on vain potentiaalienergiaa, kohdassa 3 vain liike-energiaa ja kohdassa 2 puolet kumpaakin. Palkkien summa on joka kohdassa yhtä suuri." style="max-width:100%;font-size:24px">
  <rect x="14" y="236" width="572" height="10" fill="#f1dfb5"/>
  <line x1="227.5" y1="225.5" x2="227.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="372.5" y1="225.5" x2="372.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="203" y1="219.5" x2="203" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="397" y1="219.5" x2="397" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="179.5" y1="209.5" x2="179.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="420.5" y1="209.5" x2="420.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="158" y1="195.5" x2="158" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="442" y1="195.5" x2="442" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="139.5" y1="178" x2="139.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="460.5" y1="178" x2="460.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="124" y1="158" x2="124" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="476" y1="158" x2="476" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="112" y1="135.5" x2="112" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="488" y1="135.5" x2="488" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="104" y1="111.5" x2="104" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="496" y1="111.5" x2="496" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <path d="M103,102 L104,107 L105.5,112 L107,117 L108.5,121.5 L110.5,126.5 L112,131.5 L114.5,136 L116.5,140.5 L119,145 L121.5,149.5 L124.5,154 L127,158 L130,162.5 L133.5,166.5 L136.5,170.5 L140,174 L143.5,178 L147.5,181.5 L151,185 L155,188 L159,191.5 L163.5,194.5 L167.5,197.5 L172,200 L176.5,202.5 L181,205 L185.5,207.5 L190,209.5 L195,211.5 L199.5,213.5 L204.5,215 L209.5,216.5 L214.5,217.5 L219.5,219 L224.5,220 L229.5,220.5 L234.5,221 L239.5,221.5 L245,222 L250,222 L350,222 L355,222 L360.5,221.5 L365.5,221 L370.5,220.5 L375.5,220 L380.5,219 L385.5,217.5 L390.5,216.5 L395.5,215 L400.5,213.5 L405,211.5 L410,209.5 L414.5,207.5 L419,205 L423.5,202.5 L428,200 L432.5,197.5 L436.5,194.5 L441,191.5 L445,188 L449,185 L452.5,181.5 L456.5,178 L460,174 L463.5,170.5 L466.5,166.5 L470,162.5 L473,158 L475.5,154 L478.5,149.5 L481,145 L483.5,140.5 L485.5,136 L488,131.5 L489.5,126.5 L491.5,121.5 L493,117 L494.5,112 L496,107 L497,102" fill="none" stroke="#8a96a3" stroke-width="6" stroke-linejoin="round"/>
  <path d="M103,101 L104,106 L105.5,111 L107,116 L108.5,120.5 L110.5,125.5 L112,130.5 L114.5,135 L116.5,139.5 L119,144 L121.5,148.5 L124.5,153 L127,157 L130,161.5 L133.5,165.5 L136.5,169.5 L140,173 L143.5,177 L147.5,180.5 L151,184 L155,187 L159,190.5 L163.5,193.5 L167.5,196.5 L172,199 L176.5,201.5 L181,204 L185.5,206.5 L190,208.5 L195,210.5 L199.5,212.5 L204.5,214 L209.5,215.5 L214.5,216.5 L219.5,218 L224.5,219 L229.5,219.5 L234.5,220 L239.5,220.5 L245,221 L250,221 L350,221 L355,221 L360.5,220.5 L365.5,220 L370.5,219.5 L375.5,219 L380.5,218 L385.5,216.5 L390.5,215.5 L395.5,214 L400.5,212.5 L405,210.5 L410,208.5 L414.5,206.5 L419,204 L423.5,201.5 L428,199 L432.5,196.5 L436.5,193.5 L441,190.5 L445,187 L449,184 L452.5,180.5 L456.5,177 L460,173 L463.5,169.5 L466.5,165.5 L470,161.5 L473,157 L475.5,153 L478.5,148.5 L481,144 L483.5,139.5 L485.5,135 L488,130.5 L489.5,125.5 L491.5,120.5 L493,116 L494.5,111 L496,106 L497,101" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="78" y1="122" x2="540" y2="122" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="52" y1="222" x2="52" y2="122" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M52,122 l-6,12 h12 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M52,222 l-6,-12 h12 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="18" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$h$</div></foreignObject>
  <line x1="40" y1="222" x2="78" y2="222" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="108.5" cy="112.5" r="3.12" fill="#1f2933"/>
  <circle cx="114.5" cy="129.5" r="3.12" fill="#1f2933"/>
  <path d="M108,106.5 L118,134.5 L129.5,130.5 L119.5,102 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="127.5" cy="110.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="131" cy="120.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="134.5" cy="163.5" r="3.12" fill="#1f2933"/>
  <circle cx="146.5" cy="177" r="3.12" fill="#1f2933"/>
  <path d="M131.5,158 L151.5,180 L161,172 L141,149.5 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="151" cy="154.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="158" cy="162" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="146" y1="138" x2="166" y2="160.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M173.5,168.5 L161.5,163 L169.5,156 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="291" cy="219" r="3.12" fill="#1f2933"/>
  <circle cx="309" cy="219" r="3.12" fill="#1f2933"/>
  <path d="M285,217.5 L315,217.5 L315,205 L285,205 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="295.5" cy="200.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="306" cy="200.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="300" y1="192" x2="347" y2="192" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M358,192 L346,197.5 L346,186.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="485.5" cy="129.5" r="3.12" fill="#1f2933"/>
  <circle cx="491.5" cy="112.5" r="3.12" fill="#1f2933"/>
  <path d="M482,134.5 L492,106.5 L480.5,102 L470.5,130.5 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="469.5" cy="119" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="473" cy="109" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="76.5" y="73.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="94" y="151.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="264" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="505.5" y="73.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="392" y="173.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="70" y1="352" x2="560" y2="352" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="108" y="282" width="20" height="70" fill="#2b8a3e"/>
  <foreignObject x="120" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <rect x="228" y="317" width="20" height="35" fill="#2b8a3e"/>
  <rect x="252" y="317" width="20" height="35" fill="#1971c2"/>
  <foreignObject x="240" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <rect x="372" y="282" width="20" height="70" fill="#1971c2"/>
  <foreignObject x="360" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <rect x="468" y="282" width="20" height="70" fill="#2b8a3e"/>
  <foreignObject x="480" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <rect x="24" y="290" width="16" height="16" fill="#2b8a3e"/>
  <foreignObject x="46" y="283.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$E_\text{p}$</div></foreignObject>
  <rect x="24" y="326" width="16" height="16" fill="#1971c2"/>
  <foreignObject x="46" y="319.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
</svg>

Kaikki vaunuun vaikuttavat voimat eivät muuta sen energiaa. Paino tekee työtä, kun vaunu laskee tai nousee, ja juuri tämä työ muuttaa potentiaalienergiaa liike-energiaksi ja takaisin. Radan tukivoima on kohtisuorassa radan pintaa ja siis myös liikettä vastaan, joten se ei tee työtä. Siksi mekaaninen energia säilyy, kun vain paino tekee työtä, olipa rata kuinka mutkainen tahansa. Vaunun nopeus missä tahansa kohdassa riippuu silloin vain siitä, kuinka paljon alemmas se on lähtökohdasta laskeutunut, eikä radan muodosta tai vaunun massasta.

### Työ siirtää energiaa
Luvussa *Työ ja energia* opit, että voima tekee työtä, kun kappale liikkuu voiman suuntaan. Nyt tarvitaan myös työn etumerkki. Voima tekee positiivista työtä, kun sillä on liikkeen suuntainen komponentti: se lisää kappaleen energiaa. Liikettä vastustava voima, kuten kitka, tekee negatiivista työtä: se vähentää kappaleen energiaa. Liikettä vastaan kohtisuora voima, kuten tukivoima, ei tee työtä lainkaan. Työn yksikkö on sama kuin energian, joule.

<svg data-fig="tyo" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kolmesta tilanteesta, joissa laatikko liikkuu lattialla oikealle; sininen nuoli on laatikon nopeus. Vasemmalla laatikkoa vedetään liikkeen suuntaan voimalla F, joten voima tekee positiivista työtä, W &gt; 0. Keskellä kitkavoima F_μ vaikuttaa lattian pinnasta liikettä vastaan, joten se tekee negatiivista työtä, W &lt; 0. Oikealla lattian tukivoima N on kohtisuorassa liikettä vastaan, joten se ei tee työtä, W = 0." style="max-width:100%;font-size:24px">
  <rect x="14" y="210" width="172" height="10" fill="#f1dfb5"/>
  <line x1="14" y1="210" x2="186" y2="210" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="64" y="154" width="72" height="56" rx="3" fill="#d9b26a" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="64" y1="182" x2="136" y2="182" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="66" y1="62" x2="123" y2="62" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M134,62 L122,67.5 L122,56.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="140" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="136" y1="182" x2="178" y2="182" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M192,182 L177,189 L177,175 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="157.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="77.5" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W > 0$</div></foreignObject>
  <foreignObject x="10" y="281.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liikkeen suuntaan}$</div></foreignObject>
  <line x1="200" y1="20" x2="200" y2="310" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="214" y="210" width="172" height="10" fill="#f1dfb5"/>
  <line x1="214" y1="210" x2="386" y2="210" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="264" y="154" width="72" height="56" rx="3" fill="#d9b26a" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="264" y1="182" x2="336" y2="182" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266" y1="62" x2="323" y2="62" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M334,62 L322,67.5 L322,56.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="340" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="320" y1="210" x2="260" y2="210" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M246,210 L261,203 L261,217 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="215.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\mu$</div></foreignObject>
  <foreignObject x="277.5" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W < 0$</div></foreignObject>
  <foreignObject x="210" y="281.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liikettä vastaan}$</div></foreignObject>
  <line x1="400" y1="20" x2="400" y2="310" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="414" y="210" width="172" height="10" fill="#f1dfb5"/>
  <line x1="414" y1="210" x2="586" y2="210" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="464" y="154" width="72" height="56" rx="3" fill="#d9b26a" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="464" y1="182" x2="536" y2="182" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="62" x2="523" y2="62" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M534,62 L522,67.5 L522,56.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="540" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="514" y1="210" x2="514" y2="112" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M514,98 L521,113 L507,113 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="528" y="99.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="477.5" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = 0$</div></foreignObject>
  <foreignObject x="410" y="281.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kohtisuoraan}$</div></foreignObject>
</svg>

### Kitka muuttaa mekaanista energiaa sisäenergiaksi
Todellisessa vuoristoradassa pyörien vierimisvastus ja ilmanvastus vastustavat liikettä koko matkan ajan. Ne tekevät negatiivista työtä, ja vaunun mekaaninen energia pienenee juuri tämän työn verran. Energia ei katoa, vaan se muuttuu pyörien, kiskojen ja ilman sisäenergiaksi, jolloin ne lämpenevät hieman. Kokonaisenergia säilyy aina. Mekaaninen energia säilyy vain, kun kitkaa ja ilmanvastusta ei ole tai ne ovat niin pieniä, että ne voi jättää huomiotta.

Painon ja kitkan ero on tärkeä. Painon tekemä työ riippuu vain korkeuserosta: palatessaan samalle korkeudelle kappale saa takaisin saman energian, kulki se mitä reittiä tahansa. Siksi painoon liittyy potentiaalienergia, ja paino on **konservatiivinen voima**. Kitkan ja ilmanvastuksen tekemä negatiivinen työ kasvaa jokaisella kuljetulla metrillä, joten se riippuu reitistä. Tällaiselle **ei-konservatiiviselle voimalle** ei voi määritellä potentiaalienergiaa.

### Vastaus alun kysymykseen
Ketjuhissi nostaa junan ensimmäisen mäen huipulle. Sen jälkeen junalla on vain se mekaaninen energia, jonka se sai noston aikana, eikä mikään lisää sitä. Vastusvoimat vähentävät sitä jokaisella metrillä. Jos seuraava mäki olisi yhtä korkea kuin ensimmäinen, juna ei pääsisi sen huipulle. Jokaisen myöhemmän mäen on oltava matalampi, jotta junalle jää huipulla vielä liike-energiaa.

## Kaava: Mekaniikan energiaperiaate

### Työ ja liike-energia
Kun kappale siirtyy suoraviivaisesti matkan $s$ ja siihen vaikuttaa vakiovoima $\overline{F}$, voiman tekemä työ on
```latex
W = F_\parallel\, s
```
missä $F_\parallel$ on voiman liikkeen suuntainen komponentti ($\text{N}$), negatiivinen silloin, kun komponentti osoittaa liikettä vastaan, ja $s$ kuljettu matka ($\text{m}$). Työn yksikkö on $1\,\text{N}\cdot\text{m} = 1\,\text{J}$.

Kun kappaleeseen vaikuttaa liikkeen suuntainen vakio kokonaisvoima $\Sigma F$, se kiihtyy tasaisesti, ja sen kiihtyvyys on $a = \tfrac{\Sigma F}{m}$. Luvussa *Kiihtyvyys ja tasaisesti kiihtyvä liike* opit, että tasaisesti kiihtyvässä liikkeessä kiihtyvyys on $a = \tfrac{v_2 - v_1}{t}$ ja kuljettu matka on keskinopeus kertaa aika, $s = \tfrac{v_1 + v_2}{2}\,t$. Kun nämä kerrotaan keskenään, aika supistuu pois:
```latex
\begin{aligned}
&a s = \frac{v_2 - v_1}{t} \cdot \frac{v_1 + v_2}{2}\,t \\
&\phantom{as} = \tfrac12 \left(v_2^2 - v_1^2\right)
\end{aligned}
```
Kun yhtälö kerrotaan puolittain massalla $m$ ja sijoitetaan $ma = \Sigma F$, saadaan $\Sigma F\, s = \tfrac{1}{2} m v_2^2 - \tfrac{1}{2} m v_1^2$. Kokonaisvoiman tekemä työ on siis yhtä suuri kuin liike-energian muutos:
```latex
W_\text{kok} = \Delta E_\text{k}
```
missä $W_\text{kok}$ on kaikkien kappaleeseen vaikuttavien voimien yhdessä tekemä työ ($\text{J}$) ja $\Delta E_\text{k} = E_{\text{k},2} - E_{\text{k},1}$ liike-energian muutos ($\text{J}$). Kun esimerkiksi kärryn massa on $2{,}0\,\text{kg}$ ja kokonaisvoima $12\,\text{N}$ kiihdyttää sitä levosta matkan $3{,}0\,\text{m}$, voima tekee työn $36\,\text{J}$, ja kärryn nopeus on lopussa $6{,}0\,\text{m/s}$.

### Energiaperiaate
Kokonaistyö jaetaan kahteen osaan: painon tekemään työhön $W_G$ ja kaikkien muiden voimien tekemään työhön $W_\text{muut}$. Muita voimia ovat esimerkiksi kitka, ilmanvastus, vetävä köysi ja työntävä käsi. Kun kappale laskeutuu korkeuden $h$, paino tekee työn $mgh$ ja potentiaalienergia pienenee saman verran, joten $W_G = -\Delta E_\text{p}$. Kun tämä sijoitetaan yhtälöön $W_G + W_\text{muut} = \Delta E_\text{k}$, saadaan **mekaniikan energiaperiaate**:
```latex
\begin{aligned}
&E_{\text{k},1} + E_{\text{p},1} + W_\text{muut} \\
&\quad = E_{\text{k},2} + E_{\text{p},2}
\end{aligned}
```
missä indeksi $1$ tarkoittaa alkutilannetta ja $2$ lopputilannetta, $E_\text{k} = \tfrac{1}{2} mv^2$ on liike-energia, $E_\text{p} = mgh$ potentiaalienergia korkeudella $h$ valitusta nollatasosta ja $W_\text{muut}$ muiden voimien kuin painon tekemä työ ($\text{J}$). Sanoin: mekaanisen energian muutos on yhtä suuri kuin muiden voimien kuin painon tekemä työ, $\Delta E_\text{mek} = W_\text{muut}$. Nollatason saa valita vapaasti, esimerkiksi tilanteen alimpaan kohtaan, koska vain korkeuden muutos vaikuttaa tulokseen.

<svg data-fig="palkit" viewBox="0 0 600 360" role="img" aria-label="Energiapalkit, kaavakuva mittakaavassa: alussa kappaleella on vain potentiaalienergiaa E_p,1, liike-energia E_k,1 on nolla. Kitka tekee negatiivisen työn W_muut, jonka palkki osoittaa nollatasosta alaspäin. Lopussa kappaleella on vain liike-energiaa E_k,2 ja potentiaalienergia E_p,2 on nolla. Katkoviiva alun mekaanisen energian korkeudella näyttää, että loppuenergia on alkuenergiaa pienempi juuri kitkan työn verran." style="max-width:100%;font-size:24px">
  <foreignObject x="78.5" y="11.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alussa}$</div></foreignObject>
  <foreignObject x="432.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lopussa}$</div></foreignObject>
  <line x1="30" y1="232" x2="570" y2="232" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="140" y="72" width="40" height="160" fill="#2b8a3e"/>
  <rect x="280" y="232" width="40" height="64" fill="#e8590c"/>
  <rect x="420" y="136" width="40" height="96" fill="#1971c2"/>
  <foreignObject x="220" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="360" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$=$</div></foreignObject>
  <line x1="180" y1="72" x2="540" y2="72" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M470,72 h8 V136 h-8" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="486" y="89.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$|W_\text{muut}|$</div></foreignObject>
  <foreignObject x="51" y="317.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_{\text{k},1}$</div></foreignObject>
  <foreignObject x="131" y="317.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_{\text{p},1}$</div></foreignObject>
  <foreignObject x="265" y="317.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$W_\text{muut}$</div></foreignObject>
  <foreignObject x="411" y="317.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_{\text{k},2}$</div></foreignObject>
  <foreignObject x="491" y="317.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_{\text{p},2}$</div></foreignObject>
  <foreignObject x="70" y="199.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="510" y="199.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
</svg>

Kitka ja ilmanvastus tekevät aina negatiivista työtä, joten ne pienentävät mekaanista energiaa. Vetävä köysi tai moottori voi tehdä positiivista työtä ja kasvattaa sitä, kuten ketjuhissi, joka nostaa junaa. Jos muut voimat eivät tee työtä, $W_\text{muut} = 0$, ja energiaperiaatteesta tulee **mekaanisen energian säilymislaki**:
```latex
\begin{aligned}
&E_{\text{k},1} + E_{\text{p},1} \\
&\quad = E_{\text{k},2} + E_{\text{p},2}
\end{aligned}
```
Kun kappale lähtee levosta korkeudelta $h$ ja laskeutuu nollatasolle, säilymislaista $mgh = \tfrac{1}{2} mv^2$ saadaan $v = \sqrt{2gh}$. Massa supistuu pois, joten nopeus ei riipu massasta.

## Esimerkki
Lapsi laskee pulkalla mäen alas. Lapsen ja pulkan yhteinen massa on $32\,\text{kg}$. Pulkka lähtee levosta mäen huipulta, joka on $5{,}0\,\text{m}$ korkeammalla kuin mäen juuri. Mäen juurella pulkan nopeudeksi mitataan $7{,}6\,\text{m/s}$. Kuinka suuren työn kitka ja ilmanvastus tekevät yhteensä pulkkaan laskun aikana?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 32\,\text{kg}$, korkeusero $h = 5{,}0\,\text{m}$, alkunopeus $v_1 = 0$, loppunopeus $v_2 = 7{,}6\,\text{m/s}$ ja $g = 9{,}81\,\text{m/s}^2$. Kysytään kitkan ja ilmanvastuksen yhdessä tekemää työtä $W_\text{muut}$.

<!-- vaihe -->

**Periaate.** Pulkkaan vaikuttavat paino, lumen tukivoima, kitka ja ilmanvastus. Tukivoima on kohtisuorassa liikettä vastaan, joten se ei tee työtä. Painon työ otetaan huomioon potentiaalienergian muutoksena. Kitka ja ilmanvastus ovat muita voimia, joten käytetään energiaperiaatetta. Nollataso valitaan mäen juurelle.

<!-- vaihe -->

**Kaava ratkaistuna.** Alussa $E_{\text{k},1} = 0$ ja $E_{\text{p},1} = mgh$, lopussa $E_{\text{k},2} = \tfrac{1}{2} mv_2^2$ ja $E_{\text{p},2} = 0$:
```latex
\begin{aligned}
&mgh + W_\text{muut} = \tfrac{1}{2} m v_2^2 \\
&W_\text{muut} = \tfrac{1}{2} m v_2^2 - mgh
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki suureet ovat SI-yksiköissä, ja $1\,\text{kg}\cdot\tfrac{\text{m}^2}{\text{s}^2} = 1\,\text{J}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin loppuhetken liike-energia ja alun potentiaalienergia ja sitten niiden erotus:
```latex
\begin{aligned}
&\tfrac{1}{2} m v_2^2 \\
&= \tfrac12 \cdot 32\,\text{kg} \cdot \left(7{,}6\,\tfrac{\text{m}}{\text{s}}\right)^2 \\
&= 924{,}16\,\text{J} \\[6pt]
&mgh \\
&= 32\,\text{kg} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 5{,}0\,\text{m} \\
&= 1569{,}6\,\text{J} \\[6pt]
&W_\text{muut} \\
&= 924{,}16\,\text{J} - 1569{,}6\,\text{J} \\
&= -645{,}44\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kitka ja ilmanvastus tekevät yhteensä työn $W_\text{muut} \approx -6{,}5 \cdot 10^2\,\text{J}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla kuten korkeus $5{,}0\,\text{m}$ ja nopeus $7{,}6\,\text{m/s}$. Työ on negatiivinen, koska kitka ja ilmanvastus vastustavat liikettä: noin $650\,\text{J}$ mekaanista energiaa muuttui lumen, jalasten ja ilman sisäenergiaksi.

<!-- vaihe -->

**Järkevyys.** Ilman kitkaa ja ilmanvastusta pulkan nopeus olisi mäen juurella $\sqrt{2gh} \approx 9{,}9\,\text{m/s}$, joten mitattu $7{,}6\,\text{m/s}$ on pienempi, kuten pitääkin. Mekaanista energiaa muuttui sisäenergiaksi noin $41\,\%$ alun potentiaalienergiasta. Jos rinne on $24\,\text{m}$ pitkä, keskimääräinen vastusvoima on $645\,\text{J} : 24\,\text{m} \approx 27\,\text{N}$, alle kymmenesosa painosta $314\,\text{N}$, mikä on uskottava liukuvalle pulkalle.

## Yleinen virhekäsitys
Moni ajattelee, että raskaampi kappale on mäen alla nopeampi. Kun kitka ja ilmanvastus voi jättää huomiotta, massa supistuu säilymislaista pois: täysi ja tyhjä vaunu ovat laakson pohjalla yhtä nopeita. Raskaammalla vaunulla on pohjalla enemmän liike-energiaa, mutta sillä oli alussa myös enemmän potentiaalienergiaa.

Toinen virhe on sanoa, että kitka hävittää energiaa. Kitka pienentää mekaanista energiaa, mutta yhtä suuri määrä energiaa siirtyy sisäenergiaksi, ja kokonaisenergia säilyy. Kolmas virhe on laskea kitkan työ korkeuserosta. Kitkan työ on kitkavoima kertaa kuljettu matka pitkin rataa. Kun vastusvoima on yhtä suuri, pitkällä loivalla radalla mekaanista energiaa muuttuu sisäenergiaksi enemmän kuin lyhyellä jyrkällä, vaikka korkeusero olisi sama.

## Tiivistelmä
- Mekaaninen energia $E_\text{mek} = E_\text{k} + E_\text{p}$ säilyy, kun vain paino tekee työtä eli kitkan ja ilmanvastuksen voi jättää huomiotta. Tukivoima ei tee työtä, koska se on kohtisuorassa liikettä vastaan.
- Voima tekee työtä liikkeen suuntaisella komponentillaan, $W = F_\parallel s$: positiivista liikkeen suuntaan ja negatiivista liikettä vastaan.
- Kokonaisvoiman tekemä työ on yhtä suuri kuin liike-energian muutos, $W_\text{kok} = \Delta E_\text{k}$.
- Energiaperiaate: mekaanisen energian muutos on muiden voimien kuin painon tekemä työ, $\Delta E_\text{mek} = W_\text{muut}$. Kitka ja ilmanvastus muuttavat mekaanista energiaa sisäenergiaksi, ja kokonaisenergia säilyy.
- Paino on konservatiivinen voima, koska sen työ riippuu vain korkeuserosta. Kitka ja ilmanvastus ovat ei-konservatiivisia voimia, koska niiden työ kasvaa kuljetun matkan mukana.
