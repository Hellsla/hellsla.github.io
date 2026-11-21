# Moving in a circle: period and speed

> **Why** does a child standing at the edge of a roundabout rush along much faster than a child standing next to the centre pole, even though both complete a turn equally fast?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a playground roundabout turning on a summer day. One child stands at the edge of the roundabout, another near the centre pole. At each child there is a blue arrow in the direction of motion, along the tangent of the path; the arrow of the child at the edge is twice as long as that of the child near the centre." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
An object is in **circular motion** when its path is a circle: the object stays at the same distance from the centre of the path all the time. This distance is the radius $r$ of the path. A child on a roundabout, a car going round a roundabout and a satellite orbiting the Earth are in circular motion, or almost. If an object travels the same distance in every equal time interval, the magnitude of its velocity, that is, its speed, stays the same. The motion is then **uniform circular motion**. In this chapter we look only at uniform circular motion.

### The velocity points along the tangent
Velocity is a vector $\overline{v}$ with a magnitude and a direction. At every moment the velocity points in the direction in which the object is just then moving. On a circular path this direction is the direction of the **tangent** of the path, which is perpendicular to the radius drawn from the centre. As the object goes round, the direction of the tangent turns all the time. In uniform circular motion the velocity vectors are therefore all equally long but point in different directions: the magnitude of the velocity stays the same, but the velocity changes.

<svg data-fig="tangent" viewBox="0 0 600 380" role="img" aria-label="Formula figure: an object circles a circular path anticlockwise. A blue velocity vector is drawn at four points: all are equally long and along the tangent of the path, perpendicular to the radius drawn from the centre. On the right it says that the magnitudes of the velocities are equal but the vectors are different." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-tangent.webp" x="0" y="1.2" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="302" y="95.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="35" y="35.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="64" y="267.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_3$</div></foreignObject>
  <foreignObject x="264" y="319.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_4$</div></foreignObject>
  <foreignObject x="222" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="380" y="135.5" width="206" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_1 = v_2 = v_3 = v_4$</div></foreignObject>
  <foreignObject x="380" y="207.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{v}_1 \neq \overline{v}_2$</div></foreignObject>
</svg>

```pysahdy
An object goes round a circle counterclockwise and is just at the top of its path. In which direction does its velocity point?
---
To the left. The velocity is along the tangent, perpendicular to the vertical radius, so it is horizontal and points in the direction of motion.
```

### When the string breaks
A puck tied to a string circles a peg on the ice. The string pulls the puck towards the peg and turns its direction of motion all the time. If the string breaks, no force acts on the puck horizontally any more: the friction of the ice is assumed small, and the vertical forces, the weight and the support force of the ice, cancel each other. By Newton's first law the puck then continues in uniform motion in a straight line with the velocity it had at the moment of the break. The puck therefore leaves along the tangent of the path, not straight away from the peg. In the same way, water drops flying off the rim of a spinning umbrella leave along the tangent.

<svg data-fig="release" viewBox="0 0 600 340" role="img" aria-label="Formula figure: a puck tied to a string circles a peg anticlockwise along a circular path drawn with a dashed line. At the lowest point of the path the string breaks, and the puck continues straight to the right along the tangent of the path. The positions of the puck are marked at equal time intervals: the gaps are equally long, so the speed stays the same." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-release.webp" x="1.2" y="1.2" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="510.5" y="219.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="70.5" y="275.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{the string breaks}$</div></foreignObject>
  <foreignObject x="292" y="275.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{straight, steadily}$</div></foreignObject>
</svg>

### A change of direction is a change of velocity
The change of velocity $\Delta\overline{v}$ is seen when two successive velocity vectors are drawn starting from the same point. The change $\Delta\overline{v}$ is the vector that must be added to $\overline{v}_1$ to get $\overline{v}_2$. On a circular path the vectors are equally long but their directions differ, so $\Delta\overline{v}$ is not zero when the time interval is shorter than one revolution. Acceleration means a change of velocity, not only a change of speed. In uniform circular motion an object is therefore accelerating, and by Newton's second law a net force that is not zero acts on it. This net force points to the side of the centre of the circle, that is, to the inside of the path, not outwards. The magnitude of the acceleration is calculated in the chapter *Centripetal acceleration and the equation of motion in a circle*.

