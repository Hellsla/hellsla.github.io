# Ideal gas law $pV = nRT$

> **Why** is a helium balloon much lighter than an air balloon of the same size? Does it contain less gas?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: two balloons of the same size in a room. The helium balloon has risen to the ceiling with its string hanging down, and the ordinary balloon filled with air rests on the floor." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
The gas laws in the chapter *Changes of state of a gas and Boyle's law* applied to a fixed amount of gas. Now we compare different amounts of gas and different gases. Fill a rigid $5.00$ litre glass flask, first pumped empty, at a pressure of $101\,\text{kPa}$ and a temperature of $20\,{}^\circ\text{C}$, one after another, with helium, nitrogen, air and carbon dioxide. In an example weighing (invented values with some scatter of weighing) the masses of the gases are very different: $0.83\,\text{g}$, $5.78\,\text{g}$, $6.02\,\text{g}$ and $9.10\,\text{g}$. But when you divide each mass by the molar mass of the gas, the result is about $0.207\,\text{mol}$ every time. So at the same pressure and temperature, the same volume contains the same amount of gas, whatever the gas is. The helium balloon is lighter because helium particles are lighter, not because there is less gas.

<svg data-fig="helium-ilma" viewBox="0 0 600 326" role="img" aria-label="Schematic picture with the particles enlarged: two gas balloons of the same size at the same pressure and temperature. Both contain the same number of particles and the amount of substance n = 0.21 mol. The mass of the gas in the helium balloon is m = 0.83 g and in the air balloon m = 6.0 g, because the particles of air are heavier. The arrows show the motion of the particles to scale: at the same temperature the light helium particles move faster, and the length of the arrow is the ratio of the speeds, 2.7 : 1." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-helium-ilma.webp" x="3.7" y="-1.2" width="594.1" height="331.7" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="231.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{helium}$</div></foreignObject>
  <foreignObject x="83.5" y="263.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 0.21\,\text{mol}$</div></foreignObject>
  <foreignObject x="96" y="295.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = 0.83\,\text{g}$</div></foreignObject>
  <foreignObject x="427.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{air}$</div></foreignObject>
  <foreignObject x="383.5" y="263.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 0.21\,\text{mol}$</div></foreignObject>
  <foreignObject x="402.5" y="295.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = 6.0\,\text{g}$</div></foreignObject>
  <foreignObject x="271" y="93.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{same}$</div></foreignObject>
  <foreignObject x="275.5" y="123.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$p,\ T$</div></foreignObject>
</svg>

Even a small amount of gas contains an enormous number of particles. So we do not count them one by one but in moles, in the same way as eggs are counted in dozens. One mole is ${6.022 \cdot 10^{23}}$ particles, and the number ${N_\text{A} = 6.022 \cdot 10^{23}\,\text{1/mol}}$ is called the Avogadro constant. The amount of substance $n$ tells you how many moles of particles there are. The mass of one mole is the molar mass $M$ of the substance: $4.00\,\text{g/mol}$ for helium, $29.0\,\text{g/mol}$ for air on average and $44.0\,\text{g/mol}$ for carbon dioxide. So you can get the amount of substance both from the number of particles and from the mass:
```kaavat
amount of substance from the Avogadro constant :: n = \frac{N}{N_\text{A}}
amount of substance :: n = \frac{m}{M}
```
where $N$ is the number of particles, $m$ is the mass (g or kg) and $M$ is the molar mass (g/mol or kg/mol).

