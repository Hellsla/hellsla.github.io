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

## fy6-16-L1-06
**Find:** what the kilowatt figure of the station and the kilowatt-hour figure of the battery tell.
**Principle:** Power tells how fast energy is transferred, and its unit is the kilowatt. Energy is obtained by multiplying power by time, $W = Pt$, so its unit is kilowatt times hour, that is, the kilowatt-hour. The charging speed is therefore power, and the size of the battery is energy.
**Model answer:** The kilowatt figure of the station tells the charging speed, that is, the power, and the kilowatt-hour figure of the battery tells how much energy fits in the battery. The claim that the figures are the wrong way round is false, because the kilowatt-hour is a unit of energy and speed cannot be measured with it. The claim that the units are the same thing is false, because the kilowatt-hour is obtained by multiplying the kilowatt by time. The claim that the kilowatt is voltage and the kilowatt-hour is current is false, because voltage is measured in volts and current in amperes. For example, a station of $11\,\text{kW}$ transfers $11\,\text{kWh}$ in an hour.

## fy6-16-L1-07
**Given:** power $P = 7.4\,\text{kW}$, charging time $t = 5.5\,\text{h}$
**Find:** energy taken from the grid $W_\text{grid}$ in kilowatt-hours
**Principle:** The power is constant, so the energy is power times time (chapter *Electrical energy at home*). We calculate the energy taken from the grid, so the efficiency is not needed.
**Formula:** $W_\text{grid} = Pt$
**Conversions:** Not needed: kilowatts times hours gives kilowatt-hours directly.
**Substitution:** $W_\text{grid} = 7.4\,\text{kW} \cdot 5.5\,\text{h} = 40.7\,\text{kWh}$
**Answer:** $41\,\text{kWh}$, two significant figures like the power $7.4\,\text{kW}$ and the time $5.5\,\text{h}$.
**Reasonableness:** Estimate: $7\,\text{kW}$ for six hours is $42\,\text{kWh}$, and the result is a little smaller because the power and the time are a little smaller. It is of the same order of magnitude as the energy of the battery of a typical electric car.

## fy6-16-L1-08
**Given:** resistance $R = 0.25\,\Omega$, current $I = 16\,\text{A}$
**Find:** heating power of the cable $P$ in watts
**Principle:** When a current flows through a resistance, electrical energy is converted into internal energy at the power given by Joule's law. The power depends on the square of the current and on the resistance.
**Formula:** $P = RI^2$
**Conversions:** Not needed: ohms and amperes give watts directly.
**Substitution:** $P = 0.25\,\Omega \cdot (16\,\text{A})^2 = 0.25\,\Omega \cdot 256\,\text{A}^2 = 64\,\text{W}$
**Answer:** $64\,\text{W}$, two significant figures like the resistance $0.25\,\Omega$.
**Reasonableness:** The voltage drop is $RI = 0.25\,\Omega \cdot 16\,\text{A} = 4.0\,\text{V}$, and the power is the voltage drop times the current, $4.0\,\text{V} \cdot 16\,\text{A} = 64\,\text{W}$. The result is small compared with the power of the station, but in a cable it is enough to heat it.

