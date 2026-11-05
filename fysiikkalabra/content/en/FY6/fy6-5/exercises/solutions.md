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

## fy6-5-L1-06
**Find:** why the sum of the currents arriving at a junction is equal to the sum of the currents leaving it.
**Principle:** Current is the charge that passes through the cross-section of a wire in a unit of time. A junction is a point of a wire where charge cannot collect and where none is created or destroyed. So the charge arriving there leaves at the same rate, and this is Kirchhoff's current law.
**Model answer:** The law follows from the conservation of charge: charge is neither created, destroyed nor collected at the junction, so the sum of the arriving currents is equal to the sum of the leaving currents. The current does not divide equally among the branches, but the resistances of the branches determine how large a share of the current flows in each branch. The common voltage of the branches does not explain the current law, and current is not used up in a resistor: in a resistor the potential decreases, not the current.

## fy6-5-L1-07
**Find:** what happens to the potentials, the voltages and the current when another point is chosen as the zero point.
**Principle:** Potential is the voltage of a point relative to the chosen zero point, and voltage is the difference of the potentials of two points $U_{AB} = V_A - V_B$. When all potentials are measured from the new zero point, each changes by the same amount, and in the difference the change cancels out. The current is determined by the source and the resistors, not by the choice of the zero point.
**Model answer:** The potentials of all points change by the same amount. When the positive terminal is chosen as the zero point, the potential of the positive terminal is $0$ and the potential of the negative terminal is negative, and its magnitude is the voltage of the source. The voltages between the points, including the voltages of the resistors, stay the same, because they are differences of potentials. The current in the resistors does not change, because the zero point is only a choice made for calculation and does not change how the circuit works. So what stays unchanged is not the potentials but the voltages and the currents.

## fy6-5-L1-08
**Given:** $V_A = 9.0\,\text{V}$, $R_1 = 60\,\Omega$, $R_2 = 90\,\Omega$, $I = 0.040\,\text{A}$
**Find:** the potential $V_C$ of the point $C$ in volts
**Principle:** The same current flows through both resistors. In a resistor the potential drops in the direction of the current by the voltage $RI$, so when going from the point $A$ to the point $C$ the potential drops by the voltage of each resistor.
**Formula:** $V_C = V_A - R_1 I - R_2 I$
**Conversions:** Not needed: all quantities are in base units.
**Substitution:** $V_C = 9.0\,\text{V} - 60\,\Omega \cdot 0.040\,\text{A} - 90\,\Omega \cdot 0.040\,\text{A} = 9.0\,\text{V} - 2.4\,\text{V} - 3.6\,\text{V} = 3.0\,\text{V}$
**Answer:** $3.0\,\text{V}$, two significant figures like the given values.
**Reasonableness:** The total drop in the resistors is $150\,\Omega \cdot 0.040\,\text{A} = 6.0\,\text{V}$, and $9.0\,\text{V} - 6.0\,\text{V} = 3.0\,\text{V}$. The potential decreases in the direction of the current, so $V_C$ is smaller than $V_A$.

## fy6-5-L2-05
**Given:** $U = 12\,\text{V}$, $R_1 = 60\,\Omega$, $R_2 = 80\,\Omega$, $R_3 = 50\,\Omega$ in parallel; readings $\text{A}_0$: $0.50\,\text{A}$, $\text{A}_1$: $0.20\,\text{A}$, $\text{A}_2$: $0.15\,\text{A}$, $\text{A}_3$: $0.24\,\text{A}$
**Find:** the wrong reading and the correct reading $I_0$ of the meter $\text{A}_0$ in the main wire in amperes
**Principle:** The voltage of each resistor of the parallel branches is the voltage of the source, so Ohm's law $I = U : R$ gives the branch currents, and the branch meters can be checked with them. By Kirchhoff's current law the current of the main wire is the sum of the branch currents.
**Formula:** $I_k = \dfrac{U}{R_k}$ and $I_0 = I_1 + I_2 + I_3$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $\dfrac{12\,\text{V}}{60\,\Omega} = 0.20\,\text{A}$, $\dfrac{12\,\text{V}}{80\,\Omega} = 0.15\,\text{A}$ and $\dfrac{12\,\text{V}}{50\,\Omega} = 0.24\,\text{A}$, as the branch meters show. The sum of the branch currents is $0.20\,\text{A} + 0.15\,\text{A} + 0.24\,\text{A} = 0.59\,\text{A}$.
**Answer:** $0.59\,\text{A}$. The wrong reading is that of the meter in the main wire, $0.50\,\text{A}$, because it is smaller than the sum of the branch currents.
**Reasonableness:** The total resistance would be $12\,\text{V} : 0.59\,\text{A} \approx 20\,\Omega$, which is smaller than the smallest branch resistance $50\,\Omega$, as it should be in a parallel connection. With the reading $0.50\,\text{A}$ more current would leave into the branches than arrives at the point.

