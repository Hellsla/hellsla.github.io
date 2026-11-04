## fy5-14-L1-01
**Given:** distance to the wall $d = 86.0\,\text{m}$, return time of the echo $t = 0.505\,\text{s}$
**Find:** the speed of sound $v$ in $\text{m/s}$
**Principle:** The sound travels to the wall and is reflected back, so during the return time it covers a distance $2d$. In air sound travels at a steady speed, so the speed is the distance travelled divided by the time.
**Formula:** $2d = v t$, so $v = \dfrac{2d}{t}$
**Conversions:** None needed: the distance is in metres and the time in seconds.
**Substitution:** $v = \dfrac{2 \cdot 86.0\,\text{m}}{0.505\,\text{s}} = \dfrac{172.0\,\text{m}}{0.505\,\text{s}} = 340.59\,\text{m/s}$
**Answer:** $341\,\text{m/s}$, three significant figures like the distance and the time.
**Reasonableness:** The result is close to the table value $340\,\text{m/s}$ for air at about $15\,{}^\circ\text{C}$. If the distance had not been multiplied by two, the speed would have come out as about $170\,\text{m/s}$, which is clearly too small. With timing started by hand, the reaction time can still change the result by several per cent.

## fy5-14-L1-02
**Given:** frequency of the ultrasound $f = 45.0\,\text{kHz}$, speed of sound in air $v = 340\,\text{m/s}$
**Find:** the wavelength $\lambda$ in millimetres
**Principle:** Ultrasound is a longitudinal wave just like audible sound, so the basic wave equation $v = f\lambda$ holds for it.
**Formula:** $v = f\lambda$, so $\lambda = \dfrac{v}{f}$
**Conversions:** $f = 45.0\,\text{kHz} = 45.0 \cdot 1000\,\text{Hz} = 45\,000\,\text{Hz}$; finally $1\,\text{m} = 1000\,\text{mm}$.
**Substitution:** $\lambda = \dfrac{340\,\text{m/s}}{45\,000\,\text{Hz}} = 0.0075556\,\text{m} = 7.5556\,\text{mm}$
**Answer:** $7.56\,\text{mm}$, three significant figures like the frequency $45.0\,\text{kHz}$ and the speed $340\,\text{m/s}$.
**Reasonableness:** At the upper limit of hearing, $20\,\text{kHz}$, the wavelength is $1.7\,\text{cm}$, and at more than twice the frequency the wavelength is less than half of that. A wavelength of a few millimetres is the size of an insect, so a bat can detect insects by echolocation.

## fy5-14-L1-03
**Given:** fundamental frequency $f_1 = 147\,\text{Hz}$
**Find:** the frequency $f_4$ of the fourth member of the harmonic series
**Principle:** A string fixed at both ends vibrates at all its natural frequencies at once, which are whole-number multiples of the fundamental frequency and form the harmonic series. The first member of the series is the fundamental frequency, so the fourth member is the third overtone.
**Formula:** $f_n = n f_1$, so $f_4 = 4 f_1$
**Conversions:** None needed: the frequency is in hertz.
**Substitution:** $f_4 = 4 \cdot 147\,\text{Hz} = 588\,\text{Hz}$
**Answer:** $588\,\text{Hz}$, three significant figures like the fundamental frequency.
**Reasonableness:** The members of the series are $147\,\text{Hz}$, $294\,\text{Hz}$, $441\,\text{Hz}$ and $588\,\text{Hz}$, so the fourth member is two octaves above the fundamental: two doublings give four times the frequency.

## fy5-14-L1-04
**Given:** frequency of the note $f_0 = 415\,\text{Hz}$, speed of the car $v_\text{s} = 15.0\,\text{m/s}$ away from the listener, speed of sound $v = 340\,\text{m/s}$
**Find:** the frequency heard $f$
**Principle:** The sound source moves and the listener is at rest, so we use the Doppler formula for a moving source. The source moves away, so the wavefronts spread out behind it and the frequency heard is lower than $f_0$: the denominator gets a plus sign.
**Formula:** $f = f_0 \cdot \dfrac{v}{v + v_\text{s}}$
**Conversions:** None needed: the speeds are in $\text{m/s}$ and the frequency in hertz.
**Substitution:** $f = 415\,\text{Hz} \cdot \dfrac{340\,\text{m/s}}{340\,\text{m/s} + 15.0\,\text{m/s}} = 415\,\text{Hz} \cdot \dfrac{340}{355} = 397.46\,\text{Hz}$
**Answer:** $397\,\text{Hz}$, three significant figures like the given data.
**Reasonableness:** The frequency drops because the source moves away. The speed of the car is about $4.4\,\%$ of the speed of sound, and the frequency drops by about $\tfrac{415 - 397}{415} \approx 4.2\,\%$, so the change is of the same order as the ratio of the speeds.

