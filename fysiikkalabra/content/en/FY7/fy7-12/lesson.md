# Total internal reflection and optical fibre

> **Why** can light travel in a glass fibre along the bed of the Baltic Sea from Helsinki to Germany without escaping on the way, even though glass is transparent?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a cross-section of the sea. There is a city on the shore at the left and another at the right, and a submarine cable runs along the seabed from one shore to the other. In a circle in the middle, like a magnifying glass, the glass fibre inside the cable is shown, with a ray of light zigzagging along the core by reflecting from the fibre&#x27;s edges." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Light going into an optically less dense substance
In the chapter *Reflection and refraction of light* we saw that light refracts at the boundary between two substances according to the law of refraction $n_1 \sin\alpha_1 = n_2 \sin\alpha_2$, and that part of the light is reflected. When light goes from a substance with a larger refractive index into one with a smaller refractive index, for example from water into air, it refracts away from the normal: the angle of refraction is larger than the angle of incidence. A ray coming from water at an angle of incidence of $30^\circ$ continues in the air at an angle of $41.7^\circ$ to the normal. When the angle of incidence is increased, the angle of refraction grows even faster and approaches $90^\circ$. At the same time the share of the light that is reflected grows.

### The critical angle and total internal reflection
The angle of incidence at which the angle of refraction is $90^\circ$ is called the **critical angle** $\alpha_\text{r}$. At the critical angle the refracted ray travels along the boundary. When the angle of incidence is larger than the critical angle, the law of refraction gives no angle of refraction, because the sine would have to be greater than one. No propagating refracted ray then arises in the second substance, and the light is reflected back according to the law of reflection. This is **total internal reflection**. At an ideal, lossless boundary all the incident light power is reflected back, and no energy passes into the second substance. A very rapidly decaying electromagnetic field does arise close to the boundary, however.

At the boundary between water and air the critical angle is $48.8^\circ$. That is why a diver looking at the water surface at a slant from below sees it as a mirror in which the bottom can be seen.

<svg data-fig="water" viewBox="0 0 600 360" role="img" aria-label="Schematic picture: a lamp at the bottom of the water sends three rays of light to the water surface at different angles of incidence. The normal to the surface is drawn as a dashed line at each point of impact. On the left the angle of incidence of 30 degrees is smaller than the critical angle: the ray refracts into the air, away from the normal, and a weak part is reflected back into the water. In the middle the angle of incidence is the critical angle, 48.8 degrees: the refracted ray travels along the surface. On the right the angle of incidence of 65 degrees is larger than the critical angle: no light gets into the air, and the whole ray is reflected back into the water, which is total internal reflection." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-water.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="87" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha < \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="216.5" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha = \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="361" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha > \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="539" y="85.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{air}$</div></foreignObject>
  <foreignObject x="272" y="231.5" width="295" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$\text{total internal reflection}$</div></foreignObject>
  <foreignObject x="405" y="291.5" width="162" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$\text{water},\ n = 1.33$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/tir-wine-glass.webp" alt="A hand holds a wine glass by its stem against a black background; a green laser beam enters from below and zigzags through the stem and base of the glass."><figcaption>A green laser beam in the stem of a wine glass. The beam meets the surface of the glass at an angle larger than the critical angle, so it is totally reflected back into the glass and does not escape into the air.</figcaption></figure>

```pysahdy
Light goes from water into air at an angle of incidence of $70^\circ$. The critical angle for water and air is $48.8^\circ$. Can some of the light get out into the air?
---
No. The angle of incidence $70^\circ$ is larger than the critical angle $48.8^\circ$, so the light is totally reflected back into the water.
```

### Only from a larger refractive index to a smaller one
Total internal reflection can happen only when light goes from a substance with a larger refractive index into one with a smaller refractive index. When light goes from air into water or glass, it refracts towards the normal, and a refracted ray exists at every angle of incidence. Then some of the light always gets into the second substance, even though the reflected share grows at large angles of incidence. In total internal reflection no light is lost: when the substance does not absorb light, the ray reflected from a smooth boundary carries away all the power of the incident ray. That is why total internal reflection is a better mirror than a metal surface, which absorbs some of the light.

