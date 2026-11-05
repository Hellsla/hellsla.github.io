## fy1-3-L1-01
**Given:** $t_1 = 0.52\,\text{s}$, $t_2 = 0.48\,\text{s}$, $t_3 = 0.55\,\text{s}$, $t_4 = 0.49\,\text{s}$; the number of measurements is $n = 4$
**Find:** the mean of the series $\bar{t}$ in the unit $\text{s}$
**Principle:** Every measurement has a random error, which throws the result in one direction or another. When the results are added up and the sum is divided by the number of measurements, the deviations partly cancel each other. So the mean is a better estimate than a single result.
**Formula:** $\bar{t} = \dfrac{t_1 + t_2 + t_3 + t_4}{n}$
**Conversions:** All times are in seconds, so there is no need to convert units.
**Substitution:** The sum is $0.52\,\text{s} + 0.48\,\text{s} + 0.55\,\text{s} + 0.49\,\text{s} = 2.04\,\text{s}$, so $\bar{t} = \dfrac{2.04\,\text{s}}{4} = 0.51\,\text{s}$
**Answer:** $0.51\,\text{s}$, two significant figures like the measurement results (the divisor $4$ is an exact count).
**Reasonableness:** The mean must be between the smallest result $0.48\,\text{s}$ and the largest result $0.55\,\text{s}$, and $0.51\,\text{s}$ is. Check backwards: $4 \cdot 0.51\,\text{s} = 2.04\,\text{s}$ is the sum of the results.

## fy1-3-L1-02
**Given:** true value (reference length) $x_\text{true} = 20.0\,\text{cm}$, measurement result $x = 20.3\,\text{cm}$
**Find:** the measurement error $x - x_\text{true}$ with its sign in the unit $\text{cm}$
**Principle:** The measurement error is the difference between the measurement result and the true value. The sign tells the direction: plus means that the result is too large, and minus that it is too small.
**Formula:** The measurement error is the difference between the result and the true value: $\text{measurement error} = x - x_\text{true}$
**Conversions:** Both lengths are in centimetres, so no conversions are needed.
**Substitution:** $x - x_\text{true} = 20.3\,\text{cm} - 20.0\,\text{cm} = +0.3\,\text{cm}$
**Answer:** $0.3\,\text{cm}$, that is, the result is too large. The difference is known only to one decimal place, because both lengths are given with one decimal place.
**Reasonableness:** The result $20.3\,\text{cm}$ is larger than the true value $20.0\,\text{cm}$, so the error must be positive. Relative to the length the error is $\dfrac{0.3\,\text{cm}}{20.0\,\text{cm}} \approx 1.5\,\%$, which is a large error for a tape measure (a tape is usually accurate to about a millimetre), so the cause is probably systematic, for example a worn start of the tape or a wrong zero.

## fy1-3-L1-03
**Given:** the five results of the figure on the time axis; the smallest result $t_\text{min} = 12.2\,\text{s}$ and the largest $t_\text{max} = 12.9\,\text{s}$
**Find:** half of the range $\Delta t$ in the unit $\text{s}$
**Principle:** The scatter of the results tells the size of the random error. The simplest estimate is half of the range, that is, half of the difference between the largest and the smallest result, because a single result can deviate from the middle in either direction. Only the two extremes determine the range, so the other points are not needed.
**Reading the graph:** The vertical lines of the axis are $0.1\,\text{s}$ apart and the numbers $0.2\,\text{s}$ apart. The leftmost point is on the line $12.2\,\text{s}$, so $t_\text{min} = 12.2\,\text{s}$. The rightmost point is on the line that is one interval to the right of the number $12.8$, so $t_\text{max} = 12.9\,\text{s}$. The other points are at $12.4\,\text{s}$, $12.6\,\text{s}$ and $12.7\,\text{s}$.
**Formula:** $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$
**Conversions:** All times are in seconds, so no conversions are needed.
**Substitution:** $\Delta t = \dfrac{12.9\,\text{s} - 12.2\,\text{s}}{2} = \dfrac{0.7\,\text{s}}{2} = 0.35\,\text{s}$
**Answer:** $0.35\,\text{s}$ is exactly half of the range. The uncertainty is stated with one significant figure, so in a report it is $0.4\,\text{s}$. Both answers are accepted.
**Reasonableness:** In the figure the extreme points are seven squares apart, that is, $0.7\,\text{s}$, and half of it is smaller than the range, as it should be. The middle of the range is $12.55\,\text{s}$, and $12.55\,\text{s} \pm 0.35\,\text{s}$ gives exactly the interval $12.2\,\text{s}$–$12.9\,\text{s}$, onto which all the points fall.

