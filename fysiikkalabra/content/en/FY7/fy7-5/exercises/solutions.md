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
