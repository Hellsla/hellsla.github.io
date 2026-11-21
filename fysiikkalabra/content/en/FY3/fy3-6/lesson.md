# Heating and cooling of matter: $Q = cm\Delta T$

> **Why** does the sand on a beach burn your feet already in the late morning, when the water is still cool, even though the Sun has shone on both for the same time?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a lakeside beach in the late morning. The Sun shines on both the sand and the water. Heat shimmers above the sand, and the red column of a thermometer stuck in the sand is high. The column of a thermometer stuck in the shallow water is low, because the water is still cool." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
When heat is transferred to an object and its phase does not change, its internal energy increases and its temperature rises. Experiments show that the quantity of heat needed is directly proportional both to the change in temperature and to the mass of the object: a temperature rise twice as large needs twice the heat, and twice the amount of water needs twice the heat. In addition, the heat depends on the substance. Heating one kilogram of water by one degree takes about $4.2\,\text{kJ}$, but heating one kilogram of iron takes only about $0.45\,\text{kJ}$. The coefficient that is characteristic of a substance is the specific heat capacity $c$, whose unit is J/(kg·K). It tells how much energy is needed to heat one kilogram by one kelvin, and the same amount is released when the substance cools by one kelvin.

<figure class="unit-photo"><img src="pics/fy3/steaming-kettle.webp" alt="Hot water is poured from a kettle into a glass jug against a dark background, and the water is steaming."><figcaption>Hot water is poured from a kettle. The visible mist is condensed water droplets.</figcaption></figure>

An important reason is that the specific heat capacity of water is exceptionally large: water warms slowly in the Sun and cools slowly in the evening, whereas sand, whose $c$ is about one fifth of that of water, gets many times hotter with the same energy. In addition, the Sun heats only a thin surface layer of the sand, whereas in water the warming reaches deeper. Because of their large specific heat capacity, lakes even out the temperatures of the coast, and water is a good heat-transfer medium in heating pipes.

<svg data-fig="water-sand" viewBox="0 0 600 384" role="img" aria-label="Schematic: the same quantity of heat Q is transferred to equal masses of water and sand, shown by arrows of equal length. The reading of the water thermometer rises a little, that of the sand about five times as much, because the specific heat capacity of sand, 800 J/(kg·K), is about one fifth of that of water, 4190 J/(kg·K). The rises in temperature are drawn to scale and highlighted in red. The sand takes up less volume in its container, because it is denser than water." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-water-sand.webp" x="0" y="1.2" width="600" height="392.5" preserveAspectRatio="none"/>
  <foreignObject x="196" y="9.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{same } Q \text{ and the same } m$</div></foreignObject>
  <foreignObject x="216" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="24" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\Delta T$</div></foreignObject>
  <foreignObject x="157" y="279.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{water}$</div></foreignObject>
  <foreignObject x="107" y="317" width="170" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$c = 4190\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}$</div></foreignObject>
  <foreignObject x="536" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="307" y="168.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\approx 5\,\Delta T$</div></foreignObject>
  <foreignObject x="483" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sand}$</div></foreignObject>
  <foreignObject x="427" y="317" width="170" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$c = 800\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}$</div></foreignObject>
</svg>

```pysahdy
The same amount of energy is transferred to equal masses of water and sand. Which warms up more, and why?
---
The sand. Its specific heat capacity is about one fifth of that of water, so the same energy raises its temperature about five times as much.
```

When a hot and a cold object are put into one insulated container, heat is transferred from the hotter to the colder one until both have the same temperature. This state is called thermal equilibrium. Energy is conserved: the heat given out by the hot object is equal to the heat received by the cold one. An insulated container in which this is measured is called a calorimeter, and the measurement is called a calorimetric measurement. With it you can determine the specific heat capacity of an unknown substance when the specific heat capacity of water is known.

<svg data-fig="calorimeter" viewBox="0 0 600 432" role="img" aria-label="Calorimeter before and after thermal equilibrium, schematic, not to scale. Before: an insulated container holds 0.300 kg of water at 20.0 °C, and above it a 0.200 kg metal object at 100.0 °C hangs from a thread. After: the object is in the water, and both the water and the object are at a temperature of 24.5 °C. The heat given out by the metal is equal to the heat received by the water." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-calorimeter.webp" x="0" y="0" width="600" height="440" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{before}$</div></foreignObject>
  <foreignObject x="415" y="7.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{after}$</div></foreignObject>
  <foreignObject x="137" y="77.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$T_\text{m} = 100.0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="137" y="107.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m_\text{m} = 0.200\,\text{kg}$</div></foreignObject>
  <foreignObject x="50" y="317.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$T_\text{v} = 20.0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="50" y="351.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_\text{v} = 0.300\,\text{kg}$</div></foreignObject>
  <foreignObject x="456" y="221.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$Q$</span></div></foreignObject>
  <foreignObject x="350" y="317.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T = 24.5\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="340" y="351.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{same } T \text{ everywhere}$</div></foreignObject>
  <foreignObject x="130" y="399.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q_\text{given out} = Q_\text{received}$</div></foreignObject>
