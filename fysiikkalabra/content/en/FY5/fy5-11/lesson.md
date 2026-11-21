# A wave meets an obstacle or a gap

> **Why** do waves reach the corners of a harbour through the narrow gap in a breakwater, and do not travel only straight to the place opposite the gap?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a harbour seen at a slant from above. In the background is the open sea, where wave crests travel in straight rows towards the harbour. A breakwater made of rocks has a narrow gap in the middle, with a small lighthouse on each side of it. Behind the gap, in the harbour basin, the wave crests spread as half circles across the whole width of the basin, also behind the breakwater into the corners of the basin, where boats at the quay rock on the waves. On the quays are red boathouses and spruces, and far out at sea there is a sailing boat." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Wavefront and ray
A wave is easiest to describe from above. A **wavefront** is a line that joins the points of a wave that are in the same phase, for example one wave crest. The distance between two successive crests is the wavelength $\lambda$ (chapter *How waves form and travel*). A **ray** is an arrow that shows the direction of travel of the wave, and it is always perpendicular to the wavefront. A wave with straight fronts is a plane wave, and a point source, such as a stone dropped into water, sends out a circular wave whose rays point away from the source in every direction.

<svg data-fig="rintamat" viewBox="0 0 600 340" role="img" aria-label="Diagram of two waves seen from above. On the left a plane wave: the wavefronts are parallel straight lines spaced by the wavelength lambda, and the rays are arrows perpendicular to them. On the right a circular wave from a point source: the wavefronts are concentric circles, and the rays leave the source in every direction, perpendicular to the fronts." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-rintamat.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{plane wave}$</div></foreignObject>
  <foreignObject x="371" y="7.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{circular wave}$</div></foreignObject>
  <foreignObject x="90" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="164" y="301.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{wavefront}$</div></foreignObject>
  <foreignObject x="539" y="301.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ray}$</div></foreignObject>
</svg>

```pysahdy
The circular wave made by a stone dropped into water has circles as its wavefronts. In which direction do the rays point relative to a wavefront?
---
The rays point away from the source and are perpendicular to the wavefront at every point, because a ray shows the direction of propagation.
```

### Reflection from the end of a rope
When a wave arrives at a boundary of the medium, it is reflected: part of it or the whole wave returns. In a rope you can see this from a single pulse. If the end of the rope is tied to a wall, the end cannot move. An upward pulse pulls the fastening up, and the wall pulls the rope down with an equally large force. So **a pulse reflected from a fixed end is inverted**: it returns pointing downwards. If the end of the rope is a ring that slides without friction along a rod, the end swings up with the pulse and nothing pulls it down. **A pulse reflected from a free end is not inverted** but returns with the same sign.

<svg data-fig="koysi" viewBox="0 0 600 380" role="img" aria-label="Diagram, not to scale: reflection of a rope pulse in two cases. On the left the end of the rope is tied to a wall (fixed end), on the right the end is a ring that slides without friction along a vertical rod (free end). In the top row, before reflection, an upward pulse travels to the right towards the end. In the bottom row, after reflection, the pulse travels to the left: the pulse reflected from the fixed end is inverted and points downwards, the one reflected from the free end still points upwards." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-koysi.webp" x="1.2" y="0" width="597" height="386.8" preserveAspectRatio="none"/>
  <foreignObject x="96" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{fixed end}$</div></foreignObject>
  <foreignObject x="402.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{free end}$</div></foreignObject>
  <foreignObject x="16" y="45.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{before}$</div></foreignObject>
  <foreignObject x="136" y="59.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="16" y="211.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{after}$</div></foreignObject>
  <foreignObject x="120" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="316" y="45.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{before}$</div></foreignObject>
  <foreignObject x="436" y="59.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="316" y="211.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{after}$</div></foreignObject>
  <foreignObject x="420" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
</svg>

### Huygens' principle
In the 17th century the Dutchman Christiaan Huygens presented a principle with which the propagation of a wave can be worked out by drawing. According to **Huygens' principle**, every point of a wavefront acts as the source of a new small circular wave, a wavelet. The wavelets travel at the same speed as the original wave, and after a moment the new wavefront is the line that touches all the wavelets, their envelope. In open water the envelope of the wavelets is again a straight line, so a plane wave continues straight. When part of the front stops at an obstacle or bounces off a wall, the remaining wavelets tell where the wave goes.

```pysahdy
A wave travels at $0.30\,\text{m/s}$. What is the radius of the circle a wavelet has drawn after $2.0\,\text{s}$?
---
A wavelet travels at the same speed as the original wave, so the radius is $0.30\,\text{m/s} \cdot 2.0\,\text{s} = 0.60\,\text{m}$. The new wavefront touches all these circles.
```

