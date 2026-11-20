# Transferring energy: electricity and heat

> **Why** is the voltage in power lines hundreds of kilovolts when a wall socket gives only $230\,\text{V}$, and why are district heating pipes wrapped in thick insulation?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: tall power line pylons in a landscape, their wires running far away. In the foreground a cut-away view through the ground: district heating pipes surrounded by a thick layer of insulation carry heat to a house." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

Energy is often produced far from where it is used: the power plant is outside the city, but the heater and the wall socket are at home. So the energy has to be transferred to the user. Energy can be transferred from place to place in many ways. This chapter looks at two ways that are important for society's energy networks: transferring **electrical energy** in the electricity grid and transferring **thermal energy** in the water pipes of the district heating network.

### The electricity grid

The **electricity grid** carries electrical energy from the power plant to the home. Long distances are covered by the power lines of the national grid, whose voltage is $110\text{–}400\,\text{kV}$. Closer to the user the voltage is first lowered to $20\,\text{kV}$ and finally to the $0.4\,\text{kV}$ of the low-voltage network, from which the sockets in homes get $230\,\text{V}$. The voltage is changed in transformers.

<svg data-fig="grid" viewBox="0 0 600 332" role="img" aria-label="Schematic of the route of electricity from the power plant to the home. From left to right: power plant and its transformer, national grid power line (voltage from 110 kV to 400 kV), substation, distribution network poles (20 kV) and home (0.4 kV, 230 V at the socket). Below, an orange arrow shows the flow of energy from the power plant to the home. Not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-grid.webp" x="0" y="-1.2" width="600" height="338.8" preserveAspectRatio="none"/>
  <foreignObject x="160" y="47.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$110\text{–}400\,\text{kV}$</div></foreignObject>
  <foreignObject x="426" y="101.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="506" y="47.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.4\,\text{kV}$</div></foreignObject>
  <foreignObject x="67" y="88.5" width="110" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{transformer}$</div></foreignObject>
  <foreignObject x="18" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{power plant}$</div></foreignObject>
  <foreignObject x="175" y="247.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{national grid}$</div></foreignObject>
  <foreignObject x="325" y="281.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{substation}$</div></foreignObject>
  <foreignObject x="462" y="241" width="136" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\text{distribution}$</div></foreignObject>
  <foreignObject x="482" y="267" width="96" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\text{network}$</div></foreignObject>
</svg>

### Why long distances use high voltage

The same power can be transferred in two ways: with a low voltage and a large electric current, or with a high voltage and a small electric current. A wire gets hotter the larger the current in it is, and the energy used for heating is a loss. So long distances are covered with a high voltage, which keeps the current and the loss small. The exact connection between voltage, current and loss belongs to later courses on electricity.

A transformer raises the voltage at the power plant and lowers it again close to the user. In a good transformer the loss is very small.

```pysahdy
Two power lines transfer the same power, one with a high voltage and the other with a low voltage. In which line do the wires get hotter?
---
In the low-voltage line. There the current is larger, and a larger current heats a wire more.
```

<figure class="unit-photo"><img src="pics/fy2/muurame-transformer.webp" alt="A large grey-green transformer with insulators and fans at a fenced substation among birch trees."><figcaption>A substation transformer in Muurame, Finland. At a substation the transformer lowers the high voltage of the power line to the voltage of the distribution network.</figcaption></figure>

### District heating

**District heating** transfers energy as hot water. The water heated at the heating plant flows in the supply pipe to buildings and gives heat to the building's heating system. The cooled water returns in the return pipe to be heated again. The pipes are underground in thick insulation so that as little heat as possible goes into the surrounding ground.

<svg data-fig="district" viewBox="0 0 600 320" role="img" aria-label="Schematic of the district heating loop. On the left the heating plant, on the right a home. A red supply pipe takes hot water to the home and a blue return pipe brings the cooled water back. The pipes are inside shared insulation underground. Orange arrows show that a little heat still escapes through the insulation into the ground. Not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-district.webp" x="2.5" y="5" width="597" height="325.9" preserveAspectRatio="none"/>
  <foreignObject x="444" y="209.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{heat loss}$</div></foreignObject>
  <foreignObject x="121" y="79.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{supply water}$</div></foreignObject>
  <foreignObject x="165" y="253.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{return water}$</div></foreignObject>
  <foreignObject x="339" y="79.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{insulation}$</div></foreignObject>
  <foreignObject x="16" y="247.5" width="146" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{heating plant}$</div></foreignObject>
  <foreignObject x="505" y="247.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{home}$</div></foreignObject>
</svg>

### Transmission loss

In the electricity grid some of the electrical energy is converted into internal energy in the wires and other equipment, and this is transferred as heat to the surroundings. In the district heating network, energy is transferred as heat from the hot water through the pipes and insulation to the surroundings. In both cases the users get less energy than is fed into the network. This is called **transmission loss**. The energy does not disappear (chapter *Forms of energy and conservation of energy*), but the loss is useless to the user.

