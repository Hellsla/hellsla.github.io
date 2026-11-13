## fy4-13-L1-01
**Given:** $m = 1.5\,\text{kg}$, tension in the string $T = 3.0\,\text{N}$ horizontally; friction is neglected
**Find:** the acceleration $a$ of the cart in $\text{m/s}^2$
**Principle:** The cart accelerates horizontally, so by Newton's second law the sum of the horizontal forces is mass times acceleration. The cart does not accelerate vertically, so the forces there cancel.
**Free-body diagram:** The cart as a rectangle, with $x$ along the string. Weight $\overline{G}$ down and normal force $\overline{N}$ from the table up, equally long. Tension $\overline{T}$ horizontally forward. In the horizontal direction only $\overline{T}$ acts.
```voimakuvio
pinta 0
G 14,715
N 14,715
T 3,0 oikea
a oikea
akselit 0
```
**Formula:** $T = ma$, so $a = \dfrac{T}{m}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{3.0\,\text{N}}{1.5\,\text{kg}} = 2.0\,\text{m/s}^2$
**Answer:** $2.0\,\text{m/s}^2$, two significant figures like the data $3.0\,\text{N}$ and $1.5\,\text{kg}$.
**Reasonableness:** One newton gives a one-kilogram body an acceleration of $1\,\text{m/s}^2$. A force of $3.0\,\text{N}$ and a mass of $1.5\,\text{kg}$ give twice that, and the product $1.5\,\text{kg} \cdot 2.0\,\text{m/s}^2 = 3.0\,\text{N}$ gives back the force.

## fy4-13-L1-02
**Given:** $m = 0.60\,\text{kg}$, downward acceleration $a = 2.0\,\text{m/s}^2$, $g = 9.81\,\text{m/s}^2$; air resistance is neglected
**Find:** the tension $T$ in the string in $\text{N}$
**Principle:** The mass accelerates downward, so by Newton's second law its net force points down and equals $ma$. The Earth and the string act on it.
**Free-body diagram:** The mass as a rectangle, positive direction down. Weight $\overline{G}$ down from the centre and tension $\overline{T}$ up from the top surface. The arrow $\overline{G}$ is longer, because the net force points down.
```voimakuvio
G 5,886
T 4,686 ylös
a alas
```
**Formula:** $mg - T = ma$, so $T = m(g - a)$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $T = 0.60\,\text{kg} \cdot (9.81\,\text{m/s}^2 - 2.0\,\text{m/s}^2) = 0.60\,\text{kg} \cdot 7.81\,\text{m/s}^2 = 4.686\,\text{N}$
**Answer:** $4.7\,\text{N}$, two significant figures like the mass $0.60\,\text{kg}$ and the acceleration $2.0\,\text{m/s}^2$.
**Reasonableness:** The weight of the mass is $0.60\,\text{kg} \cdot 9.81\,\text{m/s}^2 \approx 5.9\,\text{N}$, and $4.7\,\text{N}$ is smaller than that, because the mass accelerates downward. The difference $1.2\,\text{N}$ is $ma = 0.60\,\text{kg} \cdot 2.0\,\text{m/s}^2$.

## fy4-13-L1-03
**Given:** cart $m_1 = 1.0\,\text{kg}$, hanging mass $m_2 = 0.40\,\text{kg}$, $g = 9.81\,\text{m/s}^2$; friction and air resistance are neglected, the string is light and inextensible, the pulley is light and frictionless
**Find:** the tension $T$ in the string in $\text{N}$
**Principle:** There are two bodies, so each gets its own equation of motion. The string is inextensible, so the acceleration magnitude $a$ is the same, and a light string and a frictionless pulley pass the force on unchanged, so the string pulls both bodies with the force $T$.
**Free-body diagram:** The cart as a rectangle, positive direction to the right: $\overline{G}_1$ and $\overline{N}$ cancel, and in the horizontal direction $\overline{T}_1$ acts. The hanging mass as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up.
```voimakuvio
pinta 0
G_1 9,81
N 9,81
T_1 2,803 oikea
a oikea
---
G_2 3,924
T_2 2,803 ylös
a alas
```
**Formula:** $T = m_1 a$ and $m_2 g - T = m_2 a$. Adding gives $m_2 g = (m_1 + m_2)\,a$, so $a = \dfrac{m_2 g}{m_1 + m_2}$, and $T = m_1 a$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{0.40\,\text{kg} \cdot 9.81\,\text{m/s}^2}{1.4\,\text{kg}} = 2.803\,\text{m/s}^2$ and $T = 1.0\,\text{kg} \cdot 2.803\,\text{m/s}^2 = 2.803\,\text{N}$
**Answer:** $2.8\,\text{N}$, two significant figures like the masses $1.0\,\text{kg}$ and $0.40\,\text{kg}$.
**Reasonableness:** The tension is smaller than the weight of the hanging mass $m_2 g = 3.9\,\text{N}$, because the mass accelerates downward. The acceleration $a = T : m_1 \approx 2.8\,\text{m/s}^2$ is smaller than $g$, and the difference $3.9\,\text{N} - 2.8\,\text{N} = 1.1\,\text{N}$ is $m_2 a = 0.40\,\text{kg} \cdot 2.8\,\text{m/s}^2$.

## fy4-13-L1-04
**Given:** two bodies, each of mass $m = 3.0\,\text{kg}$, at rest; $g = 9.81\,\text{m/s}^2$; the string is light, the pulley is light and frictionless
**Find:** the tension $T$ in the string in $\text{N}$
**Principle:** The body is at rest, so by Newton's second law the sum of the forces on it is zero. The free-body diagram of one body is enough, because the string is light and pulls both bodies with equally large forces.
**Free-body diagram:** The body as a rectangle, positive direction up. Weight $\overline{G}$ down from the centre and tension $\overline{T}$ up from the top surface. The arrows are equally long.
```voimakuvio
G 29,43
T 29,43 ylös
a 0
```
**Formula:** $T - mg = 0$, so $T = mg$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $T = 3.0\,\text{kg} \cdot 9.81\,\text{m/s}^2 = 29.43\,\text{N}$
**Answer:** $29\,\text{N}$, two significant figures like the mass $3.0\,\text{kg}$.
**Reasonableness:** The tension is the weight of one body, not the sum $59\,\text{N}$ of the weights of both: the string holds up each body from its end with one force. If one body were replaced by a hook fixed to a wall, the string would carry the same force.

