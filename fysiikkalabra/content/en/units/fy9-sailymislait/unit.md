# Mechanical energy and momentum

> **Why** do two railway wagons that couple together move on more slowly than before coupling, even though nothing brakes them?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter railway yard in the middle of a forest on a bright day. On the left a reddish-brown covered goods wagon rolls to the right, with motion lines behind it. On the right stands an identical wagon that the rolling wagon is about to couple with. Above the tracks are the masts and the contact wire of an electrified railway, and in the background spruce forest and snowbanks." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sailymislait-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

A large share of the mechanics problems in the exam can be solved with two conservation laws. **Energy is always conserved**: mechanical energy is transformed into internal energy when friction, air resistance or the deformation of a body does work, but the total energy stays the same. **Momentum is conserved** when the sum of the external forces on the system is zero or their impulse during the collision is negligible.

```pysahdy
When is momentum conserved, and why can mechanical energy still decrease?
---
Momentum is conserved when the sum of the external forces is zero or their impulse is negligibly small. Mechanical energy decreases when friction, air resistance or deformation transforms it into internal energy; the total energy is conserved.
```

<svg data-fig="kartta" viewBox="0 0 380 870" role="img" aria-label="Recognition chart: how do I tell which law to use? First see the sign in the task. No friction, only gravity: mechanical energy is conserved, so the sum of the initial potential and kinetic energy equals the final sum. Friction or a motor does work: the work-energy principle, where the work of the other forces is added to the initial mechanical energy. A body is moving: kinetic energy is half m v squared. Height changes: potential energy is m g h. Collision or explosion: momentum is conserved, before equals after. Elastic collision: kinetic energy is conserved too, its change is zero. A force acts for a time: the impulse is the change of momentum. Power or efficiency asked: efficiency is the output power divided by the input power." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{the sign first, then the law}$</div></foreignObject>
  <line x1="14" y1="149" x2="30" y2="149" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{no friction, only gravity}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{mechanical energy is conserved}$</div></foreignObject>
  <rect x="132" y="171" width="230" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="136" y="174" width="222" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$</div></foreignObject>
  <line x1="14" y1="265" x2="30" y2="265" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="214" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="224.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{friction or a motor does work}$</div></foreignObject>
  <line x1="40" y1="254" x2="362" y2="254" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="259" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{work-energy principle}$</div></foreignObject>
  <rect x="72" y="287" width="290" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="76" y="290" width="282" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$</div></foreignObject>
  <line x1="14" y1="366" x2="30" y2="366" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="330" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="340.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a body is moving}$</div></foreignObject>
  <line x1="40" y1="370" x2="362" y2="370" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="375" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kinetic energy}$</div></foreignObject>
  <rect x="238" y="374" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="376" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_\text{k} = \tfrac12 mv^2$</div></foreignObject>
  <line x1="14" y1="452" x2="30" y2="452" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="416" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="426.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{height changes}$</div></foreignObject>
  <line x1="40" y1="456" x2="362" y2="456" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="461" width="198" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{potential energy}$</div></foreignObject>
  <rect x="256" y="460" width="106" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="260" y="462" width="98" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_\text{p} = mgh$</div></foreignObject>
  <line x1="14" y1="553" x2="30" y2="553" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="502" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="512.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{collision or explosion}$</div></foreignObject>
  <line x1="40" y1="542" x2="362" y2="542" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="547" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{momentum is conserved}$</div></foreignObject>
  <rect x="152" y="575" width="210" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="156" y="578" width="202" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\overline{p}_\text{before} = \overline{p}_\text{after}$</div></foreignObject>
  <line x1="14" y1="654" x2="30" y2="654" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="618" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="628.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{elastic collision}$</div></foreignObject>
  <line x1="40" y1="658" x2="362" y2="658" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="663" width="204" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kinetic energy stays}$</div></foreignObject>
  <rect x="262" y="662" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="664" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta E_\text{k} = 0$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a force acts for a time}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{impulse}$</div></foreignObject>
  <rect x="246" y="748" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="750" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\overline{I} = \Delta\overline{p}$</div></foreignObject>
  <line x1="14" y1="826" x2="30" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="790" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="800.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{power or efficiency asked}$</div></foreignObject>
  <line x1="40" y1="830" x2="362" y2="830" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="835" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{efficiency}$</div></foreignObject>
  <rect x="238" y="834" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="836" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = P_\text{a}/P_\text{o}$</div></foreignObject>
