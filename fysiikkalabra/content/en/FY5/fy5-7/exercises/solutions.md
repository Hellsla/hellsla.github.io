## fy5-7-L1-01
**Given:** period $T = 0.40\,\text{s}$
**Find:** the frequency $f$ of the oscillation in $\text{Hz}$
**Principle:** The frequency is the number of full oscillations per unit time. When one oscillation takes the time $T$, $\tfrac{1}{T}$ oscillations are completed in a second, so the frequency is the reciprocal of the period.
**Formula:** $f = \dfrac{1}{T}$
**Conversions:** None needed: the period is in seconds, so the frequency comes out in the unit $\tfrac{1}{\text{s}} = \text{Hz}$.
**Substitution:** $f = \dfrac{1}{0.40\,\text{s}} = 2.5\,\text{Hz}$
**Answer:** $2.5\,\text{Hz}$, two significant figures as in the period $0.40\,\text{s}$.
**Reasonableness:** Check in the other direction: $2.5$ oscillations per second means that one oscillation takes $\tfrac{1\,\text{s}}{2.5} = 0.40\,\text{s}$, as in the task. A weight bouncing on a spring often makes a few oscillations per second, so the order of magnitude fits.

## fy5-7-L1-02
**Given:** frequency $f = 196\,\text{Hz}$
**Find:** the period $T$ in milliseconds
**Principle:** The period is the duration of one oscillation, and the frequency is the number of oscillations per second. They are reciprocals of each other, so the period is obtained by solving it from the formula of the frequency.
**Formula:** $f = \dfrac{1}{T}$, from which $T = \dfrac{1}{f}$
**Conversions:** $1\,\text{Hz} = 1\,\tfrac{1}{\text{s}}$, so the period comes out in seconds; finally $1\,\text{s} = 1000\,\text{ms}$.
**Substitution:** $T = \dfrac{1}{196\,\tfrac{1}{\text{s}}} = 0.005102\,\text{s} = 0.005102 \cdot 1000\,\text{ms} = 5.102\,\text{ms}$
**Answer:** $5.10\,\text{ms}$, three significant figures as in the frequency $196\,\text{Hz}$.
**Reasonableness:** An estimate with round numbers: at the frequency $200\,\text{Hz}$ the period would be $\tfrac{1}{200}\,\text{s} = 5\,\text{ms}$. The frequency is a little lower, so the period is a little longer, like $5.10\,\text{ms}$. The vibration of a string is so fast that the eye cannot follow it, which fits the order of magnitude of milliseconds.

## fy5-7-L1-03
**Given:** a graph of the displacement $x$ of a weight as a function of time $t$ from $0$ to $3.0\,\text{s}$
**Find:** the amplitude $A$ of the oscillation in centimetres
**Principle:** The amplitude is the greatest displacement from the equilibrium position. At the equilibrium position $x = 0$, so the amplitude is read from the level of the dashed line $x = 0$ to the level of a peak of the curve, not from a peak to a trough.
**Reading the graph:** The peaks of the curve are at the grid line between $2$ and $3$ on the vertical axis, that is, at $x = 2.5\,\text{cm}$, and the troughs correspondingly at $x = -2.5\,\text{cm}$. So a peak is $2.5\,\text{cm}$ above the equilibrium position.
**Formula:** $A = x_\text{peak} - 0$, that is, $A = x_\text{peak}$
**Conversions:** None needed: the values of the vertical axis are in centimetres.
**Substitution:** $A = 2.5\,\text{cm} - 0\,\text{cm} = 2.5\,\text{cm}$
**Answer:** $2.5\,\text{cm}$, two significant figures, because the value is read from a half-centimetre grid line.
**Reasonableness:** Another route: the distance between a peak and a trough is $2.5\,\text{cm} - (-2.5\,\text{cm}) = 5.0\,\text{cm}$, and the amplitude is half of it, $2.5\,\text{cm}$. The value $5.0\,\text{cm}$ would be the distance $2A$ between the extreme positions.

## fy5-7-L1-04
**Given:** number of full swings $n = 20$, their duration $t_n = 36\,\text{s}$
**Find:** the period $T$ of the pendulum in seconds
**Principle:** The period is the duration of one full swing. When the swings are alike, one takes the fraction $\tfrac{1}{n}$ of the duration of all of them. A period calculated from the time of several swings is more precise than a measurement of one swing.
**Formula:** $T = \dfrac{t_n}{n}$
**Conversions:** None needed: the time is in seconds, and the number of swings is a dimensionless number.
**Substitution:** $T = \dfrac{36\,\text{s}}{20} = 1.8\,\text{s}$
**Answer:** $1.8\,\text{s}$, two significant figures as in the time $36\,\text{s}$; the number of swings $20$ is counted exactly.
**Reasonableness:** Check by multiplying: $20 \cdot 1.8\,\text{s} = 36\,\text{s}$. The frequency is $\tfrac{1}{1.8\,\text{s}} \approx 0.56\,\text{Hz}$, so the pendulum makes a little over half a swing per second, which fits the long pendulum of a floor-standing pendulum clock.