## fy4-13-L1-05
**Given:** carts $m_1 = 1.0\,\text{kg}$ and $m_2 = 2.0\,\text{kg}$, pulling force $F = 12\,\text{N}$ on the lighter cart; friction is neglected
**Find:** the common acceleration $a$ of the carts in $\text{m/s}^2$
**Principle:** The carts move together with the same acceleration magnitude. Each cart gets its own equation of motion, and when they are added, the internal force $T$ in the string cancels.
**Free-body diagram:** The lighter cart as a rectangle, positive direction toward the pull: horizontally the pulling force $\overline{F}$ forward and the tension $\overline{T}_1$ backward. The heavier cart as a rectangle: horizontally only $\overline{T}_2$ forward. Weight and normal force cancel in both.
```voimakuvio
pinta 0
G_1 9,81
N_1 9,81
F 12 oikea
T_1 8,0 vasen
a oikea
---
pinta 0
G_2 19,62
N_2 19,62
T_2 8,0 oikea
a oikea
```
**Formula:** $F - T = m_1 a$ and $T = m_2 a$. Adding gives $F = (m_1 + m_2)\,a$, so $a = \dfrac{F}{m_1 + m_2}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{12\,\text{N}}{1.0\,\text{kg} + 2.0\,\text{kg}} = 4.0\,\text{m/s}^2$
**Answer:** $4.0\,\text{m/s}^2$, two significant figures like the data.
**Reasonableness:** The tension is $T = m_2 a = 2.0\,\text{kg} \cdot 4.0\,\text{m/s}^2 = 8.0\,\text{N}$, and the lighter cart is left with $F - T = 4.0\,\text{N} = m_1 a$. The acceleration is the same as if a body of $3.0\,\text{kg}$ were pulled with a force of $12\,\text{N}$.

## fy4-13-L2-01
**Given:** upper crate $m_1 = 50\,\text{kg}$, lower crate $m_2 = 30\,\text{kg}$, upward acceleration $a = 1.2\,\text{m/s}^2$, $g = 9.81\,\text{m/s}^2$; the ropes are light and inextensible, air resistance is neglected
**Find:** the tension $T_1$ in the crane's rope in $\text{N}$
**Principle:** The crates are two bodies, and each gets its own equation of motion. The lower crate hangs from the upper one, so they have the same acceleration $a$. The force of a light rope is the same at both ends of the rope, so the lower rope pulls the upper crate down with the same force $T_2$ with which it pulls the lower crate up.
**Free-body diagram:** The upper crate as a rectangle, positive direction up: the crane rope's $\overline{T}_1$ up from the top surface, weight $\overline{G}_1$ down from the centre and the lower rope's $\overline{T}_2$ down from the bottom surface. The lower crate as a rectangle: $\overline{T}_2$ up from the top surface and weight $\overline{G}_2$ down. The arrow $\overline{T}_1$ is the longest.
```voimakuvio
T_1 880,8 ylös
G_1 490,5
T_2 330,3 alas @ala
a ylös
---
T_2 330,3 ylös
G_2 294,3
a ylös
```
**Formula:** $T_1 - T_2 - m_1 g = m_1 a$ and $T_2 - m_2 g = m_2 a$, so adding gives $T_1 = (m_1 + m_2)(g + a)$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $T_1 = (50\,\text{kg} + 30\,\text{kg}) \cdot (9.81\,\text{m/s}^2 + 1.2\,\text{m/s}^2) = 80\,\text{kg} \cdot 11.01\,\text{m/s}^2 = 880.8\,\text{N}$
**Answer:** $880\,\text{N}$, that is $8.8 \cdot 10^{2}\,\text{N}$, two significant figures like the acceleration $1.2\,\text{m/s}^2$ and the mass $30\,\text{kg}$.
**Reasonableness:** The combined weight of the crates is $80\,\text{kg} \cdot 9.81\,\text{m/s}^2 \approx 785\,\text{N}$, and lifting with acceleration needs more. The excess $96\,\text{N}$ is $(m_1 + m_2)\,a = 80\,\text{kg} \cdot 1.2\,\text{m/s}^2$. The force in the lower rope is $T_2 = m_2 (g + a) \approx 330\,\text{N}$, smaller than $T_1$, because it carries only the lower crate.

## fy4-13-L2-02
**Given:** $m_1 = 0.50\,\text{kg}$ and $m_2 = 1.0\,\text{kg}$ at the ends of the string, $g = 9.81\,\text{m/s}^2$; the string is light, the pulley is light and frictionless, air resistance is neglected
**Find:** the tension $T$ in the string in $\text{N}$
**Principle:** Each body gets its own equation of motion. The heavier body $m_2$ goes down and the lighter body $m_1$ goes up with the same acceleration magnitude $a$, because the string is inextensible, and the string pulls both with the force $T$.
**Free-body diagram:** The lighter body as a rectangle, positive direction up: $\overline{T}_1$ up and $\overline{G}_1$ down. The heavier body as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up.
```voimakuvio
G_1 4,905
T_1 6,54 ylös
a ylös
---
G_2 9,81
T_2 6,54 ylös
a alas
```
**Formula:** $T - m_1 g = m_1 a$ and $m_2 g - T = m_2 a$, so adding gives $a = \dfrac{(m_2 - m_1)\,g}{m_1 + m_2}$ and $T = m_1 (g + a) = \dfrac{2 m_1 m_2}{m_1 + m_2}\cdot g$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $T = \dfrac{2 \cdot 0.50\,\text{kg} \cdot 1.0\,\text{kg}}{0.50\,\text{kg} + 1.0\,\text{kg}} \cdot 9.81\,\text{m/s}^2 = 0.6667\,\text{kg} \cdot 9.81\,\text{m/s}^2 = 6.54\,\text{N}$
**Answer:** $6.5\,\text{N}$, two significant figures like the masses $0.50\,\text{kg}$ and $1.0\,\text{kg}$.
**Reasonableness:** The weights are $m_1 g \approx 4.9\,\text{N}$ and $m_2 g \approx 9.8\,\text{N}$, and $6.5\,\text{N}$ lies between them: $T > G_1$ for the rising body and $T < G_2$ for the descending one. The acceleration $a = 3.27\,\text{m/s}^2$ gives the same forces: $T - G_1 = 1.635\,\text{N} = m_1 a$.

