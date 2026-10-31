# Paikka, nopeus ja tasainen liike kuvaajina

> **Miksi** pyöräilijän kuljettu matka voi olla neljä kilometriä, vaikka hänen siirtymänsä on nolla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: järvi metsän keskellä nähtynä vinosti ylhäältä. Järven ympäri kiertää hiekkapolku. Polun lähtöpaikalla on lippu ja lähtöviiva. Etualalla pyöräilijä ajaa polkua kohti lähtöpaikkaa. Hän on kiertänyt järven ympäri. Polun nuolet näyttävät kiertosuunnan." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy41h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy41h-grass" gradientUnits="userSpaceOnUse" x1="0" y1="226" x2="0" y2="600"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#f1dfb5"/></linearGradient><linearGradient id="fy41h-lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="200" fill="url(#fy41h-sky)"/>
  <path d="M157,84 Q155.5,60 183.5,63 Q195,38 223,46 Q248,32 262,59 Q287,61.5 284.5,84 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M930.5,61 Q929.5,42.5 951.5,44.5 Q960,24.5 982,31.5 Q1002,20.5 1013,41 Q1033,43.5 1030.5,61 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,150 Q100,123 200,148 Q300,117 400,149.5 Q500,122 600,148.5 Q700,98 800,153 Q900,109.5 1000,151 Q1100,97.5 1200,153.5 Q1300,106.5 1400,151.5 V600 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M0,186 Q100,158.5 200,183.5 Q300,140.5 400,188.5 Q500,144.5 600,186.5 Q700,164.5 800,182.5 Q900,167.5 1000,183 Q1100,161.5 1200,184 Q1300,150.5 1400,190 V600 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M0,196 L8,179.5 L16,196 L25,178 L33.5,196 L42,178.5 L50.5,196 L63.5,165.5 L76.5,196 L85.5,177 L94.5,196 L103.5,177 L112.5,196 L124.5,168 L137,196 L150.5,163.5 L164.5,196 L176.5,168 L189,196 L203,162.5 L217,196 L230.5,164.5 L244,196 L255,171 L266.5,196 L280,163.5 L294,196 L305,171 L316.5,196 L326,174.5 L336,196 L348,168 L360.5,196 L371.5,170.5 L383,196 L393.5,172 L404.5,196 L412.5,180 L420.5,196 L434,164 L447.5,196 L461.5,163 L475.5,196 L487,169 L499,196 L512,166 L524.5,196 L536.5,169 L548,196 L561,166.5 L574,196 L587,165.5 L600,196 L610,175 L619.5,196 L628.5,177.5 L637.5,196 L651.5,163 L665,196 L679.5,162 L693.5,196 L705.5,168.5 L717.5,196 L731.5,163.5 L745.5,196 L757,169.5 L768.5,196 L780.5,168 L793,196 L805,168.5 L816.5,196 L826,176.5 L835,196 L848,166 L861,196 L874.5,164.5 L887.5,196 L901.5,163 L915.5,196 L925,175.5 L934.5,196 L942.5,179.5 L950.5,196 L964,164.5 L977.5,196 L988,172 L999,196 L1007,179 L1015.5,196 L1024.5,176.5 L1034,196 L1047.5,164 L1061,196 L1073.5,166.5 L1086,196 L1094.5,179.5 L1102.5,196 L1113,172.5 L1123.5,196 L1137,164.5 L1150.5,196 L1163.5,165 L1176.5,196 L1187,174 L1197,196 L1209.5,167 L1222,196 V216 H0 Z" fill="#6c757d" stroke-linejoin="round"/>
  <path d="M0,216 L11.5,190.5 L23.5,216 L40,176.5 L57,216 L67.5,193.5 L78,216 L89,193 L100,216 L109,197.5 L118.5,216 L128,196.5 L137.5,216 L151.5,185 L165,216 L181,179 L197,216 L210.5,186 L223.5,216 L233.5,196.5 L243,216 L257,184.5 L271,216 L282,193 L292.5,216 L305.5,187 L318.5,216 L328.5,195.5 L338.5,216 L349.5,193.5 L360.5,216 L374.5,183.5 L388.5,216 L401.5,187 L414.5,216 L431.5,176 L448.5,216 L463.5,182 L478,216 L494,179.5 L509.5,216 L526,176.5 L543,216 L554,193 L564.5,216 L578.5,185 L592.5,216 L608.5,177 L625,216 L639.5,183 L654,216 L669.5,180 L685,216 L694,198 L703,216 L719.5,177.5 L736,216 L751.5,179 L767.5,216 L783,179.5 L798.5,216 L813,183.5 L827.5,216 L839.5,190 L851,216 L864,187.5 L877,216 L888.5,191 L900,216 L915,181 L930,216 L939.5,196 L949.5,216 L963,186 L976.5,216 L985.5,197.5 L995,216 L1010,182 L1024.5,216 L1039,183.5 L1053,216 L1062.5,197.5 L1071.5,216 L1088.5,176 L1105.5,216 L1117,190.5 L1129,216 L1144.5,179 L1160.5,216 L1176,179.5 L1191.5,216 L1202,194.5 L1212.5,216 V228 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="226" width="1200" height="374" fill="url(#fy41h-grass)"/>
  <ellipse cx="600" cy="360" rx="500" ry="168" fill="#d9b26a" stroke="#a97a35" stroke-width="3"/>
  <ellipse cx="600" cy="360" rx="452" ry="132" fill="#b2f2bb" stroke="#a97a35" stroke-width="3"/>
  <circle cx="1072.5" cy="360" r="2.18328" fill="#a97a35"/>
  <circle cx="1073.5" cy="370.5" r="2.16153" fill="#a97a35"/>
  <circle cx="1068" cy="380.5" r="3.35639" fill="#a97a35"/>
  <circle cx="1072" cy="391.5" r="2.81224" fill="#a97a35"/>
  <circle cx="1059.5" cy="401.5" r="3.18638" fill="#a97a35"/>
  <circle cx="1053.5" cy="412" r="2.56828" fill="#a97a35"/>
  <circle cx="1037.5" cy="421.5" r="3.11917" fill="#a97a35"/>
  <circle cx="1015" cy="429.5" r="2.08561" fill="#a97a35"/>
  <circle cx="1008.5" cy="440.5" r="3.25867" fill="#a97a35"/>
  <circle cx="979.5" cy="447" r="3.40278" fill="#a97a35"/>
  <circle cx="962" cy="455.5" r="2.22068" fill="#a97a35"/>
  <circle cx="945" cy="465" r="3.37245" fill="#a97a35"/>
  <circle cx="920" cy="472" r="2.14981" fill="#a97a35"/>
  <circle cx="889.5" cy="476.5" r="2.79276" fill="#a97a35"/>
  <circle cx="862.5" cy="482.5" r="3.36054" fill="#a97a35"/>
  <circle cx="835.5" cy="488.5" r="2.84886" fill="#a97a35"/>
  <circle cx="808.5" cy="495" r="3.04284" fill="#a97a35"/>
  <circle cx="778" cy="499" r="3.24251" fill="#a97a35"/>
  <circle cx="745.5" cy="501" r="3.08356" fill="#a97a35"/>
  <circle cx="713.5" cy="503" r="3.47453" fill="#a97a35"/>
  <circle cx="681.5" cy="506" r="2.32569" fill="#a97a35"/>
  <circle cx="650" cy="510" r="3.01261" fill="#a97a35"/>
  <circle cx="617" cy="511.5" r="2.25274" fill="#a97a35"/>
  <circle cx="583.5" cy="508.5" r="2.11039" fill="#a97a35"/>
  <circle cx="551" cy="507.5" r="2.93836" fill="#a97a35"/>
  <circle cx="518.5" cy="505.5" r="3.13812" fill="#a97a35"/>
  <circle cx="483" cy="508" r="3.19647" fill="#a97a35"/>
  <circle cx="455" cy="500.5" r="2.26381" fill="#a97a35"/>
  <circle cx="420" cy="500.5" r="2.47518" fill="#a97a35"/>
  <circle cx="392" cy="494.5" r="2.41843" fill="#a97a35"/>
  <circle cx="360" cy="491" r="2.03854" fill="#a97a35"/>
  <circle cx="331" cy="486" r="2.35837" fill="#a97a35"/>
  <circle cx="307" cy="478" r="2.76829" fill="#a97a35"/>
  <circle cx="285" cy="470" r="2.63295" fill="#a97a35"/>
  <circle cx="259" cy="464" r="2.75349" fill="#a97a35"/>
  <circle cx="233" cy="457" r="3.10068" fill="#a97a35"/>
  <circle cx="209.5" cy="449.5" r="2.41606" fill="#a97a35"/>
  <circle cx="201" cy="438.5" r="3.3989" fill="#a97a35"/>
  <circle cx="177.5" cy="431" r="2.141" fill="#a97a35"/>
  <circle cx="167" cy="420.5" r="2.71535" fill="#a97a35"/>
  <circle cx="154.5" cy="411" r="2.56303" fill="#a97a35"/>
  <circle cx="140" cy="401.5" r="2.75215" fill="#a97a35"/>
  <circle cx="141" cy="390.5" r="3.00212" fill="#a97a35"/>
  <circle cx="135.5" cy="380.5" r="2.14584" fill="#a97a35"/>
  <circle cx="129.5" cy="370.5" r="2.43241" fill="#a97a35"/>
  <circle cx="125.5" cy="360" r="2.22089" fill="#a97a35"/>
  <circle cx="128.5" cy="349.5" r="2.04251" fill="#a97a35"/>
  <circle cx="130.5" cy="339" r="2.02217" fill="#a97a35"/>
  <circle cx="136" cy="329" r="2.86257" fill="#a97a35"/>
  <circle cx="140.5" cy="318.5" r="2.60697" fill="#a97a35"/>
  <circle cx="155.5" cy="309" r="3.19944" fill="#a97a35"/>
  <circle cx="165" cy="299" r="3.1832" fill="#a97a35"/>
  <circle cx="178.5" cy="289.5" r="3.18349" fill="#a97a35"/>
  <circle cx="195" cy="280.5" r="2.07953" fill="#a97a35"/>
  <circle cx="210" cy="271" r="3.19716" fill="#a97a35"/>
  <circle cx="232.5" cy="263" r="3.40616" fill="#a97a35"/>
  <circle cx="262" cy="257" r="2.03292" fill="#a97a35"/>
  <circle cx="280" cy="248" r="3.12135" fill="#a97a35"/>
  <circle cx="306.5" cy="241.5" r="2.98842" fill="#a97a35"/>
  <circle cx="329.5" cy="233.5" r="3.01336" fill="#a97a35"/>
  <circle cx="363" cy="230.5" r="2.65217" fill="#a97a35"/>
  <circle cx="394.5" cy="227" r="2.45301" fill="#a97a35"/>
  <circle cx="419.5" cy="219" r="2.4002" fill="#a97a35"/>
  <circle cx="450.5" cy="215" r="3.13542" fill="#a97a35"/>
  <circle cx="483.5" cy="212.5" r="2.06309" fill="#a97a35"/>
  <circle cx="516.5" cy="211" r="2.27766" fill="#a97a35"/>
  <circle cx="550.5" cy="211.5" r="3.44887" fill="#a97a35"/>
  <circle cx="583" cy="208.5" r="2.60565" fill="#a97a35"/>
  <circle cx="617" cy="208.5" r="2.25837" fill="#a97a35"/>
  <circle cx="650.5" cy="209" r="3.46079" fill="#a97a35"/>
  <circle cx="681.5" cy="214.5" r="2.94704" fill="#a97a35"/>
  <circle cx="714.5" cy="215.5" r="3.35592" fill="#a97a35"/>
  <circle cx="747" cy="217.5" r="2.77619" fill="#a97a35"/>
  <circle cx="780" cy="219.5" r="2.17709" fill="#a97a35"/>
  <circle cx="811.5" cy="223.5" r="3.26843" fill="#a97a35"/>
  <circle cx="837" cy="230.5" r="2.41472" fill="#a97a35"/>
  <circle cx="866.5" cy="235.5" r="2.36924" fill="#a97a35"/>
  <circle cx="896" cy="240.5" r="2.0645" fill="#a97a35"/>
  <circle cx="917.5" cy="249" r="2.20148" fill="#a97a35"/>
  <circle cx="942" cy="256" r="2.0011" fill="#a97a35"/>
  <circle cx="959" cy="265" r="2.74428" fill="#a97a35"/>
  <circle cx="984.5" cy="272" r="2.04688" fill="#a97a35"/>
  <circle cx="1007.5" cy="280" r="2.95071" fill="#a97a35"/>
  <circle cx="1022" cy="289.5" r="3.09768" fill="#a97a35"/>
  <circle cx="1032" cy="299.5" r="2.7221" fill="#a97a35"/>
  <circle cx="1048.5" cy="308.5" r="3.39544" fill="#a97a35"/>
  <circle cx="1064" cy="318" r="2.44897" fill="#a97a35"/>
  <circle cx="1065.5" cy="329" r="2.11653" fill="#a97a35"/>
  <circle cx="1070.5" cy="339" r="3.46653" fill="#a97a35"/>
  <circle cx="1068" cy="349.5" r="3.36811" fill="#a97a35"/>
  <ellipse cx="600" cy="354" rx="420" ry="112" fill="#f1dfb5"/>
  <ellipse cx="600" cy="352" rx="400" ry="100" fill="url(#fy41h-lake)" stroke="#2f74b5" stroke-width="3"/>
  <path d="M360,320 q27.5,-6 55.0,0 t55.0,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M560,300 q35.0,-6 70.0,0 t70.0,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M760,340 q30.0,-6 60.0,0 t60.0,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M480,380 q22.5,-6 45.0,0 t45.0,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M690,395 q25.0,-6 50.0,0 t50.0,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <line x1="250" y1="352" x2="246" y2="318" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="246" cy="318" rx="4" ry="10" fill="#b8622d"/>
  <line x1="264" y1="370" x2="260" y2="336" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="260" cy="336" rx="4" ry="10" fill="#b8622d"/>
  <line x1="278" y1="388" x2="274" y2="354" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="274" cy="354" rx="4" ry="10" fill="#b8622d"/>
  <line x1="292" y1="352" x2="288" y2="318" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="288" cy="318" rx="4" ry="10" fill="#b8622d"/>
  <line x1="306" y1="370" x2="302" y2="336" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="302" cy="336" rx="4" ry="10" fill="#b8622d"/>
  <line x1="880" y1="388" x2="876" y2="354" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="876" cy="354" rx="4" ry="10" fill="#b8622d"/>
  <line x1="894" y1="352" x2="890" y2="318" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="890" cy="318" rx="4" ry="10" fill="#b8622d"/>
  <line x1="908" y1="370" x2="904" y2="336" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="904" cy="336" rx="4" ry="10" fill="#b8622d"/>
  <line x1="922" y1="388" x2="918" y2="354" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="918" cy="354" rx="4" ry="10" fill="#b8622d"/>
  <rect x="55.5" y="287" width="9" height="13" fill="#b8622d"/>
  <path d="M20.5,289 L60,245 L99.5,289 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M60,245 L99.5,289 H60 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M29,265 L60,221 L91,265 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M60,221 L91,265 H60 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M38,240.5 L60,190 L82,240.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M60,190 L82,240.5 H60 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="125" y="314.5" width="10.5" height="15.5" fill="#b8622d"/>
  <path d="M83,317 L130,265 L177,317 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M130,265 L177,317 H130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M93.5,288.5 L130,236.5 L166.5,288.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M130,236.5 L166.5,288.5 H130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M104,260 L130,200 L156,260 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M130,200 L156,260 H130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1075.5" y="287" width="9" height="13" fill="#b8622d"/>
  <path d="M1040.5,289 L1080,245 L1119.5,289 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1080,245 L1119.5,289 H1080 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1049,265 L1080,221 L1111,265 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1080,221 L1111,265 H1080 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1058,240.5 L1080,190 L1102,240.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1080,190 L1102,240.5 H1080 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1144.5" y="323" width="11" height="17" fill="#b8622d"/>
  <path d="M1099.5,326 L1150,270 L1200.5,326 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,270 L1200.5,326 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1111,295 L1150,239 L1189,295 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,239 L1189,295 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1122,264.5 L1150,200 L1178,264.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,200 L1178,264.5 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="33" y="449.5" width="13.5" height="20.5" fill="#b8622d"/>
  <path d="M-21,453 L40,385 L101,453 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M40,385 L101,453 H40 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M-7.5,415.5 L40,347.5 L87.5,415.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M40,347.5 L87.5,415.5 H40 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M6,378 L40,300 L74,378 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M40,300 L74,378 H40 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1123" y="478.5" width="14.5" height="21.5" fill="#b8622d"/>
  <path d="M1065,482 L1130,410 L1195,482 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1130,410 L1195,482 H1130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1079.5,442.5 L1130,370.5 L1180.5,442.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1130,370.5 L1180.5,442.5 H1130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1094,403 L1130,320 L1166,403 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1130,320 L1166,403 H1130 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="197" y="260.5" width="6.5" height="9.5" fill="#b8622d"/>
  <path d="M171,262 L200,230 L229,262 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,230 L229,262 H200 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M177.5,244.5 L200,212.5 L222.5,244.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,212.5 L222.5,244.5 H200 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M184,227 L200,190 L216,227 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,190 L216,227 H200 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="977" y="252.5" width="6.5" height="9.5" fill="#b8622d"/>
  <path d="M951,254 L980,222 L1009,254 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M980,222 L1009,254 H980 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M957.5,236.5 L980,204.5 L1002.5,236.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M980,204.5 L1002.5,236.5 H980 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M964,219 L980,182 L996,219 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M980,182 L996,219 H980 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="327.5" y="223" width="5" height="7" fill="#b8622d"/>
  <path d="M308.5,224 L330,200 L351.5,224 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M330,200 L351.5,224 H330 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M313,211 L330,187 L347,211 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M330,187 L347,211 H330 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M318,197.5 L330,170 L342,197.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M330,170 L342,197.5 H330 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="857.5" y="224.5" width="5" height="7.5" fill="#b8622d"/>
  <path d="M837,225.5 L860,200 L883,225.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M860,200 L883,225.5 H860 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M842,211.5 L860,186 L878,211.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M860,186 L878,211.5 H860 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M847,197.5 L860,168 L873,197.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M860,168 L873,197.5 H860 Z" fill="#1f2933" fill-opacity="0.18"/>
  <line x1="780" y1="499" x2="735" y2="504" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M720.5,505.5 L735.5,496.5 L737,511 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="218.5" y1="451" x2="179" y2="430.5" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M165.5,423.5 L183,424.5 L176.5,437 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="169.5" y1="294" x2="209.5" y2="274" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M223,267 L212,280.5 L205.5,268 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="516.5" y1="212" x2="561.5" y2="210.5" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M576.5,210 L561,217.5 L560.5,203.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="908.5" y1="245" x2="951.5" y2="258.5" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M966,263 L948.5,265.5 L953,251.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M594,488 L606,532" fill="none" stroke="#ffffff" stroke-width="10" stroke-linejoin="round"/>
  <line x1="620" y1="540" x2="620" y2="420" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <path d="M620,420 Q660,406 696,428 Q660,446 620,450 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <ellipse cx="620" cy="540" rx="18" ry="6" fill="#a97a35"/>
  <g transform="translate(1760,0) scale(-1,1)">
  <circle cx="780" cy="492" r="40" fill="none" stroke="#1f2933" stroke-width="6"/>
  <circle cx="780" cy="492" r="36" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="780" y1="492" x2="814.5" y2="492" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="810" y2="509" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="797" y2="522" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="780" y2="526.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="763" y2="522" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="750" y2="509" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="745.5" y2="492" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="750" y2="475" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="763" y2="462" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="780" y2="457.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="797" y2="462" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="492" x2="810" y2="475" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="780" cy="492" r="3.6" fill="#1f2933"/>
  <circle cx="920" cy="492" r="40" fill="none" stroke="#1f2933" stroke-width="6"/>
  <circle cx="920" cy="492" r="36" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="920" y1="492" x2="954.5" y2="492" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="950" y2="509" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="937" y2="522" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="920" y2="526.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="903" y2="522" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="890" y2="509" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="885.5" y2="492" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="890" y2="475" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="903" y2="462" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="920" y2="457.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="937" y2="462" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="920" y1="492" x2="950" y2="475" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="920" cy="492" r="3.6" fill="#1f2933"/>
  <path d="M780,492 L830.5,492 L890.5,433 L820.5,433 Z" fill="none" stroke="#1971c2" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M830.5,492 L819,418" fill="none" stroke="#1971c2" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M890.5,433 L920,492" fill="none" stroke="#1971c2" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M890.5,433 L886.5,418" fill="none" stroke="#1971c2" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M802.5,418 H823.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M876.5,419 Q886.5,413.5 899,419" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="830.5" cy="492" r="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M813.5,412 L844.5,429 L839,500.5" fill="none" stroke="#1f2933" stroke-width="10.5" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M833,503 h11" fill="none" stroke="#6c757d" stroke-width="6.3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M809.5,415 L855.5,370" fill="none" stroke="#e8590c" stroke-width="15.4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M855.5,370 L886.5,416.5" fill="none" stroke="#e8590c" stroke-width="8.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="886.5" cy="416.5" r="4.2" fill="#f1dfb5"/>
  <circle cx="869.5" cy="359" r="10.5" fill="#f1dfb5"/>
  <path d="M857,358.5 Q861,343.5 875,345.5 Q883.5,349 881.5,356 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  </g>
</svg>

## Ydinajatus
Liikkeen kuvaaminen alkaa sopimuksesta. Valitaan suora, jota pitkin kappale liikkuu. Suoralle valitaan origo eli nollakohta ja positiivinen suunta. Tämä suora on $x$-akseli. **Paikka** $x$ kertoo, missä kappale on origoon nähden. Etumerkki kertoo, kummalla puolella kappale on. Paikka $x = -3\,\text{m}$ on kolme metriä origosta negatiiviseen suuntaan. Aika $t$ mitataan kellolla. Liike kuvataan kertomalla paikka jokaisella hetkellä.

Kappale voi siirtyä paikasta $x_1$ paikkaan $x_2$. Silloin sen **siirtymä** on paikan muutos $\Delta x = x_2 - x_1$. Siirtymä on vektorisuure. Vektorisuureella on suuruus ja suunta. Suoralla suunta kerrotaan etumerkillä. Plus tarkoittaa positiivista suuntaa ja miinus vastakkaista suuntaa. Siirtymä ei ole sama asia kuin kuljettu matka $s$. Matka on reitin pituus. Matka ei voi olla negatiivinen. Pyöräilijä voi ajaa kaupalle ja takaisin. Silloin matka on neljä kilometriä. Siirtymä on nolla, koska loppupaikka on sama kuin alkupaikka.

<svg data-fig="displacement" viewBox="0 0 600 392" role="img" aria-label="Kaavakuva kahdesta siirtymästä x-akselilla. Akseli on piirretty mittakaavassa. Ylhäällä kappale siirtyy paikasta x1 = 2 m paikkaan x2 = 8 m. Siirtymä on +6 m ja osoittaa oikealle. Alhaalla kappale siirtyy paikasta x1 = 8 m paikkaan x2 = 3 m. Siirtymä on −5 m ja osoittaa vasemmalle." style="max-width:100%;font-size:24px">
  <line x1="50" y1="104" x2="482" y2="104" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,104 L481,110 L481,98 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="100" x2="70" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="150" y1="100" x2="150" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="230" y1="100" x2="230" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="310" y1="100" x2="310" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="390" y1="100" x2="390" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="470" y1="100" x2="470" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="502" y="89.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="222.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\Delta x = +6\,\text{m}$</div></foreignObject>
  <line x1="150" y1="62" x2="371" y2="62" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M390,62 L370,71 L370,53 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="150" cy="104" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="390" cy="104" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="133.5" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="373.5" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
  <line x1="24" y1="198" x2="576" y2="198" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <line x1="50" y1="304" x2="482" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,304 L481,310 L481,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="300" x2="70" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="150" y1="300" x2="150" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="230" y1="300" x2="230" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="310" y1="300" x2="310" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="390" y1="300" x2="390" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="470" y1="300" x2="470" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="502" y="289.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="242.5" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\Delta x = -5\,\text{m}$</div></foreignObject>
  <line x1="390" y1="262" x2="209" y2="262" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M190,262 L210,253 L210,271 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="390" cy="304" r="9" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="190" cy="304" r="9" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="373.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="173.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
</svg>

<svg data-fig="round-trip" viewBox="0 0 600 322" role="img" aria-label="Kaavakuva, ei mittakaavassa. Pyöräilijä ajaa kotoa kauppaan, kaksi kilometriä, ja takaisin kotiin, toiset kaksi kilometriä. Kuljettu matka on s = 2 km + 2 km = 4 km. Loppupaikka on sama kuin alkupaikka, joten siirtymä on nolla." style="max-width:100%;font-size:24px">
  <line x1="50" y1="120" x2="468" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M480,120 L467,126 L467,114 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="116" x2="110" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="100" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="260" y1="116" x2="260" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="410" y1="116" x2="410" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="400" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="488" y="105.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{km})$</div></foreignObject>
  <rect x="90" y="96" width="40" height="24" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M84,96 L110,76 L136,96 Z" fill="#b8622d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="386" y="90" width="48" height="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="382" y="90" width="56" height="10" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="110" y1="64" x2="391" y2="64" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M410,64 L390,73 L390,55 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="175" y="15.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{menomatka } 2\,\text{km}$</div></foreignObject>
  <line x1="410" y1="184" x2="129" y2="184" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M110,184 L130,175 L130,193 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="168.5" y="199.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{paluumatka } 2\,\text{km}$</div></foreignObject>
  <line x1="24" y1="238" x2="576" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="196" y="251.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s = 2\,\text{km} + 2\,\text{km} = 4\,\text{km}$</div></foreignObject>
  <foreignObject x="233.5" y="285.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta x = x_2 - x_1 = 0$</div></foreignObject>
</svg>

**Nopeus** kertoo, kuinka nopeasti paikka muuttuu ja mihin suuntaan. Nopeus on myös vektorisuure. Sen etumerkki kertoo suunnan. Nopeuden itseisarvo $|v|$ on vauhti. Vauhti on nopeuden suuruus ilman etumerkkiä. Tasaisessa liikkeessä nopeus pysyy vakiona. Silloin paikka muuttuu yhtä paljon jokaisessa yhtä pitkässä aikavälissä.

Liike voidaan piirtää **$(t,x)$-kuvaajaksi**. Vaaka-akselilla on aika ja pystyakselilla paikka. Tasaisen liikkeen kuvaaja on suora. Suoran jyrkkyys eli kulmakerroin on nopeus. Jyrkempi suora tarkoittaa suurempaa nopeutta. Vaakasuora suora tarkoittaa, että kappale on paikallaan. Laskeva suora tarkoittaa liikettä negatiiviseen suuntaan. Kuvaaja ei ole kuva kappaleen reitistä. Nouseva viiva ei tarkoita ylämäkeä. Se tarkoittaa, että paikka kasvaa.

## Kaava: Keskinopeus ja tasaisen liikkeen yhtälö
Paikka voi muuttua määrän $\Delta x$ aikavälillä $\Delta t = t_2 - t_1$. Silloin keskinopeus on siirtymä jaettuna ajalla:
```latex
v_\text{ka} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}
```
missä $v_\text{ka}$ on keskinopeus (m/s), $\Delta x$ siirtymä (m), $\Delta t$ kulunut aika (s) ja $x_1$ ja $x_2$ paikat (m) hetkillä $t_1$ ja $t_2$. Vektorina nopeus kirjoitetaan $\overline{v}$ ja siirtymä $\Delta\overline{x}$. Suoralla käytetään niiden komponentteja $v$ ja $\Delta x$. Niiden etumerkki kertoo suunnan.

Tasaisessa liikkeessä keskinopeus on sama millä tahansa aikavälillä. Sitä kutsutaan nopeudeksi $v$. Epätasaisessa liikkeessä keskinopeus kertoo vain yhden asian. Se kertoo vakionopeuden, jolla sama siirtymä tehtäisiin samassa ajassa. Kappale voi olla hetkellä $t = 0$ paikassa $x_0$. Silloin kaavasta saadaan paikka ajan funktiona:
```latex
x = x_0 + v\,t
```
missä $x$ on paikka hetkellä $t$ (m), $x_0$ alkupaikka (m), $v$ nopeus (m/s) ja $t$ aika (s). Tämä on $(t,x)$-kuvaajan suoran yhtälö. Luku $x_0$ on kohta, jossa suora leikkaa paikka-akselin. Nopeus $v$ on suoran kulmakerroin.

<svg data-fig="graph-slope" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kahdesta (t,x)-kuvaajasta ilman lukuarvoja. Vasemmalla suora nousee alkupaikasta x0. Suoralta on valittu kaksi pistettä. Aikaväli Δt ja paikan muutos Δx muodostavat kolmion. Sen avulla nopeus v on Δx jaettuna Δt:lla. Oikealla on kolme suoraa samasta alkupaikasta. Nouseva suora on nopeus v suurempi kuin nolla. Vaakasuora suora on nopeus nolla. Laskeva suora on nopeus pienempi kuin nolla." style="max-width:100%;font-size:24px">
  <line x1="49" y1="290" x2="264" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M276,290 L263,296 L263,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="291" x2="50" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,44 L56,57 L44,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="282" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="40" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="50,246 250,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="110,206.5 210,206.5 210,140.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="50" cy="246" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="110" cy="206.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="210" cy="140.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="143.5" y="216" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="222" y="159" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta x$</div></foreignObject>
  <foreignObject x="7" y="231.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x_0$</div></foreignObject>
  <foreignObject x="62" y="76" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v = \dfrac{\Delta x}{\Delta t}$</div></foreignObject>
  <line x1="339" y1="290" x2="504" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M516,290 L503,296 L503,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="340" y1="291" x2="340" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M340,44 L346,57 L334,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="522" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="330" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="340,180 490,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v > 0$</div></foreignObject>
  <polyline points="340,180 490,180" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="165.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$v = 0$</div></foreignObject>
  <polyline points="340,180 490,246" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$v < 0$</div></foreignObject>
  <circle cx="340" cy="180" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="297" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x_0$</div></foreignObject>
</svg>

Kulmakerroin lasketaan näin. Valitaan suoralta kaksi pistettä, jotka ovat kaukana toisistaan. Paikan muutos jaetaan ajan muutoksella. Mittauspisteistä piirretään kuvaaja. Siihen sovitetaan suora niin, että pisteet jäävät tasaisesti suoran molemmille puolille. Kulmakerroin lasketaan suoralta. Sitä ei lasketa kahdesta vierekkäisestä mittauspisteestä, koska jokaisessa mittauksessa on pieni virhe.

## Esimerkki
Hölkkääjän liike on tasaista. Kuvaajasta luetaan, että hän on hetkellä $t = 0$ paikassa $20\,\text{m}$. Hetkellä $t = 40\,\text{s}$ hän on paikassa $120\,\text{m}$. Mikä on hölkkääjän nopeus? Missä paikassa hän on hetkellä $t = 60\,\text{s}$?

<svg data-fig="jogger-graph" viewBox="0 0 600 340" role="img" aria-label="(t,x)-kuvaaja mittakaavassa. Suora nousee paikasta 20 metriä hetkellä 0 paikkaan 120 metriä hetkellä 40 sekuntia. Se jatkuu katkoviivana paikkaan 170 metriä hetkellä 60 sekuntia." style="max-width:100%;font-size:24px">
  <line x1="200" y1="296" x2="200" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308" y1="296" x2="308" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="296" x2="416" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="272.5" x2="470" y2="272.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="155.5" x2="470" y2="155.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="97" x2="470" y2="97" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="296" x2="484" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,296 L483,302 L483,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="297" x2="92" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,36 L98,49 L86,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="200" y1="296" x2="200" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="183.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="308" y1="296" x2="308" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="291.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="416" y1="296" x2="416" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="399.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="85" y1="272.5" x2="92" y2="272.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="258" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="155.5" x2="92" y2="155.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="141" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <line x1="85" y1="97" x2="92" y2="97" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="82.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$170$</div></foreignObject>
  <foreignObject x="62" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="281.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="82" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <polyline points="92,272.5 308,155.5" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="308,155.5 416,97" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <line x1="308" y1="155.5" x2="308" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="155.5" x2="308" y2="155.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="416" y1="97" x2="416" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="97" x2="416" y2="97" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="92" cy="272.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="308" cy="155.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="416" cy="97" r="7" fill="#ffffff" stroke="#1971c2" stroke-width="3"/>
</svg>

<!-- vaihe -->

**Tunnetut ja kysytty.** Kuvaajasta luetaan kaksi pistettä: $(t_1;\, x_1) = (0\,\text{s};\, 20\,\text{m})$ ja $(t_2;\, x_2) = (40\,\text{s};\, 120\,\text{m})$. Kysytään nopeutta $v$ ja paikkaa $x$ hetkellä $t = 60\,\text{s}$.

<!-- vaihe -->

**Periaate.** Hölkkääjän liike on tasaista. Siksi nopeus pysyy vakiona ja $(t, x)$-kuvaaja on suora. Nopeus on suoran kulmakerroin. Se on paikan muutos jaettuna ajan muutoksella. Kun nopeus tunnetaan, paikan saa näin: alkupaikkaan lisätään nopeuden ja ajan tulo.

<!-- vaihe -->

**Kaava ratkaistuna.** Nopeus ja paikka ratkaistaan ensin symbolein. Lukuja ei vielä käytetä:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
x &= x_1 + v\,t
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Paikat ovat metreinä ja ajat sekunteina. Siksi nopeus tulee suoraan yksikössä $\text{m/s}$. Muunnoksia ei tarvita. Alkupaikka on $x_1 = 20\,\text{m}$ hetkellä $t_1 = 0$. Siksi ajaksi $t$ kelpaa suoraan $60\,\text{s}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
&= \frac{120\,\text{m} - 20\,\text{m}}{40\,\text{s} - 0\,\text{s}} \\
&= 2{,}5\,\text{m/s}
\\[4pt]
x &= x_1 + v\,t \\
&= 20\,\text{m} + 2{,}5\,\text{m/s} \cdot 60\,\text{s} \\
&= 20\,\text{m} + 150\,\text{m} \\
&= 170\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Nopeus on $v = 2{,}5\,\text{m/s}$. Paikka hetkellä $60\,\text{s}$ on $x = 170\,\text{m}$ eli $1{,}7 \cdot 10^2\,\text{m}$. Nopeudessa on kaksi merkitsevää numeroa, koska aikaväli $40\,\text{s}$ on annettu kahdella numerolla. Paikassa tulo $2{,}5\,\text{m/s} \cdot 60\,\text{s} = 150\,\text{m}$ on myös kahdella numerolla. Siksi summa $20\,\text{m} + 150\,\text{m}$ tunnetaan vain kymmenien metrien tarkkuudella: $x = 1{,}7 \cdot 10^2\,\text{m}$.

<!-- vaihe -->

**Järkevyys.** Ensimmäisten 40 sekunnin aikana paikka kasvoi $100\,\text{m}$. Seuraavien 20 sekunnin aikana se kasvaa puolet siitä, $50\,\text{m}$. Paikka on $120\,\text{m} + 50\,\text{m} = 170\,\text{m}$. Tulos on sama. Nopeus $2{,}5\,\text{m/s}$ on noin $9\,\text{km/h}$. Se on hölkän vauhti. Nopeus on positiivinen, koska kuvaaja nousee.

## Yleinen virhekäsitys
$(t,x)$-kuvaaja ei ole kuva kappaleen reitistä. Nouseva viiva ei tarkoita ylämäkeä. Se tarkoittaa, että paikka kasvaa. Toinen virhe on pitää negatiivista nopeutta hitaana nopeutena. Etumerkki kertoo vain suunnan. Nopeus $-3\,\text{m/s}$ on suuruudeltaan suurempi kuin $+2\,\text{m/s}$. Kolmas virhe on päätellä paikasta nopeus. Kappale voi olla edellä ja liikkua silti hitaammin.

## Tiivistelmä
- Paikka $x$ kertoo, missä kappale on origoon nähden. Siirtymä $\Delta x = x_2 - x_1$ on paikan muutos. Sen etumerkki kertoo suunnan. Matka on reitin pituus. Matka ei ole negatiivinen.
- Nopeus $v = \Delta x / \Delta t$ on vektorisuure. Tasaisessa liikkeessä se on vakio. Paikka on $x = x_0 + v\,t$.
- Tasaisen liikkeen viiva $(t,x)$-kuvaajassa on suora. Kulmakerroin on nopeus. Sen etumerkki kertoo suunnan.
- Mittausaineistoon sovitetaan suora. Nopeus lasketaan suoralta valituista pisteistä, jotka ovat kaukana toisistaan.
- Edestakaisen liikkeen keskinopeus voi olla nolla, vaikka matka ei ole nolla.
