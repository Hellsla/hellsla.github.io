## fy1-3-L1-01
**Given:** $t_1 = 0.52\,\text{s}$, $t_2 = 0.48\,\text{s}$, $t_3 = 0.55\,\text{s}$, $t_4 = 0.49\,\text{s}$; the number of measurements is $n = 4$
**Find:** the mean of the series $\bar{t}$ in the unit $\text{s}$
**Principle:** Every measurement has a random error, which throws the result in one direction or another. When the results are added up and the sum is divided by the number of measurements, the deviations partly cancel each other. So the mean is a better estimate than a single result.
**Formula:** $\bar{t} = \dfrac{t_1 + t_2 + t_3 + t_4}{n}$. The formula is already solved for the quantity to find: $\bar{t} = \dfrac{t_1 + t_2 + t_3 + t_4}{n}$
**Conversions:** All times are in seconds, so there is no need to convert units.
**Substitution:** The sum is $0.52\,\text{s} + 0.48\,\text{s} + 0.55\,\text{s} + 0.49\,\text{s} = 2.04\,\text{s}$, so $\bar{t} = \dfrac{2.04\,\text{s}}{4} = 0.51\,\text{s}$
**Answer:** $0.51\,\text{s}$, two significant figures like the measurement results (the divisor $4$ is an exact count).
**Reasonableness:** The mean must be between the smallest result $0.48\,\text{s}$ and the largest result $0.55\,\text{s}$, and $0.51\,\text{s}$ is. Check backwards: $4 \cdot 0.51\,\text{s} = 2.04\,\text{s}$ is the sum of the results.

## fy1-3-L1-02
**Given:** true value (reference length) $x_\text{true} = 20.0\,\text{cm}$, measurement result $x = 20.3\,\text{cm}$
**Find:** the measurement error $\Delta x$ with its sign in the unit $\text{cm}$
**Principle:** The measurement error is the difference between the measurement result and the true value. The sign tells the direction: plus means that the result is too large, and minus that it is too small.
**Formula:** $\Delta x = x - x_\text{true}$. The formula is already solved for the quantity to find: $\Delta x = x - x_\text{true}$
**Conversions:** Both lengths are in centimetres, so no conversions are needed.
**Substitution:** $\Delta x = 20.3\,\text{cm} - 20.0\,\text{cm} = +0.3\,\text{cm}$
**Answer:** $0.3\,\text{cm}$, that is, the result is too large. The difference is known only to one decimal place, because both lengths are given with one decimal place.
**Reasonableness:** The result $20.3\,\text{cm}$ is larger than the true value $20.0\,\text{cm}$, so the error must be positive. Relative to the length the error is $\dfrac{0.3\,\text{cm}}{20.0\,\text{cm}} \approx 1.5\,\%$, which is a large error for a tape measure (a tape is usually accurate to about a millimetre), so the cause is probably systematic, for example a worn start of the tape or a wrong zero.

## fy1-3-L1-03
**Given:** $t = 12.4\,\text{s}$, $12.9\,\text{s}$, $12.6\,\text{s}$, $12.2\,\text{s}$ and $12.7\,\text{s}$; the smallest result $t_\text{min} = 12.2\,\text{s}$ and the largest $t_\text{max} = 12.9\,\text{s}$
**Find:** half of the range $\Delta t$ in the unit $\text{s}$
**Principle:** The scatter of the results tells the size of the random error. The simplest estimate is half of the range, that is, half of the difference between the largest and the smallest result, because a single result can deviate from the middle in either direction.
**Formula:** $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$. The formula is already solved for the quantity to find: $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$
**Conversions:** All times are in seconds, so no conversions are needed.
**Substitution:** $\Delta t = \dfrac{12.9\,\text{s} - 12.2\,\text{s}}{2} = \dfrac{0.7\,\text{s}}{2} = 0.35\,\text{s}$
**Answer:** $0.35\,\text{s}$, two significant figures; the divisor $2$ is an exact number. This is exactly half of the range. As a stated error estimate it would be rounded to one significant figure, $0.4\,\text{s}$.
**Reasonableness:** The range is $0.7\,\text{s}$, and half of it is smaller than the range, as it should be. The middle of the range is $12.55\,\text{s}$, and $12.55\,\text{s} \pm 0.35\,\text{s}$ gives exactly the interval $12.2\,\text{s}$–$12.9\,\text{s}$.

