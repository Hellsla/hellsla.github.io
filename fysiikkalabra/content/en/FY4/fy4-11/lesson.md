# Road safety: braking, seat belts and airbags

> **Why** is the stopping distance of a car travelling at $100\,\text{km/h}$ almost three times that at $50\,\text{km/h}$, and why does a seat belt protect you when the car cannot stop in time?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an autumn evening on a country road in the middle of a spruce forest. A car with its headlights on approaches from the left. On the right side of the road is a moose warning sign, and behind it a moose steps from the edge of the forest onto the road in front of the car. The distance between the car and the moose is short compared with the distance the car needs to stop." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Stopping starts with a reaction
When a driver notices danger, the car does not start to slow down at once. The driver must first notice the danger, decide to brake and move a foot to the brake pedal. This takes the **reaction time** $t_\text{r}$, usually about one second. For example, the crash speed calculator of Liikenneturva, the Finnish Road Safety Council, assumes a reaction time of $1\,\text{s}$. Fatigue, alcohol and a glance at the phone make the reaction time longer. During the reaction time the car still moves at its original speed and travels the **reaction distance** $s_\text{r}$. Only then do the brakes begin to slow the car, and it travels the **braking distance** $s_\text{b}$ before it stops. The reaction distance and the braking distance together are the **stopping distance** $s_\text{stop}$.

### The road stops the car by friction
The brakes slow the rotation of the wheels, but it is the road that slows the car. On a horizontal road the friction between the tyres and the road is the only horizontal force, when air resistance is neglected. Friction points backwards, so by Newton's second law the acceleration also points backwards and the car slows down. In braking, the magnitude of the acceleration is called the **deceleration** $a$.

<svg data-fig="jarrutus" viewBox="0 0 600 330" role="img" aria-label="On the left a picture of the situation: a car brakes on a horizontal road, the brake lights are on. Above the car a blue velocity arrow points forwards to the right and an orange acceleration arrow points backwards to the left. On the right the free-body diagram of the car, the car drawn as a rectangle: the weight G from the centre downwards, the normal force N of the road from the lower surface upwards, as long as the weight, and the friction F mu of the road from the rear corner of the lower surface backwards, almost as long as the weight. Friction is the only horizontal force." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-11-jarrutus.webp" x="1.2" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="90" y="9.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <foreignObject x="205.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="97.5" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="371" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{force diagram}$</div></foreignObject>
  <foreignObject x="475.5" y="230" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="503.5" y="107" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="312" y="203.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

Friction has an upper limit that depends on the tyres and the road surface. On dry asphalt the deceleration can be about $9\,\text{m/s}^2$, and the Liikenneturva calculator uses this value too. On a wet, snowy or icy road the friction and therefore the deceleration are smaller, on ice only a fraction of the value on a dry road. Anti-lock brakes (ABS) stop the wheels from locking. The surface of a rolling tyre does not slide relative to the road, so static friction acts on the tyre. It can be greater than the sliding friction of a sliding tyre, and the car stays steerable.

```pysahdy
Why is the braking distance longer on an icy road than on dry asphalt, even when the brake pedal is pressed fully?
---
On ice the friction is smaller, so the deceleration is smaller. Stopping then takes longer and the car travels a longer distance.
```

### Speed makes the braking distance grow steeply
The reaction distance is directly proportional to the speed: at double the speed the car travels double the distance during the reaction time. The braking distance grows more steeply. With the same deceleration, stopping from double the speed takes twice as long, and for that whole time the car moves twice as fast. The braking distance is therefore four times as long. In the figure the reaction time is $1.0\,\text{s}$ and the deceleration $9.0\,\text{m/s}^2$ at both speeds.

