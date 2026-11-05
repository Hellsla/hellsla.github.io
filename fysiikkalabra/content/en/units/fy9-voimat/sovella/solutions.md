## fy9-voimat-s1

### a)
**Find:** the free-body diagram of the boat when the winch pulls it up the ramp at a constant velocity
**Principle:** The boat is chosen as the object and its interactions are found: the Earth (weight), the slide strips of the ramp (normal force and friction) and the cable (tension). The boat slides up the ramp, so kinetic friction points down the ramp. The velocity is constant, so the sum of the forces is zero.
**Model answer:** The boat is drawn as a rectangle parallel to the ramp.
- The weight $\overline{G}$ starts from the centre and points straight down, not perpendicular to the ramp.
- The normal force $\overline{N}$ starts from the bottom and points perpendicular to the ramp, outwards. It is as large as the component of the weight perpendicular to the ramp, so it is slightly smaller than the weight.
- Kinetic friction $\overline{F}_\mu$ starts from the lower corner of the bottom and points down the ramp.
- The tension of the cable $\overline{T}$ starts from the bow and points up the ramp.

Lengths of the arrows: $\overline{T}$ is as long as the friction and the component of the weight along the ramp together, because the net force is zero. The velocity may be marked separately next to the diagram, but not as a force.
```voimakuvio
pinta 14
G 2746,8
N 2665,2
F_mu 666,3 alas
T 1330,8 14
a 0
v ylös
```

### b)
**Given:** mass $m = 280\,\text{kg}$, angle of inclination of the ramp $\alpha = 14^\circ$, coefficient of kinetic friction $\mu = 0.25$, velocity constant, $g = 9.81\,\text{m/s}^2$
**Find:** the tension $T$ of the winch cable
**Principle:** The velocity is constant, so by Newton's first law the sum of the forces is zero both along the ramp and perpendicular to it. The boat slides, so the friction is kinetic friction $\mu N$, and perpendicular to the ramp only the component of the weight and the normal force act (chapter *Weight, friction and the inclined plane*).
**Free-body diagram:** the diagram of part a; the $x$ axis up the ramp and the $y$ axis perpendicular to the ramp, outwards. The components of the weight are $G_x = mg\sin\alpha$ down the ramp and $G_y = mg\cos\alpha$ towards the ramp.
```voimakuvio
pinta 14
G 2746,8
N 2665,2
F_mu 666,3 alas
T 1330,8 14
a 0
akselit 14
komponentit G
```
**Formula:** $y$: $N - mg\cos\alpha = 0$ and $x$: $T - mg\sin\alpha - \mu N = 0$, so $T = mg(\sin\alpha + \mu\cos\alpha)$
**Conversions:** None needed, the quantities are in base units.
**Substitution:** $T = 280\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot (\sin 14^\circ + 0.25 \cdot \cos 14^\circ) = 2746.8\,\text{N} \cdot (0.2419 + 0.2426) = 1330.8\,\text{N}$
**Answer:** $T \approx 1.3\,\text{kN}$, two significant figures like the angle $14^\circ$ and the coefficient of friction $0.25$.
**Reasonableness:** The component of the weight along the ramp is $665\,\text{N}$ and the friction $666\,\text{N}$, so the winch works against friction almost as much as it lifts the boat. The pull is about half of the weight $2.7\,\text{kN}$: the ramp makes the work lighter, but friction takes a large part of it.

### c)
**Given:** $m = 280\,\text{kg}$, $\alpha = 14^\circ$, coefficient of static friction $\mu_0 = 0.35$, $g = 9.81\,\text{m/s}^2$
**Find:** whether the boat stays at rest, and the smallest angle of inclination $\alpha_0$ at which the boat starts to slide by itself
**Principle:** Once the cable is slack, the forces on the boat are the weight, the normal force and static friction, which points up the ramp. Static friction is only as large as the situation requires, at most $\mu_0 N$. The boat stays in place if the static friction needed, $mg\sin\alpha$, does not exceed this upper limit (chapter *Weight, friction and the inclined plane*).
**Free-body diagram:** The boat as a rectangle parallel to the ramp: the weight from the centre downwards, the normal force from the bottom perpendicular to the ramp, outwards, and static friction from the upper corner of the bottom up the ramp, as large as the component of the weight along the ramp.
```voimakuvio
pinta 14
G 2746,8
N 2665,2
F_mu 664,5 ylös
a 0
```
**Formula:** The boat stays when $mg\sin\alpha \le \mu_0 mg\cos\alpha$, that is $\tan\alpha \le \mu_0$. At the limiting angle $\tan\alpha_0 = \mu_0$, so $\alpha_0 = \arctan\mu_0$
**Conversions:** None needed. The mass cancels.
**Substitution:** The static friction needed is $mg\sin\alpha = 2746.8\,\text{N} \cdot \sin 14^\circ = 664.5\,\text{N}$ and the upper limit $\mu_0 mg\cos\alpha = 0.35 \cdot 2746.8\,\text{N} \cdot \cos 14^\circ = 932.8\,\text{N}$; the limiting angle $\alpha_0 = \arctan 0.35 = 19.29^\circ$
**Answer:** The boat stays in place, because $664.5\,\text{N} < 932.8\,\text{N}$ (equally, $\tan 14^\circ \approx 0.25 < 0.35$). It would start to slide by itself if the ramp were at an angle of at least about $19^\circ$; two significant figures like the coefficient of friction $0.35$.
**Reasonableness:** The limiting angle does not depend on the mass, because both the component pulling down the ramp and the upper limit of friction are proportional to the mass. A wet, slippery or icy strip can lower the coefficient of static friction, and then the boat can start moving on a gentler ramp too: the boat should not be left held by friction alone.

