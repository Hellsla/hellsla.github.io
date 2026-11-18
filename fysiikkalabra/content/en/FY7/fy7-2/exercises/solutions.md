## fy7-2-L1-01
**Given:** proton, $q = 1.602 \cdot 10^{-19}\,\text{C}$, $v = 3.0 \cdot 10^{5}\,\text{m/s}$, $B = 0.25\,\text{T}$, velocity perpendicular to the field
**Find:** the magnetic force $F_\text{m}$ on the proton in the form $\ldots \cdot 10^{-14}\,\text{N}$
**Principle:** A charged particle moving in a magnetic field is acted on by a magnetic force. When the velocity is perpendicular to the field, $\sin 90^\circ = 1$ and the force is greatest.
**Formula:** $F_\text{m} = qvB \sin\alpha$, when $\alpha = 90^\circ$: $F_\text{m} = qvB$
**Conversions:** Not needed: all quantities are in SI units, and $1\,\text{C} \cdot 1\,\tfrac{\text{m}}{\text{s}} \cdot 1\,\text{T} = 1\,\text{N}$.
**Substitution:** $$\begin{aligned} F_\text{m} &= 1.602 \cdot 10^{-19}\,\text{C} \\ &\cdot 3.0 \cdot 10^{5}\,\tfrac{\text{m}}{\text{s}} \cdot 0.25\,\text{T} \\ &= 1.2015 \cdot 10^{-14}\,\text{N} \end{aligned}$$
**Answer:** $1.2 \cdot 10^{-14}\,\text{N}$, two significant figures like the speed $3.0 \cdot 10^{5}\,\text{m/s}$ and the field $0.25\,\text{T}$.
**Reasonableness:** The force is very small, but the mass of a proton is only $1.7 \cdot 10^{-27}\,\text{kg}$, so the acceleration is about $10^{13}\,\text{m/s}^2$: the beam clearly curves within a few centimetres. With rounded numbers $$\begin{aligned} &1.6 \cdot 10^{-19}\,\text{C} \cdot 3 \cdot 10^{5}\,\text{m/s} \\ &\cdot 0.25\,\text{T} \\ &\approx 1.2 \cdot 10^{-14}\,\text{N} \end{aligned}$$, the same result.

## fy7-2-L1-02
**Given:** electron, $m = 9.109 \cdot 10^{-31}\,\text{kg}$, magnitude of the charge ${|q| = e = 1.602 \cdot 10^{-19}\,\text{C}}$, $v = 2.0 \cdot 10^{6}\,\text{m/s}$ perpendicular to the field, $B = 1.5\,\text{mT}$
**Find:** the radius $r$ of the circular path in millimetres
**Principle:** The magnetic force is perpendicular to the velocity and of constant magnitude, so the electron is in uniform circular motion and the magnetic force is its centripetal force.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ |q|vB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{|q|B} \end{aligned}$$
**Conversions:** $B = 1.5\,\text{mT} = 1.5 \cdot 0.001\,\text{T} = 1.5 \cdot 10^{-3}\,\text{T}$; finally $1\,\text{m} = 1000\,\text{mm}$.
**Substitution:** $r = \dfrac{9.109 \cdot 10^{-31}\,\text{kg} \cdot 2.0 \cdot 10^{6}\,\text{m/s}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 1.5 \cdot 10^{-3}\,\text{T}} = 7.581 \cdot 10^{-3}\,\text{m} = 7.581\,\text{mm}$
**Answer:** $7.6\,\text{mm}$, two significant figures like the speed and the field.
**Reasonableness:** The mass of an electron is very small, so even a weak field, measured in millitesla, bends it onto a small circle. With the same values a proton would go round a circle about $1840$ times larger, with a radius of about $14\,\text{m}$.

## fy7-2-L1-03
**Given:** $E = 4.0 \cdot 10^{4}\,\text{V/m}$, $B = 0.080\,\text{T}$, fields perpendicular to each other
**Find:** the speed $v$ at which ions pass straight through, in kilometres per second
**Principle:** An ion passing straight through the selector is acted on by an electric force $qE$ and a magnetic force $qvB$ that are equal and opposite, so the net force is zero and the path does not curve.
**Formula:** $$\begin{aligned} \Sigma F &= 0 \\ F_\text{s} &= F_\text{m} \\ qE &= qvB \\ v &= \dfrac{E}{B} \end{aligned}$$
**Conversions:** $\tfrac{\text{V/m}}{\text{T}} = \tfrac{\text{m}}{\text{s}}$; finally $1\,\text{km/s} = 1000\,\text{m/s}$.
**Substitution:** $v = \dfrac{4.0 \cdot 10^{4}\,\text{V/m}}{0.080\,\text{T}} = 5.0 \cdot 10^{5}\,\text{m/s} = 500\,\text{km/s}$
**Answer:** $5.0 \cdot 10^{2}\,\text{km/s}$, or $500\,\text{km/s}$, two significant figures like the fields.
**Reasonableness:** The result does not depend on the mass or the charge of the ion. The speed is about $0.2\,\%$ of the speed of light, a usual speed for an ion beam. Check: $qvB = q \cdot 5.0 \cdot 10^{5} \cdot 0.080 = q \cdot 4.0 \cdot 10^{4} = qE$.

## fy7-2-L1-04
**Given:** alpha particle, $q = 3.204 \cdot 10^{-19}\,\text{C}$, accelerating voltage $U = 1.5\,\text{kV}$, starts from rest
**Find:** the kinetic energy $E_\text{k}$ in the form $\ldots \cdot 10^{-16}\,\text{J}$
**Principle:** The electric field does work $W = qU$ on the particle as it travels across the voltage $U$. In a vacuum all of the kinetic energy of a particle starting from rest comes from this work.
**Formula:** $E_\text{k} = W = qU$
**Conversions:** $U = 1.5\,\text{kV} = 1.5 \cdot 1000\,\text{V} = 1500\,\text{V}$, and $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$.
**Substitution:** $E_\text{k} = 3.204 \cdot 10^{-19}\,\text{C} \cdot 1500\,\text{V} = 4.806 \cdot 10^{-16}\,\text{J}$
**Answer:** $4.8 \cdot 10^{-16}\,\text{J}$, two significant figures like the voltage $1.5\,\text{kV}$.
**Reasonableness:** The charge of an alpha particle is twice that of a proton, so it gains twice the energy from the same voltage; a proton would gain $1.602 \cdot 10^{-19}\,\text{C} \cdot 1500\,\text{V} = 2.4 \cdot 10^{-16}\,\text{J}$. The energy does not depend on the mass.

