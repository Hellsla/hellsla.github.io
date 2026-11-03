# Force on a current-carrying wire: the electric motor and the loudspeaker

> **Why** does a loudspeaker cone vibrate and the blades of a desk fan turn, when nothing visible pushes either of them?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a desk there is a wooden loudspeaker, from whose cone sound waves spread, and next to it a desk fan with turning blades. Nobody touches either, but the cone vibrates and the blades turn when electric current is switched on to the devices." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy74h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy74h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy74h-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b8622d"/><stop offset="1" stop-color="#8a5f22"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="430" width="1200" height="170" fill="url(#fy74h-desk)"/>
  <line x1="0" y1="430" x2="1200" y2="430" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <rect x="120" y="60" width="220" height="260" rx="6" fill="url(#fy74h-sky)" stroke="#1f2933" stroke-width="3"/>
  <line x1="230" y1="60" x2="230" y2="320" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="190" x2="340" y2="190" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M520,420 C520,470 600,480 700,486" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <path d="M840,424 C840,476 760,480 700,486" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <rect x="660" y="476" width="110" height="26" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="400" y="150" width="240" height="280" rx="10" fill="url(#fy74h-wood)" stroke="#1f2933" stroke-width="3"/>
  <circle cx="520" cy="330" r="78" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="520" cy="330" r="64" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="330" r="40" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="330" r="18" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="205" r="34" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="520" cy="205" r="20" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M390,235 A150,150 0 0 0 390,385" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M650,235 A150,150 0 0 1 650,385" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M364,220 A180,180 0 0 0 364,400" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M676,220 A180,180 0 0 1 676,400" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M338,205 A210,210 0 0 0 338,415" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.4"/>
  <path d="M702,205 A210,210 0 0 1 702,415" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.4"/>
  <path d="M770,430 Q840,400 910,430 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="830" y="300" width="20" height="120" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="840" cy="250" r="118" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <path d="M840,250 Q897.5,144.5 810.5,154.5 Z" fill="#1971c2" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M840,250 Q720,253 772,323.5 Z" fill="#1971c2" stroke-linejoin="round" fill-opacity="0.75"/>
  <path d="M840,250 Q902.5,352.5 937.5,272 Z" fill="#1971c2" stroke-linejoin="round" fill-opacity="0.75"/>
  <circle cx="840" cy="250" r="60" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="840" cy="250" r="90" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="840" cy="250" r="22" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <path d="M966,204 A134,134 0 0 0 886,124" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M737.5,164 A134,134 0 0 0 708,273.5" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M816.5,382 A134,134 0 0 0 926,352.5" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

## Key idea

### A magnetic field pushes a current-carrying wire
In the chapter *Charged particle in electric and magnetic fields*, a magnetic field exerted on a moving charged particle a force perpendicular to both the velocity of the particle and the field. An electric current in a wire is a motion of charges: the conduction electrons of the metal move along the wire. The magnetic field exerts a force on every moving electron, and the electrons pass it on to the metal of the wire, so the force acts on the whole wire. When a light copper wire is hung between the poles of a horseshoe magnet and a current is switched on, the wire swings sideways. Copper is not ferromagnetic, and the magnet does not attract it: the force appears only when there is a current in the wire.

<svg data-fig="swing" viewBox="0 0 600 360" role="img" aria-label="Two schematic figures, not to scale. On the left a wire is seen end-on between the poles of two magnets: the N pole is at the top and the S pole at the bottom, so the magnetic field points downwards. The current flows into the page in the wire, and the force of the magnetic field pushes the wire to the left, perpendicular to both the current and the field. On the right the right-hand rule: the thumb points in the direction of the current, the other fingers in the direction of the field (the obliquely drawn arrow comes towards the viewer), and the force points out of the palm, here downwards. The three arrows are perpendicular to each other." style="max-width:100%;font-size:24px">
  <rect x="70" y="40" width="180" height="56" rx="4" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="150" y="53.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <rect x="70" y="268" width="180" height="56" rx="4" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="150" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <line x1="84" y1="104" x2="84" y2="246" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,258 L78,245 L90,245 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="236" y1="104" x2="236" y2="246" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M236,258 L230,245 L242,245 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="246" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <circle cx="160" cy="180" r="16" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="151" y1="171" x2="169" y2="189" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="169" y1="171" x2="151" y2="189" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="140" y1="180" x2="111" y2="180" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M98,180 L112,173.5 L112,186.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="103.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="150" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="300" y1="24" x2="300" y2="340" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="400" y1="120" x2="536" y2="120" stroke="#7048e8" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M550,120 L535,127 L535,113 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="400" y1="120" x2="340.5" y2="174.5" stroke="#2b8a3e" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M330,184 L336.5,169 L345.5,179 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="400" y1="120" x2="400" y2="276" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M400,290 L393,275 L407,275 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="400" cy="120" r="5" fill="#1f2933"/>
  <foreignObject x="540" y="81.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="465" y="131.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{thumb}$</div></foreignObject>
  <foreignObject x="287" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="286" y="209.5" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{fingers}$</div></foreignObject>
  <foreignObject x="416" y="265.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="416" y="303.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{palm}$</div></foreignObject>
  <foreignObject x="310" y="13.5" width="280" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{right-hand rule}$</div></foreignObject>
</svg>

### The direction of the force
The force is always perpendicular to both the direction of the current and the magnetic field. Its direction is given by the **right-hand rule**: when the thumb of an outstretched right hand points in the direction of the current and the other fingers in the direction of the magnetic field, the force points out of the palm. It is the same rule as for a positively charged particle, because the direction of the current is the direction in which positive charge moves. When the direction of the current or of the field is reversed, the direction of the force reverses. If the wire is parallel to the field, there is no force at all.

### The electric motor
In a direct-current motor, a **current loop** that can turn about an axle sits between the poles of a magnet. In the two sides of the loop that cross the field, the current flows in opposite directions, so the forces on them are in opposite directions. The forces are not on the same line, so they have a turning effect: they turn the loop. When the loop has turned to be perpendicular to the field, the forces point away from the axle and no longer turn it, and the loop keeps moving because of its inertia. Exactly then the **commutator**, a split ring with the carbon brushes that touch it, reverses the direction of the current in the loop. In this way the forces turn the loop in the same direction every half turn. A real motor has many coils and an iron core, so it turns smoothly and strongly.

<svg data-fig="motor" viewBox="0 0 600 380" role="img" aria-label="Two schematic figures of a direct-current motor, not to scale. On the left a current loop is seen along the axle between the N and S poles; the magnetic field points from left to right. In one side of the loop the current flows into the page and in the other out of the page. The forces on the sides are in opposite directions, one downwards and the other upwards, and they turn the loop anticlockwise. On the right the commutator: around the axle is a ring split into two parts, touched by two carbon brushes. The brushes are connected to the positive and negative terminals of the power supply." style="max-width:100%;font-size:24px">
  <rect x="20" y="110" width="52" height="170" rx="4" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="36" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <rect x="288" y="110" width="52" height="170" rx="4" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="304" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <line x1="82" y1="130" x2="267" y2="130" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M278,130 L266,135.5 L266,124.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="82" y1="260" x2="267" y2="260" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M278,260 L266,265.5 L266,254.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="243" y="269.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <circle cx="180" cy="195" r="70" fill="none" stroke="#c9c2b2" stroke-width="1.5"/>
  <line x1="116.5" y1="224.5" x2="243.5" y2="165.5" stroke="#b8622d" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="180" cy="195" r="6" fill="#1f2933"/>
  <circle cx="116.5" cy="224.5" r="13" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="109.5" y1="217.5" x2="123.5" y2="231.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="123.5" y1="217.5" x2="109.5" y2="231.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="243.5" cy="165.5" r="13" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="243.5" cy="165.5" r="4.16" fill="#7048e8"/>
  <line x1="116.5" y1="240.5" x2="116.5" y2="288.5" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M116.5,300.5 L110.5,287.5 L122.5,287.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="243.5" y1="149.5" x2="243.5" y2="101.5" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M243.5,89.5 L249.5,102.5 L237.5,102.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="130.5" y="276" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="196.5" y="85" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M154.5,100.5 A98,98 0 0 0 95,146" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M89,156.5 L91,139 L103,146 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="95" y="345.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current loop}$</div></foreignObject>
  <line x1="370" y1="30" x2="370" y2="350" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <path d="M476,152 A38,38 0 0 0 476,228 V214 A24,24 0 0 1 476,166 Z" fill="#b8622d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M488,152 A38,38 0 0 1 488,228 V214 A24,24 0 0 0 488,166 Z" fill="#b8622d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="482" cy="190" r="8" fill="#1f2933"/>
  <rect x="416" y="176" width="28" height="28" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="520" y="176" width="28" height="28" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="416" y1="190" x2="404" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="548" y1="190" x2="560" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="380" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="564" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="392" y="77.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{commutator}$</div></foreignObject>
  <foreignObject x="407" y="275.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{carbon brushes}$</div></foreignObject>
  <line x1="430" y1="208" x2="442" y2="272" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="534" y1="208" x2="522" y2="272" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

