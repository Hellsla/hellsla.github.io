# Fusion reactions: from the Sun to deuterium and tritium

> **Why** must a fusion reactor on Earth be hotter than the centre of the Sun?

<!-- The fusion reaction and energy-scale components in inquiry.json read data-src="units/fy14/data/nuclides.json" (named here so that build.py embeds it and the content hash covers it). -->

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration in two halves. Left: a close view of the Sun&#x27;s core, a deep orange glow packed with many small particles close together. Right: a doughnut-shaped fusion machine cut open, with grey magnet coils around a vacuum chamber; inside it floats a thin ring of faint pink glowing gas, with only a few particles far apart." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy14fr-h-sun" cx="20%" cy="50%" r="75%"><stop offset="0" stop-color="#fff3bf"/><stop offset="0.35" stop-color="#ffc078"/><stop offset="0.75" stop-color="#e8590c"/><stop offset="1" stop-color="#a61e1e"/></radialGradient><linearGradient id="fy14fr-h-lab" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d3a46"/><stop offset="1" stop-color="#18212a"/></linearGradient><radialGradient id="fy14fr-h-pl" cx="50%" cy="50%" r="50%"><stop offset="0.55" stop-color="#f783ac" stop-opacity="0"/><stop offset="0.8" stop-color="#f783ac" stop-opacity="0.75"/><stop offset="1" stop-color="#f783ac" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="600" height="600" fill="url(#fy14fr-h-sun)"/>
  <circle cx="548" cy="446" r="3.2" fill="#ffd8a8"/>
  <circle cx="173.5" cy="118.5" r="3.2" fill="#fff4e6"/>
  <circle cx="250" cy="299.5" r="3.2" fill="#fff4e6"/>
  <circle cx="305.5" cy="426.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="68.5" cy="567" r="3.2" fill="#fff4e6"/>
  <circle cx="354" cy="346.5" r="3.2" fill="#fff4e6"/>
  <circle cx="195" cy="481" r="3.2" fill="#ffd8a8"/>
  <circle cx="318" cy="422.5" r="3.2" fill="#fff4e6"/>
  <circle cx="240.5" cy="454.5" r="3.2" fill="#fff4e6"/>
  <circle cx="201.5" cy="51" r="3.2" fill="#ffd8a8"/>
  <circle cx="460" cy="527.5" r="3.2" fill="#fff4e6"/>
  <circle cx="177" cy="546.5" r="3.2" fill="#fff4e6"/>
  <circle cx="491" cy="505" r="3.2" fill="#ffd8a8"/>
  <circle cx="497.5" cy="394.5" r="3.2" fill="#fff4e6"/>
  <circle cx="586.5" cy="436.5" r="3.2" fill="#fff4e6"/>
  <circle cx="227" cy="372.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="200.5" cy="22" r="3.2" fill="#fff4e6"/>
  <circle cx="85.5" cy="482.5" r="3.2" fill="#fff4e6"/>
  <circle cx="136" cy="445.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="441.5" cy="382" r="3.2" fill="#fff4e6"/>
  <circle cx="63" cy="92" r="3.2" fill="#fff4e6"/>
  <circle cx="7" cy="389.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="402.5" cy="65.5" r="3.2" fill="#fff4e6"/>
  <circle cx="438.5" cy="555" r="3.2" fill="#fff4e6"/>
  <circle cx="283" cy="464" r="3.2" fill="#ffd8a8"/>
  <circle cx="368" cy="231" r="3.2" fill="#fff4e6"/>
  <circle cx="258" cy="52.5" r="3.2" fill="#fff4e6"/>
  <circle cx="354.5" cy="450" r="3.2" fill="#ffd8a8"/>
  <circle cx="74" cy="300.5" r="3.2" fill="#fff4e6"/>
  <circle cx="557" cy="553" r="3.2" fill="#fff4e6"/>
  <circle cx="282" cy="237.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="221" cy="43.5" r="3.2" fill="#fff4e6"/>
  <circle cx="450" cy="473" r="3.2" fill="#fff4e6"/>
  <circle cx="228" cy="536" r="3.2" fill="#ffd8a8"/>
  <circle cx="573" cy="371.5" r="3.2" fill="#fff4e6"/>
  <circle cx="370" cy="327.5" r="3.2" fill="#fff4e6"/>
  <circle cx="432.5" cy="86.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="212.5" cy="478" r="3.2" fill="#fff4e6"/>
  <circle cx="281" cy="552" r="3.2" fill="#fff4e6"/>
  <circle cx="498.5" cy="424.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="95.5" cy="61.5" r="3.2" fill="#fff4e6"/>
  <circle cx="447" cy="82" r="3.2" fill="#fff4e6"/>
  <circle cx="473" cy="115" r="3.2" fill="#ffd8a8"/>
  <circle cx="272.5" cy="211" r="3.2" fill="#fff4e6"/>
  <circle cx="532.5" cy="356" r="3.2" fill="#fff4e6"/>
  <circle cx="524.5" cy="550.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="483.5" cy="205.5" r="3.2" fill="#fff4e6"/>
  <circle cx="564" cy="218.5" r="3.2" fill="#fff4e6"/>
  <circle cx="298" cy="337.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="413.5" cy="592.5" r="3.2" fill="#fff4e6"/>
  <circle cx="45" cy="24.5" r="3.2" fill="#fff4e6"/>
  <circle cx="179.5" cy="557" r="3.2" fill="#ffd8a8"/>
  <circle cx="494.5" cy="320.5" r="3.2" fill="#fff4e6"/>
  <circle cx="580" cy="177.5" r="3.2" fill="#fff4e6"/>
  <circle cx="56" cy="574" r="3.2" fill="#ffd8a8"/>
  <circle cx="196" cy="243" r="3.2" fill="#fff4e6"/>
  <circle cx="288.5" cy="434" r="3.2" fill="#fff4e6"/>
  <circle cx="575" cy="401.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="325" cy="128.5" r="3.2" fill="#fff4e6"/>
  <circle cx="45" cy="163.5" r="3.2" fill="#fff4e6"/>
  <circle cx="453.5" cy="84.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="509.5" cy="588" r="3.2" fill="#fff4e6"/>
  <circle cx="194" cy="434" r="3.2" fill="#fff4e6"/>
  <circle cx="19" cy="449.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="362.5" cy="522.5" r="3.2" fill="#fff4e6"/>
  <circle cx="490" cy="165.5" r="3.2" fill="#fff4e6"/>
  <circle cx="362" cy="264" r="3.2" fill="#ffd8a8"/>
  <circle cx="38.5" cy="562.5" r="3.2" fill="#fff4e6"/>
  <circle cx="582" cy="308" r="3.2" fill="#fff4e6"/>
  <circle cx="593" cy="257" r="3.2" fill="#ffd8a8"/>
  <circle cx="71.5" cy="125" r="3.2" fill="#fff4e6"/>
  <circle cx="6" cy="403" r="3.2" fill="#fff4e6"/>
  <circle cx="34.5" cy="291.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="498.5" cy="289.5" r="3.2" fill="#fff4e6"/>
  <circle cx="486" cy="381.5" r="3.2" fill="#fff4e6"/>
  <circle cx="467.5" cy="591.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="293" cy="164.5" r="3.2" fill="#fff4e6"/>
  <circle cx="251.5" cy="271" r="3.2" fill="#fff4e6"/>
  <circle cx="191.5" cy="111" r="3.2" fill="#ffd8a8"/>
  <circle cx="65.5" cy="280.5" r="3.2" fill="#fff4e6"/>
  <circle cx="395.5" cy="240" r="3.2" fill="#fff4e6"/>
  <circle cx="334.5" cy="482" r="3.2" fill="#ffd8a8"/>
  <circle cx="361.5" cy="362" r="3.2" fill="#fff4e6"/>
  <circle cx="298.5" cy="7.5" r="3.2" fill="#fff4e6"/>
  <circle cx="266.5" cy="447" r="3.2" fill="#ffd8a8"/>
  <circle cx="340" cy="510" r="3.2" fill="#fff4e6"/>
  <circle cx="521" cy="512.5" r="3.2" fill="#fff4e6"/>
  <circle cx="261.5" cy="352" r="3.2" fill="#ffd8a8"/>
  <circle cx="362" cy="544" r="3.2" fill="#fff4e6"/>
  <circle cx="425" cy="307.5" r="3.2" fill="#fff4e6"/>
  <circle cx="124" cy="315.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="322.5" cy="356" r="3.2" fill="#fff4e6"/>
  <circle cx="437" cy="296" r="3.2" fill="#fff4e6"/>
  <circle cx="370.5" cy="182.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="156" cy="75" r="3.2" fill="#fff4e6"/>
  <circle cx="424" cy="43" r="3.2" fill="#fff4e6"/>
  <circle cx="10" cy="8" r="3.2" fill="#ffd8a8"/>
  <circle cx="366" cy="20.5" r="3.2" fill="#fff4e6"/>
  <circle cx="483.5" cy="56" r="3.2" fill="#fff4e6"/>
  <circle cx="229.5" cy="184" r="3.2" fill="#ffd8a8"/>
  <circle cx="476" cy="80" r="3.2" fill="#fff4e6"/>
  <circle cx="520" cy="117" r="3.2" fill="#fff4e6"/>
  <circle cx="13.5" cy="340" r="3.2" fill="#ffd8a8"/>
  <circle cx="594.5" cy="329" r="3.2" fill="#fff4e6"/>
  <circle cx="366" cy="477" r="3.2" fill="#fff4e6"/>
  <circle cx="532" cy="483" r="3.2" fill="#ffd8a8"/>
  <circle cx="415" cy="330.5" r="3.2" fill="#fff4e6"/>
  <circle cx="421" cy="159.5" r="3.2" fill="#fff4e6"/>
  <circle cx="33.5" cy="236.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="461.5" cy="239.5" r="3.2" fill="#fff4e6"/>
  <circle cx="226" cy="301.5" r="3.2" fill="#fff4e6"/>
  <circle cx="417" cy="491.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="433.5" cy="398.5" r="3.2" fill="#fff4e6"/>
  <circle cx="249.5" cy="581.5" r="3.2" fill="#fff4e6"/>
  <circle cx="495.5" cy="88.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="591" cy="82" r="3.2" fill="#fff4e6"/>
  <circle cx="22.5" cy="312" r="3.2" fill="#fff4e6"/>
  <circle cx="149.5" cy="346" r="3.2" fill="#ffd8a8"/>
  <circle cx="73.5" cy="414.5" r="3.2" fill="#fff4e6"/>
  <circle cx="423" cy="293" r="3.2" fill="#fff4e6"/>
  <circle cx="247.5" cy="589" r="3.2" fill="#ffd8a8"/>
  <circle cx="322.5" cy="562.5" r="3.2" fill="#fff4e6"/>
  <circle cx="432" cy="400" r="3.2" fill="#fff4e6"/>
  <circle cx="331.5" cy="364.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="560" cy="91" r="3.2" fill="#fff4e6"/>
  <circle cx="172.5" cy="339" r="3.2" fill="#fff4e6"/>
  <circle cx="116.5" cy="552" r="3.2" fill="#ffd8a8"/>
  <circle cx="33.5" cy="555" r="3.2" fill="#fff4e6"/>
  <circle cx="588.5" cy="452" r="3.2" fill="#fff4e6"/>
  <circle cx="520" cy="564.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="264.5" cy="160.5" r="3.2" fill="#fff4e6"/>
  <circle cx="401" cy="358" r="3.2" fill="#fff4e6"/>
  <circle cx="124.5" cy="173.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="42" cy="521" r="3.2" fill="#fff4e6"/>
  <circle cx="355.5" cy="378" r="3.2" fill="#fff4e6"/>
  <circle cx="19.5" cy="174.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="334" cy="494.5" r="3.2" fill="#fff4e6"/>
  <circle cx="73.5" cy="115" r="3.2" fill="#fff4e6"/>
  <circle cx="530.5" cy="34" r="3.2" fill="#ffd8a8"/>
  <circle cx="342" cy="326.5" r="3.2" fill="#fff4e6"/>
  <circle cx="136" cy="466.5" r="3.2" fill="#fff4e6"/>
  <circle cx="478" cy="512.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="55" cy="110" r="3.2" fill="#fff4e6"/>
  <circle cx="221" cy="212" r="3.2" fill="#fff4e6"/>
  <circle cx="379.5" cy="588.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="325.5" cy="92.5" r="3.2" fill="#fff4e6"/>
  <circle cx="278.5" cy="591.5" r="3.2" fill="#fff4e6"/>
  <circle cx="384" cy="484.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="19" cy="477" r="3.2" fill="#fff4e6"/>
  <circle cx="194.5" cy="208.5" r="3.2" fill="#fff4e6"/>
  <circle cx="455.5" cy="17" r="3.2" fill="#ffd8a8"/>
  <circle cx="104.5" cy="334.5" r="3.2" fill="#fff4e6"/>
  <circle cx="88" cy="536.5" r="3.2" fill="#fff4e6"/>
  <circle cx="350" cy="487.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="567" cy="106.5" r="3.2" fill="#fff4e6"/>
  <circle cx="45" cy="239" r="3.2" fill="#fff4e6"/>
  <circle cx="333" cy="51.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="413.5" cy="416.5" r="3.2" fill="#fff4e6"/>
  <circle cx="302.5" cy="290.5" r="3.2" fill="#fff4e6"/>
  <circle cx="182" cy="41" r="3.2" fill="#ffd8a8"/>
  <circle cx="507" cy="338" r="3.2" fill="#fff4e6"/>
  <circle cx="280" cy="27.5" r="3.2" fill="#fff4e6"/>
  <circle cx="42" cy="410" r="3.2" fill="#ffd8a8"/>
  <circle cx="193.5" cy="201.5" r="3.2" fill="#fff4e6"/>
  <circle cx="271.5" cy="471.5" r="3.2" fill="#fff4e6"/>
  <circle cx="272" cy="374.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="432.5" cy="490" r="3.2" fill="#fff4e6"/>
  <circle cx="577.5" cy="346.5" r="3.2" fill="#fff4e6"/>
  <circle cx="531.5" cy="61" r="3.2" fill="#ffd8a8"/>
  <circle cx="469.5" cy="41" r="3.2" fill="#fff4e6"/>
  <circle cx="434.5" cy="246" r="3.2" fill="#fff4e6"/>
  <circle cx="67" cy="575" r="3.2" fill="#ffd8a8"/>
  <circle cx="28" cy="427.5" r="3.2" fill="#fff4e6"/>
  <circle cx="278.5" cy="391" r="3.2" fill="#fff4e6"/>
  <circle cx="66.5" cy="260.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="58" cy="234.5" r="3.2" fill="#fff4e6"/>
  <circle cx="107.5" cy="453.5" r="3.2" fill="#fff4e6"/>
  <circle cx="456" cy="470.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="287" cy="279" r="3.2" fill="#fff4e6"/>
  <circle cx="74" cy="114" r="3.2" fill="#fff4e6"/>
  <circle cx="444.5" cy="409" r="3.2" fill="#ffd8a8"/>
  <circle cx="314" cy="416.5" r="3.2" fill="#fff4e6"/>
  <circle cx="402" cy="433" r="3.2" fill="#fff4e6"/>
  <circle cx="449.5" cy="120.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="83.5" cy="451.5" r="3.2" fill="#fff4e6"/>
  <circle cx="48" cy="367.5" r="3.2" fill="#fff4e6"/>
  <circle cx="406" cy="501" r="3.2" fill="#ffd8a8"/>
  <circle cx="333.5" cy="226" r="3.2" fill="#fff4e6"/>
  <circle cx="234" cy="59.5" r="3.2" fill="#fff4e6"/>
  <circle cx="210" cy="474.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="118" cy="316" r="3.2" fill="#fff4e6"/>
  <circle cx="347" cy="494.5" r="3.2" fill="#fff4e6"/>
  <circle cx="546.5" cy="189.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="176" cy="174" r="3.2" fill="#fff4e6"/>
  <circle cx="42" cy="476" r="3.2" fill="#fff4e6"/>
  <circle cx="96" cy="564" r="3.2" fill="#ffd8a8"/>
  <circle cx="485" cy="419.5" r="3.2" fill="#fff4e6"/>
  <circle cx="115.5" cy="388" r="3.2" fill="#fff4e6"/>
  <circle cx="447" cy="382" r="3.2" fill="#ffd8a8"/>
  <circle cx="209.5" cy="221" r="3.2" fill="#fff4e6"/>
  <circle cx="518.5" cy="381.5" r="3.2" fill="#fff4e6"/>
  <circle cx="24.5" cy="576" r="3.2" fill="#ffd8a8"/>
  <circle cx="538.5" cy="422.5" r="3.2" fill="#fff4e6"/>
  <circle cx="294" cy="427.5" r="3.2" fill="#fff4e6"/>
  <circle cx="244" cy="120" r="3.2" fill="#ffd8a8"/>
  <circle cx="202.5" cy="508" r="3.2" fill="#fff4e6"/>
  <circle cx="136" cy="296.5" r="3.2" fill="#fff4e6"/>
  <circle cx="374" cy="428.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="521" cy="581" r="3.2" fill="#fff4e6"/>
  <circle cx="418.5" cy="573.5" r="3.2" fill="#fff4e6"/>
  <circle cx="50.5" cy="228" r="3.2" fill="#ffd8a8"/>
  <circle cx="471.5" cy="503" r="3.2" fill="#fff4e6"/>
  <circle cx="179" cy="314" r="3.2" fill="#fff4e6"/>
  <circle cx="36" cy="126.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="13.5" cy="367" r="3.2" fill="#fff4e6"/>
  <circle cx="433" cy="571.5" r="3.2" fill="#fff4e6"/>
  <circle cx="230" cy="336" r="3.2" fill="#ffd8a8"/>
  <circle cx="553" cy="373" r="3.2" fill="#fff4e6"/>
  <circle cx="28" cy="54" r="3.2" fill="#fff4e6"/>
  <circle cx="445.5" cy="581" r="3.2" fill="#ffd8a8"/>
  <circle cx="587.5" cy="86.5" r="3.2" fill="#fff4e6"/>
  <circle cx="153.5" cy="313.5" r="3.2" fill="#fff4e6"/>
  <circle cx="588" cy="412.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="442" cy="465.5" r="3.2" fill="#fff4e6"/>
  <circle cx="95" cy="58" r="3.2" fill="#fff4e6"/>
  <circle cx="486.5" cy="111" r="3.2" fill="#ffd8a8"/>
  <circle cx="354.5" cy="405.5" r="3.2" fill="#fff4e6"/>
  <circle cx="355" cy="272.5" r="3.2" fill="#fff4e6"/>
  <circle cx="225.5" cy="6.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="533.5" cy="528.5" r="3.2" fill="#fff4e6"/>
  <circle cx="13.5" cy="563" r="3.2" fill="#fff4e6"/>
  <circle cx="214.5" cy="466" r="3.2" fill="#ffd8a8"/>
  <circle cx="382.5" cy="522" r="3.2" fill="#fff4e6"/>
  <circle cx="217.5" cy="209.5" r="3.2" fill="#fff4e6"/>
  <circle cx="567.5" cy="430.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="563" cy="593" r="3.2" fill="#fff4e6"/>
  <circle cx="290" cy="95" r="3.2" fill="#fff4e6"/>
  <circle cx="104.5" cy="70" r="3.2" fill="#ffd8a8"/>
  <circle cx="500.5" cy="7" r="3.2" fill="#fff4e6"/>
  <circle cx="175.5" cy="404.5" r="3.2" fill="#fff4e6"/>
  <circle cx="357.5" cy="503.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="175" cy="222" r="3.2" fill="#fff4e6"/>
  <circle cx="272" cy="321.5" r="3.2" fill="#fff4e6"/>
  <circle cx="541" cy="313" r="3.2" fill="#ffd8a8"/>
  <circle cx="509.5" cy="170" r="3.2" fill="#fff4e6"/>
  <circle cx="489" cy="515" r="3.2" fill="#fff4e6"/>
  <circle cx="564.5" cy="437" r="3.2" fill="#ffd8a8"/>
  <circle cx="107.5" cy="23.5" r="3.2" fill="#fff4e6"/>
  <circle cx="493.5" cy="122" r="3.2" fill="#fff4e6"/>
  <circle cx="445.5" cy="112" r="3.2" fill="#ffd8a8"/>
  <circle cx="234.5" cy="483.5" r="3.2" fill="#fff4e6"/>
  <circle cx="277" cy="26.5" r="3.2" fill="#fff4e6"/>
  <circle cx="273" cy="13" r="3.2" fill="#ffd8a8"/>
  <circle cx="375" cy="7" r="3.2" fill="#fff4e6"/>
  <circle cx="459.5" cy="206" r="3.2" fill="#fff4e6"/>
  <circle cx="348.5" cy="119.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="516" cy="440.5" r="3.2" fill="#fff4e6"/>
  <circle cx="584.5" cy="555" r="3.2" fill="#fff4e6"/>
  <circle cx="170" cy="417.5" r="3.2" fill="#ffd8a8"/>
  <circle cx="475.5" cy="380.5" r="3.2" fill="#fff4e6"/>
  <rect x="600" y="0" width="600" height="600" fill="url(#fy14fr-h-lab)"/>
  <line x1="600" y1="0" x2="600" y2="600" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <ellipse cx="900" cy="320" rx="250" ry="130" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <ellipse cx="900" cy="320" rx="235" ry="118" fill="#3b4a58"/>
  <ellipse cx="900" cy="320" rx="215" ry="102" fill="url(#fy14fr-h-pl)"/>
  <ellipse cx="900" cy="320" rx="110" ry="46" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <ellipse cx="900" cy="320" rx="70" ry="28" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="1134" y="288" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="1101" y="350" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="1011.5" y="395.5" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="889" y="412" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="766.5" y="395.5" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="677" y="350" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="644" y="288" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="677" y="226" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="766.5" y="180.5" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="889" y="164" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="1011.5" y="180.5" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="1101" y="226" width="22" height="64" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="932" cy="245.5" r="3" fill="#ffdeeb"/>
  <circle cx="1072" cy="324" r="3" fill="#ffdeeb"/>
  <circle cx="939.5" cy="398" r="3" fill="#ffdeeb"/>
  <circle cx="875.5" cy="239.5" r="3" fill="#ffdeeb"/>
  <circle cx="981.5" cy="250.5" r="3" fill="#ffdeeb"/>
  <circle cx="1068" cy="314.5" r="3" fill="#ffdeeb"/>
  <circle cx="731.5" cy="305" r="3" fill="#ffdeeb"/>
  <circle cx="805.5" cy="262" r="3" fill="#ffdeeb"/>
  <circle cx="1067.5" cy="313" r="3" fill="#ffdeeb"/>
  <circle cx="771.5" cy="280.5" r="3" fill="#ffdeeb"/>
  <circle cx="732" cy="319.5" r="3" fill="#ffdeeb"/>
  <circle cx="802.5" cy="377.5" r="3" fill="#ffdeeb"/>
  <circle cx="969.5" cy="251" r="3" fill="#ffdeeb"/>
  <circle cx="786.5" cy="269.5" r="3" fill="#ffdeeb"/>
  <circle cx="951.5" cy="245" r="3" fill="#ffdeeb"/>
  <circle cx="1007.5" cy="270.5" r="3" fill="#ffdeeb"/>
  <circle cx="749" cy="333" r="3" fill="#ffdeeb"/>
  <circle cx="945" cy="247" r="3" fill="#ffdeeb"/>
