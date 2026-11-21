# Satellites and planets in circular orbits

> **Why** does the International Space Station ISS not fall to the Earth, and why do the astronauts float inside it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the International Space Station ISS orbits the Earth against black space. A long truss runs across the station, and at each end of it there are two pairs of large golden-brown solar panel wings. From the middle of the truss a chain of cylindrical living modules runs across it, and white radiator panels hang from the truss. At the bottom is the curved edge of the Earth: blue sea, green and brown land, white clouds and a thin blue atmosphere." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
A body that goes round another body under gravity is called a satellite. The Moon is a natural satellite of the Earth; the ISS and weather satellites are built by people. The path along which a satellite goes round is called an orbit. In space practically only one force acts on a satellite: the gravitational force of the Earth, which points towards the centre of the Earth. Because it is the only force, it is also the net force. In the chapter *Centripetal acceleration and the equation of motion in a circle* we found that in uniform circular motion the net force points to the centre of the path and gives the body its centripetal acceleration. In a circular orbit the gravitational force does exactly this: it is perpendicular to the velocity, so it does not change the speed but turns the direction of the velocity all the time.

<svg data-fig="orbit" viewBox="0 0 600 360" role="img" aria-label="Diagram, not to scale: a satellite orbits the Earth in a circular orbit drawn with a dashed line. The satellite is at the highest point of the orbit. The blue velocity arrow v points to the right along the tangent of the orbit. The red arrow of the gravitational force F points towards the centre of the Earth, and beside it the orange arrow of the centripetal acceleration a n points in the same direction. A thin dashed line continues straight to the right: the satellite would move along it without gravity." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-orbit.webp" x="-1.3" y="0" width="603" height="370.6" preserveAspectRatio="none"/>
  <foreignObject x="165" y="225.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Earth}$</div></foreignObject>
  <foreignObject x="389" y="47.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{without gravity}$</div></foreignObject>
  <foreignObject x="349.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="207.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="125.5" y="127.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="268" y="133.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="412" y="141.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{only force}$</div></foreignObject>
  <foreignObject x="412" y="177.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="412" y="213.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{towards the}$</div></foreignObject>
  <foreignObject x="412" y="247.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Earth's centre}$</div></foreignObject>
  <foreignObject x="412" y="297.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{F} = m\,\overline{a}_\text{n}$</div></foreignObject>
</svg>

So a satellite falls towards the Earth all the time, but it never hits it. Without gravity it would continue straight ahead along the tangent of the orbit. Gravity bends the path, and when the speed is just right, the path curves at the same rate as the surface of the Earth curves away beneath the satellite. Then the distance from the centre of the Earth stays the same and the orbit is a circle.

```pysahdy
What would happen to a satellite if the Earth's gravity suddenly stopped acting?
---
No force would bend the path, so the satellite would continue straight ahead along the tangent of the orbit at the same speed. It would not fall to the Earth and it would no longer go round in a circle.
```

If the speed is lower, gravity turns the path more sharply than a circle would require: the satellite descends lower and then returns to the starting altitude, or hits the Earth if the speed is much too low. If the speed is higher, the path curves more gently and the satellite rises farther away before returning. In these cases the orbit is not a circle but an ellipse, and the model of uniform circular motion does not describe it.

<svg data-fig="cannon" viewBox="0 0 600 380" role="img" aria-label="Diagram, not to scale: a body is launched horizontally from the same point above the Earth at three speeds. The paths have been calculated from the law of gravitation. At too low a speed the path curves more sharply than a circle and hits the Earth. At the circular-orbit speed the body goes round a circle that stays at the distance of the starting point. At a higher speed the path curves more gently, and the body moves farther away and returns to the starting point. This path is an ellipse whose point nearest the Earth is the starting point." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-cannon.webp" x="0" y="0" width="600" height="386.2" preserveAspectRatio="none"/>
  <foreignObject x="201" y="147.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Earth}$</div></foreignObject>
  <foreignObject x="323.5" y="21.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="444" y="135.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{too slow}$</div></foreignObject>
  <foreignObject x="444" y="179.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{circular}$</div></foreignObject>
  <foreignObject x="444" y="223.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{too fast}$</div></foreignObject>
</svg>

