## fy6-4-L1-01
**Given:** resistors in series $R_1 = 120\,\Omega$, $R_2 = 220\,\Omega$ and $R_3 = 330\,\Omega$
**Find:** the total resistance $R$ in ohms
**Principle:** In a series connection the same current passes through every resistor and the voltages of the resistors add up. So the total resistance is the sum of the resistances of the resistors.
**Formula:** $R = R_1 + R_2 + R_3$
**Conversions:** Not needed, all the resistances are in ohms.
**Substitution:** $R = 120\,\Omega + 220\,\Omega + 330\,\Omega = 670\,\Omega$
**Answer:** $670\,\Omega$. The precision of a sum is decided by the terms, which are all given to the nearest ohm.
**Reasonableness:** The total resistance of a series connection is greater than the largest of the resistors, $330\,\Omega$. The result is about twice the largest resistor, which fits, because the other two resistors together are $340\,\Omega$.

## fy6-4-L1-02
**Given:** resistors in parallel $R_1 = 40\,\Omega$ and $R_2 = 60\,\Omega$
**Find:** the total resistance $R$ in ohms
**Principle:** In a parallel connection the same voltage is across both resistors and the branch currents add up. So the reciprocal of the total resistance is the sum of the reciprocals of the branch resistances.
**Formula:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$, so $R = \dfrac{R_1 R_2}{R_1 + R_2}$
**Conversions:** Not needed, both resistances are in ohms.
**Substitution:** $R = \dfrac{40\,\Omega \cdot 60\,\Omega}{40\,\Omega + 60\,\Omega} = \dfrac{2400\,\Omega^2}{100\,\Omega} = 24\,\Omega$
**Answer:** $24\,\Omega$, two significant figures like the values of the resistors.
**Reasonableness:** The total resistance of a parallel connection is smaller than the smaller of the resistors, $40\,\Omega$. If both resistors were $40\,\Omega$, the result would be half, that is, $20\,\Omega$; here one resistor is larger, so the result is a little over $20\,\Omega$.

## fy6-4-L1-03
**Given:** currents of the lamps connected in parallel $I_1 = 0.20\,\text{A}$, $I_2 = 0.45\,\text{A}$ and $I_3 = 0.85\,\text{A}$
**Find:** the current $I$ leaving the battery
**Principle:** In a parallel connection the current divides into the branches and joins again. Charge neither disappears nor accumulates at the branching points, so the current leaving the battery is the sum of the branch currents.
**Formula:** $I = I_1 + I_2 + I_3$
**Conversions:** Not needed, all the currents are in amperes.
**Substitution:** $I = 0.20\,\text{A} + 0.45\,\text{A} + 0.85\,\text{A} = 1.50\,\text{A}$
**Answer:** $1.50\,\text{A}$, to the nearest hundredth of an ampere like all the terms.
**Reasonableness:** The current leaving the battery is greater than any of the branch currents, because each lamp is a route of its own. With rounded numbers $0.2\,\text{A} + 0.5\,\text{A} + 0.8\,\text{A} = 1.5\,\text{A}$.

## fy6-4-L1-04
**Given:** lamps in series, battery voltage $U = 4.5\,\text{V}$, voltage of the first lamp $U_1 = 1.8\,\text{V}$
**Find:** the voltage $U_2$ of the second lamp
**Principle:** In a series connection the battery voltage is shared between the components: each charge passes through both lamps, and its energy is transformed into light and internal energy of the filaments in the lamps. The sum of the voltages of the lamps is the battery voltage.
**Formula:** $U = U_1 + U_2$, so $U_2 = U - U_1$
**Conversions:** Not needed, the voltages are in volts.
**Substitution:** $U_2 = 4.5\,\text{V} - 1.8\,\text{V} = 2.7\,\text{V}$
**Answer:** $2.7\,\text{V}$, to the nearest tenth of a volt like the given voltages.
**Reasonableness:** The voltage of each lamp is smaller than the battery voltage, and together $1.8\,\text{V} + 2.7\,\text{V} = 4.5\,\text{V}$. The same current passes through the lamps, so the larger voltage is across the lamp with the larger resistance.

