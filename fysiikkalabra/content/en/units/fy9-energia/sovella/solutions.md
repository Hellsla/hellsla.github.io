## fy9-energia-s1

### a)
**Given:** average power of the fridge $P_1 = 45\,\text{W}$ for the whole day, $t_1 = 24\,\text{h}$; six LED lamps, each $7.0\,\text{W}$, time $t_2 = 5.0\,\text{h}$; coffee maker $P_3 = 1.0\,\text{kW}$, time $t_3 = 15\,\text{min}$
**Find:** the electrical energy $E_\text{need}$ used by the devices in a day, in kilowatt-hours
**Principle:** Each device transforms energy at its own power, so its energy is power multiplied by the time of use (chapter *Power*). The power of the fridge is an average power, so it too is multiplied by the whole day. The energies are added up in the same unit.
**Formula:** $E = P\,t$ for each device, so $E_\text{need} = P_1 t_1 + 6\,P_2 t_2 + P_3 t_3$
**Conversions:** For kilowatt-hours the powers to kilowatts and the times to hours: $45\,\text{W} = 45 \cdot 0.001\,\text{kW} = 0.045\,\text{kW}$, $7.0\,\text{W} = 0.0070\,\text{kW}$ and $15\,\text{min} = 15 \cdot \tfrac{1}{60}\,\text{h} = 0.25\,\text{h}$.
**Substitution:** $E_\text{need} = 0.045\,\text{kW} \cdot 24\,\text{h} + 6 \cdot 0.0070\,\text{kW} \cdot 5.0\,\text{h} + 1.0\,\text{kW} \cdot 0.25\,\text{h} = 1.08\,\text{kWh} + 0.21\,\text{kWh} + 0.25\,\text{kWh} = 1.54\,\text{kWh}$
**Answer:** $E_\text{need} \approx 1.5\,\text{kWh}$, that is, $1.54 \cdot 3.6\,\text{MJ} \approx 5.5\,\text{MJ}$, two significant figures like the power of the fridge $45\,\text{W}$ and the power of the coffee maker $1.0\,\text{kW}$.
**Reasonableness:** The fridge uses almost two thirds of the energy, even though its power is the second smallest of the devices: it is on all the time. The large power of the coffee maker matters little, because it is on for only a quarter of an hour. One and a half kilowatt-hours a day is a usual consumption for a small summer cottage.

### b)
**Given:** from part a $E_\text{need} = 1.54\,\text{kWh}$; efficiency of the battery $\eta_\text{batt} = 90\,\%$, of the inverter $\eta_\text{inv} = 93\,\%$; production on a cloudy day $1.5\,\text{kWh}$
**Find:** the daily production $E_\text{panels}$ needed from the panels, and whether the production of a cloudy day is enough
**Principle:** Energy travels from the panels through the battery and the inverter to the devices. The stages are in series: the energy given by the battery is the energy taken in by the inverter. So the efficiency of the chain is the product of the efficiencies of the stages, and the panels must produce more than the devices use (chapter *Energy production and the efficiency of power plants*).
**Formula:** $\eta = \eta_\text{batt}\,\eta_\text{inv} = \dfrac{E_\text{need}}{E_\text{panels}}$, so $E_\text{panels} = \dfrac{E_\text{need}}{\eta_\text{batt}\,\eta_\text{inv}}$
**Conversions:** $90\,\% = 0.90$ and $93\,\% = 0.93$. The energies stay in kilowatt-hours.
**Substitution:** $E_\text{panels} = \dfrac{1.54\,\text{kWh}}{0.90 \cdot 0.93} = \dfrac{1.54\,\text{kWh}}{0.837} = 1.84\,\text{kWh}$. On a cloudy day $0.837 \cdot 1.5\,\text{kWh} = 1.26\,\text{kWh}$ reaches the devices.
**Answer:** The panels must produce about $1.8\,\text{kWh}$ a day (two significant figures like the need in part a). The $1.5\,\text{kWh}$ of a cloudy day is not enough: only about $1.3\,\text{kWh}$ of it reaches the devices, so the missing part is taken from the battery if it holds a surplus from a sunny day.
**Reasonableness:** The efficiency of the chain, $0.84$, is smaller than that of either stage, as it must be in a multiplication, and the need grows by about a fifth. On a sunny day $0.837 \cdot 5.4\,\text{kWh} \approx 4.5\,\text{kWh}$ reaches the devices, which is enough for almost three days.

### c)
**Find:** whether the neighbour's conclusion about the panels' daily energy is correct
**Principle:** Power tells how fast energy is transformed, and energy is power multiplied by time (chapter *Power*). The rated power of a panel is the maximum power it gives in bright sunshine.
**Model answer:** The claim is wrong, because it mixes up power and energy. The kilowatt is a unit of power and the kilowatt-hour a unit of energy: $1.2\,\text{kW}$ means that the panels can produce at most $1.2\,\text{kWh}$ *per hour*. The day's energy is the average power multiplied by the time, and it depends on how long and how strongly the sun shines. According to the data, on a sunny day the panels produced $5.4\,\text{kWh}$, which corresponds to $5.4\,\text{kWh} : 1.2\,\text{kW} = 4.5$ hours at full power. On a cloudy day the production of $1.5\,\text{kWh}$ corresponded to only about one hour. The neighbour's number happens to be close to the cloudy day, but the reasoning is wrong.

