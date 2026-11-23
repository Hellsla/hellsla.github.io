# Mass defect and nuclear binding energy

> **Why** is a helium-4 atom lighter than two hydrogen atoms and two neutrons put together, even though it consists of exactly those particles?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a laboratory table is an old-fashioned balance. In the left pan, which is lower, two red protons and two grey neutrons lie apart. In the right pan, which is higher, the same four particles are packed tightly together as a helium nucleus, which glows and sends out two orange photons. The separate particles weigh more than the nucleus assembled from them." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Atomic mass unit
The masses of atoms and nuclei are given in **atomic mass units**. The atomic mass unit $\text{u}$ is defined so that the mass of a carbon-12 atom is exactly $12\,\text{u}$, which gives $1\,\text{u} = 1.66054 \cdot 10^{-27}\,\text{kg}$. The masses of the proton and the neutron are each about $1\,\text{u}$, so the mass of an atom in atomic mass units is close to its mass number $A$ but not exactly equal to it. The values in the table are masses of **atoms**: they include the electrons too. The mass of a hydrogen atom ${}^{1}\text{H}$ is the mass of a proton plus the mass of an electron.

| Particle | Symbol | Mass ($\text{u}$) |
| --- | --- | --- |
| hydrogen-1 | ${}^{1}\text{H}$ | $1.007825$ |
| neutron | $\text{n}$ | $1.008665$ |
| hydrogen-2 | ${}^{2}\text{H}$ | $2.014102$ |
| helium-4 | ${}^{4}\text{He}$ | $4.002603$ |
| carbon-12 | ${}^{12}\text{C}$ | $12.000000$ |
| oxygen-16 | ${}^{16}\text{O}$ | $15.994915$ |
| iron-56 | ${}^{56}\text{Fe}$ | $55.934936$ |
| uranium-238 | ${}^{238}\text{U}$ | $238.050787$ |

Source: the atomic mass table AME2020 (Atomic Mass Evaluation 2020, IAEA Atomic Mass Data Center), rounded to six decimals. This many decimals are needed for nuclear masses because the important differences are small.

### Mass defect
A helium-4 atom contains two protons, two neutrons and two electrons. The same particles are in two hydrogen atoms and two neutrons, whose total mass is $$
\begin{aligned}
&2 \cdot 1.007825\,\text{u} + 2 \cdot 1.008665\,\text{u} \\
&= 4.032980\,\text{u}
\end{aligned}
$$. The mass of the helium-4 atom, however, is only $4.002603\,\text{u}$. When the nucleons are bound into a nucleus, their mass is smaller than when they are apart. The difference $$
\begin{aligned}
&4.032980\,\text{u} - 4.002603\,\text{u} \\
&= 0.030377\,\text{u}
\end{aligned}
$$ is the **mass defect** $\Delta m$ of the nucleus, about $0.76\,\%$ of the mass of the atom. Hydrogen atoms are used instead of separate protons so that the masses of the electrons cancel: there are two electrons on both sides.

<svg data-fig="massat" viewBox="0 0 600 350" role="img" aria-label="Bar chart, the vertical axis to scale but broken: it starts at the value 3.990 u, not at zero. The left bar is the total mass of two hydrogen atoms and two neutrons, 4.032980 u. The right bar is the mass of a helium-4 atom, 4.002603 u. The difference between the bars, the mass defect, is 0.030377 u, and it is marked with a red bracket." style="max-width:100%;font-size:24px">
  <line x1="130" y1="243" x2="560" y2="243" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="243" x2="130" y2="243" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="228.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4.000$</div></foreignObject>
  <line x1="130" y1="196.5" x2="560" y2="196.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="196.5" x2="130" y2="196.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="182" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4.010$</div></foreignObject>
  <line x1="130" y1="149.5" x2="560" y2="149.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="149.5" x2="130" y2="149.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="135" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4.020$</div></foreignObject>
  <line x1="130" y1="103" x2="560" y2="103" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="103" x2="130" y2="103" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="88.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4.030$</div></foreignObject>
  <line x1="130" y1="56" x2="560" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="56" x2="130" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="41.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4.040$</div></foreignObject>
  <line x1="130" y1="290" x2="560" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="130" y1="291" x2="130" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M130,28 L136,41 L124,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="142" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m\ (\text{u})$</div></foreignObject>
  <rect x="121" y="264" width="18" height="12" fill="#ffffff"/>
  <line x1="121" y1="268" x2="139" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="121" y1="278" x2="139" y2="272" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="160" y="89" width="80" height="201" fill="#c9c2b2" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="133.5" y="54.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$4.032980\,\text{u}$</span></div></foreignObject>
  <foreignObject x="152.5" y="305.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2m_\text{H} + 2m_\text{n}$</div></foreignObject>
  <rect x="280" y="231" width="80" height="59" fill="#b2f2bb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="253.5" y="196.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$4.002603\,\text{u}$</span></div></foreignObject>
  <foreignObject x="278.5" y="305.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m({}^{4}\text{He})$</div></foreignObject>
  <line x1="240" y1="89" x2="428" y2="89" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="360" y1="231" x2="428" y2="231" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="420" y1="89" x2="420" y2="231" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="89" x2="428" y2="89" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="231" x2="428" y2="231" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="437" y="128.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta m$</span></div></foreignObject>
  <foreignObject x="437" y="162.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0.030377\,\text{u}$</span></div></foreignObject>
