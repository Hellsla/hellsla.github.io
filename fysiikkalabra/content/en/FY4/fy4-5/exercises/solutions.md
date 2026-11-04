## fy4-5-L1-01
**Given:** $m = 1.5\,\text{kg}$, the lamp is at rest; $g = 9.81\,\text{m/s}^2$
**Find:** the tension $T$ of the cord in $\text{N}$
**Principle:** The lamp is at rest, so by Newton's second law the sum of the forces acting on it is zero.
**Free-body diagram:** The lamp as a rectangle, $y$-axis up. The Earth and the cord act on the lamp: the weight $\overline{G}$ down and the tension $\overline{T}$ of the cord up along the cord. The arrows are equally long.
```voimakuvio
G 14,715
T 14,715 ylös
a 0
```
**Formula:** $T - mg = 0$, so $T = mg$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $T = 1.5\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 14.715\,\text{N}$
**Answer:** $14.7\,\text{N} \approx 15\,\text{N}$, two significant figures like the mass $1.5\,\text{kg}$.
**Reasonableness:** The weight of one kilogram is about $10\,\text{N}$, so the weight of a lamp of one and a half kilograms is about $15\,\text{N}$. The cord supports the whole weight, because there are no other forces acting upward.

## fy4-5-L1-02
**Given:** forces read from the diagram: $F_1 = 40\,\text{N}$ to the right, $F_2 = 25\,\text{N}$ to the left, $F_3 = 30\,\text{N}$ up and $F_4 = 30\,\text{N}$ down
**Find:** the magnitude of the net force $\Sigma F$ in $\text{N}$
**Principle:** The net force is the vector sum of the forces. Calculate the sums of the components separately in each axis direction, with $x$ pointing to the right and $y$ up.
**Reading the graph:** The lengths of the arrows are read from the squares: $F_1$ is four squares, $F_2$ two and a half squares, and $F_3$ and $F_4$ three squares each. One square is $10\,\text{N}$.
**Formula:** $\Sigma F_x = F_1 - F_2$ and $\Sigma F_y = F_3 - F_4$. When $\Sigma F_y = 0$, the magnitude of the net force is $\Sigma F = |\Sigma F_x|$
**Conversions:** The squares are converted to newtons: $4\cdot 10\,\text{N} = 40\,\text{N}$ and $2.5\cdot 10\,\text{N} = 25\,\text{N}$.
**Substitution:** $\Sigma F_y = 30\,\text{N} - 30\,\text{N} = 0$ and $\Sigma F = 40\,\text{N} - 25\,\text{N} = 15\,\text{N}$
**Answer:** $15\,\text{N}$ to the right, with two significant figures; the grid is read to the accuracy of half a square, that is $5\,\text{N}$.
**Reasonableness:** The vertical forces are equally long and cancel each other. Horizontally the arrow pointing right is one and a half squares longer, that is $15\,\text{N}$, so the net force points to the right. The net force is not the sum of the magnitudes of the forces, $125\,\text{N}$.

## fy4-5-L1-03
**Given:** $m = 0.50\,\text{kg}$, the force of the hand $F = 20\,\text{N}$ horizontally toward the wall, the book is at rest; $g = 9.81\,\text{m/s}^2$
**Find:** the friction force $F_\mu$ from the wall in $\text{N}$
**Principle:** The book is at rest, so the sum of the forces is zero both horizontally and vertically. The wall is vertical, so its normal force is horizontal and its friction force is vertical.
**Free-body diagram:** The book as a rectangle, $x$ toward the wall and $y$ up. The force $\overline{F}$ of the hand toward the wall and the normal force $\overline{N}$ of the wall away from the wall, both horizontal. The weight $\overline{G}$ down and the friction force $\overline{F}_\mu$ of the wall up, because the book tends to slide down.
```voimakuvio
pinta 0
F 20 0 työntö
N 20 @oikea
G 4,905
F_mu 4,905 ylös @oikea
a 0
akselit 0
```
**Formula:** $y$: $F_\mu - mg = 0$, so $F_\mu = mg$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $F_\mu = 0.50\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 4.905\,\text{N}$
**Answer:** $4.9\,\text{N}$, two significant figures like the mass $0.50\,\text{kg}$.
**Reasonableness:** Friction supports the whole weight of the book, because it is the only force acting upward. The force of the hand, $20\,\text{N}$, does not appear directly in the answer: it determines the normal force $N = 20\,\text{N}$, but friction is exactly as large as staying at rest requires. Here the normal force does not point up but horizontally.

## fy4-5-L1-04
**Given:** $m = 65\,\text{kg}$, the elevator moves at constant velocity; $g = 9.81\,\text{m/s}^2$
**Find:** the normal force $N$ of the floor in $\text{N}$
**Principle:** In uniform motion the acceleration is zero, so by Newton's second law the sum of the forces is zero even though the person is moving.
**Free-body diagram:** The person as a rectangle, $y$-axis up. The weight $\overline{G}$ down and the normal force $\overline{N}$ of the floor up, equally long. The velocity is not drawn as a force.
```voimakuvio
pinta 0
G 637,65
N 637,65
a 0
```
**Formula:** $N - mg = 0$, so $N = mg$
**Conversions:** The mass is in kilograms, so no conversions are needed.
**Substitution:** $N = 65\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 637.65\,\text{N}$
**Answer:** $640\,\text{N}$ or $6.4\cdot 10^{2}\,\text{N}$, two significant figures like the mass $65\,\text{kg}$.
**Reasonableness:** The normal force is the same as the weight of the person, just as if the elevator were standing still. Motion at constant velocity does not require a net force. A person standing on a scale would read their ordinary weight.

