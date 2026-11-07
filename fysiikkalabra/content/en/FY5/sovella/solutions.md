## fy5-s1

### a)
**Given:** load $m = 2.0\,\text{t} = 2000\,\text{kg}$, jib $m_\text{p} = 4.0\,\text{t}$ and $r_\text{p} = 12\,\text{m}$, counterweight $m_\text{v} = 9.0\,\text{t}$ and $r_\text{v} = 10\,\text{m}$
**Find:** the distance $r$ of the trolley from the axis of the tower when the total moment of the weights is zero
**Principle:** Three weights act on the jib: the weight of the load at the trolley (through the cable), the weight of the jib itself at its centre of mass, and the weight of the counterweight. The jib turns about the vertical axis of the tower, but the vertical weights are parallel to this axis and do not turn the jib about it. The weights tend to tip the jib in its vertical plane, so the moments are calculated about the horizontal moment axis A, which passes through the tower perpendicular to this plane. The lever arm of each weight is the perpendicular distance of its line of action from the axis A. The weights are vertical and the axis horizontal, so the lever arm is the horizontal distance of the weight from the axis of the tower. The load and the weight of the jib turn the jib towards the side of the load, the counterweight in the opposite direction. In equilibrium with respect to rotation the sum of the moments is zero.
**Formula:** $m_\text{p} g r_\text{p} + m g r - m_\text{v} g r_\text{v} = 0$. The acceleration of free fall cancels, so $r = \dfrac{m_\text{v} r_\text{v} - m_\text{p} r_\text{p}}{m}$.
**Conversions:** $1\,\text{t} = 1000\,\text{kg}$, so $m_\text{p} = 4000\,\text{kg}$ and $m_\text{v} = 9000\,\text{kg}$.
**Substitution:** $r = \dfrac{9000\,\text{kg} \cdot 10\,\text{m} - 4000\,\text{kg} \cdot 12\,\text{m}}{2000\,\text{kg}} = \dfrac{42\,000\,\text{kg}\cdot\text{m}}{2000\,\text{kg}} = 21\,\text{m}$
**Answer:** $r \approx 21\,\text{m}$, two significant figures like the distances and masses.
**Reasonableness:** The moment of the counterweight is about twice the moment of the jib, so the load has to make up the difference. A light load has to be far out, and the point is within the $40\,\text{m}$ length of the jib.

### b)
**Given:** the data of part a, trolley at the tip of the jib $r_\text{max} = 40\,\text{m}$, permitted total moment $M_\text{max} = 600\,\text{kNm}$ and $g = 9.81\,\text{m/s}^2$
**Find:** the greatest load $m$ at the tip of the jib
**Principle:** When the load is at the tip, the total moment points towards the side of the load, and with the greatest permitted load it is equal to the limit. The moments are calculated about the moment axis A as in part a, with the positive direction of rotation towards the side of the load.
**Formula:** $m g r_\text{max} + m_\text{p} g r_\text{p} - m_\text{v} g r_\text{v} = M_\text{max}$, so $m = \dfrac{M_\text{max} + m_\text{v} g r_\text{v} - m_\text{p} g r_\text{p}}{g r_\text{max}}$
**Conversions:** $M_\text{max} = 600\,\text{kNm} = 600\,000\,\text{Nm}$
**Substitution:** $m_\text{p} g r_\text{p} = 4000\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 12\,\text{m} = 470\,880\,\text{Nm}$ and $m_\text{v} g r_\text{v} = 9000\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 10\,\text{m} = 882\,900\,\text{Nm}$. The moment of the load may therefore be $600\,000\,\text{Nm} + 882\,900\,\text{Nm} - 470\,880\,\text{Nm} = 1\,012\,020\,\text{Nm}$, so $m = \dfrac{1\,012\,020\,\text{Nm}}{9.81\,\text{m/s}^2 \cdot 40\,\text{m}} = 2579\,\text{kg}$
**Answer:** $m \approx 2.6\,\text{t}$, two significant figures like the data of the crane.
**Reasonableness:** Without a load the total moment is $882.9\,\text{kNm} - 470.9\,\text{kNm} = 412\,\text{kNm}$ towards the counterweight, so the limit is not exceeded even by the empty crane. The load at the tip is smaller than the load the crane carries closer to the tower, as in the load charts of cranes.

### c)
**Find:** whether the counterweight can be increased by a couple of tonnes so that heavier loads can be lifted from the tip
**Principle:** The moment of the counterweight turns the jib in the opposite direction to the load. The limit applies to the total moment in both directions, so both the fully loaded and the empty crane must be checked.
**Model answer:** *The loaded crane.* A larger counterweight reduces the total moment on the side of the load, so a heavier load could be lifted at the tip. The foreman is right about this.

*The empty crane.* Without a load the total moment points towards the counterweight: now it is $412\,\text{kNm}$. An addition of two tonnes increases it by $2000\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 10\,\text{m} = 196.2\,\text{kNm}$, so the total moment becomes $608\,\text{kNm}$. This exceeds the limit of $600\,\text{kNm}$, and the tower is overloaded on the side of the counterweight whenever there is no load on the hook.

*How much could be added.* For the empty crane there is room of $600\,\text{kNm} - 412\,\text{kNm} = 188\,\text{kNm}$ below the limit, so the counterweight can be increased by at most $188\,000\,\text{Nm} : (9.81\,\text{m/s}^2 \cdot 10\,\text{m}) \approx 1.9\,\text{t}$. Then the greatest load at the tip would be $1200\,\text{kNm} : 392.4\,\text{m}^2/\text{s}^2 \approx 3.1\,\text{t}$.

*Conclusion.* The suggestion does not work as it stands. In the model of the problem the counterweight is dimensioned so that the limit is not exceeded with the empty or the fully loaded crane. Instead of two tonnes, the counterweight could be increased by at most about $1.9\,\text{t}$, and the lifting capacity cannot be increased further without a sturdier tower. For a real crane one moment condition is not enough: the counterweight may be changed only as the manufacturer instructs, because safety also depends on, for example, the wind, the strength of the structures and the foundation.