</svg>

## Formula: Heat and thermal equilibrium
When the phase of a substance does not change, the quantity of heat needed to heat a mass $m$, or released when it cools, is
```kaavat
heat transferred :: Q = c m \Delta T
\Delta T = T_\text{final} - T_\text{initial}
```
where $Q$ is the quantity of heat (J), $c$ the specific heat capacity of the substance (J/(kg·K)), $m$ the mass (kg) and $\Delta T$ the change in temperature (K), that is, the final temperature $T_\text{final}$ minus the initial temperature $T_\text{initial}$. The change in temperature is the same in kelvins and in degrees Celsius, so $\Delta T$ can be calculated directly from Celsius temperatures. When an object warms, $\Delta T$ and $Q$ are positive; when it cools, they are negative.

The heat capacity of a whole object
```kaavat
heat capacity :: C = c m
```
tells how many joules it takes to raise the temperature of the object by one kelvin. $C$ is the heat capacity (J/K), $c$ the specific heat capacity and $m$ the mass. An object with a large heat capacity warms and cools slowly.

```pysahdy
The heat capacity of an object is $C = 300\,\text{J/K}$. How much energy is needed to warm it by $4.0\,\text{K}$?
---
The heat capacity gives the energy per kelvin, so $300\,\text{J/K} \cdot 4.0\,\text{K} = 1200\,\text{J}$ is needed.
```

In an insulated container, energy is conserved when the heat capacity of the container itself is ignored. The heat given out by the hot object $1$ is equal to the heat received by the cold object $2$:
```latex
Q_\text{given out} = Q_\text{received}
```
Since $Q = c m \Delta T$ holds for each object, this is
```latex
c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)
```
where $T_1$ and $T_2$ are the initial temperatures of the objects and $T$ is the common final temperature, that is, the equilibrium temperature. Both sides of the equation are positive quantities of heat: for the hot object you calculate initial temperature minus final temperature, and for the cold object final temperature minus initial temperature. From the equation you can solve any quantity when the others are known: the final temperature, a mass or an unknown specific heat capacity.

The equilibrium temperature $T$ appears in two terms of the equation. You solve it by multiplying out the brackets, collecting the terms that contain $T$ on the same side and taking $T$ as a common factor:
```latex
\begin{aligned}
&c_1 m_1 T_1 - c_1 m_1 T \\
&\quad = c_2 m_2 T - c_2 m_2 T_2 \\[6pt]
&c_1 m_1 T_1 + c_2 m_2 T_2 \\
&\quad = c_1 m_1 T + c_2 m_2 T \\
&\quad = (c_1 m_1 + c_2 m_2)\,T
\end{aligned}
```
When the equation is divided on both sides by the sum $c_1 m_1 + c_2 m_2$, you get
```latex
T = \frac{c_1 m_1 T_1 + c_2 m_2 T_2}{c_1 m_1 + c_2 m_2}
```
So the equilibrium temperature is a weighted mean of the initial temperatures, where the weights are the heat capacities $c_1 m_1$ and $c_2 m_2$ of the objects. You get the ordinary mean only when the heat capacities are equal.

```pysahdy
In an insulated container, equal masses of the same liquid at $20\,{}^\circ\text{C}$ and $60\,{}^\circ\text{C}$ are mixed. What is the equilibrium temperature?
---
The heat capacities are equal, so the equilibrium temperature is the ordinary mean: $(20\,{}^\circ\text{C} + 60\,{}^\circ\text{C})/2 = 40\,{}^\circ\text{C}$.
```

| Substance | $c$ (J/(kg·K)) |
| --- | --- |
| water | 4190 |
| ice | 2100 |
| aluminium | 900 |
| sand | 800 |
| iron | 450 |
| copper | 385 |

