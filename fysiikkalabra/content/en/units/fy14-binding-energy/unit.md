# Mass defect and binding energy

> **Why** can both joining nuclei and splitting nuclei release energy?

<!-- The Binding Energy Explorer in inquiry.json reads data-src="units/fy14/data/nuclides.json" (named here so that build.py embeds it and the content hash covers it). -->

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration on a dark background, in two halves. Left: two small nuclei, made of red protons and grey neutrons, fly towards each other and meet in a bright yellow flash. Right: a large nucleus with many protons and neutrons breaks into two medium-sized pieces that fly apart, with a few single neutrons and another bright flash." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-binding-energy-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Formula: Mass–energy equivalence

In 1905 Albert Einstein showed that mass and energy are two sides of the same quantity. If a system gives away the energy $E$, its mass decreases by $\Delta m$:
```latex
E = \Delta m \cdot c^2
```
where $c = 2.998 \cdot 10^{8}\ \text{m/s}$ is the speed of light. Because $c^2$ is so large, a tiny mass corresponds to a huge energy: $1\ \text{kg}$ corresponds to $9.0 \cdot 10^{16}\ \text{J}$.

In nuclear physics, masses are given in **atomic mass units** and energies in **megaelectronvolts**, $1\ \text{MeV} = 10^{6}\ \text{eV} = 1.602 \cdot 10^{-13}\ \text{J}$. The mass $1\ \text{u} = 1.661 \cdot 10^{-27}\ \text{kg}$ corresponds to the energy
```latex
1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}
```
so a mass difference in $\text{u}$ times $931.5\ \text{MeV/u}$ gives the energy in $\text{MeV}$.

## Key idea

A nucleus has *less* mass than the free protons and neutrons it is made of. The difference is the **mass defect** $\Delta m$. When nucleons join, the strong force pulls them together and energy is released, so the system loses mass. To pull the nucleus apart again, the same energy must be given back. This energy is the **binding energy** $B$:
```latex
B = \Delta m \cdot c^2
```

<svg data-fig="ladder" viewBox="0 0 600 380" role="img" aria-label="Energy diagram of helium-4. An upper level: two protons and two neutrons far apart, with the total mass 4.032980 u. A lower level, 28.3 MeV below: the helium-4 nucleus, mass 4.002603 u. An arrow up on the left is the binding energy B = 28.3 MeV that must be added to separate the nucleons. An arrow down on the right is the same energy released when they join." style="max-width:100%;font-size:26px">
  <image href="pics/fy14/fy14-binding-energy-ladder.webp" x="1.2" y="0" width="597" height="384.3" preserveAspectRatio="none"/>
  <foreignObject x="250" y="18.5" width="170" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{free nucleons}$</div></foreignObject>
  <foreignObject x="261.5" y="316.5" width="147" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">${}^{4}\text{He}\ \text{nucleus}$</div></foreignObject>
  <foreignObject x="450" y="94.5" width="134" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$4.032980\ \text{u}$</div></foreignObject>
  <foreignObject x="450" y="284.5" width="134" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$4.002603\ \text{u}$</div></foreignObject>
  <foreignObject x="6" y="153.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{add}$</div></foreignObject>
  <foreignObject x="6" y="189.5" width="184" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${B = 28.3\ \text{MeV}}$</div></foreignObject>
  <foreignObject x="379" y="177.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$\text{released}$</div></foreignObject>
</svg>

We calculate with the **atomic masses** of tables such as AME2020, which include the electrons. So for the protons we use the mass of a hydrogen-1 atom, $m_\text{H} = 1.007825\ \text{u}$, and the electrons cancel:
```latex
\Delta m = Z \cdot m_\text{H} + N \cdot m_\text{n} - m_\text{atom}
```
Here $m_\text{n} = 1.008665\ \text{u}$ is the mass of a neutron.

```pysahdy
Why must energy be added to a nucleus to split it into free protons and neutrons?
---
The nucleus has less mass, and so less energy, than its separate nucleons. The binding energy $B = \Delta m \cdot c^2$ must be supplied to separate them.
```

## Binding energy per nucleon {Curve}

To compare nuclei, we divide the binding energy by the number of nucleons. The **binding energy per nucleon** $B/A$ tells how tightly each nucleon is held on average. A large $B/A$ means a tightly bound nucleus.

The curve of $B/A$ rises steeply among the light nuclei: $1.11\ \text{MeV}$ for deuterium, $7.07\ \text{MeV}$ for helium-4. It reaches its peak near iron and nickel ($8.79\ \text{MeV}$ for $^{56}\text{Fe}$ and $^{62}\text{Ni}$) and then falls slowly to $7.59\ \text{MeV}$ for $^{235}\text{U}$. In light nuclei, every added nucleon finds more neighbours to bind to. In heavy nuclei, the electric repulsion of the many protons wins back part of the binding.

