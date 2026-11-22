# Kirchhoff's laws and potential in a circuit

> **Why** can a bird sit on a bare high-voltage wire unharmed, even though a current of hundreds of amperes flows in the wire?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a high-voltage line above a field landscape on a summer day. Wires hang between two lattice pylons, and four small birds sit in a row on one wire. In the background are the edge of a forest and a rolling field." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Current is not used up: Kirchhoff's current law
Electric current is the motion of charges. Charge is neither created nor destroyed, and it does not collect in the wires when the currents stay constant. Therefore all the charge that arrives at a **junction**, a point where a wire divides into branches, also leaves it. **The sum of the currents arriving at a junction is equal to the sum of the currents leaving it.** This is Kirchhoff's current law. For the same reason the current is equal on both sides of a resistor: in a resistor electrical energy changes into internal energy of the resistor, which is transferred to the surroundings as heat, but the current is not used up in it.

The voltage across parallel branches is the same (chapter *Resistors in series and in parallel*), so by Ohm's law the branch with the smaller resistance carries the larger current. In the figure the current in the $30\,\Omega$ branch is twice the current in the $60\,\Omega$ branch, and the branch currents $0.20\,\text{A}$ and $0.10\,\text{A}$ are together equal to the arriving current $0.30\,\text{A}$.

<svg data-fig="junction" viewBox="0 0 600 330" role="img" aria-label="Schematic of a junction, not to scale. From the left a current I1 = 0.30 A arrives along a wire at the junction. Two branches leave it: the upper branch has a 30 ohm resistor and the lower branch a 60 ohm resistor, and the branches join again on the right. The width of the purple current arrows is proportional to the current: in the upper branch I2 = 0.20 A, in the lower branch I3 = 0.10 A, and together the branches carry away as much current as arrives at the junction, 0.30 A." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-5-junction.webp" x="0" y="-1.2" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="351" y="91.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="351" y="219.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <foreignObject x="15" y="93.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1 = 0.30\,\text{A}$</div></foreignObject>
  <foreignObject x="334" y="27.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2 = 0.20\,\text{A}$</div></foreignObject>
  <foreignObject x="334" y="283.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_3 = 0.10\,\text{A}$</div></foreignObject>
  <foreignObject x="216" y="155.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{junction}$</div></foreignObject>
</svg>

```pysahdy
A current of $0.80\,\text{A}$ arrives at a junction and divides into two branches. Can the current be $0.50\,\text{A}$ in both branches? Why or why not?
---
No. By the current law the currents leaving are together $0.80\,\text{A}$, but $0.50\,\text{A} + 0.50\,\text{A} = 1.00\,\text{A}$.
```

### Potential: the electrical level of every point
Every point of a circuit has a **potential** $V$: the voltage of the point relative to a chosen zero point. The zero point is often chosen to be the negative terminal of the voltage source or the earth, and its potential is $0\,\text{V}$. The voltage between two points is the difference of their potentials. Potential can be compared with height: height depends on where it is measured from, but the difference in height between two points does not. In the same way, moving the zero point changes all potentials by the same amount, but the voltages stay the same.

Potential changes only in the source and in the resistors. In the source it rises from the negative terminal to the positive terminal by the voltage of the source; in this chapter the source is ideal, that is, the effect of its own resistance is neglected. In a resistor it drops in the direction of the current by the voltage $U = RI$. The resistance of a wire is so small that its voltage is neglected, so all points of the same wire have the same potential. In the circuit of the figure the points $B$ and $C$ are the same wire, so the potential of both is $6.0\,\text{V}$.

<svg data-fig="circuit" viewBox="0 0 600 368" role="img" aria-label="Circuit diagram, not to scale: a voltage source of 9.0 V, from its positive terminal a resistor R1 = 10 ohms and after it two parallel resistors R2 = 30 ohms and R3 = 60 ohms, which return to the negative terminal of the source. The points A–F are marked on the wires with their potentials when the negative terminal of the source is the zero point: A 9.0 V, B and C 6.0 V, and D, E and F 0 V. At all points of the same wire the potential is the same; it changes only in the source and the resistors." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-5-circuit.webp" x="0" y="0" width="600" height="377.5" preserveAspectRatio="none"/>
  <foreignObject x="26" y="152.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="26" y="192.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="111" y="170.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 9.0\,\text{V}$</div></foreignObject>
  <foreignObject x="126" y="111.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1 = 10\,\Omega$</div></foreignObject>
  <foreignObject x="352" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="352" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="492" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_3$</div></foreignObject>
  <foreignObject x="492" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <foreignObject x="98" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="72" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$9.0\,\text{V}$</div></foreignObject>
  <foreignObject x="272" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <foreignObject x="246" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6.0\,\text{V}$</div></foreignObject>
  <foreignObject x="456" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="430" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6.0\,\text{V}$</div></foreignObject>
  <foreignObject x="456" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D$</div></foreignObject>
  <foreignObject x="430" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="316" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="290" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="98" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="72" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
