# Free-body diagrams and the combined effect of forces

> **Why** can a sled press on the snow differently when it is pulled upward at an angle by a rope than when it simply stands still?

## Key idea
Usually several forces act on an object at the same time. The Earth pulls it down, the surface supports it, a rope pulls and the ground resists the motion. Each force describes one interaction between the object and some other object. The motion is decided by the **combined effect** of these forces, the **net force** $\Sigma\mathbf{F}$, which is the vector sum of the forces. In the chapter *Newton's second law* you learn that the net force determines the acceleration: $\Sigma\mathbf{F} = m\mathbf{a}$.

To include every force and to keep anything extra out of the calculation, the forces are first drawn in a **free-body diagram**. It is a different picture from the **situation diagram**. The situation diagram shows the whole situation: the surface, the rope, the person pulling and the direction of motion. The free-body diagram shows only the chosen object and the forces acting on it, as arrows. The direction of an arrow is the direction of the force, and the lengths of the arrows tell which force is larger.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Two pictures of the same situation. On the left the situation diagram: a box is pulled along the floor by a rope that rises obliquely, and above the box a thin blue arrow shows the velocity to the right. On the right the free-body diagram: only the box and the forces acting on it as red arrows. The weight G points straight down from the centre, the normal force N from the floor points straight up from the bottom surface and is shorter than the weight, the tension T of the rope starts from the attachment point obliquely up and to the right, and the friction force from the floor points to the left from the bottom surface. The velocity is not drawn in the free-body diagram." style="max-width:100%;font-size:24px">
  <foreignObject x="46" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation diagram}$</div></foreignObject>
  <line x1="20" y1="200" x2="280" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="20" y1="200" x2="10" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="36" y1="200" x2="26" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="52" y1="200" x2="42" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="68" y1="200" x2="58" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="200" x2="74" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="200" x2="90" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="200" x2="106" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="132" y1="200" x2="122" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="200" x2="138" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164" y1="200" x2="154" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="200" x2="170" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="196" y1="200" x2="186" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="212" y1="200" x2="202" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="228" y1="200" x2="218" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="244" y1="200" x2="234" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="200" x2="250" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="200" x2="266" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="80" y="140" width="80" height="60" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="160" y1="160" x2="246.5" y2="110" stroke="#a97a35" stroke-width="3" stroke-linecap="round"/>
  <circle cx="246.5" cy="110" r="8" fill="#6b7480"/>
  <line x1="90" y1="110" x2="158" y2="110" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M147,116.5 L160,110 L147,103.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="172" y="91.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\mathbf{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="346" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <rect x="400" y="140" width="80" height="60" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="440" y1="170" x2="440" y2="266" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,283 L432,265 L448,265 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="450" y="264.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="460" y1="200" x2="460" y2="133" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M460,116 L468,134 L452,134 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="470" y="105.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="480" y1="160" x2="515" y2="140" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,131 L518.5,147.5 L510,133 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="540.5" y="105" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="418" y1="200" x2="400.5" y2="200" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M383.5,200 L401.5,192 L401.5,208 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="353" y="169.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
</svg>

In the figure, a box is pulled along by a rope that points obliquely upward. The force of the rope points both forward and upward. The upward part helps to hold the box up, so the floor does not have to support it as much as when the box stands still. That is why the normal force $N$ is smaller than the weight $G$. The velocity is not drawn in the free-body diagram, because velocity is not a force.

## Drawing a free-body diagram {Voimakuvion piirtäminen}
A free-body diagram is always drawn with the same eight steps. They are worth going through every time, even when the situation looks easy.

1. **Choose the object.** Decide whose forces you draw. Only forces that act **on this object** go into the diagram. Forces that the object itself exerts on others do not belong in it.
2. **Find the interactions.** List everything that acts on the object: the Earth (weight), every surface the object touches (normal force and friction), every rope (tension), a push or a pull, and air or water (drag and buoyancy). Every force has a cause outside the object. Motion alone does not cause a force.
3. **Draw the forces.** Draw one arrow for each force, starting from the object.
   - The weight $\mathbf{G}$ points straight down.
   - The normal force $\mathbf{N}$ is perpendicular to the contact surface and pushes the object away from the surface. It does not always point up: a ceiling pushes down and a wall pushes sideways.
   - The friction force $\mathbf{F}_\mu$ is parallel to the contact surface. Its direction comes from the direction in which the object slides, or tends to slide, relative to the surface. It does not always oppose the velocity.
   - The tension $\mathbf{T}$ acts along the rope and pulls the object toward the rope.
   - Air drag is drawn only when the situation and its assumptions call for it.