### Yleisiä virheitä
- The average power of the fridge is multiplied by only a few hours, because the compressor does not run all the time; the average power already takes this into account.
- $15\,\text{min}$ is written as $0.15\,\text{h}$; correctly $15 \cdot \tfrac{1}{60}\,\text{h} = 0.25\,\text{h}$.
- In part b the need is multiplied by the efficiencies, which gives a panel production smaller than the need.
- The losses of the efficiencies are added up ($10\,\% + 7\,\% = 17\,\%$); here the result is close to the correct one, but the principle is wrong.

### Hyväksytään myös
- The energy of part a in joules: $E_\text{need} = 1.54 \cdot 3.6\,\text{MJ} \approx 5.5\,\text{MJ}$.

## fy9-energia-s2

### a)
**Given:** mass of chips burnt in an hour $m = 42\,\text{t}$, time $t = 1\,\text{h}$, heat of combustion $H = 9.5\,\text{MJ/kg}$
**Find:** the fuel power $P_0$ in megawatts
**Principle:** The energy released from the chips is the heat of combustion multiplied by the mass burnt, because the heat of combustion is energy per kilogram (chapter *Fuels and heat of combustion*). The fuel power is this energy divided by the time in which it is released (chapter *Power*).
**Formula:** $E = Hm$ and $P_0 = \dfrac{E}{t}$, so $P_0 = \dfrac{Hm}{t}$
**Conversions:** $42\,\text{t} = 42 \cdot 1000\,\text{kg} = 42\,000\,\text{kg}$, $9.5\,\text{MJ/kg} = 9.5 \cdot 10^{6}\,\text{J/kg}$ and $1\,\text{h} = 3600\,\text{s}$; finally $1\,\text{W} = 10^{-6}\,\text{MW}$.
**Substitution:** $P_0 = \dfrac{9.5 \cdot 10^{6}\,\text{J}/\text{kg} \cdot 42\,000\,\text{kg}}{3600\,\text{s}} = \dfrac{3.99 \cdot 10^{11}\,\text{J}}{3600\,\text{s}} = 1.108 \cdot 10^{8}\,\text{W} = 110.8\,\text{MW}$
**Answer:** $P_0 \approx 1.1 \cdot 10^{2}\,\text{MW}$, two significant figures like the heat of combustion $9.5\,\text{MJ/kg}$ and the mass $42\,\text{t}$. The later parts use the unrounded value $110.8\,\text{MW}$.
**Reasonableness:** The fuel power is a little greater than the sum of the electrical and district heating powers, $100\,\text{MW}$, as conservation of energy requires: the remaining $11\,\text{MW}$ or so is losses. With round numbers $10\,\text{MJ/kg} \cdot 40\,000\,\text{kg} : 3600\,\text{s} \approx 110\,\text{MW}$.

### b)
**Given:** from part a $P_0 = 110.8\,\text{MW}$; electrical power $P_\text{el} = 30\,\text{MW}$, district heating power $P_\text{dh} = 70\,\text{MW}$
**Find:** the electrical efficiency $\eta_\text{el}$ and the overall efficiency $\eta_\text{tot}$ as percentages
**Principle:** Efficiency is the fraction of the power taken in that is useful. In the electrical efficiency only electricity is useful, in the overall efficiency electricity and district heat together (chapter *Energy production and the efficiency of power plants*).
**Formula:** $\eta_\text{el} = \dfrac{P_\text{el}}{P_0}$ and $\eta_\text{tot} = \dfrac{P_\text{el} + P_\text{dh}}{P_0}$
**Conversions:** All the powers are in megawatts, so the unit cancels. The ratio is converted to a percentage by multiplying it by $100\,\%$.
**Substitution:** $\eta_\text{el} = \dfrac{30\,\text{MW}}{110.8\,\text{MW}} = 0.271 = 27.1\,\%$ and $\eta_\text{tot} = \dfrac{30\,\text{MW} + 70\,\text{MW}}{110.8\,\text{MW}} = 0.902 = 90.2\,\%$
**Answer:** $\eta_\text{el} \approx 27\,\%$ and $\eta_\text{tot} \approx 90\,\%$, two significant figures like the powers $30\,\text{MW}$ and $70\,\text{MW}$.
**Reasonableness:** Both are below $100\,\%$. The electrical efficiency is smaller than the roughly $40\,\%$ of an ordinary condensing power plant, because in combined heat and power the steam is condensed at a higher temperature for district heating. An overall efficiency of $90\,\%$ is typical of combined heat and power.

