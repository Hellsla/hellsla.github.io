## fy7-16-L1-01
**Given:** attenuation coefficient $a = 0.18\,\text{dB/km}$, length of the fibre $L = 50\,\text{km}$
**Find:** the attenuation $A$ of the fibre in decibels
**Principle:** The fibre is uniform along its whole length, so every kilometre attenuates by the same number of decibels, and decibels are added. The attenuation of the whole fibre is the attenuation coefficient times the length.
**Formula:** $A = aL$
**Conversions:** Not needed: the kilometres cancel in the result, and the attenuation comes out in decibels.
**Substitution:** $A = 0.18\,\tfrac{\text{dB}}{\text{km}} \cdot 50\,\text{km} = 9.0\,\text{dB}$
**Answer:** $9.0\,\text{dB}$, two significant figures like the attenuation coefficient $0.18\,\text{dB/km}$.
**Reasonableness:** $9\,\text{dB}$ is a little less than $10\,\text{dB}$, so a little more than a tenth of the power is left. This fits the fact that the power halves over about $17\,\text{km}$: $50\,\text{km}$ is about three halvings, and $0.5^3 \approx 0.13$.

## fy7-16-L1-02
**Given:** power at the start $P_0 = 2.0\,\text{mW}$, power at the end $P = 0.50\,\text{mW}$
**Find:** the attenuation $A$ in decibels
**Principle:** The attenuation in decibels is defined as the base-ten logarithm of the ratio of the powers. The power decreases, so the ratio $P_0 : P$ is greater than one and the attenuation is positive.
**Formula:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$
**Conversions:** Not needed: both powers are in milliwatts, and the unit cancels.
**Substitution:** $A = 10\,\text{dB} \cdot \lg \dfrac{2.0\,\text{mW}}{0.50\,\text{mW}} = 10\,\text{dB} \cdot \lg 4.0 = 6.021\,\text{dB}$
**Answer:** $6.0\,\text{dB}$, two significant figures like the powers.
**Reasonableness:** The power falls to a quarter, that is it halves twice. One halving is about $3\,\text{dB}$, so two halvings are about $6\,\text{dB}$, as in the result.

## fy7-16-L1-03
**Given:** resistance of the eddy-current loop $R = 0.010\,\Omega$, effective value of the current $I = 400\,\text{A}$
**Find:** the power $P$ at which electrical energy changes into internal energy of the base, in kilowatts
**Principle:** The eddy current flows through the resistance of the base, and in a resistance electrical energy changes into internal energy at the power $RI^2$. For an alternating current the formula gives the mean power when $I$ is the effective value of the current (chapter *The generator and alternating current*).
**Formula:** $P = RI^2$
**Conversions:** Finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P = 0.010\,\Omega \cdot (400\,\text{A})^2 = 0.010\,\Omega \cdot 160\,000\,\text{A}^2 = 1600\,\text{W} = 1.6\,\text{kW}$
**Answer:** $1.6\,\text{kW}$, two significant figures like the resistance $0.010\,\Omega$.
**Reasonableness:** The power of the cooking zone of an induction hob is usually a few kilowatts, so $1.6\,\text{kW}$ is of the right order of magnitude. Units: $\Omega \cdot \text{A}^2 = \text{V} \cdot \text{A} = \text{W}$.

