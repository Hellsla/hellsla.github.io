# Pressure, gases and the heat engine

> **Why** must the pressure of a car's tyres be checked when a hard frost sets in, even though no air has leaked from the tyres?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a frosty morning in a yard. On the left a garage whose door is open and in which a warm light is on; a compressed-air hose hangs on the wall. In the yard stands a car that has been outside all night: there is frost on its roof and windows. The red column of the thermometer on the outer wall of the garage is low. In the background snowy spruces and a pale morning sky." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-kaasut-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

The problems of this lesson revolve around one quantity: **pressure is the force perpendicular to a surface divided by the area**. In a liquid, pressure comes from the weight of the liquid above, so it increases with depth. In a gas, it comes from the collisions of the particles with the walls of the container, so it depends on the amount, the volume and the temperature of the gas. When the pressure of a gas pushes a piston, the gas does work, and in this way a heat engine turns part of the heat into work.

The gas problems of the exam need two checks before the numbers. **The temperature in kelvins**, because the gas laws are proportionalities that start from absolute zero. **The total pressure**, because a pressure gauge usually shows only the gauge pressure, and the particles of the gas produce the whole pressure.

<svg data-fig="kartta" viewBox="0 0 380 956" role="img" aria-label="Recognition chart: how do I tell which law to use? Start from the situation and see which sign in the task fits. Force spread over an area: pressure is force divided by area. Depth in a liquid: the pressure of the liquid is density times the acceleration of free fall times depth. Depth and air pressure: the total pressure is the pressure at the surface, usually air pressure, plus the pressure of the liquid. Amount of substance known: use the equation of state, pressure times volume is the amount of substance times the gas constant times the temperature. The state changes, the amount of substance does not: write the two states, pressure times volume divided by temperature is the same at the start and at the end. Temperature in degrees Celsius: convert to kelvins by adding 273.15. Constant pressure, volume changes: the magnitude of the work is pressure times the magnitude of the change of volume. Internal energy changes: the first law of thermodynamics, the change of internal energy is the heat plus the work. A machine takes in heat and does work: the efficiency of a heat engine is the work divided by the heat taken in." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="912" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{situation first, then the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{force spread over an area}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{pressure}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p = F/A$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{depth in a liquid}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{liquid pressure}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p = \rho g h$</div></foreignObject>
  <line x1="14" y1="321" x2="30" y2="321" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{depth and air pressure}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{total pressure}$</div></foreignObject>
  <rect x="192" y="344" width="170" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="196" y="346" width="162" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p = p_0 + \rho g h$</div></foreignObject>
  <line x1="14" y1="422" x2="30" y2="422" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="386" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="396.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{amount (mol) known}$</div></foreignObject>
  <line x1="40" y1="426" x2="362" y2="426" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="431" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{equation of state}$</div></foreignObject>
  <rect x="238" y="430" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="432" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$pV = nRT$</div></foreignObject>
  <line x1="14" y1="523" x2="30" y2="523" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="472" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="482.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{state changes, amount does not}$</div></foreignObject>
  <line x1="40" y1="512" x2="362" y2="512" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="517" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{two states}$</div></foreignObject>
  <rect x="182" y="546" width="180" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="186" y="548" width="172" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p_1V_1/T_1 = p_2V_2/T_2$</div></foreignObject>
  <line x1="14" y1="639" x2="30" y2="639" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="588" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="598.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{temperature in degrees Celsius}$</div></foreignObject>
  <line x1="40" y1="628" x2="362" y2="628" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="633" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{convert to kelvins}$</div></foreignObject>
  <rect x="172" y="662" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="664" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$T = \theta + 273.15\,\text{K}$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{constant pressure, volume changes}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{work done}$</div></foreignObject>
  <rect x="232" y="748" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="750" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$W = p\Delta V$</div></foreignObject>
  <line x1="14" y1="826" x2="30" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="790" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="800.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{internal energy changes}$</div></foreignObject>
  <line x1="40" y1="830" x2="362" y2="830" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="835" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{1st law}$</div></foreignObject>
  <rect x="232" y="834" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="836" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta U = Q + W$</div></foreignObject>
  <line x1="14" y1="912" x2="30" y2="912" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="876" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="886.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{machine takes heat, does work}$</div></foreignObject>
  <line x1="40" y1="916" x2="362" y2="916" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="921" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{efficiency}$</div></foreignObject>
  <rect x="238" y="920" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="922" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = W/Q_1$</div></foreignObject>
</svg>

The opening question is answered with these two checks. In the warm garage ($+20\,{}^\circ\text{C}$) the gauge showed a gauge pressure of $230\,\text{kPa}$, so the total pressure was $101\,\text{kPa} + 230\,\text{kPa} = 331\,\text{kPa}$. When the volume of the tyre stays almost the same, the total pressure is proportional to the kelvin temperature: after a night of frost ($-20\,{}^\circ\text{C}$) it is $$
\begin{aligned}
&331\,\text{kPa} \cdot 253\,\text{K} : 293\,\text{K} \\
&\approx 286\,\text{kPa}
\end{aligned}
$$. The gauge now shows only about $185\,\text{kPa}$, even though no air has leaked.

<svg data-fig="rengas" viewBox="0 0 480 330" role="img" aria-label="Bar chart to scale: the total pressure of the air in a tyre at two temperatures. Each horizontal bar is divided into two parts: the air pressure 101 kPa and the gauge pressure shown by the gauge. In the warm garage, +20 °C, the gauge pressure is 230 kPa and the total pressure 331 kPa. After a night of frost, −20 °C, the total pressure is 286 kPa and the gauge pressure 185 kPa. The total pressure has decreased in the ratio of the kelvin temperatures, but the gauge reading has decreased by 45 kPa, that is, by about a fifth." style="max-width:100%;font-size:20px">
  <line x1="140" y1="40" x2="140" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="40" x2="240" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="40" x2="340" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="50" y="26" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#c92a2a">$+20\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="40" y="60" width="101" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="141" y="60" width="230" height="46" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="76" y="71" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_0$</div></foreignObject>
  <foreignObject x="221" y="71" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\Delta p = 230$</div></foreignObject>
  <foreignObject x="379" y="71" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$331\,\text{kPa}$</div></foreignObject>
  <foreignObject x="50" y="138" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$-20\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="40" y="172" width="101" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="141" y="172" width="185" height="46" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="76" y="183" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_0$</div></foreignObject>
  <foreignObject x="198.5" y="183" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\Delta p = 185$</div></foreignObject>
  <foreignObject x="334" y="183" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$286\,\text{kPa}$</div></foreignObject>
  <line x1="39" y1="268" x2="392" y2="268" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M404,268 L391,274 L391,262 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="40" y1="269" x2="40" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="140" y1="268" x2="140" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="120.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$100$</div></foreignObject>
  <line x1="240" y1="268" x2="240" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$200$</div></foreignObject>
  <line x1="340" y1="268" x2="340" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="320.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$300$</div></foreignObject>
  <foreignObject x="16" y="280" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="410" y="256" width="74" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$p\ (\text{kPa})$</div></foreignObject>
</svg>

```pysahdy
Why is the gauge reading $230\,\text{kPa}$ not used directly when calculating the gas pressure?
---
The gauge shows only the gauge pressure, but the gas particles produce the whole pressure. So atmospheric pressure is added: $101\,\text{kPa} + 230\,\text{kPa} = 331\,\text{kPa}$.
```

## Formula: Pressure, gases and the heat engine

### Pressure and pressure in a liquid

```kaavat
pressure caused by a force :: p = \frac{F}{A}
```

where $p$ is the pressure (Pa), $F$ the force perpendicular to the surface (N) and $A$ the area (m²). In a liquid at rest, at the depth $h$

```kaavat
hydrostatic pressure :: p = \rho g h
```

where $\rho$ is the density of the liquid (kg/m³) and $g = 9.81\,\text{m/s}^2$. The hydrostatic pressure is the gauge pressure, and it depends only on the depth and the density, not on the shape of the container. The total pressure at the depth $h$ is $p_0 + \rho g h$, where $p_0$ is the pressure at the surface, usually the air pressure of about $101\,\text{kPa}$. The force caused by pressure is always perpendicular to the surface.

### The state of a gas

```kaavat
ideal gas law :: pV = nRT
```

where $V$ is the volume (m³), $n$ the amount of substance (mol), $R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ and $T$ the temperature in kelvins. The amount of substance is obtained from the mass, $n = m/M$, where $M$ is the molar mass. The equation holds for a dilute gas, when the pressure is not very high and the temperature not very low. When the amount of gas stays the same,

```kaavat
combined gas law (constant amount of gas) :: \frac{pV}{T} = \text{constant}
```

that is, for two states $\tfrac{p_1 V_1}{T_1} = \tfrac{p_2 V_2}{T_2}$. From it follow the special cases: at constant temperature Boyle's law $p_1V_1 = p_2V_2$, at constant pressure $V \propto T$ and at constant volume $p \propto T$. The kelvin temperature is

```pysahdy
Why is extending the line to zero pressure only a prediction of the gas model?
---
A real gas condenses into a liquid before the temperature gets there, so extending the line to zero is a prediction of the gas model.
```

```latex
T = \theta + 273.15\,\text{K}
```

where $\theta$ is the numerical value of the Celsius temperature. In an experiment, absolute zero is obtained by extending the $(\theta, p)$ or $(\theta, V)$ line to zero. It is a prediction of the model: a real gas condenses into a liquid before that.

### Work done by a gas and the heat engine

A gas expanding at constant pressure does work, and work is done on a compressed gas:

```kaavat
work done by an expanding gas / on a compressed gas :: W = p\Delta V
```

where $\Delta V$ is the magnitude of the change in volume (m³); the work is the area under the ($V$, $p$) graph. By the first law of thermodynamics the internal energy of the gas changes by

```kaavat
first law of thermodynamics :: \Delta U = Q + W
```

where $Q$ is the heat transferred to the gas (J) and $W$ the work done on the gas (J). In a compression $W = p\Delta V$ is positive. An expanding gas itself does the work $p\Delta V$, so then $W = -p\Delta V$ and the internal energy decreases by this amount.

In one cycle a heat engine takes the heat $Q_1$ ($\text{J}$) from a hot source, does the work $W$ ($\text{J}$) and gives the heat $Q_2$ ($\text{J}$) to a colder environment. At the end of the cycle the gas of the engine is in the same state as at the start. The efficiency of the engine is

```kaavat
efficiency of a heat engine :: \eta = \frac{W}{Q_1}
```

```pysahdy
Why is the efficiency of a heat engine always below $100\,\%$?
---
Part of the heat $Q_1$ taken in must be released as heat $Q_2$ to the colder surroundings, so the work $W$ is smaller than $Q_1$.
```

Part of the heat must always be given to a colder place, so the efficiency of a heat engine stays well below $100\,\%$. The smaller the temperature difference $T_1 - T_2$ is compared with the temperature $T_1$ of the hot source, the smaller the share of the heat the engine can turn into work. In a power plant the same is calculated from powers: the electrical power divided by the fuel power.

<svg data-fig="kone" viewBox="0 0 420 470" role="img" aria-label="Energy flows of a heat engine during one cycle, arrow widths to scale. At the top the hot source, whose temperature is T1. From it a wide heat arrow Q1 = 1000 J comes down into the engine. From the engine a narrow green arrow, the work W = 350 J, goes to the right, and a heat arrow Q2 = 650 J goes down to the colder environment, whose temperature is T2. The outgoing arrows together are as wide as the incoming arrow." style="max-width:100%;font-size:20px">
  <image href="pics/fy9/fy9-kaasut-kone.webp" x="0" y="0" width="420" height="469" preserveAspectRatio="none"/>
  <foreignObject x="149" y="31" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{hot source } T_1$</div></foreignObject>
  <foreignObject x="222" y="120" width="102" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#e8590c">$Q_1 = 1000\,\text{J}$</div></foreignObject>
  <foreignObject x="115" y="226" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{engine}$</div></foreignObject>
  <foreignObject x="187" y="328" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#e8590c">$Q_2 = 650\,\text{J}$</div></foreignObject>
  <foreignObject x="230" y="188" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#2b8a3e">$W = 350\,\text{J}$</div></foreignObject>
  <foreignObject x="107" y="413" width="206" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{colder environment } T_2$</div></foreignObject>
</svg>

```johda
In one cycle a heat engine takes the heat $Q_1$ from a hot source and gives the heat $Q_2$ to a colder environment. Derive the work $W$ done by the engine in one cycle in terms of the heats $Q_1$ and $Q_2$.
---
Apply the first law of thermodynamics $\Delta U = Q + W$ to the gas of the engine over one cycle. At the end of the cycle the gas is in the same state as at the start, so its internal energy does not change: $\Delta U = 0$.

In one cycle the heat $Q_1$ comes into the gas and the heat $Q_2$ leaves it. The heat transferred to the gas is therefore

$$Q = Q_1 - Q_2$$

In the first law $W$ is the work done on the gas. The engine itself does the work $W$ on its surroundings, so the work done on the gas is $-W$, just as in an expansion it is $-p\Delta V$. Substitute into the first law:

$$0 = (Q_1 - Q_2) + (-W)$$

Solve for the work of the engine:

$$W = Q_1 - Q_2$$

The result is the conservation of energy: in the figure the incoming heat $Q_1$ divides into the work $W$ and the heat given out $Q_2$.
```

## Common mistakes {Virheet}

- **Degrees Celsius in a ratio.** The pressure of a gas heated from $20\,{}^\circ\text{C}$ to $40\,{}^\circ\text{C}$ increases by only about $7\,\%$, it does not double: $313\,\text{K} : 293\,\text{K} \approx 1.07$.
- **Gauge pressure in a gas law.** The gauge reading is not the pressure of the gas. Add the air pressure before calculating and subtract it only at the end, if the gauge reading is asked for.
- **Units mixed up.** In the ideal gas law the pressure is in pascals and the volume in cubic metres. Kilopascals and litres work together, because $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$, but kilopascals and cubic metres give an error of a factor of a thousand.
- **Pressure and force mixed up.** The same force on a small area gives a large pressure. Force is obtained from pressure only by multiplying by the area.
- **Suction pulls.** A suction cup or a straw does not pull anything: the pressure of the outside air pushes when the pressure inside is lower.
- **A heat engine could turn all the heat into work.** Removing friction does not help: the heat $Q_2$ cannot be avoided.

## Review if needed {Kertaa}

- Pressure, gauge pressure and pressure at depth: [*Pressure and hydrostatic pressure*](fy3-4.html).
- Boyle's law and the changes of state of gases: [*Changes of state of a gas and Boyle's law*](fy3-9.html). Amount of substance and the ideal gas law: [*Ideal gas law*](fy3-10.html).
- Extending a line to zero and its uncertainty: [*Determining absolute zero*](fy3-13.html).
- Work done by a gas, the heat engine and the heat pump: [*Work done by a gas and the heat engine*](fy3-11.html). The efficiency of a power plant: [*Energy production and the efficiency of power plants*](fy3-15.html).