## fy6-16-L2-05
**Given:** power of the house hour by hour from the table, main fuses $3 \cdot 25\,\text{A}$, $U = 230\,\text{V}$, three-phase station
**Find:** a) the peak power and its time, b) the largest charging power of the station $P_\text{s}$ during the peak in kilowatts, c) when $11\,\text{kW}$ is allowed
**Principle:** The main fuse limits the current of each phase conductor, and the loads are divided equally between the phases, so the power of the whole house can be at most $3UI_\text{f}$. The powers of the house and the station are added, and what the house does not use is left for the station.
**Reading the graph:** From the table the largest power is $6.8\,\text{kW}$ at $19\text{–}20$.
**Formula:** $P_\text{max} = 3UI_\text{f}$ and $P_\text{house} + P_\text{s} \le P_\text{max}$, so $P_\text{s} = 3UI_\text{f} - P_\text{house}$, where $I_\text{f} = 25\,\text{A}$
**Conversions:** $3UI_\text{f}$ is calculated in watts and converted to kilowatts: $17\,250\,\text{W} = 17.25\,\text{kW}$.
**Substitution:** $P_\text{max} = 3 \cdot 230\,\text{V} \cdot 25\,\text{A} = 17\,250\,\text{W} = 17.25\,\text{kW}$, so $P_\text{s} = 17.25\,\text{kW} - 6.8\,\text{kW} = 10.45\,\text{kW}$
**Answer:** In the answer box $10.5\,\text{kW}$, one decimal like the powers in the table. a) The peak power is at $19\text{–}20$.

b) The power of the station may be at most $10.5\,\text{kW}$ during the peak.

c) The station may use the full power $11\,\text{kW}$ when the power of the house is at most $17.25\,\text{kW} - 11\,\text{kW} = 6.25\,\text{kW}$. In the table only $19\text{–}20$ exceeds this ($6.8\,\text{kW}$), so in the other hours no load management is needed under this assumption (the power of the house stays at the table value for an hour), but at $19\text{–}20$ the station has to be limited. In reality, peaks within the hour may require load management.
**Reasonableness:** Current during the peak: house $6800\,\text{W} : 690\,\text{V} \approx 9.9\,\text{A}$ and station $10\,450\,\text{W} : 690\,\text{V} \approx 15.1\,\text{A}$ in each phase, together $25.0\,\text{A}$, exactly the limit of the main fuse. The result is smaller than the $11\,\text{kW}$ of the station, as it should be during the peak.

## fy6-16-L2-06
**Given:** energy of the battery $60\,\text{kWh}$, charge level $20\,\% \to 80\,\%$, power taken from the grid $P = 7.4\,\text{kW}$, $\eta = 92\,\%$
**Find:** a) two errors in the student's solution, b) the correct charging time $t$ in hours
**Principle:** In charging, only the fraction of the energy of the battery given by the difference of the charge levels is transferred to the battery, not the whole battery. Of the energy taken from the grid only the fraction given by the efficiency is stored in the battery, so the charging time is calculated from the energy going into the battery divided by the product of the efficiency and the power.
**Formula:** $\eta P t = W_\text{battery}$, so $t = \dfrac{W_\text{battery}}{\eta P}$
**Conversions:** $W_\text{battery} = (0.80 - 0.20) \cdot 60\,\text{kWh} = 36\,\text{kWh}$ and $\eta = 0.92$
**Substitution:** $t = \dfrac{36\,\text{kWh}}{0.92 \cdot 7.4\,\text{kW}} = \dfrac{36\,\text{kWh}}{6.808\,\text{kW}} = 5.288\,\text{h}$
**Answer:** In the answer box $5.3\,\text{h}$, two significant figures like the efficiency $92\,\%$. a) First error: the student uses the whole energy of the battery $60\,\text{kWh}$, although only $60\,\%$ of it, that is $36\,\text{kWh}$, is transferred to the battery.

Second error: the student does not take the efficiency into account, so the student divides by the power alone and not by the product $\eta P$.

b) The correct charging time is $5.3\,\text{h}$.
**Reasonableness:** If only the efficiency is forgotten, we get $36\,\text{kWh} : 7.4\,\text{kW} \approx 4.9\,\text{h}$, and the efficiency makes the time longer than this, as it should. The student's $8.1\,\text{h}$ is too long because it describes filling the whole battery from empty to full.

