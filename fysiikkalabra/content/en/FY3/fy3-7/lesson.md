# Changes of state

> **Why** does the temperature of water boiling at normal atmospheric pressure stay at about $100\,{}^\circ\text{C}$, even though energy keeps flowing into the pan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a pan on a kitchen hob with water boiling vigorously. The hotplate glows red and energy keeps flowing from it into the pan. There are bubbles in the water and steam rises from it. The column of a thermometer dipped in the water stays at the same height." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
Matter exists in three states: solid, liquid and gas. In the micro model, the particles of a solid vibrate in place, held together by each other. In a liquid, they move past each other but stay together. In a gas, they move freely and only rarely collide. In a change of state, the interactions between the particles change: in melting, the regular order of the solid breaks down, and in vaporisation, the particles move far apart from each other. The particles themselves do not change: when ice melts or water boils, the chemical bonds inside the water molecules do not break. The opposite changes are freezing and condensation. Ice can also sublimate straight into vapour, as in laundry drying in freezing weather.

<svg data-fig="micro-model" viewBox="0 0 600 306" role="img" aria-label="Micro model, schematic diagram: in a solid the particles are bound to each other in a regular arrangement, in a liquid they are disordered but still in contact, and in a gas they are far apart and move freely. Arrows: the solid melts into a liquid, the liquid vaporises into a gas." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-7-micro-model.webp" x="1.2" y="0" width="597" height="317.2" preserveAspectRatio="none"/>
  <foreignObject x="163" y="47.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{melts}$</div></foreignObject>
  <foreignObject x="343" y="47.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vaporises}$</div></foreignObject>
  <foreignObject x="60" y="259.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{solid}$</div></foreignObject>
  <foreignObject x="258.5" y="259.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liquid}$</div></foreignObject>
  <foreignObject x="482.5" y="259.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy3/la-palma-eruption.webp" alt="A volcanic eruption at night: a glowing fountain of lava and lava flows running down the slope under red smoke. Village lights show below."><figcaption>The eruption on La Palma in 2021. Lava that flowed onto the surface cools and solidifies.</figcaption></figure>

### Where does the energy go?
Melting and vaporisation need energy but do not raise the temperature. When ice is heated, its temperature rises up to $0\,{}^\circ\text{C}$. Then the temperature stays constant until all the ice has melted, even though energy keeps being transferred. During melting and vaporisation, the energy transferred to the substance changes the interactions between the particles and increases the interaction energy between them. When a pure substance changes state at constant pressure, its temperature stays constant, so the average kinetic energy of the particles does not increase.

<figure class="unit-photo"><img src="pics/fy3/melting-ice.webp" alt="Translucent, partly melted pieces of ice photographed close up."><figcaption>Melting ice photographed close up. Melting ice takes energy.</figcaption></figure>

For the same reason, boiling water stays at $100\,{}^\circ\text{C}$ even when the hob is on full: the energy transferred vaporises water and does not raise its temperature. Steam takes up about 1700 times as much space as water, so as it expands it pushes the surrounding air. A small part of the energy needed for vaporisation is used for this work, and most of it increases the interaction energy between the molecules. The greater the power, the faster the water boils away, but it does not get any hotter. The energy that was taken up when the water vaporised is released again when the vapour condenses, and that is why 100-degree steam burns worse than 100-degree water.

```pysahdy
Water is boiling in a pot. The hob is turned to a higher power. What happens to the temperature of the water?
---
The temperature does not change but stays at about $100\,{}^\circ\text{C}$. A higher power vaporises the water faster.
```

The quantity of heat needed for melting and vaporisation is directly proportional to the mass. The coefficients are properties of the substance: the specific latent heat of fusion $s$ tells you how much energy it takes to melt one kilogram, and the specific latent heat of vaporisation $r$ how much it takes to vaporise one kilogram. For water, $s = 334\,\text{kJ/kg}$ and $r = 2260\,\text{kJ/kg}$. So vaporising takes almost seven times as much energy as melting, and more than five times as much as heating water from $0\,{}^\circ\text{C}$ to $100\,{}^\circ\text{C}$.

```pysahdy
The specific latent heat of fusion of water is $s = 334\,\text{kJ/kg}$. How much energy is needed to melt $0.50\,\text{kg}$ of ice?
---
The energy is directly proportional to the mass, so $0.50\,\text{kg} \cdot 334\,\text{kJ/kg} = 167\,\text{kJ}$ is needed.
```

