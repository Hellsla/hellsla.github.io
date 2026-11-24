# Fotoni lab visit: modern physics experiments

> **Why** can a small glass tube, a lamp and a voltmeter tell us something about the whole universe of quantum physics?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a dim university teaching laboratory. On a long bench stand three experiments. On the left, a small black box with a vacuum tube and a row of coloured LEDs, red, yellow, green, blue and violet, connected to a meter. In the middle, a round glass bulb stands between two large copper coils, and a thin glowing beam inside the bulb bends into a closed circle. On the right, a glowing gas tube shines through a grating, and four coloured lines appear on a small white screen. Two students without faces stand behind the bench, one looking at the coils and one writing on a clipboard." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-fotoni-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Before the visit: the physics of each station {Stations}

Fotoni is the open physics teaching laboratory of the University of Helsinki. Its material bank describes the stations below. Your teacher chooses with Fotoni which ones your group does, and the equipment on the day can differ a little from the instructions: always check with the instructor.

<figure class="unit-photo logo"><img src="units/fy14/pics/fotoni-logo.png" alt="The Fotoni logo: the word FOTONI in large black letters over an orange wave, with the text Fysiikan avoin opetuslaboratorio below." width="1200" height="468" loading="lazy"><figcaption>At Fotoni, upper-secondary groups do modern-physics experiments themselves. <span class="photo-credit">Logo: Fotoni, University of Helsinki</span></figcaption></figure>

### Photoelectric effect: Planck's constant

LEDs of different colours shine on the metal plate of a vacuum tube (a **photocell**). A **counter-voltage** pushes the freed electrons back. You raise it until the current is zero: this is the **stopping voltage** $U_\text{s}$. From the unit *Light as particles: the photoelectric effect* you know that ${eU_\text{s} = hf - W}$. You measure $U_\text{s}$ for every LED and find Planck's constant $h$ from the slope of a graph.

### The charge-to-mass ratio of the electron

A heated cathode emits electrons, and an **accelerating voltage** $U$ of about $100\text{–}300\ \text{V}$ speeds them up. The tube contains a little helium, so the beam glows. Two coils make a nearly uniform magnetic field $\overline{B}$, and the beam bends into a circle of radius $r$, as in the unit *Charged particles and magnetic confinement*.

<svg data-fig="em" viewBox="0 0 600 543" role="img" aria-label="Sketch, not to scale: the glass bulb of the e/m tube seen along the axis of the two coils. The magnetic field points out of the page, shown by green circles with a dot and labelled B. An electron leaves the electron gun at the bottom moving to the right and travels on a circle of radius r. At one point of the circle a blue arrow shows its velocity v along the circle and a red arrow shows the magnetic force F, which points to the centre of the circle." style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-fotoni-em.webp" x="0" y="0" width="600" height="546.2" preserveAspectRatio="none"/>
  <foreignObject x="355.5" y="74" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="243" y="432" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gun}$</div></foreignObject>
  <foreignObject x="220" y="228" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="454" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="372" y="280" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
</svg>

The magnetic force is the centripetal force, and the voltage gives the kinetic energy:

```latex
\begin{aligned}
evB &= \frac{mv^2}{r} \\
eU &= \tfrac{1}{2}mv^2
\end{aligned}
```

Together these give ${2U = (e/m) \cdot B^2r^2}$. The field of the coil pair is ${B = (4/5)^{3/2}\,\mu_0 N I / R}$, where $N$ is the number of turns of one coil, $R$ its radius and $I$ the current.

### Double slit, also with single photons

Light passes two narrow slits, and a detector moves across the pattern. Bright light is measured with a **photodiode**. Then a very dim green lamp is used, so that there is practically never more than one photon in the apparatus. A **photomultiplier** turns each photon into a pulse, and a **counter** counts the pulses in $10\ \text{s}$. This links to the unit *Waves, probability and quantum tunnelling*.

```pysahdy
Why is the lamp made so dim that there is practically never more than one photon in the apparatus?
---
Then any pattern cannot come from photons interfering with each other. If bands still appear, each single photon must be responsible for the wave pattern: its probability of arriving follows the wave.
```