</svg>

## The proton–proton chain {Chain}

The Sun turns hydrogen into helium in three steps, called the **proton–proton chain**. Hans Bethe and Charles Critchfield worked out its first step in 1938. Energies are from the AME2020 masses:

<svg data-fig="ppchain" viewBox="0 0 600 420" role="img" aria-label="The proton–proton chain in three numbered steps. Step 1, which happens twice: two hydrogen-1 nuclei fuse into hydrogen-2 plus a positron and a neutrino, releasing 1.44 MeV including the annihilation of the positron. Step 2, also twice: hydrogen-2 and hydrogen-1 fuse into helium-3 and a gamma-ray photon, 5.49 MeV. Step 3: two helium-3 nuclei fuse into helium-4 and two protons, 12.86 MeV. Total: four protons become one helium-4 nucleus, 26.7 MeV." style="max-width:100%;font-size:26px">
  <defs><radialGradient id="fy14fr-pp-p" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#ff8a80"/><stop offset="55%" stop-color="#c92a2a"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient><radialGradient id="fy14fr-pp-n" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="#e9ecef"/><stop offset="55%" stop-color="#9aa1a9"/><stop offset="100%" stop-color="#4b5259"/></radialGradient></defs>
  <circle cx="30" cy="70" r="18" fill="#1971c2"/>
  <foreignObject x="13.5" y="55.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\textbf{1}$</div></foreignObject>
  <foreignObject x="62" y="38.5" width="224" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">${}^{1}_{1}\text{H} + {}^{1}_{1}\text{H} \to {}^{2}_{1}\text{H} + \text{e}^{+} + \nu$</div></foreignObject>
  <foreignObject x="62" y="80.5" width="242" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$Q = 1.44\ \text{MeV}\quad (\text{twice})$</div></foreignObject>
  <circle cx="548" cy="74" r="11" fill="url(#fy14fr-pp-p)" stroke="#1f2933" stroke-width="1.2"/>
  <line x1="543" y1="74" x2="553" y2="74" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <line x1="548" y1="69" x2="548" y2="79" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <circle cx="566" cy="74" r="11" fill="url(#fy14fr-pp-n)" stroke="#1f2933" stroke-width="1.2"/>
  <line x1="30" y1="92" x2="30" y2="148" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="30" cy="170" r="18" fill="#1971c2"/>
  <foreignObject x="13.5" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\textbf{2}$</div></foreignObject>
  <foreignObject x="62" y="138.5" width="197" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">${}^{2}_{1}\text{H} + {}^{1}_{1}\text{H} \to {}^{3}_{2}\text{He} + \gamma$</div></foreignObject>
  <foreignObject x="62" y="180.5" width="242" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$Q = 5.49\ \text{MeV}\quad (\text{twice})$</div></foreignObject>
  <circle cx="548" cy="166" r="11" fill="url(#fy14fr-pp-n)" stroke="#1f2933" stroke-width="1.2"/>
  <circle cx="539" cy="182" r="11" fill="url(#fy14fr-pp-p)" stroke="#1f2933" stroke-width="1.2"/>
  <line x1="534" y1="182" x2="544" y2="182" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <line x1="539" y1="177" x2="539" y2="187" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <circle cx="557" cy="182" r="11" fill="url(#fy14fr-pp-p)" stroke="#1f2933" stroke-width="1.2"/>
  <line x1="552" y1="182" x2="562" y2="182" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <line x1="557" y1="177" x2="557" y2="187" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <line x1="30" y1="192" x2="30" y2="248" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="30" cy="270" r="18" fill="#1971c2"/>
  <foreignObject x="13.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\textbf{3}$</div></foreignObject>
  <foreignObject x="62" y="238.5" width="278" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">${}^{3}_{2}\text{He} + {}^{3}_{2}\text{He} \to {}^{4}_{2}\text{He} + 2\,{}^{1}_{1}\text{H}$</div></foreignObject>
  <foreignObject x="62" y="280.5" width="147" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c">$Q = 12.86\ \text{MeV}$</div></foreignObject>
  <circle cx="557" cy="266" r="11" fill="url(#fy14fr-pp-p)" stroke="#1f2933" stroke-width="1.2"/>
  <line x1="552" y1="266" x2="562" y2="266" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <line x1="557" y1="261" x2="557" y2="271" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <circle cx="539" cy="266" r="11" fill="url(#fy14fr-pp-n)" stroke="#1f2933" stroke-width="1.2"/>
  <circle cx="539" cy="282" r="11" fill="url(#fy14fr-pp-p)" stroke="#1f2933" stroke-width="1.2"/>
  <line x1="534" y1="282" x2="544" y2="282" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <line x1="539" y1="277" x2="539" y2="287" stroke="#ffffff" stroke-width="1.76" stroke-linecap="round"/>
  <circle cx="557" cy="282" r="11" fill="url(#fy14fr-pp-n)" stroke="#1f2933" stroke-width="1.2"/>
  <line x1="20" y1="330" x2="580" y2="330" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="174.5" y="350.5" width="251" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$4\,{}^{1}_{1}\text{H} \to {}^{4}_{2}\text{He} + 2\,\text{e}^{+} + 2\nu$</div></foreignObject>
  <foreignObject x="197.5" y="386.5" width="205" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#e8590c">$\text{total}\ Q = 26.7\ \text{MeV}$</div></foreignObject>
