## fy7-8-L1-01
**Given:** number of turns of the primary coil $N_1 = 1200$, of the secondary coil $N_2 = 60$, primary voltage $U_1 = 230\,\text{V}$, ideal transformer
**Find:** the secondary voltage $U_2$ in volts
**Principle:** In the iron core of a transformer the same changing magnetic flux passes through every turn of both coils, so an equal voltage is induced in every turn. Therefore the voltages of an ideal transformer are in the same ratio as the numbers of turns.
**Formula:** $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$, so $U_2 = \dfrac{U_1 N_2}{N_1}$
**Conversions:** Not needed: the ratio of the numbers of turns has no unit, and the voltage comes out in volts.
**Substitution:** $U_2 = \dfrac{230\,\text{V} \cdot 60}{1200} = 11.5\,\text{V}$
**Answer:** $11.5\,\text{V}$, three significant figures like the voltage $230\,\text{V}$; the numbers of turns are exact numbers.
**Reasonableness:** The secondary coil has $20$ times fewer turns, so the voltage must be $20$ times smaller: $230\,\text{V} : 20 = 11.5\,\text{V}$. A small voltage like this suits a doorbell and is safe to touch.

## fy7-8-L1-02
**Given:** primary voltage $U_1 = 230\,\text{V}$, secondary voltage $U_2 = 8.0\,\text{V}$, number of turns of the secondary coil $N_2 = 40$, ideal transformer
**Find:** the number of turns $N_1$ of the primary coil
**Principle:** In an ideal transformer the same changing magnetic flux passes through both coils, so the same voltage is induced in every turn and the voltages of the coils are in the same ratio as the numbers of turns.
**Formula:** $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$, so $N_1 = \dfrac{N_2 U_1}{U_2}$
**Conversions:** Not needed: in the ratio of the voltages the volts cancel.
**Substitution:** $N_1 = \dfrac{40 \cdot 230\,\text{V}}{8.0\,\text{V}} = 1150$
**Answer:** $1150$ turns. The number of turns is a whole number, and the two significant figures of the voltage $8.0\,\text{V}$ are enough for this precision.
**Reasonableness:** The voltage falls by a factor of about $29$ ($230\,\text{V} : 8.0\,\text{V} \approx 29$), so the primary coil must have about $29$ times as many turns as the secondary coil: $29 \cdot 40 \approx 1150$.

## fy7-8-L1-03
**Given:** primary voltage $U_1 = 20\,\text{kV}$, secondary voltage $U_2 = 400\,\text{V}$, secondary current $I_2 = 250\,\text{A}$, ideal transformer
**Find:** the primary current $I_1$ in amperes
**Principle:** An ideal transformer does not consume energy, so power is conserved, $U_1 I_1 = U_2 I_2$. Therefore the currents are in inverse proportion to the voltages.
**Formula:** $\dfrac{U_1}{U_2} = \dfrac{I_2}{I_1}$, so $I_1 = \dfrac{I_2 U_2}{U_1}$
**Conversions:** $U_1 = 20\,\text{kV} = 20 \cdot 1000\,\text{V} = 20\,000\,\text{V}$, so that the voltages are in the same unit.
**Substitution:** $I_1 = \dfrac{250\,\text{A} \cdot 400\,\text{V}}{20\,000\,\text{V}} = 5.0\,\text{A}$
**Answer:** $5.0\,\text{A}$, two significant figures like the voltage $20\,\text{kV}$.
**Reasonableness:** Power is conserved: $20\,000\,\text{V} \cdot 5.0\,\text{A} = 100\,\text{kW}$ and $400\,\text{V} \cdot 250\,\text{A} = 100\,\text{kW}$. The primary current of a step-down transformer is smaller than the secondary current, as it should be.

## fy7-8-L1-04
**Given:** total resistance of the conductors $R = 2.5\,\Omega$, current $I = 120\,\text{A}$
**Find:** the power $P_\text{h}$ that becomes internal energy in the line, in kilowatts
**Principle:** In the resistance of the line the current changes electrical energy into internal energy. When the current and the resistance of the line are known, the power loss is obtained directly from the expression $P_\text{h} = R I^2$.
**Formula:** $P_\text{h} = R I^2$
**Conversions:** Finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P_\text{h} = 2.5\,\Omega \cdot (120\,\text{A})^2 = 2.5\,\Omega \cdot 14\,400\,\text{A}^2 = 36\,000\,\text{W} = 36\,\text{kW}$
**Answer:** $36\,\text{kW}$, two significant figures like the resistance $2.5\,\Omega$.
**Reasonableness:** Units: $\Omega \cdot \text{A}^2 = \tfrac{\text{V}}{\text{A}} \cdot \text{A}^2 = \text{V} \cdot \text{A} = \text{W}$. The loss corresponds to the power of about five electric stoves; in a distribution line such a power can be lost when the current is over a hundred amperes.

