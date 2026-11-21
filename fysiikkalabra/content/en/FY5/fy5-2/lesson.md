# Equilibrium of a body: forces and moments

> **Why** can a paint can be placed on the overhang of a plank lying across trestles, but only up to a certain point before the plank topples?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a painter is painting the wall of a house red. In front of the wall there are two painter&#x27;s trestles with a long plank on top of them. The painter stands on the plank between the trestles and reaches up under the eaves with a brush. The right end of the plank reaches far beyond the right-hand trestle, and a large paint tin stands on this overhang. There is nothing under the overhang, which raises the question of how far out along the overhang the tin can be moved before the plank topples." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Two equilibrium conditions
In the chapter *Moment: the turning effect of a force* we learned that a force rotates a body the more, the greater the moment of the force $M = Fr$. For a body to stay at rest, it is not enough that the forces cancel each other. A body is in **equilibrium** when it neither starts to move nor starts to rotate. For translation the condition is familiar from Newton's laws: the sum of the forces is zero. For rotation the condition is new: the sum of the moments of the forces is zero. In both cases in the figure two equal and opposite forces act on the ruler, so the sum of the forces is zero. On the left the forces lie along the same line and do not rotate the ruler. On the right they act along different lines, and their moments rotate the ruler in the same direction: the ruler starts to rotate, although its middle does not start to move.

<svg data-fig="pari" viewBox="0 0 600 330" role="img" aria-label="Schematic figure, a ruler on a table seen from above, two cases. On the left, equal and opposite forces F1 and F2 pull the ends of the ruler along the ruler on the same line: the sum of the forces and the sum of the moments are zero, and the ruler does not rotate. On the right, equal and opposite forces act on the ends of the ruler perpendicular to it along different lines: the sum of the forces is zero but the sum of the moments is not, and the ruler starts to rotate, shown by a curved arrow." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-pari.webp" x="0" y="0" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="65" y="11.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{does not rotate}$</div></foreignObject>
  <foreignObject x="402.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rotates}$</div></foreignObject>
  <foreignObject x="5.5" y="129.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{1}$</div></foreignObject>
  <foreignObject x="263.5" y="129.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{2}$</div></foreignObject>
  <foreignObject x="323.5" y="79.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{1}$</div></foreignObject>
  <foreignObject x="531.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{2}$</div></foreignObject>
  <foreignObject x="108.5" y="253.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <foreignObject x="121" y="289.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma M = 0$</div></foreignObject>
  <foreignObject x="408.5" y="253.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <foreignObject x="421" y="289.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\Sigma M \neq 0$</div></foreignObject>
</svg>

### Centre of mass
The Earth's gravitational pull acts on every part of a body. When the moment of the weight is calculated, however, the whole weight can be thought to act at a single point, the **centre of mass** of the body. The centre of mass of a uniform, symmetrical body, such as a plank of constant thickness, is at its middle. This is why the weight is drawn in a free-body diagram starting from the centre of mass. The common centre of mass of two bodies is between their centres of mass, nearer the heavier body. When a body is supported at one point, it stays in place only if the centre of mass is on the vertical line through the point of support: otherwise the moment of the weight about the point of support rotates the body.

```pysahdy
A plank of constant thickness is held up at one point. Where must the support be placed for the plank to stay horizontal, and why?
---
At the middle of the plank, below the centre of mass. The lever arm of the weight is then zero, so the weight does not rotate the plank.
```

### When a body topples
The **support area** of a body at rest is the region bounded by the points where the body touches the ground: for a box its base, for a chair the area between its legs. Toppling is judged with the vertical line through the centre of mass, the vertical projection of the centre of mass. When the line falls within the support area, the moment of the weight about the edge of the support area turns the body back onto the ground, and the body stays upright. If the line falls outside the support area, the moment of the weight about the lower edge rotates the body over the edge, and the body topples. A low, wide body therefore withstands a greater tilt than a tall, narrow one. Toppling is rotation about an edge, whereas sliding is the motion of the whole body along the surface, and friction prevents sliding. The boxes in the figure are on the same inclined plane, and friction prevents them from sliding, so they can only stay put or topple.

