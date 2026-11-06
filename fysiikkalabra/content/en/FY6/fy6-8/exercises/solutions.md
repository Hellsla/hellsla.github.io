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
**Given:** the points of the graph and the straight line drawn through them, extended to the axes
**Find:** the short-circuit current $I_\text{k}$ in amperes
**Principle:** In a short circuit the terminal voltage is zero. The $(I, U)$ graph of a battery is the straight line $U = E - R_\text{s} I$, so the short-circuit current is the current at which the line meets the horizontal axis. The short-circuit current was not measured but is obtained by extending the line drawn through the points.
**Reading the graph:** The line, extended with a dashed line, meets the horizontal axis $U = 0$ at the gridline $3.0\,\text{A}$. It meets the vertical axis at $4.5\,\text{V}$, which is the source voltage.
**Formula:** $U = E - R_\text{s} I_\text{k} = 0$, from which $I_\text{k} = \dfrac{E}{R_\text{s}}$; the value is read from where the line meets the horizontal axis.
**Conversions:** Not needed: the current is read in amperes.
**Substitution:** From the graph $I_\text{k} = 3.0\,\text{A}$.
**Answer:** $3.0\,\text{A}$, to two significant figures, because the value is read from a grid of $0.5\,\text{A}$.
**Reasonableness:** From the points on the line $(0.40\,\text{A};\ 3.9\,\text{V})$ and $(1.60\,\text{A};\ 2.1\,\text{V})$ we get $R_\text{s} = 1.8\,\text{V} : 1.20\,\text{A} = 1.5\,\Omega$, and $I_\text{k} = E : R_\text{s} = 4.5\,\text{V} : 1.5\,\Omega = 3.0\,\text{A}$. The result depends on the internal resistance staying the same outside the range of measurement.

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

## fy6-8-L1-06
**Find:** when the terminal voltage of a battery is equal to its source voltage.
**Principle:** The terminal voltage is $U = E - R_\text{s} I$, where $R_\text{s} I$ is the voltage drop in the internal resistance of the battery. The terminal voltage is the source voltage only when this voltage drop is zero, that is, when no current is drawn from the battery.
**Model answer:** The terminal voltage is equal to the source voltage when no current is drawn from the battery, because then no voltage drop arises in the internal resistance. If the current is large, the voltage drop is large and a voltage smaller than the source voltage is left across the terminals; the current is greatest in a short circuit, when the terminal voltage is zero. When the load resistance is equal to the internal resistance, the terminal voltage is only half of the source voltage. The claim that the voltages are always equal does not hold: the source voltage is a property of the battery, but the terminal voltage depends on the current drawn.

## fy6-8-L1-07
**Find:** what happens in a short circuit of a battery.
**Principle:** The current is $I = E : (R + R_\text{s})$. In a short circuit the resistance of the external circuit is $R \approx 0$, so only the internal resistance of the battery limits the current, and the current is the short-circuit current $I_\text{k} = E : R_\text{s}$. In batteries $R_\text{s}$ is small, so the short-circuit current is large.
**Model answer:** In a short circuit the current grows large, because only the internal resistance of the battery limits it. The whole source voltage is left across the internal resistance, so the terminal voltage is almost zero and the internal energy of the battery grows quickly. That is why a short circuit is dangerous and can damage the battery. The current does not drop to zero or stay the same, because the current is determined by the resistance of the whole circuit, and the terminal voltage cannot exceed the source voltage.