## fy7-2-L1-05
**Given:** proton, $q = 1.602 \cdot 10^{-19}\,\text{C}$, $v = 5.0 \cdot 10^{6}\,\text{m/s}$, $B = 0.40\,\text{T}$, angle between the velocity and the field $\alpha = 30^\circ$
**Find:** the magnetic force $F_\text{m}$ in the form $\ldots \cdot 10^{-13}\,\text{N}$
**Principle:** The magnetic force depends on the angle between the velocity and the field: only the part $v \sin\alpha$ of the velocity that is perpendicular to the field causes a force.
**Formula:** $F_\text{m} = qvB \sin\alpha$
**Conversions:** Not needed: the quantities are in SI units, and $\sin 30^\circ = 0.5$.
**Substitution:** $$\begin{aligned} F_\text{m} &= 1.602 \cdot 10^{-19}\,\text{C} \\ &\cdot 5.0 \cdot 10^{6}\,\tfrac{\text{m}}{\text{s}} \cdot 0.40\,\text{T} \cdot 0.5 \\ &= 1.602 \cdot 10^{-13}\,\text{N} \end{aligned}$$
**Answer:** $1.6 \cdot 10^{-13}\,\text{N}$, two significant figures like the speed and the field.
**Reasonableness:** In a perpendicular field the force would be twice as great, $3.2 \cdot 10^{-13}\,\text{N}$; the angle $30^\circ$ halves it, because only half of the velocity is perpendicular to the field. A proton moving along the field would not be acted on by any force.

## fy7-2-L1-06
**Find:** what happens to the kinetic energy of a proton as it travels in a magnetic field perpendicular to the field.
**Principle:** Kinetic energy changes only if the force acting on the particle does work. The magnetic force $qvB$ is always perpendicular to the velocity, so it does no work and does not change the speed. It only turns the direction of motion and acts as the centripetal force of the circular path. Only an electric field can change the speed.
**Model answer:** The kinetic energy stays the same. The proton goes round a circular path at a constant speed, because the force is perpendicular to the velocity all the time and does no work.

The field neither accelerates nor brakes the proton, and the force is not in the direction of the field but perpendicular to both the field and the velocity. A strong field does not change this: it only bends the path into a smaller circle.

## fy7-2-L1-07
**Given:** electron, $m = 9.109 \cdot 10^{-31}\,\text{kg}$, $q = 1.602 \cdot 10^{-19}\,\text{C}$, $v = 3.0 \cdot 10^{6}\,\text{m/s}$ perpendicular to the field, radius of the circular path $r = 4.0\,\text{cm}$
**Find:** the magnetic flux density $B$ in millitesla
**Principle:** The magnetic force is perpendicular to the velocity and constant in magnitude, so it is the centripetal force of the circular motion of the electron.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ B &= \dfrac{mv}{qr} \end{aligned}$$
**Conversions:** $r = 4.0\,\text{cm} = 4.0 \cdot 0.01\,\text{m} = 0.040\,\text{m}$; finally $1\,\text{T} = 1000\,\text{mT}$.
**Substitution:** $$\begin{aligned} &B \\ &= \dfrac{9.109 \cdot 10^{-31}\,\text{kg} \cdot 3.0 \cdot 10^{6}\,\text{m/s}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 0.040\,\text{m}} \\ &= 4.264 \cdot 10^{-4}\,\text{T} \\ &= 0.4264\,\text{mT} \end{aligned}$$
**Answer:** $0.43\,\text{mT}$, two significant figures like the speed and the radius.
**Reasonableness:** The field is about 8.5 times the magnetic field of the Earth ($0.05\,\text{mT}$), so a small coil easily produces it. Calculating back, $r = \dfrac{mv}{qB} = \dfrac{9.109 \cdot 10^{-31}\,\text{kg} \cdot 3.0 \cdot 10^{6}\,\text{m/s}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 4.264 \cdot 10^{-4}\,\text{T}} = 0.040\,\text{m}$.

## fy7-2-L1-08
**Given:** electron, $m = 9.109 \cdot 10^{-31}\,\text{kg}$, $q = 1.602 \cdot 10^{-19}\,\text{C}$, $v = 5.0 \cdot 10^{6}\,\text{m/s}$ perpendicular to the field, $B = 0.020\,\text{T}$
**Find:** the time taken by one revolution, the period $T$, in nanoseconds
**Principle:** On a circular path the period is the length of the path divided by the speed. The magnetic force is the centripetal force, so the radius follows from it, and the speed cancels from the expression for the period.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{qB} \\ T &= \dfrac{2\pi r}{v} \\ &= \dfrac{2\pi m}{qB} \end{aligned}$$
**Conversions:** Not needed: the quantities are in SI units. Finally $1\,\text{s} = 10^{9}\,\text{ns}$.
**Substitution:** $T = \dfrac{2\pi \cdot 9.109 \cdot 10^{-31}\,\text{kg}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 0.020\,\text{T}} = 1.786 \cdot 10^{-9}\,\text{s} = 1.786\,\text{ns}$
**Answer:** $1.8\,\text{ns}$, two significant figures like the field $0.020\,\text{T}$. The speed $5.0 \cdot 10^{6}\,\text{m/s}$ does not affect the result.
**Reasonableness:** Through the radius: $r = \dfrac{mv}{qB} = 1.42 \cdot 10^{-3}\,\text{m}$ and $T = \dfrac{2\pi r}{v} = \dfrac{2\pi \cdot 1.42 \cdot 10^{-3}\,\text{m}}{5.0 \cdot 10^{6}\,\text{m/s}} = 1.79 \cdot 10^{-9}\,\text{s}$, the same result. If the speed were doubled, the radius and the circumference would double, and the period would stay the same.

## fy7-2-L2-01
**Given:** proton, $m = 1.673 \cdot 10^{-27}\,\text{kg}$, $q = 1.602 \cdot 10^{-19}\,\text{C}$, accelerating voltage $U = 500\,\text{V}$, starts from rest; $B = 0.050\,\text{T}$ perpendicular to the velocity
**Find:** the radius $r$ of the circular path in centimetres
**Principle:** In the acceleration the work $qU$ done by the electric field becomes the kinetic energy of the proton, because the proton starts from rest in a vacuum. In the magnetic field the magnetic force $qvB$ is the centripetal force of the circular path and does not change the speed.
**Formula:** $$\begin{aligned} W &= \Delta E_\text{k} \\ qU &= \tfrac{1}{2}mv^2 \\ v &= \sqrt{\dfrac{2qU}{m}} \\ \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{qB} \end{aligned}$$
**Conversions:** Not needed: the quantities are in SI units. Finally $1\,\text{m} = 100\,\text{cm}$.
**Substitution:** $v = \sqrt{\dfrac{2 \cdot 1.602 \cdot 10^{-19}\,\text{C} \cdot 500\,\text{V}}{1.673 \cdot 10^{-27}\,\text{kg}}} = 3.0945 \cdot 10^{5}\,\text{m/s}$ and
$$\begin{aligned} r &= \dfrac{1.673 \cdot 10^{-27}\,\text{kg}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 0.050\,\text{T}} \\ &\quad \cdot 3.0945 \cdot 10^{5}\,\text{m/s} \\ &= 0.06463\,\text{m} = 6.463\,\text{cm} \end{aligned}$$
**Answer:** $6.5\,\text{cm}$, two significant figures like the field $0.050\,\text{T}$; the voltage $500\,\text{V}$ is taken to have at least two figures.
**Reasonableness:** The speed $3 \cdot 10^{5}\,\text{m/s}$ is about $0.1\,\%$ of the speed of light, so classical mechanics holds. The radius is of the size of laboratory equipment. If the accelerating voltage were quadrupled, the speed and the radius would double.

