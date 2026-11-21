# Acceleration and uniformly accelerated motion

> **Why** does a stone dropped from a bridge travel a longer distance during each second than during the second before?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a footbridge for pedestrians and cyclists over a river on a summer day. In the middle of the bridge a young person drops a stone over the railing, and a friend on the bank films the fall with a phone. The stone is drawn at five positions at equal time intervals: the gaps grow downwards in the ratio 1 : 3 : 5 : 7, and the blue velocity arrow beside the stone grows by the same amount each time. The measuring rod on the right shows five heights: its alternately shaded parts are the distances travelled by the stone, and they grow in the ratio 1 : 3 : 5 : 7. At the lowest position the stone hits the water and the water splashes. The scale is not exact, but the ratios of the gaps are." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Acceleration tells you how the velocity changes
In the chapter *Position, velocity and uniform motion as graphs* the velocity stayed constant. In most motions, however, it changes: a car starts from a traffic light, a cyclist brakes and a dropped stone falls faster and faster. **Acceleration** $a$ tells you how much the velocity changes per unit of time. Its unit is $\tfrac{\text{m/s}}{\text{s}} = \text{m/s}^2$. An acceleration of $2.0\,\text{m/s}^2$ means that the velocity grows by $2.0\,\text{m/s}$ every second.

Acceleration is a vector quantity $\overline{a}$, like velocity $\overline{v}$, and in rectilinear motion its direction is given by its sign. When the acceleration and the velocity point in the same direction, the speed increases. When they point in opposite directions, the speed decreases. So a negative acceleration does not always mean slowing down: if an object moves in the negative direction and $a < 0$, its speed increases. Acceleration can exist even when the velocity is zero for a moment.

<svg data-fig="strobe" viewBox="0 0 600 368" role="img" aria-label="Schematic picture of two carts photographed at one-second intervals, the gaps to scale. At the top the cart starts from rest and accelerates: the gaps grow, the blue velocity arrow grows by the same amount every second, and the orange acceleration arrow points in the direction of motion and stays the same length. At the bottom the cart slows down: the gaps get shorter, the velocity arrow gets shorter, and the acceleration arrow points against the motion; in the last picture the cart is at rest for a moment, but the acceleration arrow is still the same." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-2-strobe.webp" x="-1.3" y="0" width="603" height="379.4" preserveAspectRatio="none"/>
  <foreignObject x="24" y="9.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{accelerating motion}\text{, frames } 1\,\text{s} \text{ apart}$</div></foreignObject>
  <foreignObject x="521" y="41.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="526" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="24" y="194.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{decelerating motion}\text{, frames } 1\,\text{s} \text{ apart}$</div></foreignObject>
  <foreignObject x="71" y="223.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="76" y="337.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

```pysahdy
A cart moves in the negative direction and its acceleration is $a < 0$. Does its speed increase or decrease?
---
It increases, because the velocity and the acceleration point the same way (both are negative).
```

### Uniformly accelerated motion and the $(t,v)$ graph
Motion is **uniformly accelerated** when the acceleration stays constant: the velocity changes by the same amount in every time interval of equal length. Then the **$(t,v)$ graph**, with time on the horizontal axis and velocity on the vertical axis, is a straight line. The slope of the line is the acceleration. A rising line means a positive acceleration, a horizontal line uniform motion and a falling line a negative acceleration.

<svg data-fig="tv-graph" viewBox="0 0 600 330" role="img" aria-label="Schematic picture of two (t,v) graphs, with no numerical values. On the left a straight line rises from the initial velocity v0, and two points chosen on the line bound a triangle: the time interval Δt and the change in velocity Δv, whose ratio is the acceleration a. On the right three lines from the same initial velocity: the rising line is acceleration a greater than zero, the horizontal line acceleration zero, that is, uniform motion, and the falling line acceleration less than zero." style="max-width:100%;font-size:24px">
  <line x1="49" y1="290" x2="250" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M262,290 L249,296 L249,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="291" x2="50" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,44 L56,57 L44,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="268" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="40" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polyline points="50,246 236,114" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="106,206.5 199,206.5 199,140.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="50" cy="246" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="106" cy="206.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="199" cy="140.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="136" y="216" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="211" y="159" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta v$</div></foreignObject>
  <foreignObject x="7" y="231.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="61" y="72" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$a = \dfrac{\Delta v}{\Delta t}$</div></foreignObject>
  <line x1="316" y1="30" x2="316" y2="300" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="359" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="360" y1="291" x2="360" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M360,44 L366,57 L354,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="532" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="350" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polyline points="360,180 500,103" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="88.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$a > 0$</div></foreignObject>
  <polyline points="360,180 500,180" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="165.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <polyline points="360,180 500,257" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="510" y="242.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a < 0$</div></foreignObject>
  <circle cx="360" cy="180" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="317" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
