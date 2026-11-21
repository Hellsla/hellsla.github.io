# How waves form and travel

> **Why** does a bell hanging on a post ring when the other end of a long rope is flicked once, although nobody touches the bell?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the yard of a summer cottage by a lake. On the left a girl holds the end of a long rope; she has just flicked the rope once. The other end of the rope is tied to a wooden post, from whose arm a brass bell hangs. Halfway along the taut rope there is a single hump on its way towards the post. In the background are the lake, the wooded shore, a red cottage, a sauna and birches." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A wave is a travelling disturbance
When the end of a rope is flicked upwards, the hand pulls the nearest point of the rope along with it. The taut rope in turn pulls the next point, and that pulls the next one, so every point starts to move a little later than the one before. In this way the displacement from the equilibrium position, the disturbance, travels along the rope away from the hand. **Mechanical wave motion** is the propagation of a disturbance in a medium. The particles of the medium vibrate only around their equilibrium positions and do not travel with the wave. In a gas the molecules also move randomly because of thermal motion, but the wave does not carry them along. So in the ideal wave model a wave carries energy away from the source, but not matter. This is why the bell at the other end of the rope can ring although no point of the rope travels all the way from the hand to the bell. Real waves can also carry a little matter: in a water surface wave, for example, the water particles move round almost closed paths, but a floating object drifts slowly in the direction of the wave.

A mechanical wave needs a medium, such as a rope, a spring, water or air. One flick makes a **pulse**, a single hump that travels along the rope. When the hand is moved steadily up and down, a periodic wave forms, in which crests and troughs repeat. Every point of the rope then vibrates with the same frequency $f$ as the hand. Period $T$, frequency $f$ and amplitude $A$ mean the same as in the chapter *Describing oscillation: period, frequency and amplitude*. When the wave reaches the end of the rope, it is reflected back; reflection is studied in the chapter *A wave meets an obstacle or a gap*.

```pysahdy
A hand shakes the end of a rope with frequency $2.0\,\text{Hz}$. With what frequency does a point of the rope one metre from the hand vibrate?
---
It vibrates with the same frequency, $2.0\,\text{Hz}$. Every point of the rope vibrates with the same frequency as the hand, even though it starts moving a little later.
```

### Transverse and longitudinal waves
Waves are divided into two kinds according to the direction in which the particles of the medium vibrate. In a **transverse wave** the particles vibrate perpendicular to the direction of travel of the wave: the points of the rope move up and down while the wave travels horizontally. In a **longitudinal wave** the particles vibrate parallel to the direction of travel. When the end of a long coil spring is pushed back and forth, compressions form in the spring, where the coils are close together, and rarefactions, where they are far apart. The compressions and rarefactions travel along, but each coil only swings back and forth around its own place. Sound in air, for example, is a longitudinal wave.

<svg data-fig="types" viewBox="0 0 600 412" role="img" aria-label="Schematic diagram, not to scale. At the top a transverse wave: the rope has the shape of a sine wave, and a blue arrow points to the right for the direction of travel of the wave. At three points of the rope a vertical double-headed arrow shows that the point moves up and down, that is, perpendicular to the direction of travel. At the bottom a longitudinal wave: the coils of a long coil spring are close together in places (compression) and far apart in places (rarefaction). Above one coil a horizontal double-headed arrow shows that the coil moves back and forth along the spring. A blue arrow points to the right for the direction of travel of this wave too." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-types.webp" x="0" y="0" width="600" height="420" preserveAspectRatio="none"/>
  <foreignObject x="24" y="9.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{transverse wave}$</div></foreignObject>
  <foreignObject x="412" y="9.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="18.5" y="169.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{motion of a point}$</div></foreignObject>
  <foreignObject x="24" y="211.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{longitudinal wave}$</div></foreignObject>
  <foreignObject x="412" y="211.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="165" y="247.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{motion of a coil}$</div></foreignObject>
  <foreignObject x="87.5" y="339.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{compression}$</div></foreignObject>
  <foreignObject x="287.5" y="339.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{compression}$</div></foreignObject>
  <foreignObject x="187.5" y="369.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rarefaction}$</div></foreignObject>
  <foreignObject x="387.5" y="369.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rarefaction}$</div></foreignObject>
