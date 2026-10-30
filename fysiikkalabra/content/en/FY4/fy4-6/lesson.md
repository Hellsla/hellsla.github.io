# Weight, friction and the inclined plane

> **Why** does a moving box stay in place on a slanted loading ramp, but start to slide when the ramp is made a little steeper?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: moving day in the yard of an apartment building. The rear doors of a van are open, and a wooden loading ramp slopes down from the floor of the van to the ground. In the middle of the ramp there is a cardboard moving box that stays in place. Inside the van there are more boxes, and a mover is carrying one box beside the ramp. In a small picture in the sky a steeper ramp, on which the box slides down, and a blue arrow shows the direction of motion." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy46h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy46h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy46h-asf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="470" fill="url(#fy46h-sky)"/>
  <circle cx="1080" cy="90" r="64" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="1080" cy="90" r="40" fill="url(#fy46h-sun)"/>
  <path d="M201,112 Q199,74.5 243,79 Q260.5,39.5 304.5,52.5 Q344,30.5 366,72.5 Q405.5,77 401,112 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M688,76 Q686.5,49 718.5,52 Q731,23 763,33 Q792,17 808,47 Q837,50.5 833.5,76 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="40" y="120" width="470" height="350" fill="#e3dccb" stroke="#8a96a3" stroke-width="2"/>
  <rect x="70" y="150" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="90" y1="150" x2="90" y2="196" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="70" y="226" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="90" y1="226" x2="90" y2="272" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="70" y="302" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="90" y1="302" x2="90" y2="348" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="70" y="378" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="90" y1="378" x2="90" y2="424" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="142" y="150" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="162" y1="150" x2="162" y2="196" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="142" y="226" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="162" y1="226" x2="162" y2="272" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="142" y="302" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="162" y1="302" x2="162" y2="348" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="142" y="378" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="162" y1="378" x2="162" y2="424" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="214" y="150" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="234" y1="150" x2="234" y2="196" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="214" y="226" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="234" y1="226" x2="234" y2="272" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="214" y="302" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="234" y1="302" x2="234" y2="348" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="214" y="378" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="234" y1="378" x2="234" y2="424" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="286" y="150" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="306" y1="150" x2="306" y2="196" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="286" y="226" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="306" y1="226" x2="306" y2="272" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="286" y="302" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="306" y1="302" x2="306" y2="348" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="286" y="378" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="306" y1="378" x2="306" y2="424" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="358" y="150" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="378" y1="150" x2="378" y2="196" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="358" y="226" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="378" y1="226" x2="378" y2="272" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="358" y="302" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="378" y1="302" x2="378" y2="348" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="358" y="378" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="378" y1="378" x2="378" y2="424" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="430" y="150" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="450" y1="150" x2="450" y2="196" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="430" y="226" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="450" y1="226" x2="450" y2="272" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="430" y="302" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="450" y1="302" x2="450" y2="348" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="430" y="378" width="40" height="46" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="450" y1="378" x2="450" y2="424" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="40" y="112" width="470" height="12" fill="#6c757d"/>
  <path d="M500,470 L512.5,441 L525,470 L538.5,438 L552,470 L565,439.5 L578,470 L598,416.5 L618.5,470 L632.5,436.5 L646,470 L660,437 L674,470 L692.5,420.5 L711.5,470 L733,412.5 L754.5,470 L773,421 L792,470 L813.5,411 L835.5,470 L856.5,414 L877,470 L894.5,425.5 L911.5,470 L933,412.5 L954,470 L971.5,425.5 L989,470 L1004,432.5 L1019,470 L1038,420.5 L1057,470 L1074.5,425 L1091.5,470 L1108.5,427.5 L1125,470 L1137.5,441.5 L1149.5,470 L1170.5,413.5 L1191.5,470 L1213,412 L1234.5,470 V510 H500 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="1143" y="250" width="14" height="230" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1143" y="452.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1150" y="425" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1143" y="397" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1150" y="369.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1143" y="342" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1150" y="314.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1143" y="287" width="7" height="3.5" fill="#1f2933"/>
  <line x1="1150" y1="337.5" x2="1108.5" y2="310" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1150" y1="307.5" x2="1191.5" y2="280" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1150" y1="284.5" x2="1108.5" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1150" cy="261.5" r="46" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1115.5" cy="296" r="37" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1184.5" cy="291.5" r="39" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1150" cy="314.5" r="34.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="0" y="462" width="1200" height="20" fill="#b2f2bb"/>
  <rect x="0" y="480" width="1200" height="120" fill="url(#fy46h-asf)"/>
  <path d="M323.5,511 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M504,509.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M356,581.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1084,548.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M741.5,571 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1088,534 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M825.5,567 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M145,505 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1013.5,575.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M70.5,584 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M343.5,513 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M889.5,582.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M758.5,509 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M160,547.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M76,581.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M249.5,551 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M588.5,562.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M529,574.5 h22" fill="none" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="600" y="190" width="430" height="238" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="604" y="196" width="92" height="196" fill="#6c757d"/>
  <rect x="612" y="330" width="60" height="62" fill="#d9b26a" stroke="#a97a35" stroke-width="2"/>
  <rect x="648" y="268" width="44" height="62" fill="#d9b26a" stroke="#a97a35" stroke-width="2"/>
  <rect x="612" y="270" width="34" height="58" fill="#d9b26a" stroke="#a97a35" stroke-width="2"/>
  <rect x="570" y="196" width="26" height="196" rx="3" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1030" y="262" width="120" height="166" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <path d="M1040,272 H1110 Q1138,272 1142,330 H1040 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="600" y="392" width="430" height="36" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="700" y="250" width="230" height="50" fill="#d0e6fb"/>
  <rect x="700" y="250" width="230" height="50" rx="6" fill="none" stroke="#1971c2" stroke-width="2"/>
  <circle cx="700" cy="440" r="42" fill="#1f2933"/>
  <circle cx="700" cy="440" r="20" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="960" cy="440" r="42" fill="#1f2933"/>
  <circle cx="960" cy="440" r="20" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <rect x="540" y="22" width="220" height="158" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="556" y1="160" x2="744" y2="160" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <path d="M560,160 L707,75 L711.5,83 L564.5,168 Z" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M635.5,116.5 L678.5,91.5 L659.5,58.5 L616.5,83.5 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="646.5" y1="86" x2="638" y2="71" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="629.5" y1="56.5" x2="581" y2="84.5" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M581,84.5 L589.5,71.5 L596.5,83.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M210,500 L600,398 L603,409.5 L213,511.5 Z" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="245" y1="497" x2="269" y2="490.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="480" x2="334" y2="473.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375" y1="463" x2="399" y2="456.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="440" y1="446" x2="464" y2="439.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="505" y1="429" x2="529" y2="422.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M376.5,456.5 L469.5,432 L450,358.5 L357,383 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="412.5" y1="404" x2="403.5" y2="371" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <path d="M116.5,540 L122,405 H158 L163.5,540 H145.5 L140,450 L134.5,540 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M109.5,414 Q106,315 140,309.5 Q174,315 170.5,414 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M113,327.5 L104,414" fill="none" stroke="#c92a2a" stroke-width="19.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="104" cy="421" r="9.9" fill="#f1dfb5"/>
  <path d="M167,327.5 L176,414" fill="none" stroke="#c92a2a" stroke-width="19.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="176" cy="421" r="9.9" fill="#f1dfb5"/>
  <rect x="132" y="291.5" width="16" height="21.5" fill="#f1dfb5"/>
  <circle cx="140" cy="273.5" r="27" fill="#f1dfb5"/>
  <path d="M112,273.5 Q113,241 140,243 Q169,243 168,270 Q145.5,259 112,273.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="100" y="400" width="82" height="64" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="141" y1="400" x2="141" y2="430" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
</svg>

## Key idea

### Weight
The **weight** $\overline{G}$ of an object is the force with which the Earth pulls the object. It always points straight down, also on a slope, and in a free-body diagram it is drawn from the center of the object. The magnitude of the weight is the product of the mass and the acceleration of free fall, $mg$. Mass describes the inertia of an object, that is how hard it is to change its state of motion, and it is the same everywhere. Weight, on the other hand, depends on the place: on the surface of the Moon $g = 1.62\,\text{m/s}^2$, so the weight of a $60\,\text{kg}$ person there is about $97\,\text{N}$, whereas on Earth it is about $590\,\text{N}$.

### Static friction and kinetic friction
When two surfaces touch each other, they resist sliding relative to each other. This force parallel to the surface is **friction** $\overline{F}_\mu$. The surfaces are not perfectly smooth: tiny bumps catch on each other, and there are attractive forces between the particles of the surfaces. The harder the surfaces are pressed against each other, that is the greater the normal force $N$ is, the greater the friction can be.

When a box on a floor is pulled only weakly, it does not move. Then **static friction** acts on it, equal to the pull and in the opposite direction, so the net force is zero. Static friction is therefore not constant but adapts to the situation. It does have an upper limit, though. When the pull exceeds it, the box starts to slide, and the friction changes into **kinetic friction**. Kinetic friction is usually smaller than the greatest static friction, and at ordinary speeds it is approximately constant.

<svg data-fig="kitka" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: on the horizontal axis the horizontal force F pulling the box in newtons from zero to 80, on the vertical axis the friction force of the floor in newtons from zero to 60. A normal force of 100 newtons presses the box against the floor. At first the friction force grows equal to the pull: a straight line rises from the origin to the point where the pull and the friction are 50 newtons. This is the greatest value of static friction, mu zero times N. There the box starts to move, and the friction force drops along a dashed line to 35 newtons, mu times N, and stays there as the pull grows." style="max-width:100%;font-size:24px">
  <line x1="193" y1="300" x2="193" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="294" y1="300" x2="294" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="300" x2="395" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496" y1="300" x2="496" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="261.5" x2="496" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="223.5" x2="496" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="185" x2="496" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="146.5" x2="496" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="108.5" x2="496" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="70" x2="496" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="510" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M522,300 L509,306 L509,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,44 L98,57 L86,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="193" y1="300" x2="193" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="294" y1="300" x2="294" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="277.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="395" y1="300" x2="395" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="378.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="496" y1="300" x2="496" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="85" y1="261.5" x2="92" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="247" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="223.5" x2="92" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="185" x2="92" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="170.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="85" y1="146.5" x2="92" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="132" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="85" y1="108.5" x2="92" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="94" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="85" y1="70" x2="92" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="55.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <foreignObject x="82" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\mu\ (\text{N})$</div></foreignObject>
  <polyline points="92,300 344.5,108.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="344.5" y1="108.5" x2="344.5" y2="166" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <polyline points="344.5,166 496,166" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="344.5" cy="108.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="107" y="170.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{static friction}$</div></foreignObject>
  <foreignObject x="370" y="124.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{kinetic friction}$</div></foreignObject>
  <foreignObject x="279.5" y="71" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\mu_0 N$</div></foreignObject>
  <foreignObject x="419" y="174.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\mu N$</div></foreignObject>
</svg>

In the graph the normal force of the floor is $100\,\text{N}$. Static friction grows with the pull up to $50\,\text{N}$, where the box starts to move. A sliding box is acted on by a kinetic friction of $35\,\text{N}$, even if the pull is increased. This is why a heavy cabinet is hardest to get moving, and once it is moving it goes more easily.

### The inclined plane
On an inclined plane, that is a slope, the weight still points straight down, but the surface is slanted. The normal force is perpendicular to the surface, and the friction is parallel to the surface. For calculation the weight is split into two **components**: the component along the slope tends to take the object down the slope, and the component perpendicular to the surface presses the object against the surface. The components are not new forces. They replace the weight in the calculation, and in a free-body diagram they are drawn as dashed lines.

<svg data-fig="kalteva-ydin" viewBox="0 0 600 380" role="img" aria-label="Two pictures. On the left a snapshot: a box is at rest on a wooden plank that rises to the right at an angle alpha to the horizontal. On the right the free-body diagram of the box, the box tilted as a rectangle like on the plank: the weight G from the center straight down, the normal force N from the lower surface perpendicular to the surface, outward, and the static friction from the upper corner of the lower surface parallel to the surface, up the slope. The components of the weight are drawn dashed from the center: G x down the slope and G y perpendicular to the surface, toward it. The angle between the weight and the component G y is alpha. The component G y is as long as the normal force and G x as long as the friction force." style="max-width:100%;font-size:24px">
  <foreignObject x="76" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{snapshot}$</div></foreignObject>
  <rect x="214" y="172" width="30" height="128" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="12" y1="312" x2="262" y2="312" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="12" y1="312" x2="2" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="28" y1="312" x2="18" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="44" y1="312" x2="34" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="312" x2="50" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="76" y1="312" x2="66" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="312" x2="82" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="108" y1="312" x2="98" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="124" y1="312" x2="114" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="312" x2="130" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="156" y1="312" x2="146" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="172" y1="312" x2="162" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="188" y1="312" x2="178" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="204" y1="312" x2="194" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220" y1="312" x2="210" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="312" x2="226" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="252" y1="312" x2="242" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M22,300 L213.5,139.5 L221,148.5 L29.5,309 Z" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M95,239 L148.5,194 L115,154 L61.5,199 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="103" y1="194.5" x2="88" y2="176.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <path d="M78,300 A56,56 0 0 0 65,264" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="81.5" y="260" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <line x1="22" y1="300" x2="102" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="270" y1="20" x2="270" y2="360" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="336" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <rect x="382" y="136" width="96" height="64" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-40 430 168)"/>
  <line x1="430" y1="168" x2="430" y2="281" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M430,298 L422,280 L438,280 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="399.5" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="464.5" y1="181" x2="411.5" y2="117.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M400.5,104.5 L418,113 L405.5,123.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="374" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="487.5" y1="161.5" x2="538.5" y2="119" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M551.5,108 L543,125.5 L532.5,113.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="547" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="430" y1="168" x2="367.5" y2="220.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M372,208.5 L366,221.5 L380,218.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="321.5" y="213" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="430" y1="168" x2="492.5" y2="243" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M480.5,238.5 L494,244.5 L490.5,230" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="497.5" y="234" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <path d="M430,212 A44,44 0 0 0 458.5,201.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="440" y="208" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
</svg>

The steeper the slope, the greater the component along the slope and the smaller the perpendicular component. When only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction, the normal force decreases together with the perpendicular component, and with it the upper limit of static friction. This is why a box starts to slide on a steep slope: the component pulling it down the slope grows greater than the greatest static friction that the ramp can give.

### Friction does not always oppose motion
Friction opposes the sliding of surfaces **relative to each other**, not necessarily the motion of the object. When a pickup truck starts to move with an acceleration, a box on its bed accelerates along with it. When air drag is ignored, the only horizontal force on the box is the friction of the bed, so it must point forward, in the direction of motion: the bed tends to slide forward from under the box, and static friction prevents this. Likewise, when we walk, the foot pushes the ground backward, and the static friction of the ground pushes the foot forward. On mirror-smooth ice, where there is very little friction, getting started is therefore difficult.

<svg data-fig="kuorma" viewBox="0 0 600 360" role="img" aria-label="Two pictures. On the left a snapshot: a pickup truck starts moving to the right and accelerates, and on its bed there is a box that does not slide on the bed. Above the box a thin orange arrow a points to the right. On the right the free-body diagram of the box as a rectangle: the weight G from the center down, the normal force N of the bed from the lower surface up and as long as the weight, and the friction force of the bed from the front corner of the lower surface to the right, that is in the direction of motion. The friction force is much shorter than the weight." style="max-width:100%;font-size:24px">
  <foreignObject x="96" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{snapshot}$</div></foreignObject>
  <line x1="14" y1="268" x2="286" y2="268" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="14" y1="268" x2="4" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="30" y1="268" x2="20" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="46" y1="268" x2="36" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="268" x2="52" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="78" y1="268" x2="68" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="94" y1="268" x2="84" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="268" x2="100" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="126" y1="268" x2="116" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="142" y1="268" x2="132" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="158" y1="268" x2="148" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="174" y1="268" x2="164" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="190" y1="268" x2="180" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="206" y1="268" x2="196" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="222" y1="268" x2="212" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="238" y1="268" x2="228" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="254" y1="268" x2="244" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="268" x2="260" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M30,200 H196 V160 Q200,146 214,146 H246 Q262,148 270,176 L282,200 V236 H30 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M206,156 H240 Q252,158 258,186 H206 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="196" y1="200" x2="196" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="76" cy="246" r="21" fill="#1f2933"/>
  <circle cx="76" cy="246" r="9" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="232" cy="246" r="21" fill="#1f2933"/>
  <circle cx="232" cy="246" r="9" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="84" y="150" width="70" height="50" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="119" y1="150" x2="119" y2="172" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="84" y1="112" x2="152" y2="112" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M141,118.5 L154,112 L141,105.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="159.5" y="93.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="340" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="346" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <rect x="365" y="154" width="90" height="64" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="410" y1="186" x2="410" y2="310.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M410,327.5 L402,309.5 L418,309.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="415.5" y="309" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="390" y1="218" x2="390" y2="93.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M390,76.5 L398,94.5 L382,94.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="68" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="455" y1="218" x2="467" y2="218" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M484,218 L466,226 L466,210 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="465.5" y="225.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="489" y1="156" x2="547" y2="156" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M536,162.5 L549,156 L536,149.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="554.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

Besides friction, other contact forces can act on an object. **Buoyancy** is the force with which a liquid or a gas pushes upward an object immersed in it, and the **drag of the medium** is the force with which air or water opposes the motion of an object. Air drag is treated in more detail in the chapter *Air drag and falling in air*. In this chapter air drag and buoyancy are ignored.

## Formula: The friction force and the inclined plane
The magnitude of the weight is
```latex
G = mg
```
where $G$ is the weight (N), $m$ the mass (kg) and $g$ the acceleration of free fall, $9.81\,\text{m/s}^2$ on the surface of the Earth.

Kinetic friction is proportional to the normal force:
```latex
F_\mu = \mu N
```
where $F_\mu$ is the magnitude of the kinetic friction (N), $\mu$ the **coefficient of kinetic friction** (no unit) and $N$ the magnitude of the normal force (N). Static friction is at most the product of the normal force and the **coefficient of static friction** $\mu_0$:
```latex
F_{\mu 0} \le \mu_0 N
```
where $F_{\mu 0}$ is the magnitude of the static friction (N). The coefficients of friction depend on the materials and the condition of the surfaces, and usually $\mu < \mu_0$. The formulas are empirical models that describe dry surfaces well. In them the friction does not depend on the area of contact or on the sliding speed.

On an inclined plane whose angle of inclination is $\alpha$, the $x$-axis is chosen along the slope and the $y$-axis perpendicular to the surface. The components of the weight are
```latex
\begin{aligned}
G_x &= G\sin\alpha \\
G_y &= G\cos\alpha
\end{aligned}
```
where $G_x$ is the component along the slope (N) and $G_y$ the component perpendicular to the surface (N). The angle between the weight and the component $G_y$ is the same $\alpha$ as the angle of inclination of the slope, because each is perpendicular to its counterpart: the weight to the horizontal and $G_y$ to the slope.

<svg data-fig="kalteva" viewBox="0 0 600 380" role="img" aria-label="Two pictures. On the left a snapshot: a box is at rest on a wooden plank that rises to the right at an angle alpha to the horizontal. On the right the free-body diagram of the box, the box tilted as a rectangle like on the plank: the weight G from the center straight down, the normal force N from the lower surface perpendicular to the surface, outward, and the static friction from the upper corner of the lower surface parallel to the surface, up the slope. The components of the weight are drawn dashed from the center: G x down the slope and G y perpendicular to the surface, toward it. The angle between the weight and the component G y is alpha. The component G y is as long as the normal force and G x as long as the friction force." style="max-width:100%;font-size:24px">
  <foreignObject x="76" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{snapshot}$</div></foreignObject>
  <rect x="214" y="172" width="30" height="128" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="12" y1="312" x2="262" y2="312" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="12" y1="312" x2="2" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="28" y1="312" x2="18" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="44" y1="312" x2="34" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="312" x2="50" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="76" y1="312" x2="66" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="312" x2="82" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="108" y1="312" x2="98" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="124" y1="312" x2="114" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="312" x2="130" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="156" y1="312" x2="146" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="172" y1="312" x2="162" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="188" y1="312" x2="178" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="204" y1="312" x2="194" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220" y1="312" x2="210" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="312" x2="226" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="252" y1="312" x2="242" y2="324" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M22,300 L238.5,175 L244.5,185.5 L28,310.5 Z" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M104.5,252.5 L165,217.5 L139,172.5 L78.5,207.5 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="120.5" y1="210" x2="108.5" y2="190" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <path d="M78,300 A56,56 0 0 0 70.5,272" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="83.5" y="266.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <line x1="22" y1="300" x2="102" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="270" y1="20" x2="270" y2="360" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="336" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <rect x="382" y="136" width="96" height="64" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-30 430 168)"/>
  <line x1="430" y1="168" x2="430" y2="281" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M430,298 L422,280 L438,280 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="399.5" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="461.5" y1="186.5" x2="414" y2="104" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M405.5,89 L421.5,101 L407.5,109 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="379" y="62.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="487.5" y1="171.5" x2="529" y2="147.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M544,139 L532.5,155 L524,141 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="539.5" y="130.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="430" y1="168" x2="375.5" y2="199.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M381.5,188.5 L373.5,200.5 L388,199.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="329" y="192" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="430" y1="168" x2="485.5" y2="264" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M474,257.5 L486.5,265.5 L485.5,251" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="490" y="255" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <path d="M430,212 A44,44 0 0 0 452,206" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="435" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
</svg>

If only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction, the normal force equals $G_y$: $N = mg\cos\alpha$, which is less than the weight. (A pulling or pushing force directed toward or away from the surface would change the normal force.) The static friction acting on an object at rest equals $G_x$. The object stays in place as long as $mg\sin\alpha \le \mu_0\,mg\cos\alpha$, that is $\tan\alpha \le \mu_0$. The mass cancels, so according to this model a heavy and a light box start to slide on the same surface at the same angle.

### Determining the coefficient of friction
In the diagrams and in the simulation, the static friction acting on an object at rest is denoted $\overline{F}_\mu$; its magnitude is $F_{\mu 0} \le \mu_0 N$, and while sliding $F_\mu = \mu N$.

The coefficient of static friction is obtained from an experiment in which a board is tilted slowly until the object starts to slide. At this limiting angle $\alpha_0$ the static friction is at its greatest, so $\mu_0 = \tan\alpha_0$. The coefficient of kinetic friction is obtained for example by pulling the object on a horizontal table with a spring balance, horizontally and at a constant velocity. Then the pull equals the kinetic friction and the normal force equals the weight, so $\mu = F : mg$. When the measurement is repeated with different masses, the coefficient of friction is the slope of the straight line through the origin fitted to the $(N, F_\mu)$ graph.

## Worked example
A moving box of mass $18\,\text{kg}$ slides down a loading ramp. The ramp is at an angle of $25^\circ$ to the horizontal, and the coefficient of kinetic friction between the box and the ramp is $0.30$. How large is the acceleration of the box, and how large is the friction force? Air drag is ignored.

<!-- vaihe -->

**Given and asked.** $m = 18\,\text{kg}$, $\alpha = 25^\circ$, $\mu = 0.30$ and $g = 9.81\,\text{m/s}^2$. The acceleration $a$ and the friction force $F_\mu$ are asked.

<!-- vaihe -->

**Principle.** The box is chosen as the object. The Earth (weight) and the ramp (normal force and kinetic friction) act on it. The box slides down, so the kinetic friction points up the slope. Newton's second law is written along the slope, where the box accelerates, and perpendicular to the surface, where it does not accelerate: $a_y = 0$.

<!-- vaihe -->

**Free-body diagram.** The box is drawn as a rectangle along the slope, and the forces start from their points of application. The axes are chosen so that $x$ points down the slope, that is in the direction of the acceleration, and $y$ perpendicular to the surface, outward. The weight is split into the components $G_x = mg\sin\alpha$ and $G_y = mg\cos\alpha$, drawn with a dashed line.

<svg data-fig="esimerkki" viewBox="0 0 600 420" role="img" aria-label="Free-body diagram of a box, the box as a rectangle tilted along a 25 degree slope. The weight G from the center straight down. The normal force N from the lower surface perpendicular to the surface, outward. The kinetic friction from the upper corner of the lower surface up the slope, because the box slides down. The components of the weight dashed from the center: G x down the slope and G y perpendicular to the surface, toward it. G x is longer than the friction force. Separately a thin orange acceleration arrow a down the slope. In the corner the axes: x down the slope and y perpendicular to the surface, outward." style="max-width:100%;font-size:24px">
  <rect x="235" y="132" width="130" height="76" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-25 300 170)"/>
  <line x1="300" y1="170" x2="300" y2="321" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,338 L292,320 L308,320 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="267.5" y="341.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="332.5" y1="197" x2="275.5" y2="74.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M268,59 L283,72 L268.5,79 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="239.5" y="32.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="375" y1="177" x2="401" y2="165" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M416.5,157.5 L403.5,172.5 L396.5,158 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="412" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="300" y1="170" x2="237.5" y2="199" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M245,188.5 L235.5,200 L250.5,200.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="193" y="195.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="300" y1="170" x2="363.5" y2="306" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M353,299 L364.5,308 L364.5,293.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="370" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <line x1="120" y1="120" x2="58.5" y2="148.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M65.5,138 L56.5,149.5 L71,150" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="20" y="140.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M300,230 A60,60 0 0 0 325.5,224.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="295.5" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25^\circ$</div></foreignObject>
  <line x1="520" y1="330" x2="486.5" y2="345.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M478.5,349.5 L485.5,341 L489.5,349.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="520" y1="330" x2="504.5" y2="296.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M500.5,288.5 L509,295.5 L500.5,299.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="455.5" y="341" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="484.5" y="261" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**The formula solved.** The equations of motion are read from the diagram and the asked quantities are solved:
```latex
\begin{aligned}
&x\text{:}\ \ mg\sin\alpha - \mu N = ma \\
&y\text{:}\ \ N - mg\cos\alpha = 0 \\
&F_\mu = \mu mg\cos\alpha \\
&a = g(\sin\alpha - \mu\cos\alpha)
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: all quantities are in SI units, and the coefficient of friction has no unit.

<!-- vaihe -->

**Substitution.** The numerical values are substituted with their units:
```latex
\begin{aligned}
&F_\mu = \mu mg\cos\alpha \\
&\phantom{F_\mu} = 0.30\cdot 18\,\text{kg} \\
&\quad\ \cdot 9.81\,\text{m/s}^2\cdot\cos 25^\circ \\
&\phantom{F_\mu} \approx 48.0\,\text{N} \\[4pt]
&a = g(\sin\alpha - \mu\cos\alpha) \\
&\phantom{a} = 9.81\,\text{m/s}^2 \\
&\quad\ \cdot(\sin 25^\circ - 0.30\cdot\cos 25^\circ) \\
&\phantom{a} \approx 1.48\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration of the box is $a \approx 1.5\,\text{m/s}^2$ down the slope and the friction force is $F_\mu \approx 48\,\text{N}$, to two significant figures like the data $\mu = 0.30$ and $m = 18\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** Without friction the acceleration would be $g\sin 25^\circ \approx 4.1\,\text{m/s}^2$, so friction reduces it, as it should. The friction force $48\,\text{N}$ is less than the component along the slope $G_x \approx 75\,\text{N}$, so the net force points down the slope and the box accelerates down. The mass does not affect the acceleration, because both $G_x$ and $F_\mu$ are proportional to the mass.

