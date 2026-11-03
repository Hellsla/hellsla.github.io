# Batteries and the charging circuit

> **Why** does a phone battery charge quickly at the start, but the last few percent take a long time?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a smartphone charging on a wooden table in the evening. A cable runs from the phone to a white charger in a wall socket. The phone screen shows a battery symbol that is almost full of green, and a lightning bolt beside it. There is also a coffee cup on the table, and a lamp lights the wall." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy69h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><radialGradient id="fy69h-glow"><stop offset="0" stop-color="#ffc078" stop-opacity="0.8"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient><linearGradient id="fy69h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="380" fill="url(#fy69h-wall)"/>
  <circle cx="200" cy="120" r="170" fill="url(#fy69h-glow)"/>
  <path d="M160,70 L240,70 L262,140 L138,140 Z" fill="#ffc078" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="192" y="40" width="16" height="30" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="820" y="160" width="150" height="150" rx="14" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="838" y="178" width="114" height="114" rx="10" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="850" y="196" width="90" height="92" rx="12" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="864" y="212" width="62" height="8" rx="4" fill="#e3dccb"/>
  <rect x="884" y="286" width="22" height="24" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="0" y="380" width="1200" height="220" fill="url(#fy69h-table)"/>
  <rect x="0" y="372" width="1200" height="16" fill="#e9c98a"/>
  <path d="M0,410 C300,404 700,418 1200,408" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,442 C300,436 700,450 1200,440" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,474 C300,468 700,482 1200,472" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,506 C300,500 700,514 1200,504" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,538 C300,532 700,546 1200,536" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,570 C300,564 700,578 1200,568" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M895,310 C895,380 900,430 820,452 C740,474 700,470 690,470" fill="none" stroke="#1f2933" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M895,310 C895,380 900,430 820,452 C740,474 700,470 690,470" fill="none" stroke="#c4ccd4" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M430,410 L690,428 Q712,430 710,452 L700,520 Q698,540 676,538 L414,520 Q394,518 396,496 L406,430 Q410,408 430,410 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M436,424 L682,441 Q694,442 693,454 L685,512 Q684,524 672,523 L424,506 Q412,505 413,493 L421,437 Q423,423 436,424 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M478,452 L598,460 L594,500 L474,492 Z" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>
  <path d="M600,470 L610,471 L608,489 L598,488 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M484,458 L572,464 L569,494 L480,488 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M484,458 L572,464 L569,494 L480,488 Z" fill="none" stroke="#2b8a3e" stroke-width="2" stroke-linejoin="round"/>
  <path d="M636,452 L620,480 L634,481 L626,506 L652,472 L638,471 L648,453 Z" fill="#ffc078" stroke="#e8590c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M210,380 L300,380 L292,470 Q290,486 274,486 L236,486 Q220,486 218,470 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M298,400 Q336,404 330,432 Q324,454 294,452" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round"/>
  <path d="M216,380 Q255,368 296,380" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M236,362 C224,346 248,334 236,318 C224,302 244,292 238,280" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M262,362 C250,346 274,334 262,318 C250,302 270,292 264,280" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
</svg>

## Key idea

### Disposable and rechargeable batteries
In both a disposable and a rechargeable battery, a chemical reaction keeps a source voltage $E$ between the terminals (chapter *Electromotive force and internal resistance*), and when the circuit is closed, chemical energy becomes electrical energy. A **disposable battery** (primary battery) is single-use: when its substances have reacted, the reaction cannot be safely reversed. A **rechargeable battery** can be charged: an external voltage source can drive its reaction backwards, and chemical energy is stored in the battery again. Phones, laptops and electric cars usually have a lithium-ion battery, and a car starter battery is a lead-acid battery.

A battery does not store electric charge. It is electrically neutral both full and empty: when it discharges, it only moves charges around the circuit, and every charge that leaves the positive terminal returns to the negative terminal. In the external circuit the current passes from the positive terminal to the negative terminal, and inside the battery from the negative terminal to the positive terminal.

### Charging reverses the current inside the battery
A battery is charged by connecting the positive terminal of the charger to the positive terminal of the battery and the negative terminal to the negative terminal. When the voltage of the charger is greater than the source voltage of the battery, the charger forces the current through the battery in the opposite direction to discharging: inside the battery from the positive terminal to the negative terminal. Then electrical energy becomes the chemical energy of the battery. In the figure the upper circuit discharges the battery into a lamp and the lower one charges it. When the direction of the current inside the battery reverses, the energy also flows in the other direction.

