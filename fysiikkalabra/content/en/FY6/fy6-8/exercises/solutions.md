## fy6-8-L1-01
**Given:** source voltage $E = 1.58\,\text{V}$, internal resistance $R_\text{s} = 0.25\,\Omega$, current $I = 0.80\,\text{A}$
**Find:** the terminal voltage $U$ in volts
**Principle:** A battery is an ideal source with an internal resistance in series. When a current is drawn from the battery, the potential drops in the internal resistance by the voltage $R_\text{s} I$, so a voltage smaller than the source voltage is left between the terminals.
**Formula:** $U = E - R_\text{s} I$
**Conversions:** Not needed: $1\,\Omega \cdot 1\,\text{A} = 1\,\text{V}$.
**Substitution:** $U = 1.58\,\text{V} - 0.25\,\Omega \cdot 0.80\,\text{A} = 1.58\,\text{V} - 0.20\,\text{V} = 1.38\,\text{V}$
**Answer:** $1.38\,\text{V}$, to a hundredth of a volt like the source voltage $1.58\,\text{V}$.
**Reasonableness:** The terminal voltage is smaller than the source voltage, as it should be for a battery that is giving a current. The voltage across the internal resistance, $0.20\,\text{V}$, is about an eighth of the source voltage, which fits the fairly large current $0.80\,\text{A}$.

## fy6-8-L1-02
**Given:** source voltage $E = 1.30\,\text{V}$, internal resistance $R_\text{s} = 0.040\,\Omega$; the resistance of the short-circuit conductor is neglected
**Find:** the short-circuit current $I_\text{k}$ in amperes
**Principle:** In a short circuit the resistance of the external circuit is zero, so by Kirchhoff's voltage law the whole source voltage is left across the internal resistance of the cell. Only the internal resistance limits the current.
**Formula:** $E - R_\text{s} I_\text{k} = 0$, from which $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I_\text{k} = \dfrac{1.30\,\text{V}}{0.040\,\Omega} = 32.5\,\text{A}$
**Answer:** $33\,\text{A}$, two significant figures like the internal resistance $0.040\,\Omega$.
**Reasonableness:** Estimate $1.3\,\text{V} : 0.04\,\Omega \approx 30\,\text{A}$. The internal resistance of a rechargeable cell is small, so the short-circuit current is tens of amperes: such a large current heats the conductor and the cell quickly, which is why a short circuit is dangerous.

## fy6-8-L1-03
**Given:** four batteries in series, the source voltage of each $E_1 = 1.55\,\text{V}$
**Find:** the source voltage $E$ of the group of batteries in volts
**Principle:** In a series connection the charge passes through each battery one after the other, and in each the potential rises by the source voltage. The batteries are the right way round, so the rises are added.
**Formula:** $E = E_1 + E_2 + E_3 + E_4$, and for identical batteries $E = 4E_1$
**Conversions:** Not needed: the voltages are in volts.
**Substitution:** $E = 4 \cdot 1.55\,\text{V} = 6.20\,\text{V}$
**Answer:** $6.20\,\text{V}$, three significant figures like the source voltage of a battery, $1.55\,\text{V}$.
**Reasonableness:** From a group of four $1.5\,\text{V}$ batteries one expects about $6\,\text{V}$, and the result is slightly larger, because the source voltage of a new battery is a little over the marking $1.5\,\text{V}$.

## fy6-8-L1-04
**Given:** three identical batteries in parallel, the internal resistance of each $R_{\text{s}1} = 0.45\,\Omega$
**Find:** the internal resistance $R_\text{s}$ of the group of batteries in ohms
**Principle:** The internal resistances of batteries in parallel are parallel branches between the same two points. The batteries are identical, so the current is shared equally among them, and the internal resistance of the group is the internal resistance of one battery divided by the number of batteries.
**Formula:** $R_\text{s} = \dfrac{R_{\text{s}1}}{n}$
**Conversions:** Not needed: the resistance is in ohms.
**Substitution:** $R_\text{s} = \dfrac{0.45\,\Omega}{3} = 0.15\,\Omega$
**Answer:** $0.15\,\Omega$, two significant figures like the internal resistance $0.45\,\Omega$; the number of batteries, $3$, is an exact number.
**Reasonableness:** The resistance of a parallel connection is smaller than the resistance of any single branch, and $0.15\,\Omega < 0.45\,\Omega$. Check with the equation for resistors in parallel: $\tfrac{1}{R_\text{s}} = \tfrac{3}{0.45\,\Omega}$, so $R_\text{s} = 0.15\,\Omega$.

