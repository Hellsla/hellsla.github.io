# Changes of state of a gas and Boyle's law

> **Why** does a sealed bag of crisps swell up tight on an aeroplane, even though nothing has been added to it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on the tray table of an aeroplane seat there is a swollen, tight bag of crisps and a mug of water. Through the window clouds can be seen far below." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy39h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1971c2"/><stop offset="1" stop-color="#a5d8ff"/></linearGradient><linearGradient id="fy39h-seat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#e3dccb"/>
  <path d="M0,0 H1200 V60 Q600,20 0,60 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="780" y="70" width="230" height="300" rx="100" fill="#ffffff" stroke="#c9c2b2" stroke-width="6"/>
  <clipPath id="fy39h-win"><rect x="800" y="90" width="190" height="260" rx="90"/></clipPath>
  <g clip-path="url(#fy39h-win)">
  <rect x="800" y="90" width="190" height="260" fill="url(#fy39h-sky)"/>
  <path d="M758,316 Q756.5,289 788.5,292 Q801,263 833,273 Q862,257 878,287 Q907,290.5 903.5,316 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M869,338 Q867,307.5 903,311 Q917.5,278.5 953.5,289.5 Q986,271.5 1004,305.5 Q1036.5,309 1033,338 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M790,360 Q788,326 828,330 Q844,294 884,306 Q920,286 940,324 Q976,328 972,360 Z" fill="#ffffff" stroke-linejoin="round"/>
  </g>
  <rect x="800" y="90" width="190" height="260" fill="none" rx="90" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="120" y="40" width="520" height="560" rx="40" fill="url(#fy39h-seat)" stroke="#1f2933" stroke-width="3"/>
  <rect x="170" y="80" width="420" height="60" rx="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M60,430 H760 L720,480 H100 Z" fill="#c9c2b2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="100" y="480" width="620" height="16" fill="#6b7480"/>
  <path d="M260,250 Q206,335 262,420 Q380,462 500,420 Q556,335 500,250 Q380,208 260,250 Z" fill="#1971c2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M248,246 H512 L506,268 H254 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M252,412 H508 L514,434 H246 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M300,300 Q380,284 460,300" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" stroke-opacity="0.7" stroke-linecap="round"/>
  <circle cx="380" cy="352" r="44" fill="#e9c98a" stroke="#d9b26a" stroke-width="3"/>
  <path d="M560,330 L572,428 H640 L652,330 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M563,354 L572,426 H640 L649,354 Z" fill="#a9d1f0" stroke-linejoin="round"/>
  <path d="M560,330 L572,428 H640 L652,330" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
</svg>

## Key idea
The state of a fixed amount of gas is described by its pressure $p$, volume $V$ and temperature $T$. When one of them changes, at least one of the others usually changes too. This kind of change is called a change of state. It is easiest to study changes of state by keeping one of the quantities constant. In an isothermal change the temperature is constant, in an isobaric change the pressure, and in an isochoric change the volume.

According to the micro model, the pressure of a gas comes from particles colliding with the walls of the container. If the gas is compressed to half of its original volume and the temperature stays the same, the particles move as fast as before, but they hit the walls twice as often. The pressure doubles.

