## fy6-6-L1-01
**Given:** voltage $U = 5.0\,\text{V}$, current $I = 2.4\,\text{A}$
**Find:** the charging power $P$ in watts
**Principle:** Electric power is the product of voltage and current: the voltage tells how many joules one coulomb gives up, and the current how many coulombs pass per second. The formula holds for any device, including a charger.
**Formula:** $P = UI$
**Conversions:** Not needed: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Substitution:** $P = 5.0\,\text{V} \cdot 2.4\,\text{A} = 12\,\text{W}$
**Answer:** $12\,\text{W}$, two significant figures like the voltage and the current.
**Reasonableness:** The estimate $5\,\text{V} \cdot 2\,\text{A} = 10\,\text{W}$ is close to the result. The powers of fast phone chargers are typically between $10\,\text{W}$ and a few tens of watts, so the result is plausible.

## fy6-6-L1-02
**Given:** resistance $R = 47\,\Omega$, current $I = 0.20\,\text{A}$
**Find:** the power $P$ transformed into internal energy in the resistor, in watts
**Principle:** Joule's law: the power transformed into internal energy in a resistor is the resistance times the square of the current. The current is known, so this form fits directly.
**Formula:** $P = RI^2$
**Conversions:** Not needed: $\Omega \cdot \text{A}^2 = \text{V} \cdot \text{A} = \text{W}$.
**Substitution:** $P = 47\,\Omega \cdot (0.20\,\text{A})^2 = 47\,\Omega \cdot 0.040\,\text{A}^2 = 1.88\,\text{W}$
**Answer:** $1.9\,\text{W}$, two significant figures like the resistance and the current.
**Reasonableness:** The voltage of the resistor is $47\,\Omega \cdot 0.20\,\text{A} = 9.4\,\text{V}$, and $9.4\,\text{V} \cdot 0.20\,\text{A} = 1.88\,\text{W}$ gives the same power. An ordinary small resistor withstands only $0.25\,\text{W}$, so a power resistor is needed here.

## fy6-6-L1-03
**Given:** resistance $R = 26.5\,\Omega$, voltage $U = 230\,\text{V}$
**Find:** the power $P$ of the kettle in kilowatts
**Principle:** The full mains voltage is across the heating resistor, so it is best to use Joule's law in the form written with the voltage, $P = U^2 : R$.
**Formula:** $P = \dfrac{U^2}{R}$
**Conversions:** The result in watts is converted: $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P = \dfrac{(230\,\text{V})^2}{26.5\,\Omega} = \dfrac{52\,900\,\text{V}^2}{26.5\,\Omega} = 1996\,\text{W} = 1.996\,\text{kW}$
**Answer:** $2.00\,\text{kW}$, three significant figures like the resistance and the mains voltage $230\,\text{V}$ (which is assumed to be given to three figures).
**Reasonableness:** The power of a household kettle is typically of the order of $2\,\text{kW}$. The current is $230\,\text{V} : 26.5\,\Omega \approx 8.7\,\text{A}$, which is within the current limit of an ordinary socket.

## fy6-6-L1-04
**Given:** power $P = 9.0\,\text{W}$, time $t = 2.0\,\text{h}$
**Find:** the electrical energy $E$ transformed in the lamp, in kilojoules
**Principle:** Power tells how many joules of energy are transformed per second. When the power is constant, the energy is the power times the time.
**Formula:** $E = Pt$
**Conversions:** $t = 2.0\,\text{h} = 2.0 \cdot 3600\,\text{s} = 7200\,\text{s}$ and finally $1\,\text{kJ} = 1000\,\text{J}$.
**Substitution:** $E = 9.0\,\text{W} \cdot 7200\,\text{s} = 64\,800\,\text{J} = 64.8\,\text{kJ}$
**Answer:** $65\,\text{kJ}$, two significant figures like the power and the time.
**Reasonableness:** In one hour the lamp uses $9\,\text{W} \cdot 3600\,\text{s} \approx 32\,\text{kJ}$, so in two hours about twice that. The unit $\text{W} \cdot \text{s} = \text{J}$ is correct.

