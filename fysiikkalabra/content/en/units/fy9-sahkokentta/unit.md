# Electric field and the capacitor

> **Why** does the spark that jumps from a door handle on a frosty day do no harm, although its voltage is thousands of volts?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter evening in a hallway. In the middle there is a wooden front door with a brass handle on a long metal plate. From the right a hand in a red knitted sleeve reaches towards the handle, and a small bright spark flashes between the fingertip and the metal plate. On the floor there is a striped woollen rug. On the left there is a window showing a snowy night, the moon and spruces, and a radiator under the window. A woolly hat hangs on the coat rack on the wall." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9sk-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4e7cf"/><stop offset="1" stop-color="#ead6b2"/></linearGradient><linearGradient id="fy9sk-floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c99a68"/><stop offset="1" stop-color="#a9784a"/></linearGradient><linearGradient id="fy9sk-night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d3557"/><stop offset="1" stop-color="#4f6d93"/></linearGradient><linearGradient id="fy9sk-door" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9a6440"/><stop offset="1" stop-color="#7a4a2c"/></linearGradient><linearGradient id="fy9sk-brass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f1d58f"/><stop offset="1" stop-color="#c9a046"/></linearGradient><linearGradient id="fy9sk-lever" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4dc9c"/><stop offset="1" stop-color="#c9a046"/></linearGradient><linearGradient id="fy9sk-sleeve" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d64545"/><stop offset="1" stop-color="#a61e1e"/></linearGradient><radialGradient id="fy9sk-glow"><stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/><stop offset="0.35" stop-color="#d0e6fb" stop-opacity="0.75"/><stop offset="1" stop-color="#d0e6fb" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy9sk-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy9sk-floor)"/>
  <line x1="0" y1="504" x2="1200" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="538" x2="1200" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="572" x2="1200" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="470" x2="60" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="504" x2="250" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="538" x2="360" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="550" y1="470" x2="550" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="504" x2="660" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="850" y1="538" x2="850" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="960" y1="470" x2="960" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1150" y1="504" x2="1150" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1260" y1="538" x2="1260" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="0" y="462" width="1200" height="10" fill="#e7d3ae" stroke="#1f2933" stroke-width="2"/>
  <rect x="70" y="80" width="260" height="250" rx="4" fill="url(#fy9sk-night)" stroke="#1f2933" stroke-width="4"/>
  <circle cx="270" cy="132" r="22" fill="#fff4d6"/>
  <circle cx="280" cy="126" r="20" fill="#3b5a82"/>
  <circle cx="95" cy="134" r="3.16043" fill="#ffffff"/>
  <circle cx="118.5" cy="126" r="2.99475" fill="#ffffff"/>
  <circle cx="108.5" cy="93" r="2.44434" fill="#ffffff"/>
  <circle cx="273" cy="123.5" r="3.07418" fill="#ffffff"/>
  <circle cx="129" cy="209.5" r="2.44092" fill="#ffffff"/>
  <circle cx="126.5" cy="241" r="2.11153" fill="#ffffff"/>
  <circle cx="242.5" cy="209.5" r="2.6959" fill="#ffffff"/>
  <circle cx="302" cy="260" r="2.46306" fill="#ffffff"/>
  <circle cx="240.5" cy="253.5" r="2.34635" fill="#ffffff"/>
  <circle cx="312" cy="173" r="1.66264" fill="#ffffff"/>
  <circle cx="287.5" cy="198.5" r="3.04026" fill="#ffffff"/>
  <circle cx="206.5" cy="243.5" r="3.10226" fill="#ffffff"/>
  <circle cx="299.5" cy="93" r="2.58907" fill="#ffffff"/>
  <circle cx="206" cy="120" r="2.8447" fill="#ffffff"/>
  <circle cx="157.5" cy="157" r="2.59527" fill="#ffffff"/>
  <circle cx="243.5" cy="181" r="2.83611" fill="#ffffff"/>
  <circle cx="209.5" cy="130" r="2.91189" fill="#ffffff"/>
  <circle cx="192" cy="249.5" r="2.10826" fill="#ffffff"/>
  <circle cx="91" cy="230" r="1.8787" fill="#ffffff"/>
  <circle cx="294.5" cy="257.5" r="3.10957" fill="#ffffff"/>
  <circle cx="303.5" cy="234.5" r="3.18535" fill="#ffffff"/>
  <circle cx="228" cy="130" r="2.64288" fill="#ffffff"/>
  <circle cx="265.5" cy="132.5" r="3.092" fill="#ffffff"/>
  <circle cx="229" cy="196.5" r="2.53966" fill="#ffffff"/>
  <circle cx="264.5" cy="132.5" r="2.67846" fill="#ffffff"/>
  <circle cx="275.5" cy="253" r="2.62559" fill="#ffffff"/>
  <path d="M83,300 L110,210 L137,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M126,300 L162,180 L198,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M196,300 L220,220 L244,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M251,300 L284,190 L317,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M70,290 Q160,266 230,284 T330,280 V330 H70 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="200" y1="80" x2="200" y2="330" stroke="#f4efe6" stroke-width="6" stroke-linecap="butt"/>
  <line x1="70" y1="185" x2="330" y2="185" stroke="#f4efe6" stroke-width="6" stroke-linecap="butt"/>
  <rect x="70" y="80" width="260" height="250" rx="4" fill="none" stroke="#1f2933" stroke-width="4"/>
  <rect x="54" y="330" width="292" height="16" rx="3" fill="#f4efe6" stroke="#1f2933" stroke-width="3"/>
  <rect x="96" y="368" width="208" height="82" rx="6" fill="#f8f9fa" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="117" y1="376" x2="117" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="137.5" y1="376" x2="137.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="158.5" y1="376" x2="158.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="179" y1="376" x2="179" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="200" y1="376" x2="200" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="221" y1="376" x2="221" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="241.5" y1="376" x2="241.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="262.5" y1="376" x2="262.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283" y1="376" x2="283" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="126" y1="450" x2="126" y2="462" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="274" y1="450" x2="274" y2="462" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <rect x="392" y="112" width="120" height="12" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <line x1="452" y1="124" x2="452" y2="150" stroke="#6c757d" stroke-width="4" stroke-linecap="round"/>
  <path d="M404,214 Q404,146 452,142 Q500,146 500,214 Z" fill="#2f74b5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="412" y1="164" x2="412" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="432" y1="164" x2="432" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="452" y1="164" x2="452" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="472" y1="164" x2="472" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="492" y1="164" x2="492" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <rect x="398" y="206" width="108" height="20" rx="6" fill="#a9d1f0" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="452" cy="136" r="12" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="546" y="38" width="298" height="424" fill="#e2cfa8" stroke="#1f2933" stroke-width="3"/>
  <rect x="560" y="52" width="270" height="410" fill="url(#fy9sk-door)" stroke="#1f2933" stroke-width="3"/>
  <rect x="590" y="82" width="210" height="150" rx="4" fill="none" stroke="#5e3720" stroke-width="3"/>
  <rect x="596" y="88" width="198" height="138" rx="3" fill="none" stroke="#b07b52" stroke-width="2"/>
  <rect x="590" y="266" width="210" height="166" rx="4" fill="none" stroke="#5e3720" stroke-width="3"/>
  <rect x="596" y="272" width="198" height="154" rx="3" fill="none" stroke="#b07b52" stroke-width="2"/>
  <rect x="554" y="92" width="10" height="40" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="554" y="392" width="10" height="40" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="771" y="232" width="26" height="150" rx="6" fill="url(#fy9sk-brass)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="784" cy="272" r="11" fill="#e8c66e" stroke="#1f2933" stroke-width="2"/>
  <path d="M784,265 L702,267 Q688,272 700,279 L784,279 Z" fill="url(#fy9sk-lever)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="784" cy="344" r="5.5" fill="#1f2933"/>
  <path d="M781,346 L779,360 L789,360 L787,346 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M1200,244 L1010,256 Q984,276 990,312 Q996,350 1016,360 L1200,376 Z" fill="url(#fy9sk-sleeve)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1040,262 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1040,352 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1068,261 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1068,353 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1096,260 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1096,354 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1124,259 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1124,355 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1152,258 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1152,356 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1180,257 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1180,357 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1004,264 Q996,300 1010,352" fill="none" stroke="#f6d2c4" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M996,272 Q960,266 930,284 L825,297 Q817,303 825,310 L928,312 Q920,330 936,338 Q964,352 998,344 Z" fill="#f1c9a5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M944,318 Q930,322 944,326" fill="none" stroke="#d9a47c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M948,327 Q933,331 948,335" fill="none" stroke="#d9a47c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M952,336 Q936,340 952,344" fill="none" stroke="#d9a47c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M829,300 q4,3 0,7" fill="none" stroke="#d9a47c" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="808" cy="304" r="36" fill="url(#fy9sk-glow)"/>
  <path d="M819,304 L812,297 L808,309 L803,300 L797,306" fill="none" stroke="#1971c2" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M819,304 L812,297 L808,309 L803,300 L797,306" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="825" y1="290" x2="832.5" y2="283.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="830" y1="304" x2="840" y2="304" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="825" y1="318" x2="832.5" y2="324.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="791" y1="318" x2="783.5" y2="324.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="786" y1="304" x2="776" y2="304" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="791" y1="290" x2="783.5" y2="283.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M620,488 L1010,488 L1080,560 L560,560 Z" fill="#c9d6c0" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M613.5,496 L1018,496 L1024.5,502.5 L608,502.5 Z" fill="#7a9e7e" stroke-linejoin="round"/>
  <path d="M602,509.5 L1030.5,509.5 L1037,516 L596.5,516 Z" fill="#e9c98a" stroke-linejoin="round"/>
  <path d="M591,522.5 L1043.5,522.5 L1050,529.5 L585.5,529.5 Z" fill="#7a9e7e" stroke-linejoin="round"/>
  <path d="M580,536 L1056.5,536 L1063,542.5 L574.5,542.5 Z" fill="#c95f4a" stroke-linejoin="round"/>
  <path d="M569,549.5 L1069.5,549.5 L1076,556 L563.5,556 Z" fill="#7a9e7e" stroke-linejoin="round"/>
  <path d="M620,488 L1010,488 L1080,560 L560,560 Z" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="566" y1="560" x2="564" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="592" y1="560" x2="590" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="618" y1="560" x2="616" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="644" y1="560" x2="642" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="670" y1="560" x2="668" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="696" y1="560" x2="694" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="722" y1="560" x2="720" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="748" y1="560" x2="746" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="774" y1="560" x2="772" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="800" y1="560" x2="798" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="826" y1="560" x2="824" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="852" y1="560" x2="850" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="878" y1="560" x2="876" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="904" y1="560" x2="902" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="930" y1="560" x2="928" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="956" y1="560" x2="954" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="982" y1="560" x2="980" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="1008" y1="560" x2="1006" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="1034" y1="560" x2="1032" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="1060" y1="560" x2="1058" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
