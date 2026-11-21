# Changes of state of a gas and Boyle's law

> **Why** does a sealed bag of crisps swell up tight on an aeroplane, even though nothing has been added to it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on the tray table of an aeroplane seat there is a swollen, tight bag of crisps and a mug of water. Through the window clouds can be seen far below." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-9-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
The state of a fixed amount of gas is described by its pressure $p$, volume $V$ and temperature $T$. When one of them changes, at least one of the others usually changes too. This kind of change is called a change of state. It is easiest to study changes of state by keeping one of the quantities constant. In an isothermal change the temperature is constant, in an isobaric change the pressure, and in an isochoric change the volume.

According to the micro model, the pressure of a gas comes from particles colliding with the walls of the container. If the gas is compressed to half of its original volume and the temperature stays the same, the particles move as fast as before, but they hit the walls twice as often. The pressure doubles.

<svg data-fig="micro-boyle" viewBox="0 0 600 332" role="img" aria-label="Micro model of Boyle&#x27;s law, schematic picture. On the left, a cylinder contains eight gas particles in volume V at pressure p. On the right, the same eight particles have been squeezed by pressing the piston to half the volume, V/2, at the same temperature. The velocity arrows are equally long, but there are twice as many hit marks on the piston and the bottom, so the pressure is 2p. The heights of the gas spaces are in the ratio 2 : 1." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-9-micro-boyle.webp" x="0" y="0" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="238" y="51.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hit}$</div></foreignObject>
  <foreignObject x="205" y="171.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T\ \text{constant}$</div></foreignObject>
  <foreignObject x="81" y="289.5" width="78" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V\ \text{and}\ p$</div></foreignObject>
  <foreignObject x="352.5" y="289.5" width="115" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V/2\ \text{and}\ 2p$</div></foreignObject>
</svg>

So in an isothermal change the pressure is inversely proportional to the volume, and the product of pressure and volume stays constant. This is called Boyle's law. It answers the opening question: the air pressure in the aeroplane cabin drops to about $78\,\text{kPa}$, so the air in the bag expands until the bag is tight. In a tight bag the pressure of the air stays slightly higher than the cabin pressure, and that is why the bag feels hard.

```pysahdy
The volume of a gas is reduced to one third, and the temperature stays the same. What happens to the pressure?
---
The pressure triples, because the product $pV$ stays constant.
```

Boyle's law works well for air and other gases at ordinary pressures and temperatures. The amount of gas must stay the same, so no gas may leak out or come in. The pressure used is the total pressure of the gas, not the gauge pressure shown by a meter.

Boyle's law can be verified experimentally. Air is sealed in a syringe, and the syringe is connected to a pressure gauge. The plunger is pressed in steps, and the pressure is read at each volume. The measurement is done slowly so that the temperature of the air has time to return to room temperature. When the results are plotted in a $(V, p)$ coordinate system, the points lie on a falling curve, and it is hard to see from it whether the relationship is exactly inverse proportionality. So a new column $1/V$ is calculated in the table, and $p$ is plotted as a function of $1/V$. If the law holds, within the measurement uncertainty the points lie on a straight line through the origin, and the slope of the line is the constant $pV$. Try it in the simulation: save measurements at different volumes and choose “Plot p as a function of 1/V”.

When a gas is heated, its particles move faster. If the piston can move so that the pressure stays constant (an isobaric change), the gas expands. When the amount of gas stays the same and the gas is dilute, its volume is directly proportional to the temperature in kelvins. If the volume is instead kept constant (an isochoric change), the pressure rises, and it is directly proportional to the temperature in kelvins. In both cases the temperature must be given in kelvins, because the proportionality starts from absolute zero.

