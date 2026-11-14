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
**Given:** frequency of the note $f_0 = 415\,\text{Hz}$, speed of the car $v_\text{L} = 15.0\,\text{m/s}$ away from the listener, speed of sound $v = 340\,\text{m/s}$
**Find:** the frequency heard $f$
**Principle:** The sound source moves and the listener is at rest, so we use the Doppler formula for a moving source. The source moves away, so the wavefronts spread out behind it and the frequency heard is lower than $f_0$: the denominator gets a plus sign.
**Formula:** $f = f_0 \cdot \dfrac{v}{v + v_\text{L}}$
**Conversions:** None needed: the speeds are in $\text{m/s}$ and the frequency in hertz.
**Substitution:** $f = 415\,\text{Hz} \cdot \dfrac{340\,\text{m/s}}{340\,\text{m/s} + 15.0\,\text{m/s}} = 415\,\text{Hz} \cdot \dfrac{340}{355} = 397.46\,\text{Hz}$
**Answer:** $397\,\text{Hz}$, three significant figures like the given data.
**Reasonableness:** The frequency drops because the source moves away. The speed of the car is about $4.4\,\%$ of the speed of sound, and the frequency drops by about $\tfrac{415 - 397}{415} \approx 4.2\,\%$, so the change is of the same order as the ratio of the speeds.

## fy5-14-L1-05
**Find:** the class of each sound: infrasound, audible sound or ultrasound
**Principle:** A human hears frequencies from about $20\,\text{Hz}$ to about $20\,\text{kHz}$. Sound below $20\,\text{Hz}$ is infrasound and sound above $20\,\text{kHz}$ is ultrasound. All of them are longitudinal pressure waves of the same kind; the class depends only on the frequency.
**Model answer:** a) $12\,\text{Hz} < 20\,\text{Hz}$, so the lowest part of the thunder is infrasound. b) $440\,\text{Hz}$ lies between the limits $20\,\text{Hz}$ and $20\,\text{kHz}$, so the tuning note is audible sound. c) $35\,\text{kHz} > 20\,\text{kHz}$, so the sound of the dog whistle is ultrasound: a dog hears it, but a human does not. d) $2.5\,\text{MHz} = 2\,500\,000\,\text{Hz}$ is many orders of magnitude above the range of hearing, so the sound of ultrasound imaging is ultrasound.

## fy5-14-L1-09
**Find:** which of the five statements about the pitch and timbre of a violin note and about the sound of the horn of a moving car are true
**Principle:** We hear the pitch from the fundamental frequency, which is the lowest frequency of the harmonic series and the spacing of adjacent peaks. The timbre depends on the strengths of the overtones compared with the fundamental frequency. When the source moves, the sound still travels relative to the air at the speed $v$, but in front of the source the wavelength becomes shorter and behind it longer. The frequency that is heard depends on the speed of the source, not on its distance.
**Model answer:** Statements 2 and 5 are true, statements 1, 3 and 4 are false.

Statement 1 is false. The spacing of the peaks is $660\,\text{Hz} - 330\,\text{Hz} = 330\,\text{Hz}$, and the lowest peak is $330\,\text{Hz}$, so the fundamental frequency and the pitch correspond to the frequency $330\,\text{Hz}$. The strongest peak $660\,\text{Hz}$ is an overtone.

Statement 2 is true. The fundamental frequency of the same note is $330\,\text{Hz}$ in both instruments, but the strengths of the overtones differ, so the timbre is different.

Statement 3 is false. The motion of the source does not change the speed of sound in air. It changes the wavelength: in front of an approaching car the wavefronts are closer together.

Statement 4 is false. The car drives at a steady speed, so the frequency that is heard is the same throughout the approach and higher than $400\,\text{Hz}$. As the car approaches, the loudness grows, not the pitch.

Statement 5 is true. At the moment of passing, the frequency drops. Behind a car that moves away the wavelength is longer than when the car stands still, so the frequency that is heard is lower than $400\,\text{Hz}$.

