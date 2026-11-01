# Mass defect and binding energy

> **Why** can both joining nuclei and splitting nuclei release energy?

<!-- The Binding Energy Explorer in inquiry.json reads data-src="units/fy14/data/nuclides.json" (named here so that build.py embeds it and the content hash covers it). -->

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration on a dark background, in two halves. Left: two small nuclei, made of red protons and grey neutrons, fly towards each other and meet in a bright yellow flash. Right: a large nucleus with many protons and neutrons breaks into two medium-sized pieces that fly apart, with a few single neutrons and another bright flash." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy14be-h-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#26313b"/><stop offset="1" stop-color="#121820"/></linearGradient><radialGradient id="fy14be-h-p" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#ff8a80"/><stop offset="55%" stop-color="#c92a2a"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient><radialGradient id="fy14be-h-n" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#e9ecef"/><stop offset="55%" stop-color="#9aa1a9"/><stop offset="100%" stop-color="#4b5259"/></radialGradient><radialGradient id="fy14be-h-f1"><stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/><stop offset="0.35" stop-color="#ffc078" stop-opacity="0.7"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient><radialGradient id="fy14be-h-f2"><stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/><stop offset="0.35" stop-color="#ffc078" stop-opacity="0.7"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy14be-h-bg)"/>
  <line x1="600" y1="60" x2="600" y2="540" stroke="#3a4754" stroke-width="3" stroke-linecap="butt" stroke-dasharray="10 12"/>
  <circle cx="67.5" cy="512" r="1.6715" fill="#4b5866"/>
  <circle cx="187" cy="383.5" r="1.65715" fill="#4b5866"/>
  <circle cx="134" cy="320" r="1.73755" fill="#4b5866"/>
  <circle cx="972.5" cy="200.5" r="1.61125" fill="#4b5866"/>
  <circle cx="238.5" cy="200" r="1.23268" fill="#4b5866"/>
  <circle cx="225.5" cy="252" r="1.49282" fill="#4b5866"/>
  <circle cx="816.5" cy="363" r="0.871156" fill="#4b5866"/>
  <circle cx="1118" cy="589.5" r="1.66619" fill="#4b5866"/>
  <circle cx="806" cy="579" r="1.55954" fill="#4b5866"/>
  <circle cx="1170.5" cy="440.5" r="1.79657" fill="#4b5866"/>
  <circle cx="1046" cy="204" r="1.43511" fill="#4b5866"/>
  <circle cx="633.5" cy="553" r="1.24844" fill="#4b5866"/>
  <circle cx="1105.5" cy="560" r="1.77518" fill="#4b5866"/>
  <circle cx="630.5" cy="345" r="0.94504" fill="#4b5866"/>
  <circle cx="383.5" cy="412" r="1.10497" fill="#4b5866"/>
  <circle cx="822" cy="49.5" r="1.41436" fill="#4b5866"/>
  <circle cx="647.5" cy="540" r="1.5074" fill="#4b5866"/>
  <circle cx="560" cy="565.5" r="1.10763" fill="#4b5866"/>
  <circle cx="47" cy="203" r="0.8425" fill="#4b5866"/>
  <circle cx="1080" cy="492" r="0.975386" fill="#4b5866"/>
  <circle cx="1126.5" cy="76.5" r="1.35527" fill="#4b5866"/>
  <circle cx="742" cy="161.5" r="1.05719" fill="#4b5866"/>
  <circle cx="933.5" cy="355.5" r="1.03203" fill="#4b5866"/>
  <circle cx="746.5" cy="388.5" r="1.50641" fill="#4b5866"/>
  <circle cx="927" cy="68.5" r="1.50175" fill="#4b5866"/>
  <circle cx="984" cy="294.5" r="1.44845" fill="#4b5866"/>
  <circle cx="381" cy="127" r="1.23479" fill="#4b5866"/>
  <circle cx="209" cy="228.5" r="1.26903" fill="#4b5866"/>
  <circle cx="1132" cy="557" r="1.62254" fill="#4b5866"/>
  <circle cx="1189" cy="187" r="1.39506" fill="#4b5866"/>
  <circle cx="782" cy="264.5" r="1.09103" fill="#4b5866"/>
  <circle cx="1119" cy="554" r="1.61518" fill="#4b5866"/>
  <circle cx="704.5" cy="351" r="1.04594" fill="#4b5866"/>
  <circle cx="809" cy="54.5" r="1.05865" fill="#4b5866"/>
  <circle cx="769" cy="517.5" r="1.49722" fill="#4b5866"/>
  <circle cx="277.5" cy="521.5" r="1.13439" fill="#4b5866"/>
  <circle cx="933.5" cy="114" r="1.60293" fill="#4b5866"/>
  <circle cx="1045" cy="509" r="1.12085" fill="#4b5866"/>
  <circle cx="1133" cy="310.5" r="1.26796" fill="#4b5866"/>
  <circle cx="318.5" cy="199.5" r="0.820137" fill="#4b5866"/>
  <circle cx="63.5" cy="324.5" r="1.79253" fill="#4b5866"/>
  <circle cx="1033" cy="454" r="1.59703" fill="#4b5866"/>
  <circle cx="550" cy="268" r="0.984431" fill="#4b5866"/>
  <circle cx="110.5" cy="236" r="1.67869" fill="#4b5866"/>
  <circle cx="268.5" cy="325.5" r="1.51808" fill="#4b5866"/>
  <circle cx="1062" cy="33" r="1.16583" fill="#4b5866"/>
  <circle cx="902" cy="397.5" r="1.17559" fill="#4b5866"/>
  <circle cx="83" cy="326" r="1.44385" fill="#4b5866"/>
  <circle cx="529" cy="119.5" r="0.806799" fill="#4b5866"/>
  <circle cx="1024" cy="220.5" r="1.13806" fill="#4b5866"/>
  <circle cx="300" cy="300" r="150" fill="url(#fy14be-h-f1)"/>
  <line x1="90" y1="300" x2="210" y2="300" stroke="#d0e6fb" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 14"/>
  <line x1="510" y1="300" x2="390" y2="300" stroke="#d0e6fb" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 14"/>
  <circle cx="222" cy="300" r="26" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="210.5" y1="300" x2="233.5" y2="300" stroke="#ffffff" stroke-width="4.16" stroke-linecap="round"/>
  <line x1="222" y1="288.5" x2="222" y2="311.5" stroke="#ffffff" stroke-width="4.16" stroke-linecap="round"/>
  <circle cx="258" cy="300" r="26" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="344" cy="316" r="26" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="380" cy="316" r="26" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="362" cy="285" r="26" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="350.5" y1="285" x2="373.5" y2="285" stroke="#ffffff" stroke-width="4.16" stroke-linecap="round"/>
  <line x1="362" y1="273.5" x2="362" y2="296.5" stroke="#ffffff" stroke-width="4.16" stroke-linecap="round"/>
  <circle cx="900" cy="300" r="170" fill="url(#fy14be-h-f2)"/>
  <circle cx="876.5" cy="172" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="705.5" cy="221" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="698.5" y1="221" x2="712" y2="221" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="705.5" y1="214.5" x2="705.5" y2="228" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="863" cy="299.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="800.5" cy="137.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="738" cy="297" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="731.5" y1="297" x2="745" y2="297" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="738" y1="290" x2="738" y2="303.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="889.5" cy="222.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="730" cy="176" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="723" y1="176" x2="736.5" y2="176" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="730" y1="169" x2="730" y2="182.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="815" cy="316" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="846.5" cy="158" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="718.5" cy="251.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="711.5" y1="251.5" x2="725" y2="251.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="718.5" y1="245" x2="718.5" y2="258.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="873.5" cy="268.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="772.5" cy="153" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="765.5" y1="153" x2="779" y2="153" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="772.5" y1="146.5" x2="772.5" y2="160" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="769" cy="304" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="871.5" cy="197" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="726.5" cy="206.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="719.5" y1="206.5" x2="733" y2="206.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="726.5" y1="200" x2="726.5" y2="213.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="837.5" cy="295.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="816.5" cy="157.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="809.5" y1="157.5" x2="823" y2="157.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="816.5" y1="151" x2="816.5" y2="164.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="740.5" cy="271.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="870.5" cy="239.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="755.5" cy="177" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="749" y1="177" x2="762.5" y2="177" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="755.5" y1="170" x2="755.5" y2="183.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="797" cy="297.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="846.5" cy="183.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="840" y1="183.5" x2="853.5" y2="183.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="846.5" y1="177" x2="846.5" y2="190.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="736" cy="232.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="847.5" cy="270" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="792.5" cy="170.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="785.5" y1="170.5" x2="799" y2="170.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="792.5" y1="163.5" x2="792.5" y2="177" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="766.5" cy="277.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="855" cy="218" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="848" y1="218" x2="861.5" y2="218" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="855" y1="211" x2="855" y2="224.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="753" cy="203" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="815.5" cy="279.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="821" cy="185" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="814.5" y1="185" x2="828" y2="185" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="821" y1="178.5" x2="821" y2="192" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="756.5" cy="248" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="842" cy="245.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="835" y1="245.5" x2="848.5" y2="245.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="842" y1="238.5" x2="842" y2="252" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="780.5" cy="193" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="790" cy="267.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="830.5" cy="210.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="823.5" y1="210.5" x2="837" y2="210.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="830.5" y1="204" x2="830.5" y2="217.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="768" cy="224.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="817.5" cy="252.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="810.5" y1="252.5" x2="824" y2="252.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="817.5" y1="246" x2="817.5" y2="259.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="802" cy="206" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="786" cy="242.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="811" cy="230" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="804" y1="230" x2="817.5" y2="230" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="811" y1="223" x2="811" y2="237" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="1056.5" cy="308" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1049.5" y1="308" x2="1063" y2="308" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1056.5" y1="301" x2="1056.5" y2="314.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="928.5" cy="401.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1083.5" cy="418.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="982.5" cy="303" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="975.5" y1="303" x2="989" y2="303" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="982.5" y1="296.5" x2="982.5" y2="310" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="979" cy="454" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1081.5" cy="347" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1074.5" y1="347" x2="1088" y2="347" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1081.5" y1="340" x2="1081.5" y2="353.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="936.5" cy="356.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1047.5" cy="445.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1026.5" cy="307.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1019.5" y1="307.5" x2="1033" y2="307.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1026.5" y1="301" x2="1026.5" y2="314.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="950.5" cy="421.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1080.5" cy="389.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1073.5" y1="389.5" x2="1087" y2="389.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1080.5" y1="382.5" x2="1080.5" y2="396" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="965.5" cy="327" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1007" cy="447.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1056.5" cy="333.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1050" y1="333.5" x2="1063.5" y2="333.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1056.5" y1="327" x2="1056.5" y2="340.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="946" cy="382.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1057.5" cy="420" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1051" y1="420" x2="1064.5" y2="420" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1057.5" y1="413.5" x2="1057.5" y2="427" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="1002.5" cy="320.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="976.5" cy="427.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1065" cy="368" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1058" y1="368" x2="1071.5" y2="368" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1065" y1="361" x2="1065" y2="374.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="963" cy="353" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1025.5" cy="429.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1019" y1="429.5" x2="1032.5" y2="429.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1025.5" y1="423" x2="1025.5" y2="436.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="1031" cy="335" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="966.5" cy="398" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1052" cy="395.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1045" y1="395.5" x2="1058.5" y2="395.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1052" y1="388.5" x2="1052" y2="402" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="990.5" cy="343" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1000" cy="417.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="993" y1="417.5" x2="1006.5" y2="417.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1000" y1="411" x2="1000" y2="424.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="1040.5" cy="360.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="978" cy="374.5" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1027.5" cy="402.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="1020.5" y1="402.5" x2="1034" y2="402.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="1027.5" y1="396" x2="1027.5" y2="409.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="1012" cy="356" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="996" cy="392.5" r="15" fill="url(#fy14be-h-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="989.5" y1="392.5" x2="1003" y2="392.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <line x1="996" y1="386" x2="996" y2="399.5" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="1021" cy="380" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="730" y1="165" x2="670" y2="115" stroke="#d0e6fb" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 14"/>
  <line x1="1085" y1="450" x2="1145" y2="500" stroke="#d0e6fb" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 14"/>
  <circle cx="905" cy="160" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="1080" cy="250" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="860" cy="450" r="15" fill="url(#fy14be-h-n)" stroke="#1f2933" stroke-width="1.5"/>
