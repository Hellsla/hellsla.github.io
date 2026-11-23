# Newton's second law

> **Why** does a fully loaded truck accelerate away from the traffic lights more slowly than an empty one, even though the engine is the same?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the traffic lights on a country road have just turned green, and two identical trucks have set off from side-by-side lanes. The nearer truck is fully loaded with logs and has only just crossed the stop line. The empty truck farther away is already clearly ahead. Forest and fields are in the background." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### The net force changes the velocity
In the chapter *Interaction and force: Newton's first and third laws* you learned that an object's velocity stays unchanged when the forces acting on it cancel each other. The object is then at rest or moves in a straight line at constant velocity. When the forces do not cancel, the velocity changes: the object speeds up, slows down or turns. What matters is not any single force but the combined effect of all the forces acting on the object, the **net force** $\Sigma\overline{F}$. It is the vector sum of the forces, not just one force added to another.

On the left of the figure a box rests on the floor. The weight $\overline{G}$ and the normal force $\overline{N}$ from the floor are equal and opposite, so the net force is zero. On the right the box is pulled by a rope. The vertical forces still cancel, but horizontally the tension $\overline{T}$ in the rope is greater than the friction force $\overline{F}_\mu$ from the floor. The net force points to the right, and the box accelerates to the right.

<svg data-fig="kokonaisvoima" viewBox="0 0 600 420" role="img" aria-label="Two situations. On the left a box rests on the floor. In its free-body diagram the box is a rectangle: the weight G points down from the centre and the normal force N from the floor points up from the bottom surface, equally long. On the right the same box is pulled horizontally to the right by a rope, and in the situation picture an orange acceleration arrow points to the right above the box. Its free-body diagram has the weight and the normal force equally long, the tension T of the rope to the right, and the friction force from the floor to the left from the back corner of the bottom surface, one third of the length of the tension. Separately there is a green hollow arrow, the net force, to the right: the difference between the tension and the friction. The arrows are to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-4-kokonaisvoima.webp" x="0" y="0" width="600" height="425" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="5.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{at rest}$</div></foreignObject>
  <foreignObject x="153.5" y="326" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="170.5" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="377.5" y="5.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{being pulled}$</div></foreignObject>
  <foreignObject x="423.5" y="326" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="440.5" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="530.5" y="253.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="333.5" y="301.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="437.5" y="33.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="513.5" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
</svg>

```pysahdy
A box is pulled to the right by a rope, and it speeds up. What can you conclude about the horizontal forces?
---
The force of the rope is greater than the friction, so the horizontal net force is not zero but points to the right.
```

### Mass resists a change in velocity
Measurements with a cart reveal two regularities. When the net force doubles, the acceleration doubles: the acceleration is directly proportional to the net force. When the same net force acts on a cart with twice the mass, the acceleration is halved. Mass therefore tells us about the inertia of an object, that is, how hard it is to change its velocity. In the graph each mass gives a straight line through the origin, and the line of the heavier cart is half as steep.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: the horizontal axis shows the net force in newtons from 0 to 3, and the vertical axis shows the acceleration from 0 to 6 metres per second squared. Two straight lines through the origin, each with three points. For a mass of 0.50 kilograms the points are 1 N and 2, 2 N and 4, and 3 N and 6. For a mass of 1.0 kilogram the points are 1 N and 1, 2 N and 2, and 3 N and 3. Dashed lines show that at a net force of 2 N the acceleration of the lighter cart is 4 and that of the heavier cart is 2." style="max-width:100%;font-size:24px">
  <line x1="138.5" y1="300" x2="138.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186.5" y1="300" x2="186.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="235" y1="300" x2="235" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283.5" y1="300" x2="283.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="300" x2="331.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="380" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="261.5" x2="380" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="223.5" x2="380" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="185" x2="380" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="146.5" x2="380" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="108.5" x2="380" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="70" x2="380" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="300" x2="394" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M406,300 L393,306 L393,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,44 L96,57 L84,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="138.5" y1="300" x2="138.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186.5" y1="300" x2="186.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="235" y1="300" x2="235" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283.5" y1="300" x2="283.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="273.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="331.5" y1="300" x2="331.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="380" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="370" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="83" y1="261.5" x2="90" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="247" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="83" y1="223.5" x2="90" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="209" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="185" x2="90" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="83" y1="146.5" x2="90" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="132" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="108.5" x2="90" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="94" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="83" y1="70" x2="90" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="412" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Sigma F\ (\text{N})$</div></foreignObject>
  <foreignObject x="80" y="13.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a\ (\text{m/s}^2)$</div></foreignObject>
  <line x1="283.5" y1="146.5" x2="283.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="146.5" x2="283.5" y2="146.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="283.5" y1="223.5" x2="283.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="223.5" x2="283.5" y2="223.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="90,300 380,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,300 380,185" fill="none" stroke="#b8622d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="186.5" cy="223.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186.5" cy="261.5" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283.5" cy="146.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283.5" cy="223.5" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <circle cx="380" cy="70" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="380" cy="185" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="394" y="55.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 0.50\,\text{kg}$</div></foreignObject>
  <foreignObject x="394" y="170.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d">$m = 1.0\,\text{kg}$</div></foreignObject>
