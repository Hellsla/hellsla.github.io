# Measurements in an electric circuit

> **Why** is an ammeter connected to a circuit in a different way from a voltmeter, and what happens if the connections get mixed up?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a work bench in a school laboratory. On the bench there is a breadboard where a battery holder and a lamp holder are connected with wires in the same circuit, and the lamp is lit. Next to it is a grey digital multimeter whose red and black test leads touch the two terminals of the lamp holder." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### An ammeter is connected in series
An **ammeter** measures how large an electric current passes through it. That is why the current to be measured has to pass through the meter: the circuit is opened at the point whose current we want to know, and the meter is placed in the gap. The meter is then **in series** with the other components. In a circuit without branches the current is the same at every point, because charge neither disappears nor accumulates anywhere. A lamp changes electrical energy into light and internal energy of the filament, but it does not use up current. An ammeter can therefore be connected at any point of a circuit without branches, and it always shows the same reading.

### A voltmeter is connected in parallel
Voltage is a quantity between two points (chapter *Circuit, electric current and voltage*). A **voltmeter** measures the voltage between the two points that its leads are touched to. The voltage of a lamp is measured by touching both terminals of the lamp: the circuit is not opened, but the meter comes **in parallel** with the lamp. The red lead of the meter is touched to the terminal that is closer to the positive terminal of the battery, so the reading is positive.

<svg data-fig="connections" viewBox="0 0 600 344" role="img" aria-label="Two circuit diagrams. On the left the battery, the lamp and the ammeter A are in the same loop one after another: the ammeter is in series with the lamp, and the same current I passes through the battery, the meter and the lamp. On the right the battery and the lamp form a loop, and the voltmeter V is connected between the terminals of the lamp, in parallel with the lamp. The purple arrows show the direction of the current from the positive terminal of the battery to the negative terminal." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-connections.webp" x="0" y="0" width="600" height="355" preserveAspectRatio="none"/>
  <foreignObject x="98" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="64" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="102.5" y="275.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ammeter}$</div></foreignObject>
  <foreignObject x="96" y="305.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in series}$</div></foreignObject>
  <foreignObject x="436" y="34.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="356" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="390" y="275.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{voltmeter}$</div></foreignObject>
  <foreignObject x="383.5" y="305.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in parallel}$</div></foreignObject>
</svg>

```pysahdy
The red lead of a digital voltmeter touches the terminal of a lamp that is farther from the plus terminal of the battery. What is the reading?
---
The reading is negative, because the red lead is not on the terminal nearer the plus terminal.
```

### The multimeter
In a laboratory, current and voltage are usually measured with a **multimeter**: the same device measures, depending on the position of the selector, voltage, current and often other quantities too. In the example meter of the figure, the black lead is connected to the COM jack. The red lead is connected to the jack $\text{V}\ \text{mA}$ when measuring voltage and small currents and in the jack $10\,\text{A}$ when measuring large currents. The jacks and maximum currents of different multimeters can differ, so always check the markings and the manual of the meter you use. The selector chooses both the quantity and the **measuring range**, which is the largest value that the meter shows in this position. On the range $20\,\text{V}$ the display shows at most $19.99\,\text{V}$; at a larger voltage the display shows OL (*overload*), which means that the value is over the measuring range.

<svg data-fig="multimeter" viewBox="0 0 600 360" role="img" aria-label="Drawing of a digital multimeter. At the top the display with the reading 1.500 V. In the middle the selector, around which are the measuring ranges 2 V, 20 V, 200 mA and 10 A; the pointer is on the range 2 V. At the bottom three jacks: COM, V mA and 10 A. The place of the black lead is COM and that of the red lead V mA or 10 A. On the right the labels display, selector and jacks." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-multimeter.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="72" y="50" width="150" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:40px">$1.500$</div></foreignObject>
  <foreignObject x="228" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="86.5" y="179" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffc078">$2\,\text{V}$</div></foreignObject>
  <foreignObject x="109.5" y="132.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$20\,\text{V}$</div></foreignObject>
  <foreignObject x="180" y="132.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$200\,\text{mA}$</div></foreignObject>
  <foreignObject x="222" y="179" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <foreignObject x="87.5" y="307.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{COM}$</div></foreignObject>
  <foreignObject x="155.5" y="307.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{V}\ \text{mA}$</div></foreignObject>
  <foreignObject x="221" y="307.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <foreignObject x="358" y="58.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{display}$</div></foreignObject>
  <foreignObject x="358" y="191.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{selector}$</div></foreignObject>
  <foreignObject x="358" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{jacks}$</div></foreignObject>