</svg>

## Formula: Mass–energy equivalence

In 1905 Albert Einstein showed that mass and energy are two sides of the same quantity. If a system gives away the energy $E$, its mass decreases by $\Delta m$:
```latex
E = \Delta m \cdot c^2
```
where $c = 2.998 \cdot 10^{8}\ \text{m/s}$ is the speed of light. Because $c^2$ is so large, a tiny mass corresponds to a huge energy: $1\ \text{kg}$ corresponds to $9.0 \cdot 10^{16}\ \text{J}$.

In nuclear physics, masses are given in **atomic mass units** and energies in **megaelectronvolts**, $1\ \text{MeV} = 10^{6}\ \text{eV} = 1.602 \cdot 10^{-13}\ \text{J}$. The mass $1\ \text{u} = 1.661 \cdot 10^{-27}\ \text{kg}$ corresponds to the energy
```latex
1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}
```
so a mass difference in $\text{u}$ times $931.5\ \text{MeV/u}$ gives the energy in $\text{MeV}$.

## Key idea

A nucleus has *less* mass than the free protons and neutrons it is made of. The difference is the **mass defect** $\Delta m$. When nucleons join, the strong force pulls them together and energy is released, so the system loses mass. To pull the nucleus apart again, the same energy must be given back. This energy is the **binding energy** $B$:
```latex
B = \Delta m \cdot c^2
```