<svg data-fig="iso-processes" viewBox="0 0 600 412" role="img" aria-label="Two changes of state, schematic picture. On the left, an isobaric change: the piston of the cylinder is loaded by an object of constant weight, so when the gas warms from temperature T₁ to temperature T₂, the piston rises and the volume increases from V₁ to V₂; the velocity arrows of the particles are longer. On the right, an isochoric change: the volume V of a rigid, closed container stays the same, and when the gas warms, the needle of the pressure gauge turns to the greater pressure p₂." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-9-iso-processes.webp" x="0" y="0" width="600" height="420" preserveAspectRatio="none"/>
  <foreignObject x="96" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{isobaric}$</div></foreignObject>
  <foreignObject x="390" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{isochoric}$</div></foreignObject>
  <foreignObject x="65" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$m$</div></foreignObject>
  <foreignObject x="40" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_1\text{, }V_1$</div></foreignObject>
  <foreignObject x="205" y="164.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$m$</div></foreignObject>
  <foreignObject x="180" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_2\text{, }V_2$</div></foreignObject>
  <foreignObject x="136" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="355" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_1\text{, }p_1$</div></foreignObject>
  <foreignObject x="475" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_2\text{, }p_2$</div></foreignObject>
  <foreignObject x="440" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
</svg>

```pysahdy
A gas in a rigid, closed container is heated. Which quantity increases, and why?
---
The pressure increases, because the volume is constant and the particles move faster.
```

<figure class="unit-photo"><img src="pics/fy3/barrel-balloon.webp" alt="Researchers fill a large transparent gas balloon on a snowy plain on a sunny day."><figcaption>Filling a NASA BARREL research balloon in Antarctica. Helium fills only the top of the balloon, because the gas expands as the outside pressure falls while the balloon rises.</figcaption></figure>

## Formula: Boyle's law and changes of state of a gas
In an isothermal change, that is, according to Boyle's law,
```latex
p_1 V_1 = p_2 V_2
```
where $p_1$ and $V_1$ are the pressure (Pa) and volume (m³) of the gas in the initial state and $p_2$ and $V_2$ in the final state. The equation is the same as $pV = \text{constant}$. Dividing it by $V$ gives
```latex
p = \text{constant} \cdot \frac{1}{V}
```
So the pressure is inversely proportional to the volume. If we write $x = 1/V$ and $y = p$, the equation has the form $y = kx$, like the equation of a straight line in FY1. So the $(1/V, p)$ graph is a straight line through the origin, and its slope is $k = pV$.

The unit of the product $pV$ is $\text{Pa} \cdot \text{m}^3 = \text{N/m}^2 \cdot \text{m}^3 = \text{N} \cdot \text{m} = \text{J}$, and $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$. Because both sides of the equation $p_1 V_1 = p_2 V_2$ have the same units, pressure and volume can also be given in, for example, kilopascals and litres, as long as they are the same on both sides.

