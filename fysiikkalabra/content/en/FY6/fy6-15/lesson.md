# Electrical safety at home and at work

> **Why** does the kitchen fuse trip when many devices are on at the same time, even though none of them is broken?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a kitchen in the evening. On the worktop are a kettle with steam rising from it, a coffee maker, a toaster and a microwave oven, all plugged into wall sockets. On the left wall an open fuse board has a row of circuit breakers; one of them has tripped down. Through the window can be seen the evening sky and, far away, power line pylons." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A fuse protects the cable from overheating
The electricity of a home is divided into circuits in the fuse board. Each circuit has its own circuit cable and its own fuse, usually $10\,\text{A}$ or $16\,\text{A}$. The sockets and lights of one circuit are connected in parallel, so the voltage across each device is $230\,\text{V}$ and the currents of the devices add up in the circuit cable (chapter *Resistors in series and in parallel*). The fuse is at the start of the circuit cable, so the current of the whole circuit flows through it. A single device can be in working order, but many devices together exceed the rated current of the fuse.

<svg data-fig="ryhma" viewBox="0 0 600 340" role="img" aria-label="Circuit diagram, not to scale: one electrical circuit of a home. On the left is a 230 V alternating voltage source. The upper conductor runs from the source through a fuse to the right, and three devices are connected in parallel to it: two resistors with powers P1 and P2, and a lamp with power P3. The lower ends of the devices are connected to the lower conductor, which returns to the source. Purple arrows: the whole current I flows through the fuse, and it divides into the device currents I1, I2 and I3. Below is the equation I = I1 + I2 + I3." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-ryhma.webp" x="0" y="-1.2" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="25" y="21.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$230\,\text{V}$</div></foreignObject>
  <foreignObject x="120" y="41.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{fuse}$</div></foreignObject>
  <foreignObject x="230" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="236" y="162.5" width="42" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_1$</div></foreignObject>
  <foreignObject x="330" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="346" y="162.5" width="42" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_2$</div></foreignObject>
  <foreignObject x="440" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="444" y="162.5" width="42" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_3$</div></foreignObject>
  <foreignObject x="550" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_3$</div></foreignObject>
  <foreignObject x="190" y="301.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I = I_1 + I_2 + I_3$</div></foreignObject>
</svg>

The conductors of the circuit cable have a small resistance, and they produce thermal power $P = RI^2$ (chapter *Electric power and the heating of a resistor*): when the current doubles, the thermal power of the cable becomes four times as large. The size of the fuse is chosen according to the cable: the cable determines how large a current the fuse may let through. If the current is larger for a long time, the cable and its connections heat up, the insulation is damaged and a fire can start. The fuse cuts off the current before that happens. A small overload can continue for a long time, but the larger the overcurrent, the faster the fuse acts; in a short circuit the current is cut off in a fraction of a second. In a screw-in fuse a thin wire melts from its own heating, whereas a circuit breaker trips and is switched back on. A blown fuse is never replaced with a larger one.

```pysahdy
The current in a circuit cable becomes three times as large. How many times as large does the thermal power of the cable become?
---
The thermal power is $P = RI^2$, so it is proportional to the square of the current. The power becomes $3^2 = 9$ times as large.
```

### Earthing leads the fault current away from the person
The two holes of a socket take the line conductor L and the neutral conductor N. An earthed socket also has protective earth contacts PE, which are connected to the yellow-green protective earth conductor, that is, the protective conductor. In the distribution board of the building, the protective conductor is connected to the earthing and to the conductor coming from the grid along which the current returns to the supply. The colours of the insulation of the conductors are well established in Finland: in new installations the line conductor is usually brown, the neutral conductor blue and the protective earth conductor yellow-green. In old installations the colours may differ, and you must never conclude from the colour of a conductor that it is not live.

<svg data-fig="pistorasia" viewBox="0 0 600 330" role="img" aria-label="Schematic picture, not to scale, two parts. On the left an earthed socket from the front: in a round recess are two holes for the line and neutral conductors and, at the top and bottom, metal protective earth contacts, labelled PE. On the right an electric cable with three insulated conductors coming out of its sheath: a brown line conductor L, a blue neutral conductor N and a yellow-green protective earth conductor PE." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-pistorasia.webp" x="1.2" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="66" y="11.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{socket}$</div></foreignObject>
  <foreignObject x="178" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{PE}$</div></foreignObject>
  <foreignObject x="178" y="237.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{PE}$</div></foreignObject>
  <foreignObject x="385" y="11.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{cable}$</div></foreignObject>
  <foreignObject x="418" y="85.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{line}\ \text{L}$</div></foreignObject>
  <foreignObject x="418" y="151.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{neutral}\ \text{N}$</div></foreignObject>
  <foreignObject x="418" y="217.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{earthing}\ \text{PE}$</div></foreignObject>