## fy7-16-L1-04
**Given:** peak value of the magnetic flux density $B_0 = 0.50\,\text{mT}$, area of one turn $A = 12\,\text{cm}^2$, field uniform and perpendicular to the plane of the coil
**Find:** the peak value $\Phi_0$ of the flux through one turn in microwebers
**Principle:** In a uniform field perpendicular to the surface the flux is the magnetic flux density times the area (chapter *Electromagnetic induction*). When the flux density is greatest, the flux is also greatest.
**Formula:** $\Phi = BA$, so $\Phi_0 = B_0 A$
**Conversions:** $B_0 = 0.50\,\text{mT} = 0.50 \cdot 10^{-3}\,\text{T}$ and $A = 12\,\text{cm}^2 = 12 \cdot (0.01\,\text{m})^2 = 1.2 \cdot 10^{-3}\,\text{m}^2$. Finally $1\,\text{Wb} = 10^{6}\,\mu\text{Wb}$.
**Substitution:** $\Phi_0 = 0.50 \cdot 10^{-3}\,\text{T} \cdot 1.2 \cdot 10^{-3}\,\text{m}^2 = 6.0 \cdot 10^{-7}\,\text{Wb} = 0.60\,\mu\text{Wb}$
**Answer:** $0.60\,\mu\text{Wb}$, two significant figures like the initial data.
**Reasonableness:** Units: $\text{T} \cdot \text{m}^2 = \text{Wb}$. The flux is small because both the field and the area are small; because of the high frequency even such a small flux induces volts in the coil.

## fy7-16-L1-05
**Given:** power taken by the charger $P_\text{in} = 10.0\,\text{W}$, power transferred to the battery $P_\text{battery} = 7.2\,\text{W}$
**Find:** the efficiency $\eta$ of the charging as a percentage
**Principle:** Efficiency is the share of the useful power in the power taken. Here the useful power is the power transferred to the battery; the rest changes into internal energy of the coils and electronics of the charger and the phone.
**Formula:** $\eta = \dfrac{P_\text{battery}}{P_\text{in}}$
**Conversions:** Not needed: both powers are in watts. Finally the ratio is multiplied by one hundred to give a percentage.
**Substitution:** $\eta = \dfrac{7.2\,\text{W}}{10.0\,\text{W}} = 0.72 = 72\,\%$
**Answer:** $72\,\%$, two significant figures like the power transferred to the battery, $7.2\,\text{W}$.
**Reasonableness:** The efficiency is below $100\,\%$, as it must be. The power wasted is $10.0\,\text{W} - 7.2\,\text{W} = 2.8\,\text{W}$, which shows in the fact that the charger and the phone get warm during charging.

## fy7-16-L2-01
**Given:** number of turns $N = 10$, frequency $f = 140\,\text{kHz}$, peak value of the flux through one turn $\Phi_0 = 0.40\,\mu\text{Wb}$
**Find:** the peak value $e_0$ of the induced voltage
**Principle:** The flux varies sinusoidally, so a sinusoidal voltage is induced in every turn, and its peak value is the peak value of the rate of change of the flux, $2\pi f \cdot \Phi_0$, as in a generator. The voltages of the turns add up.
**Formula:** $e_0 = N \cdot 2\pi f \cdot \Phi_0$
**Conversions:** $f = 140\,\text{kHz} = 140 \cdot 1000\,\text{Hz} = 1.40 \cdot 10^{5}\,\text{Hz}$ and $\Phi_0 = 0.40\,\mu\text{Wb} = 0.40 \cdot 10^{-6}\,\text{Wb}$
**Substitution:** $e_0 = 10 \cdot 2\pi \cdot 1.40 \cdot 10^{5}\,\text{Hz} \cdot 0.40 \cdot 10^{-6}\,\text{Wb} = 3.519\,\text{V}$
**Answer:** $3.5\,\text{V}$, two significant figures like the flux $0.40\,\mu\text{Wb}$.
**Reasonableness:** Units: $\text{Hz} \cdot \text{Wb} = \tfrac{1}{\text{s}} \cdot \text{V}\cdot\text{s} = \text{V}$. A voltage of a few volts is enough for the electronics of a phone, which rectifies it to charge the battery.

