# The transformer and the transmission of electrical energy

> **Why** is electricity carried from a power plant to a city at a voltage of $400\,\text{kV}$, when the voltage at a socket at home is only $230\,\text{V}$?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on the left, beside a river, a power plant and its transformer, from which a long power line leaves. Large lattice pylons carry the conductors over fields and forest towards a city seen far away on the right, where lights are on in the windows." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A transformer changes an alternating voltage
A transformer has a closed iron core and two coils wound around it. An alternating voltage is connected to the **primary coil**, and the voltage for the device is taken from the **secondary coil**. The coils do not touch each other, and no current flows between them along a conductor. The alternating current of the primary coil produces in the iron core a magnetic field whose magnitude and direction vary in step with the current. The iron core guides almost the whole magnetic flux around the core and so also through the secondary coil. In the chapter *Electromagnetic induction* we saw that a changing magnetic flux induces a voltage in a coil. Therefore an alternating voltage is produced in the secondary coil, with the same frequency as the primary voltage.

<svg data-fig="transformer" viewBox="0 0 600 360" role="img" aria-label="Schematic picture of a transformer, not to scale. A primary coil with more turns is wound on the left limb of a closed iron core, and a secondary coil with fewer turns on the right limb. The primary coil is connected to an alternating voltage source whose voltage is U1, and the secondary coil to a lamp whose voltage is U2. A green dashed line with arrows circles inside the iron core: the changing magnetic flux produced by the primary current also passes along the core through the secondary coil." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-transformer.webp" x="1.2" y="1.2" width="597" height="368.2" preserveAspectRatio="none"/>
  <foreignObject x="290" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Phi$</div></foreignObject>
  <foreignObject x="-6" y="165.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_1$</div></foreignObject>
  <foreignObject x="528.5" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_2$</div></foreignObject>
  <foreignObject x="81.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="487.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="222" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N_1$</div></foreignObject>
  <foreignObject x="345" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$N_2$</div></foreignObject>
  <foreignObject x="77.5" y="317.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{primary coil}$</div></foreignObject>
  <foreignObject x="246" y="317.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{iron core}$</div></foreignObject>
  <foreignObject x="365" y="317.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{secondary coil}$</div></foreignObject>
</svg>

### The number of turns decides the voltage
The same changing magnetic flux passes through every turn of both coils, so an equal voltage is induced in every turn. The voltage of a coil is the sum of the voltages of its turns, so it is proportional to the number of turns. In an ideal transformer the ratio of the primary and secondary voltages is therefore the same as the ratio of the numbers of turns of the coils, the **turns ratio**. When the secondary coil has more turns than the primary coil, the transformer raises the voltage (a step-up transformer). When the secondary coil has fewer turns, the transformer lowers the voltage (a step-down transformer).

### A transformer needs a changing magnetic flux
A voltage is induced in the secondary coil only when the magnetic flux through it changes. If the primary coil is connected to a battery, a steady direct current flows in the coil, and the magnetic field of the iron core is constant. A constant magnetic flux does not induce a voltage, so the voltage of the secondary coil is zero. A voltage pulse is produced only at the moment when the current is switched on or off, because then the flux changes. This is why the power grid uses alternating current: in the chapter *The generator and alternating current* a generator produces an alternating voltage, and with transformers its size can be changed to suit each purpose.

```pysahdy
The primary coil is connected to a battery, and the switch has been closed for a long time. What is the voltage of the secondary coil while the current of the primary coil is constant?
---
The voltage of the secondary coil is zero. A constant current gives a constant magnetic flux, and a constant flux does not induce a voltage.
```

