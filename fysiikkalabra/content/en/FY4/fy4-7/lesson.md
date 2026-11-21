# Kinetic energy, potential energy and mechanical energy

> **Why** does a skateboarder who is twice as fast rise four times as high on a ramp?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a skateboarder in a skatepark. The skateboarder is drawn in three places: on level ground in front of the ramp a long blue speed arrow v starts from her, three quarters of the way up the ramp the arrow is half as long, v/2, and at the top she is still for a moment, v = 0. A height gauge on the side of the ramp shows the heights: half of the speed is used up in the rise of three quarters, 3/4 h, the other half only in the last quarter, 1/4 h. The lengths of the arrows (2 : 1 : 0) and the heights are to scale." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-7-hero.webp" x="12.4" y="17.3" width="1188.1" height="599" preserveAspectRatio="none"/>
  <foreignObject x="256.5" y="380" width="39" height="72" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:60px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="855.5" y="41.5" width="37" height="134" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:56px;color:#1971c2">$\dfrac{v}{2}$</div></foreignObject>
  <foreignObject x="1007.5" y="24" width="102" height="72" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:60px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$v = 0$</span></div></foreignObject>
  <foreignObject x="1086" y="349" width="66" height="134" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:56px">$\dfrac{3}{4}h$</div></foreignObject>
  <foreignObject x="1086" y="184" width="66" height="134" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:56px">$\dfrac{1}{4}h$</div></foreignObject>
</svg>

## Key idea

### Height stores energy
In the chapter *Forms of energy and conservation of energy*, potential energy and kinetic energy were forms of energy. Now we calculate how much of them there is. When an object is lifted higher, energy is transferred to it: a book lifted onto a shelf can gain speed when it falls, and water pumped uphill can turn a turbine. This energy tied to the position of an object is called **potential energy**. Gravitational potential energy is greater the greater the mass of the object and the higher it is. Lifting two identical books onto the same shelf takes twice as much energy as lifting one, and lifting by two metres takes twice as much as lifting by one metre. The height is measured from a chosen **zero level**, for example the floor.

### Kinetic energy grows with the square of the speed
A moving object has **kinetic energy**. When a cart goes up a frictionless ramp, it slows down, and its kinetic energy changes into potential energy. The cart rises as high as a ball thrown straight up at the same speed in the chapter *Acceleration and uniformly accelerated motion*, that is, to the height $h = \tfrac{v^2}{2g}$: on the ramp the acceleration is smaller, but the distance is correspondingly longer. At double the speed the cart therefore rises four times as high, and that takes four times as much energy. **Kinetic energy is proportional to the square of the speed.** The mass does not change the rise height, but lifting a cart that is twice as heavy to the same height takes twice the energy. Kinetic energy is therefore also proportional to the mass.

<svg data-fig="ramppi" viewBox="0 0 600 360" role="img" aria-label="Two pictures of the same ramp, heights and speed arrows to scale. On the left a cart starts from the foot of the ramp at speed v, shown by a short blue arrow, and rises to height h. On the right the same cart starts at double the speed 2v, the arrow is twice as long, and it rises to height 4h, that is, four times as high. There is no friction." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-7-ramppi.webp" x="0" y="-1.2" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="60.5" y="233.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="16" y="271" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="365.5" y="233.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$2\overline{v}$</div></foreignObject>
  <foreignObject x="348" y="176" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4h$</div></foreignObject>
</svg>

The square of the speed shows in traffic. When the speed of a car grows from $50\,\text{km/h}$ to $70\,\text{km/h}$, the kinetic energy grows by the factor $\left(\tfrac{70}{50}\right)^2 \approx 2.0$, that is, almost doubles. This is exactly the energy that braking or a collision has to change into other energy.

```pysahdy
The speed of a car triples. By what factor does its kinetic energy change?
---
It becomes nine times as large, because kinetic energy is proportional to the square of the speed and $3^2 = 9$.
```

