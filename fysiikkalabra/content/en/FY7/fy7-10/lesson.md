# Reflection and refraction of light

> **Why** does a straw in a glass of water seem to break exactly at the surface of the water?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a kitchen table there is a glass of water with a striped straw in it. The part of the straw that is in the water seems to be shifted sideways, so the straw seems to break at the surface of the water. Behind it is a window with the sun shining in." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Light travels as rays
Light is electromagnetic wave motion (chapter *Electromagnetic radiation and the black-body spectrum*). In a uniform material such as air, water or glass, light travels in a straight line. The path of light is described by **rays**: a ray is a line that shows the direction in which light travels. When light meets the boundary between two materials, part of it is **reflected** back into the same material and part continues into the other material. Light that passes through the boundary usually changes direction: it is **refracted**. Angles are always measured from the **normal** of the boundary, the straight line that is perpendicular to the boundary at the point where the ray hits it. The angle between the incident ray and the normal is the angle of incidence $\alpha_1$, the angle of the reflected ray is the angle of reflection $\beta$, and the angle of the refracted ray is the angle of refraction $\alpha_2$.

<svg data-fig="interface" viewBox="0 0 600 360" role="img" aria-label="Schematic picture, angles to scale: a ray of light arrives from the air at the surface of water. A grey dashed line, the normal, is drawn at the point of incidence perpendicular to the surface. The incident ray comes from the upper left at the angle alpha 1, which is 50 degrees, from the normal. A thinner reflected ray leaves to the upper right at an equal angle beta. The refracted ray continues into the water to the lower right at the angle alpha 2, which is 35 degrees, so it has been refracted towards the normal." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-interface.webp" x="1.2" y="1.2" width="597" height="368.2" preserveAspectRatio="none"/>
  <foreignObject x="246.5" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_1$</div></foreignObject>
  <foreignObject x="327" y="77.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\beta$</div></foreignObject>
  <foreignObject x="313" y="259" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_2$</div></foreignObject>
  <foreignObject x="52" y="38" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e64980">$\text{incident}$</div></foreignObject>
  <foreignObject x="380" y="38" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e64980">$\text{reflected}$</div></foreignObject>
  <foreignObject x="398.5" y="288" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$\text{refracted}$</div></foreignObject>
  <foreignObject x="207" y="315.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{normal}$</div></foreignObject>
  <foreignObject x="28" y="135.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{air},\ n_1$</div></foreignObject>
  <foreignObject x="28" y="189.5" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{water},\ n_2$</div></foreignObject>
</svg>

### The law of reflection
Light is reflected in the same way as the mechanical waves in the chapter *A wave meets an obstacle or a gap*: the angle of reflection is equal to the angle of incidence, and the incident ray, the reflected ray and the normal lie in the same plane. A smooth surface, such as a mirror or the still surface of water, reflects parallel rays as parallel rays, so an image can be seen in it. On a rough surface, such as paper, the normal points in a different direction at every point. The surface therefore reflects light in all directions, and the paper can be seen from any direction. The law of reflection still holds at every small point of the surface.

### Light slows down in a material
In a vacuum light travels at the speed $c = 3.00 \cdot 10^{8}\,\text{m/s}$. In a material light travels more slowly. The **refractive index** $n$ of a material tells how many times more slowly: in water the speed of light is about $2.26 \cdot 10^{8}\,\text{m/s}$, so the refractive index of water is $1.33$. The refractive index of air is $1.0003$, so in air light travels almost as fast as in a vacuum. A material with a greater refractive index is **optically denser**. When light passes from one material to another, its frequency does not change, because the frequency is set by the source of the light. The speed does change, so the wavelength changes too according to the equation $v = f \lambda$: in water the wavelength is $1.33$ times shorter than in air.

```pysahdy
Light passes from air into water. Does its frequency change, and does its wavelength change?
---
The frequency does not change, because the light source sets it. The wavelength gets shorter: in water it is $1.33$ times shorter than in air, because the speed decreases and $v = f \lambda$.
```

### Why light is refracted
Refraction is caused by the change in speed. In the figure, the wavefronts of a wave arriving obliquely at the boundary are parallel lines, and the ray is perpendicular to them. The left end of the front reaches the water first and slows down, while the right end still travels faster in the air. The front therefore turns, and in the water the wave travels in a new direction, closer to the normal. In the water the fronts are also closer together, because the wavelength is shorter. When light arrives perpendicular to the boundary, $\alpha_1 = 0^\circ$, every part of the front slows down at the same moment, and the direction does not change.