## fy4-13-L2-03
**Given:** sleds $m_1 = 3.0\,\text{kg}$ (the one being pulled) and $m_2 = 2.0\,\text{kg}$, pulling force $F = 20\,\text{N}$; friction and air resistance are neglected, the ropes are light and inextensible
**Find:** the tension $T$ in the rope between the sleds in $\text{N}$
**Principle:** The sleds move together with the same acceleration magnitude $a$. Each sled gets its own equation of motion; the rear sled is pulled only by the rope between the sleds.
**Free-body diagram:** The heavier sled as a rectangle, positive direction toward the pull: the pulling force $\overline{F}$ forward and the tension $\overline{T}_1$ backward. The lighter sled as a rectangle: horizontally only $\overline{T}_2$ forward. Weight and normal force cancel in both.
```voimakuvio
pinta 0
G_1 29,43
N_1 29,43
F 20 oikea
T_1 8,0 vasen
a oikea
---
pinta 0
G_2 19,62
N_2 19,62
T_2 8,0 oikea
a oikea
```
**Formula:** $F - T = m_1 a$ and $T = m_2 a$. Adding gives $a = \dfrac{F}{m_1 + m_2}$, so $T = m_2 a = \dfrac{m_2}{m_1 + m_2}\,F$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $T = \dfrac{2.0\,\text{kg}}{3.0\,\text{kg} + 2.0\,\text{kg}} \cdot 20\,\text{N} = 0.40 \cdot 20\,\text{N} = 8.0\,\text{N}$
**Answer:** $8.0\,\text{N}$, two significant figures like the data.
**Reasonableness:** The force in the rope is smaller than the pulling force $20\,\text{N}$, because it accelerates only the rear sled. The acceleration is $a = 20\,\text{N} : 5.0\,\text{kg} = 4.0\,\text{m/s}^2$, and the front sled is left with $20\,\text{N} - 8.0\,\text{N} = 12\,\text{N} = m_1 a$.

## fy4-13-L2-04
**Given:** mass of the lighter body $m_1 = 0.60\,\text{kg}$, downward acceleration of the heavier one $a = 2.0\,\text{m/s}^2$, $g = 9.81\,\text{m/s}^2$; the string is light, the pulley is light and frictionless, air resistance is neglected
**Find:** the mass $m_2$ of the heavier body in $\text{kg}$
**Principle:** There are two bodies, and each gets its own equation of motion. The string is inextensible, so the acceleration magnitude $a$ is the same, and the light string pulls both with the force $T$. The lighter body goes up and the heavier one goes down.
**Free-body diagram:** The lighter body as a rectangle, positive direction up: $\overline{T}_1$ up and $\overline{G}_1$ down, with $\overline{T}_1$ longer. The heavier body as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up, with $\overline{G}_2$ longer.
```voimakuvio
G_1 5,886
T_1 7,086 ylös
a ylös
---
G_2 8,901
T_2 7,086 ylös
a alas
```
**Formula:** $T - m_1 g = m_1 a$ and $m_2 g - T = m_2 a$. The first gives $T = m_1 (g + a)$, and the second gives $m_2 (g - a) = T$, so $m_2 = \dfrac{m_1 (g + a)}{g - a}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $m_2 = \dfrac{0.60\,\text{kg} \cdot (9.81 + 2.0)\,\text{m/s}^2}{(9.81 - 2.0)\,\text{m/s}^2} = \dfrac{7.086\,\text{N}}{7.81\,\text{m/s}^2} = 0.9073\,\text{kg}$
**Answer:** $0.91\,\text{kg}$, two significant figures like the mass $0.60\,\text{kg}$ and the acceleration $2.0\,\text{m/s}^2$.
**Reasonableness:** The mass $0.91\,\text{kg}$ is greater than $0.60\,\text{kg}$, as it must be for the heavier body. Check with the formula $a = \dfrac{(m_2 - m_1)\,g}{m_1 + m_2} = \dfrac{0.3073 \cdot 9.81}{1.5073}\,\text{m/s}^2 \approx 2.0\,\text{m/s}^2$, and the tension $T = 7.09\,\text{N}$ lies between the weights $5.9\,\text{N}$ and $8.9\,\text{N}$.

## fy4-13-L3-01
**Given:** mass of the cabin $m_1 = 800\,\text{kg}$, mass of the counterweight $m_2 = 1200\,\text{kg}$, $g = 9.81\,\text{m/s}^2$; the rope is light and inextensible, the wheel is light and frictionless, air resistance is neglected
**Find:** the force $F_\text{axle}$ that the rope exerts on the axle of the wheel, in $\text{N}$
**Principle:** The cabin and the counterweight are two bodies, and each gets its own equation of motion. The rope is inextensible, so $a$ is the same for both, and the light rope pulls both with the force $T$. The wheel is light and does not accelerate, so its net force is zero.
**Free-body diagram:** The cabin as a rectangle, positive direction up: $\overline{T}_1$ up and $\overline{G}_1$ down. The counterweight as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up. The arrows $\overline{T}_1$ and $\overline{T}_2$ are equally long. On the wheel: two forces $T$ down and $F_\text{axle}$ up.
```voimakuvio
G_1 7848
T_1 9418 ylös
a ylös
---
G_2 1,177e+04
T_2 9418 ylös
a alas
```
**Formula:** $T - m_1 g = m_1 a$ and $m_2 g - T = m_2 a$, so $T = \dfrac{2 m_1 m_2}{m_1 + m_2}\cdot g$. From the equilibrium of the wheel, $F_\text{axle} - 2T = 0$, so $F_\text{axle} = 2T$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $T = \dfrac{2 \cdot 800\,\text{kg} \cdot 1200\,\text{kg}}{800\,\text{kg} + 1200\,\text{kg}} \cdot 9.81\,\text{m/s}^2 = 960\,\text{kg} \cdot 9.81\,\text{m/s}^2 = 9418\,\text{N}$ and $F_\text{axle} = 2 \cdot 9418\,\text{N} = 18\,835\,\text{N}$
**Answer:** $19000\,\text{N}$, that is $19\,\text{kN}$, two significant figures, because the masses are given to the nearest hundred kilograms.
**Reasonableness:** The weights are $m_1 g \approx 7850\,\text{N}$ and $m_2 g \approx 11\,770\,\text{N}$, and $T = 9418\,\text{N}$ lies between them. The force on the axle, $18\,835\,\text{N}$, is smaller than the sum of the weights, $19\,620\,\text{N}$, because the counterweight accelerates downward.