## fy7-8-L1-05
**Given:** transmission voltage $U = 400\,\text{kV}$, current $I = 800\,\text{A}$
**Find:** the transmitted power $P$ in megawatts
**Principle:** Electric power is the product of voltage and current. The power transmitted by a line is the product of the transmission voltage and the current of the line.
**Formula:** $P = U I$
**Conversions:** $U = 400\,\text{kV} = 400 \cdot 1000\,\text{V} = 400\,000\,\text{V}$. Finally $1\,\text{MW} = 1\,000\,000\,\text{W}$.
**Substitution:** $P = 400\,000\,\text{V} \cdot 800\,\text{A} = 320\,000\,000\,\text{W} = 320\,\text{MW}$
**Answer:** $320\,\text{MW}$, three significant figures like the given values.
**Reasonableness:** $320\,\text{MW}$ is of the order of magnitude of the power of a large power plant, and a line of the transmission grid transmits just such powers. The same power at $230\,\text{V}$ would require a current of over a million amperes.

## fy7-8-L2-01
**Given:** power $P = 50\,\text{MW}$, transmission voltage $U = 110\,\text{kV}$, resistance of the conductors $R = 4.0\,\Omega$
**Find:** the power $P_\text{h}$ that becomes internal energy in the line, in kilowatts
**Principle:** The line is heated by its current, and the power loss is $P_\text{h} = R I^2$. The current is obtained from the power and the transmission voltage, because $P = U I$. The transmission voltage is not across the resistance of the line, so the loss is not calculated with the expression $U^2 : R$.
**Formula:** $P = U I$, so $I = \dfrac{P}{U}$, and $P_\text{h} = R I^2$
**Conversions:** $P = 50\,\text{MW} = 50 \cdot 10^{6}\,\text{W}$ and $U = 110\,\text{kV} = 110 \cdot 10^{3}\,\text{V}$. Finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $I = \dfrac{50 \cdot 10^{6}\,\text{W}}{110 \cdot 10^{3}\,\text{V}} = 454.5\,\text{A}$ and $P_\text{h} = 4.0\,\Omega \cdot (454.5\,\text{A})^2 = 826\,400\,\text{W} = 826.4\,\text{kW}$
**Answer:** $8.3 \cdot 10^{2}\,\text{kW}$ or about $830\,\text{kW}$, two significant figures like the power $50\,\text{MW}$ and the resistance $4.0\,\Omega$.
**Reasonableness:** The loss is $0.83\,\text{MW} : 50\,\text{MW} \approx 1.7\,\%$ of the transmitted power, of the same order of magnitude as the losses of the transmission grid, about $2\,\%$. So the loss is small but not negligible.

## fy7-8-L2-02
**Given:** charging voltage $U_2 = 5.0\,\text{V}$, charging current $I_2 = 2.0\,\text{A}$, mains voltage $U_1 = 230\,\text{V}$, ideal transformer
**Find:** the primary current $I_1$ in milliamperes
**Principle:** An ideal transformer does not consume energy, so the power coming into the primary coil is the same as the power going to the phone, $U_1 I_1 = U_2 I_2$.
**Formula:** $U_1 I_1 = U_2 I_2$, so $I_1 = \dfrac{U_2 I_2}{U_1}$
**Conversions:** Finally $1\,\text{A} = 1000\,\text{mA}$.
**Substitution:** $I_1 = \dfrac{5.0\,\text{V} \cdot 2.0\,\text{A}}{230\,\text{V}} = \dfrac{10\,\text{W}}{230\,\text{V}} = 0.04348\,\text{A} = 43.48\,\text{mA}$
**Answer:** $43\,\text{mA}$, two significant figures like the voltage $5.0\,\text{V}$ and the current $2.0\,\text{A}$.
**Reasonableness:** The voltage falls by a factor of $46$, so the primary current must be $46$ times smaller than the charging current: $2.0\,\text{A} : 46 \approx 0.043\,\text{A}$. A real charger takes slightly more, because some of the energy becomes internal energy in the charger.

