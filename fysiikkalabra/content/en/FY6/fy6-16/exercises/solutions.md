## fy6-16-L1-01
**Given:** energy of the battery when fully charged $W = 64\,\text{kWh}$, charge level rises from $15\,\%$ to $80\,\%$
**Find:** energy to be stored in the battery $W_\text{battery}$ in kilowatt-hours
**Principle:** The charge level tells what fraction of the full energy of the battery is stored in it. So the fraction of the full energy given by the difference of the charge levels has to be transferred to the battery.
**Formula:** $W_\text{battery} = (s_2 - s_1) W$, where $s_1$ and $s_2$ are the charge levels as decimal numbers
**Conversions:** $s_1 = 15\,\% = 0.15$ and $s_2 = 80\,\% = 0.80$
**Substitution:** $W_\text{battery} = (0.80 - 0.15) \cdot 64\,\text{kWh} = 0.65 \cdot 64\,\text{kWh} = 41.6\,\text{kWh}$
**Answer:** $42\,\text{kWh}$, two significant figures like the energy of the battery $64\,\text{kWh}$.
**Reasonableness:** Two thirds of the battery is about $\tfrac{2}{3} \cdot 64\,\text{kWh} \approx 43\,\text{kWh}$, and $65\,\%$ is a little less than two thirds. The result is smaller than the whole battery, as it should be.

## fy6-16-L1-02
**Given:** voltage $U = 230\,\text{V}$, charging current $I = 10\,\text{A}$
**Find:** charging power $P$ in kilowatts
**Principle:** A socket uses one phase, so the power is voltage times current, like the power of any single-phase device. The mains voltage $230\,\text{V}$ is the effective value of an alternating voltage, so it is used in the calculation like a direct voltage.
**Formula:** $P = UI$
**Conversions:** The result in watts is converted to kilowatts: $1\,\text{W} = 0.001\,\text{kW}$.
**Substitution:** $P = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W} = 2.3\,\text{kW}$
**Answer:** $2.3\,\text{kW}$, two significant figures like the current $10\,\text{A}$.
**Reasonableness:** The power is of the same order of magnitude as the power of a kettle, but charging takes hours. A $40\,\text{kWh}$ charge would take more than $17\,\text{h}$ at this power, so charging from a socket suits mainly emergencies or a cottage.

## fy6-16-L1-03
**Given:** power $P = 11\,\text{kW}$, three phases, phase voltage $U = 230\,\text{V}$
**Find:** current $I$ of one phase conductor in amperes
**Principle:** The station draws the same current from each of the three phase conductors, and each phase transfers a power $UI$. The total power is therefore three times the power of one phase.
**Formula:** $P = 3UI$, so $I = \dfrac{P}{3U}$
**Conversions:** $P = 11\,\text{kW} = 11\,000\,\text{W}$
**Substitution:** $I = \dfrac{11\,000\,\text{W}}{3 \cdot 230\,\text{V}} = \dfrac{11\,000\,\text{W}}{690\,\text{V}} = 15.94\,\text{A}$
**Answer:** $16\,\text{A}$, two significant figures like the power $11\,\text{kW}$.
**Reasonableness:** If the whole power flowed in one phase, the current would be $11\,000\,\text{W} : 230\,\text{V} \approx 48\,\text{A}$; divided between three phases it is a third of that. $16\,\text{A}$ is a common size for the circuit fuse of a charging station.

## fy6-16-L1-04
**Given:** energy taken from the grid $W_\text{grid} = 45\,\text{kWh}$, price $a = 14\,\text{c/kWh}$
**Find:** cost $K$ in euros
**Principle:** Charging is paid for by the energy taken from the grid, and every kilowatt-hour costs the same price. The cost is therefore the price times the energy.
**Formula:** $K = a W_\text{grid}$
**Conversions:** $a = 14\,\text{c/kWh} = 14 \cdot 0.01\,\text{€/kWh} = 0.14\,\text{€/kWh}$
**Substitution:** $K = 0.14\,\text{€/kWh} \cdot 45\,\text{kWh} = 6.30\,\text{€}$
**Answer:** $6.3\,\text{€}$, two significant figures like the energy $45\,\text{kWh}$ and the price $14\,\text{c/kWh}$.
**Reasonableness:** In cents $45 \cdot 14\,\text{c} = 630\,\text{c}$. At ten cents the price would be $4.50\,\text{€}$ and at fifteen $6.75\,\text{€}$, so the result is between them, close to the latter.

