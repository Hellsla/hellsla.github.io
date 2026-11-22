# Force on a current-carrying wire: the electric motor and the loudspeaker

> **Why** does a loudspeaker cone vibrate and the blades of a desk fan turn, when nothing visible pushes either of them?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a desk there is a wooden loudspeaker, from whose cone sound waves spread, and next to it a desk fan with turning blades. Nobody touches either, but the cone vibrates and the blades turn when electric current is switched on to the devices." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A magnetic field pushes a current-carrying wire
In the chapter *Charged particle in electric and magnetic fields*, a magnetic field exerted on a moving charged particle a force perpendicular to both the velocity of the particle and the field. An electric current in a wire is a motion of charges: the conduction electrons of the metal move along the wire. The magnetic field exerts a force on every moving electron, and the electrons pass it on to the metal of the wire, so the force acts on the whole wire. When a light copper wire is hung between the poles of a horseshoe magnet and a current is switched on, the wire swings sideways. Copper is not ferromagnetic, and the magnet does not attract it: the force appears only when there is a current in the wire.

<svg data-fig="swing" viewBox="0 0 600 360" role="img" aria-label="Two schematic figures, not to scale. On the left a wire is seen end-on between the poles of two magnets: the N pole is at the top and the S pole at the bottom, so the magnetic field points downwards. The current flows into the page in the wire, and the force of the magnetic field pushes the wire to the left, perpendicular to both the current and the field. On the right the right-hand rule: the thumb points in the direction of the current, the other fingers in the direction of the field (the obliquely drawn arrow comes towards the viewer), and the force points out of the palm, here downwards. The three arrows are perpendicular to each other." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-swing.webp" x="1.2" y="1.2" width="597" height="366.9" preserveAspectRatio="none"/>
  <foreignObject x="150" y="53.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="150" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="246" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="103.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="150" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
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

```pysahdy
A current flows in a wire perpendicular to a magnetic field, and the force pushes the wire upward. In which direction does the force point if the direction of the current is reversed and the field stays the same?
---
The force points downward. When the direction of the current or the field is reversed, the direction of the force reverses, but its magnitude stays the same.
```

### The electric motor
In a direct-current motor, a **current loop** that can turn about an axle sits between the poles of a magnet. In the two sides of the loop that cross the field, the current flows in opposite directions, so the forces on them are in opposite directions. The forces are not on the same line, so they have a turning effect: they turn the loop. When the loop has turned to be perpendicular to the field, the forces point away from the axle and no longer turn it, and the loop keeps moving because of its inertia. Exactly then the **commutator**, a split ring with the carbon brushes that touch it, reverses the direction of the current in the loop. In this way the forces turn the loop in the same direction every half turn. A real motor has many coils and an iron core, so it turns smoothly and strongly.

<svg data-fig="motor" viewBox="0 0 600 380" role="img" aria-label="Two schematic figures of a direct-current motor, not to scale. On the left a current loop is seen along the axle between the N and S poles; the magnetic field points from left to right. In one side of the loop the current flows into the page and in the other out of the page. The forces on the sides are in opposite directions, one downwards and the other upwards, and they turn the loop anticlockwise. On the right the commutator: around the axle is a ring split into two parts, touched by two carbon brushes. The brushes are connected to the positive and negative terminals of the power supply." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-motor.webp" x="0" y="-1.2" width="600" height="387.5" preserveAspectRatio="none"/>
  <foreignObject x="36" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="304" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="243" y="269.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="130.5" y="276" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="196.5" y="85" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="95" y="345.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current loop}$</div></foreignObject>
  <foreignObject x="380" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="564" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="392" y="77.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{commutator}$</div></foreignObject>
  <foreignObject x="407" y="275.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{carbon brushes}$</div></foreignObject>
</svg>

```pysahdy
What would happen to a DC motor if the commutator did not reverse the current in the loop?
---
Once the loop has turned perpendicular to the field, the forces would start to turn it back. The loop would not keep rotating but would oscillate about that position and finally come to rest there.
```

### The loudspeaker
The magnet of a loudspeaker is built so that in the ring-shaped gap the field points radially outwards. In the gap is a light voice coil, and every part of it is perpendicular to the field, so an equal force acts on every part in the direction of the axis of the coil. A radial field is essential: in a uniform field the forces on opposite sides of a closed coil would be in opposite directions and would cancel, so nothing would push the coil. The coil is attached to the cone. The alternating current from the amplifier changes its direction in step with the sound signal, so the force pushes the cone alternately forwards and backwards. The cone vibrates at the frequency of the signal, compresses and rarefies the air and produces a sound wave. The larger the current, the larger the force and the louder the sound. Most of the electrical energy delivered to the loudspeaker is, however, transformed into internal energy of the coil and the magnet.

<svg data-fig="speaker" viewBox="0 0 600 360" role="img" aria-label="Cross-section of a loudspeaker, schematic figure, not to scale. On the left is an iron centre pole, and around it a ring magnet and a front plate. The centre pole is an N pole and the front plate an S pole, so in the narrow gap the magnetic field points radially outwards, upwards in the upper gap and downwards in the lower gap. In the gap is the voice coil: in the cross-section of its turns the current flows into the page above and out of the page below. On both sides the force points to the right, towards the cone, which is attached to the coil." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-speaker.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="198" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{N}$</div></foreignObject>
  <foreignObject x="138" y="72.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="138" y="258.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="92" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="92" y="215.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="186" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="252" y="97.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="252" y="233.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="446" y="25.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{cone}$</div></foreignObject>
  <foreignObject x="40" y="315.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ring magnet}$</div></foreignObject>
  <foreignObject x="365" y="165.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \text{ varies}$</div></foreignObject>
  <foreignObject x="325" y="207.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Rightarrow F \text{ varies}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/electric-motor-cutaway.webp" alt="A blue industrial electric motor with part of its casing cut away, showing the shaft, rotor, copper windings and fan."><figcaption>A cut-away industrial electric motor. Current flows in the copper windings, and the magnetic field exerts a force on the conductors of the rotor, so the shaft turns. This AC motor is built differently from the DC motor in this lesson, but the basic effect is the same: a magnetic field pushes a current-carrying conductor.</figcaption></figure>

