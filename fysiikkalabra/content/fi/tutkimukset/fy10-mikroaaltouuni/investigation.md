# Valonnopeuden määrittäminen mikroaaltouunilla

> **Tutkimuskysymys:** Miten mikroaaltouunissa syntyvästä seisovasta aallosta voidaan määrittää mikroaaltojen aallonpituus, ja kuinka suureksi valonnopeus saadaan sen ja uunin taajuuden avulla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: mikroaaltouuni laboratorion työpöydällä. Uunin luukku on kiinni ja uuni on pois päältä. Luukun ikkunasta näkyy uunin pohjalla lautanen, jolle on levitetty tasainen kerros juustoraastetta, ja sen vieressä kuppi vettä. Pöydällä uunin vieressä on mitta-asteikko, patalappu ja kulho juustoraastetta." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10mh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10mh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy10mh-body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1f3f5"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><pattern id="fy10mh-mesh" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.6" fill="#000" fill-opacity="0.35"/></pattern></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10mh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10mh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="300" y="456" width="30" height="14" rx="3" fill="#1f2933"/>
  <rect x="830" y="456" width="30" height="14" rx="3" fill="#1f2933"/>
  <rect x="280" y="140" width="600" height="318" rx="14" fill="url(#fy10mh-body)" stroke="#1f2933" stroke-width="3"/>
  <rect x="700" y="160" width="160" height="278" rx="8" fill="#e9ecef" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="720" y="182" width="120" height="44" rx="5" fill="#343a40" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="745" cy="260" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="780" cy="260" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="815" cy="260" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="745" cy="294" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="780" cy="294" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="815" cy="294" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="745" cy="328" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="780" cy="328" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="815" cy="328" r="11" fill="#ffffff" stroke="#8a96a3" stroke-width="2.5"/>
  <circle cx="780" cy="392" r="22" fill="#ffffff" stroke="#8a96a3" stroke-width="3"/>
  <line x1="780" y1="392" x2="780" y2="374" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="296" y="156" width="392" height="286" rx="8" fill="#dee2e6" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="648" y="210" width="18" height="176" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="320" y="186" width="310" height="226" rx="6" fill="#2b3036" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="330" y="196" width="290" height="206" fill="#495057"/>
  <path d="M330,402 L360,330 L590,330 L620,402 Z" fill="#6c757d" stroke-linejoin="round"/>
  <ellipse cx="460" cy="370" rx="104" ry="24" fill="#f8f9fa" stroke="#ced4da" stroke-width="2.5"/>
  <ellipse cx="460" cy="368" rx="86" ry="17" fill="#ffe066"/>
  <line x1="455.5" y1="380.5" x2="447.5" y2="381" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="400" y1="374" x2="393.5" y2="375" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="432.5" y1="382.5" x2="440.5" y2="382.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="517" y1="360" x2="525" y2="360.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="432" y1="362.5" x2="425" y2="363" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="491.5" y1="363.5" x2="499" y2="364" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="430" y1="355.5" x2="435.5" y2="356.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="496" y1="374.5" x2="503.5" y2="375" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="501" y1="357" x2="497" y2="358" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="473" y1="368.5" x2="475" y2="369.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="452" y1="376" x2="446.5" y2="377" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="459.5" y1="354" x2="452.5" y2="354.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="417.5" y1="358.5" x2="413" y2="359.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="513.5" y1="378" x2="506" y2="378.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="499.5" y1="370.5" x2="499.5" y2="372" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="483" y1="380.5" x2="476" y2="381.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="386" y1="368" x2="390.5" y2="369.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="398.5" y1="372.5" x2="391" y2="373" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="482" y1="373" x2="477.5" y2="374" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="518" y1="369.5" x2="510" y2="370" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="507" y1="377" x2="505" y2="378.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="414.5" y1="359" x2="407" y2="359.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="468" y1="359.5" x2="474.5" y2="360.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="474" y1="376" x2="480.5" y2="377" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="490.5" y1="377.5" x2="487.5" y2="379" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="512" y1="375" x2="519.5" y2="375.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="544.5" y1="367" x2="537" y2="367.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="512.5" y1="372" x2="506" y2="373" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="473" y1="362.5" x2="466" y2="363.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="431.5" y1="371.5" x2="437" y2="372.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="459.5" y1="355" x2="463" y2="356.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="502" y1="355.5" x2="499" y2="356.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="394" y1="367.5" x2="392" y2="369" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="501" y1="378.5" x2="502" y2="380" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="421.5" y1="373" x2="429" y2="373.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="434.5" y1="356.5" x2="440" y2="357.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="537" y1="362" x2="529" y2="362" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="501" y1="376" x2="493" y2="376" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="418.5" y1="354.5" x2="425.5" y2="355" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="429.5" y1="375.5" x2="422" y2="376" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="411.5" y1="376.5" x2="417" y2="377.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="445" y1="363.5" x2="450.5" y2="364.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="510.5" y1="372.5" x2="504.5" y2="373.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="495" y1="370" x2="500.5" y2="371" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="470.5" y1="382" x2="462.5" y2="382" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="394.5" y1="375.5" x2="387.5" y2="376" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="436.5" y1="378.5" x2="442.5" y2="379.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="445.5" y1="370" x2="448.5" y2="371.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="425" y1="373" x2="417.5" y2="373.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="404.5" y1="359" x2="405" y2="360.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="431" y1="380" x2="438" y2="380.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="385" y1="366" x2="378.5" y2="367" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="445.5" y1="365" x2="440" y2="366" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="395" y1="359.5" x2="393" y2="361" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="493" y1="361.5" x2="485" y2="362" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="452" y1="361.5" x2="453" y2="363" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="517.5" y1="376.5" x2="518" y2="378" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="402" y1="358.5" x2="408" y2="359" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="395" y1="365" x2="398.5" y2="366.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="491.5" y1="367.5" x2="487.5" y2="368.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="434.5" y1="373" x2="431.5" y2="374.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="535" y1="372" x2="531" y2="373" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="500" y1="362.5" x2="493" y2="363" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="520.5" y1="364" x2="524.5" y2="365.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="500.5" y1="356.5" x2="508" y2="357" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="474" y1="361" x2="467" y2="361.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="427.5" y1="376.5" x2="428.5" y2="378" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="481.5" y1="362" x2="476" y2="363" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="471.5" y1="353.5" x2="470" y2="355" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="485.5" y1="356" x2="491" y2="357" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="534" y1="370.5" x2="539.5" y2="372" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="428" y1="381" x2="432.5" y2="382" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="396.5" y1="366.5" x2="395" y2="368" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="479.5" y1="361.5" x2="472" y2="362" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="517" y1="361" x2="521" y2="362.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="399.5" y1="375" x2="405" y2="376" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="382" y1="364" x2="378.5" y2="365" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="466" y1="366" x2="459" y2="366.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="415" y1="373.5" x2="415.5" y2="375" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="391" y1="369" x2="397.5" y2="370" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="514.5" y1="369.5" x2="522" y2="369.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="410" y1="370.5" x2="405.5" y2="371.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="458" y1="364.5" x2="466" y2="364.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="438" y1="365.5" x2="446" y2="365.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="422" y1="381" x2="429.5" y2="381.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="406.5" y1="361.5" x2="399.5" y2="362" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="527.5" y1="360.5" x2="525.5" y2="362" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="403" y1="369" x2="395" y2="369.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="410" y1="371" x2="402" y2="371" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="508.5" y1="372" x2="513" y2="373" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="495.5" y1="363" x2="503" y2="363.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="410" y1="374" x2="402" y2="374" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="398" y1="360" x2="396.5" y2="361.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="452.5" y1="355" x2="444.5" y2="355" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="519.5" y1="371" x2="511.5" y2="371.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="509.5" y1="362.5" x2="513.5" y2="363.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="483.5" y1="367.5" x2="491" y2="368" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="448" y1="365.5" x2="443.5" y2="366.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="493.5" y1="372.5" x2="486" y2="373.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="441.5" y1="367.5" x2="440.5" y2="369" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="476.5" y1="368" x2="470" y2="369" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="449.5" y1="370" x2="455.5" y2="371" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="470.5" y1="372.5" x2="478.5" y2="372.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="494.5" y1="364" x2="487.5" y2="365" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="436" y1="375.5" x2="429" y2="376" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="468.5" y1="356.5" x2="462" y2="357" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="397" y1="369" x2="392.5" y2="370" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="408.5" y1="363" x2="402.5" y2="364" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="422" y1="376" x2="429.5" y2="376.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="461.5" y1="381.5" x2="454.5" y2="382.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="402" y1="368.5" x2="401" y2="370" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="456.5" y1="381" x2="464" y2="381.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="528" y1="361.5" x2="522.5" y2="363" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="531.5" y1="369" x2="524.5" y2="369.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="377" y1="365.5" x2="382.5" y2="366.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="392" y1="369" x2="400" y2="369" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="427.5" y1="355" x2="435" y2="355.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="498.5" y1="374.5" x2="502" y2="375.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="407.5" y1="361" x2="412.5" y2="362.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="432" y1="373" x2="431.5" y2="374.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <rect x="560" y="318" width="40" height="46" rx="4" fill="#ffffff" stroke="#ced4da" stroke-width="2.5"/>
  <ellipse cx="580" cy="320" rx="18" ry="5" fill="#a9d1f0" stroke="#2f74b5" stroke-width="1.5"/>
  <path d="M600,328 Q614,333 600,350" fill="none" stroke="#ced4da" stroke-width="3" stroke-linejoin="round"/>
  <rect x="320" y="186" width="310" height="226" rx="6" fill="url(#fy10mh-mesh)"/>
  <rect x="320" y="186" width="310" height="226" rx="6" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <g transform="translate(1030,505) rotate(-4)"><rect x="-120" y="-14" width="240" height="28" rx="3" fill="#ffe8a3" stroke="#1f2933" stroke-width="2.5"/><line x1="-110" y1="-14" x2="-110" y2="-2" stroke="#1f2933" stroke-width="1.5"/><line x1="-100" y1="-14" x2="-100" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-90" y1="-14" x2="-90" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-80" y1="-14" x2="-80" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-70" y1="-14" x2="-70" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-60" y1="-14" x2="-60" y2="-2" stroke="#1f2933" stroke-width="1.5"/><line x1="-50" y1="-14" x2="-50" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-40" y1="-14" x2="-40" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-30" y1="-14" x2="-30" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-20" y1="-14" x2="-20" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="-10" y1="-14" x2="-10" y2="-2" stroke="#1f2933" stroke-width="1.5"/><line x1="0" y1="-14" x2="0" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="10" y1="-14" x2="10" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="20" y1="-14" x2="20" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="30" y1="-14" x2="30" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="40" y1="-14" x2="40" y2="-2" stroke="#1f2933" stroke-width="1.5"/><line x1="50" y1="-14" x2="50" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="60" y1="-14" x2="60" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="70" y1="-14" x2="70" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="80" y1="-14" x2="80" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="90" y1="-14" x2="90" y2="-2" stroke="#1f2933" stroke-width="1.5"/><line x1="100" y1="-14" x2="100" y2="-8" stroke="#1f2933" stroke-width="1.5"/><line x1="110" y1="-14" x2="110" y2="-8" stroke="#1f2933" stroke-width="1.5"/></g>
  <path d="M935,470 L935,400 Q935,372 962,372 L1010,372 Q1036,372 1036,398 L1036,470 Z" fill="#ff8787" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M935,420 Q906,414 906,390 Q906,370 928,372" fill="#ff8787" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="930" y="448" width="112" height="22" rx="4" fill="#fa5252" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M110,428 L250,428 Q244,470 180,470 Q116,470 110,428 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <ellipse cx="180" cy="426" rx="64" ry="12" fill="#ffe066" stroke="#d9a400" stroke-width="2"/>
  <line x1="214.5" y1="423.5" x2="218.5" y2="424.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="200" y1="425.5" x2="192" y2="426" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="208" y1="426" x2="214.5" y2="426.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="197.5" y1="413" x2="203.5" y2="414" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="184" y1="426" x2="192" y2="426" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="187.5" y1="426.5" x2="195" y2="426.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="169" y1="417" x2="167" y2="418.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="195" y1="421" x2="187.5" y2="421.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="164" y1="416.5" x2="162.5" y2="417.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="199.5" y1="421.5" x2="207" y2="421.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="196" y1="419" x2="193" y2="420" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="128" y1="420" x2="134" y2="421" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="191" y1="420.5" x2="191.5" y2="421.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="134.5" y1="420.5" x2="142" y2="421" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="168" y1="424.5" x2="174" y2="425.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="164.5" y1="415" x2="161" y2="416" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="152" y1="420" x2="152" y2="421.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="168.5" y1="422.5" x2="160.5" y2="422.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="206" y1="422.5" x2="200.5" y2="423.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="225" y1="417" x2="218" y2="417.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="221.5" y1="419.5" x2="213.5" y2="419.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="138.5" y1="416" x2="144.5" y2="416.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="184.5" y1="418" x2="182.5" y2="419.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="176" y1="420.5" x2="168" y2="421" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="188.5" y1="414" x2="184.5" y2="415" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="190" y1="419.5" x2="183" y2="420" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="154.5" y1="429.5" x2="162.5" y2="429.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="207" y1="429" x2="199" y2="429.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="230" y1="419" x2="223" y2="419.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="229.5" y1="421.5" x2="222.5" y2="422" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="172.5" y1="419.5" x2="168.5" y2="420.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="210.5" y1="419" x2="214" y2="420" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="156" y1="419" x2="156.5" y2="420.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="163" y1="417" x2="167.5" y2="418" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="148.5" y1="415" x2="142.5" y2="415.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="182.5" y1="430.5" x2="190.5" y2="431" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="188" y1="415" x2="186.5" y2="416" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="202" y1="417.5" x2="210" y2="417.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="214" y1="419.5" x2="209" y2="420.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="179.5" y1="426" x2="175.5" y2="427" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
