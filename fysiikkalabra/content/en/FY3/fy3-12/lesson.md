# Heat transfer, energy balance and climate change

> **Why** is the mean temperature of the Earth about $+15\,{}^\circ\text{C}$ and not below freezing, even though the Earth radiates as much energy into space as it absorbs from the Sun?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the Earth seen from space, with a thin atmosphere around it. The Sun shines at the left edge of the picture, and stars twinkle in the black sky." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
Because of a temperature difference, energy transfers by itself, as a net amount, from a warmer object to a colder one. Energy that transfers in this way is called heat, and it transfers in three ways. In conduction, energy passes through matter from one particle to the next, as faster vibrating particles nudge their slower neighbours. Metals conduct heat well, because in them free electrons also carry energy, and they carry most of it; air and wool conduct it poorly. In convection, a warm liquid or gas flows and carries energy with it: warm air rises above a radiator, because it has expanded and is lighter than the surrounding air.

In thermal radiation, an object emits electromagnetic radiation, which needs no medium. This is how the Sun's energy reaches the Earth through empty space, and how the glow of a fireplace warms your face. All objects radiate, and the hotter an object is, the more radiation it emits and the shorter the wavelengths of that radiation are. Thermal radiation therefore leaves both objects, so the colder object also radiates towards the warmer one. The warmer one radiates more, however, so the net transfer of energy is to the colder object.

<svg data-fig="heat-transfer" viewBox="0 0 600 300" role="img" aria-label="The three ways of heat transfer, schematic diagram. Conduction: heat travels through a metal rod from the hot end to the cold end. Convection: warm water rises in the middle of a pot and cooled water sinks at the edges, so the water circulates. Radiation: a hot object emits radiation, which travels through empty space." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-heat-transfer.webp" x="6.2" y="7.4" width="594.1" height="308.2" preserveAspectRatio="none"/>
  <foreignObject x="14" y="177.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hot}$</div></foreignObject>
  <foreignObject x="128" y="177.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{cold}$</div></foreignObject>
  <foreignObject x="33.5" y="247.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{conduction}$</div></foreignObject>
  <foreignObject x="233.5" y="247.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{convection}$</div></foreignObject>
  <foreignObject x="440" y="247.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{radiation}$</div></foreignObject>
</svg>

```pysahdy
The Sun's energy reaches the Earth through empty space. Which way of heat transfer is it, and why is it neither conduction nor convection?
---
It is thermal radiation. Radiation needs no medium, but conduction and convection need matter for the energy to pass through.
```

### Heat losses of a building
A large part of the heating energy of a house is used because heat is conducted out through the walls, roof, windows and floor. The heat insulation of a building part is described by its U-value, or thermal transmittance, which tells you how many watts of thermal power pass through one square metre when the difference between the indoor and outdoor temperature is one kelvin. The smaller the U-value, the better the structure insulates. The U-value of a modern wall is about $0.17\,\text{W/(m}^2\text{}\cdot\text{K)}$, but even a good window has about $1.0\,\text{W/(m}^2\text{}\cdot\text{K)}$, so a small window lets through as much heat as many times its area of wall. Good insulation saves energy and reduces the emissions from heating.

```pysahdy
The U-value of a wall is $0.17\,\text{W/(m}^2\text{}\cdot\text{K)}$ and that of a window $1.0\,\text{W/(m}^2\text{}\cdot\text{K)}$. Which one insulates better, and why?
---
The wall, because its U-value is smaller. Less thermal power passes through it with the same area and temperature difference.
```

### Energy balance
The temperature of an object stays constant when the power coming into it is equal to the power leaving it. This is called energy balance. The Earth receives energy as radiation from the Sun, and about $30\,\%$ of it is reflected straight back into space by clouds, ice and light surfaces. The rest is absorbed, and the Earth radiates the same power away as long-wavelength thermal radiation. Without an atmosphere, the balance would settle at a mean temperature of about $-18\,{}^\circ\text{C}$.

### Greenhouse effect
Water vapour, carbon dioxide and methane in the atmosphere let sunlight mostly through, although about a fifth of it is absorbed in the atmosphere. They absorb the thermal radiation emitted by the ground and radiate part of it back down. The ground therefore receives more energy than from the Sun alone, and the balance settles at about $+15\,{}^\circ\text{C}$. This is called the greenhouse effect, and it answers the question at the start.

