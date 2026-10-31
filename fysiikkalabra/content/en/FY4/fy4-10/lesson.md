# Conservation of momentum and one-dimensional collisions

> **Why** can a cue ball stop dead when it hits a stationary ball head-on, while the other ball carries on at almost the same velocity?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a billiard table seen close up in the light of a lamp hanging above it. A cue points onto the table from the lower left, and has just struck the white cue ball. The cue ball has hit a red ball head-on, and a moment after the collision it has stopped in the middle of the table; a faint trail behind it shows the distance it travelled. The red ball speeds ahead towards the right edge of the table, with motion lines behind it. At the back of the table there are three more balls." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy410h-wall" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="420"><stop offset="0" stop-color="#f6f1e6"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><linearGradient id="fy410h-panel" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="270"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#8a5f22"/></linearGradient><linearGradient id="fy410h-felt" gradientUnits="userSpaceOnUse" x1="0" y1="180" x2="0" y2="640"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><radialGradient id="fy410h-yellow" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><radialGradient id="fy410h-blue" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></radialGradient><radialGradient id="fy410h-black" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#1f2933"/></radialGradient><radialGradient id="fy410h-white" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></radialGradient><radialGradient id="fy410h-red" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy410h-wall)"/>
  <rect x="0" y="150" width="1200" height="120" fill="url(#fy410h-panel)"/>
  <line x1="75" y1="150" x2="75" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="225" y1="150" x2="225" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="375" y1="150" x2="375" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="525" y1="150" x2="525" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="675" y1="150" x2="675" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="825" y1="150" x2="825" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="975" y1="150" x2="975" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1125" y1="150" x2="1125" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="0" y1="150" x2="1200" y2="150" stroke="#8a5f22" stroke-width="4" stroke-linecap="butt"/>
  <line x1="600" y1="0" x2="600" y2="40" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M420,118 L780,118 L1080,520 L120,520 Z" fill="#ffc078" fill-opacity="0.16"/>
  <path d="M430,118 L770,118 L720,44 L480,44 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="450" y="118" width="300" height="8" rx="3" fill="#ffc078"/>
  <path d="M20,590 L1180,590 L1040,236 L160,236 Z" fill="#b8622d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M20,590 L1180,590 L1180,600 L20,600 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <path d="M74,566 L1126,566 L1006,256 L194,256 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M104,550 L1096,550 L986,270 L214,270 Z" fill="url(#fy410h-felt)" stroke-linejoin="round"/>
  <ellipse cx="600" cy="400" rx="380" ry="120" fill="#ffffff" fill-opacity="0.16"/>
  <ellipse cx="64" cy="572" rx="34" ry="17" fill="#1f2933"/>
  <ellipse cx="600" cy="576" rx="32" ry="16" fill="#1f2933"/>
  <ellipse cx="1136" cy="572" rx="34" ry="17" fill="#1f2933"/>
  <ellipse cx="180" cy="250" rx="24" ry="12" fill="#1f2933"/>
  <ellipse cx="600" cy="248" rx="22" ry="11" fill="#1f2933"/>
  <ellipse cx="1020" cy="250" rx="24" ry="12" fill="#1f2933"/>
  <circle cx="300" cy="578" r="5" fill="#f1dfb5"/>
  <circle cx="340" cy="244" r="4" fill="#f1dfb5"/>
  <circle cx="900" cy="578" r="5" fill="#f1dfb5"/>
  <circle cx="860" cy="244" r="4" fill="#f1dfb5"/>
  <ellipse cx="364" cy="318" rx="19" ry="5.5" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="360" cy="300" r="20" fill="url(#fy410h-yellow)" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="874" cy="314" rx="19" ry="5.5" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="870" cy="296" r="20" fill="url(#fy410h-blue)" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="918" cy="337" rx="20" ry="6" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="914" cy="318" r="21" fill="url(#fy410h-black)" stroke="#1f2933" stroke-width="2"/>
  <line x1="330" y1="440" x2="356" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="372" y1="440" x2="398" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="414" y1="440" x2="440" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="456" y1="440" x2="482" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="498" y1="440" x2="524" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="540" y1="440" x2="566" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <ellipse cx="626.5" cy="461" rx="30.5" ry="9" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="620" cy="432" r="32" fill="url(#fy410h-white)" stroke="#1f2933" stroke-width="2"/>
  <line x1="700" y1="414" x2="760" y2="414" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="710" y1="430" x2="764" y2="430" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="720" y1="446" x2="768" y2="446" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <ellipse cx="818.5" cy="459" rx="30.5" ry="9" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="812" cy="430" r="32" fill="url(#fy410h-red)" stroke="#1f2933" stroke-width="2"/>
  <path d="M-10,566 L4,598 L292,468 L284,452 Z" fill="#d9b26a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M-10,566 L4,598 L100,554 L88,524 Z" fill="#8a5f22" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M292,468 L284,452 L298,446 L306,462 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
</svg>

## Key idea

### A system and its total momentum
In the chapter *Momentum and impulse* you learned that the momentum of an object is $\overline{p} = m\overline{v}$ and that the impulse of a constant net force changes it: $\Delta\overline{p} = \Sigma\overline{F}\,\Delta t$. In a collision, however, there are two objects that act on each other. So we look at them together as a **system**. The **total momentum** of a system is the vector sum of the momenta of its objects, $\overline{p}_\text{tot} = \overline{p}_1 + \overline{p}_2$.

The forces that the objects of the system exert on each other are **internal forces**, for example the forces of the bumpers of two carts on each other in a collision. Forces that come from outside the system are **external forces**, for example the weight of the carts, the normal force of the track and friction.

### Why the total momentum is conserved
When cart 1 pushes cart 2 with a force $\overline{F}$, by Newton's third law cart 2 pushes cart 1 with an equally large force $-\overline{F}$ in the opposite direction. The forces begin and end at the same moment, so they act for the same time $\Delta t$. If the force is constant, the momentum of cart 2 changes by the impulse $\overline{F}\,\Delta t$, and the momentum of cart 1 changes by the same amount in the opposite direction. The momentum that one cart gains is exactly what the other loses. The total momentum does not change. The same holds even if the force changes during the collision, because at every moment the forces are equally large and opposite.

<svg data-fig="vuorovaikutus" viewBox="0 0 600 340" role="img" aria-label="Diagram, not to scale: two air-track carts during a collision. The spring bumper between the carts is compressed. At the top are red force arrows: cart 1 pushes cart 2 to the right with a force F, and cart 2 pushes cart 1 to the left with an equally large force in the opposite direction, −F. Both forces act for the same time Δt. At the bottom the purple arrows are the changes in momentum: the change of cart 1, Δp1 = −FΔt, points to the left and that of cart 2, Δp2 = FΔt, to the right, equally long. Their sum is zero." style="max-width:100%;font-size:24px">
  <rect x="30" y="150" width="540" height="14" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="44" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="62" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="80" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="98" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="116" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="134" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="152" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="170" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="188" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="206" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="224" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="242" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="260" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="278" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="296" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="314" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="332" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="350" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="368" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="386" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="404" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="422" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="440" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="458" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="476" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="494" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="512" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="530" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="548" cy="157" r="1.8" fill="#8a96a3"/>
  <rect x="135" y="86" width="150" height="64" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="141" y="144" width="138" height="6" fill="#8a96a3"/>
  <rect x="325" y="86" width="150" height="64" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="331" y="144" width="138" height="6" fill="#8a96a3"/>
  <foreignObject x="240" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="350" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <path d="M285,128 L288.5,120 L295,136 L301.5,120 L308.5,136 L315,120 L321.5,136 L325,128" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="325" y1="128" x2="426" y2="128" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,128 L425,135 L425,121 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="285" y1="128" x2="184" y2="128" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M170,128 L185,121 L185,135 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="488.5" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="72.5" y="45.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$-\overline{F}$</div></foreignObject>
  <line x1="497" y1="74" x2="440" y2="122" stroke="#c92a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="103" y1="74" x2="170" y2="122" stroke="#c92a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="283.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <line x1="20" y1="196" x2="580" y2="196" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="300" y1="236" x2="185" y2="236" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M170,236 L186,229 L186,243 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="300" y1="236" x2="415" y2="236" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M430,236 L414,243 L414,229 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="300" y1="222" x2="300" y2="250" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="87.5" y="257.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_1 = -\overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="373.5" y="257.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_2 = \overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="221" y="299.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta\overline{p}_1 + \Delta\overline{p}_2 = \overline{0}$</div></foreignObject>
</svg>

This reasoning works only when external forces do not change the momentum. On a horizontal air track the weight and the normal force cancel each other, and friction is very small. Colliding cars, on the other hand, do feel the friction of the road, but the collision lasts only a fraction of a second. The forces of the bumpers are then much larger than friction, so the impulse of friction during the collision remains negligibly small. This gives the **law of conservation of momentum**: when the sum of the external forces acting on a system is zero, or their impulse during the collision is negligibly small, the total momentum of the system is conserved.

### Types of collisions
Momentum is conserved in every collision when the condition of the conservation law is met. Kinetic energy is not always conserved. A collision is **elastic** if the total kinetic energy of the objects after the collision is equal to that before it. Steel balls, billiard balls and carts with spring bumpers collide almost elastically. A collision is **inelastic** if some of the kinetic energy changes into other forms of energy. The objects then change shape, and kinetic energy becomes their internal energy and sound. When the objects stick together and move on together, the collision is **perfectly inelastic**, and the kinetic energy decreases the most: the largest possible part of it is transformed into other forms of energy.

<svg data-fig="tarra" viewBox="0 0 600 360" role="img" aria-label="Diagram to scale: two carts of equal mass on an air track, before the collision at the top and after it at the bottom. Before the collision cart 1 moves to the right at velocity v, and its momentum p is a purple arrow; cart 2 is at rest. The ends of the carts have hook-and-loop tape. After the collision the carts have stuck together and move together at half of the original velocity; the blue arrow is half as long. The purple arrow of the common momentum is as long as the momentum of cart 1 before the collision." style="max-width:100%;font-size:24px">
  <rect x="30" y="150" width="540" height="14" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="44" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="62" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="80" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="98" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="116" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="134" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="152" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="170" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="188" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="206" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="224" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="242" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="260" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="278" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="296" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="314" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="332" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="350" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="368" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="386" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="404" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="422" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="440" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="458" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="476" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="494" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="512" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="530" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="548" cy="157" r="1.8" fill="#8a96a3"/>
  <foreignObject x="36" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{before}$</div></foreignObject>
  <rect x="30" y="318" width="540" height="14" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="44" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="62" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="80" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="98" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="116" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="134" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="152" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="170" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="188" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="206" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="224" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="242" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="260" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="278" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="296" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="314" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="332" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="350" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="368" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="386" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="404" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="422" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="440" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="458" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="476" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="494" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="512" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="530" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="548" cy="325" r="1.8" fill="#8a96a3"/>
  <foreignObject x="36" y="185.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{after}$</div></foreignObject>
  <rect x="120" y="102" width="100" height="48" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="126" y="144" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="160" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <rect x="350" y="102" width="100" height="48" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="356" y="144" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="390" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <rect x="220" y="110" width="5" height="32" fill="#6b7480"/>
  <rect x="345" y="110" width="5" height="32" fill="#6b7480"/>
  <line x1="120" y1="84" x2="241" y2="84" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M252,84 L240,89.5 L240,78.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="260" y="69.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="120" y1="52" x2="237" y2="52" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M252,52 L236,59 L236,45 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="260" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
  <foreignObject x="358.5" y="65.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{v}_2 = \overline{0}$</div></foreignObject>
  <line x1="20" y1="178" x2="580" y2="178" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="200" y="270" width="100" height="48" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="206" y="312" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="240" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <rect x="300" y="270" width="100" height="48" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="306" y="312" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="340" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="200" y1="252" x2="255" y2="252" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M266,252 L254,257.5 L254,246.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="274" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\tfrac{1}{2}\overline{v}$</div></foreignObject>
  <line x1="200" y1="220" x2="317" y2="220" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M332,220 L316,227 L316,213 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="340" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
</svg>

In the figure, carts of equal mass stick together with hook-and-loop tape. The total momentum is the same before and after, but now the same momentum is shared by twice the mass, so the common velocity is half of the original. Kinetic energy $\tfrac12 mv^2$ is not conserved: twice the mass and half the velocity give half of the original kinetic energy. The other half becomes internal energy of the tape and the carts.

### An explosion
In an **explosion**, a system that is at rest or moving together breaks into parts because of internal forces: a spring is released between carts, skaters push each other away, or gunpowder pushes a bullet and a rifle apart. If the system is at rest at first, its total momentum is zero and stays zero. When a system at rest breaks into two parts, the parts get momenta of equal magnitude in opposite directions, and the lighter part gets the greater velocity. If there are more parts, the vector sum of their momenta is zero, but the momenta of the individual parts can differ in magnitude. This is why a rifle kicks backwards when the bullet goes forwards. Kinetic energy increases in an explosion, because energy of the spring, the muscles or the gunpowder is changed into kinetic energy.

### The answer to the opening question
Billiard balls have equal masses, and their collision is almost elastic. When the velocity of the cue ball is $v$, conservation of momentum says that the sum of the velocities of the balls stays the same: $v_1' + v_2' = v$. Conservation of kinetic energy says that the sum of the squares of the velocities stays the same: $v_1'^2 + v_2'^2 = v^2$. Squaring the first condition and subtracting the second gives $2 v_1' v_2' = 0$, so one of the balls is at rest after the collision. The cue ball cannot pass through the other ball, so it stops, and the other ball moves on with velocity $v$. In reality the balls also spin and the collision is not perfectly elastic, so the cue ball may keep moving a little.

## Formula: Conservation of momentum

### The conservation law with vectors and in one dimension
When the sum of the external forces acting on a system is zero, or their impulse during a collision or explosion is negligibly small, the total momentum is the same before and after:
```latex
\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'
```
where $\overline{p}_1$ and $\overline{p}_2$ are the momenta of the objects before and $\overline{p}_1'$ and $\overline{p}_2'$ their momenta after ($\text{kg}\cdot\text{m/s}$).

In a one-dimensional collision, all the velocities lie on the same line. We choose a positive direction, and then every velocity is a signed number: the velocity of an object moving in the opposite direction is negative. The conservation law becomes
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = m_1 v_1' + m_2 v_2'
\end{aligned}
```
where $m_1$ and $m_2$ are the masses of the objects ($\text{kg}$), $v_1$ and $v_2$ their velocities before and $v_1'$ and $v_2'$ their velocities after ($\text{m/s}$).

### Perfectly inelastic collision
When the objects stick together, they have a common velocity $v'$ after the collision:
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = (m_1 + m_2)\,v'
\end{aligned}
```
where $v'$ is the common velocity of the objects after the collision ($\text{m/s}$). For example, when a $0.40\,\text{kg}$ cart at a velocity of $0.60\,\text{m/s}$ sticks to a similar cart at rest, the common velocity is $0.30\,\text{m/s}$, and the kinetic energy decreases from $0.072\,\text{J}$ to $0.036\,\text{J}$.

### Elastic collision
In an elastic collision, in addition to momentum, the total kinetic energy of the objects is conserved:
```latex
\begin{aligned}
&E_{\text{k},1} + E_{\text{k},2} \\
&\quad = E_{\text{k},1}' + E_{\text{k},2}'
\end{aligned}
```
where $E_\text{k} = \tfrac12 mv^2$ is the kinetic energy of each object before and $E_\text{k}'$ after ($\text{J}$). When the velocity of one object after the collision is known, the other follows from the law of conservation of momentum, and by comparing the kinetic energies we can see whether the collision was elastic. When an object hits an object of equal mass at rest elastically and head-on, the objects exchange velocities.

<svg data-fig="tyypit" viewBox="0 0 600 434" role="img" aria-label="Diagram, momenta to scale: three events for two carts of equal mass, before on the left and after on the right. At the top an elastic collision: before, cart 1 has a momentum to the right and cart 2 is at rest; after, cart 1 is at rest and cart 2 has the same momentum; kinetic energy is conserved. In the middle a perfectly inelastic collision: the carts stick together, and the common momentum is as large as before; kinetic energy decreases. At the bottom an explosion: before, the carts are together at rest and the total momentum is zero; after, the carts have momenta of equal magnitude in opposite directions; kinetic energy increases." style="max-width:100%;font-size:24px">
  <foreignObject x="90" y="45.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{elastic: } E_\text{k}\ \text{conserved}$</div></foreignObject>
  <line x1="40" y1="152" x2="270" y2="152" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="330" y1="152" x2="560" y2="152" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="282" y1="132" x2="309" y2="132" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M318,132 L308,136.5 L308,127.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="65" y="122" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="71" y="146" width="38" height="6" fill="#8a96a3"/>
  <rect x="195" y="122" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="201" y="146" width="38" height="6" fill="#8a96a3"/>
  <line x1="70" y1="106" x2="167" y2="106" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,106 L166,112.5 L166,99.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <rect x="335" y="122" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="341" y="146" width="38" height="6" fill="#8a96a3"/>
  <rect x="425" y="122" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="431" y="146" width="38" height="6" fill="#8a96a3"/>
  <line x1="440" y1="106" x2="537" y2="106" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M550,106 L536,112.5 L536,99.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="20" y1="170" x2="580" y2="170" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="90" y="175.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{perfectly inelastic: } E_\text{k}\ \text{decreases}$</div></foreignObject>
  <line x1="40" y1="282" x2="270" y2="282" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="330" y1="282" x2="560" y2="282" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="282" y1="262" x2="309" y2="262" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M318,262 L308,266.5 L308,257.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="65" y="252" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="71" y="276" width="38" height="6" fill="#8a96a3"/>
  <rect x="195" y="252" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="201" y="276" width="38" height="6" fill="#8a96a3"/>
  <line x1="70" y1="236" x2="167" y2="236" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,236 L166,242.5 L166,229.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <rect x="395" y="252" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="401" y="276" width="38" height="6" fill="#8a96a3"/>
  <rect x="445" y="252" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="451" y="276" width="38" height="6" fill="#8a96a3"/>
  <line x1="390" y1="236" x2="487" y2="236" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M500,236 L486,242.5 L486,229.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="20" y1="300" x2="580" y2="300" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="90" y="305.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{explosion: } E_\text{k}\ \text{increases}$</div></foreignObject>
  <line x1="40" y1="412" x2="270" y2="412" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="330" y1="412" x2="560" y2="412" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="282" y1="392" x2="309" y2="392" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M318,392 L308,396.5 L308,387.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="105" y="382" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="111" y="406" width="38" height="6" fill="#8a96a3"/>
  <rect x="155" y="382" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="161" y="406" width="38" height="6" fill="#8a96a3"/>
  <path d="M150,397 L152.5,392 L157.5,402 L160,397" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="113.5" y="349.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$p_\text{tot} = 0$</div></foreignObject>
  <rect x="345" y="382" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="351" y="406" width="38" height="6" fill="#8a96a3"/>
  <rect x="495" y="382" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="501" y="406" width="38" height="6" fill="#8a96a3"/>
  <line x1="390" y1="366" x2="337" y2="366" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M324,366 L338,359.5 L338,372.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="500" y1="366" x2="553" y2="366" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M566,366 L552,372.5 L552,359.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="113.5" y="3.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{before}$</div></foreignObject>
  <foreignObject x="410" y="3.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{after}$</div></foreignObject>
</svg>

When external forces act, the law of conservation of momentum is used only across the collision or explosion itself, a short time from beginning to end. Before and after, external forces such as friction or weight can change the motion of the objects, and then the motion is studied with other laws, for example the work–energy principle.

## Worked example
In a rail yard, freight car A, of mass $32\,000\,\text{kg}$, moves at $1.5\,\text{m/s}$ and catches up with car B, of mass $18\,000\,\text{kg}$, moving in the same direction at $0.50\,\text{m/s}$. The cars couple together and continue together. What is the common velocity of the cars immediately after coupling?

<!-- vaihe -->

**Given and find.** $m_\text{A} = 32\,000\,\text{kg}$, $v_\text{A} = 1.5\,\text{m/s}$, $m_\text{B} = 18\,000\,\text{kg}$ and $v_\text{B} = 0.50\,\text{m/s}$. We are asked for the common velocity $v'$ immediately after coupling.

<!-- vaihe -->

**Principle.** We choose both cars as the system and the direction of motion of the cars as the positive direction. Coupling takes a moment, and during it the forces of the couplers are internal forces. The weight and the normal force of the rails cancel each other, and the impulse of rolling resistance is negligibly small during the short coupling, so the total momentum is conserved. The cars stick together, so the collision is perfectly inelastic.

<!-- vaihe -->

**Formula solved.** The momentum before is equal to the momentum of the combined object after:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} + m_\text{B} v_\text{B} \\
&\quad = (m_\text{A} + m_\text{B})\,v' \\[6pt]
&v' = \frac{m_\text{A} v_\text{A} + m_\text{B} v_\text{B}}{m_\text{A} + m_\text{B}}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: the masses are in kilograms and the velocities in $\text{m/s}$.

