# The puzzle of the Sun's energy

> **Why** hasn't the Sun burned out?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a bright Sun in a pale sky above the sea. In front, a tall cliff shows many horizontal rock layers in sand, brown and grey colours, stacked one on top of another. In one of the lower layers lies a spiral fossil shell. Small waves break at the foot of the cliff." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-sun-puzzle-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Three candidate explanations {Candidates}

The Sun radiates the power $L = 3.83 \cdot 10^{26}\ \text{W}$, its **luminosity**. In the 19th century, physicists asked where this energy comes from, and how long the supply can last.

The first idea was **chemical energy**: perhaps the Sun burns like a giant fire. But even if the whole Sun were coal, and the oxygen came for free, it would burn out in about $5000$ years. Chemical reactions release only a few electronvolts per molecule, far too little.

In 1854 Hermann von Helmholtz proposed **gravitational contraction**. If the Sun slowly shrinks, its gravitational potential energy turns into heat, as when a falling stone warms the ground. William Thomson, later Lord Kelvin, calculated the consequences. In 1862 he wrote that the Sun had most probably shone on the Earth for less than $100$ million years, and in 1887 he lowered the limit to about $20$ million years.

This was a real conflict. Geologists, who studied how slowly rocks form, and biologists, who followed Darwin's theory of evolution, needed hundreds of millions of years. Kelvin's physics was correct; what he did not know was that a new form of energy existed. In 1903 Pierre Curie and Albert Laborde found that radium gives off heat without any chemical reaction, over its whole decay about $200\,000$ times as much as the same mass of burning coal. Energy was hidden inside atoms.

## Key idea

The answer came in 1920. On 24 August, the astronomer **Arthur Eddington** spoke to the British Association for the Advancement of Science in Cardiff. He used a new measurement by the chemist Francis Aston: a helium atom has less mass than the four hydrogen atoms it could be made of. With today's AME2020 masses:
```latex
\begin{aligned}
4 \cdot m(^{1}\text{H}) &= 4 \cdot 1.007825\ \text{u} \\
&= 4.031300\ \text{u} \\
m(^{4}\text{He}) &= 4.002603\ \text{u}
\end{aligned}
```
About $0.71\ \%$ of the mass disappears, and by $E = \Delta m \cdot c^2$ it must leave as energy. Eddington argued that a star is "drawing on some vast reservoir of energy", which "can scarcely be other than the sub-atomic energy". Turning hydrogen into helium, he showed, would easily keep the Sun shining for billions of years.

<figure class="unit-photo"><img src="units/fy14/pics/aston.jpg" alt="Black-and-white portrait photograph of Francis William Aston, a man with a moustache wearing a suit." width="1164" height="1600" loading="lazy"><figcaption>Francis Aston (1877–1945) built the mass spectrograph and measured that a helium atom is slightly lighter than four hydrogen atoms, the clue to fusion energy. <span class="photo-credit">Photo: Bain News Service, publisher, public domain, via Wikimedia Commons</span></figcaption></figure>

Eddington could not say *how* the protons fuse: by classical physics, the Sun's core was much too cold for them to overcome their electric repulsion. George Gamow explained alpha decay with quantum tunnelling in 1928; in 1929 Robert Atkinson and Fritz Houtermans applied tunnelling to stars, and in 1938–1939 Hans Bethe worked out the reactions. That is the next unit.

## Formula: The lifetime of an energy source

If a source holds the energy $E$ and gives it away at the constant power $L$, it lasts for the time
```latex
t = \frac{E}{L}
```
For hydrogen fusion, the energy is the mass that disappears times $c^2$. If the mass $m_\text{H}$ of hydrogen is fused into helium, the energy released is
```latex
E = 0.0071 \cdot m_\text{H} \cdot c^2
```
For comparison, gravitational contraction can release at most about $GM^2/R$, where $M$ is the mass and $R$ the radius of the Sun, and burning gives the mass times the **heat of combustion** of the fuel. The three estimates are shown below on a logarithmic scale.