</svg>

Valo kulkee sekunnissa noin seitsemän ja puoli kertaa maapallon ympäri, joten sen nopeutta ei voi mitata kellolla ja mittanauhalla. Mikroaaltouuni tarjoaa kiertotien: uunin mikroaallot ovat sähkömagneettista säteilyä kuten valo, ja niiden aallonpituuden voi selvittää juustoraasteen avulla. Tässä tutkimuksessa määrität mikroaaltojen aallonpituuden ja lasket siitä valonnopeuden. Mittaa, laske ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mikroaaltojen aallonpituus uunissa syntyvän seisovan aallon avulla, siitä ja uunin taajuudesta laskettu valonnopeus epävarmuuksineen sekä se, onko tulos sopusoinnussa valonnopeuden tunnetun arvon kanssa.

**Päätät itse (osittain ohjattu työtapa):** miten kuumennat juustoa (tehoasetus ja yksittäisen kuumennusjakson pituus), mistä riveistä ja suunnista mittaat sulaneiden kohtien välit, kuinka monen välin yhteispituuden mittaat ja montako riviä tai toistoa teet, miten paikannat sulaneen kohdan keskikohdan sekä tavan, jolla arvioit tuloksen epävarmuuden. Kirjaa valintasi perusteluineen. Ohjatussa työtavassa sivu kiinnittää useimmat näistä valinnoista puolestasi.

