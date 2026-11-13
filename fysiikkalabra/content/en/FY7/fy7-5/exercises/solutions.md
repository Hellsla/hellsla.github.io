## fy7-5-L1-01
**Given:** side of the square $a = 0.12\,\text{m}$, magnetic flux density $B = 0.35\,\text{T}$, field perpendicular to the plane of the loop
**Find:** magnetic flux $\Phi$ through the loop in milliwebers
**Principle:** When a uniform field is perpendicular to the plane of the loop, the magnetic flux is the product of the field and the area. The loop is a square, so its area is the square of the side.
**Formula:** $\Phi = BA$ and $A = a^2$, so $\Phi = B a^2$
**Conversions:** The given values are in SI units. The answer is converted to milliwebers: $1\,\text{Wb} = 1000\,\text{mWb}$.
**Substitution:** $\Phi = 0.35\,\text{T} \cdot (0.12\,\text{m})^2 = 0.35\,\text{T} \cdot 0.0144\,\text{m}^2 = 0.00504\,\text{Wb} = 5.04\,\text{mWb}$
**Answer:** $5.0\,\text{mWb}$, two significant figures like the given values.
**Reasonableness:** The area of the loop is a little under $0.015\,\text{m}^2$, about the size of an A6 sheet (a postcard), and the field is of the order of tenths of a tesla, so the flux is of the order of thousandths of a weber. Doubling the side would quadruple the flux.

## fy7-5-L1-02
**Given:** number of turns $N = 400$, change in flux through one turn $\Delta\Phi = 1.5\,\text{mWb}$, time $\Delta t = 0.20\,\text{s}$
**Find:** magnitude of the induced voltage $|e|$ in the coil in volts
**Principle:** The magnetic flux through the coil changes when the magnet is pushed into it, so an induced voltage appears in the coil according to Faraday's law. The flux grows steadily, so the voltage is constant throughout. The turns are in series, so the voltage is $N$ times the voltage of one turn.
**Formula:** $|e| = N\dfrac{\Delta\Phi}{\Delta t}$
**Conversions:** $\Delta\Phi = 1.5\,\text{mWb} = 1.5 \cdot 10^{-3}\,\text{Wb}$
**Substitution:** $|e| = 400 \cdot \dfrac{1.5 \cdot 10^{-3}\,\text{Wb}}{0.20\,\text{s}} = 400 \cdot 7.5 \cdot 10^{-3}\,\text{V} = 3.0\,\text{V}$
**Answer:** $3.0\,\text{V}$, two significant figures like the change in flux and the time.
**Reasonableness:** The units fit: $\tfrac{\text{Wb}}{\text{s}} = \text{V}$. One turn would give only $7.5\,\text{mV}$; with a coil of hundreds of turns the voltage rises to volts, which matches experiments done with school coils.

## fy7-5-L1-03
**Given:** length of the rod $l = 0.25\,\text{m}$, speed $v = 2.0\,\text{m/s}$, magnetic flux density $B = 0.40\,\text{T}$; the rod, the velocity and the field are mutually perpendicular
**Find:** induced voltage $e$ between the ends of the rod in volts
**Principle:** The electrons that move with the rod experience a magnetic force $evB$ along the rod, so electrons collect at one end of the rod. The shift stops when the electric field $E = vB$ that appears cancels the magnetic force, and the voltage between the ends is $El$.
**Formula:** $e = vBl$
**Conversions:** None needed: all quantities are in SI units, and $\tfrac{\text{m}}{\text{s}} \cdot \text{T} \cdot \text{m} = \text{V}$.
**Substitution:** $e = 2.0\,\text{m/s} \cdot 0.40\,\text{T} \cdot 0.25\,\text{m} = 0.20\,\text{V}$
**Answer:** $0.20\,\text{V}$, two significant figures like the given values.
**Reasonableness:** Every second the rod sweeps an area of $0.25\,\text{m} \cdot 2.0\,\text{m} = 0.50\,\text{m}^2$, so the flux grows at the rate $0.40\,\text{T} \cdot 0.50\,\tfrac{\text{m}^2}{\text{s}} = 0.20\,\tfrac{\text{Wb}}{\text{s}}$: Faraday's law gives the same voltage.

## fy7-5-L1-04
**Given:** number of turns $N = 150$, average induced voltage $|e| = 0.45\,\text{V}$, time $\Delta t = 0.12\,\text{s}$
**Find:** change in the magnetic flux through one turn $\Delta\Phi$ in milliwebers
**Principle:** The voltage appears because the flux decreases as the magnet is pulled away. According to Faraday's law, the average voltage is the change in flux divided by the time, multiplied by the number of turns, so when the voltage, the time and the number of turns are known, the change in flux can be solved.
**Formula:** $|e| = N\dfrac{\Delta\Phi}{\Delta t}$, so $\Delta\Phi = \dfrac{|e|\,\Delta t}{N}$
**Conversions:** The given values are in SI units, and $\text{V}\cdot\text{s} = \text{Wb}$. The answer is converted to milliwebers: $1\,\text{Wb} = 1000\,\text{mWb}$.
**Substitution:** $\Delta\Phi = \dfrac{0.45\,\text{V} \cdot 0.12\,\text{s}}{150} = \dfrac{0.054\,\text{V}\cdot\text{s}}{150} = 3.6 \cdot 10^{-4}\,\text{Wb} = 0.36\,\text{mWb}$
**Answer:** $0.36\,\text{mWb}$, two significant figures like the voltage and the time.
**Reasonableness:** Check: $150 \cdot 3.6 \cdot 10^{-4}\,\text{Wb} : 0.12\,\text{s} = 0.45\,\text{V}$. If the area of the coil is about $10\,\text{cm}^2$, the flux corresponds to a field of about $0.4\,\text{T}$ inside the coil, which suits a strong permanent magnet.

