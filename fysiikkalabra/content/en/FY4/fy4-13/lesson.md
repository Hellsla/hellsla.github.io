# Equation of motion for connected bodies

> **Why** does a mass hanging over the edge of a table fall more slowly than a freely falling object when it pulls a cart along the table with a string?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a physics classroom table. On the table is a cart carrying two metal masses. A string tied to the cart passes over a pulley at the edge of the table, and a single metal mass hangs from the other end of the string. A measuring scale and a stopwatch lie on the table, and a student stands beside it." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy413h-wall" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="470"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy413h-win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy413h-floor" gradientUnits="userSpaceOnUse" x1="0" y1="470" x2="0" y2="600"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-leg110" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-leg760" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-cart" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy413h-m290" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy413h-m362" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy413h-hang" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="470" fill="url(#fy413h-wall)"/>
  <rect x="880" y="70" width="240" height="230" rx="4" fill="url(#fy413h-win)" stroke="#1f2933" stroke-width="3"/>
  <path d="M933,176 Q932,160 951,162 Q958.5,144.5 978,150.5 Q995,140.5 1005,159 Q1022,161 1020,176 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="1000" y1="70" x2="1000" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="880" y1="185" x2="1120" y2="185" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="868" y="300" width="264" height="14" rx="3" fill="#c9c2b2" stroke="#1f2933" stroke-width="3"/>
  <rect x="70" y="110" width="300" height="14" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="3"/>
  <rect x="100" y="64" width="60" height="46" rx="8" fill="#a5d8ff" stroke="#1f2933" stroke-width="3"/>
  <rect x="190" y="64" width="60" height="46" rx="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/>
  <rect x="280" y="64" width="60" height="46" rx="8" fill="#b2f2bb" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy413h-floor)"/>
  <line x1="0" y1="492" x2="1200" y2="492" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="514" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="536" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="558" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="580" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="602" x2="1200" y2="602" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="110" y="354" width="26" height="170" fill="url(#fy413h-leg110)" stroke="#1f2933" stroke-width="3"/>
  <rect x="760" y="354" width="26" height="170" fill="url(#fy413h-leg760)" stroke="#1f2933" stroke-width="3"/>
  <rect x="70" y="330" width="770" height="24" rx="3" fill="url(#fy413h-top)" stroke="#1f2933" stroke-width="3"/>
  <path d="M130,344 q200,-4 400,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M170,340 q200,-4 400,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M210,344 q200,-4 400,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <rect x="120" y="336" width="560" height="12" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="124" y1="336" x2="124" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="134" y1="336" x2="134" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="143.5" y1="336" x2="143.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="153.5" y1="336" x2="153.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163" y1="336" x2="163" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="173" y1="336" x2="173" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="183" y1="336" x2="183" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="336" x2="192.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="202.5" y1="336" x2="202.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="212" y1="336" x2="212" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="222" y1="336" x2="222" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="232" y1="336" x2="232" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="241.5" y1="336" x2="241.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="251.5" y1="336" x2="251.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="261" y1="336" x2="261" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="271" y1="336" x2="271" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="281" y1="336" x2="281" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290.5" y1="336" x2="290.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300.5" y1="336" x2="300.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="336" x2="310" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="336" x2="320" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="336" x2="330" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="339.5" y1="336" x2="339.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="349.5" y1="336" x2="349.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="336" x2="359" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="369" y1="336" x2="369" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="379" y1="336" x2="379" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="388.5" y1="336" x2="388.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398.5" y1="336" x2="398.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="408" y1="336" x2="408" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="418" y1="336" x2="418" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428" y1="336" x2="428" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="437.5" y1="336" x2="437.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="447.5" y1="336" x2="447.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="457" y1="336" x2="457" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="467" y1="336" x2="467" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="477" y1="336" x2="477" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="486.5" y1="336" x2="486.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496.5" y1="336" x2="496.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="506" y1="336" x2="506" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="516" y1="336" x2="516" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="526" y1="336" x2="526" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="535.5" y1="336" x2="535.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="545.5" y1="336" x2="545.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="555" y1="336" x2="555" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="565" y1="336" x2="565" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="575" y1="336" x2="575" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="584.5" y1="336" x2="584.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="594.5" y1="336" x2="594.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="604" y1="336" x2="604" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="614" y1="336" x2="614" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="624" y1="336" x2="624" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="633.5" y1="336" x2="633.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="643.5" y1="336" x2="643.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="653" y1="336" x2="653" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="663" y1="336" x2="663" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="673" y1="336" x2="673" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="145" y="252.5" width="9.5" height="7" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="148" y="259" width="4" height="4" fill="#6c757d"/>
  <circle cx="150" cy="292" r="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="150" cy="292" r="24.6" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="271.5" x2="150" y2="268.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="274.5" x2="161.5" y2="271.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="167.5" y1="282" x2="170.5" y2="280.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="170.5" y1="292" x2="173.5" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="167.5" y1="302" x2="170.5" y2="303.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="309.5" x2="161.5" y2="312.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="312.5" x2="150" y2="315.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="140" y1="309.5" x2="138.5" y2="312.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="132.5" y1="302" x2="129.5" y2="303.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="129.5" y1="292" x2="126.5" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="132.5" y1="282" x2="129.5" y2="280.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="140" y1="274.5" x2="138.5" y2="271.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="292" x2="168" y2="283.5" stroke="#c92a2a" stroke-width="2.1" stroke-linecap="round"/>
  <circle cx="150" cy="292" r="2.4" fill="#1f2933"/>
  <rect x="250" y="262" width="200" height="34" rx="5" fill="url(#fy413h-cart)" stroke="#1f2933" stroke-width="3"/>
  <rect x="260" y="270" width="180" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <rect x="290" y="218" width="56" height="44" rx="6" fill="url(#fy413h-m290)" stroke="#1f2933" stroke-width="3"/>
  <rect x="298" y="226" width="40" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <rect x="362" y="218" width="56" height="44" rx="6" fill="url(#fy413h-m362)" stroke="#1f2933" stroke-width="3"/>
  <rect x="370" y="226" width="40" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="286" cy="312" r="22" fill="#1f2933"/>
  <circle cx="286" cy="312" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="286" cy="312" r="4" fill="#1f2933"/>
  <circle cx="414" cy="312" r="22" fill="#1f2933"/>
  <circle cx="414" cy="312" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="414" cy="312" r="4" fill="#1f2933"/>
  <rect x="448" y="270" width="14" height="6" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M812,330 V318 Q812,290 872,290" fill="none" stroke="#6c757d" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="796" y="316" width="34" height="18" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="872" cy="290" r="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="872" cy="290" r="21" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <line x1="878" y1="290" x2="893" y2="290" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="875" y1="295" x2="882.5" y2="308" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="869" y1="295" x2="861.5" y2="308" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="866" y1="290" x2="851" y2="290" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="869" y1="285" x2="861.5" y2="272" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="875" y1="285" x2="882.5" y2="272" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="872" cy="290" r="6" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M462,273 H872 A30,30 0 0 1 902,290 V396" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M888,396 h28 v14 h-28 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="874" y="410" width="56" height="44" rx="6" fill="url(#fy413h-hang)" stroke="#1f2933" stroke-width="3"/>
  <rect x="882" y="418" width="40" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <ellipse cx="902" cy="472" rx="46" ry="8" fill="#1f2933" fill-opacity="0.12"/>
  <path d="M989.5,560 L994.5,443 H1025.5 L1030.5,560 H1014.5 L1010,482 L1005.5,560 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M983.5,451 Q980.5,365 1010,360.5 Q1039.5,365 1036.5,451 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M986.5,376 L979,451" fill="none" stroke="#1971c2" stroke-width="17.16" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="979" cy="457" r="8.58" fill="#f1dfb5"/>
  <path d="M1033.5,376 L1041,451" fill="none" stroke="#1971c2" stroke-width="17.16" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1041" cy="457" r="8.58" fill="#f1dfb5"/>
  <rect x="1003" y="344.5" width="14" height="18.5" fill="#f1dfb5"/>
  <circle cx="1010" cy="329" r="23.4" fill="#f1dfb5"/>
  <path d="M986,329 Q986.5,301 1010,302.5 Q1035,302.5 1034,326 Q1014.5,316.5 986,329 Z" fill="#1f2933" stroke-linejoin="round"/>
