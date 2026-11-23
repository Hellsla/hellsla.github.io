# Motion as graphs

> **Why** can you work out the distance between tram stops from the tram's velocity graph, even though the graph does not contain a single metre?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a city street on a summer morning. In the middle of the street a tram runs along the rails to the right, with motion lines behind it. On the left and the right there are glass tram shelters. Above the tram an overhead wire runs between poles. In the background there are blocks of flats and birches. The picture has no text and no people." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-liike-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

Motion is always described in a chosen coordinate system: a straight $x$ axis, an origin, a positive direction and a clock. The **position** $x$ tells you where a body is, the **displacement** $\Delta x$ the change in position and the **velocity** $v$ how fast and in which direction the position changes. The **acceleration** $a$ tells you how fast the velocity changes. The sign of the displacement, the velocity and the acceleration gives the direction. The distance is the length of the route, and it is never negative.

The same motion can be shown as three graphs: $(t,x)$, $(t,v)$ and $(t,a)$. You move between the graphs in two ways. Downwards: the **slope** of a graph is the value of the next quantity, so the slope of the $(t,x)$ graph is the velocity and the slope of the $(t,v)$ graph the acceleration. Upwards: the **area** between a graph and the time axis is the change in the previous quantity, so the area of the $(t,v)$ graph is the displacement.

```pysahdy
What does the slope of a $(t,x)$ graph tell, and what does the area under a $(t,v)$ graph tell?
---
The slope of a $(t,x)$ graph is the velocity and the area under a $(t,v)$ graph is the displacement.
```

<svg data-fig="kartta" viewBox="0 0 380 724" role="img" aria-label="Recognition chart: how do I tell which law to use? See what the task gives or which graph is given. Constant velocity: position in time, x equals x zero plus v t. Constant acceleration: velocity in time, v equals v zero plus a t. Constant acceleration and the distance is asked: position, x equals x zero plus v zero t plus half a t squared. Constant acceleration, a not known: average velocity, so the displacement is the mean of the initial and final velocity times the time. Velocity from the position graph: the slope, v equals delta x per delta t. Acceleration from the velocity graph: the slope, a equals delta v per delta t. Distance from the velocity graph: the area between the graph and the time axis." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="680" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{graph or formula? see what you know}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{constant velocity}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{position in time}$</div></foreignObject>
  <rect x="246" y="142" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="144" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$x = x_0 + vt$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{acceleration is constant}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{velocity in time}$</div></foreignObject>
  <rect x="246" y="228" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="230" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = v_0 + at$</div></foreignObject>
  <line x1="14" y1="321" x2="30" y2="321" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{constant acceleration, distance?}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{position in time}$</div></foreignObject>
  <rect x="142" y="343" width="220" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="146" y="346" width="212" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$x = x_0 + v_0 t + \tfrac12 at^2$</div></foreignObject>
  <line x1="14" y1="422" x2="30" y2="422" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="386" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="396.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{constant acceleration, a not known}$</div></foreignObject>
  <line x1="40" y1="426" x2="362" y2="426" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="431" width="154" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{average velocity}$</div></foreignObject>
  <rect x="212" y="430" width="150" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="432" width="142" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta x = \tfrac{v_0 + v}{2}\,t$</div></foreignObject>
  <line x1="14" y1="508" x2="30" y2="508" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="472" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="482.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{velocity from the position graph}$</div></foreignObject>
  <line x1="40" y1="512" x2="362" y2="512" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="517" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{slope}$</div></foreignObject>
  <rect x="238" y="516" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="518" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = \Delta x/\Delta t$</div></foreignObject>
  <line x1="14" y1="594" x2="30" y2="594" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="558" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="568.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{acceleration from the velocity graph}$</div></foreignObject>
  <line x1="40" y1="598" x2="362" y2="598" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="603" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{slope}$</div></foreignObject>
  <rect x="238" y="602" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="604" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$a = \Delta v/\Delta t$</div></foreignObject>
  <line x1="14" y1="680" x2="30" y2="680" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="644" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="654.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{distance from the velocity graph}$</div></foreignObject>
  <line x1="40" y1="684" x2="362" y2="684" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="689" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{under the graph}$</div></foreignObject>
  <rect x="246" y="688" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="690" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\text{area}$</div></foreignObject>
