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

## fy6-2-L1-06
**Find:** how an ammeter is connected to measure the current passing through a lamp.
**Principle:** Current is the flow of charge through the cross-section of a conductor, so the whole current to be measured must pass through the ammeter. That is why an ammeter is connected in series: the circuit is opened and the meter is placed in the gap. The resistance of an ammeter is very small, so connected in parallel it would direct the current past the component and make a short circuit.
**Model answer:** The circuit is opened, for example between the battery and the lamp, and the ammeter is placed in the gap. Then the same current passes through the battery, the meter and the lamp, and the meter shows the current of the lamp. The meter is not connected between the terminals of the lamp, because that is how a voltmeter is connected and the small resistance of an ammeter would cause a short circuit. It is not connected between the terminals of the battery either, nor left next to the lamp without wires, because a meter measures only the current passing through its own conductor.

## fy6-2-L1-07
**Find:** why the resistance of a voltmeter must be very large.
**Principle:** A voltmeter is connected in parallel, so part of the current of the circuit passes through the meter. The larger the resistance of the meter, the smaller the current passing through it, and a current taken away from the component would change exactly the voltage we are trying to measure.
**Model answer:** When the resistance of a voltmeter is very large, only a very small current passes through the meter. Then the meter does not take current from the component being measured and does not change the circuit, and the reading is close to the voltage that the component had before the meter. A large resistance does not amplify the voltage, does not increase the current through the meter and has nothing to do with the heating of the leads. For the same reason the resistance of an ammeter must, on the contrary, be very small.

## fy6-2-L1-08
**Given:** reading $U = 5.98\,\text{V}$ on the range $20\,\text{V}$, resolution $r = 0.01\,\text{V}$, error limit $\pm(0.5\,\% + 2\ \text{digits})$
**Find:** the error limit $\Delta U$ in volts and the measurement result in the form $U \pm \Delta U$
**Principle:** The error limit is a share of the reading plus two steps of the last digit. The measurement result is stated as the reading and the error limit, and the error limit is rounded to one significant figure.
**Formula:** $\Delta U = p \cdot U + n \cdot r$
**Conversions:** $p = 0.5\,\% = 0.005$; the reading and the resolution are already in volts.
**Substitution:** $\Delta U = 0.005 \cdot 5.98\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.0299\,\text{V} + 0.02\,\text{V} = 0.0499\,\text{V}$
**Answer:** $\Delta U = 0.05\,\text{V}$, one significant figure, because the first digit is 4 (calculator value $0.0499\,\text{V}$). The measurement result is $U = 5.98\,\text{V} \pm 0.05\,\text{V}$, that is the interval $5.93$–$6.03\,\text{V}$. The reading is written with the same number of decimals as the error limit.
**Reasonableness:** The error limit $0.05\,\text{V}$ is less than a percent of the reading $5.98\,\text{V}$, because the reading is about a third of the range $20\,\text{V}$ ($5.98 : 20 = 0.30$). The percentage part $0.03\,\text{V}$ and the share of the digits $0.02\,\text{V}$ are of the same order of magnitude, so both matter.

## fy6-2-L2-05
**Given:** example data: on the range $2\,\text{V}$ the reading $1.847\,\text{V}$ and the resolution $0.001\,\text{V}$, on the range $20\,\text{V}$ the reading $1.85\,\text{V}$ and the resolution $0.01\,\text{V}$, on the range $200\,\text{V}$ the reading $1.8\,\text{V}$ and the resolution $0.1\,\text{V}$; the error limit on all ranges $\pm(0.5\,\% + 2\ \text{digits})$
**Find:** a) the error limit on each range, b) the best range and the justification; in the answer box the error limit of the best range in millivolts
**Principle:** The error limit given by the manufacturer is a share of the reading plus two steps of the last digit. The reading is approximately the same on all ranges, so the percentage part is approximately the same and the difference comes from the share of the digits. The smaller the range, the smaller the resolution and the smaller the error limit.
**Formula:** $\Delta U = p \cdot U + n \cdot r$
**Conversions:** $p = 0.5\,\% = 0.005$; the readings and the resolutions are in volts. Finally the result is converted to millivolts: $1\,\text{V} = 1000\,\text{mV}$.
**Substitution:**
$\Delta U_2 = 0.005 \cdot 1.847\,\text{V} + 2 \cdot 0.001\,\text{V} = 0.009235\,\text{V} + 0.002\,\text{V} = 0.011235\,\text{V} = 11.235\,\text{mV}$
$\Delta U_{20} = 0.005 \cdot 1.85\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.00925\,\text{V} + 0.02\,\text{V} = 0.02925\,\text{V} = 29.25\,\text{mV}$
$\Delta U_{200} = 0.005 \cdot 1.8\,\text{V} + 2 \cdot 0.1\,\text{V} = 0.009\,\text{V} + 0.2\,\text{V} = 0.209\,\text{V} = 209\,\text{mV}$
**Answer:** the best range is $2\,\text{V}$, because its error limit is the smallest: $11\,\text{mV}$, two significant figures, because the first digit is 1 (calculator value $11.235\,\text{mV}$). The error limit of the range $20\,\text{V}$ is $29\,\text{mV}$ and that of the range $200\,\text{V}$ is $209\,\text{mV}$. The voltage fits on the range $2\,\text{V}$, so the smallest suitable range gives the most accurate result.
**Reasonableness:** The percentage part is about $9\,\text{mV}$ on all ranges, and the shares of the digits are $2\,\text{mV}$, $20\,\text{mV}$ and $200\,\text{mV}$. On the range $200\,\text{V}$ the error limit $209\,\text{mV}$ is over $11$ percent of the reading $1.8\,\text{V}$, whereas on the range $2\,\text{V}$ it is about $0.6\,\%$.

