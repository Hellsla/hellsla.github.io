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

## fy7-16-L1-06
**Find:** why the glass plate of an induction hob does not heat up by itself, even though the magnetic field of the coil passes through it
**Principle:** In an induction hob the coil produces a changing magnetic field, and a changing flux induces eddy currents in a conducting object. The eddy currents change electrical energy into internal energy in a resistance at the power $RI^2$. Heating therefore requires that an electric current can flow in the object.
**Model answer:** Glass does not conduct electricity, so no eddy currents arise in it to change electrical energy into internal energy. The option saying that glass blocks the magnetic field is wrong, because the field passes through the glass and heats the base of the pan. The option saying that the melting point prevents heating is wrong, because heating depends on the current and not on the melting point. The option saying that the eddy currents cancel each other according to Lenz’s law is wrong, because Lenz’s law gives the direction of the current and does not remove the current.

## fy7-16-L1-07
**Given:** power at the start $P_0 = 4.0\,\text{mW}$, attenuation coefficient $a = 0.20\,\text{dB/km}$, length $L = 45\,\text{km}$
**Find:** the power $P$ at the end of the fibre in milliwatts
**Principle:** The fibre is uniform along its whole length, so the attenuation is calculated with the formula $A = aL$. After that the ratio of the powers follows from the definition of attenuation, and the power $P$ is solved.
**Formula:** $A = aL$ and $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, so $P = P_0 \cdot 10^{-A / (10\,\text{dB})}$
**Conversions:** Not needed: the power stays in milliwatts, because the ratio $P : P_0$ has no unit.
**Substitution:** $A = 0.20\,\tfrac{\text{dB}}{\text{km}} \cdot 45\,\text{km} = 9.0\,\text{dB}$, so $P = 4.0\,\text{mW} \cdot 10^{-9.0 / 10} = 4.0\,\text{mW} \cdot 0.1259 = 0.5036\,\text{mW}$
**Answer:** $0.50\,\text{mW}$, two significant figures like the initial data.
**Reasonableness:** The attenuation $9.0\,\text{dB}$ is about three times $3\,\text{dB}$, so the power halves three times: $4.0\,\text{mW} : 8 = 0.50\,\text{mW}$, as in the result. The power has not fallen to a tenth, because $9\,\text{dB}$ is less than $10\,\text{dB}$.

## fy7-16-L1-08
**Given:** attenuation coefficient $a = 0.20\,\text{dB/km}$, the power halves, that is $P_0 : P = 2$
**Find:** the distance $L$ in kilometres over which the power halves
**Principle:** Halving means a power ratio of $2$, which gives the attenuation in decibels. The fibre is uniform along its whole length, so the attenuation is $A = aL$, and the distance is solved from it.
**Formula:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ and $A = aL$, so $L = \dfrac{A}{a}$
**Conversions:** Not needed: the attenuation is in decibels and the attenuation coefficient in decibels per kilometre.
**Substitution:** $A = 10\,\text{dB} \cdot \lg 2 = 3.010\,\text{dB}$, so $L = \dfrac{3.010\,\text{dB}}{0.20\,\text{dB/km}} = 15.05\,\text{km}$
**Answer:** $15\,\text{km}$, two significant figures like the attenuation coefficient $0.20\,\text{dB/km}$.
**Reasonableness:** Halving corresponds to about $3\,\text{dB}$, and the fibre attenuates by $0.20\,\text{dB}$ per kilometre, so $3 : 0.2 = 15$ kilometres. The power halves about every $15\,\text{km}$, so over a distance of $45\,\text{km}$ it halves three times.

