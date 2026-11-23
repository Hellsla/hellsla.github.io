# Thermal balance during a change of state

> **Why** do ice cubes cool a drink so effectively, even though the ice itself is only at zero degrees? And why can some ice be left in the glass, even though the drink was at room temperature?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a tall glass of a cold drink stands on a table, with ice cubes and a straw floating in it. Water droplets have condensed on the outside of the glass, and a box of ice cubes stands next to the glass." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-14-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
When warm water and ice are put in an insulated container, heat is transferred from the water to the ice until the temperatures are equal and the container is in thermal equilibrium. Energy is conserved, so the quantity of heat given out by the water is equal to the quantity of heat taken in by the ice. The energy taken in by the ice does not simply raise its temperature, however: the ice first warms to $0\,{}^\circ\text{C}$ and then melts. During melting the temperature stays constant, but every kilogram of ice takes in $334\,\text{kJ}$ of energy, and the same energy would raise the temperature of a kilogram of water by almost $80\,\text{K}$.

<svg data-fig="before-after" viewBox="0 0 600 344" role="img" aria-label="Before-and-after schematic: an insulated container first holds 0.30 kg of water at 20 °C and 0.10 kg of ice at 0 °C. Heat Q is transferred from the water to the ice. At equilibrium the thermometer reads 0 °C, there is 0.375 kg of water and only 0.025 kg of ice is left. The total area of the ice cubes is drawn to scale with the mass of the ice." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-14-before-after.webp" x="0" y="0" width="600" height="355" preserveAspectRatio="none"/>
  <foreignObject x="173" y="195.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="-2" y="218" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="-2" y="178" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$10$</div></foreignObject>
  <foreignObject x="-2" y="138" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="-2" y="98" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$30$</div></foreignObject>
  <foreignObject x="8" y="59.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="53" y="8.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{initially}$</div></foreignObject>
  <foreignObject x="31" y="278.5" width="244" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{water } 0.30\,\text{kg},\ 20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="31" y="311.5" width="244" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ice } 0.10\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="320" y="217.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="330" y="59.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="375" y="8.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at equilibrium}$</div></foreignObject>
  <foreignObject x="353" y="278.5" width="244" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{water } 0.375\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="353" y="311.5" width="244" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ice } 0.025\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
</svg>

When warm water and cold ice are mixed in an insulated container, the final temperature is generally not the mean of the initial temperatures. The solution is based on conservation of energy.

```pysahdy
Why is the final temperature of warm water and ice generally not the mean of the initial temperatures?
---
The ice takes in $334\,\text{kJ}$ per kilogram when it melts without its temperature rising, so part of the heat from the water does not change any temperature.
```

## Formula: Thermal equilibrium and melting
An insulated container holds water of mass $m_\text{w}$ and temperature $T_\text{w} > 0\,{}^\circ\text{C}$, and ice of mass $m_\text{i}$ and temperature $T_\text{i} \le 0\,{}^\circ\text{C}$. The quantity of heat given out by the water as it cools to the melting point is
```latex
Q_\text{w} = c_\text{w} m_\text{w} \Delta T_\text{w}
```
Warming the ice to the melting point needs the energy
```latex
Q_\text{i,warm} = c_\text{i} m_\text{i} \Delta T_\text{i}
```
Melting all the ice needs the additional energy $s m_\text{i}$. So warming and melting the ice need altogether
```latex
Q_\text{i} = Q_\text{i,warm} + s m_\text{i}
```
where $c_\text{w}$ is the specific heat capacity of water and $c_\text{i}$ that of ice (J/(kg·K)), $\Delta T_\text{w} = T_\text{w} - 0\,{}^\circ\text{C}$ is the fall in the temperature of the water to the melting point (K), $\Delta T_\text{i} = 0\,{}^\circ\text{C} - T_\text{i}$ is the rise in the temperature of the ice to the melting point (K) and $s$ is the specific latent heat of fusion of ice (J/kg).