<svg data-fig="energy-balance" viewBox="0 0 600 340" role="img" aria-label="Energy balance of the Earth, schematic diagram. Radiation from the Sun passes through the atmosphere to the ground; part of it is reflected back into space. The ground radiates thermal radiation upwards, and the greenhouse gases of the atmosphere radiate part of it back down." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-energy-balance.webp" x="-2.5" y="-2.5" width="603" height="353" preserveAspectRatio="none"/>
  <foreignObject x="230" y="289.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ground}$</div></foreignObject>
  <foreignObject x="24" y="231.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{atmosphere}$</div></foreignObject>
  <foreignObject x="122" y="35.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Sun}$</div></foreignObject>
  <foreignObject x="302" y="37.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{reflected}$</div></foreignObject>
  <foreignObject x="370" y="235.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{heat radiation}$</div></foreignObject>
  <foreignObject x="427.5" y="63.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{CO}_2$</div></foreignObject>
  <foreignObject x="396" y="177.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{back}$</div></foreignObject>
</svg>

```pysahdy
Greenhouse gases let sunlight mostly through. Why do they still raise the temperature of the ground?
---
They absorb the thermal radiation emitted by the ground and radiate part of it back down. The ground therefore receives more energy than from the Sun alone.
```

### Climate change
Human activity, mainly the use of fossil fuels, has raised the carbon dioxide concentration of the atmosphere from about 280 parts per million to over 420 parts per million. When greenhouse gases are added, for a while less energy escapes into space than arrives from the Sun. Today the difference is about $1\,\text{W}$ for every square metre of the Earth. The extra energy warms the oceans, the land and the air until a new balance settles at a higher temperature. This is called climate change. A power difference that looks small is huge over the whole area of the Earth, and most of it is stored in the oceans, whose large heat capacity slows the warming down but also keeps it going for a long time. Energy choices such as insulation, heat pumps and zero-emission power plants are therefore also ethical choices that affect future generations.

## Formula: Thermal power and U-value
The thermal power transferred through a building part is
```latex
P = U A \Delta T
```
where $P$ is the thermal power (W), $U$ is the U-value of the building part (W/(m²·K)), $A$ is the area (m²) and $\Delta T$ is the difference between the indoor and outdoor temperature (K). The formula holds when the temperatures on both sides of the building part stay constant. In energy balance the power coming into an object and the power leaving it are equal, and the temperature stays constant.

<svg data-fig="wall-temperature" viewBox="0 0 600 300" role="img" aria-label="Cross-section of a wall and the course of the temperature, schematic diagram. The wall has a thin inner board, a thick layer of insulation and a thin outer cladding. The temperature falls from 21 degrees indoors to minus 15 degrees outdoors, that is, by 36 kelvins, and most of the fall happens in the insulation. The thermal power P passes through the wall from the inside to the outside." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-wall-temperature.webp" x="0" y="3.8" width="615.4" height="315.4" preserveAspectRatio="none"/>
  <foreignObject x="269.5" y="85.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{insulation}$</div></foreignObject>
  <foreignObject x="101" y="25.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$21\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="82.5" y="85.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{indoors}$</div></foreignObject>
  <foreignObject x="465" y="181.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-15\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="446" y="135.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{outdoors}$</div></foreignObject>
  <foreignObject x="36" y="128.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta T = 36\,\text{K}$</div></foreignObject>
  <foreignObject x="484" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$P$</div></foreignObject>
</svg>


## Worked example
The walls of a detached house have an area of $120\,\text{m}^2$ and a U-value of $0.17\,\text{W/(m}^2\text{}\cdot\text{K)}$, and the windows have an area of $20.0\,\text{m}^2$ and a U-value of $1.0\,\text{W/(m}^2\text{}\cdot\text{K)}$. It is $21\,{}^\circ\text{C}$ indoors and $-15\,{}^\circ\text{C}$ outdoors. How large is the thermal power conducted through the walls and windows, and how much energy does it transfer in one day?

<!-- vaihe -->