## fy7-2-L2-02
**Given:** deuteron, $m = 3.344 \cdot 10^{-27}\,\text{kg}$, $q = 1.602 \cdot 10^{-19}\,\text{C}$, radius of the path $r = 12\,\text{cm}$, $B = 0.60\,\text{T}$
**Find:** the speed $v$ of the deuteron in kilometres per second
**Principle:** The deuteron goes round a circle because the magnetic force $qvB$ is perpendicular to the velocity and acts as the centripetal force.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ v &= \dfrac{qBr}{m} \end{aligned}$$
**Conversions:** $r = 12\,\text{cm} = 12 \cdot 0.01\,\text{m} = 0.12\,\text{m}$; finally $1\,\text{km/s} = 1000\,\text{m/s}$.
**Substitution:** $v = \dfrac{\begin{aligned}1.602 \cdot 10^{-19}\,\text{C} \cdot 0.60\,\text{T} \\ \cdot 0.12\,\text{m}\end{aligned}}{3.344 \cdot 10^{-27}\,\text{kg}}$
$= 3.449 \cdot 10^{6}\,\text{m/s}$
$= 3449\,\text{km/s}$
**Answer:** $3.4 \cdot 10^{3}\,\text{km/s}$, two significant figures like the radius $12\,\text{cm}$ and the field $0.60\,\text{T}$.
**Reasonableness:** The speed is about $1\,\%$ of the speed of light, so the classical formula still holds. Calculating back, $$\begin{aligned} r &= mv : (qB) \\ &= 3.344 \cdot 10^{-27} \cdot 3.449 \cdot 10^{6} \\ &: (1.602 \cdot 10^{-19} \cdot 0.60)\,\text{m} \\ &= 0.12\,\text{m} \end{aligned}$$.

## fy7-2-L2-03
**Given:** distance between the plates $d = 2.0\,\text{cm}$, voltage between the plates $U = 600\,\text{V}$, magnetic flux density $B = 0.15\,\text{T}$ perpendicular to the electric field
**Find:** the speed $v$ at which ions pass straight through, in kilometres per second
**Principle:** The field between the plates is uniform, so its strength is the voltage divided by the distance between the plates (chapter *Uniform electric field*). On an ion passing straight through, the electric and magnetic forces are equal and opposite.
**Formula:** $$\begin{aligned} \Sigma F &= 0 \\ qE &= qvB \\ v &= \dfrac{E}{B} \\ E &= \dfrac{U}{d} \\ v &= \dfrac{U}{dB} \end{aligned}$$
**Conversions:** $d = 2.0\,\text{cm} = 2.0 \cdot 0.01\,\text{m} = 0.020\,\text{m}$; finally $1\,\text{km/s} = 1000\,\text{m/s}$.
**Substitution:** $E = \dfrac{600\,\text{V}}{0.020\,\text{m}} = 3.0 \cdot 10^{4}\,\text{V/m}$ and $v = \dfrac{3.0 \cdot 10^{4}\,\text{V/m}}{0.15\,\text{T}} = 2.0 \cdot 10^{5}\,\text{m/s} = 200\,\text{km/s}$
**Answer:** $2.0 \cdot 10^{2}\,\text{km/s}$, or $200\,\text{km/s}$, two significant figures like the distance $2.0\,\text{cm}$ and the field $0.15\,\text{T}$.
**Reasonableness:** At this speed the selector lets through all ions, whatever their mass and charge. If the plates were twice as far apart, the field and the selected speed would be halved.

## fy7-2-L2-04
**Given:** the Earth's magnetic field $B = 50\,\mu\text{T}$, proton $m = 1.673 \cdot 10^{-27}\,\text{kg}$, $q = 1.602 \cdot 10^{-19}\,\text{C}$, velocity perpendicular to the field; $g = 9.81\,\text{m/s}^2$
**Find:** the speed $v$ at which the magnetic force equals the weight of the proton, in millimetres per second
**Principle:** In a perpendicular field the magnetic force is $qvB$ and the weight is $mg$. The speed asked for is found by setting these equal.
**Formula:** $$\begin{aligned} \Sigma F &= 0 \\ F_\text{m} &= G \\ qvB &= mg \\ v &= \dfrac{mg}{qB} \end{aligned}$$
**Conversions:** $B = 50\,\mu\text{T} = 50 \cdot 10^{-6}\,\text{T} = 5.0 \cdot 10^{-5}\,\text{T}$; finally $1\,\text{m/s} = 1000\,\text{mm/s}$.
**Substitution:** $v = \dfrac{1.673 \cdot 10^{-27}\,\text{kg} \cdot 9.81\,\text{m/s}^2}{1.602 \cdot 10^{-19}\,\text{C} \cdot 5.0 \cdot 10^{-5}\,\text{T}} = 2.049 \cdot 10^{-3}\,\text{m/s} = 2.049\,\text{mm/s}$
**Answer:** $2.0\,\text{mm/s}$, two significant figures like the field $50\,\mu\text{T}$.
**Reasonableness:** Even in the weak field of the Earth, a proton moving at the speed of a snail is acted on by a magnetic force as great as its weight. At the usual speeds of particles, about $10^{6}\,\text{m/s}$, the magnetic force is thus about $10^{8}$ to $10^{9}$ times the weight, and that is why gravity is neglected.

## fy7-2-L2-05
**Given:** $B = 0.050\,\text{T}$ into the page; for all ions $v = 2.0 \cdot 10^{5}\,\text{m/s}$ to the right and $q = 1.602 \cdot 10^{-19}\,\text{C}$; paths: 1 curves up, $r_1 = 4.1\,\text{cm}$, 2 down, $r_2 = 4.2\,\text{cm}$, 3 up, $r_3 = 8.4\,\text{cm}$; mass of a proton $m_\text{p} = 1.673 \cdot 10^{-27}\,\text{kg}$
**Find:** a) the signs of the charges of the ions, b) the ratio $m : q$ of the ion on path 1 in the form $\ldots \cdot 10^{-8}\,\text{kg/C}$ and the identification of the ion, c) the ratio of the ratios $m : q$ of path 3 and path 1
**Principle:** a) In the right-hand rule the thumb points in the direction of the velocity, that is to the right, the index finger in the direction of the field, that is into the page, and the middle finger points up.

So a positive charge is acted on by a force upwards and a negative charge by a force downwards. The path curves in the direction of the force.

b) The magnetic force is the centripetal force, $qvB = mv^2 : r$, so $m : q$ follows from the radius when the speed and the field are known.