## fy6-6-L1-05
**Given:** points of the graph: power $P$ as a function of current $I$
**Find:** the resistance $R$ of the resistor in ohms
**Principle:** By Joule's law the power of a resistor is $P = RI^2$. When the current and power of one point are known, the resistance can be solved.
**Reading the graph:** We read the point where the current is largest and easiest to read: when $I = 2.0\,\text{A}$, the point is on the grid line $P = 20\,\text{W}$. The point $(1.0\,\text{A};\ 5.0\,\text{W})$ is also on a grid line and gives the same result.
**Formula:** $P = RI^2$, so $R = \dfrac{P}{I^2}$
**Conversions:** Not needed: $\text{W} : \text{A}^2 = \text{V} : \text{A} = \Omega$.
**Substitution:** $R = \dfrac{20\,\text{W}}{(2.0\,\text{A})^2} = \dfrac{20\,\text{W}}{4.0\,\text{A}^2} = 5.0\,\Omega$
**Answer:** $5.0\,\Omega$, two significant figures, because the values are read from the graph to two figures.
**Reasonableness:** From the point $(1.0\,\text{A};\ 5.0\,\text{W})$ we get $5.0\,\text{W} : (1.0\,\text{A})^2 = 5.0\,\Omega$, the same result. When the current doubles, the power becomes four times larger, from $5\,\text{W}$ to $20\,\text{W}$, as Joule's law requires.

## fy6-6-L2-01
**Given:** power $P = 1.8\,\text{kW}$, voltage $U = 230\,\text{V}$
**Find:** the current $I$ through the dryer, in amperes
**Principle:** Electric power is the product of voltage and current. When the power and the voltage are known, the current is solved from the formula for power.
**Formula:** $P = UI$, so $I = \dfrac{P}{U}$
**Conversions:** $P = 1.8\,\text{kW} = 1.8 \cdot 1000\,\text{W} = 1800\,\text{W}$
**Substitution:** $I = \dfrac{1800\,\text{W}}{230\,\text{V}} = 7.83\,\text{A}$
**Answer:** $7.8\,\text{A}$, two significant figures like the power $1.8\,\text{kW}$.
**Reasonableness:** The estimate $2000\,\text{W} : 250\,\text{V} = 8\,\text{A}$ is close to the result. The current is smaller than the current limit of an ordinary socket. Without converting the kilowatts, the current would be $0.008\,\text{A}$, which is far too small for such a powerful device.

## fy6-6-L2-02
**Given:** $R_1 = 10\,\Omega$ and $R_2 = 20\,\Omega$ in series, voltage of the source $U = 12\,\text{V}$
**Find:** the power $P_2$ of the resistor $R_2$ in watts
**Principle:** In a series connection the same current flows through both resistors, and it is determined by the total resistance $R_1 + R_2$. When the current is known, the power of a resistor is given by Joule's law $P = RI^2$.
**Formula:** $I = \dfrac{U}{R_1 + R_2}$ and $P_2 = R_2 I^2$, so $P_2 = R_2 \left(\dfrac{U}{R_1 + R_2}\right)^2$
**Conversions:** Not needed: $\text{V} : \Omega = \text{A}$ and $\Omega \cdot \text{A}^2 = \text{W}$.
**Substitution:** $I = \dfrac{12\,\text{V}}{10\,\Omega + 20\,\Omega} = 0.40\,\text{A}$ and $P_2 = 20\,\Omega \cdot (0.40\,\text{A})^2 = 3.2\,\text{W}$
**Answer:** $3.2\,\text{W}$, two significant figures like the resistances and the voltage.
**Reasonableness:** The power of the resistor $R_1$ is $10\,\Omega \cdot (0.40\,\text{A})^2 = 1.6\,\text{W}$, half as large, as it should be in a series connection. The powers add up to $4.8\,\text{W}$, and the power of the source is $12\,\text{V} \cdot 0.40\,\text{A} = 4.8\,\text{W}$.

## fy6-6-L2-03
**Given:** resistance $R = 1.0\,\text{k}\Omega$, maximum permitted power $P = 0.25\,\text{W}$
**Find:** the maximum permitted voltage $U$ in volts
**Principle:** By Joule's law the power of a resistor grows as the square of the voltage, $P = U^2 : R$. The maximum permitted voltage is the one at which the power is exactly the maximum permitted power.
**Formula:** $P = \dfrac{U^2}{R}$, so $U = \sqrt{PR}$
**Conversions:** $R = 1.0\,\text{k}\Omega = 1.0 \cdot 1000\,\Omega = 1000\,\Omega$
**Substitution:** $U = \sqrt{0.25\,\text{W} \cdot 1000\,\Omega} = \sqrt{250\,\text{V}^2} = 15.8\,\text{V}$
**Answer:** $16\,\text{V}$, two significant figures like the power and the resistance.
**Reasonableness:** Check: $(15.8\,\text{V})^2 : 1000\,\Omega = 0.25\,\text{W}$. The unit $\sqrt{\text{W} \cdot \Omega} = \sqrt{\text{V}^2} = \text{V}$ is correct. In an ordinary $5\,\text{V}$ or $9\,\text{V}$ circuit the resistor is therefore in the safe range, even if the whole voltage were across the resistor.

