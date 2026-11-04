# Mekaaninen energia ja liikemäärä

> **Miksi** kaksi yhteen kytkeytyvää junanvaunua jatkavat hitaammin kuin ennen kytkeytymistä, vaikka mikään ei jarruta niitä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen ratapiha metsän keskellä kirkkaana päivänä. Vasemmalla punaruskea katettu tavaravaunu rullaa oikealle, ja sen takana on liikeviivoja. Oikealla seisoo samanlainen vaunu, johon rullaava vaunu on kohta kytkeytymässä. Raiteiden yllä on sähköradan pylväitä ja ajojohdin, taustalla kuusimetsää ja lumipenkkoja." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9sl-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9cc4e4"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy9sl-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy9sl-sky)"/>
  <circle cx="1050" cy="96" r="64" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="1050" cy="96" r="40" fill="url(#fy9sl-sun)"/>
  <path d="M179,110 Q177,79.5 213,83 Q227.5,50.5 263.5,61.5 Q296,43.5 314,77.5 Q346.5,81 343,110 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M637,84 Q635.5,60 663.5,63 Q675,38 703,46 Q728,32 742,59 Q767,61.5 764.5,84 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,330 L22,284.5 L43.5,330 L64,288.5 L84,330 L96.5,308.5 L108.5,330 L121,308.5 L133,330 L153,288.5 L173.5,330 L186.5,307 L199,330 L213.5,302.5 L228,330 L241.5,305.5 L255,330 L273.5,292.5 L292.5,330 L308.5,298.5 L324.5,330 L344,290.5 L363.5,330 L384,288 L404.5,330 L423.5,291.5 L442.5,330 L463.5,287 L484.5,330 L501,297 L518,330 L538.5,288 L559,330 L574,301 L589.5,330 L610,287 L631,330 L650,292 L669,330 L690.5,285.5 L712,330 L729.5,294.5 L747.5,330 L768.5,287 L789.5,330 L803.5,304 L817.5,330 L831.5,304 L845.5,330 L863.5,293.5 L882,330 L894.5,307.5 L907,330 L928,286.5 L949.5,330 L969.5,289 L989.5,330 L1010,288 L1030.5,330 L1045,303 L1059.5,330 L1075,300.5 L1090.5,330 L1108.5,293.5 L1127,330 L1144.5,294.5 L1162.5,330 L1179,297.5 L1195.5,330 L1208.5,306 L1222,330 V354 H0 Z" fill="#3b6b4f" stroke-linejoin="round"/>
  <path d="M0,352 L19,314 L37.5,352 L50.5,327.5 L63.5,352 L78,325 L92,352 L107.5,323 L122.5,352 L134,331.5 L145.5,352 L161,321 L177,352 L190.5,327 L203.5,352 L219,322.5 L234.5,352 L248.5,325 L262.5,352 L276,326.5 L289.5,352 L307,317 L324.5,352 L337.5,327.5 L350.5,352 L368.5,316 L386.5,352 L404.5,315.5 L422.5,352 L442,312.5 L461,352 L475,325.5 L489,352 L502.5,326.5 L516,352 L527.5,331 L539.5,352 L552,329 L564.5,352 L581.5,317.5 L598.5,352 L610,332 L621.5,352 L632,334 L642.5,352 L659,319 L675.5,352 L692.5,318 L710,352 L724.5,323.5 L739.5,352 L755.5,320.5 L771.5,352 L786,324.5 L800,352 L816,321 L832,352 L843.5,331.5 L855,352 L874,313.5 L892.5,352 L907.5,323.5 L922,352 L936,326 L949.5,352 L967,317.5 L984.5,352 L998,325.5 L1012,352 L1031.5,313 L1050.5,352 L1066.5,320.5 L1082.5,352 L1099.5,318 L1116.5,352 L1130.5,326.5 L1144,352 L1158.5,323.5 L1173.5,352 L1191.5,315.5 L1209.5,352 V372 H0 Z" fill="#2f5a41" stroke-linejoin="round"/>
  <path d="M0,350 Q300,334 600,346 T1200,342 V600 H0 Z" fill="#f8fbfd" stroke-linejoin="round"/>
  <path d="M0,560 Q360,548 700,560 T1200,556 V600 H0 Z" fill="#e6eff5" stroke-linejoin="round"/>
  <rect x="0" y="392" width="1200" height="6.5" fill="#8a8172"/>
  <rect x="0" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="26" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="52" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="78" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="104" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="130" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="156" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="182" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="208" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="234" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="260" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="286" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="312" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="338" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="364" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="390" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="416" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="442" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="468" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="494" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="520" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="546" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="572" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="598" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="624" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="650" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="676" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="702" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="728" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="754" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="780" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="806" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="832" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="858" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="884" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="910" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="936" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="962" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="988" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1014" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1040" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1066" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1092" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1118" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1144" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1170" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="1196" y="393" width="10" height="5" fill="#5a4a3a"/>
  <rect x="0" y="390" width="1200" height="2" fill="#6c757d"/>
  <rect x="0" y="500" width="1200" height="12" fill="#6f6556"/>
  <rect x="0" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="42" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="84" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="126" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="168" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="210" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="252" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="294" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="336" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="378" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="420" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="462" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="504" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="546" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="588" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="630" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="672" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="714" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="756" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="798" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="840" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="882" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="924" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="966" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="1008" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="1050" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="1092" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="1134" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="1176" y="502" width="18" height="9" fill="#5a4a3a"/>
  <rect x="0" y="496" width="1200" height="4" fill="#6c757d"/>
  <rect x="120" y="170" width="10" height="330" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="125" y1="190" x2="250" y2="190" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="125" y1="214" x2="230" y2="190" stroke="#6c757d" stroke-width="2" stroke-linecap="butt"/>
  <rect x="520" y="170" width="10" height="330" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="525" y1="190" x2="650" y2="190" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="525" y1="214" x2="630" y2="190" stroke="#6c757d" stroke-width="2" stroke-linecap="butt"/>
  <rect x="920" y="170" width="10" height="330" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="925" y1="190" x2="1050" y2="190" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="925" y1="214" x2="1030" y2="190" stroke="#6c757d" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="206" x2="1200" y2="206" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="190" x2="1200" y2="190" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <rect x="1150" y="300" width="8" height="200" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1136" y="280" width="36" height="60" rx="6" fill="#1f2933"/>
  <circle cx="1154" cy="296" r="9" fill="#2b8a3e"/>
  <circle cx="1154" cy="324" r="9" fill="#4b5560"/>
  <rect x="690" y="344" width="420" height="118" rx="4" fill="#9c3b2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="716" y1="350" x2="716" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="742" y1="350" x2="742" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="768" y1="350" x2="768" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="794" y1="350" x2="794" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="820" y1="350" x2="820" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="846" y1="350" x2="846" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="872" y1="350" x2="872" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="898" y1="350" x2="898" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="924" y1="350" x2="924" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="950" y1="350" x2="950" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="976" y1="350" x2="976" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="1002" y1="350" x2="1002" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="1028" y1="350" x2="1028" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="1054" y1="350" x2="1054" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="1080" y1="350" x2="1080" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <rect x="816" y="354" width="75.5" height="98" fill="#9c3b2a" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="854" y1="354" x2="854" y2="452" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="879" y="397" width="8" height="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="908.5" y="354" width="75.5" height="98" fill="#9c3b2a" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="946" y1="354" x2="946" y2="452" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="971.5" y="397" width="8" height="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M686,344 Q900,322 1114,344 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M696,340 Q900,320 1104,340 Q900,330 696,340 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="684" y="462" width="432" height="10" fill="#1f2933"/>
  <rect x="713" y="468" width="88" height="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="733" cy="482" r="14" fill="#1f2933"/>
  <circle cx="733" cy="482" r="5" fill="#c4ccd4"/>
  <circle cx="781" cy="482" r="14" fill="#1f2933"/>
  <circle cx="781" cy="482" r="5" fill="#c4ccd4"/>
  <rect x="999" y="468" width="88" height="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1019" cy="482" r="14" fill="#1f2933"/>
  <circle cx="1019" cy="482" r="5" fill="#c4ccd4"/>
  <circle cx="1067" cy="482" r="14" fill="#1f2933"/>
  <circle cx="1067" cy="482" r="5" fill="#c4ccd4"/>
  <rect x="670" y="463" width="14" height="6" fill="#6c757d"/>
  <rect x="666" y="456" width="4" height="20" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="684" y1="470" x2="662" y2="474" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <rect x="1116" y="463" width="14" height="6" fill="#6c757d"/>
  <rect x="1130" y="456" width="4" height="20" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1116" y1="470" x2="1138" y2="474" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <rect x="150" y="344" width="420" height="118" rx="4" fill="#9c3b2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="176" y1="350" x2="176" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="202" y1="350" x2="202" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="228" y1="350" x2="228" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="254" y1="350" x2="254" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="280" y1="350" x2="280" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="306" y1="350" x2="306" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="332" y1="350" x2="332" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="358" y1="350" x2="358" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="384" y1="350" x2="384" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="410" y1="350" x2="410" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="436" y1="350" x2="436" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="462" y1="350" x2="462" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="488" y1="350" x2="488" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="514" y1="350" x2="514" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="540" y1="350" x2="540" y2="456" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <rect x="276" y="354" width="75.5" height="98" fill="#9c3b2a" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="314" y1="354" x2="314" y2="452" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="339" y="397" width="8" height="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="368.5" y="354" width="75.5" height="98" fill="#9c3b2a" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="406" y1="354" x2="406" y2="452" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="431.5" y="397" width="8" height="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M146,344 Q360,322 574,344 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M156,340 Q360,320 564,340 Q360,330 156,340 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="144" y="462" width="432" height="10" fill="#1f2933"/>
  <rect x="173" y="468" width="88" height="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="193" cy="482" r="14" fill="#1f2933"/>
  <circle cx="193" cy="482" r="5" fill="#c4ccd4"/>
  <circle cx="241" cy="482" r="14" fill="#1f2933"/>
  <circle cx="241" cy="482" r="5" fill="#c4ccd4"/>
  <rect x="459" y="468" width="88" height="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="479" cy="482" r="14" fill="#1f2933"/>
  <circle cx="479" cy="482" r="5" fill="#c4ccd4"/>
  <circle cx="527" cy="482" r="14" fill="#1f2933"/>
  <circle cx="527" cy="482" r="5" fill="#c4ccd4"/>
  <rect x="130" y="463" width="14" height="6" fill="#6c757d"/>
  <rect x="126" y="456" width="4" height="20" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="144" y1="470" x2="122" y2="474" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <rect x="576" y="463" width="14" height="6" fill="#6c757d"/>
  <rect x="590" y="456" width="4" height="20" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="576" y1="470" x2="598" y2="474" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="40" y1="380" x2="136" y2="380" stroke="#ffffff" stroke-width="9" stroke-linecap="round"/>
  <line x1="40" y1="380" x2="136" y2="380" stroke="#1971c2" stroke-width="4" stroke-linecap="round"/>
  <line x1="10" y1="412" x2="136" y2="412" stroke="#ffffff" stroke-width="9" stroke-linecap="round"/>
  <line x1="10" y1="412" x2="136" y2="412" stroke="#1971c2" stroke-width="4" stroke-linecap="round"/>
  <line x1="60" y1="444" x2="136" y2="444" stroke="#ffffff" stroke-width="9" stroke-linecap="round"/>
  <line x1="60" y1="444" x2="136" y2="444" stroke="#1971c2" stroke-width="4" stroke-linecap="round"/>
  <path d="M0,528 Q80,506 170,526 Q260,544 360,562 Q430,576 480,600 H0 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="29" y="539.5" width="13.5" height="20.5" fill="#b8622d"/>
  <path d="M-25,543 L36,475 L97,543 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M36,475 L97,543 H36 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M-11.5,505.5 L36,437.5 L83.5,505.5 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M36,437.5 L83.5,505.5 H36 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M2,468 L36,390 L70,468 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M36,390 L70,468 H36 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1176" y="542" width="12" height="18" fill="#b8622d"/>
  <path d="M1128,545 L1182,485 L1236,545 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1182,485 L1236,545 H1182 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1140,512 L1182,452 L1224,512 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1182,452 L1224,512 H1182 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1152,479 L1182,410 L1212,479 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1182,410 L1212,479 H1182 Z" fill="#1f2933" fill-opacity="0.18"/>