## fy7-16-L2-02
**Given:** transmitted power $P_0 = 1.0\,\text{mW}$, smallest power that can be received $P = 1.0\,\mu\text{W}$, attenuation coefficient $a = 0.20\,\text{dB/km}$
**Find:** the greatest length $L$ of the link in kilometres
**Principle:** The receiver detects the pulses when the power is at least $1.0\,\mu\text{W}$, so the greatest permitted attenuation follows from the ratio of the powers. The fibre is uniform along its whole length, so the attenuation is $A = aL$, and the length is solved from it.
**Formula:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ and $A = aL$, so $L = \dfrac{A}{a}$
**Conversions:** $P_0 = 1.0\,\text{mW} = 1.0 \cdot 10^{-3}\,\text{W}$ and $P = 1.0\,\mu\text{W} = 1.0 \cdot 10^{-6}\,\text{W}$
**Substitution:** $A = 10\,\text{dB} \cdot \lg \dfrac{1.0 \cdot 10^{-3}\,\text{W}}{1.0 \cdot 10^{-6}\,\text{W}} = 10\,\text{dB} \cdot \lg 1000 = 30\,\text{dB}$, so $L = \dfrac{30\,\text{dB}}{0.20\,\text{dB/km}} = 150\,\text{km}$
**Answer:** $150\,\text{km}$, that is $1.5 \cdot 10^{2}\,\text{km}$, two significant figures like the attenuation coefficient $0.20\,\text{dB/km}$.
**Reasonableness:** The power may fall to a thousandth, that is three times to a tenth, which is $3 \cdot 10\,\text{dB}$. When every $10\,\text{dB}$ needs $50\,\text{km}$ of fibre, the length is $150\,\text{km}$. This is of the same order of magnitude as the amplifier spacing of real links.

## fy7-16-L2-03
**Given:** power of the cooking zone $P = 2.0\,\text{kW}$, share transferred to the water $\eta = 85\,\%$, mass of water $m = 1.5\,\text{kg}$, initial temperature $15\,{}^\circ\text{C}$, final temperature $100\,{}^\circ\text{C}$, specific heat capacity of water from the table $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Find:** the heating time $t$ in minutes
**Principle:** The water stays liquid throughout the heating, so the energy it needs is $Q = cm\Delta T$. The eddy currents heat the base, and by assumption $85\,\%$ of the power taken by the hob is transferred to the water, so the power transferred to the water is $\eta P$. The time is the energy divided by the power.
**Formula:** $Q = cm\Delta T$ and $Q = \eta P t$, so $t = \dfrac{cm\Delta T}{\eta P}$
**Conversions:** $\Delta T = 100\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 85\,{}^\circ\text{C} = 85\,\text{K}$ (a temperature difference is the same in degrees Celsius and in kelvins), $P = 2.0\,\text{kW} = 2000\,\text{W}$ and $\eta = 85\,\% = 0.85$. Finally $1\,\text{min} = 60\,\text{s}$.
**Substitution:** $t = \dfrac{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 1.5\,\text{kg} \cdot 85\,\text{K}}{0.85 \cdot 2000\,\text{W}} = \dfrac{534\,225\,\text{J}}{1700\,\text{W}} = 314.3\,\text{s} = 5.238\,\text{min}$
**Answer:** $5.2\,\text{min}$, two significant figures like the power $2.0\,\text{kW}$ and the mass $1.5\,\text{kg}$.
**Reasonableness:** From experience, about a litre and a half of water boils on an induction hob in a few minutes. An estimate with round numbers: $4000 \cdot 1.5 \cdot 85 \approx 500\,000\,\text{J}$ and $500\,000\,\text{J} : 1700\,\text{W} \approx 300\,\text{s} = 5\,\text{min}$.