## fy6-8-L1-08
**Given:** source voltage $E = 1.50\,\text{V}$, terminal voltage $U = 1.31\,\text{V}$, current $I = 0.50\,\text{A}$
**Find:** the internal resistance $R_\text{s}$ in ohms
**Principle:** The terminal voltage is smaller than the source voltage by the voltage drop $R_\text{s} I$ in the internal resistance. When the source voltage, the terminal voltage and the current are known, $R_\text{s}$ can be solved from the equation.
**Formula:** $U = E - R_\text{s} I$, from which $R_\text{s} = \dfrac{E - U}{I}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Substitution:** $R_\text{s} = \dfrac{1.50\,\text{V} - 1.31\,\text{V}}{0.50\,\text{A}} = \dfrac{0.19\,\text{V}}{0.50\,\text{A}} = 0.38\,\Omega$
**Answer:** $0.38\,\Omega$, two significant figures like the current $0.50\,\text{A}$.
**Reasonableness:** The voltage drop is $0.38\,\Omega \cdot 0.50\,\text{A} = 0.19\,\text{V}$, and $1.50\,\text{V} - 0.19\,\text{V} = 1.31\,\text{V}$ is the given terminal voltage. The short-circuit current would be $1.50\,\text{V} : 0.38\,\Omega \approx 3.9\,\text{A}$, which is a usual size for a new battery cell.

## fy6-8-L2-05
**Given:** the measured points of the table $(I;\ U)$: $(0.20\,\text{A};\ 1.43\,\text{V})$, $(0.40\,\text{A};\ 1.31\,\text{V})$, $(0.60\,\text{A};\ 1.20\,\text{V})$, $(0.80\,\text{A};\ 1.10\,\text{V})$, $(1.00\,\text{A};\ 0.99\,\text{V})$ and $(1.20\,\text{A};\ 0.86\,\text{V})$ (example data)
**Find:** a) the source voltage $E$ read from the line, b) the internal resistance $R_\text{s}$ in ohms
**Principle:** The terminal voltage of a battery is $U = E - R_\text{s} I$, so the $(I, U)$ points lie on a descending line. The line meets the vertical axis at $U = E$, and its slope is $-R_\text{s}$. The measured points have a little scatter, so the line is drawn through the middle of the set of points and not tied to individual points.
**Reading the graph:** The fitted line meets the vertical axis at $1.54\,\text{V}$ and passes approximately through the point $(1.20\,\text{A};\ 0.87\,\text{V})$. The points lie on both sides of the line; if the line is turned differently within the limits of the points, the slope changes by about $\pm 0.03\,\Omega$. The two points read from the line are far apart: $(0\,\text{A};\ 1.54\,\text{V})$ and $(1.20\,\text{A};\ 0.87\,\text{V})$.
**Formula:** $R_\text{s} = -\dfrac{\Delta U}{\Delta I} = \dfrac{U_1 - U_2}{I_2 - I_1}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Substitution:** $R_\text{s} = \dfrac{1.54\,\text{V} - 0.87\,\text{V}}{1.20\,\text{A} - 0\,\text{A}} = \dfrac{0.67\,\text{V}}{1.20\,\text{A}} = 0.558\,\Omega$
**Answer:** a) $E \approx 1.54\,\text{V}$; b) $R_\text{s} \approx 0.56\,\Omega$, two significant figures, because the line is fitted by eye. A fit by eye varies: the slope can change by about $\pm 0.03\,\Omega$, so a value between $0.53\text{–}0.59\,\Omega$ is a good answer.
**Reasonableness:** According to the model, at the current $0.60\,\text{A}$ the terminal voltage is $1.54\,\text{V} - 0.56\,\Omega \cdot 0.60\,\text{A} = 1.20\,\text{V}$, and that is the third value of the table. The source voltage is greater than any measured terminal voltage, as it should be. The short-circuit current would be $1.54\,\text{V} : 0.56\,\Omega \approx 2.8\,\text{A}$, but that is an extension of the line outside the range of measurement and it is not measured.

