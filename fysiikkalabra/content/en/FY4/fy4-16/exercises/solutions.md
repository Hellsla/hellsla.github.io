## fy4-16-L1-01
**Given:** $m = 70.0\,\text{kg}$, acceleration of the lift $a = 0.80\,\text{m/s}^2$ upwards; $g = 9.81\,\text{m/s}^2$
**Find:** the normal force $N$ of the floor in $\text{N}$
**Principle:** The person stands still in the lift, so the person accelerates with the lift. By Newton's second law the acceleration is determined by the net force, so in a lift accelerating upwards the normal force must be larger than the weight.
**Free-body diagram:** The person as a rectangle, positive direction up. The weight $\overline{G}$ from the centre down and the normal force $\overline{N}$ of the floor from the bottom surface up, longer than the weight. The acceleration up is marked separately and not as a force.
```voimakuvio
pinta 0
G 686,7
N 742,7 työntö
a ylös
```
**Formula:** $N - mg = ma$, so $N = m(g + a)$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $N = 70.0\,\text{kg}\cdot(9.81 + 0.80)\,\text{m/s}^2 = 70.0\,\text{kg}\cdot 10.61\,\text{m/s}^2 = 742.7\,\text{N}$
**Answer:** $743\,\text{N}$ upwards, three significant figures like the mass $70.0\,\text{kg}$.
**Reasonableness:** The weight is $70.0\,\text{kg}\cdot 9.81\,\text{m/s}^2 \approx 687\,\text{N}$, and the normal force is $ma = 56\,\text{N}$ larger, about $8\,\%$. The acceleration is about $8\,\%$ of the acceleration of free fall, so the proportion matches.

## fy4-16-L1-02
**Given:** $m = 90.0\,\text{kg}$, air resistance $F_\text{d} = 2.10\,\text{kN}$, the skydiver moves down; $g = 9.81\,\text{m/s}^2$
**Find:** the net force $\Sigma F$ in $\text{kN}$ and its direction
**Principle:** The Earth (the weight) and the air (air resistance) act on the skydiver. The net force is the vector sum of the forces. The skydiver moves down, so the air resistance points up, against the weight.
**Free-body diagram:** The skydiver with the parachute as a rectangle, positive direction up. The weight $\overline{G}$ from the centre down and the air resistance $\overline{F}_\text{d}$ from the top surface up, more than twice as long as the weight.
```voimakuvio
G 882,9
F_v 2100 ylös
a ylös
```
**Formula:** $\Sigma F = F_\text{d} - G$, and $G = mg$, so $\Sigma F = F_\text{d} - mg$
**Conversions:** $2.10\,\text{kN} = 2.10\cdot 1000\,\text{N} = 2100\,\text{N}$; the result is changed back into kilonewtons at the end.
**Substitution:** $\Sigma F = 2100\,\text{N} - 90.0\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 2100\,\text{N} - 882.9\,\text{N} = 1217.1\,\text{N} \approx 1.22\,\text{kN}$
**Answer:** $1.22\,\text{kN}$ upwards, three significant figures like the mass $90.0\,\text{kg}$ and the air resistance $2.10\,\text{kN}$.
**Reasonableness:** The air resistance is about $2.4$ times the weight $883\,\text{N}$, so about $1.4$ weights are left upwards, about $1.2\,\text{kN}$. The net force points up although the skydiver moves down, so the skydiver slows down.

## fy4-16-L1-03
**Given:** height difference $h = 3.20\,\text{m}$, initial speed $v_1 = 0$, friction and air resistance are ignored; $g = 9.81\,\text{m/s}^2$
**Find:** the speed $v_2$ at the end of the chute in $\text{m/s}$
**Free-body diagram:** The child as a rectangle, tilted along the surface of the chute. The weight $\overline{G}$ from the centre straight down and the normal force $\overline{N}$ of the chute from the bottom surface perpendicularly out of the surface. There is no friction and no force in the direction of the motion. The velocity is marked separately and not as a force.
```voimakuvio
pinta -30
G 300
N 259,8
a alas
v alas
```
**Principle:** The weight and the normal force of the chute act on the child. The normal force is perpendicular to the motion and does no work, and friction is ignored, so the mechanical energy is conserved. The shape of the chute does not matter, only the height difference.
**Formula:** Zero level at the end of the chute: $mgh = \tfrac12 mv_2^2$, so $v_2 = \sqrt{2gh}$
**Conversions:** The quantities are in SI units, so no conversions are needed. The mass is not needed, because it cancels.
**Substitution:** $v_2 = \sqrt{2\cdot 9.81\,\text{m/s}^2\cdot 3.20\,\text{m}} = \sqrt{62.78\,\text{m}^2/\text{s}^2} = 7.924\,\text{m/s}$
**Answer:** $7.92\,\text{m/s}$, three significant figures like the height $3.20\,\text{m}$.
**Reasonableness:** $7.9\,\text{m/s}$ is about $29\,\text{km/h}$, which suits an icy chute. In reality friction and air resistance reduce the speed a little, so the result is an upper limit.

## fy4-16-L1-04
**Given:** initial speed $v_1 = 6.0\,\text{m/s}$, final speed $v_2 = 0$, $\mu = 0.080$; $g = 9.81\,\text{m/s}^2$
**Find:** the sliding distance $s$ in $\text{m}$
**Principle:** The question is about the distance over which the kinetic energy is used up, so we use the work–energy principle. The height does not change, and friction is the only force doing work: its negative work turns the kinetic energy into internal energy. The friction force comes from the free-body diagram.
**Free-body diagram:** The sled as a rectangle. The weight $\overline{G}$ from the centre down, the normal force $\overline{N}$ of the snow from the bottom surface up, equally long, and the kinetic friction $\overline{F}_\mu$ from the rear corner of the bottom surface backwards. There is no force pointing forwards. In the vertical direction $N - mg = 0$, so $F_\mu = \mu mg$.
```voimakuvio
pinta 0
G 100
N 100
F_mu 8 vasen
a vasen
```
**Formula:** $\tfrac12 mv_1^2 - \mu mg s = 0$, so $s = \dfrac{v_1^2}{2\mu g}$
**Conversions:** The quantities are in SI units, so no conversions are needed. The mass cancels.
**Substitution:** $s = \dfrac{(6.0\,\text{m/s})^2}{2\cdot 0.080\cdot 9.81\,\text{m/s}^2} = \dfrac{36\,\text{m}^2/\text{s}^2}{1.5696\,\text{m/s}^2} = 22.94\,\text{m}$
**Answer:** $23\,\text{m}$, two significant figures like the speed $6.0\,\text{m/s}$ and the coefficient of friction $0.080$.
**Reasonableness:** The deceleration is $\mu g \approx 0.8\,\text{m/s}^2$, so stopping takes about $6\,\text{s} : 0.8 \approx 7.5\,\text{s}$, and at the average speed $3\,\text{m/s}$ the distance is about $23\,\text{m}$. On the flat of a sledding hill this is a usual sliding distance.