## fy4-5-L1-05
**Given:** $T = 250\,\text{N}$, angle to the horizontal $\alpha = 40^\circ$
**Find:** the horizontal component $T_x$ of the tension in $\text{N}$
**Principle:** The force and its components form a right triangle whose hypotenuse is the force. The horizontal component is the leg adjacent to the angle $\alpha$.
**Free-body diagram:** The force $\overline{T}$ of the rope as one solid arrow from the attachment point obliquely up at an angle of $40^\circ$, and the components $T_x$ and $T_y$ with dashed lines from the same point.
```voimakuvio
T 250 40
akselit 0
komponentit T
```
**Formula:** $T_x = T\cos\alpha$
**Conversions:** The force is in newtons and the angle in degrees, so no conversions are needed; the calculator is in DEG mode.
**Substitution:** $T_x = 250\,\text{N}\cdot\cos 40^\circ = 191.5\,\text{N}$
**Answer:** $190\,\text{N}$ or $1.9\cdot 10^{2}\,\text{N}$, two significant figures, because the angle $40^\circ$ is given with two figures and the force $250\,\text{N}$ is not more precise than that.
**Reasonableness:** The component is smaller than the force $250\,\text{N}$, as it should be. The angle is less than $45^\circ$, so the horizontal component is larger than the vertical component $250\,\text{N}\cdot\sin 40^\circ \approx 161\,\text{N}$.

## fy4-5-L2-01
**Given:** $m = 15\,\text{kg}$, $T = 60\,\text{N}$, $\alpha = 30^\circ$, the sled moves at constant velocity
**Find:** the friction force $F_\mu$ from the snow in $\text{N}$
**Principle:** In uniform motion the acceleration is zero, so the sum of the forces is zero also in the direction of motion: friction is equal to the horizontal component of the force of the rope.
**Free-body diagram:** The sled as a rectangle, $x$ in the direction of motion and $y$ up. The weight $\overline{G}$ down, the normal force $\overline{N}$ from the snow up and shorter than the weight, the tension $\overline{T}$ of the rope obliquely up and forward, and the friction force $\overline{F}_\mu$ from the snow backward. The component $T_x$ is dashed.
```voimakuvio
pinta 0
G 147,15
N 117,15
T 60 30
F_mu 51,96 vasen
a 0
akselit 0
komponentit T
```
**Formula:** $x$: $T\cos\alpha - F_\mu = 0$, so $F_\mu = T\cos\alpha$
**Conversions:** The force is in newtons, so no conversions are needed. The mass is not needed, because friction comes from the horizontal equation.
**Substitution:** $F_\mu = 60\,\text{N}\cdot\cos 30^\circ = 51.96\,\text{N}$
**Answer:** $52\,\text{N}$, two significant figures like the force $60\,\text{N}$.
**Reasonableness:** Friction is a little smaller than the force of the rope, $60\,\text{N}$, because only part of the force of the rope pulls forward. From the vertical direction the normal force is $N = mg - T\sin\alpha \approx 147\,\text{N} - 30\,\text{N} = 117\,\text{N}$, smaller than the weight.

## fy4-5-L2-02
**Given:** $m = 60\,\text{kg}$, acceleration upward $a = 1.2\,\text{m/s}^2$; $g = 9.81\,\text{m/s}^2$
**Find:** the normal force $N$ of the floor in $\text{N}$
**Principle:** The person accelerates upward with the elevator, so the net force points up and by Newton's second law is $ma$.
**Free-body diagram:** The person as a rectangle, $y$-axis up. The weight $\overline{G}$ down and the normal force $\overline{N}$ up, the normal force longer. The acceleration is drawn separately, not as a force.
```voimakuvio
pinta 0
G 588,6
N 660,6
a ylös
```
**Formula:** $N - mg = ma$, so $N = m(g + a)$
**Conversions:** The mass is in kilograms and the accelerations in $\text{m/s}^2$, so no conversions are needed.
**Substitution:** $N = 60\,\text{kg}\cdot(9.81\,\text{m/s}^2 + 1.2\,\text{m/s}^2) = 60\,\text{kg}\cdot 11.01\,\text{m/s}^2 = 660.6\,\text{N}$
**Answer:** $660\,\text{N}$ or $6.6\cdot 10^{2}\,\text{N}$, two significant figures like the mass $60\,\text{kg}$ and the acceleration $1.2\,\text{m/s}^2$.
**Reasonableness:** The weight is about $590\,\text{N}$, and the normal force is about $70\,\text{N}$ larger, which is $ma = 60\,\text{kg}\cdot 1.2\,\text{m/s}^2 = 72\,\text{N}$. When the elevator starts upward you feel heavier, because the floor presses on your feet more than usual.

