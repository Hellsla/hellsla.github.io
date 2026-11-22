# The gravitational force between bodies

> **Why** does a dropped apple rush towards the Earth, while the Earth does not seem to move towards the apple at all?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an apple tree in a meadow on a summer evening at dusk. One apple has come loose from a branch and is halfway to the ground; motion lines trail behind it. In the sky, to the right of the tree, a full moon is shining." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
In the 17th century Isaac Newton concluded that the same interaction that makes an apple fall also keeps the Moon in its orbit. This interaction is called **gravitation**: every body that has mass attracts every other body. You and your desk attract each other, and so do two students sitting side by side. In everyday life we do not notice this, because the force is very small unless one of the bodies is enormous. The gravitational force between two people of $70\,\text{kg}$ and $60\,\text{kg}$ one metre apart is only about $0.28\,\mu\text{N}$. The pull of the Earth on the same person is almost $700\,\text{N}$.

Gravitation is an interaction, so Newton's third law applies to it. The Earth pulls the apple with a force $\overline{F}_1$, and the apple pulls the Earth with a force $\overline{F}_2$ of equal magnitude and opposite direction. The larger body does not pull the smaller one harder than the smaller pulls the larger: the forces are always equal, $F_1 = F_2$.

<svg data-fig="vuorovaikutus" viewBox="0 0 600 360" role="img" aria-label="Diagram, not to scale: on the left the Earth, on the right an apple. The Earth pulls the apple with a force F1 that points from the apple towards the Earth, and the apple pulls the Earth with a force F2 of equal magnitude that points from the centre of the Earth towards the apple. The arrows are equally long. The acceleration of the apple is 9.8 metres per second squared, the acceleration of the Earth about 3 times 10 to the power minus 25 metres per second squared." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-vuorovaikutus.webp" x="2.5" y="0" width="597" height="365.7" preserveAspectRatio="none"/>
  <foreignObject x="187.5" y="125.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <foreignObject x="417.5" y="125.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <foreignObject x="47" y="315.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{Earth: } a \approx 3 \cdot 10^{-25}\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="465" y="205.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{apple}$</div></foreignObject>
  <foreignObject x="433.5" y="315.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$a = 9.8\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="265" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F_1 = F_2$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/artemis2-earthset.webp" alt="The cratered surface of the Moon at the bottom of the picture, with the blue Earth setting behind it against black space."><figcaption>The Earth sets behind the Moon's horizon. The Artemis II crew took the photo from the Orion spacecraft in April 2026 as it flew past the Moon. The Earth and the Moon pull each other with gravitational forces of equal size.</figcaption></figure>

The difference is in the accelerations. By Newton's second law the acceleration of a body is $a = \tfrac{F}{m}$. When a force of about $1.96\,\text{N}$ acts on an apple of $0.20\,\text{kg}$, the acceleration of the apple is about $9.8\,\text{m/s}^2$. The same force gives the Earth, whose mass is $5.97 \cdot 10^{24}\,\text{kg}$, an acceleration of about $3 \cdot 10^{-25}\,\text{m/s}^2$. The Earth really does move towards the apple, but so little that it cannot be measured.

```pysahdy
The Earth and the Moon attract each other with equal gravitational forces. Which one accelerates more?
---
The Moon. The acceleration is $a = \tfrac{F}{m}$, and with the same force the body with the smaller mass, the Moon, accelerates more than the Earth.
```

## Formula: Newton's law of gravitation
The gravitational force between two bodies is greater the greater the masses of the bodies, and smaller the farther apart they are. Newton's law of gravitation says that the force is directly proportional to each mass and inversely proportional to the square of the distance (an inverse-square law):

```kaavat
Newton's law of gravitation :: F = \gamma \frac{m_1 m_2}{r^2}
```

where $F$ is the magnitude of the gravitational force acting on each body (N), $m_1$ and $m_2$ are the masses of the bodies (kg), $r$ is the distance between the centres of the bodies (m) and $\gamma$ is the gravitational constant, $\gamma = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$. (Many English books write the gravitational constant as *G*; in this book *G* is the weight of a body, so the constant is written *γ*.) The force acts on each body towards the other body. In 1798 Henry Cavendish determined the mean density of the Earth by measuring the weak gravitational interaction between lead spheres. The value of the gravitational constant can be derived from his result.

