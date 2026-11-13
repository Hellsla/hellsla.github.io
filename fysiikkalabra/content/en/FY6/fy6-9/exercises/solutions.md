## fy6-9-L1-01
**Given:** current $I = 0.25\,\text{A}$, time $t = 8.0\,\text{h}$
**Find:** the capacity of the battery $Q$ in ampere-hours
**Principle:** The capacity is the charge that the battery moves through the circuit from full to empty. The current is constant, so the charge is current times time.
**Formula:** $Q = It$
**Conversions:** Not needed: when the current is in amperes and the time in hours, the charge comes directly in ampere-hours.
**Substitution:** $Q = 0.25\,\text{A} \cdot 8.0\,\text{h} = 2.0\,\text{Ah}$
**Answer:** $2.0\,\text{Ah}$, two significant figures like the current and the time.
**Reasonableness:** A quarter of an ampere for eight hours is the same charge as $1\,\text{A}$ for two hours, that is, $2\,\text{Ah}$. A capacity of a few ampere-hours is usual for the battery of a small light.

## fy6-9-L1-02
**Given:** capacity $Q = 3000\,\text{mAh}$
**Find:** the charge $Q$ in coulombs
**Principle:** The capacity is the charge that the battery moves from full to empty. An ampere-hour is the charge that a current of $1\,\text{A}$ moves in an hour, so it is converted to coulombs by substituting $1\,\text{A} = 1\,\text{C/s}$ and $1\,\text{h} = 3600\,\text{s}$.
**Formula:** $Q = It$
**Conversions:** $3000\,\text{mAh} = 3000 \cdot 0.001\,\text{Ah} = 3.0\,\text{Ah}$ and $1\,\text{Ah} = 1\,\text{A} \cdot 3600\,\text{s}$
**Substitution:** $Q = 3.0\,\text{A} \cdot 3600\,\text{s} = 10\,800\,\text{C}$
**Answer:** $1.08 \cdot 10^{4}\,\text{C}$, that is, about $11\,000\,\text{C}$, two significant figures like the capacity $3.0\,\text{Ah}$.
**Reasonableness:** One ampere-hour is $3600\,\text{C}$, and three ampere-hours is three times as much, $10\,800\,\text{C}$. In coulombs the number is large, because an hour has $3600$ seconds.

## fy6-9-L1-03
**Given:** nominal voltage $U = 36\,\text{V}$, capacity $Q = 13\,\text{Ah}$
**Find:** the energy $W$ stored in the battery in watt-hours
**Principle:** Voltage tells the energy per unit of charge, so the energy of a battery is voltage times charge. The nominal voltage is the average voltage of the battery during discharging.
**Formula:** $W = UQ$
**Conversions:** Not needed: $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh}$.
**Substitution:** $W = 36\,\text{V} \cdot 13\,\text{Ah} = 468\,\text{Wh}$
**Answer:** $470\,\text{Wh}$, two significant figures like the voltage and the capacity.
**Reasonableness:** The estimate $40\,\text{V} \cdot 12\,\text{Ah} = 480\,\text{Wh}$ is close. About half a kilowatt-hour is usual for an electric-bike battery, and it lasts for tens of kilometres.

## fy6-9-L1-04
**Given:** capacity $Q = 2.4\,\text{Ah}$, current $I = 0.15\,\text{A}$
**Find:** the time $t$ in hours that the lamp stays on
**Principle:** The lamp draws a constant current, so the charge passing through the battery is current times time. The battery is empty when the charge equals the capacity.
**Formula:** $Q = It$, from which $t = \dfrac{Q}{I}$
**Conversions:** Not needed: the quotient of ampere-hours and amperes is hours.
**Substitution:** $t = \dfrac{2.4\,\text{Ah}}{0.15\,\text{A}} = 16\,\text{h}$
**Answer:** $16\,\text{h}$, two significant figures like the capacity and the current.
**Reasonableness:** With a current of $0.15\,\text{A}$, a charge of $1.5\,\text{Ah}$ passes in ten hours, and $2.4\,\text{Ah}$ is a little over one and a half times that. Sixteen hours of light suits a low-power LED flashlight.

