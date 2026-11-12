# Lasers and quantum structures

> **Why** does the light of a laser pointer cross a dark classroom as a narrow beam and show on the wall as a small dot, while the light of a torch spreads into a large, dim patch?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: in a dim classroom, a laser pointer and a torch on a desk point at the same white screen. A thin red beam leaves the laser pointer and hits the screen as a small bright dot. The light of the torch spreads into a wide cone and lights a large, dim, yellowish area of the screen." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy87h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b7480"/><stop offset="1" stop-color="#1f2933"/></linearGradient><linearGradient id="fy87h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy87h-cone" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078" stop-opacity="0.75"/><stop offset="1" stop-color="#ffc078" stop-opacity="0.12"/></linearGradient><radialGradient id="fy87h-patch" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078" stop-opacity="0.55"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient><radialGradient id="fy87h-dot" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff"/><stop offset="0.35" stop-color="#c92a2a"/><stop offset="1" stop-color="#c92a2a" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy87h-wall)"/>
  <rect x="0" y="450" width="1200" height="150" fill="url(#fy87h-desk)"/>
  <rect x="0" y="450" width="1200" height="10" fill="#f1dfb5"/>
  <rect x="930" y="70" width="200" height="340" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="1020" y="410" width="20" height="44" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="975" y="446" width="110" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M300,372 L930,180 L930,400 L300,412 Z" fill="url(#fy87h-cone)" stroke-linejoin="round"/>
  <ellipse cx="1030" cy="300" rx="96" ry="110" fill="url(#fy87h-patch)"/>
  <rect x="130" y="368" width="150" height="48" rx="10" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <path d="M280,360 L312,350 L312,430 L280,422 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="170" y="362" width="26" height="8" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="150" y="416" width="40" height="36" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="170" y="236" width="120" height="22" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="290" y="241" width="14" height="12" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="206" y="230" width="18" height="6" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="214" y="258" width="16" height="40" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="190" y="296" width="64" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="190" y="308" width="64" height="60" rx="3" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="304" y1="247" x2="1018" y2="196" stroke="#f2a69c" stroke-width="7" stroke-linecap="round"/>
  <line x1="304" y1="247" x2="1018" y2="196" stroke="#c92a2a" stroke-width="3" stroke-linecap="round"/>
  <circle cx="1018" cy="196" r="22" fill="url(#fy87h-dot)"/>
  <circle cx="1018" cy="196" r="5" fill="#ffffff"/>
  <path d="M520,520 L700,498 L730,560 L540,586 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="537" y1="540" x2="714.5" y2="516.5" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="544" y1="553" x2="720.5" y2="529" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="551" y1="566" x2="726.5" y2="541.5" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
</svg>

## Key idea

### Atom and photon: three events
In the chapter *Energy levels of the hydrogen atom and the Bohr model*, an atom absorbs a photon whose energy is the difference of two levels, or emits one when it drops to a lower level. An excited atom usually emits its photon by itself, at a random moment and in a random direction. This is **spontaneous emission**. The light of a lamp and of an LED is produced this way, so the photons of different atoms leave in different directions and out of step.

In 1917 Albert Einstein concluded that there is also a third event. When a photon whose energy is exactly the difference of the levels $E_2 - E_1$ hits an excited atom, it can make the atom drop to the lower level at once. This is **stimulated emission**. The incoming photon is not absorbed; a second photon is created beside it with the same energy, that is the same wavelength, the same direction of travel and the same phase. One photon becomes two identical ones, two become four, and so on. The laser is based on this amplification of light: the word comes from the English *light amplification by stimulated emission of radiation*.

<svg data-fig="processes" viewBox="0 0 600 380" role="img" aria-label="Three events side by side, schematic figure, not to scale. Each has two energy levels of an atom, the lower E1 and the upper E2, and the blue dot is an electron; the ring shows where it was before the event. On the left absorption: a photon whose energy hf is the difference of the levels enters the atom and lifts the electron to the level E2, and the photon disappears. In the middle spontaneous emission: the electron drops by itself from the level E2 to the level E1, and a photon leaves in a random direction, here obliquely upwards. On the right stimulated emission: an incoming photon makes the electron of an excited atom drop, and two identical photons leave the atom in the same direction and in step." style="max-width:100%;font-size:24px">
  <foreignObject x="7" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_2$</div></foreignObject>
  <foreignObject x="7" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_1$</div></foreignObject>
  <line x1="60" y1="80" x2="216" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="60" y1="236" x2="216" y2="236" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="71.5" y="303.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{absorption}$</div></foreignObject>
  <line x1="229" y1="20" x2="229" y2="360" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="242" y1="80" x2="398" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="242" y1="236" x2="398" y2="236" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="247.5" y="287.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{spontaneous}$</div></foreignObject>
  <foreignObject x="266" y="321.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{emission}$</div></foreignObject>
  <line x1="411" y1="20" x2="411" y2="360" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="424" y1="80" x2="580" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="424" y1="236" x2="580" y2="236" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="435.5" y="287.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{stimulated}$</div></foreignObject>
  <foreignObject x="448" y="321.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{emission}$</div></foreignObject>
  <path d="M58,158 L58.5,158 L59,158.5 L59.5,159 L60,159.5 L61,160.5 L61.5,161 L62,162 L62.5,163 L63,164 L63.5,164.5 L64,165 L64.5,164.5 L65.5,164 L66,163.5 L66.5,163 L67,162 L67.5,161 L68,160 L68.5,159 L69,158 L69.5,157 L70.5,156 L71,155 L71.5,154 L72,153 L72.5,152.5 L73,152 L73.5,151.5 L74,151 L75,151 L75.5,151 L76,151.5 L76.5,152 L77,152.5 L77.5,153 L78,154 L78.5,155 L79,156 L80,157 L80.5,158 L81,159 L81.5,160 L82,161 L82.5,162 L83,163 L83.5,163.5 L84,164 L85,164.5 L85.5,165 L86,165 L86.5,165 L87,164.5 L87.5,164 L88,163.5 L88.5,163 L89.5,162 L90,161 L90.5,160 L91,159 L91.5,158 L92,157 L92.5,156 L93,155 L93.5,154 L94.5,153 L95,152.5 L95.5,152 L96,151.5 L96.5,151 L97,151 L97.5,151 L98,151.5 L99,152 L99.5,152.5 L100,153 L100.5,154 L101,155 L101.5,156 L102,157 L102.5,158 L103,159 L104,160 L104.5,161 L105,162 L105.5,163 L106,163.5 L106.5,164 L107,164.5 L107.5,165 L108,165 L109,165 L109.5,164.5 L110,164 L110.5,163.5 L111,163 L111.5,162 L112,161 L112.5,160 L113.5,159 L114,158 L114.5,157 L115,156 L115.5,155 L116,154 L116.5,153 L117,152.5 L117.5,152 L118.5,151.5 L119,151 L119.5,151.5 L120,152 L120.5,153 L121,154 L121.5,155 L122,155.5 L123,156.5 L123.5,157 L124,157.5 L124.5,158 L125,158" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M140,158 L125,165.5 L125,150.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="77.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <circle cx="176" cy="236" r="9" fill="#ffffff" stroke="#1971c2" stroke-width="2"/>
  <line x1="176" y1="224" x2="176" y2="105" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M176,93 L182,106 L170,106 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="176" cy="80" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="290" cy="80" r="9" fill="#ffffff" stroke="#1971c2" stroke-width="2"/>
  <line x1="290" y1="92" x2="290" y2="211" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M290,223 L284,210 L296,210 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="290" cy="236" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <path d="M310,196 L311,195.5 L312,195.5 L313,195.5 L314.5,195.5 L316,196 L318,196.5 L319.5,196.5 L320,196 L320.5,195 L320.5,194 L320.5,193 L320.5,191.5 L320,190 L320,188.5 L319.5,187 L319,185 L318.5,183.5 L318.5,182 L318.5,180.5 L318.5,179.5 L318.5,178.5 L319,177.5 L319.5,177 L320.5,176.5 L321.5,176.5 L322.5,176.5 L324,176.5 L325.5,177 L327,177 L329,177.5 L330.5,178 L332,178.5 L333.5,178.5 L335,179 L336,179 L337,178.5 L338,178.5 L338.5,177.5 L339,177 L339.5,176 L339.5,174.5 L339,173 L339,171.5 L338.5,170 L338,168.5 L338,167 L337.5,165 L337,163.5 L337,162.5 L337,161 L337.5,160 L338,159 L338.5,158.5 L339,158 L340.5,158 L341.5,158 L343,158 L344.5,158.5 L346,159 L347.5,159 L349.5,159.5 L351,160 L352.5,160.5 L354,160.5 L355,160.5 L356,160.5 L357,160 L357.5,159.5 L358,158.5 L358,157.5 L358,156 L358,155 L358,153.5 L357.5,151.5 L357,150 L356.5,148.5 L356.5,147 L356,145.5 L356,144 L356,142.5 L356,141.5 L356.5,141 L357,140 L358,140 L359,139.5 L360.5,139.5 L361.5,140 L363,140 L365,140.5 L366.5,141 L368,141.5 L369.5,141.5 L371,142 L372.5,142 L374,142 L375,142 L375.5,141.5 L376.5,141 L376.5,140 L377,139 L377,138 L377,136.5 L376.5,135 L376.5,133.5 L376,131.5 L375.5,130 L375,128.5 L375,127 L374.5,125.5 L375,124.5 L375,123 L375.5,122.5 L376,122 L377.5,122 L379,122.5 L380.5,123 L382,123 L383.5,123 L384.5,123 L385.5,122.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M396,112 L390.5,128 L380,117 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="353.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <path d="M420,161 L420.5,161 L421,161 L421,161.5 L421.5,161.5 L422,162 L422.5,162.5 L422.5,163 L423,163.5 L423.5,164.5 L424,165 L424.5,165.5 L424.5,166 L425,167 L425.5,167.5 L426,168 L426.5,168 L426.5,168 L427,167.5 L427.5,167.5 L428,167 L428,166.5 L428.5,166 L429,165.5 L429.5,165 L430,164.5 L430,164 L430.5,163 L431,162.5 L431.5,161.5 L432,161 L432,160.5 L432.5,159.5 L433,159 L433.5,158 L433.5,157.5 L434,157 L434.5,156.5 L435,156 L435.5,155.5 L435.5,155 L436,154.5 L436.5,154.5 L437,154 L437,154 L437.5,154 L438,154 L438.5,154 L439,154.5 L439,154.5 L439.5,155 L440,155.5 L440.5,156 L441,156.5 L441,157 L441.5,157.5 L442,158 L442.5,159 L442.5,159.5 L443,160.5 L443.5,161 L444,161.5 L444.5,162.5 L444.5,163 L445,164 L445.5,164.5 L446,165 L446,165.5 L446.5,166 L447,166.5 L447.5,167 L448,167.5 L448,167.5 L448.5,168 L449,168 L449.5,168 L450,168 L450,168 L450.5,167.5 L451,167.5 L451.5,167 L451.5,166.5 L452,166 L452.5,165.5 L453,165 L453.5,164.5 L453.5,164 L454,163 L454.5,162.5 L455,161.5 L455,161 L455.5,160.5 L456,159.5 L456.5,159 L457,158 L457,157.5 L457.5,157 L458,156.5 L458.5,156 L459,155.5 L459,155 L459.5,154.5 L460,154.5 L460.5,154 L460.5,154 L461,154 L461.5,154.5 L462,155 L462.5,156 L462.5,156.5 L463,157 L463.5,157.5 L464,158.5 L464.5,159 L464.5,159.5 L465,160 L465.5,160.5 L466,160.5 L466,161 L466.5,161 L467,161" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M482,161 L467,168.5 L467,153.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="431.5" y="111.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <circle cx="504" cy="80" r="9" fill="#ffffff" stroke="#1971c2" stroke-width="2"/>
  <line x1="504" y1="92" x2="504" y2="211" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M504,223 L498,210 L510,210 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="504" cy="236" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <path d="M520,143 L520.5,143 L521,143 L521,143.5 L521.5,144 L522,144 L522.5,144.5 L523,145 L523.5,146 L523.5,146.5 L524,147 L524.5,148 L525,148.5 L525.5,149 L525.5,149.5 L526,150 L526.5,150 L527,150 L527.5,149.5 L528,149.5 L528,149 L528.5,148.5 L529,148 L529.5,147.5 L530,147 L530,146.5 L530.5,146 L531,145 L531.5,144.5 L532,143.5 L532,143 L532.5,142.5 L533,141.5 L533.5,141 L534,140 L534.5,139.5 L534.5,139 L535,138.5 L535.5,138 L536,137.5 L536.5,137 L536.5,136.5 L537,136.5 L537.5,136 L538,136 L538.5,136 L539,136 L539,136 L539.5,136.5 L540,136.5 L540.5,137 L541,137.5 L541,138 L541.5,138.5 L542,139 L542.5,139.5 L543,140 L543.5,141 L543.5,141.5 L544,142.5 L544.5,143 L545,143.5 L545.5,144.5 L545.5,145 L546,146 L546.5,146.5 L547,147 L547.5,147.5 L548,148 L548,148.5 L548.5,149 L549,149.5 L549.5,149.5 L550,150 L550,150 L550.5,150 L551,150 L551.5,150 L552,149.5 L552.5,149.5 L552.5,149 L553,148.5 L553.5,148 L554,147.5 L554.5,147 L554.5,146.5 L555,146 L555.5,145 L556,144.5 L556.5,143.5 L557,143 L557,142.5 L557.5,141.5 L558,141 L558.5,140 L559,139.5 L559,139 L559.5,138.5 L560,138 L560.5,137.5 L561,137 L561,136.5 L561.5,136.5 L562,136 L562.5,136 L563,136 L563.5,136.5 L563.5,137 L564,137.5 L564.5,138 L565,139 L565.5,139.5 L565.5,140 L566,141 L566.5,141.5 L567,142 L567.5,142 L568,142.5 L568,143 L568.5,143 L569,143" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M584,143 L569,150.5 L569,135.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M520,181 L520.5,181 L521,181 L521,181.5 L521.5,182 L522,182 L522.5,182.5 L523,183 L523.5,184 L523.5,184.5 L524,185 L524.5,186 L525,186.5 L525.5,187 L525.5,187.5 L526,188 L526.5,188 L527,188 L527.5,187.5 L528,187.5 L528,187 L528.5,186.5 L529,186 L529.5,185.5 L530,185 L530,184.5 L530.5,184 L531,183 L531.5,182.5 L532,181.5 L532,181 L532.5,180.5 L533,179.5 L533.5,179 L534,178 L534.5,177.5 L534.5,177 L535,176.5 L535.5,176 L536,175.5 L536.5,175 L536.5,174.5 L537,174.5 L537.5,174 L538,174 L538.5,174 L539,174 L539,174 L539.5,174.5 L540,174.5 L540.5,175 L541,175.5 L541,176 L541.5,176.5 L542,177 L542.5,177.5 L543,178 L543.5,179 L543.5,179.5 L544,180.5 L544.5,181 L545,181.5 L545.5,182.5 L545.5,183 L546,184 L546.5,184.5 L547,185 L547.5,185.5 L548,186 L548,186.5 L548.5,187 L549,187.5 L549.5,187.5 L550,188 L550,188 L550.5,188 L551,188 L551.5,188 L552,187.5 L552.5,187.5 L552.5,187 L553,186.5 L553.5,186 L554,185.5 L554.5,185 L554.5,184.5 L555,184 L555.5,183 L556,182.5 L556.5,181.5 L557,181 L557,180.5 L557.5,179.5 L558,179 L558.5,178 L559,177.5 L559,177 L559.5,176.5 L560,176 L560.5,175.5 L561,175 L561,174.5 L561.5,174.5 L562,174 L562.5,174 L563,174 L563.5,174.5 L563.5,175 L564,175.5 L564.5,176 L565,177 L565.5,177.5 L565.5,178 L566,179 L566.5,179.5 L567,180 L567.5,180 L568,180.5 L568,181 L568.5,181 L569,181" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M584,181 L569,188.5 L569,173.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="535.5" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
</svg>

### Population inversion
A photon that makes an excited atom emit can be absorbed when it hits an atom in the ground state. Which happens more often depends on which level has more atoms. Normally almost all atoms are in the ground state, so a photon is much more likely to be absorbed than multiplied, and light becomes weaker in matter. Light is amplified only if the upper level has more atoms than the lower one, $N_2 > N_1$. This state is called **population inversion**. Heating does not produce it: even in warm matter the lower level always has more atoms than the upper one.

Inversion is made by **pumping**, that is by bringing energy to the atoms with light, an electric discharge or an electric current. In a simple model with two separate energy levels, inversion cannot be achieved by pumping with the same resonant light, because the photons of the pump light cause stimulated emission in atoms of the upper level just as likely as they excite atoms of the ground state: at most half of the atoms can be brought to the upper level. That is why many atomic and ion lasers use a structure of three or four energy levels. In semiconductor lasers, on the other hand, the amplification of light is based on the energy bands of the semiconductor and on an inversion produced by an electric current. In ruby, the green light of the pump lamp lifts atoms to a short-lived level $E_3$, from which they move quickly and without light to the level $E_2$. The level $E_2$ is long-lived: an atom stays in it for a few milliseconds on average, hundreds of thousands of times longer than in an ordinary excited state ($10^{-8}\,\text{s}$). So more atoms have time to collect on the level $E_2$ than are left in the ground state.

<svg data-fig="inversion" viewBox="0 0 600 360" role="img" aria-label="The energy levels of a three-level laser medium, such as ruby, schematic figure, not to scale. At the bottom is the ground state E1, at the top the short-lived level E3 and between them the long-lived level E2. Green arrow: pumping lifts atoms from the level E1 to the level E3. Grey dashed arrow: the atoms move from the level E3 quickly and without light to the level E2. Red arrow: the laser transition from the level E2 to the level E1, wavelength 694 nm. The blue dots are atoms: on the level E2 there are seven and on the level E1 four, so the upper level has more atoms than the lower. This is called population inversion." style="max-width:100%;font-size:24px">
  <line x1="120" y1="60" x2="310" y2="60" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="120" y1="150" x2="310" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="120" y1="300" x2="310" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="77" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_3$</div></foreignObject>
  <foreignObject x="77" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_2$</div></foreignObject>
  <foreignObject x="77" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_1$</div></foreignObject>
  <circle cx="136" cy="140" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="150" cy="140" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="164" cy="140" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="178" cy="140" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="192" cy="140" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="206" cy="140" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="220" cy="140" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="136" cy="290" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="150" cy="290" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="164" cy="290" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="178" cy="290" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="240" y1="297" x2="240" y2="76" stroke="#2b8a3e" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M240,62 L247,77 L233,77 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M262,64 L262,134" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="6 5"/>
  <path d="M262,148 L255,134 L269,134 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="286" y1="153" x2="286" y2="284" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M286,298 L279,283 L293,283 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="330" y="90.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{fast, no light}$</div></foreignObject>
  <foreignObject x="330" y="190.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{laser}\ 694\,\text{nm}$</div></foreignObject>
  <foreignObject x="330" y="247.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{pumping}$</div></foreignObject>
  <foreignObject x="181" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N_2 > N_1$</div></foreignObject>
</svg>

### Mirrors make light into a beam
The laser medium is between two mirrors. One mirror reflects all the light, the other for example $99\,\%$, and lets the rest through. A photon travelling along the axis between the mirrors passes through the medium hundreds of times and creates stimulated copies of itself on the way. Photons leaving sideways exit the medium and do not have time to multiply. So only light along the axis is amplified, and a beam comes out through the partly transmitting mirror. A laser starts to work only when the pumping is so strong that the amplification makes up for the light lost through the mirror and elsewhere. This limit of the pumping is called the **threshold**.

Laser light is nearly monochromatic because the photons are produced in the same transition. It is directional because only light along the axis is amplified, and the beam spreads only a little. It is also coherent: the waves are in step, because each stimulated photon copies the phase of the incoming photon. The light of a torch contains many wavelengths, and it leaves in different directions and out of step. A laser diode also has an amplifying medium and mirrors: an electric current produces the inversion in a semiconductor, and the cleaved ends of the crystal act as mirrors. Its energy levels, however, are energy bands and not the levels of a single atom.

<svg data-fig="cavity" viewBox="0 0 600 300" role="img" aria-label="The structure of a laser, schematic figure, not to scale. In the middle is a horizontal rod of active medium. At its left end is a mirror that reflects all the light, and at its right end a mirror that reflects 99 percent and lets 1 percent through. Under the rod is a pump lamp whose light lifts atoms to the excited state. Inside the rod red photons travel along the axis back and forth between the mirrors and multiply. Two photons leave obliquely sideways and exit the rod. A narrow red laser beam comes out through the right mirror." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy87c-rod" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="0.5" stop-color="#ffffff"/><stop offset="1" stop-color="#f2a69c"/></linearGradient><linearGradient id="fy87c-lamp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#b2f2bb"/></linearGradient></defs>
  <rect x="150" y="112" width="300" height="60" rx="8" fill="url(#fy87c-rod)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="108" y="98" width="14" height="88" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="474" y="98" width="10" height="88" rx="3" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="479" y1="102" x2="479" y2="182" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <path d="M170,132 L170.5,132 L171.5,132.5 L172,133 L173,134 L173.5,135 L174,136 L175,137 L175.5,138.5 L176.5,139 L177,139 L178,139 L178.5,138.5 L179,138 L180,137.5 L180.5,137 L181.5,136 L182,135 L183,134 L183.5,133 L184,132 L185,131 L185.5,130 L186.5,129 L187,128 L187.5,127 L188.5,126.5 L189,126 L190,125.5 L190.5,125 L191,125 L192,125 L192.5,125.5 L193.5,126 L194,126.5 L195,127 L195.5,128 L196,129 L197,130 L197.5,131 L198.5,132 L199,133 L200,134 L200.5,135 L201,136 L202,137 L202.5,137.5 L203.5,138 L204,138.5 L204.5,139 L205.5,139 L206,139 L207,138.5 L207.5,138 L208,137.5 L209,137 L209.5,136 L210.5,135 L211,134 L212,133 L212.5,132 L213,131 L214,130 L214.5,129 L215.5,128 L216,127 L217,126.5 L217.5,126 L218,125.5 L219,125 L219.5,125 L220.5,125 L221,125.5 L221.5,126 L222.5,126.5 L223,127 L224,128 L224.5,129 L225,130 L226,131 L226.5,132 L227.5,133 L228,134 L229,135 L229.5,136 L230,137 L231,137.5 L231.5,138 L232.5,138.5 L233,139 L234,139 L234.5,139 L235,138.5 L236,138 L236.5,137.5 L237.5,137 L238,136 L238.5,135 L239.5,134 L240,133 L241,132 L241.5,131 L242,130 L243,129 L243.5,128 L244.5,127 L245,126.5 L246,126 L246.5,125.5 L247,125 L248,125 L248.5,125 L249.5,125.5 L250,127 L251,128 L251.5,129 L252,130 L253,131 L253.5,131.5 L254.5,132 L255,132" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M270,132 L255,139.5 L255,124.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M300,132 L300.5,132 L301.5,132.5 L302,133 L303,134 L303.5,135 L304,136 L305,137 L305.5,138.5 L306.5,139 L307,139 L308,139 L308.5,138.5 L309,138 L310,137.5 L310.5,137 L311.5,136 L312,135 L313,134 L313.5,133 L314,132 L315,131 L315.5,130 L316.5,129 L317,128 L317.5,127 L318.5,126.5 L319,126 L320,125.5 L320.5,125 L321,125 L322,125 L322.5,125.5 L323.5,126 L324,126.5 L325,127 L325.5,128 L326,129 L327,130 L327.5,131 L328.5,132 L329,133 L330,134 L330.5,135 L331,136 L332,137 L332.5,137.5 L333.5,138 L334,138.5 L334.5,139 L335.5,139 L336,139 L337,138.5 L337.5,138 L338,137.5 L339,137 L339.5,136 L340.5,135 L341,134 L342,133 L342.5,132 L343,131 L344,130 L344.5,129 L345.5,128 L346,127 L347,126.5 L347.5,126 L348,125.5 L349,125 L349.5,125 L350.5,125 L351,125.5 L351.5,126 L352.5,126.5 L353,127 L354,128 L354.5,129 L355,130 L356,131 L356.5,132 L357.5,133 L358,134 L359,135 L359.5,136 L360,137 L361,137.5 L361.5,138 L362.5,138.5 L363,139 L364,139 L364.5,139 L365,138.5 L366,138 L366.5,137.5 L367.5,137 L368,136 L368.5,135 L369.5,134 L370,133 L371,132 L371.5,131 L372,130 L373,129 L373.5,128 L374.5,127 L375,126.5 L376,126 L376.5,125.5 L377,125 L378,125 L378.5,125 L379.5,125.5 L380,127 L381,128 L381.5,129 L382,130 L383,131 L383.5,131.5 L384.5,132 L385,132" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M400,132 L385,139.5 L385,124.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M430,154 L429.5,154 L428.5,153.5 L428,153 L427,152 L426.5,151 L426,150 L425,149 L424.5,147.5 L423.5,147 L423,147 L422,147 L421.5,147.5 L421,148 L420,148.5 L419.5,149 L418.5,150 L418,151 L417,152 L416.5,153 L416,154 L415,155 L414.5,156 L413.5,157 L413,158 L412.5,159 L411.5,159.5 L411,160 L410,160.5 L409.5,161 L409,161 L408,161 L407.5,160.5 L406.5,160 L406,159.5 L405,159 L404.5,158 L404,157 L403,156 L402.5,155 L401.5,154 L401,153 L400,152 L399.5,151 L399,150 L398,149 L397.5,148.5 L396.5,148 L396,147.5 L395.5,147 L394.5,147 L394,147 L393,147.5 L392.5,148 L392,148.5 L391,149 L390.5,150 L389.5,151 L389,152 L388,153 L387.5,154 L387,155 L386,156 L385.5,157 L384.5,158 L384,159 L383,159.5 L382.5,160 L382,160.5 L381,161 L380.5,161 L379.5,161 L379,160.5 L378.5,160 L377.5,159.5 L377,159 L376,158 L375.5,157 L375,156 L374,155 L373.5,154 L372.5,153 L372,152 L371,151 L370.5,150 L370,149 L369,148.5 L368.5,148 L367.5,147.5 L367,147 L366,147 L365.5,147 L365,147.5 L364,148 L363.5,148.5 L362.5,149 L362,150 L361.5,151 L360.5,152 L360,153 L359,154 L358.5,155 L358,156 L357,157 L356.5,158 L355.5,159 L355,159.5 L354,160 L353.5,160.5 L353,161 L352,161 L351.5,161 L350.5,160.5 L350,159 L349,158 L348.5,157 L348,156 L347,155 L346.5,154.5 L345.5,154 L345,154" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M330,154 L345,146.5 L345,161.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M260,154 L259.5,154 L258.5,153.5 L258,153 L257,152 L256.5,151 L256,150 L255,149 L254.5,147.5 L253.5,147 L253,147 L252,147 L251.5,147.5 L251,148 L250,148.5 L249.5,149 L248.5,150 L248,151 L247,152 L246.5,153 L246,154 L245,155 L244.5,156 L243.5,157 L243,158 L242.5,159 L241.5,159.5 L241,160 L240,160.5 L239.5,161 L239,161 L238,161 L237.5,160.5 L236.5,160 L236,159.5 L235,159 L234.5,158 L234,157 L233,156 L232.5,155 L231.5,154 L231,153 L230,152 L229.5,151 L229,150 L228,149 L227.5,148.5 L226.5,148 L226,147.5 L225.5,147 L224.5,147 L224,147 L223,147.5 L222.5,148 L222,148.5 L221,149 L220.5,150 L219.5,151 L219,152 L218,153 L217.5,154 L217,155 L216,156 L215.5,157 L214.5,158 L214,159 L213,159.5 L212.5,160 L212,160.5 L211,161 L210.5,161 L209.5,161 L209,160.5 L208.5,160 L207.5,159.5 L207,159 L206,158 L205.5,157 L205,156 L204,155 L203.5,154 L202.5,153 L202,152 L201,151 L200.5,150 L200,149 L199,148.5 L198.5,148 L197.5,147.5 L197,147 L196,147 L195.5,147 L195,147.5 L194,148 L193.5,148.5 L192.5,149 L192,150 L191.5,151 L190.5,152 L190,153 L189,154 L188.5,155 L188,156 L187,157 L186.5,158 L185.5,159 L185,159.5 L184,160 L183.5,160.5 L183,161 L182,161 L181.5,161 L180.5,160.5 L180,159 L179,158 L178.5,157 L178,156 L177,155 L176.5,154.5 L175.5,154 L175,154" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M160,154 L175,146.5 L175,161.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M222,162 L222,162.5 L222.5,162.5 L222.5,163 L222.5,163.5 L222.5,164 L222,164 L222,164.5 L222,165 L222,165.5 L222,166 L221.5,166.5 L221.5,167 L221.5,167.5 L221,168 L221,168.5 L221,169 L221,169.5 L221,169.5 L221.5,170 L222,170 L222.5,170 L223,170 L223.5,170.5 L224,170.5 L224.5,170.5 L225,170.5 L225.5,170.5 L226,170.5 L227,170.5 L227.5,170.5 L228,170.5 L228.5,170.5 L229,170.5 L230,170.5 L230.5,170.5 L231,170.5 L231.5,170.5 L232,170.5 L232.5,171 L233,171 L233,171 L233.5,171.5 L234,171.5 L234,172 L234.5,172 L234.5,172.5 L234.5,172.5 L234.5,173 L234.5,173.5 L234.5,174 L234.5,174 L234.5,174.5 L234.5,175 L234,175.5 L234,176 L234,176.5 L233.5,177.5 L233.5,178 L233,178.5 L233,179 L232.5,179.5 L232.5,180 L232,180.5 L232,181 L231.5,181.5 L231.5,182 L231,182.5 L231,183 L231,183.5 L231,184 L231,184.5 L231,185 L231,185 L231,185.5 L231.5,186 L231.5,186 L231.5,186.5 L232,186.5 L232.5,187 L232.5,187 L233,187 L233.5,187 L234,187 L234.5,187.5 L235,187.5 L235.5,187.5 L236.5,187.5 L237,187.5 L237.5,187.5 L238,187.5 L239,187.5 L239.5,187.5 L240,187.5 L240.5,187.5 L241,187.5 L241.5,187.5 L242,187.5 L242.5,187.5 L243,188 L243.5,188 L244,188 L244.5,188 L244.5,188.5 L244.5,189 L244.5,189.5 L244.5,190 L244,190.5 L244,191 L244,191.5 L244,192 L243.5,192 L243.5,192.5 L243.5,193 L243.5,193.5 L243,194 L243,194.5 L243,195 L243.5,195 L243.5,195.5 L243.5,196" fill="none" stroke="#f2a69c" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M250,206 L238.5,199 L248.5,192.5 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <path d="M352,162 L352,162.5 L352.5,162.5 L352.5,163 L352.5,163.5 L352.5,164 L352,164 L352,164.5 L352,165 L352,165.5 L352,166 L351.5,166.5 L351.5,167 L351.5,167.5 L351,168 L351,168.5 L351,169 L351,169.5 L351,169.5 L351.5,170 L352,170 L352.5,170 L353,170 L353.5,170.5 L354,170.5 L354.5,170.5 L355,170.5 L355.5,170.5 L356,170.5 L357,170.5 L357.5,170.5 L358,170.5 L358.5,170.5 L359,170.5 L360,170.5 L360.5,170.5 L361,170.5 L361.5,170.5 L362,170.5 L362.5,171 L363,171 L363,171 L363.5,171.5 L364,171.5 L364,172 L364.5,172 L364.5,172.5 L364.5,172.5 L364.5,173 L364.5,173.5 L364.5,174 L364.5,174 L364.5,174.5 L364.5,175 L364,175.5 L364,176 L364,176.5 L363.5,177.5 L363.5,178 L363,178.5 L363,179 L362.5,179.5 L362.5,180 L362,180.5 L362,181 L361.5,181.5 L361.5,182 L361,182.5 L361,183 L361,183.5 L361,184 L361,184.5 L361,185 L361,185 L361,185.5 L361.5,186 L361.5,186 L361.5,186.5 L362,186.5 L362.5,187 L362.5,187 L363,187 L363.5,187 L364,187 L364.5,187.5 L365,187.5 L365.5,187.5 L366.5,187.5 L367,187.5 L367.5,187.5 L368,187.5 L369,187.5 L369.5,187.5 L370,187.5 L370.5,187.5 L371,187.5 L371.5,187.5 L372,187.5 L372.5,187.5 L373,188 L373.5,188 L374,188 L374.5,188 L374.5,188.5 L374.5,189 L374.5,189.5 L374.5,190 L374,190.5 L374,191 L374,191.5 L374,192 L373.5,192 L373.5,192.5 L373.5,193 L373.5,193.5 L373,194 L373,194.5 L373,195 L373.5,195 L373.5,195.5 L373.5,196" fill="none" stroke="#f2a69c" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M380,206 L368.5,199 L378.5,192.5 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="484" y="138" width="92" height="8" rx="3" fill="#c92a2a"/>
  <path d="M566,130 L586,142 L566,154 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <rect x="160" y="216" width="280" height="22" rx="11" fill="url(#fy87c-lamp)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="190" y1="212" x2="190" y2="192" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M190,182 L195,193 L185,193 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="300" y1="212" x2="300" y2="192" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M300,182 L305,193 L295,193 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="410" y1="212" x2="410" y2="192" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M410,182 L415,193 L405,193 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="41.5" y="49.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mirror}\ 100\,\%$</div></foreignObject>
  <foreignObject x="415.5" y="49.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mirror}\ 99\,\%$</div></foreignObject>
  <foreignObject x="221" y="73.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{active medium}$</div></foreignObject>
  <foreignObject x="530" y="171.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\text{beam}$</div></foreignObject>
  <foreignObject x="252.5" y="255.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{pumping}$</div></foreignObject>
</svg>

### Quantum structures: size determines the energy levels
The **energy gap** of a semiconductor is the smallest energy that its electron can get from light or give up as light, and it determines the colour of an LED (chapter *Light from an LED and measuring the Planck constant*). In a large crystal the energy gap depends only on the material. In the chapter *The wave-mechanical model of the atom and orbitals*, the states of an electron were compared with the standing waves of a string: the allowed vibrations of a shorter string are higher and farther apart. The same happens when electrons are confined in a structure only a few nanometres in size. The allowed energies move apart, and the energy gap grows as the structure gets smaller. Such semiconductor structures are called **quantum structures**. A thin layer is a quantum well, and a nanocrystal confined in every direction is a **quantum dot**.

So the colour of a semiconductor quantum dot can be chosen by its size, even though the material is the same. A quantum dot made of cadmium selenide with a diameter of $2\,\text{nm}$ emits cyan light, and a dot with a diameter of $6\,\text{nm}$ emits red light. The energy gap of a large cadmium selenide crystal is $1.74\,\text{eV}$, which corresponds to dark red light at the edge of the visible range, about $713\,\text{nm}$. Making the dot smaller thus moves the light towards shorter wavelengths. In this chapter this qualitative connection is enough. Calculating the energy levels exactly from the size of the dot requires quantum mechanical modelling, and tasks in which the connection between size and wavelength is modelled by calculation are enrichment material. The Nobel Prize in Chemistry 2023 was awarded for the discovery and production of quantum dots.

<svg data-fig="qdots" viewBox="0 0 600 370" role="img" aria-label="Five quantum dots one under another, their diameters to scale with each other, each drawn in the colour of the light it emits. Diameter 2.0 nm: wavelength 480 nm, photon energy 2.58 eV, cyan. 3.0 nm: 530 nm, 2.34 eV, green. 4.0 nm: 570 nm, 2.18 eV, yellow-green. 5.0 nm: 600 nm, 2.07 eV, orange. 6.0 nm: 620 nm, 2.00 eV, red. The smaller the dot, the shorter the wavelength and the greater the photon energy." style="max-width:100%;font-size:24px">
  <circle cx="78" cy="46" r="11" fill="#1098ad" stroke="#1f2933" stroke-width="2"/>
  <circle cx="75" cy="43" r="2.2" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="31.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 2.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="31.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1098ad">$\lambda = 480\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="31.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.58\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="114" r="16.5" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="73" cy="109" r="3.3" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="99.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 3.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="99.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\lambda = 530\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="99.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.34\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="182" r="22" fill="#a8a21f" stroke="#1f2933" stroke-width="2"/>
  <circle cx="71.5" cy="175.5" r="4.4" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="167.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 4.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="167.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda = 570\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.18\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="250" r="27.5" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <circle cx="70" cy="242" r="5.5" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 5.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\lambda = 600\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="235.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.07\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="318" r="33" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="68.5" cy="308.5" r="6.6" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="303.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 6.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="303.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\lambda = 620\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="303.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.00\,\text{eV}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/helium-neon-laser.webp" alt="A black box-shaped device labelled He-Ne LASER sits in a mount on a table; red light shines from its end, with a holder in front of it."><figcaption>A helium–neon laser in an optics set-up. An electric discharge pumps the gas in the tube, and the mirrors at the ends of the tube amplify the light into a narrow red beam with a wavelength of $633\,\text{nm}$.</figcaption></figure>

### Applications of quantum structures
In a quantum dot display, blue backlight hits quantum dots, which absorb it and emit pure green or red light in the same way as in the fluorescence of the chapter *Spectra reveal the energy levels of atoms*. Most laser diodes are quantum well lasers, in which the thickness of the well selects the wavelength. Quantum dot layers are being studied for solar cells, and by the size of the dots they can be tuned to absorb the wanted part of the spectrum of the Sun.

The basic unit of a quantum computer is the **qubit**: a quantum system that has two states and can also be in a combination of them, a superposition. Qubits are made, for example, of electrons confined in the quantum dots of a semiconductor and of superconducting circuits. Such a circuit behaves like an artificial atom with its own quantised energy levels. In Finland, superconducting quantum computers are being built by VTT and IQM. The states of a qubit are sensitive, so the circuits are cooled close to absolute zero and shielded from disturbances of the environment.

<figure class="unit-photo"><img src="pics/fy8/rgb-laser-pointer.webp" alt="Three horizontal laser beams in the dark: red at the top, green in the middle and blue at the bottom; the beams come from devices on the right."><figcaption>Red, green and blue laser beams. Particles in the air scatter some of the light towards the camera, so the beams are visible. A photon of blue light carries the most energy and one of red light the least.</figcaption></figure>

## Formula: Laser photons
All the photons of a laser are produced in the same transition, so the energy and wavelength of each photon are
```latex
\begin{aligned}
hf &= E_2 - E_1 \\
\lambda &= \frac{hc}{E_2 - E_1}
\end{aligned}
```
where $E_2$ is the energy of the upper and $E_1$ of the lower laser level, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$ is the Planck constant, $f$ the frequency of the light, $c = 2.998 \cdot 10^{8}\,\text{m/s}$ the speed of light and $\lambda$ the wavelength.

Because the photons are identical, the power of a laser is the number of photons leaving per second multiplied by the energy of one photon:
```latex
P = \frac{N}{t} \cdot hf
```
where $P$ is the power of the laser and $N$ the number of photons leaving in the time $t$. The number of photons per second is thus $\tfrac{N}{t} = \tfrac{P}{hf}$. Energies are often calculated in electronvolts and converted to joules by substituting $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.

With the same power, a laser of a longer wavelength emits more photons, because one photon carries less energy. In the graph, a red laser pointer of $1.0\,\text{mW}$ emits about $3.3 \cdot 10^{15}$ photons per second and a violet one of equal power about $2.0 \cdot 10^{15}$.

<svg data-fig="rate-graph" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the number of photons per second emitted by a laser of power 1.0 milliwatt as a function of the wavelength. On the horizontal axis the wavelength from zero to 700 nanometres, on the vertical axis the number of photons per second in units of 10 to the power 15 photons per second, from zero to 3.5. The graph is a straight line through the origin. Three laser pointers are marked on it: violet 405 nm, 2.04; green 532 nm, 2.68; and red 650 nm, 3.27. With the same power, a laser of a longer wavelength emits more photons, because one photon carries less energy." style="max-width:100%;font-size:24px">
  <line x1="151.5" y1="290" x2="151.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="207.5" y1="290" x2="207.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="290" x2="263" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="319" y1="290" x2="319" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374.5" y1="290" x2="374.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430.5" y1="290" x2="430.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="486" y1="290" x2="486" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="259" x2="486" y2="259" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="228.5" x2="486" y2="228.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="486" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="166.5" x2="486" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="135.5" x2="486" y2="135.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="105" x2="486" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="74" x2="486" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="500" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M512,290 L499,296 L499,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="60" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,48 L102,61 L90,61 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="151.5" y1="290" x2="151.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="129" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="207.5" y1="290" x2="207.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="185" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="263" y1="290" x2="263" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="319" y1="290" x2="319" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="296.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="374.5" y1="290" x2="374.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="430.5" y1="290" x2="430.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="486" y1="290" x2="486" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="463.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="89" y1="259" x2="96" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="244.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.5$</div></foreignObject>
  <line x1="89" y1="228.5" x2="96" y2="228.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="214" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="183" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.5$</div></foreignObject>
  <line x1="89" y1="166.5" x2="96" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="152" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="135.5" x2="96" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="121" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2.5$</div></foreignObject>
  <line x1="89" y1="105" x2="96" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="74" x2="96" y2="74" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3.5$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="518" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="86" y="17.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N/t\ (10^{15}\,\text{1/s})$</div></foreignObject>
  <polyline points="96,290 486,72.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="321.5" cy="164" r="7" fill="#7048e8" stroke="#ffffff" stroke-width="2"/>
  <circle cx="392.5" cy="124.5" r="7" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <circle cx="458" cy="88" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="224.5" y="123.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$405\,\text{nm}$</div></foreignObject>
  <foreignObject x="295.5" y="84" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$532\,\text{nm}$</div></foreignObject>
  <foreignObject x="361" y="47.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$650\,\text{nm}$</div></foreignObject>
  <foreignObject x="362" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P = 1.0\,\text{mW}$</div></foreignObject>
</svg>

## Worked example
The energy difference of the levels of the laser transition of a helium–neon laser is $1.96\,\text{eV}$, and the power of the laser is $1.0\,\text{mW}$. How many photons does the laser emit per second?

<!-- vaihe -->

**Given and asked.** The energy difference of the levels is $E_2 - E_1 = 1.96\,\text{eV}$ and the power is $P = 1.0\,\text{mW}$. We are asked for the number of photons leaving per second, $\tfrac{N}{t}$.

<!-- vaihe -->

**Principle.** All the photons of a laser are produced in the same transition, so the energy of each is $hf = E_2 - E_1$. The power is the number of photons per second multiplied by the energy of one photon.

<!-- vaihe -->

**Formula solved.** We substitute the difference of the levels for the energy of the photon and solve the number of photons per second:
```latex
\begin{aligned}
&P = \frac{N}{t} \cdot (E_2 - E_1) \\
&\frac{N}{t} = \frac{P}{E_2 - E_1}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The power is $P = 1.0\,\text{mW} = 1.0 \cdot 10^{-3}\,\text{W}$, and the energy difference is converted to joules by substituting $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$: $E_2 - E_1 = 1.96 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 3.1399 \cdot 10^{-19}\,\text{J}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\frac{N}{t} = \frac{P}{E_2 - E_1} \\
&= \frac{1.0 \cdot 10^{-3}\,\text{W}}{3.1399 \cdot 10^{-19}\,\text{J}} \\
&= 3.1848 \cdot 10^{15}\,\tfrac{1}{\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Result.** The laser emits about $3.2 \cdot 10^{15}$ photons per second. The result is given with two significant figures, because the power $1.0\,\text{mW}$ is given with two.

<!-- vaihe -->

**Reasonableness.** The unit is correct, because $\tfrac{\text{W}}{\text{J}} = \tfrac{\text{J/s}}{\text{J}} = \tfrac{1}{\text{s}}$. The energy difference corresponds to the wavelength $\lambda = \tfrac{hc}{E_2 - E_1} \approx 633\,\text{nm}$, the familiar red light of a helium–neon laser. According to the graph, a laser of $1.0\,\text{mW}$ emits about $3.3 \cdot 10^{15}$ photons per second at the wavelength $650\,\text{nm}$, so a slightly smaller number at a slightly shorter wavelength is credible.

## Common misconception
Many think that laser light is dangerous because its photons would be especially energetic. But the energy of a photon depends only on the wavelength: the photon energy $1.91\,\text{eV}$ of a red laser pointer is the same as that of any light of $650\,\text{nm}$, and the photons of violet light of $405\,\text{nm}$ are more energetic, whether they come from a laser or from a lamp. The danger of a laser is that the whole power travels in a narrow beam, which the lens of the eye focuses on the retina into a very small spot. That is why only low-power lasers are used at school, and nobody looks into the beam or its mirror reflection or points it at people.

Another mistake is to think that in stimulated emission the atom absorbs a photon and emits two. The incoming photon is not absorbed but continues on its way. The energy of the new photon comes from the excited atom, which drops from the level $E_2$ to the level $E_1$, so energy is conserved.

## Tunnelling {Tunneloituminen}
According to classical physics, a ball whose energy is not enough to get over a hill rolls back. In quantum physics, the probability of detecting an electron does not end at the edge of a barrier but decreases quickly inside the barrier. If the barrier is very thin, the probability behind the barrier remains small but not zero: the electron can be found behind the barrier even though its energy is smaller than the energy needed to cross the barrier. This is called **tunnelling**. The probability decreases extremely steeply as the barrier gets thicker and higher, so tunnelling is significant only for barriers of the order of nanometres.

<svg data-fig="tunnel" viewBox="0 0 600 320" role="img" aria-label="Schematic figure of tunnelling, not to scale. An electron arrives from the left; its energy E, the horizontal dashed line, is smaller than the height of the grey barrier in the middle. The blue area shows the probability of detecting the electron: on the left of the barrier it is large, inside the barrier it decreases quickly, and on the right of the barrier it is small but not zero. So the electron can be found behind the barrier even though its energy is not enough to get over the barrier." style="max-width:100%;font-size:24px">
  <rect x="270" y="90" width="60" height="170" rx="2" fill="#c9c2b2" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="24" y1="260" x2="576" y2="260" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="24" y1="180" x2="576" y2="180" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M30,260 L30,198 L30,198 L34,196 L38,194 L42,192.5 L46,192 L50,192 L54,193 L58,194.5 L62,197 L66,199 L70,201 L74,202.5 L78,203.5 L82,204 L86,203.5 L90,202 L94,200.5 L98,198.5 L102,196 L106,194 L110,193 L114,192 L118,192 L122,193 L126,194.5 L130,196.5 L134,198.5 L138,200.5 L142,202.5 L146,203.5 L150,204 L154,203.5 L158,202.5 L162,200.5 L166,198.5 L170,196.5 L174,194.5 L178,193 L182,192 L186,192 L190,193 L194,194 L198,196 L202,198.5 L206,200.5 L210,202 L214,203.5 L218,204 L222,203.5 L226,202.5 L230,201 L234,199 L238,197 L242,194.5 L246,193 L250,192 L254,192 L258,192.5 L262,194 L266,196 L270,198 L270,198 L271.5,200.5 L273,203.5 L274.5,206 L276,208 L277.5,210.5 L279,212.5 L280.5,215 L282,216.5 L283.5,218.5 L285,220.5 L286.5,222 L288,224 L289.5,225.5 L291,227 L292.5,228.5 L294,230 L295.5,231 L297,232.5 L298.5,233.5 L300,235 L301.5,236 L303,237 L304.5,238 L306,239 L307.5,240 L309,241 L310.5,241.5 L312,242.5 L313.5,243 L315,244 L316.5,244.5 L318,245.5 L319.5,246 L321,246.5 L322.5,247 L324,247.5 L325.5,248.5 L327,249 L328.5,249.5 L330,250 L570,250 L570,260 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="252.5" y="51.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{barrier}$</div></foreignObject>
  <foreignObject x="36" y="143.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$E$</div></foreignObject>
  <foreignObject x="46" y="275.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{incoming electron}$</div></foreignObject>
  <foreignObject x="352" y="275.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{behind the barrier}$</div></foreignObject>
  <line x1="380" y1="210" x2="439" y2="210" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M450,210 L438,215.5 L438,204.5 Z" fill="#1971c2" stroke-linejoin="round"/>
</svg>

In a scanning tunnelling microscope, a sharp metal tip is brought about a nanometre from a surface. The current of electrons tunnelling between the tip and the surface changes strongly with the distance, so the tip can be used to image single atoms. A bit is written into a memory cell of flash memory by moving electrons through a thin insulating layer by tunnelling. In superconducting qubits the current passes through a thin insulating layer by tunnelling; the Nobel Prize in Physics 2025 was awarded for the discovery of quantum tunnelling and the quantisation of energy in such circuits. Alpha decay, discussed in the chapter *The atomic nucleus and radioactive decay*, is also tunnelling.

## Summary
- An excited atom can emit a photon by itself (spontaneous emission) or under the influence of an incoming photon (stimulated emission). Stimulated emission produces a photon with the energy, direction and phase of the incoming photon.
- Light is amplified only when the upper laser level has more atoms than the lower one, $N_2 > N_1$ (population inversion). In atomic and ion lasers it is obtained by pumping a medium that has three or four levels and a long-lived upper laser level. In a semiconductor laser the inversion is produced in the energy bands by an electric current.
- Between the mirrors, light along the axis passes through the medium many times and is amplified; the laser works when the pumping exceeds the threshold. Laser light is nearly monochromatic, directional and coherent.
- The energy of the photons of a laser is $hf = E_2 - E_1$, and the power is $P = \tfrac{N}{t} \cdot hf$.
- In semiconductor quantum structures the electrons are confined in a space of nanometre size, and the energy gap grows as the structure gets smaller: a smaller quantum dot emits a shorter wavelength. Applications are quantum dot displays, quantum well lasers, research on solar cells and the qubits of quantum computers.