### Yleisiä virheitä
- A "force of motion" up the ramp is drawn in the free-body diagram in addition to the force of the cable, or the components of the weight are drawn as forces of their own in addition to the weight.
- The normal force is taken as $N = mg$, although on the ramp $N = mg\cos\alpha$.
- Friction is drawn up the ramp, although the boat slides up and kinetic friction opposes the sliding.
- In part c static friction is taken directly as $\mu_0 N$, although that is only the upper limit; or the condition for sliding is written with the sine, $\sin\alpha_0 = \mu_0$.

### Hyväksytään myös
- In part c the comparison $\tan 14^\circ \approx 0.25 < \mu_0 = 0.35$ without numerical values of the forces.

## fy9-voimat-s2

### a)
**Find:** the free-body diagrams of sledge A and sledge B during the acceleration
**Principle:** Each of the connected bodies is chosen as the object in turn, and each gets its own diagram containing only the forces acting on it. A rope pulls each sledge towards itself: rope 2 pulls A backwards and B forwards with forces of the same magnitude, because the rope is light.
**Model answer:** Each sledge is drawn as a rectangle of its own.
- Sledge A: weight $\overline{G}_\text{A}$ down, normal force $\overline{N}_\text{A}$ up, the force of rope 1 $\overline{T}_1$ forwards, the force of rope 2 $\overline{T}_2$ backwards and kinetic friction $\overline{F}_{\mu\text{A}}$ backwards.
- Sledge B: weight $\overline{G}_\text{B}$ down, normal force $\overline{N}_\text{B}$ up, the force of rope 2 $\overline{T}_2$ forwards and kinetic friction $\overline{F}_{\mu\text{B}}$ backwards.

The net force on each sledge points forwards, because the sledges accelerate. The acceleration is marked next to the diagrams in its own colour. The snowmobile is not drawn, and the force of B on the rope is not drawn in the diagram of B. The horizontal forces are drawn to a scale of their own, because they are much smaller than the weights.
```voimakuvio
pinta 0
G 1177,2
N 1177,2
T_1 296,2 0
T_2 118,48 180
F_mu 117,72 vasen
a oikea
---
pinta 0
G 784,8
N 784,8
T_2 118,48 0
F_mu 78,48 vasen
a oikea
```

### b)
**Given:** $m_\text{B} = 80\,\text{kg}$, coefficient of kinetic friction $\mu = 0.10$, acceleration $a = 0.50\,\text{m/s}^2$, $g = 9.81\,\text{m/s}^2$
**Find:** the tension $T_2$ in rope 2
**Principle:** The horizontal forces on sledge B are the pull of rope 2 forwards and friction backwards. By Newton's second law their sum is $m_\text{B} a$. There is no vertical acceleration, so $N_\text{B} = m_\text{B} g$ and the friction is $\mu m_\text{B} g$ (chapter *Equation of motion for connected bodies*).
**Formula:** $T_2 - \mu m_\text{B} g = m_\text{B} a$, so $T_2 = m_\text{B}(a + \mu g)$
**Conversions:** None needed, the quantities are in base units.
**Substitution:** $T_2 = 80\,\text{kg} \cdot (0.50\,\text{m/s}^2 + 0.10 \cdot 9.81\,\text{m/s}^2) = 80\,\text{kg} \cdot 1.481\,\text{m/s}^2 = 118.48\,\text{N}$
**Answer:** $T_2 \approx 120\,\text{N}$, two significant figures like the acceleration $0.50\,\text{m/s}^2$ and the coefficient of friction $0.10$.
**Reasonableness:** The friction on B is $0.10 \cdot 80\,\text{kg} \cdot 9.81\,\text{m/s}^2 \approx 78\,\text{N}$ and accelerating it takes $80\,\text{kg} \cdot 0.50\,\text{m/s}^2 = 40\,\text{N}$; together about $118\,\text{N}$, as it should be.