</svg>

A solution starts with choosing the law to suit the situation. When the question asks for a speed or a height at different points and the work done by the forces is known, use the work–energy principle. When bodies collide or push each other, use conservation of momentum. When the question asks for a force and the time is known, use the impulse–momentum principle. Many problems combine them: first energy, then a collision, then energy again.

This also answers the opening question. In the coupling the forces between the wagons are internal, so the momentum $32\,000\,\text{kg} \cdot 1.6\,\text{m/s} = 51\,200\,\text{kg} \cdot \text{m/s}$ is conserved. It is shared by twice the mass, so the speed is halved, $0.80\,\text{m/s}$. The kinetic energy $\tfrac12 mv^2$ then decreases from $41\,\text{kJ}$ to $20\,\text{kJ}$: half of it is transformed into internal energy of the buffers and couplings and into sound.

<svg data-fig="tormays" viewBox="0 0 420 560" role="img" aria-label="Diagram, velocities and bars to scale. At the top, before the collision: the left wagon moves to the right at 1.6 m/s, blue arrow, and the right wagon is at rest. Below it, after the collision: the wagons are coupled and move together at 0.80 m/s, an arrow half as long. At the bottom are bars. The total momentum is the same before and after, 51 200 kilogram metres per second. The kinetic energy is 41 kJ before and 20 kJ after; the missing half has been transformed into internal energy of the buffers and couplings." style="max-width:100%;font-size:20px">
  <foreignObject x="8" y="10" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{before}$</div></foreignObject>
  <line x1="0" y1="130" x2="420" y2="130" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="20" y="60" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="42" cy="114" r="9" fill="#1f2933"/>
  <circle cx="108" cy="114" r="9" fill="#1f2933"/>
  <rect x="290" y="60" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="312" cy="114" r="9" fill="#1f2933"/>
  <circle cx="378" cy="114" r="9" fill="#1f2933"/>
  <line x1="75" y1="44" x2="222" y2="44" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M235,44 L221,50.5 L221,37.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="119.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#1971c2">$1.6\,\text{m/s}$</div></foreignObject>
  <foreignObject x="327" y="29" width="36" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$v = 0$</div></foreignObject>
  <foreignObject x="8" y="148" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{after}$</div></foreignObject>
  <line x1="0" y1="260" x2="420" y2="260" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="100" y="190" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="122" cy="244" r="9" fill="#1f2933"/>
  <circle cx="188" cy="244" r="9" fill="#1f2933"/>
  <rect x="214" y="190" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="236" cy="244" r="9" fill="#1f2933"/>
  <circle cx="302" cy="244" r="9" fill="#1f2933"/>
  <rect x="208" y="206" width="8" height="10" fill="#1f2933"/>
  <line x1="155" y1="176" x2="222" y2="176" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M235,176 L221,182.5 L221,169.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="290" y="152" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$0.80\,\text{m/s}$</div></foreignObject>
  <line x1="10" y1="500" x2="410" y2="500" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="40" y="340" width="52" height="160" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="110" y="340" width="52" height="160" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="230" y="340" width="52" height="160" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="420" width="52" height="80" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="340" width="52" height="80" fill="#dee2e6" stroke="#1f2933" stroke-width="1.5" stroke-dasharray="6 4"/>
  <foreignObject x="76" y="280" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_\text{tot}$</div></foreignObject>
  <foreignObject x="241.5" y="280" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="35.5" y="512" width="61" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{before}$</div></foreignObject>
  <foreignObject x="110" y="512" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{after}$</div></foreignObject>
  <foreignObject x="225.5" y="512" width="61" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{before}$</div></foreignObject>
  <foreignObject x="300" y="512" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{after}$</div></foreignObject>
  <foreignObject x="242.5" y="312" width="167" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#6b7480">$\text{into internal energy}$</div></foreignObject>
  <foreignObject x="39.5" y="308" width="123" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$51\,200\,\text{kg} \cdot \text{m/s}$</div></foreignObject>
  <foreignObject x="230" y="410" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$41\,\text{kJ}$</div></foreignObject>
  <foreignObject x="300" y="450" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$20\,\text{kJ}$</div></foreignObject>
