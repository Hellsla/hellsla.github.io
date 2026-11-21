# Comparing the motions of two bodies

> **Why** does a car that starts from rest catch a steadily pedalling cyclist ahead of it only far down the road, even though the car accelerates all the time?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a country road in the late morning. The traffic light has turned green and a car starts moving from the stop line. Ahead of it on the road a cyclist is already pedalling at a steady speed. Behind the car there is a puff of exhaust and behind the cyclist there are speed lines. Marker posts stand at equal intervals along the road, and in the background there are a field, a red house, birches and a spruce forest." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
The motions of two bodies can be compared only when both positions are measured in the same coordinate system. We choose one $x$-axis, one origin, one positive direction and one clock that reads zero when the motions begin. Then each body has its own position as a function of time: $x_\text{A}(t)$ and $x_\text{B}(t)$. The origin and the direction can be chosen freely, but they are chosen once and kept for the whole problem.

The bodies **meet** when they are at the same place at the same moment, that is, $x_\text{A} = x_\text{B}$. A meeting always raises two questions: when does it happen, and where? If the bodies come from opposite directions, they meet each other. If the one behind catches up with the one ahead and passes it, this is **overtaking**. The physics is the same in both: the positions are equal.

```pysahdy
Two cyclists ride in the same direction, one ahead of the other. How do you know the one behind has reached the other?
---
Their positions are equal at the same moment: $x_\text{A} = x_\text{B}$. After that, the one who came from behind is ahead.
```

<svg data-fig="tilanne" viewBox="0 0 600 420" role="img" aria-label="Formula figure, to scale, with two bodies on the same x-axis. At the top, at t = 0, body A is at 0 m and moves to the right at 3.0 m/s, and body B is at 60 m and moves to the left at 2.0 m/s. At the bottom, at t = 12 s, both are at 36 m: the bodies have met. The velocity arrows are blue and of different lengths." style="max-width:100%;font-size:24px">
  <line x1="32" y1="168" x2="516" y2="168" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M528,168 L515,174 L515,162 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="164" x2="50" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="40" y="179.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="125" y1="164" x2="125" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="108.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="200" y1="164" x2="200" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="183.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="275" y1="164" x2="275" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="258.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="350" y1="164" x2="350" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="425" y1="164" x2="425" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="500" y1="164" x2="500" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="536" y="153.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="24" y="11.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t = 0$</div></foreignObject>
  <line x1="50" y1="87" x2="50" y2="168" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="50" cy="70" r="17" fill="#2b8a3e" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="40" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{A}$</div></foreignObject>
  <circle cx="50" cy="168" r="7" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <line x1="76" y1="70" x2="103" y2="70" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M118,70 L102,77 L102,63 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="500" y1="135" x2="500" y2="168" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="500" cy="118" r="17" fill="#8a5f22" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="490" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{B}$</div></foreignObject>
  <circle cx="500" cy="168" r="7" fill="#8a5f22" stroke="#ffffff" stroke-width="2"/>
  <line x1="474" y1="118" x2="461" y2="118" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M446,118 L462,111 L462,125 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="94" y="23.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{A}$</div></foreignObject>
  <foreignObject x="415" y="71.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{B}$</div></foreignObject>
  <line x1="24" y1="214" x2="576" y2="214" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <line x1="32" y1="380" x2="516" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M528,380 L515,386 L515,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="376" x2="50" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="40" y="391.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="125" y1="376" x2="125" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="108.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="200" y1="376" x2="200" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="183.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="275" y1="376" x2="275" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="258.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="350" y1="376" x2="350" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="425" y1="376" x2="425" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="500" y1="376" x2="500" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="536" y="365.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="24" y="227.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t = 12\,\text{s}$</div></foreignObject>
  <line x1="320" y1="299" x2="320" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="320" cy="282" r="17" fill="#2b8a3e" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="310" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{A}$</div></foreignObject>
  <line x1="346" y1="282" x2="373" y2="282" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M388,282 L372,289 L372,275 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="320" y1="347" x2="320" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="320" cy="330" r="17" fill="#8a5f22" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="310" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{B}$</div></foreignObject>
  <line x1="294" y1="330" x2="281" y2="330" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M266,330 L282,323 L282,337 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="320" cy="380" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="406" y="291.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x_\text{A} = x_\text{B} = 36\,\text{m}$</div></foreignObject>
