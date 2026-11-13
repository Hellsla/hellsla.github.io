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
**Given:** area $A = 1.6\,\text{m}^2$, irradiance $G = 800\,\text{W/m}^2$, electric power $P = 260\,\text{W}$
**Find:** the efficiency $\eta$ as a percentage
**Principle:** Efficiency is the useful power divided by the power taken in. The panel receives the power of the light, which is the irradiance times the area, and the useful power is the electric power given by the panel.
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

## fy6-14-L1-06
**Find:** what happens in the circuit when the voltage of the battery is $9.0\,\text{V}$ and the triangle of the diode symbol points towards the resistor, which is connected to the negative terminal
**Principle:** The direction of the current is agreed to be from the positive terminal to the negative terminal. A diode lets current through when the direction of the current is the same as the direction the triangle of the symbol points (the forward direction), and blocks it in the opposite direction (the reverse direction). In the forward direction the voltage of the diode is small, and by Kirchhoff's voltage law the rest of the voltage of the battery is left for the resistor in series.
**Model answer:** The triangle points towards the negative terminal, that is, in the direction of the current, so the diode is in the forward direction. Current flows in the circuit, and there is only a small voltage across the diode (at most about $1\,\text{V}$), because the resistor takes most of the $9.0\,\text{V}$ of the battery. The other options are wrong: they either put the diode in the reverse direction or give a diode in the forward direction the whole voltage of the battery.

## fy6-14-L1-07
**Find:** why a series resistor is needed in series with an LED
**Principle:** The voltage of an LED stays almost the same in the forward direction even when the current changes a lot: the characteristic curve rises steeply. If the LED is connected directly to the terminals of the battery, the extra voltage has nowhere else to go, and the current grows so large that the LED burns out. A resistor connected in series takes part of the voltage by Kirchhoff's voltage law ($U = U_R + U_\text{D}$), and by Ohm's law its voltage determines the current: $I = U_R : R$.
**Model answer:** The series resistor is needed because the current of the LED grows steeply even when the voltage of the LED grows only a little. The resistor takes the extra voltage of the battery for itself and keeps the current suitable. The other options are wrong: the resistor does not increase the current, does not change the type of the voltage, and does not prevent current from flowing in the wrong direction.

## fy6-14-L1-08
**Given:** area $A = 12\,\text{cm}^2$, irradiance $G = 1000\,\text{W/m}^2$, voltage $U = 2.0\,\text{V}$, current $I = 100\,\text{mA}$
**Find:** the efficiency $\eta$ as a percentage
**Principle:** The efficiency is the electric power of the cell divided by the power of the light falling on the cell. The electric power is the voltage times the current, and the power of the light is the irradiance times the area.
**Formula:** $P = UI$ and $\eta = \dfrac{P}{GA}$
**Conversions:** $A = 12\,\text{cm}^2 = 12 \cdot 10^{-4}\,\text{m}^2 = 0.0012\,\text{m}^2$ and $I = 100\,\text{mA} = 0.100\,\text{A}$
**Substitution:** $P = 2.0\,\text{V} \cdot 0.100\,\text{A} = 0.20\,\text{W}$ and $\eta = \dfrac{0.20\,\text{W}}{1000\,\tfrac{\text{W}}{\text{m}^2} \cdot 0.0012\,\text{m}^2} = \dfrac{0.20\,\text{W}}{1.2\,\text{W}} = 0.167 = 16.7\,\%$
**Answer:** $17\,\%$, two significant figures like the voltage and the area.
**Reasonableness:** The light falling on the cell is $1.2\,\text{W}$, and about a sixth of it, $0.20\,\text{W}$, becomes electricity: $1.2\,\text{W} : 6 = 0.20\,\text{W}$. The efficiency is in the range of ordinary silicon cells, $15$–$22\,\%$.