### c)
**Given:** $m_\text{A} = 120\,\text{kg}$, $m_\text{B} = 80\,\text{kg}$, $\mu = 0.10$, $a = 0.50\,\text{m/s}^2$, from part b $T_2 = 118.48\,\text{N}$, $g = 9.81\,\text{m/s}^2$
**Find:** the tension $T_1$ in rope 1
**Principle:** The horizontal forces on sledge A are the pull of rope 1 forwards and the pull of rope 2 and friction backwards, and their sum is $m_\text{A} a$. The same result comes from the system of both sledges, in which the forces of rope 2 are internal and cancel each other.
**Formula:** $T_1 - T_2 - \mu m_\text{A} g = m_\text{A} a$, so $T_1 = T_2 + m_\text{A}(a + \mu g) = (m_\text{A} + m_\text{B})(a + \mu g)$
**Conversions:** None needed, the quantities are in base units.
**Substitution:** $T_1 = 118.48\,\text{N} + 120\,\text{kg} \cdot 1.481\,\text{m/s}^2 = 118.48\,\text{N} + 177.72\,\text{N} = 296.2\,\text{N}$
**Answer:** $T_1 \approx 300\,\text{N}$ ($296\,\text{N}$), two significant figures like the data.
**Reasonableness:** Check with the system: $(120 + 80)\,\text{kg} \cdot 1.481\,\text{m/s}^2 = 296.2\,\text{N}$, the same result. The front rope is tighter, because it accelerates and pulls both sledges.

### d)
**Find:** whether the claim "the force of the rear rope is half the force of the front rope" holds
**Principle:** Each rope pulls all the sledges behind it. When the coefficient of friction is the same, every sledge needs a pull $m(a + \mu g)$, that is, the pull needed is proportional to the mass.
**Model answer:** The claim does not hold. Rope 2 pulls only sledge B, rope 1 both sledges. From the results of parts b and c, $T_2 : T_1 = 118\,\text{N} : 296\,\text{N} = 0.40$, which is the same as the ratio of the masses $80\,\text{kg} : 200\,\text{kg}$. So the ratio depends on the masses of the sledges, not on their number. It would be a half only if the sledges were equally heavy and had the same coefficient of friction.

### Yleisiä virheitä
- Both sledges are drawn in one diagram, or the force of the snowmobile is drawn directly on sledge B.
- The backward force of rope 2 is missing from the diagram of sledge A, so $T_1$ comes out too small ($T_1 = m_\text{A}(a + \mu g) \approx 178\,\text{N}$).
- Friction is forgotten, and the tension is calculated as $ma$ alone.
- The rope forces $\overline{T}_1$ and $\overline{T}_2$ are given the same symbol, so the equations do not show which rope is meant.

### Hyväksytään myös
- In part c treating both sledges as one body, when the solution states that the forces of rope 2 are internal to the system.

## fy9-voimat-s3

### a)
**Find:** a graph of the cart's acceleration as a function of the pulling force and a model fitted to it
**Graph:** The pulling force $F\ (\text{N})$ is on the horizontal axis and the acceleration $a\ (\text{m/s}^2)$ on the vertical axis. The horizontal axis starts from zero, so that the point where the line crosses the axis can be seen.

<svg data-fig="fy9-voimat-s3-graph" viewBox="0 0 600 440" role="img" aria-label="Graph: the acceleration a of the cart as a function of the pulling force F. Seven black points at forces 0.40–1.60 N. A rising straight line is fitted to the points and extended as a dashed line down to the horizontal axis. The line passes through the points (0.40 N; 0.19 m/s²) and (1.60 N; 1.60 m/s²); these two points on the line are circled. The line crosses the horizontal axis at about F = 0.24 N and does not pass through the origin." style="max-width:100%;font-size:24px">
  <line x1="141" y1="380" x2="141" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="380" x2="186" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="380" x2="230.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="380" x2="275.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="380" x2="320.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="380" x2="365.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="380" x2="410" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="380" x2="455" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="380" x2="500" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="344.5" x2="500" y2="344.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="309" x2="500" y2="309" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="273.5" x2="500" y2="273.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="238" x2="500" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="202" x2="500" y2="202" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="166.5" x2="500" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="131" x2="500" y2="131" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="95.5" x2="500" y2="95.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="500" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="514" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,380 L513,386 L513,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="380" x2="141" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="380" x2="186" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="163.5" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.4$</div></foreignObject>
  <line x1="230.5" y1="380" x2="230.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="380" x2="275.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="253" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.8$</div></foreignObject>
  <line x1="320.5" y1="380" x2="320.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="380" x2="365.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="343" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.2$</div></foreignObject>
  <line x1="410" y1="380" x2="410" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="380" x2="455" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="432.5" y="389.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.6$</div></foreignObject>
  <line x1="500" y1="380" x2="500" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="344.5" x2="96" y2="344.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="309" x2="96" y2="309" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="294.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.4$</div></foreignObject>
  <line x1="89" y1="273.5" x2="96" y2="273.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="238" x2="96" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="223.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.8$</div></foreignObject>
  <line x1="89" y1="202" x2="96" y2="202" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="166.5" x2="96" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="152" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.2$</div></foreignObject>
  <line x1="89" y1="131" x2="96" y2="131" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="95.5" x2="96" y2="95.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="81" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.6$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="365.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a\ (\text{m/s}^2)$</div></foreignObject>
  <polyline points="186,346.5 455,95.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="149.5,380 186,346.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="186" cy="344.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="230.5" cy="307" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="275.5" cy="261" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="223.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="365.5" cy="177.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="410" cy="140" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="455" cy="94" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186" cy="346" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="455" cy="95.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="149.5" cy="380" r="7" fill="#e8590c"/>
  <foreignObject x="159.5" y="337.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$F_0 \approx 0.24\,\text{N}$</div></foreignObject>
  <foreignObject x="189" y="107.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$k \approx 1.18\,\tfrac{1}{\text{kg}}$</div></foreignObject>
