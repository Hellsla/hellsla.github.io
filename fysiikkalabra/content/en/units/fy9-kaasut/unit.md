# Pressure, gases and the heat engine

> **Why** must the pressure of a car's tyres be checked when a hard frost sets in, even though no air has leaked from the tyres?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a frosty morning in a yard. On the left a garage whose door is open and in which a warm light is on; a compressed-air hose hangs on the wall. In the yard stands a car that has been outside all night: there is frost on its roof and windows. The red column of the thermometer on the outer wall of the garage is low. In the background snowy spruces and a pale morning sky." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9ka-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fc3e0"/><stop offset="1" stop-color="#f3e3cf"/></linearGradient><linearGradient id="fy9ka-warm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe8c2"/><stop offset="1" stop-color="#ffc078"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy9ka-sky)"/>
  <circle cx="980" cy="300" r="70" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="980" cy="300" r="44" fill="#ffd8a8"/>
  <path d="M0,330 L13,306 L26.5,330 L39.5,306.5 L52.5,330 L73.5,286.5 L94.5,330 L112,295.5 L129.5,330 L149.5,289.5 L169.5,330 L185,299.5 L201,330 L220.5,290.5 L240,330 L252.5,308 L265,330 L285.5,288 L305.5,330 L327,285.5 L348.5,330 L362,305.5 L375.5,330 L396.5,286 L418,330 L431,307 L443.5,330 L461,296 L478.5,330 L499.5,286.5 L520.5,330 L538.5,295 L556,330 L575,291.5 L594,330 L614.5,288.5 L634.5,330 L654,291 L673,330 L695,284.5 L717,330 L731,304 L745.5,330 L764,292 L783,330 L796.5,305 L810,330 L822.5,307.5 L835.5,330 L853.5,293.5 L872,330 L891.5,290 L911,330 L931,289 L951.5,330 L965,305 L978.5,330 L994,301.5 L1009,330 L1023.5,302 L1038.5,330 L1050.5,308.5 L1062.5,330 L1077,303.5 L1091.5,330 L1108.5,296.5 L1125.5,330 L1142,298.5 L1158,330 L1175,296.5 L1192,330 L1211.5,290.5 L1231,330 V356 H0 Z" fill="#3d5a4a" stroke-linejoin="round"/>
  <path d="M0,330 Q300,316 600,326 T1200,322 V600 H0 Z" fill="#f8fbfd" stroke-linejoin="round"/>
  <path d="M0,470 Q320,452 640,466 T1200,462 V600 H0 Z" fill="#e6eff5" stroke-linejoin="round"/>
  <line x1="98" y1="494" x2="108" y2="494" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="103" y1="489" x2="103" y2="499" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="209.5" y1="554.5" x2="219.5" y2="554.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="214.5" y1="549.5" x2="214.5" y2="559.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="160" y1="351" x2="170" y2="351" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="165" y1="346" x2="165" y2="356" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="942.5" y1="388" x2="952.5" y2="388" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="947.5" y1="383" x2="947.5" y2="393" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="258" y1="438" x2="268" y2="438" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="263" y1="433" x2="263" y2="443" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="245.5" y1="470.5" x2="255.5" y2="470.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="250.5" y1="465.5" x2="250.5" y2="475.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="797" y1="401.5" x2="807" y2="401.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="802" y1="396.5" x2="802" y2="406.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1078.5" y1="563" x2="1088.5" y2="563" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1083.5" y1="558" x2="1083.5" y2="568" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="787.5" y1="536.5" x2="797.5" y2="536.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="792.5" y1="531.5" x2="792.5" y2="541.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1127.5" y1="574" x2="1137.5" y2="574" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1132.5" y1="569" x2="1132.5" y2="579" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1011.5" y1="542.5" x2="1021.5" y2="542.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1016.5" y1="537.5" x2="1016.5" y2="547.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="626" y1="401.5" x2="636" y2="401.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="631" y1="396.5" x2="631" y2="406.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1067" y1="404.5" x2="1077" y2="404.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1072" y1="399.5" x2="1072" y2="409.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="623.5" y1="491.5" x2="633.5" y2="491.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="628.5" y1="486.5" x2="628.5" y2="496.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="393" y1="405" x2="403" y2="405" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="398" y1="400" x2="398" y2="410" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="802" y1="567.5" x2="812" y2="567.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="807" y1="562.5" x2="807" y2="572.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="639" y1="364.5" x2="649" y2="364.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="644" y1="359.5" x2="644" y2="369.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="557.5" y1="462" x2="567.5" y2="462" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="562.5" y1="457" x2="562.5" y2="467" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="79" y1="549" x2="89" y2="549" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="84" y1="544" x2="84" y2="554" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1043" y1="385.5" x2="1053" y2="385.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1048" y1="380.5" x2="1048" y2="390.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1086.5" y1="442" x2="1096.5" y2="442" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="1091.5" y1="437" x2="1091.5" y2="447" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="727.5" y1="460" x2="737.5" y2="460" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="732.5" y1="455" x2="732.5" y2="465" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="906.5" y1="521.5" x2="916.5" y2="521.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="911.5" y1="516.5" x2="911.5" y2="526.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="731.5" y1="398.5" x2="741.5" y2="398.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="736.5" y1="393.5" x2="736.5" y2="403.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="900.5" y1="377.5" x2="910.5" y2="377.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="905.5" y1="372.5" x2="905.5" y2="382.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="953.5" y1="456.5" x2="963.5" y2="456.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="958.5" y1="451.5" x2="958.5" y2="461.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="692.5" y="377" width="15" height="23" fill="#b8622d"/>
  <path d="M631.5,381 L700,305 L768.5,381 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M700,305 L768.5,381 H700 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M647,339 L700,263 L753,339 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M700,263 L753,339 H700 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M662,297.5 L700,210 L738,297.5 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M700,210 L738,297.5 H700 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M643,367.5 L700,329.5 L757,367.5 l-11.5,-4 L700,341 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="764" y="382" width="12" height="18" fill="#b8622d"/>
  <path d="M716,385 L770,325 L824,385 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M770,325 L824,385 H770 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M728,352 L770,292 L812,352 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M770,292 L812,352 H770 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M740,319 L770,250 L800,319 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M770,250 L800,319 H770 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M725,374.5 L770,344.5 L815,374.5 l-9,-3 L770,353.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="1121.5" y="375" width="17" height="25" fill="#b8622d"/>
  <path d="M1054.5,379 L1130,295 L1205.5,379 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1130,295 L1205.5,379 H1130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1071,333 L1130,249 L1189,333 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1130,249 L1189,333 H1130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1088,286.5 L1130,190 L1172,286.5 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1130,190 L1172,286.5 H1130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1067,364.5 L1130,322.5 L1193,364.5 l-12.5,-4 L1130,335 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="1178.5" y="381" width="13" height="19" fill="#b8622d"/>
  <path d="M1127.5,384 L1185,320 L1242.5,384 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1185,320 L1242.5,384 H1185 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1140,349 L1185,285 L1230,349 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1185,285 L1230,349 H1185 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1153,313.5 L1185,240 L1217,313.5 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1185,240 L1217,313.5 H1185 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1137,373 L1185,341 L1233,373 l-9.5,-3 L1185,350.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="70" y="240" width="420" height="230" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="84" y1="243" x2="84" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="98" y1="243" x2="98" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="112" y1="243" x2="112" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="126" y1="243" x2="126" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="140" y1="243" x2="140" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="154" y1="243" x2="154" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="168" y1="243" x2="168" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="182" y1="243" x2="182" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="196" y1="243" x2="196" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="210" y1="243" x2="210" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="224" y1="243" x2="224" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="238" y1="243" x2="238" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="252" y1="243" x2="252" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="266" y1="243" x2="266" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="280" y1="243" x2="280" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="294" y1="243" x2="294" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="308" y1="243" x2="308" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="322" y1="243" x2="322" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="336" y1="243" x2="336" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="350" y1="243" x2="350" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="364" y1="243" x2="364" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="378" y1="243" x2="378" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="392" y1="243" x2="392" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="406" y1="243" x2="406" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="420" y1="243" x2="420" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="434" y1="243" x2="434" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="448" y1="243" x2="448" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="462" y1="243" x2="462" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="476" y1="243" x2="476" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="70" y="240" width="10" height="230" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="480" y="240" width="10" height="230" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M46,240 L280.0,144 L514,240 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M46,240 L280.0,144 L514,240 l-9,9 L280.0,156 L55,249 Z" fill="#a5d8ff" stroke-linejoin="round"/>
  <rect x="110" y="290" width="250" height="180" fill="url(#fy9ka-warm)" stroke="#1f2933" stroke-width="3"/>
  <rect x="116" y="290" width="238" height="10" fill="#6c757d"/>
  <circle cx="235.0" cy="320" r="10" fill="#fff4e0" stroke="#1f2933" stroke-width="2"/>
  <path d="M110,470 L360,470 L430,530 L60,530 Z" fill="#ffc078" fill-opacity="0.35"/>
  <rect x="134" y="406" width="64" height="64" rx="6" fill="#1971c2" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="166" cy="430" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="166" y1="430" x2="173" y2="423" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <path d="M198,420 Q260,330 300,370 Q332,404 310,440" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="302" y="436" width="16" height="22" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="250" y="342" width="96" height="8" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="320" cy="440" r="28" fill="#1f2933"/>
  <circle cx="320" cy="440" r="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="441" y="290" width="18" height="140" rx="9" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="450" cy="430" r="16" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <rect x="446" y="400" width="8" height="30" fill="#c92a2a"/>
  <line x1="459" y1="408" x2="467" y2="408" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="386" x2="467" y2="386" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="364" x2="467" y2="364" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="342" x2="467" y2="342" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="320" x2="467" y2="320" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="441" y="290" width="18" height="140" rx="9" fill="none" stroke="#a5d8ff" stroke-width="2"/>
  <path d="M640,520 L646,480 Q654,462 680,458 L728,434 Q760,422 812,422 L874,422 Q912,424 938,454 L980,468 Q1002,474 1004,498 L1004,520 Z" fill="#5c7c99" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M694,458 L738,438 Q766,428 806,428 L806,458 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M818,428 L870,428 Q900,432 922,458 L818,458 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="713.5" y1="454" x2="723.5" y2="436.5" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="737.5" y1="454" x2="747.5" y2="438.5" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="760" y1="454" x2="770" y2="442" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="786.5" y1="454" x2="796.5" y2="441" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="807.5" y1="454" x2="817.5" y2="437" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="832.5" y1="454" x2="842.5" y2="436.5" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="854" y1="454" x2="864" y2="437.5" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="873.5" y1="454" x2="883.5" y2="440" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <line x1="901" y1="454" x2="911" y2="439.5" stroke="#a5d8ff" stroke-width="2" stroke-linecap="round"/>
  <path d="M736,428 Q790,412 870,418 Q912,422 930,444 L922,448 Q900,428 868,426 Q800,422 740,434 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="652" y="486" width="14" height="12" rx="3" fill="#fff4e0" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="712" cy="522" r="30" fill="#1f2933"/>
  <circle cx="712" cy="522" r="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="930" cy="522" r="30" fill="#1f2933"/>
  <circle cx="930" cy="522" r="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M618,554 Q820,566 1030,554" fill="none" stroke="#c9d6e0" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