<svg data-fig="dv" viewBox="0 0 600 340" role="img" aria-label="Formula figure: on the left an arc of a circular path and two successive positions of an object, where the velocities are equally long but point in different directions. On the right the same vectors have been moved to start from the same point, and the black arrow from the tip of the first to the tip of the second is the change of velocity. The second velocity is the first velocity plus the change of velocity." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-dv.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="221" y="96" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="-3" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="490" y="137" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="375" y="233.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="394" y="166.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\Delta\overline{v}$</div></foreignObject>
  <foreignObject x="366" y="297.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{v}_2 = \overline{v}_1 + \Delta\overline{v}$</div></foreignObject>
</svg>

```pysahdy
An object goes round a circle at constant speed. Is its acceleration zero?
---
No. The speed stays the same, but the direction of the velocity changes all the time, so the velocity changes and the object accelerates.
```

## Formula: Speed
Uniform circular motion is described by the **period** $T$, which is the time in which the object goes round the path once. Its reciprocal is the **rotation frequency** $f$, which tells how many revolutions the object makes per unit of time:
```kaavat
rotational frequency :: f = \frac{1}{T}
```
where $f$ is the rotation frequency ($\tfrac{1}{\text{s}}$) and $T$ the period ($\text{s}$). When the period is $T = 0.50\,\text{s}$, the object makes $2.0$ revolutions per second, that is, $f = 2.0\,\tfrac{1}{\text{s}}$. The rotation frequency is also often given in revolutions per minute. For example, $45\,\tfrac{1}{\text{min}}$ is converted by substituting $1\,\text{min} = 60\,\text{s}$, which gives $45\,\tfrac{1}{\text{min}} = \tfrac{45}{60\,\text{s}} = 0.75\,\tfrac{1}{\text{s}}$.

<figure class="unit-photo"><img src="pics/fy5/playground-carousel.webp" alt="A red hand-pushed roundabout in a playground. The round floor has rails at the edge and an axle in the middle."><figcaption>A playground roundabout. Every point of the roundabout makes a revolution in the same time, but the distance travelled at the edge is longer than near the axle.</figcaption></figure>

In one revolution the object travels a distance equal to the circumference $2\pi r$ of the circle, and this takes the period $T$. Because the speed is constant, the magnitude of the velocity on the circular path, the **speed along the path**, is the distance travelled divided by the time:
```latex
v = \frac{2\pi r}{T} = 2\pi r f
```
where $v$ is the speed ($\text{m/s}$), $r$ the radius of the path ($\text{m}$), $T$ the period ($\text{s}$) and $f$ the rotation frequency ($\tfrac{1}{\text{s}}$). The latter form is obtained by replacing $\tfrac{1}{T}$ with the rotation frequency $f$.

The formula answers the opening question. All parts of the roundabout complete a turn in the same time $T$, but the child at the edge goes round a bigger circle. The speed is directly proportional to the radius when the period is the same: a child standing twice as far from the centre travels twice the distance in the same time, so the speed is doubled. At the same radius, halving the period doubles the speed.

<svg data-fig="two-radii" viewBox="0 0 600 380" role="img" aria-label="Formula figure from above: two points A and B are on the same radius of a rotating roundabout, A at the distance r and B at the distance 2r from the centre. In the same time each turns through the same fraction of a revolution, but the arc travelled by B is twice as long, and the blue velocity vector of B is twice as long as that of A. The proportions are to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-3-two-radii.webp" x="-1.2" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="240" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="380" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <foreignObject x="146" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="286" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="168" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{A}$</div></foreignObject>
  <foreignObject x="241.5" y="38" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{B}$</div></foreignObject>
  <foreignObject x="240" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{A}$</div></foreignObject>
  <foreignObject x="370" y="208" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{B}$</div></foreignObject>
  <foreignObject x="440" y="105.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{same } T$</div></foreignObject>
  <foreignObject x="440" y="161.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{B} = 2\,s_\text{A}$</div></foreignObject>
  <foreignObject x="440" y="217.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v_\text{B} = 2\,v_\text{A}$</div></foreignObject>
