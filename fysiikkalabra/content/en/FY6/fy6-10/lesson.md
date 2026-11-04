# Electric charge and Coulomb's law

> **Why** does a balloon rubbed on a wool sweater stick to a wall, although the wall has no electric charge?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a pale wall in a room, with a blue balloon staying stuck to the wall without tape, its string hanging down. On the right a wool sweater hangs on the back of a chair. On the left a plastic comb lies on a table, and small bits of paper rise from the table towards it." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy610h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><linearGradient id="fy610h-floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy610h-balloon" cx="0.35" cy="0.3" r="0.85"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></radialGradient><linearGradient id="fy610h-leg1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy610h-leg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy610h-wool" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient><linearGradient id="fy610h-top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="430" fill="url(#fy610h-wall)"/>
  <rect x="0" y="420" width="1200" height="14" fill="#c9c2b2"/>
  <rect x="0" y="434" width="1200" height="166" fill="url(#fy610h-floor)"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="500" x2="1200" y2="500" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="530" x2="1200" y2="530" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="560" x2="1200" y2="560" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="590" x2="1200" y2="590" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="612" cy="226" rx="98" ry="118" fill="#c9c2b2" fill-opacity="0.35"/>
  <path d="M600,346 C590,380 616,410 600,446 C586,480 612,510 598,540" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M590,344 L600,328 L610,344 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <ellipse cx="600" cy="210" rx="98" ry="120" fill="url(#fy610h-balloon)" stroke="#1f2933" stroke-width="3"/>
  <path d="M548,140 Q560,112 590,104" fill="none" stroke="#ffffff" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.7"/>
  <rect x="880" y="210" width="18" height="330" rx="6" fill="url(#fy610h-leg1)" stroke="#1f2933" stroke-width="3"/>
  <rect x="1060" y="210" width="18" height="330" rx="6" fill="url(#fy610h-leg2)" stroke="#1f2933" stroke-width="3"/>
  <rect x="866" y="196" width="226" height="30" rx="10" fill="#d9b26a" stroke="#1f2933" stroke-width="3"/>
  <rect x="866" y="392" width="226" height="28" rx="8" fill="#d9b26a" stroke="#1f2933" stroke-width="3"/>
  <path d="M880,206 L1080,206 L1102,330 Q1060,346 1040,322 L1020,268 L940,268 L920,322 Q898,346 858,330 Z" fill="url(#fy610h-wool)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M900,226 q11,9 22,0 M922,226 q11,9 22,0 M944,226 q11,9 22,0 M966,226 q11,9 22,0 M988,226 q11,9 22,0 M1010,226 q11,9 22,0 M1032,226 q11,9 22,0 M1054,226 q11,9 22,0" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M900,240 q11,9 22,0 M922,240 q11,9 22,0 M944,240 q11,9 22,0 M966,240 q11,9 22,0 M988,240 q11,9 22,0 M1010,240 q11,9 22,0 M1032,240 q11,9 22,0 M1054,240 q11,9 22,0" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M900,254 q11,9 22,0 M922,254 q11,9 22,0 M944,254 q11,9 22,0 M966,254 q11,9 22,0 M988,254 q11,9 22,0 M1010,254 q11,9 22,0 M1032,254 q11,9 22,0 M1054,254 q11,9 22,0" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M900,268 q11,9 22,0 M922,268 q11,9 22,0 M944,268 q11,9 22,0 M966,268 q11,9 22,0 M988,268 q11,9 22,0 M1010,268 q11,9 22,0 M1032,268 q11,9 22,0 M1054,268 q11,9 22,0" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <rect x="70" y="330" width="330" height="22" rx="6" fill="url(#fy610h-top)" stroke="#1f2933" stroke-width="3"/>
  <rect x="96" y="352" width="18" height="190" rx="5" fill="#a97a35" stroke="#1f2933" stroke-width="3"/>
  <rect x="356" y="352" width="18" height="190" rx="5" fill="#a97a35" stroke="#1f2933" stroke-width="3"/>
  <rect x="190" y="220" width="150" height="22" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="196" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="208" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="220" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="232" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="244" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="256" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="268" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="280" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="292" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="304" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="316" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="328" y="242" width="6" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="197" y="295" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(10 206 300)"/>
  <rect x="227" y="281" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(-18 236 286)"/>
  <rect x="253" y="301" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(24 262 306)"/>
  <rect x="283" y="285" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(8 292 290)"/>
  <rect x="309" y="307" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(-30 318 312)"/>
  <rect x="171" y="313" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(14 180 318)"/>
  <rect x="237" y="313" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(-6 246 318)"/>
  <rect x="291" y="315" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(40 300 320)"/>
  <rect x="321" y="319" width="18" height="10" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2" transform="rotate(-12 330 324)"/>
</svg>

## Key idea

### Electric charge and elementary charge
The atoms of matter contain positively charged protons and negatively charged electrons (chapter *Circuit, electric current and voltage*). **Electric charge** is a property of particles that makes them act on each other through the electric interaction: charges of the same sign repel each other and charges of opposite signs attract each other. The symbol of charge is $Q$ or $q$, and its unit is the coulomb $\text{C}$. The charge of a proton is $+e$ and that of an electron $-e$, where $e$ is the **elementary charge**, the smallest charge that occurs free. A neutron has no charge.

An ordinary object has as many protons as electrons, so its total charge is zero: the object is electrically neutral. An object is charged when it has more or fewer electrons than protons. Charge is always made of whole elementary charges:
```latex
Q = n e
```
where $Q$ is the magnitude of the charge of the object ($\text{C}$), $n$ is the number of extra or missing electrons and $e = 1.602 \cdot 10^{-19}\,\text{C}$ is the elementary charge. The coulomb is a large charge, since it takes $6.24 \cdot 10^{18}$ elementary charges. The charge of a balloon charged by rubbing is typically tens of nanocoulombs: a charge of $-50\,\text{nC}$ means about $3.1 \cdot 10^{11}$ extra electrons.

### Conservation of charge
Charge is neither created nor destroyed. The total charge of an isolated system, that is, the sum of all its charges, stays the same, even though charge moves from one object to another. This is the **law of conservation of charge**. When a balloon is rubbed on wool, some of the electrons of the wool move to the surface of the balloon. The balloon gets a negative charge, and the wool is left with an equal positive charge, because it is missing the same number of electrons. In solids it is the electrons that move; the protons stay in the nuclei of the atoms.

<svg data-fig="hankaus" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale, two panels. On the left before rubbing: the balloon and the wool cloth each have four positive and four negative charges, so each is neutral, Q = 0. On the right after rubbing: three electrons have moved from the wool to the balloon, shown by a blue arrow from the wool to the balloon. The balloon has four positive and seven negative charges, Q = −3e, and the wool has four positive and one negative charge, Q = +3e. The sum of the charges is still zero." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy610-ilma-ennen" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e3dccb"/></radialGradient><linearGradient id="fy610-villa-ennen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><radialGradient id="fy610-ilma-jalkeen" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e3dccb"/></radialGradient><linearGradient id="fy610-villa-jalkeen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#e9c98a"/></linearGradient></defs>
  <line x1="300" y1="14" x2="300" y2="346" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="65" y="11.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{before rubbing}$</div></foreignObject>
  <path d="M77,230 L84,218 L91,230 Z" fill="#c9c2b2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <ellipse cx="84" cy="150" rx="56" ry="70" fill="url(#fy610-ilma-ennen)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="168" y="92" width="116" height="120" rx="14" fill="url(#fy610-villa-ennen)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M178,110 q9,8 18,0 M196,110 q9,8 18,0 M214,110 q9,8 18,0 M232,110 q9,8 18,0 M250,110 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M178,132.5 q9,8 18,0 M196,132.5 q9,8 18,0 M214,132.5 q9,8 18,0 M232,132.5 q9,8 18,0 M250,132.5 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M178,155 q9,8 18,0 M196,155 q9,8 18,0 M214,155 q9,8 18,0 M232,155 q9,8 18,0 M250,155 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M178,177.5 q9,8 18,0 M196,177.5 q9,8 18,0 M214,177.5 q9,8 18,0 M232,177.5 q9,8 18,0 M250,177.5 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M178,200 q9,8 18,0 M196,200 q9,8 18,0 M214,200 q9,8 18,0 M232,200 q9,8 18,0 M250,200 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="62" cy="108" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="57" y1="108" x2="67" y2="108" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="62" y1="103" x2="62" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="104" cy="108" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="99" y1="108" x2="109" y2="108" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="50" cy="138" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="45" y1="138" x2="55" y2="138" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="50" y1="133" x2="50" y2="143" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="84" cy="136" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="79" y1="136" x2="89" y2="136" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="116" cy="138" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="111" y1="138" x2="121" y2="138" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="133" x2="116" y2="143" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="54" cy="168" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="49" y1="168" x2="59" y2="168" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="86" cy="166" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="81" y1="166" x2="91" y2="166" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="86" y1="161" x2="86" y2="171" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="114" cy="168" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="109" y1="168" x2="119" y2="168" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="190" cy="116" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="185" y1="116" x2="195" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="111" x2="190" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="226" cy="116" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="221" y1="116" x2="231" y2="116" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="262" cy="116" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="257" y1="116" x2="267" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="262" y1="111" x2="262" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="190" cy="152" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="185" y1="152" x2="195" y2="152" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="226" cy="152" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="221" y1="152" x2="231" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="226" y1="147" x2="226" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="262" cy="152" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="257" y1="152" x2="267" y2="152" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="208" cy="188" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="203" y1="188" x2="213" y2="188" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="208" y1="183" x2="208" y2="193" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="244" cy="188" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="239" y1="188" x2="249" y2="188" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="61.5" y="243.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = 0$</div></foreignObject>
  <foreignObject x="203.5" y="243.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = 0$</div></foreignObject>
  <foreignObject x="36.5" y="281.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{balloon}$</div></foreignObject>
  <foreignObject x="197" y="281.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{wool}$</div></foreignObject>
  <foreignObject x="371" y="11.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{after rubbing}$</div></foreignObject>
  <path d="M377,230 L384,218 L391,230 Z" fill="#c9c2b2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <ellipse cx="384" cy="150" rx="56" ry="70" fill="url(#fy610-ilma-jalkeen)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="468" y="92" width="116" height="120" rx="14" fill="url(#fy610-villa-jalkeen)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M478,110 q9,8 18,0 M496,110 q9,8 18,0 M514,110 q9,8 18,0 M532,110 q9,8 18,0 M550,110 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M478,132.5 q9,8 18,0 M496,132.5 q9,8 18,0 M514,132.5 q9,8 18,0 M532,132.5 q9,8 18,0 M550,132.5 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M478,155 q9,8 18,0 M496,155 q9,8 18,0 M514,155 q9,8 18,0 M532,155 q9,8 18,0 M550,155 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M478,177.5 q9,8 18,0 M496,177.5 q9,8 18,0 M514,177.5 q9,8 18,0 M532,177.5 q9,8 18,0 M550,177.5 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M478,200 q9,8 18,0 M496,200 q9,8 18,0 M514,200 q9,8 18,0 M532,200 q9,8 18,0 M550,200 q9,8 18,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="362" cy="108" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="357" y1="108" x2="367" y2="108" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="362" y1="103" x2="362" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="404" cy="108" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="399" y1="108" x2="409" y2="108" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="350" cy="138" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="345" y1="138" x2="355" y2="138" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="350" y1="133" x2="350" y2="143" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="384" cy="136" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="379" y1="136" x2="389" y2="136" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="416" cy="138" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="411" y1="138" x2="421" y2="138" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="416" y1="133" x2="416" y2="143" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="354" cy="168" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="349" y1="168" x2="359" y2="168" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="386" cy="166" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="381" y1="166" x2="391" y2="166" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="414" cy="168" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="409" y1="168" x2="419" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="414" y1="163" x2="414" y2="173" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="368" cy="196" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="363" y1="196" x2="373" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="400" cy="196" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="395" y1="196" x2="405" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="384" cy="90" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="379" y1="90" x2="389" y2="90" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="490" cy="116" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="485" y1="116" x2="495" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="490" y1="111" x2="490" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="526" cy="116" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="521" y1="116" x2="531" y2="116" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="562" cy="116" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="557" y1="116" x2="567" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="562" y1="111" x2="562" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="490" cy="152" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="485" y1="152" x2="495" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="490" y1="147" x2="490" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="526" cy="152" r="9" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="521" y1="152" x2="531" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="526" y1="147" x2="526" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="300" x2="411" y2="300" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M396,300 L412,293 L412,307 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="390" y="315.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{electrons}$</div></foreignObject>
  <foreignObject x="349" y="243.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = -3e$</div></foreignObject>
  <foreignObject x="491" y="243.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = +3e$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/balloon-hair.webp" alt="A hand holds a red balloon above long hair, and the hair rises towards the balloon."><figcaption>A balloon rubbed on hair attracts the hair. Rubbing moved electrons from the hair to the balloon, so the balloon became negatively charged and the hair positively charged. Opposite charges attract each other.</figcaption></figure>

### Charging objects
An object can be charged in three ways.

- **Rubbing.** Two different materials are rubbed against each other, and electrons move from the material that holds them more weakly to the other material. The objects become equally charged with opposite signs.
- **Contact.** A charged object touches a conductor, and some of the charge moves to the conductor. Two identical metal spheres share their common charge equally in contact: if the charges are first $+12\,\text{nC}$ and $0\,\text{nC}$, the charge of each is $+6\,\text{nC}$ after the contact.
- **Induction.** A charged object is brought near a conductor without touching it. The free electrons of the conductor move, so a charge of opposite sign appears on the near side of the conductor and a charge of the same sign on the far side. The total charge of the conductor does not change. However, if the conductor is connected to the ground for a moment with a wire, some electrons move to the ground or from the ground to the conductor, and the conductor is left charged.

### Why a charged object attracts a neutral object
Induction explains why a charged object also attracts a neutral object. The charge of opposite sign on a metal sphere is nearer to the charged rod than the charge of the same sign. The electric force weakens as the distance grows, so the attraction is greater than the repulsion, and the sphere is drawn towards the rod.

In an insulator the electrons cannot move from one object to another, but the charges in each molecule shift slightly: the molecule becomes **polarised**. Next to a negatively charged balloon, the positive ends of the molecules in the wall turn towards the balloon. The wall stays neutral, but the positive ends nearby attract the balloon more than the negative ends farther away repel it. That is why the balloon stays on the wall and the comb lifts bits of paper.

<svg data-fig="influenssi" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale, two panels. On the left a conductor: a negatively charged plastic rod is on the left of a metal sphere at the end of an insulating rod. The free electrons of the sphere have moved farther from the rod, so the surface of the sphere facing the rod has three positive charges and the opposite surface three negative charges; the sphere as a whole is neutral. A red force arrow points from the sphere towards the rod. On the right an insulator: a negatively charged balloon next to a wall. The charges in the molecules of the wall have shifted slightly so that the positive end of each molecule is towards the balloon. A red force arrow points from the balloon towards the wall." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy610-sauva" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><radialGradient id="fy610-metalli" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></radialGradient><linearGradient id="fy610-seina" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><radialGradient id="fy610-ilma-inf" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e3dccb"/></radialGradient></defs>
  <line x1="300" y1="14" x2="300" y2="346" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="90" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{conductor}$</div></foreignObject>
  <foreignObject x="390" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{insulator}$</div></foreignObject>
  <rect x="14" y="138" width="96" height="26" rx="13" fill="url(#fy610-sauva)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="36" cy="151" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="31.5" y1="151" x2="40.5" y2="151" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="62" cy="151" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="57.5" y1="151" x2="66.5" y2="151" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="88" cy="151" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="83.5" y1="151" x2="92.5" y2="151" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="12" y="179.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{plastic rod}$</div></foreignObject>
  <rect x="207" y="204" width="14" height="82" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="174" y="284" width="80" height="14" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="214" cy="151" r="54" fill="url(#fy610-metalli)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="172" cy="122" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="167.5" y1="122" x2="176.5" y2="122" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="172" y1="117.5" x2="172" y2="126.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="166" cy="151" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="161.5" y1="151" x2="170.5" y2="151" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="166" y1="146.5" x2="166" y2="155.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="172" cy="180" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="167.5" y1="180" x2="176.5" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="172" y1="175.5" x2="172" y2="184.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="256" cy="122" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="251.5" y1="122" x2="260.5" y2="122" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="262" cy="151" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="257.5" y1="151" x2="266.5" y2="151" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="256" cy="180" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="251.5" y1="180" x2="260.5" y2="180" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="228" y1="76" x2="169" y2="76" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M154,76 L170,69 L170,83 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="109" y="61.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="141.5" y="311.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{metal sphere}$</div></foreignObject>
  <rect x="470" y="56" width="116" height="248" fill="url(#fy610-seina)" stroke="#c9c2b2" stroke-width="2"/>
  <line x1="470" y1="56" x2="470" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="502" cy="82" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="490" y1="82" x2="498" y2="82" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="494" y1="78" x2="494" y2="86" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="506" y1="82" x2="514" y2="82" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="502" cy="122" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="490" y1="122" x2="498" y2="122" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="494" y1="118" x2="494" y2="126" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="506" y1="122" x2="514" y2="122" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="502" cy="162" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="490" y1="162" x2="498" y2="162" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="494" y1="158" x2="494" y2="166" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="506" y1="162" x2="514" y2="162" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="502" cy="202" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="490" y1="202" x2="498" y2="202" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="494" y1="198" x2="494" y2="206" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="506" y1="202" x2="514" y2="202" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="502" cy="242" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="490" y1="242" x2="498" y2="242" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="494" y1="238" x2="494" y2="246" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="506" y1="242" x2="514" y2="242" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="502" cy="282" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="490" y1="282" x2="498" y2="282" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="494" y1="278" x2="494" y2="286" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="506" y1="282" x2="514" y2="282" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="536" cy="82" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="524" y1="82" x2="532" y2="82" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="528" y1="78" x2="528" y2="86" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="540" y1="82" x2="548" y2="82" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="536" cy="122" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="524" y1="122" x2="532" y2="122" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="528" y1="118" x2="528" y2="126" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="540" y1="122" x2="548" y2="122" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="536" cy="162" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="524" y1="162" x2="532" y2="162" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="528" y1="158" x2="528" y2="166" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="540" y1="162" x2="548" y2="162" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="536" cy="202" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="524" y1="202" x2="532" y2="202" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="528" y1="198" x2="528" y2="206" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="540" y1="202" x2="548" y2="202" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="536" cy="242" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="524" y1="242" x2="532" y2="242" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="528" y1="238" x2="528" y2="246" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="540" y1="242" x2="548" y2="242" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="536" cy="282" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="524" y1="282" x2="532" y2="282" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="528" y1="278" x2="528" y2="286" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="540" y1="282" x2="548" y2="282" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="570" cy="82" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="558" y1="82" x2="566" y2="82" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="562" y1="78" x2="562" y2="86" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="574" y1="82" x2="582" y2="82" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="570" cy="122" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="558" y1="122" x2="566" y2="122" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="562" y1="118" x2="562" y2="126" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="574" y1="122" x2="582" y2="122" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="570" cy="162" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="558" y1="162" x2="566" y2="162" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="562" y1="158" x2="562" y2="166" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="574" y1="162" x2="582" y2="162" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="570" cy="202" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="558" y1="202" x2="566" y2="202" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="562" y1="198" x2="562" y2="206" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="574" y1="202" x2="582" y2="202" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="570" cy="242" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="558" y1="242" x2="566" y2="242" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="562" y1="238" x2="562" y2="246" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="574" y1="242" x2="582" y2="242" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="570" cy="282" rx="15" ry="10" fill="#ffffff" stroke="#6b7480" stroke-width="1.5"/>
  <line x1="558" y1="282" x2="566" y2="282" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="562" y1="278" x2="562" y2="286" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="574" y1="282" x2="582" y2="282" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M387,248 L394,236 L401,248 Z" fill="#c9c2b2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <ellipse cx="394" cy="176" rx="50" ry="62" fill="url(#fy610-ilma-inf)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="378" cy="150" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="373.5" y1="150" x2="382.5" y2="150" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="410" cy="150" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="405.5" y1="150" x2="414.5" y2="150" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="372" cy="180" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="367.5" y1="180" x2="376.5" y2="180" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="404" cy="182" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="399.5" y1="182" x2="408.5" y2="182" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="390" cy="210" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="385.5" y1="210" x2="394.5" y2="210" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="376" y1="82" x2="431" y2="82" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M446,82 L430,89 L430,75 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="333" y="67.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="346.5" y="275.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{balloon}$</div></foreignObject>
  <foreignObject x="499" y="311.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{wall}$</div></foreignObject>
</svg>

### Electric current is moving charge
When charge moves from one place to another, an electric current flows. In a conductor the current is the charge that passes through the cross-section in a unit of time, $I = Q : t$ (chapter *Circuit, electric current and voltage*). The same holds for a spark and for lightning. When you touch a door handle on a dry winter day, a charge, typically under a microcoulomb, is discharged from your body in a spark. The discharge lasts only about a microsecond, so the current is for a moment of the order of an ampere, although the charge that moves is small.

### There is an electric field around a charge
A charged object acts on another charged object without touching it. This is described with an electric field: a charge changes the space around it so that an electric force acts on another charge there. The field is illustrated with field lines. The direction of a field line is the direction in which the force on a small positive test charge points; the force on a negative charge points against the field line.

A **point charge** is a charged object whose size is small compared with the distances considered. From a positive point charge the field lines go out radially, and into a negative point charge they come in radially. Near the charge the lines are close together and the field is strong; farther away the lines spread out and the field weakens. The strength of the field is handled with calculations in the chapter *Uniform electric field*.

<svg data-fig="kentta" viewBox="0 0 600 340" role="img" aria-label="Schematic figure, not to scale, two panels. On the left a positive point charge with eight radial field lines around it, arrows pointing away from the charge. On the right a negative point charge whose field line arrows point towards the charge. On the right of each there is a small positive test charge, and a red force arrow points in the direction of the field line: away from the positive charge and towards the negative charge. The field lines are green and the force arrow red. The lines are close together near the charge and spread out farther away." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy610-q-p" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#f2a69c"/></radialGradient><radialGradient id="fy610-q-n" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#1971c2"/></radialGradient></defs>
  <line x1="300" y1="14" x2="300" y2="326" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="150" y1="150" x2="232" y2="150" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M197,150 L175,157.5 L175,142.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="141" y1="171" x2="199" y2="229" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M174.5,204.5 L153.5,194.5 L164.5,183.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="120" y1="180" x2="120" y2="262" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M120,227 L112.5,205 L127.5,205 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="99" y1="171" x2="41" y2="229" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M65.5,204.5 L75.5,183.5 L86.5,194.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="90" y1="150" x2="8" y2="150" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M43,150 L65,142.5 L65,157.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="99" y1="129" x2="41" y2="71" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M65.5,95.5 L86.5,105.5 L75.5,116.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="120" y1="120" x2="120" y2="38" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M120,73 L127.5,95 L112.5,95 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="141" y1="129" x2="199" y2="71" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M174.5,95.5 L164.5,116.5 L153.5,105.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="120" cy="150" r="22" fill="url(#fy610-q-p)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="110" y1="150" x2="130" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="140" x2="120" y2="160" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="224" cy="150" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="219.5" y1="150" x2="228.5" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="224" y1="145.5" x2="224" y2="154.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="234" y1="126" x2="263" y2="126" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M276,126 L262,132.5 L262,119.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="219.5" y="81.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="103.5" y="281.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+Q$</div></foreignObject>
  <line x1="450" y1="150" x2="532" y2="150" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M475,150 L497,142.5 L497,157.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="441" y1="171" x2="499" y2="229" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M459,189 L480,199 L469,210 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="420" y1="180" x2="420" y2="262" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M420,205 L427.5,227 L412.5,227 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="399" y1="171" x2="341" y2="229" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M381,189 L371,210 L360,199 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="390" y1="150" x2="308" y2="150" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M365,150 L343,157.5 L343,142.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="399" y1="129" x2="341" y2="71" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M381,111 L360,101 L371,90 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="420" y1="120" x2="420" y2="38" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M420,95 L412.5,73 L427.5,73 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="441" y1="129" x2="499" y2="71" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M459,111 L469,90 L480,101 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="420" cy="150" r="22" fill="url(#fy610-q-n)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="410" y1="150" x2="430" y2="150" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="524" cy="150" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="519.5" y1="150" x2="528.5" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="524" y1="145.5" x2="524" y2="154.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="554" y1="126" x2="525" y2="126" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M512,126 L526,119.5 L526,132.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="519.5" y="81.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="403.5" y="281.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-Q$</div></foreignObject>
  <foreignObject x="12" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{field line}$</div></foreignObject>
  <line x1="84" y1="40" x2="104" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="104" cy="70" r="3.5" fill="#6b7480"/>
</svg>

<figure class="unit-photo"><img src="pics/fy6/balloons-repel.webp" alt="Two yellow balloons hang on thin threads in front of a green chalkboard; the balloons are apart and the threads are slanted."><figcaption>Two balloons charged in the same way push each other apart, so the threads tilt. Each balloon is acted on by gravity, the tension of its thread and the electric force from the other balloon.</figcaption></figure>

## Formula: Coulomb's law
The magnitude of the electric force between two point charges is directly proportional to the product of the charges and inversely proportional to the square of the distance between them. This is **Coulomb's law**:
```latex
F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2}
```
where $F$ is the magnitude of the force ($\text{N}$), $q_1$ and $q_2$ are the charges ($\text{C}$), $r$ is the distance between the charges ($\text{m}$) and $k = 8.988 \cdot 10^{9}\,\tfrac{\text{N} \cdot \text{m}^2}{\text{C}^2}$ is the constant of Coulomb's law. The law holds for point charges and for uniformly charged spheres, whose distance is measured between the centres. The value of the constant holds in a vacuum; in air the force is almost the same.

### Force and reaction force
Coulomb's law gives the magnitude of the force. The direction of the force is worked out from the signs of the charges: the forces lie on the line between the charges, and charges of the same sign repel and charges of opposite signs attract each other. The charge $q_1$ acts on the charge $q_2$ with the force $\overline{F}_{12}$, and the charge $q_2$ acts on the charge $q_1$ with the force $\overline{F}_{21}$. They are a force and its reaction force, $\overline{F}_{12} = -\overline{F}_{21}$ (chapter *Interaction and force: Newton's first and third laws*), so they are equal in magnitude and opposite in direction, also when the charges are of different sizes. In the formula of the law the charges appear symmetrically, so the same $F$ acts on both charges.

<svg data-fig="coulomb" viewBox="0 0 600 364" role="img" aria-label="Schematic figure, not to scale. At the top charges of the same sign q1 and q2, both positive: the force F21 on the charge q1 points to the left, away from q2, and the force F12 on the charge q2 to the right, away from q1, so the charges repel each other. At the bottom charges of opposite signs, q1 positive and q2 negative: the forces point towards each other, so the charges attract each other. All four force arrows are equally long. At the very bottom the distance r between the centres of the charges." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy610-c1-0" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#f2a69c"/></radialGradient><radialGradient id="fy610-c2-0" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#f2a69c"/></radialGradient><radialGradient id="fy610-c1-1" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#f2a69c"/></radialGradient><radialGradient id="fy610-c2-1" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#1971c2"/></radialGradient></defs>
  <foreignObject x="140" y="7.5" width="320" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{charges of the same sign repel}$</div></foreignObject>
  <foreignObject x="115" y="177.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{charges of opposite signs attract}$</div></foreignObject>
  <line x1="12" y1="168" x2="588" y2="168" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <circle cx="200" cy="96" r="24" fill="url(#fy610-c1-0)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="400" cy="96" r="24" fill="url(#fy610-c2-0)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="190" y1="96" x2="210" y2="96" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="200" y1="86" x2="200" y2="106" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="390" y1="96" x2="410" y2="96" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="400" y1="86" x2="400" y2="106" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="174" y1="96" x2="119" y2="96" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M102,96 L120,88 L120,104 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="426" y1="96" x2="481" y2="96" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M498,96 L480,104 L480,88 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="109" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{21}$</div></foreignObject>
  <foreignObject x="433" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{12}$</div></foreignObject>
  <foreignObject x="183.5" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_1$</div></foreignObject>
  <foreignObject x="383.5" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_2$</div></foreignObject>
  <circle cx="200" cy="266" r="24" fill="url(#fy610-c1-1)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="400" cy="266" r="24" fill="url(#fy610-c2-1)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="190" y1="266" x2="210" y2="266" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="200" y1="256" x2="200" y2="276" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="390" y1="266" x2="410" y2="266" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <line x1="226" y1="266" x2="281" y2="266" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M298,266 L280,274 L280,258 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="374" y1="266" x2="319" y2="266" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M302,266 L320,258 L320,274 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="225" y="213.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{21}$</div></foreignObject>
  <foreignObject x="317" y="213.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{12}$</div></foreignObject>
  <foreignObject x="183.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_1$</div></foreignObject>
  <foreignObject x="383.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_2$</div></foreignObject>
  <line x1="200" y1="333" x2="200" y2="351" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="333" x2="400" y2="351" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="200" y1="342" x2="284" y2="342" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="316" y1="342" x2="400" y2="342" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="287" y="327.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
</svg>

### The square of the distance
The force depends strongly on the distance. When the distance doubles, the denominator $r^2$ becomes four times as large and the force drops to a quarter. At three times the distance the force is a ninth and at four times the distance a sixteenth. On the charges, in contrast, the force is directly proportional: when one charge doubles, the force doubles. In the graph each charge is $20\,\text{nC}$. At a distance of $3\,\text{cm}$ the force is $4.0\,\text{mN}$ and at a distance of $6\,\text{cm}$ only $1.0\,\text{mN}$.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: the force F between two point charges, q1 = q2 = 20 nC, in millinewtons as a function of the distance r in centimetres. The curve falls steeply. At a distance of 3 cm the force is 4.0 mN, at twice the distance, 6 cm, a quarter, that is 1.0 mN, at three times, 9 cm, a ninth, that is 0.44 mN, and at four times, 12 cm, a sixteenth, that is 0.25 mN. F, F/4, F/9 and F/16 are marked next to the points." style="max-width:100%;font-size:24px">
  <line x1="166.5" y1="310" x2="166.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="249.5" y1="310" x2="249.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332" y1="310" x2="332" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="415" y1="310" x2="415" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="257" x2="470" y2="257" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="204" x2="470" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="151.5" x2="470" y2="151.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="98.5" x2="470" y2="98.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="310" x2="484" y2="310" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,310 L483,316 L483,304 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="311" x2="84" y2="58" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,46 L90,59 L78,59 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="166.5" y1="310" x2="166.5" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="156.5" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="249.5" y1="310" x2="249.5" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="239.5" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="332" y1="310" x2="332" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="322" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$9$</div></foreignObject>
  <line x1="415" y1="310" x2="415" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="398.5" y="319.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="77" y1="257" x2="84" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="242.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="77" y1="204" x2="84" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="189.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="77" y1="151.5" x2="84" y2="151.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="137" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="77" y1="98.5" x2="84" y2="98.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="84" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="54" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="295.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{cm})$</div></foreignObject>
  <foreignObject x="74" y="15.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{mN})$</div></foreignObject>
  <polyline points="164,84 166.5,97 169,109.5 171.5,120.5 174,130.5 176,140 178.5,149 181,157 183.5,164.5 186,171.5 188.5,177.5 191,183.5 193.5,189.5 196,194.5 198.5,199.5 201,204 203.5,208.5 206,212.5 208,216.5 210.5,220 213,223.5 215.5,226.5 218,229.5 220.5,232.5 223,235 225.5,237.5 228,240 230.5,242.5 233,244.5 235.5,247 237.5,249 240,250.5 242.5,252.5 245,254.5 247.5,256 250,257.5 252.5,259 255,260.5 257.5,262 260,263 262.5,264.5 265,266 267,267 269.5,268 272,269 274.5,270 277,271 279.5,272 282,273 284.5,274 287,275 289.5,275.5 292,276.5 294.5,277.5 296.5,278 299,279 301.5,279.5 304,280 306.5,281 309,281.5 311.5,282 314,282.5 316.5,283 319,284 321.5,284.5 324,285 326,285.5 328.5,286 331,286.5 333.5,287 336,287 338.5,287.5 341,288 343.5,288.5 346,289 348.5,289.5 351,289.5 353.5,290 355.5,290.5 358,291 360.5,291 363,291.5 365.5,292 368,292 370.5,292.5 373,292.5 375.5,293 378,293.5 380.5,293.5 383,294 385,294 387.5,294.5 390,294.5 392.5,295 395,295 397.5,295.5 400,295.5 402.5,295.5 405,296 407.5,296 410,296.5 412.5,296.5 414.5,297 417,297 419.5,297 422,297.5 424.5,297.5 427,297.5 429.5,298 432,298 434.5,298 437,298.5 439.5,298.5 442,298.5 444,299 446.5,299 449,299 451.5,299.5 454,299.5 456.5,299.5 459,299.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="166.5" cy="98.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="180.5" y="54" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <circle cx="249.5" cy="257" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="263.5" y="212.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{F}{4}$</div></foreignObject>
  <circle cx="332" cy="286.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="346" y="242" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{F}{9}$</div></foreignObject>
  <circle cx="415" cy="297" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="429" y="252.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{F}{16}$</div></foreignObject>
  <foreignObject x="230.5" y="88" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$4.0\,\text{mN}$</div></foreignObject>
  <line x1="166.5" y1="98.5" x2="166.5" y2="310" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="84" y1="98.5" x2="166.5" y2="98.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
</svg>

### The forces of several charges
When several other charges act on a charge, the force of each charge is calculated separately with Coulomb's law, as if the others were not there. The net force on the charge is the vector sum of these forces:
```latex
\overline{F} = \overline{F}_1 + \overline{F}_2
```
where $\overline{F}$ is the net force ($\text{N}$) and $\overline{F}_1$ and $\overline{F}_2$ are the forces that two other charges exert on it ($\text{N}$). When all the charges are on the same line, forces in the same direction are added and forces in opposite directions are subtracted from each other.

## Worked example
Two small metal spheres are on insulating rods so that the distance between the centres of the spheres is $6.0\,\text{cm}$. The charge of one sphere is $+12\,\text{nC}$ and that of the other $-8.0\,\text{nC}$. How large is the electric force between the spheres, and do the spheres attract or repel each other?

<!-- vaihe -->

**Given and find.** $q_1 = +12\,\text{nC}$, $q_2 = -8.0\,\text{nC}$ and $r = 6.0\,\text{cm}$. We are asked for the magnitude of the force $F$ and whether the spheres attract or repel each other.

<!-- vaihe -->

**Principle.** The spheres are small compared with their distance, so they can be treated as point charges, and Coulomb's law gives the magnitude of the force. The direction of the force is worked out from the signs: charges of opposite signs attract each other. An equal force acts on each sphere.

<!-- vaihe -->

**Formula solved.**
```latex
F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2}
```

<!-- vaihe -->

**Conversions.** $q_1 = 12\,\text{nC} = 12 \cdot 10^{-9}\,\text{C}$, $\lvert q_2 \rvert = 8.0\,\text{nC} = 8.0 \cdot 10^{-9}\,\text{C}$ and $r = 6.0\,\text{cm} = 6.0 \cdot 0.01\,\text{m} = 0.060\,\text{m}$. The absolute value of the product of the charges is $\lvert q_1 q_2 \rvert = 12 \cdot 10^{-9}\,\text{C} \cdot 8.0 \cdot 10^{-9}\,\text{C} = 9.6 \cdot 10^{-17}\,\text{C}^2$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2} \\
&= 8.988 \cdot 10^{9}\,\tfrac{\text{N} \cdot \text{m}^2}{\text{C}^2} \\
&\quad \cdot \frac{9.6 \cdot 10^{-17}\,\text{C}^2}{(0.060\,\text{m})^2} \\
&= 2.397 \cdot 10^{-4}\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The force is $2.4 \cdot 10^{-4}\,\text{N} = 0.24\,\text{mN}$, two significant figures like the charge $8.0\,\text{nC}$ and the distance $6.0\,\text{cm}$. The spheres attract each other, because their charges have opposite signs.

<!-- vaihe -->

**Reasonableness.** With rounded numbers $10^{10} \cdot 10^{-16} : 0.004 \approx 2.5 \cdot 10^{-4}$, so the order of magnitude is right. The force is equal to the weight of a mass of about $24\,\text{mg}$, so it is small, but it is enough to move light objects. At half the distance the force would be four times as large, $0.96\,\text{mN}$.

## Common misconception
Many people think that a larger charge acts on a smaller one with a greater force than the smaller acts on the larger. The forces between the charges are, however, a force and its reaction force: they are always equal in magnitude and opposite in direction. Coulomb's law contains the product of the charges, so doubling both charges quadruples the same force that acts on both.

Another mistake is to think that no electric force acts on a neutral object. A charged object attracts a neutral object, because induction or polarisation brings the charge of opposite sign nearer than the charge of the same sign. A third mistake is to believe that rubbing creates charge. Rubbing only moves electrons from one object to another, and the total charge is conserved.

## Summary
- Charge is a multiple of the elementary charge, $Q = ne$, $e = 1.602 \cdot 10^{-19}\,\text{C}$. Charges of the same sign repel and charges of opposite signs attract each other.
- Charge is conserved: in rubbing and contact, electrons only move from one object to another. Two identical metal spheres share their common charge equally in contact.
- In induction a charged object moves the charges of a conductor, and in an insulator it polarises the molecules, so a charged object attracts a neutral object.
- Electric current is moving charge, $I = Q : t$.
- The field lines of a point charge are radial: outwards from a positive charge and inwards into a negative one, and the field weakens as the distance grows.
- Coulomb's law $F = k\,\tfrac{\lvert q_1 q_2 \rvert}{r^2}$: double the distance gives a quarter of the force. A force and its reaction force are equal, and the forces of several charges are added as vectors.
