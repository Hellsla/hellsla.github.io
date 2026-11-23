# Equilibrium, circular motion and gravitation

> **Why** can a satellite dish be aimed once and left in place, although the television satellite orbits the Earth at a speed of about $3\,\text{km/s}$?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter dusk in the countryside. In the middle is a red wooden house with snow on its roof and light in its windows. On the gable wall of the house is a satellite dish aimed low into the sky on the left. A faint dashed line runs from the dish to a television satellite with two solar panels in the sky. The satellite is on a dashed arc that crosses the sky. There are stars in the sky, the edge of a forest in the background and snowbanks and spruces in front." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-ympyraliike-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

The problems of this lesson start in the same way as mechanics problems usually do: **choose the body, draw the free-body diagram and write Newton's second law**. The situation tells what the acceleration is. In equilibrium the body at rest neither starts to move nor starts to turn, so both the sum of the forces and the sum of the moments are zero. In uniform circular motion the acceleration points to the centre of the path, so the sum of the forces points there too. Only gravitation acts on a satellite, so the gravitational force is itself the net force.

```pysahdy
In which direction does the sum of the forces point in uniform circular motion, and why?
---
Towards the centre of the path, because the acceleration points there and the net force has the same direction as the acceleration.
```

<svg data-fig="kartta" viewBox="0 0 380 870" role="img" aria-label="Recognition chart: how do I tell which law to use? Draw the free-body diagram first and see which sign in the task fits. A rod stays in place: the sum of the moments is zero too. Circular path: the normal acceleration is v squared divided by r. Angular velocity given: the orbital speed is omega times r. Which force bends the path: the sum of the forces is mass times normal acceleration. A bend on a level road: static friction turns the car, and the friction force equals m v squared per r. Two bodies attract each other: the law of gravitation, F g equals gamma M m per r squared. Free-fall acceleration asked: weight is gravitation, m g equals gamma M m per r squared. A satellite orbits: gravity bends the path, gamma M m per r squared equals m v squared per r." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="811" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{free-body diagram first, then the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a rod stays in place}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="204" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{moments too}$</div></foreignObject>
  <rect x="262" y="142" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="144" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma M = 0$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{circular path}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{normal acceleration}$</div></foreignObject>
  <rect x="246" y="228" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="230" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$a_\text{n} = v^2/r$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{angular velocity given}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="204" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{orbital speed}$</div></foreignObject>
  <rect x="262" y="314" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="316" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = \omega r$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{which force bends the path?}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{sum of forces}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma F = ma_\text{n}$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a bend on a level road}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{static friction}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F = mv^2/r$</div></foreignObject>
  <line x1="14" y1="579" x2="30" y2="579" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{two bodies attract each other}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{law of gravitation}$</div></foreignObject>
  <rect x="192" y="601" width="170" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="196" y="604" width="162" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{g} = \gamma Mm/r^2$</div></foreignObject>
  <line x1="14" y1="695" x2="30" y2="695" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="644" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="654.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{free-fall acceleration asked}$</div></foreignObject>
  <line x1="40" y1="684" x2="362" y2="684" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="689" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{weight is gravitation}$</div></foreignObject>
  <rect x="192" y="717" width="170" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="196" y="720" width="162" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$mg = \gamma Mm/r^2$</div></foreignObject>
  <line x1="14" y1="811" x2="30" y2="811" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="760" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="770.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a satellite orbits}$</div></foreignObject>
  <line x1="40" y1="800" x2="362" y2="800" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="805" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{gravity bends the path}$</div></foreignObject>
  <rect x="162" y="833" width="200" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="166" y="836" width="192" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\gamma Mm/r^2 = mv^2/r$</div></foreignObject>
</svg>

The opening question is solved in the same way. Only the gravitational force of the Earth acts on the satellite, and it gives the satellite its centripetal acceleration. The further away the satellite orbits, the longer its period. The geostationary orbit lies above the equator at exactly the distance at which the period is the same as the Earth's rotation period, $23\,\text{h}\;56\,\text{min}$. From the period the radius of the orbit comes out as $r \approx 42\,200\,\text{km}$, about $35\,800\,\text{km}$ above the Earth's surface, and the orbital speed as $v = \tfrac{2\pi r}{T} \approx 3.07\,\text{km/s}$. The satellite and the dish go round the Earth's axis in the same time and in the same direction, so as seen from the dish the satellite stays still.

