## fy6-2-L1-01
**Given:** reading $U = 12.46\,\text{V}$ on the range $20\,\text{V}$, resolution $r = 0.01\,\text{V}$, error limit $\pm(0.5\,\% + 2\ \text{digits})$
**Find:** the error limit $\Delta U$ of the reading in volts
**Principle:** The error limit given by the manufacturer consists of two parts: a share of the reading and a few steps of the last digit. One "digit" means the resolution of the range, that is the smallest step that the display can take, here $0.01\,\text{V}$.
**Formula:** $\Delta U = p \cdot U + n \cdot r$
**Conversions:** $p = 0.5\,\% = 0.005$; no other conversions are needed, because the reading and the resolution are in volts.
**Substitution:** $\Delta U = 0.005 \cdot 12.46\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.0623\,\text{V} + 0.02\,\text{V} = 0.0823\,\text{V}$
**Answer:** $0.08\,\text{V}$, one significant figure, because an error limit is rounded like an error estimate (calculator value $0.0823\,\text{V}$).
**Reasonableness:** The percentage part is about half of a hundredth of $12\,\text{V}$, that is about $0.06\,\text{V}$, and two steps add $0.02\,\text{V}$: altogether about $0.08\,\text{V}$. The error limit is less than a percent of the reading, which suits a good meter.

## fy6-2-L1-02
**Given:** reading $I = 146.3\,\text{mA}$ on the range $200\,\text{mA}$, resolution $r = 0.1\,\text{mA}$, error limit $\pm(1.0\,\% + 2\ \text{digits})$
**Find:** the error limit $\Delta I$ of the reading in milliamperes
**Principle:** The error limit is a percentage of the reading plus two steps of the last digit. On the range $200\,\text{mA}$ the last digit is a tenth of a milliampere, so one step is $0.1\,\text{mA}$.
**Formula:** $\Delta I = p \cdot I + n \cdot r$
**Conversions:** $p = 1.0\,\% = 0.010$; the reading and the resolution are already in milliamperes.
**Substitution:** $\Delta I = 0.010 \cdot 146.3\,\text{mA} + 2 \cdot 0.1\,\text{mA} = 1.463\,\text{mA} + 0.2\,\text{mA} = 1.663\,\text{mA}$
**Answer:** $1.7\,\text{mA}$, two significant figures, because the first figure of the error limit is 1.
**Reasonableness:** A percent of $146\,\text{mA}$ is about $1.5\,\text{mA}$, and the share of the digits $0.2\,\text{mA}$ is smaller, because the reading is close to the upper limit of the range. The result is a little over a percent of the reading.

## fy6-2-L1-03
**Given:** reading $U = 8.00\,\text{V}$, error limit $\Delta U = 0.06\,\text{V}$
**Find:** the relative error limit $s$ as a percentage
**Principle:** The relative error limit tells what part of the reading the error limit is. It makes the accuracy of measurements of different sizes comparable.
**Formula:** $s = \dfrac{\Delta U}{U}$
**Conversions:** Not needed: both are in volts, and the unit cancels. The result is multiplied by a hundred to get it as a percentage.
**Substitution:** $s = \dfrac{0.06\,\text{V}}{8.00\,\text{V}} = 0.0075 = 0.75\,\%$
**Answer:** $0.8\,\%$, one significant figure like the error limit $0.06\,\text{V}$.
**Reasonableness:** A percent of $8\,\text{V}$ would be $0.08\,\text{V}$; the error limit $0.06\,\text{V}$ is a little smaller, so the result must be a little under $1\,\%$, and $0.8\,\%$ is.

## fy6-2-L1-04
**Given:** a circuit without branches in which a battery, a lamp and a resistor are one after another; current between the battery and the lamp $I = 0.180\,\text{A}$
**Find:** the reading of the ammeter between the lamp and the resistor in amperes
**Principle:** In a circuit without branches the current is the same at every point: charge neither disappears nor accumulates anywhere, so the same amount of charge passes through every cross-section in a second. A lamp changes electrical energy into light and internal energy of the filament, but it does not use up current.
**Formula:** $I_\text{after} = I_\text{before}$
**Conversions:** Not needed: the current is in amperes.
**Substitution:** $I_\text{after} = 0.180\,\text{A}$
**Answer:** $0.180\,\text{A}$, three significant figures like the reading of the meter.
**Reasonableness:** If a smaller current passed after the lamp, more and more charge would accumulate in the lamp all the time, and that is not observed. In the simulation the ammeter showed the same reading at both points.

