# Interference and diffraction of light

> **Why** does the beam of a laser pointer draw a whole row of dots of light on the wall when it passes through a thin transparent film?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a dark classroom. On the table on the left there is a laser pointer on a small stand, and in front of it a thin transparent film mounted in a slide frame. The laser beam passes through the film, and faint rays fan out from the film to a white board on the right. On the board there is a horizontal row of evenly spaced red dots of light; the middle one is the brightest, and the dots become dimmer towards the edges." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy713h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy713h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><radialGradient id="fy713h-glow"><stop offset="0" stop-color="#ffffff"/><stop offset="0.3" stop-color="#e64980"/><stop offset="1" stop-color="#e64980" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy713h-wall)"/>
  <rect x="0" y="430" width="1200" height="170" fill="url(#fy713h-table)"/>
  <line x1="0" y1="430" x2="1200" y2="430" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M760,110 L1150,60 L1150,420 L760,400 Z" fill="#e3dccb" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <path d="M772,122 L1138,76 L1138,408 L772,390 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="150" y="392" width="26" height="38" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="70" y="362" width="190" height="32" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="232" y="366" width="28" height="24" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="90" y="362" width="18" height="32" fill="#6c757d"/>
  <rect x="392" y="420" width="56" height="12" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="404" y="316" width="32" height="108" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="412" y="334" width="16" height="72" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="260" y1="378" x2="420" y2="378" stroke="#e64980" stroke-width="5" stroke-linecap="butt"/>
  <line x1="420" y1="378" x2="763" y2="256" stroke="#e64980" stroke-width="3" stroke-opacity="0.20"/>
  <line x1="420" y1="378" x2="827" y2="250" stroke="#e64980" stroke-width="3" stroke-opacity="0.30"/>
  <line x1="420" y1="378" x2="891" y2="244" stroke="#e64980" stroke-width="3" stroke-opacity="0.40"/>
  <line x1="420" y1="378" x2="955" y2="238" stroke="#e64980" stroke-width="3" stroke-opacity="0.50"/>
  <line x1="420" y1="378" x2="1019" y2="232" stroke="#e64980" stroke-width="3" stroke-opacity="0.40"/>
  <line x1="420" y1="378" x2="1083" y2="226" stroke="#e64980" stroke-width="3" stroke-opacity="0.30"/>
  <line x1="420" y1="378" x2="1147" y2="220" stroke="#e64980" stroke-width="3" stroke-opacity="0.20"/>
  <circle cx="763" cy="256" r="16" fill="url(#fy713h-glow)"/>
  <circle cx="763" cy="256" r="4" fill="#e64980"/>
  <circle cx="827" cy="250" r="22" fill="url(#fy713h-glow)"/>
  <circle cx="827" cy="250" r="5" fill="#e64980"/>
  <circle cx="891" cy="244" r="28" fill="url(#fy713h-glow)"/>
  <circle cx="891" cy="244" r="6" fill="#e64980"/>
  <circle cx="955" cy="238" r="34" fill="url(#fy713h-glow)"/>
  <circle cx="955" cy="238" r="7" fill="#e64980"/>
  <circle cx="1019" cy="232" r="28" fill="url(#fy713h-glow)"/>
  <circle cx="1019" cy="232" r="6" fill="#e64980"/>
  <circle cx="1083" cy="226" r="22" fill="url(#fy713h-glow)"/>
  <circle cx="1083" cy="226" r="5" fill="#e64980"/>
  <circle cx="1147" cy="220" r="16" fill="url(#fy713h-glow)"/>
  <circle cx="1147" cy="220" r="4" fill="#e64980"/>
</svg>

## Key idea

### Light as a wave
In the chapter *When waves combine: superposition and interference* we saw that the waves from two sources of the same frequency, oscillating in the same phase, form a stable interference pattern. At places where the path difference $\Delta s$ of the waves is a whole number of wavelengths, the waves reinforce each other. At places where the path difference is half a wavelength more than a whole number, they weaken each other. Light is electromagnetic wave motion (chapter *Electromagnetic radiation and the black-body spectrum*), so light should interfere, too. The wavelength of visible light is very small, however, about $400$–$700\,\text{nm}$. For the interference of light to be clearly visible, the slit separations and the measuring arrangement must be suitable. The spacing of the fringes is not determined by the wavelength alone but also by the geometry of the slits and the screen. In a suitable experiment the bright and dark fringes can be millimetres or centimetres apart.

<figure class="unit-photo"><img src="pics/fy7/laser-interference.webp" alt="Concentric red rings on a black background; a bright white spot in the centre, with the rings fading outwards."><figcaption>An interference pattern of red laser light. In the bright rings the waves reinforce each other, and in the dark rings they cancel. The pattern forms because laser light is coherent.</figcaption></figure>

### Coherent light
A stable pattern forms only when the sources are **coherent**: they have the same frequency, and their phase difference stays constant. Two ordinary lamps do not produce a pattern. The light of a lamp is emitted by countless atoms independently of each other, so the phase difference of the light of two lamps varies randomly and very rapidly. The places of constructive and destructive interference then keep swapping, and the eye sees only an even illumination. The light of a laser is coherent. Coherent sources can also be obtained by dividing the light of one source into two parts, for example with two slits.

### Diffraction at a slit
When light passes through a narrow slit, it does not continue as a sharp beam but spreads out behind the slit, also into directions that would be in shadow. This is **diffraction**, which is familiar from water waves (chapter *A wave meets an obstacle or a gap*). Diffraction is strong when the width of the slit is of the order of the wavelength. The narrower the slit, the wider the light spreads: when the slit is narrowed, the bright central region on the screen widens instead of narrowing. Light coming through a window does not seem to bend, because the window is millions of times wider than the wavelength.

<svg data-fig="slit" viewBox="0 0 600 360" role="img" aria-label="Schematic diagram, not to scale: two panels one above the other. In both, plane wavefronts arrive from the left and hit a wall with a slit. In the upper panel the slit is many wavelengths wide: behind the slit the wavefronts continue almost straight, curving a little only at the edges, and the light travels as a narrow beam. In the lower panel the slit is as wide as the wavelength: behind the slit the wavefronts are semicircles, and the light spreads over a wide region, also behind the wall." style="max-width:100%;font-size:24px">
  <defs><clipPath id="fy713-slit-c0"><rect x="12" y="22" width="576" height="150"/></clipPath><clipPath id="fy713-slit-c1"><rect x="12" y="196" width="576" height="150"/></clipPath></defs>
  <rect x="12" y="22" width="576" height="150" rx="6" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <g clip-path="url(#fy713-slit-c0)">
  <line x1="186" y1="30" x2="186" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="166" y1="30" x2="166" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="146" y1="30" x2="146" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="126" y1="30" x2="126" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="106" y1="30" x2="106" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="86" y1="30" x2="86" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="66" y1="30" x2="66" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="46" y1="30" x2="46" y2="164" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M213.5,45.5 A14,14 0 0,1 214,49 L214,145 A14,14 0 0,1 213.5,148.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.96"/>
  <path d="M232.5,39.5 A34,34 0 0,1 234,49 L234,145 A34,34 0 0,1 232.5,154.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.93"/>
  <path d="M251.5,33.5 A54,54 0 0,1 254,49 L254,145 A54,54 0 0,1 251.5,160.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.90"/>
  <path d="M270.5,26.5 A74,74 0 0,1 274,49 L274,145 A74,74 0 0,1 270.5,167.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.86"/>
  <path d="M289,19 A94,94 0 0,1 294,49 L294,145 A94,94 0 0,1 289,175" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.82"/>
  <path d="M307.5,11 A114,114 0 0,1 314,49 L314,145 A114,114 0 0,1 307.5,183" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.79"/>
  <path d="M325.5,2.5 A134,134 0 0,1 334,49 L334,145 A134,134 0 0,1 325.5,191.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.76"/>
  <path d="M343.5,-6.5 A154,154 0 0,1 354,49 L354,145 A154,154 0 0,1 343.5,200.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.72"/>
  <path d="M361,-16.5 A174,174 0 0,1 374,49 L374,145 A174,174 0 0,1 361,210.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.68"/>
  <path d="M378.5,-27 A194,194 0 0,1 394,49 L394,145 A194,194 0 0,1 378.5,221" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.65"/>
  <path d="M395.5,-37.5 A214,214 0 0,1 414,49 L414,145 A214,214 0 0,1 395.5,231.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.61"/>
  <path d="M412.5,-49 A234,234 0 0,1 434,49 L434,145 A234,234 0 0,1 412.5,243" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.58"/>
  <path d="M429,-61 A254,254 0 0,1 454,49 L454,145 A254,254 0 0,1 429,255" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.54"/>
  <path d="M445,-73.5 A274,274 0 0,1 474,49 L474,145 A274,274 0 0,1 445,267.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.51"/>
  <path d="M461,-87 A294,294 0 0,1 494,49 L494,145 A294,294 0 0,1 461,281" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.47"/>
  <path d="M476,-100.5 A314,314 0 0,1 514,49 L514,145 A314,314 0 0,1 476,294.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.44"/>
  <path d="M491.5,-114.5 A334,334 0 0,1 534,49 L534,145 A334,334 0 0,1 491.5,308.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.40"/>
  <path d="M506,-129 A354,354 0 0,1 554,49 L554,145 A354,354 0 0,1 506,323" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.37"/>
  <path d="M520,-144 A374,374 0 0,1 574,49 L574,145 A374,374 0 0,1 520,338" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.33"/>
  </g>
  <rect x="190" y="23" width="10" height="26" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="190" y="145" width="10" height="26" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="30" y="29.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{wide slit}$</span></div></foreignObject>
  <rect x="12" y="196" width="576" height="150" rx="6" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <g clip-path="url(#fy713-slit-c1)">
  <line x1="186" y1="204" x2="186" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="166" y1="204" x2="166" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="146" y1="204" x2="146" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="126" y1="204" x2="126" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="106" y1="204" x2="106" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="86" y1="204" x2="86" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="66" y1="204" x2="66" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="46" y1="204" x2="46" y2="338" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M202.5,257 A14,14 0 0,1 202.5,285" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.96"/>
  <path d="M206,237.5 A34,34 0 0,1 206,304.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.93"/>
  <path d="M209.5,218 A54,54 0 0,1 209.5,324" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.90"/>
  <path d="M213,198 A74,74 0 0,1 213,344" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.86"/>
  <path d="M216.5,178.5 A94,94 0 0,1 216.5,363.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.82"/>
  <path d="M220,158.5 A114,114 0 0,1 220,383.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.79"/>
  <path d="M223.5,139 A134,134 0 0,1 223.5,403" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.76"/>
  <path d="M226.5,119.5 A154,154 0 0,1 226.5,422.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.72"/>
  <path d="M230,99.5 A174,174 0 0,1 230,442.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.68"/>
  <path d="M233.5,80 A194,194 0 0,1 233.5,462" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.65"/>
  <path d="M237,60.5 A214,214 0 0,1 237,481.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.61"/>
  <path d="M240.5,40.5 A234,234 0 0,1 240.5,501.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.58"/>
  <path d="M244,21 A254,254 0 0,1 244,521" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.54"/>
  <path d="M247.5,1 A274,274 0 0,1 247.5,541" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.51"/>
  <path d="M251,-18.5 A294,294 0 0,1 251,560.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.47"/>
  <path d="M254.5,-38 A314,314 0 0,1 254.5,580" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.44"/>
  <path d="M258,-58 A334,334 0 0,1 258,600" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.40"/>
  <path d="M261.5,-77.5 A354,354 0 0,1 261.5,619.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.37"/>
  <path d="M265,-97.5 A374,374 0 0,1 265,639.5" fill="none" stroke="#e64980" stroke-width="2.5" stroke-opacity="0.33"/>
  </g>
  <rect x="190" y="197" width="10" height="66" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="190" y="279" width="10" height="66" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="30" y="203.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{narrow slit}$</span></div></foreignObject>