</svg>

### Mass and energy
The mass defect is not matter that has vanished. According to Einstein's theory of relativity, mass and energy are **equivalent**: a change $\Delta E$ in the energy of an object changes its mass by $\tfrac{\Delta E}{c^2}$, where $c$ is the speed of light. When protons and neutrons bind into a nucleus, the strong interaction pulls them together and energy is released, for example as gamma photons. The energy, and therefore also the mass, of the resulting nucleus is smaller than that of the separate nucleons. The same energy is needed if the nucleus is broken back into separate nucleons. This energy is the **binding energy** $E_\text{B}$ of the nucleus.

<svg data-fig="energia" viewBox="0 0 600 345" role="img" aria-label="Diagram, not to scale: energy levels. The upper horizontal line is the energy of separate protons and neutrons: on it are two red protons and two grey neutrons apart. The lower horizontal line is the energy of the helium-4 nucleus: on it the same four nucleons tightly together. On the left an orange arrow pointing up: breaking the nucleus into nucleons requires the binding energy E B. On the right an orange arrow pointing down: when the nucleus forms, the same energy is released. Between the levels is written E B = Δm c²." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-10-energia.webp" x="0" y="0" width="600" height="355" preserveAspectRatio="none"/>
  <foreignObject x="149" y="25.5" width="332" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{separate protons and neutrons}$</div></foreignObject>
  <foreignObject x="240.5" y="301.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{nucleus}\ {}^{4}_{2}\text{He}$</div></foreignObject>
  <foreignObject x="261" y="135.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$E_\text{B} = \Delta m\,c^2$</div></foreignObject>
  <foreignObject x="118" y="185.5" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{needed}\ E_\text{B}$</div></foreignObject>
  <foreignObject x="378" y="185.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{released}\ E_\text{B}$</div></foreignObject>
</svg>

```pysahdy
The binding energy of a carbon-12 nucleus is $92.2\,\text{MeV}$. By how many atomic mass units is the nucleus lighter than its $12$ nucleons separated? Use $1\,\text{u} = 931.5\,\tfrac{\text{MeV}}{c^2}$.
---
The binding energy corresponds to the mass difference: $\Delta m = \tfrac{E_\text{B}}{c^2} = \tfrac{92.2\,\text{MeV}}{931.5\,\text{MeV}/\text{u}} \approx 0.0990\,\text{u}$. The nucleus is about $0.099\,\text{u}$ lighter.
```

### Why a change of mass is not noticed in everyday life
The equivalence of mass and energy applies to every change of energy, but $c^2$ is so large that in ordinary phenomena the change of mass is too small to measure. A mass of one gram corresponds to the energy
```latex
\begin{aligned}
&E = 1.00 \cdot 10^{-3}\,\text{kg} \\
&\quad \cdot (2.998 \cdot 10^{8}\,\text{m/s})^2 \\
&\approx 9.0 \cdot 10^{13}\,\text{J}.
\end{aligned}
```
When carbon burns, the mass decreases by only about one ten-billionth. In nuclei the binding energy is so large that the mass defect is about $0.8\,\%$ of the mass of the atom for helium-4 and uranium-238 alike. This is why nuclear physics calculates energy directly from the difference of masses.

## Formula: Binding energy

