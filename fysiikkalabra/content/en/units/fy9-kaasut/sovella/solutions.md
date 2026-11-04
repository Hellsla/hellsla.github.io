## fy9-kaasut-s1

### a)
**Given:** diameter of the piston $d = 0.200\,\text{m}$, mass of the car and the platform $m = 1800\,\text{kg}$, pressure of the outside air $p_0 = 101\,\text{kPa}$, lift at a constant speed; $g = 9.81\,\text{m/s}^2$
**Find:** the gauge pressure $\Delta p$ in the cylinder, that is, the pressure difference between the air in the cylinder and the outside air, in kilopascals
**Principle:** The platform moves at a constant speed, so the forces acting on it are in balance (chapter *Newton's second law*). From below the piston the air in the cylinder pushes the piston up with the force $pA$, and from above the outside air pushes it down with the force $p_0A$. Their difference $\Delta p\,A$ supports the weight $mg$. The force of pressure is perpendicular to the surface of the piston, that is, vertical (chapter *Pressure and hydrostatic pressure*).
**Formula:** $\Delta p\,A = mg$ and $A = \pi r^2 = \pi \left(\dfrac{d}{2}\right)^2$, so $\Delta p = \dfrac{mg}{\pi (d/2)^2}$
**Conversions:** Radius $r = 0.200\,\text{m} : 2 = 0.100\,\text{m}$. At the end $1\,\text{Pa} = 0.001\,\text{kPa}$.
**Substitution:** $A = \pi \cdot (0.100\,\text{m})^2 = 0.031\,42\,\text{m}^2$, $mg = 1800\,\text{kg} \cdot 9.81\,\text{m/s}^2 = 17\,658\,\text{N}$ and $\Delta p = \dfrac{17\,658\,\text{N}}{0.031\,42\,\text{m}^2} = 562\,100\,\text{Pa} = 562\,\text{kPa}$
**Answer:** $\Delta p \approx 562\,\text{kPa}$, three significant figures like the diameter $0.200\,\text{m}$.
**Reasonableness:** The gauge pressure is smaller than the tank's $900\,\text{kPa}$, so the air in the tank is able to push the piston. Order of magnitude: $18\,\text{kN}$ on an area of about $0.03\,\text{m}^2$ is about $600\,\text{kPa}$.

### b)
**Given:** $m = 1800\,\text{kg}$, lifting height $h = 1.20\,\text{m}$, from part a $\Delta p = 562.1\,\text{kPa}$ and $A = 0.031\,42\,\text{m}^2$, pressure of the outside air $p_0 = 101\,\text{kPa}$
**Find:** the work $W$ done by the lift on the car and the platform in kilojoules, the same work from the pressure difference, and why the air does more work
**Principle:** The platform rises at a constant speed, so the piston does lifting work on it, which is the force times the distance (chapter *Work and energy*). The force is $\Delta p\,A$, and $Ah$ is the change in volume of the air in the cylinder, so the same work is $\Delta p\,\Delta V$. The air in the cylinder itself pushes the piston with the total pressure, and its work is $p\,\Delta V$ (chapter *Work done by a gas and the heat engine*).
**Formula:** $W = mgh$ and $W = \Delta p\,A h = \Delta p\,\Delta V$; the work of the air $W_\text{g} = (p_0 + \Delta p)\,\Delta V$
**Conversions:** $\Delta V = Ah = 0.031\,42\,\text{m}^2 \cdot 1.20\,\text{m} = 0.037\,70\,\text{m}^3 = 37.7\,\textsf{l}$, and $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$.
**Substitution:** $W = 1800\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 1.20\,\text{m} = 21\,190\,\text{J}$ and $\Delta p\,\Delta V = 562.1\,\text{kPa} \cdot 37.70\,\textsf{l} = 21\,190\,\text{J}$. The work of the air $W_\text{g} = 663.1\,\text{kPa} \cdot 37.70\,\textsf{l} = 25\,000\,\text{J}$, of which $p_0\,\Delta V = 101\,\text{kPa} \cdot 37.70\,\textsf{l} = 3810\,\text{J}$.
**Answer:** $W \approx 21.2\,\text{kJ}$, three significant figures like the lifting height $1.20\,\text{m}$. The air in the cylinder does the work $25.0\,\text{kJ}$, because it pushes the piston with the total pressure. Above the piston there is outside air, and during the lift the piston pushes it out of the way: this takes $3.8\,\text{kJ}$, and only the rest lifts the car.
**Reasonableness:** The two different ways give the same result, because $\Delta p\,A$ is exactly as large as the weight. The result is equal to the increase in the car's potential energy.

### c)
**Given:** volume of the tank $V_\text{s} = 100\,\textsf{l}$, gauge pressure of the tank at first $900\,\text{kPa}$, total pressure in the cylinder during the lift $p_\text{c} = 101\,\text{kPa} + 562\,\text{kPa} = 663\,\text{kPa}$, volume entering the cylinder $\Delta V = 37.7\,\textsf{l}$; constant temperature
**Find:** the reading $\Delta p_2$ of the tank's gauge after one lift, and whether the air is enough for a second lift
**Principle:** No air is lost: the air of the tank is divided between the tank and the cylinder. At constant temperature the product $pV$ of the same amount of air stays the same (chapter *Changes of state of a gas and Boyle's law*), so the $pV$ of the original air in the tank is the sum of the $pV$ of the air left in the tank and of the air moved into the cylinder. The calculations use total pressures. Air flows only from a higher pressure to a lower one, so the lift continues only as long as the pressure in the tank is at least $p_\text{c}$.
**Formula:** $p_1V_\text{s} = p_2V_\text{s} + p_\text{c}\,\Delta V$, so $p_2 = p_1 - \dfrac{p_\text{c}\,\Delta V}{V_\text{s}}$ and $\Delta p_2 = p_2 - p_0$
**Conversions:** The total pressure at first $p_1 = 900\,\text{kPa} + 101\,\text{kPa} = 1001\,\text{kPa}$. The litres cancel.
**Substitution:** $p_2 = 1001\,\text{kPa} - \dfrac{663.1\,\text{kPa} \cdot 37.70\,\textsf{l}}{100\,\textsf{l}} = 1001\,\text{kPa} - 250.0\,\text{kPa} = 751.0\,\text{kPa}$ and $\Delta p_2 = 751.0\,\text{kPa} - 101\,\text{kPa} = 650\,\text{kPa}$. After a second full lift the pressure would be $751.0\,\text{kPa} - 250.0\,\text{kPa} = 501\,\text{kPa}$.
**Answer:** The gauge shows about $650\,\text{kPa}$, three significant figures like the numbers of the tank and the cylinder. The air is not enough for a second lift: the pressure in the tank would fall below the $663\,\text{kPa}$ the cylinder needs once $\dfrac{(751.0 - 663.1)\,\text{kPa} \cdot 100\,\textsf{l}}{663.1\,\text{kPa}} \approx 13.3\,\textsf{l}$ has gone from the tank into the cylinder, that is, when the platform has risen about $13.3\,\textsf{l} : 31.4\,\textsf{l/m} \approx 0.42\,\text{m}$. The platform stops there until the compressor starts. The model assumes a constant temperature. In reality the air leaving the tank cools as it expands, so the pressure is momentarily even lower than calculated and the lift stops earlier.
**Reasonableness:** One lift takes $250\,\text{kPa}$, that is, a quarter, of the tank's pressure, because the $pV$ of the air moved into the cylinder is $663 \cdot 37.7 \approx 25\,000\,\text{kPa}\cdot\textsf{l}$ and the original $pV$ of the tank is about $100\,000\,\text{kPa}\cdot\textsf{l}$.

### Yleisiä virheitä
- In part a the area is calculated from the diameter instead of the radius, so the gauge pressure comes out as a quarter.
- The gauge pressure of part a is substituted into Boyle's law in part c instead of the total pressure, or the tank's gauge reading $900\,\text{kPa}$ is used without the air pressure.
- In part b the work of the air $p\,\Delta V$ is calculated with the total pressure and taken to be the energy received by the car.
- In part c it is forgotten that air does not flow from the tank into the cylinder when the pressure in the tank is lower than in the cylinder.

### Hyväksytään myös
- In part c the calculation can be done with amounts of substance $n = pV/(RT)$; the temperature cancels, and the result is the same.

## fy9-kaasut-s2

### a)
**Given:** volume of methane per hour $V = 52.0\,\text{m}^3$, temperature $\theta = 25\,{}^\circ\text{C}$, pressure $p = 104\,\text{kPa}$, molar mass $M = 16.0\,\text{g/mol}$; $R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$
**Find:** the mass $m$ of methane burnt per hour, in kilograms
**Principle:** At the meter the methane is at ordinary pressure and temperature, so it can be described as an ideal gas. The ideal gas law gives the amount of substance of the gas flowing per hour, and the molar mass gives its mass (chapter *Ideal gas law $pV = nRT$*).
**Formula:** $pV = nRT$ and $n = \dfrac{m}{M}$, so $m = \dfrac{pVM}{RT}$
**Conversions:** $p = 104 \cdot 1000\,\text{Pa} = 104\,000\,\text{Pa}$, $T = (25 + 273.15)\,\text{K} = 298.15\,\text{K}$ and $M = 16.0 \cdot 0.001\,\text{kg/mol} = 0.0160\,\text{kg/mol}$
**Substitution:** $n = \dfrac{104\,000\,\text{Pa} \cdot 52.0\,\text{m}^3}{8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 298.15\,\text{K}} = 2183\,\text{mol}$ and $m = 2183\,\text{mol} \cdot 0.0160\,\tfrac{\text{kg}}{\text{mol}} = 34.9\,\text{kg}$
**Answer:** $m \approx 34.9\,\text{kg}$ per hour, three significant figures like the volume $52.0\,\text{m}^3$ and the molar mass $16.0\,\text{g/mol}$.
**Reasonableness:** The density of methane is $34.9\,\text{kg} : 52.0\,\text{m}^3 \approx 0.67\,\text{kg/m}^3$, smaller than the about $1.2\,\text{kg/m}^3$ of air, as the ratio of the molar masses $16 : 29$ predicts.

### b)
**Given:** from part a $m = 34.92\,\text{kg}$ in the time $t = 1\,\text{h}$, heat of combustion $H = 50.0\,\text{MJ/kg}$, electrical efficiency $\eta_\text{s} = 36\,\%$
**Find:** the electrical power $P_\text{s}$ in kilowatts
**Principle:** The fuel power is the energy released in burning per unit time, and the electrical efficiency tells what share of it is obtained as electricity (chapter *Energy production and the efficiency of power plants*).
**Formula:** $P_0 = \dfrac{Hm}{t}$ and $\eta_\text{s} = \dfrac{P_\text{s}}{P_0}$, so $P_\text{s} = \dfrac{\eta_\text{s} H m}{t}$
**Conversions:** $H = 50.0 \cdot 10^{6}\,\text{J/kg}$, $t = 1\,\text{h} = 3600\,\text{s}$ and $36\,\% = 0.36$
**Substitution:** $Hm = 50.0 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} \cdot 34.92\,\text{kg} = 1.746 \cdot 10^{9}\,\text{J}$, $P_0 = \dfrac{1.746 \cdot 10^{9}\,\text{J}}{3600\,\text{s}} = 485\,100\,\text{W}$ and $P_\text{s} = 0.36 \cdot 485.1\,\text{kW} = 174.6\,\text{kW}$
**Answer:** $P_\text{s} \approx 175\,\text{kW}$, three significant figures like the mass; the efficiency $36\,\%$ is given to two figures, so $170$–$180\,\text{kW}$ is an equally good answer.
**Reasonableness:** The fuel power is about $0.5\,\text{MW}$, and a good third of it is obtained as electricity, as in a small engine power plant. The power would be enough for the electricity consumption of tens of detached houses.

### c)
**Given:** $P_0 = 485.1\,\text{kW}$, $P_\text{s} = 174.6\,\text{kW}$, $75\,\%$ of the heat recovered
**Find:** why not all of the fuel power is obtained as electricity, and the total efficiency $\eta_\text{tot}$
**Principle:** The engine is a heat engine. It can turn heat into work only if it gives part of the heat to a colder environment: with the exhaust gases and the cooling water (chapter *Work done by a gas and the heat engine*). Energy is conserved, so the heat power given away is the difference between the fuel power and the electrical power. In the total efficiency the electricity and the recovered heat are counted as useful.
**Formula:** $P_2 = P_0 - P_\text{s}$, $P_\text{l} = 0.75\,P_2$ and $\eta_\text{tot} = \dfrac{P_\text{s} + P_\text{l}}{P_0}$
**Conversions:** Not needed: the powers are in kilowatts, and $75\,\% = 0.75$.
**Substitution:** $P_2 = 485.1\,\text{kW} - 174.6\,\text{kW} = 310.5\,\text{kW}$, $P_\text{l} = 0.75 \cdot 310.5\,\text{kW} = 232.9\,\text{kW}$ and $\eta_\text{tot} = \dfrac{174.6\,\text{kW} + 232.9\,\text{kW}}{485.1\,\text{kW}} = 0.840$
**Answer:** $\eta_\text{tot} \approx 84\,\%$, two significant figures like the efficiencies $36\,\%$ and $75\,\%$. Even a frictionless engine must give heat to a colder place, so the share of electricity stays well below $100\,\%$. The total efficiency is high because the heat given away is used for heating; it does not increase the electricity obtained.
**Reasonableness:** What goes to waste is $485\,\text{kW} - 175\,\text{kW} - 233\,\text{kW} \approx 78\,\text{kW}$, that is, $16\,\%$, the same as $25\,\%$ of the heat power. The result is of the same order of magnitude as the $85$–$90\,\%$ of combined heat and power plants.

### Yleisiä virheitä
- In part a the temperature is substituted in degrees Celsius, so the amount of substance comes out over ten times too large, $26\,000\,\text{mol}$.
- The molar mass is left in grams, so the mass comes out a thousand times too large.
- In part b the energy released in an hour in megajoules is taken directly as the power without dividing by the seconds.
- In part c the answer is that no more electricity is obtained “because of friction”; removing friction does not remove the heat that a heat engine gives to a colder place.

### Hyväksytään myös
- In part b the electrical power can also be calculated as energy per hour: $0.36 \cdot 1746\,\text{MJ} \approx 629\,\text{MJ}$ per hour, and $629\,\text{MJ} : 3600\,\text{s} \approx 175\,\text{kW}$.

## fy9-kaasut-s3

### a)
**Find:** the volume $V$ of the air as a function of the temperature $\theta$ as a graph, and a model fitted to it
**Graph:** The temperature $\theta\ ({}^\circ\text{C})$ is on the horizontal axis and the volume $V\ (\text{ml})$ on the vertical axis. Here the vertical axis starts at $36\,\text{ml}$ so that the variation of the points can be seen; for the extension in part b a second graph is drawn with the axes starting at zero. Each point has an uncertainty bar of $\pm 0.3\,\text{ml}$.

<svg data-fig="fy9-kaasut-s3-graph" viewBox="0 0 420 360" role="img" aria-label="Graph: the volume V of the air in the syringe as a function of the temperature θ, with θ from 0 to 80 °C. The vertical axis starts at 36 millilitres. Eight black points at the temperatures 5, 15, …, 75 °C, each with a vertical uncertainty bar of ±0.3 ml. A rising straight line is fitted to the points, passing between them. Two points of the line far apart are circled, (0 °C; 37.7 ml) and (80 °C; 48.5 ml), from which the slope is read: about 0.135 ml per degree." style="max-width:100%;font-size:24px">
  <line x1="94" y1="306" x2="94" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="125.5" y1="306" x2="125.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="157" y1="306" x2="157" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="189" y1="306" x2="189" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="221" y1="306" x2="221" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="252.5" y1="306" x2="252.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="284" y1="306" x2="284" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="316" y1="306" x2="316" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="271" x2="316" y2="271" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="236.5" x2="316" y2="236.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="201.5" x2="316" y2="201.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="166.5" x2="316" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="131.5" x2="316" y2="131.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="97" x2="316" y2="97" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="62" x2="316" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="61" y1="306" x2="330" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M342,306 L329,312 L329,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="62" y1="307" x2="62" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M62,36 L68,49 L56,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="94" y1="306" x2="94" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="125.5" y1="306" x2="125.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="157" y1="306" x2="157" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="189" y1="306" x2="189" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="221" y1="306" x2="221" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="252.5" y1="306" x2="252.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="236" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="284" y1="306" x2="284" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="316" y1="306" x2="316" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="299.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="55" y1="271" x2="62" y2="271" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="55" y1="236.5" x2="62" y2="236.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="222" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="55" y1="201.5" x2="62" y2="201.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="55" y1="166.5" x2="62" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="152" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$44$</div></foreignObject>
  <line x1="55" y1="131.5" x2="62" y2="131.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="55" y1="97" x2="62" y2="97" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="82.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="55" y1="62" x2="62" y2="62" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="348" y="291.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="52" y="5.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{ml})$</div></foreignObject>
  <rect x="53" y="290" width="18" height="8" fill="#ffffff"/>
  <line x1="53" y1="293" x2="71" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="53" y1="301" x2="71" y2="295" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <polyline points="62,276 316,88" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="78" y1="273" x2="78" y2="262.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="74" y1="273" x2="82" y2="273" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="74" y1="262.5" x2="82" y2="262.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="78" cy="267.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="109.5" y1="243.5" x2="109.5" y2="233" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="105.5" y1="243.5" x2="113.5" y2="243.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="105.5" y1="233" x2="113.5" y2="233" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="109.5" cy="238" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="141.5" y1="222.5" x2="141.5" y2="212" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="137.5" y1="222.5" x2="145.5" y2="222.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="137.5" y1="212" x2="145.5" y2="212" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="141.5" cy="217" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="173" y1="198" x2="173" y2="187.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="169" y1="198" x2="177" y2="198" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="169" y1="187.5" x2="177" y2="187.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="173" cy="192.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="205" y1="175.5" x2="205" y2="165" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201" y1="175.5" x2="209" y2="175.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201" y1="165" x2="209" y2="165" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="205" cy="170" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="236.5" y1="152.5" x2="236.5" y2="142" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="232.5" y1="152.5" x2="240.5" y2="152.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="232.5" y1="142" x2="240.5" y2="142" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="236.5" cy="147.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="268.5" y1="128" x2="268.5" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="264.5" y1="128" x2="272.5" y2="128" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="264.5" y1="118" x2="272.5" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="268.5" cy="123" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="300" y1="105.5" x2="300" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="296" y1="105.5" x2="304" y2="105.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="296" y1="95" x2="304" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="300" cy="100.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="62" cy="276.5" r="10" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="316" cy="88" r="10" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="71.5" y="96" width="145" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$k \approx 0.135\,\text{ml}/{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="78" y="276" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$(0;\ 37.7)$</div></foreignObject>
  <foreignObject x="176" y="58" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$(80;\ 48.5)$</div></foreignObject>
