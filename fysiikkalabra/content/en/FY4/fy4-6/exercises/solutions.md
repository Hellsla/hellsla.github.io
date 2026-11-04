## fy4-6-L1-01
**Given:** $m = 160\,\text{kg}$, the acceleration of free fall on the Moon $g_\text{Moon} = 1.62\,\text{m/s}^2$
**Find:** the weight on the surface of the Moon $G$ in $\text{N}$
**Principle:** Weight is the force with which a celestial body pulls an object, and its magnitude is the product of the mass and the acceleration of free fall. The mass is the same on the Moon as on Earth, but the acceleration of free fall is smaller on the Moon.
**Free-body diagram:** The astronaut as a rectangle on the surface of the Moon: the weight $\overline{G}$ from the center down and the normal force $\overline{N}$ from the lower surface up, equally long. What is asked is the magnitude of the weight $mg_\text{Moon}$.
```voimakuvio
pinta 0
G 259,2
N 259,2
a 0
```
**Formula:** $G = m g_\text{Moon}$
**Conversions:** The mass is in kilograms and the acceleration in $\text{m/s}^2$, so no conversions are needed.
**Substitution:** $G = 160\,\text{kg}\cdot 1.62\,\text{m/s}^2 = 259.2\,\text{N}$
**Answer:** $259\,\text{N}$, three significant figures like the acceleration of free fall $1.62\,\text{m/s}^2$.
**Reasonableness:** On Earth the weight would be $160\,\text{kg}\cdot 9.81\,\text{m/s}^2 \approx 1570\,\text{N}$. The acceleration of free fall on the Moon is about a sixth of the value on Earth, and $1570\,\text{N} : 6 \approx 260\,\text{N}$, the same result.

## fy4-6-L1-02
**Given:** $m = 30\,\text{kg}$, $\mu = 0.12$, the sled slides on horizontal snow; $g = 9.81\,\text{m/s}^2$
**Find:** the kinetic friction $F_\mu$ in $\text{N}$
**Principle:** The sled slides, so kinetic friction $F_\mu = \mu N$ acts on it. In the vertical direction the sled does not accelerate, so by Newton's second law the normal force equals the weight.
**Free-body diagram:** The sled as a rectangle, $x$ in the direction of motion and $y$ up. The weight $\overline{G}$ from the center down, the normal force $\overline{N}$ of the snow from the lower surface up and equally long as the weight, the kinetic friction $\overline{F}_\mu$ from the rear corner of the lower surface backward. There is no force pushing forward.
```voimakuvio
pinta 0
G 294,3
N 294,3
F_mu 35,32 vasen
v oikea
a vasen
akselit 0
```
**Formula:** $y$: $N - mg = 0$, so $N = mg$ and $F_\mu = \mu N = \mu mg$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $F_\mu = 0.12\cdot 30\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 35.316\,\text{N}$
**Answer:** $35\,\text{N}$, two significant figures like the coefficient of friction $0.12$ and the mass $30\,\text{kg}$.
**Reasonableness:** The weight of the sled is about $290\,\text{N}$, and the friction is about an eighth of it, as the small coefficient of friction $0.12$ requires. The friction slows the sled down: $a = F_\mu : m \approx 1.2\,\text{m/s}^2$.

## fy4-6-L1-03
**Given:** $m = 40\,\text{kg}$, the horizontal pushing force $F = 120\,\text{N}$, the box slides at a constant velocity; $g = 9.81\,\text{m/s}^2$
**Find:** the coefficient of kinetic friction $\mu$ (no unit)
**Principle:** In uniform motion the sum of the forces is zero, so the kinetic friction equals the push and the normal force equals the weight. The kinetic friction is $F_\mu = \mu N$.
**Free-body diagram:** The box as a rectangle, $x$ in the direction of motion and $y$ up. The pushing force $\overline{F}$ forward, the kinetic friction $\overline{F}_\mu$ backward and equally long, the weight $\overline{G}$ down and the normal force $\overline{N}$ up, equally long.
```voimakuvio
pinta 0
G 392,4
N 392,4
F 120 oikea työntö
F_mu 120 vasen
v oikea
a 0
akselit 0
```
**Formula:** $x$: $F - \mu N = 0$ and $y$: $N - mg = 0$, so $\mu = \dfrac{F}{mg}$
**Conversions:** The mass is in kilograms and the force in newtons, so no conversions are needed.
**Substitution:** $\mu = \dfrac{120\,\text{N}}{40\,\text{kg}\cdot 9.81\,\text{m/s}^2} = \dfrac{120\,\text{N}}{392.4\,\text{N}} = 0.3058$
**Answer:** $0.31$, two significant figures like the mass $40\,\text{kg}$.
**Reasonableness:** The coefficient of friction has no unit, because it is the ratio of two forces. The push $120\,\text{N}$ is a little under a third of the weight of the box $392\,\text{N}$, so the coefficient is a little over $0.3$, a common value for wood against a floor.

