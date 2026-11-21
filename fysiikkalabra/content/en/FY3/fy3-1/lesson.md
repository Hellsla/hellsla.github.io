# Force as a measure of interaction and weight $G = mg$

> **Why** does an astronaut weigh only one sixth as much on the Moon as on Earth, even though no part of the astronaut has gone missing?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an astronaut leaps across the grey surface of the Moon, and his footprints show in the dust. The Earth, with oceans, continents and clouds, is visible in the black sky." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
When two objects act on each other, they interact. For example, the Earth pulls an apple towards itself. Force tells you how strong the interaction is: the greater the force, the stronger the interaction. The unit of force is the newton (N), and about $1\,\text{N}$ is the weight of a hundred-gram apple on Earth. At this stage only the magnitude of the force matters, and in the figures an arrow shows the direction in which the force points.

You can measure a force with a force meter. It contains a spring that stretches more the greater the force acting on it.

<svg data-fig="forcemeter" viewBox="0 0 600 410" role="img" aria-label="Force meter, schematic figure, not to scale. Two identical springs hang from a stand: an object of mass m hangs from the left-hand spring and two identical objects from the right-hand one. Double the weight stretches the spring double the distance. The weight G of each object is an arrow pointing down." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-1-forcemeter.webp" x="-1.3" y="0" width="603" height="417.1" preserveAspectRatio="none"/>
  <foreignObject x="160" y="176.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="184" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$G$</div></foreignObject>
  <foreignObject x="360" y="226.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="360" y="276.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="384" y="337.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2G$</div></foreignObject>
  <foreignObject x="260" y="116.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <foreignObject x="460" y="141.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2x$</div></foreignObject>
</svg>

The extension is directly proportional to the force as long as the spring is not stretched too far: double the force stretches the spring double the distance. The graph (force, extension) is therefore a straight line through the origin, like the directly proportional models in FY1, for example uniform motion $s = v t$. If $5.0\,\text{N}$ stretches a spring by $2.0\,\text{cm}$, then $10\,\text{N}$ stretches it by $4.0\,\text{cm}$ and $2.5\,\text{N}$ stretches it by $1.0\,\text{cm}$.

```pysahdy
A spring stretches $3.0\,\text{cm}$ when a force of $4.0\,\text{N}$ acts on it. How far does it stretch with a force of $12\,\text{N}$?
---
The extension is directly proportional to the force. The force is three times as large, so the extension is $3 \cdot 3.0\,\text{cm} = 9.0\,\text{cm}$.
```

<svg data-fig="force-extension" viewBox="0 0 600 330" role="img" aria-label="Graph to scale: extension x of a spring in centimetres as a function of force F, for F from 0 to 11 N. The measurement points 2.5 N and 1.0 cm, 5.0 N and 2.0 cm, and 10 N and 4.0 cm are on the same straight line through the origin; dashed lines show the values of the points on the axes." style="max-width:100%;font-size:24px">
  <line x1="179.5" y1="290" x2="179.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="267.5" y1="290" x2="267.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="355" y1="290" x2="355" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="443" y1="290" x2="443" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="246" x2="478" y2="246" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="202" x2="478" y2="202" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="158" x2="478" y2="158" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="114" x2="478" y2="114" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="290" x2="492" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M504,290 L491,296 L491,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="291" x2="92" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,44 L98,57 L86,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="290" x2="179.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.5$</div></foreignObject>
  <line x1="267.5" y1="290" x2="267.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="245" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5.0$</div></foreignObject>
  <line x1="355" y1="290" x2="355" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="332.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7.5$</div></foreignObject>
  <line x1="443" y1="290" x2="443" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="426.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="246" x2="92" y2="246" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.0$</div></foreignObject>
  <line x1="85" y1="202" x2="92" y2="202" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="187.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2.0$</div></foreignObject>
  <line x1="85" y1="158" x2="92" y2="158" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="143.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3.0$</div></foreignObject>
  <line x1="85" y1="114" x2="92" y2="114" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4.0$</div></foreignObject>
  <foreignObject x="62" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="510" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <foreignObject x="82" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{cm})$</div></foreignObject>
  <polyline points="92,290 478,96.5" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="179.5" y1="246" x2="179.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="246" x2="179.5" y2="246" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="267.5" y1="202" x2="267.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="202" x2="267.5" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="443" y1="114" x2="443" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="114" x2="443" y2="114" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="179.5" cy="246" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="267.5" cy="202" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="443" cy="114" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="309.5" y="222.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{line through origin}$</span></div></foreignObject>
</svg>