</svg>

## Ydinajatus

Mekaniikan kokeen tehtävistä suuri osa ratkeaa kahdella säilymislailla. **Energia säilyy aina**: mekaaninen energia muuttuu sisäenergiaksi, kun kitka, ilmanvastus tai kappaleen muodonmuutos tekee työtä, mutta kokonaisenergia pysyy samana. **Liikemäärä säilyy**, kun systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen aikana merkityksettömän pieni.

<svg data-fig="kartta" viewBox="0 0 380 604" role="img" aria-label="Käsitekartta. Ylhäällä solmu säilymislait: energia ja liikemäärä. Siitä lähtee alas kolme haaraa. Energia: liike-energia E k = puolet m v toiseen, potentiaalienergia E p = m g h ja energiaperiaate, jossa alun mekaaninen energia ja muiden voimien työ on yhtä suuri kuin lopun mekaaninen energia. Liikemäärä: p = m v vektoreina, impulssiperiaate summa F kertaa delta t = delta p ja liikemäärän säilyminen törmäyksessä. Sovellukset: törmäyksessä liikemäärä säilyy mutta liike-energia vain kimmoisassa, pysähtymismatka on reaktiomatka ja jarrutusmatka, ja vesivoimalan teho on eeta rho Q g h." style="max-width:100%;font-size:20px">
  <line x1="24" y1="80" x2="24" y2="454" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="123.5" y="18" width="133" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{säilymislait}$</div></foreignObject>
  <foreignObject x="87" y="47" width="206" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{energia ja liikemäärä}$</div></foreignObject>
  <line x1="24" y1="122" x2="44" y2="122" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="100" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="110" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\textbf{energia}$</div></foreignObject>
  <line x1="54" y1="142" x2="362" y2="142" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="154" width="102" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$E_\text{k} = \tfrac12 mv^2$</div></foreignObject>
  <foreignObject x="239" y="156" width="123" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{liike-energia}$</div></foreignObject>
  <foreignObject x="58" y="188" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$E_\text{p} = mgh$</div></foreignObject>
  <foreignObject x="195" y="190" width="167" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{potentiaalienergia}$</div></foreignObject>
  <foreignObject x="58" y="223" width="186" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px">$E_\text{mek,1} + W_\text{muut} = E_\text{mek,2}$</div></foreignObject>
  <line x1="24" y1="288" x2="44" y2="288" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="266" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="276" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\textbf{liikemäärä}$</div></foreignObject>
  <line x1="54" y1="308" x2="362" y2="308" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="320" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\overline{p} = m\overline{v}$</div></foreignObject>
  <foreignObject x="266" y="322" width="96" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{määritelmä}$</div></foreignObject>
  <foreignObject x="58" y="355" width="102" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px">$\Sigma\overline{F}\,\Delta t = \Delta\overline{p}$</div></foreignObject>
  <foreignObject x="283" y="356" width="79" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{impulssi}$</div></foreignObject>
  <foreignObject x="58" y="389" width="167" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px">$\overline{p}_\text{ennen} = \overline{p}_\text{jälkeen}$</div></foreignObject>
  <foreignObject x="266" y="390" width="96" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{säilyminen}$</div></foreignObject>
  <line x1="24" y1="454" x2="44" y2="454" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="432" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="442" width="133" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\textbf{sovellukset}$</div></foreignObject>
  <line x1="54" y1="474" x2="362" y2="474" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="487" width="233" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px">$\text{törmäys: } p \text{ säilyy, } E_\text{k} \text{ ei aina}$</div></foreignObject>
  <foreignObject x="58" y="521" width="158" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px">$s_\text{p} = v_0 t_\text{r} + v_0^2/(2a)$</div></foreignObject>
  <foreignObject x="248" y="522" width="114" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{pysähtyminen}$</div></foreignObject>
  <foreignObject x="58" y="554" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$P = \eta\rho Qgh$</div></foreignObject>
  <foreignObject x="274" y="556" width="88" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{vesivoima}$</div></foreignObject>
