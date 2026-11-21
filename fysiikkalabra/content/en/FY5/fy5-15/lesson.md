# Intensity and the decibel scale

> **Why** is the loudness of a sound given in decibels and not in watts per square metre, and what does a decibel reading actually tell us?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an open-air concert in the afternoon. On both sides of the stage are loudspeaker towers, and an audience stands in front of them. Ever wider arcs spread out from the loudspeakers. Two listeners sit far away on the hillside on the right, where the arcs reaching them are pale." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-15-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Intensity: power per unit area
Sound is a wave travelling in air that carries energy from the source to the listener. How loud a sound seems depends on how much energy per second hits, for example, the surface of the eardrum or of a microphone. That is why the loudness of a sound is described by the **intensity** $I$: it is the sound power $P$ passing through a surface divided by the area $A$ of the surface, when the surface is perpendicular to the direction in which the sound travels. The unit of intensity is watt per square metre, $\text{W/m}^2$. The same power concentrated on a small area means a large intensity, and spread over a large area a small one.

### A point source and distance
A small sound source that radiates evenly in all directions is a point source. When there are no reflections and the air does not absorb the sound, the whole power $P$ of the source passes through every spherical surface around the source. The area of a sphere, $4\pi r^2$, grows as the square of the distance $r$: at twice the distance the same power is spread over four times the area, at three times the distance over nine times the area. The intensity is therefore inversely proportional to the square of the distance. This is the **inverse-square law**. In reality walls and the ground reflect sound, so indoors the intensity decreases more slowly.

<svg data-fig="kartio" viewBox="0 0 600 340" role="img" aria-label="Schematic figure, not to scale: a point sound source on the left. Rays from it bound a cone that cuts three squares at distances r, 2r and 3r. The nearest square is one cell with an area A. At distance 2r the same cone covers four cells of the same size, that is an area 4A, and at distance 3r nine cells, that is 9A. The same power is spread over an ever larger area, so the intensity is I, I/4 and I/9; the colour of the cells becomes paler in the same proportion." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-15-kartio.webp" x="1.2" y="1.2" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="42" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="176.5" y="115.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A,\ I$</div></foreignObject>
  <foreignObject x="316" y="86" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4A,\ I/4$</div></foreignObject>
  <foreignObject x="475" y="56" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$9A,\ I/9$</div></foreignObject>
  <foreignObject x="192" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="335.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2r$</div></foreignObject>
  <foreignObject x="485.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3r$</div></foreignObject>
  <foreignObject x="42" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/sound-level-meter-park.webp" alt="People sit on benches under trees in a park. A red digital display on a post reads 62 dB."><figcaption>A noise display in the People's Park in Chengdu, China. The display shows the sound level in decibels. Such meters usually show the A-weighted sound pressure level. Outdoors in a free sound field the unweighted sound pressure level is numerically about the same as the sound intensity level; an A-weighted reading can differ from it, especially at low frequencies. $62\,\text{dB}$ is about the level of normal conversation.</figcaption></figure>

```pysahdy
Why does the intensity decrease farther from a point source, even though the power of the source stays the same?
---
The same power is spread over an ever larger spherical surface. The area is larger, so the power per unit area, the intensity, is smaller.
```

### Threshold of hearing and threshold of pain
The human ear is astonishingly sensitive. The weakest sound that a young person with normal hearing can distinguish at a frequency of about $1000\,\text{Hz}$ has an intensity of about $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$. This is called the **threshold of hearing**. The threshold of hearing is not silence but the weakest audible sound, and it is different at different frequencies. The loudest sounds begin to feel painful when the intensity is about $1\,\text{W/m}^2$. This threshold of pain is a trillion, that is $10^{12}$, times the threshold of hearing. Such a wide range is hard to present on an ordinary scale. Both thresholds vary from person to person and with frequency, so these values are agreed approximate values, not constants of nature.