## Key idea

The problems of this lesson revolve around one quantity: **pressure is the force perpendicular to a surface divided by the area**. In a liquid, pressure comes from the weight of the liquid above, so it increases with depth. In a gas, it comes from the collisions of the particles with the walls of the container, so it depends on the amount, the volume and the temperature of the gas. When the pressure of a gas pushes a piston, the gas does work, and in this way a heat engine turns part of the heat into work.

The gas problems of the exam need two checks before the numbers. **The temperature in kelvins**, because the gas laws are proportionalities that start from absolute zero. **The total pressure**, because a pressure gauge usually shows only the gauge pressure, and the particles of the gas produce the whole pressure.

<svg data-fig="kartta" viewBox="0 0 380 596" role="img" aria-label="Concept map. At the top the node pressure: p = F / A. Three branches go down from it. Liquid: pressure at depth p = p0 + ρ g h, gauge pressure ρ g h and total pressure, which is the air pressure and the gauge pressure together. Gas: the ideal gas law p V = n R T, the combined gas law p V / T = constant and the kelvin temperature T = θ + 273.15 K. Heat engine: work done by a gas W = p ΔV, the first law of thermodynamics ΔU = Q + W and efficiency eta = W / Q1." style="max-width:min(100%,440px);font-size:21px">
  <line x1="24" y1="80" x2="24" y2="454" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="142.5" y="16.5" width="95" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\text{pressure}$</div></foreignObject>
  <foreignObject x="158.5" y="46.5" width="63" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$p = F/A$</div></foreignObject>
  <line x1="24" y1="122" x2="44" y2="122" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="100" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="109.5" width="84" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\textbf{liquid}$</div></foreignObject>
  <line x1="54" y1="142" x2="362" y2="142" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="153.5" width="95" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$p = p_0 + \rho g h$</div></foreignObject>
  <foreignObject x="292" y="156" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{at depth}$</div></foreignObject>
  <foreignObject x="58" y="187.5" width="74" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\Delta p = \rho g h$</div></foreignObject>
  <foreignObject x="239" y="190" width="123" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{gauge pressure}$</div></foreignObject>
  <foreignObject x="58" y="221.5" width="84" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$p = p_0 + \Delta p$</div></foreignObject>
  <foreignObject x="239" y="224" width="123" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{total pressure}$</div></foreignObject>
  <line x1="24" y1="288" x2="44" y2="288" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="266" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="275.5" width="52" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\textbf{gas}$</div></foreignObject>
  <line x1="54" y1="308" x2="362" y2="308" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="319.5" width="74" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$pV = nRT$</div></foreignObject>
  <foreignObject x="257" y="322" width="105" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{ideal gas law}$</div></foreignObject>
  <foreignObject x="58" y="353.5" width="150" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$pV/T = \text{constant}$</div></foreignObject>
  <foreignObject x="292" y="356" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{same gas}$</div></foreignObject>
  <foreignObject x="58" y="387.5" width="139" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$T = \theta + 273.15\,\text{K}$</div></foreignObject>
  <foreignObject x="292" y="390" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{kelvins}$</div></foreignObject>
  <line x1="24" y1="454" x2="44" y2="454" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="432" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="441.5" width="128" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\textbf{heat engine}$</div></foreignObject>
  <line x1="54" y1="474" x2="362" y2="474" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="485.5" width="74" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$W = p\,\Delta V$</div></foreignObject>
  <foreignObject x="239" y="488" width="123" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{work done by gas}$</div></foreignObject>
  <foreignObject x="58" y="519.5" width="74" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\Delta U = Q + W$</div></foreignObject>
  <foreignObject x="283" y="522" width="79" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{first law}$</div></foreignObject>
  <foreignObject x="58" y="553.5" width="74" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\eta = W/Q_1$</div></foreignObject>
  <foreignObject x="266" y="556" width="96" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{efficiency}$</div></foreignObject>
