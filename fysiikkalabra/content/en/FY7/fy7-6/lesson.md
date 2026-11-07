# Lenz's law and eddy currents

> **Why** does a strong magnet take several seconds to fall through a copper tube, although copper is not magnetic and an ordinary object falls the same distance in less than a second?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a laboratory bench a vertical copper tube stands in a stand, with a transparent plastic tube beside it. A small magnet is just emerging from the lower end of the copper tube above a soft pad. On the bench is a stopwatch showing that several seconds have passed." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy76h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy76h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy76h-rod" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy76h-cu" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b8622d"/><stop offset="1" stop-color="#8a5f22"/></linearGradient><linearGradient id="fy76h-pl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy76h-desk)"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <rect x="90" y="70" width="220" height="250" rx="6" fill="url(#fy76h-sky)" stroke="#1f2933" stroke-width="3"/>
  <line x1="200" y1="70" x2="200" y2="320" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="90" y1="195" x2="310" y2="195" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="470" y="448" width="200" height="22" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="500" y="50" width="16" height="400" rx="3" fill="url(#fy76h-rod)" stroke="#1f2933" stroke-width="3"/>
  <rect x="508" y="90" width="110" height="14" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="612" y="82" width="30" height="30" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="508" y="330" width="110" height="14" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="612" y="322" width="30" height="30" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="600" y="40" width="56" height="350" rx="4" fill="url(#fy76h-cu)" stroke="#1f2933" stroke-width="3"/>
  <ellipse cx="628" cy="40" rx="28" ry="8" fill="#8a5f22" stroke="#1f2933" stroke-width="3"/>
  <rect x="611" y="392" width="34" height="30" rx="4" fill="#f2a69c" stroke="#1f2933" stroke-width="3"/>
  <rect x="611" y="372" width="34" height="22" rx="4" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/>
  <rect x="586" y="452" width="84" height="18" rx="8" fill="#f2a69c" stroke="#1f2933" stroke-width="3"/>
  <line x1="614" y1="432" x2="614" y2="444" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="628" y1="432" x2="628" y2="444" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="642" y1="432" x2="642" y2="444" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <rect x="760" y="120" width="44" height="350" rx="4" fill="url(#fy76h-pl)" stroke="#1f2933" stroke-width="3" fill-opacity="0.75"/>
  <ellipse cx="782" cy="120" rx="22" ry="7" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="950" y="318" width="20" height="15" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="955.5" y="332" width="8.5" height="8.5" fill="#6c757d"/>
  <circle cx="960" cy="400" r="62" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="960" cy="400" r="50.84" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="960" y1="358" x2="960" y2="351.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="981" y1="363.5" x2="984" y2="358" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="996.5" y1="379" x2="1002" y2="376" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1002" y1="400" x2="1008.5" y2="400" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="996.5" y1="421" x2="1002" y2="424" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="981" y1="436.5" x2="984" y2="442" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="442" x2="960" y2="448.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="939" y1="436.5" x2="936" y2="442" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="923.5" y1="421" x2="918" y2="424" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="918" y1="400" x2="911.5" y2="400" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="923.5" y1="379" x2="918" y2="376" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="939" y1="363.5" x2="936" y2="358" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="400" x2="932" y2="430" stroke="#c92a2a" stroke-width="4.34" stroke-linecap="round"/>
  <circle cx="960" cy="400" r="4.96" fill="#1f2933"/>
  <ellipse cx="628" cy="352" rx="32" ry="7" fill="none" stroke="#7048e8" stroke-width="3" stroke-opacity="0.55"/>
  <ellipse cx="628" cy="382" rx="32" ry="7" fill="none" stroke="#7048e8" stroke-width="3" stroke-opacity="0.55"/>
</svg>

## Key idea