## fy6-6-L2-04
**Given:** power $P = 200\,\text{W}$, mass of the water $m = 0.80\,\text{kg}$, time $t = 5.0\,\text{min}$, $c = 4190\,\tfrac{\text{J}}{\text{kg} \cdot \text{K}}$
**Find:** the rise in the temperature of the water $\Delta T$ in kelvins
**Principle:** In the heater the electrical energy $E = Pt$ is transformed. Since all the energy heats the water and the state of matter does not change, the energy equals the heat $cm\Delta T$ received by the water (chapter *Heating and cooling of matter*).
**Formula:** $Pt = cm\Delta T$, so $\Delta T = \dfrac{Pt}{cm}$
**Conversions:** $t = 5.0\,\text{min} = 5.0 \cdot 60\,\text{s} = 300\,\text{s}$
**Substitution:** $\Delta T = \dfrac{200\,\text{W} \cdot 300\,\text{s}}{4190\,\tfrac{\text{J}}{\text{kg} \cdot \text{K}} \cdot 0.80\,\text{kg}} = \dfrac{60\,000\,\text{J}}{3352\,\tfrac{\text{J}}{\text{K}}} = 17.9\,\text{K}$
**Answer:** $18\,\text{K}$, two significant figures like the mass and the time.
**Reasonableness:** Raising the temperature of $0.80\,\text{kg}$ of water by one degree takes about $3.4\,\text{kJ}$, and the heater gives $60\,\text{kJ}$, so the rise is about $60 : 3.4 \approx 18$ degrees. In reality some of the energy goes to the surroundings, so the rise is slightly smaller.

## fy6-6-L3-01
**Given:** bulbs $230\,\text{V}$, $40\,\text{W}$ and $230\,\text{V}$, $100\,\text{W}$ in series at a voltage of $230\,\text{V}$; the resistances stay at their values at the rated voltage
**Find:** the power $P_{40}$ of the $40\,\text{W}$ bulb in watts in the series connection
**Principle:** The marking of a bulb gives the power at the rated voltage, so the resistance is found from the formula $P = U^2 : R$. In a series connection the same current flows through both bulbs, and it is determined by the sum of the resistances. The power of each is $RI^2$.
**Formula:** $R_{40} = \dfrac{U^2}{P_\text{n,40}}$, $R_{100} = \dfrac{U^2}{P_\text{n,100}}$, $I = \dfrac{U}{R_{40} + R_{100}}$, so $P_{40} = R_{40} I^2$
**Conversions:** Not needed: all quantities are in base units.
**Substitution:** $R_{40} = \dfrac{(230\,\text{V})^2}{40\,\text{W}} = 1322.5\,\Omega$, $R_{100} = \dfrac{(230\,\text{V})^2}{100\,\text{W}} = 529\,\Omega$, $I = \dfrac{230\,\text{V}}{1851.5\,\Omega} = 0.1242\,\text{A}$ and $P_{40} = 1322.5\,\Omega \cdot (0.1242\,\text{A})^2 = 20.4\,\text{W}$
**Answer:** $20\,\text{W}$, two significant figures like the power $40\,\text{W}$.
**Reasonableness:** The power of the $100\,\text{W}$ bulb is $529\,\Omega \cdot (0.1242\,\text{A})^2 \approx 8.2\,\text{W}$, so in series the $40\,\text{W}$ bulb shines brighter, because its resistance is larger and the current is the same. The power of each is smaller than the marked one, because across each there is only a part of the mains voltage.