The boiling point depends on pressure. A phase diagram shows the state of a substance at each temperature and pressure: its curves join the melting, boiling and sublimation points at different pressures. On a mountain, where the atmospheric pressure is lower, water boils below $100\,{}^\circ\text{C}$, and in a pressure cooker the pressure raises the boiling point above $100\,{}^\circ\text{C}$, so food cooks faster.

<svg data-fig="phase-diagram" viewBox="0 0 600 350" role="img" aria-label="Phase diagram, schematic diagram: pressure p as a function of temperature T. The curves separate the solid, liquid and gas regions and meet at the triple point. At atmospheric pressure, water boils at 100 degrees; on a mountain the pressure is lower and the boiling point is lower." style="max-width:100%;font-size:24px">
  <line x1="95" y1="296" x2="490" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,296 L489,302 L489,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="297" x2="96" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,30 L102,43 L90,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="508" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="86" y="-0.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p$</div></foreignObject>
  <polygon points="96,296 100,296 103.5,296 107.5,296 111,295.5 115,295.5 119,295 122.5,295 126.5,294.5 130,294 134,293.5 138,293 141.5,292 145.5,291.5 149,290.5 153,289.5 157,289 160.5,287.5 164.5,286.5 168,285.5 172,284 176,283 179.5,281.5 183.5,280 187,278.5 191,276.5 195,275 198.5,273 202.5,271.5 206,269.5 210,267 198.5,56 96,56" fill="#d0e6fb" fill-opacity="0.7"/>
  <polygon points="210,267 215.5,267 221,266 226.5,265 232,263.5 237.5,262 243,260.5 248.5,258.5 254,256.5 259.5,254.5 265,252 270.5,249.5 276,247 281.5,244 287,241 292.5,238 298,235 303.5,232 309,228.5 314.5,225 320,221.5 325.5,217.5 331,213.5 336.5,210 342,205.5 348,201.5 353.5,197.5 359,193 364.5,188.5 370,184 375.5,179.5 381,174.5 386.5,170 392,165 397.5,160 403,155 408.5,149.5 414,144.5 419.5,139 425,133.5 430.5,128 476,128 476,56 198.5,56 210,267" fill="#a9d1f0" fill-opacity="0.55"/>
  <polygon points="96,296 100,296 103.5,296 107.5,296 111,295.5 115,295.5 119,295 122.5,295 126.5,294.5 130,294 134,293.5 138,293 141.5,292 145.5,291.5 149,290.5 153,289.5 157,289 160.5,287.5 164.5,286.5 168,285.5 172,284 176,283 179.5,281.5 183.5,280 187,278.5 191,276.5 195,275 198.5,273 202.5,271.5 206,269.5 210,267 215.5,267 221,266 226.5,265 232,263.5 237.5,262 243,260.5 248.5,258.5 254,256.5 259.5,254.5 265,252 270.5,249.5 276,247 281.5,244 287,241 292.5,238 298,235 303.5,232 309,228.5 314.5,225 320,221.5 325.5,217.5 331,213.5 336.5,210 342,205.5 348,201.5 353.5,197.5 359,193 364.5,188.5 370,184 375.5,179.5 381,174.5 386.5,170 392,165 397.5,160 403,155 408.5,149.5 414,144.5 419.5,139 425,133.5 430.5,128 476,128 476,296 96,296" fill="#ffc078" fill-opacity="0.5"/>
  <polyline points="96,296 100,296 103.5,296 107.5,296 111,295.5 115,295.5 119,295 122.5,295 126.5,294.5 130,294 134,293.5 138,293 141.5,292 145.5,291.5 149,290.5 153,289.5 157,289 160.5,287.5 164.5,286.5 168,285.5 172,284 176,283 179.5,281.5 183.5,280 187,278.5 191,276.5 195,275 198.5,273 202.5,271.5 206,269.5 210,267" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="210,267 215.5,267 221,266 226.5,265 232,263.5 237.5,262 243,260.5 248.5,258.5 254,256.5 259.5,254.5 265,252 270.5,249.5 276,247 281.5,244 287,241 292.5,238 298,235 303.5,232 309,228.5 314.5,225 320,221.5 325.5,217.5 331,213.5 336.5,210 342,205.5 348,201.5 353.5,197.5 359,193 364.5,188.5 370,184 375.5,179.5 381,174.5 386.5,170 392,165 397.5,160 403,155 408.5,149.5 414,144.5 419.5,139 425,133.5 430.5,128" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="210,267 198.5,56" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="368" y1="185.5" x2="368" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="185.5" x2="368" y2="185.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="368" cy="185.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="382" y="179" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{air pressure}$</div></foreignObject>
  <line x1="308.5" y1="229" x2="308.5" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="229" x2="308.5" y2="229" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="308.5" cy="229" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="322.5" y="222.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mountain}$</div></foreignObject>
  <foreignObject x="318" y="305.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100\,{}^\circ\text{C}$</div></foreignObject>
  <circle cx="210" cy="267" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="210" y1="267" x2="210" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="140" y="305.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{triple point}$</div></foreignObject>
  <foreignObject x="110.5" y="123" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{solid}$</div></foreignObject>
  <foreignObject x="275" y="70.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liquid}$</div></foreignObject>
  <foreignObject x="392.5" y="260" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas}$</div></foreignObject>