</svg>

The circled points are the two points on the line from which the slope in part b is read. The dashed line is the extension of the line to the horizontal axis.

**Model answer:** The points lie almost on a straight line, so the acceleration increases steadily as the pulling force increases. A single straight line passing between the points is fitted to them; the points are not joined into a broken line. In real measurement series the measured points do not usually lie exactly on the same line because of measurement uncertainty. The line does not pass through the origin: it crosses the horizontal axis at about $0.24\,\text{N}$. That is why the line is not forced through the origin but extended to the horizontal axis for part b.

### b)
**Given:** the graph of part a and points read from the line
**Find:** the mass $m$ of the cart and the friction force $F_\mu$
**Principle:** The horizontal forces on the cart are the pull of the string $F$ forwards and friction $F_\mu$ backwards. By Newton's second law $F - F_\mu = ma$, so $a = \tfrac{1}{m}F - \tfrac{F_\mu}{m}$ is the equation of a straight line: the slope is $\tfrac{1}{m}$, and the line crosses the horizontal axis at $F = F_\mu$, where the pull just cancels the friction. That is why the line does not pass through the origin (chapter *Newton's second law*).
**Reading the graph:** Two points far apart on the line, not measured points, are read: $(0.40\,\text{N};\ 0.19\,\text{m/s}^2)$ and $(1.60\,\text{N};\ 1.60\,\text{m/s}^2)$. The line crosses the horizontal axis at about $F_0 = 0.24\,\text{N}$.
**Formula:** $k = \dfrac{\Delta a}{\Delta F} = \dfrac{1}{m}$, so $m = \dfrac{1}{k}$; and $F_\mu = F_0 = F_1 - \dfrac{a_1}{k}$
**Conversions:** $1\,\tfrac{\text{m/s}^2}{\text{N}} = 1\,\tfrac{\text{m/s}^2}{\text{kg} \cdot \text{m/s}^2} = 1\,\tfrac{1}{\text{kg}}$, so the reciprocal of the slope is in kilograms.
**Substitution:** $k = \dfrac{1.60\,\text{m/s}^2 - 0.19\,\text{m/s}^2}{1.60\,\text{N} - 0.40\,\text{N}} = \dfrac{1.41\,\text{m/s}^2}{1.20\,\text{N}} = 1.175\,\tfrac{1}{\text{kg}}$, so $m = \dfrac{1}{1.175\,\tfrac{1}{\text{kg}}} = 0.851\,\text{kg}$ and $F_\mu = 0.40\,\text{N} - \dfrac{0.19\,\text{m/s}^2}{1.175\,\tfrac{1}{\text{kg}}} = 0.238\,\text{N}$
**Answer:** $m \approx 0.85\,\text{kg}$ and $F_\mu \approx 0.24\,\text{N}$, two significant figures, because the slope read from the line is accurate to about $\pm 0.03\,\tfrac{1}{\text{kg}}$.
**Reasonableness:** The mass of a laboratory cart is typically less than a kilogram. The least-squares line gives the same: $k = 1.175\,\tfrac{1}{\text{kg}}$ and the intercept $0.239\,\text{N}$. The friction is small compared with the pull, as it should be for a cart on wheels.