```pysahdy
Which nucleus has the larger binding energy per nucleon, $^{56}\text{Fe}$ or $^{235}\text{U}$, and which is more tightly bound?
---
$^{56}\text{Fe}$ has $8.79\,\text{MeV}$ per nucleon and $^{235}\text{U}$ only $7.59\,\text{MeV}$. A larger $B/A$ means a more tightly bound nucleus, so iron is more tightly bound.
```

## Fission and fusion {Reactions}

A nuclear reaction releases energy when its products are *more tightly bound* than the nuclei it starts from. The energy released, the **Q-value**, is
```latex
\begin{aligned}
Q &= (m_\text{before} - m_\text{after}) \cdot c^2 \\
&= B_\text{after} - B_\text{before}
\end{aligned}
```
Both sides of the peak can climb towards it:

- In **fusion**, two light nuclei join into a heavier one. Deuterium and tritium give helium-4 and a neutron, with $Q = 17.6\ \text{MeV}$.
- In **fission**, a heavy nucleus splits into two medium-sized ones. A uranium-235 nucleus that absorbs a neutron releases about $200\ \text{MeV}$ in all.

<svg data-fig="qbars" viewBox="0 0 600 400" role="img" aria-label="Two bar charts of the total binding energy before and after a reaction; each has its own scale. Left, D–T fusion: before, deuterium plus tritium, 10.7 MeV; after, helium-4 plus a neutron, 28.3 MeV; the difference Q = 17.6 MeV is released. Right, fission of uranium-235 into barium-141, krypton-92 and three neutrons: before 1784 MeV, after 1957 MeV, Q = 173 MeV. In both, the products are more tightly bound." style="max-width:100%;font-size:26px">
  <foreignObject x="80" y="12.5" width="130" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{D–T fusion}$</div></foreignObject>
  <line x1="30" y1="330" x2="270" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="50" y="248" width="80" height="82" fill="#d0e6fb" stroke="#1971c2" stroke-width="2"/>
  <rect x="170" y="113" width="80" height="217" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="40.5" y="213.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10.7\ \text{MeV}$</div></foreignObject>
  <foreignObject x="160.5" y="78.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$28.3\ \text{MeV}$</div></foreignObject>
  <foreignObject x="67.5" y="341.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{D + T}$</div></foreignObject>
  <foreignObject x="175" y="341.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{4}\text{He + n}$</div></foreignObject>
  <line x1="130" y1="248" x2="270" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M260,248 V113" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="264" y="165" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="364.5" y="12.5" width="161" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">${}^{235}\text{U}\ \text{fission}$</div></foreignObject>
  <line x1="330" y1="330" x2="570" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="350" y="125" width="80" height="205" fill="#d0e6fb" stroke="#1971c2" stroke-width="2"/>
  <rect x="470" y="105" width="80" height="225" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="340.5" y="90.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1784\ \text{MeV}$</div></foreignObject>
  <foreignObject x="460.5" y="70.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1957\ \text{MeV}$</div></foreignObject>
  <foreignObject x="348.5" y="341.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{235}\text{U + n}$</div></foreignObject>
  <foreignObject x="475" y="341.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Ba + Kr}$</div></foreignObject>
  <line x1="430" y1="125" x2="570" y2="125" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M560,125 V105" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="564" y="99.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="34" y="369.5" width="532" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{total binding energy; each panel has its own scale}$</div></foreignObject>
</svg>

The figure shows one possible split of uranium-235, into barium-141, krypton-92 and three neutrons: it releases $173\ \text{MeV}$ at once, and the radioactive fragments release more later.

Fission was discovered in Berlin in December 1938 by Otto Hahn and Fritz Strassmann. Lise Meitner and Otto Frisch explained it at Christmas 1938 (published February 1939) and used $E = \Delta m \cdot c^2$ to estimate the energy. Fission gives about $0.85\ \text{MeV}$ per nucleon of fuel; D–T fusion gives $3.5\ \text{MeV}$ per nucleon, about four times more.

## Worked example

The atomic mass of helium-4 is $4.002603\ \text{u}$ (AME2020). Calculate the mass defect, the binding energy and the binding energy per nucleon of the helium-4 nucleus.

<!-- vaihe -->

