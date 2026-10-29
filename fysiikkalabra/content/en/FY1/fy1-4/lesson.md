# Graphing and fitting a straight line

> **Why** do data points not usually all land exactly on one straight line, and yet a single line fitted to them can reveal the relationship between the quantities?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a sheet of grid paper on a desk. On it are measured points with error bars; they do not lie exactly on one straight line, and one straight line has been drawn through them with a ruler. Beside it are a pencil, an eraser and a calculator." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy14h-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy14h-desk)"/>
  <path d="M0,24 q300,-4.5 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,88 q300,-1.5 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,152 q300,-4 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,216 q300,8 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,280 q300,2.5 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,344 q300,8 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,408 q300,4 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,472 q300,-7.5 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,536 q300,7 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,600 q300,-9 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M257.5,596.5 L978,581.5 L988.5,19.5 L268,34.5 Z" fill="#1f2933" fill-opacity="0.2"/>
  <path d="M247.5,584.5 L968,569.5 L978.5,7.5 L258,22.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="285" y1="578" x2="295" y2="27" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="254.5" y1="555" x2="962" y2="540.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="302" y1="578" x2="312" y2="26.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="255" y1="542" x2="962" y2="527" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="319" y1="577.5" x2="329" y2="26.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="255" y1="528.5" x2="962.5" y2="514" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="577" x2="346" y2="26" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="255.5" y1="515.5" x2="962.5" y2="500.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="353" y1="577" x2="363" y2="25.5" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="255.5" y1="502" x2="963" y2="487.5" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="370" y1="576.5" x2="380" y2="25.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="489" x2="963" y2="474" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="387" y1="576" x2="397" y2="25" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="475.5" x2="963.5" y2="461" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="404" y1="576" x2="414" y2="24.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256.5" y1="462.5" x2="963.5" y2="447.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="421" y1="575.5" x2="431" y2="24" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256.5" y1="449" x2="964" y2="434.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="438" y1="575" x2="448" y2="24" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="257" y1="436" x2="964" y2="421" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="455" y1="575" x2="465" y2="23.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="257" y1="422.5" x2="964.5" y2="408" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="574.5" x2="482" y2="23" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="257.5" y1="409.5" x2="964.5" y2="394.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="489" y1="574" x2="499" y2="23" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="257.5" y1="396" x2="965" y2="381.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="506" y1="573.5" x2="516" y2="22.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258" y1="383" x2="965" y2="368" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="523" y1="573.5" x2="533" y2="22" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="258" y1="369.5" x2="965.5" y2="355" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="540" y1="573" x2="550" y2="22" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258.5" y1="356.5" x2="965.5" y2="341.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="557" y1="572.5" x2="567" y2="21.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258.5" y1="343" x2="966" y2="328.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="574" y1="572.5" x2="584" y2="21" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="259" y1="330" x2="966" y2="315" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="591" y1="572" x2="601" y2="20.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="259" y1="316.5" x2="966.5" y2="302" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="608" y1="571.5" x2="618" y2="20.5" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="259.5" y1="303.5" x2="966.5" y2="288.5" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="625" y1="571" x2="635" y2="20" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="259.5" y1="290" x2="967" y2="275.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="642" y1="571" x2="652" y2="19.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="277" x2="967" y2="262" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="659" y1="570.5" x2="669" y2="19.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="263.5" x2="967.5" y2="249" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="676" y1="570" x2="686" y2="19" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260.5" y1="250.5" x2="967.5" y2="235.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="693" y1="570" x2="703" y2="18.5" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="260.5" y1="237" x2="968" y2="222.5" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="710" y1="569.5" x2="720" y2="18.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="261" y1="224" x2="968" y2="209" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="727" y1="569" x2="737" y2="18" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="261" y1="210.5" x2="968.5" y2="196" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="744" y1="569" x2="754" y2="17.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="261.5" y1="197.5" x2="968.5" y2="182.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="761" y1="568.5" x2="771" y2="17" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="261.5" y1="184" x2="969" y2="169.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="778" y1="568" x2="788" y2="17" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="262" y1="171" x2="969" y2="156" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="795" y1="568" x2="805" y2="16.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="157.5" x2="969.5" y2="143" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="812" y1="567.5" x2="822" y2="16" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262.5" y1="144.5" x2="969.5" y2="129.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="829" y1="567" x2="839" y2="16" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262.5" y1="131" x2="970" y2="116.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="846" y1="566.5" x2="856" y2="15.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="118" x2="970" y2="103" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="863" y1="566.5" x2="873" y2="15" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="263" y1="104.5" x2="970.5" y2="90" stroke="#d0e6fb" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="880" y1="566" x2="890" y2="15" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263.5" y1="91.5" x2="970.5" y2="76.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="897" y1="565.5" x2="907" y2="14.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263.5" y1="78" x2="971" y2="63.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="914" y1="565.5" x2="924" y2="14" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="264" y1="65" x2="971" y2="50" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="931" y1="565" x2="941" y2="13.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="264" y1="51.5" x2="971.5" y2="37" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="323" y1="524.5" x2="915" y2="512.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="323" y1="524.5" x2="332" y2="63.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M915,512.5 l-14,-7 v14 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="391" y1="523" x2="391" y2="531" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="471.5" x2="314" y2="471.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="459" y1="521.5" x2="459" y2="529.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="325" y1="418.5" x2="315" y2="418.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="527" y1="520.5" x2="527" y2="528" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="326" y1="365.5" x2="316" y2="365.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="595" y1="519" x2="595" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="327" y1="312.5" x2="317" y2="312.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="663" y1="517.5" x2="663" y2="525.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="328" y1="259.5" x2="318" y2="259.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="731" y1="516" x2="731" y2="524" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="329" y1="206.5" x2="319" y2="206.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="799" y1="514.5" x2="799" y2="522.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="330" y1="153.5" x2="320" y2="153.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="867" y1="513.5" x2="867" y2="521" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="331" y1="100.5" x2="321" y2="100.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="344" y1="495" x2="882" y2="102.5" stroke="#e8590c" stroke-width="4" stroke-linecap="round"/>
  <line x1="385" y1="486" x2="386" y2="443.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="378.5" y1="486.5" x2="392" y2="486" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="379" y1="444" x2="392.5" y2="443.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="385.5" cy="465" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <line x1="447.5" y1="416" x2="448.5" y2="363" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="441" y1="416" x2="454.5" y2="416" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="442" y1="363" x2="455.5" y2="363" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="448" cy="389.5" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <line x1="509" y1="404" x2="510" y2="361.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="502" y1="404" x2="516" y2="404" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="503" y1="362" x2="516.5" y2="361.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="509.5" cy="383" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <line x1="571.5" y1="339" x2="572.5" y2="286" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="564.5" y1="339.5" x2="578" y2="339" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="565.5" y1="286.5" x2="579" y2="286" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="572" cy="312.5" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <line x1="633" y1="317" x2="634" y2="274.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="626" y1="317" x2="640" y2="316.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="627" y1="274.5" x2="640.5" y2="274" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="633.5" cy="295.5" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <line x1="695" y1="262.5" x2="696" y2="209.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="688.5" y1="262.5" x2="702" y2="262.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="689.5" y1="209.5" x2="703" y2="209.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="695.5" cy="236" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <line x1="757" y1="229.5" x2="758" y2="187" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="750" y1="229.5" x2="764" y2="229.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="751" y1="187" x2="764.5" y2="187" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="757.5" cy="208.5" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <line x1="819.5" y1="164.5" x2="820.5" y2="111.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="812.5" y1="164.5" x2="826" y2="164.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="813.5" y1="111.5" x2="827" y2="111.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="820" cy="138" r="8" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <g transform="translate(642.5,339) rotate(-36)"><rect x="-340" y="0" width="680" height="60" rx="5" fill="#eef5f9" fill-opacity="0.7" stroke="#8a96a3" stroke-width="2.5"/><rect x="-336" y="40" width="672" height="16" rx="3" fill="#ffffff" fill-opacity="0.5"/><line x1="-320" y1="0" x2="-320" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="-304" y1="0" x2="-304" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-288" y1="0" x2="-288" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-272" y1="0" x2="-272" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-256" y1="0" x2="-256" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-240" y1="0" x2="-240" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="-224" y1="0" x2="-224" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-208" y1="0" x2="-208" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-192" y1="0" x2="-192" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-176" y1="0" x2="-176" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-160" y1="0" x2="-160" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="-144" y1="0" x2="-144" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-128" y1="0" x2="-128" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-112" y1="0" x2="-112" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-96" y1="0" x2="-96" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-80" y1="0" x2="-80" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="-64" y1="0" x2="-64" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-48" y1="0" x2="-48" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-32" y1="0" x2="-32" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="-16" y1="0" x2="-16" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="0" y1="0" x2="0" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="16" y1="0" x2="16" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="32" y1="0" x2="32" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="48" y1="0" x2="48" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="64" y1="0" x2="64" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="80" y1="0" x2="80" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="96" y1="0" x2="96" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="112" y1="0" x2="112" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="128" y1="0" x2="128" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="144" y1="0" x2="144" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="160" y1="0" x2="160" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="176" y1="0" x2="176" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="192" y1="0" x2="192" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="208" y1="0" x2="208" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="224" y1="0" x2="224" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="240" y1="0" x2="240" y2="26" stroke="#8a96a3" stroke-width="2"/><line x1="256" y1="0" x2="256" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="272" y1="0" x2="272" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="288" y1="0" x2="288" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="304" y1="0" x2="304" y2="14" stroke="#8a96a3" stroke-width="2"/><line x1="320" y1="0" x2="320" y2="26" stroke="#8a96a3" stroke-width="2"/></g>
  <g transform="translate(1060,330) rotate(-64)"><rect x="-170" y="-13" width="290" height="26" fill="#ffc078" stroke="#1f2933" stroke-width="2"/><line x1="-170" y1="0" x2="120" y2="0" stroke="#e8590c" stroke-width="2"/><rect x="-196" y="-13" width="20" height="26" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/><rect x="-216" y="-13" width="22" height="26" rx="6" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/><path d="M120,-13 L162,0 L120,13 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/><path d="M148,-4 L162,0 L148,4 Z" fill="#1f2933"/></g>
  <g transform="translate(120,470) rotate(-12)"><rect x="-50" y="-22" width="100" height="44" rx="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/><rect x="-50" y="-22" width="38" height="44" rx="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/></g>
  <g transform="translate(130,190) rotate(8)"><rect x="-70" y="-110" width="140" height="220" rx="14" fill="#6c757d" stroke="#1f2933" stroke-width="3"/><rect x="-52" y="-92" width="104" height="44" rx="4" fill="#b2f2bb" stroke="#1f2933" stroke-width="2"/><rect x="-52" y="-34" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="-24" y="-34" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="4" y="-34" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="32" y="-34" width="22" height="22" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/><rect x="-52" y="-4" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="-24" y="-4" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="4" y="-4" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="32" y="-4" width="22" height="22" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/><rect x="-52" y="26" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="-24" y="26" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="4" y="26" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="32" y="26" width="22" height="22" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/><rect x="-52" y="56" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="-24" y="56" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="4" y="56" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="32" y="56" width="22" height="22" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/><rect x="-52" y="86" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="-24" y="86" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="4" y="86" width="22" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/><rect x="32" y="86" width="22" height="22" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/></g>
