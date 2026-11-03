## fy6-5-L1-01
**Given:** arriving currents $2.4\,\text{A}$ and $0.6\,\text{A}$, leaving current $1.8\,\text{A}$
**Find:** the current $I$ of the other leaving wire in amperes
**Principle:** Kirchhoff's current law: charge neither disappears nor collects at the junction, so the sum of the arriving currents is equal to the sum of the leaving currents.
**Formula:** $I_\text{in1} + I_\text{in2} = I_\text{out1} + I$, from which $I = I_\text{in1} + I_\text{in2} - I_\text{out1}$
**Conversions:** Not needed: all the currents are in amperes.
**Substitution:** $I = 2.4\,\text{A} + 0.6\,\text{A} - 1.8\,\text{A} = 1.2\,\text{A}$
**Answer:** $1.2\,\text{A}$, to one decimal place like the given currents.
**Reasonableness:** A total of $3.0\,\text{A}$ arrives at the point, and the leaving currents $1.8\,\text{A}$ and $1.2\,\text{A}$ are together the same $3.0\,\text{A}$. The current is positive, so it really does leave the point.

## fy6-5-L1-02
**Given:** voltage of the source $U = 12.0\,\text{V}$, voltage of the first resistor $U_1 = 4.5\,\text{V}$
**Find:** the voltage $U_2$ of the second resistor in volts
**Principle:** Kirchhoff's voltage law: when a loop is traversed, the sum of the changes of potential is zero. The rise in the source is equal to the total of the drops in the resistors.
**Formula:** $U - U_1 - U_2 = 0$, from which $U_2 = U - U_1$
**Conversions:** Not needed: the voltages are in volts.
**Substitution:** $U_2 = 12.0\,\text{V} - 4.5\,\text{V} = 7.5\,\text{V}$
**Answer:** $7.5\,\text{V}$, to one decimal place like the given voltages.
**Reasonableness:** $4.5\,\text{V} + 7.5\,\text{V} = 12.0\,\text{V}$, the whole voltage of the source. The voltage of the second resistor is greater, so its resistance is greater, because the current of resistors in series is the same.

## fy6-5-L1-03
**Given:** $V_A = 5.0\,\text{V}$, $V_B = -3.0\,\text{V}$ relative to the same zero point
**Find:** the voltage $U_{AB}$ in volts
**Principle:** Voltage is the difference of the potentials of two points. When both potentials are given relative to the same zero point, the difference does not depend on the zero point.
**Formula:** $U_{AB} = V_A - V_B$
**Conversions:** Not needed: the potentials are in volts.
**Substitution:** $U_{AB} = 5.0\,\text{V} - (-3.0\,\text{V}) = 8.0\,\text{V}$
**Answer:** $8.0\,\text{V}$, to one decimal place like the potentials.
**Reasonableness:** The point $A$ is $5.0\,\text{V}$ above the zero point and the point $B$ is $3.0\,\text{V}$ below it, so their difference is $5.0\,\text{V} + 3.0\,\text{V}$. The voltage is positive because $A$ is at the higher potential.

## fy6-5-L1-04
**Given:** $R = 40\,\Omega$, $I = 0.15\,\text{A}$
**Find:** the drop of potential in the resistor, that is, the voltage $U$ of the resistor in volts
**Principle:** In a resistor the potential drops in the direction of the current by the voltage of the resistor, and by Ohm's law the voltage is resistance times current.
**Formula:** $U = RI$
**Conversions:** Not needed: $1\,\Omega \cdot 1\,\text{A} = 1\,\text{V}$.
**Substitution:** $U = 40\,\Omega \cdot 0.15\,\text{A} = 6.0\,\text{V}$
**Answer:** $6.0\,\text{V}$, two significant figures like the resistance and the current.
**Reasonableness:** The estimates $40\,\Omega \cdot 0.1\,\text{A} = 4\,\text{V}$ and $40\,\Omega \cdot 0.2\,\text{A} = 8\,\text{V}$ put $6\,\text{V}$ between them. A drop of $6\,\text{V}$ is smaller than the voltage of a typical battery or mains adapter ($9\,\text{V}$ or $12\,\text{V}$), so the resistor can be in such a circuit, and $\Omega \cdot \text{A} = \text{V}$ gives the right unit.

