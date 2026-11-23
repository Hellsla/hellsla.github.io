# The atomic nucleus and radioactive decay

> **Why** does a small sample of americium in a smoke detector keep emitting particles, and what happens to an americium nucleus when a particle leaves?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a white round smoke detector on the ceiling of a living room, partly drawn cut open. Inside, in a chamber between two metal plates, is a small americium sample, from which short violet particle tracks go out into the air. The room has a window and a ceiling lamp." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### The nucleus is made of nucleons
Almost all of the mass of an atom is in the nucleus at its centre. The diameter of a nucleus is of the order of $10^{-15}$–$10^{-14}\,\text{m}$, while the diameter of an atom is about $10^{-10}\,\text{m}$: the nucleus is tens of thousands of times smaller than the atom. The nucleus is made of protons and neutrons, which have a common name, **nucleons**. The charge of a proton is $+e$, and a neutron is electrically neutral.

A nucleus is described by two numbers. The **atomic number** $Z$ is the number of protons, and it determines the element. The **mass number** $A$ is the number of nucleons, so the neutron number is $N = A - Z$. A nucleus is written ${}^{A}_{Z}\text{X}$, where X is the symbol of the element. Nuclei of the same element with different numbers of neutrons are called **isotopes** of the element: carbon-12 ${}^{12}_{6}\text{C}$ and carbon-14 ${}^{14}_{6}\text{C}$ are isotopes of carbon. A particular kind of nucleus is called a nuclide.

<svg data-fig="isotopes" viewBox="0 0 600 340" role="img" aria-label="Two carbon nuclei side by side, not to scale. On the left carbon-12: six red protons and six grey neutrons, written with 12 as a superscript and 6 as a subscript in front of C. On the right carbon-14: six protons and eight neutrons. Both have six protons, so they are isotopes of the same element. At the bottom the key: a red ball is a proton, a grey one a neutron." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-isotopes.webp" x="0" y="0" width="600" height="352.5" preserveAspectRatio="none"/>
  <foreignObject x="99" y="204" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">${}^{12}_{\phantom{1}6}\text{C}$</div></foreignObject>
  <foreignObject x="100.5" y="247.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z = 6,\ N = 6$</div></foreignObject>
  <foreignObject x="399" y="204" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">${}^{14}_{\phantom{1}6}\text{C}$</div></foreignObject>
  <foreignObject x="400.5" y="247.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z = 6,\ N = 8$</div></foreignObject>
  <foreignObject x="190" y="297.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{proton } p^+$</div></foreignObject>
  <foreignObject x="400" y="297.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{neutron } n$</div></foreignObject>
</svg>

```pysahdy
A sodium nucleus is written ${}^{23}_{11}\text{Na}$. How many protons and neutrons does the nucleus have?
---
There are $Z = 11$ protons and $N = A - Z = 23 - 11 = 12$ neutrons.
```

### Why some nuclei decay
Protons repel each other electrically, but the nucleus is held together by the strong interaction. It pulls nucleons towards each other, but only over a very short distance, the size of a nucleus. Neutrons add attraction without adding repulsion, so stable heavy nuclei have more neutrons than protons.

Only certain combinations of protons and neutrons are stable. When nuclei are drawn on a chart of nuclides, with $N$ and $Z$ on the axes, the stable nuclei form a narrow band. A nucleus outside the band is unstable, or **radioactive**: over time it decays by itself and emits radiation. In alpha and beta decay the nucleus changes into another nuclide, but in gamma decay an excited nucleus only moves to a lower energy level and stays the same nuclide. The moment when a single nucleus decays cannot be predicted; decay is random.

