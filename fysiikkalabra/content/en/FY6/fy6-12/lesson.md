# Potential energy and potential in an electric field

> **Why** are the electrons plunging into the upper atmosphere in the aurora so fast that they make the air glow?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the aurora over wintry Lapland. Green aurora curtains arch across a dark starry sky, and the vertical rays glow brightest at their lower edge. Below are snowy fells, a spruce forest and a red cabin with a warm light shining from its window." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### An electric field does work like gravity
In a uniform electric field the same force $\overline{F} = q\overline{E}$ acts on a charged particle everywhere between the plates (chapter *Uniform electric field*). The situation resembles gravity near the surface of the Earth, where the weight $m\overline{g}$ of a ball is the same at every height. When a ball falls from a height $h$, the weight does the work $W = mgh$, and the potential energy of the ball changes into kinetic energy (chapter *Kinetic energy, potential energy and mechanical energy*). In the same way, when a positive charge $q$ travels from the positive plate to the negative plate in the direction of the field a distance $d$, the electric force does the work $W = Fd = qEd$. The force and the displacement are in the same direction, so the work is positive.

<svg data-fig="kentta" viewBox="0 0 600 340" role="img" aria-label="Two parallel schematic figures, not to scale. On the left a ball is at a height h above the ground, and a red weight m times g acts downward on it. When the ball falls to the ground, the weight does the work W = mgh. On the right are two horizontal metal plates: the upper one positive and the lower one negative, with the plate separation d. Between the plates there is a uniform electric field E whose field lines point downward. A positive charge q is attached to the positive plate, and a red force q times E acts downward on it. When the charge travels from one plate to the other, the electric force does the work W = qEd." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-12-kentta.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="124" y="133.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$m\overline{g}$</div></foreignObject>
  <foreignObject x="226" y="162.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="80" y="291.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = mgh$</div></foreignObject>
  <foreignObject x="306" y="53.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="306" y="253.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="384" y="181.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="452" y="133.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$q\overline{E}$</div></foreignObject>
  <foreignObject x="574" y="153.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="380" y="291.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = qEd$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/lightning-dallas.webp" alt="A blue night sky and a thundercloud from which a branching lightning bolt runs sideways through the cloud and down to a mast on the ground."><figcaption>Lightning strikes a mast in Dallas. The potential difference between a thundercloud and the ground can be tens or hundreds of millions of volts. When charge is discharged across it, electric potential energy turns into light, sound and internal energy of the air, which is transferred to the surroundings as heat.</figcaption></figure>

### Electric potential energy
The electric force is conservative like gravity: the work it does depends only on the initial and final points, not on the path. So a charge in a field has **potential energy** $E_\text{p}$, which depends on its position. When the field does positive work, the potential energy decreases by the same amount. When a charge is moved against the force of the field, the potential energy increases. The zero level of the potential energy is chosen freely, like the zero level of height: often it is the negative plate or an earthed point. Only the changes of the potential energy matter, and they do not depend on the choice of the zero level.

```pysahdy
Does the choice of the zero level affect how much work the field does when a charge moves from one point to another?
---
No. The work done by the field equals the decrease in potential energy, $W = -\Delta E_\text{p}$, and moving the zero level changes the initial and final energies by the same amount, so the difference stays the same.
```

### Potential: energy per unit charge
A double charge experiences a double force, so at the same point it has a double potential energy. The ratio $E_\text{p} : q$ therefore does not depend on the charge but describes the point in the field. It is called the **potential** $V$ of the point, and its unit is $1\,\text{J/C} = 1\,\text{V}$. This is the same potential as in the chapter *Kirchhoff's laws and potential in a circuit*: the voltage of a point relative to the chosen zero point. The **potential difference** of two points is the voltage between them.

