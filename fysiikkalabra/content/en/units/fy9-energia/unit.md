# Energy, power and efficiency

> **Why** does charging an electric car from a household socket take all night, even though the battery holds less energy than ten litres of petrol?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter evening. In the foreground is a red detached house with light shining from its windows, and an electric car connected to the charger on its wall. A power line runs from the house along poles far across a lake. On the other shore of the lake is a power plant with steam rising from its chimney and its cooling tower, and next to it three wind turbines." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-energia-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

All the problems of this lesson start from the same principle: **energy is conserved**. It is transformed from one form to another and transferred from one place to another, but it is neither created nor destroyed. When a device “consumes” energy, it transforms it, and most of it finally ends up as heat in the surroundings.

Three questions branch off from the conservation law, and the energy problems of the exam come back to them. **How fast** is energy transformed? Power tells that. **How large a share** is useful? Efficiency tells that. **Where** does the energy come from? From the heat of combustion of a fuel, from the work done by a force, or from flowing water, the wind and the sun.

```pysahdy
The problem asks how fast energy is transformed and how large a share of it becomes useful. Which quantities tell these?
---
How fast energy is transformed is told by power. How large a share becomes useful is told by efficiency.
```

<svg data-fig="kartta" viewBox="0 0 380 870" role="img" aria-label="Recognition chart: how do I tell which law to use? Start by listing the forms of energy and see which sign in the task fits. Isolated system: energy is conserved, so the initial energy equals the final energy. Energy over time: power is the change of energy divided by the time. Steady power, duration known: energy is power times time. Kilowatt-hours: convert to joules, one kilowatt-hour is 3.6 megajoules. Useful energy and input energy: efficiency is the useful energy divided by the input energy. Several devices in a row: multiply the efficiencies of the stages. Fuel, heating value: the heat released in burning is the heating value times the mass. A force moves a distance: the work is force times distance." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{forms of energy first, then the sign}$</div></foreignObject>
  <line x1="14" y1="149" x2="30" y2="149" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{isolated system}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{energy is conserved}$</div></foreignObject>
  <rect x="142" y="172" width="220" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="146" y="174" width="212" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_\text{initial} = E_\text{final}$</div></foreignObject>
  <line x1="14" y1="250" x2="30" y2="250" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="214" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="224.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{energy over time}$</div></foreignObject>
  <line x1="40" y1="254" x2="362" y2="254" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="259" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{power}$</div></foreignObject>
  <rect x="232" y="258" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="260" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$P = \Delta E/\Delta t$</div></foreignObject>
  <line x1="14" y1="336" x2="30" y2="336" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="300" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="310.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{steady power, duration known}$</div></foreignObject>
  <line x1="40" y1="340" x2="362" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="345" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{energy}$</div></foreignObject>
  <rect x="238" y="344" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="346" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = Pt$</div></foreignObject>
  <line x1="14" y1="437" x2="30" y2="437" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="386" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="396.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kilowatt-hours}$</div></foreignObject>
  <line x1="40" y1="426" x2="362" y2="426" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="431" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{convert to joules}$</div></foreignObject>
  <rect x="172" y="460" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="462" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$1\,\text{kWh} = 3.6\,\text{MJ}$</div></foreignObject>
  <line x1="14" y1="538" x2="30" y2="538" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="502" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="512.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{useful and input energy}$</div></foreignObject>
  <line x1="40" y1="542" x2="362" y2="542" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="547" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{efficiency}$</div></foreignObject>
  <rect x="232" y="546" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="548" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = W_\text{a}/W_\text{o}$</div></foreignObject>
  <line x1="14" y1="639" x2="30" y2="639" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="588" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="598.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{several devices in a row}$</div></foreignObject>
  <line x1="40" y1="628" x2="362" y2="628" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="633" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{multiply efficiencies}$</div></foreignObject>
  <rect x="212" y="662" width="150" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="664" width="142" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = \eta_1\eta_2\eta_3$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{fuel, heating value}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="206" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{heat of combustion}$</div></foreignObject>
  <rect x="262" y="748" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="750" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = Hm$</div></foreignObject>
  <line x1="14" y1="826" x2="30" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="790" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="800.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a force moves a distance}$</div></foreignObject>
  <line x1="40" y1="830" x2="362" y2="830" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="835" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{work}$</div></foreignObject>
  <rect x="238" y="834" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="836" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$W = Fs$</div></foreignObject>
</svg>

