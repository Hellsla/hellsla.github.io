# Work and energy

> **Why** is carrying a heavy backpack along a level corridor not work in the physics sense, even though your shoulders get tired?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a student walks along a level school corridor with a heavy backpack on their back. The floor is horizontal, and a dashed arrow parallel to the floor shows the direction of travel. In the background there is a row of lockers and some windows." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
In everyday language, work often means effort. In physics, work has a more precise meaning: a force does work when an object is displaced and the force has a component along the displacement.

When you carry a backpack horizontally at a steady speed, your force supporting the backpack points upwards, but the backpack is displaced horizontally. The force is perpendicular to the displacement, so the mechanical work done by this force is zero. Your muscles still use energy to hold the backpack up.

```pysahdy
You hold a heavy book still in your outstretched hand. Does the supporting force of your hand do work?
---
No. The book does not move, so there is no displacement and no mechanical work is done.
```

<svg data-fig="carry-lift" viewBox="0 0 600 320" role="img" aria-label="Diagram of two situations. On the left a backpack is carried sideways: the supporting force F points up but the motion is sideways, so the force does no work, W = 0. On the right the backpack is lifted up: the force F and the motion are in the same direction, so the force does work W = F s." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-carry-lift.webp" x="3.7" y="2.5" width="594.1" height="324.3" preserveAspectRatio="none"/>
  <foreignObject x="52.5" y="15.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{carried sideways}$</div></foreignObject>
  <foreignObject x="396" y="15.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lifted up}$</div></foreignObject>
  <foreignObject x="166" y="84.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="113" y="251.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{path}$</div></foreignObject>
  <foreignObject x="127.5" y="291.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = 0$</div></foreignObject>
  <foreignObject x="414" y="84.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="534" y="145.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{path}$</div></foreignObject>
  <foreignObject x="415" y="291.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = F\,s$</div></foreignObject>
</svg>

Work is a way of transferring energy. James Prescott Joule showed this in the 1840s by letting a falling weight turn a paddle wheel in water. The weight did work, and the water warmed by a measurable amount even though it was not heated: the work increased the internal energy of the water. In the experiments the warming of the water turned out to be proportional to the product of the weight and the falling distance, that is, the product of force and distance. This experimental result justifies the definition of work $W = Fs$ (formula below). The same warming can also be produced by heating, so work and heat are two ways of transferring energy, and both are measured in the same unit, the joule.

```pysahdy
In Joule's experiment the water was not heated, but it got warmer. What caused this?
---
The work done by the falling weight turned the paddle wheel and increased the internal energy of the water.
```

<svg data-fig="joule" viewBox="0 0 600 340" role="img" aria-label="Diagram of Joule&#x27;s experiment. A falling weight pulls a string that passes over a pulley and turns a paddle wheel in a vessel of water. The force of the weight does work over the falling distance h, and the paddle wheel warms the water: work increases the internal energy of the water." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-joule.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="127.5" y="15.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{work} \to \text{internal energy}$</div></foreignObject>
  <foreignObject x="291" y="165.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{weight}$</div></foreignObject>
  <foreignObject x="500" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="81" y="289.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{water warms up}$</div></foreignObject>
</svg>

When you do work on an object, energy is transferred: the energy of a lifted object increases, a spring stretches and stores energy, and work done against friction warms the surfaces. Energy does not disappear; it changes form. Power tells you how fast work is done. Walking and running up the stairs you do the same work, but when running the power is greater. The $6\,\text{kW}$ power of a sauna heater means that every second it turns 6000 joules of electrical energy into internal energy, which is transferred as heat to the stones and the air.

<figure class="unit-photo"><img src="pics/fy3/crane-lifting-load.webp" alt="A grey concrete bucket hangs from a crane hook under the roof of a building under construction, and two workers guide it."><figcaption>A crane lifts a concrete bucket on a building site. As the load rises, the lifting force does work and the load's potential energy increases.</figcaption></figure>

## Formula: Work and power
When a constant force is in the direction of motion, the work done by the force is the product of force and distance:
```kaavat
work done by a force :: W = F s
```
where $W$ is the work (J), $F$ is the magnitude of the force (N) and $s$ is the distance moved by the object (m). One joule is the work done by a force of one newton over a distance of one metre: $1\,\text{J} = 1\,\text{N} \cdot \text{m}$.

If the force changes during the motion, the work is the area between the force curve and the $s$-axis in an $(s,F)$ graph. For a constant force the area is a rectangle with area $F \cdot s$, so the same rule works in both cases. You can find the area of a complicated graph by dividing it into rectangles, triangles and trapeziums.