Between the plates the potential grows steadily from the negative plate to the positive one. When the negative plate is the zero point, the potential of the positive plate is the voltage $U$ between the plates. The field always points from a higher potential to a lower one. Points with the same potential form an **equipotential surface**. Between the plates the equipotential surfaces are planes parallel to the plates, and the field lines are perpendicular to them. When a charge is moved along an equipotential surface, the field does no work, because the force is perpendicular to the displacement.

<svg data-fig="tasapotentiaali" viewBox="0 0 600 340" role="img" aria-label="Schematic figure to scale: two horizontal metal plates 4.0 centimetres apart. The upper plate is positive and its potential is 200 V; the lower, negative plate is the zero point, 0 V. Between the plates are grey dashed lines with potentials 150 V, 100 V and 50 V; the lines are 1.0 centimetre apart. Green field lines E point from top to bottom and cross the dashed lines perpendicularly. The potential decreases by 50 V for every centimetre in the direction of the field." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-12-tasapotentiaali.webp" x="35.5" y="4.7" width="568.7" height="332.9" preserveAspectRatio="none"/>
  <foreignObject x="70" y="100.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="155.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="210.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="45.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="265.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="242" y="128" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="512" y="238" width="78" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1.0\,\text{cm}$</div></foreignObject>
  <foreignObject x="512" y="73" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$50\,\text{V}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/lightning-strikes.webp" alt="A dim blue sky over flat countryside; several branching lightning bolts on the distant horizon and a power pylon on the right."><figcaption>Lightning in a summer evening sky. The lower part of a thundercloud is usually negatively charged, so its potential is lower than that of the ground. In a lightning strike electrons move towards the higher potential, and their potential energy decreases.</figcaption></figure>

### Positive and negative charge
A positive charge starts moving from rest in the direction of the field, that is, toward a lower potential, and its potential energy decreases. The charge of an electron is negative, $q = -e$, so the force on it points against the field: the electron starts toward a higher potential. Its potential energy decreases then too, because the potential energy of a negative charge is the lower the higher the potential. At the same point of $150\,\text{V}$ the potential energy of a proton is positive and that of an electron negative. **Each charge starts moving from rest in the direction in which its potential energy decreases**, like a ball falling downward.

### The electronvolt
When a particle whose charge has the magnitude of the elementary charge $e$ travels through a potential difference $U$, the field does the work $eU$. If only the electric force does work, the kinetic energy of the particle increases by the same amount. The energies of particles are therefore often given in **electronvolts** ($\text{eV}$): one electronvolt is the energy that a charge of the magnitude of the elementary charge gets when it travels through a potential difference of $1\,\text{V}$. When a proton and an electron travel from rest through a potential difference of $200\,\text{V}$, each gets a kinetic energy of $200\,\text{eV}$, although they move in opposite directions. For each, the sum of the kinetic energy and the potential energy stays the same all the way.

```pysahdy
A particle with a charge of the size of the elementary charge starts from rest and passes through a potential difference of $45\,\text{V}$. How large a kinetic energy does it gain, in electronvolts?
---
If only the electric force does work, the kinetic energy is $eU$, that is $45\,\text{eV}$.
```

