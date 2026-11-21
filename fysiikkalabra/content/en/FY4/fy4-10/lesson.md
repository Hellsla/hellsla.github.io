# Conservation of momentum and one-dimensional collisions

> **Why** can a cue ball stop dead when it hits a stationary ball head-on, while the other ball carries on at almost the same velocity?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a billiard table seen close up in the light of a lamp hanging above it. A cue points onto the table from the lower left, and has just struck the white cue ball. The cue ball has hit a red ball head-on, and a moment after the collision it has stopped in the middle of the table; a faint trail behind it shows the distance it travelled. The red ball speeds ahead towards the right edge of the table, with motion lines behind it. At the back of the table there are three more balls." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A system and its total momentum
In the chapter *Momentum and impulse* you learned that the momentum of an object is $\overline{p} = m\overline{v}$ and that the impulse of a constant net force changes it: $\Delta\overline{p} = \Sigma\overline{F}\,\Delta t$. In a collision, however, there are two objects that act on each other. So we look at them together as a **system**. The **total momentum** of a system is the vector sum of the momenta of its objects, $\overline{p}_\text{tot} = \overline{p}_1 + \overline{p}_2$.

The forces that the objects of the system exert on each other are **internal forces**, for example the forces of the bumpers of two carts on each other in a collision. Forces that come from outside the system are **external forces**, for example the weight of the carts, the normal force of the track and friction.

### Why the total momentum is conserved
When cart 1 pushes cart 2 with a force $\overline{F}$, by Newton's third law cart 2 pushes cart 1 with an equally large force $-\overline{F}$ in the opposite direction. The forces begin and end at the same moment, so they act for the same time $\Delta t$. If the force is constant, the momentum of cart 2 changes by the impulse $\overline{F}\,\Delta t$, and the momentum of cart 1 changes by the same amount in the opposite direction. The momentum that one cart gains is exactly what the other loses. The total momentum does not change. The same holds even if the force changes during the collision, because at every moment the forces are equally large and opposite.

<svg data-fig="vuorovaikutus" viewBox="0 0 600 340" role="img" aria-label="Diagram, not to scale: two air-track carts during a collision. The spring bumper between the carts is compressed. At the top are red force arrows: cart 1 pushes cart 2 to the right with a force F, and cart 2 pushes cart 1 to the left with an equally large force in the opposite direction, −F. Both forces act for the same time Δt. At the bottom the purple arrows are the changes in momentum: the change of cart 1, Δp1 = −FΔt, points to the left and that of cart 2, Δp2 = FΔt, to the right, equally long. Their sum is zero." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-vuorovaikutus.webp" x="1.2" y="1.2" width="597" height="348.3" preserveAspectRatio="none"/>
  <foreignObject x="240" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="350" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="488.5" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="72.5" y="45.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$-\overline{F}$</div></foreignObject>
  <foreignObject x="283.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="87.5" y="257.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_1 = -\overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="373.5" y="257.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_2 = \overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="221" y="299.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta\overline{p}_1 + \Delta\overline{p}_2 = \overline{0}$</div></foreignObject>
</svg>

This reasoning works only when external forces do not change the momentum. On a horizontal air track the weight and the normal force cancel each other, and friction is very small. Colliding cars, on the other hand, do feel the friction of the road, but the collision lasts only a fraction of a second. The forces of the bumpers are then much larger than friction, so the impulse of friction during the collision remains negligibly small. This gives the **law of conservation of momentum**: when the sum of the external forces acting on a system is zero, or their impulse during the collision is negligibly small, the total momentum of the system is conserved.

```pysahdy
In a collision of two cars, road friction acts on the cars. Why can the total momentum still be treated as conserved?
---
The collision lasts only a fraction of a second, and the forces between the bumpers are much greater than friction. The impulse of friction is then negligibly small.
```