</svg>

A motion problem in the exam starts with choosing the coordinate system and identifying the type of motion: is the velocity constant or the acceleration constant? Only then do you write the equation.

This answers the opening question. The velocity tells you how many metres the tram travels in a second, so the product of velocity and time is in metres. The area under the $(t,v)$ graph is exactly this product added up over the whole trip, that is, the displacement. The tram in the Investigate task travelled $450\,\text{m}$ from one stop to the next.

## Formula: Equations and graphs of motion

### Uniform motion

The average velocity is the displacement divided by the time it took:

```kaavat
average velocity :: \overline{v}_\text{k} = \frac{\Delta\overline{x}}{\Delta t}
```

where $\Delta\overline{x}$ is the displacement ($\text{m}$) and $\Delta t$ the time elapsed ($\text{s}$). In linear motion the signed displacement $\Delta x = x_2 - x_1$ is enough, and the average velocity is $v_\text{k} = \tfrac{\Delta x}{\Delta t}$. When the velocity $v$ is constant and the body is at the position $x_0$ at $t = 0$,

```latex
x = x_0 + v\,t
```

This is the straight line of the $(t,x)$ graph: $x_0$ is its intercept on the position axis and $v$ its slope. The position is directly proportional to the time only when $x_0 = 0$.

### Uniformly accelerated motion

Acceleration is the change in velocity per unit of time:

```kaavat
average acceleration :: \overline{a}_\text{k} = \frac{\Delta\overline{v}}{\Delta t}
```

where $\Delta\overline{v}$ is the change in velocity ($\text{m/s}$), $\Delta t$ the elapsed time ($\text{s}$) and $\overline{a}_\text{k}$ the average acceleration ($\text{m/s}^2$). In rectilinear motion the signed acceleration $a = \tfrac{\Delta v}{\Delta t}$ is enough, and with a constant acceleration the average acceleration equals the instantaneous one.

When the acceleration is constant and the motion rectilinear, the velocity and the position at time $t$ are

```kaavat
velocity in uniformly accelerated linear motion :: v = v_0 + a\,t
position in uniformly accelerated linear motion :: x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
```

where $v_0$ is the initial velocity ($\text{m/s}$) and $a$ the acceleration ($\text{m/s}^2$). The speed increases when $a$ and $v$ point in the same direction and decreases when they point in opposite directions. In free fall $a = g = 9.81\,\text{m/s}^2$ downwards when air resistance is small.

```pysahdy
A body moves in the positive direction and its acceleration is negative. Does the speed increase or decrease?
---
The speed decreases, because the velocity and the acceleration point in opposite directions.
```

### Slope and area

The instantaneous velocity on a curved $(t,x)$ graph is the slope $k$ of the tangent. A ratio calculated through two points of the curve is the average velocity. The displacement is the area between the $(t,v)$ graph and the time axis, and the part below the axis is counted as negative.

```pysahdy
Part of a $(t,v)$ graph lies below the time axis. How does this part affect the displacement?
---
The area below the axis is counted as negative, so it reduces the displacement.
```