<svg data-fig="pysahtyminen" viewBox="0 0 600 400" role="img" aria-label="Two roads one above the other, distances to scale, cars not. In both, the driver notices the danger at the dashed line. At the top the speed is 50 kilometres per hour: a green reaction distance of 13.9 metres and a brown braking distance of 10.7 metres, 24.6 metres in total. At the bottom the speed is 100 kilometres per hour: the reaction distance is twice as long, 27.8 metres, and the braking distance four times as long, 42.9 metres, 70.6 metres in total. The reaction time is 1.0 seconds and the deceleration 9.0 metres per second squared. Below, a tape measure in metres." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy411-p50" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy411-p100" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient></defs>
  <foreignObject x="16" y="11.5" width="299" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_0 = 50\,\text{km/h}:\ s_\text{stop} = 24.6\,\text{m}$</div></foreignObject>
  <rect x="16" y="90" width="568" height="24" fill="#6c757d"/>
  <line x1="16" y1="90" x2="584" y2="90" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="16" y1="114" x2="584" y2="114" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <g transform="translate(147.5,90) scale(0.32)">
  <path d="M2,-15 Q0,-41 24,-45 L62,-49 Q82,-77 112,-79 H156 Q178,-77 192,-51 L212,-45 Q226,-41 224,-15 Z" fill="url(#fy411-p50)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M72,-51 Q88,-71 110,-72 H128 V-51 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M136,-72 H154 Q170,-69 180,-51 H136 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="208" y="-39" width="14" height="8" rx="2" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="6" cy="-36" r="14" fill="#f2a69c"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="48" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="48" cy="-15" r="7" fill="#c4ccd4"/>
  <circle cx="178" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="178" cy="-15" r="7" fill="#c4ccd4"/>
  </g>
  <line x1="60" y1="48" x2="60" y2="146" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <rect x="60" y="124" width="90.5" height="12" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="150.5" y="124" width="69.5" height="12" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="88.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$s_\text{r}$</div></foreignObject>
  <foreignObject x="168.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#b8622d">$s_\text{b}$</div></foreignObject>
  <foreignObject x="16" y="181.5" width="311" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_0 = 100\,\text{km/h}:\ s_\text{stop} = 70.6\,\text{m}$</div></foreignObject>
  <rect x="16" y="260" width="568" height="24" fill="#6c757d"/>
  <line x1="16" y1="260" x2="584" y2="260" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="16" y1="284" x2="584" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <g transform="translate(447,260) scale(0.32)">
  <path d="M2,-15 Q0,-41 24,-45 L62,-49 Q82,-77 112,-79 H156 Q178,-77 192,-51 L212,-45 Q226,-41 224,-15 Z" fill="url(#fy411-p100)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M72,-51 Q88,-71 110,-72 H128 V-51 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M136,-72 H154 Q170,-69 180,-51 H136 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="208" y="-39" width="14" height="8" rx="2" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="6" cy="-36" r="14" fill="#f2a69c"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="48" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="48" cy="-15" r="7" fill="#c4ccd4"/>
  <circle cx="178" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="178" cy="-15" r="7" fill="#c4ccd4"/>
  </g>
  <line x1="60" y1="218" x2="60" y2="316" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <rect x="60" y="294" width="180.5" height="12" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="240.5" y="294" width="278.5" height="12" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="134" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$s_\text{r}$</div></foreignObject>
  <foreignObject x="363.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#b8622d">$s_\text{b}$</div></foreignObject>
  <line x1="60" y1="364" x2="547.5" y2="364" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="60" y1="364" x2="60" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="50" y="367.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <line x1="125" y1="364" x2="125" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="108.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <line x1="190" y1="364" x2="190" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="173.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$20$</div></foreignObject>
  <line x1="255" y1="364" x2="255" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="238.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$30$</div></foreignObject>
  <line x1="320" y1="364" x2="320" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="303.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$40$</div></foreignObject>
  <line x1="385" y1="364" x2="385" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="368.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$50$</div></foreignObject>
  <line x1="450" y1="364" x2="450" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="433.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$60$</div></foreignObject>
  <line x1="515" y1="364" x2="515" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="498.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$70$</div></foreignObject>
  <foreignObject x="555.5" y="367.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{m}$</div></foreignObject>
</svg>

This gives the answer to the first part of the opening question. When the speed doubles from $50\,\text{km/h}$ to $100\,\text{km/h}$, the reaction distance doubles from $13.9\,\text{m}$ to $27.8\,\text{m}$, but the braking distance quadruples from $10.7\,\text{m}$ to $42.9\,\text{m}$. The stopping distance therefore grows from $24.6\,\text{m}$ to $70.6\,\text{m}$, almost three times as long.

