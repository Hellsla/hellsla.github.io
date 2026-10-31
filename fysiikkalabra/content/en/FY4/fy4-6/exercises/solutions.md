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
