# The generator and alternating current

> **Why** does the rotating rotor of a wind turbine produce in the electricity grid a voltage that reverses its direction a hundred times a second?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a wind farm in a Finnish field by the sea. In the middle is a large wind turbine with turning blades, and behind it are smaller turbines. On the right a power line on pylons runs to red houses. There are clouds in the sky, and the wind bends the tops of the birches." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A rotating coil in a magnetic field
In the chapter *Electromagnetic induction* a voltage was induced in a coil when the magnetic flux through it changed. A **generator** produces the change in flux by rotation: a coil is turned between the poles of a magnet. When the plane of the coil is perpendicular to the field, the greatest number of field lines pass through the coil and the flux is at its greatest, $\Phi = BA$. After a quarter of a turn the plane of the coil is parallel to the field, and not a single field line passes through it: the flux is zero. After the next quarter the field passes through the coil perpendicularly again, but from the other side of the coil, so the flux is $-BA$. In a rotating coil the flux thus varies smoothly and continuously between $BA$ and $-BA$.

<svg data-fig="generator" viewBox="0 0 600 360" role="img" aria-label="Schematic picture of an alternating-current generator, not to scale. At the top is the N pole of a magnet and at the bottom the S pole, so the magnetic field points downwards. Between the poles is a copper coil that is rotated about a horizontal axis. The ends of the wire of the coil are connected to two slip rings on the axis. Carbon brushes touch the rings, and wires run from the brushes to a lamp." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-generator.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="200" y="36.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="200" y="304.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="348" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="165" y="171.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{coil}$</div></foreignObject>
  <foreignObject x="365" y="81.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{brushes}$</div></foreignObject>
  <foreignObject x="372" y="267.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{slip rings}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/bicycle-dynamo.webp" alt="The front wheel of a bicycle and a round headlamp; a small silver bottle dynamo is pressed against the tyre."><figcaption>A bicycle dynamo is a small generator. The spindle turned by the tyre rotates a permanent magnet inside a coil. The coil stays still, but the magnetic flux through it changes, so an alternating voltage is induced in it.</figcaption></figure>

```pysahdy
A coil has an area of $0.010\,\text{m}^2$ and the magnetic flux density is $0.20\,\text{T}$. How great is the flux through the coil when its plane is perpendicular to the field, and how great is it after a quarter of a turn?
---
At first $\Phi = BA = 0.20\,\text{T} \cdot 0.010\,\text{m}^2 = 0.0020\,\text{Wb}$. After a quarter of a turn the plane of the coil is parallel to the field and no field line passes through it, so the flux is zero.
```

### Slip rings and brushes
The ends of the wire of the coil are connected to two **slip rings** on the axis. Carbon brushes touch the rings, and the voltage is led through the brushes to an external circuit, such as the lamp in the picture. Unlike the commutator of a direct-current motor in the chapter *Force on a current-carrying wire: the electric motor and the loudspeaker*, slip rings do not reverse the direction of the current, so the external circuit receives the voltage induced in the coil as it is.

### Why the voltage is sinusoidal
By the law of induction the voltage does not depend on how large the flux is, but on how fast it changes. In the graph of $\Phi(t)$ the rate of change is the steepness of the graph. When the flux is at its greatest, the sides of the coil move along the field lines, the flux hardly changes for a moment and the voltage is zero. When the plane of the coil is parallel to the field, the flux is zero, but the sides move perpendicular to the field lines and the flux changes fastest: the voltage is at its greatest. The flux varies like a cosine, and its steepness varies like a sine. In every half revolution the direction of the change in flux reverses, so the sign of the voltage also reverses. The result is an **alternating voltage**, and in a closed circuit an **alternating current** flows, whose direction reverses twice during every revolution.

