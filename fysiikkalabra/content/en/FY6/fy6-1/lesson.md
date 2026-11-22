# Circuit, electric current and voltage

> **Why** does the lamp of a torch light at the same moment as you press the switch, although the electrons in the wire move more slowly than a snail?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a dark room in the evening. On a table there is a torch whose side has been drawn open: inside are two batteries in a row, a spring and a switch. The beam of the lamp lights the table and the wall on the right." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy61h-night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy61h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy61h-tube" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4f8fbf"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy61h-head" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61h-cell420" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61h-cell556" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy61h-night)"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy61h-table)"/>
  <rect x="0" y="436" width="1200" height="8" fill="#f1dfb5"/>
  <path d="M0,470 Q600,463.829163520506 1200,474" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,492 Q600,491.40084824198675 1200,496" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,514 Q600,511.6439512766883 1200,518" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,536 Q600,532.5474926083261 1200,540" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,558 Q600,552.7240073720895 1200,562" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,580 Q600,580.2344871059468 1200,584" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M790,390 L1200,170 L1200,440 Z" fill="#ffc078" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M790,390 L1200,250 L1200,440 Z" fill="#f1dfb5" stroke-linejoin="round" fill-opacity="0.45"/>
  <ellipse cx="1150" cy="300" rx="44" ry="150" fill="#ffffff" fill-opacity="0.35"/>
  <rect x="330" y="344" width="400" height="92" rx="20" fill="url(#fy61h-tube)" stroke="#1f2933" stroke-width="4"/>
  <path d="M730,350 L790,330 L790,450 L730,430 Z" fill="url(#fy61h-head)" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <rect x="786" y="330" width="14" height="112" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <circle cx="788" cy="390" r="30" fill="#ffffff"/>
  <rect x="470" y="326" width="60" height="20" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="372" y="358" width="330" height="64" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="420" y="368" width="128" height="44" rx="6" fill="url(#fy61h-cell420)" stroke="#1f2933" stroke-width="3"/>
  <rect x="504" y="370" width="36" height="40" fill="#f1dfb5"/>
  <rect x="548" y="382" width="9" height="16" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="556" y="368" width="128" height="44" rx="6" fill="url(#fy61h-cell556)" stroke="#1f2933" stroke-width="3"/>
  <rect x="640" y="370" width="36" height="40" fill="#f1dfb5"/>
  <rect x="684" y="382" width="9" height="16" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polyline points="378,410 383,370 388,410 393,370 398,410 403,370 408,410 413,370 418,410" fill="none" stroke="#8a96a3" stroke-width="4" stroke-linejoin="round"/>
  <line x1="694" y1="390" x2="730" y2="390" stroke="#b8622d" stroke-width="5" stroke-linecap="butt"/>
</svg>

## Key idea
All matter consists of atoms that contain positively charged protons and negatively charged electrons. Charges act on each other through the **electric interaction**: charges of the same sign repel each other and charges of opposite sign attract each other. In an ordinary object there are as many protons as electrons, so the object is electrically neutral. When charges are made to move in the same direction, an **electric current** arises. Electric current is thus the motion of charge, and through it the electric interaction transfers energy from a battery to a lamp.

### Conductors and insulators
A substance in which charges are able to move is a **conductor**. In metals some of the electrons are not bound to a single atom but move freely between the metal ions. These are called free electrons. This is why copper, aluminium and other metals conduct electricity well. A substance in which charges are not able to move is an **insulator**: plastic, rubber, glass and dry wood. An electric wire has a copper conductor surrounded by a plastic insulating sheath. The insulator prevents the current from flowing where it should not flow.

```pysahdy
An electrician wears rubber gloves. Why does rubber protect against an electric current?
---
Rubber is an insulator: its charges are not able to move, so a current cannot pass through the glove.
```

### Electric circuit
A lamp is lit only when it is part of a closed **electric circuit**: from a voltage source, such as a battery, a wire leads to the lamp and from the lamp a wire back to the other terminal of the voltage source. A switch opens and closes the circuit. When the switch is opened, a break appears in the circuit. The change caused by switching propagates quickly to the whole circuit, and the current stops flowing. The change does not, however, propagate infinitely fast. Current is not created in the battery and is not used up in the lamp. The same current passes through the lamp as through every other point of the circuit, and the same charge returns to the battery. The lamp does not use up charge but changes electrical energy into light and internal energy of the filament, which is transferred to the surroundings as heat.