</svg>

The circled places in the graph are the two points of the line from which the slope of part b is read.

**Model answer:** The points lie almost on a straight line: the volume increases by the same amount for each degree of temperature. One rising straight line is fitted to the points, passing between the points and through each uncertainty bar. The points are not joined into a broken line. In real measurement series the points do not usually lie exactly on the same line because of the measurement uncertainty.

### b)
**Given:** the line of part a and the points read from it; uncertainty of the reading $\pm 0.3\,\text{ml}$
**Find:** the temperature $\theta_0$ at which $V = 0$ according to the line, its uncertainty and a comparison with the value $-273.15\,{}^\circ\text{C}$
**Principle:** At constant pressure the volume of a dilute gas is directly proportional to the kelvin temperature, so the $(\theta, V)$ graph is a straight line whose extension reaches zero at absolute zero (chapter *Changes of state of a gas and Boyle's law*). The line is extended outside the measurement range, that is, extrapolated. The uncertainty is estimated with the steepest and the least steep line that still pass through all the uncertainty bars (chapter *Determining absolute zero*).
**Reading the graph:** Two points far apart are read from the line, not measured points: $(0\,{}^\circ\text{C};\ 37.7\,\text{ml})$ and $(80\,{}^\circ\text{C};\ 48.5\,\text{ml})$. The extreme lines pass through the ends of the bars: the steepest through the points $(15\,{}^\circ\text{C};\ 39.6\,\text{ml})$ and $(75\,{}^\circ\text{C};\ 48.1\,\text{ml})$, the least steep through the points $(5\,{}^\circ\text{C};\ 38.5\,\text{ml})$ and $(75\,{}^\circ\text{C};\ 47.5\,\text{ml})$.

<svg data-fig="fy9-kaasut-s3-extra" viewBox="0 0 420 350" role="img" aria-label="Graph: the same line over the whole range θ = −300…100 °C and V = 0…50 ml. The measured points are only in the range 5–75 °C. The fitted line is extended as a dashed line, and it crosses the temperature axis at about −279 °C. Two grey extreme lines, the steepest and the least steep line that still pass through all the uncertainty bars, cross the axis at about −265 °C and −294 °C. The accepted value −273 °C lies between them." style="max-width:100%;font-size:24px">
  <line x1="88" y1="300" x2="88" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120.5" y1="300" x2="120.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="153" y1="300" x2="153" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="185" y1="300" x2="185" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="217" y1="300" x2="217" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="249.5" y1="300" x2="249.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="282" y1="300" x2="282" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="314" y1="300" x2="314" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="252" x2="314" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="204" x2="314" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="156" x2="314" y2="156" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="108" x2="314" y2="108" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="60" x2="314" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="55" y1="300" x2="328" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M340,300 L327,306 L327,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="56" y1="301" x2="56" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M56,34 L62,47 L50,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="88" y1="300" x2="88" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="120.5" y1="300" x2="120.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="309.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${-}200$</div></foreignObject>
  <line x1="153" y1="300" x2="153" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="185" y1="300" x2="185" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="156" y="309.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${-}100$</div></foreignObject>
  <line x1="217" y1="300" x2="217" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="249.5" y1="300" x2="249.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="239.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="282" y1="300" x2="282" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="314" y1="300" x2="314" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="291.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="49" y1="252" x2="56" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="49" y1="204" x2="56" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="11" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="49" y1="156" x2="56" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="49" y1="108" x2="56" y2="108" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="11" y="93.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="49" y1="60" x2="56" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="46" y="3.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{ml})$</div></foreignObject>
  <line x1="249.5" y1="300" x2="249.5" y2="60" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <polyline points="79,300 301,65.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="4 5"/>
  <polyline points="59.5,300 301,69" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="4 5"/>
  <polyline points="69.5,300 252.5,116" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="252.5,116 298,70.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="252.5" cy="116.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="259" cy="108.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="265.5" cy="102.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="272" cy="96" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="278.5" cy="90" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="285" cy="83.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="291.5" cy="77" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298" cy="70.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="75.5" y1="296" x2="117.5" y2="281" stroke="#e8590c" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="69.5" cy="300" r="6" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="119" y="264" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\theta_0 \approx {-}279\,{}^\circ\text{C}$</span></div></foreignObject>
  <foreignObject x="61" y="69.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{extreme lines:}$</div></foreignObject>
  <foreignObject x="61" y="98.5" width="178" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">${-}265\ \text{and}\ {-}294\,{}^\circ\text{C}$</div></foreignObject>
</svg>

**Formula:** $k = \dfrac{V_2 - V_1}{\theta_2 - \theta_1}$ and $V = V_0 + k\theta$; when $V = 0$, $\theta_0 = -\dfrac{V_0}{k}$, and $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Conversions:** Not needed: the millilitres cancel, and the result comes out in degrees Celsius.
**Substitution:** $k = \dfrac{48.5\,\text{ml} - 37.7\,\text{ml}}{80\,{}^\circ\text{C} - 0\,{}^\circ\text{C}} = 0.135\,\text{ml}/{}^\circ\text{C}$ and $\theta_0 = -\dfrac{37.7\,\text{ml}}{0.135\,\text{ml}/{}^\circ\text{C}} = -279\,{}^\circ\text{C}$. The steepest line: $k = 0.1417\,\text{ml}/{}^\circ\text{C}$, $V_0 = 37.48\,\text{ml}$, $\theta_0 = -264.5\,{}^\circ\text{C}$; the least steep: $k = 0.1286\,\text{ml}/{}^\circ\text{C}$, $V_0 = 37.86\,\text{ml}$, $\theta_0 = -294.4\,{}^\circ\text{C}$. $\Delta\theta_0 = \dfrac{-264.5\,{}^\circ\text{C} - (-294.4\,{}^\circ\text{C})}{2} = 15\,{}^\circ\text{C}$
**Answer:** $\theta_0 \approx (-279 \pm 15)\,{}^\circ\text{C}$. The result is given in whole degrees, because the uncertainty is tens of degrees. The accepted value $-273.15\,{}^\circ\text{C}$ is inside the interval $-294$…$-265\,{}^\circ\text{C}$, so the result agrees with it, and the difference of $6\,\text{K}$ is not significant. The interval is an estimate, not a guaranteed limit: it does not tell whether the relationship stays a straight line outside the measurement range.
**Reasonableness:** The line is extended by about $280\,\text{K}$, almost four times the length of the measurement range of $70\,\text{K}$, so even a small difference in slope grows into tens of degrees in the extension. The least-squares line gives the same: $k = 0.1351\,\text{ml}/{}^\circ\text{C}$ and $\theta_0 = -279\,{}^\circ\text{C}$.

### c)
**Given:** the slope of part b $k = 0.135\,\text{ml}/{}^\circ\text{C}$, pressure $p = 101.3\,\text{kPa}$; $R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$
**Find:** the amount of substance $n$ of the air in the syringe
**Principle:** The amount of air and the pressure stay the same, so by the ideal gas law the volume is directly proportional to the kelvin temperature, and the slope of the line is $nR/p$ (chapter *Ideal gas law $pV = nRT$*). A change of one degree Celsius is the same as a change of one kelvin, so the slope is the same on both scales.
**Reading the graph:** The slope is read from the line of part a as in part b: $k = 10.8\,\text{ml} : 80\,{}^\circ\text{C} = 0.135\,\text{ml}/{}^\circ\text{C}$.
**Formula:** $pV = nRT$, so $V = \dfrac{nR}{p}\,T$ and $k = \dfrac{\Delta V}{\Delta T} = \dfrac{nR}{p}$, from which $n = \dfrac{pk}{R}$
**Conversions:** $k = 0.135\,\text{ml/K} = 0.135 \cdot 10^{-6}\,\text{m}^3/\text{K}$, because $1\,\text{ml} = 10^{-6}\,\text{m}^3$, and $p = 101.3 \cdot 1000\,\text{Pa} = 101\,300\,\text{Pa}$
**Substitution:** $n = \dfrac{101\,300\,\text{Pa} \cdot 0.135 \cdot 10^{-6}\,\text{m}^3/\text{K}}{8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}} = 1.65 \cdot 10^{-3}\,\text{mol}$
**Answer:** $n \approx 1.65\,\text{mmol}$, three significant figures like the slope $0.135\,\text{ml}/{}^\circ\text{C}$.
**Reasonableness:** A single measured point gives almost the same: $n = \dfrac{pV}{RT} = \dfrac{101\,300\,\text{Pa} \cdot 41.1 \cdot 10^{-6}\,\text{m}^3}{8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 298.15\,\text{K}} = 1.68\,\text{mmol}$. The difference arises because the result calculated through the slope does not use the assumption that the line passes through absolute zero. The order of magnitude fits: $40\,\text{ml}$ of air is about $1.7\,\text{mmol}$, since a mole of gas takes up about $24\,\textsf{l}$ at room temperature.

