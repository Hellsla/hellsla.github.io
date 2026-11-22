# Applied chapter: the electric car and the home electrical system

> **Why** should an electric car not be charged through an extension cord from an ordinary socket, and is the electricity of a home enough for the sauna and for charging the car at the same time?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter evening and a red detached house in the snow. Light shines from the windows of the house, and smoke rises from the chimney of the sauna. On the end wall of the house there is a charging station, from which a winding charging cable runs to the charging socket below the front door of a blue electric car standing in the yard. In the background there are spruces and an electricity pole from which wires come to the roof of the house." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-16-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Battery, power and charging time
The battery of an electric car is a large lithium-ion battery (chapter *Batteries and the charging circuit*). This chapter uses an example car whose battery has a nominal voltage of $400\,\text{V}$ and a capacity of $160\,\text{Ah}$. The energy of the battery is then $$\begin{aligned} W &= UQ \\ &= 400\,\text{V} \cdot 160\,\text{Ah} \\ &= 64\,\text{kWh} \end{aligned}$$, and it is enough for about $350\,\text{km}$ of driving when the car uses $18\,\text{kWh}$ per hundred kilometres. So the battery holds as much energy as a $6\,\text{kW}$ sauna heater uses in over ten hours.

The charging time depends on how much energy has to be transferred to the battery and at what power this is done. In charging, part of the energy taken from the grid does not end up in the battery but turns into internal energy of the charger of the car, the cables and the battery, which is transferred to the surroundings as heat. The efficiency of home charging is typically about $80\text{–}95\,\%$, and it is always below $100\,\%$. More energy therefore has to be taken from the grid than is stored in the battery.

<figure class="unit-photo"><img src="pics/fy6/ev-charging-socket.webp" alt="An open flap in the front of a white car with two charging inlets beneath it: a larger black one and a smaller one with an orange protective cap."><figcaption>The charging inlets of an electric car. The larger inlet is for fast charging with direct current. The smaller one is for charging with alternating current, in which the car's own charger converts the alternating current of the grid into direct current for the battery.</figcaption></figure>

```pysahdy
The efficiency of charging is $0.85$. What does this mean for the energy drawn from the grid, and where does the rest go?
---
Only $85\,\%$ of the energy drawn from the grid is stored in the battery. The other $15\,\%$ becomes internal energy of the charger, the wires and the battery.
```

### One phase or three
A Finnish detached house usually gets **three-phase** electricity: three phase conductors $\text{L}_1$, $\text{L}_2$ and $\text{L}_3$ and a neutral conductor $\text{N}$. Between each phase conductor and the neutral conductor there is a voltage of $230\,\text{V}$. An ordinary socket and a kettle use one phase, a sauna heater and a charging station usually all three. When a device draws the same current $I$ from each phase conductor, each phase transfers a power $UI$, and the total power is three times as great. The voltage between the phase conductors is $400\,\text{V}$, but it is not needed here.

The current of a device is obtained from its power as in the chapter *Electrical energy at home*: in one phase $I = P : U$. When charging from an ordinary socket, the charging cable usually limits the current to about $8\,\text{A}$, and the power is then $230\,\text{V} \cdot 8\,\text{A} \approx 1.8\,\text{kW}$. A single-phase charging station with a current of $16\,\text{A}$ charges with a power of about $3.7\,\text{kW}$, and a three-phase one with the same current at three times the power, about $11\,\text{kW}$. The same $40\,\text{kWh}$ charge takes more than a day from a socket, when the losses of charging are taken into account, and about four hours with a three-phase station.

```pysahdy
A three-phase charging station has a power of $6.9\,\text{kW}$ and the phase voltage is $230\,\text{V}$. What is the current in each phase conductor?
---
From $P = 3UI$ we get $I = \tfrac{P}{3U}$, so $I = \tfrac{6900\,\text{W}}{3 \cdot 230\,\text{V}} = 10\,\text{A}$.
```