c) At the same speed and field $m : q = rB : v$ is proportional to the radius, so the ratio of the ratios is the ratio of the radii.
**Reading the graph:** From the table: paths 1 and 3 curve up, path 2 down. The radii are $4.1\,\text{cm}$, $4.2\,\text{cm}$ and $8.4\,\text{cm}$.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{qB} \\ \dfrac{m}{q} &= \dfrac{rB}{v} \end{aligned}$$
**Conversions:** $r_1 = 4.1\,\text{cm} = 4.1 \cdot 0.01\,\text{m} = 0.041\,\text{m}$; $\tfrac{\text{m} \cdot \text{T}}{\text{m/s}} = \tfrac{\text{kg}}{\text{C}}$.
**Substitution:** a) Paths 1 and 3: positive charge; path 2: negative charge. b) $\dfrac{m}{q} = \dfrac{0.041\,\text{m} \cdot 0.050\,\text{T}}{2.0 \cdot 10^{5}\,\text{m/s}} = 1.025 \cdot 10^{-8}\,\text{kg/C}$. For a proton $\dfrac{m_\text{p}}{e} = \dfrac{1.673 \cdot 10^{-27}\,\text{kg}}{1.602 \cdot 10^{-19}\,\text{C}} = 1.044 \cdot 10^{-8}\,\text{kg/C}$. c) $\dfrac{m_3 : q_3}{m_1 : q_1} = \dfrac{r_3}{r_1} = \dfrac{8.4\,\text{cm}}{4.1\,\text{cm}} = 2.05$
**Answer:** a) Paths 1 and 3 are of positive particles, path 2 of a negative particle. b) $1.0 \cdot 10^{-8}\,\text{kg/C}$, two significant figures like the speed and the field; the value agrees with that of the proton, so the particle on path 1 can be a proton (an H$^+$ ion). c) About double, $2.0$ times.
**Reasonableness:** The value for path 1 differs from that of the proton by less than $2\,\%$, which is within the precision of the measurement.

The ion on path 2 has almost the same $m : q$ but the opposite charge: it can be an H$^-$ ion, in which two electrons surround the proton and the mass is practically the mass of the proton.

The $m : q = 2.1 \cdot 10^{-8}\,\text{kg/C}$ of the ion on path 3 is double, for example an H$_2^+$ ion, whose mass is double and charge $e$. The speed $2.0 \cdot 10^{5}\,\text{m/s}$ corresponds to an energy of about $210\,\text{eV}$ for a proton, so the ion beam travels in the vacuum chamber without collisions.

## fy7-2-L2-06
**Given:** points of impact A, B and C at distances $d_\text{A} = 19.2\,\text{cm}$, $d_\text{B} = 20.1\,\text{cm}$ and $d_\text{C} = 20.7\,\text{cm}$, hits $N_\text{A} = 7890$, $N_\text{B} = 1000$ and $N_\text{C} = 1110$; $m_\text{A} = 24.0\,\text{u}$; the same charge, speed and field
**Find:** a) the masses of ions B and C in atomic mass units, b) the share of the ions that hit A as a percentage
**Principle:** The ions travel a semicircle, so $d = 2r$. Since $r = mv : (qB)$ and $q$, $v$ and $B$ are the same, the distance $d$ of the point of impact is proportional to the mass. The number of hits is proportional to the share of the isotope in the ion source.
**Reading the graph:** From the table: the lightest ion hits closest to the slit and clearly the most of them hit there.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{qB} \\ d &= 2r \\ &= \dfrac{2v}{qB}\,m \\ \dfrac{m}{m_\text{A}} &= \dfrac{d}{d_\text{A}} \\ m &= m_\text{A} \cdot \dfrac{d}{d_\text{A}} \\ p_\text{A} &= \dfrac{N_\text{A}}{N_\text{A} + N_\text{B} + N_\text{C}} \\ &\cdot 100\,\% \end{aligned}$$
**Conversions:** Not needed: the distances are in the same unit and cancel. The sum of the hits is $7890 + 1000 + 1110 = 10000$.
**Substitution:** a) $m_\text{B} = 24.0\,\text{u} \cdot \dfrac{20.1\,\text{cm}}{19.2\,\text{cm}} = 25.1\,\text{u}$ and $m_\text{C} = 24.0\,\text{u} \cdot \dfrac{20.7\,\text{cm}}{19.2\,\text{cm}} = 25.9\,\text{u}$. b) The sum is $10000$, so $p_\text{A} = \dfrac{7890}{10000} \cdot 100\,\% = 78.9\,\%$
**Answer:** a) $25.1\,\text{u}$ and $25.9\,\text{u}$, so the mass numbers of the isotopes are $24$, $25$ and $26$. b) $78.9\,\%$, three significant figures like the numbers of hits.
**Reasonableness:** The masses are close to the integers $25$ and $26$, as they should be for isotopes. One mass unit corresponds to a shift of the point of impact of $19.2\,\text{cm} : 24.0 = 0.80\,\text{cm}$. The shares of the other isotopes are $10.0\,\%$ and $11.1\,\%$, and altogether $$\begin{aligned} &78.9\,\% + 10.0\,\% + 11.1\,\% \\ &= 100\,\% \end{aligned}$$.

## fy7-2-L2-07
**Find:** what is the error in the reasoning of the student who claims that a faster particle completes a revolution faster.
**Principle:** The period is the length of the path divided by the speed, $T = 2\pi r : v$. The student treats the circumference as constant, but in a magnetic field the radius $r = mv : (qB)$ grows with the speed. Substituting the radius gives $T = 2\pi m : (qB)$, which does not contain the speed.
**Model answer:** The student forgets that the radius does not stay the same. Double the speed gives double the radius and so double the circumference, and double the distance is travelled at double the speed in the same time as before. The period depends only on the mass and the charge of the particle and on the field.

Nor does the magnetic force accelerate the particle, because it is perpendicular to the velocity, and the radius does not decrease as the speed increases. The radius does not grow more steeply than the speed either: it is directly proportional to the speed.

## fy7-2-L3-01
**Given:** carbon-12 and carbon-14 ions, the same charge $q$, the same accelerating voltage $U$ from rest, the same magnetic field $B$; $m_{12} = 12.0\,\text{u}$, $m_{14} = 14.0\,\text{u}$, $r_{12} = 25.0\,\text{cm}$; the ions travel along a semicircle
**Find:** the distance $\Delta d$ between the points of impact in centimetres
**Principle:** In the acceleration $qU = \tfrac{1}{2}mv^2$, so a heavier ion gets a smaller speed. In the field the magnetic force is the centripetal force, $r = mv : (qB)$.

