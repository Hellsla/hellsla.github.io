## fy6-14-L1-01
**Given:** voltage of the LED $U_\text{D} = 2.0\,\text{V}$, current $I = 15\,\text{mA}$
**Find:** the power $P_\text{D}$ of the LED in milliwatts
**Principle:** The electric power of a component is its voltage times the current flowing through it. This holds also for an LED, although it does not obey Ohm's law, because power is always the energy that the charge gives up in the component per unit time.
**Formula:** $P_\text{D} = U_\text{D} I$
**Conversions:** $I = 15\,\text{mA} = 15 \cdot 10^{-3}\,\text{A} = 0.015\,\text{A}$
**Substitution:** $P_\text{D} = 2.0\,\text{V} \cdot 0.015\,\text{A} = 0.030\,\text{W} = 30\,\text{mW}$
**Answer:** $30\,\text{mW}$, two significant figures like the voltage and the current.
**Reasonableness:** The unit is consistent: $\text{V} \cdot \text{mA} = \text{mW}$, and $2 \cdot 15 = 30$. The power of an indicator LED is tens of milliwatts, much smaller than that of a light bulb, as we know from experience.

## fy6-14-L1-02
**Given:** voltage of the source $U = 5.0\,\text{V}$, voltage of the LED $U_\text{D} = 3.1\,\text{V}$, current $I = 20\,\text{mA}$
**Find:** the resistance $R$ of the series resistor in ohms
**Principle:** The source, the resistor and the LED are in series, so the same current flows through all of them. By Kirchhoff's voltage law the voltage of the source is shared: $U = U_R + U_\text{D}$. The resistor obeys Ohm's law, $U_R = RI$.
**Formula:** $U = RI + U_\text{D}$, from which $R = \dfrac{U - U_\text{D}}{I}$
**Conversions:** $I = 20\,\text{mA} = 20 \cdot 10^{-3}\,\text{A} = 0.020\,\text{A}$
**Substitution:** $R = \dfrac{5.0\,\text{V} - 3.1\,\text{V}}{0.020\,\text{A}} = \dfrac{1.9\,\text{V}}{0.020\,\text{A}} = 95\,\Omega$
**Answer:** $95\,\Omega$, two significant figures like the difference of the voltages $1.9\,\text{V}$ and the current.
**Reasonableness:** Check: $95\,\Omega \cdot 0.020\,\text{A} = 1.9\,\text{V}$, and $1.9\,\text{V} + 3.1\,\text{V} = 5.0\,\text{V}$. The voltage of a white LED is large, so only a little voltage is left for the resistor and the resistor is small.

## fy6-14-L1-03
**Given:** voltage of the battery $U = 9.0\,\text{V}$, resistor $R = 1.0\,\text{k}\Omega$, voltage of the diode $U_\text{D} = 0.70\,\text{V}$, diode in the forward direction
**Find:** the current $I$ in milliamperes
**Principle:** The diode is in the forward direction, so current flows, and the voltage of the diode is the $0.70\,\text{V}$ given in the task. The battery, the resistor and the diode are in series: the voltage of the battery is shared between the resistor and the diode, and the voltage of the resistor is $U_R = RI$.
**Formula:** $U = RI + U_\text{D}$, from which $I = \dfrac{U - U_\text{D}}{R}$
**Conversions:** $R = 1.0\,\text{k}\Omega = 1.0 \cdot 1000\,\Omega = 1000\,\Omega$
**Substitution:** $I = \dfrac{9.0\,\text{V} - 0.70\,\text{V}}{1000\,\Omega} = \dfrac{8.3\,\text{V}}{1000\,\Omega} = 0.0083\,\text{A} = 8.3\,\text{mA}$
**Answer:** $8.3\,\text{mA}$, two significant figures like the voltage $9.0\,\text{V}$ and the resistance $1.0\,\text{k}\Omega$.
**Reasonableness:** Without the diode the current would be $9.0\,\text{V} : 1000\,\Omega = 9.0\,\text{mA}$. The diode takes only a little voltage, so the current is slightly smaller, as it should be.

