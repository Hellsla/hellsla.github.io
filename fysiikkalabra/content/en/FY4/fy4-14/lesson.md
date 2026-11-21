# Air resistance and falling through air

> **Why** does a skydiver's speed stop increasing, even though the weight pulls the skydiver down throughout the whole fall?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: high above fields, forests and a lake, two skydivers. At the upper left a skydiver falls belly down with arms and legs spread, and lines of the airflow are seen above. At the lower right another skydiver floats slowly under an open parachute. At the top edge of the sky is the aeroplane they jumped from." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-14-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Air resists motion
When an object moves through air or water, it has to push the medium out of its way. The medium pushes back on the object: the object experiences **resistance of the medium**, in air **air resistance** (also called **drag**), which this book writes as $\overline{F}_\text{v}$. It points against the velocity of the object when the air is still. In the chapter *Weight, friction and the inclined plane*, friction resisted sliding along a surface. Air resistance is a similar resistive force, but it is caused by the surrounding air, and the object does not need to touch any solid surface. A bicycle and a car also have **rolling resistance** $\overline{F}_\text{r}$, the resistance caused by the tyres and the road, which is a different force from air resistance.

<figure class="unit-photo"><img src="pics/fy4/epic-parachute-test.webp" alt="A white round parachute in a blue sky, with a small metal test body hanging at the end of a long line."><figcaption>NASA's EPIC test in California in June 2025: a drone dropped a parachute fitted with instruments and its payload. There is no person in the photo, only a test body.</figcaption></figure>

Air resistance differs from sliding friction in that it depends on speed. Air resistance does not act at all on an object that is at rest relative to the air, and it grows quickly when the speed of the object relative to the air grows. At the same speed, air resistance is greater the larger the cross-sectional area of the object and the worse the air can flow past it. At the same speed, the resistance in water is much greater than in air, because water is denser.

```pysahdy
The skydiver leaves the plane at rest relative to the air, even though there is air all around. Why is there no air resistance right after the jump?
---
Air resistance depends on the speed relative to the air, and right after the jump that speed is zero. Only as the speed grows does the air start to resist the motion.
```

### The three stages of a fall
The skydiver starts from rest relative to the air (the speed of the plane is ignored), so right after the jump there is no air resistance yet. The only force is the weight, and the skydiver accelerates downward with the free-fall acceleration $g$. As the speed grows, air resistance grows. The weight stays the same, so the net force becomes smaller, and the acceleration becomes smaller with it: the speed grows more and more slowly. Finally the air resistance is equal to the weight. Then the net force is zero, the acceleration is zero and the speed stays constant, as Newton's first law says. This speed is called the **terminal velocity**.

<svg data-fig="pudotus" viewBox="0 0 600 450" role="img" aria-label="Three stages of a skydiver&#x27;s fall belly down, to scale. At the top are situation pictures and at the bottom free-body diagrams in which the skydiver is a rectangle. On the left, right after the jump: the skydiver starts from rest relative to the air, the speed is zero, the free-body diagram has only the weight G from the centre down, and the orange acceleration arrow points down. In the middle the skydiver accelerates: a blue velocity arrow down, the weight G down and the air resistance F_v from the bottom up to the bottom surface, half the length of the weight, and the acceleration arrow is shorter. On the right terminal velocity: a long velocity arrow down, the air resistance as long as the weight, and the acceleration is zero." style="max-width:100%;font-size:30px">
  <image href="pics/fy4/fy4-14-pudotus.webp" x="0" y="0" width="600" height="457.5" preserveAspectRatio="none"/>
  <foreignObject x="33.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{at the start}$</div></foreignObject>
  <foreignObject x="72.5" y="130" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$v = 0$</div></foreignObject>
  <foreignObject x="94.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="148.5" y="308" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="65" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} = 0$</div></foreignObject>
  <foreignObject x="221" y="7.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{accelerating}$</div></foreignObject>
  <foreignObject x="368" y="75" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="294.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="218.5" y="310" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="348.5" y="288" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="265" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} < G$</div></foreignObject>
  <foreignObject x="396" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{terminal velocity}$</div></foreignObject>
  <foreignObject x="568" y="92" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="494.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="418.5" y="357" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="522.5" y="196" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="465" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} = G$</div></foreignObject>
</svg>