### d)
**Find:** the free-body diagram of the load while the jib turns steadily, and an evaluation of the operator's explanation
**Principle:** The load is chosen as the object. The bodies interacting with it are the Earth (weight) and the cable (tension); nothing else touches the load, and air resistance is small at low speed. When the jib turns steadily, the load moves in a horizontal circle about the axis of the tower, so it has a centripetal acceleration towards the axis. The net force must then point towards the axis.

<svg data-fig="fy5-s1-fbd" viewBox="0 0 600 400" role="img" aria-label="Two pictures. On the left a side view of the situation: a part of the jib at the top, the axis of the tower as a dashed line on the left. The cable from the trolley is tilted so that the load is farther from the axis of the tower than the trolley. Next to the load an orange acceleration arrow a n points horizontally towards the axis of the tower. On the right the free-body diagram of the load, the load as a rectangle tilted along the cable: the weight G straight down from the centre and the tension S of the cable from the upper surface along the cable upwards and towards the axis of the tower. The tension is slightly longer than the weight, and its vertical component is equal to the weight. Separately an orange acceleration arrow a n to the left. The angle has been drawn much larger than in the problem so that the arrows can be told apart." style="max-width:100%;font-size:24px">
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <rect x="20" y="52" width="270" height="12" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <line x1="40" y1="34" x2="40" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="48" y="355.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{axis}$</div></foreignObject>
  <rect x="136" y="64" width="28" height="10" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="150" y1="74" x2="218.5" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="74" x2="150" y2="184" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <foreignObject x="154" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <path d="M192,271.5 L244.5,252.5 L257,286 L204.5,305.5 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="200" y1="330" x2="138" y2="330" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M149,323.5 L136,330 L149,336.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="103.5" y="293.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="390" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="346" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <rect x="420" y="214" width="60" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-20 450 236)"/>
  <line x1="450" y1="236" x2="450" y2="339" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M450,356 L442,338 L458,338 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="457.5" y="337.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="442.5" y1="215.5" x2="404.5" y2="111.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M399,95.5 L412.5,109.5 L397.5,115 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="360.5" y="81" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{S}$</div></foreignObject>
  <line x1="442.5" y1="215.5" x2="442.5" y2="97.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <line x1="575" y1="120" x2="517" y2="120" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M528,113.5 L515,120 L528,126.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="488.5" y="83.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <line x1="560" y1="350" x2="529" y2="350" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M520,350 L530,345.5 L530,354.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="560" y1="350" x2="560" y2="319" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M560,310 L564.5,320 L555.5,320 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="496" y="335.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="550" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

**Model answer:** The load is drawn as a rectangle tilted along the cable.
- The weight $\overline{G}$ starts from the centre and points straight down.
- The tension $\overline{S}$ of the cable starts from the upper surface where the cable is attached and points along the cable upwards and slightly towards the axis of the tower, because the load is farther out than the trolley.

In the vertical direction the load does not accelerate, so the vertical component of the tension is equal to the weight, and the tension is slightly larger than the weight. The horizontal component of the tension is the net force, and it points towards the axis of the tower like the centripetal acceleration $\overline{a}_\text{n}$, which is drawn separately in its own colour. In the model picture the angle of the cable has been drawn much larger than in the problem so that the arrows can be told apart.

*The operator's explanation.* There is no real centrifugal force: no body pulls the load outwards, and there is no outward force in the free-body diagram. When the jib starts to turn, the load tends to continue straight ahead because of its inertia. That is why it stays on the outer edge of the circle and the cable tilts, until the horizontal component of the tension is enough to turn the motion of the load onto a circular path. So the load is not thrown outwards but lags behind its straight path only by as much as the cable needs to pull it towards the centre.

### e)
**Given:** the radius $r = 21\,\text{m}$ of part a, period $T = 90\,\text{s}$, cable length $15\,\text{m}$ and $g = 9.81\,\text{m/s}^2$
**Find:** the angle $\theta$ between the cable and the vertical, and whether it matters
**Principle:** The load moves in uniform circular motion, so its acceleration is the centripetal acceleration $a_\text{n} = \tfrac{v^2}{r}$ towards the axis of the tower. The speed is obtained from the period. Newton's second law is written for the free-body diagram of part d by components: axis $x$ horizontally towards the axis of the tower and $y$ upwards. The tilt moves the load only by centimetres, so the distance of the trolley, $21\,\text{m}$, can be used as the radius of the circle.
**Formula:** $x$: $S\sin\theta = m\dfrac{v^2}{r}$ and $y$: $S\cos\theta - mg = 0$. Dividing the equations by each other gives $\tan\theta = \dfrac{v^2}{rg}$, where $v = \dfrac{2\pi r}{T}$. The mass cancels.
**Conversions:** Not needed.
**Substitution:** $v = \dfrac{2\pi \cdot 21\,\text{m}}{90\,\text{s}} = 1.466\,\text{m/s}$ and $\tan\theta = \dfrac{(1.466\,\text{m/s})^2}{21\,\text{m} \cdot 9.81\,\text{m/s}^2} = 0.01043$, so $\theta = 0.598^\circ$
**Answer:** $\theta \approx 0.60^\circ$, two significant figures like the period $90\,\text{s}$. The load has moved outwards from the trolley by $15\,\text{m} \cdot 0.01043 \approx 0.16\,\text{m}$.
**Reasonableness:** The centripetal acceleration $a_\text{n} = (1.466\,\text{m/s})^2 : 21\,\text{m} \approx 0.10\,\text{m/s}^2$ is only about one percent of the acceleration of free fall, so the angle is small and the tension is practically equal to the weight. Steady turning therefore hardly matters in lifting work. A sudden start or stop, on the other hand, makes the load swing, because the cable cannot immediately give the load the same acceleration as the trolley.