## fy1-3-L1-04
**Given:** the reading of the scale when empty (zero reading) $m_0 = 1.2\,\text{g}$, the reading with the object $m_\text{reading} = 48.7\,\text{g}$
**Find:** the mass of the object $m$ in the unit $\text{g}$
**Principle:** The scale adds the same amount $1.2\,\text{g}$ to every reading, because it already shows it when empty. This is a systematic error, and it is corrected by subtracting the zero reading from the reading.
**Formula:** $m = m_\text{reading} - m_0$
**Conversions:** Both readings are in grams, so no conversions are needed.
**Substitution:** $m = 48.7\,\text{g} - 1.2\,\text{g} = 47.5\,\text{g}$
**Answer:** $47.5\,\text{g}$, three significant figures; both readings are known to one decimal place.
**Reasonableness:** The scale shows too much, so the true mass must be smaller than the reading, and $47.5\,\text{g} < 48.7\,\text{g}$. Check: $47.5\,\text{g} + 1.2\,\text{g} = 48.7\,\text{g}$.

## fy1-3-L1-05
**Given:** the smallest scale division $d = 1.0\,\text{mm}$
**Find:** the uncertainty of the reading $\Delta x$ in the unit $\text{mm}$
**Principle:** A reading is taken from the scale according to the nearest scale mark. In a simple situation the uncertainty of the reading is estimated as half of a scale division; the total uncertainty can be larger if, for example, the edge of the object is unclear or the scale is viewed from the side.
**Formula:** $\Delta x = \dfrac{d}{2}$
**Conversions:** The scale division is already in millimetres, so no conversions are needed.
**Substitution:** $\Delta x = \dfrac{1.0\,\text{mm}}{2} = 0.5\,\text{mm}$
**Answer:** $0.5\,\text{mm}$; the error estimate is a rough estimate, so it is stated with one significant figure.
**Reasonableness:** If $23.0\,\text{mm}$ is read from a ruler, on the basis of the reading the length is estimated to be between $22.5\,\text{mm}$ and $23.5\,\text{mm}$, and this interval is one scale division, that is, $1.0\,\text{mm}$ wide. So the uncertainty of the reading is smaller than a scale division, but the total uncertainty of the measurement can be larger than this.

## fy1-3-L2-01
**Given:** $t = 1.84\,\text{s}$, $1.91\,\text{s}$, $1.78\,\text{s}$, $1.88\,\text{s}$, $1.96\,\text{s}$ and $1.82\,\text{s}$; $n = 6$, $t_\text{min} = 1.78\,\text{s}$, $t_\text{max} = 1.96\,\text{s}$
**Find:** the ratio of the estimate of random error $\Delta t$ to the mean $\bar{t}$ as a percentage
**Principle:** The estimate of random error is half of the range, and the precision of the result is best described by its ratio to the result, the relative uncertainty. The mean is taken as the result, because it reduces the effect of random error.
**Formula:** $\bar{t} = \dfrac{t_1 + \dots + t_6}{n}$, $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$ and $\varepsilon = \dfrac{\Delta t}{\bar{t}} \cdot 100\,\%$
**Conversions:** The times are in seconds and the ratio has no unit. It is multiplied by a hundred to get percent.
**Substitution:** $\bar{t} = \dfrac{11.19\,\text{s}}{6} = 1.865\,\text{s}$ and $\Delta t = \dfrac{1.96\,\text{s} - 1.78\,\text{s}}{2} = 0.09\,\text{s}$, so $\varepsilon = \dfrac{0.09\,\text{s}}{1.865\,\text{s}} \cdot 100\,\% = 4.83\,\%$
**Answer:** $5\,\%$, one significant figure like the error estimate $0.09\,\text{s}$ (calculator value $4.83\,\%$).
**Reasonableness:** Rough estimate: $0.09\,\text{s}$ is about $\tfrac{1}{20}$ of the time $1.87\,\text{s}$, that is, about $5\,\%$. For a hand-timed measurement a random error of a few percent is usual.