Uunin valmistelee opettaja, eikä sen turvallisuudesta päätetä itse: noudata kohdan Suunnittele turvallisuusohjeita kaikissa työtavoissa.

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Millaisen kuvion arvelet syntyvän tasaiseen juustokerrokseen, kun sitä kuumennetaan hetken uunissa, jonka alusta ei pyöri? Miksi mikroaaltouunin alusta tavallisesti pyörii?
2. Jos juustoon sulaa toisistaan erillisiä kohtia, miten kahden vierekkäisen kohdan välinen etäisyys voisi liittyä mikroaaltojen aallonpituuteen?
3. Kuinka kaukana toisistaan arvelet sulaneiden kohtien olevan: millimetrejä, senttimetrejä vai kymmeniä senttimetrejä?
4. Mitä arvelet sulaneille kohdille tapahtuvan, jos juustoa kuumennetaan liian kauan, ja miten se vaikuttaisi mittaukseen?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

**Aallon nopeus.** Aallon etenemisnopeus $v$, taajuus $f$ ja aallonpituus $\lambda$ liittyvät toisiinsa aaltoyhtälöllä

```latex
v = f\lambda
```

Taajuuden yksikkö on hertsi, $1\ \text{Hz} = 1\ \tfrac{1}{\text{s}}$. Aaltoliikettä käsitellään tarkemmin moduulissa FY5.

**Mikroaallot.** Mikroaaltouunin mikroaallot ovat sähkömagneettista säteilyä, samaa ilmiötä kuin valo ja radioaallot, mutta niiden aallonpituus on paljon suurempi kuin valon. Kaikki sähkömagneettinen säteily etenee tyhjiössä samalla nopeudella, valonnopeudella $c$, ja ilmassa käytännössä yhtä nopeasti. Siksi mikroaaltojen etenemisnopeus on valonnopeus: $c = f\lambda$. Sähkömagneettista säteilyä käsitellään moduulissa FY7. Mikroaaltojen taajuus on uunin ominaisuus, ja se on merkitty uunin arvokilpeen tai käyttöohjeeseen.

**Seisova aalto.** Uunin metalliseinät heijastavat mikroaallot. Kun kaksi samantaajuista aaltoa etenee vastakkaisiin suuntiin, ne yhdistyvät seisovaksi aalloksi. Seisovassa aallossa on kohtia, joissa sähkökenttä ei värähtele lainkaan (**solmukohdat**), ja niiden puolivälissä kohtia, joissa se värähtelee voimakkaimmin (**kupukohdat**). Kuvio pysyy paikallaan. Kahden vierekkäisen kupukohdan välinen etäisyys on puolet aallonpituudesta, samoin kahden vierekkäisen solmukohdan välinen etäisyys. Seisovia aaltoja käsitellään moduulissa FY5.