</svg>

### Young's double-slit experiment
At the beginning of the 19th century Thomas Young carried out an experiment that showed light to be a wave motion. He directed the same light at two narrow slits close together. Because of diffraction, the light spreads widely from each slit, and the waves from the slits overlap. Because the light at both slits comes from the same wavefront, the slits act as coherent sources. Evenly spaced bright and dark fringes form on the screen. In the middle there is a bright fringe, because the distance from each slit to that point is equal. In the next bright fringe the path difference is one wavelength. The dark fringes are the hallmark of interference: they receive less light from the two slits together than from either slit alone.

<svg data-fig="young" viewBox="0 0 600 360" role="img" aria-label="Schematic diagram, not to scale: Young&#x27;s double-slit experiment seen from above. Plane wavefronts arrive from the left at a wall with two narrow slits S1 and S2. Circular wavefronts spread from each slit and overlap. On the screen on the right bright and dark fringes alternate; in the middle there is a bright fringe. Point P, which is the first bright fringe above the central fringe, is one wavelength farther from slit S2 than from slit S1." style="max-width:100%;font-size:24px">
  <defs><clipPath id="fy713-young-c"><rect x="154" y="16" width="322" height="296"/></clipPath></defs>
  <line x1="136" y1="30" x2="136" y2="300" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="112" y1="30" x2="112" y2="300" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="88" y1="30" x2="88" y2="300" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="64" y1="30" x2="64" y2="300" stroke="#e64980" stroke-width="2.5" stroke-linecap="butt"/>
  <g clip-path="url(#fy713-young-c)">
  <path d="M151.5,106 A24,24 0 0,1 151.5,154" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M153.5,82 A48,48 0 0,1 153.5,178" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M155,58 A72,72 0 0,1 155,202" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M156.5,34 A96,96 0 0,1 156.5,226" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M158.5,10.5 A120,120 0 0,1 158.5,249.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M160,-13.5 A144,144 0 0,1 160,273.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M161.5,-37.5 A168,168 0 0,1 161.5,297.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M163.5,-61.5 A192,192 0 0,1 163.5,321.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M165,-85.5 A216,216 0 0,1 165,345.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M166.5,-109.5 A240,240 0 0,1 166.5,369.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M168.5,-133.5 A264,264 0 0,1 168.5,393.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M170,-157.5 A288,288 0 0,1 170,417.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M172,-181 A312,312 0 0,1 172,441" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M173.5,-205 A336,336 0 0,1 173.5,465" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M151.5,186 A24,24 0 0,1 151.5,234" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M153.5,162 A48,48 0 0,1 153.5,258" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M155,138 A72,72 0 0,1 155,282" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M156.5,114 A96,96 0 0,1 156.5,306" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M158.5,90.5 A120,120 0 0,1 158.5,329.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M160,66.5 A144,144 0 0,1 160,353.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M161.5,42.5 A168,168 0 0,1 161.5,377.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M163.5,18.5 A192,192 0 0,1 163.5,401.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M165,-5.5 A216,216 0 0,1 165,425.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M166.5,-29.5 A240,240 0 0,1 166.5,449.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M168.5,-53.5 A264,264 0 0,1 168.5,473.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M170,-77.5 A288,288 0 0,1 170,497.5" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M172,-101 A312,312 0 0,1 172,521" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  <path d="M173.5,-125 A336,336 0 0,1 173.5,545" fill="none" stroke="#e64980" stroke-width="2" stroke-opacity="0.55"/>
  </g>
  <rect x="146" y="16" width="10" height="109" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="146" y="135" width="10" height="70" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="146" y="215" width="10" height="97" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="480" y="16" width="20" height="296" fill="#1f2933"/>
  <rect x="480" y="16" width="20" height="2" fill="#e64980" fill-opacity="0.09"/>
  <rect x="480" y="18" width="20" height="2" fill="#e64980" fill-opacity="0.12"/>
  <rect x="480" y="20" width="20" height="2" fill="#e64980" fill-opacity="0.15"/>
  <rect x="480" y="22" width="20" height="2" fill="#e64980" fill-opacity="0.19"/>
  <rect x="480" y="24" width="20" height="2" fill="#e64980" fill-opacity="0.23"/>
  <rect x="480" y="26" width="20" height="2" fill="#e64980" fill-opacity="0.27"/>
  <rect x="480" y="28" width="20" height="2" fill="#e64980" fill-opacity="0.32"/>
  <rect x="480" y="30" width="20" height="2" fill="#e64980" fill-opacity="0.36"/>
  <rect x="480" y="32" width="20" height="2" fill="#e64980" fill-opacity="0.41"/>
  <rect x="480" y="34" width="20" height="2" fill="#e64980" fill-opacity="0.46"/>
  <rect x="480" y="36" width="20" height="2" fill="#e64980" fill-opacity="0.51"/>
  <rect x="480" y="38" width="20" height="2" fill="#e64980" fill-opacity="0.56"/>
  <rect x="480" y="40" width="20" height="2" fill="#e64980" fill-opacity="0.61"/>
  <rect x="480" y="42" width="20" height="2" fill="#e64980" fill-opacity="0.66"/>
  <rect x="480" y="44" width="20" height="2" fill="#e64980" fill-opacity="0.71"/>
  <rect x="480" y="46" width="20" height="2" fill="#e64980" fill-opacity="0.76"/>
  <rect x="480" y="48" width="20" height="2" fill="#e64980" fill-opacity="0.80"/>
  <rect x="480" y="50" width="20" height="2" fill="#e64980" fill-opacity="0.84"/>
  <rect x="480" y="52" width="20" height="2" fill="#e64980" fill-opacity="0.88"/>
  <rect x="480" y="54" width="20" height="2" fill="#e64980" fill-opacity="0.91"/>
  <rect x="480" y="56" width="20" height="2" fill="#e64980" fill-opacity="0.94"/>
  <rect x="480" y="58" width="20" height="2" fill="#e64980" fill-opacity="0.96"/>
  <rect x="480" y="60" width="20" height="2" fill="#e64980" fill-opacity="0.98"/>
  <rect x="480" y="62" width="20" height="2" fill="#e64980" fill-opacity="0.99"/>
  <rect x="480" y="64" width="20" height="2" fill="#e64980" fill-opacity="1.00"/>
  <rect x="480" y="66" width="20" height="2" fill="#e64980" fill-opacity="1.00"/>
  <rect x="480" y="68" width="20" height="2" fill="#e64980" fill-opacity="0.99"/>
  <rect x="480" y="70" width="20" height="2" fill="#e64980" fill-opacity="0.98"/>
  <rect x="480" y="72" width="20" height="2" fill="#e64980" fill-opacity="0.96"/>
  <rect x="480" y="74" width="20" height="2" fill="#e64980" fill-opacity="0.94"/>
  <rect x="480" y="76" width="20" height="2" fill="#e64980" fill-opacity="0.91"/>
  <rect x="480" y="78" width="20" height="2" fill="#e64980" fill-opacity="0.88"/>
  <rect x="480" y="80" width="20" height="2" fill="#e64980" fill-opacity="0.84"/>
  <rect x="480" y="82" width="20" height="2" fill="#e64980" fill-opacity="0.79"/>
  <rect x="480" y="84" width="20" height="2" fill="#e64980" fill-opacity="0.74"/>
  <rect x="480" y="86" width="20" height="2" fill="#e64980" fill-opacity="0.69"/>
  <rect x="480" y="88" width="20" height="2" fill="#e64980" fill-opacity="0.64"/>
  <rect x="480" y="90" width="20" height="2" fill="#e64980" fill-opacity="0.58"/>
  <rect x="480" y="92" width="20" height="2" fill="#e64980" fill-opacity="0.52"/>
  <rect x="480" y="94" width="20" height="2" fill="#e64980" fill-opacity="0.46"/>
  <rect x="480" y="96" width="20" height="2" fill="#e64980" fill-opacity="0.41"/>
  <rect x="480" y="98" width="20" height="2" fill="#e64980" fill-opacity="0.35"/>
  <rect x="480" y="100" width="20" height="2" fill="#e64980" fill-opacity="0.29"/>
  <rect x="480" y="102" width="20" height="2" fill="#e64980" fill-opacity="0.24"/>
  <rect x="480" y="104" width="20" height="2" fill="#e64980" fill-opacity="0.19"/>
  <rect x="480" y="106" width="20" height="2" fill="#e64980" fill-opacity="0.15"/>
  <rect x="480" y="108" width="20" height="2" fill="#e64980" fill-opacity="0.11"/>
  <rect x="480" y="110" width="20" height="2" fill="#e64980" fill-opacity="0.07"/>
  <rect x="480" y="112" width="20" height="2" fill="#e64980" fill-opacity="0.04"/>
  <rect x="480" y="126" width="20" height="2" fill="#e64980" fill-opacity="0.05"/>
  <rect x="480" y="128" width="20" height="2" fill="#e64980" fill-opacity="0.08"/>
  <rect x="480" y="130" width="20" height="2" fill="#e64980" fill-opacity="0.11"/>
  <rect x="480" y="132" width="20" height="2" fill="#e64980" fill-opacity="0.15"/>
  <rect x="480" y="134" width="20" height="2" fill="#e64980" fill-opacity="0.20"/>
  <rect x="480" y="136" width="20" height="2" fill="#e64980" fill-opacity="0.25"/>
  <rect x="480" y="138" width="20" height="2" fill="#e64980" fill-opacity="0.31"/>
  <rect x="480" y="140" width="20" height="2" fill="#e64980" fill-opacity="0.37"/>
  <rect x="480" y="142" width="20" height="2" fill="#e64980" fill-opacity="0.43"/>
  <rect x="480" y="144" width="20" height="2" fill="#e64980" fill-opacity="0.49"/>
  <rect x="480" y="146" width="20" height="2" fill="#e64980" fill-opacity="0.56"/>
  <rect x="480" y="148" width="20" height="2" fill="#e64980" fill-opacity="0.62"/>
  <rect x="480" y="150" width="20" height="2" fill="#e64980" fill-opacity="0.68"/>
  <rect x="480" y="152" width="20" height="2" fill="#e64980" fill-opacity="0.74"/>
  <rect x="480" y="154" width="20" height="2" fill="#e64980" fill-opacity="0.79"/>
  <rect x="480" y="156" width="20" height="2" fill="#e64980" fill-opacity="0.84"/>
  <rect x="480" y="158" width="20" height="2" fill="#e64980" fill-opacity="0.88"/>
  <rect x="480" y="160" width="20" height="2" fill="#e64980" fill-opacity="0.92"/>
  <rect x="480" y="162" width="20" height="2" fill="#e64980" fill-opacity="0.95"/>
  <rect x="480" y="164" width="20" height="2" fill="#e64980" fill-opacity="0.98"/>
  <rect x="480" y="166" width="20" height="2" fill="#e64980" fill-opacity="0.99"/>
  <rect x="480" y="168" width="20" height="2" fill="#e64980" fill-opacity="1.00"/>
  <rect x="480" y="170" width="20" height="2" fill="#e64980" fill-opacity="1.00"/>
  <rect x="480" y="172" width="20" height="2" fill="#e64980" fill-opacity="0.99"/>
  <rect x="480" y="174" width="20" height="2" fill="#e64980" fill-opacity="0.98"/>
  <rect x="480" y="176" width="20" height="2" fill="#e64980" fill-opacity="0.95"/>
  <rect x="480" y="178" width="20" height="2" fill="#e64980" fill-opacity="0.92"/>
  <rect x="480" y="180" width="20" height="2" fill="#e64980" fill-opacity="0.88"/>
  <rect x="480" y="182" width="20" height="2" fill="#e64980" fill-opacity="0.84"/>
  <rect x="480" y="184" width="20" height="2" fill="#e64980" fill-opacity="0.79"/>
  <rect x="480" y="186" width="20" height="2" fill="#e64980" fill-opacity="0.74"/>
  <rect x="480" y="188" width="20" height="2" fill="#e64980" fill-opacity="0.68"/>
  <rect x="480" y="190" width="20" height="2" fill="#e64980" fill-opacity="0.62"/>
  <rect x="480" y="192" width="20" height="2" fill="#e64980" fill-opacity="0.56"/>
  <rect x="480" y="194" width="20" height="2" fill="#e64980" fill-opacity="0.49"/>
  <rect x="480" y="196" width="20" height="2" fill="#e64980" fill-opacity="0.43"/>
  <rect x="480" y="198" width="20" height="2" fill="#e64980" fill-opacity="0.37"/>
  <rect x="480" y="200" width="20" height="2" fill="#e64980" fill-opacity="0.31"/>
  <rect x="480" y="202" width="20" height="2" fill="#e64980" fill-opacity="0.25"/>
  <rect x="480" y="204" width="20" height="2" fill="#e64980" fill-opacity="0.20"/>
  <rect x="480" y="206" width="20" height="2" fill="#e64980" fill-opacity="0.15"/>
  <rect x="480" y="208" width="20" height="2" fill="#e64980" fill-opacity="0.11"/>
  <rect x="480" y="210" width="20" height="2" fill="#e64980" fill-opacity="0.08"/>
  <rect x="480" y="212" width="20" height="2" fill="#e64980" fill-opacity="0.05"/>
  <rect x="480" y="226" width="20" height="2" fill="#e64980" fill-opacity="0.04"/>
  <rect x="480" y="228" width="20" height="2" fill="#e64980" fill-opacity="0.07"/>
  <rect x="480" y="230" width="20" height="2" fill="#e64980" fill-opacity="0.11"/>
  <rect x="480" y="232" width="20" height="2" fill="#e64980" fill-opacity="0.15"/>
  <rect x="480" y="234" width="20" height="2" fill="#e64980" fill-opacity="0.19"/>
  <rect x="480" y="236" width="20" height="2" fill="#e64980" fill-opacity="0.24"/>
  <rect x="480" y="238" width="20" height="2" fill="#e64980" fill-opacity="0.29"/>
  <rect x="480" y="240" width="20" height="2" fill="#e64980" fill-opacity="0.35"/>
  <rect x="480" y="242" width="20" height="2" fill="#e64980" fill-opacity="0.41"/>
  <rect x="480" y="244" width="20" height="2" fill="#e64980" fill-opacity="0.46"/>
  <rect x="480" y="246" width="20" height="2" fill="#e64980" fill-opacity="0.52"/>
  <rect x="480" y="248" width="20" height="2" fill="#e64980" fill-opacity="0.58"/>
  <rect x="480" y="250" width="20" height="2" fill="#e64980" fill-opacity="0.64"/>
  <rect x="480" y="252" width="20" height="2" fill="#e64980" fill-opacity="0.69"/>
  <rect x="480" y="254" width="20" height="2" fill="#e64980" fill-opacity="0.74"/>
  <rect x="480" y="256" width="20" height="2" fill="#e64980" fill-opacity="0.79"/>
  <rect x="480" y="258" width="20" height="2" fill="#e64980" fill-opacity="0.84"/>
  <rect x="480" y="260" width="20" height="2" fill="#e64980" fill-opacity="0.88"/>
  <rect x="480" y="262" width="20" height="2" fill="#e64980" fill-opacity="0.91"/>
  <rect x="480" y="264" width="20" height="2" fill="#e64980" fill-opacity="0.94"/>
  <rect x="480" y="266" width="20" height="2" fill="#e64980" fill-opacity="0.96"/>
  <rect x="480" y="268" width="20" height="2" fill="#e64980" fill-opacity="0.98"/>
  <rect x="480" y="270" width="20" height="2" fill="#e64980" fill-opacity="0.99"/>
  <rect x="480" y="272" width="20" height="2" fill="#e64980" fill-opacity="1.00"/>
  <rect x="480" y="274" width="20" height="2" fill="#e64980" fill-opacity="1.00"/>
  <rect x="480" y="276" width="20" height="2" fill="#e64980" fill-opacity="0.99"/>
  <rect x="480" y="278" width="20" height="2" fill="#e64980" fill-opacity="0.98"/>
  <rect x="480" y="280" width="20" height="2" fill="#e64980" fill-opacity="0.96"/>
  <rect x="480" y="282" width="20" height="2" fill="#e64980" fill-opacity="0.94"/>
  <rect x="480" y="284" width="20" height="2" fill="#e64980" fill-opacity="0.91"/>
  <rect x="480" y="286" width="20" height="2" fill="#e64980" fill-opacity="0.88"/>
  <rect x="480" y="288" width="20" height="2" fill="#e64980" fill-opacity="0.84"/>
  <rect x="480" y="290" width="20" height="2" fill="#e64980" fill-opacity="0.80"/>
  <rect x="480" y="292" width="20" height="2" fill="#e64980" fill-opacity="0.76"/>
  <rect x="480" y="294" width="20" height="2" fill="#e64980" fill-opacity="0.71"/>
  <rect x="480" y="296" width="20" height="2" fill="#e64980" fill-opacity="0.66"/>
  <rect x="480" y="298" width="20" height="2" fill="#e64980" fill-opacity="0.61"/>
  <rect x="480" y="300" width="20" height="2" fill="#e64980" fill-opacity="0.56"/>
  <rect x="480" y="302" width="20" height="2" fill="#e64980" fill-opacity="0.51"/>
  <rect x="480" y="304" width="20" height="2" fill="#e64980" fill-opacity="0.46"/>
  <rect x="480" y="306" width="20" height="2" fill="#e64980" fill-opacity="0.41"/>
  <rect x="480" y="308" width="20" height="2" fill="#e64980" fill-opacity="0.36"/>
  <rect x="480" y="310" width="20" height="2" fill="#e64980" fill-opacity="0.32"/>
  <rect x="480" y="16" width="20" height="296" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="151" y1="130" x2="480" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="151" y1="210" x2="480" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="480" cy="66" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="105" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$S_1$</span></div></foreignObject>
  <foreignObject x="105" y="195.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$S_2$</span></div></foreignObject>
  <foreignObject x="510" y="51.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="510" y="155.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{bright}$</div></foreignObject>
  <foreignObject x="510" y="209.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{dark}$</div></foreignObject>
  <foreignObject x="135" y="323.5" width="330" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at point P}\ \ s_2 - s_1 = \lambda$</div></foreignObject>
