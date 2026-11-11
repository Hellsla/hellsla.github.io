## fy9-liike-s1

### a)
**Given:** length of the lane $\Delta x = 270\,\text{m}$, velocity at the beginning of the lane $v_0 = 54\,\text{km/h}$ and at the end $v = 108\,\text{km/h}$; the acceleration is uniform
**Find:** the duration of the acceleration $t$ in seconds
**Principle:** The acceleration is constant, so the $(t,v)$ graph is a straight line and the region under it is a trapezium. The displacement is the area of this region, so the average velocity is the mean of the initial and final velocities (chapter *Acceleration and uniformly accelerated motion*). The acceleration is not needed to calculate the time.
**Formula:** $\Delta x = \dfrac{v_0 + v}{2}\,t$, so $t = \dfrac{2\,\Delta x}{v_0 + v}$
**Conversions:** $54\,\text{km/h} = \dfrac{54 \cdot 1000\,\text{m}}{3600\,\text{s}} = 15\,\text{m/s}$ and $108\,\text{km/h} = \dfrac{108 \cdot 1000\,\text{m}}{3600\,\text{s}} = 30\,\text{m/s}$
**Substitution:** $t = \dfrac{2 \cdot 270\,\text{m}}{15\,\text{m/s} + 30\,\text{m/s}} = \dfrac{540\,\text{m}}{45\,\text{m/s}} = 12.0\,\text{s}$
**Answer:** $t \approx 12\,\text{s}$, two significant figures like the velocities $54\,\text{km/h}$ and $108\,\text{km/h}$.
**Reasonableness:** The average velocity is $22.5\,\text{m/s}$, and $22.5\,\text{m/s} \cdot 12.0\,\text{s} = 270\,\text{m}$, the length of the lane. An acceleration of about ten seconds to motorway speed is usual for a car.

### b)
**Given:** $v_0 = 15\,\text{m/s}$, $v = 30\,\text{m/s}$ and from part a $t = 12.0\,\text{s}$
**Find:** the acceleration $a$ in $\text{m/s}^2$
**Principle:** The acceleration is the change in velocity divided by the time it took; in uniformly accelerated motion it is the same all the time and equal to the slope of the $(t,v)$ graph (chapter *Acceleration and uniformly accelerated motion*).
**Formula:** $a = \dfrac{\Delta v}{\Delta t} = \dfrac{v - v_0}{t}$
**Conversions:** The velocities were converted to $\text{m/s}$ in part a, and the time is in seconds.
**Substitution:** $a = \dfrac{30\,\text{m/s} - 15\,\text{m/s}}{12.0\,\text{s}} = \dfrac{15\,\text{m/s}}{12.0\,\text{s}} = 1.25\,\text{m/s}^2$
**Answer:** $a \approx 1.3\,\text{m/s}^2$, two significant figures like the velocities ($1.25\,\text{m/s}^2$ is also accepted).
**Reasonableness:** The velocity grows by $1.25\,\text{m/s} = 4.5\,\text{km/h}$ every second, so in twelve seconds it grows by $54\,\text{km/h}$, as in the data. A check with the equation of position: $15\,\text{m/s} \cdot 12.0\,\text{s} + \tfrac{1}{2} \cdot 1.25\,\text{m/s}^2 \cdot (12.0\,\text{s})^2 = 180\,\text{m} + 90\,\text{m} = 270\,\text{m}$.

### c)
**Given:** origin at the beginning of the acceleration lane, positive direction the direction of driving; car: $x_{0\text{A}} = 0$, $v_0 = 15\,\text{m/s}$, $a = 1.25\,\text{m/s}^2$; lorry: $x_{0\text{L}} = -40\,\text{m}$, $v_\text{L} = 81\,\text{km/h}$ (constant)
**Find:** whether the lorry draws level with the car, and the smallest distance $d_\text{min}$
**Principle:** The positions are written in the same coordinate system (chapter *Comparing the motions of two bodies*). The lorry is faster at first and approaches the car. The distance decreases as long as the lorry is faster and starts to grow when the car is faster, so it is at its smallest when the velocities are equal. If the distance is then positive, the lorry does not draw level.
**Formula:** $x_\text{A} = v_0\,t + \tfrac{1}{2}\,a\,t^2$ and $x_\text{L} = x_{0\text{L}} + v_\text{L}\,t$. Equal velocities: $v_0 + a\,t_1 = v_\text{L}$, so $t_1 = \dfrac{v_\text{L} - v_0}{a}$ and $d_\text{min} = x_\text{A}(t_1) - x_\text{L}(t_1)$
**Conversions:** $81\,\text{km/h} = \dfrac{81 \cdot 1000\,\text{m}}{3600\,\text{s}} = 22.5\,\text{m/s}$
**Substitution:** $t_1 = \dfrac{22.5\,\text{m/s} - 15\,\text{m/s}}{1.25\,\text{m/s}^2} = 6.0\,\text{s}$; $x_\text{A} = 15\,\text{m/s} \cdot 6.0\,\text{s} + \tfrac{1}{2} \cdot 1.25\,\text{m/s}^2 \cdot (6.0\,\text{s})^2 = 90\,\text{m} + 22.5\,\text{m} = 112.5\,\text{m}$; $x_\text{L} = -40\,\text{m} + 22.5\,\text{m/s} \cdot 6.0\,\text{s} = 95\,\text{m}$; $d_\text{min} = 112.5\,\text{m} - 95\,\text{m} = 17.5\,\text{m}$
**Answer:** The lorry does not draw level with the car. The distance is at its smallest, about $18\,\text{m}$, at $6.0\,\text{s}$, two significant figures like the distance $40\,\text{m}$ and the velocities.
**Reasonableness:** At the end of the lane ($12.0\,\text{s}$) the lorry is at $-40\,\text{m} + 22.5\,\text{m/s} \cdot 12.0\,\text{s} = 230\,\text{m}$ and the car at $270\,\text{m}$, so the gap is $40\,\text{m}$ again, as it should be: the areas between the velocity graphs before and after $6.0\,\text{s}$ are equal. The meeting equation $\tfrac{1}{2}\,a\,t^2 + (v_0 - v_\text{L})\,t - x_{0\text{L}} = 0$ has no real solutions, because the discriminant $(-7.5)^2 - 4 \cdot 0.625 \cdot 40 < 0$.

