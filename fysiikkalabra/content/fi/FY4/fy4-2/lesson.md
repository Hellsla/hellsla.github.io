# Kiihtyvyys ja tasaisesti kiihtyvä liike

> **Miksi** sillalta pudotettu kivi kulkee jokaisen sekunnin aikana pidemmän matkan kuin edellisen sekunnin aikana?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kevyen liikenteen silta joen yllä kesäpäivänä. Sillan keskellä nuori pudottaa kiven kaiteen yli, ja rannalla ystävä kuvaa putoamista puhelimella. Kivi on piirretty viiteen kohtaan yhtä pitkin aikavälein: välit kasvavat alaspäin suhteessa 1 : 3 : 5 : 7, ja kiven vieressä oleva sininen nopeusnuoli pitenee joka kerta yhtä paljon. Alimmassa kohdassa kivi osuu veteen ja vesi roiskuu. Mittakaava ei ole tarkka, välien suhteet ovat." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy42h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy42h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy42h-river" gradientUnits="userSpaceOnUse" x1="0" y1="330" x2="0" y2="600"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy42h-grass" gradientUnits="userSpaceOnUse" x1="0" y1="300" x2="0" y2="520"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#f1dfb5"/></linearGradient><linearGradient id="fy42h-pier" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.4" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy42h-deck" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy42h-rail" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#b8622d"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="380" fill="url(#fy42h-sky)"/>
  <circle cx="1060" cy="92" r="70.5" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="1060" cy="92" r="44" fill="url(#fy42h-sun)"/>
  <path d="M308,54 Q319.0,48 330,60 Q341.0,48 352,54" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M348,40 Q357.0,34 366,46 Q375.0,34 384,40" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M680,98 Q690.0,92 700,104 Q710.0,92 720,98" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M162.5,95 Q161,69.5 191,72.5 Q203,45.5 233,54.5 Q260,39.5 275,68 Q302,71 299,95 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M770.5,69 Q769.5,50.5 791.5,52.5 Q800,32.5 822,39.5 Q842,28.5 853,49 Q873,51.5 870.5,69 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M434,138 Q433,124.5 449,126 Q455.5,111.5 471.5,116.5 Q486,108.5 494,123.5 Q508.5,125 507,138 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,236 Q100,189.5 200,239 Q300,194.5 400,238 Q500,221 600,233 Q700,221.5 800,233 Q900,194.5 1000,238 Q1100,219.5 1200,233 Q1300,213.5 1400,234.5 V600 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M0,266.5 Q100,228 200,264 Q300,224.5 400,264 Q500,229.5 600,269.5 Q700,223 800,267 Q900,236.5 1000,268.5 Q1100,224.5 1200,266 Q1300,242 1400,268.5 V600 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M0,290 L8.5,269.5 L17,290 L26,268.5 L35,290 L46,261.5 L57,290 L68,262 L78.5,290 L94,247.5 L109,290 L121.5,257 L133.5,290 L146,256.5 L158.5,290 L171,256.5 L183.5,290 L196,256.5 L208.5,290 L221,256.5 L233.5,290 L244.5,261 L256,290 L271,248 L286,290 L300,250.5 L314.5,290 L324,265.5 L334,290 L348,252 L361.5,290 L375,254 L388,290 L403,247 L418.5,290 L430,259 L442,290 L457,248 L472,290 L484,258 L496,290 L508,257.5 L520.5,290 L532.5,258 L544.5,290 L553.5,267.5 L562.5,290 L571.5,268 L580.5,290 L592,260.5 L603.5,290 L618,249 L633,290 L645.5,256.5 L658,290 L667.5,266.5 L677,290 L689,257 L701.5,290 L715.5,251.5 L729.5,290 L738,270 L746.5,290 L759.5,255 L772,290 L781,269.5 L789.5,290 L801,260.5 L812,290 L822,265.5 L831.5,290 L845.5,252.5 L859,290 L872.5,252.5 L886,290 L900.5,250.5 L914.5,290 L926.5,259 L938,290 L949.5,259.5 L961,290 L972.5,260 L984,290 L995.5,260 L1007,290 L1016,268 L1025,290 L1037,258 L1049,290 L1061,258.5 L1073,290 L1088,247.5 L1103.5,290 L1113.5,264.5 L1123.5,290 L1139,246.5 L1154.5,290 L1167.5,254.5 L1180.5,290 L1194.5,252 L1208.5,290 V308 H0 Z" fill="#6c757d" stroke-linejoin="round"/>
  <path d="M0,314 L17.5,266 L35,314 L47.5,283.5 L59.5,314 L72.5,280 L86,314 L100,277.5 L114,314 L125,288.5 L135.5,314 L150.5,275 L165,314 L177.5,282.5 L190,314 L204.5,277 L218.5,314 L232,280.5 L245,314 L257.5,282.5 L270,314 L286.5,270.5 L302.5,314 L315,283.5 L327,314 L344,269 L360.5,314 L377.5,268.5 L394.5,314 L412.5,264.5 L430.5,314 L443.5,281 L456.5,314 L469,282.5 L481.5,314 L492.5,288 L503.5,314 L515,285.5 L526.5,314 L542.5,271 L558.5,314 L569.5,289 L580,314 L590,291.5 L599.5,314 L615,273 L630.5,314 L646.5,271.5 L662.5,314 L676.5,278.5 L690,314 L705,274.5 L720,314 L733.5,279.5 L747,314 L761.5,275 L776.5,314 L787,288.5 L798,314 L815.5,266 L833,314 L847,278.5 L860.5,314 L873.5,281.5 L886.5,314 L902.5,270.5 L918.5,314 L931.5,281 L944.5,314 L962.5,265 L980.5,314 L995.5,274.5 L1010.5,314 L1026.5,271.5 L1042,314 L1055,282 L1067.5,314 L1081.5,278.5 L1095,314 L1112,268.5 L1129,314 L1140,287.5 L1151,314 L1167,271 L1183,314 L1199.5,269.5 L1216,314 V328 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="330" width="1200" height="270" fill="url(#fy42h-river)"/>
  <path d="M351,372.5 q14,-5 28.5,0 t28.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M513.5,394.5 q22,-5 44.5,0 t44.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M380,384.5 q12.5,-5 25,0 t25,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M1035.5,538.5 q13,-5 26,0 t26,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M727,404 q10,-5 20.5,0 t20.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M1039,401.5 q11,-5 21.5,0 t21.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M803,509.5 q17.5,-5 34.5,0 t34.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M190.5,565 q21,-5 42,0 t42,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M972,508 q17,-5 34,0 t34,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M123.5,574.5 q11,-5 22,0 t22,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M369,552 q17.5,-5 35.5,0 t35.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M860.5,476 q13,-5 26,0 t26,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M742.5,562.5 q16,-5 32.5,0 t32.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M204,475.5 q11.5,-5 23,0 t23,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M128.5,430.5 q12.5,-5 25.5,0 t25.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M284.5,510.5 q18,-5 36.5,0 t36.5,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M0,300 H250 Q300,304 322,350 L372,486 Q380,512 404,524 H0 Z" fill="url(#fy42h-grass)" stroke-linejoin="round"/>
  <path d="M0,500 H360 Q390,512 404,524 L430,560 H0 Z" fill="#d9b26a" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="102.5" cy="551" r="3.08131" fill="#a97a35"/>
  <circle cx="342" cy="544.5" r="3.22171" fill="#a97a35"/>
  <circle cx="230" cy="513.5" r="4.0927" fill="#a97a35"/>
  <circle cx="33.5" cy="513" r="4.0056" fill="#a97a35"/>
  <circle cx="61.5" cy="545" r="5.82233" fill="#a97a35"/>
  <circle cx="124" cy="515.5" r="4.61358" fill="#a97a35"/>
  <circle cx="400" cy="522.5" r="4.70626" fill="#a97a35"/>
  <circle cx="187" cy="517.5" r="4.69956" fill="#a97a35"/>
  <circle cx="21" cy="539" r="4.72443" fill="#a97a35"/>
  <circle cx="215" cy="528.5" r="4.70478" fill="#a97a35"/>
  <circle cx="245" cy="541.5" r="4.13328" fill="#a97a35"/>
  <circle cx="307.5" cy="546" r="5.74787" fill="#a97a35"/>
  <circle cx="266" cy="540" r="5.4366" fill="#a97a35"/>
  <circle cx="28" cy="547" r="3.59257" fill="#a97a35"/>
  <circle cx="184" cy="531.5" r="5.24372" fill="#a97a35"/>
  <circle cx="157" cy="545.5" r="4.99664" fill="#a97a35"/>
  <circle cx="114.5" cy="525" r="5.87183" fill="#a97a35"/>
  <circle cx="202" cy="547.5" r="4.36756" fill="#a97a35"/>
  <rect x="85.5" y="120" width="12.5" height="210" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="85.5" y="305" width="6.5" height="3" fill="#1f2933"/>
  <rect x="92" y="279.5" width="6.5" height="3" fill="#1f2933"/>
  <rect x="85.5" y="254.5" width="6.5" height="3" fill="#1f2933"/>
  <rect x="92" y="229" width="6.5" height="3" fill="#1f2933"/>
  <rect x="85.5" y="204" width="6.5" height="3" fill="#1f2933"/>
  <rect x="92" y="179" width="6.5" height="3" fill="#1f2933"/>
  <rect x="85.5" y="153.5" width="6.5" height="3" fill="#1f2933"/>
  <line x1="92" y1="200" x2="54" y2="174.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="92" y1="172.5" x2="130" y2="147.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="92" y1="151.5" x2="54" y2="126.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="92" cy="130.5" r="42" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="60.5" cy="162" r="33.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="123.5" cy="158" r="35.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="92" cy="179" r="31.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="191" y="301.5" width="9.5" height="14.5" fill="#b8622d"/>
  <path d="M153,304 L196,256 L239,304 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M196,256 L239,304 H196 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M162.5,277.5 L196,229.5 L229.5,277.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M196,229.5 L229.5,277.5 H196 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M172,251 L196,196 L220,251 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M196,196 L220,251 H196 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1200,300 H960 Q920,304 900,350 L862,452 Q850,486 820,500 H1200 Z" fill="url(#fy42h-grass)" stroke-linejoin="round"/>
  <path d="M1200,470 H860 Q830,486 800,520 L780,560 H1200 Z" fill="#d9b26a" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="847.5" cy="541" r="3.16843" fill="#a97a35"/>
  <circle cx="842" cy="503" r="3.46714" fill="#a97a35"/>
  <circle cx="1152.5" cy="511" r="3.33455" fill="#a97a35"/>
  <circle cx="1011" cy="516.5" r="5.43077" fill="#a97a35"/>
  <circle cx="1108.5" cy="492.5" r="3.59674" fill="#a97a35"/>
  <circle cx="948" cy="521.5" r="3.56354" fill="#a97a35"/>
  <circle cx="1091" cy="505.5" r="5.04081" fill="#a97a35"/>
  <circle cx="822.5" cy="518" r="5.79468" fill="#a97a35"/>
  <circle cx="1127.5" cy="510" r="5.01552" fill="#a97a35"/>
  <circle cx="1164.5" cy="506" r="5.9258" fill="#a97a35"/>
  <circle cx="857.5" cy="532.5" r="5.61515" fill="#a97a35"/>
  <circle cx="1157" cy="503.5" r="4.58315" fill="#a97a35"/>
  <circle cx="839" cy="535.5" r="5.76408" fill="#a97a35"/>
  <circle cx="1006" cy="536" r="4.57672" fill="#a97a35"/>
  <circle cx="1153.5" cy="545" r="3.95911" fill="#a97a35"/>
  <circle cx="1020.5" cy="508.5" r="5.05482" fill="#a97a35"/>
  <circle cx="1071" cy="506" r="4.61823" fill="#a97a35"/>
  <circle cx="1123" cy="494" r="4.39941" fill="#a97a35"/>
  <rect x="1135" y="290.5" width="10.5" height="15.5" fill="#b8622d"/>
  <path d="M1093,293 L1140,241 L1187,293 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1140,241 L1187,293 H1140 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1103.5,264.5 L1140,212.5 L1176.5,264.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1140,212.5 L1176.5,264.5 H1140 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1114,236 L1140,176 L1166,236 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1140,176 L1166,236 H1140 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1056.5" y="289" width="7" height="11" fill="#b8622d"/>
  <path d="M1027.5,291 L1060,255 L1092.5,291 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1060,255 L1092.5,291 H1060 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1035,271 L1060,235 L1085,271 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1060,235 L1085,271 H1060 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1042,251.5 L1060,210 L1078,251.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1060,210 L1078,251.5 H1060 Z" fill="#1f2933" fill-opacity="0.18"/>
  <circle cx="30" cy="318" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="46" cy="312" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="16" cy="314" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="64" cy="326" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="80" cy="320" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="50" cy="322" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="98" cy="318" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="114" cy="312" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="84" cy="314" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="132" cy="326" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="148" cy="320" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="118" cy="322" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="166" cy="318" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="182" cy="312" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="152" cy="314" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1000" cy="326" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1016" cy="320" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="986" cy="322" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1046" cy="318" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1062" cy="312" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1032" cy="314" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1092" cy="326" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1108" cy="320" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1078" cy="322" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1138" cy="318" r="18" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1154" cy="312" r="14" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1124" cy="314" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="254.5" y1="383.5" x2="254.5" y2="373.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="254.5" cy="371.5" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="22.5" y1="428.5" x2="22.5" y2="418.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="22.5" cy="416.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="84" y1="464.5" x2="84" y2="454.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="84" cy="452.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="238.5" y1="410" x2="238.5" y2="400" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="238.5" cy="398" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="269" y1="397" x2="269" y2="387" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="269" cy="385" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="179" y1="378.5" x2="179" y2="368.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="179" cy="366.5" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="214" y1="363.5" x2="214" y2="353.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="214" cy="351.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="197.5" y1="362" x2="197.5" y2="352" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="197.5" cy="350" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="170.5" y1="369.5" x2="170.5" y2="359.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="170.5" cy="357.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="127" y1="358" x2="127" y2="348" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="127" cy="346" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="266" y1="375.5" x2="266" y2="365.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="266" cy="363.5" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="1071" y1="375" x2="1071" y2="365" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="1071" cy="363" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="949.5" y1="427" x2="949.5" y2="417" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="949.5" cy="415" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="1079" y1="467.5" x2="1079" y2="457.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="1079" cy="455.5" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="985" y1="375.5" x2="985" y2="365.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="985" cy="363.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="932" y1="399.5" x2="932" y2="389.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="932" cy="387.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="962" y1="436" x2="962" y2="426" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="962" cy="424" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="1143" y1="366.5" x2="1143" y2="356.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="1143" cy="354.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="1055" y1="352.5" x2="1055" y2="342.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="1055" cy="340.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="1154.5" y1="429.5" x2="1154.5" y2="419.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="1154.5" cy="417.5" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="946" y1="448.5" x2="946" y2="438.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="946" cy="436.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="921" y1="425" x2="921" y2="415" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="921" cy="413" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <line x1="1100.5" y1="429.5" x2="1100.5" y2="419.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="1100.5" cy="417.5" r="3.5" fill="#c92a2a" stroke="#1f2933" stroke-width="1"/>
  <line x1="930.5" y1="364.5" x2="930.5" y2="354.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="930.5" cy="352.5" r="3.5" fill="#ffffff" stroke="#1f2933" stroke-width="1"/>
  <path d="M156.5,478 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M158.5,415.5 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M264.5,433.5 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M221,441 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M186,412 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M150.5,432 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M173.5,446 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M947.5,428 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M938,414 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M1056.5,471.5 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M967.5,414.5 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M1076.5,403.5 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M1083,414.5 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M999.5,471 l4,-14 l4,14 l4,-12 l4,12" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="353" y1="528" x2="350" y2="488" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="350" cy="488" rx="4" ry="10" fill="#b8622d"/>
  <line x1="362" y1="534" x2="359" y2="494" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="359" cy="494" rx="4" ry="10" fill="#b8622d"/>
  <line x1="371" y1="528" x2="368" y2="488" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="368" cy="488" rx="4" ry="10" fill="#b8622d"/>
  <line x1="380" y1="534" x2="377" y2="494" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="377" cy="494" rx="4" ry="10" fill="#b8622d"/>
  <line x1="389" y1="528" x2="386" y2="488" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="386" cy="488" rx="4" ry="10" fill="#b8622d"/>
  <line x1="398" y1="534" x2="395" y2="494" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="395" cy="494" rx="4" ry="10" fill="#b8622d"/>
  <line x1="813" y1="488" x2="810" y2="448" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="810" cy="448" rx="4" ry="10" fill="#b8622d"/>
  <line x1="822" y1="494" x2="819" y2="454" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="819" cy="454" rx="4" ry="10" fill="#b8622d"/>
  <line x1="831" y1="488" x2="828" y2="448" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="828" cy="448" rx="4" ry="10" fill="#b8622d"/>
  <line x1="840" y1="494" x2="837" y2="454" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="837" cy="454" rx="4" ry="10" fill="#b8622d"/>
  <line x1="849" y1="488" x2="846" y2="448" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="846" cy="448" rx="4" ry="10" fill="#b8622d"/>
  <line x1="858" y1="494" x2="855" y2="454" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="855" cy="454" rx="4" ry="10" fill="#b8622d"/>
  <ellipse cx="430" cy="548" rx="54" ry="10" fill="#2f74b5" fill-opacity="0.5"/>
  <path d="M396,260 L388,548 H472 L464,260 Z" fill="url(#fy42h-pier)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="395" y1="300" x2="465" y2="300" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="260" x2="420" y2="300" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="393.5" y1="340" x2="466.5" y2="340" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="438" y1="300" x2="438" y2="340" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="392.5" y1="380" x2="467.5" y2="380" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="340" x2="420" y2="380" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="391" y1="420" x2="469" y2="420" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="438" y1="380" x2="438" y2="420" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="390" y1="460" x2="470" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="420" x2="420" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="389" y1="500" x2="471" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="438" y1="460" x2="438" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <path d="M400,554 q15,8 30,0 t30,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="790" cy="548" rx="54" ry="10" fill="#2f74b5" fill-opacity="0.5"/>
  <path d="M756,260 L748,548 H832 L824,260 Z" fill="url(#fy42h-pier)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="755" y1="300" x2="825" y2="300" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="780" y1="260" x2="780" y2="300" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="753.5" y1="340" x2="826.5" y2="340" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="798" y1="300" x2="798" y2="340" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="752.5" y1="380" x2="827.5" y2="380" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="780" y1="340" x2="780" y2="380" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="751" y1="420" x2="829" y2="420" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="798" y1="380" x2="798" y2="420" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="750" y1="460" x2="830" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="780" y1="420" x2="780" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="749" y1="500" x2="831" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="798" y1="460" x2="798" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <path d="M760,554 q15,8 30,0 t30,0" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="170" y="236" width="860" height="24" rx="2" fill="url(#fy42h-deck)" stroke="#1f2933" stroke-width="3"/>
  <rect x="170" y="254" width="860" height="6" fill="#6c757d"/>
  <rect x="150" y="232" width="40" height="70" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1010" y="232" width="40" height="70" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M566,178.5 L559.5,234" fill="none" stroke="#6c757d" stroke-width="10.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M552.5,236 h16" fill="none" stroke="#6c757d" stroke-width="5.76" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M572.5,129.5 L630,142" fill="none" stroke="#2b8a3e" stroke-width="8.64" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M559,121 Q586.5,110 581,142.5 L574.5,182 H553 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M566,178.5 L572.5,234" fill="none" stroke="#6c757d" stroke-width="10.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M578,236 h16" fill="none" stroke="#6c757d" stroke-width="5.76" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M575,128 L630,142" fill="none" stroke="#2b8a3e" stroke-width="8.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="630" cy="142" r="4.68" fill="#f1dfb5"/>
  <rect x="574.5" y="106.5" width="7" height="11" fill="#f1dfb5"/>
  <circle cx="578" cy="97" r="12.24" fill="#f1dfb5"/>
  <path d="M566,99 Q565,83.5 579,84 Q590.5,85 590.5,93.5 Q578,90.5 566,99 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="183" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="221.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="260" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="298.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="337" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="375.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="414" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="452.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="491" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="529.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="568" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="606.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="645" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="683.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="722" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="760.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="799" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="837.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="876" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="914.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="953" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="991.5" y="152" width="6" height="84" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="176" y="146" width="848" height="10" rx="3" fill="url(#fy42h-rail)" stroke="#1f2933" stroke-width="2"/>
  <line x1="180" y1="192" x2="1020" y2="192" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="180" y1="216" x2="1020" y2="216" stroke="#b8622d" stroke-width="3" stroke-linecap="butt"/>
  <path d="M575,128 L630,142" fill="none" stroke="#2b8a3e" stroke-width="8.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="630" cy="142" r="4.68" fill="#f1dfb5"/>
  <g transform="translate(1900,0) scale(-1,1)">
  <path d="M950,412 L942,473.5" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M934,476 h17.5" fill="none" stroke="#6c757d" stroke-width="6.4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M953,357.5 L890,330" fill="none" stroke="#e9c98a" stroke-width="9.6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M938.5,348 Q968.5,336 963.5,372 L959.5,416 H935.5 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M950,412 L958,473.5" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M964.5,476 h17.5" fill="none" stroke="#6c757d" stroke-width="6.4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M955.5,356 L890,330" fill="none" stroke="#e9c98a" stroke-width="9.6" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="890" cy="330" r="5.2" fill="#f1dfb5"/>
  <rect x="952.5" y="332" width="8" height="12" fill="#f1dfb5"/>
  <circle cx="956.5" cy="321.5" r="13.6" fill="#f1dfb5"/>
  <path d="M943,324 Q942,306.5 957,307 Q970,308 970,317.5 Q956.5,314.5 943,324 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <rect x="1002" y="312" width="16" height="28" rx="3" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <rect x="1005" y="316" width="10" height="20" rx="2" fill="#a5d8ff"/>
  <ellipse cx="230" cy="572" rx="24" ry="10" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="250" cy="558" r="8" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <path d="M257,557 l9,2 l-9,3 Z" fill="#ffc078" stroke="#1f2933" stroke-width="1" stroke-linejoin="round"/>
  <path d="M200,582 q12,5 24,0 t24,0 t24,0" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <ellipse cx="282" cy="586" rx="24" ry="10" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="302" cy="572" r="8" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <path d="M309,571 l9,2 l-9,3 Z" fill="#ffc078" stroke="#1f2933" stroke-width="1" stroke-linejoin="round"/>
  <path d="M252,596 q12,5 24,0 t24,0 t24,0" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <g opacity="1">
  <ellipse cx="636" cy="156" rx="12" ry="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="632" cy="153" rx="4" ry="3" fill="#c4ccd4"/>
  </g>
  <g opacity="0.55">
  <ellipse cx="636" cy="179" rx="12" ry="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="632" cy="176" rx="4" ry="3" fill="#c4ccd4"/>
  </g>
  <line x1="680" y1="169.5" x2="680" y2="175.5" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M680,188.5 L673.5,174.5 L686.5,174.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <g opacity="0.55">
  <ellipse cx="636" cy="247.5" rx="12" ry="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="632" cy="244.5" rx="4" ry="3" fill="#c4ccd4"/>
  </g>
  <line x1="680" y1="228.5" x2="680" y2="253.5" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M680,266.5 L673.5,252.5 L686.5,252.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <g opacity="0.55">
  <ellipse cx="636" cy="362" rx="12" ry="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="632" cy="359" rx="4" ry="3" fill="#c4ccd4"/>
  </g>
  <line x1="680" y1="333.5" x2="680" y2="377.5" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M680,390.5 L673.5,376.5 L686.5,376.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <g opacity="1">
  <ellipse cx="636" cy="522" rx="12" ry="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="632" cy="519" rx="4" ry="3" fill="#c4ccd4"/>
  </g>
  <line x1="680" y1="484" x2="680" y2="547" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M680,560 L673.5,546 L686.5,546 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="606" cy="504" r="5" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="616" cy="488" r="4" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="660" cy="500" r="5" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="670" cy="514" r="4" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="646" cy="482" r="3.5" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5"/>
  <circle cx="596" cy="518" r="3.5" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5"/>
  <ellipse cx="636" cy="534" rx="24" ry="4.8" fill="none" stroke="#ffffff" stroke-width="3" stroke-opacity="0.9"/>
  <ellipse cx="636" cy="534" rx="40" ry="8" fill="none" stroke="#ffffff" stroke-width="3" stroke-opacity="0.6"/>
  <ellipse cx="636" cy="534" rx="56" ry="11.2" fill="none" stroke="#ffffff" stroke-width="3" stroke-opacity="0.35"/>
</svg>

## Ydinajatus

### Kiihtyvyys kertoo, miten nopeus muuttuu
Luvussa *Paikka, nopeus ja tasainen liike kuvaajina* nopeus pysyi vakiona. Useimmissa liikkeissä se kuitenkin muuttuu: auto lähtee liikennevaloista, pyöräilijä jarruttaa ja pudotettu kivi putoaa yhä nopeammin. **Kiihtyvyys** $a$ kertoo, kuinka paljon nopeus muuttuu aikayksikössä. Sen yksikkö on $\tfrac{\text{m/s}}{\text{s}} = \text{m/s}^2$. Kiihtyvyys $2{,}0\,\text{m/s}^2$ tarkoittaa, että nopeus kasvaa joka sekunti $2{,}0\,\text{m/s}$.

Kiihtyvyys on vektorisuure $\overline{a}$ kuten nopeus $\overline{v}$, ja suoraviivaisessa liikkeessä sen suunta ilmoitetaan etumerkillä. Kun kiihtyvyys ja nopeus ovat samansuuntaiset, vauhti kasvaa. Kun ne ovat vastakkaissuuntaiset, vauhti pienenee. Negatiivinen kiihtyvyys ei siis aina tarkoita hidastumista: jos kappale liikkuu negatiiviseen suuntaan ja $a < 0$, sen vauhti kasvaa. Kiihtyvyys voi olla olemassa silloinkin, kun nopeus on hetken nolla.

<svg data-fig="strobe" viewBox="0 0 600 368" role="img" aria-label="Kaavakuva kahdesta kärrystä, jotka on kuvattu yhden sekunnin välein, välit mittakaavassa. Ylhäällä kärry lähtee levosta ja kiihtyy: välit kasvavat, sininen nopeusnuoli pitenee joka sekunti yhtä paljon ja oranssi kiihtyvyysnuoli osoittaa liikkeen suuntaan ja pysyy samanpituisena. Alhaalla kärry hidastuu: välit lyhenevät, nopeusnuoli lyhenee ja kiihtyvyysnuoli osoittaa liikettä vastaan; viimeisessä kuvassa kärry on hetken paikallaan, mutta kiihtyvyysnuoli on yhä sama." style="max-width:100%;font-size:24px">
  <foreignObject x="24" y="9.5" width="357" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kiihtyvä liike}\text{, kuvat } 1\,\text{s} \text{ välein}$</div></foreignObject>
  <rect x="24" y="140" width="552" height="10" fill="#f1dfb5"/>
  <line x1="24" y1="140" x2="576" y2="140" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <g opacity="0.45">
  <rect x="28" y="110" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="40" y="100" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="38" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="38" cy="132" r="2.5" fill="#c4ccd4"/>
  <circle cx="62" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="62" cy="132" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="32" y1="170" x2="56" y2="170" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M68,170 L55,176 L55,164 Z" fill="#e8590c" stroke-linejoin="round"/>
  <g opacity="0.633333">
  <rect x="78" y="110" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="90" y="100" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="88" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="88" cy="132" r="2.5" fill="#c4ccd4"/>
  <circle cx="112" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="112" cy="132" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="100" y1="84" x2="112" y2="84" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M125,84 L111,90.5 L111,77.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="82" y1="170" x2="106" y2="170" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M118,170 L105,176 L105,164 Z" fill="#e8590c" stroke-linejoin="round"/>
  <g opacity="0.816667">
  <rect x="228" y="110" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="240" y="100" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="238" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="238" cy="132" r="2.5" fill="#c4ccd4"/>
  <circle cx="262" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="262" cy="132" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="250" y1="84" x2="287" y2="84" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,84 L286,90.5 L286,77.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="232" y1="170" x2="256" y2="170" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M268,170 L255,176 L255,164 Z" fill="#e8590c" stroke-linejoin="round"/>
  <g opacity="1">
  <rect x="478" y="110" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="490" y="100" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="488" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="488" cy="132" r="2.5" fill="#c4ccd4"/>
  <circle cx="512" cy="132" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="512" cy="132" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="500" y1="84" x2="562" y2="84" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M575,84 L561,90.5 L561,77.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="482" y1="170" x2="506" y2="170" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M518,170 L505,176 L505,164 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="521" y="41.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="526" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="24" y="191.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hidastuva liike}\text{, kuvat } 1\,\text{s} \text{ välein}$</div></foreignObject>
  <rect x="24" y="322" width="552" height="10" fill="#f1dfb5"/>
  <line x1="24" y1="322" x2="576" y2="322" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <g opacity="0.45">
  <rect x="28" y="292" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="40" y="282" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="38" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="38" cy="314" r="2.5" fill="#c4ccd4"/>
  <circle cx="62" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="62" cy="314" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="50" y1="266" x2="112" y2="266" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M125,266 L111,272.5 L111,259.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="68" y1="352" x2="44" y2="352" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M32,352 L45,346 L45,358 Z" fill="#e8590c" stroke-linejoin="round"/>
  <g opacity="0.633333">
  <rect x="278" y="292" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="290" y="282" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="288" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="288" cy="314" r="2.5" fill="#c4ccd4"/>
  <circle cx="312" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="312" cy="314" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="300" y1="266" x2="337" y2="266" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M350,266 L336,272.5 L336,259.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="318" y1="352" x2="294" y2="352" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M282,352 L295,346 L295,358 Z" fill="#e8590c" stroke-linejoin="round"/>
  <g opacity="0.816667">
  <rect x="428" y="292" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="440" y="282" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="438" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="438" cy="314" r="2.5" fill="#c4ccd4"/>
  <circle cx="462" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="462" cy="314" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="450" y1="266" x2="462" y2="266" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M475,266 L461,272.5 L461,259.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="468" y1="352" x2="444" y2="352" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M432,352 L445,346 L445,358 Z" fill="#e8590c" stroke-linejoin="round"/>
  <g opacity="1">
  <rect x="478" y="292" width="44" height="18" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="490" y="282" width="20" height="10" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="488" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="488" cy="314" r="2.5" fill="#c4ccd4"/>
  <circle cx="512" cy="314" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="512" cy="314" r="2.5" fill="#c4ccd4"/>
  </g>
  <line x1="518" y1="352" x2="494" y2="352" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M482,352 L495,346 L495,358 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="71" y="223.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="76" y="337.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="24" y1="196" x2="576" y2="196" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
</svg>

### Tasaisesti kiihtyvä liike ja $(t,v)$-kuvaaja
Liike on **tasaisesti kiihtyvää**, kun kiihtyvyys pysyy vakiona: nopeus muuttuu yhtä paljon jokaisessa yhtä pitkässä aikavälissä. Silloin **$(t,v)$-kuvaaja**, jossa vaaka-akselilla on aika ja pystyakselilla nopeus, on suora. Suoran kulmakerroin on kiihtyvyys. Nouseva suora tarkoittaa positiivista kiihtyvyyttä, vaakasuora tasaista liikettä ja laskeva suora negatiivista kiihtyvyyttä.

<svg data-fig="tv-graph" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kahdesta (t,v)-kuvaajasta, ei lukuarvoja. Vasemmalla suora nousee alkunopeudesta v0, ja suoralta valitut kaksi pistettä rajaavat kolmion: aikaväli Δt ja nopeuden muutos Δv, joiden suhde on kiihtyvyys a. Oikealla kolme suoraa samasta alkunopeudesta: nouseva suora on kiihtyvyys a suurempi kuin nolla, vaakasuora suora kiihtyvyys nolla eli tasainen liike ja laskeva suora kiihtyvyys pienempi kuin nolla." style="max-width:100%;font-size:24px">
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
  <foreignObject x="510" y="88.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$a > 0$</div></foreignObject>
  <polyline points="360,180 500,180" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="165.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <polyline points="360,180 500,257" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="242.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a < 0$</div></foreignObject>
  <circle cx="360" cy="180" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="317" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
</svg>

### Hetkellinen nopeus on tangentin kulmakerroin
Kun nopeus kasvaa, paikka muuttuu jokaisessa sekunnissa enemmän kuin edellisessä. Siksi $(t,x)$-kuvaaja ei ole suora vaan käyrä, joka jyrkkenee. Nopeus tietyllä hetkellä eli **hetkellinen nopeus** saadaan käyrän tangentista: suorasta, joka sivuaa käyrää kyseisessä pisteessä. Tangentilta valitaan kaksi kaukana toisistaan olevaa pistettä, ja hetkellinen nopeus on niiden välinen paikan muutos jaettuna ajan muutoksella. Kahden käyrän pisteen kautta laskettu suhde antaisi vain keskinopeuden niiden välillä.

<svg data-fig="tangent" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva (t,x)-kuvaajasta, ei lukuarvoja. Levosta kiihtyvän kärryn kuvaaja on ylöspäin kaartuva käyrä, joka jyrkkenee koko ajan. Käyrän pisteeseen P on piirretty katkoviivana tangentti eli suora, joka sivuaa käyrää siinä kohdassa. Tangentilta on valittu kaksi kaukana toisistaan olevaa pistettä, ja niiden aikaväli Δt ja paikan muutos Δx muodostavat kolmion. Tangentin kulmakerroin Δx jaettuna Δt:llä on kärryn hetkellinen nopeus hetkellä, jota P vastaa." style="max-width:100%;font-size:24px">
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

### Vapaa pudotus
Kun ilmanvastus on pieni, kaikki kappaleet putoavat samalla kiihtyvyydellä massasta riippumatta. Tämä **putoamiskiihtyvyys** on Maan pinnalla $g = 9{,}81\,\text{m/s}^2$ ja suunnattu alaspäin. Pudotetun kiven nopeus kasvaa siis joka sekunti noin $9{,}8\,\text{m/s}$. Siksi kivi kulkee jokaisessa sekunnissa pidemmän matkan kuin edellisessä: levosta lähtevän kappaleen peräkkäisinä yhtä pitkinä aikaväleinä kulkemat matkat suhtautuvat kuin $1 : 3 : 5 : 7$.

## Kaava: Tasaisesti kiihtyvän liikkeen yhtälöt
Kiihtyvyys on nopeuden muutos jaettuna siihen kuluneella ajalla:
```latex
a = \frac{\Delta v}{\Delta t}
```
missä $a$ on kiihtyvyys ($\text{m/s}^2$), $\Delta v = v_2 - v_1$ nopeuden muutos ($\text{m/s}$) ja $\Delta t$ siihen kulunut aika ($\text{s}$). Kun kiihtyvyys on vakio ja ajanotto alkaa hetkestä $t = 0$, jolloin nopeus on $v_0$, nopeus kasvaa joka sekunti määrän $a$:
```latex
v = v_0 + a\,t
```
missä $v$ on nopeus hetkellä $t$ ($\text{m/s}$), $v_0$ alkunopeus ($\text{m/s}$), $a$ kiihtyvyys ($\text{m/s}^2$) ja $t$ aika ($\text{s}$).

### Siirtymä on $(t,v)$-kuvaajan alle jäävä pinta-ala
Tasaisessa liikkeessä siirtymä $v\,t$ on $(t,v)$-kuvaajan alle jäävän suorakulmion pinta-ala. Sama pätee, kun nopeus muuttuu: siirtymä on kuvaajan ja aika-akselin väliin jäävä pinta-ala. Tasaisesti kiihtyvässä liikkeessä alue jakautuu suorakulmioon, jonka ala on $v_0\,t$, ja kolmioon, jonka korkeus on nopeuden kasvu $a\,t$ ja leveys $t$. Kolmion ala on $\tfrac{1}{2} \cdot a\,t \cdot t = \tfrac{1}{2}\,a\,t^2$.

<svg data-fig="area" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva (t,v)-kuvaajasta, ei lukuarvoja. Nopeus kasvaa suoraviivaisesti alkunopeudesta v0 hetkellä 0 nopeuteen v hetkellä t. Suoran alle jäävä alue on jaettu kahteen osaan: sininen suorakulmio, jonka korkeus on v0 ja leveys t, ja oranssi kolmio sen päällä, jonka korkeus on nopeuden kasvu at ja leveys t. Suorakulmion ala on v0 kertaa t ja kolmion ala puolet a t:n ja t:n tulosta; yhdessä ne ovat siirtymä Δx." style="max-width:100%;font-size:24px">
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

Kun kappale on hetkellä $t = 0$ paikassa $x_0$, sen paikka on alkupaikka plus siirtymä:
```latex
x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
```
missä $x$ on paikka hetkellä $t$ ($\text{m}$) ja $x_0$ alkupaikka ($\text{m}$); muut symbolit ovat samat kuin edellä. Kun kysytään aikaa, tästä tulee toisen asteen yhtälö, jonka ratkaisuista valitaan se, joka sopii tilanteeseen.

### Putoamiskiihtyvyyden määrittäminen mittauksista
Putoavan kappaleen paikka mitataan monella hetkellä esimerkiksi videolta tai valoporteilla. Mittauspisteisiin sovitetaan toisen asteen polynomi $s = A\,t^2 + B\,t + C$ laskimella tai taulukkolaskennalla. Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen samalla käyrällä mittausepävarmuuden vuoksi, joten sovitus käyttää kaikkia pisteitä yhtä aikaa. Kun polynomia verrataan paikan yhtälöön, $t^2$:n kertoimet ovat samat, $A = \tfrac{1}{2}\,a$:
```latex
a = 2A
```
missä $A$ on sovitetun polynomin $t^2$-termin kerroin ($\text{m/s}^2$). Kerroin $B$ on alkunopeus ja $C$ alkupaikka.

## Esimerkki
Pyöräilijä tulee mäen alkuun nopeudella $4{,}0\,\text{m/s}$ ja lakkaa polkemasta. Alamäessä hänen kiihtyvyytensä on $0{,}50\,\text{m/s}^2$, ja mäkeä on $60\,\text{m}$. Kuinka kauan alamäen laskeminen kestää, ja mikä on nopeus mäen alla?

<!-- vaihe -->

**Tunnetut ja kysytty.** Alkunopeus $v_0 = 4{,}0\,\text{m/s}$, kiihtyvyys $a = 0{,}50\,\text{m/s}^2$ ja siirtymä $\Delta x = x - x_0 = 60\,\text{m}$ liikkeen suuntaan, joka valitaan positiiviseksi. Kysytään aikaa $t$ ja nopeutta $v$ mäen alla.

<!-- vaihe -->

**Periaate.** Kiihtyvyys on vakio, joten liike on tasaisesti kiihtyvää ja siirtymä on $\Delta x = v_0\,t + \tfrac{1}{2}\,a\,t^2$. Aika on tuntematon, ja se esiintyy sekä ensimmäisessä että toisessa potenssissa, joten saadaan toisen asteen yhtälö. Kun aika tiedetään, nopeus saadaan yhtälöstä $v = v_0 + a\,t$.

<!-- vaihe -->

**Kaava ratkaistuna.** Kirjoitetaan yhtälö muotoon $\tfrac{1}{2}\,a\,t^2 + v_0\,t - \Delta x = 0$ ja ratkaistaan se toisen asteen yhtälön ratkaisukaavalla. Positiivinen ratkaisu on
```latex
t = \frac{-v_0 + \sqrt{v_0^2 + 2a\,\Delta x}}{a}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Kaikki suureet ovat SI-yksiköissä (m, m/s, m/s²), joten muunnoksia ei tarvita. Juuren alla $\text{m}^2/\text{s}^2$, joten juuri on yksikössä $\text{m/s}$ ja aika sekunteina.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin juuren alla oleva lauseke ja sen neliöjuuri, sitten aika ja nopeus:
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

**Tulos.** Alamäen laskeminen kestää noin $9{,}4\,\text{s}$, ja nopeus mäen alla on noin $8{,}7\,\text{m/s}$. Kaksi merkitsevää numeroa, kuten alkunopeudessa $4{,}0\,\text{m/s}$, kiihtyvyydessä $0{,}50\,\text{m/s}^2$ ja matkassa $60\,\text{m}$. Ratkaisukaavan toinen ratkaisu $t \approx -25\,\text{s}$ hylätään, koska liike alkaa hetkellä $t = 0$.

<!-- vaihe -->

**Järkevyys.** Nopeus kasvaa tasaisesti, joten keskinopeus on alku- ja loppunopeuden keskiarvo $\tfrac{4{,}0\,\text{m/s} + 8{,}72\,\text{m/s}}{2} \approx 6{,}36\,\text{m/s}$, ja $6{,}36\,\text{m/s} \cdot 9{,}44\,\text{s} \approx 60\,\text{m}$, eli mäen pituus. Loppunopeus $8{,}7\,\text{m/s} \approx 31\,\text{km/h}$ on alamäessä tavallinen pyöräilyvauhti.

## Yleinen virhekäsitys
Moni ajattelee, että kiihtyvyys on nolla aina, kun nopeus on nolla. Ylös heitetty pallo on lakipisteessä hetken paikallaan, mutta sen nopeus muuttuu koko ajan: juuri ennen lakipistettä se liikkuu ylöspäin ja heti sen jälkeen alaspäin. Kiihtyvyys on koko lennon ajan $g = 9{,}81\,\text{m/s}^2$ alaspäin. Toinen virhe on pitää negatiivista kiihtyvyyttä aina hidastumisena: vauhti pienenee vain, kun kiihtyvyys ja nopeus ovat vastakkaissuuntaiset. Kolmas virhe on ajatella, että raskas kappale putoaa nopeammin kuin kevyt. Kun ilmanvastus on pieni, molemmat putoavat samalla kiihtyvyydellä.

## Tiivistelmä
- Kiihtyvyys $a = \tfrac{\Delta v}{\Delta t}$ kertoo nopeuden muutoksen aikayksikössä, yksikkö $\text{m/s}^2$. Se on vektorisuure, ja suoralla etumerkki kertoo suunnan.
- Vauhti kasvaa, kun kiihtyvyys ja nopeus ovat samansuuntaiset, ja pienenee, kun ne ovat vastakkaissuuntaiset.
- Tasaisesti kiihtyvässä liikkeessä $(t,v)$-kuvaaja on suora, jonka kulmakerroin on kiihtyvyys ja jonka alle jäävä pinta-ala on siirtymä.
- $v = v_0 + a\,t$ ja $x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$. $(t,x)$-kuvaaja on käyrä, ja hetkellinen nopeus on sen tangentin kulmakerroin.
- Vapaassa pudotuksessa kiihtyvyys on $g = 9{,}81\,\text{m/s}^2$ alaspäin. Sen voi määrittää sovittamalla mittauspisteisiin toisen asteen polynomin: $a = 2A$.