## fy4-13-L3-02
**Given:** cart $m_1 = 1.0\,\text{kg}$, greatest allowed tension $T_{\max} = 3.0\,\text{N}$, $g = 9.81\,\text{m/s}^2$; friction is neglected, the string and the pulley are light
**Find:** the greatest mass $m_2$ of the hanging mass in $\text{kg}$
**Principle:** The bodies get their own equations of motion, and from them the tension is obtained as a function of the masses. The tension increases as the mass of the hanging mass increases, so the limiting value $T = T_{\max}$ gives the greatest mass.
**Free-body diagram:** The cart as a rectangle, positive direction to the right: horizontally only $\overline{T}_1$. The hanging mass as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up.
```voimakuvio
pinta 0
G_1 9,81
N 9,81
T_1 3 oikea
a oikea
---
G_2 4,321
T_2 3 ylös
a alas
```
**Formula:** $T = m_1 a$ and $m_2 g - T = m_2 a$, so $T = \dfrac{m_1 m_2}{m_1 + m_2}\,g$. When $T = T_{\max}$: $T_{\max} (m_1 + m_2) = m_1 m_2 g$, so $m_2 = \dfrac{m_1\,T_{\max}}{g\,m_1 - T_{\max}}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $m_2 = \dfrac{3.0\,\text{N} \cdot 1.0\,\text{kg}}{1.0\,\text{kg} \cdot 9.81\,\text{m/s}^2 - 3.0\,\text{N}} = \dfrac{3.0\,\text{N}\cdot\text{kg}}{6.81\,\text{N}} = 0.4405\,\text{kg}$
**Answer:** $0.44\,\text{kg}$, two significant figures like the data $3.0\,\text{N}$ and $1.0\,\text{kg}$.
**Reasonableness:** Check: $T = \dfrac{1.0 \cdot 0.4405}{1.4405} \cdot 9.81\,\text{N} \approx 3.0\,\text{N}$. With a hanging mass heavier than the limit, $T$ is greater, but always below the weight of the cart $9.81\,\text{N}$, because $T$ approaches $m_1 g$ only for an infinitely large $m_2$.

## fy4-13-L3-03
**Given:** cart $m_1 = 1.5\,\text{kg}$, hanging mass $m_2 = 0.50\,\text{kg}$, distance $s = 0.90\,\text{m}$, starting from rest, $g = 9.81\,\text{m/s}^2$; friction is neglected, the string and the pulley are light
**Find:** the time $t$ in $\text{s}$
**Principle:** First the equations of motion of the bodies give the acceleration. The acceleration is constant, so for motion from rest $s = \tfrac{1}{2}at^2$, which gives the time.
**Free-body diagram:** The cart as a rectangle, positive direction to the right: horizontally only $\overline{T}_1$. The hanging mass as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up, and $T_1 = T_2 = T$.
```voimakuvio
pinta 0
G_1 14,71
N 14,71
T_1 3,679 oikea
a oikea
---
G_2 4,905
T_2 3,679 ylös
a alas
```
**Formula:** $T = m_1 a$ and $m_2 g - T = m_2 a$, so $a = \dfrac{m_2 g}{m_1 + m_2}$. From the distance $s = \tfrac{1}{2}at^2$, so $t = \sqrt{\dfrac{2s}{a}}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{0.50\,\text{kg} \cdot 9.81\,\text{m/s}^2}{2.0\,\text{kg}} = 2.4525\,\text{m/s}^2$ and $t = \sqrt{\dfrac{2 \cdot 0.90\,\text{m}}{2.4525\,\text{m/s}^2}} = 0.857\,\text{s}$
**Answer:** $0.86\,\text{s}$, two significant figures like the data $0.90\,\text{m}$ and $0.50\,\text{kg}$.
**Reasonableness:** Check: the final speed is $at \approx 2.1\,\text{m/s}$ and the average speed $1.05\,\text{m/s}$, so $1.05\,\text{m/s} \cdot 0.857\,\text{s} \approx 0.90\,\text{m}$. A freely falling mass ($a = g$) would cover the same distance in $0.43\,\text{s}$, so $0.86\,\text{s}$ is sensibly longer.

## fy4-13-L1-06
**Find:** how the tension $T$ in the string and the weight $G_2$ of the hanging mass are related when the mass descends with an acceleration.
**Principle:** By Newton's second law the net force on a body points in the direction of its acceleration. The hanging mass accelerates downward, so its net force points down. Only the weight, down, and the tension in the string, up, act on the hanging mass.
**Model answer:** For the hanging mass, $G_2 - T = m_2 a$, and because $a > 0$ downward, $G_2 - T > 0$. So the tension is smaller than the weight of the hanging mass. The string does not support the whole weight, because the mass accelerates downward and is not at rest. The string cannot pull harder than the weight either, because then the net force on the hanging mass would point up and the mass would not descend. The string pulls the cart and the hanging mass with the same force $T$, so it does not share its force in halves: the difference from the weight is always $m_2 a$.

## fy4-13-L1-07
**Given:** $m_1 = 0.30\,\text{kg}$ and $m_2 = 0.70\,\text{kg}$ at the ends of the string, $g = 9.81\,\text{m/s}^2$; the string is light and inextensible, the pulley is light and frictionless, air resistance is neglected
**Find:** the common acceleration $a$ of the bodies in $\text{m/s}^2$
**Principle:** Each body gets its own equation of motion. The string is inextensible, so the accelerations of the bodies have the same magnitude $a$, and the light string pulls both with the force $T$. The heavier body descends and the lighter one rises.
**Free-body diagram:** The lighter body as a rectangle, positive direction up: $\overline{T}_1$ up and $\overline{G}_1$ down. The heavier body as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up. The arrow $\overline{T}$ is shorter than $\overline{G}_2$ and longer than $\overline{G}_1$.
```voimakuvio
G_1 2,943
T_1 4,12 ylös
a ylös
---
G_2 6,867
T_2 4,12 ylös
a alas
```
**Formula:** $T - m_1 g = m_1 a$ and $m_2 g - T = m_2 a$. Adding eliminates $T$: $(m_2 - m_1)\,g = (m_1 + m_2)\,a$, so $a = \dfrac{(m_2 - m_1)\,g}{m_1 + m_2}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{(0.70\,\text{kg} - 0.30\,\text{kg}) \cdot 9.81\,\text{m/s}^2}{0.30\,\text{kg} + 0.70\,\text{kg}} = \dfrac{0.40 \cdot 9.81}{1.00}\,\text{m/s}^2 = 3.924\,\text{m/s}^2$
**Answer:** $3.9\,\text{m/s}^2$, two significant figures like the masses $0.30\,\text{kg}$ and $0.70\,\text{kg}$.
**Reasonableness:** The acceleration is smaller than $g = 9.81\,\text{m/s}^2$, because the lighter body slows down the heavier one. The tension $T = m_1 (g + a) = 0.30\,\text{kg} \cdot 13.73\,\text{m/s}^2 = 4.12\,\text{N}$ gives the heavier body $m_2 g - T = 6.87\,\text{N} - 4.12\,\text{N} = 2.75\,\text{N} = m_2 a$.

