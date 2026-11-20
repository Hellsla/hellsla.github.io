# Pressure and hydrostatic pressure

> **Why** is the wall of a dam much thicker at the bottom than at the top, even though the water pressing on it is the same water all the way down?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a concrete dam in a mountain valley seen from the side. Behind the dam is a deep reservoir whose water gets darker with depth. The dam is narrow at the top and widens downwards; at the bottom it is many times thicker." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
When a force is spread over a surface, its effect depends on how large an area it is spread over. The sharp tip of a drawing pin sinks into a wall with the same force that leaves no mark when applied to the blunt head, and skis carry you on deep snow although boots sink in. The quantity that describes this is pressure: force divided by the area over which the force is spread. The unit of pressure is the pascal (Pa), and $1\,\text{Pa} = 1\,\text{N/m}^2$. The pascal is a small unit, so in everyday life we use the kilopascal: $1\,\text{kPa} = 1000\,\text{Pa}$.

```pysahdy
A force of $60\,\text{N}$ acts on an area of $2.0\,\text{cm}^2$. What is the pressure?
---
$p = \dfrac{F}{A}$, so $p = \dfrac{60\,\text{N}}{2.0 \cdot 10^{-4}\,\text{m}^2}$. That is $3.0 \cdot 10^{5}\,\text{Pa} = 300\,\text{kPa}$.
```

<svg data-fig="pressure-area" viewBox="0 0 600 380" role="img" aria-label="The same force F acts on an identical brick in two ways. On the left the brick stands on end and touches the ground with a small area A1, so the pressure p1 = F/A1 is large. On the right the brick lies on its side and touches the ground with an area three times as large, A2 = 3 A1, so the pressure p2 = F/A2 is one third of the pressure on the left. The force arrows are equally long. The contact areas are to scale; the diagram is otherwise schematic." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-pressure-area.webp" x="0" y="0" width="600" height="387.5" preserveAspectRatio="none"/>
  <foreignObject x="115" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{on end}$</div></foreignObject>
  <foreignObject x="164" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="133.5" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_1$</div></foreignObject>
  <foreignObject x="115" y="317" width="70" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_1 = \dfrac{F}{A_1}$</div></foreignObject>
  <foreignObject x="390" y="9.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{on its side}$</div></foreignObject>
  <foreignObject x="464" y="151.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="408.5" y="285.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_2 = 3A_1$</div></foreignObject>
  <foreignObject x="415" y="317" width="70" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_2 = \dfrac{F}{A_2}$</div></foreignObject>
</svg>

### Where does pressure come from?
According to the micro model, the pressure of a gas comes from particles colliding with the walls of the container. The pressure of a liquid comes from the weight of the liquid itself: above every layer of water there is more water pressing down on it. The deeper you go, the more water there is above you and the greater the pressure. In a liquid at rest, a horizontal surface of area $A$ below the surface carries the weight of the column of water above it. The height of the column is the depth $h$ and its volume is $V = Ah$. Density $\rho$ is mass per volume ($m = \rho V$), so the mass of the column is $\rho A h$ and its weight is $G = mg = \rho A h g$. Pressure is weight divided by area, so the area cancels and what is left is $\rho g h$. The pressure produced by the weight of a liquid is called hydrostatic pressure. It does not depend on the shape of the container or on the total amount of water, only on the depth and the density of the liquid.

<svg data-fig="water-column" viewBox="0 0 600 300" role="img" aria-label="A column of water whose base has area A and whose height is the depth h. The weight of the column, G = ρAhg, presses the base downwards, and the pressure is the weight divided by the area, p = G/A = ρgh: the area cancels. Schematic diagram, not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-water-column.webp" x="2.6" y="2.6" width="615.4" height="316.7" preserveAspectRatio="none"/>
  <foreignObject x="44" y="19.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{water surface}$</div></foreignObject>
  <foreignObject x="136" y="117" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px;color:#c92a2a">$G$</div></foreignObject>
  <foreignObject x="198" y="234" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$A$</div></foreignObject>
  <foreignObject x="290" y="117" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$h$</div></foreignObject>
  <foreignObject x="392" y="25.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{column's weight}$</div></foreignObject>
  <foreignObject x="392" y="59" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$G = \rho A h g$</div></foreignObject>
  <foreignObject x="392" y="115.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{bottom pressure}$</div></foreignObject>
  <foreignObject x="392" y="154.5" width="110" height="67" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$p = \dfrac{G}{A} = \rho g h$</div></foreignObject>
</svg>

Pressure is not a force but the ratio of force to area, and in a liquid at rest the pressure acts equally in every direction. If the pressure sideways were smaller than downwards, the water would flow sideways and would not stay at rest. If you make holes at several heights in the side of a bottle, the water squirts out hardest from the lowest hole, because the pressure grows with depth. The force caused by pressure is always perpendicular to the surface: on the vertical wall of a dam the force points horizontally, and on a diver's body it acts from all sides. That is why here we can treat the force as just a magnitude; the direction comes from the surface.