</svg>

```pysahdy
An object goes round a circle of radius $2.0\,\text{m}$, and one revolution takes $4.0\,\text{s}$. What is its speed along the path?
---
The speed is $v = \tfrac{2\pi r}{T}$. It is $\tfrac{2\pi \cdot 2.0\,\text{m}}{4.0\,\text{s}} \approx 3.1\,\text{m/s}$.
```

## Worked example
The diameter of the drum of a washing machine is $46\,\text{cm}$. In the spin cycle the drum turns $1200$ revolutions per minute. What is the speed of a sock pressed against the wall of the drum?

<!-- vaihe -->

**Given and find.** The diameter of the drum is $d = 46\,\text{cm}$ and the rotation frequency $f = 1200\,\tfrac{1}{\text{min}}$. We want the speed $v$ of the sock.

<!-- vaihe -->

**Principle.** The sock turns with the drum on its wall, so it is in uniform circular motion whose radius is the radius of the drum, $r = \tfrac{d}{2}$. In one revolution the sock travels the circumference $2\pi r$, and there are $f$ revolutions per unit of time, so the speed is $v = 2\pi r f$.

<!-- vaihe -->

**Rearranged formula.** Substitute the radius using the diameter:
```latex
\begin{aligned}
&v = 2\pi r f, \quad r = \frac{d}{2} \\
&v = \pi d f
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The diameter is $46\,\text{cm} = 46 \cdot 0.01\,\text{m} = 0.46\,\text{m}$. The rotation frequency is $f = 1200\,\tfrac{1}{\text{min}} = \tfrac{1200}{60\,\text{s}} = 20\,\tfrac{1}{\text{s}}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
v &= \pi d f \\
&= \pi \cdot 0.46\,\text{m} \cdot 20\,\tfrac{1}{\text{s}} \\
&= 28.90\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Result.** The speed of the sock is about $29\,\text{m/s}$. The result is given with two significant figures, because the diameter $46\,\text{cm}$ is given with two figures.

<!-- vaihe -->

**Reasonableness.** The circumference of the drum is $\pi \cdot 0.46\,\text{m} \approx 1.45\,\text{m}$, and the drum turns $20$ revolutions per second, so the sock travels about $20 \cdot 1.45\,\text{m} \approx 29\,\text{m}$ per second. The period is $T = \tfrac{1}{f} = 0.050\,\text{s}$, and the formula $v = \tfrac{2\pi r}{T} = \tfrac{2\pi \cdot 0.23\,\text{m}}{0.050\,\text{s}}$ gives the same $28.9\,\text{m/s}$. That is about $29 \cdot 3.6\,\tfrac{\text{km}}{\text{h}} \approx 104\,\tfrac{\text{km}}{\text{h}}$, the order of magnitude of motorway speed, which fits a fast spin cycle.

## Common misconception
Many think that in uniform circular motion the velocity does not change, because the speedometer shows the same reading all the time. The speedometer, however, shows only the magnitude of the velocity, that is, the speed. Velocity is a vector, and its direction turns all the time, so the velocity changes and the object is accelerating. Without a net force the object would not stay on the circular path but would continue in a straight line.

Another mistake is to think that when the string breaks the object flies straight away from the centre. No force pushes the object outwards. When the string stops pulling, the object continues in the direction of its velocity at that moment, that is, along the tangent of the path.

Common mistakes in calculations are substituting the diameter in place of the radius in the formula $v = \tfrac{2\pi r}{T}$ and substituting the rotation frequency in revolutions per minute without converting it to revolutions per second.

## Summary
- In circular motion the path of an object is a circle of radius $r$. In uniform circular motion the speed stays the same.
- The velocity $\overline{v}$ is at every moment along the tangent of the path. Its direction changes all the time, so the velocity changes and the object is accelerating, even though the speed is constant.
- When no net force acts on the object any more, it continues in a straight line along the tangent of the path.
- The period $T$ is the time of one revolution, and the rotation frequency $f = \tfrac{1}{T}$ is the number of revolutions per unit of time.
- The speed $v = \tfrac{2\pi r}{T} = 2\pi r f$ is directly proportional to the radius when the period is the same.