## fy6-16-L2-07
**Given:** power taken from the grid $P$ as a function of time $t$ from the table, measuring interval $0.5\,\text{h}$, $t = 0\text{–}3.0\,\text{h}$
**Find:** a) energy taken from the grid $W_\text{grid}$ in kilowatt-hours, b) average power $P_\text{avg}$ in kilowatts
**Principle:** The power changes with time, so the energy is not power times time. The energy is the area under the $(t, P)$ graph, and it is obtained by adding the areas of trapezoids half an hour wide. The average power is the energy divided by the total time.
**Reading the graph:** The points are joined with straight lines, and the area of each half-hour interval is the mean of the powers at the end points of the interval times $\Delta t = 0.5\,\text{h}$. The first and last powers are $11.0\,\text{kW}$ and $1.4\,\text{kW}$, and in between are $11.0$, $10.8$, $8.7$, $5.9$ and $3.1\,\text{kW}$.
**Formula:** interval by interval $W_i = \Delta t \cdot \dfrac{P_i + P_{i+1}}{2}$, the sum over all the intervals $W_\text{grid} = \sum W_i$, and $P_\text{avg} = \dfrac{W_\text{grid}}{t}$
**Conversions:** Not needed: kilowatts times hours gives kilowatt-hours.
**Substitution:** The sum of the intermediate powers is $11.0 + 10.8 + 8.7 + 5.9 + 3.1 = 39.5\,\text{kW}$ and the mean of the end points $(11.0 + 1.4) : 2 = 6.2\,\text{kW}$, so $W_\text{grid} = 0.5\,\text{h} \cdot (6.2\,\text{kW} + 39.5\,\text{kW}) = 22.85\,\text{kWh}$ and $P_\text{avg} = \dfrac{22.85\,\text{kWh}}{3.0\,\text{h}} = 7.617\,\text{kW}$
**Answer:** In the answer box $23\,\text{kWh}$, two significant figures like the powers. a) The energy taken from the grid is $23\,\text{kWh}$.

b) The average power is $7.6\,\text{kW}$.
**Reasonableness:** If the power had stayed at $11\,\text{kW}$ for the whole $3.0\,\text{h}$, the energy taken would have been $33\,\text{kWh}$. The result is smaller because the power falls towards the end of charging, and the average power $7.6\,\text{kW}$ is between the peak power $11\,\text{kW}$ and the final value $1.4\,\text{kW}$.

## fy6-16-L2-08
**Find:** the charging time $t$ when $24\,\text{kWh}$ is stored in the battery from a socket with a current of $8.0\,\text{A}$.
**Principle:** The power of single-phase charging is $P = UI$. Because of losses, more energy is taken from the grid than is stored in the battery, so the energy going into the battery is divided by the efficiency and the charging time is $t = W_\text{battery} : (\eta P)$. The energy and the power are substituted in the same multiple unit, kilowatt-hours and kilowatts, which gives the time in hours, and the efficiency as a decimal number.
**Model answer:** The charging power is

$P = UI = 230\,\text{V} \cdot 8.0\,\text{A}$

$P = 1840\,\text{W} = 1.84\,\text{kW}$

and the efficiency is $\eta = 85\,\% = 0.85$. The charging time is

$$\begin{aligned}
t &= \frac{W_\text{battery}}{\eta P} \\
&= \frac{24\,\text{kWh}}{0.85 \cdot 1.84\,\text{kW}} \\
&\approx 15\,\text{h}
\end{aligned}$$

The correct option is about $15\,\text{h}$.

The result is reasonable: about $1.8\,\text{kWh}$ is taken from the grid in an hour, and about $1.6\,\text{kWh}$ of it goes into the battery, so $24\,\text{kWh}$ takes about $15$ hours. Charging does not fit into one night, but it fits into a day and a night.

The other options come from typical errors. Without the efficiency we get the time of charging without losses:

$t = 24\,\text{kWh} : 1.84\,\text{kW} \approx 13\,\text{h}$

When the energy is multiplied by the efficiency instead of divided by it, the time becomes even shorter:

$t = 0.85 \cdot 24\,\text{kWh} : 1.84\,\text{kW}$