</svg>

```pysahdy
The end of a coil spring is pushed back and forth. In which direction do the coils vibrate compared with the direction in which the wave travels?
---
Parallel to the direction of travel. The wave is therefore longitudinal: the compressions travel along, but each coil only swings back and forth in place.
```

## Formula: The fundamental equation of wave motion
The **wavelength** $\lambda$ is the distance between two successive crests or two successive compressions. It is the shortest distance between two points that move in exactly the same way. When the source makes one full vibration, that is, during one period $T$, the wave travels exactly one wavelength. The four moments in the figure show how each quarter of a period takes the wave a quarter of a wavelength further.

<svg data-fig="birth" viewBox="0 0 600 420" role="img" aria-label="Schematic diagram: the end of a rope starts to shake up and down, and the rope is drawn in four pictures one below the other at the moments a quarter of a period, a half, three quarters and a whole period. A dashed line shows how far the wave has travelled at each moment: a quarter of a wavelength, a half, three quarters and a whole wavelength. Below the lowest picture a measuring bar shows that during one period the wave has travelled one wavelength. Behind the front the rope is at rest." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-birth.webp" x="0" y="0" width="600" height="425" preserveAspectRatio="none"/>
  <foreignObject x="40" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{1}{4}T$</div></foreignObject>
  <foreignObject x="40" y="125.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{1}{2}T$</div></foreignObject>
  <foreignObject x="40" y="207.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{3}{4}T$</div></foreignObject>
  <foreignObject x="53" y="289.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = T$</div></foreignObject>
  <foreignObject x="442" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="270" y="371.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
</svg>

So the speed of the wave is the wavelength divided by the period. Since the frequency is $f = \tfrac{1}{T}$, we get the **fundamental equation of wave motion**
```kaavat
wave equation :: v = \frac{\lambda}{T} = f\lambda
```
where $v$ is the speed of propagation of the wave ($\text{m/s}$), $\lambda$ the wavelength ($\text{m}$), $T$ the period ($\text{s}$) and $f$ the frequency ($\text{Hz}$). The units agree, because $1\,\text{Hz} = 1\,\text{s}^{-1}$, so $1\,\text{Hz} \cdot 1\,\text{m} = 1\,\text{m/s}$. The speed of a pulse can also be measured directly: a pulse travels at a steady speed in the same medium, so $v = \tfrac{s}{t}$, where $s$ is the distance and $t$ the time it takes.

```pysahdy
A wave has wavelength $0.50\,\text{m}$ and period $0.25\,\text{s}$. What is the speed of the wave?
---
The speed is $v = \tfrac{\lambda}{T}$, so $\tfrac{0.50\,\text{m}}{0.25\,\text{s}} = 2.0\,\text{m/s}$.
```

### The speed depends on the medium, the frequency on the source
The speed of a wave is determined by the properties of the medium. In a taut rope a wave travels faster than in a slack one, and sound travels in air at $20\,{}^\circ\text{C}$ at about $343\,\text{m/s}$ but in water at about $1500\,\text{m/s}$. The frequency is determined by the source: it is the frequency of the vibration of the hand, the end of the spring or the loudspeaker. In an ideal rope the speed of the wave is determined by the tension and the mass per unit length of the rope, so it does not depend on the frequency or on a small amplitude; likewise in air the speed of sound practically does not depend on the frequency. This is not a general law for all waves: the speed of water surface waves, for example, can depend on the wavelength, and such a wave is called dispersive. The very long wave of a tsunami, again, travels the faster the deeper the sea is. When the same rope is shaken more rapidly, the speed stays the same and the wavelength gets shorter: doubling the frequency halves the wavelength. When a wave passes from one medium to another, the frequency stays the same, but the speed and the wavelength change.

