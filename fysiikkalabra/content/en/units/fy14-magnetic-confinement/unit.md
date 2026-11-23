# Charged particles and magnetic confinement

> **Why** can an invisible magnetic field hold a fuel that would melt or vaporise any solid container?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a dark experimental hall seen from above at an angle. A large ring of orange coils surrounds a glowing pink ring of plasma. Thin green lines run round and round the ring, inside the coils, and a bright white track spirals tightly around one of the green lines as it follows the ring. Nothing touches the walls." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-magnetic-confinement-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## The magnetic force on a moving charge {Lorentz}

A magnetic field $\overline{B}$ pushes on a charge $q$ only when the charge moves. The force is called the magnetic part of the **Lorentz force**. In the formula below, $v$ is the speed and $\alpha$ is the angle between the velocity $\overline{v}$ and the field $\overline{B}$.
```latex
F = |q|\,v B \sin\alpha
```
A charge that moves along the field feels no force.

The force is always **perpendicular** both to $\overline{v}$ and to $\overline{B}$. For a positive charge, the right-hand rule gives its direction; a negative charge is pushed the opposite way. Because the force is perpendicular to the motion, it does no work: it changes the direction of the particle, not its speed.

<svg data-fig="lorentz" viewBox="0 0 600 380" role="img" aria-label="Diagram: a uniform magnetic field into the page, shown by a grid of green crossed circles. A positive particle moves anticlockwise on a circle of radius r. At the bottom of the circle its velocity arrow, blue, points to the right and the magnetic force arrow, red, points up to the centre. At the right-hand side of the circle the velocity points up and the force points left, again to the centre. The force is always perpendicular to the velocity." style="max-width:100%;font-size:24px">
  <circle cx="34" cy="160" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="28.5" y1="154.5" x2="39.5" y2="165.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="28.5" y1="165.5" x2="39.5" y2="154.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="34" cy="222" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="28.5" y1="216.5" x2="39.5" y2="227.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="28.5" y1="227.5" x2="39.5" y2="216.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="34" cy="284" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="28.5" y1="278.5" x2="39.5" y2="289.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="28.5" y1="289.5" x2="39.5" y2="278.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="34" cy="346" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="28.5" y1="340.5" x2="39.5" y2="351.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="28.5" y1="351.5" x2="39.5" y2="340.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="101" cy="160" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="95.5" y1="154.5" x2="106.5" y2="165.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="95.5" y1="165.5" x2="106.5" y2="154.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="101" cy="222" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="95.5" y1="216.5" x2="106.5" y2="227.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="95.5" y1="227.5" x2="106.5" y2="216.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="101" cy="284" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="95.5" y1="278.5" x2="106.5" y2="289.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="95.5" y1="289.5" x2="106.5" y2="278.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="101" cy="346" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="95.5" y1="340.5" x2="106.5" y2="351.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="95.5" y1="351.5" x2="106.5" y2="340.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="168" cy="346" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="162.5" y1="340.5" x2="173.5" y2="351.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="162.5" y1="351.5" x2="173.5" y2="340.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="235" cy="36" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="229.5" y1="30.5" x2="240.5" y2="41.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="229.5" y1="41.5" x2="240.5" y2="30.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="302" cy="36" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="296.5" y1="30.5" x2="307.5" y2="41.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="296.5" y1="41.5" x2="307.5" y2="30.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="369" cy="36" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="363.5" y1="30.5" x2="374.5" y2="41.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="363.5" y1="41.5" x2="374.5" y2="30.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="436" cy="36" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="430.5" y1="30.5" x2="441.5" y2="41.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="430.5" y1="41.5" x2="441.5" y2="30.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="503" cy="36" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="497.5" y1="30.5" x2="508.5" y2="41.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="497.5" y1="41.5" x2="508.5" y2="30.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="503" cy="98" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="497.5" y1="92.5" x2="508.5" y2="103.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="497.5" y1="103.5" x2="508.5" y2="92.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="503" cy="160" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="497.5" y1="154.5" x2="508.5" y2="165.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="497.5" y1="165.5" x2="508.5" y2="154.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="503" cy="222" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="497.5" y1="216.5" x2="508.5" y2="227.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="497.5" y1="227.5" x2="508.5" y2="216.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="503" cy="284" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="497.5" y1="278.5" x2="508.5" y2="289.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="497.5" y1="289.5" x2="508.5" y2="278.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="503" cy="346" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="497.5" y1="340.5" x2="508.5" y2="351.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="497.5" y1="351.5" x2="508.5" y2="340.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="570" cy="36" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="564.5" y1="30.5" x2="575.5" y2="41.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="564.5" y1="41.5" x2="575.5" y2="30.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="570" cy="98" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="564.5" y1="92.5" x2="575.5" y2="103.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="564.5" y1="103.5" x2="575.5" y2="92.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="570" cy="160" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="564.5" y1="154.5" x2="575.5" y2="165.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="564.5" y1="165.5" x2="575.5" y2="154.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="570" cy="222" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="564.5" y1="216.5" x2="575.5" y2="227.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="564.5" y1="227.5" x2="575.5" y2="216.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="570" cy="284" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="564.5" y1="278.5" x2="575.5" y2="289.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="564.5" y1="289.5" x2="575.5" y2="278.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="570" cy="346" r="8" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="564.5" y1="340.5" x2="575.5" y2="351.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="564.5" y1="351.5" x2="575.5" y2="340.5" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="300" cy="200" r="120" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-dasharray="8 7"/>
  <line x1="300" y1="200" x2="215" y2="115" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="236" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$r$</span></div></foreignObject>
  <circle cx="300" cy="200" r="4" fill="#1f2933"/>
  <line x1="300" y1="320" x2="389" y2="320" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M404,320 L388,327 L388,313 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="408" y="307.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{v}$</span></div></foreignObject>
  <line x1="300" y1="320" x2="300" y2="255" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,240 L307,256 L293,256 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="310" y="245.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <circle cx="300" cy="320" r="11" fill="#c2255c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="291" y="308" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#ffffff">$+$</div></foreignObject>
  <line x1="420" y1="200" x2="420" y2="111" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M420,96 L427,112 L413,112 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="438" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{v}$</span></div></foreignObject>
  <line x1="420" y1="200" x2="355" y2="200" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M340,200 L356,193 L356,207 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="343.5" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <circle cx="420" cy="200" r="11" fill="#c2255c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="411" y="188" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#ffffff">$+$</div></foreignObject>
  <path d="M251.5,66.5 A142,142 0 0 0 166.5,151.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M157.5,139.5 L166.5,155.5 L175.5,141.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="6" y="8" width="190" height="88" rx="8" fill="#ffffff" stroke="#c9c2b2" stroke-width="2"/>
  <circle cx="28" cy="32" r="9" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.2"/>
  <line x1="22" y1="26" x2="34" y2="38" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="22" y1="38" x2="34" y2="26" stroke="#2b8a3e" stroke-width="2.2" stroke-linecap="butt"/>
  <foreignObject x="44" y="17.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}\ \text{into}$</div></foreignObject>
  <foreignObject x="20" y="55.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{the page}$</div></foreignObject>