```pysahdy
A skydiver falls at terminal velocity. Why does the speed no longer change, even though the weight still pulls down?
---
Air resistance equals the weight, so the net force and the acceleration are zero. The speed stays constant.
```

### Terminal velocity depends on mass and shape
At terminal velocity, air resistance is equal to the weight. A heavier skydiver has a greater weight, so the speed has time to grow greater before air resistance has grown to the size of the weight. In the graph, the curves of a $60\,\text{kg}$ and a $100\,\text{kg}$ skydiver falling in the same position start equally steep, but they level off at different speeds, in the values of the model at about $48\,\text{m/s}$ and $61\,\text{m/s}$. A skydiver diving head first has a smaller cross-sectional area and a more streamlined shape, so the terminal velocity is greater.

<svg data-fig="vt" viewBox="0 0 600 360" role="img" aria-label="Graph to scale, values of the simulation model: on the horizontal axis time 0 to 30 seconds, on the vertical axis speed 0 to 70 metres per second. A dashed straight line rises steeply: the speed without air resistance, 49 metres per second at five seconds. Two curves start with the same steepness but flatten and level off horizontally: the speed of the 60 kilogram skydiver at about 48 metres per second and of the 100 kilogram skydiver at about 61 metres per second." style="max-width:100%;font-size:24px">
  <line x1="146.5" y1="304" x2="146.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="203.5" y1="304" x2="203.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="304" x2="260" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="316.5" y1="304" x2="316.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="373.5" y1="304" x2="373.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="304" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="270" x2="430" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="236" x2="430" y2="236" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="202" x2="430" y2="202" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="168" x2="430" y2="168" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="134" x2="430" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="100" x2="430" y2="100" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="66" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="304" x2="444" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,304 L443,310 L443,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="305" x2="90" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,40 L96,53 L84,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="146.5" y1="304" x2="146.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="136.5" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="203.5" y1="304" x2="203.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="187" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="260" y1="304" x2="260" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="243.5" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="316.5" y1="304" x2="316.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="373.5" y1="304" x2="373.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="430" y1="304" x2="430" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="413.5" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="83" y1="270" x2="90" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="83" y1="236" x2="90" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="83" y1="202" x2="90" y2="202" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="187.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="83" y1="168" x2="90" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="153.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="83" y1="134" x2="90" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="83" y1="100" x2="90" y2="100" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="83" y1="66" x2="90" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="51.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$70$</div></foreignObject>
  <foreignObject x="60" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="289.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="80" y="9.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <polyline points="90,304 171,66" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="181" y="58.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{without air resistance}$</div></foreignObject>
  <polyline points="90,304 93,295.5 95.5,287.5 98.5,279 101.5,271 104,263 107,255 110,247 112.5,239.5 115.5,232 118.5,225 121,218 124,211 127,204.5 129.5,198 132.5,192 135.5,186 138,180.5 141,175.5 144,170.5 146.5,165.5 149.5,161 152.5,156.5 155,152.5 158,148.5 161,145 163.5,141.5 166.5,138.5 169.5,135.5 172,132.5 175,130 178,127.5 180.5,125.5 183.5,123 186.5,121 189,119 192,117.5 195,116 197.5,114.5 200.5,113 203.5,111.5 206,110.5 209,109.5 212,108 214.5,107 217.5,106.5 220.5,105.5 223,104.5 226,104 229,103.5 231.5,102.5 234.5,102 237.5,101.5 240,101 243,100.5 246,100.5 248.5,100 251.5,99.5 254.5,99 257,99 260,98.5 263,98.5 265.5,98 268.5,98 271.5,97.5 274,97.5 277,97.5 280,97 282.5,97 285.5,97 288.5,96.5 291,96.5 294,96.5 297,96.5 299.5,96.5 302.5,96 305.5,96 308,96 311,96 314,96 316.5,96 319.5,96 322.5,96 325,95.5 328,95.5 331,95.5 333.5,95.5 336.5,95.5 339.5,95.5 342,95.5 345,95.5 348,95.5 350.5,95.5 353.5,95.5 356.5,95.5 359,95.5 362,95.5 365,95.5 367.5,95.5 370.5,95.5 373.5,95.5 376,95.5 379,95.5 382,95.5 384.5,95.5 387.5,95 390.5,95 393,95 396,95 399,95 401.5,95 404.5,95 407.5,95 410,95 413,95 416,95 418.5,95 421.5,95 424.5,95 427,95 430,95" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="442" y="80.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 100\,\text{kg}$</div></foreignObject>
  <polyline points="90,304 93,295.5 95.5,287.5 98.5,279 101.5,271 104,263 107,255.5 110,248 112.5,241 115.5,234 118.5,227.5 121,221 124,215 127,209.5 129.5,204 132.5,199 135.5,194.5 138,190 141,186 144,182 146.5,178.5 149.5,175.5 152.5,172.5 155,170 158,167.5 161,165 163.5,163 166.5,161 169.5,159.5 172,157.5 175,156.5 178,155 180.5,153.5 183.5,152.5 186.5,151.5 189,151 192,150 195,149 197.5,148.5 200.5,148 203.5,147.5 206,147 209,146.5 212,146 214.5,145.5 217.5,145.5 220.5,145 223,145 226,144.5 229,144.5 231.5,144 234.5,144 237.5,143.5 240,143.5 243,143.5 246,143.5 248.5,143 251.5,143 254.5,143 257,143 260,143 263,143 265.5,143 268.5,142.5 271.5,142.5 274,142.5 277,142.5 280,142.5 282.5,142.5 285.5,142.5 288.5,142.5 291,142.5 294,142.5 297,142.5 299.5,142.5 302.5,142.5 305.5,142.5 308,142.5 311,142.5 314,142.5 316.5,142.5 319.5,142.5 322.5,142.5 325,142.5 328,142.5 331,142.5 333.5,142.5 336.5,142.5 339.5,142.5 342,142.5 345,142.5 348,142.5 350.5,142.5 353.5,142.5 356.5,142 359,142 362,142 365,142 367.5,142 370.5,142 373.5,142 376,142 379,142 382,142 384.5,142 387.5,142 390.5,142 393,142 396,142 399,142 401.5,142 404.5,142 407.5,142 410,142 413,142 416,142 418.5,142 421.5,142 424.5,142 427,142 430,142" fill="none" stroke="#b8622d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="442" y="127.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d">$m = 60\,\text{kg}$</div></foreignObject>
