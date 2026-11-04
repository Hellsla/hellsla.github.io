# Magnetic field of a wire and a coil

> **Why** can the magnet of a scrapyard crane lift a tonne of scrap car into the air and drop it at the press of a button, when a fridge magnet never lets go?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a scrapyard crane. From the end of the boom of the crane a round grey electromagnet hangs on chains; it holds a rusty scrap car by its bottom and lifts it off a heap of scrap. In the background are heaps of scrap and the sky." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy73h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy73h-sky)"/>
  <path d="M130,130 Q128,96 168,100 Q184,64 224,76 Q260,56 280,94 Q316,98 312,130 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M917,94 Q915.5,70 943.5,73 Q955,48 983,56 Q1008,42 1022,69 Q1047,71.5 1044.5,94 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="0" y="470" width="1200" height="130" fill="#e9c98a"/>
  <path d="M0,480 L80,400 L170,430 L260,380 L360,470 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M780,480 L860,390 L930,420 L1010,360 L1100,410 L1200,380 L1200,480 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <rect x="40" y="440" width="70" height="30" rx="6" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="190" y="430" width="60" height="40" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="880" y="430" width="80" height="36" rx="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1040" y="420" width="90" height="44" rx="6" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="820" y="470" width="280" height="50" rx="18" fill="#1f2933"/>
  <circle cx="845" cy="495" r="14" fill="#6c757d" stroke="#8a96a3" stroke-width="3"/>
  <circle cx="885" cy="495" r="14" fill="#6c757d" stroke="#8a96a3" stroke-width="3"/>
  <circle cx="925" cy="495" r="14" fill="#6c757d" stroke="#8a96a3" stroke-width="3"/>
  <circle cx="965" cy="495" r="14" fill="#6c757d" stroke="#8a96a3" stroke-width="3"/>
  <circle cx="1005" cy="495" r="14" fill="#6c757d" stroke="#8a96a3" stroke-width="3"/>
  <circle cx="1045" cy="495" r="14" fill="#6c757d" stroke="#8a96a3" stroke-width="3"/>
  <circle cx="1085" cy="495" r="14" fill="#6c757d" stroke="#8a96a3" stroke-width="3"/>
  <rect x="860" y="380" width="200" height="90" rx="6" fill="#e8590c" stroke="#1f2933" stroke-width="3"/>
  <rect x="980" y="330" width="80" height="60" rx="6" fill="#e8590c" stroke="#1f2933" stroke-width="3"/>
  <rect x="992" y="342" width="56" height="34" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <path d="M900,400 L560,90 L585,78 L940,392 Z" fill="#ffc078" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="832" y1="338" x2="862" y2="330" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="764" y1="276" x2="794" y2="268" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="696" y1="214" x2="726" y2="206" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="628" y1="152" x2="658" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="566" y1="92" x2="540" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="566" y1="92" x2="600" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <g transform="translate(0 -14)">
  <path d="M440,300 L480,262 L640,262 L690,300 L710,302 L710,348 L430,348 L430,302 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M470,298 L494,272 L560,272 L560,298 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M574,298 L574,272 L630,272 L660,298 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="490" cy="350" r="26" fill="#1f2933"/>
  <circle cx="490" cy="350" r="11" fill="#c4ccd4"/>
  <circle cx="650" cy="350" r="26" fill="#1f2933"/>
  <circle cx="650" cy="350" r="11" fill="#c4ccd4"/>
  <path d="M520,320 L540,330 L530,340" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  </g>
  <ellipse cx="570" cy="206" rx="80" ry="16" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="490" y="206" width="160" height="38" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <ellipse cx="570" cy="244" rx="80" ry="16" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <path d="M566,92 C520,140 640,150 600,206" fill="none" stroke="#7048e8" stroke-width="3" stroke-linejoin="round"/>
</svg>

## Key idea