</svg>

In the figure, body A starts from $0\,\text{m}$ and B from $60\,\text{m}$, and they move toward each other. When the positions of the bodies are marked on the same axis, you can see at once which is where and how the distance between them changes. At the moment of meeting, the distance is zero.

In a $(t,x)$ graph, each motion is its own line in the same coordinate system. The meeting is the intersection of the lines: its horizontal coordinate is the time of the meeting and its vertical coordinate is the place. A line higher in the graph means a larger position coordinate. At the moment of meeting, the bodies' graphs intersect. Which body is ahead also depends on the direction of motion: when the bodies move in the positive $x$ direction, the higher line belongs to the body that is ahead. When they move in the negative direction, the body whose line is lower is ahead.

<svg data-fig="kohtaus" viewBox="0 0 600 350" role="img" aria-label="(t,x) graph, to scale, of two uniform motions. Body A starts from 0 m and moves at 3.0 m/s: the line rises. Body B starts from 60 m at −2.0 m/s: the line falls. The lines intersect at the point where t = 12 s and x = 36 m. Dashed lines lead from the point to the axes." style="max-width:100%;font-size:24px">
  <line x1="186" y1="300" x2="186" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="300" x2="280" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="300" x2="374" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="258.5" x2="468" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="217.5" x2="468" y2="217.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="176" x2="468" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="134.5" x2="468" y2="134.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="93.5" x2="468" y2="93.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186" y1="300" x2="186" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="280" y1="300" x2="280" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="374" y1="300" x2="374" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="451.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="85" y1="258.5" x2="92" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="244" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="85" y1="217.5" x2="92" y2="217.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="203" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="85" y1="176" x2="92" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="161.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$36$</div></foreignObject>
  <line x1="85" y1="134.5" x2="92" y2="134.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="85" y1="93.5" x2="92" y2="93.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="79" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$x\ (\text{m})$</span></div></foreignObject>
  <polyline points="92,300 468,134.5" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,93.5 468,203.5" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="374" y1="176" x2="374" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="176" x2="374" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="374" cy="176" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$x_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="189" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$x_\text{B}$</div></foreignObject>
  <foreignObject x="388" y="244" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{meeting}$</div></foreignObject>
</svg>

A meeting does not mean that the bodies have the same velocity. At the intersection the lines have different slopes, because the velocities of the bodies are different. If two uniformly moving bodies had equal velocities, the lines would be parallel and the distance between the bodies would stay the same, so they would not meet if they started from different places. In overtaking, the body coming from behind is faster than the one being overtaken at the moment of meeting.

```pysahdy
Two cars drive in the same direction at the same velocity, one $50\,\text{m}$ ahead. Do they meet?
---
No. The distance stays $50\,\text{m}$, because the lines in the graph are parallel and do not intersect.
```

## Formula: Meeting condition
The time and place of a meeting are found by writing the position of each body as a function of time and setting the positions equal:
```latex
x_\text{A}(t) = x_\text{B}(t)
```
where $x_\text{A}(t)$ and $x_\text{B}(t)$ are the positions of the bodies in the same coordinate system ($\text{m}$) and $t$ is the time of the meeting ($\text{s}$). Once $t$ is solved, it is substituted into either position function, and the result is the place of the meeting. As a check, the other position function gives the same place.

The position function depends on the kind of motion. In uniform motion it is $x = x_0 + v\,t$ (chapter *Position, velocity and uniform motion as graphs*). In uniformly accelerated motion (chapter *Acceleration and uniformly accelerated motion*) it is
```kaavat
position in uniformly accelerated linear motion :: x = x_0 + v_0\,t + \tfrac12\,a\,t^2
velocity in uniformly accelerated linear motion :: v = v_0 + a\,t
```
where $x_0$ is the initial position ($\text{m}$), $v_0$ the initial velocity ($\text{m/s}$), $a$ the acceleration ($\text{m/s}^2$), $t$ the time ($\text{s}$) and $v$ the velocity at time $t$ ($\text{m/s}$). The formulas hold when the motion is along a straight line and the acceleration is constant. The equation for two uniform motions is a first-degree equation. If the position functions are different lines, they have at most one point of intersection, so the bodies meet at most once. If the position functions are the same, the bodies are at the same position during the whole time considered. If one of them accelerates, the equation is quadratic, and the lines can have two intersections.

