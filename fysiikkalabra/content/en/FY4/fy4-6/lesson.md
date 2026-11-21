# Weight, friction and the inclined plane

> **Why** does a moving box stay in place on a slanted loading ramp, but start to slide when the ramp is made a little steeper?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: moving day in the yard of an apartment building. The rear doors of a van are open, and a wooden loading ramp slopes down from the floor of the van to the ground. In the middle of the ramp there is a cardboard moving box that stays in place. Inside the van there are more boxes, and a mover is carrying one box beside the ramp." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Weight
The **weight** $\overline{G}$ of an object is the force with which the Earth pulls the object. It always points straight down, also on a slope, and in a free-body diagram it is drawn from the center of the object. The magnitude of the weight is the product of the mass and the acceleration of free fall, $mg$. Mass describes the inertia of an object, that is how hard it is to change its state of motion, and it is the same everywhere. Weight, on the other hand, depends on the place: on the surface of the Moon $g = 1.62\,\text{m/s}^2$, so the weight of a $60\,\text{kg}$ person there is about $97\,\text{N}$, whereas on Earth it is about $590\,\text{N}$.

```pysahdy
An astronaut whose mass is $80\,\text{kg}$ moves to the Moon. Does the astronaut's mass change, the weight, or both?
---
The mass stays the same, but the weight becomes smaller, because the Moon's free-fall acceleration is smaller than the Earth's.
```

### Static friction and sliding friction
When two surfaces touch each other, they resist sliding relative to each other. This force parallel to the surface is **friction** $\overline{F}_\mu$. The surfaces are not perfectly smooth: tiny bumps catch on each other, and there are attractive forces between the particles of the surfaces. The harder the surfaces are pressed against each other, that is the greater the normal force $N$ is, the greater the friction can be.

When a box on a floor is pulled only weakly, it does not move. Then **static friction** acts on it, equal to the pull and in the opposite direction, so the net force is zero. Static friction is therefore not constant but adapts to the situation. It does have an upper limit, though. When the pull exceeds it, the box starts to slide, and the friction changes into **sliding friction**. Sliding friction is usually smaller than the maximum (fully developed) static friction, and at ordinary speeds it is approximately constant.

<svg data-fig="kitka" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: on the horizontal axis the horizontal force F pulling the box in newtons from zero to 80, on the vertical axis the friction force of the floor in newtons from zero to 60. A normal force of 100 newtons presses the box against the floor. At first the friction force grows equal to the pull: a straight line rises from the origin to the point where the pull and the friction are 50 newtons. This is the maximum static friction, mu zero times N. There the box starts to move, and the friction force drops along a dashed line to 35 newtons, mu times N, and stays there as the pull grows." style="max-width:100%;font-size:24px">
  <line x1="193" y1="300" x2="193" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="294" y1="300" x2="294" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="300" x2="395" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496" y1="300" x2="496" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="261.5" x2="496" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="223.5" x2="496" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="185" x2="496" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="146.5" x2="496" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="108.5" x2="496" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="70" x2="496" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="510" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M522,300 L509,306 L509,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,44 L98,57 L86,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="193" y1="300" x2="193" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="294" y1="300" x2="294" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="277.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="395" y1="300" x2="395" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="378.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="496" y1="300" x2="496" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="85" y1="261.5" x2="92" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="247" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="223.5" x2="92" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="185" x2="92" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="170.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="85" y1="146.5" x2="92" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="132" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="85" y1="108.5" x2="92" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="94" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="85" y1="70" x2="92" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="55.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <foreignObject x="82" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\mu\ (\text{N})$</div></foreignObject>
  <polyline points="92,300 344.5,108.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="344.5" y1="108.5" x2="344.5" y2="166" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <polyline points="344.5,166 496,166" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="344.5" cy="108.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="107" y="170.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{static friction}$</div></foreignObject>
  <foreignObject x="370" y="124.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{sliding friction}$</div></foreignObject>
  <foreignObject x="279.5" y="71" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\mu_0 N$</div></foreignObject>
  <foreignObject x="419" y="174.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\mu N$</div></foreignObject>
</svg>

In the graph the normal force of the floor is $100\,\text{N}$. Static friction grows with the pull up to $50\,\text{N}$, where the box starts to move. A sliding box is acted on by a sliding friction of $35\,\text{N}$, even if the pull is increased. This is why a heavy cabinet is hardest to get moving, and once it is moving it goes more easily.

```pysahdy
You pull a box weakly, but it does not move. How large is the static friction?
---
As large as the force with which you pull, but in the opposite direction, because the net force is zero and the box stays at rest.
```

### The inclined plane
On an inclined plane, that is a slope, the weight still points straight down, but the surface is slanted. The normal force is perpendicular to the surface, and the friction is parallel to the surface. For calculation the weight is split into two **components**: the component along the slope tends to take the object down the slope, and the component perpendicular to the surface presses the object against the surface. The components are not new forces. They replace the weight in the calculation, and in a free-body diagram they are drawn as dashed lines.