</svg>

### Instantaneous velocity is the slope of the tangent
When the velocity grows, the position changes more in each second than in the one before. That is why the $(t,x)$ graph is not a straight line but a curve that gets steeper. The velocity at a given moment, the **instantaneous velocity**, is found from the tangent of the curve: the line that just touches the curve at that point. Two points far apart are chosen on the tangent, and the instantaneous velocity is the change in position between them divided by the change in time. A ratio calculated through two points of the curve would give only the average velocity between them.

<svg data-fig="tangent" viewBox="0 0 600 340" role="img" aria-label="Schematic picture of a (t,x) graph, with no numerical values. The graph of a cart accelerating from rest is a curve bending upwards that gets steeper all the time. A tangent, that is, a line that just touches the curve at that point, is drawn as a dashed line at the point P of the curve. Two points far apart are chosen on the tangent, and their time interval Δt and change in position Δx form a triangle. The slope of the tangent, Δx divided by Δt, is the cart&#x27;s instantaneous velocity at the moment that P corresponds to." style="max-width:100%;font-size:24px">
  <line x1="69" y1="300" x2="454" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M466,300 L453,306 L453,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="301" x2="70" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M70,38 L76,51 L64,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="472" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="60" y="7.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <polyline points="70,300 73,300 76,300 79,300 82,300 85,299.5 88,299.5 90.5,299.5 93.5,299 96.5,299 99.5,298.5 102.5,298 105.5,298 108.5,297.5 111.5,297 114.5,296.5 117.5,296 120.5,295.5 123.5,295 126,294.5 129,294 132,293.5 135,292.5 138,292 141,291.5 144,290.5 147,290 150,289 153,288 156,287.5 159,286.5 162,285.5 164.5,284.5 167.5,283.5 170.5,282.5 173.5,281.5 176.5,280.5 179.5,279.5 182.5,278 185.5,277 188.5,276 191.5,274.5 194.5,273.5 197.5,272 200,271 203,269.5 206,268 209,266.5 212,265 215,263.5 218,262 221,260.5 224,259 227,257.5 230,256 233,254.5 236,252.5 238.5,251 241.5,249 244.5,247.5 247.5,245.5 250.5,244 253.5,242 256.5,240 259.5,238 262.5,236 265.5,234 268.5,232 271.5,230 274,228 277,226 280,224 283,221.5 286,219.5 289,217.5 292,215 295,213 298,210.5 301,208 304,205.5 307,203.5 310,201 312.5,198.5 315.5,196 318.5,193.5 321.5,191 324.5,188.5 327.5,185.5 330.5,183 333.5,180.5 336.5,177.5 339.5,175 342.5,172 345.5,169.5 348,166.5 351,163.5 354,161 357,158 360,155 363,152 366,149 369,146 372,143 375,140 378,136.5 381,133.5 384,130.5 386.5,127 389.5,124 392.5,120.5 395.5,117 398.5,114 401.5,110.5 404.5,107 407.5,103.5 410.5,100 413.5,97 416.5,93 419.5,89.5 422,86 425,82.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="181,300 432.5,107.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 7"/>
  <polyline points="255,243.5 418,243.5 418,119" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="255" cy="243.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="418" cy="119" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="292" cy="215" r="8" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="258" y="178.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="320" y="253" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="430" y="166.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta x$</div></foreignObject>
  <foreignObject x="440.5" y="107" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{tangent}$</div></foreignObject>
  <foreignObject x="85" y="73" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v = \dfrac{\Delta x}{\Delta t}$</div></foreignObject>
</svg>

```pysahdy
You draw a straight line through two points of a $(t,x)$ curve. What does the slope of the line tell you?
---
It gives the average velocity between the two points, not the instantaneous velocity at either point.
```

### Free fall
When air resistance is small, all objects fall with the same acceleration regardless of mass. This **acceleration of free fall** is $g = 9.81\,\text{m/s}^2$ at the Earth's surface, directed downwards. The velocity of a dropped stone therefore grows by about $9.8\,\text{m/s}$ every second. That is why the stone travels a longer distance in each second than in the one before: the distances that an object starting from rest covers in successive intervals of equal length are in the ratio $1 : 3 : 5 : 7$.

```pysahdy
You drop a tennis ball and a steel ball from the same height, and air resistance is small. Which one hits the ground first?
---
They hit the ground at the same time, because the acceleration of free fall does not depend on mass.
```

