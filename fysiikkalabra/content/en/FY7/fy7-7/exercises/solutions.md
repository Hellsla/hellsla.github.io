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
**Answer:** $25\,\text{Hz}$; the reading $1500$ revolutions per minute is exact, so the result is exactly $25\,\text{Hz}$.
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
