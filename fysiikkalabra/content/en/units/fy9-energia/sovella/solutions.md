## fy9-energia-s1

### a)
**Given:** average power of the fridge $P_1 = 45\,\text{W}$ for the whole day, $t_1 = 24\,\text{h}$; six LED lamps, each $7.0\,\text{W}$, time $t_2 = 5.0\,\text{h}$; coffee maker $P_3 = 1.0\,\text{kW}$, time $t_3 = 15\,\text{min}$
**Find:** the electrical energy $E_\text{need}$ used by the devices in a day, in kilowatt-hours
**Principle:** Each device transforms energy at its own power, so its energy is power multiplied by the time of use (chapter *Power*). The power of the fridge is an average power, so it too is multiplied by the whole day. The energies are added up in the same unit.
**Formula:** $E = P\,t$ for each device, so $E_\text{need} = P_1 t_1 + 6\,P_2 t_2 + P_3 t_3$
**Conversions:** For kilowatt-hours the powers to kilowatts and the times to hours: $45\,\text{W} = 45 \cdot 0.001\,\text{kW} = 0.045\,\text{kW}$, $7.0\,\text{W} = 0.0070\,\text{kW}$ and $15\,\text{min} = 15 \cdot \tfrac{1}{60}\,\text{h} = 0.25\,\text{h}$.
**Substitution:** $$
\begin{aligned}
E_\text{need} &= 0.045\,\text{kW} \cdot 24\,\text{h} \\
&+ 6 \cdot 0.0070\,\text{kW} \cdot 5.0\,\text{h} \\
&+ 1.0\,\text{kW} \cdot 0.25\,\text{h} \\
&= 1.08\,\text{kWh} \\
&+ 0.21\,\text{kWh} \\
&+ 0.25\,\text{kWh} \\
&= 1.54\,\text{kWh}
\end{aligned}
$$
**Answer:** $E_\text{need} \approx 1.5\,\text{kWh}$, that is, $1.54 \cdot 3.6\,\text{MJ} \approx 5.5\,\text{MJ}$, two significant figures like the power of the fridge $45\,\text{W}$ and the power of the coffee maker $1.0\,\text{kW}$.
**Reasonableness:** The fridge uses about $70\,\%$ of the energy, even though its power is the second smallest of the devices: it is on all the time. The large power of the coffee maker matters little, because it is on for only a quarter of an hour. One and a half kilowatt-hours a day is a usual consumption for a small summer cottage.

### b)
**Given:** from part a $E_\text{need} = 1.54\,\text{kWh}$; efficiency of the battery $\eta_\text{batt} = 90\,\%$, of the inverter $\eta_\text{inv} = 93\,\%$; production on a cloudy day $1.5\,\text{kWh}$
**Find:** the daily production $E_\text{panels}$ needed from the panels, and whether the production of a cloudy day is enough
**Principle:** Energy travels from the panels through the battery and the inverter to the devices. The stages are in series: the energy given by the battery is the energy taken in by the inverter. So the efficiency of the chain is the product of the efficiencies of the stages, and the panels must produce more than the devices use (chapter *Energy production and the efficiency of power plants*).
**Formula:** $\eta = \eta_\text{batt}\,\eta_\text{inv} = \dfrac{E_\text{need}}{E_\text{panels}}$, so $E_\text{panels} = \dfrac{E_\text{need}}{\eta_\text{batt}\,\eta_\text{inv}}$
**Conversions:** $90\,\% = 0.90$ and $93\,\% = 0.93$. The energies stay in kilowatt-hours.
**Substitution:** $E_\text{panels} = \dfrac{1.54\,\text{kWh}}{0.90 \cdot 0.93} = \dfrac{1.54\,\text{kWh}}{0.837} = 1.84\,\text{kWh}$. On a cloudy day $0.837 \cdot 1.5\,\text{kWh} = 1.26\,\text{kWh}$ reaches the devices.
**Answer:** The panels must produce about $1.8\,\text{kWh}$ a day (two significant figures like the need in part a). The $1.5\,\text{kWh}$ of a cloudy day is not enough: only about $1.3\,\text{kWh}$ of it reaches the devices, so the missing part is taken from the battery if it holds a surplus from a sunny day.
**Reasonableness:** The efficiency of the chain, $0.84$, is smaller than that of either stage, as it must be in a multiplication, and the need grows by about a fifth. On a sunny day $$
0.837 \cdot 5.4\,\text{kWh} \approx 4.5\,\text{kWh}
$$ reaches the devices, which is enough for almost three days.

### c)
**Find:** whether the neighbour's conclusion about the panels' daily energy is correct
**Principle:** Power tells how fast energy is transformed, and energy is power multiplied by time (chapter *Power*). The rated power of a panel is the maximum power it gives in bright sunshine.
**Model answer:** The claim is wrong, because it mixes up power and energy. The kilowatt is a unit of power and the kilowatt-hour a unit of energy: $1.2\,\text{kW}$ means that the panels can produce at most $1.2\,\text{kWh}$ *per hour*. The day's energy is the average power multiplied by the time, and it depends on how long and how strongly the sun shines.

According to the data, on a sunny day the panels produced $5.4\,\text{kWh}$, which corresponds to $5.4\,\text{kWh} : 1.2\,\text{kW} = 4.5$ hours at full power. On a cloudy day the production of $1.5\,\text{kWh}$ corresponded to only about one hour. The neighbour's number happens to be close to the cloudy day, but the reasoning is wrong.

