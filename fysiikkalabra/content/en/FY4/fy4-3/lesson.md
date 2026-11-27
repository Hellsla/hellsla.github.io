# Interaction and force: Newton's first and third laws

> **Why** does a curling stone slide tens of metres along the ice although nobody is pushing it any more?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a curling hall. On the left the curler has slid in a low delivery position and released the stone, and the outstretched hand is already far from the stone. In the middle a curling stone with a red handle slides to the right on the ice, with a thin trail behind it. Two sweepers move ahead of the stone with their brooms against the ice. On the right, in the ice, are the rings of the target area with two stones already in them." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
### Force is an interaction
When two objects act on each other, there is an **interaction** between them: a hand pushes a box, a rope pulls a sledge and the Earth pulls an apple. The strength of an interaction is described by a **force**, whose unit is the newton ($\text{N}$). A force is a vector with a magnitude and a direction, and it is written $\overline{F}$. Every force has a cause, and that cause is always another object. In contact forces the objects touch each other. The gravitational force of the Earth, the **weight** $\overline{G}$, and the forces of magnets also act at a distance.

```pysahdy
A thrown ball is flying through the air. Which bodies act on the ball during the flight?
---
The Earth (its weight) and the air (air resistance). The thrower's hand no longer acts on the ball.
```

### Motion continues without a force
A curler pushes the stone only for a moment. When the hand lets go, nothing pushes the stone forward any more, but the stone still slides tens of metres. During the slide only the Earth and the ice act on the stone (air resistance is very small). In the vertical direction the weight and the **normal force** of the ice, the force that supports the stone upwards and is perpendicular to the surface, cancel each other. In the horizontal direction there is only the small **friction** of the ice, a force between the surfaces that opposes motion, points backwards and slows the stone down very gradually.

<svg data-fig="curling" viewBox="0 0 600 340" role="img" aria-label="Two pictures of a sliding curling stone. On the left the situation picture: the stone slides to the right on the ice, and above it a thin blue arrow v shows the velocity to the right. The curler&#x27;s hand has been left far behind. On the right the force diagram: the stone as a rectangle. The weight G points down from the centre, the normal force N of the ice points up from the bottom surface at the same length, and the small friction force of the ice points to the left from the rear corner of the bottom surface. There is no forward-pointing force. The picture is not to scale: the arrow of the friction force is drawn longer than the real one for clarity." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-curling.webp" x="0" y="-1.2" width="600" height="352.5" preserveAspectRatio="none"/>
  <foreignObject x="46" y="9.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation picture}$</div></foreignObject>
  <foreignObject x="227.5" y="131.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="371" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{force diagram}$</div></foreignObject>
  <foreignObject x="455.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="479.5" y="87.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="336.5" y="199.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

If there were no friction at all, the speed of the stone would not change, and it would slide in the same direction for ever. This is **Newton's first law**, also called the **law of inertia**: if the sum of the forces acting on an object is zero, the object stays at rest or moves in a straight line at constant velocity. A force is needed to *change* motion, not to keep it going. The tendency of an object to keep its state of motion is called **inertia**.

<figure class="unit-photo"><img src="pics/fy4/tug-of-war.webp" alt="Three men pulling a thick rope, leaning back with their feet against the ground."><figcaption>Tug of war players lean back and press their feet against the ground.</figcaption></figure>

Everyday experience seems to say otherwise, because on Earth friction and air resistance slow down almost everything that moves. A bicycle stops when you stop pedalling because the road and the air brake it, not because the "force of motion" has been used up. The smaller the friction, the longer the motion continues: further on ice than on asphalt, and in space almost without limit.

```pysahdy
Why does a shopping cart stop when you stop pushing it?
---
Friction and air resistance change its motion. Without them the cart would keep moving at the same velocity.
```