</svg>

This gives the answer to the question at the start. The weight pulls the skydiver down all the time, but as the speed grows, air resistance grows until it cancels the weight. After that the speed no longer changes. Without air resistance, all objects would fall with the same acceleration $g$. In air, a light and wide object, such as a sheet of paper or a feather, reaches a small terminal velocity very soon and therefore falls slowly.

```pysahdy
Why does a sheet of paper fall more slowly in air than a crumpled paper ball of the same weight?
---
At the same speed the wide sheet gets a greater air resistance, so air resistance grows to equal its weight already at a small speed. The sheet's terminal velocity is therefore smaller.
```

## Formula: Equation of motion with air resistance
Air resistance is one of the forces acting on an object, so the motion follows Newton's second law. An object falling or rising through air is acted on by its weight and by air resistance:
```latex
\overline{G} + \overline{F}_\text{v} = m\overline{a}
```
where $\overline{G}$ is the weight of the object ($\text{N}$), $\overline{F}_\text{v}$ is the air resistance ($\text{N}$), $m$ is the mass of the object ($\text{kg}$) and $\overline{a}$ is its acceleration ($\text{m/s}^2$). In this chapter the magnitude of air resistance is not calculated from the speed, but it is given or deduced from the motion: at terminal velocity $F_\text{v} = G$.

### A falling and a rising object
As always, first choose the object, draw its free-body diagram and choose the positive direction, and only then write the equation. The air resistance of a falling object points up, against the weight. When the positive direction is down, $mg - F_\text{v} = ma$, so the acceleration is smaller than $g$. The air resistance of a ball thrown upward points down, in the same direction as the weight. When the positive direction is up, $-mg - F_\text{v} = ma$. The magnitude of the acceleration is then greater than $g$, and the rising ball slows down faster than without air resistance.

<svg data-fig="ylos" viewBox="0 0 600 430" role="img" aria-label="Two situations, to scale: a ball thrown straight up, when air resistance is not ignored. At the top are situation pictures and at the bottom free-body diagrams in which the ball is a rectangle. On the left the ball rises: a blue velocity arrow up. In the free-body diagram the weight G from the centre down and the air resistance F_v from the top surface down. Separately a green hollow net force arrow down, longer than the weight, and an orange acceleration arrow down. On the right the ball falls back: a velocity arrow down. In the free-body diagram the weight down and the air resistance from the bottom surface up. The net force arrow down is shorter than the weight, and the acceleration arrow is shorter than on the left." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-14-ylos.webp" x="0" y="1.2" width="600" height="438.8" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising}$</div></foreignObject>
  <foreignObject x="188" y="80.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="125.5" y="314" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="49.5" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="203.5" y="226.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="239.5" y="390" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
  <foreignObject x="402.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{falling}$</div></foreignObject>
  <foreignObject x="488" y="80.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="425.5" y="314" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="349.5" y="289.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="503.5" y="207.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="539.5" y="326" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