<svg data-fig="kuvaajat" viewBox="0 0 440 650" role="img" aria-label="Schematic of one motion as two graphs with the same time axis. Below, the velocity graph: the velocity grows uniformly from zero until t1, stays constant until t2 and falls uniformly to zero at t3. The region under the graph is coloured green, and its area is the displacement Δx. Above, the position graph: first a curve bending upwards, then a rising straight line and finally a curve that levels off to horizontal. Over the whole motion the position grows by Δx in total. A blue tangent is drawn at the point P of the curve; its slope k is the velocity v_P, and the same value is marked in the lower graph." style="max-width:100%;font-size:21px">
  <line x1="49" y1="280" x2="370" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,280 L369,286 L369,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="281" x2="50" y2="60" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,48 L56,61 L44,61 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="127.5" y1="280" x2="127.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="244" y1="280" x2="244" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="321" y1="280" x2="321" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="267.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="40" y="19.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$x$</div></foreignObject>
  <line x1="49" y1="590" x2="370" y2="590" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,590 L369,596 L369,584 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="591" x2="50" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,388 L56,401 L44,401 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="127.5" y1="590" x2="127.5" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="244" y1="590" x2="244" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="321" y1="590" x2="321" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="577.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="40" y="359.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$v$</div></foreignObject>
  <polygon points="50,590 127.5,451.5 244,451.5 321,590" fill="#b2f2bb" fill-opacity="0.8"/>
  <line x1="127.5" y1="241" x2="127.5" y2="451.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="244" y1="124.5" x2="244" y2="451.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="321" y1="85.5" x2="321" y2="590" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="50,280 52.5,280 54.5,280 57,279.5 59,279.5 61.5,279 63.5,279 66,278.5 68,278 70.5,277.5 72.5,276.5 75,276 77,275 79.5,274.5 81.5,273.5 84,272.5 86,271.5 88.5,270.5 90.5,269.5 93,268 95,267 97.5,265.5 99.5,264 102,262.5 104,261 106.5,259.5 109,257.5 111,256 113.5,254 115.5,252 118,250 120,248 122.5,246 124.5,244 127,242 129,239.5 131.5,237 133.5,235 136,232.5 138,230.5 140.5,228 142.5,226 145,223.5 147,221.5 149.5,219 151.5,217 154,214.5 156,212.5 158.5,210 161,207.5 163,205.5 165.5,203 167.5,201 170,198.5 172,196.5 174.5,194 176.5,192 179,189.5 181,187.5 183.5,185 185.5,183 188,180.5 190,178 192.5,176 194.5,173.5 197,171.5 199,169 201.5,167 203.5,164.5 206,162.5 208,160 210.5,158 213,155.5 215,153.5 217.5,151 219.5,149 222,146.5 224,144 226.5,142 228.5,139.5 231,137.5 233,135 235.5,133 237.5,130.5 240,128.5 242,126 244.5,124 246.5,121.5 249,119.5 251,117.5 253.5,115.5 255.5,113.5 258,111.5 260,109.5 262.5,108 264.5,106 267,104.5 269.5,103 271.5,101.5 274,100 276,99 278.5,97.5 280.5,96.5 283,95 285,94 287.5,93 289.5,92 292,91 294,90.5 296.5,89.5 298.5,89 301,88 303,87.5 305.5,87 307.5,86.5 310,86.5 312,86 314.5,86 316.5,85.5 319,85.5 321,85.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="321,85.5 352,85.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="50,590 127.5,451.5 244,451.5 321,590 352,590" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90.5,270.5 158.5,223" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <line x1="104" y1="261" x2="104" y2="493" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="104" cy="261" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="73" y="244.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$P$</div></foreignObject>
  <foreignObject x="164.5" y="238.5" width="52" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px;color:#1971c2">$k = v_\text{P}$</div></foreignObject>
  <circle cx="104" cy="493" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="62" y="466.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$v_\text{P}$</div></foreignObject>
  <foreignObject x="170.5" y="515" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
  <line x1="350" y1="280" x2="356" y2="280" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="350" y1="85.5" x2="356" y2="85.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="356" y1="280" x2="356" y2="85.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="364" y="170.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
  <foreignObject x="112.5" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_1$</div></foreignObject>
  <foreignObject x="229" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_2$</div></foreignObject>
  <foreignObject x="306" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_3$</div></foreignObject>
  <foreignObject x="21" y="597.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
  <foreignObject x="21" y="287.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
</svg>

In uniformly accelerated motion the velocity changes uniformly from the initial velocity $v_0$ to the final velocity $v$ ($\text{m/s}$) in the time $t$ ($\text{s}$). The $(t,v)$ graph is then a straight line, and the region under it is a trapezium.

<svg data-fig="puolisuunnikas" viewBox="0 0 440 330" role="img" aria-label="Schematic of the velocity graph of uniformly accelerated motion, no numerical values. The velocity grows uniformly from the initial velocity v0 at the instant 0 to the velocity v at the instant t, so the graph is a rising straight line. Between the graph and the time axis there is a green trapezium, whose area is the displacement Δx. The parallel sides of the trapezium are v0 and v, and the distance between them is t." style="max-width:100%;font-size:21px">
  <line x1="59" y1="280" x2="370" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,280 L369,286 L369,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="281" x2="60" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M60,28 L66,41 L54,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="317" y1="280" x2="317" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="267.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="50" y="-0.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$v$</div></foreignObject>
  <polygon points="60,280 60,206 317,94.5 317,280" fill="#b2f2bb" fill-opacity="0.8"/>
  <line x1="317" y1="94.5" x2="317" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="60" y1="94.5" x2="317" y2="94.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="60,206 317,94.5" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="60" cy="206" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="317" cy="94.5" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="18" y="193.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$v_0$</div></foreignObject>
  <foreignObject x="29" y="82" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$v$</div></foreignObject>
  <foreignObject x="307.5" y="291.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="31" y="287.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
  <foreignObject x="173.5" y="223" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