### Optical fibre
An **optical fibre** is a glass fibre as thin as a hair, with a core in the middle and a cladding around it. The refractive index of the core is slightly larger than that of the cladding, for example $1.48$ and $1.46$. Light that enters the end of the fibre almost parallel to its axis meets the boundary between the core and the cladding at a very shallow angle, that is at a large angle of incidence, which is larger than the critical angle. The light is totally internally reflected back into the core every time and travels along the fibre in a zigzag, even when the fibre bends gently. If light enters the end of the fibre at too steep an angle, it meets the boundary at an angle of incidence smaller than the critical angle, and at every impact part of it refracts into the cladding and is lost from the core. A sharp bend reduces the angle of incidence in the same way, so a fibre must not be folded into a tight bend.

<svg data-fig="fibre" viewBox="0 0 600 340" role="img" aria-label="Schematic picture of an optical fibre, not to scale. At the top the fibre is cut lengthwise: in the middle the core with refractive index n1, around it the cladding with a slightly smaller refractive index n2, and outermost a plastic protective coating. A ray of light travels in the core in a zigzag: it meets the boundary between the core and the cladding at an angle of incidence larger than the critical angle and is totally internally reflected back into the core each time. At the bottom right the same fibre in cross-section: the core, the cladding and the coating as nested circles." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-fibre.webp" x="-2.5" y="0" width="603" height="353" preserveAspectRatio="none"/>
  <foreignObject x="333.5" y="63.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="422.5" y="63.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha > \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="132" y="147.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{cladding}\ n_2$</div></foreignObject>
  <foreignObject x="60" y="247.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{core}\ n_1$</div></foreignObject>
  <foreignObject x="210" y="291.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{coating}$</div></foreignObject>
  <foreignObject x="330" y="255.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n_1 > n_2$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/optical-fibres.webp" alt="A translucent optical cable coiled on a black surface; at each end is a connector shining with red light."><figcaption>Red light sent into one end of a plastic optical cable comes out of the other end. Thanks to total internal reflection, the light follows the fibre around the coil.</figcaption></figure>

```pysahdy
What if the refractive indices of a fibre's core and cladding are equal, $n_1 = n_2$? Could light still be totally reflected at the boundary between core and cladding?
---
No. Then $\sin\alpha_\text{r} = n_2 : n_1 = 1$ and the critical angle would be $90^\circ$. The angle of incidence cannot be that large, so the light would not be totally reflected but would go on into the cladding and leak out of the fibre.
```

### Why a fibre has a cladding
A bare glass rod keeps light inside even in air, and even light that arrives at a steeper angle, because the difference between the refractive indices of glass and air is large and the critical angle is therefore small. However, water, grease or another fibre that touches the surface of the glass changes the boundary, and light leaks out at the point of contact. The cladding keeps the reflecting boundary clean inside the fibre, and the plastic protective coating protects the glass from scratches. When the difference between the refractive indices of the core and the cladding is small, only rays almost parallel to the axis stay in the fibre. Their paths are almost equally long, so short light pulses spread out only a little on the way.

### Information as light pulses
In telecommunications, information travels in a fibre as short light pulses. The light used is usually infrared light with a wavelength of about $1550\,\text{nm}$, because the silica glass of the fibre attenuates it least. The power of the light in a fibre drops to half only over a distance of about $15\,\text{km}$, so on long links the pulses are amplified only at intervals of about $50$–$100\,\text{km}$. For example, Cinia's submarine cable C-Lion1 runs along the bed of the Baltic Sea from Helsinki to Rostock in Germany, and its length is $1172\,\text{km}$ (Cinia, 2016). Light travels more slowly in glass than in a vacuum, so the fibre delays the signal slightly more than the distance alone would suggest.