### The induced current opposes the change
In the chapter *Electromagnetic induction*, an induced current appeared in a closed conducting loop whenever the magnetic flux through the loop changed. The direction of the current follows one rule, **Lenz's law**: *the direction of the induced current is always such that its own magnetic field opposes the change that induces the current.* When the north pole of a magnet is pushed towards a copper ring, the flux through the ring increases. The induced current in the ring turns the ring into a small magnet whose side facing the magnet is a north pole, so the ring repels the approaching magnet. When the magnet is pulled away, the flux decreases. Now the current circulates in the other direction, the side of the ring facing the magnet is a south pole, and the ring attracts the magnet back. In both cases the force of the ring opposes the motion of the magnet.

<svg data-fig="ring" viewBox="0 0 600 360" role="img" aria-label="Two schematic diagrams, not to scale. The copper ring is cut in the plane of the paper, so the cross-sections of its upper and lower edges are visible. On the left a magnet moves towards the ring, north pole first. The induced current in the ring flows into the paper in the upper edge and out of the paper in the lower edge, and its magnetic field at the centre of the ring points to the left, towards the magnet: the side of the ring facing the magnet is a north pole, and the ring repels the magnet. The force on the magnet points to the left, against the motion. On the right the magnet moves away from the ring. The current is in the opposite direction, the field of the ring points to the right, the side facing the magnet is a south pole, and the ring attracts the magnet back. The force points to the right, again against the motion." style="max-width:100%;font-size:24px">
  <foreignObject x="30" y="13.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magnet approaching}$</div></foreignObject>
  <foreignObject x="330" y="13.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magnet moving away}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="340" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="26" y="162" width="56" height="40" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="82" y="162" width="56" height="40" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="44" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="100" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <ellipse cx="222" cy="182" rx="16" ry="70" fill="none" stroke="#b8622d" stroke-width="5"/>
  <circle cx="222" cy="112" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="215.5" y1="105.5" x2="228.5" y2="118.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="228.5" y1="105.5" x2="215.5" y2="118.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="222" cy="252" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="222" cy="252" r="3.84" fill="#7048e8"/>
  <foreignObject x="240" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="250" y1="182" x2="200" y2="182" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M188,182 L201,176 L201,188 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="145" y="197.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="172" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <line x1="56" y1="140" x2="106" y2="140" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M118,140 L105,146 L105,134 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="124" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="76" y1="226" x2="32" y2="226" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M20,226 L33,220 L33,232 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="82" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="65" y="315.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ring repels}$</div></foreignObject>
  <rect x="326" y="162" width="56" height="40" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="382" y="162" width="56" height="40" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="344" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="400" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <ellipse cx="522" cy="182" rx="16" ry="70" fill="none" stroke="#b8622d" stroke-width="5"/>
  <circle cx="522" cy="112" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="522" cy="112" r="3.84" fill="#7048e8"/>
  <circle cx="522" cy="252" r="12" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="515.5" y1="245.5" x2="528.5" y2="258.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="528.5" y1="245.5" x2="515.5" y2="258.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="540" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="488" y1="182" x2="538" y2="182" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M550,182 L537,188 L537,176 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="445" y="197.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="472" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <line x1="408" y1="140" x2="358" y2="140" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M346,140 L359,134 L359,146 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="414" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="382" y1="226" x2="426" y2="226" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M438,226 L425,232 L425,220 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="343" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="365" y="315.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ring attracts}$</div></foreignObject>
</svg>

### Lenz's law is conservation of energy
Why could the induced current not help the change? If an approaching magnet pulled the ring towards itself, the magnet would accelerate towards the ring, the flux would change ever faster, the induced current would grow and the pull would strengthen. The kinetic energy of the magnet and the electrical energy of the ring would both increase without anyone doing work: a perpetual motion machine would produce energy from nothing. Conservation of energy rules this out. So the magnet has to be moved by a force that does work against the opposing force of the ring, and this work is what is converted into the electrical energy of the induced current. The current heats the conductor, so the energy ends up as internal energy of the conductor.

