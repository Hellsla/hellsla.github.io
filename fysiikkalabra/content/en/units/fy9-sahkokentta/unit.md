# Electric field and the capacitor

> **Why** does the spark that jumps from a door handle on a frosty day do no harm, although its voltage is thousands of volts?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter evening in a hallway. In the middle there is a wooden front door with a brass handle on a long metal plate. From the right a hand in a red knitted sleeve reaches towards the handle, and a small bright spark flashes between the fingertip and the metal plate. On the floor there is a striped woollen rug. On the left there is a window showing a snowy night, the moon and spruces, and a radiator under the window. A woolly hat hangs on the coat rack on the wall." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sahkokentta-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

The tasks of the lesson start from the same idea: **a charge creates an electric field around itself, and the field exerts a force on another charge**, $\overline{F} = q\overline{E}$. On a positive charge the force points in the direction of the field and on a negative charge against the field. When the field moves a charge, it does work, and the potential energy of the charge changes like the gravitational potential energy of a ball in the gravitational field. A capacitor stores energy in the field between its plates. Semiconductor components and electrical safety return to the same quantities: voltage, current and the field a dielectric can withstand.

```pysahdy
In which direction does the electric force act on an electron when the field points to the right?
---
The electron's charge is negative, so the force points against the field, that is, to the left.
```

<svg data-fig="kartta" viewBox="0 0 380 780" role="img" aria-label="Recognition chart: how do I tell which law to use? Draw the situation first and see which sign in the task fits. Two charged bodies: the Coulomb force is the Coulomb constant times the product of the charges divided by the square of the distance. A charge in an electric field: the field strength is the force divided by the charge. Uniform field between plates: the voltage is the field strength times the distance. A charge accelerated by a voltage: the work of the field, charge times voltage, equals the kinetic energy. Charge of a capacitor: the charge is the capacitance times the voltage. Dimensions of a plate capacitor: the capacitance is the permittivity of vacuum times the relative permittivity times the area divided by the plate separation. Energy of a capacitor: half of the capacitance times the square of the voltage. An LED needs a series resistor: apply Kirchhoff&#x27;s second law to the loop, the sum of the voltages is zero." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{draw the situation first, then the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{two charged bodies}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{force}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_E = kQ_1Q_2/r^2$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a charge in an electric field}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{field strength}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = F_E/Q$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{uniform field between plates}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{voltage and distance}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$U = Ed$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a charge accelerated by a voltage}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{work and energy}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$QU = \tfrac12 mv^2$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{charge of a capacitor}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{capacitance}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = CU$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{dimensions of a plate capacitor}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{capacitance}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$C = \varepsilon_0\varepsilon_\text{r}A/d$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{energy of a capacitor}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{stored energy}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = \tfrac12 CU^2$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{an LED needs a series resistor}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{loop}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\Delta V = 0$</div></foreignObject>
</svg>

The spark of the opening is solved with these laws. When you walk on a woollen rug, charge builds up on your body, and because of induction a charge of opposite sign moves to the nearby surface of the metal plate of the handle. The spark jumps when the field in the air gap exceeds the dielectric strength of air, about $3\,\text{MV/m}$. A spark of about $3\,\text{mm}$ therefore tells of a voltage of about $9\,\text{kV}$.

```pysahdy
What voltage is across a spark of about $2\,\text{mm}$, when the dielectric strength of air is $3\,\text{MV/m}$?
---
The voltage is $U = Ed \approx 3\,\text{MV/m} \cdot 2\,\text{mm} = 6\,\text{kV}$.
```

The voltage is large, but the body is a small capacitor with a capacitance of about $100\,\text{pF}$, so the charge is only about $0.9\,\mu\text{C}$ and the energy about $4\,\text{mJ}$. The discharge lasts about a microsecond. A dangerous current, about $50\,\text{mA}$ for one second, would carry $0.05\,\text{C}$ through the body, over $50\,000$ times more charge.