</svg>

### Grating
A **diffraction grating** is a plate or film with a large number of evenly spaced narrow slits or lines. The distance between adjacent slits is the **grating spacing** $d$. School gratings usually have $100$, $300$ or $600$ lines per millimetre. The bright maxima of a grating form in the same directions as the bright fringes of a double slit with the same slit spacing, that is in directions where the path difference of adjacent slits is a whole number of wavelengths. Then the wave from every slit arrives in the same phase. Even a little to the side, the waves from different slits are in different phases and cancel each other almost completely. That is why the maxima of a grating are narrow and bright, and almost dark between them. The light of a laser draws sharp dots on the screen, and the positions of the dots can be measured accurately.

<svg data-fig="pattern" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the intensity of light on the screen relative to the largest value as a function of the path difference of neighbouring slits, with the path difference expressed in wavelengths from zero to 3.2. The dashed curve of the double slit varies smoothly: peaks at 0, 1, 2 and 3 and zeros halfway between them. The curve of the eight-slit grating has narrow, tall peaks at the same places, and between them the intensity is almost zero. The effect of the width of the slits is left out." style="max-width:100%;font-size:24px">
  <line x1="156" y1="290" x2="156" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="216" y1="290" x2="216" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="290" x2="276" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="290" x2="336" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="396" y1="290" x2="396" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="456" y1="290" x2="456" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="249.5" x2="480" y2="249.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="209" x2="480" y2="209" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="168.5" x2="480" y2="168.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="128" x2="480" y2="128" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="494" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,290 L493,296 L493,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="156" y1="290" x2="156" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="216" y1="290" x2="216" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="206" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="276" y1="290" x2="276" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="336" y1="290" x2="336" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="326" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="396" y1="290" x2="396" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="456" y1="290" x2="456" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="446" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="249.5" x2="96" y2="249.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="209" x2="96" y2="209" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="194.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.5$</div></foreignObject>
  <line x1="89" y1="168.5" x2="96" y2="168.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="128" x2="96" y2="128" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="113.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.0$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="275.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{\Delta s}{\lambda}$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{intensity}$</div></foreignObject>
  <polyline points="96,128 97,128.5 98.5,129 99.5,129.5 101,131 102,132 103,134 104.5,136 105.5,138 107,141 108,143.5 109,147 110.5,150 111.5,153.5 113,157.5 114,161.5 115,166 116.5,170 117.5,174.5 119,179.5 120,184 121,189 122.5,194 123.5,199 125,204 126,209 127,214 128.5,219.5 129.5,224.5 131,229 132,234 133,239 134.5,243.5 135.5,248 137,252.5 138,256.5 139,260.5 140.5,264.5 141.5,268 143,271.5 144,274.5 145,277.5 146.5,280 147.5,282.5 149,284.5 150,286 151,287.5 152.5,288.5 153.5,289.5 155,290 156,290 157,290 158.5,289.5 159.5,288.5 161,287.5 162,286 163,284.5 164.5,282.5 165.5,280 167,277.5 168,274.5 169,271.5 170.5,268 171.5,264.5 173,260.5 174,256.5 175,252.5 176.5,248 177.5,243.5 179,239 180,234 181,229 182.5,224.5 183.5,219.5 185,214 186,209 187,204 188.5,199 189.5,194 191,189 192,184 193,179.5 194.5,174.5 195.5,170 197,166 198,161.5 199,157.5 200.5,153.5 201.5,150 203,147 204,143.5 205,141 206.5,138 207.5,136 209,134 210,132 211,131 212.5,129.5 213.5,129 215,128.5 216,128 217,128.5 218.5,129 219.5,129.5 221,131 222,132 223,134 224.5,136 225.5,138 227,141 228,143.5 229,147 230.5,150 231.5,153.5 233,157.5 234,161.5 235,166 236.5,170 237.5,174.5 239,179.5 240,184 241,189 242.5,194 243.5,199 245,204 246,209 247,214 248.5,219.5 249.5,224.5 251,229 252,234 253,239 254.5,243.5 255.5,248 257,252.5 258,256.5 259,260.5 260.5,264.5 261.5,268 263,271.5 264,274.5 265,277.5 266.5,280 267.5,282.5 269,284.5 270,286 271,287.5 272.5,288.5 273.5,289.5 275,290 276,290 277,290 278.5,289.5 279.5,288.5 281,287.5 282,286 283,284.5 284.5,282.5 285.5,280 287,277.5 288,274.5 289,271.5 290.5,268 291.5,264.5 293,260.5 294,256.5 295,252.5 296.5,248 297.5,243.5 299,239 300,234 301,229 302.5,224.5 303.5,219.5 305,214 306,209 307,204 308.5,199 309.5,194 311,189 312,184 313,179.5 314.5,174.5 315.5,170 317,166 318,161.5 319,157.5 320.5,153.5 321.5,150 323,147 324,143.5 325,141 326.5,138 327.5,136 329,134 330,132 331,131 332.5,129.5 333.5,129 335,128.5 336,128 337,128.5 338.5,129 339.5,129.5 341,131 342,132 343,134 344.5,136 345.5,138 347,141 348,143.5 349,147 350.5,150 351.5,153.5 353,157.5 354,161.5 355,166 356.5,170 357.5,174.5 359,179.5 360,184 361,189 362.5,194 363.5,199 365,204 366,209 367,214 368.5,219.5 369.5,224.5 371,229 372,234 373,239 374.5,243.5 375.5,248 377,252.5 378,256.5 379,260.5 380.5,264.5 381.5,268 383,271.5 384,274.5 385,277.5 386.5,280 387.5,282.5 389,284.5 390,286 391,287.5 392.5,288.5 393.5,289.5 395,290 396,290 397,290 398.5,289.5 399.5,288.5 401,287.5 402,286 403,284.5 404.5,282.5 405.5,280 407,277.5 408,274.5 409,271.5 410.5,268 411.5,264.5 413,260.5 414,256.5 415,252.5 416.5,248 417.5,243.5 419,239 420,234 421,229 422.5,224.5 423.5,219.5 425,214 426,209 427,204 428.5,199 429.5,194 431,189 432,184 433,179.5 434.5,174.5 435.5,170 437,166 438,161.5 439,157.5 440.5,153.5 441.5,150 443,147 444,143.5 445,141 446.5,138 447.5,136 449,134 450,132 451,131 452.5,129.5 453.5,129 455,128.5 456,128 457,128.5 458.5,129 459.5,129.5 461,131 462,132 463,134 464.5,136 465.5,138 467,141 468,143.5 469,147 470.5,150 471.5,153.5 473,157.5 474,161.5 475,166 476.5,170 477.5,174.5 479,179.5 480,184" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 6"/>
  <polyline points="96,128 96.5,128.5 96.5,129 97,130 97,131.5 97.5,133.5 98,135.5 98,138 98.5,141 98.5,144.5 99,148 99.5,152 99.5,156.5 100,160.5 100,165.5 100.5,170.5 101,175.5 101,180.5 101.5,186 101.5,191 102,196.5 102.5,202 102.5,207.5 103,213 103,218.5 103.5,223.5 104,229 104,234 104.5,238.5 104.5,243.5 105,248 105.5,252.5 105.5,256.5 106,260.5 106,264 106.5,267.5 107,270.5 107,273.5 107.5,276.5 107.5,278.5 108,281 108.5,283 108.5,284.5 109,286 109,287 109.5,288 110,288.5 110,289.5 110.5,289.5 110.5,290 111,290 111.5,290 111.5,289.5 112,289.5 112,289 112.5,288.5 113,288 113,287.5 113.5,287 113.5,286.5 114,286 114.5,285 114.5,284.5 115,284 115,283.5 115.5,283 116,282.5 116,282.5 116.5,282 116.5,282 117,281.5 117.5,281.5 117.5,281.5 118,281.5 118,281.5 118.5,282 119,282 119,282.5 119.5,282.5 119.5,283 120,283.5 120.5,284 120.5,284.5 121,284.5 121,285 121.5,285.5 122,286 122,286.5 122.5,287 122.5,287.5 123,288 123.5,288.5 123.5,288.5 124,289 124,289 124.5,289.5 125,289.5 125,290 125.5,290 125.5,290 126,290 126.5,290 126.5,290 127,290 127,289.5 127.5,289.5 128,289.5 128,289 128.5,289 128.5,288.5 129,288.5 129.5,288 129.5,288 130,288 130,287.5 130.5,287.5 131,287 131,287 131.5,287 131.5,286.5 132,286.5 132.5,286.5 132.5,286.5 133,286.5 133,286.5 133.5,286.5 134,286.5 134,286.5 134.5,286.5 134.5,286.5 135,287 135.5,287 135.5,287 136,287.5 136,287.5 136.5,288 137,288 137,288.5 137.5,288.5 137.5,288.5 138,289 138.5,289 138.5,289.5 139,289.5 139,289.5 139.5,289.5 140,290 140,290 140.5,290 140.5,290 141,290 141.5,290 141.5,290 142,290 142,290 142.5,289.5 143,289.5 143,289.5 143.5,289.5 143.5,289 144,289 144.5,289 144.5,288.5 145,288.5 145,288.5 145.5,288 146,288 146,288 146.5,288 146.5,287.5 147,287.5 147.5,287.5 147.5,287.5 148,287.5 148,287.5 148.5,287.5 149,287.5 149,287.5 149.5,287.5 149.5,287.5 150,287.5 150.5,288 150.5,288 151,288 151,288 151.5,288.5 152,288.5 152,288.5 152.5,289 152.5,289 153,289 153.5,289.5 153.5,289.5 154,289.5 154,289.5 154.5,290 155,290 155,290 155.5,290 155.5,290 156,290 156.5,290 156.5,290 157,290 157,290 157.5,290 158,289.5 158,289.5 158.5,289.5 158.5,289.5 159,289 159.5,289 159.5,289 160,288.5 160,288.5 160.5,288.5 161,288 161,288 161.5,288 161.5,288 162,287.5 162.5,287.5 162.5,287.5 163,287.5 163,287.5 163.5,287.5 164,287.5 164,287.5 164.5,287.5 164.5,287.5 165,287.5 165.5,287.5 165.5,288 166,288 166,288 166.5,288 167,288.5 167,288.5 167.5,288.5 167.5,289 168,289 168.5,289 168.5,289.5 169,289.5 169,289.5 169.5,289.5 170,290 170,290 170.5,290 170.5,290 171,290 171.5,290 171.5,290 172,290 172,290 172.5,289.5 173,289.5 173,289.5 173.5,289.5 173.5,289 174,289 174.5,288.5 174.5,288.5 175,288.5 175,288 175.5,288 176,287.5 176,287.5 176.5,287 176.5,287 177,287 177.5,286.5 177.5,286.5 178,286.5 178,286.5 178.5,286.5 179,286.5 179,286.5 179.5,286.5 179.5,286.5 180,286.5 180.5,286.5 180.5,287 181,287 181,287 181.5,287.5 182,287.5 182,288 182.5,288 182.5,288 183,288.5 183.5,288.5 183.5,289 184,289 184,289.5 184.5,289.5 185,289.5 185,290 185.5,290 185.5,290 186,290 186.5,290 186.5,290 187,290 187,289.5 187.5,289.5 188,289 188,289 188.5,288.5 188.5,288.5 189,288 189.5,287.5 189.5,287 190,286.5 190,286 190.5,285.5 191,285 191,284.5 191.5,284.5 191.5,284 192,283.5 192.5,283 192.5,282.5 193,282.5 193,282 193.5,282 194,281.5 194,281.5 194.5,281.5 194.5,281.5 195,281.5 195.5,282 195.5,282 196,282.5 196,282.5 196.5,283 197,283.5 197,284 197.5,284.5 197.5,285 198,286 198.5,286.5 198.5,287 199,287.5 199,288 199.5,288.5 200,289 200,289.5 200.5,289.5 200.5,290 201,290 201.5,290 201.5,289.5 202,289.5 202,288.5 202.5,288 203,287 203,286 203.5,284.5 203.5,283 204,281 204.5,278.5 204.5,276.5 205,273.5 205,270.5 205.5,267.5 206,264 206,260.5 206.5,256.5 206.5,252.5 207,248 207.5,243.5 207.5,238.5 208,234 208,229 208.5,223.5 209,218.5 209,213 209.5,207.5 209.5,202 210,196.5 210.5,191 210.5,186 211,180.5 211,175.5 211.5,170.5 212,165.5 212,160.5 212.5,156.5 212.5,152 213,148 213.5,144.5 213.5,141 214,138 214,135.5 214.5,133.5 215,131.5 215,130 215.5,129 215.5,128.5 216,128 216.5,128.5 216.5,129 217,130 217,131.5 217.5,133.5 218,135.5 218,138 218.5,141 218.5,144.5 219,148 219.5,152 219.5,156.5 220,160.5 220,165.5 220.5,170.5 221,175.5 221,180.5 221.5,186 221.5,191 222,196.5 222.5,202 222.5,207.5 223,213 223,218.5 223.5,223.5 224,229 224,234 224.5,238.5 224.5,243.5 225,248 225.5,252.5 225.5,256.5 226,260.5 226,264 226.5,267.5 227,270.5 227,273.5 227.5,276.5 227.5,278.5 228,281 228.5,283 228.5,284.5 229,286 229,287 229.5,288 230,288.5 230,289.5 230.5,289.5 230.5,290 231,290 231.5,290 231.5,289.5 232,289.5 232,289 232.5,288.5 233,288 233,287.5 233.5,287 233.5,286.5 234,286 234.5,285 234.5,284.5 235,284 235,283.5 235.5,283 236,282.5 236,282.5 236.5,282 236.5,282 237,281.5 237.5,281.5 237.5,281.5 238,281.5 238,281.5 238.5,282 239,282 239,282.5 239.5,282.5 239.5,283 240,283.5 240.5,284 240.5,284.5 241,284.5 241,285 241.5,285.5 242,286 242,286.5 242.5,287 242.5,287.5 243,288 243.5,288.5 243.5,288.5 244,289 244,289 244.5,289.5 245,289.5 245,290 245.5,290 245.5,290 246,290 246.5,290 246.5,290 247,290 247,289.5 247.5,289.5 248,289.5 248,289 248.5,289 248.5,288.5 249,288.5 249.5,288 249.5,288 250,288 250,287.5 250.5,287.5 251,287 251,287 251.5,287 251.5,286.5 252,286.5 252.5,286.5 252.5,286.5 253,286.5 253,286.5 253.5,286.5 254,286.5 254,286.5 254.5,286.5 254.5,286.5 255,287 255.5,287 255.5,287 256,287.5 256,287.5 256.5,288 257,288 257,288.5 257.5,288.5 257.5,288.5 258,289 258.5,289 258.5,289.5 259,289.5 259,289.5 259.5,289.5 260,290 260,290 260.5,290 260.5,290 261,290 261.5,290 261.5,290 262,290 262,290 262.5,289.5 263,289.5 263,289.5 263.5,289.5 263.5,289 264,289 264.5,289 264.5,288.5 265,288.5 265,288.5 265.5,288 266,288 266,288 266.5,288 266.5,287.5 267,287.5 267.5,287.5 267.5,287.5 268,287.5 268,287.5 268.5,287.5 269,287.5 269,287.5 269.5,287.5 269.5,287.5 270,287.5 270.5,288 270.5,288 271,288 271,288 271.5,288.5 272,288.5 272,288.5 272.5,289 272.5,289 273,289 273.5,289.5 273.5,289.5 274,289.5 274,289.5 274.5,290 275,290 275,290 275.5,290 275.5,290 276,290 276.5,290 276.5,290 277,290 277,290 277.5,290 278,289.5 278,289.5 278.5,289.5 278.5,289.5 279,289 279.5,289 279.5,289 280,288.5 280,288.5 280.5,288.5 281,288 281,288 281.5,288 281.5,288 282,287.5 282.5,287.5 282.5,287.5 283,287.5 283,287.5 283.5,287.5 284,287.5 284,287.5 284.5,287.5 284.5,287.5 285,287.5 285.5,287.5 285.5,288 286,288 286,288 286.5,288 287,288.5 287,288.5 287.5,288.5 287.5,289 288,289 288.5,289 288.5,289.5 289,289.5 289,289.5 289.5,289.5 290,290 290,290 290.5,290 290.5,290 291,290 291.5,290 291.5,290 292,290 292,290 292.5,289.5 293,289.5 293,289.5 293.5,289.5 293.5,289 294,289 294.5,288.5 294.5,288.5 295,288.5 295,288 295.5,288 296,287.5 296,287.5 296.5,287 296.5,287 297,287 297.5,286.5 297.5,286.5 298,286.5 298,286.5 298.5,286.5 299,286.5 299,286.5 299.5,286.5 299.5,286.5 300,286.5 300.5,286.5 300.5,287 301,287 301,287 301.5,287.5 302,287.5 302,288 302.5,288 302.5,288 303,288.5 303.5,288.5 303.5,289 304,289 304,289.5 304.5,289.5 305,289.5 305,290 305.5,290 305.5,290 306,290 306.5,290 306.5,290 307,290 307,289.5 307.5,289.5 308,289 308,289 308.5,288.5 308.5,288.5 309,288 309.5,287.5 309.5,287 310,286.5 310,286 310.5,285.5 311,285 311,284.5 311.5,284.5 311.5,284 312,283.5 312.5,283 312.5,282.5 313,282.5 313,282 313.5,282 314,281.5 314,281.5 314.5,281.5 314.5,281.5 315,281.5 315.5,282 315.5,282 316,282.5 316,282.5 316.5,283 317,283.5 317,284 317.5,284.5 317.5,285 318,286 318.5,286.5 318.5,287 319,287.5 319,288 319.5,288.5 320,289 320,289.5 320.5,289.5 320.5,290 321,290 321.5,290 321.5,289.5 322,289.5 322,288.5 322.5,288 323,287 323,286 323.5,284.5 323.5,283 324,281 324.5,278.5 324.5,276.5 325,273.5 325,270.5 325.5,267.5 326,264 326,260.5 326.5,256.5 326.5,252.5 327,248 327.5,243.5 327.5,238.5 328,234 328,229 328.5,223.5 329,218.5 329,213 329.5,207.5 329.5,202 330,196.5 330.5,191 330.5,186 331,180.5 331,175.5 331.5,170.5 332,165.5 332,160.5 332.5,156.5 332.5,152 333,148 333.5,144.5 333.5,141 334,138 334,135.5 334.5,133.5 335,131.5 335,130 335.5,129 335.5,128.5 336,128 336.5,128.5 336.5,129 337,130 337,131.5 337.5,133.5 338,135.5 338,138 338.5,141 338.5,144.5 339,148 339.5,152 339.5,156.5 340,160.5 340,165.5 340.5,170.5 341,175.5 341,180.5 341.5,186 341.5,191 342,196.5 342.5,202 342.5,207.5 343,213 343,218.5 343.5,223.5 344,229 344,234 344.5,238.5 344.5,243.5 345,248 345.5,252.5 345.5,256.5 346,260.5 346,264 346.5,267.5 347,270.5 347,273.5 347.5,276.5 347.5,278.5 348,281 348.5,283 348.5,284.5 349,286 349,287 349.5,288 350,288.5 350,289.5 350.5,289.5 350.5,290 351,290 351.5,290 351.5,289.5 352,289.5 352,289 352.5,288.5 353,288 353,287.5 353.5,287 353.5,286.5 354,286 354.5,285 354.5,284.5 355,284 355,283.5 355.5,283 356,282.5 356,282.5 356.5,282 356.5,282 357,281.5 357.5,281.5 357.5,281.5 358,281.5 358,281.5 358.5,282 359,282 359,282.5 359.5,282.5 359.5,283 360,283.5 360.5,284 360.5,284.5 361,284.5 361,285 361.5,285.5 362,286 362,286.5 362.5,287 362.5,287.5 363,288 363.5,288.5 363.5,288.5 364,289 364,289 364.5,289.5 365,289.5 365,290 365.5,290 365.5,290 366,290 366.5,290 366.5,290 367,290 367,289.5 367.5,289.5 368,289.5 368,289 368.5,289 368.5,288.5 369,288.5 369.5,288 369.5,288 370,288 370,287.5 370.5,287.5 371,287 371,287 371.5,287 371.5,286.5 372,286.5 372.5,286.5 372.5,286.5 373,286.5 373,286.5 373.5,286.5 374,286.5 374,286.5 374.5,286.5 374.5,286.5 375,287 375.5,287 375.5,287 376,287.5 376,287.5 376.5,288 377,288 377,288.5 377.5,288.5 377.5,288.5 378,289 378.5,289 378.5,289.5 379,289.5 379,289.5 379.5,289.5 380,290 380,290 380.5,290 380.5,290 381,290 381.5,290 381.5,290 382,290 382,290 382.5,289.5 383,289.5 383,289.5 383.5,289.5 383.5,289 384,289 384.5,289 384.5,288.5 385,288.5 385,288.5 385.5,288 386,288 386,288 386.5,288 386.5,287.5 387,287.5 387.5,287.5 387.5,287.5 388,287.5 388,287.5 388.5,287.5 389,287.5 389,287.5 389.5,287.5 389.5,287.5 390,287.5 390.5,288 390.5,288 391,288 391,288 391.5,288.5 392,288.5 392,288.5 392.5,289 392.5,289 393,289 393.5,289.5 393.5,289.5 394,289.5 394,289.5 394.5,290 395,290 395,290 395.5,290 395.5,290 396,290 396.5,290 396.5,290 397,290 397,290 397.5,290 398,289.5 398,289.5 398.5,289.5 398.5,289.5 399,289 399.5,289 399.5,289 400,288.5 400,288.5 400.5,288.5 401,288 401,288 401.5,288 401.5,288 402,287.5 402.5,287.5 402.5,287.5 403,287.5 403,287.5 403.5,287.5 404,287.5 404,287.5 404.5,287.5 404.5,287.5 405,287.5 405.5,287.5 405.5,288 406,288 406,288 406.5,288 407,288.5 407,288.5 407.5,288.5 407.5,289 408,289 408.5,289 408.5,289.5 409,289.5 409,289.5 409.5,289.5 410,290 410,290 410.5,290 410.5,290 411,290 411.5,290 411.5,290 412,290 412,290 412.5,289.5 413,289.5 413,289.5 413.5,289.5 413.5,289 414,289 414.5,288.5 414.5,288.5 415,288.5 415,288 415.5,288 416,287.5 416,287.5 416.5,287 416.5,287 417,287 417.5,286.5 417.5,286.5 418,286.5 418,286.5 418.5,286.5 419,286.5 419,286.5 419.5,286.5 419.5,286.5 420,286.5 420.5,286.5 420.5,287 421,287 421,287 421.5,287.5 422,287.5 422,288 422.5,288 422.5,288 423,288.5 423.5,288.5 423.5,289 424,289 424,289.5 424.5,289.5 425,289.5 425,290 425.5,290 425.5,290 426,290 426.5,290 426.5,290 427,290 427,289.5 427.5,289.5 428,289 428,289 428.5,288.5 428.5,288.5 429,288 429.5,287.5 429.5,287 430,286.5 430,286 430.5,285.5 431,285 431,284.5 431.5,284.5 431.5,284 432,283.5 432.5,283 432.5,282.5 433,282.5 433,282 433.5,282 434,281.5 434,281.5 434.5,281.5 434.5,281.5 435,281.5 435.5,282 435.5,282 436,282.5 436,282.5 436.5,283 437,283.5 437,284 437.5,284.5 437.5,285 438,286 438.5,286.5 438.5,287 439,287.5 439,288 439.5,288.5 440,289 440,289.5 440.5,289.5 440.5,290 441,290 441.5,290 441.5,289.5 442,289.5 442,288.5 442.5,288 443,287 443,286 443.5,284.5 443.5,283 444,281 444.5,278.5 444.5,276.5 445,273.5 445,270.5 445.5,267.5 446,264 446,260.5 446.5,256.5 446.5,252.5 447,248 447.5,243.5 447.5,238.5 448,234 448,229 448.5,223.5 449,218.5 449,213 449.5,207.5 449.5,202 450,196.5 450.5,191 450.5,186 451,180.5 451,175.5 451.5,170.5 452,165.5 452,160.5 452.5,156.5 452.5,152 453,148 453.5,144.5 453.5,141 454,138 454,135.5 454.5,133.5 455,131.5 455,130 455.5,129 455.5,128.5 456,128 456.5,128.5 456.5,129 457,130 457,131.5 457.5,133.5 458,135.5 458,138 458.5,141 458.5,144.5 459,148 459.5,152 459.5,156.5 460,160.5 460,165.5 460.5,170.5 461,175.5 461,180.5 461.5,186 461.5,191 462,196.5 462.5,202 462.5,207.5 463,213 463,218.5 463.5,223.5 464,229 464,234 464.5,238.5 464.5,243.5 465,248 465.5,252.5 465.5,256.5 466,260.5 466,264 466.5,267.5 467,270.5 467,273.5 467.5,276.5 467.5,278.5 468,281 468.5,283 468.5,284.5 469,286 469,287 469.5,288 470,288.5 470,289.5 470.5,289.5 470.5,290 471,290 471.5,290 471.5,289.5 472,289.5 472,289 472.5,288.5 473,288 473,287.5 473.5,287 473.5,286.5 474,286 474.5,285 474.5,284.5 475,284 475,283.5 475.5,283 476,282.5 476,282.5 476.5,282 476.5,282 477,281.5 477.5,281.5 477.5,281.5 478,281.5 478,281.5 478.5,282 479,282 479,282.5 479.5,282.5 479.5,283 480,283.5" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="108" y1="89.5" x2="148" y2="89.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <foreignObject x="158" y="75" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{double slit}$</span></div></foreignObject>
  <line x1="318" y1="89.5" x2="358" y2="89.5" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="368" y="75" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{grating, 8 slits}$</span></div></foreignObject>
