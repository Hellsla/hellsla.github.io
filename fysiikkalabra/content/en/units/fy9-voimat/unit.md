# Newton's laws and the free-body diagram

> **Why** can a car set a trailer moving, even though the trailer pulls the car backwards with a force as large as the force with which the car pulls the trailer forwards?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an autumn afternoon by a lake. On the road in the foreground a red car pulls a small trailer loaded with firewood. The car and the trailer are joined by a drawbar. Behind the road there is a lake with forest on the far shore, and birches and spruces grow along the road." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9vo-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe3f1"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><linearGradient id="fy9vo-lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#7fb3dc"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy9vo-sky)"/>
  <path d="M151,112 Q149,74.5 193,79 Q210.5,39.5 254.5,52.5 Q294,30.5 316,72.5 Q355.5,77 351,112 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M819,88 Q817,57.5 853,61 Q867.5,28.5 903.5,39.5 Q936,21.5 954,55.5 Q986.5,59 983,88 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M557,154 Q555.5,130 583.5,133 Q595,108 623,116 Q648,102 662,129 Q687,131.5 684.5,154 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,300 L13,276 L26.5,300 L39.5,276.5 L52.5,300 L73.5,256.5 L94.5,300 L112,265.5 L129.5,300 L149.5,259.5 L169.5,300 L185,269.5 L201,300 L220.5,260.5 L240,300 L252.5,278 L265,300 L285.5,258 L305.5,300 L327,255.5 L348.5,300 L362,275.5 L375.5,300 L396.5,256 L418,300 L431,277 L443.5,300 L461,266 L478.5,300 L499.5,256.5 L520.5,300 L538.5,265 L556,300 L575,261.5 L594,300 L614.5,258.5 L634.5,300 L654,261 L673,300 L695,254.5 L717,300 L731,274 L745.5,300 L764,262 L783,300 L796.5,275 L810,300 L822.5,277.5 L835.5,300 L853.5,263.5 L872,300 L891.5,260 L911,300 L931,259 L951.5,300 L965,275 L978.5,300 L994,271.5 L1009,300 L1023.5,272 L1038.5,300 L1050.5,278.5 L1062.5,300 L1077,273.5 L1091.5,300 L1108.5,266.5 L1125.5,300 L1142,268.5 L1158,300 L1175,266.5 L1192,300 L1211.5,260.5 L1231,300 V324 H0 Z" fill="#3f6b4f" stroke-linejoin="round"/>
  <rect x="0" y="300" width="1200" height="110" fill="url(#fy9vo-lake)"/>
  <line x1="80" y1="330" x2="300" y2="330" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="420" y1="352" x2="700" y2="352" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="820" y1="336" x2="1100" y2="336" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="160" y1="384" x2="460" y2="384" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="760" y1="392" x2="1040" y2="392" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <path d="M0,410 Q300,398 600,406 T1200,404 V600 H0 Z" fill="#b9c98a" stroke-linejoin="round"/>
  <path d="M0,440 L1200,432 L1200,540 L0,548 Z" fill="#8a8f96" stroke-linejoin="round"/>
  <rect x="30" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="170" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="310" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="450" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="590" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="730" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="870" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="1010" y="487" width="70" height="6" fill="#ffffff"/>
  <rect x="1150" y="487" width="70" height="6" fill="#ffffff"/>
  <path d="M0,548 L1200,540 V600 H0 Z" fill="#a3b86c" stroke-linejoin="round"/>
  <rect x="64.5" y="250" width="11.5" height="190" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="64.5" y="417" width="5.5" height="3" fill="#1f2933"/>
  <rect x="70" y="394.5" width="5.5" height="3" fill="#1f2933"/>
  <rect x="64.5" y="371.5" width="5.5" height="3" fill="#1f2933"/>
  <rect x="70" y="349" width="5.5" height="3" fill="#1f2933"/>
  <rect x="64.5" y="326" width="5.5" height="3" fill="#1f2933"/>
  <rect x="70" y="303" width="5.5" height="3" fill="#1f2933"/>
  <rect x="64.5" y="280.5" width="5.5" height="3" fill="#1f2933"/>
  <line x1="70" y1="322" x2="36" y2="299.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="70" y1="297.5" x2="104" y2="274.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="70" y1="278.5" x2="36" y2="255.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="70" cy="259.5" r="38" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="41.5" cy="288" r="30.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="98.5" cy="284" r="32.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="70" cy="303" r="28.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="1113.5" y="226" width="12.5" height="210" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1113.5" y="411" width="6.5" height="3" fill="#1f2933"/>
  <rect x="1120" y="385.5" width="6.5" height="3" fill="#1f2933"/>
  <rect x="1113.5" y="360.5" width="6.5" height="3" fill="#1f2933"/>
  <rect x="1120" y="335" width="6.5" height="3" fill="#1f2933"/>
  <rect x="1113.5" y="310" width="6.5" height="3" fill="#1f2933"/>
  <rect x="1120" y="285" width="6.5" height="3" fill="#1f2933"/>
  <rect x="1113.5" y="259.5" width="6.5" height="3" fill="#1f2933"/>
  <line x1="1120" y1="306" x2="1082" y2="280.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1120" y1="278.5" x2="1158" y2="253.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1120" y1="257.5" x2="1082" y2="232.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1120" cy="236.5" r="42" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1088.5" cy="268" r="33.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1151.5" cy="264" r="35.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1120" cy="285" r="31.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="1004" y="418" width="12" height="18" fill="#b8622d"/>
  <path d="M956,421 L1010,361 L1064,421 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1010,361 L1064,421 H1010 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M968,388 L1010,328 L1052,388 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1010,328 L1052,388 H1010 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M980,355 L1010,286 L1040,355 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1010,286 L1040,355 H1010 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="165" y="425.5" width="9.5" height="14.5" fill="#b8622d"/>
  <path d="M127,428 L170,380 L213,428 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M170,380 L213,428 H170 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M136.5,401.5 L170,353.5 L203.5,401.5 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M170,353.5 L203.5,401.5 H170 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M146,375 L170,320 L194,375 Z" fill="#2b6a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M170,320 L194,375 H170 Z" fill="#1f2933" fill-opacity="0.18"/>
  <circle cx="103" cy="418.5" r="4" fill="#f2c94c"/>
  <circle cx="214.5" cy="430" r="4" fill="#f2c94c"/>
  <circle cx="165" cy="424.5" r="4" fill="#f2c94c"/>
  <circle cx="947.5" cy="419.5" r="4" fill="#f2c94c"/>
  <circle cx="263" cy="421" r="4" fill="#f2c94c"/>
  <circle cx="250.5" cy="430.5" r="4" fill="#f2c94c"/>
  <circle cx="802" cy="428.5" r="4" fill="#f2c94c"/>
  <circle cx="1083.5" cy="419" r="4" fill="#f2c94c"/>
  <circle cx="792.5" cy="424" r="4" fill="#f2c94c"/>
  <circle cx="1132.5" cy="430" r="4" fill="#f2c94c"/>
  <circle cx="1016.5" cy="429.5" r="4" fill="#f2c94c"/>
  <circle cx="631" cy="423" r="4" fill="#f2c94c"/>
  <circle cx="1072" cy="428.5" r="4" fill="#f2c94c"/>
  <circle cx="628.5" cy="424" r="4" fill="#f2c94c"/>
  <rect x="250" y="430" width="230" height="62" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <line x1="250" y1="446" x2="480" y2="446" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="270" cy="418" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="270" cy="418" r="5" fill="#a97a35"/>
  <circle cx="300" cy="418" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="300" cy="418" r="5" fill="#a97a35"/>
  <circle cx="330" cy="418" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="330" cy="418" r="5" fill="#a97a35"/>
  <circle cx="360" cy="418" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="360" cy="418" r="5" fill="#a97a35"/>
  <circle cx="390" cy="418" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="390" cy="418" r="5" fill="#a97a35"/>
  <circle cx="420" cy="418" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="420" cy="418" r="5" fill="#a97a35"/>
  <circle cx="450" cy="418" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="450" cy="418" r="5" fill="#a97a35"/>
  <circle cx="285" cy="394" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="285" cy="394" r="5" fill="#a97a35"/>
  <circle cx="315" cy="394" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="315" cy="394" r="5" fill="#a97a35"/>
  <circle cx="345" cy="394" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="345" cy="394" r="5" fill="#a97a35"/>
  <circle cx="375" cy="394" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="375" cy="394" r="5" fill="#a97a35"/>
  <circle cx="405" cy="394" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="405" cy="394" r="5" fill="#a97a35"/>
  <circle cx="435" cy="394" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="435" cy="394" r="5" fill="#a97a35"/>
  <circle cx="300" cy="370" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="300" cy="370" r="5" fill="#a97a35"/>
  <circle cx="330" cy="370" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="330" cy="370" r="5" fill="#a97a35"/>
  <circle cx="360" cy="370" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="360" cy="370" r="5" fill="#a97a35"/>
  <circle cx="390" cy="370" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="390" cy="370" r="5" fill="#a97a35"/>
  <circle cx="420" cy="370" r="14" fill="#d9b26a" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="420" cy="370" r="5" fill="#a97a35"/>
  <rect x="470" y="470" width="120" height="8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="365" cy="496" r="26" fill="#1f2933"/>
  <circle cx="365" cy="496" r="11" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M580,500 L580,452 Q584,436 606,432 L660,428 L712,384 Q726,372 750,372 L846,372 Q868,372 884,390 L924,428 L968,436 Q994,442 996,466 L996,500 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M720,426 L752,388 Q760,382 772,382 L800,382 L800,426 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M812,382 L842,382 Q858,382 868,394 L896,426 L812,426 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="806" y1="432" x2="806" y2="494" stroke="#a32222" stroke-width="2" stroke-linecap="butt"/>
  <rect x="976" y="448" width="16" height="12" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="584" y="446" width="10" height="14" rx="2" fill="#ffd8a8" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="660" cy="496" r="30" fill="#1f2933"/>
  <circle cx="660" cy="496" r="13" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="914" cy="496" r="30" fill="#1f2933"/>
  <circle cx="914" cy="496" r="13" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M220,526 Q600,534 1010,524" fill="none" stroke="#757b82" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