### Yleisiä virheitä
- The average power of the fridge is multiplied by only a few hours, because the compressor does not run all the time; the average power already takes this into account.
- $15\,\text{min}$ is written as $0.15\,\text{h}$; correctly $15 \cdot \tfrac{1}{60}\,\text{h} = 0.25\,\text{h}$.
- In part b the need is multiplied by the efficiencies, which gives a panel production smaller than the need.
- The losses of the efficiencies are added up ($10\,\% + 7\,\% = 17\,\%$); here the result is close to the correct one, but the principle is wrong.

### Hyväksytään myös
- The energy of part a in joules: $$
\begin{aligned}
E_\text{need} &= 1.54 \cdot 3.6\,\text{MJ} \\
&\approx 5.5\,\text{MJ}
\end{aligned}
$$.

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
**Model answer:** Heat must in any case be removed from the steam cycle in the condenser when the plant produces electricity. In winter this heat warms district heating water and counts as useful, so the overall efficiency is about $90\,\%$. In summer district heat is needed only for tap water, so most of the condenser's heat must be given off to the surroundings, for example to cooling water, as waste heat.

If the electrical power stays at $30\,\text{MW}$, about the same amount of fuel is still used, but less of it is useful, and the overall efficiency falls towards the electrical efficiency. That is why a combined heat and power plant is run according to the heat demand: in summer at a lower power or not at all, and the electricity is produced elsewhere.

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
**Reasonableness:** According to the model, heating is needed at outdoor temperatures below about $17\,{}^\circ\text{C}$ (part d). When it is $-20\,{}^\circ\text{C}$ outside, the heating power is about $$
\begin{aligned}
&36.5\,\text{K} \cdot 0.204\,\text{kW}/\text{K} \\
&\approx 7.5\,\text{kW}
\end{aligned}
$$, the same as $$
\begin{aligned}
&(191 - 12)\,\text{kWh} : 24\,\text{h} \\
&\approx 7.5\,\text{kW}
\end{aligned}
$$, which suits the electric heating of a detached house. The least-squares line gives the same: $-4.89\,\text{kWh}$ per degree, that is, $204\,\text{W/K}$.

### c)
**Given:** the line of part a, the slope of part b $k = -4.9\,\text{kWh}$ per degree and the point of the line $(T_0;\ E_0) = (0\,{}^\circ\text{C};\ 93\,\text{kWh})$; the temperature to estimate $T = -28\,{}^\circ\text{C}$
**Find:** the daily consumption $E$ in kilowatt-hours and the reliability of the estimate
**Principle:** The line is a model of the consumption. A value outside the measured range is obtained by extending the line, that is, by extrapolating, which is justified only if the same model also holds there.
**Reading the graph:** From the line extended as a dashed line, about $230\,\text{kWh}$ is read at the temperature $-28\,{}^\circ\text{C}$.
**Formula:** $E = E_0 + k\,(T - T_0)$, where $(T_0;\ E_0)$ is a known point of the line and $k$ its slope
**Conversions:** Not needed: the temperature and the slope are in the same units as in the graph.
**Substitution:** $$
\begin{aligned}
E &= 93\,\text{kWh} \\
&+ (-4.9\,\text{kWh}/{}^\circ\text{C}) \\
&\cdot (-28\,{}^\circ\text{C} - 0\,{}^\circ\text{C}) \\
&= 93\,\text{kWh} + 137.2\,\text{kWh} \\
&= 230.2\,\text{kWh}
\end{aligned}
$$
**Answer:** about $230\,\text{kWh}$ a day, two significant figures like the slope. The estimate is an extrapolation $9\,\text{K}$ beyond the coldest measurement, $-19\,{}^\circ\text{C}$. It holds if the heat losses keep growing in direct proportion to the temperature difference; a strong wind increases the consumption, and if the combined power of the heaters is below about $9\,\text{kW}$, they are not enough and the indoor temperature falls.
**Reasonableness:** The consumption is roughly two and a half times the consumption at zero degrees, and the average power $230\,\text{kWh} : 24\,\text{h} \approx 9.6\,\text{kW}$ is at the upper end of the electric heating of a detached house. At an example price of $0.20\,\text{€/kWh}$ the day would cost about $46\,\text{€}$.

### d)
**Find:** the outdoor temperature at which, according to the model, no heating is needed, and why it is not $21\,{}^\circ\text{C}$
**Principle:** When no heating is needed, the consumption is just the other electricity consumption, $E_\text{other} = 12\,\text{kWh}$, so from the line $E = E_0 + kT$ we solve $T = \dfrac{E_\text{other} - E_0}{k}$. Energy is conserved: all the electrical energy used indoors finally becomes internal energy of the house, and the people and solar radiation also bring energy into the house (chapter *Forms of energy and conservation of energy*).
**Model answer:** From the extended line we read that the consumption falls to the level of the other consumption, $12\,\text{kWh}$, at about $16$–$17\,{}^\circ\text{C}$ ($T = \dfrac{E_\text{other} - E_0}{k} = \dfrac{12\,\text{kWh} - 93\,\text{kWh}}{-4.9\,\text{kWh}/{}^\circ\text{C}} = 16.5\,{}^\circ\text{C}$ from the equation of the line). So the house needs heating only when it is colder outside. The temperature is about $4\,\text{K}$ below the indoor temperature $21\,{}^\circ\text{C}$, because the electrical energy of lighting, cooking and appliances becomes internal energy in the house.