### The home electrical system
The cable coming from the electricity grid goes through the meter to the **consumer unit**. In the consumer unit come first the **main fuses**, one in each phase conductor, for example $3 \cdot 25\,\text{A}$. After them the current divides into **circuits**: each circuit has its own cable and its own fuse or miniature circuit breaker, for example $10\,\text{A}$ or $16\,\text{A}$. A fuse protects the cable: it cuts the current before the current heats the cable dangerously (chapter *Electrical safety at home and at work*). That is why the size of a fuse is chosen according to the cross-sectional area of the cable, and a larger one must not be put in its place.

<svg data-fig="koti" viewBox="0 0 600 380" role="img" aria-label="Diagram, not to scale: the home electrical system. At the top left a cable with three phase conductors comes from the electricity grid to the consumer unit. In the consumer unit come first the main fuses, three of them, 25 amperes each, and below them the busbars from which three circuits leave. The top circuit is three-phase, its miniature circuit breaker is 16 amperes and it feeds the electric sauna heater. The middle circuit is single-phase, 16 amperes, and it feeds the sockets of the kitchen, to which a kettle is connected. The bottom circuit is the charging station&#x27;s own three-phase circuit: it has a 16 ampere miniature circuit breaker and a residual current device (RCD) with a tripping current of 30 milliamperes. The three-phase wires are drawn as three lines, the single-phase one as one." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-16-koti.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="112" y="15.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{grid}$</div></foreignObject>
  <foreignObject x="120" y="87.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$3 \cdot 25\,\text{A}$</div></foreignObject>
  <foreignObject x="101" y="121.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3 \cdot 16\,\text{A}$</div></foreignObject>
  <foreignObject x="317" y="135.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sauna heater}$</div></foreignObject>
  <foreignObject x="101" y="207.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16\,\text{A}$</div></foreignObject>
  <foreignObject x="317" y="221.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sockets}$</div></foreignObject>
  <foreignObject x="101" y="285.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3 \cdot 16\,\text{A}$</div></foreignObject>
  <foreignObject x="213" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30\,\text{mA}$</div></foreignObject>
  <foreignObject x="317" y="299.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{charging station}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/ev-charging-station.webp" alt="A yellow charging station in a parking garage, surrounded by yellow protective railings and yellow-and-black bollards."><figcaption>An electric car charging station in a parking garage in Jyväskylä, Finland. The station has its own circuit with its own fuse and residual current device, and the railings protect it from collisions.</figcaption></figure>

### Why a charging station has its own circuit and a residual current device
Charging a car is the longest large load in a home: the current can flow for hours at almost the size of the fuse of the circuit. If there were other sockets in the same circuit, the cable and the socket would be at almost the rated current for hours, the contacts of the socket would warm up, and other loads could cut the charging. That is why the electrical installation standard requires that every charging point has its **own circuit**, sized for its current. A charging point also has its own **residual current device (RCD)**: it cuts the current if part of it leaks along another route, for example through a wet cable and a person to the ground, and the difference is over $30\,\text{mA}$. Outdoors a cable gets wet, freezes and sometimes ends up under a wheel, so damage to the insulation is more likely than indoors. The enclosure of a station installed outdoors has an enclosure rating (IP rating), for example IP54, which tells that it withstands dust and splashing water.

### The main fuse and simultaneous loads
The main fuses limit the current of the whole house. When the main fuses are $3 \cdot 25\,\text{A}$, the house can draw at most about $3 \cdot 230\,\text{V} \cdot 25\,\text{A} \approx 17\,\text{kW}$ from the grid, and even then only if the load divides evenly between the three phases. What decides is the current of each phase conductor. In the figure the following are on at the same time: a $9.0\,\text{kW}$ sauna heater, which draws $13.0\,\text{A}$ from each phase, an $11\,\text{kW}$ charging station, which draws $16\,\text{A}$ from each phase, and in phase $\text{L}_1$ a kettle, $8.7\,\text{A}$. The current of phase $\text{L}_1$ is $37.7\,\text{A}$ and that of the others $29.0\,\text{A}$.

