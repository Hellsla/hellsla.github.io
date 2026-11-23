# Direct-current circuits and electrical energy

> **Why** does the cottage battery last more than a week for the LED lights alone, but only a day together with the cool box?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a red summer cottage on a lakeshore at dusk. The sky is dark blue above and warm orange at the horizon, with a crescent moon and a few stars. Warm yellow light shines from the windows of the cottage. In the yard there is a solar panel on a stand, and its cable runs to a grey battery box on the wall of the cottage. On the porch steps there is a blue cool box. On the shore there is a jetty and a rowing boat, in the background the spruce forest of the opposite shore, and a birch and spruces grow beside the cottage." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-tasavirta-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

In a direct-current circuit the source maintains a **voltage**, and the voltage drives a **current** through the circuit. The size of the current is set by the resistance of the whole circuit, so the same battery gives different currents to different loads. Current is not used up in a component: the component transforms the electrical energy carried by the charges into light, motion or internal energy. **Power** tells how fast energy is transformed.

<svg data-fig="kartta" viewBox="0 0 380 866" role="img" aria-label="Recognition chart: how do I tell which law to use? Draw the circuit diagram first and see which sign in the task fits. Charge flows in a time: the current is the charge divided by the time. Voltage and current are known: the resistance follows from Ohm&#x27;s law, the voltage is the resistance times the current. Dimensions and material of a wire: the resistance is the resistivity times the length divided by the cross-sectional area. Connected in series: the current is the same and the total resistance is the sum of the resistances. Connected in parallel: the voltage is the same and the reciprocal of the total resistance is the sum of the reciprocals. Current branches: the currents into a junction add up to the currents out of it. Closed loop: the sum of the voltages is zero. Power or energy of a device: the power is the voltage times the current. A battery has internal resistance: the terminal voltage is derived by going once round the circuit, the sum of the voltages is zero." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{draw the circuit first, then the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{charge flows in a time}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{current}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$I = \Delta Q/\Delta t$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{voltage and current are known}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{resistance}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$U = RI$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{dimensions and material of a wire}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{resistance}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$R = \rho\ell/A$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{connected in series}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{same current}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$R_\text{tot} = \Sigma R$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{connected in parallel}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{same voltage}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$1/R_\text{tot} = \Sigma 1/R$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{current branches}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{junction}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma I_\text{in} = \Sigma I_\text{out}$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{closed loop}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{voltages}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\Delta V = 0$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{power or energy of a device}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{power}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$P = UI$</div></foreignObject>
  <line x1="14" y1="822" x2="30" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="786" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="796.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a battery has internal resistance}$</div></foreignObject>
  <line x1="40" y1="826" x2="362" y2="826" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="831" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{derive by a loop}$</div></foreignObject>
  <rect x="238" y="830" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="832" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\Delta V = 0$</div></foreignObject>
</svg>

In a circuit problem in the exam it pays to work out the connection first. The same current passes through components connected in series, and the voltage across components connected in parallel is the same. After that Kirchhoff's laws and Ohm's law give the currents and voltages, and the power and energy follow from them.

This answers the opening question. The devices of the cottage are connected to the battery in parallel, so the voltage across each is $12\,\text{V}$. The LED lights take a current of $\tfrac{6.0\,\text{W}}{12\,\text{V}} = 0.50\,\text{A}$ and the cool box $\tfrac{48\,\text{W}}{12\,\text{V}} = 4.0\,\text{A}$, and the battery supplies their sum $4.5\,\text{A}$. The battery capacity of $100\,\text{Ah}$ lasts $200\,\text{h}$, that is, more than eight days, for the lights alone, but only about $22\,\text{h}$ for both.

<svg data-fig="mokki" viewBox="0 0 600 356" role="img" aria-label="Circuit diagram, not to scale. On the left a 12-volt battery, positive terminal at the top. Two branches are connected in parallel to the battery: LED lights with a power of 6.0 watts and a cool box with a power of 48 watts. Violet current arrows: a current of 4.5 amperes leaves the positive terminal of the battery and divides at the junction into a current of 0.50 amperes to the LED lights and a current of 4.0 amperes to the cool box. The currents of the branches join in the lower wire and return to the negative terminal of the battery." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-tasavirta-mokki.webp" x="1.2" y="1.2" width="597" height="360.7" preserveAspectRatio="none"/>
  <foreignObject x="94" y="158.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="96" y="198.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$12\,\text{V}$</div></foreignObject>
  <foreignObject x="282" y="164.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{LED}$</div></foreignObject>
  <foreignObject x="282" y="198.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$6.0\,\text{W}$</div></foreignObject>
  <foreignObject x="436" y="164.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{cool box}$</div></foreignObject>
  <foreignObject x="436" y="198.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$48\,\text{W}$</div></foreignObject>
  <foreignObject x="120" y="25.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$4.5\,\text{A}$</div></foreignObject>
  <foreignObject x="153" y="252.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$0.50\,\text{A}$</div></foreignObject>
  <foreignObject x="326" y="252.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$4.0\,\text{A}$</div></foreignObject>
  <foreignObject x="120" y="329.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$4.5\,\text{A}$</div></foreignObject>
</svg>

```pysahdy
Why is the voltage across both the LED lights and the cooler $12\,\text{V}$?
---
The devices are connected to the battery in parallel, and components connected in parallel have the same voltage across them as the source.
```

## Formula: Direct-current circuits and electrical energy

### Current, voltage and resistance

```kaavat
electric current :: I = \frac{\Delta Q}{\Delta t}
voltage drop across a conductor :: U = RI
resistance of a conductor :: R = \rho\,\frac{\ell}{A}
```

where $I$ is the current ($\text{A}$), $\Delta Q$ the charge that has passed through a cross-section ($\text{C}$), $\Delta t$ the time ($\text{s}$), $U$ the voltage across the component ($\text{V}$), $R$ the resistance ($\Omega$), $\rho$ the resistivity ($\Omega\cdot\text{m}$), $\ell$ the length of the wire ($\text{m}$) and $A$ the cross-sectional area ($\text{m}^2$). By Ohm's law the resistance of a metal conductor is constant when the temperature stays the same. The resistance of a filament lamp increases as the filament heats up. An ammeter is connected in series and a voltmeter in parallel.

### Connections and Kirchhoff's laws

```kaavat
total resistance of resistors in series :: R_\text{tot} = \Sigma R
total resistance of resistors in parallel :: \frac{1}{R_\text{tot}} = \Sigma\frac{1}{R}
Kirchhoff's first law :: \Sigma I_\text{in} = \Sigma I_\text{out}
Kirchhoff's second law :: \Sigma \Delta V = 0
```

The first is the total resistance $R_\text{tot}$ of resistors connected in series and the second of resistors connected in parallel; $\Sigma$ means a sum, and in the current law $I_\text{in}$ are the currents into a junction and $I_\text{out}$ those out of it. The current law holds at a junction, because charge is conserved. The voltage law holds when a loop is gone round once: the potential $V$ rises in the source from the negative terminal to the positive terminal and falls by $RI$ across a resistor in the direction of the current. That is why the voltage across parallel branches is the same.

### Power and energy

```kaavat
power consumed in a conductor :: P = UI
power :: P = \frac{W}{\Delta t}
```

where $P$ is the power ($\text{W}$) and $W$ the electrical energy transformed in the time $\Delta t$ ($\text{J}$ or $\text{kWh}$). The form $P = UI$ holds for every component. The power of a resistor can also be found from the current alone or from the voltage alone by substituting Ohm's law (Derive it yourself below). In series the larger resistance gets the larger power, in parallel the smaller. Units of energy are converted by substitution: $1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3.6\,\text{MJ}$. The letter $W$ is used for energy, because $E$ is the emf.

```pysahdy
Two resistors are connected in series. Which one gets the greater power?
---
The one with the greater resistance. In series the current $I$ is the same, so the power $P = RI^2$ grows with the resistance.
```

```johda
Derive the power $P$ of a resistor in terms of the current $I$ and in terms of the voltage $U$.
---
The power is $P = UI$, and by Ohm's law the voltage across the resistor is $U = RI$. Substitute the voltage into the power:

$$P = UI = RI \cdot I = RI^2$$

By Ohm's law the current is $I = \tfrac{U}{R}$. Substitute the current into the power:

$$P = UI = U \cdot \frac{U}{R} = \frac{U^2}{R}$$

These forms hold only for a resistor that obeys Ohm's law.
```

### Battery and accumulator

A battery is described by a model in which the emf $E$ ($\text{V}$) and the internal resistance $R_\text{s}$ ($\Omega$) are in series. When a current $I$ flows from the battery, part of the emf is used inside the battery, so the terminal voltage $U$ ($\text{V}$), the voltage between the terminals, is smaller than the emf. The resistance of the external circuit is $R$ ($\Omega$).

<svg data-fig="piiri" viewBox="0 0 600 330" role="img" aria-label="Circuit diagram, no numerical values. On the left a dashed box, the battery. Inside it the emf E, drawn with the symbol of a voltage source, and the internal resistance R s, drawn as a resistor, are in series. The terminals of the battery are on the right edge of the box, the positive terminal at the top and the negative terminal at the bottom, and between them the terminal voltage U. An external resistor R is connected to the terminals. A violet current I flows from the positive terminal through the resistor R back to the negative terminal." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-tasavirta-piiri.webp" x="9.7" y="1.2" width="582.5" height="327.7" preserveAspectRatio="none"/>
  <foreignObject x="64" y="251" width="74" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px;color:#6b7480">$\text{battery}$</div></foreignObject>
  <foreignObject x="184" y="121" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="96" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="91" y="190.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="324" y="71" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="324" y="223" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$-$</div></foreignObject>
  <foreignObject x="248" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$U$</div></foreignObject>
  <foreignObject x="494" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="380" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

```pysahdy
Why is the terminal voltage of a battery smaller than its emf when a current flows in the circuit?
---
Part of the emf is used up in the internal resistance of the battery. The terminal voltage is $U = E - R_\text{s}I$.
```

```johda
A resistor $R$ is connected to the terminals of a battery. Derive the current $I$ in the circuit and the terminal voltage $U$ of the battery.
---
Go once round the circuit in the direction of the current using Kirchhoff's second law. The potential rises by the emf $E$ in the source and falls by $R_\text{s}I$ in the internal resistance and by $RI$ in the external resistor:

$$E - R_\text{s}I - RI = 0$$

Solve for the current:

$$I = \frac{E}{R + R_\text{s}}$$

The terminal voltage is the voltage across the external resistor, the emf minus the voltage drop across the internal resistance:

$$U = RI = E - R_\text{s}I$$
```

```kaavat
electric current :: I = \frac{\Delta Q}{\Delta t}
```

where $Q$ is the capacity of the battery ($\text{Ah}$ or $\text{C}$), the charge $\Delta Q$ it gives in the time $\Delta t$. The model assumes that $E$ and $R_\text{s}$ stay constant. The energy of a battery is $W = UQ$, where $U$ is the rated voltage. During charging the current flows through the battery the other way, so the terminal voltage is larger than the emf.

The $(I, U)$ graph of a battery is a falling straight line. It crosses the vertical axis at the emf $E$ and the horizontal axis at the short-circuit current $I_\text{k} = \tfrac{E}{R_\text{s}}$, and its slope is $-R_\text{s}$.

<svg data-fig="napa" viewBox="0 0 600 380" role="img" aria-label="Schematic, no numerical values: the terminal voltage U of a battery as a function of the current I. A falling straight line starts on the vertical axis at the emf E and crosses the horizontal axis at the short-circuit current I k. A slope triangle is drawn on the line, with horizontal side delta I and vertical side delta U; the slope is minus R s. At the upper end of the line, at small currents, the terminal voltage is almost E." style="max-width:100%;font-size:24px">
  <line x1="79" y1="320" x2="484" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,320 L483,326 L483,314 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="321" x2="80" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,34 L86,47 L74,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="50" y="325.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="70" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <polyline points="80,103.5 431,320" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="80" cy="103.5" r="6" fill="#1971c2"/>
  <foreignObject x="48" y="89" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$E$</div></foreignObject>
  <circle cx="431" cy="320" r="6" fill="#c92a2a"/>
  <foreignObject x="414.5" y="331.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$I_\text{k}$</div></foreignObject>
  <line x1="177.5" y1="163.5" x2="314" y2="163.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="314" y1="163.5" x2="314" y2="248" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="229" y="129" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta I$</div></foreignObject>
  <foreignObject x="326" y="191" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta U$</div></foreignObject>
  <foreignObject x="298.5" y="106" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{slope } {-R_\text{s}}$</div></foreignObject>
</svg>

## Common mistakes {Virheet}

- **Current is used up.** The same current enters a component and leaves it; what changes in the component is energy, not current.
- **The source voltage for a series resistor.** Only part of the source voltage is across a resistor connected in series. First calculate the current, then $U_1 = R_1 I$.
- **The reciprocal is forgotten.** A calculation for a parallel connection first gives $\tfrac{1}{R}$, which is inverted at the end. The total resistance is smaller than the smallest resistance of a branch.
- **A filament lamp treated by Ohm's law.** The resistance of a hot filament is larger, so the resistance of the lamp is calculated as the ratio $U : I$ separately at each point.
- **The terminal voltage is always the rated voltage.** When current is drawn from a battery, the terminal voltage is smaller than the emf by $R_\text{s} I$.
- **The kilowatt-hour as power.** $\text{kWh}$ is a unit of energy: kilowatts are multiplied by hours, and minutes are first converted into hours.
- **Milliampere-hours as energy.** $\text{mAh}$ is a unit of charge, so batteries are compared by their energy $W = UQ$.

## Review if needed {Kertaa}

- The quantities of a circuit: [*Electric circuit, current and voltage*](fy6-1.html), [*Measurements in an electric circuit*](fy6-2.html) and [*Resistance and Ohm's law*](fy6-3.html).
- Connections: [*Resistors in series and in parallel*](fy6-4.html) and [*Kirchhoff's laws and potential in a circuit*](fy6-5.html).
- Power and energy: [*Electric power and the heating of a resistor*](fy6-6.html) and [*Electrical energy at home*](fy6-7.html).
- Sources: [*Electromotive force and internal resistance*](fy6-8.html) and [*Batteries and the charging circuit*](fy6-9.html).