<svg data-fig="standing" viewBox="0 0 600 360" role="img" aria-label="Kaaviokuva yksinkertaisesta mallista. Kahden metalliseinän välissä on seisova aalto. Kiinteä viiva ja katkoviiva näyttävät sähkökentän värähtelyn ääriasennot. Solmukohdissa, myös seinien kohdalla, kenttä ei värähtele. Kupukohdissa, solmukohtien puolivälissä, värähtely on suurin. Alla olevassa juustokerroksessa on sulanut kohta jokaisen kupukohdan alla. Kahden vierekkäisen kupukohdan välinen etäisyys on puolet aallonpituudesta, lambda per kaksi." style="max-width:100%;font-size:24px">
  <rect x="48" y="70" width="22" height="210" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="48" y1="84" x2="70" y2="72" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="48" y1="112" x2="70" y2="100" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="48" y1="140" x2="70" y2="128" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="48" y1="168" x2="70" y2="156" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="48" y1="196" x2="70" y2="184" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="48" y1="224" x2="70" y2="212" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="48" y1="252" x2="70" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="530" y="70" width="22" height="210" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="530" y1="84" x2="552" y2="72" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="112" x2="552" y2="100" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="140" x2="552" y2="128" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="168" x2="552" y2="156" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="196" x2="552" y2="184" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="224" x2="552" y2="212" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="252" x2="552" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M70,150 L72,147 L74,143.5 L76,140.5 L77.5,137 L79.5,134 L81.5,131 L83.5,128 L85.5,125 L87,122 L89,119 L91,116 L93,113.5 L95,111 L97,108.5 L99,106 L100.5,104 L102.5,102 L104.5,100 L106.5,98 L108.5,96.5 L110,95 L112,93.5 L114,92 L116,91 L118,90 L120,89.5 L122,89 L123.5,88.5 L125.5,88 L127.5,88 L129.5,88 L131.5,88.5 L133,89 L135,89.5 L137,90 L139,91 L141,92 L143,93.5 L145,95 L146.5,96.5 L148.5,98 L150.5,100 L152.5,102 L154.5,104 L156,106 L158,108.5 L160,111 L162,113.5 L164,116 L166,119 L168,122 L169.5,125 L171.5,128 L173.5,131 L175.5,134 L177.5,137 L179,140.5 L181,143.5 L183,147 L185,150 L187,153 L189,156.5 L191,159.5 L192.5,163 L194.5,166 L196.5,169 L198.5,172 L200.5,175 L202,178 L204,181 L206,184 L208,186.5 L210,189 L212,191.5 L214,194 L215.5,196 L217.5,198 L219.5,200 L221.5,202 L223.5,203.5 L225,205 L227,206.5 L229,208 L231,209 L233,210 L235,210.5 L237,211 L238.5,211.5 L240.5,212 L242.5,212 L244.5,212 L246.5,211.5 L248,211 L250,210.5 L252,210 L254,209 L256,208 L258,206.5 L260,205 L261.5,203.5 L263.5,202 L265.5,200 L267.5,198 L269.5,196 L271,194 L273,191.5 L275,189 L277,186.5 L279,184 L281,181 L283,178 L284.5,175 L286.5,172 L288.5,169 L290.5,166 L292.5,163 L294,159.5 L296,156.5 L298,153 L300,150 L302,147 L304,143.5 L306,140.5 L307.5,137 L309.5,134 L311.5,131 L313.5,128 L315.5,125 L317,122 L319,119 L321,116 L323,113.5 L325,111 L327,108.5 L329,106 L330.5,104 L332.5,102 L334.5,100 L336.5,98 L338.5,96.5 L340,95 L342,93.5 L344,92 L346,91 L348,90 L350,89.5 L352,89 L353.5,88.5 L355.5,88 L357.5,88 L359.5,88 L361.5,88.5 L363,89 L365,89.5 L367,90 L369,91 L371,92 L373,93.5 L375,95 L376.5,96.5 L378.5,98 L380.5,100 L382.5,102 L384.5,104 L386,106 L388,108.5 L390,111 L392,113.5 L394,116 L396,119 L398,122 L399.5,125 L401.5,128 L403.5,131 L405.5,134 L407.5,137 L409,140.5 L411,143.5 L413,147 L415,150 L417,153 L419,156.5 L421,159.5 L422.5,163 L424.5,166 L426.5,169 L428.5,172 L430.5,175 L432,178 L434,181 L436,184 L438,186.5 L440,189 L442,191.5 L444,194 L445.5,196 L447.5,198 L449.5,200 L451.5,202 L453.5,203.5 L455,205 L457,206.5 L459,208 L461,209 L463,210 L465,210.5 L467,211 L468.5,211.5 L470.5,212 L472.5,212 L474.5,212 L476.5,211.5 L478,211 L480,210.5 L482,210 L484,209 L486,208 L488,206.5 L490,205 L491.5,203.5 L493.5,202 L495.5,200 L497.5,198 L499.5,196 L501,194 L503,191.5 L505,189 L507,186.5 L509,184 L511,181 L513,178 L514.5,175 L516.5,172 L518.5,169 L520.5,166 L522.5,163 L524,159.5 L526,156.5 L528,153 L530,150" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M70,150 L72,153 L74,156.5 L76,159.5 L77.5,163 L79.5,166 L81.5,169 L83.5,172 L85.5,175 L87,178 L89,181 L91,184 L93,186.5 L95,189 L97,191.5 L99,194 L100.5,196 L102.5,198 L104.5,200 L106.5,202 L108.5,203.5 L110,205 L112,206.5 L114,208 L116,209 L118,210 L120,210.5 L122,211 L123.5,211.5 L125.5,212 L127.5,212 L129.5,212 L131.5,211.5 L133,211 L135,210.5 L137,210 L139,209 L141,208 L143,206.5 L145,205 L146.5,203.5 L148.5,202 L150.5,200 L152.5,198 L154.5,196 L156,194 L158,191.5 L160,189 L162,186.5 L164,184 L166,181 L168,178 L169.5,175 L171.5,172 L173.5,169 L175.5,166 L177.5,163 L179,159.5 L181,156.5 L183,153 L185,150 L187,147 L189,143.5 L191,140.5 L192.5,137 L194.5,134 L196.5,131 L198.5,128 L200.5,125 L202,122 L204,119 L206,116 L208,113.5 L210,111 L212,108.5 L214,106 L215.5,104 L217.5,102 L219.5,100 L221.5,98 L223.5,96.5 L225,95 L227,93.5 L229,92 L231,91 L233,90 L235,89.5 L237,89 L238.5,88.5 L240.5,88 L242.5,88 L244.5,88 L246.5,88.5 L248,89 L250,89.5 L252,90 L254,91 L256,92 L258,93.5 L260,95 L261.5,96.5 L263.5,98 L265.5,100 L267.5,102 L269.5,104 L271,106 L273,108.5 L275,111 L277,113.5 L279,116 L281,119 L283,122 L284.5,125 L286.5,128 L288.5,131 L290.5,134 L292.5,137 L294,140.5 L296,143.5 L298,147 L300,150 L302,153 L304,156.5 L306,159.5 L307.5,163 L309.5,166 L311.5,169 L313.5,172 L315.5,175 L317,178 L319,181 L321,184 L323,186.5 L325,189 L327,191.5 L329,194 L330.5,196 L332.5,198 L334.5,200 L336.5,202 L338.5,203.5 L340,205 L342,206.5 L344,208 L346,209 L348,210 L350,210.5 L352,211 L353.5,211.5 L355.5,212 L357.5,212 L359.5,212 L361.5,211.5 L363,211 L365,210.5 L367,210 L369,209 L371,208 L373,206.5 L375,205 L376.5,203.5 L378.5,202 L380.5,200 L382.5,198 L384.5,196 L386,194 L388,191.5 L390,189 L392,186.5 L394,184 L396,181 L398,178 L399.5,175 L401.5,172 L403.5,169 L405.5,166 L407.5,163 L409,159.5 L411,156.5 L413,153 L415,150 L417,147 L419,143.5 L421,140.5 L422.5,137 L424.5,134 L426.5,131 L428.5,128 L430.5,125 L432,122 L434,119 L436,116 L438,113.5 L440,111 L442,108.5 L444,106 L445.5,104 L447.5,102 L449.5,100 L451.5,98 L453.5,96.5 L455,95 L457,93.5 L459,92 L461,91 L463,90 L465,89.5 L467,89 L468.5,88.5 L470.5,88 L472.5,88 L474.5,88 L476.5,88.5 L478,89 L480,89.5 L482,90 L484,91 L486,92 L488,93.5 L490,95 L491.5,96.5 L493.5,98 L495.5,100 L497.5,102 L499.5,104 L501,106 L503,108.5 L505,111 L507,113.5 L509,116 L511,119 L513,122 L514.5,125 L516.5,128 L518.5,131 L520.5,134 L522.5,137 L524,140.5 L526,143.5 L528,147 L530,150" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="7 6"/>
  <line x1="70" y1="150" x2="530" y2="150" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="70" y="252" width="460" height="16" fill="#ffe066" stroke="#d9a400" stroke-width="2"/>
  <ellipse cx="127.5" cy="260" rx="26" ry="8" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <line x1="127.5" y1="220" x2="127.5" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <ellipse cx="242.5" cy="260" rx="26" ry="8" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <line x1="242.5" y1="220" x2="242.5" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <ellipse cx="357.5" cy="260" rx="26" ry="8" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <line x1="357.5" y1="220" x2="357.5" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <ellipse cx="472.5" cy="260" rx="26" ry="8" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <line x1="472.5" y1="220" x2="472.5" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="242.5" y1="84" x2="242.5" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="182.5" y="15.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kupukohta}$</div></foreignObject>
  <line x1="415" y1="144" x2="415" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="348.5" y="15.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{solmukohta}$</div></foreignObject>
  <line x1="357.5" y1="292" x2="472.5" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="357.5" y1="282" x2="357.5" y2="302" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="472.5" y1="282" x2="472.5" y2="302" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="405" y="297" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\dfrac{\lambda}{2}$</div></foreignObject>
  <foreignObject x="70" y="297.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{juustokerros}$</div></foreignObject>