### The loudspeaker
The magnet of a loudspeaker is built so that in the ring-shaped gap the field points radially outwards. In the gap is a light voice coil, and every part of it is perpendicular to the field, so an equal force acts on every part in the direction of the axis of the coil. A radial field is essential: in a uniform field the forces on opposite sides of a closed coil would be in opposite directions and would cancel, so nothing would push the coil. The coil is attached to the cone. The alternating current from the amplifier changes its direction in step with the sound signal, so the force pushes the cone alternately forwards and backwards. The cone vibrates at the frequency of the signal, compresses and rarefies the air and produces a sound wave. The larger the current, the larger the force and the louder the sound. Most of the electrical energy delivered to the loudspeaker is, however, transformed into internal energy of the coil and the magnet.

<svg data-fig="speaker" viewBox="0 0 600 360" role="img" aria-label="Cross-section of a loudspeaker, schematic figure, not to scale. On the left is an iron centre pole, and around it a ring magnet and a front plate. The centre pole is an N pole and the front plate an S pole, so in the narrow gap the magnetic field points radially outwards, upwards in the upper gap and downwards in the lower gap. In the gap is the voice coil: in the cross-section of its turns the current flows into the page above and out of the page below. On both sides the force points to the right, towards the cone, which is attached to the coil." style="max-width:100%;font-size:24px">
  <rect x="40" y="60" width="24" height="240" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="64" y="150" width="176" height="60" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="64" y="60" width="56" height="54" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="64" y="246" width="56" height="54" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="120" y="60" width="56" height="54" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <rect x="120" y="246" width="56" height="54" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="198" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{N}$</div></foreignObject>
  <foreignObject x="138" y="72.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="138" y="258.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <rect x="126" y="141" width="142" height="4" fill="#e9c98a"/>
  <rect x="126" y="215" width="142" height="4" fill="#e9c98a"/>
  <circle cx="143" cy="130" r="8" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="138.5" y1="125.5" x2="147.5" y2="134.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="147.5" y1="125.5" x2="138.5" y2="134.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="143" cy="230" r="8" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="143" cy="230" r="2.56" fill="#7048e8"/>
  <foreignObject x="92" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="92" y="215.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="168" y1="148" x2="168" y2="125" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M168,116 L172.5,126 L163.5,126 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="168" y1="212" x2="168" y2="235" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M168,244 L163.5,234 L172.5,234 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="186" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <path d="M268,141 L420,40 L434,40 L282,143 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M268,219 L420,320 L434,320 L282,217 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M268,141 Q306,180 268,219" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="184" y1="126" x2="234" y2="126" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M246,126 L233,132 L233,120 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="184" y1="234" x2="234" y2="234" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M246,234 L233,240 L233,228 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="252" y="97.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="252" y="233.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="446" y="25.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{cone}$</div></foreignObject>
  <foreignObject x="40" y="315.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ring magnet}$</div></foreignObject>
  <foreignObject x="365" y="165.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \text{ varies}$</div></foreignObject>
  <foreignObject x="325" y="207.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Rightarrow F \text{ varies}$</div></foreignObject>