### Eddy currents
An induced current does not need a separate conducting loop. When the magnetic flux changes in a solid piece of metal, such as a plate or the wall of a tube, closed current loops, **eddy currents**, appear in the metal. In a copper tube, the flux through the wall below a falling magnet increases and above it decreases. By Lenz's law the eddy current below repels the magnet and the one above attracts it, so both brake the fall. The eddy currents are the greater, the faster the magnet moves, so the braking force also grows with the speed. When the braking force has grown equal to the weight of the magnet, the net force is zero and the magnet falls at a steady speed. No currents appear in a plastic tube, because plastic does not conduct electricity, and a copper tube does not brake a non-magnetised steel object, because its motion does not change the flux through the tube.

<svg data-fig="tube" viewBox="0 0 600 380" role="img" aria-label="Schematic diagram, not to scale. On the left, a vertical copper tube cut lengthwise, with a magnet falling inside it, north pole downwards. Below the magnet an eddy current circulates in the wall of the tube; it flows into the paper in the right wall and out of the paper in the left wall, and its field points upwards, towards the magnet. Above the magnet the eddy current circulates in the opposite direction, and its field points downwards. The weight acts on the magnet downwards and an equally large braking force upwards, and its velocity points downwards. On the right, the lower eddy-current ring seen from above: the current circulates anticlockwise, and at the centre of the ring the field points towards the viewer, that is, upwards." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy76t-back" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b8622d"/><stop offset="1" stop-color="#8a5f22"/></linearGradient></defs>
  <rect x="114" y="24" width="72" height="332" fill="url(#fy76t-back)" fill-opacity="0.3"/>
  <rect x="104" y="24" width="10" height="332" rx="2" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <rect x="186" y="24" width="10" height="332" rx="2" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <rect x="127" y="152" width="46" height="38" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="127" y="190" width="46" height="38" rx="3" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="140" y="156.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="140" y="194.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <circle cx="191" cy="272" r="11" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="185" y1="266" x2="197" y2="278" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="197" y1="266" x2="185" y2="278" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="109" cy="272" r="11" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="109" cy="272" r="3.52" fill="#7048e8"/>
  <circle cx="191" cy="108" r="11" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="191" cy="108" r="3.52" fill="#7048e8"/>
  <circle cx="109" cy="108" r="11" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="103" y1="102" x2="115" y2="114" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="115" y1="102" x2="103" y2="114" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="294" x2="150" y2="263" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M150,252 L155.5,264 L144.5,264 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="150" y1="86" x2="150" y2="117" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M150,128 L144.5,116 L155.5,116 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="70" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="70" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="12" y="287.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <line x1="70" y1="294" x2="142" y2="276" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="222" y1="190" x2="222" y2="256" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M222,268 L216,255 L228,255 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="232" y="241.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="222" y1="190" x2="222" y2="124" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M222,112 L228,125 L216,125 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="232" y="109.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{j}$</div></foreignObject>
  <line x1="286" y1="160" x2="286" y2="208" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M286,220 L280,207 L292,207 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="296" y="197.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="330" y1="24" x2="330" y2="356" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <circle cx="466" cy="196" r="74" fill="none" stroke="#b8622d" stroke-width="9"/>
  <path d="M513,277.5 A94,94 0 1 0 377.5,228" fill="none" stroke="#7048e8" stroke-width="3" stroke-linejoin="round"/>
  <path d="M373,216 L385.5,229.5 L372.5,234.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="544" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <circle cx="466" cy="196" r="15" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.5"/>
  <circle cx="466" cy="196" r="4.8" fill="#2b8a3e"/>
  <foreignObject x="436" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="341" y="31.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lower ring from above}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/eddy-current-brake.webp" alt="A grey axle with a large round metal disc around it; next to the disc is a box-like brake unit with cables and connectors."><figcaption>An eddy current brake on a train. Next to a metal disc that turns with the axle there are electromagnets. When the brake is applied, the magnetic field induces eddy currents in the disc, which by Lenz's law oppose the rotation. Kinetic energy turns into internal energy of the disc without brake pads wearing out.</figcaption></figure>