## fy5-7-L1-05
**Given:** amplitude $A = 4.0\,\text{cm}$
**Find:** the distance $s$ travelled during one period in centimetres
**Principle:** During one full oscillation the weight leaves the equilibrium position, rises to the highest position (distance $A$), falls to the lowest position (distance $2A$) and returns to the equilibrium position (distance $A$). The distance travelled is the sum of these, although the weight ends up at the same place from which it started.
**Formula:** $s = A + 2A + A$, that is, $s = 4A$
**Conversions:** None needed: the amplitude is in centimetres, and the answer is asked in centimetres.
**Substitution:** $s = 4 \cdot 4.0\,\text{cm} = 16\,\text{cm}$
**Answer:** $16\,\text{cm}$, two significant figures as in the amplitude $4.0\,\text{cm}$.
**Reasonableness:** The distance between the extreme positions is $2A = 8.0\,\text{cm}$, and during a period the weight travels it twice, up and down: $2 \cdot 8.0\,\text{cm} = 16\,\text{cm}$. The displacement of the weight during a period is, however, zero, because it returns to its starting place.

## fy5-7-L2-01
**Given:** a graph of the displacement $x$ of a cart as a function of time $t$ according to the sine model, time $t = 0.10\,\text{s}$
**Find:** the displacement $x$ of the cart from the equilibrium position in centimetres at the moment $t$
**Principle:** The graph is a sine curve that starts from the equilibrium position going up, so the displacement is described by the model $x = A \sin\left(\tfrac{2\pi t}{T}\right)$. The coefficients $A$ and $T$ of the model are read from the graph, and then the displacement is calculated at the desired moment.
**Reading the graph:** The peaks are at the grid line $x = 3.0\,\text{cm}$, so $A = 3.0\,\text{cm}$. The curve passes the equilibrium position going up at the times $0$, $0.50\,\text{s}$ and $1.0\,\text{s}$, so one oscillation takes $T = 0.50\,\text{s}$. The value at the time $0.10\,\text{s}$ cannot be read accurately from the graph, because there is no grid line there, so it is calculated.
**Formula:** $x = A \sin\left(\dfrac{2\pi t}{T}\right)$
**Conversions:** None needed: the time is in seconds and the amplitude in centimetres. The calculator is set to radian mode.
**Substitution:** $x = 3.0\,\text{cm} \cdot \sin\left(\dfrac{2\pi \cdot 0.10\,\text{s}}{0.50\,\text{s}}\right) = 3.0\,\text{cm} \cdot \sin 1.257 = 3.0\,\text{cm} \cdot 0.951 = 2.85\,\text{cm}$
**Answer:** $2.9\,\text{cm}$ on the positive side of the equilibrium position, two significant figures as in the values $3.0\,\text{cm}$ and $0.50\,\text{s}$ read from the graph.
**Reasonableness:** The cart is at an extreme position at the time $\tfrac{T}{4} = 0.125\,\text{s}$, so at $0.10\,\text{s}$ it is just before the peak and the displacement must be a little less than the amplitude $3.0\,\text{cm}$, like $2.9\,\text{cm}$. Another route: $0.10\,\text{s}$ is $\tfrac{0.10}{0.50} = 0.20$ of the period, that is, $72^\circ$, and $3.0\,\text{cm} \cdot \sin 72^\circ = 2.85\,\text{cm}$.