The scale is calibrated by hanging identical small objects on the spring, each with a mass of about $100\,\text{g}$, that is, a weight of about $1\,\text{N}$:

- One object stretches the spring by a certain distance, and the position is marked $1\,\text{N}$.
- Each object pulls on the spring equally hard, so two objects pull with double the force and stretch it double the distance. This position is marked $2\,\text{N}$, and so on.
- After that you can read the force directly in newtons from the extension.

The weight of an object is a measure of the strength of the interaction between the Earth and the object. It is a force, and its unit is the newton. Mass is something quite different: it tells you how much matter an object contains, and its unit is the kilogram. Mass is the same everywhere, but weight depends on where the object is. The Moon is a much smaller celestial body than the Earth, and the interaction between the Moon and the astronaut is weaker than between the Earth and the astronaut, so the astronaut weighs less on the Moon.

```pysahdy
An astronaut's mass on Earth is $80\,\text{kg}$. What is the astronaut's mass on the Moon, and what happens to the weight?
---
The mass is the same, $80\,\text{kg}$, because mass tells how much matter there is. The weight decreases, because the interaction between the Moon and the astronaut is weaker.
```

<figure class="unit-photo"><img src="pics/fy3/iss-cupola.webp" alt="An astronaut floats in the window dome of the space station. Earth and clouds can be seen through the windows."><figcaption>Astronaut Jessica Watkins floats in front of the Cupola window of the International Space Station, 2022. The Earth still pulls her there, but the station and the astronaut fall around the Earth together.</figcaption></figure>

## Formula: Weight
Two identical objects stretch the spring of a force meter twice as much as one, so weight is directly proportional to mass:
```kaavat
gravitational force on a body at the Earth's surface :: G = m g
```
where $G$ is the weight (N), $m$ the mass (kg) and $g$ the acceleration of free fall (m/s²), $9.81\,\text{m/s}^2$ on the surface of the Earth. When mass is in kilograms and $g$ in m/s², the weight comes out in newtons, because $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$ (this is justified in FY4). So the weight of a one-kilogram mass on Earth is $9.81\,\text{N}$. Elsewhere $g$ is different. The values in the table apply to the surface of the celestial body (for Jupiter, the level of the cloud tops):

| Celestial body | $g$ at the surface (m/s²) |
| --- | --- |
| Moon | 1.62 |
| Mars | 3.71 |
| Earth | 9.81 |
| Jupiter | 24.8 |

The Moon's $g$ is about one sixth of the Earth's value ($1.62 : 9.81 \approx 0.17 \approx 1 : 6$), so the same mass weighs about one sixth as much on the Moon as on Earth. This answers the question about the astronaut at the beginning.

In the graph, weight is plotted as a function of mass. For each celestial body, weight is directly proportional to mass, so the graph is a straight line through the origin. The greater $g$ is, the steeper the line: for the same mass, weight is greatest on Jupiter and smallest on the Moon.

```pysahdy
Why is the line for Jupiter steeper than the line for the Moon?
---
On Jupiter $g$ is greater, so the same mass weighs more there. Therefore the weight grows faster with mass.
```

<svg data-fig="weight-mass" viewBox="0 0 600 336" role="img" aria-label="Graph to scale: weight G in newtons as a function of mass m, for m from 0 to 100 kg. Four straight lines through the origin, from steepest to gentlest: Jupiter (the line continues past the top edge of the figure), Earth (100 kg weighs 981 N), Mars (371 N) and the Moon (162 N)." style="max-width:100%;font-size:24px">
  <line x1="185" y1="300" x2="185" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="300" x2="270" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="355" y1="300" x2="355" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="440" y1="300" x2="440" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="245.5" x2="440" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="191" x2="440" y2="191" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="136.5" x2="440" y2="136.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="82" x2="440" y2="82" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="300" x2="454" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M466,300 L453,306 L453,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="301" x2="100" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,34 L106,47 L94,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="185" y1="300" x2="185" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="168.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="270" y1="300" x2="270" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="253.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="355" y1="300" x2="355" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="338.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$75$</div></foreignObject>
  <line x1="440" y1="300" x2="440" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="417.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="245.5" x2="100" y2="245.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="231" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <line x1="93" y1="191" x2="100" y2="191" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="176.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="93" y1="136.5" x2="100" y2="136.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="122" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$750$</div></foreignObject>
  <line x1="93" y1="82" x2="100" y2="82" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="67.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1000$</div></foreignObject>
  <foreignObject x="70" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="472" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m\ (\text{kg})$</div></foreignObject>
  <foreignObject x="90" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$G\ (\text{N})$</div></foreignObject>
  <polyline points="100,300 251,60" fill="none" stroke="#a97a35" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="261" y="47.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#a97a35">$\text{Jupiter}$</div></foreignObject>
  <polyline points="100,300 440,86" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="452" y="71.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{Earth}$</div></foreignObject>
  <polyline points="100,300 440,219" fill="none" stroke="#b8622d" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="452" y="204.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d">$\text{Mars}$</div></foreignObject>
  <polyline points="100,300 440,264.5" fill="none" stroke="#6c757d" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="452" y="243.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6c757d">$\text{Moon}$</div></foreignObject>