### A snapshot and a graph of one point
A wave can be described by two graphs that look like similar sine waves. A **snapshot**, the $(x, y)$ graph, shows the shape of the whole rope at one moment: the horizontal axis shows the position $x$, and the distance between two crests is the wavelength $\lambda$. A **graph of one point**, the $(t, y)$ graph, shows the displacement $y$ of one point of the rope as a function of time: the horizontal axis shows the time $t$, and the distance between two peaks is the period $T$. The amplitude $A$ can be read from either graph. So always read first which quantity is on the horizontal axis.

<svg data-fig="graphs" viewBox="0 0 600 556" role="img" aria-label="Two graphs of the same wave one below the other, amplitude 4 cm. The upper one is a snapshot of the whole rope at one moment: the horizontal axis shows the position x in metres from zero to 2.5 metres and the vertical axis the displacement y in centimetres. The distance between two successive crests, 1.0 m, is marked as the wavelength lambda and the height of the crest as the amplitude A. The lower one is the displacement of one point of the rope as a function of time: the horizontal axis shows the time t in seconds from zero to 1.25 seconds. The distance between two successive peaks, 0.50 s, is marked as the period T. The graphs look the same in shape, but the quantities on their horizontal axes are different." style="max-width:100%;font-size:24px">
  <foreignObject x="24" y="7.5" width="407" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{snapshot: the whole rope at one moment}$</div></foreignObject>
  <foreignObject x="24" y="295.5" width="482" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{one point: displacement as a function of time}$</div></foreignObject>
  <line x1="12" y1="282" x2="588" y2="282" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="172" y1="236" x2="172" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="236" x2="248" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="236" x2="324" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="236" x2="400" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="236" x2="476" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="214" x2="476" y2="214" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="126" x2="476" y2="126" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="236" x2="96" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="170" x2="490" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,170 L489,176 L489,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="171" x2="96" y2="90" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,78 L102,91 L90,91 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="172" y1="170" x2="172" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248" y1="170" x2="248" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="170" x2="324" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="170" x2="400" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="170" x2="476" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="214" x2="96" y2="214" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="199.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-4$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="126" x2="96" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="111.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="508" y="155.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="86" y="47.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y\ (\text{cm})$</div></foreignObject>
  <foreignObject x="149.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0.5$</div></foreignObject>
  <foreignObject x="238" y="241.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="301.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1.5$</div></foreignObject>
  <foreignObject x="390" y="241.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2$</div></foreignObject>
  <foreignObject x="453.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2.5$</div></foreignObject>
  <polyline points="96,170 99,164.5 102.5,158.5 105.5,153 108.5,148 112,143 115,139 118,135 121.5,132 124.5,129.5 127.5,127.5 131,126.5 134,126 137,126.5 140.5,127.5 143.5,129.5 146.5,132 150,135 153,139 156,143 159.5,148 162.5,153 165.5,158.5 169,164.5 172,170 175,175.5 178.5,181.5 181.5,187 184.5,192 188,197 191,201 194,205 197.5,208 200.5,210.5 203.5,212.5 207,213.5 210,214 213,213.5 216.5,212.5 219.5,210.5 222.5,208 226,205 229,201 232,197 235.5,192 238.5,187 241.5,181.5 245,175.5 248,170 251,164.5 254.5,158.5 257.5,153 260.5,148 264,143 267,139 270,135 273.5,132 276.5,129.5 279.5,127.5 283,126.5 286,126 289,126.5 292.5,127.5 295.5,129.5 298.5,132 302,135 305,139 308,143 311.5,148 314.5,153 317.5,158.5 321,164.5 324,170 327,175.5 330.5,181.5 333.5,187 336.5,192 340,197 343,201 346,205 349.5,208 352.5,210.5 355.5,212.5 359,213.5 362,214 365,213.5 368.5,212.5 371.5,210.5 374.5,208 378,205 381,201 384,197 387.5,192 390.5,187 393.5,181.5 397,175.5 400,170 403,164.5 406.5,158.5 409.5,153 412.5,148 416,143 419,139 422,135 425.5,132 428.5,129.5 431.5,127.5 435,126.5 438,126 441,126.5 444.5,127.5 447.5,129.5 450.5,132 454,135 457,139 460,143 463.5,148 466.5,153 469.5,158.5 473,164.5 476,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="134" y1="113" x2="286" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="134" y1="105" x2="134" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="105" x2="286" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="200" y="78.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <line x1="134" y1="126" x2="134" y2="121" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="286" y1="126" x2="286" y2="121" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="134" y1="170" x2="134" y2="135" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M134,126 L138.5,136 L129.5,136 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="141" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="172" y1="522" x2="172" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="522" x2="248" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="522" x2="324" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="522" x2="400" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="522" x2="476" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="500" x2="476" y2="500" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="412" x2="476" y2="412" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="522" x2="96" y2="456" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="456" x2="490" y2="456" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,456 L489,462 L489,450 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="457" x2="96" y2="376" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,364 L102,377 L90,377 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="172" y1="456" x2="172" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248" y1="456" x2="248" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="456" x2="324" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="456" x2="400" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="456" x2="476" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="500" x2="96" y2="500" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="485.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-4$</div></foreignObject>
  <line x1="89" y1="456" x2="96" y2="456" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="441.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="412" x2="96" y2="412" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="397.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="508" y="441.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="333.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y\ (\text{cm})$</div></foreignObject>
  <foreignObject x="143" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0.25$</div></foreignObject>
  <foreignObject x="225.5" y="527.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0.5$</div></foreignObject>
  <foreignObject x="295" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0.75$</div></foreignObject>
  <foreignObject x="390" y="527.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="447" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1.25$</div></foreignObject>
  <polyline points="96,456 99,450.5 102.5,444.5 105.5,439 108.5,434 112,429 115,425 118,421 121.5,418 124.5,415.5 127.5,413.5 131,412.5 134,412 137,412.5 140.5,413.5 143.5,415.5 146.5,418 150,421 153,425 156,429 159.5,434 162.5,439 165.5,444.5 169,450.5 172,456 175,461.5 178.5,467.5 181.5,473 184.5,478 188,483 191,487 194,491 197.5,494 200.5,496.5 203.5,498.5 207,499.5 210,500 213,499.5 216.5,498.5 219.5,496.5 222.5,494 226,491 229,487 232,483 235.5,478 238.5,473 241.5,467.5 245,461.5 248,456 251,450.5 254.5,444.5 257.5,439 260.5,434 264,429 267,425 270,421 273.5,418 276.5,415.5 279.5,413.5 283,412.5 286,412 289,412.5 292.5,413.5 295.5,415.5 298.5,418 302,421 305,425 308,429 311.5,434 314.5,439 317.5,444.5 321,450.5 324,456 327,461.5 330.5,467.5 333.5,473 336.5,478 340,483 343,487 346,491 349.5,494 352.5,496.5 355.5,498.5 359,499.5 362,500 365,499.5 368.5,498.5 371.5,496.5 374.5,494 378,491 381,487 384,483 387.5,478 390.5,473 393.5,467.5 397,461.5 400,456 403,450.5 406.5,444.5 409.5,439 412.5,434 416,429 419,425 422,421 425.5,418 428.5,415.5 431.5,413.5 435,412.5 438,412 441,412.5 444.5,413.5 447.5,415.5 450.5,418 454,421 457,425 460,429 463.5,434 466.5,439 469.5,444.5 473,450.5 476,456" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="134" y1="399" x2="286" y2="399" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="134" y1="391" x2="134" y2="407" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="391" x2="286" y2="407" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="200" y="364.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="134" y1="412" x2="134" y2="407" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="286" y1="412" x2="286" y2="407" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="134" y1="456" x2="134" y2="421" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M134,412 L138.5,422 L129.5,422 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="141" y="431.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