</svg>

The conductive metal frame of a washing machine or a kettle is connected to protective earth through the plug. If the insulation of the line conductor fails and the metal frame becomes live, the protective conductor gives the fault current a low-resistance path back to the supply. The large fault current makes the fuse or the circuit breaker cut off the current quickly. A residual current device can also cut off the supply when the fault current it detects exceeds its tripping limit. Without protective earthing, the frame would stay live, and a current would flow through a person touching the frame to the ground. This explanation applies to the TN system common in Finland; in other earthing systems the path of the fault current can be different. For this reason the earth contact must not be bypassed, and an earthed plug must not be connected to a socket without earthing by means of an extension cord or an adapter.

<svg data-fig="maadoitus" viewBox="0 0 600 380" role="img" aria-label="Schematic picture, not to scale, two panels. Each shows a device whose metal frame is drawn open: a brown line conductor comes from above to the resistor of the device, but its worn part touches the frame, marked with a spark and the word fault. A person stands on the ground and touches the frame of the device with a hand. On the left, without earthing, a purple dashed line and an arrow show the current I flowing from the frame through the person&#x27;s hand and body to the feet and the ground. On the right, a yellow-green protective earth conductor is connected to the frame, and a purple arrow shows the fault current flowing along it upwards back towards the supply; the text: the fuse trips. Only a small current flows through the person until the fuse cuts off the current." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-maadoitus.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="50" y="9.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{no earthing}$</div></foreignObject>
  <foreignObject x="340" y="9.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{protectively earthed}$</div></foreignObject>
  <foreignObject x="162" y="211.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{fault}$</div></foreignObject>
  <foreignObject x="13" y="233.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="462" y="211.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{fault}$</div></foreignObject>
  <foreignObject x="526" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_\text{E}$</div></foreignObject>
  <foreignObject x="20" y="347.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current through the person}$</div></foreignObject>
  <foreignObject x="350" y="347.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{the fuse trips}$</div></foreignObject>
</svg>

### Protection classes tell how a device protects the user
The rating plate of a device has the sign of its **protection class**. A protection class I device has a conductive frame that is protectively earthed, and its plug has earth contacts. A protection class II device has no earthing: the live parts are separated from the user by double or reinforced insulation, and the plug is often flat. A protection class III device works at a protective extra-low voltage, at most $50\,\text{V}$ alternating voltage or $120\,\text{V}$ direct voltage, which comes from a safety transformer or a battery. In ordinary conditions, touching it does not cause a dangerous current.

<svg data-fig="luokat" viewBox="0 0 600 300" role="img" aria-label="Signs of the protection classes in three columns. On the left class I: the earth symbol, that is, a vertical line and three shortening horizontal lines, inside a circle; protective earthing, for example a washing machine. In the middle class II: two nested squares; double insulation, for example a hair dryer. On the right class III: a diamond with the Roman numeral three inside; protective extra-low voltage, for example a cordless drill." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-luokat.webp" x="15.6" y="6" width="576.9" height="299.3" preserveAspectRatio="none"/>
  <foreignObject x="30" y="165.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{class I}$</div></foreignObject>
  <foreignObject x="5" y="201.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{earthing}$</div></foreignObject>
  <foreignObject x="5" y="241.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{washing machine}$</div></foreignObject>
  <foreignObject x="230" y="165.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{class II}$</div></foreignObject>
  <foreignObject x="205" y="201.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{double insulation}$</div></foreignObject>
  <foreignObject x="205" y="241.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{hair dryer}$</div></foreignObject>
  <foreignObject x="430" y="165.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{class III}$</div></foreignObject>
  <foreignObject x="405" y="201.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{extra-low voltage}$</div></foreignObject>
  <foreignObject x="405" y="241.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{cordless drill}$</div></foreignObject>
  <foreignObject x="462" y="88.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{III}$</div></foreignObject>
</svg>

