# Position, velocity and uniform motion as graphs

> **Why** can the distance a cyclist has travelled be four kilometres, even though her displacement is zero?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a lake in the middle of a forest seen obliquely from above, with a gravel path going around it. At the starting point of the path there is a flag and a starting line. In the foreground a cyclist rides along the path towards the starting point: she has gone all the way around the lake. Arrows on the path show the direction of travel." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
Describing motion begins with a convention. We choose the straight line along which the object moves, and an origin and a positive direction on it: this is the $x$-axis. The **position** $x$ tells where the object is relative to the origin. The sign tells which side: the position $x = -3\,\text{m}$ is three metres from the origin in the negative direction. Time $t$ is measured with a clock, and the motion is described by giving the position at every moment.

When an object moves from the position $x_1$ to the position $x_2$, its **displacement** is the change in position $\Delta x = x_2 - x_1$. Displacement is a vector quantity: it has a magnitude and a direction, and on a line the direction is given by the sign. Plus means the positive direction and minus the opposite one. Displacement is not the same thing as the **distance travelled** $s$. The distance is the length of the route, and it cannot be negative. If a cyclist rides to the shop and back, the distance is four kilometres, but the displacement is zero, because the final position is the same as the initial position.

<svg data-fig="displacement" viewBox="0 0 600 392" role="img" aria-label="Schematic picture of two displacements on the x-axis, with the axis drawn to scale. At the top an object moves from the position x1 = 2 m to the position x2 = 8 m, so the displacement is +6 m and points to the right. At the bottom an object moves from the position x1 = 8 m to the position x2 = 3 m, so the displacement is −5 m and points to the left." style="max-width:100%;font-size:24px">
  <line x1="50" y1="104" x2="482" y2="104" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,104 L481,110 L481,98 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="100" x2="70" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="150" y1="100" x2="150" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="230" y1="100" x2="230" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="310" y1="100" x2="310" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="390" y1="100" x2="390" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="470" y1="100" x2="470" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="502" y="89.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="222.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\Delta x = +6\,\text{m}$</div></foreignObject>
  <line x1="150" y1="62" x2="371" y2="62" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M390,62 L370,71 L370,53 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="150" cy="104" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="390" cy="104" r="9" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="133.5" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="373.5" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
  <line x1="24" y1="198" x2="576" y2="198" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <line x1="50" y1="304" x2="482" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,304 L481,310 L481,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="300" x2="70" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="150" y1="300" x2="150" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="230" y1="300" x2="230" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="310" y1="300" x2="310" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="390" y1="300" x2="390" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="470" y1="300" x2="470" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="502" y="289.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="242.5" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta x = -5\,\text{m}$</div></foreignObject>
  <line x1="390" y1="262" x2="209" y2="262" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <path d="M190,262 L210,253 L210,271 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="390" cy="304" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="190" cy="304" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="373.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="173.5" y="347.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
</svg>

<svg data-fig="round-trip" viewBox="0 0 600 322" role="img" aria-label="Schematic picture, not to scale: a cyclist rides from home to the shop, two kilometres, and back home, another two kilometres. The distance travelled is s = 2 km + 2 km = 4 km, but the final position is the same as the initial position, so the displacement is zero." style="max-width:100%;font-size:24px">
  <line x1="50" y1="120" x2="468" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M480,120 L467,126 L467,114 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="116" x2="110" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="100" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="260" y1="116" x2="260" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="410" y1="116" x2="410" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="400" y="131.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="488" y="105.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{km})$</div></foreignObject>
  <rect x="90" y="96" width="40" height="24" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M84,96 L110,76 L136,96 Z" fill="#b8622d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="386" y="90" width="48" height="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="382" y="90" width="56" height="10" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="110" y1="64" x2="391" y2="64" stroke="#1971c2" stroke-width="5" stroke-linecap="butt"/>
  <path d="M410,64 L390,73 L390,55 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="162.5" y="15.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{outward trip } 2\,\text{km}$</div></foreignObject>
  <line x1="410" y1="184" x2="129" y2="184" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <path d="M110,184 L130,175 L130,193 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="168.5" y="199.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{return trip } 2\,\text{km}$</div></foreignObject>
  <line x1="24" y1="238" x2="576" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="196" y="251.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s = 2\,\text{km} + 2\,\text{km} = 4\,\text{km}$</div></foreignObject>
  <foreignObject x="233.5" y="285.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta x = x_2 - x_1 = 0$</div></foreignObject>
</svg>

```pysahdy
A cyclist rides to the shop and back. Why is the displacement zero even though the cyclist has ridden several kilometres?
---
Displacement depends only on the difference between the initial and final positions, and they are the same. The distance is the length of the route, so it is still four kilometres.
```

