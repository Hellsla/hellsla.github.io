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

## fy6-15-L1-06
**Find:** which statement about the purpose of protective earthing is correct
**Principle:** Protective earthing connects the metal frame of a device to the protective conductor. If the live conductor touches the frame because of a fault, a large fault current flows along the protective conductor back to the supply and the fuse or the residual current device cuts off the current, so the frame does not stay live.
**Model answer:** The correct statement is the one according to which earthing gives the fault current a low-resistance path back to the supply, so the fuse or the residual current device cuts off the current. The statement about reduced electricity consumption is wrong, because in normal use no current flows in the earth conductor. The statement about insulating the frame from the ground is wrong, because earthing connects the frame to the protective conductor and does not insulate it. The statement about the frame being live all the time is wrong, because the purpose of earthing is to prevent the frame from staying live.

## fy6-15-L1-07
**Find:** which statement about a class II device is correct
**Principle:** The protection class tells how a device protects the user from electric shock. The metal frame of a class I device is protectively earthed, a class II device has double or reinforced insulation, and a class III device operates at a low safety voltage. The protection of class II therefore lies in the insulation: a single insulation fault does not yet bring the mains voltage to the casing.
**Model answer:** The correct statement is the one according to which the device has double insulation, so the casing does not become live because of a single fault. The statement about an earthed metal frame is wrong, because it describes class I. The statement about a low safety voltage is wrong, because it describes class III. The statement about a watertight casing is wrong, because the protection class tells about protection against electric shock and not about resistance to moisture.

## fy6-15-L1-08
**Given:** air gap $d = 2.0\,\text{mm}$, uniform field, dielectric strength of air $E_\text{max} = 3.0\,\text{MV/m}$
**Find:** the greatest allowed voltage $U_\text{max}$ in kilovolts
**Principle:** In a uniform field the field strength is the voltage divided by the length of the gap. Air does not break down when the field is at most the dielectric strength, so the greatest allowed voltage is the one at which the field is exactly $E_\text{max}$.
**Formula:** $E = \dfrac{U}{d} \le E_\text{max}$, so $U_\text{max} = E_\text{max}\,d$
**Conversions:** $d = 2.0\,\text{mm} = 2.0 \cdot 0.001\,\text{m} = 0.0020\,\text{m}$; $E_\text{max} = 3.0\,\text{MV/m} = 3.0 \cdot 1\,000\,000\,\text{V/m}$; the result $1\,\text{kV} = 1000\,\text{V}$.
**Substitution:** $U_\text{max} = 3\,000\,000\,\text{V/m} \cdot 0.0020\,\text{m} = 6000\,\text{V} = 6.0\,\text{kV}$
**Answer:** $6.0\,\text{kV}$, two significant figures like the dielectric strength $3.0\,\text{MV/m}$.
**Reasonableness:** One megavolt per metre is one kilovolt per millimetre, so air withstands about $3\,\text{kV}$ per millimetre and a gap of two millimetres $2 \cdot 3\,\text{kV} = 6\,\text{kV}$. The $230\,\text{V}$ of a socket is far below this, but the voltages of lightning or a high-voltage line are thousands of times larger.

## fy6-15-L1-09
**Find:** the order of situations A–D by the current $I$ through the body, from the smallest to the greatest.
**Principle:** The harm is done by the current through the body, and by Ohm's law it depends on both the contact voltage and the resistance of the current path, $I = U : R$. So the greatest voltage does not necessarily give the greatest current, nor the greatest resistance the smallest. We calculate the current of each situation.
**Model answer:** The currents are:

$I_\text{A} = 24\,\text{V} : 20\,\text{k}\Omega = 1.2\,\text{mA}$

$I_\text{B} = 230\,\text{V} : 46\,\text{k}\Omega = 5.0\,\text{mA}$

$I_\text{C} = 230\,\text{V} : 1.6\,\text{k}\Omega \approx 140\,\text{mA}$

$I_\text{D} = 1000\,\text{V} : 25\,\text{k}\Omega = 40\,\text{mA}$

