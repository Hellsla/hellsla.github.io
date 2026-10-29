# Energy transformations and the joule

> **Why** does the motion of a bicycle ultimately come from the Sun, and how can the amount of energy be given as a single number?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the Sun shines on a field of grain. Orange arrows run from the Sun to the grain, from the grain to bread and from the bread to a cyclist riding on a road: the energy of the motion comes from the Sun." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy22h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy22h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="420" fill="url(#fy22h-sky)"/>
  <circle cx="120" cy="110" r="86.5" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M183,134 L211,134.5 L186.5,120.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M162.5,162.5 L186.5,176.5 L172.5,152.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M130.5,176.5 L144.5,201 L144,173 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M96,173 L95.5,201 L109.5,176.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M67.5,152.5 L53.5,176.5 L77.5,162.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M53.5,120.5 L29,134.5 L57,134 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M57,86 L29,85.5 L53.5,99.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M77.5,57.5 L53.5,43.5 L67.5,67.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M109.5,43.5 L95.5,19 L96,47 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M144,47 L144.5,19 L130.5,43.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M172.5,67.5 L186.5,43.5 L162.5,57.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M186.5,99.5 L211,85.5 L183,86 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="120" cy="110" r="54" fill="url(#fy22h-sun)"/>
  <path d="M688,106 Q686.5,79 718.5,82 Q731,53 763,63 Q792,47 808,77 Q837,80.5 833.5,106 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M986,162 Q985,141.5 1009,144 Q1018.5,122.5 1042.5,129.5 Q1064,117.5 1076,140.5 Q1097.5,143 1095,162 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,330 L12,307 L24.5,330 L37,305.5 L49.5,330 L65.5,297.5 L81,330 L96,298.5 L111.5,330 L133,281.5 L154.5,330 L172,292.5 L189.5,330 L207,292 L224.5,330 L242.5,292 L260,330 L278,291.5 L295.5,330 L313.5,292 L331,330 L346.5,297 L362.5,330 L383.5,282.5 L405,330 L425,285 L445.5,330 L459,302 L473,330 L492.5,287 L512,330 L531,289 L549.5,330 L571.5,281 L593,330 L609.5,295 L626,330 L647.5,282 L668.5,330 L685.5,293.5 L702.5,330 L720,293 L737,330 L754,294 L771,330 L784,304.5 L797,330 L810,305 L822.5,330 L838.5,296 L855,330 L875.5,283.5 L896.5,330 L914,291.5 L932,330 L945.5,303.5 L959,330 L976.5,292.5 L994,330 L1013.5,286.5 L1033,330 L1045.5,307 L1057.5,330 L1075.5,290 L1094,330 L1106.5,306.5 L1118.5,330 L1134.5,296.5 L1150.5,330 L1164,302 L1178,330 L1197.5,287.5 L1217,330 V360 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="360" width="1200" height="240" fill="#b2f2bb"/>
  <rect x="0" y="380" width="420" height="120" fill="#d9b26a"/>
  <line x1="12" y1="500" x2="16" y2="402" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="16" cy="396" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="28" y1="500" x2="32" y2="407.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="32" cy="401.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="44" y1="500" x2="48" y2="405.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="48" cy="399.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="60" y1="500" x2="64" y2="404.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="64" cy="398.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="76" y1="500" x2="80" y2="402.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="80" cy="396.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="92" y1="500" x2="96" y2="408" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="96" cy="402" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="108" y1="500" x2="112" y2="407.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="112" cy="401.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="124" y1="500" x2="128" y2="405" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="128" cy="399" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="140" y1="500" x2="144" y2="405" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="144" cy="399" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="156" y1="500" x2="160" y2="405" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="160" cy="399" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="172" y1="500" x2="176" y2="400" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="176" cy="394" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="188" y1="500" x2="192" y2="406" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="192" cy="400" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="204" y1="500" x2="208" y2="406" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="208" cy="400" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="220" y1="500" x2="224" y2="404" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="224" cy="398" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="236" y1="500" x2="240" y2="408.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="240" cy="402.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="252" y1="500" x2="256" y2="403.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="256" cy="397.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="268" y1="500" x2="272" y2="404" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="272" cy="398" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="284" y1="500" x2="288" y2="402.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="288" cy="396.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="300" y1="500" x2="304" y2="410" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="304" cy="404" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="316" y1="500" x2="320" y2="407" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="320" cy="401" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="332" y1="500" x2="336" y2="408.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="336" cy="402.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="348" y1="500" x2="352" y2="408.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="352" cy="402.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="364" y1="500" x2="368" y2="400.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="368" cy="394.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="380" y1="500" x2="384" y2="406.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="384" cy="400.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="396" y1="500" x2="400" y2="409.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="400" cy="403.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="412" y1="500" x2="416" y2="402.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="416" cy="396.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <path d="M0,520 H1200 V600 H0 Z" fill="#6c757d" stroke-linejoin="round"/>
  <path d="M0,560 H1200" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" stroke-dasharray="40 30"/>
  <rect x="470" y="420" width="150" height="18" rx="4" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <path d="M482,420 Q480,360 545,356 Q610,360 608,420 Z" fill="#d9b26a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M510,384 q10,-10 18,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <path d="M536,384 q10,-10 18,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <path d="M562,384 q10,-10 18,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="820" cy="460" r="50" fill="none" stroke="#1f2933" stroke-width="6"/>
  <circle cx="820" cy="460" r="6" fill="#1f2933"/>
  <circle cx="980" cy="460" r="50" fill="none" stroke="#1f2933" stroke-width="6"/>
  <circle cx="980" cy="460" r="6" fill="#1f2933"/>
  <path d="M820,460 L880,460 L940,380 L860,380 Z M880,460 L854,360 M980,460 L950,350" fill="none" stroke="#c92a2a" stroke-width="7" stroke-linejoin="round" stroke-linejoin="round"/>
  <line x1="838" y1="358" x2="870" y2="358" stroke="#1f2933" stroke-width="8" stroke-linecap="round"/>
  <line x1="940" y1="348" x2="970" y2="342" stroke="#1f2933" stroke-width="6" stroke-linecap="round"/>
  <path d="M854,352 L890,410 L880,460" fill="none" stroke="#1f2933" stroke-width="18" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M854,350 L898,250" fill="none" stroke="#1971c2" stroke-width="40" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M886,272 L954,342" fill="none" stroke="#1971c2" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="956" cy="342" r="10" fill="#f1dfb5"/>
  <circle cx="912" cy="214" r="28" fill="#f1dfb5"/>
  <path d="M882,208 Q892,174 922,180 Q944,186 940,210 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M183.5,163 L252.5,309.5 L243.5,313.5 L270,330 L274.5,299 L265.5,303.5 L196.5,157 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M420.5,407 L440.5,405 L441.5,415 L466,396 L438.5,381.5 L439.5,391.5 L419.5,393 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M632.5,386.5 L799,316.5 L802.5,326 L820,300 L789.5,294.5 L793.5,303.5 L627.5,373.5 Z" fill="#e8590c" stroke-linejoin="round"/>
</svg>

## Key idea
### Energy changes from one form to another
Energy is a quantity that describes what can happen in a system. It appears in different forms, such as mechanical, chemical, electrical, thermal energy, radiation and nuclear energy (chapter *Forms of energy and conservation of energy*). In everyday life, energy seldom stays in one form: it changes from one form to another in a chain of steps.

The cyclist's chain begins with the Sun. Radiation energy is stored in a plant as chemical energy, and it ends up in oats and in morning porridge. The muscles turn part of the chemical energy of the porridge into the motion of the bicycle, and when you stop, the kinetic energy finally turns into thermal energy of the tyres, the brakes and the air.

<svg data-fig="ketju" viewBox="0 0 600 370" role="img" aria-label="Diagram: the energy chain from the Sun to cycling. The Sun emits radiant energy, the plant (oats) stores it as chemical energy in food, the muscles turn part of it into the motion of the bicycle, and the rest turns into thermal energy. At every step part of the energy is transferred as heat to the surroundings (orange arrows pointing down), and finally the kinetic energy also turns into thermal energy. The lengths of the arrows are not to scale." style="max-width:100%;font-size:24px">
  <line x1="106" y1="100" x2="120" y2="100" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="97" y1="122" x2="107" y2="132" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="75" y1="131" x2="75" y2="145" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="53" y1="122" x2="43" y2="132" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="44" y1="100" x2="30" y2="100" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="53" y1="78" x2="43" y2="68" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="75" y1="69" x2="75" y2="55" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="97" y1="78" x2="107" y2="68" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <circle cx="75" cy="100" r="23" fill="#ffc078" stroke="#e8590c" stroke-width="3"/>
  <line x1="181" y1="146" x2="181" y2="86" stroke="#a97a35" stroke-width="3" stroke-linecap="round"/>
  <path d="M181,88 q-9,-10 -7.2,-22 q7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M181,100 q9,-10 7.2,-22 q-7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M181,112 q-9,-10 -7.2,-22 q7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M181,124 q9,-10 7.2,-22 q-7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M203,114 L273,114 A35,30 0 0 1 203,114 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M209,114 Q238,100 267,114 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M221,102 q-7,-9 0,-17 q7,-8 0,-16" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <path d="M238,102 q-7,-9 0,-17 q7,-8 0,-16" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <path d="M255,102 q-7,-9 0,-17 q7,-8 0,-16" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="345" cy="112" r="24" fill="none" stroke="#1f2933" stroke-width="3"/>
  <circle cx="345" cy="112" r="3" fill="#1f2933"/>
  <circle cx="405" cy="112" r="24" fill="none" stroke="#1f2933" stroke-width="3"/>
  <circle cx="405" cy="112" r="3" fill="#1f2933"/>
  <line x1="345" y1="112" x2="369" y2="86" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="369" y1="86" x2="405" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="345" y1="112" x2="375" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="375" y1="112" x2="369" y2="86" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="397" y1="80" x2="405" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="391" y1="78" x2="403" y2="78" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="363" y1="84" x2="373" y2="84" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <rect x="517" y="50" width="16" height="72" rx="8" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="525" cy="130" r="16" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="521" y="84" width="8" height="46" fill="#c92a2a"/>
  <line x1="537" y1="62" x2="547" y2="62" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="537" y1="74" x2="547" y2="74" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="537" y1="86" x2="547" y2="86" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M130,107 L158,107 L158,115 L180,100 L158,85 L158,93 L130,93 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M280,107 L308,107 L308,115 L330,100 L308,85 L308,93 L280,93 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M430,107 L458,107 L458,115 L480,100 L458,85 L458,93 L430,93 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="136" y="29.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{plant}$</div></foreignObject>
  <foreignObject x="5" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Sun}$</div></foreignObject>
  <foreignObject x="5" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{radiation}$</div></foreignObject>
  <foreignObject x="155" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Porridge}$</div></foreignObject>
  <foreignObject x="155" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{chemical}$</div></foreignObject>
  <foreignObject x="305" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Cycling}$</div></foreignObject>
  <foreignObject x="305" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{motion}$</div></foreignObject>
  <foreignObject x="455" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Surroundings}$</div></foreignObject>
  <foreignObject x="455" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{heat}$</div></foreignObject>
  <rect x="30" y="300" width="540" height="44" rx="8" fill="#f2a69c"/>
  <foreignObject x="150" y="307.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat to the surroundings}$</div></foreignObject>
  <path d="M218,232 L218,274 L210,274 L225,296 L240,274 L232,274 L232,232 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M368,232 L368,274 L360,274 L375,296 L390,274 L382,274 L382,232 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M518,232 L518,274 L510,274 L525,296 L540,274 L532,274 L532,232 Z" fill="#e8590c" stroke-linejoin="round"/>