## Formula: Orbital speed in a circular orbit
When a satellite of mass $m$ goes round a central body in a circular orbit, the gravitational force is the only force and therefore the net force. According to Newton's second law it must be equal to the force required by the circular motion, $m a_\text{n} = \tfrac{m v^2}{r}$:
```latex
\gamma \frac{M m}{r^2} = \frac{m v^2}{r}
```
where $\gamma = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$ is the gravitational constant (many English books write it as *G*), $M$ is the mass of the central body ($\text{kg}$), $m$ is the mass of the satellite ($\text{kg}$), $r$ is the orbital radius ($\text{m}$) and $v$ is the orbital speed of the satellite ($\text{m/s}$). The orbital radius is measured from the centre of the central body: for a satellite of the Earth $r = R + h$, where $R = 6371\,\text{km}$ is the radius of the Earth and $h$ is the altitude of the satellite above the surface.

The mass $m$ of the satellite is on both sides of the equation and cancels. When the equation is multiplied by $r$ and divided by the mass $m$, we get $v^2 = \tfrac{\gamma M}{r}$, so the orbital speed in a circular orbit is
```latex
v = \sqrt{\frac{\gamma M}{r}}
```
The orbital speed depends only on the mass $M$ of the central body and on the orbital radius $r$, not on the mass of the satellite. A heavy space station and a small CubeSat orbit at the same altitude at the same speed. The farther away a satellite orbits, the lower its orbital speed.

<svg data-fig="vr" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: the orbital speed v of a circular orbit in kilometres per second as a function of the distance r, where r is the distance from the centre of the Earth in thousands of kilometres. The curve starts at the surface of the Earth, r is 6 371 km and v about 7.9 km/s, and decreases ever more gently: a satellite orbiting far away moves more slowly. The points marked on the curve are the ISS (r 6 790 km, v 7.65 km/s), a GPS satellite (r 26 560 km, v 3.87 km/s) and a geostationary satellite (r 42 164 km, v 3.07 km/s), calculated from real orbital periods." style="max-width:100%;font-size:24px">
  <line x1="126.5" y1="300" x2="126.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="300" x2="163.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="300" x2="200" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236.5" y1="300" x2="236.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="273.5" y1="300" x2="273.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="300" x2="310" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="300" x2="346.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383.5" y1="300" x2="383.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="300" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="273.5" x2="420" y2="273.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="246.5" x2="420" y2="246.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="220" x2="420" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="193.5" x2="420" y2="193.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="166.5" x2="420" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="140" x2="420" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="113.5" x2="420" y2="113.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="86.5" x2="420" y2="86.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="60" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="300" x2="434" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,300 L433,306 L433,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="126.5" y1="300" x2="126.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163.5" y1="300" x2="163.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="147" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="200" y1="300" x2="200" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="236.5" y1="300" x2="236.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="273.5" y1="300" x2="273.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="310" y1="300" x2="310" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="293.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="346.5" y1="300" x2="346.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="383.5" y1="300" x2="383.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="367" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="420" y1="300" x2="420" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="273.5" x2="90" y2="273.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="246.5" x2="90" y2="246.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="232" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="220" x2="90" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="193.5" x2="90" y2="193.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="179" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="166.5" x2="90" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="140" x2="90" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="125.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="83" y1="113.5" x2="90" y2="113.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="86.5" x2="90" y2="86.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="72" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="83" y1="60" x2="90" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="285.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (1000\,\text{km})$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{km/s})$</div></foreignObject>
  <polyline points="136.5,89 139,94 141.5,99 144,103.5 146,107.5 148.5,111.5 151,115.5 153,118.5 155.5,122 158,125 160.5,128 162.5,131 165,133.5 167.5,136 170,138.5 172,141 174.5,143 177,145.5 179,147.5 181.5,149.5 184,151.5 186.5,153 188.5,155 191,156.5 193.5,158 195.5,160 198,161.5 200.5,163 203,164.5 205,165.5 207.5,167 210,168.5 212.5,169.5 214.5,171 217,172 219.5,173.5 221.5,174.5 224,175.5 226.5,176.5 229,177.5 231,178.5 233.5,179.5 236,180.5 238,181.5 240.5,182.5 243,183.5 245.5,184.5 247.5,185 250,186 252.5,187 255,187.5 257,188.5 259.5,189.5 262,190 264,191 266.5,191.5 269,192 271.5,193 273.5,193.5 276,194.5 278.5,195 280.5,195.5 283,196.5 285.5,197 288,197.5 290,198 292.5,198.5 295,199.5 297,200 299.5,200.5 302,201 304.5,201.5 306.5,202 309,202.5 311.5,203 314,203.5 316,204 318.5,204.5 321,205 323,205.5 325.5,206 328,206.5 330.5,207 332.5,207.5 335,208 337.5,208.5 339.5,209 342,209 344.5,209.5 347,210 349,210.5 351.5,211 354,211.5 356.5,211.5 358.5,212 361,212.5 363.5,213 365.5,213 368,213.5 370.5,214 373,214.5 375,214.5 377.5,215 380,215.5 382,215.5 384.5,216 387,216.5 389.5,216.5 391.5,217 394,217.5 396.5,217.5 399,218 401,218.5 403.5,218.5 406,219 408,219 410.5,219.5 413,220 415.5,220 417.5,220.5 420,220.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="140" cy="96" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="156" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ISS}$</span></div></foreignObject>
  <circle cx="285" cy="196.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="262.5" y="152" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{GPS}$</span></div></foreignObject>
  <circle cx="399" cy="218" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="253" y="233.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{geostationary}$</span></div></foreignObject>
  <foreignObject x="235" y="95" width="150" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v = \sqrt{\dfrac{\gamma M}{r}}$</div></foreignObject>