## Formula: Equations of uniformly accelerated motion
The average acceleration is the change in velocity divided by the time it took:
```kaavat
average acceleration :: a_\text{k} = \frac{\Delta v}{\Delta t}
```
where $a_\text{k}$ is the average acceleration ($\text{m/s}^2$), $\Delta v = v_2 - v_1$ the change in velocity ($\text{m/s}$) and $\Delta t$ the time it took ($\text{s}$). When the acceleration is constant, it equals the average acceleration at every moment, $a = a_\text{k}$. When timing starts at $t = 0$, when the velocity is $v_0$, the velocity changes by the amount $a$ every second:
```kaavat
velocity in uniformly accelerated linear motion :: v = v_0 + a\,t
```
where $v$ is the velocity at time $t$ ($\text{m/s}$), $v_0$ the initial velocity ($\text{m/s}$), $a$ the acceleration ($\text{m/s}^2$) and $t$ the time ($\text{s}$).

### The displacement is the area between the $(t,v)$ graph and the time axis
In uniform motion the displacement $v\,t$ is the area of the rectangle under the $(t,v)$ graph. The same holds when the velocity changes: the displacement is the area between the graph and the time axis, where the part below the time axis ($v < 0$) is counted as negative. In uniformly accelerated motion the region divides into a rectangle whose area is $v_0\,t$ and a triangle whose height is the growth of velocity $a\,t$ and whose width is $t$. The area of the triangle is $\tfrac{1}{2} \cdot a\,t \cdot t = \tfrac{1}{2}\,a\,t^2$.

<svg data-fig="area" viewBox="0 0 600 340" role="img" aria-label="Schematic picture of a (t,v) graph, with no numerical values. The velocity grows in a straight line from the initial velocity v0 at time 0 to the velocity v at time t. The region under the line is divided into two parts: a blue rectangle whose height is v0 and width t, and on top of it an orange triangle whose height is the growth of velocity at and width t. The area of the rectangle is v0 times t and the area of the triangle is half of a t times t; together they are the displacement Δx." style="max-width:100%;font-size:24px">
  <line x1="79" y1="300" x2="444" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,300 L443,306 L443,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="301" x2="80" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,38 L86,51 L74,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="462" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="70" y="7.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polygon points="80,300 395,300 395,217.5 80,217.5" fill="#d0e6fb" fill-opacity="0.9"/>
  <polygon points="80,217.5 395,217.5 395,99.5" fill="#ffc078" fill-opacity="0.75"/>
  <polyline points="80,217.5 395,99.5" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="395,300 395,99.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="80,217.5 395,217.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="80" cy="217.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395" cy="99.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="37" y="203" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="50" y="85" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v$</div></foreignObject>
  <line x1="73" y1="99.5" x2="80" y2="99.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="80" y1="99.5" x2="395" y2="99.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="385" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="208.5" y="244" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$v_0\,t$</div></foreignObject>
  <foreignObject x="234" y="160.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\tfrac{1}{2}\,a t\cdot t$</div></foreignObject>
  <foreignObject x="407" y="144" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$a t$</div></foreignObject>
  <foreignObject x="407" y="244" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_0$</div></foreignObject>
</svg>

When the object is at the position $x_0$ at time $t = 0$, its position is the initial position plus the displacement:
```kaavat
position in uniformly accelerated linear motion :: x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
```
where $x$ is the position at time $t$ ($\text{m}$) and $x_0$ the initial position ($\text{m}$); the other symbols are the same as above. When the time is asked for, this becomes a quadratic equation, and of its solutions you choose the one that fits the situation.

### Determining the acceleration of free fall from measurements
The position of a falling object is measured at many moments, for example from a video or with light gates. A quadratic polynomial $s = A\,t^2 + B\,t + C$ is fitted to the measured points with a calculator or a spreadsheet. In real series of measurements the points do not usually lie exactly on one curve because of measurement uncertainty, so the fit uses all the points at once. When the polynomial is compared with the equation of position, the coefficients of $t^2$ are the same, $A = \tfrac{1}{2}\,a$:
```latex
a = 2A
```
where $A$ is the coefficient of the $t^2$ term of the fitted polynomial ($\text{m/s}^2$). The coefficient $B$ is the initial velocity and $C$ the initial position.

<figure class="unit-photo"><img src="pics/fy4/gull-takeoff-multiple-exposure.webp" alt="The same gull in three successive images as it runs on the water and takes off."><figcaption>A gull taking off, shown as a multiple exposure: the same bird is photographed three times in a row in one picture.</figcaption></figure>

## Worked example
A cyclist reaches the top of a hill at $4.0\,\text{m/s}$ and stops pedalling. On the downhill her acceleration is $0.50\,\text{m/s}^2$, and the hill is $60\,\text{m}$ long. How long does the descent take, and what is her velocity at the bottom?

<!-- vaihe -->

