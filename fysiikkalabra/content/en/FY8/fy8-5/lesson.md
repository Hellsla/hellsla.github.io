# The wave-mechanical model of the atom and orbitals

> **Why** is the electron of an atom drawn in a chemistry book as a fuzzy cloud and not as a small ball going round the nucleus along an orbit?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an open book lies on a desk. On the left page is an old picture of an atom in which a small electron goes round the nucleus along a circular orbit. On the right page the same atom is drawn as a blue cloud of dots, and next to it is a two-lobed p orbital. A desk lamp lights the book." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy85h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6f1e6"/><stop offset="1" stop-color="#f1dfb5"/></linearGradient><linearGradient id="fy85h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><radialGradient id="fy85h-light" cx="0.5" cy="0" r="0.9"><stop offset="0" stop-color="#ffc078" stop-opacity="0.55"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient><radialGradient id="fy85h-cloud"><stop offset="0" stop-color="#1971c2" stop-opacity="0.85"/><stop offset="1" stop-color="#1971c2" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy85h-wall)"/>
  <rect x="0" y="330" width="1200" height="270" fill="url(#fy85h-desk)"/>
  <line x1="0" y1="330" x2="1200" y2="330" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <path d="M930,150 L560,560 L1140,560 Z" fill="url(#fy85h-light)" stroke-linejoin="round"/>
  <path d="M330,520 L600,540 L600,330 L360,300 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M870,520 L600,540 L600,330 L840,300 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M342,508 L600,528 L600,318 L370,290 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M858,508 L600,528 L600,318 L830,290 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M596,320 L604,320 L604,528 L596,528 Z" fill="#c9c2b2" stroke-linejoin="round"/>
  <ellipse cx="478" cy="410" rx="88" ry="64" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="478" cy="410" r="13" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="560" cy="384" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="682" cy="408" r="78" fill="url(#fy85h-cloud)"/>
  <circle cx="674" cy="421.5" r="3" fill="#1971c2"/>
  <circle cx="678" cy="419.5" r="3" fill="#1971c2"/>
  <circle cx="686" cy="403.5" r="3" fill="#1971c2"/>
  <circle cx="649" cy="401.5" r="3" fill="#1971c2"/>
  <circle cx="714" cy="432" r="3" fill="#1971c2"/>
  <circle cx="667.5" cy="422" r="3" fill="#1971c2"/>
  <circle cx="692.5" cy="428" r="3" fill="#1971c2"/>
  <circle cx="666.5" cy="415" r="3" fill="#1971c2"/>
  <circle cx="683" cy="398" r="3" fill="#1971c2"/>
  <circle cx="674.5" cy="391" r="3" fill="#1971c2"/>
  <circle cx="704.5" cy="384.5" r="3" fill="#1971c2"/>
  <circle cx="668" cy="398.5" r="3" fill="#1971c2"/>
  <circle cx="650.5" cy="401" r="3" fill="#1971c2"/>
  <circle cx="654.5" cy="411" r="3" fill="#1971c2"/>
  <circle cx="683.5" cy="385" r="3" fill="#1971c2"/>
  <circle cx="676.5" cy="426.5" r="3" fill="#1971c2"/>
  <circle cx="684" cy="406" r="3" fill="#1971c2"/>
  <circle cx="667.5" cy="432" r="3" fill="#1971c2"/>
  <circle cx="676.5" cy="374" r="3" fill="#1971c2"/>
  <circle cx="689.5" cy="379.5" r="3" fill="#1971c2"/>
  <circle cx="676" cy="408" r="3" fill="#1971c2"/>
  <circle cx="674.5" cy="410" r="3" fill="#1971c2"/>
  <circle cx="660.5" cy="396.5" r="3" fill="#1971c2"/>
  <circle cx="689.5" cy="379" r="3" fill="#1971c2"/>
  <circle cx="692" cy="405" r="3" fill="#1971c2"/>
  <circle cx="686.5" cy="409.5" r="3" fill="#1971c2"/>
  <circle cx="684.5" cy="408.5" r="3" fill="#1971c2"/>
  <circle cx="666" cy="424" r="3" fill="#1971c2"/>
  <circle cx="678" cy="383.5" r="3" fill="#1971c2"/>
  <circle cx="681" cy="410.5" r="3" fill="#1971c2"/>
  <circle cx="673.5" cy="390.5" r="3" fill="#1971c2"/>
  <circle cx="691.5" cy="407.5" r="3" fill="#1971c2"/>
  <circle cx="698.5" cy="417.5" r="3" fill="#1971c2"/>
  <circle cx="688" cy="421" r="3" fill="#1971c2"/>
  <circle cx="704" cy="414.5" r="3" fill="#1971c2"/>
  <circle cx="688" cy="405.5" r="3" fill="#1971c2"/>
  <circle cx="678" cy="412.5" r="3" fill="#1971c2"/>
  <circle cx="696" cy="393.5" r="3" fill="#1971c2"/>
  <circle cx="682" cy="388" r="3" fill="#1971c2"/>
  <circle cx="689" cy="416" r="3" fill="#1971c2"/>
  <circle cx="679" cy="367" r="3" fill="#1971c2"/>
  <circle cx="683" cy="404" r="3" fill="#1971c2"/>
  <circle cx="649.5" cy="389.5" r="3" fill="#1971c2"/>
  <circle cx="680" cy="399" r="3" fill="#1971c2"/>
  <circle cx="694.5" cy="378" r="3" fill="#1971c2"/>
  <circle cx="675.5" cy="412.5" r="3" fill="#1971c2"/>
  <circle cx="678.5" cy="400" r="3" fill="#1971c2"/>
  <circle cx="715" cy="414" r="3" fill="#1971c2"/>
  <circle cx="676.5" cy="429" r="3" fill="#1971c2"/>
  <circle cx="668.5" cy="420" r="3" fill="#1971c2"/>
  <circle cx="658.5" cy="407" r="3" fill="#1971c2"/>
  <circle cx="678.5" cy="420.5" r="3" fill="#1971c2"/>
  <circle cx="704" cy="392.5" r="3" fill="#1971c2"/>
  <circle cx="674" cy="407.5" r="3" fill="#1971c2"/>
  <circle cx="679" cy="390" r="3" fill="#1971c2"/>
  <circle cx="731" cy="402" r="3" fill="#1971c2"/>
  <circle cx="701" cy="410.5" r="3" fill="#1971c2"/>
  <circle cx="691.5" cy="399.5" r="3" fill="#1971c2"/>
  <circle cx="695" cy="426" r="3" fill="#1971c2"/>
  <circle cx="616.5" cy="421.5" r="3" fill="#1971c2"/>
  <circle cx="617.5" cy="417" r="3" fill="#1971c2"/>
  <circle cx="691" cy="403.5" r="3" fill="#1971c2"/>
  <circle cx="672.5" cy="412.5" r="3" fill="#1971c2"/>
  <circle cx="722" cy="379" r="3" fill="#1971c2"/>
  <circle cx="681.5" cy="405.5" r="3" fill="#1971c2"/>
  <circle cx="680.5" cy="388" r="3" fill="#1971c2"/>
  <circle cx="709.5" cy="394" r="3" fill="#1971c2"/>
  <circle cx="690.5" cy="423" r="3" fill="#1971c2"/>
  <circle cx="699.5" cy="388.5" r="3" fill="#1971c2"/>
  <circle cx="709" cy="405" r="3" fill="#1971c2"/>
  <circle cx="690" cy="414.5" r="3" fill="#1971c2"/>
  <circle cx="680.5" cy="409.5" r="3" fill="#1971c2"/>
  <circle cx="671" cy="424" r="3" fill="#1971c2"/>
  <circle cx="679.5" cy="406.5" r="3" fill="#1971c2"/>
  <circle cx="691.5" cy="436" r="3" fill="#1971c2"/>
  <circle cx="652" cy="414.5" r="3" fill="#1971c2"/>
  <circle cx="670.5" cy="370.5" r="3" fill="#1971c2"/>
  <circle cx="688" cy="425.5" r="3" fill="#1971c2"/>
  <circle cx="693" cy="419.5" r="3" fill="#1971c2"/>
  <circle cx="684" cy="430" r="3" fill="#1971c2"/>
  <circle cx="681" cy="409" r="3" fill="#1971c2"/>
  <circle cx="674" cy="410" r="3" fill="#1971c2"/>
  <circle cx="682" cy="424" r="3" fill="#1971c2"/>
  <circle cx="681.5" cy="414" r="3" fill="#1971c2"/>
  <circle cx="673" cy="398.5" r="3" fill="#1971c2"/>
  <circle cx="718" cy="421.5" r="3" fill="#1971c2"/>
  <circle cx="687" cy="430.5" r="3" fill="#1971c2"/>
  <circle cx="704.5" cy="379.5" r="3" fill="#1971c2"/>
  <circle cx="694" cy="388" r="3" fill="#1971c2"/>
  <circle cx="687" cy="391.5" r="3" fill="#1971c2"/>
  <circle cx="684" cy="413" r="3" fill="#1971c2"/>
  <circle cx="656" cy="398" r="3" fill="#1971c2"/>
  <circle cx="653" cy="408" r="3" fill="#1971c2"/>
  <circle cx="701" cy="420.5" r="3" fill="#1971c2"/>
  <circle cx="698" cy="399" r="3" fill="#1971c2"/>
  <circle cx="684" cy="401.5" r="3" fill="#1971c2"/>
  <circle cx="681.5" cy="422.5" r="3" fill="#1971c2"/>
  <circle cx="687.5" cy="433" r="3" fill="#1971c2"/>
  <circle cx="676" cy="399" r="3" fill="#1971c2"/>
  <circle cx="692" cy="423" r="3" fill="#1971c2"/>
  <circle cx="665" cy="473.5" r="3" fill="#1971c2"/>
  <circle cx="694.5" cy="434.5" r="3" fill="#1971c2"/>
  <circle cx="654.5" cy="437" r="3" fill="#1971c2"/>
  <circle cx="719" cy="407" r="3" fill="#1971c2"/>
  <circle cx="719" cy="409" r="3" fill="#1971c2"/>
  <circle cx="689.5" cy="413" r="3" fill="#1971c2"/>
  <circle cx="682" cy="434.5" r="3" fill="#1971c2"/>
  <circle cx="715.5" cy="388.5" r="3" fill="#1971c2"/>
  <circle cx="681" cy="395" r="3" fill="#1971c2"/>
  <circle cx="686.5" cy="420" r="3" fill="#1971c2"/>
  <circle cx="678" cy="432.5" r="3" fill="#1971c2"/>
  <circle cx="686.5" cy="395.5" r="3" fill="#1971c2"/>
  <circle cx="659" cy="363" r="3" fill="#1971c2"/>
  <circle cx="682.5" cy="410.5" r="3" fill="#1971c2"/>
  <circle cx="687" cy="396" r="3" fill="#1971c2"/>
  <circle cx="694.5" cy="401" r="3" fill="#1971c2"/>
  <circle cx="668.5" cy="406" r="3" fill="#1971c2"/>
  <circle cx="678.5" cy="403" r="3" fill="#1971c2"/>
  <circle cx="682.5" cy="414" r="3" fill="#1971c2"/>
  <circle cx="657.5" cy="391.5" r="3" fill="#1971c2"/>
  <circle cx="697.5" cy="413.5" r="3" fill="#1971c2"/>
  <circle cx="655.5" cy="407.5" r="3" fill="#1971c2"/>
  <circle cx="664" cy="421" r="3" fill="#1971c2"/>
  <circle cx="718.5" cy="366.5" r="3" fill="#1971c2"/>
  <circle cx="652" cy="410" r="3" fill="#1971c2"/>
  <circle cx="696.5" cy="387.5" r="3" fill="#1971c2"/>
  <circle cx="653.5" cy="435.5" r="3" fill="#1971c2"/>
  <circle cx="686.5" cy="392.5" r="3" fill="#1971c2"/>
  <circle cx="683.5" cy="400" r="3" fill="#1971c2"/>
  <circle cx="681.5" cy="437" r="3" fill="#1971c2"/>
  <circle cx="670" cy="428" r="3" fill="#1971c2"/>
  <circle cx="698" cy="404.5" r="3" fill="#1971c2"/>
  <circle cx="711.5" cy="396" r="3" fill="#1971c2"/>
  <circle cx="680.5" cy="397" r="3" fill="#1971c2"/>
  <circle cx="673" cy="404" r="3" fill="#1971c2"/>
  <circle cx="714.5" cy="430" r="3" fill="#1971c2"/>
  <circle cx="687" cy="420.5" r="3" fill="#1971c2"/>
  <circle cx="679" cy="386.5" r="3" fill="#1971c2"/>
  <circle cx="676.5" cy="396.5" r="3" fill="#1971c2"/>
  <circle cx="653.5" cy="429.5" r="3" fill="#1971c2"/>
  <circle cx="691.5" cy="417" r="3" fill="#1971c2"/>
  <circle cx="667.5" cy="442" r="3" fill="#1971c2"/>
  <circle cx="687" cy="350.5" r="3" fill="#1971c2"/>
  <circle cx="710.5" cy="391.5" r="3" fill="#1971c2"/>
  <circle cx="691.5" cy="415" r="3" fill="#1971c2"/>
  <circle cx="684" cy="401" r="3" fill="#1971c2"/>
  <circle cx="695.5" cy="382" r="3" fill="#1971c2"/>
  <circle cx="692.5" cy="411" r="3" fill="#1971c2"/>
  <circle cx="673.5" cy="435.5" r="3" fill="#1971c2"/>
  <circle cx="692.5" cy="437.5" r="3" fill="#1971c2"/>
  <circle cx="668.5" cy="374.5" r="3" fill="#1971c2"/>
  <circle cx="674" cy="429" r="3" fill="#1971c2"/>
  <circle cx="687.5" cy="404.5" r="3" fill="#1971c2"/>
  <circle cx="649.5" cy="429" r="3" fill="#1971c2"/>
  <circle cx="629.5" cy="441.5" r="3" fill="#1971c2"/>
  <circle cx="680" cy="386.5" r="3" fill="#1971c2"/>
  <circle cx="665.5" cy="422.5" r="3" fill="#1971c2"/>
  <circle cx="682.5" cy="420.5" r="3" fill="#1971c2"/>
  <circle cx="680" cy="407.5" r="3" fill="#1971c2"/>
  <circle cx="684" cy="410" r="3" fill="#1971c2"/>
  <circle cx="695" cy="395" r="3" fill="#1971c2"/>
  <circle cx="656.5" cy="420.5" r="3" fill="#1971c2"/>
  <circle cx="682.5" cy="418" r="3" fill="#1971c2"/>
  <circle cx="658.5" cy="419" r="3" fill="#1971c2"/>
  <circle cx="655.5" cy="372" r="3" fill="#1971c2"/>
  <circle cx="682" cy="408" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <path d="M796,408 L767.5,397 L765.5,394 L763.5,390.5 L762.5,387.5 L761.5,384 L761,380.5 L761,377 L761.5,373.5 L762.5,370 L764,366.5 L765.5,363.5 L767.5,360 L769.5,357.5 L772.5,355 L775,352.5 L778.5,350.5 L781.5,349 L785,347.5 L788.5,347 L792.5,346 L796,346 L799.5,346 L803.5,347 L807,347.5 L810.5,349 L813.5,350.5 L817,352.5 L819.5,355 L822.5,357.5 L824.5,360 L826.5,363.5 L828,366.5 L829.5,370 L830.5,373.5 L831,377 L831,380.5 L830.5,384 L829.5,387.5 L828.5,390.5 L826.5,394 L824.5,397 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="3" stroke-linejoin="round"/>
  <path d="M796,416 L767.5,427 L765.5,430 L763.5,433.5 L762.5,436.5 L761.5,440 L761,443.5 L761,447 L761.5,450.5 L762.5,454 L764,457.5 L765.5,460.5 L767.5,464 L769.5,466.5 L772.5,469 L775,471.5 L778.5,473.5 L781.5,475 L785,476.5 L788.5,477 L792.5,478 L796,478 L799.5,478 L803.5,477 L807,476.5 L810.5,475 L813.5,473.5 L817,471.5 L819.5,469 L822.5,466.5 L824.5,464 L826.5,460.5 L828,457.5 L829.5,454 L830.5,450.5 L831,447 L831,443.5 L830.5,440 L829.5,436.5 L828.5,433.5 L826.5,430 L824.5,427 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="796" cy="412" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <path d="M1040,560 h120 v-16 q0,-12 -12,-12 h-96 q-12,0 -12,12 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1100,532 L1060,250" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1060,250 L960,150" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M990,120 L900,190 L880,165 L960,96 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="1060" cy="250" r="10" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M250,560 L420,548 L428,556 L258,570 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M420,548 L446,552 L428,556 Z" fill="#d9b26a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M120,420 h90 v110 q0,14 -14,14 h-62 q-14,0 -14,-14 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M210,445 q34,0 34,30 q0,30 -34,30" fill="none" stroke="#1f2933" stroke-width="5" stroke-linejoin="round"/>