</svg>

## Worked example
A long rope is stretched taut across a yard. When the end of the rope is flicked once, the pulse travels a distance of $6.0\,\text{m}$ in $2.5\,\text{s}$. Then the same rope is shaken steadily at a frequency of $3.0\,\text{Hz}$, and the tension of the rope does not change. What is the wavelength of the wave that forms?

<!-- vaihe -->

**Given and find.** The distance travelled by the pulse is $s = 6.0\,\text{m}$ and the time taken is $t = 2.5\,\text{s}$; the frequency of the periodic wave is $f = 3.0\,\text{Hz}$.

We are asked for the wavelength $\lambda$.

<!-- vaihe -->

**Principle.** The speed of a wave depends on the properties of the medium, here the tension of the rope and its mass per unit length, not on whether a pulse or a periodic wave is made in the rope.

So the periodic wave travels at the same speed $v$ as the pulse, and the pulse travels steadily, so $v = \tfrac{s}{t}$. The wavelength then follows from the fundamental equation $v = f\lambda$.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&v = \frac{s}{t} \quad\text{and}\quad v = f\lambda \\
&\lambda = \frac{v}{f} = \frac{s}{f\,t}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the distance is in metres and the time in seconds, and $1\,\text{Hz} = 1\,\text{s}^{-1}$, so $\tfrac{\text{m/s}}{\text{Hz}} = \text{m}$.