<svg data-fig="phi-e" viewBox="0 0 600 440" role="img" aria-label="Two graphs on the same time axis for one period T. In the upper graph the green magnetic flux Phi starts from its greatest value BA, falls to zero at a quarter period, is at its smallest, minus BA, at half a period and returns to BA. In the lower graph the purple voltage e starts from zero, is greatest, e0, at a quarter period, zero at half a period and smallest, minus e0, at three quarters of a period. A dashed line at a quarter period shows that the voltage is greatest when the flux is zero. At the bottom are small pictures of the coil seen end-on: the field points to the right, and the plane of the coil is perpendicular to the field at time zero, parallel to the field at a quarter period, and so on." style="max-width:100%;font-size:24px">
  <line x1="208" y1="170" x2="208" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296" y1="170" x2="296" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="170" x2="384" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="170" x2="472" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="159" x2="500" y2="159" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="115" x2="500" y2="115" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="71" x2="500" y2="71" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="170" x2="514" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,170 L513,176 L513,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="171" x2="120" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,34 L126,47 L114,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="208" y1="170" x2="208" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166.5" y="179.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.25\,T$</div></foreignObject>
  <line x1="296" y1="170" x2="296" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="179.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.5\,T$</div></foreignObject>
  <line x1="384" y1="170" x2="384" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="342.5" y="179.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.75\,T$</div></foreignObject>
  <line x1="472" y1="170" x2="472" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="462" y="179.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="159" x2="120" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="144.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-BA$</div></foreignObject>
  <line x1="113" y1="115" x2="120" y2="115" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="88" y="100.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="113" y1="71" x2="120" y2="71" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="56.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$BA$</div></foreignObject>
  <foreignObject x="532" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="110" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Phi$</div></foreignObject>
  <polyline points="120,71 123,71 126,71 129,71.5 131.5,72 134.5,72.5 137.5,73 140.5,74 143.5,75 146.5,76 149.5,77 152.5,78 155,79.5 158,81 161,82.5 164,84 167,85.5 170,87.5 173,89 175.5,91 178.5,93 181.5,95 184.5,97 187.5,99 190.5,101.5 193.5,103.5 196,106 199,108 202,110.5 205,112.5 208,115 211,117.5 214,119.5 217,122 219.5,124 222.5,126.5 225.5,128.5 228.5,131 231.5,133 234.5,135 237.5,137 240,139 243,141 246,142.5 249,144.5 252,146 255,147.5 258,149 260.5,150.5 263.5,152 266.5,153 269.5,154 272.5,155 275.5,156 278.5,157 281.5,157.5 284,158 287,158.5 290,159 293,159 296,159 299,159 302,159 304.5,158.5 307.5,158 310.5,157.5 313.5,157 316.5,156 319.5,155 322.5,154 325,153 328,152 331,150.5 334,149 337,147.5 340,146 343,144.5 346,142.5 348.5,141 351.5,139 354.5,137 357.5,135 360.5,133 363.5,131 366.5,128.5 369,126.5 372,124 375,122 378,119.5 381,117.5 384,115 387,112.5 390,110.5 392.5,108 395.5,106 398.5,103.5 401.5,101.5 404.5,99 407.5,97 410.5,95 413,93 416,91 419,89 422,87.5 425,85.5 428,84 431,82.5 433.5,81 436.5,79.5 439.5,78 442.5,77 445.5,76 448.5,75 451.5,74 454.5,73 457,72.5 460,72 463,71.5 466,71 469,71 472,71" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="482" y="56.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\Phi$</div></foreignObject>
  <line x1="208" y1="330" x2="208" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296" y1="330" x2="296" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="330" x2="384" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="330" x2="472" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="320" x2="500" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="280" x2="500" y2="280" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="240" x2="500" y2="240" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="330" x2="514" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,330 L513,336 L513,324 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="331" x2="120" y2="216" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,204 L126,217 L114,217 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="208" y1="330" x2="208" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166.5" y="339.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.25\,T$</div></foreignObject>
  <line x1="296" y1="330" x2="296" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="339.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.5\,T$</div></foreignObject>
  <line x1="384" y1="330" x2="384" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="342.5" y="339.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.75\,T$</div></foreignObject>
  <line x1="472" y1="330" x2="472" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="462" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="320" x2="120" y2="320" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="305.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-e_0$</div></foreignObject>
  <line x1="113" y1="280" x2="120" y2="280" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="88" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="113" y1="240" x2="120" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$e_0$</div></foreignObject>
  <foreignObject x="532" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="110" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e$</div></foreignObject>
  <polyline points="120,280 123,278 126,276 129,273.5 131.5,271.5 134.5,269.5 137.5,267.5 140.5,265.5 143.5,263.5 146.5,262 149.5,260 152.5,258 155,256.5 158,255 161,253 164,251.5 167,250.5 170,249 173,247.5 175.5,246.5 178.5,245.5 181.5,244.5 184.5,243.5 187.5,242.5 190.5,242 193.5,241.5 196,241 199,240.5 202,240 205,240 208,240 211,240 214,240 217,240.5 219.5,241 222.5,241.5 225.5,242 228.5,242.5 231.5,243.5 234.5,244.5 237.5,245.5 240,246.5 243,247.5 246,249 249,250.5 252,251.5 255,253 258,255 260.5,256.5 263.5,258 266.5,260 269.5,262 272.5,263.5 275.5,265.5 278.5,267.5 281.5,269.5 284,271.5 287,273.5 290,276 293,278 296,280 299,282 302,284 304.5,286.5 307.5,288.5 310.5,290.5 313.5,292.5 316.5,294.5 319.5,296.5 322.5,298 325,300 328,302 331,303.5 334,305 337,307 340,308.5 343,309.5 346,311 348.5,312.5 351.5,313.5 354.5,314.5 357.5,315.5 360.5,316.5 363.5,317.5 366.5,318 369,318.5 372,319 375,319.5 378,320 381,320 384,320 387,320 390,320 392.5,319.5 395.5,319 398.5,318.5 401.5,318 404.5,317.5 407.5,316.5 410.5,315.5 413,314.5 416,313.5 419,312.5 422,311 425,309.5 428,308.5 431,307 433.5,305 436.5,303.5 439.5,302 442.5,300 445.5,298 448.5,296.5 451.5,294.5 454.5,292.5 457,290.5 460,288.5 463,286.5 466,284 469,282 472,280" fill="none" stroke="#7048e8" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="482" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$e$</div></foreignObject>
  <line x1="208" y1="60" x2="208" y2="170" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="208" y1="230" x2="208" y2="330" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="49.5" y="399.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <line x1="94" y1="418" x2="138" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M146,418 L137,422 L137,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="120" y1="375" x2="120" y2="409" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="120" cy="375" r="4" fill="#1f2933"/>
  <circle cx="120" cy="409" r="4" fill="#1f2933"/>
  <line x1="182" y1="418" x2="226" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M234,418 L225,422 L225,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="191" y1="392" x2="225" y2="392" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="191" cy="392" r="4" fill="#1f2933"/>
  <circle cx="225" cy="392" r="4" fill="#1f2933"/>
  <line x1="270" y1="418" x2="314" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M322,418 L313,422 L313,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="296" y1="409" x2="296" y2="375" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="296" cy="409" r="4" fill="#1f2933"/>
  <circle cx="296" cy="375" r="4" fill="#1f2933"/>
  <line x1="358" y1="418" x2="402" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M410,418 L401,422 L401,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="401" y1="392" x2="367" y2="392" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="401" cy="392" r="4" fill="#1f2933"/>
  <circle cx="367" cy="392" r="4" fill="#1f2933"/>
  <line x1="446" y1="418" x2="490" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M498,418 L489,422 L489,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="472" y1="375" x2="472" y2="409" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="472" cy="375" r="4" fill="#1f2933"/>
  <circle cx="472" cy="409" r="4" fill="#1f2933"/>