### Endoscope
A traditional fibre endoscope has two bundles of fibres. One brings the illuminating light into the body, and the other carries the image back. The thousands of fibres of the image bundle are in the same order at both ends of the bundle, and each fibre carries the light of one pixel. The bundle bends, so it can be used to see round a bend, for example into the stomach. In modern video endoscopes the image can also be formed by a camera sensor at the tip of the instrument, and the fibres then bring only the illumination.

### The sparkle of a diamond
The refractive index of diamond is $2.42$, so its critical angle against air is only $24.4^\circ$. The slanting lower faces of a cut diamond are tilted so that light coming from the top face meets them at an angle of incidence larger than the critical angle. The light is totally internally reflected and returns upwards towards the viewer. In a glass stone of the same shape the critical angle is $41.8^\circ$, so some of the same light refracts out below the stone, and the glass sparkles less.

<svg data-fig="diamond" viewBox="0 0 600 310" role="img" aria-label="Schematic picture, not to scale: two cut stones of the same shape in cross-section. From the top face of each stone the same ray of light comes straight down and meets the lower slanting face at an angle of incidence of 38 degrees. On the left, in diamond, which has refractive index 2.42 and critical angle 24.4 degrees, the ray is totally internally reflected twice and returns upwards out of the top of the stone. On the right, in glass, which has refractive index 1.50 and critical angle 41.8 degrees, the angle of incidence is smaller than the critical angle: most of the light refracts out below the stone, and only a weak part is reflected." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-diamond.webp" x="13.2" y="1.2" width="576.9" height="308.9" preserveAspectRatio="none"/>
  <foreignObject x="137" y="118.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$38^\circ$</div></foreignObject>
  <foreignObject x="25" y="265.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{diamond},\ \alpha_\text{r} = 24.4^\circ$</div></foreignObject>
  <foreignObject x="426" y="118.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$38^\circ$</div></foreignObject>
  <foreignObject x="325" y="265.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{glass},\ \alpha_\text{r} = 41.8^\circ$</div></foreignObject>
</svg>