<svg data-fig="chart" viewBox="0 0 600 380" role="img" aria-label="Chart of nuclides, schematic: the neutron number N from zero to 140 on the horizontal axis and the atomic number Z from zero to 90 on the vertical axis. The green band is the region of stable nuclei. For light nuclei it runs close to the dashed line N = Z, for heavy ones it bends below it, because stable heavy nuclei have more neutrons than protons. Below the band there are too many neutrons and the nucleus decays by beta minus decay, above it there are too few neutrons and the nucleus decays by beta plus decay. At the upper end of the band, Z above 82, heavy nuclei often decay by alpha decay: the violet arrow to the right of the upper end of the band points diagonally down and to the left, because alpha decay reduces both the neutron number and the atomic number by two." style="max-width:100%;font-size:24px">
  <line x1="135.5" y1="336" x2="135.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="191.5" y1="336" x2="191.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247" y1="336" x2="247" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="303" y1="336" x2="303" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="358.5" y1="336" x2="358.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="336" x2="414.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="336" x2="470" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="278" x2="470" y2="278" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="220.5" x2="470" y2="220.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="162.5" x2="470" y2="162.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="105" x2="470" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="336" x2="484" y2="336" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,336 L483,342 L483,330 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="337" x2="80" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,50 L86,63 L74,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="135.5" y1="336" x2="135.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="119" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="191.5" y1="336" x2="191.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="175" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="247" y1="336" x2="247" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="230.5" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="303" y1="336" x2="303" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="286.5" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="358.5" y1="336" x2="358.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="336" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="414.5" y1="336" x2="414.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="392" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$120$</div></foreignObject>
  <line x1="470" y1="336" x2="470" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$140$</div></foreignObject>
  <line x1="73" y1="278" x2="80" y2="278" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="263.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="73" y1="220.5" x2="80" y2="220.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="206" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="73" y1="162.5" x2="80" y2="162.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="148" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="73" y1="105" x2="80" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="90.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="50" y="341.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N$</div></foreignObject>
  <foreignObject x="70" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Z$</div></foreignObject>
  <polyline points="80,336 330.5,76" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 6"/>
  <foreignObject x="135.5" y="194.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$N = Z$</div></foreignObject>
  <polygon points="88,315.5 94,310 100,304.5 106,299.5 112,294 118,289 124.5,284 130.5,278.5 137,273.5 143,268.5 149.5,263.5 156,259 162.5,254 169,249 175.5,244.5 182,239.5 188.5,235 195,230 202,225.5 208.5,221 215,216 222,211.5 228.5,207 235.5,202.5 242.5,198 249,193.5 256,189 263,185 270,180.5 276.5,176 283.5,171.5 290.5,167.5 297.5,163 305,159 312,154.5 319,150.5 326,146 333,142 340.5,138 347.5,134 354.5,129.5 362,125.5 369,121.5 376.5,117.5 383.5,113.5 391,109.5 398,105.5 405.5,101.5 412.5,97.5 420,93.5 427.5,89.5 439.5,102.5 432.5,106.5 425,110 417.5,114 410.5,118 403,122 396,126 388.5,130 381.5,134 374,138.5 367,142.5 359.5,146.5 352.5,150.5 345.5,155 338,159 331,163 324,167.5 317,171.5 310,176 303,180 296,184.5 289,188.5 282,193 275,197.5 268,202 261.5,206.5 254.5,211 247.5,215.5 241,220 234,224.5 227.5,229 220.5,233.5 214,238 207.5,243 201,247.5 194,252 187.5,257 181,262 174.5,266.5 168,271.5 162,276.5 155.5,281.5 149,286.5 143,291.5 136.5,296.5 130.5,301.5 124.5,307 118.5,312 112,317.5 106.5,323 100.5,328.5" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2"/>
  <foreignObject x="314" y="258" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{too many neutrons: } \beta^-$</div></foreignObject>
  <foreignObject x="91" y="125" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{too few: } \beta^+$</div></foreignObject>
  <circle cx="467" cy="73" r="5" fill="#7048e8" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="464" y1="76" x2="455.5" y2="85.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M447.5,93.5 L452,81 L460,88.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="427.5" y="53" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\alpha$</div></foreignObject>
  <line x1="266.5" y1="197.5" x2="347.5" y2="197.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="353" y="183" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{stable}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/cloud-chamber-beta.webp" alt="Many thin, winding white tracks on a black background, spreading from a radioactive source at the top left."><figcaption>Beta particle tracks in a cloud chamber. An electron is light and ionises the air less than an alpha particle, so its track is thin and long. An electron is also easily deflected, so the track winds about.</figcaption></figure>

