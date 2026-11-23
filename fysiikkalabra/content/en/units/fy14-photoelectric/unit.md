# Light as particles: the photoelectric effect

> **Why** can a dim violet lamp free electrons from a metal plate when a bright red lamp cannot?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a darkened laboratory. On a bench stands an evacuated glass tube with a sealed tip, and a grey metal plate lies inside it. On the left, a large lamp shines a wide, bright red beam onto the left half of the plate. On the right, a small lamp shines a narrow, dim violet beam onto the right half. Small blue electrons fly up from the plate only where the violet light falls; under the bright red light the plate stays quiet." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-photoelectric-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## The puzzle: what the wave model predicted {Puzzle}

Around 1900, physicists were sure that light is an electromagnetic **wave**. The energy that a wave carries depends on its **intensity**, that is, on how much energy arrives on each square metre every second. Brighter light means a larger wave amplitude and more energy.

In 1887 Heinrich Hertz noticed that ultraviolet light helps sparks jump between two metal electrodes. Later experiments showed what was happening: light falling on a metal surface frees electrons from it. This is the **photoelectric effect**, and the freed electrons are called **photoelectrons**. In 1902 Philipp Lenard found that the energy of the photoelectrons does not depend on the intensity of the light.

The wave model made clear predictions, and the experiments did not agree with them:

| What changes | The wave model predicts | Experiments show |
| --- | --- | --- |
| brighter light | faster electrons | more electrons, not faster |
| bright red light | electrons leave | no electrons at all |
| very dim violet light | a delay | electrons at once |
| higher frequency | no change | faster electrons |

So the largest kinetic energy of the electrons does not depend on the intensity, but it grows with the **frequency** of the light. Below a **threshold frequency** no electrons leave the metal, however bright the light is. Brighter light frees more electrons every second: the current is proportional to the intensity.

Classical physics had no answer to these observations. A new idea was needed.

## Key idea

In 1905 Albert Einstein suggested that light carries its energy in small packets. Today we call these packets **photons**. The energy of one photon depends only on the frequency $f$ of the light: ${E = hf}$, where $h$ is **Planck's constant**. Violet light has a higher frequency than red light, so a violet photon carries more energy than a red one.

When light falls on a metal, one photon gives all its energy to one electron. The electron needs a minimum energy to escape from the metal surface. This energy is called the **work function** $W$, and it is different for different metals. If $hf < W$, the electron cannot escape, and it soon loses the energy as heat in the metal. If $hf > W$, the electron can leave, and the rest of the photon's energy becomes its kinetic energy.

```pysahdy
If $hf < W$, what happens to the energy of the absorbed photon?
---
The electron cannot escape, so it soon loses the energy as heat in the metal.
```

<svg data-fig="energy" viewBox="0 0 600 384" role="img" aria-label="Energy diagram to scale for sodium, work function 2.36 eV. Left: red light of wavelength 650 nm. The photon energy hf = 1.91 eV is drawn as an arrow from the electron in the metal; it ends below the dashed line of the energy needed to get out of the metal, so the electron stays. Right: violet light of 400 nm. The arrow hf = 3.10 eV reaches above the dashed line: the first 2.36 eV, the work function W, frees the electron, and the remaining 0.74 eV is the largest kinetic energy E_k,max the electron can have. The dashed line is labelled free electron." style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-photoelectric-energy.webp" x="1.2" y="1.2" width="597" height="391.8" preserveAspectRatio="none"/>
  <foreignObject x="96" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda = 650\,\text{nm}$</div></foreignObject>
  <foreignObject x="35" y="326.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{metal}$</div></foreignObject>
  <foreignObject x="140" y="326.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = 2.36\,\text{eV}$</div></foreignObject>
  <foreignObject x="130" y="122.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{free electron}$</div></foreignObject>
  <foreignObject x="12" y="221" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="120" y="246.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$hf = 1.91\,\text{eV}$</div></foreignObject>
  <foreignObject x="120" y="178" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$hf < W$</div></foreignObject>
  <foreignObject x="396" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda = 400\,\text{nm}$</div></foreignObject>
  <foreignObject x="335" y="326.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{metal}$</div></foreignObject>
  <foreignObject x="440" y="326.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = 2.36\,\text{eV}$</div></foreignObject>
  <foreignObject x="312" y="221" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="420" y="235" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$hf = 3.10\,\text{eV}$</div></foreignObject>
  <foreignObject x="432" y="86.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_{\text{k,max}}$</div></foreignObject>
  <foreignObject x="432" y="114.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$= 0.74\,\text{eV}$</div></foreignObject>
</svg>

The photon model explains every observation in the table. Brighter light means *more* photons every second, not *bigger* photons. So more electrons leave, and the current grows, but each electron still gets the energy of just one photon. One photon is absorbed at once, so there is no delay. And if one photon is too small, many photons do not help, because an electron practically never collects the energy of two photons.