</svg>

### White light in a grating
The longer the wavelength, the larger the path difference and therefore the larger the angle of deviation required by a maximum. All the colours of white light go in the same direction into the central maximum, so the central maximum is white. On both sides of it the light is spread into a spectrum: violet is deviated least and red most. In a prism the order is the opposite, because the refractive index is largest for violet light (chapter *Dispersion: the prism and the rainbow*). Farther from the central maximum the spectra of different orders partly overlap. In spectrometers the wavelengths of light are measured with a grating.

<svg data-fig="white" viewBox="0 0 600 350" role="img" aria-label="Diagram with angles and screen distances to scale for a grating with 300 lines per millimetre. At the top, the situation seen from above: white light arrives from the left at the grating. The white central maximum, k = 0, continues straight through. On both sides of it the first-order light is spread into colours: violet, 400 nm, is deviated least, by 6.9 degrees, and red, 700 nm, most, by 12.1 degrees. At the bottom, the screen seen from the front at a distance of one metre from the grating: a white spot in the middle and on each side the first- and second-order spectra, with violet at the inner edge and red at the outer edge. The third-order spectrum already begins inside the second-order spectrum, so they partly overlap." style="max-width:100%;font-size:24px">
  <defs><clipPath id="fy713-white-c"><rect x="40" y="248" width="520" height="40"/></clipPath></defs>
  <line x1="24" y1="120" x2="150" y2="120" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <line x1="24" y1="120" x2="150" y2="120" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <line x1="150" y1="120" x2="490" y2="79" stroke="#7048e8" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="161" stroke="#7048e8" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="73.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="166.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="68.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="171.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="63" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="177" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="58" stroke="#e8590c" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="182" stroke="#e8590c" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="52.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="187.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="47" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="193" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="150" y1="120" x2="490" y2="120" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <line x1="150" y1="120" x2="490" y2="120" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <rect x="146" y="68" width="8" height="104" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="146" y1="74" x2="154" y2="74" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="82.5" x2="154" y2="82.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="91" x2="154" y2="91" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="99" x2="154" y2="99" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="107.5" x2="154" y2="107.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="116" x2="154" y2="116" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="124.5" x2="154" y2="124.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="133" x2="154" y2="133" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="141" x2="154" y2="141" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="149.5" x2="154" y2="149.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="158" x2="154" y2="158" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="146" y1="166.5" x2="154" y2="166.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <rect x="490" y="20" width="10" height="200" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="24" y="25.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{white light}$</div></foreignObject>
  <foreignObject x="164" y="181.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{grating}$</div></foreignObject>
  <foreignObject x="508" y="32.5" width="82" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$700\,\text{nm}$</div></foreignObject>
  <foreignObject x="508" y="64.5" width="82" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$400\,\text{nm}$</div></foreignObject>
  <foreignObject x="508" y="105.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k = 0$</div></foreignObject>
  <rect x="40" y="248" width="520" height="40" rx="3" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <g clip-path="url(#fy713-white-c)">
  <rect x="231.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="231" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="230.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="229.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="229" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="228" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="227.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="227" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="226" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="225.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="225" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="224" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="223.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="223" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="222" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="221.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="220.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="220" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="219.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="218.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="218" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="217.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="216.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="216" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="215.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="214.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="214" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="213" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="212.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="212" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="211" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="210.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="210" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="209" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="208.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="207.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="207" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="206.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="205.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="205" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="204" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="203.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="203" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="202" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="201.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="201" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="200" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="199.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="198.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="198" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="197.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="196.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="196" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="195" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="194.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="194" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="193" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="192.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="191.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="191" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="190.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="189.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="189" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="188" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="187.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="187" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="186" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="185.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="184.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="184" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="183" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="182.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="182" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="181" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="180.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="179.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="365.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="366" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="366.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="367.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="368" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="369" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="369.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="370" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="371" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="371.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="372" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="373" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="373.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="374" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="375" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="375.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="376.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="377" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="377.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="378.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="379" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="379.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="380.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="381" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="381.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="382.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="383" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="384" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="384.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="385" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="386" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="386.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="387" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="388" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="388.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="389.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="390" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="390.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="391.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="392" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="393" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="393.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="394" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="395" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="395.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="396" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="397" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="397.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="398.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="399" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="399.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="400.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="401" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="402" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="402.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="403" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="404" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="404.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="405.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="406" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="406.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="407.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="408" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="409" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="409.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="410" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="411" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="411.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="412.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="413" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="414" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="414.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="415" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="416" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="416.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="417.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="161.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="160.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="159" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="157.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="156" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="154.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="153" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="151.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="150" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="148.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="147" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="145.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="144" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="142.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="141" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="139.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="138" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="136.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="135" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="133.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="132" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="130.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="129" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="127.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="126" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="124.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="123" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="121.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="120" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="118.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="117" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="115.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="113.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="112" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="110.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="109" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="107.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="106" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="104.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="102.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="101" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="99.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="98" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="96.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="95" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="93" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="91.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="90" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="88.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="86.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="85" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="83.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="82" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="80" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="78.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="77" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="75" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="73.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="72" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="70" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="68.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="66.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="65" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="63.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="61.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="60" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="58" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="56.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="55" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="53" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="51.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="49.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="48" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="46" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="44.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="42.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="435.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="436.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="438" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="439.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="441" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="442.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="444" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="445.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="447" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="448.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="450" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="451.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="453" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="454.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="456" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="457.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="459" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="460.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="462" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="463.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="465" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="466.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="468" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="469.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="471" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="472.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="474" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="475.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="477" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="478.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="480" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="481.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="483.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="485" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="486.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="488" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="489.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="491" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="492.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="494.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="496" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="497.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="499" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="500.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="502" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="504" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="505.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="507" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="508.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="510.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="512" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="513.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="515" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="517" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="518.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="520" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="522" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="523.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="525" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="527" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="528.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="530.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="532" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="533.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="535.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="537" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="539" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="540.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="542" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="544" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="545.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="547.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="549" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="551" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="552.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="554.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="85" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="82.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="80" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="77.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="75" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="72.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="70" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="67.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="65" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="62.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="60" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="57.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="55" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="52" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="49.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="47" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="44.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="41.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="39" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="36" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="33.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="31" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="28" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="25.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="22.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="19.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="17" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="14" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="11.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="8.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="5.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="2.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-0.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-3" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-6" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-9" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-12" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-15" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-18" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-21" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-24.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-27.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-30.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="-33.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="-37" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="-40" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="-43.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="-46.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="-50" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="-53" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="-56.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-60" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-63" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-66.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-70" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-73.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-77" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-80.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-84" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-87.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="-91.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-95" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-98.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-102.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-106" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-110" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-114" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-117.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-121.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-125.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-129.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-133.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-137.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-142" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-146" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="-150.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="512" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="514.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="517" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="519.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="522" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="524.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="527" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="529.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="532" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="534.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="537" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="539.5" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="542" y="252" width="3.5" height="32" fill="#7048e8" fill-opacity="0.75"/>
  <rect x="545" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="547.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="550" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="552.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="555.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="558" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="561" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="563.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="566" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="569" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="571.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="574.5" y="252" width="3.5" height="32" fill="#1971c2" fill-opacity="0.75"/>
  <rect x="577.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="580" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="583" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="585.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="588.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="591.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="594.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="597.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="600" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="603" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="606" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="609" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="612" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="615" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="618" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="621.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="624.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="627.5" y="252" width="3.5" height="32" fill="#2b8a3e" fill-opacity="0.75"/>
  <rect x="630.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="634" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="637" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="640.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="643.5" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="647" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="650" y="252" width="3.5" height="32" fill="#f59f00" fill-opacity="0.75"/>
  <rect x="653.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="657" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="660" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="663.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="667" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="670.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="674" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="677.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="681" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="684.5" y="252" width="3.5" height="32" fill="#e8590c" fill-opacity="0.75"/>
  <rect x="688.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="692" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="695.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="699.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="703" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="707" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="711" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="714.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="718.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="722.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="726.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="730.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="734.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="739" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="743" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  <rect x="747.5" y="252" width="3.5" height="32" fill="#c92a2a" fill-opacity="0.75"/>
  </g>
  <circle cx="300" cy="268" r="9" fill="#ffffff"/>
  <rect x="40" y="248" width="520" height="40" rx="3" fill="none" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="277.5" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$k = 0$</div></foreignObject>
  <foreignObject x="370.5" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$k = 1$</div></foreignObject>
  <foreignObject x="449" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$k = 2$</div></foreignObject>
  <foreignObject x="515.5" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$k = 3$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/laser-diffraction.webp" alt="A green pattern in the dark: on the right a grid of bright green spots on a pale surface, and on the left a fainter grid of spots."><figcaption>A diffraction pattern of green laser light. The light has passed through a fine structure that repeats in two directions, so the bright spots form a grid. Each spot is a direction in which the waves reinforce each other.</figcaption></figure>

