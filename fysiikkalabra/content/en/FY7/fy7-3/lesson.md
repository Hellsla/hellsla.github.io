# Magnetic field of a wire and a coil

> **Why** can the magnet of a scrapyard crane lift a tonne of scrap car into the air and drop it at the press of a button, when a fridge magnet never lets go?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a scrapyard crane. From the end of the boom of the crane a round grey electromagnet hangs on chains; it holds a rusty scrap car by its bottom and lifts it off a heap of scrap. In the background are heaps of scrap and the sky." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### An electric current creates a magnetic field
In 1820 the Danish physicist Hans Christian Ørsted noticed during a lecture that a compass needle turned when a current was switched on in a wire next to it. When the current was switched off, the needle went back to pointing north. The observation joined electricity and magnetism: **every current-carrying wire has a magnetic field around it**. The field is created by moving charges, so the wire does not have to be made of a magnetic material; even a copper wire creates a field. When the current grows, the field becomes stronger, and when the direction of the current is reversed, the direction of the field is reversed too.

The field lines of a straight wire are concentric circles around the wire, perpendicular to it. The field therefore does not point away from the wire or towards it, but goes round it. Compasses placed around the wire turn along the tangent of the circle when the field of the wire is much stronger than the Earth's magnetic field. The farther from the wire we are, the weaker the field.

<svg data-fig="wire-field" viewBox="0 0 600 372" role="img" aria-label="Schematic figure, not to scale, in two parts. On the left a vertical current-carrying wire through a table top seen from the side: a purple arrow shows the current upwards, and around the wire there are three green circular field lines whose arrows go round anticlockwise seen from above. On the right the same situation from above: the wire is a dot inside a circle, because the current comes towards the viewer, and around it there are three concentric field lines going anticlockwise. Four compasses on a field line: the north end of each needle, pink, points in the direction of the field line." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-wire-field.webp" x="0" y="1.2" width="600" height="380" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{from the side}$</div></foreignObject>
  <foreignObject x="390" y="9.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{from above}$</div></foreignObject>
  <foreignObject x="186" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="250" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="470" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="554" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/compass-needles-wire.webp" alt="A blue wire passes through a board, surrounded by four rows of small compass needles."><figcaption>Small compass needles around a current-carrying wire. Close to the wire, the needles turn along the field lines that circle the wire.</figcaption></figure>

### The right-hand rule
The direction in which the field goes round is given by the **right-hand rule**: when the thumb of the right hand points in the direction of the current, the curled fingers go round in the direction of the field lines. In the figure the current goes upwards, so seen from above the field goes round anticlockwise. In figures a current towards the viewer is marked with a dot $\odot$ and a current away from the viewer with a cross $\otimes$, like the tip and the tail feathers of an arrow.

```pysahdy
In a vertical wire the current flows downwards. In which direction does the field of the wire go round when you look at the wire from above?
---
The thumb points in the direction of the current, that is, down, so the fingers curl clockwise seen from above. The field therefore goes round clockwise.
```

### The field of a coil
When a wire is wound into a spiral, called a **coil**, the field of each turn points the same way inside the coil, and the fields strengthen each other. Inside a long coil the field lines are almost straight and evenly spaced: the field is almost uniform and parallel to the axis of the coil. At the ends of the coil the field lines spread out, and outside the coil the field is like that of a bar magnet in the chapter *Magnets, the magnetic dipole and the magnetic field*. The end from which the field lines emerge is the north pole N. The right-hand rule works for a coil like this: when the fingers curl along the turns in the direction of the current, the thumb points inside the coil in the direction of the field, that is, towards the north pole.

<svg data-fig="coil-field" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale: a long coil cut along its length. The wire cross-sections in the upper row have a dot (current towards the viewer) and those in the lower row a cross (current away from the viewer). Inside the coil the green field lines are straight, evenly spaced and pointing to the right, so the field is almost uniform. Outside, the field lines curve from the right end back to the left. The right end is the north pole N and the left end the south pole S, as in a bar magnet." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-coil-field.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="492" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="89" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="372" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{B}$</span></div></foreignObject>
  <foreignObject x="90" y="9.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current: } \odot \text{ towards the viewer, } \otimes \text{ away}$</div></foreignObject>
  <foreignObject x="100" y="321.5" width="400" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{almost uniform field inside}$</div></foreignObject>