## fy4-6-L1-04
**Given:** $m = 0.80\,\text{kg}$, the angle of the desktop $\alpha = 20^\circ$, the book is at rest; $g = 9.81\,\text{m/s}^2$
**Find:** the normal force $N$ in $\text{N}$
**Principle:** The book does not move in the direction perpendicular to the desktop, so by Newton's second law the sum of the forces in that direction is zero. The normal force cancels the perpendicular component of the weight.
**Free-body diagram:** The book as a rectangle along the desktop, $x$ down along the desktop and $y$ perpendicular to the desktop, outward. The weight $\overline{G}$ straight down and its components $mg\sin\alpha$ and $mg\cos\alpha$ dashed, the normal force $\overline{N}$ perpendicular to the desktop, outward, and the static friction $\overline{F}_\mu$ up along the desktop.
```voimakuvio
pinta -20
G 7,848
N 7,375
F_mu 2,684 ylös
a 0
akselit -20
komponentit G
```
**Formula:** $y$: $N - mg\cos\alpha = 0$, so $N = mg\cos\alpha$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $N = 0.80\,\text{kg}\cdot 9.81\,\text{m/s}^2\cdot\cos 20^\circ = 7.848\,\text{N}\cdot 0.9397 = 7.375\,\text{N}$
**Answer:** $7.4\,\text{N}$, two significant figures like the mass $0.80\,\text{kg}$.
**Reasonableness:** The weight of the book is $7.8\,\text{N}$, and the normal force is a little smaller, because the desktop is slanted. On a horizontal desktop the normal force would be the whole weight, on a vertical one zero.

## fy4-6-L1-05
**Given:** $m = 12\,\text{kg}$, the angle of inclination of the slope $\alpha = 30^\circ$; $g = 9.81\,\text{m/s}^2$
**Find:** the component of the weight along the slope $G_x$ in $\text{N}$
**Free-body diagram:** The box as a rectangle along the slope, $x$ down the slope. The weight $\overline{G}$ straight down and its components $G_x$ and $G_y$ dashed; the other forces do not affect the asked component.
```voimakuvio
pinta -30
G 117,7
N 101,9
F_mu 58,86 ylös
a 0
akselit -30
komponentit G
```
**Principle:** The weight points straight down. When the $x$-axis is chosen along the slope, the component of the weight in its direction is obtained from a right triangle in which the angle between the weight and the perpendicular component is the angle of inclination $\alpha$ of the slope.
**Formula:** $G_x = G\sin\alpha = mg\sin\alpha$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $G_x = 12\,\text{kg}\cdot 9.81\,\text{m/s}^2\cdot\sin 30^\circ = 117.72\,\text{N}\cdot 0.5 = 58.86\,\text{N}$
**Answer:** $59\,\text{N}$, two significant figures like the mass $12\,\text{kg}$.
**Reasonableness:** At $30^\circ$ the sine is exactly $0.5$, so the component along the slope is half of the weight $118\,\text{N}$. The component is always smaller than the weight itself.

## fy4-6-L2-01
**Given:** $\alpha = 12^\circ$, the sled starts from rest, $v = 3.0\,\text{m/s}$ in the time $t = 4.0\,\text{s}$, the acceleration is constant, air drag is ignored; $g = 9.81\,\text{m/s}^2$
**Find:** the coefficient of kinetic friction $\mu$ (no unit)
**Principle:** The acceleration is obtained from the change of velocity, and Newton's second law along the slope gives the friction. The sled slides, so kinetic friction $F_\mu = \mu N$ acts on it. In the perpendicular direction the sled does not accelerate.
**Free-body diagram:** The sled as a rectangle along the slope, $x$ down the slope and $y$ perpendicular to the surface, outward. The weight $\overline{G}$ straight down and its components dashed, the normal force $\overline{N}$ perpendicular to the surface, outward, and the kinetic friction $\overline{F}_\mu$ up the slope. The acceleration $\overline{a}$ is drawn separately as an orange arrow down the slope.
```voimakuvio
pinta -12
G 196,2
N 191,9
F_mu 25,79 ylös
a alas
akselit -12
komponentit G
```
**Formula:** $a = \dfrac{v - 0}{t}$, $y$: $N - mg\cos\alpha = 0$ and $x$: $mg\sin\alpha - \mu N = ma$, so $\mu = \dfrac{g\sin\alpha - a}{g\cos\alpha}$
**Conversions:** All quantities are in SI units, so no conversions are needed, and the mass cancels.
**Substitution:** $a = \dfrac{3.0\,\text{m/s}}{4.0\,\text{s}} = 0.75\,\text{m/s}^2$ and $\mu = \dfrac{9.81\,\text{m/s}^2\cdot\sin 12^\circ - 0.75\,\text{m/s}^2}{9.81\,\text{m/s}^2\cdot\cos 12^\circ} = \dfrac{2.040 - 0.75}{9.596} = 0.134$
**Answer:** $0.13$, two significant figures like the velocity $3.0\,\text{m/s}$ and the time $4.0\,\text{s}$.
**Reasonableness:** Without friction the acceleration would be $g\sin 12^\circ \approx 2.0\,\text{m/s}^2$, so friction reduces it, as it should. The coefficient $0.13$ is smaller than $\tan 12^\circ = 0.21$, at which the sled would slide at a constant velocity, and it fits between a plastic sled and snow ($0.05$–$0.3$).