```pysahdy
A driver brakes to a stop from $40\,\text{km/h}$ instead of from $80\,\text{km/h}$. How does the braking distance change when the deceleration is the same?
---
It becomes one quarter. Stopping takes only half the time, and the car moves at half the speed the whole time.
```

### Same change in momentum, different collision time
If the obstacle is closer than the stopping distance, the car collides with it. In a frontal collision the front of the car crumples and the car stops in about a tenth of a second. When the passenger stops with the car, their momentum $p = mv$ changes from $mv$ to zero. For a passenger of the same mass the change in momentum is the same with and without a seat belt when they stop from the same initial velocity to the same final velocity: the initial and final velocities determine the change in momentum. In a real accident, however, the motion of a passenger without a belt does not necessarily end when the car stops, because they may, for example, be thrown through the windscreen. When the change in momentum is the same, the only thing that can be changed is how long the **collision time** $\Delta t$ is, that is, the time in which the passenger stops. In the chapter *Momentum and impulse* you learned that the change in momentum equals the impulse $\overline{I} = \overline{F}\,\Delta t$. The longer the collision time, the smaller the force needed for the same change in momentum.

<svg data-fig="tormays" viewBox="0 0 600 340" role="img" aria-label="Schematic graph, rounded example values: the speed of a passenger in a frontal collision from a speed of 50 kilometres per hour. On the horizontal axis the time 0–0.12 seconds, on the vertical axis the speed 0–16 metres per second. Blue line: a passenger wearing a belt slows down steadily with the car from 13.9 metres per second to zero in 0.10 seconds. Brown line: without a belt the passenger keeps moving at 13.9 metres per second until 0.090 seconds, hits the interior of the car and stops in 0.010 seconds. The change in speed is the same in both." style="max-width:100%;font-size:24px">
  <line x1="145" y1="290" x2="145" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="290" x2="210" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275" y1="290" x2="275" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="290" x2="340" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="290" x2="405" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="232.5" x2="470" y2="232.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="175" x2="470" y2="175" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="117.5" x2="470" y2="117.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="291" x2="80" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,34 L86,47 L74,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="145" y1="290" x2="145" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="116" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.02$</div></foreignObject>
  <line x1="210" y1="290" x2="210" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.04$</div></foreignObject>
  <line x1="275" y1="290" x2="275" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.06$</div></foreignObject>
  <line x1="340" y1="290" x2="340" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="311" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.08$</div></foreignObject>
  <line x1="405" y1="290" x2="405" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="382.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.1$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.12$</div></foreignObject>
  <line x1="73" y1="232.5" x2="80" y2="232.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="218" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="73" y1="175" x2="80" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="160.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="73" y1="117.5" x2="80" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="103" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="73" y1="60" x2="80" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$16$</div></foreignObject>
  <foreignObject x="50" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="70" y="3.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <polyline points="80,90.5 405,290" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="80,90.5 372.5,90.5 405,290" fill="none" stroke="#b8622d" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="96" y="55.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{no belt: }\Delta t = 0.010\,\text{s}$</span></div></foreignObject>
  <foreignObject x="119" y="241" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{with belt: }\Delta t = 0.10\,\text{s}$</span></div></foreignObject>
</svg>

Without a seat belt the passenger keeps moving at almost the original speed while the car slows down around them: by Newton's first law no force is yet slowing them down. They hit the steering wheel, the dashboard or the windscreen and stop in hundredths of a second. The **seat belt** fastens the passenger to the car, so they slow down together with the crumpling front of the car. The belt also stretches a little and spreads the force over the strong bones of the pelvis, chest and shoulder.

```pysahdy
The car stops in a collision. Why does a passenger without a belt keep moving forward even though nothing pushes them?
---
No force slows them down, so by Newton's first law they keep moving at their original velocity while the car stops around them.
```

<figure class="unit-photo"><img src="pics/fy4/side-impact-crash-test.webp" alt="A yellow small car in a test hall, its side pushed in and its body covered in measurement markers."><figcaption>A 2014 Chevrolet Spark after a side impact test by the US National Highway Traffic Safety Administration (NHTSA). The side of the car has been pushed in.</figcaption></figure>

