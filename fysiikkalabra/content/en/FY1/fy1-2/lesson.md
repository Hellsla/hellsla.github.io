# Quantities, units and the SI system

> **Why** is the distance to the Voyager 2 probe sometimes given in kilometres, sometimes in astronomical units and sometimes in light-hours, even though it is one and the same distance?

<svg data-fig="hero" data-style="house" viewBox="0 0 1200 600" role="img" aria-label="Illustration: in space, the Sun on the left and the Voyager 2 probe on the right, with a dashed line and planets between them. Under the line are three rulers of the same length whose marks are spaced differently: the same distance in three different units." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Quantity, numerical value and unit
Physics describes the world with measurable properties called **quantities**: length, mass, time and speed are quantities. The value of a quantity is measured by comparing it with an agreed measure, a **unit**, and the value is written as the product of a numerical value and a unit, for example the length of a pencil $l = 12.0\,\text{cm}$. A numerical value without a unit tells you nothing: the number 12 could mean centimetres, hours or kilograms. The symbol of a quantity is written in italics ($l$, $m$, $t$) and the unit in upright letters ($\text{m}$, $\text{kg}$, $\text{s}$).

<svg data-fig="quantity" data-style="house" viewBox="0 0 600 322" role="img" aria-label="Diagram: the value of a quantity is a numerical value times a unit. A pencil is measured with a ruler: the tip of the pencil is at the zero mark and the end edge at 12.0 cm, so the value of the length is $l = 12.0\,\text{cm}$. Below, the value is split into parts: $l$ is the quantity, $12.0$ the numerical value and $\text{cm}$ the unit. The ruler and the pencil are drawn to scale, horizontally 1 cm is 40 units." style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-2-quantity.webp" x="0" y="0" width="600" height="332.5" preserveAspectRatio="none"/>
  <foreignObject x="50.2" y="101.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="127.6" y="101.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="205" y="101.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="282.4" y="101.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <foreignObject x="359.8" y="101.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <foreignObject x="437.2" y="101.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="514.6" y="101.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <foreignObject x="148" y="182.5" width="40" height="43" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:36px">$l$</div></foreignObject>
  <foreignObject x="204" y="182.5" width="40" height="43" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:36px">$=$</div></foreignObject>
  <foreignObject x="257" y="182.5" width="110" height="43" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:36px;color:#e8590c">$12.0$</div></foreignObject>
  <foreignObject x="383" y="182.5" width="90" height="43" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:36px;color:#2b8a3e">$\text{cm}$</div></foreignObject>
  <foreignObject x="273" y="137.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{value of the quantity}$</div></foreignObject>
  <foreignObject x="118" y="255.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{quantity}$</div></foreignObject>
  <foreignObject x="252" y="255.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{numerical value}$</div></foreignObject>
  <foreignObject x="373" y="255.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{unit}$</div></foreignObject>
</svg>

```pysahdy
A friend gives the length of a pencil as just the number 12. Why is this not a valid measurement result in physics?
---
A numerical value without a unit tells you nothing: 12 could mean centimetres, hours or kilograms.
```

### The SI system
So that a metre is the same metre everywhere in the world, the scientific community has agreed on a common system of units, the **SI system**. It has seven base quantities, and each has its own base unit. All other quantities are derived from them: speed is length divided by time, so its unit is $\text{m/s}$, and the unit of area is $\text{m}^2$.

| Base quantity | Symbol | SI unit |
|---|---|---|
| length | $l$ | metre $\text{m}$ |
| mass | $m$ | kilogram $\text{kg}$ |
| time | $t$ | second $\text{s}$ |
| electric current | $I$ | ampere $\text{A}$ |
| temperature | $T$ | kelvin $\text{K}$ |
| amount of substance | $n$ | mole $\text{mol}$ |
| luminous intensity | $I_\text{v}$ | candela $\text{cd}$ |

In this course you need the first three most. You will meet the other base quantities in later courses.

<figure class="unit-photo"><img src="pics/fy1/nist-4-kibble-balance.webp" alt="A complex metal apparatus with frames, coils, wires and parts of a vacuum chamber against a dark background."><figcaption>The NIST-4 Kibble balance at the US National Institute of Standards and Technology. Today the kilogram is defined using a constant of nature, the Planck constant, and a balance like this can measure mass according to that definition.</figcaption></figure>