</svg>

## Key idea
### A graph brings the measurements together
When you measure two quantities, for example the distance $s$ travelled by a trolley at different times $t$, each measurement is one point on the graph. The horizontal coordinate of the point is the value of one quantity and the vertical coordinate is the value of the other. The horizontal axis usually gets the quantity that the experimenter chooses or that increases steadily, such as time, and the vertical axis gets the quantity being measured.

A graph needs axes with the quantity and its unit written at the end, such as $s\ (\text{m})$, an evenly spaced scale and tick marks that are close enough together. Choose the scale so that the points fill most of the graph.

<svg data-fig="scatter" viewBox="0 0 600 350" role="img" aria-label="Graph drawn to scale: the distance s travelled by a trolley as a function of time t. Six data points (t = 1…6 s) are scattered around the line s = 0.5 m/s · t. There are points on both sides of the line, three above and three below, and vertical dashed lines show the deviation of each point from the line. The line does not pass through every point." style="max-width:100%;font-size:24px">
  <line x1="149.5" y1="300" x2="149.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="203" y1="300" x2="203" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256.5" y1="300" x2="256.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="309.5" y1="300" x2="309.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="300" x2="363" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416.5" y1="300" x2="416.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="231.5" x2="470" y2="231.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="163" x2="470" y2="163" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="94.5" x2="470" y2="94.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="484" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,300 L483,306 L483,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="149.5" y1="300" x2="149.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="139.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="203" y1="300" x2="203" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="193" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="256.5" y1="300" x2="256.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="309.5" y1="300" x2="309.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="299.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="363" y1="300" x2="363" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="353" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="416.5" y1="300" x2="416.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="406.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="231.5" x2="96" y2="231.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="217" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="163" x2="96" y2="163" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="148.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="94.5" x2="96" y2="94.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="80" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <polyline points="96,300 470,60" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="149.5" y1="259" x2="149.5" y2="265.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="203" y1="245" x2="203" y2="231.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="256.5" y1="190.5" x2="256.5" y2="197" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="309.5" y1="156" x2="309.5" y2="163" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="363" y1="135.5" x2="363" y2="128.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="416.5" y1="101" x2="416.5" y2="94.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="149.5" cy="259" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="203" cy="245" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="256.5" cy="190.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="309.5" cy="156" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="363" cy="135.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="416.5" cy="101" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="114.5" cy="77" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="132.5" y="62.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{data points}$</div></foreignObject>
  <line x1="102.5" y1="111.5" x2="126.5" y2="111.5" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="132.5" y="97" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{fitted line}$</div></foreignObject>
  <foreignObject x="414.5" y="176" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{deviation}$</div></foreignObject>
  <line x1="410.5" y1="190.5" x2="366" y2="132" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