</svg>

<figure class="unit-photo"><img src="pics/fy7/generator-stator.webp" alt="A large round pit seen from above; a ring of coil windings runs around its walls, with yellow railings around the edges and tools on the floor."><figcaption>The stator of a hydroelectric generator with its rotor lifted out. The coils stay fixed around the ring, and a voltage is induced in them when the rotor carrying the magnetic poles turns inside.</figcaption></figure>

<figure class="unit-photo"><img src="pics/fy7/generator-rotor.webp" alt="A large reddish-brown cylinder stands on the floor of a brightly lit hall; it has vertical stripes around its rim, and equipment and people around it look small."><figcaption>The rotor of a pumped-storage plant's generator during maintenance at Coo-Trois-Ponts, Belgium. Around its rim are the poles of electromagnets. When the rotor turns inside the stator, the magnetic flux through the coils keeps changing.</figcaption></figure>

### The generator of a power plant and the wind turbine
In the large generators of power plants an electromagnet rotates and the coils stay in place around it. The flux through a stationary coil changes in the same way as in a rotating coil, so a similar alternating voltage arises, and a large current is obtained from the coils without sliding contacts. In a wind turbine the wind turns the rotor, and the shaft of the rotor turns the generator. The rotor turns slowly, about $10$–$15$ revolutions per minute, so the generator has either a gearbox that raises the rotation rate or a large number of magnetic poles. The wind speed varies, so a frequency converter changes the voltage of the generator to the grid frequency, $50\,\text{Hz}$. At the end of 2024 Finland had $1835$ wind turbines with a combined rated power of $8358\,\text{MW}$. In 2024 they produced $19.8\,\text{TWh}$ of electricity, about $24\,\%$ of Finland's electricity consumption (Suomen Uusiutuvat ry, wind power statistics 2024).