</svg>

## Key idea

### From an orbit to a wave
The Bohr model gave the energy levels of the hydrogen atom correctly (chapter *Energy levels of the hydrogen atom and the Bohr model*), but its picture of a small ball on a circular orbit does not stand closer examination. The model does not tell why only certain orbits are allowed, and it does not work for atoms with several electrons.

In the chapter *Light and electrons as waves and particles* we also saw that electrons sent one at a time form an interference pattern behind a double slit: the motion of an electron must be described by a wave. In the **wave-mechanical model of the atom**, the state of an electron in an atom is described by a wave that spreads around the nucleus, not by an orbit.

### The allowed states are standing waves
A guitar string is fixed at both ends, so only those standing waves arise in it in which the ends of the string are nodes. There are therefore only certain ways of vibrating: one antinode, two antinodes, three antinodes and so on. The electric attraction of the nucleus binds the electron, and its wave must likewise fit around the nucleus. Lasting states arise only for certain wave shapes, and each shape has its own energy. The quantisation of energy is thus not a separate assumption as in the Bohr model, but follows from the fact that a bound wave can only be a standing wave. In a string, an extra node raises the frequency of the vibration. In the hydrogen atom the energy of a state is greater the more nodes the wave has; in an atom with many electrons this holds for states of the same shape (s, p, …).