The airbag inflates in hundredths of a second and catches the head and upper body. It lengthens the stopping time and spreads the force over a large area, so the pressure on the body is smaller. An airbag is designed to work together with the seat belt, not instead of it.

This is the answer to the second part of the opening question. The difference also shows in accident statistics. According to the Finnish Crash Data Institute (OTI), in the fatal accidents investigated by the road accident investigation teams in 2017–2021, 278 people wearing a seat belt and 198 people not wearing one died in cars and vans. The investigation teams estimated that 114 of those without a belt could have survived if the belt had been fastened. In Liikenneturva's monitoring, almost everyone in the front seat wears a belt.

## Formula: Stopping distance and the force of a collision

### Reaction distance and braking distance
During the reaction time the car moves at a constant speed $v_0$, so the reaction distance is
```latex
s_\text{r} = v_0\,t_\text{r}
```
where $s_\text{r}$ is the reaction distance ($\text{m}$), $v_0$ is the speed of the car before braking ($\text{m/s}$) and $t_\text{r}$ is the reaction time ($\text{s}$). In braking the deceleration is assumed to be constant, so on the $(t,v)$ graph the speed falls in a straight line to zero. As in the chapter *Acceleration and uniformly accelerated motion*, the distance travelled is the area between the graph and the time axis.

<svg data-fig="tv" viewBox="0 0 600 340" role="img" aria-label="Schematic of a (t, v) graph, no numerical values. The speed stays at the value v_0 during the reaction time t_r, so the graph is horizontal, and under it is a green rectangle whose area is the reaction distance s_r = v_0 t_r. Then the speed falls in a straight line to zero during the braking time t_b, and under the graph is a brown triangle whose area is the braking distance s_b = half of v_0 t_b. The magnitude of the slope of the line is the deceleration a." style="max-width:100%;font-size:24px">
  <line x1="196.5" y1="290" x2="196.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="453.5" y1="290" x2="453.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="121" x2="500" y2="121" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="291" x2="80" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,44 L86,57 L74,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="196.5" y1="290" x2="196.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="180" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r}$</div></foreignObject>
  <line x1="453.5" y1="290" x2="453.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="418.5" y="299.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r} + t_\text{b}$</div></foreignObject>
  <line x1="73" y1="121" x2="80" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="106.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="50" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="70" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polygon points="80,290 80,121 196.5,121 196.5,290" fill="#2b8a3e" fill-opacity="0.35"/>
  <polygon points="196.5,290 196.5,121 453.5,290" fill="#b8622d" fill-opacity="0.35"/>
  <polyline points="80,121 196.5,121 453.5,290" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="122" y="199.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s_\text{r}$</div></foreignObject>
  <foreignObject x="265.5" y="224.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s_\text{b}$</div></foreignObject>
  <foreignObject x="348" y="170.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{slope } {-a}$</div></foreignObject>
</svg>

The speed falls by $v_0$ at deceleration $a$, so the braking time is
```latex
t_\text{b} = \frac{v_0}{a}
```
where $t_\text{b}$ is the braking time ($\text{s}$) and $a$ is the deceleration, that is, the magnitude of the acceleration ($\text{m/s}^2$). The braking distance is the area of the triangle, $\tfrac{1}{2}\,v_0\,t_\text{b}$. Substituting the braking time gives
```latex
s_\text{b} = \frac{v_0^2}{2a}
```
where $s_\text{b}$ is the braking distance ($\text{m}$). The stopping distance is the sum of these:
```latex
s_\text{stop} = v_0\,t_\text{r} + \frac{v_0^2}{2a}
```
where $s_\text{stop}$ is the stopping distance ($\text{m}$). The model assumes that the road is horizontal, the deceleration is constant during braking and air resistance is neglected. The speed is substituted in $\text{m/s}$.

### Deceleration from friction
On a horizontal road the car does not accelerate vertically, so the normal force equals the weight, $N = mg$. When braking as hard as the grip allows, the friction is $F_\mu = \mu N$, where $\mu$ is the coefficient of friction between the tyres and the road. By Newton's second law $\mu mg = ma$, and the mass cancels:
```latex
a = \mu g
```
where $\mu$ is the coefficient of friction (no unit) and $g = 9.81\,\text{m/s}^2$. The $9.0\,\text{m/s}^2$ of dry asphalt corresponds to a coefficient of friction of $0.92$. In this model the braking distance does not depend on the mass of the car. The braking distance of a heavy lorry is still often longer, because its brakes and tyres cannot always use all of the grip.

