## fy7-7-L1-01
**Given:** number of turns $N = 300$, area $A = 0.0030\,\text{m}^2$, magnetic flux density $B = 0.15\,\text{T}$, rotation frequency $f = 10\,\text{Hz}$
**Find:** the peak value $e_0$ of the voltage in volts
**Principle:** The coil rotates steadily in a uniform field, so the flux through it varies sinusoidally and a sinusoidal alternating voltage is induced in the coil. Its peak value is $e_0 = NBA \cdot 2\pi f$: the voltage is greatest when the plane of the coil is parallel to the field and the flux changes fastest.
**Formula:** $e_0 = NBA \cdot 2\pi f$
**Conversions:** Not needed: the quantities are in SI units, and $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \text{V}$.
**Substitution:** $e_0 = 300 \cdot 0.15\,\text{T} \cdot 0.0030\,\text{m}^2 \cdot 2\pi \cdot 10\,\tfrac{1}{\text{s}} = 8.482\,\text{V}$
**Answer:** $8.5\,\text{V}$, two significant figures like the initial values.
**Reasonableness:** With round numbers $300 \cdot 0.15\,\text{T} \cdot 0.003\,\text{m}^2 \approx 0.14\,\text{Wb}$, and multiplying this by $2\pi \cdot 10 \approx 60$ gives about $8\,\text{V}$. A voltage of a few volts suits a teaching generator turned by hand.

## fy7-7-L1-02
**Given:** rms value of the voltage $U = 115\,\text{V}$, frequency $400\,\text{Hz}$
**Find:** the peak value $U_0$ of the voltage in volts
**Principle:** An alternating voltage is given as an rms value. The rms value of a sinusoidal voltage is the peak value divided by $\sqrt{2}$, so the peak value is $\sqrt{2}$ times the rms value. The frequency does not affect this ratio.
**Formula:** $U = \dfrac{U_0}{\sqrt{2}}$, so $U_0 = \sqrt{2} \cdot U$
**Conversions:** Not needed.
**Substitution:** $U_0 = \sqrt{2} \cdot 115\,\text{V} = 162.63\,\text{V}$
**Answer:** $163\,\text{V}$, three significant figures like the voltage $115\,\text{V}$.
**Reasonableness:** The peak value is about $1.4$ times the rms value: $1.4 \cdot 115\,\text{V} \approx 161\,\text{V}$. In the same way the peak value of the household $230\,\text{V}$ is about $325\,\text{V}$.

## fy7-7-L1-03
**Given:** peak value of the current $I_0 = 8.5\,\text{A}$, the current is sinusoidal
**Find:** the rms value $I$ of the current in amperes
**Principle:** The rms value is the direct current that would deliver the same average power to a resistor. For a sinusoidal current the power in a resistor is on average half of the peak power, so the rms value is the peak value divided by $\sqrt{2}$.
**Formula:** $I = \dfrac{I_0}{\sqrt{2}}$
**Conversions:** Not needed.
**Substitution:** $I = \dfrac{8.5\,\text{A}}{\sqrt{2}} = 6.010\,\text{A}$
**Answer:** $6.0\,\text{A}$, two significant figures like the peak value $8.5\,\text{A}$.
**Reasonableness:** The rms value is about $0.7$ times the peak value: $0.7 \cdot 8.5\,\text{A} \approx 6\,\text{A}$. At the mains voltage $230\,\text{V}$ this corresponds to a power of about $1.4\,\text{kW}$, which suits a kettle.

## fy7-7-L1-04
**Given:** the shaft makes $1500$ revolutions per minute
**Find:** the rotation frequency $f$ in hertz
**Principle:** The rotation frequency is the number of revolutions per second. When the revolutions are known per minute, they are divided by the number of seconds in a minute.
**Formula:** $f = \dfrac{n}{t}$, where $n$ is the number of revolutions in the time $t$
**Conversions:** $t = 1\,\text{min} = 60\,\text{s}$
**Substitution:** $f = \dfrac{1500}{60\,\text{s}} = 25\,\tfrac{1}{\text{s}} = 25\,\text{Hz}$
**Answer:** $25\,\text{Hz}$. The reading $1500$ revolutions per minute is exact, so the result is exactly $25\,\text{Hz}$.
**Reasonableness:** The grid frequency $50\,\text{Hz}$ would correspond to $3000$ revolutions per minute with one pair of magnetic poles. Half of that gives half the frequency, so such a generator has two pairs of poles so that the frequency of the voltage is $50\,\text{Hz}$.

