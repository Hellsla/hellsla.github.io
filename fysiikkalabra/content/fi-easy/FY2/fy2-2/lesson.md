# Energian muuntuminen ja yksikkö joule

> **Miksi** polkupyörän liike on lopulta peräisin Auringosta, ja miten energian määrän voi kertoa yhdellä luvulla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: Aurinko paistaa kultaiselle viljapellolle. Oranssit nuolet kulkevat Auringosta viljaan, viljasta leipään ja leivästä pyöräilijään. Pyöräilijä ajaa maantiellä. Liikkeen energia on siis peräisin Auringosta." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy22h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy22h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy22h-field" gradientUnits="userSpaceOnUse" x1="0" y1="370" x2="0" y2="500"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><linearGradient id="fy22h-road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#1f2933"/></linearGradient><linearGradient id="fy22h-board" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy22h-bread" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#b8622d"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="400" fill="url(#fy22h-sky)"/>
  <circle cx="110" cy="100" r="83" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M170.5,123.5 L197.5,123.5 L174,110 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M150.5,150.5 L174,164 L160.5,140.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M120,164 L133.5,187.5 L133.5,160.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M86.5,160.5 L86.5,187.5 L100,164 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M59.5,140.5 L46,164 L69.5,150.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M46,110 L22.5,123.5 L49.5,123.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M49.5,76.5 L22.5,76.5 L46,90 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M69.5,49.5 L46,36 L59.5,59.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M100,36 L86.5,12.5 L86.5,39.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M133.5,39.5 L133.5,12.5 L120,36 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M160.5,59.5 L174,36 L150.5,49.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M174,90 L197.5,76.5 L170.5,76.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="110" cy="100" r="52" fill="url(#fy22h-sun)"/>
  <path d="M628,96 Q626.5,69 658.5,72 Q671,43 703,53 Q732,37 748,67 Q777,70.5 773.5,96 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M956,152 Q955,131.5 979,134 Q988.5,112.5 1012.5,119.5 Q1034,107.5 1046,130.5 Q1067.5,133 1065,152 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,280 Q100,263 200,276 Q300,261 400,276.5 Q500,249.5 600,279 Q700,250.5 800,278.5 Q900,226.5 1000,283.5 Q1100,242.5 1200,280.5 Q1300,241 1400,280.5 V600 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M0,316 Q100,285 200,314 Q300,263.5 400,315.5 Q500,267.5 600,314.5 Q700,292 800,319 Q900,270 1000,317 Q1100,273.5 1200,319.5 Q1300,261.5 1400,317.5 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M0,340 L9.5,318.5 L18.5,340 L28.5,317.5 L38,340 L50,310 L62,340 L73.5,311 L85.5,340 L101.5,295.5 L118,340 L131.5,305.5 L145,340 L158.5,305 L172,340 L185.5,305 L199,340 L212.5,305 L226,340 L239.5,305 L253,340 L265,309.5 L277,340 L293.5,296 L309.5,340 L325,299 L340.5,340 L351,314.5 L362,340 L377,300.5 L391.5,340 L406,302.5 L420.5,340 L437,295 L453.5,340 L466,308 L478.5,340 L495,296 L511.5,340 L524.5,306.5 L537.5,340 L550.5,306 L564,340 L576.5,306.5 L589.5,340 L599.5,316.5 L609.5,340 L619.5,317 L629,340 L641.5,309 L653.5,340 L669.5,297 L685.5,340 L699,304.5 L712.5,340 L723,315.5 L733,340 L746.5,305.5 L760,340 L775,300 L790,340 L799.5,319 L808.5,340 L822.5,303.5 L836.5,340 L846,318.5 L855.5,340 L867.5,309.5 L879.5,340 L890.5,314.5 L901,340 L915.5,301 L930.5,340 L945,301 L960,340 L975.5,299 L991,340 L1003.5,307.5 L1016,340 L1028.5,308 L1041,340 L1053.5,308.5 L1066,340 L1078.5,308.5 L1091,340 L1100.5,317 L1110.5,340 L1123.5,306.5 L1136.5,340 L1149.5,307 L1162.5,340 L1179,295.5 L1195.5,340 L1206.5,313 L1217.5,340 V360 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="356" width="1200" height="244" fill="#b2f2bb"/>
  <path d="M0,370 H500 L470,500 H0 Z" fill="url(#fy22h-field)" stroke-linejoin="round"/>
  <line x1="6" y1="389" x2="8" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="8" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="19.5" y1="389" x2="21.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="21.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="26" y1="389" x2="28" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="28" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="38" y1="389" x2="40" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="40" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="47.5" y1="389" x2="49.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="49.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="58" y1="389" x2="60" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="60" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="68.5" y1="389" x2="70.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="70.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="76.5" y1="389" x2="78.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="78.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="87.5" y1="389" x2="89.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="89.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="98" y1="389" x2="100" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="100" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="110" y1="389" x2="112" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="112" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="119.5" y1="389" x2="121.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="121.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="126.5" y1="389" x2="128.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="128.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="140" y1="389" x2="142" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="142" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="149.5" y1="389" x2="151.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="151.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="158" y1="389" x2="160" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="160" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="169.5" y1="389" x2="171.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="171.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="177.5" y1="389" x2="179.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="179.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="188.5" y1="389" x2="190.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="190.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="197.5" y1="389" x2="199.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="199.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="209" y1="389" x2="211" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="211" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="218" y1="389" x2="220" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="220" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="228.5" y1="389" x2="230.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="230.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="237.5" y1="389" x2="239.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="239.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="246.5" y1="389" x2="248.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="248.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="257.5" y1="389" x2="259.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="259.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="268" y1="389" x2="270" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="270" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="276" y1="389" x2="278" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="278" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="286.5" y1="389" x2="288.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="288.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="297.5" y1="389" x2="299.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="299.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="310" y1="389" x2="312" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="312" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="319" y1="389" x2="321" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="321" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="327" y1="389" x2="329" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="329" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="337.5" y1="389" x2="339.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="339.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="347" y1="389" x2="349" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="349" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="358.5" y1="389" x2="360.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="360.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="370" y1="389" x2="372" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="372" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="379.5" y1="389" x2="381.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="381.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="388" y1="389" x2="390" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="390" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="399" y1="389" x2="401" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="401" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="408.5" y1="389" x2="410.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="410.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="419.5" y1="389" x2="421.5" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="421.5" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="428" y1="389" x2="430" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="430" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="437" y1="389" x2="439" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="439" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="449" y1="389" x2="451" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="451" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="459" y1="389" x2="461" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="461" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="467" y1="389" x2="469" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="469" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="478" y1="389" x2="480" y2="374.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="480" cy="372.5" rx="2.5" ry="5.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="6.5" y1="422.5" x2="8.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="8.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="22" y1="422.5" x2="24" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="24" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="34.5" y1="422.5" x2="36.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="36.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="47" y1="422.5" x2="49" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="49" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="59" y1="422.5" x2="61" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="61" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="74.5" y1="422.5" x2="76.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="76.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="87" y1="422.5" x2="89" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="89" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="99" y1="422.5" x2="101" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="101" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="112" y1="422.5" x2="114" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="114" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="125" y1="422.5" x2="127" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="127" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="136" y1="422.5" x2="138" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="138" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="151.5" y1="422.5" x2="153.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="153.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="164.5" y1="422.5" x2="166.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="166.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="176.5" y1="422.5" x2="178.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="178.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="191.5" y1="422.5" x2="193.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="193.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="202.5" y1="422.5" x2="204.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="204.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="215.5" y1="422.5" x2="217.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="217.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="228" y1="422.5" x2="230" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="230" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="244" y1="422.5" x2="246" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="246" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="256" y1="422.5" x2="258" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="258" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="269.5" y1="422.5" x2="271.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="271.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="282.5" y1="422.5" x2="284.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="284.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="292" y1="422.5" x2="294" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="294" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="307.5" y1="422.5" x2="309.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="309.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="321.5" y1="422.5" x2="323.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="323.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="332" y1="422.5" x2="334" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="334" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="347" y1="422.5" x2="349" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="349" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="357.5" y1="422.5" x2="359.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="359.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="373.5" y1="422.5" x2="375.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="375.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="383.5" y1="422.5" x2="385.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="385.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="397.5" y1="422.5" x2="399.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="399.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="411.5" y1="422.5" x2="413.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="413.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="423.5" y1="422.5" x2="425.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="425.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="436.5" y1="422.5" x2="438.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="438.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="450.5" y1="422.5" x2="452.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="452.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="461.5" y1="422.5" x2="463.5" y2="403" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="463.5" cy="401" rx="3.5" ry="7" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="6" y1="460" x2="8" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="8" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="22.5" y1="460" x2="24.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="24.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="39.5" y1="460" x2="41.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="41.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="55.5" y1="460" x2="57.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="57.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="74" y1="460" x2="76" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="76" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="88" y1="460" x2="90" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="90" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="104.5" y1="460" x2="106.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="106.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="120.5" y1="460" x2="122.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="122.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="136.5" y1="460" x2="138.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="138.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="152.5" y1="460" x2="154.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="154.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="167.5" y1="460" x2="169.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="169.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="185.5" y1="460" x2="187.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="187.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="201" y1="460" x2="203" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="203" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="215" y1="460" x2="217" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="217" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="233" y1="460" x2="235" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="235" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="248.5" y1="460" x2="250.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="250.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="266" y1="460" x2="268" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="268" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="280" y1="460" x2="282" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="282" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="297.5" y1="460" x2="299.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="299.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="312" y1="460" x2="314" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="314" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="328" y1="460" x2="330" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="330" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="344" y1="460" x2="346" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="346" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="358.5" y1="460" x2="360.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="360.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="374.5" y1="460" x2="376.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="376.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="391.5" y1="460" x2="393.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="393.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="409.5" y1="460" x2="411.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="411.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="424.5" y1="460" x2="426.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="426.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="438.5" y1="460" x2="440.5" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="440.5" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="456" y1="460" x2="458" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="458" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="473" y1="460" x2="475" y2="436" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="475" cy="433" rx="4.5" ry="9" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="7" y1="503" x2="9" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="9" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="26.5" y1="503" x2="28.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="28.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="45" y1="503" x2="47" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="47" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="66.5" y1="503" x2="68.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="68.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="84.5" y1="503" x2="86.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="86.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="104.5" y1="503" x2="106.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="106.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="123" y1="503" x2="125" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="125" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="139.5" y1="503" x2="141.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="141.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="161.5" y1="503" x2="163.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="163.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="177" y1="503" x2="179" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="179" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="197" y1="503" x2="199" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="199" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="218" y1="503" x2="220" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="220" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="236.5" y1="503" x2="238.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="238.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="253.5" y1="503" x2="255.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="255.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="272.5" y1="503" x2="274.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="274.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="292" y1="503" x2="294" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="294" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="312" y1="503" x2="314" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="314" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="331" y1="503" x2="333" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="333" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="348.5" y1="503" x2="350.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="350.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="367" y1="503" x2="369" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="369" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="386.5" y1="503" x2="388.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="388.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="407.5" y1="503" x2="409.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="409.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="427" y1="503" x2="429" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="429" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="444" y1="503" x2="446" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="446" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <line x1="462.5" y1="503" x2="464.5" y2="472.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <ellipse cx="464.5" cy="468.5" rx="5.5" ry="11.5" fill="#e9c98a" stroke="#a97a35" stroke-width="1"/>
  <path d="M0,500 H1200 V600 H0 Z" fill="url(#fy22h-road)" stroke-linejoin="round"/>
  <path d="M0,552 H1200" fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" stroke-dasharray="44 30"/>
  <rect x="0" y="496" width="1200" height="6" fill="#c9c2b2"/>
  <rect x="500" y="418" width="170" height="22" rx="6" fill="url(#fy22h-board)" stroke="#1f2933" stroke-width="3"/>
  <path d="M510,423.5 q42.5,-1.5 85,0 t65,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M510,429 q42.5,-1.5 85,0 t65,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M510,434.5 q42.5,-1.5 85,0 t65,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M512,418 Q508,352 585,346 Q662,352 658,418 Z" fill="url(#fy22h-bread)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M532,376 q12,-14 22,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <path d="M560,376 q12,-14 22,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <path d="M588,376 q12,-14 22,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <path d="M616,376 q12,-14 22,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="820" cy="446" r="56" fill="none" stroke="#1f2933" stroke-width="8.4"/>
  <circle cx="820" cy="446" r="50.4" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="820" y1="446" x2="868" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="861.5" y2="470" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="844" y2="487.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="820" y2="494" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="796" y2="487.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="778.5" y2="470" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="772" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="778.5" y2="422" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="796" y2="404.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="820" y2="398" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="844" y2="404.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="446" x2="861.5" y2="422" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="820" cy="446" r="5.04" fill="#1f2933"/>
  <circle cx="1020" cy="446" r="56" fill="none" stroke="#1f2933" stroke-width="8.4"/>
  <circle cx="1020" cy="446" r="50.4" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="1020" y1="446" x2="1068" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="1061.5" y2="470" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="1044" y2="487.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="1020" y2="494" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="996" y2="487.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="978.5" y2="470" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="972" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="978.5" y2="422" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="996" y2="404.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="1020" y2="398" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="1044" y2="404.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="446" x2="1061.5" y2="422" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="1020" cy="446" r="5.04" fill="#1f2933"/>
  <path d="M820,446 L892,446 L978,362 L878,362 Z" fill="none" stroke="#1971c2" stroke-width="6.72" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M892,446 L876,340" fill="none" stroke="#1971c2" stroke-width="6.72" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M978,362 L1020,446" fill="none" stroke="#1971c2" stroke-width="6.72" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M978,362 L972,340" fill="none" stroke="#1971c2" stroke-width="6.72" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M852,340 H882" fill="none" stroke="#1f2933" stroke-width="8.4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M958,342 Q972,334 990,342" fill="none" stroke="#1f2933" stroke-width="5.6" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="892" cy="446" r="11.2" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M868,332 L912,356 L904,458" fill="none" stroke="#1f2933" stroke-width="15" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M896,462 h16" fill="none" stroke="#6c757d" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M862,336 L928,272" fill="none" stroke="#c92a2a" stroke-width="22" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M928,272 L972,338" fill="none" stroke="#c92a2a" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="972" cy="338" r="6" fill="#f1dfb5"/>
  <circle cx="948" cy="256" r="15" fill="#f1dfb5"/>
  <path d="M930,255 Q936,234 956,237 Q968,242 965,252 Z" fill="#e8590c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M161.5,153 L242.5,319.5 L233.5,324 L260,340 L264,309 L255,313.5 L174.5,147 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M441.5,419 L476,412 L478,422 L500,400 L471,388.5 L473,398 L438.5,405 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M683,366.5 L799,316.5 L803,326 L820,300 L789.5,294.5 L793.5,304 L677,353.5 Z" fill="#e8590c" stroke-linejoin="round"/>