## fy6-6-L3-02
**Given:** $20$ identical bulbs in series, mains voltage $U = 230\,\text{V}$, power of the string $P = 9.2\,\text{W}$
**Find:** the resistance $R$ of one bulb in ohms
**Principle:** In a series connection the same current flows through all the bulbs, and it is found from the power and the voltage of the whole string, $P = UI$. The bulbs are identical, so the mains voltage is shared equally among them. The resistance of one bulb is found from Ohm's law.
**Formula:** $I = \dfrac{P}{U}$ and $U_1 = \dfrac{U}{20}$, so $R = \dfrac{U_1}{I}$
**Conversions:** Not needed: $\text{V} : \text{A} = \Omega$.
**Substitution:** $I = \dfrac{9.2\,\text{W}}{230\,\text{V}} = 0.040\,\text{A}$, $U_1 = \dfrac{230\,\text{V}}{20} = 11.5\,\text{V}$ and $R = \dfrac{11.5\,\text{V}}{0.040\,\text{A}} = 287.5\,\Omega$
**Answer:** $2.9 \cdot 10^{2}\,\Omega$, that is about $290\,\Omega$, two significant figures like the power $9.2\,\text{W}$.
**Reasonableness:** The power of one bulb is $9.2\,\text{W} : 20 = 0.46\,\text{W}$, and $(11.5\,\text{V})^2 : 287.5\,\Omega = 0.46\,\text{W}$ gives the same. The resistance of the whole string, $20 \cdot 287.5\,\Omega = 5750\,\Omega$, gives the current $230\,\text{V} : 5750\,\Omega = 0.040\,\text{A}$.

## fy6-6-L3-03
**Given:** parallel connection, voltage $U = 12\,\text{V}$, $R_1 = 6.0\,\Omega$, total power $P = 36\,\text{W}$
**Find:** the resistance $R_2$ of the other resistor in ohms
**Principle:** In a parallel connection the full voltage of the source is across each resistor, so the power of each is $U^2 : R$. Energy is conserved, so the powers of the resistors add up to the total power, and the power of the other resistor is the total power minus the power of the first.
**Formula:** $P = \dfrac{U^2}{R_1} + \dfrac{U^2}{R_2}$, so $R_2 = \dfrac{U^2}{P - \dfrac{U^2}{R_1}}$
**Conversions:** Not needed: $\text{V}^2 : \text{W} = \Omega$.
**Substitution:** $P_1 = \dfrac{(12\,\text{V})^2}{6.0\,\Omega} = 24\,\text{W}$, $P_2 = 36\,\text{W} - 24\,\text{W} = 12\,\text{W}$ and $R_2 = \dfrac{(12\,\text{V})^2}{12\,\text{W}} = 12\,\Omega$
**Answer:** $12\,\Omega$, two significant figures like the resistance $6.0\,\Omega$ and the power $36\,\text{W}$.
**Reasonableness:** The other resistor gets half the power, so in a parallel connection its resistance must be twice as large, $2 \cdot 6.0\,\Omega = 12\,\Omega$. The currents are $2.0\,\text{A}$ and $1.0\,\text{A}$, and $12\,\text{V} \cdot 3.0\,\text{A} = 36\,\text{W}$.

## fy6-6-L1-06
**Find:** in which of the resistors connected in series more electrical energy is transformed into internal energy.
**Principle:** In a series connection the same current flows through all the components. When the current is the same, the form of Joule's law $P = RI^2$ gives a larger power for the resistor with the larger resistance. The same result is reached through the voltage: the voltage across the larger resistance is larger, $U = RI$, so $P = UI$ is also larger.
**Model answer:** More energy is transformed in the resistor with the larger resistance, because the current is the same and the power grows with the resistance ($P = RI^2$). The option in which the resistor with the smaller resistance has the larger current belongs to a parallel connection. The option in which the voltage is the same also belongs to a parallel connection: in a series connection the voltage of the source is divided among the resistors. Nor is the power equal, because the voltages across the resistors are different.

## fy6-6-L1-07
**Given:** voltage $U = 12\,\text{V}$, current $I = 350\,\text{mA}$
**Find:** the power $P$ of the strip in watts
**Principle:** Electric power is the product of voltage and current. The current is given in milliamperes, so it is first converted to amperes.
**Formula:** $P = UI$
**Conversions:** $1\,\text{mA} = 0.001\,\text{A}$, so $I = 350\,\text{mA} = 0.350\,\text{A}$
**Substitution:** $P = 12\,\text{V} \cdot 0.350\,\text{A} = 4.2\,\text{W}$
**Answer:** $4.2\,\text{W}$, two significant figures like the voltage.
**Reasonableness:** The estimate $12\,\text{V} \cdot 0.35\,\text{A} \approx 12 \cdot \tfrac{1}{3}\,\text{W} = 4\,\text{W}$ is close to the result. Without converting the milliamperes the result would be $4200\,\text{W}$, which is far too large for a small LED strip.