### The decibel scale
Because the range is so wide, the loudness of a sound is described by the **sound intensity level** $L$, which compares the intensity with the threshold of hearing by means of a logarithm. The unit of the level is the **decibel** ($\text{dB}$). At the threshold of hearing the level is about $0\,\text{dB}$, at the threshold of pain about $120\,\text{dB}$. The scale is logarithmic: every time the intensity increases tenfold, $10\,\text{dB}$ is added to the level. A conversation, about $60\,\text{dB}$, is therefore not half of the threshold of pain but a millionth of its intensity. The ear also senses loudness roughly logarithmically: an increase of about $10\,\text{dB}$ sounds roughly twice as loud, even though the intensity increases tenfold.

<svg data-fig="asteikko" viewBox="0 0 600 396" role="img" aria-label="Schematic figure: the scale of the sound intensity level as a vertical bar that darkens from bottom to top. At the bottom 0 dB, that is an intensity of 10 to the power minus 12 watts per square metre, the threshold of hearing. For every 20 decibels the intensity is a hundred times greater: 20 dB whisper, 40 dB quiet room, 60 dB conversation, 80 dB busy street, 100 dB chainsaw and at the top 120 dB, that is 1 watt per square metre, the threshold of pain. The example sounds are typical orders of magnitude." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy515-bar" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ffc078" stop-opacity="0.35"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <foreignObject x="284" y="7.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{dB})$</div></foreignObject>
  <foreignObject x="400" y="7.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{W/m}^2)$</div></foreignObject>
  <rect x="236" y="68" width="32" height="300" rx="4" fill="url(#fy515-bar)" stroke="#1f2933" stroke-width="2"/>
  <line x1="230" y1="368" x2="236" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="368" x2="274" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="14" y="353.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{hearing threshold}$</div></foreignObject>
  <foreignObject x="284" y="353.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="400" y="353.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-12}$</div></foreignObject>
  <line x1="230" y1="318" x2="236" y2="318" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="318" x2="274" y2="318" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="127" y="303.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{whisper}$</div></foreignObject>
  <foreignObject x="284" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="400" y="303.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-10}$</div></foreignObject>
  <line x1="230" y1="268" x2="236" y2="268" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="268" x2="274" y2="268" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="102" y="253.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{quiet room}$</div></foreignObject>
  <foreignObject x="284" y="253.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="400" y="253.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-8}$</div></foreignObject>
  <line x1="230" y1="218" x2="236" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="218" x2="274" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="203.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{conversation}$</div></foreignObject>
  <foreignObject x="284" y="203.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="400" y="203.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-6}$</div></foreignObject>
  <line x1="230" y1="168" x2="236" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="168" x2="274" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="89" y="153.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{busy street}$</div></foreignObject>
  <foreignObject x="284" y="153.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="400" y="153.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-4}$</div></foreignObject>
  <line x1="230" y1="118" x2="236" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="118" x2="274" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="114" y="103.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{chainsaw}$</div></foreignObject>
  <foreignObject x="284" y="103.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="400" y="103.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-2}$</div></foreignObject>
  <line x1="230" y1="68" x2="236" y2="68" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="68" x2="274" y2="68" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="53.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{pain threshold}$</div></foreignObject>
  <foreignObject x="284" y="53.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$120$</div></foreignObject>
  <foreignObject x="400" y="53.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1$</div></foreignObject>
</svg>

```pysahdy
The intensity of a sound becomes a thousand times greater. By how many decibels does the level increase?
---
A thousandfold increase is three tenfold increases in a row. The level increases by $3 \cdot 10\,\text{dB} = 30\,\text{dB}$.
```

The ear is not equally sensitive to all frequencies: low and very high sounds seem quieter at the same intensity than sounds of about $1000$–$4000\,\text{Hz}$. Sound level meters therefore weight the frequencies according to the sensitivity of the ear, and such a weighted reading is written $\text{dB(A)}$. Ordinary sound level meters often show the A-weighted sound pressure level. In this chapter we calculate unweighted sound intensity levels.