When the speed is substituted, the radius is $r = \tfrac{1}{B}\sqrt{\tfrac{2mU}{q}}$, so with the same $U$, $q$ and $B$ the radius is proportional to the square root of the mass. The distance of the point of impact from the slit is the diameter $2r$.
**Formula:** $$\begin{aligned} qU &= \tfrac{1}{2}mv^2 \\ v &= \sqrt{\dfrac{2qU}{m}} \\ \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{qB} \\ &= \dfrac{1}{B}\sqrt{\dfrac{2mU}{q}} \\ \dfrac{r_{14}}{r_{12}} &= \sqrt{\dfrac{m_{14}}{m_{12}}} \\ r_{14} &= r_{12}\sqrt{\dfrac{m_{14}}{m_{12}}} \\ \Delta d &= 2r_{14} - 2r_{12} \\ &= 2\left(r_{14} - r_{12}\right) \end{aligned}$$
**Conversions:** Not needed: the masses are in the same unit and cancel, and the radius stays in centimetres.
**Substitution:** $r_{14} = 25.0\,\text{cm} \cdot \sqrt{\dfrac{14.0\,\text{u}}{12.0\,\text{u}}} = 27.003\,\text{cm}$ and $\Delta d = 2 \cdot (27.003\,\text{cm} - 25.0\,\text{cm}) = 4.006\,\text{cm}$
**Answer:** $4.0\,\text{cm}$, two significant figures, because the precision of the difference $27.0\,\text{cm} - 25.0\,\text{cm}$ is a tenth of a centimetre.
**Reasonableness:** Carbon-14 is about $17\,\%$ heavier, but the radius grows by only about $8\,\%$, because the heavier ion gets a smaller speed from the same voltage. A difference of four centimetres is quite enough for the ions to land on different detectors.

## fy7-2-L3-02
**Given:** proton, $m = 1.673 \cdot 10^{-27}\,\text{kg}$, $q = 1.602 \cdot 10^{-19}\,\text{C}$, $B = 1.50\,\text{T}$
**Find:** a justification that the period of revolution does not depend on the speed, and the frequency of revolution $f$ in megahertz
**Principle:** The proton goes round a circle because the magnetic force $qvB$ is the centripetal force. In uniform circular motion the period is the length of the path divided by the speed (chapter *Moving in a circle: period and speed*), and the frequency is the reciprocal of the period.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{qB} \\ T &= \dfrac{2\pi r}{v} \\ &= \dfrac{2\pi m}{qB} \\ f &= \dfrac{1}{T} \\ &= \dfrac{qB}{2\pi m} \end{aligned}$$ The speed $v$ cancels, so $T$ does not depend on the speed.
**Conversions:** Not needed: the quantities are in SI units, and $\tfrac{\text{C} \cdot \text{T}}{\text{kg}} = \tfrac{1}{\text{s}}$. Finally $1\,\text{MHz} = 10^{6}\,\text{Hz}$.
**Substitution:** $f = \dfrac{1.602 \cdot 10^{-19}\,\text{C} \cdot 1.50\,\text{T}}{2\pi \cdot 1.673 \cdot 10^{-27}\,\text{kg}} = 2.286 \cdot 10^{7}\,\text{Hz} = 22.86\,\text{MHz}$
**Answer:** $22.9\,\text{MHz}$, three significant figures like the field $1.50\,\text{T}$.
**Reasonableness:** A faster proton goes round a larger circle, but the radius grows in the same proportion as the speed, so the period $T = 1 : f \approx 44\,\text{ns}$ stays the same. That is why the accelerating voltage of a cyclotron can change direction at a constant frequency. The frequency is in the range of radio frequencies, which electrical devices produce easily.

## fy7-2-L3-03
**Given:** proton $m_\text{p} = 1.673 \cdot 10^{-27}\,\text{kg}$, charge $e$; alpha particle $m_\alpha = 6.645 \cdot 10^{-27}\,\text{kg}$, charge $2e$; the same accelerating voltage $U$ from rest and the same field $B$
**Find:** the ratio of the radii $r_\alpha : r_\text{p}$
**Principle:** In the acceleration $qU = \tfrac{1}{2}mv^2$, so $v = \sqrt{2qU : m}$. In the field the magnetic force is the centripetal force and $r = mv : (qB)$. Substituting the speed gives $r = \tfrac{1}{B}\sqrt{\tfrac{2mU}{q}}$: with the same $U$ and $B$ the radius is proportional to $\sqrt{m : q}$.
**Formula:** $$\begin{aligned} qU &= \tfrac{1}{2}mv^2 \\ \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ r &= \dfrac{1}{B}\sqrt{\dfrac{2mU}{q}} \\ \dfrac{r_\alpha}{r_\text{p}} &= \sqrt{\dfrac{m_\alpha : q_\alpha}{m_\text{p} : q_\text{p}}} \\ &= \sqrt{\dfrac{m_\alpha \, q_\text{p}}{m_\text{p} \, q_\alpha}} \end{aligned}$$
**Conversions:** Not needed: the masses and charges cancel in the ratio when they are in the same units; $q_\text{p} : q_\alpha = e : 2e = 1 : 2$.
**Substitution:** $\dfrac{r_\alpha}{r_\text{p}} = \sqrt{\dfrac{6.645 \cdot 10^{-27}\,\text{kg} \cdot e}{1.673 \cdot 10^{-27}\,\text{kg} \cdot 2e}} = \sqrt{1.986} = 1.409$
**Answer:** $1.41$ times, three significant figures; the result is almost exactly $\sqrt{2}$.
**Reasonableness:** An alpha particle has about four times the mass and twice the charge, so $m : q$ is twice as great and the radius is $\sqrt{2} \approx 1.41$ times as large. An alpha particle gains twice the energy of a proton from the same voltage but a smaller speed, and the greater mass wins: the path is gentler.

## fy7-2-L3-04
**Given:** ions $q = e = 1.602 \cdot 10^{-19}\,\text{C}$, accelerated from rest by a voltage $U$, $B = 0.200\,\text{T}$; measurements $(U;\ r)$: $(200\,\text{V};\ 4.9\,\text{cm})$, $(400\,\text{V};\ 6.8\,\text{cm})$, $(600\,\text{V};\ 8.5\,\text{cm})$, $(800\,\text{V};\ 9.8\,\text{cm})$ and $(1000\,\text{V};\ 10.8\,\text{cm})$; $1\,\text{u} = 1.661 \cdot 10^{-27}\,\text{kg}$; options lithium-7, sodium-23 and potassium-39
**Find:** a) $r^2$ as a function of the voltage $U$, b) the mass $m$ of the ion in atomic mass units, c) the identification of the ion and why the line passes through the origin
**Principle:** In the acceleration the work $qU$ of the electric field becomes the kinetic energy of the ion, $qU = \tfrac{1}{2}mv^2$. In the magnetic field the magnetic force is the centripetal force, $qvB = mv^2 : r$, from which $v = qBr : m$. Substituting the speed into the acceleration equation gives a line $r^2 = kU$, whose slope $k$ tells the mass.
**Reading the graph:** We calculate $r^2$: $24.0$, $46.2$, $72.3$, $96.0$ and $116.6\,\text{cm}^2$. When these are plotted as a function of the voltage, the points lie around a line through the origin; the quotient $r^2 : U$ is about $0.12\,\text{cm}^2/\text{V}$ at every point.