## fy6-14-L1-04
**Given:** voltage of the panel $U = 17.5\,\text{V}$, current $I = 5.40\,\text{A}$
**Find:** the power $P$ of the panel in watts
**Principle:** A solar panel is a direct-voltage source. The electric power it gives is the voltage between its terminals times the current, like the power of any source.
**Formula:** $P = UI$
**Conversions:** None needed: the voltage is in volts and the current in amperes, and $\text{V} \cdot \text{A} = \text{W}$.
**Substitution:** $P = 17.5\,\text{V} \cdot 5.40\,\text{A} = 94.5\,\text{W}$
**Answer:** $94.5\,\text{W}$, three significant figures like the voltage and the current.
**Reasonableness:** The estimate $18\,\text{V} \cdot 5\,\text{A} = 90\,\text{W}$ is close to the result. A panel of about $100\,\text{W}$ is an ordinary solar panel for a cabin.

## fy6-14-L1-05
**Given:** the characteristic curve of a green LED, current $I = 10\,\text{mA}$
**Find:** the power $P_\text{D}$ of the LED in milliwatts
**Principle:** The characteristic curve tells what voltage is across the LED at each current. The power is the voltage times the current, so we need the voltage that corresponds to the current $10\,\text{mA}$.
**Reading the graph:** From $10\,\text{mA}$ on the vertical axis we go horizontally to the curve. The curve meets the $10\,\text{mA}$ grid line at a vertical grid line that is one $0.2\,\text{V}$ square to the right of $2.0\,\text{V}$, so $U_\text{D} = 2.2\,\text{V}$.
**Formula:** $P_\text{D} = U_\text{D} I$
**Conversions:** $I = 10\,\text{mA} = 0.010\,\text{A}$
**Substitution:** $P_\text{D} = 2.2\,\text{V} \cdot 0.010\,\text{A} = 0.022\,\text{W} = 22\,\text{mW}$
**Answer:** $22\,\text{mW}$, two significant figures, because the voltage is read from a $0.2\,\text{V}$ grid and the current from a $5\,\text{mA}$ grid.
**Reasonableness:** The voltage of the green LED, $2.2\,\text{V}$, lies between that of the red ($1.8$–$2.0\,\text{V}$) and the blue (about $3\,\text{V}$), as in the text of the chapter. The power is a few tens of milliwatts, ordinary for an indicator light.

## fy6-14-L2-01
**Given:** voltage of the battery $U = 9.0\,\text{V}$, series resistor $R = 470\,\Omega$, LED in the reverse direction; assumption: no current flows in the reverse direction
**Find:** the voltage $U_\text{D}$ of the LED in volts
**Principle:** In the reverse direction practically no current flows through the diode. Since the LED and the resistor are in series, the current of the resistor is also zero, so by Ohm's law the voltage of the resistor is zero. By Kirchhoff's voltage law the whole voltage of the battery is then across the LED.
**Formula:** $U = U_R + U_\text{D}$ and $U_R = RI$, so with the current $I = 0$ we get $U_\text{D} = U - RI = U$
**Conversions:** None needed: the current is zero, so the value of the resistor does not need converting.
**Substitution:** $U_\text{D} = 9.0\,\text{V} - 470\,\Omega \cdot 0\,\text{A} = 9.0\,\text{V}$
**Answer:** $9.0\,\text{V}$, two significant figures like the voltage of the battery.
**Reasonableness:** The series resistor does not protect an LED in the reverse direction, because there is no voltage across the resistor. An ordinary LED often withstands only about $5\,\text{V}$ in the reverse direction, so $9.0\,\text{V}$ can break it; this is why the polarity is checked before connecting.