## fy1-3-L2-02
**Given:** the length of the rod $L_0 = 1.000\,\text{m}$ and the readings of the tape $L_1 = 1.012\,\text{m}$, $L_2 = 1.009\,\text{m}$, $L_3 = 1.011\,\text{m}$
**Find:** the average error of the tape $\Delta L_\text{sys}$ in the unit $\text{mm}$
**Principle:** The rod is the same length all the time, and the worn start of the tape adds the same amount to every reading: this is a systematic error. The readings vary slightly because of random error, so the error is estimated as the difference between the mean of the readings and the true value.
**Formula:** $\bar{L} = \dfrac{L_1 + L_2 + L_3}{3}$ and $\Delta L_\text{sys} = \bar{L} - L_0$
**Conversions:** The result comes out in metres, and $1\,\text{m} = 1000\,\text{mm}$, so it is multiplied by a thousand.
**Substitution:** The sum is $1.012\,\text{m} + 1.009\,\text{m} + 1.011\,\text{m} = 3.032\,\text{m}$, so $\bar{L} = \dfrac{3.032\,\text{m}}{3} = 1.01067\,\text{m}$ and $\Delta L_\text{sys} = 1.01067\,\text{m} - 1.000\,\text{m} = 0.01067\,\text{m} = 10.67\,\text{mm}$
**Answer:** about $11\,\text{mm}$ (calculator value $10.67\,\text{mm}$): the readings vary by about $\pm 1.5\,\text{mm}$, so the mean should not be stated more precisely than a millimetre.
**Reasonableness:** Each reading is $9\,\text{mm}$–$12\,\text{mm}$ too large, so the mean $11\,\text{mm}$ is between these. The tape shows about $1\,\%$ too much, and the sign of the error is positive, because the readings exceed the true value.

## fy1-3-L2-03
**Given:** $L_1 = 12.4\,\text{cm}$, $L_2 = 0.125\,\text{m}$, $L_3 = 123\,\text{mm}$
**Find:** the mean $\bar{L}$ in the unit $\text{cm}$
**Principle:** A mean can be calculated only from numbers in the same unit, because numbers in different units cannot be added. So convert all results to centimetres first.
**Formula:** $\bar{L} = \dfrac{L_1 + L_2 + L_3}{3}$
**Conversions:** $0.125\,\text{m} = 12.5\,\text{cm}$, because $1\,\text{m} = 100\,\text{cm}$, and $123\,\text{mm} = 12.3\,\text{cm}$, because $10\,\text{mm} = 1\,\text{cm}$.
**Substitution:** The sum is $12.4\,\text{cm} + 12.5\,\text{cm} + 12.3\,\text{cm} = 37.2\,\text{cm}$, so $\bar{L} = \dfrac{37.2\,\text{cm}}{3} = 12.4\,\text{cm}$
**Answer:** $12.4\,\text{cm}$, three significant figures like the measurement results.
**Reasonableness:** The mean is between the smallest result $12.3\,\text{cm}$ and the largest result $12.5\,\text{cm}$. If the numbers had not been converted, the sum $12.4 + 0.125 + 123$ would give the absurd mean $45.2$, so the conversion is necessary.