### Types of collisions
Momentum is conserved in every collision when the condition of the conservation law is met. Kinetic energy is not always conserved. A collision is **elastic** if the total kinetic energy of the objects after the collision is equal to that before it. Steel balls, billiard balls and carts with spring bumpers collide almost elastically. A collision is **inelastic** if some of the kinetic energy changes into other forms of energy. The objects then change shape, and kinetic energy becomes their internal energy and sound. When the objects stick together and move on together, the collision is **perfectly inelastic**, and the kinetic energy decreases the most: the largest possible part of it is transformed into other forms of energy.

<svg data-fig="tarra" viewBox="0 0 600 360" role="img" aria-label="Diagram to scale: two carts of equal mass on an air track, before the collision at the top and after it at the bottom. Before the collision cart 1 moves to the right at velocity v, and its momentum p is a purple arrow; cart 2 is at rest. The ends of the carts have hook-and-loop tape. After the collision the carts have stuck together and move together at half of the original velocity; the blue arrow is half as long. The purple arrow of the common momentum is as long as the momentum of cart 1 before the collision." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-tarra.webp" x="0" y="0" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="36" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{before}$</div></foreignObject>
  <foreignObject x="36" y="185.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{after}$</div></foreignObject>
  <foreignObject x="160" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="390" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="260" y="69.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="260" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
  <foreignObject x="358.5" y="65.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{v}_2 = \overline{0}$</div></foreignObject>
  <foreignObject x="240" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="340" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="274" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\tfrac{1}{2}\overline{v}$</div></foreignObject>
  <foreignObject x="340" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
</svg>

In the figure, carts of equal mass stick together with hook-and-loop tape. The total momentum is the same before and after, but now the same momentum is shared by twice the mass, so the common velocity is half of the original. Kinetic energy $\tfrac12 mv^2$ is not conserved: twice the mass and half the velocity give half of the original kinetic energy. The other half becomes internal energy of the tape and the carts.

```pysahdy
In a perfectly inelastic collision the carts stick together. Where does the kinetic energy that "disappears" go?
---
It does not vanish but becomes internal energy of the tape and the carts. Total energy is conserved even though kinetic energy decreases.
```

### An explosion
In an **explosion**, a system that is at rest or moving together breaks into parts because of internal forces: a spring is released between carts, skaters push each other away, or gunpowder pushes a bullet and a rifle apart. If the system is at rest at first, its total momentum is zero and stays zero. When a system at rest breaks into two parts, the parts get momenta of equal magnitude in opposite directions, and the lighter part gets the greater velocity. This is why a rifle kicks backwards when the bullet goes forwards. If there are more parts, the vector sum of their momenta is zero, but the momenta of the individual parts can differ in magnitude. Kinetic energy increases in an explosion, because energy of the spring, the muscles or the gunpowder is changed into kinetic energy.

```pysahdy
A skater stands at rest on ice and throws a heavy ball forward. Why does the skater slide backward?
---
The ball gains momentum forwards, and the total momentum of the system stays zero. So the skater gains an equal momentum backwards.
```

### The answer to the opening question
Billiard balls have equal masses, and their collision is almost elastic. When the velocity of the cue ball is $v$, conservation of momentum says that the sum of the velocities of the balls stays the same: $v_1' + v_2' = v$. Conservation of kinetic energy says that the sum of the squares of the velocities stays the same: $v_1'^2 + v_2'^2 = v^2$. Squaring the first condition and subtracting the second gives $2 v_1' v_2' = 0$, so one of the balls is at rest after the collision. The cue ball cannot pass through the other ball, so it stops, and the other ball moves on with velocity $v$. In reality the balls also spin and the collision is not perfectly elastic, so the cue ball may keep moving a little.

<figure class="unit-photo"><img src="pics/fy4/newtons-cradle.webp" alt="Newton's cradle: a row of hanging steel balls; the leftmost one is moving and therefore blurred."><figcaption>In Newton's cradle, a ball swinging in from the left hits the balls at rest. The moving ball is blurred in the photo.</figcaption></figure>

## Formula: Conservation of momentum