</svg>

### When the parachute opens
The large area of the parachute makes air resistance many times greater. When the parachute opens, the skydiver is still moving downward at terminal velocity, so for a moment the air resistance is many times the weight. The net force and the acceleration point up, even though the skydiver is moving down: the skydiver slows down but does not rise. As the speed decreases, air resistance decreases until, at a new, small terminal velocity, it is again equal to the weight. How many times the weight the air resistance is depends on the parachute and the moment: in the diagram it is three times, in the example almost three times, and in the model of the simulation at most about five times. The direction of the net force can therefore differ from the direction of motion. It always tells the direction of the acceleration, not of the velocity.

<svg data-fig="varjo" viewBox="0 0 600 500" role="img" aria-label="Three stages when the parachute is opened, forces to scale. At the top are situation pictures and at the bottom free-body diagrams of the skydiver, in which the skydiver with the parachute is a rectangle. On the left falling before the parachute is opened, at terminal velocity: a long blue velocity arrow down, the weight G from the centre down and the air resistance F_v from the bottom up to the bottom surface, equally long, acceleration zero. In the middle the parachute opens: the velocity arrow still points down, the air resistance starts from the top surface and points up and is three times the length of the weight. Separately a green hollow net force arrow up and an orange acceleration arrow up. On the right the parachute is open: a short velocity arrow down, the air resistance from the top surface up as long as the weight, acceleration zero." style="max-width:100%;font-size:30px">
  <image href="pics/fy4/fy4-14-varjo.webp" x="0" y="0" width="600" height="506.2" preserveAspectRatio="none"/>
  <foreignObject x="-4" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{terminal velocity}$</div></foreignObject>
  <foreignObject x="168" y="98" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="88.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="12.5" y="420" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="132.5" y="354" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="233.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{chute opens}$</div></foreignObject>
  <foreignObject x="368" y="87" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="288.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="212.5" y="205.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="346.5" y="252" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="350.5" y="338" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
  <foreignObject x="415" y="7.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{new terminal v.}$</div></foreignObject>
  <foreignObject x="568" y="60" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="488.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="412.5" y="300" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="532.5" y="354" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
</svg>

## Worked example
A skydiver whose mass with equipment is $85.0\,\text{kg}$ opens the parachute. At one moment while the parachute is opening, the air resistance is $2.40\,\text{kN}$, and the skydiver is still moving downward. What is the acceleration of the skydiver at this moment, and in which direction does it point?

<!-- vaihe -->

**Given and find.** $m = 85.0\,\text{kg}$, $F_\text{v} = 2.40\,\text{kN}$ and $g = 9.81\,\text{m/s}^2$. We want the acceleration $a$ and its direction.

<!-- vaihe -->

**Principle.** Choose the skydiver with the equipment and the parachute as the object. The Earth (weight) and the air (air resistance) act on it. By Newton's second law, the acceleration is determined by the sum of these forces; the direction of the velocity does not decide the direction of the acceleration.

<!-- vaihe -->

**Rearranged formula.** In the free-body diagram the skydiver is a rectangle. The weight $\overline{G}$ starts from the centre and points down. Air resistance $\overline{F}_\text{v}$ acts mainly on the parachute, so it starts from the top surface and points up. The positive direction is chosen down, the direction of motion.