### Hyväksytään myös
- The moments of parts a and b can be calculated as products of mass and distance without the acceleration of free fall, when $g$ cancels, as long as in part b the limit is changed to the same form: $600\,000\,\text{Nm} : 9.81\,\text{m/s}^2 \approx 61\,160\,\text{kg}\cdot\text{m}$.
- In part b the answers $2.6\,\text{t}$ and $2580\,\text{kg}$ are accepted.
- In part e the angle may also be obtained by drawing the forces to scale when the centripetal acceleration has been calculated correctly, and $0.6^\circ$ is accepted as the answer.

### Yleisiä virheitä
- The moments are thought to be calculated about the vertical slewing axis of the tower, although the vertical weights do not turn the jib about it. The moments of the weights are calculated about the horizontal moment axis A.
- The weight of the jib itself is forgotten, or its moment is calculated from the end of the jib instead of its centre of mass.
- The directions of rotation of the moments are mixed up, so the counterweight and the weight of the jib are calculated in the same direction.
- In part b the limit is interpreted so that the total moment must be zero, which gives the load at the tip as only $42\,000\,\text{kg}\cdot\text{m} : 40\,\text{m} \approx 1.1\,\text{t}$.
- In part c only the loaded crane is checked and it is not noticed that the limit applies to the empty crane too.
- A centrifugal force pointing outwards, or the centripetal acceleration as a force, is drawn in the free-body diagram.
- In part e the rotation frequency is used wrongly instead of the period, or the angle is calculated using the length of the cable, although it does not affect the angle.

## fy5-s2

### a)
**Find:** a graph whose points, according to the circular-orbit model, fit a straight line through the origin
**Graph:** In the model, the moon is kept in a circular orbit by the gravity of Jupiter, which is the only significant force acting on the moon. It is the centripetal force of the circular motion of the moon: $\gamma\dfrac{Mm}{r^2} = m\dfrac{v^2}{r}$, so $v^2 = \gamma M \cdot \dfrac{1}{r}$. The orbital speed is calculated from the period: $v = \dfrac{2\pi r}{T}$, with the radius in metres and the period in seconds ($1\,\text{d} = 86\,400\,\text{s}$). For example, for Io $v = \dfrac{2\pi \cdot 421.8 \cdot 10^{6}\,\text{m}}{1.769 \cdot 86\,400\,\text{s}} = 17\,340\,\text{m/s}$, so $v^2 = 3.01 \cdot 10^{8}\,\text{m}^2/\text{s}^2$ and $\tfrac{1}{r} = 2.37 \cdot 10^{-9}\,\tfrac{1}{\text{m}}$.

| moon | $v\ (\text{km/s})$ | $\tfrac{1}{r}\ (10^{-9}\,\tfrac{1}{\text{m}})$ | $v^2\ (10^{8}\,\tfrac{\text{m}^2}{\text{s}^2})$ |
|---|---|---|---|
| Amalthea | $26.5$ | $5.51$ | $7.01$ |
| Io | $17.3$ | $2.37$ | $3.01$ |
| Europa | $13.7$ | $1.49$ | $1.89$ |
| Ganymede | $10.9$ | $0.935$ | $1.18$ |
| Callisto | $8.21$ | $0.531$ | $0.673$ |

$\tfrac{1}{r}$ is chosen for the horizontal axis and $v^2$ for the vertical axis.

<svg data-fig="fy5-s2-graph" viewBox="0 0 600 420" role="img" aria-label="Graph: the square of the orbital speed v of the moons as a function of the reciprocal of the orbital radius, 1 per r. Five black points: Callisto (0.53; 0.67), Ganymede (0.93; 1.18), Europa (1.49; 1.89), Io (2.37; 3.01) and Amalthea (5.51; 7.01), with the unit 10 to the power minus 9 per metre on the horizontal axis and 10 to the power 8 square metres per square second on the vertical axis. A straight line through the origin has been fitted to the points, and the point (5.0; 6.35) has been marked on it. The slope of the line is 1.27 times 10 to the power 17 cubic metres per square second." style="max-width:100%;font-size:24px">
  <line x1="143.5" y1="370" x2="143.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="196.5" y1="370" x2="196.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="370" x2="250" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="303.5" y1="370" x2="303.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="356.5" y1="370" x2="356.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="370" x2="410" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="331" x2="410" y2="331" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="292.5" x2="410" y2="292.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="254" x2="410" y2="254" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="215" x2="410" y2="215" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="176" x2="410" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="137.5" x2="410" y2="137.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="99" x2="410" y2="99" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="60" x2="410" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="370" x2="424" y2="370" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M436,370 L423,376 L423,364 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="371" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="143.5" y1="370" x2="143.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="133.5" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="196.5" y1="370" x2="196.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="186.5" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="250" y1="370" x2="250" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="303.5" y1="370" x2="303.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="293.5" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="356.5" y1="370" x2="356.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346.5" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="410" y1="370" x2="410" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="400" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="83" y1="331" x2="90" y2="331" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="292.5" x2="90" y2="292.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="278" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="254" x2="90" y2="254" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="215" x2="90" y2="215" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="200.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="176" x2="90" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="137.5" x2="90" y2="137.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="123" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="83" y1="99" x2="90" y2="99" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="60" x2="90" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="45.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <foreignObject x="60" y="375.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="442" y="355.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{1}{r}\ (\tfrac{10^{-9}}{\text{m}})$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v^2\ (10^{8}\,\tfrac{\text{m}^2}{\text{s}^2})$</div></foreignObject>
  <polyline points="90,370 410,74.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="384" cy="98.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="216.5" cy="253.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="169.5" cy="297" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="140" cy="324" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="118.5" cy="344" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="398" y="102.5" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{Amalthea}$</div></foreignObject>
  <foreignObject x="230.5" y="257.5" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{Io}$</div></foreignObject>
  <foreignObject x="183.5" y="301" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{Europa}$</div></foreignObject>
  <line x1="356.5" y1="124" x2="356.5" y2="370" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="124" x2="356.5" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="356.5" cy="124" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="203.5" y="87.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$(5.0;\ 6.35)$</span></div></foreignObject>