### d)
**Find:** why the lorry catches up with a car that accelerates uniformly only to $72\,\text{km/h}$, and why it is worth accelerating to the speed of the traffic
**Principle:** The displacement is the area of the $(t,v)$ graph, and the distance between two bodies changes by the area between their two graphs (chapter *Comparing the motions of two bodies*).
**Model answer:** This car is slower than the lorry for the whole lane, because its greatest velocity $72\,\text{km/h} = 20\,\text{m/s}$ is smaller than the lorry's $22.5\,\text{m/s}$. In the $(t,v)$ graph the lorry's horizontal line is above the car's rising line all the time, so the lorry's displacement grows more than the car's at every moment and the gap of $40\,\text{m}$ shrinks all the time. When the gap has been closed, the lorry is level with the car and goes past. A calculation confirms this (the car accelerates uniformly over the whole length of the lane): the acceleration lasts $2 \cdot 270\,\text{m} : (15\,\text{m/s} + 20\,\text{m/s}) \approx 15.4\,\text{s}$ and the car's average velocity is $17.5\,\text{m/s}$, so the lorry travels on average $5\,\text{m/s}$ faster and makes up $5\,\text{m/s} \cdot 15.4\,\text{s} \approx 77\,\text{m}$, more than the gap of $40\,\text{m}$; and in that time the lorry gets to $-40\,\text{m} + 22.5\,\text{m/s} \cdot 15.4\,\text{s} \approx 307\,\text{m}$, past the car before the end of the lane ($270\,\text{m}$). The car must then slow down and merge behind the lorry. When the car accelerates to the speed of the traffic, it is faster than the lorry in the final stage, the distance grows again and the car can merge safely in front of the lorry.

### Yleisiä virheitä
- The velocities are not converted to $\text{m/s}$, and kilometres per hour are multiplied by seconds.
- In part a the distance is divided by the final velocity ($270\,\text{m} : 30\,\text{m/s} = 9.0\,\text{s}$), although the velocity grows gradually.
- In part c the meeting condition is solved and the negative discriminant is taken for a calculation error, although it tells you that there is no meeting.
- In part c the $-40\,\text{m}$ is forgotten from the lorry's position, or the initial distance $40\,\text{m}$ is taken as the smallest distance.

### Hyväksytään myös
- In part a first solving $a = \dfrac{v^2 - v_0^2}{2\,\Delta x}$ and then $t = \dfrac{v - v_0}{a}$, or using the equation of position and the equation of velocity together.
- In part c the distance $d(t) = x_\text{A} - x_\text{L} = 40\,\text{m} - 7.5\,\text{m/s} \cdot t + 0.625\,\text{m/s}^2 \cdot t^2$ and its smallest value from the vertex of the parabola.

## fy9-liike-s2

### a)
**Given:** height of the throw $y_{0\text{A}} = 1.5\,\text{m}$, initial velocity $v_0 = 12.0\,\text{m/s}$ upwards, $g = 9.81\,\text{m/s}^2$; up positive, air resistance neglected
**Find:** the height of the highest point $y_\text{top}$ above the floor
**Principle:** The ball's acceleration is $g$ downwards during the whole flight, so the motion is uniformly accelerated. At the highest point the ball's velocity is zero for an instant, although the acceleration is not (chapter *Acceleration and uniformly accelerated motion*).
**Formula:** $v = v_0 - g\,t_\text{top} = 0$, so $t_\text{top} = \dfrac{v_0}{g}$, and $y_\text{top} = y_{0\text{A}} + v_0\,t_\text{top} - \tfrac{1}{2}\,g\,t_\text{top}^2$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $t_\text{top} = \dfrac{12.0\,\text{m/s}}{9.81\,\text{m/s}^2} = 1.223\,\text{s}$; $y_\text{top} = 1.5\,\text{m} + 12.0\,\text{m/s} \cdot 1.223\,\text{s} - \tfrac{1}{2} \cdot 9.81\,\text{m/s}^2 \cdot (1.223\,\text{s})^2 = 1.5\,\text{m} + 14.68\,\text{m} - 7.34\,\text{m} = 8.84\,\text{m}$
**Answer:** $y_\text{top} \approx 8.8\,\text{m}$, to a tenth of a metre, because the height of the throw $1.5\,\text{m}$ is known to a tenth of a metre.
**Reasonableness:** The rise is $7.34\,\text{m}$; the ball's average velocity while rising is $6.0\,\text{m/s}$, and $6.0\,\text{m/s} \cdot 1.223\,\text{s} \approx 7.3\,\text{m}$. The ball does not rise as high as the railing of the third floor ($9.0\,\text{m}$), which suits a strong but ordinary throw.