## fy6-5-L1-05
**Given:** the potentials of the graph at the points of the loop; the zero point is the negative terminal of the source
**Find:** the voltage $U_2$ of the resistor $R_2$ in volts
**Principle:** The voltage of a resistor is the potential difference between its ends. The resistor $R_2$ is between the points $B$ and $C$, so its voltage is the drop of potential from the point $B$ to the point $C$.
**Reading the graph:** At the point $B$ the potential is on the horizontal line at the $7\,\text{V}$ grid line and at the point $C$ at the $3\,\text{V}$ grid line. At the resistor $R_2$ the line drops between these.
**Formula:** $U_2 = V_B - V_C$
**Conversions:** Not needed: the potentials are read in volts.
**Substitution:** $U_2 = 7.0\,\text{V} - 3.0\,\text{V} = 4.0\,\text{V}$
**Answer:** $4.0\,\text{V}$, to two significant figures. The values are read from the $1\,\text{V}$ grid lines.
**Reasonableness:** The voltages of the resistors are $2\,\text{V}$, $4\,\text{V}$ and $3\,\text{V}$, together $9\,\text{V}$, as much as the rise in the source. The voltage law holds.

## fy6-5-L2-01
**Given:** $R = 220\,\Omega$, $I = 25\,\text{mA}$, $V_A = 9.0\,\text{V}$; the current flows from the point $A$ to the point $B$
**Find:** the potential $V_B$ of the point $B$ in volts
**Principle:** In a resistor the potential drops in the direction of the current by the voltage $RI$ given by Ohm's law. The point $B$ is after the resistor, so its potential is smaller than that of the point $A$.
**Formula:** $V_A - V_B = RI$, from which $V_B = V_A - RI$
**Conversions:** $I = 25\,\text{mA} = 25 \cdot 0.001\,\text{A} = 0.025\,\text{A}$
**Substitution:** $V_B = 9.0\,\text{V} - 220\,\Omega \cdot 0.025\,\text{A} = 9.0\,\text{V} - 5.5\,\text{V} = 3.5\,\text{V}$
**Answer:** $3.5\,\text{V}$, to one decimal place like the potential $9.0\,\text{V}$.
**Reasonableness:** The potential drops in the resistor, and $3.5\,\text{V}$ is smaller than $9.0\,\text{V}$. Without converting the milliamperes the drop would be $5500\,\text{V}$, which is impossible in a $9\,\text{V}$ circuit.

## fy6-5-L2-02
**Given:** $U = 12.0\,\text{V}$, $R_1 = 200\,\Omega$ (on the side of the positive terminal), $R_2 = 400\,\Omega$ (on the side of the negative terminal); the negative terminal is the zero point
**Find:** the potential $V$ of the wire between the resistors in volts
**Principle:** In a series connection the same current flows through both resistors, and the total resistance is the sum of the resistances. Between the middle wire and the negative terminal there is only the resistor $R_2$, so the potential of the middle wire is the voltage of the resistor $R_2$.
**Formula:** $I = \dfrac{U}{R_1 + R_2}$ and $V = R_2 I$, so $V = \dfrac{R_2 U}{R_1 + R_2}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{12.0\,\text{V}}{200\,\Omega + 400\,\Omega} = 0.020\,\text{A}$ and $V = 400\,\Omega \cdot 0.020\,\text{A} = 8.0\,\text{V}$
**Answer:** $8.0\,\text{V}$, two significant figures, because the resistances are given to two figures.
**Reasonableness:** The voltage of the resistor $R_1$ is $200\,\Omega \cdot 0.020\,\text{A} = 4.0\,\text{V}$, and $4.0\,\text{V} + 8.0\,\text{V} = 12.0\,\text{V}$. The larger resistor gets the larger share of the voltage, as it should in a series connection.