</svg>

1. Two protons fuse into a deuteron, $^{2}_{1}\text{H}$. One proton turns into a neutron, so a **positron** $\text{e}^+$ and a **neutrino** $\nu$ are emitted.
2. The deuteron captures another proton and becomes helium-3; a gamma-ray photon $\gamma$ carries off energy.
3. Two helium-3 nuclei, each from steps 1 and 2, fuse into helium-4 and give back two protons.

In total, four protons become one helium-4 nucleus, and $26.7\ \text{MeV}$ is released; about $2\ \%$ of it escapes with the neutrinos. The first step is extremely slow, because turning a proton into a neutron needs the **weak interaction**. An average proton in the Sun's core waits about $9$ billion years before it fuses. The Sun shines only because it holds an enormous number of protons.

## Key idea

Two nuclei are both positive, so they repel each other. To fuse, they must come within about $3\ \text{fm}$ of each other, where the strong force takes over. At this distance their electric potential energy is about $0.5\ \text{MeV}$. This energy hill is the **Coulomb barrier**.

<svg data-fig="barrier" viewBox="0 0 600 420" role="img" aria-label="Graph of the potential energy U in MeV of two hydrogen nuclei against the distance r between their centres in femtometres, from 0 to 20. Outside 3 fm the curve is the electric repulsion U = k e squared over r, drawn to scale: it rises from about 0.07 MeV at 20 fm to 0.48 MeV at 3 fm. Inside 3 fm the curve drops steeply into a deep well, the attraction of the strong force (schematic, not to scale). A horizontal line at 0.10 MeV stands for a fast nucleus: classically it would turn back at about 14 fm, but a dashed arrow shows it tunnelling through the barrier to the well." style="max-width:100%;font-size:26px">
  <line x1="170" y1="360" x2="170" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="360" x2="270" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="360" x2="370" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="360" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="70" y1="256.5" x2="470" y2="256.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="70" y1="153.5" x2="470" y2="153.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="70" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="69" y1="360" x2="484" y2="360" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,360 L483,366 L483,354 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="361" x2="70" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M70,24 L76,37 L64,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="170" y1="360" x2="170" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159" y="368.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$5$</div></foreignObject>
  <line x1="270" y1="360" x2="270" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252.5" y="368.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$10$</div></foreignObject>
  <line x1="370" y1="360" x2="370" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352.5" y="368.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$15$</div></foreignObject>
  <line x1="470" y1="360" x2="470" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="452.5" y="368.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$20$</div></foreignObject>
  <line x1="63" y1="256.5" x2="70" y2="256.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="9" y="241" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0.2$</div></foreignObject>
  <line x1="63" y1="153.5" x2="70" y2="153.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="9" y="138" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0.4$</div></foreignObject>
  <line x1="63" y1="50" x2="70" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="9" y="34.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0.6$</div></foreignObject>
  <foreignObject x="38" y="364.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0$</div></foreignObject>
  <foreignObject x="502" y="344.5" width="80" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$r\ (\text{fm})$</div></foreignObject>
  <foreignObject x="84" y="14.5" width="93" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$U\ (\text{MeV})$</span></div></foreignObject>
  <rect x="72" y="359.5" width="54" height="22" fill="#b2f2bb"/>
  <line x1="130" y1="112" x2="126" y2="382" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <line x1="74" y1="382" x2="126" y2="382" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="142" y="319.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{strong force}$</span></div></foreignObject>
  <polyline points="130,112 133,123 135.5,133.5 138.5,143 141.5,151.5 144,159.5 147,167 150,173.5 152.5,180 155.5,186 158.5,191.5 161,197 164,201.5 167,206.5 169.5,210.5 172.5,215 175.5,218.5 178,222.5 181,226 184,229.5 186.5,232.5 189.5,235.5 192.5,238.5 195,241 198,244 201,246.5 203.5,248.5 206.5,251 209.5,253 212,255.5 215,257.5 218,259.5 220.5,261 223.5,263 226.5,265 229,266.5 232,268 235,269.5 237.5,271.5 240.5,272.5 243.5,274 246,275.5 249,277 252,278 254.5,279.5 257.5,280.5 260.5,282 263,283 266,284 269,285 271.5,286 274.5,287 277.5,288 280,289 283,290 286,291 288.5,292 291.5,293 294.5,293.5 297,294.5 300,295.5 303,296 305.5,297 308.5,297.5 311.5,298.5 314,299 317,300 320,300.5 322.5,301 325.5,302 328.5,302.5 331,303 334,303.5 337,304 339.5,305 342.5,305.5 345.5,306 348,306.5 351,307 354,307.5 356.5,308 359.5,308.5 362.5,309 365,309.5 368,310 371,310.5 373.5,311 376.5,311.5 379.5,312 382,312.5 385,313 388,313 390.5,313.5 393.5,314 396.5,314.5 399,315 402,315 405,315.5 407.5,316 410.5,316.5 413.5,316.5 416,317 419,317.5 422,317.5 424.5,318 427.5,318.5 430.5,318.5 433,319 436,319.5 439,319.5 441.5,320 444.5,320.5 447.5,320.5 450,321 453,321 456,321.5 458.5,321.5 461.5,322 464.5,322.5 467,322.5 470,323" fill="none" stroke="#c92a2a" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="138" y="92.5" width="107" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0.48\ \text{MeV}$</span></div></foreignObject>
  <foreignObject x="250" y="174" width="76" height="62" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$U = \dfrac{ke^2}{r}$</span></div></foreignObject>
  <polyline points="358,308.5 470,308.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="358" cy="308.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="358" y1="308.5" x2="134" y2="308.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt" stroke-dasharray="8 7"/>
  <line x1="150" y1="308.5" x2="139" y2="308.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M126,308.5 L140,302 L140,314.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="162" y="270" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{tunnelling}$</span></div></foreignObject>
  <foreignObject x="325" y="320" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{fast nucleus}$</span></div></foreignObject>