## fy5-14-L1-05
**Find:** the class of each sound: infrasound, audible sound or ultrasound
**Principle:** A human hears frequencies from about $20\,\text{Hz}$ to about $20\,\text{kHz}$. Sound below $20\,\text{Hz}$ is infrasound and sound above $20\,\text{kHz}$ is ultrasound. All of them are longitudinal pressure waves of the same kind; the class depends only on the frequency.
**Model answer:** a) $12\,\text{Hz} < 20\,\text{Hz}$, so the lowest part of the thunder is infrasound. b) $440\,\text{Hz}$ lies between the limits $20\,\text{Hz}$ and $20\,\text{kHz}$, so the tuning note is audible sound. c) $35\,\text{kHz} > 20\,\text{kHz}$, so the sound of the dog whistle is ultrasound: a dog hears it, but a human does not. d) $2.5\,\text{MHz} = 2\,500\,000\,\text{Hz}$ is many orders of magnitude above the range of hearing, so the sound of ultrasound imaging is ultrasound.

## fy5-14-L2-01
**Given:** frequency of the tuning fork $f_1 = 262\,\text{Hz}$, $N = 15$ loud moments in a time $t = 5.0\,\text{s}$, the string is lower than the tuning fork
**Find:** the frequency of the string $f_2$
**Principle:** Two sounds of almost the same frequency produce beats, and the number of loud moments per second equals the difference of the frequencies. The beat frequency is obtained by counting the loud moments per unit time. Because the string is lower, its frequency is smaller than that of the tuning fork by the beat frequency.
**Formula:** $f_\text{h} = \dfrac{N}{t}$ and $f_\text{h} = |f_1 - f_2| = f_1 - f_2$, so $f_2 = f_1 - \dfrac{N}{t}$
**Conversions:** None needed: the time is in seconds, so $\tfrac{N}{t}$ comes out in hertz.
**Substitution:** $f_\text{h} = \dfrac{15}{5.0\,\text{s}} = 3.0\,\text{Hz}$ and $f_2 = 262\,\text{Hz} - 3.0\,\text{Hz} = 259\,\text{Hz}$
**Answer:** $259\,\text{Hz}$; the difference $3.0\,\text{Hz}$ is known to a tenth of a hertz, so the result is given in whole hertz like the frequency of the tuning fork.
**Reasonableness:** Three loud moments per second are easy to count by ear, and the frequency difference is less than $10\,\text{Hz}$, so the beats stand out clearly. When the tuner tightens the string, the frequency rises towards $262\,\text{Hz}$ and the beats slow down.

## fy5-14-L2-02
**Given:** wavelength in air $\lambda_\text{a} = 0.850\,\text{m}$, speed of sound in air $v_\text{a} = 340\,\text{m/s}$ and in water $v_\text{w} = 1480\,\text{m/s}$
**Find:** the wavelength in water $\lambda_\text{w}$
**Principle:** When sound passes from air into water, the frequency stays the same, because the particles at the boundary vibrate in step with the incoming wave. The speed changes, so the wavelength changes. In both substances $v = f\lambda$ holds.
**Formula:** $f = \dfrac{v_\text{a}}{\lambda_\text{a}}$ and $\lambda_\text{w} = \dfrac{v_\text{w}}{f}$
**Conversions:** None needed: the speeds are in $\text{m/s}$ and the wavelength in metres.
**Substitution:** $f = \dfrac{340\,\text{m/s}}{0.850\,\text{m}} = 400\,\text{Hz}$ and $\lambda_\text{w} = \dfrac{1480\,\text{m/s}}{400\,\text{Hz}} = 3.70\,\text{m}$
**Answer:** $3.70\,\text{m}$, three significant figures like the given data.
**Reasonableness:** Sound travels $\tfrac{1480}{340} \approx 4.4$ times as fast in water as in air, and at the same frequency the wavelength grows in the same ratio: $0.850\,\text{m} \cdot 4.35 \approx 3.7\,\text{m}$.

