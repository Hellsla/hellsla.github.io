# Dispersion: the prism and the rainbow

> **Why** is there red on the outer edge and violet on the inner edge of the primary rainbow, and why can you see a rainbow only when the sun is behind you?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: after a summer shower a bright rainbow arches over a field and forest, red on its outer edge and violet on its inner edge. Outside it a fainter second rainbow is visible with the colours in the opposite order, and the sky between the arcs is darker. Grey rain clouds are in the background. In the foreground a person stands with their back to the viewer, looking at the arc." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### The refractive index depends on wavelength
In the chapter *Reflection and refraction of light* the refractive index $n$ told how many times slower light travels in a material than in vacuum. Precise measurements show that the refractive index also depends on the wavelength of the light. In water and glass the refractive index is greater for violet light than for red, so violet light travels more slowly in them. In crown glass red light travels at about $198\,000\,\text{km/s}$ and violet at about $196\,000\,\text{km/s}$. The dependence of the refractive index on wavelength is called **dispersion**. The wavelengths in the table are vacuum wavelengths. At a boundary the frequency of light does not change, and colour is determined by frequency, so the colour stays the same even though the speed and wavelength change.

| colour | $\lambda\ (\text{nm})$ | water | crown glass |
|---|---|---|---|
| red | $656$ | $1.3315$ | $1.5143$ |
| yellow | $589$ | $1.3334$ | $1.5167$ |
| blue | $486$ | $1.3375$ | $1.5224$ |
| violet | $405$ | $1.3431$ | $1.5302$ |

Refractive indices of water at $20\,{}^\circ\text{C}$: M. Daimon and A. Masumura, *Applied Optics* 46, 2007. Refractive indices of N-BK7 crown glass: SCHOTT AG, optical glass catalogue, 2017.

<figure class="unit-photo"><img src="pics/fy7/prism-dispersion.webp" alt="A vertical band of light on a grey wall, its colours changing from left to right from red through yellow and green to blue."><figcaption>White light that has passed through a prism, falling on a wall. The prism refracts violet and blue light more than red, so the colours spread out into a spectrum.</figcaption></figure>

```pysahdy
White light arrives from air in crown glass. Which colour is slowed down more in the glass, red or violet, and why?
---
Violet is slowed down more, because its refractive index ($1.5302$) is greater than that of red ($1.5143$).
```

### Why violet is slowed down more
The electric field of light makes the electrons of the material oscillate at the frequency of the light. The oscillating electrons emit light themselves, which combines with the incoming light, and the combined wave travels more slowly than light in vacuum. The response of the electrons depends on frequency. In water and glass it strengthens as the frequency increases towards the ultraviolet, which the material absorbs strongly. So high-frequency violet light is slowed down more than low-frequency red, and its refractive index is greater.

### A prism splits white light
White light, such as sunlight, is a mixture of different wavelengths, that is, colours. When it enters glass at a slant, each colour is refracted according to the law of refraction but by a different amount: violet has the greatest refractive index, so it bends the most towards the normal. On leaving the second surface of a flat window pane of uniform thickness, the colours emerge again parallel to the original ray, so the colours are not noticed. The surfaces of a prism are slanted relative to each other, so at the second surface the colours are refracted still further apart. A fan of colours, a **spectrum**, comes out of the prism: red is deviated the least from its original direction and violet the most.

<svg data-fig="prism" viewBox="0 0 600 340" role="img" aria-label="Schematic diagram, not to scale: a narrow beam of white light arrives from the lower left at the left side of a glass prism. In the prism the light splits into colours, and a fan leaves from the other side: red is deviated the least from its original direction and violet the most, with orange, yellow, green and blue between them. The colours hit a white screen on the right one below another, red at the top. The spreading of the colours is drawn larger than in reality." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-prism.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="16" y="113.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{white light}$</div></foreignObject>
  <foreignObject x="504.5" y="137" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\text{red}$</div></foreignObject>
  <foreignObject x="485.5" y="283.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{violet}$</div></foreignObject>
  <foreignObject x="223.5" y="276.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{glass prism}$</div></foreignObject>
</svg>

A prism does not colour light. In the 1660s Isaac Newton showed that when a single colour is separated from the spectrum and sent through a second prism, it is refracted but not split into new colours. A second prism turned the other way, on the other hand, gathers the spectrum back into white light. The colours were therefore already present in white light, and the prism only separates them from each other.

