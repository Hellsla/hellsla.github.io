# Air resistance and falling through air

> **Why** does a skydiver's speed stop increasing, even though the weight pulls the skydiver down throughout the whole fall?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: high above fields, forests and a lake, two skydivers. At the upper left a skydiver falls belly down with arms and legs spread, and lines of the airflow are seen above. At the lower right another skydiver floats slowly under an open parachute. At the top edge of the sky is the aeroplane they jumped from." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy414h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy414h-lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy414h-canopy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy414h-sky)"/>
  <path d="M0,430 Q300,404 600,418 T1200,410 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M-12,442 l120,-6 l20,40 l-130,8 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M132.5,448.5 l120,-6 l20,40 l-130,8 Z" fill="#b2f2bb" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M269,445.5 l120,-6 l20,40 l-130,8 Z" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M427,440.5 l120,-6 l20,40 l-130,8 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M558.5,441 l120,-6 l20,40 l-130,8 Z" fill="#b2f2bb" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M707,442.5 l120,-6 l20,40 l-130,8 Z" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M840.5,449.5 l120,-6 l20,40 l-130,8 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M963.5,444.5 l120,-6 l20,40 l-130,8 Z" fill="#b2f2bb" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M1125.5,440 l120,-6 l20,40 l-130,8 Z" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M760,470 Q840,446 940,462 Q1010,480 960,512 Q860,540 780,512 Q730,492 760,470 Z" fill="url(#fy414h-lake)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M0,500 L9,477.5 L18,500 L31.5,464 L44.5,500 L55.5,470 L67,500 L75,481 L83,500 L91.5,479.5 L99.5,500 L109,476 L118.5,500 L132.5,460.5 L147,500 L157.5,472.5 L168,500 L175.5,482 L183.5,500 L194.5,471 L205.5,500 L217,469.5 L228.5,500 L241,466 L253.5,500 L265.5,468 L277,500 L285,481.5 L293,500 L303.5,472.5 L314,500 L324,474.5 L334,500 L343,476.5 L352.5,500 L363.5,471.5 L374,500 L384,474.5 L394,500 L407.5,462.5 L421,500 L434,464 L447,500 L457.5,472.5 L468.5,500 L482.5,461 L496.5,500 L507,472.5 L517.5,500 L530.5,464.5 L543,500 L554,472 L564.5,500 L578.5,460.5 L592.5,500 L603,473 L613.5,500 L625,470 L636,500 L647.5,469.5 L659,500 L668,476.5 L677.5,500 L688,473 L698,500 L712.5,460.5 L726.5,500 V526 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M600,560 L612.5,531.5 L625,560 L634,542 L642.5,560 L652,539.5 L661.5,560 L671.5,538 L681.5,560 L689,544.5 L697,560 L707.5,536.5 L718,560 L727,541 L736,560 L746,537.5 L756,560 L765.5,540 L775,560 L784,541 L793,560 L804.5,534 L816,560 L825,541.5 L833.5,560 L845.5,533 L857.5,560 L869.5,532.5 L881.5,560 L894.5,530 L907.5,560 L916.5,540.5 L926,560 L935,541 L944,560 L952,544.5 L959.5,560 L968,543 L976,560 L987.5,534.5 L999,560 L1006.5,545 L1014.5,560 L1021.5,546.5 L1028.5,560 L1039.5,535.5 L1050.5,560 L1062,534.5 L1073,560 L1083,538.5 L1093,560 L1103.5,536.5 L1114.5,560 L1124,539.5 L1133.5,560 L1144,536.5 L1154.5,560 L1162,544.5 L1170,560 L1182.5,531 L1195,560 L1205,539 L1215,560 V580 H600 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="380" width="1200" height="90" fill="#eef5f9" fill-opacity="0.55"/>
  <path d="M121,352 Q119,314.5 163,319 Q180.5,279.5 224.5,292.5 Q264,270.5 286,312.5 Q325.5,317 321,352 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M919,318 Q917,287.5 953,291 Q967.5,258.5 1003.5,269.5 Q1036,251.5 1054,285.5 Q1086.5,289 1083,318 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M586,232 Q585,211.5 609,214 Q618.5,192.5 642.5,199.5 Q664,187.5 676,210.5 Q697.5,213 695,232 Z" fill="#ffffff" stroke-linejoin="round" fill-opacity="0.8"/>
  <g transform="translate(1010,70) scale(0.9)">
  <path d="M-80,0 Q-60,-14 40,-12 Q70,-10 84,0 Q70,10 40,10 L-70,8 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M-10,-6 L-34,-44 L-16,-44 L16,-6 Z" fill="#8a96a3" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M-70,-4 L-86,-30 L-74,-30 L-56,-4 Z" fill="#8a96a3" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="-40" y="-8" width="10" height="7" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="-20" y="-8" width="10" height="7" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="0" y="-8" width="10" height="7" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="20" y="-8" width="10" height="7" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="30" y="-8" width="14" height="16" rx="2" fill="#1f2933"/>
  </g>
  <line x1="330" y1="92.5" x2="330" y2="151" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="356" y1="93" x2="356" y2="153" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="382" y1="96.5" x2="382" y2="152" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="408" y1="96" x2="408" y2="166" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="434" y1="103.5" x2="434" y2="154" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <g transform="translate(400,220) scale(2.6)">
  <path d="M-22,-2 Q-34,-16 -40,-34" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M18,-4 Q26,-18 22,-34" fill="none" stroke="#2b8a3e" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-28" y="-10" width="54" height="20" rx="9" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M-24,2 Q-42,-6 -50,-26" fill="none" stroke="#2b8a3e" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M-50,-26 l-6,-6" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M14,2 Q30,-6 34,-26" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="34" cy="-28" r="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="-16" y="-18" width="30" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="36" cy="2" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M27,-3 A10,10 0 0 1 46,0 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="807.5" y1="292.5" x2="735.5" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="815" y1="292.5" x2="786" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="825" y1="292.5" x2="854" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="832.5" y1="292.5" x2="904.5" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M726,220 Q726,180 820,180 Q914,180 914,220 Z" fill="url(#fy414h-canopy)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="757.5" y1="220" x2="757.5" y2="204" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="789" y1="220" x2="789" y2="192.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="220" x2="820" y2="188" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="851" y1="220" x2="851" y2="192.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="882.5" y1="220" x2="882.5" y2="204" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <g transform="translate(820,330) scale(1.25)">
  <path d="M-5,12 L-7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M5,12 L7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-11" y="-18" width="22" height="34" rx="7" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="-8" y="-16" width="16" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M-11,-12 L-18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M11,-12 L18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="0" cy="-28" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M-10,-28 A10,10 0 0 1 10,-28 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
