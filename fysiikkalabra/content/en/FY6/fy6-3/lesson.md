# Resistance and Ohm's law

> **Why** is the heating wire of a toaster made of thin special metal, while the conductors of an extension cord are thick copper?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a kitchen counter. A toaster is on, and an orange glow shines from its bread slots as the thin heating wires glow. The toaster&#x27;s cord is plugged into a thick extension cord that runs to a wall socket. The extension cord does not glow." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy63h-top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy63h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078"/><stop offset="0.55" stop-color="#e8590c" stop-opacity="0.8"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient><linearGradient id="fy63h-steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="400" fill="#ffffff"/>
  <line x1="0" y1="0" x2="0" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="80" y1="0" x2="80" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="0" x2="160" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="0" x2="240" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320" y1="0" x2="320" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="0" x2="400" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="480" y1="0" x2="480" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="560" y1="0" x2="560" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="640" y1="0" x2="640" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="720" y1="0" x2="720" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="0" x2="800" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="880" y1="0" x2="880" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="0" x2="960" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1040" y1="0" x2="1040" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1120" y1="0" x2="1120" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1200" y1="0" x2="1200" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="0" x2="1200" y2="0" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="80" x2="1200" y2="80" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="160" x2="1200" y2="160" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="240" x2="1200" y2="240" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="320" x2="1200" y2="320" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="400" x2="1200" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="96" y="196" width="104" height="104" rx="14" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="148" cy="248" r="32" fill="#e3dccb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="136" cy="248" r="5" fill="#1f2933"/>
  <circle cx="160" cy="248" r="5" fill="#1f2933"/>
  <rect x="0" y="400" width="1200" height="34" fill="url(#fy63h-top)" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="434" width="1200" height="166" fill="#e9c98a"/>
  <rect x="20" y="452" width="360" height="160" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <rect x="180" y="476" width="40" height="10" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="420" y="452" width="360" height="160" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <rect x="580" y="476" width="40" height="10" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="820" y="452" width="360" height="160" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <rect x="980" y="476" width="40" height="10" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <path d="M148,282 C150,340 170,392 230,404 C300,418 330,392 372,396" fill="none" stroke="#1f2933" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M148,282 C150,340 170,392 230,404 C300,418 330,392 372,396" fill="none" stroke="#6b7480" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="360" y="366" width="120" height="38" rx="8" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="392" cy="385" r="9" fill="#e3dccb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="448" cy="385" r="9" fill="#e3dccb" stroke="#1f2933" stroke-width="2"/>
  <path d="M448,385 C470,372 500,380 520,392" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="700" cy="196" rx="190" ry="96" fill="url(#fy63h-glow)" fill-opacity="0.75"/>
  <path d="M604,218 V150 Q604,126 626,124 Q646,112 666,124 Q688,126 688,150 V218 Z" fill="#f1dfb5" stroke="#d9b26a" stroke-width="4" stroke-linejoin="round"/>
  <path d="M712,218 V150 Q712,126 734,124 Q754,112 774,124 Q796,126 796,150 V218 Z" fill="#f1dfb5" stroke="#d9b26a" stroke-width="4" stroke-linejoin="round"/>
  <rect x="520" y="210" width="360" height="190" rx="34" fill="url(#fy63h-steel)" stroke="#1f2933" stroke-width="3"/>
  <rect x="590" y="206" width="112" height="18" rx="6" fill="#1f2933"/>
  <rect x="698" y="206" width="112" height="18" rx="6" fill="#1f2933"/>
  <rect x="586" y="262" width="228" height="84" rx="12" fill="#1f2933" stroke="#1f2933" stroke-width="3"/>
  <path d="M600,278 L612,284 L624,272 L636,284 L648,272 L660,284 L672,272 L684,284 L696,272 L708,284 L720,272 L732,284 L744,272 L756,284 L768,272 L780,284 L792,272 L804,284" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M600,278 L612,284 L624,272 L636,284 L648,272 L660,284 L672,272 L684,284 L696,272 L708,284 L720,272 L732,284 L744,272 L756,284 L768,272 L780,284 L792,272 L804,284" fill="none" stroke="#ffc078" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M600,296 L612,302 L624,290 L636,302 L648,290 L660,302 L672,290 L684,302 L696,290 L708,302 L720,290 L732,302 L744,290 L756,302 L768,290 L780,302 L792,290 L804,302" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M600,296 L612,302 L624,290 L636,302 L648,290 L660,302 L672,290 L684,302 L696,290 L708,302 L720,290 L732,302 L744,290 L756,302 L768,290 L780,302 L792,290 L804,302" fill="none" stroke="#ffc078" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M600,314 L612,320 L624,308 L636,320 L648,308 L660,320 L672,308 L684,320 L696,308 L708,320 L720,308 L732,320 L744,308 L756,320 L768,308 L780,320 L792,308 L804,320" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M600,314 L612,320 L624,308 L636,320 L648,308 L660,320 L672,308 L684,320 L696,308 L708,320 L720,308 L732,320 L744,308 L756,320 L768,308 L780,320 L792,308 L804,320" fill="none" stroke="#ffc078" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M600,332 L612,338 L624,326 L636,338 L648,326 L660,338 L672,326 L684,338 L696,326 L708,338 L720,326 L732,338 L744,326 L756,338 L768,326 L780,338 L792,326 L804,338" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M600,332 L612,338 L624,326 L636,338 L648,326 L660,338 L672,326 L684,338 L696,326 L708,338 L720,326 L732,338 L744,326 L756,338 L768,326 L780,338 L792,326 L804,338" fill="none" stroke="#ffc078" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="878" y="270" width="30" height="18" rx="4" fill="#1f2933"/>
  <circle cx="560" cy="372" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="546" y="398" width="30" height="10" rx="3" fill="#1f2933"/>
  <rect x="824" y="398" width="30" height="10" rx="3" fill="#1f2933"/>
  <path d="M640,104 q-10,-14 0,-28 t0,-28" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.7"/>
  <path d="M700,104 q-10,-14 0,-28 t0,-28" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.7"/>
  <path d="M760,104 q-10,-14 0,-28 t0,-28" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.7"/>