### Hot filament and spectra

The light of a lamp filament is spread out by a prism, and a sensor measures the intensity at each wavelength at four voltages ($7$, $8$, $9$ and $10\ \text{V}$). The software calculates the filament's temperature. Compare with Wien's law ${\lambda_\text{max} T = b}$ (unit *When classical physics ran out of answers*). At the spectra station you look at lamps and gas tubes with a hand spectroscope and a spectrometer (unit *From Rutherford's nucleus to Bohr's atom*).

### Millikan's oil drops (qualitative)

Tiny oil drops float between two plates with a voltage of about $500\ \text{V}$. An alpha source charges them. You watch the drops through a microscope camera and look for sudden changes in their motion.

## Planning a measurement {Planning}

Every station has a **research question**: what do you want to find out? Then name the variables:

- the **independent variable** is the one you change (the LED, the coil current);
- the **dependent variable** is the one you measure (the stopping voltage, the radius);
- the **controlled variables** are kept the same (the accelerating voltage, the intensity).

No measurement is exact. The **uncertainty** $\Delta x$ of a quantity $x$ tells how far the true value may be from your reading. For a scale or a digital display, the reading uncertainty is about half of the smallest step you can read, unless the reading jumps around more. If you repeat a measurement, use the mean. Half of the range, (largest minus smallest) divided by two, is a simple estimate of how much single readings spread; use it as $\Delta x$ of one reading. It is not the uncertainty of the mean, which is smaller. Write the result as ${x \pm \Delta x}$ with its unit. The **relative uncertainty** $\Delta x / x$ is often given in percent.

```pysahdy
A digital voltmeter shows $0.93\,\text{V}$ and its smallest step is $0.01\,\text{V}$. What is the reading uncertainty?
---
About half of the smallest step, $0.005\,\text{V}$, so the result is written ${(0.930 \pm 0.005)\,\text{V}}$ unless the reading jumps around more.
```

### Safety at the stations

- Several stations use high voltages: the electron tube up to $300\ \text{V}$, the oil-drop plates about $500\ \text{V}$, and the gas tubes. Change the connections only when the instructor allows it.
- The electron tube is thin glass: a magnet may come near it, but never touch it.
- Lamps and gas tubes get hot. Do not touch them, and do not look straight into a bright lamp or LED from close by.
- The alpha source of the oil-drop station stays inside the apparatus. Only the instructor handles it.
- Do not run the filament lamp at $10\ \text{V}$ for long: it shortens the lamp's life.

## During the visit: lab worksheet {Worksheet}

Print this section, or copy the tables into your notebook. Fill in the empty cells at the station. Write every number with its unit and its uncertainty.

### Group

| Names | Date | Stations we did |
| --- | --- | --- |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

### Station: photoelectric effect

Research question: how does the stopping voltage depend on the frequency of the light, and what is Planck's constant?

| Instrument at the station | What it measures | Smallest step | $\Delta x$ |
| --- | --- | --- | --- |
| &emsp;&emsp; | voltage $U$ | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | current $I$ | &emsp;&emsp; | &emsp;&emsp; |

Observations with the red LED, before you take the measurements:

| What we did | What happened to the current |
| --- | --- |
| $U$ slightly negative, more light | &emsp;&emsp;&emsp;&emsp; |
| $U$ at the stopping voltage, more light | &emsp;&emsp;&emsp;&emsp; |

| LED colour | $\lambda\ (\text{nm})$ | $f\ (10^{14}\ \text{Hz})$ | $U_\text{s}\ (\text{V})$ |
| --- | --- | --- | --- |
| red | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |

Where does the LED's wavelength come from (a label, the instructor, a spectrometer)? Write it down.

### Station: charge-to-mass ratio of the electron

Research question: what is the ratio $e/m$ of the electron?

| Coil data | Value | Where it comes from |
| --- | --- | --- |
| turns of one coil $N$ | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| coil radius $R\ (\text{m})$ | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

Observations before the measurements:

| What we did | What happened to the beam |
| --- | --- |
| a bar magnet near the tube (not touching) | &emsp;&emsp;&emsp;&emsp; |
| $U$ kept the same, coil current up | &emsp;&emsp;&emsp;&emsp; |
| coil current kept the same, $U$ up | &emsp;&emsp;&emsp;&emsp; |

Measurements:

| $I\ (\text{A})$ | $U\ (\text{V})$ | $r\ (\text{m})$ |
| --- | --- | --- |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

Calculated from each row of the table above:

| $B\ (\text{T})$ | $B^2r^2\ (\text{T}^2\text{m}^2)$ | $2U\ (\text{V})$ |
| --- | --- | --- |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

How did you measure the radius, and what is $\Delta r$?

### Station: double slit and single photons

Research question: does a pattern of bright and dark bands appear when photons arrive one at a time?

| Data of the setup | Value | Where it comes from |
| --- | --- | --- |
| slit separation $d\ (\text{mm})$ | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| slit to detector $L\ (\text{cm})$ | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| wavelength $\lambda\ (\text{nm})$ | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

Repeated counts at one position (each in $10\ \text{s}$):

| Count 1 | Count 2 | Count 3 | Count 4 | Count 5 |
| --- | --- | --- | --- | --- |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |

Counts at different positions:

| Position $x\ (\text{mm})$ | Counts in $10\ \text{s}$ | Position $x\ (\text{mm})$ | Counts in $10\ \text{s}$ |
| --- | --- | --- | --- |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |

### Station: hot filament

Research question: how does the spectrum of a hot filament change with its temperature?

| Voltage $U\ (\text{V})$ | Temperature $T\ (\text{K})$ | Peak $\lambda_\text{max}\ (\text{nm})$ | Colour we saw |
| --- | --- | --- | --- |
| $7$ | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| $8$ | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| $9$ | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |
| $10$ | &emsp;&emsp; | &emsp;&emsp; | &emsp;&emsp; |

### Station: spectra

Research question: which light sources give a continuous spectrum, and which give lines?

| Light source | Continuous or lines? | Brightest colours or lines |
| --- | --- | --- |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

### Station: oil drops

Research question: how do charged oil drops move between the plates, and what happens when a drop's charge changes?

| What we saw | Our explanation |
| --- | --- |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

### After each station

One sentence: what surprised us, and what limited the precision?

| Station | Our sentence |
| --- | --- |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |
| &emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp; |

## After the visit: what the stations show {Evidence}

Compare these results with your own worksheet.

**Photoelectric effect.** When the counter-voltage is slightly negative, more intensity gives more current, because more photons free more electrons. At the stopping voltage the current stays at zero however bright the LED is. One photon frees at most one electron, and the photon's energy $hf$ depends only on the colour. Shorter wavelengths give larger stopping voltages, and the points $(f, U_\text{s})$ lie close to a straight line with the slope $h/e$.

**Electron beam.** A larger coil current makes a stronger field and a *smaller* circle, because ${r = mv/(eB)}$. A larger accelerating voltage makes the electrons faster and the circle larger. The points $(B^2r^2, 2U)$ lie on a line through the origin, and its slope is $e/m$, about ${1.76 \cdot 10^{11}\ \text{C/kg}}$.

**Single photons.** The counter clicks at random moments, and repeated counts at one place differ a little. But the counts at different positions form the same bright and dark bands as bright light does. Each photon arrives at one point like a particle, but the probability of where it arrives follows a wave pattern.

**Hot filament.** When the temperature rises, the peak moves to shorter wavelengths and the light looks whiter. The peak still stays in the infrared, so most of the energy of an ordinary filament lamp is not visible light. The curves fall at short wavelengths, as Planck's law says, not as classical physics predicted.

**Spectra and oil drops.** A filament gives a continuous spectrum. A gas tube gives lines at fixed wavelengths, for hydrogen $656$, $486$, $434$ and $410\ \text{nm}$. An oil drop that suddenly changes its speed has gained or lost charge. Millikan's measurements showed that the charge changes in whole steps of $e$.

## Key idea