In the exam a solution starts with recognising which sign the problem gives and writing its law before the numbers. Energy and power are different quantities: the kilowatt tells the rate, the kilowatt-hour the amount.

This also answers the opening question. Ten litres of petrol contain about $7.5\,\text{kg} \cdot 43\,\text{MJ/kg} \approx 320\,\text{MJ} \approx 90\,\text{kWh}$ of energy, more than a $40\,\text{kWh}$ battery. Charging still takes a long time, because the power of the socket is small: $40\,\text{kWh} : 2.3\,\text{kW} \approx 17\,\text{h}$.

## Formula: Energy, power and efficiency

### Conservation and power

In an isolated system, which no energy enters or leaves, the total energy stays the same:

```latex
E_\text{initial} = E_\text{final}
```

where each side is the sum of all forms of energy, internal energy included. Power is the energy transformed or transferred per unit time:

```kaavat
power :: P = \frac{\Delta E}{\Delta t}
```

where $P$ is the power (W), $\Delta E$ the energy (J) and $\Delta t$ the time (s). For uneven use the formula gives the average power; at constant power $E = P\,t$. The kilowatt-hour is a unit of energy, and it is converted by substitution:

```latex
1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3.6\,\text{MJ}
```

```pysahdy
Is the kilowatt-hour a unit of power or of energy, and how many joules is it?
---
The kilowatt-hour is a unit of energy, and $1\,\text{kWh} = 3.6\,\text{MJ}$. The kilowatt, in turn, is a unit of power.
```

### Efficiency and the energy chain

```kaavat
efficiency :: \eta = \frac{W_\text{a}}{W_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```

where $\eta$ is the efficiency, $W_\text{a}$ and $P_\text{a}$ the useful energy and power given, and $W_\text{o}$ and $P_\text{o}$ the energy and power taken in. The ratio of the powers can be used when the device runs steadily. Energy is conserved, so $W_\text{o} = W_\text{a} + W_\text{h}$, where $W_\text{h}$ is the losses. The efficiency is at most $100\,\%$; it depends on what is defined as useful.

An energy chain has successive stages, and the useful power given by each stage is the power taken in by the next. The example plant in the figure has three stages with the efficiencies $\eta_1$, $\eta_2$ and $\eta_3$. Of the fuel power of $500\,\text{MW}$, $198\,\text{MW}$ becomes electricity, so the efficiency of the whole plant is $\eta = \tfrac{198\,\text{MW}}{500\,\text{MW}} \approx 0.40$. The widths of the bands are to scale, and the outgoing bands are together as wide as the incoming one.

<svg data-fig="ketju" viewBox="0 0 420 476" role="img" aria-label="A to-scale energy flow diagram of a condensing power plant. From the left comes the fuel power of 500 MW as a wide grey band. In the first stage, the boiler, the efficiency is 0.90: an orange loss band of 50 MW turns down from the band, and 450 MW remains. In the second stage, the steam cycle, the efficiency is 0.45: a wide loss band of 248 MW turns down, and 203 MW remains. In the third stage, the generator and the transformer, the efficiency is 0.98 and the loss only 4 MW. A green band of electricity leaves to the right, 198 MW, that is, about 40 per cent of the fuel power. The losses are transferred to the surroundings as waste heat." style="max-width:100%;font-size:20px">
  <image href="pics/fy9/fy9-energia-ketju.webp" x="0" y="0" width="420" height="475.1" preserveAspectRatio="none"/>
  <foreignObject x="57.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\eta_1 = 0.90$</div></foreignObject>
  <foreignObject x="157.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\eta_2 = 0.45$</div></foreignObject>
  <foreignObject x="257.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\eta_3 = 0.98$</div></foreignObject>
  <foreignObject x="23" y="144" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$500\,\text{MW}$</div></foreignObject>
  <foreignObject x="113" y="144" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$450\,\text{MW}$</div></foreignObject>
  <foreignObject x="213" y="80" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$203\,\text{MW}$</div></foreignObject>
  <foreignObject x="342" y="148.5" width="64" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#2b8a3e">$198\,\text{MW}$</div></foreignObject>
  <foreignObject x="295" y="176.5" width="111" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#2b8a3e">$\text{electricity}$</div></foreignObject>
  <foreignObject x="90" y="324" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$50\,\text{MW}$</div></foreignObject>
  <foreignObject x="213" y="324" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$248\,\text{MW}$</div></foreignObject>
  <foreignObject x="332" y="292" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$4\,\text{MW}$</div></foreignObject>
  <foreignObject x="8" y="324" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{losses:}$</div></foreignObject>
  <foreignObject x="8" y="376" width="94" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\eta_1\ \text{boiler}$</div></foreignObject>
  <foreignObject x="8" y="404" width="136" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\eta_2\ \text{steam cycle}$</div></foreignObject>
  <foreignObject x="8" y="432" width="271" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\eta_3\ \text{generator and transformer}$</div></foreignObject>