## fy5-14-L2-03
**Given:** frequency of the siren $f_0 = 650\,\text{Hz}$, speed of the driver $v_\text{h} = 90.0\,\text{km/h}$ towards the siren, speed of sound $v = 340\,\text{m/s}$
**Find:** the frequency heard by the driver $f$
**Principle:** The source is at rest and the listener moves, so the wavelength does not change, but the driver meets the wavefronts more often, because they approach at speed $v + v_\text{h}$. We use the Doppler formula for a moving listener with the plus sign for approaching.
**Formula:** $f = f_0 \cdot \dfrac{v + v_\text{h}}{v}$
**Conversions:** $v_\text{h} = 90.0\,\tfrac{\text{km}}{\text{h}} = 90.0 \cdot \tfrac{1000\,\text{m}}{3600\,\text{s}} = 25.0\,\tfrac{\text{m}}{\text{s}}$
**Substitution:** $f = 650\,\text{Hz} \cdot \dfrac{340\,\text{m/s} + 25.0\,\text{m/s}}{340\,\text{m/s}} = 650\,\text{Hz} \cdot \dfrac{365}{340} = 697.79\,\text{Hz}$
**Answer:** $698\,\text{Hz}$, three significant figures like the given data.
**Reasonableness:** The frequency rises because the driver approaches. The rise is $f_0 \cdot \tfrac{v_\text{h}}{v} = 650\,\text{Hz} \cdot \tfrac{25.0}{340} \approx 48\,\text{Hz}$, which is about $7\,\%$, like the ratio of the speeds $\tfrac{25}{340}$.

## fy5-14-L2-04
**Given:** frequency of the engine at rest $f_0 = 425\,\text{Hz}$, frequency heard as the car moves away $f = 398\,\text{Hz}$, speed of sound $v = 340\,\text{m/s}$
**Find:** the speed of the car $v_\text{s}$
**Principle:** The car, that is, the sound source, moves straight away from the spectator, and the spectator is at rest, so the Doppler formula for a moving source applies with the plus sign for moving away. The engine speed is the same, so the engine's own frequency is $f_0$. The speed of the source is solved from the formula.
**Formula:** $f = f_0 \cdot \dfrac{v}{v + v_\text{s}}$, so $v + v_\text{s} = \dfrac{f_0 v}{f}$ and $v_\text{s} = v \left(\dfrac{f_0}{f} - 1\right)$
**Conversions:** None needed: the frequencies are in hertz, and the unit cancels in their ratio.
**Substitution:** $v_\text{s} = 340\,\text{m/s} \cdot \left(\dfrac{425\,\text{Hz}}{398\,\text{Hz}} - 1\right) = 340\,\text{m/s} \cdot 0.067839 = 23.065\,\text{m/s}$
**Answer:** $23\,\text{m/s}$, two significant figures, because the result depends on the frequency difference $27\,\text{Hz}$, which is known to two figures.
**Reasonableness:** $23\,\text{m/s}$ is about $83\,\text{km/h}$, which is a believable speed on a racetrack. Check: $425\,\text{Hz} \cdot \tfrac{340}{340 + 23.07} \approx 398\,\text{Hz}$, as measured.