## fy7-16-L2-04
**Given:** from the measurement, the energy of the cable charger $E_1 = 14.26\,\text{Wh}$ and of the charging pad $E_2 = 21.01\,\text{Wh}$ per charge, $365$ charges a year
**Find:** the extra energy consumption $\Delta E$ of the charging pad in a year in kilowatt-hours
**Principle:** In every charge the pad takes $E_2 - E_1$ more energy from the wall socket than the cable charger. By assumption the phone is charged every day in the same way from empty to full, so the increase over a year is the increase of one charge times the number of charges.
**Formula:** $\Delta E = 365 \cdot (E_2 - E_1)$
**Conversions:** Finally $1\,\text{kWh} = 1000\,\text{Wh}$.
**Substitution:** $\Delta E = 365 \cdot (21.01\,\text{Wh} - 14.26\,\text{Wh}) = 365 \cdot 6.75\,\text{Wh} = 2463.75\,\text{Wh} = 2.464\,\text{kWh}$
**Answer:** $2.46\,\text{kWh}$, three significant figures like the difference $6.75\,\text{Wh}$.
**Reasonableness:** Estimate: about $7\,\text{Wh}$ a day is about $2.5\,\text{kWh}$ a year. For one person this is a small amount, about the same as a $1\,\text{kW}$ kettle uses in two and a half hours, but the combined waste of millions of phones is large.

## fy7-16-L3-01
**Given:** length of the cable $L = 1172\,\text{km}$, attenuation coefficient $a = 0.18\,\text{dB/km}$, greatest attenuation of one section $A_\text{max} = 20\,\text{dB}$
**Find:** the smallest number of amplifiers
**Principle:** The fibre is uniform along its whole length, so the attenuation of a section is $A = a\,l$, where $l$ is the length of the section. A section may be at most so long that the attenuation is $20\,\text{dB}$. Enough sections are needed to cover the whole cable, and because the transmitter and the receiver are at the ends, there is one amplifier fewer than there are sections.
**Formula:** $A_\text{max} = a\,l_\text{max}$, so $l_\text{max} = \dfrac{A_\text{max}}{a}$; the number of sections $k \ge \dfrac{L}{l_\text{max}}$ and the number of amplifiers $k - 1$
**Conversions:** Not needed: the lengths are in kilometres and the attenuations in decibels.
**Substitution:** $l_\text{max} = \dfrac{20\,\text{dB}}{0.18\,\text{dB/km}} = 111.1\,\text{km}$, so $\dfrac{L}{l_\text{max}} = \dfrac{1172\,\text{km}}{111.1\,\text{km}} = 10.55$. Thus $k = 11$ sections are needed, and $11 - 1 = 10$ amplifiers.
**Answer:** at least $10$ amplifiers. The number is a whole number, and the number of sections is rounded up, because $10$ sections would be too long.
**Reasonableness:** Without amplifiers the attenuation of the whole cable would be $0.18\,\text{dB/km} \cdot 1172\,\text{km} = 211\,\text{dB}$, and $211\,\text{dB} : 20\,\text{dB} \approx 10.5$ sections. The length of a section, $1172\,\text{km} : 11 = 107\,\text{km}$, is slightly above the typical amplifier spacing of $50$–$100\,\text{km}$ in real links.

