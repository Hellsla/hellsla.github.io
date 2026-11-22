# Electromotive force and internal resistance

> **Why** do the headlights of a car dim for a moment when the engine is started on a cold winter morning?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a dark winter morning. A small red car stands in a snowy yard, its headlight shining into the dusk and steam rising from its exhaust pipe: the car is being started. In the background is a red house with a snow-covered roof, light showing in its windows, and dark spruce trees." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A battery is a source and a resistor together
In a battery, chemical reactions separate charges from each other and maintain a voltage between the terminals. The **source voltage** $E$ of a battery (also called its electromotive force, or emf) tells how much energy the battery gives to each unit of charge passing through it: a source voltage of $1.5\,\text{V}$ means an energy of $1.5\,\text{J}$ for every coulomb. However, the current also passes inside the battery, through the electrolyte and the electrodes, and they have resistance too. This is called the **internal resistance** $R_\text{s}$ of the battery. A battery can therefore be described by a model in which an ideal voltage source $E$ is in series with a resistor $R_\text{s}$. In the chapter *Kirchhoff's laws and potential in a circuit* the source was ideal; now its own resistance is taken into account.

<svg data-fig="model" viewBox="0 0 600 344" role="img" aria-label="Circuit diagram, not to scale: the model of a battery. Inside the battery, bounded by a dashed line, is an ideal voltage source with source voltage E, and in series with it the internal resistance Rs. The positive terminal of the battery is at the top right and the negative terminal at the bottom right. Wires from the terminals lead to an external load resistor R. A voltmeter is connected between the terminals and measures the terminal voltage U. Purple arrows show the current I: in the external circuit from the positive terminal through the load to the negative terminal, and inside the battery from the negative terminal to the positive terminal." style="max-width:100%;font-size:24px">
  <rect x="30" y="58" width="192" height="256" rx="12" fill="#eef5f9" stroke="#6b7480" stroke-width="2" stroke-dasharray="8 6"/>
  <foreignObject x="71" y="17.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <polyline points="222,88 106,88 106,134" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="82" y1="134" x2="130" y2="134" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="94" y1="148" x2="118" y2="148" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <polyline points="106,148 106,196" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="94" y="196" width="24" height="60" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="106,256 106,284 222,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="62" y="113.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="62" y="141.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="140" y="126.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="128" y="211.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <path d="M106,168 L98,188 L114,188 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="120" y="163.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <polyline points="222,88 530,88 530,284 222,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="222" cy="88" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="222" cy="284" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="234" y="51.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="234" y="291.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <rect x="518" y="156" width="24" height="60" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="552" y="171.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <circle cx="352" cy="88" r="6" fill="#1f2933"/>
  <circle cx="352" cy="284" r="6" fill="#1f2933"/>
  <polyline points="352,88 352,166" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="352,206 352,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="352" cy="186" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="337" y="171.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="382" y="171.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$U$</div></foreignObject>
  <path d="M298,88 L278,80 L278,96 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="276" y="49.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <path d="M458,88 L438,80 L438,96 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M438,284 L458,276 L458,292 Z" fill="#7048e8" stroke-linejoin="round"/>
</svg>

### The terminal voltage decreases as the current grows
The voltage between the terminals of a battery is called the **terminal voltage** $U$. When a current $I$ is drawn from the battery, the potential rises in the ideal source by the source voltage $E$, but it drops in the internal resistance by the voltage $R_\text{s} I$, as in any resistor. The potential of the positive terminal relative to the negative terminal is therefore $E - R_\text{s} I$. In terms of energy, of each coulomb to which the source gives an energy $E$, a part $R_\text{s} I$ is changed into internal energy of the battery itself, and only the rest, $U$, is transferred to the external circuit. That is why a battery warms up when a large current is drawn from it.