</svg>

In one revolution the satellite travels the circumference $2\pi r$ of the circle, so the orbital period follows from the relation $v = \tfrac{2\pi r}{T}$ of the chapter *Centripetal acceleration and the equation of motion in a circle*:
```latex
T = \frac{2\pi r}{v}
```
where $T$ is the orbital period ($\text{s}$). The orbit of a faraway satellite is longer and its speed lower, so the orbital period grows quickly as the distance grows: the ISS goes round the Earth in about an hour and a half, the Moon in about $27\,\text{d}$. When the radius and the orbital period of a satellite are measured, the same equation can also be solved for the mass $M$ of the central body. This is how, for example, the masses of the Earth, the Sun and Mars have been determined.

```pysahdy
A satellite orbits in a circle at a speed of $3.0\,\text{km/s}$, and one revolution takes $4.0\,\text{h}$. How long is the orbit?
---
The orbit is the distance of one revolution, so $2\pi r = vT$. Thus $vT = 3.0 \cdot 10^{3}\,\text{m/s} \cdot 14\,400\,\text{s}$, which is about $4.3 \cdot 10^{7}\,\text{m}$ or $43\,000\,\text{km}$.
```

### Geostationary orbit
A geostationary satellite orbits above the equator in the same direction as the Earth rotates, and its orbital period is the same as the rotation period of the Earth, $23\,\text{h}\;56\,\text{min}$. It therefore seems to stay in place in the sky, and a satellite dish can be aimed at it once. Because the orbital period determines the orbital radius, all geostationary satellites orbit at the same altitude, about $35\,800\,\text{km}$.

## Weightlessness {Painottomuus}
On a space station the astronauts float, and a scale would show zero. The reason is not the absence of gravity. At the altitude of the ISS, $420\,\text{km}$, the acceleration due to the gravitational force is $\tfrac{\gamma M}{r^2} \approx 8.6\,\text{m/s}^2$, about $88\,\%$ of the value at the surface of the Earth. On an astronaut of mass $70\,\text{kg}$ there acts a weight of about $605\,\text{N}$, that is, the gravitational force $F$ of the Earth, whereas at the surface it would be $687\,\text{N}$.

The station and the astronaut are in free fall: only gravity acts on each, and each gets the same acceleration towards the Earth. Because they fall in the same way, the floor does not press on the astronaut and a scale does not have to support them, so the support force is zero. **Weightlessness (apparent weightlessness) means that nothing supports the body: only gravity acts on it, and it falls freely together with its surroundings. The support force is zero, although the weight acts all the time.**

<svg data-fig="paino" viewBox="0 0 600 380" role="img" aria-label="Two free-body diagrams at the same scale. On the left an astronaut stands on a scale at the surface of the Earth, drawn as a rectangle: the gravitational force F (weight) points down from the centre and the support force N of the scale up from the bottom face, equally long, so the acceleration is zero. On the right the same astronaut on a space station: the only force is the gravitational force F, about 12 per cent shorter, there is no support force, and the orange acceleration arrow a beside the body points down towards the Earth. The station falls with the same acceleration, so the floor does not press on the astronaut." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-paino.webp" x="1.2" y="1.2" width="597" height="386.8" preserveAspectRatio="none"/>
  <foreignObject x="27.5" y="11.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{on the Earth's surface}$</div></foreignObject>
  <foreignObject x="352.5" y="11.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{on a space station}$</div></foreignObject>
  <foreignObject x="111.5" y="267" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="175.5" y="140" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="115" y="341.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{a} = \overline{0}$</div></foreignObject>
  <foreignObject x="411.5" y="256" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="511.5" y="203.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="427.5" y="341.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N = 0$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/iss-from-soyuz.webp" alt="The International Space Station with its solar panels against black space. The cloudy surface of the Earth is visible below."><figcaption>The International Space Station photographed from a Soyuz spacecraft in October 2018. The station is always in free fall towards the Earth, but its orbital speed is so high that it never hits the Earth.</figcaption></figure>