<figure class="unit-photo"><img src="pics/fy8/cloud-chamber-alpha.webp" alt="Many short, thick, straight white tracks in various directions on a black background, along with some thin winding tracks."><figcaption>Alpha particle tracks in a cloud chamber. An alpha particle ionises the air strongly and loses its energy within a few centimetres, so its track is short, thick and straight.</figcaption></figure>

### Alpha, beta and gamma decay
In **alpha decay**, an alpha particle, a helium nucleus ${}^{4}_{2}\text{He}$ with two protons and two neutrons, leaves the nucleus. It is typical of heavy nuclei such as uranium, radium and the americium of a smoke detector.

In **beta decay**, the nucleus has too many or too few neutrons compared with its protons. In beta minus decay, a neutron of the nucleus changes into a proton, and an electron and an antineutrino leave the nucleus. The electron was not in the nucleus beforehand; it is created in the decay. In beta plus decay, a proton changes into a neutron, and a positron, the antiparticle of the electron, and a neutrino leave the nucleus. Beta decay is caused by the weak interaction.

```pysahdy
Carbon-14 ${}^{14}_{6}\text{C}$ undergoes beta minus decay. What are the mass number and atomic number of the daughter nucleus, and which element is it?
---
A neutron turns into a proton, so $Z = 6 + 1 = 7$, and the number of nucleons stays the same, $A = 14$. The daughter nucleus is nitrogen-14, ${}^{14}_{7}\text{N}$.
```

Related to beta decay is **electron capture**: the nucleus captures an electron from the innermost electron shell of the atom, a proton changes into a neutron, and an electron neutrino ${}^{0}_{0}\nu_\text{e}$ leaves the nucleus. In general
```kaavat
electron capture :: {}^{A}_{Z}\text{X} + {}^{0}_{-1}\text{e} \to {}^{A}_{Z-1}\text{Y} + {}^{0}_{0}\nu_\text{e}
```
where X is the parent nucleus, Y the daughter nucleus and $Z$ the atomic number. For example, ${}^{7}_{4}\text{Be} + {}^{0}_{-1}\text{e} \to {}^{7}_{3}\text{Li} + {}^{0}_{0}\nu_\text{e}$. The nucleus changes as in beta plus decay ($Z - 1$), and capture is possible even when there is not enough energy to create a positron.

In **gamma decay**, a nucleus in an excited state, marked with an asterisk ${}^{A}_{Z}\text{X}^{\ast}$, moves to a lower energy level and emits a gamma photon. The nucleus stays the same nuclide. The excited state is often created in a previous alpha or beta decay, so gamma radiation follows them.

<svg data-fig="decays" viewBox="0 0 600 360" role="img" aria-label="Three kinds of decay side by side, a schematic figure, not to scale. On the left alpha decay: an alpha particle, a helium nucleus made of two protons and two neutrons, leaves the nucleus, and the atomic number of the nucleus decreases by two and the mass number by four. In the middle beta minus decay: a neutron of the nucleus changes into a proton, an electron and an antineutrino leave the nucleus, the atomic number increases by one and the mass number stays the same. On the right gamma decay: a nucleus in an excited state emits a gamma photon, and the atomic number and the mass number stay the same." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-decays.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="88" y="18" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#7048e8">$\alpha$</div></foreignObject>
  <foreignObject x="50.5" y="285.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z - 2,\ A - 4$</div></foreignObject>
  <foreignObject x="280.5" y="18" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#1971c2">$\beta^-$</div></foreignObject>
  <foreignObject x="236" y="285.5" width="128" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z + 1,\ A\ \text{same}$</div></foreignObject>
  <foreignObject x="488" y="18" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\gamma$</div></foreignObject>
  <foreignObject x="450.5" y="285.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z, A\ \text{same}$</div></foreignObject>
  <foreignObject x="131" y="145.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">${}^4_2\text{He}$</div></foreignObject>
  <foreignObject x="355.5" y="51.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="349.5" y="215.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\bar{\nu}$</div></foreignObject>
  <foreignObject x="550" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\gamma$</div></foreignObject>
  <foreignObject x="385" y="225.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{excited state } {}^{\ast}$</div></foreignObject>