<svg data-fig="kalteva-ydin" viewBox="0 0 600 380" role="img" aria-label="Two pictures. On the left a snapshot: a box is at rest on a wooden plank that rises to the right at an angle alpha to the horizontal. On the right the free-body diagram of the box, the box tilted as a rectangle like on the plank: the weight G from the center straight down, the normal force N from the lower surface perpendicular to the surface, outward, and the static friction from the upper corner of the lower surface parallel to the surface, up the slope. The components of the weight are drawn dashed from the center: G x down the slope and G y perpendicular to the surface, toward it. The angle between the weight and the component G y is alpha. The component G y is as long as the normal force and G x as long as the friction force." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-kalteva-ydin.webp" x="1.2" y="0" width="597" height="388.1" preserveAspectRatio="none"/>
  <foreignObject x="76" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{snapshot}$</div></foreignObject>
  <foreignObject x="81.5" y="260" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="336" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <foreignObject x="399.5" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="374" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="547" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="321.5" y="213" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <foreignObject x="497.5" y="234" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <foreignObject x="440" y="208" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
</svg>

The steeper the slope, the greater the component along the slope and the smaller the perpendicular component. When only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction, the normal force decreases together with the perpendicular component, and with it the upper limit of static friction. This is why a box starts to slide on a steep slope: the component pulling it down the slope grows greater than the maximum static friction that the surface can exert.

```pysahdy
Why does a box start to slide when the slope is steep enough?
---
As the slope gets steeper, the component of the weight along the slope grows, and the normal force and the maximum static friction become smaller. When the component exceeds the maximum static friction, the box starts to move.
```

### Friction does not always oppose motion
Friction opposes the sliding of surfaces **relative to each other**, not necessarily the motion of the object. When a pickup truck starts to move with an acceleration, a box on its bed accelerates along with it. When air drag is ignored, the only horizontal force on the box is the friction of the bed, so it must point forward, in the direction of motion: the bed tends to slide forward from under the box, and static friction prevents this. Likewise, when we walk, the foot pushes the ground backward, and the static friction of the ground pushes the foot forward. On mirror-smooth ice, where there is very little friction, getting started is therefore difficult.

<svg data-fig="kuorma" viewBox="0 0 600 360" role="img" aria-label="Two pictures. On the left a snapshot: a pickup truck starts moving to the right and accelerates, and on its bed there is a box that does not slide on the bed. Above the box a thin orange arrow a points to the right. On the right the free-body diagram of the box as a rectangle: the weight G from the center down, the normal force N of the bed from the lower surface up and as long as the weight, and the friction force of the bed from the front corner of the lower surface to the right, that is in the direction of motion. The friction force is much shorter than the weight." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-kuorma.webp" x="0" y="0" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="96" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{snapshot}$</div></foreignObject>
  <foreignObject x="159.5" y="93.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="346" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <foreignObject x="415.5" y="309" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="349.5" y="68" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="465.5" y="225.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="554.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

Besides friction, other contact forces can act on an object. **Buoyancy** is the force with which a liquid or a gas pushes upward an object immersed in it, and the **drag of the medium** is the force with which air or water opposes the motion of an object. Air drag is treated in more detail in the chapter *Air resistance and falling through air*. In this chapter air drag and buoyancy are ignored.

```pysahdy
You walk forward. Which way does the friction from the ground act on your foot?
---
Forwards, in the direction of your motion: your foot pushes the ground backwards, and the static friction from the ground pushes your foot forwards.
```

## Formula: The friction force and the inclined plane
The magnitude of the weight is
```kaavat
weight of a body at the Earth's surface :: G = mg
```
where $G$ is the weight (N), $m$ the mass (kg) and $g$ the acceleration of free fall, $9.81\,\text{m/s}^2$ on the surface of the Earth.

Sliding friction is proportional to the normal force:
```kaavat
sliding friction :: F_\mu = \mu N
```
where $F_\mu$ is the magnitude of the sliding friction (N), $\mu$ the **coefficient of sliding friction** (no unit) and $N$ the magnitude of the normal force (N). Static friction is at most the product of the normal force and the **coefficient of static friction** $\mu_0$:
```latex
F_{\mu 0} \le \mu_0 N
```
where $F_{\mu 0}$ is the magnitude of the static friction (N). The static friction is at its greatest just before the object starts to slide. This greatest value is the **maximum (fully developed) static friction**, also called the limiting static friction:
```kaavat
limiting static friction :: F_{\mu 0} = \mu_0 N
```
The coefficients of friction depend on the materials and the condition of the surfaces, and usually $\mu < \mu_0$. The formulas are empirical models that describe dry surfaces well. In them the friction does not depend on the area of contact or on the sliding speed.

