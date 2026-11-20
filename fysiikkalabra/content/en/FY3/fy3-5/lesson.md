# Internal energy, heat and conservation of energy

> **Why** does a bicycle pump get hot when you pump up a tyre, even though nothing is heating the pump?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: hands push the handle of a foot pump down, and a hose leads air into a bicycle tyre. The lower part of the pump has warmed up, shown by an orange glow and wavy lines." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
In chapter *Work and energy*, work was described as a way of transferring energy, and Joule's experiment showed that mechanical work can heat water: the work done by the weight increased the internal energy of the water, even though the water was not heated. Water does not contain "heat". The internal energy $U$ of a system is the sum of the kinetic energy of its particles and the energy of the interactions between the particles. In chapter *Forms of energy and conservation of energy*, this energy was called thermal energy; a more precise name is internal energy. Temperature describes how strongly the particles move because of thermal motion: in a gas, it tells you the average kinetic energy of the particles. When the temperature of a substance rises and its state of matter does not change, the particles move more strongly and the internal energy increases. Even so, temperature and internal energy are not the same thing, because when the state of matter changes, the internal energy changes even though the temperature stays the same: when, for example, pure ice melts at normal pressure, the internal energy increases, but the temperature stays at $0\,{}^\circ\text{C}$. Internal energy also depends on the amount of substance: a big lake contains much more internal energy than a cup of hot tea, even though the lake is colder.

```pysahdy
Pure ice melts at normal pressure. What happens to its internal energy and its temperature?
---
The internal energy increases, but the temperature stays at $0\,{}^\circ\text{C}$, because temperature and internal energy are not the same thing.
```

You can change the internal energy of a system in two ways. The first is work: when the piston of a pump compresses air, the surroundings do work on the gas, and the internal energy of the gas increases, because the moving piston hits the particles like a bat hits a ball and they bounce off faster. In the simulation you can see this at the particle level. This is why the pump gets hot. The second is heat: when two objects at different temperatures touch, energy transfers by itself from the hotter one to the colder one until the temperatures are the same. Energy transferred in this way is called heat, and the amount of energy transferred is the quantity of heat $Q$. So heat is a transfer of energy, not a property of matter: an object has a temperature and internal energy, but it does not have heat.

<svg data-fig="two-ways" viewBox="0 0 600 316" role="img" aria-label="Two ways to change internal energy (schematic, not to scale). On the left, a piston is pushed into the cylinder and does work W on the air, and the air particles move faster. On the right, a hot and a cold object touch, and a quantity of heat Q is transferred from the hot one to the cold one." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-two-ways.webp" x="0" y="0" width="600" height="327.5" preserveAspectRatio="none"/>
  <foreignObject x="131" y="13.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{work}$</div></foreignObject>
  <foreignObject x="421" y="13.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat}$</div></foreignObject>
  <foreignObject x="50" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="108.5" y="261.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{air heats up}$</div></foreignObject>
  <foreignObject x="359.5" y="159.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hot}$</div></foreignObject>
  <foreignObject x="473" y="159.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{cold}$</div></foreignObject>
  <foreignObject x="432" y="43.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="357" y="261.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{from hot to cold}$</div></foreignObject>
</svg>

```pysahdy
Someone says that a hot cup of tea contains a lot of heat. Is the claim correct in physics?
---
No. The cup has internal energy. Heat is energy transferred from the hotter object to the colder one, and an object does not have heat.
```

Energy is conserved. When energy is transferred into a system as heat or work and the kinetic or potential energy of the system does not change, its internal energy increases by exactly the amount of energy transferred, and when energy is transferred out, the internal energy decreases by the same amount. This is the first law of thermodynamics: the law of conservation of energy written for heat and work. An isolated system is a closed system into which, and out of which, no energy is transferred either as heat or as work. Its total energy stays constant, even if energy changes form inside it.

<figure class="unit-photo"><img src="pics/fy3/glowing-metal-furnace.webp" alt="A piece of metal glowing orange seen through the opening of an industrial furnace."><figcaption>Heated metal glows in a furnace. When the metal is heated, its internal energy increases.</figcaption></figure>

## Formula: First law of thermodynamics
The change in internal energy is the sum of the quantity of heat transferred into the system and the work done on the system:
```kaavat
first law of thermodynamics :: \Delta U = Q + W
```
where $\Delta U$ is the change in internal energy (J), $Q$ is the quantity of heat transferred into the system (J) and $W$ is the work done on the system by the surroundings (J). The signs tell you the direction: $Q$ is positive when heat is transferred into the system and negative when it is transferred out; $W$ is positive when the surroundings do work on the system (for example, compress a gas) and negative when the system does work on the surroundings (the gas expands and pushes the piston). All the terms are in joules, the same unit as work in chapter *Work and energy*, and the work done by a piston on a gas is calculated in the same way as there, as the product of force and distance.