## fy6-6-L1-08
**Given:** initially $U_1 = 2.0\,\text{V}$ and $P_1 = 0.80\,\text{W}$, finally $U_2 = 6.0\,\text{V}$, the resistance $R$ stays the same
**Find:** the power $P_2$ at the voltage $U_2$ in watts
**Principle:** When the voltage is known, the power of a resistor is $P = U^2 : R$. The resistance is obtained from the initial situation, and the same resistance is substituted into the new voltage.
**Formula:** $R = \dfrac{U_1^2}{P_1}$ and $P_2 = \dfrac{U_2^2}{R}$
**Conversions:** Not needed: $\text{V}^2 : \text{W} = \Omega$ and $\text{V}^2 : \Omega = \text{W}$.
**Substitution:** $R = \dfrac{(2.0\,\text{V})^2}{0.80\,\text{W}} = 5.0\,\Omega$ and $P_2 = \dfrac{(6.0\,\text{V})^2}{5.0\,\Omega} = 7.2\,\text{W}$
**Answer:** $7.2\,\text{W}$, two significant figures like the initial data.
**Reasonableness:** The voltage became three times as large, so the power becomes nine times as large: $9 \cdot 0.80\,\text{W} = 7.2\,\text{W}$. The current is $6.0\,\text{V} : 5.0\,\Omega = 1.2\,\text{A}$, and $6.0\,\text{V} \cdot 1.2\,\text{A} = 7.2\,\text{W}$ gives the same power.

## fy6-6-L2-05
**Given:** air temperature $22.0\,{}^\circ\text{C}$ and the measurements of the table $(U;\ I;\ T)$: $(3.0\,\text{V};\ 0.064\,\text{A};\ 24.4\,{}^\circ\text{C})$, $(6.0\,\text{V};\ 0.127\,\text{A};\ 31.0\,{}^\circ\text{C})$, $(9.0\,\text{V};\ 0.192\,\text{A};\ 42.6\,{}^\circ\text{C})$, $(12.0\,\text{V};\ 0.254\,\text{A};\ 58.9\,{}^\circ\text{C})$ and $(15.0\,\text{V};\ 0.320\,\text{A};\ 80.2\,{}^\circ\text{C})$
**Find:** the slope $k$ of the fitted line, that is, the rise in temperature per one watt in the unit K/W
**Principle:** The electric power of a resistor is $P = UI$. The temperature levels off when the power transferred to the surroundings is equal to the electric power coming into the resistor: the resistor warms up until the power transferred to the surroundings is enough to carry away all the incoming power. If the power transferred to the surroundings is approximately proportional to the temperature difference, as it is at small temperature differences, the steady rise $\Delta T = T - 22.0\,{}^\circ\text{C}$ is proportional to the power. When $P = 0$, $\Delta T = 0$, so the line passes through the origin.
**Reading the graph:** The powers are $P = UI$: $0.192\,\text{W}$, $0.762\,\text{W}$, $1.73\,\text{W}$, $3.05\,\text{W}$ and $4.80\,\text{W}$. The rises in temperature are $2.4\,\text{K}$, $9.0\,\text{K}$, $20.6\,\text{K}$, $36.9\,\text{K}$ and $58.2\,\text{K}$. The points $(P;\ \Delta T)$ lie along a line with points on both sides of it. The fitted line passes through the origin and the point $(4.80\,\text{W};\ 58\,\text{K})$.
**Formula:** $\Delta T = kP$, so $k = \dfrac{\Delta T}{P}$
**Conversions:** Not needed: a change of temperature $1\,{}^\circ\text{C} = 1\,\text{K}$.
**Substitution:** $k = \dfrac{58\,\text{K}}{4.80\,\text{W}} = 12.1\,\tfrac{\text{K}}{\text{W}}$
**Answer:** $12.1\,\text{K/W}$, rounded $12\,\text{K/W}$. A fit by eye gives the slope to two significant figures, so about $11.5\text{–}12.7\,\text{K/W}$ is a good answer.
**Reasonableness:** The line predicts for the power $3.05\,\text{W}$ the rise $12.1\,\tfrac{\text{K}}{\text{W}} \cdot 3.05\,\text{W} = 36.9\,\text{K}$, which is the rise of the fourth measurement in the table. At its largest power the temperature of the resistor is $22.0 + 58.2 = 80.2\,{}^\circ\text{C}$, which is plausible for a hot resistor.

