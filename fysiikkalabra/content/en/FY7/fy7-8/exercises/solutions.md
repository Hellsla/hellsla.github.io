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

## fy7-8-L1-06
**Find:** why a transformer gives no voltage in the secondary coil when the primary coil is connected to a direct voltage.
**Principle:** A voltage is induced in the secondary coil only if the magnetic flux through the coil changes (the law of induction). Direct current is constant, so the magnetic flux it produces in the iron core is constant, even though the current flows and the field exists.
**Model answer:** The magnetic flux produced by the direct current does not change, so no voltage is induced in the secondary coil. The current flows in the primary coil and the iron core is magnetized, but only a changing flux induces a voltage. Alternating current changes the flux continuously, which is why a transformer works with alternating voltage. A transformer can both raise and lower a voltage, and this depends on the numbers of turns, not on the type of current.

## fy7-8-L1-07
**Given:** the power loss at first $P_\text{h,1} = 840\,\text{kW}$, the transmission voltage is doubled, $U_2 = 2U_1$, the power $P$ and the resistance $R$ stay the same
**Find:** the new power loss $P_\text{h,2}$ in kilowatts
**Principle:** The current of the line is $I = P : U$, and the power loss is $P_\text{h} = R I^2 = R P^2 : U^2$. When $P$ and $R$ stay the same, the power loss is inversely proportional to the square of the voltage. Doubling the voltage halves the current, and the loss depends on the square of the current.
**Formula:** $P_\text{h} = \dfrac{R P^2}{U^2}$, so $\dfrac{P_\text{h,2}}{P_\text{h,1}} = \dfrac{U_1^2}{U_2^2}$ and $P_\text{h,2} = P_\text{h,1} \cdot \dfrac{U_1^2}{U_2^2}$
**Conversions:** Not needed: the power loss is in kilowatts, and the ratio of the voltages has no unit.
**Substitution:** $P_\text{h,2} = 840\,\text{kW} \cdot \dfrac{U_1^2}{(2U_1)^2} = 840\,\text{kW} \cdot \dfrac{1}{4} = 210\,\text{kW}$
**Answer:** $210\,\text{kW}$, two significant figures like the power loss $840\,\text{kW}$.
**Reasonableness:** The current is halved, so the square of the current is a quarter: $840\,\text{kW} : 4 = 210\,\text{kW}$. The loss decreases, but not to a half, because it depends on the square of the current.

## fy7-8-L1-08
**Given:** primary power $P_1 = 80\,\text{W}$, secondary power $P_2 = 72\,\text{W}$
**Find:** the efficiency $\eta$ as a percentage
**Principle:** The efficiency is the share of the power received by the load in the power taken from the mains. In a real transformer part of the primary power becomes internal energy in the iron core and the coils, so $\eta < 1$.
**Formula:** $\eta = \dfrac{P_2}{P_1}$
**Conversions:** Not needed: the powers are in the same unit, so the ratio calculated in watts has no unit. Finally $1 = 100\,\%$.
**Substitution:** $\eta = \dfrac{72\,\text{W}}{80\,\text{W}} = 0.90 = 90\,\%$
**Answer:** $90\,\%$, two significant figures like the powers $80\,\text{W}$ and $72\,\text{W}$.
**Reasonableness:** The power loss is $80\,\text{W} - 72\,\text{W} = 8\,\text{W}$, and $8\,\text{W} : 80\,\text{W} = 10\,\%$, so $100\,\% - 10\,\% = 90\,\%$. The efficiency of small transformers is usually in this range.