### A conservative force returns the energy
When a frictionless cart has risen to its highest point on the ramp, it starts back down and is at the foot of the ramp as fast as when it started. Gravity returns as kinetic energy all the energy that changed into potential energy in the rise. In addition, a frictionless object that starts from rest at a height $h$ gets the same speed on the way down, whether it falls straight down or slides down a steep or a gentle ramp: the energy depends only on height, not on the path. A force with these properties is called a **conservative force**. Potential energy is always associated with a conservative force.

<svg data-fig="polut" viewBox="0 0 600 350" role="img" aria-label="Schematic picture, not to scale. Three routes from the same height h to the floor: on the left a ball falls straight down beside a tower, in the middle a cart goes down a steep ramp and on the right down a gentler ramp. There is no friction or air resistance. At the bottom all three have a blue speed arrow of equal length: the speed is the same, because gravitational potential energy depends only on height, not on the path." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-7-polut.webp" x="0" y="-1.2" width="600" height="360" preserveAspectRatio="none"/>
  <foreignObject x="96" y="215.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="210.5" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="480.5" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="564" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="171" y="25.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{same height, same speed}$</div></foreignObject>
</svg>

Gravitational potential energy is not the only kind of potential energy. A stretched spring, a drawn bow and a compressed trampoline return the energy as kinetic energy: the spring force is conservative, and a stretched spring has **spring potential energy**. The force between electric charges is also conservative. Friction and air resistance, on the other hand, are not conservative. They change kinetic energy into the internal energy of the objects and the air, and this energy does not return as motion even if the object returns to its starting place. That is why no potential energy is associated with friction.

```pysahdy
A box slides on a floor with friction and stops. Where did its kinetic energy go, and why does it not return as motion?
---
It changed into internal energy of the box and the floor. Friction is not a conservative force, so this energy does not return as kinetic energy.
```

### Mechanical energy
The kinetic energy and the potential energy of an object together are its **mechanical energy**. When a cart goes up a frictionless ramp, the kinetic energy decreases and the potential energy grows by the same amount, so the mechanical energy stays the same. When friction acts, part of the mechanical energy changes into internal energy, and the mechanical energy decreases. In the chapter *Conservation of mechanical energy and the work–energy principle* this becomes a tool for calculation.

```pysahdy
A frictionless cart goes up a ramp, and its kinetic energy decreases by $30\,\text{J}$. What happens to its potential energy and its mechanical energy?
---
The potential energy grows by $30\,\text{J}$, so the mechanical energy stays the same.
```

## Formula: Kinetic energy and potential energy
Gravitational potential energy is
```kaavat
gravitational potential energy near the Earth's surface :: E_\text{p} = m g h
```
where $E_\text{p}$ is the potential energy ($\text{J}$), $m$ the mass ($\text{kg}$), $g = 9.81\,\text{m/s}^2$ the acceleration of free fall and $h$ the height from the chosen zero level ($\text{m}$). The expression holds near the surface of the Earth, where $g$ is constant. Below the zero level $h < 0$, so the potential energy is negative. The unit is $\text{kg} \cdot \text{m/s}^2 \cdot \text{m} = \text{N} \cdot \text{m} = \text{J}$.

Kinetic energy is
```kaavat
kinetic energy :: E_\text{k} = \tfrac{1}{2}\,m v^2
```
where $E_\text{k}$ is the kinetic energy ($\text{J}$), $m$ the mass ($\text{kg}$) and $v$ the speed ($\text{m/s}$). The expression is obtained from the rise height on a ramp. A frictionless cart rises to the height $h = \tfrac{v^2}{2g}$, and its potential energy then grows by $m g h = m g \cdot \tfrac{v^2}{2g} = \tfrac{1}{2}\,m v^2$. That is exactly how much kinetic energy the cart had at the foot of the ramp. Kinetic energy is never negative, and it does not depend on the direction of motion.

