## fy6-15-L1-01
**Given:** power $P = 1500\,\text{W}$, voltage $U = 230\,\text{V}$
**Find:** the current $I$ in amperes
**Principle:** Electric power is voltage times current. The mains voltage $230\,\text{V}$ is the rms value of the alternating voltage, so the power of a heating device is calculated with it as with a direct voltage.
**Formula:** $P = UI$, so $I = \dfrac{P}{U}$
**Conversions:** None needed: $1\,\text{W} : 1\,\text{V} = 1\,\text{A}$.
**Substitution:** $I = \dfrac{1500\,\text{W}}{230\,\text{V}} = 6.522\,\text{A}$
**Answer:** $6.5\,\text{A}$, two significant figures like the power $1500\,\text{W}$.
**Reasonableness:** The estimate $1500\,\text{W} : 200\,\text{V} = 7.5\,\text{A}$ is slightly larger, because the divisor is smaller. The current is below $10\,\text{A}$, so the heater fits alone in a $10\,\text{A}$ circuit, but there is not much room left for anything else on the same circuit.

## fy6-15-L1-02
**Given:** rated current of the fuse $I_\text{f} = 10\,\text{A}$, voltage $U = 230\,\text{V}$
**Find:** the greatest total power $P_\text{max}$ in watts
**Principle:** The devices of the circuit are in parallel at the same voltage, so their currents add up and the current in the circuit cable is the total power divided by the voltage. The rated current is not exceeded when this current is at most $I_\text{f}$.
**Formula:** $I = \dfrac{P_1 + P_2 + \dots}{U} \le I_\text{f}$, so $P_\text{max} = UI_\text{f}$
**Conversions:** None needed: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Substitution:** $P_\text{max} = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}$
**Answer:** $2300\,\text{W}$, that is, $2.3\,\text{kW}$, two significant figures like the rated current $10\,\text{A}$.
**Reasonableness:** One $2000\,\text{W}$ kettle fits in the circuit, but the kettle and a $900\,\text{W}$ toaster together do not. This matches the experience that the fuse of an old kitchen trips when too many heating devices are on at the same time.

## fy6-15-L1-03
**Given:** touch voltage $U = 230\,\text{V}$, resistance of the current path $R = 2.3\,\text{k}\Omega$
**Find:** the current $I$ through the body in milliamperes
**Principle:** The body is part of the circuit between the point of contact and the ground, so the current through it is obtained from Ohm's law with the resistance of the whole current path.
**Formula:** $U = RI$, so $I = \dfrac{U}{R}$
**Conversions:** $R = 2.3\,\text{k}\Omega = 2.3 \cdot 1000\,\Omega = 2300\,\Omega$; the result from amperes to milliamperes: $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $I = \dfrac{230\,\text{V}}{2300\,\Omega} = 0.100\,\text{A} = 100\,\text{mA}$
**Answer:** $100\,\text{mA}$, two significant figures like the resistance $2.3\,\text{k}\Omega$.
**Reasonableness:** The numerical value of the resistance $2300\,\Omega$ is ten times that of the voltage $230\,\text{V}$, so the numerical value of the current in amperes is one tenth, about $0.1\,\text{A}$. The current is twice the limit for the danger of ventricular fibrillation, about $50\,\text{mA}$, so touching with wet hands is life-threatening.

## fy6-15-L1-04
**Given:** touch voltage $U = 230\,\text{V}$, resistance of the current path $R = 50\,\text{k}\Omega$
**Find:** the current $I$ through the body in milliamperes
**Principle:** The body, the shoes and the floor are in the same current path, and their combined resistance is given. The current is obtained from Ohm's law.
**Formula:** $U = RI$, so $I = \dfrac{U}{R}$
**Conversions:** $R = 50\,\text{k}\Omega = 50 \cdot 1000\,\Omega = 50\,000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $I = \dfrac{230\,\text{V}}{50\,000\,\Omega} = 0.0046\,\text{A} = 4.6\,\text{mA}$
**Answer:** $4.6\,\text{mA}$, two significant figures like the resistance $50\,\text{k}\Omega$.
**Reasonableness:** The current is clearly felt, because it is almost ten times the threshold of perception $0.5\,\text{mA}$, but it stays below the let-go threshold $10\,\text{mA}$. With wet hands the resistance can be a tenth or less, and then the current is ten times as large. The result holds only with undamaged, dry shoes and a dry floor, when the person does not touch anything earthed at the same time, such as a tap; otherwise the current bypasses the shoes. Shoes must not be regarded as protection.