</svg>

## Key idea

The tasks of the lesson start from the same idea: **a charge creates an electric field around itself, and the field exerts a force on another charge**, $\overline{F} = q\overline{E}$. On a positive charge the force points in the direction of the field and on a negative charge against the field. When the field moves a charge, it does work, and the potential energy of the charge changes like the gravitational potential energy of a ball in the gravitational field. A capacitor stores energy in the field between its plates. Semiconductor components and electrical safety return to the same quantities: voltage, current and the field a dielectric can withstand.

<svg data-fig="kartta" viewBox="0 0 380 780" role="img" aria-label="Concept map. At the top is the node: a charge creates an electric field, and the field exerts a force on a charge, F = q E. Four branches go down from it. Charge and force: charge Q = n e, Coulomb&#x27;s law F = k times the absolute value of the product of the charges divided by r squared, and the vector sum of the forces. Field and potential: uniform field E = U divided by d, work done by the field W = q U and acceleration one half m v squared = charge times U. Capacitor: capacitance C = Q divided by U, parallel-plate capacitor C = epsilon zero epsilon r A divided by d and energy W = one half C U squared. Components and safety: series resistor R = U minus U D divided by I, efficiency of a solar cell eta = P divided by G A, and current through the body I = U divided by R." style="max-width:100%;font-size:22px">
  <line x1="24" y1="80" x2="24" y2="638" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/>
  <foreignObject x="71.5" y="17" width="237" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\text{a charge creates a field}$</div></foreignObject>
  <foreignObject x="151.5" y="46" width="77" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\overline{F} = q\overline{E}$</div></foreignObject>
  <line x1="24" y1="122" x2="44" y2="122" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="100" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="109" width="180" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{charge and force}$</div></foreignObject>
  <line x1="54" y1="142" x2="362" y2="142" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="153" width="54" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$Q = ne$</div></foreignObject>
  <foreignObject x="213" y="156" width="149" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{elementary charge}$</div></foreignObject>
  <foreignObject x="58" y="190" width="157" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$F = k\,|q_1 q_2|/r^2$</div></foreignObject>
  <foreignObject x="292" y="193" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{Coulomb}$</div></foreignObject>
  <foreignObject x="58" y="227" width="122" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\overline{F} = \overline{F}_1 + \overline{F}_2$</div></foreignObject>
  <foreignObject x="327" y="230" width="35" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{sum}$</div></foreignObject>
  <line x1="24" y1="294" x2="44" y2="294" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="272" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="281" width="214" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{field and potential}$</div></foreignObject>
  <line x1="54" y1="314" x2="362" y2="314" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="325" width="65" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$E = U/d$</div></foreignObject>
  <foreignObject x="292" y="328" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{uniform}$</div></foreignObject>
  <foreignObject x="58" y="362" width="54" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$W = qU$</div></foreignObject>
  <foreignObject x="230" y="365" width="132" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{work of the field}$</div></foreignObject>
  <foreignObject x="58" y="399" width="134" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\tfrac12 mv^2 = |q|U$</div></foreignObject>
  <foreignObject x="248" y="402" width="114" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{acceleration}$</div></foreignObject>
  <line x1="24" y1="466" x2="44" y2="466" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="444" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="453" width="122" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{capacitor}$</div></foreignObject>
  <line x1="54" y1="486" x2="362" y2="486" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="497" width="65" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$C = Q/U$</div></foreignObject>
  <foreignObject x="257" y="500" width="105" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{capacitance}$</div></foreignObject>
  <foreignObject x="58" y="534" width="111" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$C = \varepsilon_0\varepsilon_\text{r}A/d$</div></foreignObject>
  <foreignObject x="301" y="537" width="61" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{plates}$</div></foreignObject>
  <foreignObject x="58" y="571" width="100" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$W = \tfrac12 CU^2$</div></foreignObject>
  <foreignObject x="301" y="574" width="61" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{energy}$</div></foreignObject>
  <line x1="24" y1="638" x2="44" y2="638" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="616" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="625" width="237" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{components and safety}$</div></foreignObject>
  <line x1="54" y1="658" x2="362" y2="658" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="669" width="122" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$R = (U - U_\text{D})/I$</div></foreignObject>
  <foreignObject x="230" y="672" width="132" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{series resistor}$</div></foreignObject>
  <foreignObject x="58" y="706" width="100" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\eta = P/(GA)$</div></foreignObject>
  <foreignObject x="319" y="709" width="43" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{cell}$</div></foreignObject>
  <foreignObject x="58" y="743" width="65" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$I = U/R$</div></foreignObject>
  <foreignObject x="257" y="746" width="105" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{body current}$</div></foreignObject>