</svg>

```pysahdy
Two points are at the ends of the same bare conductor with no resistor between them. How large is the voltage between them, and why?
---
It is approximately zero. The resistance of the conductor is negligibly small, so the potential does not change along it.
```

### A round trip in a loop: Kirchhoff's voltage law
A **loop** is a closed path in a circuit that returns to its starting point. When a loop is traversed, the potential returns to the same value from which it started. Therefore **the sum of the rises and drops of potential in a loop is zero**. This is Kirchhoff's voltage law. In a circuit of one loop the voltage of the source is equal to the sum of the voltages of the resistors. In terms of energy, voltage tells how much energy per unit of charge changes from one form to another (chapter *Circuit, electric current and voltage*): a charge gains energy in the source and gives up the same amount in the resistors.

The circuit of the figure has two loops, one through the resistor $R_2$ and the other through the resistor $R_3$. In each of them the $9.0\,\text{V}$ of the source divides into the voltage $3.0\,\text{V}$ of the resistor $R_1$ and the voltage $6.0\,\text{V}$ of the branch. This is why the voltage across parallel branches is the same.

### A bird on a wire
The bird's feet are at two points of the same wire, only a few centimetres apart. The bird is a branch parallel to the piece of wire between its feet, whose resistance is negligible. Therefore the voltage between the feet is only millivolts, and by Ohm's law a negligible current flows through the bird. By the current law almost all the current thus continues along the wire. The potential of the bird relative to the ground is high, but danger would arise only if it touched another wire or a pylon at the same time, since their potential is different. For a person the situation is not comparable: a high-voltage line must not be approached, because an electric arc can form even without contact.

<figure class="unit-photo"><img src="pics/fy6/swallows-power-line.webp" alt="Two barn swallows sit on an overhead line against a blue sky."><figcaption>Barn swallows on an overhead line. The line in the photo is an insulated cable, but birds sit on bare lines in the same way: both feet are at two nearby points of the same conductor.</figcaption></figure>

## Formula: Kirchhoff's laws
Kirchhoff's current law for a junction:
```kaavat
Kirchhoff's first law :: \sum I_\text{in} = \sum I_\text{out}
```
where $I_\text{in}$ are the currents arriving at the junction (A) and $I_\text{out}$ the currents leaving it (A). For a current dividing into two branches $I_1 = I_2 + I_3$.

The voltage between the points $A$ and $B$ is the difference of the potentials:
```kaavat
voltage between two points :: U_{AB} = V_A - V_B
```
where $U_{AB}$ is the voltage (V) and $V_A$ and $V_B$ are the potentials of the points (V) relative to the same zero point. The voltage is positive when $A$ is at the higher potential.

Kirchhoff's voltage law for a loop:
```kaavat
Kirchhoff's second law :: \sum \Delta V = 0
```
where $\Delta V$ (V) is the change of potential in each part of the loop when the loop is traversed once. In the source from the negative terminal to the positive terminal $\Delta V = +U$, in a resistor in the direction of the current $\Delta V = -RI$, and in a wire $\Delta V = 0$. In a circuit of one loop with two resistors the law gives $U - R_1 I - R_2 I = 0$, that is, $U = R_1 I + R_2 I$.

```pysahdy
In a one-loop circuit the resistors are $R_1 = 20\,\Omega$ and $R_2 = 10\,\Omega$. How many times larger is the voltage of $R_1$ than the voltage of $R_2$, and why?
---
Twice as large. The same current $I$ passes through both, so by $U = RI$ the voltage is proportional to the resistance. The voltages together make the source voltage, $U = R_1 I + R_2 I$.
```

A **potential graph** shows the potential at different points of a loop. In the graph the loop of the circuit marked with the points $A$–$F$ is traversed from the negative terminal $F$ through the resistors $R_1$ and $R_2$ back to the point $F$. The rise of the source $+9.0\,\text{V}$ is equal to the total of the drops of the resistors $-3.0\,\text{V}$ and $-6.0\,\text{V}$, and in the wires the graph is horizontal.

<svg data-fig="potential-graph" viewBox="0 0 600 360" role="img" aria-label="Potential graph, vertical axis to scale, horizontal axis schematic: potential V in volts as the loop of the circuit in the figure is traversed from the negative terminal F of the source through the source and the resistors R1 and R2 back to F. In the source the potential rises from 0 volts to 9.0 volts. Along the wire to the point A it stays at 9.0 volts, in the resistor R1 it drops by 3.0 V to 6.0 volts at the point B, and in the resistor R2 from 6.0 V to zero at the point E. From the point E to the point F the potential stays at zero. The sum of the rises and drops is zero." style="max-width:100%;font-size:24px">
  <line x1="96" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="230" x2="96" y2="230" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="215.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="110" x2="96" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="95.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$9$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{point}$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{V})$</div></foreignObject>
  <rect x="127.5" y="70" width="27" height="220" fill="#eef5f9"/>
  <foreignObject x="119" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <rect x="230.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="231" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <rect x="365.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="366" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <line x1="97" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="64" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,290 141,290 141,110 186,110 230.5,110 275.5,170 320.5,170 365.5,170 410,290 455,290 500,290" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="96" y1="290" x2="96" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="82" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <line x1="186" y1="290" x2="186" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="320.5" y1="290" x2="320.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="306.5" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <line x1="455" y1="290" x2="455" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <line x1="500" y1="290" x2="500" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="486" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <circle cx="96" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186" cy="110" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="170" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="455" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="149" y="185.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+9.0\,\text{V}$</div></foreignObject>
  <foreignObject x="283.5" y="125.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-3.0\,\text{V}$</div></foreignObject>
  <foreignObject x="418" y="215.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-6.0\,\text{V}$</div></foreignObject>