## fy7-7-L1-05
**Given:** rms value of the voltage $U = 230\,\text{V}$, rms value of the current $I = 4.35\,\text{A}$
**Find:** the average power $P$ in kilowatts
**Principle:** The rms value is defined so that with alternating current the average power is calculated from the rms values with the same formula as with direct current. A heater is a resistor, so the voltage and the current are in step.
**Formula:** $P = UI$
**Conversions:** The result is converted to kilowatts: $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P = 230\,\text{V} \cdot 4.35\,\text{A} = 1000.5\,\text{W} = 1000.5 \cdot 0.001\,\text{kW} = 1.0005\,\text{kW}$
**Answer:** $1.00\,\text{kW}$, three significant figures like the current $4.35\,\text{A}$ and the voltage $230\,\text{V}$.
**Reasonableness:** The power of an ordinary electric heater is $0.5$–$2\,\text{kW}$. A power calculated with the peak values would be $2.00\,\text{kW}$, twice as large, but that is only the instantaneous peak value, not the average.

## fy7-7-L1-06
**Find:** which statement about the voltage $230\,\text{V}$ of the socket is correct.
**Principle:** An alternating voltage is given as an rms value: the rms value is the direct voltage that would produce the same average power in a resistor. The peak value of a sinusoidal voltage is $\sqrt{2}$ times the rms value, so it is larger than the rms value. The average value of the voltage over a period is zero, so it is not a suitable measure of the size of the voltage.
**Model answer:** The number $230\,\text{V}$ is the rms value: it produces the same power as a direct voltage, and the peak value is larger, about $230\,\text{V} \cdot \sqrt{2} \approx 325\,\text{V}$. The claim that the number is the peak value is wrong, because meters show the rms value. The claim about the average value is wrong, because the average is zero. The claim that the peak value is smaller than the rms value is wrong, because the peak value is larger than the rms value.

## fy7-7-L1-07
**Given:** rotation rate $3000$ revolutions per minute
**Find:** the period $T$ of the voltage in milliseconds
**Principle:** The frequency of the voltage is the same as the rotation frequency of the coil, and the period is the reciprocal of the frequency. First the revolutions per minute are converted into revolutions per second.
**Formula:** $f = \dfrac{n}{t}$ and $T = \dfrac{1}{f}$
**Conversions:** $t = 1\,\text{min} = 60\,\text{s}$ and finally $1\,\text{s} = 1000\,\text{ms}$
**Substitution:** $f = \dfrac{3000}{60\,\text{s}} = 50\,\text{Hz}$ and $T = \dfrac{1}{50\,\tfrac{1}{\text{s}}} = 0.020\,\text{s} = 0.020 \cdot 1000\,\text{ms} = 20\,\text{ms}$
**Answer:** $20\,\text{ms}$; the reading $3000$ revolutions per minute is exact, so the result is exactly $20\,\text{ms}$.
**Reasonableness:** The frequency $50\,\text{Hz}$ is the frequency of the electricity grid, and its period is $20\,\text{ms}$. Check: $50 \cdot 20\,\text{ms} = 1000\,\text{ms} = 1\,\text{s}$.

## fy7-7-L1-08
**Given:** peak value of the sinusoidal voltage $U_0 = 17.0\,\text{V}$
**Find:** the voltage $U$ shown by the multimeter in volts
**Principle:** A multimeter shows the rms value of an alternating voltage. The rms value of a sinusoidal voltage is the peak value divided by $\sqrt{2}$.
**Formula:** $U = \dfrac{U_0}{\sqrt{2}}$
**Conversions:** Not needed.
**Substitution:** $U = \dfrac{17.0\,\text{V}}{\sqrt{2}} = 12.02\,\text{V}$
**Answer:** $12.0\,\text{V}$, three significant figures like the peak value $17.0\,\text{V}$.
**Reasonableness:** The rms value is about $0.7$ times the peak value: $0.7 \cdot 17.0\,\text{V} \approx 12\,\text{V}$. The result is smaller than the peak value, as it should be.

