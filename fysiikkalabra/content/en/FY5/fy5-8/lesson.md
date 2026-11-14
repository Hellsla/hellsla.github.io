# Spring force and spring energy

> **Why** does a pinball launcher shoot the ball faster the further its spring is compressed?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the lower right corner of a pinball machine seen from above, close up. In the launch lane a steel ball rests on the tip of the plunger. The coil spring around the plunger rod is compressed between the tip and the front wall, because a hand holds the plunger knob from below and pulls it out of the machine. On the left are the right flipper of the playfield and a triangle with a rubber edge, on the right the machine&#x27;s wooden side wall and the floor." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy58h-side" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="500"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy58h-field" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="460"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy58h-bump0" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient><linearGradient id="fy58h-bump1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><linearGradient id="fy58h-bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><radialGradient id="fy58h-ball" cx="0.35" cy="0.35" r="0.7"><stop offset="0" stop-color="#ffffff"/><stop offset="0.5" stop-color="#c4ccd4"/><stop offset="1" stop-color="#6c757d"/></radialGradient><linearGradient id="fy58h-knob" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <line x1="-30" y1="0" x2="-30" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="34" y1="0" x2="34" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="98" y1="0" x2="98" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="162" y1="0" x2="162" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="226" y1="0" x2="226" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="290" y1="0" x2="290" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="354" y1="0" x2="354" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="418" y1="0" x2="418" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="482" y1="0" x2="482" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="0" x2="546" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="610" y1="0" x2="610" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="674" y1="0" x2="674" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="738" y1="0" x2="738" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="802" y1="0" x2="802" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="866" y1="0" x2="866" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="0" x2="930" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="994" y1="0" x2="994" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1058" y1="0" x2="1058" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1122" y1="0" x2="1122" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1186" y1="0" x2="1186" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <g transform="translate(-585 -201) scale(1.35)">
  <path d="M1150,160 H1166 V510 H104 V496 H1150 Z" fill="#1f2933" fill-opacity="0.12"/>
  <rect x="100" y="150" width="1050" height="346" fill="url(#fy58h-side)" stroke="#1f2933" stroke-width="2"/>
  <rect x="148" y="150" width="904" height="310" fill="url(#fy58h-field)" stroke="#1f2933" stroke-width="2"/>
  <rect x="1000" y="150" width="52" height="310" fill="#ffffff"/>
  <line x1="1000" y1="150" x2="1000" y2="460" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <g transform="translate(16 0)">
  <circle cx="520" cy="176" r="53" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="176" r="42" fill="url(#fy58h-bump0)" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="176" r="17.64" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="716" cy="160" r="53" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="716" cy="160" r="42" fill="url(#fy58h-bump1)" stroke="#1f2933" stroke-width="2"/>
  <circle cx="716" cy="160" r="17.64" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="540" cy="256" r="13" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="596" cy="272" r="13" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="652" cy="278" r="13" fill="#1971c2" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="708" cy="272" r="13" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="764" cy="256" r="13" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <ellipse cx="652" cy="336" rx="40" ry="22" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="878" y="150" width="44" height="90" rx="22" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="900" cy="206" r="9" fill="#ffc078" stroke="#1f2933" stroke-width="1"/>
  <path d="M876,258 L876,346 L794,380 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M870,266 L802,372" fill="none" stroke="#1f2933" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M940,240 V354 L788,414" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linejoin="round"/>
  <path d="M778,396 L638,430 L640,442 L778,416 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="778" cy="406" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="778" cy="406" r="5" fill="#1f2933"/>
  <path d="M340,396 L480,430 L478,442 L340,416 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M984,446 H640 L606,460 H984 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M478,446 L512,460 H400 V446 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  </g>
  <path d="M640,150 L700,150 L620,460 L560,460 Z" fill="#ffffff" fill-opacity="0.3"/>
  <path d="M900,150 L960,150 L880,460 L820,460 Z" fill="#ffffff" fill-opacity="0.3"/>
  <rect x="92" y="460" width="1066" height="34" rx="6" fill="url(#fy58h-bar)" stroke="#1f2933" stroke-width="2"/>
  <rect x="1020" y="356" width="12" height="190" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1002" y="446" width="48" height="12" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M1045,374 L1007,380 L1045,386 L1007,392 L1045,398 L1007,404 L1045,410 L1007,416 L1045,422 L1007,428 L1045,434 L1007,440 L1045,446" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round" stroke-linejoin="round"/>
  <rect x="1004" y="356" width="44" height="18" rx="5" fill="#1f2933" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1026" cy="332" r="23" fill="url(#fy58h-ball)" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M1176,664 L1082,574" fill="none" stroke="#1f2933" stroke-width="51" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1176,664 L1082,574" fill="none" stroke="#f1dfb5" stroke-width="46" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="1066" cy="562" rx="38" ry="30" fill="#f1dfb5" stroke="#1f2933" stroke-width="2" transform="rotate(-30 1066 562)"/>
  <path d="M1056,578 Q1020,584 1004,564" fill="none" stroke="#1f2933" stroke-width="20" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1056,578 Q1020,584 1004,564" fill="none" stroke="#f1dfb5" stroke-width="15" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1026" cy="544" r="18" fill="url(#fy58h-knob)" stroke="#1f2933" stroke-width="2"/>
  <path d="M1070,540 Q1044,508 1006,518" fill="none" stroke="#1f2933" stroke-width="19" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1070,540 Q1044,508 1006,518" fill="none" stroke="#f1dfb5" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1066,526 Q1044,494 1006,504" fill="none" stroke="#1f2933" stroke-width="19" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1066,526 Q1044,494 1006,504" fill="none" stroke="#f1dfb5" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1078,542 Q1060,524 1034,530" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  </g>
</svg>

## Key idea

### A spring pulls back towards the equilibrium position
In the chapter *Describing oscillation: period, frequency and amplitude* an object moved back and forth on both sides of the equilibrium position. Now we find out what kind of force always pulls the object back towards the equilibrium position. Consider a trolley attached to a horizontal spring. When the spring is at its rest length, it exerts no force on the trolley, and the trolley can be at rest. This point is the **equilibrium position** of the trolley. Let the $x$-axis point along the spring with its origin at the equilibrium position. The position $x$ of the trolley is then its **displacement** from the equilibrium position: to the right of the equilibrium position $x > 0$ and to the left $x < 0$.

When the trolley is pulled to the right, the spring stretches and pulls the trolley to the left. When the trolley is pushed to the left, the spring is compressed and pushes the trolley to the right. In both cases the force of the spring points towards the equilibrium position, that is opposite to the displacement. This is why the force of a spring is also called a **restoring force**.

<svg data-fig="suunta" viewBox="0 0 600 390" role="img" aria-label="Diagram, not to scale: three situations one below the other. A trolley is attached to a horizontal spring whose other end is fixed to a wall on the left. The vertical dashed line is the equilibrium position x = 0. At the top the trolley has been moved to the right, the spring is stretched, and the spring force F points to the left, towards the equilibrium position. In the middle the trolley is at the equilibrium position, the spring is at its rest length and there is no force. At the bottom the trolley has been moved to the left, the spring is compressed, and the spring force points to the right, towards the equilibrium position. The position x of the trolley is shown by a thin black dimension arrow, the force by a red arrow." style="max-width:100%;font-size:24px">
  <foreignObject x="158.5" y="3.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{equilibrium position } x = 0$</div></foreignObject>
  <line x1="300" y1="34" x2="300" y2="372" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <rect x="28" y="58" width="16" height="78" fill="#e3dccb"/>
  <line x1="44" y1="58" x2="44" y2="136" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="43" y1="64" x2="31" y2="74" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="76" x2="31" y2="86" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="88" x2="31" y2="98" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="100" x2="31" y2="110" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="112" x2="31" y2="122" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="124" x2="31" y2="134" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="44" y1="136" x2="470" y2="136" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M44,105 L54,105 L61,97 L76,113 L90,97 L105,113 L119,97 L134,113 L148,97 L163,113 L177,97 L192,113 L206,97 L221,113 L235,97 L250,113 L264,97 L279,113 L293,97 L308,113 L315,105 L325,105" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="325" y="78" width="90" height="44" rx="6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="345" cy="129" r="7" fill="#1f2933"/>
  <circle cx="345" cy="129" r="2.5" fill="#ffffff"/>
  <circle cx="395" cy="129" r="7" fill="#1f2933"/>
  <circle cx="395" cy="129" r="2.5" fill="#ffffff"/>
  <foreignObject x="465" y="73.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{stretched}$</div></foreignObject>
  <foreignObject x="540" y="105.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$x > 0$</div></foreignObject>
  <line x1="300" y1="47" x2="300" y2="61" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="54" x2="360" y2="54" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M370,54 L359,59 L359,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="380" y="39.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <line x1="325" y1="88" x2="272" y2="88" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M255,88 L273,80 L273,96 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="204" y="53.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <rect x="28" y="178" width="16" height="78" fill="#e3dccb"/>
  <line x1="44" y1="178" x2="44" y2="256" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="43" y1="184" x2="31" y2="194" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="196" x2="31" y2="206" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="208" x2="31" y2="218" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="220" x2="31" y2="230" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="232" x2="31" y2="242" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="244" x2="31" y2="254" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="44" y1="256" x2="470" y2="256" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M44,225 L54,225 L59.5,217 L70,233 L80.5,217 L91,233 L102,217 L112.5,233 L123,217 L133.5,233 L144,217 L155,233 L165.5,217 L176,233 L186.5,217 L197,233 L208,217 L218.5,233 L229,217 L239.5,233 L245,225 L255,225" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="255" y="198" width="90" height="44" rx="6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="275" cy="249" r="7" fill="#1f2933"/>
  <circle cx="275" cy="249" r="2.5" fill="#ffffff"/>
  <circle cx="325" cy="249" r="7" fill="#1f2933"/>
  <circle cx="325" cy="249" r="2.5" fill="#ffffff"/>
  <foreignObject x="452" y="193.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{rest length}$</div></foreignObject>
  <foreignObject x="540" y="225.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$x = 0$</div></foreignObject>
  <foreignObject x="195" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$F = 0$</div></foreignObject>
  <rect x="28" y="298" width="16" height="78" fill="#e3dccb"/>
  <line x1="44" y1="298" x2="44" y2="376" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="43" y1="304" x2="31" y2="314" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="316" x2="31" y2="326" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="328" x2="31" y2="338" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="340" x2="31" y2="350" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="352" x2="31" y2="362" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="364" x2="31" y2="374" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="44" y1="376" x2="470" y2="376" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M44,345 L54,345 L57.5,337 L64,353 L71,337 L77.5,353 L84,337 L91,353 L97.5,337 L104.5,353 L111,337 L118,353 L124.5,337 L131.5,353 L138,337 L145,353 L151.5,337 L158,353 L165,337 L171.5,353 L175,345 L185,345" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="185" y="318" width="90" height="44" rx="6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="205" cy="369" r="7" fill="#1f2933"/>
  <circle cx="205" cy="369" r="2.5" fill="#ffffff"/>
  <circle cx="255" cy="369" r="7" fill="#1f2933"/>
  <circle cx="255" cy="369" r="2.5" fill="#ffffff"/>
  <foreignObject x="452" y="313.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{compressed}$</div></foreignObject>
  <foreignObject x="540" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$x < 0$</div></foreignObject>
  <line x1="300" y1="287" x2="300" y2="301" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="294" x2="240" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M230,294 L241,289 L241,299 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="200" y="279.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x$</div></foreignObject>
  <line x1="115" y1="328" x2="168" y2="328" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M185,328 L167,336 L167,320 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="72" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/spring-rider-suomenlinna.webp" alt="A small child sits on a yellow lion-shaped rider fixed to the ground by a thick coil spring."><figcaption>A spring rider in Suomenlinna, Helsinki. When the rider tilts to one side, the spring pulls it back towards the equilibrium position, and the rider rocks back and forth.</figcaption></figure>

### Harmonic force
When a spring is neither stretched nor compressed too much, the magnitude of the spring force is directly proportional to the displacement: double the displacement gives double the force. A force whose magnitude is directly proportional to the displacement of an object from the equilibrium position and which always points towards the equilibrium position is called a **harmonic force**. The force of a spring is its most common example. The restoring force of a pendulum is also approximately harmonic for small swings. In the chapter *The mass–spring oscillator and the pendulum* we see what kind of motion a harmonic force produces.

### The force of the spring and the force that stretches the spring
When a hand stretches a spring, two objects interact: the hand pulls the spring, and the spring pulls the hand. By Newton's third law these forces are equal in magnitude and opposite in direction, but they act on different objects. The force $\overline{F}_\text{v}$ that stretches the spring acts on the spring (the subscript v comes from the Finnish *venyttävä*, stretching, as in the simulation). The spring force $\overline{F}$ acts on the hand or on the object at the end of the spring. So only the spring force is drawn in the free-body diagram of the object.

<svg data-fig="pari" viewBox="0 0 600 330" role="img" aria-label="Two pictures one below the other. At the top a hand stretches a spring fixed to a wall, to the right. At the bottom the spring and the hand are drawn apart: the force of the hand F_v acts to the right on the right end of the spring, and the force of the spring F acts to the left on the hand. The arrows are equally long: the forces are equal in magnitude and opposite in direction, and they act on different objects." style="max-width:100%;font-size:24px">
  <rect x="28" y="40" width="16" height="90" fill="#e3dccb"/>
  <line x1="44" y1="40" x2="44" y2="130" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="43" y1="46" x2="31" y2="56" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="58" x2="31" y2="68" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="70" x2="31" y2="80" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="82" x2="31" y2="92" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="94" x2="31" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="106" x2="31" y2="116" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="118" x2="31" y2="128" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M44,86 L54,86 L60,77 L72,95 L84,77 L96.5,95 L108.5,77 L120.5,95 L132.5,77 L144.5,95 L157,77 L169,95 L181,77 L193,95 L205,77 L217,95 L229.5,77 L241.5,95 L253.5,77 L265.5,95 L277.5,77 L290,95 L302,77 L314,95 L320,86 L330,86" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="336" cy="86" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="340" y="68" width="44" height="36" rx="12" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="350" y1="76" x2="362" y2="76" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="86" x2="362" y2="86" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="96" x2="362" y2="96" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="378" y="74" width="40" height="24" rx="6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="465" y="71.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{situation}$</div></foreignObject>
  <line x1="20" y1="160" x2="580" y2="160" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="28" y="196" width="16" height="80" fill="#e3dccb"/>
  <line x1="44" y1="196" x2="44" y2="276" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="43" y1="202" x2="31" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="214" x2="31" y2="224" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="226" x2="31" y2="236" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="238" x2="31" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="250" x2="31" y2="260" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="262" x2="31" y2="272" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="43" y1="274" x2="31" y2="284" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M44,236 L54,236 L59,227 L69.5,245 L80,227 L90,245 L100.5,227 L111,245 L121,227 L131.5,245 L142,227 L152,245 L162.5,227 L173,245 L183,227 L193.5,245 L204,227 L214,245 L224.5,227 L235,245 L240,236 L250,236" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="256" cy="236" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="262" y1="236" x2="335" y2="236" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M352,236 L334,244 L334,228 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="284.5" y="191.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="62.5" y="275.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hand pulls spring}$</div></foreignObject>
  <rect x="466" y="218" width="44" height="36" rx="12" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="476" y1="226" x2="488" y2="226" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="236" x2="488" y2="236" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="246" x2="488" y2="246" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="504" y="224" width="40" height="24" rx="6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="462" y1="236" x2="389" y2="236" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M372,236 L390,228 L390,244 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="400.5" y="191.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="372.5" y="275.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{spring pulls hand}$</div></foreignObject>
</svg>

When the trolley is held still at displacement $x$, a hand pulls or pushes the trolley, and the trolley pulls or pushes the spring with a force of equal magnitude. The force of the hand and the force of the spring on the trolley cancel each other. A force meter used to stretch the spring shows the magnitude of the stretching force, and it is equal to the magnitude of the spring force.

## Formula: Harmonic force
When the origin of the $x$-axis is at the point where the spring is at its rest length, and $x$ is the extension or compression of the spring from its rest length, the $x$-component of the force that the spring exerts on an object is
```kaavat
harmonic force :: F = -kx
```
where $F$ is the force of the spring on the object ($\text{N}$), $x$ the extension or compression of the spring from its rest length ($\text{m}$) and $k$ the **spring constant** of the spring ($\text{N/m}$). The minus sign gives the direction: the force is always opposite to the displacement. When $x > 0$, $F < 0$, and when $x < 0$, $F > 0$. The magnitude of the force is $k|x|$. The spring constant tells the stiffness of the spring, that is how many newtons of force are needed per metre of extension. The spring of a car's suspension can have tens of kilonewtons per metre, the spring of a toy only a few newtons per metre. For a horizontal spring the rest-length position is also the equilibrium position of the object, so the displacement from the equilibrium position is then $x$. The law holds only when the spring is neither stretched too much nor compressed too much.

### The spring constant from a measurement
The spring constant is determined by measuring. Weights are hung from the spring, and for each weight the extension $x$ of the spring is measured. A weight hanging at rest pulls the spring with a force equal to the weight $mg$ of the weight. This is the force stretching the spring, whose magnitude is
```latex
F_\text{v} = kx
```
where $F_\text{v}$ is the stretching force ($\text{N}$) and $x$ the extension ($\text{m}$). The measurement points are plotted in an $(x, F_\text{v})$ coordinate system and a straight line is fitted to them. In real data series the measurement points do not usually lie exactly on one line because of measurement uncertainty. The line passes through the origin, because without a stretching force the spring is at its rest length. The gradient (slope) of the line is the spring constant $k$.

<svg data-fig="kulmakerroin" viewBox="0 0 600 360" role="img" aria-label="Graph to scale, made-up example values: on the horizontal axis the extension x in metres from zero to 0.125, on the vertical axis the force F_v stretching the spring in newtons from zero to five. Five measurement points lie close to a straight line through the origin. Two points have been chosen on the line, x 0.025 metres with force 1.0 newtons and x 0.100 metres with force 4.0 newtons, and between them a gradient triangle has been drawn whose sides are Δx and ΔF_v. The gradient of the line is the spring constant k." style="max-width:100%;font-size:24px">
  <line x1="169.5" y1="300" x2="169.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247" y1="300" x2="247" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="325" y1="300" x2="325" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="402.5" y1="300" x2="402.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="253" x2="480" y2="253" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="205.5" x2="480" y2="205.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="158.5" x2="480" y2="158.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="111" x2="480" y2="111" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="64" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="494" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,300 L493,306 L493,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,38 L98,51 L86,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="169.5" y1="300" x2="169.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="134.5" y="309.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.025$</div></foreignObject>
  <line x1="247" y1="300" x2="247" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="212" y="309.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.050$</div></foreignObject>
  <line x1="325" y1="300" x2="325" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="290" y="309.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.075$</div></foreignObject>
  <line x1="402.5" y1="300" x2="402.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="367.5" y="309.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.100$</div></foreignObject>
  <line x1="85" y1="253" x2="92" y2="253" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="238.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="85" y1="205.5" x2="92" y2="205.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="191" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="85" y1="158.5" x2="92" y2="158.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="144" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="85" y1="111" x2="92" y2="111" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="96.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="85" y1="64" x2="92" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="49.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="82" y="7.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\text{v}\ (\text{N})$</div></foreignObject>
  <polyline points="92,300 449,83" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="169.5" y1="253" x2="402.5" y2="253" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="402.5" y1="253" x2="402.5" y2="111" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="269.5" y="258.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta x$</div></foreignObject>
  <foreignObject x="414.5" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta F_\text{v}$</div></foreignObject>
  <circle cx="154" cy="260" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="216" cy="227" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="278" cy="184.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="340.5" cy="151.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="402.5" cy="109" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="169.5" cy="253" r="8" fill="none" stroke="#c92a2a" stroke-width="2.5"/>
  <circle cx="402.5" cy="111" r="8" fill="none" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="101.5" y="68" width="70" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k = \dfrac{\Delta F_\text{v}}{\Delta x}$</div></foreignObject>
</svg>

The gradient is read from two points of the fitted line, not from two measurement points. In the example data of the graph the line passes through the points $(0.025\,\text{m};\ 1.0\,\text{N})$ and $(0.100\,\text{m};\ 4.0\,\text{N})$, so $k = \tfrac{3.0\,\text{N}}{0.075\,\text{m}} = 40\,\text{N/m}$. The points are chosen far apart, so that the uncertainty of the reading affects the result little. You can make the same measurement yourself in the laboratory investigation [Determining the spring constant](../fy10-jousivakio.html) (page in Finnish).

### Elastic potential energy
In the chapter *Kinetic energy, potential energy and mechanical energy* it was stated that a stretched spring has elastic potential energy. Now its magnitude can be calculated. When a spring is stretched slowly from its rest length to extension $x$, the stretching force does work, and the work is stored in the spring as potential energy. The work of a constant force, $W = Fs$, is the area of a rectangle in an $(s, F)$ graph (chapter *Conservation of mechanical energy and the work–energy principle*). The stretching force is not constant, however, but grows steadily from zero to $kx$. So the work is the triangle between the $(x, F_\text{v})$ graph and the $x$-axis, with base $x$ and height $kx$. The elastic potential energy is
```latex
E_\text{p} = \frac{1}{2}kx^2
```
where $E_\text{p}$ is the elastic potential energy ($\text{J}$), $k$ the spring constant ($\text{N/m}$) and $x$ the extension or compression ($\text{m}$). At the rest length the elastic potential energy is zero.

<svg data-fig="pinta-ala" viewBox="0 0 600 360" role="img" aria-label="Diagram without numerical values: the line F_v = kx going up from the origin. On the horizontal axis the extensions x and 2x, on the vertical axis the forces kx and 2kx. The triangle under the line for extension x is coloured orange and labelled E_p: its base is x and its height kx. The larger triangle for extension 2x is divided by dashed lines into four identical triangles, one of which is coloured, so its area is 4 E_p." style="max-width:100%;font-size:24px">
  <line x1="99" y1="306" x2="454" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M466,306 L453,312 L453,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="307" x2="100" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,38 L106,51 L94,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="248" y1="306" x2="248" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="238" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x$</div></foreignObject>
  <line x1="395.5" y1="306" x2="395.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="379" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2x$</div></foreignObject>
  <line x1="93" y1="201" x2="100" y2="201" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="186.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$kx$</div></foreignObject>
  <line x1="93" y1="95.5" x2="100" y2="95.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="81" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2kx$</div></foreignObject>
  <foreignObject x="70" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="472" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <foreignObject x="90" y="7.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\text{v}$</div></foreignObject>
  <polygon points="248,306 395.5,306 395.5,95.5 248,201" fill="#ffc078" fill-opacity="0.3"/>
  <polygon points="100,306 248,306 248,201" fill="#ffc078" fill-opacity="0.95"/>
  <line x1="248" y1="306" x2="248" y2="201" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="248" y1="201" x2="395.5" y2="201" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="248" y1="306" x2="395.5" y2="201" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="395.5" y1="306" x2="395.5" y2="95.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="100,306 425,74.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="184" y="260" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <foreignObject x="409.5" y="233.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$4E_\text{p}$</div></foreignObject>
  <path d="M401.5,304 h6 V97.5 h-6" fill="none" stroke="#e8590c" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="200" y="65.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$F_\text{v} = kx$</div></foreignObject>
</svg>

The triangle for double the extension is twice as wide and twice as tall, so four triangles of the original size fit in it. So the potential energy grows with the square of the extension, even though the force grows only in direct proportion. Because $x$ is squared, the energy is the same when the spring is stretched or compressed by the same amount. The units agree: $\tfrac{\text{N}}{\text{m}}\cdot\text{m}^2 = \text{N}\cdot\text{m} = \text{J}$.

## Worked example
A fisherman weighs a fish with a spring balance. When a fish of mass $1.20\,\text{kg}$ hangs at rest from the hook of the balance, the spring of the balance has stretched $3.0\,\text{cm}$. What is the spring constant of the spring, and how much elastic potential energy is stored in the spring? The masses of the spring and the hook are neglected.

<!-- vaihe -->

**Given and find.** Mass of the fish $m = 1.20\,\text{kg}$, extension of the spring $x = 3.0\,\text{cm}$ and $g = 9.81\,\text{m/s}^2$. We are asked for the spring constant $k$ and the elastic potential energy $E_\text{p}$.

<!-- vaihe -->

**Principle.** Choose the fish as the object. The Earth (weight $\overline{G}$) and the spring (spring force $\overline{F}$) act on it. The fish is at rest, so the forces cancel each other, and the magnitude of the spring force is $mg$. By Newton's third law the fish pulls the spring with a force of equal magnitude, so the force stretching the spring is $F_\text{v} = mg$. From this and the extension we get the spring constant. In the free-body diagram the $y$-axis points up.

<svg data-fig="esimerkki" viewBox="0 0 600 340" role="img" aria-label="Two pictures side by side. On the left the situation: a spring balance hangs from a hook, and a fish hangs at rest from the hook at its lower end. On the right the free-body diagram of the fish, the fish as a rectangle: weight G from the centre downwards and spring force F from the middle of the upper surface upwards, equally long. In the corner the y-axis pointing up." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy58-fish" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <line x1="60" y1="22" x2="200" y2="22" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M130,22 v14 q0,10 -8,10" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="112" y="48" width="36" height="120" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M130,52 L121,58 L139,65 L121,72 L139,79 L121,86 L139,93 L121,100 L139,107 L121,114 L139,121 L121,128 L139,135 L121,142 L139,149 L130,160" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="148" y1="70" x2="154" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="86" x2="154" y2="86" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="102" x2="154" y2="102" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="118" x2="154" y2="118" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="134" x2="154" y2="134" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="150" x2="154" y2="150" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="168" x2="130" y2="186" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M130,186 q8,0 8,8 q0,8 -8,8" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M72,250 Q130,196 190,250 Q130,300 72,250 Z" fill="url(#fy58-fish)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M190,250 L224,226 L220,274 Z" fill="#2f74b5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="92" cy="244" r="4" fill="#1f2933"/>
  <path d="M130,202 L130,212" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="270" y1="30" x2="270" y2="320" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="370" y="150" width="120" height="60" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="430" y1="180" x2="430" y2="263" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M430,280 L422,262 L438,262 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="261.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="430" y1="150" x2="430" y2="67" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M430,50 L438,68 L422,68 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="43.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <line x1="312" y1="300" x2="312" y2="265" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M312,256 L316.5,266 L307.5,266 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="302" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Rearranged formula.** The equation of motion is read from the free-body diagram: $F - mg = 0$, so the force stretching the spring is $F_\text{v} = kx = mg$. The spring constant is solved from this, and the energy is obtained from the extension:
```latex
\begin{aligned}
&k = \frac{mg}{x} \\
&E_\text{p} = \frac{1}{2}kx^2
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The extension is converted to metres: $x = 3.0\,\text{cm} = 3.0 \cdot 0.01\,\text{m} = 0.030\,\text{m}$.

<!-- vaihe -->

**Substitution.** Substitute the values with their units:
```latex
\begin{aligned}
&k = \frac{mg}{x} \\
&\phantom{k} = \frac{1.20\,\text{kg}\cdot 9.81\,\text{m/s}^2}{0.030\,\text{m}} \\
&\phantom{k} = 392.4\,\text{N/m} \\[4pt]
&E_\text{p} = \tfrac{1}{2}kx^2 \\
&\phantom{E_\text{p}} = \tfrac{1}{2}\cdot 392.4\,\tfrac{\text{N}}{\text{m}} \\
&\phantom{E_\text{p} =}\cdot (0.030\,\text{m})^2 \\
&\phantom{E_\text{p}} = 0.1766\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The spring constant is $k \approx 3.9 \cdot 10^{2}\,\text{N/m}$ and the elastic potential energy $E_\text{p} \approx 0.18\,\text{J}$, to two significant figures like the extension $3.0\,\text{cm}$.

<!-- vaihe -->

**Reasonableness.** The energy can also be calculated from the triangle of the $(x, F_\text{v})$ graph: $\tfrac{1}{2}F_\text{v}x = \tfrac{1}{2}\cdot 11.77\,\text{N}\cdot 0.030\,\text{m} \approx 0.18\,\text{J}$, the same result. A spring of about $400\,\text{N/m}$ stretches a centimetre under a force of about $4\,\text{N}$, which suits a balance used to weigh fish of a few kilograms. The energy is small because the extension is small.

## Common misconception
Many people think the force of the spring and the force stretching the spring are the same force. They are a Newton's third law pair: the stretching force acts on the spring and the spring force on the object, so only the spring force is drawn in the free-body diagram of the object. Another mistake is to read the minus sign in the expression $F = -kx$ as meaning that the force is always negative or small. The minus sign only gives the direction: the force points against the displacement, towards the equilibrium position, and is positive when $x < 0$. A third mistake is to assume that double the extension doubles the elastic potential energy. The force doubles, but the energy becomes four times as large, because it depends on the square of the extension.

## Summary
- A harmonic force is directly proportional to the displacement of an object from the equilibrium position and always points towards the equilibrium position: $F = -kx$.
- The minus sign gives the direction: the force is opposite to the displacement.
- The spring constant $k$ tells the stiffness of the spring. It is the gradient of the $(x, F_\text{v})$ graph, read from two points of the fitted line.
- The force stretching a spring acts on the spring and the spring force on the object: they are a Newton's third law pair.
- The elastic potential energy is the area of the triangle under the $(x, F_\text{v})$ graph, $E_\text{p} = \tfrac{1}{2}kx^2$. Double the extension gives four times the energy.
