## fy5-16-L1-01
**Given:** noise level $L = 91\,\text{dB}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the permitted daily time $t_\text{perm}$ in hours
**Principle:** Noise exposure is calculated as an average of energy: every rise of $3\,\text{dB}$ doubles the intensity, so the same dose is reached in half the time.
**Formula:** $t_\text{perm} = \dfrac{t_0}{2^{\,n}}$, where $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Conversions:** Not needed: the levels are in decibels and the time comes out in hours.
**Substitution:** $n = \dfrac{91\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 2$, $t_\text{perm} = \dfrac{8\,\text{h}}{2^2} = 2.0\,\text{h}$
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
**Reasonableness:** The level stays below the upper action value $85\,\text{dB}$, so the protectors are enough for the whole working day if they are well fitted and worn all the time. Without protectors the permitted time would be about $4\,\text{min}$.

## fy5-16-L1-05
**Find:** whether each measure belongs to the source, the path or the ear
**Principle:** At the source the sound produced is reduced, along the path the travel of sound from the source to the listener is blocked or dampened, and at the ear the sound reaching the ear is reduced.
**Model answer:** a) A noise barrier stops the direct sound between the road and the homes, so it is a measure along the path. b) A casing encloses the sound right around the machine, so it controls noise at the source. c) Earplugs attenuate sound only at the ear. d) Panels fitted in the ceiling do not make the machine quieter, but they absorb the reflections through which the sound travels to the worker, so they are a measure along the path.

## fy5-16-L2-01
**Given:** two identical machines, each $L_1 = 85\,\text{dB}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the permitted daily time $t_\text{perm}$ in hours
**Principle:** The intensities of two equally strong sources add, so the intensity doubles and the level rises by about $3\,\text{dB}$. Then every $3\,\text{dB}$ above the action value halves the permitted time.
**Formula:** $L = L_1 + 3\,\text{dB}$ and $t_\text{perm} = \dfrac{t_0}{2^{\,n}}$, where $n = \dfrac{L - L_0}{3\,\text{dB}}$
**Conversions:** Not needed.
**Substitution:** $L = 85\,\text{dB} + 3\,\text{dB} = 88\,\text{dB}$, $n = \dfrac{88\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 1$, $t_\text{perm} = \dfrac{8\,\text{h}}{2^1} = 4.0\,\text{h}$
**Answer:** $4.0\,\text{h}$. The rule is an estimate, so two significant figures are enough.
**Reasonableness:** The second machine brings as much energy again, so the total energy builds up twice as fast and the dose is reached in half the time. The result is consistent: $2 \cdot 4\,\text{h} = 8\,\text{h}$.

## fy5-16-L2-02
**Given:** level at the ear $L = 94\,\text{dB}$, listening time $t = 1.5\,\text{h}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the dose as a percentage of the reference dose
**Principle:** First calculate the permitted time at a level of $94\,\text{dB}$: in that time exactly the reference dose builds up. The share of the dose is the ratio of the listening time to the permitted time, because the level is the same all the time.
**Formula:** $t_\text{perm} = \dfrac{t_0}{2^{\,n}}$, where $n = \dfrac{L - L_0}{3\,\text{dB}}$, and share $= \dfrac{t}{t_\text{perm}} \cdot 100\,\%$
**Conversions:** Not needed: the times are in hours, and the unit cancels.
**Substitution:** $n = \dfrac{94\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 3$, $t_\text{perm} = \dfrac{8\,\text{h}}{2^3} = 1.0\,\text{h}$, share $= \dfrac{1.5\,\text{h}}{1.0\,\text{h}} \cdot 100\,\% = 150\,\%$
**Answer:** $150\,\%$, two significant figures as in the time $1.5\,\text{h}$.
**Reasonableness:** The listening time is longer than the permitted time, so the dose exceeds the reference, that is, more than $100\,\%$ is expected. If the sound were lowered by $3\,\text{dB}$, the dose would be halved to $75\,\%$.

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

## fy5-16-L3-01
**Given:** $t_1 = 4.0\,\text{h}$ at a level $L_1 = 88\,\text{dB}$, $t_2 = 4.0\,\text{h}$ at a level $L_2 = 82\,\text{dB}$; reference $L_0 = 85\,\text{dB}$ and $t_0 = 8\,\text{h}$
**Find:** the day's dose as a percentage of the reference dose
**Principle:** The dose is the energy accumulated in the ear, so the shares of the different periods are added. The share of each period is the ratio of its duration to the permitted time at that level.
**Formula:** $t_{\text{perm},i} = \dfrac{t_0}{2^{\,n_i}}$, where $n_i = \dfrac{L_i - L_0}{3\,\text{dB}}$, and dose $= \left(\dfrac{t_1}{t_{\text{perm},1}} + \dfrac{t_2}{t_{\text{perm},2}}\right) \cdot 100\,\%$
**Conversions:** Not needed: the times are in hours, and the unit cancels.
**Substitution:** $n_1 = 1$, so $t_{\text{perm},1} = 8\,\text{h} : 2 = 4.0\,\text{h}$. $n_2 = \dfrac{82\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = -1$, so $t_{\text{perm},2} = 8\,\text{h} \cdot 2 = 16\,\text{h}$. Dose $= \left(\dfrac{4.0\,\text{h}}{4.0\,\text{h}} + \dfrac{4.0\,\text{h}}{16\,\text{h}}\right) \cdot 100\,\% = (1 + 0.25) \cdot 100\,\% = 125\,\%$
**Answer:** $125\,\%$. The times are given to two figures, so the result is an estimate, about $1.3$ times the dose. The upper action value is exceeded, so protectors must be used.
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
