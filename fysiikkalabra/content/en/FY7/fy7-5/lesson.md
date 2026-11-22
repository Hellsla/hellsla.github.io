# Electromagnetic induction

> **Why** does a bicycle dynamo light the lamp only while the wheel is turning, even though the dynamo contains no battery or accumulator?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a cyclist rides along a forest road at dusk. The dynamo is in the hub of the front wheel of the bicycle, and the lamp on the handlebars shines: the beam of light falls on the road in front of the wheel. The sky is evening blue, and spruces stand at the edge of the road." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Faraday's observation
In the chapter *Magnetic field of a wire and a coil*, an electric current produced a magnetic field. Michael Faraday spent years looking for the reverse effect: could a magnetic field produce an electric current? In 1831 he noticed that a magnet at rest beside a coil does nothing, however strong the magnet is. When the magnet is pushed into the coil, the needle of a voltmeter connected to the coil deflects. When the magnet is at rest inside the coil, the needle returns to zero. When the magnet is pulled out, the needle deflects the other way. The faster the magnet is moved and the more turns the coil has, the greater the voltage. The same happens if the magnet is at rest and the coil is moved.

<svg data-fig="faraday" viewBox="0 0 600 340" role="img" aria-label="Schematic picture, not to scale: Faraday&#x27;s experiment in three stages. In each picture a wire coil is connected to a voltmeter. On the left a bar magnet is pushed north pole first towards the coil and into it, and the needle of the meter deflects to the right. In the middle the magnet is at rest inside the coil, and the needle is at zero. On the right the magnet is pulled out of the coil, and the needle deflects to the left." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-faraday.webp" x="0" y="1.2" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="83.5" y="15.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in}$</div></foreignObject>
  <foreignObject x="21" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="63" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="35.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="258.5" y="15.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at rest}$</div></foreignObject>
  <foreignObject x="283" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="325" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="477.5" y="15.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{out}$</div></foreignObject>
  <foreignObject x="421" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="463" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="435.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/shake-flashlight.webp" alt="A transparent plastic torch on a pale background; inside the body a copper-coloured coil can be seen, with the black lamp end on the left."><figcaption>A shake torch. When the torch is shaken, a magnet inside it slides back and forth through the coil. The magnetic flux through the coil changes, so a voltage is induced in the coil, which charges the torch's energy store.</figcaption></figure>

### A change produces a voltage
The phenomenon is called **electromagnetic induction**, and the voltage produced between the ends of the coil is called the **induced voltage**. When the ends of the coil are joined by a wire or a lamp, an induced current flows in the circuit. What all of Faraday's experiments have in common is that the magnetic field passing through the coil **changes**. A coil at rest in a strong but unchanging field gets no voltage. The change can come about in many ways: the magnet or the coil moves, the coil turns in the field, the area of the loop changes, or the current in a nearby electromagnet is switched on or off. In the hub dynamo of a bicycle, a ring magnet turns with the hub around fixed coils, so the magnet turns relative to the coils when the wheel turns. When the wheel stands still, nothing changes and the lamp stays dark.

```pysahdy
A coil sits in a strong but unchanging magnetic field and is turned so that its plane gradually becomes parallel to the field. Is a voltage induced in the coil?
---
Yes. As the coil turns, the magnetic flux through it changes, and the change produces a voltage.
```

### Magnetic flux
The size of the change is measured with the **magnetic flux**. It tells how much magnetic field passes through a loop. When a uniform field is perpendicular to the plane of the loop, the magnetic flux is
```kaavat
magnetic flux :: \Phi = BA
```
where $\Phi$ is the magnetic flux, $B$ the magnetic flux density (T) and $A$ the area of the loop (m²). The unit of flux is the weber: $1\,\text{Wb} = 1\,\text{T}\cdot\text{m}^2$. The flux is greater, the stronger the field and the larger the loop. If the loop is tilted, fewer field lines pass through it and the flux decreases. When the plane of the loop is parallel to the field, no field line passes through it and the flux is zero.

<svg data-fig="flux" viewBox="0 0 600 340" role="img" aria-label="Schematic picture from the side, three parts: horizontal green field lines point from left to right, and a wire loop is seen edge-on as a narrow oval. On the left the plane of the loop is perpendicular to the field, and five field lines pass through the loop: the flux is B times A. In the middle the loop is tilted, and only three lines pass through it: the flux is smaller. On the right the plane of the loop is parallel to the field, and no line passes through it: the flux is zero." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-flux.webp" x="-1.3" y="0" width="603" height="353" preserveAspectRatio="none"/>
  <foreignObject x="71" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi = BA$</div></foreignObject>
  <foreignObject x="271" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi < BA$</div></foreignObject>
  <foreignObject x="477.5" y="285.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi = 0$</div></foreignObject>
  <foreignObject x="28" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="90" y="25.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
