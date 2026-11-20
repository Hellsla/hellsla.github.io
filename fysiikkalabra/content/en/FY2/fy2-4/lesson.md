# Efficiency

> **Why** does an incandescent lamp get so hot that it can burn your finger, even though its job is to give light, and why does an LED lamp give just as much light with much less electricity?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: two ceiling lamps side by side above a table in a room in the evening. On the left an incandescent bulb whose filament glows and around which heat shimmers; on the right an LED bulb. Both cones of light on the table are equally bright." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
Energy does not disappear, but not all the energy taken by a device becomes the form of energy that you want from the device. The job of an incandescent lamp is to give light, so its useful energy is light. However, most of the electrical energy that the lamp takes becomes heat, which warms the lamp and its surroundings but does not give light. This part is called losses. Losses are not lost energy but energy that has changed into a useless form, usually heat.

<svg data-fig="lamp" viewBox="0 0 600 350" role="img" aria-label="Energy flow diagram to scale: an incandescent lamp takes electrical energy of 100 J. Electricity flows from the left into the picture of the lamp. To the right continue a thin green arrow, the light energy of 5 J, and a thick orange arrow, the heat energy of 95 J. The thicknesses of the arrows are proportional to the energies, so the share of light is 5 percent of the incoming energy." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-4-lamp.webp" x="1.2" y="0" width="597" height="358.2" preserveAspectRatio="none"/>
  <foreignObject x="30" y="13.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{incandescent lamp}$</div></foreignObject>
  <foreignObject x="30" y="55.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{o} = 100\,\text{J}$</div></foreignObject>
  <foreignObject x="30" y="233.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{electricity}$</div></foreignObject>
  <foreignObject x="297" y="53.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_\text{a} = 5\,\text{J}\ (\text{light})$</div></foreignObject>
  <foreignObject x="287" y="323.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{h} = 95\,\text{J}\ (\text{heat})$</div></foreignObject>
  <foreignObject x="186" y="255.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
</svg>

The flow of energy through a device can be shown with an energy flow diagram, also called a Sankey diagram. In the diagram the thickness of an arrow is proportional to energy: the incoming arrow divides into a thin arrow of useful energy and a thick arrow of losses. When the lamp takes electrical energy of $100\,\text{J}$, only $5\,\text{J}$ becomes light and the remaining $95\,\text{J}$ is heat. The thicknesses of the outgoing arrows add up to the thickness of the incoming arrow, because energy is conserved.

### Losses depend on the purpose of the device
In a kettle, heat is useful when it warms the water, and a loss when it escapes through the sides of the kettle into the room. The heat of an incandescent lamp, on the other hand, is counted as a loss, even if it warms a room in winter, because the benefit of the lamp has been defined as light. So what is useful depends on the purpose of the device, and the value of the efficiency depends on what is defined as useful and what is counted as part of the device.

```pysahdy
The purpose of an electric heater is to warm a room. Is the heat it produces useful or a loss?
---
It is useful, because the benefit of a heater has been defined as heat. The same heat would be a loss in a device whose purpose is, for example, to give light.
```

### Efficiency tells the share of the useful part
Efficiency is the share of useful energy in the energy taken by the device. Efficiency is at most $100\,\%$, because energy is conserved and you cannot get more useful energy out than you put in. In real devices it is often below $100\,\%$, because part of the energy taken does not end up in the defined useful purpose: for example, it becomes heat in friction or in conductors, and the heat spreads into the surroundings. When the purpose of a device is something other than heat, efficiency varies a lot: an electric motor reaches about $90\,\%$, but a lamp and a combustion engine stay clearly below $100\,\%$. In an electric heater the purpose is the heat itself: in practice all the electrical energy becomes heat that warms the room, so the efficiency is almost $100\,\%$. An ideal, lossless device would have an efficiency of $100\,\%$. The efficiencies of devices vary a lot:

| Device and its useful output | typical $\eta$ |
| --- | --- |
| incandescent lamp: light | $5\,\%$ |
| LED lamp: light | $30\,\%$ |
| kettle: warming of water | $90\,\%$ |
| electric motor: motion | $90\,\%$ |
| petrol engine: motion of a car | $25\,\%$ |
| solar panel: electricity | $20\,\%$ |

The values in the table are typical rounded values, not measurements of any particular device. The real efficiency depends on the model of the device and on the way it is used. The value for the petrol engine is typical for steady motorway driving; in city driving and at other small loads the efficiency is clearly lower. The efficiency of an electric motor changes little when it runs close to the power it was designed for.