## fy6-2-L1-05
**Given:** reading $U = 1.587\,\text{V}$ on the range $2\,\text{V}$, resolution $r = 0.001\,\text{V}$, error limit $\pm(0.5\,\% + 2\ \text{digits})$
**Find:** the error limit $\Delta U$ of the reading in volts
**Principle:** The manufacturer's error limit is a share of the reading plus two steps of the last digit. On the range $2\,\text{V}$ the display has three decimals, so the step is $0.001\,\text{V}$.
**Formula:** $\Delta U = p \cdot U + n \cdot r$
**Conversions:** $p = 0.5\,\% = 0.005$; the reading and the resolution are in volts.
**Substitution:** $\Delta U = 0.005 \cdot 1.587\,\text{V} + 2 \cdot 0.001\,\text{V} = 0.007935\,\text{V} + 0.002\,\text{V} = 0.009935\,\text{V}$
**Answer:** $0.010\,\text{V}$, or $10\,\text{mV}$: the calculator value $0.009935\,\text{V}$ rounds to one significant figure as $0.01\,\text{V}$, and because the first figure is 1, the error limit is given with two figures.
**Reasonableness:** Half a percent of $1.6\,\text{V}$ is about $8\,\text{mV}$, and two steps add $2\,\text{mV}$: altogether about $10\,\text{mV}$. On the range $20\,\text{V}$ the share of the digits alone would be $20\,\text{mV}$, so the small range is clearly more accurate here.

## fy6-2-L2-01
**Given:** reading $I = 0.35\,\text{A}$ on the range $10\,\text{A}$, resolution $r = 0.01\,\text{A}$, error limit $\pm(2.0\,\% + 3\ \text{digits})$
**Find:** the relative error limit $\dfrac{\Delta I}{I}$ as a percentage
**Principle:** First the error limit is calculated from the manufacturer's statement: a share of the reading and three steps of the last digit. Then the error limit is compared with the reading. When the reading is small compared with the range, the share of the digits is large.
**Formula:** $\Delta I = p \cdot I + n \cdot r$, so $\dfrac{\Delta I}{I} = \dfrac{p \cdot I + n \cdot r}{I}$
**Conversions:** $p = 2.0\,\% = 0.020$; all currents are in amperes.
**Substitution:** $\Delta I = 0.020 \cdot 0.35\,\text{A} + 3 \cdot 0.01\,\text{A} = 0.007\,\text{A} + 0.03\,\text{A} = 0.037\,\text{A}$, so $\dfrac{\Delta I}{I} = \dfrac{0.037\,\text{A}}{0.35\,\text{A}} = 0.106 = 10.6\,\%$
**Answer:** about $11\,\%$, two significant figures, because the first digit is 1.
**Reasonableness:** Three steps, that is $0.03\,\text{A}$, are already almost a tenth of the reading $0.35\,\text{A}$, and the percentage part adds a little. The current $0.35\,\text{A}$ does not fit on the range $200\,\text{mA}$, so $10\,\text{A}$ is the smallest suitable range here; the error limit is still almost $11\,\%$, because the reading is small compared with the range, and a more accurate range for large currents would help.

## fy6-2-L2-02
**Given:** reading $I = 0.0875\,\text{A}$ on the range $200\,\text{mA}$, resolution $r = 0.1\,\text{mA}$, error limit $\pm(1.0\,\% + 2\ \text{digits})$
**Find:** the error limit $\Delta I$ of the reading in amperes
**Principle:** The error limit is a share of the reading plus two steps of the last digit. The reading and the resolution are given in different units, so they are converted to the same unit before adding.
**Formula:** $\Delta I = p \cdot I + n \cdot r$
**Conversions:** $p = 1.0\,\% = 0.010$ and $r = 0.1\,\text{mA} = 0.1 \cdot 0.001\,\text{A} = 0.0001\,\text{A}$
**Substitution:** $\Delta I = 0.010 \cdot 0.0875\,\text{A} + 2 \cdot 0.0001\,\text{A} = 0.000875\,\text{A} + 0.0002\,\text{A} = 0.001075\,\text{A}$
**Answer:** $0.0011\,\text{A}$, or about $1.1\,\text{mA}$, two significant figures, because the first figure of the error limit is 1.
**Reasonableness:** The display shows $87.5\,\text{mA}$; a percent of it is about $0.9\,\text{mA}$ and two steps $0.2\,\text{mA}$, altogether about $1.1\,\text{mA}$. If the resolution were not converted to amperes, one would get the absurd result $0.2\,\text{A}$, which is larger than the current itself.