<svg data-fig="micro-boyle" viewBox="0 0 600 332" role="img" aria-label="Micro model of Boyle&#x27;s law, schematic picture. On the left, a cylinder contains eight gas particles in volume V at pressure p. On the right, the same eight particles have been squeezed by pressing the piston to half the volume, V/2, at the same temperature. The velocity arrows are equally long, but there are twice as many hit marks on the piston and the bottom, so the pressure is 2p. The heights of the gas spaces are in the ratio 2 : 1." style="max-width:100%;font-size:24px">
  <rect x="40" y="44" width="160" height="220" fill="#eef5f9"/>
  <path d="M40,28 V264 H200 V28" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="43" y="30" width="154" height="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="120" y1="20" x2="120" y2="30" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="95" y1="20" x2="145" y2="20" stroke="#1f2933" stroke-width="5" stroke-linecap="round"/>
  <circle cx="68" cy="70" r="6.5" fill="#c92a2a"/>
  <line x1="60.5" y1="72.5" x2="50" y2="76.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M41.5,79 L49.5,71.5 L52.5,80 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="115" cy="58" r="6.5" fill="#c92a2a"/>
  <line x1="122.5" y1="55.5" x2="133" y2="51.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M141.5,49 L133.5,56.5 L130.5,48 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="165" cy="74" r="6.5" fill="#c92a2a"/>
  <line x1="172" y1="78" x2="181.5" y2="83" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M189.5,87.5 L178.5,86.5 L183,79 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="92" cy="134" r="6.5" fill="#c92a2a"/>
  <line x1="90" y1="126" x2="87.5" y2="115.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M85,107 L92,115.5 L83.5,117.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="140" cy="124" r="6.5" fill="#c92a2a"/>
  <line x1="134.5" y1="130" x2="127.5" y2="138" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M121.5,145 L124.5,134.5 L131.5,140.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="185" cy="158" r="6.5" fill="#c92a2a"/>
  <line x1="188" y1="150.5" x2="192.5" y2="140.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M196,132 L196,143 L188,139.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="70" cy="190" r="6.5" fill="#c92a2a"/>
  <line x1="77.5" y1="193" x2="87.5" y2="197" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,200.5 L85,201 L88.5,192.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="158" cy="194" r="6.5" fill="#c92a2a"/>
  <line x1="166" y1="192.5" x2="176.5" y2="190.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M185.5,188.5 L176.5,195 L175,186 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M78,43 L80.4,48.6 L86,51 L80.4,53.4 L78,59 L75.6,53.4 L70,51 L75.6,48.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M178,43 L180.4,48.6 L186,51 L180.4,53.4 L178,59 L175.6,53.4 L170,51 L175.6,48.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M100,249 L102.4,254.6 L108,257 L102.4,259.4 L100,265 L97.6,259.4 L92,257 L97.6,254.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M180,249 L182.4,254.6 L188,257 L182.4,259.4 L180,265 L177.6,259.4 L172,257 L177.6,254.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="330" y="154" width="160" height="110" fill="#eef5f9"/>
  <path d="M330,28 V264 H490 V28" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="333" y="140" width="154" height="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="410" y1="20" x2="410" y2="140" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="385" y1="20" x2="435" y2="20" stroke="#1f2933" stroke-width="5" stroke-linecap="round"/>
  <circle cx="358" cy="179" r="6.5" fill="#c92a2a"/>
  <line x1="350.5" y1="181.5" x2="340" y2="185.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M331.5,188 L339.5,180.5 L342.5,189 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="405" cy="173" r="6.5" fill="#c92a2a"/>
  <line x1="412.5" y1="170.5" x2="423" y2="166.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M431.5,164 L423.5,171.5 L420.5,163 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="455" cy="181" r="6.5" fill="#c92a2a"/>
  <line x1="462" y1="185" x2="471.5" y2="190" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M479.5,194.5 L468.5,193.5 L473,186 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="382" cy="211" r="6.5" fill="#c92a2a"/>
  <line x1="380" y1="203" x2="377.5" y2="192.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M375,184 L382,192.5 L373.5,194.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="430" cy="206" r="6.5" fill="#c92a2a"/>
  <line x1="424.5" y1="212" x2="417.5" y2="220" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M411.5,227 L414.5,216.5 L421.5,222.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="475" cy="223" r="6.5" fill="#c92a2a"/>
  <line x1="478" y1="215.5" x2="482.5" y2="205.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M486,197 L486,208 L478,204.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="360" cy="239" r="6.5" fill="#c92a2a"/>
  <line x1="367.5" y1="242" x2="377.5" y2="246" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M386,249.5 L375,250 L378.5,241.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="448" cy="241" r="6.5" fill="#c92a2a"/>
  <line x1="456" y1="239.5" x2="466.5" y2="237.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M475.5,235.5 L466.5,242 L465,233 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M353,153 L355.4,158.6 L361,161 L355.4,163.4 L353,169 L350.6,163.4 L345,161 L350.6,158.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M396,153 L398.4,158.6 L404,161 L398.4,163.4 L396,169 L393.6,163.4 L388,161 L393.6,158.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M440,153 L442.4,158.6 L448,161 L442.4,163.4 L440,169 L437.6,163.4 L432,161 L437.6,158.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M476,153 L478.4,158.6 L484,161 L478.4,163.4 L476,169 L473.6,163.4 L468,161 L473.6,158.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M353,249 L355.4,254.6 L361,257 L355.4,259.4 L353,265 L350.6,259.4 L345,257 L350.6,254.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M413,249 L415.4,254.6 L421,257 L415.4,259.4 L413,265 L410.6,259.4 L405,257 L410.6,254.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M438,249 L440.4,254.6 L446,257 L440.4,259.4 L438,265 L435.6,259.4 L430,257 L435.6,254.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M476,249 L478.4,254.6 L484,257 L478.4,259.4 L476,265 L473.6,259.4 L468,257 L473.6,254.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M222,58 L224.4,63.6 L230,66 L224.4,68.4 L222,74 L219.6,68.4 L214,66 L219.6,63.6 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="238" y="51.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hit}$</div></foreignObject>
  <line x1="218" y1="214" x2="296" y2="214" stroke="#6b7480" stroke-width="4" stroke-linecap="butt"/>
  <line x1="218" y1="214" x2="299" y2="214" stroke="#e8590c" stroke-width="4" stroke-linecap="butt"/>
  <path d="M316,214 L298,222 L298,206 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="205" y="171.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T\ \text{constant}$</div></foreignObject>
  <foreignObject x="81" y="289.5" width="78" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V\ \text{and}\ p$</div></foreignObject>
  <foreignObject x="352.5" y="289.5" width="115" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V/2\ \text{and}\ 2p$</div></foreignObject>