## fy6-14-L2-02
**Given:** voltage of the battery $U = 9.0\,\text{V}$, two LEDs in series, the voltage of each $U_\text{D} = 2.0\,\text{V}$, current $I = 20\,\text{mA}$
**Find:** the resistance $R$ of the series resistor in ohms
**Principle:** All the components are in series, so the same current flows through them. The voltage of the battery is shared between the resistor and both LEDs: $U = U_R + 2U_\text{D}$. The voltage of the resistor is $U_R = RI$.
**Formula:** $U = RI + 2U_\text{D}$, from which $R = \dfrac{U - 2U_\text{D}}{I}$
**Conversions:** $I = 20\,\text{mA} = 0.020\,\text{A}$
**Substitution:** $R = \dfrac{9.0\,\text{V} - 2 \cdot 2.0\,\text{V}}{0.020\,\text{A}} = \dfrac{5.0\,\text{V}}{0.020\,\text{A}} = 250\,\Omega$
**Answer:** $250\,\Omega$, two significant figures like the voltages and the current.
**Reasonableness:** For one LED the resistor would be $7.0\,\text{V} : 0.020\,\text{A} = 350\,\Omega$. The second LED takes $2.0\,\text{V}$ more, so less voltage is left for the resistor and the resistor is smaller.

## fy6-14-L2-03
**Given:** area $A = 1.6\,\text{m}^2$, light intensity $G = 800\,\text{W/m}^2$, electric power $P = 260\,\text{W}$
**Find:** the efficiency $\eta$ as a percentage
**Principle:** Efficiency is the useful power divided by the power taken in. The panel receives the power of the light, which is the light intensity times the area, and the useful power is the electric power given by the panel.
**Formula:** $\eta = \dfrac{P}{GA}$
**Conversions:** None needed: $\tfrac{\text{W}}{\text{m}^2} \cdot \text{m}^2 = \text{W}$. Finally the ratio is changed to a percentage by multiplying by a hundred.
**Substitution:** $\eta = \dfrac{260\,\text{W}}{800\,\tfrac{\text{W}}{\text{m}^2} \cdot 1.6\,\text{m}^2} = \dfrac{260\,\text{W}}{1280\,\text{W}} = 0.203 = 20.3\,\%$
**Answer:** $20\,\%$, two significant figures like the area $1.6\,\text{m}^2$.
**Reasonableness:** About $1300\,\text{W}$ of light arrives at the panel, and about a fifth of it becomes electricity. The efficiency is in the range of ordinary silicon cells, $15$–$22\,\%$.

## fy6-14-L2-04
**Given:** power of the cell $P = 0.35\,\text{W}$, time $t = 6.0\,\text{h}$
**Find:** the electrical energy $E$ in kilojoules
**Principle:** Power is energy per unit time. When the power is assumed to be the average power all the time, the energy is the power times the time.
**Formula:** $P = \dfrac{E}{t}$, from which $E = Pt$
**Conversions:** $t = 6.0\,\text{h} = 6.0 \cdot 3600\,\text{s} = 21\,600\,\text{s}$
**Substitution:** $E = 0.35\,\text{W} \cdot 21\,600\,\text{s} = 7560\,\text{J} = 7.56\,\text{kJ}$
**Answer:** $7.6\,\text{kJ}$, two significant figures like the power and the time.
**Reasonableness:** In watt-hours the energy is $0.35\,\text{W} \cdot 6.0\,\text{h} = 2.1\,\text{Wh}$, and $2.1 \cdot 3600\,\text{J} = 7560\,\text{J}$, the same result. The amount is of the order of a small battery, which is enough for one LED for the whole night.

## fy6-14-L3-01
**Given:** voltage of the LED $U_\text{D} = 2.0\,\text{V}$, series resistor $R = 120\,\Omega$, voltage of the batteries first $U_1 = 4.5\,\text{V}$ and finally $U_2 = 3.6\,\text{V}$
**Find:** the decrease of the current as a percentage of the original current
**Principle:** By assumption the voltage of the LED stays the same, so the whole change in voltage falls on the resistor. The current is obtained from Kirchhoff's voltage law and Ohm's law. The voltage of the resistor decreases proportionally more than the voltage of the batteries, because the constant voltage of the LED has been subtracted from it.
**Formula:** $I = \dfrac{U - U_\text{D}}{R}$, so $I_1 = \dfrac{U_1 - U_\text{D}}{R}$, $I_2 = \dfrac{U_2 - U_\text{D}}{R}$ and the relative change is $\dfrac{I_1 - I_2}{I_1}$
**Conversions:** None needed: the currents are divided by each other, so the unit cancels. The ratio is changed to a percentage by multiplying by a hundred.
**Substitution:** $I_1 = \dfrac{4.5\,\text{V} - 2.0\,\text{V}}{120\,\Omega} = 0.02083\,\text{A}$, $I_2 = \dfrac{3.6\,\text{V} - 2.0\,\text{V}}{120\,\Omega} = 0.01333\,\text{A}$ and $\dfrac{I_1 - I_2}{I_1} = \dfrac{0.00750\,\text{A}}{0.02083\,\text{A}} = 0.36$
**Answer:** $36\,\%$, two significant figures like the voltages.
**Reasonableness:** The voltage of the batteries fell by only $0.9\,\text{V} : 4.5\,\text{V} = 20\,\%$, but the voltage of the resistor fell from $2.5\,\text{V}$ to $1.6\,\text{V}$, that is, by $36\,\%$. This is why an LED flashlight clearly dims when the batteries start to run down.