### Prefixes and powers of ten
The metre is good for measuring a room but not an atom or Neptune. That is why a **prefix**, an abbreviation for a power of ten, is attached in front of the unit: $1\,\text{km} = 10^{3}\,\text{m}$ and $1\,\text{mm} = 10^{-3}\,\text{m}$. The most common prefixes go up in steps of a factor of a thousand (exceptions are, for example, centi $10^{-2}$ and deci $10^{-1}$), and large and small numbers are written in scientific notation $a\cdot10^{n}$, where $1 \le a < 10$ and $n$ is an integer. For example, the distance between the Earth and the Sun is $1.5\cdot10^{11}\,\text{m} = 1.5\cdot10^{8}\,\text{km}$.

<svg data-fig="prefixes" data-style="house" viewBox="0 0 600 290" role="img" aria-label="Prefixes are abbreviations for powers of ten. The eight boxes show the factors nano $10^{-9}$, micro $10^{-6}$, milli $10^{-3}$, no prefix $10^{0}$, kilo $10^{3}$, mega $10^{6}$, giga $10^{9}$ and tera $10^{12}$. Between the arrows the factor grows a thousandfold at every step. In the bottom row the prefix is combined with the metre." style="max-width:100%;font-size:24px">
  <rect x="22" y="54" width="52" height="58" rx="8" fill="#d0e6fb" stroke="#727e8a" stroke-width="1.75"/>
  <foreignObject x="24" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\text{n}$</div></foreignObject>
  <foreignObject x="13" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{-9}$</div></foreignObject>
  <foreignObject x="13" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{nano}$</div></foreignObject>
  <foreignObject x="18" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{nm}$</div></foreignObject>
  <line x1="76" y1="83" x2="85" y2="83" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M92,83 L82.5,87 L85,83 L82.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="49" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\cdot 10^{3}$</div></foreignObject>
  <rect x="94" y="54" width="52" height="58" rx="8" fill="#d0e6fb" stroke="#727e8a" stroke-width="1.75"/>
  <foreignObject x="96" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\text{µ}$</div></foreignObject>
  <foreignObject x="85" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{-6}$</div></foreignObject>
  <foreignObject x="85" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{micro}$</div></foreignObject>
  <foreignObject x="90" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{µm}$</div></foreignObject>
  <line x1="148" y1="83" x2="157" y2="83" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M164,83 L154.5,87 L157,83 L154.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="121" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\cdot 10^{3}$</div></foreignObject>
  <rect x="166" y="54" width="52" height="58" rx="8" fill="#d0e6fb" stroke="#727e8a" stroke-width="1.75"/>
  <foreignObject x="168" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\text{m}$</div></foreignObject>
  <foreignObject x="157" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{-3}$</div></foreignObject>
  <foreignObject x="157" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{milli}$</div></foreignObject>
  <foreignObject x="162" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mm}$</div></foreignObject>
  <line x1="220" y1="83" x2="229" y2="83" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M236,83 L226.5,87 L229,83 L226.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="193" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\cdot 10^{3}$</div></foreignObject>
  <rect x="238" y="54" width="52" height="58" rx="8" fill="#ffffff" stroke="#3a4350" stroke-width="1.75"/>
  <foreignObject x="240" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$1$</div></foreignObject>
  <foreignObject x="229" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{0}$</div></foreignObject>
  <foreignObject x="234" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{m}$</div></foreignObject>
  <line x1="292" y1="83" x2="301" y2="83" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M308,83 L298.5,87 L301,83 L298.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="265" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\cdot 10^{3}$</div></foreignObject>
  <rect x="310" y="54" width="52" height="58" rx="8" fill="#ffc078" stroke="#8c6a42" stroke-width="1.75"/>
  <foreignObject x="312" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\text{k}$</div></foreignObject>
  <foreignObject x="301" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{3}$</div></foreignObject>
  <foreignObject x="301" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kilo}$</div></foreignObject>
  <foreignObject x="306" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{km}$</div></foreignObject>
  <line x1="364" y1="83" x2="373" y2="83" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M380,83 L370.5,87 L373,83 L370.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="337" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\cdot 10^{3}$</div></foreignObject>
  <rect x="382" y="54" width="52" height="58" rx="8" fill="#ffc078" stroke="#8c6a42" stroke-width="1.75"/>
  <foreignObject x="384" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\text{M}$</div></foreignObject>
  <foreignObject x="373" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{6}$</div></foreignObject>
  <foreignObject x="373" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mega}$</div></foreignObject>
  <foreignObject x="378" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Mm}$</div></foreignObject>
  <line x1="436" y1="83" x2="445" y2="83" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M452,83 L442.5,87 L445,83 L442.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="409" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\cdot 10^{3}$</div></foreignObject>
  <rect x="454" y="54" width="52" height="58" rx="8" fill="#ffc078" stroke="#8c6a42" stroke-width="1.75"/>
  <foreignObject x="456" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\text{G}$</div></foreignObject>
  <foreignObject x="445" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{9}$</div></foreignObject>
  <foreignObject x="445" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{giga}$</div></foreignObject>
  <foreignObject x="450" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Gm}$</div></foreignObject>
  <line x1="508" y1="83" x2="517" y2="83" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M524,83 L514.5,87 L517,83 L514.5,79 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="481" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\cdot 10^{3}$</div></foreignObject>
  <rect x="526" y="54" width="52" height="58" rx="8" fill="#ffc078" stroke="#8c6a42" stroke-width="1.75"/>
  <foreignObject x="528" y="65" width="48" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\text{T}$</div></foreignObject>
  <foreignObject x="517" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{12}$</div></foreignObject>
  <foreignObject x="517" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tera}$</div></foreignObject>
  <foreignObject x="522" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Tm}$</div></foreignObject>
  <line x1="12" y1="208" x2="588" y2="208" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <foreignObject x="20" y="253.5" width="560" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{one step to the right = a thousand times larger}$</div></foreignObject>