</svg>

## Ydinajatus
### Energia muuttuu muodosta toiseen
Energia on suure. Sen avulla kuvataan, mitä systeemissä voi tapahtua. Energia esiintyy eri muodoissa. Muotoja ovat esimerkiksi mekaaninen energia, kemiallinen energia, sähköenergia, lämpöenergia, säteily ja ydinenergia (luku *Energialajit ja energian säilyminen*). Arjessa energia on harvoin vain yhdessä muodossa. Se muuttuu muodosta toiseen monessa vaiheessa. Vaiheet muodostavat ketjun.

Pyöräilijän ketju alkaa Auringosta. Kasvi sitoo säteilyenergian kemialliseksi energiaksi. Kemiallinen energia päätyy kauraan ja aamupuuroon. Lihakset muuttavat osan puuron kemiallisesta energiasta pyörän liikkeeksi. Kun pysähdyt, liike-energia muuttuu lopulta renkaiden, jarrujen ja ilman lämpöenergiaksi.

<svg data-fig="ketju" viewBox="0 0 600 370" role="img" aria-label="Kaavakuva: energiaketju Auringosta pyöräilyyn. Aurinko lähettää säteilyenergiaa. Kasvi (kaura) sitoo sen kemialliseksi energiaksi ruokaan. Lihakset muuttavat osan siitä pyörän liikkeeksi. Loppu muuttuu lämpöenergiaksi. Joka vaiheessa osa energiasta siirtyy lämpönä ympäristöön (oranssit nuolet alas). Lopuksi myös liike-energia muuttuu lämpöenergiaksi. Nuolten pituus ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="106" y1="100" x2="120" y2="100" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="97" y1="122" x2="107" y2="132" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="75" y1="131" x2="75" y2="145" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="53" y1="122" x2="43" y2="132" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="44" y1="100" x2="30" y2="100" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="53" y1="78" x2="43" y2="68" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="75" y1="69" x2="75" y2="55" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="97" y1="78" x2="107" y2="68" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <circle cx="75" cy="100" r="23" fill="#ffc078" stroke="#e8590c" stroke-width="3"/>
  <line x1="181" y1="146" x2="181" y2="86" stroke="#a97a35" stroke-width="3" stroke-linecap="round"/>
  <path d="M181,88 q-9,-10 -7.2,-22 q7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M181,100 q9,-10 7.2,-22 q-7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M181,112 q-9,-10 -7.2,-22 q7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M181,124 q9,-10 7.2,-22 q-7.2,12 0.0,22 z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M203,114 L273,114 A35,30 0 0 1 203,114 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M209,114 Q238,100 267,114 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2" stroke-linejoin="round"/>
  <path d="M221,102 q-7,-9 0,-17 q7,-8 0,-16" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <path d="M238,102 q-7,-9 0,-17 q7,-8 0,-16" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <path d="M255,102 q-7,-9 0,-17 q7,-8 0,-16" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="345" cy="112" r="24" fill="none" stroke="#1f2933" stroke-width="3"/>
  <circle cx="345" cy="112" r="3" fill="#1f2933"/>
  <circle cx="405" cy="112" r="24" fill="none" stroke="#1f2933" stroke-width="3"/>
  <circle cx="405" cy="112" r="3" fill="#1f2933"/>
  <line x1="345" y1="112" x2="369" y2="86" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="369" y1="86" x2="405" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="345" y1="112" x2="375" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="375" y1="112" x2="369" y2="86" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="397" y1="80" x2="405" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="391" y1="78" x2="403" y2="78" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="363" y1="84" x2="373" y2="84" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <rect x="517" y="50" width="16" height="72" rx="8" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="525" cy="130" r="16" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="521" y="84" width="8" height="46" fill="#c92a2a"/>
  <line x1="537" y1="62" x2="547" y2="62" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="537" y1="74" x2="547" y2="74" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="537" y1="86" x2="547" y2="86" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M130,107 L158,107 L158,115 L180,100 L158,85 L158,93 L130,93 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M280,107 L308,107 L308,115 L330,100 L308,85 L308,93 L280,93 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M430,107 L458,107 L458,115 L480,100 L458,85 L458,93 L430,93 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="136" y="29.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kasvi}$</div></foreignObject>
  <foreignObject x="5" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Aurinko}$</div></foreignObject>
  <foreignObject x="5" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{säteily}$</div></foreignObject>
  <foreignObject x="155" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Puuro}$</div></foreignObject>
  <foreignObject x="155" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="305" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Pyöräily}$</div></foreignObject>
  <foreignObject x="305" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{liike}$</div></foreignObject>
  <foreignObject x="455" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Ympäristö}$</div></foreignObject>
  <foreignObject x="455" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lämpö}$</div></foreignObject>
  <rect x="30" y="300" width="540" height="44" rx="8" fill="#f2a69c"/>
  <foreignObject x="150" y="307.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpöä ympäristöön}$</div></foreignObject>
  <path d="M218,232 L218,274 L210,274 L225,296 L240,274 L232,274 L232,232 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M368,232 L368,274 L360,274 L375,296 L390,274 L382,274 L382,232 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M518,232 L518,274 L510,274 L525,296 L540,274 L532,274 L532,232 Z" fill="#e8590c" stroke-linejoin="round"/>