## fy6-9-L1-05
**Given:** the charging current as a function of time in the graph
**Find:** the charge $Q$ that passed through the battery in ampere-hours
**Principle:** With a constant current the charge is current times time, that is, the area under the graph of current against time. The current is constant in two parts, so the charge is the sum of the areas of two rectangles.
**Reading the graph:** The current is on the $2.0\,\text{A}$ grid line from time $0$ to time $1.5\,\text{h}$ and on the $1.0\,\text{A}$ line from time $1.5\,\text{h}$ to time $2.5\,\text{h}$, after which it is zero.
**Formula:** $Q = I_1 t_1 + I_2 t_2$
**Conversions:** Not needed: an ampere times an hour is an ampere-hour. The duration of the second part is $t_2 = 2.5\,\text{h} - 1.5\,\text{h} = 1.0\,\text{h}$.
**Substitution:** $Q = 2.0\,\text{A} \cdot 1.5\,\text{h} + 1.0\,\text{A} \cdot 1.0\,\text{h} = 3.0\,\text{Ah} + 1.0\,\text{Ah} = 4.0\,\text{Ah}$
**Answer:** $4.0\,\text{Ah}$, two significant figures. The values are read from grid lines whose spacing is $0.5\,\text{A}$ and $0.5\,\text{h}$.
**Reasonableness:** If the current had been $2.0\,\text{A}$ for the whole $2.5$ hours, the charge would be $5.0\,\text{Ah}$; the current decreased towards the end, so the result is smaller, as it should be.

## fy6-9-L2-01
**Given:** $E = 12.4\,\text{V}$, $R_\text{s} = 40\,\text{m}\Omega$, $U_\text{ch} = 14.4\,\text{V}$, $R = 0.36\,\Omega$
**Find:** the charging current $I$ in amperes
**Principle:** The circuit has one loop, so by the voltage law the voltage of the charger is the sum of the potential drops. The current passes through the battery from the positive terminal to the negative terminal, so the potential drops in the battery both in the internal resistance and by the source voltage.
**Formula:** $U_\text{ch} - RI - R_\text{s} I - E = 0$, from which $I = \dfrac{U_\text{ch} - E}{R + R_\text{s}}$
**Conversions:** $R_\text{s} = 40\,\text{m}\Omega = 40 \cdot 0.001\,\Omega = 0.040\,\Omega$
**Substitution:** $I = \dfrac{14.4\,\text{V} - 12.4\,\text{V}}{0.36\,\Omega + 0.040\,\Omega} = \dfrac{2.0\,\text{V}}{0.40\,\Omega} = 5.0\,\text{A}$
**Answer:** $5.0\,\text{A}$, two significant figures like the voltage difference $2.0\,\text{V}$ and the resistances.
**Reasonableness:** The terminal voltage is $12.4\,\text{V} + 0.040\,\Omega \cdot 5.0\,\text{A} = 12.6\,\text{V}$, and from the charger side $14.4\,\text{V} - 0.36\,\Omega \cdot 5.0\,\text{A} = 12.6\,\text{V}$, the same. Without converting the milliohms the resistance would be $40\,\Omega$ and the current only about $0.05\,\text{A}$.

## fy6-9-L2-02
**Given:** $U_\text{ch} = 5.0\,\text{V}$, $E = 3.8\,\text{V}$, $R = 0.80\,\Omega$, $I = 1.2\,\text{A}$
**Find:** the internal resistance $R_\text{s}$ of the cell in ohms
**Principle:** By the voltage law, the difference between the voltage of the charger and the source voltage of the cell equals the sum of the voltages of the resistances in the loop. When the current is known, we get the sum of the resistances and from it the share of the cell.
**Formula:** $U_\text{ch} - RI - R_\text{s} I - E = 0$, from which $R_\text{s} = \dfrac{U_\text{ch} - E}{I} - R$
**Conversions:** Not needed: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Substitution:** $R_\text{s} = \dfrac{5.0\,\text{V} - 3.8\,\text{V}}{1.2\,\text{A}} - 0.80\,\Omega = 1.0\,\Omega - 0.80\,\Omega = 0.20\,\Omega$
**Answer:** $0.20\,\Omega$, to a hundredth of an ohm like the resistance $0.80\,\Omega$; the difference $1.2\,\text{V}$ and the current limit the precision.
**Reasonableness:** Check: $1.2\,\text{A} \cdot (0.80\,\Omega + 0.20\,\Omega) = 1.2\,\text{V}$, which is the difference between the voltages of the charger and the cell. The result is positive and suits the internal resistance of a small battery cell.