<svg data-fig="piiri" viewBox="0 0 600 340" role="img" aria-label="A closed circuit on a table. At the bottom left two AA batteries in a row in a holder, the positive terminal on the right. From the positive terminal of the battery a wire goes to the right through a closed switch, rises to the upper right corner and goes left along the top through a lamp. The lamp is lit. The wire returns down the left edge to the negative terminal of the battery. Violet arrows show the conventional direction of current: from the positive terminal through the external circuit to the negative terminal. Schematic figure, not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-piiri.webp" x="0" y="-1.2" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="560" y="121.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="176.5" y="295.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{battery}$</div></foreignObject>
  <foreignObject x="362.5" y="295.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{switch}$</div></foreignObject>
  <foreignObject x="380" y="35.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{lamp}$</div></foreignObject>
  <foreignObject x="131" y="81.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{wire}$</div></foreignObject>
  <foreignObject x="315" y="229.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="111" y="229.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
</svg>

### Direction of current and motion of the electrons
The conventional direction of current is the direction in which a positive charge would move: in the external circuit from the positive terminal of the voltage source to the negative terminal. In a metal conductor, however, it is the negative electrons that move, and they travel in the opposite direction, from the negative terminal to the positive terminal. The conventional direction dates from the time before the electron was discovered, and it is still used in all circuit diagrams. The electrons move slowly along the wire, typically less than a millimetre per second. When the switch is closed, an electromagnetic disturbance propagates in the circuit very quickly but at a finite speed. The conductors already contain free electrons, also in the filament of the lamp, so they do not have to travel from the battery to the lamp before the lamp lights up. In an ordinary circuit only a few metres long the propagation delay is so small that the lamp appears to light at once.

<svg data-fig="johdin" viewBox="0 0 600 330" role="img" aria-label="A piece of wire magnified. On the outside is a plastic insulating sheath, and inside it a copper conductor. In the copper there are positive metal ions in a regular lattice and free electrons between them. A blue arrow points to the left: the free electrons move to the left. A violet arrow points to the right: the conventional direction of current is opposite to the motion of the electrons. Schematic figure, not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-johdin.webp" x="0" y="0" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="206" y="275.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\text{electrons}$</div></foreignObject>
  <foreignObject x="482" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="40" y="31.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{insulator}$</div></foreignObject>
  <foreignObject x="40" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{copper}$</div></foreignObject>
</svg>

### Circuit diagram
An electric circuit is drawn as a **circuit diagram**, where every component has its own symbol. In a battery the long thin line is the positive terminal and the short thick line the negative terminal. A lamp is a circle with a cross inside, and a resistor is a rectangle. Meters are drawn as circles with the letter of the meter inside: the ammeter $\text{A}$ and the voltmeter $\text{V}$. Wires are drawn as straight horizontal and vertical lines. The junction of two wires is marked with a dot.

<svg data-fig="symbolit" viewBox="0 0 600 390" role="img" aria-label="The symbols of a circuit diagram in two columns. On the left from top to bottom: a battery, where the long thin line is the positive terminal and the short thick line the negative terminal; a lamp, a circle with a cross inside; a resistor, a rectangle; an ammeter, a circle with an A inside. On the right: an open switch with its lever lifted away, a closed switch with its lever in contact, a wire, a junction as a dot, and a voltmeter, a circle with a V inside." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-symbolit.webp" x="0" y="1.2" width="600" height="398.8" preserveAspectRatio="none"/>
  <foreignObject x="31" y="15.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="71" y="15.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="120" y="47.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <foreignObject x="120" y="125.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lamp}$</div></foreignObject>
  <foreignObject x="120" y="203.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{resistor}$</div></foreignObject>
  <foreignObject x="49" y="281.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="120" y="281.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ammeter}$</div></foreignObject>
  <foreignObject x="416" y="47.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{open switch}$</div></foreignObject>
  <foreignObject x="416" y="125.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{closed switch}$</div></foreignObject>
  <foreignObject x="416" y="203.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{wire}$</div></foreignObject>
  <foreignObject x="416" y="281.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{junction}$</div></foreignObject>
  <foreignObject x="347" y="329.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="416" y="329.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{voltmeter}$</div></foreignObject>
</svg>

A diagram shows which components are connected to each other, not what the devices look like or how long the wires are. The same electric circuit can therefore be drawn as many correct-looking diagrams. What matters is that in the diagram the current passes through the same components in the same order as in the real circuit. The direction of current is marked next to a wire with an arrow from the positive terminal to the negative terminal.

