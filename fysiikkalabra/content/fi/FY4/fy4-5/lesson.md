# Voimakuvio ja voimien yhteisvaikutus

> **Miksi** pulkka voi painaa lunta eri tavalla, kun sitä vedetään narusta vinosti ylöspäin, kuin silloin, kun se vain seisoo paikallaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen piha. Vasemmalla pulkka seisoo paikallaan ja on painunut syvälle lumeen. Oikealla lapsi vetää samanlaista pulkkaa narusta vinosti ylöspäin, ja sen jättämä jälki lumessa on matalampi." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy45h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy45h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy45h-snow" gradientUnits="userSpaceOnUse" x1="0" y1="340" x2="0" y2="600"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy45h-s1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient><linearGradient id="fy45h-s2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy45h-sky)"/>
  <circle cx="1040" cy="90" r="64" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="1040" cy="90" r="40" fill="url(#fy45h-sun)"/>
  <path d="M0,230 Q100,208 200,228 Q300,186 400,232.5 Q500,196 600,230.5 Q700,214.5 800,226.5 Q900,211.5 1000,227 Q1100,206 1200,228.5 Q1300,180.5 1400,233.5 V600 H0 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,262.5 Q100,227 200,259 Q300,221.5 400,260 Q500,225.5 600,259.5 Q700,247.5 800,264.5 Q900,233 1000,260 Q1100,235.5 1200,260 Q1300,239.5 1400,263.5 V600 H0 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M0,300 L13,258 L26,300 L40,252.5 L54.5,300 L67.5,257 L80.5,300 L99.5,233.5 L118,300 L134,244.5 L150,300 L169,233.5 L187.5,300 L204,242 L221,300 L232.5,264 L244,300 L262,236 L280,300 L291,266 L302.5,300 L315.5,257.5 L328.5,300 L345.5,240 L363,300 L379,244 L395,300 L407,263.5 L418.5,300 L429.5,266 L440.5,300 L453,260.5 L465.5,300 L480.5,249.5 L495,300 L509.5,251.5 L524,300 L536,262.5 L548,300 L559,267.5 L569.5,300 L581,263.5 L593,300 L609,244.5 L625,300 L642.5,238 L660.5,300 L672.5,261 L685,300 L697,262 L709,300 L720.5,264.5 L731.5,300 L751,230.5 L770.5,300 L781.5,265.5 L793,300 L810.5,237.5 L828.5,300 L842.5,253.5 L856.5,300 L873.5,239.5 L891,300 L909,236 L927,300 L942,249.5 L957,300 L969,262.5 L980.5,300 L994.5,253.5 L1008.5,300 L1025.5,242 L1042,300 L1061,232.5 L1080,300 L1091.5,263 L1103.5,300 L1120,242.5 L1136.5,300 L1150,254.5 L1164,300 L1178,254.5 L1191.5,300 L1208,243 L1224.5,300 V340 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M253.5,261 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M990.5,267.5 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M646.5,298.5 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M41,299 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M128.5,267 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M320.5,296.5 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M1169,289.5 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M513.5,294.5 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M4,273 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M600,283.5 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M693,270.5 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M884.5,266 l8,-14 l8,14 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="60" y="222" width="300" height="130" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="74" y1="225" x2="74" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="88" y1="225" x2="88" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="102" y1="225" x2="102" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="116" y1="225" x2="116" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="130" y1="225" x2="130" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="144" y1="225" x2="144" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="158" y1="225" x2="158" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="172" y1="225" x2="172" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="186" y1="225" x2="186" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="200" y1="225" x2="200" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="214" y1="225" x2="214" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="228" y1="225" x2="228" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="242" y1="225" x2="242" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="256" y1="225" x2="256" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="270" y1="225" x2="270" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="284" y1="225" x2="284" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="298" y1="225" x2="298" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="312" y1="225" x2="312" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="326" y1="225" x2="326" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="340" y1="225" x2="340" y2="349" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="60" y="222" width="10" height="130" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="350" y="222" width="10" height="130" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M40,222 L210,150.5 L380,222 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M40,222 L210,150.5 L380,222 l-8,8 L210,165 L48,230 Z" fill="#a5d8ff" stroke-linejoin="round"/>
  <rect x="90" y="258.5" width="40" height="52" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="90" y="258.5" width="40" height="52" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="110" y1="258.5" x2="110" y2="310.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="160" y="258.5" width="40" height="52" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="160" y="258.5" width="40" height="52" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="180" y1="258.5" x2="180" y2="310.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="230" y="258.5" width="40" height="52" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="230" y="258.5" width="40" height="52" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="250" y1="258.5" x2="250" y2="310.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <path d="M380,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M408,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M436,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M464,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M492,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M520,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M548,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M576,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M604,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M632,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M660,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M688,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M716,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M744,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M772,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M800,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M828,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M856,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M884,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M912,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M940,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M968,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M996,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1024,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1052,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1080,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1108,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1136,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1164,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1192,352 V312 l9,-10 l9,10 V352 Z" fill="#ffffff" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <rect x="370" y="322" width="830" height="8" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <rect x="1142.5" y="110" width="15" height="250" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1142.5" y="330" width="7.5" height="4" fill="#1f2933"/>
  <rect x="1150" y="300" width="7.5" height="4" fill="#1f2933"/>
  <rect x="1142.5" y="270" width="7.5" height="4" fill="#1f2933"/>
  <rect x="1150" y="240" width="7.5" height="4" fill="#1f2933"/>
  <rect x="1142.5" y="210" width="7.5" height="4" fill="#1f2933"/>
  <rect x="1150" y="180" width="7.5" height="4" fill="#1f2933"/>
  <rect x="1142.5" y="150" width="7.5" height="4" fill="#1f2933"/>
  <line x1="1150" y1="205" x2="1105" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1150" y1="172.5" x2="1195" y2="142.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1150" y1="147.5" x2="1105" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <path d="M0,350 Q300,336 600,350 T1200,346 V600 H0 Z" fill="url(#fy45h-snow)" stroke-linejoin="round"/>
  <path d="M1104,376 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M342.5,386.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M498.5,450 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M611,443.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M129,577 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M709.5,488.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M386,495 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M637,494.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M479,496.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M400,495 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M925.5,453 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M350,571.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M988,548.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1001.5,413.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1183,534.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M452,516.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M397.5,580.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M163.5,470.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M266,573.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M887.5,480 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M117.5,485.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M3.5,479.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M808.5,392.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M882,388.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M565.5,460.5 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M738.5,563 q14,-4 28,0" fill="none" stroke="#a5d8ff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="885" cy="522" rx="14" ry="6" fill="#d0e6fb" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="927" cy="534" rx="14" ry="6" fill="#d0e6fb" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="969" cy="522" rx="14" ry="6" fill="#d0e6fb" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="1011" cy="534" rx="14" ry="6" fill="#d0e6fb" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="250" cy="474" rx="184.0" ry="34.0" fill="#d0e6fb"/>
  <path d="M100.0,444 Q94.0,510 130.0,510 H350.0 Q410.0,510 418.0,426 L392.0,424 Q380.0,456 340.0,456 H126.0 L120.0,436 Z" fill="url(#fy45h-s1)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M130.0,466 H330.0" fill="none" stroke="#f2a69c" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <rect x="144" y="474" width="34" height="14" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="308" y="474" width="34" height="14" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M50.0,470 Q80.0,456 110.0,466 H390.0 Q420.0,456 450.0,470 V530 H50.0 Z" fill="url(#fy45h-snow)" stroke-linejoin="round"/>
  <path d="M50.0,470 Q80.0,456 110.0,466 H390.0 Q420.0,456 450.0,470" fill="none" stroke="#4f8fbf" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M440,464 H560" fill="none" stroke="#4f8fbf" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.7"/>
  <path d="M440,478 H560" fill="none" stroke="#4f8fbf" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.7"/>
  <ellipse cx="700" cy="474" rx="184.0" ry="17.0" fill="#d0e6fb"/>
  <path d="M550.0,410 Q544.0,476 580.0,476 H800.0 Q860.0,476 868.0,392 L842.0,390 Q830.0,422 790.0,422 H576.0 L570.0,402 Z" fill="url(#fy45h-s2)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M580.0,432 H780.0" fill="none" stroke="#f2a69c" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <rect x="594" y="440" width="34" height="14" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="758" y="440" width="34" height="14" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M500.0,470 Q530.0,456 560.0,466 H840.0 Q870.0,456 900.0,470 V530 H500.0 Z" fill="url(#fy45h-snow)" stroke-linejoin="round"/>
  <path d="M500.0,470 Q530.0,456 560.0,466 H840.0 Q870.0,456 900.0,470" fill="none" stroke="#4f8fbf" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="854" y1="394" x2="1010" y2="330" stroke="#b8622d" stroke-width="5" stroke-linecap="round"/>
  <path d="M1050,421 L1022,516.5" fill="none" stroke="#1f2933" stroke-width="18.6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1009.5,520 h27.5" fill="none" stroke="#1f2933" stroke-width="12.4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1067,336.5 L1010,330" fill="none" stroke="#1971c2" stroke-width="14.88" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1042,321.5 Q1090.5,303 1079,359 L1065,427 H1027.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1050,421 L1078,516.5" fill="none" stroke="#1f2933" stroke-width="18.6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1088,520 h27.5" fill="none" stroke="#1f2933" stroke-width="12.4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1070.5,334 L1010,330" fill="none" stroke="#1971c2" stroke-width="14.88" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1010" cy="330" r="8.06" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="1073.5" y="297" width="12.5" height="18.5" fill="#f1dfb5"/>
  <path d="M1063.5,309 Q1079.5,319 1096,309 L1093.5,299.5 H1066 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="1079.5" cy="280.5" r="21.08" fill="#f1dfb5"/>
  <path d="M1057.5,279.5 Q1058.5,248.5 1079.5,248.5 Q1101,248.5 1102,279.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="1056" y="273" width="47" height="8.5" rx="3.72" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1076" cy="244.5" r="7.44" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
</svg>

## Ydinajatus
Kappaleeseen vaikuttaa yleensä monta voimaa yhtä aikaa. Maa vetää sitä alaspäin, alusta tukee, naru vetää ja pinta jarruttaa. Jokainen voima kertoo yhdestä vuorovaikutuksesta kappaleen ja jonkin toisen kappaleen välillä. Liikkeen ratkaisee näiden voimien **yhteisvaikutus** eli **kokonaisvoima** $\Sigma\overline{F}$, joka on voimien vektorisumma. Luvussa *Newtonin toinen laki* opit, että kokonaisvoima määrää kiihtyvyyden: $\Sigma\overline{F} = m\overline{a}$.

Jotta kaikki voimat tulevat mukaan eikä mitään ylimääräistä eksy laskuun, voimat piirretään ensin **voimakuvioon**. Se on eri kuva kuin **tilannekuva**. Tilannekuvassa näkyy koko tilanne: alusta, naru, vetäjä ja liikkeen suunta. Voimakuviossa on vain valittu kappale pelkistettynä suorakulmiona ja siihen vaikuttavat voimat nuolina. Nuolen suunta on voiman suunta, ja nuolten pituudet kertovat, mikä voima on suurempi.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa samasta tilanteesta. Vasemmalla tilannekuva: laatikkoa vedetään lattiaa pitkin narulla, joka nousee vinosti ylöspäin, ja laatikon yllä ohut sininen nuoli näyttää nopeuden oikealle. Oikealla voimakuvio: vain laatikko suorakulmiona ja siihen vaikuttavat voimat punaisina nuolina. Paino G osoittaa keskipisteestä suoraan alas, lattian tukivoima N alapinnasta suoraan ylös ja on lyhyempi kuin paino, narun jännitysvoima T lähtee narun kiinnityskohdasta vinosti ylös oikealle ja lattian kitkavoima lähtee alapinnan takakulmasta vasemmalle. Nopeutta ei piirretä voimakuvioon." style="max-width:100%;font-size:24px">
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <line x1="20" y1="200" x2="280" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="20" y1="200" x2="10" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="36" y1="200" x2="26" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="52" y1="200" x2="42" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="68" y1="200" x2="58" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="200" x2="74" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="200" x2="90" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="200" x2="106" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="132" y1="200" x2="122" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="200" x2="138" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164" y1="200" x2="154" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="200" x2="170" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="196" y1="200" x2="186" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="212" y1="200" x2="202" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="228" y1="200" x2="218" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="244" y1="200" x2="234" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="200" x2="250" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="200" x2="266" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="80" y="140" width="80" height="60" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="160" y1="160" x2="246.5" y2="110" stroke="#a97a35" stroke-width="3" stroke-linecap="round"/>
  <circle cx="246.5" cy="110" r="8" fill="#6b7480"/>
  <line x1="90" y1="110" x2="158" y2="110" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M147,116.5 L160,110 L147,103.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="165.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="383.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <rect x="400" y="140" width="80" height="60" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="170" x2="440" y2="266" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,283 L432,265 L448,265 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="443.5" y="264.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="460" y1="200" x2="460" y2="133" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M460,116 L468,134 L452,134 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="463.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="480" y1="160" x2="515" y2="140" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,131 L518.5,147.5 L510,133 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="534" y="105" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="400" y1="200" x2="382.5" y2="200" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M365.5,200 L383.5,192 L383.5,208 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="329" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

Kuvan laatikkoa vedetään narulla vinosti ylöspäin. Narun voima osoittaa sekä eteenpäin että ylöspäin. Ylöspäin osoittava osa kannattelee laatikkoa, joten lattian ei tarvitse tukea sitä yhtä paljon kuin paikallaan seistessä. Siksi tukivoima $N$ on pienempi kuin paino $G$. Nopeutta ei piirretä voimakuvioon, koska nopeus ei ole voima.

## Voimakuvion piirtäminen
Voimakuvio piirretään aina samoilla kahdeksalla vaiheella. Ne kannattaa käydä läpi joka kerta, myös silloin, kun tilanne näyttää helpolta.

1. **Valitse kappale.** Päätä, minkä kappaleen voimat piirrät. Voimakuvioon tulevat vain voimat, jotka vaikuttavat **tähän kappaleeseen**. Voimat, joilla kappale itse vaikuttaa muihin, eivät kuulu siihen.
2. **Etsi vuorovaikutukset.** Luettele kaikki, mikä vaikuttaa kappaleeseen: Maa (paino), jokainen pinta, jota kappale koskettaa (tukivoima ja kitka), jokainen naru (jännitysvoima), työntö tai veto sekä ilma tai vesi (vastus ja noste). Jokaisella voimalla on aiheuttaja kappaleen ulkopuolella. Pelkkä liike ei aiheuta voimaa.
3. **Piirrä kappale ja voimat.** Piirrä kappale pelkistettynä suorakulmiona. Piirrä kullekin voimalle yksi nuoli, joka lähtee voiman vaikutuskohdasta. Työntävän voiman nuoli voi myös päättyä vaikutuskohtaan.
   - Paino $\overline{G}$ osoittaa suoraan alas.
   - Tukivoima $\overline{N}$ on kohtisuorassa kosketuspintaa vastaan ja työntää kappaletta poispäin pinnasta. Se ei aina osoita ylös: katto työntää alas ja seinä sivulle.
   - Kitkavoima $\overline{F}_\mu$ on kosketuspinnan suuntainen. Sen suunta tulee siitä, mihin suuntaan kappale liukuu tai pyrkii liukumaan pinnan suhteen. Se ei aina ole nopeutta vastaan. Kitkan nuoli alkaa kosketuspinnan kulmasta kappaleen ulkopuolelle tai päättyy siihen. Sitä ei piirretä kappaleen sivua pitkin sivun keskeltä.
   - Jännitysvoima $\overline{T}$ vaikuttaa narun suuntaisesti ja vetää kappaletta narua kohti.
   - Ilmanvastus piirretään vain, kun tilanne ja sen oletukset sitä vaativat.
4. **Nimeä voimat.** Anna jokaiselle voimalle oma tunnus. Kaksi samanlaista voimaa erotetaan indekseillä, esimerkiksi $\overline{T}_1$ ja $\overline{T}_2$.
5. **Mieti suuruudet.** Levossa ja tasaisessa liikkeessä kokonaisvoima on nolla, joten nuolet kumoavat toisensa. Kiihtyvässä liikkeessä kokonaisvoima osoittaa kiihtyvyyden suuntaan, joka ei aina ole nopeuden suunta. Älä keksi tarkkoja pituuksia, jos tiedot eivät niitä määrää.
6. **Vain voimat.** Nopeus, kiihtyvyys ja siirtymä eivät ole voimia. Jos niitä tarvitaan, ne piirretään kappaleen viereen ohuina nuolina ja eri värein: tässä kurssissa voimat ovat punaisia, nopeus sininen ja kiihtyvyys oranssi. Kokonaisvoima ei ole yksi voima lisää.
7. **Komponentit eivät ole uusia voimia.** Kun voima jaetaan komponentteihin, komponentit yhdessä korvaavat voiman laskussa. Ne piirretään katkoviivalla, jotta niitä ei sekoiteta voimiin.
8. **Liikeyhtälö.** Vasta nyt valitaan akselit ja kirjoitetaan Newtonin toinen laki komponenteittain kuvion voimista ja etumerkeistä.

<svg data-fig="suunnat" viewBox="0 0 600 620" role="img" aria-label="Neljä tilannetta. Kussakin on vasemmalla pieni tilannekuva ja oikealla kappaleen voimakuvio, jossa kappale on suorakulmio eikä pintoja piirretä. Vasemmalla ylhäällä laatikko lepää vaakasuoralla lattialla: paino G keskipisteestä alas ja yhtä pitkä tukivoima N alapinnasta ylös. Oikealla ylhäällä laatikko on paikallaan kaltevalla rinteellä: voimakuviossa suorakulmio on kallellaan kuten rinteellä, paino G suoraan alas, tukivoima N kohtisuoraan alapintaa vastaan ja kitkavoima alapinnan ylemmästä kulmasta rinteen suuntaisesti ylös. Vasemmalla alhaalla lamppu roikkuu johdon varassa: paino G alas ja johdon jännitysvoima T yläpinnasta ylös. Oikealla alhaalla heliumilmapallo painuu kattoa vasten ja on paikallaan: noste keskipisteestä ylös, paino keskipisteestä alas ja katon tukivoima N, joka painaa yläpintaa alaspäin, pois katon pinnasta. Nosteen nuoli on yhtä pitkä kuin painon ja tukivoiman nuolet yhteensä." style="max-width:100%;font-size:24px">
  <line x1="300" y1="10" x2="300" y2="610" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="10" y1="310" x2="590" y2="310" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="108.5" y="9.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lattia}$</div></foreignObject>
  <line x1="20" y1="190" x2="120" y2="190" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="20" y1="190" x2="10" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="36" y1="190" x2="26" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="52" y1="190" x2="42" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="68" y1="190" x2="58" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="190" x2="74" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="190" x2="90" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="190" x2="106" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="42" y="146" width="56" height="44" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="185" y="138" width="60" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="215" y1="160" x2="215" y2="231" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M215,248 L207,230 L223,230 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="218.5" y="229.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="230" y1="182" x2="230" y2="111" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M230,94 L238,112 L222,112 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="233.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="415" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rinne}$</div></foreignObject>
  <line x1="312" y1="230" x2="421" y2="179.5" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="312" y1="230" x2="302" y2="242" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326.5" y1="223" x2="316.5" y2="235" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="341" y1="216.5" x2="331" y2="228.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="355.5" y1="209.5" x2="345.5" y2="221.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="203" x2="360" y2="215" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384.5" y1="196" x2="374.5" y2="208" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="399" y1="189.5" x2="389" y2="201.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="413.5" y1="182.5" x2="403.5" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M350.1,212.3 L389.9,193.7 L375.6,162.8 L335.7,181.4 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="462" y="128" width="60" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-25 492 150)"/>
  <line x1="492" y1="150" x2="492" y2="221" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M492,238 L484,220 L500,220 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="495.5" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="512" y1="165" x2="485.5" y2="108" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M478.5,92.5 L493.5,105.5 L478.5,112.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="446" y="72" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="528.5" y1="157.5" x2="547" y2="148.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M562,141.5 L549.5,156.5 L542.5,142 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="539.5" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="108.5" y="319.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
  <line x1="30" y1="360" x2="110" y2="360" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="30" y1="360" x2="20" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="46" y1="360" x2="36" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="360" x2="52" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="78" y1="360" x2="68" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="94" y1="360" x2="84" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="70" y1="360" x2="70" y2="440" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M48,470 L92,470 L81,440 L59,440 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="190" y="452" width="50" height="36" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="215" y1="470" x2="215" y2="530" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M215,547 L207,529 L223,529 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="220.5" y="528.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="215" y1="452" x2="215" y2="392" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M215,375 L223,393 L207,393 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="220.5" y="380.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="377.5" y="319.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{heliumpallo}$</div></foreignObject>
  <line x1="316" y1="360" x2="430" y2="360" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="316" y1="360" x2="306" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332" y1="360" x2="322" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="348" y1="360" x2="338" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364" y1="360" x2="354" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="360" x2="370" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="396" y1="360" x2="386" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="412" y1="360" x2="402" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="372" cy="402" r="40" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="372" y1="442" x2="368" y2="520" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="480" y="470" width="70" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="515" y1="490" x2="515" y2="407" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M515,390 L523,408 L507,408 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="507.5" y="387.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{noste}$</div></foreignObject>
  <line x1="515" y1="490" x2="515" y2="513" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M515,530 L507,512 L523,512 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="516.5" y="519.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="495" y1="410" x2="495" y2="453" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M495,470 L487,452 L503,452 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="458.5" y="389.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
</svg>

Kuvassa on neljä tilannetta, joissa voimien suunnat yllättävät usein. Rinteellä tukivoima on kohtisuorassa rinnettä vastaan eikä pystysuora, ja kitka pitää laatikkoa paikallaan rinteen suuntaisesti. Kattoa vasten painuvaan heliumpalloon katto vaikuttaa alaspäin.

Voimakuviossa kappale on aina pelkistetty suorakulmio, ja jokainen voima lähtee vaikutuskohdastaan: paino keskipisteestä, tukivoima ja kitka kosketuspinnasta ja jännitysvoima narun kiinnityskohdasta. Työntävän voiman nuoli voi myös päättyä kohtaan, johon työntö kohdistuu. Tilannekuvassa kappaleet piirretään sellaisina kuin ne näyttävät, mutta voimakuvioon piirretään vain suorakulmio ja voimat.

Ylioppilaskokeiden arviointiohjeissa voimakuviolle on annettu tehtäväkohtaiset pisteet. Esimerkiksi kevään 2025 heliumpallotehtävässä puuttuva, ylimääräinen tai väärään suuntaan piirretty voima vei kaikki voimakuvion pisteet, ja nopeuden tai kiihtyvyyden piirtäminen pallon voimaksi samoin. Syksyn 2025 kokeessa puuttuvasta nimestä vähennettiin piste. Tarkka pisteytys vaihtelee tehtävästä toiseen, mutta joka kokeessa vaaditaan samaa: kaikki voimat, ei keksittyjä voimia, oikeat suunnat ja yksiselitteiset nimet.

## Kaava: Liikeyhtälö komponenteittain
Newtonin toinen laki koskee kokonaisvoimaa:
```latex
\Sigma\overline{F} = m\overline{a}
```
missä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien vektorisumma (N), $m$ kappaleen massa (kg) ja $\overline{a}$ sen kiihtyvyys (m/s²). Kun voimat eivät ole samalla suoralla, valitaan kaksi kohtisuoraa akselia ja kirjoitetaan laki kummankin akselin suuntaan erikseen:
```latex
\begin{aligned}
\Sigma F_x &= m a_x \\
\Sigma F_y &= m a_y
\end{aligned}
```
missä $\Sigma F_x$ ja $\Sigma F_y$ ovat voimien komponenttien summat (N) ja $a_x$ ja $a_y$ kiihtyvyyden komponentit (m/s²). Akselin suuntaan osoittava komponentti on positiivinen ja vastakkainen negatiivinen. Akselit kannattaa valita niin, että toinen osoittaa kiihtyvyyden suuntaan.

Vinon voiman $F$ komponentit saadaan suorakulmaisesta kolmiosta, kun $\alpha$ on voiman ja $x$-akselin välinen kulma:
```latex
\begin{aligned}
F_x &= F\cos\alpha \\
F_y &= F\sin\alpha
\end{aligned}
```
missä $F$ on voiman suuruus (N), $F_x$ ja $F_y$ sen komponentit (N) ja $\alpha$ kulma. Komponentit eivät ole uusia voimia, vaan ne korvaavat voiman $F$ laskussa.

<svg data-fig="komponentit" viewBox="0 0 600 300" role="img" aria-label="Kappaleeseen vaikuttaa voima F, joka lähtee kappaleen oikeasta yläkulmasta vinosti ylös oikealle kulmassa alfa vaakasuoraan nähden. Katkoviivoin piirretyt komponentit lähtevät samasta kulmasta: vaakasuora F x pitkin x-akselia ja pystysuora F y pitkin y-akselia. Komponentit ja voima muodostavat suorakulmaisen kolmion, jonka hypotenuusa on F. Merkinnät: F x on F kertaa kosini alfa ja F y on F kertaa sini alfa." style="max-width:100%;font-size:24px">
  <rect x="30" y="230" width="80" height="56" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="110" y1="230" x2="260" y2="125" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M274,115.5 L263.5,132 L254.5,119 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="251.5" y="83" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <line x1="110" y1="230" x2="272" y2="230" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M261,236.5 L274,230 L261,223.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="251.5" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{x}$</div></foreignObject>
  <line x1="110" y1="230" x2="110" y2="117.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M116.5,128.5 L110,115.5 L103.5,128.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="63.5" y="101" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{y}$</div></foreignObject>
  <line x1="274" y1="230" x2="274" y2="115.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="110" y1="115.5" x2="274" y2="115.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <path d="M162,230 A52,52 0 0 0 152.6,200.2" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="174" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="390" y="105.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_x = F\cos\alpha$</div></foreignObject>
  <foreignObject x="390" y="155.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_y = F\sin\alpha$</div></foreignObject>
</svg>

## Esimerkki
Pulkkaa, jonka massa on $12\,\text{kg}$, vedetään vaakasuoralla lumella narulla, joka on $35^\circ$:n kulmassa vaakatasoon nähden. Narun jännitysvoima on $80\,\text{N}$ ja lumen kitkavoima $30\,\text{N}$. Kuinka suuri on pulkan kiihtyvyys, ja kuinka suuri on lumen tukivoima?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 12\,\text{kg}$, $T = 80\,\text{N}$, $\alpha = 35^\circ$, $F_\mu = 30\,\text{N}$ ja $g = 9{,}81\,\text{m/s}^2$. Kysytään kiihtyvyyttä $a$ ja tukivoimaa $N$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi pulkka. Siihen vaikuttavat Maa (paino), lumi (tukivoima ja kitka) ja naru (jännitysvoima). Newtonin toinen laki kirjoitetaan kahteen suuntaan: vaakasuunnassa pulkka kiihtyy, pystysuunnassa se pysyy lumen pinnalla, joten $a_y = 0$.

<!-- vaihe -->

**Voimakuvio.** Pulkka piirretään suorakulmiona, ja voimat lähtevät vaikutuskohdistaan. Akselit valitaan niin, että $x$ osoittaa liikkeen suuntaan ja $y$ ylös. Narun voima jaetaan komponentteihin $T_x = T\cos\alpha$ ja $T_y = T\sin\alpha$, jotka on piirretty katkoviivalla.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Pulkan voimakuvio, pulkka suorakulmiona. Paino G keskipisteestä alas, lumen tukivoima N alapinnasta ylös ja painoa lyhyempi, narun jännitysvoima T etuyläkulmasta vinosti ylös oikealle kulmassa 35 astetta, sen komponentit katkoviivoin, ja lumen kitkavoima alapinnan takakulmasta vasemmalle. Nurkassa akselit: x oikealle eli liikkeen suuntaan ja y ylös." style="max-width:100%;font-size:24px">
  <rect x="210" y="163" width="120" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="270" y1="185" x2="270" y2="303.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M270,320.5 L262,302.5 L278,302.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="273.5" y="302" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="290" y1="207" x2="290" y2="141.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,124.5 L298,142.5 L282,142.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="243.5" y="116" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="330" y1="163" x2="391.5" y2="120" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M405.5,110 L395.5,127 L386,114 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="405" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="210" y1="207" x2="192.5" y2="207" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M175.5,207 L193.5,199 L193.5,215 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="143" y="176.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="330" y1="163" x2="403.5" y2="163" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M392.5,169.5 L405.5,163 L392.5,156.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="383" y="172.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{x}$</div></foreignObject>
  <line x1="330" y1="163" x2="330" y2="112" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M336.5,123 L330,110 L323.5,123" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="303.5" y="79.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{y}$</div></foreignObject>
  <path d="M370.0,163.0 A40,40 0 0 0 362.8,140.1" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="378" y="134.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$35^\circ$</div></foreignObject>
  <line x1="70" y1="320" x2="107" y2="320" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M116,320 L106,324.5 L106,315.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="70" y1="320" x2="70" y2="283" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M70,274 L74.5,284 L65.5,284 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="118" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="60" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Kuviosta luetaan liikeyhtälöt ja ratkaistaan kysytyt suureet:
```latex
\begin{aligned}
&x\text{:}\ \ T\cos\alpha - F_\mu = m a \\
&y\text{:}\ \ N + T\sin\alpha - mg = 0 \\
&a = \frac{T\cos\alpha - F_\mu}{m} \\
&N = mg - T\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki suureet ovat SI-yksiköissä, ja $\tfrac{\text{N}}{\text{kg}} = \tfrac{\text{m}}{\text{s}^2}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
&a = \frac{T\cos\alpha - F_\mu}{m} \\
&\phantom{a} = \frac{80\,\text{N}\cdot\cos 35^\circ - 30\,\text{N}}{12\,\text{kg}} \\
&\phantom{a} \approx 2{,}96\,\text{m/s}^2 \\[4pt]
&N = mg - T\sin\alpha \\
&\phantom{N} = 12\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\
&\quad\ - 80\,\text{N}\cdot\sin 35^\circ \\
&\phantom{N} \approx 71{,}8\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kiihtyvyys on $a \approx 3{,}0\,\text{m/s}^2$ ja tukivoima $N \approx 72\,\text{N}$, kahden merkitsevän numeron tarkkuudella kuten lähtötiedot $80\,\text{N}$, $30\,\text{N}$ ja $12\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** Pulkan paino on $mg \approx 118\,\text{N}$. Tukivoima $72\,\text{N}$ on sitä pienempi, koska narun pystykomponentti $T_y \approx 46\,\text{N}$ kannattelee osan painosta, ja $72\,\text{N} + 46\,\text{N} \approx 118\,\text{N}$. Ilman kitkaa kiihtyvyys olisi $65{,}5\,\text{N} : 12\,\text{kg} \approx 5{,}5\,\text{m/s}^2$, joten kitka pienentää sitä, kuten pitääkin.

## Yleinen virhekäsitys
Liikkuvaan kappaleeseen ei tarvitse vaikuttaa voimaa liikkeen suuntaan. Liukuvaan laatikkoon vaikuttavat vain paino, tukivoima ja kitka, eikä "liikkeen voimaa" ole: ei ole mitään kappaletta, joka sitä aiheuttaisi. Toinen yleinen virhe on pitää tukivoimaa aina yhtä suurena kuin paino. Tukivoima on juuri niin suuri, kuin tilanne vaatii: vinossa vedossa se on painoa pienempi, vinossa työnnössä suurempi ja ylöspäin kiihtyvässä hississä suurempi. Kolmas virhe on piirtää komponentit voimiksi voiman lisäksi, jolloin sama voima tulee laskuun kahteen kertaan.

## Tiivistelmä
- Voimakuviossa on vain valittu kappale suorakulmiona ja siihen vaikuttavat voimat. Tilannekuva ja voimakuvio ovat eri kuvia.
- Jokaisella voimalla on aiheuttaja: Maa, pinta, naru, työntäjä tai ilma. Nopeus ja kiihtyvyys eivät ole voimia, ja ne piirretään eri värein kuin voimat.
- Tukivoima on kohtisuorassa pintaa vastaan, kitka pinnan suuntainen ja jännitysvoima narun suuntainen.
- Kokonaisvoima on voimien vektorisumma, ja $\Sigma\overline{F} = m\overline{a}$ kirjoitetaan komponenteittain: $\Sigma F_x = m a_x$ ja $\Sigma F_y = m a_y$.
- Vinon voiman komponentit ovat $F\cos\alpha$ ja $F\sin\alpha$. Ne korvaavat voiman laskussa eivätkä ole uusia voimia.