## fy5-14-L2-01
**Given:** frequency of the tuning fork $f_1 = 262\,\text{Hz}$, $N = 15$ loud moments in a time $t = 5.0\,\text{s}$, the string is lower than the tuning fork
**Find:** the frequency of the string $f_2$
**Principle:** Two sounds of almost the same frequency produce beats, and the number of loud moments per second equals the difference of the frequencies. The beat frequency is obtained by counting the loud moments per unit time. Because the string is lower, its frequency is smaller than that of the tuning fork by the beat frequency.
**Formula:** $f_\text{H} = \dfrac{N}{t}$ and $f_\text{H} = |f_1 - f_2| = f_1 - f_2$, so $f_2 = f_1 - \dfrac{N}{t}$
**Conversions:** None needed: the time is in seconds, so $\tfrac{N}{t}$ comes out in hertz.
**Substitution:** $f_\text{H} = \dfrac{15}{5.0\,\text{s}} = 3.0\,\text{Hz}$ and $f_2 = 262\,\text{Hz} - 3.0\,\text{Hz} = 259\,\text{Hz}$
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
**Given:** frequency of the siren $f_0 = 650\,\text{Hz}$, speed of the driver $v_\text{H} = 90.0\,\text{km/h}$ towards the siren, speed of sound $v = 340\,\text{m/s}$
**Find:** the frequency heard by the driver $f$
**Principle:** The source is at rest and the listener moves, so the wavelength does not change, but the driver meets the wavefronts more often, because they approach at speed $v + v_\text{H}$. We use the Doppler formula for a moving listener with the plus sign for approaching.
**Formula:** $f = f_0 \cdot \dfrac{v + v_\text{H}}{v}$
**Conversions:** $v_\text{H} = 90.0\,\tfrac{\text{km}}{\text{h}} = 90.0 \cdot \tfrac{1000\,\text{m}}{3600\,\text{s}} = 25.0\,\tfrac{\text{m}}{\text{s}}$
**Substitution:** $f = 650\,\text{Hz} \cdot \dfrac{340\,\text{m/s} + 25.0\,\text{m/s}}{340\,\text{m/s}} = 650\,\text{Hz} \cdot \dfrac{365}{340} = 697.79\,\text{Hz}$
**Answer:** $698\,\text{Hz}$, three significant figures like the given data.
**Reasonableness:** The frequency rises because the driver approaches. The rise is $f_0 \cdot \tfrac{v_\text{H}}{v} = 650\,\text{Hz} \cdot \tfrac{25.0}{340} \approx 48\,\text{Hz}$, which is about $7\,\%$, like the ratio of the speeds $\tfrac{25}{340}$.

## fy5-14-L2-04
**Given:** frequency of the engine at rest $f_0 = 425\,\text{Hz}$, frequency heard as the car moves away $f = 398\,\text{Hz}$, speed of sound $v = 340\,\text{m/s}$
**Find:** the speed of the car $v_\text{L}$
**Principle:** The car, that is, the sound source, moves straight away from the spectator, and the spectator is at rest, so the Doppler formula for a moving source applies with the plus sign for moving away. The engine speed is the same, so the engine's own frequency is $f_0$. The speed of the source is solved from the formula.
**Formula:** $f = f_0 \cdot \dfrac{v}{v + v_\text{L}}$, so $v + v_\text{L} = \dfrac{f_0 v}{f}$ and $v_\text{L} = v \left(\dfrac{f_0}{f} - 1\right)$
**Conversions:** None needed: the frequencies are in hertz, and the unit cancels in their ratio.
**Substitution:** $v_\text{L} = 340\,\text{m/s} \cdot \left(\dfrac{425\,\text{Hz}}{398\,\text{Hz}} - 1\right) = 340\,\text{m/s} \cdot 0.067839 = 23.065\,\text{m/s}$
**Answer:** $23\,\text{m/s}$, two significant figures, because the result depends on the frequency difference $27\,\text{Hz}$, which is known to two figures.
**Reasonableness:** $23\,\text{m/s}$ is about $83\,\text{km/h}$, which is a believable speed on a racetrack. Check: $425\,\text{Hz} \cdot \tfrac{340}{340 + 23.07} \approx 398\,\text{Hz}$, as measured.