## fy4-6-L2-02
**Given:** $m = 40\,\text{kg}$, the horizontal tension of the rope $T = 150\,\text{N}$, $\mu = 0.30$; $g = 9.81\,\text{m/s}^2$
**Find:** the acceleration $a$ in $\text{m/s}^2$
**Principle:** The pallet slides, so kinetic friction $\mu N$ acts on it. In the vertical direction it does not accelerate, so $N = mg$. In the horizontal direction, by Newton's second law, the difference between the tension and the friction accelerates the pallet.
**Free-body diagram:** The pallet as a rectangle, $x$ in the direction of the pull and $y$ up. The tension of the rope $\overline{T}$ forward, the kinetic friction $\overline{F}_\mu$ from the rear corner of the lower surface backward and shorter, the weight $\overline{G}$ down and the normal force $\overline{N}$ up, equally long.
```voimakuvio
pinta 0
G 392,4
N 392,4
T 150 oikea
F_mu 117,7 vasen
v oikea
a oikea
akselit 0
```
**Formula:** $y$: $N - mg = 0$ and $x$: $T - \mu N = ma$, so $a = \dfrac{T - \mu mg}{m}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{150\,\text{N} - 0.30\cdot 40\,\text{kg}\cdot 9.81\,\text{m/s}^2}{40\,\text{kg}} = \dfrac{150\,\text{N} - 117.72\,\text{N}}{40\,\text{kg}} = 0.807\,\text{m/s}^2$
**Answer:** $0.81\,\text{m/s}^2$, two significant figures like the coefficient of friction $0.30$ and the mass $40\,\text{kg}$.
**Reasonableness:** Without friction the acceleration would be $150\,\text{N} : 40\,\text{kg} \approx 3.8\,\text{m/s}^2$. The friction $118\,\text{N}$ cancels most of the force of the rope, so the acceleration stays under $1\,\text{m/s}^2$, which is reasonable.

## fy4-6-L2-03
**Given:** the five measurement points $(N, F_\mu)$ of the graph of the example data: $(5\,\text{N};\,1.1\,\text{N})$, $(10\,\text{N};\,2.1\,\text{N})$, $(15\,\text{N};\,3.3\,\text{N})$, $(20\,\text{N};\,4.2\,\text{N})$ and $(25\,\text{N};\,5.4\,\text{N})$
**Find:** the coefficient of kinetic friction $\mu$ (no unit)
**Principle:** Kinetic friction is proportional to the normal force, $F_\mu = \mu N$, so the $(N, F_\mu)$ graph is a straight line through the origin whose slope is $\mu$. The slope is read from a line fitted to the points, not from two neighbouring measurement points, because measurement points are usually not exactly on the same line because of measurement uncertainty.
**Reading the graph:** A line is drawn through the origin so that it passes as close as possible to all the points. A point far away is read from the line, for example at the normal force $N = 25\,\text{N}$ the value of the line is about $F_\mu = 5.35\,\text{N}$.
**Formula:** $\mu = \dfrac{\Delta F_\mu}{\Delta N}$, when $\Delta F_\mu$ and $\Delta N$ are read from the fitted line
**Conversions:** Both axes are in newtons, so the units cancel and no conversions are needed.
**Substitution:** $\mu = \dfrac{5.35\,\text{N} - 0\,\text{N}}{25\,\text{N} - 0\,\text{N}} = 0.214$
**Answer:** $0.21$, two significant figures, because the friction forces have been measured to two figures and the line is drawn by hand.
**Reasonableness:** The individual points give the ratios $0.21$–$0.22$, for example $4.2\,\text{N} : 20\,\text{N} = 0.21$, so the slope of the fitted line falls between them. The coefficient has no unit, as the ratio of two forces should not.

