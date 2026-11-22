# Resistors in series and in parallel

> **Why** do all the bulbs of an old string of fairy lights go out when one bulb breaks, while at home the floor lamp stays on even when the desk lamp is switched off?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a living room on a winter evening. At the top of the window hangs an old string of Christmas lights whose bulbs are all dark, because one bulb is broken and dangles loose from its socket. The floor lamp and the desk lamp plugged into the sockets of the same extension cord shine brightly." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
An electric circuit often has more than one resistor or lamp. Two resistors can be connected to a battery in two ways: one after the other in the same loop, that is, in series, or in separate branches between the same two points, that is, in parallel. The way they are connected decides how the current and the voltage are shared between the resistors and how large a current leaves the battery. In this chapter the battery is ideal, that is, the voltage between its terminals does not depend on the current, and the resistance of the wires is ignored.

### Series connection
In a series connection the resistors are one after the other, and the charges have only one route. So the same current $I$ passes through every resistor. Current is not used up in a resistor: charge does not vanish or pile up anywhere in the circuit. The voltage across a resistor tells how much of the electrical energy of each charge is transformed into internal energy of the resistor, which is transferred to the surroundings as heat. The battery voltage is shared between the resistors, $U = U_1 + U_2$. By Ohm's law $U_1 = R_1 I$ and $U_2 = R_2 I$, so the larger voltage is across the larger resistance.

<svg data-fig="series" viewBox="0 0 600 344" role="img" aria-label="Circuit diagram, not to scale: a battery and two resistors R1 and R2 in series in the same loop. Purple current arrows run from the positive terminal of the battery through R1 and R2 and back to the negative terminal, and the label of every arrow is the same, I. The voltages U1 and U2, marked with blue brackets, are across the resistors, and the battery voltage is U." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-4-series.webp" x="0" y="0" width="600" height="355" preserveAspectRatio="none"/>
  <foreignObject x="30" y="143.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="30" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="126" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="229.5" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <foreignObject x="229.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$U_1$</div></foreignObject>
  <foreignObject x="389.5" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="389.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$U_2$</div></foreignObject>
  <foreignObject x="138" y="37.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="316" y="37.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="556" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="296" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="221" y="171.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{same current } I$</div></foreignObject>
</svg>

If a component connected in series breaks, for example the filament of a lamp burns through, the only route is opened and the current stops in the whole circuit. This is why all the bulbs of an old-style string of fairy lights go out when one of them breaks.

```pysahdy
The current through the first of two resistors in series is $0.20\,\text{A}$. How large is the current through the second resistor, and why?
---
The same, $0.20\,\text{A}$. There is only one path, and no charge disappears or piles up anywhere.
```

### Parallel connection
In a parallel connection the resistors are in separate branches between the same two branching points. The ends of both branches are joined by wires to the terminals of the battery, so the same voltage $U$ is across both resistors. At a branching point the current divides, and at the second branching point the branch currents join again: the current leaving the battery is the sum of the branch currents, $I = I_1 + I_2$. By Ohm's law the branch current is $I_1 = U : R_1$, so a larger current passes through the branch with the smaller resistance.

<svg data-fig="parallel" viewBox="0 0 600 404" role="img" aria-label="Circuit diagram, not to scale: a battery and two resistors R1 and R2 in parallel. The current I leaving the positive terminal of the battery divides at a branching point into two branches carrying the currents I1 and I2, and the currents join again at the second branching point. The same voltage U as between the terminals of the battery is across both resistors." style="max-width:100%;font-size:24px">
  <path d="M86,182 L86,86 L476,86 L476,306 L86,306 L86,210" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M236,86 L236,196 L476,196" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="56" y="182" width="60" height="28" fill="#ffffff"/>
  <line x1="58" y1="188" x2="114" y2="188" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="73" y1="204" x2="99" y2="204" stroke="#1f2933" stroke-width="8" stroke-linecap="butt"/>
  <foreignObject x="30" y="159.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="30" y="203.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="126" y="181.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <circle cx="236" cy="86" r="5.5" fill="#1f2933"/>
  <circle cx="476" cy="196" r="5.5" fill="#1f2933"/>
  <rect x="318" y="72" width="76" height="28" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="339.5" y="33.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <rect x="318" y="182" width="76" height="28" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="339.5" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <line x1="132" y1="70" x2="167" y2="70" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M180,70 L166,76.5 L166,63.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="146" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="408" y1="70" x2="439" y2="70" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M452,70 L438,76.5 L438,63.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="413.5" y="31.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <line x1="408" y1="180" x2="439" y2="180" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M452,180 L438,186.5 L438,173.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="413.5" y="141.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <line x1="330" y1="324" x2="295" y2="324" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M282,324 L296,317.5 L296,330.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="296" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="308.5" y="241.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I = I_1 + I_2$</div></foreignObject>
  <foreignObject x="65" y="369.5" width="470" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{same voltage } U \text{ across both resistors}$</div></foreignObject>