</svg>

Ratkaisu alkaa siitä, että valitset lain tilanteen mukaan. Kun kysytään nopeutta tai korkeutta eri kohdissa ja tunnetaan voimien tekemä työ, käytä energiaperiaatetta. Kun kappaleet törmäävät tai työntävät toisiaan, käytä liikemäärän säilymistä. Kun kysytään voimaa ja tunnetaan aika, käytä impulssiperiaatetta. Moni tehtävä yhdistää ne: ensin energia, sitten törmäys, sitten taas energia.

Tästä saadaan myös vastaus alun kysymykseen. Kytkeytymisessä vaunujen voimat toisiinsa ovat sisäisiä, joten liikemäärä $32\,000\,\text{kg} \cdot 1{,}6\,\text{m/s} = 51\,200\,\text{kg} \cdot \text{m/s}$ säilyy. Se jakautuu kaksinkertaiselle massalle, joten nopeus puolittuu, $0{,}80\,\text{m/s}$. Liike-energia $\tfrac12 mv^2$ pienenee silloin $41\,\text{kJ}$:sta $20\,\text{kJ}$:iin: puolet siitä muuttuu puskurien ja kytkimien sisäenergiaksi ja ääneksi.

<svg data-fig="tormays" viewBox="0 0 420 560" role="img" aria-label="Kaavakuva, nopeudet ja palkit mittakaavassa. Ylhäällä ennen törmäystä: vasen vaunu liikkuu oikealle nopeudella 1,6 m/s, sininen nuoli, ja oikea vaunu on levossa. Sen alla törmäyksen jälkeen: vaunut ovat kiinni toisissaan ja liikkuvat yhdessä nopeudella 0,80 m/s, puolet lyhyempi nuoli. Alhaalla palkit. Kokonaisliikemäärä on ennen ja jälkeen sama, 51 200 kilogrammametriä sekunnissa. Liike-energia on ennen 41 kJ ja jälkeen 20 kJ; puuttuva puolikas on muuttunut puskurien ja kytkimien sisäenergiaksi." style="max-width:100%;font-size:20px">
  <foreignObject x="8" y="10" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{ennen}$</div></foreignObject>
  <line x1="0" y1="130" x2="420" y2="130" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="20" y="60" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="42" cy="114" r="9" fill="#1f2933"/>
  <circle cx="108" cy="114" r="9" fill="#1f2933"/>
  <rect x="290" y="60" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="312" cy="114" r="9" fill="#1f2933"/>
  <circle cx="378" cy="114" r="9" fill="#1f2933"/>
  <line x1="75" y1="44" x2="222" y2="44" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M235,44 L221,50.5 L221,37.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="119.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#1971c2">$1{,}6\,\text{m/s}$</div></foreignObject>
  <foreignObject x="327" y="29" width="36" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$v = 0$</div></foreignObject>
  <foreignObject x="8" y="148" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{jälkeen}$</div></foreignObject>
  <line x1="0" y1="260" x2="420" y2="260" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="100" y="190" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="122" cy="244" r="9" fill="#1f2933"/>
  <circle cx="188" cy="244" r="9" fill="#1f2933"/>
  <rect x="214" y="190" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="236" cy="244" r="9" fill="#1f2933"/>
  <circle cx="302" cy="244" r="9" fill="#1f2933"/>
  <rect x="208" y="206" width="8" height="10" fill="#1f2933"/>
  <line x1="155" y1="176" x2="222" y2="176" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M235,176 L221,182.5 L221,169.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="290" y="152" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$0{,}80\,\text{m/s}$</div></foreignObject>
  <line x1="10" y1="500" x2="410" y2="500" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="40" y="340" width="52" height="160" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="110" y="340" width="52" height="160" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="230" y="340" width="52" height="160" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="420" width="52" height="80" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="340" width="52" height="80" fill="#dee2e6" stroke="#1f2933" stroke-width="1.5" stroke-dasharray="6 4"/>
  <foreignObject x="76" y="280" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_\text{kok}$</div></foreignObject>
  <foreignObject x="241.5" y="280" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="40" y="512" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="101" y="512" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="230" y="512" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="291" y="512" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="260" y="312" width="132" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#6b7480">$\text{sisäenergiaksi}$</div></foreignObject>
  <foreignObject x="39.5" y="308" width="123" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$51\,200\,\text{kg} \cdot \text{m/s}$</div></foreignObject>
  <foreignObject x="230" y="410" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$41\,\text{kJ}$</div></foreignObject>
  <foreignObject x="300" y="450" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$20\,\text{kJ}$</div></foreignObject>