</svg>

```pysahdy
A proton moves exactly along a magnetic field line. What is the magnetic force on it?
---
Zero. The force is $F = |q|\,vB\sin\alpha$, and along the field $\alpha = 0$, so $\sin\alpha = 0$.
```

## Formula: Radius and period of the orbit

When $\overline{v}$ is perpendicular to a uniform $\overline{B}$, the magnetic force is a constant-size force towards a centre, so the particle moves on a **circle**. The magnetic force is the centripetal force:
```latex
\begin{aligned}
|q|\,v B &= \frac{m v^2}{r} \\[8pt]
r &= \frac{m v}{|q| B} \\[8pt]
T &= \frac{2 \pi r}{v} = \frac{2 \pi m}{|q| B}
\end{aligned}
```
The radius $r$ is called the **gyroradius**. A stronger field gives a smaller circle. The period $T$ does not depend on the speed: a faster particle runs on a larger circle in the same time.

## Along the field: helices and magnetic mirrors {Mirror}

Usually the velocity has a part along the field, $v_{\parallel} = v\cos\theta$, and a part across it, $v_{\perp} = v\sin\theta$. The angle $\theta$ is the **pitch angle**. The field does not affect $v_{\parallel}$, so the particle circles *around* a field line and slides *along* it: its path is a **helix**. The particle is tied to its field line, but it can run freely along it.