## fy6-2-L2-06
**Find:** what is done when the display of the meter reads OL on the current range $200\,\text{mA}$.
**Principle:** OL means that the value being measured is above the selected measuring range. It is not a fault message and does not mean zero. When the order of magnitude is not known, the measurement is started from the largest range and moved to the smallest range where the reading fits.
**Model answer:** The current of the lamp is larger than $200\,\text{mA}$, so a larger current range is selected, the current is switched off or the circuit is opened, and only then is the red lead moved to the jack meant for large currents. When the reading is obtained, the range can be changed to the smallest range where the reading fits, so that the error limit becomes smaller. Moving to a smaller range would not help, because the current already exceeds the present range. The meter is not broken, because OL is the ordinary message for an overrange, and the current is not zero, because zero would show as the reading zero.

## fy6-2-L2-07
**Given:** example data: the readings $12.48\,\text{V}$, $12.52\,\text{V}$, $12.46\,\text{V}$, $12.50\,\text{V}$ and $12.49\,\text{V}$ on the range $20\,\text{V}$, resolution $r = 0.01\,\text{V}$, error limit $\pm(0.5\,\% + 2\ \text{digits})$, rest voltage of a fully charged battery $12.60\,\text{V}$
**Find:** a) the mean, b) an estimate of the spread as half of the range of variation, c) the error limit of the meter for the mean, d) consistency with the rest voltage; in the answer box the error limit of part c) in volts
**Principle:** Repeated measurement tells how much the readings spread. Half of the range of variation is a simple estimate of the spread, not the uncertainty of the mean. The error limit of the meter does not become smaller by repeating, because it belongs to the meter. The result is consistent with a reference value if the difference of the values is smaller than the error limit.
**Formula:** $U_\text{avg} = \dfrac{\text{sum of the readings}}{N}$, the estimate of the spread $\dfrac{U_\text{max} - U_\text{min}}{2}$ and the error limit $\Delta U = p \cdot U_\text{avg} + n \cdot r$
**Conversions:** $p = 0.5\,\% = 0.005$; all voltages are in volts.
**Substitution:** a) The sum of the readings is $62.45\,\text{V}$ and the number of readings is $N = 5$, so $U_\text{avg} = 62.45\,\text{V} : 5 = 12.49\,\text{V}$. b) The estimate of the spread is $(12.52\,\text{V} - 12.46\,\text{V}) : 2 = 0.03\,\text{V}$. c) $\Delta U = 0.005 \cdot 12.49\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.06245\,\text{V} + 0.02\,\text{V} = 0.08245\,\text{V}$
**Answer:** the error limit of part c) is $0.08\,\text{V}$, one significant figure, because the first digit is 8 (calculator value $0.08245\,\text{V}$). The mean is $12.49\,\text{V}$ and the estimate of the spread $0.03\,\text{V}$. The difference of the rest voltage and the mean is $12.60\,\text{V} - 12.49\,\text{V} = 0.11\,\text{V}$, which is larger than the error limit $0.08\,\text{V}$. The result $12.49\,\text{V} \pm 0.08\,\text{V}$ is not consistent with the rest voltage of a fully charged battery: the battery is probably partly discharged. Repeating would not help, because the spread $0.03\,\text{V}$ is already small and the error limit belongs to the meter.
**Reasonableness:** The result interval $12.41$–$12.57\,\text{V}$ does not contain the value $12.60\,\text{V}$, but it is close, so the battery is only a little short of full. The error limit $0.08\,\text{V}$ is almost three times the estimate of the spread $0.03\,\text{V}$, so the own error limit of the meter dominates the result and repeating the readings does not make it smaller.