## fy4-6-L2-04
**Given:** $m = 10\,\text{kg}$, $\alpha = 35^\circ$, $\mu_0 = 0.60$, the box is placed at rest; $g = 9.81\,\text{m/s}^2$
**Find:** the difference $G_x - F_\text{max}$ in $\text{N}$, where $F_\text{max}$ is the greatest value of static friction; the sign of the difference tells whether the box stays in place
**Principle:** Static friction is at most $\mu_0 N$. The box stays in place only if this upper limit is enough to cancel the component of the weight along the slope. In the perpendicular direction the box does not accelerate, so $N = mg\cos\alpha$.
**Free-body diagram:** The box as a rectangle along the slope, $x$ down the slope and $y$ perpendicular to the surface, outward. The weight $\overline{G}$ straight down and its components $mg\sin\alpha$ and $mg\cos\alpha$ dashed, the normal force $\overline{N}$ perpendicular to the surface, outward, and the friction $\overline{F}_\mu$ up the slope.
```voimakuvio
pinta -35
G 98,1
N 80,36
F_mu 48,22 ylös
a alas
akselit -35
komponentit G
```
**Formula:** $y$: $N - mg\cos\alpha = 0$, so the greatest static friction is $F_\text{max} = \mu_0 mg\cos\alpha$, and it is compared with the component $G_x = mg\sin\alpha$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $F_\text{max} = 0.60\cdot 10\,\text{kg}\cdot 9.81\,\text{m/s}^2\cdot\cos 35^\circ = 48.2\,\text{N}$ and $G_x = 10\,\text{kg}\cdot 9.81\,\text{m/s}^2\cdot\sin 35^\circ = 56.3\,\text{N}$, so $G_x - F_\text{max} = 8.1\,\text{N}$
**Answer:** the component exceeds the greatest static friction by $56.3\,\text{N} - 48.2\,\text{N} = 8.1\,\text{N}$, two significant figures like the coefficient of friction $0.60$. The greatest static friction $48\,\text{N}$ is smaller than the component $56\,\text{N}$, so the box does not stay in place but starts to slide. The difference is positive, so the friction is not enough.
**Reasonableness:** The same conclusion follows from the angle: $\tan 35^\circ = 0.70$ is greater than $\mu_0 = 0.60$, so the plank is steeper than the limiting angle $\tan^{-1} 0.60 \approx 31^\circ$.

## fy4-6-L3-01
**Given:** $m = 50\,\text{kg}$, the acceleration of the truck and the box $a = 3.5\,\text{m/s}^2$ forward, the road is horizontal; $g = 9.81\,\text{m/s}^2$
**Find:** the smallest value of the coefficient of static friction $\mu_0$ (no unit)
**Principle:** If the box does not slide, it accelerates along with the truck. The only horizontal force on the box is the static friction of the bed, so by Newton's second law it must be $ma$ and point forward, in the direction of motion. Static friction can be at most $\mu_0 N$.
**Free-body diagram:** The box as a rectangle, $x$ forward and $y$ up. The weight $\overline{G}$ from the center down, the normal force $\overline{N}$ of the bed from the lower surface up and equally long, the static friction $\overline{F}_\mu$ from the front corner of the lower surface forward. The acceleration is drawn separately as a thin orange arrow, not as a force.
```voimakuvio
pinta 0
G 490,5
N 490,5
F_mu 175 oikea
a oikea
akselit 0
```
**Formula:** $y$: $N - mg = 0$ and $x$: $F_\mu = ma$. The condition $F_\mu \le \mu_0 N$ gives $ma \le \mu_0 mg$, so $\mu_0 \ge \dfrac{a}{g}$
**Conversions:** The accelerations are in $\text{m/s}^2$, so no conversions are needed, and the mass cancels.
**Substitution:** $\mu_0 = \dfrac{3.5\,\text{m/s}^2}{9.81\,\text{m/s}^2} = 0.357$
**Answer:** $0.36$, two significant figures like the acceleration $3.5\,\text{m/s}^2$.
**Reasonableness:** The friction points in the direction of motion, because the bed tends to slide forward from under the box. The mass cancels, so the result holds for a light and a heavy box. On wet plywood the coefficient can be below $0.36$, and then the box slides backward relative to the bed: this is why cargo is fastened.

## fy4-6-L3-02
**Given:** the angle of the slope $\alpha = 20^\circ$, the initial velocity $v_0 = 3.0\,\text{m/s}$ up the slope, $\mu = 0.25$, the final velocity $v = 0$; $g = 9.81\,\text{m/s}^2$
**Find:** the sliding distance $s$ in $\text{m}$
**Principle:** When sliding up, both the component of the weight along the slope and the kinetic friction point down the slope, so the puck decelerates uniformly. The acceleration is obtained from Newton's second law, and the distance from the equation of uniformly accelerated motion $v^2 = v_0^2 - 2as$, where $a$ is the magnitude of the deceleration.
**Free-body diagram:** The puck as a rectangle along the slope, $x$ down the slope and $y$ perpendicular to the surface, outward. The weight $\overline{G}$ straight down and its components dashed, the normal force $\overline{N}$ perpendicular to the surface, outward, and the kinetic friction $\overline{F}_\mu$ down the slope, because the puck slides up. The velocity is up the slope, but it is not a force.
```voimakuvio
pinta -20
G 9,81
N 9,218
F_mu 2,305 alas
v 160
a alas
akselit -20
komponentit G
```
**Formula:** $y$: $N = mg\cos\alpha$ and $x$: $mg\sin\alpha + \mu mg\cos\alpha = ma$, so $a = g(\sin\alpha + \mu\cos\alpha)$. From the equation of motion $v^2 = v_0^2 - 2as$ and the condition $v = 0$ we get $s = \dfrac{v_0^2}{2a}$, where $a = g(\sin\alpha + \mu\cos\alpha)$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = 9.81\,\text{m/s}^2\cdot(\sin 20^\circ + 0.25\cdot\cos 20^\circ) = 5.660\,\text{m/s}^2$ and $s = \dfrac{(3.0\,\text{m/s})^2}{2\cdot 5.660\,\text{m/s}^2} = 0.795\,\text{m}$
**Answer:** $0.80\,\text{m}$, two significant figures like the velocity $3.0\,\text{m/s}$ and the coefficient of friction $0.25$.
**Reasonableness:** Without friction the deceleration would be $g\sin 20^\circ \approx 3.4\,\text{m/s}^2$ and the distance about $1.3\,\text{m}$; friction shortens the distance. After stopping, the puck stays on the slope only if the coefficient of static friction is at least $\tan 20^\circ \approx 0.36$; otherwise it starts to slide back down.