## fy6-5-L2-06
**Given:** potentials $V_A = 12.0\,\text{V}$, $V_B = 8.4\,\text{V}$, $V_C = 8.4\,\text{V}$, $V_D = 3.6\,\text{V}$, $V_E = 0\,\text{V}$; current $I = 0.12\,\text{A}$
**Find:** the resistance of the resistor $R_2$ in ohms
**Principle:** Between the points $B$ and $C$ there is only a wire, in which the potential does not change ($\Delta V = 0$), so they have the same potential. The resistor $R_2$ is between the points $C$ and $D$, so its voltage is the difference of the potentials. In a series connection the same current flows through it, and Ohm's law gives the resistance.
**Formula:** $U_2 = V_C - V_D$ and $R_2 = \dfrac{U_2}{I}$
**Conversions:** Not needed: the potentials are in volts and the current in amperes.
**Substitution:** $U_2 = 8.4\,\text{V} - 3.6\,\text{V} = 4.8\,\text{V}$ and $R_2 = \dfrac{4.8\,\text{V}}{0.12\,\text{A}} = 40\,\Omega$
**Answer:** $40\,\Omega$, two significant figures like the current.
**Reasonableness:** The voltages of the resistors are $12.0\,\text{V} - 8.4\,\text{V} = 3.6\,\text{V}$, $4.8\,\text{V}$ and $3.6\,\text{V} - 0\,\text{V} = 3.6\,\text{V}$, together $12.0\,\text{V}$, the voltage of the source. The resistances $30\,\Omega$, $40\,\Omega$ and $30\,\Omega$ give the current $12.0\,\text{V} : 100\,\Omega = 0.12\,\text{A}$, which is the measured reading.

## fy6-5-L2-07
**Given:** $U = 9.0\,\text{V}$, $R_1 = 100\,\Omega$, $R_2 = 200\,\Omega$; the zero point is the positive terminal of the source; the student's current $0.030\,\text{A}$
**Find:** the student's error and the correct potential $V$ of the wire between the resistors in volts, with its sign
**Principle:** The student's current is correct but the sign is wrong. In a resistor the potential drops in the direction of the current, and the current flows from the positive terminal through the resistor $R_1$. When the zero point is the positive terminal, the potential of the wire between the resistors is therefore below zero: $V = 0 - R_1 I$.
**Formula:** $I = \dfrac{U}{R_1 + R_2}$ and $V = 0 - R_1 I$
**Conversions:** Not needed: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{9.0\,\text{V}}{100\,\Omega + 200\,\Omega} = 0.030\,\text{A}$ and $V = 0 - 100\,\Omega \cdot 0.030\,\text{A} = -3.0\,\text{V}$
**Answer:** $-3.0\,\text{V}$, two significant figures. The error was in the sign: the student treated the drop in the resistor as a rise.
**Reasonableness:** The potential of the negative terminal is $-9.0\,\text{V}$. The voltage of the resistor $R_1$ is $0 - (-3.0\,\text{V}) = 3.0\,\text{V}$ and the voltage of the resistor $R_2$ is $-3.0\,\text{V} - (-9.0\,\text{V}) = 6.0\,\text{V}$, and they correspond to the products $100\,\Omega \cdot 0.030\,\text{A}$ and $200\,\Omega \cdot 0.030\,\text{A}$.