### A rainbow forms in water droplets
A small raindrop is almost spherical. Sunlight is refracted into the droplet, reflected from the back surface of the droplet and refracted out of the lower part of the droplet. The light therefore returns towards the sun, but turned around. In both refractions violet is refracted more than red, so the colours separate. The direction in which the light leaves also depends on where the ray hits the droplet. However, the light is concentrated in one direction, because over a wide range of points of incidence the rays leave in almost the same direction: red at about $42^\circ$ and violet at about $40.6^\circ$ from the direction the sunlight came from. In this direction the droplet shines most brightly.

<svg data-fig="drop" viewBox="0 0 600 372" role="img" aria-label="Schematic diagram, not to scale: a large water droplet. A horizontal ray of white sunlight arrives from the left at the upper part of the droplet. At the point of incidence the normal is drawn as a dashed line, and the angle of incidence alpha and the angle of refraction beta are marked. In the droplet the light splits: the red and violet rays travel to the back wall of the droplet, are reflected from it and are refracted out of the lower part of the droplet towards the lower left. Violet leaves at a smaller angle than red. The difference between the colours is drawn larger than in reality." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-drop.webp" x="0" y="0" width="600" height="380" preserveAspectRatio="none"/>
  <foreignObject x="252" y="20" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="380" y="78" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\beta$</div></foreignObject>
  <foreignObject x="20" y="12" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sunlight}$</div></foreignObject>
  <foreignObject x="468" y="43.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{reflected}$</div></foreignObject>
  <foreignObject x="349.5" y="330" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{red}$</div></foreignObject>
  <foreignObject x="197.5" y="310.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\text{violet}$</div></foreignObject>
</svg>

### Why red is on the outer edge of the primary rainbow
When the sun is behind you, the sun's rays pass your head towards the **antisolar point**, which is below the horizon at the shadow of your own head. Red light reaches the eye from the droplets seen at $42^\circ$ from the direction of the antisolar point, and violet from those seen at $40.6^\circ$. Droplets at the same angle form a circle whose centre is the antisolar point. The circle of red is larger, so red is on the outer edge of the arc. The different colours leave a droplet at their strongest in slightly different directions. That is why light of a particular colour reaches the eye especially strongly from each droplet, and the strongest directions of the droplet's other colours pass by the eye. That is why each viewer sees their own rainbow.

<svg data-fig="observer" viewBox="0 0 600 380" role="img" aria-label="Schematic side view, angles not to scale: the viewer stands on the right with their back to the Sun, and the sunlight comes from the upper right obliquely down into the shower on the left. From the eye a dashed line runs along the sunlight down to the left towards the antisolar point, which is at the shadow of the viewer&#x27;s head below the horizon. The upper drop is at an angle of 42 degrees from this direction, and red light from it reaches the eye; its violet light passes above the eye. The lower drop is at an angle of about 40.6 degrees, and violet light from it reaches the eye; its red light hits the ground in front of the viewer." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-observer.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="480" y="89.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$\text{sunlight}$</div></foreignObject>
  <foreignObject x="212" y="232.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$42^\circ$</span></div></foreignObject>
  <foreignObject x="281" y="224" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$40.6^\circ$</span></div></foreignObject>
  <foreignObject x="132.5" y="84" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{red}$</span></div></foreignObject>
  <foreignObject x="80.5" y="142" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{violet}$</span></div></foreignObject>
  <foreignObject x="187.5" y="347.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{antisolar point}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/rainbow-glen-coe.webp" alt="A green mountain valley with a stream; a rainbow appears over the valley beneath a cloudy sky."><figcaption>A rainbow in Glen Coe, Scotland. The Sun shines from behind the viewer, and the light is refracted and reflected in water drops, which split it into colours.</figcaption></figure>

A rainbow is therefore seen only when the sun shines from behind you and there are droplets ahead. On level ground only the part of the arc above the horizon is visible. If the sun is at a height $h$ above the horizon, the antisolar point is the same distance below the horizon, and the top of the red arc is at a height $42^\circ - h$. When the sun is higher than $42^\circ$, the whole arc is below the horizon and cannot be seen from the ground. That is why rainbows are seen in midsummer in the morning and evening, when the sun is low.