### Mass defect and binding energy
A nucleus ${}^{A}_{Z}\text{X}$ has $Z$ protons and $N = A - Z$ neutrons. The mass defect is calculated from atomic masses:
```latex
\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atom}
```
where $m_\text{H}$ is the mass of a hydrogen atom ${}^{1}\text{H}$, $m_\text{n}$ the mass of a neutron and $m_\text{atom}$ the mass of the atom ${}^{A}_{Z}\text{X}$. The binding energy of a nucleus is the energy corresponding to the mass defect
```kaavat
binding energy of a nucleus :: E_\text{B} = \Delta m\,c^2
```
where $E_\text{B}$ is the binding energy and $c = 2.998 \cdot 10^{8}\,\text{m/s}$ the speed of light. The binding energy of the electrons themselves in the atom is not taken into account, because it is at most hundreds of kiloelectronvolts, and even for the heaviest atoms less than a thousandth of the binding energy of the nucleus.

### The atomic mass unit as energy
The energies of nuclei are given in megaelectronvolts: $1\,\text{MeV} = 10^{6}\,\text{eV}$ and $1\,\text{eV} = 1.602177 \cdot 10^{-19}\,\text{J}$. Let us calculate the energy that corresponds to a mass of $1\,\text{u}$. Because the mass defect is a small difference, six significant figures are used here for the constants:
```latex
\begin{aligned}
&E = 1\,\text{u} \cdot c^2 \\
&= 1.66054 \cdot 10^{-27}\,\text{kg} \\
&\quad \cdot (2.99792 \cdot 10^{8}\,\text{m/s})^2 \\
&= 1.49241 \cdot 10^{-10}\,\text{J} \\
&= \frac{1.49241 \cdot 10^{-10}}{1.602177 \cdot 10^{-19}}\,\text{eV} \\
&= 9.3149 \cdot 10^{8}\,\text{eV} \\
&\approx 931.5\,\text{MeV}
\end{aligned}
```
So $1\,\text{u} = 931.5\,\tfrac{\text{MeV}}{c^2}$. When the mass defect is in atomic mass units, this is put in place of the unit, and $c^2$ cancels: for example $$
\begin{aligned}
&0.001000\,\text{u} \cdot c^2 \\
&= 0.001000 \cdot 931.5\,\tfrac{\text{MeV}}{c^2} \cdot c^2 \\
&= 0.9315\,\text{MeV}
\end{aligned}
$$. With four-figure constants $1.661 \cdot 10^{-27}\,\text{kg}$, $2.998 \cdot 10^{8}\,\text{m/s}$ and $1.602 \cdot 10^{-19}\,\text{J}$ the result would be $931.9\,\text{MeV}$, so four-figure constants already change the fourth figure.

```pysahdy
The mass defect of a nucleus is $0.0020\,\text{u}$. How large is the binding energy of the nucleus in megaelectronvolts?
---
Substitute $1\,\text{u} = 931.5\,\tfrac{\text{MeV}}{c^2}$: $E_\text{B} = 0.0020 \cdot 931.5\,\text{MeV} \approx 1.9\,\text{MeV}$.
```

### Binding energy per nucleon
The strength of the binding of nuclei is compared with the **binding energy per nucleon**
```kaavat
binding energy per nucleon :: \frac{E_\text{B}}{A}
```
where $A$ is the mass number, that is, the number of nucleons. The graph shows it calculated from atomic masses for $32$ nuclei. For light nuclei the value rises steeply, because each nucleon has more and more neighbours to which the strong interaction binds it. Helium-4 is exceptionally tightly bound. The value is highest, about $8.8\,\text{MeV}$, for iron-56 and nickel-62. For heavier nuclei it falls gently, because the strong interaction acts only between nearest neighbours, but the electric repulsion of the protons reaches across the whole nucleus.