## fy6-6-L2-06
**Given:** the measurements $(U;\ I)$ of the table at the voltages $0.5\,\text{V}$ … $6.0\,\text{V}$, in particular $(3.0\,\text{V};\ 0.254\,\text{A})$ and $(6.0\,\text{V};\ 0.346\,\text{A})$
**Find:** the percentage increase of the power $\dfrac{P_2 - P_1}{P_1}$ when the voltage increases from $3.0\,\text{V}$ to $6.0\,\text{V}$
**Principle:** The electric power $P = UI$ holds for any component, also for a bulb whose resistance is not constant. The power is calculated for each row as the product of the voltage and the current, and the change is compared with the initial value.
**Formula:** $P = UI$ and $p = \dfrac{P_2 - P_1}{P_1} \cdot 100\,\%$
**Conversions:** Not needed: $\text{V} \cdot \text{A} = \text{W}$.
**Substitution:** $P_1 = 3.0\,\text{V} \cdot 0.254\,\text{A} = 0.762\,\text{W}$ and $P_2 = 6.0\,\text{V} \cdot 0.346\,\text{A} = 2.076\,\text{W}$, so $p = \dfrac{2.076\,\text{W} - 0.762\,\text{W}}{0.762\,\text{W}} \cdot 100\,\% = 172\,\%$
**Answer:** $172\,\%$, rounded $1.7 \cdot 10^{2}\,\%$ or about $170\,\%$, two significant figures like the measurements of the current and the voltage.
**Reasonableness:** The powers of the other rows are $0.049\,\text{W}$, $0.15\,\text{W}$, $0.424\,\text{W}$, $1.15\,\text{W}$ and $1.59\,\text{W}$, and the power grows on every row. The power does not grow as the square of the voltage because the resistance of the bulb is not constant: at the voltage $3.0\,\text{V}$ it is $3.0\,\text{V} : 0.254\,\text{A} = 11.8\,\Omega$ and at the voltage $6.0\,\text{V}$ already $6.0\,\text{V} : 0.346\,\text{A} = 17.3\,\Omega$. The bulb heats up, the resistance of the filament grows, and the current grows less than the voltage. So the power becomes only $2.7$ times as large and not $4$ times as large, as it would with a constant resistance $P = U^2 : R$ ($300\,\%$).

## fy6-6-L2-07
**Given:** in series bulb A: $U_\text{A} = 9.0\,\text{V}$, bulb B: $U_\text{B} = 3.0\,\text{V}$, current $I = 0.50\,\text{A}$ in both
**Find:** the difference of the powers $P_\text{A} - P_\text{B}$ in watts and the error in the student's reasoning
**Principle:** In a series connection the components are in the same loop, so the same current flows through all of them and current is not used up in a bulb. The student's claim that the brighter bulb uses less current is therefore wrong: according to the table the current is $0.50\,\text{A}$ in both. The power depends on the voltage of the component as well as on the current, $P = UI$. The brighter bulb A is the one with the larger voltage across it, so its power is larger, not smaller.
**Formula:** $P = UI$, so $P_\text{A} - P_\text{B} = (U_\text{A} - U_\text{B})\,I$
**Conversions:** Not needed: $\text{V} \cdot \text{A} = \text{W}$.
**Substitution:** $P_\text{A} = 9.0\,\text{V} \cdot 0.50\,\text{A} = 4.5\,\text{W}$ and $P_\text{B} = 3.0\,\text{V} \cdot 0.50\,\text{A} = 1.5\,\text{W}$, so $P_\text{A} - P_\text{B} = 3.0\,\text{W}$
**Answer:** $3.0\,\text{W}$, two significant figures like the voltages and the current.
**Reasonableness:** The power of bulb A is three times the power of bulb B, because its voltage is three times as large and the current is the same. The resistances of the bulbs are $9.0\,\text{V} : 0.50\,\text{A} = 18\,\Omega$ and $3.0\,\text{V} : 0.50\,\text{A} = 6.0\,\Omega$, and $P = RI^2$ gives the same powers $4.5\,\text{W}$ and $1.5\,\text{W}$. The power of the source $12\,\text{V} \cdot 0.50\,\text{A} = 6.0\,\text{W}$ is the sum of the powers.