## fy6-5-L2-03
**Given:** from the figure $U = 6.0\,\text{V}$, parallel resistors $R_2 = 20\,\Omega$ and $R_3 = 30\,\Omega$
**Find:** the current $I$ of the main wire in amperes
**Principle:** Each branch forms with the source a loop that has no other resistors, so by the voltage law the voltage of each resistor is the voltage of the source. By the current law the current of the main wire is the sum of the currents of the branches.
**Formula:** $I_2 = \dfrac{U}{R_2}$, $I_3 = \dfrac{U}{R_3}$ and $I = I_2 + I_3$, so $I = \dfrac{U}{R_2} + \dfrac{U}{R_3}$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{6.0\,\text{V}}{20\,\Omega} + \dfrac{6.0\,\text{V}}{30\,\Omega} = 0.30\,\text{A} + 0.20\,\text{A} = 0.50\,\text{A}$
**Answer:** $0.50\,\text{A}$, two significant figures like the initial data.
**Reasonableness:** The total resistance of the parallel connection is $12\,\Omega$, and $6.0\,\text{V} : 12\,\Omega = 0.50\,\text{A}$ gives the same result. The branch with the smaller resistance carries the larger current.

## fy6-5-L2-04
**Given:** $U = 9.0\,\text{V}$, $R_1 = 120\,\Omega$, current $I = 50\,\text{mA}$
**Find:** the resistance $R_2$ in ohms
**Principle:** In a series connection the same current flows through both resistors. By the voltage law the voltage of the source is shared among the resistors: $U = R_1 I + R_2 I$.
**Formula:** $U = R_1 I + R_2 I$, from which $R_2 = \dfrac{U - R_1 I}{I}$
**Conversions:** $I = 50\,\text{mA} = 50 \cdot 0.001\,\text{A} = 0.050\,\text{A}$
**Substitution:** $R_2 = \dfrac{9.0\,\text{V} - 120\,\Omega \cdot 0.050\,\text{A}}{0.050\,\text{A}} = \dfrac{3.0\,\text{V}}{0.050\,\text{A}} = 60\,\Omega$
**Answer:** $60\,\Omega$, two significant figures like the voltage and the current.
**Reasonableness:** The total resistance $120\,\Omega + 60\,\Omega = 180\,\Omega$ gives the current $9.0\,\text{V} : 180\,\Omega = 0.050\,\text{A}$, which is the measured reading. The voltage $3.0\,\text{V}$ of the resistor $R_2$ is half the voltage of the resistor $R_1$, as the ratio of the resistances requires.

## fy6-5-L3-01
**Given:** $U = 12\,\text{V}$, $R_1 = 30\,\Omega$, $R_2 = 50\,\Omega$, $R_3 = 40\,\Omega$ in series; the zero point is between the resistors $R_1$ and $R_2$
**Find:** the potential $V_-$ of the negative terminal of the source in volts, with its sign
**Principle:** In a series connection the same current flows through all the resistors. When we go from the zero point in the direction of the current to the negative terminal, the potential drops in the resistors $R_2$ and $R_3$ by their voltages. So the potential of the negative terminal is negative.
**Formula:** $I = \dfrac{U}{R_1 + R_2 + R_3}$ and $0 - R_2 I - R_3 I = V_-$, so $V_- = -(R_2 + R_3) I$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{12\,\text{V}}{30\,\Omega + 50\,\Omega + 40\,\Omega} = 0.10\,\text{A}$ and $V_- = -(50\,\Omega + 40\,\Omega) \cdot 0.10\,\text{A} = -9.0\,\text{V}$
**Answer:** $-9.0\,\text{V}$, two significant figures like the voltage $12\,\text{V}$.
**Reasonableness:** The potential of the positive terminal is $R_1 I = 3.0\,\text{V}$, so the voltage between the terminals of the source is $3.0\,\text{V} - (-9.0\,\text{V}) = 12\,\text{V}$, as it should be. Moving the zero point did not change the voltages, only the values of the potentials.