</svg>

This gives the answer to the opening question. The engine turns the driving wheels, and the road pushes the tyres forward. When this force is equally large for the loaded and the empty truck, the much greater mass of the loaded truck makes its acceleration small. The weight of the load does not pull the truck backward as such, because the normal force from the road cancels it. The heavy load does increase the rolling resistance of the tyres, but the main reason for the slow acceleration is the large mass.

```pysahdy
The same net force acts on an empty and on a full shopping cart. Which one accelerates more, and why?
---
The empty cart, because its mass is smaller. Mass resists a change in velocity: double the mass halves the acceleration.
```

## Formula: Newton's second law
Newton's second law, also called the fundamental law of dynamics, gathers the observations into one equation:
```kaavat
Newton's second law (fundamental law of dynamics) :: \Sigma\overline{F} = m\overline{a}
```
where $\Sigma\overline{F}$ is the vector sum of the forces acting on the object, the net force ($\text{N}$), $m$ is the mass of the object ($\text{kg}$) and $\overline{a}$ is its acceleration ($\text{m/s}^2$). The unit of force is defined by this law: one newton is the force that gives a mass of one kilogram an acceleration of $1\,\text{m/s}^2$. So $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.

### The net force points in the direction of the acceleration
The law is a vector equation: the net force and the acceleration always point in the same direction. The direction of the velocity can be another one. In the figure a crane holds a crate on a rope. When the crate rises while speeding up, the force of the rope is greater than the weight and the net force points up. When the crate rises while slowing down, the force of the rope is smaller than the weight: the net force and the acceleration point down, even though the crate still moves upward. At rest and when rising at constant velocity, the force of the rope and the weight are equal.

<svg data-fig="nosturi" viewBox="0 0 600 620" role="img" aria-label="Four situations in which the rope of a crane holds a crate. Each has the situation picture on the left and the free-body diagram of the crate on the right, where the crate is a rectangle: the weight G points down from the centre and the tension T of the rope points up from the top surface. Next to the free-body diagram there is a blue velocity arrow and an orange acceleration arrow when they are not zero. At the top left the crate is at rest, v and a are zero and the arrows T and G are equally long. At the top right the crate rises at constant velocity: the velocity is up, a is zero and the arrows are equally long. At the bottom left the crate rises while speeding up: the velocity and the acceleration are up, and T is longer than G. At the bottom right the crate rises while slowing down: the velocity is up but the acceleration is down, and T is shorter than G." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-4-nosturi.webp" x="1.2" y="1.2" width="597" height="618.2" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{at rest}$</div></foreignObject>
  <foreignObject x="185.5" y="249.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="185.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="224" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$v = 0$</div></foreignObject>
  <foreignObject x="224" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="296" y="7.5" width="308" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising at constant velocity}$</div></foreignObject>
  <foreignObject x="485.5" y="249.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="485.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="519.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="524" y="229.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="27.5" y="317.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising and speeding up}$</div></foreignObject>
  <foreignObject x="185.5" y="559.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="185.5" y="369.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="219.5" y="415.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="255.5" y="431.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="321" y="317.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising and slowing down}$</div></foreignObject>
  <foreignObject x="485.5" y="559.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="485.5" y="417.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="519.5" y="415.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="555.5" y="509.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

```pysahdy
A box rises on a rope and slows down. Which way does the net force point?
---
Downwards, because the acceleration points downwards even though the box is still moving up. The force of the rope is smaller than the weight.
```

### First the forces, then the equation
When the law is used in a calculation, the steps are always taken in the same order. Choose the object and draw its free-body diagram, in which every force has a cause: the Earth, a rope, a surface or a puller. Choose a positive direction, usually the direction of the acceleration. Only then write the net force from the forces, with signs, and set it equal to $ma$. For the crate of the crane, when up is positive, we get $T - G = ma$. In the chapter *Free-body diagrams and the combined effect of forces* the same method extends to slanted forces.

## Worked example
A construction crane lifts a concrete slab of mass $480\,\text{kg}$. The tension in the rope is $5.20\,\text{kN}$. What is the acceleration of the slab, and in which direction does it point? Air resistance is ignored.

<!-- vaihe -->

**Given and find.** $m = 480\,\text{kg}$, $T = 5.20\,\text{kN}$ and $g = 9.81\,\text{m/s}^2$. We want the acceleration $a$ and its direction.

<!-- vaihe -->

**Principle.** Choose the concrete slab as the object. The Earth (weight) and the rope (tension) act on it. By Newton's second law, the acceleration is determined by the sum of these forces. The force of the rope alone does not accelerate the slab, because most of it is used to hold up the weight.