## fy7-16-L3-02
**Given:** frequency $f = 25\,\text{kHz}$, peak value of the magnetic flux density $B_0 = 4.0\,\text{mT}$, radius of the loop $r = 8.0\,\text{cm}$, resistance of the loop $R = 0.050\,\Omega$, field uniform and perpendicular to the base
**Find:** the mean power $P$ at which the base heats up, in kilowatts
**Principle:** The flux $\Phi = BA$ through the loop varies sinusoidally, so a sinusoidal voltage is induced in the loop, with the peak value $e_0 = 2\pi f \cdot \Phi_0$, as in a one-turn generator (chapter *The generator and alternating current*). The electrical energy of the eddy current changes into internal energy in the resistance; the mean power is calculated from the effective voltage $U = e_0 : \sqrt{2}$.
**Formula:** $\Phi_0 = B_0 \cdot \pi r^2$, $e_0 = 2\pi f \cdot \Phi_0$, $U = \dfrac{e_0}{\sqrt{2}}$ and $P = \dfrac{U^2}{R}$, so $P = \dfrac{(2\pi f \cdot B_0 \cdot \pi r^2)^2}{2R}$
**Conversions:** $f = 25\,\text{kHz} = 25 \cdot 1000\,\text{Hz} = 2.5 \cdot 10^{4}\,\text{Hz}$, $B_0 = 4.0\,\text{mT} = 4.0 \cdot 10^{-3}\,\text{T}$ and $r = 8.0\,\text{cm} = 8.0 \cdot 0.01\,\text{m} = 0.080\,\text{m}$. Finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $e_0 = 2\pi \cdot 2.5 \cdot 10^{4}\,\text{Hz} \cdot 4.0 \cdot 10^{-3}\,\text{T} \cdot \pi \cdot (0.080\,\text{m})^2 = 12.63\,\text{V}$, so $P = \dfrac{(12.63\,\text{V})^2}{2 \cdot 0.050\,\Omega} = 1596\,\text{W} = 1.596\,\text{kW}$
**Answer:** $1.6\,\text{kW}$, two significant figures like the flux density $4.0\,\text{mT}$, the radius $8.0\,\text{cm}$ and the resistance $0.050\,\Omega$.
**Reasonableness:** The effective voltage is $12.63\,\text{V} : \sqrt{2} = 8.93\,\text{V}$ and the effective current $8.93\,\text{V} : 0.050\,\Omega = 179\,\text{A}$; the power $8.93\,\text{V} \cdot 179\,\text{A} \approx 1600\,\text{W}$ agrees. The result is of the order of magnitude of the power of a cooking zone; in reality the field of the eddy current itself reduces the current, so the result is an upper limit.

## fy7-16-L3-03
**Given:** transmitted power $P_0 = 1.0\,\text{mW}$, smallest power needed $P = 10\,\mu\text{W}$, attenuation coefficient $a = 0.20\,\text{dB/km}$, four splices each attenuating by $0.50\,\text{dB}$, refractive index of the glass $n = 1.47$, speed of light in a vacuum $c = 3.00 \cdot 10^8\,\text{m/s}$
**Find:** the travel time $t$ of a light pulse from end to end of the longest link, in milliseconds
**Principle:** The total attenuation of the link may be at most the amount given by the ratio of the powers. Decibels are added, so the part that is not used up by the splices is left for the fibre, and from it the greatest length is found. In glass light travels at the speed $v = c : n$ (chapter *Total internal reflection and optical fibre*), and a pulse travelling along the axis covers the length of the fibre.
**Formula:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, $A = aL + 4 \cdot 0.50\,\text{dB}$, so $L = \dfrac{A - 4 \cdot 0.50\,\text{dB}}{a}$, and $t = \dfrac{L}{v} = \dfrac{nL}{c}$
**Conversions:** $P_0 = 1.0\,\text{mW} = 1.0 \cdot 10^{-3}\,\text{W}$, $P = 10\,\mu\text{W} = 1.0 \cdot 10^{-5}\,\text{W}$; length $90\,\text{km} = 90 \cdot 1000\,\text{m}$; finally $1\,\text{s} = 1000\,\text{ms}$.
**Substitution:** $A = 10\,\text{dB} \cdot \lg \dfrac{1.0 \cdot 10^{-3}\,\text{W}}{1.0 \cdot 10^{-5}\,\text{W}} = 10\,\text{dB} \cdot \lg 100 = 20\,\text{dB}$, $L = \dfrac{20\,\text{dB} - 2.0\,\text{dB}}{0.20\,\text{dB/km}} = 90\,\text{km} = 90\,000\,\text{m}$, so $t = \dfrac{1.47 \cdot 90\,000\,\text{m}}{3.00 \cdot 10^8\,\text{m/s}} = 4.41 \cdot 10^{-4}\,\text{s} = 0.441\,\text{ms}$
**Answer:** $0.44\,\text{ms}$, two significant figures like the powers and the attenuation coefficient.
**Reasonableness:** Without splices the fibre could be $100\,\text{km}$, so the splices shorten the link a little, as they should. In glass light travels about $200\,\text{km}$ in a millisecond, so $90\,\text{km}$ takes a little less than half a millisecond.