The same state can be experienced for a moment on the Earth too: during a jump, in a freely falling lift, or in an aeroplane whose engines are adjusted so that it flies along the path of a projectile. Weightlessness is not explained by any "centrifugal force" cancelling gravity. If some force cancelled gravity, the net force would be zero, and the station would continue straight ahead and would not orbit the Earth.

## When the circular model holds {Milloin ympyrämalli pätee}
The model of uniform circular motion is a simplification. It describes the motion of a satellite well when

- the central body is much more massive than the satellite, so it can be considered to stay in place,
- the gravity of other bodies and air resistance are so small that only the gravity of the central body acts,
- the speed of the satellite is exactly the circular-orbit speed of the radius of its orbit, so that the distance from the centre stays constant.

Real satellite motion always deviates slightly from the model. In a low orbit the thin upper atmosphere slows the motion, the gravity of the Moon and the Sun pulls on the satellite, and the mass of the Earth is not distributed exactly spherically, because the Earth is slightly flattened at the poles. Because of the drag, for example, the orbit of the ISS is raised from time to time with rocket engines.

Many real orbits are nearly circles. The distance of the Earth from the Sun varies by only about $3\,\%$ of the mean distance, so the circular model describes the orbit of the Earth well. The distance of the Moon from the Earth varies by about $11\,\%$, so the model gives a good approximation for the Moon. The orbit of Halley's comet, in contrast, is very elongated, and the circular model does not suit it at all.

| Body | nearest distance | greatest distance |
| --- | --- | --- |
| Earth | $147.1\,\text{million km}$ | $152.1\,\text{million km}$ |
| Moon | $363\,300\,\text{km}$ | $405\,500\,\text{km}$ |
| Halley's comet | $88\,\text{million km}$ | $5250\,\text{million km}$ |

The distances of the Earth and Halley's comet are measured from the Sun, the distance of the Moon from the Earth. Source: NASA, Planetary Fact Sheets (Earth, Moon) and orbital data of Halley's comet, 2024.

<svg data-fig="radat" viewBox="0 0 600 360" role="img" aria-label="Two orbits, each at its own scale, with the Sun at the focus of the orbit. On the left the orbit of the Earth: the smallest distance from the Sun is 147.1 million kilometres and the greatest 152.1 million kilometres. The orbit is drawn with a solid line and a dashed circle over it, and the two cannot be told apart. On the right the orbit of Halley&#x27;s comet: the smallest distance is 88 million kilometres and the greatest about 5 250 million kilometres, a very elongated ellipse." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-radat.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="52.5" y="11.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{orbit of the Earth}$</div></foreignObject>
  <foreignObject x="321" y="11.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{orbit of Halley's comet}$</div></foreignObject>
  <foreignObject x="52" y="141.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Earth}$</div></foreignObject>
  <foreignObject x="14" y="309.5" width="272" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$147.1\text{–}152.1\ \text{million km}$</div></foreignObject>
  <foreignObject x="328" y="123.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{comet}$</div></foreignObject>
  <foreignObject x="533" y="207.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{Sun}$</div></foreignObject>
  <foreignObject x="325" y="309.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$88\text{–}5250\ \text{million km}$</div></foreignObject>
</svg>

```pysahdy
The distance of Halley's comet from the Sun is $88\,\text{million km}$ at its smallest and $5250\,\text{million km}$ at its greatest. Does the circular model fit its orbit?
---
No. The greatest distance is about $60$ times the smallest, but on a circular orbit the distance from the central body would stay constant.
```

Small deviations from the model show up in precise measurements. The orbital speed of the Moon calculated from measured values, $1.023\,\text{km/s}$, is about $0.5\,\%$ greater than the $1.018\,\text{km/s}$ given by the model, because the mass of the Moon is about $\tfrac{1}{81}$ of the mass of the Earth: the Earth and the Moon go round their common centre of mass, and the Earth does not stay in place. At the altitude of the ISS thin air brakes the station and its orbit slowly descends, so the station is raised with engines regularly.