In addition, the residents warm the house, and solar radiation through the windows adds energy. These make up for the heat losses of a small temperature difference, so the heaters are needed only to cover the rest. The result is indicative: it is based on a line of winter days extended far beyond the measured range, and the data do not separate the sun and the wind.

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
**Model answer:** The average power of the wind turbines is $P_\text{avg} = k\,N\,P_\text{nom}$ and the energy in a year $E = P_\text{avg}\,t$, where the average is the share $k = 0.30$ of the nominal power, there are $N = 2$ turbines and the nominal power is $P_\text{nom} = 1.0\,\text{MW}$. The average power is $0.30 \cdot 2 \cdot 1.0\,\text{MW} = 0.60\,\text{MW}$, so in a year they produce $0.60\,\text{MW} \cdot 8760\,\text{h} \approx 5.3\,\text{GWh}$. That is more than the island's consumption of $3.0\,\text{GWh}$, so the first part of the claim holds for the year's energy.

Electricity, however, cannot be used at the time it is produced on average over the year: in calm weather the wind turbines produce nothing. A full battery covers the winter peak consumption for only $2.0\,\text{MWh} : 1.2\,\text{MW} \approx 1.7$ hours, and a calm frosty period can last for days. So the diesel plant cannot be dismantled unless the island gets other dispatchable power or a connection to the mainland grid.

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
**Model answer:** The consumption in kilowatt-hours is $3.0\,\text{GWh} = 3.0 \cdot 10^{6}\,\text{kWh}$, so the emissions of the diesel power plant are $$
\begin{aligned}
m &= e \cdot E \\
&= 700\,\text{g}/\text{kWh} \cdot 3.0 \\
&\cdot 10^{6}\,\text{kWh} \\
&= 2.1 \cdot 10^{9}\,\text{g}
\end{aligned}
$$. Substituting $1\,\text{g} = 10^{-6}\,\text{t}$: the emissions are about $2100\,\text{t}$ of carbon dioxide a year. A wind turbine burns nothing in operation, but manufacturing its steel and concrete, transporting it, building it and dismantling it cause emissions.

So its life-cycle emission factor is a few tens of grams per kilowatt-hour or less, not zero. The claim is therefore inaccurate: wind power is low-emission, and its emissions are only a fraction of the emissions of diesel, but it is not completely emission-free.

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
**Substitution:** $$
\begin{aligned}
E_\text{p} &= 1000\,\text{kg}/\text{m}^3 \cdot 7.50 \\
&\cdot 10^{4}\,\text{m}^3 \cdot 9.81\,\text{m}/\text{s}^2 \\
&\cdot 1200\,\text{m} \\
&= 8.829 \cdot 10^{11}\,\text{J} \\
&= \dfrac{8.829 \cdot 10^{11}}{3.6 \cdot 10^{9}}\,\text{MWh} \\
&= 245.3\,\text{MWh}
\end{aligned}
$$
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
**Reasonableness:** A check with the energies: $$
\begin{aligned}
&E_\text{el} : E_\text{grid} \\
&= 215.8\,\text{MWh} : 288.5\,\text{MWh} \\
&= 0.748
\end{aligned}
$$, the same as the product of the efficiencies. About a quarter of the energy becomes internal energy in the pipes, the pump, the turbine and the generators, which is typical of pumped-storage plants.

### d)
**Find:** whether the claim “the plant produces $216\,\text{MWh}$ of electricity every day” holds, and why the plant can still be useful
**Principle:** Energy is conserved: as electricity the plant can give at most the energy stored in it by pumping, and because of the losses less (chapter *Forms of energy and conservation of energy*). A store shifts energy in time (chapter *Transferring energy: electricity and heat*).
**Model answer:** The claim is misleading. A pumped-storage plant does not produce energy but stores it: in each filling and emptying it takes about $289\,\text{MWh}$ from the grid and gives back about $216\,\text{MWh}$, so about $73\,\text{MWh}$ becomes internal energy, which is transferred to the surroundings as heat. The plant is still useful, because it shifts energy in time.

It is filled when electricity is plentiful and cheap, for example on a windy night, and emptied at the time of peak consumption or in calm weather, when electricity is scarce. As hydropower it is also quickly controllable power, which weather-dependent wind power needs alongside it. A correct wording would be: “The plant gives $216\,\text{MWh}$ to the grid from the $289\,\text{MWh}$ it took, later, when electricity is needed.”

### Yleisiä virheitä
- In part a the mass is calculated directly from the volume without the density, or the kilometres are not converted to metres.
- The joules are converted to megawatt-hours by dividing by $3600$ or by $10^{6}$, but not by both.
- In part c the potential energy is multiplied by the efficiency of the pump, so the energy taken from the grid would be smaller than the energy stored in the water.
- The overall efficiency is calculated as the mean $(85\,\% + 88\,\%) : 2$ or as a sum and not as a product.

### Hyväksytään myös
- The energy of part c to three significant figures, $289\,\text{MWh}$, and the overall efficiency $74.8\,\%$.

## fy9-energia-s7

