# Thermodynamic system, state variables and temperature

> **Why** does a bicycle tyre feel harder on a hot summer day than on a frosty day, even though no more air has been pumped into it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a bicycle stands on hot asphalt in the summer heat. The sun is shining, heat shimmers above the asphalt, and the red column of the thermometer on the post is high." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
When you study a phenomenon, you separate the part of the world you are looking at from the rest. The separated part is the thermodynamic system, and everything outside it is the surroundings. The air in a bicycle tyre is an example of a system. If no matter can leave or enter the system, the system is closed. The state of a system is described by state variables: temperature, pressure and volume, and the amount of substance. Pressure is force per unit area; its unit is the pascal (Pa), and $1\,\text{kPa} = 1000\,\text{Pa}$. Pressure is studied in more detail later. When you change one state variable of a gas system, at least one of the others changes too.

```pysahdy
The air in a bicycle tyre is the system. What is the surroundings then?
---
The surroundings are everything outside the system, for example the tyre, the rim and the outside air.
```

<svg data-fig="system" viewBox="0 0 600 340" role="img" aria-label="Principle diagram, not to scale: gas in a cylinder whose upper end is closed by a movable piston. The gas is a thermodynamic system; its boundary is drawn as a dashed line around the gas. The walls of the cylinder, the piston and the rest of the world are the surroundings. The state variables that describe the state of the system are pressure p, volume V and temperature T." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-system.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="180" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="224" y="154.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="72" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V$</div></foreignObject>
  <foreignObject x="412" y="220.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{system}$</div></foreignObject>
  <foreignObject x="412" y="175.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{boundary}$</div></foreignObject>
  <foreignObject x="412" y="105.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{surroundings}$</div></foreignObject>
</svg>

The micro model of matter explains why this happens. A gas consists of particles that move all the time in all directions and collide with each other and with the walls of the container. The temperature of a gas tells you the average kinetic energy of the particles: the hotter the gas, the faster the particles move on average. Pressure arises when particles hit the wall and each collision pushes the wall a little. When the volume decreases and the temperature stays the same, the particles have less room and hit the wall more often, so the pressure increases, but a single collision does not become harder. When the temperature rises but the volume stays the same, the particles hit the wall both more often and harder, so the pressure increases. This is why the tyre feels harder in summer.

```pysahdy
Why does the pressure of a gas increase when the volume is decreased and the temperature stays the same?
---
The particles have less room, so they hit the wall more often. A single collision does not become harder.
```

<svg data-fig="micro-model" viewBox="0 0 600 300" role="img" aria-label="Schematic diagram of the micro model of a gas: two closed containers of the same size with the same number of particles. In the cold gas the arrows showing speed are short, in the hot gas they are long, and the pressure p2 of the hot gas is greater than the pressure p1 of the cold gas." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-micro-model.webp" x="4.9" y="8.6" width="591.1" height="306.7" preserveAspectRatio="none"/>
  <foreignObject x="107.5" y="25.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{cold gas}$</div></foreignObject>
  <foreignObject x="403.5" y="25.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hot gas}$</div></foreignObject>
  <foreignObject x="138.5" y="257.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_1$</div></foreignObject>
  <foreignObject x="380" y="257.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_2 \gt p_1$</div></foreignObject>
</svg>

The figure is schematic: the length of an arrow shows the speed of a particle. The containers are the same size and contain the same number of particles.

Temperature is measured on the Celsius scale, where $0\,{}^\circ\text{C}$ is the freezing point of water and $100\,{}^\circ\text{C}$ is the boiling point of water at normal pressure, and on the Kelvin scale. The zero of the Kelvin scale is absolute zero, the lowest possible temperature. At absolute zero the average kinetic energy of the particles is at its smallest, and nothing can be colder. A Celsius degree and a kelvin are the same size, so a temperature difference is the same in kelvins and in degrees Celsius. When the volume and the amount of gas stay the same and the gas is dilute, that is, far from liquefying, the pressure of the gas is directly proportional to the temperature in kelvins. The average kinetic energy of the particles of a dilute gas is also directly proportional to the temperature in kelvins, so ratios of temperatures are compared in kelvins. The connection between pressure, volume and temperature is studied in more detail in the chapter *Changes of state of a gas and Boyle's law*.

