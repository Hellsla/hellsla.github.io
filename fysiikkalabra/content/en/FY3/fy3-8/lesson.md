# Thermal expansion

> **Why** is there a comb-shaped steel joint at the end of a long bridge, which makes the car tyres thump as they cross it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a car drives away from the viewer along a long bridge. In the foreground a comb-shaped steel joint crosses the road, its teeth interlocking and leaving a gap between them to allow for the thermal expansion of the bridge." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
Almost all substances expand when they are heated and contract when they are cooled. This phenomenon is called **thermal expansion**.

<figure class="unit-photo"><img src="pics/fy3/bridge-expansion-joint.webp" alt="A metal expansion joint runs across the deck of a bridge, with patterned steel plates and a yellow painted stripe. The bridge railing is in the background."><figcaption>An expansion joint of the Kruunuvuori bridge in Helsinki in August 2026, before renovation. The expansion joint gives the bridge structures room to move, for example when the temperature changes.</figcaption></figure>

### Why does a substance expand?
The micro model explains thermal expansion. In a solid the particles vibrate around their equilibrium positions. When the temperature rises, the vibration gets stronger.

It is easier for the particles to move apart than to be squeezed closer: particles pressed close together repel each other strongly, but the attraction between particles moving apart weakens gradually. So a particle swings farther from its neighbour than closer to it, and for more strongly vibrating particles the **average distance grows**. When all the gaps between the particles grow, the whole object expands.

<svg data-fig="particles" viewBox="0 0 600 316" role="img" aria-label="The same row of particles cold and warm. When warm, the particles vibrate more strongly and their average distance d is greater than the distance d₀ of the cold row, but the particles are the same size. The change in distance is drawn exaggerated." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-particles.webp" x="3.8" y="1.3" width="606.1" height="330.8" preserveAspectRatio="none"/>
  <foreignObject x="20" y="85.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{cold}$</div></foreignObject>
  <foreignObject x="198.5" y="33.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d_0$</div></foreignObject>
  <foreignObject x="20" y="207.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{warm}$</div></foreignObject>
  <foreignObject x="196" y="155.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d > d_0$</div></foreignObject>
  <foreignObject x="131" y="281.5" width="457" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{particles the same size, gaps exaggerated}$</div></foreignObject>
</svg>

```pysahdy
The particles do not grow when an object is heated. Why does the object still expand?
---
When heated, the vibration of the particles becomes stronger and their average distance increases. When all the gaps between particles grow, the whole object expands.
```

### Thermal expansion in everyday life
The change is small but powerful. A steel rod gets longer by only about one hundred-thousandth of its length for each kelvin, but if the ends of the rod are fixed, the expanding steel pushes on them with an enormous force. That is why long structures have expansion joints. A steel bridge deck is shorter in a winter frost than in a summer heatwave, and the comb-shaped joint at the end of the bridge lets the deck move freely. For the same reason electric power lines hang lower in a heatwave than in a frost.

An object expands in all directions in the same proportion, as when a photograph is enlarged. A hole in a plate also gets bigger when the plate warms up. This is used in a shrink fit: a heated steel ring is slipped onto an axle, and as it cools it is pressed tightly in place.

```pysahdy
A steel plate has a round hole. The plate is heated. Does the hole get smaller or larger?
---
The hole gets larger, because an object expands in all directions in the same proportion, as when a photograph is enlarged.
```

### Thermal expansion of different substances
Different substances expand differently. A bimetallic strip, in which two different metals are joined together, bends when it warms up, because one metal lengthens more. Such a strip opens and closes an electric circuit in old-style thermostats.

Liquids usually expand clearly more than solids, and gases much more still. The particles of a liquid do not stay in place, and the interactions between them are weaker than in a solid, so a rise in temperature moves them farther apart. The particles of a gas are far apart and almost free, so at constant pressure the volume of a gas grows much more. The volume of a gas also depends on pressure, and we return to this in the chapter *Changes of state of a gas and Boyle's law*. A liquid thermometer is based on the expansion of a liquid: when the temperature rises, the liquid column rises in a thin tube.

Water is an exception: between $0\,{}^\circ\text{C}$ and $4\,{}^\circ\text{C}$ it contracts when it warms up, so its density is greatest at about $4\,{}^\circ\text{C}$. The densest, 4-degree water sinks to the bottom, and colder water stays at the surface and freezes. That is why a lake freezes from the surface, and even in winter there is water of about four degrees at the bottom, where fish survive.