</svg>

The temperature of the Sun's core is about $15.7$ million kelvin. There, the average kinetic energy of a nucleus is only $\frac{3}{2}kT \approx 2\ \text{keV}$, more than $200$ times too little. By classical physics, practically no nucleus would ever get over the barrier, and the Sun could not shine.

The answer is **quantum tunnelling**. A nucleus behaves partly like a wave, and it has a small probability of appearing on the other side of the barrier without having the energy to climb over it. George Gamow found this effect in 1928 for alpha decay, and in 1929 Robert Atkinson and Fritz Houtermans used it to calculate fusion in stars. Tunnelling is most likely for the fastest nuclei and for barriers that are low and thin, so fusion needs high temperatures, and it is easiest for the hydrogen isotopes, which have the smallest charge. Because of tunnelling, deuterium and tritium already fuse readily at collision energies of about $0.1\ \text{MeV}$, well below the $0.5\ \text{MeV}$ top of the barrier, and in a reactor plasma (about $15\ \text{keV}$) the fastest nuclei do most of the fusing.

## Formula: Sharing the energy of D–T fusion

The easiest reaction for a reactor is the fusion of deuterium and tritium:
```latex
{}^{2}_{1}\text{H} + {}^{3}_{1}\text{H} \to {}^{4}_{2}\text{He} + {}^{1}_{0}\text{n} + 17.6\ \text{MeV}
```
The reaction is balanced: $2 + 3 = 4 + 1$ nucleons and $1 + 1 = 2 + 0$ elementary charges. The energy appears as kinetic energy of the products. If the fuel nuclei are almost at rest, the total momentum is about zero, so the two products fly apart with equal and opposite momenta, $p_\alpha = p_\text{n} = p$. With $E_\text{k} = p^2/(2m)$, the lighter particle gets more energy:
```latex
\begin{aligned}
\frac{E_\text{n}}{E_\alpha} &= \frac{m_\alpha}{m_\text{n}} \approx 4 \\
E_\text{n} &= \frac{m_\alpha}{m_\alpha + m_\text{n}} \cdot Q
\end{aligned}
```
So the neutron carries $14.1\ \text{MeV}$ and the helium nucleus, the **alpha particle**, $3.5\ \text{MeV}$.