### Fit a line, do not join the points
In real data sets the data points do not usually lie exactly on one straight line, because of measurement uncertainty, especially random error (chapter *Measuring and the reliability of a measurement*). So you do not join the points into a broken line, since that line would follow the errors too. Instead you fit one straight line that runs through the middle of the set of points.

A good fit is close to all the points and does not lean towards any single point. There are roughly as many points on each side of the line, and the deviations above and below cancel each other. The line does not have to pass through any point. If one point is clearly further away than the others, it is worth finding out why, and you do not drop the point automatically.

### Linear model
If the points lie roughly along a straight line, the relationship between the quantities is described by a linear model, whose equation is the equation of a straight line. The slope tells you how much the vertical quantity changes when the horizontal quantity increases by one unit, and the constant term tells you the value of the vertical quantity when the horizontal quantity is zero.

When the constant term is zero, the line passes through the origin and the quantities are directly proportional: doubling $x$ doubles $y$. The measurements show that the model holds only in the range that was measured. If the line is extended beyond the measured range, you assume that the relationship stays the same, and the result is only an estimate. If the points curve systematically around the line, for example all the points are above the line at the ends and below it in the middle, the linear model does not fit.

## Formula: Equation of a straight line
The graph of a linear model is a straight line with the equation
```latex
y = kx + b
```
where $y$ is the quantity on the vertical axis, $x$ the quantity on the horizontal axis, $k$ the slope and $b$ the constant term, that is, the point where the line crosses the vertical axis. The slope is calculated from two chosen points $(x_1,\ y_1)$ and $(x_2,\ y_2)$ on the line:
```latex
k = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}
```
where $\Delta y$ is the change in $y$ between the points and $\Delta x$ the change in $x$ between them. The unit of the slope is the unit of $y$ divided by the unit of $x$: if $y$ is in metres and $x$ in seconds, $k$ is in $\text{m/s}$.