## fy1-3-L1-04
**Given:** the reading of the scale when empty (zero reading) $m_0 = 1.2\,\text{g}$, the reading with the object $m_\text{reading} = 48.7\,\text{g}$
**Find:** the mass of the object $m$ in the unit $\text{g}$
**Principle:** The scale adds the same amount $1.2\,\text{g}$ to every reading, because it already shows it when empty. This is a systematic error, and it is corrected by subtracting the zero reading from the reading.
**Formula:** $m = m_\text{reading} - m_0$. The formula is already solved for the quantity to find: $m = m_\text{reading} - m_0$
**Conversions:** Both readings are in grams, so no conversions are needed.
**Substitution:** $m = 48.7\,\text{g} - 1.2\,\text{g} = 47.5\,\text{g}$
**Answer:** $47.5\,\text{g}$, three significant figures; both readings are known to one decimal place.
**Reasonableness:** The scale shows too much, so the true mass must be smaller than the reading, and $47.5\,\text{g} < 48.7\,\text{g}$. Check: $47.5\,\text{g} + 1.2\,\text{g} = 48.7\,\text{g}$.

## fy1-3-L1-05
**Given:** the smallest scale division $d = 1.0\,\text{mm}$
**Find:** the error estimate of a single reading $\Delta x$ in the unit $\text{mm}$
**Principle:** A reading is taken from the scale according to the nearest scale mark. The true value can be anything between two marks, so the reading can be wrong by at most half of a scale division.
**Formula:** $\Delta x = \dfrac{d}{2}$. The formula is already solved for the quantity to find: $\Delta x = \dfrac{d}{2}$
**Conversions:** The scale division is already in millimetres, so no conversions are needed.
**Substitution:** $\Delta x = \dfrac{1.0\,\text{mm}}{2} = 0.5\,\text{mm}$
**Answer:** $0.5\,\text{mm}$; the error estimate is a rough estimate, so it is stated with one significant figure.
**Reasonableness:** If $23.0\,\text{mm}$ is read from a ruler, the true length is between $22.5\,\text{mm}$ and $23.5\,\text{mm}$, and this interval is one scale division, that is, $1.0\,\text{mm}$ wide. The error estimate cannot be larger than a scale division.

## fy1-3-L2-01
**Given:** $t = 1.84\,\text{s}$, $1.91\,\text{s}$, $1.78\,\text{s}$, $1.88\,\text{s}$, $1.96\,\text{s}$ and $1.82\,\text{s}$; $n = 6$, $t_\text{min} = 1.78\,\text{s}$, $t_\text{max} = 1.96\,\text{s}$
**Find:** the ratio of the estimate of random error $\Delta t$ to the mean $\bar{t}$ as a percentage
**Principle:** The estimate of random error is half of the range, and the precision of the result is best described by its ratio to the result, the relative error. The mean is taken as the result, because it reduces the effect of random error.
**Formula:** $\bar{t} = \dfrac{t_1 + \dots + t_6}{n}$, $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$ and $\varepsilon = \dfrac{\Delta t}{\bar{t}} \cdot 100\,\%$. The quantity to find is $\varepsilon = \dfrac{\Delta t}{\bar{t}} \cdot 100\,\%$
**Conversions:** The times are in seconds and the ratio has no unit. It is multiplied by a hundred to get percent.
**Substitution:** $\bar{t} = \dfrac{11.19\,\text{s}}{6} = 1.865\,\text{s}$ and $\Delta t = \dfrac{1.96\,\text{s} - 1.78\,\text{s}}{2} = 0.09\,\text{s}$, so $\varepsilon = \dfrac{0.09\,\text{s}}{1.865\,\text{s}} \cdot 100\,\% = 4.83\,\%$
**Answer:** $5\,\%$, one significant figure like the error estimate $0.09\,\text{s}$ (calculator value $4.83\,\%$).
**Reasonableness:** Rough estimate: $0.09\,\text{s}$ is about $\tfrac{1}{20}$ of the time $1.87\,\text{s}$, that is, about $5\,\%$. For a hand-timed measurement a random error of a few percent is usual.