<svg data-fig="wavefronts" viewBox="0 0 600 360" role="img" aria-label="Schematic picture, to scale, with the refractive index of water 1.33: a light wave arrives obliquely from the air at the surface of water. The wavefronts are parallel lines perpendicular to the ray. In the air the distance between the fronts is the wavelength lambda 1. The left end of the front is already in the water while the right end is still in the air. In the water the fronts are closer together, the wavelength lambda 2 is shorter, and the fronts have turned so that the ray travels closer to the normal." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-wavefronts.webp" x="2.5" y="2.5" width="594.1" height="365.1" preserveAspectRatio="none"/>
  <foreignObject x="309.5" y="31" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda_1$</div></foreignObject>
  <foreignObject x="219.5" y="292.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda_2$</div></foreignObject>
  <foreignObject x="28" y="31.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{air}$</div></foreignObject>
  <foreignObject x="28" y="307.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{water}$</div></foreignObject>
</svg>

### Towards the normal or away from it
When light passes into an optically denser material, for example from air into water, it is refracted **towards the normal**: the angle of refraction is smaller than the angle of incidence. When light passes into an optically less dense material, for example from water into air, it is refracted **away from the normal**. The path of light is reversible: if a ray travels from air into water along a certain path, a ray coming from the water into the air can travel the same path back. The greater the difference between the refractive indices, the more the ray is refracted at the same angle of incidence. This is why diamond, with a refractive index of $2.42$, bends light much more than water does.

### Partial reflection
Usually, at the boundary between two transparent substances, part of the light is reflected and part passes through the boundary. There are exceptions, however: in total internal reflection no refracted ray travels into the second substance (chapter *Total internal reflection and optical fibre*), and at Brewster's angle a certain direction of polarisation of light is not reflected (chapter *Polarisation of light*).

When light arrives perpendicular to glass from air, about $4\,\%$ of the light is reflected from each surface of the glass, and about $2\,\%$ from the surface of water. The greater the angle of incidence, that is, the more the light grazes the surface, the greater the share that is reflected. This is why the surface of a lake mirrors the trees on the shore in the evening, although the bottom can be seen when you look straight down. In the evening you can see a reflection of your own room in a window, because little light comes from outside and the light from the room that hits the glass is partly reflected back. The reflected and transmitted parts together equal the incident light when the material does not absorb light.

### Apparent depth
When you look at a coin at the bottom of a swimming pool, the rays from the coin are refracted away from the normal at the surface of the water. The eye and the brain interpret the light as having come along a straight line. When the rays that reach the eye are extended backwards into the water, they seem to start from a point that is higher than the coin. This is why the pool looks shallower than it is, and the coin seems to be closer to the surface. For the same reason the part of a straw that is in the water seems to be raised when the glass is looked at obliquely from above through the surface, and the straw seems to break at the surface. Because you look obliquely, the raised part also appears shifted sideways.

<svg data-fig="depth" viewBox="0 0 600 360" role="img" aria-label="Schematic picture, angles for the refractive index of water 1.33: cross-section of a swimming pool. There is a coin on the bottom on the left. Two rays leave it obliquely upwards to the right. At the surface of the water the rays are refracted away from the normal and continue to the eye at the upper right. The extensions of the rays are drawn as grey dashed lines back into the water: they meet above the coin, and at that point the eye sees the coin. The coin seems to be closer to the surface than it really is." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-depth.webp" x="1.2" y="1.2" width="597" height="368.2" preserveAspectRatio="none"/>
  <foreignObject x="170" y="289.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{coin}$</div></foreignObject>
  <foreignObject x="55" y="179" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{apparent position}$</div></foreignObject>
  <foreignObject x="28" y="77.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{air}$</div></foreignObject>
  <foreignObject x="502" y="281.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{water}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/pencil-in-water.webp" alt="A blue pencil leaning in a glass of water against a grey wall; at the water surface the pencil seems to break and shift sideways."><figcaption>A pencil in a glass of water looks broken. Light from the part of the pencil under water is refracted as it passes from the water through the glass into the air, so we see the pencil in a different place from where it is.</figcaption></figure>

## Formula: Law of reflection and law of refraction
The law of reflection: the angle of reflection is equal to the angle of incidence,
```latex
\beta = \alpha_1
```
where $\beta$ is the angle of reflection and $\alpha_1$ the angle of incidence, both measured from the normal of the boundary.