## fy6-15-L1-05
**Given:** resistance of the conductors $R = 0.20\,\Omega$, current $I = 16\,\text{A}$
**Find:** the thermal power $P$ produced in the extension cord
**Principle:** In the resistance of a conductor, electrical energy is transformed into the internal energy of the conductor, which is transferred as heat to the surroundings. When the resistance and the current of the conductor are known, the power is obtained from Joule's law.
**Formula:** $P = RI^2$
**Conversions:** None needed: $1\,\Omega \cdot (1\,\text{A})^2 = 1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Substitution:** $P = 0.20\,\Omega \cdot (16\,\text{A})^2 = 0.20\,\Omega \cdot 256\,\text{A}^2 = 51.2\,\text{W}$
**Answer:** $51\,\text{W}$, two significant figures like the resistance and the current.
**Reasonableness:** The power is like that of a small incandescent lamp, but it is spread over the whole length of the cord, so an intact cord heats up only a little. If the cord is wound tightly on a reel, little energy is transferred from it as heat to the surroundings, and the cord can become dangerously hot.

## fy6-15-L2-01
**Given:** rated current $I_\text{f} = 16\,\text{A}$, voltage $U = 230\,\text{V}$, powers that are on $P_1 = 2000\,\text{W}$ and $P_2 = 1200\,\text{W}$
**Find:** the power $P_\text{extra}$ that can still be connected to the circuit
**Principle:** The devices of the circuit are in parallel, so the currents add up and the total current is the total power divided by the voltage. The rated current is not exceeded when the total power is at most $UI_\text{f}$; the extra power left is the difference between this and the power in use.
**Formula:** $\dfrac{P_1 + P_2 + P_\text{extra}}{U} = I_\text{f}$, so $P_\text{extra} = UI_\text{f} - (P_1 + P_2)$
**Conversions:** None needed: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Substitution:** $P_\text{extra} = 230\,\text{V} \cdot 16\,\text{A} - (2000\,\text{W} + 1200\,\text{W}) = 3680\,\text{W} - 3200\,\text{W} = 480\,\text{W}$
**Answer:** about $480\,\text{W}$. The difference is calculated from large numbers, so it is only indicative: the rated current $16\,\text{A}$ has two significant figures.
**Reasonableness:** In terms of currents: the kettle draws $8.7\,\text{A}$ and the microwave oven $5.2\,\text{A}$, together $13.9\,\text{A}$, so about $2.1\,\text{A}$ is left, that is, $230\,\text{V} \cdot 2.1\,\text{A} \approx 480\,\text{W}$. A toaster ($900\,\text{W}$) therefore does not fit, but a refrigerator does.

## fy6-15-L2-02
**Given:** power of the heater $P = 2000\,\text{W}$, voltage $U = 230\,\text{V}$, resistance of the conductors $R = 0.30\,\Omega$
**Find:** the thermal power $P_\text{c}$ produced in the extension cord
**Principle:** The extension cord is in series with the heater, so the current of the heater flows through it. The current is obtained from the power of the heater, and in the cord electrical energy is transformed into internal energy at the rate $RI^2$. Assumption: the voltage drop in the cord is so small that the current of the heater is the same as without the extension cord.
**Formula:** $P = UI$, so $I = \dfrac{P}{U}$; in the cord $P_\text{c} = RI^2$, so $P_\text{c} = R\left(\dfrac{P}{U}\right)^2$
**Conversions:** None needed: all quantities are in base units.
**Substitution:** $I = \dfrac{2000\,\text{W}}{230\,\text{V}} = 8.696\,\text{A}$ and $P_\text{c} = 0.30\,\Omega \cdot (8.696\,\text{A})^2 = 22.68\,\text{W}$
**Answer:** $23\,\text{W}$, two significant figures like the resistance $0.30\,\Omega$.
**Reasonableness:** The voltage across the cord is $RI = 0.30\,\Omega \cdot 8.7\,\text{A} \approx 2.6\,\text{V}$, very small compared with $230\,\text{V}$, so the assumption holds. About $1\,\%$ of the power of the heater is used in the cord, which is little but enough to heat a cord wound on a reel.