### What a meter measures
The microphone of a meter does not measure intensity but sound pressure, the variation of air pressure. From it the **sound pressure level** is calculated, which compares the sound pressure with the reference pressure $p_0 = 20\,\mu\text{Pa}$, whereas the sound intensity level compares the intensity with the reference intensity $I_0$. The levels are related, but they are not the same quantity. In a freely travelling sound wave, for example outdoors far from reflecting surfaces, the numerical values of the unweighted sound pressure level and the sound intensity level are about the same with these reference values. In a reverberant room reflected waves travel in many directions: they increase the sound pressure, but their energy flows partly cancel, so the levels can differ. The calculations of this chapter assume an ideal sound field: sound travels freely without reflections, and the meter reading is treated as the sound intensity level. The effects of noise and the protection of hearing are covered in the chapter *Noise, acoustics and sound reproduction*.

## Formula: Sound intensity level

### Intensity
The intensity of a sound is
```kaavat
intensity :: I = \frac{P}{A}
```
where $I$ is the intensity ($\text{W/m}^2$), $P$ the sound power passing through the surface ($\text{W}$) and $A$ the area of the surface ($\text{m}^2$). For a point source that radiates evenly in all directions without reflections, $A$ is the area of a sphere, $4\pi r^2$:
```latex
I = \frac{P}{4\pi r^2}
```
where $P$ is the sound power of the source ($\text{W}$) and $r$ the distance from the source ($\text{m}$).

### Sound intensity level
The sound intensity level in decibels is
```kaavat
sound intensity level :: L = 10\lg\left(\frac{I}{I_0}\right)\,\text{dB}
```
where $L$ is the sound intensity level ($\text{dB}$), $I$ the intensity and $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$ the agreed reference intensity, which corresponds approximately to the threshold of hearing. The notation $\lg$ is the base-ten logarithm: $\lg x$ tells you to what power $10$ must be raised to get $x$. For example $\lg 1000 = 3$, because $10^3 = 1000$, and $\lg 1 = 0$, so $I = I_0$ gives the level $0\,\text{dB}$.

### Intensity from a known level
When the level is known, the intensity is solved in two steps. First the equation is divided on both sides by $10\,\text{dB}$. Then the definition of the logarithm is used: if $\lg x = y$, then $x = 10^y$. Finally we multiply by $I_0$:
```latex
\begin{aligned}
&\lg \frac{I}{I_0} = \frac{L}{10\,\text{dB}} \\
&\frac{I}{I_0} = 10^{\,L/(10\,\text{dB})} \\
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})}
\end{aligned}
```
For example, the $60\,\text{dB}$ of a conversation gives $\tfrac{L}{10\,\text{dB}} = 6$, so $I = 10^{6} \cdot I_0 = 1.0 \cdot 10^{-6}\,\text{W/m}^2$. On a calculator the logarithm is the key $\lg$ (or $\log$) and the power $10^x$ is usually the second function of the same key; check that $\lg 3 \approx 0.477$ and $10^{0.477} \approx 3$.

### Difference in levels
The difference between the levels of two sounds depends only on the ratio of their intensities, because $I_0$ cancels:
```latex
L_2 - L_1 = 10\,\text{dB} \cdot \lg \frac{I_2}{I_1}
```
When the intensity doubles, the level increases by $10\,\text{dB} \cdot \lg 2 \approx 3.0\,\text{dB}$. When it increases tenfold, the level increases by $10\,\text{dB}$. When the distance from a point source doubles, the intensity falls to a quarter and the level decreases by $10\,\text{dB} \cdot \lg 4 \approx 6.0\,\text{dB}$.