### d)
**Find:** how the $1.5\,\text{ml}$ of air outside the bath changes the line and the estimate of absolute zero, and whether repetitions remove the error
**Principle:** The air in the tube stays at room temperature and at the same pressure, so its volume does not change as the bath warms. The volume recorded by the group is the volume of the air in the bath and the constant volume of the tube together, because they added the tube's $1.5\,\text{ml}$ to every reading. Only the air in the bath follows the law $V \propto T$. A systematic error shifts all results in the same direction, and it cannot be removed by repetition (chapter *Determining absolute zero*).
**Model answer:** The same addition $1.5\,\text{ml}$ is made to every recorded volume, so the line moves upwards but its slope does not change: the slope is set only by the air in the bath. The zero point is then $\theta_0 = -\dfrac{V_0 + 1.5\,\text{ml}}{k}$, that is, the estimate moves colder by about $\dfrac{1.5\,\text{ml}}{0.135\,\text{ml}/{}^\circ\text{C}} \approx 11\,\text{K}$: this group's result would be about $-290\,{}^\circ\text{C}$. The error is systematic, so more repetitions or more measured points do not remove it. The whole amount of air must be kept in the bath, or the constant volume of the tube is left out of the total volume: the amount of substance of the air in the syringe is then still constant, so the scale readings alone follow the law $V \propto T$ and give the correct zero point.