## fy6-2-L3-04
**Given:** an example situation: voltage source $U_0 = 12.0\,\text{V}$ (ideal), resistors $R_1 = R_2 = 1.0\,\text{M}\Omega$ one after another, resistance of the meter $R_\text{m} = 10\,\text{M}\Omega$ in parallel with the resistor $R_2$; error limit of the meter on the range $20\,\text{V}$ $\pm(0.5\,\% + 2\ \text{digits})$, resolution $0.01\,\text{V}$
**Find:** a) the voltage of $R_2$ without the meter, b) the voltage $U$ shown by the meter, c) the decrease of the voltage caused by the meter as a percentage (in the answer box), d) comparison with the error limit and a more reliable measurement
**Principle:** The meter is in parallel with the resistor $R_2$, so they have the same voltage $U$, and the current passing through the meter is taken away from the rest of the current of the circuit. The current through the resistor $R_1$ is the sum of the currents of the resistor $R_2$ and the meter. The voltages are in the same loop: $U_1 + U = U_0$. The current is obtained from the voltage and the resistance of a resistor: $I = U : R$.
**Formula:** $\dfrac{U_0 - U}{R_1} = \dfrac{U}{R_2} + \dfrac{U}{R_\text{m}}$, from which $U = \dfrac{U_0}{1 + \dfrac{R_1}{R_2} + \dfrac{R_1}{R_\text{m}}}$; the decrease $\dfrac{U_\text{without} - U}{U_\text{without}}$
**Conversions:** The ratios of the resistances are plain numbers, so the megaohms do not need to be converted: $\dfrac{R_1}{R_2} = 1.0$ and $\dfrac{R_1}{R_\text{m}} = \dfrac{1.0\,\text{M}\Omega}{10\,\text{M}\Omega} = 0.10$.
**Substitution:** a) Without the meter the resistors have the same current and the same resistance, so the voltage is divided equally: $U_\text{without} = 12.0\,\text{V} : 2 = 6.00\,\text{V}$. b) Multiply the equation $\dfrac{U_0 - U}{R_1} = \dfrac{U}{R_2} + \dfrac{U}{R_\text{m}}$ on both sides by the resistance $R_1$: $U_0 - U = U \cdot \dfrac{R_1}{R_2} + U \cdot \dfrac{R_1}{R_\text{m}}$. Move $U$ to the same side: $U_0 = U \left(1 + \dfrac{R_1}{R_2} + \dfrac{R_1}{R_\text{m}}\right)$, and divide by the bracket. Then $U = \dfrac{12.0\,\text{V}}{1 + 1.0 + 0.10} = \dfrac{12.0\,\text{V}}{2.10} = 5.714\,\text{V}$. c) The decrease is $6.00\,\text{V} - 5.714\,\text{V} = 0.286\,\text{V}$, so $\dfrac{0.286\,\text{V}}{6.00\,\text{V}} = 0.0476 = 4.76\,\%$. d) For the reading $5.71\,\text{V}$ the error limit of the meter is $\Delta U = 0.005 \cdot 5.71\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.0486\,\text{V}$.
**Answer:** the result of part c) is $4.8\,\%$, two significant figures like the given resistances (calculator value $4.76\,\%$). Without the meter the voltage is $6.00\,\text{V}$ and the voltage shown by the meter is $5.71\,\text{V}$. The change $0.286\,\text{V}$ caused by the meter is about $5.9$ times the error limit $0.0486\,\text{V}$. The error limit tells only the internal inaccuracy of the meter, not the effect of the meter on the circuit, so the measurement result $5.71\,\text{V} \pm 0.05\,\text{V}$ is not reliable: the voltage without the meter, $6.00\,\text{V}$, lies outside it. The measurement is more reliable when the resistance of the meter is much larger than that of the component being measured or when the resistors are smaller. If the resistors were $R_1 = R_2 = 10\,\text{k}\Omega$, the effect of the meter would be only $0.05\,\%$.
**Reasonableness:** Substituting back: the current through the resistor $R_1$ is $(12.0 - 5.714)\,\text{V} : 1.0\,\text{M}\Omega = 6.29\,\mu\text{A}$, and it is the sum of the current of the resistor $R_2$ and the current of the meter: $5.714\,\mu\text{A} + 0.571\,\mu\text{A} = 6.29\,\mu\text{A}$. The meter takes almost a tenth of the current of the resistor $R_2$, so the voltage decreases by about $5\,\%$, which fits the result $4.8\,\%$. With the smaller resistors $U = 12.0\,\text{V} : 2.001 = 5.997\,\text{V}$, which is almost $6.00\,\text{V}$.