## fy7-5-L1-05
**Given:** induced voltage $e = 12\,\text{mV}$, length of the rod in the field $l = 0.30\,\text{m}$, magnetic flux density $B = 0.080\,\text{T}$, velocity perpendicular to the rod and the field
**Find:** speed of the rod $v$ in metres per second
**Principle:** The magnetic force on the electrons of the moving rod moves them to one end of the rod, and a voltage $e = vBl$ appears between the ends. The voltage is proportional to the speed, so the speed can be solved from the measured voltage.
**Formula:** $e = vBl$, so $v = \dfrac{e}{Bl}$
**Conversions:** $e = 12\,\text{mV} = 12 \cdot 0.001\,\text{V} = 0.012\,\text{V}$
**Substitution:** $v = \dfrac{0.012\,\text{V}}{0.080\,\text{T} \cdot 0.30\,\text{m}} = \dfrac{0.012\,\text{V}}{0.024\,\text{T}\cdot\text{m}} = 0.50\,\text{m/s}$
**Answer:** $0.50\,\text{m/s}$, two significant figures like the given values.
**Reasonableness:** Check: $0.50\,\text{m/s} \cdot 0.080\,\text{T} \cdot 0.30\,\text{m} = 0.012\,\text{V}$. Half a metre per second is slower than a slow walk, which suits a rail experiment done on a table.

## fy7-5-L2-01
**Given:** magnetic flux density $B = 0.80\,\text{T}$ perpendicular to the plane of the loop, area at first $A_1 = 200\,\text{cm}^2$ and at the end $A_2 = 50\,\text{cm}^2$, time $\Delta t = 0.25\,\text{s}$, one turn $N = 1$
**Find:** magnitude of the induced voltage $|e|$ in the loop in millivolts
**Principle:** The field stays the same, but the area of the loop decreases, so the flux $\Phi = BA$ through the loop decreases. The change in flux produces a voltage according to Faraday's law. The area decreases steadily, so the voltage is constant.
**Formula:** $\Delta\Phi = B(A_1 - A_2)$ and $|e| = N\dfrac{\Delta\Phi}{\Delta t}$, so $|e| = \dfrac{B(A_1 - A_2)}{\Delta t}$ when $N = 1$
**Conversions:** $A_1 = 200\,\text{cm}^2 = 200 \cdot (0.01\,\text{m})^2 = 0.0200\,\text{m}^2$ and $A_2 = 50\,\text{cm}^2 = 50 \cdot (0.01\,\text{m})^2 = 0.0050\,\text{m}^2$
**Substitution:** $A_1 - A_2 = 0.0200\,\text{m}^2 - 0.0050\,\text{m}^2 = 0.0150\,\text{m}^2$ and $|e| = \dfrac{0.80\,\text{T} \cdot 0.0150\,\text{m}^2}{0.25\,\text{s}} = \dfrac{0.012\,\text{Wb}}{0.25\,\text{s}} = 0.048\,\text{V} = 48\,\text{mV}$
**Answer:** $48\,\text{mV}$, two significant figures like the field $0.80\,\text{T}$ and the time $0.25\,\text{s}$.
**Reasonableness:** One turn gives a voltage of only tens of millivolts even though the field is strong; this fits the fact that practical devices need many turns. If the loop were squeezed twice as fast, the voltage would be twice as great.