## fy7-7-L2-01
**Given:** number of turns $N = 150$, sides of the coil $6.0\,\text{cm}$ and $8.0\,\text{cm}$, magnetic flux density $B = 0.25\,\text{T}$, rotation rate $1200$ revolutions per minute
**Find:** the peak value $e_0$ of the voltage in volts
**Principle:** The coil rotates steadily in a uniform field, so a sinusoidal alternating voltage is induced in it, with peak value $e_0 = NBA \cdot 2\pi f$. First the area of the coil and the rotation frequency are calculated in SI units.
**Formula:** $A = ab$ and $e_0 = NBA \cdot 2\pi f$
**Conversions:** $A = 6.0 \cdot 0.01\,\text{m} \cdot 8.0 \cdot 0.01\,\text{m} = 0.0048\,\text{m}^2$ and $f = \dfrac{1200}{60\,\text{s}} = 20\,\text{Hz}$
**Substitution:** $e_0 = 150 \cdot 0.25\,\text{T} \cdot 0.0048\,\text{m}^2 \cdot 2\pi \cdot 20\,\tfrac{1}{\text{s}} = 22.62\,\text{V}$
**Answer:** $23\,\text{V}$, two significant figures like the dimensions of the coil and the magnetic flux density.
**Reasonableness:** With round numbers $150 \cdot 0.25\,\text{T} \cdot 0.005\,\text{m}^2 \approx 0.19\,\text{Wb}$ and $2\pi \cdot 20\,\tfrac{1}{\text{s}} \approx 125\,\tfrac{1}{\text{s}}$, so $e_0 \approx 23\,\text{V}$. If the rotation rate $1200$ had been used as hertz, the result would have been $60$ times as large.

## fy7-7-L2-02
**Given:** number of turns $N = 200$, area $A = 30\,\text{cm}^2$, peak value and period read from the graph
**Find:** the magnetic flux density $B$ in teslas
**Principle:** The coil rotates steadily in a uniform field, so its voltage is sinusoidal and the peak value is $e_0 = NBA \cdot 2\pi f$. The graph gives the peak value and the period, and the period gives the rotation frequency $f = 1 : T$.
**Reading the graph:** The peaks of the curve are on the grid line $12\,\text{V}$ (at the times $10\,\text{ms}$ and $50\,\text{ms}$), so $e_0 = 12\,\text{V}$. The curve is zero and rising at the times $0\,\text{ms}$, $40\,\text{ms}$ and $80\,\text{ms}$, so one period lasts $T = 40\,\text{ms}$.
**Formula:** $f = \dfrac{1}{T}$ and $e_0 = NBA \cdot 2\pi f$, so $B = \dfrac{e_0}{NA \cdot 2\pi f} = \dfrac{e_0 T}{NA \cdot 2\pi}$
**Conversions:** $T = 40\,\text{ms} = 40 \cdot 0.001\,\text{s} = 0.040\,\text{s}$ and $A = 30\,\text{cm}^2 = 30 \cdot 0.0001\,\text{m}^2 = 0.0030\,\text{m}^2$
**Substitution:** $f = \dfrac{1}{0.040\,\text{s}} = 25\,\text{Hz}$ and $B = \dfrac{12\,\text{V}}{200 \cdot 0.0030\,\text{m}^2 \cdot 2\pi \cdot 25\,\tfrac{1}{\text{s}}} = \dfrac{12\,\text{V}}{94.25\,\tfrac{\text{m}^2}{\text{s}}} = 0.1273\,\text{T}$
**Answer:** $0.13\,\text{T}$, two significant figures, because the values $12\,\text{V}$ and $40\,\text{ms}$ read from the graph are known to two figures.
**Reasonableness:** The field of a permanent magnet is typically a few tenths of a tesla, so $0.13\,\text{T}$ is believable. Check: $200 \cdot 0.13\,\text{T} \cdot 0.0030\,\text{m}^2 \cdot 2\pi \cdot 25\,\tfrac{1}{\text{s}} \approx 12.3\,\text{V}$, which matches the peak of the graph.