### An electric current creates a magnetic field
In 1820 the Danish physicist Hans Christian Ørsted noticed during a lecture that a compass needle turned when a current was switched on in a wire next to it. When the current was switched off, the needle went back to pointing north. The observation joined electricity and magnetism: **every current-carrying wire has a magnetic field around it**. The field is created by moving charges, so the wire does not have to be made of a magnetic material; even a copper wire creates a field. When the current grows, the field becomes stronger, and when the direction of the current is reversed, the direction of the field is reversed too.

The field lines of a straight wire are concentric circles around the wire, perpendicular to it. The field therefore does not point away from the wire or towards it, but goes round it. Compasses placed around the wire turn along the tangent of the circle when the field of the wire is much stronger than the Earth's magnetic field. The farther from the wire we are, the weaker the field.

<svg data-fig="wire-field" viewBox="0 0 600 372" role="img" aria-label="Schematic figure, not to scale, in two parts. On the left a vertical current-carrying wire through a table top seen from the side: a purple arrow shows the current upwards, and around the wire there are three green circular field lines whose arrows go round anticlockwise seen from above. On the right the same situation from above: the wire is a dot inside a circle, because the current comes towards the viewer, and around it there are three concentric field lines going anticlockwise. Four compasses on a field line: the north end of each needle, pink, points in the direction of the field line." style="max-width:100%;font-size:24px">
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{from the side}$</div></foreignObject>
  <foreignObject x="390" y="9.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{from above}$</div></foreignObject>
  <line x1="300" y1="48" x2="300" y2="356" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <path d="M30,236 L270,236 L246,276 L54,276 Z" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2" stroke-linejoin="round"/>
  <path d="M58,196 A92,22 0 0 1 242,196" fill="none" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round" stroke-opacity="0.55"/>
  <path d="M38,256 A112,26 0 0 1 262,256" fill="none" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round" stroke-opacity="0.55"/>
  <path d="M86,128 A64,15 0 0 1 214,128" fill="none" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round" stroke-opacity="0.55"/>
  <rect x="145" y="64" width="10" height="286" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <path d="M242,196 A92,22 0 0 1 58,196" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round"/>
  <path d="M128,218 L114,224.5 L114,211.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M262,256 A112,26 0 0 1 38,256" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round"/>
  <path d="M128,282 L114,288.5 L114,275.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M214,128 A64,15 0 0 1 86,128" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round"/>
  <path d="M128,143 L114,149.5 L114,136.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="176" y1="338" x2="176" y2="301" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M176,288 L182.5,302 L169.5,302 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="186" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="250" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <circle cx="450" cy="200" r="52" fill="none" stroke="#2b8a3e" stroke-width="2.5"/>
  <path d="M487,163 L500,168.5 L492,176.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M413,163 L418.5,150 L426.5,158 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M413,237 L400,231.5 L408,223.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M487,237 L481.5,250 L473.5,242 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="450" cy="200" r="96" fill="none" stroke="#2b8a3e" stroke-width="3"/>
  <path d="M518,132 L531,137 L523,145.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M382,132 L387,119 L395.5,127 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M382,268 L369,263 L377,254.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M518,268 L513,281 L504.5,273 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="450" cy="200" r="136" fill="none" stroke="#2b8a3e" stroke-width="2.5"/>
  <path d="M546,104 L559.5,109 L551,117 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M354,104 L359,90.5 L367,99 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M354,296 L340.5,291 L349,283 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M546,296 L541,309.5 L533,301 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="450" cy="200" r="14" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="450" cy="200" r="3.92" fill="#7048e8"/>
  <foreignObject x="470" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <circle cx="546" cy="200" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M546,180 L552,200 L540,200 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M546,220 L552,200 L540,200 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="546" cy="200" r="2.5" fill="#1f2933"/>
  <circle cx="450" cy="104" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M430,104 L450,98 L450,110 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M470,104 L450,98 L450,110 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="450" cy="104" r="2.5" fill="#1f2933"/>
  <circle cx="354" cy="200" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M354,220 L348,200 L360,200 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M354,180 L348,200 L360,200 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="354" cy="200" r="2.5" fill="#1f2933"/>
  <circle cx="450" cy="296" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M470,296 L450,302 L450,290 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M430,296 L450,302 L450,290 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="450" cy="296" r="2.5" fill="#1f2933"/>
  <foreignObject x="554" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/compass-needles-wire.webp" alt="A blue wire passes through a board, surrounded by four rows of small compass needles."><figcaption>Small compass needles around a current-carrying wire. Close to the wire, the needles turn along the field lines that circle the wire.</figcaption></figure>