<svg data-fig="kipina" viewBox="0 0 600 540" role="img" aria-label="Schematic, not to scale. On the left a fingertip with negative charges on its surface. On the right the metal plate of the door handle, where positive charges have moved to the surface facing the finger because of induction. Between them there is an air gap of about 3 millimetres, crossed by green field lines from the plate to the finger and a bright bluish-white spark; the field is about 3 MV/m, the dielectric strength of air. Below, the calculation: the voltage U = E times d is about 9 kV, the body is a capacitor with a capacitance of about 100 pF, so the charge Q = C U is about 0.9 microcoulombs and the energy W = one half C U squared about 4 millijoules." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sahkokentta-kipina.webp" x="0" y="0" width="600" height="541.2" preserveAspectRatio="none"/>
  <foreignObject x="322" y="29" width="40" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="261" y="261" width="160" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$d \approx 3\,\text{mm}$</div></foreignObject>
  <foreignObject x="62.5" y="223" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{finger}$</div></foreignObject>
  <foreignObject x="457.5" y="253" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{handle}$</div></foreignObject>
  <foreignObject x="14" y="319.5" width="379" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$U = Ed \approx 3\,\text{MV/m} \cdot 3\,\text{mm} \approx 9\,\text{kV}$</div></foreignObject>
  <foreignObject x="14" y="381.5" width="397" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$Q = CU \approx 100\,\text{pF} \cdot 9\,\text{kV} \approx 0.9\,\mu\text{C}$</div></foreignObject>
  <foreignObject x="14" y="443" width="238" height="82" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$W = \dfrac12 CU^2 \approx 4\,\text{mJ}$</div></foreignObject>
</svg>

## Formula: Electric field and the capacitor

### Charge, force and field

```kaavat
Q = ne
magnitude of the Coulomb force :: F_E = k\,\frac{Q_1 Q_2}{r^2}
electric field strength :: E = \frac{F_E}{Q}
voltage in a uniform electric field :: U = Ed
```

where $n$ is the number of elementary charges, $e = 1.602 \cdot 10^{-19}\,\text{C}$ the elementary charge, $F_E$ the magnitude of the electric force ($\text{N}$), $Q_1$ and $Q_2$ the magnitudes of the charges ($\text{C}$), $r$ their distance ($\text{m}$), $k = 8.988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2}$, $E$ the electric field strength ($\text{N/C} = \text{V/m}$) at the charge $Q$, $U$ the voltage between the plates ($\text{V}$) and $d$ the distance between the plates ($\text{m}$). The force on a positive charge is along the field, on a negative one opposite to it; as vectors $\overline{F}_E = Q\overline{E}$. Charge is conserved. Coulomb's law holds for point charges and uniformly charged spheres, and the forces of several charges are added as vectors. The relation $U = Ed$ holds only between large parallel plates, where the field is uniform.

<svg data-fig="levyt" viewBox="0 0 600 440" role="img" aria-label="Schematic: two horizontal plates. The upper plate is positive and its potential is 200 V; the lower, negative plate is the zero, 0 V. Between the plates there are five green vertical field lines pointing down: the field is uniform. Grey dashed lines are the equipotential surfaces 150 V, 100 V and 50 V. On the left a proton, whose red force arrow points down in the direction of the field. On the right an electron, whose red force arrow points up against the field, towards the higher potential." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sahkokentta-levyt.webp" x="0" y="0" width="600" height="447.5" preserveAspectRatio="none"/>
  <foreignObject x="34" y="124.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$150\,\text{V}$</div></foreignObject>
  <foreignObject x="34" y="194.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$100\,\text{V}$</div></foreignObject>
  <foreignObject x="48" y="264.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$50\,\text{V}$</div></foreignObject>
  <foreignObject x="34" y="45.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$200\,\text{V}$</div></foreignObject>
  <foreignObject x="61" y="343.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="524" y="285.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="230" y="245.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = e\overline{E}$</span></div></foreignObject>
  <foreignObject x="486" y="157.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = -e\overline{E}$</span></div></foreignObject>
  <foreignObject x="170.5" y="391.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{proton}$</div></foreignObject>
  <foreignObject x="414" y="391.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{electron}$</div></foreignObject>
</svg>

### Potential and energy

```kaavat
electric potential :: V = \frac{E_\text{p}}{Q}
work done by an electric field :: W = QU
```