</svg>

## Key idea
Often two bodies move together because a string joins them. When the string is taut and does not stretch, the bodies travel the same distance in the same time, so their accelerations have the same magnitude $a$. The string passes a force from one body to the other: it pulls each body toward itself. In this chapter the string is light and inextensible, the pulley is light and frictionless, and friction on the table and air resistance are neglected.

Connected bodies are treated one at a time. Each gets its own free-body diagram that shows only the forces acting on it, and each gets its own equation of motion. In the figure, the cart is acted on by its weight $\overline{G}_1$, the normal force $\overline{N}$ from the table and the tension $\overline{T}_1$ in the string. The hanging mass is acted on by its weight $\overline{G}_2$ and the tension $\overline{T}_2$ in the string.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Two bodies and their free-body diagrams. On the left, the situation: a cart on a table, and a string tied to it passes over a pulley at the table&#x27;s edge to a hanging mass. Above the cart are thin arrows: a blue velocity to the right and a shorter orange acceleration to the right. Top right, the free-body diagram of the cart, drawn as a rectangle: weight G1 down from the centre, the normal force N from the table up from the bottom surface and as long as the weight, and the tension T1 in the string to the right from the right edge. Bottom right, the free-body diagram of the hanging mass: weight G2 down from the centre and the tension T2 in the string up from the top surface. The arrow T2 is shorter than G2, and the arrows T1 and T2 are equally long." style="max-width:100%;font-size:24px">
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <rect x="20" y="176" width="214" height="12" rx="2" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="28" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="190" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="10" y1="296" x2="290" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="244" cy="164" r="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="244" cy="164" r="7" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="244" cy="164" r="2.5" fill="#1f2933"/>
  <rect x="226" y="172" width="12" height="10" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="70" y="146" width="60" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="83" cy="169" r="7" fill="#1f2933"/>
  <circle cx="117" cy="169" r="7" fill="#1f2933"/>
  <circle cx="83" cy="169" r="3" fill="#c4ccd4"/>
  <circle cx="117" cy="169" r="3" fill="#c4ccd4"/>
  <rect x="82" y="132" width="36" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M130,156 H244 A12,12 0 0 1 256,164 V236" fill="none" stroke="#b8622d" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="244" y="236" width="24" height="32" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="236" x2="256" y2="232" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="82" y1="124" x2="140" y2="124" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M129,130.5 L142,124 L129,117.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="82" y1="84" x2="120" y2="84" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M109,90.5 L122,84 L109,77.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="197.5" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="332" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="182" x2="590" y2="182" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: cart}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: mass}$</div></foreignObject>
  <rect x="400" y="88" width="80" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="108" x2="440" y2="150" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,167 L432,149 L448,149 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="148.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="418" y1="128" x2="418" y2="86" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M418,69 L426,87 L410,87 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="56.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="480" y1="102" x2="482.5" y2="102" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M499.5,102 L481.5,110 L481.5,94 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="499" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <rect x="412" y="254" width="56" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="276" x2="440" y2="288.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,305.5 L432,287.5 L448,287.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="293" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="254" x2="440" y2="251.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,234.5 L448,252.5 L432,252.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="222" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