## fy6-9-L2-03
**Given:** capacity $4500\,\text{mAh}$, charge level $15\,\%$ → $80\,\%$, average current $I = 1.8\,\text{A}$
**Find:** the charging time $t$ in minutes
**Principle:** The charge passing through the battery must be the part of the capacity by which the charge level rises. With the average current the charge is current times time.
**Formula:** $Q = (0.80 - 0.15) \cdot Q_\text{cap}$ and $Q = It$, from which $t = \dfrac{(0.80 - 0.15)\, Q_\text{cap}}{I}$
**Conversions:** $Q_\text{cap} = 4500\,\text{mAh} = 4500 \cdot 0.001\,\text{Ah} = 4.5\,\text{Ah}$ and finally $1\,\text{h} = 60\,\text{min}$
**Substitution:** $t = \dfrac{0.65 \cdot 4.5\,\text{Ah}}{1.8\,\text{A}} = \dfrac{2.925\,\text{Ah}}{1.8\,\text{A}} = 1.625\,\text{h} = 1.625 \cdot 60\,\text{min} = 97.5\,\text{min}$
**Answer:** $98\,\text{min}$, two significant figures like the current $1.8\,\text{A}$.
**Reasonableness:** Charging the whole battery with a current of $1.8\,\text{A}$ would take $4.5 : 1.8 = 2.5\,\text{h}$; a little under two thirds of that is about an hour and a half, which agrees.

## fy6-9-L2-04
**Given:** nominal voltage $U = 36\,\text{V}$, capacity $Q = 14\,\text{Ah}$, energy taken from the mains $W_\text{ch} = 600\,\text{Wh}$
**Find:** the efficiency of charging $\eta$ in percent
**Principle:** The efficiency is the ratio of the energy stored in the battery to the energy taken. By the assumption of the task, the energy stored in the battery is the nominal voltage times the capacity. The rest of the energy taken becomes internal energy of the charger, the wires and the battery.
**Formula:** $W_\text{batt} = UQ$ and $\eta = \dfrac{W_\text{batt}}{W_\text{ch}}$, from which $\eta = \dfrac{UQ}{W_\text{ch}}$
**Conversions:** Not needed: $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh}$, and finally $0.84 = 84\,\%$.
**Substitution:** $\eta = \dfrac{36\,\text{V} \cdot 14\,\text{Ah}}{600\,\text{Wh}} = \dfrac{504\,\text{Wh}}{600\,\text{Wh}} = 0.84$
**Answer:** $84\,\%$, two significant figures like the voltage and the capacity.
**Reasonableness:** The efficiency is below $100\,\%$, as it should be. The losses are $96\,\text{Wh}$, and the charger and the battery warm up during charging, which fits.

## fy6-9-L3-01
**Given:** car battery $U_1 = 12\,\text{V}$, $Q_1 = 60\,\text{Ah}$, half usable; scooter battery $U_2 = 36\,\text{V}$, $Q_2 = 7.8\,\text{Ah}$, fully usable
**Find:** the ratio of the usable energies $W_1 : W_2$
**Principle:** Ampere-hours tell only the charge. The voltages of the batteries are different, so they are compared by the energy $W = UQ$. Only half of the capacity is drawn from the car battery, so its usable energy is calculated from half the charge.
**Formula:** $W_1 = 0.5\, U_1 Q_1$ and $W_2 = U_2 Q_2$, from which $\dfrac{W_1}{W_2} = \dfrac{0.5\, U_1 Q_1}{U_2 Q_2}$
**Conversions:** Not needed: $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh}$, and in the ratio the units cancel.
**Substitution:** $\dfrac{W_1}{W_2} = \dfrac{0.5 \cdot 12\,\text{V} \cdot 60\,\text{Ah}}{36\,\text{V} \cdot 7.8\,\text{Ah}} = \dfrac{360\,\text{Wh}}{280.8\,\text{Wh}} \approx 1.28$
**Answer:** $1.3$ times, two significant figures like the voltages and the capacities.
**Reasonableness:** The ratio of the ampere-hours is almost eight, but the voltage of the scooter battery is three times as great and only half of the car battery may be used: $7.7 : 3 : 2 \approx 1.3$. The usable energies are therefore of almost the same order of magnitude.