</svg>

```pysahdy
Why does food cook faster in a pressure cooker than in an open pot?
---
The pressure raises the boiling point above $100\,{}^\circ\text{C}$, so the water is hotter.
```

## Formula: Latent heat of fusion and vaporisation
The quantity of heat needed to melt or vaporise a mass $m$ is
```kaavat
heat of fusion :: Q = s m
heat of vaporisation :: Q = r m
```
where $Q$ is the quantity of heat (J), $s$ is the specific latent heat of fusion of the substance (J/kg), $r$ is the specific latent heat of vaporisation (J/kg) and $m$ is the mass of the substance that melts or vaporises (kg). The same quantity of heat is released when the substance freezes or condenses. At constant pressure the temperature does not change during a change of state, so the formula has no temperature change $\Delta T$.

| Water | Value |
|---|---|
| $s$ | $334\,\text{kJ/kg}$ |
| $r$ | $2260\,\text{kJ/kg}$ |
| $c$ (ice) | $2100\,\text{J/(kg}\cdot\text{K)}$ |
| $c$ (water) | $4190\,\text{J/(kg}\cdot\text{K)}$ |
| $c$ (steam) | $2000\,\text{J/(kg}\cdot\text{K)}$ |

In the table, $c$ is the specific heat capacity, which was introduced in chapter *Heating and cooling of matter: $Q = cm\Delta T$*.

A heating curve shows the temperature as a function of the energy transferred. On the rising parts the substance warms up and $Q = cm\Delta T$ applies. On the horizontal parts the substance changes state and $Q = sm$ or $Q = rm$ applies. The smaller the specific heat capacity, the steeper the temperature rises, so the parts for ice and steam are about twice as steep as the part for water:

<svg data-fig="heating-curve" viewBox="0 0 600 350" role="img" aria-label="Heating curve of water, schematic diagram: temperature as a function of the energy transferred Q. Ice warms up steeply, melts on a horizontal part at 0 degrees (Q = sm), water warms up more gently from 0 to 100 degrees, boils on a long horizontal part at 100 degrees (Q = rm) and steam warms up steeply. The parts for ice and steam are about twice as steep as the part for water; the lengths of the horizontal parts are not to scale." style="max-width:100%;font-size:24px">
  <line x1="96" y1="237" x2="476" y2="237" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="119" x2="476" y2="119" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="296" x2="490" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,296 L489,302 L489,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="297" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="237" x2="96" y2="237" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="222.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="119" x2="96" y2="119" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="104.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="508" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (^\circ\text{C})$</div></foreignObject>
  <polyline points="96,272.5 114,237 150,237 270,119 456,119 468,95.5" fill="none" stroke="#c92a2a" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="484" y="79" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{steam}$</div></foreignObject>
  <foreignObject x="99" y="184.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ice}$</span></div></foreignObject>
  <foreignObject x="156" y="242.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{melts}\quad Q = sm$</div></foreignObject>
  <foreignObject x="246" y="196.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{water}$</div></foreignObject>
  <foreignObject x="296.5" y="81" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{boils}\quad Q = rm$</div></foreignObject>
</svg>

## Worked example
The specific latent heat of vaporisation of water is determined experimentally. An open calorimeter containing boiling water stands on a balance, and the water contains a $1000\,\text{W}$ immersion heater. During five minutes ($300\,\text{s}$), the balance reading falls by $128\,\text{g}$ (an invented figure, not the result of a real measurement). What is the specific latent heat of vaporisation of water according to this reading?

<!-- vaihe -->