## fy1-3-L2-02
**Given:** the length of the rod $L_0 = 1.000\,\text{m}$ and the readings of the tape $L_1 = 1.012\,\text{m}$, $L_2 = 1.009\,\text{m}$, $L_3 = 1.011\,\text{m}$
**Find:** the average error of the tape $\Delta L_\text{sys}$ in the unit $\text{mm}$
**Principle:** The rod is the same length all the time, and the worn start of the tape adds the same amount to every reading: this is a systematic error. The readings vary slightly because of random error, so the error is estimated as the difference between the mean of the readings and the true value.
**Formula:** $\bar{L} = \dfrac{L_1 + L_2 + L_3}{3}$ and $\Delta L_\text{sys} = \bar{L} - L_0$. The quantity to find is $\Delta L_\text{sys} = \bar{L} - L_0$
**Conversions:** The result comes out in metres, and $1\,\text{m} = 1000\,\text{mm}$, so it is multiplied by a thousand.
**Substitution:** The sum is $1.012\,\text{m} + 1.009\,\text{m} + 1.011\,\text{m} = 3.032\,\text{m}$, so $\bar{L} = \dfrac{3.032\,\text{m}}{3} = 1.01067\,\text{m}$ and $\Delta L_\text{sys} = 1.01067\,\text{m} - 1.000\,\text{m} = 0.01067\,\text{m} = 10.67\,\text{mm}$
**Answer:** $10.7\,\text{mm}$, three significant figures: the readings are to a millimetre, and the mean of three readings carries one more figure.
**Reasonableness:** Each reading is $9\,\text{mm}$–$12\,\text{mm}$ too large, so the mean $10.7\,\text{mm}$ is between these. The tape shows about $1\,\%$ too much, and the sign of the error is positive, because the readings exceed the true value.

## fy1-3-L2-03
**Given:** $L_1 = 12.4\,\text{cm}$, $L_2 = 0.125\,\text{m}$, $L_3 = 123\,\text{mm}$
**Find:** the mean $\bar{L}$ in the unit $\text{cm}$
**Principle:** A mean can be calculated only from numbers in the same unit, because numbers in different units cannot be added. So convert all results to centimetres first.
**Formula:** $\bar{L} = \dfrac{L_1 + L_2 + L_3}{3}$. The formula is already solved for the quantity to find: $\bar{L} = \dfrac{L_1 + L_2 + L_3}{3}$
**Conversions:** $0.125\,\text{m} = 12.5\,\text{cm}$, because $1\,\text{m} = 100\,\text{cm}$, and $123\,\text{mm} = 12.3\,\text{cm}$, because $10\,\text{mm} = 1\,\text{cm}$.
**Substitution:** The sum is $12.4\,\text{cm} + 12.5\,\text{cm} + 12.3\,\text{cm} = 37.2\,\text{cm}$, so $\bar{L} = \dfrac{37.2\,\text{cm}}{3} = 12.4\,\text{cm}$
**Answer:** $12.4\,\text{cm}$, three significant figures like the measurement results.
**Reasonableness:** The mean is between the smallest result $12.3\,\text{cm}$ and the largest result $12.5\,\text{cm}$. If the numbers had not been converted, the sum $12.4 + 0.125 + 123$ would give the absurd mean $45.2$, so the conversion is necessary.

## fy1-3-L2-04
**Given:** instrument A: $5.2$, $5.6$, $5.4$, $5.3$ and $5.5\,\text{cm}$; instrument B: $5.40$, $5.43$, $5.41$, $5.42$ and $5.44\,\text{cm}$
**Find:** the ratio $k = \dfrac{\Delta x_\text{A}}{\Delta x_\text{B}}$, where $\Delta x$ is half of the range
**Principle:** Half of the range describes the size of the random error, that is, how well the measurement repeats. A smaller half means better repeatability, so the ratio tells how much better one instrument repeats.
**Formula:** $\Delta x = \dfrac{x_\text{max} - x_\text{min}}{2}$ for both instruments, and $k = \dfrac{\Delta x_\text{A}}{\Delta x_\text{B}}$. The quantity to find is $k = \dfrac{\Delta x_\text{A}}{\Delta x_\text{B}}$
**Conversions:** All lengths are in centimetres. In the ratio the units cancel, so no conversions are needed.
**Substitution:** $\Delta x_\text{A} = \dfrac{5.6\,\text{cm} - 5.2\,\text{cm}}{2} = 0.2\,\text{cm}$ and $\Delta x_\text{B} = \dfrac{5.44\,\text{cm} - 5.40\,\text{cm}}{2} = 0.02\,\text{cm}$, so $k = \dfrac{0.2\,\text{cm}}{0.02\,\text{cm}} = 10$
**Answer:** $10$ times; the differences $0.4\,\text{cm}$ and $0.04\,\text{cm}$ are one-figure numbers, so the ratio is given with one significant figure.
**Reasonableness:** The results of instrument B fit in an interval $0.04\,\text{cm}$ wide and the results of instrument A in one $0.4\,\text{cm}$ wide, that is, ten times wider. Good repeatability still does not tell whether the mean of instrument B is correct.