## fy5-14-L3-01
**Given:** frequency heard when approaching $f_1 = 476\,\text{Hz}$ and when moving away $f_2 = 404\,\text{Hz}$, speed of sound $v = 340\,\text{m/s}$; the frequency of the siren $f_0$ is unknown
**Find:** the speed of the ambulance $v_\text{L}$
**Principle:** The listener is at rest and the source moves straight towards them and straight away from them at the same speed, so the moving-source formula holds in both phases, with the minus sign when approaching and the plus sign when moving away. The unknown $f_0$ cancels when the frequencies are divided by each other.
**Formula:** $f_1 = f_0 \cdot \dfrac{v}{v - v_\text{L}}$ and $f_2 = f_0 \cdot \dfrac{v}{v + v_\text{L}}$, so $\dfrac{f_1}{f_2} = \dfrac{v + v_\text{L}}{v - v_\text{L}}$. Cross-multiplying, $f_1 v - f_1 v_\text{L} = f_2 v + f_2 v_\text{L}$, so $v_\text{L} (f_1 + f_2) = v (f_1 - f_2)$ and $v_\text{L} = v \cdot \dfrac{f_1 - f_2}{f_1 + f_2}$
**Conversions:** None needed: the unit of the frequencies cancels, and the speed comes out in $\text{m/s}$.
**Substitution:** $v_\text{L} = 340\,\text{m/s} \cdot \dfrac{476\,\text{Hz} - 404\,\text{Hz}}{476\,\text{Hz} + 404\,\text{Hz}} = 340\,\text{m/s} \cdot \dfrac{72}{880} = 27.818\,\text{m/s}$
**Answer:** $28\,\text{m/s}$, two significant figures, because the frequency difference $72\,\text{Hz}$ is known to two figures.
**Reasonableness:** $28\,\text{m/s}$ is about $100\,\text{km/h}$, which suits an emergency drive. The siren's own frequency is $f_0 = f_1 \cdot \tfrac{v - v_\text{L}}{v} \approx 437\,\text{Hz}$, and it lies between the frequencies heard, as it should. Also $f_2 = 437\,\text{Hz} \cdot \tfrac{340}{367.8} \approx 404\,\text{Hz}$ agrees.

## fy5-14-L3-02
**Given:** reference note $f_0 = 440\,\text{Hz}$, beat frequency before tightening $f_\text{H} = 4\,\text{Hz}$ and after tightening $6\,\text{Hz}$
**Find:** the frequency of the string $f$ before tightening
**Principle:** The beat frequency is the absolute value of the frequency difference, so from the beats alone the frequency of the string could be either $440\,\text{Hz} - 4\,\text{Hz}$ or $440\,\text{Hz} + 4\,\text{Hz}$. Tightening increases the speed of the wave in the string and therefore raises the frequency of the string. Because the beats sped up, that is, the difference grew, the rising frequency moved away from the reference note: the string was already higher than the reference note. If the string had been $436\,\text{Hz}$, tightening would have taken it towards $440\,\text{Hz}$ and the beats would have slowed down.
**Formula:** $f_\text{H} = |f - f_0|$, and when $f > f_0$, $f = f_0 + f_\text{H}$
**Conversions:** None needed: all the frequencies are in hertz.
**Substitution:** $f = 440\,\text{Hz} + 4\,\text{Hz} = 444\,\text{Hz}$
**Answer:** $444\,\text{Hz}$, in whole hertz like the reference note and the beat frequency.
**Reasonableness:** After tightening, the frequency of the string is $440\,\text{Hz} + 6\,\text{Hz} = 446\,\text{Hz}$, so it rose by $2\,\text{Hz}$, which suits a small tightening. To tune the string, it must therefore be loosened until the beats stop.

## fy5-14-L3-03
**Find:** the fundamental frequency of the note, the members of the harmonic series missing from the spectrum, and what they mean for the air column of the clarinet
**Principle:** The peaks in the spectrum of an instrument are at the natural frequencies of the air column, and the fundamental frequency is the lowest natural frequency. In a tube open at both ends the natural frequencies are all multiples $n f_1$ of the fundamental frequency, but in a tube closed at one end only the odd multiples, because the closed end is always a node and the open end an antinode (chapter *Standing waves: nodes, antinodes and natural frequencies*).
**Model answer:** The lowest peak is $147\,\text{Hz}$, and the others are its multiples: $441\,\text{Hz} = 3 \cdot 147\,\text{Hz}$, $735\,\text{Hz} = 5 \cdot 147\,\text{Hz}$ and $1029\,\text{Hz} = 7 \cdot 147\,\text{Hz}$. So the fundamental frequency is $147\,\text{Hz}$. The even members of the harmonic series, $294\,\text{Hz}$, $588\,\text{Hz}$ and $882\,\text{Hz}$, are almost entirely missing. Only the odd multiples are natural frequencies of a tube closed at one end, so the air column of the clarinet vibrates like a tube with one end closed: the mouthpiece end, where the reed is, acts as the closed end with a node of the air motion, and the bell end as the open end with an antinode. The missing overtones give the clarinet its dark timbre.