## fy7-5-L2-02
**Given:** number of turns $N = 50$; the graph shows the magnetic flux $\Phi$ through one turn as a function of time $t$
**Find:** greatest absolute value of the induced voltage $|e|$ in volts
**Principle:** According to Faraday's law, the voltage is proportional to the rate of change of the flux $\Delta\Phi : \Delta t$, which is the slope of the flux graph. The voltage is therefore greatest where the graph is steepest, not where the flux is greatest.
**Reading the graph:** The graph consists of straight parts. In the interval $0$–$0.20\,\text{s}$ the flux grows from zero to $4.0\,\text{mWb}$, so the absolute value of the slope is $4.0\,\text{mWb} : 0.20\,\text{s} = 20\,\tfrac{\text{mWb}}{\text{s}}$. In the interval $0.20$–$0.50\,\text{s}$ the graph is horizontal, so the voltage is zero. In the interval $0.50$–$0.60\,\text{s}$ the flux decreases from $4.0\,\text{mWb}$ to zero, so the absolute value of the slope is $4.0\,\text{mWb} : 0.10\,\text{s} = 40\,\tfrac{\text{mWb}}{\text{s}}$. The steepest part is therefore $0.50$–$0.60\,\text{s}$, where $\Delta\Phi = 4.0\,\text{mWb}$ and $\Delta t = 0.10\,\text{s}$.
**Formula:** $|e| = N\dfrac{\Delta\Phi}{\Delta t}$
**Conversions:** $\Delta\Phi = 4.0\,\text{mWb} = 4.0 \cdot 10^{-3}\,\text{Wb}$
**Substitution:** $|e| = 50 \cdot \dfrac{4.0 \cdot 10^{-3}\,\text{Wb}}{0.10\,\text{s}} = 50 \cdot 0.040\,\text{V} = 2.0\,\text{V}$
**Answer:** $2.0\,\text{V}$, two significant figures like the flux $4.0\,\text{mWb}$ read from the graph.
**Reasonableness:** In the rising part the voltage is $50 \cdot 4.0 \cdot 10^{-3}\,\text{Wb} : 0.20\,\text{s} = 1.0\,\text{V}$, half of the greatest, because the same change in flux takes twice as long. In the falling part the sign of the voltage is opposite to that in the rising part, because the flux decreases.

## fy7-5-L2-03
**Given:** distance between the rails, that is, the length of the rod in the field, $l = 0.40\,\text{m}$, speed $v = 3.0\,\text{m/s}$, magnetic flux density $B = 0.50\,\text{T}$, resistance $R = 2.0\,\Omega$; the resistance of the rails and the rod is very small
**Find:** current $I$ through the resistor in amperes
**Principle:** An induced voltage $e = vBl$ appears between the ends of the moving rod, because a magnetic force acts on the electrons of the rod. The rod, the rails and the resistor form a closed circuit in which the rod acts as the voltage source. The resistance of the rest of the circuit is small, so the whole voltage is across the resistor, and the current follows from Ohm's law.
**Formula:** $e = vBl$ and $I = \dfrac{e}{R}$, so $I = \dfrac{vBl}{R}$
**Conversions:** None needed: all quantities are in SI units.
**Substitution:** $e = 3.0\,\text{m/s} \cdot 0.50\,\text{T} \cdot 0.40\,\text{m} = 0.60\,\text{V}$ and $I = \dfrac{0.60\,\text{V}}{2.0\,\Omega} = 0.30\,\text{A}$
**Answer:** $0.30\,\text{A}$, two significant figures like the given values.
**Reasonableness:** The flux grows at the rate $0.50\,\text{T} \cdot 0.40\,\text{m} \cdot 3.0\,\tfrac{\text{m}}{\text{s}} = 0.60\,\tfrac{\text{Wb}}{\text{s}}$, which gives the same voltage. When a current flows in the rod, the field exerts a force $IlB = 0.060\,\text{N}$ on it; its direction is found in the chapter *Lenz's law and eddy currents*.

## fy7-5-L2-04
**Given:** side of the coil $l = 5.0\,\text{cm}$, number of turns $N = 20$, speed $v = 0.25\,\text{m/s}$, magnetic flux density $B = 0.30\,\text{T}$ perpendicular to the plane of the coil
**Find:** induced voltage $|e|$ in millivolts while the coil is entering the field
**Principle:** When the coil enters the field, the part of its area that is in the field grows steadily, so the flux through each turn grows steadily and the voltage is constant. In the time $\Delta t$ the coil moves a distance $v\Delta t$, so the flux grows by $\Delta\Phi = Bl \cdot v\Delta t$.
**Formula:** $|e| = N\dfrac{\Delta\Phi}{\Delta t} = N\dfrac{Bl \cdot v\Delta t}{\Delta t}$, so $|e| = NBlv$
**Conversions:** $l = 5.0\,\text{cm} = 5.0 \cdot 0.01\,\text{m} = 0.050\,\text{m}$
**Substitution:** $|e| = 20 \cdot 0.30\,\text{T} \cdot 0.050\,\text{m} \cdot 0.25\,\text{m/s} = 0.075\,\text{V} = 75\,\text{mV}$
**Answer:** $75\,\text{mV}$, two significant figures like the given values.
**Reasonableness:** Check using the whole entry: the flux grows from zero to $BA = 0.30\,\text{T} \cdot (0.050\,\text{m})^2 = 7.5 \cdot 10^{-4}\,\text{Wb}$ in the time $0.050\,\text{m} : 0.25\,\text{m/s} = 0.20\,\text{s}$, so $|e| = 20 \cdot 7.5 \cdot 10^{-4}\,\text{Wb} : 0.20\,\text{s} = 0.075\,\text{V}$.