## fy6-8-L2-06
**Given:** the measured points of the table $(I;\ U_\text{A};\ U_\text{B})$ at currents $0.10\,\text{A}$ … $1.00\,\text{A}$: the terminal voltage of battery A decreases from $1.55\,\text{V}$ to $1.10\,\text{V}$ and that of battery B from $1.47\,\text{V}$ to $1.27\,\text{V}$ (example data)
**Find:** a) the current $I$ at which the terminal voltages are equal; b) which battery is better at a large current and why
**Principle:** Both batteries follow the model $U = E - R_\text{s} I$, so the points of each fit its own descending line. At the intersection of the lines the terminal voltages are equal. The slope of a line is $-R_\text{s}$, so a gentler line means a smaller internal resistance.
**Reading the graph:** The line of battery A passes through the points $(0\,\text{A};\ 1.60\,\text{V})$ and $(1.00\,\text{A};\ 1.10\,\text{V})$, so $E_\text{A} = 1.60\,\text{V}$ and $R_\text{A} = 0.50\,\Omega$. The line of battery B passes through the points $(0\,\text{A};\ 1.49\,\text{V})$ and $(1.00\,\text{A};\ 1.27\,\text{V})$, so $E_\text{B} = 1.49\,\text{V}$ and $R_\text{B} = 0.22\,\Omega$. The lines intersect in the graph at about the current $0.4\,\text{A}$, between the table rows $0.30\,\text{A}$ and $0.50\,\text{A}$: first the terminal voltage of A is greater ($1.45\,\text{V}$ and $1.42\,\text{V}$), then that of B ($1.35\,\text{V}$ and $1.38\,\text{V}$).
**Formula:** $E_\text{A} - R_\text{A} I = E_\text{B} - R_\text{B} I$, from which $I = \dfrac{E_\text{A} - E_\text{B}}{R_\text{A} - R_\text{B}}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{1.60\,\text{V} - 1.49\,\text{V}}{0.50\,\Omega - 0.22\,\Omega} = \dfrac{0.11\,\text{V}}{0.28\,\Omega} = 0.39\,\text{A}$
**Answer:** a) about $0.40\,\text{A}$; the graphical reading and the calculation give a value between $0.35\text{–}0.45\,\text{A}$, because the fit of the lines varies. b) At a large current battery B is better, because its internal resistance $0.22\,\Omega$ is smaller than that of battery A, $0.50\,\Omega$, so its terminal voltage decreases more gently as the current grows. The source voltage of battery A is greater, so at a small current, below $0.4\,\text{A}$, battery A gives the higher terminal voltage. At the current $1.00\,\text{A}$ the terminal voltage is $1.10\,\text{V}$ for battery A and $1.27\,\text{V}$ for battery B.
**Reasonableness:** At the current $0.40\,\text{A}$ the terminal voltage of battery A is $1.60\,\text{V} - 0.50\,\Omega \cdot 0.40\,\text{A} = 1.40\,\text{V}$ and that of battery B is $1.49\,\text{V} - 0.22\,\Omega \cdot 0.40\,\text{A} = 1.40\,\text{V}$, and this is between the table rows $0.30\,\text{A}$ and $0.50\,\text{A}$, as it should be. The short-circuit current is $1.49\,\text{V} : 0.22\,\Omega \approx 6.8\,\text{A}$ for battery B and $1.60\,\text{V} : 0.50\,\Omega = 3.2\,\text{A}$ for battery A, so B can deliver a larger current.

## fy6-8-L2-07
**Find:** which statement about the student's conclusion that the internal resistance is zero is correct.
**Principle:** The terminal voltage is $U = E - R_\text{s} I$. When a voltmeter is connected without a load, a vanishingly small current passes through it, so $I \approx 0$ and the voltage drop in the internal resistance is zero. Then $U = E$ regardless of how large the internal resistance is.
**Model answer:** The student's conclusion is wrong. The voltage $1.58\,\text{V}$ measured without a load is the source voltage of the battery, because the current is zero and no voltage drop arises in the internal resistance. The same voltage would be seen even if the internal resistance were large, so a single measurement without a current tells nothing about it. The current of the voltmeter is very small, so the meter itself does not reduce the voltage. Nor is the internal resistance infinite even though the current is zero, because it is a constant property of the battery. The internal resistance is obtained by measuring the terminal voltage and the current under load, preferably at several loads, and calculating $R_\text{s} = (E - U) : I$ or from the slope of the graph.

