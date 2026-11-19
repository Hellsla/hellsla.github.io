# Forms of energy and conservation of energy

> **Why** does a bouncing ball eventually come to rest on the floor?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a ball bounces across the wooden floor of a gym from left to right. The dashed arcs get lower bounce by bounce, and at the end the ball lies at rest on the floor. At each point of impact there is a small heat shimmer." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
**Energy** is a quantity used to describe what happens in a system when something moves, warms up, gives off light or changes its form. The symbol for energy is $E$ and its unit is the **joule**, $\text{J}$. The joule is a small unit, so energies are often given in kilojoules too: the prefix kilo means a thousand, so $1\,\text{kJ} = 1000\,\text{J}$.

Energy comes in many forms, and each form is called a **form of energy**. The form of energy tells you where the energy is stored or how it shows itself.

<figure class="unit-photo"><img src="pics/fy2/hydropower-plant-aerial.webp" alt="A hydroelectric power plant seen from above: a river flows on the left, a car park is in the middle and transformers and power line towers are at the bottom."><figcaption>The site of a hydroelectric power plant seen from above. In a hydroelectric plant the potential energy of water turns into kinetic energy in the turbine and into electrical energy in the generator.</figcaption></figure>

### Seven forms of energy
| Form of energy | What it is linked to | Example |
|---|---|---|
| **Potential energy** $E_\text{p}$ | The position of an object, here gravitational potential energy. The higher an object is and the greater its mass, the more potential energy it has. | A ball at the edge of a shelf can pick up speed as it falls. |
| **Kinetic energy** $E_\text{k}$ | The motion of an object. The faster an object moves and the greater its mass, the more kinetic energy it has. An object at rest has none. | A rolling ball |
| **Thermal energy** $E_\text{thermal}$ | The motion of the particles of a substance and the interactions between them. When an object warms up, its particles move more and its thermal energy increases. | A hot cup of coffee |
| **Chemical energy** | The chemical bonds of substances. The energy is released in, for example, combustion and metabolism. | Food, fuels and batteries |
| **Radiant energy** | Radiation: the energy is carried by radiation, also through a vacuum. | Sunlight |
| **Electrical energy** | Electric current: the energy is transferred by the current. | The electricity grid |
| **Nuclear energy** | Atomic nuclei. The energy is released in nuclear reactions. | A nuclear power plant and the Sun |

Thermal energy also depends on the amount of substance, so it is not the same thing as temperature. The word **heat**, on the other hand, means in physics energy that is *transferred* because of a temperature difference: the net transfer of energy is from the warmer object to the colder one. An object has thermal energy, and energy is transferred from one object to another as heat.

Potential energy and kinetic energy together make up **mechanical energy**, $E_\text{mech} = E_\text{p} + E_\text{k}$.

```pysahdy
A hot coffee cup cools down on the table. What does the physics word heat mean in this situation?
---
Heat is energy that transfers from the cup to the cooler air because of the temperature difference. At the same time the cup's thermal energy decreases.
```

<svg data-fig="energialajit" viewBox="0 0 600 396" role="img" aria-label="Schematic diagram: forms of energy with examples. Mechanical energy is potential energy (a ball at the edge of a cliff) and kinetic energy (a rolling ball). The picture also shows thermal energy (a hot coffee cup), chemical energy (a battery), radiant energy (the Sun), electrical energy (lightning) and nuclear energy (an atomic nucleus). The picture is schematic, not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-1-energialajit.webp" x="0" y="-1.2" width="600" height="401.2" preserveAspectRatio="none"/>
  <foreignObject x="46" y="5.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mechanical energy}$</div></foreignObject>
  <foreignObject x="99" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="243" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$v$</div></foreignObject>
  <foreignObject x="15" y="155.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potential}$</div></foreignObject>
  <foreignObject x="33.5" y="185.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="177.5" y="155.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kinetic}$</div></foreignObject>
  <foreignObject x="183.5" y="185.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="327.5" y="155.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{thermal}$</div></foreignObject>
  <foreignObject x="333.5" y="185.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="471" y="155.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{chemical}$</div></foreignObject>
  <foreignObject x="483.5" y="185.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="102.5" y="327.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{radiant}$</div></foreignObject>
  <foreignObject x="108.5" y="357.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="233.5" y="327.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{electrical}$</div></foreignObject>
  <foreignObject x="258.5" y="357.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="402.5" y="327.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{nuclear}$</div></foreignObject>
  <foreignObject x="408.5" y="357.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