<svg data-fig="geo" viewBox="0 0 600 600" role="img" aria-label="Diagram seen from the direction of the North Pole, radii to scale. In the middle is the Earth, round which the geostationary orbit runs as a dashed line. The radius r of the orbit is about 42 200 km, about 6.6 Earth radii. The Earth rotates and the satellite orbits in the same direction, anticlockwise, and each makes one revolution in the time T = 23 h 56 min. The blue velocity arrow of the satellite is along the tangent of the orbit, and the red arrow of the gravitational force points to the centre of the Earth. On the Earth&#x27;s surface is the position of the dish, from which a dashed line runs to the satellite. Six hours later the dish and the satellite have each turned a quarter of a revolution: the new line of sight, drawn faintly, is the same line turned." style="max-width:100%;font-size:26px">
  <image href="pics/fy9/fy9-ympyraliike-geo.webp" x="0" y="0" width="600" height="600" preserveAspectRatio="none"/>
  <foreignObject x="166.5" y="57.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="297.5" y="155" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="326" y="243.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{dish}$</div></foreignObject>
  <foreignObject x="78" y="262.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{6 h later}$</div></foreignObject>
  <foreignObject x="416" y="414.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$r \approx 6.6\,R$</span></div></foreignObject>
  <foreignObject x="208" y="10.5" width="184" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$T = 23\,\text{h}\;56\,\text{min}$</div></foreignObject>
  <foreignObject x="147.5" y="564.5" width="305" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{orbit radius } r \approx 42\,200\,\text{km}$</div></foreignObject>
</svg>

## Formula: Equilibrium, circular motion and gravitation

### Moment and equilibrium

```kaavat
moment of a force :: M = Fr
\Sigma\overline{F} = \overline{0}
\Sigma M = 0
```

where $M$ is the moment of the force ($\text{Nm}$), $F$ the size of the force ($\text{N}$) and $r$ the lever arm of the force ($\text{m}$), that is, the perpendicular distance of the axis of rotation from the line of action of the force. If the force makes the angle $\alpha$ with the line from the axis to the point of application and the point of application is at the distance $d$, the lever arm is $r = d\sin\alpha$. An anticlockwise moment is positive. For a body at rest the moment condition holds about any point, so it pays to choose the point of application of an unknown force as the pivot point. The weight acts at the centre of gravity.

<svg data-fig="tilanteet" viewBox="0 0 380 690" role="img" aria-label="Three free-body diagrams one below the other. At the top a uniform plank at rest on two supports, drawn as a rectangle: the weight G starts from the centre and points down, and the normal forces N 1 and N 2 point up from the lower surface. Support 2 is closer to the centre, and its normal force is twice as long as N 1; together they are as long as the weight. Conditions: the sum of the forces and the sum of the moments are zero. In the middle a car at the top of a hump, drawn as a rectangle: the weight G down and the normal force N up, shorter than the weight. Beside the car a blue velocity arrow forwards and an orange acceleration arrow down towards the centre of the curve. Condition: G minus N is m v squared divided by r. At the bottom a satellite drawn as a rectangle: the only force is the gravitational force F of the Earth, down towards the centre of the Earth. Beside it a velocity arrow forwards and an acceleration arrow down. Condition: the gravitational force is m v squared divided by r." style="max-width:100%;font-size:20px">
  <image href="pics/fy9/fy9-ympyraliike-tilanteet.webp" x="0" y="0" width="380" height="679.2" preserveAspectRatio="none"/>
  <foreignObject x="12" y="8" width="250" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{plank at rest: } \Sigma\overline{F} = \overline{0},\ \Sigma M = 0$</div></foreignObject>
  <foreignObject x="157.5" y="194" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="90.5" y="65" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}_{1}$</div></foreignObject>
  <foreignObject x="234.5" y="45" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}_{2}$</div></foreignObject>
  <foreignObject x="12" y="232" width="195" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{top of a hump: } G - N = m\dfrac{v^2}{r}$</div></foreignObject>
  <foreignObject x="291.5" y="330" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="269.5" y="398" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="115.5" y="430" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="161.5" y="304" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="12" y="466" width="174" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{satellite: } \gamma\dfrac{Mm}{r^2} = m\dfrac{v^2}{r}$</div></foreignObject>
  <foreignObject x="265.5" y="550" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="243.5" y="612" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="115.5" y="620" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="298" y="634" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{Earth}$</div></foreignObject>
</svg>

### Uniform circular motion

```kaavat
orbital speed :: v = \omega r
centripetal acceleration :: a_\text{n} = \frac{v^2}{r} = \omega^2 r
```