## fy6-8-L3-04
**Given:** the measured points of the table at currents $0.10\,\text{A}$ … $0.50\,\text{A}$: the terminal voltage of the new battery decreases from $1.56\,\text{V}$ to $1.46\,\text{V}$ and that of the aged battery from $1.41\,\text{V}$ to $0.97\,\text{V}$ (example data); load resistance $R = 2.0\,\Omega$
**Find:** a) $E$ and $R_\text{s}$ of each battery; b) the share of the electric power produced by the aged battery that is converted into the internal energy of the battery, as a percentage; c) the power delivered to the resistor at the resistances $0.55\,\Omega$, $1.1\,\Omega$, $2.2\,\Omega$ and $4.4\,\Omega$, and the load with the greatest power
**Principle:** The terminal voltage of both batteries follows the model $U = E - R_\text{s} I$, so the intercept of the fitted line on the vertical axis is $E$ and the slope is $-R_\text{s}$. Under load the current is $I = E : (R + R_\text{s})$. The power produced by the battery is $P = EI$, the power converted in the internal resistance is $R_\text{s} I^2$ and the power in the load is $RI^2$. The expression for power comes from the formula for electric power (chapter *Electric power and heating of a resistor*).
**Reading the graph:** The line of the new battery passes through the points $(0.10\,\text{A};\ 1.56\,\text{V})$ and $(0.50\,\text{A};\ 1.46\,\text{V})$ and that of the aged battery through the points $(0.10\,\text{A};\ 1.41\,\text{V})$ and $(0.50\,\text{A};\ 0.97\,\text{V})$. The points of both lie on both sides of the line.
**Formula:** $R_\text{s} = \dfrac{U_1 - U_2}{I_2 - I_1}$ and $E = U_1 + R_\text{s} I_1$

$I = \dfrac{E}{R + R_\text{s}}$

$\text{share} = \dfrac{R_\text{s} I^2}{EI} = \dfrac{R_\text{s}}{R + R_\text{s}}$

$P = RI^2 = \dfrac{E^2 R}{(R + R_\text{s})^2}$
**Conversions:** Not needed: all quantities are in base units.
**Substitution:** a) New: $R_\text{s} = \dfrac{0.10\,\text{V}}{0.40\,\text{A}} = 0.25\,\Omega$ and $E = 1.56\,\text{V} + 0.25\,\Omega \cdot 0.10\,\text{A} = 1.58\,\text{V}$. Aged: $R_\text{s} = \dfrac{1.41\,\text{V} - 0.97\,\text{V}}{0.40\,\text{A}} = 1.10\,\Omega$ and $E = 1.41\,\text{V} + 1.10\,\Omega \cdot 0.10\,\text{A} = 1.52\,\text{V}$.
b) Aged: $I = \dfrac{1.52\,\text{V}}{2.0\,\Omega + 1.10\,\Omega} = 0.490\,\text{A}$, the power produced is $EI = 1.52\,\text{V} \cdot 0.490\,\text{A} = 0.745\,\text{W}$ and the power remaining in the battery is $R_\text{s} I^2 = 1.10\,\Omega \cdot (0.490\,\text{A})^2 = 0.264\,\text{W}$. The share is $\dfrac{0.264\,\text{W}}{0.745\,\text{W}} = \dfrac{1.10\,\Omega}{3.10\,\Omega} = 0.355$. New battery: $\dfrac{0.25\,\Omega}{2.0\,\Omega + 0.25\,\Omega} = 0.11$.
c) For the aged battery ($E = 1.52\,\text{V}$, $R_\text{s} = 1.10\,\Omega$): $R = 0.55\,\Omega$: $P = \dfrac{(1.52\,\text{V})^2 \cdot 0.55\,\Omega}{(1.65\,\Omega)^2} = 0.47\,\text{W}$; $R = 1.1\,\Omega$: $P = \dfrac{(1.52\,\text{V})^2 \cdot 1.1\,\Omega}{(2.2\,\Omega)^2} = 0.53\,\text{W}$; $R = 2.2\,\Omega$: $P = 0.47\,\text{W}$; $R = 4.4\,\Omega$: $P = 0.34\,\text{W}$. The share converted into the internal energy of the battery: $R = 1.1\,\Omega$: $\dfrac{1.10\,\Omega}{2.2\,\Omega} = 0.50$.
**Answer:** In the answer box: $35\,\%$. a) New battery: $E = 1.58\,\text{V}$, $R_\text{s} = 0.25\,\Omega$; aged battery: $E = 1.52\,\text{V}$, $R_\text{s} = 1.1\,\Omega$.
b) For the answer box: about $35\,\%$ of the power produced by the aged battery is converted into the internal energy of the battery, two significant figures like the precision of the load $2.0\,\Omega$. For the new battery the share is only about $11\,\%$, because its internal resistance $0.25\,\Omega$ is much smaller.
c) The power is greatest, about $0.53\,\text{W}$, with the load $1.1\,\Omega$, which is equal to the internal resistance. Then half of the power produced is converted into the internal energy of the battery.
**Reasonableness:** The powers match: $0.264\,\text{W} + 2.0\,\Omega \cdot (0.490\,\text{A})^2 = 0.264\,\text{W} + 0.481\,\text{W} = 0.745\,\text{W}$, as the power produced. The source voltage of the aged battery is only slightly smaller than that of the new one, but the internal resistance is more than four times as large, and so it heats up much more and gives less power to the load. The maximum of the power is gentle, as the values $0.47\,\text{W}$, $0.53\,\text{W}$ and $0.47\,\text{W}$ show, but even at the greatest power half of the energy is wasted, so in devices the load is usually chosen larger than $R_\text{s}$.