## fy6-6-L3-04
**Given:** voltage $U = 230\,\text{V}$; power with the resistor $R_1$ alone: $1100\,\text{W}$, in series $420\,\text{W}$, in parallel $1780\,\text{W}$; permitted powers $1.4\,\text{kW}$ ($R_1$) and $0.75\,\text{kW}$ ($R_2$); new voltage $U' = 1.10 \cdot 230\,\text{V}$
**Find:** the resistances of the resistors and the power, at the voltage $U'$, of the resistor that exceeds its permitted power
**Principle:** The power of a resistor is $P = U^2 : R$ when the resistance is constant. The resistor $R_1$ alone and the series connection give the resistances: in series the total resistance is $R_1 + R_2 = U^2 : P_\text{s}$. For part a) the row $1780\,\text{W}$ of the parallel connection is not needed but serves as a check: in parallel the powers of the resistors add up, so the power of $R_2$ is $1780\,\text{W} - 1100\,\text{W}$. In parallel the full mains voltage $U'$ is across each resistor, so the power of each is $U'^2 : R$.
**Formula:** $R_1 = \dfrac{U^2}{P_1}$, $R_2 = \dfrac{U^2}{P_\text{s}} - R_1$, $P' = \dfrac{U'^2}{R}$
**Conversions:** $U' = 1.10 \cdot 230\,\text{V} = 253\,\text{V}$ and $1.4\,\text{kW} = 1400\,\text{W}$, $0.75\,\text{kW} = 750\,\text{W}$
**Substitution:** $R_1 = \dfrac{(230\,\text{V})^2}{1100\,\text{W}} = 48.09\,\Omega$ and $R_2 = \dfrac{(230\,\text{V})^2}{420\,\text{W}} - 48.09\,\Omega = 125.95\,\Omega - 48.09\,\Omega = 77.86\,\Omega$. At the voltage $253\,\text{V}$: $P_1' = \dfrac{(253\,\text{V})^2}{48.09\,\Omega} = 1331\,\text{W}$ and $P_2' = \dfrac{(253\,\text{V})^2}{77.86\,\Omega} = 822\,\text{W}$
**Answer:** $822\,\text{W}$ in the resistor $R_2$ (rounded $8.2 \cdot 10^{2}\,\text{W}$). The resistances of part a) are $R_1 = 48.1\,\Omega$ and $R_2 = 77.9\,\Omega$. The overloaded resistor is therefore $R_2$. The rounded result has two significant figures like the power $420\,\text{W}$ of the series connection. It exceeds the permitted power $750\,\text{W}$, whereas the power $1331\,\text{W}$ of the resistor $R_1$ stays below the limit $1400\,\text{W}$. More energy is transformed in the resistor $R_1$, but the power grows by the same factor in both ($1.10^2 = 1.21$ times), and the resistor $R_2$ is already near its limit: its power is $679\,\text{W} : 750\,\text{W} = 91\,\%$ of the permitted power, that of the resistor $R_1$ only $79\,\%$.
**Reasonableness:** The measurement of the parallel connection agrees: the power of $R_2$ at the voltage $230\,\text{V}$ is $(230\,\text{V})^2 : 77.86\,\Omega = 679\,\text{W}$, so $1100\,\text{W} + 679\,\text{W} = 1779\,\text{W} \approx 1780\,\text{W}$. The growth factor of the power checks out: $679\,\text{W} \cdot 1.21 = 822\,\text{W}$ and $1100\,\text{W} \cdot 1.21 = 1331\,\text{W}$.