### Yleisiä virheitä
- The points of the graph are joined into a broken line, or the line is forced through the origin even though the horizontal axis is in degrees Celsius.
- The slope is calculated from two adjacent measured points and not from the fitted line.
- In part b the result $-279\,{}^\circ\text{C}$ is considered a failure because it is not $-273\,{}^\circ\text{C}$, or the extrapolation is not mentioned.
- In part c the millilitres are not converted to cubic metres, so the amount of substance comes out a million times too large.
- In part d it is assumed that repetitions remove the error caused by the tube.

### Hyväksytään myös
- The slope $0.132$…$0.138\,\text{ml}/{}^\circ\text{C}$ of a line fitted by eye and the results that follow from it: in part b $-290$…$-268\,{}^\circ\text{C}$, in part c $1.61$…$1.68\,\text{mmol}$.
- In part b an estimate of the uncertainty of $\pm 10$…$\pm 20\,{}^\circ\text{C}$, when it is justified with the extreme lines.

## fy9-kaasut-s4

### a)
**Find:** what in the brochure is true and what is not
**Principle:** The law of conservation of energy allows only changes in which energy is neither created nor lost (chapter *Internal energy, heat and conservation of energy*). A heat engine has a further limit: it can turn heat into work only if it gives part of the heat to a colder environment (chapter *Work done by a gas and the heat engine*).
**Model answer:** The part of the brochure about energy holds: as far as energy goes, the internal energy of the sea could turn into the motion of the ship, and if the sea cools by as much as work is done, energy is conserved. The engine still cannot work. A heat engine does work only when heat flows from hot to colder and part of it is given to a colder environment. The brochure's engine has only one temperature, the sea at $15\,{}^\circ\text{C}$, and nothing colder where the heat could go. Not all heat can be turned into work, however frictionless the machine is. So the brochure's claim that the engine breaks no law of nature is wrong, and the project is not worth funding.