<svg data-fig="purku-lataus" viewBox="0 0 600 384" role="img" aria-label="Two circuit diagrams one above the other, not to scale. Upper: the battery discharges. The battery is on the left, the positive terminal, the long plate, at the top, and the lamp on the right. A purple current passes from the positive terminal of the battery along the upper wire to the lamp and along the lower wire to the negative terminal; inside the battery the current passes from the negative terminal to the positive terminal. An orange energy arrow points from the battery to the lamp. Lower: the battery is being charged. The charger is on the left and the battery on the right, both with the positive terminal at the top. The current passes from the positive terminal of the charger to the positive terminal of the battery, so inside the battery the current now passes from the positive terminal to the negative terminal, that is, in the opposite direction. The energy arrow points from the charger to the battery." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy69-en-d" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><linearGradient id="fy69-en-c" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <polyline points="130,108 130,60 430,60 430,108" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="130,124 130,172 430,172 430,124" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="12" y="7.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Discharging}$</div></foreignObject>
  <rect x="102" y="105" width="56" height="22" fill="#ffffff"/>
  <line x1="104" y1="108" x2="156" y2="108" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="117" y1="124" x2="143" y2="124" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="24" y="101.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <circle cx="430" cy="116" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="416" y1="102" x2="444" y2="130" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="416" y1="130" x2="444" y2="102" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="460" y="101.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lamp}$</div></foreignObject>
  <line x1="174" y1="136" x2="174" y2="107" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M174,94 L180.5,108 L167.5,108 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M196,123 L326,123 L326,133 L354,114 L326,95 L326,105 L196,105 Z" fill="url(#fy69-en-d)" stroke-linejoin="round"/>
  <path d="M290,60 L270,52 L270,68 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M370,172 L390,164 L390,180 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="268" y="23.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="205" y="135.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
  <line x1="12" y1="190" x2="588" y2="190" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <polyline points="130,300 130,252 430,252 430,300" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="130,316 130,364 430,364 430,316" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="12" y="199.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Charging}$</div></foreignObject>
  <rect x="92" y="268" width="76" height="80" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="102" y="297" width="56" height="22" fill="#ffffff"/>
  <line x1="104" y1="300" x2="156" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="117" y1="316" x2="143" y2="316" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <polyline points="130,268 130,300" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="130,316 130,348" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="4" y="293.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{charger}$</div></foreignObject>
  <rect x="402" y="297" width="56" height="22" fill="#ffffff"/>
  <line x1="404" y1="300" x2="456" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="417" y1="316" x2="443" y2="316" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="464" y="293.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <line x1="386" y1="288" x2="386" y2="317" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M386,330 L379.5,316 L392.5,316 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M196,315 L326,315 L326,325 L354,306 L326,287 L326,297 L196,297 Z" fill="url(#fy69-en-c)" stroke-linejoin="round"/>
  <path d="M290,252 L270,244 L270,260 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M370,364 L390,356 L390,372 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="268" y="215.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="205" y="327.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energy}$</div></foreignObject>
</svg>

### Battery capacity
The **capacity of a battery** tells how large a charge a fully charged battery can move through the circuit before it is empty. Charge is current times time, so capacity is often given in ampere-hours or milliampere-hours. One ampere-hour is the charge that a current of $1\,\text{A}$ moves in an hour: $1\,\text{Ah} = 1\,\text{A} \cdot 3600\,\text{s} = 3600\,\text{C}$. When the current is constant, the charge is the area under the graph of current against time. The battery in the figure gives a current of $0.50\,\text{A}$ for four hours, so its capacity is $2.0\,\text{Ah}$.

<svg data-fig="kapasiteetti" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the discharge current I in amperes as a function of time t in hours. The current is constant at 0.50 A from 0 to 4.0 h and then zero, when the battery is empty. The rectangle between the graph and the time axis is shaded; its area is the charge Q = It = 0.50 A · 4.0 h = 2.0 Ah." style="max-width:100%;font-size:24px">
  <line x1="169.5" y1="284" x2="169.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247" y1="284" x2="247" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="325" y1="284" x2="325" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="402.5" y1="284" x2="402.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="284" x2="480" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="227" x2="480" y2="227" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="170" x2="480" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="113" x2="480" y2="113" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="56" x2="480" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="284" x2="494" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,284 L493,290 L493,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="285" x2="92" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,30 L98,43 L86,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="169.5" y1="284" x2="169.5" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159.5" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="247" y1="284" x2="247" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="237" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="325" y1="284" x2="325" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="315" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="402.5" y1="284" x2="402.5" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="392.5" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="480" y1="284" x2="480" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="470" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="85" y1="227" x2="92" y2="227" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="212.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.2$</div></foreignObject>
  <line x1="85" y1="170" x2="92" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="155.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.4$</div></foreignObject>
  <line x1="85" y1="113" x2="92" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="98.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.6$</div></foreignObject>
  <line x1="85" y1="56" x2="92" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="41.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.8$</div></foreignObject>
  <foreignObject x="62" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="269.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{h})$</div></foreignObject>
  <foreignObject x="82" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <polygon points="92,284 92,141.5 402.5,141.5 402.5,284" fill="#b2f2bb" fill-opacity="0.75"/>
  <polyline points="92,141.5 402.5,141.5 402.5,284 472,284" fill="none" stroke="#7048e8" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="187" y="182" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = It$</div></foreignObject>
  <foreignObject x="172" y="216" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$= 2.0\,\text{Ah}$</div></foreignObject>
  <foreignObject x="197" y="105" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$0.50\,\text{A}$</div></foreignObject>
</svg>

### Charge alone does not tell the energy
Voltage tells how much energy per unit of charge is changed from one form to another (chapter *Electric circuit, current and voltage*). The energy of a battery is therefore voltage times charge, and its unit is the watt-hour: $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh} = 3600\,\text{J}$. The voltage used is the **nominal voltage** marked on the battery, which is the average voltage of the battery during discharging. In this chapter energy is denoted by $W$, because $E$ is the source voltage.