## fy4-5-L2-03
**Given:** $m = 40\,\text{kg}$, $F = 120\,\text{N}$ at an angle $\alpha = 30^\circ$ below the horizontal, $F_\mu = 80\,\text{N}$
**Find:** the acceleration $a$ of the box in $\text{m/s}^2$
**Principle:** The box accelerates horizontally. By Newton's second law the sum of the horizontal force components is $ma$. The vertical equation is not needed, because friction is given.
**Free-body diagram:** The box as a rectangle, $x$ in the direction of motion and $y$ up. The weight $\overline{G}$ down, the normal force $\overline{N}$ from the floor up and longer than the weight, the force $\overline{F}$ of the handle obliquely down and forward, and the friction force $\overline{F}_\mu$ backward. The components $F_x$ and $F_y$ are dashed.
```voimakuvio
pinta 0
G 392,4
N 452,4
F 120 -30 työntö @ylä
F_mu 80 vasen
a oikea
akselit 0
komponentit F
```
**Formula:** $x$: $F\cos\alpha - F_\mu = ma$, so $a = \dfrac{F\cos\alpha - F_\mu}{m}$
**Conversions:** The forces are in newtons and the mass in kilograms, so the result comes directly in $\text{m/s}^2$.
**Substitution:** $a = \dfrac{120\,\text{N}\cdot\cos 30^\circ - 80\,\text{N}}{40\,\text{kg}} = \dfrac{103.9\,\text{N} - 80\,\text{N}}{40\,\text{kg}} = 0.598\,\text{m/s}^2$
**Answer:** $0.60\,\text{m/s}^2$, two significant figures like the data.
**Reasonableness:** The horizontal component $104\,\text{N}$ is only a little larger than friction, $80\,\text{N}$, so the net force $24\,\text{N}$ is small and a box of $40\,\text{kg}$ accelerates slowly. If the whole force $120\,\text{N}$ acted forward, the acceleration would be $1.0\,\text{m/s}^2$.

## fy4-5-L2-04
**Given:** $m = 50\,\text{kg}$, $F_1 = 30\,\text{N}$ and $F_2 = 40\,\text{N}$ horizontal, perpendicular to each other; no friction
**Find:** the magnitude $a$ of the acceleration of the sled in $\text{m/s}^2$
**Principle:** The net force is the vector sum of the forces, and by Newton's second law it determines the acceleration. Vertically the weight and the normal force from the ice cancel each other.
**Free-body diagram:** The sled as a rectangle seen from above, $x$ in the direction of the force $\overline{F}_1$ and $y$ in the direction of the force $\overline{F}_2$. Seen from the side, the weight $\overline{G}$ down and the normal force $\overline{N}$ up, equally long.
```voimakuvio
F_1 30 0
F_2 40 90
a 53,13
akselit 0
```
**Formula:** $\Sigma F_x = F_1$ and $\Sigma F_y = F_2$, so $\Sigma F = \sqrt{F_1^2 + F_2^2}$. From Newton's second law $\Sigma F = ma$, so $a = \dfrac{\Sigma F}{m}$
**Conversions:** The forces are in newtons and the mass in kilograms, so no conversions are needed.
**Substitution:** $\Sigma F = \sqrt{(30\,\text{N})^2 + (40\,\text{N})^2} = 50\,\text{N}$ and $a = \dfrac{50\,\text{N}}{50\,\text{kg}} = 1.0\,\text{m/s}^2$
**Answer:** $1.0\,\text{m/s}^2$, two significant figures like the forces $30\,\text{N}$ and $40\,\text{N}$.
**Reasonableness:** The net force $50\,\text{N}$ is larger than either force but smaller than their sum $70\,\text{N}$, because the forces point in different directions. The acceleration points between the forces, closer to the larger force.

## fy4-5-L3-01
**Given:** $m = 70\,\text{kg}$, the elevator moves upward and slows down, magnitude of the acceleration $1.5\,\text{m/s}^2$; $g = 9.81\,\text{m/s}^2$
**Find:** the normal force $N$ of the floor in $\text{N}$
**Principle:** An elevator moving upward is slowing down, so its acceleration points down even though the velocity points up. By Newton's second law the net force points in the direction of the acceleration, that is down.
**Free-body diagram:** The person as a rectangle, $y$-axis up. The weight $\overline{G}$ down and the normal force $\overline{N}$ up, the normal force shorter. The velocity $\overline{v}$ up (blue) and the acceleration $\overline{a}$ down (orange) are drawn beside the diagram as thin arrows, not as forces. The component of the acceleration is $a_y = -1.5\,\text{m/s}^2$.
```voimakuvio
pinta 0
G 686,7
N 581,7
v ylös
a alas
```
**Formula:** $N - mg = m a_y$, so $N = m(g + a_y)$
**Conversions:** The mass is in kilograms and the accelerations in $\text{m/s}^2$, so no conversions are needed.
**Substitution:** $N = 70\,\text{kg}\cdot(9.81\,\text{m/s}^2 - 1.5\,\text{m/s}^2) = 70\,\text{kg}\cdot 8.31\,\text{m/s}^2 = 581.7\,\text{N}$
**Answer:** $580\,\text{N}$ or $5.8\cdot 10^{2}\,\text{N}$, two significant figures like the mass $70\,\text{kg}$ and the acceleration $1.5\,\text{m/s}^2$.
**Reasonableness:** The weight is about $690\,\text{N}$, and the normal force is smaller, because the net force points down. When the elevator stops at the top you feel lighter for a moment. If you got a normal force larger than the weight, the direction of the acceleration would have been chosen by the velocity, which is a common mistake.