</svg>

Joka vaiheessa osa energiasta muuttuu lämpöenergiaksi. Lämpöenergia siirtyy lämpönä ympäristöön ja hajaantuu. Energiaa ei silti katoa. Luvussa *Energialajit ja energian säilyminen* todettiin, että ketjun alussa ja lopussa energiaa on yhtä paljon. Kuvan esimerkissä puuron $800\,\text{kJ}$ jakautuu liikkeeksi ja lämpöenergiaksi. Osat ovat yhteensä yhtä paljon kuin alussa. Lämpöenergia hajaantuu niin laajalle, ettei sitä ole enää helppo käyttää hyödyksi. Siksi energia tuntuu "kuluvan loppuun".

<svg data-fig="sailyminen" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva mittakaavassa (esimerkki): pyöräilijän aamupuuron kemiallisesta energiasta on 800 kJ. Lihakset muuttavat siitä liikkeeksi 200 kJ ja lämpöenergiaksi 600 kJ. Nuolten leveys on verrannollinen energiaan. Haarojen yhteinen leveys on yhtä suuri kuin alkuperäisen nuolen leveys." style="max-width:100%;font-size:24px">
  <rect x="40" y="112" width="192" height="96" fill="#ffc078" stroke="#e8590c" stroke-width="2"/>
  <path d="M232,112 L400,112 L400,98 L452,124 L400,150 L400,136 L232,136 Z" fill="#ffc078" stroke="#e8590c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M232,136 L304,136 L304,262 L326,262 L268,302 L210,262 L232,262 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="100" y="23.5" width="400" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$800\,\text{kJ} = 200\,\text{kJ} + 600\,\text{kJ}$</div></foreignObject>
  <foreignObject x="52" y="129.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="52" y="167.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800\,\text{kJ}$</div></foreignObject>
  <foreignObject x="244" y="63.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{liike: }200\,\text{kJ}$</div></foreignObject>
  <foreignObject x="340" y="217.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämpö: }600\,\text{kJ}$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="460" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nuolen leveys kuvaa energian määrää}$</div></foreignObject>