## fy4-13-L1-08
**Find:** which forces act on the cart in the direction of the table when the hanging mass descends on the string.
**Principle:** The free-body diagram of a body includes only the forces that act on that very body. Every force arises from an interaction: in the direction of the table only the string touches the cart. The weight of the cart and the normal force from the table are vertical.
**Model answer:** The weight of the hanging mass is the force of the Earth on the hanging mass, and it belongs in the free-body diagram of the hanging mass. The string transmits the effect of the hanging mass to the cart as the tension $T$, and that is the only force on the cart along the table. The equation of motion of the cart along the table is therefore $T = m_1 a$. The cart moves forward, but motion is not a force, and kinetic energy is not drawn in a free-body diagram. Because the hanging mass accelerates downward, the tension is smaller than the weight of the hanging mass: $T < m_2 g$.

## fy4-13-L2-05
**Given:** total mass of the masses $M = 0.500\,\text{kg}$; from the table $\Delta m = 50$; $100$; $150$; $200$ and $250\,\text{g}$ and $a = 0.96$; $2.02$; $2.88$; $3.97$ and $4.84\,\text{m/s}^2$ (example data)
**Find:** a) a formula for $a$ using the mass difference $\Delta m$; b) the acceleration of free fall $g$ in $\text{m/s}^2$
**Principle:** Each mass gets its own equation of motion. The string is inextensible and light, so the magnitude of the acceleration $a$ and the tension $T$ are the same for both masses. When the equations are added, $T$ cancels and a direct proportionality $a \propto \Delta m$ remains. The slope of the line gives $g$.
**Reading the graph:** The points $(\Delta m, a)$ lie almost on a straight line through the origin; individual points deviate from it by at most about $0.1\,\text{m/s}^2$, which is random variation of the measurement. The fitted line through the origin hits the value $a = 4.9\,\text{m/s}^2$ at the last point, where $\Delta m = 0.250\,\text{kg}$, so the slope is $k = \dfrac{4.9\,\text{m/s}^2}{0.250\,\text{kg}} = 19.6\,\dfrac{\text{m/s}^2}{\text{kg}}$.
**Formula:** The lighter $m_1$ rises and the heavier $m_2$ descends: $T - m_1 g = m_1 a$ and $m_2 g - T = m_2 a$. Adding gives $(m_2 - m_1)\,g = (m_1 + m_2)\,a$, so $a = \dfrac{g}{M}\,\Delta m$. The slope is $k = \dfrac{g}{M}$, so $g = k\,M$
**Conversions:** $\Delta m = 250\,\text{g} = 0.250\,\text{kg}$; the other quantities are in SI units.
**Substitution:** $g = 19.6\,\dfrac{\text{m/s}^2}{\text{kg}} \cdot 0.500\,\text{kg} = 9.8\,\text{m/s}^2$
**Answer:** $9.8\,\text{m/s}^2$, two significant figures, because the slope of a line fitted by hand is obtained only to two figures.
**Reasonableness:** The result is close to the known value $9.81\,\text{m/s}^2$. The ratios $a : \Delta m$ of the points are $19.2$; $20.2$; $19.2$; $19.9$ and $19.4$ in the unit $\dfrac{\text{m/s}^2}{\text{kg}}$, so all are close to $19.6$. By the formula, $\Delta m = 250\,\text{g}$ gives $a = \dfrac{0.250 \cdot 9.81}{0.500}\,\text{m/s}^2 = 4.9\,\text{m/s}^2$, which is smaller than $g$, as it should be.

## fy4-13-L2-06
**Given:** mass of the cart $m_1 = 1.20\,\text{kg}$; from the measurement in which the hanging mass is $m_2 = 0.50\,\text{kg}$, the acceleration $a = 2.84\,\text{m/s}^2$ (example data); $g = 9.81\,\text{m/s}^2$; friction is neglected, the string and the pulley are light
**Find:** the tension $T$ in the string in $\text{N}$
**Principle:** In the direction of the table only the string acts on the cart, so its equation of motion gives $T$ directly from the measured acceleration. As a check, $T$ is calculated from the same measurement using the equation of motion of the hanging mass, where $T$ is opposite in direction to the weight.
**Reading the graph:** The row $m_2 = 0.50\,\text{kg}$ of the table gives $a = 2.84\,\text{m/s}^2$. The acceleration grows as the hanging mass grows, but not in direct proportion: the mass becomes five times as large ($0.10\,\text{kg} \to 0.50\,\text{kg}$), but the acceleration becomes only four times as large ($0.74 \to 2.84\,\text{m/s}^2$).
**Free-body diagram:** The cart as a rectangle, positive direction along the string: $\overline{G}_1$ and $\overline{N}$ cancel, and in the horizontal direction only $\overline{T}_1$ acts. The hanging mass as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up.
```voimakuvio
pinta 0
G_1 11,77
N 11,77
T_1 3,41 oikea
a oikea
---
G_2 4,905
T_2 3,41 ylös
a alas
```
**Formula:** Cart: $T = m_1 a$. Hanging mass: $m_2 g - T = m_2 a$, so the check is $T = m_2\,(g - a)$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $T = 1.20\,\text{kg} \cdot 2.84\,\text{m/s}^2 = 3.408\,\text{N}$. Check: $T = 0.50\,\text{kg} \cdot (9.81\,\text{m/s}^2 - 2.84\,\text{m/s}^2) = 0.50\,\text{kg} \cdot 6.97\,\text{m/s}^2 = 3.485\,\text{N}$
**Answer:** $3.4\,\text{N}$, two significant figures, because the two equations give $3.41\,\text{N}$ and $3.49\,\text{N}$, which differ by about $2\,\%$, so only the first two figures are reliable.
**Reasonableness:** The two ways give $3.4\,\text{N}$ and $3.5\,\text{N}$, so they differ by about $2\,\%$, which fits the precision of the measurement. By theory, $a = \dfrac{0.50 \cdot 9.81}{1.70}\,\text{m/s}^2 = 2.89\,\text{m/s}^2$, so the measured $2.84\,\text{m/s}^2$ is slightly smaller. The tension is smaller than the weight of the hanging mass $4.9\,\text{N}$, as it should be.