## fy4-5-L3-02
**Given:** $m = 19\,\text{kg}$, initial velocity $v_0 = 2.0\,\text{m/s}$, final velocity $v = 0$, time $\Delta t = 20\,\text{s}$; the deceleration is uniform
**Find:** the friction force $F_\mu$ in $\text{N}$
**Principle:** The speed of the stone changes uniformly, so the acceleration is $a = \dfrac{\Delta v}{\Delta t}$ (chapter *Acceleration and uniformly accelerated motion*). By Newton's second law the net force in the direction of motion is $ma$, and the only horizontal force is friction.
**Free-body diagram:** The stone as a rectangle, $x$ in the direction of motion and $y$ up. The weight $\overline{G}$ down, the normal force $\overline{N}$ of the ice up and the friction force $\overline{F}_\mu$ backward. There is no forward force, because the thrower is no longer touching the stone.
```voimakuvio
pinta 0
G 186,39
N 186,39
F_mu 1,9 vasen
v oikea
a vasen
```
**Formula:** $a_x = \dfrac{v - v_0}{\Delta t}$ and $x$: $-F_\mu = m a_x$, so $F_\mu = \dfrac{m(v_0 - v)}{\Delta t}$
**Conversions:** The mass is in kilograms, the velocities in $\text{m/s}$ and the time in seconds, so no conversions are needed.
**Substitution:** $F_\mu = \dfrac{19\,\text{kg}\cdot(2.0\,\text{m/s} - 0)}{20\,\text{s}} = 19\,\text{kg}\cdot 0.10\,\text{m/s}^2 = 1.9\,\text{N}$
**Answer:** $1.9\,\text{N}$, two significant figures like the mass, the velocity and the time.
**Reasonableness:** The weight of the stone is about $190\,\text{N}$, and friction is only about one percent of it, which suits smooth ice. The component of the acceleration is negative because the stone slows down, and friction points backward as in the diagram.

## fy4-5-L3-03
**Given:** $m = 4.0\,\text{g}$, buoyancy $F_\text{b} = 0.10\,\text{N}$, the balloon is at rest against the ceiling; $g = 9.81\,\text{m/s}^2$
**Find:** the normal force $N$ of the ceiling in $\text{N}$
**Principle:** The balloon is at rest, so by Newton's second law the sum of the forces is zero. The ceiling touches the balloon from above, so its normal force is perpendicular to the ceiling and pushes the balloon away from the ceiling, that is down.
**Free-body diagram:** The balloon as a rectangle, $y$-axis up. Buoyancy $\overline{F}_\text{b}$ up, the weight $\overline{G}$ down and the normal force $\overline{N}$ of the ceiling down. The buoyancy arrow is as long as the weight and normal force arrows together. There is no air drag, because the balloon is not moving.
```voimakuvio
pinta 0
F_noste 0,10 ylös
G 0,03924
N 0,06076 @ylä
a 0
```
**Formula:** $F_\text{b} - mg - N = 0$, so $N = F_\text{b} - mg$
**Conversions:** $m = 4.0\,\text{g} = 4.0 \cdot 0.001\,\text{kg} = 0.0040\,\text{kg}$
**Substitution:** $N = 0.10\,\text{N} - 0.0040\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 0.10\,\text{N} - 0.03924\,\text{N} = 0.06076\,\text{N}$
**Answer:** $0.061\,\text{N} \approx 0.06\,\text{N}$. The normal force is a difference, and in a difference the number of decimals decides: the buoyancy $0.10\,\text{N}$ is known to a hundredth of a newton.
**Reasonableness:** The buoyancy is larger than the weight, $0.039\,\text{N}$, so without the ceiling the balloon would rise. The ceiling stops it by pushing down exactly by the excess: $0.039\,\text{N} + 0.061\,\text{N} = 0.10\,\text{N}$. Here the normal force points down, not up.

## fy4-5-L1-06
**Find:** which forces are drawn in the free-body diagram when a box slides on a horizontal floor and slows down because of friction.
**Principle:** The free-body diagram includes only the forces that act on the chosen object, and every force has a cause: the Earth, a surface, a string or a pusher. Velocity and acceleration are not forces. According to Newton's second law, an object can move without a force in the direction of motion.
**Model answer:** Three forces act on the box. The Earth pulls the box down (weight), the floor supports it upward (normal force) and the floor resists the sliding to the left (friction). The weight and the normal force are equally long, because the box does not move in the vertical direction, and friction is the only horizontal force, so it slows the box down. There is no motion force pointing to the right, because there is no object that would cause it. Velocity is not drawn as a force. If needed, it is drawn separately beside the free-body diagram. The normal force must not be left out, even though it cancels the weight.