## fy6-5-L3-02
**Given:** from the figure $U = 12\,\text{V}$, $R_1 = 40\,\Omega$, $R_2 = 60\,\Omega$, current of the main wire $I_1 = 0.20\,\text{A}$
**Find:** the resistance $R_3$ in ohms
**Principle:** The whole current flows through the resistor $R_1$. By the voltage law the common voltage of the branches is the voltage of the source minus the voltage of the resistor $R_1$. By the current law the current of the resistor $R_3$ is the current of the main wire minus the current of the resistor $R_2$, and Ohm's law gives the resistance.
**Formula:** $U_{23} = U - R_1 I_1$, $I_3 = I_1 - \dfrac{U_{23}}{R_2}$ and $R_3 = \dfrac{U_{23}}{I_3}$
**Conversions:** Not needed: all quantities are in base units.
**Substitution:** $U_{23} = 12\,\text{V} - 40\,\Omega \cdot 0.20\,\text{A} = 4.0\,\text{V}$, $I_3 = 0.20\,\text{A} - \dfrac{4.0\,\text{V}}{60\,\Omega} = 0.1333\,\text{A}$ and $R_3 = \dfrac{4.0\,\text{V}}{0.1333\,\text{A}} = 30.0\,\Omega$
**Answer:** $30\,\Omega$, two significant figures like the current $0.20\,\text{A}$.
**Reasonableness:** The total resistance of the parallel connection of $60\,\Omega$ and $30\,\Omega$ is $20\,\Omega$, and the $40\,\Omega + 20\,\Omega = 60\,\Omega$ of the whole circuit gives the current $12\,\text{V} : 60\,\Omega = 0.20\,\text{A}$, which is the reading of the meter. The current of the resistor $R_3$ is twice the current of the resistor $R_2$, because its resistance is half.

## fy6-5-L3-03
**Given:** $U = 12\,\text{V}$, a resistor $R = 20\,\Omega$ between the positive terminal and the bulbs, two parallel bulbs, the resistance of each $R_\text{L} = 60\,\Omega$ (constant); the negative terminal is the zero point
**Find:** the change $\Delta V$ of the potential of the junction between the resistor and the bulbs in volts, with its sign
**Principle:** The resistances of the source and the wires are neglected. Between the junction of the resistor and the bulbs and the negative terminal there is the bulb branch, so the potential of the junction is the voltage of the bulbs. By the voltage law it is the voltage of the source minus the voltage $RI$ of the series resistor. When a bulb is removed, the resistance of the branch increases, the current decreases, the voltage of the series resistor decreases and the voltage of the bulb increases.
**Formula:** $V = \dfrac{R_\text{b}}{R + R_\text{b}}\, U$, where $R_\text{b}$ is the resistance of the bulb branch; $\Delta V = V_\text{one} - V_\text{two}$
**Conversions:** Not needed: all quantities are in base units.
**Substitution:** Two bulbs: $R_\text{b} = 30\,\Omega$ and $V_\text{two} = \dfrac{30\,\Omega}{50\,\Omega} \cdot 12\,\text{V} = 7.2\,\text{V}$. One bulb: $R_\text{b} = 60\,\Omega$ and $V_\text{one} = \dfrac{60\,\Omega}{80\,\Omega} \cdot 12\,\text{V} = 9.0\,\text{V}$. $\Delta V = 9.0\,\text{V} - 7.2\,\text{V} = 1.8\,\text{V}$
**Answer:** $1.8\,\text{V}$, two significant figures like the resistances.
**Reasonableness:** The current decreases from $0.24\,\text{A}$ to $0.15\,\text{A}$, so the voltage of the series resistor decreases from $4.8\,\text{V}$ to $3.0\,\text{V}$, that is, by $1.8\,\text{V}$, and the voltage of the bulb increases by exactly that much. The remaining bulb shines brighter, because its voltage increases.