</svg>

The opening question is answered with these two checks. In the warm garage ($+20\,{}^\circ\text{C}$) the gauge showed a gauge pressure of $230\,\text{kPa}$, so the total pressure was $101\,\text{kPa} + 230\,\text{kPa} = 331\,\text{kPa}$. When the volume of the tyre stays almost the same, the total pressure is proportional to the kelvin temperature: after a night of frost ($-20\,{}^\circ\text{C}$) it is $331\,\text{kPa} \cdot 253\,\text{K} : 293\,\text{K} \approx 286\,\text{kPa}$. The gauge now shows only about $185\,\text{kPa}$, even though no air has leaked.

<svg data-fig="rengas" viewBox="0 0 480 330" role="img" aria-label="Bar chart to scale: the total pressure of the air in a tyre at two temperatures. Each horizontal bar is divided into two parts: the air pressure 101 kPa and the gauge pressure shown by the gauge. In the warm garage, +20 °C, the gauge pressure is 230 kPa and the total pressure 331 kPa. After a night of frost, −20 °C, the total pressure is 286 kPa and the gauge pressure 185 kPa. The total pressure has decreased in the ratio of the kelvin temperatures, but the gauge reading has decreased by 45 kPa, that is, by about a fifth." style="max-width:100%;font-size:20px">
  <line x1="140" y1="40" x2="140" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="40" x2="240" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="40" x2="340" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="50" y="26" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#c92a2a">$+20\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="40" y="60" width="101" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="141" y="60" width="230" height="46" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="76" y="71" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_0$</div></foreignObject>
  <foreignObject x="221" y="71" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\Delta p = 230$</div></foreignObject>
  <foreignObject x="379" y="71" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$331\,\text{kPa}$</div></foreignObject>
  <foreignObject x="50" y="138" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$-20\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="40" y="172" width="101" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="141" y="172" width="185" height="46" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="76" y="183" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_0$</div></foreignObject>
  <foreignObject x="198.5" y="183" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\Delta p = 185$</div></foreignObject>
  <foreignObject x="334" y="183" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$286\,\text{kPa}$</div></foreignObject>
  <line x1="39" y1="268" x2="392" y2="268" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M404,268 L391,274 L391,262 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="40" y1="269" x2="40" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="140" y1="268" x2="140" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="120.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$100$</div></foreignObject>
  <line x1="240" y1="268" x2="240" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$200$</div></foreignObject>
  <line x1="340" y1="268" x2="340" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="320.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$300$</div></foreignObject>
  <foreignObject x="16" y="280" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="410" y="256" width="74" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$p\ (\text{kPa})$</div></foreignObject>