## fy7-7-L2-03
**Given:** rms value of the voltage $U = 12\,\text{V}$, number of turns $N = 200$, area $A = 0.0050\,\text{m}^2$, magnetic flux density $B = 0.30\,\text{T}$
**Find:** the rotation frequency $f$ in hertz
**Principle:** The voltage of a rotating coil is sinusoidal, and its peak value is $e_0 = NBA \cdot 2\pi f$. The given $12\,\text{V}$ is an rms value, so the peak value is $\sqrt{2}$ times as large. The rotation frequency is solved from the formula for the peak value.
**Formula:** $e_0 = \sqrt{2} \cdot U$ and $e_0 = NBA \cdot 2\pi f$, so $f = \dfrac{\sqrt{2} \cdot U}{NBA \cdot 2\pi}$
**Conversions:** Not needed: the quantities are in SI units.
**Substitution:** $e_0 = \sqrt{2} \cdot 12\,\text{V} = 16.97\,\text{V}$ and $f = \dfrac{16.97\,\text{V}}{200 \cdot 0.30\,\text{T} \cdot 0.0050\,\text{m}^2 \cdot 2\pi} = \dfrac{16.97\,\text{V}}{1.885\,\text{V}\cdot\text{s}} = 9.003\,\text{Hz}$
**Answer:** $9.0\,\text{Hz}$, two significant figures like the voltage $12\,\text{V}$ and the field $0.30\,\text{T}$.
**Reasonableness:** Nine revolutions per second is brisk but possible with a crank that has gearing. If the rms value had been substituted in place of the peak value, the frequency would have come out too small, $6.4\,\text{Hz}$, and the rms value of the voltage would have been below $12\,\text{V}$.

## fy7-7-L2-04
**Given:** electrical energy produced $E = 19.8\,\text{TWh}$ in 2024, length of the year $366$ days, rated power at the end of the year $P_\text{n} = 8358\,\text{MW}$ (Suomen Uusiutuvat ry)
**Find:** the share of the average power in the rated power as a percentage
**Principle:** The average power is the energy produced during the year divided by the length of the year. Wind turbines produce their rated power only in a strong wind, so the average power is clearly smaller than the rated power. The share is obtained by dividing the average power by the rated power.
**Formula:** $P = \dfrac{E}{t}$ and share $= \dfrac{P}{P_\text{n}} \cdot 100\,\%$
**Conversions:** $t = 366 \cdot 24\,\text{h} = 8784\,\text{h}$, $E = 19.8\,\text{TWh} = 19.8 \cdot 10^{12}\,\text{Wh}$ and $P_\text{n} = 8358\,\text{MW} = 8358 \cdot 10^{6}\,\text{W}$
**Substitution:** $P = \dfrac{19.8 \cdot 10^{12}\,\text{Wh}}{8784\,\text{h}} = 2.254 \cdot 10^{9}\,\text{W}$ and share $= \dfrac{2.254 \cdot 10^{9}\,\text{W}}{8358 \cdot 10^{6}\,\text{W}} \cdot 100\,\% = 26.97\,\%$
**Answer:** $27\,\%$, two significant figures, because the production $19.8\,\text{TWh}$ is given to three figures and the result is an estimate.
**Reasonableness:** The average power of wind turbines is typically a quarter to a third of the rated power, so $27\,\%$ is believable. The true share is slightly larger, because the rated power grew during the year: at the beginning of the year there were fewer turbines than at the end.

## fy7-7-L2-05
**Given:** the $14$ data points of the table, where the voltage $e$ is given as a function of time $t$; the voltage is sinusoidal
**Find:** a) the period $T$ and the frequency $f$, b) the peak value $e_0$, c) the rms value $U$ in volts
**Principle:** The period of a sinusoidal voltage is the time after which the voltage has the same value and is going in the same direction. The peak value is the greatest value of the absolute value of the voltage, and the rms value is the peak value divided by $\sqrt{2}$.
**Reading the graph:** In the table the voltage is zero and rising at the time $0\,\text{ms}$ (value $0.1\,\text{V}$) and again at the time $24\,\text{ms}$ (value $0.0\,\text{V}$), so $T = 24\,\text{ms}$. The voltage is zero also at the time $12\,\text{ms}$ (value $-0.1\,\text{V}$), that is, at half a period. The greatest voltage is $8.4\,\text{V}$ at the time $6\,\text{ms}$ and the smallest $-8.4\,\text{V}$ at the time $18\,\text{ms}$, so $e_0 = 8.4\,\text{V}$.
**Formula:** $f = \dfrac{1}{T}$ and $U = \dfrac{e_0}{\sqrt{2}}$
**Conversions:** $T = 24\,\text{ms} = 24 \cdot 0.001\,\text{s} = 0.024\,\text{s}$
**Substitution:** $f = \dfrac{1}{0.024\,\text{s}} = 41.7\,\text{Hz}$ and $U = \dfrac{8.4\,\text{V}}{\sqrt{2}} = 5.94\,\text{V}$
**Answer:** a) $T = 24\,\text{ms}$ and $f \approx 42\,\text{Hz}$, b) $e_0 = 8.4\,\text{V}$, c) $U \approx 5.9\,\text{V}$. The result is recorded to two significant figures, like the peak value of the voltage.
**Reasonableness:** The rms value is about $0.7$ times the peak value: $0.7 \cdot 8.4\,\text{V} \approx 5.9\,\text{V}$. The voltage rises from zero to the peak value $8.4\,\text{V}$ in a quarter of a period, as on a sine curve: $24\,\text{ms} : 4 = 6\,\text{ms}$, and in the table the peak is at the time $6\,\text{ms}$.