The refractive index of a material is the ratio of the speed of light in a vacuum to the speed of light in the material:
```kaavat
refractive index for electromagnetic waves (light) :: n = \frac{c}{v}
```
where $c = 3.00 \cdot 10^{8}\,\text{m/s}$ is the speed of light in a vacuum and $v$ the speed of light in the material (m/s). The refractive index has no unit, and for materials transparent to visible light it is always greater than $1$.

```pysahdy
The speed of light in a vacuum is $3.00 \cdot 10^{8}\,\text{m/s}$ and the refractive index of diamond is $2.42$. How fast does light travel in diamond?
---
The speed is $v = c : n = 3.00 \cdot 10^{8}\,\text{m/s} : 2.42 \approx 1.24 \cdot 10^{8}\,\text{m/s}$.
```

### The law of refraction, or Snell's law
When light passes from a material with refractive index $n_1$ into a material with refractive index $n_2$, the angle of incidence and the angle of refraction satisfy the equation
```kaavat
law of refraction (Snell's law) :: n_1 \sin \alpha_1 = n_2 \sin \alpha_2
```
where $\alpha_1$ is the angle of incidence and $\alpha_2$ the angle of refraction, both measured from the normal. The law follows from the turning of the wavefronts: the ratio of the sines of the angles is the same as the ratio of the speeds, $\sin\alpha_1 : \sin\alpha_2 = v_1 : v_2 = n_2 : n_1$. The law concerns the sines of the angles, not the angles: when the angle of incidence doubles, the angle of refraction does not double. In the graph the angle of refraction increases with the angle of incidence, but more and more slowly.