</svg>

**Model answer:** All five points are on the same straight line through the origin, so the circular-orbit model, in which gravity is the centripetal force, describes the motion of the moons well. The line passes through the origin because according to the model the orbital speed would be zero infinitely far away ($\tfrac{1}{r} = 0$). According to the model, the slope of the line is $\gamma M$, which is the same for all the moons, although the masses of the moons are very different.

### b)
**Given:** the graph of part a and $\gamma = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$
**Find:** the mass $M$ of Jupiter
**Principle:** According to the model $v^2 = \gamma M \cdot \tfrac{1}{r}$, so the slope $k$ of the line is $\gamma M$. The slope is read from a point of the line far from the origin, so that the relative error of the reading is small.
**Reading the graph:** The line passes through the origin and the point $(5.0 \cdot 10^{-9}\,\tfrac{1}{\text{m}};\ 6.35 \cdot 10^{8}\,\text{m}^2/\text{s}^2)$, so $k = \dfrac{6.35 \cdot 10^{8}\,\text{m}^2/\text{s}^2}{5.0 \cdot 10^{-9}\,\tfrac{1}{\text{m}}} = 1.27 \cdot 10^{17}\,\text{m}^3/\text{s}^2$.
**Formula:** $k = \gamma M$, so $M = \dfrac{k}{\gamma}$
**Conversions:** $1\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} = 1\,\tfrac{\text{m}^3}{\text{kg}\cdot\text{s}^2}$, because $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.
**Substitution:** $M = \dfrac{1.27 \cdot 10^{17}\,\text{m}^3/\text{s}^2}{6.674 \cdot 10^{-11}\,\tfrac{\text{m}^3}{\text{kg}\cdot\text{s}^2}} = 1.90 \cdot 10^{27}\,\text{kg}$
**Answer:** $M \approx 1.9 \cdot 10^{27}\,\text{kg}$. Two significant figures, because the slope is read from the graph to an accuracy of about two or three figures.
**Reasonableness:** The value in the data book is $1.898 \cdot 10^{27}\,\text{kg}$, about $320$ Earth masses, so the result is correct. Jupiter is the most massive planet in the Solar System, and its mass is about a thousandth of the mass of the Sun.

### c)
**Given:** the rotation period of Jupiter $T = 9.93\,\text{h}$ and $\gamma M = 1.27 \cdot 10^{17}\,\text{m}^3/\text{s}^2$ from part b
**Find:** the radius $r$ of the orbit of the probe
**Principle:** The probe stays above the same cloud formation only if it orbits Jupiter in the same direction and in the same time as the cloud formation, which the problem assumes to go round in the rotation period of Jupiter, $9.93\,\text{h}$. The orbit is thus an equatorial circular orbit synchronised with the rotation of Jupiter. The centripetal force of the circular motion of the probe is the gravity of Jupiter, as for the moons, so $v^2 = \dfrac{\gamma M}{r}$, and the orbital speed is $v = \dfrac{2\pi r}{T}$.
**Formula:** $\dfrac{4\pi^2 r^2}{T^2} = \dfrac{\gamma M}{r}$, so $r^3 = \dfrac{\gamma M T^2}{4\pi^2}$ and $r = \sqrt[3]{\dfrac{\gamma M T^2}{4\pi^2}}$
**Conversions:** $T = 9.93 \cdot 3600\,\text{s} = 35\,748\,\text{s}$
**Substitution:** $r^3 = \dfrac{1.27 \cdot 10^{17}\,\text{m}^3/\text{s}^2 \cdot (35\,748\,\text{s})^2}{4\pi^2} = 4.11 \cdot 10^{24}\,\text{m}^3$, so $r = 1.60 \cdot 10^{8}\,\text{m}$
**Answer:** $r \approx 1.6 \cdot 10^{8}\,\text{m} = 160\,000\,\text{km}$ from the centre of Jupiter. Two significant figures like the result of part b.
**Reasonableness:** The period $9.93\,\text{h}$ is shorter than that of Amalthea, $0.4982\,\text{d} \approx 12\,\text{h}$, so the orbit must be inside the orbit of Amalthea ($181\,400\,\text{km}$), as it is. The radius of Jupiter is about $71\,500\,\text{km}$, so the probe would orbit at a height of about $89\,000\,\text{km}$ above the clouds.

### d)
**Find:** an evaluation of the claim that Ganymede would orbit faster than Io on the orbit of Io, and the assumptions of the result of part b
**Principle:** The orbital speed is obtained from the condition that gravity is the centripetal force of the circular motion of the moon: $\gamma\dfrac{Mm}{r^2} = m\dfrac{v^2}{r}$, where $m$ is the mass of the moon.
**Model answer:** *The claim.* It is true that at the same distance a larger gravitational force acts on a more massive moon, because the force is proportional to the mass $m$ of the moon. However, a more massive moon needs a correspondingly larger centripetal force to stay on the same circular orbit, because the required force $m\tfrac{v^2}{r}$ is also proportional to the mass. The mass of the moon cancels from the equation, leaving $v^2 = \dfrac{\gamma M}{r}$: the orbital speed depends only on the mass $M$ of Jupiter and the radius of the orbit. On the orbit of Io, Ganymede would therefore orbit with the same speed and in the same time as Io. The claim is not correct. The same can be seen from the graph of part a: moons of very different masses are on the same line.