## fy7-7-L2-06
**Given:** rotation frequency $f_1 = 5.0\,\text{Hz}$ and peak value $e_{0,1} = 4.1\,\text{V}$; rotation frequency $f_2 = 10.0\,\text{Hz}$ and measured peak value $e_{0,2} = 8.0\,\text{V}$; $N$, $B$ and $A$ the same
**Find:** a) the predicted peak value at the frequency $f_2$, b) the deviation of the measurement from the prediction as a percentage, c) the change of the frequency and whether the measurement fits
**Principle:** The peak value $e_0 = NBA \cdot 2\pi f$ is directly proportional to the rotation frequency when $N$, $B$ and $A$ stay the same. A doubled rotation frequency therefore gives a doubled peak value. The deviation is calculated as the difference between the prediction and the measurement relative to the prediction.
**Formula:** $e_{0,2} = e_{0,1} \cdot \dfrac{f_2}{f_1}$ and deviation $= \dfrac{|e_{0,\text{predicted}} - e_{0,\text{measured}}|}{e_{0,\text{predicted}}} \cdot 100\,\%$
**Conversions:** Not needed: the ratio $f_2 : f_1$ is a number.
**Substitution:** a) $e_{0,\text{predicted}} = 4.1\,\text{V} \cdot \dfrac{10.0\,\text{Hz}}{5.0\,\text{Hz}} = 8.2\,\text{V}$. b) Deviation $= \dfrac{|8.2\,\text{V} - 8.0\,\text{V}|}{8.2\,\text{V}} \cdot 100\,\% = 2.44\,\%$
**Answer:** The deviation is $2.4\,\%$. c) The frequency of the voltage is the same as the rotation frequency, so it also doubles: the period is halved from $200\,\text{ms}$ to $100\,\text{ms}$. The uncertainty of reading each peak value is $\pm 0.1\,\text{V}$. The prediction $2 \cdot 4.1\,\text{V}$ doubles the uncertainty of the reading ($\pm 0.2\,\text{V}$), and the uncertainty of the measured value $\pm 0.1\,\text{V}$ is added to it, so the total uncertainty is about $\pm 0.3\,\text{V}$. The difference $0.2\,\text{V}$ is smaller than this, so the measurement does not differ from the prediction by more than the reading accuracy allows: a difference from proportionality cannot be shown, and the measurement agrees with the prediction.
**Reasonableness:** At double the frequency the peak value is almost double: $8.0 : 4.1 = 1.95$. If the peak value had depended on the frequency in some other way, for example quadratically, the result would have been about $16\,\text{V}$.

## fy7-7-L2-07
**Given:** power of the bulb $P = 60\,\text{W}$, mains voltage $230\,\text{V}$; in the student’s solution $230\,\text{V}$ has been interpreted as a peak value and the current obtained is $0.37\,\text{A}$
**Find:** a) the student’s error, b) the rms value $I$ of the current of the bulb in amperes
**Principle:** The mains voltage $230\,\text{V}$ is already an rms value, because an alternating voltage is given as an rms value. The average power is calculated from rms values as with direct current, $P = UI$, so the rms value of the current is obtained directly from the power and the rms voltage. Nothing needs to be calculated with the peak value.
**Formula:** $P = UI$, so $I = \dfrac{P}{U}$
**Conversions:** Not needed.
**Substitution:** $I = \dfrac{60\,\text{W}}{230\,\text{V}} = 0.2609\,\text{A}$
**Answer:** a) The student took the mains voltage to be a peak value and divided it by $\sqrt{2}$, although the voltage of the socket is already an rms value. The rms voltage is therefore $230\,\text{V}$, not $163\,\text{V}$, and with a voltage that is too small the current came out too large. b) The rms value of the current is $0.26\,\text{A}$, two significant figures like the power $60\,\text{W}$.
**Reasonableness:** Check: $230\,\text{V} \cdot 0.26\,\text{A} \approx 60\,\text{W}$. The student’s result $0.37\,\text{A}$ would have given a power of $230\,\text{V} \cdot 0.37\,\text{A} = 85\,\text{W}$, which is not $60\,\text{W}$.

