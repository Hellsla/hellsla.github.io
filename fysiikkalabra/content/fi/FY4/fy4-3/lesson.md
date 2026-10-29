# Vuorovaikutus ja voima: Newtonin ensimmäinen ja kolmas laki

> **Miksi** curlingkivi liukuu jäällä kymmeniä metrejä, vaikka kukaan ei enää työnnä sitä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: curlinghalli. Vasemmalla heittäjä on liukunut matalassa heittoasennossa ja päästänyt kivestä irti, ja hänen ojennettu kätensä on jo kaukana kivestä. Keskellä punakahvainen curlingkivi liukuu jäällä oikealle, ja sen takana näkyy ohut jälki. Kaksi harjaajaa kulkee kiven edellä harjat jäätä vasten. Oikealla jäässä on maalialueen renkaat, joissa on jo kaksi kiveä." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy43h-roof" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy43h-ice" gradientUnits="userSpaceOnUse" x1="0" y1="370" x2="0" y2="600"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy43h-g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="0.55" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy43h-g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="0.55" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy43h-g0" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="0.55" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy43h-wall)"/>
  <rect x="0" y="0" width="1200" height="70" fill="url(#fy43h-roof)"/>
  <line x1="0" y1="70" x2="50" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="50" y1="8" x2="100" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="100" y1="70" x2="150" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="8" x2="200" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="200" y1="70" x2="250" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="250" y1="8" x2="300" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="70" x2="350" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="350" y1="8" x2="400" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="70" x2="450" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="450" y1="8" x2="500" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="70" x2="550" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="550" y1="8" x2="600" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="70" x2="650" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="650" y1="8" x2="700" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="700" y1="70" x2="750" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="750" y1="8" x2="800" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="70" x2="850" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="850" y1="8" x2="900" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="900" y1="70" x2="950" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="950" y1="8" x2="1000" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1000" y1="70" x2="1050" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1050" y1="8" x2="1100" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1100" y1="70" x2="1150" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1150" y1="8" x2="1200" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1200" y1="70" x2="1250" y2="8" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1250" y1="8" x2="1300" y2="70" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="8" x2="1200" y2="8" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="0" y1="70" x2="1200" y2="70" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <ellipse cx="100" cy="96" rx="70" ry="22" fill="#ffffff" fill-opacity="0.55"/>
  <rect x="60" y="82" width="80" height="12" rx="4" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <ellipse cx="300" cy="96" rx="70" ry="22" fill="#ffffff" fill-opacity="0.55"/>
  <rect x="260" y="82" width="80" height="12" rx="4" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <ellipse cx="500" cy="96" rx="70" ry="22" fill="#ffffff" fill-opacity="0.55"/>
  <rect x="460" y="82" width="80" height="12" rx="4" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <ellipse cx="700" cy="96" rx="70" ry="22" fill="#ffffff" fill-opacity="0.55"/>
  <rect x="660" y="82" width="80" height="12" rx="4" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <ellipse cx="900" cy="96" rx="70" ry="22" fill="#ffffff" fill-opacity="0.55"/>
  <rect x="860" y="82" width="80" height="12" rx="4" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <ellipse cx="1100" cy="96" rx="70" ry="22" fill="#ffffff" fill-opacity="0.55"/>
  <rect x="1060" y="82" width="80" height="12" rx="4" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <rect x="40" y="150" width="150" height="70" rx="4" fill="#f2a69c" stroke="#8a96a3" stroke-width="2"/>
  <rect x="56" y="168" width="70" height="10" fill="#ffffff"/>
  <rect x="56" y="188" width="110" height="8" fill="#ffffff" fill-opacity="0.7"/>
  <rect x="236" y="150" width="150" height="70" rx="4" fill="#d0e6fb" stroke="#8a96a3" stroke-width="2"/>
  <rect x="252" y="168" width="70" height="10" fill="#ffffff"/>
  <rect x="252" y="188" width="110" height="8" fill="#ffffff" fill-opacity="0.7"/>
  <rect x="432" y="150" width="150" height="70" rx="4" fill="#ffc078" stroke="#8a96a3" stroke-width="2"/>
  <rect x="448" y="168" width="70" height="10" fill="#ffffff"/>
  <rect x="448" y="188" width="110" height="8" fill="#ffffff" fill-opacity="0.7"/>
  <rect x="628" y="150" width="150" height="70" rx="4" fill="#b2f2bb" stroke="#8a96a3" stroke-width="2"/>
  <rect x="644" y="168" width="70" height="10" fill="#ffffff"/>
  <rect x="644" y="188" width="110" height="8" fill="#ffffff" fill-opacity="0.7"/>
  <rect x="824" y="150" width="150" height="70" rx="4" fill="#f2a69c" stroke="#8a96a3" stroke-width="2"/>
  <rect x="840" y="168" width="70" height="10" fill="#ffffff"/>
  <rect x="840" y="188" width="110" height="8" fill="#ffffff" fill-opacity="0.7"/>
  <rect x="1020" y="150" width="150" height="70" rx="4" fill="#d0e6fb" stroke="#8a96a3" stroke-width="2"/>
  <rect x="1036" y="168" width="70" height="10" fill="#ffffff"/>
  <rect x="1036" y="188" width="110" height="8" fill="#ffffff" fill-opacity="0.7"/>
  <rect x="0" y="240" width="1200" height="40" fill="#eef5f9" stroke="#8a96a3" stroke-width="2"/>
  <line x1="0" y1="240" x2="0" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="50" y1="240" x2="50" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="240" x2="100" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="240" x2="150" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="240" x2="200" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="240" x2="250" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="240" x2="300" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="240" x2="350" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="240" x2="400" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="450" y1="240" x2="450" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="240" x2="500" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="550" y1="240" x2="550" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="240" x2="600" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="650" y1="240" x2="650" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="240" x2="700" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="750" y1="240" x2="750" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="800" y1="240" x2="800" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="850" y1="240" x2="850" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="240" x2="900" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="950" y1="240" x2="950" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1000" y1="240" x2="1000" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1050" y1="240" x2="1050" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1100" y1="240" x2="1100" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1150" y1="240" x2="1150" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1200" y1="240" x2="1200" y2="280" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="0" y="300" width="1200" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="18" y="314" width="116" height="40" rx="3" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <rect x="32" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="168" y="314" width="116" height="40" rx="3" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="182" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="318" y="314" width="116" height="40" rx="3" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <rect x="332" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="468" y="314" width="116" height="40" rx="3" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <rect x="482" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="618" y="314" width="116" height="40" rx="3" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <rect x="632" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="768" y="314" width="116" height="40" rx="3" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="782" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="918" y="314" width="116" height="40" rx="3" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <rect x="932" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="1068" y="314" width="116" height="40" rx="3" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <rect x="1082" y="328" width="60" height="10" fill="#ffffff" fill-opacity="0.85"/>
  <rect x="0" y="296" width="1200" height="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="0" y="370" width="1200" height="230" fill="url(#fy43h-ice)"/>
  <line x1="0" y1="371" x2="1200" y2="371" stroke="#4f8fbf" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="67.5" cy="452" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="187" cy="589" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="134" cy="423.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="972.5" cy="430" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="238.5" cy="384" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="225.5" cy="394.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="816.5" cy="506" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1118" cy="567.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="806" cy="499" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1170.5" cy="396.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1046" cy="511.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="633.5" cy="430" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1105.5" cy="486.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="630.5" cy="407" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="383.5" cy="426" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="822" cy="520" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="647.5" cy="489" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="560" cy="594.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="47" cy="538.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1080" cy="558.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1126.5" cy="592" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="742" cy="429.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="933.5" cy="508.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="746.5" cy="583" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="927" cy="525" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="984" cy="555.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="381" cy="381" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="209" cy="580" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1132" cy="566" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1189" cy="560" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="782" cy="523" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1119" cy="458" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="704.5" cy="482" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="809" cy="446.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="769" cy="544" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="277.5" cy="399.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="933.5" cy="499" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1045" cy="387" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1133" cy="536.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="318.5" cy="523" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="63.5" cy="384" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1033" cy="594.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="550" cy="451" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="110.5" cy="564.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="268.5" cy="561" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1062" cy="416.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="902" cy="468.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="83" cy="536" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="529" cy="469.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1024" cy="554.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="996.5" cy="563.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="428.5" cy="573" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="894.5" cy="550" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="499.5" cy="554" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="476" cy="485" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="546" cy="482.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="360" cy="496" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="747.5" cy="474" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="806.5" cy="383" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="44.5" cy="562.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="296.5" cy="437" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="239" cy="515" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="5.5" cy="572.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="223" cy="532" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="831" cy="471" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1052" cy="501" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="828.5" cy="554.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1185.5" cy="393.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1139" cy="579" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="573.5" cy="496" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="752.5" cy="454" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1068" cy="516" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="6.5" cy="452" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="197.5" cy="422" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="458.5" cy="388.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="627.5" cy="446" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="267.5" cy="394" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1110.5" cy="421" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="973.5" cy="388.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1170" cy="497.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1004.5" cy="461" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="267.5" cy="405" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="284.5" cy="521" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="739.5" cy="525" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="287" cy="413" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1134.5" cy="519" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="75.5" cy="577.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="585.5" cy="468" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1038.5" cy="413.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="185" cy="406.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="481" cy="568.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="573" cy="561.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="895" cy="574" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="253" cy="491.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="143.5" cy="525" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="555.5" cy="466" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="590.5" cy="587.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="230" cy="391" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="819" cy="495.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1056.5" cy="514" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="755.5" cy="432.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="587" cy="514" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="657.5" cy="437" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1101" cy="483" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="234.5" cy="435" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="541.5" cy="540.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="331.5" cy="410.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="843" cy="468.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="246" cy="497.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="108" cy="579.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="896.5" cy="537.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="131.5" cy="575" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="743" cy="474" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="774" cy="575" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="153.5" cy="417" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="963" cy="553.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="169" cy="489" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="369.5" cy="524.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="405.5" cy="491.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="357" cy="383" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="120" cy="559.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="655.5" cy="421.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="349" cy="426" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="570.5" cy="565" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="405.5" cy="399" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1065.5" cy="497.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="897.5" cy="582" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="448.5" cy="543.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="322.5" cy="401.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="347.5" cy="587" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="669" cy="548.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="424" cy="554.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="697" cy="489" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="48" cy="450.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="236.5" cy="449" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="720.5" cy="423" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="929.5" cy="440.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="245.5" cy="584.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="604" cy="504" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="899.5" cy="526" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="307" cy="411.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="163.5" cy="502.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="494.5" cy="543.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="757.5" cy="459" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="379.5" cy="395.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="27.5" cy="456" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1058" cy="422" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1095" cy="524" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1025.5" cy="509" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="682" cy="471.5" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1196" cy="594.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1148" cy="539" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="325" cy="473" r="1" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="606" cy="434" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="716" cy="384.5" r="2.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="435" cy="387.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="64" cy="566.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="984.5" cy="380.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="202.5" cy="575.5" r="1.5" fill="#4f8fbf" fill-opacity="0.25"/>
  <circle cx="1032.5" cy="480.5" r="2" fill="#4f8fbf" fill-opacity="0.25"/>
  <line x1="0" y1="482" x2="1200" y2="482" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="374" x2="470" y2="598" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <line x1="1040" y1="374" x2="1040" y2="598" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="1040" cy="482" rx="180" ry="58" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="1040" cy="482" rx="124" ry="40" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="1040" cy="482" rx="74" ry="24" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="1040" cy="482" rx="26" ry="8" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M1085.5,470 Q1080,456.5 1087,443.5 H1133 Q1140,456.5 1134.5,470 Z" fill="url(#fy43h-g1)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1082,456.5 H1138" fill="none" stroke="#1f2933" stroke-width="2.9" stroke-linejoin="round"/>
  <circle cx="1092.5" cy="450.5" r="1.2" fill="#ffffff"/>
  <circle cx="1101.5" cy="451.5" r="1.2" fill="#ffffff"/>
  <circle cx="1110" cy="451" r="1.2" fill="#ffffff"/>
  <circle cx="1118.5" cy="454" r="1.2" fill="#ffffff"/>
  <circle cx="1127.5" cy="452.5" r="1.2" fill="#ffffff"/>
  <rect x="1106" y="437.5" width="8" height="6" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <path d="M1107.5,437.5 L1111,431.5 H1128.5" fill="none" stroke="#ffc078" stroke-width="4.35" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M942,500 Q936,485.5 943,471.5 H993 Q1000,485.5 994,500 Z" fill="url(#fy43h-g2)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M938,485.5 H998" fill="none" stroke="#1f2933" stroke-width="3.1" stroke-linejoin="round"/>
  <circle cx="949.5" cy="479.5" r="1.2" fill="#ffffff"/>
  <circle cx="958.5" cy="480" r="1.2" fill="#ffffff"/>
  <circle cx="968" cy="479.5" r="1.2" fill="#ffffff"/>
  <circle cx="977.5" cy="483" r="1.2" fill="#ffffff"/>
  <circle cx="986.5" cy="481.5" r="1.2" fill="#ffffff"/>
  <rect x="963.5" y="465.5" width="8.5" height="6" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <path d="M965.5,465.5 L969,459 H988" fill="none" stroke="#c92a2a" stroke-width="4.65" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M400,500 Q520,499 560,499" fill="none" stroke="#4f8fbf" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M470,468 h50" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.35"/>
  <path d="M450,482 h70" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.50"/>
  <path d="M480,494 h40" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.65"/>
  <ellipse cx="610" cy="502" rx="74" ry="9" fill="#4f8fbf" fill-opacity="0.25"/>
  <path d="M551,500 Q537.5,468.5 553.5,437.5 H662.5 Q678.5,468.5 665,500 Z" fill="url(#fy43h-g0)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M542.5,468.5 H673.5" fill="none" stroke="#1f2933" stroke-width="6.8" stroke-linejoin="round"/>
  <circle cx="567" cy="454.5" r="2.448" fill="#ffffff"/>
  <circle cx="587.5" cy="456.5" r="2.448" fill="#ffffff"/>
  <circle cx="608" cy="455" r="2.448" fill="#ffffff"/>
  <circle cx="628.5" cy="462.5" r="2.448" fill="#ffffff"/>
  <circle cx="649" cy="459" r="2.448" fill="#ffffff"/>
  <rect x="598.5" y="424" width="19" height="13.5" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <path d="M602.5,424 L610.5,410 H651.5" fill="none" stroke="#c92a2a" stroke-width="10.2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M236,452 L120,492" fill="none" stroke="#1f2933" stroke-width="26" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M106,498 h34" fill="none" stroke="#6c757d" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M236,452 L300,436 L306,488" fill="none" stroke="#1f2933" stroke-width="26" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M290,494 h46" fill="none" stroke="#1f2933" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M210,462 Q226,392 296,374 L320,402 Q276,432 266,464 Z" fill="#1971c2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M306,388 L426,438" fill="none" stroke="#1971c2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="432" cy="440" r="12" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <circle cx="342" cy="352" r="30" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M311,354 Q312,314 344,316 Q374,318 373,346 Q342,336 311,354 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M286,398 L176,472" fill="none" stroke="#1971c2" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="196" y1="456" x2="86" y2="494" stroke="#1f2933" stroke-width="6" stroke-linecap="round"/>
  <rect x="54" y="490" width="60" height="14" rx="4" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <path d="M770,372 L750,449" fill="none" stroke="#1f2933" stroke-width="15" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M740,452 h22" fill="none" stroke="#6c757d" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M795,304 L802,337" fill="none" stroke="#c92a2a" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M773,292 Q814,277 801,322 L782,377 H752 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M770,372 L790,449" fill="none" stroke="#1f2933" stroke-width="15" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M798,452 h22" fill="none" stroke="#6c757d" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M798,302 L802,337" fill="none" stroke="#c92a2a" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="802" cy="337" r="6.5" fill="#f1dfb5"/>
  <rect x="808" y="272" width="10" height="15" fill="#f1dfb5"/>
  <circle cx="813" cy="259" r="17" fill="#f1dfb5"/>
  <path d="M796,262 Q795,240 814,241 Q830,242 830,254 Q813,250 796,262 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="802" y1="337" x2="730" y2="486" stroke="#1f2933" stroke-width="6" stroke-linecap="round"/>
  <rect x="698" y="482" width="50" height="14" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <circle cx="692" cy="494" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="684" cy="490" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="676" cy="494" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="668" cy="490" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <path d="M850,494 L826,586.5" fill="none" stroke="#1f2933" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M814,590 h26.5" fill="none" stroke="#6c757d" stroke-width="9.6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M875,412.5 L888.5,452" fill="none" stroke="#1971c2" stroke-width="14.4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M849.5,398 Q898,380 884,434 L864.5,500 H828.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M850,494 L874,586.5" fill="none" stroke="#1f2933" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M883.5,590 h26.5" fill="none" stroke="#6c757d" stroke-width="9.6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M879,410 L888.5,452" fill="none" stroke="#1971c2" stroke-width="14.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="888.5" cy="452" r="7.8" fill="#f1dfb5"/>
  <rect x="887.5" y="374" width="12" height="18" fill="#f1dfb5"/>
  <circle cx="893.5" cy="358.5" r="20.4" fill="#f1dfb5"/>
  <path d="M873,362 Q872,335.5 895,337 Q914,338 914,352.5 Q893.5,347.5 873,362 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="888.5" y1="452" x2="748" y2="510" stroke="#1f2933" stroke-width="6" stroke-linecap="round"/>
  <rect x="716" y="506" width="50" height="14" rx="4" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="710" cy="518" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="702" cy="514" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="694" cy="518" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="686" cy="514" r="2.5" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
</svg>

## Ydinajatus
### Voima on vuorovaikutus
Kun kaksi kappaletta vaikuttavat toisiinsa, niiden välillä on **vuorovaikutus**: käsi työntää laatikkoa, naru vetää pulkkaa ja Maa vetää omenaa. Vuorovaikutuksen voimakkuutta kuvaa **voima**, jonka yksikkö on newton ($\text{N}$). Voima on vektori, jolla on suuruus ja suunta, ja sitä merkitään $\overline{F}$. Jokaisella voimalla on aiheuttaja, joka on aina toinen kappale. Kosketusvoimissa kappaleet koskettavat toisiaan. Maan vetovoima eli **paino** $\overline{G}$ ja magneettien voimat vaikuttavat myös etäältä.

### Liike jatkuu ilman voimaa
Curlingin heittäjä työntää kiveä vain hetken. Kun käsi irtoaa, mikään ei enää työnnä kiveä eteenpäin, mutta kivi liukuu silti kymmeniä metrejä. Liu'un aikana kiveen vaikuttavat vain Maa ja jää (ilmanvastus on hyvin pieni). Pystysuunnassa paino ja jään tukivoima eli jään kiveä ylöspäin tukeva, pintaa vastaan kohtisuora voima kumoavat toisensa. Vaakasuunnassa on vain jään pieni kitkavoima eli pintojen välinen liikettä vastustava voima, joka osoittaa taaksepäin ja hidastaa kiveä hyvin vähitellen.

<svg data-fig="curling" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa liukuvasta curlingkivestä. Vasemmalla tilannekuva: kivi liukuu jäällä oikealle, ja sen yllä ohut sininen nuoli v näyttää nopeuden oikealle. Heittäjän käsi on jäänyt kauas taakse. Oikealla voimakuvio: kivi suorakulmiona. Paino G osoittaa keskipisteestä alas, jään tukivoima N alapinnasta ylös yhtä pitkänä, ja jään pieni kitkavoima alapinnan takakulmasta vasemmalle. Eteenpäin osoittavaa voimaa ei ole. Kuva ei ole mittakaavassa: kitkavoiman nuoli on piirretty selvyyden vuoksi todellista pidemmäksi." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43c-ice" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy43c-granite" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="0.55" stop-color="#8a96a3"/><stop offset="1" stop-color="#6c757d"/></linearGradient></defs>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <rect x="16" y="230" width="270" height="46" fill="url(#fy43c-ice)"/>
  <line x1="16" y1="230" x2="286" y2="230" stroke="#4f8fbf" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="44" cy="214" r="11" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M16,206 Q26,210 33,212" fill="none" stroke="#1971c2" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M82,206 h34" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.4"/>
  <path d="M64,216 h52" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M88,224 h28" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M139.5,230 Q130,208 141.5,186 H218.5 Q230,208 220.5,230 Z" fill="url(#fy43c-granite)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M134,208 H226" fill="none" stroke="#1f2933" stroke-width="4.8" stroke-linejoin="round"/>
  <circle cx="151" cy="198" r="1.728" fill="#ffffff"/>
  <circle cx="165.5" cy="199.5" r="1.728" fill="#ffffff"/>
  <circle cx="180" cy="198" r="1.728" fill="#ffffff"/>
  <circle cx="194.5" cy="203.5" r="1.728" fill="#ffffff"/>
  <circle cx="209" cy="201" r="1.728" fill="#ffffff"/>
  <rect x="173.5" y="176" width="13.5" height="9.5" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <path d="M176,176 L182,166.5 H210.5" fill="none" stroke="#c92a2a" stroke-width="7.2" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="146" y1="150" x2="220" y2="150" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M209,156.5 L222,150 L209,143.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="227.5" y="131.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <rect x="397" y="148" width="110" height="48" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="452" y1="172" x2="452" y2="255" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M452,272 L444,254 L460,254 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="455.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="476" y1="196" x2="476" y2="113" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M476,96 L484,114 L468,114 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="479.5" y="87.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="397" y1="196" x2="390" y2="196" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M373,196 L391,188 L391,204 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="336.5" y="199.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

Jos kitkaa ei olisi lainkaan, kiven nopeus ei muuttuisi, ja se liukuisi samaan suuntaan loputtomiin. Tämä on **Newtonin ensimmäinen laki** eli **jatkavuuden laki**: jos kappaleeseen vaikuttavien voimien summa on nolla, kappale pysyy levossa tai liikkuu suoraviivaisesti tasaisella nopeudella. Voimaa tarvitaan liikkeen *muuttamiseen*, ei liikkeen ylläpitämiseen. Kappaleen taipumusta säilyttää liiketilansa sanotaan **inertiaksi** eli hitaudeksi.

Arkikokemus näyttää toista, koska maan päällä kitka ja ilmanvastus hidastavat lähes kaikkea, mikä liikkuu. Pyörä pysähtyy, kun polkeminen loppuu, koska tie ja ilma jarruttavat sitä, eivät siksi, että "liikkeen voima" kuluisi loppuun. Mitä pienempi kitka, sitä kauemmin liike jatkuu: jäällä pidemmälle kuin asfaltilla ja avaruudessa lähes rajatta.

### Voima ja vastavoima
Kun luistelija A työntää luistelijaa B, kumpikin lähtee liukumaan poispäin toisesta. B ei vain ota työntöä vastaan, vaan se vaikuttaa samalla A:han. Vuorovaikutus on aina kaksisuuntainen. Tämä on **Newtonin kolmas laki** eli **voiman ja vastavoiman laki**: kun kappale A vaikuttaa kappaleeseen B voimalla, B vaikuttaa A:han yhtä suurella mutta vastakkaissuuntaisella voimalla. Voima ja vastavoima syntyvät samassa vuorovaikutuksessa samaan aikaan, ja ne ovat samaa lajia: työntö ja vastatyöntö, vetovoima ja vastavetovoima.

<svg data-fig="luistelijat" viewBox="0 0 600 460" role="img" aria-label="Ylhäällä tilannekuva: kaksi luistelijaa seisoo jäällä vastakkain ja työntää toisiaan kämmenillä. Vasemmalla on suurikokoinen aikuinen A, oikealla pienempi lapsi B. Alhaalla kummankin voimakuvio erikseen, luistelija suorakulmiona. A:n kuviossa paino G A keskipisteestä alas, jään tukivoima N A alapinnasta ylös ja B:n voima A:han, F B A, joka osoittaa vasemmalle ja päättyy A:n oikeaan kylkeen. B:n kuviossa paino G B, joka on lyhyempi kuin A:n paino, tukivoima N B ja A:n voima B:hen, F A B, joka osoittaa oikealle ja päättyy B:n vasempaan kylkeen. Nuolet F B A ja F A B ovat yhtä pitkät. Kitka jätetään huomiotta." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43s-ice" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <rect x="16" y="172" width="568" height="26" fill="url(#fy43s-ice)"/>
  <line x1="16" y1="172" x2="584" y2="172" stroke="#4f8fbf" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M232,104 L221.5,166" fill="none" stroke="#1f2933" stroke-width="14.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M215.5,167.5 h19" fill="none" stroke="#1f2933" stroke-width="7.4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="211.5" y1="172" x2="239.5" y2="172" stroke="#8a96a3" stroke-width="2.22" stroke-linecap="round"/>
  <path d="M232,104 L241,166" fill="none" stroke="#1f2933" stroke-width="14.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M235,167.5 h19" fill="none" stroke="#1f2933" stroke-width="7.4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="230.5" y1="172" x2="258.5" y2="172" stroke="#8a96a3" stroke-width="2.22" stroke-linecap="round"/>
  <path d="M215.5,108.5 Q229,31.5 251,44.5 L250,108.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M239.5,49 L292,84" fill="none" stroke="#1971c2" stroke-width="11.84" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="292" cy="84" r="6.66" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="244" cy="15" r="17.76" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M225.5,16.5 Q226,-7 244,-5.5 Q261.5,-7 262.5,16.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M352,120.5 L360,167.5" fill="none" stroke="#1f2933" stroke-width="11.2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M364.5,168.5 h-14.5" fill="none" stroke="#1f2933" stroke-width="5.6" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="367.5" y1="172" x2="346.5" y2="172" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M352,120.5 L345.5,167.5" fill="none" stroke="#1f2933" stroke-width="11.2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M350,168.5 h-14.5" fill="none" stroke="#1f2933" stroke-width="5.6" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="353" y1="172" x2="332" y2="172" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M339.5,124 Q354,65.5 337.5,75.5 L338.5,124 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M346.5,79 L306,84" fill="none" stroke="#c92a2a" stroke-width="8.96" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="306" cy="84" r="5.04" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="343" cy="53.5" r="13.44" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M329,54.5 Q329.5,36.5 343,37.5 Q356.5,36.5 357,54.5 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="166" y="25.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="390" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <line x1="16" y1="214" x2="584" y2="214" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="125" y="300" width="70" height="60" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="160" y1="330" x2="160" y2="421" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M160,438 L152,420 L168,420 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="111.5" y="417.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_A$</div></foreignObject>
  <line x1="176" y1="360" x2="176" y2="269" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M176,252 L184,270 L168,270 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="179.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_A$</div></foreignObject>
  <line x1="252.5" y1="316" x2="212" y2="316" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M195,316 L213,308 L213,324 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="229.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{BA}$</div></foreignObject>
  <rect x="427" y="325" width="56" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="455" y1="345" x2="455" y2="390.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M455,407.5 L447,389.5 L463,389.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="460.5" y="389" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_B$</div></foreignObject>
  <line x1="443" y1="365" x2="443" y2="319.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M443,302.5 L451,320.5 L435,320.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="390.5" y="288" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_B$</div></foreignObject>
  <line x1="369.5" y1="337" x2="410" y2="337" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M427,337 L409,345 L409,329 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="324.5" y="300.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{AB}$</div></foreignObject>
  <foreignObject x="93" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{A}$</div></foreignObject>
  <foreignObject x="495" y="320.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{B}$</div></foreignObject>
</svg>

Aikuinen ja lapsi saavat toisiltaan yhtä suuren voiman, vaikka aikuinen on paljon raskaampi. Lapsi lähtee silti liikkeelle suuremmalla nopeudella, koska pienemmän massan liiketila muuttuu samasta voimasta enemmän; tähän palataan luvussa *Newtonin toinen laki*. Tärkeintä on, että voima ja vastavoima vaikuttavat **eri kappaleisiin**. Siksi ne eivät koskaan kumoa toisiaan, eikä niitä piirretä saman kappaleen voimakuvioon.

## Kaava: Newtonin ensimmäinen ja kolmas laki
Newtonin ensimmäinen laki on ehto kappaleeseen vaikuttavien voimien summalle:
```latex
\Sigma\overline{F} = \overline{0} \ \Leftrightarrow\ \overline{v} = \text{vakio}
```
missä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien vektorisumma eli **kokonaisvoima** (N) ja $\overline{v}$ kappaleen nopeus (m/s). Vakionopeus tarkoittaa, että sekä nopeuden suuruus että suunta pysyvät samoina; myös lepo $\overline{v} = \overline{0}$ on vakionopeus.

Kokonaisvoima nolla ei tarkoita, ettei voimia olisi, vaan että ne kumoavat toisensa. Suoralla tiellä tasaisella nopeudella ajavaan autoon vaikuttavat paino ja tien tukivoima pystysuunnassa sekä tien renkaisiin kohdistama voima eteenpäin ja ilmanvastus taaksepäin. Koska nopeus ei muutu, eteenpäin vievä voima on yhtä suuri kuin ilmanvastus, kun vierimisvastus jätetään huomiotta.

<svg data-fig="auto" viewBox="0 0 600 330" role="img" aria-label="Kaksi kuvaa autosta, joka ajaa suoralla tiellä tasaisella nopeudella. Vasemmalla tilannekuva: auto ja sen yllä ohut sininen nuoli v oikealle. Oikealla auton voimakuvio, auto suorakulmiona. Paino G keskipisteestä alas ja tien tukivoima N alapinnasta ylös, yhtä pitkinä. Tien voima F renkaisiin lähtee alapinnan etukulmasta eteenpäin, ja ilmanvastus F v lähtee auton takasivulta taaksepäin. Vaakasuorat nuolet ovat yhtä pitkät, joten voimat kumoavat toisensa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43a-car" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <rect x="16" y="236" width="270" height="34" fill="#c9c2b2"/>
  <line x1="16" y1="236" x2="286" y2="236" stroke="#1f2933" stroke-width="2.5" stroke-linecap="round"/>
  <rect x="30" y="251" width="30" height="5" fill="#ffffff"/>
  <rect x="86" y="251" width="30" height="5" fill="#ffffff"/>
  <rect x="142" y="251" width="30" height="5" fill="#ffffff"/>
  <rect x="198" y="251" width="30" height="5" fill="#ffffff"/>
  <rect x="254" y="251" width="30" height="5" fill="#ffffff"/>
  <path d="M52,222 Q50,196 74,192 L112,188 Q132,160 162,158 H206 Q228,160 242,186 L262,192 Q276,196 274,222 Z" fill="url(#fy43a-car)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M122,186 Q138,166 160,165 H178 V186 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M186,165 H204 Q220,168 230,186 H186 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="258" y="198" width="14" height="8" rx="2" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="98" cy="222" r="15" fill="#1f2933"/>
  <circle cx="98" cy="222" r="7" fill="#c4ccd4"/>
  <circle cx="228" cy="222" r="15" fill="#1f2933"/>
  <circle cx="228" cy="222" r="7" fill="#c4ccd4"/>
  <line x1="124" y1="128" x2="198" y2="128" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M187,134.5 L200,128 L187,121.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="205.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <rect x="386" y="146" width="120" height="48" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="446" y1="170" x2="446" y2="249" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M446,266 L438,248 L454,248 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="449.5" y="245.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="424" y1="194" x2="424" y2="115" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M424,98 L432,116 L416,116 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="385.5" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="506" y1="194" x2="541" y2="194" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M558,194 L540,202 L540,186 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="555.5" y="197.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <line x1="386" y1="164" x2="351" y2="164" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M334,164 L352,156 L352,172 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="305.5" y="127.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
</svg>

Newtonin kolmas laki kirjoitetaan kahden kappaleen välisille voimille:
```latex
\overline{F}_{AB} = -\overline{F}_{BA}
```
missä $\overline{F}_{AB}$ on voima, jolla kappale A vaikuttaa kappaleeseen B (N), ja $\overline{F}_{BA}$ voima, jolla B vaikuttaa A:han (N). Miinusmerkki kertoo, että voimat ovat vastakkaissuuntaiset; suuruudet ovat samat, $F_{AB} = F_{BA}$.

Laskuissa tarvitaan usein painon suuruutta:
```latex
G = mg
```
missä $G$ on paino (N), $m$ kappaleen massa (kg) ja $g = 9{,}81\,\text{m/s}^2$ putoamiskiihtyvyys. Painon vastavoima on kappaleen yhtä suuri vetovoima Maahan.

## Esimerkki
Matkustajakone lentää vaakasuoraan suoraan eteenpäin tasaisella nopeudella $850\,\text{km/h}$. Kumpikin sen kahdesta suihkumoottorista työntää ilmaa ja palokaasuja taaksepäin $48\,\text{kN}$:n voimalla. Kuinka suuri on koneeseen kohdistuva ilmanvastus?

<!-- vaihe -->

**Tunnetut ja kysytty.** Yhden moottorin voima kaasuihin $F_1 = 48\,\text{kN}$ taaksepäin, moottoreita on kaksi, ja nopeus $850\,\text{km/h}$ pysyy samana suuruudeltaan ja suunnaltaan. Kysytään ilmanvastusta $F_\text{v}$.

<!-- vaihe -->

**Periaate.** Newtonin kolmannen lain mukaan kaasut työntävät kutakin moottoria eteenpäin yhtä suurella voimalla $F_1$; se on moottorin työntövoima. Kone lentää suoraan tasaisella nopeudella, joten Newtonin ensimmäisen lain mukaan sen kokonaisvoima on nolla. Vaakasuunnassa koneeseen vaikuttavat vain kaksi työntövoimaa $\overline{F}_1$ ja $\overline{F}_2$ eteenpäin (molemmat $48\,\text{kN}$) ja ilmanvastus $\overline{F}_\text{v}$ taaksepäin, joten ne kumoavat toisensa. Pystysuunnassa siipien nostovoima ja paino kumoavat toisensa. Voimakuviossa kone on suorakulmio ja siihen vaikuttavat voimat ovat nuolia:

<svg data-fig="kone" viewBox="0 0 600 330" role="img" aria-label="Kaksi kuvaa matkustajakoneesta, joka lentää vaakasuoraan tasaisella nopeudella. Vasemmalla tilannekuva: kone ja sen yllä ohut sininen nuoli v oikealle. Oikealla koneen voimakuvio, kone suorakulmiona. Paino G keskipisteestä alas ja siipien nostovoima F noste ylös, yhtä pitkinä. Kahden moottorin työntövoimat F 1 ja F 2 lähtevät rungon etureunasta eteenpäin ja ovat yhtä pitkät. Ilmanvastus F v lähtee takareunasta taaksepäin ja on yhtä pitkä kuin työntövoimat yhteensä. Vaakasuorat voimat kumoavat toisensa, ja pystysuorat voimat kumoavat toisensa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43k-body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <path d="M44,214 Q40,196 62,192 L226,190 Q262,188 276,176 L262,214 Q150,230 44,214 Z" fill="url(#fy43k-body)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M62,192 L48,150 L74,150 L104,192 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M138,200 L196,200 L120,250 L100,250 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="160" cy="238" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="130" cy="244" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="150" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="170" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="190" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="210" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="230" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="124" y1="128" x2="198" y2="128" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M187,134.5 L200,128 L187,121.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="205.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <rect x="381" y="145" width="130" height="50" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="446" y1="170" x2="446" y2="253" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M446,270 L438,252 L454,252 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="407.5" y="249.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="476" y1="170" x2="476" y2="87" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M476,70 L484,88 L468,88 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="462.5" y="53.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{noste}$</div></foreignObject>
  <line x1="511" y1="158" x2="542" y2="158" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M559,158 L541,166 L541,150 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="550.5" y="123.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <line x1="511" y1="182" x2="542" y2="182" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M559,182 L541,190 L541,174 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="550.5" y="187.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <line x1="381" y1="170" x2="302" y2="170" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M285,170 L303,162 L303,178 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="254.5" y="133.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Valitaan positiivinen suunta eteenpäin ja ratkaistaan ilmanvastus:
```latex
\begin{aligned}
&\Sigma F_x = 2F_1 - F_\text{v} = 0 \\
&F_\text{v} = 2F_1
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Nopeutta $850\,\text{km/h}$ ei tarvita: riittää tietää, että se ei muutu. Voimat ovat kilonewtoneina, joten tulos saadaan suoraan kilonewtoneina: $48\,\text{kN} = 48\,000\,\text{N}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan moottorin voima yksikköineen:
```latex
\begin{aligned}
F_\text{v} &= 2F_1 \\
&= 2\cdot 48\,\text{kN} \\
&= 96\,\text{kN}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ilmanvastus on $96\,\text{kN}$ eli $9{,}6\cdot 10^{4}\,\text{N}$ ja osoittaa taaksepäin. Tarkkuus on kaksi merkitsevää numeroa kuten moottorin voimassa $48\,\text{kN}$.

<!-- vaihe -->

**Järkevyys.** Jos ilmanvastus olisi työntövoimia pienempi, kokonaisvoima osoittaisi eteenpäin ja kone kiihtyisi; jos suurempi, kone hidastuisi. Tasainen nopeus on mahdollinen vain, kun ilmanvastus on yhtä suuri kuin työntövoimien summa $2\cdot 48\,\text{kN}$. Tulos ei riipu nopeuden suuruudesta: sama päättely pätee kaikilla tasaisilla nopeuksilla.

## Yleinen virhekäsitys
Moni ajattelee, että liikkuvaan kappaleeseen täytyy vaikuttaa voima liikkeen suuntaan ja että liike loppuu, kun tämä voima "kuluu loppuun". Ensimmäisen lain mukaan näin ei ole: liukuvaan curlingkiveen ei vaikuta mikään eteenpäin, ja se hidastuu vain kitkan takia. Toinen yleinen virhe on luulla, että voima ja vastavoima kumoavat toisensa. Ne vaikuttavat eri kappaleisiin: hevonen vetää kärryä ja kärry hevosta, mutta kärryn liikkeen ratkaisevat vain kärryyn vaikuttavat voimat. Kolmas virhe on pitää pöydällä lepäävän kirjan painoa ja pöydän tukivoimaa voimana ja vastavoimana. Ne ovat yhtä suuret ensimmäisen lain takia. Tukivoiman vastavoima on kirjan voima pöytään ja painon vastavoima kirjan vetovoima Maahan.

## Tiivistelmä
- Voima kuvaa kahden kappaleen vuorovaikutusta. Jokaisella voimalla on aiheuttaja, toinen kappale, ja voiman yksikkö on newton.
- Newtonin ensimmäinen laki: jos kokonaisvoima on nolla, kappale pysyy levossa tai liikkuu suoraviivaisesti tasaisella nopeudella.
- Voimaa tarvitaan liikkeen muuttamiseen, ei sen ylläpitämiseen. Liike hidastuu arjessa kitkan ja ilmanvastuksen takia.
- Newtonin kolmas laki: $\overline{F}_{AB} = -\overline{F}_{BA}$. Voima ja vastavoima ovat yhtä suuret, vastakkaissuuntaiset ja samaa lajia, ja ne vaikuttavat eri kappaleisiin, joten ne eivät kumoa toisiaan.