<figure class="unit-photo"><img src="pics/fy3/liquid-thermometer.webp" alt="A glass liquid thermometer on a blue background. The numbers 36–39 are visible on the scale."><figcaption>A thermometer shows its own temperature. That is why the thermometer must be in thermal equilibrium with the object before the reading tells the object's temperature.</figcaption></figure>

<figure class="unit-photo"><img src="pics/fy3/liquid-nitrogen.webp" alt="A hand holds a glass dish from which liquid pours, surrounded by white mist."><figcaption>Liquid nitrogen poured from a glass dish at a science festival in Katowice, Poland. Nitrogen boils at a very low temperature, and the white mist is tiny water droplets that condense from water vapour in the cold air.</figcaption></figure>

### Limits of the model
The statement "temperature tells you the average kinetic energy of the particles" holds as such for a dilute gas whose particles interact with each other only when they collide. Then the temperature is proportional to the average kinetic energy of the translational motion of the particles. In a liquid and in a solid the particles are close to each other and vibrate, pulled by their neighbours. Temperature describes the strength of the thermal motion of the particles in them too, but the energy of the substance also includes the energy of the interactions between the particles. So temperature is not the same thing as the energy of a substance: ice and water can have the same temperature $0\,{}^\circ\text{C}$, although water of the same mass has more internal energy than ice (chapters *Internal energy, heat and conservation of energy* and *Changes of state*). Even at absolute zero not all motion of the particles stops, but its energy is the smallest possible.

## Formula: Kelvin scale
The numerical values of the Celsius temperature $\theta$ and the kelvin temperature $T$ are related by the equation
```latex
\frac{T}{\text{K}} = \frac{\theta}{{}^\circ\text{C}} + 273.15
```
For example, $20\,{}^\circ\text{C}$ corresponds to $293.15\,\text{K}$. A temperature difference, on the other hand, has the same numerical value in kelvins and in degrees Celsius: a rise from $20\,{}^\circ\text{C}$ to $30\,{}^\circ\text{C}$ is $10\,\text{K}$. In practice the number 273 is often enough. For kelvins you do not use the word degree: you say "300 kelvins", not "300 degrees kelvin".

Absolute zero is therefore $0\,\text{K}$ = $-273.15\,{}^\circ\text{C}$. A temperature in kelvins cannot be negative, but a Celsius temperature can.

```pysahdy
The temperature is $250\,\text{K}$. What is it in degrees Celsius?
---
$\theta = 250 - 273.15 = -23.15$, that is $-23.15\,{}^\circ\text{C}$.
```

<svg data-fig="kelvin-scale" viewBox="0 0 600 250" role="img" aria-label="The Kelvin scale and the Celsius scale side by side to scale: 0 K is −273.15 °C (absolute zero), 273.15 K is 0 °C (water freezes) and 373.15 K is 100 °C (water boils). The intervals of the scales are the same size, and you get the reading in kelvins by adding 273.15 to the Celsius reading." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-kelvin-scale.webp" x="0" y="12.5" width="600" height="260" preserveAspectRatio="none"/>
  <foreignObject x="62" y="61.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0\,\text{K}$</div></foreignObject>
  <foreignObject x="346" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$273.15\,\text{K}$</div></foreignObject>
  <foreignObject x="466" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$373.15\,\text{K}$</div></foreignObject>
  <foreignObject x="62" y="203.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-273.15\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="358" y="203.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="473" y="203.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="62" y="15.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{absolute zero}$</div></foreignObject>
  <foreignObject x="332" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{water freezes}$</div></foreignObject>
  <foreignObject x="472" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{water boils}$</div></foreignObject>
  <foreignObject x="72" y="132.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T/\text{K} = \theta/{}^\circ\text{C} + 273.15$</div></foreignObject>
  <foreignObject x="553" y="97.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="553" y="167.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta$</div></foreignObject>
