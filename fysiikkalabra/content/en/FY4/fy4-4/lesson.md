# Newton's second law

> **Why** does a fully loaded truck accelerate away from the traffic lights more slowly than an empty one, even though the engine is the same?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: the traffic lights on a country road have just turned green, and two identical trucks have set off from side-by-side lanes. The nearer truck is fully loaded with logs and has only just crossed the stop line. The empty truck farther away is already clearly ahead. Forest and fields are in the background." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy44h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy44h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy44h-road" gradientUnits="userSpaceOnUse" x1="0" y1="352" x2="0" y2="600"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#6b7480"/></linearGradient><linearGradient id="fy44h-e-cab" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy44h-e-glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy44h-l-log0" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#b8622d"/></linearGradient><linearGradient id="fy44h-l-log1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#b8622d"/></linearGradient><linearGradient id="fy44h-l-log2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#b8622d"/></linearGradient><linearGradient id="fy44h-l-cab" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy44h-l-glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy44h-sky)"/>
  <circle cx="1060" cy="92" r="70.5" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="1060" cy="92" r="44" fill="url(#fy44h-sun)"/>
  <path d="M219,108 Q217,77.5 253,81 Q267.5,48.5 303.5,59.5 Q336,41.5 354,75.5 Q386.5,79 383,108 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M706,72 Q705,51.5 729,54 Q738.5,32.5 762.5,39.5 Q784,27.5 796,50.5 Q817.5,53 815,72 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,230 Q100,212 200,227.5 Q300,212.5 400,227.5 Q500,185.5 600,232.5 Q700,198 800,230.5 Q900,189.5 1000,232 Q1100,203.5 1200,229 Q1300,191 1400,231.5 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M0,260.5 Q100,242 200,259.5 Q300,216 400,264 Q500,243.5 600,258.5 Q700,229 800,259 Q900,216 1000,257.5 Q1100,228 1200,257.5 Q1300,223.5 1400,261 V600 H0 Z" fill="#f1dfb5" stroke-linejoin="round"/>
  <path d="M0,292 L11,258.5 L22,292 L34,254.5 L46,292 L57.5,256 L69,292 L86.5,229.5 L104.5,292 L116.5,253 L129,292 L141,253.5 L153.5,292 L170,234.5 L186.5,292 L205.5,224.5 L224.5,292 L241,234.5 L257.5,292 L277,223 L296,292 L314.5,227 L332.5,292 L348,240 L363,292 L382,225 L401,292 L416,240.5 L431.5,292 L444.5,248 L458,292 L474.5,234 L491.5,292 L506.5,239.5 L522,292 L537,242.5 L551.5,292 L562.5,259 L573,292 L592,226 L610.5,292 L629.5,224.5 L648.5,292 L664.5,236.5 L680.5,292 L698,230.5 L715.5,292 L731.5,236.5 L747.5,292 L765,231 L782.5,292 L800.5,229 L818.5,292 L831.5,248.5 L845,292 L857,254 L869,292 L888,224 L907,292 L926.5,222.5 L946,292 L962.5,235.5 L978.5,292 L997.5,224.5 L1016.5,292 L1032,238 L1048,292 L1064.5,234.5 L1081,292 L1097.5,236 L1113.5,292 L1126.5,251.5 L1139,292 L1156.5,230.5 L1174,292 L1192,227 L1210.5,292 V332 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="69.5" y="317.5" width="8.5" height="12.5" fill="#b8622d"/>
  <path d="M36.5,319.5 L73.5,278.5 L110.5,319.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M73.5,278.5 L110.5,319.5 H73.5 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M44.5,297 L73.5,255.5 L102.5,297 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M73.5,255.5 L102.5,297 H73.5 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M53,274 L73.5,226.5 L94,274 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M73.5,226.5 L94,274 H73.5 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="266" y="314.5" width="10.5" height="15.5" fill="#b8622d"/>
  <path d="M224.5,317 L271,265.5 L317.5,317 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M271,265.5 L317.5,317 H271 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M235,288.5 L271,237 L307,288.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M271,237 L307,288.5 H271 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M245,260.5 L271,201 L297,260.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M271,201 L297,260.5 H271 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="451" y="318" width="8" height="12" fill="#b8622d"/>
  <path d="M419.5,320 L455,281 L490,320 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M455,281 L490,320 H455 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M427.5,298.5 L455,259.5 L482.5,298.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M455,259.5 L482.5,298.5 H455 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M435,277 L455,232 L474.5,277 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M455,232 L474.5,277 H455 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="671" y="318" width="8" height="12" fill="#b8622d"/>
  <path d="M639.5,320 L675,280.5 L711,320 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M675,280.5 L711,320 H675 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M647.5,298 L675,258.5 L703,298 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M675,258.5 L703,298 H675 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M655.5,276.5 L675,230.5 L695,276.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M675,230.5 L695,276.5 H675 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="847.5" y="319" width="7.5" height="11" fill="#b8622d"/>
  <path d="M818,321 L851,284.5 L883.5,321 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M851,284.5 L883.5,321 H851 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M825.5,301 L851,264.5 L876.5,301 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M851,264.5 L876.5,301 H851 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M832.5,281 L851,239.5 L869,281 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M851,239.5 L869,281 H851 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1051.5" y="319" width="7.5" height="11" fill="#b8622d"/>
  <path d="M1022,320.5 L1055.5,283.5 L1088.5,320.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1055.5,283.5 L1088.5,320.5 H1055.5 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1029.5,300.5 L1055.5,263 L1081.5,300.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1055.5,263 L1081.5,300.5 H1055.5 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1037,280 L1055.5,237.5 L1074,280 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1055.5,237.5 L1074,280 H1055.5 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="880" y="230" width="150" height="70" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="894" y1="233" x2="894" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="908" y1="233" x2="908" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="922" y1="233" x2="922" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="936" y1="233" x2="936" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="950" y1="233" x2="950" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="964" y1="233" x2="964" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="978" y1="233" x2="978" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="992" y1="233" x2="992" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1006" y1="233" x2="1006" y2="297" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="880" y="230" width="10" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1020" y="230" width="10" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M860,230 L955,191.5 L1050,230 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="910" y="249.5" width="40" height="28" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="910" y="249.5" width="40" height="28" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="930" y1="249.5" x2="930" y2="277.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="1075.5" y="186" width="9" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1075.5" y="318" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1080" y="300" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1075.5" y="282" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1080" y="264" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1075.5" y="246" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1080" y="228" width="4.5" height="2" fill="#1f2933"/>
  <rect x="1075.5" y="210" width="4.5" height="2" fill="#1f2933"/>
  <line x1="1080" y1="243" x2="1053" y2="225" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1080" y1="223.5" x2="1107" y2="205.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1080" y1="208.5" x2="1053" y2="190.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1080" cy="193.5" r="30" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1057.5" cy="216" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1102.5" cy="213" r="25.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1080" cy="228" r="22.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="326.5" y="216" width="7" height="120" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="326.5" y="321.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="330" y="307" width="3.5" height="2" fill="#1f2933"/>
  <rect x="326.5" y="293" width="3.5" height="2" fill="#1f2933"/>
  <rect x="330" y="278.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="326.5" y="264" width="3.5" height="2" fill="#1f2933"/>
  <rect x="330" y="249.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="326.5" y="235" width="3.5" height="2" fill="#1f2933"/>
  <line x1="330" y1="261.5" x2="308.5" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="330" y1="246" x2="351.5" y2="231.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="330" y1="234" x2="308.5" y2="219.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="330" cy="222" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="312" cy="240" r="19" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="348" cy="237.5" r="20.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="330" cy="249.5" r="18" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="0" y="326" width="1200" height="30" fill="#b2f2bb"/>
  <rect x="10" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="60" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="110" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="160" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="210" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="260" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="310" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="360" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="410" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="460" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="510" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="560" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="610" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="660" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="710" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="760" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="810" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="860" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="910" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="960" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="1010" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="1060" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="1110" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="1160" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="1210" y="322" width="6" height="26" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="0" y="326" width="1200" height="8" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <rect x="0" y="352" width="1200" height="248" fill="url(#fy44h-road)"/>
  <rect x="0" y="348" width="1200" height="8" fill="#c4ccd4"/>
  <rect x="0" y="588" width="1200" height="12" fill="#c4ccd4"/>
  <rect x="40" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="190" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="340" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="490" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="640" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="790" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="940" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="1090" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="1240" y="466" width="80" height="8" rx="2" fill="#ffffff"/>
  <rect x="212" y="360" width="14" height="226" fill="#ffffff"/>
  <rect x="150" y="160" width="12" height="200" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="128" y="100" width="56" height="136" rx="10" fill="#1f2933"/>
  <circle cx="156" cy="124" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="156" cy="166" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="156" cy="208" r="15" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="156" cy="208" r="26" fill="#b2f2bb" fill-opacity="0.45"/>
  <g transform="translate(1150,452) scale(0.8) translate(-1150,-452)">
  <rect x="640" y="378" width="500" height="16" rx="3" fill="#1f2933"/>
  <rect x="680" y="356" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="682" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="700" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="785" y="356" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="787" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="805" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="890" y="356" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="892" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="910" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="995" y="356" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="997" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="1015" y="242" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <path d="M1030,394 V262 Q1030,246 1046,246 H1120 Q1140,246 1144,272 L1150,332 V394 Z" fill="url(#fy44h-e-cab)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1080,256 H1120 Q1134,256 1137,274 L1142,312 H1080 Z" fill="url(#fy44h-e-glass)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="1040" y="256" width="30" height="56" rx="3" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="1076" y1="256" x2="1076" y2="390" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="1084" y="324" width="18" height="6" rx="3" fill="#1f2933"/>
  <rect x="1142" y="368" width="16" height="26" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1148" cy="352" r="7" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="1016" y="222" width="10" height="120" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="720" cy="420" r="32" fill="#1f2933"/>
  <circle cx="720" cy="420" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="728" cy="420" r="2" fill="#8a96a3"/>
  <circle cx="722.5" cy="427.5" r="2" fill="#8a96a3"/>
  <circle cx="713.5" cy="424.5" r="2" fill="#8a96a3"/>
  <circle cx="713.5" cy="415.5" r="2" fill="#8a96a3"/>
  <circle cx="722.5" cy="412.5" r="2" fill="#8a96a3"/>
  <circle cx="800" cy="420" r="32" fill="#1f2933"/>
  <circle cx="800" cy="420" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="808" cy="420" r="2" fill="#8a96a3"/>
  <circle cx="802.5" cy="427.5" r="2" fill="#8a96a3"/>
  <circle cx="793.5" cy="424.5" r="2" fill="#8a96a3"/>
  <circle cx="793.5" cy="415.5" r="2" fill="#8a96a3"/>
  <circle cx="802.5" cy="412.5" r="2" fill="#8a96a3"/>
  <circle cx="980" cy="420" r="32" fill="#1f2933"/>
  <circle cx="980" cy="420" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="988" cy="420" r="2" fill="#8a96a3"/>
  <circle cx="982.5" cy="427.5" r="2" fill="#8a96a3"/>
  <circle cx="973.5" cy="424.5" r="2" fill="#8a96a3"/>
  <circle cx="973.5" cy="415.5" r="2" fill="#8a96a3"/>
  <circle cx="982.5" cy="412.5" r="2" fill="#8a96a3"/>
  <circle cx="1080" cy="420" r="32" fill="#1f2933"/>
  <circle cx="1080" cy="420" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="1088" cy="420" r="2" fill="#8a96a3"/>
  <circle cx="1082.5" cy="427.5" r="2" fill="#8a96a3"/>
  <circle cx="1073.5" cy="424.5" r="2" fill="#8a96a3"/>
  <circle cx="1073.5" cy="415.5" r="2" fill="#8a96a3"/>
  <circle cx="1082.5" cy="412.5" r="2" fill="#8a96a3"/>
  </g>
  <rect x="190" y="502" width="500" height="16" rx="3" fill="#1f2933"/>
  <rect x="230" y="480" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="232" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="250" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="335" y="480" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="337" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="355" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="440" y="480" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="442" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="460" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="545" y="480" width="30" height="22" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="547" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="565" y="366" width="8" height="116" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="208" y="450" width="364" height="30" rx="13" fill="url(#fy44h-l-log0)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M238,462 H532" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.7"/>
  <path d="M268,472 H482" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <circle cx="218" cy="465" r="15" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="218" cy="465" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <circle cx="227" cy="465" r="14.5" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="227" cy="465" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <circle cx="236" cy="465" r="14" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="236" cy="465" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <rect x="204" y="420" width="374" height="30" rx="13" fill="url(#fy44h-l-log1)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M234,432 H538" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.7"/>
  <path d="M264,442 H488" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <circle cx="214" cy="435" r="15" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="214" cy="435" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <circle cx="223" cy="435" r="14.5" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="223" cy="435" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <circle cx="232" cy="435" r="14" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="232" cy="435" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <rect x="200" y="390" width="384" height="30" rx="13" fill="url(#fy44h-l-log2)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M230,402 H544" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.7"/>
  <path d="M260,412 H494" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <circle cx="210" cy="405" r="15" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="210" cy="405" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <circle cx="219" cy="405" r="14.5" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="219" cy="405" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <circle cx="228" cy="405" r="14" fill="#f1dfb5" stroke="#a97a35" stroke-width="2"/>
  <circle cx="228" cy="405" r="8" fill="none" stroke="#a97a35" stroke-width="1.5"/>
  <path d="M210,392 Q400,380 580,394" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M580,518 V386 Q580,370 596,370 H670 Q690,370 694,396 L700,456 V518 Z" fill="url(#fy44h-l-cab)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M630,380 H670 Q684,380 687,398 L692,436 H630 Z" fill="url(#fy44h-l-glass)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="590" y="380" width="30" height="56" rx="3" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="626" y1="380" x2="626" y2="514" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="634" y="448" width="18" height="6" rx="3" fill="#1f2933"/>
  <rect x="692" y="492" width="16" height="26" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="698" cy="476" r="7" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="566" y="346" width="10" height="120" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="270" cy="544" r="32" fill="#1f2933"/>
  <circle cx="270" cy="544" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="278" cy="544" r="2" fill="#8a96a3"/>
  <circle cx="272.5" cy="551.5" r="2" fill="#8a96a3"/>
  <circle cx="263.5" cy="548.5" r="2" fill="#8a96a3"/>
  <circle cx="263.5" cy="539.5" r="2" fill="#8a96a3"/>
  <circle cx="272.5" cy="536.5" r="2" fill="#8a96a3"/>
  <circle cx="350" cy="544" r="32" fill="#1f2933"/>
  <circle cx="350" cy="544" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="358" cy="544" r="2" fill="#8a96a3"/>
  <circle cx="352.5" cy="551.5" r="2" fill="#8a96a3"/>
  <circle cx="343.5" cy="548.5" r="2" fill="#8a96a3"/>
  <circle cx="343.5" cy="539.5" r="2" fill="#8a96a3"/>
  <circle cx="352.5" cy="536.5" r="2" fill="#8a96a3"/>
  <circle cx="530" cy="544" r="32" fill="#1f2933"/>
  <circle cx="530" cy="544" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="538" cy="544" r="2" fill="#8a96a3"/>
  <circle cx="532.5" cy="551.5" r="2" fill="#8a96a3"/>
  <circle cx="523.5" cy="548.5" r="2" fill="#8a96a3"/>
  <circle cx="523.5" cy="539.5" r="2" fill="#8a96a3"/>
  <circle cx="532.5" cy="536.5" r="2" fill="#8a96a3"/>
  <circle cx="630" cy="544" r="32" fill="#1f2933"/>
  <circle cx="630" cy="544" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="638" cy="544" r="2" fill="#8a96a3"/>
  <circle cx="632.5" cy="551.5" r="2" fill="#8a96a3"/>
  <circle cx="623.5" cy="548.5" r="2" fill="#8a96a3"/>
  <circle cx="623.5" cy="539.5" r="2" fill="#8a96a3"/>
  <circle cx="632.5" cy="536.5" r="2" fill="#8a96a3"/>
  <circle cx="1029" cy="254" r="10" fill="#6b7480" fill-opacity="0.45"/>
  <circle cx="1007" cy="238" r="16" fill="#6b7480" fill-opacity="0.33"/>
  <circle cx="985" cy="222" r="22" fill="#6b7480" fill-opacity="0.21"/>
  <circle cx="553" cy="332" r="12" fill="#6b7480" fill-opacity="0.45"/>
  <circle cx="531" cy="316" r="19" fill="#6b7480" fill-opacity="0.33"/>
  <circle cx="509" cy="300" r="26.5" fill="#6b7480" fill-opacity="0.21"/>
  <line x1="712" y1="404" x2="742" y2="404" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="130" y1="500" x2="174" y2="500" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="704" y1="420" x2="734" y2="420" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="120" y1="524" x2="164" y2="524" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="696" y1="436" x2="726" y2="436" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="110" y1="548" x2="154" y2="548" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
</svg>

## Key idea

### The net force changes the velocity
In the chapter *Interaction and force: Newton's first and third laws* you learned that an object's velocity stays unchanged when the forces acting on it cancel each other. The object is then at rest or moves in a straight line at constant velocity. When the forces do not cancel, the velocity changes: the object speeds up, slows down or turns. What matters is not any single force but the combined effect of all the forces acting on the object, the **net force** $\Sigma\overline{F}$. It is the vector sum of the forces, not just one force added to another.

On the left of the figure a box rests on the floor. The weight $\overline{G}$ and the normal force $\overline{N}$ from the floor are equal and opposite, so the net force is zero. On the right the box is pulled by a rope. The vertical forces still cancel, but horizontally the tension $\overline{T}$ in the rope is greater than the friction force $\overline{F}_\mu$ from the floor. The net force points to the right, and the box accelerates to the right.

<svg data-fig="kokonaisvoima" viewBox="0 0 600 420" role="img" aria-label="Two situations. On the left a box rests on the floor. In its free-body diagram the box is a rectangle: the weight G points down from the centre and the normal force N from the floor points up from the bottom surface, equally long. On the right the same box is pulled horizontally to the right by a rope, and in the situation picture an orange acceleration arrow points to the right above the box. Its free-body diagram has the weight and the normal force equally long, the tension T of the rope to the right, and the friction force from the floor to the left from the back corner of the bottom surface, one third of the length of the tension. Separately there is a green hollow arrow, the net force, to the right: the difference between the tension and the friction. The arrows are to scale." style="max-width:100%;font-size:24px">
  <line x1="300" y1="10" x2="300" y2="410" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="20" y1="140" x2="580" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <foreignObject x="108.5" y="5.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{at rest}$</div></foreignObject>
  <line x1="50" y1="112" x2="250" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="50" y1="112" x2="40" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="66" y1="112" x2="56" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="82" y1="112" x2="72" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="98" y1="112" x2="88" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="114" y1="112" x2="104" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="112" x2="120" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="146" y1="112" x2="136" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="162" y1="112" x2="152" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="178" y1="112" x2="168" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="194" y1="112" x2="184" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="112" x2="200" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="226" y1="112" x2="216" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="242" y1="112" x2="232" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="115" y="64" width="70" height="48" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="121" y1="88" x2="179" y2="88" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="115" y="246" width="70" height="48" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="270" x2="150" y2="327.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,344.5 L142,326.5 L158,326.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="153.5" y="326" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="167" y1="294" x2="167" y2="236.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M167,219.5 L175,237.5 L159,237.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="170.5" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="377.5" y="5.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{being pulled}$</div></foreignObject>
  <line x1="330" y1="112" x2="580" y2="112" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="330" y1="112" x2="320" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346" y1="112" x2="336" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="362" y1="112" x2="352" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="378" y1="112" x2="368" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="394" y1="112" x2="384" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="112" x2="400" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="426" y1="112" x2="416" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="442" y1="112" x2="432" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="458" y1="112" x2="448" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="474" y1="112" x2="464" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="490" y1="112" x2="480" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="506" y1="112" x2="496" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="522" y1="112" x2="512" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="538" y1="112" x2="528" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="554" y1="112" x2="544" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="570" y1="112" x2="560" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="375" y="64" width="70" height="48" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="381" y1="88" x2="439" y2="88" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="445" y1="88" x2="520" y2="88" stroke="#a97a35" stroke-width="3" stroke-linecap="round"/>
  <circle cx="524" cy="88" r="8" fill="#6b7480"/>
  <rect x="385" y="246" width="70" height="48" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="420" y1="270" x2="420" y2="327.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M420,344.5 L412,326.5 L428,326.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="423.5" y="326" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="437" y1="294" x2="437" y2="236.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M437,219.5 L445,237.5 L429,237.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="440.5" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="455" y1="270" x2="495" y2="270" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M512,270 L494,278 L494,262 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="517.5" y="253.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="385" y1="294" x2="383" y2="294" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M366,294 L384,286 L384,302 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="333.5" y="301.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="378" y1="52" x2="430" y2="52" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M419,58.5 L432,52 L419,45.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="437.5" y="33.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M470,365 L486,365 L486,373 L508,360 L486,347 L486,355 L470,355 Z" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="513.5" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
</svg>

### Mass resists a change in velocity
Measurements with a cart reveal two regularities. When the net force doubles, the acceleration doubles: the acceleration is directly proportional to the net force. When the same net force acts on a cart with twice the mass, the acceleration is halved. Mass therefore tells us about the inertia of an object, that is, how hard it is to change its velocity. In the graph each mass gives a straight line through the origin, and the line of the heavier cart is half as steep.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Graph to scale: the horizontal axis shows the net force in newtons from 0 to 3, and the vertical axis shows the acceleration from 0 to 6 metres per second squared. Two straight lines through the origin, each with three points. For a mass of 0.50 kilograms the points are 1 N and 2, 2 N and 4, and 3 N and 6. For a mass of 1.0 kilogram the points are 1 N and 1, 2 N and 2, and 3 N and 3. Dashed lines show that at a net force of 2 N the acceleration of the lighter cart is 4 and that of the heavier cart is 2." style="max-width:100%;font-size:24px">
  <line x1="138.5" y1="300" x2="138.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186.5" y1="300" x2="186.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="235" y1="300" x2="235" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283.5" y1="300" x2="283.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="300" x2="331.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="380" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="261.5" x2="380" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="223.5" x2="380" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="185" x2="380" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="146.5" x2="380" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="108.5" x2="380" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="70" x2="380" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="300" x2="394" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M406,300 L393,306 L393,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,44 L96,57 L84,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="138.5" y1="300" x2="138.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186.5" y1="300" x2="186.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="235" y1="300" x2="235" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283.5" y1="300" x2="283.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="273.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="331.5" y1="300" x2="331.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="380" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="370" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="83" y1="261.5" x2="90" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="247" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="83" y1="223.5" x2="90" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="209" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="185" x2="90" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="83" y1="146.5" x2="90" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="132" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="108.5" x2="90" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="94" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="83" y1="70" x2="90" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="412" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Sigma F\ (\text{N})$</div></foreignObject>
  <foreignObject x="80" y="13.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a\ (\text{m/s}^2)$</div></foreignObject>
  <line x1="283.5" y1="146.5" x2="283.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="146.5" x2="283.5" y2="146.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="283.5" y1="223.5" x2="283.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="223.5" x2="283.5" y2="223.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="90,300 380,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,300 380,185" fill="none" stroke="#b8622d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="186.5" cy="223.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186.5" cy="261.5" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283.5" cy="146.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283.5" cy="223.5" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <circle cx="380" cy="70" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="380" cy="185" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="394" y="55.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 0.50\,\text{kg}$</div></foreignObject>
  <foreignObject x="394" y="170.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d">$m = 1.0\,\text{kg}$</div></foreignObject>
</svg>

This gives the answer to the opening question. The engine turns the driving wheels, and the road pushes the tyres forward. When this force is equally large for the loaded and the empty truck, the much greater mass of the loaded truck makes its acceleration small. The weight of the load does not pull the truck backward as such, because the normal force from the road cancels it. The heavy load does increase the rolling resistance of the tyres, but the main reason for the slow acceleration is the large mass.

## Formula: Newton's second law
Newton's second law, also called the fundamental law of dynamics, gathers the observations into one equation:
```latex
\Sigma\overline{F} = m\overline{a}
```
where $\Sigma\overline{F}$ is the vector sum of the forces acting on the object, the net force ($\text{N}$), $m$ is the mass of the object ($\text{kg}$) and $\overline{a}$ is its acceleration ($\text{m/s}^2$). The unit of force is defined by this law: one newton is the force that gives a mass of one kilogram an acceleration of $1\,\text{m/s}^2$. So $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.

### The net force points in the direction of the acceleration
The law is a vector equation: the net force and the acceleration always point in the same direction. The direction of the velocity can be another one. In the figure a crane holds a crate on a rope. When the crate rises while speeding up, the force of the rope is greater than the weight and the net force points up. When the crate rises while slowing down, the force of the rope is smaller than the weight: the net force and the acceleration point down, even though the crate still moves upward. At rest and when rising at constant velocity, the force of the rope and the weight are equal.

<svg data-fig="nosturi" viewBox="0 0 600 620" role="img" aria-label="Four situations in which the rope of a crane holds a crate. Each has the situation picture on the left and the free-body diagram of the crate on the right, where the crate is a rectangle: the weight G points down from the centre and the tension T of the rope points up from the top surface. Next to the free-body diagram there is a blue velocity arrow and an orange acceleration arrow when they are not zero. At the top left the crate is at rest, v and a are zero and the arrows T and G are equally long. At the top right the crate rises at constant velocity: the velocity is up, a is zero and the arrows are equally long. At the bottom left the crate rises while speeding up: the velocity and the acceleration are up, and T is longer than G. At the bottom right the crate rises while slowing down: the velocity is up but the acceleration is down, and T is shorter than G." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy44-crate00" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy44-crate3000" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy44-crate0310" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy44-crate300310" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="300" y1="10" x2="300" y2="610" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="10" y1="310" x2="590" y2="310" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="108.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{at rest}$</div></foreignObject>
  <line x1="62" y1="44" x2="62" y2="118" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M62,118 q-12,4 -10,16 q4,10 14,6" fill="none" stroke="#6c757d" stroke-width="4" stroke-linejoin="round"/>
  <line x1="56" y1="138" x2="36" y2="160" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="68" y1="138" x2="88" y2="160" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="28" y="160" width="68" height="52" rx="2" fill="url(#fy44-crate00)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="28" y1="177" x2="96" y2="177" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="28" y1="194" x2="96" y2="194" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="48" x2="120" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="152" y="166" width="56" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="180" y1="186" x2="180" y2="249" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,266 L172,248 L188,248 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="185.5" y="249.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="180" y1="166" x2="180" y2="103" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,86 L188,104 L172,104 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="185.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="224" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$v = 0$</div></foreignObject>
  <foreignObject x="224" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="296" y="7.5" width="308" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising at constant velocity}$</div></foreignObject>
  <line x1="362" y1="44" x2="362" y2="118" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M362,118 q-12,4 -10,16 q4,10 14,6" fill="none" stroke="#6c757d" stroke-width="4" stroke-linejoin="round"/>
  <line x1="356" y1="138" x2="336" y2="160" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="368" y1="138" x2="388" y2="160" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="328" y="160" width="68" height="52" rx="2" fill="url(#fy44-crate3000)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="328" y1="177" x2="396" y2="177" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="328" y1="194" x2="396" y2="194" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="48" x2="420" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="452" y="166" width="56" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="480" y1="186" x2="480" y2="249" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M480,266 L472,248 L488,248 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="485.5" y="249.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="480" y1="166" x2="480" y2="103" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M480,86 L488,104 L472,104 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="485.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="536" y1="206" x2="536" y2="148" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M542.5,159 L536,146 L529.5,159" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="519.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="524" y="229.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="27.5" y="317.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising and speeding up}$</div></foreignObject>
  <line x1="62" y1="354" x2="62" y2="428" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M62,428 q-12,4 -10,16 q4,10 14,6" fill="none" stroke="#6c757d" stroke-width="4" stroke-linejoin="round"/>
  <line x1="56" y1="448" x2="36" y2="470" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="68" y1="448" x2="88" y2="470" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="28" y="470" width="68" height="52" rx="2" fill="url(#fy44-crate0310)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="28" y1="487" x2="96" y2="487" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="28" y1="504" x2="96" y2="504" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="358" x2="120" y2="596" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="152" y="476" width="56" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="180" y1="496" x2="180" y2="559" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,576 L172,558 L188,558 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="185.5" y="559.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="180" y1="476" x2="180" y2="389" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,372 L188,390 L172,390 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="185.5" y="369.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="236" y1="516" x2="236" y2="458" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M242.5,469 L236,456 L229.5,469" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="219.5" y="415.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="272" y1="516" x2="272" y2="474" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M278.5,485 L272,472 L265.5,485" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="255.5" y="431.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="321" y="317.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rising and slowing down}$</div></foreignObject>
  <line x1="362" y1="354" x2="362" y2="428" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M362,428 q-12,4 -10,16 q4,10 14,6" fill="none" stroke="#6c757d" stroke-width="4" stroke-linejoin="round"/>
  <line x1="356" y1="448" x2="336" y2="470" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="368" y1="448" x2="388" y2="470" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="328" y="470" width="68" height="52" rx="2" fill="url(#fy44-crate300310)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="328" y1="487" x2="396" y2="487" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="328" y1="504" x2="396" y2="504" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="358" x2="420" y2="596" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="452" y="476" width="56" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="480" y1="496" x2="480" y2="559" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M480,576 L472,558 L488,558 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="485.5" y="559.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="480" y1="476" x2="480" y2="437" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M480,420 L488,438 L472,438 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="485.5" y="417.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="536" y1="516" x2="536" y2="458" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M542.5,469 L536,456 L529.5,469" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="519.5" y="415.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="572" y1="456" x2="572" y2="504" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M565.5,493 L572,506 L578.5,493" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="555.5" y="509.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