The current $I_\text{C}$ is given with two significant figures like the resistance $1.6\,\text{k}\Omega$. By the current, from the smallest to the greatest, the order is A, B, D, C.

By the voltage the order would be different, A, B and C, D: the voltage of situation D, $1000\,\text{V}$, is the greatest, but the small resistance of a wet hand makes the current of situation C the greatest. The resistance alone does not decide either: the resistance of situation A is smaller than those of situations B and D, but its voltage is so small that the current remains the smallest.

The current of situation A only exceeds the threshold of perception. With these values the current of situation B stays below the let-go threshold $10\,\text{mA}$, but shoes cannot be considered protection against electric shock: a wet floor, a damaged shoe or touching a tap at the same time bypasses them, and no current can be considered certainly safe. The current of situation D exceeds the limit $30\,\text{mA}$ at which breathing becomes difficult, and the current of situation C exceeds the limit $50\,\text{mA}$ at which there is a danger of ventricular fibrillation.

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

## fy6-15-L2-05
**Given:** touch voltage $U = 230\,\text{V}$; resistances from the table: $R_1 = 55\,\text{k}\Omega$ (dry skin, rubber shoes), $R_2 = 12\,\text{k}\Omega$ (dry skin, bare feet), $R_3 = 2.4\,\text{k}\Omega$ (wet hands), $R_4 = 0.90\,\text{k}\Omega$ (in a bathtub)
**Find:** a) the current $I$ in each situation and its effect; b) the ratio of the currents in the bathtub and with rubber shoes $I_4 : I_1$
**Principle:** The body is part of the circuit between the point of contact and the ground, so the current through the body is obtained from Ohm's law with the resistance of the current path. The effect of the current is read from its magnitude using the threshold values. The voltage is the same in every situation, so the currents are inversely proportional to the resistances.
**Formula:** $I = \dfrac{U}{R}$ and $\dfrac{I_4}{I_1} = \dfrac{U / R_4}{U / R_1} = \dfrac{R_1}{R_4}$
**Conversions:** $R_1 = 55\,\text{k}\Omega = 55 \cdot 1000\,\Omega = 55\,000\,\Omega$, and similarly $R_2 = 12\,000\,\Omega$, $R_3 = 2400\,\Omega$ and $R_4 = 900\,\Omega$; the currents from amperes to milliamperes: $1\,\text{A} = 1000\,\text{mA}$. In the ratio the kilohms cancel.
**Substitution:** $I_1 = \dfrac{230\,\text{V}}{55\,000\,\Omega} = 4.2\,\text{mA}$, $I_2 = \dfrac{230\,\text{V}}{12\,000\,\Omega} = 19.2\,\text{mA}$, $I_3 = \dfrac{230\,\text{V}}{2400\,\Omega} = 95.8\,\text{mA}$, $I_4 = \dfrac{230\,\text{V}}{900\,\Omega} = 255.6\,\text{mA}$ and $\dfrac{I_4}{I_1} = \dfrac{55\,\text{k}\Omega}{0.90\,\text{k}\Omega} = 61.11$
**Answer:** about $61$ times as large, two significant figures like the resistance $0.90\,\text{k}\Omega$. Part a): with rubber shoes $4.2\,\text{mA}$ is felt but stays below the let-go threshold; with bare feet $19\,\text{mA}$ exceeds the let-go threshold, so the grip may not release; with wet hands $96\,\text{mA}$ and in the bathtub $256\,\text{mA}$ exceed the limit for the danger of ventricular fibrillation.
**Reasonableness:** Estimate: $55 : 0.9 \approx 60$. The same ratio is obtained from the currents, $256\,\text{mA} : 4.2\,\text{mA} \approx 61$. All four currents are larger than the threshold of perception $0.5\,\text{mA}$, and the current grows from one situation to the next in the same order as the resistance decreases. At the same voltage, moisture and bare skin increase the current to over sixty times as large.