**Given and find.** Walls: $A_\text{s} = 120\,\text{m}^2$, $U_\text{s} = 0.17\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$. Windows: $A_\text{i} = 20.0\,\text{m}^2$, $U_\text{i} = 1.0\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$. Temperatures $T_\text{in} = 21\,{}^\circ\text{C}$ and $T_\text{out} = -15\,{}^\circ\text{C}$.

You are asked for the thermal power $P$ and the energy $E$ in one day.

<!-- vaihe -->

**Principle.** Heat is conducted through a structure from warm to cold, and when the temperatures stay constant, the power is proportional to the area and the temperature difference: $P = UA\Delta T$. The walls and windows conduct heat in parallel, so their powers are added. The power is constant, so the energy is the power multiplied by the time.

<!-- vaihe -->

**Rearranged formula.** First solve the power and then the energy:
```latex
\begin{aligned}
&P = (U_\text{s} A_\text{s} \\
&\quad + U_\text{i} A_\text{i})\,\Delta T \\[6pt]
&E = Pt
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The temperature difference is the same in kelvins and in degrees Celsius: $\Delta T = 21\,{}^\circ\text{C} - (-15\,{}^\circ\text{C}) = 36\,\text{K}$. The time is $t = 24\,\text{h}$, and the power is converted to kilowatts so that the energy comes out in kilowatt-hours.

<!-- vaihe -->

**Substitution.** Calculate the power and then the energy:
```latex
\begin{aligned}
&P = (0.17 \cdot 120 \\
&\quad + 1.0 \cdot 20.0)\,\tfrac{\text{W}}{\text{K}} \cdot 36\,\text{K} \\
&= (20.4 + 20.0)\,\tfrac{\text{W}}{\text{K}} \cdot 36\,\text{K} \\
&= 1454.4\,\text{W} \\
&E = 1.4544\,\text{kW} \cdot 24\,\text{h} \\
&= 34.9\,\text{kWh}
\end{aligned}
```

<!-- vaihe -->

**Result.** The power conducted through the walls and windows is $P \approx 1.5\,\text{kW}$, and in one day it transfers the energy $E \approx 35\,\text{kWh}$. The result is given to two significant figures.

The limiting data are the U-values $0.17$ and $1.0$ and the temperature difference $36\,\text{K}$ (a difference of whole degrees), all with two figures; the areas $120\,\text{m}^2$ and $20.0\,\text{m}^2$ are more precise.

<!-- vaihe -->

**Reasonableness.** The area of the windows is only a sixth of the area of the walls, but the same amount of heat goes through them ($20.0\,\text{W/K}$ and $20.4\,\text{W/K}$), because their U-value is almost six times as large.

With rounded numbers, $40\,\text{W/K} \cdot 36\,\text{K} \approx 1.4\,\text{kW}$ and $1.4\,\text{kW} \cdot 24\,\text{h} \approx 34\,\text{kWh}$. The heating of the house replaces this power, and the roof, floor and ventilation add to the need.

## Common misconception
Many people mix up the greenhouse effect and ozone depletion, although they are different things: ozone depletion lets more ultraviolet radiation through, but it hardly warms the Earth. Another mistake is to think that the greenhouse effect is entirely harmful. The natural greenhouse effect keeps the Earth habitable, and the problem is its strengthening because of human emissions. A third mistake is to believe that a woollen sweater produces heat. It only slows down the conduction and convection of heat away from the body, just as the insulation in a wall slows down the escape of heat from a house.

## Summary
- Heat transfers by conduction, convection and thermal radiation, and because of a temperature difference the net transfer of energy is from the warmer object to the colder one. All objects emit thermal radiation, the colder one too.
- The thermal power transferred through a building part is $P = UA\Delta T$. A small U-value means good heat insulation.
- In energy balance the power coming in and the power going out are equal, and the temperature stays constant.
- Greenhouse gases absorb the thermal radiation of the ground and radiate part of it back, which raises the equilibrium temperature of the ground from about $-18\,{}^\circ\text{C}$ to about $+15\,{}^\circ\text{C}$.
- An increase in greenhouse gases breaks the balance for a while, and the Earth warms until a new balance settles at a higher temperature.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a detached house on a winter night. Heat escapes outwards through the windows and the roof, shown by orange arrows. There is snow on the ground." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