## fy5-14-L1-06
**Find:** which statement about the higher sound is necessarily true
**Principle:** Pitch is determined by frequency: the more pressure vibrations per second, the higher the sound seems. Loudness depends on the amplitude, and the speed of sound in air is the same for all frequencies.
**Model answer:** The frequency of the higher sound is greater, so the air pressure varies more times per second. The amplitude does not have to be greater, because the sounds seem equally loud. The wavelength is not longer but shorter, because $\lambda = \tfrac{v}{f}$ and the speed $v$ is the same. The period is also shorter, because $T = \tfrac{1}{f}$.

## fy5-14-L1-07
**Find:** what pitch of the siren the listener hears as the car approaches
**Principle:** In front of an approaching source the wavefronts are bunched up, because the source moves after its own wavefronts. The wavelength is then shorter and the frequency heard $f = \tfrac{v}{\lambda}$ is greater than the frequency of the source. The frequency heard depends on the speed of the source, not on the distance.
**Model answer:** The listener hears the sound of the siren at a constant frequency and higher than the siren's own frequency throughout the approach, because the speed of the car is constant and the wavefronts are bunched up in front of it. As the distance decreases, only the loudness of the sound grows. At the moment of passing, the frequency heard drops suddenly to below the siren's own frequency. The motion of the source does not slow down the sound: the speed of sound in air is the same.

## fy5-14-L1-08
**Given:** frequencies of the tuning forks $f_1 = 392\,\text{Hz}$ and $f_2 = 398\,\text{Hz}$
**Find:** the period of the beats $T_\text{H}$ in seconds
**Principle:** The number of loud moments per second equals the frequency difference. The time between two successive loud moments is the reciprocal of the beat frequency.
**Formula:** $f_\text{H} = |f_1 - f_2|$ and $T_\text{H} = \dfrac{1}{f_\text{H}}$
**Conversions:** None needed: the frequencies are in hertz, so the period comes out in seconds.
**Substitution:** $f_\text{H} = |392\,\text{Hz} - 398\,\text{Hz}| = 6\,\text{Hz}$, so $T_\text{H} = \dfrac{1}{6\,\text{Hz}} = 0.1667\,\text{s}$
**Answer:** $0.167\,\text{s}$, three significant figures, because the nominal frequencies of the tuning forks are taken as exact.
**Reasonableness:** Six beat periods last $6 \cdot 0.1667\,\text{s} = 1.00\,\text{s}$ altogether, which suits the frequency $6\,\text{Hz}$. The frequency difference is less than $10\,\text{Hz}$, so the beats stand out clearly.

## fy5-14-L2-05
**Given:** frequency of the horn at rest $f_0 = 392\,\text{Hz}$, four measured frequencies $431\,\text{Hz}$, $429\,\text{Hz}$, $432\,\text{Hz}$ and $430\,\text{Hz}$, speed of sound $v = 340\,\text{m/s}$
**Find:** the speed of the car $v_\text{L}$
**Principle:** The car, that is, the sound source, approaches a listener at rest, so the Doppler formula for a moving source with a minus sign applies. The measurements vary slightly, so we use their mean $f_\text{mean}$. The speed of the source is solved from the formula.
**Processing the data:** The sum of the four frequencies in the table is $431 + 429 + 432 + 430 = 1722$ hertz, so the mean is $f_\text{mean} = \dfrac{1722\,\text{Hz}}{4} = 430.5\,\text{Hz}$.
**Formula:** $f_\text{mean} = f_0 \cdot \dfrac{v}{v - v_\text{L}}$, so $v - v_\text{L} = \dfrac{f_0 v}{f_\text{mean}}$ and $v_\text{L} = v \left(1 - \dfrac{f_0}{f_\text{mean}}\right)$
**Conversions:** None needed: the frequencies are in hertz, and the unit cancels in their ratio.
**Substitution:** $v_\text{L} = 340\,\text{m/s} \cdot \left(1 - \dfrac{392\,\text{Hz}}{430.5\,\text{Hz}}\right) = 340\,\text{m/s} \cdot 0.08943 = 30.41\,\text{m/s}$
**Answer:** $30.4\,\text{m/s}$, three significant figures like the frequencies.
**Reasonableness:** $30.4\,\text{m/s}$ is about $109\,\text{km/h}$, which is roughly a highway speed. Calculating back: $\dfrac{392\,\text{Hz}}{1 - 30.41/340} = 430.5\,\text{Hz}$ is the measured mean. The individual measurements give speeds of $29.3$–$31.5\,\text{m/s}$, so the spread is about $1\,\text{m/s}$.