### b)
**Given:** ball A: $y_{0\text{A}} = 1.5\,\text{m}$, $v_0 = 12.0\,\text{m/s}$; ball B: $y_{0\text{B}} = 9.0\,\text{m}$, starts from rest; the acceleration of both $g = 9.81\,\text{m/s}^2$ downwards
**Find:** the moment of passing $t$ and the height of passing $y$
**Principle:** The balls pass each other when they are at the same height at the same moment: $y_\text{A}(t) = y_\text{B}(t)$ (chapter *Comparing the motions of two bodies*). The motion of each is uniformly accelerated with the same acceleration, so the terms $-\tfrac{1}{2}\,g\,t^2$ cancel.
**Formula:** $y_{0\text{A}} + v_0\,t - \tfrac{1}{2}\,g\,t^2 = y_{0\text{B}} - \tfrac{1}{2}\,g\,t^2$, so $t = \dfrac{y_{0\text{B}} - y_{0\text{A}}}{v_0}$ and $y = y_{0\text{B}} - \tfrac{1}{2}\,g\,t^2$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $t = \dfrac{9.0\,\text{m} - 1.5\,\text{m}}{12.0\,\text{m/s}} = \dfrac{7.5\,\text{m}}{12.0\,\text{m/s}} = 0.625\,\text{s}$; $y = 9.0\,\text{m} - \tfrac{1}{2} \cdot 9.81\,\text{m/s}^2 \cdot (0.625\,\text{s})^2 = 9.0\,\text{m} - 1.916\,\text{m} = 7.08\,\text{m}$
**Answer:** The balls pass each other at $t \approx 0.63\,\text{s}$ at the height $y \approx 7.1\,\text{m}$, two significant figures like the difference in height $7.5\,\text{m}$.
**Reasonableness:** Ball A's position function gives the same height: $1.5\,\text{m} + 12.0\,\text{m/s} \cdot 0.625\,\text{s} - 1.916\,\text{m} = 7.08\,\text{m}$. The passing happens before A's highest point at $1.22\,\text{s}$ and before B hits the floor at $\sqrt{2 \cdot 9.0\,\text{m} : 9.81\,\text{m/s}^2} \approx 1.35\,\text{s}$.

### c)
**Find:** why the moment of passing does not depend on the acceleration of free fall, and whether the balls would pass each other at the same moment on the Moon
**Principle:** The acceleration tells you how much the velocity changes in a second. When two bodies have the same acceleration, their velocities change by the same amount (chapter *Acceleration and uniformly accelerated motion*).
**Model answer:** Both balls are free from the same moment on, so the acceleration of each is $g$ downwards. Their velocities decrease by the same amount every second, so the difference of the velocities stays at its initial value $12.0\,\text{m/s}$ all the time. The distance of $7.5\,\text{m}$ between the balls therefore decreases uniformly at $12.0\,\text{m/s}$, just as if neither of them accelerated, and the passing happens at $7.5\,\text{m} : 12.0\,\text{m/s} \approx 0.63\,\text{s}$ whatever the acceleration of free fall. On the Moon the moment of passing would be the same. The height of passing, however, does depend on the acceleration of free fall: on the Moon ($g = 1.62\,\text{m/s}^2$) each ball falls only about $0.32\,\text{m}$ in this time, so the passing would happen at a height of about $8.7\,\text{m}$.

### d)
**Given:** $v_0 = 12.0\,\text{m/s}$ (A), B starts from rest, $g = 9.81\,\text{m/s}^2$ downwards, from part b $t = 0.625\,\text{s}$; up positive
**Find:** the velocities $v_\text{A}$ and $v_\text{B}$ with their signs at the moment of passing
**Principle:** In uniformly accelerated motion the velocity changes by the acceleration every second. Up is positive, so the acceleration is $-g$, and the sign of the velocity gives the direction (chapter *Acceleration and uniformly accelerated motion*).
**Formula:** $v_\text{A} = v_0 - g\,t$ and $v_\text{B} = -g\,t$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $v_\text{A} = 12.0\,\text{m/s} - 9.81\,\text{m/s}^2 \cdot 0.625\,\text{s} = 12.0\,\text{m/s} - 6.131\,\text{m/s} = 5.869\,\text{m/s}$ and $v_\text{B} = -9.81\,\text{m/s}^2 \cdot 0.625\,\text{s} = -6.131\,\text{m/s}$
**Answer:** $v_\text{A} \approx 5.9\,\text{m/s}$ upwards and $v_\text{B} \approx -6.1\,\text{m/s}$, that is, $6.1\,\text{m/s}$ downwards, two significant figures like the moment of passing.
**Reasonableness:** The difference of the velocities is $5.869\,\text{m/s} - (-6.131\,\text{m/s}) = 12.0\,\text{m/s}$, as the reasoning of part c requires. Ball A is still rising, because its highest point is only at $1.22\,\text{s}$.

### Yleisiä virheitä
- At the highest point the acceleration is assumed to be zero, or the height is calculated without the height of the throw $1.5\,\text{m}$.
- The position of the falling ball is written as $y_\text{B} = \tfrac{1}{2}\,g\,t^2$, forgetting that up is positive and that the ball starts from the height $9.0\,\text{m}$.
- In part b the moment when the velocities are equal is solved instead of the moment when the heights are equal.
- In part d the signs of the velocities are left out, so it does not show that the balls move in opposite directions.

### Hyväksytään myös
- A coordinate system with down positive, when the signs are consistent with it.
- The reasoning of part b directly from the relative motion of the balls, as in the model answer of part c.

## fy9-liike-s3

### a)
**Find:** the train's velocity $v$ as a function of time $t$ as a graph, and a model fitted to it
**Graph:** On the horizontal axis is the time $t\ (\text{s})$ and on the vertical axis the velocity $v\ (\text{km/h})$. The time axis extends to about $55\,\text{s}$, so that the moment of stopping in part c fits in the graph.