## Fusion in the laboratory {Lab}

A power plant cannot simply copy the Sun:

| | Sun's core | ITER (plan) |
| --- | --- | --- |
| fuel | protons | D and T |
| how hot | $1.6 \cdot 10^{7}\ \text{K}$ | $1.5 \cdot 10^{8}\ \text{K}$ |
| density | $150\ \text{g/cm}^3$ | $10^{-6}$ of air |
| held by | gravity | magnetic fields |
| power per $\text{m}^3$ | $280\ \text{W}$ | $0.6\ \text{MW}$ |

The Sun's reaction is far too slow for a machine, and its gravity holds a dense core for billions of years. A reactor must use the fastest reaction, D–T, in a thin plasma that it can hold only for seconds or less. To make enough nuclei tunnel in that short time, the plasma must be about ten times hotter than the Sun's core, which ITER plans at about $150$ million kelvin. "Hotter than the Sun" refers to the temperature only; the Sun's core has a far higher density and pressure.

The neutron has no charge, so magnetic fields cannot hold it: it leaves the plasma with $80\ \%$ of the energy and heats the wall around it, where its energy can be collected and where it can breed new tritium from lithium. The alpha particle is charged and stays in the plasma, keeping it hot.

## Worked example

This example repeats the calculation of the reaction diagram and the formula step by step, so that you can do it yourself. In D–T fusion, $Q = 17.6\ \text{MeV}$ is released. The nuclear masses are $m_\alpha = 4.0015\ \text{u}$ for the helium nucleus and $m_\text{n} = 1.0087\ \text{u}$ for the neutron. Calculate the kinetic energy of each product, assuming that the fuel nuclei are almost at rest.