## fy6-4-L1-05
**Given:** three resistors in parallel, each $R_1 = 330\,\Omega$
**Find:** the total resistance $R$ in ohms
**Principle:** In a parallel connection the same voltage is across every resistor and the branch currents add up, so the reciprocal of the total resistance is the sum of the reciprocals of the branches. When the resistors are equal, the sum is three times one reciprocal.
**Formula:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_1} + \dfrac{1}{R_1} = \dfrac{3}{R_1}$, so $R = \dfrac{R_1}{3}$
**Conversions:** Not needed, the resistance is in ohms.
**Substitution:** $R = \dfrac{330\,\Omega}{3} = 110\,\Omega$
**Answer:** $110\,\Omega$, three significant figures like the resistance $330\,\Omega$.
**Reasonableness:** Three identical branches conduct three times as well as one, so the resistance is a third. The result is smaller than the $330\,\Omega$ of one resistor, as it should be in a parallel connection.

## fy6-4-L2-01
**Given:** resistors in series $R_1 = 1.2\,\text{k}\Omega$ and $R_2 = 680\,\Omega$, battery voltage $U = 9.0\,\text{V}$
**Find:** the current $I$ of the circuit in milliamperes
**Principle:** In a series connection there is only one route, so the same current passes through both resistors. The connection can be replaced with the total resistance, which is the sum of the resistances, and the current is obtained from Ohm's law.
**Formula:** $R = R_1 + R_2$ and $U = RI$, so $I = \dfrac{U}{R_1 + R_2}$
**Conversions:** $R_1 = 1.2\,\text{k}\Omega = 1.2 \cdot 1000\,\Omega = 1200\,\Omega$. At the end $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $I = \dfrac{9.0\,\text{V}}{1200\,\Omega + 680\,\Omega} = \dfrac{9.0\,\text{V}}{1880\,\Omega} = 0.004\,787\,\text{A} = 4.787\,\text{mA}$
**Answer:** $4.8\,\text{mA}$, two significant figures like the voltage $9.0\,\text{V}$ and the resistance $1.2\,\text{k}\Omega$.
**Reasonableness:** The total resistance is about $2\,\text{k}\Omega$, so the current is about $9\,\text{V} : 2000\,\Omega \approx 4.5\,\text{mA}$. With resistors of kilohms and a battery the currents are typically milliamperes.

## fy6-4-L2-02
**Given:** voltage of the lamp $U_\text{L} = 2.5\,\text{V}$ and current $I = 0.10\,\text{A}$, battery voltage $U = 6.0\,\text{V}$
**Find:** the resistance $R_\text{s}$ of the series resistor
**Principle:** The lamp and the resistor are in series, so the same current $I$ must pass through both, and the battery voltage is shared between them. Across the resistor is the part of the voltage that is not left for the lamp, and its resistance is obtained from Ohm's law.
**Formula:** $U = U_\text{L} + U_\text{s}$ and $U_\text{s} = R_\text{s} I$, so $R_\text{s} = \dfrac{U - U_\text{L}}{I}$
**Conversions:** Not needed: the voltages are in volts and the current in amperes, and $\tfrac{\text{V}}{\text{A}} = \Omega$.
**Substitution:** $R_\text{s} = \dfrac{6.0\,\text{V} - 2.5\,\text{V}}{0.10\,\text{A}} = \dfrac{3.5\,\text{V}}{0.10\,\text{A}} = 35\,\Omega$
**Answer:** $35\,\Omega$, two significant figures like the current $0.10\,\text{A}$.
**Reasonableness:** There is more voltage across the resistor than across the lamp, so the resistance of the resistor is greater than that of the lamp, $2.5\,\text{V} : 0.10\,\text{A} = 25\,\Omega$. Check: the total resistance $35\,\Omega + 25\,\Omega = 60\,\Omega$ gives the current $6.0\,\text{V} : 60\,\Omega = 0.10\,\text{A}$.