*The assumptions.* The result of part b requires that
- the orbits of the moons are circles whose centre is the centre of Jupiter; in reality Jupiter and the moon orbit their common centre of mass, but the masses of the moons are so small compared with the mass of Jupiter that the difference is insignificant
- only the gravity of Jupiter acts on the moon; the attractions of the other moons and the Sun are small in comparison
- the mass of Jupiter pulls as if it were concentrated at its centre, which holds well for a spherically symmetric body.

### Hyväksytään myös
- In part a the graph can also be drawn from the quantities $r^3$ and $T^2$, because the model gives $T^2 = \dfrac{4\pi^2}{\gamma M}\,r^3$; then in part b $M = \dfrac{4\pi^2}{\gamma k}$. The points then cluster near the origin, so the slope should be read near the point of Callisto.
- In part b slopes of $1.22\text{–}1.32 \cdot 10^{17}\,\text{m}^3/\text{s}^2$ and masses of $1.8\text{–}2.0 \cdot 10^{27}\,\text{kg}$ are accepted. A fit through the origin by a calculator or spreadsheet is also accepted.
- Part c can also be calculated from the period alone and a Kepler-type comparison with some moon, for example $r = r_\text{Io}\,\left(\tfrac{T}{T_\text{Io}}\right)^{2/3}$, as long as the relationship is justified from the circular-orbit model.

### Yleisiä virheitä
- The orbital speed is calculated in kilometres and days, but $\gamma$ is substituted in base units.
- The points are drawn in an $(r, v)$ coordinate system and a straight line is fitted to them, although the set of points is curved.
- The height above the surface of Jupiter is taken as the radius of the orbit, or the radius is measured from the surface of the moon.
- In part c $24\,\text{h}$ is used as the period, as for the geostationary orbit of the Earth.
- In part d it is only stated that "the mass does not matter", without showing that it cancels from the equation.

## fy5-s3

### a)
**Find:** a graph of the oscillation measurements whose points fit a straight line, and the model fitted to it
**Graph:** The period of a spring and a mass is $T = 2\pi\sqrt{\dfrac{m}{k}}$. Squaring the equation gives $T^2 = \dfrac{4\pi^2}{k}\,m$: the square of the period is proportional to the mass. The points are therefore drawn in a $(m, T^2)$ coordinate system. The period is a tenth of the measured time, for example $T = 4.74\,\text{s} : 10 = 0.474\,\text{s}$ and $T^2 = 0.2247\,\text{s}^2$.

| $m\ (\text{kg})$ | $T\ (\text{s})$ | $T^2\ (\text{s}^2)$ |
|---|---|---|
| $0.100$ | $0.474$ | $0.225$ |
| $0.150$ | $0.573$ | $0.328$ |
| $0.200$ | $0.650$ | $0.423$ |
| $0.250$ | $0.725$ | $0.526$ |
| $0.300$ | $0.786$ | $0.618$ |
| $0.350$ | $0.851$ | $0.724$ |

<svg data-fig="fy5-s3-graph" viewBox="0 0 600 420" role="img" aria-label="Graph: the square of the period T as a function of the hanging mass m. Six black points with masses 0.100–0.350 kg; T squared grows from 0.225 to 0.724 square seconds. A straight line has been fitted to the points so that it passes between them, and it has been extended with a dashed line to the vertical axis, which it meets at about 0.028 square seconds above the origin. The points (0.100 kg; 0.226 s²) and (0.350 kg; 0.722 s²) have been marked on the line." style="max-width:100%;font-size:24px">
  <line x1="144" y1="370" x2="144" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192" y1="370" x2="192" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="370" x2="240" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="288" y1="370" x2="288" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="370" x2="336" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="370" x2="384" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432" y1="370" x2="432" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="370" x2="480" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="331" x2="480" y2="331" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="292.5" x2="480" y2="292.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="254" x2="480" y2="254" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="215" x2="480" y2="215" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="176" x2="480" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137.5" x2="480" y2="137.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="99" x2="480" y2="99" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="480" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="370" x2="494" y2="370" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,370 L493,376 L493,364 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="371" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="144" y1="370" x2="144" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="192" y1="370" x2="192" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="169.5" y="379.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.1$</div></foreignObject>
  <line x1="240" y1="370" x2="240" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="288" y1="370" x2="288" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="265.5" y="379.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.2$</div></foreignObject>
  <line x1="336" y1="370" x2="336" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="384" y1="370" x2="384" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="361.5" y="379.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.3$</div></foreignObject>
  <line x1="432" y1="370" x2="432" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="480" y1="370" x2="480" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="457.5" y="379.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.4$</div></foreignObject>
  <line x1="89" y1="331" x2="96" y2="331" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="292.5" x2="96" y2="292.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="278" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.2$</div></foreignObject>
  <line x1="89" y1="254" x2="96" y2="254" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="215" x2="96" y2="215" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="200.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.4$</div></foreignObject>
  <line x1="89" y1="176" x2="96" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="137.5" x2="96" y2="137.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="123" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.6$</div></foreignObject>
  <line x1="89" y1="99" x2="96" y2="99" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="45.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.8$</div></foreignObject>
  <foreignObject x="66" y="375.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="355.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m\ (\text{kg})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T^2\ (\text{s}^2)$</div></foreignObject>
  <polyline points="163,305.5 461,67.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,359 163,305.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="192" cy="283" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="240" cy="243" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="288" cy="206.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="336" cy="166.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="384" cy="130.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432" cy="89.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="192" cy="282.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="432" cy="90" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="210" y="292" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$(0.100;\ 0.226)$</span></div></foreignObject>
  <foreignObject x="240" y="53.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$(0.350;\ 0.722)$</span></div></foreignObject>
</svg>

**Model answer:** The points are almost on a straight line, so the square of the period grows steadily with the mass, as the model predicts. A straight line is fitted to the points so that it passes between them; it is not forced through the origin, because the measured points do not point there. When the line is extended to the vertical axis, it meets the axis at about $0.028\,\text{s}^2$, slightly above the origin.