### The right-hand rule
The direction in which the field goes round is given by the **right-hand rule**: when the thumb of the right hand points in the direction of the current, the curled fingers go round in the direction of the field lines. In the figure the current goes upwards, so seen from above the field goes round anticlockwise. In figures a current towards the viewer is marked with a dot $\odot$ and a current away from the viewer with a cross $\otimes$, like the tip and the tail feathers of an arrow.

### The field of a coil
When a wire is wound into a spiral, called a **coil**, the field of each turn points the same way inside the coil, and the fields strengthen each other. Inside a long coil the field lines are almost straight and evenly spaced: the field is almost uniform and parallel to the axis of the coil. At the ends of the coil the field lines spread out, and outside the coil the field is like that of a bar magnet in the chapter *Magnets, the magnetic dipole and the magnetic field*. The end from which the field lines emerge is the north pole N. The right-hand rule works for a coil like this: when the fingers curl along the turns in the direction of the current, the thumb points inside the coil in the direction of the field, that is, towards the north pole.

<svg data-fig="coil-field" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale: a long coil cut along its length. The wire cross-sections in the upper row have a dot (current towards the viewer) and those in the lower row a cross (current away from the viewer). Inside the coil the green field lines are straight, evenly spaced and pointing to the right, so the field is almost uniform. Outside, the field lines curve from the right end back to the left. The right end is the north pole N and the left end the south pole S, as in a bar magnet." style="max-width:100%;font-size:24px">
  <path d="M456,152 C542,146 520,84 300,84 C80,84 58,146 144,152" fill="none" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M292,84 L306,77.5 L306,90.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M456,132 C542,126 520,52 300,52 C80,52 58,126 144,132" fill="none" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M292,52 L306,45.5 L306,58.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M456,200 C542,206 520,268 300,268 C80,268 58,206 144,200" fill="none" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M292,268 L306,261.5 L306,274.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M456,220 C542,226 520,300 300,300 C80,300 58,226 144,220" fill="none" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M292,300 L306,293.5 L306,306.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="126" y1="146" x2="474" y2="146" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M320,146 L306,152.5 L306,139.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="126" y1="176" x2="474" y2="176" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M320,176 L306,182.5 L306,169.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="126" y1="206" x2="474" y2="206" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M320,206 L306,212.5 L306,199.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <circle cx="168" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="168" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="168" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="161.5" y1="229.5" x2="174.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="161.5" y1="242.5" x2="174.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="201" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="201" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="201" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="194.5" y1="229.5" x2="207.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="194.5" y1="242.5" x2="207.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="234" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="234" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="234" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="227.5" y1="229.5" x2="240.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="227.5" y1="242.5" x2="240.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="267" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="267" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="267" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="260.5" y1="229.5" x2="273.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="260.5" y1="242.5" x2="273.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="300" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="300" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="293.5" y1="229.5" x2="306.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="293.5" y1="242.5" x2="306.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="333" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="333" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="333" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="326.5" y1="229.5" x2="339.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="326.5" y1="242.5" x2="339.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="366" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="366" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="366" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="359.5" y1="229.5" x2="372.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="359.5" y1="242.5" x2="372.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="399" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="399" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="399" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="392.5" y1="229.5" x2="405.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="392.5" y1="242.5" x2="405.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="432" cy="116" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="432" cy="116" r="3.36" fill="#7048e8"/>
  <circle cx="432" cy="236" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="425.5" y1="229.5" x2="438.5" y2="242.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="425.5" y1="242.5" x2="438.5" y2="229.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="508" cy="176" r="19" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="498" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <circle cx="92" cy="176" r="19" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="82" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="372" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{B}$</span></div></foreignObject>
  <foreignObject x="90" y="9.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current: } \odot \text{ towards the viewer, } \otimes \text{ away}$</div></foreignObject>
  <foreignObject x="100" y="321.5" width="400" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{almost uniform field inside}$</div></foreignObject>