</svg>

When you move to a smaller unit, the numerical value grows: $4.2\,\text{km} = 4.2\cdot10^{3}\,\text{m} = 4200\,\text{m}$. When you move to a larger unit, the numerical value gets smaller. The quantity stays the same, only the way of writing it changes.

```pysahdy
How many millimetres is $2.5\,\text{m}$? Does the numerical value grow or shrink?
---
A millimetre is a smaller unit than a metre ($1\,\text{mm} = 10^{-3}\,\text{m}$), so the numerical value grows: $2.5\,\text{m} = 2500\,\text{mm}$.
```

### A unit for every scale
A unit is chosen so that the numerical value is easy to read. In the chapter *Physics as a science and the scales of the universe* you saw that the structures of matter and of the universe lie on steps of powers of ten. Each step has a convenient unit:

| Structure | Size or distance | Unit | Value of the unit |
|---|---|---|---|
| **Atomic nucleus** | about $10^{-15}\,\text{m}$ | femtometre | $1\,\text{fm} = 10^{-15}\,\text{m}$ |
| **Atom** | about $10^{-10}\,\text{m}$ | nanometre | $1\,\text{nm} = 10^{-9}\,\text{m}$ |
| **Red blood cell** | about $10^{-5}\,\text{m}$ | micrometre | $1\,\mu\text{m} = 10^{-6}\,\text{m}$ |
| **Earth** | about $10^{7}\,\text{m}$ | kilometre | $1\,\text{km} = 10^{3}\,\text{m}$ |
| **Orbits of the planets** | about $10^{12}\,\text{m}$ | astronomical unit | $1\,\text{AU} \approx 1.5\cdot10^{11}\,\text{m}$ |
| **Distances between stars** | about $10^{16}\,\text{m}$ and more | light-year | about $9.46\cdot10^{15}\,\text{m}$ |

For example, the diameter of a hydrogen atom is $0.11\,\text{nm}$ and that of a proton $1.7\,\text{fm}$. A unit does not change the size, only the way of writing it. The astronomical unit and the light-year are not SI units, but they are defined in metres, so you can always convert them to metres.