The string pulls the cart with the force $\overline{T}_1$ and the hanging mass with the force $\overline{T}_2$. They act on different bodies, so they appear in different free-body diagrams. A light string and a frictionless pulley only pass the force on and turn its direction, so the magnitudes are equal: $T_1 = T_2 = T$. The forces $\overline{T}_1$ and $\overline{T}_2$ are nevertheless not an action–reaction pair. When the string pulls the cart, the cart pulls the string back with an equally large force, and that force acts on the string and is not in the cart's free-body diagram.

When the hanging mass accelerates downward, the tension in the string is smaller than its weight. The acceleration is downward, so the net force on the mass points down and $G_2 > T$. If $T$ were equal to $G_2$, the net force on the mass would be zero and it would not start to move. The mass therefore descends more slowly than a freely falling object: the acceleration $a = \tfrac{m_2 g}{m_1 + m_2}$ is smaller than $g$, because the weight of the hanging mass also accelerates the cart.

## Formula: Equations of motion for connected bodies
Each body gets its own equation of motion $\Sigma F = ma$. The positive direction is chosen separately for each body along its acceleration: to the right for the cart and down for the hanging mass. Because the string does not stretch, both bodies have the same acceleration magnitude $a$. The equations of the cart and the hanging mass are
```latex
\begin{aligned}
T &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
where $m_1$ is the mass of the cart (kg), $m_2$ the mass of the hanging mass (kg), $T$ the tension in the string (N), $a$ the acceleration (m/s²) and $g = 9.81\,\text{m/s}^2$. There are two unknowns, $a$ and $T$, and two equations.

When the equations are added side by side, $T$ cancels, because the string is an internal force between the bodies. This gives the acceleration and then the tension:
```latex
\begin{aligned}
a &= \frac{m_2}{m_1 + m_2}\,g \\
T &= m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
The tension is always smaller than the weight $m_2 g$ of the hanging mass, because $\tfrac{m_1}{m_1 + m_2} < 1$. The heavier the cart is compared with the hanging mass, the less the bodies accelerate and the closer $T$ is to the weight $m_2 g$.

