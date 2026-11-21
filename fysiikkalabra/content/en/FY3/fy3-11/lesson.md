# Work done by a gas and the heat engine

> **Why** does a thermal power plant get less than half of the energy of its fuel as electricity, and where does the rest of the energy go?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a condensing power plant on a lake shore. Power lines carry electricity away, a large cloud of steam rises from the cooling tower, and the condenser water is discharged into the lake warm, which shows as an orange zone in the water. Most of the energy of the fuel leaves as heat into the air and the water." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
When a gas expands and pushes a piston, it does work. The gas pushes the piston with a force $F = pA$, where $A$ is the area of the piston. If the piston moves a distance $s$ and the pressure stays the same, the work done by the gas is force times distance, $pAs$. The product $As$ is the change in the volume of the gas $\Delta V$, so the work done by the gas is $W = p\,\Delta V$. In the ($V$, $p$) graph it is the area between the graph and the $V$ axis, just like the work in an ($s$, $F$) graph. When the gas is compressed, the surroundings do compression work on the gas, and its size is calculated with the same formula. A gas that does work gives up energy, so its internal energy grows less than the heat brought to it.

<svg data-fig="piston-work" viewBox="0 0 600 330" role="img" aria-label="Principle drawing of the work done by a gas on a piston. The cross-sectional area of the cylinder is A. The pressure p of the gas pushes the piston with a force F = pA, and the piston moves a distance Δs to the right. The volume of the gas grows by the shaded part, ΔV = AΔs. The work is W = FΔs = pAΔs = pΔV. The picture is not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-piston-work.webp" x="1.2" y="0" width="597" height="339.6" preserveAspectRatio="none"/>
  <foreignObject x="449" y="85.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$F = pA$</div></foreignObject>
  <foreignObject x="143" y="115.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas},\ p$</div></foreignObject>
  <foreignObject x="318.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta V$</span></div></foreignObject>
  <foreignObject x="46" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="318.5" y="228.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="190" y="275.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = F\,\Delta s = pA\,\Delta s = p\,\Delta V$</div></foreignObject>
</svg>

```pysahdy
The pressure of a gas is $100\,\text{kPa}$, and it expands by a volume of $0.010\,\text{m}^3$. The pressure stays constant. How much work does the gas do?
---
$W = p\,\Delta V$, so $W = 1.0\,\text{kJ}$ ($100\,000\,\text{Pa} \cdot 0.010\,\text{m}^3$).
```

### A heat engine repeats its motion
A heat engine turns heat into work continuously, so it has to repeat its motion. The piston has to be brought back down. If it is pressed down at the same pressure, the return takes all the work done by the gas. The return takes less work if the gas is first cooled to a lower pressure, but then the gas gives up heat to a colder environment. In a steam power plant, water boils in the boiler, the hot steam expands in the turbine and turns the generator, and the steam coming out of the turbine condenses back into water in the condenser, which is cooled by seawater. The working substance goes round the same path again and again, so at the end of a cycle its internal energy is the same as at the start. Energy is conserved: the heat $Q_1$ from the hot source equals the work $W$ done by the engine plus the heat $Q_2$ given up to the colder environment.

<figure class="unit-photo"><img src="pics/fy3/steam-locomotive-wheel.webp" alt="Close-up of the large driving wheel of a red steam locomotive and the connecting rod attached to it."><figcaption>In a steam locomotive the expanding steam pushes a piston, and the connecting rod turns the piston's back-and-forth motion into the rotation of the wheels.</figcaption></figure>

Experience shows that a heat engine cannot turn all the heat it receives into work; part of it must always be given up to a colder environment. This is the content of the second law of thermodynamics. The larger the temperature difference between the hot source and the cold environment compared with the temperature of the hot source, the larger the share of the heat the engine can turn into work. Cyclic processes are not calculated in this course; the simulation only shows why the heat $Q_2$ cannot be avoided.

<svg data-fig="heat-engine" viewBox="0 0 600 340" role="img" aria-label="The energy flows of a heat engine as arrows whose width shows the energy flow, that is, the power: from the hot source, whose temperature is T_1, the heat Q_1 enters the engine. The engine does work W, which is 40 per cent of Q_1, and gives up the rest, the heat Q_2, to the cold environment, whose temperature is T_2. The widths of the arrows are to scale: Q_1 is 60, W is 24 and Q_2 is 36 units, so the Q_1 arrow is as wide as the W and Q_2 arrows together." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-heat-engine.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="221" y="23.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hot source}\quad T_1$</div></foreignObject>
  <foreignObject x="183.5" y="287.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{cold environment}\quad T_2$</div></foreignObject>
  <foreignObject x="258.5" y="152.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{engine}$</div></foreignObject>
  <foreignObject x="354" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_1$</div></foreignObject>
  <foreignObject x="342" y="229.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_2$</div></foreignObject>
  <foreignObject x="460" y="119.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="16" y="137.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{arrow width}$</div></foreignObject>
  <foreignObject x="16" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{shows power}$</div></foreignObject>