<svg data-fig="ladder" viewBox="0 0 600 380" role="img" aria-label="Energy diagram of helium-4. An upper level: two protons and two neutrons far apart, with the total mass 4.032980 u. A lower level, 28.3 MeV below: the helium-4 nucleus, mass 4.002603 u. An arrow up on the left is the binding energy B = 28.3 MeV that must be added to separate the nucleons. An arrow down on the right is the same energy released when they join." style="max-width:100%;font-size:26px">
  <defs><radialGradient id="fy14be-l-p" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#ff8a80"/><stop offset="55%" stop-color="#c92a2a"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient><radialGradient id="fy14be-l-n" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#e9ecef"/><stop offset="55%" stop-color="#9aa1a9"/><stop offset="100%" stop-color="#4b5259"/></radialGradient></defs>
  <line x1="230" y1="110" x2="440" y2="110" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="230" y1="300" x2="440" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="250" cy="86" r="17" fill="url(#fy14be-l-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="242.5" y1="86" x2="257.5" y2="86" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <line x1="250" y1="78.5" x2="250" y2="93.5" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <circle cx="305" cy="86" r="17" fill="url(#fy14be-l-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="370" cy="86" r="17" fill="url(#fy14be-l-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="362.5" y1="86" x2="377.5" y2="86" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <line x1="370" y1="78.5" x2="370" y2="93.5" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <circle cx="420" cy="86" r="17" fill="url(#fy14be-l-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="309.5" cy="291.5" r="17" fill="url(#fy14be-l-n)" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="292.5" cy="238.5" r="17" fill="url(#fy14be-l-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="284.5" y1="238.5" x2="300" y2="238.5" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <line x1="292.5" y1="231" x2="292.5" y2="246.5" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <circle cx="274.5" cy="280.5" r="17" fill="url(#fy14be-l-p)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="266.5" y1="280.5" x2="282" y2="280.5" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <line x1="274.5" y1="272.5" x2="274.5" y2="288" stroke="#ffffff" stroke-width="2.72" stroke-linecap="round"/>
  <circle cx="302.5" cy="266" r="17" fill="url(#fy14be-l-n)" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="250" y="18.5" width="170" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{free nucleons}$</div></foreignObject>
  <foreignObject x="261.5" y="316.5" width="147" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">${}^{4}\text{He}\ \text{nucleus}$</div></foreignObject>
  <foreignObject x="450" y="94.5" width="134" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$4.032980\ \text{u}$</div></foreignObject>
  <foreignObject x="450" y="284.5" width="134" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$4.002603\ \text{u}$</div></foreignObject>
  <path d="M212,296 L212,140 L222,140 L205,114 L188,140 L198,140 L198,296 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="6" y="153.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{add}$</div></foreignObject>
  <foreignObject x="6" y="189.5" width="184" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${B = 28.3\ \text{MeV}}$</div></foreignObject>
  <path d="M348,124 L348,202 L338,202 L355,228 L372,202 L362,202 L362,124 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="379" y="177.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$\text{released}$</div></foreignObject>
</svg>

We calculate with the **atomic masses** of tables such as AME2020, which include the electrons. So for the protons we use the mass of a hydrogen-1 atom, $m_\text{H} = 1.007825\ \text{u}$, and the electrons cancel:
```latex
\Delta m = Z \cdot m_\text{H} + N \cdot m_\text{n} - m_\text{atom}
```
Here $m_\text{n} = 1.008665\ \text{u}$ is the mass of a neutron.

## Binding energy per nucleon {Curve}

To compare nuclei, we divide the binding energy by the number of nucleons. The **binding energy per nucleon** $B/A$ tells how tightly each nucleon is held on average. A large $B/A$ means a tightly bound nucleus.

The curve of $B/A$ rises steeply among the light nuclei: $1.11\ \text{MeV}$ for deuterium, $7.07\ \text{MeV}$ for helium-4. It reaches its peak near iron and nickel ($8.79\ \text{MeV}$ for $^{56}\text{Fe}$ and $^{62}\text{Ni}$) and then falls slowly to $7.59\ \text{MeV}$ for $^{235}\text{U}$. In light nuclei, every added nucleon finds more neighbours to bind to. In heavy nuclei, the electric repulsion of the many protons wins back part of the binding.

## Fission and fusion {Reactions}

A nuclear reaction releases energy when its products are *more tightly bound* than the nuclei it starts from. The energy released, the **Q-value**, is
```latex
\begin{aligned}
Q &= (m_\text{before} - m_\text{after}) \cdot c^2 \\
&= B_\text{after} - B_\text{before}
\end{aligned}
```
Both sides of the peak can climb towards it:

- In **fusion**, two light nuclei join into a heavier one. Deuterium and tritium give helium-4 and a neutron, with $Q = 17.6\ \text{MeV}$.
- In **fission**, a heavy nucleus splits into two medium-sized ones. A uranium-235 nucleus that absorbs a neutron releases about $200\ \text{MeV}$ in all.

<svg data-fig="qbars" viewBox="0 0 600 400" role="img" aria-label="Two bar charts of the total binding energy before and after a reaction; each has its own scale. Left, D–T fusion: before, deuterium plus tritium, 10.7 MeV; after, helium-4 plus a neutron, 28.3 MeV; the difference Q = 17.6 MeV is released. Right, fission of uranium-235 into barium-141, krypton-92 and three neutrons: before 1784 MeV, after 1957 MeV, Q = 173 MeV. In both, the products are more tightly bound." style="max-width:100%;font-size:26px">
  <foreignObject x="80" y="12.5" width="130" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{D–T fusion}$</div></foreignObject>
  <line x1="30" y1="330" x2="270" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="50" y="248" width="80" height="82" fill="#d0e6fb" stroke="#1971c2" stroke-width="2"/>
  <rect x="170" y="113" width="80" height="217" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="40.5" y="213.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10.7\ \text{MeV}$</div></foreignObject>
  <foreignObject x="160.5" y="78.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$28.3\ \text{MeV}$</div></foreignObject>
  <foreignObject x="67.5" y="341.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{D + T}$</div></foreignObject>
  <foreignObject x="175" y="341.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{4}\text{He + n}$</div></foreignObject>
  <line x1="130" y1="248" x2="270" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M260,248 V113" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="264" y="165" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="364.5" y="12.5" width="161" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">${}^{235}\text{U}\ \text{fission}$</div></foreignObject>
  <line x1="330" y1="330" x2="570" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="350" y="125" width="80" height="205" fill="#d0e6fb" stroke="#1971c2" stroke-width="2"/>
  <rect x="470" y="105" width="80" height="225" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="340.5" y="90.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1784\ \text{MeV}$</div></foreignObject>
  <foreignObject x="460.5" y="70.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1957\ \text{MeV}$</div></foreignObject>
  <foreignObject x="348.5" y="341.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{235}\text{U + n}$</div></foreignObject>
  <foreignObject x="475" y="341.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Ba + Kr}$</div></foreignObject>
  <line x1="430" y1="125" x2="570" y2="125" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M560,125 V105" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="564" y="99.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="34" y="369.5" width="532" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{total binding energy; each panel has its own scale}$</div></foreignObject>
</svg>

The figure shows one possible split of uranium-235, into barium-141, krypton-92 and three neutrons: it releases $173\ \text{MeV}$ at once, and the radioactive fragments release more later.

Fission was discovered in Berlin in December 1938 by Otto Hahn and Fritz Strassmann. Lise Meitner and Otto Frisch explained it at Christmas 1938 (published February 1939) and used $E = \Delta m \cdot c^2$ to estimate the energy. Fission gives about $0.85\ \text{MeV}$ per nucleon of fuel; D–T fusion gives $3.5\ \text{MeV}$ per nucleon, about four times more.

## Worked example

The atomic mass of helium-4 is $4.002603\ \text{u}$ (AME2020). Calculate the mass defect, the binding energy and the binding energy per nucleon of the helium-4 nucleus.

<!-- vaihe -->

**Given:** $m(^{4}\text{He}) = 4.002603\ \text{u}$, $Z = 2$, $N = 2$, $A = 4$; from AME2020, $m_\text{H} = 1.007825\ \text{u}$ and $m_\text{n} = 1.008665\ \text{u}$; ${1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}}$. **Find:** the mass defect $\Delta m$, the binding energy $B$ and $B/A$.

