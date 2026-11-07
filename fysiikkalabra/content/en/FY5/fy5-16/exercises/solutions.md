## fy5-16-L1-01
**Given:** noise level $L = 91\,\text{dB}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the daily reference time $t_\text{ref}$ in hours
**Principle:** Noise exposure is calculated as an average of energy: every rise of $3\,\text{dB}$ doubles the intensity, so the same dose is reached in half the time.
**Formula:** $t_\text{ref} = \dfrac{t_0}{2^{\,n}}$, where $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Conversions:** Not needed: the levels are in decibels and the time comes out in hours.
**Substitution:** $n = \dfrac{91\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 2$, $t_\text{ref} = \dfrac{8\,\text{h}}{2^2} = 2.0\,\text{h}$
**Answer:** $2.0\,\text{h}$. The levels are whole decibels and the rule is an estimate, so two significant figures are enough.
**Reasonableness:** Two halvings: $8\,\text{h} \to 4\,\text{h} \to 2\,\text{h}$. The intensity is four times as great, and $4 \cdot 2\,\text{h} = 8\,\text{h}$, so the dose is the same as in the reference.

## fy5-16-L1-02
**Given:** level of one fan $L_1 = 70\,\text{dB}$; two identical fans
**Find:** the combined level $L$ in decibels
**Principle:** The intensities of two sources add, not the levels. Two equally strong sources double the intensity (chapter *Intensity and the decibel scale*).
**Formula:** $L = L_1 + 10\,\text{dB} \cdot \lg \dfrac{2 I_1}{I_1} = L_1 + 10\,\text{dB} \cdot \lg 2$
**Conversions:** Not needed.
**Substitution:** $L = 70\,\text{dB} + 10\,\text{dB} \cdot \lg 2 = 70\,\text{dB} + 3.01\,\text{dB} = 73.01\,\text{dB}$
**Answer:** $73\,\text{dB}$, in whole decibels like the given value.
**Reasonableness:** The level rises only a little even though the number of noisy devices doubles. A result of $140\,\text{dB}$ would be above the threshold of pain, which does not suit two fans.

## fy5-16-L1-03
**Given:** $L_1 = 88\,\text{dB}$ at a distance $r_1 = 4.0\,\text{m}$, new distance $r_2 = 8.0\,\text{m}$; point source in an open space
**Find:** the level $L_2$ at the distance $r_2$
**Principle:** The intensity of a point source is inversely proportional to the square of the distance, so double the distance gives a quarter of the intensity. That lowers the level by $10\,\text{dB} \cdot \lg 4 \approx 6\,\text{dB}$ (chapter *Intensity and the decibel scale*).
**Formula:** $L_2 = L_1 - 6\,\text{dB}$, when $r_2 = 2 r_1$
**Conversions:** Not needed: $r_2 : r_1 = 8.0\,\text{m} : 4.0\,\text{m} = 2$.
**Substitution:** $L_2 = 88\,\text{dB} - 6\,\text{dB} = 82\,\text{dB}$
**Answer:** $82\,\text{dB}$, in whole decibels like the given value.
**Reasonableness:** The level decreases but stays of the same order of magnitude: a quarter of the intensity is not a quarter of the decibel number. In a reflective space the drop would be smaller.

## fy5-16-L1-04
**Given:** noise level $L_\text{noise} = 106\,\text{dB}$, attenuation of the protectors $\Delta L = 23\,\text{dB}$
**Find:** the level $L$ reaching the ear
**Principle:** The attenuation of a hearing protector tells by how many decibels it lowers the level reaching the ear, so the attenuation is subtracted from the noise level.
**Formula:** $L = L_\text{noise} - \Delta L$
**Conversions:** Not needed.
**Substitution:** $L = 106\,\text{dB} - 23\,\text{dB} = 83\,\text{dB}$
**Answer:** $83\,\text{dB}$, in whole decibels like the given values.
**Reasonableness:** The level stays below the upper action value $85\,\text{dB}$, so the dose of the upper action value is not reached during the working day if the protectors are well fitted and worn all the time. The level is still above the lower action value $80\,\text{dB}$, and staying below the reference dose does not guarantee safe hearing. Without protectors the reference time would be about $4\,\text{min}$.

## fy5-16-L1-05
**Find:** whether each measure belongs to the source, the path or the ear
**Principle:** At the source the sound produced is reduced, along the path the travel of sound from the source to the listener is blocked or dampened, and at the ear the sound reaching the ear is reduced.
**Model answer:** a) A noise barrier stops the direct sound between the road and the homes, so it is a measure along the path. b) A casing encloses the sound right around the machine, so it controls noise at the source. c) Earplugs attenuate sound only at the ear. d) Panels fitted in the ceiling do not make the machine quieter, but they absorb the reflections through which the sound travels to the worker, so they are a measure along the path.