### A CD as a reflection grating
The data track of a CD winds over the surface of the disc as a dense spiral, and the distance between adjacent turns of the track is $1.6\,\mu\text{m}$ (standard IEC 60908, 1999). On a DVD the distance is $0.74\,\mu\text{m}$ (standard ECMA-267, 2001). Light reflected from the surface of the disc behaves in the same way as light passing through a grating: the waves reflected from the evenly spaced tracks interfere, and each wavelength is reinforced in its own direction. That is why rainbow colours are seen on the surface of the disc, changing with the viewing angle. Such a grating is called a reflection grating.

## Formula: Grating equation
When light arrives perpendicular to the grating, the path difference of rays leaving adjacent slits at angle $\theta$ comes from the right-angled triangle in the figure: $\Delta s = d\sin\theta$. The angle $\theta$ is measured from the direction of the incident light, that is from the direction of the central maximum. A maximum forms when the path difference is a whole number of wavelengths:
```latex
d \sin\theta = k\lambda
```
where $d$ is the grating spacing ($\text{m}$), $\theta$ the direction of the maximum relative to the direction of the incident light, $k = 0, 1, 2, \ldots$ the order of the maximum and $\lambda$ the wavelength of the light ($\text{m}$). The order $k = 0$ is the central maximum. On both sides of it there are similar maxima, so the orders on the other side are often written as negative.