</svg>

## Kaava: Mekaaninen energia ja liikemäärä

### Energia

```latex
\begin{aligned}
E_\text{k} &= \tfrac{1}{2}\,mv^2 \\
E_\text{p} &= mgh
\end{aligned}
```

missä $m$ on massa ($\text{kg}$), $v$ nopeus ($\text{m/s}$), $g = 9{,}81\,\text{m/s}^2$ ja $h$ korkeus valitusta nollatasosta ($\text{m}$). $E_\text{p} = mgh$ pätee Maan pinnan lähellä. Energiaperiaate on

```latex
E_{\text{k},1} + E_{\text{p},1} + W_\text{muut} = E_{\text{k},2} + E_{\text{p},2}
```

missä $W_\text{muut}$ on muiden voimien kuin painon tekemä työ ($\text{J}$). Vakiovoiman työ on $W = F_\parallel\,s$, missä $F_\parallel$ on voiman liikkeen suuntainen komponentti; kitkan ja ilmanvastuksen työ on negatiivinen. Kun $W_\text{muut} = 0$, mekaaninen energia säilyy.

### Liikemäärä ja impulssi

```latex
\begin{aligned}
\overline{p} &= m\overline{v} \\
\Sigma\overline{F}\,\Delta t &= \Delta\overline{p}
\end{aligned}
```