<svg data-fig="c-bars" viewBox="0 0 600 350" role="img" aria-label="Horizontal bar chart of specific heat capacities in J/(kg·K): water 4190, ice 2100, aluminium 900, sand 800, iron 450 and copper 385. The lengths of the bars are to scale: the bar of water is about five times as long as that of sand." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-c-bars.webp" x="0" y="-1.2" width="600" height="360" preserveAspectRatio="none"/>
  <foreignObject x="130" y="9.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$c\ \left(\text{J/(kg}\cdot\text{K)}\right)$</div></foreignObject>
  <foreignObject x="50" y="51.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{water}$</div></foreignObject>
  <foreignObject x="529" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4190$</div></foreignObject>
  <foreignObject x="75" y="93.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ice}$</div></foreignObject>
  <foreignObject x="334" y="93.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2100$</div></foreignObject>
  <foreignObject x="0" y="135.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{aluminium}$</div></foreignObject>
  <foreignObject x="222" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$900$</div></foreignObject>
  <foreignObject x="62" y="177.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{sand}$</div></foreignObject>
  <foreignObject x="212.5" y="177.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800$</div></foreignObject>
  <foreignObject x="62" y="219.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{iron}$</div></foreignObject>
  <foreignObject x="180" y="219.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$450$</div></foreignObject>
  <foreignObject x="37" y="261.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{copper}$</div></foreignObject>
  <foreignObject x="174" y="261.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$385$</div></foreignObject>
  <foreignObject x="120" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="194.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1000$</div></foreignObject>
  <foreignObject x="287.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2000$</div></foreignObject>
  <foreignObject x="381" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$3000$</div></foreignObject>
  <foreignObject x="474.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$4000$</div></foreignObject>
</svg>

## Worked example
A calorimeter contains $0.300\,\text{kg}$ of water at a temperature of $20.0\,{}^\circ\text{C}$. A metal object of mass $0.200\,\text{kg}$, heated in boiling water to a temperature of $100.0\,{}^\circ\text{C}$, is lowered into it. After stirring, the temperature settles at $24.5\,{}^\circ\text{C}$. What is the specific heat capacity of the metal? Ignore the heat capacity of the calorimeter itself and heat losses to the surroundings.

<!-- vaihe -->

**Given and find.** Water: $m_\text{w} = 0.300\,\text{kg}$, $T_\text{w} = 20.0\,{}^\circ\text{C}$ and from the table $c_\text{w} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$.

Metal: $m_\text{m} = 0.200\,\text{kg}$, $T_\text{m} = 100.0\,{}^\circ\text{C}$.

Equilibrium temperature $T = 24.5\,{}^\circ\text{C}$.

We want the specific heat capacity of the metal $c_\text{m}$.

<!-- vaihe -->

**Principle.** Energy is conserved. When the calorimeter and the air take up no heat, the heat given out by the metal is equal to the heat received by the water. Each one only warms or cools and its phase does not change, so $Q = c m \Delta T$ holds for both. At the end both are at the same temperature $T$.

<!-- vaihe -->