## Formula: Critical angle
At the critical angle the angle of refraction is $90^\circ$, and $\sin 90^\circ = 1$. When the critical angle is substituted into the law of refraction as the angle of incidence and $90^\circ$ as the angle of refraction, we get for the critical angle
```latex
\begin{aligned}
&n_1 \sin\alpha_\text{r} = n_2 \sin 90^\circ \\[6pt]
&\sin\alpha_\text{r} = \frac{n_2}{n_1}
\end{aligned}
```
where $\alpha_\text{r}$ is the critical angle measured from the normal to the boundary, $n_1$ is the refractive index of the substance the light comes from and $n_2$ is the refractive index of the substance the light is going into. A critical angle exists only when $n_1 > n_2$: otherwise $n_2 : n_1 \ge 1$. When the angle of incidence is larger than the critical angle, the light is totally internally reflected. The larger the difference between the refractive indices, the smaller the critical angle, as the graph shows.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Graph, to scale: the critical angle in degrees as a function of the refractive index n1 of a substance, when the other substance is air with refractive index 1.00. The curve falls from 90 degrees when n1 is 1.00, first steeply and then more gently. Marked points: water, n1 = 1.33, critical angle 48.8 degrees; glass, n1 = 1.50, 41.8 degrees; diamond, n1 = 2.42, 24.4 degrees." style="max-width:100%;font-size:24px">
  <line x1="149" y1="290" x2="149" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="202" y1="290" x2="202" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="255" y1="290" x2="255" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308" y1="290" x2="308" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361" y1="290" x2="361" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414" y1="290" x2="414" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="467" y1="290" x2="467" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="290" x2="520" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="254.5" x2="520" y2="254.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="218.5" x2="520" y2="218.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="183" x2="520" y2="183" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="147.5" x2="520" y2="147.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="111.5" x2="520" y2="111.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="520" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="534" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M546,290 L533,296 L533,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="149" y1="290" x2="149" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="126.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.2$</div></foreignObject>
  <line x1="202" y1="290" x2="202" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="255" y1="290" x2="255" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="232.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.6$</div></foreignObject>
  <line x1="308" y1="290" x2="308" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="361" y1="290" x2="361" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="338.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.0$</div></foreignObject>
  <line x1="414" y1="290" x2="414" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="467" y1="290" x2="467" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="444.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.4$</div></foreignObject>
  <line x1="520" y1="290" x2="520" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="254.5" x2="96" y2="254.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="218.5" x2="96" y2="218.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="204" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="183" x2="96" y2="183" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="147.5" x2="96" y2="147.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="133" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="89" y1="111.5" x2="96" y2="111.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="61.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$90$</div></foreignObject>
  <foreignObject x="552" y="275.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_1$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_\text{r}\ (^\circ)$</div></foreignObject>
  <foreignObject x="73.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.0$</div></foreignObject>
  <foreignObject x="64" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,76 99.5,98 103,107 106.5,114 110,119.5 113.5,124.5 117,129 120.5,132.5 124.5,136.5 128,139.5 131.5,143 135,145.5 138.5,148.5 142,151 145.5,153.5 149,156 152.5,158 156,160 159.5,162 163,164 166.5,166 170,168 173.5,169.5 177.5,171.5 181,173 184.5,174.5 188,176 191.5,177.5 195,179 198.5,180.5 202,181.5 205.5,183 209,184 212.5,185.5 216,186.5 219.5,188 223,189 226.5,190 230.5,191 234,192 237.5,193 241,194 244.5,195 248,196 251.5,197 255,198 258.5,199 262,200 265.5,200.5 269,201.5 272.5,202.5 276,203 279.5,204 283.5,204.5 287,205.5 290.5,206 294,207 297.5,207.5 301,208.5 304.5,209 308,210 311.5,210.5 315,211 318.5,211.5 322,212.5 325.5,213 329,213.5 332.5,214 336.5,215 340,215.5 343.5,216 347,216.5 350.5,217 354,217.5 357.5,218 361,218.5 364.5,219 368,219.5 371.5,220 375,220.5 378.5,221 382,221.5 385.5,222 389.5,222.5 393,223 396.5,223.5 400,224 403.5,224.5 407,225 410.5,225.5 414,225.5 417.5,226 421,226.5 424.5,227 428,227.5 431.5,228 435,228 438.5,228.5 442.5,229 446,229.5 449.5,229.5 453,230 456.5,230.5 460,230.5 463.5,231 467,231.5 470.5,232 474,232 477.5,232.5 481,233 484.5,233 488,233.5 491.5,234 495.5,234 499,234.5 502.5,234.5 506,235 509.5,235.5 513,235.5 516.5,236 520,236" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="183.5" cy="174" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="101.5" y="185.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{water}$</span></div></foreignObject>
  <circle cx="228.5" cy="190.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="240.5" y="154" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{glass}$</span></div></foreignObject>
  <circle cx="472.5" cy="232" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="425" y="181.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{diamond}$</span></div></foreignObject>
  <foreignObject x="320" y="97.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$n_2 = 1.00\ (\text{air})$</span></div></foreignObject>
</svg>

```pysahdy
The refractive index of a substance is $2.00$. What is the critical angle at the boundary between this substance and air?
---
The refractive index of air is $1.00$, so $\sin\alpha_\text{r} = 1.00 : 2.00 = 0.500$. Thus $\alpha_\text{r} = 30.0^\circ$.
```

### The travel time of light in a fibre
In a substance with refractive index $n$, light travels at the speed $v = c : n$ (chapter *Reflection and refraction of light*). A distance $s$ therefore takes the time
```latex
t = \frac{s}{v} = \frac{n s}{c}
```
where $c = 3.00 \cdot 10^8\,\text{m/s}$ is the speed of light in a vacuum. In the glass of a fibre $n \approx 1.47$, so light travels at about $2.04 \cdot 10^8\,\text{m/s}$, which is about two thirds of the speed of light in a vacuum. The formula gives the travel time of a ray along the axis of the fibre. A ray that zigzags travels a slightly longer distance and arrives slightly later.