### c)
**Given:** electrical power $P_\text{el} = 30\,\text{MW}$ and district heating power $P_\text{dh} = 70\,\text{MW}$; efficiency of the condensing power plant $\eta_\text{cond} = 38\,\%$, of the heating boiler $\eta_\text{hb} = 90\,\%$; $H = 9.5\,\text{MJ/kg}$; time $t = 1\,\text{h}$
**Find:** the mass $m$ of chips needed per hour in separate production, in tonnes
**Principle:** Each plant needs a fuel power that is its useful power divided by its efficiency. The fuel powers of the plants are added up, and the mass is obtained from the energy of one hour with the heat of combustion as in part a.
**Formula:** $P_0 = \dfrac{P_\text{el}}{\eta_\text{cond}} + \dfrac{P_\text{dh}}{\eta_\text{hb}}$ and $P_0\,t = Hm$, so $m = \dfrac{P_0\,t}{H}$
**Conversions:** $38\,\% = 0.38$, $90\,\% = 0.90$, $1\,\text{MW} = 10^{6}\,\text{W}$, $1\,\text{h} = 3600\,\text{s}$, $9.5\,\text{MJ/kg} = 9.5 \cdot 10^{6}\,\text{J/kg}$ and finally $1\,\text{kg} = 0.001\,\text{t}$.
**Substitution:** $P_0 = \dfrac{30\,\text{MW}}{0.38} + \dfrac{70\,\text{MW}}{0.90} = 78.9\,\text{MW} + 77.8\,\text{MW} = 156.7\,\text{MW}$ and $m = \dfrac{156.7 \cdot 10^{6}\,\text{W} \cdot 3600\,\text{s}}{9.5 \cdot 10^{6}\,\text{J}/\text{kg}} = 59\,390\,\text{kg} = 59.4\,\text{t}$
**Answer:** about $59\,\text{t}$ of chips per hour, two significant figures like the powers and the heat of combustion. That is about $17\,\text{t}$ more than the $42\,\text{t}$ of combined heat and power.
**Reasonableness:** Separate production needs more fuel, because the heat of the condensing power plant's condenser is wasted. Combined heat and power saves $1 - 42 : 59.4 \approx 0.29$, that is, about a third of the fuel, which is a typical order of magnitude for combined heat and power.

### d)
**Find:** why the overall efficiency falls in summer, when little district heat is needed
**Principle:** Efficiency depends on what is counted as useful (chapter *Efficiency*). A heat engine cannot turn all heat into electricity; part must be given off to the colder surroundings (chapter *Energy production and the efficiency of power plants*).
**Model answer:** Heat must in any case be removed from the steam cycle in the condenser when the plant produces electricity. In winter this heat warms district heating water and counts as useful, so the overall efficiency is about $90\,\%$. In summer district heat is needed only for tap water, so most of the condenser's heat must be given off to the surroundings, for example to cooling water, as waste heat. If the electrical power stays at $30\,\text{MW}$, about the same amount of fuel is still used, but less of it is useful, and the overall efficiency falls towards the electrical efficiency. That is why a combined heat and power plant is run according to the heat demand: in summer at a lower power or not at all, and the electricity is produced elsewhere.

### Yleisiä virheitä
- The tonnes per hour are divided directly by the hour without conversions, so the power is obtained in the unit $\text{MJ/h}$ and compared with megawatts.
- Only electricity is counted in the overall efficiency, or the efficiency is calculated from the electrical power ($70 : 30$).
- In part c the electrical and heating powers are added up and divided by a single efficiency, even though there are two plants.
- In part c the efficiencies are multiplied together, even though the plants are not in series but in parallel.

### Hyväksytään myös
- In part a $P_0 \approx 111\,\text{MW}$ and the later parts calculated with it: $\eta_\text{el} \approx 27\,\%$ and $\eta_\text{tot} \approx 90\,\%$.

## fy9-energia-s3

### a)
**Find:** a graph of the daily electricity consumption $E$ as a function of the outdoor temperature $T$, and a model fitted to it
**Graph:** On the horizontal axis is the outdoor temperature $T\ ({}^\circ\text{C})$ and on the vertical axis the daily consumption $E\ (\text{kWh})$. The horizontal axis needs negative temperatures, and the scale continues for parts c and d from $-30\,{}^\circ\text{C}$ to $+20\,{}^\circ\text{C}$.

<svg data-fig="fy9-energia-s3-graph" viewBox="0 0 600 440" role="img" aria-label="Graph: the house&#x27;s daily electricity consumption E as a function of the outdoor temperature T. Eight black points at temperatures −19…2 °C. A falling straight line is fitted to the points and extended as a dashed line in both directions. The line passes through the points (−20 °C, 191 kWh) and (0 °C, 93 kWh); these two points of the line are circled, and the slope, about −4.9 kWh per degree, is read from them. At the temperature −28 °C about 230 kWh is read from the line. The line falls to the level of the other consumption, 12 kWh, at about 17 °C." style="max-width:100%;font-size:24px">
  <line x1="125.5" y1="390" x2="125.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="167" y1="390" x2="167" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="209" y1="390" x2="209" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250.5" y1="390" x2="250.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="292" y1="390" x2="292" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="333.5" y1="390" x2="333.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375" y1="390" x2="375" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="417" y1="390" x2="417" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="458.5" y1="390" x2="458.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="390" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="326" x2="500" y2="326" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="262" x2="500" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="198" x2="500" y2="198" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="134" x2="500" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="70" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="390" x2="514" y2="390" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,390 L513,396 L513,384 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="391" x2="84" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,44 L90,57 L78,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="125.5" y1="390" x2="125.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="167" y1="390" x2="167" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="144.5" y="399.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="209" y1="390" x2="209" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="250.5" y1="390" x2="250.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="228" y="399.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-10$</div></foreignObject>
  <line x1="292" y1="390" x2="292" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="333.5" y1="390" x2="333.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="323.5" y="399.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="375" y1="390" x2="375" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="417" y1="390" x2="417" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="400.5" y="399.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="458.5" y1="390" x2="458.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="390" x2="500" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="399.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="77" y1="326" x2="84" y2="326" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="77" y1="262" x2="84" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="77" y1="198" x2="84" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="183.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="77" y1="134" x2="84" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="119.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="77" y1="70" x2="84" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="532" y="375.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="74" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{kWh})$</div></foreignObject>
  <line x1="333.5" y1="390" x2="333.5" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <polyline points="175.5,152 350,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92.5,89.5 175.5,152" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="350,284 483.5,384" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="300.5" cy="246.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="250.5" cy="212" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="200.5" cy="167.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="175.5" cy="152" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="225.5" cy="191.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="275.5" cy="228.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="325.5" cy="262" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="350" cy="284" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="167" cy="145.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="333.5" cy="271" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="100.5" y1="96" x2="100.5" y2="390" stroke="#e8590c" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="84" y1="96" x2="100.5" y2="96" stroke="#e8590c" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="471" y1="374.5" x2="471" y2="390" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="84" y1="374.5" x2="471" y2="374.5" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="134" y="68.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$230\,\text{kWh}$</div></foreignObject>
  <foreignObject x="125.5" y="341" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$12\,\text{kWh}$</div></foreignObject>
  <foreignObject x="283.5" y="119.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k \approx -4.9\,\text{kWh}/{}^\circ\text{C}$</div></foreignObject>