## fy7-8-L2-05
**Given:** primary voltage $U_1 = 6.00\,\text{V}$, the measurement points of the table $N_2 \to U_2$: ${100 \to 1.22\,\text{V}}$, ${200 \to 2.53\,\text{V}}$, ${300 \to 3.70\,\text{V}}$, ${400 \to 4.93\,\text{V}}$, ${600 \to 7.41\,\text{V}}$ and ${800 \to 9.88\,\text{V}}$, ideal transformer
**Find:** the number of turns $N_1$ of the primary coil
**Principle:** In an ideal transformer $U_2 : U_1 = N_2 : N_1$, so $U_2 = \dfrac{U_1}{N_1} \cdot N_2$. When $U_1$ is constant, $U_2$ is directly proportional to the number of turns $N_2$, and the slope $k = U_1 : N_1$ contains the unknown $N_1$. The measurements have a little scatter, so the slope is determined from the whole data and not from a single point.
**Reading the graph:** The points of the table lie on a line through the origin, and the ratios $U_2 : N_2$ are $0.01220$, $0.01265$, $0.01233$, $0.01233$, $0.01235$ and $0.01235\,\tfrac{\text{V}}{\text{turn}}$. The slope of the line fitted through the origin is $k = 0.012354\,\tfrac{\text{V}}{\text{turn}}$.
**Formula:** $k = \dfrac{U_1}{N_1}$, so $N_1 = \dfrac{U_1}{k}$
**Conversions:** Not needed: the voltage is in volts, and $k$ is in volts per turn.
**Substitution:** $N_1 = \dfrac{6.00\,\text{V}}{0.012354\,\text{V/turn}} = 485.7$
**Answer:** $486$ turns, three significant figures like the voltages. Because of the scatter, an answer of $485$–$487$ is good.
**Reasonableness:** From the greatest number of turns we get $N_1 = 6.00\,\text{V} \cdot 800 : 9.88\,\text{V} = 485.8$, so the result is the same. A voltage of $6.00\,\text{V}$ and a number of turns $N_2 = 486$ would give $U_2 = 6.00\,\text{V}$, and a smaller $N_2$ in the table gives a smaller voltage, as it should.

## fy7-8-L2-06
**Given:** $U_1 = 230\,\text{V}$ and the rows of the table $(I_2;\ U_2;\ I_1)$: $(0.20\,\text{A};\ 12.4\,\text{V};\ 0.020\,\text{A})$, $(0.60\,\text{A};\ 12.2\,\text{V};\ 0.042\,\text{A})$, $(1.00\,\text{A};\ 12.0\,\text{V};\ 0.063\,\text{A})$, $(1.50\,\text{A};\ 11.8\,\text{V};\ 0.089\,\text{A})$ and $(2.00\,\text{A};\ 11.5\,\text{V};\ 0.114\,\text{A})$
**Find:** the efficiency $\eta$ as a percentage on the row where $I_2 = 2.00\,\text{A}$; in addition the load of the greatest efficiency and an explanation
**Principle:** Electric power is the product of voltage and current, $P = U I$, and the efficiency is the share of the secondary power in the primary power, $\eta = P_2 : P_1$. In a transformer part of the primary power becomes internal energy, so $\eta < 1$.
**Formula:** $P_1 = U_1 I_1$ (assumption: the current and the voltage are in the same phase), $P_2 = U_2 I_2$ and $\eta = \dfrac{P_2}{P_1}$
**Conversions:** Not needed: the voltages are in volts and the currents in amperes, so the powers come out in watts.
**Substitution:** On the rows $\eta = 0.54$, $0.76$, $0.83$, $0.86$ and $0.88$ (powers $P_1 = 4.6$; $9.66$; $14.49$; $20.47$ and $26.22\,\text{W}$, $P_2 = 2.48$; $7.32$; $12.0$; $17.7$ and $23.0\,\text{W}$). On the last row $P_1 = 230\,\text{V} \cdot 0.114\,\text{A} = 26.22\,\text{W}$, $P_2 = 11.5\,\text{V} \cdot 2.00\,\text{A} = 23.0\,\text{W}$ and $\eta = \dfrac{23.0\,\text{W}}{26.22\,\text{W}} = 0.877 = 87.7\,\%$
**Answer:** $87.7\,\%$, three significant figures like the values $0.114\,\text{A}$, $11.5\,\text{V}$ and $2.00\,\text{A}$. The efficiency is greatest at the greatest load and lowest at the smallest load, only about $54\,\%$. The reason is that the power loss is almost constant, about $2\text{–}3\,\text{W}$ (the differences $P_1 - P_2$ of the powers are $2.1$; $2.3$; $2.5$; $2.8$ and $3.2\,\text{W}$), while the secondary power increases. At a small load an almost constant loss is a large part of the primary power, at a large load a small part.
**Reasonableness:** On the last row the loss is $26.22\,\text{W} - 23.0\,\text{W} = 3.2\,\text{W}$, which is $3.22\,\text{W} : 26.22\,\text{W} = 12.3\,\%$ of the primary power, and $100\,\% - 12.3\,\% = 87.7\,\%$. The secondary voltage falls as the load increases ($12.4\,\text{V} \to 11.5\,\text{V}$), which shows the loss caused by the resistance of the coils.

