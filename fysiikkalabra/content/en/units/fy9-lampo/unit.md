# Heat and changes of state

> **Why** does it take so long to melt snow into drinking water over a campfire, although the snow is only a little below freezing? Which takes more energy: melting it or heating the meltwater to boiling?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a sunny winter day in Lapland. On the left is a log lean-to shelter with snow on its roof. In front of the shelter a campfire burns in a ring of stones, and above it a black, sooty pot full of snow hangs from a tripod. Steam rises from the pot. Beside the campfire is a bucket of snow. In the background are snowy fells and spruces." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-lampo-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

In thermal physics three concepts must be kept apart. **Temperature** describes how vigorous the thermal motion of the particles is. **Internal energy** is the sum of the kinetic energy of the particles and the energy of their interactions, so it also depends on the amount of substance and on its state. **Heat** is the transfer of energy because of a temperature difference: a body has a temperature and internal energy, but it has no heat.

```pysahdy
A hot cup of coffee has a temperature and internal energy. Does it also have heat?
---
No. Heat is the transfer of energy because of a temperature difference, so it exists only during the transfer.
```

Every problem of the lesson comes back to conservation of energy. Heat transferred to a substance either raises its temperature or changes its state, and as the temperature rises the substance also expands. In an isolated system the heat released by the hot part equals the heat received by the cold part. The temperature of a house stays constant when the power coming in equals the power going out.

<svg data-fig="kartta" viewBox="0 0 380 784" role="img" aria-label="Recognition chart: how do I tell which law to use? Ask what happens to the substance and see which sign in the task fits. Temperature changes, state does not: heating, the quantity of heat is specific heat capacity times mass times the change of temperature. Ice melts or water freezes: heat of fusion, the quantity of heat is the specific heat of fusion times mass. Water boils or steam condenses: heat of vaporisation, the quantity of heat is the specific heat of vaporisation times mass. Insulated vessel, mixing: thermal equilibrium, the heat released equals the heat absorbed. The length of an object changes: thermal expansion, the length is the original length times one plus the coefficient of linear expansion times the change of temperature. The volume of a liquid changes: thermal expansion, the volume is the original volume times one plus the coefficient of volume expansion times the change of temperature. Heat conducts through a wall: the U-value, the power is the U-value times the area times the temperature difference." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{what happens to the substance?}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{temperature changes, state does not}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{heating}$</div></foreignObject>
  <rect x="232" y="142" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="144" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = cm\Delta T$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{ice melts or water freezes}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="206" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{heat of fusion}$</div></foreignObject>
  <rect x="262" y="228" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="230" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = sm$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{water boils or steam condenses}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="206" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{heat of vaporisation}$</div></foreignObject>
  <rect x="262" y="314" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="316" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = rm$</div></foreignObject>
  <line x1="14" y1="407" x2="30" y2="407" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{insulated vessel, mixing}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{thermal equilibrium}$</div></foreignObject>
  <rect x="112" y="430" width="250" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="116" y="432" width="242" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q_\text{released} = Q_\text{absorbed}$</div></foreignObject>
  <line x1="14" y1="523" x2="30" y2="523" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="472" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="482.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{length of an object changes}$</div></foreignObject>
  <line x1="40" y1="512" x2="362" y2="512" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="517" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{thermal expansion}$</div></foreignObject>
  <rect x="172" y="546" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="548" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$l = l_0(1 + \alpha\Delta T)$</div></foreignObject>
  <line x1="14" y1="639" x2="30" y2="639" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="588" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="598.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{volume of a liquid changes}$</div></foreignObject>
  <line x1="40" y1="628" x2="362" y2="628" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="633" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{thermal expansion}$</div></foreignObject>
  <rect x="172" y="662" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="664" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$V = V_0(1 + \gamma\Delta T)$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{heat conducts through a wall}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="166" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{U-value}$</div></foreignObject>
  <rect x="222" y="748" width="140" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="226" y="750" width="132" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$P = UA\Delta T$</div></foreignObject>
</svg>

In the exam, follow the energy first: where it comes from, where it goes and whether the state changes on the way. Only then choose the formula.

## Formula: Quantity of heat and energy balance

### Temperature and internal energy

```latex
T = \theta + 273.15
```