<svg data-fig="string" viewBox="0 0 600 330" role="img" aria-label="Schematic figure: the first three standing waves of a string fixed at both ends. In the top one the string vibrates as one antinode and there is no node in its middle, in the middle one there is one node and two antinodes, and in the bottom one two nodes and three antinodes. No other ways of vibrating arise, because the ends of the string stay in place. The more nodes, the greater the frequency of the vibration." style="max-width:100%;font-size:24px">
  <rect x="96" y="52" width="12" height="68" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="456" y="52" width="12" height="68" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M112,86 L115.5,85 L119,84 L122,83 L125.5,82 L129,81.5 L132.5,80.5 L136,79.5 L139,78.5 L142.5,77.5 L146,76.5 L149.5,76 L153,75 L156,74 L159.5,73 L163,72.5 L166.5,71.5 L170,70.5 L173,70 L176.5,69 L180,68.5 L183.5,67.5 L187,67 L190,66 L193.5,65.5 L197,65 L200.5,64 L204,63.5 L207,63 L210.5,62.5 L214,61.5 L217.5,61 L221,60.5 L224,60 L227.5,59.5 L231,59.5 L234.5,59 L238,58.5 L241,58 L244.5,58 L248,57.5 L251.5,57 L255,57 L258,56.5 L261.5,56.5 L265,56.5 L268.5,56 L272,56 L275,56 L278.5,56 L282,56 L285.5,56 L289,56 L292,56 L295.5,56 L299,56.5 L302.5,56.5 L306,56.5 L309,57 L312.5,57 L316,57.5 L319.5,58 L323,58 L326,58.5 L329.5,59 L333,59.5 L336.5,59.5 L340,60 L343,60.5 L346.5,61 L350,61.5 L353.5,62.5 L357,63 L360,63.5 L363.5,64 L367,65 L370.5,65.5 L374,66 L377,67 L380.5,67.5 L384,68.5 L387.5,69 L391,70 L394,70.5 L397.5,71.5 L401,72.5 L404.5,73 L408,74 L411,75 L414.5,76 L418,76.5 L421.5,77.5 L425,78.5 L428,79.5 L431.5,80.5 L435,81.5 L438.5,82 L442,83 L445,84 L448.5,85 L452,86" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round"/>
  <path d="M112,86 L115.5,87 L119,88 L122,89 L125.5,90 L129,90.5 L132.5,91.5 L136,92.5 L139,93.5 L142.5,94.5 L146,95.5 L149.5,96 L153,97 L156,98 L159.5,99 L163,99.5 L166.5,100.5 L170,101.5 L173,102 L176.5,103 L180,103.5 L183.5,104.5 L187,105 L190,106 L193.5,106.5 L197,107 L200.5,108 L204,108.5 L207,109 L210.5,109.5 L214,110.5 L217.5,111 L221,111.5 L224,112 L227.5,112.5 L231,112.5 L234.5,113 L238,113.5 L241,114 L244.5,114 L248,114.5 L251.5,115 L255,115 L258,115.5 L261.5,115.5 L265,115.5 L268.5,116 L272,116 L275,116 L278.5,116 L282,116 L285.5,116 L289,116 L292,116 L295.5,116 L299,115.5 L302.5,115.5 L306,115.5 L309,115 L312.5,115 L316,114.5 L319.5,114 L323,114 L326,113.5 L329.5,113 L333,112.5 L336.5,112.5 L340,112 L343,111.5 L346.5,111 L350,110.5 L353.5,109.5 L357,109 L360,108.5 L363.5,108 L367,107 L370.5,106.5 L374,106 L377,105 L380.5,104.5 L384,103.5 L387.5,103 L391,102 L394,101.5 L397.5,100.5 L401,99.5 L404.5,99 L408,98 L411,97 L414.5,96 L418,95.5 L421.5,94.5 L425,93.5 L428,92.5 L431.5,91.5 L435,90.5 L438.5,90 L442,89 L445,88 L448.5,87 L452,86" fill="none" stroke="#a9d1f0" stroke-width="3" stroke-linejoin="round" stroke-dasharray="7 5"/>
  <line x1="112" y1="86" x2="452" y2="86" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <foreignObject x="49" y="71.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.$</div></foreignObject>
  <foreignObject x="482" y="71.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{0 nodes}$</div></foreignObject>
  <rect x="96" y="152" width="12" height="68" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="456" y="152" width="12" height="68" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M112,186 L115.5,184 L119,182 L122,180.5 L125.5,178.5 L129,176.5 L132.5,175 L136,173 L139,171.5 L142.5,170 L146,168.5 L149.5,167 L153,165.5 L156,164 L159.5,163 L163,161.5 L166.5,160.5 L170,159.5 L173,159 L176.5,158 L180,157.5 L183.5,157 L187,156.5 L190,156 L193.5,156 L197,156 L200.5,156 L204,156 L207,156.5 L210.5,157 L214,157.5 L217.5,158 L221,159 L224,159.5 L227.5,160.5 L231,161.5 L234.5,163 L238,164 L241,165.5 L244.5,167 L248,168.5 L251.5,170 L255,171.5 L258,173 L261.5,175 L265,176.5 L268.5,178.5 L272,180.5 L275,182 L278.5,184 L282,186 L285.5,188 L289,190 L292,191.5 L295.5,193.5 L299,195.5 L302.5,197 L306,199 L309,200.5 L312.5,202 L316,203.5 L319.5,205 L323,206.5 L326,208 L329.5,209 L333,210.5 L336.5,211.5 L340,212.5 L343,213 L346.5,214 L350,214.5 L353.5,215 L357,215.5 L360,216 L363.5,216 L367,216 L370.5,216 L374,216 L377,215.5 L380.5,215 L384,214.5 L387.5,214 L391,213 L394,212.5 L397.5,211.5 L401,210.5 L404.5,209 L408,208 L411,206.5 L414.5,205 L418,203.5 L421.5,202 L425,200.5 L428,199 L431.5,197 L435,195.5 L438.5,193.5 L442,191.5 L445,190 L448.5,188 L452,186" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round"/>
  <path d="M112,186 L115.5,188 L119,190 L122,191.5 L125.5,193.5 L129,195.5 L132.5,197 L136,199 L139,200.5 L142.5,202 L146,203.5 L149.5,205 L153,206.5 L156,208 L159.5,209 L163,210.5 L166.5,211.5 L170,212.5 L173,213 L176.5,214 L180,214.5 L183.5,215 L187,215.5 L190,216 L193.5,216 L197,216 L200.5,216 L204,216 L207,215.5 L210.5,215 L214,214.5 L217.5,214 L221,213 L224,212.5 L227.5,211.5 L231,210.5 L234.5,209 L238,208 L241,206.5 L244.5,205 L248,203.5 L251.5,202 L255,200.5 L258,199 L261.5,197 L265,195.5 L268.5,193.5 L272,191.5 L275,190 L278.5,188 L282,186 L285.5,184 L289,182 L292,180.5 L295.5,178.5 L299,176.5 L302.5,175 L306,173 L309,171.5 L312.5,170 L316,168.5 L319.5,167 L323,165.5 L326,164 L329.5,163 L333,161.5 L336.5,160.5 L340,159.5 L343,159 L346.5,158 L350,157.5 L353.5,157 L357,156.5 L360,156 L363.5,156 L367,156 L370.5,156 L374,156 L377,156.5 L380.5,157 L384,157.5 L387.5,158 L391,159 L394,159.5 L397.5,160.5 L401,161.5 L404.5,163 L408,164 L411,165.5 L414.5,167 L418,168.5 L421.5,170 L425,171.5 L428,173 L431.5,175 L435,176.5 L438.5,178.5 L442,180.5 L445,182 L448.5,184 L452,186" fill="none" stroke="#a9d1f0" stroke-width="3" stroke-linejoin="round" stroke-dasharray="7 5"/>
  <line x1="112" y1="186" x2="452" y2="186" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <circle cx="282" cy="186" r="6" fill="#1f2933"/>
  <foreignObject x="49" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2.$</div></foreignObject>
  <foreignObject x="482" y="171.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{1 node}$</div></foreignObject>
  <rect x="96" y="252" width="12" height="68" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="456" y="252" width="12" height="68" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M112,286 L115.5,283 L119,280.5 L122,277.5 L125.5,275 L129,272.5 L132.5,270 L136,267.5 L139,265.5 L142.5,263.5 L146,261.5 L149.5,260 L153,259 L156,258 L159.5,257 L163,256.5 L166.5,256 L170,256 L173,256 L176.5,256.5 L180,257.5 L183.5,258.5 L187,259.5 L190,261 L193.5,263 L197,265 L200.5,267 L204,269 L207,271.5 L210.5,274 L214,276.5 L217.5,279.5 L221,282 L224,285 L227.5,288 L231,290.5 L234.5,293.5 L238,296 L241,299 L244.5,301.5 L248,303.5 L251.5,306 L255,308 L258,309.5 L261.5,311.5 L265,312.5 L268.5,314 L272,315 L275,315.5 L278.5,316 L282,316 L285.5,316 L289,315.5 L292,315 L295.5,314 L299,312.5 L302.5,311.5 L306,309.5 L309,308 L312.5,306 L316,303.5 L319.5,301.5 L323,299 L326,296 L329.5,293.5 L333,290.5 L336.5,288 L340,285 L343,282 L346.5,279.5 L350,276.5 L353.5,274 L357,271.5 L360,269 L363.5,267 L367,265 L370.5,263 L374,261 L377,259.5 L380.5,258.5 L384,257.5 L387.5,256.5 L391,256 L394,256 L397.5,256 L401,256.5 L404.5,257 L408,258 L411,259 L414.5,260 L418,261.5 L421.5,263.5 L425,265.5 L428,267.5 L431.5,270 L435,272.5 L438.5,275 L442,277.5 L445,280.5 L448.5,283 L452,286" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round"/>
  <path d="M112,286 L115.5,289 L119,291.5 L122,294.5 L125.5,297 L129,299.5 L132.5,302 L136,304.5 L139,306.5 L142.5,308.5 L146,310.5 L149.5,312 L153,313 L156,314 L159.5,315 L163,315.5 L166.5,316 L170,316 L173,316 L176.5,315.5 L180,314.5 L183.5,313.5 L187,312.5 L190,311 L193.5,309 L197,307 L200.5,305 L204,303 L207,300.5 L210.5,298 L214,295.5 L217.5,292.5 L221,290 L224,287 L227.5,284 L231,281.5 L234.5,278.5 L238,276 L241,273 L244.5,270.5 L248,268.5 L251.5,266 L255,264 L258,262.5 L261.5,260.5 L265,259.5 L268.5,258 L272,257 L275,256.5 L278.5,256 L282,256 L285.5,256 L289,256.5 L292,257 L295.5,258 L299,259.5 L302.5,260.5 L306,262.5 L309,264 L312.5,266 L316,268.5 L319.5,270.5 L323,273 L326,276 L329.5,278.5 L333,281.5 L336.5,284 L340,287 L343,290 L346.5,292.5 L350,295.5 L353.5,298 L357,300.5 L360,303 L363.5,305 L367,307 L370.5,309 L374,311 L377,312.5 L380.5,313.5 L384,314.5 L387.5,315.5 L391,316 L394,316 L397.5,316 L401,315.5 L404.5,315 L408,314 L411,313 L414.5,312 L418,310.5 L421.5,308.5 L425,306.5 L428,304.5 L431.5,302 L435,299.5 L438.5,297 L442,294.5 L445,291.5 L448.5,289 L452,286" fill="none" stroke="#a9d1f0" stroke-width="3" stroke-linejoin="round" stroke-dasharray="7 5"/>
  <line x1="112" y1="286" x2="452" y2="286" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <circle cx="225.5" cy="286" r="6" fill="#1f2933"/>
  <circle cx="338.5" cy="286" r="6" fill="#1f2933"/>
  <foreignObject x="49" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3.$</div></foreignObject>
  <foreignObject x="482" y="271.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{2 nodes}$</div></foreignObject>
  <foreignObject x="253" y="215.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{node}$</span></div></foreignObject>
  <line x1="282" y1="218" x2="282" y2="196" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

In an atom the wave is three-dimensional, so its nodes are surfaces, and the electron is not detected on a nodal surface. The wave of the lowest state, the $1\text{s}$ state, has no node. The states of the shell $n = 2$ have one node: in the $2\text{s}$ state it is a spherical surface around the nucleus, and in the $2\text{p}$ state a plane through the nucleus. The number in the name of the state is the principal quantum number $n$, and there are $n - 1$ nodes altogether. The letter tells the shape of the wave: an s state is spherically symmetric, and a p state has two lobes on opposite sides of the nucleus.