## fy7-8-L2-03
**Given:** power $P = 100\,\text{MW}$, transmission voltage $U = 220\,\text{kV}$, resistance of the conductors $R = 4.8\,\Omega$
**Find:** the share of the power loss $P_\text{h} : P$ as a percentage
**Principle:** The line is heated by the current, and the power loss is $P_\text{h} = R I^2$. The current is obtained from the transmitted power and the transmission voltage, $P = U I$. Finally the power loss is compared with the transmitted power.
**Formula:** $I = \dfrac{P}{U}$, $P_\text{h} = R I^2$ and the share $\dfrac{P_\text{h}}{P}$
**Conversions:** $P = 100\,\text{MW} = 100 \cdot 10^{6}\,\text{W}$ and $U = 220\,\text{kV} = 220 \cdot 10^{3}\,\text{V}$.
**Substitution:** $I = \dfrac{100 \cdot 10^{6}\,\text{W}}{220 \cdot 10^{3}\,\text{V}} = 454.5\,\text{A}$, $P_\text{h} = 4.8\,\Omega \cdot (454.5\,\text{A})^2 = 0.9917 \cdot 10^{6}\,\text{W}$ and $\dfrac{P_\text{h}}{P} = \dfrac{0.9917 \cdot 10^{6}\,\text{W}}{100 \cdot 10^{6}\,\text{W}} = 0.009917 = 0.9917\,\%$
**Answer:** $0.99\,\%$, two significant figures like the resistance $4.8\,\Omega$.
**Reasonableness:** The loss is about $1\,\text{MW}$ in the transmission of a hundred megawatts, smaller than the average share of loss of the transmission grid, about $2\,\%$. If the same power were transmitted at $110\,\text{kV}$, the share would be four times as large, about $4\,\%$.

## fy7-8-L2-04
**Given:** the curve of the graph showing the power loss $P_\text{h}$ as a function of the current $I$
**Find:** the resistance $R$ of the wire in ohms
**Principle:** The power that becomes internal energy in the wire is $P_\text{h} = R I^2$, so the power loss grows with the square of the current and the graph is a parabola starting from the origin. When one point is read from the curve, the resistance can be solved. The fitted curve evens out the random errors of the individual measurements, so the value is read from the curve and not from an individual point.
**Reading the graph:** The curve passes through the grid point ($5.0\,\text{A}$; $20\,\text{W}$): at the current $5.0\,\text{A}$ the power loss of the fitted curve is $20\,\text{W}$. The measurement point $20.1\,\text{W}$ is close to the curve.
**Formula:** $P_\text{h} = R I^2$, so $R = \dfrac{P_\text{h}}{I^2}$
**Conversions:** Not needed: the power is in watts and the current in amperes, and $\tfrac{\text{W}}{\text{A}^2} = \tfrac{\text{V}}{\text{A}} = \Omega$.
**Substitution:** $R = \dfrac{20\,\text{W}}{(5.0\,\text{A})^2} = \dfrac{20\,\text{W}}{25\,\text{A}^2} = 0.80\,\Omega$
**Answer:** $0.80\,\Omega$, two significant figures like the current $5.0\,\text{A}$ read from the graph.
**Reasonableness:** A check with another point of the curve: at the current $2.5\,\text{A}$ the curve gives $0.80\,\Omega \cdot (2.5\,\text{A})^2 = 5.0\,\text{W}$, which fits between the measurement points $3.1\,\text{W}$ ($2.0\,\text{A}$) and $7.4\,\text{W}$ ($3.0\,\text{A}$). A resistance of less than an ohm is plausible for a few metres of resistance wire.