Each station shows a result that classical physics could not explain. Light gives and takes energy in **quanta** $hf$: the photoelectric effect, line spectra and the shape of the filament's spectrum all need Planck's constant. Electrons are particles with a fixed charge $e$ and a fixed ratio $e/m$. And single photons behave like particles when they are detected and like waves when they travel. This is the **wave–particle duality** of modern physics.

The same physics is a tool in fusion research. A charged particle circles around a magnetic field line and slides along it. Your electron beam shows the circling part, because it moves perpendicular to the field. A tokamak bends the field lines into closed loops inside the vessel, so the hot plasma stays away from the walls. Spectrometers measure the light of the plasma: at ITER, spectroscopic instruments cover the range from visible light to X-rays and measure, for example, which impurities the plasma contains and the temperature of its ions.

## Formula: A straight-line fit

When a law has the form $y = kx + b$, plot the measured points $(x, y)$ and **fit** the straight line that passes closest to all of them. A spreadsheet or a graphing calculator does this (a *trendline* or *linear fit*). For the photocell, ${U_\text{s} = (h/e)\,f - W/e}$, so

```latex
\begin{aligned}
k &= \frac{h}{e}, & h &= e\,k, \\
b &= -\frac{W}{e}, & W &= -e\,b.
\end{aligned}
```

For the electron beam, ${2U = (e/m) \cdot B^2r^2}$ is a line through the origin, and its slope is $e/m$.

The uncertainty of the slope can be estimated with the **steepest and least steep lines** that still pass through the uncertainty ranges of the points, usually the first and the last point. Then

```latex
\Delta k \approx \frac{k_\text{max} - k_\text{min}}{2}
```

Finally, compare your result with the accepted value by the **percentage difference**:

```latex
\text{difference} = \dfrac{x - x_\text{acc}}{x_\text{acc}} \cdot 100\ \%
```

where $x$ is your result and $x_\text{acc}$ the accepted value.

If the accepted value lies inside ${x \pm \Delta x}$, your result **agrees** with it within the uncertainty.

## Worked example

<!-- photo: fotoni-photocell-station -->

A group measured the stopping voltage with five LEDs. The numbers are an invented example, rounded like real readings. The group estimated the uncertainty of every stopping voltage as $\Delta U_\text{s} = 0.02\ \text{V}$. Find Planck's constant with its uncertainty, and compare it with the accepted value ${6.626 \cdot 10^{-34}\ \text{J} \cdot \text{s}}$.

| LED | $\lambda\ (\text{nm})$ | $f\ (10^{14}\ \text{Hz})$ | $U_\text{s}\ (\text{V})$ |
| --- | --- | --- | --- |
| red | 625 | 4.80 | 0.55 |
| yellow | 590 | 5.08 | 0.69 |
| green | 525 | 5.71 | 0.93 |
| blue | 470 | 6.38 | 1.17 |
| violet | 405 | 7.40 | 1.60 |

The graph shows the five points and the line that a spreadsheet fits through them.

