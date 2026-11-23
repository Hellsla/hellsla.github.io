# Newton's laws and the free-body diagram

> **Why** can a car set a trailer moving, even though the trailer pulls the car backwards with a force as large as the force with which the car pulls the trailer forwards?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an autumn afternoon by a lake. On the road in the foreground a red car pulls a small trailer loaded with firewood. The car and the trailer are joined by a drawbar. Behind the road there is a lake with forest on the far shore, and birches and spruces grow along the road." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-voimat-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

Every task in this lesson is solved in the same way: **first the free-body diagram, then the equation of motion**. Choose the object, list its interactions and draw one force for each. In the free-body diagram the object is a rectangle, and each force starts from its point of application. Then choose the axes and write Newton's second law along each axis. In the exam, points for the free-body diagram are lost for a missing force, an extra force or a force drawn in the wrong direction.

<svg data-fig="kartta" viewBox="0 0 380 888" role="img" aria-label="Recognition chart: how do I tell which law to use? Start from the free-body diagram and see which sign in the task fits. Constant velocity or at rest: the acceleration is zero, so the sum of the forces is zero. Starts from rest or speeds up: the acceleration is not zero, so the sum of the forces is mass times acceleration. A rod or lever stays at rest: the sum of the moments is zero too. Two bodies joined by a rope: an equation of motion for each body. Frictionless surface: no friction force. Slides on a rough surface: sliding friction is the coefficient of friction times the normal force. Stays put although pulled: static friction, at most as large as the limiting friction. Is just about to slide: fully developed static friction, or limiting friction, is the coefficient of static friction times the normal force. Falling, air resistance and the speed levels off: the forces balance and the air resistance equals the weight." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="844" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{free-body diagram first, then the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{constant velocity or at rest}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ a = 0$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{starts from rest or speeds up}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ a \neq 0$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\overline{F} = m\overline{a}$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a rod or lever stays at rest}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{moments too}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma M = 0$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{two bodies on a rope}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{an equation each}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma F_i = m_i a_i$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{frictionless surface}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{no friction force}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\mu = 0$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{slides on a rough surface}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{sliding friction}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\mu = \mu N$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{stays put although pulled}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{static friction}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F \le F_{\mu_0}$</div></foreignObject>
  <line x1="14" y1="747" x2="30" y2="747" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="94" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{is just about to slide}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="300" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{fully developed static friction}$</div></foreignObject>
  <foreignObject x="44" y="767" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\text{or limiting friction}$</div></foreignObject>
  <rect x="238" y="766" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="768" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_{\mu_0} = \mu_0 N$</div></foreignObject>
  <line x1="14" y1="844" x2="30" y2="844" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="808" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="818.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{falling, air resistance, speed levels off}$</div></foreignObject>
  <line x1="40" y1="848" x2="362" y2="848" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="853" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{forces balance}$</div></foreignObject>
  <rect x="238" y="852" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="854" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{v} = G$</div></foreignObject>
</svg>

The opening question is settled by the choice of object. The car and the trailer act on each other with equal forces, but the forces act on **different objects**, so they do not cancel each other. The motion of the trailer is decided only by the forces acting on the trailer: while accelerating, the drawbar pulls it forwards more than the rolling resistance holds it back.

```pysahdy
The car pulls the trailer forward and the trailer pulls the car backward with equal forces. Why do these forces not cancel each other?
---
They act on different objects. Only the forces acting on the trailer decide the motion of the trailer.
```

## Formula: Newton's laws and forces

### Newton's laws

```kaavat
\Sigma\overline{F} = \overline{0} \ \Leftrightarrow\ \overline{v} = \text{constant}
Newton's second law (fundamental law of dynamics) :: \Sigma\overline{F} = m\overline{a}
\overline{F}_{AB} = -\overline{F}_{BA}
```

where $\Sigma\overline{F}$ is the sum of the forces acting on the object ($\text{N}$), $m$ the mass ($\text{kg}$), $\overline{a}$ the acceleration ($\text{m/s}^2$) and $\overline{F}_{AB}$ the force with which A acts on B. In a calculation the second law is written in components, $\Sigma F_x = ma_x$ and $\Sigma F_y = ma_y$, and the components of an oblique force are $F\cos\alpha$ and $F\sin\alpha$. The net force points in the direction of the acceleration, not always in the direction of the velocity.

```pysahdy
An object brakes on a straight road. In which direction does the sum of the forces acting on it point?
---
In the direction of the acceleration, which here is against the motion. The net force does not always point in the direction of the velocity.
```

### Weight, friction and the slope