In a **magnetic mirror** the field is stronger at both ends. As a particle moves into the stronger field, more of its motion turns into circling and $v_{\parallel}$ shrinks. If $v_{\parallel}$ reaches zero, the particle turns back. The condition for this is below: $B_0$ is the field in the middle and $B_{\max}$ the field at the ends.

```latex
\sin^2\theta \geq \frac{B_0}{B_{\max}}
```
Particles with smaller pitch angles, inside the **loss cone**, escape through the ends.

<svg data-fig="mirror" viewBox="0 0 600 440" role="img" aria-label="Side view of a magnetic mirror. Green field lines run from left to right; they are spread out in the middle and squeezed together at both ends, where two coils make the field four times stronger. A particle path spirals around the axis, moving to the right, and turns back before the right-hand coil. In the middle, the particle&#x27;s velocity arrow, blue, is split into a part along the field, v parallel, and a part across it, v perpendicular; the angle between the velocity and the field is the pitch angle theta." style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-magnetic-confinement-mirror.webp" x="0" y="-1.2" width="600" height="445" preserveAspectRatio="none"/>
  <foreignObject x="527" y="191.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="33.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B_{\max}$</div></foreignObject>
  <foreignObject x="533.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B_{\max}$</div></foreignObject>
  <foreignObject x="283.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B_0$</div></foreignObject>
  <foreignObject x="327" y="119.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{turns back}$</div></foreignObject>
  <foreignObject x="310.5" y="317" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="261" y="345" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v_{\parallel}$</div></foreignObject>
  <foreignObject x="211.5" y="296" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v_{\perp}$</div></foreignObject>
  <foreignObject x="293" y="278.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="127.5" y="401.5" width="345" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B_{\max} = 4B_0\text{: reflected if } \sin^2\theta \geq B_0 / B_{\max}$</div></foreignObject>
</svg>

```pysahdy
Why does $v_{\parallel}$ shrink when a particle moves into a stronger field?
---
The magnetic force does no work, so the kinetic energy stays the same. More of the motion turns into circling around the field line, and less is left for sliding along it.
```

The Earth's magnetic field is a natural mirror: it traps charged particles in the radiation belts, where they bounce between the north and the south. Particles that do reach the upper air near the poles make the northern lights.

## Why a ring, and why it is still hard {Torus}

A straight field always has ends, and every particle with $v_{\parallel} \neq 0$ eventually leaks out. Bending the field into a ring, a **torus**, closes the field lines, so there are no ends.

<svg data-fig="torus" viewBox="0 0 600 300" role="img" aria-label="Two diagrams. Left: a straight tube with coils around it; green field lines run along it and out of both open ends, and particles spiralling along the field lines escape through the ends. Right: the same coils bent into a ring, seen from above; the green field lines go round and round and close on themselves, so there are no ends to escape through." style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-magnetic-confinement-torus.webp" x="12.3" y="0" width="588.2" height="302.7" preserveAspectRatio="none"/>
  <foreignObject x="8.5" y="269.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{open ends: particles leak}$</div></foreignObject>
  <foreignObject x="371" y="269.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{a ring: no ends}$</div></foreignObject>
</svg>

But in a ring the coils are closer together on the inside, so the field is **stronger near the centre and weaker on the outside**, and the field lines are curved. A circling particle then **drifts** slowly across the field: ions one way, electrons the other. The charges separate, an electric field forms, and the whole plasma drifts outward into the wall. The cure is to **twist** the field lines, which is the topic of the chapter *From Early Machines to Modern Reactors*.

## One particle is not a plasma {Collective}

The simulation follows one particle in a fixed field. A fusion plasma has about $10^{20}$ ions and as many electrons in every cubic metre. They collide, which lets them jump from one field line to another. Their currents change the magnetic field that holds them. Small waves and swirls, **turbulence**, carry heat out much faster than single-particle theory predicts. Large-scale **instabilities** can bend or break up the whole plasma: the kinks and wriggles of early pinch machines such as ZETA in 1958 are an example. Single-particle motion explains *why* magnetic confinement is possible; the collective behaviour of the plasma explains *why it is so difficult*.

## Worked example