## fy6-4-L2-03
**Given:** resistors in parallel $R_1 = 30\,\Omega$ and an unknown $R_2$, battery voltage $U = 6.0\,\text{V}$, current leaving the battery $I = 0.50\,\text{A}$
**Find:** the resistance $R_2$ of the unknown resistor
**Principle:** In a parallel connection the battery voltage is across both resistors, and the current leaving the battery is the sum of the branch currents. The current of the known resistor is obtained from Ohm's law, and the rest of the current passes through the unknown resistor.
**Formula:** $I = I_1 + I_2$, $I_1 = \dfrac{U}{R_1}$ and $I_2 = \dfrac{U}{R_2}$, so $R_2 = \dfrac{U}{I - \dfrac{U}{R_1}}$
**Conversions:** Not needed: the voltage is in volts, the current in amperes and the resistance in ohms.
**Substitution:** $I_1 = \dfrac{6.0\,\text{V}}{30\,\Omega} = 0.20\,\text{A}$ and $R_2 = \dfrac{6.0\,\text{V}}{0.50\,\text{A} - 0.20\,\text{A}} = \dfrac{6.0\,\text{V}}{0.30\,\text{A}} = 20\,\Omega$
**Answer:** $20\,\Omega$, two significant figures like the given values.
**Reasonableness:** A larger current, $0.30\,\text{A}$, passes through the unknown branch, so its resistance is smaller than $30\,\Omega$. Check with the total resistance: $\dfrac{30\,\Omega \cdot 20\,\Omega}{50\,\Omega} = 12\,\Omega$ and $6.0\,\text{V} : 12\,\Omega = 0.50\,\text{A}$.

## fy6-4-L2-04
**Given:** resistors in parallel $R_1 = 2.2\,\text{k}\Omega$ and $R_2 = 3.3\,\text{k}\Omega$
**Find:** the total resistance $R$ in kilohms
**Principle:** In a parallel connection the same voltage is across both resistors and the branch currents add up, so the reciprocal of the total resistance is the sum of the reciprocals. For two resistors it can be solved in advance.
**Formula:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$, so $R = \dfrac{R_1 R_2}{R_1 + R_2}$
**Conversions:** $R_1 = 2.2 \cdot 1000\,\Omega = 2200\,\Omega$ and $R_2 = 3.3 \cdot 1000\,\Omega = 3300\,\Omega$. At the end $1\,\text{k}\Omega = 1000\,\Omega$.
**Substitution:** $R = \dfrac{2200\,\Omega \cdot 3300\,\Omega}{2200\,\Omega + 3300\,\Omega} = \dfrac{7\,260\,000\,\Omega^2}{5500\,\Omega} = 1320\,\Omega = 1.32\,\text{k}\Omega$
**Answer:** $1.3\,\text{k}\Omega$, two significant figures like the values of the resistors.
**Reasonableness:** The result is smaller than the smaller resistor, $2.2\,\text{k}\Omega$. With two $2.2\,\text{k}\Omega$ resistors the result would be $1.1\,\text{k}\Omega$, and here the other resistor is larger, so the result is a little greater. The calculation could also have been done directly in kilohms, because the unit is in both the numerator and the denominator.

## fy6-4-L3-01
**Given:** from the figure, battery voltage $U = 12\,\text{V}$, resistor $R_1 = 40\,\Omega$ in series with the parallel resistors $R_2 = 60\,\Omega$ and $R_3 = 120\,\Omega$
**Find:** the current $I_3$ of resistor $R_3$ in milliamperes
**Principle:** The parallel resistors $R_2$ and $R_3$ are replaced with one resistor $R_{23}$, which is in series with $R_1$. The current leaving the battery passes through $R_1$ and through the whole parallel part. The voltage of the parallel part is the same across both branches, so the current of $R_3$ is obtained from it by Ohm's law.
**Reading the figure:** From the figure we read the values $12\,\text{V}$, $R_1 = 40\,\Omega$, $R_2 = 60\,\Omega$ and $R_3 = 120\,\Omega$. The resistors $R_2$ and $R_3$ are between the same two branching points, that is, in parallel, and the whole current leaving the battery passes through $R_1$ and then through the parallel part, so $R_1$ and the parallel part are one after the other, that is, in series.
**Formula:** $R_{23} = \dfrac{R_2 R_3}{R_2 + R_3}$, $I = \dfrac{U}{R_1 + R_{23}}$, $U_{23} = R_{23} I$, so $I_3 = \dfrac{U_{23}}{R_3}$
**Conversions:** Not needed during the calculation. At the end $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $R_{23} = \dfrac{60\,\Omega \cdot 120\,\Omega}{180\,\Omega} = 40\,\Omega$, $I = \dfrac{12\,\text{V}}{40\,\Omega + 40\,\Omega} = 0.15\,\text{A}$, $U_{23} = 40\,\Omega \cdot 0.15\,\text{A} = 6.0\,\text{V}$ and $I_3 = \dfrac{6.0\,\text{V}}{120\,\Omega} = 0.050\,\text{A} = 50\,\text{mA}$
**Answer:** $50\,\text{mA}$, two significant figures like the voltage $12\,\text{V}$.
**Reasonableness:** The current of $R_2$ is $6.0\,\text{V} : 60\,\Omega = 0.10\,\text{A}$, and the branch currents together are $0.10\,\text{A} + 0.050\,\text{A} = 0.15\,\text{A}$, the same as the current leaving the battery. The branch with the larger resistance carries the smaller current, as it should.