<svg data-fig="potential" viewBox="0 0 600 360" role="img" aria-label="Potential graph, schematic: the potential V as a loop is traced from the negative terminal of the battery through the inside of the battery and the external load resistor R back to the negative terminal. At the negative terminal the potential is zero. In the ideal source it rises by the source voltage E, and in the internal resistance Rs of the battery it drops by the voltage Rs times I. At the positive terminal the potential is therefore the terminal voltage U, which is smaller than E. In the load resistor the potential drops by U back to zero." style="max-width:100%;font-size:24px">
  <line x1="95" y1="280" x2="490" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,280 L489,286 L489,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="281" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="508" y="265.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{place}$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V$</div></foreignObject>
  <rect x="139.5" y="64" width="21.5" height="216" fill="#eef5f9"/>
  <foreignObject x="128.5" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <rect x="204.5" y="64" width="54.5" height="216" fill="#eef5f9"/>
  <foreignObject x="209.5" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <rect x="367.5" y="64" width="54.5" height="216" fill="#eef5f9"/>
  <foreignObject x="372.5" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="64" y="259.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="96" y1="100" x2="150.5" y2="100" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="148" x2="259" y2="148" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="54" y="85.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="54" y="133.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$U$</div></foreignObject>
  <polyline points="96,280 150.5,280 150.5,100 204.5,100 259,148 313,148 367.5,148 421.5,280 476,280" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M266,100 H273 V148 H266" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="283" y="109.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s} I$</div></foreignObject>
  <line x1="96" y1="280" x2="96" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="84" y="289.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <circle cx="96" cy="280" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="313" y1="280" x2="313" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="301" y="289.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <circle cx="313" cy="148" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="476" y1="280" x2="476" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="464" y="289.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <circle cx="476" cy="280" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <path d="M96,322 V330 H313 V322" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="149.5" y="331.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{battery}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/lithium-ion-cells.webp" alt="Two light blue cylindrical battery cells in yellow holders on a wooden table; the labels read INR21700 and INR18650."><figcaption>Lithium-ion cells of types 21700 and 18650. The numbers give the size of the cell: a diameter of $21\,\text{mm}$ and a length of $70\,\text{mm}$, or $18\,\text{mm}$ and $65\,\text{mm}$. The internal resistance of such a cell is only tens of milliohms, so it can supply a large current without its terminal voltage dropping much.</figcaption></figure>

```pysahdy
A current of $2.0\,\text{A}$ passes inside a battery, and the internal resistance is $0.10\,\Omega$. How large is the voltage of the internal resistance?
---
The voltage is $R_\text{s} I$. So $0.10\,\Omega \cdot 2.0\,\text{A} = 0.20\,\text{V}$.
```

### The source voltage is measured without a current
When no current is drawn from the battery, the voltage $R_\text{s} I$ across the internal resistance is zero, and the terminal voltage is equal to the source voltage. The source voltage can therefore be measured by connecting just a voltmeter to the terminals of the battery, because a good voltmeter draws only a vanishingly small current. A new AA battery gives about $1.6\,\text{V}$ this way. The source voltage of a used battery can be almost as large, but its internal resistance has grown many times over. A voltmeter alone therefore does not reveal whether a battery is still usable: only under load does its terminal voltage drop clearly.

### A car battery at starting
The internal resistance of a car battery is very small, only hundredths of an ohm. However, the starter motor draws a current of hundreds of amperes for a moment, so the voltage $R_\text{s} I$ across the internal resistance of the battery is volts, and the terminal voltage drops clearly. The headlights are connected to the same terminals, so their voltage and power decrease for the same moment, and they dim. In the cold the chemical reactions of the battery slow down and the internal resistance grows, so the effect is stronger in frost.

### Short circuit
In a **short circuit** the terminals of a battery are connected by a conductor whose resistance is almost zero. Then the terminal voltage is almost zero, and only the internal resistance limits the current. The short-circuit current is the largest current that can be obtained from a battery: for a new AA battery it is about $1.60\,\text{V} : 0.20\,\Omega = 8.0\,\text{A}$, and for a car battery over a thousand amperes. The whole power of the source is then changed into internal energy of the battery and the conductor. The conductor may become red hot, and the battery may leak or heat up dangerously; a lithium battery may even catch fire. The terminals of a battery must therefore never be connected directly with a conductor, and loose batteries are not carried in a pocket with keys or coins.