missä $\overline{p}$ on liikemäärä ($\text{kg} \cdot \text{m/s}$) ja $\Sigma\overline{F}$ vakiosuuruinen kokonaisvoima aikavälin $\Delta t$ ajan. Muuttuvalle voimalle keskimääräinen voima on $F_\text{ka} = |\Delta p| : \Delta t$. Yhdessä ulottuvuudessa valitaan positiivinen suunta, ja vastakkaiseen suuntaan osoittavat nopeudet ovat negatiivisia. Kun ulkoisten voimien impulssi on merkityksettömän pieni,

```latex
m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'
```

Kimmoisassa törmäyksessä myös liike-energia säilyy. Täysin kimmottomassa kappaleet jatkavat yhteisellä nopeudella, $v_1' = v_2' = v'$, ja liike-energiaa muuttuu eniten sisäenergiaksi.

### Sovellukset

Vaakasuoralla tiellä auton pysähtymismatka on reaktiomatka ja jarrutusmatka:

```latex
\begin{aligned}
s_\text{p} &= v_0\,t_\text{r} + \frac{v_0^2}{2a} \\
P_\text{vesi} &= \eta\rho Qgh \\
P_\text{tuuli} &= \tfrac12\eta\rho Av^3
\end{aligned}
```

missä $t_\text{r}$ on reaktioaika ($\text{s}$) ja $a$ hidastuvuus ($\text{m/s}^2$), oletettu vakioksi; lukkojarrutuksen rajalla $a = \mu g$. Voimaloiden sähkötehoissa $\eta$ on hyötysuhde ja $\rho$ veden tai ilman tiheys; vesivoimalassa $Q$ on virtaama ($\text{m}^3\text{/s}$) ja $h$ putouskorkeus ($\text{m}$), tuulivoimalassa $A$ on roottorin pyyhkäisemä pinta-ala ($\text{m}^2$) ja $v$ tuulen nopeus. Tuulen tehon lauseke pätee, kun hyötysuhde pysyy vakiona ja voimala toimii nimellistehoaan pienemmällä teholla.