</svg>

### Choosing the measuring range
On a smaller range the display shows more decimals. On the range $20\,\text{V}$ the voltage of a lamp appears as $1.50\,\text{V}$, on the range $2\,\text{V}$ as $1.500\,\text{V}$: the last digit tells the **resolution**, that is the smallest step that the display can take. That is why we measure on the smallest range on which the reading still fits. When the order of magnitude is not known, we start from the largest range and move to a smaller one. When measuring current, this is also a safety matter, because too large a current blows the fuse of the meter.

### The meter affects the circuit
Every component has a **resistance**, which describes how strongly it opposes an electric current; the quantity is made more precise in the chapter *Resistance and Ohm's law*. The resistance of an ammeter connected in series is very small, so that the meter hardly decreases the current that it measures. The resistance of a voltmeter connected in parallel is very large, for example $10\,\text{M}\Omega$, so that hardly any current passes through the meter past the component. An ideal meter would not change the circuit at all; a real one changes it a little, which is one source of measurement uncertainty.

A wrongly connected meter changes the circuit a lot. If an ammeter is connected in parallel with a lamp, the current passes almost entirely through the meter of small resistance past the lamp: the lamp goes out, and the current can grow so large that the fuse of the meter blows. When the fuse has blown, the meter is out of the circuit and the lamp lights up again. A current path that bypasses a component like this is called a short circuit. An ammeter must not be connected across the terminals of a voltage source. In the school laboratory, measurements are made with safe low-voltage sources as instructed by the teacher. If, on the other hand, a voltmeter is connected in series, its large resistance decreases the current of the whole circuit to almost zero: the lamp goes out, and the meter shows approximately the voltage of the battery.

<svg data-fig="wrong" viewBox="0 0 600 352" role="img" aria-label="Two wrong connections. On the left the ammeter A is connected in parallel with the lamp. The current passes almost entirely through the ammeter of small resistance, which is shown by the thick purple arrow: the lamp is not lit, and the current is large. On the right the voltmeter V is in series with the lamp. The large resistance of the meter decreases the current to almost zero, so the lamp is not lit and there are no current arrows." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-wrong.webp" x="0" y="0" width="600" height="361.2" preserveAspectRatio="none"/>
  <foreignObject x="145" y="42.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="66" y="143.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\text{large } I$</div></foreignObject>
  <foreignObject x="102.5" y="283.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ammeter}$</div></foreignObject>
  <foreignObject x="83.5" y="313.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in parallel}$</div></foreignObject>
  <foreignObject x="387" y="102.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="427.5" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \approx 0$</div></foreignObject>
  <foreignObject x="390" y="283.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{voltmeter}$</div></foreignObject>
  <foreignObject x="396" y="313.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in series}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/multimeter-breadboard.webp" alt="A red and a black probe touch a breadboard holding a resistor and a red LED."><figcaption>Multimeter probes on a breadboard. When the probes are placed at two points of a circuit, the meter is connected in parallel with the part between them and measures its voltage.</figcaption></figure>

```pysahdy
An ammeter is connected across a lamp by mistake. What happens to the lamp, and why?
---
The lamp goes out, because almost all the current goes through the low-resistance meter and bypasses the lamp. This is a short circuit.
```

## Formula: Error limit of a multimeter

### The error limit given by the manufacturer
The reading of a meter is not exactly the true value of the quantity being measured. The manufacturer of a digital meter gives in the manual for every range an **error limit** in the form $\pm(p + n\ \text{digits})$: the error limit is a percentage $p$ of the reading plus $n$ steps of the last digit. The error limit given by the manufacturer tells how much the reading of a meter that is in order and used according to the instructions can at most differ from the true value. However, the total uncertainty of a measurement can also be affected by the measuring method, the effect of the meter on the circuit and other sources of error.