## Formula: The voltage of a generator
When a coil with $N$ turns and area $A$ rotates steadily in a uniform magnetic field $B$ at a rotation frequency $f$, and at the moment $t = 0$ the plane of the coil is perpendicular to the field, the flux through the coil and the voltage induced in it are
```kaavat
\Phi = BA\cos(2\pi f t)
sinusoidal alternating voltage as a function of time :: e = e_0 \sin(2\pi f t)
e_0 = NBA \cdot 2\pi f
```
where $\Phi$ is the magnetic flux through one turn (Wb), $e$ the instantaneous value of the voltage (V), $e_0$ the peak value of the voltage (V), $N$ the number of turns, $B$ the magnetic flux density (T), $A$ the area of the coil (m²) and $f$ the rotation frequency (Hz). The frequency of the voltage is the same as the rotation frequency, and the period is $T = 1 : f$. The flux changes unevenly during the rotation, so $e$ is the instantaneous voltage: it is greatest when the flux is zero and changes fastest, and zero when the flux is at its greatest.

```pysahdy
The coil of a generator rotates steadily $20$ turns per second. What are the frequency and the period of the voltage produced?
---
The frequency of the voltage is the same as the rotation frequency, $20\,\text{Hz}$. The period is $T = \tfrac{1}{f} = \tfrac{1}{20\,\text{Hz}} = 0.050\,\text{s}$.
```

### Where the peak value comes from
The peak value is obtained from the voltage of a moving conductor, $e = vBl$ (chapter *Electromagnetic induction*). The two sides of a rectangular coil, of length $l$, circle the axis at a radius $b : 2$, where $b$ is the width of the coil. The speed of the sides is $v = 2\pi f \cdot b : 2 = \pi f b$. Only the component of the velocity perpendicular to the field, $v \sin\theta$, contributes to the voltage, where $\theta$ is the angle between the velocity and the field. A voltage $B l v \sin\theta$ is induced in each side, and the voltages of the sides add up in a turn. In one turn the voltage is therefore $2 B l \cdot \pi f b \sin\theta = BA \cdot 2\pi f \sin\theta$, because $lb = A$, and in $N$ turns it is $N$ times as large. When $\theta = 90^\circ$, the plane of the coil is parallel to the field and the voltage is at its peak value $e_0 = NBA \cdot 2\pi f$. Doubling the rotation frequency doubles both the frequency and the peak value of the voltage, because the sides move twice as fast.