## fy6-4-L3-02
**Given:** two heating resistors, each $R_1 = 46\,\Omega$, mains voltage $U = 230\,\text{V}$; the resistance does not change
**Find:** how many times as large the current $I_\text{parallel}$ is compared with the current $I_\text{series}$
**Principle:** In both connections the same mains voltage is across the heater, so by Ohm's law the current of the heater depends only on the total resistance. The total resistance of equal resistors in series is twice the resistance of one, and in parallel half of it.
**Formula:** $R_\text{series} = 2R_1$ and $R_\text{parallel} = \dfrac{R_1}{2}$, so $\dfrac{I_\text{parallel}}{I_\text{series}} = \dfrac{U : R_\text{parallel}}{U : R_\text{series}} = \dfrac{R_\text{series}}{R_\text{parallel}} = \dfrac{2R_1}{R_1 : 2} = 4$
**Conversions:** Not needed: the voltage and the resistance cancel out of the ratio.
**Substitution:** With numbers $I_\text{series} = \dfrac{230\,\text{V}}{92\,\Omega} = 2.5\,\text{A}$ and $I_\text{parallel} = \dfrac{230\,\text{V}}{23\,\Omega} = 10\,\text{A}$, so $\dfrac{I_\text{parallel}}{I_\text{series}} = \dfrac{10\,\text{A}}{2.5\,\text{A}} = 4.0$
**Answer:** $4$ times. The ratio is exact, because it does not depend on the values of the resistance or the voltage when the resistors are equal.
**Reasonableness:** In the parallel connection the full $230\,\text{V}$ is across each resistor, in the series connection only half. So the current of each resistor is doubled, and there are two branches: altogether four times the current. A larger current means a higher heating power, as the settings of the heater promise.

## fy6-4-L3-03
**Given:** total resistance of the series connection $R_\text{s} = 250\,\Omega$, of the parallel connection $R_\text{r} = 60\,\Omega$
**Find:** the resistance of the larger resistor
**Principle:** In a series connection the resistances add up, and the total resistance of a parallel connection is the product of the resistances divided by their sum. The two equations give the sum and the product of the resistances, and these determine the resistors.
**Formula:** $R_1 + R_2 = R_\text{s}$ and $R_1 R_2 = R_\text{r} R_\text{s}$ (from the formula of the parallel connection). Substituting $R_2 = R_\text{s} - R_1$ gives $R_1^2 - R_\text{s} R_1 + R_\text{r} R_\text{s} = 0$, so $R_1 = \dfrac{R_\text{s} \pm \sqrt{R_\text{s}^2 - 4 R_\text{r} R_\text{s}}}{2}$
**Conversions:** Not needed, both resistances are in ohms.
**Substitution:** $R_\text{r} R_\text{s} = 60\,\Omega \cdot 250\,\Omega = 15\,000\,\Omega^2$ and $R_\text{s}^2 - 4 R_\text{r} R_\text{s} = 62\,500\,\Omega^2 - 60\,000\,\Omega^2 = 2500\,\Omega^2$, whose square root is $50\,\Omega$. So $R_1 = \dfrac{250\,\Omega \pm 50\,\Omega}{2}$, so $R_1 = 150\,\Omega$ or $R_1 = 100\,\Omega$
**Answer:** $150\,\Omega$; the other resistor is $100\,\Omega$. Two significant figures like the value $60\,\Omega$; the data are taken as exact, because the difference $62\,500 - 60\,000$ under the root is small and the result is sensitive to the last digit of the data.
**Reasonableness:** Check: $150\,\Omega + 100\,\Omega = 250\,\Omega$ and $\dfrac{150\,\Omega \cdot 100\,\Omega}{250\,\Omega} = 60\,\Omega$. The result of the parallel connection is smaller than the smaller resistor, $100\,\Omega$, as it should be.