<svg data-fig="kaatuu" viewBox="0 0 600 372" role="img" aria-label="Scale drawing: two boxes on the same 30 degree inclined plane, friction prevents sliding. The low box is 0.60 m wide and 0.60 m high, the tall box 0.30 m wide and 0.80 m high. From the centre of mass of each a vertical dashed line runs down to the plane. The line of the low box meets the base of the box, so it stays upright. The line of the tall box meets the plane outside the lower edge of the base, so it topples, shown by a curved arrow." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-kaatuu.webp" x="1.2" y="0" width="597" height="380.6" preserveAspectRatio="none"/>
  <foreignObject x="132" y="305.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30^\circ$</div></foreignObject>
  <foreignObject x="72.5" y="120.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{stays upright}$</div></foreignObject>
  <foreignObject x="431.5" y="33.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{topples}$</div></foreignObject>
</svg>

```pysahdy
A box on an inclined plane topples even though friction prevents it from sliding. What decides whether the box topples?
---
The box topples if the vertical line through its centre of mass falls outside the support area. The moment of the weight about the lower edge then rotates the box over the edge.
```

## Formula: Equilibrium conditions
A body is in equilibrium when both the sum of the forces and the sum of the moments of the forces are zero:
```latex
\begin{aligned}
&\Sigma\overline{F} = \overline{0} \\
&\Sigma M = 0
\end{aligned}
```
where $\Sigma\overline{F}$ is the vector sum of the forces acting on the body ($\text{N}$) and $\Sigma M$ the sum of the moments of the forces about some point ($\text{Nm}$). The first is the **equilibrium condition for translation** and the second the **moment condition**, that is, the equilibrium condition for rotation. In components the first condition is $\Sigma F_x = 0$ and $\Sigma F_y = 0$. The moments are calculated as in the chapter *Moment: the turning effect of a force*: $M = Fr$, where $r$ is the lever arm of the force, and the sign tells the direction of rotation. In this chapter an anticlockwise moment is positive.

### Choosing the reference point
A body at rest does not rotate about any point, so the moment condition holds about every point. It is worth choosing the point of application of an unknown force as the reference point for the moments: the lever arm of that force is then zero, so the force does not appear in the moment condition. If a force is not perpendicular to a rod-like body (a plank, a rod), it is resolved into components. When the reference point is on the line of the rod, the moment is given by the component perpendicular to the rod multiplied by the distance from the reference point. In the figure the force $\overline{F}$ acting on the end of the rod makes the angle $\alpha$ with the rod: the component $F\cos\alpha$ along the rod passes through the hinge and does not rotate the rod, and the perpendicular component $F\sin\alpha$ gives the moment $M = F\sin\alpha \cdot r$.

<svg data-fig="komponentit" viewBox="0 0 600 290" role="img" aria-label="Schematic figure: a horizontal rod is on a hinge on a wall. A force F acts on the outer end of the rod, pointing obliquely up towards the wall and making the angle alpha with the rod. The force is resolved with dashed arrows into a component along the rod, which passes through the hinge and does not rotate the rod, and a component F sin alpha perpendicular to the rod, which gives a moment about the hinge. The lever arm of the moment is the length of the rod r." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-komponentit.webp" x="2.5" y="6.3" width="606.1" height="305.6" preserveAspectRatio="none"/>
  <foreignObject x="328" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="262" y="81.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="444" y="132.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F\sin\alpha$</div></foreignObject>
  <foreignObject x="326" y="215.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$F\cos\alpha$</div></foreignObject>
  <foreignObject x="250" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="96" y="209.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hinge}$</div></foreignObject>
</svg>

