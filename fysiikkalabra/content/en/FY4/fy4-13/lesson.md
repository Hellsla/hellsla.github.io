# Equation of motion for connected bodies

> **Why** does a mass hanging over the edge of a table fall more slowly than a freely falling object when it pulls a cart along the table with a string?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a physics classroom table. On the table is a cart carrying two metal masses. A string tied to the cart passes over a pulley at the edge of the table, and a single metal mass hangs from the other end of the string. A measuring scale and a stopwatch lie on the table, and a student stands beside it." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-13-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
Often two bodies move together because a string joins them. When the string is taut and does not stretch, the bodies travel the same distance in the same time, so their accelerations have the same magnitude $a$. The string passes a force from one body to the other: it pulls each body toward itself. In this chapter the string is light and inextensible, the pulley is light and frictionless, and friction on the table and air resistance are neglected.

Connected bodies are treated one at a time. Each gets its own free-body diagram that shows only the forces acting on it, and each gets its own equation of motion. In the figure, the cart is acted on by its weight $\overline{G}_1$, the normal force $\overline{N}$ from the table and the tension $\overline{T}_1$ in the string. The hanging mass is acted on by its weight $\overline{G}_2$ and the tension $\overline{T}_2$ in the string.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Two bodies and their free-body diagrams. On the left, the situation: a cart on a table, and a string tied to it passes over a pulley at the table&#x27;s edge to a hanging mass. Above the cart are thin arrows: a blue velocity to the right and a shorter orange acceleration to the right. Top right, the free-body diagram of the cart, drawn as a rectangle: weight G1 down from the centre, the normal force N from the table up from the bottom surface and as long as the weight, and the tension T1 in the string to the right from the right edge. Bottom right, the free-body diagram of the hanging mass: weight G2 down from the centre and the tension T2 in the string up from the top surface. The arrow T2 is shorter than G2, and the arrows T1 and T2 are equally long." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-13-tilanne.webp" x="1.2" y="0" width="597" height="345.8" preserveAspectRatio="none"/>
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="210.8" y="234.8" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <foreignObject x="312" y="7.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: cart}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: mass}$</div></foreignObject>
  <foreignObject x="439.5" y="148.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <foreignObject x="379.5" y="56.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="499" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <foreignObject x="439.5" y="293" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <foreignObject x="439.5" y="234" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

The string pulls the cart with the force $\overline{T}_1$ and the hanging mass with the force $\overline{T}_2$. They act on different bodies, so they appear in different free-body diagrams. A light string and a frictionless pulley only pass the force on and turn its direction, so the magnitudes are equal: $T_1 = T_2 = T$. The forces $\overline{T}_1$ and $\overline{T}_2$ are nevertheless not an action–reaction pair. When the string pulls the cart, the cart pulls the string back with an equally large force, and that force acts on the string and is not in the cart's free-body diagram.

```pysahdy
The string pulls the cart with the force $\overline{T}_1$ and the hanging mass with the force $\overline{T}_2$. Why are these two forces not a force and its reaction?
---
They belong to two different interactions: string and cart, and string and hanging mass. The reaction to $\overline{T}_1$ is the force with which the cart pulls the string.
```

<figure class="unit-photo"><img src="pics/fy4/inclined-plane-apparatus.webp" alt="An old inclined plane apparatus: a small roller on a sloping bar and a hanging weight are connected by a string over a pulley."><figcaption>An inclined plane teaching apparatus from the early 20th century in the school museum of Bremerhaven, Germany. A roller on the incline and a hanging weight are connected by a string that runs over a pulley.</figcaption></figure>

When the hanging mass accelerates downward, the tension in the string is smaller than its weight. The acceleration is downward, so the net force on the mass points down and $G_2 > T$. If $T$ were equal to $G_2$, the net force on the mass would be zero and it would not start to move. The mass therefore descends more slowly than a freely falling object: the acceleration $a = \tfrac{m_2 g}{m_1 + m_2}$ is smaller than $g$, because the weight of the hanging mass also accelerates the cart.