### The residual current device protects a person
A fuse does not notice a current through a person: its rated current is amperes, but a current of just tens of milliamperes through the body can be life-threatening. A fuse protects a person only together with protective earthing, when a fault causes an earth fault. The small current through a person is cut off by a **residual current device** (RCD). It compares the current going to the device in the line conductor with the current returning in the neutral conductor. In an intact circuit they are equal. If part of the current gets to the ground through a fault, for example through a person, the returning current is smaller. When the difference exceeds the tripping current, usually $30\,\text{mA}$, the device cuts off the current in a fraction of a second. In new installations the socket circuits are protected with an RCD, and its test button should be pressed regularly.

<svg data-fig="vikavirtasuoja" viewBox="0 0 600 360" role="img" aria-label="Circuit diagram, not to scale. On the left a 230 V alternating voltage source. The upper conductor is the line conductor L and the lower one the neutral conductor N. Both pass through a residual current device outlined with a dashed line, where they pass through the same iron ring. After that the line conductor has a fuse. On the right a device with a resistor inside its metal frame between the line and neutral conductors; between the line conductor and the frame there is a fault, marked with a spark. From the frame a current path leads through the resistance R body of a person to the ground. Purple arrows: in the line conductor the current I L to the device, in the neutral conductor the current I N back, and the earth-fault current I E through the person to the ground. At the top right the equation I L minus I N is I E." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-vikavirtasuoja.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="16" y="25.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$230\,\text{V}$</div></foreignObject>
  <foreignObject x="71" y="77.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{L}$</div></foreignObject>
  <foreignObject x="71" y="273.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="55" y="311.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{residual current device}$</div></foreignObject>
  <foreignObject x="209" y="65.5" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{fuse}$</div></foreignObject>
  <foreignObject x="313.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_\text{L}$</div></foreignObject>
  <foreignObject x="313.5" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_\text{N}$</div></foreignObject>
  <foreignObject x="365" y="175.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{device}$</div></foreignObject>
  <foreignObject x="436" y="257.5" width="76" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_\text{body}$</div></foreignObject>
  <foreignObject x="552" y="167.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_\text{E}$</div></foreignObject>
  <foreignObject x="420" y="17.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$I_\text{L} - I_\text{N} = I_\text{E}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/residual-current-device.webp" alt="A white four-pole residual current device on a black background: a yellow TEST button, a black lever and screw terminals along the top and bottom; its side is marked with the voltage, the tripping current and the rated current."><figcaption>A residual current device. The marking $I_{\Delta n} = 0.03\,\text{A}$ means that it cuts the current when the currents in the phase and neutral conductors differ by $30\,\text{mA}$. The yellow TEST button is used to check regularly that the device works.</figcaption></figure>

An RCD does not prevent all shocks. If a person touches the line conductor and the neutral conductor at the same time, the current returns along the neutral conductor, and there is no difference between the currents of the line and neutral conductors. For this reason live parts are never touched, even if the circuit has an RCD.

```pysahdy
Which two currents does a residual current device compare, and when does it cut the current?
---
It compares the current in the line conductor and in the neutral conductor. When the difference exceeds the tripping current, usually $30\,\text{mA}$, it cuts the current.
```

### The dielectric strength of an insulator
The plastic sheath of cables, the body of a plug and the insulators of high-voltage lines separate the live parts from people. Every insulator, however, withstands only an electric field of a certain size. When the field exceeds the **dielectric strength** of the insulator, the insulator starts to conduct and a spark discharges through it (chapter *The capacitor and its energy*). In a uniform field, an insulating layer of thickness $d$ withstands a voltage $E_\text{max} d$. A larger voltage therefore needs a thicker insulator or a longer air gap, and the insulator must be intact: a crack, moisture or dirt weakens the insulation.

### High-voltage lines and step voltage
Electricity is transmitted from power plants at a high voltage, in the national grid as much as $400\,\text{kV}$, because for the same power a high voltage means a small current and thus small thermal losses $RI^2$ in the lines. High-voltage conductors are bare, and they are insulated by the surrounding air. The dielectric strength of air is about $3\,\text{MV/m}$, so you do not need to touch a conductor to get a shock: an electric arc can jump from the conductor to an object brought near it, such as the boom of a crane, a fishing rod or the string of a kite. The voltage of the overhead line of trains is $25\,\text{kV}$, so you must not climb on the roof of the carriages.

