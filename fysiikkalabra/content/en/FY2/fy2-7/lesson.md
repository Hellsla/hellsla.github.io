# Transferring energy: electricity and heat

> **Why** is the voltage in power lines hundreds of kilovolts when a wall socket gives only $230\,\text{V}$, and why are district heating pipes wrapped in thick insulation?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: tall power line pylons in a landscape, their wires running far away. In the foreground a cut-away view through the ground: district heating pipes surrounded by a thick layer of insulation carry heat to a house." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy27h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy27h-field" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#f1dfb5"/></linearGradient><linearGradient id="fy27h-soil" gradientUnits="userSpaceOnUse" x1="0" y1="420" x2="0" y2="600"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy27h-case486" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#1f2933"/></linearGradient><linearGradient id="fy27h-case556" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#1f2933"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="380" fill="url(#fy27h-sky)"/>
  <path d="M166,82 Q165,61.5 189,64 Q198.5,42.5 222.5,49.5 Q244,37.5 256,60.5 Q277.5,63 275,82 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M595,120 Q594,103 614,105 Q622,87 642,93 Q660,83 670,102 Q688,104 686,120 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,250 Q100,205 200,253 Q300,226.5 400,248.5 Q500,222.5 600,249.5 Q700,219 800,250 Q900,232.5 1000,247.5 Q1100,216.5 1200,250.5 Q1300,225.5 1400,249 V600 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M0,280.5 Q100,241 200,282 Q300,257 400,282.5 Q500,239 600,284 Q700,238.5 800,282.5 Q900,233.5 1000,279 Q1100,254 1200,279 Q1300,255.5 1400,282.5 V600 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M0,300 L11.5,274.5 L23.5,300 L40,260.5 L57,300 L67.5,277.5 L78,300 L89,277 L100,300 L109,281.5 L118.5,300 L128,280.5 L137.5,300 L151.5,269 L165,300 L181,263 L197,300 L210.5,270 L223.5,300 L233.5,280.5 L243,300 L257,268.5 L271,300 L282,277 L292.5,300 L305.5,271 L318.5,300 L328.5,279.5 L338.5,300 L349.5,277.5 L360.5,300 L374.5,267.5 L388.5,300 L401.5,271 L414.5,300 L431.5,260 L448.5,300 L463.5,266 L478,300 L494,263.5 L509.5,300 L526,260.5 L543,300 L554,277 L564.5,300 L578.5,269 L592.5,300 L608.5,261 L625,300 L639.5,267 L654,300 L669.5,264 L685,300 L694,282 L703,300 L719.5,261.5 L736,300 L751.5,263 L767.5,300 L783,263.5 L798.5,300 L813,267.5 L827.5,300 L839.5,274 L851,300 L864,271.5 L877,300 L888.5,275 L900,300 L915,265 L930,300 L939.5,280 L949.5,300 L963,270 L976.5,300 L985.5,281.5 L995,300 L1010,266 L1024.5,300 L1039,267.5 L1053,300 L1062.5,281.5 L1071.5,300 L1088.5,260 L1105.5,300 L1117,274.5 L1129,300 L1144.5,263 L1160.5,300 L1176,263.5 L1191.5,300 L1202,278.5 L1212.5,300 V320 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="316" width="1200" height="110" fill="url(#fy27h-field)"/>
  <path d="M46,400 L74,160 H86 L114,400" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <line x1="46" y1="400" x2="108.5" y2="352" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="114" y1="400" x2="51.5" y2="352" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="51.5" y1="352" x2="103" y2="304" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="108.5" y1="352" x2="57" y2="304" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="57" y1="304" x2="97" y2="256" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="103" y1="304" x2="63" y2="256" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="63" y1="256" x2="91.5" y2="208" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="256" x2="68.5" y2="208" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="28" y1="208" x2="132" y2="208" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="28" y1="208" x2="28" y2="222" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="132" y1="208" x2="132" y2="222" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="46" y1="160" x2="114" y2="160" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="46" y1="160" x2="46" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="114" y1="160" x2="114" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M394,360 L415.5,180 H424.5 L446,360" fill="none" stroke="#6c757d" stroke-width="2.28" stroke-linejoin="round"/>
  <line x1="394" y1="360" x2="441.5" y2="324" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="446" y1="360" x2="398.5" y2="324" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="398.5" y1="324" x2="437.5" y2="288" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="441.5" y1="324" x2="402.5" y2="288" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="402.5" y1="288" x2="433" y2="252" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="437.5" y1="288" x2="407" y2="252" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="407" y1="252" x2="429" y2="216" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="433" y1="252" x2="411" y2="216" stroke="#6c757d" stroke-width="1.14" stroke-linecap="butt"/>
  <line x1="380.5" y1="216" x2="459.5" y2="216" stroke="#6c757d" stroke-width="2.28" stroke-linecap="butt"/>
  <line x1="380.5" y1="216" x2="380.5" y2="226.5" stroke="#1f2933" stroke-width="1.52" stroke-linecap="butt"/>
  <line x1="459.5" y1="216" x2="459.5" y2="226.5" stroke="#1f2933" stroke-width="1.52" stroke-linecap="butt"/>
  <line x1="394" y1="180" x2="446" y2="180" stroke="#6c757d" stroke-width="2.28" stroke-linecap="butt"/>
  <line x1="394" y1="180" x2="394" y2="190.5" stroke="#1f2933" stroke-width="1.52" stroke-linecap="butt"/>
  <line x1="446" y1="180" x2="446" y2="190.5" stroke="#1f2933" stroke-width="1.52" stroke-linecap="butt"/>
  <path d="M660.5,336 L676.5,200 H683.5 L699.5,336" fill="none" stroke="#6c757d" stroke-width="1.74" stroke-linejoin="round"/>
  <line x1="660.5" y1="336" x2="696.5" y2="309" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="699.5" y1="336" x2="663.5" y2="309" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="663.5" y1="309" x2="693" y2="281.5" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="696.5" y1="309" x2="667" y2="281.5" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="667" y1="281.5" x2="690" y2="254.5" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="693" y1="281.5" x2="670" y2="254.5" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="670" y1="254.5" x2="686.5" y2="227" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="690" y1="254.5" x2="673.5" y2="227" stroke="#6c757d" stroke-width="0.87" stroke-linecap="butt"/>
  <line x1="650" y1="227" x2="710" y2="227" stroke="#6c757d" stroke-width="1.74" stroke-linecap="butt"/>
  <line x1="650" y1="227" x2="650" y2="235.5" stroke="#1f2933" stroke-width="1.16" stroke-linecap="butt"/>
  <line x1="710" y1="227" x2="710" y2="235.5" stroke="#1f2933" stroke-width="1.16" stroke-linecap="butt"/>
  <line x1="660.5" y1="200" x2="699.5" y2="200" stroke="#6c757d" stroke-width="1.74" stroke-linecap="butt"/>
  <line x1="660.5" y1="200" x2="660.5" y2="208" stroke="#1f2933" stroke-width="1.16" stroke-linecap="butt"/>
  <line x1="699.5" y1="200" x2="699.5" y2="208" stroke="#1f2933" stroke-width="1.16" stroke-linecap="butt"/>
  <path d="M844.5,322 L857.5,218 H862.5 L875.5,322" fill="none" stroke="#6c757d" stroke-width="1.35" stroke-linejoin="round"/>
  <line x1="844.5" y1="322" x2="873" y2="301" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="875.5" y1="322" x2="847" y2="301" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="847" y1="301" x2="870.5" y2="280.5" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="873" y1="301" x2="849.5" y2="280.5" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="849.5" y1="280.5" x2="867.5" y2="259.5" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="870.5" y1="280.5" x2="852.5" y2="259.5" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="852.5" y1="259.5" x2="865" y2="239" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="867.5" y1="259.5" x2="855" y2="239" stroke="#6c757d" stroke-width="0.675" stroke-linecap="butt"/>
  <line x1="836.5" y1="239" x2="883.5" y2="239" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="836.5" y1="239" x2="836.5" y2="245" stroke="#1f2933" stroke-width="0.9" stroke-linecap="butt"/>
  <line x1="883.5" y1="239" x2="883.5" y2="245" stroke="#1f2933" stroke-width="0.9" stroke-linecap="butt"/>
  <line x1="844.5" y1="218" x2="875.5" y2="218" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="844.5" y1="218" x2="844.5" y2="224.5" stroke="#1f2933" stroke-width="0.9" stroke-linecap="butt"/>
  <line x1="875.5" y1="218" x2="875.5" y2="224.5" stroke="#1f2933" stroke-width="0.9" stroke-linecap="butt"/>
  <path d="M28,222 Q204,250.5 380.5,226.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M132,222 Q296,250.5 459.5,226.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M46,174 Q220,208.5 394,190.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M114,174 Q280,208.5 446,190.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M380.5,226.5 Q515,257 650,235.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M459.5,226.5 Q585,257 710,235.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M394,190.5 Q527,225.5 660.5,208" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M446,190.5 Q573,225.5 699.5,208" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M650,235.5 Q743,266 836.5,245" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M710,235.5 Q797,266 883.5,245" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M660.5,208 Q752.5,242 844.5,224.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M699.5,208 Q787.5,242 875.5,224.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="535.5" y="407" width="9" height="13" fill="#b8622d"/>
  <path d="M500.5,409 L540,365 L579.5,409 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M540,365 L579.5,409 H540 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M509,385 L540,341 L571,385 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M540,341 L571,385 H540 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M518,360.5 L540,310 L562,360.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M540,310 L562,360.5 H540 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="756.5" y="409" width="7" height="11" fill="#b8622d"/>
  <path d="M727.5,411 L760,375 L792.5,411 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M760,375 L792.5,411 H760 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M735,391 L760,355 L785,391 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M760,355 L785,391 H760 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M742,371.5 L760,330 L778,371.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M760,330 L778,371.5 H760 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="960" y="310" width="190" height="110" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="974" y1="313" x2="974" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="988" y1="313" x2="988" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1002" y1="313" x2="1002" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1016" y1="313" x2="1016" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1030" y1="313" x2="1030" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1044" y1="313" x2="1044" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1058" y1="313" x2="1058" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1072" y1="313" x2="1072" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1086" y1="313" x2="1086" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1100" y1="313" x2="1100" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1114" y1="313" x2="1114" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1128" y1="313" x2="1128" y2="417" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="960" y="310" width="10" height="110" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1140" y="310" width="10" height="110" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M940,310 L1055,249.5 L1170,310 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="990" y="341" width="40" height="44" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="990" y="341" width="40" height="44" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="1010" y1="341" x2="1010" y2="385" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="1060" y="341" width="40" height="44" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="1060" y="341" width="40" height="44" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="1080" y1="341" x2="1080" y2="385" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="0" y="420" width="1200" height="180" fill="url(#fy27h-soil)"/>
  <rect x="0" y="420" width="1200" height="14" fill="#2b8a3e"/>
  <circle cx="323.5" cy="584" r="2.16843" fill="#a97a35"/>
  <circle cx="504" cy="489" r="2.46714" fill="#e9c98a"/>
  <circle cx="356" cy="508.5" r="2.33455" fill="#a97a35"/>
  <circle cx="1084" cy="522.5" r="4.43077" fill="#e9c98a"/>
  <circle cx="741.5" cy="462" r="2.59674" fill="#a97a35"/>
  <circle cx="1088" cy="534.5" r="2.56354" fill="#e9c98a"/>
  <circle cx="825.5" cy="494.5" r="4.04081" fill="#a97a35"/>
  <circle cx="145" cy="525.5" r="4.79468" fill="#e9c98a"/>
  <circle cx="1013.5" cy="506" r="4.01552" fill="#a97a35"/>
  <circle cx="70.5" cy="496" r="4.9258" fill="#e9c98a"/>
  <circle cx="343.5" cy="561.5" r="4.61515" fill="#a97a35"/>
  <circle cx="889.5" cy="490" r="3.58315" fill="#e9c98a"/>
  <circle cx="758.5" cy="569.5" r="4.76408" fill="#a97a35"/>
  <circle cx="160" cy="571" r="3.57672" fill="#e9c98a"/>
  <circle cx="76" cy="594" r="2.95911" fill="#a97a35"/>
  <circle cx="249.5" cy="502.5" r="4.05482" fill="#e9c98a"/>
  <circle cx="588.5" cy="495.5" r="3.61823" fill="#a97a35"/>
  <circle cx="529" cy="466.5" r="3.39941" fill="#e9c98a"/>
  <circle cx="190.5" cy="479" r="2.11746" fill="#a97a35"/>
  <circle cx="31.5" cy="557" r="4.70049" fill="#e9c98a"/>
  <circle cx="163.5" cy="460.5" r="4.81674" fill="#a97a35"/>
  <circle cx="746" cy="446.5" r="3.85451" fill="#e9c98a"/>
  <circle cx="947" cy="547" r="4.33381" fill="#a97a35"/>
  <circle cx="232" cy="556" r="3.86612" fill="#e9c98a"/>
  <circle cx="210" cy="516.5" r="4.31771" fill="#a97a35"/>
  <circle cx="117" cy="538.5" r="4.4598" fill="#e9c98a"/>
  <circle cx="1191" cy="510.5" r="2.95298" fill="#a97a35"/>
  <circle cx="86.5" cy="535" r="2.52256" fill="#e9c98a"/>
  <circle cx="962.5" cy="463.5" r="4.83044" fill="#a97a35"/>
  <circle cx="464" cy="586.5" r="4.97252" fill="#e9c98a"/>
  <circle cx="903.5" cy="516.5" r="3.95541" fill="#a97a35"/>
  <circle cx="1006" cy="501" r="4.7975" fill="#e9c98a"/>
  <circle cx="597.5" cy="559" r="3.76187" fill="#a97a35"/>
  <circle cx="185" cy="502.5" r="4.02211" fill="#e9c98a"/>
  <circle cx="466" cy="590.5" r="3.92299" fill="#a97a35"/>
  <circle cx="831.5" cy="539" r="2.69362" fill="#e9c98a"/>
  <circle cx="1118" cy="554.5" r="4.33371" fill="#a97a35"/>
  <circle cx="165.5" cy="499" r="4.61263" fill="#e9c98a"/>
  <circle cx="807" cy="516" r="4.83253" fill="#a97a35"/>
  <circle cx="432" cy="571.5" r="2.79569" fill="#e9c98a"/>
  <circle cx="442.5" cy="469" r="2.15847" fill="#a97a35"/>
  <circle cx="802" cy="558.5" r="4.58217" fill="#e9c98a"/>
  <circle cx="97.5" cy="565" r="3.37543" fill="#a97a35"/>
  <circle cx="65" cy="514" r="2.27656" fill="#e9c98a"/>
  <circle cx="284.5" cy="580" r="2.67132" fill="#a97a35"/>
  <circle cx="494" cy="578" r="4.65464" fill="#e9c98a"/>
  <circle cx="361.5" cy="567.5" r="4.25526" fill="#a97a35"/>
  <circle cx="442.5" cy="588" r="2.20804" fill="#e9c98a"/>
  <circle cx="478" cy="520.5" r="3.32238" fill="#a97a35"/>
  <circle cx="732.5" cy="550" r="4.56025" fill="#e9c98a"/>
  <circle cx="370" cy="456" r="4.49107" fill="#a97a35"/>
  <circle cx="619.5" cy="490.5" r="3.07159" fill="#e9c98a"/>
  <circle cx="723" cy="570.5" r="4.23651" fill="#a97a35"/>
  <circle cx="709.5" cy="592" r="3.24873" fill="#e9c98a"/>
  <circle cx="1033.5" cy="459" r="3.18947" fill="#a97a35"/>
  <circle cx="856.5" cy="494.5" r="3.36555" fill="#e9c98a"/>
  <circle cx="137" cy="518" r="2.89938" fill="#a97a35"/>
  <circle cx="742.5" cy="591" r="3.86836" fill="#e9c98a"/>
  <circle cx="636" cy="527.5" r="4.01668" fill="#a97a35"/>
  <circle cx="1198" cy="456" r="2.11081" fill="#e9c98a"/>
  <line x1="0" y1="420" x2="1200" y2="420" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="0" y="456" width="1010" height="60" fill="url(#fy27h-case486)" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="462" width="1010" height="48" fill="#f1dfb5"/>
  <circle cx="12" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="38" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="64" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="90" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="116" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="142" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="168" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="194" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="220" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="246" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="272" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="298" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="324" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="350" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="376" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="402" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="428" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="454" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="480" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="506" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="532" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="558" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="584" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="610" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="636" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="662" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="688" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="714" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="740" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="766" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="792" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="818" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="844" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="870" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="896" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="922" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="948" cy="474" r="3" fill="#e9c98a"/>
  <circle cx="974" cy="496" r="3" fill="#e9c98a"/>
  <circle cx="1000" cy="474" r="3" fill="#e9c98a"/>
  <rect x="0" y="477" width="1010" height="18" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="0" y="526" width="1060" height="60" fill="url(#fy27h-case556)" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="532" width="1060" height="48" fill="#f1dfb5"/>
  <circle cx="12" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="38" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="64" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="90" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="116" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="142" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="168" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="194" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="220" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="246" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="272" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="298" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="324" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="350" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="376" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="402" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="428" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="454" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="480" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="506" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="532" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="558" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="584" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="610" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="636" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="662" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="688" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="714" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="740" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="766" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="792" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="818" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="844" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="870" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="896" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="922" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="948" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="974" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="1000" cy="544" r="3" fill="#e9c98a"/>
  <circle cx="1026" cy="566" r="3" fill="#e9c98a"/>
  <circle cx="1052" cy="544" r="3" fill="#e9c98a"/>
  <rect x="0" y="547" width="1060" height="18" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <rect x="980" y="420" width="60" height="96" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <rect x="1001" y="420" width="18" height="75" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="1030" y="420" width="60" height="166" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <rect x="1051" y="420" width="18" height="145" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="0" cy="486" r="30" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="0" cy="486" r="24" fill="#f1dfb5"/>
  <circle cx="0" cy="486" r="9" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="0" cy="556" r="30" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="0" cy="556" r="24" fill="#f1dfb5"/>
  <circle cx="0" cy="556" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
</svg>

## Key idea

Energy is often produced far from where it is used: the power plant is outside the city, but the heater and the wall socket are at home. So the energy has to be transferred to the user. In Finland this happens in two ways: as **electrical energy** in the electricity grid and as **thermal energy** in the water pipes of the district heating network.

### The electricity grid

The **electricity grid** carries electrical energy from the power plant to the home. Long distances are covered by the power lines of the national grid, whose voltage is $110\text{–}400\,\text{kV}$. Closer to the user the voltage is first lowered to $20\,\text{kV}$ and finally to the $0.4\,\text{kV}$ of the low-voltage network, from which the sockets in homes get $230\,\text{V}$. The voltage is changed in transformers.

<svg data-fig="grid" viewBox="0 0 600 332" role="img" aria-label="Schematic of the route of electricity from the power plant to the home. From left to right: power plant and its transformer, national grid power line (voltage from 110 kV to 400 kV), substation, distribution network poles (20 kV) and home (0.4 kV, 230 V at the socket). Below, an orange arrow shows the flow of energy from the power plant to the home. Not to scale." style="max-width:100%;font-size:24px">
  <line x1="12" y1="206" x2="588" y2="206" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="30" y="150" width="76" height="56" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="44" y="96" width="16" height="54" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="58" cy="82" rx="14" ry="9" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/><ellipse cx="72" cy="66" rx="12" ry="8" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <rect x="76" y="166" width="18" height="22" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="118" y="172" width="34" height="34" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="130" cy="189" r="8" fill="none" stroke="#ffffff" stroke-width="2"/>
  <circle cx="141" cy="189" r="8" fill="none" stroke="#ffffff" stroke-width="2"/>
  <path d="M106,160 Q135,150 164,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M152,178 Q158,155 164,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M170,206 L185,112 L195,112 L210,206" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="176" y1="172" x2="204" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="140" x2="200" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="177" y1="172" x2="200" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="203" y1="172" x2="180" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="160" y1="124" x2="220" y2="124" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="164" y1="124" x2="164" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="216" y1="124" x2="216" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M280,206 L295,112 L305,112 L320,206" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="286" y1="172" x2="314" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="140" x2="310" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="287" y1="172" x2="310" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="313" y1="172" x2="290" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="124" x2="330" y2="124" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="274" y1="124" x2="274" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="326" y1="124" x2="326" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M164,124 Q217,152 270,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M216,124 Q245,144 274,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M326,124 Q349,157 372,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,124 Q230,148 270,124" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <rect x="372" y="164" width="54" height="42" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="382" y="176" width="18" height="30" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="406" y="176" width="14" height="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="396" y1="164" x2="396" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="380" y1="150" x2="412" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="452" y1="206" x2="452" y2="142" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="438" y1="150" x2="466" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="500" y1="206" x2="500" y2="142" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="486" y1="150" x2="514" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M412,150 Q432,162 452,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M452,150 Q476,166 500,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M500,150 Q519,167 538,168" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="528" y="172" width="54" height="34" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M520,174 L555,142 L590,174 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="536" y="182" width="14" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="558" y="182" width="16" height="14" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="160" y="47.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$110\text{–}400\,\text{kV}$</div></foreignObject>
  <foreignObject x="426" y="101.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="506" y="47.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.4\,\text{kV}$</div></foreignObject>
  <foreignObject x="85" y="86" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{transformer}$</div></foreignObject>
  <line x1="130" y1="118" x2="130" y2="171" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="556" y1="82" x2="556" y2="130" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <foreignObject x="18" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{power plant}$</div></foreignObject>
  <foreignObject x="175" y="247.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{national grid}$</div></foreignObject>
  <foreignObject x="325" y="281.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{substation}$</div></foreignObject>
  <foreignObject x="450" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{distribution network}$</div></foreignObject>
  <path d="M30,235 L544,235 L544,243 L570,228 L544,213 L544,221 L30,221 Z" fill="#e8590c" stroke-linejoin="round"/>
</svg>

### Why long distances use high voltage

The same power can be transferred in two ways: with a low voltage and a large electric current, or with a high voltage and a small electric current. A wire gets hotter the larger the current in it is, and the energy used for heating is a loss. So long distances are covered with a high voltage, which keeps the current and the loss small. The exact connection between voltage, current and loss belongs to later courses on electricity.

A transformer raises the voltage at the power plant and lowers it again close to the user. In a good transformer the loss is very small.

### District heating

**District heating** transfers energy as hot water. The water heated at the heating plant flows in the supply pipe to buildings and gives heat to the building's heating system. The cooled water returns in the return pipe to be heated again. The pipes are underground in thick insulation so that as little heat as possible goes into the surrounding ground.

<svg data-fig="district" viewBox="0 0 600 320" role="img" aria-label="Schematic of the district heating loop. On the left the heating plant, on the right a home. A red supply pipe takes hot water to the home and a blue return pipe brings the cooled water back. The pipes are inside shared insulation underground. Orange arrows show that a little heat still escapes through the insulation into the ground. Not to scale." style="max-width:100%;font-size:24px">
  <rect x="20" y="124" width="86" height="80" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="34" y="80" width="16" height="44" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="46" cy="66" rx="14" ry="9" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <rect x="64" y="150" width="30" height="54" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M492,128 L546,84 L600,128 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="500" y="128" width="90" height="76" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="512" y="140" width="22" height="26" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="548" y="144" width="32" height="52" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="556" y1="148" x2="556" y2="192" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="564" y1="148" x2="564" y2="192" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="572" y1="148" x2="572" y2="192" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <rect x="106" y="120" width="394" height="78" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="106" y="138" width="394" height="14" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="106" y="166" width="394" height="14" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <path d="M312,145 L293,137 L293,153 Z" fill="#ffffff" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M288,173 L307,165 L307,181 Z" fill="#ffffff" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M176,204 L176,222 L170,222 L180,236 L190,222 L184,222 L184,204 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M416,204 L416,222 L410,222 L420,236 L430,222 L424,222 L424,204 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="444" y="209.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{loss}$</div></foreignObject>
  <foreignObject x="170" y="79.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{supply water}$</div></foreignObject>
  <foreignObject x="165" y="253.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{return water}$</div></foreignObject>
  <foreignObject x="331" y="79.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{insulation}$</div></foreignObject>
  <line x1="376" y1="108" x2="376" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="-7" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heating plant}$</div></foreignObject>
  <foreignObject x="505" y="247.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{home}$</div></foreignObject>