## fy6-2-L2-03
**Given:** on the range $2\,\text{V}$ the reading $U_2 = 1.234\,\text{V}$ and the resolution $r_2 = 0.001\,\text{V}$; on the range $20\,\text{V}$ the reading $U_{20} = 1.23\,\text{V}$ and the resolution $r_{20} = 0.01\,\text{V}$; for both the error limit $\pm(0.5\,\% + 2\ \text{digits})$
**Find:** the ratio of the error limits $\dfrac{\Delta U_{20}}{\Delta U_2}$ as a pure number
**Principle:** The percentage part is almost the same on both ranges, because the reading is the same. The difference comes from the share of the digits: on the larger range the last digit is ten times coarser.
**Formula:** $\Delta U = p \cdot U + n \cdot r$, so $\dfrac{\Delta U_{20}}{\Delta U_2} = \dfrac{p \cdot U_{20} + n \cdot r_{20}}{p \cdot U_2 + n \cdot r_2}$
**Conversions:** $p = 0.5\,\% = 0.005$; the voltages are in volts.
**Substitution:** $\Delta U_2 = 0.005 \cdot 1.234\,\text{V} + 2 \cdot 0.001\,\text{V} = 0.00817\,\text{V}$ and $\Delta U_{20} = 0.005 \cdot 1.23\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.02615\,\text{V}$, so $\dfrac{\Delta U_{20}}{\Delta U_2} = \dfrac{0.02615\,\text{V}}{0.00817\,\text{V}} = 3.20$
**Answer:** $3.2$; the ratio is calculated from the unrounded error limits, and because they are estimates, two figures are enough: the error limit of the range $20\,\text{V}$ is about three times as large.
**Reasonableness:** If the error limit consisted of digits only, the ratio would be $10$; if of the percentage part only, it would be $1$. The result is between these, closer to the small end, because the percentage part $0.006\,\text{V}$ on the range $2\,\text{V}$ is larger than the share of the digits $0.002\,\text{V}$.

## fy6-2-L2-04
**Given:** voltage of the battery $9.0\,\text{V}$; a voltmeter in series with the lamp; the resistance of the meter is very large compared with the resistance of the lamp; the lamp goes out
**Find:** the reading of the voltmeter $U_\text{m}$ in volts
**Principle:** A voltmeter lets through only a very small current, so connected in series it decreases the current of the whole circuit to almost zero. Then hardly any voltage is left across the lamp, because the voltage of the lamp is its resistance times the almost zero current, and the whole voltage of the battery is left between the terminals of the meter.
**Formula:** $U_\text{m} + U_\text{lamp} = U_\text{battery}$ and $U_\text{lamp} \approx 0$, so $U_\text{m} \approx U_\text{battery}$
**Conversions:** Not needed: the voltage is in volts.
**Substitution:** $U_\text{m} \approx 9.0\,\text{V}$
**Answer:** about $9.0\,\text{V}$, two significant figures like the voltage of the battery.
**Reasonableness:** In the simulation the voltmeter connected in series showed the voltage of the battery $4.50\,\text{V}$, and the lamp went out. The reading cannot be larger than the voltage of the battery, and because the current is almost zero, it is hardly smaller either.

## fy6-2-L3-01
**Given:** the voltage left across the meter $1.0\,\text{mV}$ per milliampere on the range $200\,\text{mA}$, reading of the meter $I = 97.8\,\text{mA}$, voltage of the batteries $U_0 = 4.5\,\text{V}$, an ideal battery
**Find:** the share of the voltage left across the meter, $\dfrac{U_\text{m}}{U_0}$, as a percentage
**Principle:** The resistance of a real ammeter is not zero, so a small voltage is left across the meter. According to the manual it grows in the same proportion as the current passing through the meter. This voltage is taken away from the lamp and the resistor, so the meter decreases the current of the circuit slightly.
**Formula:** $U_\text{m} = k \cdot I$, where $k = 1.0\,\tfrac{\text{mV}}{\text{mA}}$, so $\dfrac{U_\text{m}}{U_0} = \dfrac{k \cdot I}{U_0}$
**Conversions:** $U_0 = 4.5\,\text{V} = 4.5 \cdot 1000\,\text{mV} = 4500\,\text{mV}$
**Substitution:** $U_\text{m} = 1.0\,\tfrac{\text{mV}}{\text{mA}} \cdot 97.8\,\text{mA} = 97.8\,\text{mV}$, so $\dfrac{U_\text{m}}{U_0} = \dfrac{97.8\,\text{mV}}{4500\,\text{mV}} = 0.0217 = 2.17\,\%$
**Answer:** $2.2\,\%$, two significant figures like the voltage drop $1.0\,\text{mV}$ per milliampere and the voltage of the batteries $4.5\,\text{V}$.
**Reasonableness:** About $100\,\text{mA}$ gives about $100\,\text{mV}$, that is $0.1\,\text{V}$, and $0.1\,\text{V} : 4.5\,\text{V} \approx 0.022$. The meter takes a few percent of the voltage from the circuit, so it decreases the current by the same amount: without the meter the current would be about $100\,\text{mA}$, which fits the readings of the simulation $97.8\,\text{mA}$ and $0.10\,\text{A}$.