## fy7-8-L2-07
**Given:** primary voltage $U_1 = 230\,\text{V}$, secondary voltage $U_2 = 2300\,\text{V}$, primary current $I_1 = 2.0\,\text{A}$, ideal transformer
**Find:** a) what is wrong in the student's reasoning, b) the secondary current $I_2$ in amperes
**Principle:** An ideal transformer neither consumes nor produces energy, so power is conserved, $U_1 I_1 = U_2 I_2$. The student's mistake is to claim that a transformer does not change the current: when the voltage becomes ten times as large, the current must become a tenth so that the power stays the same. The student's result $4600\,\text{W}$ is ten times the primary power $460\,\text{W}$, that is, the transformer would have produced energy out of nothing.
**Formula:** $U_1 I_1 = U_2 I_2$, so $I_2 = \dfrac{U_1 I_1}{U_2}$
**Conversions:** Not needed: the voltages are in volts and the current in amperes.
**Substitution:** $I_2 = \dfrac{230\,\text{V} \cdot 2.0\,\text{A}}{2300\,\text{V}} = \dfrac{460\,\text{W}}{2300\,\text{V}} = 0.20\,\text{A}$
**Answer:** $0.20\,\text{A}$, two significant figures like the primary current $2.0\,\text{A}$.
**Reasonableness:** The power on the secondary side is $2300\,\text{V} \cdot 0.20\,\text{A} = 460\,\text{W}$, the same as on the primary side, $230\,\text{V} \cdot 2.0\,\text{A} = 460\,\text{W}$. The voltage is ten times as large and the current a tenth, as it should be in an ideal transformer.

## fy7-8-L3-04
**Given:** constant power $P = 200\,\text{MW}$, distance $150\,\text{km}$, total resistance of the conductors $0.040\,\Omega$ per kilometre of line, time $t = 8760\,\text{h}$, voltages $U_\text{A} = 220\,\text{kV}$ and $U_\text{B} = 400\,\text{kV}$, price of electricity $50\,\text{€/MWh}$
**Find:** the yearly saving of option B in the value of the lost energy in millions of euros, and the justification
**Principle:** The current of the line is determined by the transmission voltage, $I = P : U$, and the power that becomes internal energy in the conductors is $P_\text{h} = R I^2$. The same power flows with a smaller current at a higher voltage, so the loss is smaller. Because the power is constant, the lost energy is the power loss multiplied by the time, $E = P_\text{h} t$, and the saving is the difference of the energies multiplied by the price.
**Formula:** $R = 0.040\,\tfrac{\Omega}{\text{km}} \cdot s$, $I = \dfrac{P}{U}$, $P_\text{h} = R I^2$, $E = P_\text{h} t$ and

$$\text{saving} = (E_\text{A} - E_\text{B}) \cdot \text{price}$$
**Conversions:** $P = 200\,\text{MW} = 200 \cdot 10^{6}\,\text{W}$, $U_\text{A} = 220 \cdot 10^{3}\,\text{V}$ and $U_\text{B} = 400 \cdot 10^{3}\,\text{V}$. The power loss is finally converted to megawatts, $1\,\text{MW} = 10^{6}\,\text{W}$.
**Substitution:** a) $R = 0.040\,\tfrac{\Omega}{\text{km}} \cdot 150\,\text{km} = 6.0\,\Omega$, $I_\text{A} = \dfrac{200 \cdot 10^{6}\,\text{W}}{220 \cdot 10^{3}\,\text{V}} = 909.1\,\text{A}$ and $I_\text{B} = \dfrac{200 \cdot 10^{6}\,\text{W}}{400 \cdot 10^{3}\,\text{V}} = 500\,\text{A}$. b) $P_\text{h,A} = 6.0\,\Omega \cdot (909.1\,\text{A})^2 = 4.959\,\text{MW}$ and $P_\text{h,B} = 6.0\,\Omega \cdot (500\,\text{A})^2 = 1.500\,\text{MW}$, so $E_\text{A} = 4.959\,\text{MW} \cdot 8760\,\text{h} = 43\,440\,\text{MWh}$ and $E_\text{B} = 1.500\,\text{MW} \cdot 8760\,\text{h} = 13\,140\,\text{MWh}$. c) Saving $= (43\,440\,\text{MWh} - 13\,140\,\text{MWh}) \cdot 50\,\tfrac{\text{€}}{\text{MWh}} = 30\,300\,\text{MWh} \cdot 50\,\tfrac{\text{€}}{\text{MWh}} = 1.515 \cdot 10^{6}\,\text{€}$
**Answer:** about $1.5\,\text{million €}$ a year, two significant figures like the power $200\,\text{MW}$. Justification: the transmitted power is the same, but at a higher voltage the current is smaller ($500\,\text{A}$ and not $909\,\text{A}$). The power loss depends on the square of the current, so it falls to about a third even though the resistance is the same. The high voltage of the transmission grid is therefore economical.
**Reasonableness:** The ratio of the voltages is $400 : 220 = 1.82$, and the ratio of the losses is its square, $3.3$: $4.959\,\text{MW} : 1.500\,\text{MW} = 3.3$. The loss in option B is $1.5\,\text{MW} : 200\,\text{MW} = 0.75\,\%$ and in option A $2.5\,\%$, of the order of magnitude of the transmission grid.