<svg data-fig="boyle-graphs" viewBox="0 0 600 580" role="img" aria-label="Two graphs of the same measurements, to scale, when pV = 2000 kPa·ml. Above, pressure as a function of volume is a falling curve; the measurement points V = 10, 15, 20, 30 and 40 ml are on the curve. Below, pressure as a function of the reciprocal of the volume, 1/V, is a straight line through the origin whose slope is pV." style="max-width:100%;font-size:24px">
  <line x1="170" y1="250" x2="170" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="244.5" y1="250" x2="244.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318.5" y1="250" x2="318.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="393" y1="250" x2="393" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="215" x2="430" y2="215" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="180.5" x2="430" y2="180.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="145.5" x2="430" y2="145.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="111" x2="430" y2="111" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="250" x2="444" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,250 L443,256 L443,244 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="251" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="170" y1="250" x2="170" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153.5" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="244.5" y1="250" x2="244.5" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="228" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="318.5" y1="250" x2="318.5" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="302" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="393" y1="250" x2="393" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="376.5" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="215" x2="96" y2="215" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="200.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="180.5" x2="96" y2="180.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="166" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="145.5" x2="96" y2="145.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="131" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="111" x2="96" y2="111" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="96.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="61.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="235.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{ml})$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="155.5,76 157,81 159,85.5 160.5,90 162,94 164,98 165.5,101.5 167.5,105.5 169,108.5 171,112 172.5,115 174.5,118 176,121 177.5,123.5 179.5,126 181,128.5 183,131 184.5,133.5 186.5,135.5 188,137.5 189.5,139.5 191.5,141.5 193,143.5 195,145.5 196.5,147.5 198.5,149 200,150.5 201.5,152.5 203.5,154 205,155.5 207,157 208.5,158 210.5,159.5 212,161 213.5,162 215.5,163.5 217,164.5 219,166 220.5,167 222.5,168 224,169.5 225.5,170.5 227.5,171.5 229,172.5 231,173.5 232.5,174.5 234.5,175.5 236,176 238,177 239.5,178 241,179 243,179.5 244.5,180.5 246.5,181.5 248,182 250,183 251.5,183.5 253,184.5 255,185 256.5,185.5 258.5,186.5 260,187 262,187.5 263.5,188.5 265,189 267,189.5 268.5,190 270.5,191 272,191.5 274,192 275.5,192.5 277,193 279,193.5 280.5,194 282.5,194.5 284,195 286,195.5 287.5,196 289.5,196.5 291,197 292.5,197.5 294.5,198 296,198.5 298,199 299.5,199 301.5,199.5 303,200 304.5,200.5 306.5,201 308,201.5 310,201.5 311.5,202 313.5,202.5 315,203 316.5,203 318.5,203.5 320,204 322,204.5 323.5,204.5 325.5,205 327,205.5 328.5,205.5 330.5,206 332,206.5 334,206.5 335.5,207 337.5,207 339,207.5 340.5,208 342.5,208 344,208.5 346,208.5 347.5,209 349.5,209 351,209.5 353,210 354.5,210 356,210.5 358,210.5 359.5,211 361.5,211 363,211.5 365,211.5 366.5,212 368,212 370,212.5 371.5,212.5 373.5,212.5 375,213 377,213 378.5,213.5 380,213.5 382,214 383.5,214 385.5,214.5 387,214.5 389,214.5 390.5,215 392,215 394,215.5 395.5,215.5 397.5,215.5 399,216 401,216 402.5,216.5 404.5,216.5 406,216.5 407.5,217 409.5,217 411,217 413,217.5 414.5,217.5 416.5,217.5 418,218 419.5,218 421.5,218.5 423,218.5 425,218.5 426.5,218.5 428.5,219 430,219" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="170" cy="111" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="207.5" cy="157" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="244.5" cy="180.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="318.5" cy="203.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="393" cy="215" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="440" y="200.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{curve}$</div></foreignObject>
  <line x1="207.5" y1="520" x2="207.5" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318.5" y1="520" x2="318.5" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="520" x2="430" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="485" x2="430" y2="485" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="450.5" x2="430" y2="450.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="415.5" x2="430" y2="415.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="381" x2="430" y2="381" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="346" x2="430" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="520" x2="444" y2="520" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,520 L443,526 L443,514 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="521" x2="96" y2="332" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,320 L102,333 L90,333 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="207.5" y1="520" x2="207.5" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="178.5" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.04$</div></foreignObject>
  <line x1="318.5" y1="520" x2="318.5" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="289.5" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.08$</div></foreignObject>
  <line x1="430" y1="520" x2="430" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="401" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.12$</div></foreignObject>
  <line x1="89" y1="485" x2="96" y2="485" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="470.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="450.5" x2="96" y2="450.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="436" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="415.5" x2="96" y2="415.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="401" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="381" x2="96" y2="381" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="366.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="346" x2="96" y2="346" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="525.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="505.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1/V\ (\text{1/ml})$</div></foreignObject>
  <foreignObject x="86" y="289.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="96,520 430,353" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="374.5" cy="381" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="281.5" cy="427" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="235" cy="450.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="189" cy="473.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="165.5" cy="485" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="440" y="360.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{line}$</div></foreignObject>
</svg>