## fy6-8-L3-05
**Given:** the measured points of the table $(I;\ U)$ at currents $0.50\,\text{A}$ … $3.00\,\text{A}$: the voltage decreases from $5.56\,\text{V}$ to $2.79\,\text{V}$ (example data); total resistance of the wires $R_\text{j} = 0.30\,\Omega$; the student's slope $1.1\,\Omega$ and short-circuit current $5.6\,\text{A}$
**Find:** a) the source voltage $E$; b) the student's error and the correct internal resistance of the group of batteries; c) the correct short-circuit current $I_\text{k}$ of the group of batteries in amperes
**Principle:** The voltmeter is across the terminals of the load resistor, so it shows a voltage that is smaller than the terminal voltage of the group of batteries by the voltage drop $R_\text{j} I$ in the wires: $U = E - R_\text{s} I - R_\text{j} I = E - (R_\text{s} + R_\text{j}) I$. So the slope of the graph is $-(R_\text{s} + R_\text{j})$, and the student's value includes the resistance of the wires. The internal resistance of the group of batteries itself is obtained by subtracting $R_\text{j}$, and the short-circuit current is calculated from it.
**Reading the graph:** The fitted line passes through the points $(0.50\,\text{A};\ 5.56\,\text{V})$ and $(3.00\,\text{A};\ 2.80\,\text{V})$. The points lie on both sides of the line. The line meets the vertical axis at $6.11\,\text{V}$, which is the source voltage, because when the current is zero there is no voltage drop in the wires.
**Formula:** $E = U_1 + (R_\text{s} + R_\text{j}) I_1$; $R_\text{s} + R_\text{j} = \dfrac{U_1 - U_2}{I_2 - I_1}$; $R_\text{s} = (R_\text{s} + R_\text{j}) - R_\text{j}$; $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Substitution:** a) $R_\text{s} + R_\text{j} = \dfrac{5.56\,\text{V} - 2.80\,\text{V}}{3.00\,\text{A} - 0.50\,\text{A}} = \dfrac{2.76\,\text{V}}{2.50\,\text{A}} = 1.10\,\Omega$