### a)
**Given:** from the chart of the source (checked 16 Nov 2026) the stated range $s_\text{stated}$ and the measured range $s_\text{meas}$ of three cars: Hyundai Inster $360\,\text{km}$ and $256\,\text{km}$, Tesla Model Y $629\,\text{km}$ and $359\,\text{km}$, Lucid Air $960\,\text{km}$ and $520\,\text{km}$. If you chose other cars from the chart, your numbers are different, but the method is the same.
**Find:** by how many per cent the measured range deviates from the stated one, and what the comparison shows
**Principle:** A relative difference tells how large a part of the reference value the difference is. The reference value is the stated range, because the deviation from it is asked. The difference is negative when the measured distance is shorter than the stated one.
**Formula:** The difference is $\Delta s = s_\text{meas} - s_\text{stated}$, and the relative difference is $\dfrac{\Delta s}{s_\text{stated}} = \dfrac{s_\text{meas} - s_\text{stated}}{s_\text{stated}}$
**Conversions:** The distances are in kilometres, so the units cancel. A decimal number is changed to per cent by multiplying by a hundred: $-0.289 = -28.9\,\%$.
**Substitution:** Hyundai Inster: $$
\begin{aligned}
\dfrac{\Delta s}{s_\text{stated}} &= \dfrac{256\,\text{km} - 360\,\text{km}}{360\,\text{km}} \\
&= \dfrac{-104\,\text{km}}{360\,\text{km}} \\
&= -0.289
\end{aligned}
$$
Tesla Model Y: $$
\begin{aligned}
\dfrac{\Delta s}{s_\text{stated}} &= \dfrac{359\,\text{km} - 629\,\text{km}}{629\,\text{km}} \\
&= \dfrac{-270\,\text{km}}{629\,\text{km}} \\
&= -0.429
\end{aligned}
$$
Lucid Air: $$
\begin{aligned}
\dfrac{\Delta s}{s_\text{stated}} &= \dfrac{520\,\text{km} - 960\,\text{km}}{960\,\text{km}} \\
&= \dfrac{-440\,\text{km}}{960\,\text{km}} \\
&= -0.458
\end{aligned}
$$
**Answer:** The measured range was $28.9\,\%$ shorter than the stated one for the Hyundai Inster, $42.9\,\%$ for the Tesla Model Y and $45.8\,\%$ for the Lucid Air, that is, about $29\,\%$, $43\,\%$ and $46\,\%$.

Three significant figures match the distances read from the chart, and whole per cents are enough for the comparison. The comparison shows that every car drove a clearly shorter distance in the frost than stated and that the deviation varied from car to car from about $30\,\%$ to almost a half.
**Reasonableness:** The mean of the deviations of the three cars is $39.2\,\%$, close to the average of all the cars given by the source, $38\,\%$. One of the chosen cars is below the average and two are above it, as it should be when both short-range and long-range cars are included.

### b)
**Given:** usable battery energy $E = 75\,\text{kWh}$, range in mild weather $s = 450\,\text{km}$, reference distance $s_{100} = 100\,\text{km}$; from the source (checked 16 Nov 2026) the average loss of range $38\,\%$
**Find:** the energy the car uses on a hundred kilometres in mild weather, $E_{100}$, and in frost, $E_{100,\text{c}}$; an assessment of the assumption that the battery gives the same energy
**Principle:** An average consumption means that the same amount of energy is used on every kilometre, so the energy used is directly proportional to the distance. Energy is conserved: the energy $E$ available from the battery is enough for the distance $s$ (chapter *Forms of energy and conservation of energy*). In frost the energy is assumed to be the same, but it is enough for a shorter distance $s_\text{c}$.
**Formula:** $\dfrac{E_{100}}{s_{100}} = \dfrac{E}{s}$, so $E_{100} = \dfrac{E\,s_{100}}{s}$. In frost the distance is $s_\text{c} = (1 - 0.38)\,s$ and $E_{100,\text{c}} = \dfrac{E\,s_{100}}{s_\text{c}}$.
**Conversions:** $38\,\% = 0.38$. The energy stays in kilowatt-hours and the distances in kilometres, so the kilometres cancel.
**Substitution:** $$
\begin{aligned}
E_{100} &= \dfrac{75\,\text{kWh} \cdot 100\,\text{km}}{450\,\text{km}} \\
&= 16.67\,\text{kWh} \\
s_\text{c} &= 0.62 \cdot 450\,\text{km} = 279\,\text{km} \\
E_{100,\text{c}} &= \dfrac{75\,\text{kWh} \cdot 100\,\text{km}}{279\,\text{km}} \\
&= 26.88\,\text{kWh}
\end{aligned}
$$
**Answer:** The consumption is about $17\,\text{kWh}$ in mild weather and about $27\,\text{kWh}$ in frost per hundred kilometres, two significant figures like the battery energy $75\,\text{kWh}$ and the loss $38\,\%$. The assumption does not hold exactly: a cold battery gives less energy than a warm one. Part of the loss of range therefore comes from the smaller energy and not from a larger consumption, so the real consumption grows less than the model gives.
**Reasonableness:** In the model the consumption grows by the factor $\tfrac{1}{0.62} \approx 1.6$, that is, by more than $38\,\%$, because the same energy is divided over a shorter distance. The measured consumptions of the source, $21.2\,\text{kWh}$ and $21.6\,\text{kWh}$ per hundred kilometres, are of the same order of magnitude but smaller than the model's $27\,\text{kWh}$.