</svg>

At every step, part of the energy turns into thermal energy, which is transferred as heat to the surroundings and spreads out. Even so, no energy disappears: as stated in chapter *Forms of energy and conservation of energy*, there is the same amount of energy at the start and at the end of the chain. In the example in the figure, the $800\,\text{kJ}$ of the porridge is divided into motion and thermal energy, and the parts add up to the same amount as at the start. Thermal energy spreads so widely that it is no longer easy to put to use, and this is why energy seems to "run out".

<svg data-fig="sailyminen" viewBox="0 0 600 350" role="img" aria-label="Scale diagram (example): of the 800 kJ of chemical energy in the cyclist&#x27;s morning porridge, the muscles turn 200 kJ into motion and 600 kJ into thermal energy. The width of the arrows is proportional to the energy, and the combined width of the branches equals the width of the original arrow." style="max-width:100%;font-size:24px">
  <rect x="40" y="112" width="192" height="96" fill="#ffc078" stroke="#e8590c" stroke-width="2"/>
  <path d="M232,112 L400,112 L400,98 L452,124 L400,150 L400,136 L232,136 Z" fill="#ffc078" stroke="#e8590c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M232,136 L304,136 L304,262 L326,262 L268,302 L210,262 L232,262 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="100" y="23.5" width="400" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$800\,\text{kJ} = 200\,\text{kJ} + 600\,\text{kJ}$</div></foreignObject>
  <foreignObject x="52" y="129.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{chemical}$</div></foreignObject>
  <foreignObject x="52" y="167.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800\,\text{kJ}$</div></foreignObject>
  <foreignObject x="244" y="63.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{motion: }200\,\text{kJ}$</div></foreignObject>
  <foreignObject x="340" y="217.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{heat: }600\,\text{kJ}$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="460" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{the width of the arrow shows the amount of energy}$</div></foreignObject>