## fy5-16-L2-01
**Given:** two identical machines, each $L_1 = 85\,\text{dB}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the daily reference time $t_\text{ref}$ in hours
**Principle:** The intensities of two equally strong sources add, so the intensity doubles and the level rises by about $3\,\text{dB}$. Then every $3\,\text{dB}$ above the action value halves the reference time.
**Formula:** $L = L_1 + 3\,\text{dB}$ and $t_\text{ref} = \dfrac{t_0}{2^{\,n}}$, where $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Conversions:** Not needed.
**Substitution:** $L = 85\,\text{dB} + 3\,\text{dB} = 88\,\text{dB}$, $n = \dfrac{88\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 1$, $t_\text{ref} = \dfrac{8\,\text{h}}{2^1} = 4.0\,\text{h}$
**Answer:** $4.0\,\text{h}$. The rule is an estimate, so two significant figures are enough.
**Reasonableness:** The second machine brings as much energy again, so the total energy builds up twice as fast and the dose is reached in half the time. The result is consistent: $2 \cdot 4\,\text{h} = 8\,\text{h}$.

## fy5-16-L2-02
**Given:** level at the ear $L = 94\,\text{dB}$, listening time $t = 1.5\,\text{h}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the dose as a percentage of the reference dose
**Principle:** First calculate the reference time at a level of $94\,\text{dB}$: in that time exactly the reference dose builds up. The share of the dose is the ratio of the listening time to the reference time, because the level is the same all the time.
**Formula:** $t_\text{ref} = \dfrac{t_0}{2^{\,n}}$, where $n = \dfrac{L - L_0}{3\,\text{dB}}$, and share $= \dfrac{t}{t_\text{ref}} \cdot 100\,\%$
**Conversions:** Not needed: the times are in hours, and the unit cancels.
**Substitution:** $n = \dfrac{94\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 3$, $t_\text{ref} = \dfrac{8\,\text{h}}{2^3} = 1.0\,\text{h}$, share $= \dfrac{1.5\,\text{h}}{1.0\,\text{h}} \cdot 100\,\% = 150\,\%$
**Answer:** $150\,\%$, two significant figures as in the time $1.5\,\text{h}$.
**Reasonableness:** The listening time is longer than the reference time, so the dose exceeds the reference, that is, more than $100\,\%$ is expected. If the sound were lowered by $3\,\text{dB}$, the dose would be halved to $75\,\%$.

## fy5-16-L2-03
**Given:** $L_1 = 78\,\text{dB}$ at a distance $r_1 = 2.0\,\text{m}$, desired level $L_2 = 60\,\text{dB}$; point source in an open space
**Find:** the distance $r_2$ in metres
**Principle:** In an open space every doubling of the distance lowers the level by $6\,\text{dB}$, because the intensity falls to a quarter (chapter *Intensity and the decibel scale*). We calculate how many doublings are needed.
**Formula:** $k = \dfrac{L_1 - L_2}{6\,\text{dB}}$ and $r_2 = 2^{\,k} \cdot r_1$
**Conversions:** Not needed.
**Substitution:** $k = \dfrac{78\,\text{dB} - 60\,\text{dB}}{6\,\text{dB}} = 3$, $r_2 = 2^3 \cdot 2.0\,\text{m} = 16\,\text{m}$
**Answer:** $16\,\text{m}$, two significant figures as in the distance $2.0\,\text{m}$.
**Reasonableness:** The distances $2\,\text{m}$, $4\,\text{m}$, $8\,\text{m}$ and $16\,\text{m}$ give the levels $78\,\text{dB}$, $72\,\text{dB}$, $66\,\text{dB}$ and $60\,\text{dB}$. In a yard the walls of houses reflect sound, so in reality a slightly longer distance would be needed.

## fy5-16-L2-04
**Given:** the level falls from $L_1 = 92\,\text{dB}$ to $L_2 = 62\,\text{dB}$ in a time $\Delta t = 0.45\,\text{s}$; the fall is steady
**Find:** the reverberation time $T$, that is, the time in which the level falls by $60\,\text{dB}$
**Principle:** When the level falls steadily, it falls by the same number of decibels every second. The reverberation time follows from the rate of fall: a fall of $60\,\text{dB}$ takes as many times longer as the measured fall is smaller. The measurement is often done this way, because the background noise of the room hides the full drop of $60\,\text{dB}$.
**Formula:** $T = \dfrac{60\,\text{dB}}{L_1 - L_2} \cdot \Delta t$
**Conversions:** Not needed.
**Substitution:** $T = \dfrac{60\,\text{dB}}{92\,\text{dB} - 62\,\text{dB}} \cdot 0.45\,\text{s} = 2 \cdot 0.45\,\text{s} = 0.90\,\text{s}$
**Answer:** $0.90\,\text{s}$, two significant figures as in the time $0.45\,\text{s}$.
**Reasonableness:** The measured fall of $30\,\text{dB}$ is half of $60\,\text{dB}$, so the time doubles. The result is longer than the roughly half a second aimed for in classrooms, which suits an empty classroom with hard surfaces.

## fy5-16-L2-08
**Find:** which conclusion the noise level measurements of the compressor at four distances support, when the uncertainty of a reading is $\Delta L = 1\,\text{dB}$
**Principle:** In an open space the intensity of a point source is inversely proportional to the square of the distance. When the distance doubles, the intensity drops to a quarter and the level decreases by $10\,\text{dB} \cdot \lg 4 \approx 6.0\,\text{dB}$. The uncertainty of the difference of two readings is at most $2\Delta L = 2\,\text{dB}$, so differences smaller than this cannot be measured.
**Model answer:** The data supports the conclusion that the level drops by about $6\,\text{dB}$ every time the distance doubles. The differences of consecutive readings are

$91\,\text{dB} - 85\,\text{dB} = 6\,\text{dB}$

$85\,\text{dB} - 79\,\text{dB} = 6\,\text{dB}$

$79\,\text{dB} - 74\,\text{dB} = 5\,\text{dB}$

All the differences are close to the expected $6.0\,\text{dB}$, and the largest deviation, $1\,\text{dB}$, is smaller than the uncertainty of the difference, $2\,\text{dB}$. So even the smaller drop in the last interval does not show that the sound is damped more slowly farther away. The level does not halve: half of $91\,\text{dB}$ would be about $46\,\text{dB}$, while $85\,\text{dB}$ was measured. At the distance $4.0\,\text{m}$ the reading is $85\,\text{dB}$, but because of the uncertainty the real level can be $84$–$86\,\text{dB}$, so the upper action value may be exceeded. Nor is the action value a safety limit, so the measurement does not show working for $8\,\text{h}$ to be safe.

## fy5-16-L3-01
**Given:** $t_1 = 4.0\,\text{h}$ at a level $L_1 = 88\,\text{dB}$, $t_2 = 4.0\,\text{h}$ at a level $L_2 = 82\,\text{dB}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the day's dose as a percentage of the reference dose
**Principle:** The dose is the energy accumulated in the ear, so the shares of the different periods are added. The share of each period is the ratio of its duration to the reference time at that level.
**Formula:** $t_{\text{perm},i} = \dfrac{t_0}{2^{\,n_i}}$, where $n_i = \dfrac{L_i - L_0}{3\,\text{dB}}$, and dose $= \left(\dfrac{t_1}{t_{\text{perm},1}} + \dfrac{t_2}{t_{\text{perm},2}}\right) \cdot 100\,\%$
**Conversions:** Not needed: the times are in hours, and the unit cancels.
**Substitution:** $n_1 = 1$, so $t_{\text{perm},1} = 8\,\text{h} : 2 = 4.0\,\text{h}$. $n_2 = \dfrac{82\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = -1$, so $t_{\text{perm},2} = 8\,\text{h} \cdot 2 = 16\,\text{h}$. Dose $= \left(\dfrac{4.0\,\text{h}}{4.0\,\text{h}} + \dfrac{4.0\,\text{h}}{16\,\text{h}}\right) \cdot 100\,\% = (1 + 0.25) \cdot 100\,\% = 125\,\%$
**Answer:** $125\,\%$. The times are given to two figures, so the result is an estimate, about $1.3$ times the dose. The daily exposure exceeds the upper action value, so hearing protectors must be used and the noise must be reduced.
**Reasonableness:** The $4\,\text{h}$ at the loading dock alone fill the whole dose, so the result must be over $100\,\%$. The share of the packing room is small, because there the intensity is only a quarter of the intensity at the dock.

## fy5-16-L3-02
**Given:** two identical units, each $L_1 = 55\,\text{dB}$ at a distance $r_1 = 3.0\,\text{m}$; the window's distance from each $r_2 = 12\,\text{m}$; point sources in an open space
**Find:** the level $L$ at the window when both are running
**Principle:** First calculate the level of one unit at the window: every doubling of the distance lowers the level by $6\,\text{dB}$. The intensities of two equally strong sources add, so the combined level is $3\,\text{dB}$ higher.
**Formula:** $L_\text{one} = L_1 - k \cdot 6\,\text{dB}$, where $2^{\,k} = \dfrac{r_2}{r_1}$, and $L = L_\text{one} + 3\,\text{dB}$
**Conversions:** Not needed: $r_2 : r_1 = 12\,\text{m} : 3.0\,\text{m} = 4$, so $2^{\,k} = 4$ and $k = 2$.
**Substitution:** $L_\text{one} = 55\,\text{dB} - 2 \cdot 6\,\text{dB} = 43\,\text{dB}$. $L = 43\,\text{dB} + 3\,\text{dB} = 46\,\text{dB}$
**Answer:** $46\,\text{dB}$, in whole decibels like the given value.
**Reasonableness:** Because of the distance the level of one unit is clearly lower than close by, and the second unit raises it only a little. The result is below a quiet conversation, but in a bedroom a steady hum can still disturb sleep.

## fy5-16-L3-03
**Find:** why anti-noise dampens a low hum better than speech
**Principle:** Anti-noise cancels noise by destructive interference only if it is in the opposite phase at the ear. The wavelength $\lambda = \dfrac{v}{f}$ and the period $T = \dfrac{1}{f}$ tell how precisely the timing and the position must match.
**Model answer:** The wavelength of the hum is $\lambda = \dfrac{343\,\text{m/s}}{100\,\text{Hz}} \approx 3.4\,\text{m}$ and its period $10\,\text{ms}$. The whole ear canal and the inside of the cup are small compared with the wavelength, and the electronics have time to form the opposite signal, so the anti-noise stays in the opposite phase at the ear. The wavelengths of speech are $\dfrac{343\,\text{m/s}}{3000\,\text{Hz}} \approx 11\,\text{cm}$ and $\dfrac{343\,\text{m/s}}{1000\,\text{Hz}} \approx 34\,\text{cm}$, and the period is at most $1\,\text{ms}$. Even a small timing error or a difference in position of a few centimetres shifts the phase a lot, and then the waves no longer cancel each other. In addition, speech varies quickly, whereas a hum is steady. High sounds are dampened mainly by the cups of the headphones.

## fy5-16-L1-06
**Find:** which measure shortens the reverberation time of the classroom
**Principle:** The reverberation time is the time in which the level falls by $60\,\text{dB}$ after the source has stopped. Hard surfaces reflect sound and keep it in the room, whereas soft and porous surfaces dampen the reflections, so the level falls faster.
**Model answer:** The reverberation time is shortened by fitting porous damping panels in the ceiling, which absorb part of the sound hitting them. Glossy tiles and glass surfaces are hard surfaces that reflect sound back into the room and would lengthen the time. Lowering the loudness of the sound does not help, because the reverberation time is measured as a drop of $60\,\text{dB}$ and does not depend on the initial level.

## fy5-16-L1-07
**Given:** outdoor level $L_\text{out} = 68\,\text{dB}$, indoor level $L_\text{in} = 41\,\text{dB}$
**Find:** the attenuation $\Delta L$ of the wall and the windows
**Principle:** The attenuation tells by how many decibels a structure lowers the level, so it is the difference between the outdoor and indoor levels.
**Formula:** $\Delta L = L_\text{out} - L_\text{in}$
**Conversions:** Not needed.
**Substitution:** $\Delta L = 68\,\text{dB} - 41\,\text{dB} = 27\,\text{dB}$
**Answer:** $27\,\text{dB}$, in whole decibels like the given values.
**Reasonableness:** The attenuation added to the indoor level gives the outdoor level: $41\,\text{dB} + 27\,\text{dB} = 68\,\text{dB}$. It is quieter inside than outside, as it should be.

## fy5-16-L1-08
**Find:** how a loudspeaker produces sound from an electrical signal
**Principle:** In a loudspeaker the signal is an alternating current that flows in a coil in the field of a magnet. The magnetic field exerts an alternating force on the current, so the coil and the cone attached to it vibrate, and the cone produces a sound wave in the air.
**Model answer:** The alternating current in the coil and the magnet make the cone vibrate in time with the signal, and the cone pushes the air back and forth. Sound that moves a diaphragm and induces a voltage is the operation of a microphone, not of a loudspeaker. In a loudspeaker the magnet stays in place, and the production of sound is not based on the heating of the air.

## fy5-16-L2-05
**Given:** before the panels the level falls from $90.3\,\text{dB}$ to $74.4\,\text{dB}$ and after the panels from $90.2\,\text{dB}$ to $50.1\,\text{dB}$ in a time $\Delta t = 0.40\,\text{s}$; the fall is steady
**Find:** the shortening of the reverberation time as a percentage
**Principle:** When the level falls steadily, the reverberation time is the time in which the fall is $60\,\text{dB}$. It is calculated for both measurements from the measured drop and time, and the times are compared.
**Reading the table:** The drop before the panels is $\Delta L_1 = 90.3\,\text{dB} - 74.4\,\text{dB} = 15.9\,\text{dB}$ and after the panels $\Delta L_2 = 90.2\,\text{dB} - 50.1\,\text{dB} = 40.1\,\text{dB}$.
**Formula:** $T = \dfrac{60\,\text{dB}}{\Delta L} \cdot \Delta t$ and shortening $= \dfrac{T_1 - T_2}{T_1} \cdot 100\,\%$
**Conversions:** Not needed.
**Substitution:**
$$\begin{aligned}
T_1 &= \frac{60\,\text{dB}}{15.9\,\text{dB}} \cdot 0.40\,\text{s} \\
&= 1.51\,\text{s} \\
T_2 &= \frac{60\,\text{dB}}{40.1\,\text{dB}} \cdot 0.40\,\text{s} \\
&= 0.599\,\text{s} \\
\text{shortening} &= \frac{1.51 - 0.599}{1.51} \cdot 100\,\% \\
&= 60.3\,\%
\end{aligned}$$
**Answer:** $60.3\,\%$. The given data have three significant figures, so the result is given with three.
**Reasonableness:** The reverberation time shortened from about $1.5\,\text{s}$ to about $0.6\,\text{s}$, that is, it is about $0.4$ times as long. After the panels the level falls $40.1\,\text{dB} : 15.9\,\text{dB} \approx 2.5$ times faster, and $1 - 1 : 2.5 = 0.6$ matches the result. A time of $0.6\,\text{s}$ suits a speech classroom.

## fy5-16-L2-06
**Given:** attenuation $\Delta L = L_\text{without} - L_\text{barrier}$ at the frequencies $125$, $500$, $2000$ and $4000\,\text{Hz}$ from the values in the table; speed of sound $v = 343\,\text{m/s}$
**Find:** a) the difference in attenuation at $4000\,\text{Hz}$ and $500\,\text{Hz}$; b) why a low sound is attenuated less
**Principle:** The attenuation of a barrier is the drop in the level behind the barrier. A wave bends round a barrier the better, the longer its wavelength $\lambda = \dfrac{v}{f}$ is compared with the size of the barrier.
**Reading the table:** From the table the attenuations are $8.1\,\text{dB}$ at $125\,\text{Hz}$, $13.4\,\text{dB}$ at $500\,\text{Hz}$, $22.2\,\text{dB}$ at $2000\,\text{Hz}$ and $25.2\,\text{dB}$ at $4000\,\text{Hz}$.
**Formula:** $\Delta L = L_\text{without} - L_\text{barrier}$ and $\lambda = \dfrac{v}{f}$
**Conversions:** Not needed.
**Substitution:**
$$\begin{aligned}
\Delta L_{500} &= 68.4\,\text{dB} - 55.0\,\text{dB} \\
&= 13.4\,\text{dB} \\
\Delta L_{4000} &= 60.3\,\text{dB} - 35.1\,\text{dB} \\
&= 25.2\,\text{dB} \\
\Delta L_{4000} - \Delta L_{500} &= 11.8\,\text{dB}
\end{aligned}$$
The wavelengths are $\lambda_{125} = \dfrac{343\,\text{m/s}}{125\,\text{Hz}} = 2.7\,\text{m}$ and $\lambda_{4000} = \dfrac{343\,\text{m/s}}{4000\,\text{Hz}} = 0.086\,\text{m}$.
**Answer:** a) $11.8\,\text{dB}$. b) The wavelength of the low sound, $2.7\,\text{m}$, is of the order of the height of the barrier, so the wave bends over the barrier and the level behind the barrier stays higher. The wavelength of the high sound, $0.086\,\text{m}$, is much smaller than the barrier, so the barrier leaves it in its shadow.
**Reasonableness:** The attenuation grows with frequency on every row: $8.1 < 13.4 < 22.2 < 25.2\,\text{dB}$. That is why the result is positive, and the difference is smaller than the greatest attenuation $25.2\,\text{dB}$.