```pysahdy
At what temperature is water densest, and so where does the densest water in a lake sink to?
---
Water is densest at about $4\,{}^\circ\text{C}$, and the densest water sinks to the bottom of the lake.
```

## Formula: Thermal expansion of length and volume
When the temperature of an object changes by $\Delta T$, its length is
```kaavat
linear thermal expansion :: l = l_0(1 + \alpha \Delta T)
```
where $l$ is the length after the change in temperature (m), $l_0$ is the original length (m), $\alpha$ is the coefficient of linear expansion (1/K) and $\Delta T$ is the change in temperature (K). The coefficient of linear expansion $\alpha$ tells you what fraction of its length an object lengthens when its temperature rises by $1\,\text{K}$. The number 12 in the table means that $\alpha = 12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$.

Subtracting the original length from the new length gives the change in length, the form used in this chapter's calculations:
```latex
\Delta l = l - l_0 = \alpha l_0 \Delta T
```
So the change is proportional to the original length: a rod twice as long has twice as many gaps between particles, so it lengthens twice as much. When the object cools, $\Delta T$ is negative, so $\Delta l$ is also negative, that is, the object gets shorter.

The volume of liquids (and of gases at constant pressure) is calculated in the same way:
```kaavat
volume thermal expansion :: V = V_0(1 + \gamma \Delta T)
```
where $V$ is the volume after the change in temperature (m³), $V_0$ is the original volume (m³) and $\gamma$ is the coefficient of volume expansion (1/K). Likewise, the change in volume is $\Delta V = V - V_0 = \gamma V_0 \Delta T$.

For a solid $\gamma \approx 3\alpha$, because an object expands in all three directions: length, width and height each grow in proportion $\alpha \Delta T$, and when the changes are small, the relative growth in volume is almost the sum of these, $3\alpha \Delta T$. The formulas are good models when the change in temperature is moderate. For solids that means, for example, at most about a hundred kelvins. For liquids, especially water, the coefficient $\gamma$ changes clearly with temperature, so the values in the table at $20\,{}^\circ\text{C}$ are used only close to $20\,{}^\circ\text{C}$.

<svg data-fig="volume-expansion" viewBox="0 0 600 350" role="img" aria-label="Thermal expansion of the volume of a liquid. The same amount of liquid in a flask with a thin tube as its neck: when cold, the volume of the liquid is V₀ and the surface is lower; when warm, the liquid has expanded and the surface rises in the thin tube. The change in volume ΔV is marked in the tube. The expansion is drawn exaggerated." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-volume-expansion.webp" x="0" y="-1.2" width="600" height="360" preserveAspectRatio="none"/>
  <foreignObject x="102.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{cold, } T_0$</div></foreignObject>
  <foreignObject x="395" y="11.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$T_0 + \Delta T$</div></foreignObject>
  <foreignObject x="39" y="243.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V_0$</div></foreignObject>
  <foreignObject x="190" y="175.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{surface}$</div></foreignObject>
  <foreignObject x="319" y="243.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V_0$</div></foreignObject>
  <foreignObject x="474" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\Delta V$</div></foreignObject>
</svg>

| Substance | $\alpha$ (10⁻⁶ 1/K) |
| --- | --- |
| steel | 12 |
| aluminium | 23 |
| copper | 17 |
| ordinary glass | 9 |
| borosilicate glass | 3.3 |

| Substance ($20\,{}^\circ\text{C}$) | $\gamma$ (10⁻³ 1/K) |
| --- | --- |
| water | 0.21 |
| ethanol | 1.1 |
| petrol | 0.95 |
| air (at constant pressure) | 3.4 |

<svg data-fig="rod-expansion" viewBox="0 0 600 300" role="img" aria-label="The same rod cold and warm: the warm rod is longer, and the change in length Δl is marked at the end of the rod. The rod is fixed to a wall at its left end. The expansion is drawn exaggerated." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-rod-expansion.webp" x="5" y="5" width="597" height="309.7" preserveAspectRatio="none"/>
  <foreignObject x="66" y="23.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{cold, temperature } T_0$</div></foreignObject>
  <foreignObject x="233.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l_0$</div></foreignObject>
  <foreignObject x="66" y="111.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{warm, temperature } T_0 + \Delta T$</div></foreignObject>
  <foreignObject x="250" y="153.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l_0 + \Delta l$</div></foreignObject>
  <foreignObject x="468.5" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta l$</div></foreignObject>
  <foreignObject x="330" y="271.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{expansion exaggerated}$</div></foreignObject>
</svg>