<svg data-fig="vaiheet" viewBox="0 0 600 340" role="img" aria-label="Horizontal bar chart, to scale: the current passing through the main fuses in each phase conductor L1, L2 and L3 when the following are on at the same time: a 9.0 kilowatt three-phase sauna heater, a 2.0 kilowatt kettle on phase L1 and an 11 kilowatt three-phase charging station. The heater draws 13.0 amperes from each phase and the charging station 16 amperes, the kettle 8.7 amperes from phase L1. The current of phase L1 is 37.7 amperes and that of phases L2 and L3 29.0 amperes. A vertical dashed line at 25 amperes is the size of the main fuse: the bar of every phase extends past it." style="max-width:100%;font-size:24px">
  <line x1="176" y1="56" x2="176" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="176" y1="284" x2="176" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="276" y1="56" x2="276" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="284" x2="276" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="259.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="376" y1="56" x2="376" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376" y1="284" x2="376" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="359.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="476" y1="56" x2="476" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="284" x2="476" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="459.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="46" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="75" y1="284" x2="490" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,284 L489,290 L489,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="508" y="269.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <line x1="76" y1="56" x2="76" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="18" y="81.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{L}_1$</div></foreignObject>
  <rect x="76" y="73" width="130.5" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="79" y="81.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sauna heater}$</div></foreignObject>
  <rect x="206.5" y="73" width="160" height="46" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="209.5" y="81.5" width="154" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{car}$</div></foreignObject>
  <rect x="366.5" y="73" width="87" height="46" fill="#a5d8ff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="369.5" y="81.5" width="81" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kettle}$</div></foreignObject>
  <foreignObject x="18" y="151.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{L}_2$</div></foreignObject>
  <rect x="76" y="143" width="130.5" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="79" y="151.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sauna heater}$</div></foreignObject>
  <rect x="206.5" y="143" width="160" height="46" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="209.5" y="151.5" width="154" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{car}$</div></foreignObject>
  <foreignObject x="18" y="221.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{L}_3$</div></foreignObject>
  <rect x="76" y="213" width="130.5" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="79" y="221.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sauna heater}$</div></foreignObject>
  <rect x="206.5" y="213" width="160" height="46" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="209.5" y="221.5" width="154" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{car}$</div></foreignObject>
  <line x1="326" y1="34" x2="326" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="221" y="7.5" width="210" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{main fuse}\ 25\,\text{A}$</div></foreignObject>
</svg>

A main fuse does not blow at once from a small overload, but if the overload is large enough and lasts long, it may blow and the whole house goes dark. That is why a charging station often has **load management**: it measures the current of the main fuses and reduces the charging current when other devices are on. When the heater draws $13.0\,\text{A}$, about $12\,\text{A}$ is left for the car in each phase, that is, about $8.3\,\text{kW}$. If the kettle is also switched on, only about $3\,\text{A}$ is left in phase $\text{L}_1$, so load management interrupts the charging for a moment.

### Heating of a cable and a joint
A cable is a resistor through which flows the same current as through the device. The current goes to the device along the phase conductor and returns along the neutral conductor, so there is copper twice the length of the cable. By Joule's law the power dissipated in the cable is $RI^2$ (chapter *Electric power and the heating of a resistor*): when the current doubles, the heating power becomes four times as great. A $25\,\text{m}$ extension cord on a reel, with conductors of $1.5\,\text{mm}^2$, has a resistance of about $0.57\,\Omega$, and with a current of $10\,\text{A}$ about $57\,\text{W}$ is dissipated in it. From the reel little energy is transferred as heat to the surroundings, so the reel gets hot, and the high temperature ages the insulation. The dielectric strength of the insulation can then weaken, and the insulation can fail.

A loose or oxidised joint is even more dangerous. The contact resistance of an old socket can be, for example, $0.10\,\Omega$, and with a current of $10\,\text{A}$ a power of $10\,\text{W}$ is dissipated in the joint. It is concentrated in a spot the size of a pea, and the charging lasts for hours. That is why a charging station is recommended for regular charging, and an extension cord is not used.