Energies at the scale of one electron are small, so physicists measure them in **electronvolts**: $1\ \text{eV}$ is the energy an electron gains when it moves through a voltage of one volt, ${1\ \text{eV} = 1.602 \cdot 10^{-19}\ \text{J}}$. A photon of visible light has an energy of about $1.6\text{–}3.3\ \text{eV}$.

```pysahdy
An electron moves through a voltage of $2.0\,\text{V}$. How much energy does it gain in electronvolts?
---
It gains $2.0\,\text{eV}$, because $1\,\text{eV}$ is the energy gained through a voltage of one volt.
```

## Formula: Einstein's photoelectric equation

The energy of a photon of frequency $f$ and wavelength $\lambda$ is
```latex
E = hf = \frac{hc}{\lambda}
```
where ${h = 6.626 \cdot 10^{-34}\ \text{J} \cdot \text{s}}$ is Planck's constant and ${c = 2.998 \cdot 10^{8}\ \text{m/s}}$ is the speed of light. Energy is conserved when the photon frees an electron:
```latex
\begin{aligned}
hf &= W + E_{\text{k,max}} \\
E_{\text{k,max}} &= hf - W
\end{aligned}
```
where $W$ is the work function of the metal and $E_{\text{k,max}}$ is the **largest kinetic energy** of the photoelectrons. Most electrons leave with less, because they lose some energy on their way to the surface. Electrons leave only when $hf > W$, so the threshold frequency is ${f_0 = W/h}$.

### Measuring the energy with a stopping voltage

In a photocell, a **retarding voltage** $U$ between the metal plate and the collector pushes the electrons back. An electron with the charge ${e = 1.602 \cdot 10^{-19}\ \text{C}}$ loses the energy $eU$ on its way. When $U$ is large enough, even the fastest electrons turn back and the current $I$ falls to zero. This voltage is the **stopping voltage** $U_\text{s}$:
```latex
\begin{aligned}
eU_\text{s} &= E_{\text{k,max}} = hf - W \\
U_\text{s} &= \frac{h}{e}\,f - \frac{W}{e}
\end{aligned}
```
So the stopping voltage is a straight-line function of the frequency, and the slope of the line is $h/e$. It is the same for every metal. The work function only moves the line sideways.

```pysahdy
Two metals have different work functions. Why do their $U_\text{s}$–$f$ lines have the same slope?
---
The slope $h/e$ contains only constants. The work function appears only in the term $-W/e$, so it moves the line sideways.
```

<svg data-fig="usf" viewBox="0 0 600 360" role="img" aria-label="Graph of model values, to scale: the stopping voltage U_s in volts against the frequency f in units of 10^14 Hz, from 0 to 14. Two straight, parallel lines: sodium starts on the frequency axis at its threshold frequency 5.71 · 10^14 Hz and zinc at 10.4 · 10^14 Hz. Five points on the sodium line are the wavelengths 500, 450, 400, 350 and 300 nm. A triangle on the sodium line shows that the stopping voltage rises by 1.65 V when the frequency rises by 4 · 10^14 Hz; this slope is h/e and is the same for both metals. The threshold frequency f_0 of each metal is marked where its line meets the axis." style="max-width:100%;font-size:24px">
  <line x1="132.5" y1="300" x2="132.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="181" y1="300" x2="181" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="229.5" y1="300" x2="229.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="278.5" y1="300" x2="278.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="327" y1="300" x2="327" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375.5" y1="300" x2="375.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424" y1="300" x2="424" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="265.5" x2="424" y2="265.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="231" x2="424" y2="231" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="196.5" x2="424" y2="196.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="161.5" x2="424" y2="161.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="127" x2="424" y2="127" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="92.5" x2="424" y2="92.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="58" x2="424" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="300" x2="438" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M450,300 L437,306 L437,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="301" x2="84" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,32 L90,45 L78,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="132.5" y1="300" x2="132.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="122.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="181" y1="300" x2="181" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="171" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="229.5" y1="300" x2="229.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="219.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="278.5" y1="300" x2="278.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="268.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="327" y1="300" x2="327" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="310.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="375.5" y1="300" x2="375.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="359" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="424" y1="300" x2="424" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$14$</div></foreignObject>
  <line x1="77" y1="265.5" x2="84" y2="265.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="231" x2="84" y2="231" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="216.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="77" y1="196.5" x2="84" y2="196.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="161.5" x2="84" y2="161.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="147" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="77" y1="127" x2="84" y2="127" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="92.5" x2="84" y2="92.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="78" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="77" y1="58" x2="84" y2="58" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="456" y="285.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="74" y="1.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_\text{s}\ (\text{V})$</div></foreignObject>
  <circle cx="229.5" cy="291.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="246" cy="272.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="266" cy="249" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="292" cy="218" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="326.5" cy="177.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <polyline points="222.5,300 424,63" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="336.5,300 424,197" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="222.5" cy="300" r="5" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="181.5" y="267.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$f_0$</div></foreignObject>
  <circle cx="336.5" cy="300" r="5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="295.5" y="267.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$f_0$</div></foreignObject>
  <line x1="302.5" y1="206" x2="399.5" y2="206" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="399.5" y1="206" x2="399.5" y2="91.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="334.5" y="209.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta f$</div></foreignObject>
  <foreignObject x="407.5" y="134" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta U_\text{s}$</div></foreignObject>
  <foreignObject x="113" y="61" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{model values}$</span></div></foreignObject>
  <foreignObject x="278" y="57.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{sodium}$</span></div></foreignObject>
  <foreignObject x="363.5" y="247.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{zinc}$</span></div></foreignObject>
  <foreignObject x="113" y="105.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{slope} = h/e$</span></div></foreignObject>