## fy6-2-L3-05
**Given:** example data: resistance of the voltmeter $10\,\text{M}\Omega$, voltage $U = 4.52\,\text{V}$ on the range $20\,\text{V}$ ($r = 0.01\,\text{V}$, error limit $\pm(0.5\,\% + 2\ \text{digits})$), current $I = 38.4\,\text{mA}$ on the range $200\,\text{mA}$ ($r = 0.1\,\text{mA}$, error limit $\pm(1.0\,\% + 2\ \text{digits})$); the student's claim: $R = 117.71\,\Omega$, so the resistor is not $120\,\Omega$ but faulty
**Find:** a) $R = U : I$, b) the relative error limits, c) the error limit of the resistance $\Delta R$ in ohms (in the answer box), d) evaluation of the conclusion and the correct result
**Principle:** The resistance is calculated from the measurement results as the quotient $R = U : I$, and its error limit is obtained from the rule for a quotient: the relative error limit is the sum of the relative error limits of the voltage and the current. The result is consistent with the nominal value if the nominal value fits in the result interval. A mere difference from the calculated value does not show a fault.
**Formula:** $R = \dfrac{U}{I}$, $\Delta U = p_U \cdot U + n_U \cdot r_U$, $\Delta I = p_I \cdot I + n_I \cdot r_I$ and $\dfrac{\Delta R}{R} = \dfrac{\Delta U}{U} + \dfrac{\Delta I}{I}$
**Conversions:** $p_U = 0.5\,\% = 0.005$ and $p_I = 1.0\,\% = 0.010$; the current is converted to amperes: $I = 38.4\,\text{mA} = 0.0384\,\text{A}$.
**Substitution:** a) $R = \dfrac{4.52\,\text{V}}{0.0384\,\text{A}} = 117.71\,\Omega$. b) $\Delta U = 0.005 \cdot 4.52\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.0426\,\text{V}$, so $\dfrac{\Delta U}{U} = \dfrac{0.0426\,\text{V}}{4.52\,\text{V}} = 0.00942 = 0.94\,\%$. Also $\Delta I = 0.010 \cdot 38.4\,\text{mA} + 2 \cdot 0.1\,\text{mA} = 0.584\,\text{mA}$, so $\dfrac{\Delta I}{I} = \dfrac{0.584\,\text{mA}}{38.4\,\text{mA}} = 0.0152 = 1.5\,\%$. c) The relative error limit is $0.00942 + 0.0152 = 0.0246 = 2.5\,\%$, so $\Delta R = 0.0246 \cdot 117.71\,\Omega = 2.90\,\Omega$.
**Answer:** the error limit of part c) is $\Delta R = 3\,\Omega$, one significant figure (calculator value $2.90\,\Omega$). The measurement result is $R = 118\,\Omega \pm 3\,\Omega$, that is the interval $115$–$121\,\Omega$, and the nominal value $120\,\Omega$ fits in this interval. The student's conclusion is wrong: the difference from the nominal value is $2.3\,\Omega$, which is smaller than the error limit, so the measurement does not show the resistor to be faulty. In the report the result must be given with its error limit and rounded according to the error limit, instead of writing four significant figures without an error limit. The current of the voltmeter is $4.52\,\text{V} : 10\,\text{M}\Omega = 0.45\,\mu\text{A}$, which is only $0.001\,\%$ of the current $38.4\,\text{mA}$, so it can be neglected (the resistance of the meter is large compared with the resistor $118\,\Omega$).
**Reasonableness:** The relative error limits of the voltage and the current are about one and one and a half percent, so their sum is about two and a half percent, and $2.5\,\%$ of $118\,\Omega$ is about $3\,\Omega$. The nominal value $120\,\Omega$ differs from the measurement result by about $2\,\%$ ($2.29\,\Omega : 117.71\,\Omega = 1.95\,\%$), which is less than $2.5\,\%$.

## fy6-2-L2-08
**Find:** which line of the student's measurement plan is wrong, when the current and the voltage of a lamp are measured with multimeters.
**Principle:** An ammeter is connected in series and a voltmeter in parallel. The measurement of an unknown value is started on the largest range, but the final reading is read on the smallest range on which the value fits. The error limit of a reading is $\Delta x = p \cdot x + n \cdot r$, and on a small range the resolution $r$ is smaller.
**Model answer:** Line 1 is correct: the current must pass through the meter, so the meter is in series with the lamp.