## fy4-16-L1-05
**Given:** $\mu = 0.15$, the speed is constant, air resistance is ignored
**Find:** the angle of inclination $\alpha$ of the slope in degrees
**Principle:** The speed is constant, so by Newton's second law the net force is zero both along the slope and perpendicular to it. The component of the weight along the slope and the kinetic friction cancel each other.
**Free-body diagram:** The sled as a rectangle along the slope, $x$ down the slope and $y$ perpendicularly out of the slope. The weight $\overline{G}$ from the centre straight down, the normal force $\overline{N}$ from the bottom surface perpendicularly out of the slope and the kinetic friction $\overline{F}_\mu$ from the upper corner of the bottom surface up the slope. The components of the weight as dashed lines.
```voimakuvio
pinta -8,53
G 100
N 98,89
F_mu 14,83 ylös
a 0
akselit -8,53
komponentit G
```
**Formula:** $y$: $N - mg\cos\alpha = 0$; $x$: $mg\sin\alpha - \mu N = 0$, so $mg\sin\alpha = \mu mg\cos\alpha$, $\tan\alpha = \mu$ and $\alpha = \tan^{-1}\mu$
**Conversions:** The coefficient of friction has no unit, and the angle comes in degrees with the calculator in degree mode, so no conversions are needed.
**Substitution:** $\alpha = \tan^{-1} 0.15 = 8.531^\circ$
**Answer:** $8.5^\circ$, two significant figures like the coefficient of friction $0.15$.
**Reasonableness:** For small angles $\tan\alpha \approx \alpha$ in radians, and $0.15\,\text{rad} \approx 8.6^\circ$. The angle is gentle, which fits: on a steeper slope the sled would accelerate, on a gentler one it would slow down. The mass cancelled.

## fy4-16-L2-01
**Given:** $m = 60.0\,\text{kg}$, reading of the scale $\tfrac{N}{g} = 66.5\,\text{kg}$; $g = 9.81\,\text{m/s}^2$
**Find:** the acceleration $a$ of the lift in $\text{m/s}^2$ and its direction
**Principle:** A scale measures the normal force. The reading is larger than the mass, so the normal force is larger than the weight, the net force points up and by Newton's second law the acceleration also points up.
**Free-body diagram:** The student as a rectangle, positive direction up. The weight $\overline{G}$ from the centre down and the normal force $\overline{N}$ from the bottom surface up, longer than the weight.
```voimakuvio
pinta 0
G 588,6
N 652,4 työntö
a ylös
```
**Formula:** $N - mg = ma$, so $a = \dfrac{N - mg}{m}$. When the reading is $L = \tfrac{N}{g}$, $N = Lg$ and $a = g\left(\dfrac{L}{m} - 1\right)$
**Conversions:** The reading is changed into the normal force by multiplying by $g$: $N = 66.5\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 652.4\,\text{N}$.
**Substitution:** $a = 9.81\,\text{m/s}^2\cdot\left(\dfrac{66.5\,\text{kg}}{60.0\,\text{kg}} - 1\right) = 9.81\,\text{m/s}^2\cdot 0.10833 = 1.063\,\text{m/s}^2$
**Answer:** $1.06\,\text{m/s}^2$ upwards, three significant figures like the mass $60.0\,\text{kg}$ and the reading $66.5\,\text{kg}$.
**Reasonableness:** The reading is about $11\,\%$ larger than the mass, so the acceleration is about $11\,\%$ of the acceleration of free fall, about $1\,\text{m/s}^2$. The lift either starts up or slows down while moving down: both give an acceleration pointing up.

## fy4-16-L2-02
**Given:** $L = 18.0\,\text{m}$, $\alpha = 12.0^\circ$, $v_1 = 0$, $v_2 = 5.10\,\text{m/s}$; $g = 9.81\,\text{m/s}^2$
**Find:** the coefficient of kinetic friction $\mu$ (no unit)
**Principle:** The speed is known at the start and at the end of the slope, so we use the work–energy principle. The weight does work through the potential energy, the normal force does no work, and kinetic friction does negative work along the whole slope. The friction force comes from the free-body diagram.
**Free-body diagram:** The sled as a rectangle along the slope, $x$ down the slope and $y$ perpendicularly out of the slope. The weight $\overline{G}$ from the centre straight down, the normal force $\overline{N}$ from the bottom surface perpendicularly out of the slope and the kinetic friction $\overline{F}_\mu$ from the upper corner of the bottom surface up the slope. In the $y$ direction $N = mg\cos\alpha$, so $F_\mu = \mu mg\cos\alpha$.
```voimakuvio
pinta -12
G 100
N 97,81
F_mu 13,43 ylös
a alas
akselit -12
komponentit G
```
**Formula:** Zero level at the foot: $mgL\sin\alpha - \mu mg\cos\alpha\cdot L = \tfrac12 mv_2^2$, so $\mu = \dfrac{gL\sin\alpha - \tfrac12 v_2^2}{gL\cos\alpha}$
**Conversions:** The quantities are in SI units, so no conversions are needed. The mass cancels.
**Substitution:** The numerator is $9.81\cdot 18.0\cdot\sin 12.0^\circ\,\tfrac{\text{m}^2}{\text{s}^2} - \tfrac12\cdot 5.10^2\,\tfrac{\text{m}^2}{\text{s}^2} = 36.71\,\tfrac{\text{m}^2}{\text{s}^2} - 13.01\,\tfrac{\text{m}^2}{\text{s}^2} = 23.71\,\tfrac{\text{m}^2}{\text{s}^2}$ and the denominator $9.81\cdot 18.0\cdot\cos 12.0^\circ\,\tfrac{\text{m}^2}{\text{s}^2} = 172.72\,\tfrac{\text{m}^2}{\text{s}^2}$, so $\mu = \dfrac{23.71}{172.72} = 0.1373$
**Answer:** $0.137$, three significant figures like the length of the slope $18.0\,\text{m}$, the angle $12.0^\circ$ and the speed $5.10\,\text{m/s}$.
**Reasonableness:** Without friction the speed would be $\sqrt{2\cdot 9.81\cdot 3.74}\,\text{m/s} \approx 8.6\,\text{m/s}$ from the drop height $h = 18.0\,\text{m}\cdot\sin 12.0^\circ \approx 3.74\,\text{m}$, so friction takes about two thirds of the energy. The coefficient is smaller than $\tan 12.0^\circ \approx 0.21$, as it should be, because the sled accelerates.