### b)
**Given:** heat power taken from the seawater $P_1 = 500\,\text{kW}$, work power $P_W = 30\,\text{kW}$; sea $3\,{}^\circ\text{C}$, frosty air $-20\,{}^\circ\text{C}$
**Find:** the efficiency $\eta$, the heat power $P_2$ given to the frosty air, and why the efficiency is small
**Principle:** The machine is a heat engine whose hot source is the sea and whose cold environment is the frosty air. Energy is conserved, so the heat of the sea is divided into work and heat given to the cold. The efficiency is the share of work in the heat taken, and it can be calculated from the powers (chapter *Work done by a gas and the heat engine*).
**Formula:** $\eta = \dfrac{P_W}{P_1}$ and $P_1 = P_W + P_2$, so $P_2 = P_1 - P_W$
**Conversions:** Not needed for the calculation. For the comparison, in kelvins the sea is $3 + 273 = 276\,\text{K}$ and the air $253\,\text{K}$.
**Substitution:** $\eta = \dfrac{30\,\text{kW}}{500\,\text{kW}} = 0.060 = 6.0\,\%$ and $P_2 = 500\,\text{kW} - 30\,\text{kW} = 470\,\text{kW}$
**Answer:** $\eta \approx 6.0\,\%$ and $P_2 \approx 470\,\text{kW}$, two significant figures like the work power $30\,\text{kW}$. The efficiency is small because the temperature difference of $23\,\text{K}$ is small compared with the temperature of the hot source, $276\,\text{K}$: the smaller this ratio is, the smaller the share of the heat that can turn into work.
**Reasonableness:** Energy is conserved: $30\,\text{kW} + 470\,\text{kW} = 500\,\text{kW}$. The machine breaks no laws, because it gives almost all the heat to the colder place. The efficiency is much smaller than the about $40\,\%$ of a power plant, where the steam is hundreds of degrees hotter than the condenser.