$E = 5.56\,\text{V} + 1.10\,\Omega \cdot 0.50\,\text{A} = 6.11\,\text{V}$
b) $R_\text{s} = 1.10\,\Omega - 0.30\,\Omega = 0.80\,\Omega$.
c) $I_\text{k} = \dfrac{6.11\,\text{V}}{0.80\,\Omega} = 7.64\,\text{A}$
**Answer:** For the answer box: c) $7.6\,\text{A}$, two significant figures like the resistance of the wires $0.30\,\Omega$. The measurement should have been made by connecting the voltmeter directly across the terminals of the group of batteries, so that the voltage drop in the wires is not included in the measured voltage.
**Other parts:** a) the source voltage of the group of batteries is $E \approx 6.11\,\text{V}$. b) The student's internal resistance is too large, because the slope includes the resistance of the wires; the internal resistance of the group of batteries is $0.80\,\Omega$. The student's short-circuit current $5.6\,\text{A}$ is too small, because the student divided the source voltage by too large a resistance.
**Reasonableness:** According to the model, at the current $2.00\,\text{A}$ the terminal voltage of the group of batteries is $6.11\,\text{V} - 0.80\,\Omega \cdot 2.00\,\text{A} = 4.51\,\text{V}$ and after the wires $4.51\,\text{V} - 0.30\,\Omega \cdot 2.00\,\text{A} = 3.91\,\text{V}$, which is the fourth value of the table. The correct short-circuit current is greater than the student's, because the internal resistance of the group of batteries is smaller than the $1.1\,\Omega$ the student obtained. If the terminals were connected with wires, the current would be smaller, $6.11\,\text{V} : 1.10\,\Omega \approx 5.6\,\text{A}$, which is the student's figure, but it is the current with the wires, not the short-circuit current of the group of batteries.

## fy6-8-L2-08
**Find:** which conclusion about the source voltage $E$ and the internal resistance $R_\text{s}$ of the battery is justified on the basis of the measurements of the table.
**Principle:** The terminal voltage is $U = E - R_\text{s} I$, so the measured points $(I, U)$ should lie on a descending line. The line meets the vertical axis at $U = E$, and its slope is $-R_\text{s}$. The slope is read from the line at two points far apart; here the extreme points are on the line. The deviations of the points from the line are compared with the measurement uncertainty $\pm 0.01\,\text{V}$.
**Model answer:** The drops of the terminal voltage between successive measurements, when the current increases by $0.20\,\text{A}$, are $0.08\,\text{V}$, $0.07\,\text{V}$, $0.09\,\text{V}$ and $0.08\,\text{V}$. They differ from each other by at most $0.02\,\text{V}$. The difference of two drops depends on three or four readings, so its uncertainty is up to $4 \cdot 0.01\,\text{V} = 0.04\,\text{V}$, and the difference fits within it. The points thus fit one line, and the measurements do not show that the internal resistance changes.

The slope from the extreme points:

$$\begin{aligned}
&R_\text{s} = -\frac{\Delta U}{\Delta I} \\
&\phantom{R_\text{s}} = -\frac{1.19\,\text{V} - 1.51\,\text{V}}{0.90\,\text{A} - 0.10\,\text{A}} \\
&\phantom{R_\text{s}} = \frac{0.32\,\text{V}}{0.80\,\text{A}} = 0.40\,\Omega
\end{aligned}$$

The source voltage is obtained by extending the line from the point $(0.10\,\text{A};\ 1.51\,\text{V})$ to $I = 0$:

$$\begin{aligned}
&E = U + R_\text{s} I \\
&\phantom{E} = 1.51\,\text{V} + 0.40\,\Omega \cdot 0.10\,\text{A} \\
&\phantom{E} = 1.55\,\text{V}
\end{aligned}$$

Conclusion: the source voltage is about $1.55\,\text{V}$ and the internal resistance about $0.40\,\Omega$. The reading $1.51\,\text{V}$ at the smallest current is a terminal voltage, not the source voltage. The quotient of one measurement, for example $1.19\,\text{V} : 0.90\,\text{A} \approx 1.3\,\Omega$, is the resistance of the load and not the internal resistance. If both errors are made, the result is $1.51\,\text{V}$ and $1.3\,\Omega$.

The uncertainty affects the result too: if the readings of the extreme points are $0.01\,\text{V}$ off in opposite directions, the slope becomes $0.30\,\text{V} : 0.80\,\text{A} \approx 0.38\,\Omega$ or $0.34\,\text{V} : 0.80\,\text{A} \approx 0.43\,\Omega$, so the internal resistance is about $0.4\,\Omega$.