A bird can sit on a bare conductor because both its feet are at almost the same potential: the potential difference between the feet is very small, so only a very small current flows through the bird. The danger arises when a body connects two points at different potentials, for example a conductor and the ground.

If a conductor falls to the ground, the current spreads into the ground. The potential of the ground is greatest at the point of contact and decreases with distance, so there is a voltage between different points. The voltage between a person's feet is called the **step voltage**: it is the larger, the closer to the point of contact you are and the longer your step is. You move away from a fallen conductor with short steps, feet together, or by hopping with both feet together; you do not approach the conductor, and you report the damage to the emergency number $112$.

<svg data-fig="askel" viewBox="0 0 600 340" role="img" aria-label="Schematic picture, not to scale: a fallen power line and step voltage. On the left a wooden pole whose broken conductor has fallen to the ground; there is a spark at the point of contact. In the ground around the point of contact are nested dashed arcs of equal potential; the colour fades from reddish to sand colour farther away, and an arrow tells that the potential decreases. In the middle a person takes a long step: their feet are on different arcs, and there is a step voltage U step between the feet. On the right a person stands with their feet together, and the voltage between their feet is almost zero." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-15-askel.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="255" y="227.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_\text{step}$</div></foreignObject>
  <foreignObject x="445" y="227.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U \approx 0$</div></foreignObject>
  <foreignObject x="255" y="267.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potential decreases}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/high-voltage-sign.webp" alt="A yellow triangular warning sign with a black border and a black lightning arrow, on a white surface."><figcaption>The lightning-arrow sign warns of dangerous voltage. It is found, for example, on the cover of a fuse box: behind the cover are live parts that must not be touched.</figcaption></figure>

### Safe action at home and at work
In Finland, actual electrical installation work may be done only by electrical professionals, and the company doing the work must be in the register of the Finnish Safety and Chemicals Agency Tukes as an electrical contractor. A layperson may do only specifically permitted minor electrical jobs, and even those only when they are sure they know how to do the job safely and know the instructions for it. Such jobs include, for example, replacing a fuse and a lamp, resetting a tripped circuit breaker or residual current device (RCD), repairing a single-phase extension cord, replacing the broken single-phase power cord and plug of an appliance and connecting a light fitting with a lighting connector block. The work is always done with the circuit de-energised. An up-to-date list of the permitted jobs is on the website of Tukes. When in doubt, the job is left to an electrical professional.

At workplaces such as building sites, extension cords and devices are inspected, in damp places an RCD or a protective extra-low voltage is used, and a damaged device is taken out of use. If a device smells of burning, gets hotter than usual or gives small electric shocks, its plug is pulled out and the device is taken for repair. If someone is stuck to a live part, the current is switched off first, before the person is touched, and the emergency number $112$ is called.

## Formula: Current of a circuit and touch current
The devices of a circuit are in parallel at the same voltage, so the current of each device is $I_k = P_k : U$, and the sum of them flows in the circuit cable and the fuse:
```latex
I = \frac{P_1 + P_2 + P_3 + \dots}{U}
```
where $I$ is the total current of the circuit cable ($\text{A}$), $P_1, P_2, \dots$ are the powers of the devices that are on at the same time ($\text{W}$) and $U$ is the mains voltage $230\,\text{V}$. The mains voltage is the rms value of the alternating voltage. This chapter considers devices whose current and voltage are in phase, such as heating devices, or whose power factor is assumed to be approximately one. Then the power is calculated with the formula $P = UI$ as with a direct voltage. In general, the active power of an alternating-current circuit also depends on the phase difference between the voltage and the current. The circuit is not overloaded when $I$ is at most the rated current of the fuse $I_\text{f}$. The total power of the devices may therefore be at most $230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}$ in a $10\,\text{A}$ circuit and $230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W}$ in a $16\,\text{A}$ circuit.

```pysahdy
An iron ($1.1\,\text{kW}$) and a coffee maker ($0.70\,\text{kW}$) are on in the same group. What is the current in the group cable?
---
$I = \tfrac{P_1 + P_2}{U}$. Substituting: $\tfrac{1100\,\text{W} + 700\,\text{W}}{230\,\text{V}} \approx 7.8\,\text{A}$.
```