</svg>

So in an isothermal change the pressure is inversely proportional to the volume, and the product of pressure and volume stays constant. This is called Boyle's law. It answers the opening question: the air pressure in the aeroplane cabin drops to about 78 kPa, so the air in the bag expands until the bag is tight. In a tight bag the pressure of the air stays slightly higher than the cabin pressure, and that is why the bag feels hard.

Boyle's law works well for air and other gases at ordinary pressures and temperatures. The amount of gas must stay the same, so no gas may leak out or come in. The pressure used is the total pressure of the gas, not the gauge pressure shown by a meter.

Boyle's law can be verified experimentally. Air is sealed in a syringe, and the syringe is connected to a pressure gauge. The plunger is pressed in steps, and the pressure is read at each volume. The measurement is done slowly so that the temperature of the air has time to return to room temperature. When the results are plotted in a $(V, p)$ coordinate system, the points lie on a falling curve, and it is hard to see from it whether the relationship is exactly inverse proportionality. So a new column $1/V$ is calculated in the table, and $p$ is plotted as a function of $1/V$. If the law holds, the points lie on a straight line through the origin, and the slope of the line is the constant $pV$. Try it in the simulation: save measurements at different volumes and choose “Plot p as a function of 1/V”.

When a gas is heated, its particles move faster. If the piston can move so that the pressure stays constant (an isobaric change), the gas expands, and its volume is directly proportional to the temperature in kelvins. If the volume is instead kept constant (an isochoric change), the pressure rises, and it is directly proportional to the temperature in kelvins. In both cases the temperature must be given in kelvins, because the proportionality starts from absolute zero.