</svg>

### Energy levels of the nucleus and the gamma spectrum
The energy of a nucleus is quantised like the energy of the electrons of an atom. When a nucleus moves from a higher energy level to a lower one, the energy of the gamma photon that leaves is the difference between the levels, just as in a transition of the hydrogen atom in the chapter *Energy levels of the hydrogen atom and the Bohr model*. This is why the gamma spectrum of a nucleus is a line spectrum: each peak tells the difference of one pair of levels. The scale is different. Transitions of an atom are of the order of electronvolts, while the differences between the levels of a nucleus are typically tens of kiloelectronvolts or more, so tens of thousands to hundreds of thousands of times larger.

For example, cobalt-60 decays by beta minus decay to an excited state of nickel-60 whose energy is $2505.8\,\text{keV}$ above the ground state. The nucleus returns to the ground state through an intermediate level at $1332.5\,\text{keV}$, and the gamma spectrum shows two lines: $1173.2\,\text{keV}$ and $1332.5\,\text{keV}$ (the NNDC NuDat 3 database, ENSDF values). The sum of the photon energies is less than the level energy by about $0.1\,\text{keV}$. Most of this gap is rounding: the recoil, the little kinetic energy the nucleus gains when a photon leaves, is only about $0.03\,\text{keV}$. Alpha particles likewise have only certain energies. The energies of beta particles, on the other hand, are spread continuously, because the decay energy is shared between the electron and the antineutrino.

<svg data-fig="levels" viewBox="0 0 600 380" role="img" aria-label="Energy level diagram, energies to scale: cobalt-60 decays by beta minus decay to an excited state of nickel-60 whose energy is 2505.8 keV above the ground state. The nucleus returns to the ground state in two steps: first to the level 1332.5 keV, emitting a gamma photon of 1173.2 keV, and then to the ground state, emitting a gamma photon of 1332.5 keV. Data from the NNDC NuDat database." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-levels.webp" x="3.7" y="1.2" width="594.1" height="386.1" preserveAspectRatio="none"/>
  <foreignObject x="58.5" y="50.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{60}_{27}\text{Co}$</div></foreignObject>
  <foreignObject x="170" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\beta^-$</div></foreignObject>
  <foreignObject x="440" y="59" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2505.8\,\text{keV}$</div></foreignObject>
  <foreignObject x="440" y="185.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1332.5\,\text{keV}$</div></foreignObject>
  <foreignObject x="440" y="329.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="153" y="329.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">${}^{60}_{28}\text{Ni}$</div></foreignObject>
  <foreignObject x="199" y="122" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$1173.2$</div></foreignObject>
  <foreignObject x="269" y="257.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$1332.5$</div></foreignObject>
</svg>

## Formula: Decay equations
In a decay equation, both the **mass number**, the total number of nucleons, and the **charge number**, the sum of the subscripts, are conserved. The electron is written ${}^{0}_{-1}\text{e}$ and the positron ${}^{0}_{+1}\text{e}$, because their mass number is zero and their charge is $-e$ or $+e$. Alpha decay is
```kaavat
alpha decay :: {}^{A}_{Z}\text{X} \to {}^{A-4}_{Z-2}\text{Y} + {}^{4}_{2}\text{He}
```
beta minus decay
```kaavat
$\beta^-$ decay :: {}^{A}_{Z}\text{X} \to {}^{A}_{Z+1}\text{Y} + {}^{0}_{-1}\text{e} + \bar{\nu}
```
beta plus decay
```kaavat
$\beta^+$ decay :: {}^{A}_{Z}\text{X} \to {}^{A}_{Z-1}\text{Y} + {}^{0}_{+1}\text{e} + \nu
```
and gamma decay
```latex
{}^{A}_{Z}\text{X}^{\ast} \to {}^{A}_{Z}\text{X} + \gamma
```
where X is the decaying parent nucleus, Y the daughter nucleus that is formed, $A$ the mass number, $Z$ the atomic number, $\bar{\nu}$ the antineutrino, $\nu$ the neutrino and $\gamma$ the gamma photon. The element of the daughter nucleus is read from the periodic table using its atomic number.