## fy6-4-L1-06
**Find:** which connection of three identical $100\,\Omega$ resistors gives the smallest total resistance.
**Principle:** A resistor added in parallel opens a new route for the current and reduces the total resistance, and a resistor added in series increases it. So the smallest total resistance is obtained when all the resistors are in parallel. Calculating the total resistance of each connection shows the difference: all in parallel $\tfrac{100\,\Omega}{3} \approx 33\,\Omega$, two in series and the third in parallel $\tfrac{200 \cdot 100}{300}\,\Omega \approx 67\,\Omega$, two in parallel and the third in series $50\,\Omega + 100\,\Omega = 150\,\Omega$, and all in series $300\,\Omega$.
**Model answer:** The smallest total resistance is obtained by connecting all three resistors in parallel, because then the current has three parallel routes. The total resistance is $33\,\Omega$, and it is smaller than the resistance of any single resistor. The series connection of all three is the largest ($300\,\Omega$), and the mixed connections fall between these.

## fy6-4-L1-07
**Find:** what happens to the total resistance and to the current leaving the battery when a third lamp is added among the lamps in parallel.
**Principle:** In a parallel connection the battery voltage $U$ is across every branch, and every branch takes a current $I = U : R$. The current leaving the battery is the sum of the branch currents, so a new branch increases it. When the voltage stays the same and the current increases, by Ohm's law the total resistance decreases. Two identical lamps, each with resistance $R_\text{L}$, give $\tfrac{R_\text{L}}{2}$ and three give $\tfrac{R_\text{L}}{3}$.
**Model answer:** The total resistance decreases and the current leaving the battery increases, because the new branch opens more routes for the current. Each of the old lamps takes the same current as before, and the third lamp adds its own current on top of them. Adding resistors increases the total resistance only in a series connection.

## fy6-4-L1-08
**Given:** resistors in parallel $R_1 = 90\,\Omega$ and an unknown $R_x$, total resistance $R = 36\,\Omega$
**Find:** the resistance $R_x$ of the unknown resistor
**Principle:** In a parallel connection the reciprocal of the total resistance is the sum of the reciprocals of the branches. When the total resistance and one branch are known, the reciprocal of the unknown branch is obtained by subtraction, and finally it is inverted.
**Formula:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_x}$, so $\dfrac{1}{R_x} = \dfrac{1}{R} - \dfrac{1}{R_1}$
**Conversions:** Not needed, all the resistances are in ohms.
**Substitution:** $\dfrac{1}{R_x} = \dfrac{1}{36\,\Omega} - \dfrac{1}{90\,\Omega} = \dfrac{5 - 2}{180\,\Omega} = \dfrac{1}{60\,\Omega}$, so $R_x = 60\,\Omega$
**Answer:** $60\,\Omega$, two significant figures like the given values.
**Reasonableness:** The result of the parallel connection, $36\,\Omega$, is smaller than either of the resistors, $90\,\Omega$ and $60\,\Omega$. Check: $\dfrac{90\,\Omega \cdot 60\,\Omega}{90\,\Omega + 60\,\Omega} = \dfrac{5400\,\Omega^2}{150\,\Omega} = 36\,\Omega$.