## fy7-5-L3-01
**Given:** speed of the train $v = 200\,\text{km/h}$, length of the axle from rail to rail $l = 1524\,\text{mm}$, vertical component of the Earth's magnetic field $B_\text{v} = 50\,\mu\text{T}$
**Find:** induced voltage $e$ between the ends of the axle in millivolts
**Principle:** The axle is a metal rod that moves horizontally, perpendicular to itself. The magnetic force on the electrons is perpendicular to the velocity and the field; a component along the axle arises only from the vertical component of the field, because the horizontal component is either parallel to the velocity or gives a vertical force. The voltage is therefore given by $e = vB_\text{v}l$.
**Formula:** $e = vB_\text{v}l$
**Conversions:** $v = 200\,\text{km/h} = 200 \cdot \dfrac{1000\,\text{m}}{3600\,\text{s}} = 55.56\,\text{m/s}$, $l = 1524\,\text{mm} = 1524 \cdot 0.001\,\text{m} = 1.524\,\text{m}$ and $B_\text{v} = 50\,\mu\text{T} = 50 \cdot 10^{-6}\,\text{T}$
**Substitution:** $e = 55.56\,\text{m/s} \cdot 50 \cdot 10^{-6}\,\text{T} \cdot 1.524\,\text{m} = 4.233 \cdot 10^{-3}\,\text{V} = 4.2\,\text{mV}$
**Answer:** $4.2\,\text{mV}$, two significant figures like the field $50\,\mu\text{T}$.
**Reasonableness:** The Earth's field is about one ten-thousandth of the field of a laboratory magnet, so despite the high speed the voltage stays in the millivolt range. At a cyclist's speed of $20\,\text{km/h}$ the voltage would be a tenth of this, about $0.4\,\text{mV}$.

## fy7-5-L3-02
**Given:** number of turns $N = 100$, area $A = 0.020\,\text{m}^2$, plane of the coil at first perpendicular to the field, half-turn in the time $\Delta t = 0.10\,\text{s}$, average voltage $|e| = 2.0\,\text{mV}$
**Find:** magnetic flux density $B$ of the Earth's magnetic field in microteslas
**Principle:** At first the flux through one turn is $\Phi_1 = BA$. After a half-turn the same field passes through the turn from the opposite direction, so the flux is $\Phi_2 = -BA$. The magnitude of the change in flux is therefore $\Delta\Phi = 2BA$, and according to Faraday's law the average voltage is $N \cdot 2BA : \Delta t$.
**Formula:** $|e| = N\dfrac{2BA}{\Delta t}$, so $B = \dfrac{|e|\,\Delta t}{2NA}$
**Conversions:** $|e| = 2.0\,\text{mV} = 2.0 \cdot 10^{-3}\,\text{V}$; the answer is converted to microteslas: $1\,\text{T} = 10^{6}\,\mu\text{T}$
**Substitution:** $B = \dfrac{2.0 \cdot 10^{-3}\,\text{V} \cdot 0.10\,\text{s}}{2 \cdot 100 \cdot 0.020\,\text{m}^2} = \dfrac{2.0 \cdot 10^{-4}\,\text{V}\cdot\text{s}}{4.0\,\text{m}^2} = 5.0 \cdot 10^{-5}\,\text{T} = 50\,\mu\text{T}$
**Answer:** $50\,\mu\text{T}$, two significant figures like the voltage $2.0\,\text{mV}$.
**Reasonableness:** The Earth's magnetic field in Finland is about $50\,\mu\text{T}$, so the result is believable. If the change in flux had wrongly been taken as $BA$, the result would be twice as great, $100\,\mu\text{T}$, which is too large.

## fy7-5-L3-03
**Given:** number of turns $N = 300$, triangular voltage pulse, peak value $e_0 = 0.90\,\text{V}$, duration $\Delta t = 40\,\text{ms}$; at first the magnet is far away, so the flux is zero
**Find:** average magnetic flux $\Phi$ through one turn in milliwebers when the magnet is in the middle of the coil
**Principle:** Faraday's law implies that the product of the voltage and the duration of a short interval is $N$ times the change in flux. When the intervals of the pulse are added up, the area between the voltage graph $(t, e)$ and the time axis is $N\Delta\Phi$. At the end of the pulse the voltage is zero, because the flux is at its greatest and no longer growing; the magnet is then in the middle of the coil. The flux has grown from zero to this value, so $\Delta\Phi = \Phi$.
**Formula:** the area of the triangle is $N\Phi = \tfrac{1}{2} e_0 \Delta t$, so $\Phi = \dfrac{e_0 \Delta t}{2 \cdot N}$
**Conversions:** $\Delta t = 40\,\text{ms} = 40 \cdot 0.001\,\text{s} = 0.040\,\text{s}$; the answer is converted to milliwebers: $1\,\text{Wb} = 1000\,\text{mWb}$
**Substitution:** $\Phi = \dfrac{0.90\,\text{V} \cdot 0.040\,\text{s}}{2 \cdot 300} = \dfrac{0.036\,\text{V}\cdot\text{s}}{600} = 6.0 \cdot 10^{-5}\,\text{Wb} = 0.060\,\text{mWb}$
**Answer:** $0.060\,\text{mWb}$, two significant figures like the peak value $0.90\,\text{V}$ and the duration $40\,\text{ms}$.
**Reasonableness:** If the cross-sectional area of the coil is about $2\,\text{cm}^2 = 2 \cdot 10^{-4}\,\text{m}^2$, the average field through a turn is $6.0 \cdot 10^{-5}\,\text{Wb} : 2 \cdot 10^{-4}\,\text{m}^2 = 0.3\,\text{T}$, which suits a small strong magnet. When the magnet leaves the coil, a pulse of opposite sign appears, with an equal area.