The slope of the line fitted to the points is $k = 0.118\,\dfrac{\text{cm}^2}{\text{V}}$ (a least-squares fit through the origin; a well-drawn line gives the same slope).
**Formula:** a) $$\begin{aligned} qU &= \tfrac{1}{2}mv^2 \\ qvB &= m\dfrac{v^2}{r} \\ v &= \dfrac{qBr}{m} \\ qU &= \dfrac{q^2B^2r^2}{2m} \\ r^2 &= \dfrac{2m}{qB^2}\,U \end{aligned}$$ b) $$\begin{aligned} k &= \dfrac{2m}{qB^2} \\ m &= \dfrac{qB^2k}{2} \end{aligned}$$
**Conversions:** $k = 0.118\,\dfrac{\text{cm}^2}{\text{V}} = 0.118 \cdot 10^{-4}\,\dfrac{\text{m}^2}{\text{V}} = 1.18 \cdot 10^{-5}\,\dfrac{\text{m}^2}{\text{V}}$; finally $m$ is divided by the atomic mass unit.
**Substitution:** $$\begin{aligned} &m \\ &= \dfrac{1.602 \cdot 10^{-19}\,\text{C} \cdot (0.200\,\text{T})^2}{2} \\ &\cdot 1.18 \cdot 10^{-5}\,\text{m}^2/\text{V} \\ &= 3.78 \cdot 10^{-26}\,\text{kg} \end{aligned}$$, that is in atomic mass units $\dfrac{3.78 \cdot 10^{-26}\,\text{kg}}{1.661 \cdot 10^{-27}\,\text{kg}} = 22.8\,\text{u}$
**Answer:** a) $r^2 = \dfrac{2m}{qB^2}\,U$, a line through the origin. b) about $23\,\text{u}$ ($22.8\,\text{u}$); the precision is limited by the two significant figures of the radii, so for a line fitted by hand $22\text{–}23\,\text{u}$ is a good answer. c) The ion is sodium-23, whose mass is about $23\,\text{u}$. The line must pass through the origin, because when $U = 0$ the ion gains no kinetic energy and has no path, $r = 0$.
**Reasonableness:** Lithium-7 ($7\,\text{u}$) would give the slope $$\begin{aligned} &0.118\,\text{cm}^2/\text{V} \cdot 7 : 22.8 \\ &= 0.036\,\text{cm}^2/\text{V} \end{aligned}$$ and potassium-39 ($39\,\text{u}$) the value $0.202\,\text{cm}^2/\text{V}$, each clearly different from the measurement.

For sodium-23 the formula $r^2 = 2mU : (qB^2)$ gives at the voltage $U = 400\,\text{V}$ the radius $r = 6.9\,\text{cm}$, which agrees with the measured value $6.8\,\text{cm}$. The speed at this voltage is about $6 \cdot 10^{4}\,\text{m/s}$, so the classical treatment is valid.

## fy7-2-L3-05
**Given:** $B = 1.00\,\text{T}$, accelerating voltage of a gap crossing $U = 60.0\,\text{kV}$, two crossings per revolution, extraction radius $r = 0.200\,\text{m}$, $m = 1.673 \cdot 10^{-27}\,\text{kg}$, $q = 1.602 \cdot 10^{-19}\,\text{C}$, $c = 3.00 \cdot 10^{8}\,\text{m/s}$; the proton starts practically from rest
**Find:** a) the speed and the kinetic energy at the moment of extraction, b) the number of gap crossings and revolutions and the acceleration time $t$ in microseconds, c) the ratio of the speed to the speed of light and an assessment of the classical treatment
**Principle:** The magnetic field does not change the speed but bends the path, so the speed follows from the extraction radius by the formula $r = mv : (qB)$.

All the kinetic energy is given by the electric field: each gap crossing gives the energy $qU$. The period $T = 2\pi m : (qB)$ depends neither on the speed nor on the radius, so the acceleration time is the number of revolutions times $T$.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ qvB &= m\dfrac{v^2}{r} \\ v &= \dfrac{qBr}{m} \\ E_\text{k} &= \tfrac{1}{2}mv^2 \\ E_\text{k} &= n\,qU \\ n &= \dfrac{E_\text{k}}{qU} \\ T &= \dfrac{2\pi r}{v} \\ &= \dfrac{2\pi m}{qB} \\ t &= \dfrac{n}{2}\,T \end{aligned}$$
**Conversions:** $U = 60.0\,\text{kV} = 60.0 \cdot 1000\,\text{V} = 6.00 \cdot 10^{4}\,\text{V}$; finally $1\,\mu\text{s} = 10^{-6}\,\text{s}$.
**Substitution:** a) $$\begin{aligned} &v \\ &= \dfrac{1.602 \cdot 10^{-19}\,\text{C} \cdot 1.00\,\text{T} \cdot 0.200\,\text{m}}{1.673 \cdot 10^{-27}\,\text{kg}} \\ &= 1.92 \cdot 10^{7}\,\text{m/s} \end{aligned}$$ and $$\begin{aligned} E_\text{k} &= \tfrac{1}{2} \cdot 1.673 \cdot 10^{-27}\,\text{kg} \\ &\cdot (1.92 \cdot 10^{7}\,\text{m/s})^2 \\ &= 3.07 \cdot 10^{-13}\,\text{J} \end{aligned}$$.

b) In one crossing the energy increases by $qU = 1.602 \cdot 10^{-19}\,\text{C} \cdot 6.00 \cdot 10^{4}\,\text{V} = 9.61 \cdot 10^{-15}\,\text{J}$, so $n = \dfrac{3.07 \cdot 10^{-13}\,\text{J}}{9.61 \cdot 10^{-15}\,\text{J}} = 31.9 \approx 32$ crossings, that is $16$ revolutions. The period is $T = \dfrac{2\pi \cdot 1.673 \cdot 10^{-27}\,\text{kg}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 1.00\,\text{T}} = 6.56 \cdot 10^{-8}\,\text{s}$, so $t = 16 \cdot 6.56 \cdot 10^{-8}\,\text{s} = 1.05 \cdot 10^{-6}\,\text{s} = 1.05\,\mu\text{s}$.

c) $\dfrac{v}{c} = \dfrac{1.92 \cdot 10^{7}\,\text{m/s}}{3.00 \cdot 10^{8}\,\text{m/s}} = 0.064$
**Answer:** a) $1.92 \cdot 10^{7}\,\text{m/s}$ and $3.07 \cdot 10^{-13}\,\text{J}$ (about $1.9\,\text{MeV}$). b) About $32$ crossings and $16$ revolutions; the acceleration takes $1.05\,\mu\text{s}$, three significant figures like the field and the radius. c) The speed is about $6\,\%$ of the speed of light, so the relativistic correction to the kinetic energy is of the order of $\tfrac{3}{4}(v : c)^2 \approx 0.3\,\%$. The classical treatment is valid here; at greater energies the period would begin to grow, and the switching rate of the accelerating voltage would not stay constant.
**Reasonableness:** The period at the extraction radius: $\dfrac{2\pi r}{v} = \dfrac{2\pi \cdot 0.200\,\text{m}}{1.92 \cdot 10^{7}\,\text{m/s}} = 6.56 \cdot 10^{-8}\,\text{s}$, the same as with the formula $T = 2\pi m : (qB)$. Checking the energy: $$\begin{aligned} &32 \cdot 9.61 \cdot 10^{-15}\,\text{J} \\ &= 3.08 \cdot 10^{-13}\,\text{J} \end{aligned}$$, the same as $E_\text{k}$.