</svg>

## Worked example
A research robot has a mass of $1.20 \cdot 10^2\,\text{kg}$. What is its weight on Earth and on Mars?

<!-- vaihe -->

**Given and find.** The mass is $m = 1.20 \cdot 10^2\,\text{kg}$, and from the table $g_\text{Earth} = 9.81\,\text{m/s}^2$ and $g_\text{Mars} = 3.71\,\text{m/s}^2$.

We want the weights $G_\text{Earth}$ and $G_\text{Mars}$.

<!-- vaihe -->

**Principle.** Weight is a measure of the strength of the interaction: it is directly proportional to mass, and the constant is the $g$ of the celestial body on whose surface the robot is. The robot's mass is the same in both places, so only $g$ changes.

<!-- vaihe -->

**Rearranged formula.** The weight we want is already alone on the left-hand side of the formula, so the formula does not need rearranging. The same mass is multiplied by the acceleration of free fall at each place:
```latex
\begin{aligned}
G_\text{Earth} &= m g_\text{Earth} \\
G_\text{Mars} &= m g_\text{Mars}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The mass is already in kilograms and $g$ in m/s², so no conversions are needed: $1\,\text{kg} \cdot 1\,\text{m/s}^2 = 1\,\text{N}$, and the result comes out directly in newtons.

<!-- vaihe -->

**Substitution.** The values are substituted with their units into both formulas:
```latex
\begin{aligned}
&G_\text{Earth} = m g_\text{Earth} \\
&= 1.20 \cdot 10^2\,\text{kg} \cdot 9.81\,\text{m/s}^2 \\
&= 1177.2\,\text{N} \\[6pt]
&G_\text{Mars} = m g_\text{Mars} \\
&= 1.20 \cdot 10^2\,\text{kg} \cdot 3.71\,\text{m/s}^2 \\
&= 445.2\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** To three significant figures, the robot's weight is about $1.18\,\text{kN}$ on Earth and about $445\,\text{N}$ on Mars. The results are given to three significant figures because the mass and the values of the free-fall acceleration are given to that precision.

<!-- vaihe -->

**Reasonableness.** The weight of a one-kilogram mass on Earth is about $10\,\text{N}$, so the weight of a $120\,\text{kg}$ mass is about $1200\,\text{N}$. Mars's $g$ is a little over one third of the Earth's value ($3.71 : 9.81 \approx 0.38$), and $445\,\text{N}$ is a little over one third of $1.18\,\text{kN}$. On Mars the weight is smaller because the interaction between Mars and the robot is weaker than between the Earth and the robot. The mass is the same in both.

## Common misconception
In everyday language people say "I weigh 70 kilos", but the kilogram is a unit of mass, not of weight. In physics the mass is $70\,\text{kg}$ and the weight on Earth is about $690\,\text{N}$. Another mistake is to think that an object's mass changes on the Moon. The mass stays the same, and only the weight decreases. Note also that a force meter measures force, not mass: its reading changes when the same object is taken to another place. A bathroom scale still shows kilograms, because it measures force and its scale has been made on Earth by dividing the force by $9.81\,\text{m/s}^2$. On the Moon such a scale would show only about one sixth of the mass.

## Summary
- Force tells you the strength of an interaction, and its unit is the newton (N). The extension of a force meter's spring is directly proportional to the force.
- Weight is a force: $G = m g$. Mass tells you how much matter an object contains, and it is the same everywhere.
- $g = 9.81\,\text{m/s}^2$ on the surface of the Earth, so the weight of a one-kilogram mass on Earth is $9.81\,\text{N}$. On the Moon $g = 1.62\,\text{m/s}^2$ and on Mars $3.71\,\text{m/s}^2$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: the same backpack hangs from a spring balance on Earth and on the Moon. On Earth the spring stretches far, on the Moon only one sixth as much, because the Moon pulls the backpack six times more weakly. The extensions are drawn to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-1-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