<!-- vaihe -->

**Free-body diagram.** The slab is drawn as a rectangle. The weight $\overline{G}$ starts from the centre and points down, and the tension $\overline{T}$ starts from the top surface and points up. The positive direction is chosen to be up.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Free-body diagram of the concrete slab, the slab as a rectangle. The tension T of the rope starts from the top surface and points up, and the weight G starts from the centre and points down. The arrow T is a little longer than the arrow G. Separately on the right there is an orange acceleration arrow pointing up. On the right there is also a small arrow y pointing up: the positive direction is up. On the left is the situation picture: the hook of a crane lifts the concrete slab on a rope." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy44-ex-elem" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="110" y1="20" x2="110" y2="138" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M110,138 q-14,5 -12,19 q5,12 17,7" fill="none" stroke="#6c757d" stroke-width="5" stroke-linejoin="round"/>
  <line x1="104" y1="168" x2="66" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="168" x2="154" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="46" y="200" width="128" height="60" rx="2" fill="url(#fy44-ex-elem)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="46" y1="220" x2="174" y2="220" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="46" y1="240" x2="174" y2="240" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="8" y1="296" x2="212" y2="296" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="6" y="335.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation picture}$</div></foreignObject>
  <foreignObject x="296" y="335.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <line x1="228" y1="20" x2="228" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="285" y="165" width="110" height="50" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="340" y1="165" x2="340" y2="47" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M340,30 L348,48 L332,48 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="27.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="340" y1="190" x2="340" y2="295.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M340,312.5 L332,294.5 L348,294.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="292" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="470" y1="220" x2="470" y2="162" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476.5,173 L470,160 L463.5,173" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="453.5" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="560" y1="300" x2="560" y2="245" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M560,236 L564.5,246 L555.5,246 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="550" y="203.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Rearranged formula.** We start from Newton's second law $\Sigma F = ma$. From the diagram the net force is $T - mg$, and we solve for the acceleration:
```latex
\begin{aligned}
\Sigma F &= ma \\
T - mg &= ma \\
a &= \frac{T - mg}{m}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The tension is converted to newtons: $5.20\,\text{kN} = 5.20\cdot 1000\,\text{N} = 5200\,\text{N}$.

<!-- vaihe -->

**Substitution.** First we calculate the weight and then the acceleration:
```latex
\begin{aligned}
a &= \frac{T - mg}{m} \\
mg &= 480\,\text{kg}\cdot 9.81\,\text{m/s}^2 \\
&= 4708.8\,\text{N} \\
a &= \frac{5200\,\text{N} - 4708.8\,\text{N}}{480\,\text{kg}} \\
&\approx 1.02\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration is $a \approx 1.02\,\text{m/s}^2$ upward. All the given values have three significant figures: the mass $480\,\text{kg}$, the tension $5.20\,\text{kN}$ and the free-fall acceleration $9.81\,\text{m/s}^2$. So the result also has three significant figures.

<!-- vaihe -->

**Reasonableness.** The force of the rope is only about ten percent greater than the weight $4.71\,\text{kN}$, so the acceleration should also be about a tenth of the free-fall acceleration: $0.1\cdot 9.81\,\text{m/s}^2 \approx 1\,\text{m/s}^2$. If the weight were forgotten, the result would be $5200\,\text{N} : 480\,\text{kg} \approx 10.8\,\text{m/s}^2$. That would be wrong, because besides the force of the rope the weight acts on the element downward, and the acceleration is set by the sum of these forces. For example, when the element rises at a constant velocity, the rope pulls with a force equal to the weight and the forces cancel, but a calculation that forgets the weight would still give an acceleration of about $9.8\,\text{m/s}^2$.

## Common misconception
Many people think that a force always acts in the direction of motion and that the net force points in the direction of motion. The net force, however, points in the direction of the acceleration. When air resistance is ignored, a ball thrown upward keeps rising even though only its weight, which points down, acts on it, and that is why it slows down. In a slowing motion the net force points against the velocity. A second mistake is to think that a constant force keeps up a constant velocity. When the net force is constant and not zero, the velocity changes steadily. A third mistake is to confuse mass and weight. On a horizontal track the weight does not resist the motion, because the normal force cancels it: it is the mass that makes the acceleration smaller.

## Summary
- When the net force is zero, the velocity does not change. When it is not zero, the object accelerates in the direction of the net force.
- Newton's second law is $\Sigma\overline{F} = m\overline{a}$. The acceleration is directly proportional to the net force and inversely proportional to the mass.
- The net force points in the direction of the acceleration, which is not always the direction of the velocity: in a slowing motion it points against the velocity.
- First the free-body diagram is drawn and a positive direction is chosen, then $\Sigma F = ma$ is written with signs.
- The unit of force is $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.