</svg>

## Worked example
The voltage of a voltage source is $12\,\text{V}$. From the positive terminal of the source the current flows through a resistor $R_1 = 20\,\Omega$ to a junction $B$, from which two parallel branches leave: a resistor $R_2 = 60\,\Omega$ and a resistor $R_3 = 30\,\Omega$. The branches return to the negative terminal of the source, which is the zero point. What is the potential of the point $B$, and how large is the current through the resistor $R_3$?

<!-- vaihe -->

**Given and find.** $U = 12\,\text{V}$, $R_1 = 20\,\Omega$, $R_2 = 60\,\Omega$, $R_3 = 30\,\Omega$ and the potential of the negative terminal $0\,\text{V}$. We are asked for the potential $V_B$ of the point $B$ and the current $I_3$.

<!-- vaihe -->

**Principle.** The whole current $I_1$ flows through the source and the resistor $R_1$. The parallel resistors are replaced with a single resistor $R_{23}$, and then Ohm's law gives $I_1$. By the voltage law the potential drops from the value $U$ of the positive terminal in the resistor $R_1$ by the voltage $R_1 I_1$. The resistor $R_3$ is between the point $B$ and the zero point, so its voltage is $V_B$.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{R_2} + \frac{1}{R_3} \\
&I_1 = \frac{U}{R_1 + R_{23}} \\
&V_B = U - R_1 I_1 \\
&I_3 = \frac{V_B}{R_3}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: all quantities are in base units, and $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{60\,\Omega} + \frac{1}{30\,\Omega} \\
&R_{23} = 20\,\Omega \\
&I_1 = \frac{12\,\text{V}}{20\,\Omega + 20\,\Omega} = 0.30\,\text{A} \\
&V_B = 12\,\text{V} - 20\,\Omega \cdot 0.30\,\text{A} \\
&\phantom{V_B} = 6.0\,\text{V} \\
&I_3 = \frac{6.0\,\text{V}}{30\,\Omega} = 0.20\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Result.** The potential of the point $B$ is $6.0\,\text{V}$, and a current of $0.20\,\text{A}$ flows through the resistor $R_3$. The results are given to two significant figures like the resistances.

<!-- vaihe -->

**Reasonableness.** A current of $6.0\,\text{V} : 60\,\Omega = 0.10\,\text{A}$ flows through the resistor $R_2$, and the branch currents are together $0.30\,\text{A}$, as the current law requires. In the loop $12\,\text{V} - 6.0\,\text{V} - 6.0\,\text{V} = 0$, as the voltage law requires. The branch with the smaller resistance carries the larger current, as it should.

## Common misconception
Many think that a resistor uses up current, so that the current after the resistor would be smaller than before it. A resistor changes electrical energy into its internal energy, but no charges disappear: an ammeter shows the same reading on both sides of a resistor. In a resistor the potential decreases, not the current.

Another common mistake is to use the whole voltage of the source when calculating the current of a branch. If the current of the $30\,\Omega$ branch were wrongly calculated from the voltage $9.0\,\text{V}$, the result would be $0.30\,\text{A}$. The actual voltage of the branch is, however, $6.0\,\text{V}$, so $I_2 = 0.20\,\text{A}$. In the other branch $I_3 = 6.0\,\text{V} : 60\,\Omega = 0.10\,\text{A}$. Kirchhoff's current law holds: $0.20\,\text{A} + 0.10\,\text{A} = 0.30\,\text{A}$. A third mistake is to think that voltage is a property of a single point: voltage is always the potential difference between two points.

## Summary
- Kirchhoff's current law: the sum of the currents arriving at a junction is equal to the sum of the currents leaving it, because charge is conserved. Current is not used up in a resistor.
- Potential $V$ is the voltage of a point relative to the zero point. Voltage is a potential difference $U_{AB} = V_A - V_B$, and it does not depend on the choice of the zero point.
- Potential rises in the source from the negative terminal to the positive terminal, drops in a resistor in the direction of the current by $RI$, and stays the same in a wire.
- Kirchhoff's voltage law: the sum of the changes of potential in a loop is zero, $\sum \Delta V = 0$. Therefore the voltage of the source is shared among the resistors of the loop, and the voltage across parallel branches is the same.