</svg>

```pysahdy
In a long coil the current goes round clockwise seen from end $P$ of the coil. Is end $P$ the north or the south pole of the coil?
---
When the fingers of the right hand curl along the turns in the direction of the current, the thumb points in the direction of the field, and here it points away from end $P$. The field lines emerge from the other end, so that end is the north pole and end $P$ is the south pole.
```

### The electromagnet
When an iron core is pushed inside a coil, the field becomes many times stronger. The field of the coil turns the magnetic domains of the iron to point the same way, and the magnetised iron adds its own field to the field of the coil. A coil like this is an **electromagnet**. When the current is switched off, the field of the coil disappears, and the domains of soft iron return almost to disorder, so the core loses almost all of its magnetisation. That is why the scrapyard crane holds the scrap only as long as the current flows. A permanent magnet, by contrast, is made of a material whose domains stay aligned, so it cannot be switched off.

<svg data-fig="electromagnet" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale: an electromagnet. A copper coil is wound round a vertical grey iron core, and the wires of the coil go to a battery and a switch. On the left the switch is closed and a current flows: the lower end of the iron core attracts iron nails, which hang from it in a chain. On the right the same electromagnet with the switch open: the blade of the switch is lifted off its contact, the circuit is broken and the nails have fallen onto the table." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-electromagnet.webp" x="1.2" y="1.2" width="597" height="366.9" preserveAspectRatio="none"/>
  <foreignObject x="71" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current flows}$</div></foreignObject>
  <foreignObject x="333.5" y="9.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current switched off}$</div></foreignObject>
  <foreignObject x="191" y="221.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="56" y="145.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{iron}$</div></foreignObject>
  <foreignObject x="342" y="145.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{iron}$</div></foreignObject>
</svg>

## Formula: Magnetic field of a straight wire and of a coil
The magnetic flux density of a long straight wire at a distance $r$ from the wire is
```kaavat
magnetic flux density of a straight current-carrying wire :: B = \frac{\mu_0 I}{2\pi r}
```
where $B$ is the magnetic flux density (T), $I$ the current in the wire (A), $r$ the distance from the wire (m) and $\mu_0 \approx 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$ the permeability of free space, a constant of nature. In air the same value is used. The field is directly proportional to the current and inversely proportional to the distance: doubling the distance halves the field. The formula holds when the wire is much longer than the distance $r$ and other wires are far away. For example, the field of a $10\,\text{A}$ wire at a distance of $1\,\text{cm}$ is $200\,\mu\text{T}$, about four times the Earth's magnetic field of about $50\,\mu\text{T}$.

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
```kaavat
magnetic flux density of a long solenoid :: B = \mu_0 \frac{N I}{l}
```
where $N$ is the number of turns of the coil, $I$ the current (A) and $l$ the length of the coil (m). The field depends on the turn density $N : l$, that is, on how many turns there are per metre, and not on the thickness of the coil. The formula holds when the coil is much longer than it is wide and has only air inside it. At the ends of the coil the field is about half of its value at the centre, and an iron core makes the field many times stronger.

<svg data-fig="coil-dims" viewBox="0 0 600 330" role="img" aria-label="Schematic figure, not to scale: a coil seen from the side. The coil has N turns of copper wire over a length l. A current I, marked with a purple arrow, flows from the ends of the wire. Inside the coil a green arrow points along the axis; its label B is on the left of the coil, level with the arrow." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-coil-dims.webp" x="0" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="73" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="60" y="253.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="255" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l$</div></foreignObject>
  <foreignObject x="426" y="135.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N\ \text{turns}$</div></foreignObject>
</svg>