### Significant figures
The **significant figures** of a numerical value tell how precisely the quantity is known. Starting from the first digit that is not zero, all digits, including the trailing zeros of a decimal number, are significant: $0.0250\,\text{m}$ has three significant figures and $3.0\,\text{m}$ has two. Scientific notation makes the precision visible: $3.00\cdot10^{8}$ has three significant figures and $3\cdot10^{8}$ has one. The trailing zeros of a whole number are unclear: from the Moon's mean distance $384\,400\,\text{km}$ you cannot see whether the precision is a hundred, ten or one kilometre. Show the precision in scientific notation, for example $3.844\cdot10^{5}\,\text{km}$ (four significant figures). In the tasks of this book a value given as a whole number ending in zeros, such as $10\,\text{min}$, is exact unless stated otherwise.

The result of a multiplication or division is given with as many significant figures as the least precise factor has. Rounding is done only at the end, and exact numbers such as the conversion factor $1000$ have no limiting effect. For example, $1.85\,\text{m}\cdot0.92\,\text{m} = 1.702\,\text{m}^2$ is rounded to $1.7\,\text{m}^2$.

## Formula: Unit conversions
When you change a unit, the quantity does not change, only the way of writing it. A conversion is done by replacing the old unit with its value in the new unit. Since $1\,\text{km} = 1000\,\text{m}$, you can write $1000\,\text{m}$ in place of the kilometre:

```latex
4.2\,\text{km} = 4.2\cdot1000\,\text{m} = 4200\,\text{m}
```

In the other direction $1\,\text{m} = 0.001\,\text{km}$, so $350\,\text{m} = 350\cdot0.001\,\text{km} = 0.35\,\text{km}$. Always check the result by reasoning: in a smaller unit the numerical value is greater, because more of the small units are needed. For area, the unit is a product of two lengths, so $$\begin{aligned} 1\,\text{km}^2 &= 1000\,\text{m}\cdot1000\,\text{m} \\ &= 10^{6}\,\text{m}^2 \end{aligned}$$.

In astronomy the kilometre is too small a unit. The **astronomical unit** $\text{AU}$ is an agreed unit of length that is close to the mean distance between the Earth and the Sun: $$\begin{aligned} 1\,\text{AU} &= 149\,597\,870.7\,\text{km} \\ &\approx 1.496\cdot10^{8}\,\text{km} \end{aligned}$$. The light-year is also a unit of length, not of time: it is the distance light travels in a vacuum in a year, about $9.46\cdot10^{12}\,\text{km}$.

```pysahdy
Light from a star takes four years to reach the Earth. How far away is the star in light-years, and is a light-year a unit of time?
---
The star is four light-years away. A light-year is a unit of length: the distance light travels in a vacuum in one year.
```

A distance can also be given as the time light needs to travel it. Light travels in a vacuum at a constant speed $c$, so the distance it covers is speed times time, $s = ct$. The travel time is obtained by solving this formula for time:

```latex
t = \frac{s}{c}
```
where $t$ is the travel time of light, $s$ the distance travelled by light and $$\begin{aligned} c &= 299\,792\,458\,\text{m/s} \\ &\approx 2.998\cdot10^{5}\,\text{km/s} \end{aligned}$$ the speed of light in a vacuum. Light travels one AU in $\tfrac{1.496\cdot10^{8}\,\text{km}}{2.998\cdot10^{5}\,\text{km/s}} = 499\,\text{s}$, which is $8.32\,\text{min}$.

<svg data-fig="conversion" data-style="house" viewBox="0 0 600 372" role="img" aria-label="Diagram, not to scale: the same distance from the Sun to the Earth can be given in three ways. At the top a ray of light travels from the Sun to the Earth. Below, the distance $s$ is $1.496\cdot10^{8}\,\text{km}$, which is one astronomical unit $1\,\text{AU}$ and which light travels in 499 seconds, that is 8.32 minutes. The sizes of the Sun and the Earth and the distance between them are not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-2-conversion.webp" x="6.2" y="12.4" width="594.1" height="375" preserveAspectRatio="none"/>
  <foreignObject x="21" y="207.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Sun}$</div></foreignObject>
  <foreignObject x="495" y="207.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Earth}$</div></foreignObject>
  <foreignObject x="260" y="85.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{light}$</div></foreignObject>
  <foreignObject x="293" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="135" y="267.5" width="330" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s = 1.496\cdot10^{8}\,\text{km}$</div></foreignObject>
  <foreignObject x="230" y="307.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$= 1\,\text{AU}$</div></foreignObject>
  <foreignObject x="35" y="341.5" width="530" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{light travel time } t = 499\,\text{s} = 8.32\,\text{min}$</div></foreignObject>