### Action and reaction
When skater A pushes skater B, both start to glide away from each other. B does not just receive the push, but acts on A at the same time. An interaction always works in both directions. This is **Newton's third law**, the **law of action and reaction**: when object A exerts a force on object B, B exerts an equally large but oppositely directed force on A. The two forces form an action–reaction pair. A force and its reaction force arise in the same interaction at the same time, and they are of the same kind: push and counter-push, attraction and counter-attraction.

<svg data-fig="luistelijat" viewBox="0 0 600 460" role="img" aria-label="At the top the situation picture: two skaters stand facing each other on the ice and push each other with their palms. On the left is a large adult A, on the right a smaller child B. At the bottom the force diagram of each separately, the skater as a rectangle. In the diagram of A: the weight G A down from the centre, the normal force N A of the ice up from the bottom surface and the force of B on A, F B A, pointing to the left and ending at the right side of A. In the diagram of B: the weight G B, which is shorter than the weight of A, the normal force N B and the force of A on B, F A B, pointing to the right and ending at the left side of B. The arrows F B A and F A B are equally long. Friction is ignored." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-luistelijat.webp" x="0" y="-1.2" width="600" height="467.5" preserveAspectRatio="none"/>
  <foreignObject x="166" y="25.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="390" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <foreignObject x="111.5" y="417.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_A$</div></foreignObject>
  <foreignObject x="179.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_A$</div></foreignObject>
  <foreignObject x="229.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{BA}$</div></foreignObject>
  <foreignObject x="460.5" y="389" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_B$</div></foreignObject>
  <foreignObject x="390.5" y="288" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_B$</div></foreignObject>
  <foreignObject x="324.5" y="300.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{AB}$</div></foreignObject>
  <foreignObject x="93" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{A}$</div></foreignObject>
  <foreignObject x="495" y="320.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{B}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy4/falcon9-crew9-launch.webp" alt="A white rocket rises vertically on a bright flame and a trail of smoke. Around the launch pad there are large white clouds of steam and lattice towers."><figcaption>A Falcon 9 rocket lifts off in Florida in September 2024. The rocket pushes the exhaust gases downwards, and the gases push the rocket upwards with a force of equal magnitude. The rocket does not need air or ground to push against.</figcaption></figure>

An adult and a child receive an equally large force from each other, although the adult is much heavier. The child still starts moving with a greater speed, because the same force changes the motion of the smaller mass more; we return to this in the chapter *Newton's second law*. The most important point is that a force and its reaction force act on **different objects**. That is why they never cancel each other, and why they are not drawn in the force diagram of the same object.

### Two ways to choose the system
The same push can be looked at in two ways. If the system is only skater A, the push from B is an external force $\overline{F}_{BA}$ on A, and it is drawn in A's force diagram. If the system is A and B together, the forces of the interaction pair, $\overline{F}_{AB}$ and $\overline{F}_{BA}$, are internal to the system. They are equal in magnitude and opposite in direction, so their vector sum is $\overline{F}_{AB}+\overline{F}_{BA}=\overline{0}$. That is why they do not belong in the system's force diagram, which shows only the external forces.