</svg>

### Energy changes form
Energy does not stay in the same form. In a torch (flashlight), the chemical energy of the battery changes into electrical energy, and the bulb changes the electrical energy into light and thermal energy. In an incandescent bulb, most of the energy changes into thermal energy and only a small part into light.

<svg data-fig="energian-muuttuminen" viewBox="0 0 600 250" role="img" aria-label="Schematic diagram: energy changes in a torch (flashlight). The battery holds chemical energy. It changes into electrical energy, and the bulb changes the electrical energy into light and thermal energy. Most of it changes into thermal energy, so the arrow for thermal energy is wider. The picture is schematic, and the widths of the arrows are not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-1-energian-muuttuminen.webp" x="0" y="0" width="600" height="258.8" preserveAspectRatio="none"/>
  <foreignObject x="26" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{chemical}$</div></foreignObject>
  <foreignObject x="38.5" y="41.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="32.5" y="183.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <foreignObject x="138.5" y="11.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{electrical}$</div></foreignObject>
  <foreignObject x="163.5" y="41.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <foreignObject x="293" y="183.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{bulb}$</div></foreignObject>
  <foreignObject x="444" y="62.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{light}$</div></foreignObject>
  <foreignObject x="444" y="139.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{thermal}$</div></foreignObject>
  <foreignObject x="444" y="169.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
</svg>

There are similar changes everywhere. A plant changes the radiant energy of the Sun into chemical energy. A muscle changes chemical energy into kinetic energy and thermal energy. In a nuclear power plant, nuclear energy finally changes into electrical energy.

## Formula: Law of conservation of energy
In all these changes the total amount of energy stays the same: energy is neither created nor destroyed, but changes form or moves from one place to another. This is a universal principle of physics, the **law of conservation of energy**. We look at an **isolated system**, which receives no energy from outside and loses none to the outside. Then the total energy of the system is the same at the start and at the end:

```latex
E_\text{initial} = E_\text{final}
```

where $E_\text{initial}$ is the sum of the energies of all forms of energy in the system at the start and $E_\text{final}$ is their sum at the end. Both are given in joules ($\text{J}$).

The sum includes all forms of energy, thermal energy too. When a skateboarder slides from the edge of a half-pipe to the bottom and friction acts, the mechanical energy $E_\text{p} + E_\text{k}$ decreases, but the thermal energy $E_\text{thermal}$ increases by the same amount. The sum $E_\text{p} + E_\text{k} + E_\text{thermal}$ does not change. So friction does not create energy: it changes mechanical energy into thermal energy, and the wheels, the ramp and the air warm up a little.

```pysahdy
Friction makes a skateboarder's mechanical energy decrease by $50\,\text{J}$. What happens to the thermal energy if the system is isolated?
---
The thermal energy increases by $50\,\text{J}$. The total energy does not change, because energy is neither created nor destroyed.
```