</svg>

### The electromagnet
When an iron core is pushed inside a coil, the field becomes many times stronger. The field of the coil turns the magnetic domains of the iron to point the same way, and the magnetised iron adds its own field to the field of the coil. A coil like this is an **electromagnet**. When the current is switched off, the field of the coil disappears, and the domains of soft iron return almost to disorder, so the core loses almost all of its magnetisation. That is why the scrapyard crane holds the scrap only as long as the current flows. A permanent magnet, by contrast, is made of a material whose domains stay aligned, so it cannot be switched off.

<svg data-fig="electromagnet" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale: an electromagnet. A copper coil is wound round a vertical grey iron core, and the wires of the coil go to a battery and a switch. On the left the switch is closed and a current flows: the lower end of the iron core attracts iron nails, which hang from it in a chain. On the right the same electromagnet with the switch open: the blade of the switch is lifted off its contact, the circuit is broken and the nails have fallen onto the table." style="max-width:100%;font-size:24px">
  <line x1="300" y1="40" x2="300" y2="344" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="71" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current flows}$</div></foreignObject>
  <foreignObject x="333.5" y="9.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current switched off}$</div></foreignObject>
  <line x1="12" y1="316" x2="588" y2="316" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="132" y="70" width="36" height="170" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M124,92 Q150,102 176,96" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,105 Q150,115 176,109" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,118 Q150,128 176,122" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,131 Q150,141 176,135" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,144 Q150,154 176,148" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,157 Q150,167 176,161" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,170 Q150,180 176,174" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,183 Q150,193 176,187" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,196 Q150,206 176,200" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M124,209 Q150,219 176,213" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M176,96 H184" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M212,96 H224 V128" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="184" cy="96" r="4" fill="#1f2933"/>
  <circle cx="212" cy="96" r="4" fill="#1f2933"/>
  <path d="M176,210 H224 V182" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="208" y="128" width="32" height="54" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="217" y="122" width="14" height="6" fill="#1f2933"/>
  <line x1="184" y1="96" x2="212" y2="96" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="190" y1="210" x2="202" y2="210" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M212,210 L201,215 L201,205 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="191" y="221.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <rect x="147" y="246" width="6" height="16" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="143" y="246" width="14" height="3" fill="#8a96a3"/>
  <rect x="147" y="263" width="6" height="16" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="143" y="263" width="14" height="3" fill="#8a96a3"/>
  <rect x="147" y="280" width="6" height="16" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="143" y="280" width="14" height="3" fill="#8a96a3"/>
  <rect x="147" y="297" width="6" height="16" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="143" y="297" width="14" height="3" fill="#8a96a3"/>
  <foreignObject x="56" y="145.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{iron}$</div></foreignObject>
  <rect x="432" y="70" width="36" height="170" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M424,92 Q450,102 476,96" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,105 Q450,115 476,109" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,118 Q450,128 476,122" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,131 Q450,141 476,135" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,144 Q450,154 476,148" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,157 Q450,167 476,161" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,170 Q450,180 476,174" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,183 Q450,193 476,187" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,196 Q450,206 476,200" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M424,209 Q450,219 476,213" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M476,96 H484" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M512,96 H524 V128" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="484" cy="96" r="4" fill="#1f2933"/>
  <circle cx="512" cy="96" r="4" fill="#1f2933"/>
  <path d="M476,210 H524 V182" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="508" y="128" width="32" height="54" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="517" y="122" width="14" height="6" fill="#1f2933"/>
  <line x1="484" y1="96" x2="506" y2="72" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="410" y="306" width="22" height="6" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="444" y="306" width="22" height="6" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="476" y="306" width="22" height="6" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="504" y="306" width="22" height="6" rx="1" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="356" y="145.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{iron}$</div></foreignObject>
</svg>