## fy7-16-L2-05
**Given:** the measurement points $(d;\ \eta)$ of the table, the limit $\eta = 50\,\%$
**Find:** the distance $d$ at which the efficiency falls to $50\,\%$, in millimetres
**Principle:** As the distance grows, the flux through the receiver coil decreases steeply, so the efficiency falls. The limit $50\,\%$ lies between the measurements $58\,\%$ and $44\,\%$, so the distance is found from the graph or by linear interpolation between these two points.
**Reading the graph:** Plot the points $(3;\ 81)$, $(6;\ 73)$, $(10;\ 58)$, $(15;\ 44)$, $(20;\ 31)$ and $(25;\ 22)$ and join them with a smooth curve. Draw a horizontal line at the height $50\,\%$. The curve crosses it between the points $d = 10\,\text{mm}$ and $d = 15\,\text{mm}$, a little past the middle, that is above $12.5\,\text{mm}$.
**Formula:** $d = d_1 + (d_2 - d_1) \cdot \dfrac{\eta_1 - 50\,\%}{\eta_1 - \eta_2}$, where $(d_1;\ \eta_1)$ and $(d_2;\ \eta_2)$ are the measurement points on either side of the limit
**Conversions:** Not needed: the distances are in millimetres and the efficiencies in percent, and the units cancel in the ratio.
**Substitution:** $d = 10\,\text{mm} + 5\,\text{mm} \cdot \dfrac{58\,\% - 50\,\%}{58\,\% - 44\,\%} = 10\,\text{mm} + 5\,\text{mm} \cdot 0.571 = 12.86\,\text{mm}$
**Answer:** $13\,\text{mm}$, two significant figures. The measurement was made with a precision of about a millimetre, so a value of $12$–$13\,\text{mm}$ read from the graph is just as good (a smooth curve runs a little lower than the linear interval).
**Reasonableness:** The efficiency $50\,\%$ is closer to $44\,\%$ than to $58\,\%$ (differences of $6$ and $8$ percentage points), so the result is a little past the middle, that is above $12.5\,\text{mm}$, as it should be. The efficiency falls over every interval, which fits the fact that the flux weakens as the distance grows.

## fy7-16-L2-06
**Given:** initial power $P_0 = 800\,\mu\text{W}$, the lengths $L$ and powers $P$ of the table
**Find:** the attenuation coefficient $a$ in the unit $\text{dB/km}$
**Principle:** The fibre is uniform along its whole length, so the attenuation grows in direct proportion to the length: $A = aL$. When $A$ is plotted as a function of the length $L$, the points lie on a straight line through the origin whose slope is $a$. The line goes through the origin because a fibre of zero length has no attenuation.
**Reading the graph:** The attenuations are $A = 2.15;\ 3.89;\ 6.11;\ 7.93;\ 10.05\,\text{dB}$ at the lengths $10;\ 20;\ 30;\ 40;\ 50\,\text{km}$. In real measurements the points are not exactly on one line, so the line is drawn between the points. The fitted line goes through the points $(0;\ 0)$ and $(50;\ 10.0)$.
**Formula:** $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ and $A = aL$, so the slope of the line is $a = \dfrac{\Delta A}{\Delta L}$
**Conversions:** Not needed: the powers are in microwatts and their ratio has no unit.
**Substitution:** For example at the length $10\,\text{km}$: $A = 10\,\text{dB} \cdot \lg \dfrac{800\,\mu\text{W}}{488\,\mu\text{W}} = 2.15\,\text{dB}$. The slope is $a = \dfrac{10.0\,\text{dB} - 0}{50\,\text{km} - 0} = 0.200\,\text{dB/km}$. The least-squares line through the origin gives the slope $0.2003\,\text{dB/km}$.
**Answer:** $0.20\,\text{dB/km}$, two significant figures; the power was measured with three significant figures, but the scatter of the points limits the result.
**Reasonableness:** The ratios $A : L$ of the individual points are between $0.194$ and $0.215\,\text{dB/km}$, so $0.20\,\text{dB/km}$ is in the middle of them. The value is typical of a telecommunications fibre, whose attenuation coefficient is of the order of $0.2\,\text{dB/km}$.

## fy7-16-L2-07
**Given:** attenuation $A = 20\,\text{dB}$; the student’s claim: the power decreases by $20\,\%$ and $80\,\%$ arrives
**Find:** a) the error in the student’s reasoning; b) the share of the transmitted power that arrives, as a percentage
**Principle:** The decibel is a logarithmic unit, not a percentage. The attenuation $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$ gives the ratio of the powers as a power of ten, and every $10\,\text{dB}$ reduces the power to a tenth. Therefore $20\,\text{dB}$ is a reduction to a tenth twice.
**Formula:** $\dfrac{P}{P_0} = 10^{-A / (10\,\text{dB})}$
**Conversions:** Finally the ratio is multiplied by one hundred to give percent.
**Substitution:** $\dfrac{P}{P_0} = 10^{-20\,\text{dB} / (10\,\text{dB})} = 10^{-2} = 0.010$, so $0.010 \cdot 100\,\% = 1.0\,\%$ arrives
**Answer:** a) The error is that decibels were interpreted as percentages. Decibels are added and the ratios of the powers are multiplied: two $10\,\text{dB}$ parts reduce the power to a tenth twice. b) $1.0\,\%$ of the transmitted power arrives. The student’s value $80\,\%$ would correspond to an attenuation of only about $1\,\text{dB}$.
**Reasonableness:** The attenuation $20\,\text{dB}$ is $2 \cdot 10\,\text{dB}$, so the power is $\tfrac{1}{10} \cdot \tfrac{1}{10} = \tfrac{1}{100}$, that is $1\,\%$. Checking the student’s value: $10\,\text{dB} \cdot \lg \dfrac{1}{0.80} = 0.97\,\text{dB}$, so $80\,\%$ would correspond to an attenuation of about $1\,\text{dB}$ and not $20\,\text{dB}$.