On an inclined plane whose angle of inclination is $\alpha$, the $x$-axis is chosen along the slope and the $y$-axis perpendicular to the surface. The components of the weight are
```latex
\begin{aligned}
G_x &= G\sin\alpha \\
G_y &= G\cos\alpha
\end{aligned}
```
where $G_x$ is the component along the slope (N) and $G_y$ the component perpendicular to the surface (N). The angle between the weight and the component $G_y$ is the same $\alpha$ as the angle of inclination of the slope, because each is perpendicular to its counterpart: the weight to the horizontal and $G_y$ to the slope.

<svg data-fig="kalteva" viewBox="0 0 600 380" role="img" aria-label="Two pictures. On the left a snapshot: a box is at rest on a wooden plank that rises to the right at an angle alpha to the horizontal. On the right the free-body diagram of the box, the box tilted as a rectangle like on the plank: the weight G from the center straight down, the normal force N from the lower surface perpendicular to the surface, outward, and the static friction from the upper corner of the lower surface parallel to the surface, up the slope. The components of the weight are drawn dashed from the center: G x down the slope and G y perpendicular to the surface, toward it. The angle between the weight and the component G y is alpha. The component G y is as long as the normal force and G x as long as the friction force." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-kalteva.webp" x="0" y="0" width="600" height="386.2" preserveAspectRatio="none"/>
  <foreignObject x="76" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{snapshot}$</div></foreignObject>
  <foreignObject x="83.5" y="266.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="336" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <foreignObject x="399.5" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="379" y="62.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="539.5" y="130.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="329" y="192" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <foreignObject x="490" y="255" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <foreignObject x="435" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
</svg>

If only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction, the normal force equals $G_y$: $N = mg\cos\alpha$, which is less than the weight. (A pulling or pushing force directed toward or away from the surface would change the normal force.) The static friction acting on an object at rest equals $G_x$. The object stays in place as long as $mg\sin\alpha \le \mu_0\,mg\cos\alpha$, that is $\tan\alpha \le \mu_0$. The mass cancels, so according to this model a heavy and a light box start to slide on the same surface at the same angle.

<figure class="unit-photo"><img src="pics/fy4/snow-sledding.webp" alt="A child in an orange jacket sliding down a snowy slope on a yellow plastic sled."><figcaption>A child slides down a snowy slope on a plastic sled.</figcaption></figure>

### Determining the coefficient of friction
In the diagrams and in the simulation, the static friction acting on an object at rest is denoted $\overline{F}_\mu$; its magnitude is $F_{\mu 0} \le \mu_0 N$, and while sliding $F_\mu = \mu N$.

The coefficient of static friction is obtained from an experiment in which a board is tilted slowly until the object starts to slide. At this limiting angle $\alpha_0$ the static friction is at its greatest, so $\mu_0 = \tan\alpha_0$. The coefficient of sliding friction is obtained for example by pulling the object on a horizontal table with a spring balance, horizontally and at a constant velocity. Then the pull equals the sliding friction and the normal force equals the weight, so $\mu = F : mg$. When the measurement is repeated with different masses, the coefficient of friction is the slope of the straight line through the origin fitted to the $(N, F_\mu)$ graph.

## Worked example
A moving box of mass $18\,\text{kg}$ slides down a loading ramp. The ramp is at an angle of $25^\circ$ to the horizontal, and the coefficient of sliding friction between the box and the ramp is $0.30$. How large is the acceleration of the box, and how large is the friction force? Air drag is ignored.

<!-- vaihe -->

**Given and asked.** $m = 18\,\text{kg}$, $\alpha = 25^\circ$, $\mu = 0.30$ and $g = 9.81\,\text{m/s}^2$. The acceleration $a$ and the friction force $F_\mu$ are asked.

<!-- vaihe -->

**Principle.** The box is chosen as the object. The Earth (weight) and the ramp (normal force and sliding friction) act on it. The box slides down, so the sliding friction points up the slope. Newton's second law is written along the slope, where the box accelerates, and perpendicular to the surface, where it does not accelerate: $a_y = 0$.

<!-- vaihe -->

**Free-body diagram.** The box is drawn as a rectangle along the slope, and the forces start from their points of application. The axes are chosen so that $x$ points down the slope, that is in the direction of the acceleration, and $y$ perpendicular to the surface, outward. The weight is split into the components $G_x = mg\sin\alpha$ and $G_y = mg\cos\alpha$, drawn with a dashed line.