</svg>

```pysahdy
Can a heat engine turn all the heat it receives into work?
---
No. Part of the heat must always be given up to a colder environment.
```

### Efficiency
Efficiency tells how large a share of the energy supplied to a machine is put to use, so its value depends on what is counted as useful. In the efficiency of a power plant's electricity production, only the electricity is useful. A Finnish condensing power plant that produces only electricity gets about $40\,\%$ of the energy of its fuel as electricity, and a nuclear power plant about $35\,\%$. Most of the rest is transferred to the sea through the condenser, and in a plant that burns fuel part also leaves into the air with the flue gases. The efficiency of a car engine is about $30\,\%$, and the rest of the energy leaves with the exhaust gases and the radiator.

In combined production of electricity and heat, the heat $Q_2$ of the condenser is recovered: it heats the water of the district heating network, which carries it to the houses of the city. So the heat engine still gives up heat to something colder, but this heat is put to use. In the overall efficiency, the electricity and the district heating together count as useful, and it is 85–$90\,\%$. The efficiency of electricity production therefore does not rise; it is usually lower than when only electricity is produced. This answers the opening question: less than half becomes electricity, but the rest does not disappear; it is transferred as heat to the environment or to the district heating network.

### Refrigerator and heat pump
A refrigerator and a heat pump work the opposite way to a heat engine: they use electrical energy to transfer heat from a cold place to a warm one. A refrigerator transfers heat from inside the cabinet to the room, and an air-source heat pump from the outdoor air to the inside. The heat given out indoors is the sum of the heat taken from outside and the electricity used, so a pump can heat a house with, for example, three times as much heating power as the electric power it uses. The ratio of the heating power to the electric power is called the coefficient of performance. The coefficient of performance is not an efficiency: it can be greater than 1, because part of the heat that comes indoors is transferred from the outdoor air and does not come from the electricity. The pump does not create energy; it transfers it.

<svg data-fig="heat-pump" viewBox="0 0 600 340" role="img" aria-label="The energy flows of a heat pump as arrows whose width shows the power: the electrical energy W and the heat Q_2 taken from the outdoor air enter the pump, and the pump gives out indoors the heat Q_1, which is their sum. The widths of the arrows are to scale: W is 20, Q_2 is 40 and Q_1 is 60 units, so the arrow going indoors is as wide as the two incoming arrows together and three times as wide as the electricity arrow." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-heat-pump.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="208.5" y="23.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{cold outdoor air}$</div></foreignObject>
  <foreignObject x="202.5" y="287.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{warm indoor space}$</div></foreignObject>
  <foreignObject x="271" y="152.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pump}$</div></foreignObject>
  <foreignObject x="344" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_2$</div></foreignObject>
  <foreignObject x="41" y="119.5" width="162" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{electricity}\ W$</div></foreignObject>
  <foreignObject x="354" y="230.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_1$</div></foreignObject>
  <foreignObject x="451" y="137.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{arrow width}$</div></foreignObject>
  <foreignObject x="451" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{shows power}$</div></foreignObject>
</svg>

```pysahdy
The coefficient of performance of a heat pump is 3. How much heat does it give out indoors with $1\,\text{kWh}$ of electricity, and where does the rest of the heat come from?
---
It gives out $3\,\text{kWh}$ of heat indoors. The electricity is $1\,\text{kWh}$, and the other $2\,\text{kWh}$ is transferred from the outdoor air.
```

## Formula: Work done by a gas and efficiency
When the pressure of a gas stays constant, the work done by the gas in expanding is
```kaavat
work done by a gas in expansion / on a gas in compression :: W = p\,\Delta V
```
where $W$ is the work done by the gas (J), $p$ the pressure of the gas (Pa) and $\Delta V$ the change in the volume of the gas (m³). When the gas is compressed, the same formula gives the magnitude of the compression work done on the gas by the surroundings. The change in the internal energy of the gas is given by the first law of thermodynamics
```kaavat
first law of thermodynamics :: \Delta U = Q + W
```
where $Q$ is the quantity of heat transferred to the gas (J) and $W$ the work done on the gas (J), as in the chapter *Internal energy, heat and conservation of energy*. So in the first law $W$ is the work done on the gas: when the gas expands and does the work $p\,\Delta V$, the work done on it is $W = -p\,\Delta V$, so $\Delta U = Q - p\,\Delta V$.