</svg>

## Formula: Mechanical energy and momentum

### Energy

```kaavat
kinetic energy :: E_\text{k} = \tfrac{1}{2}\,mv^2
gravitational potential energy near the Earth's surface :: E_\text{p} = mgh
```

where $m$ is the mass ($\text{kg}$), $v$ the speed ($\text{m/s}$), $g = 9.81\,\text{m/s}^2$ and $h$ the height above the chosen zero level ($\text{m}$). $E_\text{p} = mgh$ holds near the Earth's surface. The work–energy principle is

```kaavat
work-energy principle of mechanics :: E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}
```

where the index $0$ means the initial state and $W$ is the work done by forces other than the weight ($\text{J}$). The work done by a constant force is $W = F_\parallel\,s$, where $F_\parallel$ is the component of the force along the motion; the work done by friction and air resistance is negative. When $W = 0$, mechanical energy is conserved: $E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$.

```pysahdy
What is the sign of the work done by friction in the work-energy principle, and why?
---
The work of friction is negative, $W < 0$, because the friction force points against the motion. It therefore decreases the mechanical energy, which turns into internal energy.
```

### Momentum and impulse

```kaavat
momentum :: \overline{p} = m\overline{v}
impulse of a force :: \overline{I} = \overline{F}\Delta t
impulse-momentum principle :: \overline{I} = \Delta\overline{p}
```

where $\overline{p}$ is the momentum ($\text{kg} \cdot \text{m/s}$), $\overline{I}$ the impulse ($\text{N} \cdot \text{s}$) and $\overline{F}$ a constant force acting for the time interval $\Delta t$. The change in momentum is caused by the impulse of the net force, $\Sigma\overline{F}\,\Delta t = \Delta\overline{p}$. For a varying force the average force is $F_\text{avg} = |\Delta p| : \Delta t$. In one dimension a positive direction is chosen, and velocities pointing in the opposite direction are negative. When the impulse of the external forces is negligible,

```latex
m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'
```

In an elastic collision kinetic energy is also conserved. In a perfectly inelastic collision the bodies move on with a common velocity, $v_1' = v_2' = v'$, and the largest share of kinetic energy is transformed into internal energy.

```pysahdy
Two bodies collide perfectly inelastically and move on together. What is conserved and what is not?
---
Momentum is conserved, because the impulse of the external forces is negligibly small. Kinetic energy is transformed into internal energy, so it is not conserved.
```

### Applications

On a horizontal road the stopping distance $s_\text{p}$ ($\text{m}$) of a car is the reaction distance plus the braking distance. During the reaction time $t_\text{r}$ ($\text{s}$) the car moves at the constant speed $v_0$ ($\text{m/s}$), and during braking the speed falls to zero with a constant deceleration $a$ ($\text{m/s}^2$); at the limit of locking the wheels $a = \mu g$.