<svg data-fig="geometry" viewBox="0 0 600 360" role="img" aria-label="Diagram, not to scale: two adjacent slits of a grating magnified. The distance between the slits is the grating spacing d. Light arrives from the left perpendicular to the grating. A parallel ray leaves each slit at angle theta to the original direction, which is shown by a horizontal dashed line. A perpendicular segment drawn from the lower slit to the ray of the upper slit separates off the extra distance of the lower ray, the path difference delta s. In the right-angled triangle whose hypotenuse is d and whose angle is theta, the path difference is d times sine theta." style="max-width:100%;font-size:24px">
  <line x1="36" y1="40" x2="156" y2="40" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <path d="M168,40 L155,46 L155,34 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="36" y1="120" x2="156" y2="120" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <path d="M168,120 L155,126 L155,114 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="36" y1="200" x2="156" y2="200" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <path d="M168,200 L155,206 L155,194 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="36" y1="280" x2="156" y2="280" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <path d="M168,280 L155,286 L155,274 Z" fill="#e64980" stroke-linejoin="round"/>
  <rect x="185" y="24" width="10" height="39" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="185" y="77" width="10" height="126" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="185" y="217" width="10" height="99" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="190" y1="70" x2="372.5" y2="151.5" stroke="#e64980" stroke-width="3" stroke-linecap="round"/>
  <path d="M287,113 L272.5,113.5 L277.5,102.5 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="190" y1="210" x2="372.5" y2="291.5" stroke="#e64980" stroke-width="3" stroke-linecap="round"/>
  <path d="M287,253 L272.5,253.5 L277.5,242.5 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="190" y1="210" x2="430" y2="210" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M252,210 A62,62 0 0,1 246.5,235" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="261" y="210.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <line x1="190" y1="210" x2="242" y2="93" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M233,89 L237,80 L246,84" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M190,170 A40,40 0 0,1 206.5,173.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="190" y="133.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <line x1="196.5" y1="55.5" x2="248.5" y2="78.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="193.5" y1="62.5" x2="196.5" y2="55.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="245.5" y1="86" x2="248.5" y2="78.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="262.5" y="38" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta s = d\sin\theta$</div></foreignObject>
  <line x1="174" y1="140" x2="174" y2="79" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M174,70 L178.5,80 L169.5,80 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="174" y1="140" x2="174" y2="201" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M174,210 L169.5,200 L178.5,200 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="138" y="125.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$d$</span></div></foreignObject>
  <foreignObject x="142.5" y="323.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{grating}$</div></foreignObject>
  <foreignObject x="380" y="315.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{towards the screen}$</div></foreignObject>