## fy1-3-L3-01
**Given:** starting delay $\tau_1 = 0.18\,\text{s}$ (the stopwatch starts too late), stopping delay $\tau_2 = 0.12\,\text{s}$ (the stopwatch stops too late)
**Find:** the systematic error $\Delta t_\text{sys}$ = reading − true time, with its sign, in the unit $\text{s}$
**Principle:** The delays are the same in every measurement, so they are systematic. A stopwatch that starts late lags behind and the reading is too short, and a stopwatch that stops late shows too much. So the delays act in opposite directions.
**Formula:** reading $= t_\text{true} - \tau_1 + \tau_2$, so the error is $\Delta t_\text{sys} = \tau_2 - \tau_1$
**Conversions:** Both delays are in seconds, so no conversions are needed.
**Substitution:** $\Delta t_\text{sys} = 0.12\,\text{s} - 0.18\,\text{s} = -0.06\,\text{s}$
**Answer:** $-0.06\,\text{s}$, two decimal places like the delays. The minus sign tells that the reading is too short.
**Reasonableness:** The starting delay is larger than the stopping delay, so the reading comes out short, and the sign is negative. The delays cancel each other almost completely: the error is only a third of the starting delay. If the reading were $3.44\,\text{s}$, the true time would be $3.50\,\text{s}$.

## fy1-3-L3-02
**Given:** the number of sheets $n = 250$, the smallest scale division $d = 1.0\,\text{mm}$
**Find:** the error estimate of the thickness of one sheet $\Delta h_1$ in the unit $\mu\text{m}$
**Principle:** The thickness of the stack is the sum of $n$ equally thick sheets, $h = n h_1$. The thickness of the stack has a reading error, and because the number of sheets is exact, the error of the thickness of one sheet is the error of the stack divided by $n$.
**Formula:** $\Delta h = \dfrac{d}{2}$ and $\Delta h_1 = \dfrac{\Delta h}{n}$, so $\Delta h_1 = \dfrac{d}{2n}$
**Conversions:** The result comes out in millimetres, and $1\,\text{mm} = 1000\,\mu\text{m}$, so it is multiplied by a thousand.
**Substitution:** $\Delta h_1 = \dfrac{1.0\,\text{mm}}{2 \cdot 250} = \dfrac{0.5\,\text{mm}}{250} = 0.0020\,\text{mm} = 2.0\,\mu\text{m}$
**Answer:** $2\,\mu\text{m}$, one significant figure, because the error estimate is rounded to one significant figure; the number of sheets is an exact number.
**Reasonableness:** The thickness of ordinary copy paper is about $0.1\,\text{mm} = 100\,\mu\text{m}$, so the error estimate is about $2\,\%$. Measuring one sheet directly with a ruler would give an error of $0.5\,\text{mm}$, that is, about $500\,\%$, so measuring the stack reduces the relative error to a 250th.

## fy1-3-L3-03
**Given:** true value $x_\text{true} = 8.00\,\text{cm}$; readings $8.24$, $8.27$, $8.25$, $8.29$ and $8.25\,\text{cm}$; $n = 5$
**Find:** the estimate of the systematic error $\Delta x_\text{sys}$ in the unit $\text{cm}$
**Principle:** The readings are tightly close to each other but all clearly above the true value. The mean reduces random error, so its difference from the true value describes the systematic error that remains.
**Formula:** $\bar{x} = \dfrac{x_1 + \dots + x_5}{n}$ and $\Delta x_\text{sys} = \bar{x} - x_\text{true}$. The quantity to find is $\Delta x_\text{sys} = \bar{x} - x_\text{true}$
**Conversions:** All lengths are in centimetres, so no conversions are needed.
**Substitution:** The sum is $8.24\,\text{cm} + 8.27\,\text{cm} + 8.25\,\text{cm} + 8.29\,\text{cm} + 8.25\,\text{cm} = 41.30\,\text{cm}$, so $\bar{x} = \dfrac{41.30\,\text{cm}}{5} = 8.26\,\text{cm}$ and $\Delta x_\text{sys} = 8.26\,\text{cm} - 8.00\,\text{cm} = 0.26\,\text{cm}$
**Answer:** $0.26\,\text{cm}$, two significant figures; the difference is to two decimal places.
**Reasonableness:** The estimate of random error $\dfrac{8.29\,\text{cm} - 8.24\,\text{cm}}{2} = 0.025\,\text{cm} \approx 0.03\,\text{cm}$ is about a tenth of the systematic error, so the error is dominated by the systematic part, for example a wrong zero. If $0.26\,\text{cm}$ is subtracted from all the readings, they are $7.98\,\text{cm}$–$8.03\,\text{cm}$, that is, close to the true value.