## fy6-5-L3-04
**Given:** $U_1 = 12\,\text{V}$, $U_2 = 9.0\,\text{V}$, $R_1 = 30\,\Omega$, $R_2 = 20\,\Omega$, $R_3 = 30\,\Omega$; currents $I_1$ and $I_3$ to the point $P$ and $I_2$ from the point $P$
**Find:** the branch currents and especially the current $I_2$ in amperes, and the check with the energy balance
**Principle:** At the junction $P$ the current law gives $I_1 + I_3 = I_2$. The left loop (source $U_1$, resistors $R_1$ and $R_2$) and the right loop (source $U_2$, resistors $R_3$ and $R_2$) are traversed in the direction of the current, and by the voltage law the sum of the changes of potential is zero in each. Three equations are enough for three unknown currents. In the energy balance the power produced by the sources turns completely into internal energy of the resistors, because no energy is lost in ideal sources and wires.
**Formula:** $I_1 + I_3 = I_2$, $U_1 - R_1 I_1 - R_2 I_2 = 0$ and $U_2 - R_3 I_3 - R_2 I_2 = 0$. From the loop equations $I_1 = \dfrac{U_1 - R_2 I_2}{R_1}$ and $I_3 = \dfrac{U_2 - R_2 I_2}{R_3}$. Power: $P = UI$ in a source and $P = RI^2$ in a resistor.
**Conversions:** Not needed: all quantities are in base units.
**Substitution:** From the loop equations (the units $\text{V}$, $\Omega$ and $\text{A}$ left out):

$$\begin{aligned} I_1 &= \frac{12 - 20\, I_2}{30} \\ I_3 &= \frac{9.0 - 20\, I_2}{30} \end{aligned}$$

From the current law $I_1 + I_3 = I_2$:

$$\begin{aligned} \frac{21 - 40\, I_2}{30} &= I_2 \\ 21 &= 70\, I_2 \\ I_2 &= 0.30\,\text{A} \end{aligned}$$

Then $I_1 = \dfrac{12\,\text{V} - 6.0\,\text{V}}{30\,\Omega} = 0.20\,\text{A}$ and $I_3 = \dfrac{9.0\,\text{V} - 6.0\,\text{V}}{30\,\Omega} = 0.10\,\text{A}$.

The power of the sources is $12\,\text{V} \cdot 0.20\,\text{A} + 9.0\,\text{V} \cdot 0.10\,\text{A} = 2.4\,\text{W} + 0.9\,\text{W} = 3.3\,\text{W}$. The power of the resistors is $30\,\Omega \cdot (0.20\,\text{A})^2 + 20\,\Omega \cdot (0.30\,\text{A})^2 + 30\,\Omega \cdot (0.10\,\text{A})^2 = 1.2\,\text{W} + 1.8\,\text{W} + 0.3\,\text{W} = 3.3\,\text{W}$.
**Answer:** $I_2 = 0.30\,\text{A}$, two significant figures like the given values. The other branch currents are $I_1 = 0.20\,\text{A}$ and $I_3 = 0.10\,\text{A}$, and the power of the sources and the power of the resistors are both $3.3\,\text{W}$, so the energy balance holds.
**Reasonableness:** The current law holds: $0.20\,\text{A} + 0.10\,\text{A} = 0.30\,\text{A}$. The voltage between the points $P$ and $Q$ is $R_2 I_2 = 6.0\,\text{V}$, and it is obtained also from the side of each source: $12\,\text{V} - 30\,\Omega \cdot 0.20\,\text{A} = 6.0\,\text{V}$ and $9.0\,\text{V} - 30\,\Omega \cdot 0.10\,\text{A} = 6.0\,\text{V}$. All the currents are positive, so each source really does produce current to the point $P$.