## fy6-9-L3-02
**Given:** $U_\text{ch} = 13.8\,\text{V}$, source voltage at the start $E_1 = 12.0\,\text{V}$ and at the end $E_2 = 12.6\,\text{V}$, resistances in total $R_\text{tot} = 0.30\,\Omega$
**Find:** the relative decrease of the charging current in percent
**Principle:** By the voltage law, the charging current is driven by the difference between the voltage of the charger and the source voltage, and the resistances stay constant. When the source voltage grows, the difference and the current decrease. The decrease is compared with the initial current.
**Formula:** $I = \dfrac{U_\text{ch} - E}{R_\text{tot}}$, and the decrease is $\dfrac{I_1 - I_2}{I_1}$
**Conversions:** Not needed: the voltages are in volts and the resistance in ohms. Finally the ratio is converted to percent.
**Substitution:** $I_1 = \dfrac{13.8\,\text{V} - 12.0\,\text{V}}{0.30\,\Omega} = 6.0\,\text{A}$, $I_2 = \dfrac{13.8\,\text{V} - 12.6\,\text{V}}{0.30\,\Omega} = 4.0\,\text{A}$ and $\dfrac{6.0\,\text{A} - 4.0\,\text{A}}{6.0\,\text{A}} = 0.333 = 33.3\,\%$
**Answer:** $33\,\%$, two significant figures like the voltage differences $1.8\,\text{V}$ and $1.2\,\text{V}$.
**Reasonableness:** The current is proportional to the voltage difference, and the difference decreases from $1.8\,\text{V}$ to $1.2\,\text{V}$, that is, by a third. The current decreases in the same proportion, although the source voltage changes by only $5\,\%$.

## fy6-9-L3-03
**Given:** charging current $I = 2.0\,\text{A}$, time $t = 1.5\,\text{h}$, internal resistance $R_\text{s} = 0.15\,\Omega$
**Find:** the energy $W$ that becomes internal energy, in kilojoules
**Principle:** The charging current passes through the internal resistance of the battery, and by Ohm's law the voltage of the resistance is $R_\text{s} I$. Electric power is voltage times current (chapter *Electric power and the heating of a resistor*), and at constant power energy is power times time. This energy becomes internal energy of the battery, which is transferred to the surroundings as heat.
**Formula:** $P = R_\text{s} I \cdot I = R_\text{s} I^2$ and $W = Pt$, from which $W = R_\text{s} I^2 t$
**Conversions:** $t = 1.5\,\text{h} = 1.5 \cdot 3600\,\text{s} = 5400\,\text{s}$ and finally $1\,\text{kJ} = 1000\,\text{J}$
**Substitution:** $W = 0.15\,\Omega \cdot (2.0\,\text{A})^2 \cdot 5400\,\text{s} = 0.60\,\text{W} \cdot 5400\,\text{s} = 3240\,\text{J} = 3.24\,\text{kJ}$
**Answer:** $3.2\,\text{kJ}$, two significant figures like the current, the time and the resistance.
**Reasonableness:** The power $0.60\,\text{W}$ is small, but enough to warm a phone noticeably in an hour and a half. In charging, about $4\,\text{V} \cdot 3.0\,\text{Ah} = 12\,\text{Wh} \approx 43\,\text{kJ}$ passes into the battery, so the loss is a few percent.

## fy6-9-L1-06
**Find:** why the energies of batteries cannot be compared on the basis of ampere-hours alone
**Principle:** An ampere-hour is a unit of charge, $1\,\text{Ah} = 3600\,\text{C}$. The energy of a battery is voltage times charge, $W = UQ$, so the energy depends on the nominal voltage of the battery as well as on the capacity.
**Model answer:** Energy depends on the voltage as well as on the charge, and the voltages of the batteries can be different. For example, a battery with a capacity of $2.0\,\text{Ah}$ and a nominal voltage of $3.7\,\text{V}$ contains an energy of $7.4\,\text{Wh}$, but a battery with a capacity of $1.0\,\text{Ah}$ and a nominal voltage of $12\,\text{V}$ contains an energy of $12\,\text{Wh}$. So the battery with the smaller capacity has more energy. An ampere-hour is neither a unit of time nor a unit of energy, and other reasons, such as mass or temperature, do not explain the difference.

## fy6-9-L1-07
**Find:** the direction of the current inside the battery during charging
**Principle:** In charging, the voltage of the charger is larger than the source voltage of the battery, and the charger drives the current through the battery from the positive terminal to the negative terminal. In discharging, the battery drives the current in the external circuit from the positive terminal to the negative terminal and inside the battery from the negative terminal to the positive terminal, so in charging the direction inside the battery is the opposite.
**Model answer:** The current goes inside the battery from the positive terminal to the negative terminal, because the charger drives it through the battery in the direction opposite to discharging. The current does not stop, since thanks to it the chemical energy increases, and its direction does not alternate, since the charger produces a direct voltage.

