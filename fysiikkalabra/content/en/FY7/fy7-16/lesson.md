# Applied chapter: wireless charging, the induction hob and the fibre link

> **Why** does a phone charge without a cable, a pan get hot without a flame and an internet connection travel as light in a glass fibre?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a kitchen worktop. In the middle is a black induction hob with a steel pan on the cooking zone, and steam rises from the pan. On the right a phone rests on a round wireless charger. On the wall at the left is a fibre router, with a thin optical cable running to it, and the end of the cable glows." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-16-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Three devices, two phenomena
Three everyday devices in the kitchen work by phenomena from this course. A wireless charger and an induction hob are based on **electromagnetic induction**: a changing magnetic flux produces a voltage in a wire loop or eddy currents in a metal (chapters *Electromagnetic induction* and *Lenz's law and eddy currents*). A fibre link is based on **total internal reflection**: light stays in the core of the fibre because it meets the boundary between the core and the cladding at an angle of incidence larger than the critical angle (chapter *Total internal reflection and optical fibre*). In this chapter the ideas are combined: in which device energy is transferred, where it is lost and what limits how the device works.

### Wireless charging: a transformer without an iron core
The pad of a wireless charger contains a flat **transmitter coil**, and under the back cover of the phone there is a similar **receiver coil**. An alternating current flows in the transmitter coil, at a frequency of about $100$–$200\,\text{kHz}$ in Qi-standard chargers. The current produces a changing magnetic field, and part of its flux passes through the receiver coil. The changing flux induces an alternating voltage in the receiver coil according to the law of induction: the instantaneous value of the voltage depends on the rate of change of the flux at each moment. The electronics of the phone rectifies the voltage and uses it to charge the battery. The device is like a transformer (chapter *The transformer and the transmission of electrical energy*), but the coils are not joined by an iron core: between them there is only air and plastic.

### Why distance decides
In a transformer the iron core guides almost all of the flux through the secondary coil. Without a core, the field lines of the transmitter coil loop around the wires of the coil and turn back close to the coil. When the phone lies right on the pad, a large part of the flux passes through the receiver. When the phone is lifted, fewer and fewer field lines reach the receiver, and the flux and the voltage fall steeply. In the figure the green lines are field lines of the transmitter coil, the green triangle shows the direction of the field at the centre of the coil, and the lines that pass through the receiver coil are drawn darker. This is why the gap between the charger and the phone is only a few millimetres. A thin ferrite sheet is placed behind the coils. Ferrite is magnetised like a ferromagnetic substance but conducts electricity poorly, so large eddy currents are not produced in it. The sheet gathers the field between the coils and keeps it from heating the metal parts of the phone.

<svg data-fig="charger" viewBox="0 0 600 380" role="img" aria-label="Schematic of a wireless charger in cross-section, field shape calculated: two panels. In each, at the bottom is the charging pad with the transmitter coil inside it, and above it is the phone, with a receiver coil of the same size in its base. The alternating current of the transmitter coil produces a magnetic field whose green field lines loop around the wires of the coil and pass upward through the middle of the coil; the green triangle at the centre of the coil shows the direction of the field. On the left the phone is 3 millimetres away, and six field lines pass through the receiver coil. On the right the phone is 20 millimetres away, and only one line passes through the receiver; the other lines turn back before reaching the phone. The lines passing through the receiver are drawn darker." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-16-charger.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="115" y="214.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{phone}$</span></div></foreignObject>
  <foreignObject x="415" y="146.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{phone}$</span></div></foreignObject>
  <foreignObject x="75" y="17.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$z = 3\,\text{mm}$</div></foreignObject>
  <foreignObject x="370" y="17.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$z = 20\,\text{mm}$</div></foreignObject>
  <foreignObject x="100" y="303.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{charger}$</div></foreignObject>
  <foreignObject x="400" y="303.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{charger}$</div></foreignObject>
  <foreignObject x="8" y="337.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{transmitter coil}$</div></foreignObject>
  <foreignObject x="306" y="85.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{receiver coil}$</div></foreignObject>
</svg>

```pysahdy
A phone is lifted from a height of $3\,\text{mm}$ above a wireless charger to a height of $20\,\text{mm}$. Why does the voltage induced in the receiver coil decrease even though the current in the transmitter coil stays the same?
---
Fewer field lines pass through the receiver, so the flux decreases. A smaller flux and a smaller change in it induce a smaller voltage.
```

### Losses in wireless charging
A sufficient voltage is obtained in the receiver even if only part of the flux reaches it, but then a larger current has to flow in the transmitter coil. In the resistance of the coils the current changes electrical energy into internal energy at the power $P = RI^2$, so the charger and the phone get warm.

In one device comparison made in 2020 (Ravenscraft, OneZero, 2020), charging a phone from empty to full took $14.26\,\text{Wh}$ from the wall socket with a cable and on average $21.01\,\text{Wh}$ with a charging pad with the phone in place, that is about $47\,\%$ more energy. When the coils were slightly offset from each other, charging took $25.62\,\text{Wh}$. The difference depends on the charger, the phone, the charging method and the alignment of the coils, however, so the figures do not apply to all wireless chargers. If there is a coin or a key between the charger and the phone, eddy currents are produced in it and it gets hot. This is why the charger detects a foreign metal object and stops charging.

### Induction hob: the base of the pan as the secondary
Under the glass top of an induction hob there is a flat copper coil in which an alternating current flows at a frequency of tens of kilohertz. The changing magnetic field of the coil passes through the glass into the base of the pan. The flux through the base changes all the time, so eddy currents are induced in the base. According to Lenz's law they circulate so that their own field opposes the change of flux. In the resistance of the base the electrical energy of the eddy currents changes into internal energy of the base, and the hot base heats the food.

The working of an induction hob thus resembles a transformer in which the metal base of the pan acts as the secondary. The base does not, however, form a single turn of an ordinary coil: the changing magnetic field produces many paths of eddy currents in it. Glass does not conduct electricity, so no currents are produced in it. The glass gets warm only from the hot pan.

<svg data-fig="hob" viewBox="0 0 600 360" role="img" aria-label="Schematic of an induction hob in cross-section, not to scale. At the top is a steel pan containing water. The pan stands on the glass top of the hob, and under the glass is a flat copper coil. The alternating current of the coil produces a changing magnetic field whose green field lines loop around the wires of the coil; the outermost ones pass through the glass into the base of the pan. In the base of the pan an eddy current circulates in the opposite direction to the current of the coil. The direction of the current of the coil is marked on the copper-coloured wires with white dots and crosses, and the direction of the eddy current with purple marks. Orange arrows show that energy is transferred from the heating base to the water. No current flows in the glass top." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-16-hob.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="470" y="85.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{water}$</div></foreignObject>
  <foreignObject x="12" y="105.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{steel pan}$</div></foreignObject>
  <foreignObject x="20" y="285.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{glass}$</div></foreignObject>
  <foreignObject x="522" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{coil}$</div></foreignObject>
  <foreignObject x="443" y="125.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{eddy current}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/induction-hob.webp" alt="A black glass hob with four cooking zones and touch controls at the front; a steel saucepan stands at the back right."><figcaption>An induction hob. An alternating current flows in a coil under the glass, and its changing magnetic field induces eddy currents in the steel base of the pan. The pan heats itself, and the hob only gets warm from the pan.</figcaption></figure>

```pysahdy
On an induction hob the glass plate is not hot until a pan has heated up on it. Why are no eddy currents induced in the glass?
---
Glass does not conduct electricity, so the changing magnetic field cannot drive a current in it. The glass only warms up when the hot pan heats it.
```

### Why the pan must be steel or cast iron
Ordinary household induction hobs are designed for pans whose base contains a ferromagnetic substance, such as steel or cast iron. The principle of induction heating does not physically require ferromagnetism, however: other conductors also heat up if the device is designed for them. A ferromagnetic base strengthens the field of the coil and gathers the flux into itself (chapter *Magnets, the magnetic dipole and the magnetic field*). In addition, steel conducts electricity worse than aluminium, and the eddy currents flow in it only in a thin surface layer with a large resistance, so with the same current in the coil the internal energy of the base grows quickly.

Aluminium and copper are not ferromagnetic, and they conduct electricity extremely well. In them the eddy currents spread over a thicker region, the resistance stays small and there is little heating. An ordinary induction hob therefore usually does not heat an aluminium pan: it detects an unsuitable pan and does not start. Many pans have a steel plate under the base for just this reason.

### The fibre link: light travels in glass
In a fibre link the transmitter changes the information into pulses of infrared light, which travel in the core of a fibre as thick as a hair by total internal reflection. The refractive index of the core is slightly larger than that of the cladding, and light travelling almost along the axis meets the wall of the core at an angle of incidence larger than the critical angle. In glass with a refractive index of $1.47$ light travels at the speed $v = c : n$, so every kilometre delays the signal by about $4.9\,\mu\text{s}$. Total internal reflection does not waste light, but the glass itself attenuates it: some of the light is absorbed and some is scattered sideways by small variations in the density of the glass. The attenuation of silica glass is smallest at a wavelength of about $1550\,\text{nm}$, so long links use it.

### Attenuation limits the length of a link
According to the manufacturer, the attenuation of a common telecommunications fibre is at most $0.18\,\text{dB/km}$ at a wavelength of $1550\,\text{nm}$ and $0.32\,\text{dB/km}$ at a wavelength of $1310\,\text{nm}$ (Corning, product information sheet of the SMF-28 Ultra fibre, 2016). The decibel is familiar from the chapter *Intensity and the decibel scale* (FY5): every $10\,\text{dB}$ means that the power falls to a tenth, and about $3\,\text{dB}$ halves the power. At a wavelength of $1550\,\text{nm}$ the power therefore halves over about $17\,\text{km}$, and after $100\,\text{km}$ less than $2\,\%$ of it is left. The receiver detects pulses even in very weak light, but on long links the light has to be amplified with an optical amplifier about every $50$–$100\,\text{km}$.

## Formula: Attenuation in decibels
When the power of light is $P_0$ at the start of a fibre and $P$ at the end, the **attenuation** of the fibre in decibels is
```latex
\begin{aligned}
&A = 10\,\text{dB} \cdot \lg \frac{P_0}{P} \\[6pt]
&A = aL
\end{aligned}
```
where $A$ is the attenuation ($\text{dB}$), $\lg$ the base-ten logarithm, $a$ the attenuation coefficient of the fibre ($\text{dB/km}$) and $L$ the length of the fibre ($\text{km}$). The formula $A = aL$ holds when the fibre is uniform along its whole length. The attenuations of successive sections in decibels are added, and the ratios of their powers are multiplied: two successive $10\,\text{dB}$ sections attenuate by $20\,\text{dB}$, and the power falls to a tenth of a tenth, that is a hundredth. Splices and sharp bends add to the attenuation, and they are added in the same way. The graph shows that the power falls in the same proportion on every kilometre: the curves are not straight but flatten out.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the power of light passing through an optical fibre as a percentage of the transmitted power, as a function of the length of the fibre over 0–25 kilometres. The solid curve is for a wavelength of 1550 nm with an attenuation of 0.18 dB/km: over 25 kilometres the power falls to 35 per cent. The dashed curve is for a wavelength of 1310 nm with an attenuation of 0.32 dB/km: the power falls to 16 per cent. Dashed lines mark that the power of 1550 nanometre light halves over a distance of 16.7 kilometres." style="max-width:100%;font-size:24px">
  <line x1="163" y1="286" x2="163" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="229.5" y1="286" x2="229.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296.5" y1="286" x2="296.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="286" x2="363" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="286" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="242" x2="430" y2="242" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="198" x2="430" y2="198" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="154" x2="430" y2="154" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="110" x2="430" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="66" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="444" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,286 L443,292 L443,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,40 L102,53 L90,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="163" y1="286" x2="163" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="229.5" y1="286" x2="229.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="213" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="296.5" y1="286" x2="296.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="280" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="363" y1="286" x2="363" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="430" y1="286" x2="430" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="413.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="89" y1="242" x2="96" y2="242" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="198" x2="96" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="183.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="154" x2="96" y2="154" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="89" y1="110" x2="96" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="89" y1="66" x2="96" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="51.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="66" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="271.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{km})$</div></foreignObject>
  <foreignObject x="86" y="9.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P : P_0\ (\%)$</div></foreignObject>
  <polyline points="96,66 99,68 101.5,70 104.5,71.5 107,73.5 110,75.5 112.5,77 115.5,79 118.5,80.5 121,82.5 124,84 126.5,86 129.5,87.5 132,89.5 135,91 138,92.5 140.5,94.5 143.5,96 146,97.5 149,99.5 151.5,101 154.5,102.5 157,104 160,105.5 163,107 165.5,108.5 168.5,110 171,112 174,113 176.5,114.5 179.5,116 182.5,117.5 185,119 188,120.5 190.5,122 193.5,123.5 196,125 199,126 202,127.5 204.5,129 207.5,130.5 210,131.5 213,133 215.5,134 218.5,135.5 221,137 224,138 227,139.5 229.5,140.5 232.5,142 235,143 238,144.5 240.5,145.5 243.5,147 246.5,148 249,149 252,150.5 254.5,151.5 257.5,152.5 260,154 263,155 266,156 268.5,157 271.5,158.5 274,159.5 277,160.5 279.5,161.5 282.5,162.5 285.5,163.5 288,165 291,166 293.5,167 296.5,168 299,169 302,170 305,171 307.5,172 310.5,173 313,174 316,175 318.5,175.5 321.5,176.5 324,177.5 327,178.5 330,179.5 332.5,180.5 335.5,181.5 338,182 341,183 343.5,184 346.5,185 349.5,185.5 352,186.5 355,187.5 357.5,188.5 360.5,189 363,190 366,191 369,191.5 371.5,192.5 374.5,193 377,194 380,195 382.5,195.5 385.5,196.5 388,197 391,198 394,198.5 396.5,199.5 399.5,200 402,201 405,201.5 407.5,202.5 410.5,203 413.5,204 416,204.5 419,205 421.5,206 424.5,206.5 427,207.5 430,208" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,66 99,69.5 101.5,72.5 104.5,76 107,79 110,82.5 112.5,85.5 115.5,88.5 118.5,91.5 121,94.5 124,97.5 126.5,100 129.5,103 132,106 135,108.5 138,111 140.5,114 143.5,116.5 146,119 149,121.5 151.5,124 154.5,126.5 157,129 160,131.5 163,134 165.5,136 168.5,138.5 171,140.5 174,143 176.5,145 179.5,147 182.5,149.5 185,151.5 188,153.5 190.5,155.5 193.5,157.5 196,159.5 199,161.5 202,163 204.5,165 207.5,167 210,169 213,170.5 215.5,172.5 218.5,174 221,175.5 224,177.5 227,179 229.5,180.5 232.5,182.5 235,184 238,185.5 240.5,187 243.5,188.5 246.5,190 249,191.5 252,193 254.5,194.5 257.5,195.5 260,197 263,198.5 266,200 268.5,201 271.5,202.5 274,203.5 277,205 279.5,206 282.5,207.5 285.5,208.5 288,209.5 291,211 293.5,212 296.5,213 299,214.5 302,215.5 305,216.5 307.5,217.5 310.5,218.5 313,219.5 316,220.5 318.5,221.5 321.5,222.5 324,223.5 327,224.5 330,225.5 332.5,226.5 335.5,227 338,228 341,229 343.5,230 346.5,230.5 349.5,231.5 352,232.5 355,233 357.5,234 360.5,235 363,235.5 366,236.5 369,237 371.5,238 374.5,238.5 377,239.5 380,240 382.5,240.5 385.5,241.5 388,242 391,243 394,243.5 396.5,244 399.5,244.5 402,245.5 405,246 407.5,246.5 410.5,247 413.5,248 416,248.5 419,249 421.5,249.5 424.5,250 427,250.5 430,251" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <line x1="319.5" y1="176" x2="319.5" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="176" x2="319.5" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="319.5" cy="176" r="6.5" fill="#e64980" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="329.5" y="139.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$16.7\,\text{km}$</span></div></foreignObject>
  <foreignObject x="440" y="193.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$1550\,\text{nm}$</div></foreignObject>
  <foreignObject x="440" y="230.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$1310\,\text{nm}$</div></foreignObject>
</svg>

```pysahdy
The attenuation coefficient of a fibre is $0.18\,\text{dB/km}$ and the fibre is $50\,\text{km}$ long. What is the attenuation in decibels, and what fraction of the power is left?
---
The attenuation is $A = aL = 0.18\,\text{dB/km}\cdot 50\,\text{km} = 9.0\,\text{dB}$. From the definition of attenuation, $\lg (P_0 : P) = A : 10\,\text{dB} = 0.90$, so $P_0 : P = 10^{0.90} \approx 7.9$. The power ratio is therefore $P/P_0 \approx 0.13$, so about $13\,\%$ of the power is left.
```

### Voltage of a wireless charger
When the flux through one turn of the receiver coil varies sinusoidally with the peak value $\Phi_0$ and the frequency $f$, an alternating voltage is produced in the coil, and its peak value is found in the same way as in a generator (chapter *The generator and alternating current*):
```latex
e_0 = N \cdot 2\pi f \cdot \Phi_0
```
where $e_0$ is the peak value of the voltage ($\text{V}$), $N$ the number of turns of the receiver coil, $f$ the frequency ($\text{Hz}$) and $\Phi_0$ the peak value of the flux through one turn ($\text{Wb}$). A high frequency makes the change of flux fast, so even a small flux is enough. As the distance grows, $\Phi_0$ and with it $e_0$ fall steeply.

## Worked example
A fibre link is $80\,\text{km}$ long, and the attenuation coefficient of the fibre is $0.20\,\text{dB/km}$. The transmitter feeds light of power $2.0\,\text{mW}$ into the fibre. How large is the power that reaches the receiver? Ignore the attenuation of the splices.

<!-- vaihe -->

**Given and find.** The length of the fibre is $L = 80\,\text{km}$, the attenuation coefficient is $a = 0.20\,\text{dB/km}$ and the transmitted power is $P_0 = 2.0\,\text{mW}$. We are asked for the power $P$ that reaches the receiver.

<!-- vaihe -->

**Principle.** The fibre is uniform along its whole length, so the attenuation is the attenuation coefficient times the length. The ratio of the powers is solved from the definition of attenuation, and from it the power that arrives.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&A = aL \\[6pt]
&\lg \frac{P_0}{P} = \frac{A}{10\,\text{dB}} \\[6pt]
&P = P_0 \cdot 10^{-\frac{A}{10\,\text{dB}}}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the kilometres cancel in the product $aL$, and the power comes out in the same unit as $P_0$. Finally $1\,\text{mW} = 1000\,\mu\text{W}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&A = aL \\
&= 0.20\,\tfrac{\text{dB}}{\text{km}} \cdot 80\,\text{km} \\
&= 16\,\text{dB} \\[6pt]
&P = P_0 \cdot 10^{-\frac{A}{10\,\text{dB}}} \\
&= 2.0\,\text{mW} \cdot 10^{-\frac{16\,\text{dB}}{10\,\text{dB}}} \\
&= 2.0\,\text{mW} \cdot 10^{-1.6} \\
&= 0.0502\,\text{mW}
\end{aligned}
```

<!-- vaihe -->

**Result.** The power that reaches the receiver is $P \approx 0.050\,\text{mW} = 50\,\mu\text{W}$, to two significant figures like the transmitted power $2.0\,\text{mW}$ and the attenuation coefficient.

<!-- vaihe -->

**Reasonableness.** Ten decibels reduce the power to a tenth and twenty to a hundredth, so after $16\,\text{dB}$ the power lies between those, about $2.5\,\%$. Of the power $2.0\,\text{mW}$, $2.5\,\%$ is $0.050\,\text{mW}$, as in the result.

## Common misconception
Many people think that a wireless charger sends energy far into the room like radio waves, and that a phone could be charged anywhere near the charger. The magnetic field of the charger, however, weakens steeply already over a few centimetres, and energy is transferred only when the receiver coil is in the field right next to the transmitter. Another common mistake is to think that an induction hob heats the glass top, which then warms the pan. The eddy currents convert electrical energy into internal energy of the base of the pan, and the glass warms up only because heat is transferred to it from the hot pan. The third mistake concerns decibels: doubling the attenuation in decibels does not halve the power but raises the ratio of the powers to the second power. $20\,\text{dB}$ leaves $1\,\%$ of the power, not $5\,\%$.

## Summary
- A wireless charger is a transformer without an iron core: the flux of the alternating current in the transmitter coil induces a voltage $e_0 = N \cdot 2\pi f \cdot \Phi_0$ in the receiver coil. The flux and the voltage fall steeply when the distance between the coils grows or when they move sideways.
- In wireless charging part of the energy changes into internal energy of the coils: in one device comparison, charging took about $47\,\%$ more energy than with a cable, but the difference depends on the devices and the alignment of the coils.
- In an induction hob the changing field of the coil produces eddy currents in the base of the pan, and they heat the base. A ferromagnetic steel base gets hot well, aluminium and copper poorly, and glass, which does not conduct electricity, not at all.
- In an optical fibre light stays in the core by total internal reflection, but the glass attenuates it: $A = aL$ and $A = 10\,\text{dB} \cdot \lg (P_0 : P)$. Every $10\,\text{dB}$ reduces the power to a tenth.