<svg data-fig="mole-masses" viewBox="0 0 600 316" role="img" aria-label="Schematic picture with the particles enlarged: three containers of the same size at the same pressure and temperature, each with the same number of particles, that is, amount of substance n = 1.00 mol. The molar mass is 4.00 g/mol for helium, 29.0 g/mol for air and 44.0 g/mol for carbon dioxide. The bar under each container is the mass of the gas to scale: one mole weighs a different amount for different gases." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-mole-masses.webp" x="0" y="0" width="603" height="325.4" preserveAspectRatio="none"/>
  <foreignObject x="14" y="153.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{helium}$</div></foreignObject>
  <foreignObject x="14" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 4.00\,\text{g/mol}$</div></foreignObject>
  <foreignObject x="14" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 4.00\,\text{g}$</div></foreignObject>
  <foreignObject x="214" y="153.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{air}$</div></foreignObject>
  <foreignObject x="214" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 29.0\,\text{g/mol}$</div></foreignObject>
  <foreignObject x="214" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 29.0\,\text{g}$</div></foreignObject>
  <foreignObject x="414" y="153.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{carbon dioxide}$</div></foreignObject>
  <foreignObject x="414" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 44.0\,\text{g/mol}$</div></foreignObject>
  <foreignObject x="414" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 44.0\,\text{g}$</div></foreignObject>
  <foreignObject x="20" y="281.5" width="560" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{in each container }n = 1.00\,\text{mol},\ \text{same }p, T$</div></foreignObject>
</svg>

```pysahdy
The molar mass of helium is $4.00\,\text{g/mol}$. How many moles are there in $8.0\,\text{g}$ of helium?
---
The amount of substance is $n = m/M$, so $n = 8.0\,\text{g}/4.00\,\text{g/mol} = 2.0\,\text{mol}$.
```

The ideal gas is a microscopic model. In it, the particles are thought of as points, and they interact with each other and with the walls of the container only when they collide. So the energy of the interactions between the particles is negligible in the model, and the temperature in kelvins is directly proportional to the mean kinetic energy of the particles. Pressure comes from collisions with the walls. It grows when there are more particles, when they move faster (that is, the temperature is higher) or when the volume is smaller. Real gases follow the model well in ordinary conditions. The model starts to fail at high pressures and low temperatures, when the particles are close together and the attraction between them condenses the gas into a liquid.

## Formula: Equation of state of an ideal gas
The example weighing gives a number that is the same for all gases: pressure multiplied by volume and divided by the amount of substance and the temperature in kelvins. With the mean amount of substance of the four gases, $0.2071\,\text{mol}$, it is
```latex
\begin{aligned}
R &= \frac{pV}{nT} \\
&= \frac{101\,000\,\text{Pa} \cdot 0.00500\,\text{m}^3}{0.2071\,\text{mol} \cdot 293.15\,\text{K}} \\
&\approx 8.3\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}
\end{aligned}
```
Precise measurements give the value $R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ for all gases, as long as the pressure is not very high and the temperature is not very low. This number is called the molar gas constant. From it we get the equation of state of an ideal gas
```kaavat
ideal gas law :: pV = nRT
```
where $p$ is the absolute pressure of the gas, $V$ the volume, $n$ the amount of substance, $R$ the molar gas constant and $T$ the temperature in kelvins. The type of gas does not appear in the equation at all. A temperature $\theta$ given in degrees Celsius is converted to kelvins by adding $273.15$ to the numerical value.

```pysahdy
Two balloons of the same size are at the same pressure and temperature, one with helium and one with air. Do they contain the same amount of gas?
---
Yes. The type of gas does not appear in the equation $pV = nRT$, so the same $p$, $V$ and $T$ mean the same amount of substance $n$. The masses differ because the molar masses differ.
```

When the value of the gas constant
```latex
R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}
```
is used, the unit of the product $pV$ must be the joule. Usually the pressure is converted to pascals and the volume to cubic metres, and then
```latex
1\,\text{Pa} \cdot \text{m}^3 = 1\,\tfrac{\text{N}}{\text{m}^2} \cdot \text{m}^3 = 1\,\text{N} \cdot \text{m} = 1\,\text{J}
```
Kilopascals and litres can also be combined, because
```latex
1\,\text{kPa} \cdot \textsf{l} = 1000\,\text{Pa} \cdot 0.001\,\text{m}^3 = 1\,\text{J}
```
What matters most is to handle the units consistently throughout the calculation.