## fy6-15-L2-03
**Given:** voltage $U = 90\,\text{kV}$, dielectric strength of air $E_\text{max} = 3.0\,\text{MV/m}$, uniform field
**Find:** the smallest air gap $d$ in centimetres
**Principle:** In a uniform field, the strength of the field is the voltage divided by the length of the gap (chapter *The capacitor and its energy*). Air does not break down when the field is at most the dielectric strength, so the shortest allowed gap is the one where the field is exactly $E_\text{max}$.
**Formula:** $E = \dfrac{U}{d} \le E_\text{max}$, so $d = \dfrac{U}{E_\text{max}}$
**Conversions:** $U = 90\,\text{kV} = 90 \cdot 1000\,\text{V} = 90\,000\,\text{V}$; $E_\text{max} = 3.0\,\text{MV/m} = 3.0 \cdot 1\,000\,000\,\text{V/m}$; $1\,\text{m} = 100\,\text{cm}$.
**Substitution:** $d = \dfrac{90\,000\,\text{V}}{3\,000\,000\,\text{V/m}} = 0.030\,\text{m} = 3.0\,\text{cm}$
**Answer:** $3.0\,\text{cm}$, two significant figures like the dielectric strength $3.0\,\text{MV/m}$.
**Reasonableness:** One megavolt per metre is one kilovolt per millimetre, so air withstands about $3\,\text{kV}$ per millimetre, and $90\,\text{kV}$ requires $30\,\text{mm}$. Real safety distances are metres, because near a thin conductor the field is much stronger than a uniform one, moisture and dirt weaken the air and overvoltages can occur in the grid; the calculated gap is only a lower limit from the calculation.

## fy6-15-L2-04
**Given:** resistance of the current path $R = 1.5\,\text{k}\Omega$, greatest allowed current $I = 10\,\text{mA}$
**Find:** the greatest touch voltage $U$ in volts
**Principle:** The current through the body follows Ohm's law: when the resistance is given, the current grows with the voltage. The greatest allowed voltage is the one that gives exactly a current of $10\,\text{mA}$.
**Formula:** $I = \dfrac{U}{R}$, so $U = RI$
**Conversions:** $R = 1.5\,\text{k}\Omega = 1.5 \cdot 1000\,\Omega = 1500\,\Omega$; $I = 10\,\text{mA} = 10 \cdot 0.001\,\text{A} = 0.010\,\text{A}$.
**Substitution:** $U = 1500\,\Omega \cdot 0.010\,\text{A} = 15\,\text{V}$
**Answer:** $15\,\text{V}$, two significant figures like the resistance $1.5\,\text{k}\Omega$.
**Reasonableness:** The result is much smaller than the mains voltage $230\,\text{V}$ and smaller than the upper limit of protective extra-low voltage, $50\,\text{V}$. This is why an RCD and an especially low voltage are used in wet spaces: when the skin is wet, a voltage of just tens of volts can be dangerous.

## fy6-15-L3-01
**Given:** resistance of the conductors $R = 0.50\,\Omega$, rated current $I_1 = 10\,\text{A}$, actual current $I_2 = 22\,\text{A}$
**Find:** how many times as large the thermal power $P_2$ is compared with the power $P_1$
**Principle:** In the conductors, electrical energy is transformed into internal energy at the rate $P = RI^2$. The resistance is the same in both situations, so the ratio of the powers depends only on the ratio of the currents squared. A $25\,\text{A}$ fuse does not cut off a current of $22\,\text{A}$, so the cable is loaded beyond its rating.
**Formula:** $P_1 = RI_1^2$ and $P_2 = RI_2^2$, so $\dfrac{P_2}{P_1} = \dfrac{I_2^2}{I_1^2}$
**Conversions:** None needed: the currents are in the same unit, and the units cancel.
**Substitution:** $P_1 = 0.50\,\Omega \cdot (10\,\text{A})^2 = 50\,\text{W}$, $P_2 = 0.50\,\Omega \cdot (22\,\text{A})^2 = 242\,\text{W}$ and $\dfrac{P_2}{P_1} = \dfrac{242\,\text{W}}{50\,\text{W}} = 4.84$
**Answer:** about $4.8$ times as large, two significant figures like the current $22\,\text{A}$.
**Reasonableness:** The current is a little over twice as large, so the power is a little over four times as large, since $2^2 = 4$. The cable therefore heats up much more than it was designed to withstand, and the insulation can melt and catch fire. This is why a fuse must not be replaced with a larger one.