## fy4-5-L1-07
**Given:** pushing forces $F_1 = 120\,\text{N}$ and $F_2 = 85\,\text{N}$ in the same direction, friction force $F_\mu = 150\,\text{N}$ in the opposite direction; the weight and the normal force cancel each other
**Find:** the magnitude of the net force $\Sigma F$ in $\text{N}$
**Principle:** The net force is the vector sum of the forces. The forces lie on the same line, so the sum is calculated from the horizontal components, with $x$ pointing in the direction of the pushing. In the vertical direction the net force is zero.
**Free-body diagram:** The cabinet as a rectangle, $x$ in the direction of the pushing and $y$ up. Two pushing forces $\overline{F}_1$ and $\overline{F}_2$ forward, the friction force $\overline{F}_\mu$ backward, and the weight $\overline{G}$ down and the normal force $\overline{N}$ up with equal lengths. The friction force is longer than either pushing force but shorter than their sum.
**Formula:** $\Sigma F_x = F_1 + F_2 - F_\mu$
**Conversions:** All forces are in newtons, so no conversions are needed.
**Substitution:** $\Sigma F_x = 120\,\text{N} + 85\,\text{N} - 150\,\text{N} = 55\,\text{N}$
**Answer:** $55\,\text{N}$ in the direction of the pushing, two significant figures like the given forces.
**Reasonableness:** The pushing forces total $205\,\text{N}$, which is greater than the friction $150\,\text{N}$, so the net force points in the direction of the pushing and the cabinet accelerates. If the pushing forces totalled less than $150\,\text{N}$, the cabinet would slow down or stay at rest. The net force is not the sum of the magnitudes of the forces, $355\,\text{N}$.

## fy4-5-L1-08
**Find:** how the normal force $N$ from the floor compares with the weight $G$ of the box when the box is pulled with a string obliquely upward and does not move.
**Principle:** The box is at rest, so according to Newton's second law the sum of the forces is zero also in the vertical direction. There are three forces in the vertical direction: the weight down, and the normal force and the vertical component of the tension of the string up.
**Model answer:** The equation in the vertical direction is $N + T\sin\alpha - G = 0$, so $N = G - T\sin\alpha$. The vertical component of the string supports part of the weight, and the floor needs to support only the rest, so the normal force is smaller than the weight. The normal force is therefore not always equal to the weight: it is exactly as large as the balance in the vertical direction requires. If the string pulled horizontally, the normal force would be equal to the weight, and if the string pulled the box obliquely downward, the normal force would be greater than the weight. The normal force would be zero only when the vertical component of the string were equal to the whole weight, and then the box would be about to lift off the floor.

## fy4-5-L2-05
**Given:** the ring is at rest; measurements $(F_\text{A}, F_\text{C}, F_\text{B})$: $(3.0;\ 2.5;\ 3.9)\,\text{N}$, $(4.5;\ 3.8;\ 5.9)\,\text{N}$ and $(6.0;\ 5.1;\ 7.9)\,\text{N}$
**Find:** the mean $\alpha_\text{avg}$ of the angle $\alpha$ in $^\circ$
**Principle:** The ring is at rest, so according to Newton's second law the sum of the forces acting on it is zero in both the horizontal and the vertical direction. Rope B is oblique, so its force is divided into components.
**Free-body diagram:** The ring as a rectangle, $x$ to the right and $y$ up. The tension $\overline{F}_\text{A}$ of rope A to the left and the tension $\overline{F}_\text{C}$ of rope C down. The force $\overline{F}_\text{B}$ of rope B starts obliquely up and to the right at an angle $\alpha$, and its components $F_\text{B}\cos\alpha$ and $F_\text{B}\sin\alpha$ are drawn with dashed lines. The components are as long as $F_\text{A}$ and $F_\text{C}$. The weight of the ring is not drawn, because it is ignored in the task.
**Reading the graph:** The forces $F_\text{A}$ and $F_\text{C}$ of each measurement are read from the table. The reading of sensor B is also taken for comparison.
**Formula:** $x$: $F_\text{B}\cos\alpha - F_\text{A} = 0$ and $y$: $F_\text{B}\sin\alpha - F_\text{C} = 0$, so $\alpha = \arctan\dfrac{F_\text{C}}{F_\text{A}}$
**Conversions:** The forces are in newtons and the angle is calculated in degrees, so no conversions are needed; the calculator is in DEG mode.
**Substitution:** The angles are
```latex
\begin{aligned}
\alpha_1 &= \arctan\dfrac{2.5}{3.0} = 39.8\,{}^\circ \\
\alpha_2 &= \arctan\dfrac{3.8}{4.5} = 40.2\,{}^\circ \\
\alpha_3 &= \arctan\dfrac{5.1}{6.0} = 40.4\,{}^\circ
\end{aligned}
```
The sum is $120.4\,{}^\circ$, so the mean is $\alpha_\text{avg} = 120.4\,{}^\circ : 3 = 40.1\,{}^\circ$. Check with the first measurement: $F_\text{B} = \sqrt{(3.0\,\text{N})^2 + (2.5\,\text{N})^2} = 3.9\,\text{N}$.
**Answer:** a) The free-body diagram and the equations are above. b) $\alpha_\text{avg} = 40.1\,{}^\circ \approx 40\,{}^\circ$, to two significant figures like the readings of the forces. c) The calculated $F_\text{B} = 3.9\,\text{N}$ is the same as the reading of the sensor.
**Reasonableness:** The three angles differ from each other by at most $0.6\,{}^\circ$, so they describe the same angle and the small variation is random variation of the measurement. The forces grow in the same proportion, and the ratio $F_\text{C} : F_\text{A}$ stays at about $0.84$. The angle is less than $45\,{}^\circ$, so $F_\text{A} > F_\text{C}$ as in the table. The force $F_\text{B}$ is greater than either component but smaller than their sum, $5.5\,\text{N}$.