## fy6-4-L2-05
**Given:** from the table the individual resistances $R_1 = 217\,\Omega$, $R_2 = 328\,\Omega$ and $R_3 = 468\,\Omega$, the measured series connection $1009\,\Omega$ and the measured parallel connection $101.4\,\Omega$; error limit of the meter $\pm 1.5\,\%$ of the reading
**Find:** the calculated total resistance of the parallel connection $R_\text{parallel}$ and whether the difference from the measured value is within the error limit
**Principle:** The formulas of the connections predict the total resistance from the individual resistances. In a series connection the resistances add up, in a parallel connection the reciprocals do. The calculated and measured values are compared by relating the difference to the measured value and comparing it with the error limit.
**Reading the graph:** No graph; the values are read from the table.
**Formula:** $R_\text{series} = R_1 + R_2 + R_3$ and $\dfrac{1}{R_\text{parallel}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3}$
**Conversions:** Not needed, all the resistances are in ohms.
**Substitution:** a) $R_\text{series} = 217\,\Omega + 328\,\Omega + 468\,\Omega = 1013\,\Omega$. The difference from the measured value is $1013\,\Omega - 1009\,\Omega = 4\,\Omega$, that is, $\dfrac{4\,\Omega}{1009\,\Omega} \approx 0.4\,\%$, which is smaller than $1.5\,\%$. b) $\dfrac{1}{R_\text{parallel}} = \dfrac{1}{217\,\Omega} + \dfrac{1}{328\,\Omega} + \dfrac{1}{468\,\Omega} = 0.009\,794\,\dfrac{1}{\Omega}$, so $R_\text{parallel} = 102.1\,\Omega$. The difference from the measured value is $102.1\,\Omega - 101.4\,\Omega = 0.7\,\Omega$, that is, $\dfrac{0.7\,\Omega}{101.4\,\Omega} \approx 0.7\,\%$.
**Answer:** $102\,\Omega$, three significant figures like the measurement results. The difference for the series connection is about $0.4\,\%$ and for the parallel connection about $0.7\,\%$, both within the error limit of $1.5\,\%$, so the measurement supports the formulas of the connections.
**Reasonableness:** The calculated parallel connection is smaller than the smallest individual resistance, $217\,\Omega$, and the series connection is larger than the largest, $468\,\Omega$, as they should be. With rounded numbers $\tfrac{1}{200} + \tfrac{1}{300} + \tfrac{1}{500} = 0.010$, so $R \approx 100\,\Omega$.

## fy6-4-L2-06
**Given:** battery $U = 9.0\,\text{V}$, $R_1 = 100\,\Omega$ in series with $R_2 = R_3 = 200\,\Omega$ in parallel; meter readings $I = 30.2\,\text{mA}$, $U_1 = 3.02\,\text{V}$ and $U_{23} = 5.98\,\text{V}$
**Find:** the resistance $R_{23}$ of the parallel part from the meter readings and the cause of the wiring error
**Principle:** The parallel part is in series with resistor $R_1$, so the current $I$ leaving the battery passes through it. By Ohm's law the resistance of the parallel part is its voltage divided by the current. The result is compared with the value that the formula of the parallel connection gives for the resistors $200\,\Omega$ and $200\,\Omega$.
**Reading the graph:** No graph; the values are read from the table.
**Formula:** $R_{23} = \dfrac{U_{23}}{I}$ and with the correct wiring $R_{23} = \dfrac{R_2 R_3}{R_2 + R_3}$
**Conversions:** $I = 30.2\,\text{mA} = 30.2 \cdot 0.001\,\text{A} = 0.0302\,\text{A}$.
**Substitution:** $R_{23} = \dfrac{5.98\,\text{V}}{0.0302\,\text{A}} = 198\,\Omega$. In a correctly wired circuit $R_{23} = \dfrac{200\,\Omega \cdot 200\,\Omega}{400\,\Omega} = 100\,\Omega$. The resistance of resistor $R_1$ from the meter readings is $\dfrac{3.02\,\text{V}}{0.0302\,\text{A}} = 100\,\Omega$, so $R_1$ is fine.
**Answer:** a) $198\,\Omega$, three significant figures like the readings. In a correctly wired circuit it should be $100\,\Omega$. b) The measured value is approximately the resistance of a single $200\,\Omega$ resistor, so one of the parallel resistors is not part of the circuit: its wire is off or the branch is broken, and the current passes through only one resistor.
**Reasonableness:** If one branch is missing, the total resistance is $100\,\Omega + 200\,\Omega = 300\,\Omega$ and the current is $9.0\,\text{V} : 300\,\Omega = 30\,\text{mA}$, which matches the reading $30.2\,\text{mA}$. The correct wiring would give $9.0\,\text{V} : 200\,\Omega = 45\,\text{mA}$, so the measurement clearly differs from it. The voltages add up: $3.02\,\text{V} + 5.98\,\text{V} = 9.00\,\text{V}$.

