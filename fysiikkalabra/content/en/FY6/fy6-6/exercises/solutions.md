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
