# Building nuclei: isotopes and nuclear notation

> **Why** do the protons in a nucleus not fly apart, although they all repel each other?

<!-- The Isotope Builder in inquiry.json reads data-src="units/fy14/data/nuclides.json" (named here so that build.py embeds it and the content hash covers it). -->

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a dark background. On the left, a large, faint blue cloud stands for the electrons of an atom; at its centre is a tiny bright dot, the nucleus. Two thin lines lead from the dot to a large magnifying circle on the right. Inside the circle the nucleus is shown enlarged: a tight cluster of red protons, each marked with a plus sign, and grey neutrons, all touching each other." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-nucleus-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Inside the atom {Particles}

An atom has a tiny **nucleus** with **electrons** around it (Rutherford, 1911). The nucleus is made of **protons** and **neutrons**, together called **nucleons**. Rutherford identified the proton in experiments from 1917 to 1920; James Chadwick discovered the neutron in 1932.

| Particle | Charge | Mass (u) | Where |
| --- | --- | --- | --- |
| proton | $+e$ | $1.00728$ | nucleus |
| neutron | $0$ | $1.00866$ | nucleus |
| electron | $-e$ | $0.00055$ | around it |

Here $e = 1.602 \cdot 10^{-19}\ \text{C}$ is the elementary charge and $1\ \text{u} = 1.661 \cdot 10^{-27}\ \text{kg}$ the **atomic mass unit**. A proton is $1836$ times as heavy as an electron, so almost all the mass of an atom is in the nucleus, although its diameter is only $1/60\,000$ (hydrogen) to $1/27\,000$ (uranium) of the atom's.

```pysahdy
Why is almost all the mass of an atom in the nucleus, although the nucleus is tiny?
---
Protons and neutrons are about $1836$ times as heavy as electrons, so the electrons add very little mass.
```

## Key idea

The number of protons is the **atomic number** $Z$. It decides the element: every carbon nucleus has $Z = 6$, every uranium nucleus $Z = 92$. The number of neutrons is the **neutron number** $N$. Nuclei of one element with different numbers of neutrons are **isotopes** of the element, from the Greek for "same place": they share a place in the periodic table. The Scottish doctor Margaret Todd suggested the word to the chemist Frederick Soddy in 1913.

Isotopes have practically the same chemistry but different masses. Some are **stable**; others are **radioactive** and change into another nucleus after some time. Hydrogen has three isotopes, and two of them are the fuel of fusion reactors:

<svg data-fig="hydrogen" viewBox="0 0 600 300" role="img" aria-label="Three nuclei side by side, drawn as red protons with a plus sign and grey neutrons. Left: hydrogen-1, one proton only, notation 1 over 1 H, stable. Middle: hydrogen-2 or deuterium, one proton and one neutron, 2 over 1 H, stable. Right: hydrogen-3 or tritium, one proton and two neutrons, 3 over 1 H, radioactive with a half-life of 12.3 years. All three have Z = 1, so they are the same element." style="max-width:100%;font-size:26px">
  <defs><radialGradient id="fy14nu-hy-p" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#ff8a80"/><stop offset="55%" stop-color="#c92a2a"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient><radialGradient id="fy14nu-hy-n" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#e9ecef"/><stop offset="55%" stop-color="#9aa1a9"/><stop offset="100%" stop-color="#4b5259"/></radialGradient></defs>
  <circle cx="100" cy="92" r="22" fill="url(#fy14nu-hy-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="90" y1="92" x2="110" y2="92" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <line x1="100" y1="82" x2="100" y2="102" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <circle cx="281" cy="92" r="22" fill="url(#fy14nu-hy-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="319" cy="92" r="22" fill="url(#fy14nu-hy-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="309" y1="92" x2="329" y2="92" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <line x1="319" y1="82" x2="319" y2="102" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <circle cx="481" cy="103" r="22" fill="url(#fy14nu-hy-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="519" cy="103" r="22" fill="url(#fy14nu-hy-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="500" cy="72" r="22" fill="url(#fy14nu-hy-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="490" y1="72" x2="510" y2="72" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <line x1="500" y1="62" x2="500" y2="82" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <foreignObject x="69.5" y="149.5" width="61" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:34px">${}^{1}_{1}\text{H}$</div></foreignObject>
  <foreignObject x="28.5" y="206.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{hydrogen-1}$</div></foreignObject>
  <foreignObject x="55.5" y="242.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#2b8a3e">$\text{stable}$</div></foreignObject>
  <foreignObject x="269.5" y="149.5" width="61" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:34px">${}^{2}_{1}\text{H}$</div></foreignObject>
  <foreignObject x="235" y="206.5" width="130" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{deuterium}$</div></foreignObject>
  <foreignObject x="255.5" y="242.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#2b8a3e">$\text{stable}$</div></foreignObject>
  <foreignObject x="469.5" y="149.5" width="61" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:34px">${}^{3}_{1}\text{H}$</div></foreignObject>
  <foreignObject x="448.5" y="206.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{tritium}$</div></foreignObject>
  <foreignObject x="426.5" y="242.5" width="147" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$T_{1/2} = 12.3\ \text{a}$</div></foreignObject>
  <line x1="200" y1="30" x2="200" y2="280" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="30" x2="400" y2="280" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
</svg>

About one hydrogen atom in $6400$ on Earth is deuterium, so every litre of water contains some. Tritium is radioactive, with a **half-life** of $12.3$ years, so there is almost none in nature.

```pysahdy
Why is there almost no tritium in nature?
---
Tritium is radioactive with a half-life of $12.3$ years, so the tritium that formed earlier has decayed.
```

## Formula: Mass number and nuclear notation

The **mass number** $A$ is the total number of nucleons:
```latex
A = Z + N
```
A nucleus is written in **nuclear notation** as $^{A}_{Z}\text{X}$, where $\text{X}$ is the chemical symbol. The symbol and $Z$ always belong together, so $Z$ is sometimes left out: $^{14}\text{C}$ or "carbon-14" means the same as $^{14}_{6}\text{C}$.

<svg data-fig="notation" viewBox="0 0 600 300" role="img" aria-label="Diagram of nuclear notation, using carbon-14 as the example. In the middle the large chemical symbol C. Top left, the mass number 14, with a label: mass number A, the number of protons plus neutrons. Bottom left, the atomic number 6, with a label: atomic number Z, the number of protons. A label on the right says that the symbol names the element, and that Z and the symbol always belong together. Below: N = A − Z = 8 neutrons." style="max-width:100%;font-size:26px">
  <foreignObject x="337" y="72" width="110" height="156" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:130px">$\text{C}$</div></foreignObject>
  <foreignObject x="257" y="50.5" width="80" height="67" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:56px">$14$</div></foreignObject>
  <foreignObject x="287" y="180.5" width="50" height="67" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:56px">$6$</div></foreignObject>
  <foreignObject x="16" y="36.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{mass number}$</div></foreignObject>
  <foreignObject x="16" y="70.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$A = Z + N$</div></foreignObject>
  <line x1="160" y1="86" x2="240" y2="86" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M252,86 L239,92 L239,80 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="16" y="184.5" width="170" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{atomic number}$</div></foreignObject>
  <foreignObject x="16" y="218.5" width="147" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$Z\ (\text{protons})$</div></foreignObject>
  <line x1="196" y1="214" x2="270" y2="214" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M282,214 L269,220 L269,208 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="480" y1="150" x2="464" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M452,150 L465,144 L465,156 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="484" y="102.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{chemical}$</div></foreignObject>
  <foreignObject x="484" y="134.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{symbol}$</div></foreignObject>
  <foreignObject x="484" y="166.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$(\text{by } Z)$</div></foreignObject>
  <foreignObject x="328.5" y="262.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$N = A - Z = 8$</div></foreignObject>
</svg>

The mass number is a count, not a mass, although it is close to the mass in $\text{u}$.

## The force that holds the nucleus {Forces}

Inside a nucleus, protons are only about $1\text{–}2\ \text{fm}$ apart ($1\ \text{fm} = 10^{-15}\ \text{m}$). There the electric repulsion of two protons is huge, about $58\ \text{N}$ at $2\ \text{fm}$. Gravity between them is about $10^{36}$ times weaker.

The nucleus is held by a different force, the **strong nuclear force**. It attracts any two nucleons, protons and neutrons alike, and it beats the electric repulsion when they nearly touch. But it has a very **short range**: it fades out by about $2.5\ \text{fm}$. Below about $0.7\ \text{fm}$ it repels, so nucleons cannot be squeezed together.

```pysahdy
What does the strong force do to two nucleons that are closer than about $0.7\,\text{fm}$?
---
It repels them, so nucleons cannot be squeezed together.
```

<svg data-fig="ranges" viewBox="0 0 600 350" role="img" aria-label="Schematic bar diagram along an axis of distance r between the centres of two nucleons, from 0 to 10 femtometres. Top bar, green: the strong nuclear force attracts from about 0.7 fm and fades out by about 2.5 fm; below 0.7 fm it repels (a hatched grey part). Middle bar, red: the electric repulsion between two protons acts at every distance and continues past the end of the axis, getting weaker with distance. Bottom: a bracket shows the diameter of an iron-56 nucleus, about 9.2 fm, much wider than the reach of the strong force." style="max-width:100%;font-size:26px">
  <defs><linearGradient id="fy14nu-r-g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2b8a3e"/><stop offset="0.6" stop-color="#2b8a3e"/><stop offset="1" stop-color="#2b8a3e" stop-opacity="0.05"/></linearGradient><pattern id="fy14nu-r-h" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#e3dccb"/><line x1="0" y1="0" x2="0" y2="10" stroke="#6b7480" stroke-width="3"/></pattern><linearGradient id="fy14nu-r-e" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c92a2a"/><stop offset="0.65" stop-color="#c92a2a"/><stop offset="1" stop-color="#c92a2a" stop-opacity="0.25"/></linearGradient></defs>
  <line x1="40" y1="300" x2="514" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,300 L513,306 L513,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="40" y1="300" x2="40" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$0$</div></foreignObject>
  <line x1="132" y1="300" x2="132" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="121" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$2$</div></foreignObject>
  <line x1="224" y1="300" x2="224" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="213" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$4$</div></foreignObject>
  <line x1="316" y1="300" x2="316" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="305" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$6$</div></foreignObject>
  <line x1="408" y1="300" x2="408" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="397" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$8$</div></foreignObject>
  <line x1="500" y1="300" x2="500" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="482.5" y="312.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10$</div></foreignObject>
  <foreignObject x="524" y="258.5" width="80" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$r\ (\text{fm})$</div></foreignObject>
  <rect x="40" y="56" width="32" height="40" fill="url(#fy14nu-r-h)" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="72" y="56" width="83" height="40" fill="url(#fy14nu-r-g)" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="169" y="46.5" width="278" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#2b8a3e">$\text{strong force: attracts}$</div></foreignObject>
  <foreignObject x="169" y="76.5" width="224" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{(any two nucleons)}$</div></foreignObject>
  <foreignObject x="42" y="14.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{repels}$</div></foreignObject>
  <path d="M40,126 H500 V118 L522,146 L500,174 V166 H40 Z" fill="url(#fy14nu-r-e)" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="58.5" y="130.5" width="278" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#ffffff">$\text{electric force: repels}$</div></foreignObject>
  <foreignObject x="58.5" y="176.5" width="332" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{(two protons, any distance)}$</div></foreignObject>
  <path d="M40,256 V270 H462.5 V256" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="110" y="220.5" width="282" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{diameter of }{}^{56}\text{Fe} \approx 9.2\ \text{fm}$</span></div></foreignObject>
</svg>

So each nucleon is held only by its nearest neighbours, but each proton is pushed by *every* other proton in the nucleus. Neutrons add attraction without adding repulsion. This is why light stable nuclei have $N \approx Z$, but heavy stable nuclei need more neutrons than protons. Above lead, no amount of neutrons makes a nucleus fully stable.

## Worked example

An iron-56 nucleus, $^{56}_{26}\text{Fe}$, has the mass $m = 9.29 \cdot 10^{-26}\ \text{kg}$. Its radius can be estimated with $R = r_0 A^{1/3}$, where $r_0 = 1.2\ \text{fm}$. How many protons and neutrons does it have, how large is it, and what is the density of the nucleus?

<!-- vaihe -->

**Given:** mass number $A = 56$, atomic number $Z = 26$, mass ${m = 9.29 \cdot 10^{-26}\ \text{kg}}$, ${r_0 = 1.2\ \text{fm}}$. **Find:** the number of protons $Z$, the number of neutrons $N$, the radius $R$ and the density $\rho$.

<!-- vaihe -->

**Principle:** The lower number in the notation is the number of protons, the upper one the number of nucleons, $A = Z + N$. A nucleus is close to a sphere, so its volume is $V = \frac{4}{3}\pi R^3$, and the density is mass divided by volume.

<!-- vaihe -->

**Formula:** Solved in symbols:
```latex
\begin{aligned}
N &= A - Z \\
R &= r_0 A^{1/3} \\
\rho &= \frac{m}{V} = \frac{3m}{4\pi R^3}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** ${r_0 = 1.2\ \text{fm} = 1.2 \cdot 10^{-15}\ \text{m}}$, so that the density comes out in $\text{kg/m}^3$.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
N &= 56 - 26 = 30 \\[4pt]
R &= 1.2 \cdot 10^{-15}\ \text{m} \cdot 56^{1/3} \\
&= 1.2 \cdot 10^{-15}\ \text{m} \cdot 3.826 \\
&= 4.59 \cdot 10^{-15}\ \text{m} \\[4pt]
\rho &= \frac{3 \cdot 9.29 \cdot 10^{-26}\ \text{kg}}{4\pi \cdot (4.59 \cdot 10^{-15}\ \text{m})^3} \\
&= 2.29 \cdot 10^{17}\ \text{kg/m}^3
\end{aligned}
```

<!-- vaihe -->

**Answer:** The nucleus has $26$ protons and $30$ neutrons. Its radius is about $4.6\ \text{fm}$ and its density about $2 \cdot 10^{17}\ \text{kg/m}^3$. The density is given to one significant figure, because $R = r_0 A^{1/3}$ is only an estimate: a nucleus has no sharp surface.

<!-- vaihe -->

**Reasonableness:** The density of solid iron is about $7900\ \text{kg/m}^3$. The nucleus is about $3 \cdot 10^{13}$ times denser, which fits: almost all of the mass of an atom sits in a volume $10^{13}\text{–}10^{14}$ times smaller than the atom. A teaspoon ($5\ \text{cm}^3$) of nuclear matter would have a mass of about $10^{12}\ \text{kg}$.

## The people behind the neutron {People}

### James Chadwick (1891–1974)

<figure class="unit-photo"><img src="units/fy14/pics/chadwick.jpg" alt="Black-and-white photograph of four men talking at a table; one of them, General Groves, is in army uniform." width="600" height="460" loading="lazy"><figcaption>James Chadwick (left), discoverer of the neutron in 1932, with General Leslie Groves, Richard Tolman and Henry DeWolf Smyth during the Manhattan Project, the wartime US atomic bomb programme. <span class="photo-credit">Photo: United States Army Signal Corps, public domain, via Wikimedia Commons</span></figcaption></figure>

James Chadwick was an English physicist who studied under Ernest Rutherford in Manchester and followed him to the Cavendish Laboratory in Cambridge. Rutherford had suggested that the nucleus might contain a neutral particle, but nobody had found it. In 1932 Chadwick aimed the radiation from polonium and beryllium at paraffin wax and measured the protons that it knocked out. Only a neutral particle with about the mass of a proton explained the results. In February 1932 he reported "the possible existence of a neutron". He received the Nobel Prize in Physics in 1935.

## Common misconception

"Isotopes are different elements." No: isotopes have the same $Z$ and so belong to the same element. Only the number of neutrons, and so the mass, is different. If the number of protons changes, the element changes.

"The mass number is the mass of the nucleus." The mass number is a whole number that counts nucleons. The real mass of $^{56}\text{Fe}$ is not $56\ \text{u}$, and in the next unit you will see why the difference matters.

"The neutrons hold the nucleus together by cancelling the charge of the protons." A neutron has no charge, so it cannot cancel anything. It helps because the strong force also acts on it.

## Summary

- A nucleus contains $Z$ protons and $N$ neutrons; the mass number is $A = Z + N$, written $^{A}_{Z}\text{X}$.
- $Z$ decides the element. Isotopes of an element have the same $Z$ but different $N$.
- Hydrogen-1, deuterium $^{2}_{1}\text{H}$ and tritium $^{3}_{1}\text{H}$ are the isotopes of hydrogen; tritium is radioactive.
- The nucleus is about $10^{-15}\text{–}10^{-14}\ \text{m}$ across, and nuclear matter has a density of about $2 \cdot 10^{17}\ \text{kg/m}^3$.
- The strong nuclear force attracts all nucleons but only over about $2.5\ \text{fm}$; the electric repulsion of protons reaches across the whole nucleus. That is why heavy nuclei need extra neutrons.