</svg>

### Joule
The symbol of energy is $E$ and its unit is the joule, whose symbol is J. One joule is a small amount of energy: it is roughly what is needed to lift an apple of about $0.1\,\text{kg}$ by one metre. In this chapter you learn the size of the joule through examples.

## Formula: Unit of energy and its multiples
Everyday energies are large numbers when given in joules, so we use prefixes (chapter *Quantities, units and the SI system*): kilo (k), mega (M), giga (G) and tera (T). Each of them is a thousand times the previous one:
```latex
\begin{aligned}
1\,\text{kJ} &= 1000\,\text{J} \\
1\,\text{MJ} &= 1000\,\text{kJ} \\
1\,\text{GJ} &= 1000\,\text{MJ} \\
1\,\text{TJ} &= 1000\,\text{GJ}
\end{aligned}
```
where J is the joule, kJ the kilojoule, MJ the megajoule, GJ the gigajoule and TJ the terajoule. So a megajoule contains $1000 \cdot 1000\,\text{J} = 1\,000\,000\,\text{J}$.

A conversion is done by replacing the prefix with its value: $2.5\,\text{kJ} = 2.5 \cdot 1000\,\text{J} = 2500\,\text{J}$. In the other direction, the number is written using the prefix: $3000\,\text{J} = 3 \cdot 1000\,\text{J} = 3\,\text{kJ}$. Energies are added together only in the same unit, so they are first converted to the same unit.