<svg data-fig="slope" viewBox="0 0 600 350" role="img" aria-label="Diagram drawn to scale: the line y = kx + b with a slope of 0.5 and a constant term of 1. The line crosses the y-axis at y = b = 1. Two points far apart have been chosen on the line, P₁ = (2, 2) and P₂ = (8, 5). The horizontal side of the right triangle is Δx = x₂ − x₁ = 6 and the vertical side is Δy = y₂ − y₁ = 3, so the slope is k = Δy/Δx = 0.5." style="max-width:100%;font-size:24px">
  <line x1="179" y1="300" x2="179" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="300" x2="262" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="300" x2="345.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428.5" y1="300" x2="428.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="260" x2="470" y2="260" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="220" x2="470" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="180" x2="470" y2="180" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="140" x2="470" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="100" x2="470" y2="100" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="484" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,300 L483,306 L483,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179" y1="300" x2="179" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="169" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="262" y1="300" x2="262" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="345.5" y1="300" x2="345.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="335.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="428.5" y1="300" x2="428.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="418.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="89" y1="260" x2="96" y2="260" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="220" x2="96" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="180" x2="96" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="140" x2="96" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="125.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="89" y1="100" x2="96" y2="100" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y$</div></foreignObject>
  <polyline points="96,260 470,80" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="179" y1="220" x2="428.5" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="428.5" y1="220" x2="428.5" y2="100" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="96" cy="260" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="179" cy="220" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="428.5" cy="100" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="269" y="231.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta x$</div></foreignObject>
  <foreignObject x="341" y="233" width="150" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$k = \dfrac{\Delta y}{\Delta x}$</span></div></foreignObject>
  <foreignObject x="442.5" y="145.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta y$</div></foreignObject>
  <foreignObject x="110" y="221.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$b$</div></foreignObject>
  <foreignObject x="121" y="175.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$P_1$</div></foreignObject>
  <foreignObject x="364.5" y="59.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$P_2$</div></foreignObject>
  <foreignObject x="167.5" y="105.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$y = kx + b$</span></div></foreignObject>