where $v$ is the orbital speed ($\text{m/s}$), $r$ the radius of the path ($\text{m}$), $\omega = \tfrac{2\pi}{T} = 2\pi f$ the angular velocity ($\text{rad/s}$), $T$ the period ($\text{s}$) and $f = \tfrac{1}{T}$ the rotation frequency ($\tfrac{1}{\text{s}}$), so $v = \tfrac{2\pi r}{T} = 2\pi r f$, and $a_\text{n}$ the centripetal acceleration ($\text{m/s}^2$). In uniform circular motion the speed is constant. The velocity is along the tangent of the path, and the centripetal acceleration points to the centre of the path.

```pysahdy
In which direction does the velocity point in uniform circular motion, and in which direction does the normal acceleration point?
---
The velocity is along the tangent of the path and the normal acceleration points towards the centre of the path.
```

By Newton's second law the net force $\Sigma F$ ($\text{N}$) on the body gives it the centripetal acceleration, so the net force points to the centre. The centripetal acceleration $a_\text{n} = \tfrac{v^2}{r}$ also holds at an instant when the speed changes: at the highest and the lowest point of the path there is no force along the tangent. In the equation of motion the forces pointing to the centre are positive, and perpendicular to the plane of the path the sum of the forces is zero.

```johda
A body of mass $m$ is in uniform circular motion at the speed $v$ on a path of radius $r$. Derive the net force $\Sigma F$ on the body from Newton's second law and the centripetal acceleration.
---
Newton's second law $\Sigma\overline{F} = m\overline{a}$ also holds in circular motion. In uniform circular motion the acceleration is the centripetal acceleration $a_\text{n} = \tfrac{v^2}{r}$, which points to the centre of the path. So the net force points to the centre, and its magnitude is

$$\Sigma F = ma_\text{n} = m\frac{v^2}{r}$$
```

<svg data-fig="kaarre" viewBox="0 0 380 280" role="img" aria-label="Free-body diagram, no numerical values: a car in a curve of a horizontal road seen from behind, as a rectangle. The centre of the curve is to the left. The weight G starts from the centre point and points down, and the normal force N, equally long, starts from the road surface and points up. The road surface is a dashed line. The friction force F mu starts from the lower left corner of the car and points to the left along the road, towards the centre of the curve. Beside the car an orange acceleration arrow points to the left towards the centre. The velocity points away from the viewer, drawn as a circle with a cross inside." style="max-width:100%;font-size:20px">
  <line x1="16" y1="206" x2="364" y2="206" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="12" y="23" width="167" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px;color:#6b7480">$\leftarrow \text{centre of the curve}$</div></foreignObject>
  <line x1="119" y1="142" x2="51" y2="142" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M62,135.5 L49,142 L62,148.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="32.5" y="108" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <rect x="135" y="130" width="130" height="76" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="200" y1="168" x2="200" y2="231" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M200,248 L192,230 L208,230 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="165.5" y="240" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="232" y1="206" x2="232" y2="143" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M232,126 L240,144 L224,144 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="237.5" y="100" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="135" y1="206" x2="94" y2="206" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M77,206 L95,198 L95,214 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="55.5" y="218" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <circle cx="305" cy="148" r="13" fill="#ffffff" stroke="#1971c2" stroke-width="2.5"/>
  <line x1="296" y1="139" x2="314" y2="157" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="296" y1="157" x2="314" y2="139" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="327" y="136" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

```johda
A car of mass $m$ drives at the speed $v$ in a curve of a horizontal road with radius $r$. The friction of the road gives the car its centripetal force. Derive how large a friction force is needed and the greatest speed at which the car still stays on the road when the coefficient of static friction is $\mu_0$.
---
In the curve the forces on the car are the weight $G = mg$, the normal force $N$ of the road and the friction force $F_\mu$ of the road (figure). There is no vertical acceleration, so $N = mg$. The only horizontal force is friction, so it is the net force. In uniform circular motion the net force is $\Sigma F = m\tfrac{v^2}{r}$, so

$$F_\mu = m\frac{v^2}{r}$$

The tyres do not slide sideways, so the friction is static friction. It is at most $\mu_0 N = \mu_0 mg$. The car stays on the road when

$$m\frac{v^2}{r} \le \mu_0 mg \quad\Rightarrow\quad v \le \sqrt{\mu_0 g r}$$

The mass cancels, so the greatest speed does not depend on the mass of the car.
```