</svg>

The figure is drawn to scale. The upper scale is the Kelvin scale and the lower scale is the Celsius scale; the interval from $0\,{}^\circ\text{C}$ to $100\,{}^\circ\text{C}$ is as long as the interval from $273.15\,\text{K}$ to $373.15\,\text{K}$.

## Worked example
A closed rigid container holds gas, so its volume and the amount of substance stay the same. The pressure of the gas is measured at different temperatures:

| $\theta$ (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| $p$ (kPa) | 100 | 107 | 115 | 122 | 129 | 137 |

Use extrapolation to find the temperature at which the pressure of the gas would be zero.

<!-- vaihe -->

**Given and find.** The table has six data points $(\theta,\, p)$, and the pressure is $p_0 = 100\,\text{kPa}$ at $0\,{}^\circ\text{C}$.

You are asked for the temperature $\theta_0$ at which the pressure would be zero.

On a graph the points lie on a straight line: for every $20\,{}^\circ\text{C}$ the pressure increases by $7$–$8\,\text{kPa}$. The line is continued to the left, outside the measured range, that is, extrapolated.

<svg data-fig="extrapolation" viewBox="0 0 600 350" role="img" aria-label="Pressure of a gas as a function of temperature in a closed container: the data points in the temperature range 0–100 °C lie on a straight line, and the extrapolated line meets zero pressure at a temperature of about −270 °C. The vertical axis is at the left edge of the figure at −300 °C." style="max-width:100%;font-size:24px">
  <line x1="120.5" y1="290" x2="120.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186.5" y1="290" x2="186.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="281" y1="290" x2="281" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375.5" y1="290" x2="375.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="255.5" x2="470" y2="255.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="221.5" x2="470" y2="221.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="187" x2="470" y2="187" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="152.5" x2="470" y2="152.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="118.5" x2="470" y2="118.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="291" x2="92" y2="70" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,58 L98,71 L86,71 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120.5" y1="290" x2="120.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-270$</div></foreignObject>
  <line x1="186.5" y1="290" x2="186.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157.5" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-200$</div></foreignObject>
  <line x1="281" y1="290" x2="281" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-100$</div></foreignObject>
  <line x1="375.5" y1="290" x2="375.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="365.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="85" y1="255.5" x2="92" y2="255.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="241" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="85" y1="221.5" x2="92" y2="221.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="207" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="85" y1="187" x2="92" y2="187" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="172.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$75$</div></foreignObject>
  <line x1="85" y1="152.5" x2="92" y2="152.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="138" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="85" y1="118.5" x2="92" y2="118.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="104" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$125$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ (^\circ\text{C})$</div></foreignObject>
  <foreignObject x="82" y="27.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <foreignObject x="60" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="120,290 375.5,152.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 7"/>
  <polyline points="375.5,152.5 470,102" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="375.5" cy="152.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="394.5" cy="143" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="413.5" cy="132" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432" cy="122.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="451" cy="113" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="470" cy="102" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="120" cy="290" r="7" fill="#ffffff" stroke="#1971c2" stroke-width="3"/>
  <foreignObject x="124" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$p = 0$</div></foreignObject>
  <foreignObject x="224.5" y="251" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{extrapolation}$</span></div></foreignObject>
  <foreignObject x="413.5" y="152" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{measurements}$</span></div></foreignObject>
</svg>

The vertical axis is drawn at the left edge of the figure, at about $-300\,{}^\circ\text{C}$, and not at $\theta = 0$. The solid line is the measured range and the dashed line is the extrapolation.

<!-- vaihe -->

**Principle.** The container is closed and rigid, so the amount of gas and the volume stay the same, and the pressure depends only on the temperature. The data points are on a straight line, so the pressure changes steadily with the temperature. The equation of the line gives an estimate of the pressure also outside the measured range, if you assume that the dependence stays the same. The pressure is zero where the line crosses the temperature axis.

<!-- vaihe -->

**Rearranged formula.** The slope $k$ is calculated from two points of the line that are far apart. Here the data points lie on the line within the reading accuracy, so the end points of the measured range are also points of the line. In the equation of the line, $p_0$ is the pressure at $0\,{}^\circ\text{C}$. Set $p = 0$ and solve for $\theta_0$:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\[4pt]
&p = p_0 + k\theta \\
&0 = p_0 + k\theta_0 \\
&\theta_0 = -\frac{p_0}{k}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** No conversions are needed. The pressures are already in kilopascals, and the temperature difference $\Delta\theta$ is the same in degrees Celsius and in kelvins, so the unit of the slope $\tfrac{\text{kPa}}{{}^\circ\text{C}}$ is also $\tfrac{\text{kPa}}{\text{K}}$. The result comes out directly in degrees Celsius, because the temperatures in the table are in degrees Celsius.

<!-- vaihe -->

**Substitution.** First calculate the slope and then the zero point:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\
&= \frac{(137 - 100)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} \\
&= 0.37\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \\[6pt]
&\theta_0 = -\frac{p_0}{k} \\
&= -\frac{100\,\text{kPa}}{0.37\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} \\
&= -270.27\,{}^\circ\text{C}
\end{aligned}
```

<!-- vaihe -->

**Result.** The temperature at zero pressure is about $-270\,{}^\circ\text{C}$. The result is given with two significant figures, because the slope $0.37\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ is known only to two figures.

<!-- vaihe -->

**Reasonableness.** The result is close to absolute zero, $-273.15\,{}^\circ\text{C}$: only about $3\,{}^\circ\text{C}$, or one per cent, away from it.

An independent check: if the pressure is proportional to the temperature in kelvins, $p = 100\,\text{kPa}$ corresponds to $273.15\,\text{K}$, so the pressure at $100\,{}^\circ\text{C}$ would be $100\,\text{kPa} \cdot \tfrac{373.15}{273.15} = 136.6\,\text{kPa}$, and the measured value is $137\,\text{kPa}$.

According to the micro model, at zero pressure the motion of the particles would be so small that no pressure would arise any more. Real gases liquefy before this temperature is reached, so the continuation of the line is only a model and describes a limiting value.

## Common misconception
Many people think that the temperature doubles when it rises from $10\,{}^\circ\text{C}$ to $20\,{}^\circ\text{C}$. The physically correct comparison is made in kelvins: from $283\,\text{K}$ to $293\,\text{K}$. The ratio of the temperatures is 293/283 ≈ 1.035, so the increase is about $3.5\,\%$. This is why the average kinetic energy of the particles does not double. Another mistake is to think that $0\,{}^\circ\text{C}$ is the lowest possible temperature. It is only the freezing point of water, and the lowest possible temperature is $0\,\text{K}$.

## Summary
- A thermodynamic system is a separated part of the world. Its state is described by state variables: temperature, pressure, volume and amount of substance.
- In a gas system, temperature, pressure and volume depend on each other: if you change one, at least one of the others changes too.
- Micro model of a gas: temperature tells you the average kinetic energy of the particles, and pressure arises from the collisions of the particles with the wall. In a liquid and in a solid the energy also includes the energy of the interactions between the particles, so temperature is not the same thing as the energy of a substance.
- When the volume and the amount of substance stay the same, the pressure of a dilute gas is directly proportional to the temperature in kelvins. Continuing the line through the data points, that is, extrapolation, gives an estimate of absolute zero.
- The conversion is $\tfrac{T}{\text{K}} = \tfrac{\theta}{{}^\circ\text{C}} + 273.15$. Absolute zero is $0\,\text{K}$ = $-273.15\,{}^\circ\text{C}$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: the same bicycle on a snowy frosty morning. There is snow on the ground and on the saddle, and the column of the thermometer on the post is low." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