<svg data-fig="nodes" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale: cross-sections through the nucleus of three orbitals of the hydrogen atom. The 1s orbital is a sphere with no node. The 2s orbital is a sphere with a nodal sphere inside it: the electron is not detected there, and inside and outside it the wave oscillates in opposite phases. The 2p orbital has two lobes, one on each side of the nucleus, and between them a nodal plane through the nucleus. The figure shows one of the three 2p orbitals, with vertical lobes; the other two point in two other directions. The nucleus is a red dot." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy85-cloud"><stop offset="0" stop-color="#1971c2" stop-opacity="0.95"/><stop offset="1" stop-color="#1971c2" stop-opacity="0.12"/></radialGradient><radialGradient id="fy85-ring" r="0.5"><stop offset="0.42" stop-color="#1971c2" stop-opacity="0"/><stop offset="0.5" stop-color="#1971c2" stop-opacity="0.12"/><stop offset="0.72" stop-color="#1971c2" stop-opacity="0.55"/><stop offset="1" stop-color="#1971c2" stop-opacity="0.08"/></radialGradient></defs>
  <line x1="200" y1="30" x2="200" y2="300" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="400" y1="30" x2="400" y2="300" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <circle cx="100" cy="150" r="48" fill="url(#fy85-cloud)"/>
  <circle cx="100" cy="150" r="48" fill="none" stroke="#1971c2" stroke-width="2"/>
  <circle cx="300" cy="150" r="86" fill="url(#fy85-ring)"/>
  <circle cx="300" cy="150" r="86" fill="none" stroke="#1971c2" stroke-width="2"/>
  <circle cx="300" cy="150" r="22" fill="url(#fy85-cloud)"/>
  <circle cx="300" cy="150" r="34" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="300" cy="150" r="34" fill="none" stroke="#ffffff" stroke-width="2" stroke-dasharray="6 5"/>
  <path d="M499.5,150 L498,150 L496.5,149.5 L494.5,149 L492.5,148.5 L490,147.5 L488,146.5 L485.5,145.5 L483,144 L480.5,142.5 L478.5,140.5 L476,138.5 L474,136 L472,133.5 L470,131 L468.5,128 L467,125 L465.5,122 L464.5,119 L464,115.5 L463,112 L463,108.5 L463,105 L463,102 L463.5,98.5 L464,95 L465,92 L466.5,88.5 L468,85.5 L469.5,82.5 L471.5,80 L474,77.5 L476,75 L479,73 L481.5,71.5 L484.5,69.5 L487.5,68.5 L490.5,67.5 L493.5,66.5 L497,66 L500,66 L503,66 L506.5,66.5 L509.5,67.5 L512.5,68.5 L515.5,69.5 L518.5,71.5 L521,73 L524,75 L526,77.5 L528.5,80 L530.5,82.5 L532,85.5 L533.5,88.5 L535,92 L536,95 L536.5,98.5 L537,102 L537,105 L537,108.5 L537,112 L536,115.5 L535.5,119 L534.5,122 L533,125 L531.5,128 L530,131 L528,133.5 L526,136 L524,138.5 L521.5,140.5 L519.5,142.5 L517,144 L514.5,145.5 L512,146.5 L510,147.5 L507.5,148.5 L505.5,149 L503.5,149.5 L502,150 L500.5,150 Z" fill="url(#fy85-cloud)" stroke="#1971c2" stroke-width="2" stroke-linejoin="round"/>
  <path d="M499.5,150 L498,150 L496.5,150.5 L494.5,151 L492.5,151.5 L490,152.5 L488,153.5 L485.5,154.5 L483,156 L480.5,157.5 L478.5,159.5 L476,161.5 L474,164 L472,166.5 L470,169 L468.5,172 L467,175 L465.5,178 L464.5,181 L464,184.5 L463,188 L463,191.5 L463,195 L463,198 L463.5,201.5 L464,205 L465,208 L466.5,211.5 L468,214.5 L469.5,217.5 L471.5,220 L474,222.5 L476,225 L479,227 L481.5,228.5 L484.5,230.5 L487.5,231.5 L490.5,232.5 L493.5,233.5 L497,234 L500,234 L503,234 L506.5,233.5 L509.5,232.5 L512.5,231.5 L515.5,230.5 L518.5,228.5 L521,227 L524,225 L526,222.5 L528.5,220 L530.5,217.5 L532,214.5 L533.5,211.5 L535,208 L536,205 L536.5,201.5 L537,198 L537,195 L537,191.5 L537,188 L536,184.5 L535.5,181 L534.5,178 L533,175 L531.5,172 L530,169 L528,166.5 L526,164 L524,161.5 L521.5,159.5 L519.5,157.5 L517,156 L514.5,154.5 L512,153.5 L510,152.5 L507.5,151.5 L505.5,151 L503.5,150.5 L502,150 L500.5,150 Z" fill="url(#fy85-cloud)" stroke="#1971c2" stroke-width="2" stroke-linejoin="round"/>
  <line x1="420" y1="150" x2="580" y2="150" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="100" cy="150" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="300" cy="150" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="500" cy="150" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="83.5" y="261.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{1s}$</div></foreignObject>
  <foreignObject x="25" y="301.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{no node}$</div></foreignObject>
  <foreignObject x="283.5" y="261.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{2s}$</div></foreignObject>
  <foreignObject x="225" y="301.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nodal sphere}$</div></foreignObject>
  <foreignObject x="483.5" y="261.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{2p}$</div></foreignObject>
  <foreignObject x="425" y="301.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nodal plane}$</div></foreignObject>
</svg>

### The probability interpretation
The wave does not tell where the electron is but where it is likely to be detected. When the position of the electron is measured, the result is always one point, and a single result cannot be predicted. The square of the amplitude of the wave tells how likely the electron is to be detected in a small volume around each place. This is the **probability interpretation** of the wave model. The distribution becomes visible only when the measurement is repeated in many atoms in the same state. If $k$ of $N$ measurements land in some region, the probability of detecting the electron there is approximately
```latex
P \approx \frac{k}{N}
```
where $P$ is the probability, $k$ the number of measurements that landed in the region and $N$ the number of all measurements. The estimate becomes more accurate as $N$ grows. Between measurements the electron has no orbit that could be drawn.

### An orbital describes the quantum state of the electron
When the measurement results are marked as dots, an electron cloud is formed that is densest where the electron is most likely to be detected. The cloud has no sharp edge. An **orbital** describes the quantum state of the electron, an allowed standing wave of the atom, and it sets the probability of detecting the electron at different points. In figures an orbital is shown as a region inside which the electron is detected with a chosen probability, usually with a probability of $90\,\%$. The drawn region is an illustration, not the definition of the orbital. The boundary is an agreed threshold, not a wall: about a tenth of the measurements land outside it. The $90\,\%$ boundary of the $1\text{s}$ orbital of the hydrogen atom is a sphere with a radius of $0.14\,\text{nm}$. For example, the $2\text{p}$ orbital is one of the states of the hydrogen atom.