## fy4-5-L2-06
**Given:** $m = 12\,\text{kg}$, friction force $F_\mu = 30\,\text{N}$ to the left, the box slides to the right and slows down; there is no air drag
**Find:** a) the student's error; b) the magnitude of the acceleration $a$ in $\text{m/s}^2$
**Principle:** The free-body diagram includes only forces that act on the object and have a cause. The student drew a “force from the kick” on the box, although after the kick no object pushes the box to the right, and concluded the direction of the acceleration from the direction of the motion, although the box slows down. The force of the kick acts on the box only while the foot touches it. When the box has left the foot, only friction affects its horizontal motion.
**Free-body diagram:** The box as a rectangle, $x$ to the right and $y$ up. The weight $\overline{G}$ down and the normal force $\overline{N}$ from the floor up with equal lengths, and the friction force $\overline{F}_\mu$ to the left. No force is drawn to the right. The velocity to the right and the acceleration to the left are drawn separately beside the diagram.
```voimakuvio
pinta 0
G 117,72
N 117,72
F_mu 30 vasen
v oikea
a vasen
```
**Formula:** $x$: $-F_\mu = m a_x$, so $a_x = -\dfrac{F_\mu}{m}$ and the magnitude of the acceleration is $a = \dfrac{F_\mu}{m}$
**Conversions:** The force is in newtons and the mass in kilograms, so the result comes directly in $\text{m/s}^2$.
**Substitution:** $a = \dfrac{30\,\text{N}}{12\,\text{kg}} = 2.5\,\text{m/s}^2$
**Answer:** a) An extra force that has no cause was included in the free-body diagram. b) $a = 2.5\,\text{m/s}^2$ to the left, that is, against the motion, two significant figures like the given values. The box slows down.
**Reasonableness:** The net force $30\,\text{N}$ points to the left, so the acceleration points to the left and the box slows down, as the task says. The student's result, according to which the box accelerates, contradicts this. Friction is only about a quarter of the weight of the box, $118\,\text{N}$.

## fy4-5-L2-07
**Given:** $F_1 = 6.0\,\text{N}$, $F_2 = 8.0\,\text{N}$, the angle between their directions $\varphi = 60\,{}^\circ$; from the table $F_3 = 12.3\,\text{N}$ when $\varphi = 60\,{}^\circ$
**Find:** the magnitude of the sum of the forces $\overline{F}_1$ and $\overline{F}_2$, $\Sigma F$, in $\text{N}$ when $\varphi = 60\,{}^\circ$
**Principle:** a) The ring is at rest, so according to Newton's second law the sum of the forces $\overline{F}_1$, $\overline{F}_2$ and $\overline{F}_3$ is zero. Therefore the force of sensor 3 is equal in magnitude and opposite in direction to the sum of the forces $\overline{F}_1$ and $\overline{F}_2$, and its reading tells the magnitude of the sum. b) The sum of oblique forces is calculated by components.
**Free-body diagram:** The ring as a rectangle, $x$ in the direction of the force $\overline{F}_1$. The force $\overline{F}_1$ starts straight in the direction of the $x$ axis and the force $\overline{F}_2$ at an angle of $60\,{}^\circ$ upward. The force $\overline{F}_3$ starts in the direction opposite to their sum. The components $F_{2x}$ and $F_{2y}$ are drawn with dashed lines.
**Reading the graph:** The row $\varphi = 60\,{}^\circ$ is read from the table: $F_3 = 12.3\,\text{N}$.
**Formula:** $\Sigma F_x = F_1 + F_2\cos\varphi$ and $\Sigma F_y = F_2\sin\varphi$, so $\Sigma F = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}$
**Conversions:** The forces are in newtons and the angle in degrees, so no conversions are needed.
**Substitution:** First the components:
```latex
\begin{aligned}
\Sigma F_x &= 6.0\,\text{N} + 8.0\,\text{N}\cdot\cos 60\,{}^\circ \\
&= 10.0\,\text{N} \\
\Sigma F_y &= 8.0\,\text{N}\cdot\sin 60\,{}^\circ \\
&= 6.93\,\text{N}
\end{aligned}
```
Then the magnitude: $\Sigma F = \sqrt{(10.0\,\text{N})^2 + (6.93\,\text{N})^2} = 12.2\,\text{N}$
**Answer:** a) The ring is at rest, so the force $\overline{F}_3$ cancels the sum of the forces $\overline{F}_1$ and $\overline{F}_2$. b) $\Sigma F \approx 12\,\text{N}$, two significant figures like the given forces. c) The measured $12.3\,\text{N}$ differs from the calculated $12.2\,\text{N}$ by about $0.1\,\text{N}$, that is, about one per cent; the difference is of the order of the measurement uncertainty. It may be due to inaccuracy in reading the angle, zeroing of the sensors, or the ring not being completely at rest.
**Reasonableness:** The sum $12.2\,\text{N}$ is smaller than the sum of the magnitudes of the forces, $14.0\,\text{N}$, and greater than the greater force $8.0\,\text{N}$, as it should be at the angle $60\,{}^\circ$. In the table the reading decreases as the angle grows ($13.4\,\text{N}$, $12.3\,\text{N}$, $10.1\,\text{N}$), and at the angle $90\,{}^\circ$ the sum is $\sqrt{6.0^2 + 8.0^2}\,\text{N} = 10\,\text{N}$ as in the measurement.