## fy6-14-L2-05
**Given:** voltages of the LEDs at the current $15\,\text{mA}$: blue $3.10\,\text{V}$, red $1.90\,\text{V}$, yellow $2.10\,\text{V}$, voltage of the source $U = 5.0\,\text{V}$, current $I = 15\,\text{mA}$
**Find:** a) which LED needs the largest series resistor, b) the resistance $R$ of that series resistor in ohms
**Principle:** The source, the resistor and the LED are in series, so the same current flows through both and $U = U_R + U_\text{D}$. The voltage of the resistor $U_R = U - U_\text{D}$ is the larger, the smaller the voltage of the LED is. Since the current is the same for all, by Ohm's law $R = U_R : I$ the greatest voltage of the resistor gives the greatest resistance. The largest series resistor is therefore needed for the LED with the smallest voltage, that is, the red LED.
**Formula:** $R = \dfrac{U - U_\text{D}}{I}$
**Conversions:** $I = 15\,\text{mA} = 0.015\,\text{A}$
**Substitution:** For the red LED $R = \dfrac{5.0\,\text{V} - 1.90\,\text{V}}{0.015\,\text{A}} = \dfrac{3.1\,\text{V}}{0.015\,\text{A}} = 207\,\Omega$
**Answer:** $210\,\Omega$ (the series resistor of the red LED), two significant figures like the current.
**Reasonableness:** Check: $207\,\Omega \cdot 0.015\,\text{A} = 3.1\,\text{V}$, and $3.1\,\text{V} + 1.90\,\text{V} = 5.0\,\text{V}$. The other LEDs get smaller resistors: for the yellow one $2.9\,\text{V} : 0.015\,\text{A} = 193\,\Omega$ and for the blue one $1.9\,\text{V} : 0.015\,\text{A} = 127\,\Omega$, so the red one is the largest.

## fy6-14-L2-06
**Given:** the measurement pairs $(R;\ U;\ I)$ of the table with eight load resistors
**Find:** the greatest measured power $P$ of the cell in milliwatts
**Principle:** The power of a solar cell is the voltage between its terminals times the current. The power is calculated with each load, and the greatest value is chosen. The load resistor does not affect the calculation, because its effect is already included in the measured voltage and current.
**Formula:** $P = UI$
**Conversions:** Not needed: $\text{V} \cdot \text{mA} = \text{mW}$.
**Substitution:** The powers are $10\,\Omega$: $0.99\,\text{V} \cdot 99\,\text{mA} = 98\,\text{mW}$, $15\,\Omega$: $146\,\text{mW}$, $20\,\Omega$: $178\,\text{mW}$, $22\,\Omega$: $1.99\,\text{V} \cdot 91\,\text{mA} = 181\,\text{mW}$, $27\,\Omega$: $165\,\text{mW}$, $33\,\Omega$: $145\,\text{mW}$, $47\,\Omega$: $109\,\text{mW}$ and $100\,\Omega$: $54\,\text{mW}$. The greatest is at $22\,\Omega$.
**Answer:** $181\,\text{mW}$, three significant figures like the voltage and the current.
**Reasonableness:** The power is small with the loads $10\,\Omega$ (the voltage is small) and $100\,\Omega$ (the current is small), and the greatest power lies between them at the knee of the curve. Check: $U : I = 1.99\,\text{V} : 0.091\,\text{A} = 21.9\,\Omega \approx 22\,\Omega$, so the measurement agrees with the load resistor.

## fy6-14-L2-07
**Given:** voltage of the battery $U = 9.0\,\text{V}$, voltage of the LED $U_\text{D} = 3.2\,\text{V}$, current $I = 15\,\text{mA}$; the student got $600\,\Omega$
**Find:** a) the student's error, b) the correct series resistor $R$ in ohms
**Principle:** The source, the resistor and the LED are in series, so the voltage of the battery is shared between the resistor and the LED: $U = U_R + U_\text{D}$. Ohm's law $R = U_R : I$ concerns the voltage of the resistor itself, not the whole voltage of the battery. The student used the whole voltage of the battery as the voltage of the resistor and forgot the voltage of the LED. The error makes the resistor too large, so the current would be smaller than desired.
**Formula:** $R = \dfrac{U - U_\text{D}}{I}$
**Conversions:** $I = 15\,\text{mA} = 0.015\,\text{A}$
**Substitution:** $R = \dfrac{9.0\,\text{V} - 3.2\,\text{V}}{0.015\,\text{A}} = \dfrac{5.8\,\text{V}}{0.015\,\text{A}} = 387\,\Omega$
**Answer:** $390\,\Omega$, two significant figures like the voltages and the current.
**Reasonableness:** Check: $387\,\Omega \cdot 0.015\,\text{A} = 5.8\,\text{V}$, and $5.8\,\text{V} + 3.2\,\text{V} = 9.0\,\text{V}$. The student's $600\,\Omega$ would give a current of only $5.8\,\text{V} : 600\,\Omega = 9.7\,\text{mA}$, so the LED would be dimmer than desired.

## fy6-14-L2-08
**Find:** which of the three lights are on and why.
**Principle:** A diode and an LED conduct only in the forward direction, when the anode is on the positive terminal side of the battery. In the reverse direction no current passes. Branches connected in parallel are each at the whole voltage of the battery, so each branch is a circuit of its own: a diode in the reverse direction in one branch interrupts only the current of that branch. The same current passes through components in series.
**Model answer:** Only LED A is on.