<svg data-fig="fy9-liike-s3-graph" viewBox="0 0 440 400" role="img" aria-label="Graph: the train&#x27;s velocity v in kilometres per hour as a function of time t. Eleven black points at the moments 0–40 s. At the first three points there is a horizontal straight line at the level 90 km/h. A falling straight line is fitted to the other points; it crosses the horizontal line at about 10 s and is extended as a dashed line to the time axis at about 48.5 s. The points (12 s, 85 km/h) and (40 s, 20 km/h) of the line are circled, and the slope, about −2.3 km/h per second, is read from them. The triangle between the falling line and the time axis is coloured green: its area is the braking distance." style="max-width:100%;font-size:24px">
  <line x1="83.5" y1="356" x2="83.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="103" y1="356" x2="103" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="122.5" y1="356" x2="122.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="141.5" y1="356" x2="141.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="161" y1="356" x2="161" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180.5" y1="356" x2="180.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="356" x2="200" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="219.5" y1="356" x2="219.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="239" y1="356" x2="239" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258.5" y1="356" x2="258.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="277.5" y1="356" x2="277.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="297" y1="356" x2="297" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="316.5" y1="356" x2="316.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="356" x2="336" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="325.5" x2="336" y2="325.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="295" x2="336" y2="295" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="265" x2="336" y2="265" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="234.5" x2="336" y2="234.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="204" x2="336" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="173.5" x2="336" y2="173.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="143" x2="336" y2="143" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="113" x2="336" y2="113" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="82.5" x2="336" y2="82.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="64" y1="52" x2="336" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="63" y1="356" x2="350" y2="356" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M362,356 L349,362 L349,350 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="64" y1="357" x2="64" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M64,26 L70,39 L58,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="83.5" y1="356" x2="83.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="356" x2="103" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="93" y="365.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="122.5" y1="356" x2="122.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="141.5" y1="356" x2="141.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="125" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="161" y1="356" x2="161" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180.5" y1="356" x2="180.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="164" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="200" y1="356" x2="200" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="219.5" y1="356" x2="219.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="203" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$32$</div></foreignObject>
  <line x1="239" y1="356" x2="239" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="258.5" y1="356" x2="258.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="242" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="277.5" y1="356" x2="277.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="297" y1="356" x2="297" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="280.5" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="316.5" y1="356" x2="316.5" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="336" y1="356" x2="336" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="319.5" y="365.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$56$</div></foreignObject>
  <line x1="57" y1="325.5" x2="64" y2="325.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="295" x2="64" y2="295" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="280.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="57" y1="265" x2="64" y2="265" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="234.5" x2="64" y2="234.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="220" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="57" y1="204" x2="64" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="173.5" x2="64" y2="173.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="159" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="57" y1="143" x2="64" y2="143" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="113" x2="64" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="19" y="98.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="57" y1="82.5" x2="64" y2="82.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="57" y1="52" x2="64" y2="52" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="7" y="37.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="34" y="361.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="368" y="341.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="78" y="17.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$v\ (\text{km/h})$</span></div></foreignObject>
  <polygon points="112,82.5 301,356 112,356" fill="#b2f2bb" fill-opacity="0.75"/>
  <polyline points="64,82.5 112,82.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="112,82.5 258.5,294.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="258.5,294.5 301,356" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="64" cy="79.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="83.5" cy="85.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="103" cy="82.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="122.5" cy="100.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="141.5" cy="122" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="161" cy="152.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="180.5" cy="186" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="200" cy="207" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="219.5" cy="237.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="239" cy="271" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="258.5" cy="292" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="122.5" cy="97.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="258.5" cy="295" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="112" y1="82.5" x2="112" y2="356" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="118" y="317" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$10\,\text{s}$</div></foreignObject>
  <foreignObject x="307" y="296" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$48.5\,\text{s}$</div></foreignObject>
  <foreignObject x="195" y="110.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k \approx -2.3\,\tfrac{\text{km/h}}{\text{s}}$</div></foreignObject>
  <foreignObject x="87" y="274.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{braking dist.}$</div></foreignObject>
</svg>

**Model answer:** The points show two stages. At the moments $0$, $4$ and $8\,\text{s}$ the velocity stays at about $90\,\text{km/h}$: the variation of $\pm 1\,\text{km/h}$ is the size of the app's uncertainty, so the train moves uniformly, and a horizontal straight line is drawn for these points. From $12\,\text{s}$ on, the velocity decreases by roughly the same amount every four seconds, so the train brakes uniformly, and a falling straight line is fitted to these points so that the points lie on both sides of it. The first three points are not included in the braking line, because they belong to a different stage and would tilt the line the wrong way. The falling line is extended as a dashed line to the time axis for part c.

### b)
**Given:** the braking line of part a; the points $(12\,\text{s};\ 85\,\text{km/h})$ and $(40\,\text{s};\ 20\,\text{km/h})$ are read from it
**Find:** the acceleration during the braking $a$ in $\text{m/s}^2$
**Principle:** The braking points lie on a straight line, so the acceleration is constant and equal to the slope of the $(t,v)$ graph (chapter *Acceleration and uniformly accelerated motion*). The slope is read from the fitted line, from two points far apart, not from adjacent measured points, because every measurement has a small error (chapter *Graphing and fitting a straight line*).
**Reading the graph:** The line passes through the points $(12\,\text{s};\ 85\,\text{km/h})$ and $(40\,\text{s};\ 20\,\text{km/h})$, which are circled in the model graph.
**Formula:** $a = \dfrac{\Delta v}{\Delta t} = \dfrac{v_2 - v_1}{t_2 - t_1}$
**Conversions:** The change in velocity to metres per second by substituting the units: $20\,\text{km/h} - 85\,\text{km/h} = -65\,\text{km/h} = \dfrac{-65 \cdot 1000\,\text{m}}{3600\,\text{s}} = -18.06\,\text{m/s}$
**Substitution:** $a = \dfrac{-18.06\,\text{m/s}}{40\,\text{s} - 12\,\text{s}} = \dfrac{-18.06\,\text{m/s}}{28\,\text{s}} = -0.645\,\text{m/s}^2$
**Answer:** $a \approx -0.65\,\text{m/s}^2$, two significant figures, because the velocities read from the line are known to about two figures. Results of $-0.61$…$-0.68\,\text{m/s}^2$ are within the range of the fit.
**Reasonableness:** The acceleration is negative, that is, opposite to the velocity, so the speed decreases, as it must when braking. The magnitude $0.65\,\text{m/s}^2$ is a usual service braking of a train: the passengers stay on their feet. The spreadsheet fit gives $-2.31\,\text{km/h}$ per second, that is, $-0.642\,\text{m/s}^2$, almost the same.

