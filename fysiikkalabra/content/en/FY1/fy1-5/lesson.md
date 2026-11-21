# Uniform motion: speed, position and graphs

> **Why** can the position of the Voyager 2 probe be calculated in advance for any day, even though it is more than 20 billion kilometres from the Sun?

<svg data-fig="hero" data-style="house" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the Sun and the orbits of the planets on the left, the Voyager 2 probe far away in space on the right. Behind the probe, marks of its earlier positions lie evenly spaced on a straight track, one for each equal time step; the next positions continue ahead as a dashed line." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
Uniform motion is motion along a straight line at constant speed: in equal intervals of time, the object travels equal distances. Speed tells you how far the object travels in one second, so its unit is metres per second (m/s). If a trolley moves two metres every second, its speed is $2\,\text{m/s}$.

<svg data-fig="motion" data-style="house" viewBox="0 0 600 330" role="img" aria-label="Motion diagram in which the same trolley is drawn at five consecutive instants: 0 s, 1 s, 2 s, 3 s and 4 s. The gaps between the trolleys are equal, and under each gap there is an equally long bracket Δs: in uniform motion an object travels equal distances in equal intervals of time. The gaps are drawn to scale, and the trolleys are the same size." style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-5-motion.webp" x="0" y="-1.2" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="20" y="175.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 0\,\text{s}$</div></foreignObject>
  <foreignObject x="155" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{s}$</div></foreignObject>
  <foreignObject x="270" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2\,\text{s}$</div></foreignObject>
  <foreignObject x="385" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3\,\text{s}$</div></foreignObject>
  <foreignObject x="500" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4\,\text{s}$</div></foreignObject>
  <foreignObject x="96" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="111" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="226" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="341" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="456" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="80" y="301.5" width="440" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{equal distances in equal intervals of time}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy1/city-highway-light-trails.webp" alt="A city motorway at night: white streaks of light on the left lanes and red ones on the right, street lamps along the road and tall buildings behind."><figcaption>With a long exposure the lights of cars draw lines in the picture: the white ones are headlights and the red ones rear lights. The photo records the path of the motion, but it does not show whether the motion was uniform.</figcaption></figure>

### Direct proportionality
Two quantities are directly proportional if their ratio is always the same. When uniform motion starts from the zero point, the position $s$, which here equals the distance travelled, and the time $t$ are directly proportional: double the time gives double the distance, and the ratio $s : t$ is the speed $v$. In a $(t, s)$ graph this shows as a straight line through the origin.

```pysahdy
A trolley starts from the zero point and travels $6\,\text{m}$ in $3\,\text{s}$. How far does it travel in $9\,\text{s}$ at the same speed?
---
The time becomes three times as long, so the distance also becomes three times as long: $18\,\text{m}$. The distance is directly proportional to time.
```

### Linear model
Uniform motion is a model, not reality. A cyclist pedals unevenly, and Voyager 2 slows down slightly because of the Sun's gravity. The model is still good when the speed changes only a little during the time being considered. Its graph is a straight line, and a straight line is described by a linear model: the position changes by the same amount every second. Values calculated with the model are model values, which are compared with measurements.

## Formula: Uniform motion
Suppose that at the start of the observation ($t = 0$) an object is at position $s_0$ and moves along a straight line at constant speed $v$. Its position at time $t$ is
```latex
s = s_0 + v t
```
where $s$ is the position (m) measured from the chosen zero point, $s_0$ the initial position (m), $v$ the speed (m/s) and $t$ the time from the start (s). The distance travelled by the object is $\Delta s = s - s_0 = vt$. In the examples of this chapter the object moves in the positive direction, so the velocity is positive.

### Speed from a graph
The $(t, s)$ graph is a straight line, and the slope of the line is the speed:
```kaavat
average speed :: v = \frac{\Delta s}{\Delta t}
```
where $\Delta s$ is the change in position (m) and $\Delta t$ is its time interval (s). The line crosses the $s$-axis at the initial position $s_0$. If $s_0 = 0$, the position is directly proportional to time: $s = vt$. If $s_0 \neq 0$, the line is as steep as the line through the origin at the same speed, but shifted up or down. Then only the distance $\Delta s$, not the position $s$, is directly proportional to time.