</svg>

**Miksi juusto sulaa kohdittain.** Mikroaallot lämmittävät ruokaa, koska värähtelevä sähkökenttä saa ruoan vesimolekyylit liikkeeseen, ja energia muuttuu sisäenergiaksi. Mitä voimakkaammin kenttä värähtelee, sitä nopeammin ruoka lämpenee. Kun alusta ei pyöri, ruoka lämpenee eniten kupukohdissa.

**Mallin rajat.** Yllä oleva malli on yksinkertaistettu: siinä aallot etenevät edestakaisin yhdessä suunnassa. Todellisessa uunissa mikroaallot heijastuvat kaikista seinistä, ja kuvio on usean seisovan aallon yhdistelmä. Siksi sulaneiden kohtien väli voi jossakin suunnassa poiketa puolesta aallonpituudesta, ja kuvio voi olla epäsäännöllinen. Lisäksi lämpö johtuu juustossa, joten sulaneet kohdat laajenevat ja lopulta yhtyvät, jos kuumennus jatkuu. Juustokerros, lautanen ja vesikuppi muuttavat kuviota jonkin verran, mutta niiden vaikutus aallonpituuteen ilmassa jätetään mallissa huomiotta.

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, miten saat juustoon selvästi erottuvat sulaneet kohdat, mitä mittaat ja miten luet uunin taajuuden.

**Turvallisuus.** Uunia käytetään vain opettajan luvalla ja valvonnassa, käyttöohjeen mukaisesti. Älä koskaan avaa uunin kuorta tai muuta, ohita tai peitä luukkua tai sen turvalukitusta. Opettaja poistaa pyörivän alustan käytöstä vain uunin käyttöohjeen sallimalla tavalla. Uunia ei koskaan käynnistetä tyhjänä: kuppi vettä on uunissa koko ajan, myös juustolautasen lisäksi. Uuniin ei laiteta metallia, ei edes mittaa. Kuuma juusto, lautanen ja vesi voivat polttaa, ja mikroaaltouunissa kuumennettu vesi voi kiehahtaa äkillisesti: käytä patalappua ja vaihda kuppiin viileää vettä, jos se on lämmennyt. Lopeta kuumennus heti, jos juusto alkaa savuta. Työssä käytettyä juustoa ei syödä.

**Taajuus.** Lue mikroaaltojen taajuus uunin arvokilvestä ja kirjaa se yksikköineen. Arvokilvessä on yleensä myös sähköverkon taajuus, joka on eri asia kuin mikroaaltojen taajuus. Jos et löydä mikroaaltojen taajuutta, kysy opettajalta: se on uunin käyttöohjeessa. [[apua:fy1-2|Kerrannaisyksiköt]]

::: tuki O
**Ohjattu.** Levitä mikroaaltouuniin sopivalle tasaiselle lautaselle ohut ja tasainen kerros juustoraastetta niin, että lautasen pohja ei näy. Aseta lautanen uuniin opettajan neuvomaan kohtaan, ja kuppi vettä uunin reunalle, aina samaan kohtaan. Kuumenna opettajan kertomalla tehoasetuksella opettajan kertomissa lyhyissä jaksoissa ja katso luukun ikkunasta välillä. Lopeta, kun juustoon on sulanut selvästi erottuvia kohtia, ennen kuin ne alkavat yhtyä toisiinsa. Ota lautanen uunista patalapulla. Etsi ainakin kolme riviä, joissa on vähintään neljä sulanutta kohtaa samalla suoralla, ja mittaa jokaisesta rivistä ensimmäisen ja viimeisen kohdan keskikohtien välinen etäisyys $L$. Kirjaa myös, montako väliä $n$ etäisyyteen sisältyy.