## fy6-4-L2-07
**Given:** known resistor $R_1 = 60\,\Omega$ in parallel with an unknown $R_x$; measurements $(U;\ I)$: $(2.0\,\text{V};\ 83\,\text{mA})$, $(4.0\,\text{V};\ 166\,\text{mA})$, $(6.0\,\text{V};\ 247\,\text{mA})$, $(8.0\,\text{V};\ 333\,\text{mA})$ and $(10.0\,\text{V};\ 414\,\text{mA})$
**Find:** the resistance $R_x$ of the unknown resistor
**Principle:** From the point of view of the source, the parallel connection behaves as one resistor whose resistance is obtained from Ohm's law $R = U : I$. The mean of the series of measurements reduces the scatter of a single measurement. When the total resistance and one branch are known, the unknown branch is obtained from the formula of the parallel connection.
**Reading the graph:** No graph; the values are read from the table. If the points were plotted in an $(I;\ U)$ coordinate system, they would lie on a straight line through the origin whose slope is the total resistance.
**Formula:** $R = \dfrac{U}{I}$, $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_x}$, so $\dfrac{1}{R_x} = \dfrac{1}{R} - \dfrac{1}{R_1}$
**Conversions:** $83\,\text{mA} = 83 \cdot 0.001\,\text{A} = 0.083\,\text{A}$, and similarly the other currents.
**Substitution:** a) The ratios $U : I$ are $24.1\,\Omega$, $24.1\,\Omega$, $24.3\,\Omega$, $24.0\,\Omega$ and $24.2\,\Omega$. Their sum is $120.7\,\Omega$, so the mean is $R_\text{avg} = \dfrac{120.7\,\Omega}{5} = 24.13\,\Omega$. b) $\dfrac{1}{R_x} = \dfrac{1}{24.13\,\Omega} - \dfrac{1}{60\,\Omega} = 0.02477\,\dfrac{1}{\Omega}$, so $R_x = 40.4\,\Omega$.
**Answer:** $40\,\Omega$, two significant figures like the voltages and currents; in the calculation one more digit is kept, $40.4\,\Omega$. The ratios vary only between $24.0\,\Omega$ and $24.3\,\Omega$, so the total resistance $24.1\,\Omega$ is reliable.
**Reasonableness:** The total resistance $24.1\,\Omega$ is smaller than either branch, $60\,\Omega$ and $40.4\,\Omega$, as it should be in a parallel connection. Check: $\dfrac{60\,\Omega \cdot 40.4\,\Omega}{100.4\,\Omega} = 24.1\,\Omega$.

## fy6-4-L3-04
**Given:** $R_1 = 70\,\Omega$ in series with $R_2 = 110\,\Omega$ and $R_3 = 110\,\Omega$ in parallel; measured total resistance $180\,\Omega$; battery $U = 9.0\,\text{V}$; ammeter readings: battery current $49.8\,\text{mA}$, current of $R_2$ $49.7\,\text{mA}$ and current of $R_3$ $0.0\,\text{mA}$
**Find:** a) the total resistance of a correctly wired board, b) the wiring that explains the fault and c) the current $I_3$ of resistor $R_3$ in the repaired circuit in milliamperes
**Principle:** A correctly wired board is a mixed connection: the parallel resistors $R_2$ and $R_3$ are replaced with one resistor $R_{23}$, which is in series with resistor $R_1$. The measured $180\,\Omega$ is compared with the value for the correct wiring and with the value for a candidate fault. The current meters tell in which branch no current passes. In the repaired circuit the voltage of the parallel part is obtained from Ohm's law and divided by the resistance of resistor $R_3$.
**Reading the graph:** No graph; the values are read from the table.
**Formula:** $R_{23} = \dfrac{R_2 R_3}{R_2 + R_3}$, $R = R_1 + R_{23}$, $I = \dfrac{U}{R}$, $U_{23} = R_{23} I$ and $I_3 = \dfrac{U_{23}}{R_3}$
**Conversions:** Not needed during the calculation. At the end $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** a) $R_{23} = \dfrac{110\,\Omega \cdot 110\,\Omega}{220\,\Omega} = 55\,\Omega$ and $R = 70\,\Omega + 55\,\Omega = 125\,\Omega$. b) If one branch is off, only one $110\,\Omega$ resistor remains, and $R = 70\,\Omega + 110\,\Omega = 180\,\Omega$, which matches the measurement. The current in the wire of $R_3$ is $0.0\,\text{mA}$ and the current of $R_2$ is equal to the battery current, so $R_3$ is off. c) In the repaired circuit $I = \dfrac{9.0\,\text{V}}{125\,\Omega} = 0.072\,\text{A}$, $U_{23} = 55\,\Omega \cdot 0.072\,\text{A} = 3.96\,\text{V}$ and $I_3 = \dfrac{3.96\,\text{V}}{110\,\Omega} = 0.036\,\text{A} = 36\,\text{mA}$
**Answer:** $36\,\text{mA}$, two significant figures like the voltage $9.0\,\text{V}$. The total resistance of the board should be $125\,\Omega$, and the measurements are explained by resistor $R_3$ being off its wire.
**Reasonableness:** In the repaired circuit the current of each of the two equal branches is half of the total current, $0.072\,\text{A} : 2 = 0.036\,\text{A}$. The voltages add up: $0.072\,\text{A} \cdot 70\,\Omega + 3.96\,\text{V} = 5.04\,\text{V} + 3.96\,\text{V} = 9.0\,\text{V}$.