### c)
**Given:** the graph of part a: the braking begins at the crossing point of the horizontal and the falling line, where the velocity is $v_0 = 90\,\text{km/h}$
**Find:** the moment of stopping $t_\text{s}$ and the braking distance $\Delta x$ from the beginning of the braking
**Principle:** The train stops when the braking line crosses the time axis; because the measurement ended at $40\,\text{s}$, the line has to be extended outside the measured range. The displacement is the area between the $(t,v)$ graph and the time axis, here a right-angled triangle (chapter *Acceleration and uniformly accelerated motion*).
**Reading the graph:** The horizontal and the falling line cross at about $t_0 = 10\,\text{s}$, and the extended braking line crosses the time axis at about $t_\text{s} = 48.5\,\text{s}$.
**Formula:** $\Delta x = \tfrac{1}{2}\,v_0\,(t_\text{s} - t_0)$
**Conversions:** $90\,\text{km/h} = \dfrac{90 \cdot 1000\,\text{m}}{3600\,\text{s}} = 25\,\text{m/s}$
**Substitution:** $\Delta x = \tfrac{1}{2} \cdot 25\,\text{m/s} \cdot (48.5\,\text{s} - 10\,\text{s}) = \tfrac{1}{2} \cdot 25\,\text{m/s} \cdot 38.5\,\text{s} = 481\,\text{m}$
**Answer:** The train stops at about $49\,\text{s}$, and the braking distance is about $480\,\text{m}$. Two significant figures, because the crossing points are read from the graph to within about half a second; results of $450$–$520\,\text{m}$ are accepted.
**Reasonableness:** With the acceleration of part b, braking from $25\,\text{m/s}$ lasts $25\,\text{m/s} : 0.645\,\text{m/s}^2 \approx 39\,\text{s}$, like the $38.5\,\text{s}$ read from the graph. The average velocity during the braking is $12.5\,\text{m/s}$, and $12.5\,\text{m/s} \cdot 38.5\,\text{s} \approx 480\,\text{m}$. A braking distance of about half a kilometre suits a train that stops at a station with ordinary braking.

### d)
**Find:** how reliable the conclusion is that the train stopped exactly at the distance of part c
**Principle:** A model is reliable only in the range where it has been measured; extending it outside the measured range, extrapolation, assumes that the motion continues in the same way. The precision of the result also depends on how well the slope is known (chapters *Graphing and fitting a straight line* and *Measuring and the reliability of a measurement*).
**Model answer:** The conclusion is good in its order of magnitude but not exact. The recording ended at $40\,\text{s}$, when the velocity was still about $20\,\text{km/h}$, so the moment of stopping $48.5\,\text{s}$ and the distance of the last $9\,\text{s}$ or so rest on the assumption that the train braked with the same acceleration until the end. In reality a driver often eases the braking just before stopping, and then the train goes a little further. In addition, the uncertainty of the slope carries over to the result: the steepest and the gentlest line that fit the points give a range of about a second for the moment of stopping and about $\pm 20\,\text{m}$ for the distance. The app's velocity uncertainty $\pm 1\,\text{km/h}$ is small compared with the change in velocity of $70\,\text{km/h}$, so it is not the largest source of uncertainty. The result should be given as “about $480\,\text{m}$, with an uncertainty of a few tens of metres”, not as “exactly”.

### Yleisiä virheitä
- All the points are joined into a broken line, or one straight line is fitted to all eleven points, so that the points of the uniform stage tilt the slope.
- The slope is calculated from two adjacent measured points or from the table values instead of the line.
- The acceleration is left in kilometres per hour per second, or in the conversion the number is multiplied by $3.6$ instead of divided.
- The braking distance is calculated as the rectangle $25\,\text{m/s} \cdot 38.5\,\text{s}$ instead of the triangle, or the distance is calculated from $0$.

### Hyväksytään myös
- The slope of part b from a spreadsheet fit to the braking points: $-2.31\,\text{km/h}$ per second, that is, $-0.642\,\text{m/s}^2$.
- The distance of part c calculated from the acceleration of part b: $t = v_0 : |a|$ and $\Delta x = \tfrac{1}{2}\,v_0\,t$.

## fy9-liike-s4

### a)
**Find:** whether an average speed over $80\,\text{km/h}$ proves that the driver has been speeding at some point
**Principle:** The average speed is the displacement divided by the time, that is, in the $(t,x)$ graph the slope of the line through the points of the beginning and the end of the section. The instantaneous velocity is the slope of the tangent to the graph, and the displacement is the area under the $(t,v)$ graph (chapters *Position, velocity and uniform motion as graphs* and *Acceleration and uniformly accelerated motion*).
**Model answer:** The opinion is wrong. If the car's velocity were at most $80\,\text{km/h}$ all the time, its $(t,v)$ graph would be below or on the horizontal line $v = 80\,\text{km/h}$ all the time. Then the area under the graph, the distance travelled, would be at most $80\,\text{km/h}$ times the travel time, and the average speed would be at most $80\,\text{km/h}$. The same with the $(t,x)$ graph: the graph cannot rise from start to finish more steeply on average than at its steepest point. So when the average speed is over $80\,\text{km/h}$, the velocity must have been over $80\,\text{km/h}$ at some point. The converse conclusion does not hold, however: a driver can speed on part of the distance and drive slowly elsewhere, so that the average speed stays below the limit. The enforcement therefore does not convict the innocent, but it does not catch every case of speeding either.