<svg data-fig="kayra" viewBox="0 0 600 350" role="img" aria-label="Graph to scale: binding energy per nucleon in megaelectronvolts as a function of the mass number A, A from zero to 250, the vertical axis from zero to 10 megaelectronvolts. The points are values for 32 nuclei calculated from atomic masses. For deuterium the value is 1.11 MeV, for helium-4 7.07 MeV, clearly higher than its neighbours. The value rises steeply for light nuclei, is highest, about 8.8 MeV, at iron-56 and nickel-62, and falls gently towards heavy nuclei: for uranium-238 7.57 MeV. On the left an orange arrow pointing up and to the right: fusion, the joining of light nuclei. On the right an orange arrow pointing left towards the peak: fission, the splitting of a heavy nucleus." style="max-width:100%;font-size:24px">
  <line x1="212" y1="300" x2="212" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="294" y1="300" x2="294" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376" y1="300" x2="376" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="458" y1="300" x2="458" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="300" x2="540" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="252" x2="540" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="204" x2="540" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="156" x2="540" y2="156" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="108" x2="540" y2="108" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="60" x2="540" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="129" y1="300" x2="554" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,300 L553,306 L553,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="130" y1="301" x2="130" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M130,34 L136,47 L124,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="212" y1="300" x2="212" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="195.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="294" y1="300" x2="294" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="271.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="376" y1="300" x2="376" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="353.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="458" y1="300" x2="458" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="435.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="540" y1="300" x2="540" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="517.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$250$</div></foreignObject>
  <line x1="123" y1="252" x2="130" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="237.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="123" y1="204" x2="130" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="189.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="123" y1="156" x2="130" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="141.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="123" y1="108" x2="130" y2="108" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="123" y1="60" x2="130" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="85" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="100" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="572" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="120" y="3.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{B}/A\ (\text{MeV})$</div></foreignObject>
  <path d="M195.5,266 L218.5,199 L226,201.5 L220,176 L199.5,192.5 L207,195 L184.5,262 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="232" y="211.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\text{fusion}$</div></foreignObject>
  <path d="M500,164 L382,164 L382,156 L360,170 L382,184 L382,176 L500,176 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="382.5" y="189.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{fission}$</div></foreignObject>
  <circle cx="133.5" cy="273.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="135" cy="232" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="135" cy="238.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="136.5" cy="130" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="140" cy="172" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="141.5" cy="165.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="145" cy="145" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="148" cy="133.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="149.5" cy="115.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="153" cy="120.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="156" cy="108.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="163" cy="107" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="169.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="176" cy="97.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="182.5" cy="96" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="195.5" cy="95" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="222" cy="89" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="231.5" cy="89" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="233.5" cy="90" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="235" cy="90.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="268" cy="91" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="277.5" cy="91" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="305.5" cy="94.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="327" cy="96" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="356.5" cy="98.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432" cy="108" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="453" cy="110" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="471" cy="111" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="473" cy="111.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="510.5" cy="117" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="515.5" cy="118" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="520.5" cy="118.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="139.5" y1="124" x2="168" y2="74" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="170" y="47.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${}^{4}\text{He}$</div></foreignObject>
  <line x1="227" y1="84" x2="262" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="264" y="47.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${}^{56}\text{Fe}$</div></foreignObject>
  <foreignObject x="487.5" y="134" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{238}\text{U}$</div></foreignObject>
  <foreignObject x="147.5" y="255" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${}^{2}\text{H}$</div></foreignObject>
</svg>

The graph shows when a nuclear reaction releases energy: when the nuclei formed are more tightly bound than the original ones, the binding energy increases and the difference is released. The joining of light nuclei, **fusion**, and the splitting of a heavy nucleus, **fission**, move nucleons towards the peak of the graph. They are discussed in the chapter *Fission, fusion and nuclear power*.

```pysahdy
In a nuclear reaction there are equally many nucleons on both sides. The total binding energy of the starting nuclei is $1800\,\text{MeV}$ and that of the products $1805\,\text{MeV}$. Is energy released or needed, how much, and how does the mass change?
---
Energy is released: the products are bound more tightly, so the difference $1805\,\text{MeV} - 1800\,\text{MeV} = 5\,\text{MeV}$ is released as kinetic energy of the products and the total mass decreases by $\tfrac{5\,\text{MeV}}{c^2}$.
```

### Reaction energy
In a **nuclear reaction** nuclei change: a nucleus decays, or another nucleus or particle hits a nucleus. In a reaction the mass number and the charge number are conserved (chapter *The atomic nucleus and radioactive decay*), but mass is not. The reaction energy is
```kaavat
energy released in a nuclear reaction :: Q = (m_\text{initial} - m_\text{final})\,c^2
```
where $m_\text{initial}$ is the sum of the masses of the starting materials and $m_\text{final}$ the sum of the masses of the particles formed. When $Q > 0$, energy is released as the kinetic energy of the particles formed and as gamma radiation; when $Q < 0$, the reaction needs energy. The formula counts the masses of all the particles on both sides. The atomic masses in tables also include the electrons of the atoms. In alpha decay and most nuclear reactions there are equally many electrons on both sides, so atomic masses can be put into the formula directly. For example, in the alpha decay of uranium-238, ${}^{238}_{92}\text{U} \to {}^{234}_{90}\text{Th} + {}^{4}_{2}\text{He}$, the mass decreases by $0.004583\,\text{u}$, so $$
\begin{aligned}
&Q \\
&= 0.004583 \cdot 931.5\,\text{MeV} \\
&\approx 4.27\,\text{MeV}
\end{aligned}
$$.