## fy6-5-L3-05
**Given:** $U = 12\,\text{V}$, $R_1 = 100\,\Omega$, $R_2 = 100\,\Omega$; load $R_\text{L}$ in parallel with the resistor $R_2$; the negative terminal is the zero point; the measurements of the table
**Find:** the load resistance $R_\text{L}$ in ohms when $V_P = 5.0\,\text{V}$; in addition the explanation of the unloaded and the loaded divider and the result with the load $100\,\Omega$
**Principle:** Without a load the resistors $R_1$ and $R_2$ are in series, and the potential of the point $P$ is the voltage of the resistor $R_2$. When a load is connected, by the current law the current of the resistor $R_1$ divides between the resistor $R_2$ and the load, and these are in parallel, so they have the same voltage $V_P$. The load decreases the resistance of the branch, the total current increases, the voltage of the resistor $R_1$ increases and by the voltage law $V_P = U - R_1 I$ decreases. The asked resistance is obtained by inverting the divider formula: first the resistance $R_\text{p}$ of the branch, from which the load.
**Formula:** Unloaded: $V_P = \dfrac{R_2}{R_1 + R_2}\, U$. Loaded: $\dfrac{1}{R_\text{p}} = \dfrac{1}{R_2} + \dfrac{1}{R_\text{L}}$ and $V_P = \dfrac{R_\text{p}}{R_1 + R_\text{p}}\, U$. When $V_P$ is known, $R_\text{p} = \dfrac{R_1 V_P}{U - V_P}$ and $R_\text{L} = \dfrac{R_\text{p} R_2}{R_2 - R_\text{p}}$ (solved from the formula of the parallel connection).
**Conversions:** Not needed: all quantities are in base units.
**Substitution:** a) Without a load the resistors $R_1$ and $R_2$ are in series, so the current is the same everywhere and by the voltage law the voltage of the source divides between them. Since $R_1 = R_2$, the potential of the point $P$ is half the voltage of the source: $V_P = \dfrac{100\,\Omega}{200\,\Omega} \cdot 12\,\text{V} = 6.00\,\text{V}$. When a load is connected, by the current law the current of the resistor $R_1$ divides between the resistor $R_2$ and the load, so the current increases, the voltage of the resistor $R_1$ increases and $V_P = U - R_1 I$ decreases.

b) With the load $100\,\Omega$ we have $R_\text{p} = 50\,\Omega$ and $V_P = \dfrac{50\,\Omega}{150\,\Omega} \cdot 12\,\text{V} = 4.0\,\text{V}$. The result agrees with the value $4.01\,\text{V}$ of the table within the accuracy of the measurement.

c) $R_\text{p} = \dfrac{100\,\Omega \cdot 5.0\,\text{V}}{12\,\text{V} - 5.0\,\text{V}} = 71.4\,\Omega$ and $R_\text{L} = \dfrac{71.4\,\Omega \cdot 100\,\Omega}{100\,\Omega - 71.4\,\Omega} = 250\,\Omega$.

**Answer:** $250\,\Omega$, to two significant figures. A smaller load resistance would lower the potential below $5.0\,\text{V}$ (with the load $100\,\Omega$ it is $4.0\,\text{V}$) and a greater load resistance would raise it closer to $6.0\,\text{V}$.
**Reasonableness:** When $R_\text{L} = 250\,\Omega$, the current of the resistor $R_1$ is $12\,\text{V} : (100\,\Omega + 71.4\,\Omega) = 0.070\,\text{A}$ and its voltage is $100\,\Omega \cdot 0.070\,\text{A} = 7.0\,\text{V}$, so $V_P = 12\,\text{V} - 7.0\,\text{V} = 5.0\,\text{V}$. The currents in the branches are $5.0\,\text{V} : 100\,\Omega = 0.050\,\text{A}$ and $5.0\,\text{V} : 250\,\Omega = 0.020\,\text{A}$, together $0.070\,\text{A}$, as the current law requires. The value $250\,\Omega$ lies between the rows $1000\,\Omega$ ($5.72\,\text{V}$) and $100\,\Omega$ ($4.01\,\text{V}$) of the table, just like $5.0\,\text{V}$.