Branch 1: the anode of the LED is on the positive terminal side, so the LED is in the forward direction. The voltage of the branch $4.5\,\text{V}$ is greater than the voltage of the LED $2.0\,\text{V}$, and across the series resistor remains $4.5\,\text{V} - 2.0\,\text{V} = 2.5\,\text{V}$. Current passes, and LED A is on.

Branch 2: the cathode of the LED is on the positive terminal side, so LED B is in the reverse direction. No current passes, and the whole $4.5\,\text{V}$ is across the LED.

Branch 3: the cathode of the silicon diode is on the positive terminal side, so the diode is in the reverse direction. The filament of the lamp would conduct in both directions, but in series the same current passes through the lamp and the diode, and the diode stops it. Lamp C is not on.

So the reason is that a diode conducts only when the anode is on the positive terminal side, and each parallel branch works as a circuit of its own. The need for a series resistor is a true fact, but it does not tell the direction of the current. If the branches were in series, even one diode in the reverse direction would interrupt the current of the whole circuit, and no light would be on.

## fy6-14-L3-04
**Given:** area $A = 24\,\text{m}^2$, efficiency $\eta = 19\,\%$, monthly radiation energies $H$ and consumptions $E_\text{kul}$ in the table
**Find:** a) the annual production $E$, b) the degree of self-sufficiency as a percentage, c) the months in which the production is smaller than the consumption, and the limitation of the degree of self-sufficiency
**Principle:** The efficiency is the electrical energy divided by the radiation energy falling on the panels. The radiation energy is the radiation energy per square metre times the area, $H A$, so the electrical energy produced is $E = \eta H A$. The annual production is obtained by adding up the radiation energies of the months, and the degree of self-sufficiency is the ratio of the annual production to the annual consumption.
**Formula:** $E = \eta A \sum H$ and degree of self-sufficiency $= \dfrac{E}{\sum E_\text{kul}}$
**Conversions:** $\eta = 19\,\% = 0.19$. No others: the energies are in kilowatt-hours.
**Substitution:** a) The sum of the radiation energies is $\sum H = 1027\,\text{kWh/m}^2$, so $E = 0.19 \cdot 24\,\text{m}^2 \cdot 1027\,\tfrac{\text{kWh}}{\text{m}^2} = 4683\,\text{kWh}$. b) The sum of the consumptions is $\sum E_\text{kul} = 5340\,\text{kWh}$, so the degree of self-sufficiency is $\dfrac{4683\,\text{kWh}}{5340\,\text{kWh}} = 0.877 = 87.7\,\%$. c) The monthly production is $E_\text{kk} = 0.19 \cdot 24\,\text{m}^2 \cdot H = 4.56\,\text{m}^2 \cdot H$. It is smaller than the consumption in January, February and March and in October, November and December: for example in January $4.56\,\text{m}^2 \cdot 12\,\tfrac{\text{kWh}}{\text{m}^2} = 55\,\text{kWh}$ when the consumption is $620\,\text{kWh}$, and in December $36\,\text{kWh}$ when the consumption is $650\,\text{kWh}$. The consumption of these six months is $3370\,\text{kWh}$ in total and the production $853\,\text{kWh}$ in total, so the shortfall is $2517\,\text{kWh}$.
**Answer:** $88\,\%$, two significant figures like the efficiency $19\,\%$. The annual production is about $4700\,\text{kWh}$.
**Reasonableness:** The production is about $4.7\,\text{MWh}$, which fits a panel array of $24\,\text{m}^2$ in Finland, and it is a little below the consumption of the house, $5340\,\text{kWh}$, so the degree of self-sufficiency is below $100\,\%$. The degree of self-sufficiency is an annual sum. The surplus of summer cannot be used in winter without storage, and the shortfall of winter, $2517\,\text{kWh}$, is $2517 : 5340 = 47\,\%$ of the annual consumption. So at least this share is bought from the grid, although the degree of self-sufficiency is $88\,\%$.