</svg>

```johda
An energy chain has three successive stages with the efficiencies $\eta_1$, $\eta_2$ and $\eta_3$. Derive the efficiency $\eta$ of the whole chain in terms of the efficiencies of the stages.
---
By the definition of efficiency the efficiency of the whole chain is $\eta = \tfrac{P_\text{a}}{P_\text{o}}$, where $P_\text{o}$ is the power taken in by the first stage and $P_\text{a}$ the useful power given by the last stage. Denote the powers given by the stages $P_1$, $P_2$ and $P_3 = P_\text{a}$. The efficiency gives the power given by each stage from the power it takes in, and the power a stage takes in is the power given by the stage before it:

$$\begin{aligned} P_1 &= \eta_1 P_\text{o} \\ P_2 &= \eta_2 P_1 \\ P_3 &= \eta_3 P_2 \end{aligned}$$

Substitute the powers one after another:

$$P_\text{a} = P_3 = \eta_3\,\eta_2\,\eta_1\,P_\text{o}$$

Divide by the power taken in:

$$\eta = \frac{P_\text{a}}{P_\text{o}} = \eta_1\,\eta_2\,\eta_3$$

The efficiencies are multiplied. Each of them is less than $1$, so the efficiency of the whole chain is smaller than that of any single stage.
```

```pysahdy
The efficiencies of the stages of the chain are $0.90$, $0.45$ and $0.98$. Why is the efficiency of the whole chain smaller than $0.45$?
---
The efficiencies are multiplied together, and each is below $1$. Every stage reduces the useful power, so the product is smaller than the smallest factor.
```

### Sources of energy

The energy released from a fuel and the work done by a force are

```kaavat
heat released in combustion :: Q = Hm
work done by a force :: W = Fs
```

where $Q$ is the heat released (J), $H$ the heat of combustion ($\text{MJ/kg}$) and $m$ the mass burnt (kg); $Q = Hm$ holds when the fuel burns completely and $H$ is the heat of combustion for its actual moisture content. In the work, $F$ is a constant force in the direction of motion (N) and $s$ the distance (m). In steady lifting $W = mgh$, where $g = 9.81\,\text{m/s}^2$ and $h$ is the lifting height.

## Common mistakes {Virheet}

- **Power and energy mixed up.** “The power of the panel is $1.2\,\text{kWh}$” is a mistake: power is in kilowatts, energy in kilowatt-hours. A high-power device does not use much energy if it is on only for a moment.
- **Efficiencies added or subtracted.** In a chain they are multiplied, so the efficiency of the whole chain is smaller than that of the weakest stage.
- **The wrong denominator.** The loss percentage and the efficiency are always calculated from the energy taken in, not from the energy given.
- **Minutes as hours.** $30\,\text{min} = 30 \cdot \tfrac{1}{60}\,\text{h} = 0.50\,\text{h}$; the product of power and time is in kilowatt-hours only when the time is in hours.
- **Losses “disappear”.** Losses are energy that has been transformed into a useless form, usually internal energy, which is transferred to the surroundings as heat.
- **The overall efficiency of combined heat and power compared with an electrical efficiency.** Electricity and district heat are not equally valuable, so the numbers tell different things.

## Review if needed {Kertaa}

- Forms of energy and the conservation law: [*Forms of energy and conservation of energy*](fy2-1.html), chains and prefixes: [*Energy transformations and the joule*](fy2-2.html).
- Power and the kilowatt-hour: [*Power*](fy2-3.html). Efficiency and the energy flow diagram: [*Efficiency*](fy2-4.html).
- Heat of combustion: [*Fuels and heat of combustion*](fy2-5.html). Comparing production methods: [*Ways of producing energy and how they compare*](fy2-6.html).
- Transmission losses and storage: [*Transferring energy: electricity and heat*](fy2-7.html). Emissions: [*Energy production, the environment and climate change*](fy2-8.html).
- Work and the work of lifting: [*Work and energy*](fy3-2.html). The chain of a power plant and combined heat and power: [*Energy production and the efficiency of power plants*](fy3-15.html).