### b)
**Given:** the graph of part a
**Find:** the spring constant $k$ of the spring
**Principle:** According to the model $T^2 = \dfrac{4\pi^2}{k}\,m$ the slope of the line is $\dfrac{4\pi^2}{k}$. The intercept on the vertical axis does not affect the slope, so the spring constant is obtained from the slope although the line does not pass through the origin. The slope is read from two points of the line far apart from each other.
**Reading the graph:** The line passes through the points $(0.100\,\text{kg};\ 0.226\,\text{s}^2)$ and $(0.350\,\text{kg};\ 0.722\,\text{s}^2)$, so the slope is $\dfrac{0.722\,\text{s}^2 - 0.226\,\text{s}^2}{0.350\,\text{kg} - 0.100\,\text{kg}} = \dfrac{0.496\,\text{s}^2}{0.250\,\text{kg}} = 1.984\,\text{s}^2/\text{kg}$.
**Formula:** $\dfrac{4\pi^2}{k} = 1.984\,\text{s}^2/\text{kg}$, so $k = \dfrac{4\pi^2}{1.984\,\text{s}^2/\text{kg}}$
**Conversions:** $1\,\text{kg/s}^2 = 1\,\text{N/m}$, because $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.
**Substitution:** $k = \dfrac{4\pi^2}{1.984\,\text{s}^2/\text{kg}} = \dfrac{39.48}{1.984\,\text{s}^2/\text{kg}} = 19.9\,\text{kg/s}^2$
**Answer:** $k \approx 19.9\,\text{N/m}$, three significant figures, because the masses and times have been measured to three figures and the points are very close to the line.
**Reasonableness:** The spring stretches about $10\,\text{cm}$ under a $200\,\text{g}$ mass, which corresponds to a spring constant of about $20\,\text{N/m}$. Such a spring is typical in school oscillation experiments.

### c)
**Find:** what the deviation of the line from the origin can be due to and how reliable the spring constant of part b is
**Principle:** Random error scatters the points on both sides of the line. A systematic error or a deficiency of the model shifts the results in the same direction. The result is reliable when different methods give the same value within the uncertainties.
**Model answer:** *Uncertainty.* In hand timing the uncertainty due to reaction time is about $0.2\,\text{s}$. Spread over ten periods, it is only $0.02\,\text{s}$ in the period, which is the reason for measuring ten periods. The points deviate from the line by at most about $0.005\,\text{s}^2$, so the random variation is small and does not explain the intercept of $0.028\,\text{s}^2$ on the vertical axis.

*The cause of the deviation.* In the model $T = 2\pi\sqrt{\tfrac{m}{k}}$ only the mass oscillates and the spring is massless. The mass of the spring itself, $45\,\text{g}$, however, moves along: its lower end moves with the mass and its upper end is at rest. The oscillating mass is therefore larger than the hanging mass alone, which shifts the whole line upwards but does not change its slope. From the intercept the extra mass is $0.028\,\text{s}^2 : 1.984\,\text{s}^2/\text{kg} \approx 0.014\,\text{kg}$, about a third of the mass of the spring. The result makes sense, because the lower part of the spring moves almost as much as the mass and the upper part hardly at all.

*Comparison.* From the measurement at rest $k = \dfrac{mg}{x} = \dfrac{0.200\,\text{kg} \cdot 9.81\,\text{m/s}^2}{0.098\,\text{m}} \approx 20.0\,\text{N/m}$. It differs from the result of part b, $19.9\,\text{N/m}$, by less than one percent, so two independent methods support each other.

*Conclusion.* There is no contradiction: the spring constant is reliable, because it is obtained from the slope, which the mass of the spring does not affect. If the line had been forced through the origin, the spring constant would have been too small, about $18.9\,\text{N/m}$.

### d)
**Given:** $m = 0.250\,\text{kg}$, the mass of the spring $m_\text{s} = 45\,\text{g}$, amplitude $A = 5.0\,\text{cm}$ and $k = 19.9\,\text{N/m}$ from part b
**Find:** the greatest speed $v_\text{max}$ of the mass
**Principle:** The energy of the oscillation is conserved when friction and air resistance are small. At an extreme position the mass is momentarily at rest, and the whole energy $\tfrac{1}{2}kA^2$ is potential energy. At the equilibrium position the displacement is zero, so the whole energy is kinetic energy and the speed is greatest. For a vertical spring the weight only shifts the equilibrium position, so the displacement is measured from the equilibrium position. In the model of the problem the mass of the spring itself is taken into account as in part c: the lower part of the spring moves with the mass, so a third of the mass of the spring is added to the mass in the kinetic energy.
**Formula:** $\tfrac{1}{2}m_\text{eff}v_\text{max}^2 = \tfrac{1}{2}kA^2$, where $m_\text{eff} = m + \tfrac{1}{3}m_\text{s}$, so $v_\text{max} = A\sqrt{\dfrac{k}{m_\text{eff}}}$
**Conversions:** $A = 5.0\,\text{cm} = 0.050\,\text{m}$ and $m_\text{s} = 45\,\text{g} = 0.045\,\text{kg}$
**Substitution:** $m_\text{eff} = 0.250\,\text{kg} + 0.045\,\text{kg} : 3 = 0.265\,\text{kg}$ and $v_\text{max} = 0.050\,\text{m} \cdot \sqrt{\dfrac{19.9\,\text{N/m}}{0.265\,\text{kg}}} = 0.050\,\text{m} \cdot 8.67\,\tfrac{1}{\text{s}} = 0.433\,\text{m/s}$
**Answer:** $v_\text{max} \approx 0.43\,\text{m/s}$, two significant figures like the amplitude $5.0\,\text{cm}$.
**Reasonableness:** The period is about $2\pi\sqrt{0.265\,\text{kg} : 19.9\,\text{N/m}} \approx 0.73\,\text{s}$, and during a period the mass travels $4A = 20\,\text{cm}$, so its average speed is about $0.28\,\text{m/s}$. The greatest speed is larger than this, as it should be. A massless spring would give a slightly larger speed, about $0.45\,\text{m/s}$, because then none of the same energy goes to the spring.