In an isobaric and in an isochoric change
```latex
\frac{V_1}{T_1} = \frac{V_2}{T_2} \qquad \text{and} \qquad \frac{p_1}{T_1} = \frac{p_2}{T_2}
```
where $T_1$ and $T_2$ are the temperatures of the gas in kelvins (K) in the initial and final state. So the volume or the pressure of a closed, dilute gas is directly proportional to the temperature in kelvins, and the extension of the straight line in a $(T, V)$ or $(T, p)$ graph passes through the origin, that is, through absolute zero, $0\,\text{K}$. The extension is a prediction of the model: a real gas condenses into a liquid before $0\,\text{K}$ is reached.

The temperature in kelvins is obtained from the Celsius temperature $\theta$ by adding 273.15:
```latex
T = \theta + 273.15\,\text{K}
```
where $\theta$ is the temperature in degrees Celsius as a number; in calculations $273\,\text{K}$ is enough.

<svg data-fig="absolute-zero" viewBox="0 0 600 640" role="img" aria-label="Graphs to scale when T is 0–400 K. Above, the volume of a gas at constant pressure, below, the pressure of a gas at constant volume, as a function of the temperature in kelvins. The measurement points between 253 and 373 K are on a straight line. The extension of the line, drawn dashed, passes through the origin: the volume or the pressure would be zero at absolute zero, 0 K, that is, −273 °C." style="max-width:100%;font-size:24px">
  <line x1="179.5" y1="240" x2="179.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="240" x2="263" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="240" x2="346.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="240" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="189" x2="430" y2="189" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137.5" x2="430" y2="137.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="86" x2="430" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="240" x2="444" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,240 L443,246 L443,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="241" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="240" x2="179.5" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="263" y1="240" x2="263" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="346.5" y1="240" x2="346.5" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="430" y1="240" x2="430" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="189" x2="96" y2="189" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="174" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="137.5" x2="96" y2="137.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="123" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="86" x2="96" y2="86" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="72" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="462" y="225.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (\text{K})$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\textsf{l})$</div></foreignObject>
  <foreignObject x="86" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="61" y="283.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$-273^\circ\text{C}$</div></foreignObject>
  <polyline points="96,240 307.5,145" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <polyline points="307.5,145 407.5,100" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="307.5" cy="145" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="134" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="357.5" cy="122.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="382.5" cy="111.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="407.5" cy="100" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="123.5" y="162" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{extension}$</span></div></foreignObject>
  <line x1="179.5" y1="556" x2="179.5" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="556" x2="263" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="556" x2="346.5" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="556" x2="430" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="506" x2="430" y2="506" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="456" x2="430" y2="456" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="406" x2="430" y2="406" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="556" x2="444" y2="556" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,556 L443,562 L443,550 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="557" x2="96" y2="382" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,370 L102,383 L90,383 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="556" x2="179.5" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="263" y1="556" x2="263" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="346.5" y1="556" x2="346.5" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="430" y1="556" x2="430" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="506" x2="96" y2="506" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="491.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="456" x2="96" y2="456" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="441.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="406" x2="96" y2="406" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="391.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <foreignObject x="462" y="541.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (\text{K})$</div></foreignObject>
  <foreignObject x="86" y="339.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <foreignObject x="86" y="565.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="61" y="599.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$-273^\circ\text{C}$</div></foreignObject>
  <polyline points="96,556 307.5,462.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <polyline points="307.5,462.5 407.5,418" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="307.5" cy="462.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="451.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="357.5" cy="440.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="382.5" cy="429" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="407.5" cy="418" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="123.5" y="478.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{extension}$</span></div></foreignObject>
</svg>

```pysahdy
The temperature of a gas rises from $20\,{}^\circ\text{C}$ to $40\,{}^\circ\text{C}$ at constant volume. Does the pressure double?
---
No. In kelvins the temperature rises from $293\,\text{K}$ to $313\,\text{K}$, so the pressure increases only by a factor of $313/293 \approx 1.07$.
```

## Worked example
At the airport, a bag of crisps contains $0.80\,\textsf{l}$ of air at a pressure of $101\,\text{kPa}$. During the flight the cabin pressure is $78\,\text{kPa}$. What is the volume of the air in the bag during the flight, if the temperature stays the same and the bag can expand freely?