## Worked example
The core of an optical fibre has a refractive index of $1.48$ and the cladding $1.46$. What is the critical angle at the boundary between the core and the cladding? A ray travelling in the core meets the boundary at an angle of incidence of $83^\circ$. Does it stay in the core?

<!-- vaihe -->

**Given and find.** The refractive index of the core is $n_1 = 1.48$, that of the cladding is $n_2 = 1.46$ and the angle of incidence of the ray is $\alpha = 83^\circ$. We are asked for the critical angle $\alpha_\text{r}$ and whether the ray is totally internally reflected.

<!-- vaihe -->

**Principle.** Light goes from the core into the cladding, that is from a substance with a larger refractive index into one with a smaller refractive index, so a critical angle exists. At the critical angle the angle of refraction would be $90^\circ$, so the sine of the critical angle follows from the law of refraction. If the angle of incidence is larger than the critical angle, the ray is totally internally reflected.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&n_1 \sin\alpha_\text{r} = n_2 \sin 90^\circ \\[6pt]
&\sin\alpha_\text{r} = \frac{n_2}{n_1} \\[6pt]
&\alpha_\text{r} = \sin^{-1}\frac{n_2}{n_1}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the refractive indices are numbers without units, and the angle comes out in degrees.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\sin\alpha_\text{r} = \frac{1.46}{1.48} \\
&= 0.9865 \\[6pt]
&\alpha_\text{r} = \sin^{-1} 0.9865 \\
&= 80.57^\circ
\end{aligned}
```

<!-- vaihe -->

**Result.** The critical angle is $\alpha_\text{r} \approx 80.6^\circ$, to three significant figures like the refractive indices. The angle of incidence $83^\circ$ is larger than the critical angle, so the ray is totally internally reflected and stays in the core.

<!-- vaihe -->

**Reasonableness.** The refractive indices are almost equal, so the ray refracts only a little into the cladding and the critical angle must be close to $90^\circ$, as in the result. At the boundary between glass and air the difference is much larger, and the critical angle is only about $42^\circ$. Check: $1.48 \cdot \sin 80.57^\circ = 1.48 \cdot 0.9865 = 1.46$.

## Common misconception
Many people think that light can be totally internally reflected at any boundary as long as the angle of incidence is large enough, for example also when light goes from air into water. However, light going from air into water refracts towards the normal, and the refracted ray exists at every angle of incidence, so some of the light always gets into the water. Total internal reflection requires that the light goes from a substance with a larger refractive index into one with a smaller refractive index. Another mistake is to think that the inner surface of an optical fibre is mirrored. A fibre has no mirror surface: the core and the cladding are both transparent glass, and light stays in the core because the refractive index of the cladding is smaller and the angle of incidence is larger than the critical angle.

## Summary
- When light goes from a substance with a larger refractive index into one with a smaller refractive index, it refracts away from the normal. At the critical angle $\alpha_\text{r}$ the angle of refraction is $90^\circ$.
- The critical angle follows from the equation $\sin\alpha_\text{r} = n_2 : n_1$ when $n_1 > n_2$. When the angle of incidence is larger than the critical angle, all of the light is reflected back: total internal reflection takes place.
- In an optical fibre the refractive index of the core is slightly larger than that of the cladding, and light travels in the core by total internal reflection. Light that arrives at too steep an angle leaks out.
- Fibres are used in data transmission, endoscopes and lamps. In a fibre light travels at the speed $v = c : n$, and the travel time is $t = n s : c$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: an optical-fibre lamp on a shelf. A bundle of thin transparent plastic fibres rises from its base and curves in every direction. The fibres do not glow along their sides, but the end of each fibre shines as a bright point." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