## fy4-16-L2-03
**Given:** $m = 80.0\,\text{kg}$, $v_1 = 52.0\,\text{m/s}$, $v_2 = 6.0\,\text{m/s}$, drop $h = 145\,\text{m}$; $g = 9.81\,\text{m/s}^2$
**Find:** the mechanical energy changed into other forms of energy $|\Delta E_\text{mech}|$ in $\text{kJ}$
**Free-body diagram:** The skydiver with the parachute as a rectangle, positive direction down. The weight $\overline{G}$ from the centre down and the air resistance $\overline{F}_\text{d}$ from the top surface up. The velocity down is marked separately and not as a force. The air resistance is against the motion, so the work it does is negative.
```voimakuvio
G 784,8
F_v 1520,8 ylös
a ylös
v alas
```
**Principle:** By the work–energy principle the change in mechanical energy is the work done by forces other than the weight, here the negative work done by air resistance. Both the kinetic energy and the potential energy decrease, and the change in both is counted.
**Formula:** Zero level at the height of the final situation: $\Delta E_\text{mech} = \left(\tfrac12 mv_2^2 - \tfrac12 mv_1^2\right) - mgh$, and $|\Delta E_\text{mech}| = \dfrac{m\left(v_1^2 - v_2^2\right)}{2} + mgh$
**Conversions:** We calculate in joules and finally change to kilojoules: $1\,\text{kJ} = 1000\,\text{J}$.
**Substitution:** $|\Delta E_\text{mech}| = \tfrac12\cdot 80.0\,\text{kg}\cdot\left(52.0^2 - 6.0^2\right)\,\text{m}^2/\text{s}^2 + 80.0\,\text{kg}\cdot 9.81\,\text{m/s}^2\cdot 145\,\text{m} = 106\,720\,\text{J} + 113\,796\,\text{J} = 220\,516\,\text{J} \approx 221\,\text{kJ}$
**Answer:** $221\,\text{kJ}$, three significant figures like the mass $80.0\,\text{kg}$ and the speed $52.0\,\text{m/s}$.
**Reasonableness:** Each part is about $110\,\text{kJ}$: the kinetic energy decreases almost completely ($\tfrac12\cdot 80\cdot 52^2\,\text{J} \approx 108\,\text{kJ}$), and the potential energy decreases by $mgh \approx 800\,\text{N}\cdot 145\,\text{m} \approx 116\,\text{kJ}$. The energy does not disappear but turns into motion of the air and finally into internal energy.

## fy4-16-L2-04
**Given:** $m = 850\,\text{kg}$, lifting height $h = 12.0\,\text{m}$, time $t = 15.0\,\text{s}$, the speed is constant; $g = 9.81\,\text{m/s}^2$
**Find:** the power $P$ of the cable in $\text{kW}$
**Principle:** The speed is constant, so by Newton's second law the tension of the cable is equal to the weight. The cable pulls in the direction of the motion, so it does positive work $W = Th$, which increases the potential energy of the car. Power is work divided by time, as in the chapter *Hydro and wind power as energy converters*, $E = Pt$.
**Free-body diagram:** The lift car with its load as a rectangle, positive direction up. The weight $\overline{G}$ from the centre down and the tension $\overline{T}$ of the cable from the top surface up, equally long. The velocity up is marked separately and not as a force.
```voimakuvio
G 8338,5
T 8338,5 90
a 0
v ylös
```
**Formula:** $T - mg = 0$, so $T = mg$. The work is $W = Th = mgh$, and the power $P = \dfrac{W}{t} = \dfrac{mgh}{t}$
**Conversions:** We calculate in watts and finally change to kilowatts: $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P = \dfrac{850\,\text{kg}\cdot 9.81\,\text{m/s}^2\cdot 12.0\,\text{m}}{15.0\,\text{s}} = \dfrac{100\,062\,\text{J}}{15.0\,\text{s}} = 6670.8\,\text{W} \approx 6.67\,\text{kW}$
**Answer:** $6.67\,\text{kW}$, three significant figures like the height $12.0\,\text{m}$ and the time $15.0\,\text{s}$.
**Reasonableness:** The speed is $12.0\,\text{m} : 15.0\,\text{s} = 0.80\,\text{m/s}$, and the tension is about $8.3\,\text{kN}$. The product $8.3\,\text{kN}\cdot 0.80\,\text{m/s} \approx 6.7\,\text{kW}$ matches. The power of a lift motor is typically a few kilowatts, and because of losses the motor needs more.