</svg>

## Formula: Faraday's law of induction
Faraday's observations are summarised in **Faraday's law of induction**: the induced voltage in a coil is proportional to the rate of change of the magnetic flux through the coil and to the number of turns of the coil. The average induced voltage of a coil in the time interval $\Delta t$ is
```kaavat
voltage induced in a coil :: e_\text{ka} = -N\frac{\Delta\Phi}{\Delta t}
```
where $e_\text{ka}$ is the average induced voltage (V), $N$ the number of turns of the coil, $\Delta\Phi$ the change in the magnetic flux through one turn (Wb) and $\Delta t$ the time (s) in which the change takes place.

If the flux changes at a steady rate, the induced voltage is constant over the whole interval and equal to its average, and then it is written simply $e$. If the flux changes unevenly, the instantaneous value of the voltage depends on the rate of change of the flux at that very moment: $e(t) = -N\,\tfrac{\mathrm{d}\Phi}{\mathrm{d}t}$.

The turns are in series, so each turn adds the same amount to the voltage. The units fit together: $1\,\tfrac{\text{Wb}}{\text{s}} = 1\,\text{V}$. The minus sign gives the direction of the induced voltage: it opposes the change that produces it. The direction is discussed in the chapter *Lenz's law and eddy currents*; the magnitude of the voltage is calculated from the equation $|e_\text{ka}| = N \cdot |\Delta\Phi| : \Delta t$. The magnitude is always positive, also when the flux decreases.

```pysahdy
A coil has $200$ turns. When it is moved in a magnetic field, the flux through one turn of it changes steadily from $0.030\,\text{Wb}$ to $0.010\,\text{Wb}$ in $0.50\,\text{s}$. What is the magnitude of the induced voltage?
---
The change in flux through one turn is $0.020\,\text{Wb}$, so the voltage is $|e| = 200 \cdot 0.020\,\text{Wb} : 0.50\,\text{s} = 8.0\,\text{V}$.
```

### The flux graph and the voltage
The quotient $\Delta\Phi : \Delta t$ is the slope of the flux graph $(t, \Phi)$; when the graph is curved, the instantaneous rate of change is the slope of the tangent of the graph. The induced voltage therefore does not depend on how large the flux is but on how steeply it changes. In the graph below, a coil of ten turns moves at a steady speed through a region of magnetic field. When the coil enters the field, the flux grows steadily and the voltage is constant. When the coil is completely inside the field, the flux is at its greatest but does not change, so the voltage is zero. When the coil leaves the field, the flux decreases and the voltage is equal in size but opposite in sign.

