# Kirchhoff's laws and potential in a circuit

> **Why** can a bird sit on a bare high-voltage wire unharmed, even though a current of hundreds of amperes flows in the wire?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a high-voltage line above a field landscape on a summer day. Wires hang between two lattice pylons, and four small birds sit in a row on one wire. In the background are the edge of a forest and a rolling field." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy65h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy65h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy65h-field" gradientUnits="userSpaceOnUse" x1="0" y1="430" x2="0" y2="600"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy65h-sky)"/>
  <circle cx="1020" cy="110" r="80" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M1078,133 L1104,132.5 L1081.5,119.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1059,159 L1081.5,171.5 L1069,149 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1029.5,171.5 L1042.5,194 L1043,168 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M997,168 L997.5,194 L1010.5,171.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M971,149 L958.5,171.5 L981,159 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M958.5,119.5 L936,132.5 L962,133 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M962,87 L936,87.5 L958.5,100.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M981,61 L958.5,48.5 L971,71 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1010.5,48.5 L997.5,26 L997,52 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1043,52 L1042.5,26 L1029.5,48.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1069,71 L1081.5,48.5 L1059,61 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1081.5,100.5 L1104,87.5 L1078,87 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="1020" cy="110" r="50" fill="url(#fy65h-sun)"/>
  <path d="M210,130 Q208,96 248,100 Q264,64 304,76 Q340,56 360,94 Q396,98 392,130 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M697,84 Q695.5,60 723.5,63 Q735,38 763,46 Q788,32 802,59 Q827,61.5 824.5,84 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,400 Q100,372 200,397.5 Q300,343.5 400,403 Q500,357 600,400.5 Q700,380 800,395.5 Q900,376.5 1000,396.5 Q1100,369.5 1200,398 Q1300,337 1400,404.5 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M0,402 L15.5,352.5 L31,402 L45,357 L59.5,402 L68,378.5 L76.5,402 L85.5,379 L94,402 L108,357 L122.5,402 L131.5,377 L140.5,402 L151,372.5 L161,402 L170.5,375.5 L180,402 L193,361 L206.5,402 L218,368 L229,402 L243,359 L256.5,402 L271,356.5 L285.5,402 L299,360.5 L312.5,402 L327,355.5 L342,402 L354,366 L365.5,402 L380,356.5 L394.5,402 L405.5,370.5 L416,402 L430.5,355 L445.5,402 L459,361 L472,402 L487.5,353.5 L502.5,402 L515,363.5 L527.5,402 L542.5,355 L557.5,402 L567,374 L577,402 L587,374 L597,402 L609.5,362.5 L622.5,402 L631.5,377.5 L640.5,402 L655,354.5 L670,402 L684.5,357.5 L698.5,402 L713,356.5 L727.5,402 L737.5,372.5 L748,402 L758.5,370 L769.5,402 L782.5,362.5 L795.5,402 L808,363.5 L820.5,402 L832,367 L844,402 L853,376 L862.5,402 L873,372.5 L883,402 L898.5,353 L913.5,402 L929,352.5 L944.5,402 L954,375.5 L963.5,402 L978.5,354.5 L993.5,402 L1003.5,372 L1014,402 L1024.5,372.5 L1034.5,402 L1048.5,358.5 L1062.5,402 L1072.5,373 L1083,402 L1098.5,352.5 L1114,402 L1128,357 L1142.5,402 L1152.5,373.5 L1162,402 L1173.5,369 L1184.5,402 L1199.5,353.5 L1215,402 V432 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="430" width="1200" height="170" fill="url(#fy65h-field)"/>
  <path d="M-60,600 L240,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M90,600 L390,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M240,600 L540,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M390,600 L690,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M540,600 L840,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M690,600 L990,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M840,600 L1140,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M990,600 L1290,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M1140,600 L1440,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M107.5,470 L142.5,110 H157.5 L192.5,470" fill="none" stroke="#6c757d" stroke-width="3.75" stroke-linejoin="round"/>
  <line x1="107.5" y1="470" x2="185.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="192.5" y1="470" x2="114.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="114.5" y1="398" x2="178.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="185.5" y1="398" x2="121.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="121.5" y1="326" x2="171.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="178.5" y1="326" x2="128.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="128.5" y1="254" x2="164.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="171.5" y1="254" x2="135.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="85" y1="182" x2="215" y2="182" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="85" y1="182" x2="85" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="215" y1="182" x2="215" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="107.5" y1="110" x2="192.5" y2="110" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="107.5" y1="110" x2="107.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="110" x2="192.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M1037.5,470 L1072.5,110 H1087.5 L1122.5,470" fill="none" stroke="#6c757d" stroke-width="3.75" stroke-linejoin="round"/>
  <line x1="1037.5" y1="470" x2="1115.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1122.5" y1="470" x2="1044.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1044.5" y1="398" x2="1108.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1115.5" y1="398" x2="1051.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1051.5" y1="326" x2="1101.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1108.5" y1="326" x2="1058.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1058.5" y1="254" x2="1094.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1101.5" y1="254" x2="1065.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1015" y1="182" x2="1145" y2="182" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="1015" y1="182" x2="1015" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1145" y1="182" x2="1145" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1037.5" y1="110" x2="1122.5" y2="110" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="1037.5" y1="110" x2="1037.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1122.5" y1="110" x2="1122.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M89,199.5 Q550,269.5 1011,199.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M219,199.5 Q680,269.5 1141,199.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M111.5,127.5 Q572.5,197.5 1033.5,127.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M196.5,127.5 Q657.5,197.5 1118.5,127.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="563.5" y1="232.5" x2="563.5" y2="218.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="575" y1="232.5" x2="575" y2="218.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M539.5,198 Q542,218.5 569.5,220 Q594.5,218.5 597,193.5 Q592.5,179.5 576.5,182 Q558,182 539.5,198 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M539.5,198 L516.5,207 L521,193.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="599.5" cy="182" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M611,179.5 L622.5,184 L611,186.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="602.5" cy="178.5" r="2.875" fill="#ffffff"/>
  <path d="M555.5,198 Q574,207 590,198" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
  <line x1="619" y1="234" x2="619" y2="220" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="630.5" y1="234" x2="630.5" y2="220" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M595,199.5 Q597,220 624.5,221.5 Q650,220 652.5,195 Q647.5,181 631.5,183.5 Q613,183.5 595,199.5 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M595,199.5 L572,208.5 L576.5,195 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="654.5" cy="183.5" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M666,181 L677.5,185.5 L666,188 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="658" cy="180" r="2.875" fill="#ffffff"/>
  <path d="M611,199.5 Q629.5,208.5 645.5,199.5" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
  <line x1="692.5" y1="234.5" x2="692.5" y2="220.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="704" y1="234.5" x2="704" y2="220.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M728.5,200 Q726,220.5 698.5,222 Q673,220.5 671,195.5 Q675.5,181.5 691.5,184 Q710,184 728.5,200 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M728.5,200 L751.5,209 L746.5,195.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="668.5" cy="184" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M657,181.5 L645.5,186 L657,188.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="665" cy="180.5" r="2.875" fill="#ffffff"/>
  <path d="M712,200 Q694,209 677.5,200" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
  <line x1="766.5" y1="233" x2="766.5" y2="219.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="778" y1="233" x2="778" y2="219.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M742.5,198.5 Q744.5,219.5 772,220.5 Q797.5,219.5 800,194 Q795,180 779,182.5 Q760.5,182.5 742.5,198.5 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M742.5,198.5 L719.5,208 L724,194 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="802" cy="182.5" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M813.5,180 L825,185 L813.5,187 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="805.5" cy="179" r="2.875" fill="#ffffff"/>
  <path d="M758.5,198.5 Q777,208 793,198.5" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
</svg>

## Key idea

### Current is not used up: Kirchhoff's current law
Electric current is the motion of charges. Charge is neither created nor destroyed, and it does not collect in the wires when the currents stay constant. Therefore all the charge that arrives at a **junction**, a point where a wire divides into branches, also leaves it. **The sum of the currents arriving at a junction is equal to the sum of the currents leaving it.** This is Kirchhoff's current law. For the same reason the current is equal on both sides of a resistor: in a resistor electrical energy changes into internal energy of the resistor, which is transferred to the surroundings as heat, but the current is not used up in it.

The voltage across parallel branches is the same (chapter *Resistors in series and in parallel*), so by Ohm's law the branch with the smaller resistance carries the larger current. In the figure the current in the $30\,\Omega$ branch is twice the current in the $60\,\Omega$ branch, and the branch currents $0.20\,\text{A}$ and $0.10\,\text{A}$ are together equal to the arriving current $0.30\,\text{A}$.

<svg data-fig="junction" viewBox="0 0 600 330" role="img" aria-label="Schematic of a junction, not to scale. From the left a current I1 = 0.30 A arrives along a wire at the junction. Two branches leave it: the upper branch has a 30 ohm resistor and the lower branch a 60 ohm resistor, and the branches join again on the right. The width of the purple current arrows is proportional to the current: in the upper branch I2 = 0.20 A, in the lower branch I3 = 0.10 A, and together the branches carry away as much current as arrives at the junction, 0.30 A." style="max-width:100%;font-size:24px">
  <polyline points="24,170 200,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="200,170 200,72 520,72 520,268 200,268 200,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="520,170 576,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="348" y="60" width="64" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="348" y="256" width="64" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="200" cy="170" r="6" fill="#1f2933"/>
  <circle cx="520" cy="170" r="6" fill="#1f2933"/>
  <foreignObject x="351" y="91.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="351" y="219.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <path d="M40,152 L124,152 L124,160 L150,140 L124,120 L124,128 L40,128 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="15" y="93.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1 = 0.30\,\text{A}$</div></foreignObject>
  <path d="M230,52 L298,52 L298,60 L320,44 L298,28 L298,36 L230,36 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M230,300 L302,300 L302,307 L320,296 L302,285 L302,292 L230,292 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="334" y="27.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2 = 0.20\,\text{A}$</div></foreignObject>
  <foreignObject x="334" y="283.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_3 = 0.10\,\text{A}$</div></foreignObject>
  <foreignObject x="216" y="155.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{junction}$</div></foreignObject>
</svg>

### Potential: the electrical level of every point
Every point of a circuit has a **potential** $V$: the voltage of the point relative to a chosen zero point. The zero point is often chosen to be the negative terminal of the voltage source or the earth, and its potential is $0\,\text{V}$. The voltage between two points is the difference of their potentials. Potential can be compared with height: height depends on where it is measured from, but the difference in height between two points does not. In the same way, moving the zero point changes all potentials by the same amount, but the voltages stay the same.

Potential changes only in the source and in the resistors. In the source it rises from the negative terminal to the positive terminal by the voltage of the source; in this chapter the source is ideal, that is, the effect of its own resistance is neglected. In a resistor it drops in the direction of the current by the voltage $U = RI$. The resistance of a wire is so small that its voltage is neglected, so all points of the same wire have the same potential. In the circuit of the figure the points $B$ and $C$ are the same wire, so the potential of both is $6.0\,\text{V}$.

<svg data-fig="circuit" viewBox="0 0 600 368" role="img" aria-label="Circuit diagram, not to scale: a voltage source of 9.0 V, from its positive terminal a resistor R1 = 10 ohms and after it two parallel resistors R2 = 30 ohms and R3 = 60 ohms, which return to the negative terminal of the source. The points A–F are marked on the wires with their potentials when the negative terminal of the source is the zero point: A 9.0 V, B and C 6.0 V, and D, E and F 0 V. At all points of the same wire the potential is the same; it changes only in the source and the resistors." style="max-width:100%;font-size:24px">
  <polyline points="72,177 72,90 470,90 470,280 72,280 72,193" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="330,90 330,280" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="46" y1="177" x2="98" y2="177" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="59" y1="193" x2="85" y2="193" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <rect x="164" y="78" width="64" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="318" y="153" width="24" height="64" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="458" y="153" width="24" height="64" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="330" cy="90" r="6" fill="#1f2933"/>
  <circle cx="330" cy="280" r="6" fill="#1f2933"/>
  <foreignObject x="26" y="152.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="26" y="192.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="100" y="170.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 9.0\,\text{V}$</div></foreignObject>
  <foreignObject x="126" y="111.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1 = 10\,\Omega$</div></foreignObject>
  <foreignObject x="352" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="352" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="492" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_3$</div></foreignObject>
  <foreignObject x="492" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <circle cx="112" cy="90" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="98" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="72" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$9.0\,\text{V}$</div></foreignObject>
  <circle cx="286" cy="90" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="272" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <foreignObject x="246" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6.0\,\text{V}$</div></foreignObject>
  <circle cx="470" cy="90" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="456" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="430" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6.0\,\text{V}$</div></foreignObject>
  <circle cx="470" cy="280" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="456" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D$</div></foreignObject>
  <foreignObject x="430" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <circle cx="330" cy="280" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="316" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="290" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <circle cx="112" cy="280" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="98" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="72" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
</svg>

### A round trip in a loop: Kirchhoff's voltage law
A **loop** is a closed path in a circuit that returns to its starting point. When a loop is traversed, the potential returns to the same value from which it started. Therefore **the sum of the rises and drops of potential in a loop is zero**. This is Kirchhoff's voltage law. In a circuit of one loop the voltage of the source is equal to the sum of the voltages of the resistors. In terms of energy, voltage tells how much energy per unit of charge changes from one form to another (chapter *Circuit, electric current and voltage*): a charge gains energy in the source and gives up the same amount in the resistors.

The circuit of the figure has two loops, one through the resistor $R_2$ and the other through the resistor $R_3$. In each of them the $9.0\,\text{V}$ of the source divides into the voltage $3.0\,\text{V}$ of the resistor $R_1$ and the voltage $6.0\,\text{V}$ of the branch. This is why the voltage across parallel branches is the same.

### A bird on a wire
The bird's feet are at two points of the same wire, only a few centimetres apart. The bird is a branch parallel to the piece of wire between its feet, whose resistance is negligible. Therefore the voltage between the feet is only millivolts, and by Ohm's law a negligible current flows through the bird. By the current law almost all the current thus continues along the wire. The potential of the bird relative to the ground is high, but danger would arise only if it touched another wire or a pylon at the same time, since their potential is different. For a person the situation is not comparable: a high-voltage line must not be approached, because an electric arc can form even without contact.

<figure class="unit-photo"><img src="pics/fy6/swallows-power-line.webp" alt="Two barn swallows sit on an overhead line against a blue sky."><figcaption>Barn swallows on an overhead line. The line in the photo is an insulated cable, but birds sit on bare lines in the same way: both feet are at two nearby points of the same conductor.</figcaption></figure>

## Formula: Kirchhoff's laws
Kirchhoff's current law for a junction:
```latex
\sum I_\text{in} = \sum I_\text{out}
```
where $I_\text{in}$ are the currents arriving at the junction (A) and $I_\text{out}$ the currents leaving it (A). For a current dividing into two branches $I_1 = I_2 + I_3$.

The voltage between the points $A$ and $B$ is the difference of the potentials:
```latex
U_{AB} = V_A - V_B
```
where $U_{AB}$ is the voltage (V) and $V_A$ and $V_B$ are the potentials of the points (V) relative to the same zero point. The voltage is positive when $A$ is at the higher potential.

Kirchhoff's voltage law for a loop:
```latex
\sum \Delta V = 0
```
where $\Delta V$ (V) is the change of potential in each part of the loop when the loop is traversed once. In the source from the negative terminal to the positive terminal $\Delta V = +U$, in a resistor in the direction of the current $\Delta V = -RI$, and in a wire $\Delta V = 0$. In a circuit of one loop with two resistors the law gives $U - R_1 I - R_2 I = 0$, that is, $U = R_1 I + R_2 I$.

A **potential graph** shows the potential at different points of a loop. In the graph the loop of the circuit marked with the points $A$–$F$ is traversed from the negative terminal $F$ through the resistors $R_1$ and $R_2$ back to the point $F$. The rise of the source $+9.0\,\text{V}$ is equal to the total of the drops of the resistors $-3.0\,\text{V}$ and $-6.0\,\text{V}$, and in the wires the graph is horizontal.

<svg data-fig="potential-graph" viewBox="0 0 600 360" role="img" aria-label="Potential graph, vertical axis to scale, horizontal axis schematic: potential V in volts as the loop of the circuit in the figure is traversed from the negative terminal F of the source through the source and the resistors R1 and R2 back to F. In the source the potential rises from 0 volts to 9.0 volts. Along the wire to the point A it stays at 9.0 volts, in the resistor R1 it drops by 3.0 V to 6.0 volts at the point B, and in the resistor R2 from 6.0 V to zero at the point E. From the point E to the point F the potential stays at zero. The sum of the rises and drops is zero." style="max-width:100%;font-size:24px">
  <line x1="96" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="230" x2="96" y2="230" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="215.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="110" x2="96" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="95.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$9$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{point}$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{V})$</div></foreignObject>
  <rect x="127.5" y="70" width="27" height="220" fill="#eef5f9"/>
  <foreignObject x="119" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <rect x="230.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="231" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <rect x="365.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="366" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <line x1="97" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="64" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,290 141,290 141,110 186,110 230.5,110 275.5,170 320.5,170 365.5,170 410,290 455,290 500,290" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="96" y1="290" x2="96" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="82" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <line x1="186" y1="290" x2="186" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="320.5" y1="290" x2="320.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="306.5" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <line x1="455" y1="290" x2="455" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <line x1="500" y1="290" x2="500" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="486" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <circle cx="96" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186" cy="110" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="170" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="455" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="149" y="185.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+9.0\,\text{V}$</div></foreignObject>
  <foreignObject x="283.5" y="125.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-3.0\,\text{V}$</div></foreignObject>
  <foreignObject x="418" y="215.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-6.0\,\text{V}$</div></foreignObject>