### b)
**Given:** the parts $\Delta x_1 = 2.0\,\text{km}$ at $v_1 = 100\,\text{km/h}$ and $\Delta x_2 = 1.0\,\text{km}$ at $v_2 = 60\,\text{km/h}$; the whole section $\Delta x = 3.0\,\text{km}$
**Find:** the average speed $v_\text{av}$ in $\text{km/h}$
**Principle:** The average speed is the whole displacement divided by the whole time (chapter *Position, velocity and uniform motion as graphs*). On each part the velocity is constant, so the time of a part is its distance divided by the velocity. The mean of the velocities will not do, because the velocities are driven for different lengths of time.
**Formula:** $t_1 = \dfrac{\Delta x_1}{v_1}$, $t_2 = \dfrac{\Delta x_2}{v_2}$ and $v_\text{av} = \dfrac{\Delta x}{t_1 + t_2}$
**Conversions:** The distances are in kilometres and the velocities in kilometres per hour, so the times come out in hours and no conversions are needed. For comparison, hours to seconds: $1\,\text{h} = 3600\,\text{s}$.
**Substitution:** $t_1 = \dfrac{2.0\,\text{km}}{100\,\text{km/h}} = 0.020\,\text{h} = 72\,\text{s}$, $t_2 = \dfrac{1.0\,\text{km}}{60\,\text{km/h}} = 0.01667\,\text{h} = 60\,\text{s}$ and $v_\text{av} = \dfrac{3.0\,\text{km}}{0.020\,\text{h} + 0.01667\,\text{h}} = \dfrac{3.0\,\text{km}}{0.03667\,\text{h}} = 81.8\,\text{km/h}$
**Answer:** $v_\text{av} \approx 82\,\text{km/h}$, two significant figures like the distances $2.0\,\text{km}$ and $1.0\,\text{km}$. The opinion is wrong: the average speed exceeds the limit.
**Reasonableness:** At the speed limit the section would take $3.0\,\text{km} : 80\,\text{km/h} = 0.0375\,\text{h} = 135\,\text{s}$. The driver took $132\,\text{s}$, less than $135\,\text{s}$, so the driver was faster than the speed limit. The average speed is closer to $100\,\text{km/h}$, because that velocity was driven for a larger part of the time.

### c)
**Find:** the uncertainty of the average speed on a $3.0\,\text{km}$ and on a $100\,\text{m}$ section when the car is driving at $80\,\text{km/h}$, and whether the third opinion holds
**Principle:** The average speed is calculated from the travel time, and the travel time is the difference of two records, so the $0.5\,\text{s}$ uncertainty of each record affects it: in total at most about $1\,\text{s}$. The shorter the travel time, the greater the relative effect of the same time error (chapter *Measuring and the reliability of a measurement*).
**Model answer:** At $80\,\text{km/h} = \dfrac{80 \cdot 1000\,\text{m}}{3600\,\text{s}} = 22.2\,\text{m/s}$ the travel time of the long section is $3000\,\text{m} : 22.2\,\text{m/s} = 135\,\text{s}$. An error of one second is less than $1\,\%$ of it, so the uncertainty of the average speed is about $80\,\text{km/h} \cdot 1\,\text{s} : 135\,\text{s} \approx 0.6\,\text{km/h}$. On the short section the travel time is only $100\,\text{m} : 22.2\,\text{m/s} = 4.5\,\text{s}$, and an error of one second is over $20\,\%$ of it: the measured average speed could be about $65$–$100\,\text{km/h}$, so the uncertainty is about $18\,\text{km/h}$. The third opinion therefore does not hold. On a short section the system could not tell a driver at the speed limit from a speeding one, and the result could go either way. The enforcement section must be long, so that the uncertainty of the timing is small compared with the travel time.

### Yleisiä virheitä
- In part b the mean of the velocities is calculated, or a mean weighted by the distances ($\tfrac{2}{3} \cdot 100 + \tfrac{1}{3} \cdot 60 \approx 87\,\text{km/h}$), or the distance is divided by the wrong velocity.
- In part a the average speed and the instantaneous velocity are mixed up, or it is claimed that an average speed over the limit can arise without speeding.
- In part c the uncertainty of the timing is compared with the distance or the velocity instead of the travel time.

### Hyväksytään myös
- Part b in seconds and metres: $3000\,\text{m} : 132\,\text{s} = 22.7\,\text{m/s} \approx 82\,\text{km/h}$.
- In part c the uncertainty based on $0.5\,\text{s}$ ($0.3\,\text{km/h}$ and $9\,\text{km/h}$), when the conclusion is the same.

## fy9-liike-s5