where $T$ is the temperature in kelvins ($\text{K}$) and $\theta$ in degrees Celsius (${}^\circ\text{C}$). A temperature difference is the same in kelvins and in degrees Celsius, but ratios of temperatures are calculated in kelvins. Internal energy is changed by heat and work:

```kaavat
first law of thermodynamics :: \Delta U = Q + W
```

where $\Delta U$ is the change in internal energy, $Q$ the quantity of heat transferred to the system and $W$ the work done on the system, all in joules. Energy coming into the system is positive. The equation holds when the kinetic and potential energy of the system do not change.

### Heating and change of state

```kaavat
heat transferred :: Q = cm\Delta T
```

where $c$ is the specific heat capacity ($\text{J/(kg}\cdot\text{K)}$), $m$ the mass ($\text{kg}$) and $\Delta T$ the change in temperature ($\text{K}$). The formula holds only when the state does not change. In melting and vaporisation

```kaavat
heat of fusion :: Q = sm
heat of vaporisation :: Q = rm
```

where $s$ is the specific latent heat of fusion and $r$ the specific latent heat of vaporisation ($\text{J/kg}$). At constant pressure the temperature of a pure substance stays constant during the change, because the energy increases the interaction energy of the particles. The same energy is released in solidification and condensation. For water $c = 4190\,\text{J/(kg}\cdot\text{K)}$, for ice $c = 2100\,\text{J/(kg}\cdot\text{K)}$, $s = 334\,\text{kJ/kg}$ and $r = 2260\,\text{kJ/kg}$.

```pysahdy
When ice melts, energy is transferred to it, but its temperature stays constant. Where does the energy go?
---
The energy increases the interaction energy of the particles and not their kinetic energy, so the temperature does not rise.
```

This gives the answer to the opening question. Warming a kilogram of snow from $-10\,{}^\circ\text{C}$ to $0\,{}^\circ\text{C}$ takes only $21\,\text{kJ}$, but melting it takes $334\,\text{kJ}$, almost as much as heating the meltwater to boiling, $419\,\text{kJ}$.

<svg data-fig="kayra" viewBox="0 0 600 380" role="img" aria-label="Graph to scale: the temperature T of a kilogram of snow in degrees Celsius as a function of the energy transferred Q in kilojoules. The snow warms from −10 degrees to 0 degrees when 21 kJ of energy has been transferred. Then the temperature stays at 0 degrees until 355 kJ of energy has been transferred: melting takes Q = s m = 334 kJ. The meltwater warms to 100 degrees when 774 kJ of energy has been transferred: this takes Q = c m ΔT = 419 kJ. After that the water boils at 100 degrees, and the graph continues as a horizontal arrow, because vaporisation Q = r m would still need 2260 kJ." style="max-width:100%;font-size:24px">
  <line x1="138.5" y1="318" x2="138.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="181.5" y1="318" x2="181.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224" y1="318" x2="224" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266.5" y1="318" x2="266.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="309.5" y1="318" x2="309.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="352" y1="318" x2="352" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="394.5" y1="318" x2="394.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="437.5" y1="318" x2="437.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="318" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="301" x2="480" y2="301" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="267" x2="480" y2="267" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="233.5" x2="480" y2="233.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="199.5" x2="480" y2="199.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="165.5" x2="480" y2="165.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="131.5" x2="480" y2="131.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="98" x2="480" y2="98" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="318" x2="494" y2="318" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,318 L493,324 L493,312 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="319" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="138.5" y1="318" x2="138.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="181.5" y1="318" x2="181.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="224" y1="318" x2="224" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="266.5" y1="318" x2="266.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="244" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="309.5" y1="318" x2="309.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="352" y1="318" x2="352" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="329.5" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="394.5" y1="318" x2="394.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="437.5" y1="318" x2="437.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="415" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$800$</div></foreignObject>
  <line x1="480" y1="318" x2="480" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="301" x2="96" y2="301" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="286.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="89" y1="267" x2="96" y2="267" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="252.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="233.5" x2="96" y2="233.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="219" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="199.5" x2="96" y2="199.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="185" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="165.5" x2="96" y2="165.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="151" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="89" y1="131.5" x2="96" y2="131.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="117" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="89" y1="98" x2="96" y2="98" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="83.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <foreignObject x="512" y="303.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q\ (\text{kJ})$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="86" y="327.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,284 105,267 247.5,267 426,98 466.5,98" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="466.5" y1="98" x2="472" y2="98" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M484,98 L471,103.5 L471,92 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="96" cy="284" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <circle cx="105" cy="267" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <circle cx="247.5" cy="267" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <circle cx="426" cy="98" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <path d="M105,254 V247 H247.5 V254" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="147" y="178" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = sm$</div></foreignObject>
  <foreignObject x="128.5" y="210.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$= 334\,\text{kJ}$</div></foreignObject>
  <path d="M247.5,273.5 V280.5 H426 V273.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="272" y="285" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = cm\Delta T = 419\,\text{kJ}$</div></foreignObject>
  <foreignObject x="422" y="59.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$Q = rm$</div></foreignObject>