During one cycle of a heat engine, the work done and the efficiency are
```latex
W = Q_1 - Q_2
```
```kaavat
efficiency of a heat engine :: \eta = \frac{W}{Q_1} = \frac{Q_1 - Q_2}{Q_1}
```
where $Q_1$ is the heat transferred to the engine from the hot source (J), $Q_2$ the heat given up to the colder environment (J), $W$ the work done by the engine during the cycle (J) and $\eta$ the efficiency, which is often given as a percentage. Efficiency can be calculated in the same way from powers, for example the electric power divided by the fuel power.

<svg data-fig="pv-work" viewBox="0 0 600 330" role="img" aria-label="(V, p) graph of a gas expanding at constant pressure: the pressure p stays constant while the volume grows from V_1 to V_2, so the graph is a horizontal line segment, and an arrow shows the direction of the expansion. The shaded rectangle between the segment and the V axis, whose width is the change in volume ΔV and whose height is p, is the work done by the gas W = p ΔV. Schematic diagram." style="max-width:100%;font-size:24px">
  <line x1="203" y1="270" x2="203" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="270" x2="363" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="112.5" x2="470" y2="112.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="271" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="203" y1="270" x2="203" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="186.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_1$</div></foreignObject>
  <line x1="363" y1="270" x2="363" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_2$</div></foreignObject>
  <line x1="89" y1="112.5" x2="96" y2="112.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="98" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{m}^3)$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{Pa})$</div></foreignObject>
  <polygon points="203,270 363,270 363,112.5 203,112.5" fill="#e8590c" fill-opacity="0.35"/>
  <polyline points="203,112.5 363,112.5" fill="none" stroke="#1f2933" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="203" y1="112.5" x2="203" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="363" y1="112.5" x2="363" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="269" y1="112.5" x2="278" y2="112.5" stroke="#1f2933" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M297,112.5 L277,121.5 L277,103.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="216.5" y="72" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas expands}$</div></foreignObject>
  <foreignObject x="241.5" y="156" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = p\,\Delta V$</div></foreignObject>
  <line x1="257" y1="228" x2="218" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M206,228 L219,222 L219,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="309" y1="228" x2="348" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M360,228 L347,234 L347,222 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="266.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta V$</div></foreignObject>
</svg>

A heat pump gives out indoors the heat $Q_1$, which is the sum of the heat $Q_2$ taken from the outdoor air and the electrical energy $W$ used by the pump. Energy is conserved, so the electrical energy used by the pump is $W = Q_1 - Q_2$. The coefficient of performance tells how many times as much heat the pump gives out indoors as the electrical energy it uses:
```kaavat
coefficient of performance of a heat pump :: \varepsilon = \frac{Q_1}{W} = \frac{Q_1}{Q_1 - Q_2}
```
where $Q_1$ is the heat given out to the warm side, that is, indoors (J), $Q_2$ the heat taken from the cold side, that is, from the outdoor air (J), $W$ the electrical energy, that is, the work used by the pump (J) and $\varepsilon$ the coefficient of performance. The coefficient of performance can be calculated in the same way from powers.

## Worked example
Wood chip energy is fed into the boiler of a biopower plant at a power of $500\,\text{MW}$. When the plant produces only electricity, the electric power is $190\,\text{MW}$. In winter the same plant works as a combined heat and power plant: it produces $150\,\text{MW}$ of electricity and $290\,\text{MW}$ of district heating. What is the efficiency in each case, and how much power is transferred to the environment as waste heat?

<!-- vaihe -->

**Given and find.** Fuel power $P_1 = 500\,\text{MW}$. When only electricity is produced, the electric power is $P_\text{e} = 190\,\text{MW}$; in combined production $P_\text{e} = 150\,\text{MW}$ and the district heating power is $P_\text{dh} = 290\,\text{MW}$.

The efficiencies $\eta$ and the power of the waste heat $P_2$ are asked for in both cases.

<!-- vaihe -->

**Principle.** Efficiency is the useful power divided by the power supplied; it is calculated from powers just like from energies, because both are energy in the same time.

Energy is conserved, so the fuel power is divided into the useful power and the waste heat. In electricity production alone only the electricity is useful; in combined production both the electricity and the district heating are.

<!-- vaihe -->

**Rearranged formula.** Solve for the quantities asked for, with symbols before numbers:
```latex
\begin{aligned}
\eta &= \frac{P_\text{a}}{P_1} \\
P_2 &= P_1 - P_\text{a}
\end{aligned}
```
The useful (output) power is $P_\text{a}$: for electricity alone $P_\text{a} = P_\text{e}$, and for combined production $P_\text{a} = P_\text{e} + P_\text{dh}$.

<!-- vaihe -->