<svg data-fig="ek-kuvaaja" viewBox="0 0 600 350" role="img" aria-label="Graph to scale: on the horizontal axis the speed from zero to 4.5 metres per second, on the vertical axis the kinetic energy from zero to 9 joules for an object whose mass is 1.0 kilograms. The graph is a parabola curving upward. At a speed of 2.0 metres per second the kinetic energy is 2.0 joules and at a speed of 4.0 metres per second 8.0 joules: double the speed gives four times the kinetic energy. Dashed lines show the readings." style="max-width:100%;font-size:24px">
  <line x1="174.5" y1="304" x2="174.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="259" y1="304" x2="259" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="343.5" y1="304" x2="343.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428" y1="304" x2="428" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="278.5" x2="470" y2="278.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="253.5" x2="470" y2="253.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="228" x2="470" y2="228" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="202.5" x2="470" y2="202.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="177.5" x2="470" y2="177.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="152" x2="470" y2="152" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="126.5" x2="470" y2="126.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="101.5" x2="470" y2="101.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="76" x2="470" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="304" x2="484" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,304 L483,310 L483,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="305" x2="90" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,50 L96,63 L84,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="174.5" y1="304" x2="174.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="164.5" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="259" y1="304" x2="259" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="249" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="343.5" y1="304" x2="343.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="428" y1="304" x2="428" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="418" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="278.5" x2="90" y2="278.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="253.5" x2="90" y2="253.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="239" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="228" x2="90" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="202.5" x2="90" y2="202.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="188" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="177.5" x2="90" y2="177.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="152" x2="90" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="83" y1="126.5" x2="90" y2="126.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="101.5" x2="90" y2="101.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="87" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="83" y1="76" x2="90" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="289.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <foreignObject x="80" y="19.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{k}\ (\text{J})$</div></foreignObject>
  <polyline points="90,304 93,304 96,304 99,304 102,303.5 105,303.5 108,303.5 111,303 114,303 117,302.5 120,302.5 123,302 126,301.5 129,301.5 132,301 135,300.5 137.5,300 140.5,299.5 143.5,299 146.5,298.5 149.5,297.5 152.5,297 155.5,296.5 158.5,295.5 161.5,295 164.5,294 167.5,293.5 170.5,292.5 173.5,291.5 176.5,290.5 179.5,290 182.5,289 185.5,288 188.5,287 191.5,285.5 194.5,284.5 197.5,283.5 200.5,282.5 203.5,281 206.5,280 209.5,278.5 212.5,277.5 215.5,276 218.5,275 221.5,273.5 224.5,272 227.5,270.5 230,269 233,267.5 236,266 239,264.5 242,263 245,261 248,259.5 251,258 254,256 257,254.5 260,252.5 263,251 266,249 269,247 272,245 275,243 278,241 281,239 284,237 287,235 290,233 293,231 296,228.5 299,226.5 302,224.5 305,222 308,219.5 311,217.5 314,215 317,212.5 319.5,210 322.5,208 325.5,205.5 328.5,203 331.5,200 334.5,197.5 337.5,195 340.5,192.5 343.5,189.5 346.5,187 349.5,184.5 352.5,181.5 355.5,178.5 358.5,176 361.5,173 364.5,170 367.5,167 370.5,164.5 373.5,161.5 376.5,158.5 379.5,155 382.5,152 385.5,149 388.5,146 391.5,142.5 394.5,139.5 397.5,136 400.5,133 403.5,129.5 406.5,126.5 409.5,123 412,119.5 415,116 418,112.5 421,109 424,105.5 427,102 430,98.5 433,95 436,91 439,87.5 442,84 445,80 448,76.5" fill="none" stroke="#e8590c" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="259" y1="253.5" x2="259" y2="304" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="253.5" x2="259" y2="253.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="259" cy="253.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="428" y1="101.5" x2="428" y2="304" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="101.5" x2="428" y2="101.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="428" cy="101.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="177" y="217" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$2.0\,\text{J}$</span></div></foreignObject>
  <foreignObject x="346" y="65" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$8.0\,\text{J}$</span></div></foreignObject>
  <foreignObject x="458" y="71.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$E_\text{k}$</div></foreignObject>
</svg>

### The zero level is chosen
You may choose the zero level freely, as long as it stays the same throughout the calculation. When a $0.50\,\text{kg}$ book is on a shelf $1.80\,\text{m}$ above the floor, its potential energy is $8.8\,\text{J}$ relative to the floor but only $4.9\,\text{J}$ relative to the surface of a table $0.80\,\text{m}$ high. When the book is moved from the shelf to the table, the potential energy decreases by the same amount in both cases, $4.9\,\text{J}$. **Only the change in potential energy has physical significance**, and it does not depend on the zero level.