## fy7-5-L1-06
**Find:** why no induced voltage appears between a magnet at rest and a coil even though the flux is large
**Principle:** According to the law of induction, the voltage appearing in the coil is $e = -N\dfrac{\Delta\Phi}{\Delta t}$, that is, it depends on the rate of change of the flux and not on the size of the flux. When the magnet is at rest relative to the coil, the flux stays constant, so $\Delta\Phi = 0$.
**Model answer:** The flux through the coil is large, but it does not change, because the magnet and the coil are at rest relative to each other. A voltage appears only when the flux changes, so the voltmeter reads zero. When the magnet is moved, the flux changes and the meter shows a voltage, the greater the faster the flux changes. The field does not prevent a voltage from appearing, and a current is not a precondition for the voltage: the current is a consequence of the voltage in a closed circuit.

## fy7-5-L1-07
**Given:** number of turns of the first coil $N_1 = 120$ and voltage $e_1 = 0.90\,\text{V}$; number of turns of the second coil $N_2 = 300$; the coils are otherwise similar and the magnet moves in the same way
**Find:** induced voltage $e_2$ of the second coil in volts
**Principle:** The coils have the same area and the magnet moves in the same way, so the rate of change of the flux through one turn, $\Delta\Phi : \Delta t$, is the same in both. The turns are in series, so the voltage is directly proportional to the number of turns.
**Formula:** $e_1 = N_1\dfrac{\Delta\Phi}{\Delta t}$ and $e_2 = N_2\dfrac{\Delta\Phi}{\Delta t}$, so $e_2 = \dfrac{N_2}{N_1}\,e_1$
**Conversions:** Not needed: the numbers of turns are plain numbers, and the voltage is in volts.
**Substitution:** $e_2 = \dfrac{300}{120} \cdot 0.90\,\text{V} = 2.5 \cdot 0.90\,\text{V} = 2.25\,\text{V} \approx 2.3\,\text{V}$
**Answer:** $2.3\,\text{V}$, two significant figures like the voltage $0.90\,\text{V}$.
**Reasonableness:** There are more than twice as many turns, so the voltage is more than double: $2 \cdot 0.90\,\text{V} = 1.8\,\text{V}$ is smaller and $3 \cdot 0.90\,\text{V} = 2.7\,\text{V}$ greater than the answer. The voltage of one turn is the same in both, $0.90\,\text{V} : 120 = 7.5\,\text{mV}$.

## fy7-5-L1-08
**Given:** length of the rod $l = 0.50\,\text{m}$, speed $v = 0.60\,\text{m/s}$, induced voltage $e = 18\,\text{mV}$; the rod, the velocity and the field are mutually perpendicular
**Find:** magnetic flux density $B$ in teslas
**Principle:** A magnetic force acts on the electrons of the moving rod, and a voltage $e = vBl$ appears between the ends of the rod. The voltage is directly proportional to the magnetic flux density, so $B$ can be solved from the measured voltage.
**Formula:** $e = vBl$, so $B = \dfrac{e}{vl}$
**Conversions:** $e = 18\,\text{mV} = 18 \cdot 0.001\,\text{V} = 0.018\,\text{V}$
**Substitution:** $B = \dfrac{0.018\,\text{V}}{0.60\,\text{m/s} \cdot 0.50\,\text{m}} = \dfrac{0.018\,\text{V}}{0.30\,\text{m}^2/\text{s}} = 0.060\,\text{T}$
**Answer:** $0.060\,\text{T}$, two significant figures like the given values.
**Reasonableness:** Check: $0.60\,\text{m/s} \cdot 0.060\,\text{T} \cdot 0.50\,\text{m} = 0.018\,\text{V}$. The field is more than a thousand times stronger than the Earth's magnetic field but clearly weaker than the field of a strong electromagnet, which suits the vicinity of a permanent magnet.