## fy1-3-L2-04
**Given:** instrument A: $5.2$, $5.6$, $5.4$, $5.3$ and $5.5\,\text{cm}$; instrument B: $5.40$, $5.43$, $5.41$, $5.42$ and $5.44\,\text{cm}$
**Find:** the ratio $k = \dfrac{\Delta x_\text{A}}{\Delta x_\text{B}}$, where $\Delta x$ is half of the range
**Principle:** Half of the range describes the size of the random error, that is, how well the measurement repeats. A smaller half means better repeatability, so the ratio tells how much better one instrument repeats.
**Formula:** $\Delta x = \dfrac{x_\text{max} - x_\text{min}}{2}$ for both instruments, and $k = \dfrac{\Delta x_\text{A}}{\Delta x_\text{B}}$
**Conversions:** All lengths are in centimetres. In the ratio the units cancel, so no conversions are needed.
**Substitution:** $\Delta x_\text{A} = \dfrac{5.6\,\text{cm} - 5.2\,\text{cm}}{2} = 0.2\,\text{cm}$ and $\Delta x_\text{B} = \dfrac{5.44\,\text{cm} - 5.40\,\text{cm}}{2} = 0.02\,\text{cm}$, so $k = \dfrac{0.2\,\text{cm}}{0.02\,\text{cm}} = 10$
**Answer:** $10$ times; the differences $0.4\,\text{cm}$ and $0.04\,\text{cm}$ are one-figure numbers, so the ratio is given with one significant figure.
**Reasonableness:** The results of instrument B fit in an interval $0.04\,\text{cm}$ wide and the results of instrument A in one $0.4\,\text{cm}$ wide, that is, ten times wider. Good repeatability still does not tell whether the mean of instrument B is accurate.

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
**Reasonableness:** The thickness of ordinary copy paper is about $0.1\,\text{mm} = 100\,\mu\text{m}$, so the relative uncertainty is about $2\,\%$. Measuring one sheet directly with a ruler would give an uncertainty of $0.5\,\text{mm}$, that is, about $500\,\%$ of its thickness, so measuring the stack reduces the relative uncertainty to a 250th.

## fy1-3-L3-03
**Given:** true value $x_\text{true} = 8.00\,\text{cm}$; readings $8.24$, $8.27$, $8.25$, $8.29$ and $8.25\,\text{cm}$; $n = 5$
**Find:** the estimate of the systematic error $\Delta x_\text{sys}$ in the unit $\text{cm}$
**Principle:** The readings are close together but all clearly above the true value. The mean reduces random error, so its difference from the true value describes the systematic error that remains.
**Formula:** $\bar{x} = \dfrac{x_1 + \dots + x_5}{n}$ and $\Delta x_\text{sys} = \bar{x} - x_\text{true}$
**Conversions:** All lengths are in centimetres, so no conversions are needed.
**Substitution:** The sum is $8.24\,\text{cm} + 8.27\,\text{cm} + 8.25\,\text{cm} + 8.29\,\text{cm} + 8.25\,\text{cm} = 41.30\,\text{cm}$, so $\bar{x} = \dfrac{41.30\,\text{cm}}{5} = 8.26\,\text{cm}$ and $\Delta x_\text{sys} = 8.26\,\text{cm} - 8.00\,\text{cm} = 0.26\,\text{cm}$
**Answer:** $0.26\,\text{cm}$, two significant figures; the difference is to two decimal places.
**Reasonableness:** The estimate of random error $\dfrac{8.29\,\text{cm} - 8.24\,\text{cm}}{2} = 0.025\,\text{cm} \approx 0.03\,\text{cm}$ is about a tenth of the systematic error, so the error is dominated by the systematic part, for example a wrong zero. If $0.26\,\text{cm}$ is subtracted from all the readings, they are $7.98\,\text{cm}$–$8.03\,\text{cm}$, that is, close to the true value.

## fy1-3-L1-06
**Find:** which of the situations is a systematic error.
**Principle:** A systematic error is almost the same in direction and size in every measurement, for example a wrong zero point of an instrument. A random error varies at random in either direction, and a gross error is a single mistake that shows up as a result differing from the others.
**Model answer:** The systematic error is the wrong zero point of the thermometer: in ice water the thermometer reads about $1.5\,{}^\circ\text{C}$ too high every time, so all readings shift in the same direction. Repeating and averaging do not remove it, but comparison with a known value (ice water is $0\,{}^\circ\text{C}$) reveals it, and the readings are corrected by subtracting the error. The varying moment of stopping the clock and the varying viewing direction are random errors, which the mean reduces. The wrongly recorded number $34.2\,\text{s}$ is a gross error, which is checked and corrected.