</svg>

## Formula: Pressure, gases and the heat engine

### Pressure and pressure in a liquid

```kaavat
pressure caused by a force :: p = \frac{F}{A}
```

where $p$ is the pressure (Pa), $F$ the force perpendicular to the surface (N) and $A$ the area (m²). In a liquid at rest, at the depth $h$

```kaavat
hydrostatic pressure :: p = \rho g h
```

where $\rho$ is the density of the liquid (kg/m³) and $g = 9.81\,\text{m/s}^2$. The hydrostatic pressure is the gauge pressure, and it depends only on the depth and the density, not on the shape of the container. The total pressure at the depth $h$ is $p_0 + \rho g h$, where $p_0$ is the pressure at the surface, usually the air pressure of about $101\,\text{kPa}$. The force caused by pressure is always perpendicular to the surface.

### The state of a gas

```kaavat
ideal gas law :: pV = nRT
```

where $V$ is the volume (m³), $n$ the amount of substance (mol), $R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ and $T$ the temperature in kelvins. The amount of substance is obtained from the mass, $n = m/M$, where $M$ is the molar mass. The equation holds for a dilute gas, when the pressure is not very high and the temperature not very low. When the amount of gas stays the same,

```kaavat
combined gas law (constant amount of gas) :: \frac{pV}{T} = \text{constant}
```