</svg>

## Key idea

### Resistance tells how strongly a component opposes current
When a voltage is connected across the terminals of a component, an electric current flows through it. The same voltage produces a different current in different components: in a short thick copper wire the current is large, in a long thin heating wire it is small. The **resistance** $R$ of a component tells how strongly it opposes electric current. It is defined as the ratio of voltage to current, $R = U : I$. The greater the resistance, the smaller the current a given voltage produces. The unit of resistance is the ohm, $1\,\Omega = 1\,\text{V/A}$: a component has a resistance of one ohm when a voltage of one volt makes a current of one ampere flow through it.

A component made to have a certain resistance is called a **resistor**. Its circuit symbol is a rectangle. Resistance is determined by measuring the voltage across the component and the current through it at the same time. The ammeter is connected in series with the component so that the same current flows through both, and the voltmeter in parallel with the component, across its terminals. When the measurement is repeated at several voltages, we can see whether the ratio $U : I$ stays the same.

<svg data-fig="measure-circuit" viewBox="0 0 600 350" role="img" aria-label="Circuit diagram for measuring resistance, schematic figure. A battery, an ammeter and a resistor R are in the same circuit one after another, that is, in series, so the same current I flows through the ammeter as through the resistor. The voltmeter is connected across the terminals of the resistor, that is, in parallel with the resistor, and it measures the voltage U across the resistor. Purple arrows show the direction of the current from the positive terminal of the battery through the circuit to the negative terminal." style="max-width:100%;font-size:24px">
  <path d="M90,162 L90,90 L223,90" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="245" cy="90" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="230" y="75.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <path d="M267,90 L400,90 L400,135" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="387" y="135" width="26" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M400,205 L400,250 L90,250 L90,178" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="68" y="158" width="44" height="4" fill="#1f2933"/>
  <rect x="79" y="172" width="22" height="6" fill="#1f2933"/>
  <foreignObject x="36" y="137.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="36" y="173.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <circle cx="400" cy="115" r="5" fill="#1f2933"/>
  <circle cx="400" cy="225" r="5" fill="#1f2933"/>
  <path d="M400,115 L500,115 L500,148" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M400,225 L500,225 L500,192" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="500" cy="170" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="485" y="155.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="348" y="155.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="532" y="155.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <path d="M159,90 L141,98 L141,82 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M349,90 L331,98 L331,82 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M236,250 L254,242 L254,258 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="138" y="49.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="233" y="261.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="197.5" y="35.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ammeter}$</div></foreignObject>
  <foreignObject x="440" y="247.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{voltmeter}$</div></foreignObject>
  <line x1="12" y1="296" x2="588" y2="296" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="90" y="309.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I = \text{current},\ U = \text{voltage},\ R = \text{resistance}$</div></foreignObject>