### The current through the body
When a person touches a live part and the ground at the same time, their body is part of the circuit. The current through the body is obtained from Ohm's law (chapter *Resistance and Ohm's law*):
```latex
I = \frac{U}{R}
```
where $I$ is the current through the body ($\text{A}$), $U$ is the touch voltage, that is, the voltage between the points of contact ($\text{V}$), and $R$ is the resistance of the whole current path ($\Omega$): the resistances of the skin, the inside of the body, and the shoes and the floor, in series.

The resistance of the body is not constant. Most of it is in the skin, and it depends on the moisture of the skin, the size of the contact area, the path of the current and the voltage. With dry skin and insulating shoes, the resistance of the current path can be hundreds of kilohms. Wet or sweaty skin, a large contact area and bare feet on a wet floor reduce it to about a kilohm, and then a touch voltage of $230\,\text{V}$ gives a current of $230\,\text{V} : 1\,\text{k}\Omega \approx 230\,\text{mA}$. The resistance of the inside of the body is only of the order of hundreds of ohms.

Shoes reduce the current only if they are undamaged and dry, the floor is dry and the person does not touch anything else earthed at the same time, such as a tap or an earthed device: then the current flows past the shoes. Shoes must not be regarded as equipment that protects against electric shock.

| $I$ (approx.) | effect |
| --- | --- |
| $0.5\,\text{mA}$ | the current can be felt |
| $10\,\text{mA}$ | the grip does not release |
| $30\,\text{mA}$ | breathing becomes difficult |
| over $50\,\text{mA}$ | danger of ventricular fibrillation |

About $0.5\,\text{mA}$ is the threshold of perception. A current of about $10\,\text{mA}$ cramps the muscles so that you may not be able to let go: this is the let-go threshold. A current of over $50\,\text{mA}$ can cause ventricular fibrillation of the heart if it lasts about a second; a shorter shock needs a larger current.

The table applies to the $50\,\text{Hz}$ alternating current of a home. The usual tripping current of an RCD, $30\,\text{mA}$, has been chosen so that the device usually cuts off the current before it has time to cause ventricular fibrillation. The values are indicative, and they are based on the effects of current on an adult described in the international standard IEC 60479-1. The effect also depends on the duration and path of the current and on the person, and no current can be regarded as certainly safe.

<svg data-fig="vaikutukset" viewBox="0 0 600 360" role="img" aria-label="Scale, not linear: the size of the 50 hertz alternating current I through the body in milliamperes on a logarithmic vertical axis from 0.1 mA to 1000 mA, each tenfold increase an equally long interval. Beside the axis a colour bar: below 0.5 mA green, 0.5-10 mA light orange, 10-50 mA orange and over 50 mA red. Labels: 0.5 mA the current can be felt, 10 mA the grip does not release, 30 mA breathing becomes difficult, 50 mA danger of ventricular fibrillation. Indicative values." style="max-width:100%;font-size:24px">
  <line x1="140" y1="334" x2="140" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M140,32 L133,48 L147,48 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="95" y="3.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I\ (\text{mA})$</div></foreignObject>
  <line x1="134" y1="330" x2="140" y2="330" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="315.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0.1$</div></foreignObject>
  <line x1="134" y1="264" x2="140" y2="264" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="249.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <line x1="134" y1="198" x2="140" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="183.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <line x1="134" y1="132" x2="140" y2="132" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="117.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$100$</div></foreignObject>
  <line x1="134" y1="66" x2="140" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="51.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$1000$</div></foreignObject>
  <rect x="146" y="284" width="26" height="46" fill="#b2f2bb" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="146" y="198" width="26" height="86" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="146" y="152" width="26" height="46" fill="#e8590c" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="146" y="66" width="26" height="86" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="172" y1="284" x2="190" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="284" x2="202" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="269.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0.5\,\text{mA}\ \ \text{the current can be felt}$</div></foreignObject>
  <line x1="172" y1="198" x2="190" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="198" x2="202" y2="212" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="197.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10\,\text{mA}\ \ \text{the grip does not release}$</div></foreignObject>
  <line x1="172" y1="166.5" x2="190" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="166.5" x2="202" y2="172.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="158" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30\,\text{mA}\ \ \text{breathing becomes difficult}$</div></foreignObject>
  <line x1="172" y1="152" x2="190" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="152" x2="202" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210" y="111.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$50\,\text{mA}\ \ \text{danger of fibrillation}$</div></foreignObject>
</svg>