### Two supports
The plank in the figure rests on two supports. Let us take the moments about the centre of mass: the lever arm of the weight $\overline{G}$ is zero, the support force $\overline{N}_1$ rotates the plank clockwise and $\overline{N}_2$ anticlockwise. From the moment condition $N_2 r_2 - N_1 r_1 = 0$ we get
```latex
N_1 r_1 = N_2 r_2
```
where $N_1$ and $N_2$ are the support forces ($\text{N}$) and $r_1$ and $r_2$ the distances of the supports from the centre of mass ($\text{m}$). The support nearer the centre of mass thus carries the larger share of the weight. From the condition for translation the sum of the support forces is $N_1 + N_2 = G$.

<svg data-fig="lankku" viewBox="0 0 600 290" role="img" aria-label="Free-body diagram: a uniform plank on two supports, drawn as a rectangle. The weight G starts from the middle of the plank, the centre of mass, and points down. The support forces N1 and N2 point up and end at the lower surface of the plank at the supports. Support 1 is at the distance r1 from the centre of mass and support 2 at the shorter distance r2. The lengths of the arrows are to scale: N2 is longer than N1, and together they are as long as G." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-lankku.webp" x="17.9" y="14.4" width="574.2" height="285.9" preserveAspectRatio="none"/>
  <foreignObject x="309.5" y="227" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="112.5" y="191.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_{1}$</div></foreignObject>
  <foreignObject x="387.5" y="236.7" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_{2}$</div></foreignObject>
  <foreignObject x="201" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_1$</div></foreignObject>
  <foreignObject x="338.5" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_2$</div></foreignObject>
  <foreignObject x="435" y="77.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{plank}$</div></foreignObject>
</svg>

```pysahdy
A uniform plank rests on two supports. The supports are $0.40\,\text{m}$ and $1.20\,\text{m}$ from the centre of mass. Does each support carry half of the weight?
---
No. Since $N_1 r_1 = N_2 r_2$, the nearer support carries three times the force, which is $\tfrac{3}{4}$ of the weight, and the farther support carries $\tfrac{1}{4}$.
```

### Common centre of mass
For two bodies of masses $m_1$ and $m_2$, the common centre of mass is at
```kaavat
centre of mass :: x_\text{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}
```
where $x_1$ and $x_2$ are the positions of the centres of mass of the bodies ($\text{m}$) on the same axis. The formula follows from the moment condition: if the bodies are supported at $x_\text{cm}$, the moments of the weights about the point of support cancel each other. A loaded plank resting on two supports topples when the common centre of mass of the plank and the load moves outside the interval between the supports.

## Worked example
Two carriers carry a uniform horizontal log of length $4.00\,\text{m}$ and mass $60.0\,\text{kg}$. Carrier A holds the front end of the log, and carrier B is $1.00\,\text{m}$ from the back end. With what force does each carrier hold the log? The carriers support the log vertically upwards.

<svg data-fig="hirsi" viewBox="0 0 600 330" role="img" aria-label="Free-body diagram: a uniform log as a rectangle. Carrier A is at the left end of the log and carrier B 1.00 m from the right end. The weight G starts from the middle of the log, downwards. The forces of the carriers NA and NB point up and end at the lower surface of the log. Distances: from A to the centre of mass 2.00 m, from the centre of mass to B 1.00 m. A is marked as the reference point and anticlockwise as the positive direction of rotation. The lengths of the arrows are to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-2-hirsi.webp" x="1.2" y="2.5" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="309.5" y="259" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="66.5" y="215.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_\text{A}$</div></foreignObject>
  <foreignObject x="387.5" y="255" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_\text{B}$</div></foreignObject>
  <foreignObject x="148.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.00\,\text{m}$</div></foreignObject>
  <foreignObject x="313.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.00\,\text{m}$</div></foreignObject>
  <foreignObject x="423.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.00\,\text{m}$</div></foreignObject>
  <foreignObject x="46" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="440" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <foreignObject x="156" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
</svg>

<!-- vaihe -->

