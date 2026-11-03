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
**Principle:** In a series connection the battery voltage is shared between the components: each charge passes through both lamps, and its energy is transformed into heat and light in the lamps. The sum of the voltages of the lamps is the battery voltage.
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