## fy6-9-L1-08
**Given:** capacity $Q = 2600\,\text{mAh}$, charging current $I = 0.50\,\text{A}$
**Find:** the charging time $t$ in hours
**Principle:** With a constant current the charge passing through the battery is current times time. Charging an empty battery is complete when a charge equal to the capacity has passed through.
**Formula:** $Q = It$, from which $t = \dfrac{Q}{I}$
**Conversions:** $2600\,\text{mAh} = 2600 \cdot 0.001\,\text{Ah} = 2.6\,\text{Ah}$
**Substitution:** $t = \dfrac{2.6\,\text{Ah}}{0.50\,\text{A}} = 5.2\,\text{h}$
**Answer:** $5.2\,\text{h}$, two significant figures like the current $0.50\,\text{A}$.
**Reasonableness:** With a current of $0.50\,\text{A}$, a charge of $2.5\,\text{Ah}$ passes in five hours, which is close to the capacity $2.6\,\text{Ah}$, so the time is a little over five hours.

## fy6-9-L1-09
**Find:** which of the four expressions gives the energy stored in the power bank, that is, which expression has the unit of energy
**Principle:** The unit of an expression is found by substituting the unit of each quantity: $Q$ ($\text{Ah}$), $U$ ($\text{V}$) and $t$ ($\text{h}$). A volt times an ampere is a watt, so $1\,\text{V}\cdot 1\,\text{Ah} = 1\,\text{Wh}$, which is a unit of energy. The energy of a battery is voltage times charge, $W = UQ$.
**Model answer:** The correct one is $UQ$. The units of the expressions:

The unit of $Q$ is $\text{Ah}$, the unit of charge

The unit of $UQ$ is $\text{V}\cdot\text{Ah} = \text{Wh}$, the unit of energy

The unit of $\tfrac{UQ}{t}$ is $\dfrac{\text{Wh}}{\text{h}} = \text{W}$, the unit of power

The unit of $UQt$ is $\text{Wh}\cdot\text{h}$, not the unit of any quantity of this chapter

Only the unit of $UQ$ is a unit of energy, and it is also the formula for the energy of a battery, $W = UQ$. The capacity $Q$ alone tells the charge that can pass through the battery, and it tells no energy without the voltage. The expression $\tfrac{UQ}{t}$ is the average power of the charging. In $UQt$ the time is included twice, because the ampere-hour already contains time: $1\,\text{Ah} = 1\,\text{A}\cdot 1\,\text{h}$. So the charging time is not needed for calculating the energy.

## fy6-9-L2-05
**Given:** discharge current $I = 0.50\,\text{A}$, measurement interval $\Delta t = 1.0\,\text{h}$, terminal voltages from the table $4.15\,\text{V}$, $3.92\,\text{V}$, $3.80\,\text{V}$, $3.71\,\text{V}$, $3.58\,\text{V}$ and $3.12\,\text{V}$
**Find:** the energy $W$ delivered by the cell in watt-hours
**Principle:** Power is voltage times current, and with a constant current the voltage changes with time. The voltage is assumed to change uniformly between the measurements, so the mean voltage of each interval is the average of the voltages at the ends of the interval. The energy is current times time times mean voltage, summed over all the intervals.
**Formula:** $W = I\,\Delta t\,(U_{1,\text{avg}} + U_{2,\text{avg}} + \dots + U_{5,\text{avg}})$, where $U_{k,\text{avg}}$ is the mean voltage of interval $k$
**Conversions:** Not needed: an ampere times an hour times a volt is a watt-hour.
**Substitution:** The mean voltages of the intervals are $4.035\,\text{V}$, $3.86\,\text{V}$, $3.755\,\text{V}$, $3.645\,\text{V}$ and $3.35\,\text{V}$, and their sum is $18.645\,\text{V}$. So $W = 0.50\,\text{A} \cdot 1.0\,\text{h} \cdot 18.645\,\text{V} = 9.3225\,\text{Wh}$
**Answer:** $9.3\,\text{Wh}$, two significant figures like the current $0.50\,\text{A}$ and the measurement interval $1.0\,\text{h}$.
**Reasonableness:** The discharge lasted five hours, so the charge is $0.50\,\text{A} \cdot 5.0\,\text{h} = 2.5\,\text{Ah}$. The quotient of the energy and the charge, $9.3225\,\text{Wh} : 2.5\,\text{Ah} \approx 3.73\,\text{V}$, is the mean voltage, and it lies between the measured voltages $3.12\,\text{V}$ and $4.15\,\text{V}$, close to the nominal voltage $3.7\,\text{V}$ of a lithium cell.