<svg data-fig="kaava" viewBox="0 0 600 300" role="img" aria-label="Diagram: two spheres, a larger mass m1 on the left and a smaller mass m2 on the right. The distance r between the centres of the spheres is marked with a dimension line below the spheres. An equal gravitational force acts on each sphere towards the other sphere: F1 from the left sphere towards the right and F2 from the right sphere towards the left." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-kaava.webp" x="14.6" y="11" width="585.4" height="304.9" preserveAspectRatio="none"/>
  <foreignObject x="133.5" y="21.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="453.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <foreignObject x="221.5" y="85.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <foreignObject x="353.5" y="85.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <foreignObject x="290" y="253.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
</svg>

The law holds as such for point masses. It also holds for uniform spheres and other spherically symmetric bodies, such as planets and stars, when $r$ is measured between the centres: such a body attracts outside bodies as if its whole mass were at its centre. The distance of a person standing on the Earth's surface from the Earth's centre is therefore the radius of the Earth.

```pysahdy
A person stands on the Earth's surface. Which distance $r$ goes into the law of gravitation when the force between the Earth and the person is calculated?
---
The distance from the Earth's centre, that is the radius of the Earth, about $6378\,\text{km}$. The distance from the surface is wrong, because $r$ is measured between the centres.
```

The distance is squared in the formula. When the distance doubles, the force falls to a quarter, and when the distance triples, to a ninth. When one mass doubles, the force doubles too. The gravitational force decreases quickly as the distance grows, but it never becomes exactly zero. The graph shows the force when the mass of each body is $10\,\text{t}$.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Graph, to scale: on the horizontal axis the distance r between the centres of the bodies in metres from zero to ten, on the vertical axis the gravitational force F in micronewtons from zero to 1800, when the mass of each body is 10 tonnes. The points of the falling curve are r = 2 m, F = 1670 µN; r = 4 m, F = 417 µN; r = 6 m, F = 185 µN; r = 8 m, F = 104 µN and r = 10 m, F = 66.7 µN. Dashed lines show that when the distance doubles from two to four metres, the force falls to a quarter." style="max-width:100%;font-size:24px">
  <line x1="173" y1="306" x2="173" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="249.5" y1="306" x2="249.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326.5" y1="306" x2="326.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="403" y1="306" x2="403" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="306" x2="480" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="228" x2="480" y2="228" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="150" x2="480" y2="150" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="72" x2="480" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="306" x2="494" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,306 L493,312 L493,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="307" x2="96" y2="58" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,46 L102,59 L90,59 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="173" y1="306" x2="173" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="163" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="249.5" y1="306" x2="249.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="239.5" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="326.5" y1="306" x2="326.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="316.5" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="403" y1="306" x2="403" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="393" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="480" y1="306" x2="480" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="463.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="228" x2="96" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="213.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="89" y1="150" x2="96" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="135.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1200$</div></foreignObject>
  <line x1="89" y1="72" x2="96" y2="72" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="57.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1800$</div></foreignObject>
  <foreignObject x="66" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="291.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{m})$</div></foreignObject>
  <foreignObject x="86" y="15.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\mu\text{N})$</div></foreignObject>
  <polyline points="173,89 175.5,103 178,115.5 180.5,126.5 183,137 185.5,146.5 188,155.5 190.5,163.5 193.5,171 196,177.5 198.5,184 201,190 203.5,195.5 206,200.5 208.5,205 211,209.5 214,213.5 216.5,217.5 219,221.5 221.5,224.5 224,228 226.5,231 229,234 231.5,236.5 234,239 237,241.5 239.5,244 242,246 244.5,248 247,250 249.5,252 252,253.5 254.5,255 257.5,257 260,258.5 262.5,260 265,261 267.5,262.5 270,264 272.5,265 275,266 278,267.5 280.5,268.5 283,269.5 285.5,270.5 288,271.5 290.5,272 293,273 295.5,274 298,274.5 301,275.5 303.5,276 306,277 308.5,277.5 311,278.5 313.5,279 316,279.5 318.5,280 321.5,281 324,281.5 326.5,282 329,282.5 331.5,283 334,283.5 336.5,284 339,284.5 342,285 344.5,285.5 347,285.5 349.5,286 352,286.5 354.5,287 357,287 359.5,287.5 362,288 365,288.5 367.5,288.5 370,289 372.5,289.5 375,289.5 377.5,290 380,290 382.5,290.5 385.5,290.5 388,291 390.5,291 393,291.5 395.5,291.5 398,292 400.5,292 403,292.5 406,292.5 408.5,293 411,293 413.5,293.5 416,293.5 418.5,293.5 421,294 423.5,294 426,294.5 429,294.5 431.5,294.5 434,295 436.5,295 439,295 441.5,295.5 444,295.5 446.5,295.5 449.5,295.5 452,296 454.5,296 457,296 459.5,296.5 462,296.5 464.5,296.5 467,296.5 470,297 472.5,297 475,297 477.5,297 480,297.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="173" y1="89" x2="173" y2="306" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="89" x2="173" y2="89" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="249.5" y1="252" x2="249.5" y2="306" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="252" x2="249.5" y2="252" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="173" cy="89" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="249.5" cy="252" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="326.5" cy="282" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="403" cy="292.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="480" cy="297.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="187" y="76.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="261.5" y="211.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\tfrac{F}{4}$</div></foreignObject>
  <foreignObject x="306" y="77.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$m_1 = m_2 = 10\,\text{t}$</span></div></foreignObject>
  <foreignObject x="325" y="115.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$2r \;\Rightarrow\; \tfrac{1}{4}F$</span></div></foreignObject>