</svg>

### Where resistance comes from
In a metal, the positive ions form a regular lattice, and the free electrons move among them. When there is a voltage between the ends of a conductor, the electrons drift along the conductor, but they keep colliding with the vibrating ions. The collisions slow the electrons down: this is the cause of resistance. In the collisions electrical energy is changed into internal energy of the conductor, so the conductor warms up. In a long conductor an electron collides more often on its way, so the resistance is greater. In a thick conductor more electrons travel side by side, so the resistance is smaller. When a metal gets hot, the ions vibrate more strongly and there are more collisions. This is why the resistance of a metal conductor increases as the temperature rises.

<svg data-fig="micro" viewBox="0 0 600 330" role="img" aria-label="Schematic figure of the inside of a metal wire, not to scale. The positive metal ions are in a regular lattice, and the free electrons move among them to the left, when the agreed direction of the current is to the right. In the left panel the wire is at room temperature: the ions vibrate a little, and an electron rarely collides. In the right panel the wire is hot: the ions vibrate strongly, which the wider rings show, and the path of the electron is interrupted more often by collisions. The resistance of the hot wire is greater." style="max-width:100%;font-size:24px">
  <line x1="300" y1="14" x2="300" y2="316" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="52.5" y="11.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{room temperature}$</div></foreignObject>
  <rect x="22" y="52" width="256" height="178" rx="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="54" cy="86" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="54" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="49" y1="86" x2="59" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="54" y1="81" x2="54" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="54" cy="141" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="54" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="49" y1="141" x2="59" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="54" y1="136" x2="54" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="54" cy="196" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="54" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="49" y1="196" x2="59" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="54" y1="191" x2="54" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="102" cy="86" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="102" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="97" y1="86" x2="107" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="102" y1="81" x2="102" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="102" cy="141" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="102" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="97" y1="141" x2="107" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="102" y1="136" x2="102" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="102" cy="196" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="102" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="97" y1="196" x2="107" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="102" y1="191" x2="102" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="150" cy="86" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="150" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="145" y1="86" x2="155" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="81" x2="150" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="150" cy="141" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="150" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="145" y1="141" x2="155" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="136" x2="150" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="150" cy="196" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="150" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="145" y1="196" x2="155" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="191" x2="150" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="198" cy="86" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="198" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="193" y1="86" x2="203" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="198" y1="81" x2="198" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="198" cy="141" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="198" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="193" y1="141" x2="203" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="198" y1="136" x2="198" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="198" cy="196" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="198" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="193" y1="196" x2="203" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="198" y1="191" x2="198" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="246" cy="86" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="246" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="241" y1="86" x2="251" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="246" y1="81" x2="246" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="246" cy="141" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="246" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="241" y1="141" x2="251" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="246" y1="136" x2="246" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="246" cy="196" r="15" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="246" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="241" y1="196" x2="251" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="246" y1="191" x2="246" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <path d="M266,112 L192,120 L142,106 L62,118" fill="none" stroke="#1971c2" stroke-width="2" stroke-linejoin="round" stroke-dasharray="5 4"/>
  <circle cx="192" cy="120" r="3" fill="#1971c2"/>
  <circle cx="142" cy="106" r="3" fill="#1971c2"/>
  <circle cx="62" cy="118" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="82" cy="168" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="178" cy="196" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="232" cy="160" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="130" cy="64" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="138" y1="252" x2="64" y2="252" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M52,252 L65,246 L65,258 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="146" y="237.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{electrons}$</div></foreignObject>
  <line x1="162" y1="286" x2="236" y2="286" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M248,286 L235,292 L235,280 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="130" y="271.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="402.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hot wire}$</div></foreignObject>
  <rect x="322" y="52" width="256" height="178" rx="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="354" cy="86" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="354" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="349" y1="86" x2="359" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="354" y1="81" x2="354" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="354" cy="141" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="354" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="349" y1="141" x2="359" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="354" y1="136" x2="354" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="354" cy="196" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="354" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="349" y1="196" x2="359" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="354" y1="191" x2="354" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="402" cy="86" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="402" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="397" y1="86" x2="407" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="402" y1="81" x2="402" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="402" cy="141" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="402" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="397" y1="141" x2="407" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="402" y1="136" x2="402" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="402" cy="196" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="402" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="397" y1="196" x2="407" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="402" y1="191" x2="402" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="450" cy="86" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="450" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="445" y1="86" x2="455" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="450" y1="81" x2="450" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="450" cy="141" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="450" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="445" y1="141" x2="455" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="450" y1="136" x2="450" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="450" cy="196" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="450" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="445" y1="196" x2="455" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="450" y1="191" x2="450" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="498" cy="86" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="498" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="493" y1="86" x2="503" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="498" y1="81" x2="498" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="498" cy="141" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="498" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="493" y1="141" x2="503" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="498" y1="136" x2="498" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="498" cy="196" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="498" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="493" y1="196" x2="503" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="498" y1="191" x2="498" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="546" cy="86" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="546" cy="86" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="541" y1="86" x2="551" y2="86" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="81" x2="546" y2="91" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="546" cy="141" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="546" cy="141" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="541" y1="141" x2="551" y2="141" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="136" x2="546" y2="146" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="546" cy="196" r="21" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="546" cy="196" r="11" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="541" y1="196" x2="551" y2="196" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="191" x2="546" y2="201" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,112 L536,128 L508,104 L474,126 L442,102 L410,128 L380,106 L352,120" fill="none" stroke="#1971c2" stroke-width="2" stroke-linejoin="round" stroke-dasharray="5 4"/>
  <circle cx="536" cy="128" r="3" fill="#1971c2"/>
  <circle cx="508" cy="104" r="3" fill="#1971c2"/>
  <circle cx="474" cy="126" r="3" fill="#1971c2"/>
  <circle cx="442" cy="102" r="3" fill="#1971c2"/>
  <circle cx="410" cy="128" r="3" fill="#1971c2"/>
  <circle cx="380" cy="106" r="3" fill="#1971c2"/>
  <circle cx="352" cy="120" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="382" cy="168" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="478" cy="196" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="532" cy="160" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="430" cy="64" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="438" y1="252" x2="364" y2="252" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M352,252 L365,246 L365,258 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="446" y="237.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{electrons}$</div></foreignObject>
  <line x1="462" y1="286" x2="536" y2="286" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M548,286 L535,292 L535,280 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="430" y="271.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