<svg data-fig="kuvaaja" viewBox="0 0 600 420" role="img" aria-label="Graph to scale: the sound intensity level L in decibels of a point sound source as a function of the distance r from zero to ten metres, when the power of the source is 12.6 milliwatts. The curve falls first steeply and then gently. The points at distances 1, 2, 4 and 8 metres are 90.0, 84.0, 78.0 and 71.9 dB: every time the distance doubles, the level decreases by about 6 dB." style="max-width:100%;font-size:24px">
  <line x1="149" y1="376" x2="149" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="188" y1="376" x2="188" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="227" y1="376" x2="227" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266" y1="376" x2="266" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="305" y1="376" x2="305" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="344" y1="376" x2="344" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383" y1="376" x2="383" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="422" y1="376" x2="422" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="461" y1="376" x2="461" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="376" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="345.5" x2="500" y2="345.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="315" x2="500" y2="315" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="284" x2="500" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="253.5" x2="500" y2="253.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="223" x2="500" y2="223" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="192.5" x2="500" y2="192.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="162" x2="500" y2="162" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="131" x2="500" y2="131" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="100.5" x2="500" y2="100.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="70" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109" y1="376" x2="514" y2="376" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,376 L513,382 L513,370 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="377" x2="110" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,44 L116,57 L104,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="149" y1="376" x2="149" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="188" y1="376" x2="188" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="178" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="227" y1="376" x2="227" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="266" y1="376" x2="266" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="256" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="305" y1="376" x2="305" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="344" y1="376" x2="344" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="334" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="383" y1="376" x2="383" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="422" y1="376" x2="422" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="412" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="461" y1="376" x2="461" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="376" x2="500" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="385.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="103" y1="345.5" x2="110" y2="345.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="331" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="103" y1="315" x2="110" y2="315" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="300.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="103" y1="284" x2="110" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="269.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="103" y1="253.5" x2="110" y2="253.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="239" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="103" y1="223" x2="110" y2="223" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="208.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="103" y1="192.5" x2="110" y2="192.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="178" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="103" y1="162" x2="110" y2="162" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$70$</div></foreignObject>
  <line x1="103" y1="131" x2="110" y2="131" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="103" y1="100.5" x2="110" y2="100.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="86" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$90$</div></foreignObject>
  <line x1="103" y1="70" x2="110" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="53" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="80" y="381.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="361.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{m})$</div></foreignObject>
  <foreignObject x="100" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{dB})$</div></foreignObject>
  <polyline points="149,100.5 152,102.5 155,104.5 158,106 160.5,107.5 163.5,109 166.5,110.5 169.5,112 172.5,113 175.5,114.5 178,115.5 181,116.5 184,117.5 187,118.5 190,119.5 193,120.5 196,121.5 198.5,122.5 201.5,123.5 204.5,124 207.5,125 210.5,125.5 213.5,126.5 216.5,127 219,128 222,128.5 225,129.5 228,130 231,130.5 234,131.5 237,132 239.5,132.5 242.5,133 245.5,133.5 248.5,134.5 251.5,135 254.5,135.5 257,136 260,136.5 263,137 266,137.5 269,138 272,138.5 275,139 277.5,139.5 280.5,140 283.5,140.5 286.5,140.5 289.5,141 292.5,141.5 295,142 298,142.5 301,143 304,143 307,143.5 310,144 313,144.5 315.5,145 318.5,145 321.5,145.5 324.5,146 327.5,146.5 330.5,146.5 333.5,147 336,147.5 339,147.5 342,148 345,148.5 348,148.5 351,149 354,149.5 356.5,149.5 359.5,150 362.5,150 365.5,150.5 368.5,151 371.5,151 374,151.5 377,151.5 380,152 383,152.5 386,152.5 389,153 392,153 394.5,153.5 397.5,153.5 400.5,154 403.5,154 406.5,154.5 409.5,155 412,155 415,155.5 418,155.5 421,156 424,156 427,156.5 430,156.5 432.5,157 435.5,157 438.5,157 441.5,157.5 444.5,157.5 447.5,158 450.5,158 453,158.5 456,158.5 459,159 462,159 465,159.5 468,159.5 471,159.5 473.5,160 476.5,160 479.5,160.5 482.5,160.5 485.5,161 488.5,161 491,161 494,161.5 497,161.5 500,162" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="149" y1="100.5" x2="149" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="100.5" x2="149" y2="100.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="149" cy="100.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="157" y="46" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$90.0$</span></div></foreignObject>
  <line x1="188" y1="119" x2="188" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="119" x2="188" y2="119" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="188" cy="119" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="196" y="82.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$84.0$</span></div></foreignObject>
  <line x1="266" y1="137.5" x2="266" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="137.5" x2="266" y2="137.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="266" cy="137.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="274" y="101" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$78.0$</span></div></foreignObject>
  <line x1="422" y1="156" x2="422" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="156" x2="422" y2="156" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="422" cy="156" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="430" y="119.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$71.9$</span></div></foreignObject>