| Range | Resolution | Error limit |
|---|---|---|
| voltage $2\,\text{V}$ | $0.001\,\text{V}$ | $\pm(0.5\,\% + 2\ \text{digits})$ |
| voltage $20\,\text{V}$ | $0.01\,\text{V}$ | $\pm(0.5\,\% + 2\ \text{digits})$ |
| current $200\,\text{mA}$ | $0.1\,\text{mA}$ | $\pm(1.0\,\% + 2\ \text{digits})$ |
| current $10\,\text{A}$ | $0.01\,\text{A}$ | $\pm(2.0\,\% + 3\ \text{digits})$ |

### Calculating the error limit
The error limit of a reading $x$ is
```latex
\Delta x = p \cdot x + n \cdot r
```
where $\Delta x$ is the error limit, $x$ the reading, $p$ the percentage given by the manufacturer as a decimal number ($0.5\,\% = 0.005$), $n$ the number of digits and $r$ the resolution of the range. The result is written in the form $x \pm \Delta x$, for example $U = 4.50\,\text{V} \pm 0.04\,\text{V}$. The notation is the same as for an error estimate, but here $\Delta x$ is the meter's own error limit, not the uncertainty of the whole measurement. The accuracy of different measurements is compared with the **relative error limit**
```latex
\frac{\Delta x}{x}
```
which is a pure number and is usually given as a percentage.

```pysahdy
On the $2\,\text{V}$ range the reading is $0.100\,\text{V}$. The resolution is $0.001\,\text{V}$ and the error limit is $\pm(0.5\,\% + 2\ \text{digits})$. Which part of the error limit is larger, the percentage part or the digit part?
---
The percentage part is $0.005 \cdot 0.100\,\text{V} = 0.0005\,\text{V}$. The digit part is $2 \cdot 0.001\,\text{V} = 0.002\,\text{V}$, so the digit part is larger.
```

### Why the smallest suitable range
If the ranges have the same $p$ and the same $n$, as this meter's voltage ranges do, the percentage part $p \cdot x$ is the same on all of them, but the share of the digits $n \cdot r$ decreases to a tenth when we move to a range ten times smaller. When the reading is small compared with the range, the share of the digits dominates: a current of $0.02\,\text{A}$ on the range $10\,\text{A}$ is almost a guess, because three steps of the last digit are already $0.03\,\text{A}$.

<svg data-fig="error-bands" viewBox="0 0 600 312" role="img" aria-label="Picture to scale: the voltage axis from 1.46 V to 1.54 V. The upper segment shows the reading 1.50 V obtained on the range 20 V and its error limit ±0.03 V, that is the interval 1.47 V–1.53 V. The lower segment shows the reading 1.500 V obtained on the range 2 V and its error limit ±0.010 V, that is the interval 1.490 V–1.510 V. The segment of the lower range is about a third of the length of the upper one." style="max-width:100%;font-size:24px">
  <line x1="120" y1="40" x2="120" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="40" x2="180" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="40" x2="240" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="40" x2="300" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="40" x2="360" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="40" x2="420" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="40" x2="480" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="252" x2="554" y2="252" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,252 L553,258 L553,246 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="252" x2="60" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="31" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.46$</div></foreignObject>
  <line x1="120" y1="252" x2="120" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="252" x2="180" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="151" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.48$</div></foreignObject>
  <line x1="240" y1="252" x2="240" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="252" x2="300" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="271" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.50$</div></foreignObject>
  <line x1="360" y1="252" x2="360" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="252" x2="420" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="391" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.52$</div></foreignObject>
  <line x1="480" y1="252" x2="480" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="252" x2="540" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="511" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.54$</div></foreignObject>
  <foreignObject x="488" y="211.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="60" y="27.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{range } 20\,\text{V}$</div></foreignObject>
  <rect x="120" y="66" width="360" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="120" y1="58" x2="120" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="480" y1="58" x2="480" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="78" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="492" y="63.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0.03\,\text{V}$</div></foreignObject>
  <foreignObject x="60" y="125.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{range } 2\,\text{V}$</div></foreignObject>
  <rect x="240" y="164" width="120" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="240" y1="156" x2="240" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="360" y1="156" x2="360" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="176" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="372" y="161.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0.010\,\text{V}$</div></foreignObject>
