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
**Find:** the burning time $t$ in hours
**Principle:** The lamp draws a constant current, so the charge passing through the battery is current times time. The battery is empty when the charge equals the capacity.
**Formula:** $Q = It$, from which $t = \dfrac{Q}{I}$
**Conversions:** Not needed: the quotient of ampere-hours and amperes is hours.
**Substitution:** $t = \dfrac{2.4\,\text{Ah}}{0.15\,\text{A}} = 16\,\text{h}$
**Answer:** $16\,\text{h}$, two significant figures like the capacity and the current.
**Reasonableness:** With a current of $0.15\,\text{A}$, a charge of $1.5\,\text{Ah}$ passes in ten hours, and $2.4\,\text{Ah}$ is a little over one and a half times that. A burning time of sixteen hours suits a low-power LED flashlight.

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