## fy7-2-L2-08
**Find:** which of the four force diagrams correctly shows the forces acting on an electron that moves upwards in a magnetic field pointing out of the page.
**Principle:** Choose the electron as the object. In a vacuum only the magnetic field and the Earth act on it.

The magnetic force is perpendicular to both the velocity and the field, and for a positive charge its direction is given by the right-hand rule; on a negative charge the force points in the opposite direction. The velocity is not a force. The weight is compared with the magnetic force.
**Model answer:** The correct one is force diagram C. In the right-hand rule the thumb points in the direction of the velocity, up, and the other fingers in the direction of the field, out of the page, so the palm pushes to the right. The electron is negative, so the force points to the left. The magnitudes of the forces:

$F_\text{m} = |q| v B$

$$\begin{aligned}
F_\text{m} &= 1.602 \cdot 10^{-19}\,\text{C} \cdot 3.0 \cdot 10^{6}\,\tfrac{\text{m}}{\text{s}} \\
&\quad \cdot 0.50 \cdot 10^{-3}\,\text{T} \\
&\approx 2.4 \cdot 10^{-16}\,\text{N}
\end{aligned}$$

$G = mg$

$$
\begin{aligned}
G &= 9.109 \cdot 10^{-31}\,\text{kg} \\
&\cdot 9.81\,\text{m/s}^2
\end{aligned}
$$

$G \approx 8.9 \cdot 10^{-30}\,\text{N}$

The weight is about $10^{-14}$ times the magnetic force, so only $\overline{F}_\text{m}$ is drawn in the force diagram. In diagram A the force points in the direction of the field, out of the page, although the magnetic force is perpendicular to the field.

In diagram B the direction of the force is that for a positive charge, so the negative charge of the electron has been forgotten. In diagram D the force is along the velocity, although the magnetic force does not change the speed but bends the path of the electron.

## fy7-2-L1-09
**Given:** electron, $v = 4.0 \cdot 10^{6}\,\text{m/s}$ perpendicular to the field, $B = 0.80\,\text{mT}$, magnitude of the charge $|q| = e = 1.602 \cdot 10^{-19}\,\text{C}$; mass from the MAFY table *Hiukkasten ominaisuuksia*: $m = 9.109 \cdot 10^{-31}\,\text{kg}$
**Find:** the radius $r$ of the circular path in centimetres
**Principle:** The magnetic force is perpendicular to the velocity, so the electron moves on a circle and the magnetic force is its centripetal force.
**Formula:** $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ |q|vB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{|q|B} \end{aligned}$$
**Conversions:** $B = 0.80\,\text{mT} = 0.80 \cdot 10^{-3}\,\text{T}$; finally $1\,\text{m} = 100\,\text{cm}$.
**Substitution:** $r = \dfrac{9.109 \cdot 10^{-31}\,\text{kg} \cdot 4.0 \cdot 10^{6}\,\text{m/s}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 0.80 \cdot 10^{-3}\,\text{T}} = 2.843 \cdot 10^{-2}\,\text{m} = 2.843\,\text{cm}$
**Answer:** $2.8\,\text{cm}$, two significant figures like the speed and the field.
**Reasonableness:** In the electron-beam tube of task 2-2 the radius was $7.6\,\text{mm}$. Here the speed is twice as large and the field about half as strong, so the radius is about $3.75$ times as large, roughly $28\,\text{mm}$; a size of centimetres fits.

## fy7-2-L2-09
**Given:** graph $r(v)$, $B = 0.20\,\text{T}$, $|q| = 1.602 \cdot 10^{-19}\,\text{C}$, $v = 1.5 \cdot 10^{6}\,\text{m/s}$, velocity perpendicular to the field
**Find:** the mass $m$ of the particle in the form $\ldots \cdot 10^{-27}\,\text{kg}$
**Principle:** The magnetic force acts as the centripetal force of the circular path, so the mass follows from the radius, the speed, the charge and the field.
**Reading the graph:** At the speed $1.5 \cdot 10^{6}\,\text{m/s}$, that is at the value $1.5$ on the horizontal axis, the point is at the height $r = 15.7\,\text{cm}$ (between the numbers $15$ and $20$, slightly above $15$).
**Formula:** $|q|vB = \dfrac{mv^2}{r}$, so $m = \dfrac{|q|Br}{v}$
**Conversions:** $r = 15.7\,\text{cm} = 0.157\,\text{m}$.
**Substitution:** $$\begin{aligned} &m \\ &= \dfrac{1.602 \cdot 10^{-19}\,\text{C} \cdot 0.20\,\text{T} \cdot 0.157\,\text{m}}{1.5 \cdot 10^{6}\,\text{m/s}} \\ &= 3.35 \cdot 10^{-27}\,\text{kg} \end{aligned}$$
**Answer:** $3.4 \cdot 10^{-27}\,\text{kg}$ (reading from the graph gives about two significant figures).
**Reasonableness:** The mass is about twice the mass of the proton, $1.673 \cdot 10^{-27}\,\text{kg}$, so the particle can be a deuteron, whose charge is the same as that of the proton.

## fy7-2-L2-10
**Given:** from the source material ([Finnish Meteorological Institute – Revontulet ja avaruussää](https://www.ilmatieteenlaitos.fi/revontulet-ja-avaruussaa) and its [guide](https://www.ilmatieteenlaitos.fi/avaruussaatiedotuksen-tulkintaohje), in Finnish, read 16 November 2026): the R number describes how fast the magnetic field varies, and it becomes a value in $\text{nT/s}$ when it is divided by $1350$; the meaning of the thresholds; the typical speed of the solar wind is $300$–$400\,\text{km/s}$.

The example data of the task (invented): the R number from 18 to 1 o'clock is $40$, $90$, $260$, $540$, $810$, $620$, $310$ and $120$, thresholds $200$ and $400$. In part b) $v = 4.0 \cdot 10^{5}\,\text{m/s}$, $B = 50\,\mu\text{T}$, $m = 1.673 \cdot 10^{-27}\,\text{kg}$, $|q| = 1.602 \cdot 10^{-19}\,\text{C}$ and the radius of the Earth $R_\text{E} = 6370\,\text{km}$
**Find:** a) the variation of the R number and the rate of change $\dfrac{\Delta B}{\Delta t}$ in $\text{nT/s}$ that corresponds to the largest R number;

b) how the northern lights form and the radius $r$ of the proton's circular path in metres;