## Formula: Magnetic field of a straight wire and of a coil
The magnetic flux density of a long straight wire at a distance $r$ from the wire is
```latex
B = \frac{\mu_0 I}{2\pi r}
```
where $B$ is the magnetic flux density (T), $I$ the current in the wire (A), $r$ the distance from the wire (m) and $\mu_0 = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$ the permeability of free space, a constant of nature. In air the same value is used. The field is directly proportional to the current and inversely proportional to the distance: doubling the distance halves the field. The formula holds when the wire is much longer than the distance $r$ and other wires are far away. For example, the field of a $10\,\text{A}$ wire at a distance of $1\,\text{cm}$ is $200\,\mu\text{T}$, about four times the Earth's magnetic field of about $50\,\mu\text{T}$.

<svg data-fig="wire-graph" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the magnetic flux density B of a straight wire in microtesla as a function of the distance r in centimetres, when the current is 10 A. The curve falls as the distance grows: at a distance of 1 cm B is 200 µT, at 2 cm it is 100 µT and at 4 cm it is 50 µT. When the distance doubles, the field is halved." style="max-width:100%;font-size:24px">
  <line x1="171" y1="290" x2="171" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="245.5" y1="290" x2="245.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="290" x2="320.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="290" x2="395" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="243" x2="470" y2="243" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="196.5" x2="470" y2="196.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="149.5" x2="470" y2="149.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103" x2="470" y2="103" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="56" x2="470" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,30 L102,43 L90,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="171" y1="290" x2="171" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="245.5" y1="290" x2="245.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="320.5" y1="290" x2="320.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="310.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="395" y1="290" x2="395" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="460" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="243" x2="96" y2="243" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="228.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="196.5" x2="96" y2="196.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="182" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="149.5" x2="96" y2="149.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="135" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="103" x2="96" y2="103" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="88.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="56" x2="96" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="41.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{cm})$</div></foreignObject>
  <foreignObject x="86" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$B\ (\mu\text{T})$</div></foreignObject>
  <polyline points="156,56 158.5,66 161,75 163.5,83 166.5,91 169,98 171.5,104.5 174,111 177,116.5 179.5,122 182,127 184.5,132 187.5,136.5 190,141 192.5,145 195,148.5 197.5,152.5 200.5,156 203,159 205.5,162 208,165 211,168 213.5,171 216,173.5 218.5,176 221.5,178 224,180.5 226.5,182.5 229,185 232,187 234.5,189 237,190.5 239.5,192.5 242,194 245,196 247.5,197.5 250,199 252.5,200.5 255.5,202 258,203.5 260.5,205 263,206 266,207.5 268.5,209 271,210 273.5,211 276.5,212.5 279,213.5 281.5,214.5 284,215.5 286.5,216.5 289.5,217.5 292,218.5 294.5,219.5 297,220.5 300,221.5 302.5,222 305,223 307.5,224 310.5,224.5 313,225.5 315.5,226 318,227 321,227.5 323.5,228.5 326,229 328.5,230 331,230.5 334,231 336.5,232 339,232.5 341.5,233 344.5,233.5 347,234 349.5,235 352,235.5 355,236 357.5,236.5 360,237 362.5,237.5 365.5,238 368,238.5 370.5,239 373,239.5 376,240 378.5,240.5 381,241 383.5,241.5 386,242 389,242 391.5,242.5 394,243 396.5,243.5 399.5,244 402,244 404.5,244.5 407,245 410,245.5 412.5,245.5 415,246 417.5,246.5 420.5,247 423,247 425.5,247.5 428,248 430.5,248 433.5,248.5 436,249 438.5,249 441,249.5 444,249.5 446.5,250 449,250.5 451.5,250.5 454.5,251 457,251 459.5,251.5 462,252 465,252 467.5,252.5 470,252.5" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="171" y1="103" x2="171" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="103" x2="171" y2="103" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="171" cy="103" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <line x1="245.5" y1="196.5" x2="245.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="196.5" x2="245.5" y2="196.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="245.5" cy="196.5" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <line x1="395" y1="243" x2="395" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="243" x2="395" y2="243" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="395" cy="243" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="268" y="83.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$I = 10\,\text{A}$</div></foreignObject>
</svg>