</svg>

```johda
A body moves along a straight line with uniform acceleration, and its velocity changes from the initial velocity $v_0$ to $v$ in the time $t$. Derive the displacement $\Delta x$ of the body in terms of the velocities $v_0$ and $v$ and the time $t$.
---
The displacement is $\Delta x = x - x_0$. The position in uniformly accelerated linear motion gives it in terms of the initial velocity, the acceleration and the time:

$$\Delta x = x - x_0 = v_0\,t + \tfrac{1}{2}\,a\,t^2$$

The acceleration is not in the result asked for, so it is expressed in terms of the velocities. The velocity in uniformly accelerated linear motion is $v = v_0 + a\,t$, so

$$a\,t = v - v_0$$

Write the last term as $\tfrac{1}{2}\,(a\,t)\,t$ and substitute $a\,t$ into it:

$$\Delta x = v_0\,t + \tfrac{1}{2}\,(v - v_0)\,t$$

Expand the bracket and combine the terms with the initial velocity:

$$\Delta x = \tfrac{1}{2}\,v_0\,t + \tfrac{1}{2}\,v\,t = \frac{v_0 + v}{2}\,t$$

The same result is the area under the $(t,v)$ graph: the parallel sides of the trapezium are $v_0$ and $v$, its height is $t$, and its area is the mean of the sides times the height. In uniformly accelerated motion the average velocity is therefore the mean of the initial and final velocities.
```

### Two bodies and measurement data

The positions of two bodies are written in the same coordinate system, and the bodies meet when

```latex
x_\text{A}(t) = x_\text{B}(t)
```

In a $(t,x)$ graph a meeting is the crossing point of the lines. The upper line means a greater position coordinate. When the body behind is slower at first and accelerates, the distance between the bodies is at its greatest when their velocities are equal.

A straight line or a quadratic polynomial $x = A\,t^2 + B\,t + C$ is fitted to measured points. The acceleration is found from the coefficient of the polynomial: $a = 2A$.

## Common mistakes {Virheet}

- **The $(t,x)$ graph is read as a picture of the route.** A rising line means that the position grows, not an uphill.
- **The velocity is read as $x : t$ when it should be $\Delta x : \Delta t$.** The initial position is not velocity.
- **The slope from two adjacent measured points.** Read it from the fitted line or the tangent, from two points far apart.
- **A negative acceleration is always read as slowing down.** The speed decreases only when the acceleration and the velocity point in opposite directions.
- **At the highest point the acceleration is zero.** The velocity is zero for an instant, but the acceleration is still $g$ downwards.
- **The crossing point of $(t,v)$ graphs is read as a meeting.** There the velocities are equal; at a meeting it is the positions that are equal.
- **Mixed-up units.** Convert the units before you substitute, by writing them out: $$
\begin{aligned}
&72\,\text{km/h} \\
&= \dfrac{72 \cdot 1000\,\text{m}}{3600\,\text{s}} \\
&= 20\,\text{m/s}
\end{aligned}
$$.

## Review if needed {Kertaa}

- Uniform motion, $x = x_0 + vt$ and unit conversions: [*Uniform motion: speed, position and graphs*](fy1-5.html).
- Position, displacement, average velocity and the slope of the $(t,x)$ graph: [*Position, velocity and uniform motion as graphs*](fy4-1.html).
- Acceleration, the tangent, the area and free fall: [*Acceleration and uniformly accelerated motion*](fy4-2.html).
- Meeting, overtaking and the greatest distance: [*Comparing the motions of two bodies*](fy4-12.html).
- Fitting a straight line and the slope from data: [*Graphing and fitting a straight line*](fy1-4.html). Measurement uncertainty: [*Measuring and the reliability of a measurement*](fy1-3.html).