### Diffraction
When a wave passes through a slit or past an obstacle, it also bends behind the obstacle, into the region that a straight ray does not reach. This is called **diffraction**, or bending of the wave. Huygens' principle explains it: the points of the front at the slit are sources of wavelets, and the wavelets of the outermost points spread sideways. The width of the slit is denoted by $b$. If the slit is many wavelengths wide, the front continues almost straight at the slit and curves only at the edges. When the slit is clearly narrower than the wavelength, that is $b < \lambda$, the wavelets at the slit are as if from one point, and the wave spreads as a semicircle over the whole area behind the slit. Already when the slit is about as wide as the wavelength, $b \approx \lambda$, the wave spreads a lot.

<svg data-fig="diffraktio" viewBox="0 0 600 360" role="img" aria-label="Diagram, not to scale: a plane wave arrives from the left at an obstacle with a slit, seen from above. On the left the slit is about four wavelengths wide: at the slit the wavefronts continue straight, and only at the edges do they curve slightly into the shadow. Small Huygens wavelets are drawn at points of the slit. On the right the slit is narrower than the wavelength: behind the slit the wavefronts are semicircles, and the wave spreads over the whole area behind the slit." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-diffraktio.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="121" y="7.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b \approx 4\lambda$</div></foreignObject>
  <foreignObject x="427.5" y="7.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b < \lambda$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/ripple-model-single-slit.webp" alt="A computed picture of a water surface seen from above. On the left there are vertical light and dark stripes. In the middle there is a vertical barrier with a narrow slit. On the right of the barrier, semicircular rings spread from the slit and fill the whole right side."><figcaption>A computed model picture of a ripple tank seen from above: the light stripes are crests and the dark ones troughs. A plane wave from the left passes through a slit one wavelength wide, and behind the slit the wave spreads in semicircles over the whole region. In reality the wave behind the slit is weaker; for clarity the picture shows it with the same contrast, and the wave reflected from the barrier is not drawn.</figcaption></figure>

The same holds for an obstacle. An obstacle narrower than the wavelength, like a pier post, leaves hardly any shadow behind it, because the wave bends around it. Behind an obstacle much wider than the wavelength there is a sheltered region. So diffraction is strong when the width of the slit or obstacle is of the order of the wavelength or smaller. Sound bends from a door into a corridor, because the wavelength of speech is of the order of a metre, as wide as the doorway.

```pysahdy
Sea waves have a wavelength of $20\,\text{m}$ and a pier post is $0.50\,\text{m}$ wide. Is there a clear calm region behind the post?
---
No. The post is much narrower than the wavelength, so the wave bends around it and meets again behind it.
```

## Formula: Law of reflection
When a wave hits a flat surface, such as a wall or a sea wall, the **normal** of the surface, that is the line perpendicular to the surface, is drawn at the point of impact. Angles are always measured from the normal: the angle of incidence is the angle between the incoming ray and the normal, and the angle of reflection is the angle between the reflected ray and the normal. The law of reflection is
```latex
\beta = \alpha
```
where $\alpha$ is the angle of incidence and $\beta$ the angle of reflection. In addition, the incoming ray, the reflected ray and the normal are in the same plane, and the reflected ray is on the other side of the normal from the incoming one. The angle between the ray and the surface is $90^\circ - \alpha$, and it is not used as the angle of incidence.

<svg data-fig="heijastuslaki" viewBox="0 0 600 340" role="img" aria-label="Diagram: the incoming ray hits the surface of the wall at point O, and the reflected ray leaves from it. At O the normal of the surface, the line perpendicular to the surface, is drawn with a dashed line. The angle of incidence alpha is the angle between the incoming ray and the normal, and the angle of reflection beta the angle between the reflected ray and the normal; both are 40 degrees. In grey is marked the angle between the ray and the surface, 90 degrees minus alpha, which is not used as the angle of incidence." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-heijastuslaki.webp" x="6.1" y="3.7" width="588.2" height="340.7" preserveAspectRatio="none"/>
  <foreignObject x="258.5" y="33.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{normal}$</div></foreignObject>
  <foreignObject x="257" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\alpha$</div></foreignObject>
  <foreignObject x="323" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\beta$</div></foreignObject>
  <foreignObject x="88" y="183.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$90^\circ - \alpha$</div></foreignObject>
  <foreignObject x="290" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="20" y="57.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{incoming ray}$</div></foreignObject>
  <foreignObject x="422" y="57.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{reflected ray}$</div></foreignObject>
  <foreignObject x="522" y="225.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{wall}$</div></foreignObject>
</svg>