<svg data-fig="derive" viewBox="0 0 600 360" role="img" aria-label="Schematic picture, not to scale: the coil is seen along the axis. Horizontal green field lines point to the right. The plane of the coil is tilted, and its two sides, of length l, perpendicular to the paper, are shown as circles: the current in the lower right side goes into the paper and in the upper left side out of the paper. The velocities of the sides, blue arrows, are perpendicular to the plane of the coil and in opposite directions. The angle between the velocity of the right-hand side and the field is theta, and the component v sin theta of the velocity perpendicular to the field is drawn with a dashed line. The width of the coil is b." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-derive.webp" x="-1.3" y="-1.3" width="603" height="370.6" preserveAspectRatio="none"/>
  <foreignObject x="527" y="3.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="180" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$b$</span></div></foreignObject>
  <foreignObject x="404" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="23" y="209.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="350.5" y="197" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="406" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v\sin\theta$</div></foreignObject>
  <foreignObject x="264.5" y="250" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I$</span></div></foreignObject>
</svg>

### The rms value
The average of an alternating voltage over one period is zero, but a lamp or a resistor still heats up, because the power $p = ui$ is positive for both directions of the current. The power in a resistor varies between zero and the peak value $P_0 = U_0 I_0$, and its average is half of the peak value. The **rms value** (effective value) is the direct voltage or direct current that would deliver the same average power to a resistor:
```kaavat
rms value of a sinusoidal alternating voltage :: U = \frac{U_0}{\sqrt{2}}
rms value of a sinusoidal alternating current :: I = \frac{I_0}{\sqrt{2}}
```
where $U_0$ and $I_0$ are the **peak values** of the voltage and the current and $U$ and $I$ the rms values. When an alternating current passes through a purely resistive load, such as an ideal resistor, the current and the voltage are in phase. The average power can then be calculated from the rms values with the formula $P = UI$, as with direct current. In a general alternating-current circuit there can be a phase difference between the current and the voltage, and then the average power also depends on the power factor.

The $230\,\text{V}$ of a wall socket is an rms value: the peak value of the voltage is $230\,\text{V} \cdot \sqrt{2} \approx 325\,\text{V}$, and the frequency is $50\,\text{Hz}$, so the voltage reverses its direction a hundred times a second. Fingrid normally keeps the frequency of the national grid between $49.9$ and $50.1\,\text{Hz}$. Meters show the rms values of an alternating voltage and current.