</svg>

The spark of the opening is solved with these laws. When you walk on a woollen rug, charge builds up on your body, and because of induction a charge of opposite sign moves to the nearby surface of the metal plate of the handle. The spark jumps when the field in the air gap exceeds the dielectric strength of air, about $3\,\text{MV/m}$. A spark of about $3\,\text{mm}$ therefore tells of a voltage of about $9\,\text{kV}$.

The voltage is large, but the body is a small capacitor with a capacitance of about $100\,\text{pF}$, so the charge is only about $0.9\,\mu\text{C}$ and the energy about $4\,\text{mJ}$. The discharge lasts about a microsecond. A dangerous current, about $50\,\text{mA}$ for one second, would carry $0.05\,\text{C}$ through the body, over $50\,000$ times more charge.

<svg data-fig="kipina" viewBox="0 0 600 540" role="img" aria-label="Schematic, not to scale. On the left a fingertip with negative charges on its surface. On the right the metal plate of the door handle, where positive charges have moved to the surface facing the finger because of induction. Between them there is an air gap of about 3 millimetres, crossed by green field lines from the plate to the finger and a bright bluish-white spark; the field is about 3 MV/m, the dielectric strength of air. Below, the calculation: the voltage U = E max times d is about 9 kV, the body is a capacitor with a capacitance of about 100 pF, so the charge Q = C U is about 0.9 microcoulombs and the energy W = one half C U squared about 4 millijoules." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9sk-plate" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e8c66e"/><stop offset="1" stop-color="#c9a046"/></linearGradient><radialGradient id="fy9sk-kglow"><stop offset="0" stop-color="#ffffff" stop-opacity="0.9"/><stop offset="0.5" stop-color="#d0e6fb" stop-opacity="0.6"/><stop offset="1" stop-color="#d0e6fb" stop-opacity="0"/></radialGradient></defs>
  <path d="M10,70 L190,70 Q262,70 262,140 Q262,210 190,210 L10,210 Z" fill="#f1c9a5" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M150,100 Q200,94 222,118" fill="none" stroke="#d9a47c" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="420" y="40" width="170" height="200" rx="6" fill="url(#fy9sk-plate)" stroke="#1f2933" stroke-width="3"/>
  <circle cx="214" cy="92.5" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="208" y1="92.5" x2="220" y2="92.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="230" cy="114" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="224" y1="114" x2="236" y2="114" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="236" cy="140" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="230" y1="140" x2="242" y2="140" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="230" cy="166" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="224" y1="166" x2="236" y2="166" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="214" cy="187.5" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="208" y1="187.5" x2="220" y2="187.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="68" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="68" x2="446" y2="68" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="62" x2="440" y2="74" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="104" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="104" x2="446" y2="104" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="98" x2="440" y2="110" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="140" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="140" x2="446" y2="140" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="134" x2="440" y2="146" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="176" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="176" x2="446" y2="176" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="170" x2="440" y2="182" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="212" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="212" x2="446" y2="212" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="206" x2="440" y2="218" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="418" y1="80" x2="284" y2="80" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M272,80 L285,74 L285,86 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="110" x2="280" y2="110" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M268,110 L281,104 L281,116 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="140" x2="280" y2="140" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M268,140 L281,134 L281,146 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="170" x2="280" y2="170" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M268,170 L281,164 L281,176 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="200" x2="284" y2="200" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M272,200 L285,194 L285,206 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="322" y="29" width="40" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <path d="M251,155 Q341,139 431,155 Q341,171 251,155 Z" fill="url(#fy9sk-kglow)" stroke-linejoin="round"/>
  <path d="M264,155 L292,149 L312,161 L338,149 L362,161 L388,150 L416,155" fill="none" stroke="#1971c2" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M264,155 L292,149 L312,161 L338,149 L362,161 L388,150 L416,155" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="262" y1="250" x2="420" y2="250" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="262" y1="238" x2="262" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="238" x2="420" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="261" width="160" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$d \approx 3\,\text{mm}$</div></foreignObject>
  <foreignObject x="62.5" y="223" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{finger}$</div></foreignObject>
  <foreignObject x="457.5" y="253" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{handle}$</div></foreignObject>
  <line x1="10" y1="302" x2="590" y2="302" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="14" y="319.5" width="432" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$U = E_\text{max}d \approx 3\,\text{MV/m} \cdot 3\,\text{mm} \approx 9\,\text{kV}$</div></foreignObject>
  <foreignObject x="14" y="381.5" width="397" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$Q = CU \approx 100\,\text{pF} \cdot 9\,\text{kV} \approx 0.9\,\mu\text{C}$</div></foreignObject>
  <foreignObject x="14" y="443" width="238" height="82" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$W = \dfrac12 CU^2 \approx 4\,\text{mJ}$</div></foreignObject>