</svg>

```pysahdy
According to the graph the force is $417\,\mu\text{N}$ when the distance is $4\,\text{m}$. What is it when the distance is $8\,\text{m}$?
---
The distance doubles, so the force falls to a quarter: $417\,\mu\text{N} : 4 \approx 104\,\mu\text{N}$. The graph shows the same value.
```

## Weight and the gravitational field {Painovoima ja gravitaatiokenttä}
The weight $G = mg$ of a body is the gravitational force the Earth exerts on it. When the mass of the Earth is $M$ and its radius $R$, the law of gravitation gives the same force, so $mg = \gamma \tfrac{Mm}{R^2}$. The mass $m$ of the body cancels, and the acceleration due to gravity is left as $g = \gamma \tfrac{M}{R^2}$. This is why all bodies fall with the same acceleration on the Earth's surface when air resistance is ignored: a greater force acts on a heavier body, but it is also harder to accelerate.

### Gravitational field strength
**Extension section.** Gravitational field strength is not part of the central content of this course, so this subsection and the next one, *The field on different celestial bodies*, are extension material. The core path needs only Newton's law of gravitation and the fact that the weight of a body is the gravitational force acting on it at the Earth's surface.

The Earth changes its surroundings so that at every point a certain pull is ready: a force $\overline{F} = m\overline{g}$ acts on a body brought there. This is called the **gravitational field** of the Earth. The field strength at a distance $r$ from the centre of a body is

```latex
g = \gamma \frac{M}{r^2}
```

where $M$ is the mass of the body that creates the field (kg) and $r$ is the distance from its centre (m). The direction of the field is towards the centre of the body, and the unit of the field strength is $\text{m/s}^2$. If only gravitation acts on a body, its acceleration by Newton's second law is $a = \tfrac{F}{m} = \tfrac{mg}{m} = g$. The gravitational field strength is therefore the same thing as the acceleration of a freely falling body at that point.

<svg data-fig="kentta" viewBox="0 0 600 380" role="img" aria-label="Diagram, not to scale: the Earth in the centre. At a distance of two Earth radii from the centre a circle is drawn with a dashed line; from seven points of the circle an orange arrow g of equal length points towards the centre of the Earth. At the right edge of the circle there is a small body on which a red force F = mg acts towards the centre of the Earth." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-kentta.webp" x="1.2" y="1.2" width="597" height="384.3" preserveAspectRatio="none"/>
  <foreignObject x="374.5" y="61" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{g}$</div></foreignObject>
  <foreignObject x="426" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="376" y="225.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F} = m\overline{g}$</div></foreignObject>
  <foreignObject x="221" y="9.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r = 2R$</div></foreignObject>