</svg>

## Key idea

### Air resists motion
When an object moves through air or water, it has to push the medium out of its way. The medium pushes back on the object: the object experiences **resistance of the medium**, in air **air resistance** $\overline{F}_\text{v}$. It points against the velocity of the object when the air is still. In the chapter *Weight, friction and the inclined plane*, friction resisted sliding along a surface. Air resistance is a similar resistive force, but it is caused by the surrounding air, and the object does not need to touch any solid surface. A bicycle and a car also have **rolling resistance** $\overline{F}_\text{r}$, the resistance caused by the tyres and the road, which is a different force from air resistance.

Air resistance differs from sliding friction in that it depends on speed. Air resistance does not act at all on an object that is at rest relative to the air, and it grows quickly when the speed of the object relative to the air grows. At the same speed, air resistance is greater the larger the cross-sectional area of the object and the worse the air can flow past it. At the same speed, the resistance in water is much greater than in air, because water is denser.

### The three stages of a fall
The skydiver starts from rest relative to the air (the speed of the plane is ignored), so right after the jump there is no air resistance yet. The only force is the weight, and the skydiver accelerates downward with the free-fall acceleration $g$. As the speed grows, air resistance grows. The weight stays the same, so the net force becomes smaller, and the acceleration becomes smaller with it: the speed grows more and more slowly. Finally the air resistance is equal to the weight. Then the net force is zero, the acceleration is zero and the speed stays constant, as Newton's first law says. This speed is called the **terminal velocity**.