### Gravitation and satellites

```kaavat
Newton's law of gravitation :: F_\text{g} = \gamma\frac{m_1 m_2}{r^2}
```

where $$
\gamma = 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}
$$ is the gravitational constant, $F_\text{g}$ the magnitude of the gravitational force ($\text{N}$), $m_1$ and $m_2$ the masses of the bodies ($\text{kg}$) and $r$ the distance between the centres ($\text{m}$). The law holds for point-like and spherically symmetric bodies. The gravitational field strength $g$ ($\text{N/kg}$, that is $\text{m/s}^2$) of a central body of mass $M$ ($\text{kg}$) is the gravitational force per unit mass of a body; at the Earth's surface it is the acceleration due to gravity.

```pysahdy
How does the magnitude of the gravitational force change when the distance $r$ between the centres of the bodies doubles?
---
It becomes one quarter, because $F_\text{g}$ is proportional to $\tfrac{1}{r^2}$.
```

```johda
A body of mass $m$ is at the distance $r$ from the centre of a central body of mass $M$. Derive the gravitational field strength $g$, that is the acceleration due to gravity, at this distance.
---
By Newton's law of gravitation the gravitational force on the body is

$$F_\text{g} = \gamma\frac{Mm}{r^2}$$

This force is the weight $G = mg$ of the body when the rotation of the central body is ignored. Set the forces equal:

$$mg = \gamma\frac{Mm}{r^2}$$

The mass $m$ of the body cancels:

$$g = \gamma\frac{M}{r^2}$$

The field strength does not depend on the mass of the body, so all bodies fall with the same acceleration. Air resistance is neglected. At the Earth's surface $r = R$, and further away $g$ decreases with the square of the distance.
```

A satellite orbits a central body on a circular orbit of radius $r$ at the orbital speed $v$ ($\text{m/s}$). The only force on it is the gravitational force, which gives it the centripetal acceleration. For an Earth satellite $r = R + h$, where $R = 6371\,\text{km}$ and $h$ is the height above the surface, and the period is $T = \tfrac{2\pi r}{v}$.

```johda
A satellite of mass $m$ orbits a central body of mass $M$ on a circular orbit of radius $r$. Derive the orbital speed $v$ of the satellite.
---
The only force on the satellite is the gravitational force, so it is the net force and points to the centre of the orbit. By Newton's second law it gives the satellite the centripetal acceleration $a_\text{n} = \tfrac{v^2}{r}$. Writing the gravitational force by Newton's law of gravitation gives

$$\gamma\frac{Mm}{r^2} = m\frac{v^2}{r}$$

The mass $m$ of the satellite cancels. Multiply the equation by the radius $r$:

$$v^2 = \frac{\gamma M}{r}$$

The orbital speed is positive, so

$$v = \sqrt{\frac{\gamma M}{r}}$$

The orbital speed does not depend on the mass of the satellite, and the further out the orbit, the smaller it is. The result holds when the central body is much more massive than the satellite, so that the central body stays in place.
```

## Common mistakes {Virheet}

- **The distance in place of the lever arm.** The moment of a slanting force is $Fd\sin\alpha$, not $Fd$.
- **The support further away carries more.** It is the other way round: the support closer to the centre of gravity carries more.
- **A centrifugal force in the free-body diagram.** There is no outward force. The centripetal force is the sum of the real forces, and it is not drawn as an arrow of its own.
- **Diameter and revolutions per minute.** The radius is substituted into the formula, and $\tfrac{1}{\text{min}}$ is converted: $1\,\text{min} = 60\,\text{s}$.
- **The height in place of the radius.** The radius of the orbit is measured from the centre of the Earth: $r = R + h$.
- **Weightlessness is the absence of gravity.** On a space station gravitation acts, but the station and the astronaut fall freely together, so the normal force is zero.

## Review if needed {Kertaa}

- The lever arm and the direction of turning: [*Moment: the turning effect of a force*](fy5-1.html). The equilibrium conditions and the centre of gravity: [*Equilibrium of a body: forces and moments*](fy5-2.html).
- The period and the orbital speed: [*Moving in a circle: period and speed*](fy5-3.html). Centripetal acceleration and the equation of motion: [*Centripetal acceleration and the equation of motion in a circle*](fy5-4.html).
- The law of gravitation and the field strength: [*The gravitational force between bodies*](fy5-5.html). Orbital speed, period and weightlessness: [*Satellites and planets in circular orbits*](fy5-6.html).