</svg>

## Worked example
Neptune's mean distance from the Sun is $30.1\,\text{AU}$. How many kilometres is that in scientific notation, and how many hours does light take to travel from the Sun to Neptune? Use the values $1\,\text{AU} = 1.496\cdot10^{8}\,\text{km}$ and $c = 2.998\cdot10^{5}\,\text{km/s}$.

<!-- vaihe -->

**Given and unknown.**

- The distance is $s = 30.1\,\text{AU}$,
- $1\,\text{AU} = 1.496\cdot10^{8}\,\text{km}$ and
- the speed of light is $c = 2.998\cdot10^{5}\,\text{km/s}$.

We want the distance $s$ in kilometres and the travel time $t$ in hours.

<!-- vaihe -->

**Principle.** The distance does not change when the unit changes, so in place of AU we write its value in kilometres. Light travels at a constant speed $c$, so the given formula $s = ct$ gives the travel time.

<!-- vaihe -->

**Rearranged formula.**
```latex
t = \frac{s}{c}
```

<!-- vaihe -->

**Unit conversions.** The distance is converted to kilometres by writing $1.496\cdot10^{8}\,\text{km}$ in place of $\text{AU}$: $$\begin{aligned} &s \\ &= 30.1\,\text{AU} \\ &= 30.1\cdot1.496\cdot10^{8}\,\text{km} \\ &= 4.503\cdot10^{9}\,\text{km} \end{aligned}$$.
The travel time comes out in seconds, because $\text{km}$ cancels. The time is asked in hours, so the seconds are converted to hours: $1\,\text{h} = 3600\,\text{s}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
t &= \frac{s}{c} \\
&= \frac{4.503\cdot10^{9}\,\text{km}}{2.998\cdot10^{5}\,\text{km/s}} \\
&= 1.502\cdot10^{4}\,\text{s} \\
&= (1.502\cdot10^{4} : 3600)\,\text{h} = 4.17\,\text{h}
\end{aligned}
```

<!-- vaihe -->

**Result.** The distance is $4.50\cdot10^{9}\,\text{km}$ and the travel time of light is $4.17\,\text{h}$, to three significant figures like the initial value $30.1\,\text{AU}$.

<!-- vaihe -->

**Reasonableness.** Light travels one AU in $8.3\,\text{min}$, so $30\,\text{AU}$ takes light about $30\cdot 8.3\,\text{min} \approx 250\,\text{min} \approx 4.2\,\text{h}$. This agrees with the result, and the distance is of the order of billions of kilometres, as suits an outer planet.

## Common misconception
The numerical value and the unit belong together. When the unit changes, the numerical value changes inversely: a larger unit means a smaller numerical value, and the quantity itself stays the same.

Square units are easy to forget. One square kilometre is not a thousand but a million square metres, because $(10^{3})^2 = 10^{6}$.

The light-year is not a unit of time, even though the name contains the word year. It is a unit of length, about $9.46\cdot10^{12}\,\text{km}$.

## Summary
- The value of a quantity is a numerical value times a unit: $l = 12.0\,\text{cm}$. Without a unit the number tells you nothing.
- In the SI system the base units are, for example, the metre, the kilogram and the second, and the other units are derived from them.
- A prefix is a power of ten: kilo $10^{3}$, mega $10^{6}$, giga $10^{9}$, milli $10^{-3}$, micro $10^{-6}$.
- In a unit conversion, the old unit is replaced by its value in the new unit, for example $4.2\,\text{km} = 4.2\cdot1000\,\text{m}$. For a square unit the conversion is done twice: $1\,\text{km}^2 = 10^{6}\,\text{m}^2$.
- The result of a multiplication or division is given with as many significant figures as the least precise factor has.
- The travel time of light is $t = \tfrac{s}{c}$. Light travels one AU in about $8.3\,\text{min}$.