<svg data-fig="reaktio" viewBox="0 0 600 350" role="img" aria-label="Bar chart, the vertical axis to scale but broken: it starts at the value 238.040 u, not at zero. The left bar is the mass of a uranium-238 atom, 238.050787 u. The right bar is the combined mass of the thorium-234 and helium-4 atoms formed in alpha decay, 238.046204 u. The difference 0.004583 u is marked with a red bracket, and it corresponds to the reaction energy Q = 4.27 MeV." style="max-width:100%;font-size:24px">
  <line x1="130" y1="212" x2="560" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="212" x2="130" y2="212" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="197.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$238.045$</div></foreignObject>
  <line x1="130" y1="134" x2="560" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="134" x2="130" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="119.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$238.050$</div></foreignObject>
  <line x1="130" y1="56" x2="560" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="56" x2="130" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="41.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$238.055$</div></foreignObject>
  <line x1="130" y1="290" x2="560" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="130" y1="291" x2="130" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M130,28 L136,41 L124,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="142" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m\ (\text{u})$</div></foreignObject>
  <rect x="121" y="264" width="18" height="12" fill="#ffffff"/>
  <line x1="121" y1="268" x2="139" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="121" y1="278" x2="139" y2="272" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="160" y="121.5" width="80" height="168.5" fill="#c9c2b2" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="121" y="87" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$238.050787\,\text{u}$</span></div></foreignObject>
  <foreignObject x="171" y="305.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{238}\text{U}$</div></foreignObject>
  <rect x="280" y="193" width="80" height="97" fill="#b2f2bb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="241" y="158.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$238.046204\,\text{u}$</span></div></foreignObject>
  <foreignObject x="260" y="305.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{234}\text{Th} + {}^{4}\text{He}$</div></foreignObject>
  <line x1="240" y1="121.5" x2="428" y2="121.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="360" y1="193" x2="428" y2="193" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="420" y1="121.5" x2="420" y2="193" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="121.5" x2="428" y2="121.5" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="193" x2="428" y2="193" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="437" y="126" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0.004583\,\text{u}$</span></div></foreignObject>
  <foreignObject x="437" y="160" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$Q = 4.27\,\text{MeV}$</span></div></foreignObject>
</svg>

### Atomic masses in beta decay
In beta decay the charge number of the nucleus changes, so the initial and daughter atoms have different numbers of electrons. If nuclear masses are used, the mass of the electron or positron formed is included. With the masses $M$ of neutral atoms the bookkeeping depends on the type of decay. In beta minus decay the daughter nucleus has one more proton, so the daughter atom has one more electron than the initial atom. This extra electron matches the mass of the beta particle formed, so the mass of the electron is not added separately:
```latex
Q(\beta^-) = [M(\text{X}) - M(\text{Y})]\,c^2
```
where $M(\text{X})$ is the mass of the initial atom and $M(\text{Y})$ the mass of the daughter atom. In beta plus decay the daughter atom has one electron fewer than the initial atom, and in addition a positron is formed, whose mass is the same as that of an electron. That is why the mass of two electrons is subtracted:
```latex
Q(\beta^+) = [M(\text{X}) - M(\text{Y}) - 2m_e]\,c^2
```
where $m_e = 0.000549\,\text{u}$ is the mass of the electron. The model ignores the binding energies of the electrons of the atom, which are negligibly small at this precision.

## Worked example
Calculate the binding energy and the binding energy per nucleon of the helium-4 nucleus ${}^{4}_{2}\text{He}$. Use the atomic masses $m({}^{4}\text{He}) = 4.002603\,\text{u}$, $m_\text{H} = 1.007825\,\text{u}$ and $m_\text{n} = 1.008665\,\text{u}$ (AME2020) and $1\,\text{u} = 931.5\,\tfrac{\text{MeV}}{c^2}$.

<!-- vaihe -->

**Known and asked.** The atomic number is $Z = 2$ and the mass number $A = 4$, so the number of neutrons is $N = A - Z = 2$. The atomic masses are $m_\text{atom} = 4.002603\,\text{u}$, $m_\text{H} = 1.007825\,\text{u}$ and $m_\text{n} = 1.008665\,\text{u}$. The binding energy $E_\text{B}$ and the binding energy per nucleon $\tfrac{E_\text{B}}{A}$ are asked in megaelectronvolts.