### c)
**Find:** why a heat pump can heat the cabins with seawater, even though the brochure's engine cannot work
**Principle:** A heat pump works the opposite way to a heat engine: it uses electrical energy and with it moves heat from cold to warm. The heat given indoors is the sum of the heat taken from outside and the electrical energy (chapter *Work done by a gas and the heat engine*).
**Model answer:** A heat pump does not turn heat into work. It moves heat from the cold $3\,{}^\circ\text{C}$ seawater to the warm cabins, and this needs work, here an electrical power of $10\,\text{kW}$. Energy is conserved: the cabins receive the $35\,\text{kW} - 10\,\text{kW} = 25\,\text{kW}$ taken from the seawater and the $10\,\text{kW}$ of electricity, $35\,\text{kW}$ in total. The ratio $35 : 10 = 3.5$ is a coefficient of performance and not an efficiency: it can be over $1$, because most of the heat is moved from the sea and not made from electricity. Nothing is created out of nothing. The difference from the brochure's engine lies in the direction and the price: the heat pump needs external work to move heat from cold to warm, whereas the brochure's engine promises work from the sea without a colder environment.

### Yleisiä virheitä
- In part a it is only stated that “energy is not created out of nothing”, although the brochure does not claim so: the mistake lies in the other limit, the missing colder environment.
- In part b the efficiency is calculated by dividing the work by the heat given to the cold, $30 : 470$, and not by the heat taken.
- In part c the coefficient of performance $3.5$ is called an efficiency of $350\,\%$, and it is concluded that the pump produces energy.

## fy9-kaasut-s5

### a)
**Given:** from the report the mass before $m_1 = 52.36\,\text{g}$ and after $m_2 = 55.64\,\text{g}$, gauge pressure on the pump's gauge $\Delta p = 210\,\text{kPa}$, volume of the bottle $V = 1.5\,\textsf{l}$, temperature $\theta = 21\,{}^\circ\text{C}$; $R = 8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$
**Find:** the molar mass $M$ calculated by the group
**Principle:** In the group's assumption the volume and the temperature of the bottle are the same before and after the pumping. By the ideal gas law the amount of substance is then proportional to the pressure, so the amount of substance of the added air is obtained from the increase in pressure, which is the gauge pressure shown by the gauge (chapter *Ideal gas law $pV = nRT$*). The molar mass is the mass of the added air divided by its amount of substance.
**Formula:** $\Delta n = n_2 - n_1 = \dfrac{(p_0 + \Delta p)V}{RT} - \dfrac{p_0V}{RT} = \dfrac{\Delta p\,V}{RT}$ and $M = \dfrac{m_2 - m_1}{\Delta n}$
**Conversions:** $\Delta p = 210 \cdot 1000\,\text{Pa} = 210\,000\,\text{Pa}$, $V = 1.5 \cdot 0.001\,\text{m}^3 = 0.0015\,\text{m}^3$ and $T = (21 + 273.15)\,\text{K} = 294.15\,\text{K}$
**Substitution:** $\Delta n = \dfrac{210\,000\,\text{Pa} \cdot 0.0015\,\text{m}^3}{8.31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 294.15\,\text{K}} = 0.1289\,\text{mol}$ and $M = \dfrac{55.64\,\text{g} - 52.36\,\text{g}}{0.1289\,\text{mol}} = \dfrac{3.28\,\text{g}}{0.1289\,\text{mol}} = 25.4\,\text{g/mol}$
**Answer:** $M \approx 25\,\text{g/mol}$, two significant figures like the volume $1.5\,\textsf{l}$. The group's number is calculated correctly.
**Reasonableness:** If the molar mass were the table value $29.0\,\text{g/mol}$, $29.0\,\tfrac{\text{g}}{\text{mol}} \cdot 0.1289\,\text{mol} \approx 3.74\,\text{g}$ of air should have entered the bottle. The weighed $3.28\,\text{g}$ is about $12\,\%$ less.

### b)
**Find:** whether the conclusion is justified, the most important sources of error and the direction of their effect
**Principle:** The conclusion is justified only if the difference from the table value is larger than the uncertainty of the result (chapter *Measuring and the reliability of a measurement*). The effect of a source of error is estimated by recalculating the result with a changed value. The molar mass is $\Delta m : \Delta n$, so a $\Delta n$ that is too large or a $\Delta m$ that is too small decreases the result.
**Model answer:** The conclusion is not justified. The result rests on a single measurement, and the most important sources of error push it in the same direction, downwards.
- *Warm air.* The pumped air warms as it is compressed, and the gauge was read immediately. The pressure of warm air is higher than that of the same amount of air at room temperature, so $\Delta n$ was calculated too large and the result too small. If the air was at $30\,{}^\circ\text{C}$, the result would be about $27\,\text{g/mol}$.
- *The pump's gauge.* It measures the pressure in the hose during pumping and is made for rough use. If the real gauge pressure of the bottle was $10\,\text{kPa}$ lower, the result would be $27\,\text{g/mol}$; the error can go in either direction.
- *Escaping air.* When the pump is detached, and through the valve, air escapes before the weighing, so $\Delta m$ is too small and the result too small.
- *The volume of the bottle.* The marking $1.5\,\textsf{l}$ is the volume of the drink. The bottle is slightly larger and bulges under pressure, so the real $\Delta n$ is larger than calculated. This increases the calculated result, so it does not explain the value that is too small.