</svg>

### Joule
Energian symboli on $E$. Energian yksikkö on joule, ja sen merkki on J. Yksi joule on pieni energia. Sen verran energiaa tarvitaan suunnilleen siihen, että nostat omenan metrin verran ylöspäin. Omena painaa noin $0{,}1\,\text{kg}$. Tässä luvussa opit joulen suuruuden esimerkkien avulla.

## Kaava: Energian yksikkö ja kerrannaisyksiköt
Arjen energiat ovat jouleina isoja lukuja. Siksi käytetään etuliitteitä (luku *Suureet, yksiköt ja SI-järjestelmä*): kilo (k), mega (M), giga (G) ja tera (T). Jokainen etuliite on tuhatkertainen edelliseen verrattuna:
```latex
\begin{aligned}
1\,\text{kJ} &= 1000\,\text{J} \\
1\,\text{MJ} &= 1000\,\text{kJ} \\
1\,\text{GJ} &= 1000\,\text{MJ} \\
1\,\text{TJ} &= 1000\,\text{GJ}
\end{aligned}
```
missä J on joule, kJ kilojoule, MJ megajoule, GJ gigajoule ja TJ terajoule. Megajoulessa on siis $1000 \cdot 1000\,\text{J} = 1\,000\,000\,\text{J}$.