</svg>

### Transmission loss

In both networks some of the energy turns into heat in the surroundings on the way and does not arrive. This is called **transmission loss**. The energy does not disappear (chapter *Forms of energy and conservation of energy*), but the loss is useless to the user.

In Finland the losses of the electricity grid in 2024 were about $4\,\%$ of electricity consumption, when consumption was about $83\,\text{TWh}$ (Finnish Energy, Sähkövuosi 2024). In this chapter consumption is used as the energy sent into the electricity grid, so $4\,\%$ is a share of it. About $36\,\text{TWh}$ was supplied to the district heating network in 2024 and about $32.7\,\text{TWh}$ was used by customers, so about $9\,\%$ was left on the way (Finnish Energy, Kaukolämpötilasto 2024; the share is calculated from the difference, so it is an estimate). The loss of district heating is relatively larger because hot water is clearly warmer than its surroundings: the greater the temperature difference to the surroundings, the more heat escapes, and heat gets through the insulation along the whole length of the pipework.

### Transferring energy in time: storage

Energy is also transferred in time. Wind power and solar electricity are produced when the wind blows or the sun shines, but electricity is needed at other times too. A store takes in energy when there is too much of it and gives it out later.

<svg data-fig="storage" viewBox="0 0 600 300" role="img" aria-label="Schematic of three energy stores. On the left a battery, where the energy is chemical. In the middle a pumped-storage plant: upper reservoir, lower reservoir and a pipe in which water flows down. On the right a heat store, an insulated tank full of hot water. Not to scale." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy27-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy27-hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <rect x="60" y="100" width="80" height="110" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="84" y="88" width="32" height="12" fill="#1f2933"/>
  <rect x="70" y="150" width="60" height="50" rx="4" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2"/>
  <line x1="100" y1="112" x2="100" y2="132" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="90" y1="122" x2="110" y2="122" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="90" y1="138" x2="110" y2="138" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M220,110 L330,110 L330,206 L186,206 Z" fill="#d9b26a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M220,110 L300,110 L300,128 L214,128 Z" fill="url(#fy27-water)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="190" y="190" width="72" height="16" fill="url(#fy27-water)" stroke="#1f2933" stroke-width="2"/>
  <line x1="290" y1="128" x2="290" y2="190" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="290" y1="190" x2="262" y2="198" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="290" cy="160" r="9" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="420" y="92" width="100" height="118" rx="14" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <rect x="430" y="102" width="80" height="98" rx="8" fill="url(#fy27-hot)" stroke="#1f2933" stroke-width="2"/>
  <line x1="470" y1="82" x2="470" y2="92" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="470" y1="210" x2="470" y2="222" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <foreignObject x="55" y="252.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <foreignObject x="160" y="252.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pumped storage}$</div></foreignObject>
  <foreignObject x="375" y="252.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat store}$</div></foreignObject>
  <foreignObject x="25" y="25.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{chemical}$</div></foreignObject>
  <foreignObject x="188" y="14" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potential}$</div></foreignObject>
  <foreignObject x="188" y="42" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="420" y="25.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat}$</div></foreignObject>
  <foreignObject x="196" y="78" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{upper pool}$</div></foreignObject>
  <foreignObject x="176" y="210" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lower pool}$</div></foreignObject>
  <line x1="184" y1="20" x2="184" y2="280" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="380" y1="20" x2="380" y2="280" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