## fy4-16-L3-01
**Given:** height difference $h = 4.50\,\text{m}$, $\mu = 0.120$ all the way, parts of the slope $25^\circ$ and $10^\circ$, $v_1 = 0$ and at the end $v_2 = 0$
**Find:** the horizontal distance $x$ from the top to the stopping point in $\text{m}$
**Principle:** The sled is at rest at the start and at the end, so by the work–energy principle the negative work done by friction is equal to the decrease in potential energy. On a straight surface the work done by friction is $-\mu mg$ times the horizontal distance, because on a slope $N = mg\cos\alpha$ and $L\cos\alpha$ is the horizontal length of the slope. So the angles of the parts of the slope are not needed.
**Free-body diagram:** On each part of the slope the sled as a rectangle along the slope: the weight $\overline{G}$ from the centre down, the normal force $\overline{N}$ perpendicularly out of the slope, $N = mg\cos\alpha$, and the kinetic friction $\overline{F}_\mu$ up the slope. On the flat $N = mg$ and the friction points backwards. The normal force does no work anywhere.
```voimakuvio
pinta -25
G 100
N 90,63
F_mu 10,88 ylös
a alas
---
pinta 0
G 100
N 100
F_mu 12 vasen
a vasen
```
**Formula:** Horizontal distances of the parts $x_\text{a}$, $x_\text{b}$ and $x_\text{c}$: $mgh - \mu mg(x_\text{a} + x_\text{b} + x_\text{c}) = 0$, so $x = x_\text{a} + x_\text{b} + x_\text{c} = \dfrac{h}{\mu}$
**Conversions:** The quantities are in SI units and the coefficient of friction has no unit, so no conversions are needed.
**Substitution:** $x = \dfrac{4.50\,\text{m}}{0.120} = 37.5\,\text{m}$
**Answer:** $37.5\,\text{m}$, three significant figures like the height $4.50\,\text{m}$ and the coefficient of friction $0.120$.
**Reasonableness:** The inclination of both parts of the slope is greater than $\tan^{-1} 0.120 \approx 6.8^\circ$, so the sled slides down the whole slope and does not stop halfway. The result does not depend on the mass or on the shape of the slope. A smaller friction would give a longer distance, as it should. In reality the normal force and the friction grow for a moment in the bends, so the sled would stop a little earlier.

## fy4-16-L3-02
**Given:** $m = 75.0\,\text{kg}$; from the graph the normal force $N = 650\,\text{N}$ from $1.0\,\text{s}$ to $3.0\,\text{s}$; the lift starts from rest; $g = 9.81\,\text{m/s}^2$
**Find:** the greatest speed $v$ of the lift in $\text{m/s}$
**Principle:** The lift accelerates downwards when the normal force is smaller than the weight, and the speed is greatest at the end of this phase. By Newton's second law the acceleration comes from the forces. When the forces are constant, the acceleration is constant, and by the chapter *Acceleration and uniformly accelerated motion* $v = v_0 + at$.
**Free-body diagram:** The person as a rectangle, positive direction down. The weight $\overline{G}$ from the centre down and the normal force $\overline{N}$ from the bottom surface up, shorter than the weight.
```voimakuvio
pinta 0
G 735,8
N 650 työntö
a alas
```
**Reading the graph:** The weight is $75.0\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 735.75\,\text{N}$, and the reading is that large at rest and at a steady speed. From $1.0\,\text{s}$ to $3.0\,\text{s}$ the curve is on the grid line at $650\,\text{N}$, smaller than the weight, so the lift accelerates downwards for $\Delta t = 2.0\,\text{s}$. From $6.0\,\text{s}$ on the reading is larger than the weight, so the lift slows down.
**Formula:** $mg - N = ma$, so $a = g - \dfrac{N}{m}$, and starting from rest $v = a\Delta t = \left(g - \dfrac{N}{m}\right)\Delta t$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $v = \left(9.81\,\text{m/s}^2 - \dfrac{650\,\text{N}}{75.0\,\text{kg}}\right)\cdot 2.0\,\text{s} = 1.1433\,\text{m/s}^2\cdot 2.0\,\text{s} = 2.287\,\text{m/s}$
**Answer:** $2.3\,\text{m/s}$ downwards, two significant figures like the time $2.0\,\text{s}$ read from the graph.
**Reasonableness:** In the slowing phase the reading is $800\,\text{N}$, so the deceleration is $(800 - 735.75)\,\text{N} : 75.0\,\text{kg} \approx 0.86\,\text{m/s}^2$, and the speed $2.3\,\text{m/s}$ disappears in about $2.7\,\text{s}$, which matches the slowing phase of the graph from about $6.0\,\text{s}$ to $8.7\,\text{s}$. The speed of an ordinary lift is $1$–$3\,\text{m/s}$.

## fy4-16-L3-03
**Given:** $m = 70.0\,\text{kg}$, $v_1 = 50.0\,\text{m/s}$, $v_2 = 6.0\,\text{m/s}$, drop $h = 60.0\,\text{m}$, air resistance assumed constant; $g = 9.81\,\text{m/s}^2$
**Find:** the magnitude of the air resistance $F_\text{d}$ in $\text{kN}$
**Principle:** The speeds are known at the start and at the end of the distance, so we use the work–energy principle. Air resistance is the only force other than the weight, and it points against the motion, so the work it does is $W_\text{d} = -F_\text{d} h$. The work comes from the work–energy principle, and the force from the work.
**Free-body diagram:** The skydiver with the parachute as a rectangle. The weight $\overline{G}$ from the centre down and the air resistance $\overline{F}_\text{d}$ from the top surface up, much longer than the weight, because the skydiver slows down. The velocity down is marked separately and not as a force.
```voimakuvio
G 686,7
F_v 2124 ylös
a ylös
v alas
```
**Formula:** The kinetic energies are $E_{\text{k},1} = \tfrac12 mv_1^2$ and $E_{\text{k},2} = \tfrac12 mv_2^2$. Zero level at the height of the final situation: $E_{\text{k},1} + mgh - F_\text{d} h = E_{\text{k},2}$, so $F_\text{d} = mg + \dfrac{E_{\text{k},1} - E_{\text{k},2}}{h}$
**Conversions:** We calculate in newtons and finally change to kilonewtons: $1\,\text{kN} = 1000\,\text{N}$.
**Substitution:** $E_{\text{k},1} = \tfrac12\cdot 70.0\,\text{kg}\cdot(50.0\,\text{m/s})^2 = 87\,500\,\text{J}$ and $E_{\text{k},2} = \tfrac12\cdot 70.0\,\text{kg}\cdot(6.0\,\text{m/s})^2 = 1260\,\text{J}$, so $F_\text{d} = 70.0\,\text{kg}\cdot 9.81\,\text{m/s}^2 + \dfrac{87\,500\,\text{J} - 1260\,\text{J}}{60.0\,\text{m}} = 686.7\,\text{N} + 1437.3\,\text{N} = 2124\,\text{N} \approx 2.12\,\text{kN}$
**Answer:** $2.12\,\text{kN}$ upwards, three significant figures like the mass $70.0\,\text{kg}$, the speed $50.0\,\text{m/s}$ and the distance $60.0\,\text{m}$.
**Reasonableness:** The air resistance is about three times the weight $687\,\text{N}$, so the net force points up and the skydiver slows down, as it should. From the equation of motion the deceleration is $(2124 - 687)\,\text{N} : 70.0\,\text{kg} \approx 20\,\text{m/s}^2$, and then $\tfrac12(v_1^2 - v_2^2) : a \approx 1232 : 20.5 \approx 60\,\text{m}$, as in the problem.