<svg data-fig="cloud" viewBox="0 0 600 372" role="img" aria-label="Dot figure to scale: the position of the 1s electron of a hydrogen atom has been measured once, 20 times and 1000 times, and each measurement result is marked as a dot. One dot tells nothing about the distribution, 20 dots gather around the nucleus, and 1000 dots form a cloud that is densest near the nucleus and thins out outwards. In the third picture a circle has been drawn that contains 90 percent of the hits: it is the boundary of the 1s orbital, radius 0.14 nm. The hits left outside the boundary are grey. The figure is a see-through projection, so dots overlap: the three-dimensional hits have been drawn in one plane, so some of the grey dots appear inside the circle although they are in front of or behind the boundary. The nucleus is a red dot." style="max-width:100%;font-size:24px">
  <line x1="200" y1="24" x2="200" y2="296" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="400" y1="24" x2="400" y2="296" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <circle cx="79.5" cy="150" r="5" fill="#1971c2"/>
  <circle cx="100" cy="158" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="35" y="303.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N = 1$</div></foreignObject>
  <circle cx="276" cy="146.5" r="5" fill="#1971c2"/>
  <circle cx="288" cy="156.5" r="5" fill="#1971c2"/>
  <circle cx="274.5" cy="141.5" r="5" fill="#1971c2"/>
  <circle cx="320" cy="170" r="5" fill="#1971c2"/>
  <circle cx="303" cy="149" r="5" fill="#1971c2"/>
  <circle cx="314.5" cy="125" r="5" fill="#1971c2"/>
  <circle cx="272" cy="166.5" r="5" fill="#1971c2"/>
  <circle cx="303.5" cy="153.5" r="5" fill="#1971c2"/>
  <circle cx="298.5" cy="175" r="5" fill="#1971c2"/>
  <circle cx="277.5" cy="110.5" r="5" fill="#1971c2"/>
  <circle cx="313" cy="109.5" r="5" fill="#1971c2"/>
  <circle cx="357.5" cy="154" r="5" fill="#1971c2"/>
  <circle cx="274" cy="142" r="5" fill="#1971c2"/>
  <circle cx="294.5" cy="128" r="5" fill="#1971c2"/>
  <circle cx="287.5" cy="160.5" r="5" fill="#1971c2"/>
  <circle cx="283.5" cy="163.5" r="5" fill="#1971c2"/>
  <circle cx="280.5" cy="164" r="5" fill="#1971c2"/>
  <circle cx="284.5" cy="172" r="5" fill="#1971c2"/>
  <circle cx="298" cy="162" r="5" fill="#1971c2"/>
  <circle cx="309.5" cy="140.5" r="5" fill="#1971c2"/>
  <circle cx="300" cy="158" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="235" y="303.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N = 20$</div></foreignObject>
  <circle cx="500" cy="158" r="58.5455" fill="#d0e6fb"/>
  <circle cx="492" cy="183" r="2.2" fill="#6b7480"/>
  <circle cx="545.5" cy="194" r="2.2" fill="#6b7480"/>
  <circle cx="455" cy="182.5" r="2.2" fill="#6b7480"/>
  <circle cx="506.5" cy="181" r="2.2" fill="#6b7480"/>
  <circle cx="485.5" cy="183.5" r="2.2" fill="#6b7480"/>
  <circle cx="530" cy="105" r="2.2" fill="#6b7480"/>
  <circle cx="475" cy="164" r="2.2" fill="#6b7480"/>
  <circle cx="479" cy="220.5" r="2.2" fill="#6b7480"/>
  <circle cx="452.5" cy="199.5" r="2.2" fill="#6b7480"/>
  <circle cx="477" cy="214" r="2.2" fill="#6b7480"/>
  <circle cx="506" cy="86.5" r="2.2" fill="#6b7480"/>
  <circle cx="452" cy="114" r="2.2" fill="#6b7480"/>
  <circle cx="522" cy="190" r="2.2" fill="#6b7480"/>
  <circle cx="555" cy="137.5" r="2.2" fill="#6b7480"/>
  <circle cx="510" cy="206.5" r="2.2" fill="#6b7480"/>
  <circle cx="503.5" cy="179.5" r="2.2" fill="#6b7480"/>
  <circle cx="513" cy="199.5" r="2.2" fill="#6b7480"/>
  <circle cx="512.5" cy="227.5" r="2.2" fill="#6b7480"/>
  <circle cx="551.5" cy="163" r="2.2" fill="#6b7480"/>
  <circle cx="556" cy="194" r="2.2" fill="#6b7480"/>
  <circle cx="487" cy="163.5" r="2.2" fill="#6b7480"/>
  <circle cx="443" cy="125" r="2.2" fill="#6b7480"/>
  <circle cx="442.5" cy="173.5" r="2.2" fill="#6b7480"/>
  <circle cx="430" cy="152.5" r="2.2" fill="#6b7480"/>
  <circle cx="529.5" cy="124.5" r="2.2" fill="#6b7480"/>
  <circle cx="477" cy="178.5" r="2.2" fill="#6b7480"/>
  <circle cx="541" cy="192" r="2.2" fill="#6b7480"/>
  <circle cx="460.5" cy="133" r="2.2" fill="#6b7480"/>
  <circle cx="532" cy="175.5" r="2.2" fill="#6b7480"/>
  <circle cx="430.5" cy="197" r="2.2" fill="#6b7480"/>
  <circle cx="465.5" cy="199" r="2.2" fill="#6b7480"/>
  <circle cx="475" cy="57.5" r="2.2" fill="#6b7480"/>
  <circle cx="555.5" cy="119" r="2.2" fill="#6b7480"/>
  <circle cx="509.5" cy="224.5" r="2.2" fill="#6b7480"/>
  <circle cx="454.5" cy="209.5" r="2.2" fill="#6b7480"/>
  <circle cx="423.5" cy="183.5" r="2.2" fill="#6b7480"/>
  <circle cx="555.5" cy="108.5" r="2.2" fill="#6b7480"/>
  <circle cx="451" cy="126" r="2.2" fill="#6b7480"/>
  <circle cx="486" cy="212.5" r="2.2" fill="#6b7480"/>
  <circle cx="447.5" cy="191" r="2.2" fill="#6b7480"/>
  <circle cx="506.5" cy="211.5" r="2.2" fill="#6b7480"/>
  <circle cx="440" cy="139.5" r="2.2" fill="#6b7480"/>
  <circle cx="491" cy="100.5" r="2.2" fill="#6b7480"/>
  <circle cx="533" cy="213.5" r="2.2" fill="#6b7480"/>
  <circle cx="553" cy="174" r="2.2" fill="#6b7480"/>
  <circle cx="583.5" cy="123.5" r="2.2" fill="#6b7480"/>
  <circle cx="537" cy="126.5" r="2.2" fill="#6b7480"/>
  <circle cx="568" cy="144.5" r="2.2" fill="#6b7480"/>
  <circle cx="491" cy="147" r="2.2" fill="#6b7480"/>
  <circle cx="555" cy="102" r="2.2" fill="#6b7480"/>
  <circle cx="540.5" cy="178.5" r="2.2" fill="#6b7480"/>
  <circle cx="450" cy="164.5" r="2.2" fill="#6b7480"/>
  <circle cx="532" cy="197" r="2.2" fill="#6b7480"/>
  <circle cx="490" cy="123.5" r="2.2" fill="#6b7480"/>
  <circle cx="457" cy="110" r="2.2" fill="#6b7480"/>
  <circle cx="525.5" cy="137" r="2.2" fill="#6b7480"/>
  <circle cx="461.5" cy="168" r="2.2" fill="#6b7480"/>
  <circle cx="535.5" cy="200.5" r="2.2" fill="#6b7480"/>
  <circle cx="525" cy="87.5" r="2.2" fill="#6b7480"/>
  <circle cx="560.5" cy="130" r="2.2" fill="#6b7480"/>
  <circle cx="495" cy="121.5" r="2.2" fill="#6b7480"/>
  <circle cx="554" cy="140" r="2.2" fill="#6b7480"/>
  <circle cx="476.5" cy="196.5" r="2.2" fill="#6b7480"/>
  <circle cx="429.5" cy="144.5" r="2.2" fill="#6b7480"/>
  <circle cx="438.5" cy="175" r="2.2" fill="#6b7480"/>
  <circle cx="438.5" cy="127.5" r="2.2" fill="#6b7480"/>
  <circle cx="570.5" cy="137" r="2.2" fill="#6b7480"/>
  <circle cx="443" cy="186" r="2.2" fill="#6b7480"/>
  <circle cx="546.5" cy="159" r="2.2" fill="#6b7480"/>
  <circle cx="545.5" cy="151.5" r="2.2" fill="#6b7480"/>
  <circle cx="540.5" cy="201" r="2.2" fill="#6b7480"/>
  <circle cx="537" cy="151" r="2.2" fill="#6b7480"/>
  <circle cx="475" cy="180" r="2.2" fill="#6b7480"/>
  <circle cx="525" cy="157" r="2.2" fill="#6b7480"/>
  <circle cx="454.5" cy="114.5" r="2.2" fill="#6b7480"/>
  <circle cx="559" cy="70.5" r="2.2" fill="#6b7480"/>
  <circle cx="461.5" cy="101.5" r="2.2" fill="#6b7480"/>
  <circle cx="529.5" cy="224" r="2.2" fill="#6b7480"/>
  <circle cx="487" cy="180.5" r="2.2" fill="#6b7480"/>
  <circle cx="559.5" cy="154.5" r="2.2" fill="#6b7480"/>
  <circle cx="445.5" cy="160.5" r="2.2" fill="#6b7480"/>
  <circle cx="414.5" cy="155.5" r="2.2" fill="#6b7480"/>
  <circle cx="511.5" cy="216.5" r="2.2" fill="#6b7480"/>
  <circle cx="534.5" cy="201" r="2.2" fill="#6b7480"/>
  <circle cx="546.5" cy="109.5" r="2.2" fill="#6b7480"/>
  <circle cx="498.5" cy="222" r="2.2" fill="#6b7480"/>
  <circle cx="554" cy="119.5" r="2.2" fill="#6b7480"/>
  <circle cx="560" cy="205.5" r="2.2" fill="#6b7480"/>
  <circle cx="478.5" cy="153" r="2.2" fill="#6b7480"/>
  <circle cx="556.5" cy="140.5" r="2.2" fill="#6b7480"/>
  <circle cx="516.5" cy="121.5" r="2.2" fill="#6b7480"/>
  <circle cx="444" cy="175" r="2.2" fill="#6b7480"/>
  <circle cx="457.5" cy="115" r="2.2" fill="#6b7480"/>
  <circle cx="442.5" cy="97.5" r="2.2" fill="#6b7480"/>
  <circle cx="444" cy="113.5" r="2.2" fill="#6b7480"/>
  <circle cx="435.5" cy="132" r="2.2" fill="#6b7480"/>
  <circle cx="529" cy="199" r="2.2" fill="#6b7480"/>
  <circle cx="483.5" cy="134.5" r="2.2" fill="#6b7480"/>
  <circle cx="506.5" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="528.5" cy="184.5" r="2.2" fill="#1971c2"/>
  <circle cx="512" cy="134" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="138" r="2.2" fill="#1971c2"/>
  <circle cx="488.5" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="183" r="2.2" fill="#1971c2"/>
  <circle cx="521" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="168" r="2.2" fill="#1971c2"/>
  <circle cx="480.5" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="483.5" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="481.5" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="178" r="2.2" fill="#1971c2"/>
  <circle cx="519" cy="195.5" r="2.2" fill="#1971c2"/>
  <circle cx="522.5" cy="171.5" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="124.5" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="473.5" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="526" cy="178.5" r="2.2" fill="#1971c2"/>
  <circle cx="529" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="521" cy="178" r="2.2" fill="#1971c2"/>
  <circle cx="483.5" cy="110.5" r="2.2" fill="#1971c2"/>
  <circle cx="529" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="486" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="513.5" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="487.5" cy="133.5" r="2.2" fill="#1971c2"/>
  <circle cx="478.5" cy="131.5" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="169" r="2.2" fill="#1971c2"/>
  <circle cx="468.5" cy="180.5" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="476.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="513" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="512.5" cy="149" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="460.5" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="488" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="524" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="513" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="146" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="488.5" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="472" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="520.5" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="139.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="158.5" r="2.2" fill="#1971c2"/>
  <circle cx="495" cy="168" r="2.2" fill="#1971c2"/>
  <circle cx="487.5" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="520.5" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="171.5" r="2.2" fill="#1971c2"/>
  <circle cx="512" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="168" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="473" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="533.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="167" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="184" r="2.2" fill="#1971c2"/>
  <circle cx="550.5" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="478.5" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="527" cy="137.5" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="484.5" cy="138" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="127.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="180.5" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="524.5" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="135" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="183" r="2.2" fill="#1971c2"/>
  <circle cx="475" cy="127.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="181" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="449" cy="153.5" r="2.2" fill="#1971c2"/>
  <circle cx="519" cy="145" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="524.5" cy="179" r="2.2" fill="#1971c2"/>
  <circle cx="474.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="168" r="2.2" fill="#1971c2"/>
  <circle cx="465.5" cy="192.5" r="2.2" fill="#1971c2"/>
  <circle cx="482" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="526.5" cy="155.5" r="2.2" fill="#1971c2"/>
  <circle cx="536" cy="180" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="137" r="2.2" fill="#1971c2"/>
  <circle cx="488" cy="178" r="2.2" fill="#1971c2"/>
  <circle cx="490.5" cy="157.5" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="142" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="175" r="2.2" fill="#1971c2"/>
  <circle cx="460.5" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="535.5" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="179" r="2.2" fill="#1971c2"/>
  <circle cx="470.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="143.5" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="546" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="535" cy="123.5" r="2.2" fill="#1971c2"/>
  <circle cx="479.5" cy="193.5" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="472" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="129" r="2.2" fill="#1971c2"/>
  <circle cx="530" cy="178" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="149" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="513" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="133" r="2.2" fill="#1971c2"/>
  <circle cx="465" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="132" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="112" r="2.2" fill="#1971c2"/>
  <circle cx="524.5" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="521" cy="174" r="2.2" fill="#1971c2"/>
  <circle cx="488.5" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="532.5" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="129.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="486.5" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="531" cy="137" r="2.2" fill="#1971c2"/>
  <circle cx="522.5" cy="130" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="513" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="497" cy="171.5" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="140.5" r="2.2" fill="#1971c2"/>
  <circle cx="450.5" cy="186" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="492.5" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="109.5" r="2.2" fill="#1971c2"/>
  <circle cx="483" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="146" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="181" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="133.5" r="2.2" fill="#1971c2"/>
  <circle cx="474" cy="165" r="2.2" fill="#1971c2"/>
  <circle cx="530" cy="188.5" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="163.5" r="2.2" fill="#1971c2"/>
  <circle cx="512.5" cy="152.5" r="2.2" fill="#1971c2"/>
  <circle cx="466" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="468.5" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="133.5" r="2.2" fill="#1971c2"/>
  <circle cx="463.5" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="480.5" cy="141" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="481.5" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="204" r="2.2" fill="#1971c2"/>
  <circle cx="452" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="132.5" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="540.5" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="536.5" cy="153.5" r="2.2" fill="#1971c2"/>
  <circle cx="522.5" cy="122.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="152.5" r="2.2" fill="#1971c2"/>
  <circle cx="516" cy="137.5" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="175.5" r="2.2" fill="#1971c2"/>
  <circle cx="478" cy="170" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="145" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="172" r="2.2" fill="#1971c2"/>
  <circle cx="519" cy="177.5" r="2.2" fill="#1971c2"/>
  <circle cx="531" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="468" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="480.5" cy="155.5" r="2.2" fill="#1971c2"/>
  <circle cx="513" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="479" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="488" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="158.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="181" r="2.2" fill="#1971c2"/>
  <circle cx="483.5" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="495" cy="147.5" r="2.2" fill="#1971c2"/>
  <circle cx="546" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="530.5" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="535" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="182" r="2.2" fill="#1971c2"/>
  <circle cx="536.5" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="141" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="506" cy="194" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="478" cy="136.5" r="2.2" fill="#1971c2"/>
  <circle cx="455.5" cy="177.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="190.5" r="2.2" fill="#1971c2"/>
  <circle cx="457" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="515" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="503.5" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="123.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="157.5" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="134" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="131.5" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="537" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="463" cy="182" r="2.2" fill="#1971c2"/>
  <circle cx="534" cy="180.5" r="2.2" fill="#1971c2"/>
  <circle cx="475.5" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="480" cy="134" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="136" r="2.2" fill="#1971c2"/>
  <circle cx="503" cy="129.5" r="2.2" fill="#1971c2"/>
  <circle cx="478.5" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="479.5" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="526.5" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="141" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="138" r="2.2" fill="#1971c2"/>
  <circle cx="483" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="517" cy="113.5" r="2.2" fill="#1971c2"/>
  <circle cx="521" cy="189" r="2.2" fill="#1971c2"/>
  <circle cx="515" cy="210" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="143.5" r="2.2" fill="#1971c2"/>
  <circle cx="473" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="485.5" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="512.5" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="181" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="108" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="180" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="126" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="177" r="2.2" fill="#1971c2"/>
  <circle cx="536" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="470.5" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="147" r="2.2" fill="#1971c2"/>
  <circle cx="480.5" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="136" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="129" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="106.5" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="158.5" r="2.2" fill="#1971c2"/>
  <circle cx="512" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="482" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="170" r="2.2" fill="#1971c2"/>
  <circle cx="524.5" cy="195.5" r="2.2" fill="#1971c2"/>
  <circle cx="487.5" cy="199" r="2.2" fill="#1971c2"/>
  <circle cx="478.5" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="532" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="158.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="147" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="190" r="2.2" fill="#1971c2"/>
  <circle cx="520.5" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="115.5" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="174.5" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="152.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="518.5" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="486.5" cy="147" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="122.5" r="2.2" fill="#1971c2"/>
  <circle cx="486.5" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="478" cy="181.5" r="2.2" fill="#1971c2"/>
  <circle cx="480.5" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="450" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="506" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="468.5" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="524" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="492.5" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="128" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="131" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="190" r="2.2" fill="#1971c2"/>
  <circle cx="521" cy="185.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="466.5" cy="116.5" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="474" cy="185.5" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="165" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="485.5" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="473" cy="139" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="153.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="133" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="531.5" cy="169" r="2.2" fill="#1971c2"/>
  <circle cx="483" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="491.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="496.5" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="174" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="163.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="486.5" cy="178" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="175.5" r="2.2" fill="#1971c2"/>
  <circle cx="480" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="124.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="184" r="2.2" fill="#1971c2"/>
  <circle cx="538.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="513.5" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="497" cy="152.5" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="187" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="112.5" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="488.5" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="521.5" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="488" cy="183" r="2.2" fill="#1971c2"/>
  <circle cx="526.5" cy="135" r="2.2" fill="#1971c2"/>
  <circle cx="525" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="495" cy="143.5" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="127.5" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="179" r="2.2" fill="#1971c2"/>
  <circle cx="525.5" cy="128" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="136.5" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="119.5" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="178.5" r="2.2" fill="#1971c2"/>
  <circle cx="495" cy="167" r="2.2" fill="#1971c2"/>
  <circle cx="506" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="153.5" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="104.5" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="488" cy="184" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="169" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="114" r="2.2" fill="#1971c2"/>
  <circle cx="477.5" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="131.5" r="2.2" fill="#1971c2"/>
  <circle cx="492.5" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="503" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="477.5" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="527.5" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="466" cy="195.5" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="527" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="472.5" cy="181.5" r="2.2" fill="#1971c2"/>
  <circle cx="486" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="492.5" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="542.5" cy="145" r="2.2" fill="#1971c2"/>
  <circle cx="481.5" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="184.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="139.5" r="2.2" fill="#1971c2"/>
  <circle cx="512" cy="183" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="170" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="139.5" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="129" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="478" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="482" cy="194.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="132.5" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="170" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="510" cy="149" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="180" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="534" cy="134.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="480" cy="177" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="116.5" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="140.5" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="175.5" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="188.5" r="2.2" fill="#1971c2"/>
  <circle cx="506" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="539.5" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="528.5" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="488" cy="179" r="2.2" fill="#1971c2"/>
  <circle cx="464.5" cy="191.5" r="2.2" fill="#1971c2"/>
  <circle cx="469.5" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="486.5" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="135" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="483.5" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="524.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="463" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="180.5" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="134" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="129.5" r="2.2" fill="#1971c2"/>
  <circle cx="521" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="165" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="152.5" r="2.2" fill="#1971c2"/>
  <circle cx="483" cy="170" r="2.2" fill="#1971c2"/>
  <circle cx="517" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="481.5" cy="210.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="157.5" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="202" r="2.2" fill="#1971c2"/>
  <circle cx="518.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="503.5" cy="175" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="143.5" r="2.2" fill="#1971c2"/>
  <circle cx="496.5" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="506" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="519" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="497" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="180" r="2.2" fill="#1971c2"/>
  <circle cx="512" cy="167" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="177.5" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="146" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="529.5" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="545.5" cy="142" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="192.5" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="155.5" r="2.2" fill="#1971c2"/>
  <circle cx="471" cy="177.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="491.5" cy="124.5" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="185.5" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="183.5" r="2.2" fill="#1971c2"/>
  <circle cx="516" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="456" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="535.5" cy="178" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="146" r="2.2" fill="#1971c2"/>
  <circle cx="518.5" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="473" cy="180.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="131" r="2.2" fill="#1971c2"/>
  <circle cx="479" cy="135" r="2.2" fill="#1971c2"/>
  <circle cx="546.5" cy="174" r="2.2" fill="#1971c2"/>
  <circle cx="537.5" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="481.5" cy="119.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="126.5" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="512" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="527" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="147" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="471" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="157.5" r="2.2" fill="#1971c2"/>
  <circle cx="471.5" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="174" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="485.5" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="529" cy="188.5" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="479.5" cy="188.5" r="2.2" fill="#1971c2"/>
  <circle cx="532" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="528" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="519" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="198" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="142" r="2.2" fill="#1971c2"/>
  <circle cx="492.5" cy="138" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="174.5" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="103.5" r="2.2" fill="#1971c2"/>
  <circle cx="516" cy="190" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="488.5" cy="163.5" r="2.2" fill="#1971c2"/>
  <circle cx="482" cy="170" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="136" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="120.5" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="158.5" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="182" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="180" r="2.2" fill="#1971c2"/>
  <circle cx="483.5" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="513" cy="145" r="2.2" fill="#1971c2"/>
  <circle cx="470" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="516" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="510" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="531" cy="182" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="490.5" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="180.5" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="147.5" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="184.5" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="139.5" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="490.5" cy="141" r="2.2" fill="#1971c2"/>
  <circle cx="491.5" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="486.5" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="472" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="145" r="2.2" fill="#1971c2"/>
  <circle cx="517" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="475" cy="122.5" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="142" r="2.2" fill="#1971c2"/>
  <circle cx="521" cy="146" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="480" cy="141" r="2.2" fill="#1971c2"/>
  <circle cx="503" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="158.5" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="175.5" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="197.5" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="490.5" cy="168" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="459.5" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="185.5" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="526" cy="201" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="132" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="535" cy="121.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="141" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="129.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="482" cy="165" r="2.2" fill="#1971c2"/>
  <circle cx="449.5" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="515" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="452.5" cy="131" r="2.2" fill="#1971c2"/>
  <circle cx="479" cy="157.5" r="2.2" fill="#1971c2"/>
  <circle cx="523" cy="176.5" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="205" r="2.2" fill="#1971c2"/>
  <circle cx="483.5" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="163.5" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="484.5" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="476" cy="139" r="2.2" fill="#1971c2"/>
  <circle cx="540" cy="136" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="497" cy="169" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="481.5" cy="172" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="136" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="127" r="2.2" fill="#1971c2"/>
  <circle cx="471" cy="145" r="2.2" fill="#1971c2"/>
  <circle cx="522.5" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="458" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="517" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="478.5" cy="133.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="138.5" r="2.2" fill="#1971c2"/>
  <circle cx="526.5" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="479.5" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="496.5" cy="164.5" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="152.5" r="2.2" fill="#1971c2"/>
  <circle cx="530" cy="171.5" r="2.2" fill="#1971c2"/>
  <circle cx="512.5" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="526.5" cy="114" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="477.5" cy="128.5" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="120" r="2.2" fill="#1971c2"/>
  <circle cx="547.5" cy="171.5" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="469.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="487.5" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="541" cy="139.5" r="2.2" fill="#1971c2"/>
  <circle cx="506" cy="174.5" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="146" r="2.2" fill="#1971c2"/>
  <circle cx="488.5" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="523" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="179" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="463.5" cy="123.5" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="150.5" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="497" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="520.5" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="537" cy="121" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="188.5" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="181.5" r="2.2" fill="#1971c2"/>
  <circle cx="483" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="176.5" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="475" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="527.5" cy="183" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="210" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="196.5" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="165.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="147.5" r="2.2" fill="#1971c2"/>
  <circle cx="526" cy="169" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="546" cy="138" r="2.2" fill="#1971c2"/>
  <circle cx="477" cy="119" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="174.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="486" cy="158.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="496.5" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="471.5" cy="182" r="2.2" fill="#1971c2"/>
  <circle cx="456" cy="133" r="2.2" fill="#1971c2"/>
  <circle cx="482" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="473" cy="177" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="490.5" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="492.5" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="491.5" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="147.5" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="184.5" r="2.2" fill="#1971c2"/>
  <circle cx="541" cy="117" r="2.2" fill="#1971c2"/>
  <circle cx="462.5" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="124.5" r="2.2" fill="#1971c2"/>
  <circle cx="511" cy="157.5" r="2.2" fill="#1971c2"/>
  <circle cx="527.5" cy="193" r="2.2" fill="#1971c2"/>
  <circle cx="512.5" cy="148.5" r="2.2" fill="#1971c2"/>
  <circle cx="503.5" cy="150" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="177" r="2.2" fill="#1971c2"/>
  <circle cx="497" cy="145.5" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="145" r="2.2" fill="#1971c2"/>
  <circle cx="517.5" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="484.5" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="478" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="206.5" r="2.2" fill="#1971c2"/>
  <circle cx="531.5" cy="133.5" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="531" cy="175" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="486.5" cy="106.5" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="122.5" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="545.5" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="181" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="495" cy="155.5" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="115.5" r="2.2" fill="#1971c2"/>
  <circle cx="486" cy="171.5" r="2.2" fill="#1971c2"/>
  <circle cx="475" cy="153.5" r="2.2" fill="#1971c2"/>
  <circle cx="497" cy="184" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="176.5" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="469" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="137.5" r="2.2" fill="#1971c2"/>
  <circle cx="492.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="143" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="182.5" r="2.2" fill="#1971c2"/>
  <circle cx="472" cy="174" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="143.5" r="2.2" fill="#1971c2"/>
  <circle cx="503.5" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="475.5" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="143.5" r="2.2" fill="#1971c2"/>
  <circle cx="489.5" cy="169" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="500.5" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="524.5" cy="129.5" r="2.2" fill="#1971c2"/>
  <circle cx="503.5" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="536" cy="179" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="525" cy="146.5" r="2.2" fill="#1971c2"/>
  <circle cx="478" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="484.5" cy="137" r="2.2" fill="#1971c2"/>
  <circle cx="458" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="482.5" cy="181.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="547" cy="163.5" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="549" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="187.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="530" cy="127.5" r="2.2" fill="#1971c2"/>
  <circle cx="479.5" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="136" r="2.2" fill="#1971c2"/>
  <circle cx="498" cy="139" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="152" r="2.2" fill="#1971c2"/>
  <circle cx="505.5" cy="153" r="2.2" fill="#1971c2"/>
  <circle cx="464.5" cy="118" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="189" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="135" r="2.2" fill="#1971c2"/>
  <circle cx="470" cy="175.5" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="495" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="507.5" cy="155.5" r="2.2" fill="#1971c2"/>
  <circle cx="457.5" cy="132.5" r="2.2" fill="#1971c2"/>
  <circle cx="524" cy="184" r="2.2" fill="#1971c2"/>
  <circle cx="480.5" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="515" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="504.5" cy="131.5" r="2.2" fill="#1971c2"/>
  <circle cx="533" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="522" cy="132" r="2.2" fill="#1971c2"/>
  <circle cx="518.5" cy="167" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="172" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="180" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="188.5" r="2.2" fill="#1971c2"/>
  <circle cx="473.5" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="525.5" cy="115" r="2.2" fill="#1971c2"/>
  <circle cx="478" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="524" cy="147" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="159.5" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="481.5" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="532.5" cy="178.5" r="2.2" fill="#1971c2"/>
  <circle cx="523.5" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="499" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="158" r="2.2" fill="#1971c2"/>
  <circle cx="508.5" cy="163.5" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="498.5" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="151.5" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="114.5" r="2.2" fill="#1971c2"/>
  <circle cx="502.5" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="149" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="168" r="2.2" fill="#1971c2"/>
  <circle cx="529.5" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="506.5" cy="185" r="2.2" fill="#1971c2"/>
  <circle cx="527.5" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="497.5" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="517.5" cy="170.5" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="153.5" r="2.2" fill="#1971c2"/>
  <circle cx="488" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="157" r="2.2" fill="#1971c2"/>
  <circle cx="485" cy="146" r="2.2" fill="#1971c2"/>
  <circle cx="539" cy="188" r="2.2" fill="#1971c2"/>
  <circle cx="514.5" cy="151" r="2.2" fill="#1971c2"/>
  <circle cx="479" cy="180" r="2.2" fill="#1971c2"/>
  <circle cx="490" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="528" cy="128" r="2.2" fill="#1971c2"/>
  <circle cx="516" cy="178.5" r="2.2" fill="#1971c2"/>
  <circle cx="520" cy="117.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="168.5" r="2.2" fill="#1971c2"/>
  <circle cx="476" cy="129" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="141" r="2.2" fill="#1971c2"/>
  <circle cx="503.5" cy="171.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="134.5" r="2.2" fill="#1971c2"/>
  <circle cx="525" cy="155.5" r="2.2" fill="#1971c2"/>
  <circle cx="479.5" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="181.5" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="161.5" r="2.2" fill="#1971c2"/>
  <circle cx="488.5" cy="170" r="2.2" fill="#1971c2"/>
  <circle cx="504" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="501" cy="144.5" r="2.2" fill="#1971c2"/>
  <circle cx="539" cy="182.5" r="2.2" fill="#1971c2"/>
  <circle cx="510" cy="138" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="529" cy="200" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="156" r="2.2" fill="#1971c2"/>
  <circle cx="490.5" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="494.5" cy="154" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="189.5" r="2.2" fill="#1971c2"/>
  <circle cx="496" cy="155.5" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="171" r="2.2" fill="#1971c2"/>
  <circle cx="482" cy="181.5" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="162.5" r="2.2" fill="#1971c2"/>
  <circle cx="510.5" cy="115.5" r="2.2" fill="#1971c2"/>
  <circle cx="473" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="480" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="490.5" cy="163" r="2.2" fill="#1971c2"/>
  <circle cx="550" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="515.5" cy="165" r="2.2" fill="#1971c2"/>
  <circle cx="493.5" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="141.5" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="165" r="2.2" fill="#1971c2"/>
  <circle cx="532.5" cy="124.5" r="2.2" fill="#1971c2"/>
  <circle cx="550.5" cy="169.5" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="521.5" cy="180.5" r="2.2" fill="#1971c2"/>
  <circle cx="487" cy="176" r="2.2" fill="#1971c2"/>
  <circle cx="491" cy="173" r="2.2" fill="#1971c2"/>
  <circle cx="509" cy="162" r="2.2" fill="#1971c2"/>
  <circle cx="494" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="489" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="511.5" cy="169" r="2.2" fill="#1971c2"/>
  <circle cx="509.5" cy="189" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="160.5" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="476" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="164" r="2.2" fill="#1971c2"/>
  <circle cx="514" cy="148" r="2.2" fill="#1971c2"/>
  <circle cx="518" cy="166" r="2.2" fill="#1971c2"/>
  <circle cx="501.5" cy="144" r="2.2" fill="#1971c2"/>
  <circle cx="481" cy="153.5" r="2.2" fill="#1971c2"/>
  <circle cx="528" cy="172.5" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="189.5" r="2.2" fill="#1971c2"/>
  <circle cx="496.5" cy="142" r="2.2" fill="#1971c2"/>
  <circle cx="506" cy="195.5" r="2.2" fill="#1971c2"/>
  <circle cx="495" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="470" cy="168" r="2.2" fill="#1971c2"/>
  <circle cx="484" cy="135.5" r="2.2" fill="#1971c2"/>
  <circle cx="461.5" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="495.5" cy="173.5" r="2.2" fill="#1971c2"/>
  <circle cx="466" cy="179.5" r="2.2" fill="#1971c2"/>
  <circle cx="474.5" cy="160" r="2.2" fill="#1971c2"/>
  <circle cx="502" cy="143.5" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="149.5" r="2.2" fill="#1971c2"/>
  <circle cx="517.5" cy="156.5" r="2.2" fill="#1971c2"/>
  <circle cx="507" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="459.5" cy="176.5" r="2.2" fill="#1971c2"/>
  <circle cx="519.5" cy="155" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="172" r="2.2" fill="#1971c2"/>
  <circle cx="499.5" cy="154.5" r="2.2" fill="#1971c2"/>
  <circle cx="525.5" cy="137.5" r="2.2" fill="#1971c2"/>
  <circle cx="521.5" cy="167.5" r="2.2" fill="#1971c2"/>
  <circle cx="476" cy="207.5" r="2.2" fill="#1971c2"/>
  <circle cx="487.5" cy="140" r="2.2" fill="#1971c2"/>
  <circle cx="493" cy="159" r="2.2" fill="#1971c2"/>
  <circle cx="508" cy="172" r="2.2" fill="#1971c2"/>
  <circle cx="516" cy="166.5" r="2.2" fill="#1971c2"/>
  <circle cx="505" cy="142.5" r="2.2" fill="#1971c2"/>
  <circle cx="492" cy="157.5" r="2.2" fill="#1971c2"/>
  <circle cx="512" cy="161" r="2.2" fill="#1971c2"/>
  <circle cx="500" cy="158" r="58.5455" fill="none" stroke="#1971c2" stroke-width="2.5"/>
  <line x1="541.5" y1="116.5" x2="564" y2="60" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="531" y="31.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$90\,\%$</div></foreignObject>
  <circle cx="500" cy="158" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="435" y="303.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N = 1000$</div></foreignObject>
  <line x1="40" y1="354" x2="81.5" y2="354" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="40" y1="347" x2="40" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="81.5" y1="347" x2="81.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="339.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0.1\,\text{nm}$</div></foreignObject>
  <foreignObject x="438" y="339.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{overlapping dots}$</div></foreignObject>