</svg>

In a battery the energy is stored as chemical energy. In a pumped-storage power plant water is pumped to an upper reservoir, and the water flowing down turns the machines of the power plant. In a heat store hot water stays in an insulated tank, and it is used for example in the district heating network. Electricity is not stored in large amounts as such but by converting it into another form of energy and back, and in every conversion some of the energy turns into heat.

## Formula: Transmission loss

The loss is the difference between the energy sent into the network and the energy that arrives. The efficiency of the transfer (chapter *Efficiency*) is the share of the sent energy that arrives:

```latex
\begin{aligned}
E_\text{loss} &= E_\text{sent} - E_\text{arrived} \\
\eta &= \frac{E_\text{arrived}}{E_\text{sent}}
\end{aligned}
```

where $E_\text{sent}$ is the energy fed into the network, $E_\text{arrived}$ the energy that reached the user, $E_\text{loss}$ the energy that turned into heat on the way and $\eta$ the efficiency of the transfer. Efficiency is given as a percentage or as a decimal number.

<svg data-fig="sankey" viewBox="0 0 600 330" role="img" aria-label="Energy flow diagram to scale. At the top the electricity grid: of the sent energy 96 % arrives and 4 % is lost. At the bottom the district heating network: 91 % arrives and 9 % is lost. The width of a stream is proportional to the energy; the width of the sent energy is the same in both." style="max-width:100%;font-size:24px">
  <foreignObject x="12" y="17.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{electricity}$</div></foreignObject>
  <rect x="150" y="52" width="121" height="80" fill="#e8590c"/>
  <polygon points="270,52 470,52 470,44 500,90.5 470,137 470,129 270,129" fill="#e8590c"/>
  <path d="M270,129 L330,129 C370,129 370,155 410,155 L460,155 L460,147 L490,156.5 L460,166 L460,158 L410,158 C370,158 370,132 330,132 L270,132 Z" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="50" y="77.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="76" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$96\,\%$</div></foreignObject>
  <foreignObject x="506" y="142" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4\,\%$</div></foreignObject>
  <foreignObject x="12" y="175.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{district heating}$</div></foreignObject>
  <rect x="150" y="210" width="121" height="80" fill="#e8590c"/>
  <polygon points="270,210 470,210 470,202 500,246.5 470,291 470,283 270,283" fill="#e8590c"/>
  <path d="M270,283 L330,283 C370,283 370,309 410,309 L460,309 L460,301 L490,312.5 L460,324 L460,316 L410,316 C370,316 370,290 330,290 L270,290 Z" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="50" y="235.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="232" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$91\,\%$</div></foreignObject>
  <foreignObject x="506" y="298" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$9\,\%$</div></foreignObject>