<svg data-fig="iso-processes" viewBox="0 0 600 412" role="img" aria-label="Two changes of state, schematic picture. On the left, an isobaric change: the piston of the cylinder is loaded by an object of constant weight, so when the gas warms from temperature T₁ to temperature T₂, the piston rises and the volume increases from V₁ to V₂; the velocity arrows of the particles are longer. On the right, an isochoric change: the volume V of a rigid, closed container stays the same, and when the gas warms, the needle of the pressure gauge turns to the greater pressure p₂." style="max-width:100%;font-size:24px">
  <foreignObject x="96" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{isobaric}$</div></foreignObject>
  <foreignObject x="390" y="11.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{isochoric}$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="400" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <rect x="30" y="250" width="90" height="90" fill="#d0e6fb"/>
  <circle cx="44" cy="270" r="6.5" fill="#1971c2"/>
  <line x1="51.5" y1="273" x2="54" y2="274.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M62.5,277.5 L51.5,278 L55,269.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="103" cy="276.5" r="6.5" fill="#1971c2"/>
  <line x1="96" y1="280.5" x2="93.5" y2="282" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M86,286.5 L92,277.5 L96.5,285.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="72" cy="295" r="6.5" fill="#1971c2"/>
  <line x1="75.5" y1="288" x2="77" y2="285" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M81,277 L80.5,288 L72.5,284 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="106" cy="313.5" r="6.5" fill="#1971c2"/>
  <line x1="99" y1="310" x2="96" y2="308.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M88,304.5 L99,305 L95,313 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="47" cy="320" r="6.5" fill="#1971c2"/>
  <line x1="55" y1="317.5" x2="57.5" y2="316.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M66.5,314 L58,321 L55.5,312.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M30,110 V340 H120 V110" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="33" y="238" width="84" height="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="45" y="210" width="60" height="28" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="65" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$m$</div></foreignObject>
  <foreignObject x="40" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_1\text{, }V_1$</div></foreignObject>
  <rect x="170" y="205" width="90" height="135" fill="#f2a69c"/>
  <circle cx="184" cy="229.5" r="6.5" fill="#c92a2a"/>
  <line x1="191.5" y1="232.5" x2="203.5" y2="237.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M212,241 L201,241.5 L204,233 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="243" cy="240.5" r="6.5" fill="#c92a2a"/>
  <line x1="236" y1="244.5" x2="225" y2="251" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M217,256 L223.5,247 L228,254.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="212" cy="272.5" r="6.5" fill="#c92a2a"/>
  <line x1="215.5" y1="265.5" x2="221.5" y2="253.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M225.5,245.5 L225,256.5 L217,252.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="246" cy="304.5" r="6.5" fill="#c92a2a"/>
  <line x1="239" y1="301" x2="227" y2="295" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M219,291 L230,291.5 L226,299.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="187" cy="315.5" r="6.5" fill="#c92a2a"/>
  <line x1="195" y1="313" x2="207" y2="309.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M216,306.5 L207.5,314 L205,305 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M170,110 V340 H260 V110" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="173" y="193" width="84" height="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="185" y="165" width="60" height="28" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="205" y="164.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$m$</div></foreignObject>
  <foreignObject x="180" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_2\text{, }V_2$</div></foreignObject>
  <line x1="33" y1="238" x2="260" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M128,297 L148,297 L148,303 L164,290 L148,277 L148,283 L128,283 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="136" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <rect x="345" y="205" width="90" height="135" fill="#d0e6fb"/>
  <circle cx="359" cy="229.5" r="6.5" fill="#1971c2"/>
  <line x1="366.5" y1="232.5" x2="369" y2="234" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M377.5,237 L366.5,237.5 L370,229 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="418" cy="240.5" r="6.5" fill="#1971c2"/>
  <line x1="411" y1="244.5" x2="408.5" y2="246" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M401,250.5 L407,241.5 L411.5,249.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="387" cy="272.5" r="6.5" fill="#1971c2"/>
  <line x1="390.5" y1="265.5" x2="392" y2="262.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M396,254.5 L395.5,265.5 L387.5,261.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="421" cy="304.5" r="6.5" fill="#1971c2"/>
  <line x1="414" y1="301" x2="411" y2="299.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M403,295.5 L414,296 L410,304 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="362" cy="315.5" r="6.5" fill="#1971c2"/>
  <line x1="370" y1="313" x2="372.5" y2="312" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M381.5,309.5 L373,316.5 L370.5,308 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M345,110 V340 H435 V110" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="342" y="193" width="96" height="12" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="390" y1="193" x2="390" y2="175" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="390" cy="143" r="32" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="366" y1="157" x2="372" y2="153.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="362.5" y1="138" x2="369.5" y2="139.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="372" y1="121.5" x2="376.5" y2="127" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="390" y1="115" x2="390" y2="122" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="408" y1="121.5" x2="403.5" y2="127" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="417.5" y1="138" x2="410.5" y2="139.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414" y1="157" x2="408" y2="153.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="390" y1="143" x2="381.5" y2="130.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M376,123.5 L385.5,129 L378.5,134 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="390" cy="143" r="3.5" fill="#1f2933"/>
  <foreignObject x="355" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_1\text{, }p_1$</div></foreignObject>
  <rect x="465" y="205" width="90" height="135" fill="#f2a69c"/>
  <circle cx="479" cy="229.5" r="6.5" fill="#c92a2a"/>
  <line x1="486.5" y1="232.5" x2="498.5" y2="237.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M507,241 L496,241.5 L499,233 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="538" cy="240.5" r="6.5" fill="#c92a2a"/>
  <line x1="531" y1="244.5" x2="520" y2="251" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M512,256 L518.5,247 L523,254.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="507" cy="272.5" r="6.5" fill="#c92a2a"/>
  <line x1="510.5" y1="265.5" x2="516.5" y2="253.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M520.5,245.5 L520,256.5 L512,252.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="541" cy="304.5" r="6.5" fill="#c92a2a"/>
  <line x1="534" y1="301" x2="522" y2="295" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,291 L525,291.5 L521,299.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="482" cy="315.5" r="6.5" fill="#c92a2a"/>
  <line x1="490" y1="313" x2="502" y2="309.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M511,306.5 L502.5,314 L500,305 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M465,110 V340 H555 V110" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="462" y="193" width="96" height="12" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="510" y1="193" x2="510" y2="175" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="510" cy="143" r="32" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="486" y1="157" x2="492" y2="153.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="482.5" y1="138" x2="489.5" y2="139.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="492" y1="121.5" x2="496.5" y2="127" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="510" y1="115" x2="510" y2="122" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="528" y1="121.5" x2="523.5" y2="127" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="537.5" y1="138" x2="530.5" y2="139.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="534" y1="157" x2="528" y2="153.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="510" y1="143" x2="516.5" y2="129.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M520,121 L520,132 L512,128.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="510" cy="143" r="3.5" fill="#1f2933"/>
  <foreignObject x="475" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_2\text{, }p_2$</div></foreignObject>
  <path d="M438,297 L448,297 L448,303 L462,290 L448,277 L448,283 L438,283 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="440" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