### Sources of the numerical values
The numerical values of the chapter are typical example values, not measurements of a particular car or house. The mains voltage $230\,\text{V}$ and the standard currents $10\,\text{A}$, $16\,\text{A}$ and $25\,\text{A}$ are common values of the Finnish electricity grid and home installations. The battery size $64\,\text{kWh}$ and the consumption $18\,\text{kWh}$ per hundred kilometres are of the order of magnitude of a small or medium-sized electric car. The efficiency $80\text{–}95\,\%$ is an estimate. The requirement of an own circuit and a residual current device for a charging point comes from the electrical installation standard SFS 6000-7-722, and Tukes (the Finnish Safety and Chemicals Agency) gives guidance on charging an electric car at home. The resistivity of copper is from the table in the chapter *Resistance and Ohm's law*.

## Formula: Charging time, charging power and heating of a cable
The efficiency of charging tells what fraction of the energy taken from the grid is stored in the battery:
```kaavat
efficiency :: \eta = \frac{W_\text{battery}}{W_\text{grid}}
```
where $\eta$ is the efficiency, $W_\text{battery}$ the energy stored in the battery ($\text{kWh}$) and $W_\text{grid}$ the energy taken from the grid ($\text{kWh}$).

When the charging power $P$ is constant, the energy taken from the grid is $W_\text{grid} = Pt$ (chapter *Electrical energy at home*). The charging time is therefore
```latex
t = \frac{W_\text{battery}}{\eta P}
```
where $t$ is the charging time ($\text{h}$) and $P$ the power taken from the grid ($\text{kW}$). In the model in the figure the power stays constant until the battery is at a charge level of about $90\,\%$. After that the power decreases, because the source voltage of the battery grows and the control circuit reduces the current (chapter *Batteries and the charging circuit*). The energy taken from the grid is the area under the curve. The formula therefore fits the steady part of charging, for example from a charge level of $20\,\%$ to $80\,\%$.

<svg data-fig="kayra" viewBox="0 0 600 360" role="img" aria-label="Diagram, a model and not a measurement: the power P taken from the grid by the charging station of an electric car in kilowatts as a function of time t in hours, when a 64 kilowatt-hour battery is charged from a charge level of 20 percent. The power stays at 11 kilowatts for about 4.5 hours, until the charge level is 90 percent. After that the power decreases ever more slowly, and charging ends at about 6.0 hours, when the charge level is 99 percent. The area under the steady part is shaded: it is the energy taken from the grid, power times time." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy616-energy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8590c"/><stop offset="1" stop-color="#ffc078"/></linearGradient></defs>
  <line x1="140.5" y1="300" x2="140.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197" y1="300" x2="197" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253.5" y1="300" x2="253.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310.5" y1="300" x2="310.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367" y1="300" x2="367" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="423.5" y1="300" x2="423.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="300" x2="480" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="261.5" x2="480" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="223.5" x2="480" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="185" x2="480" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="146.5" x2="480" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="108.5" x2="480" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="70" x2="480" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="300" x2="494" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,300 L493,306 L493,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="301" x2="84" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,44 L90,57 L78,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="140.5" y1="300" x2="140.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="130.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="197" y1="300" x2="197" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="187" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="253.5" y1="300" x2="253.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="243.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="310.5" y1="300" x2="310.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="367" y1="300" x2="367" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="423.5" y1="300" x2="423.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="413.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="480" y1="300" x2="480" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="470" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="77" y1="261.5" x2="84" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="247" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="77" y1="223.5" x2="84" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="209" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="77" y1="185" x2="84" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="77" y1="146.5" x2="84" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="132" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="77" y1="108.5" x2="84" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="94" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="77" y1="70" x2="84" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="55.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <foreignObject x="54" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{h})$</div></foreignObject>
  <foreignObject x="74" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P\ (\text{kW})$</div></foreignObject>
  <polygon points="84,300 84,89 340,89 340,300" fill="url(#fy616-energy)" fill-opacity="0.45"/>
  <polyline points="84,300 84,89 340,89 341,95 342,101 343,106.5 344,112 345.5,117.5 346.5,122.5 347.5,127.5 348.5,132.5 349.5,137.5 350.5,142 351.5,146.5 352.5,150.5 353.5,155 354.5,159 356,163 357,167 358,170.5 359,174.5 360,178 361,181.5 362,185 363,188 364,191 365.5,194.5 366.5,197.5 367.5,200 368.5,203 369.5,206 370.5,208.5 371.5,211 372.5,213.5 373.5,216 374.5,218.5 376,221 377,223 378,225 379,227.5 380,229.5 381,231.5 382,233.5 383,235 384,237 385.5,239 386.5,240.5 387.5,242.5 388.5,244 389.5,245.5 390.5,247 391.5,248.5 392.5,250 393.5,251.5 394.5,253 396,254 397,255.5 398,256.5 399,258 400,259 401,260.5 402,261.5 403,262.5 404,263.5 405.5,264.5 406.5,265.5 407.5,266.5 408.5,267.5 409.5,268.5 410.5,269.5 411.5,270 412.5,271 413.5,272 414.5,272.5 416,273.5 417,274 418,275 419,275.5 420,276.5 421,277 422,277.5 423,278.5 424,279 424,300" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="117" y="180" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$W_\text{grid} = Pt$</span></div></foreignObject>
  <circle cx="84" cy="89" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="94" y="52.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{charge}\ 20\,\%$</span></div></foreignObject>
  <circle cx="340" cy="89" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="265" y="52.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{charge}\ 90\,\%$</span></div></foreignObject>
  <circle cx="424" cy="279" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="349" y="234.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{charge}\ 99\,\%$</span></div></foreignObject>