<svg data-fig="sailyminen" viewBox="0 0 600 380" role="img" aria-label="Schematic diagram: a skateboarder in a half-pipe at three moments, with the energies at each moment as bars. At the start the skateboarder is at rest at the edge, and all the energy, 800 J, is potential energy. In the middle there is 300 J of potential energy, 450 J of kinetic energy and 50 J of thermal energy. At the bottom there is no potential energy, 700 J of kinetic energy and 100 J of thermal energy. The heights of the bars are to scale, and the total height of every bar corresponds to 800 joules, so there is the same amount of energy at every moment." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy21-hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#c92a2a"/><line x1="0" y1="0" x2="0" y2="8" stroke="#f2a69c" stroke-width="3"/></pattern></defs>
  <path d="M10,38 L20,38 Q100,146 180,38 L190,38 L190,106 L10,106 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M10,38 L20,38 Q100,146 180,38 L190,38" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M210,38 L220,38 Q300,146 380,38 L390,38 L390,106 L210,106 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M210,38 L220,38 Q300,146 380,38 L390,38" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M410,38 L420,38 Q500,146 580,38 L590,38 L590,106 L410,106 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M410,38 L420,38 Q500,146 580,38 L590,38" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <g transform="translate(20,37) rotate(53.5) scale(0.66)" stroke-linecap="round" stroke-linejoin="round"><rect x="-17" y="-9" width="34" height="4.2" rx="2.1" fill="#d9b26a" stroke="#a97a35" stroke-width="1.5"/><circle cx="-10" cy="-3.4" r="3.4" fill="#1f2933"/><circle cx="10" cy="-3.4" r="3.4" fill="#1f2933"/><path d="M-8,-9.5 L-4,-19 L1,-28 M9,-9.5 L7,-19 L1,-28" fill="none" stroke="#6c757d" stroke-width="4.4"/><path d="M1,-28 L4,-44" fill="none" stroke="#1971c2" stroke-width="7"/><path d="M4,-41 L-6,-34 M4,-41 L14,-36" fill="none" stroke="#e9c98a" stroke-width="3.2"/><circle cx="6" cy="-51" r="6.4" fill="#e9c98a"/><path d="M-0.4,-52 A6.4,6.4 0 0 1 12.4,-52 Z" fill="#1f2933"/></g>
  <rect x="45" y="164" width="44" height="128" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="99" y="213.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800\,\text{J}$</div></foreignObject>
  <g transform="translate(251,71) rotate(39.6) scale(0.66)" stroke-linecap="round" stroke-linejoin="round"><rect x="-17" y="-9" width="34" height="4.2" rx="2.1" fill="#d9b26a" stroke="#a97a35" stroke-width="1.5"/><circle cx="-10" cy="-3.4" r="3.4" fill="#1f2933"/><circle cx="10" cy="-3.4" r="3.4" fill="#1f2933"/><path d="M-8,-9.5 L-4,-19 L1,-28 M9,-9.5 L7,-19 L1,-28" fill="none" stroke="#6c757d" stroke-width="4.4"/><path d="M1,-28 L4,-44" fill="none" stroke="#1971c2" stroke-width="7"/><path d="M4,-41 L-6,-34 M4,-41 L14,-36" fill="none" stroke="#e9c98a" stroke-width="3.2"/><circle cx="6" cy="-51" r="6.4" fill="#e9c98a"/><path d="M-0.4,-52 A6.4,6.4 0 0 1 12.4,-52 Z" fill="#1f2933"/></g>
  <rect x="245" y="284" width="44" height="8" fill="url(#fy21-hatch)" stroke="#1f2933" stroke-width="2"/>
  <rect x="245" y="212" width="44" height="72" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="245" y="164" width="44" height="48" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="299" y="262.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$50\,\text{J}$</div></foreignObject>
  <foreignObject x="299" y="233.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$450\,\text{J}$</div></foreignObject>
  <foreignObject x="299" y="173.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$300\,\text{J}$</div></foreignObject>
  <g transform="translate(500,91) rotate(0.0) scale(0.66)" stroke-linecap="round" stroke-linejoin="round"><rect x="-17" y="-9" width="34" height="4.2" rx="2.1" fill="#d9b26a" stroke="#a97a35" stroke-width="1.5"/><circle cx="-10" cy="-3.4" r="3.4" fill="#1f2933"/><circle cx="10" cy="-3.4" r="3.4" fill="#1f2933"/><path d="M-8,-9.5 L-4,-19 L1,-28 M9,-9.5 L7,-19 L1,-28" fill="none" stroke="#6c757d" stroke-width="4.4"/><path d="M1,-28 L4,-44" fill="none" stroke="#1971c2" stroke-width="7"/><path d="M4,-41 L-6,-34 M4,-41 L14,-36" fill="none" stroke="#e9c98a" stroke-width="3.2"/><circle cx="6" cy="-51" r="6.4" fill="#e9c98a"/><path d="M-0.4,-52 A6.4,6.4 0 0 1 12.4,-52 Z" fill="#1f2933"/></g>
  <rect x="445" y="276" width="44" height="16" fill="url(#fy21-hatch)" stroke="#1f2933" stroke-width="2"/>
  <rect x="445" y="164" width="44" height="112" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="499" y="262.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$100\,\text{J}$</div></foreignObject>
  <foreignObject x="499" y="205.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$700\,\text{J}$</div></foreignObject>
  <foreignObject x="65" y="303.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{start}$</div></foreignObject>
  <foreignObject x="258.5" y="303.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{middle}$</div></foreignObject>
  <foreignObject x="477.5" y="303.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{end}$</div></foreignObject>
  <line x1="24" y1="164" x2="576" y2="164" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="183.5" y="129.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{total energy } E = 800\,\text{J}$</div></foreignObject>
  <line x1="30" y1="292" x2="570" y2="292" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="120" y="348" width="20" height="20" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="150" y="343.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <rect x="270" y="348" width="20" height="20" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="300" y="343.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <rect x="420" y="348" width="20" height="20" fill="url(#fy21-hatch)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="450" y="343.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{thermal}$</div></foreignObject>