```pysahdy
Why is the terminal voltage almost zero in a short circuit, even though the current is at its largest?
---
The conductor between the terminals has almost no resistance, so its voltage $RI$ is almost zero. The source voltage is used up in the internal resistance.
```

## Formula: Terminal voltage and short-circuit current
The terminal voltage of a battery when a current $I$ is drawn from it is
```latex
U = E - R_\text{s} I
```
where $U$ is the terminal voltage ($\text{V}$), $E$ the source voltage ($\text{V}$), $R_\text{s}$ the internal resistance ($\Omega$) and $I$ the current drawn from the battery ($\text{A}$). The model assumes that $E$ and $R_\text{s}$ stay constant. In a real battery they change slightly with the current, the temperature and the use of the battery.

When a load resistor $R$ is connected to the battery, Kirchhoff's voltage law gives for the loop $E - R_\text{s} I - R I = 0$. The current is therefore
```latex
I = \frac{E}{R + R_\text{s}}
```
where $R$ is the resistance of the external circuit ($\Omega$). The internal resistance acts like an additional resistor in series with the load. In a short circuit $R = 0$, and the current is the short-circuit current
```latex
I_\text{k} = \frac{E}{R_\text{s}}
```
where $I_\text{k}$ is the short-circuit current ($\text{A}$).

```pysahdy
The source voltage of a battery is $6.0\,\text{V}$ and its internal resistance is $0.50\,\Omega$. How large is the short-circuit current?
---
The short-circuit current is $I_\text{k} = E : R_\text{s}$. So $I_\text{k} = 6.0\,\text{V} : 0.50\,\Omega$, so $I_\text{k} = 12\,\text{A}$.
```

### Source voltage and internal resistance from a graph
The terminal voltage decreases steadily as the current grows, so the $(I, U)$ graph of a battery is a descending straight line. It meets the vertical axis at $U = E$, because without a current the terminal voltage is the source voltage, and the horizontal axis at the short-circuit current $I_\text{k}$. The slope of the line is $-R_\text{s}$, so the internal resistance is obtained from a triangle of the slope: $R_\text{s} = -\Delta U : \Delta I$. For the battery in the figure the terminal voltage decreases by $0.60\,\text{V}$ when the current grows by $2.0\,\text{A}$, so $R_\text{s} = 0.60\,\text{V} : 2.0\,\text{A} = 0.30\,\Omega$.

<svg data-fig="ui-graph" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: the terminal voltage U of a battery in volts as a function of the current I in amperes. The straight line starts on the vertical axis at the source voltage 1.50 V and descends steadily until it meets the horizontal axis at the short-circuit current 5.0 A. In the slope triangle the current grows from 1.0 amperes to 3.0 amperes, that is by 2.0 A, and the terminal voltage decreases by 0.60 V. The internal resistance is 0.60 V divided by 2.0 A, that is 0.30 ohms." style="max-width:100%;font-size:24px">
  <line x1="163.5" y1="290" x2="163.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="290" x2="230.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298" y1="290" x2="298" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="290" x2="365.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="290" x2="432.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="290" x2="500" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="252.5" x2="500" y2="252.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="215.5" x2="500" y2="215.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="178" x2="500" y2="178" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="140.5" x2="500" y2="140.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103.5" x2="500" y2="103.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="66" x2="500" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,40 L102,53 L90,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="163.5" y1="290" x2="163.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="230.5" y1="290" x2="230.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="298" y1="290" x2="298" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="288" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="365.5" y1="290" x2="365.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="355.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="432.5" y1="290" x2="432.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="422.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="500" y1="290" x2="500" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="490" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="252.5" x2="96" y2="252.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="238" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.3$</div></foreignObject>
  <line x1="89" y1="215.5" x2="96" y2="215.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="201" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.6$</div></foreignObject>
  <line x1="89" y1="178" x2="96" y2="178" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="163.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.9$</div></foreignObject>
  <line x1="89" y1="140.5" x2="96" y2="140.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="126" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.2$</div></foreignObject>
  <line x1="89" y1="103.5" x2="96" y2="103.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="89" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.5$</div></foreignObject>
  <line x1="89" y1="66" x2="96" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="51.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.8$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="86" y="9.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <line x1="163.5" y1="140.5" x2="298" y2="140.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="298" y1="140.5" x2="298" y2="215.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="205.5" y="106" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta I$</span></div></foreignObject>
  <foreignObject x="308" y="163.5" width="56" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta U$</span></div></foreignObject>
  <polyline points="96,103.5 432.5,290" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="96" cy="103.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432.5" cy="290" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="112" y="69" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$E$</div></foreignObject>
  <foreignObject x="436.5" y="253.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$I_\text{k}$</div></foreignObject>