</svg>

The circled places in the graph are the two points of the line from which the slope in part b is read. The dashed line is the extension of the line outside the measured range (parts c and d).

**Model answer:** The points lie almost on a straight line: the consumption increases steadily as the outdoor temperature falls. One falling straight line passing between the points is fitted to them, and the points are not joined into a broken line in the order of the days. The small scatter of the points on both sides of the line is due to, for example, wind, sun and sauna use, which the temperature does not tell. In the figure the line has been extended as a dashed line outside the measured range for parts c and d.

### b)
**Given:** the graph of part a and the points read from the line; one day $t = 24\,\text{h}$
**Find:** the slope $k$ of the line and the increase of the heating power per kelvin, $\dfrac{\Delta P}{\Delta T}$, in the unit $\text{W/K}$
**Principle:** The line tells that the daily energy increases by the same amount for each degree the temperature falls. The slope is the change in energy per degree. Because the daily energy is the average power multiplied by the length of the day, the change in power is obtained by dividing the change in energy by the time (chapter *Power*). A change in temperature difference is the same in degrees Celsius and in kelvins.
**Reading the graph:** Two points far apart are read from the line, not measurement points: $(-20\,{}^\circ\text{C};\ 191\,\text{kWh})$ and $(0\,{}^\circ\text{C};\ 93\,\text{kWh})$.
**Formula:** $k = \dfrac{\Delta E}{\Delta T}$ and $P = \dfrac{E}{t}$, so $\dfrac{\Delta P}{\Delta T} = \dfrac{|k|}{t}$
**Conversions:** $1\,\text{kWh} : 1\,\text{h} = 1\,\text{kW} = 1000\,\text{W}$, so $\text{kWh}$ divided by hours gives kilowatts. A change of $1\,{}^\circ\text{C}$ is $1\,\text{K}$.
**Substitution:** $k = \dfrac{93\,\text{kWh} - 191\,\text{kWh}}{0\,{}^\circ\text{C} - (-20\,{}^\circ\text{C})} = \dfrac{-98\,\text{kWh}}{20\,{}^\circ\text{C}} = -4.9\,\text{kWh}/{}^\circ\text{C}$ and $\dfrac{\Delta P}{\Delta T} = \dfrac{4.9\,\text{kWh}}{24\,\text{h} \cdot 1\,\text{K}} = 0.204\,\text{kW}/\text{K} = 204\,\text{W}/\text{K}$
**Answer:** The slope is about $-4.9\,\text{kWh}$ per degree per day, that is, the heating power increases by about $200\,\text{W}$ for each kelvin the outdoor temperature falls. Two significant figures, because the slope read from the graph is accurate to about $\pm 0.2\,\text{kWh}$ per degree.
**Reasonableness:** According to the model, heating is needed at outdoor temperatures below about $17\,{}^\circ\text{C}$ (part d). When it is $-20\,{}^\circ\text{C}$ outside, the heating power is about $36.5\,\text{K} \cdot 0.204\,\text{kW}/\text{K} \approx 7.5\,\text{kW}$, the same as $(191 - 12)\,\text{kWh} : 24\,\text{h} \approx 7.5\,\text{kW}$, which suits the electric heating of a detached house. The least-squares line gives the same: $-4.89\,\text{kWh}$ per degree, that is, $204\,\text{W/K}$.