## fy4-6-L3-03
**Given:** on Earth $\alpha = 30^\circ$ and $a_\text{Earth} = 2.0\,\text{m/s}^2$ down the slope, on the Moon the same slope and surface, $g = 9.81\,\text{m/s}^2$ and $g_\text{Moon} = 1.62\,\text{m/s}^2$; there is no air drag
**Find:** the acceleration on the Moon $a_\text{Moon}$ in $\text{m/s}^2$
**Principle:** The box slides, so kinetic friction $\mu N$ acts on it up the slope. The coefficient of friction is not given, but it is a property of the surface and the same on Earth and on the Moon. The acceleration on Earth gives $\mu$, and on the Moon the same law gives the new acceleration. In the perpendicular direction the box does not accelerate.
**Free-body diagram:** The box as a rectangle along the slope, $x$ down the slope and $y$ perpendicular to the surface, outward. The weight $\overline{G}$ straight down and its components dashed, the normal force $\overline{N}$ perpendicular to the surface, outward, and the kinetic friction $\overline{F}_\mu$ up the slope.
```voimakuvio
pinta -30
G 98,1
N 84,96
F_mu 29,05 ylös
a alas
akselit -30
komponentit G
```
**Formula:** $y$: $N - mg\cos\alpha = 0$ and $x$: $mg\sin\alpha - \mu N = ma$, so $a = g(\sin\alpha - \mu\cos\alpha)$ and $\mu = \tan\alpha - \dfrac{a_\text{Earth}}{g\cos\alpha}$. Because the expression in the parentheses is the same in both places, $a_\text{Moon} = a_\text{Earth}\cdot\dfrac{g_\text{Moon}}{g}$
**Conversions:** All quantities are in SI units, so no conversions are needed, and the mass cancels.
**Substitution:** $\mu = \tan 30^\circ - \dfrac{2.0\,\text{m/s}^2}{9.81\,\text{m/s}^2\cdot\cos 30^\circ} = 0.577 - 0.235 = 0.342$, and $a_\text{Moon} = 1.62\,\text{m/s}^2\cdot(\sin 30^\circ - 0.342\cdot\cos 30^\circ) = 0.330\,\text{m/s}^2$. Directly from the ratio: $2.0\,\text{m/s}^2\cdot\dfrac{1.62}{9.81} = 0.330\,\text{m/s}^2$
**Answer:** $0.33\,\text{m/s}^2$, two significant figures like the acceleration on Earth $2.0\,\text{m/s}^2$.
**Reasonableness:** On the Moon both the weight and the friction are about a sixth of the values on Earth, so the acceleration is also about a sixth. The box slides on the Moon too, because the condition $\tan\alpha > \mu$ does not depend on the acceleration of free fall.

## fy4-6-L1-06
**Find:** the magnitude of the friction force exerted by the floor on the box while the box stays in place
**Principle:** The box is at rest, so by Newton's second law the sum of the horizontal forces is zero. Static friction adapts to the situation: it is equal in magnitude to the push and opposite in direction, as long as the push does not exceed the maximum value of static friction.
**Model answer:** The magnitude of the friction force is $20\,\text{N}$, because the box is at rest and the friction cancels the push. The maximum value $60\,\text{N}$ is only an upper limit, and the push $20\,\text{N}$ stays below it. The claim that the friction is always equal to the maximum value is wrong, because static friction is only as large as the situation requires. The claim that there is no friction at all is wrong, because it is exactly the friction that keeps the box from moving. The claim that the friction is the difference between the maximum value and the push is wrong, because at rest the friction and the push are equal.

## fy4-6-L1-07
**Given:** $m = 50\,\text{kg}$, $\mu_0 = 0.45$, the box is at rest on a horizontal floor; $g = 9.81\,\text{m/s}^2$
**Find:** the smallest horizontal force $F$ in $\text{N}$ with which the box starts to move
**Principle:** The box starts to move when the push exceeds the maximum value of static friction $\mu_0 N$. In the limiting case the push is equal to this maximum value. In the vertical direction the box does not accelerate, so $N = mg$.
**Free-body diagram:** The box as a rectangle, $x$ in the direction of the push and $y$ up. The pushing force $\overline{F}$ forward, the static friction $\overline{F}_\mu$ backward and, in the limiting case, equally long, the weight $\overline{G}$ down and the normal force $\overline{N}$ up, equally long.
```voimakuvio
pinta 0
G 490,5
N 490,5
F 220,7 oikea työntö
F_mu 220,7 vasen
a 0
akselit 0
```
**Formula:** $y$: $N - mg = 0$ and $x$: $F - \mu_0 N = 0$, so $F = \mu_0 mg$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $F = 0.45\cdot 50\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 220.7\,\text{N}$
**Answer:** $2.2\cdot 10^2\,\text{N}$ or about $220\,\text{N}$, two significant figures like the coefficient of friction $0.45$ and the mass $50\,\text{kg}$. With a smaller force the box stays in place.
**Reasonableness:** The weight of the box is $490\,\text{N}$, and the required force is $0.45$ times that, as the coefficient of friction requires. After the box has started to move, the kinetic friction is usually smaller than $\mu_0 N$, so a smaller force is enough to keep it moving.