</svg>

### Thermal balance

In an insulated container energy is conserved:

```latex
Q_\text{released} = Q_\text{received}
```

When ice and water are mixed, first compare whether the heat the water releases as it cools to $0\,{}^\circ\text{C}$ is enough to warm the ice to $0\,{}^\circ\text{C}$ and melt it. If it is, all the ice melts and the final temperature is at least $0\,{}^\circ\text{C}$. If it is not, some ice is left and the temperature is exactly $0\,{}^\circ\text{C}$. Very cold ice can also freeze some or all of the water.

```pysahdy
Water and ice are mixed, and the heat given out by the water is not enough to melt all the ice. What is the final temperature?
---
Some ice is left, and the temperature is exactly $0\,{}^\circ\text{C}$.
```

### Expansion and heat transfer

```kaavat
linear thermal expansion :: l = l_0(1 + \alpha\Delta T)
volume thermal expansion :: V = V_0(1 + \gamma\Delta T)
```

where $\alpha$ and $\gamma$ are the coefficients of linear and volume expansion ($1/\text{K}$), $l_0$ and $V_0$ the original length and volume and $l$ and $V$ the length and volume after the change in temperature $\Delta T$. The changes are $\Delta l = \alpha l_0 \Delta T$ and $\Delta V = \gamma V_0 \Delta T$. For solids the formulas hold up to a change in temperature of about $100\,\text{K}$, and the $\gamma$ of a liquid is usable only near the temperature given in the table. Water is an exception: its density is greatest at about $4\,{}^\circ\text{C}$.

Heat is transferred by conduction, convection and radiation, with a net flow from the warmer body to the colder one. The power conducted through a building element is

```latex
P = UA\Delta T
```

where $U$ is the U-value ($\text{W/(m}^2\cdot\text{K)}$), $A$ the area ($\text{m}^2$) and $\Delta T$ the difference between the indoor and outdoor temperatures ($\text{K}$). The formula holds when the temperatures stay constant.

## Common mistakes {Virheet}

- **Heat and temperature mixed up.** "The coffee contains a lot of heat" means internal energy in physics. Heat is energy that is transferred.
- **$Q = cm\Delta T$ in a change of state.** During melting the temperature does not change, but the energy $sm$ is used.
- **The final temperature as an average.** The initial temperatures are weighted by the heat capacities $cm$, and ice also needs the latent heat of fusion.
- **Kelvins in the wrong place.** The number $273$ is not added to a temperature difference, but ratios of temperatures need kelvins.
- **A hole shrinks when heated.** A body expands like an enlarged photograph, so a hole gets bigger too.
- **Cold "flows" in.** Energy flows from warm to cold. Cold is neither a substance nor energy.
- **Losses are forgotten.** In a measurement some of the energy is transferred to the surroundings. Always think about which way a loss changes the result.

## Review if needed {Kertaa}

- Temperature and the kelvin scale: [*Thermodynamic system, state variables and temperature*](fy3-3.html). Internal energy and heat: [*Internal energy, heat and conservation of energy*](fy3-5.html).
- Quantity of heat and thermal balance: [*Heating and cooling of matter*](fy3-6.html). Melting and vaporisation: [*Changes of state*](fy3-7.html).
- Ice and water in the same container: [*Thermal balance during a change of state*](fy3-14.html). Change in length and volume: [*Thermal expansion*](fy3-8.html).
- Conduction, convection, radiation and the U-value: [*Heat transfer, energy balance and climate change*](fy3-12.html).