```pysahdy
Uranium-238 ${}^{238}_{92}\text{U}$ undergoes alpha decay. What are the mass number and atomic number of the daughter nucleus?
---
The alpha particle ${}^{4}_{2}\text{He}$ carries away four nucleons and two protons: $A = 238 - 4 = 234$ and $Z = 92 - 2 = 90$.
```

<svg data-fig="shifts" viewBox="0 0 600 360" role="img" aria-label="Part of a chart of nuclides, a grid: the neutron number N on the horizontal axis and the atomic number Z on the vertical axis, one cell is one unit. In the middle is the parent nucleus. Alpha decay moves the nucleus two cells down and two to the left (Z − 2, N − 2). Beta minus decay moves it one cell up and one to the left (Z + 1, N − 1). Beta plus decay moves it one cell down and one to the right (Z − 1, N + 1). In gamma decay the nucleus stays in the same cell." style="max-width:100%;font-size:24px">
  <line x1="140" y1="40" x2="140" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="40" x2="416" y2="40" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="40" x2="186" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="86" x2="416" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="232" y1="40" x2="232" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="132" x2="416" y2="132" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="278" y1="40" x2="278" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="178" x2="416" y2="178" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="40" x2="324" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="224" x2="416" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="40" x2="370" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="270" x2="416" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="40" x2="416" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="316" x2="416" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="281" y="135" width="40" height="40" rx="5" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="189" y="227" width="40" height="40" rx="5" fill="#ffffff" stroke="#7048e8" stroke-width="2"/>
  <rect x="235" y="89" width="40" height="40" rx="5" fill="#d0e6fb" stroke="#1971c2" stroke-width="2"/>
  <rect x="327" y="181" width="40" height="40" rx="5" fill="#f2a69c" stroke="#c92a2a" stroke-width="2"/>
  <line x1="288.5" y1="167.5" x2="228" y2="228" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M220.5,235.5 L225,223.5 L232.5,231 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="175" y="262.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\alpha$</div></foreignObject>
  <line x1="288.5" y1="142.5" x2="274" y2="128" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M266.5,120.5 L278.5,125 L271,132.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="214" y="64.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\beta^-$</div></foreignObject>
  <line x1="313.5" y1="167.5" x2="328" y2="182" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M335.5,189.5 L323.5,185 L331,177.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="361" y="216.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\beta^+$</div></foreignObject>
  <path d="M311,138 A 14 14 0 1 1 318,149" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="331" y="110.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\gamma$</div></foreignObject>
  <line x1="140" y1="334" x2="434" y2="334" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,334 L433,340 L433,328 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="452" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N$</div></foreignObject>
  <line x1="122" y1="316" x2="122" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M122,34 L128,47 L116,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="92" y="29.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$Z$</div></foreignObject>
</svg>

The energy of a gamma photon is the difference between the levels of the nucleus, and its wavelength is obtained from the photon energy:
```latex
\begin{aligned}
E_\gamma &= E_\text{u} - E_\text{l} \\
\lambda &= \frac{hc}{E_\gamma}
\end{aligned}
```
where $E_\text{u}$ and $E_\text{l}$ are the energies of the upper and the lower level, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$ is the Planck constant and $c = 2.998 \cdot 10^{8}\,\text{m/s}$ is the speed of light. Kiloelectronvolts are converted to joules by substituting $1\,\text{keV} = 1000\,\text{eV}$ and $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.

## Worked example
Caesium-137 ${}^{137}_{55}\text{Cs}$ decays by beta minus decay. The daughter nucleus is usually formed in an excited state, which relaxes by emitting a gamma photon with an energy of $661.7\,\text{keV}$ (NNDC NuDat 3). What is the daughter nucleus, and what is the wavelength of the gamma photon?