### Average force in a collision
When the passenger's speed changes by $\Delta v$ in a collision in time $\Delta t$, the impulse–momentum principle $\overline{F}_\text{avg}\,\Delta t = \Delta\overline{p}$ gives the magnitude of the average force acting on them:
```latex
F_\text{avg} = \frac{m\,\Delta v}{\Delta t}
```
where $F_\text{avg}$ is the average force ($\text{N}$), $m$ is the passenger's mass ($\text{kg}$), $\Delta v$ is the magnitude of the change in speed ($\text{m/s}$) and $\Delta t$ is the collision time ($\text{s}$). When a $75\,\text{kg}$ passenger stops from $50\,\text{km/h}$, the change in momentum is about $1040\,\text{kg}\cdot\text{m/s}$. With a belt it is spread over about $0.10\,\text{s}$, and the average force is about $10\,\text{kN}$. Without a belt the time is about $0.010\,\text{s}$ and the force is ten times as large.

<svg data-fig="tF" viewBox="0 0 600 360" role="img" aria-label="Graph to scale, rounded example values for a 75 kilogram passenger from a speed of 50 kilometres per hour. On the horizontal axis the time 0–0.12 seconds, on the vertical axis the average force 0–120 kilonewtons. A low blue rectangle: with a belt the force is about 10 kilonewtons for 0.10 seconds. A narrow, tall brown rectangle: without a belt the force is about 100 kilonewtons for 0.010 seconds. The areas of the rectangles are equal." style="max-width:100%;font-size:24px">
  <line x1="145" y1="310" x2="145" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="310" x2="210" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275" y1="310" x2="275" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="310" x2="340" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="310" x2="405" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="310" x2="470" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="270" x2="470" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="230" x2="470" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="190" x2="470" y2="190" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="150" x2="470" y2="150" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="110" x2="470" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="70" x2="470" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="310" x2="484" y2="310" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,310 L483,316 L483,304 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="311" x2="80" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,44 L86,57 L74,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="145" y1="310" x2="145" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="116" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.02$</div></foreignObject>
  <line x1="210" y1="310" x2="210" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.04$</div></foreignObject>
  <line x1="275" y1="310" x2="275" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.06$</div></foreignObject>
  <line x1="340" y1="310" x2="340" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="311" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.08$</div></foreignObject>
  <line x1="405" y1="310" x2="405" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="382.5" y="319.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.1$</div></foreignObject>
  <line x1="470" y1="310" x2="470" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.12$</div></foreignObject>
  <line x1="73" y1="270" x2="80" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="73" y1="230" x2="80" y2="230" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="215.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="73" y1="190" x2="80" y2="190" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="175.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="73" y1="150" x2="80" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="73" y1="110" x2="80" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="95.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="73" y1="70" x2="80" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <foreignObject x="50" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="295.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="70" y="13.5" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\text{avg}\ (\text{kN})$</div></foreignObject>
  <polygon points="80,310 80,289 405,289 405,310" fill="#1971c2" fill-opacity="0.45"/>
  <polyline points="80,289 405,289 405,310" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polygon points="372.5,310 372.5,101.5 405,101.5 405,310" fill="#b8622d" fill-opacity="0.6"/>
  <polyline points="372.5,310 372.5,101.5 405,101.5 405,310" fill="none" stroke="#b8622d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="96" y="256.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{with belt: } F_\text{avg} \approx 10\,\text{kN}$</span></div></foreignObject>
  <foreignObject x="133" y="103.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#b8622d"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{no belt: } F_\text{avg} \approx 100\,\text{kN}$</span></div></foreignObject>
</svg>

The areas of the rectangles in the graph are equal, because each is the same change in momentum $m\,\Delta v$. In reality the force varies during the collision, and the greatest force is larger than the average.