<!-- vaihe -->

**Given:** $Q = 17.6\ \text{MeV}$, $m_\alpha = 4.0015\ \text{u}$, $m_\text{n} = 1.0087\ \text{u}$; the initial momentum is about zero. **Find:** $E_\text{n}$ and $E_\alpha$.

<!-- vaihe -->

**Principle:** Momentum is conserved: the products move in opposite directions with momenta of equal size $p$. Energy is conserved: $E_\text{n} + E_\alpha = Q$. The kinetic energy of a particle with momentum $p$ is $E_\text{k} = p^2/(2m)$.

<!-- vaihe -->

**Formula:** With the same $p$, the kinetic energies are inversely proportional to the masses, and they add up to $Q$:
```latex
\begin{aligned}
E_\text{n} &= \frac{m_\alpha}{m_\alpha + m_\text{n}} \cdot Q \\
E_\alpha &= \frac{m_\text{n}}{m_\alpha + m_\text{n}} \cdot Q
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** None: only the ratio of the masses is needed, so they can stay in $\text{u}$, and $Q$ stays in $\text{MeV}$. The sum of the masses is $4.0015\ \text{u} + 1.0087\ \text{u} = 5.0102\ \text{u}$.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
E_\text{n} &= \frac{4.0015\ \text{u}}{5.0102\ \text{u}} \cdot 17.6\ \text{MeV} \\
&= 0.7987 \cdot 17.6\ \text{MeV} \\
&= 14.06\ \text{MeV} \\[4pt]
E_\alpha &= \frac{1.0087\ \text{u}}{5.0102\ \text{u}} \cdot 17.6\ \text{MeV} \\
&= 0.2013 \cdot 17.6\ \text{MeV} \\
&= 3.54\ \text{MeV}
\end{aligned}
```