## Formula: Ohm's law and resistivity
The resistance is the ratio of the voltage across a component to the current through it:
```latex
R = \frac{U}{I}
```
where $R$ is the resistance ($\Omega$), $U$ the voltage across the component ($\text{V}$) and $I$ the current through it ($\text{A}$).

**Ohm's law:** the current through a metal conductor is directly proportional to its voltage when the temperature of the conductor stays the same. Then the resistance is constant, and
```latex
U = R I
```
When the voltage doubles, the current doubles too. Ohm's law is not a general law of nature but a property of many conducting materials: it holds for metals and resistors at a constant temperature, but not, for example, for a filament lamp, whose wire heats up, nor for a diode.

### Characteristic curve
The **characteristic curve** of a component is a graph that shows how the voltage across the component and the current through it depend on each other. When the current $I$ is on the horizontal axis and the voltage $U$ on the vertical axis, the characteristic curve of a resistor that obeys Ohm's law is a straight line through the origin, and the slope of the line is the resistance $R$. The characteristic curve of a filament lamp is curved. The tungsten wire of the lamp gets hotter the greater the current through it, and the resistance of a hot wire is greater. At every point of the curve, however, the resistance is the ratio $U : I$, that is, the slope of the straight line drawn from the origin to the point, not the steepness of the curve at that point.

