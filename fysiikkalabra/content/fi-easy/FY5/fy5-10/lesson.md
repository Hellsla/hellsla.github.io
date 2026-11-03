# Mekaaninen aaltoliike

> **Miksi** tolpassa roikkuva kello kilahtaa, kun pitkän narun toista päätä heilautetaan kerran, vaikka kukaan ei koske kelloon?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kesämökin piha järven rannalla. Vasemmalla tyttö pitelee pitkän narun päätä. Hän on juuri heilauttanut narua kerran. Narun toinen pää on sidottu puutolppaan. Tolpan varresta roikkuu messinkinen kello. Kireän narun keskivaiheilla on yksi kumpu. Kumpu on matkalla kohti tolppaa. Taustalla ovat järvi, metsäinen ranta, punainen mökki, sauna ja koivuja." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy510h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy510h-lake" gradientUnits="userSpaceOnUse" x1="0" y1="290" x2="0" y2="350"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy510h-grass" gradientUnits="userSpaceOnUse" x1="0" y1="340" x2="0" y2="600"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy510h-post" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy510h-bell" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#b8622d"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy510h-sky)"/>
  <path d="M182.5,95 Q181,69.5 211,72.5 Q223,45.5 253,54.5 Q280,39.5 295,68 Q322,71 319,95 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M715,66 Q714,49 734,51 Q742,33 762,39 Q780,29 790,48 Q808,50 806,66 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M1026,132 Q1025,111.5 1049,114 Q1058.5,92.5 1082.5,99.5 Q1104,87.5 1116,110.5 Q1137.5,113 1135,132 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,268 L9,249 L17.5,268 L27,246.5 L36.5,268 L46,247.5 L55,268 L69.5,232 L83.5,268 L93.5,245.5 L103,268 L113,246 L122.5,268 L136,235 L149.5,268 L164.5,229.5 L179.5,268 L192.5,235 L206,268 L221.5,228.5 L237,268 L251.5,231 L266,268 L278.5,238.5 L290.5,268 L305.5,229.5 L320.5,268 L333,238.5 L345,268 L355.5,243 L366.5,268 L379.5,235 L393,268 L405.5,238 L417.5,268 L429.5,239.5 L441,268 L450,249 L458.5,268 L473.5,230 L488.5,268 L503.5,229.5 L518.5,268 L531.5,236.5 L544.5,268 L558.5,233 L572.5,268 L585,236.5 L598,268 L612,233 L626,268 L640.5,232 L654.5,268 L665.5,243 L676,268 L685.5,246 L695.5,268 L710.5,229 L725.5,268 L741,228 L756.5,268 L770,235.5 L783,268 L798,229.5 L813,268 L826,237 L838.5,268 L851.5,235 L865,268 L878,236 L891,268 L901,245 L911,268 L925,233 L939,268 L953.5,231 L968.5,268 L983.5,229 L999,268 L1009,244 L1019.5,268 L1028,249 L1037,268 L1051.5,231 L1066,268 L1078,240 L1089.5,268 L1098.5,248 L1107.5,268 L1117.5,245 L1127.5,268 L1142.5,230.5 L1157.5,268 L1171,233.5 L1185,268 L1194,248.5 L1202.5,268 V280 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M0,282 L7,268 L14.5,282 L22,267.5 L29,282 L38.5,262.5 L47.5,282 L56.5,263 L65.5,282 L78,253 L91,282 L101,259.5 L111.5,282 L122,259 L132,282 L142.5,259 L153,282 L163.5,259 L174,282 L184.5,259 L194.5,282 L204,262.5 L213,282 L225.5,253.5 L238,282 L250,255 L262,282 L270,265 L278.5,282 L290,256 L301.5,282 L312.5,257.5 L323.5,282 L336,252.5 L349,282 L358.5,261 L368,282 L381,253 L393.5,282 L403.5,260 L413.5,282 L423.5,260 L433.5,282 L443.5,260.5 L453.5,282 L461.5,267 L469,282 L476.5,267 L484,282 L493.5,261.5 L503,282 L515,254 L527.5,282 L538,259 L548,282 L556,266 L564,282 L574.5,259.5 L584.5,282 L596,256 L608,282 L615,268.5 L622,282 L632.5,258 L643.5,282 L650.5,268 L658,282 L667.5,262 L676.5,282 L685,265.5 L693,282 L704.5,256.5 L715.5,282 L727,256.5 L738.5,282 L750.5,255 L762,282 L772,261 L781.5,282 L791.5,261.5 L801,282 L810.5,261.5 L820,282 L829.5,261.5 L839,282 L846.5,267 L854.5,282 L864.5,260 L874.5,282 L884,260.5 L894,282 L907,253 L919.5,282 L928,264.5 L936.5,282 L949,252.5 L962,282 L973,258 L984,282 L995.5,256 L1007,282 L1017.5,258 L1028.5,282 L1038,262 L1047.5,282 L1057,261.5 L1066.5,282 L1074.5,266.5 L1082,282 L1091.5,262 L1100.5,282 L1111.5,258 L1122.5,282 L1135,253.5 L1147,282 L1158,258 L1169,282 L1177,265 L1185.5,282 L1198,253.5 L1210,282 V292 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="290" width="1200" height="60" fill="url(#fy510h-lake)"/>
  <line x1="120" y1="306" x2="210" y2="306" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  <line x1="420" y1="318" x2="490" y2="318" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  <line x1="700" y1="304" x2="810" y2="304" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  <line x1="980" y1="322" x2="1060" y2="322" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  <line x1="560" y1="334" x2="620" y2="334" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  <path d="M0,352 Q300,336 620,346 T1200,340 V600 H0 Z" fill="url(#fy510h-grass)" stroke-linejoin="round"/>
  <path d="M0,600 Q240,520 520,500 T1200,470 V510 Q820,520 560,546 T120,600 Z" fill="#f1dfb5" stroke-linejoin="round"/>
  <rect x="760" y="294" width="220" height="88" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="774" y1="297" x2="774" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="788" y1="297" x2="788" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="802" y1="297" x2="802" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="816" y1="297" x2="816" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="830" y1="297" x2="830" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="844" y1="297" x2="844" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="858" y1="297" x2="858" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="872" y1="297" x2="872" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="886" y1="297" x2="886" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="900" y1="297" x2="900" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="914" y1="297" x2="914" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="928" y1="297" x2="928" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="942" y1="297" x2="942" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="956" y1="297" x2="956" y2="379" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="760" y="294" width="10" height="88" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="970" y="294" width="10" height="88" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M740,294 L870,245.5 L1000,294 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="790" y="318.5" width="40" height="35" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="790" y="318.5" width="40" height="35" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="810" y1="318.5" x2="810" y2="354" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="860" y="318.5" width="40" height="35" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="860" y="318.5" width="40" height="35" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="880" y1="318.5" x2="880" y2="354" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="330" y="312" width="110" height="56" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="344" y1="315" x2="344" y2="365" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="358" y1="315" x2="358" y2="365" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="372" y1="315" x2="372" y2="365" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="386" y1="315" x2="386" y2="365" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="400" y1="315" x2="400" y2="365" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="414" y1="315" x2="414" y2="365" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="330" y="312" width="10" height="56" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="430" y="312" width="10" height="56" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M310,312 L385,281 L460,312 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="360" y="327.5" width="40" height="22.5" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="360" y="327.5" width="40" height="22.5" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="380" y1="327.5" x2="380" y2="350" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="685" y="373.5" width="9.5" height="14.5" fill="#b8622d"/>
  <path d="M647,376 L690,328 L733,376 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M690,328 L733,376 H690 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M656.5,349.5 L690,301.5 L723.5,349.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M690,301.5 L723.5,349.5 H690 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M666,323 L690,268 L714,323 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M690,268 L714,323 H690 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1165" y="361.5" width="9.5" height="14.5" fill="#b8622d"/>
  <path d="M1127,364 L1170,316 L1213,364 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1170,316 L1213,364 H1170 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1136.5,337.5 L1170,289.5 L1203.5,337.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1170,289.5 L1203.5,337.5 H1170 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1146,311 L1170,256 L1194,311 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1170,256 L1194,311 H1170 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="466.5" y="361" width="7" height="11" fill="#b8622d"/>
  <path d="M437.5,363 L470,327 L502.5,363 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M470,327 L502.5,363 H470 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M445,343 L470,307 L495,343 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M470,307 L495,343 H470 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M452,323.5 L470,282 L488,323.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M470,282 L488,323.5 H470 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1105.5" y="234" width="9" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1105.5" y="366" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1110" y="348" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1105.5" y="330" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1110" y="312" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1105.5" y="294" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1110" y="276" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1105.5" y="258" width="4.5" height="2" fill="#1f2933"/>
  <line x1="1110" y1="291" x2="1083" y2="273" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1110" y1="271.5" x2="1137" y2="253.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1110" y1="256.5" x2="1083" y2="238.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1110" cy="241.5" r="30" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1087.5" cy="264" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1132.5" cy="261" r="25.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1110" cy="276" r="22.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="62.5" y="180" width="15" height="250" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="62.5" y="400" width="7.5" height="4" fill="#1f2933"/>
  <rect x="70" y="370" width="7.5" height="4" fill="#1f2933"/>
  <rect x="62.5" y="340" width="7.5" height="4" fill="#1f2933"/>
  <rect x="70" y="310" width="7.5" height="4" fill="#1f2933"/>
  <rect x="62.5" y="280" width="7.5" height="4" fill="#1f2933"/>
  <rect x="70" y="250" width="7.5" height="4" fill="#1f2933"/>
  <rect x="62.5" y="220" width="7.5" height="4" fill="#1f2933"/>
  <line x1="70" y1="275" x2="25" y2="245" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="70" y1="242.5" x2="115" y2="212.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="70" y1="217.5" x2="25" y2="187.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="70" cy="192.5" r="50" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="32.5" cy="230" r="40" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="107.5" cy="225" r="42.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="70" cy="250" r="37.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <ellipse cx="1000" cy="552" rx="34" ry="7" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="987" y="324" width="26" height="224" rx="3" fill="url(#fy510h-post)" stroke="#1f2933" stroke-width="3"/>
  <rect x="987" y="318" width="90" height="18" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="3"/>
  <path d="M1013,366 L1046,336" fill="none" stroke="#a97a35" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="1058" y1="336" x2="1058" y2="346" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M1041,384 Q1040,348 1058,346 Q1076,348 1075,384 L1082,394 H1034 Z" fill="url(#fy510h-bell)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="1058" cy="400" r="6" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="200" cy="564" rx="50" ry="9" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M200,488.5 L188.5,559" fill="none" stroke="#1971c2" stroke-width="13.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M179.5,562 h20" fill="none" stroke="#6c757d" stroke-width="7.36" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M203.5,426 L292,446" fill="none" stroke="#e8590c" stroke-width="11.04" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M186.5,415 Q221,401 215.5,442.5 L211,493 H183.5 Z" fill="#e8590c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M200,488.5 L211.5,559" fill="none" stroke="#1971c2" stroke-width="13.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M219,562 h20" fill="none" stroke="#6c757d" stroke-width="7.36" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M206,424 L292,446" fill="none" stroke="#e8590c" stroke-width="11.04" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="292" cy="446" r="5.98" fill="#f1dfb5"/>
  <rect x="202" y="396.5" width="9" height="14" fill="#f1dfb5"/>
  <circle cx="207" cy="384.5" r="15.64" fill="#f1dfb5"/>
  <path d="M191,387 Q190,367 207.5,368 Q222.5,369 222.5,380 Q207,376 191,387 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M292,446 L296,446 L300,446 L304,446 L308,446 L312,446 L316,446.5 L320,446.5 L324,446.5 L328,446.5 L332,446.5 L336,446.5 L340,446.5 L344,446.5 L348,446.5 L352,446.5 L356,446.5 L360,446.5 L364,447 L368,447 L372,447 L376,447 L380,447 L384,447 L388,447 L392,447 L396,447 L400,447 L404,447 L408,447 L412,447 L416,447 L420,447.5 L424,447.5 L428,447.5 L432,447.5 L436,447.5 L440,447.5 L444,447.5 L448,447.5 L452,447.5 L456,447.5 L460,447.5 L464,447.5 L468,447.5 L472,447.5 L476,447.5 L480,447.5 L484,447.5 L488,447.5 L492,447.5 L496,447.5 L500,447 L504,447 L508,447 L512,446.5 L516,446 L520,445.5 L524,445 L528,444.5 L532,443.5 L536,442.5 L540,441 L544,439.5 L548,437.5 L552,435.5 L556,433 L560,430.5 L564,427.5 L568,424 L572,420.5 L576,416.5 L580,412.5 L584,408 L588,403.5 L592,399.5 L596,395 L600,390.5 L604,387 L608,383 L612,380 L616,377.5 L620,375.5 L624,374 L628,373 L632,373 L636,374 L640,375 L644,377 L648,379.5 L652,383 L656,386.5 L660,390 L664,394 L668,398.5 L672,403 L676,407 L680,411.5 L684,415.5 L688,419 L692,422.5 L696,426 L700,429 L704,431.5 L708,434 L712,436 L716,437.5 L720,439 L724,440.5 L728,441.5 L732,442 L736,443 L740,443.5 L744,443.5 L748,444 L752,444 L756,444.5 L760,444.5 L764,444.5 L768,444.5 L772,444.5 L776,444.5 L780,444.5 L784,444 L788,444 L792,444 L796,444 L800,444 L804,444 L808,443.5 L812,443.5 L816,443.5 L820,443.5 L824,443 L828,443 L832,443 L836,443 L840,443 L844,442.5 L848,442.5 L852,442.5 L856,442.5 L860,442 L864,442 L868,442 L872,442 L876,441.5 L880,441.5 L884,441.5 L888,441.5 L892,441 L896,441 L900,441 L904,441 L908,440.5 L912,440.5 L916,440.5 L920,440.5 L924,440 L928,440 L932,440 L936,439.5 L940,439.5 L944,439.5 L948,439.5 L952,439 L956,439 L960,439 L964,439 L968,438.5 L972,438.5 L976,438.5 L980,438 L984,438" fill="none" stroke="#1f2933" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M292,446 L296,446 L300,446 L304,446 L308,446 L312,446 L316,446.5 L320,446.5 L324,446.5 L328,446.5 L332,446.5 L336,446.5 L340,446.5 L344,446.5 L348,446.5 L352,446.5 L356,446.5 L360,446.5 L364,447 L368,447 L372,447 L376,447 L380,447 L384,447 L388,447 L392,447 L396,447 L400,447 L404,447 L408,447 L412,447 L416,447 L420,447.5 L424,447.5 L428,447.5 L432,447.5 L436,447.5 L440,447.5 L444,447.5 L448,447.5 L452,447.5 L456,447.5 L460,447.5 L464,447.5 L468,447.5 L472,447.5 L476,447.5 L480,447.5 L484,447.5 L488,447.5 L492,447.5 L496,447.5 L500,447 L504,447 L508,447 L512,446.5 L516,446 L520,445.5 L524,445 L528,444.5 L532,443.5 L536,442.5 L540,441 L544,439.5 L548,437.5 L552,435.5 L556,433 L560,430.5 L564,427.5 L568,424 L572,420.5 L576,416.5 L580,412.5 L584,408 L588,403.5 L592,399.5 L596,395 L600,390.5 L604,387 L608,383 L612,380 L616,377.5 L620,375.5 L624,374 L628,373 L632,373 L636,374 L640,375 L644,377 L648,379.5 L652,383 L656,386.5 L660,390 L664,394 L668,398.5 L672,403 L676,407 L680,411.5 L684,415.5 L688,419 L692,422.5 L696,426 L700,429 L704,431.5 L708,434 L712,436 L716,437.5 L720,439 L724,440.5 L728,441.5 L732,442 L736,443 L740,443.5 L744,443.5 L748,444 L752,444 L756,444.5 L760,444.5 L764,444.5 L768,444.5 L772,444.5 L776,444.5 L780,444.5 L784,444 L788,444 L792,444 L796,444 L800,444 L804,444 L808,443.5 L812,443.5 L816,443.5 L820,443.5 L824,443 L828,443 L832,443 L836,443 L840,443 L844,442.5 L848,442.5 L852,442.5 L856,442.5 L860,442 L864,442 L868,442 L872,442 L876,441.5 L880,441.5 L884,441.5 L888,441.5 L892,441 L896,441 L900,441 L904,441 L908,440.5 L912,440.5 L916,440.5 L920,440.5 L924,440 L928,440 L932,440 L936,439.5 L940,439.5 L944,439.5 L948,439.5 L952,439 L956,439 L960,439 L964,439 L968,438.5 L972,438.5 L976,438.5 L980,438 L984,438" fill="none" stroke="#b8622d" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M985,429 h30 M985,447 h30" fill="none" stroke="#b8622d" stroke-width="5" stroke-linejoin="round"/>
  <circle cx="292" cy="446" r="11" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
</svg>

## Ydinajatus

### Aalto on etenevä häiriö
Heilautetaan narun päätä ylös. Käsi vetää mukanaan narun lähintä kohtaa. Jännittynyt naru vetää seuraavaa kohtaa, ja se vetää taas seuraavaa. Jokainen kohta lähtee liikkeelle vähän myöhemmin kuin edellinen. Siksi poikkeama tasapainoasemasta etenee narussa kädestä kauemmas. Tasapainoasema on paikka, jossa kohta on, kun naru on levossa. Poikkeamaa sanotaan häiriöksi. **Aaltoliike** on häiriön etenemistä väliaineessa. Väliaine on aine, jossa aalto kulkee. Väliaineen hiukkaset värähtelevät vain tasapainoasemansa ympärillä. Ne eivät kulje aallon mukana. Kaasun molekyylit liikkuvat lisäksi satunnaisesti lämpöliikkeen vuoksi, mutta aalto ei kuljeta niitä mukanaan. Aalto kuljettaa siis energiaa lähteestä kauemmas, mutta ei ainetta. Siksi narun päässä oleva kello voi kilahtaa. Mikään narun kohta ei silti kulje kädestä kelloon asti.

Mekaaninen aalto tarvitsee väliaineen. Väliaine voi olla esimerkiksi naru, jousi, vesi tai ilma. Yksi heilautus synnyttää **pulssin**. Pulssi on yksittäinen kumpu, joka etenee narussa. Kun kättä heilutetaan tasaisesti ylös ja alas, syntyy jaksollinen aalto. Siinä harjat ja pohjat toistuvat. Narun jokainen kohta värähtelee samalla taajuudella $f$ kuin käsi. Jaksonaika $T$, taajuus $f$ ja amplitudi $A$ tarkoittavat samaa kuin luvussa *Jaksollinen liike*. Kun aalto tulee narun päähän, se heijastuu takaisin. Heijastumista tarkastellaan luvussa *Aaltojen heijastuminen ja diffraktio*.

### Poikittainen ja pitkittäinen aalto
Aallot jaetaan kahteen lajiin. Jako riippuu siitä, mihin suuntaan väliaineen hiukkaset värähtelevät. **Poikittaisessa aallossa** hiukkaset värähtelevät kohtisuoraan aallon etenemissuuntaa vastaan. Esimerkiksi narun kohdat liikkuvat ylös ja alas, kun aalto etenee vaakasuoraan. **Pitkittäisessä aallossa** hiukkaset värähtelevät etenemissuunnan suuntaisesti. Työnnetään pitkän kierrejousen päätä edestakaisin. Jouseen syntyy tihentymiä, joissa kierrokset ovat lähellä toisiaan. Siihen syntyy myös harvennuksia, joissa kierrokset ovat kaukana toisistaan. Tihentymät ja harvennukset etenevät. Jokainen kierros vain heilahtelee paikkansa ympärillä. Esimerkiksi ääni ilmassa on pitkittäinen aalto.

<svg data-fig="types" viewBox="0 0 600 412" role="img" aria-label="Kaavakuva, ei mittakaavassa. Ylhäällä on poikittainen aalto. Naru on siniaallon muotoinen. Sininen nuoli osoittaa aallon etenemissuunnan oikealle. Kolmessa narun kohdassa on pystysuora kaksipäinen nuoli. Se näyttää, että kohta liikkuu ylös ja alas eli kohtisuoraan etenemissuuntaa vastaan. Alhaalla on pitkittäinen aalto. Pitkän kierrejousen kierrokset ovat paikoin tiheässä (tihentymä) ja paikoin harvassa (harvennus). Yhden kierroksen yllä on vaakasuora kaksipäinen nuoli. Se näyttää, että kierros liikkuu edestakaisin jousen suuntaisesti. Sininen nuoli osoittaa tämänkin aallon etenemissuunnan oikealle." style="max-width:100%;font-size:24px">
  <foreignObject x="24" y="9.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{poikittainen aalto}$</div></foreignObject>
  <line x1="440" y1="24" x2="545" y2="24" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M560,24 L544,31 L544,17 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="412" y="9.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <line x1="60" y1="112" x2="580" y2="112" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M60,112 L63,108 L66,104.5 L69,101 L72,97.5 L75,94 L78,90.5 L81,87.5 L84,84.5 L87,82 L90,79.5 L93,77.5 L96,76 L99,74.5 L102,73.5 L105,72.5 L108,72 L111,72 L114,72.5 L117,73 L120,74 L123,75.5 L126,77 L129,79 L132,81 L135,83.5 L138,86.5 L141,89.5 L144,92.5 L147,96 L150,99.5 L153,103.5 L156,107 L159,110.5 L162,114.5 L165,118.5 L168,122 L171,125.5 L174,129 L177,132.5 L180,135.5 L183,138.5 L186,141 L189,143.5 L192,146 L195,147.5 L198,149 L201,150.5 L204,151.5 L207,152 L210,152 L213,152 L216,151.5 L219,150.5 L222,149 L225,147.5 L228,146 L231,143.5 L234,141 L237,138.5 L240,135.5 L243,132.5 L246,129 L249,125.5 L252,122 L255,118.5 L258,114.5 L261,110.5 L264,107 L267,103.5 L270,99.5 L273,96 L276,92.5 L279,89.5 L282,86.5 L285,83.5 L288,81 L291,79 L294,77 L297,75.5 L300,74 L303,73 L306,72.5 L309,72 L312,72 L315,72.5 L318,73.5 L321,74.5 L324,76 L327,77.5 L330,79.5 L333,82 L336,84.5 L339,87.5 L342,90.5 L345,94 L348,97.5 L351,101 L354,104.5 L357,108 L360,112 L363,116 L366,119.5 L369,123 L372,126.5 L375,130 L378,133.5 L381,136.5 L384,139.5 L387,142 L390,144.5 L393,146.5 L396,148 L399,149.5 L402,150.5 L405,151.5 L408,152 L411,152 L414,151.5 L417,151 L420,150 L423,148.5 L426,147 L429,145 L432,143 L435,140.5 L438,137.5 L441,134.5 L444,131.5 L447,128 L450,124.5 L453,120.5 L456,117 L459,113.5 L462,109.5 L465,105.5 L468,102 L471,98.5 L474,95 L477,91.5 L480,88.5 L483,85.5 L486,83 L489,80.5 L492,78 L495,76.5 L498,75 L501,73.5 L504,72.5 L507,72 L510,72 L513,72 L516,72.5 L519,73.5 L522,75 L525,76.5 L528,78 L531,80.5 L534,83 L537,85.5 L540,88.5 L543,91.5 L546,95 L549,98.5 L552,102 L555,105.5 L558,109.5 L561,113.5 L564,117 L567,120.5 L570,124.5 L573,128 L576,131.5" fill="none" stroke="#a97a35" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="60" cy="112" r="3.5" fill="#1f2933"/>
  <circle cx="85" cy="83.5" r="3.5" fill="#1f2933"/>
  <circle cx="110" cy="72" r="3.5" fill="#1f2933"/>
  <circle cx="135" cy="83.5" r="3.5" fill="#1f2933"/>
  <circle cx="160" cy="112" r="3.5" fill="#1f2933"/>
  <circle cx="185" cy="140.5" r="3.5" fill="#1f2933"/>
  <circle cx="210" cy="152" r="3.5" fill="#1f2933"/>
  <circle cx="235" cy="140.5" r="3.5" fill="#1f2933"/>
  <circle cx="260" cy="112" r="3.5" fill="#1f2933"/>
  <circle cx="285" cy="83.5" r="3.5" fill="#1f2933"/>
  <circle cx="310" cy="72" r="3.5" fill="#1f2933"/>
  <circle cx="335" cy="83.5" r="3.5" fill="#1f2933"/>
  <circle cx="360" cy="112" r="3.5" fill="#1f2933"/>
  <circle cx="385" cy="140.5" r="3.5" fill="#1f2933"/>
  <circle cx="410" cy="152" r="3.5" fill="#1f2933"/>
  <circle cx="435" cy="140.5" r="3.5" fill="#1f2933"/>
  <circle cx="460" cy="112" r="3.5" fill="#1f2933"/>
  <circle cx="485" cy="83.5" r="3.5" fill="#1f2933"/>
  <circle cx="510" cy="72" r="3.5" fill="#1f2933"/>
  <circle cx="535" cy="83.5" r="3.5" fill="#1f2933"/>
  <circle cx="560" cy="112" r="3.5" fill="#1f2933"/>
  <line x1="110" y1="112" x2="110" y2="73" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,62 L115.5,74 L104.5,74 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="112" x2="110" y2="151" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,162 L104.5,150 L115.5,150 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="260" y1="112" x2="260" y2="73" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M260,62 L265.5,74 L254.5,74 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="260" y1="112" x2="260" y2="151" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M260,162 L254.5,150 L265.5,150 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="410" y1="112" x2="410" y2="73" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M410,62 L415.5,74 L404.5,74 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="410" y1="112" x2="410" y2="151" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M410,162 L404.5,150 L415.5,150 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="37.5" y="169.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kohdan liike}$</div></foreignObject>
  <line x1="12" y1="208" x2="588" y2="208" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="24" y="211.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{pitkittäinen aalto}$</div></foreignObject>
  <line x1="440" y1="226" x2="545" y2="226" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M560,226 L544,233 L544,219 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="412" y="211.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <line x1="54" y1="304" x2="572" y2="304" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="60" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="82.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="103" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="121" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="135" cy="304" rx="5" ry="30" fill="none" stroke="#1f2933" stroke-width="3"/>
  <ellipse cx="146.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="155" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="162.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="170.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="180.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="194" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="210.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="230.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="252.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="275" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="296.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="315" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="331" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="343" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="352.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="360" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="367.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="377" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="389" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="405" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="423.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="445" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="467.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="489.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="509.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="526" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="539.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="549.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <ellipse cx="557.5" cy="304" rx="5" ry="30" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <line x1="135" y1="262" x2="124" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M113,262 L125,256.5 L125,267.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="135" y1="262" x2="146" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M157,262 L145,267.5 L145,256.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="165" y="247.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kierroksen liike}$</div></foreignObject>
  <foreignObject x="100" y="339.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymä}$</div></foreignObject>
  <foreignObject x="300" y="339.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymä}$</div></foreignObject>
  <foreignObject x="200" y="369.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{harvennus}$</div></foreignObject>
  <foreignObject x="400" y="369.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{harvennus}$</div></foreignObject>
</svg>

## Kaava: Aaltoliikkeen perusyhtälö
**Aallonpituus** $\lambda$ on kahden peräkkäisen harjan välinen etäisyys. Se on myös kahden peräkkäisen tihentymän välinen etäisyys. Se on lyhin etäisyys kahden sellaisen kohdan välillä, jotka liikkuvat täsmälleen samalla tavalla. Lähde tekee yhden täyden värähdyksen yhden jaksonajan $T$ aikana. Silloin aalto etenee tasan yhden aallonpituuden. Kuvan neljä hetkeä näyttävät asian. Jokainen jaksonajan neljännes vie aaltoa neljäsosan aallonpituudesta eteenpäin.

<svg data-fig="birth" viewBox="0 0 600 420" role="img" aria-label="Kaavakuva: narun pää alkaa heilua ylös ja alas. Narusta on piirretty neljä kuvaa allekkain. Hetket ovat neljäsosa jaksonajasta, puolet, kolme neljäsosaa ja koko jaksonaika. Katkoviiva näyttää, mihin asti aalto on kunakin hetkenä edennyt. Matkat ovat neljäsosa aallonpituudesta, puolet, kolme neljäsosaa ja koko aallonpituus. Alimman kuvan alla mittajana näyttää, että yhden jaksonajan aikana aalto on edennyt yhden aallonpituuden. Rintaman takana naru on levossa." style="max-width:100%;font-size:24px">
  <foreignObject x="40" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{1}{4}T$</div></foreignObject>
  <line x1="200" y1="22" x2="200" y2="94" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M120,34 L123,34 L126,34 L129,34.5 L132,34.5 L135,35 L138,35.5 L141,36 L144,36.5 L147,37.5 L150,38 L153,39 L156,40 L159,40.5 L162,41.5 L165,43 L168,44 L171,45 L174,46.5 L177,47.5 L180,49 L183,50 L186,51.5 L189,53 L192,54 L195,55.5 L198,57 L201,58 L204,58 L207,58 L210,58 L213,58 L216,58 L219,58 L222,58 L225,58 L228,58 L231,58 L234,58 L237,58 L240,58 L243,58 L246,58 L249,58 L252,58 L255,58 L258,58 L261,58 L264,58 L267,58 L270,58 L273,58 L276,58 L279,58 L282,58 L285,58 L288,58 L291,58 L294,58 L297,58 L300,58 L303,58 L306,58 L309,58 L312,58 L315,58 L318,58 L321,58 L324,58 L327,58 L330,58 L333,58 L336,58 L339,58 L342,58 L345,58 L348,58 L351,58 L354,58 L357,58 L360,58 L363,58 L366,58 L369,58 L372,58 L375,58 L378,58 L381,58 L384,58 L387,58 L390,58 L393,58 L396,58 L399,58 L402,58 L405,58 L408,58 L411,58 L414,58 L417,58 L420,58 L423,58 L426,58 L429,58 L432,58 L435,58 L438,58 L441,58 L444,58 L447,58 L450,58 L453,58 L456,58 L459,58 L462,58 L465,58 L468,58 L471,58 L474,58 L477,58 L480,58 L483,58 L486,58 L489,58 L492,58 L495,58 L498,58 L501,58 L504,58 L507,58 L510,58 L513,58 L516,58 L519,58 L522,58 L525,58 L528,58 L531,58 L534,58 L537,58 L540,58 L543,58 L546,58 L549,58 L552,58 L555,58 L558,58 L561,58 L564,58 L567,58 L570,58 L573,58 L576,58" fill="none" stroke="#a97a35" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="104" y="25" width="16" height="18" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="40" y="125.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{1}{2}T$</div></foreignObject>
  <line x1="280" y1="104" x2="280" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M120,140 L123,138.5 L126,137 L129,136 L132,134.5 L135,133 L138,131.5 L141,130.5 L144,129 L147,128 L150,126.5 L153,125.5 L156,124.5 L159,123.5 L162,122.5 L165,121.5 L168,120.5 L171,120 L174,119 L177,118.5 L180,118 L183,117.5 L186,117 L189,116.5 L192,116.5 L195,116 L198,116 L201,116 L204,116 L207,116 L210,116.5 L213,117 L216,117 L219,117.5 L222,118 L225,119 L228,119.5 L231,120.5 L234,121 L237,122 L240,123 L243,124 L246,125 L249,126.5 L252,127.5 L255,128.5 L258,130 L261,131.5 L264,132.5 L267,134 L270,135.5 L273,136.5 L276,138 L279,139.5 L282,140 L285,140 L288,140 L291,140 L294,140 L297,140 L300,140 L303,140 L306,140 L309,140 L312,140 L315,140 L318,140 L321,140 L324,140 L327,140 L330,140 L333,140 L336,140 L339,140 L342,140 L345,140 L348,140 L351,140 L354,140 L357,140 L360,140 L363,140 L366,140 L369,140 L372,140 L375,140 L378,140 L381,140 L384,140 L387,140 L390,140 L393,140 L396,140 L399,140 L402,140 L405,140 L408,140 L411,140 L414,140 L417,140 L420,140 L423,140 L426,140 L429,140 L432,140 L435,140 L438,140 L441,140 L444,140 L447,140 L450,140 L453,140 L456,140 L459,140 L462,140 L465,140 L468,140 L471,140 L474,140 L477,140 L480,140 L483,140 L486,140 L489,140 L492,140 L495,140 L498,140 L501,140 L504,140 L507,140 L510,140 L513,140 L516,140 L519,140 L522,140 L525,140 L528,140 L531,140 L534,140 L537,140 L540,140 L543,140 L546,140 L549,140 L552,140 L555,140 L558,140 L561,140 L564,140 L567,140 L570,140 L573,140 L576,140" fill="none" stroke="#a97a35" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="104" y="131" width="16" height="18" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="40" y="207.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{3}{4}T$</div></foreignObject>
  <line x1="360" y1="186" x2="360" y2="258" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M120,246 L123,246 L126,246 L129,245.5 L132,245.5 L135,245 L138,244.5 L141,244 L144,243.5 L147,242.5 L150,242 L153,241 L156,240 L159,239.5 L162,238.5 L165,237 L168,236 L171,235 L174,233.5 L177,232.5 L180,231 L183,230 L186,228.5 L189,227 L192,226 L195,224.5 L198,223 L201,221.5 L204,220 L207,218.5 L210,217.5 L213,216 L216,214.5 L219,213.5 L222,212 L225,210.5 L228,209.5 L231,208.5 L234,207 L237,206 L240,205 L243,204 L246,203 L249,202.5 L252,201.5 L255,201 L258,200 L261,199.5 L264,199 L267,199 L270,198.5 L273,198 L276,198 L279,198 L282,198 L285,198 L288,198.5 L291,198.5 L294,199 L297,199.5 L300,200 L303,200.5 L306,201 L309,202 L312,202.5 L315,203.5 L318,204.5 L321,205.5 L324,206.5 L327,207.5 L330,208.5 L333,210 L336,211 L339,212.5 L342,213.5 L345,215 L348,216.5 L351,218 L354,219 L357,220.5 L360,222 L363,222 L366,222 L369,222 L372,222 L375,222 L378,222 L381,222 L384,222 L387,222 L390,222 L393,222 L396,222 L399,222 L402,222 L405,222 L408,222 L411,222 L414,222 L417,222 L420,222 L423,222 L426,222 L429,222 L432,222 L435,222 L438,222 L441,222 L444,222 L447,222 L450,222 L453,222 L456,222 L459,222 L462,222 L465,222 L468,222 L471,222 L474,222 L477,222 L480,222 L483,222 L486,222 L489,222 L492,222 L495,222 L498,222 L501,222 L504,222 L507,222 L510,222 L513,222 L516,222 L519,222 L522,222 L525,222 L528,222 L531,222 L534,222 L537,222 L540,222 L543,222 L546,222 L549,222 L552,222 L555,222 L558,222 L561,222 L564,222 L567,222 L570,222 L573,222 L576,222" fill="none" stroke="#a97a35" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="104" y="237" width="16" height="18" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="53" y="289.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = T$</div></foreignObject>
  <line x1="440" y1="268" x2="440" y2="340" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M120,304 L123,305.5 L126,307 L129,308 L132,309.5 L135,311 L138,312.5 L141,313.5 L144,315 L147,316 L150,317.5 L153,318.5 L156,319.5 L159,320.5 L162,321.5 L165,322.5 L168,323.5 L171,324 L174,325 L177,325.5 L180,326 L183,326.5 L186,327 L189,327.5 L192,327.5 L195,328 L198,328 L201,328 L204,328 L207,328 L210,327.5 L213,327 L216,327 L219,326.5 L222,326 L225,325 L228,324.5 L231,323.5 L234,323 L237,322 L240,321 L243,320 L246,319 L249,317.5 L252,316.5 L255,315.5 L258,314 L261,312.5 L264,311.5 L267,310 L270,308.5 L273,307.5 L276,306 L279,304.5 L282,303 L285,301.5 L288,300 L291,299 L294,297.5 L297,296 L300,295 L303,293.5 L306,292.5 L309,291 L312,290 L315,289 L318,287.5 L321,286.5 L324,286 L327,285 L330,284 L333,283.5 L336,282.5 L339,282 L342,281.5 L345,281 L348,280.5 L351,280.5 L354,280 L357,280 L360,280 L363,280 L366,280 L369,280.5 L372,280.5 L375,281 L378,281.5 L381,282 L384,282.5 L387,283.5 L390,284 L393,285 L396,286 L399,286.5 L402,287.5 L405,289 L408,290 L411,291 L414,292.5 L417,293.5 L420,295 L423,296 L426,297.5 L429,299 L432,300 L435,301.5 L438,303 L441,304 L444,304 L447,304 L450,304 L453,304 L456,304 L459,304 L462,304 L465,304 L468,304 L471,304 L474,304 L477,304 L480,304 L483,304 L486,304 L489,304 L492,304 L495,304 L498,304 L501,304 L504,304 L507,304 L510,304 L513,304 L516,304 L519,304 L522,304 L525,304 L528,304 L531,304 L534,304 L537,304 L540,304 L543,304 L546,304 L549,304 L552,304 L555,304 L558,304 L561,304 L564,304 L567,304 L570,304 L573,304 L576,304" fill="none" stroke="#a97a35" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="104" y="295" width="16" height="18" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <line x1="470" y1="360" x2="545" y2="360" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M560,360 L544,367 L544,353 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="442" y="345.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <line x1="120" y1="364" x2="440" y2="364" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="120" y1="356" x2="120" y2="372" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="440" y1="356" x2="440" y2="372" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="371.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
</svg>

Aallon nopeus on siis aallonpituus jaettuna jaksonajalla. Taajuus on $f = \tfrac{1}{T}$. Siksi saadaan **aaltoliikkeen perusyhtälö**
```latex
v = \frac{\lambda}{T} = f\lambda
```
Tässä $v$ on aallon etenemisnopeus ($\text{m/s}$), $\lambda$ on aallonpituus ($\text{m}$), $T$ on jaksonaika ($\text{s}$) ja $f$ on taajuus ($\text{Hz}$). Yksiköt sopivat yhteen, koska $1\,\text{Hz} = 1\,\text{s}^{-1}$. Siksi $1\,\text{Hz} \cdot 1\,\text{m} = 1\,\text{m/s}$. Pulssin nopeuden voi mitata myös suoraan. Pulssi etenee samassa väliaineessa tasaisella nopeudella, joten $v = \tfrac{s}{t}$. Tässä $s$ on matka ja $t$ on siihen kulunut aika.

### Nopeus riippuu väliaineesta, taajuus lähteestä
Väliaine määrää aallon nopeuden. Kireässä narussa aalto etenee nopeammin kuin löysässä. Ääni etenee $20\,{}^\circ\text{C}$:n ilmassa noin $343\,\text{m/s}$:n nopeudella. Vedessä ääni etenee noin $1500\,\text{m/s}$:n nopeudella. Lähde määrää taajuuden. Lähde on esimerkiksi käsi, jousen pää tai kaiutin, ja taajuus on sen värähtelyn taajuus. Narussa ja ilmassa aallon nopeus ei käytännössä riipu taajuudesta. Se ei myöskään riipu amplitudista, kun amplitudi on pieni. Heilutetaan samaa narua tiheämmin. Silloin nopeus pysyy samana ja aallonpituus lyhenee. Kaksinkertainen taajuus puolittaa aallonpituuden. Kun aalto siirtyy väliaineesta toiseen, taajuus säilyy. Nopeus ja aallonpituus muuttuvat.

### Valokuva ja yhden kohdan kuvaaja
Aaltoa voi kuvata kahdella kuvaajalla. Ne näyttävät samanlaisilta siniaalloilta. **Valokuva** eli $(x, y)$-kuvaaja näyttää koko narun muodon yhdellä hetkellä. Vaaka-akselilla on paikka $x$, ja kahden harjan väli on aallonpituus $\lambda$. **Yhden kohdan kuvaaja** eli $(t, y)$-kuvaaja näyttää yhden narun kohdan poikkeaman $y$ ajan funktiona. Vaaka-akselilla on aika $t$, ja kahden huipun väli on jaksonaika $T$. Kummastakin kuvaajasta voi lukea amplitudin $A$. Lue siis aina ensin, mikä suure on vaaka-akselilla.

<svg data-fig="graphs" viewBox="0 0 600 556" role="img" aria-label="Kaksi kuvaajaa samasta aallosta allekkain, amplitudi 4 cm. Ylempi on valokuva koko narusta yhdellä hetkellä. Vaaka-akselilla on paikka x metreinä nollasta 2,5 metriin ja pystyakselilla poikkeama y senttimetreinä. Kahden peräkkäisen harjan väli, 1,0 m, on merkitty aallonpituudeksi lambda. Harjan korkeus on merkitty amplitudiksi A. Alempi kuvaaja näyttää yhden narun kohdan poikkeaman ajan funktiona. Vaaka-akselilla on aika t sekunteina nollasta 1,25 sekuntiin. Kahden peräkkäisen huipun väli, 0,50 s, on merkitty jaksonajaksi T. Kuvaajat näyttävät samanmuotoisilta, mutta niiden vaaka-akseleilla on eri suureet." style="max-width:100%;font-size:24px">
  <foreignObject x="24" y="7.5" width="407" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{valokuva: koko naru yhdellä hetkellä}$</div></foreignObject>
  <foreignObject x="24" y="295.5" width="407" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{yksi kohta: poikkeama ajan funktiona}$</div></foreignObject>
  <line x1="12" y1="282" x2="588" y2="282" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="172" y1="236" x2="172" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="236" x2="248" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="236" x2="324" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="236" x2="400" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="236" x2="476" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="214" x2="476" y2="214" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="126" x2="476" y2="126" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="236" x2="96" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="170" x2="490" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,170 L489,176 L489,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="171" x2="96" y2="90" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,78 L102,91 L90,91 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="172" y1="170" x2="172" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248" y1="170" x2="248" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="170" x2="324" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="170" x2="400" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="170" x2="476" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="214" x2="96" y2="214" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="199.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-4$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="126" x2="96" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="111.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="508" y="155.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="86" y="47.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y\ (\text{cm})$</div></foreignObject>
  <foreignObject x="149.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}5$</div></foreignObject>
  <foreignObject x="238" y="241.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="301.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1{,}5$</div></foreignObject>
  <foreignObject x="390" y="241.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2$</div></foreignObject>
  <foreignObject x="453.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2{,}5$</div></foreignObject>
  <polyline points="96,170 99,164.5 102.5,158.5 105.5,153 108.5,148 112,143 115,139 118,135 121.5,132 124.5,129.5 127.5,127.5 131,126.5 134,126 137,126.5 140.5,127.5 143.5,129.5 146.5,132 150,135 153,139 156,143 159.5,148 162.5,153 165.5,158.5 169,164.5 172,170 175,175.5 178.5,181.5 181.5,187 184.5,192 188,197 191,201 194,205 197.5,208 200.5,210.5 203.5,212.5 207,213.5 210,214 213,213.5 216.5,212.5 219.5,210.5 222.5,208 226,205 229,201 232,197 235.5,192 238.5,187 241.5,181.5 245,175.5 248,170 251,164.5 254.5,158.5 257.5,153 260.5,148 264,143 267,139 270,135 273.5,132 276.5,129.5 279.5,127.5 283,126.5 286,126 289,126.5 292.5,127.5 295.5,129.5 298.5,132 302,135 305,139 308,143 311.5,148 314.5,153 317.5,158.5 321,164.5 324,170 327,175.5 330.5,181.5 333.5,187 336.5,192 340,197 343,201 346,205 349.5,208 352.5,210.5 355.5,212.5 359,213.5 362,214 365,213.5 368.5,212.5 371.5,210.5 374.5,208 378,205 381,201 384,197 387.5,192 390.5,187 393.5,181.5 397,175.5 400,170 403,164.5 406.5,158.5 409.5,153 412.5,148 416,143 419,139 422,135 425.5,132 428.5,129.5 431.5,127.5 435,126.5 438,126 441,126.5 444.5,127.5 447.5,129.5 450.5,132 454,135 457,139 460,143 463.5,148 466.5,153 469.5,158.5 473,164.5 476,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="134" y1="113" x2="286" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="134" y1="105" x2="134" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="105" x2="286" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="200" y="78.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <line x1="134" y1="126" x2="134" y2="121" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="286" y1="126" x2="286" y2="121" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="134" y1="170" x2="134" y2="135" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M134,126 L138.5,136 L129.5,136 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="141" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="172" y1="522" x2="172" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="522" x2="248" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="522" x2="324" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="522" x2="400" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="522" x2="476" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="500" x2="476" y2="500" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="412" x2="476" y2="412" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="522" x2="96" y2="456" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="456" x2="490" y2="456" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,456 L489,462 L489,450 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="457" x2="96" y2="376" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,364 L102,377 L90,377 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="172" y1="456" x2="172" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248" y1="456" x2="248" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="456" x2="324" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="456" x2="400" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="456" x2="476" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="500" x2="96" y2="500" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="485.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-4$</div></foreignObject>
  <line x1="89" y1="456" x2="96" y2="456" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="441.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="412" x2="96" y2="412" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="397.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="508" y="441.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="333.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y\ (\text{cm})$</div></foreignObject>
  <foreignObject x="143" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}25$</div></foreignObject>
  <foreignObject x="225.5" y="527.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}5$</div></foreignObject>
  <foreignObject x="295" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}75$</div></foreignObject>
  <foreignObject x="390" y="527.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="447" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1{,}25$</div></foreignObject>
  <polyline points="96,456 99,450.5 102.5,444.5 105.5,439 108.5,434 112,429 115,425 118,421 121.5,418 124.5,415.5 127.5,413.5 131,412.5 134,412 137,412.5 140.5,413.5 143.5,415.5 146.5,418 150,421 153,425 156,429 159.5,434 162.5,439 165.5,444.5 169,450.5 172,456 175,461.5 178.5,467.5 181.5,473 184.5,478 188,483 191,487 194,491 197.5,494 200.5,496.5 203.5,498.5 207,499.5 210,500 213,499.5 216.5,498.5 219.5,496.5 222.5,494 226,491 229,487 232,483 235.5,478 238.5,473 241.5,467.5 245,461.5 248,456 251,450.5 254.5,444.5 257.5,439 260.5,434 264,429 267,425 270,421 273.5,418 276.5,415.5 279.5,413.5 283,412.5 286,412 289,412.5 292.5,413.5 295.5,415.5 298.5,418 302,421 305,425 308,429 311.5,434 314.5,439 317.5,444.5 321,450.5 324,456 327,461.5 330.5,467.5 333.5,473 336.5,478 340,483 343,487 346,491 349.5,494 352.5,496.5 355.5,498.5 359,499.5 362,500 365,499.5 368.5,498.5 371.5,496.5 374.5,494 378,491 381,487 384,483 387.5,478 390.5,473 393.5,467.5 397,461.5 400,456 403,450.5 406.5,444.5 409.5,439 412.5,434 416,429 419,425 422,421 425.5,418 428.5,415.5 431.5,413.5 435,412.5 438,412 441,412.5 444.5,413.5 447.5,415.5 450.5,418 454,421 457,425 460,429 463.5,434 466.5,439 469.5,444.5 473,450.5 476,456" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="134" y1="399" x2="286" y2="399" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="134" y1="391" x2="134" y2="407" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="391" x2="286" y2="407" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="200" y="364.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="134" y1="412" x2="134" y2="407" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="286" y1="412" x2="286" y2="407" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="134" y1="456" x2="134" y2="421" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M134,412 L138.5,422 L129.5,422 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="141" y="431.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