## fy5-14-L3-01
**Given:** frequency heard when approaching $f_1 = 476\,\text{Hz}$ and when moving away $f_2 = 404\,\text{Hz}$, speed of sound $v = 340\,\text{m/s}$; the frequency of the siren $f_0$ is unknown
**Find:** the speed of the ambulance $v_\text{s}$
**Principle:** The listener is at rest and the source moves straight towards them and straight away from them at the same speed, so the moving-source formula holds in both phases, with the minus sign when approaching and the plus sign when moving away. The unknown $f_0$ cancels when the frequencies are divided by each other.
**Formula:** $f_1 = f_0 \cdot \dfrac{v}{v - v_\text{s}}$ and $f_2 = f_0 \cdot \dfrac{v}{v + v_\text{s}}$, so $\dfrac{f_1}{f_2} = \dfrac{v + v_\text{s}}{v - v_\text{s}}$. Cross-multiplying, $f_1 v - f_1 v_\text{s} = f_2 v + f_2 v_\text{s}$, so $v_\text{s} (f_1 + f_2) = v (f_1 - f_2)$ and $v_\text{s} = v \cdot \dfrac{f_1 - f_2}{f_1 + f_2}$
**Conversions:** None needed: the unit of the frequencies cancels, and the speed comes out in $\text{m/s}$.
**Substitution:** $v_\text{s} = 340\,\text{m/s} \cdot \dfrac{476\,\text{Hz} - 404\,\text{Hz}}{476\,\text{Hz} + 404\,\text{Hz}} = 340\,\text{m/s} \cdot \dfrac{72}{880} = 27.818\,\text{m/s}$
**Answer:** $28\,\text{m/s}$, two significant figures, because the frequency difference $72\,\text{Hz}$ is known to two figures.
**Reasonableness:** $28\,\text{m/s}$ is about $100\,\text{km/h}$, which suits an emergency drive. The siren's own frequency is $f_0 = f_1 \cdot \tfrac{v - v_\text{s}}{v} \approx 437\,\text{Hz}$, and it lies between the frequencies heard, as it should. Also $f_2 = 437\,\text{Hz} \cdot \tfrac{340}{367.8} \approx 404\,\text{Hz}$ agrees.

## fy5-14-L3-02
**Given:** reference note $f_0 = 440\,\text{Hz}$, beat frequency before tightening $f_\text{h} = 4\,\text{Hz}$ and after tightening $6\,\text{Hz}$
**Find:** the frequency of the string $f$ before tightening
**Principle:** The beat frequency is the absolute value of the frequency difference, so from the beats alone the frequency of the string could be either $440\,\text{Hz} - 4\,\text{Hz}$ or $440\,\text{Hz} + 4\,\text{Hz}$. Tightening increases the speed of the wave in the string and therefore raises the frequency of the string. Because the beats sped up, that is, the difference grew, the rising frequency moved away from the reference note: the string was already higher than the reference note. If the string had been $436\,\text{Hz}$, tightening would have taken it towards $440\,\text{Hz}$ and the beats would have slowed down.
**Formula:** $f_\text{h} = |f - f_0|$, and when $f > f_0$, $f = f_0 + f_\text{h}$
**Conversions:** None needed: all the frequencies are in hertz.
**Substitution:** $f = 440\,\text{Hz} + 4\,\text{Hz} = 444\,\text{Hz}$
**Answer:** $444\,\text{Hz}$, in whole hertz like the reference note and the beat frequency.
**Reasonableness:** After tightening, the frequency of the string is $440\,\text{Hz} + 6\,\text{Hz} = 446\,\text{Hz}$, so it rose by $2\,\text{Hz}$, which suits a small tightening. To tune the string, it must therefore be loosened until the beats stop.

## fy5-14-L3-03
**Find:** the fundamental frequency of the note, the members of the harmonic series missing from the spectrum, and what they mean for the air column of the clarinet
**Principle:** The peaks in the spectrum of an instrument are at the natural frequencies of the air column, and the fundamental frequency is the lowest natural frequency. In a tube open at both ends the natural frequencies are all multiples $n f_1$ of the fundamental frequency, but in a tube closed at one end only the odd multiples, because the closed end is always a node and the open end an antinode (chapter *Standing waves: nodes, antinodes and natural frequencies*).
**Model answer:** The lowest peak is $147\,\text{Hz}$, and the others are its multiples: $441\,\text{Hz} = 3 \cdot 147\,\text{Hz}$, $735\,\text{Hz} = 5 \cdot 147\,\text{Hz}$ and $1029\,\text{Hz} = 7 \cdot 147\,\text{Hz}$. So the fundamental frequency is $147\,\text{Hz}$. The even members of the harmonic series, $294\,\text{Hz}$, $588\,\text{Hz}$ and $882\,\text{Hz}$, are almost entirely missing. Only the odd multiples are natural frequencies of a tube closed at one end, so the air column of the clarinet vibrates like a tube with one end closed: the mouthpiece end, where the reed is, acts as the closed end with a node of the air motion, and the bell end as the open end with an antinode. The missing overtones give the clarinet its dark timbre.