<svg data-fig="esimerkki" viewBox="0 0 600 420" role="img" aria-label="Free-body diagram of a box, the box as a rectangle tilted along a 25 degree slope. The weight G from the center straight down. The normal force N from the lower surface perpendicular to the surface, outward. The sliding friction from the upper corner of the lower surface up the slope, because the box slides down. The components of the weight dashed from the center: G x down the slope and G y perpendicular to the surface, toward it. G x is longer than the friction force. Separately a thin orange acceleration arrow a down the slope. In the corner the axes: x down the slope and y perpendicular to the surface, outward." style="max-width:100%;font-size:24px">
  <rect x="235" y="132" width="130" height="76" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-25 300 170)"/>
  <line x1="300" y1="170" x2="300" y2="321" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,338 L292,320 L308,320 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="267.5" y="341.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="332.5" y1="197" x2="275.5" y2="74.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M268,59 L283,72 L268.5,79 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="239.5" y="32.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="375" y1="177" x2="401" y2="165" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M416.5,157.5 L403.5,172.5 L396.5,158 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="412" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="300" y1="170" x2="237.5" y2="199" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M245,188.5 L235.5,200 L250.5,200.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="193" y="195.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="300" y1="170" x2="363.5" y2="306" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M353,299 L364.5,308 L364.5,293.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="370" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <line x1="120" y1="120" x2="58.5" y2="148.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M65.5,138 L56.5,149.5 L71,150" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="20" y="140.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M300,230 A60,60 0 0 0 325.5,224.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="295.5" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25^\circ$</div></foreignObject>
  <line x1="520" y1="330" x2="486.5" y2="345.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M478.5,349.5 L485.5,341 L489.5,349.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="520" y1="330" x2="504.5" y2="296.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M500.5,288.5 L509,295.5 L500.5,299.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="455.5" y="341" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="484.5" y="261" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**The formula solved.** The equations of motion are read from the diagram and the asked quantities are solved:
```latex
\begin{aligned}
&x\text{:}\ \ mg\sin\alpha - \mu N = ma \\
&y\text{:}\ \ N - mg\cos\alpha = 0 \\
&F_\mu = \mu mg\cos\alpha \\
&a = g(\sin\alpha - \mu\cos\alpha)
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: all quantities are in SI units, and the coefficient of friction has no unit.

<!-- vaihe -->

**Substitution.** The numerical values are substituted with their units:
```latex
\begin{aligned}
&F_\mu = \mu mg\cos\alpha \\
&\phantom{F_\mu} = 0.30\cdot 18\,\text{kg} \\
&\quad\ \cdot 9.81\,\text{m/s}^2\cdot\cos 25^\circ \\
&\phantom{F_\mu} \approx 48.0\,\text{N} \\[4pt]
&a = g(\sin\alpha - \mu\cos\alpha) \\
&\phantom{a} = 9.81\,\text{m/s}^2 \\
&\quad\ \cdot(\sin 25^\circ - 0.30\cdot\cos 25^\circ) \\
&\phantom{a} \approx 1.48\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration of the box is $a \approx 1.5\,\text{m/s}^2$ down the slope and the friction force is $F_\mu \approx 48\,\text{N}$, to two significant figures like the data $\mu = 0.30$ and $m = 18\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** Without friction the acceleration would be $g\sin 25^\circ \approx 4.1\,\text{m/s}^2$, so friction reduces it, as it should. The friction force $48\,\text{N}$ is less than the component along the slope $G_x \approx 75\,\text{N}$, so the net force points down the slope and the box accelerates down. The mass does not affect the acceleration, because both $G_x$ and $F_\mu$ are proportional to the mass.

## Common misconception
Many people think that the friction force is always $\mu_0 N$ or $\mu N$ and always against the motion. Static friction, however, is only as large as the situation requires: if a box is pushed with a force of $20\,\text{N}$ and it does not move, the static friction is $20\,\text{N}$, even if its upper limit is greater. Friction opposes the sliding of surfaces relative to each other, so it can also point in the direction of motion, as on the bed of an accelerating truck. Another common mistake is to take the normal force to be always equal to the weight. On a slope $N = mg\cos\alpha$ is less than the weight, when only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction, and the weight still points straight down and not perpendicular to the slope.

## Summary
- The magnitude of the weight is $G = mg$, and the weight always points straight down. Mass is the same everywhere, but weight depends on the acceleration of free fall.
- Friction is parallel to the surface and opposes the sliding of surfaces relative to each other, not always the motion of the object.
- Static friction adapts to the situation: $F_{\mu 0} \le \mu_0 N$. A sliding object is acted on by sliding friction $F_\mu = \mu N$, and usually $\mu < \mu_0$.
- On a slope the weight is split into the components $G_x = mg\sin\alpha$ and $G_y = mg\cos\alpha$, and the normal force is $N = mg\cos\alpha$, when only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction. The components are drawn as dashed lines, and they are not new forces.
- The coefficient of static friction is obtained from the limiting angle at which the object starts to slide: $\mu_0 = \tan\alpha_0$.