<svg data-fig="energy-balance" viewBox="0 0 600 392" role="img" aria-label="Energy balance bars drawn to scale, in kilojoules: 0.30 kg of water at 20 °C gives out 25.1 kJ when it cools to 0 °C. 0.10 kg of ice at −10 °C needs 2.1 kJ to warm to 0 °C and 33.4 kJ to melt, 35.5 kJ in total. The heat from the water is not enough: the pale part of the bar shows the ice that does not have time to melt." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-14-energy-balance.webp" x="0" y="0" width="600" height="397.5" preserveAspectRatio="none"/>
  <foreignObject x="36" y="317.5" width="56" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="36" y="257.5" width="56" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <foreignObject x="36" y="197.5" width="56" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="36" y="137.5" width="56" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$30$</div></foreignObject>
  <foreignObject x="36" y="77.5" width="56" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$40$</div></foreignObject>
  <foreignObject x="20" y="8.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q\ (\text{kJ})$</div></foreignObject>
  <foreignObject x="290" y="5.5" width="306" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{water } 0.30\,\text{kg},\ 20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="290" y="41.5" width="306" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ice } 0.10\,\text{kg},\ {-10}\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="472" y="135.5" width="128" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ice left over}$</div></foreignObject>
  <foreignObject x="356" y="155.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s\,m_\text{i}$</div></foreignObject>
  <foreignObject x="472" y="295" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{warming}$</div></foreignObject>
  <foreignObject x="130" y="145.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25.1\,\text{kJ}$</div></foreignObject>
  <foreignObject x="330" y="83.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$35.5\,\text{kJ}$</div></foreignObject>
  <foreignObject x="110" y="340.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{water gives out}$</div></foreignObject>
  <foreignObject x="310" y="340.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ice needs}$</div></foreignObject>
</svg>

| Quantity | Value |
| --- | --- |
| of water $c_\text{w}$ | $4190\,\text{J/(kg}\cdot\text{K)}$ |
| of ice $c_\text{i}$ | $2100\,\text{J/(kg}\cdot\text{K)}$ |
| of ice $s$ | $334\,\text{kJ/kg}$ |

The possible end states are:

1. If $Q_\text{w} > Q_\text{i}$, all the ice melts and the resulting water warms to above $0\,{}^\circ\text{C}$.
2. If $Q_\text{i,warm} \le Q_\text{w} \le Q_\text{i}$, the final temperature is $0\,{}^\circ\text{C}$. Some ice may be left, or all the ice may only just melt.
3. If $Q_\text{w} < Q_\text{i,warm}$, the water cooling to zero degrees is not enough on its own to warm all the ice to the melting point. Then part of the water may freeze and give out energy as it solidifies.
4. If even the energy released when all the water freezes is not enough to warm the ice to the melting point, the end state is ice only, at a temperature below $0\,{}^\circ\text{C}$.

So before calculating the temperature, you must work out which phases are present in the end state.

```pysahdy
$Q_\text{w}$ is smaller than $Q_\text{i}$ but at least $Q_\text{i,warm}$. What is the final temperature, and what is in the container?
---
The temperature is $0\,{}^\circ\text{C}$. Not all the ice melts, so ice and water are in the container together.
```

If $Q_\text{w} \ge Q_\text{i}$, all the ice melts. The heat given out by the water is then used to warm and melt the ice, and the rest warms the whole amount of water $m_\text{w} + m_\text{i}$ to the temperature $T$. The energy balance is
```latex
\begin{aligned}
&c_\text{w} m_\text{w} (T_\text{w} - T) \\
&\quad = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i} \\
&\qquad + c_\text{w} m_\text{i} T
\end{aligned}
```
where the left-hand side is the quantity of heat given out by the water, and on the right are the warming of the ice, the melting of the ice and the warming of the meltwater. Solved:
```latex
T = \frac{Q_\text{w} - Q_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})}
```
In the borderline case $Q_\text{w} = Q_\text{i}$ the formula gives $T = 0\,{}^\circ\text{C}$: all the ice has only just melted, but the meltwater does not warm up.

