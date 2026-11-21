# Applied lesson: lift, parachute and sledding hill

> **Why** can two sleds stop equally far from the top of a hill, although one goes down a steep slope and the other a gentle one?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter sledding hill. Two children stand at the top of the hill, and one child&#x27;s sled waits to start. The left slope of the hill is steep and short, the right slope gentle and long, and a flat snow field continues from the foot of each slope. On both sides the tracks of the sled run down the slope and along the flat to a sled that has stopped with a child at a red marker flag. On the left the sled that came down the steep side has slid far along the flat, on the right the sled from the gentle side only a little, and both flags are equally far from the top of the hill measured horizontally. In the background are a forest, a red cottage and snowy mounds. The height of the hill and the distances are to scale, the children and sleds larger." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-16-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### First the free-body diagram, then the tool
The problems of this chapter are solved with two tools, and both start from the same place. The module has a third one too: for collisions and short impacts, the impulse principle and the conservation of momentum are used (chapter *Conservation of momentum and one-dimensional collisions*). First you choose the body and draw its free-body diagram, as in the chapter *Free-body diagrams and the combined effect of forces*. The diagram shows which forces act and in which directions. Then you choose the tool according to what is asked. When the question is about a force or an acceleration at some moment, you write the equation of motion (chapter *Newton's second law*). When the question is about the speed at some point or the change in energy over some distance, you use the work–energy principle (chapter *Conservation of mechanical energy and the work–energy principle*). Even then you need the free-body diagram, because it shows which forces do work.

<svg data-fig="kolme" viewBox="0 0 600 460" role="img" aria-label="Three situations. At the top are situation pictures and below the dashed line free-body diagrams in which the chosen body is a rectangle and the forces are to scale inside each diagram. On the left a lift starts up: a person stands on the floor of the lift car, and a blue velocity arrow points up. In the person&#x27;s free-body diagram the weight G from the centre down and the normal force N of the floor from the bottom surface up, longer than the weight, and an orange acceleration arrow up. In the middle a skydiver descends under a parachute at a steady speed: a velocity arrow down. In the free-body diagram the weight G down and the air resistance F_d from the top surface up, equally long, acceleration zero. On the right a sled slides down a slope to the left: a velocity arrow down the slope. In the free-body diagram the sled is a rectangle tilted along the slope: the weight G from the centre straight down, the normal force N from the bottom surface perpendicularly out of the slope and the sliding friction F_mu from the upper corner of the bottom surface up the slope, short. The acceleration arrow down the slope." style="max-width:100%;font-size:26px">
  <image href="pics/fy4/fy4-16-kolme.webp" x="0" y="0" width="600" height="466.2" preserveAspectRatio="none"/>
  <foreignObject x="69" y="6.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{lift}$</div></foreignObject>
  <foreignObject x="235" y="6.5" width="130" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{parachute}$</div></foreignObject>
  <foreignObject x="415" y="6.5" width="170" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{sledding hill}$</div></foreignObject>
  <foreignObject x="170.5" y="109.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="94.5" y="343" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="36.5" y="242.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="160.5" y="246.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="360.5" y="114.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="217.5" y="226" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{F}_\text{d}$</div></foreignObject>
  <foreignObject x="290.5" y="363" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="341.5" y="284.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="429.5" y="79.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="464.5" y="404.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="458.5" y="221.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="535" y="317.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="387" y="232" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

### Lift: a scale measures the normal force
A bathroom scale does not measure the weight but the normal force $N$ with which it pushes the person standing on it upwards. The reading is shown in kilograms, because the scale divides the force by $9.81\,\text{m/s}^2$. Only the weight and the normal force act on a person standing still in a lift. When the positive direction is up, the equation of motion is $N - mg = ma$, so $N = m(g + a)$. When the lift starts up and accelerates at $1.0\,\text{m/s}^2$, the normal force on a $60.0\,\text{kg}$ person is $649\,\text{N}$, rounded $650\,\text{N}$ as in the graph, and the scale shows $66\,\text{kg}$. At a steady speed $a = 0$, and the scale shows the same as at home, whether the lift moves up or down. So the reading depends on the acceleration, not on the speed.

```pysahdy
A lift moves upwards at a steady speed of $2.0\,\text{m/s}$. Does the scale then show more, less or the same as when standing still? Explain.
---
The same. The speed is constant, so $a = 0$ and $N = mg$. The reading depends on the acceleration, not on the speed.
```

### Parachute: at terminal velocity the mechanical energy decreases
A skydiver descending under a parachute soon falls at terminal velocity, that is, at a steady speed (chapter *Air resistance and falling through air*). By the equation of motion the acceleration is zero, so the air resistance is equal to the weight, $F_\text{d} = mg$. In terms of energy, the kinetic energy does not change, but the potential energy decreases all the time. By the work–energy principle the change in mechanical energy is the work done by air resistance. It is negative, because air resistance points against the motion: over a height $h$, $W_\text{d} = -F_\text{d} h = -mgh$. When an $80\,\text{kg}$ skydiver descends $100\,\text{m}$, about $78\,\text{kJ}$ of mechanical energy is changed into motion of the air and finally into internal energy. Each tool tells the same thing in its own way.

```pysahdy
At terminal velocity the skydiver's kinetic energy does not change. Where does the mechanical energy go then?
---
The potential energy decreases with height. Air resistance does negative work, and the energy is changed into motion of the air and finally into internal energy.
```

### Sledding hill: friction takes energy all the way
A sled slides down a straight slope. The free-body diagram shows that the component of the weight perpendicular to the slope and the normal force cancel each other, so $N = mg\cos\alpha$, as in the chapter *Weight, friction and the inclined plane*. The sliding friction is then $F_\mu = \mu mg\cos\alpha$. The normal force does no work, because it is perpendicular to the motion. On the slope the weight does work $mgh$, and friction does negative work $-F_\mu L$, when the length of the slope is $L$. On a hill of the same height, the normal force and the friction are smaller on a steep slope and the slope is shorter, so friction takes less energy and the sled is faster at the foot. On the flat the sled slides until friction has turned all the kinetic energy into internal energy.

```pysahdy
Two sleds start from the same height, one down a steep slope and the other down a gentle one. On which slope does friction do more work, and why?
---
On the gentle one. The slope is longer, so friction acts over a longer distance and takes more energy than on the steep slope.
```

## Formula: Equation of motion and work–energy principle
The first tool of an applied problem is Newton's second law:
```kaavat
Newton's second law (fundamental law of dynamics) :: \Sigma\overline{F} = m\overline{a}
```
where $\Sigma\overline{F}$ is the sum of the forces acting on the body, that is, the net force ($\text{N}$), $m$ is the mass of the body ($\text{kg}$) and $\overline{a}$ its acceleration ($\text{m/s}^2$). The law is written from the free-body diagram in components, $\Sigma F_x = ma_x$ and $\Sigma F_y = ma_y$, once the axes and the positive directions have been chosen. The second tool is the work–energy principle of mechanics:
```kaavat
work-energy principle of mechanics :: E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}
```
where the index $0$ means the initial situation and a quantity without an index the final situation, $E_\text{k} = \tfrac12 mv^2$ is the kinetic energy, $E_\text{p} = mgh$ the potential energy from the chosen zero level and $W$ the work done by forces other than the weight ($\text{J}$). The work–energy principle needs neither the acceleration nor the time, so it fits when the question is about the speed at a given point.

### The work done by friction depends on the horizontal distance
On a straight slope with an angle of inclination $\alpha$ and a length $L$, the sliding friction is $\mu mg\cos\alpha$ and the work it does is $-\mu mg\cos\alpha \cdot L$. The figure shows that $L\cos\alpha$ is the horizontal length $x_1$ of the slope. On the flat $N = mg$, and the work done by friction over a distance $x_2$ is $-\mu mg x_2$. In both cases the work done by sliding friction is
```latex
W_\mu = -\mu m g x
```
where $\mu$ is the coefficient of sliding friction, $m$ the mass ($\text{kg}$), $g$ the acceleration of free fall ($\text{m/s}^2$) and $x$ the horizontal length of the distance travelled ($\text{m}$). The result requires that the surface is straight, that the coefficient of friction is the same all the way and that only the weight and the normal force act perpendicular to the surface, so the sled is not, for example, pulled with a rope.

<svg data-fig="kitkatyo" viewBox="0 0 600 330" role="img" aria-label="Schematic, not to scale: a sled starts from rest at the top of a hill, slides down a straight slope and continues along the flat until it stops. The length of the slope is L and its height h, and the slope is at an angle alpha to the horizontal. The horizontal length of the slope is x 1, that is, L times the cosine of alpha, and on the flat the sled slides a distance x 2. In both places the sled is drawn at rest, speed zero." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-16-kitkatyo.webp" x="0" y="-2.5" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="25" y="29.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$v_1 = 0$</div></foreignObject>
  <foreignObject x="491" y="163.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$v_2 = 0$</div></foreignObject>
  <foreignObject x="217" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
  <foreignObject x="92" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="252.5" y="178.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="163.5" y="273.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1 = L\cos\alpha$</div></foreignObject>
  <foreignObject x="406.5" y="273.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
</svg>

### Why the sleds stop equally far away
A sled starts from rest at a height $h$, goes down the slope and stops on the flat. When the zero level is chosen at the flat, the work–energy principle gives $mgh - \mu mg(x_1 + x_2) = 0$. The mass cancels, and the whole horizontal distance of the sled from the top to the stopping point is
```latex
x_1 + x_2 = \frac{h}{\mu}
```
The angle of inclination does not appear in the result. A sled coming down the steep side travels a short horizontal distance on the slope, so it has more distance left on the flat. A sled coming down the gentle side uses a larger part of the horizontal distance on the slope. This answers the question at the start. The model assumes that the coefficient of friction is the same all the way, that air resistance is small and that the bend at the foot of the slope is short. In a sharp bend the normal force and the friction grow for a moment, so a real sled stops a little earlier below a steep hill. In addition, the slope must be steep enough for the sled to slide: $\tan\alpha > \mu$.

### Steps of the solution
1. Choose the body and draw its free-body diagram: for every force its cause and direction.
2. Decide the tool: the force or acceleration at a moment from the equation of motion, the speed at a given point from the work–energy principle.
3. For the equation of motion choose the axes and the positive directions. For the work–energy principle choose the zero level and write the work of the other forces with their signs: a force opposing the motion does negative work, and a force perpendicular to the motion does no work.
4. Solve the asked quantity in symbols, substitute only then, and check the result with a limiting case, for example without friction.

## Worked example
A child and a sled, together $32.0\,\text{kg}$, start from rest at the top of a straight slope. The length of the slope is $25.0\,\text{m}$, the angle of inclination $20.0^\circ$ and the coefficient of sliding friction between the sled and the snow $0.200$. How large is the speed of the sled at the foot of the slope? Air resistance is ignored.

<!-- vaihe -->

**Given and asked.** $m = 32.0\,\text{kg}$, $L = 25.0\,\text{m}$, $\alpha = 20.0^\circ$, $\mu = 0.200$, initial speed $v_1 = 0$ and $g = 9.81\,\text{m/s}^2$. We want the speed $v_2$ at the foot of the slope.

<!-- vaihe -->

**Principle.** The question is about the speed at a given point, so we use the work–energy principle. We choose the sled and the child together as the body. The weight does work, which the work–energy principle takes into account as a change in potential energy. The normal force does no work, because it is perpendicular to the motion. Sliding friction points against the motion and does negative work $W = -F_\mu L$. The friction force comes from the free-body diagram.

<!-- vaihe -->

**Free-body diagram.** The sled is drawn as a rectangle along the slope. The forces on it are from the Earth (the weight $\overline{G}$), from the snow (the normal force $\overline{N}$) and the sliding friction $\overline{F}_\mu$ of the snow, which points up the slope, because the sled slides down. The axes are chosen so that $x$ points down the slope and $y$ perpendicularly out of the slope. In the $y$ direction the sled does not accelerate, so $N - mg\cos\alpha = 0$ and $F_\mu = \mu N = \mu mg\cos\alpha$.

<svg data-fig="esimerkki" viewBox="0 0 600 400" role="img" aria-label="On the left a situation picture: a sled and a child slide down a snowy slope to the left, and a blue velocity arrow above the sled points down the slope. The slope rises to the right at an angle of 20 degrees. On the right the free-body diagram of the sled, the sled as a rectangle tilted along the slope, forces to scale. The weight G from the centre straight down. The normal force N from the bottom surface perpendicularly out of the slope, a little shorter than the weight. The sliding friction F_mu from the upper corner of the bottom surface up the slope, short. The components of the weight as dashed lines from the centre: G x down the slope, longer than the friction, and G y perpendicularly towards the slope. Separately an orange acceleration arrow down the slope. In the corner the axes: x down the slope and y perpendicularly out of the slope." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy416-ex-snow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy416-ex-s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <foreignObject x="50" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <foreignObject x="296" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <path d="M18,300 L215.5,228 V300 Z" fill="url(#fy416-ex-snow)" stroke="#4f8fbf" stroke-width="2.5" stroke-linejoin="round"/>
  <g transform="translate(138.5,256) rotate(-20) scale(-0.8,0.8)">
  <path d="M-46,-4 Q-48,0 -40,0 H34 Q52,0 56,-22 L48,-24 Q44,-10 30,-10 H-38 Z" fill="url(#fy416-ex-s)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M-40,-6 H28" fill="none" stroke="#f2a69c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M6,-14 Q26,-16 40,-20" fill="none" stroke="#1f2933" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M-22,-12 Q-26,-46 -6,-50 Q8,-50 10,-14 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M2,-40 L22,-24" fill="none" stroke="#1971c2" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="-8" cy="-62" r="11" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M-20,-62 Q-20,-78 -8,-78 Q4,-78 4,-62 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="-8" cy="-80" r="4" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  </g>
  <line x1="107.5" y1="170.5" x2="53" y2="190" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M61,180.5 L51,191 L65.5,192.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="58.5" y="148" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <path d="M88,300 A70,70 0 0 0 84,276" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="90" y="269" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20^\circ$</div></foreignObject>
  <line x1="234" y1="36" x2="234" y2="388" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="358" y="154" width="104" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-20 410 176)"/>
  <line x1="410" y1="176" x2="410" y2="291" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M410,308 L402,290 L418,290 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="375.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="436.5" y1="190" x2="400" y2="89.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M394,73.5 L407.5,87.5 L392.5,93 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="363.5" y="47" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="466.5" y1="179" x2="473.5" y2="176" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M489.5,170.5 L475.5,184 L470,169 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="477" y="176" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="410" y1="176" x2="369.5" y2="190.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M377.5,181 L367.5,191.5 L382,193" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="323" y="189" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="410" y1="176" x2="451.5" y2="290.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M442,282.5 L452.5,292.5 L454,278" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="458" y="280" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <line x1="300" y1="120" x2="249.5" y2="138.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M257.5,128.5 L247.5,139 L262,141" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="227" y="106.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="540" y1="330" x2="507" y2="342" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M498.5,345 L506.5,337.5 L509.5,346 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="540" y1="330" x2="528" y2="297" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M525,288.5 L532.5,296.5 L524,299.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="475.5" y="335.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="510" y="261" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Formula solved.** The zero level is chosen at the foot of the slope, so at the start $E_\text{p,1} = mgh$, where $h = L\sin\alpha$, and at the end $E_\text{p,2} = 0$. The speed is solved from the work–energy principle:
```latex
\begin{aligned}
&mgL\sin\alpha - \mu mg\cos\alpha \cdot L \\
&\quad = \tfrac12 mv_2^2 \\
&v_2 = \sqrt{2gL(\sin\alpha - \mu\cos\alpha)}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the quantities are in SI units, the coefficient of friction has no unit and the angle is in degrees with the calculator in degree mode.

<!-- vaihe -->

**Substitution.** First we calculate the expression in brackets and then the speed:
```latex
\begin{aligned}
&\sin 20.0^\circ - 0.200\cdot\cos 20.0^\circ \\
&\quad \approx 0.3420 - 0.1879 = 0.1541 \\
&v_2 = \sqrt{2\cdot 9.81\cdot 25.0\cdot 0.1541}\,\tfrac{\text{m}}{\text{s}} \\
&\phantom{v_2} \approx 8.694\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Result.** The speed of the sled at the foot of the slope is $8.69\,\text{m/s}$, or about $31\,\text{km/h}$, to three significant figures like the length of the slope $25.0\,\text{m}$, the angle $20.0^\circ$ and the coefficient of friction $0.200$.

<!-- vaihe -->

**Reasonableness.** Without friction the speed would be $\sqrt{2gh} = \sqrt{2\cdot 9.81\cdot 8.55}\,\tfrac{\text{m}}{\text{s}} \approx 13.0\,\text{m/s}$, so friction reduces it, as it should. The same result comes from the equation of motion: in the $x$ direction $mg\sin\alpha - \mu mg\cos\alpha = ma$, so $a \approx 1.51\,\text{m/s}^2$, and from the result $aL = \tfrac12 v_2^2$ of the chapter *Conservation of mechanical energy and the work–energy principle* we get $v_2^2 \approx 75.6\,\text{m}^2/\text{s}^2$ as above. The mass cancelled, so a heavier and a lighter sled are equally fast at the foot, when the coefficient of friction is the same.