### c)
**Given:** the line of part a, the slope of part b $k = -4.9\,\text{kWh}$ per degree and the value of the line $93\,\text{kWh}$ at the temperature $0\,{}^\circ\text{C}$; the temperature to estimate $T = -28\,{}^\circ\text{C}$
**Find:** the daily consumption $E$ in kilowatt-hours and the reliability of the estimate
**Principle:** The line is a model of the consumption. A value outside the measured range is obtained by extending the line, that is, by extrapolating, which is justified only if the same model also holds there.
**Reading the graph:** From the line extended as a dashed line, about $230\,\text{kWh}$ is read at the temperature $-28\,{}^\circ\text{C}$.
**Formula:** $E = kT + b$, where $b$ is the value of the line at the temperature $0\,{}^\circ\text{C}$
**Conversions:** Not needed: the temperature and the slope are in the same units as in the graph.
**Substitution:** $E = -4.9\,\text{kWh}/{}^\circ\text{C} \cdot (-28\,{}^\circ\text{C}) + 93\,\text{kWh} = 137\,\text{kWh} + 93\,\text{kWh} = 230\,\text{kWh}$
**Answer:** about $230\,\text{kWh}$ a day, two significant figures like the slope. The estimate is an extrapolation $9\,\text{K}$ beyond the coldest measurement, $-19\,{}^\circ\text{C}$. It holds if the heat losses keep growing in direct proportion to the temperature difference; a strong wind increases the consumption, and if the combined power of the heaters is below about $9\,\text{kW}$, they are not enough and the indoor temperature falls.
**Reasonableness:** The consumption is roughly two and a half times the consumption at zero degrees, and the average power $230\,\text{kWh} : 24\,\text{h} \approx 9.6\,\text{kW}$ is at the upper end of the electric heating of a detached house. At an example price of $0.20\,\text{€/kWh}$ the day would cost about $46\,\text{€}$.

### d)
**Find:** the outdoor temperature at which, according to the model, no heating is needed, and why it is not $21\,{}^\circ\text{C}$
**Principle:** When no heating is needed, the consumption is just the other electricity consumption, $12\,\text{kWh}$. Energy is conserved: all the electrical energy used indoors finally becomes heat, and the people and solar radiation also bring energy into the house (chapter *Forms of energy and conservation of energy*).
**Model answer:** From the extended line we read that the consumption falls to the level of the other consumption, $12\,\text{kWh}$, at about $16$–$17\,{}^\circ\text{C}$ ($16.5\,{}^\circ\text{C}$ from the equation of the line). So the house needs heating only when it is colder outside. The temperature is about $4\,\text{K}$ below the indoor temperature $21\,{}^\circ\text{C}$, because the electrical energy of lighting, cooking and appliances becomes heat indoors. In addition, the residents warm the house, and solar radiation through the windows adds energy. These make up for the heat losses of a small temperature difference, so the heaters are needed only to cover the rest. The result is indicative: it is based on a line of winter days extended far beyond the measured range, and the data do not separate the sun and the wind.

### Yleisiä virheitä
- The points are joined into a broken line in the order of the dates, so the graph does not show the dependence on temperature.
- The slope is calculated from two adjacent measurement points and not from the fitted line.
- In part b the kilowatt-hours are read directly as kilowatts without dividing by the hours of the day, which gives $4900\,\text{W/K}$.
- In part c extrapolation is not mentioned at all, or the result is taken as certain.
- In part d the answer is that heating stops at $21\,{}^\circ\text{C}$, because the temperature is then the same as indoors.

### Hyväksytään myös
- A slope of $-4.7$…$-5.1\,\text{kWh}$ per degree when the line is fitted by eye between the points, and the results that follow from it: in part b $192$–$216\,\text{W/K}$, in part c $220$–$240\,\text{kWh}$ and in part d $15$–$18\,{}^\circ\text{C}$.

## fy9-energia-s4

### a)
**Find:** whether two wind turbines and a battery are enough to replace the diesel power plant
**Principle:** The year's energy is the average power multiplied by the hours of the year (chapter *Ways of producing energy and how they compare*). In an electricity grid, however, production must match consumption at every moment, so besides energy the power and the storage must be examined.
**Model answer:** The average power of the wind turbines is $0.30 \cdot 2 \cdot 1.0\,\text{MW} = 0.60\,\text{MW}$, so in a year they produce $0.60\,\text{MW} \cdot 8760\,\text{h} \approx 5.3\,\text{GWh}$. That is more than the island's consumption of $3.0\,\text{GWh}$, so the first part of the claim holds for the year's energy. Electricity, however, cannot be used at the time it is produced on average over the year: in calm weather the wind turbines produce nothing. A full battery covers the winter peak consumption for only $2.0\,\text{MWh} : 1.2\,\text{MW} \approx 1.7$ hours, and a calm frosty period can last for days. So the diesel plant cannot be dismantled unless the island gets other dispatchable power or a connection to the mainland grid.

### b)
**Find:** a comparison of the options on at least three criteria and a reasoned recommendation
**Principle:** Production methods are compared on the same criteria: controllability and security of supply, emissions, transport and storage of fuel, and price (chapters *Ways of producing energy and how they compare* and *Energy production, the environment and climate change*).
**Model answer:**
- *Controllability and security of supply.* The diesel power plant is controllable and covers the peak ($1.5\,\text{MW} > 1.2\,\text{MW}$). Wind power depends on the weather, and the battery does not cover a long calm. The cable brings the dispatchable power of the whole mainland grid to the island, and its $5\,\text{MW}$ covers the peak.
- *Emissions.* Diesel produces about $2100\,\text{t}$ of carbon dioxide a year (part c). The life-cycle emissions of wind power are only a small fraction of that, and the emissions of the cable's electricity depend on the production methods on the mainland.
- *Transport and losses.* Diesel must be brought by ship, which is expensive and vulnerable to an icy winter. The transmission loss of the cable is only about $3\,\%$: for the island's $3.0\,\text{GWh}$, about $3.1\,\text{GWh}$ is sent from the mainland.
- *Price.* The cable and the wind turbines are large investments, but they have no fuel costs.