```pysahdy
The sun is at a height of $30^\circ$ above the horizon. How high above the horizon is the top of the red arc of the primary rainbow?
---
The top is at a height of $42^\circ - 30^\circ = 12^\circ$, because the antisolar point is $30^\circ$ below the horizon.
```

### The secondary bow
Outside the primary bow a fainter **secondary bow** is sometimes seen. In it the light is reflected twice inside the droplet, and the order of the colours is reversed: red is on the inner edge at about $50^\circ$ and violet on the outer edge at about $54^\circ$ from the direction of the antisolar point. At each reflection some of the light escapes from the droplet, so the secondary bow is fainter. The sky between the arcs is darker, because the droplets of the primary bow light only the inside of the arc and those of the secondary bow only the outside.

## Formula: Law of refraction for different wavelengths
When light arrives from air in a material, each wavelength is refracted according to its own refractive index:
```latex
\sin \alpha_1 = n(\lambda) \sin \alpha_2
```
where $\alpha_1$ is the angle of incidence and $\alpha_2$ the angle of refraction, both measured from the normal, and $n(\lambda)$ is the refractive index of the material at wavelength $\lambda$. The refractive index of air is $1.0003$, so it is rounded to one; the general form is $n_1 \sin\alpha_1 = n_2 \sin\alpha_2$ (chapter *Reflection and refraction of light*). The speed of light in a material is $v = c : n(\lambda)$, where $c = 3.00 \cdot 10^8\,\text{m/s}$. In the graph the refractive index of crown glass decreases as the wavelength increases, most steeply at the violet end.