## fy7-8-L3-05
**Given:** the powers of the table $(P_\text{out};\ P_\text{in})$: $(0.0\,\text{kW};\ 0.6\,\text{kW})$, $(10.0\,\text{kW};\ 10.6\,\text{kW})$, $(20.0\,\text{kW};\ 20.7\,\text{kW})$, $(40.0\,\text{kW};\ 40.9\,\text{kW})$, $(60.0\,\text{kW};\ 61.3\,\text{kW})$ and $(80.0\,\text{kW};\ 81.9\,\text{kW})$, model $P_\text{h} = P_0 + a P_\text{out}^2$
**Find:** the value of the output power $P_\text{out}$ in kilowatts at which the efficiency is greatest
**Principle:** The power loss is the difference of the input and output powers. With no load the transformer still takes a power $P_0$ (heating of the iron core), and under load an additional $R I^2$ becomes internal energy in the coils. The voltage is constant, so the secondary current $I = P_\text{out} : U$ is proportional to the output power and $R I^2 = \dfrac{R}{U^2} P_\text{out}^2 = a P_\text{out}^2$. The efficiency is greatest when the share of the loss in the output power is smallest. The condition given in the task (the constant loss and the load-dependent loss are equal) is obtained from this by differentiation, but it is not derived here.
**Formula:** $P_\text{h} = P_\text{in} - P_\text{out}$, $\eta = \dfrac{P_\text{out}}{P_\text{in}}$, $P_0 = P_\text{h}(0)$, $a = \dfrac{P_\text{h} - P_0}{P_\text{out}^2}$ and from the condition $P_0 = a P_\text{out}^2$ we get $P_\text{out} = \sqrt{\dfrac{P_0}{a}}$
**Conversions:** Not needed: all the powers are in kilowatts, and $a$ gets the unit $\text{kW}^{-1}$.
**Substitution:** a) The power losses are $0.6$; $0.6$; $0.7$; $0.9$; $1.3$ and $1.9\,\text{kW}$ and the efficiencies on the rows $10\text{–}80\,\text{kW}$ are $94.3$; $96.6$; $97.8$; $97.9$ and $97.7\,\%$. b) At no load $P_0 = 0.6\,\text{kW}$. The greatest load has the smallest relative reading error, so $a = \dfrac{1.9\,\text{kW} - 0.6\,\text{kW}}{(80.0\,\text{kW})^2} = 2.03 \cdot 10^{-4}\,\text{kW}^{-1}$. c) $P_\text{out} = \sqrt{\dfrac{0.6\,\text{kW}}{2.03 \cdot 10^{-4}\,\text{kW}^{-1}}} = \sqrt{2954\,\text{kW}^2} = 54.35\,\text{kW}$
**Answer:** about $54\,\text{kW}$, two significant figures, because the difference of the losses $1.9\,\text{kW} - 0.6\,\text{kW} = 1.3\,\text{kW}$ is known to two significant figures. The $a$ determined from the rows $20$–$60\,\text{kW}$ would give values of $49$–$57\,\text{kW}$, so the result is imprecise.
**Reasonableness:** In the table the efficiency is greatest on the row $60\,\text{kW}$ ($97.9\,\%$), close to the result $54\,\text{kW}$. At the result the loss according to the model is $0.6\,\text{kW} + 2.03 \cdot 10^{-4}\,\text{kW}^{-1} \cdot (54.35\,\text{kW})^2 = 1.2\,\text{kW}$, and the efficiency is $\dfrac{54.35}{54.35 + 1.2} = 97.8\,\%$. The two parts of the loss are here $0.6\,\text{kW}$ each.