When you solve the equation of state for pressure, you see that the pressure doubles when the number of particles or the temperature in kelvins doubles, or when the volume is halved. So the pressure is directly proportional to the number of particles and the temperature in kelvins and inversely proportional to the volume, that is, $p \propto NT/V$.

<svg data-fig="paine-ja-tekijat" viewBox="0 0 600 300" role="img" aria-label="Diagram of four gas cylinders closed with pistons, particles enlarged. From left to right: in the initial state the number of particles is N, the temperature is T and the volume is V, and the pressure is p. The pressure is 2p when there are twice as many particles (2N), when the temperature in kelvins is doubled (2T), that is, the particles move faster, or when the piston has been pushed to half the volume (V/2). The length of the arrows shows the speed of the particles." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-paine-ja-tekijat.webp" x="1.2" y="0" width="597" height="307.2" preserveAspectRatio="none"/>
  <foreignObject x="36" y="211.5" width="78" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ T,\ V$</div></foreignObject>
  <foreignObject x="65" y="251.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="180" y="211.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2N,\ T,\ V$</div></foreignObject>
  <foreignObject x="208.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
  <foreignObject x="330" y="211.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ 2T,\ V$</div></foreignObject>
  <foreignObject x="358.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
  <foreignObject x="473.5" y="211.5" width="103" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ T,\ V/2$</div></foreignObject>
  <foreignObject x="508.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
</svg>

```pysahdy
The temperature of a gas in kelvins doubles and its volume doubles. The number of particles stays the same. What happens to the pressure?
---
The pressure does not change, because $p \propto NT/V$ and the two factors of 2 cancel.
```

In the simulation you can investigate this at the particle level: change the number of particles, the temperature and the volume, and compare the pressure measured at the walls with the prediction of the equation of state, which you calculate yourself. Collisions between the particles do not change the pressure on average, so they have been left out of the simulation. In the simulation the pressure is shown relative to a reference state ($p/p_\text{ref}$), not in pascals. The reference state is $N = 100$ particles, $T = 300\,\text{K}$ and the full volume ($V = 100\,\%$); in it $p/p_\text{ref} = 1$, and the value 2 means twice the reference pressure. The number of particles $N$ represents the amount of gas.

<!-- sim -->

<figure class="unit-photo"><img src="pics/fy3/hot-air-balloon-burner.webp" alt="A bright yellow flame points up into the red envelope of a hot air balloon. The basket's attachment chains and cables are in the foreground."><figcaption>The burner of a hot air balloon heats the air inside the balloon. The mouth of the balloon is open at the bottom, so the pressure of the air inside stays almost equal to the pressure outside.</figcaption></figure>

When the amount of gas does not change, $nR$ is constant, and the equation of state gives the combined gas law $p_1V_1/T_1 = p_2V_2/T_2$ (subscripts 1 and 2 are the initial and final state). From it you get every gas law of the chapter *Changes of state of a gas and Boyle's law* when one quantity is kept constant.

## Worked example
A party balloon is filled with helium until its volume is $5.0\,\textsf{l}$. In the balloon the pressure is $101\,\text{kPa}$ and the temperature is $20\,{}^\circ\text{C}$. How many moles of helium are in the balloon, and what is the mass of the helium? The molar mass of helium is $4.0\,\text{g/mol}$.

<!-- vaihe -->

**Given and find.** The volume of the balloon is $V = 5.0\,\textsf{l}$, the pressure is $p = 101\,\text{kPa}$, the temperature is $\theta = 20\,{}^\circ\text{C}$ and the molar mass of helium is $M = 4.0\,\text{g/mol}$.

We want the amount of substance $n$ and the mass $m$.

<!-- vaihe -->

**Principle.** The balloon contains a certain amount of helium in a certain volume, at a certain pressure and temperature, and helium behaves as an ideal gas at ordinary pressure and room temperature. So the equation of state $pV = nRT$ gives the amount of substance, and the molar mass converts the amount of substance into mass.