</svg>

## Worked example
The voltage of a lamp is measured twice with a multimeter. On the range $20\,\text{V}$ the display shows $1.50\,\text{V}$ and on the range $2\,\text{V}$ the display shows $1.500\,\text{V}$. The error limit of both ranges is $\pm(0.5\,\% + 2\ \text{digits})$. How large is the error limit of the reading on each range, and which range should be chosen?

<!-- vaihe -->

**Given and asked.** The readings $U_{20} = 1.50\,\text{V}$ (resolution $r_{20} = 0.01\,\text{V}$) and $U_2 = 1.500\,\text{V}$ (resolution $r_2 = 0.001\,\text{V}$), $p = 0.5\,\%$ and $n = 2$. We are asked for the error limits $\Delta U_{20}$ and $\Delta U_2$.

<!-- vaihe -->

**Principle.** The manufacturer's error limit is a share of the reading plus two steps of the last digit. The reading is the same on both ranges, so the ranges differ only in their resolution.

<!-- vaihe -->

**Formula solved.** The formula gives the error limit directly when the resolution of each range is substituted:
```latex
\begin{aligned}
&\Delta U_{20} = p \cdot U_{20} + n \cdot r_{20} \\
&\Delta U_2 = p \cdot U_2 + n \cdot r_2
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The percentage is written as a decimal number: $p = 0.5\,\% = 0.005$. No other conversions are needed, because the readings and the resolutions are in volts.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\Delta U_{20} \\
&= 0.005 \cdot 1.50\,\text{V} + 2 \cdot 0.01\,\text{V} \\
&= 0.0275\,\text{V} \\[6pt]
&\Delta U_2 \\
&= 0.005 \cdot 1.500\,\text{V} + 2 \cdot 0.001\,\text{V} \\
&= 0.0095\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Result.** On the range $20\,\text{V}$ the voltage is $1.50\,\text{V} \pm 0.03\,\text{V}$ and on the range $2\,\text{V}$ $1.500\,\text{V} \pm 0.010\,\text{V}$. The relative error limits are $2\,\%$ and $0.67\,\%$. Like an error estimate, an error limit is rounded to one significant figure, or to two if the first figure is 1. The range $2\,\text{V}$ should be chosen: its error limit is about a third.

<!-- vaihe -->

**Reasonableness.** The percentage part is the same on both ranges, $0.0075\,\text{V}$. The difference comes entirely from the share of the digits, which on the range $20\,\text{V}$ is ten times larger, $0.02\,\text{V}$ instead of $0.002\,\text{V}$. A smaller range cannot be less accurate when the reading fits on it and the percentage part of the ranges is the same.

## Common misconception
Many people think that the largest measuring range is always the best, because on it the meter does not go over the range and the fuse does not blow. It is right to start from the largest range when the order of magnitude is not known, but the final reading is taken from the smallest range on which the value fits. On a large range the last digit is coarse, and the error limit of a small value can be as large as the reading itself. Another common mistake is to connect an ammeter in parallel with a component in the same way as a voltmeter. An ammeter is always connected in series.

## Summary
- An ammeter is connected in series: the circuit is opened and the meter is placed in the gap. In a circuit without branches the current is the same at every point.
- A voltmeter is connected in parallel, that is between the two points whose voltage is measured.
- The selector of a multimeter chooses the quantity and the measuring range; OL means that the value is over the range. The black lead belongs in the jack COM.
- We measure on the smallest range on which the reading fits; the measurement of an unknown value is started from the largest range.
- The resistance of an ammeter is very small and that of a voltmeter very large. Wrongly connected, an ammeter makes a short circuit and a voltmeter stops the current.
- The error limit is $\Delta x = p \cdot x + n \cdot r$ and the relative error limit is $\tfrac{\Delta x}{x}$.