## Yleisiä virheitä {Virheet}

- **Liike-energia ja liikemäärä sekaisin.** Törmäyksessä liikemäärä säilyy, liike-energia vain kimmoisassa törmäyksessä. Liikemäärä ei muutu lämmöksi: lämmöksi muuttuu energiaa.
- **Etumerkit unohtuvat.** Kimpoava pallo muuttaa liikemääräänsä enemmän kuin pysähtyvä: samalla nopeudella kimpoavalle pallolle $\Delta p = -mv - mv = -2mv$.
- **Kitka katoaa energiaperiaatteesta.** Kitkan työ on negatiivinen, ja se muuttaa mekaanista energiaa sisäenergiaksi; se ei synnytä eikä hävitä energiaa.
- **Kilometrit tunnissa sijoitetaan suoraan.** $72\,\text{km/h} = 72 \cdot \tfrac{1000\,\text{m}}{3600\,\text{s}} = 20\,\text{m/s}$, ennen kuin nopeus korotetaan toiseen.
- **Nopeuden neliö unohtuu.** Kaksinkertainen nopeus nelinkertaistaa liike-energian ja jarrutusmatkan, ja tuulen teho kasvaa kahdeksankertaiseksi.
- **Liikemäärän säilyminen ilman ehtoa.** Kerro, miksi ulkoiset voimat eivät muuta liikemäärää törmäyksen aikana.

## Kertaa tarvittaessa {Kertaa}

- Energialajit ja nollataso: [*Liike-energia, potentiaalienergia ja mekaaninen energia*](fy4-7.html). Työ ja energiaperiaate: [*Mekaanisen energian säilyminen ja energiaperiaate*](fy4-8.html).
- Voimalat: [*Vesi- ja tuulivoima energian muuntajina*](fy4-15.html).
- Liikemäärä, impulssi ja keskimääräinen voima: [*Liikemäärä ja impulssi*](fy4-9.html). Törmäykset: [*Liikemäärän säilyminen ja yksiulotteiset törmäykset*](fy4-10.html).
- Pysähtymismatka ja turvavarusteet: [*Liikenneturvallisuus: jarrutus, turvavyö ja turvatyyny*](fy4-11.html).