The orders of magnitude of everyday energies are collected in the figure, where each step is a factor of ten (chapter *Physics as a science and the scales of the universe*). When the orders of magnitude of two energies are very different, one division is enough for the comparison: the ratio of the $32\,\text{MJ}$ of a litre of petrol to the $10\,\text{MJ}$ of a day's food is $32\,\text{MJ} : 10\,\text{MJ} \approx 3$.

<svg data-fig="tikapuut" viewBox="0 0 600 372" role="img" aria-label="Scale diagram: energy in joules on a power-of-ten scale from 1 J to 10 TJ and beyond. Each step is a factor of ten. An apple lifted one metre is about 1 J, a burning match about 1 kJ, a day&#x27;s food about 10 MJ, a 50-litre petrol tank about 1.6 GJ, and the Olkiluoto 3 nuclear power plant produces about 140 TJ of electricity in a day." style="max-width:100%;font-size:24px">
  <line x1="66" y1="292" x2="574" y2="292" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M586,292 L573,298 L573,286 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="292" x2="96" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="129" y1="292" x2="129" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="162.5" y1="292" x2="162.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="195.5" y1="292" x2="195.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="229" y1="292" x2="229" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="292" x2="262" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="295" y1="292" x2="295" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="328.5" y1="292" x2="328.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361.5" y1="292" x2="361.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="292" x2="395" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="428" y1="292" x2="428" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="461" y1="292" x2="461" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="494.5" y1="292" x2="494.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="527.5" y1="292" x2="527.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="561" y1="292" x2="561" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="51" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{J}$</div></foreignObject>
  <foreignObject x="150.5" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{kJ}$</div></foreignObject>
  <foreignObject x="250" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{MJ}$</div></foreignObject>
  <foreignObject x="350" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{GJ}$</div></foreignObject>
  <foreignObject x="449.5" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{TJ}$</div></foreignObject>
  <foreignObject x="130" y="335.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{each step is a factor of 10}$</div></foreignObject>
  <line x1="96" y1="264" x2="96" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="96" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="106" y="237.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{apple lifted one metre}\ 1\,\text{J}$</div></foreignObject>
  <line x1="195.5" y1="226" x2="195.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="195.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="-4.5" y="199.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{match}\ 1\,\text{kJ}$</div></foreignObject>
  <line x1="328.5" y1="188" x2="328.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="328.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="58.5" y="161.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{day's food}\ 10\,\text{MJ}$</div></foreignObject>
  <line x1="401.5" y1="150" x2="401.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="401.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="91.5" y="123.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{petrol tank}\ 1.6\,\text{GJ}$</div></foreignObject>
  <line x1="565.5" y1="112" x2="565.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="565.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="215.5" y="85.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{Olkiluoto 3, per day}\ 140\,\text{TJ}$</div></foreignObject>