Muunnos tehdään näin: korvaa etuliite sen arvolla. Esimerkki: $2{,}5\,\text{kJ} = 2{,}5 \cdot 1000\,\text{J} = 2500\,\text{J}$. Toiseen suuntaan luku kirjoitetaan etuliitteen avulla: $3000\,\text{J} = 3 \cdot 1000\,\text{J} = 3\,\text{kJ}$. Energioita lasketaan yhteen vain samassa yksikössä. Muunna ne siis ensin samaan yksikköön.

Arjen energioiden suuruusluokat on koottu kuvaan. Kuvassa jokainen väli on kymmenkertainen (luku *Fysiikka tieteenä ja maailmankaikkeuden mittasuhteet*). Joskus kahden energian suuruusluokka on hyvin erilainen. Silloin vertailuun riittää yksi jakolasku. Esimerkki: bensiinilitran $32\,\text{MJ}$ ja päivän ruoan $10\,\text{MJ}$ suhde on $32\,\text{MJ} : 10\,\text{MJ} \approx 3$.

<svg data-fig="tikapuut" viewBox="0 0 600 372" role="img" aria-label="Kuvaaja mittakaavassa: energia jouleina kymmenpotenssiasteikolla 1 J:sta 10 TJ:iin ja yli. Jokainen väli on kymmenkertainen. Omena metrin ylös on noin 1 J. Palava tulitikku on noin 1 kJ. Päivän ruoka on noin 10 MJ. 50 litran bensiinitankki on noin 1,6 GJ. Ydinvoimala Olkiluoto 3 tuottaa vuorokaudessa noin 140 TJ sähköä." style="max-width:100%;font-size:24px">
  <line x1="66" y1="292" x2="574" y2="292" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M586,292 L573,298 L573,286 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="292" x2="96" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="129" y1="292" x2="129" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="162.5" y1="292" x2="162.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="195.5" y1="292" x2="195.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="229" y1="292" x2="229" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="292" x2="262" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="295" y1="292" x2="295" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="328.5" y1="292" x2="328.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361.5" y1="292" x2="361.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="292" x2="395" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="428" y1="292" x2="428" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="461" y1="292" x2="461" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="494.5" y1="292" x2="494.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="527.5" y1="292" x2="527.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="561" y1="292" x2="561" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="51" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{J}$</div></foreignObject>
  <foreignObject x="150.5" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{kJ}$</div></foreignObject>
  <foreignObject x="250" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{MJ}$</div></foreignObject>
  <foreignObject x="350" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{GJ}$</div></foreignObject>
  <foreignObject x="449.5" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{TJ}$</div></foreignObject>
  <foreignObject x="130" y="335.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jokainen väli on 10-kertainen}$</div></foreignObject>
  <line x1="96" y1="264" x2="96" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="96" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="106" y="237.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{omena metrin ylös}\ 1\,\text{J}$</div></foreignObject>
  <line x1="195.5" y1="226" x2="195.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="195.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="-4.5" y="199.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{tulitikku}\ 1\,\text{kJ}$</div></foreignObject>
  <line x1="328.5" y1="188" x2="328.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="328.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="58.5" y="161.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{päivän ruoka}\ 10\,\text{MJ}$</div></foreignObject>
  <line x1="401.5" y1="150" x2="401.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="401.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="91.5" y="123.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{bensiinitankki}\ 1{,}6\,\text{GJ}$</div></foreignObject>
  <line x1="565.5" y1="112" x2="565.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="565.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="215.5" y="85.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{Olkiluoto 3, vrk}\ 140\,\text{TJ}$</div></foreignObject>