## fy1-3-L1-07
**Given:** $x_1 = 5.41\,\text{cm}$, $x_2 = 5.47\,\text{cm}$, $x_3 = 5.39\,\text{cm}$, $x_4 = 5.44\,\text{cm}$, $x_5 = 5.43\,\text{cm}$; $n = 5$
**Find:** the mean $\bar{x}$ in $\text{cm}$, rounded to the precision of the error estimate $\Delta x$
**Principle:** The result is given in the form $\bar{x} \pm \Delta x$. The error estimate is rounded to one significant figure (two if the first figure is 1), and the mean is rounded to the same decimal place, because the figures after the decimal place of the error estimate are already uncertain.
**Formula:** $\bar{x} = \dfrac{x_1 + x_2 + x_3 + x_4 + x_5}{n}$ and $\Delta x = \dfrac{x_\text{max} - x_\text{min}}{2}$
**Conversions:** All lengths are in centimetres, so no conversions are needed.
**Substitution:** The sum of the results is $5.41\,\text{cm} + 5.47\,\text{cm} + 5.39\,\text{cm} + 5.44\,\text{cm} + 5.43\,\text{cm} = 27.14\,\text{cm}$, so $\bar{x} = \dfrac{27.14\,\text{cm}}{5} = 5.428\,\text{cm}$ and $\Delta x = \dfrac{5.47\,\text{cm} - 5.39\,\text{cm}}{2} = 0.04\,\text{cm}$
**Answer:** $5.43\,\text{cm}$, because the error estimate $0.04\,\text{cm}$ is a one-figure number at the hundredths place (the first figure is not 1). The result is $5.43\,\text{cm} \pm 0.04\,\text{cm}$.
**Reasonableness:** The interval $5.43\,\text{cm} \pm 0.04\,\text{cm}$, that is $5.39\,\text{cm}$–$5.47\,\text{cm}$, covers all five results. The result $5.428\,\text{cm}$ would be too precise, because it would imply knowing the width to the thousandths, although the error estimate is in hundredths.

## fy1-3-L1-08
**Given:** the smallest scale division of the ruler $d_\text{r} = 1.0\,\text{mm}$, the smallest step of the calliper display $d_\text{c} = 0.01\,\text{mm}$
**Find:** how many times smaller the uncertainty of the calliper reading $\Delta x_\text{c}$ is than that of the ruler $\Delta x_\text{r}$
**Principle:** The uncertainty of each reading is estimated as half of the smallest reading interval: when reading a scale, the reading is placed between the marks, and a digital display rounds the reading to the nearest step. A smaller reading interval means a smaller reading uncertainty, so the calliper is the more precise instrument. This is an estimate of the reading; the total uncertainty of a measurement can also be affected by the instrument and the method.
**Formula:** $\Delta x = \dfrac{d}{2}$ for both instruments, and the comparison is the ratio $\Delta x_\text{r} : \Delta x_\text{c}$
**Conversions:** Both intervals are in millimetres, so no conversions are needed.
**Substitution:** $\Delta x_\text{r} = \dfrac{1.0\,\text{mm}}{2} = 0.5\,\text{mm}$ and $\Delta x_\text{c} = \dfrac{0.01\,\text{mm}}{2} = 0.005\,\text{mm}$, so $0.5\,\text{mm} : 0.005\,\text{mm} = 100$
**Answer:** $100$ times smaller, one significant figure like the step $0.01\,\text{mm}$. The reading uncertainty of the calliper is a hundredth of that of the ruler.
**Reasonableness:** The ratio is the same as the ratio of the reading intervals $1.0\,\text{mm} : 0.01\,\text{mm} = 100$, because halving cancels out. With a ruler the width is read to half a millimetre and with a calliper to a hundredth of a millimetre, which matches everyday experience that a calliper is more precise.