### The conservation law with vectors and in one dimension
When the sum of the external forces acting on a system is zero, or their impulse during a collision or explosion is negligibly small, the total momentum is the same before and after:
```latex
\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'
```
where $\overline{p}_1$ and $\overline{p}_2$ are the momenta of the objects before and $\overline{p}_1'$ and $\overline{p}_2'$ their momenta after ($\text{kg}\cdot\text{m/s}$).

In a one-dimensional collision, all the velocities lie on the same line. We choose a positive direction, and then every velocity is a signed number: the velocity of an object moving in the opposite direction is negative. The conservation law becomes
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = m_1 v_1' + m_2 v_2'
\end{aligned}
```
where $m_1$ and $m_2$ are the masses of the objects ($\text{kg}$), $v_1$ and $v_2$ their velocities before and $v_1'$ and $v_2'$ their velocities after ($\text{m/s}$).

### Perfectly inelastic collision
When the objects stick together, they have a common velocity $v'$ after the collision:
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = (m_1 + m_2)\,v'
\end{aligned}
```
where $v'$ is the common velocity of the objects after the collision ($\text{m/s}$). For example, when a $0.40\,\text{kg}$ cart at a velocity of $0.60\,\text{m/s}$ sticks to a similar cart at rest, the common velocity is $0.30\,\text{m/s}$, and the kinetic energy decreases from $0.072\,\text{J}$ to $0.036\,\text{J}$.

### Elastic collision
In an elastic collision, in addition to momentum, the total kinetic energy of the objects is conserved:
```latex
\begin{aligned}
&E_{\text{k},1} + E_{\text{k},2} \\
&\quad = E_{\text{k},1}' + E_{\text{k},2}'
\end{aligned}
```
where $E_\text{k} = \tfrac12 mv^2$ is the kinetic energy of each object before and $E_\text{k}'$ after ($\text{J}$). When the velocity of one object after the collision is known, the other follows from the law of conservation of momentum, and by comparing the kinetic energies we can see whether the collision was elastic. When an object hits an object of equal mass at rest elastically and head-on, the objects exchange velocities.

<svg data-fig="tyypit" viewBox="0 0 600 434" role="img" aria-label="Diagram, momenta to scale: three events for two carts of equal mass, before on the left and after on the right. At the top an elastic collision: before, cart 1 has a momentum to the right and cart 2 is at rest; after, cart 1 is at rest and cart 2 has the same momentum; kinetic energy is conserved. In the middle a perfectly inelastic collision: the carts stick together, and the common momentum is as large as before; kinetic energy decreases. At the bottom an explosion: before, the carts are together at rest and the total momentum is zero; after, the carts have momenta of equal magnitude in opposite directions; kinetic energy increases." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-tyypit.webp" x="0" y="0" width="600" height="438.8" preserveAspectRatio="none"/>
  <foreignObject x="90" y="45.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{elastic: } E_\text{k}\ \text{conserved}$</div></foreignObject>
  <foreignObject x="90" y="175.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{perfectly inelastic: } E_\text{k}\ \text{decreases}$</div></foreignObject>
  <foreignObject x="90" y="305.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{explosion: } E_\text{k}\ \text{increases}$</div></foreignObject>
  <foreignObject x="113.5" y="349.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$p_\text{tot} = 0$</div></foreignObject>
  <foreignObject x="113.5" y="3.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{before}$</div></foreignObject>
  <foreignObject x="410" y="3.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{after}$</div></foreignObject>
</svg>

When external forces act, the law of conservation of momentum is used only across the collision or explosion itself, a short time from beginning to end. Before and after, external forces such as friction or weight can change the motion of the objects, and then the motion is studied with other laws, for example the work–energy principle.

## Worked example
In a rail yard, freight car A, of mass $32\,000\,\text{kg}$, moves at $1.5\,\text{m/s}$ and catches up with car B, of mass $18\,000\,\text{kg}$, moving in the same direction at $0.50\,\text{m/s}$. The cars couple together and continue together. What is the common velocity of the cars immediately after coupling?

<!-- vaihe -->