Recommendation: the submarine cable and the wind turbines together. The cable secures electricity in calm weather and carries the surplus to the mainland, wind power reduces emissions, and the current diesel power plant remains as backup power in case of a cable fault.

### c)
**Find:** the annual carbon dioxide emissions of the diesel power plant and an evaluation of the claim “wind power is completely emission-free”
**Principle:** The emissions are the energy multiplied by the emission factor, $m = e \cdot E$. Production methods are compared by their life-cycle emissions, which also include construction, transport and dismantling (chapter *Energy production, the environment and climate change*).
**Model answer:** The consumption in kilowatt-hours is $3.0\,\text{GWh} = 3.0 \cdot 10^{6}\,\text{kWh}$, so the emissions of the diesel power plant are $m = e \cdot E = 700\,\text{g}/\text{kWh} \cdot 3.0 \cdot 10^{6}\,\text{kWh} = 2.1 \cdot 10^{9}\,\text{g}$. Substituting $1\,\text{g} = 10^{-6}\,\text{t}$: the emissions are about $2100\,\text{t}$ of carbon dioxide a year. A wind turbine burns nothing in operation, but manufacturing its steel and concrete, transporting it, building it and dismantling it cause emissions. So its life-cycle emission factor is a few tens of grams per kilowatt-hour or less, not zero. The claim is therefore inaccurate: wind power is low-emission, and its emissions are only a fraction of the emissions of diesel, but it is not completely emission-free.

### Yleisiä virheitä
- In part a the wind turbines' annual energy is calculated with the rated power ($2.0\,\text{MW} \cdot 8760\,\text{h} = 17.5\,\text{GWh}$), so the average power is not taken into account.
- The battery capacity ($\text{MWh}$) is compared directly with the consumption peak ($\text{MW}$), even though one is energy and the other power.
- In part b the properties of the options are listed without comparing them with each other or making a recommendation.
- In part c the gigawatt-hours are multiplied directly by the emission factor without converting them to kilowatt-hours.

## fy9-energia-s5

### a)
**Given:** from the report, water $m = 1.0\,\text{kg}$, initial temperature $T_1 = 15\,{}^\circ\text{C}$, final temperature $T_2 = 96\,{}^\circ\text{C}$, time $t = 3\,\text{min}\ 5\,\text{s}$, power on the rating plate $P = 2200\,\text{W}$; $c = 4190\,\text{J/(kg}\cdot\text{K)}$
**Find:** the efficiency $\eta$ of the kettle from the data of the report
**Principle:** The efficiency is the fraction of the electrical energy taken by the kettle that is transferred to the water (chapter *Efficiency*). The energy transferred to the water is the heat $Q = cm\Delta T$ transferred to the water, because the water warms up and, according to the report, does not boil away (chapter *Heating and cooling of matter*). The electrical energy is power multiplied by time.
**Formula:** $\eta = \dfrac{Q}{E}$, where $Q = cm\,(T_2 - T_1)$ and $E = P\,t$, so $\eta = \dfrac{cm\,(T_2 - T_1)}{P\,t}$
**Conversions:** $3\,\text{min}\ 5\,\text{s} = 3 \cdot 60\,\text{s} + 5\,\text{s} = 185\,\text{s}$. A temperature difference is the same in degrees Celsius and in kelvins: $96\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 81\,\text{K}$.
**Substitution:** $\eta = \dfrac{4190\,\text{J}/(\text{kg} \cdot \text{K}) \cdot 1.0\,\text{kg} \cdot 81\,\text{K}}{2200\,\text{W} \cdot 185\,\text{s}} = \dfrac{339\,390\,\text{J}}{407\,000\,\text{J}} = 0.834 = 83.4\,\%$
**Answer:** $\eta \approx 83\,\%$, two significant figures like the amount of water $1.0\,\text{kg}$ and the temperature difference $81\,\text{K}$. The group's number is calculated correctly.
**Reasonableness:** The efficiency is below $100\,\%$ and of a usual order of magnitude for a kettle: the heating element is inside the water, so most of the energy ends up in the water. The losses are $407\,\text{kJ} - 339\,\text{kJ} \approx 68\,\text{kJ}$, which warm the jug and the air.