The simplest overtaking: a car starts from rest at the place where a cyclist passes at a constant velocity $v$. For the car $x_\text{A} = \tfrac12 a t^2$ and for the cyclist $x_\text{B} = v\,t$:
```latex
\begin{aligned}
&\tfrac12\,a\,t^2 = v\,t \\
&t\left(\tfrac12\,a\,t - v\right) = 0 \\
&t = 0 \quad\text{or}\quad t = \frac{2v}{a}
\end{aligned}
```
The solution $t = 0$ is the start: the bodies are at the same place then. The overtaking happens at $t = 2v/a$. The velocity of the car is then $a\,t = 2v$, twice the velocity of the cyclist.

<svg data-fig="kaava" viewBox="0 0 600 350" role="img" aria-label="(t,x) graph, to scale: car A starting from rest and cyclist B moving from the same place at a constant 6.0 m/s. The position of the car is the parabola x = t², that of the cyclist a straight line. The graphs intersect twice: at t = 0, when the bodies are at the same place at the start, and at t = 6.0 s at the place 36 m." style="max-width:100%;font-size:24px">
  <line x1="186" y1="300" x2="186" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="300" x2="280" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="300" x2="374" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="258.5" x2="468" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="217.5" x2="468" y2="217.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="176" x2="468" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="134.5" x2="468" y2="134.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="93.5" x2="468" y2="93.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186" y1="300" x2="186" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="280" y1="300" x2="280" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="374" y1="300" x2="374" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="364" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="458" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="85" y1="258.5" x2="92" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="244" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="85" y1="217.5" x2="92" y2="217.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="203" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="85" y1="176" x2="92" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="161.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$36$</div></foreignObject>
  <line x1="85" y1="134.5" x2="92" y2="134.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="85" y1="93.5" x2="92" y2="93.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="79" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$x\ (\text{m})$</span></div></foreignObject>
  <polyline points="92,300 95,300 98.5,300 101.5,300 104.5,300 107.5,299.5 111,299.5 114,299 117,299 120,299 123.5,298.5 126.5,298 129.5,298 132.5,297.5 136,297 139,296.5 142,296 145.5,295.5 148.5,295 151.5,294.5 154.5,294 158,293 161,292.5 164,292 167,291 170.5,290.5 173.5,289.5 176.5,289 179.5,288 183,287 186,286 189,285.5 192.5,284.5 195.5,283.5 198.5,282.5 201.5,281 205,280 208,279 211,278 214,276.5 217.5,275.5 220.5,274.5 223.5,273 226.5,271.5 230,270.5 233,269 236,267.5 239.5,266 242.5,264.5 245.5,263 248.5,261.5 252,260 255,258.5 258,257 261,255.5 264.5,253.5 267.5,252 270.5,250.5 273.5,248.5 277,246.5 280,245 283,243 286.5,241 289.5,239 292.5,237.5 295.5,235.5 299,233.5 302,231.5 305,229 308,227 311.5,225 314.5,223 317.5,220.5 320.5,218.5 324,216 327,214 330,211.5 333.5,209 336.5,207 339.5,204.5 342.5,202 346,199.5 349,197 352,194.5 355,192 358.5,189.5 361.5,187 364.5,184 367.5,181.5 371,178.5 374,176 377,173 380.5,170.5 383.5,167.5 386.5,164.5 389.5,162 393,159 396,156 399,153 402,150 405.5,147 408.5,144 411.5,140.5 414.5,137.5 418,134.5 421,131 424,128 427.5,124.5 430.5,121.5 433.5,118 436.5,115 440,111.5 443,108 446,104.5 449,101 452.5,97.5 455.5,94 458.5,90.5 461.5,87 465,83 468,79.5" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,300 468,134.5" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="374" y1="176" x2="374" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="176" x2="374" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="92" cy="300" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="374" cy="176" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="65" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$x_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$x_\text{B}$</div></foreignObject>
  <foreignObject x="388" y="206.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{overtaking}$</div></foreignObject>
  <foreignObject x="110" y="255.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{start}$</div></foreignObject>