## fy7-7-L3-01
**Given:** peak value of the voltage $e_0 = 20.0\,\text{V}$, at the moment $t = 0$ the plane of the coil is perpendicular to the field, the coil turns $30^\circ$ from this position
**Find:** the instantaneous value $e$ of the voltage in volts
**Principle:** When the plane of the coil is perpendicular to the field, the flux is at its greatest and does not change for a moment, so the voltage is zero. From then on the voltage grows like a sine, $e = e_0 \sin\theta$, where $\theta$ is the angle through which the coil has turned from this position. The voltage is at its peak value at the angle $90^\circ$, when the plane of the coil is parallel to the field.
**Formula:** $e = e_0 \sin\theta$
**Conversions:** Not needed.
**Substitution:** $e = 20.0\,\text{V} \cdot \sin 30^\circ = 20.0\,\text{V} \cdot 0.5 = 10.0\,\text{V}$
**Answer:** $10.0\,\text{V}$, three significant figures like the peak value $20.0\,\text{V}$.
**Reasonableness:** The angle $30^\circ$ is a third of the way from the position of zero voltage to the position of peak voltage, but the voltage is already half the peak value, because the sine curve rises most steeply at the start. A $17.3\,\text{V}$ calculated with the cosine would be wrong: it would give the greatest voltage in the position where the flux does not change.

## fy7-7-L3-02
**Given:** peak value of the generator's voltage $U_0 = 40\,\text{V}$, resistance $R = 40\,\Omega$, resistance of the generator negligible
**Find:** the average power $P$ of the resistor in watts
**Principle:** The resistance of the generator is negligible, so the whole voltage is across the resistor. The average power is calculated with rms values as with direct current: $P = UI$, and by Ohm's law $I = U : R$, so $P = U^2 : R$. A power calculated with the peak value would be only the instantaneous peak power.
**Formula:** $U = \dfrac{U_0}{\sqrt{2}}$ and $P = UI = \dfrac{U^2}{R} = \dfrac{U_0^2}{2R}$
**Conversions:** Not needed.
**Substitution:** $U = \dfrac{40\,\text{V}}{\sqrt{2}} = 28.28\,\text{V}$ and $P = \dfrac{(28.28\,\text{V})^2}{40\,\Omega} = \dfrac{800\,\text{V}^2}{40\,\Omega} = 20\,\text{W}$
**Answer:** $20\,\text{W}$, two significant figures like the voltage $40\,\text{V}$ and the resistance $40\,\Omega$.
**Reasonableness:** The instantaneous peak power is $U_0^2 : R = 1600\,\text{V}^2 : 40\,\Omega = 40\,\text{W}$, and the average is half of that, because the power varies between zero and the peak value. Units: $\tfrac{\text{V}^2}{\Omega} = \text{V} \cdot \text{A} = \text{W}$.

## fy7-7-L3-03
**Given:** rms voltage $U_1 = 690\,\text{V}$ at a rotation rate of $15$ revolutions per minute, new rotation rate $9.0$ revolutions per minute, magnets and coils the same
**Find:** the new rms voltage $U_2$ in volts
**Principle:** The peak voltage of a generator is $e_0 = NBA \cdot 2\pi f$. When $N$, $B$ and $A$ stay the same, the peak voltage, and with it the rms value $U = e_0 : \sqrt{2}$, are directly proportional to the rotation frequency. In a direct-drive turbine the generator rotates at the same rate as the rotor, so the frequency is proportional to the revolutions per minute of the rotor.
**Formula:** $\dfrac{U_2}{U_1} = \dfrac{f_2}{f_1}$, so $U_2 = U_1 \cdot \dfrac{f_2}{f_1}$
**Conversions:** Not needed: in the ratio the revolutions per minute cancel, so they need not be converted to hertz.
**Substitution:** $U_2 = 690\,\text{V} \cdot \dfrac{9.0}{15} = 690\,\text{V} \cdot 0.60 = 414\,\text{V}$
**Answer:** about $410\,\text{V}$, two significant figures like the rotation rates $15$ and $9.0$ revolutions per minute.
**Reasonableness:** The rotation rate fell by $40\,\%$, so the voltage also falls by $40\,\%$. The frequency of the voltage falls as well, which is why a wind turbine needs a frequency converter that matches both the voltage and the frequency to the grid.