</svg>

### Combined level of several sources
When two independent sound sources, for example two machines or two players, are heard at the same place, their powers and therefore their intensities add up: $I = I_1 + I_2$. Decibels are not added; the combined level is calculated from the total intensity. Two equally strong sources double the intensity, so $80\,\text{dB}$ and $80\,\text{dB}$ together give about $83\,\text{dB}$. If one source is much weaker, it hardly changes the level: $70\,\text{dB}$ and $60\,\text{dB}$ give an intensity of $1.1 \cdot 10^{-5}\,\text{W/m}^2$, that is about $70.4\,\text{dB}$. The rule does not apply to two loudspeakers that play the same pure tone in phase: their waves interfere as in the chapter *When waves combine: superposition and interference*, so they reinforce each other at some places and weaken each other at others.

<svg data-fig="summa" viewBox="0 0 600 360" role="img" aria-label="Two bar charts to scale. On the left the intensities in units of 10 to the power minus 4 watts per square metre: each loudspeaker alone 1.0 and together 2.0, so the combined bar is twice as tall. On the right the same situations as sound intensity levels: each alone 80 dB and together 83 dB, so the combined bar is only slightly taller." style="max-width:100%;font-size:24px">
  <line x1="300" y1="14" x2="300" y2="346" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="40" y="11.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (10^{-4}\,\text{W/m}^2)$</div></foreignObject>
  <line x1="32" y1="300" x2="284" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="52" y="200" width="52" height="100" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="55.5" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.0$</div></foreignObject>
  <foreignObject x="61.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_1$</div></foreignObject>
  <rect x="122" y="200" width="52" height="100" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="125.5" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.0$</div></foreignObject>
  <foreignObject x="131.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_2$</div></foreignObject>
  <rect x="196" y="100" width="52" height="200" rx="3" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="199.5" y="67.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.0$</div></foreignObject>
  <foreignObject x="187" y="309.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_1 + I_2$</div></foreignObject>
  <foreignObject x="330" y="11.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{dB})$</div></foreignObject>
  <line x1="318" y1="300" x2="584" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="340" y="140" width="52" height="160" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="349.5" y="107.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="349.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L_1$</div></foreignObject>
  <rect x="410" y="140" width="52" height="160" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="419.5" y="107.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="419.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L_2$</div></foreignObject>
  <rect x="486" y="134" width="52" height="166" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="495.5" y="101.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$83$</div></foreignObject>
  <foreignObject x="502" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
</svg>

```pysahdy
Two identical machines are running at the same time, and one of them is switched off. Does the level drop to half?
---
No. The intensity halves, and the level drops by only about $3\,\text{dB}$.
```

## Worked example
At an open-air concert a decibel meter reads $96\,\text{dB}$ at a distance of $10\,\text{m}$ from a loudspeaker tower. What is the intensity of the sound at the meter, and what is the sound power of the loudspeaker tower? Assume that the tower radiates like a point source evenly in all directions and the sound is neither reflected nor absorbed, so the meter reading can be treated as the sound intensity level.

<!-- vaihe -->

**Given and asked.** The meter reading, which in a free sound field is the sound intensity level, is $L = 96\,\text{dB}$, the distance $r = 10\,\text{m}$ and the threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$. We are asked for the intensity $I$ and the sound power $P$ of the source.

<!-- vaihe -->

**Principle.** The sound intensity level compares the intensity with the threshold of hearing, so the intensity is obtained by solving it from the level equation: first we divide by $10\,\text{dB}$, then we use the definition of the logarithm. Because the tower radiates evenly in all directions, the whole power passes through a spherical surface of radius $10\,\text{m}$, and $I = \tfrac{P}{4\pi r^2}$.