</svg>

Why must the car reach twice the velocity? The reason can be seen in the $(t,v)$ graph. The displacement is the area between the velocity graph and the time axis, and the area between two graphs tells how much the lead changes. As long as the car is slower than the cyclist, the cyclist's lead grows. When the one behind starts slower, the lead is greatest when the velocities are equal, and that is not the moment of meeting. Only after that is the car faster and does it reduce the lead. The overtaking happens when the decrease of the lead equals the earlier growth: in the figure each area corresponds to $9\,\text{m}$. This is why the overtaking comes only far away: the car must first make up the growth of the lead, and in this example the overtaking place is $36\,\text{m}$ from the start, although the lead grew by only $9\,\text{m}$ at most.

<svg data-fig="vt" viewBox="0 0 600 350" role="img" aria-label="(t,v) graph, to scale, of the same motion as the previous graph. The velocity of the car grows as a straight line from zero, and the velocity of the cyclist is a constant 6.0 m/s. Until t = 3.0 s the cyclist is ahead and the lead grows: the area between the lines corresponds to a growth of the lead of 9 m. From 3.0 s to 6.0 s the car reduces the lead, and the area corresponds to a decrease of 9 m. At t = 6.0 s the car has caught up with the cyclist." style="max-width:100%;font-size:24px">
  <line x1="186" y1="300" x2="186" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="300" x2="280" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="300" x2="374" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="238" x2="468" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="176" x2="468" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="114" x2="468" y2="114" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="52" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186" y1="300" x2="186" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="280" y1="300" x2="280" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="374" y1="300" x2="374" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="364" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="458" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="85" y1="238" x2="92" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="223.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="85" y1="176" x2="92" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="85" y1="114" x2="92" y2="114" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="99.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="85" y1="52" x2="92" y2="52" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$16$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$v\ (\text{m/s})$</span></div></foreignObject>
  <polygon points="92,300 92,207 233,207" fill="#e9c98a" fill-opacity="0.55"/>
  <polygon points="233,207 374,114 374,207" fill="#b2f2bb" fill-opacity="0.75"/>
  <polyline points="92,207 468,207" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,300 468,52" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="233" y1="207" x2="233" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="207" x2="233" y2="207" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="374" y1="114" x2="374" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="233" cy="207" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$v_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="194.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$v_\text{B}$</div></foreignObject>
  <foreignObject x="119.5" y="168.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+9\,\text{m}$</div></foreignObject>
  <foreignObject x="312" y="168.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-9\,\text{m}$</div></foreignObject>
</svg>

If the cyclist is a distance $x_{0\text{B}}$ ahead at the start, the equation is $\tfrac12 a t^2 = x_{0\text{B}} + v\,t$. It is solved with the quadratic formula, and the time of the meeting is the positive root. A negative root would describe a moment before the start and does not belong to the situation; two positive roots would mean two meetings. If there is no positive root, the bodies do not meet.

<figure class="unit-photo"><img src="pics/fy4/helsinki-trams.webp" alt="Two white trams side by side on a street, with old stone buildings behind them."><figcaption>Two trams in Helsinki in July 2026.</figcaption></figure>

## Worked example
A cyclist rides along a straight road at a constant velocity of $6.0\,\text{m/s}$. At the moment $t = 0$ she is $16\,\text{m}$ ahead of the stop line at a traffic light. At the same moment a car standing at the line starts moving and accelerates uniformly at $2.0\,\text{m/s}^2$ in the same direction. When does the car overtake the cyclist, and how far from the stop line does the overtaking happen?

<!-- vaihe -->

**Given and find.** The origin is at the stop line and the positive direction is the direction of travel. Car A: $x_{0\text{A}} = 0$, $v_{0\text{A}} = 0$, $a = 2.0\,\text{m/s}^2$. Cyclist B: $x_{0\text{B}} = 16\,\text{m}$, $v = 6.0\,\text{m/s}$ (constant). We want the time $t$ and the place $x$ of the overtaking.

<!-- vaihe -->