## fy7-5-L2-05
**Given:** number of turns $N = 120$; from the table the flux $\Phi$ through one turn as a function of time $t$, interval $0.10\,\text{s}$ (sample data)
**Find:** greatest absolute value of the induced voltage $|e|$ in volts
**Principle:** According to the law of induction, the voltage is proportional to the rate of change of the flux $\Delta\Phi : \Delta t$, so the voltage is greatest where the flux changes fastest. The flux changes roughly steadily during each interval, so the voltage is roughly constant in each interval.
**Reading the graph:** From the flux values of the table the change in flux $\Delta\Phi$ is calculated for each $0.10\,\text{s}$ interval. In the rising phase ($0$–$0.30\,\text{s}$) the changes are $0.98$, $1.05$ and $0.97\,\text{mWb}$, the greatest being $1.05\,\text{mWb}$ in the interval $0.10$–$0.20\,\text{s}$. In the interval $0.30$–$0.40\,\text{s}$ the flux hardly changes ($0.01\,\text{mWb}$). In the falling phase the changes are $\Delta\Phi = 1.21\,\text{mWb}$ in the interval $0.40$–$0.50\,\text{s}$ and $1.20\,\text{mWb}$ in the interval $0.50$–$0.60\,\text{s}$. The steepest single interval is therefore $0.40$–$0.50\,\text{s}$, in which $\Delta\Phi = 1.21\,\text{mWb}$ and $\Delta t = 0.10\,\text{s}$.
**Formula:** $|e| = N\dfrac{\Delta\Phi}{\Delta t}$
**Conversions:** $\Delta\Phi = 1.21\,\text{mWb} = 1.21 \cdot 10^{-3}\,\text{Wb}$
**Substitution:** $|e| = 120 \cdot \dfrac{1.21 \cdot 10^{-3}\,\text{Wb}}{0.10\,\text{s}} = 120 \cdot 0.0121\,\text{V} = 1.452\,\text{V} \approx 1.45\,\text{V}$
**Answer:** $1.45\,\text{V}$, three significant figures like the flux values of the table. The average over the whole falling phase $0.40$–$0.60\,\text{s}$ gives roughly the same result, $1.45\,\text{V}$.
**Reasonableness:** In the rising phase the flux changes by about $0.010\,\tfrac{\text{Wb}}{\text{s}}$, so the voltage is $120 \cdot 0.010\,\text{V} = 1.2\,\text{V}$, smaller than in the falling phase. The greatest voltage is where the flux changes fastest, not where the flux is greatest.

## fy7-5-L2-06
**Given:** length of the rod in the field $l = 0.20\,\text{m}$; from the table the voltage $e$ as a function of speed $v$ (sample data), the rod and the velocity perpendicular to the field
**Find:** magnetic flux density $B$ in teslas
**Principle:** The voltage of the moving rod is $e = vBl$. When $B$ and $l$ stay the same, $e$ is directly proportional to the speed $v$, so the $(v, e)$ points lie on a straight line through the origin whose slope is $Bl$. The points deviate slightly from the line because of measurement errors.
**Reading the graph:** The fitted line passes from the origin between the points (for example through the point $(0.60\,\text{m/s};\ 18\,\text{mV})$ and the origin). The slope of the line is $k = \Delta e : \Delta v = 18\,\text{mV} : 0.60\,\text{m/s} = 30\,\tfrac{\text{mV}}{\text{m/s}}$. The quotients $e : v$ of all the points are between $29$ and $31\,\tfrac{\text{mV}}{\text{m/s}}$, so the line describes the data well.
**Formula:** $k = Bl$, so $B = \dfrac{k}{l}$
**Conversions:** $k = 30\,\tfrac{\text{mV}}{\text{m/s}} = 30 \cdot 0.001\,\tfrac{\text{V}}{\text{m/s}} = 0.030\,\tfrac{\text{V}}{\text{m/s}}$
**Substitution:** $B = \dfrac{0.030\,\text{V}\cdot\text{s/m}}{0.20\,\text{m}} = 0.15\,\text{T}$
**Answer:** $0.15\,\text{T}$, two significant figures like the length $0.20\,\text{m}$ and the slope.
**Reasonableness:** Check: $0.40\,\text{m/s} \cdot 0.15\,\text{T} \cdot 0.20\,\text{m} = 12\,\text{mV}$, which matches the value $11.9\,\text{mV}$ of the table. A calculation based on a single point would be less certain than fitting a line, because the error of a single point would affect the result directly.

## fy7-5-L2-07
**Find:** what is wrong in the student's calculation
**Principle:** The formula $e = vBl$ is derived for a situation in which the velocity, the rod and the field are mutually perpendicular: the magnetic force shifts the electrons moving with the rod along the rod, and a voltage appears between the ends. In the student's problem the rod moves in the direction of the field, so this condition is not met.
**Model answer:** When the rod moves in the direction of the field, the velocity of the electrons is parallel to the field, so the magnetic force is zero. The electrons do not shift to the end of the rod, no charge collects at the ends, and no voltage appears between the ends of the rod. The student's result $0.30\,\text{V}$ is wrong; the correct voltage is zero. The same result follows from the flux: the rod does not sweep any new area through the field lines, so the flux does not change. The formula $e = vBl$ may be used only when the three directions are perpendicular to each other.