</svg>

### Using up energy is changing energy
In everyday language energy is "used up", but in physics it does not run out. When a device uses energy, it changes energy from one form to another. Most often the largest part changes into thermal energy, which is transferred as heat into the surroundings and is hard to use any more. In short, people often say that energy "changes into heat". This is why it is worth saving energy even though it cannot be destroyed.

```pysahdy
A phone battery "runs out" as you use the phone. Where has the battery's energy gone?
---
It has not disappeared. The energy has changed into other forms, for example light and thermal energy, and most of it is transferred as heat into the surroundings.
```

## Worked example
A skateboarder starts from rest at the edge of a half-pipe. At the edge her potential energy is $840\,\text{J}$, when the zero level is the bottom of the half-pipe. At the bottom her kinetic energy is $0.72\,\text{kJ}$. The skateboarder, the half-pipe and the surroundings form an isolated system. How much energy has friction changed into thermal energy during the slide?

<!-- vaihe -->

**Given and find.** At the start the potential energy is $E_\text{p} = 840\,\text{J}$ and the kinetic energy is zero, because the skateboarder is at rest.

At the bottom the potential energy is zero and the kinetic energy is $E_\text{k} = 0.72\,\text{kJ}$.

We want the amount of mechanical energy $E_\text{thermal}$ that friction changes into thermal energy during the slide.

<!-- vaihe -->

**Principle.** The system is isolated, so energy is conserved: $E_\text{initial} = E_\text{final}$. At the start all the energy is potential energy. At the bottom it is divided between kinetic energy and thermal energy, into which friction has changed part of it.

<!-- vaihe -->

**Rearranged formula.** At the start there is only $E_\text{p}$, and at the end there are $E_\text{k}$ and $E_\text{thermal}$:
```latex
\begin{aligned}
E_\text{initial} &= E_\text{final} \\
E_\text{p} &= E_\text{k} + E_\text{thermal} \\
E_\text{thermal} &= E_\text{p} - E_\text{k}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The kinetic energy is given in kilojoules and the potential energy in joules. The prefix kilo means a thousand, so it is put in place of the unit: $E_\text{k} = 0.72\,\text{kJ} = 0.72 \cdot 1000\,\text{J} = 720\,\text{J}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
E_\text{thermal} &= E_\text{p} - E_\text{k} \\
&= 840\,\text{J} - 720\,\text{J} \\
&= 120\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** Friction changed $E_\text{thermal} = 120\,\text{J}$ into thermal energy. The result is rounded to tens of joules, because the kinetic energy $0.72\,\text{kJ}$ is given to the nearest ten joules and this limits the precision of the difference.

<!-- vaihe -->

**Reasonableness.** The thermal energy is positive and smaller than the initial energy $840\,\text{J}$, as it should be with friction. The energy is accounted for: $720\,\text{J} + 120\,\text{J} = 840\,\text{J} = E_\text{initial}$. Less than a fifth of the initial energy changed into thermal energy, which is a believable amount on a smooth half-pipe.

## Common misconception
Energy does not disappear or get used up. When a ball stops or a device uses energy, the energy has changed into another form, usually thermal energy that has been transferred as heat into the surroundings. Another mistake is to calculate only the mechanical energy. In motion with friction $E_\text{p} + E_\text{k}$ decreases, but the total energy stays the same when thermal energy is included. Friction does not create energy but changes it from one form to another.

## Summary
- The symbol for energy is $E$ and its unit is the joule $\text{J}$; $1\,\text{kJ} = 1000\,\text{J}$.
- The forms of energy are potential energy, kinetic energy (together mechanical energy), thermal energy, chemical energy, radiant energy, electrical energy and nuclear energy.
- Energy changes form and moves but is neither created nor destroyed: in an isolated system $E_\text{initial} = E_\text{final}$.
- Friction does not create energy but changes mechanical energy into thermal energy: $E_\text{p} + E_\text{k}$ decreases, but the total energy does not change.
- An object has thermal energy; heat is energy that is transferred because of a temperature difference, net from the warmer object to the colder one.
- Using up energy means changing it into a form that is hard to use, usually thermal energy.