### Hyväksytään myös
- In part b slopes of $1.95\text{–}2.02\,\text{s}^2/\text{kg}$ and the spring constants calculated from them, $19.5\text{–}20.2\,\text{N/m}$, are accepted, as is a line fitted by a calculator or spreadsheet ($19.9\,\text{N/m}$).
- The graph of part a can also be drawn from the quantities $m$ and $T^2$ with the mass on a gram scale; in part b the unit must then be converted.
- In part c the deviation can also be explained by a systematic error, when the explanation is justified and it is stated that an addition of constant size does not change the slope.
- In part d, $v_\text{max} \approx 0.45\,\text{m/s}$ calculated with a massless spring is also accepted when the student says that the mass of the spring is ignored and justifies the assumption. So is the added mass of $14\,\text{g}$ from the intercept of part c, which gives the same $0.43\,\text{m/s}$.

### Yleisiä virheitä
- A $(m, T)$ graph is drawn and a straight line is fitted to its curved set of points.
- The time of ten periods is used as the period without dividing it by ten.
- The line is forced through the origin because "according to the model it must pass through the origin", which makes the spring constant too small.
- $k$ is calculated directly from the slope without the factor $4\pi^2$ or as its reciprocal.
- In part d the amplitude is substituted in centimetres, or the gravitational potential energy is added to the energy, although the displacement is measured from the equilibrium position.

## fy5-s4

### a)
**Given:** the graph of the signal of the microphone over the interval $0\text{–}20\,\text{ms}$
**Find:** the frequency $f$ of the sound
**Principle:** The period of a periodic motion is the time after which the whole waveform starts to repeat in the same form. The signal is not a sine wave: each period has a high and a low peak, so the distance between two adjacent peaks is not the period. The reading is more accurate when the duration of several periods is read.
**Reading the graph:** The high peaks are at $1\,\text{ms}$, $5\,\text{ms}$, $9\,\text{ms}$, $13\,\text{ms}$ and $17\,\text{ms}$. The graph has five whole periods in a time of $20.0\,\text{ms}$, so $T = \dfrac{20.0\,\text{ms}}{5} = 4.0\,\text{ms}$.
**Formula:** $f = \dfrac{1}{T}$
**Conversions:** $T = 4.0\,\text{ms} = 0.0040\,\text{s}$
**Substitution:** $f = \dfrac{1}{0.0040\,\text{s}} = 250\,\tfrac{1}{\text{s}} = 250\,\text{Hz}$
**Answer:** $f = 250\,\text{Hz}$. Two or three significant figures: the duration of five periods can be read accurately from the guide lines.
**Reasonableness:** The frequency is typical of the sound of an instrument, close to middle C. The shape of the signal shows that in addition to the fundamental frequency it contains double the frequency, $500\,\text{Hz}$: the distance between a high and a low peak is half a period. If the distance between peaks, $2.0\,\text{ms}$, is taken as the period, $500\,\text{Hz}$ is wrongly obtained.

### b)
**Given:** the fundamental frequency $f = 250\,\text{Hz}$ and the speed of sound $v = 343\,\text{m/s}$; the pipe is open at both ends
**Find:** the length $L$ of the pipe
**Principle:** A standing wave forms in the air column of the pipe when the sound wave is reflected from the ends of the tube. At an open end the air can move freely, so there is an antinode of the oscillation there. When both ends are open, in the fundamental mode the tube has two antinodes at the ends and one node in the middle, so the length of the tube is half the wavelength. The wavelength is obtained from the basic equation of waves $v = f\lambda$.
**Formula:** $L = \dfrac{\lambda}{2}$ and $\lambda = \dfrac{v}{f}$, so $L = \dfrac{v}{2f}$
**Conversions:** Not needed.
**Substitution:** $L = \dfrac{343\,\text{m/s}}{2 \cdot 250\,\text{Hz}} = 0.686\,\text{m}$
**Answer:** $L \approx 0.686\,\text{m}$, three significant figures like the speed of sound.
**Reasonableness:** The wavelength is $1.37\,\text{m}$, and the pipe is half of it, just under seventy centimetres, which is a usual size for an organ pipe of this pitch. A real pipe is slightly shorter, because the antinode of the standing wave is a little outside the end of the tube.