## fy4-5-L3-04
**Given:** $m = 25\,\text{kg}$, $T = 120\,\text{N}$, $\alpha = 30\,{}^\circ$, the box starts from rest; from the table $v = 0$ at $t = 0$ and $v = 4.01\,\text{m/s}$ at $t = 5.0\,\text{s}$; $g = 9.81\,\text{m/s}^2$
**Find:** the friction force $F_\mu$ in $\text{N}$ and the normal force $N$
**Principle:** The box accelerates in the horizontal direction and does not move in the vertical direction. The acceleration is obtained from the change in velocity (chapter *Acceleration and uniformly accelerated motion*), and Newton's second law is written by components: in the horizontal direction the net force is $ma$, in the vertical direction zero.
**Free-body diagram:** The box as a rectangle, $x$ in the direction of motion and $y$ up. The weight $\overline{G}$ down and the normal force $\overline{N}$ from the floor up and shorter than the weight, the tension $\overline{T}$ of the rope obliquely up and forward, and the friction force $\overline{F}_\mu$ backward. The components $T_x$ and $T_y$ with dashed lines. The acceleration forward is drawn separately, not as a force.
```voimakuvio
pinta 0
G 245,25
N 185,25
T 120 30
F_mu 83,87 vasen
a oikea
akselit 0
komponentit T
```
**Reading the graph:** The velocity grows by about the same amount every second: the changes of consecutive seconds are $0.78$, $0.85$, $0.75$, $0.84$ and $0.79\,\text{m/s}$. The acceleration is therefore approximately constant, and it is obtained from the change over the whole interval, $\Delta v = 4.01\,\text{m/s} - 0 = 4.01\,\text{m/s}$ and $\Delta t = 5.0\,\text{s}$.
**Formula:** $a = \dfrac{\Delta v}{\Delta t}$, $x$: $T\cos\alpha - F_\mu = ma$ and $y$: $N + T\sin\alpha - mg = 0$, so $F_\mu = T\cos\alpha - ma$ and $N = mg - T\sin\alpha$
**Conversions:** All quantities are in SI units, and $\text{N} / \text{kg} = \text{m/s}^2$.
**Substitution:** The acceleration is $a = \dfrac{4.01\,\text{m/s}}{5.0\,\text{s}} = 0.802\,\text{m/s}^2$. The friction force:
```latex
\begin{aligned}
F_\mu &= 120\,\text{N}\cdot\cos 30\,{}^\circ \\
&\quad - 25\,\text{kg}\cdot 0.802\,\text{m/s}^2 \\
&= 103.9\,\text{N} - 20.05\,\text{N} \\
&= 83.9\,\text{N}
\end{aligned}
```
The normal force:
```latex
\begin{aligned}
N &= 25\,\text{kg}\cdot 9.81\,\text{m/s}^2 \\
&\quad - 120\,\text{N}\cdot\sin 30\,{}^\circ \\
&= 245.25\,\text{N} - 60\,\text{N} \\
&= 185\,\text{N}
\end{aligned}
```
**Answer:** a) The free-body diagram and the equations are above. b) $a \approx 0.80\,\text{m/s}^2$. c) $F_\mu \approx 84\,\text{N}$, two significant figures like the mass and the angle. d) $N \approx 185\,\text{N} \approx 1.9\cdot 10^2\,\text{N}$, two significant figures like the mass and the angle. The normal force is smaller than the weight, $245\,\text{N}$, because the vertical component of the rope, $T\sin\alpha = 60\,\text{N}$, supports part of the weight: the floor needs to support only the rest, $N + T\sin\alpha = mg$.
**Reasonableness:** The horizontal component of the rope, $104\,\text{N}$, is greater than the friction $84\,\text{N}$, so the net force $20\,\text{N}$ points forward and the box accelerates, as the table shows. The net force $ma = 20\,\text{N}$ is about a fifth of the horizontal component. Check in the vertical direction: $185\,\text{N} + 60\,\text{N} = 245\,\text{N} = mg$.