## fy5-16-L2-07
**Given:** level at the workstation $L = 109\,\text{dB}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$; the student's result $1.0\,\text{h}$
**Find:** a) what is wrong in the student's reasoning; b) the correct reference time $t_\text{ref}$ in minutes
**Principle:** Every $3\,\text{dB}$ above the action value halves the reference time, so the time is divided by two for each step of $3\,\text{dB}$. The steps multiply: the time is divided by the number $2^{\,n}$, not by the number $n$.
**Formula:** $n = \dfrac{L - L_0}{3\,\text{dB}}$ and $t_\text{ref} = \dfrac{t_0}{2^{\,n}}$
**Conversions:** $1\,\text{h} = 60\,\text{min}$.
**Substitution:**
$$\begin{aligned}
n &= \frac{109\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} \\
&= 8 \\
t_\text{ref} &= \frac{8\,\text{h}}{2^{\,8}} \\
&= \frac{480\,\text{min}}{256} \\
&= 1.875\,\text{min} \\
&\approx 1.9\,\text{min}
\end{aligned}$$
**Answer:** a) The student calculated the number of steps $n = 8$ correctly but divided the time by $8$. Every step halves the remaining time, so the time is divided by two eight times, that is, altogether by $256$. b) The reference time is about $1.9\,\text{min}$, just under two minutes.
**Reasonableness:** The student's result of $1.0\,\text{h}$, that is $60\,\text{min}$, is $32$ times the correct one. In the student's way every additional step would shorten the time less and less, although the energy grows in the same ratio at every step. Check by halving: three halvings take the time $8\,\text{h} \to 1\,\text{h}$, and five more take it $60\,\text{min} \to 1.875\,\text{min}$, eight halvings in all.