## fy7-8-L3-01
**Given:** power of the generator $P = 150\,\text{MW}$ and voltage $20\,\text{kV}$, an ideal transformer raises the voltage to $U = 400\,\text{kV}$, resistance of the conductors $R = 8.0\,\Omega$
**Find:** the share of the power loss $P_\text{h} : P$ as a percentage
**Principle:** An ideal transformer does not consume energy, so the whole power $150\,\text{MW}$ goes into the line, but at the voltage $400\,\text{kV}$. The current of the line is determined by the transmission voltage, not by the voltage of the generator. This current heats the line at the rate $P_\text{h} = R I^2$.
**Formula:** $I = \dfrac{P}{U}$, $P_\text{h} = R I^2$ and the share $\dfrac{P_\text{h}}{P}$
**Conversions:** $P = 150\,\text{MW} = 150 \cdot 10^{6}\,\text{W}$ and $U = 400\,\text{kV} = 400 \cdot 10^{3}\,\text{V}$.
**Substitution:** $I = \dfrac{150 \cdot 10^{6}\,\text{W}}{400 \cdot 10^{3}\,\text{V}} = 375\,\text{A}$, $P_\text{h} = 8.0\,\Omega \cdot (375\,\text{A})^2 = 1.125 \cdot 10^{6}\,\text{W}$ and $\dfrac{P_\text{h}}{P} = \dfrac{1.125 \cdot 10^{6}\,\text{W}}{150 \cdot 10^{6}\,\text{W}} = 0.0075 = 0.75\,\%$
**Answer:** $0.75\,\%$, two significant figures like the resistance $8.0\,\Omega$.
**Reasonableness:** Without the transformer the current would be $150\,\text{MW} : 20\,\text{kV} = 7500\,\text{A}$, and the loss $8.0\,\Omega \cdot (7500\,\text{A})^2 = 450\,\text{MW}$ would be greater than the whole power, so the transmission would not be possible at all. Thanks to the transformer the loss is under one per cent.

## fy7-8-L3-02
**Given:** transmission voltage $U = 400\,\text{kV}$, transmitted power $P = 400\,\text{MW}$, loss at most $1.0\,\%$, that is $P_\text{h} \le 0.010\,P$
**Find:** the greatest permitted resistance $R$ of the conductors in ohms
**Principle:** The power loss is $P_\text{h} = R I^2$, and the current is $I = P : U$. Combining these gives $P_\text{h} = R P^2 : U^2$. When the loss may be at most a given share of the power, the resistance may be at most the value for which the loss is exactly this share.
**Formula:** $\dfrac{R P^2}{U^2} = 0.010\,P$, so $R = \dfrac{0.010\,U^2}{P}$
**Conversions:** $U = 400\,\text{kV} = 400 \cdot 10^{3}\,\text{V}$ and $P = 400\,\text{MW} = 400 \cdot 10^{6}\,\text{W}$.
**Substitution:** $R = \dfrac{0.010 \cdot (400 \cdot 10^{3}\,\text{V})^2}{400 \cdot 10^{6}\,\text{W}} = \dfrac{1.6 \cdot 10^{9}\,\text{V}^2}{4.0 \cdot 10^{8}\,\text{W}} = 4.0\,\Omega$
**Answer:** at most $4.0\,\Omega$, two significant figures like the share $1.0\,\%$.
**Reasonableness:** A check: the current is $400\,\text{MW} : 400\,\text{kV} = 1000\,\text{A}$, and the loss is $4.0\,\Omega \cdot (1000\,\text{A})^2 = 4.0\,\text{MW}$, that is $1.0\,\%$ of the power. Units: $\tfrac{\text{V}^2}{\text{W}} = \tfrac{\text{V}^2}{\text{V} \cdot \text{A}} = \Omega$.

## fy7-8-L3-03
**Given:** original transmission voltage $U_1 = 220\,\text{kV}$, new transmission voltage $U_2 = 400\,\text{kV}$, the resistance $R$ and the share of the loss stay the same
**Find:** how many times the power $P_2 : P_1$ can be transmitted
**Principle:** The power loss is $P_\text{h} = R I^2$ and the current $I = P : U$, so the share of the loss is $P_\text{h} : P = R P : U^2$. When $R$ and the share stay the same, the power $P$ is proportional to the square of the voltage $U^2$.
**Formula:** $\dfrac{R P_1}{U_1^2} = \dfrac{R P_2}{U_2^2}$, so $\dfrac{P_2}{P_1} = \dfrac{U_2^2}{U_1^2}$
**Conversions:** Not needed: in the ratio of the voltages the kilovolts cancel.
**Substitution:** $\dfrac{P_2}{P_1} = \dfrac{(400\,\text{kV})^2}{(220\,\text{kV})^2} = (1.818)^2 = 3.306$
**Answer:** about $3.3$ times the power, two significant figures like the voltage $220\,\text{kV}$.
**Reasonableness:** The voltage increases to somewhat less than double, so the power can increase to somewhat less than four times. For example, the powers $100\,\text{MW}$ and $331\,\text{MW}$ give the currents $455\,\text{A}$ and $826\,\text{A}$, and the share of the losses $R I : U$ is the same in both.