In a tokamak with a magnetic field of $5.0\ \text{T}$, a deuteron (the nucleus of deuterium) moves at $1.0 \cdot 10^{6}\ \text{m/s}$ perpendicular to the field. Calculate the radius and the period of its circular motion. The mass of a deuteron is $3.344 \cdot 10^{-27}\ \text{kg}$ and its charge is $e = 1.602 \cdot 10^{-19}\ \text{C}$.

<!-- vaihe -->

**Given:** $m = 3.344 \cdot 10^{-27}\ \text{kg}$, $q = e = 1.602 \cdot 10^{-19}\ \text{C}$, $v = 1.0 \cdot 10^{6}\ \text{m/s}$, $B = 5.0\ \text{T}$, $\overline{v}$ perpendicular to $\overline{B}$. Asked: the radius $r$ and the period $T$.

<!-- vaihe -->

**Principle:** The magnetic force $|q|vB$ is perpendicular to the velocity, so it keeps the speed constant and acts as the centripetal force $mv^2/r$ of a circular motion.

<!-- vaihe -->

**Formula:** From $|q|vB = mv^2/r$:
```latex
\begin{aligned}
r &= \frac{m v}{|q| B} \\[8pt]
T &= \frac{2 \pi m}{|q| B}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** All quantities are in SI units. $1\ \text{T} = 1\ \text{kg}/(\text{C} \cdot \text{s})$, so $\text{kg} \cdot (\text{m/s}) : (\text{C} \cdot \text{T}) = \text{m}$.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
r &= \frac{3.344 \cdot 10^{-27}\ \text{kg}}{1.602 \cdot 10^{-19}\ \text{C} \cdot 5.0\ \text{T}} \\
&\quad \cdot 1.0 \cdot 10^{6}\ \text{m/s} \\
&= 4.17 \cdot 10^{-3}\ \text{m} \\[6pt]
T &= \frac{2 \pi \cdot 3.344 \cdot 10^{-27}\ \text{kg}}{1.602 \cdot 10^{-19}\ \text{C} \cdot 5.0\ \text{T}} \\
&= 2.62 \cdot 10^{-8}\ \text{s}
\end{aligned}
```

<!-- vaihe -->

**Answer:** $r \approx 4.2\ \text{mm}$ and $T \approx 26\ \text{ns}$. Two significant figures, as in the speed and the field.

<!-- vaihe -->

**Reasonableness:** The deuteron circles about 38 million times a second on a circle of only a few millimetres, tiny compared with a plasma about $2\ \text{m}$ across. Check with $T = 2\pi r / v$: $2\pi \cdot 4.17 \cdot 10^{-3}\ \text{m} : 1.0 \cdot 10^{6}\ \text{m/s} = 2.62 \cdot 10^{-8}\ \text{s}$. You can test the result in the simulation: deuteron, $v = 1.0 \cdot 10^{6}\ \text{m/s}$, $B = 5.0\ \text{T}$.

## Common misconception

"The magnetic field pushes the particles towards the centre of the machine." It does not. The force on each particle points to the centre of its own small circle, not to the centre of the plasma. A magnetic field cannot stop motion *along* the field lines at all, and it holds particles *across* the field lines only because they circle around them. That is why the shape of the field lines matters so much: closed (a torus), twisted, and without ends.

A second mistake is to think that the magnetic force speeds the particles up or heats them. It does no work, because it is always perpendicular to the velocity. A plasma is heated in other ways, for example by its own current, by beams of fast atoms or by radio waves.

## Summary

- The magnetic force on a moving charge is $F = |q| v B \sin\alpha$, perpendicular to $\overline{v}$ and $\overline{B}$; it changes the direction, not the speed.
- Perpendicular to a uniform field the particle moves on a circle: $r = mv/(|q|B)$, $T = 2\pi m/(|q|B)$, independent of the speed.
- With a velocity part along the field, the path is a helix around a field line.
- A magnetic mirror reflects particles with $\sin^2\theta \geq B_0/B_{\max}$; the rest escape through the loss cone.
- A torus closes the field lines, but its curved, uneven field makes ions and electrons drift apart; the field lines must be twisted.
- The single-particle model shows why confinement is possible. Collisions, turbulence and instabilities of the whole plasma make it difficult.