## fy1-3-L2-05
**Given:** the eight times $t_{10}$ (10 revolutions) of the table: $18.12\,\text{s}$, $18.31\,\text{s}$, $18.05\,\text{s}$, $18.27\,\text{s}$, $18.19\,\text{s}$, $18.35\,\text{s}$, $18.10\,\text{s}$ and $18.22\,\text{s}$; $n = 8$
**Find:** the mean time of one revolution $\bar{T}$ in the unit $\text{s}$
**Principle:** A time taken by hand has a random error, so the result is the mean and the error estimate is half of the range. The time of one revolution is obtained from the time of ten revolutions by dividing both the mean and the error estimate by the exact number $10$.
**Formula:** $\bar{t}_{10} = \dfrac{t_1 + \dots + t_8}{n}$, $\;\Delta t_{10} = \dfrac{t_\text{max} - t_\text{min}}{2}$, $\;\bar{T} = \dfrac{\bar{t}_{10}}{10}$ and $\Delta T = \dfrac{\Delta t_{10}}{10}$
**Conversions:** Not needed: all times are in seconds.
**Substitution:** The sum is $145.61\,\text{s}$, so $\bar{t}_{10} = \dfrac{145.61\,\text{s}}{8} = 18.20125\,\text{s}$ and $\Delta t_{10} = \dfrac{18.35\,\text{s} - 18.05\,\text{s}}{2} = 0.15\,\text{s}$. Thus $\bar{T} = \dfrac{18.20125\,\text{s}}{10} = 1.820125\,\text{s}$ and $\Delta T = \dfrac{0.15\,\text{s}}{10} = 0.015\,\text{s}$.
**Answer:** $\bar{T} = 1.820\,\text{s}$, that is $1.82\,\text{s}$. The error estimate $0.015\,\text{s}$ is a two-figure number because the first figure is 1, so the result is rounded to thousandths: $T = 1.820\,\text{s} \pm 0.015\,\text{s}$.
**Reasonableness:** The usual speed of a turntable is $33.33$ revolutions per minute, so one revolution takes $60\,\text{s} : 33.33 = 1.800\,\text{s}$. The measured $1.820\,\text{s} \pm 0.015\,\text{s}$ has the right order of magnitude, but $1.800\,\text{s}$ falls just outside that interval; the turntable may therefore be turning slightly slowly, or the timing may have a small systematic error. Timing ten revolutions reduces the relative share of the reaction time: the error estimate $0.15\,\text{s}$ is only about $0.8\,\%$ of the time $18.2\,\text{s}$.

## fy1-3-L2-06
**Given:** known volume $V_\text{true} = 50.0\,\text{ml}$; the results of group A $50.9\,\text{ml}$, $51.1\,\text{ml}$, $50.8\,\text{ml}$, $51.0\,\text{ml}$, $50.9\,\text{ml}$ and the results of group B $49.4\,\text{ml}$, $50.5\,\text{ml}$, $49.8\,\text{ml}$, $50.3\,\text{ml}$, $50.1\,\text{ml}$
**Find:** the deviation of the mean of series A $\bar{V}_\text{A} - V_\text{true}$ with its sign in $\text{ml}$; which series is more repeatable and which is closer to the true value
**Principle:** Repeatability tells about random error, and it is described by the half-range $\Delta V$. The difference between the mean and the known value tells about systematic error, which repeating does not reduce.
**Formula:** $\bar{V} = \dfrac{V_1 + \dots + V_5}{n}$, $\;\Delta V = \dfrac{V_\text{max} - V_\text{min}}{2}$ and deviation $\bar{V}_\text{A} - V_\text{true}$
**Conversions:** Not needed: all volumes are in millilitres.
**Substitution:** $\bar{V}_\text{A} = \dfrac{254.7\,\text{ml}}{5} = 50.94\,\text{ml}$, so the deviation is $50.94\,\text{ml} - 50.0\,\text{ml} = 0.94\,\text{ml}$. In addition $\Delta V_\text{A} = \dfrac{51.1\,\text{ml} - 50.8\,\text{ml}}{2} = 0.15\,\text{ml}$ and $\Delta V_\text{B} = \dfrac{50.5\,\text{ml} - 49.4\,\text{ml}}{2} = 0.55\,\text{ml}$; $\bar{V}_\text{B} = 50.02\,\text{ml}$.
**Answer:** $+0.94\,\text{ml}$. The readings are three-figure numbers, and since the error estimate $\Delta V_\text{A} = 0.15\,\text{ml}$ is to hundredths, the deviation is also given in hundredths. Series A is more repeatable ($0.15\,\text{ml} < 0.55\,\text{ml}$), but all its results are over $50\,\text{ml}$, so it has a systematic error. The mean of series B is closer to the true value, although its scatter is larger.
**Reasonableness:** All of A's results are on the same side of the true value, and the deviation $0.94\,\text{ml}$ is a multiple of the scatter $\Delta V_\text{A} = 0.15\,\text{ml}$, so the deviation is probably not random. Good repeatability therefore does not guarantee a correct result.