## fy6-9-L2-06
**Given:** charging current $I = 2.0\,\text{A}$, time $t = 1.5\,\text{h}$, voltage of the charger $U_\text{ch} = 4.2\,\text{V}$, source voltage of the battery $E = 3.7\,\text{V}$
**Find:** the energy $W_\text{loss}$ that becomes internal energy of the resistances, in watt-hours
**Principle:** a) The $12.6\,\text{Wh}$ calculated by the student is the energy given by the charger, $U_\text{ch} I t$, and it is correct. The error is the assumption that everything is stored in the battery: only the part $E I t$, given by the source voltage, becomes chemical energy in the battery. The rest, the part of the voltage difference $U_\text{ch} - E$, is used to drive the current through the resistances and becomes their internal energy, which is transferred to the surroundings as heat. b) The loss is the difference between the energy given by the charger and the energy stored in the battery.
**Formula:** $W_\text{loss} = U_\text{ch} I t - E I t$, from which $W_\text{loss} = (U_\text{ch} - E)\, I t$
**Conversions:** Not needed: hours and amperes multiplied by volts give watt-hours directly.
**Substitution:** $W_\text{loss} = (4.2\,\text{V} - 3.7\,\text{V}) \cdot 2.0\,\text{A} \cdot 1.5\,\text{h} = 0.5\,\text{V} \cdot 3.0\,\text{Ah} = 1.5\,\text{Wh}$
**Answer:** $1.5\,\text{Wh}$, two significant figures like the voltage difference $4.2\,\text{V} - 3.7\,\text{V} = 0.5\,\text{V}$. Answer to a): what is wrong in the student's reasoning is that all the energy given by the charger is stored in the battery, since part of it becomes internal energy of the resistances.
**Reasonableness:** The energy stored in the battery is $3.7\,\text{V} \cdot 2.0\,\text{A} \cdot 1.5\,\text{h} = 11.1\,\text{Wh}$, and the sum $11.1\,\text{Wh} + 1.5\,\text{Wh}$ is the $12.6\,\text{Wh}$ given by the charger. The resistances are together $0.5\,\text{V} : 2.0\,\text{A} = 0.25\,\Omega$, and the energy that becomes internal energy in them is $0.25\,\Omega \cdot (2.0\,\text{A})^2 \cdot 1.5\,\text{h} = 1.5\,\text{Wh}$, the same result.

## fy6-9-L2-07
**Given:** charger voltages $13.0\,\text{V}$, $13.4\,\text{V}$, $13.8\,\text{V}$, $14.2\,\text{V}$ and $14.6\,\text{V}$ and charging currents $1.6\,\text{A}$, $2.4\,\text{A}$, $3.5\,\text{A}$, $4.6\,\text{A}$ and $5.5\,\text{A}$ from the table
**Find:** the resistance $R_\text{tot}$ in ohms
**Principle:** By the voltage law $I = (U_\text{ch} - E) : R_\text{tot}$, so when $E$ and $R_\text{tot}$ are constant, the current is a linear function of the voltage of the charger. The slope of its graph is $1 : R_\text{tot}$. Because of measurement uncertainty the data points are usually not exactly on one line, so the slope is read from the fitted line and not from two neighbouring data points.
**Reading the graph:** The points are plotted in an $(U_\text{ch}, I)$ coordinate system and a straight line is fitted among them. Two points far apart from each other are read from the line, $(13.0\,\text{V};\ 1.5\,\text{A})$ and $(14.6\,\text{V};\ 5.5\,\text{A})$.
**Formula:** slope $k = \dfrac{\Delta I}{\Delta U_\text{ch}} = \dfrac{1}{R_\text{tot}}$, from which $R_\text{tot} = \dfrac{\Delta U_\text{ch}}{\Delta I}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Substitution:** $R_\text{tot} = \dfrac{14.6\,\text{V} - 13.0\,\text{V}}{5.5\,\text{A} - 1.5\,\text{A}} = \dfrac{1.6\,\text{V}}{4.0\,\text{A}} = 0.40\,\Omega$
**Answer:** $0.40\,\Omega$, two significant figures like the current readings. A line fitted by hand gives the result to within a few percent.
**Reasonableness:** The line crosses the horizontal axis at $13.0\,\text{V} - 1.5\,\text{A} \cdot 0.40\,\Omega = 12.4\,\text{V}$, which is the source voltage of the battery and suits a $12\,\text{V}$ lead-acid battery. At $13.8\,\text{V}$ the voltage law gives a current $(13.8\,\text{V} - 12.4\,\text{V}) : 0.40\,\Omega = 3.5\,\text{A}$, and the measurement is $3.5\,\text{A}$.