## fy4-6-L1-08
**Find:** the ratio of the magnitude of the normal force $N$ to the magnitude of the weight $G$ for a body at rest on an inclined plane
**Principle:** Choose the $y$-axis perpendicular to the surface. In that direction the body does not accelerate, so the sum of the forces is zero. Perpendicular to the surface only the normal force and the component of the weight $G_y = mg\cos\alpha$ act, and friction is parallel to the surface. The weight points straight down, and it is divided into components along the slope and perpendicular to it.
**Model answer:** The normal force is smaller than the weight: $N = mg\cos\alpha < G$. The normal force cancels only the component of the weight perpendicular to the surface, and the component along the slope is cancelled by friction. At the angle $30^\circ$ we get $N = G\cos 30^\circ \approx 0.87\,G$. The claim that the normal force and the weight are always opposite and equal holds only on a horizontal surface. The claim $N > G$ is wrong, because friction does not press the body against the surface. The claim $N = 0$ is wrong, because the component of the weight $G_y$ presses the body against the surface.

## fy4-6-L2-05
**Given:** the five measurements $(m, F)$ of the example data: $(0.20\,\text{kg};\,0.85\,\text{N})$, $(0.40\,\text{kg};\,1.62\,\text{N})$, $(0.60\,\text{kg};\,2.50\,\text{N})$, $(0.80\,\text{kg};\,3.31\,\text{N})$ and $(1.00\,\text{kg};\,4.02\,\text{N})$; the block is pulled horizontally at a constant velocity; $g = 9.81\,\text{m/s}^2$
**Find:** the coefficient of kinetic friction $\mu$ (no unit)
**Principle:** At a constant velocity the sum of the forces is zero, so the pull is equal to the kinetic friction, $F = F_\mu$. On a horizontal table the normal force is equal to the weight, $N = mg$. Because $F_\mu = \mu N$, the $(N, F_\mu)$ graph is a straight line through the origin whose slope is $\mu$.
**Reading the graph:** First calculate the normal forces: $N = mg$ gives the values $1.96\,\text{N}$, $3.92\,\text{N}$, $5.89\,\text{N}$, $7.85\,\text{N}$ and $9.81\,\text{N}$. Draw the points $(N, F_\mu)$ and fit to them a straight line through the origin that passes as close as possible to all the points. Read a distant point from the line: at the normal force $N = 9.81\,\text{N}$ the value of the line is about $F_\mu = 4.1\,\text{N}$.
**Formula:** $\mu = \dfrac{\Delta F_\mu}{\Delta N}$, when $\Delta F_\mu$ and $\Delta N$ are read from the fitted line
**Conversions:** Both axes are in newtons, so the units cancel. The masses are in kilograms, so no conversions are needed.
**Substitution:** $\mu = \dfrac{4.1\,\text{N} - 0\,\text{N}}{9.81\,\text{N} - 0\,\text{N}} = 0.418$
**Answer:** $0.42$, two significant figures, because the pulls were measured to three figures but the line is drawn by hand.
**Reasonableness:** The individual points give ratios $F : N$ between $0.41$ and $0.43$, for example $4.02\,\text{N} : 9.81\,\text{N} = 0.41$, so the slope of the fitted line falls between them. The coefficient has no unit, and it is of the usual order of magnitude for wood on a table.