## fy6-15-L2-06
**Given:** rated current of the fuse $I_\text{f} = 10\,\text{A}$, voltage $U = 230\,\text{V}$; powers from the table: kettle $2000\,\text{W}$, vacuum cleaner $1400\,\text{W}$, iron $1100\,\text{W}$, toaster $800\,\text{W}$, coffee maker $600\,\text{W}$
**Find:** a) the pairs whose total current exceeds $I_\text{f}$; b) the greatest total power that does not exceed the limit, and the corresponding current $I$ in amperes
**Principle:** The devices of the circuit are in parallel at the same voltage, so their currents add up and the current in the circuit cable is the total power divided by the voltage. The rated current of the fuse is exceeded when the total power is larger than $P_\text{max} = UI_\text{f}$.
**Formula:** $P_\text{max} = UI_\text{f}$ and $I = \dfrac{P_1 + P_2}{U}$
**Conversions:** None needed: $1\,\text{W} : 1\,\text{V} = 1\,\text{A}$.
**Substitution:** $P_\text{max} = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}$. Total powers of the pairs: kettle and vacuum cleaner $3400\,\text{W}$, kettle and iron $3100\,\text{W}$, kettle and toaster $2800\,\text{W}$, kettle and coffee maker $2600\,\text{W}$, vacuum cleaner and iron $2500\,\text{W}$; all are over $2300\,\text{W}$. The other pairs are below it: the largest of them is the vacuum cleaner and the toaster, $1400\,\text{W} + 800\,\text{W} = 2200\,\text{W}$. The current is $I = \dfrac{2200\,\text{W}}{230\,\text{V}} = 9.565\,\text{A}$
**Answer:** $9.6\,\text{A}$, two significant figures like the rated current of the fuse. Part a): the rated current of the fuse is exceeded by the combinations of the kettle with every other device and by the pair of the vacuum cleaner and the iron.
**Reasonableness:** The current $9.6\,\text{A}$ is a little below the limit $10\,\text{A}$, so the pair fits in the circuit but leaves hardly any margin: the next largest pair, the vacuum cleaner and the coffee maker, would give only $2000\,\text{W} : 230\,\text{V} = 8.7\,\text{A}$. The kettle alone ($8.7\,\text{A}$) fits in the circuit, but no other device fits alongside it.

## fy6-15-L2-07
**Given:** fuse $16\,\text{A}$, touch voltage $U = 230\,\text{V}$, resistance of the current path $R = 2.00\,\text{k}\Omega$
**Find:** a) the error in the student's claim and the device that cuts off a small current; b) the current $I$ through the body in milliamperes
**Principle:** A fuse protects the cable from overheating, and its rated current is tens of amperes. The current through a person is tens or hundreds of milliamperes, that is, hundreds of times smaller, so the fuse does not notice it at all. The small current flowing through a person is cut off by the residual current device, which trips at a fault current of about $30\,\text{mA}$. The current through the body is obtained from Ohm's law.
**Formula:** $U = RI$, so $I = \dfrac{U}{R}$
**Conversions:** $R = 2.00\,\text{k}\Omega = 2.00 \cdot 1000\,\Omega = 2000\,\Omega$; $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $I = \dfrac{230\,\text{V}}{2000\,\Omega} = 0.115\,\text{A} = 115\,\text{mA}$
**Answer:** $115\,\text{mA}$, three significant figures like the voltage and the resistance. The student's error is thinking that the fuse would protect a person: the fuse does not notice the current through the body, because its rated current $16\,\text{A}$ is many times the current through the body. A fuse protects a person only together with protective earthing. The current through the body is cut off by the residual current device.
**Reasonableness:** The current of the fuse $16\,\text{A}$ is $16\,\text{A} : 0.115\,\text{A} \approx 139$ times the current through the body, so the fuse does not trip. The current $115\,\text{mA}$ is over twice the limit for the danger of ventricular fibrillation, $50\,\text{mA}$, and also many times the tripping current of the residual current device, $30\,\text{mA}$, so the residual current device would trip.

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