</svg>

### The field on different celestial bodies
The field strengths in the table have been calculated from the formula $g = \gamma \tfrac{M}{R^2}$ using the masses and equatorial radii from NASA's Planetary Fact Sheet. The value $9.80\,\text{m/s}^2$ for the Earth is calculated without the effect of the Earth's rotation; the measured value is slightly different, and the tasks of this book use the value $9.81\,\text{m/s}^2$. The mass of a body is the same everywhere, but its weight depends on the field of which celestial body it is in.

| Body | mass $M$ (kg) | radius $R$ (km) | $g$ ($\text{m/s}^2$) |
|---|---|---|---|
| Moon | $7.35 \cdot 10^{22}$ | $1738$ | $1.62$ |
| Mars | $6.42 \cdot 10^{23}$ | $3396$ | $3.71$ |
| Earth | $5.97 \cdot 10^{24}$ | $6378$ | $9.80$ |
| Jupiter | $1.90 \cdot 10^{27}$ | $71\,492$ | $24.8$ |
| Sun | $1.99 \cdot 10^{30}$ | $695\,700$ | $274$ |

<svg data-fig="planeetat" viewBox="0 0 600 360" role="img" aria-label="Picture, arrow lengths to scale: four surfaces side by side, the Moon, Mars, the Earth and Jupiter. Above each surface there is a small sphere and below it an orange arrow whose length is the gravitational field strength, that is, the acceleration due to gravity on the surface: Moon 1.62, Mars 3.71, Earth 9.80 and Jupiter 24.8 metres per second squared." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-planeetat.webp" x="1.2" y="-2.5" width="597" height="366.9" preserveAspectRatio="none"/>
  <foreignObject x="55" y="311.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Moon}$</div></foreignObject>
  <foreignObject x="24" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$1.62\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="199" y="311.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Mars}$</div></foreignObject>
  <foreignObject x="168" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$3.71\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="337" y="311.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Earth}$</div></foreignObject>
  <foreignObject x="312" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$9.80\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="468.5" y="311.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Jupiter}$</div></foreignObject>
  <foreignObject x="456" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$24.8\,\text{m/s}^2$</div></foreignObject>
  <foreignObject x="530" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{g}$</div></foreignObject>
</svg>

The acceleration due to gravity measured on the Earth's surface varies between $9.78\text{–}9.83\,\text{m/s}^2$, because the Earth rotates and is slightly flattened. In this book the value $g = 9.81\,\text{m/s}^2$ is used when the acceleration due to gravity on the Earth's surface is needed.

## Gravitation in the universe {Gravitaatio maailmankaikkeudessa}
Gravitation is the weakest of the fundamental interactions, but on large scales it is decisive. Electric forces are much stronger, but positive and negative charges cancel each other's effects, so large bodies are nearly electrically neutral. Gravitation, on the other hand, is always attractive: every mass adds to the pull, and nothing cancels it. In addition, the effect of gravitation reaches far, because $\tfrac{1}{r^2}$ becomes smaller but never becomes zero.

<svg data-fig="rakenteet" viewBox="0 0 600 330" role="img" aria-label="Diagram in three stages from left to right, not to scale. First an almost uniform cloud of gas and dust with a slightly denser place. Then the denser places have grown, and arrows show the surrounding matter flowing towards them. Finally a star has formed in the densest place, with a flat disc and small planets orbiting it. Arrows between the stages show the passing of time." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-5-rakenteet.webp" x="0" y="1.2" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="46" y="275.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas cloud}$</div></foreignObject>
  <foreignObject x="215" y="275.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{condensations}$</div></foreignObject>
  <foreignObject x="471" y="275.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{star}$</div></foreignObject>
</svg>