<svg data-fig="energia" viewBox="0 0 600 380" role="img" aria-label="Bar chart to scale: energy in electronvolts when a particle starts from rest and travels through the potential difference of 200 volts between the plates. On the left a proton that starts from the positive plate: at the start its potential energy is 200 eV and its kinetic energy zero; at the end at the negative plate the potential energy is zero and the kinetic energy 200 eV. On the right an electron that starts from the negative plate: at the start both energies are zero; at the end at the positive plate the potential energy is minus 200 eV and the kinetic energy 200 eV. For each particle the sum of the energies stays the same. The bars of the potential energy are dark and those of the kinetic energy orange." style="max-width:100%;font-size:24px">
  <line x1="78" y1="306" x2="78" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M78,50 L84,63 L72,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="68" y="19.5" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{eV})$</div></foreignObject>
  <line x1="71" y1="70" x2="78" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="12" y="55.5" width="54" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="71" y1="180" x2="78" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="12" y="165.5" width="54" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="71" y1="290" x2="78" y2="290" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="12" y="275.5" width="54" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-200$</div></foreignObject>
  <line x1="78" y1="180" x2="584" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="338" y1="24" x2="338" y2="366" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="181" y="15.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{proton}$</div></foreignObject>
  <rect x="108" y="70" width="42" height="110" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="107" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <line x1="158" y1="180" x2="200" y2="180" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="157" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="99" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at the start}$</div></foreignObject>
  <line x1="230" y1="180" x2="272" y2="180" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="229" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <rect x="280" y="70" width="42" height="110" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="279" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="221" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at the end}$</div></foreignObject>
  <foreignObject x="435" y="15.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{electron}$</div></foreignObject>
  <line x1="362" y1="180" x2="404" y2="180" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="361" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <line x1="412" y1="180" x2="454" y2="180" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="411" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="353" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at the start}$</div></foreignObject>
  <rect x="484" y="180" width="42" height="110" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="483" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <rect x="534" y="70" width="42" height="110" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="533" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="475" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at the end}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/plasma-lamp.webp" alt="A glass plasma ball in the dark: a glowing sphere in the centre with violet and red discharge filaments reaching out to the inside of the glass."><figcaption>The central electrode of a plasma ball carries a high-frequency alternating voltage of several kilovolts. Electrons in the thin gas are accelerated by the electric field, and when they collide with gas atoms they make the atoms emit light, much as in the aurora.</figcaption></figure>

### The aurora
The magnetic field of the Earth guides electrons coming from space to the polar regions. At a height of thousands of kilometres the electrons often travel through a potential difference of a few kilovolts, and every volt gives the electron one electronvolt of kinetic energy. A potential difference of $5\,\text{kV}$ gives a kinetic energy of $5\,\text{keV}$ and a speed of about $40\,000\,\text{km/s}$. The mass of an electron is so small that even such an energy gives it an enormous speed. At a height of about $100$–$300\,\text{km}$ the electrons collide with the oxygen and nitrogen atoms and molecules of the air and give them their energy, and these radiate the energy as light. The green light comes from oxygen.

## Formula: Electric potential energy and potential
The potential of a point is the potential energy of a charge per unit charge. From it we get the potential energy of a charge at a point whose potential is $V$:
```kaavat
electric potential :: V = \frac{E_\text{p}}{q}
:: E_\text{p} = qV
```
where $E_\text{p}$ is the potential energy ($\text{J}$), $q$ the charge with its sign ($\text{C}$) and $V$ the potential of the point ($\text{V}$) relative to the chosen zero point. For an electron $q = -e$.

When a charge moves from point $A$ to point $B$, the electric force does the work
```kaavat
work done by an electric field :: W_{AB} = q(V_A - V_B) = qU_{AB}
```
where $W_{AB}$ is the work ($\text{J}$) and $U_{AB} = V_A - V_B$ is the potential difference, or voltage, of the points ($\text{V}$). The work equals the decrease of the potential energy $E_{\text{p},A} - E_{\text{p},B}$, and it does not depend on the path. In a uniform field the voltage between the plates is $U = Ed$ (chapter *Uniform electric field*), so the field does the work $qU = qEd$ on a charge travelling from one plate to the other in the direction of the field.

```pysahdy
A charge of $2.0\,\text{nC}$ moves from a point at potential $90\,\text{V}$ to a point at potential $40\,\text{V}$. How much work does the electric force do?
---
The work is $W_{AB} = q(V_A - V_B)$. With the values, $V_A - V_B = 90\,\text{V} - 40\,\text{V} = 50\,\text{V}$ and $W_{AB} = 2.0 \cdot 10^{-9}\,\text{C} \cdot 50\,\text{V}$, so $W_{AB} = 1.0 \cdot 10^{-7}\,\text{J}$.
```