## fy6-9-L2-08
**Given:** nominal voltage of the battery $U = 11.1\,\text{V}$ and the charging current as a function of time from the graph
**Find:** the energy stored in the battery $W$ in watt-hours
**Principle:** With constant current the charge is the current times the time, that is, the area under the current-time graph. The current is constant in three parts, so the charge is the sum of the areas of three rectangles. By the assumption of the task, the energy stored in the battery is the nominal voltage times the charge.
**Reading the graph:** The current is $2.0\,\text{A}$ from $0$ to $1.0\,\text{h}$, $1.5\,\text{A}$ from $1.0\,\text{h}$ to $3.0\,\text{h}$ and $0.5\,\text{A}$ from $3.0\,\text{h}$ to $4.0\,\text{h}$, and zero after that.
**Formula:** $Q = I_1 t_1 + I_2 t_2 + I_3 t_3$ and $W = UQ$, so $W = U\,(I_1 t_1 + I_2 t_2 + I_3 t_3)$
**Conversions:** Not needed: $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh}$. The durations are $t_1 = 1.0\,\text{h}$, $t_2 = 3.0\,\text{h} - 1.0\,\text{h} = 2.0\,\text{h}$ and $t_3 = 4.0\,\text{h} - 3.0\,\text{h} = 1.0\,\text{h}$.
**Substitution:** $Q = 2.0\,\text{A} \cdot 1.0\,\text{h} + 1.5\,\text{A} \cdot 2.0\,\text{h} + 0.5\,\text{A} \cdot 1.0\,\text{h} = 2.0\,\text{Ah} + 3.0\,\text{Ah} + 0.5\,\text{Ah} = 5.5\,\text{Ah}$ and $W = 11.1\,\text{V} \cdot 5.5\,\text{Ah} = 61.05\,\text{Wh}$
**Answer:** $61\,\text{Wh}$, two significant figures like the current readings. The values are read from the grid lines, which are $0.5\,\text{A}$ and $0.5\,\text{h}$ apart.
**Reasonableness:** The average current is $5.5\,\text{Ah} : 4.0\,\text{h} \approx 1.4\,\text{A}$, which lies between the largest and the smallest current on the graph. The energy $61\,\text{Wh}$ is within the usual $50$–$100\,\text{Wh}$ range of a laptop battery.

## fy6-9-L3-04
**Given:** from the table $I_1 = 0.50\,\text{A}$, $t_1 = 5.2\,\text{h}$, $U_{1,\text{avg}} = 3.70\,\text{V}$ and $I_2 = 2.0\,\text{A}$, $t_2 = 1.2\,\text{h}$, $U_{2,\text{avg}} = 3.55\,\text{V}$; the energy required for charging $W_\text{ch} = 11.0\,\text{Wh}$
**Find:** the charge–discharge efficiency $\eta$ in percent with the current $I_2$ (b), and in addition the internal resistance of the cell $R_\text{s}$ (c)
**Principle:** Before each discharge the cell is charged full from the same empty state. With a constant current the charge is $Q = It$, and the energy is the mean voltage times the charge, $W = U_\text{avg} Q$. The efficiency is the ratio of the energy obtained in discharging to the energy used in charging. The terminal voltage in discharging is $U = E - R_\text{s} I$, so when the source voltage $E$ is the same at both currents, the difference between the terminal voltages at the two currents is due only to the internal resistance.
**Formula:** $Q = It$ and $W = U_\text{avg} Q$, and $\eta = \dfrac{W}{W_\text{ch}}$ and $R_\text{s} = \dfrac{U_{1,\text{avg}} - U_{2,\text{avg}}}{I_2 - I_1}$
**Conversions:** Not needed: $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh}$ and $1\,\text{V} : 1\,\text{A} = 1\,\Omega$. Finally $0.7745 = 77.45\,\%$.
**Substitution:** a) $Q_1 = 0.50\,\text{A} \cdot 5.2\,\text{h} = 2.6\,\text{Ah}$ and $W_1 = 3.70\,\text{V} \cdot 2.6\,\text{Ah} = 9.62\,\text{Wh}$, and $Q_2 = 2.0\,\text{A} \cdot 1.2\,\text{h} = 2.4\,\text{Ah}$ and $W_2 = 3.55\,\text{V} \cdot 2.4\,\text{Ah} = 8.52\,\text{Wh}$. b) $\eta = \dfrac{8.52\,\text{Wh}}{11.0\,\text{Wh}} = 0.7745$. c) $R_\text{s} = \dfrac{3.70\,\text{V} - 3.55\,\text{V}}{2.0\,\text{A} - 0.50\,\text{A}} = \dfrac{0.15\,\text{V}}{1.5\,\text{A}} = 0.10\,\Omega$
**Answer:** $77\,\%$ (more precisely $77.45\,\%$), two significant figures like the duration of the discharge $1.2\,\text{h}$. Explanation: with a large current the voltage drop $R_\text{s} I$ is larger, so the terminal voltage falls to the limit $3.00\,\text{V}$ sooner and part of the capacity remains unused, $2.4\,\text{Ah}$ and not $2.6\,\text{Ah}$. In the internal resistance a power $R_\text{s} I^2$ becomes internal energy, and with a current four times as large it is $16$ times as large. In fast charging the current is large, so a small $R_\text{s}$ keeps the losses and the heating of the battery small.
**Reasonableness:** The source voltage is the same at both currents: $3.70\,\text{V} + 0.10\,\Omega \cdot 0.50\,\text{A} = 3.75\,\text{V}$ and $3.55\,\text{V} + 0.10\,\Omega \cdot 2.0\,\text{A} = 3.75\,\text{V}$, as the assumption requires. With the small current the efficiency is $9.62\,\text{Wh} : 11.0\,\text{Wh} \approx 87.5\,\%$, which is larger than with the large current and stays below $100\,\%$.