<!-- vaihe -->

**Principle.** The nucleus is lighter than its separate nucleons, and the mass defect $\Delta m$ corresponds to the binding energy $E_\text{B} = \Delta m\,c^2$. We calculate with atomic masses: two hydrogen atoms contain two electrons, just like the helium-4 atom, so the masses of the electrons cancel.

<!-- vaihe -->

**Formula solved.** The mass defect, the binding energy and its share per nucleon:
```latex
\begin{aligned}
&\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atom} \\
&E_\text{B} = \Delta m\,c^2 \\
&\frac{E_\text{B}}{A} = \frac{\Delta m\,c^2}{A}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The mass is not converted to kilograms: $1\,\text{u} = 931.5\,\tfrac{\text{MeV}}{c^2}$ is put in place of the unit of the mass defect, so $c^2$ cancels and the energy is obtained directly in megaelectronvolts.

<!-- vaihe -->

**Substitution.** First the mass defect, then the energy:
```latex
\begin{aligned}
&\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atom} \\
&= 2 \cdot 1.007825\,\text{u} \\
&\quad + 2 \cdot 1.008665\,\text{u} \\
&\quad - 4.002603\,\text{u} \\
&= 0.030377\,\text{u} \\[6pt]
&E_\text{B} = \Delta m\,c^2 = 0.030377\,\text{u} \cdot c^2 \\
&= 0.030377 \cdot 931.5\,\tfrac{\text{MeV}}{c^2} \cdot c^2 \\
&= 28.296\,\text{MeV} \\[6pt]
&\frac{E_\text{B}}{A} = \frac{28.296\,\text{MeV}}{4} \\
&= 7.074\,\text{MeV}
\end{aligned}
```

<!-- vaihe -->

**Result.** The binding energy of the helium-4 nucleus is $28.30\,\text{MeV}$ and the binding energy per nucleon $7.074\,\text{MeV}$, four significant figures like the conversion factor $931.5\,\tfrac{\text{MeV}}{c^2}$.

<!-- vaihe -->

**Reasonableness.** With rounded numbers $\Delta m \approx 0.03\,\text{u}$ and $0.03 \cdot 900\,\text{MeV} = 27\,\text{MeV}$, close to the result. The mass defect is about $0.8\,\%$ of the mass of the atom, as it usually is for nuclei, and the value $7.07\,\text{MeV}$ per nucleon is the helium-4 point of the graph, clearly higher than its neighbours.

## Common misconception
Many think that binding energy is energy stored in the nucleus, which is released when the nucleus is broken into pieces. The opposite is true. The binding energy was *released* when the nucleus formed, and the same energy is *needed* to break the nucleus into separate nucleons. This is why the nucleus is lighter than its parts. A large binding energy per nucleon means a tightly bound, stable nucleus, not a store of energy. In a nuclear reaction energy is released when the total binding energy of the nuclei formed is *greater* than that of the original ones.

Another mistake is to think that mass is conserved in a nuclear reaction as in chemistry. In a nuclear reaction the mass number, that is, the number of nucleons, and the charge number are conserved, but the mass changes by the amount of the energy released, $\Delta m = \tfrac{Q}{c^2}$.

## Summary
- Atomic masses are given in atomic mass units: $1\,\text{u}$ is $\tfrac{1}{12}$ of the mass of a carbon-12 atom, that is, $1\,\text{u} = 1.66054 \cdot 10^{-27}\,\text{kg}$.
- A nucleus is lighter than its separate nucleons. The mass defect is

    $$\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atom}$$.

- The binding energy $E_\text{B} = \Delta m\,c^2$ is needed to break a nucleus into nucleons, and it is released when a nucleus forms. Putting in $1\,\text{u} = 931.5\,\tfrac{\text{MeV}}{c^2}$ gives the energy in megaelectronvolts.
- The binding energy per nucleon is highest, about $8.8\,\text{MeV}$, for iron and nickel; fusion and fission release energy because they move nucleons into more tightly bound nuclei.
- The reaction energy is $Q = (m_\text{initial} - m_\text{final})\,c^2$: mass is not conserved in a nuclear reaction, although the mass number and the charge number are. With atomic masses, in beta minus decay $Q(\beta^-) = [M(\text{X}) - M(\text{Y})]\,c^2$, and in beta plus decay $2m_e$ is also subtracted.