## fy6-14-L3-02
**Given:** measured pairs $(U;\ I)$ of the panel in the same lighting (nine pairs in the task)
**Find:** the load resistance $R$ in ohms when the power is the greatest of the measurements
**Principle:** The power of the panel is $P = UI$. It is zero in a short circuit and at open circuit, so the greatest power is between them, at the maximum power point. We calculate the power of each measurement and choose the greatest, and the load resistance is obtained from Ohm's law $U = RI$ for the load, because the voltage of the load is the voltage of the panel and its current is the current of the panel.
**Formula:** $P = UI$, and at the maximum power point $U = RI$, from which $R = \dfrac{U}{I}$
**Conversions:** None needed: the voltages are in volts and the currents in amperes.
**Substitution:** The powers are $0\,\text{W}$, $32.5\,\text{W}$, $44.5\,\text{W}$, $48.8\,\text{W}$, $49.3\,\text{W}$, $45.9\,\text{W}$, $36.1\,\text{W}$, $19.0\,\text{W}$ and $0\,\text{W}$. The greatest is $17.0\,\text{V} \cdot 2.90\,\text{A} = 49.3\,\text{W}$, so $R = \dfrac{17.0\,\text{V}}{2.90\,\text{A}} = 5.86\,\Omega$
**Answer:** $5.9\,\Omega$, two significant figures, because the greatest power and the neighbouring $48.8\,\text{W}$ are so close to each other that the true maximum power point may lie between the measurements.
**Reasonableness:** In a short circuit the load resistance is zero and at open circuit very large, and $5.9\,\Omega$ lies between them. The greatest power is at the knee of the curve, where the current has already begun to fall but the voltage is almost at its greatest.

## fy6-14-L3-03
**Given:** voltage of the strip $U = 12\,\text{V}$, three LEDs in series in a group, the voltage of each $U_\text{D} = 3.0\,\text{V}$, current of the group $I = 20\,\text{mA}$
**Find:** the share of the power of the strip that goes to the series resistors, as a percentage
**Principle:** The groups are in parallel, so across each group there is $12\,\text{V}$, and the groups are identical, so it is enough to consider one group. In a group the LEDs and the resistor are in series, so the same current flows through all of them, and the voltage is shared: $U = U_R + 3U_\text{D}$. The power of the resistor is $U_R I$ and the power of the whole group $UI$.
**Formula:** $U_R = U - 3U_\text{D}$ and the share is $\dfrac{U_R I}{UI}$, so the share is $\dfrac{U - 3U_\text{D}}{U}$
**Conversions:** None needed: the current cancels, and the ratio of the voltages is a ratio. Finally we multiply by a hundred.
**Substitution:** $\dfrac{12\,\text{V} - 3 \cdot 3.0\,\text{V}}{12\,\text{V}} = \dfrac{3.0\,\text{V}}{12\,\text{V}} = 0.25 = 25\,\%$
**Answer:** $25\,\%$, two significant figures like the voltage of the LED $3.0\,\text{V}$.
**Reasonableness:** The power of one group is $12\,\text{V} \cdot 0.020\,\text{A} = 0.24\,\text{W}$, and that of the resistor $3.0\,\text{V} \cdot 0.020\,\text{A} = 0.060\,\text{W}$, which is a quarter. This is why the strip has three LEDs in series: with one LED $9.0\,\text{V} : 12\,\text{V} = 75\,\%$ of the power would become internal energy in the resistor.