</svg>

## Formula: Boyle's law and changes of state of a gas
In an isothermal change, that is, according to Boyle's law,
```latex
p_1 V_1 = p_2 V_2
```
where $p_1$ and $V_1$ are the pressure (Pa) and volume (m³) of the gas in the initial state and $p_2$ and $V_2$ in the final state. The equation is the same as $pV = \text{constant}$. Dividing it by $V$ gives
```latex
p = \text{constant} \cdot \frac{1}{V}
```
So the pressure is inversely proportional to the volume. If we write $x = 1/V$ and $y = p$, the equation has the form $y = kx$, like the equation of a straight line in FY1. So the $(1/V, p)$ graph is a straight line through the origin, and its slope is $k = pV$.

The unit of the product $pV$ is $\text{Pa} \cdot \text{m}^3 = \text{N/m}^2 \cdot \text{m}^3 = \text{N} \cdot \text{m} = \text{J}$, and $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$. Because both sides of the equation $p_1 V_1 = p_2 V_2$ have the same units, pressure and volume can also be given in, for example, kilopascals and litres, as long as they are the same on both sides.

<svg data-fig="boyle-graphs" viewBox="0 0 600 580" role="img" aria-label="Two graphs of the same measurements, to scale, when pV = 2000 kPa·ml. Above, pressure as a function of volume is a falling curve; the measurement points V = 10, 15, 20, 30 and 40 ml are on the curve. Below, pressure as a function of the reciprocal of the volume, 1/V, is a straight line through the origin whose slope is pV." style="max-width:100%;font-size:24px">
  <line x1="170" y1="250" x2="170" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="244.5" y1="250" x2="244.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318.5" y1="250" x2="318.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="393" y1="250" x2="393" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="215" x2="430" y2="215" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="180.5" x2="430" y2="180.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="145.5" x2="430" y2="145.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="111" x2="430" y2="111" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="250" x2="444" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,250 L443,256 L443,244 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="251" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="170" y1="250" x2="170" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153.5" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="244.5" y1="250" x2="244.5" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="228" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="318.5" y1="250" x2="318.5" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="302" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="393" y1="250" x2="393" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="376.5" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="215" x2="96" y2="215" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="200.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="180.5" x2="96" y2="180.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="166" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="145.5" x2="96" y2="145.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="131" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="111" x2="96" y2="111" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="96.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="61.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="235.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{ml})$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="155.5,76 157,81 159,85.5 160.5,90 162,94 164,98 165.5,101.5 167.5,105.5 169,108.5 171,112 172.5,115 174.5,118 176,121 177.5,123.5 179.5,126 181,128.5 183,131 184.5,133.5 186.5,135.5 188,137.5 189.5,139.5 191.5,141.5 193,143.5 195,145.5 196.5,147.5 198.5,149 200,150.5 201.5,152.5 203.5,154 205,155.5 207,157 208.5,158 210.5,159.5 212,161 213.5,162 215.5,163.5 217,164.5 219,166 220.5,167 222.5,168 224,169.5 225.5,170.5 227.5,171.5 229,172.5 231,173.5 232.5,174.5 234.5,175.5 236,176 238,177 239.5,178 241,179 243,179.5 244.5,180.5 246.5,181.5 248,182 250,183 251.5,183.5 253,184.5 255,185 256.5,185.5 258.5,186.5 260,187 262,187.5 263.5,188.5 265,189 267,189.5 268.5,190 270.5,191 272,191.5 274,192 275.5,192.5 277,193 279,193.5 280.5,194 282.5,194.5 284,195 286,195.5 287.5,196 289.5,196.5 291,197 292.5,197.5 294.5,198 296,198.5 298,199 299.5,199 301.5,199.5 303,200 304.5,200.5 306.5,201 308,201.5 310,201.5 311.5,202 313.5,202.5 315,203 316.5,203 318.5,203.5 320,204 322,204.5 323.5,204.5 325.5,205 327,205.5 328.5,205.5 330.5,206 332,206.5 334,206.5 335.5,207 337.5,207 339,207.5 340.5,208 342.5,208 344,208.5 346,208.5 347.5,209 349.5,209 351,209.5 353,210 354.5,210 356,210.5 358,210.5 359.5,211 361.5,211 363,211.5 365,211.5 366.5,212 368,212 370,212.5 371.5,212.5 373.5,212.5 375,213 377,213 378.5,213.5 380,213.5 382,214 383.5,214 385.5,214.5 387,214.5 389,214.5 390.5,215 392,215 394,215.5 395.5,215.5 397.5,215.5 399,216 401,216 402.5,216.5 404.5,216.5 406,216.5 407.5,217 409.5,217 411,217 413,217.5 414.5,217.5 416.5,217.5 418,218 419.5,218 421.5,218.5 423,218.5 425,218.5 426.5,218.5 428.5,219 430,219" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="170" cy="111" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="207.5" cy="157" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="244.5" cy="180.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="318.5" cy="203.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="393" cy="215" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="440" y="200.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{curve}$</div></foreignObject>
  <line x1="207.5" y1="520" x2="207.5" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318.5" y1="520" x2="318.5" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="520" x2="430" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="485" x2="430" y2="485" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="450.5" x2="430" y2="450.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="415.5" x2="430" y2="415.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="381" x2="430" y2="381" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="346" x2="430" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="520" x2="444" y2="520" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,520 L443,526 L443,514 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="521" x2="96" y2="332" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,320 L102,333 L90,333 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="207.5" y1="520" x2="207.5" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="178.5" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.04$</div></foreignObject>
  <line x1="318.5" y1="520" x2="318.5" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="289.5" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.08$</div></foreignObject>
  <line x1="430" y1="520" x2="430" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="401" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0.12$</div></foreignObject>
  <line x1="89" y1="485" x2="96" y2="485" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="470.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="450.5" x2="96" y2="450.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="436" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="415.5" x2="96" y2="415.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="401" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="381" x2="96" y2="381" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="366.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="346" x2="96" y2="346" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="525.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="505.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1/V\ (\text{1/ml})$</div></foreignObject>
  <foreignObject x="86" y="289.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="96,520 430,353" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="374.5" cy="381" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="281.5" cy="427" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="235" cy="450.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="189" cy="473.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="165.5" cy="485" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="440" y="360.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{line}$</div></foreignObject>