## fy4-16-L1-06
**Find:** how the reading of the scale compares with the reading when a lift moving upwards slows down to stop.
**Principle:** The scale measures the normal force $N$. By Newton's second law the normal force and the weight determine the acceleration, not the direction of motion. A lift moving up and slowing down accelerates downwards, so the net force points down.
**Model answer:** The reading of the scale is smaller than at rest. When the positive direction is down, $mg - N = ma$, so $N = m(g - a)$ is smaller than the weight $mg$. The claim that the reading would be larger because the lift moves up confuses velocity and acceleration: only the acceleration affects the reading. The claim that the reading would be the same because the mass does not change ignores that the scale measures the normal force, not the mass. The reading is not zero, because the deceleration of the lift is much smaller than $g$.

## fy4-16-L1-07
**Find:** which statement about the mechanical energy of the skydiver is correct when he descends at a steady speed.
**Principle:** Mechanical energy is the sum of kinetic energy and potential energy. By the work–energy principle its change is the work done by forces other than the weight, here the work of the air resistance. The air resistance points against the motion, so its work is negative.
**Model answer:** The mechanical energy decreases. The speed does not change, so the kinetic energy stays the same, but the height decreases and the potential energy decreases. The air resistance does negative work, and it turns the mechanical energy into internal energy. The claim that the mechanical energy is conserved because the speed does not change takes only the kinetic energy into account. The claim that it is conserved because the weight and the air resistance cancel each other confuses the net force and the energy: the sum of the forces is zero, so the kinetic energy does not change, but the work of the air resistance is not zero. The mechanical energy does not increase, because the work of the weight only changes the potential energy and the air resistance takes away the same amount.

## fy4-16-L1-08
**Given:** $m = 20.0\,\text{kg}$, $\alpha = 30.0\,{}^\circ$, $\mu = 0.200$, the sled slides down the slope; the student's result $39.2\,\text{N}$; $g = 9.81\,\text{m/s}^2$
**Find:** the student's error and the correct kinetic friction force $F_\mu$ in $\text{N}$
**Principle:** Kinetic friction is $F_\mu = \mu N$, and the normal force $N$ comes from the free-body diagram perpendicular to the slope. The sled does not accelerate in this direction, so the normal force cancels only the component of the weight perpendicular to the slope. The student assumed that the normal force cancels the whole weight, which holds only on a horizontal surface.
**Free-body diagram:** The sled as a rectangle along the slope, $x$ down the slope and $y$ perpendicularly out of the slope. The weight $\overline{G}$ from the centre straight down, the normal force $\overline{N}$ from the bottom surface perpendicularly out of the slope, shorter than the weight, and the kinetic friction $\overline{F}_\mu$ from the upper corner of the bottom surface up the slope. The components of the weight as dashed lines.
```voimakuvio
pinta -30
G 196,2
N 169,9
F_mu 33,98 ylös
a alas
akselit -30
komponentit G
```
**Formula:** $y$: $N - mg\cos\alpha = 0$, so $N = mg\cos\alpha$ and $F_\mu = \mu N = \mu mg\cos\alpha$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $N = 20.0\,\text{kg}\cdot 9.81\,\text{m/s}^2\cdot\cos 30.0\,{}^\circ = 169.9\,\text{N}$, so $F_\mu = 0.200\cdot 169.9\,\text{N} = 33.98\,\text{N}$
**Answer:** $34.0\,\text{N}$ up the slope. The student's error was to write $N = mg$ on a slope; the correct one is $N = mg\cos\alpha$. Three significant figures like the mass $20.0\,\text{kg}$ and the angle $30.0\,{}^\circ$.
**Reasonableness:** On a slope the normal force is smaller than the weight $196.2\,\text{N}$, because the component of the weight along the slope does not press against the surface. The student's result $39.2\,\text{N}$ is too large by the factor $1 : \cos 30.0\,{}^\circ \approx 1.15$, and $34.0\,\text{N}\cdot 1.155 \approx 39.2\,\text{N}$. The component of the weight along the slope is $mg\sin\alpha = 98.1\,\text{N}$, so the sled accelerates down, as it should.

