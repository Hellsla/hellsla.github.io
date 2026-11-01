# Building nuclei: isotopes and nuclear notation

> **Why** do the protons in a nucleus not fly apart, although they all repel each other?

<!-- The Isotope Builder in inquiry.json reads data-src="units/fy14/data/nuclides.json" (named here so that build.py embeds it and the content hash covers it). -->

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a dark background. On the left, a large, faint blue cloud stands for the electrons of an atom; at its centre is a tiny bright dot, the nucleus. Two thin lines lead from the dot to a large magnifying circle on the right. Inside the circle the nucleus is shown enlarged: a tight cluster of red protons, each marked with a plus sign, and grey neutrons, all touching each other." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy14nu-h-bg" cx="30%" cy="50%" r="80%"><stop offset="0" stop-color="#2d3a46"/><stop offset="1" stop-color="#141b22"/></radialGradient><radialGradient id="fy14nu-h-cloud" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#d0e6fb" stop-opacity="0.55"/><stop offset="0.6" stop-color="#1971c2" stop-opacity="0.28"/><stop offset="1" stop-color="#1971c2" stop-opacity="0"/></radialGradient><radialGradient id="fy14nu-h-lens" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#3b4a58"/><stop offset="1" stop-color="#1f2933"/></radialGradient><radialGradient id="fy14nu-h-p" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#ff8a80"/><stop offset="55%" stop-color="#c92a2a"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient><radialGradient id="fy14nu-h-n" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#e9ecef"/><stop offset="55%" stop-color="#9aa1a9"/><stop offset="100%" stop-color="#4b5259"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy14nu-h-bg)"/>
  <circle cx="323.5" cy="119" r="0.896503" fill="#55626f"/>
  <circle cx="504" cy="21" r="1.96842" fill="#55626f"/>
  <circle cx="356" cy="528" r="1.57648" fill="#55626f"/>
  <circle cx="1084" cy="190.5" r="1.09109" fill="#55626f"/>
  <circle cx="741.5" cy="385.5" r="1.49172" fill="#55626f"/>
  <circle cx="1088" cy="79.5" r="1.78631" fill="#55626f"/>
  <circle cx="825.5" cy="564.5" r="1.14273" fill="#55626f"/>
  <circle cx="145" cy="188" r="0.817888" fill="#55626f"/>
  <circle cx="1013.5" cy="547" r="1.04391" fill="#55626f"/>
  <circle cx="70.5" cy="409.5" r="1.09809" fill="#55626f"/>
  <circle cx="343.5" cy="53.5" r="1.44902" fill="#55626f"/>
  <circle cx="889.5" cy="457" r="1.70485" fill="#55626f"/>
  <circle cx="758.5" cy="448" r="1.55481" fill="#55626f"/>
  <circle cx="160" cy="456.5" r="1.9422" fill="#55626f"/>
  <circle cx="76" cy="252" r="0.816292" fill="#55626f"/>
  <circle cx="249.5" cy="481.5" r="0.977195" fill="#55626f"/>
  <circle cx="588.5" cy="592.5" r="1.38651" fill="#55626f"/>
  <circle cx="529" cy="78.5" r="1.31924" fill="#55626f"/>
  <circle cx="190.5" cy="527" r="0.922022" fill="#55626f"/>
  <circle cx="31.5" cy="586.5" r="0.859964" fill="#55626f"/>
  <circle cx="163.5" cy="407.5" r="1.11421" fill="#55626f"/>
  <circle cx="746" cy="505.5" r="1.78368" fill="#55626f"/>
  <circle cx="947" cy="35" r="0.933209" fill="#55626f"/>
  <circle cx="232" cy="478.5" r="1.52605" fill="#55626f"/>
  <circle cx="210" cy="471.5" r="0.925493" fill="#55626f"/>
  <circle cx="117" cy="11.5" r="1.13346" fill="#55626f"/>
  <circle cx="1191" cy="531" r="1.85398" fill="#55626f"/>
  <circle cx="86.5" cy="71.5" r="1.87444" fill="#55626f"/>
  <circle cx="962.5" cy="474.5" r="1.34379" fill="#55626f"/>
  <circle cx="464" cy="15" r="1.578" fill="#55626f"/>
  <circle cx="903.5" cy="244" r="1.26908" fill="#55626f"/>
  <circle cx="1006" cy="40" r="1.14105" fill="#55626f"/>
  <circle cx="597.5" cy="386.5" r="1.36986" fill="#55626f"/>
  <circle cx="185" cy="385.5" r="1.22585" fill="#55626f"/>
  <circle cx="466" cy="163" r="0.955638" fill="#55626f"/>
  <circle cx="831.5" cy="587.5" r="1.82404" fill="#55626f"/>
  <circle cx="1118" cy="405" r="1.50734" fill="#55626f"/>
  <circle cx="165.5" cy="445.5" r="1.72129" fill="#55626f"/>
  <circle cx="807" cy="285.5" r="0.907591" fill="#55626f"/>
  <circle cx="432" cy="179.5" r="1.19715" fill="#55626f"/>
  <circle cx="442.5" cy="173.5" r="0.853382" fill="#55626f"/>
  <circle cx="802" cy="149.5" r="1.59074" fill="#55626f"/>
  <circle cx="97.5" cy="549" r="1.79778" fill="#55626f"/>
  <circle cx="65" cy="187.5" r="1.03175" fill="#55626f"/>
  <circle cx="284.5" cy="385.5" r="1.51347" fill="#55626f"/>
  <circle cx="494" cy="534" r="1.04305" fill="#55626f"/>
  <circle cx="361.5" cy="77" r="0.836234" fill="#55626f"/>
  <circle cx="442.5" cy="521" r="1.80421" fill="#55626f"/>
  <circle cx="478" cy="130.5" r="1.26499" fill="#55626f"/>
  <circle cx="732.5" cy="534" r="1.34605" fill="#55626f"/>
  <circle cx="370" cy="410" r="1.3242" fill="#55626f"/>
  <circle cx="619.5" cy="330.5" r="1.31658" fill="#55626f"/>
  <circle cx="723" cy="238" r="0.969723" fill="#55626f"/>
  <circle cx="709.5" cy="112" r="1.49509" fill="#55626f"/>
  <circle cx="1033.5" cy="238" r="1.69855" fill="#55626f"/>
  <circle cx="856.5" cy="514.5" r="0.806741" fill="#55626f"/>
  <circle cx="137" cy="257.5" r="0.926443" fill="#55626f"/>
  <circle cx="742.5" cy="97" r="1.71166" fill="#55626f"/>
  <circle cx="636" cy="516.5" r="1.20443" fill="#55626f"/>
  <circle cx="1198" cy="554.5" r="1.65409" fill="#55626f"/>
  <circle cx="300" cy="300" r="250" fill="url(#fy14nu-h-cloud)"/>
  <circle cx="438.5" cy="433.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="397.5" cy="378" r="2.2" fill="#d0e6fb"/>
  <circle cx="466.5" cy="186" r="2.2" fill="#d0e6fb"/>
  <circle cx="175.5" cy="267" r="2.2" fill="#d0e6fb"/>
  <circle cx="346.5" cy="123" r="2.2" fill="#d0e6fb"/>
  <circle cx="201" cy="394.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="298" cy="225.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="473.5" cy="365" r="2.2" fill="#d0e6fb"/>
  <circle cx="368" cy="192" r="2.2" fill="#d0e6fb"/>
  <circle cx="468.5" cy="227" r="2.2" fill="#d0e6fb"/>
  <circle cx="414.5" cy="452" r="2.2" fill="#d0e6fb"/>
  <circle cx="397" cy="242.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="423.5" cy="389.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="115" cy="266.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="415" cy="224" r="2.2" fill="#d0e6fb"/>
  <circle cx="194.5" cy="253.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="234.5" cy="117" r="2.2" fill="#d0e6fb"/>
  <circle cx="324" cy="255" r="2.2" fill="#d0e6fb"/>
  <circle cx="269" cy="123.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="456" cy="283.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="344.5" cy="512" r="2.2" fill="#d0e6fb"/>
  <circle cx="215.5" cy="134" r="2.2" fill="#d0e6fb"/>
  <circle cx="401.5" cy="481" r="2.2" fill="#d0e6fb"/>
  <circle cx="395" cy="347.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="193" cy="192" r="2.2" fill="#d0e6fb"/>
  <circle cx="311" cy="103" r="2.2" fill="#d0e6fb"/>
  <circle cx="327.5" cy="210.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="382" cy="463.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="247" cy="419" r="2.2" fill="#d0e6fb"/>
  <circle cx="270.5" cy="461" r="2.2" fill="#d0e6fb"/>
  <circle cx="458" cy="325.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="301" cy="316" r="2.2" fill="#d0e6fb"/>
  <circle cx="87" cy="283.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="193" cy="357" r="2.2" fill="#d0e6fb"/>
  <circle cx="236.5" cy="299" r="2.2" fill="#d0e6fb"/>
  <circle cx="280" cy="106" r="2.2" fill="#d0e6fb"/>
  <circle cx="275" cy="445" r="2.2" fill="#d0e6fb"/>
  <circle cx="448.5" cy="233" r="2.2" fill="#d0e6fb"/>
  <circle cx="419" cy="380" r="2.2" fill="#d0e6fb"/>
  <circle cx="141" cy="323" r="2.2" fill="#d0e6fb"/>
  <circle cx="254" cy="346" r="2.2" fill="#d0e6fb"/>
  <circle cx="109.5" cy="298.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="255.5" cy="221.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="451" cy="405.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="257.5" cy="473" r="2.2" fill="#d0e6fb"/>
  <circle cx="395" cy="426.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="467.5" cy="330" r="2.2" fill="#d0e6fb"/>
  <circle cx="414" cy="310.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="129.5" cy="213" r="2.2" fill="#d0e6fb"/>
  <circle cx="231" cy="347" r="2.2" fill="#d0e6fb"/>
  <circle cx="366" cy="95.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="328" cy="187.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="348" cy="107.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="502" cy="370" r="2.2" fill="#d0e6fb"/>
  <circle cx="353" cy="129.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="340" cy="283.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="506.5" cy="328.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="298" cy="159.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="219" cy="174" r="2.2" fill="#d0e6fb"/>
  <circle cx="263" cy="226.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="168" cy="357.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="266.5" cy="399" r="2.2" fill="#d0e6fb"/>
  <circle cx="278.5" cy="505.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="308.5" cy="106.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="511.5" cy="357.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="365.5" cy="452" r="2.2" fill="#d0e6fb"/>
  <circle cx="458.5" cy="265.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="171.5" cy="389" r="2.2" fill="#d0e6fb"/>
  <circle cx="387" cy="463.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="469" cy="272" r="2.2" fill="#d0e6fb"/>
  <circle cx="157" cy="145.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="362.5" cy="257" r="2.2" fill="#d0e6fb"/>
  <circle cx="227" cy="292" r="2.2" fill="#d0e6fb"/>
  <circle cx="354" cy="349.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="417.5" cy="128.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="271" cy="471.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="304" cy="471" r="2.2" fill="#d0e6fb"/>
  <circle cx="480" cy="350" r="2.2" fill="#d0e6fb"/>
  <circle cx="396" cy="408" r="2.2" fill="#d0e6fb"/>
  <circle cx="467.5" cy="301" r="2.2" fill="#d0e6fb"/>
  <circle cx="108.5" cy="304.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="323" cy="304.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="238.5" cy="231" r="2.2" fill="#d0e6fb"/>
  <circle cx="281.5" cy="137" r="2.2" fill="#d0e6fb"/>
  <circle cx="249" cy="306" r="2.2" fill="#d0e6fb"/>
  <circle cx="475" cy="218" r="2.2" fill="#d0e6fb"/>
  <circle cx="257" cy="435" r="2.2" fill="#d0e6fb"/>
  <circle cx="361.5" cy="333" r="2.2" fill="#d0e6fb"/>
  <circle cx="502" cy="271.5" r="2.2" fill="#d0e6fb"/>
  <circle cx="380" cy="251" r="2.2" fill="#d0e6fb"/>
  <circle cx="300" cy="300" r="5" fill="#f2a69c"/>
  <circle cx="300" cy="300" r="2.5" fill="#ffffff"/>
  <line x1="304" y1="296" x2="706" y2="144" stroke="#9aa1a9" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 8"/>
  <line x1="304" y1="304" x2="706" y2="456" stroke="#9aa1a9" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 8"/>
  <circle cx="300" cy="300" r="14" fill="none" stroke="#9aa1a9" stroke-width="2"/>
  <circle cx="860" cy="300" r="220" fill="url(#fy14nu-h-lens)" stroke="#8a96a3" stroke-width="10"/>
  <circle cx="860" cy="300" r="210" fill="none" stroke="#c4ccd4" stroke-width="2" stroke-opacity="0.5"/>
  <circle cx="970" cy="276" r="30" fill="url(#fy14nu-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="766.5" cy="246" r="30" fill="url(#fy14nu-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="753" y1="246" x2="780" y2="246" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <line x1="766.5" y1="232.5" x2="766.5" y2="259.5" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <circle cx="891" cy="399" r="30" fill="url(#fy14nu-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="902" cy="210" r="30" fill="url(#fy14nu-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="888.5" y1="210" x2="915.5" y2="210" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <line x1="902" y1="196.5" x2="902" y2="223.5" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <circle cx="773" cy="336" r="30" fill="url(#fy14nu-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="944" cy="330.5" r="30" fill="url(#fy14nu-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="930.5" y1="330.5" x2="957.5" y2="330.5" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <line x1="944" y1="317" x2="944" y2="344" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <circle cx="821.5" cy="225.5" r="30" fill="url(#fy14nu-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="839.5" cy="375.5" r="30" fill="url(#fy14nu-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="826" y1="375.5" x2="853" y2="375.5" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <line x1="839.5" y1="362" x2="839.5" y2="389" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <circle cx="920.5" cy="261.5" r="30" fill="url(#fy14nu-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="796" cy="288.5" r="30" fill="url(#fy14nu-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="782.5" y1="288.5" x2="809.5" y2="288.5" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <line x1="796" y1="275" x2="796" y2="302" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <circle cx="895" cy="345.5" r="30" fill="url(#fy14nu-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="864" cy="252" r="30" fill="url(#fy14nu-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="850.5" y1="252" x2="877.5" y2="252" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <line x1="864" y1="238.5" x2="864" y2="265.5" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <circle cx="832.5" cy="325.5" r="30" fill="url(#fy14nu-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="881.5" cy="300" r="30" fill="url(#fy14nu-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="868" y1="300" x2="895" y2="300" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <line x1="881.5" y1="286.5" x2="881.5" y2="313.5" stroke="#ffffff" stroke-width="4.8" stroke-linecap="round"/>
  <path d="M710,180 Q800,110 900,120" fill="none" stroke="#ffffff" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.25"/>
</svg>

## Inside the atom {Particles}

An atom has a tiny **nucleus** with **electrons** around it (Rutherford, 1911). The nucleus is made of **protons** and **neutrons**, together called **nucleons**. Rutherford identified the proton in experiments from 1917 to 1920; James Chadwick discovered the neutron in 1932.

| Particle | Charge | Mass (u) | Where |
| --- | --- | --- | --- |
| proton | $+e$ | $1.00728$ | nucleus |
| neutron | $0$ | $1.00866$ | nucleus |
| electron | $-e$ | $0.00055$ | around it |

Here $e = 1.602 \cdot 10^{-19}\ \text{C}$ is the elementary charge and $1\ \text{u} = 1.661 \cdot 10^{-27}\ \text{kg}$ the **atomic mass unit**. A proton is $1836$ times as heavy as an electron, so almost all the mass of an atom is in the nucleus, although its diameter is only $1/60\,000$ (hydrogen) to $1/27\,000$ (uranium) of the atom's.

## Key idea

The number of protons is the **atomic number** $Z$. It decides the element: every carbon nucleus has $Z = 6$, every uranium nucleus $Z = 92$. The number of neutrons is the **neutron number** $N$. Nuclei of one element with different numbers of neutrons are **isotopes** of the element, from the Greek for "same place": they share a place in the periodic table. The Scottish doctor Margaret Todd suggested the word to the chemist Frederick Soddy in 1913.

Isotopes have practically the same chemistry but different masses. Some are **stable**; others are **radioactive** and change into another nucleus after some time. Hydrogen has three isotopes, and two of them are the fuel of fusion reactors:

<svg data-fig="hydrogen" viewBox="0 0 600 300" role="img" aria-label="Three nuclei side by side, drawn as red protons with a plus sign and grey neutrons. Left: hydrogen-1, one proton only, notation 1 over 1 H, stable. Middle: hydrogen-2 or deuterium, one proton and one neutron, 2 over 1 H, stable. Right: hydrogen-3 or tritium, one proton and two neutrons, 3 over 1 H, radioactive with a half-life of 12.3 years. All three have Z = 1, so they are the same element." style="max-width:100%;font-size:26px">
  <defs><radialGradient id="fy14nu-hy-p" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#ff8a80"/><stop offset="55%" stop-color="#c92a2a"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient><radialGradient id="fy14nu-hy-n" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#e9ecef"/><stop offset="55%" stop-color="#9aa1a9"/><stop offset="100%" stop-color="#4b5259"/></radialGradient></defs>
  <circle cx="100" cy="92" r="22" fill="url(#fy14nu-hy-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="90" y1="92" x2="110" y2="92" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <line x1="100" y1="82" x2="100" y2="102" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <circle cx="281" cy="92" r="22" fill="url(#fy14nu-hy-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="319" cy="92" r="22" fill="url(#fy14nu-hy-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="309" y1="92" x2="329" y2="92" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <line x1="319" y1="82" x2="319" y2="102" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <circle cx="481" cy="103" r="22" fill="url(#fy14nu-hy-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="519" cy="103" r="22" fill="url(#fy14nu-hy-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="500" cy="72" r="22" fill="url(#fy14nu-hy-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="490" y1="72" x2="510" y2="72" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <line x1="500" y1="62" x2="500" y2="82" stroke="#ffffff" stroke-width="3.52" stroke-linecap="round"/>
  <foreignObject x="69.5" y="149.5" width="61" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:34px">${}^{1}_{1}\text{H}$</div></foreignObject>
  <foreignObject x="28.5" y="206.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{hydrogen-1}$</div></foreignObject>
  <foreignObject x="55.5" y="242.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#2b8a3e">$\text{stable}$</div></foreignObject>
  <foreignObject x="269.5" y="149.5" width="61" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:34px">${}^{2}_{1}\text{H}$</div></foreignObject>
  <foreignObject x="235" y="206.5" width="130" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{deuterium}$</div></foreignObject>
  <foreignObject x="255.5" y="242.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#2b8a3e">$\text{stable}$</div></foreignObject>
  <foreignObject x="469.5" y="149.5" width="61" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:34px">${}^{3}_{1}\text{H}$</div></foreignObject>
  <foreignObject x="448.5" y="206.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{tritium}$</div></foreignObject>
  <foreignObject x="426.5" y="242.5" width="147" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$T_{1/2} = 12.3\ \text{a}$</div></foreignObject>
  <line x1="200" y1="30" x2="200" y2="280" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="30" x2="400" y2="280" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
</svg>

About one hydrogen atom in $6400$ on Earth is deuterium, so every litre of water contains some. Tritium is radioactive, with a **half-life** of $12.3$ years, so there is almost none in nature.

## Formula: Mass number and nuclear notation

The **mass number** $A$ is the total number of nucleons:
```latex
A = Z + N
```
A nucleus is written in **nuclear notation** as $^{A}_{Z}\text{X}$, where $\text{X}$ is the chemical symbol. The symbol and $Z$ always belong together, so $Z$ is sometimes left out: $^{14}\text{C}$ or "carbon-14" means the same as $^{14}_{6}\text{C}$.

<svg data-fig="notation" viewBox="0 0 600 300" role="img" aria-label="Diagram of nuclear notation, using carbon-14 as the example. In the middle the large chemical symbol C. Top left, the mass number 14, with a label: mass number A, the number of protons plus neutrons. Bottom left, the atomic number 6, with a label: atomic number Z, the number of protons. A label on the right says that the symbol names the element, and that Z and the symbol always belong together. Below: N = A − Z = 8 neutrons." style="max-width:100%;font-size:26px">
  <foreignObject x="337" y="72" width="110" height="156" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:130px">$\text{C}$</div></foreignObject>
  <foreignObject x="257" y="50.5" width="80" height="67" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:56px">$14$</div></foreignObject>
  <foreignObject x="287" y="180.5" width="50" height="67" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:56px">$6$</div></foreignObject>
  <foreignObject x="16" y="36.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{mass number}$</div></foreignObject>
  <foreignObject x="16" y="70.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$A = Z + N$</div></foreignObject>
  <line x1="160" y1="86" x2="240" y2="86" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M252,86 L239,92 L239,80 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="16" y="184.5" width="170" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{atomic number}$</div></foreignObject>
  <foreignObject x="16" y="218.5" width="147" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$Z\ (\text{protons})$</div></foreignObject>
  <line x1="196" y1="214" x2="270" y2="214" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M282,214 L269,220 L269,208 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="480" y1="150" x2="464" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M452,150 L465,144 L465,156 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="484" y="102.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{chemical}$</div></foreignObject>
  <foreignObject x="484" y="134.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{symbol}$</div></foreignObject>
  <foreignObject x="484" y="166.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$(\text{by } Z)$</div></foreignObject>
  <foreignObject x="328.5" y="262.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$N = A - Z = 8$</div></foreignObject>
</svg>

The mass number is a count, not a mass, although it is close to the mass in $\text{u}$.

## The force that holds the nucleus {Forces}

Inside a nucleus, protons are only about $1\text{–}2\ \text{fm}$ apart ($1\ \text{fm} = 10^{-15}\ \text{m}$). There the electric repulsion of two protons is huge, about $58\ \text{N}$ at $2\ \text{fm}$. Gravity between them is about $10^{36}$ times weaker.

The nucleus is held by a different force, the **strong nuclear force**. It attracts any two nucleons, protons and neutrons alike, and it beats the electric repulsion when they nearly touch. But it has a very **short range**: it fades out by about $2.5\ \text{fm}$. Below about $0.7\ \text{fm}$ it repels, so nucleons cannot be squeezed together.

<svg data-fig="ranges" viewBox="0 0 600 350" role="img" aria-label="Schematic bar diagram along an axis of distance r between the centres of two nucleons, from 0 to 10 femtometres. Top bar, green: the strong nuclear force attracts from about 0.7 fm and fades out by about 2.5 fm; below 0.7 fm it repels (a hatched grey part). Middle bar, red: the electric repulsion between two protons acts at every distance and continues past the end of the axis, getting weaker with distance. Bottom: a bracket shows the diameter of an iron-56 nucleus, about 9.2 fm, much wider than the reach of the strong force." style="max-width:100%;font-size:26px">
  <defs><linearGradient id="fy14nu-r-g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2b8a3e"/><stop offset="0.6" stop-color="#2b8a3e"/><stop offset="1" stop-color="#2b8a3e" stop-opacity="0.05"/></linearGradient><pattern id="fy14nu-r-h" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#e3dccb"/><line x1="0" y1="0" x2="0" y2="10" stroke="#6b7480" stroke-width="3"/></pattern><linearGradient id="fy14nu-r-e" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c92a2a"/><stop offset="0.65" stop-color="#c92a2a"/><stop offset="1" stop-color="#c92a2a" stop-opacity="0.25"/></linearGradient></defs>
  <line x1="40" y1="300" x2="514" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,300 L513,306 L513,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="40" y1="300" x2="40" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$0$</div></foreignObject>
  <line x1="132" y1="300" x2="132" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="121" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$2$</div></foreignObject>
  <line x1="224" y1="300" x2="224" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="213" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$4$</div></foreignObject>
  <line x1="316" y1="300" x2="316" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="305" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$6$</div></foreignObject>
  <line x1="408" y1="300" x2="408" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="397" y="312.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$8$</div></foreignObject>
  <line x1="500" y1="300" x2="500" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="482.5" y="312.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10$</div></foreignObject>
  <foreignObject x="524" y="258.5" width="80" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$r\ (\text{fm})$</div></foreignObject>
  <rect x="40" y="56" width="32" height="40" fill="url(#fy14nu-r-h)" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="72" y="56" width="83" height="40" fill="url(#fy14nu-r-g)" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="169" y="46.5" width="278" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#2b8a3e">$\text{strong force: attracts}$</div></foreignObject>
  <foreignObject x="169" y="76.5" width="224" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{(any two nucleons)}$</div></foreignObject>
  <foreignObject x="42" y="14.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{repels}$</div></foreignObject>
  <path d="M40,126 H500 V118 L522,146 L500,174 V166 H40 Z" fill="url(#fy14nu-r-e)" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="58.5" y="130.5" width="278" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#ffffff">$\text{electric force: repels}$</div></foreignObject>
  <foreignObject x="58.5" y="176.5" width="332" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{(two protons, any distance)}$</div></foreignObject>
  <path d="M40,256 V270 H462.5 V256" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="110" y="220.5" width="282" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{diameter of }{}^{56}\text{Fe} \approx 9.2\ \text{fm}$</span></div></foreignObject>
</svg>

So each nucleon is held only by its nearest neighbours, but each proton is pushed by *every* other proton in the nucleus. Neutrons add attraction without adding repulsion. This is why light stable nuclei have $N \approx Z$, but heavy stable nuclei need more neutrons than protons. Above lead, no amount of neutrons makes a nucleus fully stable.

## Worked example

An iron-56 nucleus, $^{56}_{26}\text{Fe}$, has the mass $m = 9.29 \cdot 10^{-26}\ \text{kg}$. Its radius can be estimated with $R = r_0 A^{1/3}$, where $r_0 = 1.2\ \text{fm}$. How many protons and neutrons does it have, how large is it, and what is the density of the nucleus?

<!-- vaihe -->

**Given:** mass number $A = 56$, atomic number $Z = 26$, mass ${m = 9.29 \cdot 10^{-26}\ \text{kg}}$, ${r_0 = 1.2\ \text{fm}}$. **Find:** the number of protons $Z$, the number of neutrons $N$, the radius $R$ and the density $\rho$.

<!-- vaihe -->

**Principle:** The lower number in the notation is the number of protons, the upper one the number of nucleons, $A = Z + N$. A nucleus is close to a sphere, so its volume is $V = \frac{4}{3}\pi R^3$, and the density is mass divided by volume.

<!-- vaihe -->

**Formula:** Solved in symbols:
```latex
\begin{aligned}
N &= A - Z \\
R &= r_0 A^{1/3} \\
\rho &= \frac{m}{V} = \frac{3m}{4\pi R^3}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** ${r_0 = 1.2\ \text{fm} = 1.2 \cdot 10^{-15}\ \text{m}}$, so that the density comes out in $\text{kg/m}^3$.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
N &= 56 - 26 = 30 \\[4pt]
R &= 1.2 \cdot 10^{-15}\ \text{m} \cdot 56^{1/3} \\
&= 1.2 \cdot 10^{-15}\ \text{m} \cdot 3.826 \\
&= 4.59 \cdot 10^{-15}\ \text{m} \\[4pt]
\rho &= \frac{3 \cdot 9.29 \cdot 10^{-26}\ \text{kg}}{4\pi \cdot (4.59 \cdot 10^{-15}\ \text{m})^3} \\
&= 2.29 \cdot 10^{17}\ \text{kg/m}^3
\end{aligned}
```

<!-- vaihe -->

**Answer:** The nucleus has $26$ protons and $30$ neutrons. Its radius is about $4.6\ \text{fm}$ and its density about $2 \cdot 10^{17}\ \text{kg/m}^3$. The density is given to one significant figure, because $R = r_0 A^{1/3}$ is only an estimate: a nucleus has no sharp surface.

<!-- vaihe -->

**Reasonableness:** The density of solid iron is about $7900\ \text{kg/m}^3$. The nucleus is about $3 \cdot 10^{13}$ times denser, which fits: almost all of the mass of an atom sits in a volume $10^{13}\text{–}10^{14}$ times smaller than the atom. A teaspoon ($5\ \text{cm}^3$) of nuclear matter would have a mass of about $10^{12}\ \text{kg}$.

## The people behind the neutron {People}

### James Chadwick (1891–1974)

<figure class="unit-photo"><img src="units/fy14/pics/chadwick.jpg" alt="Black-and-white photograph of four men talking at a table; one of them, General Groves, is in army uniform." width="600" height="460" loading="lazy"><figcaption>James Chadwick (left), discoverer of the neutron in 1932, with General Leslie Groves, Richard Tolman and Henry DeWolf Smyth during the Manhattan Project, the wartime US atomic bomb programme. <span class="photo-credit">Photo: United States Army Signal Corps, public domain, via Wikimedia Commons</span></figcaption></figure>

James Chadwick was an English physicist who studied under Ernest Rutherford in Manchester and followed him to the Cavendish Laboratory in Cambridge. Rutherford had suggested that the nucleus might contain a neutral particle, but nobody had found it. In 1932 Chadwick aimed the radiation from polonium and beryllium at paraffin wax and measured the protons that it knocked out. Only a neutral particle with about the mass of a proton explained the results. In February 1932 he reported "the possible existence of a neutron". He received the Nobel Prize in Physics in 1935.

## Common misconception

"Isotopes are different elements." No: isotopes have the same $Z$ and so belong to the same element. Only the number of neutrons, and so the mass, is different. If the number of protons changes, the element changes.

"The mass number is the mass of the nucleus." The mass number is a whole number that counts nucleons. The real mass of $^{56}\text{Fe}$ is not $56\ \text{u}$, and in the next unit you will see why the difference matters.

"The neutrons hold the nucleus together by cancelling the charge of the protons." A neutron has no charge, so it cannot cancel anything. It helps because the strong force also acts on it.

## Summary

- A nucleus contains $Z$ protons and $N$ neutrons; the mass number is $A = Z + N$, written $^{A}_{Z}\text{X}$.
- $Z$ decides the element. Isotopes of an element have the same $Z$ but different $N$.
- Hydrogen-1, deuterium $^{2}_{1}\text{H}$ and tritium $^{3}_{1}\text{H}$ are the isotopes of hydrogen; tritium is radioactive.
- The nucleus is about $10^{-15}\text{–}10^{-14}\ \text{m}$ across, and nuclear matter has a density of about $2 \cdot 10^{17}\ \text{kg/m}^3$.
- The strong nuclear force attracts all nucleons but only over about $2.5\ \text{fm}$; the electric repulsion of protons reaches across the whole nucleus. That is why heavy nuclei need extra neutrons.