### c)
**Find:** the free-body diagram of the cart when $F = 1.20\,\text{N}$, and its connection with the model of part b
**Principle:** The forces on the cart come from the Earth (weight), the track (normal force and friction) and the string (pull). The string is horizontal, so vertically only the weight and the normal force act, and they cancel each other.
**Model answer:** The cart is drawn as a rectangle. The weight $\overline{G}$ from the centre downwards and the normal force $\overline{N}$ from the bottom surface upwards, equally long. The pull of the string $\overline{T}$ starts from the point of attachment and points forwards, and friction $\overline{F}_\mu$ from the rear corner of the bottom surface backwards, about a fifth of the pull. The acceleration is marked separately next to the diagram. The horizontal forces are drawn to a scale of their own, because they are much smaller than the weight.
```voimakuvio
pinta 0
G 8,35
N 8,35
T 1,20 0
F_mu 0,24 vasen
a oikea
```
The horizontal equation of motion from the diagram is $T - F_\mu = ma$, the same as the equation of the line in part b when $T = F$. The net force in the diagram, $1.20\,\text{N} - 0.24\,\text{N} = 0.96\,\text{N}$, gives the acceleration $0.96\,\text{N} : 0.851\,\text{kg} \approx 1.13\,\text{m/s}^2$, which is close to the measured $1.14\,\text{m/s}^2$.

### d)
**Given:** from part b $m = 0.851\,\text{kg}$ and $F_\mu = 0.238\,\text{N}$; extra mass $0.500\,\text{kg}$; $g = 9.81\,\text{m/s}^2$
**Find:** the coefficient $\mu = \tfrac{F_\mu}{N}$ and the change of the line with the extra mass
**Principle:** The string is horizontal, so vertically only the weight and the normal force act, and $N = mg$ (chapter *Weight, friction and the inclined plane*). In the model the friction is proportional to the normal force.
**Formula:** $\mu = \dfrac{F_\mu}{N} = \dfrac{F_\mu}{mg}$
**Conversions:** None needed, the quantities are in base units.
**Substitution:** $\mu = \dfrac{0.238\,\text{N}}{0.851\,\text{kg} \cdot 9.81\,\text{m/s}^2} = \dfrac{0.238\,\text{N}}{8.35\,\text{N}} = 0.0285$
**Answer:** $\mu \approx 0.029$, two significant figures like $F_\mu$; the coefficient has no unit. With the extra mass the mass is $1.351\,\text{kg}$: the line becomes less steep, with the slope $\tfrac{1}{1.351\,\text{kg}} \approx 0.74\,\tfrac{1}{\text{kg}}$, and the intercept moves to the right, to $0.029 \cdot 1.351\,\text{kg} \cdot 9.81\,\text{m/s}^2 \approx 0.38\,\text{N}$.
**Reasonableness:** The rolling resistance of a cart on wheels is much smaller than the friction on a sliding object, whose coefficient is typically $0.2\text{–}0.6$, so $0.03$ is plausible. The prediction is based on a model in which friction does not depend on the speed; it is worth checking by repeating the measurement with the extra mass.

### Yleisiä virheitä
- The line is forced through the origin, so the slope and the mass come out wrong and the friction is not found.
- The slope is read from two adjacent measured points and not from the fitted line.
- The slope itself ($1.18\,\text{kg}$) is taken as the mass, although the slope is the reciprocal of the mass.
- In part c the weight of the hanging masses is drawn on the cart in the free-body diagram, although it is the string that pulls the cart.

### Hyväksytään myös
- In part b the slope of a line fitted by eye $1.14\text{–}1.22\,\tfrac{1}{\text{kg}}$, that is, the mass $0.82\text{–}0.88\,\text{kg}$, and the intercept $0.21\text{–}0.27\,\text{N}$; in part d the $\mu \approx 0.025\text{–}0.032$ calculated from them.
- A straight-line fit with a calculator or a spreadsheet ($a = 1.175\,\tfrac{1}{\text{kg}} \cdot F - 0.281\,\text{m/s}^2$).

## fy9-voimat-s4