</svg>

## Esimerkki
Pitkä naru on vedetty kireälle pihan poikki. Narun päätä heilautetaan kerran. Syntyvä pulssi kulkee $6{,}0\,\text{m}$:n matkan $2{,}5\,\text{s}$:ssa. Sitten samaa narua heilutetaan tasaisesti taajuudella $3{,}0\,\text{Hz}$. Narun jännitys ei muutu. Kuinka pitkä on syntyvän aallon aallonpituus?

<!-- vaihe -->

**Tunnetut ja kysytty.** Pulssin kulkema matka on $s = 6{,}0\,\text{m}$ ja siihen kulunut aika on $t = 2{,}5\,\text{s}$. Jaksollisen aallon taajuus on $f = 3{,}0\,\text{Hz}$. Kysytään aallonpituutta $\lambda$.

<!-- vaihe -->

**Periaate.** Aallon nopeus riippuu väliaineesta. Tässä väliaine on naru ja sen jännitys. Nopeus ei riipu siitä, tehdäänkö narussa pulssi vai jaksollinen aalto. Siksi jaksollinen aalto etenee samalla nopeudella $v$ kuin pulssi. Pulssi etenee tasaisesti, joten $v = \tfrac{s}{t}$. Aallonpituus saadaan sitten perusyhtälöstä $v = f\lambda$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&v = \frac{s}{t} \quad\text{ja}\quad v = f\lambda \\
&\lambda = \frac{v}{f} = \frac{s}{f\,t}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Matka on metreinä ja aika sekunteina. Lisäksi $1\,\text{Hz} = 1\,\text{s}^{-1}$, joten $\tfrac{\text{m/s}}{\text{Hz}} = \text{m}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin nopeus ja sitten aallonpituus:
```latex
\begin{aligned}
&v = \frac{s}{t} \\
&= \frac{6{,}0\,\text{m}}{2{,}5\,\text{s}} = 2{,}4\,\text{m/s} \\[6pt]
&\lambda = \frac{v}{f} \\
&= \frac{2{,}4\,\text{m/s}}{3{,}0\,\text{Hz}} = 0{,}80\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Aallonpituus on $0{,}80\,\text{m}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla. Lähtötiedotkin on annettu kahdella merkitsevällä numerolla: $6{,}0\,\text{m}$, $2{,}5\,\text{s}$ ja $3{,}0\,\text{Hz}$.

<!-- vaihe -->

**Järkevyys.** Jaksonaika on $T = \tfrac{1}{f} = 0{,}333\,\text{s}$. Siinä ajassa aalto etenee $2{,}4\,\text{m/s} \cdot 0{,}333\,\text{s} = 0{,}80\,\text{m}$. Se on juuri yksi aallonpituus, kuten pitääkin.

## Yleinen virhekäsitys
Moni ajattelee, että aalto etenee sitä nopeammin, mitä tiheämmin kättä heilutetaan. Samassa narussa nopeus pysyy kuitenkin samana. Taajuus kasvaa $1{,}0\,\text{Hz}$:stä $2{,}0\,\text{Hz}$:iin. Silloin aallonpituus lyhenee $2{,}0\,\text{m}$:stä $1{,}0\,\text{m}$:iin. Tulo $f\lambda$ on silti edelleen $2{,}0\,\text{m/s}$. Nopeuden voi muuttaa vain muuttamalla väliainetta, esimerkiksi kiristämällä narua.

Toinen yleinen virhe on lukea aallonpituus yhden kohdan $(t, y)$-kuvaajasta. Siinä huippujen väli on jaksonaika $T$ sekunteina, ei aallonpituus. Kolmas virhe on ajatella, että aalto kuljettaa narun ainetta mukanaan. Narun kohdat vain värähtelevät paikallaan. Eteenpäin siirtyy energia.

## Tiivistelmä
- Aaltoliike on häiriön etenemistä väliaineessa. Väliaineen hiukkaset värähtelevät tasapainoasemansa ympärillä. Aalto kuljettaa energiaa mutta ei ainetta.
- Poikittaisessa aallossa hiukkaset värähtelevät kohtisuoraan etenemissuuntaa vastaan (naru). Pitkittäisessä aallossa ne värähtelevät etenemissuunnan suuntaisesti (kierrejousi, ääni ilmassa).
- Yksi heilautus tekee pulssin. Tasainen heilutus tekee jaksollisen aallon. Aallonpituus $\lambda$ on kahden peräkkäisen harjan väli.
- Aaltoliikkeen perusyhtälö on $v = \tfrac{\lambda}{T} = f\lambda$. Nopeus riippuu väliaineesta ja taajuus lähteestä.
- Valokuvasta eli $(x, y)$-kuvaajasta luetaan aallonpituus. Yhden kohdan $(t, y)$-kuvaajasta luetaan jaksonaika.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: stadionin katsomo. Katsojia istuu kolmessa rivissä. Keskellä joukko katsojia on noussut seisomaan kädet ylhäällä. Seisovien vieressä katsojat ovat puoliksi nousseet tai istuutumassa. Katsojat eivät vaihda paikkaa, mutta nousemisen kohta kiertää katsomossa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy510s-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="url(#fy510s-sky)"/>
  <rect x="0" y="174" width="600" height="18" fill="#8a96a3"/>
  <rect x="0" y="192" width="600" height="80" fill="#c4ccd4"/>
  <rect x="20.5" y="142.5" width="18.5" height="33.5" rx="4.96" fill="#1971c2"/>
  <circle cx="30" cy="133" r="8.06" fill="#f1dfb5"/>
  <rect x="70.5" y="142.5" width="18.5" height="33.5" rx="4.96" fill="#e8590c"/>
  <circle cx="80" cy="133" r="8.06" fill="#f1dfb5"/>
  <rect x="120.5" y="142.5" width="18.5" height="33.5" rx="4.96" fill="#2b8a3e"/>
  <circle cx="130" cy="133" r="8.06" fill="#f1dfb5"/>
  <rect x="170.5" y="141" width="18.5" height="35" rx="4.96" fill="#b8622d"/>
  <circle cx="180" cy="131.5" r="8.06" fill="#f1dfb5"/>
  <rect x="220.5" y="130.5" width="18.5" height="45.5" rx="4.96" fill="#c92a2a"/>
  <circle cx="230" cy="121.5" r="8.06" fill="#f1dfb5"/>
  <rect x="270.5" y="113" width="18.5" height="63" rx="4.96" fill="#6c757d"/>
  <circle cx="280" cy="103.5" r="8.06" fill="#f1dfb5"/>
  <path d="M273,116.5 L266.5,88" fill="none" stroke="#6c757d" stroke-width="5.58" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M287,116.5 L293.5,88" fill="none" stroke="#6c757d" stroke-width="5.58" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="320.5" y="115.5" width="18.5" height="60.5" rx="4.96" fill="#1971c2"/>
  <circle cx="330" cy="106.5" r="8.06" fill="#f1dfb5"/>
  <path d="M323,119.5 L316.5,91" fill="none" stroke="#1971c2" stroke-width="5.58" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M337,119.5 L343.5,91" fill="none" stroke="#1971c2" stroke-width="5.58" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="370.5" y="134" width="18.5" height="42" rx="4.96" fill="#e8590c"/>
  <circle cx="380" cy="124.5" r="8.06" fill="#f1dfb5"/>
  <rect x="420.5" y="141.5" width="18.5" height="34.5" rx="4.96" fill="#2b8a3e"/>
  <circle cx="430" cy="132" r="8.06" fill="#f1dfb5"/>
  <rect x="470.5" y="142.5" width="18.5" height="33.5" rx="4.96" fill="#b8622d"/>
  <circle cx="480" cy="133" r="8.06" fill="#f1dfb5"/>
  <rect x="520.5" y="142.5" width="18.5" height="33.5" rx="4.96" fill="#c92a2a"/>
  <circle cx="530" cy="133" r="8.06" fill="#f1dfb5"/>
  <rect x="570.5" y="142.5" width="18.5" height="33.5" rx="4.96" fill="#6c757d"/>
  <circle cx="580" cy="133" r="8.06" fill="#f1dfb5"/>
  <rect x="0" y="254" width="600" height="24" fill="#8a96a3"/>
  <rect x="0" y="278" width="600" height="80" fill="#c4ccd4"/>
  <rect x="41.5" y="218" width="21" height="38" rx="5.6" fill="#2b8a3e"/>
  <circle cx="52" cy="207.5" r="9.1" fill="#f1dfb5"/>
  <rect x="91.5" y="218" width="21" height="38" rx="5.6" fill="#b8622d"/>
  <circle cx="102" cy="207.5" r="9.1" fill="#f1dfb5"/>
  <rect x="141.5" y="218" width="21" height="38" rx="5.6" fill="#c92a2a"/>
  <circle cx="152" cy="207.5" r="9.1" fill="#f1dfb5"/>
  <rect x="191.5" y="213" width="21" height="43" rx="5.6" fill="#6c757d"/>
  <circle cx="202" cy="202.5" r="9.1" fill="#f1dfb5"/>
  <rect x="241.5" y="195.5" width="21" height="60.5" rx="5.6" fill="#1971c2"/>
  <circle cx="252" cy="185" r="9.1" fill="#f1dfb5"/>
  <path d="M244.5,199.5 L236.5,167.5" fill="none" stroke="#1971c2" stroke-width="6.3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M259.5,199.5 L267.5,167.5" fill="none" stroke="#1971c2" stroke-width="6.3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="291.5" y="182" width="21" height="74" rx="5.6" fill="#e8590c"/>
  <circle cx="302" cy="171.5" r="9.1" fill="#f1dfb5"/>
  <path d="M294.5,186 L286.5,154" fill="none" stroke="#e8590c" stroke-width="6.3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M309.5,186 L317.5,154" fill="none" stroke="#e8590c" stroke-width="6.3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="341.5" y="197" width="21" height="59" rx="5.6" fill="#2b8a3e"/>
  <circle cx="352" cy="186.5" r="9.1" fill="#f1dfb5"/>
  <path d="M344.5,201.5 L336.5,169" fill="none" stroke="#2b8a3e" stroke-width="6.3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M359.5,201.5 L367.5,169" fill="none" stroke="#2b8a3e" stroke-width="6.3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="391.5" y="214" width="21" height="42" rx="5.6" fill="#b8622d"/>
  <circle cx="402" cy="203.5" r="9.1" fill="#f1dfb5"/>
  <rect x="441.5" y="218" width="21" height="38" rx="5.6" fill="#c92a2a"/>
  <circle cx="452" cy="207.5" r="9.1" fill="#f1dfb5"/>
  <rect x="491.5" y="218" width="21" height="38" rx="5.6" fill="#6c757d"/>
  <circle cx="502" cy="207.5" r="9.1" fill="#f1dfb5"/>
  <rect x="541.5" y="218" width="21" height="38" rx="5.6" fill="#1971c2"/>
  <circle cx="552" cy="207.5" r="9.1" fill="#f1dfb5"/>
  <rect x="0" y="340" width="600" height="30" fill="#8a96a3"/>
  <rect x="0" y="370" width="600" height="80" fill="#c4ccd4"/>
  <rect x="18.5" y="300" width="23.5" height="42" rx="6.24" fill="#c92a2a"/>
  <circle cx="30" cy="288" r="10.14" fill="#f1dfb5"/>
  <rect x="68.5" y="300" width="23.5" height="42" rx="6.24" fill="#6c757d"/>
  <circle cx="80" cy="288" r="10.14" fill="#f1dfb5"/>
  <rect x="118.5" y="300" width="23.5" height="42" rx="6.24" fill="#1971c2"/>
  <circle cx="130" cy="288" r="10.14" fill="#f1dfb5"/>
  <rect x="168.5" y="297.5" width="23.5" height="44.5" rx="6.24" fill="#e8590c"/>
  <circle cx="180" cy="286" r="10.14" fill="#f1dfb5"/>
  <rect x="218.5" y="285" width="23.5" height="57" rx="6.24" fill="#2b8a3e"/>
  <circle cx="230" cy="273.5" r="10.14" fill="#f1dfb5"/>
  <rect x="268.5" y="262.5" width="23.5" height="79.5" rx="6.24" fill="#b8622d"/>
  <circle cx="280" cy="251" r="10.14" fill="#f1dfb5"/>
  <path d="M271.5,267 L263,231.5" fill="none" stroke="#b8622d" stroke-width="7.02" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M288.5,267 L297,231.5" fill="none" stroke="#b8622d" stroke-width="7.02" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="318.5" y="266" width="23.5" height="76" rx="6.24" fill="#c92a2a"/>
  <circle cx="330" cy="254.5" r="10.14" fill="#f1dfb5"/>
  <path d="M321.5,271 L313,235" fill="none" stroke="#c92a2a" stroke-width="7.02" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M338.5,271 L347,235" fill="none" stroke="#c92a2a" stroke-width="7.02" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="368.5" y="289" width="23.5" height="53" rx="6.24" fill="#6c757d"/>
  <circle cx="380" cy="277" r="10.14" fill="#f1dfb5"/>
  <rect x="418.5" y="298.5" width="23.5" height="43.5" rx="6.24" fill="#1971c2"/>
  <circle cx="430" cy="287" r="10.14" fill="#f1dfb5"/>
  <rect x="468.5" y="300" width="23.5" height="42" rx="6.24" fill="#e8590c"/>
  <circle cx="480" cy="288" r="10.14" fill="#f1dfb5"/>
  <rect x="518.5" y="300" width="23.5" height="42" rx="6.24" fill="#2b8a3e"/>
  <circle cx="530" cy="288" r="10.14" fill="#f1dfb5"/>
  <rect x="568.5" y="300" width="23.5" height="42" rx="6.24" fill="#b8622d"/>
  <circle cx="580" cy="288" r="10.14" fill="#f1dfb5"/>
</svg>