</svg>

## Worked example
The voltage of a voltage source is $12\,\text{V}$. From the positive terminal of the source the current flows through a resistor $R_1 = 20\,\Omega$ to a junction $B$, from which two parallel branches leave: a resistor $R_2 = 60\,\Omega$ and a resistor $R_3 = 30\,\Omega$. The branches return to the negative terminal of the source, which is the zero point. What is the potential of the point $B$, and how large is the current through the resistor $R_3$?

<!-- vaihe -->

**Given and find.** $U = 12\,\text{V}$, $R_1 = 20\,\Omega$, $R_2 = 60\,\Omega$, $R_3 = 30\,\Omega$ and the potential of the negative terminal $0\,\text{V}$. We are asked for the potential $V_B$ of the point $B$ and the current $I_3$.

<!-- vaihe -->

**Principle.** The whole current $I_1$ flows through the source and the resistor $R_1$. The parallel resistors are replaced with a single resistor $R_{23}$, and then Ohm's law gives $I_1$. By the voltage law the potential drops from the value $U$ of the positive terminal in the resistor $R_1$ by the voltage $R_1 I_1$. The resistor $R_3$ is between the point $B$ and the zero point, so its voltage is $V_B$.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{R_2} + \frac{1}{R_3} \\
&I_1 = \frac{U}{R_1 + R_{23}} \\
&V_B = U - R_1 I_1 \\
&I_3 = \frac{V_B}{R_3}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: all quantities are in base units, and $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{60\,\Omega} + \frac{1}{30\,\Omega} \\
&R_{23} = 20\,\Omega \\
&I_1 = \frac{12\,\text{V}}{20\,\Omega + 20\,\Omega} = 0.30\,\text{A} \\
&V_B = 12\,\text{V} - 20\,\Omega \cdot 0.30\,\text{A} \\
&\phantom{V_B} = 6.0\,\text{V} \\
&I_3 = \frac{6.0\,\text{V}}{30\,\Omega} = 0.20\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Result.** The potential of the point $B$ is $6.0\,\text{V}$, and a current of $0.20\,\text{A}$ flows through the resistor $R_3$. The results are given to two significant figures like the resistances.