</svg>

In an isobaric and in an isochoric change
```latex
\frac{V_1}{T_1} = \frac{V_2}{T_2} \qquad \text{and} \qquad \frac{p_1}{T_1} = \frac{p_2}{T_2}
```
where $T_1$ and $T_2$ are the temperatures of the gas in kelvins (K) in the initial and final state. So the volume or the pressure is directly proportional to the temperature in kelvins, and the extension of the straight line in a $(T, V)$ or $(T, p)$ graph passes through the origin, that is, through absolute zero, 0 K.

The temperature in kelvins is obtained from the Celsius temperature $\theta$ by adding 273.15:
```latex
T = \theta + 273.15\,\text{K}
```
where $\theta$ is the temperature in degrees Celsius as a number; in calculations 273 K is enough.

<svg data-fig="absolute-zero" viewBox="0 0 600 622" role="img" aria-label="Graphs to scale when T is 0–400 K. Above, the volume of a gas at constant pressure, below, the pressure of a gas at constant volume, as a function of the temperature in kelvins. The measurement points between 253 and 373 K are on a straight line. The extension of the line, drawn dashed, passes through the origin: the volume or the pressure would be zero at absolute zero, 0 K, that is, −273 °C." style="max-width:100%;font-size:24px">
  <line x1="179.5" y1="240" x2="179.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="240" x2="263" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="240" x2="346.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="240" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="189" x2="430" y2="189" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137.5" x2="430" y2="137.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="86" x2="430" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="240" x2="444" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,240 L443,246 L443,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="241" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="240" x2="179.5" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="263" y1="240" x2="263" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="346.5" y1="240" x2="346.5" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="430" y1="240" x2="430" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="189" x2="96" y2="189" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="174" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="137.5" x2="96" y2="137.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="123" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="86" x2="96" y2="86" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="72" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="462" y="225.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (\text{K})$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\textsf{l})$</div></foreignObject>
  <foreignObject x="86" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="61" y="283.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$-273^\circ\text{C}$</div></foreignObject>
  <polyline points="96,240 307.5,145" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <polyline points="307.5,145 407.5,100" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="307.5" cy="145" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="134" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="357.5" cy="122.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="382.5" cy="111.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="407.5" cy="100" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="123.5" y="162" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{extension}$</span></div></foreignObject>
  <line x1="179.5" y1="556" x2="179.5" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="556" x2="263" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="556" x2="346.5" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="556" x2="430" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="506" x2="430" y2="506" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="456" x2="430" y2="456" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="406" x2="430" y2="406" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="556" x2="444" y2="556" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,556 L443,562 L443,550 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="557" x2="96" y2="382" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,370 L102,383 L90,383 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="556" x2="179.5" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="263" y1="556" x2="263" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="346.5" y1="556" x2="346.5" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="430" y1="556" x2="430" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="506" x2="96" y2="506" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="491.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="456" x2="96" y2="456" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="441.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="406" x2="96" y2="406" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="391.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <foreignObject x="462" y="541.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (\text{K})$</div></foreignObject>
  <foreignObject x="86" y="339.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <foreignObject x="86" y="565.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="61" y="599.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$-273^\circ\text{C}$</div></foreignObject>
  <polyline points="96,556 307.5,462.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <polyline points="307.5,462.5 407.5,418" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="307.5" cy="462.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="451.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="357.5" cy="440.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="382.5" cy="429" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="407.5" cy="418" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="123.5" y="478.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{extension}$</span></div></foreignObject>