A phone battery with a capacity of $5000\,\text{mAh}$ and a nominal voltage of $3.85\,\text{V}$ stores the energy $3.85\,\text{V} \cdot 5.0\,\text{Ah} \approx 19.3\,\text{Wh}$. Batteries with different voltages can be compared only by energy: with the same number of ampere-hours, a $12\,\text{V}$ battery holds more than three times as much energy as a $3.7\,\text{V}$ battery.

### Why charging slows down at the end
The source voltage of a battery is not constant: it grows as the battery charges. The charging current is driven by the difference between the voltage of the charger and the source voltage of the battery, so when the source voltage grows, the current decreases. A phone charger keeps the voltage constant in the last phase of charging, and so the current becomes smaller and smaller as the battery fills. The last few percent charge with a small current and take a long time, and finally the control circuit of the charger cuts off the current. The battery also warms up in charging, because the current passes through its internal resistance.

## Formula: Battery capacity and charging current
The capacity of a battery, that is, the charge that a constant current moves in the time $t$:
```latex
Q = I t
```
where $Q$ is the charge (Ah or C), $I$ is the current (A) and $t$ is the time (h or s).

The energy stored in a battery:
```latex
W = U Q
```
where $W$ is the energy (Wh or J), $U$ is the nominal voltage of the battery (V) and $Q$ is the capacity of the battery (Ah or C).