<!-- vaihe -->

**Substitution.** First we calculate the momenta before coupling and then the common velocity:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} \\
&= 32\,000\,\text{kg} \cdot 1.5\,\tfrac{\text{m}}{\text{s}} \\
&= 48\,000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&m_\text{B} v_\text{B} \\
&= 18\,000\,\text{kg} \cdot 0.50\,\tfrac{\text{m}}{\text{s}} \\
&= 9000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&v' \\
&= \frac{48\,000 + 9000}{50\,000} \cdot \frac{\text{kg}\cdot\text{m/s}}{\text{kg}} \\
&= 1.14\,\tfrac{\text{m}}{\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Result.** The common velocity of the cars is $v' \approx 1.1\,\text{m/s}$ in the original direction of motion of the cars. The result is given to two significant figures, like the velocities $1.5\,\text{m/s}$ and $0.50\,\text{m/s}$.

<!-- vaihe -->

**Reasonableness.** The common velocity lies between the initial velocities of the cars, $0.50\,\text{m/s}$ and $1.5\,\text{m/s}$, and closer to the velocity of the heavier car A, as it should. The kinetic energy decreases from $38.3\,\text{kJ}$ to $32.5\,\text{kJ}$, that is, by about $15\,\%$, which fits a perfectly inelastic collision: kinetic energy changes into internal energy of the couplers and buffers, and into sound.

## Common misconception
Many people think that kinetic energy is conserved in a collision in the same way as momentum. Momentum is always conserved when the impulse of the external forces is negligibly small, but kinetic energy is conserved only in an elastic collision. If the velocity of carts that stick together is calculated from conservation of kinetic energy, the result is too large.

Another mistake is to forget the signs. When objects move towards each other, their momenta are in opposite directions, and one of them is negative. A third mistake is to think that momentum disappears when a clay ball dropped on the floor stops. The momentum of the ball passes to the Earth: the ball and the Earth form a system whose total momentum is conserved, but the mass of the Earth is so great that the change in its velocity cannot be noticed.

## Summary
- The total momentum of a system is conserved when the sum of the external forces is zero or their impulse during the collision or explosion is negligibly small: $\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'$.
- Conservation follows from Newton's third law: the internal forces in a collision are equally large and opposite and act for the same time, so the changes in the momenta of the objects cancel each other.
- In one dimension we choose a positive direction, and velocities are signed: $m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$.
- In an elastic collision, kinetic energy is also conserved. In an inelastic collision some of the kinetic energy changes into internal energy, and in a perfectly inelastic collision the objects move on together with a common velocity.
- In an explosion, the total momentum of a system at rest stays zero: the parts get momenta of equal magnitude in opposite directions, and kinetic energy increases.