where $V$ is the potential at a point ($\text{V}$) relative to a chosen zero, $E_\text{p}$ the electric potential energy of the charge $Q$ ($\text{J}$), $W$ the work done by the field ($\text{J}$) when the charge $Q$ moves from the point A to the point B, and $U = U_{AB} = V_A - V_B$ the voltage between the points. The work does not depend on the path. The field points from higher potential to lower, and a charge starting from rest moves in the direction in which its potential energy decreases. The energy unit $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.

When a particle of mass $m$ ($\text{kg}$) and charge $Q$ starts from rest and is accelerated in an electric field through the voltage $U$, the work done by the field turns into the kinetic energy of the particle. Its final speed is $v$ ($\text{m/s}$).

```johda
A particle (mass $m$, charge $Q$) starts from rest and is accelerated in an electric field between two points with the voltage $U$ between them. Only the electric force does work. Derive an equation for the final speed $v$ of the particle.
---
By the work-energy principle of mechanics, the work done on the particle changes its kinetic energy. Only the electric force does work, and the particle starts from rest, so its initial kinetic energy is zero:

$$W = E_\text{k} - 0 = \tfrac12 mv^2$$

The work done by an electric field is $W = QU$. A charge starting from rest always moves in the direction in which the field does positive work, so the magnitude of the work is $\lvert Q \rvert U$, where $U$ is the magnitude of the voltage:

$$\tfrac12 mv^2 = \lvert Q \rvert U$$

Solve for the speed:

$$v = \sqrt{\frac{2\lvert Q \rvert U}{m}}$$

For example, an elementary charge accelerated through $1\,\text{V}$ gains the kinetic energy $1\,\text{eV}$.
```

### The capacitor

```kaavat
capacitor law :: Q = CU
capacitance of a parallel-plate capacitor :: C = \varepsilon_0\varepsilon_\text{r}\,\frac{A}{d}
energy of a capacitor :: W = \tfrac12 CU^2
```

where $C$ is the capacitance ($\text{F}$), $A$ the area of a plate ($\text{m}^2$), $\varepsilon_0 = 8.854 \cdot 10^{-12}\,\text{F/m}$, $\varepsilon_\text{r}$ the relative permittivity of the dielectric, $W$ the energy stored in the capacitor ($\text{J}$), also $W = \tfrac12 QU$. The formula of the parallel-plate capacitor holds when $d$ is small compared with the size of the plates and the dielectric fills the gap. For a capacitor connected to a source the voltage stays the same; for a disconnected one, the charge.

```pysahdy
What happens to the capacitance of a parallel-plate capacitor when the distance between the plates is doubled and everything else stays the same?
---
By $C = \varepsilon_0\varepsilon_\text{r}A/d$ the capacitance is inversely proportional to the distance $d$, so it halves.
```

The dielectric strength $E_\text{max}$ ($\text{V/m}$) of a dielectric is the largest electric field strength it can withstand. If the field grows larger, the dielectric starts to conduct and breakdown occurs between the plates, so the voltage of the capacitor has a largest value $U_\text{max}$ ($\text{V}$).

```johda
The plates of a parallel-plate capacitor are a distance $d$ apart, and the dielectric filling the gap has the dielectric strength $E_\text{max}$. Derive the largest voltage $U_\text{max}$ the capacitor can withstand.
---
Between the plates the field is uniform, so the voltage in a uniform electric field is

$$U = Ed$$

When the voltage grows, the field grows in the same proportion. Breakdown occurs when the field reaches the dielectric strength, $E = E_\text{max}$:

$$U_\text{max} = E_\text{max}d$$

The same reasoning gives the voltage of the spark at the start: across an air gap $d$ the voltage can be at most the one at which the field equals the dielectric strength of air.
```

### Components and safety

```kaavat
+ \eta = \frac{P}{GA}
voltage drop across a conductor :: U = RI
```

where $\eta$ is the efficiency of the solar cell, $P$ the electric power of the cell at the maximum power point ($\text{W}$), $G$ the intensity of the light falling on the cell, that is the power per unit area ($\text{W/m}^2$), and $A$ the area of the cell ($\text{m}^2$). The equation for the efficiency holds when the light falls perpendicular to the cell. The equation is extra information: it is not in the MAFY tables, and an exam gives it in the task when it is needed.