4. **Name the forces.** Give each force its own symbol. Two similar forces are told apart with subscripts, for example $\mathbf{T}_1$ and $\mathbf{T}_2$.
5. **Think about the magnitudes.** At rest and in uniform motion the net force is zero, so the arrows cancel each other. In accelerating motion the net force points in the direction of the acceleration, which is not always the direction of the velocity. Do not invent exact lengths if the data does not fix them.
6. **Only forces.** Velocity, acceleration and displacement are not forces. If they are needed, they are drawn beside the object in a different style. The net force is not one more force.
7. **Components are not new forces.** When a force is split into components, the components together replace the force in the calculation. They are drawn with a dashed line so that they are not mistaken for forces.
8. **Equation of motion.** Only now are the axes chosen and Newton's second law written component by component from the forces and signs of the diagram.

<svg data-fig="suunnat" viewBox="0 0 600 620" role="img" aria-label="Four small free-body diagrams. Top left: a box rests on a horizontal floor, with the weight G straight down from the centre and an equally long normal force N up from the bottom surface. Top right: a box is at rest on an inclined slope, with the weight G straight down, the normal force N perpendicular to the slope and the friction force up along the slope. Bottom left: a lamp hangs from a cord, with the weight G down and the tension T of the cord up along the cord. Bottom right: a helium balloon is pressed against the ceiling and is at rest. Beside it is the free-body diagram of the balloon as a point: buoyancy up, weight down and, next to it, the normal force N from the ceiling down, away from the ceiling surface. The buoyancy arrow is as long as the weight and normal force arrows together." style="max-width:100%;font-size:24px">
  <line x1="300" y1="10" x2="300" y2="610" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="10" y1="310" x2="590" y2="310" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="115" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{floor}$</div></foreignObject>
  <line x1="40" y1="200" x2="260" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="40" y1="200" x2="30" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="200" x2="46" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="72" y1="200" x2="62" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="88" y1="200" x2="78" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="200" x2="94" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="200" x2="110" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="136" y1="200" x2="126" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="152" y1="200" x2="142" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="168" y1="200" x2="158" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="184" y1="200" x2="174" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="200" x2="190" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="216" y1="200" x2="206" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="232" y1="200" x2="222" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="200" x2="238" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="112" y="140" width="76" height="60" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="150" y1="170" x2="150" y2="252" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,269 L142,251 L158,251 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="160" y="250.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="168" y1="200" x2="168" y2="118" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M168,101 L176,119 L160,119 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="178" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <foreignObject x="415" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{slope}$</div></foreignObject>
  <line x1="316" y1="262" x2="559" y2="148.5" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="316" y1="262" x2="306" y2="274" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330.5" y1="255" x2="320.5" y2="267" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345" y1="248.5" x2="335" y2="260.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359.5" y1="241.5" x2="349.5" y2="253.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="235" x2="364" y2="247" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="388.5" y1="228" x2="378.5" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="403" y1="221.5" x2="393" y2="233.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="417.5" y1="214.5" x2="407.5" y2="226.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432" y1="208" x2="422" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="446.5" y1="201" x2="436.5" y2="213" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="461" y1="194.5" x2="451" y2="206.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="475.5" y1="187.5" x2="465.5" y2="199.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="490" y1="181" x2="480" y2="193" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="504.5" y1="174" x2="494.5" y2="186" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="519" y1="167.5" x2="509" y2="179.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="533.5" y1="160.5" x2="523.5" y2="172.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="548" y1="154" x2="538" y2="166" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M401.2,222.3 L466.4,191.8 L441.1,137.5 L375.8,167.9 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="421" y1="180" x2="421" y2="262" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M421,279 L413,261 L429,261 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="431" y="268.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="421" y1="213" x2="390.5" y2="147" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M383,131.5 L398,144.5 L383.5,151.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="357" y="111" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="448.5" y1="200.5" x2="471" y2="190" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M486,182.5 L473.5,197.5 L466.5,183 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="473.5" y="190" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <foreignObject x="121" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamp}$</div></foreignObject>
  <line x1="70" y1="360" x2="230" y2="360" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="70" y1="360" x2="60" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="360" x2="76" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="102" y1="360" x2="92" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="118" y1="360" x2="108" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="134" y1="360" x2="124" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="360" x2="140" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="166" y1="360" x2="156" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="182" y1="360" x2="172" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="198" y1="360" x2="188" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="214" y1="360" x2="204" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="360" x2="150" y2="450" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M124,480 L176,480 L163,450 L137,450 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="150" y1="468" x2="150" y2="539" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,556 L142,538 L158,538 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="162" y="537.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="150" y1="450" x2="150" y2="379" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,362 L158,380 L142,380 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="162" y="367.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <foreignObject x="365" y="319.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{helium balloon}$</div></foreignObject>
  <line x1="316" y1="360" x2="430" y2="360" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="316" y1="360" x2="306" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332" y1="360" x2="322" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="348" y1="360" x2="338" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364" y1="360" x2="354" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="360" x2="370" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="396" y1="360" x2="386" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="412" y1="360" x2="402" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="372" cy="402" r="40" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="372" y1="442" x2="368" y2="520" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="505" cy="495" r="6" fill="#1f2933"/>
  <line x1="505" y1="495" x2="505" y2="412" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M505,395 L513,413 L497,413 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="528.5" y="392.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_\text{b}$</div></foreignObject>
  <line x1="513" y1="495" x2="513" y2="518" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M513,535 L505,517 L521,517 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="521" y="518.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="497" y1="495" x2="497" y2="538" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M497,555 L489,537 L505,537 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="467" y="532.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