### The eddy-current brake, the induction hob and the metal detector
In an **induction brake**, or eddy-current brake, a metal plate or rail moves in a magnetic field, and the eddy currents brake the motion. Copper or aluminium plates fixed under a roller-coaster car pass between strong magnets on the track, and in trains the electromagnets of the brake are close to the rail. The brake does not wear out, because nothing rubs, and it brakes the more strongly, the greater the speed. Near standstill the braking weakens, so a conventional brake is needed for the final stop. In an induction hob, the alternating current in a coil under the glass changes the magnetic field tens of thousands of times a second, and eddy currents heat the base of the pan. Glass does not conduct electricity, so it warms up only because of the hot pan. The coil of a metal detector produces an alternating field, and the field of the eddy currents in a piece of metal in the ground is detected in the coil of the detector.

### When eddy currents are a nuisance
Eddy currents always convert electrical energy into internal energy. In the iron core of a transformer or an electric motor, the magnetic field varies continuously, and in a solid core large eddy currents would circulate, heating the core and wasting energy. So the core is built from thin laminations with a non-conducting insulating layer between them. The eddy currents can circulate only inside each narrow lamination, so they stay small. The transformer is discussed further in the chapter *The transformer and the transmission of electrical energy*. The same idea shows in a copper tube with a lengthwise slit sawn in it: the slit cuts the currents that circulate around the tube, and the magnet falls much faster. Smaller eddy currents still circulate in the wall around the slit, so the braking does not disappear completely.