<svg data-fig="n-graph" viewBox="0 0 600 372" role="img" aria-label="Graph to scale: the refractive index n of N-BK7 crown glass as a function of the vacuum wavelength lambda from 400 to 700 nm. Six measured points from the manufacturer&#x27;s table: 405 nm 1.5302; 436 nm 1.5267; 486 nm 1.5224; 546 nm 1.5187; 589 nm 1.5167 and 656 nm 1.5143. The curve falls: at short wavelengths the refractive index is greatest, and the curve flattens towards red. Below the horizontal axis is a strip of the colours of visible light from violet to red." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy711-band1" gradientUnits="userSpaceOnUse" x1="137.69230769230768" y1="0" x2="470.0" y2="0"><stop offset="0.000" stop-color="#7048e8"/><stop offset="0.200" stop-color="#1971c2"/><stop offset="0.400" stop-color="#2b8a3e"/><stop offset="0.583" stop-color="#f59f00"/><stop offset="0.700" stop-color="#e8590c"/><stop offset="0.867" stop-color="#c92a2a"/></linearGradient></defs>
  <line x1="137.5" y1="290" x2="137.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="193" y1="290" x2="193" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248.5" y1="290" x2="248.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="290" x2="359" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="290" x2="414.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="242" x2="470" y2="242" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="194" x2="470" y2="194" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="146" x2="470" y2="146" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="98" x2="470" y2="98" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="291" x2="110" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,24 L116,37 L104,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="290" x2="137.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="115" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="193" y1="290" x2="193" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248.5" y1="290" x2="248.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="226" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="304" y1="290" x2="304" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="359" y1="290" x2="359" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="336.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="414.5" y1="290" x2="414.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="103" y1="242" x2="110" y2="242" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="227.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.515$</div></foreignObject>
  <line x1="103" y1="194" x2="110" y2="194" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="179.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.520$</div></foreignObject>
  <line x1="103" y1="146" x2="110" y2="146" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.525$</div></foreignObject>
  <line x1="103" y1="98" x2="110" y2="98" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="83.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.530$</div></foreignObject>
  <line x1="103" y1="50" x2="110" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="35.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.535$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="124" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$n$</span></div></foreignObject>
  <polyline points="137.5,90.5 140.5,93.5 143,96.5 146,99.5 149,102 151.5,105 154.5,108 157,110.5 160,113 162.5,116 165.5,118.5 168,121 171,123.5 173.5,126 176.5,128.5 179,131 182,133 185,135.5 187.5,138 190.5,140 193,142 196,144.5 198.5,146.5 201.5,148.5 204,150.5 207,153 209.5,155 212.5,156.5 215,158.5 218,160.5 221,162.5 223.5,164.5 226.5,166 229,168 232,170 234.5,171.5 237.5,173.5 240,175 243,176.5 245.5,178.5 248.5,180 251,181.5 254,183 257,184.5 259.5,186 262.5,187.5 265,189 268,190.5 270.5,192 273.5,193.5 276,195 279,196.5 281.5,198 284.5,199 287,200.5 290,202 293,203 295.5,204.5 298.5,205.5 301,207 304,208 306.5,209.5 309.5,210.5 312,212 315,213 317.5,214 320.5,215.5 323,216.5 326,217.5 329,218.5 331.5,219.5 334.5,221 337,222 340,223 342.5,224 345.5,225 348,226 351,227 353.5,228 356.5,229 359,230 362,231 365,231.5 367.5,232.5 370.5,233.5 373,234.5 376,235.5 378.5,236 381.5,237 384,238 387,239 389.5,239.5 392.5,240.5 395,241.5 398,242 401,243 403.5,243.5 406.5,244.5 409,245.5 412,246 414.5,247 417.5,247.5 420,248.5 423,249 425.5,250 428.5,250.5 431,251 434,252 437,252.5 439.5,253.5 442.5,254 445,254.5 448,255.5 450.5,256 453.5,256.5 456,257 459,258 461.5,258.5 464.5,259 467,259.5 470,260.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="143" cy="95.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="177.5" cy="130" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="233" cy="171" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="299.5" cy="206.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="347.5" cy="225.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="421.5" cy="248.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <rect x="137.5" y="336" width="332.5" height="12" rx="2" fill="url(#fy711-band1)" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="159" y="81" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{violet}$</span></div></foreignObject>
  <foreignObject x="399" y="204" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{red}$</span></div></foreignObject>
</svg>

```pysahdy
The refractive index of red light in water is $1.3315$. How fast does red light travel in water?
---
The speed is $v = c : n = 3.00 \cdot 10^8\,\text{m/s} : 1.3315 \approx 2.25 \cdot 10^8\,\text{m/s}$.
```

### The angle of deviation of a prism
In a prism the ray is refracted twice, and the angles depend on each other:
```latex
\begin{aligned}
&\alpha_2 + \alpha_3 = A \\[6pt]
&\delta = \alpha_1 + \alpha_4 - A
\end{aligned}
```
where $\alpha_1$ is the angle of incidence and $\alpha_2$ the angle of refraction at the first surface, $\alpha_3$ the angle of incidence from inside the glass at the second surface and $\alpha_4$ the angle of refraction on leaving, all measured from the normals. $A$ is the apex angle of the prism and $\delta$ the **angle of deviation**, the amount by which the ray is turned from its original direction. The first equation follows from the sum of the angles of a triangle, because the normals of the surfaces meet at an angle $180^\circ - A$. The second follows from the ray turning by $\alpha_1 - \alpha_2$ at the first surface and by $\alpha_4 - \alpha_3$ at the second. For violet $\alpha_4$ is greater than for red, so its angle of deviation is greater. The equations hold when the ray can leave through the second surface of the prism.

<svg data-fig="prism-angles" viewBox="0 0 600 336" role="img" aria-label="Diagram of a prism: a single-colour ray arrives from the left at the left side of the prism at an angle of incidence alpha 1 to the normal and is refracted in the glass to the angle alpha 2. The ray hits the right side at an angle of incidence alpha 3 and leaves the prism at an angle of refraction alpha 4. The normals of both surfaces are drawn as dashed lines. At the top of the prism is the apex angle A. The extension of the incident ray is drawn as a dashed line, and the angle between it and the emerging ray is the angle of deviation delta." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-prism-angles.webp" x="0" y="1.2" width="600" height="346.2" preserveAspectRatio="none"/>
  <foreignObject x="99.5" y="183" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_1$</div></foreignObject>
  <foreignObject x="245" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_2$</div></foreignObject>
  <foreignObject x="298.5" y="204" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_3$</div></foreignObject>
  <foreignObject x="443" y="170" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_4$</div></foreignObject>
  <foreignObject x="280" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="455.5" y="130.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\delta$</div></foreignObject>
</svg>

### The angle of a rainbow
In the droplet the ray turns by $\alpha - \beta$ at the point of entry, by $180^\circ - 2\beta$ at the reflection and again by $\alpha - \beta$ at the point of exit. The total turning is therefore $180^\circ + 2\alpha - 4\beta$. The angle between the light leaving the droplet and the direction of the sun is $180^\circ$ minus the total turning, that is,
```latex
\theta = 4\beta - 2\alpha
```
where $\alpha$ is the angle of incidence at the surface of the droplet, $\beta$ the angle of refraction, $\sin\alpha = n \sin\beta$, and $\theta$ is the angle at which the light is seen from the direction of the antisolar point. The graph shows that $\theta$ depends on the angle of incidence but does not exceed $42.3^\circ$ when $n = 1.3315$. Near the peak the curve is almost horizontal, so over a wide range of angles of incidence the rays leave in almost the same direction, and a bright arc is seen in that direction. The rest of the light leaves at smaller angles, so the sky inside the arc is brighter. For violet ($n = 1.3431$) the greatest angle is $40.6^\circ$.

<svg data-fig="theta-graph" viewBox="0 0 600 350" role="img" aria-label="Graph to scale: a ray of red light (n = 1.332) leaves a water droplet at an angle theta from the direction of the antisolar point. The horizontal axis shows the angle of incidence alpha from 0 to 90 degrees and the vertical axis theta from 0 to 45 degrees. The curve rises from the origin, reaches its greatest value of 42.3 degrees when the angle of incidence is about 59.5 degrees, and then falls to about 15 degrees. Near the peak the curve is almost horizontal: over a wide range of angles of incidence the rays leave in almost the same direction." style="max-width:100%;font-size:24px">
  <line x1="137.5" y1="290" x2="137.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="179" y1="290" x2="179" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220.5" y1="290" x2="220.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="290" x2="262" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="290" x2="345.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="387" y1="290" x2="387" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428.5" y1="290" x2="428.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="263.5" x2="470" y2="263.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="236.5" x2="470" y2="236.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="210" x2="470" y2="210" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="183.5" x2="470" y2="183.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="156.5" x2="470" y2="156.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="130" x2="470" y2="130" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103.5" x2="470" y2="103.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76.5" x2="470" y2="76.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,24 L102,37 L90,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="290" x2="137.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="179" y1="290" x2="179" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220.5" y1="290" x2="220.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="204" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="262" y1="290" x2="262" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="345.5" y1="290" x2="345.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="329" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="387" y1="290" x2="387" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="428.5" y1="290" x2="428.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$90$</div></foreignObject>
  <line x1="89" y1="263.5" x2="96" y2="263.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="236.5" x2="96" y2="236.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="222" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="210" x2="96" y2="210" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="183.5" x2="96" y2="183.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="169" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="156.5" x2="96" y2="156.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="130" x2="96" y2="130" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="103.5" x2="96" y2="103.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76.5" x2="96" y2="76.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="62" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="50" x2="96" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha\ (^\circ)$</div></foreignObject>
  <foreignObject x="110" y="15.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\theta\ (^\circ)$</span></div></foreignObject>
  <polygon points="304,290 304,50 387,50 387,290" fill="#b2f2bb" fill-opacity="0.45"/>
  <polyline points="96,290 99,286 102,282 105.5,278 108.5,274 111.5,270 114.5,266 118,262 121,258 124,254 127,250 130.5,246 133.5,242 136.5,238 139.5,234 143,230.5 146,226.5 149,222.5 152,218.5 155,214.5 158.5,211 161.5,207 164.5,203.5 167.5,199.5 171,195.5 174,192 177,188.5 180,184.5 183.5,181 186.5,177.5 189.5,173.5 192.5,170 195.5,166.5 199,163 202,159.5 205,156 208,152.5 211.5,149.5 214.5,146 217.5,142.5 220.5,139.5 224,136.5 227,133 230,130 233,127 236,124 239.5,121 242.5,118 245.5,115 248.5,112.5 252,109.5 255,107 258,104.5 261,101.5 264.5,99 267.5,97 270.5,94.5 273.5,92 277,90 280,88 283,85.5 286,83.5 289,82 292.5,80 295.5,78 298.5,76.5 301.5,75 305,73.5 308,72 311,71 314,70 317.5,68.5 320.5,68 323.5,67 326.5,66 330,65.5 333,65 336,65 339,64.5 342,64.5 345.5,64.5 348.5,64.5 351.5,65 354.5,65.5 358,66 361,66.5 364,67.5 367,68.5 370.5,70 373.5,71 376.5,72.5 379.5,74.5 382.5,76.5 386,78.5 389,80.5 392,83 395,85.5 398.5,88.5 401.5,91.5 404.5,94.5 407.5,98 411,101.5 414,105.5 417,109.5 420,113.5 423,118 426.5,122.5 429.5,127.5 432.5,132.5 435.5,138 439,143.5 442,149 445,155 448,161.5 451.5,168 454.5,174.5 457.5,181.5 460.5,188.5 464,196 467,203.5 470,211.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="343" y1="64.5" x2="343" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="64.5" x2="343" y2="64.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="343" cy="64.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="308" y="24" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$42.3^\circ$</span></div></foreignObject>
  <foreignObject x="285.5" y="233" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{bright arc}$</span></div></foreignObject>
</svg>

## Worked example
A narrow beam of white light arrives from air at the surface of a crown-glass plate at an angle of incidence of $60.0^\circ$. What are the angles of refraction of red ($656\,\text{nm}$) and violet ($405\,\text{nm}$) light in the glass, and how large an angle arises between them? Use the refractive indices in the table.

<!-- vaihe -->

**Given and find.** Angle of incidence $\alpha_1 = 60.0^\circ$; from the table the refractive index of red light is $n_\text{r} = 1.5143$ and of violet $n_\text{v} = 1.5302$. We are asked for the angles of refraction $\alpha_\text{r}$ and $\alpha_\text{v}$ and their difference $\Delta\alpha = \alpha_\text{r} - \alpha_\text{v}$.

<!-- vaihe -->

**Principle.** Each colour obeys the law of refraction with its own refractive index. The light arrives from air, whose refractive index is rounded to $1$, so $\sin \alpha_1 = n \sin \alpha_2$. The angle of incidence is the same for both colours, because they travel in the same beam of white light.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\sin \alpha_1 = n \sin \alpha_2 \\[6pt]
&\sin \alpha_2 = \frac{\sin \alpha_1}{n}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the refractive index has no unit, and the angles are in degrees.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\sin \alpha_\text{r} = \frac{\sin \alpha_1}{n_\text{r}} \\
&= \frac{\sin 60.0^\circ}{1.5143} \\
&= 0.57190 \\
&\alpha_\text{r} = 34.88^\circ \\[6pt]
&\sin \alpha_\text{v} = \frac{\sin \alpha_1}{n_\text{v}} \\
&= \frac{\sin 60.0^\circ}{1.5302} \\
&= 0.56596 \\
&\alpha_\text{v} = 34.47^\circ
\end{aligned}
```

<!-- vaihe -->

**Result.** The angle of refraction of red light is $34.9^\circ$ and of violet $34.5^\circ$, to three significant figures like the angle of incidence $60.0^\circ$. The angle between the rays is calculated from the unrounded angles: $\Delta\alpha = 34.88^\circ - 34.47^\circ = 0.41^\circ$.

<!-- vaihe -->

**Reasonableness.** Both angles of refraction are smaller than the angle of incidence, because light entering an optically denser material bends towards the normal. The angle of refraction of violet is smaller because its refractive index is greater. The difference is less than half a degree, so in glass of uniform thickness the colours separate only a little; the slanted second surface of a prism increases the difference.

## Common misconception
Many people think that a prism colours light or that the colours are created in the glass of the prism. The colours are already present in white light, and the prism separates them because the refractive index depends on wavelength. Another common mistake is to conclude that red is refracted the most because it has the longest wavelength. In water and glass it is the other way round: violet has the greatest refractive index, so violet is refracted and deviated the most. A third mistake is to think of a rainbow as an object at a particular place. A rainbow is a direction: it is always seen at $42^\circ$ from the antisolar point, so it moves with the viewer and its end cannot be reached.

## Summary
- The refractive index depends on wavelength. This is called dispersion. In water and glass violet has the greatest refractive index and red the smallest, so violet is refracted the most.
- In a prism white light is refracted twice at slanted surfaces, and the colours separate into a spectrum. The angle of deviation is $\delta = \alpha_1 + \alpha_4 - A$, and violet is deviated the most.
- In a rainbow light is refracted into a droplet, reflected from its back surface and refracted out. Red is seen at about $42^\circ$ and violet at about $40.6^\circ$ from the antisolar point, so red is on the outer edge.
- A rainbow is seen when the sun is behind you and lower than $42^\circ$. In the secondary bow the light is reflected twice, and the colours are in the opposite order.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: in a garden a lawn is being watered with a hose. A small rainbow is visible in the droplets of the water jet when the sun shines from behind the person watering." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-11-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