## Worked example
A car is driving on dry asphalt at $80\,\text{km/h}$. The driver glances at their phone, and their reaction time in the dangerous situation is $2.0\,\text{s}$. The deceleration of the car in braking is $9.0\,\text{m/s}^2$. How long is the stopping distance of the car?

<!-- vaihe -->

**Given and find.** $v_0 = 80\,\text{km/h}$, $t_\text{r} = 2.0\,\text{s}$ and $a = 9.0\,\text{m/s}^2$. We are asked for the stopping distance $s_\text{stop}$.

<!-- vaihe -->

**Principle.** During the reaction time the car moves at a constant speed, so the reaction distance is speed times time. After that the car slows down at a constant deceleration, when the road is horizontal and air resistance is neglected, so the braking distance is the area of the triangle on the $(t,v)$ graph. The stopping distance is the sum of these.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&s_\text{stop} = s_\text{r} + s_\text{b} \\
&s_\text{stop} = v_0\,t_\text{r} + \frac{v_0^2}{2a}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The speed is converted to $\text{m/s}$: $80\,\text{km/h} = \tfrac{80 \cdot 1000\,\text{m}}{3600\,\text{s}} \approx 22.22\,\text{m/s}$.

<!-- vaihe -->

**Substitution.** First we calculate each partial distance and then the sum:
```latex
\begin{aligned}
&s_\text{r} = v_0\,t_\text{r} \\
&\phantom{s_\text{r}} = 22.22\,\tfrac{\text{m}}{\text{s}} \cdot 2.0\,\text{s} \\
&\phantom{s_\text{r}} = 44.44\,\text{m} \\
&s_\text{b} = \frac{(22.22\,\text{m/s})^2}{2 \cdot 9.0\,\text{m/s}^2} \\
&\phantom{s_\text{b}} = 27.43\,\text{m} \\
&s_\text{stop} = (44.44 + 27.43)\,\text{m} \\
&\phantom{s_\text{stop}} \approx 72\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Result.** The stopping distance is about $72\,\text{m}$, to two significant figures like the reaction time $2.0\,\text{s}$ and the deceleration $9.0\,\text{m/s}^2$. The reaction distance of $44\,\text{m}$ is more than half of it.

<!-- vaihe -->

**Reasonableness.** With a reaction time of $1.0\,\text{s}$ the reaction distance would be $22\,\text{m}$ and the stopping distance about $50\,\text{m}$. A glance at the phone therefore lengthens the stopping distance by about $22\,\text{m}$, about five car lengths, even though the braking distance is the same. A speed of $22\,\text{m/s}$ and a braking time of $22\,\text{m/s} : 9\,\text{m/s}^2 \approx 2.5\,\text{s}$ give a braking distance of about $\tfrac{1}{2} \cdot 22\,\text{m/s} \cdot 2.5\,\text{s} \approx 27\,\text{m}$, as in the calculation.

## Common misconception
Many people think that double the speed means double the stopping distance. The reaction distance doubles, but the braking distance quadruples, because it depends on the square of the speed. Another mistake is to think that a seat belt reduces the change in momentum. When the passenger stops from the same speed, the momentum changes from $mv$ to zero in both cases; the belt lengthens the time in which the change happens and therefore reduces the force. A third mistake is to believe that in a slow crash you can brace yourself with your hands. Even in a $50\,\text{km/h}$ collision the average force is about $10\,\text{kN}$ even with a belt, more than ten times a person's weight, and the muscle force of the hands is not enough against it.

## Summary
- The stopping distance is the reaction distance $s_\text{r} = v_0\,t_\text{r}$ plus the braking distance $s_\text{b} = \tfrac{v_0^2}{2a}$, when the deceleration is constant.
- The reaction distance is proportional to the speed and the braking distance to the square of the speed: double the speed gives four times the braking distance.
- In braking, the friction between the tyres and the road slows the car. On a horizontal road $a = \mu g$, so a slippery road multiplies the braking distance.
- When the passenger stops from the same initial velocity to the same final velocity, their change in momentum is the same with and without a belt. The seat belt and the airbag lengthen the collision time, so the average force $F_\text{avg} = \tfrac{m\,\Delta v}{\Delta t}$ is smaller.
- The airbag spreads the force over a large area and works together with the seat belt, not instead of it.