## fy6-16-L1-05
**Given:** energy taken from the grid $W_\text{grid} = 50\,\text{kWh}$, energy stored in the battery $W_\text{battery} = 44\,\text{kWh}$
**Find:** efficiency of charging $\eta$ as a percentage
**Principle:** The useful energy is the energy stored in the battery, and the energy taken is the energy taken from the grid. The efficiency is their ratio.
**Formula:** $\eta = \dfrac{W_\text{battery}}{W_\text{grid}}$
**Conversions:** Not needed: both energies are in kilowatt-hours, so the unit cancels. A decimal number is converted to a percentage by multiplying by a hundred.
**Substitution:** $\eta = \dfrac{44\,\text{kWh}}{50\,\text{kWh}} = 0.88 = 88\,\%$
**Answer:** $88\,\%$, two significant figures like the energies $44\,\text{kWh}$ and $50\,\text{kWh}$.
**Reasonableness:** The losses were $50\,\text{kWh} - 44\,\text{kWh} = 6\,\text{kWh}$, that is, $12\,\%$ of the energy taken; $88\,\% + 12\,\% = 100\,\%$. The efficiency is below $100\,\%$ and of the size typical of home charging.

## fy6-16-L2-01
**Given:** powers and times read from the graph
**Find:** energy taken from the grid $W_\text{grid}$ in kilowatt-hours
**Principle:** When the power is constant, the energy is power times time. In the graph the power is constant in two periods, so the energy is the sum of the areas of two rectangles.
**Reading the graph:** In the first period the power is $P_1 = 11\,\text{kW}$ for the time $0\text{–}2.0\,\text{h}$, so $t_1 = 2.0\,\text{h}$. In the second period the power is $P_2 = 5.5\,\text{kW}$ for the time $2.0\text{–}3.0\,\text{h}$, so $t_2 = 1.0\,\text{h}$. After that the power is zero.
**Formula:** $W_\text{grid} = P_1 t_1 + P_2 t_2$
**Conversions:** Not needed: with kilowatts and hours the energy comes out directly in kilowatt-hours.
**Substitution:** $W_\text{grid} = 11\,\text{kW} \cdot 2.0\,\text{h} + 5.5\,\text{kW} \cdot 1.0\,\text{h} = 22\,\text{kWh} + 5.5\,\text{kWh} = 27.5\,\text{kWh}$
**Answer:** $28\,\text{kWh}$, two significant figures like the values read from the graph.
**Reasonableness:** If the power had been $11\,\text{kW}$ for all three hours, $33\,\text{kWh}$ would have been taken; the halved power in the last hour reduces this by $5.5\,\text{kWh}$, so $33\,\text{kWh} - 5.5\,\text{kWh} = 27.5\,\text{kWh}$.

## fy6-16-L2-02
**Given:** $U = 230\,\text{V}$, $I = 16\,\text{A}$, one phase, energy of the battery $60\,\text{kWh}$, charge level $20\,\% \to 80\,\%$, $\eta = 90\,\%$
**Find:** charging time $t$ in hours
**Principle:** $60\,\%$ of its energy has to be transferred to the battery. The power is constant, so the energy taken from the grid is power times time, and the fraction given by the efficiency of it is stored in the battery. The power of a single-phase station is voltage times current.
**Formula:** $\eta P t = W_\text{battery}$ and $P = UI$, so $t = \dfrac{W_\text{battery}}{\eta U I}$
**Conversions:** $W_\text{battery} = (0.80 - 0.20) \cdot 60\,\text{kWh} = 36\,\text{kWh}$; $UI = 230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W} = 3.68\,\text{kW}$; $\eta = 0.90$
**Substitution:** $t = \dfrac{36\,\text{kWh}}{0.90 \cdot 3.68\,\text{kW}} = \dfrac{36\,\text{kWh}}{3.312\,\text{kW}} = 10.87\,\text{h}$
**Answer:** $11\,\text{h}$, two significant figures like the efficiency $90\,\%$.
**Reasonableness:** Estimate: about $3.3\,\text{kW}$ goes into the battery, and $33\,\text{kWh}$ would take $10\,\text{h}$; $36\,\text{kWh}$ takes a little more. With a three-phase $16\,\text{A}$ station the same charge would take a third, about $3.6\,\text{h}$.