## fy7-16-L2-08
**Find:** the order of magnitude of the round-trip time $t$ of a light pulse in a $1200\,\text{km}$ fibre link.
**Principle:** Light travels in the core of the fibre at the speed $v = c : n$. Because the light travels almost parallel to the axis, the distance it covers is practically the length of the fibre. The distance covered back and forth is twice the length of the link, and the time is the distance divided by the speed. The length is converted into metres first, so that the units match the speed.
**Model answer:** The speed of light in the fibre and the distance back and forth:

$$\begin{aligned}
&v = \frac{3.00 \cdot 10^8\,\text{m/s}}{1.47} \\
&v = 2.04 \cdot 10^8\,\text{m/s} \\[6pt]
&s = 2 \cdot 1.2 \cdot 10^6\,\text{m} \\
&s = 2.4 \cdot 10^6\,\text{m}
\end{aligned}$$

The travel time:

$$\begin{aligned}
&t = \frac{s}{v} = \frac{2.4 \cdot 10^6\,\text{m}}{2.04 \cdot 10^8\,\text{m/s}} \\
&t = 0.0118\,\text{s}
\end{aligned}$$

The round-trip time is about $12\,\text{ms}$, that is of the order of ten milliseconds. Check: every kilometre delays the signal by about $4.9\,\mu\text{s}$, and $2400 \cdot 4.9\,\mu\text{s} \approx 11.8\,\text{ms}$.

The wrong orders of magnitude come from unit errors. If the length is substituted as the number of kilometres, the result is a thousand times too small, about $12\,\mu\text{s}$. If $1200\,\text{km}$ is written as $1.2 \cdot 10^5\,\text{m}$, the result is ten times too small. If the speed is taken as $300\,000$, that is the speed in kilometres per second, and the length in metres, the result is a thousand times too large, about $12\,\text{s}$.

## fy7-16-L3-04
**Given:** $N = 15$, $f = 130\,\text{kHz}$, $d$ and $e_0$ of the table, the charging limit $e_0 = 1.0\,\text{V}$, new frequency $f' = 100\,\text{kHz}$ and the same flux
**Find:** the greatest distance $d$ in millimetres at which charging works at the frequency $100\,\text{kHz}$
**Principle:** The flux varies sinusoidally, so $e_0 = N \cdot 2\pi f \cdot \Phi_0$. The flux at each distance is calculated from the voltages of the table. The voltage $1.0\,\text{V}$ at the frequency $100\,\text{kHz}$ requires a certain flux, and the distance is found by interpolation.
**Formula:** $\Phi_0 = \dfrac{e_0}{N \cdot 2\pi f}$, $\Phi_{\min} = \dfrac{1.0\,\text{V}}{N \cdot 2\pi f'}$ and $d = d_1 + (d_2 - d_1) \cdot \dfrac{\Phi_1 - \Phi_{\min}}{\Phi_1 - \Phi_2}$
**Conversions:** $f = 1.30 \cdot 10^{5}\,\text{Hz}$, $f' = 1.00 \cdot 10^{5}\,\text{Hz}$ and $1\,\text{Wb} = 10^{6}\,\mu\text{Wb}$.
**Substitution:** a) The denominator is $15 \cdot 2\pi \cdot 1.30 \cdot 10^{5}\,\text{Hz} = 1.225 \cdot 10^{7}\,\text{Hz}$, so the fluxes are $0.377;\ 0.221;\ 0.124;\ 0.0677;\ 0.0384\,\mu\text{Wb}$ at the distances $4;\ 8;\ 12;\ 16;\ 20\,\text{mm}$.
b) $\Phi_{\min} = \dfrac{1.0\,\text{V}}{15 \cdot 2\pi \cdot 1.00 \cdot 10^{5}\,\text{Hz}} = 0.1061\,\mu\text{Wb}$ is between the flux values $0.1241\,\mu\text{Wb}$ ($12\,\text{mm}$) and $0.0677\,\mu\text{Wb}$ ($16\,\text{mm}$): $d = 12\,\text{mm} + 4\,\text{mm} \cdot \dfrac{0.1241 - 0.1061}{0.1241 - 0.0677} = 13.28\,\text{mm}$
**Answer:** $13\,\text{mm}$, two significant figures; the interpolation is an estimate, because the flux does not decrease linearly. c) The same flux varies more slowly at the frequency $100\,\text{kHz}$ than at $130\,\text{kHz}$, so the induced voltage is smaller. The limit $1.0\,\text{V}$ is exceeded only with a greater flux, that is closer to the charger. The distance could be restored by adding turns to the receiver coil, because the voltage is directly proportional to the number of turns.
**Reasonableness:** The limit value $0.1061\,\mu\text{Wb}$ is smaller than the flux at the distance $12\,\text{mm}$ but greater than at the distance $16\,\text{mm}$, so $13.3\,\text{mm}$ is between them. At the frequency $130\,\text{kHz}$ the limit value would be $0.0816\,\mu\text{Wb}$ and the distance about $15.0\,\text{mm}$, so lowering the frequency shortens the working distance, as in part c. Increasing the turns from $15$ to $20$ would raise the voltage by the factor $1.33$ and would make up for the drop in frequency by the factor $1.30$.