<!-- vaihe -->

**Principle:** The nucleus has less mass than its free nucleons; the difference times $c^2$ is the energy needed to separate them. Atomic masses are used, so the two protons are counted as two hydrogen-1 atoms and the two electrons cancel.

<!-- vaihe -->

**Formula:**
```latex
\begin{aligned}
\Delta m &= Z \cdot m_\text{H} + N \cdot m_\text{n} \\
&\quad - m(^{4}\text{He}) \\
B &= \Delta m \cdot c^2 \\
\frac{B}{A} &= \frac{\Delta m \cdot c^2}{A}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** The mass defect stays in $\text{u}$, and ${1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}}$ turns it into an energy in megaelectronvolts.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
\Delta m &= 2 \cdot 1.007825\ \text{u} \\
&\quad + 2 \cdot 1.008665\ \text{u} \\
&\quad - 4.002603\ \text{u} \\
&= 4.032980\ \text{u} - 4.002603\ \text{u} \\
&= 0.030377\ \text{u} \\[4pt]
B &= 0.030377\ \text{u} \cdot 931.5\ \text{MeV/u} \\
&= 28.30\ \text{MeV} \\[4pt]
\frac{B}{A} &= \frac{28.30\ \text{MeV}}{4} = 7.074\ \text{MeV}
\end{aligned}
```