<svg data-fig="esimerkki" viewBox="0 0 600 380" role="img" aria-label="On the left a situation picture: the parachute of the skydiver is opening, and next to the skydiver a blue velocity arrow points down. On the right the free-body diagram of the skydiver, the skydiver with the parachute as a rectangle: the weight G from the centre down and the air resistance F_v from the top surface up, almost three times the length of the weight. Separately an orange acceleration arrow up. On the right a small arrow y down: the positive direction is down." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy414-ex-c" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="100.5" y1="191.5" x2="71.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="106" y1="191.5" x2="94.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="114" y1="191.5" x2="125.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119.5" y1="191.5" x2="148.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M67,136.5 Q67,106 110,106 Q153,106 153,136.5 Z" fill="url(#fy414-ex-c)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="81.5" y1="136.5" x2="81.5" y2="124" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="136.5" x2="96" y2="115.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="136.5" x2="110" y2="112" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="124" y1="136.5" x2="124" y2="115.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="138.5" y1="136.5" x2="138.5" y2="124" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <g transform="translate(110,220) scale(0.95)">
  <path d="M-5,12 L-7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M5,12 L7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-11" y="-18" width="22" height="34" rx="7" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="-8" y="-16" width="16" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M-11,-12 L-18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M11,-12 L18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="0" cy="-28" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M-10,-28 A10,10 0 0 1 10,-28 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="180" y1="200" x2="180" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M173.5,267 L180,280 L186.5,267" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="198" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="40" y="341.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <foreignObject x="296" y="341.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <line x1="232" y1="20" x2="232" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="315" y="208" width="90" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="342" y1="208" x2="342" y2="81" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M342,64 L350,82 L334,82 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="285.5" y="61.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <line x1="360" y1="230" x2="360" y2="263" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M360,280 L352,262 L368,262 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="367.5" y="261.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="470" y1="250" x2="470" y2="182" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476.5,193 L470,180 L463.5,193" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="453.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="560" y1="200" x2="560" y2="257" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M560,266 L555.5,256 L564.5,256 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="550" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

From the diagram we write the net force $mg - F_\text{v}$ and solve the acceleration:
```latex
\begin{aligned}
&mg - F_\text{v} = ma \\
&a = \frac{mg - F_\text{v}}{m}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Air resistance is converted to newtons: $2.40\,\text{kN} = 2.40\cdot 1000\,\text{N} = 2400\,\text{N}$.

<!-- vaihe -->

**Substitution.** First calculate the weight and then the acceleration:
```latex
\begin{aligned}
&a = \frac{mg - F_\text{v}}{m} \\
&mg = 85.0\,\text{kg}\cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \\
&\phantom{mg} = 833.85\,\text{N} \\
&a = \frac{833.85\,\text{N} - 2400\,\text{N}}{85.0\,\text{kg}} \\
&\phantom{a} \approx -18.4\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration is negative, so it points up, opposite to the direction chosen as positive. The magnitude of the acceleration is $18.4\,\text{m/s}^2$ upward, given with three significant figures like the mass $85.0\,\text{kg}$ and the air resistance $2.40\,\text{kN}$. The skydiver moves down, but the speed decreases.

<!-- vaihe -->

**Reasonableness.** Air resistance is almost three times the weight $834\,\text{N}$, so about two weights of net force remain upward. The acceleration must therefore be about two times $g$, or about $20\,\text{m/s}^2$, and the result $18.4\,\text{m/s}^2$ fits this. To the skydiver, the opening of the parachute feels like a strong jerk, but it lasts only a few seconds.

## Common misconception
In videos, the skydiver seems to rise upward when the parachute opens. The camera operator is still falling without a parachute, and the skydiver only slows down relative to the camera operator. Relative to the ground, the skydiver moves downward all the time: the net force points up for a moment, but it decreases the speed and does not turn the motion around. Another mistake is to think that at terminal velocity air resistance is greater than the weight or that there are no forces any more. At terminal velocity the forces are equal and opposite. A third mistake is to claim that a heavy object always falls faster. Without air resistance, everything falls with the same acceleration. In air, of objects of the same size and shape the heavier one reaches the greater terminal velocity.

## Summary
- Resistance of the medium, in air air resistance $\overline{F}_\text{v}$, points against the velocity and grows when the speed grows. It is greater with a large cross-sectional area and a poorly streamlined shape.
- The acceleration of a falling object decreases as air resistance grows. At terminal velocity $F_\text{v} = G$, the net force is zero and the speed stays constant.
- Of objects of the same size and shape, the heavier one has the greater terminal velocity. A parachute lowers the terminal velocity to a safe one.
- The equation of motion is $\overline{G} + \overline{F}_\text{v} = m\overline{a}$. For a rising object, air resistance points down together with the weight, so the deceleration is greater than $g$.
- When the parachute opens, the net force and the acceleration point up even though the skydiver moves down: the direction of the net force can differ from the direction of motion.