## fy7-7-L3-04
**Given:** number of turns of the bottle dynamo $N = 240$, area $A = 6.0\,\text{cm}^2$, the six data points $(f, e_0)$ of the table
**Find:** a) the slope $k$ of the line $e_0 = kf + c$, b) the magnetic flux density $B$ and an explanation of why the line passes through the origin, c) the peak value at the frequency $22\,\text{Hz}$ and the significance of the constant term
**Principle:** The peak value $e_0 = NBA \cdot 2\pi f$ is a linear function of the rotation frequency, with slope $k = NBA \cdot 2\pi$. A line is fitted to the data points with the linear fit of a calculator (or by eye), and $B$ is solved from the slope. A coil that is not rotating gives zero voltage, so the line should pass through the origin. The roller of a bottle dynamo rotates against the tyre, and the frequency $f$ is the rotation frequency of the roller and the coil.
**Formula:** $k = NBA \cdot 2\pi$, so $B = \dfrac{k}{NA \cdot 2\pi}$
**Conversions:** $A = 6.0\,\text{cm}^2 = 6.0 \cdot 0.0001\,\text{m}^2 = 6.0 \cdot 10^{-4}\,\text{m}^2$
**Substitution:** a) Check with the two extreme points: $k \approx \dfrac{(9.1 - 1.4)\,\text{V}}{(30 - 5)\,\text{Hz}} = 0.308\,\tfrac{\text{V}}{\text{Hz}}$. The fit of the calculator gives $k = 0.308\,\tfrac{\text{V}}{\text{Hz}} = 0.308\,\text{V}\cdot\text{s}$ and $c = -0.107\,\text{V}$. b) $B = \dfrac{0.308\,\text{V}\cdot\text{s}}{240 \cdot 6.0 \cdot 10^{-4}\,\text{m}^2 \cdot 2\pi} = \dfrac{0.308\,\text{V}\cdot\text{s}}{0.9048\,\text{m}^2} = 0.3404\,\text{T}$. c) $e_0 = 0.308\,\tfrac{\text{V}}{\text{Hz}} \cdot 22\,\text{Hz} - 0.107\,\text{V} = 6.67\,\text{V}$; without the constant term the result would be $6.78\,\text{V}$.
**Answer:** b) $B \approx 0.34\,\text{T}$, two significant figures like the area of the coil. In the formula $e_0$ is directly proportional to the frequency, so the voltage should be zero when $f = 0$. The constant term $c = -0.11\,\text{V}$ is small and is probably due to measurement error, such as the zero point of the oscilloscope or the reading accuracy ($\pm 0.1\,\text{V}$). c) $e_0 \approx 6.7\,\text{V}$. The constant term changes the prediction by only $1.6\,\%$, so it does not matter.
**Reasonableness:** The field of a permanent magnet is typically a few tenths of a tesla, so $0.34\,\text{T}$ is believable. Check: at the frequency $30\,\text{Hz}$ the line gives the value $9.13\,\text{V}$, which matches the measured $9.1\,\text{V}$.