</svg>

## Key idea

Every task in this lesson is solved in the same way: **first the free-body diagram, then the equation of motion**. Choose the object, list its interactions and draw one force for each. In the free-body diagram the object is a rectangle, and each force starts from its point of application. Then choose the axes and write Newton's second law along each axis. In the exam, points for the free-body diagram are lost for a missing force, an extra force or a force drawn in the wrong direction.

<svg data-fig="kartta" viewBox="0 0 380 640" role="img" aria-label="Concept map. At the top is the node free-body diagram first: choose the object, find the interactions, draw the free-body diagram, choose the axes and write the equations of motion. Three branches go down from it. Newton&#x27;s laws: first law, sum F is zero when the velocity is constant; second law sum F = m a; third law F A B = − F B A. Forces: weight G = m g, kinetic friction F mu = mu N and static friction at most mu zero N, air resistance opposes the motion. Special cases: on a slope G x = m g sin alpha, connected bodies have an equation each, and at terminal velocity F v = G." style="max-width:100%;font-size:21px">
  <line x1="24" y1="120" x2="24" y2="494" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="112" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="66" y="17.5" width="248" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{free-body diagram first}$</div></foreignObject>
  <foreignObject x="92" y="50.5" width="196" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:19px">$\text{object} \to \text{interactions}$</div></foreignObject>
  <foreignObject x="122" y="82.5" width="136" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:19px">$\to \text{axes} \to \Sigma F_x = ma_x$</div></foreignObject>
  <line x1="24" y1="162" x2="44" y2="162" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="140" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="149.5" width="150" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\textbf{Newton's laws}$</div></foreignObject>
  <line x1="54" y1="182" x2="362" y2="182" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="193.5" width="74" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <foreignObject x="142" y="196" width="220" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{I: rest or constant velocity}$</div></foreignObject>
  <foreignObject x="58" y="227.5" width="84" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\Sigma\overline{F} = m\overline{a}$</div></foreignObject>
  <foreignObject x="336" y="230" width="26" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{II}$</div></foreignObject>
  <foreignObject x="58" y="261.5" width="117" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\overline{F}_{AB} = -\overline{F}_{BA}$</div></foreignObject>
  <foreignObject x="327" y="264" width="35" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{III}$</div></foreignObject>
  <line x1="24" y1="328" x2="44" y2="328" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="306" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="315.5" width="84" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\textbf{forces}$</div></foreignObject>
  <line x1="54" y1="348" x2="362" y2="348" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="359.5" width="52" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$G = mg$</div></foreignObject>
  <foreignObject x="301" y="362" width="61" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{weight}$</div></foreignObject>
  <foreignObject x="58" y="393.5" width="63" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$F_\mu = \mu N$</div></foreignObject>
  <foreignObject x="221" y="396" width="141" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{kinetic friction}$</div></foreignObject>
  <foreignObject x="58" y="427.5" width="84" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$F_{\mu 0} \le \mu_0 N$</div></foreignObject>
  <foreignObject x="230" y="430" width="132" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{static friction}$</div></foreignObject>
  <line x1="24" y1="494" x2="44" y2="494" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="472" width="328" height="150" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="481.5" width="150" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\textbf{special cases}$</div></foreignObject>
  <line x1="54" y1="514" x2="362" y2="514" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="525.5" width="84" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$G_x = mg\sin\alpha$</div></foreignObject>
  <foreignObject x="310" y="528" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{slope}$</div></foreignObject>
  <foreignObject x="58" y="559.5" width="95" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\Sigma F_x = m_i a_x$</div></foreignObject>
  <foreignObject x="274" y="562" width="88" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{connected}$</div></foreignObject>
  <foreignObject x="58" y="593.5" width="52" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$F_\text{v} = G$</div></foreignObject>
  <foreignObject x="213" y="596" width="149" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{terminal velocity}$</div></foreignObject>
</svg>

The opening question is settled by the choice of object. The car and the trailer act on each other with equal forces, but the forces act on **different objects**, so they do not cancel each other. The motion of the trailer is decided only by the forces acting on the trailer: while accelerating, the drawbar pulls it forwards more than the rolling resistance holds it back.

## Formula: Newton's laws and forces

### Newton's laws

```kaavat
Newton's first law (law of inertia) :: \Sigma\overline{F} = \overline{0} \ \Leftrightarrow\ \overline{v} = \text{constant}
Newton's second law (fundamental law of dynamics) :: \Sigma\overline{F} = m\overline{a}
Newton's third law (action and reaction) :: \overline{F}_{AB} = -\overline{F}_{BA}
```

where $\Sigma\overline{F}$ is the sum of the forces acting on the object ($\text{N}$), $m$ the mass ($\text{kg}$), $\overline{a}$ the acceleration ($\text{m/s}^2$) and $\overline{F}_{AB}$ the force with which A acts on B. In a calculation the second law is written in components, $\Sigma F_x = ma_x$ and $\Sigma F_y = ma_y$, and the components of an oblique force are $F\cos\alpha$ and $F\sin\alpha$. The net force points in the direction of the acceleration, not always in the direction of the velocity.

### Weight, friction and the slope

```kaavat
weight of a body at the Earth's surface :: G = mg
kinetic friction :: F_\mu = \mu N
static friction :: F_{\mu 0} \le \mu_0 N
```

where $g = 9.81\,\text{m/s}^2$, $N$ is the normal force ($\text{N}$), $\mu$ the coefficient of kinetic friction and $\mu_0$ the coefficient of static friction. Static friction is only as large as the situation requires, and it opposes the sliding of the surfaces relative to each other, not always the motion. The formulas are experimental models for dry surfaces. In free-body diagrams $\overline{F}_\mu$ stands for either kind of friction, static or kinetic.

On a slope with the angle of inclination $\alpha$, the components of the weight are $G_x = mg\sin\alpha$ down the slope and $G_y = mg\cos\alpha$ towards the slope. When only the weight and the normal force act perpendicular to the surface, $N = mg\cos\alpha$. The components are not new forces: they are drawn with dashed lines and replace the weight in the calculation.

<svg data-fig="kalteva" viewBox="0 0 600 380" role="img" aria-label="Two pictures. On the left the situation: a plastic sledge slides down a snowy slope to the left. The slope rises to the right at the angle alpha to the horizontal. Above the sledge a blue velocity arrow and an orange acceleration arrow point down the slope. On the right the free-body diagram of the sledge, the sledge as a rectangle tilted parallel to the slope: the weight G straight down from the centre, the normal force N from the bottom surface perpendicular to the slope and outwards, and kinetic friction F mu from the upper corner of the bottom surface up the slope. The components of the weight are drawn with dashed lines from the centre: G x down the slope and G y perpendicular to the slope, towards it. The component G y is as long as the normal force, and G x is clearly longer than the friction, so the sum of the forces points down the slope. The lengths of the arrows are to scale." style="max-width:100%;font-size:28px">
  <foreignObject x="38.5" y="5" width="183" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{the situation}$</div></foreignObject>
  <path d="M22,316 L248.5,210.5 L248.5,334 L22,334 Z" fill="#f8fbfd" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M52,324 L238.5,324" fill="none" stroke="#d7e3ec" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M89,284.5 L172.5,246 L173.5,215.5 L163.5,217 L76.5,257.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="91" y1="265.5" x2="160" y2="233.5" stroke="#d0e6fb" stroke-width="3" stroke-linecap="round"/>
  <line x1="137.5" y1="199.5" x2="81.5" y2="225.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="79.5" y1="226.5" x2="92.5" y2="226.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="79.5" y1="226.5" x2="87.5" y2="216" stroke="#1971c2" stroke-width="2.5" stroke-linecap="round"/>
  <foreignObject x="153.5" y="174.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="119" y1="159.5" x2="62.5" y2="185.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="61" y1="186.5" x2="74" y2="186.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="61" y1="186.5" x2="69" y2="176.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="round"/>
  <foreignObject x="135" y="134.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M80,316 A58,58 0 0 0 74.5,291.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="92.5" y="285" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$\alpha$</div></foreignObject>
  <line x1="276" y1="20" x2="276" y2="360" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="329.5" y="5" width="241" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <rect x="394" y="147" width="100" height="58" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-25 444 176)"/>
  <line x1="444" y1="176" x2="444" y2="304" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M444,321 L436,303 L452,303 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="409.5" y="326" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="474.5" y1="194" x2="426" y2="90" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M419,74.5 L434,87.5 L419,94.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="388.5" y="45.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="501.5" y1="181" x2="504" y2="180" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M519.5,173 L506.5,188 L499.5,173 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="509.5" y="142" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="444" y1="176" x2="390.5" y2="201" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M397.5,190.5 L388.5,202 L403,202.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="338.5" y="189" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="444" y1="176" x2="498.5" y2="293.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M488,286 L499.5,295 L500,280.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="501.5" y="284" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <path d="M444,220 A44,44 0 0 0 462.5,216" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="450.5" y="223" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$\alpha$</div></foreignObject>