</svg>

Energian määrä ei vielä kerro, kuinka nopeasti energiaa käytetään. Sitä kuvataan seuraavassa luvussa *Teho*.

## Esimerkki
Pyöräilijä syö banaanin. Banaanin kemiallinen energia on $0{,}45\,\text{MJ}$. Lihakset muuttavat siitä pyöräilyn liikkeeksi $110\,\text{kJ}$. Loppu muuttuu lämpöenergiaksi. Kuinka paljon energiaa muuttuu lihaksissa ja kehossa lämpöenergiaksi? Anna vastaus kilojouleina.

<!-- vaihe -->

**Tunnetut ja kysytty.** Kemiallinen energia alussa on $E_\text{alussa} = 0{,}45\,\text{MJ}$. Liikkeeksi muuttunut energia on $E_\text{liike} = 110\,\text{kJ}$. Kysytään lämpöenergiaa $E_\text{lämpö}$ kilojouleina.

<!-- vaihe -->

**Periaate.** Energia säilyy. Banaanin kemiallinen energia ei katoa. Se muuttuu kokonaan liikkeeksi ja lämpöenergiaksi. Alun energia on siis yhtä suuri kuin liikkeeksi ja lämpöenergiaksi muuttuneiden energioiden summa.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&E_\text{alussa} = E_\text{liike} + E_\text{lämpö} \\
&E_\text{lämpö} = E_\text{alussa} - E_\text{liike}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Energiat lasketaan samassa yksikössä. Korvaa megajoulen etuliite sen arvolla: $0{,}45\,\text{MJ} = 0{,}45 \cdot 1000\,\text{kJ} = 450\,\text{kJ}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
E_\text{lämpö} &= E_\text{alussa} - E_\text{liike} \\
&= 450\,\text{kJ} - 110\,\text{kJ} \\
&= 340\,\text{kJ}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lämpöenergiaksi muuttuu $340\,\text{kJ}$. Tulos on pyöristetty kahden merkitsevän numeron tarkkuuteen. Alkuenergia $0{,}45\,\text{MJ}$ ja liike $110\,\text{kJ}$ on nimittäin annettu kahdella numerolla.