<svg data-fig="pysahtyminen" viewBox="0 0 600 360" role="img" aria-label="Diagram, no numerical values: the speed v of a car as a function of the time t. During the reaction time t r the speed stays at the initial speed v 0, so the graph is horizontal, and under it is a blue rectangle, the reaction distance s r. Then during the braking time t b the speed decreases steadily to zero, so the graph is a falling straight line, and under it is a sand-coloured triangle, the braking distance s b. The car stops at the instant t r + t b." style="max-width:100%;font-size:24px">
  <line x1="89" y1="300" x2="484" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,300 L483,306 L483,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,44 L96,57 L84,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polygon points="90,300 90,127.5 185,127.5 185,300" fill="#d0e6fb" fill-opacity="0.9"/>
  <polygon points="185,300 185,127.5 394,300" fill="#f1dfb5" fill-opacity="0.9"/>
  <polyline points="185,300 185,127.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,127.5 185,127.5 394,300" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="45" y="113" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="168.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r}$</div></foreignObject>
  <foreignObject x="359" y="311.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r} + t_\text{b}$</div></foreignObject>
  <foreignObject x="121" y="199" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$s_\text{r}$</div></foreignObject>
  <foreignObject x="238" y="228" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s_\text{b}$</div></foreignObject>
  <foreignObject x="92" y="93.5" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{reaction}$</div></foreignObject>
  <foreignObject x="306.5" y="161.5" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{braking}$</div></foreignObject>
</svg>

```johda
A car is moving at the speed $v_0$ when the driver sees an obstacle. Derive the stopping distance $s_\text{p}$ when the reaction time is $t_\text{r}$ and the deceleration $a$ during braking is constant.
---
During the reaction time the car moves at a constant velocity. The position in uniformly accelerated linear motion with zero acceleration gives the reaction distance:

$$s_\text{r} = v_0\,t_\text{r}$$

During braking the acceleration is $-a$. The velocity in uniformly accelerated motion gives the braking time $t_\text{b}$, when the final velocity is zero:

$$0 = v_0 - a\,t_\text{b} \quad\Rightarrow\quad t_\text{b} = \frac{v_0}{a}$$

Substitute the braking time into the expression for the position. The braking distance is

$$s_\text{b} = v_0\,t_\text{b} - \tfrac12\,a\,t_\text{b}^2 = \frac{v_0^2}{a} - \frac{v_0^2}{2a} = \frac{v_0^2}{2a}$$

The stopping distance is the sum of the reaction distance and the braking distance:

$$s_\text{p} = s_\text{r} + s_\text{b} = v_0\,t_\text{r} + \frac{v_0^2}{2a}$$

The work–energy principle gives the same braking distance: by Newton's second law the net braking force is $ma$, and its work $-ma\,s_\text{b}$ removes all of the kinetic energy $\tfrac12 mv_0^2$. In the graph the distances are areas: the reaction distance is a rectangle and the braking distance a triangle of area $\tfrac12\,v_0 t_\text{b}$.
```

The electric power $P_\text{hydro}$ ($\text{W}$) of a hydropower plant is a part of the potential energy that the falling water loses per unit time, and the efficiency $\eta$ tells how large a part. Water of density $\rho$ ($\text{kg/m}^3$) flows through the plant at the flow rate $Q$ ($\text{m}^3\text{/s}$), the volume per second, and falls through the head $h$ ($\text{m}$).

```johda
Water flows through a hydropower plant at the flow rate $Q$, and the head is $h$. Derive the electric power $P_\text{hydro}$ of the plant when its efficiency is $\eta$.
---
In the time $\Delta t$ the volume of water $V = Q\,\Delta t$ flows through the plant. By the definition of density $\rho = \tfrac{m}{V}$ its mass is

$$m = \rho V = \rho Q\,\Delta t$$

When this water falls through the height $h$, its gravitational potential energy decreases by

$$\Delta E = mgh = \rho Q\,\Delta t\,gh$$

The speed of the water is about the same at the top and at the bottom of the fall, so this energy goes to the plant. Power is the change in energy per unit time, so the water gives the plant the input power

$$P_\text{o} = \frac{\Delta E}{\Delta t} = \rho Qgh$$

The efficiency $\eta = \tfrac{P_\text{a}}{P_\text{o}}$ tells what part of this power is obtained as electricity:

$$P_\text{hydro} = \eta P_\text{o} = \eta\rho Qgh$$
```