## Common misconception
Many people think that the friction force is always $\mu_0 N$ or $\mu N$ and always against the motion. Static friction, however, is only as large as the situation requires: if a box is pushed with a force of $20\,\text{N}$ and it does not move, the static friction is $20\,\text{N}$, even if its upper limit is greater. Friction opposes the sliding of surfaces relative to each other, so it can also point in the direction of motion, as on the bed of an accelerating truck. Another common mistake is to take the normal force to be always equal to the weight. On a slope $N = mg\cos\alpha$ is less than the weight, when only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction, and the weight still points straight down and not perpendicular to the slope.

## Summary
- The magnitude of the weight is $G = mg$, and the weight always points straight down. Mass is the same everywhere, but weight depends on the acceleration of free fall.
- Friction is parallel to the surface and opposes the sliding of surfaces relative to each other, not always the motion of the object.
- Static friction adapts to the situation: $F_{\mu 0} \le \mu_0 N$. A sliding object is acted on by kinetic friction $F_\mu = \mu N$, and usually $\mu < \mu_0$.
- On a slope the weight is split into the components $G_x = mg\sin\alpha$ and $G_y = mg\cos\alpha$, and the normal force is $N = mg\cos\alpha$, when only the weight and the normal force act perpendicular to the surface and the object does not accelerate in that direction. The components are drawn as dashed lines, and they are not new forces.
- The coefficient of static friction is obtained from the limiting angle at which the object starts to slide: $\mu_0 = \tan\alpha_0$.