## fy6-8-L1-05
**Given:** the measured points of the graph and the straight line drawn through them, extended to the axes
**Find:** the short-circuit current $I_\text{k}$ in amperes
**Principle:** In a short circuit the terminal voltage is zero. The $(I, U)$ graph of a battery is the straight line $U = E - R_\text{s} I$, so the short-circuit current is the current at which the line meets the horizontal axis. The short-circuit current was not measured but is obtained by extending the line through the measured points.
**Reading the graph:** The line, extended with a dashed line, meets the horizontal axis $U = 0$ at the gridline $3.0\,\text{A}$. It meets the vertical axis at $4.5\,\text{V}$, which is the source voltage.
**Formula:** $U = E - R_\text{s} I_\text{k} = 0$, from which $I_\text{k} = \dfrac{E}{R_\text{s}}$; the value is read from where the line meets the horizontal axis.
**Conversions:** Not needed: the current is read in amperes.
**Substitution:** From the graph $I_\text{k} = 3.0\,\text{A}$.
**Answer:** $3.0\,\text{A}$, to two significant figures, because the value is read from a grid of $0.5\,\text{A}$.
**Reasonableness:** From the measured points $(0.40\,\text{A};\ 3.9\,\text{V})$ and $(1.60\,\text{A};\ 2.1\,\text{V})$ we get $R_\text{s} = 1.8\,\text{V} : 1.20\,\text{A} = 1.5\,\Omega$, and $I_\text{k} = E : R_\text{s} = 4.5\,\text{V} : 1.5\,\Omega = 3.0\,\text{A}$. The result depends on the internal resistance staying the same outside the range of measurement.

## fy6-8-L2-01
**Given:** first load: $I_1 = 0.20\,\text{A}$, $U_1 = 4.30\,\text{V}$; second load: $I_2 = 0.80\,\text{A}$, $U_2 = 3.70\,\text{V}$
**Find:** the internal resistance $R_\text{s}$ in ohms
**Principle:** The same battery is in both measurements, so its source voltage and internal resistance are the same. The terminal voltage $U = E - R_\text{s} I$ decreases by $R_\text{s}$ for every ampere the current grows, so the source voltage cancels in the difference of the two measurements.
**Formula:** $U_1 = E - R_\text{s} I_1$ and $U_2 = E - R_\text{s} I_2$; by subtracting $U_1 - U_2 = R_\text{s}(I_2 - I_1)$, from which $R_\text{s} = \dfrac{U_1 - U_2}{I_2 - I_1}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Substitution:** $R_\text{s} = \dfrac{4.30\,\text{V} - 3.70\,\text{V}}{0.80\,\text{A} - 0.20\,\text{A}} = \dfrac{0.60\,\text{V}}{0.60\,\text{A}} = 1.0\,\Omega$
**Answer:** $1.0\,\Omega$, two significant figures like the differences $0.60\,\text{V}$ and $0.60\,\text{A}$.
**Reasonableness:** The source voltage is $E = 4.30\,\text{V} + 1.0\,\Omega \cdot 0.20\,\text{A} = 4.50\,\text{V}$, and the second measurement gives the same: $3.70\,\text{V} + 1.0\,\Omega \cdot 0.80\,\text{A} = 4.50\,\text{V}$. It may be a flat $4.5\,\text{V}$ battery, whose internal resistance is of the order of an ohm.

## fy6-8-L2-02
**Given:** source voltage $E = 6.0\,\text{V}$, internal resistance $R_\text{s} = 0.50\,\Omega$, load resistance $R = 5.5\,\Omega$
**Find:** the terminal voltage $U$ in volts
**Principle:** The internal resistance and the load resistor are in series in the same loop, so Kirchhoff's voltage law $E - R_\text{s} I - RI = 0$ gives the current. The terminal voltage is the voltage of the load resistor, because the resistor is connected directly to the terminals of the source.
**Formula:** $I = \dfrac{E}{R + R_\text{s}}$ and $U = RI$, so $U = \dfrac{R E}{R + R_\text{s}}$
**Conversions:** Not needed: all the quantities are in base units.
**Substitution:** $I = \dfrac{6.0\,\text{V}}{5.5\,\Omega + 0.50\,\Omega} = 1.0\,\text{A}$ and $U = 5.5\,\Omega \cdot 1.0\,\text{A} = 5.5\,\text{V}$
**Answer:** $5.5\,\text{V}$, two significant figures like the given data.
**Reasonableness:** The equation of the terminal voltage gives the same: $U = 6.0\,\text{V} - 0.50\,\Omega \cdot 1.0\,\text{A} = 5.5\,\text{V}$. The internal resistance is only about a tenth of the load, so the terminal voltage is only a little smaller than the source voltage.