**Given and find.** Power $P = 1000\,\text{W}$, time $t = 300\,\text{s}$ and the mass vaporised, that is, the change in the balance reading, $\Delta m = 128\,\text{g}$.

The water is boiling, so it is at $100\,{}^\circ\text{C}$.

We want the specific latent heat of vaporisation $r$.

Assume that all the energy from the heater goes into the water.

<!-- vaihe -->

**Principle.** The water boils all the time, so its temperature does not rise and all the energy $Q = Pt$ from the heater is used to vaporise water. The quantity of heat needed for vaporisation is proportional to the mass vaporised, $Q = r\,\Delta m$. Energy is conserved, so these two are equal.

<!-- vaihe -->

**Rearranged formula.** The heat $Q_\text{h}$ given out by the heater equals the heat $Q_\text{v}$ needed for vaporisation. Write it out and solve for $r$:
```latex
\begin{aligned}
&Q_\text{h} = Q_\text{v} \\[6pt]
&Pt = r\,\Delta m \\
&r = \frac{Pt}{\Delta m}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Convert the change in the balance reading to kilograms: $128\,\text{g} = 0.128\,\text{kg}$. Power and time are already in base units, and $1\,\text{W} \cdot 1\,\text{s} = 1\,\text{J}$. Finally the result is converted to megajoules: $1\,\text{MJ} = 10^6\,\text{J}$.

<!-- vaihe -->

**Substitution.** Substitute the values with their units:
```latex
\begin{aligned}
&r = \frac{Pt}{\Delta m} \\
&= \frac{1000\,\text{W} \cdot 300\,\text{s}}{0.128\,\text{kg}} \\
&= \frac{300\,000\,\text{J}}{0.128\,\text{kg}} \\
&= 2\,343\,750\,\tfrac{\text{J}}{\text{kg}}
\end{aligned}
```

<!-- vaihe -->

**Result.** The specific latent heat of vaporisation is $2.34\,\tfrac{\text{MJ}}{\text{kg}}$. The result is given to three significant figures, because the mass reading $128\,\text{g}$ is given to three figures and it limits the precision most.

<!-- vaihe -->

**Reasonableness.** The result $2.34\,\tfrac{\text{MJ}}{\text{kg}}$ is slightly greater than the table value $2.26\,\tfrac{\text{MJ}}{\text{kg}}$, by about $3.7\,\%$. This is the expected direction: some of the heater's energy passes through the vessel into the surrounding air and does not vaporise water, so the assumption "all the energy goes into the water" gives too large an $r$. With the table value, $\Delta m = \dfrac{Q}{r} = \dfrac{Pt}{r} = \dfrac{300\,\text{kJ}}{2260\,\tfrac{\text{kJ}}{\text{kg}}} = 0.133\,\text{kg}$, or $133\,\text{g}$, would vaporise, only $5\,\text{g}$ more than was measured, so the result is correct to within a few per cent.

## Common misconception
Many people think that adding heat always raises the temperature. When a pure substance changes state at constant pressure, the temperature stays constant even though a lot of energy is transferred: melting ice takes as much energy as heating the same water from $0\,{}^\circ\text{C}$ to $80\,{}^\circ\text{C}$. Another mistake is to treat ice at zero degrees and water at zero degrees as equally good coolants. Ice cools a drink much more effectively, because as it melts it takes in a lot of energy before it starts to warm up. A third mistake is to think that water always boils at $100\,{}^\circ\text{C}$: the boiling point depends on pressure.

## Summary
- The states of matter are solid, liquid and gas. In the micro model, a change of state changes the interactions between the particles: in melting and vaporisation the interaction energy between the particles increases, but the chemical bonds inside the molecules do not break.
- At constant pressure, the temperature of a pure substance stays constant during a change of state. Melting needs $Q = sm$ and vaporising needs $Q = rm$; for water, $s = 334\,\text{kJ/kg}$ and $r = 2260\,\text{kJ/kg}$.
- In a heating curve, the rising parts are warming ($Q = cm\Delta T$) and the horizontal parts are changes of state.
- The boiling point depends on pressure; a phase diagram tells you the state of a substance from its temperature and pressure.
- The specific latent heat of vaporisation can be measured by boiling water with an immersion heater on a balance: $r = Pt/\Delta m$, where $\Delta m$ is the change in the balance reading.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a lake freezing in early winter. Near the shore there is already a thin cover of ice, farther out the water is still liquid, and there is the first snow on the shore." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-7-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