</svg>

The internal resistance is determined experimentally as follows. An adjustable load resistor is connected to the battery, an ammeter in series and a voltmeter across the terminals of the battery. The terminal voltage and the current are measured with several values of the load, the points are plotted in an $(I, U)$ coordinate system and a straight line is fitted to them. In real series of measurements the points do not usually lie exactly on the same line because of measurement uncertainty. The source voltage is read from where the line meets the vertical axis, and the internal resistance is calculated from the slope of the line, read from the line at two points far apart. The short-circuit current is not measured, because a short circuit could damage the battery. It is calculated from the equation $I_\text{k} = E : R_\text{s}$ or obtained by extending the line to the horizontal axis. Extending beyond the range of measurement assumes that the internal resistance stays the same at large currents too.

### Batteries in series and in parallel
When batteries are connected in **series**, so that the positive terminal of each is connected to the negative terminal of the next, the rises of potential are added, and all the internal resistances are in the same loop one after the other. The source voltage and the internal resistance of the group are
```latex
\begin{aligned}
E &= E_1 + E_2 + \dots \\
R_\text{s} &= R_{\text{s}1} + R_{\text{s}2} + \dots
\end{aligned}
```
where $E_1$, $E_2$, … are the source voltages of the individual batteries ($\text{V}$) and $R_{\text{s}1}$, $R_{\text{s}2}$, … their internal resistances ($\Omega$). Three batteries in series in a torch give about $4.5\,\text{V}$. The source voltage of a battery put in the wrong way round is subtracted from the sum of the source voltages of the other batteries. So the source voltage of the group is smaller by twice the source voltage of the reversed battery than when all the batteries are the right way round. The internal resistance of the battery the wrong way round is still added to the others.

When $n$ identical batteries are connected in **parallel**, the positive terminals together and the negative terminals together, the source voltage of the group is the same as for one battery. The internal resistances are parallel branches among which the current is shared equally, so the internal resistance of the group is
```latex
R_\text{s} = \frac{R_{\text{s}1}}{n}
```
where $R_{\text{s}1}$ is the internal resistance of one battery ($\Omega$). Two new AA batteries in series give a source voltage of $3.20\,\text{V}$ and an internal resistance of $0.40\,\Omega$, and in parallel $1.60\,\text{V}$ and $0.10\,\Omega$. A parallel connection therefore does not raise the voltage, but it gives a larger current with a smaller drop of the terminal voltage. Only identical and equally full batteries are connected in parallel: otherwise the battery with the larger source voltage drives a current through the other, and both warm up for nothing.

<svg data-fig="connections" viewBox="0 0 600 360" role="img" aria-label="Two circuit diagrams side by side, not to scale. Each battery is drawn as its model: the source voltage E and the internal resistance Rs inside a dashed line. On the left two identical batteries are in series one above the other, the negative terminal of the upper to the positive terminal of the lower. The source voltage of the whole is 2E and the internal resistance 2Rs. On the right two identical batteries are in parallel side by side, the positive terminals together and the negative terminals together. The source voltage of the whole is E and the internal resistance half of Rs." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-8-connections.webp" x="0" y="0" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="75" y="13.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{series}$</div></foreignObject>
  <foreignObject x="162" y="91.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="148" y="135.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="162" y="191.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="148" y="235.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="86" y="47.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="86" y="275.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="65" y="313.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2E,\ 2R_\text{s}$</div></foreignObject>
  <foreignObject x="390" y="13.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{parallel}$</div></foreignObject>
  <foreignObject x="412" y="141.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="398" y="185.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="542" y="141.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="528" y="185.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="401" y="47.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="401" y="275.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="380" y="313.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E,\ \tfrac{1}{2} R_\text{s}$</div></foreignObject>