Inside a long coil, far from its ends, the magnetic flux density is
```latex
B = \mu_0 \frac{N I}{l}
```
where $N$ is the number of turns of the coil, $I$ the current (A) and $l$ the length of the coil (m). The field depends on the turn density $N : l$, that is, on how many turns there are per metre, and not on the thickness of the coil. The formula holds when the coil is much longer than it is wide and has only air inside it. At the ends of the coil the field is about half of its value at the centre, and an iron core makes the field many times stronger.

<svg data-fig="coil-dims" viewBox="0 0 600 330" role="img" aria-label="Schematic figure, not to scale: a coil seen from the side. The coil has N turns of copper wire over a length l. A current I, marked with a purple arrow, flows from the ends of the wire. Inside the coil a green arrow points along the axis; above the start of the arrow is the label B." style="max-width:100%;font-size:24px">
  <rect x="120" y="103.5" width="290" height="93" fill="#eef5f9" stroke="#8a96a3" stroke-width="1.5"/>
  <line x1="136.5" y1="92" x2="124" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="157.5" y1="92" x2="145" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="178" y1="92" x2="165.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="198.5" y1="92" x2="186.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="219.5" y1="92" x2="207" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="240" y1="92" x2="227.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="261" y1="92" x2="248.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="281.5" y1="92" x2="269" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="302.5" y1="92" x2="290" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="323" y1="92" x2="310.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="343.5" y1="92" x2="331.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="364.5" y1="92" x2="352" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="385" y1="92" x2="372.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="406" y1="92" x2="393.5" y2="208" stroke="#b8622d" stroke-width="2" stroke-opacity="0.45"/>
  <line x1="150" y1="150" x2="363" y2="150" stroke="#2b8a3e" stroke-width="4" stroke-linecap="butt"/>
  <path d="M380,150 L362,158 L362,142 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="147.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{B}$</span></div></foreignObject>
  <line x1="124" y1="92" x2="136.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="145" y1="92" x2="157.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="165.5" y1="92" x2="178" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="186.5" y1="92" x2="198.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="207" y1="92" x2="219.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="227.5" y1="92" x2="240" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="248.5" y1="92" x2="261" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="269" y1="92" x2="281.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="290" y1="92" x2="302.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="310.5" y1="92" x2="323" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="331.5" y1="92" x2="343.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="352" y1="92" x2="364.5" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="372.5" y1="92" x2="385" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <line x1="393.5" y1="92" x2="406" y2="208" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <path d="M124.14285714285714,208 V242 H50" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M405.85714285714283,208 V242 H470" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="60" y1="242" x2="92" y2="242" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M104,242 L91,248 L91,236 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="60" y="253.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="120" y1="52" x2="410" y2="52" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="120" y1="43" x2="120" y2="61" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="410" y1="43" x2="410" y2="61" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="255" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$l$</span></div></foreignObject>
  <foreignObject x="426" y="135.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N\ \text{turns}$</div></foreignObject>
</svg>

### Determining the magnetic flux density inside a coil
The field is measured with a magnetic field sensor whose tip is placed at the centre of the coil, parallel to the axis. The current is varied with a power supply, and at each current the current and the reading $B$ of the sensor are recorded. When the measurements are plotted in an $(I, B)$ graph, for example with the Vernier Graphical Analysis program, a straight line $B = A I + B_0$ is fitted to them. According to the formula the slope is $A = \mu_0 \tfrac{N}{l}$, so the measurement gives an estimate for the permeability of free space, $\mu_0 = A l : N$. When the uncertainty of the slope is $\Delta A$ and that of the length $\Delta l$, the relative uncertainty of the result is estimated by adding the relative uncertainties of the factors: $\Delta \mu_0 : \mu_0 = \Delta A : A + \Delta l : l$. The constant term $B_0$ is usually small: it is affected by the zero point of the sensor and by the Earth's magnetic field.

## Worked example
A school coil has $600$ turns and its length is $15.0\,\text{cm}$. A current of $2.50\,\text{A}$ flows in the coil. How great is the magnetic flux density at the centre of the coil? How many times greater is it than the Earth's magnetic field of $50\,\mu\text{T}$? The coil is long compared with its width, and it has air inside it.