that is, $t \approx 11\,\text{h}$. Losses make charging longer, so both are too short. The formula of a three-phase device, $P = 3UI$, gives a power three times too large, although the socket is single-phase, and the time falls to about $5.1\,\text{h}$.

## fy6-16-L3-04
**Given:** monthly distances from the table, electric car $16.0\,\text{kWh}$ from the battery per hundred kilometres, $\eta = 90.0\,\%$, $a_\text{home} = 15\,\text{c/kWh}$, $a_\text{public} = 0.45\,\text{€/kWh}$, petrol car $6.50\,\textsf{l}$ per hundred kilometres, price of petrol $b = 1.85\,\text{€/}\textsf{l}$
**Find:** b) the difference $\Delta K$ in euros between the yearly costs of the petrol car and of the electric car charged at home
**Principle:** The yearly cost is the amount consumed times the price. With the electric car the energy taken from the grid is paid for, so the energy consumed from the battery is divided by the efficiency. With the petrol car the litres bought are paid for. For both, the consumption is directly proportional to the distance driven, so the consumption per $100\,\text{km}$ is multiplied by the number $s : 100\,\text{km}$.
**Formula:** $W_\text{grid} = \dfrac{s}{100\,\text{km}} \cdot \dfrac{w}{\eta}$, $K_\text{e} = a W_\text{grid}$, $K_\text{p} = \dfrac{s}{100\,\text{km}} \cdot v b$ and $\Delta K = K_\text{p} - K_\text{e}$, where $w = 16.0\,\text{kWh}$ and $v = 6.50\,\textsf{l}$
**Conversions:** $a_\text{home} = 15\,\text{c/kWh} = 0.15\,\text{€/kWh}$ and $\eta = 0.900$
**Substitution:** The sum of the monthly distances is $s = 14\,640\,\text{km}$, so $s : 100\,\text{km} = 146.4$. Electric car: $W_\text{grid} = 146.4 \cdot 16.0\,\text{kWh} : 0.900 = 2602.7\,\text{kWh}$ and $K_\text{e} = 0.15\,\text{€/kWh} \cdot 2602.7\,\text{kWh} = 390.4\,\text{€}$. Petrol car: $K_\text{p} = 146.4 \cdot 6.50\,\textsf{l} \cdot 1.85\,\text{€/}\textsf{l} = 1760.5\,\text{€}$. The difference is $\Delta K = 1760.5\,\text{€} - 390.4\,\text{€} = 1370.1\,\text{€}$.
**Answer:** In the answer box $1370\,\text{€}$, that is, rounded to ten euros, because the cost of electricity $390\,\text{€}$ is accurate to two significant figures. a) The yearly driving distance is $14\,640\,\text{km}$.

b) The petrol car costs about $1370\,\text{€}$ more in a year.

c) With public charging $K_\text{e} = 0.45\,\text{€/kWh} \cdot 2602.7\,\text{kWh} = 1171.2\,\text{€}$, which is still less than the $1760.5\,\text{€}$ of the petrol car. The saving decreases to $1760.5\,\text{€} - 1171.2\,\text{€} = 589.3\,\text{€}$, that is, by about $780\,\text{€}$, but the electric car is still cheaper, because its energy consumption is small and its cost is about two thirds of the cost of the petrol car.
**Reasonableness:** Estimate: $15\,000\,\text{km}$ is $150$ times $100\,\text{km}$. The electric car costs about $150 \cdot 2.7\,\text{€} \approx 400\,\text{€}$ ($100\,\text{km}$ costs $17.8\,\text{kWh} \cdot 0.15\,\text{€/kWh} \approx 2.7\,\text{€}$) and the petrol car $150 \cdot 12\,\text{€} = 1800\,\text{€}$ ($100\,\text{km}$ costs $6.5\,\textsf{l} \cdot 1.85\,\text{€/}\textsf{l} \approx 12\,\text{€}$), so the difference is about $1400\,\text{€}$. The energy taken from the grid, $17.8\,\text{kWh}$ per hundred kilometres, is larger than the $16.0\,\text{kWh}$ consumed from the battery, as it should be because of the losses.