</svg>

Two things affect the result. Read the points from the fitted line and not from the data points, and choose them far apart, so that the reading error has only a small effect on the slope. Read the constant term $b$ from the point where the line crosses the vertical axis, or calculate it from one point on the line: $b = y_1 - kx_1$. If you want $x$ when $y$ is known, solve the equation: $x = \tfrac{y - b}{k}$.

The sign of the slope tells you the direction. With a positive slope the line rises, and with a negative slope it falls. The slope usually has a physical meaning: in a distance–time graph it is the speed, and in a mass–volume graph it is the density.

## Worked example
The temperature $T$ of the water in a kettle was measured every minute:

| $t$ (min) | $T$ (°C) |
| --- | --- |
| 0 | 20.8 |
| 1 | 27.9 |
| 2 | 36.5 |
| 3 | 43.8 |
| 4 | 52.4 |
| 5 | 59.6 |

Fit a straight line to the data points, find its equation $T = kt + b$ and use it to work out when the water temperature is $40\,{}^\circ\text{C}$. The power of the kettle is constant, and the heat losses are small.

<svg data-fig="kettle" viewBox="0 0 600 350" role="img" aria-label="Graph drawn to scale: the temperature T of the water in a kettle as a function of time t. Six data points, one minute apart, are scattered around the line T = 8.0 °C/min · t + 20 °C. Two points far apart have been read from the line, (0 min; 20 °C) and (5.0 min; 60 °C). A dashed line shows that the line reaches the temperature 40 °C at 2.5 min." style="max-width:100%;font-size:24px">
  <line x1="158.5" y1="300" x2="158.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220.5" y1="300" x2="220.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="300" x2="283" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="300" x2="345.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="407.5" y1="300" x2="407.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="300" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="231.5" x2="470" y2="231.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="163" x2="470" y2="163" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="94.5" x2="470" y2="94.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="484" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,300 L483,306 L483,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="158.5" y1="300" x2="158.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="148.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="220.5" y1="300" x2="220.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="283" y1="300" x2="283" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="273" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="345.5" y1="300" x2="345.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="335.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="407.5" y1="300" x2="407.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="397.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="470" y1="300" x2="470" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="460" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="231.5" x2="96" y2="231.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="217" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="163" x2="96" y2="163" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="148.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="94.5" x2="96" y2="94.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="80" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="285.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{min})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ ({}^\circ\text{C})$</div></foreignObject>
  <polyline points="96,231.5 470,67" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="252" y1="163" x2="252" y2="300" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="163" x2="252" y2="163" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="96" cy="228.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="158.5" cy="204.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="220.5" cy="175" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283" cy="150" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="345.5" cy="120.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="407.5" cy="95.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="96" cy="231.5" r="11" fill="none" stroke="#e8590c" stroke-width="2.5"/>
  <circle cx="407.5" cy="94.5" r="11" fill="none" stroke="#e8590c" stroke-width="2.5"/>
  <foreignObject x="116" y="247" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$A$</div></foreignObject>
  <foreignObject x="411.5" y="114" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$B$</div></foreignObject>
  <line x1="252" y1="300" x2="252" y2="307" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235" y="309.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$2.5$</span></div></foreignObject>
</svg>