</svg>

This gives a way to measure Planck's constant: measure $U_\text{s}$ for two or more frequencies, find the slope of the line, and multiply it by $e$:
```latex
h = e \cdot \frac{\Delta U_\text{s}}{\Delta f}
```
You will do this measurement yourself with a real photocell and LEDs of different colours in the unit *Fotoni lab visit: modern physics experiments*.

## The people behind the equation {People}

### Max Planck (1858–1947)

<figure class="unit-photo"><img src="units/fy14/pics/planck.jpg" alt="Black-and-white portrait photograph of Max Planck, an elderly man with a bald head and round glasses." width="1288" height="1600" loading="lazy"><figcaption>Max Planck (1858–1947) introduced the idea of energy quanta in 1900 to explain blackbody radiation. Photographed in Berlin in 1933. <span class="photo-credit">Photo: Unknown author, public domain, via Wikimedia Commons</span></figcaption></figure>

Max Planck was a German theoretical physicist. In 1900 he found a new law for the radiation of hot objects, and on 14 December 1900 he presented its derivation to the German Physical Society. To derive it, he had to assume that energy is exchanged in packets of size $hf$. Planck saw this as a mathematical step, not as a statement about light itself, and at first he rejected Einstein's light quanta. Still, his constant $h$ became the starting point of quantum physics. He received the Nobel Prize in Physics for 1918 for his discovery of energy quanta.

### Albert Einstein (1879–1955)

<figure class="unit-photo"><img src="units/fy14/pics/einstein.jpg" alt="Black-and-white photograph of Albert Einstein in a suit, standing at a desk in front of a blackboard." width="1218" height="1600" loading="lazy"><figcaption>Albert Einstein (1879–1955) explained the photoelectric effect with light quanta in 1905. Photograph by Ferdinand Schmutzer, Vienna, 1921. <span class="photo-credit">Photo: Ferdinand Schmutzer, public domain, via Wikimedia Commons</span></figcaption></figure>

Albert Einstein was born in Ulm, Germany. In 1905 he worked as an examiner at the Swiss patent office in Bern and did physics in his free time. In March 1905 he sent a paper to the journal *Annalen der Physik*. It proposed that light itself consists of energy quanta and predicted the law ${E_{\text{k,max}} = hf - W}$. In the same year he also published special relativity. His Nobel Prize in Physics for 1921, presented in 1922, was "for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect".

### Robert Millikan (1868–1953)

<!-- photo: robert-millikan -->

Robert Millikan was an American experimental physicist, also famous for measuring the charge of the electron with oil drops. He did not believe in light quanta, because there was so much evidence that light is a wave. So he spent about ten years testing Einstein's equation with careful measurements on several metals. His results, published in 1914–1916, confirmed the straight-line law, and in 1916 he determined Planck's constant from the slope. Millikan still doubted the explanation, but the evidence was clear. He received the Nobel Prize in Physics for 1923.

## Worked example

A violet laser pointer gives light of wavelength $405\ \text{nm}$. The beam falls on a potassium plate in a vacuum tube. The work function of potassium is $2.29\ \text{eV}$. Calculate the energy of one photon in joules and in electronvolts, and the largest kinetic energy of the photoelectrons. What stopping voltage stops all of them?

<!-- vaihe -->

**Given:** Wavelength ${\lambda = 405\ \text{nm}}$, work function ${W = 2.29\ \text{eV}}$, Planck's constant ${h = 6.626 \cdot 10^{-34}\ \text{J} \cdot \text{s}}$, speed of light ${c = 2.998 \cdot 10^{8}\ \text{m/s}}$, elementary charge ${e = 1.602 \cdot 10^{-19}\ \text{C}}$. We want to find the photon energy $E$, the largest kinetic energy $E_{\text{k,max}}$ and the stopping voltage $U_\text{s}$.