## fy7-16-L3-05
**Given:** $f = 30\,\text{kHz}$, $B_0 = 3.0\,\text{mT}$, $r = 9.0\,\text{cm}$, $R_\text{A} = 0.040\,\Omega$, $R_\text{B} = 0.050\,\Omega$, $R_\text{C} = 0.080\,\Omega$, field uniform and perpendicular to the base
**Find:** the frequency $f_\text{C}$ in kilohertz at which the base of pan C heats up at the same power as the base of pan A at $30\,\text{kHz}$
**Principle:** The flux $\Phi = BA$ of the loop varies sinusoidally, so the peak voltage is $e_0 = 2\pi f \cdot \Phi_0$ and the power is $P = U^2 : R$ with the effective voltage $U = e_0 : \sqrt{2}$. The peak voltage is directly proportional to the frequency, so the power is directly proportional to the square of the frequency and inversely proportional to the resistance.
**Formula:** $\Phi_0 = B_0 \cdot \pi r^2$, $e_0 = 2\pi f \cdot \Phi_0$ and $P = \dfrac{e_0^2}{2R} \sim \dfrac{f^2}{R}$. Equal powers: $\dfrac{f_\text{C}^2}{R_\text{C}} = \dfrac{f^2}{R_\text{A}}$, so $f_\text{C} = f \cdot \sqrt{\dfrac{R_\text{C}}{R_\text{A}}}$
**Conversions:** $f = 3.0 \cdot 10^{4}\,\text{Hz}$, $B_0 = 3.0 \cdot 10^{-3}\,\text{T}$, $r = 0.090\,\text{m}$ and $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** a) $\Phi_0 = 3.0 \cdot 10^{-3}\,\text{T} \cdot \pi \cdot (0.090\,\text{m})^2 = 7.63 \cdot 10^{-5}\,\text{Wb}$ and $e_0 = 2\pi \cdot 3.0 \cdot 10^{4}\,\text{Hz} \cdot 7.63 \cdot 10^{-5}\,\text{Wb} = 14.39\,\text{V}$. The powers $P = \dfrac{(14.39\,\text{V})^2}{2R}$ are $2.59\,\text{kW}$ for pan A, $2.07\,\text{kW}$ for B and $1.29\,\text{kW}$ for C.
b) $f_\text{C} = 30\,\text{kHz} \cdot \sqrt{\dfrac{0.080\,\Omega}{0.040\,\Omega}} = 30\,\text{kHz} \cdot \sqrt{2} = 42.43\,\text{kHz}$
**Answer:** $42\,\text{kHz}$, two significant figures like the initial data. The resistance of pan C is double, so its power is half; raising the frequency increases the rate of change of the flux and the voltage, and the power grows as the square of the frequency. c) The magnetic field of the eddy current itself was ignored: according to Lenz’s law it opposes the change of flux, so the real current and power are smaller than the model gives. In a base that conducts very well (aluminium, copper) the field of the eddy current itself cancels a large part of the flux, so the model does not apply to them; the ferromagnetism of steel, on the other hand, increases the heating.
**Reasonableness:** The ratio of the powers $2.59\,\text{kW} : 1.29\,\text{kW} = 2.0$ corresponds to the ratio of the resistances $0.080 : 0.040 = 2.0$. Raising the frequency by the factor $\sqrt{2} = 1.414$ increases the power by the factor $1.414^2 = 2.0$, so the power of pan C at the frequency $42.4\,\text{kHz}$ is $1.29\,\text{kW} \cdot 2.0 = 2.59\,\text{kW}$.