### The charging circuit
The charging circuit in the figure has a charger whose voltage is $U_\text{ch}$, the resistance $R$ of the charger and wires, and a battery with source voltage $E$ and internal resistance $R_\text{s}$. Let us go around the loop in the direction of the current, starting from the negative terminal of the charger (chapter *Kirchhoff's laws and potential in a circuit*). The potential rises in the charger by $U_\text{ch}$ and drops in the resistor by $RI$ and in the internal resistance of the battery by $R_\text{s} I$. It also drops by the source voltage $E$ of the battery, because the current passes through the battery from the positive terminal to the negative terminal. By the voltage law, $U_\text{ch} - RI - R_\text{s} I - E = 0$.

<svg data-fig="latauspiiri" viewBox="0 0 600 360" role="img" aria-label="Circuit diagram of the charging circuit, not to scale. On the left is a charger whose voltage is U_ch, with the positive terminal at the top. In the upper wire are the resistance R of the charger and wires and an ammeter A. On the right is the battery bounded by a dashed line: inside it are the internal resistance R_s and the source voltage E, whose positive terminal is at the top. The terminals of the battery are at the edge of the dashed line, and a voltmeter V is connected between them; it shows the terminal voltage U. Purple current arrows pass from the positive terminal of the charger along the upper wire to the positive terminal of the battery, down through the battery and along the lower wire back to the negative terminal of the charger." style="max-width:100%;font-size:24px">
  <polyline points="86,183 86,82 430,82 430,108" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="86,199 86,300 430,300 430,274" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="430,108 430,228" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="430,244 430,274" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="48" y="145" width="76" height="92" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <polyline points="86,145 86,183" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="86,199 86,237" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="58" y="180" width="56" height="22" fill="#ffffff"/>
  <line x1="60" y1="183" x2="112" y2="183" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="73" y1="199" x2="99" y2="199" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="132" y="174.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_\text{ch}$</div></foreignObject>
  <rect x="184" y="71" width="60" height="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="199" y="37.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <circle cx="316" cy="82" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="301" y="67.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <rect x="390" y="108" width="80" height="166" rx="6" fill="none" stroke="#6b7480" stroke-width="2" stroke-dasharray="7 6"/>
  <rect x="420" y="131" width="20" height="50" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="402" y="225" width="56" height="22" fill="#ffffff"/>
  <line x1="404" y1="228" x2="456" y2="228" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="417" y1="244" x2="443" y2="244" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="332" y="141.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="352" y="221.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <circle cx="430" cy="108" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="430" cy="274" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="390" y="317.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <polyline points="430,108 532,108 532,171" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="532,211 532,274 430,274" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="430" cy="108" r="4" fill="#1f2933"/>
  <circle cx="430" cy="274" r="4" fill="#1f2933"/>
  <circle cx="532" cy="191" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="517" y="176.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="558" y="142.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <path d="M160,82 L140,74 L140,90 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M390,82 L370,74 L370,90 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M250,300 L270,292 L270,308 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M430,206 L422,186 L438,186 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="138" y="41.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

The charging current is therefore
```latex
I = \frac{U_\text{ch} - E}{R + R_\text{s}}
```
where $I$ is the charging current (A), $U_\text{ch}$ is the voltage of the charger (V), $E$ is the source voltage of the battery (V), $R$ is the resistance of the charger and wires ($\Omega$) and $R_\text{s}$ is the internal resistance of the battery ($\Omega$). The battery charges only when $U_\text{ch} > E$. If $U_\text{ch} < E$, the current reverses and the battery discharges into the charger, unless the charger has a diode that lets the current pass in one direction only.

The terminal voltage of the battery during charging is
```latex
U = E + R_\text{s} I
```
where $U$ is the voltage between the terminals of the battery (V). In charging the terminal voltage is greater than the source voltage, in discharging smaller, $U = E - R_\text{s} I$.

In the graph the loop of the charging circuit is traced when $U_\text{ch} = 4.5\,\text{V}$, $R = 0.40\,\Omega$, $E = 3.40\,\text{V}$ and $R_\text{s} = 0.10\,\Omega$, so the charging current is $2.2\,\text{A}$. The rise of $4.5\,\text{V}$ in the charger equals the sum of the drops $0.88\,\text{V}$, $0.22\,\text{V}$ and $3.40\,\text{V}$. The potential of the positive terminal of the battery, $3.62\,\text{V}$, is the terminal voltage.

<svg data-fig="potentiaali" viewBox="0 0 600 372" role="img" aria-label="Potential graph, vertical axis to scale, horizontal axis schematic: the loop of the charging circuit is traced from the negative terminal A of the charger through the charger, the resistor R and the battery back to A, when the voltage of the charger is 4.5 V, R = 0.40 ohms, the source voltage of the battery is 3.40 V and its internal resistance is 0.10 ohms, so the current is 2.2 A. In the charger the potential rises by 4.5 volts. In the resistor R it drops by 0.88 V, and at the positive terminal B of the battery it is 3.62 V, which is the terminal voltage. In the internal resistance of the battery it drops by 0.22 V to the value 3.40 V at point C, and at the source voltage of the battery by 3.40 V to zero. The current passes through the battery from the positive terminal to the negative terminal, so the potential drops in the battery." style="max-width:100%;font-size:24px">
  <line x1="96" y1="245.5" x2="500" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="204.5" x2="500" y2="204.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="164" x2="500" y2="164" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="123" x2="500" y2="123" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="82.5" x2="500" y2="82.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="514" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,286 L513,292 L513,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,36 L102,49 L90,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="245.5" x2="96" y2="245.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="231" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="204.5" x2="96" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="190" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="164" x2="96" y2="164" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="149.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="123" x2="96" y2="123" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="108.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="89" y1="82.5" x2="96" y2="82.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="68" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="532" y="271.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{point}$</div></foreignObject>
  <foreignObject x="86" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{V})$</div></foreignObject>
  <rect x="131.5" y="62" width="30.5" height="224" fill="#eef5f9"/>
  <foreignObject x="116.5" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_\text{ch}$</div></foreignObject>
  <rect x="227.5" y="62" width="50.5" height="224" fill="#eef5f9"/>
  <foreignObject x="222.5" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <rect x="348.5" y="62" width="50.5" height="224" fill="#eef5f9"/>
  <foreignObject x="344" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <rect x="424" y="62" width="30.5" height="224" fill="#eef5f9"/>
  <foreignObject x="409.5" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <line x1="97" y1="245.5" x2="500" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="204.5" x2="500" y2="204.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="164" x2="500" y2="164" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="123" x2="500" y2="123" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="82.5" x2="500" y2="82.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="64" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,286 146.5,286 146.5,102.5 227.5,102.5 278,138.5 348.5,138.5 399,147.5 439.5,147.5 439.5,286 500,286" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="96" y1="286" x2="96" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="82" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <circle cx="96" cy="286" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="313" y1="286" x2="313" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="299" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <circle cx="313" cy="138.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="419" y1="286" x2="419" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="405" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$C$</div></foreignObject>
  <circle cx="419" cy="147.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="500" y1="286" x2="500" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="486" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <circle cx="500" cy="286" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="156.5" y="210.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+4.5\,\text{V}$</div></foreignObject>
  <foreignObject x="202.5" y="149.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$-0.88\,\text{V}$</span></div></foreignObject>
  <foreignObject x="268" y="100" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$3.62\,\text{V}$</span></div></foreignObject>
  <foreignObject x="324" y="149.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$-0.22\,\text{V}$</span></div></foreignObject>
  <foreignObject x="329.5" y="210.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$-3.40\,\text{V}$</span></div></foreignObject>