</svg>

The cloud is densest at the nucleus, but the most common distance from the nucleus is not zero. A thin spherical shell farther from the nucleus holds more volume than a small sphere right around the nucleus, so a $1\text{s}$ electron is detected most often at a distance of about $0.053\,\text{nm}$. This is the same as the radius of the smallest orbit of the Bohr model: in the wave model the Bohr orbit is the most common distance, not a path travelled by the electron.

<figure class="unit-photo"><img src="pics/fy8/stm-laboratory.webp" alt="A large laboratory instrument whose parts are wrapped in aluminium foil, surrounded by tubes, cables and pumps."><figcaption>A scanning tunnelling microscope in a laboratory in Seoul. Its sharp tip moves just above the surface of a sample, and the tiny electric current between the tip and the surface gives an image of the individual atoms of the surface.</figcaption></figure>

## Formula: Shells, orbitals and energy levels
In the hydrogen atom the energy of a state depends only on the principal quantum number $n$, and the wave model gives the same energy levels as the Bohr model:
```latex
E_n = -\frac{13.6\,\text{eV}}{n^2}
```
where $E_n$ is the energy of the electron (eV) in the shell $n = 1, 2, 3, \ldots$ States with the same principal quantum number form an electron shell. The shell $n$ has $n$ subshells, s, p, d and f, which have $1$, $3$, $5$ and $7$ orbitals, so the number of orbitals in a shell is $n^2$.