## fy6-8-L2-03
**Given:** resistance of the lamp $R = 3.0\,\Omega$, source voltage $E = 4.5\,\text{V}$, internal resistance $R_\text{s} = 1.5\,\Omega$
**Find:** the power $P$ of the lamp in watts
**Principle:** The lamp and the internal resistance of the battery are in series in the same loop, so the voltage law gives the current. The voltage of the lamp is the terminal voltage of the battery, and electric power is the product of voltage and current (chapter *Electric power and the heating of a resistor*).
**Formula:** $I = \dfrac{E}{R + R_\text{s}}$, $U = E - R_\text{s} I$ and $P = UI$
**Conversions:** Not needed: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Substitution:** $I = \dfrac{4.5\,\text{V}}{3.0\,\Omega + 1.5\,\Omega} = 1.0\,\text{A}$, $U = 4.5\,\text{V} - 1.5\,\Omega \cdot 1.0\,\text{A} = 3.0\,\text{V}$ and $P = 3.0\,\text{V} \cdot 1.0\,\text{A} = 3.0\,\text{W}$
**Answer:** $3.0\,\text{W}$, two significant figures like the resistances.
**Reasonableness:** The source gives a power $4.5\,\text{V} \cdot 1.0\,\text{A} = 4.5\,\text{W}$, of which $1.5\,\Omega \cdot (1.0\,\text{A})^2 = 1.5\,\text{W}$ is changed into internal energy of the battery and $3.0\,\text{W}$ goes to the lamp: $1.5\,\text{W} + 3.0\,\text{W} = 4.5\,\text{W}$. Without the internal resistance the power of the lamp would be greater.

## fy6-8-L2-04
**Given:** two batteries in series, each with $E_1 = 1.5\,\text{V}$ and $R_{\text{s}1} = 0.30\,\Omega$; load resistance $R = 2.4\,\Omega$
**Find:** the current $I$ in amperes
**Principle:** The source voltages of batteries in series are added, and their internal resistances are in the same loop as the load, one after the other. Kirchhoff's voltage law gives the current of the loop.
**Formula:** $E = 2E_1$ and $R_\text{s} = 2R_{\text{s}1}$, so $I = \dfrac{E}{R + R_\text{s}} = \dfrac{2E_1}{R + 2R_{\text{s}1}}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{2 \cdot 1.5\,\text{V}}{2.4\,\Omega + 2 \cdot 0.30\,\Omega} = \dfrac{3.0\,\text{V}}{3.0\,\Omega} = 1.0\,\text{A}$
**Answer:** $1.0\,\text{A}$, two significant figures like the given data.
**Reasonableness:** Without the internal resistances the current would be $3.0\,\text{V} : 2.4\,\Omega = 1.25\,\text{A}$, so the internal resistances reduce it, as they should. The terminal voltage is $2.4\,\Omega \cdot 1.0\,\text{A} = 2.4\,\text{V}$, which is less than the source voltage $3.0\,\text{V}$.