## fy5-16-L3-04
**Given:** sawing $L_1 = 97\,\text{dB}$, $t_1 = 1.0\,\text{h}$; planing $L_2 = 91\,\text{dB}$, $t_2 = 2.0\,\text{h}$; assembly $L_3 = 85\,\text{dB}$, $t_3 = 3.0\,\text{h}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** a) the day's dose as a percentage; b) the smallest attenuation $\Delta L$ of the hearing protectors; c) whether enclosing the saw is enough
**Principle:** The dose is the energy accumulated in the ear, so the shares of the stages are added. The share is the ratio of the duration to the reference time at that level. A hearing protector lowers the intensity of all stages by the same factor, so the dose is divided by the number $2^{\,\Delta L / (3\,\text{dB})}$.
**Formula:** $t_{\text{perm},i} = \dfrac{t_0}{2^{\,n_i}}$, where $n_i = \dfrac{L_i - L_0}{3\,\text{dB}}$; dose $D = \sum \dfrac{t_i}{t_{\text{perm},i}}$; condition $\dfrac{D}{2^{\,\Delta L / (3\,\text{dB})}} \le 1$
**Conversions:** Not needed: the times are in hours, and the unit cancels.
**Substitution:**
Sawing: $n_1 = \dfrac{97 - 85}{3} = 4$, so $t_{\text{perm},1} = 8\,\text{h} : 16 = 0.50\,\text{h}$ and the share is $1.0\,\text{h} : 0.50\,\text{h} = 2.0$. Planing: $n_2 = 2$, $t_{\text{perm},2} = 2.0\,\text{h}$ and the share $1.0$. Assembly: $n_3 = 0$, $t_{\text{perm},3} = 8\,\text{h}$ and the share $0.375$.
$$\begin{aligned}
D &= 2.0 + 1.0 + 0.375 \\
&= 3.375
\end{aligned}$$
Part b:
$$\begin{aligned}
2^{\,\Delta L / (3\,\text{dB})} &\ge 3.375 \\
\Delta L &\ge 3\,\text{dB} \cdot \frac{\lg 3.375}{\lg 2} \\
&= 3\,\text{dB} \cdot 1.755 \\
&= 5.26\,\text{dB}
\end{aligned}$$
Part c: the enclosure lowers the level of sawing to $87\,\text{dB}$, whereby $n_1 = \dfrac{2}{3}$ and $t_{\text{perm},1} = \dfrac{8\,\text{h}}{2^{2/3}} = 5.04\,\text{h}$, and the share is $1.0 : 5.04 = 0.198$. The new dose is $D = 0.198 + 1.0 + 0.375 = 1.57$.
**Answer:** a) about $340\,\%$. b) at least $5.3\,\text{dB}$. c) It is not enough alone, because the dose is still about $160\,\%$ of the reference dose. In addition to the enclosure, for example hearing protectors with an attenuation of at least $\dfrac{3\,\text{dB} \cdot \lg 1.57}{\lg 2} = 2.0\,\text{dB}$ are needed, or the planer could be placed away from the workstation.
**Reasonableness:** Sawing and planing are above the action value, so the dose must be over $100\,\%$. Ordinary protectors attenuate $20$–$30\,\text{dB}$, so $5.3\,\text{dB}$ is easily met.