</svg>

A new parallel branch does not change the currents of the other branches, because their voltage stays the same. It adds routes to the circuit, so the current leaving the battery increases. The lamps and sockets in homes are connected in parallel: each appliance gets the same mains voltage, and switching one appliance off breaks only its own branch.

<figure class="unit-photo"><img src="pics/fy6/christmas-lights.webp" alt="A detached house in the evening. Hundreds of small lights glow on the eaves, in a tree and in the yard."><figcaption>Christmas lights in the yard of a house. A long string has dozens of lamps, and the way they are connected decides what happens when one of them breaks.</figcaption></figure>

### Total resistance
A connection of resistors can be replaced with a single resistor from which the battery gives the same current. The resistance of this resistor is the total resistance $R$ of the connection: $U = RI$ holds for it, where $I$ is the current leaving the battery. In a series connection the charges pass through every resistor, so the total resistance is greater than any of the resistors. In a parallel connection each branch is a new route, so the total resistance is smaller than the smallest of the branch resistances.

```pysahdy
Resistors of $10\,\Omega$ and $1000\,\Omega$ are connected in parallel. Is the total resistance greater or smaller than $10\,\Omega$?
---
Smaller, because every branch is a new path. The total resistance of a parallel connection is always smaller than the smallest branch resistance.
```

## Formula: Total resistance of resistors
In a series connection the voltages add up, $U = U_1 + U_2$, and the same current $I$ passes through every resistor. When the voltages are written using Ohm's law, we get $RI = R_1 I + R_2 I$, and the current $I$ cancels. So the total resistance of resistors connected in series is
```kaavat
total resistance of resistors in series :: R = R_1 + R_2 + R_3 + \dots
```
where $R$ is the total resistance ($\Omega$) and $R_1$, $R_2$, $R_3$, … are the resistances of the resistors ($\Omega$).

In a parallel connection the currents add up, $I = I_1 + I_2$, and the same voltage $U$ is across every resistor. When the currents are written using Ohm's law, we get $\tfrac{U}{R} = \tfrac{U}{R_1} + \tfrac{U}{R_2}$, and the voltage $U$ cancels. For the total resistance of resistors connected in parallel
```kaavat
total resistance of resistors in parallel :: \frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots
```
where $R$ is the total resistance and $R_1$, $R_2$, $R_3$, … are the resistances of the branches. The equation first gives the number $\tfrac{1}{R}$, whose unit is $\tfrac{1}{\Omega}$. The total resistance is its reciprocal, so remember to invert at the end of the calculation. For two parallel resistors the equation can be solved in advance:
```latex
R = \frac{R_1 R_2}{R_1 + R_2}
```
When two equal resistors are connected in parallel, the total resistance is half the resistance of one resistor.

In the graph the resistor $R_1 = 100\,\Omega$ stays the same and $R_2$ changes. The total resistance of the series connection grows by as much as $R_2$ and is always over $100\,\Omega$. The total resistance of the parallel connection always stays smaller than either resistor; when $R_2 = 100\,\Omega$, it is $50\,\Omega$.

