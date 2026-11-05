# Electromagnetic induction

> **Why** does a bicycle dynamo light the lamp only while the wheel is turning, even though the dynamo contains no battery or accumulator?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a cyclist rides along a forest road at dusk. The dynamo is in the hub of the front wheel of the bicycle, and the lamp on the handlebars shines: the beam of light falls on the road in front of the wheel. The sky is evening blue, and spruces stand at the edge of the road." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy75h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1971c2"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy75h-road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#1f2933"/></linearGradient><linearGradient id="fy75h-beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><radialGradient id="fy75h-lamp" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078"/><stop offset="0.55" stop-color="#e8590c" stop-opacity="0.8"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy75h-sky)"/>
  <circle cx="351" cy="85.5" r="1.53206" fill="#ffffff"/>
  <circle cx="513.5" cy="130" r="2.18008" fill="#ffffff"/>
  <circle cx="380" cy="42" r="2.65251" fill="#ffffff"/>
  <circle cx="1035.5" cy="38" r="2.41039" fill="#ffffff"/>
  <circle cx="727" cy="65.5" r="1.98114" fill="#ffffff"/>
  <circle cx="1039" cy="91.5" r="2.38087" fill="#ffffff"/>
  <circle cx="803" cy="75" r="2.88057" fill="#ffffff"/>
  <circle cx="190.5" cy="85.5" r="2.22739" fill="#ffffff"/>
  <circle cx="972" cy="90" r="2.18079" fill="#ffffff"/>
  <circle cx="123.5" cy="121.5" r="1.60766" fill="#ffffff"/>
  <circle cx="369" cy="76.5" r="2.85776" fill="#ffffff"/>
  <circle cx="860.5" cy="107.5" r="2.11804" fill="#ffffff"/>
  <circle cx="742.5" cy="120.5" r="2.38678" fill="#ffffff"/>
  <circle cx="204" cy="118.5" r="2.58655" fill="#ffffff"/>
  <circle cx="128.5" cy="159" r="1.5738" fill="#ffffff"/>
  <circle cx="284.5" cy="137" r="2.88516" fill="#ffffff"/>
  <circle cx="589.5" cy="47" r="2.99958" fill="#ffffff"/>
  <circle cx="536" cy="123" r="2.41208" fill="#ffffff"/>
  <path d="M0,380 L25.5,308 L51.5,380 L79,299.5 L107,380 L133.5,303.5 L160.5,380 L202,245.5 L243.5,380 L272.5,296 L301,380 L329.5,297 L358,380 L396.5,256.5 L435.5,380 L479.5,235.5 L523.5,380 L562,257 L601,380 L646,232 L690.5,380 L733.5,240.5 L776.5,380 L812,269 L847.5,380 L891.5,236.5 L935,380 L970.5,269 L1006.5,380 L1037.5,286 L1068.5,380 L1107.5,256 L1146.5,380 L1182.5,268 L1218,380 V420 H0 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="81.5" y="395" width="17" height="25" fill="#b8622d"/>
  <path d="M14.5,399 L90,315 L165.5,399 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,315 L165.5,399 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M31,353 L90,269 L149,353 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,269 L149,353 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M48,306.5 L90,210 L132,306.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,210 L132,306.5 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="199.5" y="389" width="21" height="31" fill="#b8622d"/>
  <path d="M116.5,394 L210,290 L303.5,394 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M210,290 L303.5,394 H210 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M137,337 L210,233 L283,337 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M210,233 L283,337 H210 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M158,279.5 L210,160 L262,279.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M210,160 L262,279.5 H210 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1030.5" y="391" width="19" height="29" fill="#b8622d"/>
  <path d="M953.5,396 L1040,300 L1126.5,396 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1040,300 L1126.5,396 H1040 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M973,343 L1040,247 L1107,343 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1040,247 L1107,343 H1040 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M992,290.5 L1040,180 L1088,290.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1040,180 L1088,290.5 H1040 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1142" y="396" width="16" height="24" fill="#b8622d"/>
  <path d="M1078,400 L1150,320 L1222,400 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,320 L1222,400 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1094,356 L1150,276 L1206,356 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,276 L1206,356 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1110,312 L1150,220 L1190,312 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1150,220 L1190,312 H1150 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="0" y="410" width="1200" height="190" fill="url(#fy75h-road)"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <rect x="40" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="180" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="320" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="460" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="600" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="740" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="880" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="1020" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <rect x="1160" y="532" width="70" height="8" rx="3" fill="#f1dfb5"/>
  <path d="M742,348 L1110,470 L1160,560 L760,372 Z" fill="url(#fy75h-beam)" stroke-linejoin="round" fill-opacity="0.7"/>
  <circle cx="470" cy="520" r="92" fill="none" stroke="#1f2933" stroke-width="13.8"/>
  <circle cx="470" cy="520" r="82.8" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="470" y1="520" x2="549" y2="520" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="538.5" y2="559.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="509.5" y2="588.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="470" y2="599" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="430.5" y2="588.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="401.5" y2="559.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="391" y2="520" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="401.5" y2="480.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="430.5" y2="451.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="470" y2="441" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="509.5" y2="451.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="520" x2="538.5" y2="480.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="470" cy="520" r="8.28" fill="#1f2933"/>
  <circle cx="700" cy="520" r="92" fill="none" stroke="#1f2933" stroke-width="13.8"/>
  <circle cx="700" cy="520" r="82.8" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="700" y1="520" x2="779" y2="520" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="768.5" y2="559.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="739.5" y2="588.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="700" y2="599" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="660.5" y2="588.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="631.5" y2="559.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="621" y2="520" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="631.5" y2="480.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="660.5" y2="451.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="700" y2="441" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="739.5" y2="451.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="520" x2="768.5" y2="480.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="700" cy="520" r="8.28" fill="#1f2933"/>
  <path d="M470,520 L553,520 L651.5,423.5 L536.5,423.5 Z" fill="none" stroke="#c92a2a" stroke-width="11.04" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M553,520 L534.5,398" fill="none" stroke="#c92a2a" stroke-width="11.04" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M651.5,423.5 L700,520" fill="none" stroke="#c92a2a" stroke-width="11.04" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M651.5,423.5 L645,398" fill="none" stroke="#c92a2a" stroke-width="11.04" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M507,398 H541.5" fill="none" stroke="#1f2933" stroke-width="13.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M628.5,400.5 Q645,391 665.5,400.5" fill="none" stroke="#1f2933" stroke-width="9.2" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="553" cy="520" r="18.4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M525,389 L576,416.5 L566.5,534" fill="none" stroke="#1f2933" stroke-width="17.25" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M557.5,538.5 h18.5" fill="none" stroke="#6c757d" stroke-width="10.35" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M518.5,393.5 L594,320" fill="none" stroke="#d0e6fb" stroke-width="25.3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M594,320 L645,396" fill="none" stroke="#d0e6fb" stroke-width="13.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="645" cy="396" r="6.9" fill="#f1dfb5"/>
  <circle cx="617" cy="301.5" r="17.25" fill="#f1dfb5"/>
  <path d="M596.5,300.5 Q603.5,276 626.5,279.5 Q640,285.5 637,297 Z" fill="#e8590c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="700" cy="520" r="18" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <circle cx="700" cy="520" r="8" fill="#6c757d"/>
  <path d="M712,508 C726,470 736,420 742,366" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="728" y="340" width="30" height="24" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="756" cy="352" r="10" fill="url(#fy75h-lamp)"/>
  <circle cx="756" cy="352" r="5" fill="#ffc078"/>
</svg>

## Key idea

### Faraday's observation
In the chapter *Magnetic field of a wire and a coil*, an electric current produced a magnetic field. Michael Faraday spent years looking for the reverse effect: could a magnetic field produce an electric current? In 1831 he noticed that a magnet at rest beside a coil does nothing, however strong the magnet is. When the magnet is pushed into the coil, the needle of a voltmeter connected to the coil deflects. When the magnet is at rest inside the coil, the needle returns to zero. When the magnet is pulled out, the needle deflects the other way. The faster the magnet is moved and the more turns the coil has, the greater the voltage. The same happens if the magnet is at rest and the coil is moved.

<svg data-fig="faraday" viewBox="0 0 600 340" role="img" aria-label="Schematic picture, not to scale: Faraday&#x27;s experiment in three stages. In each picture a wire coil is connected to a voltmeter. On the left a bar magnet is pushed north pole first towards the coil and into it, and the needle of the meter deflects to the right. In the middle the magnet is at rest inside the coil, and the needle is at zero. On the right the magnet is pulled out of the coil, and the needle deflects to the left." style="max-width:100%;font-size:24px">
  <foreignObject x="83.5" y="15.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in}$</div></foreignObject>
  <circle cx="146" cy="112" r="40" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="124" y1="111.5" x2="119.5" y2="108" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="134" y1="104" x2="131.5" y2="99" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="101" x2="146" y2="95.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="158" y1="104" x2="160.5" y2="99" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="168" y1="111.5" x2="172.5" y2="108" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="130" x2="164" y2="103.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="146" cy="130" r="4" fill="#1f2933"/>
  <path d="M112,292 C104,318 96,202 128,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M182,292 C192,318 192,202 164,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="10" y="246" width="42" height="32" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="21" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <rect x="52" y="246" width="42" height="32" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="63" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <ellipse cx="112" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="126" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="140" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="154" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="168" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="182" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <line x1="18" y1="212" x2="73" y2="212" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M86,212 L72,218.5 L72,205.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="35.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="200" y1="20" x2="200" y2="320" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="258.5" y="15.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{at rest}$</div></foreignObject>
  <circle cx="346" cy="112" r="40" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="324" y1="111.5" x2="319.5" y2="108" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="334" y1="104" x2="331.5" y2="99" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="346" y1="101" x2="346" y2="95.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="358" y1="104" x2="360.5" y2="99" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="368" y1="111.5" x2="372.5" y2="108" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="346" y1="130" x2="346" y2="98" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="346" cy="130" r="4" fill="#1f2933"/>
  <path d="M312,292 C304,318 296,202 328,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M382,292 C392,318 392,202 364,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="272" y="246" width="42" height="32" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="283" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <rect x="314" y="246" width="42" height="32" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="325" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <ellipse cx="312" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="326" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="340" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="354" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="368" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="382" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <line x1="400" y1="20" x2="400" y2="320" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="477.5" y="15.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{out}$</div></foreignObject>
  <circle cx="546" cy="112" r="40" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="524" y1="111.5" x2="519.5" y2="108" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="534" y1="104" x2="531.5" y2="99" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="101" x2="546" y2="95.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="558" y1="104" x2="560.5" y2="99" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="568" y1="111.5" x2="572.5" y2="108" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="130" x2="528" y2="103.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="546" cy="130" r="4" fill="#1f2933"/>
  <path d="M512,292 C504,318 496,202 528,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M582,292 C592,318 592,202 564,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="410" y="246" width="42" height="32" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="421" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <rect x="452" y="246" width="42" height="32" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="463" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <ellipse cx="512" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="526" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="540" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="554" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="568" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <ellipse cx="582" cy="262" rx="7" ry="30" fill="none" stroke="#b8622d" stroke-width="3"/>
  <line x1="486" y1="212" x2="431" y2="212" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M418,212 L432,205.5 L432,218.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="435.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/shake-flashlight.webp" alt="A transparent plastic torch on a pale background; inside the body a copper-coloured coil can be seen, with the black lamp end on the left."><figcaption>A shake torch. When the torch is shaken, a magnet inside it slides back and forth through the coil. The magnetic flux through the coil changes, so a voltage is induced in the coil, which charges the torch's energy store.</figcaption></figure>

### A change produces a voltage
The phenomenon is called **electromagnetic induction**, and the voltage produced between the ends of the coil is called the **induced voltage**. When the ends of the coil are joined by a wire or a lamp, an induced current flows in the circuit. What all of Faraday's experiments have in common is that the magnetic field passing through the coil **changes**. A coil at rest in a strong but unchanging field gets no voltage. The change can come about in many ways: the magnet or the coil moves, the coil turns in the field, the area of the loop changes, or the current in a nearby electromagnet is switched on or off. In the hub dynamo of a bicycle, a magnet turns in the middle of the coils when the wheel turns. When the wheel stands still, nothing changes and the lamp stays dark.

### Magnetic flux
The size of the change is measured with the **magnetic flux**. It tells how much magnetic field passes through a loop. When a uniform field is perpendicular to the plane of the loop, the magnetic flux is
```latex
\Phi = BA
```
where $\Phi$ is the magnetic flux, $B$ the magnetic flux density (T) and $A$ the area of the loop (m²). The unit of flux is the weber: $1\,\text{Wb} = 1\,\text{T}\cdot\text{m}^2$. The flux is greater, the stronger the field and the larger the loop. If the loop is tilted, fewer field lines pass through it and the flux decreases. When the plane of the loop is parallel to the field, no field line passes through it and the flux is zero.

<svg data-fig="flux" viewBox="0 0 600 340" role="img" aria-label="Schematic picture from the side, three parts: horizontal green field lines point from left to right, and a wire loop is seen edge-on as a narrow oval. On the left the plane of the loop is perpendicular to the field, and five field lines pass through the loop: the flux is B times A. In the middle the loop is tilted, and only three lines pass through it: the flux is smaller. On the right the plane of the loop is parallel to the field, and no line passes through it: the flux is zero." style="max-width:100%;font-size:24px">
  <line x1="18" y1="78" x2="182" y2="78" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M166,78 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="18" y1="108" x2="182" y2="108" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M166,108 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="18" y1="138" x2="182" y2="138" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M166,138 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="18" y1="168" x2="182" y2="168" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M166,168 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="18" y1="198" x2="182" y2="198" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M166,198 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="18" y1="228" x2="182" y2="228" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M166,228 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="18" y1="258" x2="182" y2="258" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M166,258 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <ellipse cx="100" cy="168" rx="13" ry="76" fill="#b2f2bb" fill-opacity="0.35" stroke="#b8622d" stroke-width="5" transform="rotate(0 100 168)"/>
  <foreignObject x="71" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi = BA$</div></foreignObject>
  <line x1="200" y1="30" x2="200" y2="320" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="218" y1="78" x2="382" y2="78" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M366,78 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="218" y1="108" x2="382" y2="108" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M366,108 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="218" y1="138" x2="382" y2="138" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M366,138 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="218" y1="168" x2="382" y2="168" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M366,168 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="218" y1="198" x2="382" y2="198" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M366,198 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="218" y1="228" x2="382" y2="228" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M366,228 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="218" y1="258" x2="382" y2="258" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M366,258 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <ellipse cx="300" cy="168" rx="13" ry="76" fill="#b2f2bb" fill-opacity="0.35" stroke="#b8622d" stroke-width="5" transform="rotate(-55 300 168)"/>
  <foreignObject x="271" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi < BA$</div></foreignObject>
  <line x1="400" y1="30" x2="400" y2="320" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="418" y1="78" x2="582" y2="78" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,78 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="108" x2="582" y2="108" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,108 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="138" x2="582" y2="138" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,138 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="168" x2="582" y2="168" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,168 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="198" x2="582" y2="198" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,198 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="228" x2="582" y2="228" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,228 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="258" x2="582" y2="258" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566,258 l-12,-6 v12 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <ellipse cx="500" cy="183" rx="13" ry="76" fill="#b2f2bb" fill-opacity="0.35" stroke="#b8622d" stroke-width="5" transform="rotate(-90 500 183)"/>
  <foreignObject x="477.5" y="285.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi = 0$</div></foreignObject>
  <foreignObject x="28" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="90" y="25.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
</svg>

## Formula: Faraday's law of induction
Faraday's observations are summarised in **Faraday's law of induction**: the induced voltage in a coil is proportional to the rate of change of the magnetic flux through the coil and to the number of turns of the coil:
```latex
e = -N\frac{\Delta\Phi}{\Delta t}
```
where $e$ is the induced voltage (V), $N$ the number of turns of the coil, $\Delta\Phi$ the change in the magnetic flux through one turn (Wb) and $\Delta t$ the time (s) in which the change takes place. The turns are in series, so each turn adds the same amount to the voltage. The units fit together: $1\,\tfrac{\text{Wb}}{\text{s}} = 1\,\text{V}$. The minus sign gives the direction of the induced voltage: it opposes the change that produces it. The direction is discussed in the chapter *Lenz's law and eddy currents*; the magnitude of the voltage is calculated from the equation $|e| = N \cdot \Delta\Phi : \Delta t$.

### The flux graph and the voltage
The quotient $\Delta\Phi : \Delta t$ is the slope of the flux graph $(t, \Phi)$. The induced voltage therefore does not depend on how large the flux is but on how steeply it changes. In the graph below, a coil of ten turns moves at a steady speed through a region of magnetic field. When the coil enters the field, the flux grows steadily and the voltage is constant. When the coil is completely inside the field, the flux is at its greatest but does not change, so the voltage is zero. When the coil leaves the field, the flux decreases and the voltage is equal in size but opposite in sign.

<svg data-fig="graph" viewBox="0 0 600 380" role="img" aria-label="Two graphs to scale on the same time axis from zero to four seconds. A square coil of ten turns, side 0.10 m, moves at a speed of 0.10 m/s through a region of magnetic field of 0.20 T. Upper graph: the magnetic flux in milliwebers is zero until 0.5 seconds, grows steadily to 2.0 at 1.5 s, stays constant until 2.5 seconds and decreases steadily to zero at 3.5 s. Lower graph: the induced voltage in millivolts is zero when the flux does not change, minus 20 while the flux grows and plus 20 while the flux decreases. Dashed lines at 0.5, 1.5, 2.5 and 3.5 s link the graphs." style="max-width:100%;font-size:24px">
  <line x1="141" y1="150" x2="141" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="150" x2="186" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="150" x2="230.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="150" x2="275.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="150" x2="320.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="150" x2="365.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="150" x2="410" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="150" x2="455" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="150" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="134" x2="500" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="118" x2="500" y2="118" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="102" x2="500" y2="102" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="86" x2="500" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="70" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="150" x2="514" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,150 L513,156 L513,144 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="151" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="150" x2="141" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="150" x2="186" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="150" x2="230.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="150" x2="275.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="150" x2="320.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="150" x2="365.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="410" y1="150" x2="410" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="150" x2="455" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="150" x2="500" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="134" x2="96" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="118" x2="96" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="102" x2="96" y2="102" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="86" x2="96" y2="86" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="70" x2="96" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="532" y="135.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Phi\ (\text{mWb})$</div></foreignObject>
  <line x1="141" y1="332" x2="141" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="332" x2="186" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="332" x2="230.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="332" x2="275.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="332" x2="320.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="332" x2="365.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="332" x2="410" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="332" x2="455" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="332" x2="500" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="312" x2="500" y2="312" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="292" x2="500" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="252" x2="500" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="232" x2="500" y2="232" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="332" x2="96" y2="272" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="272" x2="514" y2="272" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,272 L513,278 L513,266 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="273" x2="96" y2="198" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,186 L102,199 L90,199 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="272" x2="141" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="272" x2="186" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="272" x2="230.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="272" x2="275.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="272" x2="320.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="272" x2="365.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="410" y1="272" x2="410" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="272" x2="455" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="272" x2="500" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="312" x2="96" y2="312" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="297.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="89" y1="292" x2="96" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="252" x2="96" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="232" x2="96" y2="232" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="532" y="257.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="155.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e\ (\text{mV})$</div></foreignObject>
  <foreignObject x="66" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="66" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="141" y1="70" x2="141" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="230.5" y1="70" x2="230.5" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="320.5" y1="70" x2="320.5" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="410" y1="70" x2="410" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="176" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="265.5" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="355.5" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="445" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <polyline points="96,150 141,150 230.5,86 320.5,86 410,150 455,150" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,272 141,272 141,312 230.5,312 230.5,272 320.5,272 320.5,232 410,232 410,272 455,272" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

### The induced voltage of a moving conductor
When a straight metal rod moves with velocity $v$ perpendicular to a uniform magnetic field $B$, the conduction electrons of the rod move along with it. The chapter *Charged particle in electric and magnetic fields* showed that a magnetic field exerts a force $F_\text{m} = evB$ on a moving charge. The force points along the rod, so the electrons move to one end of the rod. A deficit of electrons is left at the other end, and an electric field $E$ appears between the ends, pulling the electrons back. The shift stops when the electric force $F_\text{s} = eE$ cancels the magnetic force. Then $eE = evB$, that is, $E = vB$. In a uniform field the voltage is the product of the field and the length (chapter *Uniform electric field*), so the induced voltage between the ends of the rod is
```latex
e = vBl
```
where $v$ is the velocity of the rod (m/s), $B$ the magnetic flux density (T) and $l$ the length of the rod in the field (m), when the velocity, the rod and the field are mutually perpendicular.

<svg data-fig="rod" viewBox="0 0 600 360" role="img" aria-label="Schematic picture from above, not to scale: two horizontal metal rails whose left ends are joined to a voltmeter. On the rails is a vertical copper rod that moves to the right at velocity v. The magnetic field points into the paper, shown by evenly spaced green crosses. In the middle of the rod is an electron, on which the magnetic force points downwards and the electric force upwards. Electrons have collected at the lower end of the rod, which is negative, and the upper end is positive. In the rod the electric field points from top to bottom. The distance between the rails, that is, the length of the rod in the field, is l." style="max-width:100%;font-size:24px">
  <rect x="70" y="90" width="450" height="12" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="70" y="258" width="450" height="12" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="70" y1="96" x2="52" y2="96" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="70" y1="264" x2="52" y2="264" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="52" y1="96" x2="52" y2="154" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="52" y1="206" x2="52" y2="264" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="52" cy="180" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="42" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <line x1="114" y1="124" x2="126" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="126" y1="124" x2="114" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="114" y1="174" x2="126" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="126" y1="174" x2="114" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="114" y1="224" x2="126" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="126" y1="224" x2="114" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="174" y1="124" x2="186" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="186" y1="124" x2="174" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="174" y1="174" x2="186" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="186" y1="174" x2="174" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="174" y1="224" x2="186" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="186" y1="224" x2="174" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="224" y1="124" x2="236" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="236" y1="124" x2="224" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="224" y1="174" x2="236" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="236" y1="174" x2="224" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="224" y1="224" x2="236" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="236" y1="224" x2="224" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="434" y1="124" x2="446" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="446" y1="124" x2="434" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="434" y1="174" x2="446" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="446" y1="174" x2="434" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="434" y1="224" x2="446" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="446" y1="224" x2="434" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="484" y1="124" x2="496" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="496" y1="124" x2="484" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="484" y1="174" x2="496" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="496" y1="174" x2="484" y2="186" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="484" y1="224" x2="496" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="496" y1="224" x2="484" y2="236" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="round"/>
  <foreignObject x="483.5" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <rect x="323" y="80" width="14" height="200" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="348" y="59.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="348" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="290" y1="124" x2="290" y2="224" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <path d="M290,236 L284,223 L296,223 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <foreignObject x="247" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#8a5f22">$\overline{E}$</div></foreignObject>
  <line x1="330" y1="192" x2="330" y2="226" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M330,238 L324,225 L336,225 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="330" y1="168" x2="330" y2="134" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M330,122 L336,135 L324,135 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="330" cy="180" r="9" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="325.5" y1="180" x2="334.5" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="348" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{m}$</div></foreignObject>
  <foreignObject x="348" y="119.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{s}$</div></foreignObject>
  <line x1="300" y1="40" x2="367" y2="40" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M380,40 L366,46.5 L366,33.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="390" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="548" y1="96" x2="548" y2="264" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="96" x2="556" y2="96" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="264" x2="556" y2="264" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="562" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$l$</div></foreignObject>
</svg>

The same result follows from Faraday's law. When the rod slides along rails, the area of the loop bounded by the rails and the rod grows in the time $\Delta t$ by $\Delta A = l \cdot v\Delta t$, so the flux grows by $\Delta\Phi = Bl \cdot v\Delta t$, and the magnitude of the voltage is $\Delta\Phi : \Delta t = vBl$. When the ends of the rails are joined by a resistor, a current flows in the circuit, and the magnetic field exerts a force $F = IlB$ on the current-carrying rod, as in the chapter *Force on a current-carrying wire: the electric motor and the loudspeaker*. The direction of this force and the conservation of energy are studied in the chapter *Lenz's law and eddy currents*.

## Worked example
A coil has $250$ turns and a cross-sectional area of $4.0\,\text{cm}^2$. The coil is between the poles of an electromagnet so that the uniform field is along the axis of the coil. When the current of the electromagnet is increased, the magnetic flux density of the field grows steadily from $0.10\,\text{T}$ to $0.50\,\text{T}$ in $0.20\,\text{s}$. How large is the induced voltage between the ends of the coil?

<!-- vaihe -->

**Given and find.** Number of turns $N = 250$, area $A = 4.0\,\text{cm}^2$, magnetic flux density at first $B_1 = 0.10\,\text{T}$ and at the end $B_2 = 0.50\,\text{T}$, time $\Delta t = 0.20\,\text{s}$. The magnitude of the induced voltage $|e|$ is asked.

<!-- vaihe -->

**Principle.** The magnetic flux through the coil changes because the field grows stronger, so an induced voltage appears in the coil according to Faraday's law. The field is along the axis, that is, perpendicular to the plane of the turns, so the flux through one turn is $\Phi = BA$. The area does not change, so the change in flux is $\Delta\Phi = (B_2 - B_1)A$.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&|e| = N\frac{\Delta\Phi}{\Delta t} \\
&|e| = \frac{N(B_2 - B_1)A}{\Delta t}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The area in square metres: $A = 4.0\,\text{cm}^2 = 4.0 \cdot (0.01\,\text{m})^2 = 4.0 \cdot 10^{-4}\,\text{m}^2$. The other quantities are in SI units.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&|e| = \frac{N(B_2 - B_1)A}{\Delta t} \\
&= \frac{250 \cdot 0.40\,\text{T} \cdot 4.0 \cdot 10^{-4}\,\text{m}^2}{0.20\,\text{s}} \\
&= 0.20\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Result.** An induced voltage of $0.20\,\text{V}$ appears between the ends of the coil for as long as the field keeps growing. The result is given to two significant figures, like the area $4.0\,\text{cm}^2$ and the time $0.20\,\text{s}$.

<!-- vaihe -->

**Reasonableness.** The units fit: $\tfrac{\text{T}\cdot\text{m}^2}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. One turn would give only $1.6 \cdot 10^{-4}\,\text{Wb} : 0.20\,\text{s} = 0.80\,\text{mV}$, and $250$ turns give $250$ times that voltage. When the field stops growing, the flux no longer changes and the voltage drops to zero, even though the field is then at its strongest.

## Common misconception
Many people think that the magnetic field itself produces a voltage and that a strong field gives a large voltage. However, an induced voltage arises only from a **change in flux**: a coil at rest beside a strong magnet gets no voltage, and a coil moving steadily inside a field gets no voltage if the flux through it does not change. The flux and its rate of change are different things, in the same way as position and velocity: a large flux can stay unchanged, and zero flux can change quickly. Another common mistake is to forget the number of turns $N$ or to convert the area wrongly: $1\,\text{cm}^2 = 10^{-4}\,\text{m}^2$, not $10^{-2}\,\text{m}^2$.

## Summary
- In electromagnetic induction, an induced voltage appears in a coil when the magnetic flux through it changes. If the flux does not change, no voltage appears.
- The magnetic flux is $\Phi = BA$ when the field is perpendicular to the plane of the loop; the unit is the weber, $1\,\text{Wb} = 1\,\text{T}\cdot\text{m}^2$.
- Faraday's law: $e = -N \cdot \Delta\Phi : \Delta t$. The voltage is the slope of the flux graph multiplied by the number of turns; the minus sign gives the direction.
- The voltage between the ends of a rod moving perpendicular to the field is $e = vBl$, because the magnetic force moves the electrons of the rod to one end.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: a shake-powered torch on a table. Inside the transparent body is a cylindrical magnet, and in the middle of the body is a copper coil. When the torch is shaken, the magnet slides back and forth through the coil, and the LED at the front of the torch shines." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy75s-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy75s-led" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078"/><stop offset="0.55" stop-color="#e8590c" stop-opacity="0.8"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="#f6f1e6"/>
  <rect x="0" y="270" width="600" height="90" fill="url(#fy75s-desk)"/>
  <line x1="0" y1="270" x2="600" y2="270" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <rect x="90" y="150" width="380" height="90" rx="40" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="470" y="160" width="50" height="70" rx="10" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="536" cy="195" r="34" fill="url(#fy75s-led)"/>
  <circle cx="524" cy="195" r="10" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="250" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="260" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="270" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="280" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="290" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="300" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="310" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="320" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <ellipse cx="330" cy="195" rx="6" ry="47" fill="none" stroke="#b8622d" stroke-width="4"/>
  <rect x="150" y="175" width="50" height="40" rx="4" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="200" y="175" width="50" height="40" rx="4" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M150,128 H250" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M142,128 l14,-8 v16 Z" fill="#6b7480" stroke-linejoin="round"/>
  <path d="M258,128 l-14,-8 v16 Z" fill="#6b7480" stroke-linejoin="round"/>
  <path d="M150,262 H250" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M142,262 l14,-8 v16 Z" fill="#6b7480" stroke-linejoin="round"/>
  <path d="M258,262 l-14,-8 v16 Z" fill="#6b7480" stroke-linejoin="round"/>
</svg>