## fy6-2-L3-02
**Given:** meter A: reading $U_\text{A} = 5.02\,\text{V}$, error limit $\pm(0.5\,\% + 2\ \text{digits})$; meter B: reading $U_\text{B} = 5.14\,\text{V}$, error limit $\pm(1.5\,\% + 3\ \text{digits})$; for both resolution $r = 0.01\,\text{V}$; difference of the readings $0.12\,\text{V}$
**Find:** the sum of the error limits $\Delta U_\text{A} + \Delta U_\text{B}$ in volts, and whether the difference can be taken as evidence of a fault
**Principle:** According to the manufacturer, the true value is within its own error limit of each reading. The readings are in agreement if their intervals overlap, that is if the difference is smaller than the sum of the error limits. Then the difference cannot be shown to be due to a fault in the meters.
**Formula:** $\Delta U = p \cdot U + n \cdot r$, so $\Delta U_\text{A} + \Delta U_\text{B} = p_\text{A} \cdot U_\text{A} + n_\text{A} \cdot r + p_\text{B} \cdot U_\text{B} + n_\text{B} \cdot r$
**Conversions:** $p_\text{A} = 0.5\,\% = 0.005$ and $p_\text{B} = 1.5\,\% = 0.015$; the voltages are in volts.
**Substitution:** $\Delta U_\text{A} = 0.005 \cdot 5.02\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.0451\,\text{V}$ and $\Delta U_\text{B} = 0.015 \cdot 5.14\,\text{V} + 3 \cdot 0.01\,\text{V} = 0.1071\,\text{V}$, so $\Delta U_\text{A} + \Delta U_\text{B} = 0.0451\,\text{V} + 0.1071\,\text{V} = 0.1522\,\text{V}$
**Answer:** $0.15\,\text{V}$, two significant figures, because the first figure of the sum of the error limits is 1. The difference of the readings $0.12\,\text{V}$ is smaller than $0.15\,\text{V}$, so the intervals $4.97$–$5.07\,\text{V}$ and $5.03$–$5.25\,\text{V}$ overlap: on the basis of the difference neither meter can be said to be faulty. However, this does not prove that the meters would always show the same.
**Reasonableness:** The error limit of the cheaper meter is more than twice as large, as its larger percentage and number of digits lead one to expect. The difference $0.12\,\text{V}$ is about $2\,\%$ of the reading, which is of the same order of magnitude as the error limit of meter B.

## fy6-2-L3-03
**Find:** what happened in the circuit, why the lamp went out only for a moment and the display stayed at zero, and how the current of the lamp should have been measured
**Principle:** On the current range the resistance of a multimeter is very small, so that the meter connected in series would not change the current of the circuit. Inside the meter there is a fuse, which blows and interrupts the current path of the meter when too large a current passes through the meter.
**Model answer:** The student connected the ammeter in parallel with the lamp, although an ammeter is connected in series. A parallel path of very small resistance formed between the terminals of the lamp, so almost the whole current passed through the meter past the lamp. The lamp went out, because no current passed through it any more. Because on the path from the battery through the meter back to the battery there was hardly anything limiting the current, the current grew much larger than the measuring range $200\,\text{mA}$, and the fuse of the meter blew. The blown fuse interrupted the current through the meter, so the meter was left out of the circuit: the battery and the lamp again formed just a closed circuit, and the lamp lit up again. The display stayed at zero, because no current passes through the meter until the fuse is replaced. When measuring correctly, the circuit is opened, for example between the battery and the lamp, and the ammeter is placed in the gap, so the same current passes through the battery, the meter and the lamp. If the size of the current is not known, we start from the range $10\,\text{A}$ and move the red lead to the jack that belongs to it.

**Self-assessment:** In my answer I

- say that the ammeter was connected in parallel with the lamp, although it belongs in series
- explain that the small resistance of the meter directed the current past the lamp, which is why the lamp went out
- explain that the current grew so large that the fuse of the meter blew, after which the meter was out of the circuit, the lamp lit up again and the display stayed at zero
- tell that the circuit is opened and the meter is placed in the gap, so that the same current passes through the meter and the lamp.