```pysahdy
The mass of the cart increases while the hanging mass stays the same. How does the acceleration of the hanging mass change, and why?
---
It decreases. The same weight $m_2 g$ now accelerates a larger total mass $m_1 + m_2$.
```

## Formula: Equations of motion for connected bodies
Each body gets its own equation of motion $\Sigma F = ma$. The positive direction is chosen separately for each body along its acceleration: to the right for the cart and down for the hanging mass. Because the string does not stretch, both bodies have the same acceleration magnitude $a$. The equations of the cart and the hanging mass are
```latex
\begin{aligned}
T &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
where $m_1$ is the mass of the cart (kg), $m_2$ the mass of the hanging mass (kg), $T$ the tension in the string (N), $a$ the acceleration (m/s²) and $g = 9.81\,\text{m/s}^2$. There are two unknowns, $a$ and $T$, and two equations.

When the equations are added side by side, $T$ cancels, because the tension in the string is an internal force between the bodies. This gives the acceleration and then the tension:
```latex
\begin{aligned}
a &= \frac{m_2}{m_1 + m_2}\,g \\
T &= m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
The tension is always smaller than the weight $m_2 g$ of the hanging mass, because $\tfrac{m_1}{m_1 + m_2} < 1$. The heavier the cart is compared with the hanging mass, the less the bodies accelerate and the closer $T$ is to the weight $m_2 g$.

