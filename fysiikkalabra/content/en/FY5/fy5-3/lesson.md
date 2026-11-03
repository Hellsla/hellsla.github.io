# Moving in a circle: period and speed

> **Why** does a child standing at the edge of a roundabout rush along much faster than a child standing next to the centre pole, even though both complete a turn equally fast?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a playground roundabout turning on a summer day. One child stands at the edge of the roundabout, another near the centre pole. At each child there is a blue arrow in the direction of motion, along the tangent of the path; the arrow of the child at the edge is twice as long as that of the child near the centre." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy53h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy53h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy53h-grass" gradientUnits="userSpaceOnUse" x1="0" y1="380" x2="0" y2="600"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy53h-sky)"/>
  <circle cx="1040" cy="110" r="80" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M1098,133 L1124,132.5 L1101.5,119.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1079,159 L1101.5,171.5 L1089,149 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1049.5,171.5 L1062.5,194 L1063,168 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1017,168 L1017.5,194 L1030.5,171.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M991,149 L978.5,171.5 L1001,159 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M978.5,119.5 L956,132.5 L982,133 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M982,87 L956,87.5 L978.5,100.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1001,61 L978.5,48.5 L991,71 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1030.5,48.5 L1017.5,26 L1017,52 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1063,52 L1062.5,26 L1049.5,48.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1089,71 L1101.5,48.5 L1079,61 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1101.5,100.5 L1124,87.5 L1098,87 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="1040" cy="110" r="50" fill="url(#fy53h-sun)"/>
  <path d="M160,130 Q158,96 198,100 Q214,64 254,76 Q290,56 310,94 Q346,98 342,130 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M688,96 Q686.5,69 718.5,72 Q731,43 763,53 Q792,37 808,67 Q837,70.5 833.5,96 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,330 Q100,306 200,328.5 Q300,300.5 400,329.5 Q500,305 600,328.5 Q700,283 800,333 Q900,293.5 1000,331 Q1100,283 1200,333 Q1300,291 1400,331.5 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <rect x="0" y="380" width="1200" height="220" fill="url(#fy53h-grass)"/>
  <rect x="73" y="190" width="14" height="230" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="73" y="392.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="80" y="365" width="7" height="3.5" fill="#1f2933"/>
  <rect x="73" y="337" width="7" height="3.5" fill="#1f2933"/>
  <rect x="80" y="309.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="73" y="282" width="7" height="3.5" fill="#1f2933"/>
  <rect x="80" y="254.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="73" y="227" width="7" height="3.5" fill="#1f2933"/>
  <line x1="80" y1="277.5" x2="38.5" y2="250" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="80" y1="247.5" x2="121.5" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="80" y1="224.5" x2="38.5" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="80" cy="201.5" r="46" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="45.5" cy="236" r="37" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="114.5" cy="231.5" r="39" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="80" cy="254.5" r="34.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="164.5" y="240" width="11" height="180" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="164.5" y="398.5" width="5.5" height="2.5" fill="#1f2933"/>
  <rect x="170" y="377" width="5.5" height="2.5" fill="#1f2933"/>
  <rect x="164.5" y="355" width="5.5" height="2.5" fill="#1f2933"/>
  <rect x="170" y="333.5" width="5.5" height="2.5" fill="#1f2933"/>
  <rect x="164.5" y="312" width="5.5" height="2.5" fill="#1f2933"/>
  <rect x="170" y="290.5" width="5.5" height="2.5" fill="#1f2933"/>
  <rect x="164.5" y="269" width="5.5" height="2.5" fill="#1f2933"/>
  <line x1="170" y1="308.5" x2="137.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="170" y1="285" x2="202.5" y2="263.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="170" y1="267" x2="137.5" y2="245.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="170" cy="249" r="36" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="143" cy="276" r="29" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="197" cy="272.5" r="30.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="170" cy="290.5" r="27" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="1103" y="180" width="14.5" height="240" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1103" y="391" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1110" y="362.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1103" y="333.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1110" y="305" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1103" y="276" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1110" y="247" width="7" height="3.5" fill="#1f2933"/>
  <rect x="1103" y="218.5" width="7" height="3.5" fill="#1f2933"/>
  <line x1="1110" y1="271" x2="1067" y2="242.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1110" y1="240" x2="1153" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1110" y1="216" x2="1067" y2="187" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1110" cy="192" r="48" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1074" cy="228" r="38.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1146" cy="223" r="41" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1110" cy="247" r="36" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="1025" y="250" width="10" height="170" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1025" y="399.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1030" y="379" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1025" y="359" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1030" y="338.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1025" y="318" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1030" y="297.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1025" y="277" width="5" height="2.5" fill="#1f2933"/>
  <line x1="1030" y1="314.5" x2="999.5" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1030" y1="292.5" x2="1060.5" y2="272" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1030" y1="275.5" x2="999.5" y2="255" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1030" cy="258.5" r="34" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1004.5" cy="284" r="27" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1055.5" cy="280.5" r="29" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1030" cy="297.5" r="25.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <ellipse cx="600" cy="470" rx="420" ry="110" fill="#f1dfb5"/>
  <ellipse cx="600" cy="470" rx="420" ry="110" fill="none" stroke="#d9b26a" stroke-width="3"/>
  <ellipse cx="600" cy="462" rx="330" ry="92" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="270" y="440" width="660" height="22" fill="#8a96a3"/>
  <ellipse cx="600" cy="440" rx="330" ry="92" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <ellipse cx="600" cy="440" rx="165" ry="46" fill="none" stroke="#8a96a3" stroke-width="2.5"/>
  <line x1="752.5" y1="457.5" x2="905" y2="475" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="663" y1="482.5" x2="726.5" y2="525" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="537" y1="482.5" x2="473.5" y2="525" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="447.5" y1="457.5" x2="295" y2="475" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="447.5" y1="422.5" x2="295" y2="405" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="537" y1="397.5" x2="473.5" y2="355" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="663" y1="397.5" x2="726.5" y2="355" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="752.5" y1="422.5" x2="905" y2="405" stroke="#8a96a3" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M265.5,403.5 L277.5,395 L291.5,387 L308.5,379 L327.5,372 L348.5,365 L371,359 L396,353 L422,348 L449.5,344 L478,340.5" fill="none" stroke="#ffffff" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <path d="M778,348 L804,353 L829,359 L851.5,365 L872.5,372 L891.5,379 L908.5,387 L922.5,395 L934.5,403.5 L944,412.5 L950.5,421.5" fill="none" stroke="#ffffff" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <line x1="600" y1="250" x2="863" y2="412.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="863" y1="412.5" x2="863" y2="482.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="600" y1="250" x2="600" y2="454.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="600" y1="454.5" x2="600" y2="524.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="600" y1="250" x2="337" y2="412.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="337" y1="412.5" x2="337" y2="482.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="600" y1="250" x2="337" y2="327.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="337" y1="327.5" x2="337" y2="397.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="600" y1="250" x2="600" y2="285.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="600" y1="285.5" x2="600" y2="355.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="600" y1="250" x2="863" y2="327.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <line x1="863" y1="327.5" x2="863" y2="397.5" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>
  <rect x="590" y="244" width="20" height="196" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="600" cy="244" r="16" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M461,427 L463.5,358 H482 L485,427 H475.5 L473,381 L470,427 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M457,362.5 Q455.5,312 473,309.5 Q490.5,312 488.5,362.5 Z" fill="#e9c98a" stroke-linejoin="round"/>
  <path d="M459,318.5 L454.5,362.5" fill="none" stroke="#e9c98a" stroke-width="10.12" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="454.5" cy="366.5" r="5.06" fill="#f1dfb5"/>
  <path d="M486.5,318.5 L491.5,362.5" fill="none" stroke="#e9c98a" stroke-width="10.12" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="491.5" cy="366.5" r="5.06" fill="#f1dfb5"/>
  <rect x="468.5" y="300" width="8.5" height="11" fill="#f1dfb5"/>
  <circle cx="473" cy="291" r="13.8" fill="#f1dfb5"/>
  <path d="M458.5,291 Q459,274.5 473,275.5 Q487.5,275.5 487,289 Q475.5,283.5 458.5,291 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M760.5,498 L763.5,420 H784.5 L787.5,498 H777 L774,446 L771,498 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M756.5,425 Q754,368 774,364.5 Q793.5,368 791.5,425 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M758.5,375 L753,425" fill="none" stroke="#2b8a3e" stroke-width="11.44" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="753" cy="429" r="5.72" fill="#f1dfb5"/>
  <path d="M789.5,375 L794.5,425" fill="none" stroke="#2b8a3e" stroke-width="11.44" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="794.5" cy="429" r="5.72" fill="#f1dfb5"/>
  <rect x="769.5" y="354.5" width="9.5" height="12.5" fill="#f1dfb5"/>
  <circle cx="774" cy="344" r="15.6" fill="#f1dfb5"/>
  <path d="M758,344 Q758.5,325 774,326 Q790.5,326 790,342 Q777,335.5 758,344 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M743.5,419 L581.5,456.5 L579.5,448 L559.5,468 L586.5,477 L584.5,468.5 L746,430.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M500.5,333.5 L556.5,290.5 L562,297.5 L572,271 L544,274 L549.5,281 L493,324 Z" fill="#1971c2" stroke-linejoin="round"/>
</svg>

## Key idea
An object is in **circular motion** when its path is a circle: the object stays at the same distance from the centre of the path all the time. This distance is the radius $r$ of the path. A child on a roundabout, a car going round a roundabout and a satellite orbiting the Earth are in circular motion, or almost. If an object travels the same distance in every equal time interval, the magnitude of its velocity, that is, its speed, stays the same. The motion is then **uniform circular motion**. In this chapter we look only at uniform circular motion.

### The velocity points along the tangent
Velocity is a vector $\overline{v}$ with a magnitude and a direction. At every moment the velocity points in the direction in which the object is just then moving. On a circular path this direction is the direction of the **tangent** of the path, which is perpendicular to the radius drawn from the centre. As the object goes round, the direction of the tangent turns all the time. In uniform circular motion the velocity vectors are therefore all equally long but point in different directions: the magnitude of the velocity stays the same, but the velocity changes.

<svg data-fig="tangent" viewBox="0 0 600 380" role="img" aria-label="Formula figure: an object circles a circular path anticlockwise. A blue velocity vector is drawn at four points: all are equally long and along the tangent of the path, perpendicular to the radius drawn from the centre. On the right it says that the magnitudes of the velocities are equal but the vectors are different." style="max-width:100%;font-size:24px">
  <path d="M292,192 L291.5,183.5 L291,175.5 L289.5,167 L287.5,159 L285,151 L281.5,143 L278,135.5 L274,128.5 L269,121.5 L264,115 L258.5,108.5 L252.5,103 L246,97.5 L239,92.5 L232,88 L224.5,84 L217,80.5 L209,78 L201,75.5 L193,74 L184.5,72.5 L176,72 L168,72 L159.5,72.5 L151,74 L143,75.5 L135,78 L127,80.5 L119.5,84 L112,88 L105,92.5 L98,97.5 L91.5,103 L85.5,108.5 L80,115 L75,121.5 L70,128.5 L66,135.5 L62.5,143 L59,151 L56.5,159 L54.5,167 L53,175.5 L52.5,183.5 L52,192 L52.5,200.5 L53,208.5 L54.5,217 L56.5,225 L59,233 L62.5,241 L66,248.5 L70,255.5 L75,262.5 L80,269 L85.5,275.5 L91.5,281 L98,286.5 L105,291.5 L112,296 L119.5,300 L127,303.5 L135,306 L143,308.5 L151,310 L159.5,311.5 L168,312 L176,312 L184.5,311.5 L193,310 L201,308.5 L209,306 L217,303.5 L224.5,300 L232,296 L239,291.5 L246,286.5 L252.5,281 L258.5,275.5 L264,269 L269,262.5 L274,255.5 L278,248.5 L281.5,241 L285,233 L287.5,225 L289.5,217 L291,208.5 L291.5,200.5 L292,192 Z" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="172" cy="192" r="5" fill="#1f2933"/>
  <line x1="172" y1="192" x2="292" y2="192" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="292" y1="192" x2="292" y2="125" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M292,110 L299,126 L285,126 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="292" cy="192" r="9" fill="#1f2933"/>
  <foreignObject x="302" y="95.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <line x1="172" y1="192" x2="172" y2="72" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="172" y1="72" x2="105" y2="72" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M90,72 L106,65 L106,79 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="172" cy="72" r="9" fill="#1f2933"/>
  <foreignObject x="35" y="35.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <line x1="172" y1="192" x2="52" y2="192" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="52" y1="192" x2="52" y2="259" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M52,274 L45,258 L59,258 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="52" cy="192" r="9" fill="#1f2933"/>
  <foreignObject x="64" y="267.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_3$</div></foreignObject>
  <line x1="172" y1="192" x2="172" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="172" y1="312" x2="239" y2="312" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M254,312 L238,319 L238,305 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="172" cy="312" r="9" fill="#1f2933"/>
  <foreignObject x="264" y="319.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_4$</div></foreignObject>
  <path d="M278,192 V178 H292" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="222" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <path d="M295,121 L291.5,115.5 L288,110 L284,104.5 L279.5,99.5 L275.5,94.5 L270.5,90 L266,85.5 L260.5,81 L255.5,77 L250,73.5 L244.5,70 L238.5,66.5" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M228,61 L243,62.5 L237.5,73 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="362" y1="40" x2="362" y2="340" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="380" y="135.5" width="206" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_1 = v_2 = v_3 = v_4$</div></foreignObject>
  <foreignObject x="380" y="207.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{v}_1 \neq \overline{v}_2$</div></foreignObject>
</svg>

### When the string breaks
A puck tied to a string circles a peg on the ice. The string pulls the puck towards the peg and turns its direction of motion all the time. If the string breaks, no force acts on the puck horizontally any more: the friction of the ice is assumed small, and the vertical forces, the weight and the support force of the ice, cancel each other. By Newton's first law the puck then continues in uniform motion in a straight line with the velocity it had at the moment of the break. The puck therefore leaves along the tangent of the path, not straight away from the peg. In the same way, water drops flying off the rim of a spinning umbrella leave along the tangent.

<svg data-fig="release" viewBox="0 0 600 340" role="img" aria-label="Formula figure: a puck tied to a string circles a peg anticlockwise along a circular path drawn with a dashed line. At the lowest point of the path the string breaks, and the puck continues straight to the right along the tangent of the path. The positions of the puck are marked at equal time intervals: the gaps are equally long, so the speed stays the same." style="max-width:100%;font-size:24px">
  <path d="M168,260 L175.5,259.5 L183.5,259 L191,257.5 L198.5,255.5 L205.5,253.5 L212.5,250.5 L219.5,247 L226.5,243.5 L232.5,239 L238.5,234.5 L244.5,229 L249.5,223.5 L254.5,217.5 L259,211.5 L263.5,205 L267,198 L270,191 L272.5,184 L274.5,176.5 L276.5,169 L277.5,161.5 L278,154 L278,146 L277.5,138.5 L276.5,131 L274.5,123.5 L272.5,116 L270,109 L267,102 L263.5,95 L259,88.5 L254.5,82.5 L249.5,76.5 L244.5,71 L238.5,65.5 L232.5,61 L226.5,56.5 L219.5,53 L212.5,49.5 L205.5,46.5 L198.5,44.5 L191,42.5 L183.5,41 L175.5,40.5 L168,40 L160.5,40.5 L152.5,41 L145,42.5 L137.5,44.5 L130.5,46.5 L123.5,49.5 L116.5,53 L109.5,56.5 L103.5,61 L97.5,65.5 L91.5,71 L86.5,76.5 L81.5,82.5 L77,88.5 L72.5,95 L69,102 L66,109 L63.5,116 L61.5,123.5 L59.5,131 L58.5,138.5 L58,146 L58,154 L58.5,161.5 L59.5,169 L61.5,176.5 L63.5,184 L66,191 L69,198 L72.5,205 L77,211.5 L81.5,217.5 L86.5,223.5 L91.5,229 L97.5,234.5 L103.5,239 L109.5,243.5 L116.5,247 L123.5,250.5 L130.5,253.5 L137.5,255.5 L145,257.5 L152.5,259 L160.5,259.5 L168,260" fill="none" stroke="#c9c2b2" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="8 7"/>
  <circle cx="168" cy="150" r="8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="168" y1="150" x2="178" y2="196" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M178,196 l5,4 l-6,3" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="72.5" cy="205" r="7" fill="#1f2933"/>
  <circle cx="72.5" cy="205" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="97.5" cy="234.5" r="7" fill="#1f2933"/>
  <circle cx="97.5" cy="234.5" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="130.5" cy="253.5" r="7" fill="#1f2933"/>
  <circle cx="130.5" cy="253.5" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <line x1="168" y1="260" x2="520" y2="260" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 6"/>
  <circle cx="168" cy="260" r="7" fill="#1f2933"/>
  <circle cx="168" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="206.5" cy="260" r="7" fill="#1f2933"/>
  <circle cx="206.5" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="245" cy="260" r="7" fill="#1f2933"/>
  <circle cx="245" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="283" cy="260" r="7" fill="#1f2933"/>
  <circle cx="283" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="321.5" cy="260" r="7" fill="#1f2933"/>
  <circle cx="321.5" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="360" cy="260" r="7" fill="#1f2933"/>
  <circle cx="360" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="398.5" cy="260" r="7" fill="#1f2933"/>
  <circle cx="398.5" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="437" cy="260" r="7" fill="#1f2933"/>
  <circle cx="437" cy="260" r="7" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="475" cy="260" r="10" fill="#1f2933"/>
  <line x1="489" y1="260" x2="548" y2="260" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M563,260 L547,267 L547,253 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="510.5" y="219.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="70.5" y="275.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{the string breaks}$</div></foreignObject>
  <foreignObject x="292" y="275.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{straight, steadily}$</div></foreignObject>
</svg>

### A change of direction is a change of velocity
The change of velocity $\Delta\overline{v}$ is seen when two successive velocity vectors are drawn starting from the same point. The change $\Delta\overline{v}$ is the vector that must be added to $\overline{v}_1$ to get $\overline{v}_2$. On a circular path the vectors are equally long but their directions differ, so $\Delta\overline{v}$ is not zero when the time interval is shorter than one revolution. Acceleration means a change of velocity, not only a change of speed. In uniform circular motion an object is therefore accelerating, and by Newton's second law a net force that is not zero acts on it. This net force points to the side of the centre of the circle, that is, to the inside of the path, not outwards. The magnitude of the acceleration is calculated in the chapter *Centripetal acceleration and the equation of motion in a circle*.

<svg data-fig="dv" viewBox="0 0 600 340" role="img" aria-label="Formula figure: on the left an arc of a circular path and two successive positions of an object, where the velocities are equally long but point in different directions. On the right the same vectors have been moved to start from the same point, and the black arrow from the tip of the first to the tip of the second is the change of velocity. The second velocity is the first velocity plus the change of velocity." style="max-width:100%;font-size:24px">
  <path d="M290,300 L290,292 L289,283.5 L288,275.5 L287,267.5 L285,259.5 L283,251.5 L280.5,244 L277.5,236.5 L274.5,229 L271,221.5 L267,214.5 L262.5,207.5 L258,200.5 L253,194 L248,188 L242.5,182 L236.5,176 L230.5,170.5 L224,165.5 L217.5,160.5 L210.5,156 L203.5,152 L196.5,148 L189,144.5 L181.5,141.5 L174,139 L166,136.5 L158,134.5 L150.5,132.5 L142,131.5 L134,130.5 L126,130 L118,130 L109.5,130.5 L101.5,131 L93.5,132 L85.5,133.5 L77.5,135.5 L69.5,137.5 L62,140.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="120" cy="300" r="5" fill="#1f2933"/>
  <line x1="120" y1="300" x2="267" y2="215" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="267" y1="215" x2="216.5" y2="127.5" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M209,114.5 L223.5,125 L211,132 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="267" cy="215" r="8" fill="#1f2933"/>
  <foreignObject x="221" y="96" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <line x1="120" y1="300" x2="164" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="164" y1="136" x2="66.5" y2="109.5" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M52,106 L69.5,103 L65.5,117 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="164" cy="136" r="8" fill="#1f2933"/>
  <foreignObject x="-3" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <line x1="340" y1="30" x2="340" y2="320" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="540" y1="262" x2="489.5" y2="174.5" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M482,161.5 L496,172 L484,179 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="540" y1="262" x2="442.5" y2="236" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M428,232 L445.5,229 L441.5,243 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="482" y1="161.5" x2="436" y2="221.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M428,232 L431.5,217 L441.5,224.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="540" cy="262" r="5" fill="#1f2933"/>
  <foreignObject x="490" y="137" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="375" y="233.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="394" y="166.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\Delta\overline{v}$</div></foreignObject>
  <foreignObject x="366" y="297.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{v}_2 = \overline{v}_1 + \Delta\overline{v}$</div></foreignObject>
</svg>

## Formula: Speed
Uniform circular motion is described by the **period** $T$, which is the time in which the object goes round the path once. Its reciprocal is the **rotation frequency** $f$, which tells how many revolutions the object makes per unit of time:
```latex
f = \frac{1}{T}
```
where $f$ is the rotation frequency ($\tfrac{1}{\text{s}}$) and $T$ the period ($\text{s}$). When the period is $T = 0.50\,\text{s}$, the object makes $2.0$ revolutions per second, that is, $f = 2.0\,\tfrac{1}{\text{s}}$. The rotation frequency is also often given in revolutions per minute. For example, $45\,\tfrac{1}{\text{min}}$ is converted by substituting $1\,\text{min} = 60\,\text{s}$, which gives $45\,\tfrac{1}{\text{min}} = \tfrac{45}{60\,\text{s}} = 0.75\,\tfrac{1}{\text{s}}$.

In one revolution the object travels a distance equal to the circumference $2\pi r$ of the circle, and this takes the period $T$. Because the speed is constant, the magnitude of the velocity on the circular path, the **speed along the path**, is the distance travelled divided by the time:
```latex
v = \frac{2\pi r}{T} = 2\pi r f
```
where $v$ is the speed ($\text{m/s}$), $r$ the radius of the path ($\text{m}$), $T$ the period ($\text{s}$) and $f$ the rotation frequency ($\tfrac{1}{\text{s}}$). The latter form is obtained by replacing $\tfrac{1}{T}$ with the rotation frequency $f$.

The formula answers the opening question. All parts of the roundabout complete a turn in the same time $T$, but the child at the edge goes round a bigger circle. The speed is directly proportional to the radius when the period is the same: a child standing twice as far from the centre travels twice the distance in the same time, so the speed is doubled. At the same radius, halving the period doubles the speed.

<svg data-fig="two-radii" viewBox="0 0 600 380" role="img" aria-label="Formula figure from above: two points A and B are on the same radius of a rotating roundabout, A at the distance r and B at the distance 2r from the centre. In the same time each turns through the same fraction of a revolution, but the arc travelled by B is twice as long, and the blue velocity vector of B is twice as long as that of A. The proportions are to scale." style="max-width:100%;font-size:24px">
  <path d="M366,326 L366,315 L365,304 L364,293 L362.5,282 L360.5,271.5 L358.5,260.5 L355.5,250 L352.5,239.5 L348.5,229 L344.5,219 L340.5,209 L335.5,199 L330.5,189 L324.5,179.5 L319,170.5 L312.5,161.5 L306,152.5 L299,144 L291.5,136 L284,128 L276,120.5 L268,113 L259.5,106 L250.5,99.5 L241.5,93 L232.5,87.5 L223,81.5 L213,76.5 L203,71.5 L193,67.5 L183,63.5 L172.5,59.5 L162,56.5 L151.5,53.5 L140.5,51.5 L130,49.5 L119,48 L108,47 L97,46 L86,46" fill="none" stroke="#c9c2b2" stroke-width="2" stroke-linejoin="round" stroke-dasharray="7 6"/>
  <path d="M226,326 L226,320.5 L225.5,315 L225,309.5 L224.5,304 L223.5,298.5 L222,293.5 L220.5,288 L219,282.5 L217.5,277.5 L215.5,272.5 L213,267.5 L210.5,262.5 L208,257.5 L205.5,253 L202.5,248 L199.5,243.5 L196,239.5 L192.5,235 L189,231 L185,227 L181,223 L177,219.5 L172.5,216 L168.5,212.5 L164,209.5 L159,206.5 L154.5,204 L149.5,201.5 L144.5,199 L139.5,196.5 L134.5,194.5 L129.5,193 L124,191.5 L118.5,190 L113.5,188.5 L108,187.5 L102.5,187 L97,186.5 L91.5,186 L86,186" fill="none" stroke="#c9c2b2" stroke-width="2" stroke-linejoin="round" stroke-dasharray="7 6"/>
  <line x1="86" y1="326" x2="366" y2="326" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="326" x2="300.5" y2="146" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M226,326 L226,321 L225.5,316 L225,311.5 L224.5,306.5 L224,301.5 L223,297 L222,292 L220.5,287.5 L219,282.5 L217.5,278 L216,273.5 L214,269 L212,264.5 L209.5,260.5 L207,256 L204.5,252 L202,247.5 L199.5,243.5 L196.5,240 L193,236" fill="none" stroke="#1f2933" stroke-width="4.5" stroke-linejoin="round"/>
  <path d="M366,326 L366,319.5 L365.5,313 L365.5,306.5 L365,300 L364,293.5 L363.5,287 L362.5,280.5 L361,274 L360,268 L358.5,261.5 L357,255 L355,249 L353.5,242.5 L351.5,236.5 L349,230 L347,224 L344.5,218 L342,212 L339,206 L336,200.5 L333,194.5 L330,189 L327,183 L323.5,177.5 L320,172 L316.5,166.5 L312.5,161.5 L308.5,156 L304.5,151 L300.5,146" fill="none" stroke="#1f2933" stroke-width="4.5" stroke-linejoin="round"/>
  <circle cx="86" cy="326" r="6" fill="#1f2933"/>
  <circle cx="226" cy="326" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="240" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <circle cx="366" cy="326" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="380" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <foreignObject x="146" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="286" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <line x1="193" y1="236" x2="169.5" y2="207.5" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M160,196 L175.5,204 L164.5,213 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="193" cy="236" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="168" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{A}$</div></foreignObject>
  <line x1="300.5" y1="146" x2="243.5" y2="78" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M233.5,66.5 L249.5,74 L238.5,83 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="300.5" cy="146" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="241.5" y="38" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{B}$</div></foreignObject>
  <foreignObject x="240" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{A}$</div></foreignObject>
  <foreignObject x="370" y="208" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{B}$</div></foreignObject>
  <foreignObject x="440" y="105.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{same } T$</div></foreignObject>
  <foreignObject x="440" y="161.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s_\text{B} = 2\,s_\text{A}$</div></foreignObject>
  <foreignObject x="440" y="217.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v_\text{B} = 2\,v_\text{A}$</div></foreignObject>
</svg>

## Worked example
The diameter of the drum of a washing machine is $46\,\text{cm}$. In the spin cycle the drum turns $1200$ revolutions per minute. What is the speed of a sock pressed against the wall of the drum?

<!-- vaihe -->

**Given and find.** The diameter of the drum is $d = 46\,\text{cm}$ and the rotation frequency $f = 1200\,\tfrac{1}{\text{min}}$. We want the speed $v$ of the sock.

<!-- vaihe -->

**Principle.** The sock turns with the drum on its wall, so it is in uniform circular motion whose radius is the radius of the drum, $r = \tfrac{d}{2}$. In one revolution the sock travels the circumference $2\pi r$, and there are $f$ revolutions per unit of time, so the speed is $v = 2\pi r f$.

<!-- vaihe -->

**Rearranged formula.** Substitute the radius using the diameter:
```latex
\begin{aligned}
&v = 2\pi r f, \quad r = \frac{d}{2} \\
&v = \pi d f
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The diameter is $46\,\text{cm} = 46 \cdot 0.01\,\text{m} = 0.46\,\text{m}$. The rotation frequency is $f = 1200\,\tfrac{1}{\text{min}} = \tfrac{1200}{60\,\text{s}} = 20\,\tfrac{1}{\text{s}}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
v &= \pi d f \\
&= \pi \cdot 0.46\,\text{m} \cdot 20\,\tfrac{1}{\text{s}} \\
&= 28.90\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Result.** The speed of the sock is about $29\,\text{m/s}$. The result is given with two significant figures, because the diameter $46\,\text{cm}$ is given with two figures.

<!-- vaihe -->

**Reasonableness.** The circumference of the drum is $\pi \cdot 0.46\,\text{m} \approx 1.45\,\text{m}$, and the drum turns $20$ revolutions per second, so the sock travels about $20 \cdot 1.45\,\text{m} \approx 29\,\text{m}$ per second. The period is $T = \tfrac{1}{f} = 0.050\,\text{s}$, and the formula $v = \tfrac{2\pi r}{T} = \tfrac{2\pi \cdot 0.23\,\text{m}}{0.050\,\text{s}}$ gives the same $28.9\,\text{m/s}$. That is about $29 \cdot 3.6\,\tfrac{\text{km}}{\text{h}} \approx 104\,\tfrac{\text{km}}{\text{h}}$, the order of magnitude of motorway speed, which fits a fast spin cycle.

## Common misconception
Many think that in uniform circular motion the velocity does not change, because the speedometer shows the same reading all the time. The speedometer, however, shows only the magnitude of the velocity, that is, the speed. Velocity is a vector, and its direction turns all the time, so the velocity changes and the object is accelerating. Without a net force the object would not stay on the circular path but would continue in a straight line.

Another mistake is to think that when the string breaks the object flies straight away from the centre. No force pushes the object outwards. When the string stops pulling, the object continues in the direction of its velocity at that moment, that is, along the tangent of the path.

Common mistakes in calculations are substituting the diameter in place of the radius in the formula $v = \tfrac{2\pi r}{T}$ and substituting the rotation frequency in revolutions per minute without converting it to revolutions per second.

## Summary
- In circular motion the path of an object is a circle of radius $r$. In uniform circular motion the speed stays the same.
- The velocity $\overline{v}$ is at every moment along the tangent of the path. Its direction changes all the time, so the velocity changes and the object is accelerating, even though the speed is constant.
- When no net force acts on the object any more, it continues in a straight line along the tangent of the path.
- The period $T$ is the time of one revolution, and the rotation frequency $f = \tfrac{1}{T}$ is the number of revolutions per unit of time.
- The speed $v = \tfrac{2\pi r}{T} = 2\pi r f$ is directly proportional to the radius when the period is the same.