<svg data-fig="graph" viewBox="0 0 600 352" role="img" aria-label="Graph to scale: the total resistance R in ohms as a function of the resistor R2, when the other resistor R1 is 100 ohms. The line of the series connection rises from 100 ohms to 300 ohms as R2 grows from zero to 200 ohms. The curve of the parallel connection rises from zero to about 67 ohms and always stays below the dashed line at 100 ohms; at R2 = 100 ohms it is 50 ohms." style="max-width:100%;font-size:24px">
  <line x1="192" y1="300" x2="192" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="288" y1="300" x2="288" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="300" x2="384" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="300" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="260.5" x2="480" y2="260.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="221.5" x2="480" y2="221.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="182" x2="480" y2="182" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="142.5" x2="480" y2="142.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103.5" x2="480" y2="103.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="494" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,300 L493,306 L493,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="192" y1="300" x2="192" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="175.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="288" y1="300" x2="288" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="265.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="384" y1="300" x2="384" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="361.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="480" y1="300" x2="480" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="457.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="260.5" x2="96" y2="260.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="246" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="221.5" x2="96" y2="221.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="207" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="182" x2="96" y2="182" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="142.5" x2="96" y2="142.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="128" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="103.5" x2="96" y2="103.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="89" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$300$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_2\ (\Omega)$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R\ (\Omega)$</div></foreignObject>
  <line x1="96" y1="221.5" x2="480" y2="221.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="96,221.5 480,64" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,300 99,298.5 102.5,297.5 105.5,296.5 109,295 112,294 115,293 118.5,292 121.5,290.5 125,289.5 128,289 131,288 134.5,287 137.5,286 141,285 144,284.5 147,283.5 150.5,282.5 153.5,282 157,281 160,280.5 163,279.5 166.5,279 169.5,278 173,277.5 176,277 179,276 182.5,275.5 185.5,275 189,274.5 192,274 195,273 198.5,272.5 201.5,272 205,271.5 208,271 211,270.5 214.5,270 217.5,269.5 221,269 224,268.5 227,268 230.5,267.5 233.5,267 237,266.5 240,266.5 243,266 246.5,265.5 249.5,265 253,264.5 256,264 259,264 262.5,263.5 265.5,263 269,262.5 272,262.5 275,262 278.5,261.5 281.5,261.5 285,261 288,260.5 291,260.5 294.5,260 297.5,259.5 301,259.5 304,259 307,259 310.5,258.5 313.5,258 317,258 320,257.5 323,257.5 326.5,257 329.5,257 333,256.5 336,256.5 339,256 342.5,256 345.5,255.5 349,255.5 352,255 355,255 358.5,254.5 361.5,254.5 365,254 368,254 371,253.5 374.5,253.5 377.5,253 381,253 384,253 387,252.5 390.5,252.5 393.5,252 397,252 400,252 403,251.5 406.5,251.5 409.5,251 413,251 416,251 419,250.5 422.5,250.5 425.5,250.5 429,250 432,250 435,250 438.5,249.5 441.5,249.5 445,249.5 448,249 451,249 454.5,249 457.5,248.5 461,248.5 464,248.5 467,248 470.5,248 473.5,248 477,247.5 480,247.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="288" cy="142.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="288" cy="260.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="320" y="56" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2f74b5">$\text{series}$</div></foreignObject>
  <foreignObject x="490" y="233" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\text{parallel}$</div></foreignObject>
  <foreignObject x="406" y="207" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$R_1$</span></div></foreignObject>
</svg>

```pysahdy
Resistors of $12\,\Omega$ and $4.0\,\Omega$ are connected in parallel. What is the total resistance?
---
By $R = \tfrac{R_1 R_2}{R_1 + R_2}$, $R = \tfrac{12\,\Omega \cdot 4.0\,\Omega}{16\,\Omega}$, so $R = 3.0\,\Omega$. This is smaller than $4.0\,\Omega$, as it should be.
```

### Mixed connection
Many circuits have both resistors in series and resistors in parallel. The solution goes step by step, from the inside out:

1. Replace the parallel resistors $R_2$ and $R_3$ with a single resistor $R_{23}$ using the formula for a parallel connection.
2. The resistor $R_1$ is in series with it, so the total resistance is $R = R_1 + R_{23}$.
3. The current leaving the battery is $I = U : R$. It passes through both $R_1$ and the parallel part.
4. The voltages of the series parts are obtained from Ohm's law: $U_1 = R_1 I$ and $U_{23} = R_{23} I$. They add up to the battery voltage.
5. The voltage $U_{23}$ is the same across both parallel resistors, so the branch currents are $I_2 = U_{23} : R_2$ and $I_3 = U_{23} : R_3$. They add up to the current $I$.