### Power is conserved, current changes
An ideal transformer does not consume energy, so the power coming into the primary coil is equal to the power leaving the secondary coil. When the load is resistive, power is the product of voltage and current, so when a transformer raises the voltage tenfold, the current falls to a tenth. A transformer therefore does not add energy or power: it exchanges a large current for a high voltage or the other way round. In a real transformer some of the energy becomes internal energy in the resistance of the coils and in the eddy currents of the iron core. That is why the core is built of thin plates insulated from each other (chapter *Lenz's law and eddy currents*). The efficiency of large power-plant transformers is over $99\,\%$.

### Transmission loss and high voltage
A power line has resistance, and the current flowing in the line heats it. The power that becomes internal energy is proportional to the square of the current, so it pays to keep the current small. The same power can be transmitted at a high voltage and a small current. When the voltage is raised tenfold, the current falls to a tenth and the power loss to a hundredth. That is why the voltage of the generator of a power plant is raised with a transformer to **high voltage**. The voltages of the Finnish transmission grid, maintained by Fingrid, are $400\,\text{kV}$, $220\,\text{kV}$ and $110\,\text{kV}$. The losses of the transmission grid correspond to about $2\,\%$ of the electricity used in Finland (Fingrid, *Yhteisillä linjoilla* 2026, data for 2025).

<svg data-fig="grid" viewBox="0 0 640 372" role="img" aria-label="Schematic picture of the power grid as a single-line diagram, not to scale: real three-phase lines have three phase conductors. In the top row the generator voltage of the power plant, 20 kV, is raised by a transformer to 400 kilovolts, and the large pylons of the transmission grid carry the electricity to a substation. At the substation a transformer lowers the voltage, and in the bottom row the small pylons of the distribution network carry the 20 kV voltage to a local substation, which lowers it to the voltage of the low-voltage network: the sockets of homes have 230 volts." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-grid.webp" x="0" y="0" width="640" height="382.7" preserveAspectRatio="none"/>
  <foreignObject x="89" y="103.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="275" y="29.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400\,\text{kV}$</div></foreignObject>
  <foreignObject x="221" y="181.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{transmission grid}$</div></foreignObject>
  <foreignObject x="496" y="183.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{substation}$</div></foreignObject>
  <foreignObject x="307" y="239.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="227.5" y="335.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{distribution network}$</div></foreignObject>
  <foreignObject x="141.5" y="233.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{transformer}$</div></foreignObject>
  <foreignObject x="51" y="197.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$230\,\text{V}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/transformer-750kv.webp" alt="A large pale transformer on grass, with long insulators and a tank on top; behind it are the steel structures and lines of a substation."><figcaption>A transformer whose higher voltage is $750\,\text{kV}$. When power is transmitted at high voltage, the current in the lines is small, and the transmission loss $P = RI^2$ stays small.</figcaption></figure>

### The voltage is lowered step by step
At substations, transformers lower the voltage to $110\,\text{kV}$ in the regional network and $20\,\text{kV}$ in the distribution network, and the distribution transformer of a residential area lowers, for example, the $20\,\text{kV}$ voltage to the voltage of the low-voltage network. In the low-voltage network there is about $400\,\text{V}$ between the phase conductors and about $230\,\text{V}$ between a phase conductor and the neutral conductor, which is the voltage of a socket at home.

High voltage is not brought into homes, because insulating it requires long insulators and large distances, and touching it would be fatal (chapter *Electrical safety at home and at work*). The charger of a phone lowers the voltage still further to about $5\,\text{V}$. A modern charger first changes the mains voltage to a very high frequency, so that the transformer can be small, and rectifies it at the end. The coils of the charger's transformer do not touch each other, so the phone is not conductively connected to the power grid.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a small phone charger is plugged into a wall socket, and its cable leads to a phone on a table, which is charging." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>

## Formula: Transformer and transmission loss
The voltages and currents of an ideal transformer depend on the numbers of turns of the coils:
```kaavat
transformer :: \frac{U_1}{U_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}
```
where $U_1$ is the primary voltage (V), $U_2$ the secondary voltage (V), $N_1$ and $N_2$ the numbers of turns of the primary and secondary coils and $I_1$ and $I_2$ the primary and secondary currents (A). The ratio $N_1 : N_2$ is the turns ratio. The latter equality follows from the conservation of power: $U_1 I_1 = U_2 I_2$. The voltages and currents are effective (rms) values (chapter *The generator and alternating current*). When the voltage increases, the current decreases in the same proportion.

```pysahdy
The primary coil of a transformer has $460$ turns and its voltage is $230\,\text{V}$. The secondary coil has $40$ turns. What is the secondary voltage when the transformer is ideal?
---
The voltages are in the same ratio as the numbers of turns, so $U_2 = U_1 \cdot \tfrac{N_2}{N_1} = 230\,\text{V} \cdot \tfrac{40}{460} = 20.0\,\text{V}$.
```

### Power loss of a transmission line
The principle of power transmission is illustrated with a simplified two-wire circuit: the current flows to the destination along one conductor and returns along the other. A power plant sends a power $P$ at a voltage $U$. The current of the line and the power that becomes internal energy in the line are
```latex
\begin{aligned}
&P = U I \\
&P_\text{h} = R I^2 = \frac{R P^2}{U^2}
\end{aligned}
```
where $P$ is the transmitted power (W), $U$ the transmission voltage (V), $I$ the current of the line (A), $R$ the combined resistance of both conductors (Ω) and $P_\text{h}$ the power loss (W). When the same power is transmitted at double the voltage, the current halves and the power loss falls to a quarter. The transmission voltage $U$ is not the voltage across the resistance of the line: the voltage drop between the ends of the line is only $R I$, so the power loss must not be calculated with the expression $U^2 : R$.

<svg data-fig="loss-graph" viewBox="0 0 600 340" role="img" aria-label="Graph, to scale: the share of the transmitted power that becomes internal energy in a transmission line, as a percentage, as a function of the transmission voltage in kilovolts, when the transmitted power is 200 MW and the resistance of the line 6.0 ohms in the simplified two-wire model. The curve falls steeply: at 100 kV the share is 12 %, at 200 kV 3.0 % and at 400 kV 0.75 %. When the voltage doubles, the share falls to a quarter." style="max-width:100%;font-size:24px">
  <line x1="143" y1="290" x2="143" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="189.5" y1="290" x2="189.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="290" x2="236" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="290" x2="283" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="290" x2="330" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376.5" y1="290" x2="376.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="423" y1="290" x2="423" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="244" x2="470" y2="244" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="198" x2="470" y2="198" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="152" x2="470" y2="152" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="106" x2="470" y2="106" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="143" y1="290" x2="143" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="189.5" y1="290" x2="189.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="167" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="236" y1="290" x2="236" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283" y1="290" x2="283" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="260.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="330" y1="290" x2="330" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="376.5" y1="290" x2="376.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="354" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="423" y1="290" x2="423" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="244" x2="96" y2="244" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="229.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="198" x2="96" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="183.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="152" x2="96" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="106" x2="96" y2="106" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{kV})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{h} : P\ (\%)$</div></foreignObject>
  <polyline points="161.5,64.5 164,81.5 166.5,96.5 169,109.5 171.5,121.5 174.5,132.5 177,142.5 179.5,151.5 182,159.5 184.5,167 187,174 189.5,180 192.5,186 195,191.5 197.5,196 200,201 202.5,205 205,209 207.5,212.5 210.5,216 213,219.5 215.5,222.5 218,225 220.5,228 223,230.5 225.5,232.5 228.5,235 231,237 233.5,239 236,241 238.5,242.5 241,244 243.5,246 246.5,247.5 249,248.5 251.5,250 254,251.5 256.5,252.5 259,253.5 261.5,255 264.5,256 267,257 269.5,258 272,259 274.5,259.5 277,260.5 279.5,261.5 282.5,262 285,263 287.5,263.5 290,264.5 292.5,265 295,265.5 297.5,266.5 300.5,267 303,267.5 305.5,268 308,268.5 310.5,269 313,269.5 315.5,270 318.5,270.5 321,271 323.5,271.5 326,272 328.5,272 331,272.5 333.5,273 336.5,273.5 339,273.5 341.5,274 344,274.5 346.5,274.5 349,275 351.5,275 354.5,275.5 357,276 359.5,276 362,276.5 364.5,276.5 367,277 369.5,277 372.5,277.5 375,277.5 377.5,278 380,278 382.5,278 385,278.5 387.5,278.5 390.5,279 393,279 395.5,279 398,279.5 400.5,279.5 403,280 405.5,280 408.5,280 411,280.5 413.5,280.5 416,280.5 418.5,280.5 421,281 423.5,281 426.5,281 429,281.5 431.5,281.5 434,281.5 436.5,281.5 439,282 441.5,282 444.5,282 447,282 449.5,282.5 452,282.5 454.5,282.5 457,282.5 459.5,282.5 462.5,283 465,283 467.5,283 470,283" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="189.5" y1="179.5" x2="189.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="179.5" x2="189.5" y2="179.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="189.5" cy="179.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="283" y1="262.5" x2="283" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="262.5" x2="283" y2="262.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="283" cy="262.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="470" y1="283" x2="470" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="283" x2="470" y2="283" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="470" cy="283" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="203.5" y="165" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$12\,\%$</span></div></foreignObject>
  <foreignObject x="289" y="222" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$3.0\,\%$</span></div></foreignObject>
  <foreignObject x="383" y="242.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0.75\,\%$</span></div></foreignObject>
  <foreignObject x="300" y="77.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P = 200\,\text{MW}$</div></foreignObject>
  <foreignObject x="320" y="115.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R = 6.0\,\Omega$</div></foreignObject>
</svg>

```pysahdy
A power plant transmits the same power along a line, but the transmission voltage is raised to three times its value. How does the power loss of the line change?
---
The current falls to a third, because $I = P : U$. The power loss $P_\text{h} = R I^2$ falls to a ninth, because the square of the current falls to a ninth.
```

### The real transmission grid is three-phase
The real Finnish transmission grid is three-phase: a line has three phase conductors, and for example $400\,\text{kV}$ is the voltage between the phase conductors, the line voltage. The active power of an evenly loaded three-phase grid is
```latex
P = \sqrt{3}\,U I \cos\varphi
```
where $P$ is the transmitted active power (W), $U$ the line voltage (V), $I$ the current of a phase conductor (A) and $\cos\varphi$ the power factor. The power factor is one when the current and the voltage are in phase. At the same voltage, current and power factor, a three-phase line therefore transmits about $1.73$ times the power of the two-wire model. The principle is the same, however: a high transmission voltage reduces the current and the losses. The calculation tasks of this chapter deliberately use the simplified two-wire model $P = UI$ unless the task says otherwise.

## Worked example
The transformer of a substation lowers the voltage of the regional network, $110\,\text{kV}$, to the distribution network voltage of $20\,\text{kV}$. The secondary coil has $360$ turns, and the current going into the distribution network is $450\,\text{A}$. How many turns does the primary coil have, and how large a current flows in the primary coil? Assume the transformer to be ideal.

<!-- vaihe -->

**Given and find.** Primary voltage $U_1 = 110\,\text{kV}$, secondary voltage $U_2 = 20\,\text{kV}$, number of turns of the secondary coil $N_2 = 360$ and secondary current $I_2 = 450\,\text{A}$. We are asked for the number of turns $N_1$ of the primary coil and the primary current $I_1$.

<!-- vaihe -->

**Principle.** In an ideal transformer the same changing magnetic flux passes through both coils, so the voltages are in the same ratio as the numbers of turns. The transformer does not consume energy, so power is conserved, $U_1 I_1 = U_2 I_2$, and the currents are in inverse proportion to the voltages.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\frac{U_1}{U_2} = \frac{N_1}{N_2} \;\Rightarrow\; N_1 = \frac{N_2 U_1}{U_2} \\[6pt]
&\frac{U_1}{U_2} = \frac{I_2}{I_1} \;\Rightarrow\; I_1 = \frac{I_2 U_2}{U_1}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: in both formulas the voltages form a quotient, so the kilovolts cancel. Both voltages are in the same unit, $\text{kV}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&N_1 = \frac{N_2 U_1}{U_2} \\
&= \frac{360 \cdot 110\,\text{kV}}{20\,\text{kV}} \\
&= 1980 \\[6pt]
&I_1 = \frac{I_2 U_2}{U_1} \\
&= \frac{450\,\text{A} \cdot 20\,\text{kV}}{110\,\text{kV}} \\
&= 81.82\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Result.** The primary coil has $1980$ turns, and the primary current is $I_1 \approx 82\,\text{A}$. The current is given to two significant figures, like the voltage $20\,\text{kV}$.

<!-- vaihe -->

**Reasonableness.** The transformer lowers the voltage, so the primary coil must have more turns and a smaller current than the secondary coil, as in the result. Power is conserved: $110\,\text{kV} \cdot 81.82\,\text{A} = 9.0\,\text{MW}$ and $20\,\text{kV} \cdot 450\,\text{A} = 9.0\,\text{MW}$.

## Common misconception
Many people calculate the power loss of a power line with the expression $P = U^2 : R$ and conclude that a higher voltage increases the losses. In that expression, however, $U$ is the voltage across the resistor. The transmission voltage is the voltage between the conductors, or between the conductors and the ground, and across the resistance of the line there is only a small voltage drop $R I$. The correct way is to calculate first the current $I = P : U$ and then the power loss $P_\text{h} = R I^2$: a higher voltage reduces the current and the losses. Another mistake is to think that a transformer that raises the voltage increases the power. In an ideal transformer power is conserved, so when the voltage increases, the current decreases. A third mistake is to assume that a transformer also works with a battery. It needs a changing magnetic flux, that is, alternating current.

## Summary
- In a transformer the alternating current of the primary coil produces a changing magnetic flux in the iron core, and the flux induces an alternating voltage in the secondary coil. With direct current the flux does not change, and the transformer does not work.
- In an ideal transformer $U_1 : U_2 = N_1 : N_2 = I_2 : I_1$. Power is conserved, so when the voltage increases, the current decreases.
- The power loss of a transmission line is $P_\text{h} = R I^2$, where $I = P : U$. Double the transmission voltage reduces the loss to a quarter.
- Electricity is transmitted over long distances at high voltage: the voltages of the Finnish transmission grid are $400\,\text{kV}$, $220\,\text{kV}$ and $110\,\text{kV}$, and transformers lower the voltage step by step to the $400\,\text{V}$ and $230\,\text{V}$ of the low-voltage network.
- Calculations use the simplified two-wire model $P = UI$. The real transmission grid is three-phase: $400\,\text{kV}$ is the line voltage, and the active power is $P = \sqrt{3}\,U I \cos\varphi$.