Likewise, the electric power $P_\text{wind}$ ($\text{W}$) of a wind turbine is a part of the kinetic energy that the air carries through the rotor per unit time. Air of density $\rho$ flows at the speed $v$ ($\text{m/s}$) perpendicularly through the area $A$ ($\text{m}^2$) swept by the rotor.

<svg data-fig="tuuli" viewBox="0 0 600 420" role="img" aria-label="Diagram from the side, no numerical values. On the right is a wind turbine: the tower, the nacelle and three blades. The area A swept by the rotor is drawn as an ellipse. The wind blows from the left at the speed v, blue arrows. To the left of the rotor is a light-blue cylinder of air whose base is the area A and whose length is v times delta t: the air that passes through the rotor in the time delta t." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sailymislait-tuuli.webp" x="1.2" y="0" width="597" height="422.9" preserveAspectRatio="none"/>
  <foreignObject x="235" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="458" y="73.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="256" y="335.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$v\,\Delta t$</div></foreignObject>
  <foreignObject x="146" y="44" width="154" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{air in the time } \Delta t$</div></foreignObject>
</svg>

```johda
The wind blows at the speed $v$ perpendicularly towards the rotor, and the area swept by the rotor is $A$. Derive the electric power $P_\text{wind}$ of the wind turbine when its efficiency is $\eta$.
---
In the time $\Delta t$ the air travels the distance $v\,\Delta t$. So a cylinder of air with base area $A$ and length $v\,\Delta t$ passes through the rotor (figure). By the definition of density its mass is

$$m = \rho V = \rho A v\,\Delta t$$

The kinetic energy of this cylinder of air is

$$E_\text{k} = \tfrac12\,mv^2 = \tfrac12\,\rho A v\,\Delta t \cdot v^2$$

Simplify:

$$E_\text{k} = \tfrac12\,\rho A v^3\,\Delta t$$

Power is energy per unit time, so the air brings the input power

$$P_\text{o} = \frac{E_\text{k}}{\Delta t} = \tfrac12\,\rho A v^3$$

With the efficiency $\eta = \tfrac{P_\text{a}}{P_\text{o}}$ the electric power is

$$P_\text{wind} = \eta P_\text{o} = \tfrac12\,\eta\rho A v^3$$

The speed is cubed because a faster wind carries both more air through the rotor and more energy in each kilogram of air. The result assumes a constant efficiency, so it holds when the turbine runs below its rated power.
```

## Common mistakes {Virheet}

- **Kinetic energy and momentum mixed up.** In a collision momentum is conserved, kinetic energy only in an elastic collision. Momentum is not converted into internal energy: what is converted into internal energy is kinetic energy.
- **Signs forgotten.** A ball that bounces back changes its momentum more than one that stops: for a ball bouncing back at the same speed $\Delta p = -mv - mv = -2mv$.
- **Friction disappears from the work–energy principle.** The work done by friction is negative, and it transforms mechanical energy into internal energy; it neither creates nor destroys energy.
- **Kilometres per hour substituted directly.** $72\,\text{km/h} = 72 \cdot \tfrac{1000\,\text{m}}{3600\,\text{s}} = 20\,\text{m/s}$, before the speed is squared.
- **The square of the speed forgotten.** Twice the speed makes the kinetic energy and the braking distance four times as large, and the wind power eight times as large.
- **Conservation of momentum without its condition.** Say why the external forces do not change the momentum during the collision.

## Review if needed {Kertaa}

- Forms of energy and the zero level: [*Kinetic energy, potential energy and mechanical energy*](fy4-7.html). Work and the work–energy principle: [*Conservation of mechanical energy and the work–energy principle*](fy4-8.html).
- Power plants: [*Hydro and wind power as energy converters*](fy4-15.html).
- Momentum, impulse and average force: [*Momentum and impulse*](fy4-9.html). Collisions: [*Conservation of momentum and one-dimensional collisions*](fy4-10.html).
- Stopping distance and safety equipment: [*Road safety: braking, seat belts and airbags*](fy4-11.html).