The resolution of the scale, $0.01\,\text{g}$, is less than $1\,\%$ of the increase in mass $3.28\,\text{g}$, so it is not significant. The errors of the temperature and the gauge are each about $5$–$7\,\%$, so the uncertainty is of the same order of magnitude as the difference from the table value. The measurement does not show the table value to be wrong.

### c)
**Find:** an experimental plan that gives the molar mass of air more reliably
**Principle:** The quantities are measured as directly as possible and at a time when the assumptions hold (the same temperature before and after). The measurement is repeated with several values, and the result is determined from the slope of a graph, so the error of a single measurement weighs less (chapter *Graphing and fitting a straight line*).
**Model answer:**
- *Volume.* The volume of the bottle is measured by filling it with water and weighing the water ($1\,\text{g} \approx 1\,\text{ml}$).
- *Pressure and temperature.* A precise pressure gauge is connected to the bottle, and the gauge pressure is read only when the bottle has stood for a few minutes and the air has cooled to room temperature. The room temperature is measured with a thermometer.
- *Mass.* The bottle is weighed straight after the pressure reading, without touching the valve in between.
- *Repetitions and graph.* The measurement is made at several gauge pressures, for example $50$, $100$, $150$, $200$ and $250\,\text{kPa}$, with the same bottle and valve. The results are presented as a $(\Delta p, \Delta m)$ graph. By the ideal gas law $\Delta m = \dfrac{MV}{RT}\,\Delta p$, so a straight line through the origin is fitted to the points, and the molar mass is obtained from the slope: $M = \dfrac{kRT}{V}$.

If the points lie on a straight line but the line does not pass through the origin, this reveals a systematic error, for example air escaping every time on detaching.

### Yleisiä virheitä
- In part a the amount of substance is calculated with the total pressure $311\,\text{kPa}$ and not with the increase in pressure, so the result is a third.
- In part b it is only stated that “there were measurement errors” without naming the source of error or the direction of its effect.
- In part b the bulging of the bottle is named as the cause of the result being too small, although it acts the opposite way.
- In part c only “more precise instruments” are proposed without telling what is measured and how.

### Hyväksytään myös
- In part b one can also mention that the bulging bottle displaces more air, so the buoyancy increases and the scale shows about $0.06\,\text{g}$ too little (decreases the result slightly), when the reasoning is correct.

## fy9-kaasut-s6

### a)
**Given:** dimensions of the glass pane $2.40\,\text{m}$, $1.20\,\text{m}$ and $10\,\text{mm}$, density $\rho = 2500\,\text{kg/m}^3$, inner diameter of the pad $d = 300\,\text{mm}$, upward acceleration $a = 1.2\,\text{m/s}^2$; $g = 9.81\,\text{m/s}^2$
**Find:** the force diagram of the pane and the minimum partial vacuum $\Delta p$ under the pad, in kilopascals
**Principle:** The outside air presses on the pane from all sides, but under the pad the pressure is lower by $\Delta p$. That is why, at the pad, the force of the outside air on the lower surface of the pane is $\Delta p\,A$ larger than the force of the air on the upper surface, and the net force $F_\text{p} = \Delta p\,A$ points perpendicular to the surface, that is, upwards (chapter *Pressure and hydrostatic pressure*). In addition, the weight and the normal force from the rim of the pad, which presses the pane down, act on the pane. At the minimum partial vacuum the normal force from the rim is zero: the pane is on the verge of coming loose. The pane accelerates upwards, so by Newton's second law the sum of the forces is $ma$ upwards (chapter *Newton's second law*).

<svg data-fig="fy9-kaasut-s6-vaaka" viewBox="0 0 420 270" role="img" aria-label="Force diagram: the horizontal glass pane as a narrow rectangle, while the lift accelerates upwards and the partial vacuum is the smallest possible. The pad is shown in grey in the middle of the upper surface of the pane. The weight G starts from the centre of the pane straight down. The force of the pressure difference F p starts from the upper surface of the pane at the pad and points up, and it is longer than the weight, because the pane accelerates upwards. In this limiting case the normal force from the rim of the pad is zero. Separately, an orange acceleration arrow a upwards." style="max-width:100%;font-size:24px">
  <rect x="144" y="113" width="72" height="12" rx="4" fill="#6b7480" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="98" y="96" width="36" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#6b7480">$\text{pad}$</div></foreignObject>
  <rect x="50" y="125" width="260" height="20" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="180" y1="135" x2="180" y2="195.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,212.5 L172,194.5 L188,194.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="189.5" y="202" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="180" y1="125" x2="180" y2="55" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,38 L188,56 L172,56 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="187.5" y="29.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{p}$</div></foreignObject>
  <line x1="370" y1="165" x2="370" y2="107" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M376.5,118 L370,105 L363.5,118" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="373.5" y="94.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

**Formula:** $F_\text{p} - mg = ma$ and $F_\text{p} = \Delta p\,A$, where $m = \rho\,l\,b\,h$ and $A = \pi \left(\dfrac{d}{2}\right)^2$, so $\Delta p = \dfrac{m(g + a)}{\pi (d/2)^2}$
**Conversions:** $10\,\text{mm} = 10 \cdot 0.001\,\text{m} = 0.010\,\text{m}$ and $d/2 = 300\,\text{mm} : 2 = 150\,\text{mm} = 0.150\,\text{m}$
**Substitution:** $m = 2500\,\tfrac{\text{kg}}{\text{m}^3} \cdot 2.40\,\text{m} \cdot 1.20\,\text{m} \cdot 0.010\,\text{m} = 72.0\,\text{kg}$, $A = \pi \cdot (0.150\,\text{m})^2 = 0.070\,69\,\text{m}^2$ and $\Delta p = \dfrac{72.0\,\text{kg} \cdot (9.81 + 1.2)\,\text{m/s}^2}{0.070\,69\,\text{m}^2} = \dfrac{792.7\,\text{N}}{0.070\,69\,\text{m}^2} = 11\,210\,\text{Pa}$
**Answer:** $\Delta p \approx 11.2\,\text{kPa}$, three significant figures like the dimensions of the pane; the acceleration $1.2\,\text{m/s}^2$ is given to two figures, but it is only a small part of the sum $g + a$.
**Reasonableness:** Without the acceleration $706\,\text{N} : 0.0707\,\text{m}^2 \approx 10\,\text{kPa}$ would be needed, so the acceleration increases the need by about $12\,\%$, as the ratio $1.2 : 9.81$ tells. The lifter's $60\,\text{kPa}$ is more than five times as much.