**Given:** $m(^{4}\text{He}) = 4.002603\ \text{u}$, $Z = 2$, $N = 2$, $A = 4$; from AME2020, $m_\text{H} = 1.007825\ \text{u}$ and $m_\text{n} = 1.008665\ \text{u}$; ${1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}}$. **Find:** the mass defect $\Delta m$, the binding energy $B$ and $B/A$.

<!-- vaihe -->

**Principle:** The nucleus has less mass than its free nucleons; the difference times $c^2$ is the energy needed to separate them. Atomic masses are used, so the two protons are counted as two hydrogen-1 atoms and the two electrons cancel.

<!-- vaihe -->

**Formula:**
```latex
\begin{aligned}
\Delta m &= Z \cdot m_\text{H} + N \cdot m_\text{n} \\
&\quad - m(^{4}\text{He}) \\
B &= \Delta m \cdot c^2 \\
\frac{B}{A} &= \frac{\Delta m \cdot c^2}{A}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** The mass defect stays in $\text{u}$, and ${1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}}$ turns it into an energy in megaelectronvolts.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
\Delta m &= 2 \cdot 1.007825\ \text{u} \\
&\quad + 2 \cdot 1.008665\ \text{u} \\
&\quad - 4.002603\ \text{u} \\
&= 4.032980\ \text{u} - 4.002603\ \text{u} \\
&= 0.030377\ \text{u} \\[4pt]
B &= 0.030377\ \text{u} \cdot 931.5\ \text{MeV/u} \\
&= 28.30\ \text{MeV} \\[4pt]
\frac{B}{A} &= \frac{28.30\ \text{MeV}}{4} = 7.074\ \text{MeV}
\end{aligned}
```

<!-- vaihe -->

**Answer:** $\Delta m = 0.0304\ \text{u}$, $B = 28.3\ \text{MeV}$ and $B/A = 7.07\ \text{MeV}$ per nucleon. Three significant figures are enough, because $931.5\ \text{MeV/u}$ is given to four and the result is used only to three.

<!-- vaihe -->

**Reasonableness:** The mass defect is $0.030377 : 4.032980 = 0.75\ \%$ of the mass of the free particles: small, as expected, but far larger than in any chemical reaction. The value $7.07\ \text{MeV}$ is the point of $^{4}\text{He}$ on the binding energy curve.

## The people behind fission {People}

### Lise Meitner (1878–1968)

<figure class="unit-photo"><img src="units/fy14/pics/meitner.jpg" alt="Black-and-white photograph of Lise Meitner, an older woman in a dark jacket and white blouse, sitting in front of bookshelves with a book in her hands." width="960" height="1255" loading="lazy"><figcaption>Lise Meitner (1878–1968) explained nuclear fission together with Otto Frisch in 1939, using the idea of mass defect and $E = mc^2$. <span class="photo-credit">Photo: Harris &amp; Ewing, public domain, via Wikimedia Commons</span></figcaption></figure>

Lise Meitner was an Austrian physicist who worked for about thirty years in Berlin with the chemist Otto Hahn. In July 1938 she had to flee from Nazi Germany and moved to Sweden. In December Hahn wrote to her that uranium hit by neutrons gave barium, a much lighter element. Over Christmas 1938 Meitner and her nephew Otto Frisch worked out that the uranium nucleus had split in two, and with $E = \Delta m \cdot c^2$ they estimated about $200\ \text{MeV}$ per split. The Nobel Prize in Chemistry for 1944 went to Hahn alone, which many scientists see as unjust. Element 109, meitnerium, is named after her.

## Common misconception

"Binding energy is energy stored in the nucleus, and a nucleus with a large binding energy has a lot of energy to give." It is the other way round. Binding energy is the energy you must *add* to take a nucleus apart. A tightly bound nucleus has already given its energy away; energy is released when nuclei move *towards* larger $B/A$.

"In a nuclear reaction, protons and neutrons are destroyed and turned into energy." The number of nucleons stays the same before and after: in D–T fusion, $5$ nucleons go in and $5$ come out. Only the mass of the bound system changes.

## Summary

- Mass and energy are equivalent: $E = \Delta m \cdot c^2$, and $1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}$.
- A nucleus has less mass than its free nucleons. The mass defect times $c^2$ is the binding energy $B$, the energy needed to take the nucleus apart.
- The binding energy per nucleon $B/A$ peaks near iron-56 and nickel-62 at about $8.8\ \text{MeV}$.
- Fusion of light nuclei and fission of heavy nuclei both move towards the peak, so both release energy: $Q = B_\text{after} - B_\text{before}$.
- D–T fusion releases $17.6\ \text{MeV}$; the fission of uranium-235 about $200\ \text{MeV}$, but fusion gives more energy per nucleon of fuel.