## fy5-7-L2-02
**Given:** coefficient of the sine fit $B = 12.6\,\tfrac{1}{\text{s}}$
**Find:** the frequency $f$ of the oscillation in hertz
**Principle:** In the fit model $y = A \sin(Bt + C) + D$ the coefficient $B$ corresponds to the expression $\tfrac{2\pi}{T}$ of the sine model, because during one period the argument of the sine grows by $2\pi$. The frequency is obtained from the period as its reciprocal.
**Formula:** $B = \dfrac{2\pi}{T}$, from which $T = \dfrac{2\pi}{B}$, and $f = \dfrac{1}{T}$, so $f = \dfrac{B}{2\pi}$
**Conversions:** None needed: the coefficient $B$ is in the unit $\tfrac{1}{\text{s}}$, so the frequency comes out in the unit $\tfrac{1}{\text{s}} = \text{Hz}$.
**Substitution:** $f = \dfrac{12.6\,\tfrac{1}{\text{s}}}{2\pi} = \dfrac{12.6\,\tfrac{1}{\text{s}}}{6.283} = 2.005\,\text{Hz}$
**Answer:** $2.01\,\text{Hz}$, three significant figures as in the coefficient $12.6\,\tfrac{1}{\text{s}}$.
**Reasonableness:** An estimate: $2\pi \approx 6.3$, and $12.6$ is twice $6.3$, so the frequency must be about $2\,\text{Hz}$. The period is then about $0.50\,\text{s}$, which is usual for a weight oscillating on a spring.

## fy5-7-L2-03
**Given:** the needle moves up and down $900$ times a minute
**Find:** the period $T$ of the motion of the needle in milliseconds
**Principle:** One up-and-down motion is one full oscillation, so the number of motions per unit time is the frequency. The period is the reciprocal of the frequency. The frequency is first converted to oscillations per second.
**Formula:** $f = \dfrac{1}{T}$, from which $T = \dfrac{1}{f}$
**Conversions:** $f = 900\,\tfrac{1}{\text{min}} = \dfrac{900}{60\,\text{s}} = 15\,\text{Hz}$; finally $1\,\text{s} = 1000\,\text{ms}$.
**Substitution:** $T = \dfrac{1}{15\,\tfrac{1}{\text{s}}} = 0.06667\,\text{s} = 0.06667 \cdot 1000\,\text{ms} = 66.67\,\text{ms}$
**Answer:** $67\,\text{ms}$, two significant figures, because the rate $900$ times a minute is given as a round number.
**Reasonableness:** Another route: a minute has $60\,000\,\text{ms}$, and it is divided among $900$ motions, so one takes $\tfrac{60\,000\,\text{ms}}{900} \approx 67\,\text{ms}$. So the needle moves about $15$ times a second, which fits the fast whirr of a sewing machine.

## fy5-7-L2-04
**Given:** smallest distance from the sensor $d_\text{min} = 32.0\,\text{cm}$, greatest $d_\text{max} = 47.0\,\text{cm}$
**Find:** the amplitude $A$ of the oscillation in centimetres
**Principle:** The smallest and the greatest distance are the extreme positions of the weight. The distance between them is twice the amplitude, because the equilibrium position is halfway between the extreme positions and the amplitude is measured from the equilibrium position to an extreme position.
**Formula:** $d_\text{max} - d_\text{min} = 2A$, from which $A = \dfrac{d_\text{max} - d_\text{min}}{2}$
**Conversions:** None needed: both distances are in centimetres.
**Substitution:** $A = \dfrac{47.0\,\text{cm} - 32.0\,\text{cm}}{2} = \dfrac{15.0\,\text{cm}}{2} = 7.50\,\text{cm}$
**Answer:** $7.50\,\text{cm}$, three significant figures as in the difference of the distances $15.0\,\text{cm}$.
**Reasonableness:** The equilibrium position is at the distance $\tfrac{32.0\,\text{cm} + 47.0\,\text{cm}}{2} = 39.5\,\text{cm}$. From it to each extreme position is $7.50\,\text{cm}$: $39.5\,\text{cm} - 7.50\,\text{cm} = 32.0\,\text{cm}$ and $39.5\,\text{cm} + 7.50\,\text{cm} = 47.0\,\text{cm}$, as measured.

## fy5-7-L3-01
**Given:** period $T = 1.2\,\text{s}$, timing starts at a pass through the equilibrium position going up, the height asked about $x = \tfrac{A}{2}$
**Find:** the time $t$ after which the weight is for the first time at the height $\tfrac{A}{2}$
**Principle:** The oscillation is sinusoidal, and timing starts at a pass through the equilibrium position in the positive direction, so $x = A \sin\left(\tfrac{2\pi t}{T}\right)$. When $x = \tfrac{A}{2}$, the value of the sine is $\tfrac{1}{2}$. The first time corresponds to the smallest positive angle for which the sine is $\tfrac{1}{2}$. In a right triangle with an angle of $30^\circ$ the opposite leg is half of the hypotenuse, so $\sin 30^\circ = \tfrac{1}{2}$, and because $180^\circ = \pi$, the angle is $30^\circ = \tfrac{\pi}{6}$. The next angle, $150^\circ$, would fall only in the downward phase. The amplitude cancels, so it is not needed.
**Formula:** $\dfrac{A}{2} = A \sin\left(\dfrac{2\pi t}{T}\right)$, from which $\dfrac{2\pi t}{T} = \dfrac{\pi}{6}$, so $t = \dfrac{T}{12}$
**Conversions:** None needed: the period is in seconds, and the angle is in radians.
**Substitution:** $t = \dfrac{1.2\,\text{s}}{12} = 0.10\,\text{s}$
**Answer:** $0.10\,\text{s}$, two significant figures as in the period $1.2\,\text{s}$.
**Reasonableness:** The weight is at the highest position at $\tfrac{T}{4} = 0.30\,\text{s}$. Half of the height is reached already in a third of this time, because the weight moves fastest at the equilibrium position and slows down towards the highest position. Check: $1.2\,\text{s} \cdot \tfrac{1}{12} = 0.10\,\text{s}$ and $\sin\left(\tfrac{2\pi \cdot 0.10}{1.2}\right) = \sin 0.524 = 0.500$.