Huygens' principle explains why the angles are equal. The front $AB$ of a plane wave hits the wall obliquely, so its point $A$ touches the wall first. A wavelet starts from it while the other end $B$ of the front is still some distance away. When $B$ arrives at the wall at point $C$, the wavelet that started from $A$ has travelled the same distance, because the speed is the same. The reflected front $CD$ touches the wavelets. The triangles $ABC$ and $CDA$ are congruent: they have the common side $AC$, equally long sides $BC$ and $AD$, and a right angle at $B$ and $D$. So the fronts make equal angles with the wall. The angle between the front and the wall is equal to the angle between the ray and the normal, so $\beta = \alpha$.

<svg data-fig="huygens" viewBox="0 0 600 350" role="img" aria-label="Diagram: Huygens&#x27; principle explains the law of reflection. The wavefront AB of a plane wave hits the wall obliquely: point A is already at the wall while point B is still some distance away. When B travels along the ray to the wall at point C, the wavelet that started from A has travelled an equal distance, and its radius is equal to the distance BC. A smaller wavelet is also drawn from the midpoint of A and C. The reflected wavefront CD touches the wavelets. The front AB makes the angle alpha with the wall and the front CD the angle beta, and the angles are equal." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-huygens.webp" x="1.2" y="1.2" width="597" height="358.2" preserveAspectRatio="none"/>
  <foreignObject x="197.5" y="257" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\alpha$</div></foreignObject>
  <foreignObject x="391.5" y="257" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\beta$</div></foreignObject>
  <foreignObject x="108" y="263.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="481" y="263.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="347" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$B$</div></foreignObject>
  <foreignObject x="242" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$D$</div></foreignObject>
  <foreignObject x="148.5" y="37.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{wavelet}$</div></foreignObject>
</svg>

## Worked example
Sea waves approach a straight breakwater so that the wavefronts make an angle of $50^\circ$ with the wall of the breakwater. What are the angle of incidence and the angle of reflection of the waves, and what angle is left between the direction of travel of the reflected waves and the wall of the breakwater?

<!-- vaihe -->

**Given and find.** The angle between the wavefront and the wall is $\varphi = 50^\circ$.

We are asked for the angle of incidence $\alpha$, the angle of reflection $\beta$, and the angle $\gamma$ between the reflected ray and the surface of the wall.

<!-- vaihe -->

**Principle.** A ray is perpendicular to the wavefront and the normal is perpendicular to the wall. When both lines are turned through $90^\circ$, the angle between them does not change, so the angle between the ray and the normal is the same as the angle between the front and the wall.

By the law of reflection the angle of reflection is equal to the angle of incidence when both are measured from the normal.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\alpha = \varphi \\
&\beta = \alpha \\
&\gamma = 90^\circ - \beta
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: all angles are in degrees.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\alpha = 50^\circ \\
&\beta = 50^\circ \\
&\gamma = 90^\circ - 50^\circ = 40^\circ
\end{aligned}
```

<!-- vaihe -->

**Result.** The angle of incidence and the angle of reflection are $50^\circ$, and the reflected waves travel at an angle of $40^\circ$ to the wall of the breakwater. The angles are given in whole degrees like the given $50^\circ$.

<!-- vaihe -->

**Reasonableness.** If the fronts were parallel to the wall, that is $\varphi = 0^\circ$, the waves would arrive perpendicularly and return along the same path, $\alpha = \beta = 0^\circ$. As $\varphi$ grows, the waves arrive more and more obliquely. In addition $\alpha + \gamma = 90^\circ$, as it should for the right angle between the normal and the surface.

## Common misconception
The most common error is to measure the angle of incidence from the surface and not from the normal. If a ray makes an angle of $30^\circ$ with the wall, the angle of incidence is not $30^\circ$ but $90^\circ - 30^\circ = 60^\circ$. So always draw the normal at the point of impact first. Another error is to think that a wave bends only at a very narrow slit and a wide slit lets it through completely straight. There is diffraction at every slit and at the edge of every obstacle, but it shows clearly only when the width of the slit is of the order of the wavelength. A third error is to think that a fixed end damps the pulse. From a rigid fastening the pulse is reflected almost completely, but inverted.

## Summary
- A wavefront joins the points that are in the same phase, and a ray shows the direction of travel perpendicular to the front.
- The law of reflection: $\beta = \alpha$, when the angle of incidence and the angle of reflection are measured from the normal of the surface.
- From the fixed end of a rope the pulse is reflected inverted, from the free end not inverted.
- Huygens' principle: every point of a wavefront is the source of a wavelet, and the new front touches the wavelets. The principle explains reflection and diffraction.
- Diffraction, the bending of a wave behind a slit or an obstacle, is strong when the width of the slit or obstacle is about the wavelength or smaller.