```pysahdy
Why is the pressure sideways in a liquid at rest equal to the pressure downwards?
---
If the pressure sideways were smaller, the liquid would flow sideways and would not stay at rest.
```

<figure class="unit-photo"><img src="pics/fy3/scuba-diver.webp" alt="A diver in dark blue water, with air bubbles rising above towards the bright surface."><figcaption>A diver deep under water. The bubbles of exhaled air rise towards the surface.</figcaption></figure>

### Atmospheric pressure and gauge pressure
Atmospheric pressure, the pressure of the atmosphere, already acts on the surface of the water. At sea level it is about $101\,\text{kPa}$. It is the weight of the column of air per unit area. Atmospheric pressure also acts on the surface of the water and is transmitted through the water to depth. Under water the total pressure is therefore the sum of atmospheric pressure and hydrostatic pressure. At a depth of ten metres the hydrostatic pressure is already about the same as one atmosphere.

This answers the opening question. Atmospheric pressure acts on both sides of the dam wall, so the wall is loaded only by the gauge pressure of the water, that is, the part of the pressure that is greater than atmospheric pressure. The gauge pressure is zero at the top and grows steadily with depth: at a depth of 30 metres it is about $290\,\text{kPa}$, so every square metre of the wall feels a force of about $290\,\text{kN}$. The lower part of the wall must therefore withstand a much greater force than the upper part, and the wall is built thick at the bottom.

```pysahdy
Why does only the gauge pressure of the water load the dam wall, not the total pressure?
---
Atmospheric pressure acts on the wall from both sides and cancels, so only the gauge pressure $\rho g h$ of the water is left.
```

## Formula: Pressure and hydrostatic pressure
Pressure is the force perpendicular to a surface divided by the area:
```kaavat
pressure caused by a force :: p = \frac{F}{A}
```
where $p$ is the pressure (Pa), $F$ the force perpendicular to the surface (N) and $A$ the area (m²). One pascal is a force of one newton on an area of one square metre: $1\,\text{Pa} = 1\,\text{N/m}^2$.

In a liquid at depth $h$ the pressure is
```kaavat
hydrostatic pressure :: p = p_0 + \rho g h
```
where $p_0$ is the pressure at the surface of the liquid, usually atmospheric pressure (Pa), $\rho$ the density of the liquid (kg/m³), $g$ = $9.81\,\text{m/s}^2$ and $h$ the depth below the surface (m). The term $\rho g h$ is the hydrostatic pressure, that is, the gauge pressure $\Delta p = p - p_0$, which tells how much greater the pressure is than the pressure at the surface. The graph $(h, p)$ is a straight line whose slope is $\rho g$ and whose constant term is $p_0$, as in the linear model $y = kx + b$ of FY1. For water $\rho$ = $1000\,\text{kg/m}^3$, so the pressure grows by $9.81\,\text{kPa}$ for every metre.

<svg data-fig="pressure-depth" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the pressure p of water in kilopascals as a function of the depth h for h from 0 to 10 m. The pressure is a rising straight line: at the surface the pressure is atmospheric pressure, 101 kPa, and at a depth of 10 metres about 199 kPa. The gap between the line and the dashed line is the hydrostatic pressure ρgh." style="max-width:100%;font-size:24px">
  <line x1="173" y1="285" x2="173" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="242.5" y1="285" x2="242.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="311.5" y1="285" x2="311.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="381" y1="285" x2="381" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="450" y1="285" x2="450" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="240" x2="450" y2="240" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="195.5" x2="450" y2="195.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="150.5" x2="450" y2="150.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="106" x2="450" y2="106" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="103" y1="285" x2="464" y2="285" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476,285 L463,291 L463,279 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="104" y1="286" x2="104" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M104,44 L110,57 L98,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="173" y1="285" x2="173" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="163" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="242.5" y1="285" x2="242.5" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="232.5" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="311.5" y1="285" x2="311.5" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="301.5" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="381" y1="285" x2="381" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="371" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="450" y1="285" x2="450" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="433.5" y="294.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="97" y1="240" x2="104" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="59" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="97" y1="195.5" x2="104" y2="195.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="181" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="97" y1="150.5" x2="104" y2="150.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="136" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="97" y1="106" x2="104" y2="106" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="91.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="74" y="290.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="482" y="270.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h\ (\text{m})$</div></foreignObject>
  <foreignObject x="94" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="104,194.5 450,106.5" fill="none" stroke="#2f74b5" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="104,194.5 450,194.5" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="104" cy="194.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="450" cy="106.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="116" y="210" width="274" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{air pressure}\ p_0 = 101\,\text{kPa}$</span></div></foreignObject>
  <foreignObject x="283" y="71.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2f74b5">$p = p_0 + \rho g h$</div></foreignObject>
  <path d="M466.0,106.6 H472.0 V194.5 H466.0" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="482" y="136" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\rho g h$</div></foreignObject>