## fy5-7-L3-02
**Given:** distance of the button from the axis $r = 15\,\text{cm}$, rotation frequency $45\,\tfrac{1}{\text{min}}$, time from the pass through the middle $t = 0.20\,\text{s}$
**Find:** the distance $x$ of the shadow from the middle of its motion in centimetres
**Principle:** The button is in uniform circular motion, and the horizontal light casts on the wall its height above the level of the axis. The height of a point in circular motion oscillates sinusoidally: the amplitude is the radius of the circle and the frequency is the rotation frequency. The light comes from far away and is parallel, so the shadow is as large as the height of the button above the level of the axis. The time is counted from the pass through the middle going up, so the sine model is used.
**Formula:** $x = A \sin(2\pi f t)$, where $A = r$, that is, $x = r \sin(2\pi f t)$
**Conversions:** $f = 45\,\tfrac{1}{\text{min}} = \dfrac{45}{60\,\text{s}} = 0.75\,\text{Hz}$
**Substitution:** $x = 15\,\text{cm} \cdot \sin(2\pi \cdot 0.75\,\text{Hz} \cdot 0.20\,\text{s}) = 15\,\text{cm} \cdot \sin 0.9425 = 15\,\text{cm} \cdot 0.8090 = 12.14\,\text{cm}$
**Answer:** $12\,\text{cm}$ above the middle, two significant figures as in the distance $15\,\text{cm}$ and the rate $45\,\tfrac{1}{\text{min}}$.
**Reasonableness:** The period is $\tfrac{1}{0.75\,\text{Hz}} = 1.33\,\text{s}$, so the shadow is at its highest at $\tfrac{T}{4} = 0.33\,\text{s}$. At $0.20\,\text{s}$ it is still rising, so the displacement must be a little less than $15\,\text{cm}$, like $12\,\text{cm}$. The disc has turned $0.15$ of a revolution, that is, $54^\circ$, and $\sin 54^\circ = 0.81$.

## fy5-7-L3-03
**Given:** periods $T_1 = 0.60\,\text{s}$ and $T_2 = 0.90\,\text{s}$, both pass the equilibrium position going up at the time $0$
**Find:** the shortest time $t$ after which they again pass the equilibrium position going up at the same time
**Principle:** The first weight passes the equilibrium position going up at intervals of a full period, at the times $0.60\,\text{s}$, $1.20\,\text{s}$, $1.80\,\text{s}$, … and the second at the times $0.90\,\text{s}$, $1.80\,\text{s}$, … We look for the shortest time that is a whole multiple of both periods: integers $k$ and $m$ for which $k T_1 = m T_2$.
**Formula:** $k T_1 = m T_2$, from which $\dfrac{k}{m} = \dfrac{T_2}{T_1}$, and $t = k T_1$ with the smallest integer $k$
**Conversions:** None needed: both periods are in seconds.
**Substitution:** $\dfrac{k}{m} = \dfrac{0.90\,\text{s}}{0.60\,\text{s}} = 1.5 = \dfrac{3}{2}$, so $k = 3$ and $t = 3 \cdot 0.60\,\text{s} = 1.80\,\text{s}$
**Answer:** $1.8\,\text{s}$, two significant figures as in the periods $0.60\,\text{s}$ and $0.90\,\text{s}$.
**Reasonableness:** In the time $1.8\,\text{s}$ the first makes $\tfrac{1.8}{0.60} = 3$ and the second $\tfrac{1.8}{0.90} = 2$ full oscillations, so both are again in the starting state. It does not happen earlier: at $0.90\,\text{s}$ the first has made only one and a half oscillations and passes the equilibrium position going down.