The measured consumptions are, however, those of other cars than the model car, so they show only the order of magnitude. Energy per distance is also a force, because $W = Fs$: $$
\begin{aligned}
\dfrac{E}{s} &= \dfrac{75 \cdot 1000\,\text{W} \cdot 3600\,\text{s}}{450 \cdot 1000\,\text{m}} \\
&= 600\,\text{N}
\end{aligned}
$$
That is of the order of magnitude of the forces that resist a passenger car at highway speed.

### c)
**Find:** why the energy consumption of an electric car per kilometre grows in frost, explained with thermal physics, electricity and mechanics
**Principle:** Energy is conserved, and all the energy the car uses is taken from the same battery. Heat is transferred the faster the larger the temperature difference is (chapter *Heat transfer, energy balance and climate change*). The power of an electrical device is $P = UI$, and in a resistance the power $P = RI^2$ becomes internal energy (chapters *Electric power and the heating of a resistor* and *Electromotive force and internal resistance*). At a steady speed the motor does the work $W = Fs$ against the resistive forces (chapter *Air resistance and falling through air*).
**Model answer:** In frost the same battery gives energy to more uses, and the car moves against larger resistive forces.

- *Thermal physics.* Heat is transferred from the warm cabin and battery to the cold surroundings the faster the larger the temperature difference is. If the cabin is at $20\,{}^\circ\text{C}$, the difference to the outdoor air is $27\,\text{K}$ at Oslo's $-7\,{}^\circ\text{C}$ and $52\,\text{K}$ at Folldal's $-32\,{}^\circ\text{C}$, almost twice as large. Keeping the temperature takes heating power, and in an electric car it is taken from the traction battery. In a combustion-engine car the cabin is heated with the internal energy of the engine, which would otherwise be transferred as heat to the surroundings. The efficiency of an electric motor is high, so there is little such energy.
- *Electricity.* The heater takes the power $P = UI$ from the battery for the whole drive, so it uses the energy $E = Pt$. If the heating power is for example $3.0\,\text{kW}$ and the drive lasts $5.0\,\text{h}$, the heating takes $15\,\text{kWh}$, a fifth of the $75\,\text{kWh}$ battery. In addition, the internal resistance $R_\text{s}$ of a cold battery is larger. Inside the battery the power $P = R_\text{s}I^2$ becomes internal energy, and the voltage drop $R_\text{s}I$ across the internal resistance lowers the terminal voltage. Less energy is therefore available from the battery.
- *Mechanics.* At a steady speed the motor has to do the work $W = Fs$ against the resistive forces, so the larger the resistive forces are, the more energy is used on a kilometre. Cold air is denser: by the ideal gas law $pV = nRT$ the amount of substance per volume at the same pressure is $\tfrac{n}{V} = \tfrac{p}{RT}$, that is, about $16\,\%$ larger at $-20\,{}^\circ\text{C}$ than at $+20\,{}^\circ\text{C}$. The car then pushes aside a larger mass of air on every metre, so the air resistance is larger. Snow, slush and soft winter tyres increase the rolling resistance.

The energy used for heating and the energy that becomes internal energy of the battery, as well as the larger work against the resistive forces, are all taken from the same battery. Every kilometre therefore takes more energy from the battery than in mild weather, and less energy is available from a cold battery, so the range shrinks.

### d)
**Find:** why the largest deviation of the car that drove the furthest does not show that the car withstands frost worse than the others
**Principle:** Two measurement results can be compared only if they were measured in the same conditions. If the conditions change together with the object studied, the difference does not tell which of them caused it (chapter *Measuring and the reliability of a measurement*).
**Model answer:** The cars did not drive in the same conditions. According to the source (checked 16 Nov 2026) the temperature fell along the route from about $-7\,{}^\circ\text{C}$ in Oslo to $-32\,{}^\circ\text{C}$ at Folldal. The short-range Hyundai Inster stopped already at a point where it was $-16\,{}^\circ\text{C}$, so it drove its whole distance in the milder first part of the route.

The Lucid Air drove $520\,\text{km}$, the furthest, so it drove a large part of its distance on the coldest section of the route and was in the frost the longest. Its heating took energy from the battery for the longest time and with the largest temperature difference. A large percentage therefore tells at least partly about the conditions and not only about the car. The cars cannot be ranked by how well they withstand frost by comparing the percentages directly.

### e)
**Find:** why one winter test is not enough to predict the range of a particular car in all winter conditions, and how the test could be improved
**Principle:** One measurement gives the result only in the conditions in which it was made. A reliable experiment changes one variable at a time, keeps the others constant and repeats the measurements, so that the size of the random variation is seen (chapter *Measuring and the reliability of a measurement*).
**Model answer:** The test is one drive on one route on one day, and there was one car of each model.

- *The conditions vary.* The consumption is affected by the temperature, the wind, the road surface (snow, slush or dry asphalt), the speed, the climbs of the route, the preheating of the battery and the cabin, the heating settings, the load and the driving style. On another winter day they are different. The source shows the size of the effect: in the test of 2025, in which the temperature was between $-6\,{}^\circ\text{C}$ and $+8\,{}^\circ\text{C}$, the average deviation was $18\,\%$, and now it was $38\,\%$.
- *The scatter is not known.* Each car was driven only once, so it is not known how much the result would vary if the same car drove the same route again. Different individual cars of the same model can also differ from each other.
- *A better test.* All the cars would be driven at the same temperature and at the same speed, for example by repeating the same loop or in a cold chamber, and the preheating and the cabin temperature would be the same for all. The measurement would be made at several temperatures and repeated. Then the range as a function of temperature and the scatter of the result would be obtained.