<svg data-fig="pudotus" viewBox="0 0 600 450" role="img" aria-label="Three stages of a skydiver&#x27;s fall belly down, to scale. At the top are situation pictures and at the bottom free-body diagrams in which the skydiver is a rectangle. On the left, right after the jump: the skydiver starts from rest relative to the air, the speed is zero, the free-body diagram has only the weight G from the centre down, and the orange acceleration arrow points down. In the middle the skydiver accelerates: a blue velocity arrow down, the weight G down and the air resistance F_v from the bottom up to the bottom surface, half the length of the weight, and the acceleration arrow is shorter. On the right terminal velocity: a long velocity arrow down, the air resistance as long as the weight, and the acceleration is zero." style="max-width:100%;font-size:30px">
  <line x1="14" y1="168" x2="586" y2="168" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="200" y1="36" x2="200" y2="420" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <line x1="400" y1="36" x2="400" y2="420" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <foreignObject x="33.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{at the start}$</div></foreignObject>
  <g transform="translate(70,104) scale(0.95)">
  <path d="M-22,-2 Q-34,-16 -40,-34" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M18,-4 Q26,-18 22,-34" fill="none" stroke="#2b8a3e" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-28" y="-10" width="54" height="20" rx="9" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M-24,2 Q-42,-6 -50,-26" fill="none" stroke="#2b8a3e" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M-50,-26 l-6,-6" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M14,2 Q30,-6 34,-26" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="34" cy="-28" r="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="-16" y="-18" width="30" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="36" cy="2" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M27,-3 A10,10 0 0 1 46,0 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <foreignObject x="72.5" y="130" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$v = 0$</div></foreignObject>
  <rect x="60" y="243" width="64" height="38" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="92" y1="262" x2="92" y2="339" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M92,356 L84,338 L100,338 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="94.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="168" y1="246" x2="168" y2="306" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M161.5,295 L168,308 L174.5,295" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="148.5" y="308" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="65" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} = 0$</div></foreignObject>
  <foreignObject x="221" y="7.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{accelerating}$</div></foreignObject>
  <g transform="translate(270,104) scale(0.95)">
  <path d="M-22,-2 Q-34,-16 -40,-34" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M18,-4 Q26,-18 22,-34" fill="none" stroke="#2b8a3e" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-28" y="-10" width="54" height="20" rx="9" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M-24,2 Q-42,-6 -50,-26" fill="none" stroke="#2b8a3e" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M-50,-26 l-6,-6" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M14,2 Q30,-6 34,-26" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="34" cy="-28" r="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="-16" y="-18" width="30" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="36" cy="2" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M27,-3 A10,10 0 0 1 46,0 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="350" y1="70" x2="350" y2="114" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M343.5,103 L350,116 L356.5,103" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="368" y="75" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="260" y="243" width="64" height="38" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="292" y1="262" x2="292" y2="339" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M292,356 L284,338 L300,338 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="294.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="276" y1="328" x2="276" y2="298" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M276,281 L284,299 L268,299 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="218.5" y="310" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <line x1="368" y1="246" x2="368" y2="286" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M361.5,275 L368,288 L374.5,275" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="348.5" y="288" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="265" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} < G$</div></foreignObject>
  <foreignObject x="396" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{terminal velocity}$</div></foreignObject>
  <g transform="translate(470,104) scale(0.95)">
  <path d="M-22,-2 Q-34,-16 -40,-34" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M18,-4 Q26,-18 22,-34" fill="none" stroke="#2b8a3e" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-28" y="-10" width="54" height="20" rx="9" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M-24,2 Q-42,-6 -50,-26" fill="none" stroke="#2b8a3e" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M-50,-26 l-6,-6" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M14,2 Q30,-6 34,-26" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="34" cy="-28" r="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="-16" y="-18" width="30" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="36" cy="2" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M27,-3 A10,10 0 0 1 46,0 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="550" y1="70" x2="550" y2="148" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M543.5,137 L550,150 L556.5,137" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="568" y="92" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="460" y="243" width="64" height="38" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="492" y1="262" x2="492" y2="339" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M492,356 L484,338 L500,338 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="494.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="476" y1="375" x2="476" y2="298" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M476,281 L484,299 L468,299 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="418.5" y="357" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="522.5" y="196" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="465" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} = G$</div></foreignObject>
</svg>

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

## Formula: Equation of motion with air resistance
Air resistance is one of the forces acting on an object, so the motion follows Newton's second law. An object falling or rising through air is acted on by its weight and by air resistance:
```latex
\overline{G} + \overline{F}_\text{v} = m\overline{a}
```
where $\overline{G}$ is the weight of the object ($\text{N}$), $\overline{F}_\text{v}$ is the air resistance ($\text{N}$), $m$ is the mass of the object ($\text{kg}$) and $\overline{a}$ is its acceleration ($\text{m/s}^2$). In this chapter the magnitude of air resistance is not calculated from the speed, but it is given or deduced from the motion: at terminal velocity $F_\text{v} = G$.