<svg data-fig="fit" viewBox="0 0 560 380" role="img" aria-label="Graph of invented example data: the stopping voltage U_s in volts against the frequency f in units of 10^14 Hz, from 4 to 8. Five points rise almost on a straight line, from 0.55 V at 4.80 to 1.60 V at 7.40. A fitted straight line runs through them; the label gives its slope, 3.96 · 10^-15 V · s. The line is labelled fit." style="max-width:100%;font-size:28px">
  <line x1="155" y1="318" x2="155" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220" y1="318" x2="220" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="318" x2="285" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="318" x2="350" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="265" x2="350" y2="265" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="211.5" x2="350" y2="211.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="158.5" x2="350" y2="158.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="105" x2="350" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="52" x2="350" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="318" x2="364" y2="318" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M376,318 L363,324 L363,312 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="319" x2="90" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,26 L96,39 L84,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="155" y1="318" x2="155" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="143.5" y="325" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$5$</div></foreignObject>
  <line x1="220" y1="318" x2="220" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="208.5" y="325" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$6$</div></foreignObject>
  <line x1="285" y1="318" x2="285" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="273.5" y="325" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$7$</div></foreignObject>
  <line x1="350" y1="318" x2="350" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="338.5" y="325" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$8$</div></foreignObject>
  <line x1="83" y1="265" x2="90" y2="265" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="248" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$0.5$</div></foreignObject>
  <line x1="83" y1="211.5" x2="90" y2="211.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="194.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$1$</div></foreignObject>
  <line x1="83" y1="158.5" x2="90" y2="158.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="141.5" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$1.5$</div></foreignObject>
  <line x1="83" y1="105" x2="90" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="88" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$2$</div></foreignObject>
  <line x1="83" y1="52" x2="90" y2="52" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="35" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$2.5$</div></foreignObject>
  <foreignObject x="382" y="301" width="158" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="104" y="15" width="85" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$U_\text{s}\ (\text{V})$</span></div></foreignObject>
  <polyline points="103,283.5 343.5,127.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="142" cy="259.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="160" cy="244.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="201" cy="219" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="244.5" cy="193.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="311" cy="148" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="175.5" y="274.5" width="168" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{example data}$</span></div></foreignObject>
  <foreignObject x="96.5" y="82" width="357" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{fit: slope} = 3.96 \cdot 10^{-15}\,\text{V} \cdot \text{s}$</span></div></foreignObject>
</svg>

<!-- vaihe -->

**Given:** five pairs $(f, U_\text{s})$ from the table, ${\Delta U_\text{s} = 0.02\ \text{V}}$, the elementary charge ${e = 1.602 \cdot 10^{-19}\ \text{C}}$. We want Planck's constant $h$, its uncertainty $\Delta h$ and the percentage difference from ${6.626 \cdot 10^{-34}\ \text{J} \cdot \text{s}}$.

<!-- vaihe -->

**Principle:** Einstein's equation ${eU_\text{s} = hf - W}$ is a straight line ${U_\text{s} = (h/e)\,f - W/e}$. A fit through all five points gives the slope $k = h/e$ and uses every measurement. The steepest and least steep lines through the first and the last point, each moved by $\Delta U_\text{s}$, give the uncertainty of the slope.

<!-- vaihe -->

**Formula:** Solved in symbols, with the first point $(f_1, U_1)$ and the last point $(f_5, U_5)$:

```latex
\begin{aligned}
h &= e\,k \\
k_\text{max} &= \frac{(U_5 + \Delta U_\text{s}) - (U_1 - \Delta U_\text{s})}{f_5 - f_1} \\
k_\text{min} &= \frac{(U_5 - \Delta U_\text{s}) - (U_1 + \Delta U_\text{s})}{f_5 - f_1} \\
\Delta h &= e \cdot \frac{k_\text{max} - k_\text{min}}{2}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** The frequencies are in units of $10^{14}\ \text{Hz}$, so the difference of the last and the first frequency is ${f_5 - f_1 = (7.40 - 4.80) \cdot 10^{14}\ \text{Hz}}$, that is, ${2.60 \cdot 10^{14}\ \text{Hz}}$. A slope in ${\text{V/Hz} = \text{V} \cdot \text{s}}$ times a charge in coulombs gives ${\text{C} \cdot \text{V} \cdot \text{s} = \text{J} \cdot \text{s}}$.

<!-- vaihe -->

**Substitution:** A spreadsheet fit of the five points gives the slope ${k = 3.964 \cdot 10^{-15}\ \text{V} \cdot \text{s}}$ and the intercept ${b = -1.34\ \text{V}}$. Then:

```latex
\begin{aligned}
h &= 1.602 \cdot 10^{-19}\ \text{C} \\
&\quad \cdot 3.964 \cdot 10^{-15}\ \text{V} \cdot \text{s} \\
&= 6.351 \cdot 10^{-34}\ \text{J} \cdot \text{s} \\[6pt]
k_\text{max} &= \frac{1.62\ \text{V} - 0.53\ \text{V}}{2.60 \cdot 10^{14}\ \text{Hz}} \\
&= 4.192 \cdot 10^{-15}\ \text{V} \cdot \text{s} \\[6pt]
k_\text{min} &= \frac{1.58\ \text{V} - 0.57\ \text{V}}{2.60 \cdot 10^{14}\ \text{Hz}} \\
&= 3.885 \cdot 10^{-15}\ \text{V} \cdot \text{s} \\[6pt]
\Delta h &= 1.602 \cdot 10^{-19}\ \text{C} \\
&\quad \cdot \frac{0.307 \cdot 10^{-15}\ \text{V} \cdot \text{s}}{2} \\
&= 0.246 \cdot 10^{-34}\ \text{J} \cdot \text{s} \\[6pt]
\text{difference} &= \frac{6.351 - 6.626}{6.626} \\
&\quad \cdot 100\ \% \\
&= -4.2\ \%
\end{aligned}
```

<!-- vaihe -->

**Answer:** ${h = (6.4 \pm 0.3) \cdot 10^{-34}\ \text{J} \cdot \text{s}}$. The uncertainty is rounded up to one significant figure, and the value is given to the same decimal place. The result is about $4\ \%$ smaller than the accepted value.

<!-- vaihe -->

**Reasonableness:** The accepted value ${6.626 \cdot 10^{-34}\ \text{J} \cdot \text{s}}$ lies inside ${(6.1\ \text{to}\ 6.7) \cdot 10^{-34}\ \text{J} \cdot \text{s}}$, so the result agrees with it within the uncertainty. The intercept gives ${W = -e\,b \approx 1.34\ \text{eV}}$, positive and of the order of one electronvolt, as a work function should be. Possible systematic errors: an LED gives a band of wavelengths, not one exact wavelength, and it is hard to decide when the current is exactly zero.

## Writing a lab report in English {Report}

A lab report tells a reader what you did, what you found and how sure you are. Scientists write it in a fixed order:

1. **Title** and **aim**: the research question in one sentence.
2. **Background**: the physics and the equation you test, in the present tense ("The stopping voltage *depends* on …").
3. **Method**: the equipment and what you did, in the past tense ("We *measured* …", or the passive "The voltage *was increased* …").
4. **Results**: tables with units in the headings, a graph with labelled axes and the fitted line.
5. **Analysis**: the fit, the result with its uncertainty, ${x \pm \Delta x}$.
6. **Discussion**: the comparison with the accepted value, the sources of uncertainty and how to improve the experiment.
7. **Conclusion**: the answer to the research question in one or two sentences.

Write numbers with a decimal point and their unit ($0.93\ \text{V}$). Do not claim more than the data shows: "the result agrees with the accepted value within its uncertainty" is stronger science than "the result proves the theory".

## Common misconception

"An uncertainty means that we made a mistake." No: every measurement has an uncertainty, even a perfect one. A **mistake** (a wrong connection, a misread scale) is something you can find and correct. The uncertainty estimates how far the true value may be from the result. Part of it shows as scatter when you repeat the measurement. **Systematic errors**, such as the band of wavelengths of an LED, do not show as scatter, and repeating does not reduce them.

A second misconception is that more decimals mean a better result. A calculator may show ${6.351596 \cdot 10^{-34}}$, but with ${\Delta h = 0.3 \cdot 10^{-34}\ \text{J} \cdot \text{s}}$ only the first decimal means something. A third is that a result that differs from the accepted value is wrong. It is fine if the accepted value lies inside ${x \pm \Delta x}$.

## Summary

- At Fotoni you measure modern physics yourself: Planck's constant from stopping voltages, $e/m$ from a circular electron beam, single photons in a double slit, the spectrum of a hot filament, line spectra and charged oil drops.
- Plan every measurement: research question, independent, dependent and controlled variables, and the uncertainty $\Delta x$ of each reading.
- The slope of a fitted line gives the constant: ${h = e\,k}$ from ${U_\text{s} = (h/e)\,f - W/e}$, and $e/m$ from ${2U = (e/m) \cdot B^2r^2}$.
- The steepest and least steep lines give ${\Delta k \approx (k_\text{max} - k_\text{min})/2}$. Report ${x \pm \Delta x}$ and the percentage difference from the accepted value.
- A lab report has a fixed structure: aim, background, method, results, analysis, discussion and conclusion.