<svg data-fig="graph" data-style="house" viewBox="0 0 600 360" role="img" aria-label="Graph drawn to scale: two uniform motions at a speed of 3 m/s are shown as straight lines in a (t, s) coordinate system. The lower line passes through the origin (initial position 0), and the upper line starts from the position s₀ = 5 m and is parallel to the lower line. A slope triangle is drawn on the lower line: in 2 s the position increases by 6 m, so the slope is 3 m/s, which is the speed." style="max-width:100%;font-size:24px">
  <line x1="165" y1="300" x2="165" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="233.5" y1="300" x2="233.5" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="302.5" y1="300" x2="302.5" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="371" y1="300" x2="371" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="440" y1="300" x2="440" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="204" x2="440" y2="204" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="108" x2="440" y2="108" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="458" y2="300" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M466,300 L454.5,305 L458,300 L454.5,295 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="42" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M96,34 L101,45.5 L96,42 L91,45.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="165" y1="300" x2="165" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="155" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="233.5" y1="300" x2="233.5" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="223.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="302.5" y1="300" x2="302.5" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="292.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="371" y1="300" x2="371" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="361" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="440" y1="300" x2="440" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="430" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="204" x2="96" y2="204" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="108" x2="96" y2="108" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="93.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="472" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <polyline points="96,300 440,156" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,252 440,108" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="89" y1="252" x2="96" y2="252" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="237.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$s_0$</div></foreignObject>
  <circle cx="96" cy="252" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="233.5" y1="242.5" x2="371" y2="242.5" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="371" y1="242.5" x2="371" y2="185" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="233.5" cy="242.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="371" cy="185" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="237.5" y="252" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t = 2\,\text{s}$</div></foreignObject>
  <foreignObject x="383" y="199" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta s = 6\,\text{m}$</span></div></foreignObject>
  <foreignObject x="448" y="141.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$s = vt$</div></foreignObject>
  <foreignObject x="448" y="93.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s = s_0 + vt$</div></foreignObject>
</svg>

```pysahdy
Two objects move at the same speed. One starts from the zero point and the other from position $5\,\text{m}$. How do their $(t, s)$ lines differ?
---
The lines are parallel, because the slope, which is the speed, is the same. The second line crosses the $s$-axis at $5\,\text{m}$, so it is shifted up.
```

### Units
Always convert to compatible units (usually SI units) before substituting: substitute the value of the unit in its place. For example $1\,\text{km} = 1000\,\text{m}$ and $1\,\text{h} = 3600\,\text{s}$, so $72\,\text{km/h} = \tfrac{72\cdot1000\,\text{m}}{3600\,\text{s}} = 20\,\text{m/s}$. In the same way $1\,\text{min} = 60\,\text{s}$. Distances on the scale of the Solar System are often given in astronomical units: $1\,\text{AU} = 149\,597\,870.7\,\text{km}$ is roughly the mean distance between the Earth and the Sun.

```pysahdy
A car drives at $90\,\text{km/h}$. How many metres does it travel in one second?
---
Substitute $1\,\text{km} = 1000\,\text{m}$ and $1\,\text{h} = 3600\,\text{s}$: $90\,\text{km/h} = \tfrac{90\cdot1000\,\text{m}}{3600\,\text{s}} = 25\,\text{m/s}$. The car travels $25\,\text{m}$ in one second.
```

## Worked example
Voyager 2 crossed the heliopause on 5 November 2018 at a distance of $s_0 = 119.0\,\text{AU}$ from the Sun (Burlaga et al. 2019, Nature Astronomy). The speed of the probe relative to the Sun at the crossing was $v = 15.341\,\text{km/s}$ (NASA/JPL). Assume the speed is constant. According to the model, how far from the Sun is the probe on 5 November 2026?

<!-- vaihe -->

**Given and find.**

- $s_0 = 119.0\,\text{AU}$ at time $t = 0$ (5 November 2018),
- $v = 15.341\,\text{km/s}$ and
- $1\,\text{AU} = 149\,597\,870.7\,\text{km}$.

The time interval from 5 November 2018 to 5 November 2026 is 8 years, including the leap days of 2020 and 2024: $8 \cdot 365 + 2 = 2922$ days.