**Given and find.** $m_\text{A} = 32\,000\,\text{kg}$, $v_\text{A} = 1.5\,\text{m/s}$, $m_\text{B} = 18\,000\,\text{kg}$ and $v_\text{B} = 0.50\,\text{m/s}$. We are asked for the common velocity $v'$ immediately after coupling.

<!-- vaihe -->

**Principle.** We choose both cars as the system and the direction of motion of the cars as the positive direction. Coupling takes a moment, and during it the forces of the couplers are internal forces. The weight and the normal force of the rails cancel each other, and the impulse of rolling resistance is negligibly small during the short coupling, so the total momentum is conserved. The cars stick together, so the collision is perfectly inelastic.

<!-- vaihe -->

**Formula solved.** The momentum before is equal to the momentum of the combined object after:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} + m_\text{B} v_\text{B} \\
&\quad = (m_\text{A} + m_\text{B})\,v' \\[6pt]
&v' = \frac{m_\text{A} v_\text{A} + m_\text{B} v_\text{B}}{m_\text{A} + m_\text{B}}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: the masses are in kilograms and the velocities in $\text{m/s}$.

<!-- vaihe -->

**Substitution.** First we calculate the momenta before coupling and then the common velocity:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} \\
&= 32\,000\,\text{kg} \cdot 1.5\,\tfrac{\text{m}}{\text{s}} \\
&= 48\,000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&m_\text{B} v_\text{B} \\
&= 18\,000\,\text{kg} \cdot 0.50\,\tfrac{\text{m}}{\text{s}} \\
&= 9000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&v' \\
&= \frac{48\,000 + 9000}{50\,000} \cdot \frac{\text{kg}\cdot\text{m/s}}{\text{kg}} \\
&= 1.14\,\tfrac{\text{m}}{\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Result.** The common velocity of the cars is $v' \approx 1.1\,\text{m/s}$ in the original direction of motion of the cars. The result is given to two significant figures, like the velocities $1.5\,\text{m/s}$ and $0.50\,\text{m/s}$.

<!-- vaihe -->

**Reasonableness.** The common velocity lies between the initial velocities of the cars, $0.50\,\text{m/s}$ and $1.5\,\text{m/s}$, and closer to the velocity of the heavier car A, as it should. The kinetic energy decreases from $38.3\,\text{kJ}$ to $32.5\,\text{kJ}$, that is, by about $15\,\%$, which fits a perfectly inelastic collision: kinetic energy changes into internal energy of the couplers and buffers, and into sound.

## Common misconception
Many people think that kinetic energy is conserved in a collision in the same way as momentum. Momentum is always conserved when the impulse of the external forces is negligibly small, but kinetic energy is conserved only in an elastic collision. If the velocity of carts that stick together is calculated from conservation of kinetic energy, the result is too large.

Another mistake is to forget the signs. When objects move towards each other, their momenta are in opposite directions, and one of them is negative. A third mistake is to think that momentum disappears when a clay ball dropped on the floor stops. The momentum of the ball passes to the Earth: the ball and the Earth form a system whose total momentum is conserved, but the mass of the Earth is so great that the change in its velocity cannot be noticed.

## Summary
- The total momentum of a system is conserved when the sum of the external forces is zero or their impulse during the collision or explosion is negligibly small: $\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'$.
- Conservation follows from Newton's third law: the internal forces in a collision are equally large and opposite and act for the same time, so the changes in the momenta of the objects cancel each other.
- In one dimension we choose a positive direction, and velocities are signed: $$\begin{aligned} &m_1 v_1 + m_2 v_2 \\ &= m_1 v_1' + m_2 v_2' \end{aligned}$$
- In an elastic collision, kinetic energy is also conserved. In an inelastic collision some of the kinetic energy changes into internal energy, and in a perfectly inelastic collision the objects move on together with a common velocity.
- In an explosion, the total momentum of a system at rest stays zero: when it splits into two parts, the parts get momenta of equal magnitude in opposite directions, and kinetic energy increases.