## fy6-8-L3-01
**Given:** two identical batteries in parallel, each with $E_1 = 1.5\,\text{V}$ and $R_{\text{s}1} = 0.40\,\Omega$; resistance of the lamp $R = 0.80\,\Omega$
**Find:** the current $I_1$ through each battery in amperes
**Principle:** The source voltage of identical batteries in parallel is the same as for one, and the internal resistances are parallel branches, so the internal resistance of the group is half the internal resistance of one battery. The group and the lamp form a loop whose current comes from the voltage law. The batteries are identical, so by the current law the total current is shared equally between them.
**Formula:** $R_\text{s} = \dfrac{R_{\text{s}1}}{2}$, $I = \dfrac{E_1}{R + R_\text{s}}$ and $I_1 = \dfrac{I}{2}$
**Conversions:** Not needed: all the quantities are in base units.
**Substitution:** $R_\text{s} = \dfrac{0.40\,\Omega}{2} = 0.20\,\Omega$, $I = \dfrac{1.5\,\text{V}}{0.80\,\Omega + 0.20\,\Omega} = 1.5\,\text{A}$ and $I_1 = \dfrac{1.5\,\text{A}}{2} = 0.75\,\text{A}$
**Answer:** $0.75\,\text{A}$, two significant figures like the given data.
**Reasonableness:** The terminal voltage is $0.80\,\Omega \cdot 1.5\,\text{A} = 1.2\,\text{V}$. Across each battery it is $1.5\,\text{V} - 0.40\,\Omega \cdot 0.75\,\text{A} = 1.2\,\text{V}$, so both branches give the same voltage. One battery alone would give only $1.5\,\text{V} : 1.20\,\Omega = 1.25\,\text{A}$ and would have to give all of it itself.

## fy6-8-L3-02
**Given:** three batteries in series, one the wrong way round; each with $E_1 = 1.5\,\text{V}$ and $R_{\text{s}1} = 0.25\,\Omega$; resistance of the lamp $R = 4.0\,\Omega$
**Find:** the current $I$ through the lamp in amperes
**Principle:** In a series connection the changes of potential are added. In the batteries that are the right way round the potential rises by $E_1$, but in the one the wrong way round it drops by the same amount, so the source voltage of the group is $E_1 + E_1 - E_1$. The internal resistance of all three is still in the same loop one after the other.
**Formula:** $E = E_1 + E_1 - E_1 = E_1$, $R_\text{s} = 3R_{\text{s}1}$ and $I = \dfrac{E}{R + R_\text{s}} = \dfrac{E_1}{R + 3R_{\text{s}1}}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{1.5\,\text{V}}{4.0\,\Omega + 3 \cdot 0.25\,\Omega} = \dfrac{1.5\,\text{V}}{4.75\,\Omega} = 0.3158\,\text{A}$
**Answer:** $0.32\,\text{A}$, two significant figures like the given data.
**Reasonableness:** With the batteries the right way round the source voltage of the group would be $4.5\,\text{V}$ and the current $4.5\,\text{V} : 4.75\,\Omega = 0.95\,\text{A}$, three times as large. The lamp therefore glows clearly more dimly, which is a common sign of a battery put in the wrong way round.

## fy6-8-L3-03
**Given:** load $R_1 = 2.0\,\Omega$, terminal voltage $U_1 = 1.20\,\text{V}$; load $R_2 = 6.0\,\Omega$, terminal voltage $U_2 = 1.44\,\text{V}$
**Find:** the source voltage $E$ in volts
**Principle:** The terminal voltage is the voltage of the load resistor, so Ohm's law gives the current of each measurement. The same battery is in both measurements, so $U = E - R_\text{s} I$ holds with the same $E$ and $R_\text{s}$. From the two equations the internal resistance is solved first and then the source voltage.
**Formula:** $I_1 = \dfrac{U_1}{R_1}$ and $I_2 = \dfrac{U_2}{R_2}$; $U_1 = E - R_\text{s} I_1$ and $U_2 = E - R_\text{s} I_2$, so $R_\text{s} = \dfrac{U_2 - U_1}{I_1 - I_2}$ and $E = U_1 + R_\text{s} I_1$
**Conversions:** Not needed: all the quantities are in base units.
**Substitution:** $I_1 = \dfrac{1.20\,\text{V}}{2.0\,\Omega} = 0.60\,\text{A}$, $I_2 = \dfrac{1.44\,\text{V}}{6.0\,\Omega} = 0.24\,\text{A}$, $R_\text{s} = \dfrac{1.44\,\text{V} - 1.20\,\text{V}}{0.60\,\text{A} - 0.24\,\text{A}} = 0.667\,\Omega$ and $E = 1.20\,\text{V} + 0.667\,\Omega \cdot 0.60\,\text{A} = 1.60\,\text{V}$
**Answer:** $1.60\,\text{V}$, to a hundredth of a volt like the measured terminal voltages.
**Reasonableness:** The second measurement gives the same: $1.44\,\text{V} + 0.667\,\Omega \cdot 0.24\,\text{A} = 1.60\,\text{V}$. The source voltage is greater than either terminal voltage, as it should be, and $1.60\,\text{V}$ is a typical source voltage for a new AA battery.