## fy4-13-L2-07
**Given:** cart $m_1 = 2.0\,\text{kg}$, hanging mass $m_2 = 0.50\,\text{kg}$, $g = 9.81\,\text{m/s}^2$; friction and air resistance are neglected, the string and the pulley are light; the student's result $2.5\,\text{m/s}^2$
**Find:** the error in the student's solution and the correct acceleration $a$ in $\text{m/s}^2$
**Principle:** Each body gets its own equation of motion, and the acceleration accelerates the whole system: both the cart and the hanging mass. The student's equations $T = m_1 a$ and $m_2 g - T = m_2 a$ are correct, but the solution contains an error.
**Free-body diagram:** The cart as a rectangle, positive direction to the right: $\overline{G}_1$ and $\overline{N}$ cancel, and in the horizontal direction only $\overline{T}_1$ acts. The hanging mass as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up.
```voimakuvio
pinta 0
G_1 19,62
N 19,62
T_1 3,924 oikea
a oikea
---
G_2 4,905
T_2 3,924 ylös
a alas
```
**Formula:** The error: after the substitution the equation is $m_2 g - m_1 a = m_2 a$, and the mass of the hanging mass also belongs in the denominator: $m_2 g = m_1 a + m_2 a = (m_1 + m_2)\,a$. The student forgot the mass of the hanging mass, that is, the mass $m_1 + m_2$ of the whole moving system. Correctly, $a = \dfrac{m_2 g}{m_1 + m_2}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** $a = \dfrac{0.50\,\text{kg} \cdot 9.81\,\text{m/s}^2}{2.0\,\text{kg} + 0.50\,\text{kg}} = \dfrac{4.905\,\text{N}}{2.5\,\text{kg}} = 1.962\,\text{m/s}^2$
**Answer:** $2.0\,\text{m/s}^2$, two significant figures like the data $2.0\,\text{kg}$ and $0.50\,\text{kg}$. The student's result was too large, because the student divided only by the mass of the cart.
**Reasonableness:** The tension $T = m_1 a = 2.0\,\text{kg} \cdot 1.962\,\text{m/s}^2 = 3.92\,\text{N}$ is smaller than the weight of the hanging mass $4.9\,\text{N}$, and the difference $0.98\,\text{N}$ is $m_2 a = 0.50\,\text{kg} \cdot 1.962\,\text{m/s}^2$. With the student's value $a = 2.45\,\text{m/s}^2$ we would have $T = m_1 a = 4.9\,\text{N}$ and $m_2 g - T \approx 0$, but the equation of motion of the hanging mass would require $m_2 a = 1.2\,\text{N}$, so the value is wrong.

## fy4-13-L3-04
**Given:** masses of the cars $m_1 = 24\,\text{t}$, $m_2 = 18\,\text{t}$ and $m_3 = 12\,\text{t}$; from the table the speed $v = 0$ at $t = 0$ and $v = 10.02\,\text{m/s}$ at $t = 20.0\,\text{s}$ (example data); greatest permitted force of the coupling $20\,\text{kN}$; resistive forces are neglected
**Find:** a) the acceleration $a$ of the train; b) the force $K_{12}$ of the coupling between cars 1 and 2 in $\text{kN}$; c) the force of the coupling when the cars are in the order $12\,\text{t}$, $18\,\text{t}$, $24\,\text{t}$, and whether the coupling holds
**Principle:** The cars are coupled, so they move together with the same acceleration $a$. Each car gets its own equation of motion. The coupling between cars 1 and 2 pulls car 2 forward, and the cars 2 and 3 behind it resist it, so the force of the coupling accelerates all the cars behind it. By the third law, car 2 pulls car 1 backward with an equally large force.
**Reading the graph:** The speed grows steadily by about $2.5\,\text{m/s}$ in each five-second interval ($2.46$; $2.57$; $2.45$; $2.54\,\text{m/s}$), so the $(t, v)$ graph is almost a straight line and the acceleration is constant. The slope from the end points is $a = \dfrac{10.02\,\text{m/s} - 0}{20.0\,\text{s} - 0} = 0.50\,\text{m/s}^2$.
**Free-body diagram:** The force of the locomotive is marked $\overline{F}$. Car 3 as a rectangle, positive direction in the direction of motion of the train: horizontally only the coupling force $\overline{K}_{23}$ forward. Car 2: $\overline{K}_{12}$ forward and $\overline{K}_{23}$ backward. Car 1: the force of the locomotive forward and $\overline{K}_{12}$ backward. In each car the weight and the normal force cancel (in the figure the vertical arrows are drawn shortened). The arrows $\overline{K}_{12}$ are equally long in cars 1 and 2, and the arrows $\overline{K}_{23}$ are equally long in cars 2 and 3 (third law), and $\overline{K}_{12}$ is longer than $\overline{K}_{23}$.
```voimakuvio
pinta 0
G_1 30
N 30
F 27 oikea
K_12 15 vasen
a oikea
```
```voimakuvio
pinta 0
G_2 22
N 22
K_12 15 oikea
K_23 6 vasen
a oikea
```
```voimakuvio
pinta 0
G_3 15
N 15
K_23 6 oikea
a oikea
```
**Formula:** Car 3: $K_{23} = m_3 a$. Car 2: $K_{12} - K_{23} = m_2 a$. Adding gives $K_{12} = (m_2 + m_3)\,a$
**Conversions:** $m_2 + m_3 = 18\,\text{t} + 12\,\text{t} = 30\,\text{t} = 30\,000\,\text{kg}$ and $1\,\text{kN} = 1000\,\text{N}$.
**Substitution:** b) $K_{12} = 30\,000\,\text{kg} \cdot 0.50\,\text{m/s}^2 = 15\,000\,\text{N} = 15\,\text{kN}$
c) The new order is $12\,\text{t}$, $18\,\text{t}$, $24\,\text{t}$, and behind the coupling between cars 1 and 2 are $18\,\text{t}$ and $24\,\text{t}$, altogether $42\,\text{t}$. Then $K_{12}' = 42\,000\,\text{kg} \cdot 0.50\,\text{m/s}^2 = 21\,000\,\text{N} = 21\,\text{kN}$
**Answer:** a) $a = 0.50\,\text{m/s}^2$. b) $15\,\text{kN}$, two significant figures like the data $18\,\text{t}$ and $12\,\text{t}$ (this goes into the answer box). c) $21\,\text{kN}$, so a coupling with a limit of $20\,\text{kN}$ does not hold in the new order. Reason: the force of the coupling accelerates all the cars behind it, and the heaviest car is now behind the coupling.
**Reasonableness:** In the original order the couplings are $K_{12} = 15\,\text{kN}$ and $K_{23} = 12\,000\,\text{kg} \cdot 0.50\,\text{m/s}^2 = 6.0\,\text{kN}$, and the force of the locomotive on car 1 is $54\,000\,\text{kg} \cdot 0.50\,\text{m/s}^2 = 27\,\text{kN}$. The force decreases from the locomotive backward, because each coupling accelerates less and less mass, and the equation of car 2 checks: $15\,\text{kN} - 6.0\,\text{kN} = 9.0\,\text{kN} = 18\,000\,\text{kg} \cdot 0.50\,\text{m/s}^2$.