## fy5-14-L2-06
**Given:** peaks in the spectra of the flute and the violin at the frequencies $262\,\text{Hz}$, $524\,\text{Hz}$, $785\,\text{Hz}$, $1047\,\text{Hz}$ and $1309\,\text{Hz}$ and their relative heights in the table
**Find:** the fundamental frequency $f_1$ and which instrument sounds brighter
**Principle:** The partials of an instrument form the harmonic series $f_n = n f_1$, so the fundamental frequency is the lowest frequency of the series and the spacing of the peaks. It is not necessarily the strongest peak. Timbre depends on the strengths of the overtones: in a bright sound the overtones are strong.
**Processing the data:** The lowest peak is $262\,\text{Hz}$ in both spectra. The peaks are its multiples: $\dfrac{524}{2} = 262$, $\dfrac{785}{3} \approx 262$, $\dfrac{1047}{4} \approx 262$ and $\dfrac{1309}{5} \approx 262$. The strongest peak of the violin is the second harmonic, $524\,\text{Hz}$, but it is not the fundamental frequency.
**Formula:** $f_n = n f_1$, so $f_1 = \dfrac{f_n}{n}$
**Conversions:** None needed: all the frequencies are in hertz.
**Substitution:** $f_1 = \dfrac{1309\,\text{Hz}}{5} = 261.8\,\text{Hz}$
**Answer:** $262\,\text{Hz}$, three significant figures like the table. The violin sounds brighter, because its overtones are strong: already the third peak has the height $0.80$, whereas for the flute it is only $0.08$. The sound of the flute is almost a pure fundamental, and its timbre is soft.
**Reasonableness:** The multiples $2 \cdot 262\,\text{Hz} = 524\,\text{Hz}$ and $5 \cdot 262\,\text{Hz} = 1310\,\text{Hz}$ match the peaks in the table. The small differences come from the FFT reading the frequencies to about one hertz. The frequency $262\,\text{Hz}$ is middle C, which suits both instruments.

## fy5-14-L2-07
**Given:** speed of the car $v_\text{L} = 30.0\,\text{m/s}$, frequency of the horn $f_0 = 500\,\text{Hz}$, speed of sound $v = 340\,\text{m/s}$, the student's result $544\,\text{Hz}$
**Find:** the student's error and the correct frequency heard $f$
**Principle:** The student used a formula that applies to a moving listener. Here the listener is at rest and the sound source, the car, is moving, so the formula for a moving source applies. The motion of the source shortens the wavelength in front of the source ($\lambda = (v - v_\text{L}) T_0$), whereas the motion of a listener does not change the wavelength. The car approaches, so the sign is chosen so that $f > f_0$.
**Formula:** $f = f_0 \cdot \dfrac{v}{v - v_\text{L}}$
**Conversions:** None needed: the speeds are already in m/s.
**Substitution:**
$\begin{aligned} f &= 500\,\text{Hz} \cdot \dfrac{340\,\text{m/s}}{(340 - 30.0)\,\text{m/s}} \\ &= 500\,\text{Hz} \cdot \dfrac{340}{310.0} \\ &= 548.4\,\text{Hz} \end{aligned}$
**Answer:** $548\,\text{Hz}$, three significant figures like the given data. The student's value $544\,\text{Hz}$ is about $4\,\text{Hz}$ too small.
**Reasonableness:** The frequency rises because the car approaches: $548\,\text{Hz} > 500\,\text{Hz}$. The estimate for a small speed, $f_0 \cdot \tfrac{v_\text{L}}{v} = 500\,\text{Hz} \cdot \tfrac{30.0}{340} \approx 44\,\text{Hz}$, is close to the actual rise of $48\,\text{Hz}$, and the actual rise is slightly greater, because the denominator contains $v - v_\text{L}$.