<!-- vaihe -->

**Given and asked.** The parent nucleus is ${}^{137}_{55}\text{Cs}$, beta minus decay, the energy of the gamma photon is $E_\gamma = 661.7\,\text{keV}$, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$ and $c = 2.998 \cdot 10^{8}\,\text{m/s}$. We are asked for the atomic number $Z'$ and the mass number $A'$ of the daughter nucleus and for the wavelength $\lambda$ of the photon.

<!-- vaihe -->

**Principle.** In beta minus decay a neutron changes into a proton, so the mass number and the charge number are conserved when the electron ${}^{0}_{-1}\text{e}$ is counted. The energy of a gamma photon is the difference between an excited state and the ground state, and the energy of a photon is $\tfrac{hc}{\lambda}$.

<!-- vaihe -->

**Formula solved.** From the conservation laws and the photon energy:
```latex
\begin{aligned}
&A = A' + 0, \quad Z = Z' - 1 \\
&A' = A, \quad Z' = Z + 1 \\
&\lambda = \frac{hc}{E_\gamma}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The energy is converted to joules by substituting $1\,\text{keV} = 1000\,\text{eV}$ and $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$: $E_\gamma = 661.7 \cdot 1000 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 1.0600 \cdot 10^{-13}\,\text{J}$.

<!-- vaihe -->

**Substitution.** The numbers of the daughter nucleus and the wavelength:
```latex
\begin{aligned}
&A' = 137, \quad Z' = 55 + 1 = 56 \\[6pt]
&hc = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \\
&\quad \cdot 2.998 \cdot 10^{8}\,\text{m/s} \\
&= 1.9865 \cdot 10^{-25}\,\text{J}\,\text{m} \\[6pt]
&\lambda = \frac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{1.0600 \cdot 10^{-13}\,\text{J}} \\
&= 1.8740 \cdot 10^{-12}\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Result.** The atomic number $56$ is barium, so the daughter nucleus is ${}^{137}_{56}\text{Ba}$: ${}^{137}_{55}\text{Cs} \to {}^{137}_{56}\text{Ba} + {}^{0}_{-1}\text{e} + \bar{\nu}$. The wavelength is $\lambda \approx 1.874 \cdot 10^{-12}\,\text{m} = 1.874\,\text{pm}$, four significant figures like the energy $661.7\,\text{keV}$.

<!-- vaihe -->

**Reasonableness.** On both sides of the equation the mass number is $137$ and the charge number is $55 = 56 - 1$. The wavelength of visible light, $500\,\text{nm}$, is about $270\,000$ times longer, so the photon energy is hundreds of thousands of times greater than that of a photon of visible light: this is the scale of the levels of a nucleus.

## Common misconception
Many people think that a beta particle is an electron that was already in the nucleus. There are no electrons in the nucleus: the electron and the antineutrino are created when a neutron changes into a proton. This is why the atomic number increases by one although a negative particle leaves the nucleus.

Another mistake is to think that gamma decay changes the element. A gamma photon carries away only energy: the numbers of protons and neutrons stay the same, and the nucleus only moves to a lower energy level. The element changes only when the number of protons changes: in alpha and beta decay and in electron capture.

## Summary
- A nucleus is made of nucleons: $Z$ protons and $N = A - Z$ neutrons. Isotopes of the same element have the same $Z$ but a different $N$.
- A radioactive nucleus decays by itself and at random. In alpha decay ${}^{4}_{2}\text{He}$ leaves ($Z - 2$, $A - 4$), in beta minus decay an electron and an antineutrino ($Z + 1$), in beta plus decay a positron and a neutrino ($Z - 1$).
- In electron capture the nucleus captures an electron and emits a neutrino ($Z - 1$).
- In a decay equation the mass number and the charge number are conserved.
- The energy of a nucleus is quantised. The energy of a gamma photon is the difference between the levels of the nucleus, $E_\gamma = E_\text{u} - E_\text{l}$, typically tens or hundreds of kiloelectronvolts or megaelectronvolts, so the gamma spectrum is a line spectrum.