<!-- vaihe -->

**Järkevyys.** Lämpöenergiaksi muuttuu enemmän energiaa kuin liikkeeksi. Näin on ihmisen lihasten toiminnassa yleensä: keho lämpenee pyöräillessä. Summa tarkistuu: $110\,\text{kJ} + 340\,\text{kJ} = 450\,\text{kJ}$. Se on sama kuin alussa.

## Yleinen virhekäsitys
Moni ajattelee, että energia kuluu loppuun, kun vauhti hidastuu tai akku tyhjenee. Energia ei kulu eikä katoa. Se muuttaa muotoa. Suuri osa päätyy lämpönä ympäristöön. Sitä ei enää helposti saa sieltä takaisin hyötykäyttöön.

Toinen virhe on laskea yhteen energioita eri yksiköissä. Esimerkiksi $1{,}5\,\text{MJ} + 300\,\text{kJ} = 301{,}5$ on väärin. Etuliite on kerroin. Muunna energiat siis ensin samaan yksikköön.

## Tiivistelmä
- Energia muuttuu ketjussa muodosta toiseen, esimerkiksi säteily, kemiallinen energia, liike-energia ja lämpöenergia.
- Energia säilyy (luku *Energialajit ja energian säilyminen*). Osa muuttuu joka vaiheessa lämpöenergiaksi, ja lämpöenergia siirtyy lämpönä ympäristöön.
- Energian yksikkö on joule (J). Etuliitteet: $1\,\text{kJ} = 1000\,\text{J}$, $1\,\text{MJ} = 1000\,\text{kJ}$, $1\,\text{GJ} = 1000\,\text{MJ}$ ja $1\,\text{TJ} = 1000\,\text{GJ}$.
- Etuliite korvataan arvollaan: $2{,}5\,\text{kJ} = 2{,}5 \cdot 1000\,\text{J}$. Energioita lasketaan yhteen samassa yksikössä.
- Arjen energiat ovat jouleista terajouleihin. Vertailu tehdään kymmenpotensseina.