## Worked example
A kitchen socket circuit is protected by a $16\,\text{A}$ fuse. In the morning a kettle ($2.2\,\text{kW}$), a coffee maker ($1.0\,\text{kW}$) and a microwave oven with an input power of $1.3\,\text{kW}$ are on at the same time. How large a current flows in the circuit cable, and is the rated current of the fuse exceeded?

<!-- vaihe -->

**Given and asked.** $P_1 = 2.2\,\text{kW}$, $P_2 = 1.0\,\text{kW}$, $P_3 = 1.3\,\text{kW}$, $U = 230\,\text{V}$, rated current of the fuse $I_\text{f} = 16\,\text{A}$. We are asked for the current $I$ in the circuit cable and whether $I > I_\text{f}$.

<!-- vaihe -->

**Principle.** The devices are connected in parallel on the same circuit, so the voltage across each is $230\,\text{V}$ and their currents add up in the circuit cable and the fuse. The total current is therefore calculated from the total power of the devices.

<!-- vaihe -->

**Formula solved.**
```latex
I = \frac{P_1 + P_2 + P_3}{U}
```

<!-- vaihe -->

**Unit conversions.** $$\begin{aligned} &P_1 + P_2 + P_3 \\ &= 2.2\,\text{kW} + 1.0\,\text{kW} + 1.3\,\text{kW} \\ &= 4.5\,\text{kW} \\ &= 4.5 \cdot 1000\,\text{W} \\ &= 4500\,\text{W} \end{aligned}$$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
I &= \frac{P_1 + P_2 + P_3}{U} \\
&= \frac{4500\,\text{W}}{230\,\text{V}} \\
&= 19.6\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Result.** A current of about $20\,\text{A}$ flows in the circuit cable, two significant figures like the powers. It is larger than the rated current of the fuse, $16\,\text{A}$, so the circuit is overloaded. Such a small overcurrent does not cut off the current at once, but the fuse trips if the load continues long enough. It is worth using the devices in turn.

<!-- vaihe -->

**Reasonableness.** The currents of the devices are $9.6\,\text{A}$, $4.3\,\text{A}$ and $5.7\,\text{A}$, and their sum is the same $19.6\,\text{A}$. The estimate $4500\,\text{W} : 200\,\text{V} \approx 22\,\text{A}$ is slightly larger, because the divisor is smaller. No single device exceeds $16\,\text{A}$ alone; only the common current does.

## Common misconception
Many people think that a fuse protects a person from electric shock. A fuse protects the cables: its rated current is $10\,\text{A}$ or $16\,\text{A}$, whereas a current of only about $50\,\text{mA}$ through the body can cause ventricular fibrillation of the heart. A fuse does not notice so small a current through a person at all. It protects a person only together with protective earthing: in a frame fault, a large fault current flows along the protective conductor back to the supply, and the fuse cuts it off. The small current through a person is cut off by the residual current device (RCD), which trips at a fault current of about $30\,\text{mA}$.

Another mistake is to think that a large voltage alone is dangerous or that a small voltage is always safe. The harm is done by the current through the body, which depends on both the voltage and the resistance of the current path. A bird sits safe on a $20\,\text{kV}$ conductor because the potential difference between its feet is very small, but wet skin can make even a smaller voltage dangerous.

## Summary
- The devices of one circuit are in parallel, so the current through the fuse is their total current $I = (P_1 + P_2 + \dots) : U$. A fuse protects the cable from overheating, because the thermal power of the cable is $RI^2$.
- Protective earthing connects the metal frame of a device to the protective conductor. The fault current of a frame fault flows along the yellow-green protective conductor back to the supply, and then the fuse or the circuit breaker cuts off the current. The protection classes are I (earthing), II (double insulation) and III (protective extra-low voltage).
- A residual current device (RCD) compares the currents of the line and neutral conductors and cuts off the current when the difference exceeds about $30\,\text{mA}$.
- The current through the body is $I = U : R$. Wet skin reduces the resistance, and a current of just tens of milliamperes can be life-threatening.
- An insulator withstands a field only up to its dielectric strength; from a high-voltage line an electric arc can jump through the air without contact. Near a conductor that has fallen to the ground, the step voltage is dangerous.
- In Finland, actual electrical installation work belongs to electrical professionals. A layperson may do only specifically permitted minor jobs, such as replacing a fuse, and only if they know how to do the job safely.