```pysahdy
A long coil has $500$ turns and its length is $0.250\,\text{m}$. A current of $1.00\,\text{A}$ flows in it. What is the magnetic flux density at the middle of the coil?
---
By the formula $B = \mu_0 \tfrac{N I}{l} = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \cdot \tfrac{500 \cdot 1.00\,\text{A}}{0.250\,\text{m}} \approx 2.51\,\text{mT}$.
```

### Determining the magnetic flux density inside a coil
The field is measured with a magnetic field sensor whose tip is placed at the centre of the coil, parallel to the axis. The current is varied with a power supply, and at each current the current and the reading $B$ of the sensor are recorded. When the measurements are plotted in an $(I, B)$ graph, for example with the Vernier Graphical Analysis program, a straight line $B = A I + B_0$ is fitted to them. According to the formula the slope is $A = \mu_0 \tfrac{N}{l}$, so the measurement gives an estimate for the permeability of free space, $\mu_0 = A l : N$. When the uncertainty of the slope is $\Delta A$ and that of the length $\Delta l$, the relative uncertainty of the result is estimated by adding the relative uncertainties of the factors: $\Delta \mu_0 : \mu_0 = \Delta A : A + \Delta l : l$. The constant term $B_0$ is usually small: it is affected by the zero point of the sensor and by the Earth's magnetic field.

## Worked example
A school coil has $600$ turns and its length is $15.0\,\text{cm}$. A current of $2.50\,\text{A}$ flows in the coil. How great is the magnetic flux density at the centre of the coil? How many times greater is it than the Earth's magnetic field of $50\,\mu\text{T}$? The coil is long compared with its width, and it has air inside it.

<!-- vaihe -->

**Given and asked.** Number of turns $N = 600$, length of the coil $l = 15.0\,\text{cm}$, current $I = 2.50\,\text{A}$ and the constant $\mu_0 \approx 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$.

We are asked for the magnetic flux density $B$ at the centre of the coil and its ratio to the Earth's field $B_\text{Earth} = 50\,\mu\text{T}$.

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

**Reasonableness.** The turn density is $600 : 0.150\,\text{m} = 4000$ turns per metre. One ampere and a thousand turns per metre give about $1.3\,\text{mT}$, so $2.5\,\text{A}$ and four times the density give about $1.3\,\text{mT} \cdot 2.5 \cdot 4 = 13\,\text{mT}$.

The result is about $250$ times the Earth's field, so the field of the coil is easy to measure, and it is clearly smaller than the roughly $1.5\,\text{T}$ of an MRI scanner, which needs a superconducting coil and a current of hundreds of amperes.

## Common misconception
Many people think that the magnetic field of a current-carrying wire points away from the wire, like the electric field of a charged wire. The field lines, however, go round the wire as closed circles, and they have neither a starting point nor an end point. A compass next to the wire therefore turns across the wire, not towards it.

Another mistake is to think that the field of a coil depends on the total number of turns. If the same coil of $200$ turns is stretched to twice its length, the turn density $N : l$ is halved and the field at the centre of the coil is about halved, even though there are just as many turns. A third mistake is to forget that the formula for a long coil does not hold at the ends of the coil: there the field is only about half of its value at the centre.

## Summary
- An electric current creates a magnetic field around it (Ørsted 1820). The field lines of a straight wire are circles going round the wire, and their direction is given by the right-hand rule: thumb in the direction of the current, fingers in the direction of the field.
- The field of a long straight wire is $B = \tfrac{\mu_0 I}{2\pi r}$: it grows with the current and weakens as the distance grows.
- Inside a long coil the field is almost uniform, $B = \mu_0 \tfrac{N I}{l}$. It depends on the turn density $N : l$ and the current. Outside, the field of the coil is like that of a bar magnet.
- An iron core turns a coil into an electromagnet, whose field is many times stronger and which can be switched on and off.
- By measuring $B$ as a function of the current and fitting a straight line, we get $\mu_0 = A l : N$ from the slope.