### c)
**Given:** $L = 0.686\,\text{m}$, $v = 343\,\text{m/s}$ at a temperature of $20.0\,{}^\circ\text{C}$, the speed of sound decreases by about $0.6\,\text{m/s}$ per degree, winter temperature $8.0\,{}^\circ\text{C}$
**Find:** the change $\Delta f$ of the fundamental frequency
**Principle:** The wavelength of the standing wave is determined by the length of the pipe, $\lambda = 2L$, which practically does not change. In cold air sound travels more slowly, so with the same wavelength the frequency $f = \tfrac{v}{\lambda}$ decreases in the same proportion as the speed of sound.
**Formula:** $v' = v - 0.6\,\tfrac{\text{m/s}}{{}^\circ\text{C}} \cdot \Delta T$, $f' = \dfrac{v'}{2L}$ and $\Delta f = f - f'$
**Conversions:** The temperature falls by $20.0\,{}^\circ\text{C} - 8.0\,{}^\circ\text{C} = 12.0\,{}^\circ\text{C}$.
**Substitution:** $v' = 343\,\text{m/s} - 12.0 \cdot 0.6\,\text{m/s} = 335.8\,\text{m/s}$ and $f' = \dfrac{335.8\,\text{m/s}}{2 \cdot 0.686\,\text{m}} = 244.8\,\text{Hz}$, so $\Delta f = 250\,\text{Hz} - 244.8\,\text{Hz} = 5.2\,\text{Hz}$
**Answer:** The fundamental frequency decreases by about $5\,\text{Hz}$ (more precisely $5.2\,\text{Hz}$) to about $245\,\text{Hz}$. The change is known to one significant figure, because the change of speed $0.6\,\text{m/s}$ per degree is given to one figure.
**Reasonableness:** The speed of sound decreases by about $2\,\%$, so the frequency also decreases by about $2\,\%$, and $2\,\%$ of $250\,\text{Hz}$ is $5\,\text{Hz}$. A semitone at this pitch is about $15\,\text{Hz}$, so in winter the organ sounds about a third of a semitone lower. That is why organs are tuned at the temperature at which they are usually played.

### d)
**Given:** the sound level $L_1 = 88\,\text{dB}$, treated as an intensity level in a free sound field, at a distance $r_1 = 4.0\,\text{m}$, the distance of the organist $r_2 = 2.0\,\text{m}$, practice time $3\,\text{h}$; upper action value $L_0 = 85\,\text{dB}$ and the corresponding time $t_0 = 8\,\text{h}$
**Find:** the daily reference time $t_\text{ref}$ of the organist, the time in which the energy dose of the upper action value builds up, and whether the dose of the practice stays below it
**Principle:** When a source radiates uniformly in all directions, the same power spreads over the surface of a sphere $4\pi r^2$, so the intensity is $I = \dfrac{P}{4\pi r^2}$. When the distance is halved, the intensity quadruples. The change in the intensity level is obtained from the ratio of the intensities. The reference time, in which the same energy dose builds up, halves for every $3\,\text{dB}$ rise.
**Formula:** $L_2 - L_1 = 10\,\text{dB} \cdot \lg \dfrac{I_2}{I_1}$, where $\dfrac{I_2}{I_1} = \left(\dfrac{r_1}{r_2}\right)^2$; $n = \dfrac{L_2 - L_0}{3\,\text{dB}}$ and $t_\text{ref} = \dfrac{t_0}{2^{\,n}}$
**Conversions:** Not needed.
**Substitution:** $\dfrac{I_2}{I_1} = \left(\dfrac{4.0\,\text{m}}{2.0\,\text{m}}\right)^2 = 4$, so $L_2 = 88\,\text{dB} + 10\,\text{dB} \cdot \lg 4 = 88\,\text{dB} + 6.0\,\text{dB} = 94\,\text{dB}$. $n = \dfrac{94\,\text{dB} - 85\,\text{dB}}{3\,\text{dB}} = 3.0$ and $t_\text{ref} = \dfrac{8\,\text{h}}{2^{3}} = 1.0\,\text{h}$
**Answer:** $t_\text{ref} \approx 1\,\text{h}$. The dose does not stay below the reference dose: three hours of practice is about three times the reference time, so the dose is about $300\,\%$ of the reference dose. The organist should use hearing protection or practise with quieter stops.
**Reasonableness:** A level of $94\,\text{dB}$ is of the same order as the noise of a lawn mower at the ear of the user, when hearing protection is recommended. In the point-source model the sound power of the organ would be $P = I \cdot 4\pi r^2 \approx 0.13\,\text{W}$, which is plausible for an instrument.

### e)
**Find:** an evaluation of the assumptions of the model of part d, the direction of the real exposure, and a reliable way to find it out
**Principle:** The point-source model assumes that sound starts from a single point and travels without obstacles or reflections. For each assumption we consider whether the level at the organist would in reality be larger or smaller than the model gives.
**Model answer:** *The organ is not a point source.* The pipes are spread over an area several metres wide and high, and the distance of the organist from most of the pipes is much more than $2\,\text{m}$. Near an extended source the level does not rise by $6\,\text{dB}$ every time the distance is halved, so the $94\,\text{dB}$ of part d is probably too large an estimate.

*Reflections.* The walls, floor and vaults of the church reflect sound, and reverberation is heard throughout the hall. Part of the level measured at a distance of $4.0\,\text{m}$ is reverberation, which does not get louder closer up. This also makes the estimate too large.

*Playing.* During practice the organ is seldom played at full power all the time, so the average level is lower. On the other hand, in some churches the position of the pipes and the console may direct sound straight at the organist.

*A reliable way.* A sound level meter measures the A-weighted level at the organist's ear throughout a normal practice and the daily noise exposure is calculated from it as an energy average and compared with the action values $80\,\text{dB}$ and $85\,\text{dB}$. The exposure is probably smaller than the estimate of part d, but only a measurement tells whether hearing protection is needed. Even staying below an action value does not guarantee safe hearing, so hearing protection is worth using in loud practices.

### Hyväksytään myös
- In part a the period can also be read from the duration of two or three periods; answers of $240\text{–}260\,\text{Hz}$ are accepted.
- In part c the answers $5\,\text{Hz}$ and $5.2\,\text{Hz}$ are accepted. The change can also be calculated from the ratio $\dfrac{\Delta f}{f} = \dfrac{\Delta v}{v}$.
- In part d the change of level can also be calculated from the intensities: $I_1 = 10^{-12}\,\tfrac{\text{W}}{\text{m}^2} \cdot 10^{8.8}$ and $I_2 = 4I_1$.

### Yleisiä virheitä
- In part a the distance between two adjacent peaks, $2.0\,\text{ms}$, is taken as the period, which wrongly gives a frequency of $500\,\text{Hz}$.
- In part b the condition $L = \tfrac{\lambda}{4}$ for a tube closed at one end is used, although the pipe is open at both ends.
- In part c it is assumed that the wavelength changes and the frequency stays the same, or the change of frequency is calculated to be the same as the change of speed.
- In part d the level is assumed to double when the distance is halved, or the intensity is assumed to depend on the distance and not on its square.
- The reference time is calculated by dividing $8\,\text{h}$ by the difference of the levels instead of halving the time for each step of $3\,\text{dB}$.