If $Q_\text{w} < Q_\text{i}$ but the water is enough to warm the ice to $0\,{}^\circ\text{C}$, not all the ice has time to melt. The container then holds ice and water at the same time, so $T = 0\,{}^\circ\text{C}$. The mass of melted ice $m_\text{melt}$ is found from the heat that is left after warming the ice:
```latex
m_\text{melt} = \frac{Q_\text{w} - c_\text{i} m_\text{i} \Delta T_\text{i}}{s}
```
The mass of ice that is left is $m_\text{i} - m_\text{melt}$. The graph shows how the final temperature depends on the initial temperature of the water when there is $0.30\,\text{kg}$ of water and $0.10\,\text{kg}$ of ice at 0 °C: until the heat given out by the water is enough to melt the ice, the temperature stays at $0\,{}^\circ\text{C}$, and after that it rises. The black dot is the glass of the first figure, where the water is at 20 °C.

<svg viewBox="0 0 600 394" role="img" aria-label="Graph of the formula: final temperature T of 0.30 kg of water and 0.10 kg of ice at 0 °C as a function of the initial temperature of the water Tv. When Tv is below 26.6 °C, some ice is left over and T is 0 °C; at the limit all the ice only just melts and T is still 0 °C. After that all the ice melts and T rises in a straight line, to 40 °C when the water starts at 80 °C. The axes are drawn to scale." style="max-width:100%;font-size:24px">
  <rect x="100" y="70" width="152.8" height="240" fill="#d0e6fb" fill-opacity="0.55"/>
  <line x1="100" y1="250.0" x2="560" y2="250.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="190.0" x2="560" y2="190.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="130.0" x2="560" y2="130.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="70.0" x2="560" y2="70.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="215.0" y1="70" x2="215.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="330.0" y1="70" x2="330.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="445.0" y1="70" x2="445.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="560.0" y1="70" x2="560.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="310" x2="570" y2="310" stroke="#1f2933" stroke-width="2.5"/><line x1="100" y1="310" x2="100" y2="60" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="72.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="187.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="302.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$40$</div></foreignObject>
  <foreignObject x="417.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$60$</div></foreignObject>
  <foreignObject x="532.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$80$</div></foreignObject>
  <foreignObject x="36" y="295.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="36" y="235.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$10$</div></foreignObject>
  <foreignObject x="36" y="175.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="36" y="115.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$30$</div></foreignObject>
  <foreignObject x="36" y="55.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$40$</div></foreignObject>
  <foreignObject x="6" y="6" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$T\ (^\circ\text{C})$</div></foreignObject>
  <foreignObject x="340" y="358" width="250" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$T_\text{w}\ (^\circ\text{C})$</div></foreignObject>
  <polyline points="100.0,310.0 252.8,310.0 560.0,69.6" fill="none" stroke="#c92a2a" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="252.8" y1="310.0" x2="252.8" y2="70" stroke="#6b7480" stroke-width="2" stroke-dasharray="6 5"/>
  <circle cx="252.8" cy="310.0" r="6.5" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="215.0" cy="310.0" r="6.5" fill="#1f2933"/>
  <foreignObject x="246.78440731901352" y="62" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$26.6\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="108" y="76" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{ice left over}$</div></foreignObject>
  <foreignObject x="108" y="110" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$T = 0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="350" y="256.0" width="220" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{all ice melts}$</div></foreignObject>
  <foreignObject x="135.0" y="260.0" width="110" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{initial glass}$</div></foreignObject>
</svg>

In case 3 the cold ice freezes some of the water. As long as some water is left, ice and water are present together and the temperature is $0\,{}^\circ\text{C}$. In case 4 all the water freezes, and the temperature of the ice is found from the same energy balance in the Level 3 exercise.

```pysahdy
In case 4 all the water freezes. Is the final temperature $0\,{}^\circ\text{C}$?
---
No. Only ice is left, and its temperature is below $0\,{}^\circ\text{C}$. The temperature is $0\,{}^\circ\text{C}$ only while ice and water are present together.
```

<figure class="unit-photo"><img src="pics/fy3/ice-water-glass.webp" alt="A glass of water seen from above. The glass holds water and many ice cubes."><figcaption>Ice cubes in a glass of water. The ice melts as heat flows into it from the surrounding water.</figcaption></figure>