</svg>

```pysahdy
$20\,\text{kWh}$ must be stored in the battery. The efficiency is $0.90$ and the charging power $5.0\,\text{kW}$. How long does charging take?
---
$t = \tfrac{W_\text{battery}}{\eta P}$. Substituting: $\tfrac{20\,\text{kWh}}{0.90 \cdot 5.0\,\text{kW}} \approx 4.4\,\text{h}$.
```

This chapter assumes that the current and voltage of the charging equipment are in phase, that is, the power factor is approximately one. Then the power of a single-phase device is $P = UI$. In an evenly loaded three-phase system, where the device draws the same current from each phase conductor, the total power in this model is
```latex
P = 3UI
```
where $U = 230\,\text{V}$ is the voltage between a phase conductor and the neutral conductor and $I$ the current of one phase conductor ($\text{A}$).

The heating power dissipated in a cable is obtained from Joule's law and the resistance of the conductor $R = \rho l : A$ (chapter *Resistance and Ohm's law*), when the length of copper is taken as the outgoing and return conductor together:
```latex
P_\text{cable} = \rho \frac{2l}{A} I^2
```
where $P_\text{cable}$ is the power dissipated in the cable ($\text{W}$), $\rho$ the resistivity of copper $1.7 \cdot 10^{-8}\,\Omega\cdot\text{m}$, $l$ the length of the cable ($\text{m}$), $A$ the cross-sectional area of one conductor ($\text{m}^2$) and $I$ the current ($\text{A}$).

The cost of charging is calculated from the energy taken from the grid, not from the energy stored in the battery:
```latex
K = a W_\text{grid}
```
where $K$ is the cost ($\text{€}$) and $a$ the total price of energy and transmission ($\text{€/kWh}$). Driving a hundred kilometres, $18\,\text{kWh}$ from the battery, needs $20\,\text{kWh}$ from the grid at an efficiency of $90\,\%$, and at a price of $15\,\text{c/kWh}$ it costs about $3.0\,\text{€}$.

## Worked example
The energy of the battery of the example car is $64\,\text{kWh}$. The battery is charged overnight from a charge level of $20\,\%$ to $80\,\%$ with a three-phase charging station that draws a current of $16\,\text{A}$ from each phase conductor. The phase voltage is $230\,\text{V}$, the efficiency of charging $90\,\%$, and the power stays constant during the whole charge. How long does charging take, and how much does it cost when the electricity costs $15\,\text{c/kWh}$ including transmission?

<!-- vaihe -->

**Given and find.** Energy of the battery $64\,\text{kWh}$, charge level $20\,\% \to 80\,\%$, $I = 16\,\text{A}$ in each of the three phases, $U = 230\,\text{V}$, $\eta = 0.90$, $a = 15\,\text{c/kWh}$. We are asked for the charging time $t$ and the cost $K$.