<svg data-fig="mixed" viewBox="0 0 600 340" role="img" aria-label="Two circuit diagrams side by side, not to scale. On the left a resistor R1 is connected to a battery, and in series with it a group of two parallel resistors R2 and R3. On the right the same circuit, in which the parallel resistors are replaced with a single resistor R23 in series with R1." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-4-mixed.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="16" y="148.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="16" y="192.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="114" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="96.5" y="35.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <foreignObject x="199.5" y="35.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="199.5" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_3$</div></foreignObject>
  <foreignObject x="312" y="148.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="312" y="192.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="402" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="392.5" y="35.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <foreignObject x="497" y="170.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_{23}$</div></foreignObject>
  <foreignObject x="40" y="303.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2 \text{ and } R_3 \text{ in parallel}$</div></foreignObject>
  <foreignObject x="340" y="303.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R = R_1 + R_{23}$</div></foreignObject>
</svg>

## Worked example
Two resistors, $R_1 = 120\,\Omega$ and $R_2 = 60\,\Omega$, are connected in parallel to a $9.0\,\text{V}$ battery. How large a current leaves the battery? The battery is considered ideal, and the resistance of the wires is ignored.

<!-- vaihe -->

**Given and find.** $R_1 = 120\,\Omega$, $R_2 = 60\,\Omega$ and $U = 9.0\,\text{V}$. We want the current $I$ leaving the battery.

<!-- vaihe -->

**Principle.** The resistors are in parallel, so the battery voltage is across both. The connection can be replaced with the total resistance $R$, and Ohm's law then gives the current leaving the battery, $I = U : R$.

<!-- vaihe -->

**Formula solved.** We solve $R$ from the equation of the parallel connection, and with it the current $I$:
```latex
\begin{aligned}
&\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} \\[4pt]
&R = \frac{R_1 R_2}{R_1 + R_2} \\[4pt]
&I = \frac{U}{R}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the resistances are in ohms and the voltage in volts, and $\tfrac{\text{V}}{\Omega} = \text{A}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
R &= \frac{120\,\Omega \cdot 60\,\Omega}{120\,\Omega + 60\,\Omega} \\
&= 40\,\Omega \\[6pt]
I &= \frac{9.0\,\text{V}}{40\,\Omega} \\
&= 0.225\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Result.** The current leaving the battery is $0.23\,\text{A}$, or about $230\,\text{mA}$. The result is given to two significant figures like the voltage $9.0\,\text{V}$.

<!-- vaihe -->

**Reasonableness.** The branch currents give the same result: $9.0\,\text{V} : 120\,\Omega = 0.075\,\text{A}$ and $9.0\,\text{V} : 60\,\Omega = 0.15\,\text{A}$, together $0.225\,\text{A}$. The total resistance $40\,\Omega$ is smaller than the smaller of the resistors, $60\,\Omega$, as it should be in a parallel connection.

## Common misconception
Many people think that current is used up in a resistor, so that the first resistor in a series connection would get the most current and the later ones less. But when $10\,\Omega$ and $20\,\Omega$ resistors are connected in series to a $6.0\,\text{V}$ battery, the same current of $0.20\,\text{A}$ passes through both. No charge is lost in a resistor; instead, the electrical energy of the charges is transformed into internal energy, and in a lamp also into light.

Another common mistake is to think that every added resistor increases the total resistance. This is true only in a series connection. A resistor added in parallel opens a new route, so the total resistance decreases and the current leaving the battery increases.

## Summary
- In a series connection the same current passes through every resistor, the voltages add up, $U = U_1 + U_2$, and the total resistance is $R = R_1 + R_2 + \dots$
- In a parallel connection the same voltage is across every branch, the currents add up, $I = I_1 + I_2$, and $\tfrac{1}{R} = \tfrac{1}{R_1} + \tfrac{1}{R_2} + \dots$. The total resistance is smaller than the smallest of the branch resistances.
- When a component connected in series breaks, the current stops in the whole circuit; when a parallel branch breaks, it stops only in that branch.
- The total resistance of a mixed connection is calculated step by step: first the parallel parts, then those connected in series.