## fy6-14-L3-05
**Given:** the measurement points of the characteristic curve of the LED $(U_\text{D};\ I)$, voltage of the battery $U = 4.5\,\text{V}$, series resistor $R = 180\,\Omega$, greatest permitted current $25\,\text{mA}$
**Find:** a) the threshold voltage, b) the current at the operating point in milliamperes, c) the change in the voltage of the LED as the current grows, and the justification for a constant voltage
**Principle:** In a series circuit the same current flows through the resistor and the LED, and $U = U_R + U_\text{D}$. The current coming through the resistor is $I = \dfrac{U - U_\text{D}}{R}$ at each voltage of the LED, and the current of the LED is obtained from the characteristic curve. The operating point is the voltage at which these two currents are equal: the intersection of the load line and the characteristic curve.
**Reading the graph:** a) The steep straight part of the characteristic curve lies between the last two points of the table: the current grows from $20\,\text{mA}$ to $41\,\text{mA}$ when the voltage grows from $2.05\,\text{V}$ to $2.10\,\text{V}$, so the slope of the line is $\dfrac{41\,\text{mA} - 20\,\text{mA}}{2.10\,\text{V} - 2.05\,\text{V}} = 420\,\tfrac{\text{mA}}{\text{V}}$. The line meets the voltage axis at $2.05\,\text{V} - \dfrac{20\,\text{mA}}{420\,\text{mA/V}} = 2.05\,\text{V} - 0.048\,\text{V} = 2.00\,\text{V}$. The threshold voltage is about $2.0\,\text{V}$.
**Formula:** $I = \dfrac{U - U_\text{D}}{R}$ through the resistor and the current of the characteristic curve from the table
**Conversions:** Not needed: the voltages are in volts and the resistance in ohms, and the result $\text{V} : \Omega = \text{A}$ is converted to milliamperes by multiplying by $1000$.
**Substitution:** The current coming through the resistor is, at the voltage $2.00\,\text{V}$, $\dfrac{4.5\,\text{V} - 2.00\,\text{V}}{180\,\Omega} = 13.9\,\text{mA}$ and, at the voltage $2.05\,\text{V}$, $\dfrac{4.5\,\text{V} - 2.05\,\text{V}}{180\,\Omega} = 13.6\,\text{mA}$. The current of the LED at these voltages is $9.8\,\text{mA}$ and $20\,\text{mA}$. At the voltage $2.00\,\text{V}$ the current coming through the resistor is greater than the current of the LED, and at $2.05\,\text{V}$ it is smaller, so the intersection lies in between. Drawn as straight lines, the intersection is at $U_\text{D} \approx 2.02\,\text{V}$ and $I \approx 13.8\,\text{mA}$. Check: $\dfrac{4.5\,\text{V} - 2.02\,\text{V}}{180\,\Omega} = 13.8\,\text{mA}$. c) When the current grows from $9.8\,\text{mA}$ to $41\,\text{mA}$, that is, to more than four times, the voltage changes from $2.00\,\text{V}$ to $2.10\,\text{V}$, that is, by $0.10\,\text{V}$.
**Answer:** $14\,\text{mA}$, two significant figures, because the spacing of the points in the table is coarse and the result has been read from between two points. The voltage at the operating point is about $2.0\,\text{V}$. The current is smaller than the permitted $25\,\text{mA}$.
**Reasonableness:** The current $13.8\,\text{mA}$ is smaller than the permitted $25\,\text{mA}$, so the LED withstands it. The voltage $2.02\,\text{V}$ is in the ordinary range of a green LED, and the voltage at the operating point is slightly greater than the threshold voltage $2.0\,\text{V}$, as it should be on a steep curve. Justification for c): the voltage changes only $0.10\,\text{V}$, about $5\,\%$, although the current grows to more than four times. So the voltage of the LED can be kept constant, and the voltage $U - U_\text{D}$ is left for the series resistor, which determines the current. Without the resistor the current would be determined by the steep curve alone, and even a small increase in voltage would make the current large.

## fy6-14-L2-09
**Given:** the $(U, I)$ graph of a solar panel, voltage $U = 4.0\,\text{V}$
**Find:** the electrical power $P$ of the panel in watts
**Principle:** The panel is a DC voltage source, and its power is the voltage times the current. The graph tells the current that the panel gives when the voltage is $4.0\,\text{V}$.
**Reading the graph:** From $4\,\text{V}$ on the horizontal axis we go up to the curve and then horizontally to the vertical axis. At this point the curve is still almost horizontal and runs along the $200\,\text{mA}$ grid line, so $I = 200\,\text{mA}$.
**Formula:** $P = U I$
**Conversions:** $I = 200\,\text{mA} = 200 \cdot 10^{-3}\,\text{A} = 0.200\,\text{A}$
**Substitution:** $P = 4.0\,\text{V} \cdot 0.200\,\text{A} = 0.80\,\text{W}$
**Answer:** $0.80\,\text{W}$, two significant figures, because the voltage is given with two figures and the current is read from a $50\,\text{mA}$ grid.
**Reasonableness:** The power is smaller than the product of the short-circuit current and the open-circuit voltage, about $6.0\,\text{V} \cdot 0.200\,\text{A} = 1.2\,\text{W}$, because these do not occur at the same time. It is also smaller than the maximum power of the panel in the chapter ($0.92\,\text{W}$), as it should be.