<svg data-fig="graph" viewBox="0 0 600 360" role="img" aria-label="Graph, to scale: the angle of refraction alpha 2 as a function of the angle of incidence alpha 1, when light arrives from air, with refractive index 1.00, into water (refractive index 1.33) and into diamond (2.42). Both curves run below the line alpha 2 = alpha 1, so the ray is refracted towards the normal. The curves bend flatter: at an angle of incidence of 90 degrees the angle of refraction is 48.8 degrees in water and 24.4 degrees in diamond. The dashed line alpha 2 = alpha 1 shows the situation in which the materials have the same refractive index." style="max-width:100%;font-size:24px">
  <line x1="128.5" y1="306" x2="128.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="165" y1="306" x2="165" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="201.5" y1="306" x2="201.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="238" y1="306" x2="238" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274" y1="306" x2="274" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310.5" y1="306" x2="310.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="347" y1="306" x2="347" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383.5" y1="306" x2="383.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="306" x2="420" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="278" x2="420" y2="278" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="250.5" x2="420" y2="250.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="222.5" x2="420" y2="222.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="195" x2="420" y2="195" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="167" x2="420" y2="167" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="139.5" x2="420" y2="139.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="111.5" x2="420" y2="111.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="84" x2="420" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="56" x2="420" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="306" x2="434" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,306 L433,312 L433,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="307" x2="92" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,30 L98,43 L86,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="128.5" y1="306" x2="128.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="165" y1="306" x2="165" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201.5" y1="306" x2="201.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="185" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="238" y1="306" x2="238" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="274" y1="306" x2="274" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="310.5" y1="306" x2="310.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="294" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="347" y1="306" x2="347" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="383.5" y1="306" x2="383.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="306" x2="420" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="403.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$90$</div></foreignObject>
  <line x1="85" y1="278" x2="92" y2="278" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="250.5" x2="92" y2="250.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="222.5" x2="92" y2="222.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="208" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="85" y1="195" x2="92" y2="195" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="167" x2="92" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="139.5" x2="92" y2="139.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="125" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="85" y1="111.5" x2="92" y2="111.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="84" x2="92" y2="84" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="56" x2="92" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="41.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$90$</div></foreignObject>
  <foreignObject x="62" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="291.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_1\ (^\circ)$</div></foreignObject>
  <foreignObject x="82" y="-0.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_2\ (^\circ)$</div></foreignObject>
  <polyline points="92,306 420,56" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="92,306 94.5,304.5 97.5,303 100,301.5 103,299.5 105.5,298 108.5,296.5 111,295 114,293.5 116.5,292 119.5,290.5 122,289 125,287 127.5,285.5 130.5,284 133,282.5 135.5,281 138.5,279.5 141,278 144,276.5 146.5,275 149.5,273.5 152,271.5 155,270 157.5,268.5 160.5,267 163,265.5 166,264 168.5,262.5 171.5,261 174,259.5 176.5,258 179.5,256.5 182,255 185,253.5 187.5,252 190.5,250.5 193,249 196,247.5 198.5,246 201.5,244.5 204,243 207,241.5 209.5,240.5 212.5,239 215,237.5 217.5,236 220.5,234.5 223,233 226,231.5 228.5,230.5 231.5,229 234,227.5 237,226 239.5,225 242.5,223.5 245,222 248,221 250.5,219.5 253.5,218 256,217 258.5,215.5 261.5,214 264,213 267,211.5 269.5,210.5 272.5,209 275,208 278,206.5 280.5,205.5 283.5,204.5 286,203 289,202 291.5,201 294.5,199.5 297,198.5 299.5,197.5 302.5,196.5 305,195 308,194 310.5,193 313.5,192 316,191 319,190 321.5,189 324.5,188 327,187.5 330,186.5 332.5,185.5 335.5,184.5 338,184 340.5,183 343.5,182 346,181.5 349,180.5 351.5,180 354.5,179 357,178.5 360,178 362.5,177 365.5,176.5 368,176 371,175.5 373.5,175 376.5,174.5 379,174 381.5,173.5 384.5,173 387,173 390,172.5 392.5,172 395.5,172 398,171.5 401,171.5 403.5,171 406.5,171 409,171 412,170.5 414.5,170.5 417.5,170.5 420,170.5" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,306 94.5,305 97.5,304.5 100,303.5 103,302.5 105.5,301.5 108.5,301 111,300 114,299 116.5,298.5 119.5,297.5 122,296.5 125,295.5 127.5,295 130.5,294 133,293 135.5,292.5 138.5,291.5 141,290.5 144,290 146.5,289 149.5,288 152,287.5 155,286.5 157.5,285.5 160.5,285 163,284 166,283 168.5,282.5 171.5,281.5 174,280.5 176.5,280 179.5,279 182,278.5 185,277.5 187.5,276.5 190.5,276 193,275 196,274.5 198.5,273.5 201.5,273 204,272 207,271.5 209.5,270.5 212.5,270 215,269 217.5,268.5 220.5,267.5 223,267 226,266 228.5,265.5 231.5,265 234,264 237,263.5 239.5,263 242.5,262 245,261.5 248,261 250.5,260 253.5,259.5 256,259 258.5,258 261.5,257.5 264,257 267,256.5 269.5,255.5 272.5,255 275,254.5 278,254 280.5,253.5 283.5,253 286,252.5 289,251.5 291.5,251 294.5,250.5 297,250 299.5,249.5 302.5,249 305,248.5 308,248 310.5,248 313.5,247.5 316,247 319,246.5 321.5,246 324.5,245.5 327,245 330,245 332.5,244.5 335.5,244 338,243.5 340.5,243.5 343.5,243 346,242.5 349,242.5 351.5,242 354.5,241.5 357,241.5 360,241 362.5,241 365.5,240.5 368,240.5 371,240 373.5,240 376.5,240 379,239.5 381.5,239.5 384.5,239 387,239 390,239 392.5,239 395.5,238.5 398,238.5 401,238.5 403.5,238.5 406.5,238.5 409,238.5 412,238.5 414.5,238 417.5,238 420,238" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="430" y="156" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{water}$</div></foreignObject>
  <foreignObject x="430" y="223.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$\text{diamond}$</div></foreignObject>
  <foreignObject x="430" y="45.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\alpha_2 = \alpha_1$</div></foreignObject>
  <foreignObject x="106.5" y="69.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_1 = 1.00$</div></foreignObject>
</svg>

```pysahdy
A ray of light comes from air ($n = 1.00$) into window glass ($n = 1.52$) at an angle of incidence of $40^\circ$. What is the angle of refraction, and is the ray refracted towards the normal or away from it?
---
From Snell's law $\sin\alpha_2 = 1.00 \cdot \sin 40^\circ : 1.52 = 0.423$, so $\alpha_2 \approx 25^\circ$. Glass is optically denser, so the ray is refracted towards the normal.
```

### Refractive indices
The refractive index depends slightly on the wavelength of light (chapter *Dispersion: the prism and the rainbow*). The values in the table are for yellow light with a wavelength of $589\,\text{nm}$ and for the material at room temperature. The refractive indices of glass and acrylic vary with the quality.