</svg>

In the figure the width of a stream shows the amount of energy. In the electricity grid $4\,\%$ of the sent energy (the consumption) is lost and $96\,\%$ arrives, in district heating $9\,\%$ and $91\,\%$.

### Calculating from a loss percentage

A loss percentage is always taken of the sent energy. If the loss is $9.0\,\%$, then $100\,\% - 9.0\,\% = 91.0\,\%$ of the sent energy arrives, and $91.0\,\% = 91.0 : 100 = 0.910$. The energy you need is solved from the formula: $E_\text{arrived} = \eta\, E_\text{sent}$ and $E_\text{sent} = E_\text{arrived} : \eta$.

The same applies to power: the power that arrives is $\eta$ times the power sent. Energy and power are connected by the formula $P = \tfrac{E}{t}$ (chapter *Power P = ΔE/Δt*), so with a steady loss power $P_\text{loss}$ the energy lost during a time $t$ is $E_\text{loss} = P_\text{loss} \cdot t$.

## Worked example

A district heating network transfers $245\,\text{MWh}$ of thermal energy per week from the heating plant to a district of the city (an example situation). The loss of the network is $9.0\,\%$ of the sent energy. How much energy arrives and how much is lost?

<!-- vaihe -->

**Given and find.** $E_\text{sent} = 245\,\text{MWh}$ and the loss is $9.0\,\%$ of the sent energy. We want the energy that arrives, $E_\text{arrived}$, and the loss $E_\text{loss}$.