<svg data-fig="power" viewBox="0 0 600 320" role="img" aria-label="Graph: the power p of a resistor as a function of time t over one period T, when a sinusoidal alternating voltage is connected to the resistor. The orange curve varies between zero and the peak value P0 and is zero at times 0, half a period and T, and at its peak at a quarter and three quarters of a period. The dashed line at half of P0 is the average of the power: the peaks of the curve above it are as large as the troughs below it." style="max-width:100%;font-size:24px">
  <line x1="202.5" y1="262" x2="202.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="262" x2="285" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367" y1="262" x2="367" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="449.5" y1="262" x2="449.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="168" x2="476" y2="168" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="74.5" x2="476" y2="74.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="262" x2="490" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,262 L489,268 L489,256 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="263" x2="120" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,26 L126,39 L114,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="202.5" y1="262" x2="202.5" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="271.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.25\,T$</div></foreignObject>
  <line x1="285" y1="262" x2="285" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250" y="271.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.5\,T$</div></foreignObject>
  <line x1="367" y1="262" x2="367" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="325.5" y="271.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.75\,T$</div></foreignObject>
  <line x1="449.5" y1="262" x2="449.5" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="439.5" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="168" x2="120" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="154" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{2}P_0$</div></foreignObject>
  <line x1="113" y1="74.5" x2="120" y2="74.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="60" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_0$</div></foreignObject>
  <foreignObject x="90" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="508" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="134" y="17.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$p$</span></div></foreignObject>
  <polygon points="120,168 120,262 122.5,261.5 125.5,260 128,257.5 131,254 133.5,249.5 136.5,244 139,238 142,231 144.5,223.5 147.5,215 150,206.5 153,197 155.5,187.5 158.5,178 161,168.5 164,158.5 166.5,149 169.5,139.5 172,130 175,121.5 177.5,113 180.5,105.5 183,98.5 186,92.5 188.5,87 191.5,82.5 194,79 197,76.5 199.5,75 202.5,74.5 205,75 208,76.5 210.5,79 213.5,82.5 216,87 219,92.5 221.5,98.5 224.5,105.5 227,113 230,121.5 232.5,130 235.5,139.5 238,149 241,158.5 243.5,168 246.5,178 249,187.5 252,197 254.5,206.5 257.5,215 260,223.5 263,231 265.5,238 268.5,244 271,249.5 274,254 276.5,257.5 279.5,260 282,261.5 285,262 287.5,261.5 290.5,260 293,257.5 296,254 298.5,249.5 301.5,244 304,238 307,231 309.5,223.5 312.5,215 315,206.5 318,197 320.5,187.5 323.5,178 326,168.5 329,158.5 331.5,149 334.5,139.5 337,130 340,121.5 342.5,113 345,105.5 348,98.5 350.5,92.5 353.5,87 356,82.5 359,79 361.5,76.5 364.5,75 367,74.5 370,75 372.5,76.5 375.5,79 378,82.5 381,87 383.5,92.5 386.5,98.5 389,105.5 392,113 394.5,121.5 397.5,130 400,139.5 403,149 405.5,158.5 408.5,168 411,178 414,187.5 416.5,197 419.5,206.5 422,215 425,223.5 427.5,231 430.5,238 433,244 436,249.5 438.5,254 441.5,257.5 444,260 447,261.5 449.5,262 449.5,168" fill="#ffc078" fill-opacity="0.3"/>
  <polyline points="120,262 122.5,261.5 125.5,260 128,257.5 131,254 133.5,249.5 136.5,244 139,238 142,231 144.5,223.5 147.5,215 150,206.5 153,197 155.5,187.5 158.5,178 161,168.5 164,158.5 166.5,149 169.5,139.5 172,130 175,121.5 177.5,113 180.5,105.5 183,98.5 186,92.5 188.5,87 191.5,82.5 194,79 197,76.5 199.5,75 202.5,74.5 205,75 208,76.5 210.5,79 213.5,82.5 216,87 219,92.5 221.5,98.5 224.5,105.5 227,113 230,121.5 232.5,130 235.5,139.5 238,149 241,158.5 243.5,168 246.5,178 249,187.5 252,197 254.5,206.5 257.5,215 260,223.5 263,231 265.5,238 268.5,244 271,249.5 274,254 276.5,257.5 279.5,260 282,261.5 285,262 287.5,261.5 290.5,260 293,257.5 296,254 298.5,249.5 301.5,244 304,238 307,231 309.5,223.5 312.5,215 315,206.5 318,197 320.5,187.5 323.5,178 326,168.5 329,158.5 331.5,149 334.5,139.5 337,130 340,121.5 342.5,113 345,105.5 348,98.5 350.5,92.5 353.5,87 356,82.5 359,79 361.5,76.5 364.5,75 367,74.5 370,75 372.5,76.5 375.5,79 378,82.5 381,87 383.5,92.5 386.5,98.5 389,105.5 392,113 394.5,121.5 397.5,130 400,139.5 403,149 405.5,158.5 408.5,168 411,178 414,187.5 416.5,197 419.5,206.5 422,215 425,223.5 427.5,231 430.5,238 433,244 436,249.5 438.5,254 441.5,257.5 444,260 447,261.5 449.5,262" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="120" y1="168" x2="449.5" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="459.5" y="154" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mean}$</div></foreignObject>
</svg>

```pysahdy
The peak value of a sinusoidal alternating current through a resistor is $2.0\,\text{A}$. What is the rms value of the current?
---
The rms value is the peak value divided by $\sqrt{2}$: $I = \tfrac{I_0}{\sqrt{2}} = \tfrac{2.0\,\text{A}}{\sqrt{2}} \approx 1.4\,\text{A}$.
```

## Worked example
The coil of a generator used for teaching has $250$ turns, and the sides of the rectangular coil are $4.0\,\text{cm}$ and $5.0\,\text{cm}$ long. The coil rotates in a uniform magnetic field whose magnetic flux density is $0.18\,\text{T}$, and it makes $12$ revolutions per second. How large is the rms value of the alternating voltage induced in the coil?

<!-- vaihe -->