## fy6-15-L3-04
**Given:** resistance of the conductors $R = 0.40\,\Omega$; from the table the currents $I = 4.0$; $8.0$; $12.0$; $16.0\,\text{A}$ and the rises in temperature $\Delta T = 2.1$; $7.6$; $17.2$; $30.4\,\text{K}$; limit of the insulation $\Delta T_\text{max} = 50\,\text{K}$
**Find:** a) the slope $k$ in the unit $\text{K/W}$; b) the current $I_\text{max}$ at which the rise in temperature is $50\,\text{K}$, in amperes; c) whether the $16\,\text{A}$ and $25\,\text{A}$ fuses are enough
**Principle:** In the resistance of a conductor a thermal power $P = RI^2$ is produced (chapter *Electric power and heating of a resistor*). When the temperature has settled, the cord gives off to the surroundings the same power that is produced in it, and the measurement shows the rise in temperature growing with the power. If the points $(P, \Delta T)$ lie on a straight line through the origin, $\Delta T = kP$, that is, the rise in temperature is directly proportional to the power. When no power is produced, the cord is at the temperature of the surroundings, so the line passes through the origin.
**Reading the graph:** The points $(P, \Delta T)$ are $(6.4\,\text{W};\ 2.1\,\text{K})$, $(25.6\,\text{W};\ 7.6\,\text{K})$, $(57.6\,\text{W};\ 17.2\,\text{K})$ and $(102.4\,\text{W};\ 30.4\,\text{K})$. They lie almost on a straight line through the origin: the ratios $\Delta T : P$ are $0.33$; $0.30$; $0.30$ and $0.30\,\text{K/W}$ (the first differs, because a small rise in temperature can be read less accurately). The slope of the line fitted through the origin is $k = \dfrac{\sum P\,\Delta T}{\sum P^2}$.
**Formula:** $\Delta T = kP = kRI^2$, so $I_\text{max} = \sqrt{\dfrac{\Delta T_\text{max}}{kR}}$
**Conversions:** None needed: a rise in temperature is the same in kelvins and in degrees Celsius, and $1\,\text{K/W}$ comes directly from the units of the table.
**Substitution:** $\sum P\,\Delta T = 6.4 \cdot 2.1 + 25.6 \cdot 7.6 + 57.6 \cdot 17.2 + 102.4 \cdot 30.4 = 4311.7$ and $\sum P^2 = 6.4^2 + 25.6^2 + 57.6^2 + 102.4^2 = 14\,499.8$, so $k = \dfrac{4311.7}{14\,499.8}\,\dfrac{\text{K}}{\text{W}} = 0.2974\,\dfrac{\text{K}}{\text{W}}$. The current is $I_\text{max} = \sqrt{\dfrac{50\,\text{K}}{0.2974\,\text{K/W} \cdot 0.40\,\Omega}} = \sqrt{420.3\,\text{A}^2} = 20.50\,\text{A}$
**Answer:** $21\,\text{A}$, two significant figures like the limit $50\,\text{K}$ (part a: $k \approx 0.30\,\text{K/W}$). c) At a current of $16\,\text{A}$ the rise in temperature is $\Delta T = 0.2974 \cdot 0.40 \cdot 16^2\,\text{K} = 30\,\text{K}$, below the limit $50\,\text{K}$, so a $16\,\text{A}$ fuse is enough to protect this cord. At $25\,\text{A}$ the rise would be $0.2974 \cdot 0.40 \cdot 25^2\,\text{K} = 74\,\text{K}$, over the limit, so a $25\,\text{A}$ fuse would not protect the cord: the cord could become dangerously hot before the fuse trips.
**Reasonableness:** Check: at a current of $20.5\,\text{A}$ the power is $0.40 \cdot 20.5^2\,\text{W} = 168\,\text{W}$ and the rise $0.2974 \cdot 168\,\text{K} = 50\,\text{K}$. The limit $20.5\,\text{A}$ lies outside the greatest measured current $16\,\text{A}$, so it is an extrapolation. The current grows by the factor $20.5 : 16 = 1.28$, so the power and the rise in temperature grow by the factor $1.28^2 = 1.64$, so $30.4\,\text{K} \cdot 1.64 = 50\,\text{K}$.