## Formula: Force on a current-carrying wire
When a current $I$ flows in a straight wire and the wire is in a uniform magnetic field, the field exerts on the wire a force of magnitude
```kaavat
magnetic force on a straight conductor :: F = I l B \sin\alpha
```
where $F$ is the force (N), $I$ the current (A), $l$ the length of the part of the wire that is in the field (m), $B$ the magnetic flux density (T) and $\alpha$ the angle between the wire and the field. Only the component of the field perpendicular to the wire, $B \sin\alpha$, produces a force. The force is greatest when the wire is perpendicular to the field ($\sin 90^\circ = 1$) and zero when the wire is parallel to the field ($\sin 0^\circ = 0$). At an angle of $30^\circ$ the force is half of its greatest value, because $\sin 30^\circ = 0.5$. The formula gives the unit of the tesla: $1\,\text{T} = 1\,\tfrac{\text{N}}{\text{A}\cdot\text{m}}$.

<svg data-fig="angle" viewBox="0 0 600 340" role="img" aria-label="Schematic figure seen from above, not to scale. The horizontal green field lines point to the right. The wire is at an angle alpha to the field, and the current flows along the wire towards the upper right. The component of the field perpendicular to the wire, B sin alpha, is drawn with a dashed line. The force points into the page, which is shown by a cross inside a circle at the middle of the wire." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-angle.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="527" y="19.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="230" y="156" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="376.5" y="134" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="470" y="140" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$B \sin\alpha$</div></foreignObject>
  <foreignObject x="320" y="201.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
</svg>

```pysahdy
The length of a wire in a field is $0.50\,\text{m}$ and the current is $4.0\,\text{A}$. The magnetic flux density is $0.25\,\text{T}$, and the wire makes an angle of $30^\circ$ with the field. How large is the force on the wire?
---
The force is $F = I l B \sin\alpha = 4.0\,\text{A} \cdot 0.50\,\text{m} \cdot 0.25\,\text{T} \cdot \sin 30^\circ = 0.25\,\text{N}$.
```

### The force between two current-carrying wires
There is a force between two parallel current-carrying wires, because each is in the magnetic field of the other. In the chapter *Magnetic field of a wire and a coil*, the field of wire $1$ circles around it, and at a distance $r$ its magnitude is $B_1$. At wire $2$ the field is perpendicular to wire $2$, so a force $F$ acts on the part of wire $2$ whose length is $l$:
```latex
\begin{aligned}
&B_1 = \frac{\mu_0 I_1}{2\pi r} \\[6pt]
&F = I_2 l B_1 \\
&\quad = \frac{\mu_0 I_1 I_2 l}{2\pi r}
\end{aligned}
```
where $I_1$ and $I_2$ are the currents of the wires (A), $r$ is the distance between the wires (m), $l$ the length of the part that runs parallel (m) and $\mu_0 \approx 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$ the permeability of free space. By Newton's third law, an equal and opposite force acts on wire $1$. The right-hand rule shows that **currents in the same direction attract each other and currents in opposite directions repel each other**. Until 2019 the ampere was defined with this force: the current is $1\,\text{A}$ when the force between wires $1\,\text{m}$ apart is $2 \cdot 10^{-7}\,\text{N}$ for every metre of wire.

<svg data-fig="wires" viewBox="0 0 600 360" role="img" aria-label="Two schematic figures of parallel wires seen end-on, not to scale. On the left the current in both wires flows out of the page. The magnetic field of the left wire circles it anticlockwise, and at the right wire the field points upwards. The forces point from one wire towards the other: the wires attract each other. On the right the currents are in opposite directions, the current in the right wire flows into the page, and the forces point away from each other: the wires repel each other." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-wires.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="15" y="13.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{same direction}$</div></foreignObject>
  <foreignObject x="325" y="13.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{opposite directions}$</div></foreignObject>
  <foreignObject x="207" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_1$</div></foreignObject>
  <foreignObject x="88.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="209" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="133.5" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="90" y="321.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{attract}$</div></foreignObject>
  <foreignObject x="507" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_1$</div></foreignObject>
  <foreignObject x="388.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="509" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="354.5" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="390" y="321.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{repel}$</div></foreignObject>
</svg>

## Worked example
A loudspeaker voice coil has $60$ turns of thin wire, and the radius of the coil is $1.3\,\text{cm}$. The coil is in the gap of a magnet, where the magnetic flux density of the radial field is $0.95\,\text{T}$, and the field is perpendicular to the wire everywhere. How large is the force on the coil when the current is at its peak value of $1.5\,\text{A}$?

<!-- vaihe -->

**Given and find.** Number of turns $N = 60$, radius of the coil $r = 1.3\,\text{cm}$, magnetic flux density $B = 0.95\,\text{T}$, current $I = 1.5\,\text{A}$ and angle between the wire and the field $\alpha = 90^\circ$.

We are asked for the force $F$ on the coil.

<!-- vaihe -->

**Principle.** The field is radial, so every part of the wire of the coil is perpendicular to the field, and the force on every part points in the same direction, along the axis of the coil.

The forces therefore add up, and in the formula $F = I l B \sin\alpha$ the length $l$ is the whole length of the wire of the coil: $N$ turns, each with the length of the circumference of a circle, $2\pi r$.

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
  <image href="pics/fy7/fy7-4-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