## fy5-16-L3-05
**Given:** $L_1 = 112\,\text{dB}$ at a distance $r_1 = 2.0\,\text{m}$, listener at a distance $r_2 = 8.0\,\text{m}$; attenuation of the earplugs $\Delta L = 8\,\text{dB}$; duration of the concert $t = 3.0\,\text{h}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** a) the level without earplugs; b) the reference time with earplugs; c) the dose as a percentage and whether it stays below the reference dose at a distance of $16\,\text{m}$
**Principle:** The level of a point source falls by $6\,\text{dB}$ every time the distance doubles. The earplugs lower the level reaching the ear by their attenuation, and the reference time follows from the rule in which every $3\,\text{dB}$ above the action value halves the time. The dose is the ratio of the listening time to the reference time.
**Formula:** $L_2 = L_1 - k \cdot 6\,\text{dB}$, where $2^{\,k} = \dfrac{r_2}{r_1}$; $L = L_2 - \Delta L$; $t_\text{ref} = \dfrac{t_0}{2^{\,n}}$, where $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Conversions:** Not needed: $r_2 : r_1 = 8.0\,\text{m} : 2.0\,\text{m} = 4$, so $k = 2$.
**Substitution:**
Part a: $L_2 = 112\,\text{dB} - 2 \cdot 6\,\text{dB} = 100\,\text{dB}$.
Part b: with the earplugs the level is $L = 100\,\text{dB} - 8\,\text{dB} = 92\,\text{dB}$.
$$\begin{aligned}
n &= \frac{92\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} \\
&= 2.33 \\
t_\text{ref} &= \frac{8\,\text{h}}{2^{\,2.33}} \\
&= 1.59\,\text{h}
\end{aligned}$$
Part c: the dose is $\dfrac{3.0\,\text{h}}{1.59\,\text{h}} = 1.89$, that is, $190\,\%$. At a distance of $16\,\text{m}$ the level is $100\,\text{dB} - 6\,\text{dB} = 94\,\text{dB}$ and with the earplugs in the ears $86\,\text{dB}$. Then $n = \dfrac{1}{3}$, $t_\text{ref} = \dfrac{8\,\text{h}}{2^{1/3}} = 6.35\,\text{h}$ and the dose is $\dfrac{3.0\,\text{h}}{6.35\,\text{h}} = 0.47$, that is, $47\,\%$.
**Answer:** a) $100\,\text{dB}$. b) $1.6\,\text{h}$, two significant figures as in the attenuation and the duration. c) Standing still at a distance of $8.0\,\text{m}$ the dose is $190\,\%$ of the reference dose. If the listener keeps the earplugs in also at a distance of $16\,\text{m}$, the dose falls to about $47\,\%$, below the reference dose. That does not guarantee safe hearing, but it reduces the strain clearly.
**Reasonableness:** Without the earplugs the reference time would be only $8\,\text{h} : 2^5 = 0.25\,\text{h}$, so the attenuation of $8\,\text{dB}$ lengthens it about sixfold, and $1.59\,\text{h} : 0.25\,\text{h} = 6.3 \approx 2^{8/3} = 6.35$.