<svg data-fig="kaavio" viewBox="0 0 600 320" role="img" aria-label="The circuit of Figure 2 as a circuit diagram. A rectangular loop. At the bottom left two battery cells in a row, the long line, that is the positive terminal, on the right. At the bottom right a closed switch, in the middle of the top edge a lamp, a circle with a cross. A violet arrow next to the right edge points upwards and is labelled I: the current flows from the positive terminal through the switch and the lamp to the negative terminal." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-kaavio.webp" x="10.8" y="9.6" width="576.9" height="319.7" preserveAspectRatio="none"/>
  <foreignObject x="237" y="279.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="163" y="279.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="199" y="279.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="558" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="358.5" y="279.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{switch}$</div></foreignObject>
  <foreignObject x="266" y="15.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamp}$</div></foreignObject>
</svg>

## Formula: Electric current
Electric current tells how large a charge passes through the cross-section of a conductor per unit time:
```kaavat
electric current :: I = \frac{Q}{t}
```
where $I$ is the electric current ($\text{A}$), $Q$ the charge that has passed through the cross-section ($\text{C}$) and $t$ the time ($\text{s}$). The unit of charge is the coulomb $\text{C}$ and the unit of current the ampere $\text{A}$. The current is $1\,\text{A}$ when a charge of $1\,\text{C}$ passes through the cross-section every second, that is $1\,\text{A} = 1\,\text{C/s}$. When the current is known, the charge that has passed is obtained as the product $Q = It$.

<svg data-fig="virta" viewBox="0 0 600 320" role="img" aria-label="A copper wire magnified. In the middle of the wire a cross-section is drawn with a dashed line. Blue electrons fill the whole wire, and they move to the left through the cross-section. At the top right a stopwatch. A violet arrow above the wire points to the right and is labelled I. Labels: in the time t a charge Q passes through the cross-section. Schematic figure, not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-virta.webp" x="3.7" y="0" width="594.1" height="325.5" preserveAspectRatio="none"/>
  <foreignObject x="262" y="237.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{electrons}$</div></foreignObject>
  <foreignObject x="396" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="215" y="19.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{cross-section}$</div></foreignObject>
  <foreignObject x="450" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="180" y="279.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q\ \text{passes in the time}\ t$</div></foreignObject>
</svg>

```pysahdy
The current through a conductor doubles. How does the charge that passes a cross-section in a given time change?
---
The charge doubles. By $Q = It$ it is proportional to the current when the time $t$ stays the same.
```

### Charge and the number of electrons
The charge of an electron is $-e$, where $e$ is the elementary charge, the smallest charge that occurs free. When $N$ electrons pass through a cross-section, the charge that has passed is the sum of their charges:
```latex
Q = N e
```
where $Q$ is the magnitude of the charge ($\text{C}$), $N$ the number of electrons and $e = 1.602 \cdot 10^{-19}\,\text{C}$ the elementary charge. A charge of one coulomb therefore requires about $6.24 \cdot 10^{18}$ electrons. This is why electrons are not counted one by one, but current is measured in amperes.

### Voltage
A battery does not give charge to the circuit, because the charge circulates in the circuit and returns to the battery. The battery gives energy to the charge, and the lamp changes that energy into light and internal energy of the filament, which is transferred to the surroundings as heat. **Voltage** tells how much energy is transferred per unit of charge when the charge passes between two points:
```latex
U = \frac{E}{Q}
```
where $U$ is the voltage ($\text{V}$), $E$ the energy transferred ($\text{J}$) and $Q$ the charge ($\text{C}$). The unit of voltage is the volt $\text{V}$, and $1\,\text{V} = 1\,\text{J/C}$. The voltage $1.5\,\text{V}$ of an AA battery means that every coulomb that passes from the battery to the lamp brings $1.5\,\text{J}$ of energy to the lamp, when the resistance of the wires and the battery itself is ignored. The greater the voltage, the more energy the same charge transfers.

<svg data-fig="jannite" viewBox="0 0 600 350" role="img" aria-label="A battery on the left and a lamp on the right, between them an orange arrow of energy flow from the battery to the lamp. The battery is labelled with the voltage U equal to 1.5 volts, the arrow with the energy 1.5 joules for every coulomb. The lamp radiates light and heat. At the top a wire goes from the positive terminal of the battery to the side of the lamp, at the bottom a wire returns from the base of the lamp to the bottom of the battery, and a violet arrow shows that the same charge circulates back to the battery. Schematic figure." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-jannite.webp" x="17" y="0" width="582.5" height="345.9" preserveAspectRatio="none"/>
  <foreignObject x="12" y="211.5" width="106" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U = 1.5\,\text{V}$</div></foreignObject>
  <foreignObject x="155" y="21.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="155" y="181.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="219" y="59.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.5\,\text{J}\ \text{/}\ 1\,\text{C}$</div></foreignObject>
  <foreignObject x="252.5" y="151.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{energy}$</div></foreignObject>
  <foreignObject x="96.5" y="303.5" width="407" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{the same charge returns to the battery}$</div></foreignObject>