## Common misconception
Many think that a scale in a lift shows more because the lift moves upwards. The reading depends on the acceleration, not on the speed: in a lift moving steadily up or down the scale shows the same as at home, and in a lift moving up that slows down to stop it shows less.

Another mistake is to think that at terminal velocity the mechanical energy is conserved, because the speed does not change. The kinetic energy stays the same, but the potential energy decreases, and the negative work done by air resistance changes it into other forms of energy. A third mistake is to write the friction force on a slope as $\mu mg$. On a slope the normal force is $mg\cos\alpha$, so the friction force is $\mu mg\cos\alpha$, and the work done by friction is $-\mu mg$ times the horizontal distance, not times the length of the slope.

## Summary
- A mechanics problem always starts with choosing the body and drawing its free-body diagram. The force or acceleration at a moment comes from the equation of motion $\Sigma\overline{F} = m\overline{a}$, the speed at a given point from the work–energy principle.
- In a lift a scale measures the normal force $N = m(g + a)$, when the positive direction is up. The reading depends on the acceleration, not on the speed.
- At terminal velocity $F_\text{d} = mg$, and the work done by air resistance is $-mgh$: the mechanical energy decreases although the speed does not change.
- On a straight slope $N = mg\cos\alpha$, and the work done by sliding friction is $W_\mu = -\mu mgx$, where $x$ is the horizontal distance. A sled that starts from rest at a height $h$ stops at a horizontal distance $h/\mu$ from the top, when the coefficient of friction is the same all the way.
- When a body slides along a stationary surface, the normal force does no work, because it is perpendicular to the motion. In a moving lift the normal force of the floor is parallel to the motion, so it does work: positive when the lift moves up, negative when it moves down.