<svg data-fig="curves" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: voltage U in volts as a function of current I in amperes. The characteristic curve of the resistor is a straight line through the origin and through the point (0.30 A; 3.0 V), so its resistance is 10 ohms everywhere. The characteristic curve of the filament lamp is curved: at small voltages it rises gently and at large voltages steeply, and at a voltage of 3.0 V the current of the lamp is 0.25 A. The dashed line from the origin to the point of the lamp shows the resistance of the lamp U : I = 12 ohms at this voltage. The grid spacing is 0.05 A and 0.5 V." style="max-width:100%;font-size:24px">
  <line x1="148.5" y1="306" x2="148.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="201" y1="306" x2="201" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253.5" y1="306" x2="253.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="306.5" y1="306" x2="306.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="306" x2="359" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="411.5" y1="306" x2="411.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="464" y1="306" x2="464" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="270.5" x2="464" y2="270.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="234.5" x2="464" y2="234.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="199" x2="464" y2="199" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="163" x2="464" y2="163" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="127.5" x2="464" y2="127.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="91.5" x2="464" y2="91.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="56" x2="464" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="306" x2="478" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M490,306 L477,312 L477,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="307" x2="96" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,30 L102,43 L90,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="148.5" y1="306" x2="148.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201" y1="306" x2="201" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="178.5" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.1$</div></foreignObject>
  <line x1="253.5" y1="306" x2="253.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="306.5" y1="306" x2="306.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="284" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.2$</div></foreignObject>
  <line x1="359" y1="306" x2="359" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="411.5" y1="306" x2="411.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="389" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.3$</div></foreignObject>
  <line x1="464" y1="306" x2="464" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="270.5" x2="96" y2="270.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="234.5" x2="96" y2="234.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="220" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="199" x2="96" y2="199" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="163" x2="96" y2="163" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="148.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="127.5" x2="96" y2="127.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="91.5" x2="96" y2="91.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="77" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="56" x2="96" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="496" y="291.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="86" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <polyline points="96,306 437.5,74" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,306 112,304 123,302.5 132,300.5 139.5,299 146,297 152,295.5 157.5,293.5 162.5,291.5 167,290 171.5,288 176,286.5 180,284.5 183.5,283 187.5,281 191,279 194,277.5 197.5,275.5 200.5,274 203.5,272 206.5,270.5 209.5,268.5 212,266.5 215,265 217.5,263 220,261.5 222.5,259.5 225,258 227.5,256 230,254 232,252.5 234.5,250.5 236.5,249 239,247 241,245.5 243,243.5 245,241.5 247.5,240 249.5,238 251,236.5 253,234.5 255,233 257,231 259,229 260.5,227.5 262.5,225.5 264,224 266,222 267.5,220.5 269.5,218.5 271,216.5 273,215 274.5,213 276,211.5 277.5,209.5 279.5,208 281,206 282.5,204 284,202.5 285.5,200.5 287,199 288.5,197 290,195.5 291.5,193.5 293,191.5 294.5,190 296,188 297,186.5 298.5,184.5 300,183 301.5,181 302.5,179 304,177.5 305.5,175.5 306.5,174 308,172 309.5,170.5 310.5,168.5 312,166.5 313,165 314.5,163 315.5,161.5 317,159.5 318,158 319.5,156 320.5,154 322,152.5 323,150.5 324.5,149 325.5,147 326.5,145.5 328,143.5 329,141.5 330,140 331.5,138 332.5,136.5 333.5,134.5 334.5,133 336,131 337,129 338,127.5 339,125.5 340,124 341.5,122 342.5,120.5 343.5,118.5 344.5,116.5 345.5,115 346.5,113 347.5,111.5 348.5,109.5 350,108 351,106 352,104 353,102.5 354,100.5 355,99 356,97 357,95.5 358,93.5 359,91.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,306 359,91.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="359" cy="91.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="411.5" cy="91.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="445.5" y="59.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{resistor}$</div></foreignObject>
  <foreignObject x="187" y="67" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$\text{filament lamp}$</div></foreignObject>