**Principle.** At the moment of overtaking the bodies are at the same place, so $x_\text{A} = x_\text{B}$. The motion of the car is uniformly accelerated and that of the cyclist is uniform, so the position of each is known as a function of time. We set the positions equal and solve for the time.

<!-- vaihe -->

**Rearranged formula.** The position of the car is $x_\text{A} = \tfrac12 a t^2$ and that of the cyclist is $x_\text{B} = x_{0\text{B}} + v\,t$. The equation is solved with the quadratic formula and the positive root is chosen:
```latex
\begin{aligned}
&\tfrac12\,a\,t^2 = x_{0\text{B}} + v\,t \\
&\tfrac12\,a\,t^2 - v\,t - x_{0\text{B}} = 0 \\
&t = \frac{v + \sqrt{v^2 + 2\,a\,x_{0\text{B}}}}{a}
\end{aligned}
```
The coefficients of the quadratic equation $A t^2 + B t + C = 0$ are here $A = \tfrac12 a$, $B = -v$ and $C = -x_{0\text{B}}$, and the quadratic formula $t = \dfrac{-B \pm \sqrt{B^2 - 4AC}}{2A}$ gives the root above.

<!-- vaihe -->

**Unit conversions.** None are needed: all quantities are in SI units, and under the square root $v^2$ and $2\,a\,x_{0\text{B}}$ are both in $\text{m}^2/\text{s}^2$. The expression under the root is $v^2 + 2\,a\,x_{0\text{B}} = 36\,\text{m}^2/\text{s}^2 + 64\,\text{m}^2/\text{s}^2 = 100\,\text{m}^2/\text{s}^2$.

<!-- vaihe -->