**Given and find.** The initial velocity is $v_0 = 4.0\,\text{m/s}$, the acceleration $a = 0.50\,\text{m/s}^2$ and the displacement $\Delta x = x - x_0 = 60\,\text{m}$ in the direction of motion, which is chosen as positive. We are asked for the time $t$ and the velocity $v$ at the bottom.

<!-- vaihe -->

**Principle.** The acceleration is constant, so the motion is uniformly accelerated and the displacement is $\Delta x = v_0\,t + \tfrac{1}{2}\,a\,t^2$. The time is the unknown, and it appears in both the first and the second power, so we get a quadratic equation. Once the time is known, the velocity comes from the equation $v = v_0 + a\,t$.

<!-- vaihe -->

**Formula solved.** Write the equation in the form $\tfrac{1}{2}\,a\,t^2 + v_0\,t - \Delta x = 0$ and solve it with the quadratic formula. The positive solution is
```latex
t = \frac{-v_0 + \sqrt{v_0^2 + 2a\,\Delta x}}{a}
```

<!-- vaihe -->

**Unit conversions.** All quantities are in SI units (m, m/s, m/s²), so no conversions are needed. Under the root the unit is $\text{m}^2/\text{s}^2$, so the root is in $\text{m/s}$ and the time comes out in seconds.

<!-- vaihe -->

**Substitution.** First calculate the expression under the root and its square root, then the time and the velocity:
```latex
\begin{aligned}
&v_0^2 + 2a\,\Delta x \\
&= (4.0\,\text{m/s})^2 \\
&\quad + 2 \cdot 0.50\,\text{m/s}^2 \cdot 60\,\text{m} \\
&= 76\,\text{m}^2/\text{s}^2
\\[4pt]
&\sqrt{76\,\text{m}^2/\text{s}^2} \approx 8.72\,\text{m/s}
\\[4pt]
&t = \frac{-4.0\,\text{m/s} + 8.72\,\text{m/s}}{0.50\,\text{m/s}^2} \\
&\approx 9.44\,\text{s}
\\[4pt]
&v = v_0 + a\,t \\
&= 4.0\,\text{m/s} + 0.50\,\text{m/s}^2 \cdot 9.44\,\text{s} \\
&\approx 8.72\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Result.** The descent takes about $9.4\,\text{s}$, and the velocity at the bottom is about $8.7\,\text{m/s}$. Two significant figures, like the initial velocity $4.0\,\text{m/s}$ and the acceleration $0.50\,\text{m/s}^2$. The distance $60\,\text{m}$ is taken as an exact value. The other solution of the formula, $t \approx -25\,\text{s}$, is rejected because the motion starts at $t = 0$.

<!-- vaihe -->

**Reasonableness.** The velocity grows steadily, so the average velocity is the mean of the initial and final velocities, $$\begin{aligned} &(4.0\,\text{m/s} + 8.72\,\text{m/s}) : 2 \\ &\approx 6.36\,\text{m/s} \end{aligned}$$, and $6.36\,\text{m/s} \cdot 9.44\,\text{s} \approx 60\,\text{m}$, the length of the hill. The final velocity $8.7\,\text{m/s} \approx 31\,\text{km/h}$ is a usual cycling speed on a downhill.

## Common misconception
Many people think that the acceleration is zero whenever the velocity is zero. A ball thrown up is at rest for a moment at the highest point, but its velocity changes all the time: just before the highest point it moves up and just after it moves down. When air resistance is small, the acceleration is $g = 9.81\,\text{m/s}^2$ downwards during the whole flight. Another mistake is to take a negative acceleration to always mean slowing down: the speed decreases only when the acceleration and the velocity point in opposite directions. A third mistake is to think that a heavy object falls faster than a light one. When air resistance is small, both fall with the same acceleration.

## Summary
- The average acceleration $a_\text{k} = \tfrac{\Delta v}{\Delta t}$ tells you the change in velocity per unit of time, with the unit $\text{m/s}^2$. When the acceleration is constant, $a = a_\text{k}$. Acceleration is a vector quantity, and on a straight line its sign tells the direction.
- The speed increases when the acceleration and the velocity point in the same direction, and decreases when they point in opposite directions.
- In uniformly accelerated motion the $(t,v)$ graph is a straight line whose slope is the acceleration and whose signed area between it and the time axis is the displacement; the part below the time axis ($v < 0$) is counted as negative.
- $v = v_0 + a\,t$ and $x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$. The $(t,x)$ graph is a curve, and the instantaneous velocity is the slope of its tangent.
- In free fall the acceleration is $g = 9.81\,\text{m/s}^2$ downwards. It can be determined by fitting a quadratic polynomial to the measured points: $a = 2A$.