<svg data-fig="core" viewBox="0 0 600 340" role="img" aria-label="Two schematic diagrams of the cross-section of the iron core of a transformer, not to scale. The alternating magnetic field points along the core into the paper, shown by the green crosses. On the left a solid iron core: one large eddy-current loop circulates around the whole cross-section. On the right the core is built from thin laminations with an insulating layer between them: the eddy currents circulate only inside each narrow lamination, as small and weak loops." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy76c-iron" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy76c-sheet0" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy76c-sheet1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy76c-sheet2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy76c-sheet3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy76c-sheet4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient></defs>
  <foreignObject x="40" y="13.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{solid core}$</div></foreignObject>
  <foreignObject x="325" y="13.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{laminated core}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="330" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="50" y="86" width="200" height="194" rx="4" fill="url(#fy76c-iron)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="93" y1="127.5" x2="107" y2="141.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="107" y1="127.5" x2="93" y2="141.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="93" y1="176" x2="107" y2="190" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="107" y1="176" x2="93" y2="190" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="93" y1="224.5" x2="107" y2="238.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="107" y1="224.5" x2="93" y2="238.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="143" y1="127.5" x2="157" y2="141.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="157" y1="127.5" x2="143" y2="141.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="143" y1="176" x2="157" y2="190" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="157" y1="176" x2="143" y2="190" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="143" y1="224.5" x2="157" y2="238.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="157" y1="224.5" x2="143" y2="238.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="193" y1="127.5" x2="207" y2="141.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="207" y1="127.5" x2="193" y2="141.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="193" y1="176" x2="207" y2="190" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="207" y1="176" x2="193" y2="190" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="193" y1="224.5" x2="207" y2="238.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="207" y1="224.5" x2="193" y2="238.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="68" y="104" width="164" height="158" rx="22" fill="none" stroke="#7048e8" stroke-width="3.5"/>
  <path d="M144,104 l14,-7 v14 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="50" y="295.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{large eddy current}$</div></foreignObject>
  <rect x="350" y="86" width="32" height="194" rx="2" fill="url(#fy76c-sheet0)" stroke="#1f2933" stroke-width="2"/>
  <rect x="357" y="102" width="18" height="162" rx="8" fill="none" stroke="#7048e8" stroke-width="2"/>
  <rect x="382" y="86" width="10" height="194" fill="#f1dfb5" stroke="#1f2933" stroke-width="1"/>
  <rect x="392" y="86" width="32" height="194" rx="2" fill="url(#fy76c-sheet1)" stroke="#1f2933" stroke-width="2"/>
  <rect x="399" y="102" width="18" height="162" rx="8" fill="none" stroke="#7048e8" stroke-width="2"/>
  <rect x="424" y="86" width="10" height="194" fill="#f1dfb5" stroke="#1f2933" stroke-width="1"/>
  <rect x="434" y="86" width="32" height="194" rx="2" fill="url(#fy76c-sheet2)" stroke="#1f2933" stroke-width="2"/>
  <rect x="441" y="102" width="18" height="162" rx="8" fill="none" stroke="#7048e8" stroke-width="2"/>
  <rect x="466" y="86" width="10" height="194" fill="#f1dfb5" stroke="#1f2933" stroke-width="1"/>
  <rect x="476" y="86" width="32" height="194" rx="2" fill="url(#fy76c-sheet3)" stroke="#1f2933" stroke-width="2"/>
  <rect x="483" y="102" width="18" height="162" rx="8" fill="none" stroke="#7048e8" stroke-width="2"/>
  <rect x="508" y="86" width="10" height="194" fill="#f1dfb5" stroke="#1f2933" stroke-width="1"/>
  <rect x="518" y="86" width="32" height="194" rx="2" fill="url(#fy76c-sheet4)" stroke="#1f2933" stroke-width="2"/>
  <rect x="525" y="102" width="18" height="162" rx="8" fill="none" stroke="#7048e8" stroke-width="2"/>
  <line x1="362" y1="130.5" x2="370" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370" y1="130.5" x2="362" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="362" y1="179" x2="370" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370" y1="179" x2="362" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="362" y1="227.5" x2="370" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370" y1="227.5" x2="362" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="404" y1="130.5" x2="412" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="412" y1="130.5" x2="404" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="404" y1="179" x2="412" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="412" y1="179" x2="404" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="404" y1="227.5" x2="412" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="412" y1="227.5" x2="404" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="446" y1="130.5" x2="454" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="454" y1="130.5" x2="446" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="446" y1="179" x2="454" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="454" y1="179" x2="446" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="446" y1="227.5" x2="454" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="454" y1="227.5" x2="446" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="488" y1="130.5" x2="496" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="496" y1="130.5" x2="488" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="488" y1="179" x2="496" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="496" y1="179" x2="488" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="488" y1="227.5" x2="496" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="496" y1="227.5" x2="488" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="530" y1="130.5" x2="538" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="538" y1="130.5" x2="530" y2="138.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="530" y1="179" x2="538" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="538" y1="179" x2="530" y2="187" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="530" y1="227.5" x2="538" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="538" y1="227.5" x2="530" y2="235.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="355" y="295.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{insulated laminations}$</div></foreignObject>
  <foreignObject x="365" y="49.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}\ \text{into the page}$</div></foreignObject>
</svg>

## Formula: Lenz's law and energy
The minus sign in the law of induction from the chapter *Electromagnetic induction* is Lenz's law:
```latex
e_\text{ka} = -N \frac{\Delta \Phi}{\Delta t}
```
where $e_\text{ka}$ is the average induced voltage (V) in the time interval $\Delta t$, $N$ the number of turns of the loop, $\Delta\Phi$ the change in magnetic flux (Wb) and $\Delta t$ the time taken by the change (s). When the flux changes steadily, the voltage is constant, and it is written simply $e$. The minus sign tells us that the field of the induced current opposes the change in flux. The magnitude is calculated without the sign, and the direction is deduced from Lenz's law.

Conservation of energy tells us where the energy of a falling magnet goes. When the magnet falls a height $h$, its potential energy decreases by $mgh$. Part of it is converted into kinetic energy, and the rest, through the eddy currents, into internal energy $Q$ of the tube:
```latex
\begin{aligned}
&mgh = \tfrac{1}{2} m v^2 + Q \\
&Q = mgh - \tfrac{1}{2} m v^2
\end{aligned}
```
where $m$ is the mass of the magnet (kg), $g = 9.81\,\text{m/s}^2$, $h$ the height of the fall (m), $v$ the speed at the end (m/s) and $Q$ the energy converted into internal energy (J). When the magnet falls at a steady speed, the braking force $F$ equals the weight $mg$. During a time $\Delta t$ the force acts over a distance $v \Delta t$ and does work $F v \Delta t$, so the internal energy increases at the rate
```latex
P = F v
```
where $P$ is the power (W), $F$ the braking force (N) and $v$ the speed (m/s). The same formula holds for every eddy-current brake: the braking force times the speed is the power at which kinetic energy is converted into internal energy.

<svg data-fig="energy" viewBox="0 0 600 360" role="img" aria-label="Bar chart to scale: the energies when a 20 g magnet has fallen through a tube one metre long. In the plastic tube the decrease of 196 mJ in potential energy has been converted entirely into kinetic energy, and no internal energy is produced. In the copper tube the potential energy decreases by the same amount, but the kinetic energy is only 0.2 mJ, so little that the bar cannot be seen, and almost all of it, 196 mJ, has been converted into internal energy of the tube." style="max-width:100%;font-size:24px">
  <line x1="100" y1="227.5" x2="560" y2="227.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="175" x2="560" y2="175" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="122.5" x2="560" y2="122.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="70" x2="560" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="280" x2="574" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M586,280 L573,286 L573,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="281" x2="100" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,44 L106,57 L94,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="93" y1="227.5" x2="100" y2="227.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="213" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="93" y1="175" x2="100" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="160.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="122.5" x2="100" y2="122.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="108" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="93" y1="70" x2="100" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="70" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="90" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{mJ})$</div></foreignObject>
  <rect x="139.5" y="74" width="46" height="206" fill="#6b7480"/>
  <foreignObject x="140" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta E_\text{p}$</div></foreignObject>
  <rect x="198.5" y="74" width="46" height="206" fill="#1971c2"/>
  <foreignObject x="205" y="287.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
  <foreignObject x="270.5" y="287.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="146.5" y="327.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{plastic tube}$</div></foreignObject>
  <rect x="363" y="74" width="46" height="206" fill="#6b7480"/>
  <foreignObject x="363.5" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta E_\text{p}$</div></foreignObject>
  <foreignObject x="428.5" y="287.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
  <rect x="481" y="74" width="46" height="206" fill="#e8590c"/>
  <foreignObject x="494" y="287.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="370" y="327.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{copper tube}$</div></foreignObject>
  <line x1="445" y1="276" x2="445" y2="217" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <foreignObject x="403.5" y="192" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0.2\,\text{mJ}$</span></div></foreignObject>
</svg>

## Worked example
A student drops a $25\,\text{g}$ neodymium magnet into a vertical copper tube $1.20\,\text{m}$ long and measures that the magnet emerges from the lower end of the tube after $8.0\,\text{s}$. The magnet falls at a steady speed for almost the whole distance. By how much does the internal energy of the tube increase during the fall?

<!-- vaihe -->

**Given and find.** The mass of the magnet is $m = 25\,\text{g}$, the length of the tube, which is the height of the fall, is $h = 1.20\,\text{m}$, the falling time is $t = 8.0\,\text{s}$ and $g = 9.81\,\text{m/s}^2$. We are asked for the increase $Q$ in the internal energy of the tube.

<!-- vaihe -->

**Principle.** Energy is conserved: the eddy currents convert the part of the decrease in potential energy that does not remain as kinetic energy of the magnet into internal energy of the tube. Air resistance is negligible at such a low speed. The speed is almost the same over the whole distance, so it is obtained from the distance and the time.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&v = \frac{h}{t} \\
&Q = mgh - \tfrac{1}{2} m v^2
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The mass in kilograms: $m = 25\,\text{g} = 25 \cdot 0.001\,\text{kg} = 0.025\,\text{kg}$. The other quantities are in SI units.

<!-- vaihe -->

**Substitution.** First calculate the speed and then the energy:
```latex
\begin{aligned}
&v = \frac{h}{t} \\
&= \frac{1.20\,\text{m}}{8.0\,\text{s}} \\
&= 0.15\,\text{m/s} \\[6pt]
&Q = mgh - \tfrac{1}{2} m v^2 \\
&= 0.025\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 1.20\,\text{m} \\
&\quad - \tfrac{1}{2} \cdot 0.025\,\text{kg} \cdot (0.15\,\text{m/s})^2 \\
&= 0.29430\,\text{J} - 0.00028\,\text{J} \\
&= 0.29402\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The internal energy of the tube increases by about $0.29\,\text{J}$. The result is given to two significant figures, like the mass $25\,\text{g}$ and the time $8.0\,\text{s}$.

<!-- vaihe -->

**Reasonableness.** Only about $0.1\,\%$ of the decrease in potential energy remains as kinetic energy, so almost all the energy heats the tube, as it should in a steady fall. If the mass of the tube is $0.30\,\text{kg}$, the specific heat capacity of copper, $385\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, gives a temperature rise of only about $0.003\,\text{K}$: that is why the tube does not feel warm.

## Common misconception
Many people think that a copper tube slows the magnet because the magnet sticks to the copper. But copper is not a ferromagnetic material: a magnet at rest does not stick to the wall of a copper tube, and the tube does not brake a non-magnetised steel object of the same shape at all. The braking arises only from motion, because only a moving magnet changes the flux through the tube. Another common mistake is to say that the field of the induced current is always opposite to the field of the magnet. Lenz's law does not oppose the field but its **change**. When a magnet moves away from a ring, the flux through the ring decreases, and the field of the induced current at the centre of the ring points in the same direction as the field of the magnet, so the ring attracts the magnet.

## Summary
- Lenz's law: the magnetic field of the induced current opposes the change that induces the current. A ring repels an approaching magnet and attracts one that is moving away.
- Lenz's law follows from conservation of energy. The work done in moving the magnet is converted into the electrical energy of the induced current and further into internal energy of the conductor: $Q = mgh - \tfrac{1}{2} m v^2$.
- In a changing magnetic field, eddy currents appear in a piece of metal. They brake motion the more strongly, the greater the speed, and the power of the braking is $P = F v$.
- Eddy currents are used in the induction brake, the induction hob and the metal detector. The iron core of a transformer or a motor is built from insulated laminations so that the eddy currents and their energy loss stay small.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Illustration: an induction hob with a steel pan on its glass surface. Water is boiling in the pan and steam is rising from it. Under the glass surface a copper coil is shown in cross-section. There is no flame or glowing plate." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy76s-bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy76s-pot" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="#f6f1e6"/>
  <rect x="0" y="250" width="600" height="110" fill="url(#fy76s-bench)"/>
  <rect x="70" y="226" width="460" height="26" rx="6" fill="#1f2933"/>
  <rect x="70" y="252" width="460" height="60" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="210" y="262" width="18" height="12" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="236" y="262" width="18" height="12" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="262" y="262" width="18" height="12" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="288" y="262" width="18" height="12" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="314" y="262" width="18" height="12" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="340" y="262" width="18" height="12" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="366" y="262" width="18" height="12" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="480" cy="239" r="6" fill="#e8590c"/>
  <path d="M190,226 L196,130 L404,130 L410,226 Z" fill="url(#fy76s-pot)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="184" y="122" width="232" height="12" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="150" y="140" width="40" height="12" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="410" y="140" width="40" height="12" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="300" cy="134" rx="104" ry="9" fill="#a9d1f0" stroke="#1f2933" stroke-width="2"/>
  <path d="M250,112 c-14,-16 14,-30 0,-46 c-14,-16 14,-30 0,-46" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M300,112 c-14,-16 14,-30 0,-46 c-14,-16 14,-30 0,-46" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M350,112 c-14,-16 14,-30 0,-46 c-14,-16 14,-30 0,-46" fill="none" stroke="#6b7480" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <ellipse cx="300" cy="219" rx="80" ry="5" fill="none" stroke="#7048e8" stroke-width="3" stroke-opacity="0.6"/>
</svg>