The early universe was an almost uniform cloud of gas. Places where there was slightly more matter than average pulled the surrounding matter harder, so they became denser still. The condensations grew into gas clouds whose central parts collapsed under their own weight. As it collapsed, the gas became denser and hotter, until nuclear reactions started in its centre and a star was born. The matter left in the flat disc around the star gathered into planets. Gravitation also gathers stars into galaxies and galaxies into clusters of galaxies, and it keeps the planets in their orbits around their star.

## Worked example
With what force do the Earth and the Moon attract each other? The mass of the Earth is $5.97 \cdot 10^{24}\,\text{kg}$, the mass of the Moon $7.35 \cdot 10^{22}\,\text{kg}$ and the mean distance between their centres $3.84 \cdot 10^{5}\,\text{km}$.

<!-- vaihe -->

**Given and find.** Mass of the Earth $M = 5.97 \cdot 10^{24}\,\text{kg}$, mass of the Moon $m = 7.35 \cdot 10^{22}\,\text{kg}$, distance $r = 3.84 \cdot 10^{5}\,\text{km}$ and gravitational constant $\gamma = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$. We want the magnitude $F$ of the gravitational force.

<!-- vaihe -->

**Principle.** The Earth and the Moon are almost spherically symmetric, so the force between them can be calculated with Newton's law of gravitation when $r$ is the distance between the centres. By Newton's third law the same force acts on both the Moon and the Earth.

<!-- vaihe -->

**Formula solved.** The asked force is already solved for:

```latex
F = \gamma \frac{M m}{r^2}
```

<!-- vaihe -->

**Unit conversions.** The distance is converted to metres: $r = 3.84 \cdot 10^{5}\,\text{km} = 3.84 \cdot 10^{5} \cdot 10^{3}\,\text{m} = 3.84 \cdot 10^{8}\,\text{m}$. The masses are already in kilograms.

<!-- vaihe -->

**Substitution.** Substitute the values with their units:

```latex
\begin{aligned}
&F = \gamma \frac{M m}{r^2} \\
&= 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\
&\quad \cdot \frac{5.97 \cdot 10^{24}\,\text{kg} \cdot 7.35 \cdot 10^{22}\,\text{kg}}{(3.84 \cdot 10^{8}\,\text{m})^2} \\
&\approx 1.99 \cdot 10^{20}\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The Earth and the Moon attract each other with a force $F \approx 1.99 \cdot 10^{20}\,\text{N}$. The answer is given to three significant figures, because the masses and the distance are given to three figures.

<!-- vaihe -->

**Reasonableness.** With rounded numbers $7 \cdot 10^{-11} \cdot \tfrac{6 \cdot 10^{24} \cdot 7 \cdot 10^{22}}{(4 \cdot 10^{8})^2}\,\text{N} \approx 1.8 \cdot 10^{20}\,\text{N}$, so the order of magnitude is right. The force is enormous, but the acceleration of the Moon is still only $a = \tfrac{F}{m} \approx 2.7 \cdot 10^{-3}\,\text{m/s}^2$, because the mass of the Moon is large.

## Common misconception
"The Earth pulls the Moon harder than the Moon pulls the Earth, because the Earth is much bigger." Gravitation is an interaction, so by Newton's third law the forces are always equal and opposite. The difference in mass shows in the accelerations: the same force accelerates the lighter body more. Another common belief is that gravitation ends above the atmosphere. In fact it only weakens as the distance grows: for example, at a height of $300\,\text{km}$ the field strength is still about $8.9\,\text{m/s}^2$.

## Summary
- All bodies attract each other with the gravitational force $F = \gamma \tfrac{m_1 m_2}{r^2}$, where $r$ is the distance between the centres and $\gamma = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$.
- The gravitational forces between two bodies are equal and opposite; the lighter body accelerates more.
- When the distance doubles, the force falls to a quarter.
- The weight of a body at the Earth's surface is the gravitational force acting on it, $G = mg$.
- Extension: the gravitational field strength $g = \gamma \tfrac{M}{r^2}$ is the acceleration of a freely falling body, with the unit $\text{m/s}^2$.
- Gravitation is always attractive and reaches far, so it gathers matter into stars, planets and galaxies.