## fy6-15-L3-05
**Given:** voltage $U = 230\,\text{V}$, resistance of the current path of the body $R_\text{k} = 1.5\,\text{k}\Omega$, tripping limit of the residual current device $30\,\text{mA}$; insulation resistances from the table: $R_\text{e} = 900$; $120$; $40$; $12$ and $4.0\,\text{k}\Omega$ in weeks 1, 3, 5, 7 and 9
**Find:** a) the current $I$ through the person in each week; b) the week in which the residual current device trips, and why it is not enough alone; c) the greatest $R_\text{e}$ at which the residual current device trips, in kilohms
**Principle:** The leakage flows from the live conductor through the insulation to the frame, from the frame through the person to the ground and back, so the resistances $R_\text{e}$ and $R_\text{k}$ are in series and the resistance of the whole current path is their sum (chapter *Resistors in series and in parallel*). The same current flows through the person and the residual current device, and it is obtained from Ohm's law. The residual current device trips when the current exceeds $I_\text{limit} = 30\,\text{mA}$, so at the limit $R_\text{e} + R_\text{k} = U : I_\text{limit}$.
**Formula:** $I = \dfrac{U}{R_\text{e} + R_\text{k}}$; at the limit $I_\text{limit} = \dfrac{U}{R_\text{e} + R_\text{k}}$, so $R_\text{e} = \dfrac{U}{I_\text{limit}} - R_\text{k}$
**Conversions:** $R_\text{k} = 1.5\,\text{k}\Omega = 1500\,\Omega$; $I_\text{limit} = 30\,\text{mA} = 0.030\,\text{A}$; for example $R_\text{e} = 900\,\text{k}\Omega = 900\,000\,\Omega$; the currents from amperes to milliamperes: $1\,\text{A} = 1000\,\text{mA}$; the result from ohms to kilohms: $1\,\text{k}\Omega = 1000\,\Omega$.
**Substitution:** At the limit $R_\text{e} = \dfrac{230\,\text{V}}{0.030\,\text{A}} - 1500\,\Omega = 7667\,\Omega - 1500\,\Omega = 6167\,\Omega = 6.167\,\text{k}\Omega$. The currents: week 1: $\dfrac{230\,\text{V}}{900\,000\,\Omega + 1500\,\Omega} = 0.26\,\text{mA}$; week 3: $\dfrac{230\,\text{V}}{121\,500\,\Omega} = 1.9\,\text{mA}$; week 5: $\dfrac{230\,\text{V}}{41\,500\,\Omega} = 5.5\,\text{mA}$; week 7: $\dfrac{230\,\text{V}}{13\,500\,\Omega} = 17.0\,\text{mA}$; week 9: $\dfrac{230\,\text{V}}{5500\,\Omega} = 41.8\,\text{mA}$
**Answer:** $6.2\,\text{k}\Omega$, two significant figures like the resistance of the body $1.5\,\text{k}\Omega$. Part b): the residual current device trips only in the measurement of week 9, where the current exceeds the limit; in weeks 3, 5 and 7 the current is above the threshold of perception, and in week 7 it also exceeds the let-go threshold $10\,\text{mA}$, so the grip may not release even though the residual current device does not trip. The residual current device protects only when the current is close to the danger of ventricular fibrillation, so the earthing of the frame must be in order and the use of the device must be stopped when the insulation has weakened.
**Reasonableness:** At the limit value $R_\text{e} = 6167\,\Omega$ the whole resistance is $7667\,\Omega$ and the current $230\,\text{V} : 7667\,\Omega = 30\,\text{mA}$. The resistance of week 9, $4.0\,\text{k}\Omega$, is smaller than the limit, so the current $41.8\,\text{mA}$ exceeds the tripping limit. The resistance of week 7, $12\,\text{k}\Omega$, is larger than the limit, so the current $17.0\,\text{mA}$ stays below it, even though for a person it is already dangerous.