**Unit conversions.** All powers are given in megawatts, so no conversions are needed: in the efficiency the unit cancels, and the waste heat comes out in megawatts. A decimal number is changed to a percentage by multiplying by one hundred.

<!-- vaihe -->

**Substitution.** For electricity alone and for combined production separately:
```latex
\begin{aligned}
\eta_1 &= \frac{P_\text{e}}{P_1} \\
&= \frac{190\,\text{MW}}{500\,\text{MW}} \\
&= 0.380 \\
P_{2,1} &= P_1 - P_\text{e} \\
&= 500\,\text{MW} - 190\,\text{MW} \\
&= 310\,\text{MW} \\[6pt]
\eta_2 &= \frac{P_\text{e} + P_\text{dh}}{P_1} \\
&= \frac{150\,\text{MW} + 290\,\text{MW}}{500\,\text{MW}} \\
&= 0.880 \\
P_{2,2} &= P_1 - (P_\text{e} + P_\text{dh}) \\
&= 500\,\text{MW} - 440\,\text{MW} \\
&= 60\,\text{MW}
\end{aligned}
```

<!-- vaihe -->

**Result.** With electricity production alone the efficiency is $\eta_1 = 0.380 = 38.0\,\%$ and $310\,\text{MW}$ of waste heat is transferred to the environment, most of it through the condenser to the sea.

In combined production the overall efficiency is $\eta_2 = 0.880 = 88.0\,\%$ and there is only $60\,\text{MW}$ of waste heat. The powers are given in whole megawatts, so the differences $310\,\text{MW}$ and $60\,\text{MW}$ are known to the nearest megawatt.

The efficiencies are quotients, so they have as many figures as the least precise power: $190\,\text{MW}$, $150\,\text{MW}$, $290\,\text{MW}$ and $500\,\text{MW}$ all have three figures, so the efficiencies are given with three figures.

<!-- vaihe -->

**Reasonableness.** Energy is conserved: $190\,\text{MW} + 310\,\text{MW} = 500\,\text{MW}$ and $$\begin{aligned} &150\,\text{MW} + 290\,\text{MW} + 60\,\text{MW} \\ &= 500\,\text{MW} \end{aligned}$$. The efficiency of electricity production stays clearly below $100\,\%$, because a heat engine must give up part of the heat to something colder.

Even the overall efficiency is not $100\,\%$, because part of the heat leaves with the flue gases and other losses.

Less electricity is obtained in combined production because the steam is condensed at a higher temperature so that its heat is suitable for district heating. The energy of the fuel is still put to much better use.

## Common misconception
Many people think that better technology could make a heat engine almost perfect, so that all the heat would turn into work. Reducing friction and other losses helps, but part of the heat must always be given up to a colder environment, so the efficiency of a heat engine stays clearly below $100\,\%$. The frictionless piston of the simulation shows the reason: for the piston to be brought down with less work than it took to raise it, the gas has to be cooled, and in the cooling heat is transferred to the cold water. The limit applies to a machine that turns heat into work, not to all devices: for example, in an electric heater practically all the electrical energy increases the internal energy of the resistor and is transferred as heat to the room.

Another mistake is to think of a heat pump as a perpetual motion machine, because it gives out more heat than it uses electricity. The extra heat comes from the outdoor air, and energy is not created out of nothing. A third mistake is to think that a pressurised gas does work just because its pressure is high. Work is done only when the volume changes and the piston moves.

## Summary
- A gas that expands at constant pressure does the work $W = p\,\Delta V$, which is the area under the ($V$, $p$) graph. In the first law $\Delta U = Q + W$ the work $W$ is the work done on the gas, so for an expanding gas $\Delta U = Q - p\,\Delta V$.
- A piston machine can repeat its work only if the gas is cooled before the piston is returned; then heat is transferred to something colder.
- A heat engine takes heat $Q_1$ from a hot source, does work $W$ and gives up heat $Q_2$ to a colder environment: $W = Q_1 - Q_2$.
- Efficiency is $\eta = W/Q_1 = (Q_1 - Q_2)/Q_1$. A heat engine cannot turn all the heat into work.
- The efficiency of electricity production of a condensing power plant is about $40\,\%$. In combined production of electricity and heat the heat of the condenser is used as district heating, so the overall efficiency, in which electricity and heat both count as useful, is 85–$90\,\%$.
- A refrigerator and a heat pump use work to transfer heat from cold to warm. They do not create energy. The coefficient of performance of a heat pump, $\varepsilon = Q_1/(Q_1 - Q_2)$, where $Q_1$ is the heat given out indoors and $Q_2$ the heat taken from the outdoor air, is not an efficiency, and it can be greater than 1, because part of the heat comes from the outdoor air.