<!-- vaihe -->

**Rearranged formula.** Solve the amount of substance from the equation of state and the mass from the equation $n = m/M$:
```latex
\begin{aligned}
n &= \frac{pV}{RT} \\
m &= nM
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The equation of state needs base units:

- volume $V = 5.0\,\textsf{l} = 0.0050\,\text{m}^3$
- pressure $p = 101\,\text{kPa} = 101\,000\,\text{Pa}$
- temperature $T = (20 + 273.15)\,\text{K} = 293.15\,\text{K}$
- the molar mass stays as $M = 4.0\,\text{g/mol}$, so the mass comes out in grams

<!-- vaihe -->

**Substitution.** Substitute the values with their units:
```latex
\begin{aligned}
n &= \frac{pV}{RT} \\
&= \frac{101\,000\,\text{Pa} \cdot 0.0050\,\text{m}^3}{8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 293.15\,\text{K}} \\
&= 0.2073\,\text{mol} \approx 0.21\,\text{mol}
\end{aligned}
```

<!-- vaihe -->

**Result.** The mass of the helium is calculated with the more precise amount of substance:
```latex
\begin{aligned}
m &= nM \\
&= 0.2073\,\text{mol} \cdot 4.0\,\text{g/mol} \\
&\approx 0.83\,\text{g}
\end{aligned}
```
The balloon contains $0.21\,\text{mol}$ of helium, and its mass is $0.83\,\text{g}$.

The amount of substance is limited by the volume $5.0\,\textsf{l}$, and the mass by the molar mass $4.0\,\text{g/mol}$ as well, each with two digits, so the results are given with two significant figures.

The pressure $101\,\text{kPa}$ and the temperature $293\,\text{K}$ have three digits and do not limit the result.

<!-- vaihe -->

**Reasonableness.** One mole of gas takes up about $24\,\textsf{l}$ at room temperature and normal pressure, so $5.0\,\textsf{l}$ contain about $5.0\,\textsf{l} : 24\,\textsf{l/mol} \approx 0.21\,\text{mol}$ of gas. An air balloon of the same size contains the same number of moles of air, but its mass is about $0.2073\,\text{mol} \cdot 29\,\text{g/mol} \approx 6.0\,\text{g}$. The helium balloon is lighter because helium particles are lighter, not because there is less gas.

## Common misconception
Three mistakes keep appearing in calculations with the equation of state:

- **Degrees Celsius.** In the equation of state the temperature is always in kelvins. For example, $0\,{}^\circ\text{C}$ would give a pressure of zero, but a gas has a pressure at the freezing point too.
- **Mixed units.** If the pressure is in kilopascals but the volume in cubic metres, or the pressure in pascals but the volume in litres, the result is wrong by a factor of a thousand. The safest way is to convert all quantities to base units: pressure to pascals, volume to cubic metres and temperature to kelvins.
- **Heavy gas.** Many people think that fewer moles of a heavier gas fit in the same volume. But the amount of substance depends only on the pressure, the volume and the temperature, not on the type of gas. The mass, on the other hand, depends on the molar mass.

## Summary
- The equation of state of an ideal gas is $pV = nRT$, where $R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ and $T$ is in kelvins.
- The amount of substance $n$ tells the amount of gas in moles: $n = N/{N_\text{A}} = m/M$.
- The pressure is proportional to the expression $NT/V$: the pressure doubles when the number of particles or the temperature in kelvins doubles, or when the volume is halved.
- When the amount of gas stays the same, $p_1V_1/T_1 = p_2V_2/T_2$, and from it you get the separate gas laws.
- At the same pressure, temperature and volume there is always the same number of moles of gas, whatever the type of gas; weighing gives the same $m/M$ for all gases.
- The ideal gas model works well in ordinary conditions and fails at high pressures and low temperatures.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a hot-air balloon floats above a lake. A burning flame above the basket heats the air inside the balloon." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