<!-- vaihe -->

**Principle.** Energy does not disappear, so the sent energy equals the arriving and the lost energy together. When $9.0\,\%$ is lost, the remaining $91.0\,\%$ arrives, so the efficiency is $\eta = 0.910$.

<!-- vaihe -->

**Rearranged formula.**

```latex
\begin{aligned}
&E_\text{arrived} = \eta\, E_\text{sent} \\
&E_\text{loss} = E_\text{sent} - E_\text{arrived}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The efficiency is obtained from the percentage: $\eta = 100\,\% - 9.0\,\% = 91.0\,\% = 91.0 : 100 = 0.910$. The energies are in the same unit, megawatt-hours, so no other conversion is needed.

<!-- vaihe -->

**Substitution.**

```latex
\begin{aligned}
E_\text{arrived} &= \eta\, E_\text{sent} \\
&= 0.910 \cdot 245\,\text{MWh} \\
&= 222.95\,\text{MWh} \\
E_\text{loss} &= E_\text{sent} - E_\text{arrived} \\
&= (245 - 222.95)\,\text{MWh} \\
&= 22.05\,\text{MWh}
\end{aligned}
```

<!-- vaihe -->

**Result.** About $223\,\text{MWh}$ arrives and about $22\,\text{MWh}$ is lost. The arriving energy is given with three significant figures because the efficiency $0.910$ and the sent energy $245\,\text{MWh}$ are known to three figures. The loss is given with two significant figures because the loss percentage $9.0\,\%$ is known only to two figures.

<!-- vaihe -->

**Reasonableness.** Ten per cent of $245\,\text{MWh}$ would be $24.5\,\text{MWh}$, and $9.0\,\%$ is slightly less, so a loss of $22\,\text{MWh}$ is of the right size. Also $222.95\,\text{MWh} + 22.05\,\text{MWh} = 245\,\text{MWh}$, so the energy is conserved.

## Common misconception

Many people think that energy disappears in transmission loss. Energy does not disappear: it turns into heat, which warms the wires, the pipes and their surroundings, and the user gets no benefit from it.

Another mistake is to take the loss percentage of the energy that arrives. The percentage must be taken of the sent energy: if the loss is $9.0\,\%$ and $245\,\text{MWh}$ arrives, the sent energy is not $245\,\text{MWh} + 0.090 \cdot 245\,\text{MWh}$ but $245\,\text{MWh} : 0.910$.

A third mistake is to think that the loss is subtracted from the percentage as a unit: a loss of $4\,\%$ does not mean $4\,\text{MWh}$ but four hundredths of the sent energy.

## Summary

- Electrical energy is transferred in the electricity grid, long distances at high voltage, because then the current is small and the loss caused by heating of the wires is small. Transformers raise and lower the voltage.
- Thermal energy is transferred in the district heating network as hot water in insulated pipes. In Finland the losses were about $4\,\%$ in the electricity grid and about $9\,\%$ in the district heating network (Finnish Energy, 2024).
- Transmission loss $E_\text{loss} = E_\text{sent} - E_\text{arrived}$ and efficiency of the transfer $\eta = E_\text{arrived} : E_\text{sent}$. The loss percentage is taken of the sent energy.
- Stores (battery, pumped-storage plant, heat store) transfer energy in time, but in them too some of the energy turns into heat.