</svg>

The figure shows four situations in which the directions of the forces often surprise people. On a slope the normal force is perpendicular to the slope, not vertical, and friction holds the box in place along the slope. On a helium balloon pressed against the ceiling the ceiling pushes downward.

A free-body diagram can be drawn in two ways, and both are correct. In the **body model** the object is drawn with its shape, and each force starts from its point of action: the weight from the centre, the normal force and friction from the contact surface, and the tension from where the rope is attached. In the **point model** the object is a point, and all forces start from it. The point model is enough when the rotation of the object does not matter. Follow the model that the task uses.

<svg data-fig="malli" viewBox="0 0 600 320" role="img" aria-label="Point-model free-body diagram of the same box as above: all four forces start from one point. The weight G points down, the normal force N points up and is shorter than the weight, the tension T of the rope points obliquely up and to the right, and the friction force points to the left. In the corner are the coordinate axes: x to the right and y up." style="max-width:100%;font-size:24px">
  <circle cx="300" cy="150" r="7" fill="#1f2933"/>
  <line x1="300" y1="150" x2="300" y2="246" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,263 L292,245 L308,245 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="310" y="244.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="300" y1="150" x2="300" y2="83" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,66 L308,84 L292,84 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="310" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="300" y1="150" x2="335" y2="130" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M350,121 L338.5,137.5 L330,123 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="360.5" y="95" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="300" y1="150" x2="282.5" y2="150" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M265.5,150 L283.5,142 L283.5,158 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="233" y="121.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <line x1="80" y1="270" x2="117" y2="270" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M126,270 L116,274.5 L116,265.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="80" y1="270" x2="80" y2="233" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M80,224 L84.5,234 L75.5,234 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="128" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="70" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

The marking instructions of the matriculation examinations give task-specific points for the free-body diagram. For example, in the spring 2025 helium-balloon task a missing, extra or wrongly directed force cost all the points of the diagram, and so did drawing velocity or acceleration as a force on the balloon. In the autumn 2025 examination a missing name cost one point. The exact scoring varies from task to task, but every examination requires the same things: all the forces, no invented forces, correct directions and unambiguous names.