<!-- vaihe -->

**Answer:** The neutron gets $E_\text{n} \approx 14.1\ \text{MeV}$ and the alpha particle $E_\alpha \approx 3.5\ \text{MeV}$, as precise as $Q$ allows.

<!-- vaihe -->

**Reasonableness:** $14.1\ \text{MeV} + 3.5\ \text{MeV} = 17.6\ \text{MeV} = Q$. The neutron is about four times lighter, so it gets about four times as much energy: $14.06 : 3.54 = 3.97$. In a hot plasma the fuel nuclei are not quite at rest, so the measured neutron energies spread a little around $14.1\ \text{MeV}$.

## The people behind the first fusion experiment {People}

### Mark Oliphant (1901–2000)

<figure class="unit-photo"><img src="units/fy14/pics/oliphant.jpg" alt="Black-and-white photograph of Mark Oliphant, a man in a suit, photographed at Berkeley." width="1164" height="1600" loading="lazy"><figcaption>Mark Oliphant (1901–2000) was the first to fuse deuterium nuclei in a laboratory, at the Cavendish Laboratory in 1934, and discovered tritium and helium-3. <span class="photo-credit">Photo: Donald Cooksey, Lawrence Berkeley National Laboratory, public domain, via Wikimedia Commons</span></figcaption></figure>