## fy4-16-L2-05
**Given:** $m = 62.0\,\text{kg}$; from the table $v = 0$ at $t = 0$ and $v = 1.20\,\text{m/s}$ at $t = 3.0\,\text{s}$; $g = 9.81\,\text{m/s}^2$
**Find:** the acceleration $a$ of the lift and the normal force $N$ of the floor in $\text{N}$
**Principle:** Acceleration is the change of speed divided by time, that is, the slope of the $(t,v)$ graph. The person accelerates with the lift, so by Newton's second law the difference of the normal force and the weight gives the acceleration.
**Reading the graph:** In the table the speed increases steadily: over each $0.5\,\text{s}$ interval by about $0.2\,\text{m/s}$, so the acceleration is almost constant and it is obtained from the first and the last row. The points are far apart, so the error of a single measurement has little effect.
**Free-body diagram:** The person as a rectangle, positive direction up. The weight $\overline{G}$ from the centre down and the normal force $\overline{N}$ of the floor from below up to the bottom surface, longer than the weight. The acceleration up is marked separately and not as a force.
```voimakuvio
pinta 0
G 608,2
N 633 työntö
a ylös
```
**Formula:** $a = \dfrac{v_2 - v_1}{t_2 - t_1}$ and $N - mg = ma$, so $N = m(g + a)$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{1.20\,\text{m/s} - 0}{3.0\,\text{s} - 0} = 0.400\,\text{m/s}^2$ and $N = 62.0\,\text{kg}\cdot(9.81 + 0.400)\,\text{m/s}^2 = 62.0\,\text{kg}\cdot 10.21\,\text{m/s}^2 = 633.0\,\text{N}$
**Answer:** $633\,\text{N}$ upwards, three significant figures like the mass $62.0\,\text{kg}$.
**Reasonableness:** The weight is $62.0\,\text{kg}\cdot 9.81\,\text{m/s}^2 \approx 608\,\text{N}$, and the normal force is $ma \approx 25\,\text{N}$ larger than that, about $4\,\%$. The acceleration is about $4\,\%$ of the free-fall acceleration, so the share matches. From the middle of the table, the points $t = 1.0\,\text{s}$ and $t = 2.0\,\text{s}$, we get $a = 0.38\,\text{m/s}^2$, so the acceleration is almost the same all the time.

## fy4-16-L2-06
**Given:** from the table the positions $x$ at $t = 0$, $1.0\,\text{s}$, $4.0\,\text{s}$ and $5.0\,\text{s}$; horizontal surface, air resistance is ignored; $g = 9.81\,\text{m/s}^2$
**Find:** the coefficient of kinetic friction $\mu$ (no unit)
**Principle:** The average speed over a time interval is the displacement divided by the time. In uniformly decelerating motion it is equal to the speed in the middle of the interval, so the deceleration follows from the average speeds of two intervals. On a horizontal surface friction is the only horizontal force, so Newton's second law gives the coefficient of friction.
**Reading the graph:** During the first second the sled travels $3.62\,\text{m} - 0 = 3.62\,\text{m}$, so the average speed is $3.62\,\text{m/s}$ and it is the speed at $t = 0.5\,\text{s}$. During the last second the sled travels $10.03\,\text{m} - 9.57\,\text{m} = 0.46\,\text{m}$, so the average speed is $0.46\,\text{m/s}$ at $t = 4.5\,\text{s}$.
**Free-body diagram:** The sled as a rectangle. The weight $\overline{G}$ from the centre down, the normal force $\overline{N}$ from the bottom surface up, equally long, and the kinetic friction $\overline{F}_\mu$ from the rear corner of the bottom surface backwards. There is no force pointing forwards. In the vertical direction $N = mg$, and in the horizontal direction, when the positive direction is the direction of motion, $-\mu mg = ma$.
```voimakuvio
pinta 0
G 100
N 100
F_mu 8,05 vasen
a vasen
```
**Formula:** The deceleration is $\left|a\right| = \dfrac{v_1 - v_2}{t_2 - t_1}$, and $\mu mg = m\left|a\right|$, so $\mu = \dfrac{\left|a\right|}{g}$
**Conversions:** The quantities are in SI units, so no conversions are needed. The mass cancels.
**Substitution:** $\left|a\right| = \dfrac{3.62\,\text{m/s} - 0.46\,\text{m/s}}{4.5\,\text{s} - 0.5\,\text{s}} = 0.790\,\text{m/s}^2$ and $\mu = \dfrac{0.790\,\text{m/s}^2}{9.81\,\text{m/s}^2} = 0.0805$
**Answer:** $0.081$, two significant figures like the distance $0.46\,\text{m}$ of the last second.
**Reasonableness:** The average speeds over the other intervals are $2.76\,\text{m/s}$, $2.05\,\text{m/s}$ and $1.14\,\text{m/s}$, and they decrease by about $0.8\,\text{m/s}$ per second, so the deceleration is almost constant, as it should be in motion caused by friction. The coefficient $0.08$ is small, as it should be for a sled sliding on snow, and it is smaller than $1$.

## fy4-16-L2-07
**Given:** five angles $17.5\,{}^\circ$, $18.0\,{}^\circ$, $18.5\,{}^\circ$, $17.0\,{}^\circ$ and $18.0\,{}^\circ$; the pushed box slides at a steady speed
**Find:** a) the coefficient of kinetic friction $\mu$ from the mean of the angles; b) the range of the coefficient and the variation around the mean
**Principle:** The box is given a push. If the box were at rest, the angle would depend on static friction. When the pushed box slides at a steady speed, the net force is zero. The component of the weight along the slope cancels the kinetic friction, and the friction is $\mu mg\cos\alpha$, so $\tan\alpha = \mu$. The measurements have random variation, so the mean is taken as the angle, and the variation is described by the interval between the extreme values of the measurements.
**Free-body diagram:** The box as a rectangle along the board, $x$ down the board and $y$ perpendicularly out of the board. The weight $\overline{G}$ from the centre straight down, the normal force $\overline{N}$ from the bottom surface perpendicularly out of the board and the kinetic friction $\overline{F}_\mu$ up the board. The forces cancel each other along the slope and perpendicular to it.
```voimakuvio
pinta -17,8
G 100
N 95,2
F_mu 30,6 ylös
a 0
akselit -17,8
komponentit G
```
**Formula:** $y$: $N = mg\cos\alpha$; $x$: $mg\sin\alpha - \mu N = 0$, so $\mu = \tan\alpha$. The mean $\alpha_{\text{mean}} = \dfrac{\text{sum}}{5}$
**Conversions:** The angle is in degrees, and the calculator is in degree mode. The coefficient of friction has no unit.
**Substitution:** a) The sum of the angles is $17.5\,{}^\circ + 18.0\,{}^\circ + 18.5\,{}^\circ + 17.0\,{}^\circ + 18.0\,{}^\circ = 89.0\,{}^\circ$, so $\alpha_{\text{mean}} = \dfrac{89.0\,{}^\circ}{5} = 17.8\,{}^\circ$ and $\mu = \tan 17.8\,{}^\circ = 0.321$. b) From the smallest angle $\tan 17.0\,{}^\circ = 0.306$ and from the largest $\tan 18.5\,{}^\circ = 0.335$, so the half-range is $\dfrac{0.335 - 0.306}{2} \approx 0.015$
**Answer:** a) $\mu = 0.321$, to three significant figures like the mean angle $17.8\,{}^\circ$. b) The coefficient varies between $0.306 \ldots 0.335$, that is, $\mu \approx 0.32 \pm 0.02$. The variation is about $5\,\%$ of the coefficient; it is a simple estimate of the spread of the measurements.
**Reasonableness:** The coefficient $0.32$ is smaller than $1$ and of the order of magnitude of ordinary dry surfaces. The variation of the angles is only $\pm 0.75\,{}^\circ$, but it affects the coefficient by about $5\,\%$, so a single measurement is not enough. The range describes only random variation, not a systematic error caused by the roughness or the moisture of the board.