## fy1-3-L2-07
**Given:** period $T \approx 1.5\,\text{s}$; uncertainty due to reaction time for the whole measured time $\Delta t = 0.2\,\text{s}$ (an estimate); required relative uncertainty at most $1\,\%$
**Find:** the minimum number of swings $N$
**Principle:** Reaction time acts once at the start and once at the end, whether the measured time is short or long. When $N$ swings are timed and the time is divided by $N$, the uncertainty is divided by $N$ as well.
**Formula:** $\Delta T = \dfrac{\Delta t}{N}$ and the requirement $\dfrac{\Delta T}{T} \le 0.01$, so $\dfrac{\Delta t}{N \cdot T} \le 0.01$, from which $N \ge \dfrac{\Delta t}{0.01 \cdot T}$
**Conversions:** Not needed: all times are in seconds, and $1\,\% = 0.01$.
**Substitution:** $N \ge \dfrac{0.2\,\text{s}}{0.01 \cdot 1.5\,\text{s}} = 13.33\ldots$
**Answer:** At least $14$ swings must be timed, because $N$ is an integer and $13$ is not enough ($0.2 : (13 \cdot 1.5) = 1.03\,\%$).
**Reasonableness:** Check: $N = 14$ gives $\Delta T = 0.2\,\text{s} : 14 = 0.014\,\text{s}$ and $0.014\,\text{s} : 1.5\,\text{s} = 0.95\,\%$, so the requirement is met. Timing a single swing would give the uncertainty $0.2 : 1.5 = 13\,\%$.
**Model answer:** The error from reaction time does not grow with the length of the time; it is about the same at the start and at the end. A long measurement is divided among many swings, so the share per swing becomes smaller. Repeating also reduces random error through the mean.

## fy1-3-L3-04
**Given:** the eight times of the table; the sixth result $2.97\,\text{s}$ differs from the others, and the laboratory notebook has a note at it that the clock was stopped late
**Find:** may the result be left out, the mean $\bar{t}$ in $\text{s}$, and what would be done if no reason had been recorded
**Principle:** A clearly deviating result is checked, but it is not removed merely because it deviates. It may be left out only if the reason for the gross error is found and the omission is justified and recorded. Here the notebook note gives the reason: the clock was stopped late. If no reason is found, the result stays in the data and the deviation is described in the uncertainty.
**Formula:** $\bar{t} = \dfrac{t_1 + \dots + t_n}{n}$, where $n = 7$ remaining results
**Conversions:** Not needed: all times are in seconds.
**Substitution:** The sum of the results is $2.41\,\text{s} + 2.38\,\text{s} + 2.44\,\text{s} + 2.40\,\text{s} + 2.43\,\text{s} + 2.39\,\text{s} + 2.42\,\text{s} = 16.87\,\text{s}$, so $\bar{t} = \dfrac{16.87\,\text{s}}{7} = 2.41\,\text{s}$
**Answer:** The result may be left out, because the notebook note gives the reason and the omission is recorded; the mean is $2.41\,\text{s}$, three significant figures like the measurements. The half-range is $(2.44\,\text{s} - 2.38\,\text{s}) : 2 = 0.03\,\text{s}$. If no reason had been found, the result would stay in the data: the mean would be $19.84\,\text{s} : 8 = 2.48\,\text{s}$ and the half-range $(2.97\,\text{s} - 2.38\,\text{s}) : 2 = 0.30\,\text{s}$, ten times as large. The result would be given with this uncertainty, the deviation would be mentioned, and it would be worth repeating the measurement.
**Reasonableness:** With the deviating result the mean shifts by $0.07\,\text{s}$, which is over twice the half-range $0.03\,\text{s}$. The omission is based on the recorded reason and not on the size of the deviation $2.97\,\text{s} - 2.41\,\text{s} = 0.56\,\text{s}$: on the basis of the notebook note the result is a gross error.