### a)
**Given:** distance $x = 1.20\,\text{m}$ from rest, time $t = 1.6\,\text{s}$, uncertainty of the timing $\Delta t = 0.2\,\text{s}$
**Find:** the acceleration $a$ the group calculated, and its range because of the uncertainty of the timing
**Principle:** The group assumes the motion to be uniformly accelerated. The position of a body starting from rest is then $x = \tfrac{1}{2}\,a\,t^2$ (chapter *Acceleration and uniformly accelerated motion*). The effect of the uncertainty is estimated by calculating the result with the extreme values of the time $t \pm \Delta t$ (chapter *Measuring and the reliability of a measurement*).
**Formula:** $x = \tfrac{1}{2}\,a\,t^2$, so $a = \dfrac{2x}{t^2}$
**Conversions:** The distance is in metres and the time in seconds, so no conversions are needed.
**Substitution:** $a = \dfrac{2 \cdot 1.20\,\text{m}}{(1.6\,\text{s})^2} = \dfrac{2.40\,\text{m}}{2.56\,\text{s}^2} = 0.9375\,\text{m/s}^2$; extreme values $\dfrac{2.40\,\text{m}}{(1.8\,\text{s})^2} = 0.741\,\text{m/s}^2$ and $\dfrac{2.40\,\text{m}}{(1.4\,\text{s})^2} = 1.224\,\text{m/s}^2$
**Answer:** $a \approx 0.94\,\text{m/s}^2$, but because of the uncertainty the result lies between $0.74$…$1.22\,\text{m/s}^2$, that is, $a \approx (0.9 \pm 0.3)\,\text{m/s}^2$. The result should be given to one or two significant figures, because the uncertainty is large.
**Reasonableness:** The relative uncertainty of the time is $0.2\,\text{s} : 1.6\,\text{s} \approx 13\,\%$, and because the time is squared in the formula, the relative uncertainty of the acceleration is about twice that, $25\,\%$. This matches the calculated range. An acceleration below $1\,\text{m/s}^2$ suits a gently sloping track.

### b)
**Find:** whether the group's conclusion is justified, and the main weaknesses of the measurement
**Principle:** That a model fits can be shown only by comparing the model with many measurement points. In uniformly accelerated motion the $(t,x)$ points lie on a parabola and the $(t,v)$ points on a straight line (chapters *Acceleration and uniformly accelerated motion* and *Graphing and fitting a straight line*).
**Model answer:** The conclusion is not justified. The group used the formula $a = \dfrac{2x}{t^2}$, which is derived assuming a uniform acceleration, so a number obtained with the formula cannot prove the assumption: one distance and one time always give some number, whatever the motion is like. The reasoning is circular. A single $(t,x)$ point fits any accelerated motion; several points at different moments are needed. The measurement also has weaknesses: in hand timing the reaction time affects both the start and the end, the cart's starting moment and the point of passing are judged by eye and from the side, the cart may have got some speed as it was released, and the measurement was made only once, so the size of the random error is not known. The number $0.94\,\text{m/s}^2$ is at best a rough estimate of the acceleration, if the motion is uniformly accelerated.

### c)
**Find:** a plan for an experiment that reliably finds out whether the motion is uniformly accelerated and determines the acceleration
**Principle:** A model is tested by measuring the position at many moments and fitting a curve of the model to the measured points; the acceleration is found from a coefficient of the fit. The variables are kept constant and the measurements are repeated (chapters *Acceleration and uniformly accelerated motion*, *Graphing and fitting a straight line* and *Your own experimental investigation: planning, carrying out and reporting*).
**Model answer:** The cart's motion is filmed with a camera on a stand perpendicular to the track, and the scale is set with a measuring tape in the plane of the track. Video analysis is used to read the cart's position from, for example, every third frame, which gives tens of $(t,x)$ points. Alternatively, light gates are placed at different distances along the track and the times are measured electronically. The cart is released from rest without a push, for example by releasing a holder, and the slope of the track is kept the same in all repeats. The points are presented as a $(t,x)$ graph and a quadratic polynomial $x = A\,t^2 + B\,t + C$ is fitted to them; if the points lie on the curve without a systematic deviation, the motion is uniformly accelerated, and the acceleration is $a = 2A$. Another way is to calculate the velocities from successive points and check whether the $(t,v)$ points lie on a straight line. The experiment is repeated at least three times, and the uncertainty of the acceleration is estimated from the spread of the repeats or from the uncertainty of the coefficient given by the fit.

### Yleisiä virheitä
- In part a the formula used is $a = \dfrac{x}{t^2}$ without the factor $2$, or $a = \dfrac{v}{t}$, where $v = x : t$ is the average velocity and not the final velocity.
- The uncertainty is assessed only in words, without calculating its effect on the result.
- In part c the only suggestion is “a more accurate stopwatch” or “more repeats” with the same method, so that a single point still does not test the model.
- The circular reasoning is not noticed, and the conclusion is criticised only because of the uncertainty.

### Hyväksytään myös
- The uncertainty of part a with the relative uncertainty: $\dfrac{\Delta a}{a} \approx 2 \cdot \dfrac{\Delta t}{t} = 25\,\%$, $\Delta a \approx 0.23\,\text{m/s}^2$.
- In part c a measurement with a sensor or a motion detector that gives the $(t,x)$ or $(t,v)$ points directly.

## fy9-liike-s6

### a)
**Given:** the fitted polynomial $y = A\,t^2 + B\,t + C$, where $A = -4.44\,\text{m/s}^2$, $B = -0.007\,\text{m/s}$ and $C = 1.651\,\text{m}$; the ball started from rest, $y$ grows upwards
**Find:** the measured acceleration of free fall $a$
**Principle:** The motion of a freely falling ball is uniformly accelerated, so its position is $y = y_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$. When the fitted polynomial is compared with this, the coefficients of $t^2$ are the same: $A = \tfrac{1}{2}\,a$ (chapter *Acceleration and uniformly accelerated motion*). The coefficient $B \approx 0$ corresponds to an initial velocity of zero, and $C$ to the initial height.
**Formula:** $A = \tfrac{1}{2}\,a$, so $a = 2A$
**Conversions:** The coefficient is already in $\text{m/s}^2$, so no conversions are needed.
**Substitution:** $a = 2 \cdot (-4.44\,\text{m/s}^2) = -8.88\,\text{m/s}^2$
**Answer:** The measured acceleration of free fall is $8.88\,\text{m/s}^2$ downwards (minus sign, because $y$ grows upwards), three significant figures like the coefficient $A$.
**Reasonableness:** A check from the table: when $t = 0.50\,\text{s}$, the ball has fallen $1.653\,\text{m} - 0.538\,\text{m} = 1.115\,\text{m}$, and $\tfrac{1}{2} \cdot 8.88\,\text{m/s}^2 \cdot (0.50\,\text{s})^2 = 1.11\,\text{m}$. The result is of the same order of magnitude as $9.81\,\text{m/s}^2$ but clearly smaller, so something affects the measurement.