## fy4-16-L3-04
**Given:** slope $\alpha = 14.0\,{}^\circ$, $\mu_1 = 0.060$; flat part $\mu_2 = 0.150$; the fence is $25.0\,\text{m}$ from the foot of the slope and the sled must stop at least $5.0\,\text{m}$ before it, so the length of the flat part is $d = 25.0\,\text{m} - 5.0\,\text{m} = 20.0\,\text{m}$; $v_1 = 0$ and at the end $v_2 = 0$; $g = 9.81\,\text{m/s}^2$
**Find:** b) the maximum length $L$ of the slope in $\text{m}$; c) the speed $v$ at the foot of the slope
**Principle:** The sled is at rest at the start and at the end, so we use the work–energy principle for the whole distance. The decrease of potential energy is used up by the negative work of friction, first on the slope and then on the flat. The normal force does no work. On the slope the friction force comes from the free-body diagram, and its work is $-\mu_1 mg\cos\alpha\cdot L$. A longer slope would give more speed, so the sled stops next to the fence exactly at the maximum allowed length.
**Free-body diagram:** On the slope the sled as a rectangle along the slope: the weight $\overline{G}$ from the centre straight down, the normal force $\overline{N}$ perpendicularly out of the slope, $N = mg\cos\alpha$, and the kinetic friction $\overline{F}_\mu$ up the slope. On the flat the weight down, the normal force up, equally long, and the friction backwards, and the friction is larger there because $\mu_2 > \mu_1$. The velocity is not drawn as a force.
```voimakuvio
pinta -14
G 100
N 97,03
F_mu 5,82 ylös
a alas
---
pinta 0
G 100
N 100
F_mu 15 vasen
a vasen
```
**Formula:** The height of the slope is $h = L\sin\alpha$. Zero level at the flat: $mgL\sin\alpha - \mu_1 mg\cos\alpha\cdot L - \mu_2 mgd = 0$, so $L = \dfrac{\mu_2 d}{\sin\alpha - \mu_1\cos\alpha}$. At the foot of the slope $mgL\sin\alpha - \mu_1 mg\cos\alpha\cdot L = \tfrac12 mv^2$
**Conversions:** The quantities are in SI units, and the coefficients of friction have no unit. The mass cancels in both equations.
**Substitution:** The expression in the denominator is $\sin 14.0\,{}^\circ - 0.060\cdot\cos 14.0\,{}^\circ = 0.2419 - 0.0582 = 0.1837$, so $L = \dfrac{0.150\cdot 20.0\,\text{m}}{0.1837} = 16.33\,\text{m}$. At the foot $v = \sqrt{2gL\left(\sin\alpha - \mu_1\cos\alpha\right)} = \sqrt{2\cdot 9.81\,\tfrac{\text{m}}{\text{s}^2}\cdot 16.33\,\text{m}\cdot 0.1837} = 7.67\,\text{m/s}$
**Answer:** b) $16\,\text{m}$, two significant figures like the coefficient of friction $0.060$; c) $7.7\,\text{m/s}$. The mass cancels, because both the weight and the friction are proportional to the mass: a heavier child gets a larger kinetic energy but also a larger friction force, and the speed is the same.
**Reasonableness:** The height of the slope is $h = 16.33\,\text{m}\cdot\sin 14.0\,{}^\circ = 3.95\,\text{m}$ and the horizontal distance $16.33\,\text{m}\cdot\cos 14.0\,{}^\circ = 15.85\,\text{m}$. On the slope friction uses up a height of $0.060\cdot 15.85\,\text{m} = 0.95\,\text{m}$ and on the flat $0.150\cdot 20.0\,\text{m} = 3.00\,\text{m}$, together $3.95\,\text{m}$, as it should. On the flat the stopping distance is $\dfrac{v^2}{2\mu_2 g} = \dfrac{(7.67\,\text{m/s})^2}{2\cdot 0.150\cdot 9.81\,\text{m/s}^2} = 20.0\,\text{m}$. The sled slides because $\tan 14.0\,{}^\circ = 0.249 > \mu_1$. The calculated greatest length $16.3\,\text{m}$ holds only under the assumptions of the task. The real coefficient of friction of snow varies, for example with the temperature, ice, the quality of the snow and the bottom of the sled, and even a slightly smaller coefficient would lengthen the sliding distance. Therefore the model cannot be used directly for the safety design of a real sledging hill.