### Two hanging bodies
When a body hangs at each end of the string, the heavier one ($m_2$) goes down and the lighter one ($m_1$) goes up. The positive direction is chosen along the motion: up for the lighter body and down for the heavier one. Then
```latex
\begin{aligned}
T - m_1 g &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
```latex
\begin{aligned}
a &= \frac{m_2 - m_1}{m_1 + m_2}\,g \\
T &= \frac{2 m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
where $m_2 > m_1$. The tension lies between the weights $m_1 g$ and $m_2 g$ of the bodies. If the masses are equal, $a = 0$ and $T = mg$.

<svg data-fig="atwood" viewBox="0 0 600 410" role="img" aria-label="Two hanging bodies and their free-body diagrams. On the left, the situation: a string passes over a pulley hanging from the ceiling, with a lighter body on its left end and a heavier one on its right end. Beside the lighter body is an orange arrow up and beside the heavier one an equally long orange arrow down: the acceleration has the same magnitude. Top right, the free-body diagram of the lighter body, drawn as a rectangle: tension T1 up from the top surface and weight G1 down from the centre, with T1 longer than G1. Bottom right, the free-body diagram of the heavier body: T2 up from the top surface and G2 down from the centre, with G2 longer than T2. The arrows T1 and T2 are equally long." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-13-atwood.webp" x="-1.3" y="-1.3" width="603" height="418.3" preserveAspectRatio="none"/>
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <foreignObject x="21.5" y="173.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="217.5" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="91.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="135.5" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <foreignObject x="312" y="7.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: light}$</div></foreignObject>
  <foreignObject x="312" y="191.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: heavy}$</div></foreignObject>
  <foreignObject x="439.5" y="156.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <foreignObject x="439.5" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <foreignObject x="545.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="439.5" y="382" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <foreignObject x="439.5" y="228.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
  <foreignObject x="545.5" y="319.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

### Method for connected bodies
1. **Draw a free-body diagram** for each body. The string pulls each body toward itself, and each body has its own tension arrow.
2. **Choose the positive direction** for each body along its acceleration. If the actual direction of the acceleration is not known, the positive direction may be assumed, as long as the directions of the bodies fit together along the string. If the solution gives a negative acceleration, the actual acceleration is in the opposite direction. The direction of friction depends on the direction of motion, so with friction the assumed direction must be checked.
3. **Write the equation of motion** $\Sigma F = ma$ for each body separately. The acceleration $a$ and the tension magnitude $T$ are the same in both. If a body is also pulled by an external force $\overline{F}$, that force belongs only in the free-body diagram and equation of motion of the body being pulled.
4. **Solve** the two equations: add them, so that $T$ cancels, or substitute the $T$ from one into the other.
5. **Check** the signs and compare: the tension is not equal to the weight of a hanging body when the bodies accelerate.

## Worked example
A cart of mass $1.5\,\text{kg}$ stands on a table. A string tied to it passes over a light pulley at the edge of the table, and a mass of $0.60\,\text{kg}$ hangs from the other end of the string. The cart is released from rest. Friction and air resistance are neglected, and the string is light and inextensible. What is the acceleration of the cart and what is the tension in the string?

<!-- vaihe -->

**Given and find.** $m_1 = 1.5\,\text{kg}$, $m_2 = 0.60\,\text{kg}$ and $g = 9.81\,\text{m/s}^2$. We want the acceleration $a$ and the tension $T$ in the string.

<!-- vaihe -->

**Principle.** The cart and the hanging mass are two bodies, so each gets its own equation of motion. The string does not stretch, so the accelerations of the bodies have the same magnitude $a$. The string is light and the pulley is light and frictionless, so the string pulls both bodies with the same force $T$. There is no friction, so in the horizontal direction only the string acts on the cart.

<!-- vaihe -->

**Free-body diagram.** Each body has its own free-body diagram. The positive direction is to the right for the cart and down for the hanging mass. The cart does not accelerate vertically, so $N = G_1$. In the horizontal direction the cart is pulled only by $\overline{T}_1$. The hanging mass is acted on by $\overline{G}_2$ downward and $\overline{T}_2$ upward.

<svg data-fig="esimerkki" viewBox="0 0 600 340" role="img" aria-label="The cart and hanging mass of the example. On the left, the situation: the cart on the table, the string over a pulley to the hanging mass, and above the cart a blue velocity and an orange acceleration to the right. Top right, the free-body diagram of the cart: weight G1 down, the equally long normal force N up and the tension T1 to the right. Bottom right, the free-body diagram of the hanging mass: weight G2 down and the shorter tension T2 up. The arrows T1 and T2 are equally long." style="max-width:100%;font-size:24px">
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <rect x="20" y="176" width="214" height="12" rx="2" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="28" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="190" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="10" y1="296" x2="290" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="244" cy="164" r="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="244" cy="164" r="7" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="244" cy="164" r="2.5" fill="#1f2933"/>
  <rect x="226" y="172" width="12" height="10" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="70" y="146" width="60" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="83" cy="169" r="7" fill="#1f2933"/>
  <circle cx="117" cy="169" r="7" fill="#1f2933"/>
  <circle cx="83" cy="169" r="3" fill="#c4ccd4"/>
  <circle cx="117" cy="169" r="3" fill="#c4ccd4"/>
  <rect x="82" y="132" width="36" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M130,156 H244 A12,12 0 0 1 256,164 V236" fill="none" stroke="#b8622d" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="244" y="236" width="24" height="32" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="236" x2="256" y2="232" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="82" y1="124" x2="140" y2="124" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M129,130.5 L142,124 L129,117.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="82" y1="84" x2="120" y2="84" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M109,90.5 L122,84 L109,77.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="197.5" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="332" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="182" x2="590" y2="182" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: cart}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram: mass}$</div></foreignObject>
  <rect x="400" y="88" width="80" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="108" x2="440" y2="157" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,174 L432,156 L448,156 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="155.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="418" y1="128" x2="418" y2="79" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M418,62 L426,80 L410,80 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="480" y1="102" x2="482" y2="102" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M499,102 L481,110 L481,94 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="498.5" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <rect x="420" y="266" width="40" height="20" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="276" x2="440" y2="285.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,302.5 L432,284.5 L448,284.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="290" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="266" x2="440" y2="264" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,247 L448,265 L432,265 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="234.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Rearranged formula.** The two equations of motion are read from the diagrams and solved:
```latex
\begin{aligned}
&T = m_1 a \\
&m_2 g - T = m_2 a \\
&m_2 g = (m_1 + m_2) a \\
&a = \frac{m_2 g}{m_1 + m_2} \\
&T = m_1 a
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: the masses are in kilograms and $\tfrac{\text{kg} \cdot \text{m/s}^2}{\text{kg}} = \text{m/s}^2$.

<!-- vaihe -->

**Substitution.** The numerical values are substituted with their units:
```latex
\begin{aligned}
&a = \frac{m_2 g}{m_1 + m_2} \\
&\phantom{a} = \frac{0.60\,\text{kg} \cdot 9.81\,\text{m/s}^2}{1.5\,\text{kg} + 0.60\,\text{kg}} \\
&\phantom{a} \approx 2.80\,\text{m/s}^2 \\[4pt]
&T = m_1 a = 1.5\,\text{kg} \cdot 2.803\,\text{m/s}^2 \\
&\phantom{T} \approx 4.20\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration of the cart is $a \approx 2.8\,\text{m/s}^2$ and the tension in the string is $T \approx 4.2\,\text{N}$, with two significant figures like the masses $1.5\,\text{kg}$ and $0.60\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** The weight of the hanging mass is $m_2 g \approx 5.9\,\text{N}$, and the tension $4.2\,\text{N}$ is smaller than that, as it should be. The net force on the hanging mass is $5.886\,\text{N} - 4.204\,\text{N} \approx 1.68\,\text{N}$, and this equals $m_2 a = 0.60\,\text{kg} \cdot 2.803\,\text{m/s}^2 \approx 1.68\,\text{N}$. The acceleration is smaller than $g$, because the hanging mass also accelerates the cart. Without the cart, the mass would fall with acceleration $g$.

## Common misconception
People often think that the cart is pulled by the weight of the hanging mass, so that the tension would be $m_2 g$. The cart is pulled by the string, however, and the force of the string is $T$. Only when the bodies do not accelerate, for example when the cart is held still, is $T = m_2 g$. When the hanging mass descends with increasing speed, its net force $G_2 - T = m_2 a$ must point down, so $T < m_2 g$.

Another mistake is to treat the forces $\overline{T}_1$ and $\overline{T}_2$ as an action–reaction pair. They act on different bodies but belong to different interactions: one to the string–cart pair and the other to the string–mass pair. They are equal because the string is light and the pulley is light and frictionless, not because they would be the forces of one interaction pair. A third mistake is to think that the heavier body accelerates more. Bodies at the ends of an inextensible string have the same acceleration magnitude.

## Summary
- Bodies connected by a string or over a pulley each have their own free-body diagram and their own equation of motion $\Sigma F = ma$, and the positive direction is chosen for each body along its acceleration, or assumed if the direction is not known: a negative solution means that the acceleration is in the opposite direction.
- A light, inextensible string and a light, frictionless pulley give the bodies the same acceleration magnitude $a$ and equal tensions $T_1 = T_2 = T$.
- For a cart and a hanging mass, $a = \frac{m_2}{m_1 + m_2}\,g$ and $T = \frac{m_1 m_2}{m_1 + m_2}\,g$. For two hanging bodies, $a = \frac{m_2 - m_1}{m_1 + m_2}\,g$ and $T = \frac{2 m_1 m_2}{m_1 + m_2}\,g$.
- The tension for an accelerating hanging body is not its weight: for the cart and the hanging mass $T < m_2 g$, and for two hanging bodies $T$ lies between the weights.
- The tensions $\overline{T}_1$ and $\overline{T}_2$ act on different bodies and are not an action–reaction pair.