## Formula: Equation of motion by components
Newton's second law concerns the net force:
```latex
\Sigma\mathbf{F} = m\mathbf{a}
```
where $\Sigma\mathbf{F}$ is the vector sum of the forces acting on the object (N), $m$ is the mass of the object (kg) and $\mathbf{a}$ is its acceleration (m/s²). When the forces are not along one line, two perpendicular axes are chosen and the law is written separately for each axis direction:
```latex
\begin{aligned}
\Sigma F_x &= m a_x \\
\Sigma F_y &= m a_y
\end{aligned}
```
where $\Sigma F_x$ and $\Sigma F_y$ are the sums of the components of the forces (N) and $a_x$ and $a_y$ are the components of the acceleration (m/s²). A component pointing along the axis is positive and one pointing against it is negative. It is wise to choose the axes so that one of them points in the direction of the acceleration.

The components of an oblique force $F$ come from a right triangle, when $\alpha$ is the angle between the force and the $x$-axis:
```latex
\begin{aligned}
F_x &= F\cos\alpha \\
F_y &= F\sin\alpha
\end{aligned}
```
where $F$ is the magnitude of the force (N), $F_x$ and $F_y$ are its components (N) and $\alpha$ is the angle. The components are not new forces. They replace the force $F$ in the calculation.

<svg data-fig="komponentit" viewBox="0 0 600 300" role="img" aria-label="The force F starts from a point obliquely up and to the right at an angle alpha to the horizontal. The components drawn with dashed lines: the horizontal F x along the x-axis and the vertical F y along the y-axis. The components and the force form a right triangle whose hypotenuse is F. Labels: F x is F times cosine alpha and F y is F times sine alpha." style="max-width:100%;font-size:24px">
  <line x1="110" y1="240" x2="260" y2="135" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M274,125.5 L263.5,142 L254.5,129 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="258" y="93" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}$</div></foreignObject>
  <line x1="110" y1="240" x2="272" y2="240" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M261,246.5 L274,240 L261,233.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="257.5" y="247.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{x}$</div></foreignObject>
  <line x1="110" y1="240" x2="110" y2="127.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M116.5,138.5 L110,125.5 L103.5,138.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="69.5" y="111" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{y}$</div></foreignObject>
  <line x1="274" y1="240" x2="274" y2="125.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="110" y1="125.5" x2="274" y2="125.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <path d="M162,240 A52,52 0 0 0 152.6,210.2" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="174" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="390" y="105.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_x = F\cos\alpha$</div></foreignObject>
  <foreignObject x="390" y="155.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_y = F\sin\alpha$</div></foreignObject>
</svg>

## Worked example
A sled of mass $12\,\text{kg}$ is pulled on horizontal snow by a rope that makes an angle of $35^\circ$ with the horizontal. The tension in the rope is $80\,\text{N}$ and the friction force from the snow is $30\,\text{N}$. What is the acceleration of the sled, and what is the normal force from the snow?

<!-- vaihe -->

**Given and find.** $m = 12\,\text{kg}$, $T = 80\,\text{N}$, $\alpha = 35^\circ$, $F_\mu = 30\,\text{N}$ and $g = 9.81\,\text{m/s}^2$. We want the acceleration $a$ and the normal force $N$.

<!-- vaihe -->

**Principle.** Choose the sled as the object. The Earth (weight), the snow (normal force and friction) and the rope (tension) act on it. Newton's second law is written in two directions: horizontally the sled accelerates, vertically it stays on the surface of the snow, so $a_y = 0$.

<!-- vaihe -->