<svg data-fig="energy-balance" viewBox="0 0 600 300" role="img" aria-label="Energy diagram: a quantity of heat Q and work W enter the system, and the internal energy of the system changes by their sum. Energy transferred out is negative." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-energy-balance.webp" x="9.9" y="9.9" width="591.1" height="307.9" preserveAspectRatio="none"/>
  <foreignObject x="258.5" y="103.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{system}$</div></foreignObject>
  <foreignObject x="258.5" y="151.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta U = Q + W$</div></foreignObject>
  <foreignObject x="75" y="51.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat}\ Q$</div></foreignObject>
  <foreignObject x="75" y="209.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{work}\ W$</div></foreignObject>
  <foreignObject x="430.5" y="87.5" width="115" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q < 0\ \text{or}\ W < 0$</div></foreignObject>
  <foreignObject x="465.5" y="163.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{out}$</div></foreignObject>
  <foreignObject x="158.5" y="247.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in positive, out negative}$</div></foreignObject>
</svg>

<svg data-fig="work-sign" viewBox="0 0 600 316" role="img" aria-label="The sign of work (schematic, not to scale). On the left, the piston is pushed in and the gas is compressed: the surroundings do work on the gas, so W is positive. On the right, the gas pushes the piston out and expands: the gas does work on the surroundings, so W is negative." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-work-sign.webp" x="1.2" y="2.5" width="597" height="322.1" preserveAspectRatio="none"/>
  <foreignObject x="102.5" y="13.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{compression}$</div></foreignObject>
  <foreignObject x="395" y="13.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{expansion}$</div></foreignObject>
  <foreignObject x="152.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W > 0$</div></foreignObject>
  <foreignObject x="432.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W < 0$</div></foreignObject>
  <foreignObject x="58.5" y="269.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{surroundings do work}$</div></foreignObject>
  <foreignObject x="382.5" y="269.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas does work}$</div></foreignObject>
</svg>

```pysahdy
A gas expands and pushes a piston, so it does work of $30\,\text{J}$ on the surroundings. No heat is transferred to or from the gas. By how much does the internal energy of the gas change?
---
The gas does work on the surroundings, so $W = -30\,\text{J}$, and $Q = 0$. So $\Delta U = Q + W = -30\,\text{J}$: the internal energy decreases by $30\,\text{J}$.
```

## Worked example
A pump cylinder contains air. The piston is pushed down, so the surroundings do $150\,\text{J}$ of work on the air. At the same time, a quantity of heat of $40\,\text{J}$ is transferred from the warming air through the cylinder walls to the surroundings. By how much does the internal energy of the air change?

<!-- vaihe -->

**Given and find.** The air is the system. The surroundings do work on the system, so $W = +150\,\text{J}$. Heat is transferred out of the system, so $Q = -40\,\text{J}$.

The quantity to find is the change in internal energy $\Delta U$.

<!-- vaihe -->

**Principle.** Energy is conserved: the internal energy of the system changes by exactly the amount of energy transferred into it as heat and work. This is the first law of thermodynamics, and it applies because the air is a clearly bounded system, and energy crosses its boundary only as work and heat.

<!-- vaihe -->

**Rearranged formula.** In the first law, the quantity to find $\Delta U$ is already alone on the left-hand side, so the equation does not need rearranging:

```latex
\begin{aligned}
&\Delta U = Q + W
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None needed: both $Q$ and $W$ are given in joules, and the result is wanted in joules. The signs, however, must be decided: energy into the system is positive and energy out of the system is negative.

<!-- vaihe -->

**Substitution.** Substitute the values with their signs:

```latex
\begin{aligned}
&\Delta U = Q + W \\
&= -40\,\text{J} + 150\,\text{J} \\
&= 110\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The internal energy of the air increases by $110\,\text{J}$. The result is given in whole joules, because both the work and the heat were given in whole joules.

<!-- vaihe -->

**Reasonableness.** The work brought $150\,\text{J}$ into the air and only $40\,\text{J}$ left as heat, so the internal energy must increase and the temperature of the air must rise. If the same $150\,\text{J}$ of work were done so slowly that all the energy from the work had time to leave as heat, then $Q = -150\,\text{J}$ and $\Delta U = 0$, and the temperature would not change. Now less heat leaves, so the result lies between this limiting case and the work alone, $150\,\text{J}$.

## Common misconception
In everyday language we say that an object "has heat" or that heat is "stored". In physics, heat is the transfer of energy because of a temperature difference, and what is stored in an object is internal energy. Another mistake is to treat temperature and internal energy as the same thing: a hot spark has a temperature of thousands of degrees, but its internal energy is small, because it contains very little matter. A third mistake is to think that internal energy can be changed only by heating. The air in a pump gets hot without any heat source, because work is done on it.

## Summary
- The internal energy $U$ is the sum of the kinetic energy of the particles of a system and the energy of the interactions between the particles. It increases when the temperature rises while the state of matter stays the same, and it also depends on the amount of substance. Temperature and internal energy are not the same thing.
- Heat is the transfer of energy from hotter to colder because of a temperature difference; the energy transferred is the quantity of heat $Q$. An object does not "have heat".
- Heat and work change internal energy: $\Delta U = Q + W$. Energy transferred in is positive and energy transferred out is negative.
- Energy is conserved: this is the first law of thermodynamics. The total energy of an isolated system stays constant.