<svg data-fig="graph" viewBox="0 0 600 380" role="img" aria-label="Two graphs to scale on the same time axis from zero to four seconds. A square coil of ten turns, side 0.10 m, moves at a speed of 0.10 m/s through a region of magnetic field of 0.20 T. Upper graph: the magnetic flux in milliwebers is zero until 0.5 seconds, grows steadily to 2.0 at 1.5 s, stays constant until 2.5 seconds and decreases steadily to zero at 3.5 s. Lower graph: the induced voltage in millivolts is zero when the flux does not change, minus 20 while the flux grows and plus 20 while the flux decreases. Dashed lines at 0.5, 1.5, 2.5 and 3.5 s link the graphs. In the top right corner of the figure is the label N = 10 turns." style="max-width:100%;font-size:24px">
  <line x1="141" y1="150" x2="141" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="150" x2="186" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="150" x2="230.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="150" x2="275.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="150" x2="320.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="150" x2="365.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="150" x2="410" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="150" x2="455" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="150" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="134" x2="500" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="118" x2="500" y2="118" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="102" x2="500" y2="102" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="86" x2="500" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="70" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="150" x2="514" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,150 L513,156 L513,144 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="151" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="150" x2="141" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="150" x2="186" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="150" x2="230.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="150" x2="275.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="150" x2="320.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="150" x2="365.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="410" y1="150" x2="410" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="150" x2="455" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="150" x2="500" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="134" x2="96" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="118" x2="96" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="102" x2="96" y2="102" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="86" x2="96" y2="86" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="70" x2="96" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="532" y="135.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Phi\ (\text{mWb})$</div></foreignObject>
  <line x1="141" y1="332" x2="141" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="332" x2="186" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="332" x2="230.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="332" x2="275.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="332" x2="320.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="332" x2="365.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="332" x2="410" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="332" x2="455" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="332" x2="500" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="312" x2="500" y2="312" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="292" x2="500" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="252" x2="500" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="232" x2="500" y2="232" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="332" x2="96" y2="272" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="272" x2="514" y2="272" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,272 L513,278 L513,266 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="273" x2="96" y2="198" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,186 L102,199 L90,199 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="272" x2="141" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="272" x2="186" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="272" x2="230.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="272" x2="275.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="272" x2="320.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="272" x2="365.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="410" y1="272" x2="410" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="272" x2="455" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="272" x2="500" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="312" x2="96" y2="312" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="297.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="89" y1="292" x2="96" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="252" x2="96" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="232" x2="96" y2="232" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="532" y="257.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="155.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e\ (\text{mV})$</div></foreignObject>
  <foreignObject x="66" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="66" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="464" y="19.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$N = 10\ \text{turns}$</div></foreignObject>
  <line x1="141" y1="70" x2="141" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="230.5" y1="70" x2="230.5" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="320.5" y1="70" x2="320.5" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="410" y1="70" x2="410" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="176" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="265.5" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="355.5" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="445" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <polyline points="96,150 141,150 230.5,86 320.5,86 410,150 455,150" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,272 141,272 141,312 230.5,312 230.5,272 320.5,272 320.5,232 410,232 410,272 455,272" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

### The induced voltage of a moving conductor
When a straight metal rod moves with velocity $v$ perpendicular to a uniform magnetic field $B$, the conduction electrons of the rod move along with it. The chapter *Charged particle in electric and magnetic fields* showed that a magnetic field exerts a force $F_\text{m} = evB$ on a moving charge. The force points along the rod, so the electrons move to one end of the rod. A deficit of electrons is left at the other end, and an electric field $E$ appears between the ends, pulling the electrons back. The shift stops when the electric force $F_\text{s} = eE$ cancels the magnetic force. Then $eE = evB$, that is, $E = vB$. In a uniform field the voltage is the product of the field and the length (chapter *Uniform electric field*), so the induced voltage between the ends of the rod is
```latex
e = vBl
```
where $v$ is the velocity of the rod (m/s), $B$ the magnetic flux density (T) and $l$ the length of the rod in the field (m), when the velocity, the rod and the field are mutually perpendicular.

<svg data-fig="rod" viewBox="0 0 600 360" role="img" aria-label="Schematic picture from above, not to scale: two horizontal metal rails whose left ends are joined to a voltmeter. On the rails is a vertical copper rod that moves to the right at velocity v. The magnetic field points into the paper, shown by evenly spaced green crosses. In the middle of the rod is an electron, on which the magnetic force points downwards and the electric force upwards. Electrons have collected at the lower end of the rod, which is negative, and the upper end is positive. In the rod the electric field points from top to bottom. The distance between the rails, that is, the length of the rod in the field, is l." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-rod.webp" x="1.2" y="0" width="597" height="365.7" preserveAspectRatio="none"/>
  <foreignObject x="42" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="483.5" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="348" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="348" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="247" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#8a5f22">$\overline{E}$</div></foreignObject>
  <foreignObject x="348" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{m}$</div></foreignObject>
  <foreignObject x="348" y="119.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{s}$</div></foreignObject>
  <foreignObject x="390" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="562" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$l$</div></foreignObject>
</svg>

```pysahdy
A rod slides at $2.0\,\text{m/s}$ perpendicular to a field of $0.50\,\text{T}$, and the length of the rod in the field is $0.30\,\text{m}$. What voltage is induced between the ends of the rod?
---
The velocity, the rod and the field are mutually perpendicular, so $e = vBl = 2.0\,\text{m/s} \cdot 0.50\,\text{T} \cdot 0.30\,\text{m} = 0.30\,\text{V}$.
```