Line 2 is correct: the order of magnitude is not known, so one starts from the range $10\,\text{A}$ so that the fuse does not blow.

Line 3 is wrong. The reading $0.14\,\text{A} = 140\,\text{mA}$ fits the range $200\,\text{mA}$. The error limits on the range $10\,\text{A}$ are

$\Delta I = 0.020 \cdot 0.14\,\text{A} + 3 \cdot 0.01\,\text{A}$

$\Delta I \approx 0.033\,\text{A} = 33\,\text{mA}$ (intermediate result, about $0.03\,\text{A}$)

and on the range $200\,\text{mA}$, when the reading is about $140.0\,\text{mA}$ and $2 \cdot 0.1\,\text{mA} = 0.2\,\text{mA}$,

$\Delta I = 0.010 \cdot 140\,\text{mA} + 0.2\,\text{mA}$

$\Delta I = 1.6\,\text{mA}$

On the large range the error limit is thus about twenty times as large. The final current is read on the range $200\,\text{mA}$.

Line 4 is correct: the voltmeter is in parallel with the lamp, and on the range $2\,\text{V}$ the display shows at most $1.999\,\text{V}$, so $4.38\,\text{V}$ would give OL. The smallest range on which the reading fits is $20\,\text{V}$.

The correct answer is line 3.

## fy6-2-L2-09
**Given:** the figure: display reading $U = 1.37\,\text{V}$ and the selector on the range $20\,\text{V}$; error limit $\pm(0.5\,\% + 2\ \text{digits})$
**Find:** the error limit $\Delta U$ of the reading in volts
**Principle:** The manufacturer's error limit is a share of the reading plus two steps of the last digit. The reading and the range are read from the figure, because the resolution depends on the range.
**Reading the graph:** The display shows $1.37\,\text{V}$, so the reading is $U = 1.37\,\text{V}$. The pointer of the selector is on the range $20\,\text{V}$, and the display has two decimals, so the step of the last digit, the resolution, is $r = 0.01\,\text{V}$.
**Formula:** $\Delta U = p \cdot U + n \cdot r$
**Conversions:** $p = 0.5\,\% = 0.005$. All voltages are in volts.
**Substitution:** $\Delta U = 0.005 \cdot 1.37\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.00685\,\text{V} + 0.02\,\text{V} = 0.02685\,\text{V}$
**Answer:** $\Delta U \approx 0.03\,\text{V}$, so $U = 1.37\,\text{V} \pm 0.03\,\text{V}$. The error limit is rounded to one significant figure.
**Reasonableness:** The share of the digits, $0.02\,\text{V}$, is most of the error limit, because the reading is small compared with the range $20\,\text{V}$. The error limit is about $2\,\%$ of the reading, and the same follows from $0.03\,\text{V} : 1.37\,\text{V} = 0.02$.

## fy6-2-L2-10
**Given:** the figure: reading $U = 1.37\,\text{V}$ on the range $20\,\text{V}$; the manufacturer's value $U_0 = 1.45\,\text{V}$; error limit $\pm(0.5\,\% + 2\ \text{digits})$
**Find:** the ratio $\dfrac{U_0 - U}{\Delta U}$ as a pure number and a conclusion
**Principle:** A reading is consistent with the rated value if the difference of the values is at most the error limit of the reading. So the difference is compared with the error limit.
**Reading the graph:** The reading on the display is $U = 1.37\,\text{V}$ and the selector is on the range $20\,\text{V}$, so the resolution is $r = 0.01\,\text{V}$ (two decimals).
**Formula:** $\Delta U = p \cdot U + n \cdot r$ and $\dfrac{U_0 - U}{\Delta U}$
**Conversions:** $p = 0.5\,\% = 0.005$. All voltages are in volts.
**Substitution:** $\Delta U = 0.005 \cdot 1.37\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.02685\,\text{V}$ and the difference is $U_0 - U = 1.45\,\text{V} - 1.37\,\text{V} = 0.08\,\text{V}$, so $\dfrac{0.08\,\text{V}}{0.02685\,\text{V}} = 2.98$
**Answer:** about $3.0$ times. The difference is three times the error limit, that is larger than the error limit, so the reading is not consistent with the manufacturer's value. The error limit of the meter does not explain the difference.
**Reasonableness:** The error limit of the reading gives the interval $1.34\,\text{V}$–$1.40\,\text{V}$, and $1.45\,\text{V}$ is outside it, which fits the ratio $3.0 > 1$. The reason may be, for example, that the lamp is used at a voltage other than the rated one, not the meter.