When the negative plate is the zero point, the potential of a uniform field is
```latex
V = Ex
```
where $E$ is the field strength ($\text{V/m}$) and $x$ the distance of the point from the negative plate ($\text{m}$). The graph $(x, V)$ is a straight line whose slope is the field strength. Between the plates in the figure the potential changes by $100\,\text{V}$ over a distance of $2.0\,\text{cm}$, so $E = 100\,\text{V} : 0.020\,\text{m} = 5000\,\text{V/m}$.

<svg data-fig="vx-graph" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: potential V in volts as a function of the distance x in centimetres, when x is measured from the negative plate, whose potential is zero. The plate separation is 4.0 cm and the voltage 200 V. The graph is a rising straight line through the origin that ends at the positive plate at the point (4.0 cm; 200 V). The slope triangle shows that over a distance of two centimetres the potential changes by 100 V, so the field strength is 5000 V/m." style="max-width:100%;font-size:24px">
  <line x1="186.5" y1="280" x2="186.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272.5" y1="280" x2="272.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="280" x2="359" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="445.5" y1="280" x2="445.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="227.5" x2="480" y2="227.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="175.5" x2="480" y2="175.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="123" x2="480" y2="123" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="71" x2="480" y2="71" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="280" x2="494" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,280 L493,286 L493,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="281" x2="100" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,24 L106,37 L94,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186.5" y1="280" x2="186.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="272.5" y1="280" x2="272.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="262.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="359" y1="280" x2="359" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="349" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="445.5" y1="280" x2="445.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="435.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="93" y1="227.5" x2="100" y2="227.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="213" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="93" y1="175.5" x2="100" y2="175.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="161" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="123" x2="100" y2="123" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="108.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="93" y1="71" x2="100" y2="71" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="56.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="70" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="265.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{cm})$</div></foreignObject>
  <foreignObject x="114" y="15.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$V\ (\text{V})$</span></div></foreignObject>
  <polyline points="100,280 445.5,71" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="445.5" cy="71" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="186.5" y1="227.5" x2="359" y2="227.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="359" y1="227.5" x2="359" y2="123" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="187.5" y="235" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta x = 2.0\,\text{cm}$</span></div></foreignObject>
  <foreignObject x="371" y="161" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta V = 100\,\text{V}$</span></div></foreignObject>
  <foreignObject x="233.5" y="32.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{positive plate}$</div></foreignObject>
</svg>

When only the electric force does work, the sum of the kinetic energy and the potential energy is conserved. A particle starting from rest has, after travelling through a potential difference $U$, the kinetic energy
```latex
\frac{1}{2}mv^2 = |q|U
```
where $m$ is the mass of the particle ($\text{kg}$), $v$ its speed ($\text{m/s}$) and $|q|$ the magnitude of the charge ($\text{C}$). Gravity is ignored: for example, the weight of a proton in the field of the figure is tens of billions of times smaller than the electric force. The unit of energy of particles, the electronvolt, is
```latex
1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}
```
because $$1.602 \cdot 10^{-19}\,\text{C} \cdot 1\,\text{V} = 1.602 \cdot 10^{-19}\,\text{J}$$. So $1\,\text{keV} = 1000\,\text{eV}$.

## Worked example
An aurora electron starts almost from rest and travels toward a higher potential through a potential difference of $3.0\,\text{kV}$. What are the kinetic energy of the electron in electronvolts and in joules, and its speed? The charge of the electron is $-e$, where $e = 1.602 \cdot 10^{-19}\,\text{C}$, and its mass is $m = 9.109 \cdot 10^{-31}\,\text{kg}$. Forces other than the electric force are ignored.

<!-- vaihe -->

**Given and find.** $U = 3.0\,\text{kV}$, $e = 1.602 \cdot 10^{-19}\,\text{C}$, $m = 9.109 \cdot 10^{-31}\,\text{kg}$ and initial speed zero. We are asked for the kinetic energy $E_\text{k}$ in electronvolts and in joules and for the speed $v$.