<!-- vaihe -->

**Principle.** $60\,\%$ of its energy has to be transferred to the battery. The station draws the same current from each of the three phases, so its power is three times the power of one phase. Because of the losses, the energy taken from the grid is the energy going into the battery divided by the efficiency, and the price is paid for the energy taken from the grid.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&P = 3UI \\
&t = \frac{W_\text{battery}}{\eta P} \\
&K = \frac{a W_\text{battery}}{\eta}
\end{aligned}
```

<!-- vaihe -->

**Conversions.** $W_\text{battery} = 0.60 \cdot 64\,\text{kWh} = 38.4\,\text{kWh}$, $\eta = 90\,\% = 0.90$ and $a = 15\,\text{c/kWh} = 0.15\,\text{€/kWh}$. The power is converted to kilowatts so that the time comes out in hours.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&P = 3UI \\
&\phantom{P} = 3 \cdot 230\,\text{V} \cdot 16\,\text{A} \\
&\phantom{P} = 11\,040\,\text{W} = 11.04\,\text{kW} \\
&t = \frac{W_\text{battery}}{\eta P} \\
&\phantom{t} = \frac{38.4\,\text{kWh}}{0.90 \cdot 11.04\,\text{kW}} \\
&\phantom{t} \approx 3.86\,\text{h} \\
&K = \frac{a W_\text{battery}}{\eta} \\
&\phantom{K} = \frac{0.15\,\text{€/kWh} \cdot 38.4\,\text{kWh}}{0.90} \\
&\phantom{K} = 6.40\,\text{€}
\end{aligned}
```

<!-- vaihe -->

**Answer.** Charging takes about $3.9\,\text{h}$ and costs about $6.4\,\text{€}$. The energy taken from the grid is $$\begin{aligned} &38.4\,\text{kWh} : 0.90 \\ &\approx 42.7\,\text{kWh} \end{aligned}$$. The results are given with two significant figures like the efficiency $0.90$ and the price $15\,\text{c/kWh}$.

<!-- vaihe -->

**Reasonableness.** Estimate: about $40\,\text{kWh}$ at a power of about $10\,\text{kW}$ takes about $4\,\text{h}$. Without losses charging would take $38.4\,\text{kWh} : 11.04\,\text{kW} \approx 3.5\,\text{h}$, so the losses make it longer, as they should. The price corresponds to about $210\,\text{km}$ of driving, about $3\,\text{€}$ per hundred kilometres, and charging fits easily in one night.

## Common misconception
Many people think that when a fuse blows repeatedly, a larger one can be put in its place. A fuse, however, does not protect the device but the cable: its size is chosen so that the cable does not get dangerously hot. A larger fuse lets through a current that heats the cable more than it can stand, and the insulation can melt or catch fire. The right solution is an own circuit, as for a charging station, or taking turns between the loads.

Another common mistake is to assume that filling a $64\,\text{kWh}$ battery takes $64\,\text{kWh}$ from the grid. Because of the losses, more is taken from the grid: the energy going into the battery is divided by the efficiency, not multiplied by it.

## Summary
- The charging time is the energy to be transferred to the battery divided by the product of the efficiency and the power, $t = W_\text{battery} : (\eta P)$. The efficiency is below $100\,\%$, because there are always losses in charging, so more energy is taken from the grid than is stored in the battery, and the price is paid for the energy taken from the grid.
- The power of single-phase charging is $P = UI$ and that of three-phase charging $P = 3UI$, when each phase conductor carries the same current. With the same current of $16\,\text{A}$, a three-phase station charges three times as fast.
- The main fuses limit the current of each phase conductor. The currents in the same phase are added, and load management reduces the charging current when the sauna heater or other devices are on.
- A charging station has its own circuit and its own residual current device: charging is a long, large load, and outdoors the insulation of a cable can be damaged.
- The heating power of a cable is $RI^2$: a doubled current makes it four times as great. A coiled extension cord and a loose joint get hot: little energy is transferred from the reel as heat to the surroundings, and in a loose joint the heating power is concentrated in a small spot.