### b)
**Find:** whether the conclusion is justified, the most important sources of error in the measurement and the direction of their effect
**Principle:** A conclusion is justified only if the difference from the claimed value is greater than the uncertainty of the result (chapter *Measuring and the reliability of a measurement*). The effect of a source of error is assessed by calculating the result again with a changed value.
**Model answer:** The group's conclusion is not justified, because the uncertainty of the result is several percentage points and the measurement was made only once.
- *Power from the rating plate.* The power on the rating plate is a nominal value, not a measured one, and the actual power depends on the mains voltage. If it were $2100\,\text{W}$, the efficiency would be $87\,\%$; if above $2200\,\text{W}$, the result would be below $83\,\%$. The electrical energy should be measured with an energy meter.
- *Final temperature.* The water boiled, that is, it was at about $100\,{}^\circ\text{C}$ when the kettle switched off, but the temperature was measured only after the lid was opened. The measurement gives too small a temperature difference and therefore too small an efficiency; with $100\,{}^\circ\text{C}$ the result would be $88\,\%$.
- *Amount of water.* The scale of the jug is inaccurate. If there was $1.05\,\text{kg}$ of water, the result would be $88\,\%$; if $0.95\,\text{kg}$, it would be $79\,\%$. The water should be weighed.
- *Warming of the jug and evaporation.* Part of the energy warms the jug and part evaporates water during boiling. These are real losses, but they depend on what the manufacturer counts as useful.

The late reading of the final temperature certainly makes the result smaller. The power on the rating plate and the scale of the jug can change it in either direction: the actual power depends on the mains voltage and can be above or below $2200\,\text{W}$. So the actual efficiency may well be close to $90\,\%$. Disproving the claim requires a measured electrical energy, weighed water and several repetitions.

### c)
**Find:** an experimental plan to find out whether the efficiency depends on the amount of water
**Principle:** In the experiment only one variable, the amount of water, is changed and the others are kept constant. The quantities are measured as directly as possible, and the measurements are repeated so that the size of the random variation can be seen (chapter *Measuring and the reliability of a measurement*).
**Model answer:**
- *Variables.* The quantity changed is the mass of the water, for example $0.50\,\text{kg}$, $0.75\,\text{kg}$, $1.0\,\text{kg}$, $1.25\,\text{kg}$ and $1.5\,\text{kg}$. Kept constant are the same kettle, the same initial temperature (water from the same container), the lid closed and the initial temperature of the kettle: the jug is allowed to cool to room temperature or is rinsed with cold water between measurements.
- *Measurements.* The water is weighed on a balance. The kettle is connected through an energy meter, which shows the electrical energy directly. Heating is stopped before boiling, for example when the temperature of the stirred water is $80\,{}^\circ\text{C}$, so that evaporation does not distort the result; the temperature is measured immediately after switching off, while stirring.
- *Repetitions and results.* Each amount of water is measured three times. The efficiency is calculated with the formula $\eta = \tfrac{cm\Delta T}{E}$, and the results are presented in a graph of the efficiency as a function of the amount of water, with the spread of the repetitions.

If the efficiency increases as the amount of water increases, the reason is probably the warming of the jug: it takes almost the same energy every time, so it is a larger share of the energy for a small amount of water.

### Yleisiä virheitä
- In part a the temperature difference is converted to kelvins by adding $273$ to the two temperatures differently, or the final temperature $96\,{}^\circ\text{C}$ is used as the temperature difference.
- The time is written as $3.5\,\text{min}$; $3\,\text{min}\ 5\,\text{s}$ is $185\,\text{s}$.
- In part b it is only stated that “there were measurement errors”, without naming the source of error or the direction of its effect.
- In part c the amount of water and the kettle are changed at the same time, or the water is heated to different temperatures, so the effects cannot be separated.

### Hyväksytään myös
- In part c the heating can also be stopped when the kettle switches off, if the final temperature is measured immediately with the lid closed and the plan notes the effect of evaporation.

## fy9-energia-s6

### a)
**Given:** volume of the upper reservoir $V = 7.50 \cdot 10^{4}\,\text{m}^3$, density of water $\rho = 1000\,\text{kg/m}^3$, height difference $h = 1.20\,\text{km}$, $g = 9.81\,\text{m/s}^2$
**Find:** the potential energy $E_\text{p}$ of the water compared with the lower reservoir, in megawatt-hours
**Principle:** When the lower reservoir is chosen as the zero level, the potential energy of water at the height $h$ is equal to the work needed to lift it steadily up, $mgh$ (chapters *Work and energy* and *Kinetic energy, potential energy and mechanical energy*). The depth of the reservoir is small compared with the height difference, so all the water is at about the height $h$.
**Formula:** $m = \rho V$ and $E_\text{p} = mgh$, so $E_\text{p} = \rho V g h$
**Conversions:** $1.20\,\text{km} = 1.20 \cdot 1000\,\text{m} = 1200\,\text{m}$. The megawatt-hour by substitution: $1\,\text{MWh} = 10^{6}\,\text{W} \cdot 3600\,\text{s} = 3.6 \cdot 10^{9}\,\text{J}$.
**Substitution:** $E_\text{p} = 1000\,\text{kg}/\text{m}^3 \cdot 7.50 \cdot 10^{4}\,\text{m}^3 \cdot 9.81\,\text{m}/\text{s}^2 \cdot 1200\,\text{m} = 8.829 \cdot 10^{11}\,\text{J} = \dfrac{8.829 \cdot 10^{11}}{3.6 \cdot 10^{9}}\,\text{MWh} = 245.3\,\text{MWh}$
**Answer:** $E_\text{p} \approx 245\,\text{MWh}$, three significant figures like the volume $7.50 \cdot 10^{4}\,\text{m}^3$ and the height difference $1.20\,\text{km}$.
**Reasonableness:** A kilogram of water gains about $12\,\text{kJ}$ from a drop of $1200\,\text{m}$, so one cubic metre about $12\,\text{MJ} \approx 3.3\,\text{kWh}$. $75\,000$ cubic metres therefore give about $250\,\text{MWh}$, the same order of magnitude.