**Substitution.** First we substitute for the time and then for the place:
```latex
\begin{aligned}
t &= \frac{v + \sqrt{v^2 + 2\,a\,x_{0\text{B}}}}{a} \\
&= \frac{6.0\,\text{m/s} + \sqrt{100\,\text{m}^2/\text{s}^2}}{2.0\,\text{m/s}^2} \\
&= \frac{6.0\,\text{m/s} + 10\,\text{m/s}}{2.0\,\text{m/s}^2} \\
&= 8.0\,\text{s}
\\[4pt]
x &= \tfrac12\,a\,t^2 \\
&= \tfrac12 \cdot 2.0\,\text{m/s}^2 \cdot (8.0\,\text{s})^2 \\
&= 64\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Result.** The car overtakes the cyclist at $t = 8.0\,\text{s}$ at the place $x = 64\,\text{m}$, measured from the stop line. The results have two significant figures, because the data $6.0\,\text{m/s}$, $2.0\,\text{m/s}^2$ and $16\,\text{m}$ have two.

<!-- vaihe -->

**Reasonableness.** The position of the cyclist is $16\,\text{m} + 6.0\,\text{m/s} \cdot 8.0\,\text{s} = 64\,\text{m}$, so the other position function gives the same place. The velocity of the car at the moment of overtaking is $a\,t = 2.0\,\text{m/s}^2 \cdot 8.0\,\text{s} = 16\,\text{m/s}$ and that of the cyclist is $6.0\,\text{m/s}$, so the car is faster as it overtakes, as it should be. The other root $t = (6.0 - 10)\,\text{m/s} : 2.0\,\text{m/s}^2 = -2.0\,\text{s}$ is before the start and does not belong to the situation.

<svg data-fig="esimerkki" viewBox="0 0 600 350" role="img" aria-label="(t,x) graph, to scale, of the situation in the example: cyclist B is at first 16 m ahead of car A and moves at 6.0 m/s; the car starts from rest with an acceleration of 2.0 m/s². The line x = 16 + 6t and the parabola x = t² intersect at t = 8.0 s at the place 64 m." style="max-width:100%;font-size:24px">
  <line x1="167" y1="300" x2="167" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="242.5" y1="300" x2="242.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317.5" y1="300" x2="317.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="393" y1="300" x2="393" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="260.5" x2="468" y2="260.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="220.5" x2="468" y2="220.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="181" x2="468" y2="181" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="141.5" x2="468" y2="141.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="101.5" x2="468" y2="101.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="62" x2="468" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="167" y1="300" x2="167" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="242.5" y1="300" x2="242.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="232.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="317.5" y1="300" x2="317.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="307.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="393" y1="300" x2="393" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="383" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="451.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="260.5" x2="92" y2="260.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="246" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="85" y1="220.5" x2="92" y2="220.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="206" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$32$</div></foreignObject>
  <line x1="85" y1="181" x2="92" y2="181" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="166.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="85" y1="141.5" x2="92" y2="141.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="127" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$64$</div></foreignObject>
  <line x1="85" y1="101.5" x2="92" y2="101.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="87" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="85" y1="62" x2="92" y2="62" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$96$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$x\ (\text{m})$</span></div></foreignObject>
  <polyline points="92,300 95,300 98.5,300 101.5,300 104.5,299.5 107.5,299.5 111,299.5 114,299 117,299 120,298.5 123.5,298.5 126.5,298 129.5,297.5 132.5,297 136,296.5 139,296 142,295.5 145.5,295 148.5,294.5 151.5,294 154.5,293 158,292.5 161,291.5 164,291 167,290 170.5,289 173.5,288.5 176.5,287.5 179.5,286.5 183,285.5 186,284.5 189,283.5 192.5,282.5 195.5,281 198.5,280 201.5,279 205,277.5 208,276.5 211,275 214,274 217.5,272.5 220.5,271 223.5,269.5 226.5,268 230,266.5 233,265 236,263.5 239.5,262 242.5,260.5 245.5,258.5 248.5,257 252,255 255,253.5 258,251.5 261,250 264.5,248 267.5,246 270.5,244 273.5,242 277,240 280,238 283,236 286.5,234 289.5,231.5 292.5,229.5 295.5,227 299,225 302,222.5 305,220.5 308,218 311.5,215.5 314.5,213 317.5,210.5 320.5,208 324,205.5 327,203 330,200.5 333.5,198 336.5,195 339.5,192.5 342.5,190 346,187 349,184 352,181.5 355,178.5 358.5,175.5 361.5,172.5 364.5,169.5 367.5,166.5 371,163.5 374,160.5 377,157.5 380.5,154 383.5,151 386.5,148 389.5,144.5 393,141.5 396,138 399,134.5 402,131 405.5,128 408.5,124.5 411.5,121 414.5,117.5 418,113.5 421,110 424,106.5 427.5,103 430.5,99 433.5,95.5 436.5,91.5 440,88 443,84 446,80 449,76 452.5,72 455.5,68.5 458.5,64 461.5,60 465,56 468,52" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,260.5 468,111.5" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="393" y1="141.5" x2="393" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="141.5" x2="393" y2="141.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="92" cy="260.5" r="6.5" fill="#8a5f22" stroke="#ffffff" stroke-width="2"/>
  <circle cx="92" cy="300" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <circle cx="393" cy="141.5" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="42.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$x_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="107" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$x_\text{B}$</div></foreignObject>
</svg>

## Common misconception
The most common mistake is to think that the bodies have the same velocity at the moment of meeting, because they are at the same place. Position and velocity are different quantities: the bodies are at the same place only at that moment, and in overtaking the one coming from behind is moving faster at the moment of overtaking.

A second mistake is to solve the time of the meeting by setting the velocities equal. That finds the moment when the lead is greatest or smallest, not the moment when the bodies are at the same place. In a meeting, the positions are equal.

A third mistake is to read the intersection of a $(t,v)$ graph as a meeting. There the lines intersect when the velocities are equal. A meeting can be seen only in the $(t,x)$ graph.

## Summary
- The positions of two bodies are measured in the same coordinate system: the same origin, the same positive direction and the same clock.
- The bodies meet when $x_\text{A}(t) = x_\text{B}(t)$. The equation gives the time of the meeting, and substituting it into a position function gives the place.
- In a $(t,x)$ graph the meeting is the intersection of the lines. At a meeting the velocities are usually different.
- When one motion is uniformly accelerated, the equation is quadratic. Every positive root is a meeting (there can be two), and a negative root is before the start and does not belong to the situation.
- When the one behind starts slower, the lead is greatest when the velocities are equal, and that is not the moment of meeting.