c) what can be concluded from the R number;

d) why a disturbance does not guarantee that the northern lights are seen
**Principle:** The data are live, so your own numbers differ from these. The method is the same: read the R numbers and the thresholds from the chart and write down the time. This solution uses the example data of the task.

In part b) the proton moves perpendicular to the field, so the magnetic force $|q|vB$ is perpendicular to the velocity and acts as the centripetal force of circular motion. The field is assumed uniform over a region the size of the path.
**Part a):** In the example data the R number is small early in the evening ($40$ and $90$), so the field is quiet. At 20 o'clock the R number exceeds the lower threshold ($260 > 200$) and at 21 o'clock the upper one ($540 > 400$).

The field varies fastest at 22 o'clock, when the R number is $810$. After that the disturbance weakens: at 0 o'clock the R number is between the thresholds ($310$) and at 1 o'clock below the lower threshold ($120$).

So the lower threshold is exceeded in five consecutive hours (20 to 0 o'clock) and the upper one in three (21 to 23 o'clock).

A dated example from the page: the review published on the morning of 16 November 2026 said that space weather had been quiet at the weekend and that the solar wind would strengthen on Monday and Tuesday. In a quiet period the bars of the chart stay below the thresholds.
**Formula:** a) $\dfrac{\Delta B}{\Delta t} = \dfrac{R}{1350}\,\text{nT/s}$, where $R$ is the R number. b) $$\begin{aligned} \Sigma F &= ma_\text{n} \\ F_\text{m} &= m\dfrac{v^2}{r} \\ |q|vB &= m\dfrac{v^2}{r} \\ r &= \dfrac{mv}{|q|B} \end{aligned}$$
**Conversions:** $B = 50\,\mu\text{T} = 50 \cdot 10^{-6}\,\text{T}$. For the comparison $R_\text{E} = 6370\,\text{km} = 6.37 \cdot 10^{6}\,\text{m}$. Also $1\,\text{T} = 1\,\tfrac{\text{N}}{\text{C} \cdot \text{m/s}}$, so the result comes out in metres.
**Substitution:** a) $\dfrac{\Delta B}{\Delta t} = \dfrac{810}{1350}\,\text{nT/s} = 0.60\,\text{nT/s}$. b) $r = \dfrac{1.673 \cdot 10^{-27}\,\text{kg} \cdot 4.0 \cdot 10^{5}\,\text{m/s}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 50 \cdot 10^{-6}\,\text{T}} = 83.55\,\text{m} \approx 84\,\text{m}$
**Part b):** According to the source material the solar wind is a stream of particles that spreads from the Sun into space and produces the northern lights. Its particles are charged, mainly protons and electrons. The magnetic force is perpendicular to both the velocity and the field.

So the motion perpendicular to the field turns into a circle, whose radius is by the calculation only about $84\,\text{m}$. That is negligible compared with the radius of the Earth, $6370\,\text{km}$.

The force does not affect the motion along the field, because $\sin 0^\circ = 0$. So the particle cannot cross the field lines: it circles a field line and moves along it on a helical path.

The Earth's field lines dip steeply towards the ground near the magnetic poles (chapter *Magnets, the magnetic dipole and the magnetic field*). That is why the particles reach the upper atmosphere on a ring around the poles, which the source material calls the auroral zone.

There they collide with the atoms and molecules of the air, which gain energy in the collision and give it out as light.

The magnetic field only guides the particles: the magnetic force does no work and does not change the speed. A refinement of this solution, not of the source material: the model is a simplification.

The solar wind does not come straight into the atmosphere; it disturbs the Earth's magnetosphere, from which particles rush along the field lines into the upper atmosphere. The guiding principle is the same.
**Part c):** The R number is a measurement of the magnetic field, not of the northern lights. Moving charged particles are an electric current, and an electric current produces a magnetic field around it (chapter *Magnetic field of a wire and a coil*).

When the particle currents of the upper atmosphere change, the field at the ground varies, and the same particles produce northern lights. According to the guide the lower threshold corresponds to a probability of about $50\,\%$ for slight, faint northern lights and the upper one to a probability of about $50\,\%$ for bright or extensive northern lights.

The connection is statistical: the R number is never a sure sign of northern lights, and a short exceedance can occur without them. Several exceedances in a row are a better sign.

In the example data the upper threshold is exceeded in three consecutive hours, so from 21 to 23 o'clock northern lights are likely near the station, bright ones too.

They are not certain. The R number does not tell where in the sky the northern lights are or whether they can be seen. Nor is it a forecast, because it describes a variation already measured. The thresholds are specific to each station, so the conclusion concerns only the surroundings of this station.
**Part d):** The claim "a strong disturbance guarantees northern lights" is a conclusion that goes too far from the data.

The connection between the disturbance and the northern lights is real, but there are several reasons why they are still not seen. 1) The connection is statistical: the upper threshold corresponds to a probability of about $50\,\%$ for bright northern lights, so in part of the exceedances there are none. 2) Clouds: according to the source material the probability estimate does not take into account cloudiness, which can prevent seeing them.

The northern lights form in the upper atmosphere above the clouds. 3) Light: the northern lights are seen only when it is dark. In the daytime and on a summer night the sky is too bright, however strong the disturbance. 4) Place: according to the source material the probability grows towards the north, and Lapland belongs to the auroral zone.

In the south the northern lights can stay low in the northern sky or behind the horizon. The disturbance was also measured at a station that can be far from the observation site. An addition of this solution: city lights can also hide faint northern lights.
**Answer:** $84\,\text{m}$ is the radius of the proton's circular path, two significant figures like the speed $4.0 \cdot 10^{5}\,\text{m/s}$ and the field $50\,\mu\text{T}$.

The largest R number of the example data, $810$, corresponds to a rate of change of $0.60\,\text{nT/s}$. With your own data the numbers of parts a) and c) differ, and they are assessed in the same way.
**Reasonableness:** An estimate with round numbers: $mv \approx 7 \cdot 10^{-22}\,\text{kg} \cdot \text{m/s}$ and $|q|B \approx 8 \cdot 10^{-24}\,\text{C} \cdot \text{T}$, so $r \approx 90\,\text{m}$. The order of magnitude is right. The radius is only about a hundred-thousandth of the radius of the Earth: $\tfrac{r}{R_\text{E}} \approx 1.3 \cdot 10^{-5}$.

Higher up the field is weaker and the radius larger, but even in a field a hundred times weaker the radius would be only about $8.4\,\text{km}$.

At the rate of change $0.60\,\text{nT/s}$ the field changes in a minute by at most $0.60\,\text{nT/s} \cdot 60\,\text{s} = 36\,\text{nT}$. That is less than $0.1\,\%$ of the Earth's field $50\,\mu\text{T} = 50\,000\,\text{nT}$. So the disturbance is a small ripple on top of a large field, and measuring it takes a sensitive magnetometer.