**Velocity** tells how fast and in which direction the position changes. It is also a vector quantity, and its sign tells the direction. The absolute value of the velocity $|v|$ is the speed. In uniform motion the velocity stays constant: the position changes by the same amount in every time interval of equal length.

<figure class="unit-photo"><img src="pics/fy4/highway-light-trails.webp" alt="A curving motorway at night: red and white streaks of light, street lamps and snowy verges."><figcaption>In a night photo with a long exposure time, vehicle lights draw streaks. The red streaks are rear lights, the white ones headlights.</figcaption></figure>

Motion can be shown as a **$(t,x)$ graph**, with time on the horizontal axis and position on the vertical axis. The graph of uniform motion is a straight line. The slope of the line is the velocity. The greater the absolute value of the slope, the greater the speed of the object, and the sign of the slope tells the direction of the motion: a rising line means motion in the positive direction, a falling line motion in the negative direction and a horizontal line being at rest. The graph is not a picture of the path of the object: a rising line does not mean uphill, but that the position increases.

```pysahdy
In a position–time graph a straight line slopes downwards to the right. Is the object moving uphill, downhill or in some other way?
---
The graph does not show the path. A falling line means that the position $x$ decreases, so the object moves in the negative direction.
```

## Formula: Average velocity and the equation of uniform motion
When the position changes by $\Delta x$ during the time interval $\Delta t = t_2 - t_1$, the average velocity is the displacement divided by the time:
```kaavat
average velocity :: v_\text{k} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}
```
where $v_\text{k}$ is the average velocity (m/s), $\Delta x$ the displacement (m), $\Delta t$ the elapsed time (s) and $x_1$ and $x_2$ the positions (m) at the moments $t_1$ and $t_2$. As vectors, the velocity is written $\overline{v}$ and the displacement $\Delta\overline{x}$. On a line we use their components $v$ and $\Delta x$, whose sign tells the direction.

In uniform motion the average velocity is the same over any time interval, and it is called the velocity $v$. In non-uniform motion the average velocity only tells the constant velocity at which the same displacement would be covered in the same time. If the object is at the position $x_0$ at the moment $t = 0$, solving the formula for the position gives the position as a function of time:
```latex
x = x_0 + v\,t
```
where $x$ is the position at the moment $t$ (m), $x_0$ the initial position (m), $v$ the velocity (m/s) and $t$ the time (s). This is the equation of the straight line in the $(t,x)$ graph: $x_0$ is where the line crosses the position axis and $v$ is its slope.

<svg data-fig="graph-slope" viewBox="0 0 600 330" role="img" aria-label="Schematic picture of two (t,x) graphs, without numerical values. On the left a straight line rises from the initial position x0, and two points have been chosen on the line: the time interval Δt and the change in position Δx form a triangle, with the help of which the velocity v is Δx divided by Δt. On the right three lines from the same initial position: the rising line is the velocity v greater than zero, the horizontal line is the velocity zero and the falling line is the velocity less than zero." style="max-width:100%;font-size:24px">
  <line x1="49" y1="290" x2="264" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M276,290 L263,296 L263,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="291" x2="50" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,44 L56,57 L44,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="282" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="40" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="50,246 250,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="110,206.5 210,206.5 210,140.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="50" cy="246" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="110" cy="206.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="210" cy="140.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="143.5" y="216" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="222" y="159" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta x$</div></foreignObject>
  <foreignObject x="7" y="231.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x_0$</div></foreignObject>
  <foreignObject x="62" y="76" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v = \dfrac{\Delta x}{\Delta t}$</div></foreignObject>
  <line x1="339" y1="290" x2="504" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M516,290 L503,296 L503,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="340" y1="291" x2="340" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M340,44 L346,57 L334,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="522" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="330" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="340,180 490,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v > 0$</div></foreignObject>
  <polyline points="340,180 490,180" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="165.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$v = 0$</div></foreignObject>
  <polyline points="340,180 490,246" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="500" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v < 0$</div></foreignObject>
  <circle cx="340" cy="180" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="297" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x_0$</div></foreignObject>
</svg>

The slope is calculated by choosing two points far apart on the line and dividing the change in position by the change in time. In a graph drawn from measured points, a line is fitted through the points so that the points lie evenly on both sides of it. The slope is calculated from the line, not from two neighbouring measured points, because every measurement has a small error.

## Worked example
A jogger runs at a uniform velocity. From the graph we read that at the moment $t = 0$ she is at the position $20\,\text{m}$ and at the moment $t = 40\,\text{s}$ at the position $120\,\text{m}$. What is the jogger's velocity, and where is she at the moment $t = 60\,\text{s}$?