</svg>

### Connected bodies and air resistance

For connected bodies, each body gets its own free-body diagram and its own equation of motion. A light, inextensible string and a light, frictionless pulley give the bodies accelerations of the same magnitude and tension forces of the same magnitude. Air resistance $\overline{F}_\text{v}$ points against the velocity and grows as the speed grows. At terminal velocity the acceleration is zero, so $F_\text{v} = G$.

## Common mistakes {Virheet}

- **A force in the direction of motion.** Nothing pushes a sliding object forwards. Every force has a cause, another object.
- **Force and counterforce in the same diagram.** They act on different objects and do not cancel each other.
- **$N = mg$ always.** On a slope, with an oblique pull and in an accelerating lift, the normal force is different from the weight.
- **$F_\mu = \mu_0 N$ at rest.** At rest friction is only as large as the situation requires; $\mu_0 N$ is its upper limit.
- **Connected bodies: $T = m_2 g$.** When the hanging body accelerates downwards, the tension in the string is smaller than its weight.
- **Components in addition to the forces.** If both the weight and its components are in the calculation, the weight is counted twice.

## Review if needed {Kertaa}

- The first and third laws: [*Interaction and force: Newton's first and third laws*](fy4-3.html). The second law: [*Newton's second law*](fy4-4.html).
- The eight steps of a free-body diagram and components: [*Free-body diagrams and the combined effect of forces*](fy4-5.html).
- Weight, static and kinetic friction and the slope: [*Weight, friction and the inclined plane*](fy4-6.html).
- String and pulley: [*Equation of motion for connected bodies*](fy4-13.html). Terminal velocity: [*Air resistance and falling through air*](fy4-14.html).