```pysahdy
A manufacturer claims that a device has an efficiency of $120\,\%$. Why cannot the claim be true?
---
Energy is conserved, so a device cannot give more useful energy than it takes in. That is why efficiency is at most $100\,\%$.
```

## Formula: Efficiency
Efficiency $\eta$ (eta) is the ratio of the useful energy to the energy taken by the device. When the device runs at constant power, the same ratio is also obtained from powers:
```kaavat
efficiency :: \eta = \frac{E_\text{a}}{E_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```
where $\eta$ is the efficiency (a ratio, often given as a percentage), $E_\text{a}$ the useful energy given by the device (J), $E_\text{o}$ the energy taken by the device (J), $P_\text{a}$ the useful power (W) and $P_\text{o}$ the power taken by the device (W). A ratio is converted to a percentage by multiplying it by $100\,\%$, for example $0.30 \cdot 100\,\% = 30\,\%$. The multiplication does not change the number, because $1\,\% = 0.01$ and so $100\,\% = 100 \cdot 0.01 = 1$.

The ratio of the powers is the same as the ratio of the energies, because at constant power energy is power multiplied by time (chapter *Power: $P = \Delta E/\Delta t$*). While the device runs for a time $t$, the energies are $E_\text{a} = P_\text{a} \cdot t$ and $E_\text{o} = P_\text{o} \cdot t$, and the time cancels:
```latex
\begin{aligned}
\eta &= \frac{E_\text{a}}{E_\text{o}} \\
&= \frac{P_\text{a} \cdot t}{P_\text{o} \cdot t} \\
&= \frac{P_\text{a}}{P_\text{o}}
\end{aligned}
```
So efficiency does not depend on whether energy or power is measured, or on the running time.

### Conservation of energy and losses
Conservation of energy divides the energy taken by the device into useful energy and losses $E_\text{h}$:
```latex
E_\text{o} = E_\text{a} + E_\text{h}
```
The same holds for powers, $P_\text{o} = P_\text{a} + P_\text{h}$. When the efficiency is known, the useful energy is $E_\text{a} = \eta \cdot E_\text{o}$ and the energy taken is $E_\text{o} = \tfrac{E_\text{a}}{\eta}$.

```pysahdy
A device takes in energy $50\,\text{J}$ and gives useful energy $20\,\text{J}$. How much is lost, and what is the efficiency?
---
The losses are $E_\text{h} = 50\,\text{J} - 20\,\text{J} = 30\,\text{J}$.
The efficiency is $20\,\text{J} : 50\,\text{J} = 0.40$, or $40\,\%$.
```

### Comparing two lamps
A lamp with a low efficiency needs a higher power to get the same useful output. For a light power of $3\,\text{W}$ an incandescent lamp needs $60\,\text{W}$ but an LED lamp only $10\,\text{W}$, because the efficiencies are $5\,\%$ and $30\,\%$. In the diagram the thicknesses of the arrows are on the same scale: the green arrows of the light power are equally thick, but the incoming arrow of the incandescent lamp is six times thicker.

In this simplified model the useful energy of a lamp is defined as the energy of visible radiation. In practice the lighting ability of a lamp is better described by its luminous flux, which takes into account that the eye is not equally sensitive to all wavelengths.

<svg data-fig="pair" viewBox="0 0 600 450" role="img" aria-label="Two energy flow diagrams on the same scale. At the top, an incandescent lamp takes a power of 60 W and gives a light power of 3 W; the efficiency is 5 percent, and 57 W becomes heat. At the bottom, an LED lamp takes a power of 10 W and gives the same light power of 3 W; the efficiency is 30 percent, and 7 W becomes heat. In both, the green arrow of light power is equally thick, but the incoming arrow of the LED lamp is one sixth of the incoming arrow of the incandescent lamp." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-4-pair.webp" x="0" y="0" width="600" height="455" preserveAspectRatio="none"/>
  <foreignObject x="30" y="11.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{incandescent lamp}$</div></foreignObject>
  <foreignObject x="30" y="43.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 60\,\text{W}$</div></foreignObject>
  <foreignObject x="30" y="195.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
  <foreignObject x="257" y="41.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{light})$</div></foreignObject>
  <foreignObject x="247" y="230.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 57\,\text{W}\ (\text{heat})$</div></foreignObject>
  <foreignObject x="30" y="281.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{LED lamp}$</div></foreignObject>
  <foreignObject x="30" y="313.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 10\,\text{W}$</div></foreignObject>
  <foreignObject x="257" y="309.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{light})$</div></foreignObject>
  <foreignObject x="30" y="383.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 30\,\%$</div></foreignObject>
  <foreignObject x="257" y="412.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 7\,\text{W}\ (\text{heat})$</div></foreignObject>
