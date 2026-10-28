# Efficiency

> **Why** does an incandescent lamp get so hot that it can burn your finger, even though its job is to give light, and why does an LED lamp shine just as brightly with much less electricity?

## Key idea
Energy does not disappear, but not all the energy taken by a device becomes the form of energy that you want from the device. The job of an incandescent lamp is to give light, so its useful energy is light. However, most of the electrical energy that the lamp takes becomes heat, which warms the lamp and its surroundings but does not give light. This part is called losses. Losses are not lost energy but energy that has changed into a useless form, usually heat.

<svg data-fig="lamp" viewBox="0 0 600 350" role="img" aria-label="Energy flow diagram to scale: an incandescent lamp takes electrical energy of 100 J. Electricity flows from the left into the picture of the lamp. To the right continue a thin green arrow, the light energy of 5 J, and a thick orange arrow, the heat energy of 95 J. The thicknesses of the arrows are proportional to the energies, so the share of light is 5 percent of the incoming energy." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy24l-in" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="292" y2="0"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy24l-ok" gradientUnits="userSpaceOnUse" x1="292" y1="0" x2="550" y2="0"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy24l-loss" gradientUnits="userSpaceOnUse" x1="292" y1="0" x2="550" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <path d="M30,96 L168,96 L168,88 L190,156.0 L168,224 L168,216 L30,216 Z" fill="url(#fy24l-in)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M292,96 L520,96 L520,88 L550,99.0 L520,110.0 L520,102.0 L292,102.0 Z" fill="url(#fy24l-ok)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M292,102.0 C382,102.0 322,196 422,196 L520,196 L520,188 L550,253.0 L520,318.0 L520,310.0 L422,310.0 C322,310.0 382,216 292,216 Z" fill="url(#fy24l-loss)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="190" y="70" width="102" height="172" rx="12" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="241" cy="110" r="34" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M225,110 L233,96 L241,122 L249,96 L257,110" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  <rect x="225" y="144" width="32" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="225" y1="154" x2="257" y2="154" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="225" y1="164" x2="257" y2="164" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="30" y="13.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{incandescent lamp}$</div></foreignObject>
  <foreignObject x="30" y="55.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{o} = 100\,\text{J}$</div></foreignObject>
  <foreignObject x="30" y="233.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{electricity}$</div></foreignObject>
  <foreignObject x="297" y="53.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_\text{a} = 5\,\text{J}\ (\text{light})$</div></foreignObject>
  <foreignObject x="287" y="323.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{h} = 95\,\text{J}\ (\text{heat})$</div></foreignObject>
  <foreignObject x="186" y="255.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
</svg>

The flow of energy through a device can be shown with an energy flow diagram, also called a Sankey diagram. In the diagram the thickness of an arrow is proportional to energy: the incoming arrow divides into a thin arrow of useful energy and a thick arrow of losses. When the lamp takes electrical energy of $100\,\text{J}$, only $5\,\text{J}$ becomes light and the remaining $95\,\text{J}$ is heat. The thicknesses of the outgoing arrows add up to the thickness of the incoming arrow, because energy is conserved.

### Losses depend on the purpose of the device
In a kettle, heat is useful when it warms the water, and a loss when it escapes through the sides of the kettle into the room. The heat of an incandescent lamp, on the other hand, is always a loss, even if it warms a room in winter, because the purpose of the lamp is to give light. So what is useful depends on the purpose of the device.

### Efficiency tells the share of the useful part
Efficiency is the share of useful energy in the energy taken by the device. It is below $100\,\%$, because in practice part of the energy always becomes heat, for example in an electric resistor or in friction, and the heat spreads into the surroundings, from where it is hard to recover. When the purpose of a device is something other than heat, the efficiency stays clearly below $100\,\%$. In an electric heater the purpose is the heat itself, and the efficiency is close to $100\,\%$, but even that is below it, because some of the heat escapes to a useless place. The efficiencies of devices vary a lot:

| Device and its useful output | typical $\eta$ |
| --- | --- |
| incandescent lamp: light | $5\,\%$ |
| LED lamp: light | $30\,\%$ |
| kettle: warming of water | $90\,\%$ |
| electric motor: motion | $90\,\%$ |
| petrol engine: motion of a car | $25\,\%$ |
| solar panel: electricity | $20\,\%$ |

The values in the table are typical rounded values, not measurements of any particular device. The real efficiency depends on the model of the device and on the way it is used. The value for the petrol engine is typical for steady motorway driving; in city driving and at other small loads the efficiency is clearly lower. The efficiency of an electric motor changes little when it runs close to the power it was designed for.

## Formula: Efficiency
Efficiency $\eta$ (eta) is the ratio of the useful energy to the energy taken by the device. When the device runs at constant power, the same ratio is also obtained from powers:
```latex
\eta = \frac{E_\text{a}}{E_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```
where $\eta$ is the efficiency (a ratio, often given as a percentage), $E_\text{a}$ the useful energy given by the device (J), $E_\text{o}$ the energy taken by the device (J), $P_\text{a}$ the useful power (W) and $P_\text{o}$ the power taken by the device (W). A ratio is converted to a percentage by multiplying it by $100\,\%$, for example $0.30 \cdot 100\,\% = 30\,\%$. The multiplication does not change the number, because $1\,\% = 0.01$ and so $100\,\% = 100 \cdot 0.01 = 1$.

The ratio of the powers is the same as the ratio of the energies, because at constant power energy is power multiplied by time (chapter *Power P = ΔE/Δt*). While the device runs for a time $t$, the energies are $E_\text{a} = P_\text{a} \cdot t$ and $E_\text{o} = P_\text{o} \cdot t$, and the time cancels:
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

### Comparing two lamps
A lamp with a low efficiency needs a higher power to get the same useful output. For a light power of $3\,\text{W}$ an incandescent lamp needs $60\,\text{W}$ but an LED lamp only $10\,\text{W}$, because the efficiencies are $5\,\%$ and $30\,\%$. In the diagram the thicknesses of the arrows are on the same scale: the green arrows of the light power are equally thick, but the incoming arrow of the incandescent lamp is six times thicker.

<svg data-fig="pair" viewBox="0 0 600 450" role="img" aria-label="Two energy flow diagrams on the same scale. At the top, an incandescent lamp takes a power of 60 W and gives a light power of 3 W; the efficiency is 5 percent, and 57 W becomes heat. At the bottom, an LED lamp takes a power of 10 W and gives the same light power of 3 W; the efficiency is 30 percent, and 7 W becomes heat. In both, the green arrow of light power is equally thick, but the incoming arrow of the LED lamp is one sixth of the incoming arrow of the incandescent lamp." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy24a-in" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="200" y2="0"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy24a-ok" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy24a-loss" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><linearGradient id="fy24b-in" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="200" y2="0"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy24b-ok" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy24b-loss" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <path d="M30,84 L200,84 L200,180.0 L30,180.0 Z" fill="url(#fy24a-in)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,84 L500,84 L500,76 L532,86.4 L500,96.8 L500,88.8 L200,88.8 Z" fill="url(#fy24a-ok)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,88.8 C290,88.8 230,124 330,124 L500,124 L500,116 L532,169.6 L500,223.2 L500,215.2 L330,215.2 C230,215.2 290,180.0 200,180.0 Z" fill="url(#fy24a-loss)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="30" y="11.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{incandescent lamp}$</div></foreignObject>
  <foreignObject x="30" y="43.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 60\,\text{W}$</div></foreignObject>
  <foreignObject x="30" y="195.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
  <foreignObject x="257" y="41.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{light})$</div></foreignObject>
  <foreignObject x="247" y="230.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 57\,\text{W}\ (\text{heat})$</div></foreignObject>
  <line x1="30" y1="268" x2="570" y2="268" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="30" y="281.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{LED lamp}$</div></foreignObject>
  <foreignObject x="30" y="313.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 10\,\text{W}$</div></foreignObject>
  <path d="M30,352 L200,352 L200,368.0 L30,368.0 Z" fill="url(#fy24b-in)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,352 L500,352 L500,344 L532,354.4 L500,364.8 L500,356.8 L200,356.8 Z" fill="url(#fy24b-ok)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,356.8 C290,356.8 230,386 330,386 L500,386 L500,378 L532,391.6 L500,405.2 L500,397.2 L330,397.2 C230,397.2 290,368.0 200,368.0 Z" fill="url(#fy24b-loss)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="257" y="309.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{light})$</div></foreignObject>
  <foreignObject x="30" y="383.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 30\,\%$</div></foreignObject>
  <foreignObject x="257" y="412.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 7\,\text{W}\ (\text{heat})$</div></foreignObject>
</svg>

In a diagram drawn to scale you can see the efficiency directly: it is the thickness of the useful arrow as a share of the thickness of the incoming arrow. If the incoming arrow is $5.0\,\text{cm}$ thick and the useful arrow $4.0\,\text{cm}$, the efficiency is $4.0 : 5.0 = 0.80$, that is, $80\,\%$.

## Worked example
A kettle has an efficiency of $90\,\%$ and takes a power of $2.0\,\text{kW}$ from the electricity grid. The kettle is on for $3.0\,\text{min}$. How much electrical energy becomes losses, that is, heat that does not warm the water?

<!-- vaihe -->

**Known and unknown.** Efficiency $\eta = 90\,\%$, power taken $P_\text{o} = 2.0\,\text{kW}$ and running time $t = 3.0\,\text{min}$. We want the loss energy $E_\text{h}$.

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

**Result.** The energy that becomes losses is $36\,000\,\text{J} = 36 \cdot 1000\,\text{J} = 36\,\text{kJ}$. The result is given with two significant figures, because the initial values $90\,\%$, $2.0\,\text{kW}$ and $3.0\,\text{min}$ are given to two figures.

<!-- vaihe -->

**Reasonableness.** The losses must be $100\,\% - 90\,\% = 10\,\%$ of the energy taken, and the energy taken is $360\,000\,\text{J} = 360 \cdot 1000\,\text{J} = 360\,\text{kJ}$, so $0.10 \cdot 360\,\text{kJ} = 36\,\text{kJ}$. In addition, the useful energy and the losses add up to the energy taken: $324\,\text{kJ} + 36\,\text{kJ} = 360\,\text{kJ}$.

## Common misconception
Many people think that energy disappears in the losses. However, energy is conserved in every device. The energy leaving an incandescent lamp is equal to the energy entering it: $3\,\text{W}$ of light and $57\,\text{W}$ of heat make $60\,\text{W}$ in total. A loss only means that part of the energy ended up in a form that is of no use.

Another mistake is to think that a high-power device is efficient. Efficiency is a ratio, not an amount. A $100\,\text{W}$ incandescent lamp gives $5\,\text{W}$ of light and a $60\,\text{W}$ lamp $3\,\text{W}$, but both have an efficiency of $5\,\%$. A high-power device uses more energy, but power does not tell what share of the energy is useful.

## Summary
- Efficiency is the share of useful energy in the energy taken by the device: $\eta = \tfrac{E_\text{a}}{E_\text{o}} = \tfrac{P_\text{a}}{P_\text{o}}$. It is often given as a percentage and is below $100\,\%$ (almost $100\,\%$ for an electric heater).
- Energy is conserved: $E_\text{o} = E_\text{a} + E_\text{h}$. Losses are usually heat that spreads into the surroundings.
- In an energy flow diagram the thickness of an arrow is proportional to energy or power, and efficiency is the share of the useful arrow in the incoming arrow.
- The efficiency of a device that runs steadily does not depend on running time, because the time cancels from the ratio of the energies. The way the device is used can change it: for example, the efficiency of a petrol engine is clearly lower at a small load.