<!-- vaihe -->

**Reasonableness.** A current of $6.0\,\text{V} : 60\,\Omega = 0.10\,\text{A}$ flows through the resistor $R_2$, and the branch currents are together $0.30\,\text{A}$, as the current law requires. In the loop $12\,\text{V} - 6.0\,\text{V} - 6.0\,\text{V} = 0$, as the voltage law requires. The branch with the smaller resistance carries the larger current, as it should.

## Common misconception
Many think that a resistor uses up current, so that the current after the resistor would be smaller than before it. A resistor changes electrical energy into its internal energy, but no charges disappear: an ammeter shows the same reading on both sides of a resistor. In a resistor the potential decreases, not the current.

Another common mistake is to use the voltage of the source when calculating the current of a branch. If in the example above one calculated $I_3 = 12\,\text{V} : 30\,\Omega = 0.40\,\text{A}$, more current would leave into the branches in total than arrives at the junction. The voltage of a branch is the voltage of the source minus the voltages of the resistors connected in series with it, here $6.0\,\text{V}$. A third mistake is to think that voltage is a property of a single point: voltage is always the potential difference between two points.

## Summary
- Kirchhoff's current law: the sum of the currents arriving at a junction is equal to the sum of the currents leaving it, because charge is conserved. Current is not used up in a resistor.
- Potential $V$ is the voltage of a point relative to the zero point. Voltage is a potential difference $U_{AB} = V_A - V_B$, and it does not depend on the choice of the zero point.
- Potential rises in the source from the negative terminal to the positive terminal, drops in a resistor in the direction of the current by $RI$, and stays the same in a wire.
- Kirchhoff's voltage law: the sum of the changes of potential in a loop is zero, $\sum \Delta V = 0$. Therefore the voltage of the source is shared among the resistors of the loop, and the voltage across parallel branches is the same.