## Worked example
A calorimeter contains $0.250\,\text{kg}$ of water at a temperature of $24.0\,{}^\circ\text{C}$. $0.050\,\text{kg}$ of ice at $-8.0\,{}^\circ\text{C}$ is dropped into the water. Does all the ice melt, and what is the temperature of the contents of the calorimeter at thermal equilibrium? The heat capacity of the calorimeter itself and heat losses to the surroundings are ignored.

<!-- vaihe -->

**Given and find.** Water: $m_\text{w} = 0.250\,\text{kg}$, $T_\text{w} = 24.0\,{}^\circ\text{C}$. Ice: $m_\text{i} = 0.050\,\text{kg}$, $T_\text{i} = -8.0\,{}^\circ\text{C}$. From the table, $c_\text{w} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, $c_\text{i} = 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ and $s = 334\,\tfrac{\text{kJ}}{\text{kg}}$. We are asked whether all the ice melts, and for the final temperature $T$.

<!-- vaihe -->

**Principle.** Energy is conserved, because the calorimeter takes in no heat and no heat escapes to the surroundings: the quantity of heat given out by the water is equal to the quantity of heat taken in by the ice. The ice first warms to $0\,{}^\circ\text{C}$, then melts at a constant temperature, and finally the meltwater warms to the final temperature. So we must first check whether the heat given out by the water is enough to warm and melt all the ice. If it is, the ice melts completely and the final temperature is not below $0\,{}^\circ\text{C}$.

<!-- vaihe -->