## fy6-4-L3-05
**Given:** target $R_\text{target} = 470\,\Omega$; resistors in stock $100\,\Omega$, $390\,\Omega$, $560\,\Omega$, $1200\,\Omega$, $1500\,\Omega$, $2700\,\Omega$ and $5600\,\Omega$, one of each
**Find:** the total resistance of the best connection of two resistors and its deviation from $470\,\Omega$ as a percentage
**Principle:** The result of a series connection is larger than either resistor and that of a parallel connection smaller than either. This narrows down the candidates before calculating. Only small resistors suit a series connection and only large ones a parallel connection. The total resistances of the candidates are calculated and the deviations $\dfrac{|R - R_\text{target}|}{R_\text{target}}$ are compared.
**Reading the graph:** No graph; the values are read from the task.
**Formula:** $R_\text{series} = R_a + R_b$, $R_\text{parallel} = \dfrac{R_a R_b}{R_a + R_b}$ and the deviation $p = \dfrac{|R - R_\text{target}|}{R_\text{target}} \cdot 100\,\%$
**Conversions:** $1.2\,\text{k}\Omega = 1200\,\Omega$, $1.5\,\text{k}\Omega = 1500\,\Omega$, $2.7\,\text{k}\Omega = 2700\,\Omega$ and $5.6\,\text{k}\Omega = 5600\,\Omega$.
**Substitution:** Series connection: the only resistors smaller than the target $470\,\Omega$ are $100\,\Omega$ and $390\,\Omega$, and their sum is $490\,\Omega$ (deviation $4.3\,\%$). Any other series connection is at least $100\,\Omega + 560\,\Omega = 660\,\Omega$ and worse. Parallel connection: the result is smaller than the smaller resistor, so the smaller resistor must be over $470\,\Omega$, which leaves the resistors $560\,\Omega$, $1200\,\Omega$, $1500\,\Omega$, $2700\,\Omega$ and $5600\,\Omega$. The pairs with $560\,\Omega$ give $382\,\Omega$, $408\,\Omega$, $\dfrac{560 \cdot 2700}{3260}\,\Omega = 463.8\,\Omega$ and $509\,\Omega$. In the other pairs the smaller resistor is at least $1200\,\Omega$, so the result is larger than $\dfrac{1200 \cdot 1500}{2700}\,\Omega = 667\,\Omega$. So the best is $560\,\Omega$ in parallel with $2700\,\Omega$: $R = 463.8\,\Omega$, and $p = \dfrac{470 - 463.8}{470} \cdot 100\,\% = 1.32\,\%$
**Answer:** $1.3\,\%$, two significant figures. The connection is $560\,\Omega$ in parallel with $2700\,\Omega$, total resistance $464\,\Omega$. The best series connection ($100\,\Omega + 390\,\Omega$) deviates by $4.3\,\%$, so the parallel connection is over three times as accurate.
**Reasonableness:** The result $463.8\,\Omega$ is smaller than $560\,\Omega$, as it should be in a parallel connection, and close to the target.