## fy4-5-L3-05
**Given:** $m = 80\,\text{kg}$, the load starts from rest and stops; phases $0$–$2.0\,\text{s}$, $2.0$–$6.0\,\text{s}$ and $6.0$–$8.0\,\text{s}$; the force of the rope from the table; $g = 9.81\,\text{m/s}^2$
**Find:** the lifting height $h$ in $\text{m}$ and the acceleration in each phase
**Principle:** The weight and the tension of the rope act on the load. According to Newton's second law the acceleration is obtained from the difference of the forces, and the direction of the acceleration is the direction of the net force: up when the force of the rope is greater than the weight, and down when it is smaller than the weight. When the acceleration is known, the height is obtained from the distances of the phases of the motion (chapter *Acceleration and uniformly accelerated motion*).
**Free-body diagram:** In the first phase the load is a rectangle, $y$ up. The weight $\overline{G}$ down and the tension $\overline{T}$ of the rope up, the tension longer than the weight. The velocity up and the acceleration up are drawn separately beside the diagram, not as forces. In the second phase the arrows are equally long, and in the third phase the tension is shorter than the weight.
```voimakuvio
pinta 0
G 784,8
T 880,7 ylös
v ylös
a ylös
```
**Reading the graph:** The readings of the table are divided into phases according to the moments $2.0\,\text{s}$ and $6.0\,\text{s}$. The sum of the readings of phase 1 is $881\,\text{N} + 878\,\text{N} + 883\,\text{N} = 2642\,\text{N}$, so the mean is $880.7\,\text{N}$. In phase 2 the sum is $2354\,\text{N}$ and the mean $784.7\,\text{N}$, and in phase 3 the sum is $2069\,\text{N}$ and the mean $689.7\,\text{N}$.
**Formula:** $T - mg = m a_y$, so $a_y = \dfrac{T - mg}{m}$. The greatest velocity is $v_\text{max} = a_1 \Delta t_1$, and the distances are $h_1 = \tfrac12 a_1 \Delta t_1^2$, $h_2 = v_\text{max}\,\Delta t_2$ and $h_3 = \tfrac12 v_\text{max}\,\Delta t_3$, because in the third phase the velocity decreases uniformly to zero. The height is $h = h_1 + h_2 + h_3$
**Conversions:** The forces are in newtons, the mass in kilograms and the times in seconds, so no conversions are needed. The weight is $mg = 80\,\text{kg}\cdot 9.81\,\text{m/s}^2 = 784.8\,\text{N}$.
**Substitution:** The accelerations:
```latex
\begin{aligned}
a_1 &= \frac{880.7 - 784.8}{80}\,\frac{\text{m}}{\text{s}^2} \\
&= 1.20\,\text{m/s}^2 \\
a_2 &= \frac{784.7 - 784.8}{80}\,\frac{\text{m}}{\text{s}^2} \\
&\approx 0 \\
a_3 &= \frac{689.7 - 784.8}{80}\,\frac{\text{m}}{\text{s}^2} \\
&= -1.19\,\text{m/s}^2
\end{aligned}
```
The greatest velocity is $v_\text{max} = 1.198\,\text{m/s}^2\cdot 2.0\,\text{s} = 2.397\,\text{m/s}$. The distances:
```latex
\begin{aligned}
h_1 &= \tfrac12\cdot 1.198\,\tfrac{\text{m}}{\text{s}^2}\cdot (2.0\,\text{s})^2 \\
&= 2.40\,\text{m} \\
h_2 &= 2.397\,\tfrac{\text{m}}{\text{s}}\cdot 4.0\,\text{s} \\
&= 9.59\,\text{m} \\
h_3 &= \tfrac12\cdot 2.397\,\tfrac{\text{m}}{\text{s}}\cdot 2.0\,\text{s} \\
&= 2.40\,\text{m}
\end{aligned}
```
The height is $h = 2.40\,\text{m} + 9.59\,\text{m} + 2.40\,\text{m} = 14.38\,\text{m}$.
**Answer:** a) The free-body diagram and the equation are above. b) $a_1 \approx 1.2\,\text{m/s}^2$ up, $a_2 \approx 0$ and $a_3 \approx -1.2\,\text{m/s}^2$, that is, the acceleration is down. c) In the third phase the net force points down, so the force of the rope is smaller than the weight although the velocity points up: the load slows down. The direction of the acceleration is the direction of the net force, not the direction of the motion. d) $h \approx 14.4\,\text{m}$, which to two significant figures is $14\,\text{m}$ like the mass $80\,\text{kg}$; the more precise value $14.4\,\text{m}$ is accepted in the answer box.
**Reasonableness:** In the uniform phase the force of the rope, $785\,\text{N}$, is equal to the weight, $785\,\text{N}$, as it should be. The changes in velocity cancel each other: in phase 3 the velocity decreases by $1.19\,\text{m/s}^2\cdot 2.0\,\text{s} = 2.38\,\text{m/s}$, that is, almost from $2.40\,\text{m/s}$ to zero, so the lift ends at rest as in the task. The height is also the product of the greatest velocity and a time: the acceleration and deceleration phases together cover the same distance as uniform velocity in $2.0\,\text{s}$, so $h = v_\text{max}\cdot 6.0\,\text{s} = 2.397\,\text{m/s}\cdot 6.0\,\text{s} = 14.4\,\text{m}$.