### b)
**Given:** from part a $E_\text{p} = 245.3\,\text{MWh}$; efficiency of the turbine and the generator $\eta_\text{t} = 88\,\%$; emptying time $t = 6.0\,\text{h}$
**Find:** the electrical power $P$ of the plant in megawatts
**Principle:** The turbine and the generator turn the energy of the flowing water into electricity, and the efficiency tells the share that becomes electricity. The reservoir is emptied steadily, so the power is the electrical energy divided by the time (chapter *Power*).
**Formula:** $E_\text{el} = \eta_\text{t}\,E_\text{p}$ and $P = \dfrac{E_\text{el}}{t}$, so $P = \dfrac{\eta_\text{t}\,E_\text{p}}{t}$
**Conversions:** $88\,\% = 0.88$. Megawatt-hours divided by hours give megawatts directly: $\text{MWh} : \text{h} = \text{MW}$.
**Substitution:** $P = \dfrac{0.88 \cdot 245.3\,\text{MWh}}{6.0\,\text{h}} = \dfrac{215.8\,\text{MWh}}{6.0\,\text{h}} = 35.97\,\text{MW}$
**Answer:** $P \approx 36\,\text{MW}$, two significant figures like the emptying time $6.0\,\text{h}$ and the efficiency $88\,\%$.
**Reasonableness:** The power corresponds to about ten large wind turbines or about $16\,000$ kettles. The electrical energy $216\,\text{MWh}$ is smaller than the potential energy $245\,\text{MWh}$, as conservation of energy and the losses require.

### c)
**Given:** $E_\text{p} = 245.3\,\text{MWh}$; efficiency of the pump and the motor $\eta_\text{p} = 85\,\%$; from part b $\eta_\text{t} = 88\,\%$ and the electrical energy $E_\text{el} = 215.8\,\text{MWh}$
**Find:** the electrical energy $E_\text{grid}$ taken from the grid for pumping and the overall efficiency $\eta$ of the storage
**Principle:** In pumping, electrical energy is transformed into the potential energy of the water, and only the share $\eta_\text{p}$ of it is useful, so more must be taken from the grid than the potential energy the water gains. Filling and emptying are successive stages, so the overall efficiency is their product (chapter *Energy production and the efficiency of power plants*).
**Formula:** $\eta_\text{p} = \dfrac{E_\text{p}}{E_\text{grid}}$, so $E_\text{grid} = \dfrac{E_\text{p}}{\eta_\text{p}}$, and $\eta = \eta_\text{p}\,\eta_\text{t}$
**Conversions:** $85\,\% = 0.85$ and $88\,\% = 0.88$; the energies stay in megawatt-hours.
**Substitution:** $E_\text{grid} = \dfrac{245.3\,\text{MWh}}{0.85} = 288.5\,\text{MWh}$ and $\eta = 0.85 \cdot 0.88 = 0.748 = 74.8\,\%$
**Answer:** About $290\,\text{MWh}$ is taken from the grid (two significant figures like the efficiency $85\,\%$; more precisely $289\,\text{MWh}$), and the overall efficiency is about $75\,\%$.
**Reasonableness:** A check with the energies: $E_\text{el} : E_\text{grid} = 215.8\,\text{MWh} : 288.5\,\text{MWh} = 0.748$, the same as the product of the efficiencies. About a quarter of the energy becomes heat in the pipes, the pump, the turbine and the generators, which is typical of pumped-storage plants.

### d)
**Find:** whether the claim “the plant produces $216\,\text{MWh}$ of electricity every day” holds, and why the plant can still be useful
**Principle:** Energy is conserved: as electricity the plant can give at most the energy stored in it by pumping, and because of the losses less (chapter *Forms of energy and conservation of energy*). A store shifts energy in time (chapter *Transferring energy: electricity and heat*).
**Model answer:** The claim is misleading. A pumped-storage plant does not produce energy but stores it: in each filling and emptying it takes about $289\,\text{MWh}$ from the grid and gives back about $216\,\text{MWh}$, so about $73\,\text{MWh}$ becomes heat. The plant is still useful, because it shifts energy in time. It is filled when electricity is plentiful and cheap, for example on a windy night, and emptied at the time of peak consumption or in calm weather, when electricity is scarce. As hydropower it is also quickly controllable power, which weather-dependent wind power needs alongside it. A correct wording would be: “The plant gives $216\,\text{MWh}$ to the grid from the $289\,\text{MWh}$ it took, later, when electricity is needed.”

### Yleisiä virheitä
- In part a the mass is calculated directly from the volume without the density, or the kilometres are not converted to metres.
- The joules are converted to megawatt-hours by dividing by $3600$ or by $10^{6}$, but not by both.
- In part c the potential energy is multiplied by the efficiency of the pump, so the energy taken from the grid would be smaller than the energy stored in the water.
- The overall efficiency is calculated as the mean $(85\,\% + 88\,\%) : 2$ or as a sum and not as a product.

### Hyväksytään myös
- The energy of part c to three significant figures, $289\,\text{MWh}$, and the overall efficiency $74.8\,\%$.