that is, for two states $\tfrac{p_1 V_1}{T_1} = \tfrac{p_2 V_2}{T_2}$. From it follow the special cases: at constant temperature Boyle's law $p_1V_1 = p_2V_2$, at constant pressure $V \propto T$ and at constant volume $p \propto T$. The kelvin temperature is

```latex
T = \theta + 273.15\,\text{K}
```

where $\theta$ is the numerical value of the Celsius temperature. In an experiment, absolute zero is obtained by extending the $(\theta, p)$ or $(\theta, V)$ line to zero. It is a prediction of the model: a real gas condenses into a liquid before that.

### Work done by a gas and the heat engine

A gas expanding at constant pressure does work, and work is done on a compressed gas:

```kaavat
work done by an expanding gas / on a compressed gas :: W = p\Delta V
```

where $\Delta V$ is the magnitude of the change in volume (m³); the work is the area under the ($V$, $p$) graph. By the first law of thermodynamics the internal energy of the gas changes by

```kaavat
first law of thermodynamics :: \Delta U = Q + W
```

where $Q$ is the heat transferred to the gas (J) and $W$ the work done on the gas (J). In a compression $W = p\Delta V$ is positive. An expanding gas itself does the work $p\Delta V$, so then $W = -p\Delta V$ and the internal energy decreases by this amount.

In one cycle a heat engine takes the heat $Q_1$ ($\text{J}$) from a hot source, does the work $W$ ($\text{J}$) and gives the heat $Q_2$ ($\text{J}$) to a colder environment. At the end of the cycle the gas of the engine is in the same state as at the start. The efficiency of the engine is

```kaavat
efficiency of a heat engine :: \eta = \frac{W}{Q_1}
```

Part of the heat must always be given to a colder place, so the efficiency of a heat engine stays well below $100\,\%$. The smaller the temperature difference $T_1 - T_2$ is compared with the temperature $T_1$ of the hot source, the smaller the share of the heat the engine can turn into work. In a power plant the same is calculated from powers: the electrical power divided by the fuel power.