<svg data-fig="estimates" viewBox="0 0 600 360" role="img" aria-label="Horizontal bar chart on a logarithmic axis of time in years, from 10 to the power 3 to 10 to the power 11. Chemical burning: about 5000 years. Gravitational contraction: about 31 million years. Hydrogen fusion: about 10 billion years. A dashed vertical line marks the age of the Sun, 4.6 billion years: only the fusion bar reaches past it." style="max-width:100%;font-size:26px">
  <line x1="30" y1="286" x2="570" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M582,286 L569,292 L569,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="30" y1="286" x2="30" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="5.5" y="300.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10^{3}$</div></foreignObject>
  <line x1="30" y1="40" x2="30" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="286" x2="96" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="96" y1="40" x2="96" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="162.5" y1="286" x2="162.5" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="138" y="300.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10^{5}$</div></foreignObject>
  <line x1="162.5" y1="40" x2="162.5" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="229" y1="286" x2="229" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="229" y1="40" x2="229" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="295" y1="286" x2="295" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270.5" y="300.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10^{7}$</div></foreignObject>
  <line x1="295" y1="40" x2="295" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361" y1="286" x2="361" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="361" y1="40" x2="361" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="427.5" y1="286" x2="427.5" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="403" y="300.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10^{9}$</div></foreignObject>
  <line x1="427.5" y1="40" x2="427.5" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="494" y1="286" x2="494" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="494" y1="40" x2="494" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="560" y1="286" x2="560" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="529" y="300.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10^{11}$</div></foreignObject>
  <line x1="560" y1="40" x2="560" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="490" y="248.5" width="66" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$t\ (\text{a})$</span></div></foreignObject>
  <rect x="30" y="38" width="48.5" height="36" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="30" y="110" width="298" height="36" fill="#e8590c" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="30" y="182" width="465" height="36" fill="#1971c2" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="471.5" y1="30" x2="471.5" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="306.5" y="232.5" width="157" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{age of the Sun}$</span></div></foreignObject>
  <foreignObject x="88.5" y="40.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{chemical}$</span></div></foreignObject>
  <foreignObject x="338" y="112.5" width="157" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{contraction}$</span></div></foreignObject>
  <foreignObject x="505" y="184.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{fusion}$</span></div></foreignObject>
</svg>

## Worked example

Estimate how long the Sun can shine by fusing hydrogen into helium. Use these simplifying assumptions: (1) only the hot core, about $10\ \%$ of the Sun's mass, is ever used, and we treat it as pure hydrogen that is all turned into helium; (2) $0.71\ \%$ of the fused mass becomes energy; (3) the Sun shines with today's power all the time. The Sun's mass is $M = 1.99 \cdot 10^{30}\ \text{kg}$ and its luminosity $L = 3.83 \cdot 10^{26}\ \text{W}$.

<!-- vaihe -->

**Given:** $M = 1.99 \cdot 10^{30}\ \text{kg}$, $L = 3.83 \cdot 10^{26}\ \text{W}$, fused fraction of the mass $10\ \% = 0.10$, mass-to-energy fraction $0.0071$, $c = 3.00 \cdot 10^{8}\ \text{m/s}$. **Find:** the time $t$ in years.

<!-- vaihe -->

**Principle:** Mass–energy equivalence gives the energy of the fused hydrogen, $E = \Delta m \cdot c^2$, where $\Delta m$ is $0.71\ \%$ of the fused mass. At a constant power, the time is the energy divided by the power.

<!-- vaihe -->