<!-- vaihe -->

**Substitution.** First we calculate the speed and then the wavelength:
```latex
\begin{aligned}
&v = \frac{s}{t} \\
&= \frac{6.0\,\text{m}}{2.5\,\text{s}} = 2.4\,\text{m/s} \\[6pt]
&\lambda = \frac{v}{f} \\
&= \frac{2.4\,\text{m/s}}{3.0\,\text{Hz}} = 0.80\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Result.** The wavelength is $0.80\,\text{m}$. The answer is given with two significant figures like the initial values $6.0\,\text{m}$, $2.5\,\text{s}$ and $3.0\,\text{Hz}$.

<!-- vaihe -->

**Reasonableness.** The period is $T = \tfrac{1}{f} = 0.333\,\text{s}$, and in that time the wave travels $2.4\,\text{m/s} \cdot 0.333\,\text{s} = 0.80\,\text{m}$, exactly one wavelength, as it should.

## Common misconception
Many people think that a wave travels faster the more rapidly the hand is shaken. In the same rope, however, the speed stays the same. When the frequency increases from $1.0\,\text{Hz}$ to $2.0\,\text{Hz}$, the wavelength shortens from $2.0\,\text{m}$ to $1.0\,\text{m}$, and the product $f\lambda$ is still $2.0\,\text{m/s}$. The speed can be changed only by changing the rope or its tension, for example by tightening the rope.

Another common mistake is to read the wavelength from the graph of one point, the $(t, y)$ graph. There the distance between peaks is the period $T$ in seconds, not the wavelength. A third mistake is to think that the wave carries the matter of the rope along: the points of the rope only vibrate in place, and it is energy that moves forward.

## Summary
- Mechanical wave motion is the propagation of a disturbance in a medium. The particles of the medium vibrate around their equilibrium positions, and the ideal wave carries energy but not matter.
- In a transverse wave the particles vibrate perpendicular to the direction of travel (rope), in a longitudinal wave parallel to it (coil spring, sound in air).
- One flick makes a pulse, steady shaking makes a periodic wave. The wavelength $\lambda$ is the distance between two successive crests.
- The fundamental equation of wave motion is $v = \tfrac{\lambda}{T} = f\lambda$. The speed depends on the medium, the frequency on the source.
- The wavelength is read from a snapshot, the $(x, y)$ graph, and the period from the graph of one point, the $(t, y)$ graph.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a stadium stand. Spectators sit in three rows, and in the middle a group of spectators has stood up with their arms raised. Next to those standing, spectators are half risen or just sitting down. The spectators do not change places, but the place where they stand up travels round the stand." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