</svg>

## Formula: Electric field and the capacitor

### Charge, force and field

```latex
\begin{aligned}
Q &= ne \\
F &= k\,\frac{\lvert q_1 q_2 \rvert}{r^2} \\
\overline{F} &= q\overline{E} \\
E &= \frac{U}{d}
\end{aligned}
```

where $n$ is the number of elementary charges, $e = 1.602 \cdot 10^{-19}\,\text{C}$ the elementary charge, $F$ the force ($\text{N}$), $q_1$ and $q_2$ the charges ($\text{C}$), $r$ their distance ($\text{m}$), $k = 8.988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2}$, $\overline{E}$ the electric field strength ($\text{N/C} = \text{V/m}$), $U$ the voltage between the plates ($\text{V}$) and $d$ the distance between the plates ($\text{m}$). Charge is conserved. Coulomb's law holds for point charges and uniformly charged spheres, and the forces of several charges are added as vectors. The field $E = \tfrac{U}{d}$ holds only between large parallel plates, where the field is uniform.

<svg data-fig="levyt" viewBox="0 0 600 440" role="img" aria-label="Schematic: two horizontal plates. The upper plate is positive and its potential is 200 V; the lower, negative plate is the zero, 0 V. Between the plates there are five green vertical field lines pointing down: the field is uniform. Grey dashed lines are the equipotential surfaces 150 V, 100 V and 50 V. On the left a proton, whose red force arrow points down in the direction of the field. On the right an electron, whose red force arrow points up against the field, towards the higher potential." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9sk-pl1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dfe4ea"/><stop offset="1" stop-color="#aeb8c2"/></linearGradient><linearGradient id="fy9sk-pl2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dfe4ea"/><stop offset="1" stop-color="#aeb8c2"/></linearGradient></defs>
  <rect x="120" y="52" width="440" height="18" rx="3" fill="url(#fy9sk-pl1)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="120" y="350" width="440" height="18" rx="3" fill="url(#fy9sk-pl2)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="154" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="61" x2="158" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="154" y1="57" x2="154" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="154" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="359" x2="158" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="216" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="212" y1="61" x2="220" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="216" y1="57" x2="216" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="216" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="212" y1="359" x2="220" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="278" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="274" y1="61" x2="282" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="278" y1="57" x2="278" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="278" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="274" y1="359" x2="282" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="340" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="336" y1="61" x2="344" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="340" y1="57" x2="340" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="340" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="336" y1="359" x2="344" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="402" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="398" y1="61" x2="406" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="402" y1="57" x2="402" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="402" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="398" y1="359" x2="406" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="464" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="460" y1="61" x2="468" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="464" y1="57" x2="464" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="464" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="460" y1="359" x2="468" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="526" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="522" y1="61" x2="530" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="526" y1="57" x2="526" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="526" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="522" y1="359" x2="530" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="140" x2="560" y2="140" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="34" y="124.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$150\,\text{V}$</div></foreignObject>
  <line x1="120" y1="210" x2="560" y2="210" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="34" y="194.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$100\,\text{V}$</div></foreignObject>
  <line x1="120" y1="280" x2="560" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="48" y="264.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$50\,\text{V}$</div></foreignObject>
  <foreignObject x="34" y="45.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$200\,\text{V}$</div></foreignObject>
  <foreignObject x="61" y="343.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0\,\text{V}$</div></foreignObject>
  <line x1="170" y1="76" x2="170" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M170,344 L164.5,332 L175.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="255" y1="76" x2="255" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M255,344 L249.5,332 L260.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="340" y1="76" x2="340" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M340,344 L334.5,332 L345.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="425" y1="76" x2="425" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M425,344 L419.5,332 L430.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="510" y1="76" x2="510" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M510,344 L504.5,332 L515.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="524" y="285.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <circle cx="212" cy="220" r="15" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="204.5" y1="220" x2="219.5" y2="220" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="212" y1="212.5" x2="212" y2="227.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="212" y1="237" x2="212" y2="297" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M212,312 L205,296 L219,296 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="230" y="245.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = e\overline{E}$</span></div></foreignObject>
  <circle cx="468" cy="200" r="15" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="460.5" y1="200" x2="475.5" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="468" y1="183" x2="468" y2="123" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M468,108 L475,124 L461,124 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="486" y="157.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = -e\overline{E}$</span></div></foreignObject>
  <foreignObject x="170.5" y="391.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{proton}$</div></foreignObject>
  <foreignObject x="414" y="391.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{electron}$</div></foreignObject>
</svg>

### Potential and energy

```latex
\begin{aligned}
E_\text{p} &= qV \\
W_{AB} &= qU_{AB} \\
\tfrac12 mv^2 &= \lvert q \rvert U
\end{aligned}
```

where $V$ is the potential at a point ($\text{V}$) relative to a chosen zero, $U_{AB} = V_A - V_B$ and $W_{AB}$ the work done by the field ($\text{J}$). The work does not depend on the path. The field points from higher potential to lower, and a charge starting from rest moves in the direction in which its potential energy decreases. The last equation holds for a particle starting from rest when only the electric force does work. The energy unit $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.

### The capacitor

```latex
\begin{aligned}
C &= \frac{Q}{U} \\
C &= \frac{\varepsilon_0\varepsilon_\text{r}A}{d} \\
W &= \tfrac12 QU = \tfrac12 CU^2 \\
U_\text{max} &= E_\text{max}d
\end{aligned}
```

where $C$ is the capacitance ($\text{F}$), $A$ the area of a plate ($\text{m}^2$), $\varepsilon_0 = 8.854 \cdot 10^{-12}\,\text{F/m}$, $\varepsilon_\text{r}$ the relative permittivity of the dielectric, $W$ the energy ($\text{J}$) and $E_\text{max}$ the dielectric strength of the dielectric ($\text{V/m}$). The formula of the parallel-plate capacitor holds when $d$ is small compared with the size of the plates and the dielectric fills the gap. For a capacitor connected to a source the voltage stays the same; for a disconnected one, the charge.

### Components and safety

```latex
\begin{aligned}
R &= \frac{U - U_\text{D}}{I} \\
\eta &= \frac{P}{GA} \\
I &= \frac{U}{R}
\end{aligned}
```

where $R$ is the series resistor of an LED ($\Omega$), $U_\text{D}$ the voltage of the LED ($\text{V}$), $P = UI$ the electric power of a solar cell at the maximum power point ($\text{W}$) and $G$ the light intensity ($\text{W/m}^2$). The last equation gives the current through the body when $U$ is the touch voltage and $R$ the resistance of the whole current path. A diode conducts only in the forward direction, when its voltage exceeds the threshold voltage. A fuse protects the cable, a residual current device the person.

## Common mistakes {Virheet}

- **The field and the force always in the same direction.** On a negative charge, such as an electron, the force points against the field.
- **Distance without the square.** In Coulomb's law twice the distance gives a quarter of the force.
- **The field increases when approaching a plate.** Between the plates the field is uniform: the force is the same everywhere.
- **Energy $QU$.** The capacitor stores $\tfrac12 QU$; the other half turns into internal energy of the conductors during charging.
- **A dielectric in a disconnected capacitor.** The charge stays the same, so the voltage and the energy decrease, not increase.
- **The series resistor without the voltage of the LED.** Across the resistor there is only $U - U_\text{D}$.
- **A high voltage is always dangerous.** The danger comes from a current through the body, driven by the voltage between two points.

## Review if needed {Kertaa}

- Charge and Coulomb's law: [*Electric charge and Coulomb's law*](fy6-10.html). The field and plates: [*Uniform electric field*](fy6-11.html).
- Potential, work and the electronvolt: [*Potential energy and potential in an electric field*](fy6-12.html). Capacitance and energy: [*The capacitor and its energy*](fy6-13.html).
- The diode, the LED and the solar cell: [*Semiconductors, the diode, the LED and the solar cell*](fy6-14.html).
- The fuse, earthing and the residual current device: [*Electrical safety at home and at work*](fy6-15.html). Charging and three-phase electricity: [*Applied chapter: the electric car and the home electrical system*](fy6-16.html).