## fy4-6-L2-06
**Given:** $m = 0.75\,\text{kg}$, the pulling force $F$ of the example data as a function of time $t$; the greatest reading $3.3\,\text{N}$ at the moment $t = 2.5\,\text{s}$, the readings during uniform motion $2.2\,\text{N}$, $2.1\,\text{N}$ and $2.2\,\text{N}$ at the moments $3.5\,\text{s}$–$4.5\,\text{s}$; $g = 9.81\,\text{m/s}^2$
**Find:** the coefficient of kinetic friction $\mu$ (no unit) and the coefficient of static friction $\mu_0$
**Principle:** Before the block starts to move, the pull increases and the static friction increases with it. When the pull exceeds the maximum value of static friction $\mu_0 N$, the block starts to move, and the peak of the graph is this maximum value. At a constant velocity the sum of the forces is zero, so the pull is equal to the kinetic friction $\mu N$. On a horizontal table $N = mg$.
**Reading the graph:** The pull increases linearly up to the moment $t = 2.5\,\text{s}$, where the peak of the graph is $3.3\,\text{N}$. After the peak the pull drops and stays almost constant, about $2.2\,\text{N}$, while the block moves at a constant velocity. The sum of the constant-pull readings is $2.2\,\text{N} + 2.1\,\text{N} + 2.2\,\text{N} = 6.5\,\text{N}$, so their mean is $6.5\,\text{N} : 3 = 2.17\,\text{N}$.
**Formula:** $N = mg$, $\mu_0 = \dfrac{F_{\text{peak}}}{N}$ and $\mu = \dfrac{F_{\text{steady}}}{N}$
**Conversions:** The mass is in kilograms and the forces in newtons, so no conversions are needed.
**Substitution:** $N = 0.75\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 7.36\,\text{N}$, $\mu_0 = \dfrac{3.3\,\text{N}}{7.36\,\text{N}} = 0.449$ and $\mu = \dfrac{2.17\,\text{N}}{7.36\,\text{N}} = 0.295$
**Answer:** the coefficient of kinetic friction is $\mu = 0.29$ and the coefficient of static friction $\mu_0 = 0.45$, two significant figures like the mass $0.75\,\text{kg}$ and the force readings.
**Reasonableness:** The coefficient of kinetic friction is smaller than the coefficient of static friction, $0.29 < 0.45$, as is usual. This is why the pull drops after the block has started to move: keeping it moving takes a smaller force than getting it moving. The coefficients are of the usual order of magnitude for wood on a table.

## fy4-6-L2-07
**Given:** the five angles of the example data: $24^\circ$, $26^\circ$, $25^\circ$, $27^\circ$ and $25^\circ$
**Find:** the coefficient of static friction $\mu_0$ (no unit)
**Principle:** As the board tilts, the component of the weight along the slope $G_x = mg\sin\alpha$ increases, and the static friction increases with it. The block starts to slide when the component exceeds the maximum value of static friction $\mu_0 N$. In the perpendicular direction the block does not accelerate, so $N = mg\cos\alpha$. At the limiting angle $\alpha_0$, $mg\sin\alpha_0 = \mu_0\,mg\cos\alpha_0$. The mass cancels, and dividing both sides gives $\mu_0 = \tan\alpha_0$.
**Formula:** $\mu_0 = \tan\alpha_0$, where $\alpha_0$ is the mean of the measurements
**Conversions:** The angles are in degrees, so no conversions are needed. The calculator must be in degree mode.
**Substitution:** The sum of the angles is $24^\circ + 26^\circ + 25^\circ + 27^\circ + 25^\circ = 127^\circ$, so the mean is $\alpha_{0,\text{mean}} = 127^\circ : 5 = 25.4^\circ$ and $\mu_0 = \tan 25.4^\circ = 0.4748$
**Answer:** $0.47$, two significant figures, as the precision of the mean of the angles gives.
**Reasonableness:** The individual angles give $\tan 24^\circ = 0.45$ and $\tan 27^\circ = 0.51$, so the mean $0.47$ lies between them. The mass of the block is not needed in the experiment, because it cancels. The result is of the usual order of magnitude for the coefficient of static friction between wood and wood.

## fy4-6-L3-04
**Given:** the initial velocity $v_0 = 80\,\text{km/h}$, the final velocity $v = 0$, constant acceleration, the wheels lock; the coefficients of kinetic friction of the example data: dry asphalt $\mu = 0.75$, wet asphalt $\mu = 0.45$; in part c) a wet downhill slope $\alpha = 6.0^\circ$; $g = 9.81\,\text{m/s}^2$
**Find:** the braking distance $s$ in $\text{m}$, in parts a) dry horizontal, b) wet horizontal and c) wet downhill
**Principle:** The locked wheels slide on the road, so kinetic friction $\mu N$ acts on the car against the motion. By Newton's second law the friction gives the deceleration, and the distance is obtained from the equation of uniformly accelerated motion $v^2 = v_0^2 - 2as$, where $a$ is the magnitude of the deceleration. In the perpendicular direction the car does not accelerate, so $N = mg\cos\alpha$.
**Free-body diagram:** The car of part c) as a rectangle along the slope, $x$ down the slope and $y$ perpendicular to the road, outward. The weight $\overline{G}$ straight down and its components dashed, the normal force $\overline{N}$ perpendicular to the road, outward, and the kinetic friction $\overline{F}_\mu$ up the slope. The velocity is down the slope, but the deceleration is up the slope.
```voimakuvio
pinta -6
G 9,81
N 9,756
F_mu 4,390 ylös
v alas
a ylös
akselit -6
komponentit G
```
**Formula:** on a horizontal road $N = mg$ and $\mu mg = ma$, so $a = \mu g$. Downhill $x$: $\mu mg\cos\alpha - mg\sin\alpha = ma$, so $a = g(\mu\cos\alpha - \sin\alpha)$. The distance is $s = \dfrac{v_0^2}{2a}$
**Conversions:** $v_0 = 80\,\text{km/h} = 80 : 3.6\,\text{m/s} = 22.22\,\text{m/s}$, and $v_0^2 = 493.8\,\text{m}^2/\text{s}^2$.
**Substitution:** Part a): $a_a = 0.75\cdot 9.81\,\text{m/s}^2 = 7.358\,\text{m/s}^2$ and $s_a = \dfrac{493.8\,\text{m}^2/\text{s}^2}{2\cdot 7.358\,\text{m/s}^2} = 33.6\,\text{m}$. Parts b) and c):
```latex
\begin{aligned}
a_b &= 0.45 \cdot 9.81\,\text{m/s}^2 = 4.415\,\text{m/s}^2 \\
s_b &= \frac{493.8\,\text{m}^2/\text{s}^2}{2 \cdot 4.415\,\text{m/s}^2} = 55.9\,\text{m} \\[4pt]
a_c &= 9.81\,\text{m/s}^2 \\
&\quad \cdot (0.45\cos 6.0^\circ - \sin 6.0^\circ) \\
&= 3.365\,\text{m/s}^2 \\
s_c &= \frac{493.8\,\text{m}^2/\text{s}^2}{2 \cdot 3.365\,\text{m/s}^2} = 73.4\,\text{m}
\end{aligned}
```
**Answer:** a) $34\,\text{m}$, b) $56\,\text{m}$ and c) $73\,\text{m}$ (calculated $73.4\,\text{m}$). The result of part c) is rounded to two significant figures like the coefficient of friction $0.45$ and the angle $6.0^\circ$. The mass of the car is not needed, because it cancels: both the friction and the component of the weight are proportional to the mass, so the deceleration does not depend on it.
**Reasonableness:** On the wet road the distance is $55.9 : 33.6 = 1.66$ times that on the dry road, and the same ratio follows from the coefficients of friction $0.75 : 0.45 = 1.67$. Downhill the distance is longer than on the horizontal wet road, $73\,\text{m} > 56\,\text{m}$, because the component of the weight down the slope reduces the deceleration. The deceleration $3.365\,\text{m/s}^2$ is still positive, because $\mu = 0.45 > \tan 6.0^\circ = 0.11$.