<svg data-fig="nollataso" viewBox="0 0 600 400" role="img" aria-label="Schematic picture, heights to scale. On the left a wall shelf at a height of 1.80 metres and a table at a height of 0.80 metres from the floor, and on the shelf there is a book of 0.50 kilograms. On the right two vertical scales of potential energy values. When the zero level is the floor, the potential energy of the book is 8.8 joules on the shelf, 3.9 joules on the table and zero on the floor. When the zero level is the surface of the table, the values are 4.9 joules, zero and minus 3.9 joules. In both, the potential energy decreases by 4.9 joules when the book is moved from the shelf to the table." style="max-width:100%;font-size:24px">
  <rect x="20" y="18" width="240" height="304" fill="#eef5f9"/>
  <rect x="20" y="322" width="240" height="12" fill="#f1dfb5"/>
  <line x1="20" y1="322" x2="260" y2="322" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="36" y="52" width="110" height="8" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <path d="M48,60 l0,24 l18,-24 Z" fill="#6c757d" stroke-linejoin="round"/>
  <rect x="76" y="18" width="46" height="34" rx="2" fill="#1971c2" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="80" y="22" width="4" height="26" fill="#d0e6fb"/>
  <rect x="150" y="202" width="104" height="10" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <rect x="160" y="212" width="8" height="110" fill="#d9b26a" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="236" y="212" width="8" height="110" fill="#d9b26a" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="184" y="168" width="46" height="34" rx="2" fill="#1971c2" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="184" y="168" width="46" height="34" fill="#ffffff" fill-opacity="0.45"/>
  <line x1="256" y1="52" x2="576" y2="52" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="256" y1="202" x2="576" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="350" y1="46" x2="350" y2="328" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="338" y1="322" x2="362" y2="322" stroke="#2b8a3e" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="350" cy="52" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="364" y="21.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$8.8\,\text{J}$</div></foreignObject>
  <circle cx="350" cy="202" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="364" y="171.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$3.9\,\text{J}$</div></foreignObject>
  <circle cx="350" cy="322" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="364" y="291.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$0\,\text{J}$</div></foreignObject>
  <foreignObject x="290" y="339.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{zero level}$</div></foreignObject>
  <foreignObject x="315" y="367.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{floor}$</div></foreignObject>
  <line x1="330" y1="58" x2="330" y2="185" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M330,196 L324.5,184 L335.5,184 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="500" y1="46" x2="500" y2="328" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="488" y1="202" x2="512" y2="202" stroke="#2b8a3e" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="500" cy="52" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="514" y="21.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$4.9\,\text{J}$</div></foreignObject>
  <circle cx="500" cy="202" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="514" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$0\,\text{J}$</div></foreignObject>
  <circle cx="500" cy="322" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="514" y="291.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$-3.9\,\text{J}$</div></foreignObject>
  <foreignObject x="440" y="339.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{zero level}$</div></foreignObject>
  <foreignObject x="465" y="367.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{table}$</div></foreignObject>
  <line x1="480" y1="58" x2="480" y2="185" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M480,196 L474.5,184 L485.5,184 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="402.5" y="96.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Delta E_\text{p}$</div></foreignObject>
  <foreignObject x="377.5" y="128.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$= -4.9\,\text{J}$</div></foreignObject>
  <foreignObject x="152" y="41.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$1.80\,\text{m}$</div></foreignObject>
  <foreignObject x="57" y="187.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0.80\,\text{m}$</div></foreignObject>
</svg>

Mechanical energy is the sum of kinetic and potential energy:
```latex
E_\text{mech} = E_\text{k} + E_\text{p}
```
where $E_\text{mech}$ is the mechanical energy ($\text{J}$). Because potential energy depends on the zero level, the value of the mechanical energy depends on it too. Always state in a calculation what the zero level is.