</svg>

The amount of energy does not yet tell how fast the energy is used. That is described in the next chapter, *Power*.

## Worked example
A cyclist eats a banana whose chemical energy is $0.45\,\text{MJ}$. The muscles turn $110\,\text{kJ}$ of it into the motion of cycling, and the rest turns into thermal energy. How much energy turns into thermal energy in the muscles and the body? Give the answer in kilojoules.

<!-- vaihe -->

**Given and find.** The chemical energy at the start is $E_\text{start} = 0.45\,\text{MJ}$ and the energy that turned into motion is $E_\text{motion} = 110\,\text{kJ}$. The thermal energy $E_\text{heat}$ is to be found in kilojoules.

<!-- vaihe -->

**Principle.** Energy is conserved: the chemical energy of the banana does not disappear but turns entirely into motion and thermal energy. So the energy at the start is equal to the sum of the energies that turned into motion and thermal energy.

<!-- vaihe -->

**Rearranged formula.**
```latex
\begin{aligned}
&E_\text{start} = E_\text{motion} + E_\text{heat} \\
&E_\text{heat} = E_\text{start} - E_\text{motion}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The energies are calculated in the same unit. Replace the prefix mega with its value: $0.45\,\text{MJ} = 0.45 \cdot 1000\,\text{kJ} = 450\,\text{kJ}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
E_\text{heat} &= E_\text{start} - E_\text{motion} \\
&= 450\,\text{kJ} - 110\,\text{kJ} \\
&= 340\,\text{kJ}
\end{aligned}
```

<!-- vaihe -->

**Result.** The thermal energy produced is $340\,\text{kJ}$. The result is rounded to two significant figures, because the initial energy $0.45\,\text{MJ}$ and the motion $110\,\text{kJ}$ are given with two figures.

<!-- vaihe -->

**Reasonableness.** More energy turns into thermal energy than into motion, as is usual in human muscles: the body warms up when you cycle. The sum checks out: $110\,\text{kJ} + 340\,\text{kJ} = 450\,\text{kJ}$, which is the same as at the start.

## Common misconception
Many people think that energy runs out when the speed slows down or the battery goes flat. Energy does not run out and does not disappear. It changes form, and a large part ends up as heat in the surroundings, from where it can no longer easily be collected back for use.

Another mistake is to add energies in different units, for example $1.5\,\text{MJ} + 300\,\text{kJ} = 301.5$. A prefix is a multiplier, so the energies are first converted to the same unit.

## Summary
- Energy changes from one form to another in a chain, for example radiation, chemical energy, kinetic energy and thermal energy.
- Energy is conserved (chapter *Forms of energy and conservation of energy*). At every step part of it turns into thermal energy, which is transferred as heat to the surroundings.
- The unit of energy is the joule (J). Prefixes: $1\,\text{kJ} = 1000\,\text{J}$, $1\,\text{MJ} = 1000\,\text{kJ}$, $1\,\text{GJ} = 1000\,\text{MJ}$ and $1\,\text{TJ} = 1000\,\text{GJ}$.
- A prefix is replaced by its value: $2.5\,\text{kJ} = 2.5 \cdot 1000\,\text{J}$. Energies are added in the same unit.
- Everyday energies range from joules to terajoules, and they are compared using powers of ten.