<!-- vaihe -->

**Formula solved.** From the level equation we get $\lg \tfrac{I}{I_0} = \tfrac{L}{10\,\text{dB}}$, and the definition of the logarithm gives the intensity. The power is obtained by multiplying the intensity by the area of the sphere:
```latex
\begin{aligned}
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})} \\[6pt]
&P = I \cdot 4\pi r^2
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: the distance is in metres and the threshold of hearing in $\text{W/m}^2$. The decibels cancel in the quotient:
```latex
\begin{aligned}
&\dfrac{L}{10\,\text{dB}} \\
&= \dfrac{96\,\text{dB}}{10\,\text{dB}} \\
&= 9.6
\end{aligned}
```

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})} \\
&= 1.0 \cdot 10^{-12}\,\tfrac{\text{W}}{\text{m}^2} \cdot 10^{9.6} \\
&= 3.98 \cdot 10^{-3}\,\tfrac{\text{W}}{\text{m}^2} \\[6pt]
&P = I \cdot 4\pi r^2 \\
&= 3.98 \cdot 10^{-3}\,\tfrac{\text{W}}{\text{m}^2} \cdot 4\pi \cdot (10\,\text{m})^2 \\
&= 5.00\,\text{W}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The intensity is about $4.0 \cdot 10^{-3}\,\text{W/m}^2$ and the sound power of the loudspeaker tower about $5.0\,\text{W}$. The results are given to two significant figures, because the level $96\,\text{dB}$ is given in whole decibels: a difference of just $1\,\text{dB}$ in the level would change the intensity and the power by about a quarter. So the level limits the precision. In the example the distance $10\,\text{m}$ is treated as an exact value.

<!-- vaihe -->

**Reasonableness.** The level $96\,\text{dB}$ lies between the levels $90\,\text{dB}$ and $100\,\text{dB}$, so the intensity must be between $10^{-3}$ and $10^{-2}\,\text{W/m}^2$, and $4.0 \cdot 10^{-3}\,\text{W/m}^2$ is. A sound power of $5\,\text{W}$ seems small, but a loudspeaker typically converts only about $1\,\%$ of its electric power into sound, so the amplifiers of the tower have a power of hundreds of watts.

## Common misconception
Many people add decibels like ordinary numbers. Two machines that each produce $80\,\text{dB}$ alone do not produce $160\,\text{dB}$ together, which would be a sound louder than a jet aircraft. It is the intensities that are added: the intensity doubles, and the level rises by only about $3\,\text{dB}$, to $83\,\text{dB}$.

Another mistake is to think that a double decibel reading means a double sound. A level of $120\,\text{dB}$ is $60\,\text{dB}$ greater than $60\,\text{dB}$, so the intensity is $10^6$, that is a million times greater. A third mistake is to believe that $0\,\text{dB}$ means there is no sound. It means the intensity of the threshold of hearing, $I_0$; for even weaker sounds the level is negative.

## Summary
- Intensity is power per unit area: $I = \tfrac{P}{A}$, unit $\text{W/m}^2$. For a point source without reflections $I = \tfrac{P}{4\pi r^2}$: twice the distance gives a quarter of the intensity.
- The reference intensity $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$ corresponds approximately to the threshold of hearing, the weakest audible sound, and the threshold of pain is about $1\,\text{W/m}^2$. The thresholds are agreed approximate values that vary with the person and the frequency.
- A sound level meter measures the sound pressure level (often A-weighted, $\text{dB(A)}$). In a freely travelling wave the unweighted sound pressure level is numerically about the same as the sound intensity level, in a reverberant room not necessarily.
- The sound intensity level is $L = 10\lg\left(\tfrac{I}{I_0}\right)\,\text{dB}$. Doubling the intensity raises the level by about $3\,\text{dB}$, a tenfold intensity by $10\,\text{dB}$.
- Intensity from the level: $I = I_0 \cdot 10^{\,L/(10\,\text{dB})}$.
- The intensities of independent sources are added, the decibels are not.
