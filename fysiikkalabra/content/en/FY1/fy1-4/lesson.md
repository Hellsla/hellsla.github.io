# Graphing and fitting a straight line

> **Why** do data points not usually all land exactly on one straight line, and yet a single line fitted to them can reveal the relationship between the quantities?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a sheet of grid paper on a table. On it are measured points that do not lie exactly on one straight line, and one straight line has been drawn through them with a ruler. A pencil lies beside it." class="fig-hero" style="max-width:100%;font-size:24px">
  <rect x="0" y="0" width="1200" height="600" fill="#f1dfb5"/>
  <line x1="0" y1="30" x2="1200" y2="14" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="98" x2="1200" y2="82" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="166" x2="1200" y2="150" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="234" x2="1200" y2="218" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="302" x2="1200" y2="286" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="370" x2="1200" y2="354" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="438" x2="1200" y2="422" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="506" x2="1200" y2="490" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="574" x2="1200" y2="558" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M260,40 L960,24 L976,566 L276,580 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="303" y1="572" x2="311" y2="32" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="268.5" y1="546" x2="968.5" y2="531" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="338" y1="571.5" x2="346" y2="31.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="269" y1="519" x2="969" y2="504" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="373" y1="571" x2="381" y2="31" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="269" y1="492" x2="969" y2="477" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="408" y1="570" x2="416" y2="30" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="269.5" y1="465" x2="969.5" y2="450" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="443" y1="569" x2="451" y2="29" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="438" x2="970" y2="423" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="478" y1="568.5" x2="486" y2="28.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270.5" y1="411" x2="970.5" y2="396" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="513" y1="568" x2="521" y2="28" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="271" y1="384" x2="971" y2="369" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="548" y1="567" x2="556" y2="27" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="271" y1="357" x2="971" y2="342" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="583" y1="566" x2="591" y2="26" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="271.5" y1="330" x2="971.5" y2="315" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="618" y1="565.5" x2="626" y2="25.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272" y1="303" x2="972" y2="288" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="653" y1="565" x2="661" y2="25" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272.5" y1="276" x2="972.5" y2="261" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="688" y1="564" x2="696" y2="24" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="273" y1="249" x2="973" y2="234" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="723" y1="563" x2="731" y2="23" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="273" y1="222" x2="973" y2="207" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="758" y1="562.5" x2="766" y2="22.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="273.5" y1="195" x2="973.5" y2="180" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="793" y1="562" x2="801" y2="22" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274" y1="168" x2="974" y2="153" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="828" y1="561" x2="836" y2="21" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274.5" y1="141" x2="974.5" y2="126" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="863" y1="560" x2="871" y2="20" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275" y1="114" x2="975" y2="99" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="898" y1="559.5" x2="906" y2="19.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275" y1="87" x2="975" y2="72" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="933" y1="559" x2="941" y2="19" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="60" x2="975.5" y2="45" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="339" y1="517.5" x2="913" y2="505" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="339" y1="517.5" x2="345.5" y2="74.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="353" y1="495.5" x2="891" y2="101" stroke="#e8590c" stroke-width="4" stroke-linecap="round"/>
  <circle cx="395.5" cy="462.5" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="459.5" cy="390.5" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="522.5" cy="384" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="587" cy="312.5" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="650" cy="295" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="714" cy="234" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="777.5" cy="206" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="841.5" cy="134" r="9" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <g transform="translate(652.5,340) rotate(-36.5)"><rect x="-330" y="0" width="660" height="56" rx="4" fill="#eef5f9" fill-opacity="0.75" stroke="#8a96a3" stroke-width="2"/><line x1="-320" y1="0" x2="-320" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="-304" y1="0" x2="-304" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-288" y1="0" x2="-288" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-272" y1="0" x2="-272" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-256" y1="0" x2="-256" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-240" y1="0" x2="-240" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="-224" y1="0" x2="-224" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-208" y1="0" x2="-208" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-192" y1="0" x2="-192" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-176" y1="0" x2="-176" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-160" y1="0" x2="-160" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="-144" y1="0" x2="-144" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-128" y1="0" x2="-128" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-112" y1="0" x2="-112" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-96" y1="0" x2="-96" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-80" y1="0" x2="-80" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="-64" y1="0" x2="-64" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-48" y1="0" x2="-48" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-32" y1="0" x2="-32" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="-16" y1="0" x2="-16" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="0" y1="0" x2="0" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="16" y1="0" x2="16" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="32" y1="0" x2="32" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="48" y1="0" x2="48" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="64" y1="0" x2="64" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="80" y1="0" x2="80" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="96" y1="0" x2="96" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="112" y1="0" x2="112" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="128" y1="0" x2="128" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="144" y1="0" x2="144" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="160" y1="0" x2="160" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="176" y1="0" x2="176" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="192" y1="0" x2="192" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="208" y1="0" x2="208" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="224" y1="0" x2="224" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="240" y1="0" x2="240" y2="30" stroke="#8a96a3" stroke-width="2"/><line x1="256" y1="0" x2="256" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="272" y1="0" x2="272" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="288" y1="0" x2="288" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="304" y1="0" x2="304" y2="18" stroke="#8a96a3" stroke-width="2"/><line x1="320" y1="0" x2="320" y2="30" stroke="#8a96a3" stroke-width="2"/></g>
  <g transform="translate(1040,300) rotate(-62)"><rect x="-150" y="-12" width="260" height="24" fill="#ffc078" stroke="#1f2933" stroke-width="2"/><path d="M110,-12 L150,0 L110,12 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/><path d="M138,-4 L150,0 L138,4 Z" fill="#1f2933"/><rect x="-176" y="-12" width="26" height="24" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/></g>
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