### First the forces, then the equation
When the law is used in a calculation, the steps are always taken in the same order. Choose the object and draw its free-body diagram, in which every force has a cause: the Earth, a rope, a surface or a puller. Choose a positive direction, usually the direction of the acceleration. Only then write the net force from the forces, with signs, and set it equal to $ma$. For the crate of the crane, when up is positive, we get $T - G = ma$. In the chapter *Free-body diagrams and the combined effect of forces* the same method extends to slanted forces.

## Worked example
A construction crane lifts a concrete slab of mass $480\,\text{kg}$. The tension in the rope is $5.20\,\text{kN}$. What is the acceleration of the slab, and in which direction does it point? Air resistance is ignored.

<!-- vaihe -->

**Given and find.** $m = 480\,\text{kg}$, $T = 5.20\,\text{kN}$ and $g = 9.81\,\text{m/s}^2$. We want the acceleration $a$ and its direction.

<!-- vaihe -->

**Principle.** Choose the concrete slab as the object. The Earth (weight) and the rope (tension) act on it. By Newton's second law, the acceleration is determined by the sum of these forces. The force of the rope alone does not accelerate the slab, because most of it is used to hold up the weight.

<!-- vaihe -->

**Free-body diagram.** The slab is drawn as a rectangle. The weight $\overline{G}$ starts from the centre and points down, and the tension $\overline{T}$ starts from the top surface and points up. The positive direction is chosen to be up.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Free-body diagram of the concrete slab, the slab as a rectangle. The tension T of the rope starts from the top surface and points up, and the weight G starts from the centre and points down. The arrow T is a little longer than the arrow G. Separately on the right there is an orange acceleration arrow pointing up. On the right there is also a small arrow y pointing up: the positive direction is up. On the left is the situation picture: the hook of a crane lifts the concrete slab on a rope." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy44-ex-elem" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="110" y1="20" x2="110" y2="138" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M110,138 q-14,5 -12,19 q5,12 17,7" fill="none" stroke="#6c757d" stroke-width="5" stroke-linejoin="round"/>
  <line x1="104" y1="168" x2="66" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="168" x2="154" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="46" y="200" width="128" height="60" rx="2" fill="url(#fy44-ex-elem)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="46" y1="220" x2="174" y2="220" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="46" y1="240" x2="174" y2="240" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="8" y1="296" x2="212" y2="296" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="6" y="335.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{situation picture}$</div></foreignObject>
  <foreignObject x="296" y="335.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{free-body diagram}$</div></foreignObject>
  <line x1="228" y1="20" x2="228" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="285" y="165" width="110" height="50" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="340" y1="165" x2="340" y2="47" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M340,30 L348,48 L332,48 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="27.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="340" y1="190" x2="340" y2="295.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M340,312.5 L332,294.5 L348,294.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="292" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="470" y1="220" x2="470" y2="162" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476.5,173 L470,160 L463.5,173" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="453.5" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="560" y1="300" x2="560" y2="245" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M560,236 L564.5,246 L555.5,246 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="550" y="203.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Rearranged formula.** From the diagram we write the net force $T - mg$ and solve for the acceleration:
```latex
\begin{aligned}
&T - mg = ma \\
&a = \frac{T - mg}{m}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The tension is converted to newtons: $5.20\,\text{kN} = 5.20\cdot 1000\,\text{N} = 5200\,\text{N}$.

<!-- vaihe -->

**Substitution.** First we calculate the weight and then the acceleration:
```latex
\begin{aligned}
&a = \frac{T - mg}{m} \\
&mg = 480\,\text{kg}\cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \\
&\phantom{mg} = 4708.8\,\text{N} \\
&a = \frac{5200\,\text{N} - 4708.8\,\text{N}}{480\,\text{kg}} \\
&\phantom{a} \approx 1.02\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Result.** The acceleration is $a \approx 1.02\,\text{m/s}^2$ upward. It has three significant figures, like the tension $5.20\,\text{kN}$ and the mass $480\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** The force of the rope is only about ten percent greater than the weight $4.71\,\text{kN}$, so the acceleration should also be about a tenth of the free-fall acceleration: $0.1\cdot 9.81\,\text{m/s}^2 \approx 1\,\text{m/s}^2$. If the weight were forgotten, the result would be $5200\,\text{N} : 480\,\text{kg} \approx 10.8\,\text{m/s}^2$. That is more than the free-fall acceleration and far too large for a crane.

## Common misconception
Many people think that a force always acts in the direction of motion and that the net force points in the direction of motion. The net force, however, points in the direction of the acceleration. When air resistance is ignored, a ball thrown upward keeps rising even though only its weight, which points down, acts on it, and that is why it slows down. In a slowing motion the net force points against the velocity. A second mistake is to think that a constant force keeps up a constant velocity. When the net force is constant and not zero, the velocity changes steadily. A third mistake is to confuse mass and weight. On a horizontal track the weight does not resist the motion, because the normal force cancels it: it is the mass that makes the acceleration smaller.

## Summary
- When the net force is zero, the velocity does not change. When it is not zero, the object accelerates in the direction of the net force.
- Newton's second law is $\Sigma\overline{F} = m\overline{a}$. The acceleration is directly proportional to the net force and inversely proportional to the mass.
- The net force points in the direction of the acceleration, which is not always the direction of the velocity: in a slowing motion it points against the velocity.
- First the free-body diagram is drawn and a positive direction is chosen, then $\Sigma F = ma$ is written with signs.
- The unit of force is $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.