</svg>

## Formula: Force on a current-carrying wire
When a current $I$ flows in a straight wire and the wire is in a uniform magnetic field, the field exerts on the wire a force of magnitude
```latex
F = I l B \sin\alpha
```
where $F$ is the force (N), $I$ the current (A), $l$ the length of the part of the wire that is in the field (m), $B$ the magnetic flux density (T) and $\alpha$ the angle between the wire and the field. Only the component of the field perpendicular to the wire, $B \sin\alpha$, produces a force. The force is greatest when the wire is perpendicular to the field ($\sin 90^\circ = 1$) and zero when the wire is parallel to the field ($\sin 0^\circ = 0$). At an angle of $30^\circ$ the force is half of its greatest value, because $\sin 30^\circ = 0.5$. The formula gives the unit of the tesla: $1\,\text{T} = 1\,\tfrac{\text{N}}{\text{A}\cdot\text{m}}$.

<svg data-fig="angle" viewBox="0 0 600 340" role="img" aria-label="Schematic figure seen from above, not to scale. The horizontal green field lines point to the right. The wire is at an angle alpha to the field, and the current flows along the wire towards the upper right. The component of the field perpendicular to the wire, B sin alpha, is drawn with a dashed line. The force points into the page, which is shown by a cross inside a circle at the middle of the wire." style="max-width:100%;font-size:24px">
  <line x1="30" y1="60" x2="570" y2="60" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M470,60 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="30" y1="120" x2="570" y2="120" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M470,120 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="30" y1="180" x2="570" y2="180" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M470,180 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="30" y1="240" x2="570" y2="240" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M470,240 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="30" y1="300" x2="570" y2="300" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M470,300 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="527" y="19.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <line x1="154.5" y1="302" x2="445.5" y2="58" stroke="#b8622d" stroke-width="7" stroke-linecap="round"/>
  <line x1="194" y1="240.5" x2="368" y2="94.5" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M378,86 L371,100 L363,90 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="230" y="156" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="300" y1="180" x2="450" y2="180" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M370,180 A70,70 0 0 0 353.5,135" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="376.5" y="134" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <line x1="415" y1="83.5" x2="456" y2="132.5" stroke="#2b8a3e" stroke-width="2.5" stroke-dasharray="7 5"/>
  <path d="M460,137 L445.5,129.5 L455,122 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="470" y="140" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$B \sin\alpha$</span></div></foreignObject>
  <circle cx="300" cy="180" r="15" fill="#ffffff" stroke="#c92a2a" stroke-width="2.5"/>
  <line x1="292" y1="172" x2="308" y2="188" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="308" y1="172" x2="292" y2="188" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="320" y="201.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