## fy1-3-L3-05
**Given:** $\rho_\text{A} = 2.74\,\text{g/cm}^3$, $\Delta\rho_\text{A} = 0.05\,\text{g/cm}^3$; $\rho_\text{B} = 2.60\,\text{g/cm}^3$, $\Delta\rho_\text{B} = 0.05\,\text{g/cm}^3$; the student's conclusion: the difference is about $5\,\%$, so the results are consistent
**Find:** the error in the student's reasoning, whether the results are consistent, and the gap $E$ between the uncertainty intervals in $\text{g/cm}^3$
**Principle:** The consistency of two results is judged with uncertainty intervals, not with the percentage by which the results differ. If the intervals $\rho \pm \Delta\rho$ overlap, a difference cannot be shown; if they do not, the difference is greater than the stated uncertainties explain. The uncertainties are estimates, not certain limits.
**Formula:** the gap is the difference between the difference of the results and the sum of the uncertainties: $E = |\rho_\text{A} - \rho_\text{B}| - (\Delta\rho_\text{A} + \Delta\rho_\text{B})$
**Conversions:** Not needed: all values are in $\text{g/cm}^3$.
**Substitution:** $E = |2.74\,\text{g/cm}^3 - 2.60\,\text{g/cm}^3| - (0.05\,\text{g/cm}^3 + 0.05\,\text{g/cm}^3) = 0.14\,\text{g/cm}^3 - 0.10\,\text{g/cm}^3 = 0.04\,\text{g/cm}^3$
**Answer:** $0.04\,\text{g/cm}^3$, two decimal places like the results. The student's error is to judge consistency by the percentage difference: the intervals $2.69$–$2.79\,\text{g/cm}^3$ and $2.55$–$2.65\,\text{g/cm}^3$ do not overlap, and a gap of $0.04\,\text{g/cm}^3$ is left between them. According to these estimates the difference is greater than the stated uncertainties explain, so the results differ from each other; the cause is worth looking for, for example in a systematic error. The difference still does not prove either result wrong.
**Reasonableness:** The uncertainties are about $2\,\%$ of the results, so the $5\,\%$ difference is over twice as large as they are. If B were $2.66\,\text{g/cm}^3$, the intervals would overlap although the results would still differ by $0.08\,\text{g/cm}^3$.

## fy1-3-L2-08
**Given:** light ball: $14.3\,\text{s}$, $14.1\,\text{s}$, $14.4\,\text{s}$, $14.2\,\text{s}$, $14.5\,\text{s}$; heavy ball: $14.4\,\text{s}$, $14.2\,\text{s}$, $14.5\,\text{s}$, $14.3\,\text{s}$, $14.4\,\text{s}$; uncertainty of the hand-timed measurement $\Delta t = 0.2\,\text{s}$ for each result
**Find:** which conclusion the data support when the difference of the averages is compared with the uncertainty $\Delta t$
**Principle:** The difference of two averages is compared with the uncertainty. If the difference is smaller than the uncertainty, a difference cannot be shown by the measurement; this does not, however, prove that the quantities are equal. A result must also not be given more precisely than the uncertainty allows.
**Model answer:** The averages given by the calculator are $\bar{t}_\text{light} = \dfrac{71.5\,\text{s}}{5} = 14.30\,\text{s}$ and $\bar{t}_\text{heavy} = \dfrac{71.8\,\text{s}}{5} = 14.36\,\text{s}$, so the difference is $14.36\,\text{s} - 14.30\,\text{s} = 0.06\,\text{s}$. This is a third of the uncertainty $0.2\,\text{s}$ and smaller than half the range of either series ($0.2\,\text{s}$ and $0.15\,\text{s}$), so the difference can be mere random variation. The correct conclusion is that the data do not show that the mass of the ball affects the swing time. The claim "the heavy ball swings more slowly" goes beyond the data, because it treats a difference within the uncertainty as real. The claim "mass has no effect" goes too far, because the measurement cannot tell apart even a small real difference. The time of ten swings $14.300\,\text{s}$ is over-precise, because the uncertainty $0.2\,\text{s}$ allows only a tenth of a second, for example a time of ten swings of $14.3\,\text{s} \pm 0.2\,\text{s}$ (the time of one swing is about $1.43\,\text{s} \pm 0.02\,\text{s}$). To detect a difference, more accurate timing would be needed, for example a light gate, or a longer measured time.