</svg>

### Resistivity
The resistance of a uniform conductor of one material is directly proportional to the length $l$ of the conductor and inversely proportional to its cross-sectional area $A$:
```latex
R = \rho \frac{l}{A}
```
where $R$ is the resistance of the conductor ($\Omega$), $l$ its length ($\text{m}$), $A$ its cross-sectional area ($\text{m}^2$) and $\rho$ the **resistivity** of the material ($\Omega\cdot\text{m}$). A wire twice as long is like two wires one after the other, so the resistance doubles. A wire with twice the cross-sectional area is like two wires side by side, so the current can take two routes and the resistance is halved. The cross-sectional area is often given in square millimetres, and $1\,\text{mm}^2 = (10^{-3}\,\text{m})^2 = 10^{-6}\,\text{m}^2$.

<svg data-fig="wire" viewBox="0 0 600 340" role="img" aria-label="Schematic figure of three wires of the same material, lengths to scale. At the top a wire of length l and cross-sectional area A, and its resistance is R. In the middle a wire twice as long with the same cross-sectional area: the resistance is 2R. At the bottom a wire of the same length with twice the cross-sectional area: the resistance is half, that is, R divided by two. The cross-section is highlighted in orange at the left end of the wire." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy63-cu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="0.4" stop-color="#b8622d"/><stop offset="1" stop-color="#b8622d"/></linearGradient></defs>
  <rect x="96" y="50" width="190" height="24" fill="url(#fy63-cu)"/>
  <line x1="96" y1="50" x2="286" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="96" y1="74" x2="286" y2="74" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="286" cy="62" rx="5" ry="12" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="96" cy="62" rx="5" ry="12" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="38" y="47.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="96" y1="85" x2="96" y2="99" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="286" y1="85" x2="286" y2="99" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="171" y1="92" x2="107" y2="92" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M98,92 L108,87.5 L108,96.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="211" y1="92" x2="275" y2="92" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M284,92 L274,96.5 L274,87.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="173" y="77.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$l$</span></div></foreignObject>
  <foreignObject x="308" y="47.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <rect x="96" y="154" width="380" height="24" fill="url(#fy63-cu)"/>
  <line x1="96" y1="154" x2="476" y2="154" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="96" y1="178" x2="476" y2="178" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="476" cy="166" rx="5" ry="12" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="96" cy="166" rx="5" ry="12" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="38" y="151.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="96" y1="189" x2="96" y2="203" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="189" x2="476" y2="203" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266" y1="196" x2="107" y2="196" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M98,196 L108,191.5 L108,200.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="306" y1="196" x2="465" y2="196" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M474,196 L464,200.5 L464,191.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="268" y="181.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$2l$</span></div></foreignObject>
  <foreignObject x="498" y="151.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2R$</div></foreignObject>
  <rect x="96" y="255" width="190" height="34" fill="url(#fy63-cu)"/>
  <line x1="96" y1="255" x2="286" y2="255" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="96" y1="289" x2="286" y2="289" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="286" cy="272" rx="7" ry="17" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="96" cy="272" rx="7" ry="17" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="38" y="257.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2A$</div></foreignObject>
  <line x1="96" y1="300" x2="96" y2="314" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="286" y1="300" x2="286" y2="314" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="171" y1="307" x2="107" y2="307" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M98,307 L108,302.5 L108,311.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="211" y1="307" x2="275" y2="307" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M284,307 L274,311.5 L274,302.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="173" y="292.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$l$</span></div></foreignObject>
  <foreignObject x="308" y="243" width="60" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dfrac{R}{2}$</div></foreignObject>
</svg>

Resistivity is a property of a material: it tells how poorly the material conducts electricity. The resistivity of metals increases as the temperature rises. The resistivity of constantan changes very little with temperature, which is why it is used to make precise resistors. Heating wires are made of nichrome because of its high resistivity. The values in the table are in $\Omega\cdot\text{m}$ at room temperature ($20\,{}^\circ\text{C}$).

| material | resistivity $\rho$ |
|---|---|
| silver | $1.6 \cdot 10^{-8}$ |
| copper | $1.7 \cdot 10^{-8}$ |
| aluminium | $2.7 \cdot 10^{-8}$ |
| iron | $1.0 \cdot 10^{-7}$ |
| constantan | $5.0 \cdot 10^{-7}$ |
| nichrome | $1.1 \cdot 10^{-6}$ |

The resistivity of copper is small, so thick copper conductors let current flow with almost no voltage drop. The wire of a toaster is nichrome, whose resistivity is more than 60 times that of copper, and the wire is also thin. So its resistance is large, and it is the wire that gets hot.

## Worked example
A resistor with a resistance of $12\,\Omega$ is to be made from constantan wire with a cross-sectional area of $0.20\,\text{mm}^2$. How long a wire is needed? The resistivity of constantan is $5.0 \cdot 10^{-7}\,\Omega\cdot\text{m}$.

<!-- vaihe -->

**Given and find.** $R = 12\,\Omega$, $A = 0.20\,\text{mm}^2$ and $\rho = 5.0 \cdot 10^{-7}\,\Omega\cdot\text{m}$. We want the length $l$ of the wire.

<!-- vaihe -->

**Principle.** The wire is uniform and of one material, so its resistance is proportional to its length and inversely proportional to its cross-sectional area. The resistivity of constantan stays almost the same even if the wire warms up in use, so the table value will do.

<!-- vaihe -->

**Rearranged formula.** We solve for the length by multiplying the equation on both sides by $A$ and dividing by $\rho$:
```latex
\begin{aligned}
R &= \rho \frac{l}{A} \\
l &= \frac{R A}{\rho}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The cross-sectional area in square metres: $0.20\,\text{mm}^2 = 0.20 \cdot (10^{-3}\,\text{m})^2 = 0.20 \cdot 10^{-6}\,\text{m}^2$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
l &= \frac{R A}{\rho} \\
&= \frac{12\,\Omega \cdot 0.20 \cdot 10^{-6}\,\text{m}^2}{5.0 \cdot 10^{-7}\,\Omega\cdot\text{m}} \\
&= 4.8\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Result.** The wire needed is $4.8\,\text{m}$ long. The result is given to two significant figures, because the resistance, the cross-sectional area and the resistivity are given to two figures.

<!-- vaihe -->

**Reasonableness.** One metre of this wire has a resistance of $5.0 \cdot 10^{-7}\,\Omega\cdot\text{m} \cdot 1.0\,\text{m} : (0.20 \cdot 10^{-6}\,\text{m}^2) = 2.5\,\Omega$, so $12\,\Omega$ needs just under five metres: $12\,\Omega : 2.5\,\Omega = 4.8$. The units work out: $\Omega \cdot \text{m}^2 : (\Omega\cdot\text{m}) = \text{m}$. At a voltage of $6.0\,\text{V}$ the finished resistor would pass a current of $6.0\,\text{V} : 12\,\Omega = 0.50\,\text{A}$.

## Common misconception
Many conclude from the formula $R = U : I$ that the resistance increases when the voltage increases. The resistance of a resistor, however, does not depend on the voltage: when the voltage doubles, the current doubles too, and the ratio stays the same. Resistance depends on the material, length, thickness and temperature of the conductor. The resistance of a filament lamp increases with the voltage only because a larger current heats the wire.

Another misconception is that current is used up in a resistor. After the resistor the current is as large as before it, because charge does not disappear on the way. In a resistor electrical energy is changed into internal energy, not current.

## Summary
- Resistance $R = U : I$ tells how strongly a component opposes electric current. The unit is the ohm, $1\,\Omega = 1\,\text{V/A}$.
- Resistance is measured with an ammeter in series with the component and a voltmeter in parallel with it.
- Ohm's law: the current through a metal conductor is directly proportional to the voltage when the temperature stays the same, $U = RI$.
- The characteristic curve shows how the voltage across a component and the current through it depend on each other. The curve of a resistor is a straight line through the origin, that of a filament lamp is curved, because the resistance of a hot wire is greater.
- The resistance of a conductor is $R = \rho l : A$: it grows with length, falls with thickness and depends on the resistivity $\rho$ of the material.
