# Moment of a force and rotation of a body

> **Why** does a stuck wheel nut come loose with a long wrench, when the same force on a short wrench cannot make it budge?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a garage. The rear wheel of a car has five wheel nuts. A long cross wrench has been placed on one nut, its handle reaching far to the left, and its end is pressed down by a red force arrow. On the floor to the right of the tyre lies a short spanner." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51h-floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy51h-car" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy51h-rim" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy51h-steel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="40" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="86" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="132" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="178" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="224" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="270" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="316" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="362" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="408" width="1200" height="2" fill="#e3dccb"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy51h-floor)"/>
  <rect x="0" y="466" width="1200" height="6" fill="#c9c2b2"/>
  <path d="M520,80 H1200 V330 H975 A205,205 0 0 0 565,330 H520 Q500,330 500,300 V110 Q500,80 520,80 Z" fill="url(#fy51h-car)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M560,120 H1180" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="980" y="170" width="80" height="18" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="770" cy="360" r="182" fill="#1f2933"/>
  <line x1="938" y1="360" x2="950" y2="360" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="932.5" y1="403.5" x2="944" y2="406.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="915.5" y1="444" x2="926" y2="450" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="889" y1="479" x2="897.5" y2="487.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="854" y1="505.5" x2="860" y2="516" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="813.5" y1="522.5" x2="816.5" y2="534" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="770" y1="528" x2="770" y2="540" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="726.5" y1="522.5" x2="723.5" y2="534" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="686" y1="505.5" x2="680" y2="516" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="651" y1="479" x2="642.5" y2="487.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="624.5" y1="444" x2="614" y2="450" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="607.5" y1="403.5" x2="596" y2="406.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="602" y1="360" x2="590" y2="360" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="607.5" y1="316.5" x2="596" y2="313.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="624.5" y1="276" x2="614" y2="270" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="651" y1="241" x2="642.5" y2="232.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="686" y1="214.5" x2="680" y2="204" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="726.5" y1="197.5" x2="723.5" y2="186" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="770" y1="192" x2="770" y2="180" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="813.5" y1="197.5" x2="816.5" y2="186" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="854" y1="214.5" x2="860" y2="204" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="889" y1="241" x2="897.5" y2="232.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="915.5" y1="276" x2="926" y2="270" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="932.5" y1="316.5" x2="944" y2="313.5" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="770" cy="360" r="120" fill="url(#fy51h-rim)" stroke="#8a96a3" stroke-width="4"/>
  <path d="M755,403.5 L723,457.5 L692,434.5 L733,387.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M724,359.5 L663,345.5 L675,309 L732.5,333.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M756.5,316 L750.5,253.5 L789.5,253.5 L783.5,316 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M807.5,333.5 L865,309 L877,345.5 L816,359.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M807,387.5 L848,434.5 L817,457.5 L785,403.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <circle cx="770" cy="360" r="34" fill="#c4ccd4" stroke="#8a96a3" stroke-width="3"/>
  <polygon points="763,306.5 750,314 737,306.5 737,291.5 750,284 763,291.5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="750" cy="299" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polygon points="835,330 822,337.5 809,330 809,315 822,307.5 835,315" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="822" cy="322.5" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polygon points="835,405 822,412.5 809,405 809,390 822,382.5 835,390" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="822" cy="397.5" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polygon points="763,428.5 750,436 737,428.5 737,413.5 750,406 763,413.5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="750" cy="421" r="6.3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <path d="M706,349 L306,349 L306,371 L706,371 Z" fill="url(#fy51h-steel)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="306" cy="360" r="11" fill="url(#fy51h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="706" cy="360" r="32" fill="url(#fy51h-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <polygon points="725,371 706,382 687,371 687,349 706,338 725,349" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="706" cy="360" r="9.24" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="344" width="90" height="32" rx="14" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <line x1="344" y1="210" x2="344" y2="311" stroke="#c92a2a" stroke-width="7" stroke-linecap="butt"/>
  <path d="M344,340 L330.5,310 L357.5,310 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M1010,532 H1140 V548 H1010 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="1010" cy="540" r="20" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="1010" cy="540" r="9" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1140" cy="540" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
</svg>

## Key idea
A force can change the motion of a body, but it can also rotate the body. When a body is fixed to an axis, like a door on its hinges, a nut on a bolt or a seesaw on its support, it cannot move away but can only rotate about the axis. This axis is called the **axis of rotation**. The ability of a force to rotate a body about the axis of rotation is called the **turning effect**, and its size is measured by the **moment** (the moment of a force). The turning effect does not depend only on the size of the force. It also depends on the direction of the force and on the point of the body where the force acts.

### A door and the point of application of a force
A door is easy to open by pushing at the handle, which is far from the hinges. If the same force pushes close to the hinge, the door turns much less easily. If the door is pushed at its edge in the direction of the door towards the hinge, the door does not turn at all, even though the force is equally large. The three forces $\overline{F}_1$, $\overline{F}_2$ and $\overline{F}_3$ in the figure are therefore equally large, but their turning effects about the hinge are completely different.

<svg data-fig="ovi" viewBox="0 0 600 330" role="img" aria-label="A door seen from above. On the left is a wall and a hinge, from which the door extends to the right as a horizontal board. Three equally long red force arrows: F1 at the handle perpendicular to the door, F2 near the hinge, also perpendicular, and F3 at the end of the door along the door towards the hinge. A dashed arc shows the direction in which the door opens. Schematic figure, not to scale." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-ovi-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy51-ovi-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="24" y="200" width="40" height="110" fill="url(#fy51-ovi-wall)" stroke="#1f2933" stroke-width="2"/>
  <line x1="26" y1="214" x2="62" y2="204" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="234" x2="62" y2="224" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="254" x2="62" y2="244" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="274" x2="62" y2="264" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="294" x2="62" y2="284" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <foreignObject x="15" y="167.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{wall}$</div></foreignObject>
  <path d="M524,250 A440,440 0 0 0 486,71" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-dasharray="7 6"/>
  <rect x="84" y="242" width="440" height="16" rx="2" fill="url(#fy51-ovi-wood)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="84" cy="250" r="11" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="75" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{hinge}$</div></foreignObject>
  <rect x="452" y="258" width="26" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="423.5" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{handle}$</div></foreignObject>
  <line x1="465" y1="242" x2="465" y2="167" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M465,150 L473,168 L457,168 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="403" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <line x1="150" y1="242" x2="150" y2="167" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,150 L158,168 L142,168 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="167" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <line x1="622" y1="250" x2="547" y2="250" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,250 L548,242 L548,258 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="547.5" y="207.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_3$</div></foreignObject>
  <foreignObject x="215" y="15.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{seen from above}$</div></foreignObject>
</svg>

### The lever arm of a force
The turning effect is decided by the **line of action** of the force, the straight line that passes through the point of application of the force (in a wrench, the point where the hand grips) in the direction of the force. The **lever arm** $r$ of a force is the perpendicular distance from the axis of rotation to the line of action. When the force is perpendicular to the handle of the wrench, the lever arm equals the distance $d$ of the point of application from the axis. When the force is oblique, the lever arm is shorter than $d$. If the line of action passes through the axis of rotation, the lever arm is zero and the force does not rotate the body at all. This is why the force $\overline{F}_3$ along the door does not open the door.

<svg data-fig="varsi" viewBox="0 0 600 340" role="img" aria-label="A spanner around a nut. The axis of rotation O is at the centre of the nut. The handle of the spanner points horizontally to the right, and a hand pulls it at a point at the distance d from the axis. The force F points obliquely up and to the right, at an angle of 60 degrees to the extension of the handle. The line of action of the force is drawn dashed in both directions. The segment drawn from the axis perpendicular to the line of action is the lever arm r of the force, and it is shorter than d. Schematic figure." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-varsi-steel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <line x1="308" y1="284" x2="493" y2="-36.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="398" y1="128" x2="468" y2="128" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <path d="M118,138 L404,138 L404,118 L118,118 Z" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="404" cy="128" r="10" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="118" cy="128" r="32" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <polygon points="137,139 118,150 99,139 99,117 118,106 137,117" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="118" cy="128" r="9.24" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="118" y1="128" x2="328" y2="249" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M322,259.5 L311.5,253.5 L317.5,243" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="328" cy="249" r="3.5" fill="#1f2933"/>
  <foreignObject x="191" y="192" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <line x1="118" y1="82" x2="398" y2="82" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="118" y1="74" x2="118" y2="90" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398" y1="74" x2="398" y2="90" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="248" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <line x1="398" y1="128" x2="445.5" y2="45.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M454,31 L452,50.5 L438,42.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="461.5" y="20.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M438,128 A40,40 0 0 0 418,93.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="442" y="87" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <circle cx="398" cy="128" r="4" fill="#1f2933"/>
  <foreignObject x="68" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="319" y="264.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{line of action}$</div></foreignObject>
</svg>

## Formula: Moment of a force
The moment of a force about the axis of rotation is the product of the magnitude of the force and its lever arm:
```latex
M = F r
```
where $M$ is the moment of the force ($\text{Nm}$), $F$ the magnitude of the force ($\text{N}$) and $r$ the lever arm of the force, that is the perpendicular distance from the axis of rotation to the line of action ($\text{m}$). The unit of moment is the newton metre $\text{Nm}$. It is not the same thing as the unit of energy, the joule, even though both are a product of a newton and a metre: in a moment the distance is perpendicular to the force, in work it is a displacement in the direction of the force.

### Direction of rotation and sign
In addition to its magnitude, a moment has a direction of rotation. In this book a moment that rotates anticlockwise is positive and a moment that rotates clockwise is negative. When several forces act on a body, their moments are added together with their signs. The result is the **net moment**:
```latex
\Sigma M = M_1 + M_2 + M_3 + \ldots
```
where $\Sigma M$ is the net moment ($\text{Nm}$) and $M_1$, $M_2$, … are the moments of the individual forces about the same chosen axis of rotation ($\text{Nm}$). If the net moment on a body at rest that can rotate about a fixed axis is not zero, the body starts to rotate in the direction of the net moment. When a body stays at rest is studied more closely in the chapter *Rotational equilibrium*.

<svg data-fig="suunta" viewBox="0 0 600 320" role="img" aria-label="Two situations side by side. In both, a horizontal rod is fixed to the axis O at its left end. On the left, the force F acts on the right end of the rod upwards, and the curved arrow around the axis rotates anticlockwise: the moment is positive. On the right, the force acts on the end of the rod downwards, and the curved arrow rotates clockwise: the moment is negative." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-suunta-44" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy51-suunta-344" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="300" y1="14" x2="300" y2="306" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="70" y="157" width="200" height="18" rx="4" fill="url(#fy51-suunta-44)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="70" cy="166" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="258" y1="157" x2="258" y2="87" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M258,70 L266,88 L250,88 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="263.5" y="67.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M113,150.5 A46,46 0 0 0 30,143.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M27,150.5 L25.5,136 L36.5,140 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="66" y="19.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{anticlockwise}$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M > 0$</div></foreignObject>
  <foreignObject x="34" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <rect x="370" y="157" width="200" height="18" rx="4" fill="url(#fy51-suunta-344)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="370" cy="166" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="558" y1="175" x2="558" y2="245" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M558,262 L550,244 L566,244 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="563.5" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M327,150.5 A46,46 0 0 1 410,143.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M413,150.5 L403.5,140 L414.5,136 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="366" y="19.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{clockwise}$</div></foreignObject>
  <foreignObject x="366" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M < 0$</div></foreignObject>
  <foreignObject x="334" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
</svg>

### The lever arm of an oblique force
Often the distance $d$ of the point of application from the axis of rotation is known, together with the angle $\alpha$ that the force makes with the line from the axis to the point of application (for example, the extension of the handle of the wrench). The axis, the point of application and the foot of the lever arm form a right-angled triangle whose hypotenuse is $d$. The lever arm is the side opposite the angle $\alpha$:
```latex
r = d\sin\alpha
```
where $r$ is the lever arm of the force ($\text{m}$), $d$ the distance of the point of application from the axis of rotation ($\text{m}$) and $\alpha$ the angle between the force and the extension of the arm. When $\alpha = 90^\circ$, $r = d$ and the moment is greatest. When $\alpha = 0^\circ$ or $\alpha = 180^\circ$, $r = 0$.

<svg data-fig="kulma" viewBox="0 0 600 340" role="img" aria-label="A right-angled triangle whose vertices are the axis of rotation O, the point of application of the force and the foot of the perpendicular drawn from the axis to the line of action. The hypotenuse is the distance d between the axis and the point of application. The side from the axis to the foot is the lever arm r of the force. The angle at the point of application is alpha, the same as the angle between the force and the extension of the arm. Therefore r is d times sine alpha." style="max-width:100%;font-size:24px">
  <path d="M92,104 L422,104 L228.5,266.5 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <line x1="201" y1="289.5" x2="514" y2="27" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="422" y1="104" x2="486" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="92" y1="104" x2="422" y2="104" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="92" y1="104" x2="228.5" y2="266.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M217.5,275.5 L208.5,265 L219.5,256" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="422" y1="104" x2="485.5" y2="50.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M498.5,39.5 L490,57.5 L479.5,45 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="508" y="41" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <circle cx="92" cy="104" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="422" cy="104" r="4.5" fill="#1f2933"/>
  <foreignObject x="56" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="247" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="128" y="186.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <path d="M378,104 A44,44 0 0 0 388.5,132.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="352" y="111.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <path d="M460,104 A38,38 0 0 0 451,79.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="466.5" y="69.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="385" y="271.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r = d\sin\alpha$</div></foreignObject>
</svg>

## Worked example
A stuck nut is being loosened with a spanner. The hand grips the handle at a distance of $0.35\,\text{m}$ from the centre of the nut, which is the axis of rotation. The hand pulls the handle with a force of $240\,\text{N}$ that makes an angle of $65^\circ$ with the extension of the handle and turns the nut in the loosening direction. The nut comes loose only when the moment is at least $80\,\text{Nm}$. What is the moment of the hand's force about the axis of the nut, and does the nut come loose?

<!-- vaihe -->

**Given and find.** $F = 240\,\text{N}$, $d = 0.35\,\text{m}$, $\alpha = 65^\circ$ and the moment required by the nut $80\,\text{Nm}$. We are asked for the moment $M$ of the force and whether it is enough.

<!-- vaihe -->

**Principle.** The nut can only rotate about its axis, so the turning effect of the force is given by its moment $M = Fr$. The force is oblique to the handle, so the lever arm $r$ is shorter than the distance $d$: it is obtained from the right-angled triangle, $r = d\sin\alpha$.

<!-- vaihe -->

**Formula solved.** Substitute the expression for the lever arm into the formula for the moment:
```latex
\begin{aligned}
&M = F r \\
&M = F d\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the force is in newtons and the distance in metres, so the moment comes in newton metres.

<!-- vaihe -->

**Substitution.** Substitute the numerical values with their units:
```latex
\begin{aligned}
M &= F d\sin\alpha \\
&= 240\,\text{N}\cdot 0.35\,\text{m}\cdot\sin 65^\circ \\
&\approx 76.1\,\text{Nm}
\end{aligned}
```

<!-- vaihe -->

**Result.** The moment of the force is $M \approx 76\,\text{Nm}$, to two significant figures like the distance $0.35\,\text{m}$. It is smaller than the $80\,\text{Nm}$ required by the nut, so the nut does not come loose.

<!-- vaihe -->

**Reasonableness.** If the same force acted perpendicular to the handle, the lever arm would be the whole $0.35\,\text{m}$ and the moment $240\,\text{N}\cdot 0.35\,\text{m} = 84\,\text{Nm}$. An oblique pull gives less, because $\sin 65^\circ \approx 0.91 < 1$. So the nut would come loose with the same force if the pull were perpendicular to the handle.

## Common misconception
The moment is not obtained by multiplying the force by the distance to the point of application, but by the distance to the line of action. The distance $d$ and the lever arm $r$ are equal only when the force is perpendicular to the line from the axis to the point of application. Another mistake is to think that a long wrench adds force. The force of the hand is the same, but with a long wrench its lever arm is longer, so the moment is greater. Loosening a nut does not require a certain force but a certain moment.

## Summary
- The turning effect of a force about an axis of rotation is measured by the moment $M = Fr$, whose unit is the newton metre $\text{Nm}$.
- The lever arm $r$ of a force is the perpendicular distance from the axis of rotation to the line of action of the force, not the distance to the point of application.
- The lever arm of an oblique force is $r = d\sin\alpha$. A force whose line of action passes through the axis does not rotate the body.
- A moment that rotates anticlockwise is positive and one that rotates clockwise is negative. The net moment is the sum of the moments with their signs.
- If the net moment on a body at rest that can rotate about an axis is not zero, the body starts to rotate.