</svg>

## Worked example
A diver is in a lake at a depth of $12.0\,\text{m}$, next to the window of an underwater observation room. Atmospheric pressure at the surface is $101\,\text{kPa}$ and the density of water is $1000\,\text{kg/m}^3$. What is the pressure around the diver, and how large is the force on a window of area $150\,\text{cm}^2$ when the room contains air at normal pressure?

<!-- vaihe -->

**Given and find.** Depth $h = 12.0\,\text{m}$, atmospheric pressure $p_0 = 101\,\text{kPa}$, the density of water from a table or from the problem $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$ and window area $A = 150\,\text{cm}^2$.

We want the total pressure $p$ around the diver and the force $F$ on the window.

<!-- vaihe -->

**Principle.** The water is at rest and its density is constant, so the pressure grows steadily with depth: the total pressure is the atmospheric pressure at the surface plus the hydrostatic pressure of the water $\rho g h$. Only the gauge pressure $\rho g h$ acts on the window, because the atmospheric pressure in the room pushes the window from inside just as much as the atmospheric pressure at the surface pushes from outside. The force is pressure times area, because pressure is force per unit area.

<!-- vaihe -->

**Rearranged formula.** Both unknowns are already alone on the left-hand side:
```latex
\begin{aligned}
p &= p_0 + \rho g h \\
F &= \rho g h \cdot A
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Atmospheric pressure in pascals is $101\,\text{kPa} = 101\,000\,\text{Pa}$. The area of the window in square metres is $150\,\text{cm}^2 = 150 \cdot 10^{-4}\,\text{m}^2 = 0.015\,\text{m}^2$, because $1\,\text{cm}^2 = 10^{-4}\,\text{m}^2$. The other quantities are already in SI units.

<!-- vaihe -->

**Substitution.** We calculate the hydrostatic pressure, the total pressure and the force one after another:
```latex
\begin{aligned}
&\rho g h \\
&= 1000\,\tfrac{\text{kg}}{\text{m}^3} \\
&\quad \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \\
&\quad \cdot 12.0\,\text{m} \\
&= 117\,720\,\text{Pa} \\[6pt]
&p = p_0 + \rho g h \\
&= 101\,000\,\text{Pa} \\
&\quad + 117\,720\,\text{Pa} \\
&= 218\,720\,\text{Pa} \\[6pt]
&F = \rho g h \cdot A \\
&= 117\,720\,\text{Pa} \\
&\quad \cdot 0.015\,\text{m}^2 \\
&= 1765.8\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** The total pressure is $p \approx 219\,\text{kPa}$ and the force on the window is $F \approx 1.77\,\text{kN}$. Both the pressure and the force are given with three significant figures, because the depth $12.0\,\text{m}$, the atmospheric pressure $101\,\text{kPa}$ and the area $150\,\text{cm}^2$ are given with three figures.

<!-- vaihe -->

**Reasonableness.** The total pressure is about 2.2 times atmospheric pressure, which fits the fact that 10 metres of water add about one atmosphere and 12 metres add a little more.

Estimate: $10\,\text{kPa/m} \cdot 12\,\text{m} + 101\,\text{kPa} \approx 220\,\text{kPa}$. The force equals the weight of a mass of about $180\,\text{kg}$, although the window is small.

The pressure does not crush the diver's body, because in water the same pressure acts on the body from all sides and the body fluids transmit it to the inside as well. Only the pressure in the body's air spaces, such as the ears, has to be equalised.

## Common misconception
Many people think that the pressure at the bottom depends on how much water the container holds. In a narrow tube and a wide pool, where the water reaches the same height, the pressure at the bottom is the same, even though the pool holds a thousand times as much water. Pressure depends only on the depth, the density and the pressure at the surface. Another mistake is to confuse pressure and force: the sharp tip of a drawing pin does not produce a greater force than the head, but spreads the same force over a smaller area, so the pressure is greater. A third mistake is to forget atmospheric pressure: $\rho g h$ alone gives only the gauge pressure, and the total pressure under water is always greater than that.

## Summary
- Pressure is force per unit area: $p = F/A$. The unit is the pascal, $1\,\text{Pa} = 1\,\text{N/m}^2$, and $1\,\text{kPa} = 1000\,\text{Pa}$.
- In a liquid the pressure grows with depth: $p = p_0 + \rho g h$. The term $\rho g h$ is the hydrostatic pressure, and it depends only on the depth and the density, not on the shape of the container.
- The force caused by pressure is perpendicular to the surface and acts in every direction in a liquid.
- Atmospheric pressure at sea level is about $101\,\text{kPa}$. In water the pressure grows by about one atmosphere for every ten metres.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a diver deep in a lake. The water gets darker with depth, air bubbles rise to the surface, and the diver wears a depth and pressure gauge on the wrist." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