## fy6-9-L3-05
**Given:** capacity $Q_\text{cap} = 50\,\text{Ah}$, charger voltage $U_\text{ch} = 14.0\,\text{V}$, resistances together $R_\text{tot} = 0.40\,\Omega$, source voltages from the table $12.00\,\text{V}$, $12.20\,\text{V}$, $12.40\,\text{V}$ and $12.60\,\text{V}$ at the charge levels $20\,\%$, $40\,\%$, $60\,\%$ and $80\,\%$
**Find:** the duration of charging $t$ in hours from the charge level $20\,\%$ to the charge level $80\,\%$ (a) and the comparison time with a constant current (b)
**Principle:** By the voltage law the charging current is $I = (U_\text{ch} - E) : R_\text{tot}$. The source voltage increases as charging proceeds, so the current decreases. Therefore the charging is divided into stages in which the current is approximately constant, and in each stage the charge is $\Delta Q = It$. The current of a stage is calculated from the mean of the source voltage, because the source voltage changes during the stage.
**Formula:** $I_k = \dfrac{U_\text{ch} - E_{k,\text{avg}}}{R_\text{tot}}$, $t_k = \dfrac{\Delta Q}{I_k}$ and $t = t_1 + t_2 + t_3$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$ and $1\,\text{Ah} : 1\,\text{A} = 1\,\text{h}$. In each stage the charge level rises by $20\,\%$, so $\Delta Q = 0.20 \cdot 50\,\text{Ah} = 10\,\text{Ah}$.
**Substitution:** a) The mean source voltages are $12.10\,\text{V}$, $12.30\,\text{V}$ and $12.50\,\text{V}$. The currents are $I_1 = 1.90\,\text{V} : 0.40\,\Omega = 4.75\,\text{A}$, $I_2 = 1.70\,\text{V} : 0.40\,\Omega = 4.25\,\text{A}$ and $I_3 = 1.50\,\text{V} : 0.40\,\Omega = 3.75\,\text{A}$. The durations are $t_1 = 10\,\text{Ah} : 4.75\,\text{A} = 2.105\,\text{h}$, $t_2 = 10\,\text{Ah} : 4.25\,\text{A} = 2.353\,\text{h}$ and $t_3 = 10\,\text{Ah} : 3.75\,\text{A} = 2.667\,\text{h}$, so $t = 2.105\,\text{h} + 2.353\,\text{h} + 2.667\,\text{h} = 7.125\,\text{h}$. b) The initial current is $I_0 = (14.0\,\text{V} - 12.00\,\text{V}) : 0.40\,\Omega = 5.0\,\text{A}$ and the charge to be moved is $30\,\text{Ah}$, so $t_0 = 30\,\text{Ah} : 5.0\,\text{A} = 6.0\,\text{h}$
**Answer:** $7.1\,\text{h}$, two significant figures like the resistance $0.40\,\Omega$. With a constant current of $5.0\,\text{A}$ the time would be $6.0\,\text{h}$, and the actual charging takes longer because the source voltage increases, the voltage difference $U_\text{ch} - E$ decreases and the current falls from $4.75\,\text{A}$ to $3.75\,\text{A}$, so moving the same charge takes longer.
**Reasonableness:** The time lies between the lower limit $6.0\,\text{h}$ given by the initial current and the upper limit given by the final current: the final current is $(14.0\,\text{V} - 12.60\,\text{V}) : 0.40\,\Omega = 3.5\,\text{A}$, and the time would then be $30\,\text{Ah} : 3.5\,\text{A} \approx 8.6\,\text{h}$. The result $7.1\,\text{h}$ lies between these.