### Two hanging bodies
When a body hangs at each end of the string, the heavier one ($m_2$) goes down and the lighter one ($m_1$) goes up. The positive direction is chosen along the motion: up for the lighter body and down for the heavier one. Then
```latex
\begin{aligned}
T - m_1 g &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
```latex
\begin{aligned}
a &= \frac{m_2 - m_1}{m_1 + m_2}\,g \\
T &= \frac{2 m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
where $m_2 > m_1$. The tension lies between the weights $m_1 g$ and $m_2 g$ of the bodies. If the masses are equal, $a = 0$ and $T = mg$.

<svg data-fig="atwood" viewBox="0 0 600 380" role="img" aria-label="Two hanging bodies and their free-body diagrams. On the left, the situation: a string passes over a pulley hanging from the ceiling, with a lighter body on its left end and a heavier one on its right end. Beside the lighter body is an orange arrow up and beside the heavier one an equally long orange arrow down: the acceleration has the same magnitude. Top right, the free-body diagram of the lighter body, drawn as a rectangle: tension T1 up from the top surface and weight G1 down from the centre, with T1 longer than G1. Bottom right, the free-body diagram of the heavier body: T2 up from the top surface and G2 down from the centre, with G2 longer than T2. The arrows T1 and T2 are equally long." style="max-width:100%;font-size:24px">
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <line x1="70" y1="56" x2="190" y2="56" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="70" y1="56" x2="60" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="56" x2="76" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="102" y1="56" x2="92" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="118" y1="56" x2="108" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="134" y1="56" x2="124" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="56" x2="140" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="166" y1="56" x2="156" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="182" y1="56" x2="172" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="56" x2="130" y2="92" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="130" cy="104" r="22" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="130" cy="104" r="17" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="130" cy="104" r="2.5" fill="#1f2933"/>
  <line x1="108" y1="104" x2="108" y2="206" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="152" y1="104" x2="152" y2="242" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="94" y="206" width="28" height="31.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="134" y="242" width="36" height="37" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="60" y1="236" x2="60" y2="194" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M66.5,205 L60,192 L53.5,205" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="21.5" y="173.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="212" y1="252" x2="212" y2="294" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M205.5,283 L212,296 L218.5,283" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="217.5" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="91.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="135.5" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="368" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="190" x2="590" y2="190" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: light}$</div></foreignObject>
  <foreignObject x="312" y="191.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: heavy}$</div></foreignObject>
  <rect x="412" y="110" width="56" height="36" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="128" x2="440" y2="137.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,154.5 L432,136.5 L448,136.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="142" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="440" y1="110" x2="440" y2="91.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,74.5 L448,92.5 L432,92.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="62" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <line x1="540" y1="150" x2="540" y2="108" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M546.5,119 L540,106 L533.5,119" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="545.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <rect x="408" y="278" width="64" height="48" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="302" x2="440" y2="338" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,355 L432,337 L448,337 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="342.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="278" x2="440" y2="259.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,242.5 L448,260.5 L432,260.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="230" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
  <line x1="540" y1="280" x2="540" y2="322" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M533.5,311 L540,324 L546.5,311" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="545.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

### Method for connected bodies
1. **Draw a free-body diagram** for each body. The string pulls each body toward itself, and each body has its own tension arrow.
2. **Choose the positive direction** for each body along its acceleration.
3. **Write the equation of motion** $\Sigma F = ma$ for each body separately. The acceleration magnitude $a$ and the tension magnitude $T$ are the same in both. If a body is also pulled by an external force $\overline{F}$, that force belongs only in the free-body diagram and equation of motion of the body being pulled.
4. **Solve** the two equations: add them, so that $T$ cancels, or substitute the $T$ from one into the other.
5. **Check** the signs and compare: the tension is not equal to the weight of a hanging body when the bodies accelerate.

## Worked example
A cart of mass $1.5\,\text{kg}$ stands on a table. A string tied to it passes over a light pulley at the edge of the table, and a mass of $0.60\,\text{kg}$ hangs from the other end of the string. The cart is released from rest. Friction and air resistance are neglected, and the string is light and inextensible. What is the acceleration of the cart and what is the tension in the string?

<!-- vaihe -->

**Given and find.** $m_1 = 1.5\,\text{kg}$, $m_2 = 0.60\,\text{kg}$ and $g = 9.81\,\text{m/s}^2$. We want the acceleration $a$ and the tension $T$ in the string.

<!-- vaihe -->

**Principle.** The cart and the hanging mass are two bodies, so each gets its own equation of motion. The string does not stretch, so the accelerations of the bodies have the same magnitude $a$. The string is light and the pulley is light and frictionless, so the string pulls both bodies with the same force $T$. There is no friction, so in the horizontal direction only the string acts on the cart.

<!-- vaihe -->

**Free-body diagram.** Each body has its own free-body diagram. The positive direction is to the right for the cart and down for the hanging mass. The cart does not accelerate vertically, so $N = G_1$. In the horizontal direction the cart is pulled only by $\overline{T}_1$. The hanging mass is acted on by $\overline{G}_2$ downward and $\overline{T}_2$ upward.

<svg data-fig="esimerkki" viewBox="0 0 600 340" role="img" aria-label="The cart and hanging mass of the example. On the left, the situation: the cart on the table, the string over a pulley to the hanging mass, and above the cart a blue velocity and an orange acceleration to the right. Top right, the free-body diagram of the cart: weight G1 down, the equally long normal force N up and the tension T1 to the right. Bottom right, the free-body diagram of the hanging mass: weight G2 down and the shorter tension T2 up. The arrows T1 and T2 are equally long." style="max-width:100%;font-size:24px">
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <rect x="20" y="176" width="214" height="12" rx="2" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="28" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="190" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="10" y1="296" x2="290" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="244" cy="164" r="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="244" cy="164" r="7" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="244" cy="164" r="2.5" fill="#1f2933"/>
  <rect x="226" y="172" width="12" height="10" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="70" y="146" width="60" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="83" cy="169" r="7" fill="#1f2933"/>
  <circle cx="117" cy="169" r="7" fill="#1f2933"/>
  <circle cx="83" cy="169" r="3" fill="#c4ccd4"/>
  <circle cx="117" cy="169" r="3" fill="#c4ccd4"/>
  <rect x="82" y="132" width="36" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M130,156 H244 A12,12 0 0 1 256,164 V236" fill="none" stroke="#b8622d" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="244" y="236" width="24" height="32" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="236" x2="256" y2="232" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="82" y1="124" x2="140" y2="124" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M129,130.5 L142,124 L129,117.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="82" y1="84" x2="120" y2="84" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M109,90.5 L122,84 L109,77.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="197.5" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="332" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="182" x2="590" y2="182" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: cart}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: mass}$</div></foreignObject>
  <rect x="400" y="88" width="80" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="108" x2="440" y2="157" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,174 L432,156 L448,156 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="155.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="418" y1="128" x2="418" y2="79" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M418,62 L426,80 L410,80 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="480" y1="102" x2="482" y2="102" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M499,102 L481,110 L481,94 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="498.5" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <rect x="412" y="254" width="56" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="276" x2="440" y2="285.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,302.5 L432,284.5 L448,284.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="290" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="254" x2="440" y2="252" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,235 L448,253 L432,253 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="222.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Rearranged formula.** The two equations of motion are read from the diagrams and solved:
```latex
\begin{aligned}
&T = m_1 a \\
&m_2 g - T = m_2 a \\
&m_2 g = (m_1 + m_2) a \\
&a = \frac{m_2 g}{m_1 + m_2} \\
&T = m_1 a
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: the masses are in kilograms and $\tfrac{\text{kg} \cdot \text{m/s}^2}{\text{kg}} = \text{m/s}^2$.

<!-- vaihe -->

**Substitution.** The numerical values are substituted with their units:
```latex
\begin{aligned}
&a = \frac{m_2 g}{m_1 + m_2} \\
&\phantom{a} = \frac{0.60\,\text{kg} \cdot 9.81\,\text{m/s}^2}{1.5\,\text{kg} + 0.60\,\text{kg}} \\
&\phantom{a} \approx 2.80\,\text{m/s}^2 \\[4pt]
&T = m_1 a = 1.5\,\text{kg} \cdot 2.803\,\text{m/s}^2 \\
&\phantom{T} \approx 4.20\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration of the cart is $a \approx 2.8\,\text{m/s}^2$ and the tension in the string is $T \approx 4.2\,\text{N}$, with two significant figures like the masses $1.5\,\text{kg}$ and $0.60\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** The weight of the hanging mass is $m_2 g \approx 5.9\,\text{N}$, and the tension $4.2\,\text{N}$ is smaller than that, as it should be. The net force on the hanging mass is $5.886\,\text{N} - 4.204\,\text{N} \approx 1.68\,\text{N}$, and this equals $m_2 a = 0.60\,\text{kg} \cdot 2.803\,\text{m/s}^2 \approx 1.68\,\text{N}$. The acceleration is smaller than $g$, because the hanging mass also accelerates the cart. Without the cart, the mass would fall with acceleration $g$.

## Common misconception
People often think that the cart is pulled by the weight of the hanging mass, so that the tension would be $m_2 g$. The cart is pulled by the string, however, and the force of the string is $T$. Only when the bodies do not accelerate, for example when the cart is held still, is $T = m_2 g$. When the hanging mass descends with increasing speed, its net force $G_2 - T = m_2 a$ must point down, so $T < m_2 g$.

Another mistake is to treat the forces $\overline{T}_1$ and $\overline{T}_2$ as an action–reaction pair. They act on different bodies but belong to different interactions: one to the string–cart pair and the other to the string–mass pair. They are equal because the string is light and the pulley is light and frictionless, not because they would be the forces of one interaction pair. A third mistake is to think that the heavier body accelerates more. Bodies at the ends of an inextensible string have the same acceleration magnitude.

## Summary
- Bodies connected by a string or over a pulley each have their own free-body diagram and their own equation of motion $\Sigma F = ma$, and the positive direction is chosen for each body along its acceleration.
- A light, inextensible string and a light, frictionless pulley give the bodies the same acceleration magnitude $a$ and equal tensions $T_1 = T_2 = T$.
- For a cart and a hanging mass, $a = \frac{m_2}{m_1 + m_2}\,g$ and $T = \frac{m_1 m_2}{m_1 + m_2}\,g$. For two hanging bodies, $a = \frac{m_2 - m_1}{m_1 + m_2}\,g$ and $T = \frac{2 m_1 m_2}{m_1 + m_2}\,g$.
- The tension for an accelerating hanging body is not its weight: for the cart and the hanging mass $T < m_2 g$, and for two hanging bodies $T$ lies between the weights.
- The tensions $\overline{T}_1$ and $\overline{T}_2$ act on different bodies and are not an action–reaction pair.