**Given and find.** The number of turns is $N = 250$, the sides of the coil are $4.0\,\text{cm}$ and $5.0\,\text{cm}$, the magnetic flux density is $B = 0.18\,\text{T}$ and the rotation frequency is $f = 12\,\text{Hz}$. We are asked for the rms value $U$ of the voltage.

<!-- vaihe -->

**Principle.** The coil rotates steadily in a uniform field, so a sinusoidal alternating voltage is induced in it, with peak value $e_0 = NBA \cdot 2\pi f$. The rms value of a sinusoidal voltage is the peak value divided by $\sqrt{2}$.

<!-- vaihe -->

**Formula solved.**
```kaavat
peak value of the sinusoidal voltage induced in a generator coil :: e_0 = NBA \cdot 2\pi f
U = \frac{e_0}{\sqrt{2}} = \frac{NBA \cdot 2\pi f}{\sqrt{2}}
```

<!-- vaihe -->

**Unit conversions.** The area in square metres: $A = 4.0 \cdot 0.01\,\text{m} \cdot 5.0 \cdot 0.01\,\text{m} = 0.0020\,\text{m}^2$. The rotation frequency is $12$ revolutions per second, that is $f = 12\,\text{Hz}$.

<!-- vaihe -->

**Substitution.** First calculate the peak value and then the rms value:
```latex
\begin{aligned}
&e_0 = NBA \cdot 2\pi f \\
&= 250 \cdot 0.18\,\text{T} \cdot 0.0020\,\text{m}^2 \\
&\quad \cdot 2\pi \cdot 12\,\tfrac{1}{\text{s}} \\
&= 6.786\,\text{V} \\[6pt]
&U = \frac{6.786\,\text{V}}{\sqrt{2}} \\
&= 4.798\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Result.** The rms value of the voltage is $U \approx 4.8\,\text{V}$ and the peak value is about $6.8\,\text{V}$. The result is given to two significant figures, like the dimensions of the coil and the magnetic flux density.

<!-- vaihe -->

**Reasonableness.** The units fit: $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. With round numbers $250 \cdot 0.2\,\text{T} \cdot 0.002\,\text{m}^2 \cdot 6 \cdot 10\,\tfrac{1}{\text{s}} \approx 6\,\text{V}$, which fits the peak value. The rms value is smaller than the peak value, as it should be. A voltage of a few volts is of the same order of magnitude as the voltage of a bicycle dynamo.

## Common misconception
Many think that the voltage is greatest when the most field lines pass through the coil, that is, when the plane of the coil is perpendicular to the field. The voltage is then, however, **zero**, because the flux is not changing at that moment. The voltage is greatest when the plane of the coil is parallel to the field and the flux is zero, because then the flux changes fastest. Another common mistake is to take the $230\,\text{V}$ of the wall socket as the greatest value of the voltage. It is an rms value, and the voltage swings between $-325\,\text{V}$ and $325\,\text{V}$. A third mistake is to conclude that alternating current does not transfer energy because its average is zero. The power is positive for both directions of the current.

## Summary
- In a generator a coil rotates in a magnetic field (or a magnet rotates inside a coil), and the flux through the coil, $\Phi = BA\cos(2\pi f t)$, varies continuously.
- The induced voltage depends on the rate of change of the flux: it is zero when the flux is at its greatest, and greatest when the plane of the coil is parallel to the field and the flux is zero.
- A sinusoidal alternating voltage $e = e_0 \sin(2\pi f t)$ arises, with peak value $e_0 = NBA \cdot 2\pi f$ and the same frequency as the rotation frequency.
- The rms value of a sinusoidal alternating voltage is $U = U_0 : \sqrt{2}$ and $I = I_0 : \sqrt{2}$, and the average power of a resistive load is $P = UI$. The peak value of the mains voltage $230\,\text{V}$ is about $325\,\text{V}$ and its frequency is $50\,\text{Hz}$.
- The rotor of a wind turbine turns the generator, and a frequency converter matches the voltage to the frequency of the grid.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a cyclist rides in the evening dusk. In the hub of the front wheel is a dynamo that gives the lamp an alternating voltage, and the beam of the lamp lights the road in front of the bicycle." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