The test still gives a useful order of magnitude: in hard frost the range can be about a third or almost a half shorter than stated.

### Yleisiä virheitä
- In part a the difference is divided by the measured range. For the Inster this gives $\tfrac{104\,\text{km}}{256\,\text{km}} \approx 41\,\%$, which tells how much longer the stated distance is than the measured one.
- In part b the consumption in frost is calculated by multiplying $16.7\,\text{kWh}$ by $1.38$, which gives $23\,\text{kWh}$. The distance becomes $38\,\%$ shorter, so the energy is divided by the distance $0.62 \cdot 450\,\text{km}$.
- In part c the answer says that energy “disappears” or that it “turns into heat”. Energy is conserved: it becomes internal energy of the battery, the air and the tyres and is transferred as heat to the surroundings.
- In parts d and e the percentages are treated as permanent properties of the car, although the cars drove at different temperatures and only once.

### Hyväksytään myös
- In part a cars other than those of the table, when the values are read from the chart of the source and the calculation is correct; the results can be given as whole per cents and as positive numbers when the answer says that the measured distance is shorter.
- The results of part b to three significant figures, $16.7\,\text{kWh}$ and $26.9\,\text{kWh}$ per hundred kilometres.
- In part c also other justified reasons, for example the larger friction of cold lubricant in the drivetrain.

## fy9-energia-s8

### a)
**Given:** from the figure, potential and kinetic energy: A $E_\text{p} = 700\,\text{J}$, $E_\text{k} = 0\,\text{J}$; B $E_\text{p} = 300\,\text{J}$, $E_\text{k} = 300\,\text{J}$; C $E_\text{p} = 0\,\text{J}$, $E_\text{k} = 500\,\text{J}$
**Find:** the increase of internal energy $\Delta E_\text{int}$ from A to B and from A to C
**Principle:** On a track with friction the mechanical energy is not conserved: friction increases the internal energy of the track and the wheels. The total energy is conserved, so the decrease of the mechanical energy is the increase of the internal energy (chapter *Forms of energy and conservation of energy*).
**Reading the graph:** At each point both the potential-energy bar and the kinetic-energy bar are read with the help of the grid (grid spacing $100\,\text{J}$).
**Formula:** $E_\text{mech} = E_\text{p} + E_\text{k}$ and $\Delta E_\text{int} = E_\text{mech,A} - E_\text{mech}$
**Conversions:** None needed.
**Substitution:** $$
\begin{aligned}
E_\text{mech,A} &= 700\,\text{J} + 0\,\text{J} = 700\,\text{J} \\
E_\text{mech,B} &= 300\,\text{J} + 300\,\text{J} = 600\,\text{J} \\
E_\text{mech,C} &= 0\,\text{J} + 500\,\text{J} = 500\,\text{J} \\
\Delta E_\text{int,AB} &= 700\,\text{J} - 600\,\text{J} = 100\,\text{J} \\
\Delta E_\text{int,AC} &= 700\,\text{J} - 500\,\text{J} = 200\,\text{J}
\end{aligned}
$$
**Answer:** $100\,\text{J}$ of internal energy has been produced from A to B and $200\,\text{J}$ from A to C.
**Reasonableness:** The mechanical energy decreases from point to point ($700\,\text{J}$, $600\,\text{J}$, $500\,\text{J}$) and never grows, as on a track with friction it should. About the same amount of internal energy is produced on each part of the way, which fits a steady effect of friction on the track.

### b)
**Given:** $E_\text{k,C} = 500\,\text{J}$ from the figure, mass $m = 45\,\text{kg}$
**Find:** the speed $v$ at point C
**Principle:** At the bottom the potential energy is zero, so the kinetic energy in the figure gives the speed (chapter *Kinetic energy, potential energy and mechanical energy*).
**Reading the graph:** At point C only the kinetic-energy bar is visible, and it ends at $500\,\text{J}$.
**Formula:** $E_\text{k} = \tfrac{1}{2}mv^2$, so $v = \sqrt{\dfrac{2E_\text{k}}{m}}$
**Conversions:** None needed, since $1\,\text{J} = 1\,\text{kg}\,\text{m}^2/\text{s}^2$.
**Substitution:** $$
\begin{aligned}
v &= \sqrt{\dfrac{2 \cdot 500\,\text{J}}{45\,\text{kg}}} \\
&= \sqrt{22.2\,\text{m}^2/\text{s}^2} \\
&\approx 4.7\,\text{m/s}
\end{aligned}
$$
**Answer:** The speed at point C is $v \approx 4.7\,\text{m/s}$, two significant figures like the mass.
**Reasonableness:** $4.7\,\text{m/s} \approx 17\,\text{km/h}$ is a sensible speed at the bottom of a half-pipe.