<!-- vaihe -->

**Given and asked.** Number of turns $N = 600$, length of the coil $l = 15.0\,\text{cm}$, current $I = 2.50\,\text{A}$ and the constant $\mu_0 = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$. We are asked for the magnetic flux density $B$ at the centre of the coil and its ratio to the Earth's field $B_\text{Earth} = 50\,\mu\text{T}$.

<!-- vaihe -->

**Principle.** The coil is long, it has air inside, and we want the field at the centre, far from the ends, so the formula for a long coil holds. The field depends only on the turn density and the current.

<!-- vaihe -->

**Formula solved.** The formula gives the asked quantity directly, and the ratio is found by dividing:
```latex
\begin{aligned}
&B = \mu_0 \frac{N I}{l} \\
&k = \frac{B}{B_\text{Earth}}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The length in metres: $l = 15.0 \cdot 0.01\,\text{m} = 0.150\,\text{m}$. The Earth's field in tesla: $50\,\mu\text{T} = 50 \cdot 10^{-6}\,\text{T}$. For the units, $\tfrac{\text{Vs}}{\text{Am}} \cdot \tfrac{\text{A}}{\text{m}} = \tfrac{\text{Vs}}{\text{m}^2} = \text{T}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&B = \mu_0 \frac{N I}{l} \\
&= 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \\
&\quad \cdot \frac{600 \cdot 2.50\,\text{A}}{0.150\,\text{m}} \\
&= 0.012566\,\text{T} \\[6pt]
&k = \frac{0.012566\,\text{T}}{50 \cdot 10^{-6}\,\text{T}} \\
&= 251.3
\end{aligned}
```

<!-- vaihe -->

**Result.** The magnetic flux density at the centre of the coil is $12.6\,\text{mT}$, to three significant figures like the length $15.0\,\text{cm}$ and the current $2.50\,\text{A}$. It is about $250$ times the Earth's magnetic field; the ratio is given to two figures because the Earth's field of $50\,\mu\text{T}$ is known only to two figures.

<!-- vaihe -->

**Reasonableness.** The turn density is $600 : 0.150\,\text{m} = 4000$ turns per metre. One ampere and a thousand turns per metre give about $1.3\,\text{mT}$, so $2.5\,\text{A}$ and four times the density give about $1.3\,\text{mT} \cdot 2.5 \cdot 4 = 13\,\text{mT}$. The result is about $250$ times the Earth's field, so the field of the coil is easy to measure, and it is clearly smaller than the roughly $1.5\,\text{T}$ of an MRI scanner, which needs a superconducting coil and a current of hundreds of amperes.

## Common misconception
Many people think that the magnetic field of a current-carrying wire points away from the wire, like the electric field of a charged wire. The field lines, however, go round the wire as closed circles, and they have neither a starting point nor an end point. A compass next to the wire therefore turns across the wire, not towards it.

Another mistake is to think that the field of a coil depends on the total number of turns. If the same coil of $200$ turns is stretched to twice its length, the turn density $N : l$ is halved and the field at the centre of the coil is about halved, even though there are just as many turns. A third mistake is to forget that the formula for a long coil does not hold at the ends of the coil: there the field is only about half of its value at the centre.

## Summary
- An electric current creates a magnetic field around it (Ørsted 1820). The field lines of a straight wire are circles going round the wire, and their direction is given by the right-hand rule: thumb in the direction of the current, fingers in the direction of the field.
- The field of a long straight wire is $B = \tfrac{\mu_0 I}{2\pi r}$: it grows with the current and weakens as the distance grows.
- Inside a long coil the field is almost uniform, $B = \mu_0 \tfrac{N I}{l}$. It depends on the turn density $N : l$ and the current. Outside, the field of the coil is like that of a bar magnet.
- An iron core turns a coil into an electromagnet, whose field is many times stronger and which can be switched on and off.
- By measuring $B$ as a function of the current and fitting a straight line, we get $\mu_0 = A l : N$ from the slope.