## fy4-6-L3-05
**Given:** $m = 20\,\text{kg}$, $\alpha = 30^\circ$, $\mu = 0.35$, the box starts from rest, $t = 3.0\,\text{s}$; in the student's solution $N = mg$ and the result $1.5\,\text{m/s}^2$; $g = 9.81\,\text{m/s}^2$
**Find:** the student's error, the correct acceleration $a$ and the distance $s$ in the time $3.0\,\text{s}$ in $\text{m}$
**Principle:** The student used the whole weight as the normal force, $N = mg$. On a slope only the weight and the normal force act perpendicular to the surface, and the box does not accelerate in that direction, so $N = mg\cos\alpha$, which is smaller than the weight. The student's friction $\mu mg$ is therefore too large and the acceleration too small. The correct acceleration is obtained from Newton's second law along the slope, and the distance from the equation of uniformly accelerated motion with the initial velocity zero.
**Free-body diagram:** The box as a rectangle along the slope, $x$ down the slope and $y$ perpendicular to the surface, outward. The weight $\overline{G}$ straight down and its components dashed, the normal force $\overline{N}$ perpendicular to the surface, outward, and shorter than the weight, the kinetic friction $\overline{F}_\mu$ up the slope. The acceleration is drawn separately down the slope.
```voimakuvio
pinta -30
G 196,2
N 169,9
F_mu 59,47 ylös
a alas
akselit -30
komponentit G
```
**Formula:** $y$: $N - mg\cos\alpha = 0$ and $x$: $mg\sin\alpha - \mu N = ma$, so $a = g(\sin\alpha - \mu\cos\alpha)$. The distance is $s = \tfrac{1}{2}at^2$, because the initial velocity is zero
**Conversions:** All quantities are in SI units, so no conversions are needed, and the mass cancels.
**Substitution:** $a = 9.81\,\text{m/s}^2\cdot(\sin 30^\circ - 0.35\cdot\cos 30^\circ) = 1.931\,\text{m/s}^2$ and
```latex
\begin{aligned}
s &= \tfrac{1}{2} \cdot 1.931\,\text{m/s}^2 \cdot (3.0\,\text{s})^2 \\
&= 8.69\,\text{m}
\end{aligned}
```
**Answer:** the student's error is $N = mg$ on a slope, the correct normal force is $N = mg\cos\alpha \approx 170\,\text{N}$ and the correct acceleration $a \approx 1.9\,\text{m/s}^2$. The box slides a distance of $8.7\,\text{m}$ in the time $3.0\,\text{s}$, two significant figures like the coefficient of friction $0.35$ and the time $3.0\,\text{s}$.
**Reasonableness:** The student's acceleration $1.5\,\text{m/s}^2$ is too small, because the friction $\mu mg = 69\,\text{N}$ was calculated too large; the correct friction is $\mu mg\cos\alpha = 59\,\text{N}$. Without friction the acceleration would be $g\sin 30^\circ \approx 4.9\,\text{m/s}^2$, so friction reduces it. The box accelerates down while sliding, because $\tan 30^\circ = 0.58 > \mu = 0.35$; according to the problem it starts to move, so $\mu_0 < \tan 30^\circ$.