<svg data-fig="spots" viewBox="0 0 600 380" role="img" aria-label="Kaaviokuva ylhäältä katsottuna. Lautasella on juustokerros, johon on sulanut kohtia. Neljä sulanutta kohtaa on samalla suoralla. Niiden keskikohdat on merkitty rastilla. Ensimmäisen ja viimeisen kohdan keskikohtien välinen etäisyys L kattaa kolme kohtien väliä." style="max-width:100%;font-size:24px">
  <circle cx="300" cy="160" r="148" fill="#f8f9fa" stroke="#ced4da" stroke-width="3"/>
  <circle cx="300" cy="160" r="130" fill="#ffe066" stroke="#d9a400" stroke-width="2"/>
  <line x1="407" y1="96.5" x2="408" y2="105.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="280.5" y1="228.5" x2="287" y2="235" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="222.5" y1="201.5" x2="221.5" y2="210.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="207.5" y1="154" x2="198.5" y2="154.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="351.5" y1="201" x2="358.5" y2="206.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="222" y1="108" x2="227.5" y2="115" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="253" y1="247.5" x2="259" y2="254" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="211" y1="143" x2="220" y2="144" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="240.5" y1="198.5" x2="243" y2="207" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="237" y1="260.5" x2="244.5" y2="265" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="305.5" y1="86" x2="314" y2="90" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="288" y1="215.5" x2="281" y2="221" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="328" y1="94" x2="337" y2="95.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="361" y1="53.5" x2="359" y2="62.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="415.5" y1="147.5" x2="424" y2="151" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="259" y1="197.5" x2="256" y2="206" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="276.5" y1="193" x2="282.5" y2="199.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="370.5" y1="245" x2="379" y2="247" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="317" y1="273" x2="324.5" y2="278" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="298" y1="71.5" x2="290.5" y2="76" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="378.5" y1="211" x2="378" y2="220" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="409.5" y1="160" x2="401" y2="163.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="267" y1="102.5" x2="275" y2="106" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="285" y1="49.5" x2="294" y2="50.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="253.5" y1="165" x2="248.5" y2="173" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="236.5" y1="106.5" x2="245.5" y2="108.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="248.5" y1="185" x2="240" y2="188.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="251" y1="123" x2="244" y2="128.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="365" y1="212.5" x2="358" y2="218" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="404" y1="112.5" x2="399.5" y2="120" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="220.5" y1="173.5" x2="229.5" y2="175.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="220.5" y1="243" x2="223.5" y2="251.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="300" y1="50" x2="306.5" y2="56.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="239" y1="212.5" x2="244" y2="220.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="392" y1="138.5" x2="383" y2="139.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="248" y1="107.5" x2="239" y2="108.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="283.5" y1="52" x2="283" y2="61" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="255.5" y1="214.5" x2="256.5" y2="223.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="201.5" y1="176" x2="205.5" y2="184" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="317.5" y1="122.5" x2="324.5" y2="128.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="355.5" y1="236" x2="356" y2="245" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="303" y1="82.5" x2="296" y2="88" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="331" y1="61" x2="323" y2="65" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="223.5" y1="179" x2="221" y2="188" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="344" y1="119.5" x2="351" y2="125.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="330.5" y1="127" x2="330" y2="136" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="320.5" y1="106" x2="319" y2="115" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="403.5" y1="123" x2="396.5" y2="128.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="276.5" y1="157.5" x2="269.5" y2="163.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="278" y1="89.5" x2="269.5" y2="93" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="366" y1="190" x2="374.5" y2="194" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="270.5" y1="245.5" x2="278" y2="250.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="344.5" y1="79.5" x2="339.5" y2="87" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="408.5" y1="139.5" x2="403" y2="146.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="343.5" y1="184" x2="348.5" y2="191" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="267" y1="218" x2="271.5" y2="225.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="193" y1="173.5" x2="184" y2="174.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="346" y1="146.5" x2="352" y2="152.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="249" y1="142" x2="242" y2="148" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="354" y1="179.5" x2="352.5" y2="188.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="306" y1="126" x2="298" y2="129.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="348" y1="95.5" x2="345" y2="104" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="243.5" y1="270" x2="252" y2="272" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="414" y1="175.5" x2="421.5" y2="180.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="217.5" y1="91.5" x2="208.5" y2="91.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="346" y1="64" x2="344" y2="72.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="244" y1="113" x2="235" y2="113.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="387" y1="189.5" x2="378" y2="191.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="338" y1="150.5" x2="343.5" y2="158" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="331.5" y1="155" x2="329" y2="163.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="346.5" y1="201" x2="354.5" y2="205.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="411.5" y1="157.5" x2="407" y2="165.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="401.5" y1="191" x2="392.5" y2="192" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="351.5" y1="66.5" x2="360.5" y2="68.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="333" y1="73" x2="342" y2="75" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="322.5" y1="45" x2="325" y2="53.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="194.5" y1="163.5" x2="197.5" y2="172" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="245.5" y1="193.5" x2="236.5" y2="193.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="263.5" y1="235.5" x2="266.5" y2="244.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="379.5" y1="214" x2="372.5" y2="220" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="245" y1="63" x2="236.5" y2="65.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="208.5" y1="122.5" x2="214" y2="130" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="254.5" y1="120" x2="246.5" y2="124" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="188" y1="159" x2="194.5" y2="165" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="202.5" y1="193" x2="210.5" y2="196.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="187" y1="106.5" x2="193" y2="113.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="343.5" y1="111" x2="352.5" y2="112" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="228" y1="192.5" x2="219" y2="194" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="210.5" y1="94" x2="219.5" y2="95" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="300" y1="143.5" x2="293" y2="149" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="338.5" y1="271" x2="333.5" y2="278.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="239" y1="140.5" x2="238.5" y2="149.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="301" y1="131" x2="292.5" y2="134" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="241" y1="100" x2="240.5" y2="109" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="301" y1="218" x2="294" y2="224" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="276" y1="48.5" x2="268" y2="52.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="408.5" y1="163" x2="401" y2="168.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="225" y1="90.5" x2="219.5" y2="98" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="345" y1="48" x2="341.5" y2="56" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="260.5" y1="191" x2="265" y2="198.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="321" y1="88.5" x2="320.5" y2="97.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="359.5" y1="93.5" x2="367.5" y2="97.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="342.5" y1="163" x2="351" y2="165.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="387.5" y1="159" x2="396.5" y2="159.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="258.5" y1="123.5" x2="264" y2="130.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="389.5" y1="84" x2="391.5" y2="92.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="259.5" y1="44.5" x2="260.5" y2="53.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="288.5" y1="113" x2="286.5" y2="121.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="389" y1="184" x2="382.5" y2="190" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="304.5" y1="129" x2="303.5" y2="138" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="266.5" y1="187.5" x2="273.5" y2="193" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="272" y1="75" x2="273.5" y2="84" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="282.5" y1="49.5" x2="285.5" y2="58" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="211.5" y1="209" x2="209.5" y2="217.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="331.5" y1="112" x2="322.5" y2="112.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="342" y1="154" x2="339.5" y2="162.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="403" y1="178.5" x2="394" y2="179" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="300" y1="273.5" x2="307.5" y2="279" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="349.5" y1="204" x2="356.5" y2="210" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="276.5" y1="63" x2="273.5" y2="71.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="290" y1="161.5" x2="291.5" y2="170" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="234" y1="140" x2="237" y2="148.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="277" y1="42" x2="284" y2="48" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="204.5" y1="122" x2="204" y2="131" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="416" y1="112" x2="411" y2="119.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="287.5" y1="239.5" x2="278.5" y2="240" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="339" y1="249.5" x2="337" y2="258.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="385.5" y1="182.5" x2="385.5" y2="191.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="399.5" y1="149" x2="403" y2="157" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="371" y1="81.5" x2="373" y2="90" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="202.5" y1="199.5" x2="194" y2="201" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="289" y1="137.5" x2="291.5" y2="146" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="316" y1="226" x2="325" y2="226" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="316" y1="162" x2="315" y2="171" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="205" y1="94" x2="210" y2="101.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="402.5" y1="171.5" x2="399" y2="180" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="194" y1="119.5" x2="202.5" y2="123" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="325.5" y1="180.5" x2="330" y2="188.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="380.5" y1="88" x2="387" y2="94.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="218.5" y1="118.5" x2="209.5" y2="119" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="316.5" y1="268.5" x2="323.5" y2="274.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="323.5" y1="103" x2="314.5" y2="104" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="329.5" y1="173" x2="330.5" y2="182" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="248" y1="212" x2="250.5" y2="221" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="276" y1="128" x2="275.5" y2="137" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="210.5" y1="132" x2="203" y2="136.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="242" y1="169" x2="247.5" y2="176.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="233.5" y1="79.5" x2="241.5" y2="84" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="380" y1="167.5" x2="377.5" y2="176" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <line x1="271" y1="211" x2="277" y2="217.5" stroke="#d9a400" stroke-width="2" stroke-linecap="round"/>
  <ellipse cx="195" cy="160" rx="19" ry="17" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="265" cy="160" rx="19.5" ry="19.5" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="335" cy="160" rx="20.5" ry="18" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="405" cy="160" rx="20.5" ry="16" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="230" cy="92" rx="23" ry="16.5" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="300" cy="88" rx="21" ry="17" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="370" cy="92" rx="21.5" ry="20" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="230" cy="228" rx="21.5" ry="17.5" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="300" cy="232" rx="21.5" ry="16" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <ellipse cx="370" cy="228" rx="21.5" ry="18" fill="#ffc078" stroke="#d9a400" stroke-width="1.5"/>
  <line x1="188" y1="153" x2="202" y2="167" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="188" y1="167" x2="202" y2="153" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="258" y1="153" x2="272" y2="167" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="258" y1="167" x2="272" y2="153" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="328" y1="153" x2="342" y2="167" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="328" y1="167" x2="342" y2="153" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="153" x2="412" y2="167" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="167" x2="412" y2="153" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="195" y1="172" x2="195" y2="318" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="405" y1="172" x2="405" y2="318" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="195" y1="330" x2="405" y2="330" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="195" y1="318" x2="195" y2="342" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="405" y1="318" x2="405" y2="342" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="290" y="341.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
  <foreignObject x="425" y="315.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{3 väliä}$</div></foreignObject>
