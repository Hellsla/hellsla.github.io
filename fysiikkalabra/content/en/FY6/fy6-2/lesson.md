# Measurements in an electric circuit

> **Why** is an ammeter connected to a circuit in a different way from a voltmeter, and what happens if the connections get mixed up?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a work bench in a school laboratory. On the bench there is a breadboard where a battery holder and a lamp holder are connected with wires in the same circuit, and the lamp is lit. Next to it is a grey digital multimeter whose red and black test leads touch the two terminals of the lamp holder." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy62h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><linearGradient id="fy62h-bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy62h-glow"><stop offset="0" stop-color="#ffc078" stop-opacity="0.95"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy62h-wall)"/>
  <rect x="60" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="240" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="420" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="600" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="780" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="960" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="1140" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="0" y="330" width="1200" height="270" fill="url(#fy62h-bench)"/>
  <rect x="0" y="322" width="1200" height="16" fill="#e9c98a"/>
  <path d="M0,360 C300,354 700,368 1200,358" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,394 C300,388 700,402 1200,392" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,428 C300,422 700,436 1200,426" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,462 C300,456 700,470 1200,460" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,496 C300,490 700,504 1200,494" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,530 C300,524 700,538 1200,528" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,564 C300,558 700,572 1200,562" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <rect x="250" y="380" width="470" height="170" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="262" y="392" width="446" height="146" rx="6" fill="#eef5f9"/>
  <rect x="290" y="420" width="190" height="76" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="302" y="432" width="52" height="52" rx="6" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="342" y="446" width="12" height="24" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="360" y="432" width="52" height="52" rx="6" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="400" y="446" width="12" height="24" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="418" y="432" width="52" height="52" rx="6" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="458" y="446" width="12" height="24" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="570" y="444" width="100" height="52" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="580" cy="470" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="660" cy="470" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="620" cy="392" r="110" fill="url(#fy62h-glow)"/>
  <rect x="600" y="418" width="40" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M592,420 C580,370 594,344 620,344 C646,344 660,370 648,420 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M608,418 L612,388 L620,398 L628,388 L632,418" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  <path d="M480,458 C520,458 540,470 580,470" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M660,470 C700,470 700,530 520,530 C380,530 300,530 290,470" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="800" y="210" width="250" height="350" rx="26" fill="#c4ccd4" stroke="#1f2933" stroke-width="4"/>
  <rect x="814" y="224" width="222" height="322" rx="18" fill="#6c757d"/>
  <rect x="842" y="248" width="166" height="74" rx="8" fill="#e3dccb" stroke="#1f2933" stroke-width="3"/>
  <rect x="858" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <rect x="894" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <rect x="930" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <rect x="966" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <circle cx="925" cy="410" r="50" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <circle cx="925" cy="410" r="20" fill="#1f2933"/>
  <line x1="925" y1="410" x2="900" y2="372" stroke="#ffffff" stroke-width="8" stroke-linecap="round"/>
  <line x1="868" y1="400" x2="854" y2="397.5" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <line x1="891.5" y1="362.5" x2="883.5" y2="351" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <line x1="958.5" y1="362.5" x2="966.5" y2="351" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <line x1="982" y1="400" x2="996" y2="397.5" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="860" cy="508" r="15" fill="#1f2933" stroke="#ffffff" stroke-width="4"/>
  <circle cx="925" cy="508" r="15" fill="#1f2933" stroke="#c92a2a" stroke-width="4"/>
  <circle cx="990" cy="508" r="15" fill="#1f2933" stroke="#c92a2a" stroke-width="4"/>
  <path d="M860,508 C860,600 720,600 700,560 C686,530 662,510 662,486" fill="none" stroke="#1f2933" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M925,508 C930,620 600,620 560,560 C540,530 574,500 578,486" fill="none" stroke="#c92a2a" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="652" y="474" width="20" height="30" rx="4" fill="#1f2933"/>
  <rect x="568" y="474" width="20" height="30" rx="4" fill="#c92a2a"/>
</svg>

## Key idea

### An ammeter is connected in series
An **ammeter** measures how large an electric current passes through it. That is why the current to be measured has to pass through the meter: the circuit is opened at the point whose current we want to know, and the meter is placed in the gap. The meter is then **in series** with the other components. In a circuit without branches the current is the same at every point, because charge neither disappears nor accumulates anywhere. A lamp changes electrical energy into light and internal energy of the filament, but it does not use up current. An ammeter can therefore be connected at any point of a circuit without branches, and it always shows the same reading.