<svg data-fig="systeemit" viewBox="0 0 600 470" role="img" aria-label="Two force diagrams of the same push between skaters. On the left the system is only skater A, with a dashed line around them. Their force diagram has the weight G A, the support force N A and B&#x27;s force on A, F BA, which points left. On the right the system is skaters A and B together, and the dashed line goes around both. The force diagram has only external forces: the total weight and the total support force of A and B. The forces of the interaction pair, F AB and F BA, are internal and are not drawn as arrows; their vector sum is the zero vector." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43y-ice1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy43y-ice2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <rect x="8" y="160" width="284" height="14" fill="url(#fy43y-ice1)"/>
  <rect x="308" y="160" width="284" height="14" fill="url(#fy43y-ice2)"/>
  <line x1="300" y1="20" x2="300" y2="450" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="96" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{system: A}$</div></foreignObject>
  <foreignObject x="371" y="7.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{system: A and B}$</div></foreignObject>
  <path d="M112,123 L106.5,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M103,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="101" y1="160" x2="116" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M112,123 L117,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M113.5,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="111" y1="160" x2="126.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M103,125.5 Q110.5,84 122.5,91 L121.5,125.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M116,93.5 L142,100" fill="none" stroke="#1971c2" stroke-width="6.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="142" cy="100" r="3.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="118.5" cy="75" r="9.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M108.5,76 Q109,63 118.5,64 Q128,63 128.5,76 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M196,132.5 L200,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M202.5,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="204.5" y1="160" x2="193" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M196,132.5 L192.5,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M195,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="196.5" y1="160" x2="185" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M202.5,134 Q197,103 188,108.5 L189,134 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M193,110 L170,100" fill="none" stroke="#c92a2a" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="170" cy="100" r="2.7" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="191" cy="96.5" r="7.2" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M183.5,97 Q184,87.5 191,88 Q198.5,87.5 198.5,97 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="70" y="75.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="202" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <path d="M412,123 L406.5,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M403,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="401" y1="160" x2="416" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M412,123 L417,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M413.5,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="411" y1="160" x2="426.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M403,125.5 Q410.5,84 422.5,91 L421.5,125.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M416,93.5 L442,100" fill="none" stroke="#1971c2" stroke-width="6.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="442" cy="100" r="3.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="418.5" cy="75" r="9.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M408.5,76 Q409,63 418.5,64 Q428,63 428.5,76 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M496,132.5 L500,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M502.5,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="504.5" y1="160" x2="493" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M496,132.5 L492.5,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M495,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="496.5" y1="160" x2="485" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M502.5,134 Q497,103 488,108.5 L489,134 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M493,110 L470,100" fill="none" stroke="#c92a2a" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="470" cy="100" r="2.7" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="491" cy="96.5" r="7.2" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M483.5,97 Q484,87.5 491,88 Q498.5,87.5 498.5,97 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="370" y="75.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="502" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <rect x="60" y="44" width="96" height="120" rx="14" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-dasharray="8 6"/>
  <rect x="352" y="44" width="200" height="120" rx="14" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-dasharray="8 6"/>
  <line x1="8" y1="192" x2="592" y2="192" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="115" y="300" width="70" height="60" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="330" x2="150" y2="421" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,438 L142,420 L158,420 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="99.5" y="417.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_A$</div></foreignObject>
  <line x1="166" y1="360" x2="166" y2="269" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M166,252 L174,270 L158,270 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="169.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_A$</div></foreignObject>
  <line x1="242.5" y1="316" x2="202" y2="316" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M185,316 L203,308 L203,324 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="219.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{BA}$</div></foreignObject>
  <rect x="395" y="295" width="110" height="70" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="450" y1="330" x2="450" y2="398" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M450,415 L442,397 L458,397 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="350.5" y="394.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_A+\overline{G}_B$</div></foreignObject>
  <line x1="470" y1="365" x2="470" y2="297" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M470,280 L478,298 L462,298 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="496.5" y="261.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_A+\overline{N}_B$</div></foreignObject>
  <foreignObject x="383.5" y="220" width="133" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\overline{F}_{AB}+\overline{F}_{BA}=\overline{0}$</div></foreignObject>
</svg>

```pysahdy
You kick a ball with your foot. What force acts on your foot when it hits the ball?
---
The ball acts on your foot with a force of the same size but opposite direction, the reaction force.
```

## Formula: Newton's first and third laws
Newton's first law is a condition for the sum of the forces acting on an object:
```latex
\Sigma\overline{F} = \overline{0} \ \Leftrightarrow\ \overline{v} = \text{constant}
```
where $\Sigma\overline{F}$ is the vector sum of the forces acting on the object, the **net force** (N), and $\overline{v}$ is the velocity of the object (m/s). Constant velocity means that both the magnitude and the direction of the velocity stay the same; rest, $\overline{v} = \overline{0}$, is also constant velocity.