In Finland the losses of the electricity grid in 2024 were about $4\,\%$ of electricity consumption, when consumption was about $83\,\text{TWh}$ (Finnish Energy, Sähkövuosi 2024). In this chapter consumption is used as the energy sent into the electricity grid, so $4\,\%$ is a share of it. About $36\,\text{TWh}$ was supplied to the district heating network in 2024 and about $32.7\,\text{TWh}$ was used by customers, so about $9\,\%$ was left on the way (Finnish Energy, Kaukolämpötilasto 2024; the share is calculated from the difference, so it is an estimate). The loss of district heating is relatively larger because hot water is clearly warmer than its surroundings: the greater the temperature difference to the surroundings, the more heat escapes, and heat gets through the insulation along the whole length of the pipework.

```pysahdy
$100\,\text{GWh}$ is fed into the network and the users receive $91\,\text{GWh}$. How large is the transmission loss, and did the energy that went into the loss disappear?
---
The loss is $9\,\text{GWh}$, or $9\,\%$ of the energy fed in. The energy did not disappear but was transferred as heat to the surroundings.
```

### Transferring energy in time: storage

Energy is also transferred in time. Wind power and solar electricity are produced when the wind blows or the sun shines, but electricity is needed at other times too. A store takes in energy when there is too much of it and gives it out later.

<svg data-fig="storage" viewBox="0 0 600 300" role="img" aria-label="Schematic of three energy stores. On the left a battery, where the energy is chemical. In the middle a pumped-storage plant: upper reservoir, lower reservoir and a pipe in which water flows down. On the right a heat store, an insulated tank full of hot water. Not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-storage.webp" x="6" y="0" width="579.7" height="298.3" preserveAspectRatio="none"/>
  <foreignObject x="55" y="252.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <foreignObject x="192" y="252.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pumped storage}$</div></foreignObject>
  <foreignObject x="375" y="252.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat store}$</div></foreignObject>
  <foreignObject x="25" y="25.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{chemical}$</div></foreignObject>
  <foreignObject x="188" y="25.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potential}\ \text{energy}$</div></foreignObject>
  <foreignObject x="420" y="25.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{thermal}$</div></foreignObject>
  <foreignObject x="196" y="78" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{upper pool}$</div></foreignObject>
  <foreignObject x="186" y="211.5" width="116" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lower pool}$</div></foreignObject>
</svg>

In a battery the energy is stored as chemical energy. In a pumped-storage power plant water is pumped to an upper reservoir, and the water flowing down turns the machines of the power plant. In a heat store hot water stays in an insulated tank, and it is used for example in the district heating network. Electricity is not stored in large amounts as such but by converting it into another form of energy and back, and in every conversion some of the energy turns into heat.

```pysahdy
In a pumped-storage power plant water is pumped to an upper reservoir and later allowed to flow down. In what form is the energy stored, and can all of it be got back as electricity?
---
The energy is stored as the gravitational potential energy of the water in the upper reservoir. Not all of it comes back, because in every conversion some of the energy turns into heat.
```

## Formula: Transmission loss

The loss is the difference between the energy sent into the network and the energy that arrives. The efficiency of the transfer (chapter *Efficiency*) is the share of the sent energy that arrives:

```latex
\begin{aligned}
E_\text{loss} &= E_\text{sent} - E_\text{arrived} \\
\eta &= \frac{E_\text{arrived}}{E_\text{sent}}
\end{aligned}
```

where $E_\text{sent}$ is the energy fed into the network, $E_\text{arrived}$ the energy that reached the user, $E_\text{loss}$ the energy transferred as heat to the surroundings on the way and $\eta$ the efficiency of the transfer. Efficiency is given as a percentage or as a decimal number.

<svg data-fig="sankey" viewBox="0 0 600 330" role="img" aria-label="Energy flow diagram to scale. At the top the electricity grid: of the sent energy 96 % arrives and 4 % is lost. At the bottom the district heating network: 91 % arrives and 9 % is lost. The width of a stream is proportional to the energy; the width of the sent energy is the same in both." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-sankey.webp" x="11.1" y="2.5" width="591.1" height="332.5" preserveAspectRatio="none"/>
  <foreignObject x="12" y="17.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{electricity}$</div></foreignObject>
  <foreignObject x="50" y="77.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="76" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$96\,\%$</div></foreignObject>
  <foreignObject x="510" y="142" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4\,\%$</div></foreignObject>
  <foreignObject x="12" y="175.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{district heating}$</div></foreignObject>
  <foreignObject x="50" y="235.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="232" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$91\,\%$</div></foreignObject>
  <foreignObject x="510" y="298" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$9\,\%$</div></foreignObject>
</svg>

In the figure the width of a stream shows the amount of energy. In the electricity grid $4\,\%$ of the sent energy (the consumption) is lost and $96\,\%$ arrives, in district heating $9\,\%$ and $91\,\%$.