The same result follows from Faraday's law. When the rod slides along rails, the area of the loop bounded by the rails and the rod grows in the time $\Delta t$ by $\Delta A = l \cdot v\Delta t$, so the flux grows by $\Delta\Phi = Bl \cdot v\Delta t$, and the magnitude of the voltage is $\Delta\Phi : \Delta t = vBl$. When the ends of the rails are joined by a resistor, a current flows in the circuit, and the magnetic field exerts a force $F = IlB$ on the current-carrying rod, as in the chapter *Force on a current-carrying wire: the electric motor and the loudspeaker*. The direction of this force and the conservation of energy are studied in the chapter *Lenz's law and eddy currents*.

## Worked example
A coil has $250$ turns and a cross-sectional area of $4.0\,\text{cm}^2$. The coil is between the poles of an electromagnet so that the uniform field is along the axis of the coil. When the current of the electromagnet is increased, the magnetic flux density of the field grows steadily from $0.10\,\text{T}$ to $0.50\,\text{T}$ in $0.20\,\text{s}$. How large is the induced voltage between the ends of the coil?

<!-- vaihe -->

**Given and find.** Number of turns $N = 250$, area $A = 4.0\,\text{cm}^2$, magnetic flux density at first $B_1 = 0.10\,\text{T}$ and at the end $B_2 = 0.50\,\text{T}$, time $\Delta t = 0.20\,\text{s}$. The magnitude of the induced voltage $|e|$ is asked.

<!-- vaihe -->

**Principle.** The magnetic flux through the coil changes because the field grows stronger, so an induced voltage appears in the coil according to Faraday's law. The field is along the axis, that is, perpendicular to the plane of the turns, so the flux through one turn is $\Phi = BA$. The area does not change, so the change in flux is $\Delta\Phi = (B_2 - B_1)A$.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&|e| = N\frac{\Delta\Phi}{\Delta t} \\
&|e| = \frac{N(B_2 - B_1)A}{\Delta t}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The area in square metres: $A = 4.0\,\text{cm}^2 = 4.0 \cdot (0.01\,\text{m})^2 = 4.0 \cdot 10^{-4}\,\text{m}^2$. The other quantities are in SI units.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&|e| = \frac{N(B_2 - B_1)A}{\Delta t} \\
&= \frac{250 \cdot 0.40\,\text{T} \cdot 4.0 \cdot 10^{-4}\,\text{m}^2}{0.20\,\text{s}} \\
&= 0.20\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Result.** An induced voltage of $0.20\,\text{V}$ appears between the ends of the coil for as long as the field keeps growing. The result is given to two significant figures, like the area $4.0\,\text{cm}^2$ and the time $0.20\,\text{s}$.

<!-- vaihe -->

**Reasonableness.** The units fit: $\tfrac{\text{T}\cdot\text{m}^2}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. One turn would give only $1.6 \cdot 10^{-4}\,\text{Wb} : 0.20\,\text{s} = 0.80\,\text{mV}$, and $250$ turns give $250$ times that voltage. When the field stops growing, the flux no longer changes and the voltage drops to zero, even though the field is then at its strongest.

## Common misconception
Many people think that the magnetic field itself produces a voltage and that a strong field gives a large voltage. However, an induced voltage arises only from a **change in flux**: a coil at rest beside a strong magnet gets no voltage, and a coil moving steadily inside a field gets no voltage if the flux through it does not change. The flux and its rate of change are different things, in the same way as position and velocity: a large flux can stay unchanged, and zero flux can change quickly. Another common mistake is to forget the number of turns $N$ or to convert the area wrongly: $1\,\text{cm}^2 = 10^{-4}\,\text{m}^2$, not $10^{-2}\,\text{m}^2$.

## Summary
- In electromagnetic induction, an induced voltage appears in a coil when the magnetic flux through it changes. If the flux does not change, no voltage appears.
- The magnetic flux is $\Phi = BA$ when the field is perpendicular to the plane of the loop; the unit is the weber, $1\,\text{Wb} = 1\,\text{T}\cdot\text{m}^2$.
- Faraday's law: the average induced voltage is $e_\text{ka} = -N \cdot \Delta\Phi : \Delta t$, and its magnitude is $|e_\text{ka}| = N \cdot |\Delta\Phi| : \Delta t$. When the flux changes steadily, the voltage is constant and equal to its average; the minus sign gives the direction.
- The voltage between the ends of a rod moving perpendicular to the field is $e = vBl$, because the magnetic force moves the electrons of the rod to one end.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a shake-powered torch on a table. Inside the transparent body is a cylindrical magnet, and in the middle of the body is a copper coil. When the torch is shaken, the magnet slides back and forth through the coil, and the LED at the front of the torch shines." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