### c)
**Given:** the increase of internal energy $\Delta E_\text{int,AC} = 200\,\text{J}$ from part a, distance $s = 3.4\,\text{m}$, mass $m = 45\,\text{kg}$
**Find:** the average force of friction $F$
**Principle:** The work done by friction equals the increase of internal energy, and work is force times distance in the direction of the force (chapter *Conservation of mechanical energy and the work-energy principle*). The average force is obtained by dividing the work by the distance travelled.
**Formula:** $\Delta E_\text{int} = Fs$, so $F = \dfrac{\Delta E_\text{int}}{s}$
**Conversions:** None needed, since $1\,\text{J} = 1\,\text{N} \cdot \text{m}$.
**Substitution:** $$
\begin{aligned}
F &= \dfrac{200\,\text{J}}{3.4\,\text{m}} \\
&\approx 59\,\text{N}
\end{aligned}
$$
**Answer:** The average force of friction is $F \approx 59\,\text{N}$, two significant figures like the distance.
**Reasonableness:** The weight is $G = mg = 45\,\text{kg} \cdot 9.81\,\text{m/s}^2 \approx 440\,\text{N}$, so friction is about $13\,\%$ of the weight, a sensible size for the rolling resistance and bearing friction of a board on wheels.

### d)
**Given:** $E_\text{p,A} = 700\,\text{J}$ from the figure, $m = 45\,\text{kg}$
**Find:** the speed $v_0$ at C without friction, and the reason why the real speed is smaller
**Principle:** Without friction the mechanical energy is conserved: all the original potential energy turns into kinetic energy (chapter *Forms of energy and conservation of energy*).
**Reading the graph:** At point A all the energy is potential energy, $700\,\text{J}$.
**Formula:** $E_\text{k,C} = E_\text{p,A}$, so $\tfrac{1}{2}mv_0^2 = E_\text{p,A}$ and $v_0 = \sqrt{\dfrac{2E_\text{p,A}}{m}}$
**Conversions:** None needed.
**Substitution:** $$
\begin{aligned}
v_0 &= \sqrt{\dfrac{2 \cdot 700\,\text{J}}{45\,\text{kg}}} \\
&= \sqrt{31.1\,\text{m}^2/\text{s}^2} \\
&\approx 5.6\,\text{m/s}
\end{aligned}
$$
**Answer:** Without friction the speed would be $v_0 \approx 5.6\,\text{m/s}$. The real speed $4.7\,\text{m/s}$ is smaller because friction turns part of the energy, $200\,\text{J}$ or $\tfrac{200}{700} \approx 29\,\%$, into internal energy of the track and the wheels. It is transferred to the surroundings as heat. Only $500\,\text{J}$ of kinetic energy remains.
**Reasonableness:** Without friction the speed is greater than with friction, as it should be. The speed decreases by only about $0.9\,\text{m/s}$ although nearly a third of the energy is used, because the speed depends on the square root of the energy.

### Yleisiä virheitä
- In part a only the kinetic energy is read and the potential energy is forgotten, so B gets $700\,\text{J} - 300\,\text{J} = 400\,\text{J}$ wrongly.
- In part b the energy of point A, $700\,\text{J}$, is used, or the square root and the factor $2$ are forgotten.
- In part c the internal energy is divided by the height difference instead of the distance, or the energy in joules is given as the force.
- In part d the energy is said to "disappear" or "turn into heat": it turns into internal energy, which is transferred to the surroundings as heat.

### Hyväksytään myös
- In part c the force to three significant figures, $58.8\,\text{N}$, and in part d the speeds to three significant figures, $4.71\,\text{m/s}$ and $5.58\,\text{m/s}$.
- In part a an answer read directly from the sums of the bars of the figure, when the sums of the mechanical energies are shown.

## fy9-energia-s9

### a)
**Given:** from the graph A $E_\text{A} = 120\,\text{kJ}$ and B $E_\text{B} = 40\,\text{kJ}$ at the time $t = 80\,\text{s}$; both lines pass through the origin
**Find:** the electrical powers $P_\text{A}$ and $P_\text{B}$
**Principle:** When energy is transformed steadily, the power is constant and the energy is directly proportional to time. The power is the slope of the graph (chapter *Power*).
**Reading the graph:** A point far from the origin is read on each line, at $80\,\text{s}$: A $120\,\text{kJ}$ and B $40\,\text{kJ}$.
**Formula:** $P = \dfrac{\Delta E}{\Delta t}$
**Conversions:** $120\,\text{kJ} = 120\,000\,\text{J}$ and $40\,\text{kJ} = 40\,000\,\text{J}$; finally $1\,\text{W} = 0.001\,\text{kW}$.
**Substitution:** $$
\begin{aligned}
P_\text{A} &= \dfrac{120\,000\,\text{J}}{80\,\text{s}} = 1500\,\text{W} = 1.5\,\text{kW} \\
P_\text{B} &= \dfrac{40\,000\,\text{J}}{80\,\text{s}} = 500\,\text{W} = 0.50\,\text{kW}
\end{aligned}
$$
**Answer:** $P_\text{A} = 1.5\,\text{kW}$ and $P_\text{B} = 0.50\,\text{kW}$, two significant figures like the values read.
**Reasonableness:** A power of $1.5\,\text{kW}$ is typical of an electric radiator. A's line is three times as steep as B's, and its power is three times as large.