### Calculating from a loss percentage

A loss percentage is always taken of the sent energy. If the loss is $9.0\,\%$, then $100\,\% - 9.0\,\% = 91.0\,\%$ of the sent energy arrives, and $91.0\,\% = 91.0 : 100 = 0.910$. The energy you need is solved from the formula: $E_\text{arrived} = \eta\, E_\text{sent}$ and $E_\text{sent} = E_\text{arrived} : \eta$.

The same applies to power: the power that arrives is $\eta$ times the power sent. Energy and power are connected by the formula $P = \tfrac{E}{t}$ (chapter *Power: $P = \Delta E/\Delta t$*), so with a steady loss power $P_\text{loss}$ the energy lost during a time $t$ is $E_\text{loss} = P_\text{loss} \cdot t$.

## Worked example

A district heating network transfers $245\,\text{MWh}$ of thermal energy per week from the heating plant to a district of the city (an example situation). The loss of the network is $9.0\,\%$ of the sent energy. How much energy arrives and how much is lost?

<!-- vaihe -->

**Given and find.**

- $E_\text{sent} = 245\,\text{MWh}$ and
- the loss is $9.0\,\%$ of the sent energy.

We want the energy that arrives, $E_\text{arrived}$, and the loss $E_\text{loss}$.

<!-- vaihe -->

**Principle.** Energy does not disappear, so the sent energy equals the arriving and the lost energy together. When $9.0\,\%$ is lost, the remaining $91.0\,\%$ arrives, so the efficiency is $\eta = 0.910$.

<!-- vaihe -->

**Rearranged formula.**

```latex
\begin{aligned}
&E_\text{arrived} = \eta\, E_\text{sent} \\
&E_\text{loss} = E_\text{sent} - E_\text{arrived}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The efficiency is obtained from the percentage: $\eta = 100\,\% - 9.0\,\% = 91.0\,\% = 91.0 : 100 = 0.910$. The energies are in the same unit, megawatt-hours, so no other conversion is needed.

<!-- vaihe -->

**Substitution.**

```latex
\begin{aligned}
E_\text{arrived} &= \eta\, E_\text{sent} \\
&= 0.910 \cdot 245\,\text{MWh} \\
&= 222.95\,\text{MWh} \\
E_\text{loss} &= E_\text{sent} - E_\text{arrived} \\
&= (245 - 222.95)\,\text{MWh} \\
&= 22.05\,\text{MWh}
\end{aligned}
```

<!-- vaihe -->

**Result.** About $223\,\text{MWh}$ arrives and about $22\,\text{MWh}$ is lost. The arriving energy is given with three significant figures because the efficiency $0.910$ and the sent energy $245\,\text{MWh}$ are known to three figures. The loss is given with two significant figures because the loss percentage $9.0\,\%$ is known only to two figures.

<!-- vaihe -->

**Reasonableness.** Ten per cent of $245\,\text{MWh}$ would be $24.5\,\text{MWh}$, and $9.0\,\%$ is slightly less, so a loss of $22\,\text{MWh}$ is of the right size. Also $$
\begin{aligned}
&222.95\,\text{MWh} + 22.05\,\text{MWh} \\
&= 245\,\text{MWh}
\end{aligned}
$$, so the energy is conserved.

## Common misconception

Many people think that energy disappears in transmission loss. Energy does not disappear. In the electricity grid some of the electrical energy is converted into internal energy in the wires, and in the district heating network energy passes from the hot water through the pipes. In both cases the energy is finally transferred as heat to the surroundings, and the user gets no benefit from it.

Another mistake is to take the loss percentage of the energy that arrives. The percentage must be taken of the sent energy: if the loss is $9.0\,\%$ and $245\,\text{MWh}$ arrives, the sent energy is not $245\,\text{MWh} + 0.090 \cdot 245\,\text{MWh}$ but $245\,\text{MWh} : 0.910$.

A third mistake is to think that the loss is subtracted from the percentage as a unit: a loss of $4\,\%$ does not mean $4\,\text{MWh}$ but four hundredths of the sent energy.

## Summary

- Electrical energy is transferred in the electricity grid, long distances at high voltage, because then the current is small and the loss caused by heating of the wires is small. Transformers raise and lower the voltage.
- Thermal energy is transferred in the district heating network as hot water in insulated pipes. In transmission loss, electrical energy is converted into internal energy in the wires, and energy passes from the hot water through the pipes; in both, the energy is transferred as heat to the surroundings. In Finland the losses were about $4\,\%$ in the electricity grid and about $9\,\%$ in the district heating network (Finnish Energy, 2024).
- Transmission loss $E_\text{loss} = E_\text{sent} - E_\text{arrived}$ and efficiency of the transfer $\eta = E_\text{arrived} : E_\text{sent}$. The loss percentage is taken of the sent energy.
- Stores (battery, pumped-storage plant, heat store) transfer energy in time, but in them too some of the energy turns into heat.