### A falling and a rising object
As always, first choose the object, draw its free-body diagram and choose the positive direction, and only then write the equation. The air resistance of a falling object points up, against the weight. When the positive direction is down, $mg - F_\text{v} = ma$, so the acceleration is smaller than $g$. The air resistance of a ball thrown upward points down, in the same direction as the weight. When the positive direction is up, $-mg - F_\text{v} = ma$. The magnitude of the acceleration is then greater than $g$, and the rising ball slows down faster than without air resistance.

<svg data-fig="ylos" viewBox="0 0 600 430" role="img" aria-label="Two situations, to scale: a ball thrown straight up, when air resistance is not ignored. At the top are situation pictures and at the bottom free-body diagrams in which the ball is a rectangle. On the left the ball rises: a blue velocity arrow up. In the free-body diagram the weight G from the centre down and the air resistance F_v from the top surface down. Separately a green hollow net force arrow down, longer than the weight, and an orange acceleration arrow down. On the right the ball falls back: a velocity arrow down. In the free-body diagram the weight down and the air resistance from the bottom surface up. The net force arrow down is shorter than the weight, and the acceleration arrow is shorter than on the left." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy414-ball0" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy414-ball300" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient></defs>
  <line x1="14" y1="160" x2="586" y2="160" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="300" y1="36" x2="300" y2="420" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <foreignObject x="108.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising}$</div></foreignObject>
  <circle cx="120" cy="100" r="22" fill="url(#fy414-ball0)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M98,100 Q120,89 142,100" fill="none" stroke="#8a96a3" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M113.5,79 Q124.5,100 113.5,121" fill="none" stroke="#8a96a3" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="170" y1="120" x2="170" y2="72" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M176.5,83 L170,70 L163.5,83" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="188" y="80.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="88" y="232" width="64" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="120" y1="252" x2="120" y2="313.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M120,330.5 L112,312.5 L128,312.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="125.5" y="314" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="102" y1="200" x2="102" y2="215" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M102,232 L94,214 L110,214 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="49.5" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <line x1="200" y1="196" x2="200" y2="253" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M193.5,242 L200,255 L206.5,242" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="203.5" y="226.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M257,270 L257,358.5 L249,358.5 L262,380.5 L275,358.5 L267,358.5 L267,270 Z" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="239.5" y="390" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
  <foreignObject x="402.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{falling}$</div></foreignObject>
  <circle cx="420" cy="100" r="22" fill="url(#fy414-ball300)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M398,100 Q420,89 442,100" fill="none" stroke="#8a96a3" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M413.5,79 Q424.5,100 413.5,121" fill="none" stroke="#8a96a3" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="470" y1="70" x2="470" y2="118" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M463.5,107 L470,120 L476.5,107" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="488" y="80.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="388" y="232" width="64" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="420" y1="252" x2="420" y2="313.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M420,330.5 L412,312.5 L428,312.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="425.5" y="314" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="402" y1="304" x2="402" y2="289" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M402,272 L410,290 L394,290 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="289.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <line x1="500" y1="196" x2="500" y2="234" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M493.5,223 L500,236 L506.5,223" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="503.5" y="207.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M557,270 L557,294.5 L549,294.5 L562,316.5 L575,294.5 L567,294.5 L567,270 Z" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="539.5" y="326" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
</svg>

### When the parachute opens
The large area of the parachute makes air resistance many times greater. When the parachute opens, the skydiver is still moving downward at terminal velocity, so for a moment the air resistance is many times the weight. The net force and the acceleration point up, even though the skydiver is moving down: the skydiver slows down but does not rise. As the speed decreases, air resistance decreases until, at a new, small terminal velocity, it is again equal to the weight. How many times the weight the air resistance is depends on the parachute and the moment: in the diagram it is three times, in the example almost three times, and in the model of the simulation at most about five times. The direction of the net force can therefore differ from the direction of motion. It always tells the direction of the acceleration, not of the velocity.