</svg>

```pysahdy
Two batteries, $1.5\,\text{V}$ and $3.0\,\text{V}$, each move the same charge to a lamp. Which one transfers more energy, and how many times more?
---
From $U = E : Q$ we get $E = UQ$. With the same $Q$ the energy is proportional to the voltage, so the $3.0\,\text{V}$ battery transfers twice the energy.
```

### Typical values
Voltages and currents vary a lot in everyday devices. The values in the tables are orders of magnitude.

<figure class="unit-photo"><img src="pics/fy6/macro-circuit-board.webp" alt="A circuit board close up: a green capacitor, a small striped resistor and other components joined by conductors."><figcaption>The circuit board of an electronic device. The components are connected by the conductors on the board, and the capacitor is marked with the largest voltage it can withstand: $6.3\,\text{V}$.</figcaption></figure>

| Voltage source | Voltage |
|---|---|
| AA battery | $1.5\,\text{V}$ |
| phone battery | $3.7\,\text{V}$ |
| car battery | $12\,\text{V}$ |

| Device | Current |
|---|---|
| indicator LED | $0.02\,\text{A}$ |
| torch lamp | $0.3\,\text{A}$ |
| phone charger | $2\,\text{A}$ |

## Worked example
A current of $0.25\,\text{A}$ passes through a torch lamp, and the lamp is lit for $12\,\text{min}$. How large a charge passes through the lamp during this time?

<!-- vaihe -->

**Given and asked.** The current is $I = 0.25\,\text{A}$ and the time $t = 12\,\text{min}$. We are asked the charge $Q$ that passed through the lamp.

<!-- vaihe -->

**Principle.** Current tells how large a charge passes through the lamp in a second. The current stays the same all the time, so the charge is obtained from the definition of current $I = \tfrac{Q}{t}$.

<!-- vaihe -->

**Formula solved.** We solve the charge by multiplying both sides of the equation by the time:
```latex
\begin{aligned}
&I = \frac{Q}{t} \\
&Q = I t
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** An ampere is a coulomb per second, so the time is changed into seconds: $12\,\text{min} = 12 \cdot 60\,\text{s} = 720\,\text{s}$.

<!-- vaihe -->

**Substitution.** We substitute the values with their units, and $1\,\text{A}\cdot\text{s} = 1\,\text{C}$:
```latex
\begin{aligned}
Q &= I t \\
&= 0.25\,\text{A}\cdot 720\,\text{s} \\
&= 180\,\text{C}
\end{aligned}
```

<!-- vaihe -->

**Result.** The charge that passes through the lamp is $Q = 180\,\text{C}$, to two significant figures $1.8 \cdot 10^{2}\,\text{C}$ like the initial values $0.25\,\text{A}$ and $12\,\text{min}$.

<!-- vaihe -->

**Reasonableness.** Every second a quarter of a coulomb passes through the lamp, and in $720\,\text{s}$ a quarter of the number $720$ is $180$. In electrons the charge is $$180\,\text{C} : (1.602 \cdot 10^{-19}\,\text{C}) \approx 1.1 \cdot 10^{21}$$ electrons, an enormous number, but there are many more of them in the wire.

## Common misconception
Many think that a lamp uses up electric current, so that after the lamp less current would flow in the wire than before the lamp. This is not so: the same charge that enters the lamp leaves it and returns to the battery, so the current is equal on both sides of the lamp. The lamp changes the electrical energy carried by the charge into light and internal energy of the filament. Another misconception is that the electrons leave the battery and travel all the way to the lamp before the lamp lights. But the wire is already full of free electrons, and they start to move everywhere in the circuit at the same time.

## Summary
- Electric current is the motion of charge. In a metal conductor the free electrons move; in an insulator the charges are not able to move.
- Current flows only in a closed electric circuit. The same current passes through the lamp and returns to the battery: current is not used up. What is used up from the battery is energy, not charge.
- Electric current is $I = \tfrac{Q}{t}$, the unit is the ampere, $1\,\text{A} = 1\,\text{C/s}$. Charge is $Q = Ne$, where $e = 1.602 \cdot 10^{-19}\,\text{C}$.
- Voltage is the energy transferred per unit of charge, $U = \tfrac{E}{Q}$, the unit is the volt, $1\,\text{V} = 1\,\text{J/C}$.
- The conventional direction of current in the external circuit is from the positive terminal to the negative terminal; the electrons move in the opposite direction.
- In a circuit diagram components are drawn with symbols and wires as straight lines. A switch is drawn open (lever lifted) or closed (lever in contact).