In the equation for the voltage drop $U$ is the voltage ($\text{V}$), $R$ the resistance ($\Omega$) and $I$ the current ($\text{A}$). The equation gives the current through the body, $I = \tfrac{U}{R}$, when $U$ is the touch voltage and $R$ the resistance of the whole current path. A diode conducts only in the forward direction, when its voltage exceeds the threshold voltage. A fuse protects the cable, a residual current device the person.

An LED is connected to a voltage source $U$ ($\text{V}$) in series with a series resistor $R$ ($\Omega$), which limits the current $I$ ($\text{A}$) to a suitable value. The voltage $U_\text{D}$ ($\text{V}$) of a conducting LED stays almost the same whatever the current.

<svg data-fig="etuvastus" viewBox="0 0 600 300" role="img" aria-label="Circuit diagram, no numbers. On the left a voltage source with the voltage U, its positive terminal at the top. A series resistor R is connected in the upper wire. On the right an LED in the forward direction: its triangle points down, from the positive side towards the negative side, and two small arrows of light leave it. The voltage of the LED is U D. A violet current I flows from the positive terminal through the resistor and the LED back to the negative terminal." style="max-width:100%;font-size:24px">
  <polyline points="140,152 140,70 250,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="330,70 440,70 440,142" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="440,176 440,250 140,250 140,168" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="114" y1="152" x2="166" y2="152" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="127" y1="168" x2="153" y2="168" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="174" y="123" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="86" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <rect x="250" y="58" width="80" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="280" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <path d="M422,142 L458,142 L440,174 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="420" y1="176" x2="460" y2="176" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="464" y1="156" x2="483.5" y2="136.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M490,130 L486,140.5 L479.5,134 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="468" y1="170" x2="487.5" y2="150.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M494,144 L490,154.5 L483.5,148 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="170" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{LED}$</div></foreignObject>
  <line x1="400" y1="186" x2="400" y2="143" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M400,132 L405.5,144 L394.5,144 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="355" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$U_\text{D}$</div></foreignObject>
  <path d="M225,70 L205,62 L205,78 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M280,250 L300,242 L300,258 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="205" y="29.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

```johda
An LED and a series resistor are connected in series to a voltage source $U$. The voltage of the LED is $U_\text{D}$, and the current in the circuit is to be $I$. Derive the resistance $R$ of the series resistor.
---
Go once round the circuit in the direction of the current using Kirchhoff's second law. The potential rises by $U$ in the source. It falls by the voltage drop $RI$ in the resistor (voltage drop across a conductor) and by $U_\text{D}$ in the LED:

$$U - RI - U_\text{D} = 0$$

Solve for the resistance:

$$R = \frac{U - U_\text{D}}{I}$$

Across the resistor there is therefore only the part of the source voltage that is not across the LED. The internal resistance of the source is assumed to be small.
```

## Common mistakes {Virheet}

- **The field and the force always in the same direction.** On a negative charge, such as an electron, the force points against the field.
- **Distance without the square.** In Coulomb's law twice the distance gives a quarter of the force.
- **The field increases when approaching a plate.** Between the plates the field is uniform: the force is the same everywhere.
- **Energy $QU$.** The capacitor stores $\tfrac12 QU$; the other half turns into internal energy of the conductors during charging.
- **A dielectric in a disconnected capacitor.** The charge stays the same, so the voltage and the energy decrease, not increase.
- **The series resistor without the voltage of the LED.** Across the resistor there is only $U - U_\text{D}$.
- **A high voltage is always dangerous.** The danger comes from a current through the body, driven by the voltage between two points.

## Review if needed {Kertaa}

- Charge and Coulomb's law: [*Electric charge and Coulomb's law*](fy6-10.html). The field and plates: [*Uniform electric field*](fy6-11.html).
- Potential, work and the electronvolt: [*Potential energy and potential in an electric field*](fy6-12.html). Capacitance and energy: [*The capacitor and its energy*](fy6-13.html).
- The diode, the LED and the solar cell: [*Semiconductors, the diode, the LED and the solar cell*](fy6-14.html).
- The fuse, earthing and the residual current device: [*Electrical safety at home and at work*](fy6-15.html). Charging and three-phase electricity: [*Applied chapter: the electric car and the home electrical system*](fy6-16.html).