## fy4-13-L3-05
**Given:** distance $s = 0.80\,\text{m}$ from rest; from the table $m_2 = 0.100$; $0.200$; $0.300$ and $0.400\,\text{kg}$ and times $t = 1.29$; $0.96$; $0.80$ and $0.73\,\text{s}$ (example data); $g = 9.81\,\text{m/s}^2$; friction is neglected, the string and the pulley are light
**Find:** a) the accelerations and a formula for $m_1$; b) the mean of the mass $m_1$ of the cart in $\text{kg}$; c) the motion of the cart after the hanging mass hits the floor and its speed
**Principle:** The bodies start from rest and the acceleration is constant, so $s = \tfrac{1}{2}at^2$ gives $a$ from the time. Each body gets its own equation of motion, and from them $m_1$ can be solved when $a$ and $m_2$ are known. When the string slackens, no force acts on the cart in the horizontal direction any more, so the first law solves part c).
**Reading the graph:** Four measurements $(m_2, t)$ are read from the table. The time gets shorter as the hanging mass grows, which makes sense, because the acceleration grows.
**Free-body diagram:** The measurement $m_2 = 0.200\,\text{kg}$, $a = 1.74\,\text{m/s}^2$. The cart as a rectangle, positive direction to the right (along the string): $\overline{G}_1$ and $\overline{N}$ cancel, and in the horizontal direction only $\overline{T}_1$ acts to the right. The hanging mass as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up.
```voimakuvio
pinta 0
G_1 8,92
N 8,92
T_1 1,6 oikea
a oikea
---
G_2 1,962
T_2 1,6 ylös
a alas
```
**Formula:** a) $a = \dfrac{2s}{t^2}$. Cart: $T = m_1 a$. Hanging mass: $m_2 g - T = m_2 a$. Substituting, $m_2 g = m_1 a + m_2 a$, so $m_1 = m_2 \left(\dfrac{g}{a} - 1\right)$. b) $m_{1,\text{mean}} = \dfrac{\Sigma m_1}{n}$. c) $v = at$ and $s = \tfrac{1}{2}vt$, so $v = \dfrac{2s}{t}$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** a) The accelerations are $a = \dfrac{1.60\,\text{m}}{t^2}$: $0.961$; $1.736$; $2.500$ and $3.002\,\text{m/s}^2$.
b) $m_1 = m_2 \left(\dfrac{g}{a} - 1\right)$ gives for each measurement
$m_1 = 0.100\,\text{kg} \cdot (10.20 - 1) = 0.920\,\text{kg}$,
$m_1 = 0.200\,\text{kg} \cdot (5.65 - 1) = 0.930\,\text{kg}$,
$m_1 = 0.300\,\text{kg} \cdot (3.924 - 1) = 0.877\,\text{kg}$ and
$m_1 = 0.400\,\text{kg} \cdot (3.27 - 1) = 0.907\,\text{kg}$.
The sum of the masses is $3.634\,\text{kg}$, so $m_{1,\text{mean}} = \dfrac{3.634\,\text{kg}}{4} = 0.909\,\text{kg}$.
c) When $m_2 = 0.200\,\text{kg}$, $v = \dfrac{2 \cdot 0.80\,\text{m}}{0.96\,\text{s}} = 1.67\,\text{m/s}$.
**Answer:** b) $0.91\,\text{kg}$, two significant figures, because the four values vary between $0.88$ and $0.93\,\text{kg}$ and the third figure is not reliable. c) When the hanging mass hits the floor, the string slackens and no horizontal force acts on the cart any more. By the first law the cart keeps moving at a constant speed, about $1.7\,\text{m/s}$, until some other force acts on it.
**Reasonableness:** The four masses are $0.88$–$0.93\,\text{kg}$, so they deviate from the mean by at most $4\,\%$, and the difference is random variation, not systematic. Check: $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{0.200 \cdot 9.81}{1.109}\,\text{m/s}^2 = 1.77\,\text{m/s}^2$ is close to the measured $1.74\,\text{m/s}^2$. The final speed $1.67\,\text{m/s}$ is twice the average speed $s : t = 0.83\,\text{m/s}$, as it should be in uniformly accelerated motion.

## fy4-13-L2-08
**Find:** how the tension $T$ in the string changes when the masses of the trolley and the weight are swapped, and which reason explains it.
**Principle:** An equation of motion is written for each object: for the trolley $T = m_1 a$ and for the weight $m_2 g - T = m_2 a$. A light, inextensible string and a light, frictionless pulley give the objects the same magnitude of acceleration $a$ and the same tension $T$. From the equations $a = \tfrac{m_2}{m_1 + m_2}\,g$ and $T = \tfrac{m_1 m_2}{m_1 + m_2}\,g$.
**Model answer:** In the first experiment $m_1 = 1.6\,\text{kg}$ and $m_2 = 0.40\,\text{kg}$:

$$\begin{aligned}
&a = \frac{0.40\,\text{kg} \cdot 9.81\,\text{m/s}^2}{2.0\,\text{kg}} \\
&\phantom{a} = 1.962\,\text{m/s}^2 \\
&T = 1.6\,\text{kg} \cdot 1.962\,\text{m/s}^2 \\
&\phantom{T} \approx 3.14\,\text{N}
\end{aligned}$$

In the second experiment $m_1 = 0.40\,\text{kg}$ and $m_2 = 1.6\,\text{kg}$:

$$\begin{aligned}
&a = \frac{1.6\,\text{kg} \cdot 9.81\,\text{m/s}^2}{2.0\,\text{kg}} \\
&\phantom{a} = 7.848\,\text{m/s}^2 \\
&T = 0.40\,\text{kg} \cdot 7.848\,\text{m/s}^2 \\
&\phantom{T} \approx 3.14\,\text{N}
\end{aligned}$$

So the tension stays the same, about $3.1\,\text{N}$. Reason: in the formula $T = \tfrac{m_1 m_2}{m_1 + m_2}\,g$ the product and the sum of the masses do not change when the masses swap places. The acceleration becomes four times as large, because the weight of the hanging mass, which accelerates the system, becomes four times as large, so $T = m_1 a$ does not decrease although the mass of the trolley becomes a quarter. In both experiments $T$ is smaller than the weight of the hanging mass ($3.9\,\text{N}$ and $15.7\,\text{N}$), as it must be for an accelerating hanging mass.

## fy4-13-L2-09
**Given:** mass of the cart $m_1 = 0.80\,\text{kg}$ and the measured points of the graph for a cart starting from rest; friction and air resistance are neglected, the string and the pulley are light
**Find:** the tension $T$ in the string in $\text{N}$
**Principle:** In the horizontal direction only the string acts on the cart, so the equation of motion of the cart $T = m_1 a$ gives the tension once the acceleration is known. The acceleration is the slope of the $(t,v)$ graph. The mass of the hanging weight is not needed.
**Free-body diagram:** The cart as a rectangle, positive direction along the string. In the vertical direction the weight $\overline{G}_1$ and the normal force $\overline{N}$ cancel, and in the horizontal direction only $\overline{T}_1$ acts.
```voimakuvio
pinta 0
G_1 7,848
N 7,848
T_1 1,56 oikea
a oikea
```
**Reading the graph:** The points lie on a straight line through the origin: the speed grows by about $1.0\,\text{m/s}$ in every half second. The acceleration is therefore constant. We read the farthest point $(2.0\,\text{s};\, 3.9\,\text{m/s})$ and the starting point $(0\,\text{s};\, 0\,\text{m/s})$. The farthest point gives the most accurate slope.
**Formula:** $a = \dfrac{\Delta v}{\Delta t}$ and $T = m_1 a$
**Conversions:** The speeds are in $\text{m/s}$, the times in seconds and the mass in kilograms, so no conversions are needed.
**Substitution:** $a = \dfrac{3.9\,\text{m/s} - 0\,\text{m/s}}{2.0\,\text{s} - 0\,\text{s}} = 1.95\,\text{m/s}^2$ and $T = 0.80\,\text{kg} \cdot 1.95\,\text{m/s}^2 = 1.56\,\text{N}$
**Answer:** $T \approx 1.6\,\text{N}$, two significant figures, because the mass $0.80\,\text{kg}$ and the speeds read are given to two figures.
**Reasonableness:** The acceleration $1.95\,\text{m/s}^2$ is smaller than $g$, as it must be when the hanging weight also accelerates the cart. The tension is the product of the mass and the acceleration, and about $0.8\,\text{kg}$ and about $2\,\text{m/s}^2$ give about $1.6\,\text{N}$.

## fy4-13-L3-06
**Given:** hanging mass $m_2 = 0.30\,\text{kg}$ and the measured points of the graph for a cart starting from rest; $g = 9.81\,\text{m/s}^2$; friction and air resistance are neglected, the string and the pulley are light
**Find:** a) the mass $m_1$ of the cart in $\text{kg}$; b) whether the tension $T$ is greater than, smaller than or equal to the weight $m_2 g$ of the hanging mass
**Principle:** Each body gets its own equation of motion. The string is inextensible, so the bodies have the same magnitude of acceleration $a$, and a light string and a light, frictionless pulley give tensions of the same size $T$. The acceleration is read from the graph, so the mass of the cart is the only unknown.
**Free-body diagram:** The cart as a rectangle, positive direction along the string: $\overline{G}_1$ and $\overline{N}$ cancel, and in the horizontal direction only $\overline{T}_1$ acts. The hanging mass as a rectangle, positive direction down: $\overline{G}_2$ down and $\overline{T}_2$ up, shorter than the weight.
```voimakuvio
pinta 0
G_1 11,86
N 11,86
T_1 2,358 oikea
a oikea
---
G_2 2,943
T_2 2,358 ylös
a alas
```
**Reading the graph:** The points lie on a straight line through the origin, so the acceleration is constant. The farthest point $(2.0\,\text{s};\, 3.9\,\text{m/s})$ and the starting point $(0\,\text{s};\, 0\,\text{m/s})$ give the slope $a = \dfrac{3.9\,\text{m/s}}{2.0\,\text{s}} = 1.95\,\text{m/s}^2$. The point $(1.0\,\text{s};\, 2.0\,\text{m/s})$ gives almost the same, $2.0\,\text{m/s}^2$.
**Formula:** Cart: $T = m_1 a$. Hanging mass: $m_2 g - T = m_2 a$. From the equations $m_2 g = (m_1 + m_2)\,a$, so $m_1 = m_2\left(\dfrac{g}{a} - 1\right)$
**Conversions:** All quantities are in SI units, so no conversions are needed.
**Substitution:** a) $m_1 = 0.30\,\text{kg} \cdot \left(\dfrac{9.81\,\text{m/s}^2}{1.95\,\text{m/s}^2} - 1\right) = 0.30\,\text{kg} \cdot 4.031 = 1.21\,\text{kg}$. b) $T = m_1 a = 1.21\,\text{kg} \cdot 1.95\,\text{m/s}^2 = 2.36\,\text{N}$ and $m_2 g = 0.30\,\text{kg} \cdot 9.81\,\text{m/s}^2 = 2.94\,\text{N}$
**Answer:** a) $m_1 \approx 1.21\,\text{kg}$, two significant figures, because the hanging mass $0.30\,\text{kg}$ and the acceleration read are given to two figures. b) The tension $2.4\,\text{N}$ is smaller than the weight $2.9\,\text{N}$ of the hanging mass. The hanging mass accelerates downward, so its net force $m_2 g - T = m_2 a$ points down and $T < m_2 g$. The tension would equal the weight only if the acceleration were zero.
**Reasonableness:** The cart is about four times as heavy as the hanging mass. Check: $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{2.943\,\text{N}}{1.509\,\text{kg}} = 1.95\,\text{m/s}^2$, which agrees with the value read from the graph.