The quantity to find is the distance $s$ from the Sun.

<!-- vaihe -->

**Principle.** When the speed is assumed constant, the probe moves uniformly and its position follows the linear model. The result is a model value, not a measurement: the Sun's gravity slows the probe slightly, by only about $0.1\,\text{km/s}$ over 2018–2026, which is negligible here.

<!-- vaihe -->

**Rearranged formula.**
```latex
s = s_0 + v t
```

<!-- vaihe -->

**Unit conversions.** The time is already in days, $t = 2922\,\text{days}$, so the speed is converted to AU/day. In place of the units we substitute $1\,\text{km} = \tfrac{1}{149\,597\,870.7}\,\text{AU}$ and $1\,\text{s} = \tfrac{1}{86\,400}\,\text{day}$: $v = 15.341\,\tfrac{\text{km}}{\text{s}} = 15.341 \cdot \tfrac{1}{149\,597\,870.7}\,\text{AU} : \left(\tfrac{1}{86\,400}\,\text{day}\right) = 0.0088602\,\tfrac{\text{AU}}{\text{day}}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
s &= s_0 + v t \\
&= 119.0\,\text{AU} \\
&\quad + 0.0088602\,\tfrac{\text{AU}}{\text{day}} \cdot 2922\,\text{days} \\
&= 119.0\,\text{AU} + 25.89\,\text{AU} \\
&= 144.89\,\text{AU}
\end{aligned}
```

<!-- vaihe -->

**Result.** According to the model, the probe is $s \approx 144.9\,\text{AU}$ from the Sun, about $2.17 \cdot 10^{10}\,\text{km}$. The initial distance is given to the nearest tenth, so the result is rounded to the nearest tenth.

<!-- vaihe -->

**Reasonableness.** A speed of $15\,\text{km/s}$ covers in a year about $15\,\text{km/s} \cdot 3.16 \cdot 10^{7}\,\text{s} \approx 4.7 \cdot 10^{8}\,\text{km} \approx 3.2\,\text{AU}$, so in 8 years the probe advances about $26\,\text{AU}$ and $119.0\,\text{AU} + 26\,\text{AU} \approx 145\,\text{AU}$.

For 15 February 2026 the same model gives a distance from the Sun of $142.6\,\text{AU}$. The NASA/JPL Voyager mission status page gave the probe's distance from the Earth in February 2026 as $143.05\,\text{AU}$.

The Earth orbits the Sun, so the probe's distance from the Earth differs from its distance from the Sun by up to about $1\,\text{AU}$ over the year.

The difference of $0.5\,\text{AU}$ is smaller than this: the model and the observation agree to within about $1\,\text{AU}$, and this comparison cannot test the model more precisely. That is less than one percent of the distance, so the constant-speed model suits predictions over a few years.

## Common misconception
Many people think that in uniform motion the position doubles when the time doubles. This happens only if the motion starts from the zero point. When a trolley starts at $s_0 = 6\,\text{m}$ and moves at $2.0\,\text{m/s}$, it is at $10\,\text{m}$ at $2.0\,\text{s}$ and at $14\,\text{m}$ at $4.0\,\text{s}$, not at $20\,\text{m}$. The distance, however, does double: $4.0\,\text{m}$ becomes $8.0\,\text{m}$. Another mistake is to calculate the speed as the quotient of position and time $s : t$ instead of the quotient of the change in position and the time interval: the speed is $\Delta s : \Delta t$, not $s : t$, when $s_0 \neq 0$.

## Summary
- In uniform motion the speed is constant, and the object travels equal distances in equal intervals of time: $s = s_0 + vt$.
- The distance travelled $\Delta s = vt$ is directly proportional to time. The position $s$ is proportional to time only when $s_0 = 0$.
- The $(t, s)$ graph is a straight line. Its slope $\Delta s : \Delta t$ is the speed, and the intercept on the $s$-axis is the initial position $s_0$.
- Convert units before calculating by substitution, for example $1\,\text{km} = 1000\,\text{m}$ and $1\,\text{h} = 3600\,\text{s}$.
- Uniform motion is a linear model. The values it gives are model values, which can be compared with measurements, such as the distance of Voyager 2.