**Rearranged formula.** When the water cools to $0\,{}^\circ\text{C}$ it gives out a quantity of heat $Q_\text{w}$, and to melt, the ice needs a quantity of heat $Q_\text{i}$. When $Q_\text{w} > Q_\text{i}$, the surplus warms all the water ($m_\text{w} + m_\text{i}$) to the temperature $T$:
```latex
\begin{aligned}
&Q_\text{w} = c_\text{w} m_\text{w} \Delta T_\text{w} \\
&Q_\text{i} = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i} \\[6pt]
&T = \frac{Q_\text{w} - Q_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The masses are already in kilograms. A temperature change is the same in kelvins and in degrees Celsius: the water cools by $\Delta T_\text{w} = 24.0\,{}^\circ\text{C} - 0\,{}^\circ\text{C} = 24.0\,\text{K}$ and the ice warms by $\Delta T_\text{i} = 0\,{}^\circ\text{C} - (-8.0\,{}^\circ\text{C}) = 8.0\,\text{K}$. The latent heat of fusion is $334\,\tfrac{\text{kJ}}{\text{kg}} = 334\,000\,\tfrac{\text{J}}{\text{kg}}$.

<!-- vaihe -->

**Substitution.** We calculate the quantities of heat separately and then the temperature:
```latex
\begin{aligned}
&Q_\text{w} = c_\text{w} m_\text{w} \Delta T_\text{w} \\
&= 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.250\,\text{kg} \cdot 24.0\,\text{K} \\
&= 25\,140\,\text{J} \\[6pt]
&Q_\text{i} = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i} \\
&= 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.050\,\text{kg} \cdot 8.0\,\text{K} \\
&\quad + 334\,000\,\tfrac{\text{J}}{\text{kg}} \cdot 0.050\,\text{kg} \\
&= 840\,\text{J} + 16\,700\,\text{J} \\
&= 17\,540\,\text{J} \\[6pt]
&T = \frac{Q_\text{w} - Q_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})} \\
&= \frac{25\,140\,\text{J} - 17\,540\,\text{J}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.300\,\text{kg}} \\
&= \frac{7600\,\text{J}}{1257\,\tfrac{\text{J}}{\text{K}}} \\
&= 6.05\,{}^\circ\text{C}
\end{aligned}
```

<!-- vaihe -->

**Result.** Because $Q_\text{w} = 25\,140\,\text{J} > Q_\text{i} = 17\,540\,\text{J}$, all the ice melts. The final state is $0.300\,\text{kg}$ of water at a temperature of $6.0\,{}^\circ\text{C}$. The answer is given to two significant figures, because the mass of the ice, $0.050\,\text{kg}$, is known only to two figures and it determines the precision of the quantity of heat $Q_\text{i} = 17\,540\,\text{J}$ (hundreds of joules); the difference $Q_\text{w} - Q_\text{i} = 7600\,\text{J}$ is therefore a two-figure number.

<!-- vaihe -->

**Reasonableness.** The result lies between the initial temperatures $-8.0\,{}^\circ\text{C}$ and $24.0\,{}^\circ\text{C}$, but below $8.0\,{}^\circ\text{C}$, the midpoint of the two, even though there is five times as much water: the melting of the ice pulls the result down. If the latent heat were forgotten, the result would be about $19\,{}^\circ\text{C}$, so melting takes two thirds of the heat given out by the water ($16.7\,\text{kJ}$ of $25.1\,\text{kJ}$). The energy balance checks out: the water gives out a total of $$\begin{aligned} &4190 \cdot 0.250 \cdot (24.0 - 6.05) \\ &\approx 18.8\,\text{kJ} \end{aligned}$$ and the ice takes in $$\begin{aligned} &840 + 16\,700 + 4190 \cdot 0.050 \cdot 6.05 \\ &\approx 18.8\,\text{kJ} \end{aligned}$$. Try the same values in the simulation.

## Common misconception
Many people calculate the final temperature as if the ice were just cold water, which forgets the latent heat of fusion. When $0.30\,\text{kg}$ of water ($20\,{}^\circ\text{C}$) and $0.10\,\text{kg}$ of ice ($0\,{}^\circ\text{C}$) are mixed, this method would give
```latex
\begin{aligned}
T &= \frac{c_\text{w} m_\text{w} T_\text{w} + c_\text{w} m_\text{i} T_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})} \\
&= \frac{0.30\,\text{kg} \cdot 20\,{}^\circ\text{C}}{0.40\,\text{kg}} \\
&= 15\,{}^\circ\text{C}
\end{aligned}
```
In reality, melting all the ice would need $33.4\,\text{kJ}$, but the water can give out only $25.1\,\text{kJ}$ as it cools. So the final state is $0\,{}^\circ\text{C}$, and $24.7\,\text{g}$ of ice is left over. Another mistake is to put the temperature below $0\,{}^\circ\text{C}$ when the container still holds ice and water: as long as both are present, the temperature is $0\,{}^\circ\text{C}$. If your calculation gives a temperature below $0\,{}^\circ\text{C}$ with a formula that assumes all the ice melts, the assumption is wrong: some ice is left, and the temperature is $0\,{}^\circ\text{C}$. The exception is very cold ice that freezes all the water: then the container holds only ice, and its temperature is below $0\,{}^\circ\text{C}$.

## Summary
- In an insulated container, the quantity of heat given out by the water is equal to the quantity of heat taken in by the ice. The ice first warms to $0\,{}^\circ\text{C}$ and then melts; during melting the temperature does not change.
- First compare the quantities of heat $Q_\text{w} = c_\text{w} m_\text{w} \Delta T_\text{w}$ and $Q_\text{i} = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i}$. If $Q_\text{w} \ge Q_\text{i}$, all the ice melts and $T = \tfrac{Q_\text{w} - Q_\text{i}}{c_\text{w}(m_\text{w} + m_\text{i})}$; in the borderline case $Q_\text{w} = Q_\text{i}$ the temperature is exactly $0\,{}^\circ\text{C}$.
- If $Q_\text{w} < Q_\text{i}$, some ice is left and the temperature is $0\,{}^\circ\text{C}$. The mass of melted ice is $m_\text{melt} = \tfrac{Q_\text{w} - c_\text{i} m_\text{i} \Delta T_\text{i}}{s}$. Exception: if the ice is so cold that all the water freezes, the temperature is below $0\,{}^\circ\text{C}$.
- The specific latent heat of fusion of water is $334\,\text{kJ/kg}$: melting one kilogram of ice needs the same energy as warming a kilogram of water by almost $80\,\text{K}$.
- The final temperature is not the mean of the initial temperatures, and when ice and water are together in the same container in equilibrium at normal pressure, the temperature is $0\,{}^\circ\text{C}$.