</svg>

### Grating spacing from the line density
The manufacturer of a grating usually states how many lines the grating has per millimetre. If there are $N$ lines per millimetre, the distance between adjacent lines is
```latex
d = \frac{1\,\text{mm}}{N}
```
For example, when there are $300$ lines per millimetre, $d = 1\,\text{mm} : 300 = 1 \cdot 10^{-3}\,\text{m} : 300 = 3.33 \cdot 10^{-6}\,\text{m}$, that is $3.33\,\mu\text{m}$. The denser the grating, the smaller $d$ is and the larger the angle at which the maximum of the same order lies.

### How many maxima form
The value of a sine is at most $1$, so the order must satisfy the condition $k\lambda < d$. At the limit $k\lambda = d$ the light would travel along the surface of the grating and would not hit the screen. For example, when the grating has $600$ lines per millimetre and the wavelength of the light is $650\,\text{nm}$, $d : \lambda = 1.667\,\mu\text{m} : 0.650\,\mu\text{m} = 2.56$. Maxima form in the orders $k = 0, \pm 1, \pm 2$, that is five of them.

### The angle from the screen
The angle is usually not measured directly; instead, distances are measured on the screen. When the screen is perpendicular to the beam of the laser at distance $L$ from the grating and a maximum is at distance $x$ from the central maximum, the right-angled triangle in the figure gives
```latex
\tan\theta = \frac{x}{L}
```
The sine and the tangent are nearly equal only at small angles, so the angle is first calculated from the tangent and only then the sine of the angle. For example, when the grating has $600$ lines per millimetre and the wavelength of a green laser is $532\,\text{nm}$, $\theta_1 = 18.6^\circ$, and on a screen one metre away $x_1 = 33.7\,\text{cm}$.