### b)
**Given:** $A = (-4.44 \pm 0.05)\,\text{m/s}^2$, from part a $a = 8.88\,\text{m/s}^2$; table value $g = 9.81\,\text{m/s}^2$
**Find:** the uncertainty of the acceleration $\Delta a$, and whether the result agrees with the table value
**Principle:** When a quantity is multiplied by a constant, its uncertainty is multiplied by the same constant. A result agrees with a reference value if the difference is the size of the uncertainty or smaller (chapter *Measuring and the reliability of a measurement*).
**Formula:** $a = 2A$, so $\Delta a = 2\,\Delta A$
**Conversions:** None needed: the units are the same.
**Substitution:** $\Delta a = 2 \cdot 0.05\,\text{m/s}^2 = 0.10\,\text{m/s}^2$; the difference from the table value $9.81\,\text{m/s}^2 - 8.88\,\text{m/s}^2 = 0.93\,\text{m/s}^2$
**Answer:** $a = (8.88 \pm 0.10)\,\text{m/s}^2$. The difference from the table value, $0.93\,\text{m/s}^2$, is about nine times the uncertainty, so the result does not agree with the table value.
**Reasonableness:** The relative uncertainty is $0.10 : 8.88 \approx 1.1\,\%$, which suits the small scatter of the points, a few millimetres. The uncertainty of the fit tells you only about the random scatter, not about a systematic error that shifts all the points in the same direction.

### c)
**Given:** the scale was set in the plane of the metre stick $3.00\,\text{m}$ from the camera, the ball fell $3.30\,\text{m}$ from the camera; from parts a and b $a = (8.88 \pm 0.10)\,\text{m/s}^2$
**Find:** the cause and the direction of the systematic error, and the corrected acceleration $a_\text{c}$
**Principle:** An object further away looks smaller in the picture in the same ratio as its distance from the camera is greater. The program converts the distances the ball moves in the picture to metres with the scale set in the plane of the stick, so it gives too small values for the ball's distances. The acceleration is proportional to the distance, so it is corrected by the same ratio (chapter *Measuring and the reliability of a measurement*).
**Formula:** $a_\text{c} = \dfrac{d_\text{ball}}{d_\text{stick}}\,a$ and $\Delta a_\text{c} = \dfrac{d_\text{ball}}{d_\text{stick}}\,\Delta a$
**Conversions:** The distances are in the same unit, so their ratio has no unit.
**Substitution:** $a_\text{c} = \dfrac{3.30\,\text{m}}{3.00\,\text{m}} \cdot 8.88\,\text{m/s}^2 = 1.10 \cdot 8.88\,\text{m/s}^2 = 9.768\,\text{m/s}^2$ and $\Delta a_\text{c} = 1.10 \cdot 0.10\,\text{m/s}^2 = 0.11\,\text{m/s}^2$
**Answer:** The corrected acceleration of free fall is $a_\text{c} \approx (9.8 \pm 0.1)\,\text{m/s}^2$, with one decimal instead of two, because the uncertainty is about $0.1\,\text{m/s}^2$. The error made the result about $9\,\%$ smaller.
**Reasonableness:** The corrected result differs from the table value $9.81\,\text{m/s}^2$ by only $0.04\,\text{m/s}^2$, less than the uncertainty, so the scale error explains the whole difference. The direction of the error is right too: too small a scale gives too small an acceleration.

### d)
**Find:** whether calculating the acceleration from the first and the last point only is a good method
**Principle:** Every measurement point has a small random error. The fit uses all the points at once, so the error of a single point affects it less, and the fit also gives the uncertainty of the coefficient (chapter *Graphing and fitting a straight line*).
**Model answer:** The suggestion is worse than the fit. Here the two-point calculation gives $a = \dfrac{2 \cdot 1.115\,\text{m}}{(0.50\,\text{s})^2} \approx 8.92\,\text{m/s}^2$, almost the same as the fit, but the result depends entirely on two points: an error of a few millimetres or a wrongly chosen starting moment would change it directly, and the method does not tell you the uncertainty of the result. The formula also assumes that the ball is exactly at rest at the moment $0$. The fit uses all eleven points, allows a small initial velocity in the coefficient $B$, gives the uncertainty $\Delta A$ and shows whether the model fits the points. Neither method, however, corrects the systematic error of the scale: it has to be corrected separately, or the scale has to be set in the plane in which the ball falls.

### Yleisiä virheitä
- The acceleration is read directly as $A = 4.44\,\text{m/s}^2$ without the factor $2$.
- The difference from the table value is explained by air resistance or reaction time, although the scatter of the points is small and the data tell you where the scale was set.
- The correction is made in the wrong direction, that is, the result is multiplied by the ratio $3.00 : 3.30$.
- The uncertainty of the fit is taken as the whole uncertainty of the result, and the systematic error is ignored.

### Hyväksytään myös
- In part c first correcting the coefficient $A$: $A_\text{c} = 1.10 \cdot (-4.44\,\text{m/s}^2) = -4.88\,\text{m/s}^2$ and then $a_\text{c} = 2A_\text{c}$.
- In part b the comparison as relative numbers: a difference of about $9.5\,\%$, an uncertainty of about $1\,\%$.