### A voltmeter is connected in parallel
Voltage is a quantity between two points (chapter *Circuit, electric current and voltage*). A **voltmeter** measures the voltage between the two points that its leads are touched to. The voltage of a lamp is measured by touching both terminals of the lamp: the circuit is not opened, but the meter comes **in parallel** with the lamp. The red lead of the meter is touched to the terminal that is closer to the positive terminal of the battery, so the reading is positive.

<svg data-fig="connections" viewBox="0 0 600 344" role="img" aria-label="Two circuit diagrams. On the left the battery, the lamp and the ammeter A are in the same loop one after another: the ammeter is in series with the lamp, and the same current I passes through the battery, the meter and the lamp. On the right the battery and the lamp form a loop, and the voltmeter V is connected between the terminals of the lamp, in parallel with the lamp. The purple arrows show the direction of the current from the positive terminal of the battery to the negative terminal." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy62-c1-glow"><stop offset="0" stop-color="#ffc078" stop-opacity="0.95"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient><radialGradient id="fy62-c2-glow"><stop offset="0" stop-color="#ffc078" stop-opacity="0.95"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient></defs>
  <line x1="300" y1="16" x2="300" y2="328" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <polyline points="138,236 40,236 40,100 78,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="122,100 174,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="214,100 260,100 260,236 162,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="100" cy="100" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="90" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <circle cx="194" cy="100" r="46" fill="url(#fy62-c1-glow)"/>
  <circle cx="194" cy="100" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="180" y1="86" x2="208" y2="114" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="180" y1="114" x2="208" y2="86" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="143" y1="212" x2="143" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="157" y1="224" x2="157" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="40" y1="192" x2="40" y2="176" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M40,160 L47,176 L33,176 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="56" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="260" y1="144" x2="260" y2="160" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M260,176 L253,160 L267,160 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="102.5" y="275.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ammeter}$</div></foreignObject>
  <foreignObject x="96" y="305.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in series}$</div></foreignObject>
  <polyline points="438,236 340,236 340,100 430,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="470,100 560,100 560,236 462,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="450" cy="100" r="46" fill="url(#fy62-c2-glow)"/>
  <circle cx="450" cy="100" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="436" y1="86" x2="464" y2="114" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="436" y1="114" x2="464" y2="86" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <polyline points="398,100 398,44 428,44" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="472,44 502,44 502,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="398" cy="100" r="5" fill="#1f2933"/>
  <circle cx="502" cy="100" r="5" fill="#1f2933"/>
  <circle cx="450" cy="44" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="440" y="29.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <line x1="443" y1="212" x2="443" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="457" y1="224" x2="457" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="340" y1="192" x2="340" y2="176" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M340,160 L347,176 L333,176 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="356" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="560" y1="144" x2="560" y2="160" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M560,176 L553,160 L567,160 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="390" y="275.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{voltmeter}$</div></foreignObject>
  <foreignObject x="383.5" y="305.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in parallel}$</div></foreignObject>
</svg>

### The multimeter
In a laboratory, current and voltage are usually measured with a **multimeter**: the same device measures, depending on the position of the selector, voltage, current and often other quantities too. The black lead always belongs in the jack COM. The red lead belongs in the jack $\text{V}\ \text{mA}$ when measuring voltage and small currents and in the jack $10\,\text{A}$ when measuring large currents. The selector chooses both the quantity and the **measuring range**, which is the largest value that the meter shows in this position. On the range $20\,\text{V}$ the display shows at most $19.99\,\text{V}$; at a larger voltage the display shows OL (*overload*), which means that the value is over the measuring range.

<svg data-fig="multimeter" viewBox="0 0 600 360" role="img" aria-label="Drawing of a digital multimeter. At the top the display with the reading 1.500 V. In the middle the selector, around which are the measuring ranges 2 V, 20 V, 200 mA and 10 A; the pointer is on the range 2 V. At the bottom three jacks: COM, V mA and 10 A. The place of the black lead is COM and that of the red lead V mA or 10 A. On the right the labels display, selector and jacks." style="max-width:100%;font-size:24px">
  <rect x="52" y="14" width="256" height="332" rx="22" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="62" y="24" width="236" height="312" rx="14" fill="#6c757d"/>
  <rect x="84" y="34" width="192" height="78" rx="8" fill="#e3dccb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="72" y="50" width="150" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:40px">$1.500$</div></foreignObject>
  <foreignObject x="228" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <circle cx="180" cy="206" r="32" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="180" cy="206" r="14" fill="#1f2933"/>
  <line x1="145.5" y1="200" x2="138.5" y2="198.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="86.5" y="179" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffc078">$2\,\text{V}$</div></foreignObject>
  <line x1="160" y1="177.5" x2="156" y2="171.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109.5" y="132.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$20\,\text{V}$</div></foreignObject>
  <line x1="200" y1="177.5" x2="204" y2="171.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="180" y="132.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$200\,\text{mA}$</div></foreignObject>
  <line x1="214.5" y1="200" x2="221.5" y2="198.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="222" y="179" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <line x1="180" y1="206" x2="152.5" y2="201" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <circle cx="110" cy="290" r="12" fill="#1f2933" stroke="#ffffff" stroke-width="3"/>
  <foreignObject x="87.5" y="307.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{COM}$</div></foreignObject>
  <circle cx="180" cy="290" r="12" fill="#1f2933" stroke="#c92a2a" stroke-width="3"/>
  <foreignObject x="155.5" y="307.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{V}\ \text{mA}$</div></foreignObject>
  <circle cx="250" cy="290" r="12" fill="#1f2933" stroke="#c92a2a" stroke-width="3"/>
  <foreignObject x="221" y="307.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <line x1="312" y1="73" x2="350" y2="73" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="358" y="58.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{display}$</div></foreignObject>
  <line x1="312" y1="206" x2="350" y2="206" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="358" y="191.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{selector}$</div></foreignObject>
  <line x1="312" y1="290" x2="350" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="358" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{jacks}$</div></foreignObject>
</svg>

### Choosing the measuring range
On a smaller range the display shows more decimals. On the range $20\,\text{V}$ the voltage of a lamp appears as $1.50\,\text{V}$, on the range $2\,\text{V}$ as $1.500\,\text{V}$: the last digit tells the **resolution**, that is the smallest step that the display can take. That is why we measure on the smallest range on which the reading still fits. When the order of magnitude is not known, we start from the largest range and move to a smaller one. When measuring current, this is also a safety matter, because too large a current blows the fuse of the meter.

### The meter affects the circuit
Every component has a **resistance**, which describes how strongly it opposes an electric current; the quantity is made more precise in the chapter *Resistance and Ohm's law*. The resistance of an ammeter connected in series is very small, so that the meter hardly decreases the current that it measures. The resistance of a voltmeter connected in parallel is very large, for example $10\,\text{M}\Omega$, so that hardly any current passes through the meter past the component. An ideal meter would not change the circuit at all; a real one changes it a little, which is one source of measurement uncertainty.

A wrongly connected meter changes the circuit a lot. If an ammeter is connected in parallel with a lamp, the current passes almost entirely through the meter of small resistance past the lamp: the lamp goes out, and the current can grow so large that the fuse of the meter blows. When the fuse has blown, the meter is out of the circuit and the lamp lights up again. A current path that bypasses a component like this is called a short circuit. If, on the other hand, a voltmeter is connected in series, its large resistance decreases the current of the whole circuit to almost zero: the lamp goes out, and the meter shows approximately the voltage of the battery.

<svg data-fig="wrong" viewBox="0 0 600 352" role="img" aria-label="Two wrong connections. On the left the ammeter A is connected in parallel with the lamp. The current passes almost entirely through the ammeter of small resistance, which is shown by the thick purple arrow: the lamp is not lit, and the current is large. On the right the voltmeter V is in series with the lamp. The large resistance of the meter decreases the current to almost zero, so the lamp is not lit and there are no current arrows." style="max-width:100%;font-size:24px">
  <line x1="300" y1="16" x2="300" y2="336" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <polyline points="138,236 40,236 40,112 130,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="170,112 260,112 260,236 162,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="150" cy="112" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="136" y1="98" x2="164" y2="126" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="136" y1="126" x2="164" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <polyline points="98,112 98,50 128,50" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="172,50 202,50 202,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="98" cy="112" r="5" fill="#1f2933"/>
  <circle cx="202" cy="112" r="5" fill="#1f2933"/>
  <circle cx="150" cy="50" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="140" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <line x1="98" y1="100" x2="98" y2="84" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M98,62 L108,84 L88,84 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="202" y1="60" x2="202" y2="76" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M202,98 L192,76 L212,76 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="143" y1="212" x2="143" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="157" y1="224" x2="157" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="40" y1="174" x2="40" y2="158" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M40,136 L50,158 L30,158 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="56" y="143.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\text{large } I$</div></foreignObject>
  <foreignObject x="102.5" y="283.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ammeter}$</div></foreignObject>
  <foreignObject x="83.5" y="313.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in parallel}$</div></foreignObject>
  <polyline points="438,236 340,236 340,112 378,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="422,112 464,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="504,112 560,112 560,236 462,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="400" cy="112" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="390" y="97.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <circle cx="484" cy="112" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="470" y1="98" x2="498" y2="126" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="470" y1="126" x2="498" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="443" y1="212" x2="443" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="457" y1="224" x2="457" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="427.5" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \approx 0$</div></foreignObject>
  <foreignObject x="390" y="283.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{voltmeter}$</div></foreignObject>
  <foreignObject x="396" y="313.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in series}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/multimeter-breadboard.webp" alt="A red and a black probe touch a breadboard holding a resistor and a red LED."><figcaption>Multimeter probes on a breadboard. When the probes are placed at two points of a circuit, the meter is connected in parallel with the part between them and measures its voltage.</figcaption></figure>

## Formula: Error limit of a multimeter

### The error limit given by the manufacturer
The reading of a meter is not exactly the true value of the quantity being measured. The manufacturer of a digital meter gives in the manual for every range an **error limit** in the form $\pm(p + n\ \text{digits})$: the error limit is a percentage $p$ of the reading plus $n$ steps of the last digit. The error limit given by the manufacturer tells how much the reading of a meter that is in order and used according to the instructions can at most differ from the true value. However, the total uncertainty of a measurement can also be affected by the measuring method, the effect of the meter on the circuit and other sources of error.

| Range | Resolution | Error limit |
|---|---|---|
| voltage $2\,\text{V}$ | $0.001\,\text{V}$ | $\pm(0.5\,\% + 2\ \text{digits})$ |
| voltage $20\,\text{V}$ | $0.01\,\text{V}$ | $\pm(0.5\,\% + 2\ \text{digits})$ |
| current $200\,\text{mA}$ | $0.1\,\text{mA}$ | $\pm(1.0\,\% + 2\ \text{digits})$ |
| current $10\,\text{A}$ | $0.01\,\text{A}$ | $\pm(2.0\,\% + 3\ \text{digits})$ |

### Calculating the error limit
The error limit of a reading $x$ is
```latex
\Delta x = p \cdot x + n \cdot r
```
where $\Delta x$ is the error limit, $x$ the reading, $p$ the percentage given by the manufacturer as a decimal number ($0.5\,\% = 0.005$), $n$ the number of digits and $r$ the resolution of the range. The result is written in the form $x \pm \Delta x$, for example $U = 4.50\,\text{V} \pm 0.04\,\text{V}$. The notation is the same as for an error estimate, but here $\Delta x$ is the meter's own error limit, not the uncertainty of the whole measurement. The accuracy of different measurements is compared with the **relative error limit**
```latex
\frac{\Delta x}{x}
```
which is a pure number and is usually given as a percentage.

### Why the smallest suitable range
If the ranges have the same $p$ and the same $n$, as this meter's voltage ranges do, the percentage part $p \cdot x$ is the same on all of them, but the share of the digits $n \cdot r$ decreases to a tenth when we move to a range ten times smaller. When the reading is small compared with the range, the share of the digits dominates: a current of $0.02\,\text{A}$ on the range $10\,\text{A}$ is almost a guess, because three steps of the last digit are already $0.03\,\text{A}$.

<svg data-fig="error-bands" viewBox="0 0 600 312" role="img" aria-label="Picture to scale: the voltage axis from 1.46 V to 1.54 V. The upper segment shows the reading 1.50 V obtained on the range 20 V and its error limit ±0.03 V, that is the interval 1.47 V–1.53 V. The lower segment shows the reading 1.500 V obtained on the range 2 V and its error limit ±0.010 V, that is the interval 1.490 V–1.510 V. The segment of the lower range is about a third of the length of the upper one." style="max-width:100%;font-size:24px">
  <line x1="120" y1="40" x2="120" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="40" x2="180" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="40" x2="240" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="40" x2="300" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="40" x2="360" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="40" x2="420" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="40" x2="480" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="252" x2="554" y2="252" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,252 L553,258 L553,246 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="252" x2="60" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="31" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.46$</div></foreignObject>
  <line x1="120" y1="252" x2="120" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="252" x2="180" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="151" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.48$</div></foreignObject>
  <line x1="240" y1="252" x2="240" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="252" x2="300" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="271" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.50$</div></foreignObject>
  <line x1="360" y1="252" x2="360" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="252" x2="420" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="391" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.52$</div></foreignObject>
  <line x1="480" y1="252" x2="480" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="252" x2="540" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="511" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.54$</div></foreignObject>
  <foreignObject x="488" y="211.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="60" y="27.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{range } 20\,\text{V}$</div></foreignObject>
  <rect x="120" y="66" width="360" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="120" y1="58" x2="120" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="480" y1="58" x2="480" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="78" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="492" y="63.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0.03\,\text{V}$</div></foreignObject>
  <foreignObject x="60" y="125.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{range } 2\,\text{V}$</div></foreignObject>
  <rect x="240" y="164" width="120" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="240" y1="156" x2="240" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="360" y1="156" x2="360" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="176" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="372" y="161.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0.010\,\text{V}$</div></foreignObject>
</svg>

## Worked example
The voltage of a lamp is measured twice with a multimeter. On the range $20\,\text{V}$ the display shows $1.50\,\text{V}$ and on the range $2\,\text{V}$ the display shows $1.500\,\text{V}$. The error limit of both ranges is $\pm(0.5\,\% + 2\ \text{digits})$. How large is the error limit of the reading on each range, and which range should be chosen?

<!-- vaihe -->

**Given and asked.** The readings $U_{20} = 1.50\,\text{V}$ (resolution $r_{20} = 0.01\,\text{V}$) and $U_2 = 1.500\,\text{V}$ (resolution $r_2 = 0.001\,\text{V}$), $p = 0.5\,\%$ and $n = 2$. We are asked for the error limits $\Delta U_{20}$ and $\Delta U_2$.

<!-- vaihe -->

**Principle.** The manufacturer's error limit is a share of the reading plus two steps of the last digit. The reading is the same on both ranges, so the ranges differ only in their resolution.

<!-- vaihe -->

**Formula solved.** The formula gives the error limit directly when the resolution of each range is substituted:
```latex
\begin{aligned}
&\Delta U_{20} = p \cdot U_{20} + n \cdot r_{20} \\
&\Delta U_2 = p \cdot U_2 + n \cdot r_2
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The percentage is written as a decimal number: $p = 0.5\,\% = 0.005$. No other conversions are needed, because the readings and the resolutions are in volts.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\Delta U_{20} \\
&= 0.005 \cdot 1.50\,\text{V} + 2 \cdot 0.01\,\text{V} \\
&= 0.0275\,\text{V} \\[6pt]
&\Delta U_2 \\
&= 0.005 \cdot 1.500\,\text{V} + 2 \cdot 0.001\,\text{V} \\
&= 0.0095\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Result.** On the range $20\,\text{V}$ the voltage is $1.50\,\text{V} \pm 0.03\,\text{V}$ and on the range $2\,\text{V}$ $1.500\,\text{V} \pm 0.010\,\text{V}$. The relative error limits are $2\,\%$ and $0.67\,\%$. Like an error estimate, an error limit is rounded to one significant figure, or to two if the first figure is 1. The range $2\,\text{V}$ should be chosen: its error limit is about a third.

<!-- vaihe -->

**Reasonableness.** The percentage part is the same on both ranges, $0.0075\,\text{V}$. The difference comes entirely from the share of the digits, which on the range $20\,\text{V}$ is ten times larger, $0.02\,\text{V}$ instead of $0.002\,\text{V}$. A smaller range cannot be less accurate when the reading fits on it and the percentage part of the ranges is the same.

## Common misconception
Many people think that the largest measuring range is always the best, because on it the meter does not go over the range and the fuse does not blow. It is right to start from the largest range when the order of magnitude is not known, but the final reading is taken from the smallest range on which the value fits. On a large range the last digit is coarse, and the error limit of a small value can be as large as the reading itself. Another common mistake is to connect an ammeter in parallel with a component in the same way as a voltmeter. An ammeter is always connected in series.

## Summary
- An ammeter is connected in series: the circuit is opened and the meter is placed in the gap. In a circuit without branches the current is the same at every point.
- A voltmeter is connected in parallel, that is between the two points whose voltage is measured.
- The selector of a multimeter chooses the quantity and the measuring range; OL means that the value is over the range. The black lead belongs in the jack COM.
- We measure on the smallest range on which the reading fits; the measurement of an unknown value is started from the largest range.
- The resistance of an ammeter is very small and that of a voltmeter very large. Wrongly connected, an ammeter makes a short circuit and a voltmeter stops the current.
- The error limit is $\Delta x = p \cdot x + n \cdot r$ and the relative error limit is $\tfrac{\Delta x}{x}$.