**Formula:**
```latex
\begin{aligned}
E &= 0.0071 \cdot 0.10 \cdot M \cdot c^2 \\
t &= \frac{E}{L}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** $1\ \text{W} = 1\ \text{J/s}$, so $t$ comes out in seconds. One year is $365.25 \cdot 24 \cdot 3600\ \text{s} = 3.156 \cdot 10^{7}\ \text{s}$.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
E &= 0.0071 \cdot 0.10 \cdot 1.99 \cdot 10^{30}\ \text{kg} \\
&\quad \cdot (3.00 \cdot 10^{8}\ \text{m/s})^2 \\
&= 1.27 \cdot 10^{44}\ \text{J} \\[4pt]
t &= \frac{1.27 \cdot 10^{44}\ \text{J}}{3.83 \cdot 10^{26}\ \text{J/s}} \\
&= 3.32 \cdot 10^{17}\ \text{s} \\
&= \frac{3.32 \cdot 10^{17}\ \text{s}}{3.156 \cdot 10^{7}\ \text{s/a}} \\
&= 1.05 \cdot 10^{10}\ \text{a}
\end{aligned}
```

<!-- vaihe -->

**Answer:** about $10$ billion years ($10^{10}$ years). Only one significant figure is meaningful, because the assumption of $10\ \%$ is itself a rough estimate.

<!-- vaihe -->

**Reasonableness:** The result is far longer than the chemical ($5000$ years) and gravitational (about $30$ million years) estimates, and longer than the age of the Solar System, $4.6$ billion years, so the Sun is roughly in the middle of its life. Computer models of the Sun give a similar total of about $10$ billion years. The assumptions are rough in both directions: the core is not pure hydrogen and the Sun's power slowly grows, while the burning region slowly grows outwards and reaches fresh hydrogen.

## The people behind the idea {People}

### Arthur Eddington (1882–1944)

<figure class="unit-photo"><img src="units/fy14/pics/eddington.jpg" alt="Black-and-white portrait photograph of Arthur Eddington, a man in a suit and tie." width="1164" height="1600" loading="lazy"><figcaption>Arthur Eddington (1882–1944) suggested in 1920 that the Sun gets its energy by turning hydrogen into helium. <span class="photo-credit">Photo: Bain News Service, publisher, public domain, via Wikimedia Commons</span></figcaption></figure>

Arthur Stanley Eddington was an English astronomer, born in Kendal, and from 1913 a professor at the University of Cambridge. In 1919 he led the expedition to the island of Príncipe that measured how the Sun bends starlight during an eclipse, an early test of Einstein's general relativity. In his 1920 address in Cardiff he proposed that stars shine by turning hydrogen into helium, years before anyone could explain how. His book *The Internal Constitution of the Stars* (1926) trained a generation of astrophysicists.

## Common misconception

"The Sun is a ball of fire." Fire is a chemical reaction with oxygen, and it would have burned the Sun out in thousands of years. The Sun's energy comes from nuclear fusion: nuclei change, not molecules.

"The Sun will burn out when all of its hydrogen is used." Only the hydrogen in the core is hot and dense enough to fuse. When the core runs out of hydrogen, in about $5$ billion years, the Sun will change into a red giant, while most of its hydrogen is still left in the outer layers.

"Fusion turns the Sun's hydrogen into energy." Most of the mass stays: hydrogen becomes helium, and only $0.71\ \%$ of the fused mass leaves as energy.

## Summary

- The Sun radiates $L = 3.83 \cdot 10^{26}\ \text{W}$. The lifetime of an energy source is $t = E/L$.
- Chemical burning could power the Sun for only about $5000$ years, and gravitational contraction (Helmholtz 1854, Kelvin) for a few tens of millions of years: both far too short for geology and evolution.
- In 1920 Eddington used Aston's measurement that helium is lighter than four hydrogen atoms: fusing hydrogen into helium releases $0.71\ \%$ of the mass as energy.
- With clearly stated assumptions, hydrogen fusion gives the Sun a lifetime of about $10^{10}$ years; it is now about $4.6 \cdot 10^{9}$ years old.
- How protons can fuse in a core of "only" $15$ million kelvin needed quantum physics: tunnelling.