**Given and find.** The log: $L = 4.00\,\text{m}$, $m = 60.0\,\text{kg}$, $g = 9.81\,\text{m/s}^2$. The centre of mass is in the middle, $2.00\,\text{m}$ from A; B is $3.00\,\text{m}$ from A. We are asked for the forces of the carriers, $N_\text{A}$ and $N_\text{B}$.

<!-- vaihe -->

**Principle.** The log is at rest, so it is in equilibrium for both translation and rotation. The body is the log. In the free-body diagram the forces acting on it are the weight $\overline{G}$ downwards from the centre of mass and the forces of the carriers $\overline{N}_\text{A}$ and $\overline{N}_\text{B}$ upwards. A is chosen as the reference point, so the lever arm of $N_\text{A}$ is zero, and the anticlockwise moment is positive. The unknown $N_\text{B}$ is obtained from the moment condition and $N_\text{A}$ then from the sum of the forces.

<!-- vaihe -->

**Formula solved.** The moment condition about A and the condition $\Sigma F_y = 0$, with upwards positive:
```latex
\begin{aligned}
&N_\text{B} r_\text{B} - G r_G = 0 \\
&N_\text{B} = \frac{m g r_G}{r_\text{B}} \\[6pt]
&N_\text{A} + N_\text{B} - G = 0 \\
&N_\text{A} = m g - N_\text{B}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the mass is in kilograms and the lengths in metres. The lever arms of the forces are $r_G = 2.00\,\text{m}$ and $r_\text{B} = 3.00\,\text{m}$, because the forces are vertical and the log horizontal.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&G = m g \\
&= 60.0\,\text{kg} \cdot 9.81\,\text{m/s}^2 \\
&= 588.6\,\text{N} \\[6pt]
&N_\text{B} = \frac{G r_G}{r_\text{B}} \\
&= \frac{588.6\,\text{N} \cdot 2.00\,\text{m}}{3.00\,\text{m}} \\
&= 392.4\,\text{N} \\[6pt]
&N_\text{A} = G - N_\text{B} \\
&= 588.6\,\text{N} - 392.4\,\text{N} \\
&= 196.2\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** Carrier A holds the log with a force of $196\,\text{N}$ and carrier B with a force of $392\,\text{N}$. The results are given to three significant figures, like the mass $60.0\,\text{kg}$ and the lengths.

<!-- vaihe -->

**Reasonableness.** The sum of the forces is $196\,\text{N} + 392\,\text{N} = 588\,\text{N}$, the weight of the log. B is $1.00\,\text{m}$ and A $2.00\,\text{m}$ from the centre of mass, so B carries twice as much as A, as the moment condition about the centre of mass requires: $196\,\text{N} \cdot 2.00\,\text{m} = 392\,\text{N} \cdot 1.00\,\text{m}$.

## Common misconception
Many think that two supports always carry half of the weight each, or that the support farther away carries more because its "lever" is longer. The moment condition about the centre of mass shows the opposite: $N_1 r_1 = N_2 r_2$, so the support *nearer* the centre of mass carries more. Each support carries half of the weight only when the supports are at equal distances from the centre of mass.

Another mistake is to think that a loaded plank topples as soon as the load is past a support. The plank topples only when the *common* centre of mass of the plank and the load is past the support: until then the weight of the plank itself between the supports cancels the moment of the load.

A third mistake is to believe that moments must be calculated only about the centre of mass or a support. The moment condition holds about any point, and the same forces are obtained from different points. A good choice merely shortens the calculation.

## Summary
- A body is in equilibrium when the sum of the forces is zero, $\Sigma\overline{F} = \overline{0}$ (for translation), and the sum of the moments of the forces is zero, $\Sigma M = 0$ (for rotation).
- The moment condition holds about any point. It is worth choosing the point of application of an unknown force as the reference point.
- The weight acts at the centre of mass, which is in the middle of a uniform, symmetrical body. For a plank on two supports $N_1 r_1 = N_2 r_2$: the support nearer the centre of mass carries more.
- A supported body stays upright when the vertical line through the centre of mass falls within the support area; otherwise it topples.