The number of orbitals in a subshell depends on the shape of the wave. An s orbital is a sphere, so there can be only one. The pair of lobes of a p orbital can point in three mutually perpendicular directions ($x$, $y$ and $z$), so there are three p orbitals; the figures of this chapter show one of them, whose lobes are vertical. The d and f subshells have five and seven different orbitals, respectively. An electron also has spin, its own property with only two possible values. Each orbital can therefore hold at most two electrons, and they have opposite spins (Pauli exclusion principle). So at most
```latex
N_\text{max} = 2n^2
```
electrons fit in a shell, where $N_\text{max}$ is the greatest number of electrons and $n$ the principal quantum number of the shell.

| Shell $n$ | Subshells | Orbitals $n^2$ | Electrons $2n^2$ |
| --- | --- | --- | --- |
| $1$ | s | $1$ | $2$ |
| $2$ | s, p | $4$ | $8$ |
| $3$ | s, p, d | $9$ | $18$ |
| $4$ | s, p, d, f | $16$ | $32$ |

When an electron moves from a higher state to a lower one, the atom emits a photon whose energy is the difference between the energies of the states (chapter *Spectra reveal the energy levels of atoms*). In the hydrogen atom the states of the same shell have the same energy, so, for example, the transitions $3\text{d} \to 2\text{p}$ and $3\text{s} \to 2\text{p}$ produce the same spectral line.