## fy7-5-L3-04
**Given:** length of the rod $l = 0.40\,\text{m}$, magnetic flux density $B = 0.25\,\text{T}$, start from rest, steady acceleration; from the table $e(t)$ at six measurement points (sample data), among others $e = 198\,\text{mV}$ at the moment $t = 1.2\,\text{s}$
**Find:** a) acceleration $a$ of the cart ($\text{m/s}^2$) and the justification for the growth of the voltage; b) distance $s$ travelled by the cart in $1.2\,\text{s}$
**Principle:** The rod, the velocity and the field are perpendicular, so the voltage between the ends of the rod is $e = vBl$. The cart accelerates steadily from rest, so $v = at$. It follows that $e = aBl \cdot t$: the voltage is directly proportional to time, and the slope of the line through the $(t, e)$ points is $k = aBl$.
**Reading the graph:** The quotients $e : t$ are $0.160$, $0.163$, $0.163$, $0.166$, $0.163$ and $0.165\,\tfrac{\text{V}}{\text{s}}$, so the voltage really grows in direct proportion to time. The slope of the line fitted through the origin is $k = 0.164\,\tfrac{\text{V}}{\text{s}}$ (least-squares fit), and it suits all the quotients $0.160$–$0.166\,\tfrac{\text{V}}{\text{s}}$.
**Formula:** a) $k = aBl$, so $a = \dfrac{k}{Bl}$. b) The distance in uniformly accelerated motion from rest is $s = \tfrac{1}{2}at^2$.
**Conversions:** $1\,\text{mV} = 0.001\,\text{V}$, so $k$ is in SI units.
**Substitution:** a) $a = \dfrac{0.164\,\text{V/s}}{0.25\,\text{T} \cdot 0.40\,\text{m}} = \dfrac{0.164\,\text{V/s}}{0.100\,\text{T}\cdot\text{m}} = 1.64\,\text{m/s}^2$. b) $s = \tfrac{1}{2} \cdot 1.64\,\text{m/s}^2 \cdot (1.2\,\text{s})^2 = 1.18\,\text{m}$
**Answer:** a) $a = 1.6\,\text{m/s}^2$, two significant figures like the field and the length. b) $s \approx 1.2\,\text{m}$.
**Reasonableness:** At the moment $1.2\,\text{s}$ the speed of the cart is $v = 1.64\,\text{m/s}^2 \cdot 1.2\,\text{s} = 1.97\,\text{m/s}$. Then $e = 1.97\,\text{m/s} \cdot 0.25\,\text{T} \cdot 0.40\,\text{m} = 0.197\,\text{V}$, which matches the measured $198\,\text{mV}$.

## fy7-5-L3-05
**Given:** number of turns $N = 250$; from the table $e(t)$ at the moments $0$–$48\,\text{ms}$ at intervals of $4\,\text{ms}$ (sample data); before the drop and after it the flux is zero; the voltage is zero at about the moment $24\,\text{ms}$, when the magnet is in the middle of the coil
**Find:** a) the greatest magnetic flux $\Phi$ through one turn in milliwebers; b) the same from the second pulse and an explanation of the differences between the pulses
**Principle:** It follows from the law of induction that the product $e\,\Delta t$ over a short interval is $-N\Delta\Phi$. When these products are added up over the whole pulse, the sum is the area between the voltage graph $(t, e)$ and the time axis, and it is $N$ times the total change in flux. During the first pulse the flux grows from zero to its greatest value, and at the end of the pulse the voltage is zero, because the flux no longer changes.
**Reading the graph:** The area is estimated with the trapezoid rule: the area of each $4\,\text{ms}$ interval is the average of the voltages at the ends of the interval times $0.004\,\text{s}$. The voltages of the first pulse are $-0.02$, $0.09$, $0.63$, $1.77$, $1.77$, $0.60$ and $0.03\,\text{V}$. The sum gives the absolute value of the area $|A_\text{a}| = 0.004\,\text{s} \cdot (\tfrac{1}{2}(-0.02) + 0.09 + 0.63 + 1.77 + 1.77 + 0.60 + \tfrac{1}{2}\cdot 0.03)\,\text{V} = 0.004\,\text{s} \cdot 4.865\,\text{V} = 0.01946\,\text{V}\cdot\text{s}$.
**Formula:** $|A_\text{a}| = N\Phi$, so $\Phi = \dfrac{|A_\text{a}|}{N}$
**Conversions:** $1\,\text{ms} = 0.001\,\text{s}$; the answer is converted to milliwebers: $1\,\text{Wb} = 1000\,\text{mWb}$; $\text{V}\cdot\text{s} = \text{Wb}$.
**Substitution:** a) $\Phi = \dfrac{0.01946\,\text{V}\cdot\text{s}}{250} = 7.78 \cdot 10^{-5}\,\text{Wb} = 0.0778\,\text{mWb}$. b) Calculated in the same way, the area of the second pulse ($24$–$48\,\text{ms}$) is $-0.01968\,\text{V}\cdot\text{s}$, so $\Phi = 0.01968\,\text{V}\cdot\text{s} : 250 = 0.0787\,\text{mWb}$.
**Answer:** a) $\Phi \approx 0.078\,\text{mWb}$, two significant figures, because the voltages are given to two decimal places and the area is an estimate. b) The second pulse gives $0.079\,\text{mWb}$, the same flux. In the first pulse the flux grows and in the second it decreases back to zero, so the signs of the voltages are opposite, and the total change in flux is equally large in both pulses, so the areas are equal in absolute value. The magnet accelerates as it falls, so the same change in flux takes place in a shorter time in the second pulse: the pulse is narrower and taller.
**Reasonableness:** The areas of the pulses differ by about $1\,\%$, so the data are internally consistent. The triangle approximation $\tfrac{1}{2} \cdot 1.8\,\text{V} \cdot 0.020\,\text{s} = 0.018\,\text{V}\cdot\text{s}$ gives the same order of magnitude.