<!-- vaihe -->

**Principle.** Only the electric force does work, so the sum of the kinetic energy and the potential energy is conserved. The electron travels toward a higher potential, so its potential energy decreases by $eU$ and its kinetic energy increases by the same amount. Every volt gives the electron one electronvolt.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\tfrac{1}{2}mv^2 = eU \\
&E_\text{k} = eU \\
&v = \sqrt{\frac{2eU}{m}}
\end{aligned}
```

<!-- vaihe -->

**Conversions.** $U = 3.0\,\text{kV} = 3.0 \cdot 1000\,\text{V} = 3000\,\text{V}$. In addition $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$ and $\sqrt{1\,\text{J} : 1\,\text{kg}} = 1\,\text{m/s}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&E_\text{k} = eU \\
&= 1.602 \cdot 10^{-19}\,\text{C} \cdot 3000\,\text{V} \\
&= 4.806 \cdot 10^{-16}\,\text{J} \\
&v = \sqrt{\frac{2E_\text{k}}{m}} \\
&= \sqrt{\frac{2 \cdot 4.806 \cdot 10^{-16}\,\text{J}}{9.109 \cdot 10^{-31}\,\text{kg}}} \\
&= 3.248 \cdot 10^{7}\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The kinetic energy of the electron is $3.0\,\text{keV}$ or $4.8 \cdot 10^{-16}\,\text{J}$, and its speed is $3.2 \cdot 10^{7}\,\text{m/s}$. The results are given with two significant figures like the potential difference $3.0\,\text{kV}$.

<!-- vaihe -->

**Reasonableness.** With rounded numbers $v \approx \sqrt{2 \cdot 5 \cdot 10^{-16}\,\text{J} : 10^{-30}\,\text{kg}} \approx 3 \cdot 10^{7}\,\text{m/s}$, so the order of magnitude is right. The speed is about $11\,\%$ of the speed of light $3.00 \cdot 10^{8}\,\text{m/s}$: it stays clearly below the speed of light, so the expression $\tfrac{1}{2}mv^2$ still gives a good result.

## Common misconception
Potential and potential energy are not the same thing. Potential is a property of a point in the field, and it does not depend on whether there is a charge at the point. Potential energy is the energy of a charge, and it depends on the magnitude and the sign of the charge: at the same point of $150\,\text{V}$ the potential energy of a proton is $+150\,\text{eV}$ and that of an electron $-150\,\text{eV}$. So it cannot be said that a charge always moves toward a lower potential: an electron moves toward a higher one.

Many also think that a longer acceleration distance gives a particle more energy. If the voltage between the plates stays the same, a larger plate separation makes the field weaker, $E = U : d$, and the work $qEd = qU$ is the same. What matters is the potential difference, not the distance. The distance affects only how long the acceleration takes.

## Summary
- The electric force is conservative, so a charge in a field has potential energy $E_\text{p} = qV$. The work done by the field is the decrease of the potential energy.
- Potential $V$ is potential energy per unit charge, $1\,\text{V} = 1\,\text{J/C}$. It is a property of a point in the field, and the potential difference of two points is the voltage between them.
- In a uniform field the potential changes steadily, $V = Ex$, when the negative plate is the zero of potential and $x$ is the distance from it. The field points from a higher potential to a lower one. Equipotential surfaces are parallel to the plates, and the field lines are perpendicular to them.
- When a charge travels through a potential difference $U$, the field does the work $qU$ regardless of the distance and the path. A particle that starts from rest gets the kinetic energy $\tfrac{1}{2}mv^2 = |q|U$.
- A positive charge starts moving toward a lower potential and a negative charge toward a higher one; the potential energy of each decreases.
- The electronvolt is a unit of energy for particles: $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.