## fy5-14-L3-04
**Given:** frequency of the probe $f_0 = 4.00\,\text{MHz} = 4.00 \cdot 10^6\,\text{Hz}$, speed of sound in tissue $v = 1540\,\text{m/s}$, frequency changes $\Delta f$ in the table, blood flows straight towards the probe
**Find:** the greatest measured speed of the blood $v_\text{b}$
**Principle:** The probe is at rest, and a red blood cell moves towards it at speed $v_\text{b}$. The cell is first a moving listener approaching the source and hears the frequency $f_1 = f_0 \cdot \tfrac{v + v_\text{b}}{v}$. It reflects the same frequency back, so it is then a moving source approaching the probe at rest, and the probe receives the frequency $f = f_1 \cdot \tfrac{v}{v - v_\text{b}}$. So the Doppler shift occurs twice, which is why the change is almost double compared with one shift. The greatest speed of flow corresponds to the greatest change in frequency.
**Processing the data:** The greatest change in the table is $\Delta f = 2.47\,\text{kHz}$ at the moment $t = 0.20\,\text{s}$.
**Formula:** $f = f_0 \cdot \dfrac{v + v_\text{b}}{v - v_\text{b}}$, so $\Delta f = f - f_0 = f_0 \cdot \dfrac{2 v_\text{b}}{v - v_\text{b}}$ and $v_\text{b} = \dfrac{v \, \Delta f}{2 f_0 + \Delta f}$
**Conversions:** $\Delta f = 2.47\,\text{kHz} = 2470\,\text{Hz}$ and $f_0 = 4.00\,\text{MHz} = 4\,000\,000\,\text{Hz}$.
**Substitution:** The denominator is $2 f_0 + \Delta f = 8\,000\,000\,\text{Hz} + 2470\,\text{Hz} = 8\,002\,470\,\text{Hz}$.
$\begin{aligned} v_\text{b} &= \dfrac{1540\,\text{m/s} \cdot 2470\,\text{Hz}}{8\,002\,470\,\text{Hz}} \\ &= 0.4753\,\text{m/s} \end{aligned}$
**Answer:** $0.475\,\text{m/s}$, three significant figures like the change in frequency.
**Reasonableness:** The speed is much smaller than the speed of sound, so $v_\text{b} \approx \tfrac{v \, \Delta f}{2 f_0} = 0.4755\,\text{m/s}$, which differs from the result by less than $0.1\,\%$. The result for one shift would be $\tfrac{v \, \Delta f}{f_0} \approx 0.95\,\text{m/s}$, double. A peak speed of less than a metre per second is plausible in a blood vessel.

## fy5-14-L3-05
**Given:** length of the string $L = 0.650\,\text{m}$, peaks in the spectra at the frequencies $196\,\text{Hz}$, $392\,\text{Hz}$, $588\,\text{Hz}$, $784\,\text{Hz}$, $980\,\text{Hz}$ and $1176\,\text{Hz}$ and their relative amplitudes in the table
**Find:** the fundamental frequency $f_1$, the missing harmonics, the speed of the wave in the string $v$ and the difference in timbre
**Principle:** The natural frequencies of a string fixed at both ends are $f_n = n f_1$, and at the fundamental frequency the string has one antinode, so $L = \tfrac{\lambda_1}{2}$ and $v = \lambda_1 f_1$. The even harmonics have a node in the middle of the string, and plucking at a node does not excite them.
**Processing the data:** The lowest peak is $196\,\text{Hz}$, and the others are its multiples: $\dfrac{392}{196} = 2$, $\dfrac{588}{196} = 3$, $\dfrac{784}{196} = 4$, $\dfrac{980}{196} = 5$ and $\dfrac{1176}{196} = 6$. In the spectrum of the string plucked in the middle, the amplitudes of the even harmonics ($n = 2$, $4$, $6$) are at most $0.02$.
**Formula:** $L = \dfrac{\lambda_1}{2}$, so $\lambda_1 = 2L$, and $v = \lambda_1 f_1$, so $v = 2 L f_1$
**Conversions:** None needed: the length is in metres and the frequency in hertz.
**Substitution:**
$\begin{aligned} v &= 2 \cdot 0.650\,\text{m} \cdot 196\,\text{Hz} \\ &= 254.8\,\text{m/s} \end{aligned}$
**Answer:** a) $196\,\text{Hz}$; when plucked in the middle, the even harmonics $392\,\text{Hz}$, $784\,\text{Hz}$ and $1176\,\text{Hz}$ are missing. b) $255\,\text{m/s}$, three significant figures like the length and the frequency. c) The even harmonics have a node in the middle of the string, and a node does not start to vibrate, so they are missing. The odd ones have an antinode in the middle, so they are produced. The sound plucked in the middle is almost a pure fundamental and soft. Near the bridge all the harmonics are produced, for example the amplitude of the third is $0.30$ and that of the sixth $0.09$. The abundant overtones make the sound bright. The pitch is the same, because the fundamental frequency is $196\,\text{Hz}$ in both.
**Reasonableness:** The wavelength is $\lambda_1 = 2 \cdot 0.650\,\text{m} = 1.30\,\text{m}$, and $1.30\,\text{m} \cdot 196\,\text{Hz} \approx 255\,\text{m/s}$, a typical order of magnitude for a guitar string. The frequency $196\,\text{Hz}$ is the note G3, the third string of a guitar. When plucked in the middle, the amplitudes of the odd harmonics fall roughly like $\tfrac{1}{n^2}$: $\tfrac{1}{9} = 0.11$ and $\tfrac{1}{25} = 0.04$, as in the table.