<svg data-fig="varjo" viewBox="0 0 600 500" role="img" aria-label="Three stages when the parachute is opened, forces to scale. At the top are situation pictures and at the bottom free-body diagrams of the skydiver, in which the skydiver with the parachute is a rectangle. On the left falling before the parachute is opened, at terminal velocity: a long blue velocity arrow down, the weight G from the centre down and the air resistance F_v from the bottom up to the bottom surface, equally long, acceleration zero. In the middle the parachute opens: the velocity arrow still points down, the air resistance starts from the top surface and points up and is three times the length of the weight. Separately a green hollow net force arrow up and an orange acceleration arrow up. On the right the parachute is open: a short velocity arrow down, the air resistance from the top surface up as long as the weight, acceleration zero." style="max-width:100%;font-size:30px">
  <defs><linearGradient id="fy414-ch1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy414-ch2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="14" y1="200" x2="586" y2="200" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="200" y1="36" x2="200" y2="480" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <line x1="400" y1="36" x2="400" y2="480" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <foreignObject x="-4" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{terminal velocity}$</div></foreignObject>
  <g transform="translate(82,120) scale(0.95)">
  <path d="M-22,-2 Q-34,-16 -40,-34" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M18,-4 Q26,-18 22,-34" fill="none" stroke="#2b8a3e" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-28" y="-10" width="54" height="20" rx="9" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M-24,2 Q-42,-6 -50,-26" fill="none" stroke="#2b8a3e" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M-50,-26 l-6,-6" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M14,2 Q30,-6 34,-26" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="34" cy="-28" r="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="-16" y="-18" width="30" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="36" cy="2" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M27,-3 A10,10 0 0 1 46,0 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="150" y1="70" x2="150" y2="160" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M143.5,149 L150,162 L156.5,149" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="168" y="98" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="56" y="353" width="60" height="38" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="86" y1="372" x2="86" y2="402" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M86,419 L78,401 L94,401 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="88.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="70" y1="438" x2="70" y2="408" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M70,391 L78,409 L62,409 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="12.5" y="420" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="132.5" y="354" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="233.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{chute opens}$</div></foreignObject>
  <line x1="274" y1="136" x2="260.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="279" y1="136" x2="273.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="136" x2="290.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="136" x2="303.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M258,89.5 Q258,64 282,64 Q306,64 306,89.5 Z" fill="url(#fy414-ch1)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="266" y1="89.5" x2="266" y2="79.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274" y1="89.5" x2="274" y2="72" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="282" y1="89.5" x2="282" y2="69" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="89.5" x2="290" y2="72" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298" y1="89.5" x2="298" y2="79.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <g transform="translate(282,160) scale(0.8)">
  <path d="M-5,12 L-7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M5,12 L7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-11" y="-18" width="22" height="34" rx="7" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="-8" y="-16" width="16" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M-11,-12 L-18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M11,-12 L18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="0" cy="-28" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M-10,-28 A10,10 0 0 1 10,-28 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="350" y1="70" x2="350" y2="138" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M343.5,127 L350,140 L356.5,127" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="368" y="87" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="256" y="353" width="60" height="38" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="286" y1="372" x2="286" y2="402" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M286,419 L278,401 L294,401 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="288.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="270" y1="353" x2="270" y2="228.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M270,211.5 L278,229.5 L262,229.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="212.5" y="205.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <line x1="346" y1="322" x2="346" y2="268" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M352.5,279 L346,266 L339.5,279" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="346.5" y="252" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M383,470 L383,398 L391,398 L378,376 L365,398 L373,398 L373,470 Z" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="350.5" y="338" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
  <foreignObject x="415" y="7.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{new terminal v.}$</div></foreignObject>
  <line x1="474" y1="136" x2="440" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="479" y1="136" x2="465.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="485" y1="136" x2="498.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="490" y1="136" x2="524" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M435.5,89.5 Q435.5,64 482,64 Q528.5,64 528.5,89.5 Z" fill="url(#fy414-ch2)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="451" y1="89.5" x2="451" y2="79.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466.5" y1="89.5" x2="466.5" y2="72" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="482" y1="89.5" x2="482" y2="69" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="497.5" y1="89.5" x2="497.5" y2="72" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="513" y1="89.5" x2="513" y2="79.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <g transform="translate(482,160) scale(0.8)">
  <path d="M-5,12 L-7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M5,12 L7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-11" y="-18" width="22" height="34" rx="7" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="-8" y="-16" width="16" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M-11,-12 L-18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M11,-12 L18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="0" cy="-28" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M-10,-28 A10,10 0 0 1 10,-28 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="550" y1="70" x2="550" y2="84" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M543.5,73 L550,86 L556.5,73" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="568" y="60" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="456" y="353" width="60" height="38" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="486" y1="372" x2="486" y2="402" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M486,419 L478,401 L494,401 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="488.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="470" y1="353" x2="470" y2="323" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M470,306 L478,324 L462,324 Z" fill="#c92a2a" stroke-linejoin="round"/>
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