### b)
**Given:** the powers of part a, $P_\text{A} = 1.5\,\text{kW}$ and $P_\text{B} = 0.50\,\text{kW}$, time of use $t = 30 \cdot 3.0\,\text{h} = 90\,\text{h}$, price $p = 0.16\,\text{€/kWh}$
**Find:** the cost of electricity $C_\text{A}$ and $C_\text{B}$
**Principle:** Electrical energy is power times time, and the cost is energy times the unit price. The kilowatt-hour fits directly when the power is in kilowatts and the time in hours (chapter *Power*).
**Formula:** $E = Pt$ and $C = E\,p$, so $C = P\,t\,p$
**Conversions:** None needed, since the powers are in kilowatts and the times in hours.
**Substitution:** $$
\begin{aligned}
E_\text{A} &= 1.5\,\text{kW} \cdot 90\,\text{h} = 135\,\text{kWh} \\
C_\text{A} &= 135\,\text{kWh} \cdot 0.16\,\text{€/kWh} \approx 22\,\text{€} \\
E_\text{B} &= 0.50\,\text{kW} \cdot 90\,\text{h} = 45\,\text{kWh} \\
C_\text{B} &= 45\,\text{kWh} \cdot 0.16\,\text{€/kWh} = 7.2\,\text{€}
\end{aligned}
$$
**Answer:** The electricity of A costs about $22\,\text{€}$ and that of B $7.2\,\text{€}$, to two significant figures.
**Reasonableness:** The ratio of the costs is $22\,\text{€} : 7.2\,\text{€} \approx 3$, the same as the ratio of the powers, because the time of use and the price are the same. A monthly cost of tens of euros for a radiator is a familiar order of magnitude.

### c)
**Given:** mass $m = 150\,\text{kg}$, height $h = 20\,\text{m}$, electrical energy from the graph $E = 40\,\text{kJ}$ in $80\,\text{s}$; $g = 9.81\,\text{m/s}^2$
**Find:** the efficiency $\eta$ of motor B
**Principle:** Efficiency is the share of the energy taken in as electricity that is transformed into useful energy (chapter *Efficiency*). The useful energy is the change in the potential energy of the load in the lift.
**Reading the graph:** From B's line at $80\,\text{s}$ the reading is $E = 40\,\text{kJ}$.
**Formula:** $\eta = \dfrac{E_\text{useful}}{E}$, where $E_\text{useful} = mgh$, so $\eta = \dfrac{mgh}{E}$
**Conversions:** $40\,\text{kJ} = 40\,000\,\text{J}$.
**Substitution:** $$
\begin{aligned}
E_\text{useful} &= 150\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 20\,\text{m} \\
&\approx 29\,400\,\text{J} \\
\eta &= \dfrac{29\,400\,\text{J}}{40\,000\,\text{J}} \\
&= 0.74 = 74\,\%
\end{aligned}
$$
**Answer:** The efficiency of the motor is $\eta \approx 74\,\%$, to two significant figures.
**Reasonableness:** The efficiency is below $100\,\%$ and suits a lift motor whose gearbox and rope use some of the energy. The useful energy $29.4\,\text{kJ}$ is smaller than the $40\,\text{kJ}$ taken in.

### d)
**Given:** $P_\text{B} = 0.50\,\text{kW}$ from part a, $E_\text{useful} = 29\,400\,\text{J}$ and $t = 80\,\text{s}$ from part c
**Find:** the power transferred to the surroundings as heat, $P_\text{loss}$, and the form of energy into which the energy first changes
**Principle:** The power taken in divides into useful power and the rest. The rest of the energy does not disappear but turns into internal energy, which is transferred to the surroundings as heat (chapter *Efficiency*).
**Formula:** $P_\text{loss} = P - P_\text{useful}$, where $P_\text{useful} = \dfrac{E_\text{useful}}{t}$
**Conversions:** $P_\text{B} = 0.50\,\text{kW} = 500\,\text{W}$.
**Substitution:** $$
\begin{aligned}
P_\text{useful} &= \dfrac{29\,400\,\text{J}}{80\,\text{s}} \approx 368\,\text{W} \\
P_\text{loss} &= 500\,\text{W} - 368\,\text{W} \\
&\approx 130\,\text{W} = 0.13\,\text{kW}
\end{aligned}
$$
**Answer:** About $0.13\,\text{kW}$ is transferred to the surroundings as heat. The energy first turns into internal energy of the motor, the gearbox and the rope because of friction and electrical resistance, and it is transferred to the surroundings as heat.
**Reasonableness:** $0.13\,\text{kW} = 26\,\%$ of the power taken in, so $\eta + 26\,\% = 100\,\%$; energy is conserved.

### Yleisiä virheitä
- In part a the power is read from one value of the graph without dividing by the time, or kilojoules are used as joules.
- In part b the time of use is wrong ($3.0\,\text{h}$ instead of $90\,\text{h}$), or the power is left in watts and the cost is calculated with the price per kilowatt-hour.
- In part c the efficiency is calculated as $E / E_\text{useful}$ and comes out over $100\,\%$.
- In part d the energy is said to "disappear" or "turn into heat", although it is internal energy that is transferred as heat.

### Hyväksytään myös
- In part c the answer $73.6\,\%$ or $0.74$, and in part d $132\,\text{W}$.
- In part d the power can also be calculated from the efficiency: $$
\begin{aligned}
P_\text{loss} &= (1 - \eta)P \\
&= 0.26 \cdot 0.50\,\text{kW} \\
&\approx 0.13\,\text{kW}
\end{aligned}
$$.