## fy6-6-L3-05
**Given:** rated values of the heater $P_\text{n} = 2.0\,\text{kW}$ and $U_\text{n} = 230\,\text{V}$; voltage of the socket $U = 230\,\text{V}$; resistance of the extension cord: thin $R_\text{thin} = 2.4\,\Omega$, thick $R_\text{thick} = 0.71\,\Omega$; heater and cord in series
**Find:** the power $P_\text{thin}$ transformed into internal energy in the thin cord and the power $P_\text{thick}$ transformed in the thick cord, in watts
**Principle:** The resistance of the heater is obtained from the rated values using $P = U^2 : R$. The resistance of the extension cord is in series with the heater, so the total resistance is the sum of the resistances of the heater and the cord, and the current is the same in both. According to Joule's law the power of the cord is $P = RI^2$.
**Formula:** $R_\text{h} = \dfrac{U_\text{n}^2}{P_\text{n}}$, $I = \dfrac{U}{R_\text{h} + R_\text{w}}$, $P_\text{w} = R_\text{w} I^2$
**Conversions:** $P_\text{n} = 2.0\,\text{kW} = 2000\,\text{W}$
**Substitution:** $R_\text{h} = \dfrac{(230\,\text{V})^2}{2000\,\text{W}} = 26.45\,\Omega$. Thin cord: $I = \dfrac{230\,\text{V}}{26.45\,\Omega + 2.4\,\Omega} = 7.97\,\text{A}$ and $P_\text{thin} = 2.4\,\Omega \cdot (7.97\,\text{A})^2 = 152.5\,\text{W}$. Thick cord: $I = \dfrac{230\,\text{V}}{26.45\,\Omega + 0.71\,\Omega} = 8.47\,\text{A}$ and $P_\text{thick} = 0.71\,\Omega \cdot (8.47\,\text{A})^2 = 50.9\,\text{W}$
**Answer:** $152.5\,\text{W}$, rounded $1.5 \cdot 10^{2}\,\text{W}$ or about $150\,\text{W}$ in the thin cord and $51\,\text{W}$ in the thick one, two significant figures like the resistance $2.4\,\Omega$. The current is almost the same with both cords, $7.97\,\text{A}$ and $8.47\,\text{A}$, so the power $RI^2$ of the cord depends mainly on its resistance: the resistance of the thin cord is about $3.4$ times as large and the power about three times as large. A thin cord on a reel cools poorly, so it warms up. A loaded cord reel should be unwound, and the permitted current of the cord must not be exceeded. Less energy is transformed in the thick cord, so it stays cooler.
**Reasonableness:** With the thin cord the power of the heater is $26.45\,\Omega \cdot (7.97\,\text{A})^2 = 1681\,\text{W}$, and together with the cord $1681\,\text{W} + 152.5\,\text{W} = 1834\,\text{W}$. This is the same as the power of the source $230\,\text{V} \cdot 7.97\,\text{A} = 1834\,\text{W}$. Because of the thin cord the heater thus gets about $1681\,\text{W}$ instead of the rated power $2000\,\text{W}$.

## fy6-6-L2-08
**Find:** how the power of the resistor $R_1$ changes when an identical resistor $R_2$ is connected in series with it and the voltage of the source stays the same.
**Principle:** The total resistance of a series connection is the sum of the resistances of the resistors, and the same current $I = \tfrac{U}{R_1 + R_2}$ flows through all of them. The power of the resistor $R_1$ is obtained from Joule's law $P_1 = R_1 I^2$, because the current is known. The power depends on the square of the current, so when the current halves, the power decreases to one quarter.
**Model answer:** When the resistor $R_1$ is alone, the current and the power are

$$\begin{aligned}
&I = \frac{12\,\text{V}}{24\,\Omega} = 0.50\,\text{A} \\
&P_1 = 24\,\Omega \cdot (0.50\,\text{A})^2 \\
&\phantom{P_1} = 6.0\,\text{W}
\end{aligned}$$

In the series connection the total resistance is $24\,\Omega + 24\,\Omega = 48\,\Omega$, and

$$\begin{aligned}
&I' = \frac{12\,\text{V}}{48\,\Omega} = 0.25\,\text{A} \\
&P_1' = 24\,\Omega \cdot (0.25\,\text{A})^2 \\
&\phantom{P_1'} = 1.5\,\text{W}
\end{aligned}$$

The ratio of the powers is $\tfrac{1.5\,\text{W}}{6.0\,\text{W}} = \tfrac{1}{4}$, that is, the power of the resistor $R_1$ decreases to one quarter. The voltage gives the same result: there is now only $6.0\,\text{V}$ across the resistor $R_1$, and $\tfrac{(6.0\,\text{V})^2}{24\,\Omega} = 1.5\,\text{W}$. The power does not stay the same, because the whole voltage of the source is no longer across the resistor, and it does not decrease only to one half, because the power depends on the square of the current.