<svg data-fig="kone" viewBox="0 0 420 470" role="img" aria-label="Energy flows of a heat engine during one cycle, arrow widths to scale. At the top the hot source, whose temperature is T1. From it a wide heat arrow Q1 = 1000 J comes down into the engine. From the engine a narrow green arrow, the work W = 350 J, goes to the right, and a heat arrow Q2 = 650 J goes down to the colder environment, whose temperature is T2. The outgoing arrows together are as wide as the incoming arrow." style="max-width:100%;font-size:20px">
  <rect x="16" y="12" width="388" height="62" rx="12" fill="#f2a69c" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="149" y="31" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{hot source } T_1$</div></foreignObject>
  <path d="M100,74 L100,172 L87,172 L150,196 L213,172 L200,172 L200,74 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="222" y="120" width="102" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#e8590c">$Q_1 = 1000\,\text{J}$</div></foreignObject>
  <rect x="80" y="196" width="140" height="84" rx="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="115" y="226" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{engine}$</div></foreignObject>
  <path d="M100,280 L100,368 L87,368 L132.5,392 L178,368 L165,368 L165,280 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="187" y="328" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#e8590c">$Q_2 = 650\,\text{J}$</div></foreignObject>
  <path d="M220,255.5 L308,255.5 L308,266.5 L330,238 L308,209.5 L308,220.5 L220,220.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="230" y="188" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#2b8a3e">$W = 350\,\text{J}$</div></foreignObject>
  <rect x="16" y="394" width="388" height="62" rx="12" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5"/>
  <foreignObject x="107" y="413" width="206" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{colder environment } T_2$</div></foreignObject>
</svg>

```johda
In one cycle a heat engine takes the heat $Q_1$ from a hot source and gives the heat $Q_2$ to a colder environment. Derive the work $W$ done by the engine in one cycle in terms of the heats $Q_1$ and $Q_2$.
---
Apply the first law of thermodynamics $\Delta U = Q + W$ to the gas of the engine over one cycle. At the end of the cycle the gas is in the same state as at the start, so its internal energy does not change: $\Delta U = 0$.

In one cycle the heat $Q_1$ comes into the gas and the heat $Q_2$ leaves it. The heat transferred to the gas is therefore

$$Q = Q_1 - Q_2$$

In the first law $W$ is the work done on the gas. The engine itself does the work $W$ on its surroundings, so the work done on the gas is $-W$, just as in an expansion it is $-p\Delta V$. Substitute into the first law:

$$0 = (Q_1 - Q_2) + (-W)$$

Solve for the work of the engine:

$$W = Q_1 - Q_2$$

The result is the conservation of energy: in the figure the incoming heat $Q_1$ divides into the work $W$ and the heat given out $Q_2$.
```

## Common mistakes {Virheet}

- **Degrees Celsius in a ratio.** The pressure of a gas heated from $20\,{}^\circ\text{C}$ to $40\,{}^\circ\text{C}$ increases by only about $7\,\%$, it does not double: $313\,\text{K} : 293\,\text{K} \approx 1.07$.
- **Gauge pressure in a gas law.** The gauge reading is not the pressure of the gas. Add the air pressure before calculating and subtract it only at the end, if the gauge reading is asked for.
- **Units mixed up.** In the ideal gas law the pressure is in pascals and the volume in cubic metres. Kilopascals and litres work together, because $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$, but kilopascals and cubic metres give an error of a factor of a thousand.
- **Pressure and force mixed up.** The same force on a small area gives a large pressure. Force is obtained from pressure only by multiplying by the area.
- **Suction pulls.** A suction cup or a straw does not pull anything: the pressure of the outside air pushes when the pressure inside is lower.
- **A heat engine could turn all the heat into work.** Removing friction does not help: the heat $Q_2$ cannot be avoided.

## Review if needed {Kertaa}

- Pressure, gauge pressure and pressure at depth: [*Pressure and hydrostatic pressure*](fy3-4.html).
- Boyle's law and the changes of state of gases: [*Changes of state of a gas and Boyle's law*](fy3-9.html). Amount of substance and the ideal gas law: [*Ideal gas law*](fy3-10.html).
- Extending a line to zero and its uncertainty: [*Determining absolute zero*](fy3-13.html).
- Work done by a gas, the heat engine and the heat pump: [*Work done by a gas and the heat engine*](fy3-11.html). The efficiency of a power plant: [*Energy production and the efficiency of power plants*](fy3-15.html).