<!-- vaihe -->

**Principle:** One photon gives all its energy ${E = hf}$ to one electron, and ${f = c/\lambda}$. The electron uses the work function $W$ to leave the metal, and the rest is its kinetic energy (conservation of energy). The fastest electrons are stopped when the retarding voltage takes their whole kinetic energy, ${eU_\text{s} = E_{\text{k,max}}}$.

<!-- vaihe -->

**Formula:** Solved in symbols:
```latex
\begin{aligned}
E &= hf = \frac{hc}{\lambda} \\
E_{\text{k,max}} &= \frac{hc}{\lambda} - W \\
U_\text{s} &= \frac{E_{\text{k,max}}}{e}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** The wavelength in metres: $\lambda = 405\ \text{nm} = 405 \cdot 10^{-9}\ \text{m} = 4.05 \cdot 10^{-7}\ \text{m}$. From joules to electronvolts we divide by $1.602 \cdot 10^{-19}\ \text{J/eV}$, because ${1\ \text{eV} = 1.602 \cdot 10^{-19}\ \text{J}}$.

<!-- vaihe -->

**Substitution:** First the photon energy, then the difference:
```latex
\begin{aligned}
hc &= 6.626 \cdot 10^{-34}\ \text{J} \cdot \text{s} \\
&\quad \cdot 2.998 \cdot 10^{8}\ \text{m/s} \\
&= 1.9865 \cdot 10^{-25}\ \text{J} \cdot \text{m} \\[6pt]
E &= \frac{hc}{\lambda} \\
&= \frac{1.9865 \cdot 10^{-25}\ \text{J} \cdot \text{m}}{4.05 \cdot 10^{-7}\ \text{m}} \\
&= 4.9049 \cdot 10^{-19}\ \text{J} \\
&= \frac{4.9049 \cdot 10^{-19}\ \text{J}}{1.602 \cdot 10^{-19}\ \text{J/eV}} \\
&= 3.062\ \text{eV} \\[6pt]
E_{\text{k,max}} &= 3.062\ \text{eV} - 2.29\ \text{eV} \\
&= 0.772\ \text{eV} \\[6pt]
U_\text{s} &= \frac{0.772\ \text{eV}}{e} = 0.772\ \text{V}
\end{aligned}
```

<!-- vaihe -->

**Answer:** One photon has the energy ${E \approx 4.90 \cdot 10^{-19}\ \text{J}}$, which is ${E \approx 3.06\ \text{eV}}$. Both have three significant figures, as the wavelength has. The largest kinetic energy of the electrons is $E_{\text{k,max}} \approx 0.77\ \text{eV}$, and the stopping voltage is $U_\text{s} \approx 0.77\ \text{V}$. These are given to two decimal places of an electronvolt, because the work function $2.29\ \text{eV}$ is known to two decimal places.

<!-- vaihe -->

**Reasonableness:** A photon of violet light should have about $3\ \text{eV}$, near the top of the visible range $1.6\text{–}3.3\ \text{eV}$, and $3.06\ \text{eV}$ fits. The photon energy is larger than the work function, so electrons really do leave: the threshold wavelength of potassium is $hc/W \approx 541\ \text{nm}$, longer than $405\ \text{nm}$. Check: $W + E_{\text{k,max}} = 2.29\ \text{eV} + 0.77\ \text{eV} = 3.06\ \text{eV} = hf$.

## Common misconception

"Brighter light gives faster electrons." This is the wave-model idea, and the experiments reject it. Intensity changes the *number* of photons each second, so it changes the current. The energy of one photon, and so the largest kinetic energy of one electron, depends only on the frequency.

A second mistake is to mix the units of energy. The work function is usually given in electronvolts and a photon energy from $hc/\lambda$ comes out in joules. Convert one of them before you subtract. A third mistake is to think that every electron has the energy $E_{\text{k,max}}$: it is the largest value, which only the most loosely bound electrons at the surface reach.

## Summary

- Light is absorbed and emitted in photons, each with the energy ${E = hf = hc/\lambda}$.
- One photon frees at most one electron. The electron leaves only if $hf > W$, so below the threshold frequency ${f_0 = W/h}$ no electrons leave, however bright the light.
- Einstein's photoelectric equation: ${E_{\text{k,max}} = hf - W}$. The stopping voltage gives this energy: ${eU_\text{s} = E_{\text{k,max}}}$.
- Brighter light means more photons every second: a larger current, but the same $E_{\text{k,max}}$.
- The graph of $U_\text{s}$ against $f$ is a straight line with the slope $h/e$, the same for every metal; Millikan used it in 1916 to measure Planck's constant.
- The photoelectric effect showed that classical wave physics could not explain how light and matter exchange energy.