A net force of zero does not mean that there are no forces, but that they cancel each other. On a car driving along a straight road at constant velocity, the weight and the normal force of the road act in the vertical direction, and the force of the road on the tyres forwards and the air resistance backwards. Because the velocity does not change, the forward force is as large as the air resistance when rolling resistance is ignored.

<svg data-fig="auto" viewBox="0 0 600 330" role="img" aria-label="Two pictures of a car driving along a straight road at constant velocity. On the left the situation picture: the car and above it a thin blue arrow v to the right. On the right the force diagram of the car, the car as a rectangle. The weight G down from the centre and the normal force N of the road up from the bottom surface, equally long. The force F of the road on the tyres starts from the front corner of the bottom surface and points forwards. The air resistance F d is a push backwards: the arrow comes from in front, and its tip is on the front surface, which the air presses on. The horizontal arrows are equally long, so the forces cancel each other." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-auto.webp" x="1.2" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="46" y="9.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation picture}$</div></foreignObject>
  <foreignObject x="205.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="371" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{force diagram}$</div></foreignObject>
  <foreignObject x="423.5" y="245.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="359.5" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="529.5" y="197.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="517.5" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{d}$</div></foreignObject>
</svg>

Newton's third law is written for the forces between two objects:
```latex
\overline{F}_{AB} = -\overline{F}_{BA}
```
where $\overline{F}_{AB}$ is the force with which object A acts on object B (N), and $\overline{F}_{BA}$ is the force with which B acts on A (N). The minus sign tells that the forces are opposite in direction; the magnitudes are the same, $F_{AB} = F_{BA}$.

In calculations the magnitude of the weight is often needed:
```kaavat
weight of a body at the Earth's surface :: G = mg
```
where $G$ is the weight (N), $m$ is the mass of the object (kg) and $g = 9.81\,\text{m/s}^2$ is the acceleration due to gravity. The reaction force of the weight is the equally large gravitational force of the object on the Earth.

## Worked example
A passenger aircraft flies horizontally in a straight line at a constant velocity of $850\,\text{km/h}$. Each of its two jet engines pushes air and exhaust gases backwards with a force of $48\,\text{kN}$. How large is the air resistance on the aircraft?

<!-- vaihe -->

**Given and asked.** The force of one engine on the gases is $F_1 = 48\,\text{kN}$ backwards, there are two engines, and the velocity $850\,\text{km/h}$ stays the same in magnitude and direction. We are asked for the air resistance $F_\text{d}$.

<!-- vaihe -->

**Principle.** By Newton's third law the gases push each engine forwards with an equally large force $F_1$; this is the thrust of the engine. The aircraft flies straight at constant velocity, so by Newton's first law its net force is zero. In the horizontal direction only two thrusts $\overline{F}_1$ and $\overline{F}_2$ act forwards on the aircraft (both $48\,\text{kN}$), and the air resistance $\overline{F}_\text{d}$ acts backwards, so they cancel each other. In the vertical direction the lift of the wings and the weight cancel each other. In the force diagram the aircraft is a rectangle and the forces acting on it are arrows:

<svg data-fig="kone" viewBox="0 0 600 330" role="img" aria-label="Two pictures of a passenger aircraft flying horizontally at constant velocity. On the left the situation picture: the aircraft and above it a thin blue arrow v to the right. On the right the force diagram of the aircraft, the aircraft as a rectangle. The weight G down from the centre and the lift F lift of the wings up, equally long. The thrusts F 1 and F 2 of the two engines start from the front edge of the fuselage and point forwards, and they are equally long. The air resistance F d is a push backwards: the arrow comes from in front, its tip is on the front edge, which the air presses on, and it is as long as the thrusts together. The horizontal forces cancel each other, and the vertical forces cancel each other." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43k-body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <foreignObject x="46" y="9.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation picture}$</div></foreignObject>
  <path d="M44,214 Q40,196 62,192 L226,190 Q262,188 276,176 L262,214 Q150,230 44,214 Z" fill="url(#fy43k-body)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M62,192 L48,150 L74,150 L104,192 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M138,200 L196,200 L120,250 L100,250 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="160" cy="238" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="130" cy="244" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="150" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="170" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="190" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="210" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="230" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="124" y1="128" x2="198" y2="128" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M187,134.5 L200,128 L187,121.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="205.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="371" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{force diagram}$</div></foreignObject>
  <rect x="355" y="136" width="110" height="80" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="410" y1="176" x2="410" y2="239" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M410,256 L402,238 L418,238 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="371.5" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="390" y1="176" x2="390" y2="113" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M390,96 L398,114 L382,114 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="308.5" y="83.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{lift}$</div></foreignObject>
  <line x1="465" y1="178" x2="486.5" y2="178" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M503.5,178 L485.5,186 L485.5,170 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="503" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <line x1="465" y1="206" x2="486.5" y2="206" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M503.5,206 L485.5,214 L485.5,198 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="503" y="195.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <line x1="542" y1="148" x2="482" y2="148" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M465,148 L483,140 L483,156 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="515.5" y="109.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{d}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Formula solved.** Choose the forward direction as positive and solve the air resistance:
```latex
\begin{aligned}
&\Sigma F_x = 2F_1 - F_\text{d} = 0 \\
&F_\text{d} = 2F_1
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The velocity $850\,\text{km/h}$ is not needed: it is enough to know that it does not change. The forces are in kilonewtons, so the result is obtained directly in kilonewtons: $48\,\text{kN} = 48\,000\,\text{N}$.

<!-- vaihe -->

**Substitution.** Substitute the force of the engine with its unit:
```latex
\begin{aligned}
F_\text{d} &= 2F_1 \\
&= 2\cdot 48\,\text{kN} \\
&= 96\,\text{kN}
\end{aligned}
```

<!-- vaihe -->

**Result.** The air resistance is $96\,\text{kN}$, or $9.6\cdot 10^{4}\,\text{N}$, and it points backwards. The engine force $48\,\text{kN}$ is taken as an exact value, so the air resistance $96\,\text{kN}$ is an exact value of this model and needs no rounding.

<!-- vaihe -->

**Reasonableness.** If the air resistance were smaller than the thrusts, the net force would point forwards and the aircraft would accelerate; if it were larger, the aircraft would slow down. Constant velocity is possible only when the air resistance is as large as the sum of the thrusts $2\cdot 48\,\text{kN}$. The same reasoning holds for all constant velocities: the sum of the thrust and the air resistance is always zero. The magnitudes of the forces can still differ at different speeds, because air resistance grows as the speed grows, so a greater constant speed also needs a greater thrust.

## Common misconception
Many people think that a force must act on a moving object in the direction of motion and that the motion ends when this force "wears out". According to the first law this is not so: no force acts forwards on a sliding curling stone, and it slows down only because of friction. Another common error is to think that a force and its reaction force cancel each other. They act on different objects: a horse pulls a cart and the cart pulls the horse, but the motion of the cart is decided only by the forces acting on the cart. A third error is to take the weight of a book resting on a table and the normal force of the table as a force and its reaction force. They are equally large because of the first law. The reaction force of the normal force is the force of the book on the table, and the reaction force of the weight is the gravitational force of the book on the Earth.

## Summary
- A force describes the interaction of two objects. Every force has a cause, another object, and the unit of force is the newton.
- Newton's first law: if the net force is zero, the object stays at rest or moves in a straight line at constant velocity.
- A force is needed to change motion, not to keep it going. In everyday life motion slows down because of friction and air resistance.
- Newton's third law: $\overline{F}_{AB} = -\overline{F}_{BA}$. A force and its reaction force are equally large, opposite in direction and of the same kind, and they act on different objects, so they do not cancel each other.