**Rearranged formula.** The heat $Q_\text{m}$ given out by the metal equals the heat $Q_\text{w}$ received by the water. Write it out and solve for $c_\text{m}$:
```latex
\begin{aligned}
&Q_\text{m} = Q_\text{w} \\[6pt]
&c_\text{m} m_\text{m} (T_\text{m} - T) \\
&\quad = c_\text{w} m_\text{w} (T - T_\text{w}) \\[6pt]
&c_\text{m} = \frac{c_\text{w} m_\text{w} (T - T_\text{w})}{m_\text{m} (T_\text{m} - T)}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The masses are already in kilograms. A temperature difference is the same in kelvins and in degrees Celsius, so the metal cools by $T_\text{m} - T = 75.5\,\text{K}$ and the water warms by $T - T_\text{w} = 4.5\,\text{K}$.

<!-- vaihe -->

**Substitution.** First calculate the numerator, that is, the heat $Q_\text{w}$ received by the water, and then divide:
```latex
\begin{aligned}
&Q_\text{w} = c_\text{w} m_\text{w} (T - T_\text{w}) \\
&= 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.300\,\text{kg} \cdot 4.5\,\text{K} \\
&= 5656.5\,\text{J} \\[6pt]
&c_\text{m} = \frac{Q_\text{w}}{m_\text{m} (T_\text{m} - T)} \\
&= \frac{5656.5\,\text{J}}{0.200\,\text{kg} \cdot 75.5\,\text{K}} \\
&= 374.6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}
\end{aligned}
```

<!-- vaihe -->

**Result.** The specific heat capacity of the metal is about $3.7 \cdot 10^2\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$. The result is given with two significant figures, because the temperature change of the water, $4.5\,\text{K}$, is known only to two figures: if the final reading were $0.1\,\text{K}$ higher, that is $24.6\,{}^\circ\text{C}$, the result would be $383\,\text{J/(kg}\cdot\text{K)}$.

<!-- vaihe -->

**Reasonableness.** The value is close to the specific heat capacity of copper, $385\,\text{J/(kg}\cdot\text{K)}$, so the object is probably copper. In a lossless calorimeter a $0.200\,\text{kg}$ copper object would raise the water to $24.6\,{}^\circ\text{C}$ (try it in the simulation); the measured reading, $0.1\,\text{K}$ lower, is explained by the reading precision or by the fact that in reality some of the heat also went into the calorimeter vessel and the air.

The water warmed by only $4.5\,\text{K}$ although the metal cooled by $75.5\,\text{K}$: the heat capacity of the water is $C_\text{w} = m_\text{w} c_\text{w} = 0.300\,\text{kg} \cdot 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} = 1257\,\tfrac{\text{J}}{\text{K}}$, which is much more than the heat capacity of the object, $C_\text{m} = m_\text{m} c_\text{m} = 0.200\,\text{kg} \cdot 374.6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \approx 75\,\tfrac{\text{J}}{\text{K}}$.

## Common misconception
Many people think that heat and temperature are the same thing, or that objects heated to the same temperature have received the same amount of energy. Heating a kilogram of water and a kilogram of iron from $20\,{}^\circ\text{C}$ to $60\,{}^\circ\text{C}$ takes almost ten times as much energy for the water. Another mistake is to calculate the equilibrium temperature as a mean. When $1.0\,\text{kg}$ of 80-degree water is poured into $3.0\,\text{kg}$ of 20-degree water, the specific heat capacity of water $c$ is on both sides of the equation and cancels:
```latex
\begin{aligned}
&Q_\text{given out} = Q_\text{received} \\[6pt]
&c \cdot 1.0\,\text{kg} \cdot (80\,{}^\circ\text{C} - T) \\
&\quad = c \cdot 3.0\,\text{kg} \cdot (T - 20\,{}^\circ\text{C}) \\[6pt]
&1.0\,\text{kg} \cdot (80\,{}^\circ\text{C} - T) \\
&\quad = 3.0\,\text{kg} \cdot (T - 20\,{}^\circ\text{C}) \\[6pt]
&80\,{}^\circ\text{C} - T = 3T - 60\,{}^\circ\text{C} \\
&140\,{}^\circ\text{C} = 4T \\
&T = 35\,{}^\circ\text{C}
\end{aligned}
```
The hot water is on the left side, as in the general equation. On the first line of the last group the equation has been divided on both sides by a kilogram and the brackets have been multiplied out. So the final result is not $50\,{}^\circ\text{C}$ but $35\,{}^\circ\text{C}$, because there is three times as much cold water as hot. The same result comes from the weighted mean: $$\begin{aligned} &T \\ &= (3.0\,\text{kg} \cdot 20\,{}^\circ\text{C} + 1.0\,\text{kg} \cdot 80\,{}^\circ\text{C}) \\ &: 4.0\,\text{kg} \\ &= 35\,{}^\circ\text{C} \end{aligned}$$.

A third mistake is to convert $\Delta T$ to kelvins by adding 273: a change in temperature is the same on both scales.

## Summary
- The quantity of heat is proportional to the mass and to the change in temperature: $Q = c m \Delta T$ when the state of matter does not change. The specific heat capacity $c$ depends on the substance, and for water it is large, $4190\,\text{J/(kg}\cdot\text{K)}$.
- The heat capacity $C = cm$ tells how many joules it takes to heat the whole object by one kelvin.
- In an insulated container the heat given out by the hot object is equal to the heat received by the cold one: $$\begin{aligned} &c_1 m_1 (T_1 - T) \\ &= c_2 m_2 (T - T_2) \end{aligned}$$. The equilibrium temperature $T$ is solved by collecting the terms with $T$ on the same side; it is a mean weighted by the heat capacities, and usually not the ordinary mean of the initial temperatures.
- A calorimetric measurement determines the specific heat capacity of an unknown substance with the help of water.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a sauna stove. Water is thrown with a ladle onto the hot stones, and steam rises from the stones. Wooden benches are in the background." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