<svg data-fig="setup" viewBox="0 0 600 350" role="img" aria-label="Diagram to scale seen from above: on the left a laser whose beam hits the grating perpendicularly. The grating has 600 lines per millimetre, and the wavelength of the laser is 532 nm. One metre from the grating there is a screen. The light that goes straight through hits the screen at k = 0, and the first-order rays k = 1 and k = −1 are deviated by an angle of 18.6 degrees and hit the screen 33.7 cm on either side of the central maximum. The angle theta 1 is marked at the grating, the distance L from the grating to the screen and the distance x1 from the central maximum to the first maximum." style="max-width:100%;font-size:24px">
  <rect x="18" y="157" width="86" height="26" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="102" y="161" width="8" height="18" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="36" y="157" width="12" height="26" fill="#8a96a3"/>
  <line x1="110" y1="170" x2="140" y2="170" stroke="#e64980" stroke-width="3" stroke-linecap="round"/>
  <line x1="140" y1="170" x2="440" y2="170" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="140" y1="170" x2="440" y2="271" stroke="#e64980" stroke-width="3" stroke-linecap="round"/>
  <path d="M295.5,222.5 L281.5,224 L285.5,212.5 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="140" y1="170" x2="440" y2="170" stroke="#e64980" stroke-width="3" stroke-linecap="round"/>
  <path d="M296,170 L283,176 L283,164 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="140" y1="170" x2="440" y2="69" stroke="#e64980" stroke-width="3" stroke-linecap="round"/>
  <path d="M295.5,117.5 L285.5,127.5 L281.5,116 Z" fill="#e64980" stroke-linejoin="round"/>
  <rect x="136" y="120" width="8" height="100" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="136" y1="126" x2="144" y2="126" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="135" x2="144" y2="135" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="143.5" x2="144" y2="143.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="152.5" x2="144" y2="152.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="161" x2="144" y2="161" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="170" x2="144" y2="170" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="179" x2="144" y2="179" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="187.5" x2="144" y2="187.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="196.5" x2="144" y2="196.5" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="205" x2="144" y2="205" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <line x1="136" y1="214" x2="144" y2="214" stroke="#6b7480" stroke-width="1" stroke-linecap="butt"/>
  <rect x="440" y="34" width="10" height="272" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="445" cy="271" r="6" fill="#e64980" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="445" cy="170" r="6" fill="#e64980" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="445" cy="69" r="6" fill="#e64980" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M206.5,147.5 A70,70 0 0,1 210,170" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="226" y="138.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta_1$</div></foreignObject>
  <line x1="466" y1="119.5" x2="466" y2="161" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M466,170 L461.5,160 L470.5,160 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="466" y1="119.5" x2="466" y2="78" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M466,69 L470.5,79 L461.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="478" y="105" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="516" y="54.5" width="72" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$k = 1$</div></foreignObject>
  <foreignObject x="516" y="155.5" width="72" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$k = 0$</div></foreignObject>
  <foreignObject x="516" y="256.5" width="72" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$k = -1$</div></foreignObject>
  <line x1="290" y1="326" x2="149" y2="326" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M140,326 L150,321.5 L150,330.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="290" y1="326" x2="431" y2="326" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M440,326 L430,330.5 L430,321.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="277" y="291.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$L$</span></div></foreignObject>
  <foreignObject x="29" y="189.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{laser}$</div></foreignObject>
  <foreignObject x="154" y="225.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{grating}$</div></foreignObject>
  <foreignObject x="390.5" y="3.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{screen}$</div></foreignObject>
</svg>

### Measuring the wavelength of a laser
A grating can be used to measure the wavelength of a laser in a school laboratory. The laser, the grating and the screen are set in a line so that the beam hits both the grating and the screen perpendicularly. With a tape measure, the distance $L$ from the grating to the screen and the separation of two symmetric maxima $+k$ and $-k$ are measured; half of the separation is $x$. Measuring the separation of two dots is more accurate than estimating the position of the central maximum. School experiments use a low-power laser suitable for teaching, following the teacher's instructions. Never aim the laser beam, or a beam reflected from a grating or a disc, at anyone's eyes, and never look into the beam. The directions of the reflected beams and the safety of the surroundings are checked before measuring.

The largest uncertainty usually comes from deciding where the centre of a dot is. If $x$ can be measured with an uncertainty of, for example, $\Delta x = 0.2\,\text{cm}$, a maximum farther away gives a smaller relative uncertainty, because its $x$ is larger. The result is compared with the value stated by the manufacturer: the wavelength of a red laser pointer is usually about $650\,\text{nm}$ and that of a green one $532\,\text{nm}$.

## Worked example
The beam of a red laser pointer hits perpendicularly a grating that has $300$ lines per millimetre. On a screen $2.00\,\text{m}$ from the grating, the first-order maxima $k = 1$ and $k = -1$ are $79.2\,\text{cm}$ apart. What is the wavelength of the laser light?

<!-- vaihe -->

**Given and asked.** Line density $N = 300$ lines per millimetre, distance of the screen $L = 2.00\,\text{m}$ and separation of the maxima $\pm 1$ $79.2\,\text{cm}$, so the first maximum is at distance $x = 39.6\,\text{cm}$ from the central maximum. The order is $k = 1$. The wavelength $\lambda$ is asked.

<!-- vaihe -->

**Principle.** The directions of the maxima obey the grating equation $d\sin\theta = k\lambda$, because the beam arrives perpendicular to the grating. The screen is perpendicular to the beam, so the angle comes from the right-angled triangle whose legs are $x$ and $L$. The grating spacing comes from the line density.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\tan\theta = \frac{x}{L} \\[6pt]
&d\sin\theta = k\lambda \\[6pt]
&\lambda = \frac{d\sin\theta}{k}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The grating spacing is $d = 1\,\text{mm} : 300 = 1 \cdot 10^{-3}\,\text{m} : 300 = 3.333 \cdot 10^{-6}\,\text{m}$, and the distance of the maximum is $x = 39.6\,\text{cm} = 39.6 \cdot 0.01\,\text{m} = 0.396\,\text{m}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\tan\theta = \frac{x}{L} \\
&= \frac{0.396\,\text{m}}{2.00\,\text{m}} = 0.198 \\
&\theta = 11.20^\circ \\[6pt]
&\lambda = \frac{d\sin\theta}{k} \\
&= \frac{3.333 \cdot 10^{-6}\,\text{m} \cdot \sin 11.20^\circ}{1} \\
&= 6.474 \cdot 10^{-7}\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Result.** The wavelength is $\lambda \approx 6.47 \cdot 10^{-7}\,\text{m} = 647\,\text{nm}$, with three significant figures like the distances $2.00\,\text{m}$ and $79.2\,\text{cm}$.

<!-- vaihe -->

**Reasonableness.** The wavelength of red light is about $620$–$750\,\text{nm}$, and the stated wavelength of a red laser pointer is usually about $650\,\text{nm}$, so the result is credible. The angle is small, so $\sin\theta$ is almost the same as $\tan\theta = 0.198$. A value calculated with the tangent, $660\,\text{nm}$, would be a little too large, as it should be, since the tangent is always larger than the sine.

## Common misconception
Many assume that a grating bends blue and violet light the most, like a prism. In a grating it is the opposite: the direction of a maximum is decided by the condition $d\sin\theta = k\lambda$, so the longest wavelength, that is red light, is deviated most. In a prism violet is refracted most, because the refractive index of glass is largest for violet light. Another mistake is to think that a narrower slit makes the beam of light narrower. When the slit is of the order of the wavelength, diffraction spreads the light the more, the narrower the slit is.

## Summary
- Light is a wave motion: the light of coherent sources interferes, and bright and dark places form on the screen.
- In diffraction light spreads out behind a narrow slit. The narrower the slit, the wider the light spreads.
- The maxima of a grating are in the directions for which $d\sin\theta = k\lambda$, and the grating spacing is $d = 1\,\text{mm} : N$.
- From distances measured on the screen, $\tan\theta = x : L$. This is how a grating is used to measure the wavelength of a laser.
- White light is spread by a grating into a spectrum in which red light is deviated most. A CD is a reflection grating.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a CD lies on a table, lit by a desk lamp from the upper left. On the silvery surface of the disc there are rainbow-coloured zones stretching from the centre to the edge, in which the colours are in order from violet to red." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy713s-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><clipPath id="fy713s-disc"><ellipse cx="380" cy="262" rx="168" ry="72"/></clipPath></defs>
  <rect x="0" y="0" width="600" height="360" fill="#f6f1e6"/>
  <rect x="0" y="250" width="600" height="110" fill="url(#fy713s-desk)"/>
  <line x1="0" y1="250" x2="600" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="40" y="236" width="90" height="16" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M84,236 L104,110 L176,70" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M160,52 L222,84 L200,118 L140,88 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M200,118 L140,88" fill="none" stroke="#ffc078" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="380" cy="268" rx="170" ry="74" fill="#a97a35" fill-opacity="0.35"/>
  <ellipse cx="380" cy="262" rx="170" ry="74" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <g clip-path="url(#fy713s-disc)">
  <path d="M380,262 L640.5,167 L658.5,177 Z" fill="#7048e8" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L658.5,177 L674.5,188 Z" fill="#1971c2" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L674.5,188 L688,199.5 Z" fill="#2b8a3e" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L688,199.5 L699.5,211.5 Z" fill="#f59f00" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L699.5,211.5 L708.5,223.5 Z" fill="#e8590c" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L708.5,223.5 L715,236.5 Z" fill="#c92a2a" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L119.5,357 L101.5,347 Z" fill="#7048e8" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L101.5,347 L85.5,336 Z" fill="#1971c2" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L85.5,336 L72,324.5 Z" fill="#2b8a3e" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L72,324.5 L60.5,312.5 Z" fill="#f59f00" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L60.5,312.5 L51.5,300.5 Z" fill="#e8590c" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M380,262 L51.5,300.5 L45,287.5 Z" fill="#c92a2a" stroke-linejoin="round" fill-opacity="0.75"/>
  </g>
  <ellipse cx="380" cy="262" rx="40.8" ry="17.8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="380" cy="262" rx="15.3" ry="6.7" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
</svg>