**Free-body diagram.** The sled is drawn as a point. The axes are chosen so that $x$ points in the direction of motion and $y$ points up. The force of the rope is split into the components $T_x = T\cos\alpha$ and $T_y = T\sin\alpha$, drawn with dashed lines.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Free-body diagram of the sled as a point model. The weight G points down, the normal force N from the snow points up and is shorter than the weight, the tension T of the rope points obliquely up and to the right at an angle of 35 degrees with its components dashed, and the friction force from the snow points to the left. In the corner are the axes: x to the right, in the direction of motion, and y up." style="max-width:100%;font-size:24px">
  <circle cx="290" cy="180" r="7" fill="#1f2933"/>
  <line x1="290" y1="180" x2="290" y2="298.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,315.5 L282,297.5 L298,297.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="300" y="297" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="290" y1="180" x2="290" y2="114.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,97.5 L298,115.5 L282,115.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="302" y="89" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="290" y1="180" x2="351.5" y2="137" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M365.5,127 L355.5,144 L346,131 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="371.5" y="102.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="290" y1="180" x2="272.5" y2="180" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M255.5,180 L273.5,172 L273.5,188 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="223" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <line x1="290" y1="180" x2="363.5" y2="180" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M352.5,186.5 L365.5,180 L352.5,173.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="349" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}_{x}$</div></foreignObject>
  <line x1="290" y1="180" x2="290" y2="129" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M296.5,140 L290,127 L283.5,140" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="245.5" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}_{y}$</div></foreignObject>
  <path d="M330,180 A40,40 0 0 0 322.8,157.1" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="338" y="151.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$35^\circ$</div></foreignObject>
  <line x1="70" y1="320" x2="107" y2="320" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M116,320 L106,324.5 L106,315.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="70" y1="320" x2="70" y2="283" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M70,274 L74.5,284 L65.5,284 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="118" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="60" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Rearranged formula.** The equations of motion are read from the diagram, and the asked quantities are solved:
```latex
\begin{aligned}
&x\text{:}\ \ T\cos\alpha - F_\mu = m a \\
&y\text{:}\ \ N + T\sin\alpha - mg = 0 \\
&a = \frac{T\cos\alpha - F_\mu}{m} \\
&N = mg - T\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: all quantities are in SI units, and $\tfrac{\text{N}}{\text{kg}} = \tfrac{\text{m}}{\text{s}^2}$.

<!-- vaihe -->

**Substitution.** Substitute the values with their units:
```latex
\begin{aligned}
&a = \frac{T\cos\alpha - F_\mu}{m} \\
&\phantom{a} = \frac{80\,\text{N}\cdot\cos 35^\circ - 30\,\text{N}}{12\,\text{kg}} \\
&\phantom{a} \approx 2.96\,\text{m/s}^2 \\[4pt]
&N = mg - T\sin\alpha \\
&\phantom{N} = 12\,\text{kg}\cdot 9.81\,\text{m/s}^2 \\
&\quad\ - 80\,\text{N}\cdot\sin 35^\circ \\
&\phantom{N} \approx 71.8\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration is $a \approx 3.0\,\text{m/s}^2$ and the normal force is $N \approx 72\,\text{N}$, given with two significant figures like the data $80\,\text{N}$, $30\,\text{N}$ and $12\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** The weight of the sled is $mg \approx 118\,\text{N}$. The normal force $72\,\text{N}$ is smaller, because the vertical component of the rope force, $T_y \approx 46\,\text{N}$, supports part of the weight, and $72\,\text{N} + 46\,\text{N} \approx 118\,\text{N}$. Without friction the acceleration would be $65.5\,\text{N} : 12\,\text{kg} \approx 5.5\,\text{m/s}^2$, so friction reduces it, as it should.

## Common misconception
A moving object does not need a force in the direction of its motion. Only the weight, the normal force and friction act on a sliding box, and there is no "force of motion": there is no object that would cause it. Another common mistake is to think that the normal force is always equal to the weight. The normal force is exactly as large as the situation requires: in an oblique pull it is smaller than the weight, and in an oblique push or in an elevator accelerating upward it is larger. A third mistake is to draw the components as forces in addition to the force itself, which puts the same force into the calculation twice.

## Summary
- A free-body diagram contains only the chosen object and the forces acting on it. The situation diagram and the free-body diagram are different pictures.
- Every force has a cause: the Earth, a surface, a rope, a pusher or the air. Velocity and acceleration are not forces.
- The normal force is perpendicular to the surface, friction is parallel to the surface and tension is along the rope.
- The net force is the vector sum of the forces, and $\Sigma\mathbf{F} = m\mathbf{a}$ is written by components: $\Sigma F_x = m a_x$ and $\Sigma F_y = m a_y$.
- The components of an oblique force are $F\cos\alpha$ and $F\sin\alpha$. They replace the force in the calculation and are not new forces.