## fy6-16-L2-03
**Given:** main fuses $3 \cdot 25\,\text{A}$, power of the heater $P_\text{heater} = 9.0\,\text{kW}$ on three phases, $U = 230\,\text{V}$
**Find:** greatest allowed current $I_\text{charger}$ of the charging station in one phase conductor
**Principle:** There is a main fuse in each phase conductor, and the currents through the same phase conductor are added (chapter *Kirchhoff's laws and potential in a circuit*). The heater draws the same current from each phase, so its current is obtained from the formula $P = 3UI$. What is left of the $25\,\text{A}$ remains for the car.
**Formula:** $I_\text{heater} + I_\text{charger} = I_\text{main}$ and $I_\text{heater} = \dfrac{P_\text{heater}}{3U}$, so $I_\text{charger} = I_\text{main} - \dfrac{P_\text{heater}}{3U}$, where $I_\text{main} = 25\,\text{A}$
**Conversions:** $P_\text{heater} = 9.0\,\text{kW} = 9000\,\text{W}$
**Substitution:** $I_\text{charger} = 25\,\text{A} - \dfrac{9000\,\text{W}}{3 \cdot 230\,\text{V}} = 25\,\text{A} - 13.04\,\text{A} = 11.96\,\text{A}$
**Answer:** $12\,\text{A}$, two significant figures like the current of the main fuse $25\,\text{A}$.
**Reasonableness:** The heater and the car together then draw $13\,\text{A} + 12\,\text{A} = 25\,\text{A}$ from each phase. The power of the car is about $3 \cdot 230\,\text{V} \cdot 12\,\text{A} \approx 8.3\,\text{kW}$, less than the $11\,\text{kW}$ of the station, so load management has to reduce the charging for the time of the sauna.

## fy6-16-L2-04
**Given:** length of cable $l = 30\,\text{m}$, cross-sectional area $A = 2.5\,\text{mm}^2$, current $I = 16\,\text{A}$, $\rho = 1.7 \cdot 10^{-8}\,\Omega\cdot\text{m}$
**Find:** voltage $U_\text{loss}$ lost in the cable in volts
**Principle:** The copper conductors of the cable are a resistor through which the charging current flows. The current goes to the station along the phase conductor and returns along the neutral conductor, so the length of copper is $2l$. By Ohm's law the voltage across a resistance is resistance times current.
**Formula:** $U_\text{loss} = RI$ and $R = \rho \dfrac{2l}{A}$, so $U_\text{loss} = \rho \dfrac{2l}{A} I$
**Conversions:** $A = 2.5\,\text{mm}^2 = 2.5 \cdot (10^{-3}\,\text{m})^2 = 2.5 \cdot 10^{-6}\,\text{m}^2$
**Substitution:** $U_\text{loss} = 1.7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \dfrac{2 \cdot 30\,\text{m}}{2.5 \cdot 10^{-6}\,\text{m}^2} \cdot 16\,\text{A} = 0.408\,\Omega \cdot 16\,\text{A} = 6.53\,\text{V}$
**Answer:** $6.5\,\text{V}$, two significant figures like the resistivity $1.7 \cdot 10^{-8}\,\Omega\cdot\text{m}$ and the cross-sectional area $2.5\,\text{mm}^2$.
**Reasonableness:** The loss is $6.5\,\text{V} : 230\,\text{V} \approx 3\,\%$ of the mains voltage, so the station still gets almost the whole voltage. A power of $6.5\,\text{V} \cdot 16\,\text{A} \approx 100\,\text{W}$ is dissipated in the cable, that is, about $3.5\,\text{W}$ per metre, which is spread over a long stretch.

## fy6-16-L3-01
**Given:** into the battery in a year $W_\text{battery} = 3000\,\text{kWh}$, efficiencies $\eta_1 = 82\,\%$ (socket) and $\eta_2 = 92\,\%$ (charging station), price $a = 15\,\text{c/kWh}$
**Find:** saving in a year $\Delta K$ in euros
**Principle:** The same energy goes into the battery either way, but the energy taken from the grid is the energy going into the battery divided by the efficiency. The saving comes from less being taken from the grid with the charging station, and it is paid at the same price.
**Formula:** $W_\text{grid} = \dfrac{W_\text{battery}}{\eta}$ and $K = a W_\text{grid}$, so $\Delta K = a \left(\dfrac{W_\text{battery}}{\eta_1} - \dfrac{W_\text{battery}}{\eta_2}\right)$
**Conversions:** $\eta_1 = 0.82$, $\eta_2 = 0.92$ and $a = 15\,\text{c/kWh} = 0.15\,\text{€/kWh}$
**Substitution:** $\Delta K = 0.15\,\text{€/kWh} \cdot \left(\dfrac{3000\,\text{kWh}}{0.82} - \dfrac{3000\,\text{kWh}}{0.92}\right) = 0.15\,\text{€/kWh} \cdot (3658.5\,\text{kWh} - 3260.9\,\text{kWh}) = 0.15\,\text{€/kWh} \cdot 397.7\,\text{kWh} = 59.7\,\text{€}$
**Answer:** $60\,\text{€}$, two significant figures like the efficiencies $82\,\%$ and $92\,\%$.
**Reasonableness:** The difference in efficiency is ten percentage points, so the energy taken from the grid differs by about $10\text{–}12\,\%$ of the annual consumption ($3260\,\text{kWh}$ or $3660\,\text{kWh}$), that is, by about $400\,\text{kWh}$. $400\,\text{kWh} \cdot 0.15\,\text{€/kWh} = 60\,\text{€}$. The saving is small compared with the price of a charging station; a more important reason for a charging station is safety.

## fy6-16-L3-02
**Given:** the current grows from $I_1 = 10\,\text{A}$ to $I_2 = 16\,\text{A}$, the resistance $R$ of the cable stays the same
**Find:** increase in the heating power as a percentage
**Principle:** By Joule's law the power dissipated in the cable is $RI^2$. When $R$ stays the same, the power is directly proportional to the square of the current, so the ratio of the powers is the square of the ratio of the currents.
**Formula:** $P = RI^2$, so $\dfrac{P_2}{P_1} = \dfrac{R I_2^2}{R I_1^2} = \left(\dfrac{I_2}{I_1}\right)^2$ and the increase is $\dfrac{P_2}{P_1} - 1$
**Conversions:** Not needed: the amperes cancel. The increase is converted to a percentage by multiplying by a hundred.
**Substitution:** $\dfrac{P_2}{P_1} = \left(\dfrac{16\,\text{A}}{10\,\text{A}}\right)^2 = 1.6^2 = 2.56$, so the increase is $2.56 - 1 = 1.56 = 156\,\%$
**Answer:** $156\,\%$; $10\,\text{A}$ and $16\,\text{A}$ are exact settings of the charging device, so $156\,\%$ is given as it was calculated.
**Reasonableness:** The current grows by $60\,\%$, but the power more than doubles, because the current is squared. If the current doubled, the power would become four times as great, that is, grow by $300\,\%$; $156\,\%$ is suitably between $60\,\%$ and $300\,\%$.

## fy6-16-L3-03
**Given:** energy to be stored in the battery $W_\text{battery} = 40\,\text{kWh}$, time $22.00\text{–}7.00$, $\eta = 90\,\%$, three phases, $U = 230\,\text{V}$
**Find:** smallest constant current $I$ in one phase conductor
**Principle:** The energy going into the battery divided by the efficiency has to be taken from the grid, and it has to be taken in the time available, so the power is at least the energy divided by the time. The power of a three-phase station is $P = 3UI$ when every phase carries the same current.
**Formula:** $\eta \cdot 3UI \cdot t = W_\text{battery}$, so $I = \dfrac{W_\text{battery}}{3 \eta U t}$
**Conversions:** $t = 7.00 - 22.00 = 9.0\,\text{h}$; $W_\text{battery} = 40\,\text{kWh} = 40\,000\,\text{Wh}$ so that the result comes out in amperes; $\eta = 0.90$
**Substitution:** $I = \dfrac{40\,000\,\text{Wh}}{3 \cdot 0.90 \cdot 230\,\text{V} \cdot 9.0\,\text{h}} = \dfrac{40\,000\,\text{Wh}}{5589\,\text{Vh}} = 7.157\,\text{A}$
**Answer:** $7.2\,\text{A}$, two significant figures like the energy $40\,\text{kWh}$ and the efficiency $90\,\%$.
**Reasonableness:** $40\,\text{kWh} : 0.90 \approx 44\,\text{kWh}$ is taken from the grid, which in nine hours requires about $4.9\,\text{kW}$; $4900\,\text{W} : 690\,\text{V} \approx 7\,\text{A}$. The current is less than half of the $16\,\text{A}$ of the station, so slow overnight charging leaves room for the sauna and other loads.