## fy5-14-L1-10
**Given:** the spectrum in the figure has five peaks; the frequencies of the peaks are read from the figure
**Find:** the frequency of the seventh harmonic $f_7$ in hertz
**Principle:** The sound of an instrument consists of the fundamental frequency and its multiples, so the peaks are at the frequencies of the harmonic series $f_n = n f_1$. The fundamental $f_1$ is the lowest frequency of the series, and the seventh harmonic is not in the figure, so it is calculated as a multiple of the fundamental.
**Reading the figure:** The peaks are at $200\,\text{Hz}$, $400\,\text{Hz}$, $600\,\text{Hz}$, $800\,\text{Hz}$ and $1000\,\text{Hz}$. The lowest peak is at $200\,\text{Hz}$, so $f_1 = 200\,\text{Hz}$. The strongest peak $400\,\text{Hz}$ is the second harmonic, not the fundamental.
**Formula:** $f_n = n f_1$
**Conversions:** None are needed: the frequencies are read in hertz.
**Substitution:** $f_7 = 7 \cdot 200\,\text{Hz} = 1400\,\text{Hz}$
**Answer:** $1400\,\text{Hz}$, three significant figures like the fundamental read from the graph.
**Reasonableness:** The seventh harmonic lies above the fifth peak $1000\,\text{Hz}$ by two spacings: $1000\,\text{Hz} + 2 \cdot 200\,\text{Hz} = 1400\,\text{Hz}$, since the spacing of the peaks is $200\,\text{Hz}$.

## fy5-14-L2-08
**Given:** the combined sound of two tuning forks sounding at the same time, in the figure; one fork $523\,\text{Hz}$; wax lowers the frequency of the unknown fork and the beats get faster
**Find:** the frequency $f_x$ of the unknown fork before the wax was added
**Principle:** The beat frequency is the difference of the frequencies, $f_\text{H} = |f_x - 523\,\text{Hz}|$, and it is the reciprocal of the beat period. The difference does not tell which frequency is higher, so the side is decided by the wax: it lowers $f_x$. If the difference grows, $f_x$ was already below $523\,\text{Hz}$. If the difference shrinks, $f_x$ was above it.
**Reading the figure:** The sound is loudest at the moments $0$, $0.25\,\text{s}$, $0.50\,\text{s}$, $0.75\,\text{s}$ and $1.00\,\text{s}$. The beat period is $T_\text{H} = 0.25\,\text{s}$.
**Model answer:** The beat frequency is $f_\text{H} = \dfrac{1}{0.25\,\text{s}} = 4\,\text{Hz}$, so $f_x = 523\,\text{Hz} \pm 4\,\text{Hz}$, that is $519\,\text{Hz}$ or $527\,\text{Hz}$. The wax lowered $f_x$ and the beats got faster, so the difference grew. That is possible only if $f_x$ was below $523\,\text{Hz}$. The answer is $519\,\text{Hz}$. Check: if $f_x$ had been $527\,\text{Hz}$, the wax would have brought it closer to $523\,\text{Hz}$ and the beats would have slowed down.