<svg data-fig="work-graphs" viewBox="0 0 600 346" role="img" aria-label="Diagram of two (s,F) graphs. On the left the force is constant, and the work is the area of a rectangle F · s. On the right the force first increases steadily and then stays constant; the work is the area of a triangle A₁ plus the area of a rectangle A₂." style="max-width:100%;font-size:24px">
  <line x1="79" y1="240" x2="264" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M276,240 L263,246 L263,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="241" x2="80" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,54 L86,67 L74,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="282" y="225.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="70" y="23.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <polygon points="80,240 80,144 216,144 216,240" fill="#ffc078" fill-opacity="0.55"/>
  <line x1="216" y1="144" x2="216" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="80" y1="144" x2="216" y2="144" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="80,144 216,144" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="80" y1="262" x2="216" y2="262" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="255" x2="80" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="216" y1="255" x2="216" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="138" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s$</div></foreignObject>
  <line x1="58" y1="240" x2="58" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="51" y1="240" x2="65" y2="240" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="51" y1="144" x2="65" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="26" y="177.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="113" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = F\,s$</div></foreignObject>
  <foreignObject x="63" y="307.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{constant force}$</div></foreignObject>
  <line x1="369" y1="240" x2="554" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,240 L553,246 L553,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="370" y1="241" x2="370" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M370,54 L376,67 L364,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="572" y="225.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="360" y="23.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <polygon points="370,240 438,144 438,240" fill="#e8590c" fill-opacity="0.4"/>
  <polygon points="438,240 438,144 523,144 523,240" fill="#ffc078" fill-opacity="0.55"/>
  <line x1="523" y1="144" x2="523" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="370" y1="144" x2="523" y2="144" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="438,144 438,240" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="370,240 438,144 523,144" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="370" y1="262" x2="523" y2="262" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="255" x2="370" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="523" y1="255" x2="523" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="436.5" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s$</div></foreignObject>
  <line x1="348" y1="240" x2="348" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="341" y1="240" x2="355" y2="240" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="341" y1="144" x2="355" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="316" y="177.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="404.5" y="200" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_1$</div></foreignObject>
  <foreignObject x="464" y="177.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_2$</div></foreignObject>
  <foreignObject x="367.5" y="307.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{varying force}$</div></foreignObject>
</svg>

When you lift an object upwards at a steady speed, the lifting force is equal to the weight of the object $G = mg$ (chapter *Force as a measure of interaction and weight $G = mg$*). The work of lifting to a height $h$ is therefore:
```latex
W = G h = m g h
```
where $G$ is the weight (N), $m$ is the mass (kg), $g = 9.81\,\text{m/s}^2$ and $h$ is the lifting height (m). The energy of the lifted object increases by exactly the amount of the lifting work.

<svg data-fig="lift-work" viewBox="0 0 600 330" role="img" aria-label="Diagram of lifting work, not to scale. A box is lifted at a steady speed from the ground to a height h. The lifting force F points up and the weight G of the box points down, and the arrows are equally long, F = G. The lifting work is W = F h = G h." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-lift-work.webp" x="0" y="0" width="597" height="335.8" preserveAspectRatio="none"/>
  <foreignObject x="196" y="39.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="196" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$G$</div></foreignObject>
  <foreignObject x="20" y="181.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{path}$</div></foreignObject>
  <foreignObject x="290" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="372" y="65.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F = G$</div></foreignObject>
  <foreignObject x="372" y="135.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = F\,h$</div></foreignObject>
  <foreignObject x="372" y="185.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = G\,h$</div></foreignObject>
  <foreignObject x="372" y="235.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = m\,g\,h$</div></foreignObject>
</svg>

Power is work divided by the time it takes. In motion at a steady speed, where the force is in the direction of motion, power can also be found as the product of force and speed, because $s/t = v$:
```kaavat
power :: P = \frac{W}{t} = F v
```
where $P$ is the power (W), $t$ is the time (s) and $v$ is the speed (m/s). One watt is one joule per second: $1\,\text{W} = 1\,\text{J/s}$.

```pysahdy
A machine does $600\,\text{J}$ of work in $20\,\text{s}$. What is the power of the machine?
---
$P = W/t = 600\,\text{J}/20\,\text{s} = 30\,\text{W}$.
```

## Worked example
A spring is stretched $20\,\text{cm}$. The stretching force increases steadily from zero to 40 newtons, as the graph shows. How much work does the stretching force do?