</svg>
:::

::: tuki OO
**Osittain ohjattu.** Päätä itse, miten kuumennat juustoa niin, että kohdat erottuvat mutta eivät yhdy, mistä riveistä mittaat ja montako väliä kukin mittaus kattaa. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miksi kannattaa mitata usean välin yhteispituus eikä yhtä väliä?
- Miten paikannat sulaneen kohdan keskikohdan, kun kohta on leveä ja reunoiltaan epäselvä?
- Miten vesikuppi voi vaikuttaa kuvioon sen lähellä?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Kirjaa myös uunin taajuus ja tehoasetus sekä vesikupin paikka.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa:

| Rivi | $n$ (välejä) | $L\ (\text{m})$ | $d = \dfrac{L}{n}\ (\text{m})$ |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Aseta mitta lautaselle juustokerroksen viereen tai päälle vasta, kun lautanen on otettu uunista. Lue kummankin kohdan keskikohta samalla tavalla ja katso asteikkoa kohtisuoraan.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti pystyt paikantamaan sulaneen kohdan keskikohdan. Se on yleensä paljon epätarkempaa kuin mitan asteikko. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Merkitään kahden vierekkäisen sulaneen kohdan välistä etäisyyttä $d$. Vastaa:

1. Johda teorian avulla lauseke, jolla valonnopeus $c$ lasketaan mitatusta etäisyydestä $d$ ja taajuudesta $f$.
2. Laske jokaisesta rivistä etäisyys $d$ ja niiden keskiarvo $\bar{d}$. Laske siitä aallonpituus ja valonnopeus. Muista muuttaa taajuus perusyksikköön hertsi.
3. Olivatko eri rivien etäisyydet yhtä suuria? Jos eivät, mistä ero voi johtua?
4. Perustele, miksi usean välin yhteispituuden mittaaminen antaa tarkemman tuloksen kuin yhden välin mittaaminen.

::: tuki O
**Tarkista lausekkeesi.** Vierekkäisten kupukohtien väli on puolet aallonpituudesta, joten $\lambda = 2d$, ja valonnopeus on

```latex
c = f\lambda = 2fd
```