</svg>

### The force between two current-carrying wires
There is a force between two parallel current-carrying wires, because each is in the magnetic field of the other. In the chapter *Magnetic field of a wire and a coil*, the field of wire $1$ circles around it, and at a distance $r$ its magnitude is $B_1$. At wire $2$ the field is perpendicular to wire $2$, so a force $F$ acts on the part of wire $2$ whose length is $l$:
```latex
\begin{aligned}
&B_1 = \frac{\mu_0 I_1}{2\pi r} \\[6pt]
&F = I_2 l B_1 \\
&\quad = \frac{\mu_0 I_1 I_2 l}{2\pi r}
\end{aligned}
```
where $I_1$ and $I_2$ are the currents of the wires (A), $r$ is the distance between the wires (m), $l$ the length of the part that runs parallel (m) and $\mu_0 = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$ the permeability of vacuum. By Newton's third law, an equal and opposite force acts on wire $1$. The right-hand rule shows that **currents in the same direction attract each other and currents in opposite directions repel each other**. Until 2019 the ampere was defined with this force: the current is $1\,\text{A}$ when the force between wires $1\,\text{m}$ apart is $2 \cdot 10^{-7}\,\text{N}$ for every metre of wire.

<svg data-fig="wires" viewBox="0 0 600 360" role="img" aria-label="Two schematic figures of parallel wires seen end-on, not to scale. On the left the current in both wires flows out of the page. The magnetic field of the left wire circles it anticlockwise, and at the right wire the field points upwards. The forces point from one wire towards the other: the wires attract each other. On the right the currents are in opposite directions, the current in the right wire flows into the page, and the forces point away from each other: the wires repel each other." style="max-width:100%;font-size:24px">
  <foreignObject x="15" y="13.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{currents in the same direction}$</div></foreignObject>
  <foreignObject x="325" y="13.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{currents in opposite directions}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="340" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <circle cx="105" cy="190" r="90" fill="none" stroke="#2b8a3e" stroke-width="2"/>
  <path d="M105,100 l12,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="195" y1="172" x2="195" y2="139" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M195,128 L200.5,140 L189.5,140 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="207" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_1$</div></foreignObject>
  <circle cx="105" cy="190" r="14" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="105" cy="190" r="4.48" fill="#7048e8"/>
  <circle cx="195" cy="190" r="14" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="195" cy="190" r="4.48" fill="#7048e8"/>
  <foreignObject x="88.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="209" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <line x1="122" y1="190" x2="135" y2="190" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M146,190 L134,195.5 L134,184.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="178" y1="190" x2="165" y2="190" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M154,190 L166,184.5 L166,195.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="133.5" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="90" y="321.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{attract}$</div></foreignObject>
  <circle cx="405" cy="190" r="90" fill="none" stroke="#2b8a3e" stroke-width="2"/>
  <path d="M405,100 l12,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="495" y1="172" x2="495" y2="139" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M495,128 L500.5,140 L489.5,140 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="507" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_1$</div></foreignObject>
  <circle cx="405" cy="190" r="14" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="405" cy="190" r="4.48" fill="#7048e8"/>
  <circle cx="495" cy="190" r="14" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="487.5" y1="182.5" x2="502.5" y2="197.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="502.5" y1="182.5" x2="487.5" y2="197.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="388.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="509" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <line x1="388" y1="190" x2="369" y2="190" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M358,190 L370,184.5 L370,195.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="512" y1="190" x2="531" y2="190" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M542,190 L530,195.5 L530,184.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="354.5" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="390" y="321.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{repel}$</div></foreignObject>