## fy7-16-L2-09
**Given:** $e_0 = 4.2\,\text{V}$ at $3\,\text{mm}$, the frequency, the number of turns and the current of the transmitter coil do not change, the numbers of lines to be read from the figure
**Find:** the peak voltage $e_0'$ at $6\,\text{mm}$ in volts
**Principle:** The peak voltage is $e_0 = N \cdot 2\pi f \cdot \Phi_0$. When $N$ and $f$ stay the same, $e_0$ is proportional to the flux $\Phi_0$. The field lines of the figure are drawn at equal flux steps, so the number $n$ of lines passing through the receiver coil is proportional to the flux and therefore to the voltage.
**Reading the graph:** Count the darker lines that pass through the receiver coil. On the left ($3\,\text{mm}$) there are $6$ and on the right ($6\,\text{mm}$) $4$.
**Formula:** $\dfrac{e_0'}{e_0} = \dfrac{\Phi_0'}{\Phi_0} = \dfrac{n'}{n}$, so $e_0' = e_0 \cdot \dfrac{n'}{n}$
**Conversions:** Not needed: the ratio of the numbers of lines has no unit, and the voltage stays in volts.
**Substitution:** $e_0' = 4.2\,\text{V} \cdot \dfrac{4}{6} = 2.8\,\text{V}$
**Answer:** $2.8\,\text{V}$, two significant figures like the given voltage. Counting lines is rough, so the value is approximate.
**Reasonableness:** The phone is farther away and the flux is smaller, so the voltage falls: $2.8\,\text{V}$ is less than $4.2\,\text{V}$. The flux falls by a third over only $3\,\text{mm}$ more, which fits the efficiency measurements of the chapter falling steeply within a few millimetres.

## fy7-16-L2-10
**Given:** the curve of the graph $P : P_0$ as a function of the length $L$, the length of the new fibre $L = 70\,\text{km}$
**Find:** the attenuation coefficient $a$ and the power $P : P_0$ as a percentage at the length $70\,\text{km}$
**Principle:** The fibre is the same along its whole length, so $A = aL$, and the attenuation tells the power ratio: $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$. When the power has halved, $P_0 : P = 2$, so the attenuation is known without the numerical powers. The attenuation coefficient is obtained by dividing it by the length needed for the halving.
**Reading the graph:** Draw a horizontal line at the height $50\,\%$ and go straight down from its crossing with the curve to the horizontal axis. The point is $L_{1/2} = 10\,\text{km}$. The graph ends at $40\,\text{km}$, so the asked length $70\,\text{km}$ is calculated with the attenuation coefficient, not read from the graph.
**Formula:** $a = \dfrac{10\,\text{dB} \cdot \lg 2}{L_{1/2}}$, $A = aL$ and $\dfrac{P}{P_0} = 10^{-A / (10\,\text{dB})}$
**Conversions:** Not needed: the lengths are in kilometres and the attenuation coefficient is calculated in $\text{dB/km}$.
**Substitution:** $a = \dfrac{10\,\text{dB} \cdot 0.301}{10\,\text{km}} = 0.301\,\text{dB/km}$. At the length $70\,\text{km}$: $A = 0.301\,\text{dB/km} \cdot 70\,\text{km} = 21.07\,\text{dB}$ and $\dfrac{P}{P_0} = 10^{-21.07 / 10} = 0.00782 = 0.78\,\%$.
**Answer:** $0.78\,\%$, two significant figures; the attenuation coefficient is about $0.30\,\text{dB/km}$.
**Reasonableness:** The length $70\,\text{km}$ is $7$ halving distances, so the power is $0.5^{7} = 0.0078$, that is $0.78\,\%$. The graph ends at $40\,\text{km}$, where about $6\,\%$ remains, so a smaller value at $70\,\text{km}$ is right.