missä $f$ on mikroaaltojen taajuus ja $d$ vierekkäisten sulaneiden kohtien välinen etäisyys.
:::

## Epävarmuus ja luotettavuus

Ilmoita valonnopeus muodossa $c = (c \pm \Delta c)\ \text{m/s}$ ja perustele, miten arvioit epävarmuuden $\Delta c$.

::: tuki O
**Epävarmuus vaihe vaiheelta.**

- **Etäisyys $L$.** Se on kahden paikkalukeman erotus, joten sen epävarmuus on lukemien epävarmuuksien summa: $\Delta L = \Delta x_\text{alku} + \Delta x_\text{loppu}$, missä $\Delta x$ on se tarkkuus, jolla paikannat kohdan keskikohdan.
- **Etäisyys $d$.** Kun $d = \dfrac{L}{n}$, sen epävarmuus on $\Delta d = \dfrac{\Delta L}{n}$. Vertaa tätä myös siihen, kuinka paljon eri rivien tulokset vaihtelevat: käytä suurempaa näistä.
- **Taajuus $f$.** Arvokilven arvo on uunin nimellinen taajuus. Jos uunin käyttöohjeessa on valmistajan ilmoittama taajuuden toleranssi, käytä sitä epävarmuutena $\Delta f$; kysy sitä opettajalta. Kilven viimeisen numeron perusteella arvioitu epävarmuus on liian pieni, koska uunin todellinen taajuus voi poiketa kilven arvosta enemmän.
- **Valonnopeus $c$.** Tulon suhteellinen epävarmuus on tekijöiden suhteellisten epävarmuuksien summa: $\dfrac{\Delta c}{c} = \dfrac{\Delta f}{f} + \dfrac{\Delta d}{d}$. Kerroin 2 on tarkka, eikä se lisää epävarmuutta.

Pyöristä $\Delta c$ yhteen merkitsevään numeroon ja $c$ samaan tarkkuuteen.
:::

::: tuki OO
Mieti, mistä lukemista etäisyyden $L$ epävarmuus muodostuu, miten se jakautuu välien kesken, ja miten etäisyyden ja taajuuden epävarmuudet yhdistyvät valonnopeuden epävarmuudeksi. Valitse menetelmä ja perustele se.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Ota huomioon myös mallin rajat: noudattiko kuvio yksinkertaista mallia, jossa kohtien väli on puolet aallonpituudesta? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Vertaa tulostasi valonnopeuden tunnettuun arvoon $c = 2{,}998 \cdot 10^8\ \text{m/s}$: onko tunnettu arvo epävarmuusvälisi sisällä? Jos on, tulos on sopusoinnussa tunnetun arvon kanssa, mutta se ei todista mallia oikeaksi. Jos ei ole, mikä systemaattinen virhe tai mallin oletus voisi selittää eron? Vertaa tulosta ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** seisova aalto, miksi juusto sulaa kupukohdissa ja miten lauseke valonnopeudelle saadaan.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, miten kuumensit juuston ja mittasit kohtien välit sekä työturvallisuus (vesikuppi, ei metallia, alusta ei pyöri: poistettu käyttöohjeen mukaan).
- **Mittaustulokset:** alkuperäiset etäisyydet ja välien määrät omissa sarakkeissaan, uunin taajuus ja sen lähde.
- **Tulos:** $c = (c \pm \Delta c)\ \text{m/s}$ oikein pyöristettynä.
- **Luotettavuus:** kohtien paikantamisen epätarkkuus, taajuuden epävarmuus ja mallin rajat sekä niiden vaikutuksen suunta.

## Laajennus: kohtien paikat kuvaajana kahdessa suunnassa

Yksinkertainen malli olettaa, että sulaneiden kohtien väli on sama joka suunnassa. Testaa oletusta. Valitse kaksi toisiaan vastaan kohtisuoraa suuntaa, esimerkiksi uunin leveyden ja syvyyden suunnat, ja mittaa kummastakin suunnasta rivin jokaisen sulaneen kohdan keskikohdan paikka $x_k$ mitan asteikolta. Numeroi kohdat järjestyksessä $k = 1, 2, 3, \ldots$

Jos kohdat ovat tasavälein, paikka järjestysnumeron funktiona on suora, jonka kulmakerroin on vierekkäisten kohtien välinen etäisyys $d$. Vakiotermi riippuu vain siitä, mihin mitan nollakohta asetettiin.

<svg data-fig="model" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja: sulaneen kohdan keskikohdan paikka x k järjestysnumeron k funktiona mallin mukaan. Kuvaaja on suora, jonka kulmakerroin on vierekkäisten kohtien välinen etäisyys d, joka on mallin mukaan lambda per kaksi. Suora ei kulje origon kautta, koska ensimmäisen kohdan paikka riippuu siitä, mihin mitan nollakohta asetetaan. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="300" x2="474" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M486,300 L473,306 L473,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="157.5" y1="300" x2="157.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="147.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="224.5" y1="300" x2="224.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="214.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="292" y1="300" x2="292" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="282" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="359" y1="300" x2="359" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="349" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="426.5" y1="300" x2="426.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="416.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="492" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x_k$</div></foreignObject>
  <polyline points="123.5,250 440,62" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="224.5" y1="190" x2="292" y2="190" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="292" y1="190" x2="292" y2="150" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="302" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$d$</div></foreignObject>
  <foreignObject x="248" y="193.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="117" y="46" width="195" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } d = \dfrac{\lambda}{2}$</div></foreignObject>
</svg>

Piirrä kummastakin suunnasta kuvaaja ja sovita pisteisiin suora. Ovatko pisteet suoralla? Ovatko kahden suunnan kulmakertoimet sopusoinnussa keskenään ja päämittauksen tuloksen kanssa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Mitä mahdollinen ero kertoo yksinkertaisen mallin pätevyydestä? [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O OO
**Vihjeitä.** Pidä mitta paikallaan koko rivin lukemisen ajan, jotta kaikki paikat luetaan samasta nollakohdasta. Kulmakerroin ei riipu nollakohdasta. Sovitusohjelman ilmoittama kulmakertoimen keskivirhe käy kulmakertoimen epävarmuudeksi. Kuvaajan sovitukseen voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohje ohjelman käyttöön on tekeillä.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi mittaustuloksiin vai siihen, mitä odotit tunnetun arvon perusteella?
- Mitä tekisit toisin, jos aloittaisit alusta?