</svg>

## Worked example
A loudspeaker voice coil has $60$ turns of thin wire, and the radius of the coil is $1.3\,\text{cm}$. The coil is in the gap of a magnet, where the magnetic flux density of the radial field is $0.95\,\text{T}$, and the field is perpendicular to the wire everywhere. How large is the force on the coil when the current is at its peak value of $1.5\,\text{A}$?

<!-- vaihe -->

**Given and find.** Number of turns $N = 60$, radius of the coil $r = 1.3\,\text{cm}$, magnetic flux density $B = 0.95\,\text{T}$, current $I = 1.5\,\text{A}$ and angle between the wire and the field $\alpha = 90^\circ$. We are asked for the force $F$ on the coil.

<!-- vaihe -->

**Principle.** The field is radial, so every part of the wire of the coil is perpendicular to the field, and the force on every part points in the same direction, along the axis of the coil. The forces therefore add up, and in the formula $F = I l B \sin\alpha$ the length $l$ is the whole length of the wire of the coil: $N$ turns, each with the length of the circumference of a circle, $2\pi r$.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&l = N \cdot 2\pi r \\
&F = I l B \sin 90^\circ = I l B
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The radius in metres: $r = 1.3\,\text{cm} = 1.3 \cdot 0.01\,\text{m} = 0.013\,\text{m}$. The other quantities are in SI units.