<svg data-fig="spring-work" viewBox="0 0 600 320" role="img" aria-label="(s,F) graph to scale: the force increases linearly from zero to 40 newtons over 0–0.20 metres; the area of the triangle is the work." style="max-width:100%;font-size:24px">
  <line x1="167.5" y1="270" x2="167.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="243" y1="270" x2="243" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="319" y1="270" x2="319" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="394.5" y1="270" x2="394.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="227" x2="470" y2="227" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="184.5" x2="470" y2="184.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="141.5" x2="470" y2="141.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="99" x2="470" y2="99" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="271" x2="92" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,30 L98,43 L86,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="167.5" y1="270" x2="167.5" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="138.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.05$</div></foreignObject>
  <line x1="243" y1="270" x2="243" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="214" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.10$</div></foreignObject>
  <line x1="319" y1="270" x2="319" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="290" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.15$</div></foreignObject>
  <line x1="394.5" y1="270" x2="394.5" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="365.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.20$</div></foreignObject>
  <line x1="85" y1="227" x2="92" y2="227" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="212.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="184.5" x2="92" y2="184.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="170" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="141.5" x2="92" y2="141.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="127" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="85" y1="99" x2="92" y2="99" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="84.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="62" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <foreignObject x="82" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <polygon points="92,270 394.5,99 394.5,270" fill="#ffc078" fill-opacity="0.6"/>
  <line x1="394.5" y1="99" x2="394.5" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="99" x2="394.5" y2="99" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="92,270 394.5,99" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="394.5" cy="99" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="262" y="225.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = \text{area}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Given and find.** The stretch of the spring, that is, the distance moved by the force, is $s = 20\,\text{cm}$, and the greatest value of the force is $F_\text{max} = 40\,\text{N}$.

The force increases steadily from zero.

We want the work $W$ done by the stretching force.

<!-- vaihe -->

**Principle.** Work is the product of force and distance only when the force is constant. Here the force increases steadily, so the work is found as the area under the $(s,F)$ graph: the region between the graph and the $s$-axis is a triangle. The force is in the direction of motion, so the work is positive.

<!-- vaihe -->

**Rearranged formula.** The force is not constant, so the formula $W = Fs$ cannot be used directly. The work is the area $A_\text{triangle}$ of the triangle in the $(s,F)$ graph, which is half of the product of the base $s$ and the height $F_\text{max}$:
```latex
\begin{aligned}
W &= A_\text{triangle} \\
&= \frac{1}{2} F_\text{max}\, s
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The distance is in centimetres, but work is calculated in joules, so the distance is converted to metres: $s = 20\,\text{cm} = 0.20\,\text{m}$. The force is already in newtons, so the product $\text{N}\cdot\text{m}$ is directly in joules.

<!-- vaihe -->

**Substitution.** We substitute the values with their units:
```latex
\begin{aligned}
W &= A_\text{triangle} \\
&= \frac{1}{2} F_\text{max}\, s \\
&= \frac{1}{2} \cdot 40\,\text{N} \cdot 0.20\,\text{m} \\
&= 4.0\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The stretching force does $4.0\,\text{J}$ of work, two significant figures like the given values $20\,\text{cm}$ and $40\,\text{N}$. The work does not disappear; the energy is stored in the stretched spring.

<!-- vaihe -->

**Reasonableness.** The force increases steadily, so its average magnitude is half of the peak value, $F_\text{avg} = 20\,\text{N}$. The average force gives the same result:
```latex
\begin{aligned}
W &= F_\text{avg}\, s \\
&= 20\,\text{N} \cdot 0.20\,\text{m} \\
&= 4.0\,\text{J}
\end{aligned}
```
If you calculated $40\,\text{N} \cdot 0.20\,\text{m} = 8.0\,\text{J}$, the result would be twice too large, because the force is not $40\,\text{N}$ over the whole distance.

## Common misconception
Work is not the same thing as effort: getting tired does not mean you have done work in the physics sense. Another common mistake is to mix up work and power: a large power does not mean a large amount of work, but work done quickly.

## Summary
- A constant force in the direction of motion does the work $W = F s$. For a varying force, the work is the area under the $(s,F)$ graph.
- A force perpendicular to the motion does no work. That is why carrying something horizontally at a steady speed is not work done by the carrier's force.
- Work transfers energy: it can raise the energy of an object ($W = m g h$), stretch a spring or increase the internal energy of surfaces through friction. Joule's experiment showed that work and heat are two ways of transferring energy.
- Power is work per unit time: $P = W/t = F v$. Units: $1\,\text{J} = 1\,\text{N} \cdot \text{m}$ and $1\,\text{W} = 1\,\text{J/s}$.