## fy7-5-L1-09
**Find:** the order of five situations by the magnitude $|e|$ of the induced voltage, from smallest to largest.
**Principle:** The voltage induced in a coil depends on the rate of change of the flux of one turn and on the number of turns, $|e| = N\dfrac{\Delta\Phi}{\Delta t}$, not on the size of the flux. In a single loop $N = 1$. The voltage of a rod moving perpendicular to the field is $e = vBl$.
**Model answer:** We calculate the voltage in each situation.

Situation A:

$|e_\text{A}| = 200 \cdot \dfrac{3.0 \cdot 10^{-3}\,\text{Wb}}{0.50\,\text{s}}$

$|e_\text{A}| = 1.2\,\text{V}$

Situation B:

$|e_\text{B}| = 50 \cdot \dfrac{6.0 \cdot 10^{-3}\,\text{Wb}}{0.10\,\text{s}}$

$|e_\text{B}| = 3.0\,\text{V}$

In situation C the current of the electromagnet is constant, so the flux does not change: $\Delta\Phi = 0$ and $e_\text{C} = 0$. The large flux $8.0\,\text{mWb}$ and the large number of turns do not change this.

Situation D:

$e_\text{D} = 4.0\,\text{m/s} \cdot 0.30\,\text{T} \cdot 0.50\,\text{m}$

$e_\text{D} = 0.60\,\text{V}$

Situation E, where $N = 1$:

$|e_\text{E}| = \dfrac{40 \cdot 10^{-3}\,\text{Wb}}{0.020\,\text{s}}$

$|e_\text{E}| = 2.0\,\text{V}$

By the magnitude of the induced voltage, from smallest to largest, the order is C ($0\,\text{V}$), D ($0.60\,\text{V}$), A ($1.2\,\text{V}$), E ($2.0\,\text{V}$) and B ($3.0\,\text{V}$). In situation E the flux decreases, so the sign of the voltage is opposite to that when the flux grows, but the order compares only the magnitudes.

If the number of turns is forgotten, the voltages of situations A and B come out as only $6.0\,\text{mV}$ and $60\,\text{mV}$, and they move to the wrong place right after situation C. If the voltage is thought to depend on the size of the flux and not on its change, the large flux of situation C seems to give the greatest voltage, and C wrongly moves to the end of the order.

**Reasonableness:** In situation E the flux changes fastest, $2.0\,\tfrac{\text{Wb}}{\text{s}}$, but the $50$ turns of situation B raise its voltage to the greatest.

## fy7-5-L2-08
**Given:** number of turns $N = 200$. The graph shows the flux through one turn, $\Phi$, as a function of time $t$. The interval is $0$–$0{,}40\,\text{s}$.
**Asked:** the magnitude of the average induced voltage $|e_\text{ka}|$ in volts
**Principle:** By the law of induction the voltage is set by the change of flux $\Delta\Phi$, not by the value of the flux. The change is the final value minus the initial value, also when the flux passes through zero and changes sign. The graph is a straight line in this interval, so the average voltage is the voltage of the whole interval.
**Reading the graph:** At time $0$ the flux is $\Phi_1 = 5{,}0\,\text{mWb}$. At $0{,}40\,\text{s}$ the flux is $\Phi_2 = -3{,}0\,\text{mWb}$. The change of flux is $\Delta\Phi = \Phi_2 - \Phi_1 = -3{,}0\,\text{mWb} - 5{,}0\,\text{mWb} = -8{,}0\,\text{mWb}$, and its magnitude is $8{,}0\,\text{mWb}$. The time is $\Delta t = 0{,}40\,\text{s} - 0 = 0{,}40\,\text{s}$.
**Formula:** $|e_\text{ka}| = N\dfrac{|\Delta\Phi|}{\Delta t}$
**Conversions:** $|\Delta\Phi| = 8{,}0\,\text{mWb} = 8{,}0 \cdot 10^{-3}\,\text{Wb}$
**Substitution:** $|e_\text{ka}| = 200 \cdot \dfrac{8{,}0 \cdot 10^{-3}\,\text{Wb}}{0{,}40\,\text{s}} = 200 \cdot 0{,}020\,\text{V} = 4{,}0\,\text{V}$
**Answer:** $4{,}0\,\text{V}$, two significant figures like the fluxes $5{,}0\,\text{mWb}$ and $-3{,}0\,\text{mWb}$ read from the graph.
**Reasonableness:** Using only the final value $3{,}0\,\text{mWb}$ would give $200 \cdot 3{,}0 \cdot 10^{-3}\,\text{Wb} : 0{,}40\,\text{s} = 1{,}5\,\text{V}$, which is too small: the flux changes through zero, so the change is larger than either value alone. The slope of the graph, $-8{,}0\,\text{mWb} : 0{,}40\,\text{s} = -20\,\tfrac{\text{mWb}}{\text{s}}$, gives the same result: $200 \cdot 0{,}020\,\text{V} = 4{,}0\,\text{V}$.