| material | $n$ |
| --- | --- |
| air | $1.0003$ |
| water | $1.33$ |
| ethanol | $1.36$ |
| acrylic | $1.49$ |
| window glass | $1.52$ |
| diamond | $2.42$ |

Source: *CRC Handbook of Chemistry and Physics*, 97th edition, 2016; the values for glass and acrylic are typical values. In calculations the refractive index of air is taken to be $1.00$.

## Worked example
A laser beam arrives from the air at the surface of the water in a tank at an angle of incidence of $55.0^\circ$. What is the angle of refraction in the water, and at what speed does light travel in the water? The refractive index of air is $1.00$ and that of water $1.33$.

<!-- vaihe -->

**Given and find.** Angle of incidence $\alpha_1 = 55.0^\circ$, refractive index of air $n_1 = 1.00$, refractive index of water $n_2 = 1.33$ and speed of light in a vacuum $c = 3.00 \cdot 10^{8}\,\text{m/s}$. We are asked for the angle of refraction $\alpha_2$ and the speed of light in water $v$.

<!-- vaihe -->

**Principle.** Light passes from air into water, so it is refracted at the boundary according to the law of refraction. Water is optically denser, so the ray is refracted towards the normal. The speed of light in water follows from the definition of the refractive index, $n = c : v$.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&n_1 \sin\alpha_1 = n_2 \sin\alpha_2 \\
&\sin\alpha_2 = \frac{n_1 \sin\alpha_1}{n_2} \\[6pt]
&n_2 = \frac{c}{v} \;\Rightarrow\; v = \frac{c}{n_2}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the refractive indices have no unit, and the angle is in degrees. The speed comes out in the same unit as $c$, metres per second.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\sin\alpha_2 = \frac{n_1 \sin\alpha_1}{n_2} \\
&= \frac{1.00 \cdot \sin 55.0^\circ}{1.33} \\
&= 0.6159 \\
&\alpha_2 = 38.02^\circ \\[6pt]
&v = \frac{c}{n_2} \\
&= \frac{3.00 \cdot 10^{8}\,\text{m/s}}{1.33} \\
&= 2.256 \cdot 10^{8}\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Result.** The angle of refraction is $\alpha_2 \approx 38.0^\circ$, and light travels in water at the speed $v \approx 2.26 \cdot 10^{8}\,\text{m/s}$. The results are given to three significant figures, like the angle of incidence $55.0^\circ$ and the refractive indices.

<!-- vaihe -->

**Reasonableness.** The ray is refracted towards the normal, because $38.0^\circ < 55.0^\circ$, as it should be when light passes into an optically denser material. The speed is smaller than $c$, and the ratio of the sines is the same as the ratio of the speeds: $\sin 55.0^\circ : \sin 38.0^\circ \approx 1.33$ and $3.00 : 2.26 \approx 1.33$.

## Common misconception
Many students measure the angle of incidence from the boundary instead of from the normal. If the ray and the surface of the water make an angle of $30^\circ$, the angle of incidence is $90^\circ - 30^\circ = 60^\circ$. Another mistake is to think that the angle of refraction is proportional to the angle of incidence. The law of refraction concerns the sines of the angles: from air into water at an angle of incidence of $30^\circ$ the angle of refraction is $22.1^\circ$, but at an angle of incidence of $60^\circ$ it is $40.6^\circ$ and not $44.2^\circ$. A third mistake is to believe that light is always refracted towards the normal. The direction depends on which material is optically denser: a ray coming from water into air is refracted away from the normal. A fourth mistake is to think that light is refracted because it "collides" with the surface. Light is refracted because its speed changes.

## Summary
- At a boundary part of the light is usually reflected and part refracted. Angles are measured from the normal of the boundary.
- The law of reflection: $\beta = \alpha_1$, and the incident ray, the reflected ray and the normal lie in the same plane.
- The refractive index $n = c : v$ tells how many times more slowly light travels in a material than in a vacuum.
- The law of refraction: $n_1 \sin\alpha_1 = n_2 \sin\alpha_2$. Into an optically denser material the ray is refracted towards the normal, into a less dense one away from the normal.
- Objects in water seem to be closer to the surface than they are, because the rays from them are refracted at the surface of the water.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a still lake in the evening. The spruces on the opposite shore are reflected upside down from the surface of the water. In the foreground near the shore, stones on the bottom can be seen through the water." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