</svg>

## Worked example
Just a voltmeter is connected to the terminals of a new AA battery, and it shows $1.58\,\text{V}$. When a resistor of $4.0\,\Omega$ is also connected to the battery, the voltmeter shows $1.45\,\text{V}$. What is the internal resistance of the battery, and what would be its short-circuit current?

<!-- vaihe -->

**Given and find.** The voltage measured without a current is $1.58\,\text{V}$, the terminal voltage measured under load is $U = 1.45\,\text{V}$ and the load resistance is $R = 4.0\,\Omega$. We are asked for the internal resistance $R_\text{s}$ and the short-circuit current $I_\text{k}$.

<!-- vaihe -->

**Principle.** A voltmeter draws a vanishingly small current, so without a load it shows the source voltage: $E = 1.58\,\text{V}$. Under load the meter shows the terminal voltage, which is also the voltage of the resistor, so Ohm's law gives the current. The internal resistance is solved from the equation of the terminal voltage, and the short-circuit current from that.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&I = \frac{U}{R} \\
&U = E - R_\text{s} I \\
&R_\text{s} = \frac{E - U}{I} \\
&I_\text{k} = \frac{E}{R_\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Conversions.** Not needed: all the quantities are in base units, and $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
I &= \frac{U}{R} \\
&= \frac{1.45\,\text{V}}{4.0\,\Omega} = 0.3625\,\text{A} \\
R_\text{s} &= \frac{E - U}{I} \\
&= \frac{1.58\,\text{V} - 1.45\,\text{V}}{0.3625\,\text{A}} \\
&= 0.3586\,\Omega \\
I_\text{k} &= \frac{E}{R_\text{s}} \\
&= \frac{1.58\,\text{V}}{0.3586\,\Omega} = 4.406\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The internal resistance is about $0.36\,\Omega$ and the short-circuit current about $4.4\,\text{A}$. The results are given to two significant figures, because the difference of the voltages, $0.13\,\text{V}$, and the resistance $4.0\,\Omega$ are known to two figures.

<!-- vaihe -->

**Reasonableness.** Substitute the result back: $0.3586\,\Omega \cdot 0.3625\,\text{A} = 0.13\,\text{V}$, and $1.58\,\text{V} - 0.13\,\text{V} = 1.45\,\text{V}$ is the measured terminal voltage. The internal resistance is much smaller than the load $4.0\,\Omega$, so the terminal voltage is only a little smaller than the source voltage. The short-circuit current is a few amperes, as it should be for an AA battery.

## Common misconception
Many people think that a battery always gives the same current or that a battery holds a certain amount of current in store. A battery maintains an almost constant source voltage, and the current is determined by the resistance of the whole circuit: $I = E : (R + R_\text{s})$. The same battery gives a large current to a small load resistance and a small current to a large one. Nor is current used up in a battery, but chemical energy, which the source changes into electrical energy.

Another misconception is that the voltage of a battery is always the $1.5\,\text{V}$ printed on it. The marking gives the source voltage only approximately. The terminal voltage is smaller the larger the current drawn from the battery and the larger the internal resistance of the battery. A third mistake is to think that a parallel connection doubles the voltage: the source voltage of identical batteries in parallel is the same as for one, and only the internal resistance decreases.

## Summary
- A battery is described by a model in which an ideal source with source voltage $E$ is in series with the internal resistance $R_\text{s}$.
- The terminal voltage is $U = E - R_\text{s} I$: it decreases as the current grows. Without a current the terminal voltage is the source voltage.
- With a load resistor the current is $I = E : (R + R_\text{s})$. The short-circuit current $I_\text{k} = E : R_\text{s}$ is the largest possible current, and a short circuit is dangerous.
- The $(I, U)$ graph of a battery is a descending straight line: it meets the vertical axis at the source voltage, and its slope is $-R_\text{s}$.
- The source voltages and the internal resistances of batteries in series are added. The source voltage of identical batteries in parallel is the same as for one, and the internal resistance is $R_{\text{s}1} : n$.