<!-- vaihe -->

**Substitution.** First calculate the length of the wire and then the force:
```latex
\begin{aligned}
&l = N \cdot 2\pi r \\
&= 60 \cdot 2\pi \cdot 0.013\,\text{m} \\
&= 4.9009\,\text{m} \\[6pt]
&F = I l B \\
&= 1.5\,\text{A} \cdot 4.9009\,\text{m} \cdot 0.95\,\text{T} \\
&= 6.984\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** The force on the coil is $F \approx 7.0\,\text{N}$ along the axis of the coil. The result is given to two significant figures, like the radius $1.3\,\text{cm}$ and the current $1.5\,\text{A}$.

<!-- vaihe -->

**Reasonableness.** The units agree: $\text{A} \cdot \text{m} \cdot \text{T} = \text{A} \cdot \text{m} \cdot \tfrac{\text{N}}{\text{A}\cdot\text{m}} = \text{N}$. If the mass of the cone and the coil is about $10\,\text{g}$, their weight is only about $0.1\,\text{N}$, so the force is about $70$ times the weight. This is plausible, because the cone has to accelerate back and forth hundreds of times a second.

## Common misconception
Many people think that a magnet attracts a wire and that the wire moves along the field lines towards the other pole. The force is, however, **perpendicular** to the field, and a copper or aluminium wire experiences a force only when it carries a current. When the direction of the current is reversed, the wire moves in the opposite direction, although the magnet is the same. Another common mistake is to conclude from the charges that currents in the same direction repel each other. The force between wires is magnetic, and currents in the same direction attract each other. A third mistake is to use the cosine in the formula: the angle $\alpha$ is the angle between the wire and the field, and the force is zero when the wire is parallel to the field.

## Summary
- A magnetic field exerts on a current-carrying wire a force $F = I l B \sin\alpha$, where $\alpha$ is the angle between the wire and the field. The force is greatest when the wire is perpendicular to the field and zero when the wire is parallel to the field.
- The force is perpendicular to both the current and the field; its direction is given by the right-hand rule, and it reverses when the direction of the current or of the field reverses.
- Currents in the same direction attract each other, and currents in opposite directions repel each other. The force is $F = I_2 l B_1$, where $B_1 = \mu_0 I_1 : (2\pi r)$.
- In a direct-current motor the forces turn a current loop, and the commutator reverses the current every half turn.
- In a loudspeaker an alternating current in a radial field pushes the voice coil and the cone back and forth in step with the signal.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: headphones and a smartphone on a table. Each cup of the headphones contains a small loudspeaker, and sound waves spread from the cups." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy74s-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy74s-screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#1971c2"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="#f6f1e6"/>
  <rect x="0" y="270" width="600" height="90" fill="url(#fy74s-desk)"/>
  <path d="M180,230 C180,60 420,60 420,230" fill="none" stroke="#1f2933" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M180,230 C180,60 420,60 420,230" fill="none" stroke="#6c757d" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="146" y="196" width="68" height="96" rx="26" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="158" y="210" width="44" height="68" rx="18" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="386" y="196" width="68" height="96" rx="26" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="398" y="210" width="44" height="68" rx="18" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <path d="M138,202 A60,60 0 0 0 138,286" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M462,202 A60,60 0 0 1 462,286" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M121,185 A84,84 0 0 0 121,303" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M479,185 A84,84 0 0 1 479,303" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <rect x="270" y="236" width="70" height="108" rx="10" fill="#1f2933"/>
  <rect x="276" y="246" width="58" height="86" rx="4" fill="url(#fy74s-screen)"/>
  <path d="M296,270 v34 a8,8 0 1 1 -4,-7 v-27 l22,-6 v28 a8,8 0 1 1 -4,-7 v-18 Z" fill="#ffffff" stroke-linejoin="round"/>
</svg>