## fy6-15-L3-02
**Given:** voltage $U = 230\,\text{V}$, resistance of the body $R_\text{body} = 1.5\,\text{k}\Omega$, resistance of the shoes and the floor $R_\text{sh} = 100\,\text{k}\Omega$
**Find:** the current $I$ through the body in milliamperes
**Principle:** The current flows through the body, the shoes and the floor one after another, so the resistances are in series and their total resistance is the sum (chapter *Resistors in series and in parallel*). The same current flows through each, and it is obtained from Ohm's law with the total resistance.
**Formula:** $R = R_\text{body} + R_\text{sh}$ and $I = \dfrac{U}{R}$, so $I = \dfrac{U}{R_\text{body} + R_\text{sh}}$
**Conversions:** $R_\text{body} = 1.5 \cdot 1000\,\Omega = 1500\,\Omega$ and $R_\text{sh} = 100 \cdot 1000\,\Omega = 100\,000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $I = \dfrac{230\,\text{V}}{1500\,\Omega + 100\,000\,\Omega} = \dfrac{230\,\text{V}}{101\,500\,\Omega} = 0.002266\,\text{A} = 2.3\,\text{mA}$
**Answer:** $2.3\,\text{mA}$, two significant figures like the resistance of the body $1.5\,\text{k}\Omega$.
**Reasonableness:** Without shoes the current would be $230\,\text{V} : 1500\,\Omega \approx 150\,\text{mA}$, over the limit for the danger of ventricular fibrillation. Shoes and a dry floor reduce the current below the let-go threshold $10\,\text{mA}$, but the current is felt, because it is over the threshold of perception $0.5\,\text{mA}$. A wet floor, a damaged shoe or touching a tap or an earthed device at the same time would bypass the shoes completely, so shoes are not protection.

## fy6-15-L3-03
**Given:** the potential of the ground from the graph $(r, V)$; the feet at distances $r_1 = 2.0\,\text{m}$ and $r_2 = 3.0\,\text{m}$; resistance of the current path $R = 4.0\,\text{k}\Omega$
**Find:** the current $I$ flowing from one foot to the other in milliamperes
**Principle:** The voltage between the feet, that is, the step voltage, is the difference of the potentials of the ground at the feet. The current flows from one foot through the body to the other foot, and it is obtained from Ohm's law.
**Reading the graph:** At $r = 2.0\,\text{m}$ the curve passes through an intersection of the grid at the value $V_1 = 600\,\text{V}$ and at $r = 3.0\,\text{m}$ at the value $V_2 = 400\,\text{V}$. The step voltage is their difference.
**Formula:** $U = V_1 - V_2$ and $I = \dfrac{U}{R}$, so $I = \dfrac{V_1 - V_2}{R}$
**Conversions:** $R = 4.0\,\text{k}\Omega = 4.0 \cdot 1000\,\Omega = 4000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $I = \dfrac{600\,\text{V} - 400\,\text{V}}{4000\,\Omega} = \dfrac{200\,\text{V}}{4000\,\Omega} = 0.050\,\text{A} = 50\,\text{mA}$
**Answer:** $50\,\text{mA}$, two significant figures like the resistance $4.0\,\text{k}\Omega$.
**Reasonableness:** The current is at the limit for the danger of ventricular fibrillation, even though the person does not touch the conductor at all. If the feet were together, the potential difference and the current would be almost zero. A current from one foot to the other does not necessarily pass through the heart, but a fall can bring the heart into the path of the current. Farther away the curve levels off: the voltage between $4.0\,\text{m}$ and $6.0\,\text{m}$ is only $100\,\text{V}$, even though the gap is two metres, so it is worth moving away with short steps.