## fy4-16-L3-05
**Given:** $m = 78.0\,\text{kg}$; from the table the downward speeds at $0$ – $3.0\,\text{s}$ and at $4.0\,\text{s}$; $g = 9.81\,\text{m/s}^2$; positive direction down
**Find:** a) the distance fallen $h$ between $0$ and $3.0\,\text{s}$; b) the air resistance $F_\text{d}$ on average over this distance in $\text{kN}$; c) whether the air resistance between $3.0$ and $4.0\,\text{s}$ is larger than, smaller than or equal to the weight
**Principle:** The distance comes from the table: in each time interval the distance travelled is the average speed times the interval. When the initial and final speeds and the distance are known, we use the work–energy principle: the air resistance is the only force other than the weight and points against the motion, so its work is $-F_\text{d} h$. In part c) Newton's second law: the direction of the acceleration tells which force is larger.
**Free-body diagram:** The skydiver with the parachute as a rectangle, positive direction down. The weight $\overline{G}$ from the centre down and the air resistance $\overline{F}_\text{d}$ from the top surface up, clearly longer than the weight, because the skydiver slows down. The velocity down is marked separately and not as a force.
```voimakuvio
G 765,2
F_v 2205 ylös
a ylös
v alas
```
**Reading the graph:** The average speeds are the means of the speeds at the endpoints of the interval, and each interval is $0.5\,\text{s}$. The highest speed is at the start, $46.0\,\text{m/s}$, and the speed first decreases steeply: over the first interval the speed decreases by $16.2\,\text{m/s}$, over the last half-second interval by only $1.1\,\text{m/s}$. The skydiver moves down all the time, so distance accumulates all the time.
**Formula:** $h = \sum \dfrac{v_i + v_{i+1}}{2}\,\Delta t$. Zero level at the final height: $E_{\text{k},1} + mgh - F_\text{d} h = E_{\text{k},2}$, so $F_\text{d} = mg + \dfrac{E_{\text{k},1} - E_{\text{k},2}}{h}$. In part c) $mg - F_\text{d} = ma$, so $F_\text{d} = m(g - a)$
**Conversions:** We calculate in newtons and convert to kilonewtons at the end: $1\,\text{kN} = 1000\,\text{N}$.
**Substitution:** a) The distances of the intervals are $18.95\,\text{m}$, $12.475\,\text{m}$, $8.625\,\text{m}$, $6.35\,\text{m}$, $5.00\,\text{m}$ and $4.225\,\text{m}$. The sum is $h = 55.625\,\text{m}$. b) The kinetic energies are $E_{\text{k},1} = \tfrac12\cdot 78.0\,\text{kg}\cdot(46.0\,\text{m/s})^2 = 82\,524\,\text{J}$ and $E_{\text{k},2} = \tfrac12\cdot 78.0\,\text{kg}\cdot(7.9\,\text{m/s})^2 = 2434\,\text{J}$, so $F_\text{d} = 78.0\,\text{kg}\cdot 9.81\,\text{m/s}^2 + \dfrac{82\,524\,\text{J} - 2434\,\text{J}}{55.625\,\text{m}} = 765.2\,\text{N} + 1439.8\,\text{N} = 2205\,\text{N}$. c) Between $3.0$ and $4.0\,\text{s}$ the speed decreases from $7.9\,\text{m/s}$ to $6.8\,\text{m/s}$, so $a = \dfrac{6.8 - 7.9}{1.0}\,\text{m/s}^2 = -1.1\,\text{m/s}^2$, that is, the acceleration points up, and $F_\text{d} = 78.0\,\text{kg}\cdot(9.81 + 1.1)\,\text{m/s}^2 = 851\,\text{N}$
**Answer:** b) $2.21\,\text{kN}$ upwards, three significant figures like the mass $78.0\,\text{kg}$ and the speeds; a) $h = 55.6\,\text{m}$; c) the air resistance is larger than the weight, because the speed decreases and the acceleration points up.
**Reasonableness:** The average air resistance is about $2.9$ times the weight $765\,\text{N}$, so the net force points up and the skydiver slows down. The time average from the equation of motion is smaller: the mean acceleration is $\dfrac{46.0 - 7.9}{3.0}\,\text{m/s}^2 = 12.7\,\text{m/s}^2$, so $F_\text{d} \approx 78.0\,\text{kg}\cdot(9.81 + 12.7)\,\text{m/s}^2 \approx 1.76\,\text{kN}$. The difference is correct: the air resistance is greatest right after the opening, when the speed is high, and the skydiver then travels a long distance in a short time, so the average over distance is weighted towards the start. At the end the air resistance approaches the weight $765\,\text{N}$ ($851\,\text{N}$ is already close to it).

## fy4-16-L2-08
**Find:** which conclusion can be drawn on the basis of the table alone, when the uncertainty of a reading is $\Delta x = 1.0\,\text{m}$.
**Principle:** The difference between two readings can be considered real only when the uncertainty intervals $x \pm \Delta x$ do not overlap, that is, when the difference is greater than $2\Delta x$. If the intervals overlap, the difference cannot be shown, but that does not prove that there is no difference. A dependence extended outside the measured range is an estimate, not a measurement result.
**Model answer:** When the starting height doubles from $2.00\,\text{m}$ to $4.00\,\text{m}$, the distances grow by

$40.2\,\text{m} - 19.6\,\text{m} = 20.6\,\text{m}$

$39.5\,\text{m} - 20.3\,\text{m} = 19.2\,\text{m}$

Both differences are about twenty times the uncertainty $1.0\,\text{m}$ and much larger than $2\Delta x = 2.0\,\text{m}$, so the uncertainty intervals are clearly separate, and therefore the starting height affects the distance. The other conclusions do not hold. The differences between the distances measured from the same height are

$20.3\,\text{m} - 19.6\,\text{m} = 0.7\,\text{m}$

$40.2\,\text{m} - 39.5\,\text{m} = 0.7\,\text{m}$

They are smaller than $2\Delta x = 2.0\,\text{m}$, so the uncertainty intervals overlap, and the heavier sled travelled farther from the height $2.00\,\text{m}$ but a shorter distance from the height $4.00\,\text{m}$. So the data do not show that the heavier sled would travel farther. They do not prove, however, that the mass has no effect at all, because an effect of under $2\,\text{m}$ would be lost in the uncertainty. The result fits the model $x = \tfrac{h}{\mu}$, in which the mass cancels out.

The distance $80\,\text{m}$ from the height $8.00\,\text{m}$ would be an estimate extended outside the measured range, and it assumes the same coefficient of friction for the whole distance, so it is not a certain result. The result is reasonable: the ratio $h : x \approx 0.10$ is almost the same in every row and is a reasonable coefficient of kinetic friction between snow and a sled.