</svg>

## Worked example
At the airport, a bag of crisps contains 0.80 l of air at a pressure of 101 kPa. During the flight the cabin pressure is 78 kPa. What is the volume of the air in the bag during the flight, if the temperature stays the same and the bag can expand freely?

<!-- vaihe -->

**Given and find.** We know $p_1 = 101\,\text{kPa}$, $V_1 = 0.80\,\textsf{l}$ and $p_2 = 78\,\text{kPa}$. The temperature is the same. We want the final volume $V_2$ in litres.

<!-- vaihe -->

**Principle.** The bag is sealed, so the amount of air does not change, and the temperature stays the same. So the change is isothermal and Boyle's law holds: the product $pV$ stays constant. The bag expands freely, so the pressure inside it is always the same as in the cabin.

<!-- vaihe -->

**Rearranged formula.** Solve $V_2$ from Boyle's law by dividing both sides by the pressure $p_2$:
```latex
\begin{aligned}
p_1 V_1 &= p_2 V_2 \\
V_2 &= \frac{p_1 V_1}{p_2}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** No units need to be converted. Both pressures are in kilopascals, so they cancel in the quotient, and the volume comes out directly in litres.

<!-- vaihe -->

**Substitution.** Substitute the values with their units:
```latex
\begin{aligned}
V_2 &= \frac{p_1 V_1}{p_2} \\
&= \frac{101\,\text{kPa} \cdot 0.80\,\textsf{l}}{78\,\text{kPa}} \\
&= 1.036\,\textsf{l}
\end{aligned}
```

<!-- vaihe -->

**Result.** The volume of the air is $V_2 \approx 1.0\,\textsf{l}$, to two significant figures like the initial data $0.80\,\textsf{l}$ and $78\,\text{kPa}$. The volume increases by about 30 %. If the bag is already almost full, it swells tight.

<!-- vaihe -->

**Reasonableness.** The pressure decreases, so the volume must increase. The factor of increase is the pressure ratio $101/78 \approx 1.3$, and $0.80\,\textsf{l} \cdot 1.3 \approx 1.0\,\textsf{l}$. At the end the product $pV$ is $78\,\text{kPa} \cdot 1.036\,\textsf{l} \approx 80.8\,\text{kPa}\cdot\textsf{l}$, the same as at the start, $101\,\text{kPa} \cdot 0.80\,\textsf{l} = 80.8\,\text{kPa}\cdot\textsf{l}$.

## Common misconception
Three mistakes are often repeated:

- **Inverse proportionality is not a falling straight line.** When the volume doubles, the pressure halves, so the $(V, p)$ graph is a curve that approaches the axes but never meets them. A straight line is obtained only when $p$ is plotted as a function of $1/V$.
- **Celsius degrees do not work in a ratio of temperatures.** When 1.00 l of air is heated at constant pressure from 10 °C to 20 °C, its volume does not double. Calculated in kelvins, $V_2 = V_1 T_2 / T_1 = 1.00\,\textsf{l} \cdot 293\,\text{K} / 283\,\text{K} \approx 1.04\,\textsf{l}$, so the volume increases by only about 3.5 %.
- **The pressure of a gas in a closed container does not come from the weight of the gas.** In a small container the weight of the gas is negligible, and the pressure comes from the collisions of the particles, so it is equal everywhere in the container.

## Summary
- In a change of state, the pressure, volume and temperature of a gas change. In an isothermal change $T$ is constant, in an isobaric change $p$, and in an isochoric change $V$.
- Boyle's law: in an isothermal change $p_1 V_1 = p_2 V_2$, so the pressure is inversely proportional to the volume.
- Inverse proportionality is verified by calculating a column $1/V$ in the table and plotting $p$ as a function of $1/V$: the points must lie on a straight line through the origin.
- At constant pressure the volume, and at constant volume the pressure, is directly proportional to the temperature in kelvins. In these calculations the temperatures are always given in kelvins.