## fy6-16-L3-05
**Given:** main fuses $3 \cdot 25\,\text{A}$, $U = 230\,\text{V}$, loads $6.0\,\text{kW}$, $3.3\,\text{kW}$, $1.8\,\text{kW}$ and $0.90\,\text{kW}$ divided equally between three phases, cable $l = 30\,\text{m}$, $A = 2.5\,\text{mm}^2$, $\rho = 1.7 \cdot 10^{-8}\,\Omega\cdot\text{m}$
**Find:** b) the largest charging current $I_\text{s}$ in amperes and c) the heating power of the cable $P_\text{cable}$ at two currents
**Principle:** The currents through the same phase conductor are added, and the sum may be at most the current of the main fuse. The loads of the house are divided equally between the phases, so the current of the house per phase is obtained from the formula for three-phase power. A single-phase station loads only one phase, so what is left of that phase remains for it. The copper conductors of the cable are a resistor, in which the power according to Joule's law is $RI^2$.
**Formula:** $P_\text{house} = 3UI_\text{house}$, so $I_\text{house} = \dfrac{P_\text{house}}{3U}$; $I_\text{house} + I_\text{s} \le I_\text{f}$, so $I_\text{s} = I_\text{f} - I_\text{house}$; $P_\text{cable} = \rho \dfrac{2l}{A} I^2$
**Conversions:** $P_\text{house} = 6.0\,\text{kW} + 3.3\,\text{kW} + 1.8\,\text{kW} + 0.90\,\text{kW} = 12.0\,\text{kW} = 12\,000\,\text{W}$ and $A = 2.5\,\text{mm}^2 = 2.5 \cdot 10^{-6}\,\text{m}^2$
**Substitution:** $I_\text{house} = \dfrac{12\,000\,\text{W}}{3 \cdot 230\,\text{V}} = 17.39\,\text{A}$ and $I_\text{s} = 25\,\text{A} - 17.39\,\text{A} = 7.609\,\text{A}$. The resistance of the cable is $R = 1.7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \dfrac{2 \cdot 30\,\text{m}}{2.5 \cdot 10^{-6}\,\text{m}^2} = 0.408\,\Omega$, so $P_\text{cable} = 0.408\,\Omega \cdot (7.609\,\text{A})^2 = 23.6\,\text{W}$ and at a current of $16\,\text{A}$ $P_\text{cable} = 0.408\,\Omega \cdot (16\,\text{A})^2 = 104.4\,\text{W}$.
**Answer:** In the answer box $7.6\,\text{A}$, two significant figures like the powers of the loads. a) The current of the house is $17\,\text{A}$ in each phase conductor.

b) The station may draw at most $7.6\,\text{A}$.

c) The heating power of the cable is $24\,\text{W}$ at a current of $7.6\,\text{A}$ and $104\,\text{W}$ at a current of $16\,\text{A}$. The current increases by a factor of $16 : 7.609 \approx 2.1$, but the power increases by its square, to about $4.4$ times. In the evening the main fuse is already almost full, and $16\,\text{A}$ would exceed it ($17.4\,\text{A} + 16\,\text{A} = 33.4\,\text{A}$), so load management has to limit the charging current for the peak time; a smaller current also keeps the cable cooler.
**Reasonableness:** The current of the house and the current of the station together are $17.39\,\text{A} + 7.609\,\text{A} = 25.0\,\text{A}$, exactly the limit of the main fuse. The power of the station would be only $230\,\text{V} \cdot 7.609\,\text{A} \approx 1.75\,\text{kW}$, so slow charging is physically reasonable at peak time: at night, when the sauna heater and the stove are off, the current can be increased again.