```kaavat
weight of a body at the Earth's surface :: \overline{G} = m\overline{g}
sliding friction :: F_\mu = \mu N
limiting static friction :: F_{\mu_0} = \mu_0 N
```

where $\overline{g}$ is the acceleration due to gravity, $g = 9.81\,\text{m/s}^2$, so the magnitude of the weight is $G = mg$, $N$ is the normal force ($\text{N}$), $\mu$ the coefficient of sliding friction and $\mu_0$ the coefficient of static friction. Static friction is only as large as the situation requires, at most the limiting friction $F_{\mu_0}$, and it opposes the sliding of the surfaces relative to each other, not always the motion. The formulas are experimental models for dry surfaces. In free-body diagrams $\overline{F}_\mu$ stands for either kind of friction, static or sliding.

On a slope with the angle of inclination $\alpha$, the components of the weight are $G_x = mg\sin\alpha$ down the slope and $G_y = mg\cos\alpha$ towards the slope. When only the weight and the normal force act perpendicular to the surface, $N = mg\cos\alpha$. The components are not new forces: they are drawn with dashed lines and replace the weight in the calculation.

<svg data-fig="kalteva" viewBox="0 0 600 380" role="img" aria-label="Two pictures. On the left the situation: a plastic sledge slides down a snowy slope to the left. The slope rises to the right at the angle alpha to the horizontal. Above the sledge a blue velocity arrow and an orange acceleration arrow point down the slope. On the right the free-body diagram of the sledge, the sledge as a rectangle tilted parallel to the slope: the weight G straight down from the centre, the normal force N from the bottom surface perpendicular to the slope and outwards, and sliding friction F mu from the upper corner of the bottom surface up the slope. The components of the weight are drawn with dashed lines from the centre: G x down the slope and G y perpendicular to the slope, towards it. The component G y is as long as the normal force, and G x is clearly longer than the friction, so the sum of the forces points down the slope. The lengths of the arrows are to scale." style="max-width:100%;font-size:28px">
  <image href="pics/fy9/fy9-voimat-kalteva.webp" x="0" y="0" width="600" height="387.5" preserveAspectRatio="none"/>
  <foreignObject x="38.5" y="5" width="183" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{the situation}$</div></foreignObject>
  <foreignObject x="153.5" y="174.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="135" y="134.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="92.5" y="285" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$\alpha$</div></foreignObject>
  <foreignObject x="329.5" y="5" width="241" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <foreignObject x="409.5" y="326" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="388.5" y="45.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="509.5" y="142" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="338.5" y="189" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <foreignObject x="501.5" y="284" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <foreignObject x="450.5" y="223" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$\alpha$</div></foreignObject>
</svg>

```pysahdy
An object slides on a slope with the angle of inclination $\alpha$, and only the weight and the normal force act perpendicular to the surface. What is the magnitude of the normal force?
---
$N = mg\cos\alpha$, because the normal force cancels the component $G_y$ of the weight perpendicular to the surface. It is smaller than $mg$.
```

### Connected bodies and air resistance

For connected bodies, each body gets its own free-body diagram and its own equation of motion. A light, inextensible string and a light, frictionless pulley give the bodies accelerations of the same magnitude and tension forces of the same magnitude. Air resistance $\overline{F}_\text{v}$ points against the velocity and grows as the speed grows. At terminal velocity the acceleration is zero, so $F_\text{v} = G$.

## Common mistakes {Virheet}

- **A force in the direction of motion.** Nothing pushes a sliding object forwards. Every force has a cause, another object.
- **Force and counterforce in the same diagram.** They act on different objects and do not cancel each other.
- **$N = mg$ always.** On a slope, with an oblique pull and in an accelerating lift, the normal force is different from the weight.
- **$F_\mu = \mu_0 N$ at rest.** At rest friction is only as large as the situation requires; $\mu_0 N$ is its upper limit.
- **Connected bodies: $T = m_2 g$.** When the hanging body accelerates downwards, the tension in the string is smaller than its weight.
- **Components in addition to the forces.** If both the weight and its components are in the calculation, the weight is counted twice.

## Review if needed {Kertaa}

- The first and third laws: [*Interaction and force: Newton's first and third laws*](fy4-3.html). The second law: [*Newton's second law*](fy4-4.html).
- The eight steps of a free-body diagram and components: [*Free-body diagrams and the combined effect of forces*](fy4-5.html).
- Weight, static and sliding friction and the slope: [*Weight, friction and the inclined plane*](fy4-6.html).
- String and pulley: [*Equation of motion for connected bodies*](fy4-13.html). Terminal velocity: [*Air resistance and falling through air*](fy4-14.html).