## Worked example
The International Space Station ISS orbits the Earth in a nearly circular orbit at an altitude of about $420\,\text{km}$. Calculate the orbital speed and the orbital period of the station. The mass of the Earth is $M = 5.97 \cdot 10^{24}\,\text{kg}$ and its radius $R = 6371\,\text{km}$. Air resistance is ignored.

<!-- vaihe -->

**Given and find.** Altitude $h = 420\,\text{km}$, mass of the Earth $M = 5.97 \cdot 10^{24}\,\text{kg}$ and radius $R = 6371\,\text{km}$, gravitational constant $\gamma = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$. Find the orbital speed $v$ and the orbital period $T$.

<!-- vaihe -->

**Principle.** When air resistance is ignored, only the gravitational force of the Earth acts on the station. It is therefore the net force and, in a circular orbit, gives the centripetal acceleration towards the centre of the Earth: $\gamma \tfrac{Mm}{r^2} = \tfrac{mv^2}{r}$. The orbital radius is measured from the centre of the Earth, so $r = R + h$.

<!-- vaihe -->

**Formula solved.** The mass of the station cancels:
```latex
\begin{aligned}
r &= R + h \\
v &= \sqrt{\frac{\gamma M}{r}} \\
T &= \frac{2\pi r}{v}
\end{aligned}
```

<!-- vaihe -->

**Conversions.** Distances in metres: $R = 6371\,\text{km} = 6.371 \cdot 10^{6}\,\text{m}$ and $h = 420\,\text{km} = 0.420 \cdot 10^{6}\,\text{m}$, so $r = 6.791 \cdot 10^{6}\,\text{m}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&v = \sqrt{\frac{\gamma M}{r}} \\
&\gamma M = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\
&\quad \cdot 5.97 \cdot 10^{24}\,\text{kg} \\
&\quad = 3.98438 \cdot 10^{14}\,\text{m}^3/\text{s}^2 \\
&v = \sqrt{\frac{3.98438 \cdot 10^{14}\,\text{m}^3/\text{s}^2}{6.791 \cdot 10^{6}\,\text{m}}} \\
&= 7659.7\,\text{m/s} \\[6pt]
&T = \frac{2\pi r}{v} \\
&= \frac{2\pi \cdot 6.791 \cdot 10^{6}\,\text{m}}{7659.7\,\text{m/s}} \\
&= 5570.6\,\text{s}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The orbital speed is $v \approx 7.66\,\text{km/s}$ and the orbital period $T \approx 5570\,\text{s} \approx 92.8\,\text{min}$. The results are given to three significant figures, like the mass of the Earth $5.97 \cdot 10^{24}\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** According to NASA the ISS goes round the Earth in about $92.9\,\text{min}$, so the model is very close to the measured value. Right at the surface of the Earth the speed of a circular orbit would be $\sqrt{gR} = \sqrt{9.81\,\text{m/s}^2 \cdot 6.371 \cdot 10^{6}\,\text{m}} \approx 7.9\,\text{km/s}$; the ISS is slightly farther away, so its speed is slightly lower, as it should be.

## Common misconception
"There is no gravity in space, which is why astronauts float." This is wrong. At the altitude of the ISS gravity is almost as strong as at the surface of the Earth, and it is exactly what keeps the station in its orbit. Without gravity the station would fly straight away. The astronauts float because they and the station fall freely with the same acceleration.

Another error is to put the altitude $h$ into the formula $v = \sqrt{\tfrac{\gamma M}{r}}$ instead of the distance from the centre of the Earth, $r = R + h$. For the ISS this would give a speed of about $31\,\text{km/s}$, four times the real one. A third error is to think that a heavy satellite has to orbit faster: a greater mass experiences a greater gravitational force, but it also needs a greater force to turn, so the mass cancels.

## Summary
- Only the gravitational force of the central body acts on a satellite. It is the net force, which in a circular orbit gives the centripetal acceleration: $\gamma \tfrac{Mm}{r^2} = \tfrac{mv^2}{r}$.
- The orbital speed in a circular orbit is $v = \sqrt{\tfrac{\gamma M}{r}}$ and the orbital period $T = \tfrac{2\pi r}{v}$. The mass of the satellite has no effect, and a satellite orbiting farther away is slower and has a longer orbital period.
- The orbital radius is measured from the centre of the central body: $r = R + h$.
- Weightlessness means falling freely together with your surroundings with nothing to support you: gravity acts, but the support force is zero.
- The circular model holds when the central body is much more massive than the satellite, other forces are small and the orbit is nearly a circle.