<svg data-fig="jogger-graph" viewBox="0 0 600 340" role="img" aria-label="(t,x) graph to scale: a straight line rises from the position 20 metres at the moment 0 to the position 120 metres at the moment 40 seconds and continues as a dashed line to the position 170 metres at the moment 60 seconds." style="max-width:100%;font-size:24px">
  <line x1="200" y1="296" x2="200" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308" y1="296" x2="308" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="296" x2="416" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="272.5" x2="470" y2="272.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="155.5" x2="470" y2="155.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="97" x2="470" y2="97" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="296" x2="484" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,296 L483,302 L483,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="297" x2="92" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,36 L98,49 L86,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="200" y1="296" x2="200" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="183.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="308" y1="296" x2="308" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="291.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="416" y1="296" x2="416" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="399.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="85" y1="272.5" x2="92" y2="272.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="258" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="155.5" x2="92" y2="155.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="141" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <line x1="85" y1="97" x2="92" y2="97" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="82.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$170$</div></foreignObject>
  <foreignObject x="62" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="281.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="82" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <polyline points="92,272.5 308,155.5" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="308,155.5 416,97" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <line x1="308" y1="155.5" x2="308" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="155.5" x2="308" y2="155.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="416" y1="97" x2="416" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="97" x2="416" y2="97" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="92" cy="272.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="308" cy="155.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="416" cy="97" r="7" fill="#ffffff" stroke="#1971c2" stroke-width="3"/>
</svg>

<!-- vaihe -->

**Given and find.** Two points are read from the graph: $(t_1;\, x_1) = (0\,\text{s};\, 20\,\text{m})$ and $(t_2;\, x_2) = (40\,\text{s};\, 120\,\text{m})$. We are asked for the velocity $v$ and the position $x$ at the moment $t = 60\,\text{s}$.

<!-- vaihe -->

**Principle.** The jogger's motion is uniform, so the velocity stays constant and the $(t, x)$ graph is a straight line. Then the velocity is the slope of the line, that is the change in position divided by the change in time. Once the velocity is known, the position is obtained by adding the product of the velocity and the time to the initial position.

<!-- vaihe -->

**Formula solved.** The velocity and the position are solved symbolically before using numbers:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
x &= x_1 + v\,t
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The positions are in metres and the times in seconds, so the velocity comes directly in the unit $\text{m/s}$. No conversions are needed. The initial position is $x_1 = 20\,\text{m}$ at the moment $t_1 = 0$, so $60\,\text{s}$ can be used directly as the time $t$.

<!-- vaihe -->

**Substitution.** Substitute the numerical values with their units:
```latex
\begin{aligned}
v &= \frac{x_2 - x_1}{t_2 - t_1} \\
&= \frac{120\,\text{m} - 20\,\text{m}}{40\,\text{s} - 0\,\text{s}} \\
&= 2.5\,\text{m/s}
\\[4pt]
x &= x_1 + v\,t \\
&= 20\,\text{m} + 2.5\,\text{m/s} \cdot 60\,\text{s} \\
&= 20\,\text{m} + 150\,\text{m} \\
&= 170\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Result.** The velocity is $v = 2.5\,\text{m/s}$ and the position at the moment $60\,\text{s}$ is $x = 170\,\text{m}$. The whole numbers read from the graph, $0\,\text{s}$, $40\,\text{s}$, $20\,\text{m}$ and $120\,\text{m}$, are taken as exact values, so the results need no rounding: they are exact values of this model.

<!-- vaihe -->

**Reasonableness.** During the first $40\,\text{s}$ the position grew by $100\,\text{m}$, so during the next $20\,\text{s}$ it grows by half of that, $50\,\text{m}$. The position is $120\,\text{m} + 50\,\text{m} = 170\,\text{m}$, the same result. The velocity $2.5\,\text{m/s}$ is about $9\,\text{km/h}$, which is the speed of jogging. The velocity is positive, because the graph rises.

## Common misconception
A $(t,x)$ graph is not a picture of the path of the object: a rising line does not mean uphill, but that the position increases. Another mistake is to think of a negative velocity as a slow velocity. The sign only tells the direction: the velocity $-3\,\text{m/s}$ is greater in magnitude than $+2\,\text{m/s}$. A third mistake is to draw a conclusion about the velocity from the position: an object can be ahead and still move more slowly.

## Summary
- The position $x$ tells where the object is relative to the origin. The displacement $\Delta x = x_2 - x_1$ is the change in position, and its sign tells the direction. The distance is the length of the route and is not negative.
- The velocity $v = \Delta x / \Delta t$ is a vector quantity. In uniform motion it is constant, and the position is $x = x_0 + v\,t$.
- In a $(t,x)$ graph the line of uniform motion is straight. Its slope is the velocity, and its sign tells the direction.
- A line is fitted to measured data, and the velocity is calculated from points chosen far apart on the line.
- The average velocity of a back-and-forth motion can be zero even though the distance is not zero.