## Worked example
The deck of a steel bridge is $120\,\text{m}$ long. At the location the temperature varies during the year from a frost of $-30\,{}^\circ\text{C}$ to a heatwave of $+30\,{}^\circ\text{C}$, and the coefficient of linear expansion of steel is $12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$. By how much does the length of the deck change, that is, how much must the expansion joint give at least?

<!-- vaihe -->

**Given and find.** The length of the deck is $l_0 = 120\,\text{m}$, $\alpha = 12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$ for steel (given in the problem), the lowest temperature is $-30\,{}^\circ\text{C}$ and the highest $+30\,{}^\circ\text{C}$.

The question is the change $\Delta l$ in the length of the deck over the whole year.

<!-- vaihe -->

**Principle.** The vibration of the particles of a solid gets stronger when it warms up and their average distance grows, so the deck gets longer. Steel stays solid all year and the deck is free to expand, so the change in length is proportional to the initial length and the change in temperature: $\Delta l = \alpha l_0 \Delta T$.

<!-- vaihe -->

**Rearranged formula.** The quantity asked for is already alone on the left side of the formula, so the formula does not need rearranging:
```latex
\begin{aligned}
&\Delta l = \alpha l_0 \Delta T \\
&\Delta T = T_\text{max} - T_\text{min}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The change in temperature is the same in degrees Celsius and in kelvins, so $$\begin{aligned} &\Delta T \\ &= 30\,{}^\circ\text{C} - (-30\,{}^\circ\text{C}) \\ &= 60\,\text{K} \end{aligned}$$. The lengths are in metres, so $\Delta l$ comes out in metres; finally $1\,\text{m} = 1000\,\text{mm}$.

<!-- vaihe -->

**Substitution.** Substitute the values with their units:
```latex
\begin{aligned}
\Delta l &= \alpha l_0 \Delta T \\
&= 12 \cdot 10^{-6}\,\tfrac{1}{\text{K}} \cdot 120\,\text{m} \cdot 60\,\text{K} \\
&= 0.0864\,\text{m} \\
&= 86.4\,\text{mm}
\end{aligned}
```

<!-- vaihe -->

**Result.** The length of the deck changes by about $86\,\text{mm}$ during the year, so the expansion joint must give at least $87\,\text{mm}$. A minimum value is rounded to the safe side, up: $86.4\,\text{mm}$ → $87\,\text{mm}$. The result is given to two significant figures. The limiting data are the coefficient $12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$ and the difference of whole degrees $\Delta T = 60\,\text{K}$ (both have two figures); the length $120\,\text{m}$ has at least two figures and does not limit the result.

<!-- vaihe -->

**Reasonableness.** A rough estimate: $10^{-5}\,\tfrac{1}{\text{K}} \cdot 100\,\text{m} \cdot 60\,\text{K} = 60\,\text{mm}$, so the result is of the right order of magnitude. The deck gets almost nine centimetres longer by summer, because the temperature rises. That is only $\alpha \Delta T = 0.072\,\%$ of the length of the deck, but without an expansion joint the expanding steel would push on the ends of the bridge with such a large force that the structures would be damaged. That is why there is a comb-shaped joint at the end of the bridge, with teeth that slide between each other.

## Common misconception
Many people think that when a substance warms up, its particles themselves grow. In the micro model the particles stay the same size, and only their average distances grow. Another mistake is to think that a hole in a plate gets smaller because the plate supposedly expands from its edges towards the hole. The hole gets bigger in the same proportion as the plate does everywhere else. A third mistake is to assume that all substances always expand when they warm up: water contracts between $0\,{}^\circ\text{C}$ and $4\,{}^\circ\text{C}$, and when it freezes it expands. That is why ice floats and lakes freeze from the surface.

## Summary
- When a substance warms up, the vibration of its particles gets stronger and their average distance grows, so the substance expands.
- After a change in temperature the length is $l = l_0(1 + \alpha \Delta T)$ and the volume $V = V_0(1 + \gamma \Delta T)$. So the change in length is $\Delta l = \alpha l_0 \Delta T$ and the change in volume is $\Delta V = \gamma V_0 \Delta T$. For a solid $\gamma \approx 3\alpha$.
- Liquids expand more than solids, and gases much more than liquids.
- An object expands in all directions in the same proportion, so holes also get bigger.
- Water is an exception: its density is greatest at about $4\,{}^\circ\text{C}$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: railway rails in a heatwave. Heat shimmers above the rails, and at the joint between two rails there is a small gap to allow for thermal expansion." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