<figure class="unit-photo"><img src="pics/fy4/roller-coaster-loop.webp" alt="A red roller coaster loop against a blue sky. At the top of the loop the car travels with the riders upside down."><figcaption>A roller coaster car at the top of a loop on a sunny day.</figcaption></figure>

## Worked example
A snowboarder whose mass with equipment is $68\,\text{kg}$ goes down a slope. At a point $25\,\text{m}$ above the bottom of the slope her speed is $12\,\text{m/s}$. How great is the snowboarder's mechanical energy at this point when the bottom of the slope is chosen as the zero level?

<!-- vaihe -->

**Given and find.** Mass $m = 68\,\text{kg}$, speed $v = 12\,\text{m/s}$, height above the zero level $h = 25\,\text{m}$ and acceleration of free fall $g = 9.81\,\text{m/s}^2$. We are asked for the mechanical energy $E_\text{mech}$.

<!-- vaihe -->

**Principle.** Mechanical energy is the sum of kinetic energy and potential energy. Kinetic energy is calculated from the speed and potential energy from the height above the zero level, that is, the bottom of the slope. With such a small difference in height the acceleration of free fall is constant, so $E_\text{p} = m g h$ holds.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&E_\text{mech} = E_\text{k} + E_\text{p} \\
&E_\text{mech} = \tfrac{1}{2}\,m v^2 + m g h
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** All quantities are in SI units, so no conversions are needed. Both terms come in the unit $\text{kg} \cdot \text{m}^2/\text{s}^2 = \text{J}$.

<!-- vaihe -->

**Substitution.** First we calculate each energy and then their sum:
```latex
\begin{aligned}
&E_\text{k} = \tfrac{1}{2}\,m v^2 \\
&= \tfrac{1}{2} \cdot 68\,\text{kg} \cdot (12\,\text{m/s})^2 \\
&= 4896\,\text{J}
\\[4pt]
&E_\text{p} = m g h \\
&= 68\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 25\,\text{m} \\
&\approx 16\,677\,\text{J}
\\[4pt]
&E_\text{mech} = 4896\,\text{J} + 16\,677\,\text{J} \\
&\approx 21\,573\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The snowboarder's mechanical energy is about $22\,\text{kJ}$ relative to the bottom of the slope. Two significant figures, like the mass $68\,\text{kg}$, the speed $12\,\text{m/s}$ and the height $25\,\text{m}$.

<!-- vaihe -->

**Reasonableness.** With rounded numbers $E_\text{k} \approx \tfrac{1}{2} \cdot 70\,\text{kg} \cdot 150\,\text{m}^2/\text{s}^2 \approx 5\,\text{kJ}$ and $E_\text{p} \approx 70\,\text{kg} \cdot 10\,\text{m/s}^2 \cdot 25\,\text{m} = 17.5\,\text{kJ}$, together about $23\,\text{kJ}$, close to the result. Both energies are positive, because the snowboarder is moving and is above the zero level.

## Common misconception
Many people think that double the speed means double the kinetic energy. Kinetic energy, however, grows with the square of the speed: double the speed gives four times and triple the speed nine times the kinetic energy. Another mistake is to treat potential energy as a property of the object itself with one correct value. Its value depends on the chosen zero level, and only the change in potential energy is the same whatever the zero level. A third mistake is to think that potential energy is associated only with gravity. Potential energy is also associated with the spring force, but not with friction, because friction does not return the energy as motion.

## Summary
- Kinetic energy $E_\text{k} = \tfrac{1}{2}\,m v^2$ is proportional to the mass and the square of the speed: double the speed gives four times the kinetic energy.
- Gravitational potential energy $E_\text{p} = m g h$ depends on the height above the chosen zero level. Below the zero level it is negative, and only its change has physical significance.
- Potential energy is associated with a conservative force, such as gravity or the spring force, which returns the energy as kinetic energy and whose energy depends only on position, not on the path. Friction and air resistance are not conservative.
- Mechanical energy is $E_\text{mech} = E_\text{k} + E_\text{p}$. When there is no friction or air resistance and the object is not pushed or pulled, it stays the same; friction and air resistance change part of it into internal energy.