### a)
**Find:** which force accelerates a walker forwards and why setting off is hard on glare ice
**Principle:** The state of motion of an object is changed only by the external forces acting on it (Newton's second law). Force and counterforce act on different objects (third law). Static friction is at most $\mu_0 N$.
**Model answer:** When Ella takes a step, her foot pushes the ground backwards. By the third law the ground pushes the foot forwards with a force of the same magnitude. This force is the static friction of the ground: the foot tends to slide backwards relative to the ground, and friction prevents it. It is the only horizontal external force, so it is exactly this force that accelerates Ella forwards. Ella's muscles exert internal forces, and they alone cannot change the state of motion of the whole body. On glare ice the coefficient of static friction is small, so the upper limit of friction $\mu_0 N$ is small. If the foot pushes backwards harder than friction can resist, the foot slides. That is why the largest possible acceleration stays small, and on ice people walk with short steps, placing the foot almost vertically.

### b)
**Find:** whether the claim "the engine pushes the car forwards" holds
**Principle:** The motion of the car is changed only by the external forces acting on the car. The engine is part of the car, so its forces on the wheels and the body are internal forces that cancel each other (third law).
**Model answer:** The claim is only partly right. The engine turns the front wheels, but it cannot by itself push the whole car, because it is inside the car. The turning tyre tends to slide backwards relative to the road surface, and the static friction of the road opposes this sliding by pointing forwards. This force of the road on the driving wheels is the external force that accelerates the car. That is why a car cannot set off on glare ice even if the engine runs at full power: the wheels just spin, because the friction is not enough.

### c)
**Find:** the free-body diagram of an accelerating car when air resistance and rolling resistance are taken into account
**Principle:** The forces on the car come from the Earth (weight), the road (normal force, static friction on the driving wheels and rolling resistance) and the air (air resistance). The car accelerates, so the net force points forwards.
**Model answer:** The car is drawn as a rectangle. The weight $\overline{G}$ from the centre downwards and the normal force $\overline{N}$ from the bottom surface upwards, equally long. The static friction of the road on the driving wheels $\overline{F}_\mu$ starts from the front corner of the bottom surface and points forwards. Rolling resistance $\overline{F}_\text{r}$ and air resistance $\overline{F}_\text{v}$ point backwards. The friction pointing forwards is larger than the resistive forces, because the car accelerates. The velocity and the acceleration are marked next to the diagram. The magnitudes are illustrative, and the horizontal forces are drawn to a scale of their own. The normal force may also be split into the normal forces on the front and rear wheels, $\overline{N}_1$ and $\overline{N}_2$.
```voimakuvio
pinta 0
G 100
N 100
F_mu 30 oikea
F_r 6 vasen @vasen
F_v 10 vasen
a oikea
v oikea
```

### d)
**Find:** the largest acceleration the road can give on asphalt and on ice, and why it is smaller for a front-wheel-drive car
**Principle:** The accelerating force is the static friction of the road, which is at most $\mu_0 N$. If all the wheels drive, the normal force is the weight of the whole car, $N = mg$.
**Model answer:** The largest accelerating force is $\mu_0 mg$, so $ma_\text{max} = \mu_0 mg$ and $a_\text{max} = \mu_0 g$; the mass cancels. On asphalt $a_\text{max} \approx 0.8 \cdot 9.81\,\text{m/s}^2 \approx 8\,\text{m/s}^2$ and on ice $0.1 \cdot 9.81\,\text{m/s}^2 \approx 1\,\text{m/s}^2$, when the resistive forces are ignored. In a front-wheel-drive car the static friction pushing forwards acts only on the driving front wheels, and their normal force is only part of the weight of the car, for example about half. Then the largest accelerating force is $\mu_0 N_\text{etu} < \mu_0 mg$ (etu = front), and the largest acceleration is smaller. On ice a front-wheel-drive car can therefore accelerate at less than $1\,\text{m/s}^2$ at most.

### Yleisiä virheitä
- The muscles or the engine "push" the walker or the car, that is, an internal force is presented as an external one.
- Force and counterforce (the foot pushes the ground, the ground pushes the foot) are drawn in the same free-body diagram.
- Friction is always drawn against the motion, also on the driving wheels.
- In part d the acceleration is calculated as $\mu_0 N$ without dividing by the mass, or ice and asphalt are compared without numbers.

## fy9-voimat-s5

### a)
**Given:** limiting angles $22^\circ$, $24^\circ$, $21^\circ$, $23^\circ$ and $33^\circ$; in measurement 5 the book was lifted with a jerk
**Find:** the coefficient of static friction $\mu_0$ and its uncertainty
**Principle:** At the limiting angle the component of the weight along the cover is as large as the largest value of static friction, and the normal force is the perpendicular component of the weight (chapter *Weight, friction and the inclined plane*). Measurement 5 is left out, because a gross error is recorded in the report: a quick lift momentarily presses the cover against the phone, so the normal force and the upper limit of static friction grow for a moment, and the angle is read too late. So $33^\circ$ is not the limit of sliding. A result would not be removed only because it differs from the others.
**Formula:** $mg\sin\alpha_0 = \mu_0 mg\cos\alpha_0$, so $\mu_0 = \tan\alpha_\text{ka}$, where $\alpha_\text{ka}$ is the mean of the limiting angles
**Conversions:** None needed. The angles are in degrees, and the coefficient has no unit.
**Substitution:** $\alpha_\text{ka} = \dfrac{22^\circ + 24^\circ + 21^\circ + 23^\circ}{4} = 22.5^\circ$ and $\mu_0 = \tan 22.5^\circ = 0.414$. Limits of the spread: $\tan 21^\circ = 0.384$ and $\tan 24^\circ = 0.445$
**Answer:** $\mu_0 \approx 0.41 \pm 0.03$, two significant figures, because the angles are read to the nearest degree and their spread is about $\pm 1.5^\circ$. The uncertainty is half the range of the results ($0.384\text{–}0.445$), which is the simple estimate chosen here.
**Reasonableness:** Silicone is known to be a grippy material, so a coefficient of $0.4$ is plausible. According to the measurements the limiting angle is about $22^\circ$, and $\tan 22.5^\circ \approx 0.41$ is consistent with it. The report's value $0.54$ would correspond to a limiting angle of $28^\circ$, which no careful measurement gave.

### b)
**Find:** the errors and shortcomings of the report's method and conclusion
**Principle:** A reliable result requires the correct model, a justified treatment of all the measurements, an estimate of the uncertainty and a conclusion that does not reach beyond the data.
**Model answer:** *Model.* The formula $\mu_0 = \sin\alpha_0$ is wrong. At the limit of sliding $mg\sin\alpha_0 = \mu_0 mg\cos\alpha_0$, so $\mu_0 = \tan\alpha_0$.

*Treatment of the results.* The group chose the largest angle, although that is exactly the measurement with a recorded gross error. The correct way is to calculate the mean of the careful measurements and say why measurement 5 was left out. The report has no uncertainty, although the angles vary from $21^\circ$ to $24^\circ$.

*Method.* Lifting by hand is not steady, and reading the angle exactly at the moment of sliding is difficult. Filming is good, but the protractor should be fixed to the book, and the book should be lifted slowly and steadily, for example with a screw or a pile of books.

*Conclusion.* The result applies only to this case and this book cover, not to all surfaces. Moreover, with the correct formula the limiting angle is about $22^\circ$, not $33^\circ$: the phone starts to slide already at an angle of about $22^\circ$.

### c)
**Find:** an experiment to determine the coefficient of kinetic friction for the same surfaces
**Principle:** Kinetic friction acts on a sliding object, and its magnitude is found from Newton's laws when either the pull at a constant velocity or the acceleration on a slope is measured.
**Model answer:** *Method 1, pulling.* The book lies on a horizontal table, and a string and a force sensor (or a spring balance) are attached to the phone. The phone is pulled horizontally at a constant velocity, so the pull equals the kinetic friction and the normal force equals the weight: $\mu = \dfrac{F}{mg}$. The mass of the phone is weighed on a scale. The mass is changed by adding masses on top of the phone, and the slope of the line through the origin fitted to the $(N, F_\mu)$ points is $\mu$.

*Method 2, acceleration.* The cover is tilted steeper than the limiting angle, for example to $30^\circ$, and the phone is released to slide from rest. The acceleration is measured from a video or with the phone's own acceleration sensor. From the free-body diagram $\mu = \dfrac{g\sin\alpha - a}{g\cos\alpha}$.

*Reliability.* Each measurement is repeated several times, and the mean and the spread of the results are calculated. The surfaces are cleaned in the same way every time. When pulling, the velocity must be constant, which shows as a steady reading of the sensor.

### Yleisiä virheitä
- Measurement 5 is removed only because it differs from the others, or it is included in the mean although a gross error is recorded.
- The coefficient is calculated with the sine or the cosine instead of the tangent.
- The coefficient is given a unit.
- In part c the pull is not made at a constant velocity, so the pull is not equal to the friction, or kinetic friction is measured from the limiting angle, which gives static friction.

### Hyväksytään myös
- In part a the tangent of each angle separately and their mean ($0.415$).
- The standard error of the mean as the uncertainty, when it is calculated and named correctly.

## fy9-voimat-s6

### a)
**Given:** length of the slope $L = 40\,\text{m}$, angle of inclination $\alpha = 12^\circ$, coefficient of kinetic friction $\mu = 0.080$, initial velocity $0$, $g = 9.81\,\text{m/s}^2$; air resistance is left out
**Find:** the speed $v$ at the bottom of the slope
**Principle:** The forces on the rider are the weight, the normal force of the slope and kinetic friction up the slope. The forces are constant, so the acceleration is constant (chapter *Weight, friction and the inclined plane*), and the equations of uniformly accelerated motion apply (chapter *Acceleration and uniformly accelerated motion*).
**Free-body diagram:** The rider as a rectangle parallel to the slope, the $x$ axis down the slope. The weight $\overline{G}$ from the centre straight down, the normal force $\overline{N}$ perpendicular to the slope, outwards, and kinetic friction $\overline{F}_\mu$ from the upper corner of the bottom surface up the slope. The components of the weight with dashed lines.
```voimakuvio
pinta -12
G 100
N 97,81
F_mu 7,82 ylös
a alas
akselit -12
komponentit G
```
**Formula:** $y$: $N = mg\cos\alpha$; $x$: $mg\sin\alpha - \mu mg\cos\alpha = ma_1$, so $a_1 = g(\sin\alpha - \mu\cos\alpha)$. Starting from rest, $v^2 = 2a_1 L$, so $v = \sqrt{2gL(\sin\alpha - \mu\cos\alpha)}$
**Conversions:** None needed, the quantities are in base units.
**Substitution:** $a_1 = 9.81\,\text{m/s}^2 \cdot (\sin 12^\circ - 0.080 \cdot \cos 12^\circ) = 9.81\,\text{m/s}^2 \cdot (0.2079 - 0.0783) = 1.272\,\text{m/s}^2$ and $v = \sqrt{2 \cdot 1.272\,\text{m/s}^2 \cdot 40\,\text{m}} = \sqrt{101.76\,\text{m}^2/\text{s}^2} = 10.09\,\text{m/s}$
**Answer:** $v \approx 10\,\text{m/s}$, two significant figures like the length of the slope $40\,\text{m}$.
**Reasonableness:** $10.09\,\text{m/s} = 10.09 \cdot 3.6\,\text{km/h} \approx 36\,\text{km/h}$, fast for a sliding mat but possible. The ride takes $t = v : a_1 \approx 7.9\,\text{s}$. Without friction the speed would be $\sqrt{2gL\sin\alpha} \approx 12.8\,\text{m/s}$, so friction reduces it clearly.

### b)
**Given:** from part a $v = 10.09\,\text{m/s}$, $\mu = 0.080$, final velocity $0$, $g = 9.81\,\text{m/s}^2$
**Find:** the sliding distance $s_2$ on the field
**Principle:** The transition between the slope and the field is gentle, so the initial speed on the field is the speed of part a. On the horizontal field the normal force equals the weight, and the only horizontal force is kinetic friction backwards. The deceleration is constant, so the equations of uniformly accelerated motion apply.
**Free-body diagram:** The rider as a rectangle: the weight $\overline{G}$ down, the normal force $\overline{N}$ up and kinetic friction $\overline{F}_\mu$ backwards. The acceleration points backwards and the velocity forwards.
```voimakuvio
pinta 0
G 100
N 100
F_mu 8 vasen
a vasen
v oikea
```
**Formula:** $-\mu mg = ma_2$, so $a_2 = -\mu g$. From $0 - v^2 = 2a_2 s_2$ we get $s_2 = \dfrac{v^2}{2\mu g}$
**Conversions:** None needed, the quantities are in base units.
**Substitution:** $s_2 = \dfrac{101.76\,\text{m}^2/\text{s}^2}{2 \cdot 0.080 \cdot 9.81\,\text{m/s}^2} = \dfrac{101.76\,\text{m}^2/\text{s}^2}{1.5696\,\text{m/s}^2} = 64.83\,\text{m}$
**Answer:** $s_2 \approx 65\,\text{m}$, two significant figures like the length of the slope and the coefficient of friction.
**Reasonableness:** On the field the deceleration $0.785\,\text{m/s}^2$ is smaller than the acceleration on the slope $1.272\,\text{m/s}^2$, so the stopping distance is longer than the slope in the same ratio: $40\,\text{m} \cdot 1.272 : 0.785 \approx 65\,\text{m}$. The distance is long but possible on packed snow.

### c)
**Find:** whether the heavy father slides further than the light children, in the model and when air resistance is taken into account
**Principle:** In the model all the forces are proportional to the mass, so the mass cancels from the equations of motion. Air resistance depends on the speed and on the size and position of the rider, but not on the mass (chapter *Air resistance and falling through air*).
**Model answer:** In the model of parts a and b, $a_1 = g(\sin\alpha - \mu\cos\alpha)$ and $a_2 = -\mu g$, so the mass affects neither the speed nor the sliding distance: the father and the children stop at the same place. In reality air resistance $F_\text{v}$ slows everyone down further. It changes the rider's acceleration by $F_\text{v} : m$. The father is bigger than a child, so at the same speed his air resistance is a little larger, but his mass is much larger, so the air resistance is a smaller part of his weight. The father's deceleration therefore grows less, and he probably slides further. So the claim may hold, but the reason is air resistance and not that a heavy rider would press the sliding mat forwards. The position, the bottom of the sliding mat and the spot on the snow also affect the result.

### Yleisiä virheitä
- On the slope the friction is taken as $\mu mg$, although $N = mg\cos\alpha$.
- On the field the acceleration of the slope is used, or the speed is calculated with $v = a t$ without the time.
- Friction on the slope is forgotten, so the speed comes out too large.
- In part c it is claimed that by the model a heavy rider slides further because the weight is larger.

### Hyväksytään myös
- A solution of parts a and b with work and energy, when the results are the same ($v^2 = 2gL(\sin\alpha - \mu\cos\alpha)$ and $\mu mg s_2 = \tfrac{1}{2}mv^2$).