<!-- vaihe -->

**Answer:** $\Delta m = 0.0304\ \text{u}$, $B = 28.3\ \text{MeV}$ and $B/A = 7.07\ \text{MeV}$ per nucleon. Three significant figures are enough, because $931.5\ \text{MeV/u}$ is given to four and the result is used only to three.

<!-- vaihe -->

**Reasonableness:** The mass defect is $0.030377 : 4.032980 = 0.75\ \%$ of the mass of the free particles: small, as expected, but far larger than in any chemical reaction. The value $7.07\ \text{MeV}$ is the point of $^{4}\text{He}$ on the binding energy curve.

## The people behind fission {People}

### Lise Meitner (1878–1968)

<!-- photo: lise-meitner -->

Lise Meitner was an Austrian physicist who worked for about thirty years in Berlin with the chemist Otto Hahn. In July 1938 she had to flee from Nazi Germany and moved to Sweden. In December Hahn wrote to her that uranium hit by neutrons gave barium, a much lighter element. Over Christmas 1938 Meitner and her nephew Otto Frisch worked out that the uranium nucleus had split in two, and with $E = \Delta m \cdot c^2$ they estimated about $200\ \text{MeV}$ per split. The Nobel Prize in Chemistry for 1944 went to Hahn alone, which many scientists see as unjust. Element 109, meitnerium, is named after her.

## Common misconception

"Binding energy is energy stored in the nucleus, and a nucleus with a large binding energy has a lot of energy to give." It is the other way round. Binding energy is the energy you must *add* to take a nucleus apart. A tightly bound nucleus has already given its energy away; energy is released when nuclei move *towards* larger $B/A$.

"In a nuclear reaction, protons and neutrons are destroyed and turned into energy." The number of nucleons stays the same before and after: in D–T fusion, $5$ nucleons go in and $5$ come out. Only the mass of the bound system changes.

## Summary

- Mass and energy are equivalent: $E = \Delta m \cdot c^2$, and $1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}$.
- A nucleus has less mass than its free nucleons. The mass defect times $c^2$ is the binding energy $B$, the energy needed to take the nucleus apart.
- The binding energy per nucleon $B/A$ peaks near iron-56 and nickel-62 at about $8.8\ \text{MeV}$.
- Fusion of light nuclei and fission of heavy nuclei both move towards the peak, so both release energy: $Q = B_\text{after} - B_\text{before}$.
- D–T fusion releases $17.6\ \text{MeV}$; the fission of uranium-235 about $200\ \text{MeV}$, but fusion gives more energy per nucleon of fuel.