</svg>

### Energy in charging
The power of the charger is $P = U_\text{ch} I$ (chapter *Electric power and the heating of a resistor*), so a charger with a constant voltage delivers the energy $W_\text{ch} = U_\text{ch} Q$ when the charge $Q$ passes through the battery. Only the part given by the source voltage is stored in the battery as chemical energy, and the rest becomes internal energy of the resistances $R$ and $R_\text{s}$, which is transferred to the surroundings as heat. The efficiency of charging is
```latex
\eta = \frac{W_\text{batt}}{W_\text{ch}}
```
where $W_\text{batt}$ is the energy stored in the battery as chemical energy (Wh) and $W_\text{ch}$ is the energy delivered by the charger (Wh).

The efficiency is at most $100\,\%$. In real devices it stays below $100\,\%$, because part of the energy taken does not end up in the battery. In the figure a battery with a capacity of $2.0\,\text{Ah}$ is charged from empty to full with a $4.5\,\text{V}$ charger. The charger delivers $9.0\,\text{Wh}$ and $7.6\,\text{Wh}$ is stored in the battery, so the efficiency is about $84\,\%$. The greater the voltage of the charger compared with the source voltage of the battery, the greater the current and the faster the charging, but the greater the part of the energy that becomes internal energy.

<svg data-fig="energia" viewBox="0 0 600 340" role="img" aria-label="Energy flow diagram to scale: the width of the arrows is proportional to the energy. In a full charge from empty to full the charger delivers 9.0 Wh of energy, when the voltage of the charger is 4.5 V and the capacity of the battery is 2.0 Ah. Of this, 7.6 Wh is stored in the battery as chemical energy and continues as an arrow to the right. Two narrow arrows branch downwards: 1.1 Wh becomes internal energy of the charger and wires and 0.3 Wh internal energy of the battery, and they are transferred to the surroundings as heat." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy69-flow" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <path d="M40,96 L520,96 L520,82 L566,134 L520,186 L520,172 L373,172 L373,266 L381,266 L371.5,290 L362,266 L370,266 L370,175 L261,175 L261,266 L270,266 L255.5,292 L241,266 L250,266 L250,186 L40,186 Z" fill="url(#fy69-flow)" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="40" y="55.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W_\text{ch} = 9.0\,\text{Wh}$</div></foreignObject>
  <foreignObject x="40" y="23.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{from the charger}$</div></foreignObject>
  <foreignObject x="306" y="23.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{stored in the battery}$</div></foreignObject>
  <foreignObject x="466" y="55.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$7.6\,\text{Wh}$</div></foreignObject>
  <foreignObject x="133.5" y="299.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.1\,\text{Wh}$</div></foreignObject>
  <foreignObject x="33.5" y="267.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{charger and wires}$</div></foreignObject>
  <foreignObject x="393.5" y="299.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0.3\,\text{Wh}$</div></foreignObject>
  <foreignObject x="393.5" y="267.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{battery}$</div></foreignObject>
  <foreignObject x="40" y="207.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{to internal energy:}$</div></foreignObject>
</svg>

## Worked example
The source voltage of a battery cell is $3.70\,\text{V}$ and its internal resistance is $0.10\,\Omega$. The cell is charged with a charger whose voltage is $4.20\,\text{V}$, and the resistance of the charger and wires is $0.15\,\Omega$ in total. How large is the charging current, and what is the terminal voltage of the cell during charging?

<!-- vaihe -->

**Given and find.** $E = 3.70\,\text{V}$, $R_\text{s} = 0.10\,\Omega$, $U_\text{ch} = 4.20\,\text{V}$ and $R = 0.15\,\Omega$. We are asked for the charging current $I$ and the terminal voltage $U$.

<!-- vaihe -->

**Principle.** The circuit has one loop, so by the voltage law the voltage of the charger equals the sum of the potential drops: the voltages of the resistances and the source voltage of the battery, because the current passes through the battery from the positive terminal to the negative terminal. The terminal voltage is the source voltage of the battery plus the voltage of its internal resistance.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&U_\text{ch} - RI - R_\text{s} I - E = 0 \\
&I = \frac{U_\text{ch} - E}{R + R_\text{s}} \\
&U = E + R_\text{s} I
\end{aligned}
```

<!-- vaihe -->

**Conversions.** Not needed: all the quantities are in base units, and $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&I = \frac{U_\text{ch} - E}{R + R_\text{s}} \\
&\phantom{I} = \frac{4.20\,\text{V} - 3.70\,\text{V}}{0.15\,\Omega + 0.10\,\Omega} \\
&\phantom{I} = \frac{0.50\,\text{V}}{0.25\,\Omega} = 2.0\,\text{A} \\
&U = 3.70\,\text{V} + 0.10\,\Omega \cdot 2.0\,\text{A} \\
&\phantom{U} = 3.90\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The charging current is $2.0\,\text{A}$, two significant figures like the voltage difference $0.50\,\text{V}$ and the resistances. The terminal voltage is $3.90\,\text{V}$, to a hundredth of a volt like the given voltages.

<!-- vaihe -->

**Reasonableness.** Calculated from the charger side, the terminal voltage is $4.20\,\text{V} - 0.15\,\Omega \cdot 2.0\,\text{A} = 3.90\,\text{V}$, the same result. The terminal voltage lies between the source voltage and the voltage of the charger, as it should in charging. If the source voltage were left out, the current would be $16.8\,\text{A}$, which is more than eight times too much.

## Common misconception
Many people think that electric charge is put into the battery in charging and that the charge has run out of an empty battery. But the battery is electrically neutral all the time. In charging, chemical energy is stored in it, and the capacity tells how large a charge can pass through the battery when it discharges.

Another mistake is to compare batteries only by milliampere-hours. The ampere-hour is a unit of charge, not of energy. A power bank with $10\,000\,\text{mAh}$ at a voltage of $3.7\,\text{V}$ holds less energy than a laptop battery with $4000\,\text{mAh}$ at a voltage of $11.4\,\text{V}$: $37\,\text{Wh}$ and $45.6\,\text{Wh}$. A third mistake is to calculate the charging current from the voltage of the charger alone. The current is driven by the difference between the voltage of the charger and the source voltage of the battery.

## Summary
- A disposable battery is single-use and a rechargeable battery can be charged. Both change chemical energy into electrical energy; a rechargeable battery stores not charge but chemical energy.
- The capacity of a battery is the charge $Q = It$, usually in ampere-hours: $1\,\text{Ah} = 3600\,\text{C}$. The energy of a battery is $W = UQ$ in watt-hours, $1\,\text{Wh} = 3600\,\text{J}$, and batteries are compared by energy.
- In charging the current passes through the battery from the positive terminal to the negative terminal. The charging current is $I = \tfrac{U_\text{ch} - E}{R + R_\text{s}}$, so a battery charges only when the voltage of the charger is greater than the source voltage of the battery. The terminal voltage in charging is $U = E + R_\text{s} I$.
- The source voltage grows as the battery charges, so with a constant-voltage charger the current decreases and charging slows down towards the end.
- Part of the energy of the charger becomes internal energy of the resistances, so the efficiency of charging is below $100\,\%$.