### b)
**Given:** $m = 72.0\,\text{kg}$, $A = 0.070\,69\,\text{m}^2$, $a = 1.2\,\text{m/s}^2$ upwards, coefficient of static friction of dry glass $\mu_0 = 0.60$
**Find:** the force diagram of the upright pane and the minimum partial vacuum $\Delta p$
**Principle:** The force of the pressure difference is perpendicular to the surface of the glass, and now the surface is vertical, so the force $F_\text{p} = \Delta p\,A$ is horizontal and presses the pane against the pad. The rim of the pad pushes the pane back with the normal force $N$. Horizontally the pane does not accelerate, so $N = F_\text{p}$. Against the weight and the accelerating force the pane is supported only by the static friction of the rim of the pad, which is at most $\mu_0 N$ (chapter *Weight, friction and the inclined plane*). At the minimum partial vacuum the static friction is at its maximum.

<svg data-fig="fy9-kaasut-s6-pysty" viewBox="0 0 420 400" role="img" aria-label="Force diagram: the glass pane turned upright as a narrow vertical rectangle, the pad on the left surface of the pane, in grey. The weight G from the centre straight down. The force of the pressure difference F p pushes the pane from the right horizontally to the left, towards the pad. The normal force N from the rim of the pad pushes the pane from the left horizontally to the right; it is as large as F p. The static friction F μ0 starts from the upper left corner of the pane and points up, and it is longer than the weight, because the pane accelerates upwards. N is about 1.7 times as long as the friction, because at the smallest partial vacuum the friction is 0.60 times the normal force. Separately, an orange acceleration arrow a upwards." style="max-width:100%;font-size:24px">
  <rect x="176" y="160" width="12" height="100" rx="4" fill="#6b7480" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="134" y="265" width="36" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#6b7480">$\text{pad}$</div></foreignObject>
  <rect x="188" y="85" width="24" height="250" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="200" y1="210" x2="200" y2="253" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M200,270 L192,252 L208,252 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="211.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="324.5" y1="190" x2="229" y2="190" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M212,190 L230,182 L230,198 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="326" y="153.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{p}$</div></foreignObject>
  <line x1="75.5" y1="230" x2="171" y2="230" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M188,230 L170,238 L170,222 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="35" y="193.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="188" y1="85" x2="188" y2="34.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M188,17.5 L196,35.5 L180,35.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="129" y="11" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu 0}$</div></foreignObject>
  <line x1="385" y1="265" x2="385" y2="207" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M391.5,218 L385,205 L378.5,218" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="388.5" y="194.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

**Formula:** horizontally $N - F_\text{p} = 0$ and vertically $F_{\mu 0} - mg = ma$, where $F_{\mu 0} \le \mu_0 N = \mu_0\,\Delta p\,A$, so $\Delta p = \dfrac{m(g + a)}{\mu_0 A}$
**Conversions:** Not needed: the quantities of part a are in base units.
**Substitution:** $\Delta p = \dfrac{72.0\,\text{kg} \cdot (9.81 + 1.2)\,\text{m/s}^2}{0.60 \cdot 0.070\,69\,\text{m}^2} = \dfrac{792.7\,\text{N}}{0.042\,41\,\text{m}^2} = 18\,690\,\text{Pa}$
**Answer:** $\Delta p \approx 18.7\,\text{kPa}$, three significant figures as in part a; the coefficient of friction is an indicative two-figure value, so about $19\,\text{kPa}$ is an equally good answer.
**Reasonableness:** The result is the result of part a divided by the coefficient of friction: $11.2\,\text{kPa} : 0.60 \approx 18.7\,\text{kPa}$. The upright position needs more, because the friction is smaller than the normal force that causes it.

### c)
**Find:** whether an upright lift with wet glass meets the manufacturer's instructions
**Principle:** The safety factor is the ratio of the lifter's partial vacuum to the partial vacuum the lift requires, and according to the instructions it must be at least $2$. When wet, the coefficient of static friction is $0.30$, so the result of part b doubles (chapter *Weight, friction and the inclined plane*).
**Model answer:** With wet glass $\Delta p = \dfrac{792.7\,\text{N}}{0.30 \cdot 0.070\,69\,\text{m}^2} \approx 37\,\text{kPa}$ is needed. So the lifter's $60\,\text{kPa}$ is just enough to hold the pane, but the safety factor is only $60 : 37 \approx 1.6$, below the two that the instructions require. When dry, the upright lift meets the instructions, $60 : 18.7 \approx 3.2$, and the horizontal lift clearly, $60 : 11.2 \approx 5.4$. The upright position is more demanding, because the force of the pressure is perpendicular to the surface of the glass, that is, horizontal. It does not support the weight at all; the weight is carried by friction, which is at most $\mu_0$ times the normal force. The glazier must not lift a wet pane upright with this lifter: the glass must be dried, or two pads are used, which doubles the area.

### Yleisiä virheitä
- In part a the area is calculated from the diameter instead of the radius, or the thickness of the pane is left in millimetres.
- In part a the acceleration is forgotten and only the weight is calculated.
- In part b the force of the pressure difference is drawn upwards to support the pane, although the force of pressure is always perpendicular to the surface.
- In part b the friction is calculated from the weight, $\mu_0 mg$, and not from the normal force $N = \Delta p\,A$.
- In part c the answer is that the lift succeeds because $60\,\text{kPa}$ is more than $37\,\text{kPa}$, and the safety factor is forgotten.

### Hyväksytään myös
- In parts a and b the normal force from the rim of the pad may also be drawn in the force diagram, when the answer says that it is zero at the minimum partial vacuum (a) or equal to the force of the pressure difference (b).