</svg>

In a diagram drawn to scale you can see the efficiency directly: it is the thickness of the useful arrow as a share of the thickness of the incoming arrow. If the incoming arrow is $5.0\,\text{cm}$ thick and the useful arrow $4.0\,\text{cm}$, the efficiency is $4.0 : 5.0 = 0.80$, that is, $80\,\%$.

## Worked example
A kettle has an efficiency of $90\,\%$ and takes a power of $2.0\,\text{kW}$ from the electricity grid. The kettle is on for $3.0\,\text{min}$. How much electrical energy becomes losses, that is, heat that does not warm the water?

<!-- vaihe -->

**Known and unknown.**

- Efficiency $\eta = 90\,\%$,
- power taken $P_\text{o} = 2.0\,\text{kW}$ and
- running time $t = 3.0\,\text{min}$.

We want the loss energy $E_\text{h}$.

<!-- vaihe -->

**Principle.** The kettle runs at constant power, so the energy taken is power multiplied by time. Efficiency tells what share of the energy taken warms the water. Energy is conserved, so the rest is losses.

<!-- vaihe -->

**Rearranged formula.** The energy taken, the useful energy and the losses are found in order:
```latex
\begin{aligned}
E_\text{o} &= P_\text{o} \cdot t \\
E_\text{a} &= \eta \cdot E_\text{o} \\
E_\text{h} &= E_\text{o} - E_\text{a}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Power to watts: $2.0\,\text{kW} = 2.0 \cdot 1000\,\text{W} = 2000\,\text{W}$. Time to seconds: $3.0\,\text{min} = 3.0 \cdot 60\,\text{s} = 180\,\text{s}$. Efficiency to a number: $90\,\% = 90 \cdot 0.01 = 0.90$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
E_\text{o} &= P_\text{o} \cdot t \\
&= 2000\,\text{W} \cdot 180\,\text{s} \\
&= 360\,000\,\text{J} \\[6pt]
E_\text{a} &= \eta \cdot E_\text{o} \\
&= 0.90 \cdot 360\,000\,\text{J} \\
&= 324\,000\,\text{J} \\[6pt]
E_\text{h} &= E_\text{o} - E_\text{a} \\
&= 360\,000\,\text{J} - 324\,000\,\text{J} \\
&= 36\,000\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The energy that becomes losses is $36\,000\,\text{J} = 36 \cdot 1000\,\text{J} = 36\,\text{kJ}$.

The result is given with two significant figures, because the initial values $90\,\%$, $2.0\,\text{kW}$ and $3.0\,\text{min}$ are given to two figures.

<!-- vaihe -->

**Reasonableness.** The losses must be $100\,\% - 90\,\% = 10\,\%$ of the energy taken, and the energy taken is $360\,000\,\text{J} = 360 \cdot 1000\,\text{J} = 360\,\text{kJ}$, so $0.10 \cdot 360\,\text{kJ} = 36\,\text{kJ}$. In addition, the useful energy and the losses add up to the energy taken: $324\,\text{kJ} + 36\,\text{kJ} = 360\,\text{kJ}$.

## Common misconception
Many people think that energy disappears in the losses. However, energy is conserved in every device. The energy leaving an incandescent lamp is equal to the energy entering it: $3\,\text{W}$ of light and $57\,\text{W}$ of heat make $60\,\text{W}$ in total. A loss only means that part of the energy ended up in a form that is of no use.

Another mistake is to think that a high-power device is efficient. Efficiency is a ratio, not an amount. A $100\,\text{W}$ incandescent lamp gives $5\,\text{W}$ of light and a $60\,\text{W}$ lamp $3\,\text{W}$, but both have an efficiency of $5\,\%$. A high-power device uses more energy, but power does not tell what share of the energy is useful.

## Summary
- Efficiency is the share of useful energy in the energy taken by the device: $\eta = \tfrac{E_\text{a}}{E_\text{o}} = \tfrac{P_\text{a}}{P_\text{o}}$. It is often given as a percentage and is at most $100\,\%$. In real devices it is often below $100\,\%$, because part of the energy does not end up as the useful output; for an electric heater it is almost $100\,\%$.
- Energy is conserved: $E_\text{o} = E_\text{a} + E_\text{h}$. Losses are usually heat that spreads into the surroundings.
- In an energy flow diagram the thickness of an arrow is proportional to energy or power, and efficiency is the share of the useful arrow in the incoming arrow.
- The efficiency of a device that runs steadily does not depend on running time, because the time cancels from the ratio of the energies. The way the device is used can change it: for example, the efficiency of a petrol engine is clearly lower at a small load.