<!-- vaihe -->

**Given and find.** The graph has six data points, and the fitted line has been drawn through the middle of the set. Two points far apart are read from the line: $A = (t_1;\ T_1) = (0.0\,\text{min};\ 20.0\,{}^\circ\text{C})$ and $B = (t_2;\ T_2) = (5.0\,\text{min};\ 60.0\,{}^\circ\text{C})$. We need the slope $k$, the constant term $b$ and the time $t$ at which $T = 40\,{}^\circ\text{C}$.

<!-- vaihe -->

**Principle.** The power of the kettle is constant and the heat losses are small in this temperature range, so the water temperature rises almost steadily and the linear model $T = kt + b$ fits. The line is drawn so that there are points on both sides of it and each point is close to the line. The slope is calculated from the points $A$ and $B$ on the line, not from the data points.

<!-- vaihe -->

**Rearranged formula.** The slope comes from the differences between the points, the constant term from the point $A$, and the time is solved from the equation of the line:
```latex
\begin{aligned}
&k = \frac{T_2 - T_1}{t_2 - t_1} \\
&b = T_1 - k t_1 \\
&t = \frac{T - b}{k}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None needed: the temperatures are in degrees Celsius and the times in minutes. The unit of the slope is ${}^\circ\text{C/min}$, and a temperature change is the same in degrees Celsius and in kelvins.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
k &= \frac{T_2 - T_1}{t_2 - t_1} \\
&= \frac{60.0\,{}^\circ\text{C} - 20.0\,{}^\circ\text{C}}{5.0\,\text{min} - 0.0\,\text{min}} \\
&= 8.0\,\tfrac{{}^\circ\text{C}}{\text{min}} \\[6pt]
b &= T_1 - k t_1 \\
&= 20.0\,{}^\circ\text{C} - 8.0\,\tfrac{{}^\circ\text{C}}{\text{min}} \cdot 0.0\,\text{min} \\
&= 20.0\,{}^\circ\text{C} \\[6pt]
t &= \frac{T - b}{k} \\
&= \frac{40\,{}^\circ\text{C} - 20.0\,{}^\circ\text{C}}{8.0\,\tfrac{{}^\circ\text{C}}{\text{min}}} \\
&= 2.5\,\text{min}
\end{aligned}
```

<!-- vaihe -->

**Result.** The equation of the line is $T = 8.0\,\tfrac{{}^\circ\text{C}}{\text{min}} \cdot t + 20\,{}^\circ\text{C}$, and the temperature $40\,{}^\circ\text{C}$ is reached after about 2.5 minutes. The results are given to two significant figures, because $k$ is determined from points read to two figures.

<!-- vaihe -->

**Reasonableness.** The constant term $20\,{}^\circ\text{C}$ is the temperature of the water before heating, that is, room temperature, and the slope $8.0\,\tfrac{{}^\circ\text{C}}{\text{min}}$ tells you how fast the water warms up. In the table, $40\,{}^\circ\text{C}$ is passed between the third and fourth measurements, since $T$ is $36.5\,{}^\circ\text{C}$ at two minutes and $43.8\,{}^\circ\text{C}$ at three minutes, so $2.5\,\text{min}$ is in the right interval. The points deviate from the line by at most about one degree.

## Common misconception
Many students join the data points with a line, or force the line to pass through one of the data points, even though that point, too, has measurement uncertainty. The line is fitted to the whole set of points; it may pass through some point, but it does not have to.

Another mistake is to calculate the slope from two data points. Then the error in each point affects the result, and if the points are also close together, the result is uncertain. Read the points from the fitted line and far apart.

A third mistake is to assume that the line always passes through the origin. If the constant term is not zero, the quantities are not directly proportional, and $b$ tells you what $y$ is when $x$ is zero.

## Summary
- The axes of a graph show the quantities with their units and an evenly spaced scale. The data points are not joined to each other.
- A straight line is fitted to the data points so that it runs through the middle of the set: there are roughly as many points on each side of it.
- The equation of the linear model is $y = kx + b$. The slope is $k = \tfrac{\Delta y}{\Delta x}$, and it is calculated from two points on the line that are far apart.
- The constant term $b$ is the point where the line crosses the vertical axis. If $b = 0$, the quantities are directly proportional.
- If the points curve systematically, the linear model does not fit.