<svg data-fig="levels" viewBox="0 0 600 396" role="img" aria-label="The energy levels of the hydrogen atom to scale and their orbitals as boxes. The shell n = 1 has one orbital, 1s, with the energy −13.6 eV. The shell n = 2, with the energy −3.40 eV, has the 2s orbital and three 2p orbitals, four altogether. The shell n = 3, with the energy −1.51 eV, has 3s, three 3p and five 3d orbitals, nine altogether. At the top is a dashed line E = 0, above which the electron is free of the atom. The arrow shows the transition of the electron from the 3d orbital to the 2p orbital; at the same time a photon is produced with a wavelength of 656 nm, red light. Each orbital can hold at most two electrons." style="max-width:100%;font-size:24px">
  <line x1="118" y1="374" x2="118" y2="30" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M118,18 L124,31 L112,31 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="132" y="7.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{eV})$</div></foreignObject>
  <line x1="118" y1="40" x2="590" y2="40" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="112" y1="40" x2="118" y2="40" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="21.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="112" y1="75.5" x2="118" y2="75.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="65" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-1.51$</div></foreignObject>
  <line x1="112" y1="120" x2="118" y2="120" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="105.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-3.40$</div></foreignObject>
  <line x1="112" y1="360" x2="118" y2="360" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="345.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-13.6$</div></foreignObject>
  <foreignObject x="126" y="345.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{1s}$</div></foreignObject>
  <rect x="178" y="351" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="126" y="105.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{2s}$</div></foreignObject>
  <rect x="178" y="111" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="210" y="105.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{2p}$</div></foreignObject>
  <rect x="262" y="111" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="292" y="111" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="322" y="111" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="126" y="61" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{3s}$</div></foreignObject>
  <rect x="178" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="210" y="61" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{3p}$</div></foreignObject>
  <rect x="262" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="292" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="322" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="352" y="61" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{3d}$</div></foreignObject>
  <rect x="404" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="434" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="464" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="494" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="524" y="66.5" width="26" height="18" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="417" y1="85.5" x2="348.5" y2="106" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M339,109 L348,101 L351,110.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M365,148 L365.5,150 L365.5,152.5 L366.5,154.5 L367,156 L368,157 L369,158 L370,158.5 L371.5,158.5 L373.5,158 L375,157.5 L377,156.5 L379.5,155.5 L381.5,154.5 L383.5,153.5 L385,153 L387,152.5 L388.5,152.5 L389.5,153 L390.5,154 L391.5,155 L392.5,157 L393,158.5 L393,161 L393.5,163 L394,165.5 L394.5,167.5 L395,169.5 L395.5,171 L396.5,172 L397.5,173 L398.5,173.5 L400,173.5 L402,173 L404,172.5 L406,171.5 L408,170.5 L410,169.5 L412,169 L413.5,168 L415.5,168 L417,168 L418,168 L419.5,169 L420,170.5 L421,172 L421.5,174 L421.5,176 L422,178 L422.5,180.5 L423,182.5 L423.5,184.5 L424,186 L425,187.5 L426,188 L427,188.5 L428.5,188.5 L430.5,188 L432.5,187.5 L434.5,186.5 L436.5,185.5 L438.5,185 L440.5,184 L442,183 L444,183 L445.5,183 L446.5,183.5 L448,184 L448.5,185.5 L449.5,187 L450,189 L450,191 L450.5,193.5 L451,195.5 L451.5,197.5 L452,199.5 L452.5,201 L453.5,202.5 L454.5,203 L455.5,203.5 L457,203.5 L459,203.5 L461,202.5 L463,202 L465,201 L467,200 L469,199 L470.5,198.5 L472.5,198 L474,198 L475,198.5 L476.5,199 L477,200.5 L478,202 L478.5,204 L479,206 L479,208.5 L479.5,210.5 L480,212.5 L480.5,214.5 L481,216 L482,217.5 L483,218.5 L484.5,218.5 L486,219 L487.5,218.5 L489.5,217.5 L491.5,217 L493.5,216 L495.5,215 L497.5,214 L499,213.5 L501,213 L502.5,213 L504,213.5 L505,214.5 L505.5,215.5 L506.5,217 L507,219 L507.5,221 L507.5,223.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M520,230 L504.5,229.5 L511,217.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="476" y="173.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <foreignObject x="440" y="243.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\lambda = 656\,\text{nm}$</div></foreignObject>
  <line x1="210" y1="360" x2="228" y2="360" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="234" y="345.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{at most } 2\ e^-$</div></foreignObject>
</svg>

### Connection to the orbitals of chemistry
In an atom with many electrons the electrons repel each other, so the subshells of the same shell have different energies: $2\text{s}$ is lower than $2\text{p}$ and $3\text{s}$ lower than $3\text{p}$. In the ground state the electrons fill the orbitals starting from the lowest energy, at most two in each orbital. The filling order of light atoms is $1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$. The six electrons of carbon are placed like this: $1\text{s}^2\,2\text{s}^2\,2\text{p}^2$, where the superscript is the number of electrons in the subshell.

The electrons of the outermost shell, the valence electrons, are on average farthest from the nucleus and most weakly bound, and they decide what kind of bonds the atom forms. The periodic table and the orbital pictures of chemistry thus rest on the same wave model.

## Worked example
The electron of a hydrogen atom moves from the $3\text{d}$ orbital to the $2\text{p}$ orbital, and the atom emits a photon. What is the wavelength of the photon?

<!-- vaihe -->

**Given and asked.** The initial state $3\text{d}$ belongs to the shell $n = 3$ and the final state $2\text{p}$ to the shell $n = 2$. The energy levels of the hydrogen atom are $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$, the Planck constant is $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$ and the speed of light is $c = 2.998 \cdot 10^{8}\,\text{m/s}$. The wavelength $\lambda$ of the photon is asked.

<!-- vaihe -->

**Principle.** Energy is conserved: the energy of the atom decreases by the difference between the energies of the states, and this energy leaves as a photon whose energy is $hf = \tfrac{hc}{\lambda}$. In the hydrogen atom the energy of a state depends only on the principal quantum number, so the letters d and p do not change the energy; they tell the shape of the wave.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&\frac{hc}{\lambda} = E_3 - E_2 \\
&\lambda = \frac{hc}{E_3 - E_2}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The energy difference in electronvolts is $E_3 - E_2 = -\tfrac{13.6\,\text{eV}}{9} + \tfrac{13.6\,\text{eV}}{4} = 1.8889\,\text{eV}$. Extra figures are kept in the intermediate results, and rounding is done only at the end. The energy difference is converted to joules by substituting $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$: $E_3 - E_2 = 1.8889 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 3.0260 \cdot 10^{-19}\,\text{J}$.

<!-- vaihe -->

**Substitution.** First we calculate the numerator $hc = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s} = 1.98647 \cdot 10^{-25}\,\text{J}\,\text{m}$ and divide it by the energy difference:
```latex
\begin{aligned}
&\lambda = \frac{hc}{E_3 - E_2} \\
&= \frac{1.98647 \cdot 10^{-25}\,\text{J}\,\text{m}}{3.0260 \cdot 10^{-19}\,\text{J}} \\
&= 6.5647 \cdot 10^{-7}\,\text{m} \\
&= 656.47\,\text{nm}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The wavelength of the photon is $656\,\text{nm}$, with three significant figures like the energy $13.6\,\text{eV}$.

<!-- vaihe -->

**Reasonableness.** The wavelength is in the range of visible light, and $656\,\text{nm}$ is the red line of the spectrum of hydrogen (chapter *Spectra reveal the energy levels of atoms*). The photon energy $1.9\,\text{eV}$ lies between the energies of photons of visible light, $1.6$–$3.3\,\text{eV}$. The transition $3\text{s} \to 2\text{p}$ would give the same line, because the energy of the initial state is the same.

## Common misconception
Many think that an orbital is an orbit along which the electron goes round, or a shell inside which the electron stays. In the wave model the electron has no orbit, and the boundary of an orbital is an agreed probability boundary: outside the $90\,\%$ boundary the electron is detected on average in every tenth measurement. Another mistake is to think that the cloud arises because the electron whizzes so fast that its orbit blurs like the blades of a rotating fan. The cloud describes the distribution of the measurement results: a single measurement always gives one point, and the position of the electron between measurements cannot be described as a path.

## Summary
- In the wave-mechanical model of the atom, the state of an electron is described by a standing wave that spreads around the nucleus. Only certain wave shapes are possible, so the energy is quantised; in the hydrogen atom, the more nodes, the greater the energy.
- Probability interpretation: the wave tells how likely the electron is to be detected at each place. One measurement gives one random point, and the distribution is seen only from many measurements: $P \approx \tfrac{k}{N}$.
- An orbital describes the quantum state of the electron. It is illustrated by a region inside which the electron is detected with a chosen probability, for example $90\,\%$. The $90\,\%$ boundary of the $1\text{s}$ orbital of the hydrogen atom is a sphere with a radius of $0.14\,\text{nm}$.
- The shell $n$ has $n^2$ orbitals and at most $2n^2$ electrons. The energy levels of the hydrogen atom are $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$.
- Orbitals fill starting from the lowest energy ($1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$), and this is the basis of the electron configurations and the periodic table of chemistry.