## fy7-7-L3-05
**Given:** $N = 120$, $A = 0.0050\,\text{m}^2$, $B = 0.20\,\text{T}$, resistor $R = 8.0\,\Omega$, resistance of the generator negligible, rotation frequencies $f_1 = 25\,\text{Hz}$ and $f_2 = 40\,\text{Hz}$
**Find:** a) the peak values $e_0$ and rms values $U$ at both frequencies, b) the average powers $P_1$ and $P_2$ of the resistor and the greatest instantaneous power $p_{\max}$ at the frequency $f_2$, c) an explanation for the growth of the power
**Principle:** The peak value is $e_0 = NBA \cdot 2\pi f$, and the rms value is $U = e_0 : \sqrt{2}$. The whole voltage is across the resistor, and the average power is $P = U^2 : R$. The instantaneous power $p = e^2 : R$ varies between zero and the peak value $e_0^2 : R$.
**Formula:** $e_0 = NBA \cdot 2\pi f$, $U = \dfrac{e_0}{\sqrt{2}}$, $P = \dfrac{U^2}{R}$ and $p_{\max} = \dfrac{e_0^2}{R}$
**Conversions:** Not needed: the quantities are in SI units.
**Substitution:** a) $NBA = 120 \cdot 0.20\,\text{T} \cdot 0.0050\,\text{m}^2 = 0.12\,\text{Wb}$. At the frequency $f_1$: $e_{0,1} = 0.12\,\text{Wb} \cdot 2\pi \cdot 25\,\text{Hz} = 18.85\,\text{V}$ and $U_1 = \dfrac{18.85\,\text{V}}{\sqrt{2}} = 13.33\,\text{V}$. At the frequency $f_2$: $e_{0,2} = 0.12\,\text{Wb} \cdot 2\pi \cdot 40\,\text{Hz} = 30.16\,\text{V}$ and $U_2 = \dfrac{30.16\,\text{V}}{\sqrt{2}} = 21.33\,\text{V}$. b) $P_1 = \dfrac{(13.33\,\text{V})^2}{8.0\,\Omega} = 22.2\,\text{W}$ and $P_2 = \dfrac{(21.33\,\text{V})^2}{8.0\,\Omega} = 56.8\,\text{W}$. The greatest instantaneous power is $p_{\max} = \dfrac{(30.16\,\text{V})^2}{8.0\,\Omega} = 113.7\,\text{W}$.
**Answer:** b) The average power is $P_2 \approx 57\,\text{W}$ at the rotation frequency $40\,\text{Hz}$, two significant figures like the values of the coil and the resistor. At the rotation frequency $25\,\text{Hz}$ the power is $22\,\text{W}$, and the greatest instantaneous power is $1.1 \cdot 10^{2}\,\text{W}$. c) The peak voltage is proportional to the frequency, and the power is proportional to the square of the voltage, so the power is proportional to the square of the frequency: $1.6^2 = 2.56$. The power therefore grows $2.56$-fold, not $1.6$-fold.
**Reasonableness:** Check: $P_2 : P_1 = 56.8\,\text{W} : 22.2\,\text{W} = 2.56$, which matches $1.6^2$. The average power $56.8\,\text{W}$ is half of the peak power $113.7\,\text{W}$, as it should be for a sinusoidal voltage. Units: $\tfrac{\text{V}^2}{\Omega} = \text{W}$.

## fy7-7-L1-09
**Find:** which of the four $(t, e)$ graphs shows the voltage of the generator when the effective value is $5.0\,\text{V}$ and the frequency is $40\,\text{Hz}$.
**Principle:** The effective value of a sinusoidal voltage is the peak value divided by $\sqrt{2}$, so the peak value seen in the graph is $e_0 = U\sqrt{2}$. The period is the reciprocal of the frequency, $T = 1 : f$.
**Model answer:** The correct one is graph B. The peak value:

$e_0 = 5.0\,\text{V} \cdot \sqrt{2}$

$e_0 \approx 7.1\,\text{V}$

The period:

$T = \dfrac{1}{40\,\text{Hz}}$

$T = 0.025\,\text{s} = 25\,\text{ms}$

The curve of graph B goes between $-7.1\,\text{V}$ and $7.1\,\text{V}$, and it is zero and increasing at the times $0$, $25\,\text{ms}$, $50\,\text{ms}$ and so on: between $0$ and $100\,\text{ms}$ it has four full periods. The period of graph C is correct, but its peak value is only $5.0\,\text{V}$: the effective value has been drawn as the peak value, which is a common mistake in this topic. The peak value of graph D is correct, but its period is $40\,\text{ms}$: the numerical value of the frequency has been read as the period in milliseconds. Graph A has both mistakes.

**Reading the graph:** The peak value is read from the height of the highest point of the curve, and the period from the distance between two successive zeros where the curve goes in the same direction. Reasonableness: a frequency of $40\,\text{Hz}$ means $40$ periods per second, that is $4$ periods in $100\,\text{ms}$.