<!-- vaihe -->

**Given and find.** We know $p_1 = 101\,\text{kPa}$, $V_1 = 0.80\,\textsf{l}$ and $p_2 = 78\,\text{kPa}$. The temperature is the same.

We want the final volume $V_2$ in litres.

<!-- vaihe -->

**Principle.** The bag is sealed, so the amount of air does not change, and the temperature stays the same. So the change is isothermal and Boyle's law holds: the product $pV$ stays constant. The bag expands freely, so the pressure inside it is always the same as in the cabin.

<!-- vaihe -->

**Rearranged formula.** Solve $V_2$ from Boyle's law by dividing both sides by the pressure $p_2$:
```latex
\begin{aligned}
p_1 V_1 &= p_2 V_2 \\
V_2 &= \frac{p_1 V_1}{p_2}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** No units need to be converted. Both pressures are in kilopascals, so they cancel in the quotient, and the volume comes out directly in litres.

<!-- vaihe -->

**Substitution.** Substitute the values with their units:
```latex
\begin{aligned}
V_2 &= \frac{p_1 V_1}{p_2} \\
&= \frac{101\,\text{kPa} \cdot 0.80\,\textsf{l}}{78\,\text{kPa}} \\
&= 1.036\,\textsf{l}
\end{aligned}
```

<!-- vaihe -->

**Result.** The volume of the air is $V_2 \approx 1.0\,\textsf{l}$, to two significant figures like the initial data $0.80\,\textsf{l}$ and $78\,\text{kPa}$. The volume increases by about $30\,\%$. If the bag is already almost full, it swells tight.

<!-- vaihe -->

**Reasonableness.** The pressure decreases, so the volume must increase. The factor of increase is the pressure ratio $101/78 \approx 1.3$, and $0.80\,\textsf{l} \cdot 1.3 \approx 1.0\,\textsf{l}$. At the end the product $pV$ is $78\,\text{kPa} \cdot 1.036\,\textsf{l} \approx 80.8\,\text{kPa}\cdot\textsf{l}$, the same as at the start, $101\,\text{kPa} \cdot 0.80\,\textsf{l} = 80.8\,\text{kPa}\cdot\textsf{l}$.

## Common misconception
Three mistakes are often repeated:

- **Inverse proportionality is not a falling straight line.** When the volume doubles, the pressure halves, so the $(V, p)$ graph is a curve that approaches the axes but never meets them. A straight line is obtained only when $p$ is plotted as a function of $1/V$.
- **Celsius degrees do not work in a ratio of temperatures.** When $1.00\,\textsf{l}$ of air is heated at constant pressure from $10\,{}^\circ\text{C}$ to $20\,{}^\circ\text{C}$, its volume does not double. Calculated in kelvins, $$\begin{aligned} V_2 &= V_1 T_2 / T_1 \\ &= 1.00\,\textsf{l} \cdot 293\,\text{K} / 283\,\text{K} \\ &\approx 1.04\,\textsf{l} \end{aligned}$$, so the volume increases by only about $3.5\,\%$.
- **The pressure of a gas in a closed container does not come from the weight of the gas.** In a small container the weight of the gas is negligible, and the pressure comes from the collisions of the particles, so it is equal everywhere in the container.

## Summary
- In a change of state, the pressure, volume and temperature of a gas change. In an isothermal change $T$ is constant, in an isobaric change $p$, and in an isochoric change $V$.
- Boyle's law: in an isothermal change $p_1 V_1 = p_2 V_2$, so the pressure is inversely proportional to the volume.
- Inverse proportionality is verified by calculating a column $1/V$ in the table and plotting $p$ as a function of $1/V$: the points must lie on a straight line through the origin, within the measurement uncertainty.
- When the amount of gas stays the same, the volume of a dilute gas at constant pressure, and the pressure at constant volume, is directly proportional to the temperature in kelvins. In these calculations the temperatures are always given in kelvins.