Mark Oliphant was an Australian physicist from Adelaide. In 1927 he came to the Cavendish Laboratory in Cambridge to work with Ernest Rutherford. When a small amount of heavy water became available, he, Paul Harteck and Rutherford fired deuterons at deuterium and observed the first fusion reactions made on purpose, discovering tritium and helium-3 in 1934. Later, in Birmingham, his group developed the cavity magnetron, which made microwave radar possible. Back in Australia he founded a research school of physics in Canberra and served as Governor of South Australia from 1971 to 1976.

## Common misconception

"The Sun fuses deuterium and tritium, like a fusion reactor." The Sun fuses ordinary hydrogen through the slow proton–proton chain. D–T fusion is chosen for reactors because it is the fastest reaction at reachable temperatures; tritium hardly exists in nature and must be made.

"A reactor plasma is hotter than the Sun, so it is more extreme in every way." Only the temperature is higher. The Sun's core, $150\ \text{g/cm}^3$, is more than a hundred billion times denser than a reactor plasma, which is about a million times thinner than air, and its pressure is far higher.

"Nuclei fuse when they have enough energy to get over the Coulomb barrier." At the temperatures of the Sun and of reactors, almost all fusions happen by tunnelling, *below* the top of the barrier.

## Summary

- The Sun fuses four protons into helium-4 through the proton–proton chain and releases $26.7\ \text{MeV}$; its first step is very slow, because it needs the weak interaction.
- Positive nuclei repel: the Coulomb barrier is about $0.5\ \text{MeV}$, far more than the thermal energy: a few keV in the Sun, about $10\text{–}20\ \text{keV}$ in a reactor. Fusion happens by quantum tunnelling, mostly for the fastest nuclei.
- Oliphant, Harteck and Rutherford made the first fusion reactions in a laboratory in 1934 (D–D), discovering tritium and helium-3.
- D–T fusion releases $17.6\ \text{MeV}$; by momentum conservation the neutron gets $14.1\ \text{MeV}$ and the alpha particle $3.5\ \text{MeV}$.
- A reactor uses the fastest reaction, D–T, in a thin plasma held by magnets, so it needs about ten times the temperature of the Sun's core.
