# Gravitaation alainen ympyräliike

> **Miksi** Kansainvälinen avaruusasema ISS ei putoa Maahan, ja miksi astronautit leijuvat sen sisällä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: avaruusasema kiertää Maata. Alhaalla näkyy Maan kaareutuva pinta, jossa on merta, maata ja pilviä, ja ohut ilmakehä. Asemalla on pitkä ristikkorunko, suuret aurinkopaneelit ja asuinmoduulit. Moduulin ikkunassa näkyy astronautti leijumassa." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy56h-ocean" cx="0.4" cy="0.1" r="0.9"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></radialGradient><linearGradient id="fy56h-panel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1971c2"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#1f2933"/>
  <circle cx="1170" cy="132" r="1.36652" fill="#ffffff"/>
  <circle cx="979" cy="0" r="2.19219" fill="#ffffff"/>
  <circle cx="43" cy="599.5" r="1.21642" fill="#ffffff"/>
  <circle cx="27" cy="437.5" r="1.16567" fill="#ffffff"/>
  <circle cx="987" cy="137" r="1.57655" fill="#ffffff"/>
  <circle cx="103" cy="213.5" r="1.45149" fill="#ffffff"/>
  <circle cx="311.5" cy="253" r="2.13864" fill="#ffffff"/>
  <circle cx="171.5" cy="347.5" r="2.33082" fill="#ffffff"/>
  <circle cx="803.5" cy="489" r="1.48391" fill="#ffffff"/>
  <circle cx="500.5" cy="524.5" r="2.12911" fill="#ffffff"/>
  <circle cx="887" cy="338" r="2.44032" fill="#ffffff"/>
  <circle cx="1013" cy="353.5" r="2.01357" fill="#ffffff"/>
  <circle cx="837.5" cy="487" r="1.44702" fill="#ffffff"/>
  <circle cx="1054.5" cy="119" r="1.57908" fill="#ffffff"/>
  <circle cx="590" cy="245.5" r="1.35048" fill="#ffffff"/>
  <circle cx="1002.5" cy="243" r="1.34652" fill="#ffffff"/>
  <circle cx="382.5" cy="470" r="2.46813" fill="#ffffff"/>
  <circle cx="1064" cy="285.5" r="1.01848" fill="#ffffff"/>
  <circle cx="817" cy="305" r="1.19434" fill="#ffffff"/>
  <circle cx="1128.5" cy="358.5" r="2.1448" fill="#ffffff"/>
  <circle cx="699" cy="310.5" r="2.21278" fill="#ffffff"/>
  <circle cx="1068" cy="288" r="1.87032" fill="#ffffff"/>
  <circle cx="248.5" cy="312" r="1.93293" fill="#ffffff"/>
  <circle cx="241.5" cy="5" r="2.14185" fill="#ffffff"/>
  <circle cx="745" cy="503" r="1.97347" fill="#ffffff"/>
  <circle cx="87" cy="4.5" r="2.16344" fill="#ffffff"/>
  <circle cx="1082" cy="119" r="1.02046" fill="#ffffff"/>
  <circle cx="968" cy="224" r="1.85541" fill="#ffffff"/>
  <circle cx="1011" cy="450" r="2.49263" fill="#ffffff"/>
  <circle cx="300" cy="396.5" r="1.05591" fill="#ffffff"/>
  <circle cx="411" cy="3" r="1.57702" fill="#ffffff"/>
  <circle cx="748" cy="554" r="1.93231" fill="#ffffff"/>
  <circle cx="695" cy="362" r="1.93327" fill="#ffffff"/>
  <circle cx="550.5" cy="312" r="1.05066" fill="#ffffff"/>
  <circle cx="150.5" cy="536.5" r="1.73401" fill="#ffffff"/>
  <circle cx="306.5" cy="277" r="1.79191" fill="#ffffff"/>
  <circle cx="1153.5" cy="109.5" r="2.35188" fill="#ffffff"/>
  <circle cx="1178" cy="105" r="1.68043" fill="#ffffff"/>
  <circle cx="175.5" cy="116" r="1.98917" fill="#ffffff"/>
  <circle cx="1081" cy="284" r="2.42495" fill="#ffffff"/>
  <circle cx="333.5" cy="166" r="1.72597" fill="#ffffff"/>
  <circle cx="309" cy="324" r="1.87081" fill="#ffffff"/>
  <circle cx="927" cy="177.5" r="1.48987" fill="#ffffff"/>
  <circle cx="291" cy="438" r="2.26872" fill="#ffffff"/>
  <circle cx="1184" cy="182.5" r="2.43052" fill="#ffffff"/>
  <circle cx="981" cy="92" r="1.80133" fill="#ffffff"/>
  <circle cx="254" cy="163.5" r="2.19842" fill="#ffffff"/>
  <circle cx="454" cy="305.5" r="2.16858" fill="#ffffff"/>
  <circle cx="1136.5" cy="508" r="1.21393" fill="#ffffff"/>
  <circle cx="581" cy="225.5" r="1.21905" fill="#ffffff"/>
  <circle cx="219.5" cy="415" r="2.24394" fill="#ffffff"/>
  <circle cx="967.5" cy="219" r="1.09038" fill="#ffffff"/>
  <circle cx="911.5" cy="482.5" r="1.65531" fill="#ffffff"/>
  <circle cx="708" cy="568.5" r="1.12914" fill="#ffffff"/>
  <circle cx="1131" cy="28.5" r="2.18118" fill="#ffffff"/>
  <circle cx="553" cy="453" r="2.32381" fill="#ffffff"/>
  <circle cx="571.5" cy="99" r="2.40409" fill="#ffffff"/>
  <circle cx="266.5" cy="369" r="2.55851" fill="#ffffff"/>
  <circle cx="432.5" cy="2" r="1.07231" fill="#ffffff"/>
  <circle cx="776" cy="211.5" r="1.96703" fill="#ffffff"/>
  <circle cx="769.5" cy="250.5" r="1.19852" fill="#ffffff"/>
  <circle cx="788" cy="442" r="2.16823" fill="#ffffff"/>
  <circle cx="998.5" cy="586" r="1.38631" fill="#ffffff"/>
  <circle cx="403" cy="536" r="1.40945" fill="#ffffff"/>
  <circle cx="138" cy="244.5" r="1.84584" fill="#ffffff"/>
  <circle cx="988.5" cy="457.5" r="2.53708" fill="#ffffff"/>
  <circle cx="553" cy="16.5" r="2.11072" fill="#ffffff"/>
  <circle cx="885" cy="52" r="2.32392" fill="#ffffff"/>
  <circle cx="673.5" cy="379" r="2.13066" fill="#ffffff"/>
  <circle cx="298.5" cy="7.5" r="1.41634" fill="#ffffff"/>
  <circle cx="326.5" cy="225.5" r="2.46219" fill="#ffffff"/>
  <circle cx="359" cy="267" r="1.51185" fill="#ffffff"/>
  <circle cx="673" cy="184.5" r="2.27848" fill="#ffffff"/>
  <circle cx="1077" cy="202.5" r="2.18549" fill="#ffffff"/>
  <circle cx="404.5" cy="312" r="2.31536" fill="#ffffff"/>
  <circle cx="297.5" cy="446" r="1.50525" fill="#ffffff"/>
  <circle cx="771.5" cy="122.5" r="1.13232" fill="#ffffff"/>
  <circle cx="975.5" cy="232" r="2.19979" fill="#ffffff"/>
  <circle cx="573" cy="207" r="2.12037" fill="#ffffff"/>
  <circle cx="202" cy="267" r="1.97334" fill="#ffffff"/>
  <circle cx="91.5" cy="173" r="1.73512" fill="#ffffff"/>
  <circle cx="848" cy="219.5" r="1.58169" fill="#ffffff"/>
  <circle cx="38.5" cy="107.5" r="1.40192" fill="#ffffff"/>
  <circle cx="26.5" cy="271.5" r="2.12061" fill="#ffffff"/>
  <circle cx="123.5" cy="36.5" r="1.88472" fill="#ffffff"/>
  <circle cx="1024" cy="402.5" r="1.25203" fill="#ffffff"/>
  <circle cx="698.5" cy="359.5" r="2.40999" fill="#ffffff"/>
  <circle cx="1093" cy="181" r="2.51129" fill="#ffffff"/>
  <circle cx="1109.5" cy="227.5" r="2.39965" fill="#ffffff"/>
  <circle cx="358" cy="106.5" r="1.03307" fill="#ffffff"/>
  <circle cx="600" cy="1580" r="1150" fill="#a5d8ff" fill-opacity="0.35"/>
  <circle cx="600" cy="1580" r="1110" fill="url(#fy56h-ocean)"/>
  <ellipse cx="260" cy="520" rx="170" ry="50" fill="#e9c98a"/>
  <ellipse cx="720" cy="486" rx="220" ry="44" fill="#e9c98a"/>
  <ellipse cx="1040" cy="560" rx="130" ry="40" fill="#e9c98a"/>
  <path d="M140,480 q40,-14 80,0 t80,0" fill="none" stroke="#ffffff" stroke-width="12" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <path d="M470,455 q50,-14 100,0 t100,0" fill="none" stroke="#ffffff" stroke-width="12" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <path d="M880,470 q45,-14 90,0 t90,0" fill="none" stroke="#ffffff" stroke-width="12" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <path d="M600,540 q60,-14 120,0 t120,0" fill="none" stroke="#ffffff" stroke-width="12" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <path d="M1080,505 q30,-14 60,0 t60,0" fill="none" stroke="#ffffff" stroke-width="12" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.85"/>
  <rect x="270" y="221" width="660" height="18" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="270" y1="221" x2="281" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="292" y1="221" x2="303" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="314" y1="221" x2="325" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="336" y1="221" x2="347" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="358" y1="221" x2="369" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="221" x2="391" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="402" y1="221" x2="413" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="424" y1="221" x2="435" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="446" y1="221" x2="457" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="468" y1="221" x2="479" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="490" y1="221" x2="501" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="512" y1="221" x2="523" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="534" y1="221" x2="545" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="556" y1="221" x2="567" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="578" y1="221" x2="589" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="221" x2="611" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="622" y1="221" x2="633" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="644" y1="221" x2="655" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="666" y1="221" x2="677" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="688" y1="221" x2="699" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="710" y1="221" x2="721" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="732" y1="221" x2="743" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="754" y1="221" x2="765" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="776" y1="221" x2="787" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="798" y1="221" x2="809" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="820" y1="221" x2="831" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="842" y1="221" x2="853" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="864" y1="221" x2="875" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="886" y1="221" x2="897" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="908" y1="221" x2="919" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="221" x2="941" y2="239" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <rect x="320" y="60" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="320" y1="84.5" x2="380" y2="84.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="109.5" x2="380" y2="109.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="134" x2="380" y2="134" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="158.5" x2="380" y2="158.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="183.5" x2="380" y2="183.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="320" y="252" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="320" y1="276.5" x2="380" y2="276.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="301.5" x2="380" y2="301.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="326" x2="380" y2="326" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="350.5" x2="380" y2="350.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="375.5" x2="380" y2="375.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="208" x2="350" y2="252" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="240" y="60" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="240" y1="84.5" x2="300" y2="84.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="109.5" x2="300" y2="109.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="134" x2="300" y2="134" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="158.5" x2="300" y2="158.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="183.5" x2="300" y2="183.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="240" y="252" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="240" y1="276.5" x2="300" y2="276.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="301.5" x2="300" y2="301.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="326" x2="300" y2="326" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="350.5" x2="300" y2="350.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="375.5" x2="300" y2="375.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="208" x2="270" y2="252" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="820" y="60" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="820" y1="84.5" x2="880" y2="84.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="109.5" x2="880" y2="109.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="134" x2="880" y2="134" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="158.5" x2="880" y2="158.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="183.5" x2="880" y2="183.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="820" y="252" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="820" y1="276.5" x2="880" y2="276.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="301.5" x2="880" y2="301.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="326" x2="880" y2="326" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="350.5" x2="880" y2="350.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="375.5" x2="880" y2="375.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="850" y1="208" x2="850" y2="252" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="900" y="60" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="900" y1="84.5" x2="960" y2="84.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="109.5" x2="960" y2="109.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="134" x2="960" y2="134" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="158.5" x2="960" y2="158.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="183.5" x2="960" y2="183.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="900" y="252" width="60" height="148" rx="2" fill="url(#fy56h-panel)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="900" y1="276.5" x2="960" y2="276.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="301.5" x2="960" y2="301.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="326" x2="960" y2="326" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="350.5" x2="960" y2="350.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="375.5" x2="960" y2="375.5" stroke="#a5d8ff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="930" y1="208" x2="930" y2="252" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="430" y="244" width="40" height="80" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="730" y="244" width="40" height="80" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="490" y="184" width="220" height="70" rx="30" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="570" y="144" width="60" height="172" rx="26" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="520" y1="184" x2="520" y2="254" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="650" y1="184" x2="650" y2="254" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="676" cy="219" r="22" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <g transform="rotate(-28 676 219)">
  <circle cx="676" cy="208" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="670" y="215" width="12" height="18" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  </g>
</svg>

## Ydinajatus
Satelliitti on kappale, joka kiertää toista kappaletta gravitaation vaikutuksesta. Kuu on Maan luonnollinen satelliitti. ISS ja sääsatelliitit ovat ihmisen rakentamia. Rata, jota pitkin satelliitti kiertää, on kiertorata. Avaruudessa satelliittiin vaikuttaa käytännössä vain yksi voima. Se on Maan gravitaatiovoima, ja se osoittaa kohti Maan keskipistettä. Koska se on ainoa voima, se on myös kokonaisvoima. Luvussa *Tasainen ympyräliike ja normaalikiihtyvyys* opittiin tämä: tasaisessa ympyräliikkeessä kokonaisvoima osoittaa radan keskipisteeseen ja antaa kappaleelle normaalikiihtyvyyden. Ympyräradalla gravitaatiovoima tekee juuri näin. Se on kohtisuorassa nopeuteen nähden. Siksi se ei muuta vauhtia vaan kääntää nopeuden suuntaa koko ajan.

<svg data-fig="orbit" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: satelliitti kiertää Maata ympyrärataa, joka on piirretty katkoviivalla. Satelliitti on radan ylimmässä kohdassa. Sininen nopeusnuoli v osoittaa radan tangentin suuntaan oikealle. Punainen gravitaatiovoiman nuoli F osoittaa kohti Maan keskipistettä. Sen vieressä oranssi normaalikiihtyvyyden nuoli a n osoittaa samaan suuntaan. Ohut katkoviiva jatkaa suoraan oikealle. Sitä pitkin satelliitti liikkuisi ilman gravitaatiota." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy56o-earth" cx="0.35" cy="0.35" r="0.8"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></radialGradient></defs>
  <circle cx="200" cy="214" r="128" fill="none" stroke="#6b7480" stroke-width="2" stroke-dasharray="7 6"/>
  <circle cx="200" cy="214" r="55" fill="#a5d8ff" fill-opacity="0.45"/>
  <circle cx="200" cy="214" r="52" fill="url(#fy56o-earth)" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="184.5" cy="203.5" rx="16.5" ry="11.5" fill="#e9c98a"/>
  <ellipse cx="215.5" cy="230.5" rx="10.5" ry="13.5" fill="#e9c98a"/>
  <foreignObject x="177.5" y="225.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maa}$</div></foreignObject>
  <circle cx="200" cy="214" r="3.5" fill="#1f2933"/>
  <line x1="250" y1="86" x2="572" y2="86" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <foreignObject x="339" y="47.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{ilman gravitaatiota}$</div></foreignObject>
  <rect x="166" y="79" width="22" height="14" rx="2" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5"/>
  <rect x="212" y="79" width="22" height="14" rx="2" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5"/>
  <line x1="188" y1="86" x2="212" y2="86" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="191" y="77" width="18" height="18" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="240" y1="108" x2="348" y2="108" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M337,114.5 L350,108 L337,101.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="200" y1="100" x2="200" y2="145" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M200,162 L192,144 L208,144 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="207.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <line x1="174" y1="104" x2="174" y2="150" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M167.5,139 L174,152 L180.5,139" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="125.5" y="127.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="268" y="133.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <line x1="200" y1="214" x2="282.5" y2="116" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="398" y1="128" x2="398" y2="340" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="412" y="141.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ainoa voima}$</div></foreignObject>
  <foreignObject x="412" y="177.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="412" y="213.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kohti Maan}$</div></foreignObject>
  <foreignObject x="412" y="247.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskipistettä}$</div></foreignObject>
  <foreignObject x="412" y="297.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{F} = m\,\overline{a}_\text{n}$</div></foreignObject>
</svg>

Satelliitti siis putoaa koko ajan kohti Maata, mutta ei osu siihen. Ilman gravitaatiota se jatkaisi suoraan radan tangentin suuntaan. Gravitaatio taivuttaa rataa. Kun vauhti on juuri sopiva, rata kaartuu samaa tahtia kuin Maan pinta kaartuu satelliitin alla. Silloin etäisyys Maan keskipisteestä pysyy samana ja rata on ympyrä.

Jos nopeus on pienempi, gravitaatio kääntää rataa jyrkemmin kuin ympyrä vaatisi. Satelliitti laskeutuu alemmas ja palaa sitten lähtökorkeudelle. Jos nopeus on paljon liian pieni, se osuu Maahan. Jos nopeus on suurempi, rata kaartuu loivemmin. Satelliitti nousee kauemmas ennen paluutaan. Näissä tapauksissa rata ei ole ympyrä vaan soikea, eikä tasaisen ympyräliikkeen malli kuvaa sitä.

<svg data-fig="cannon" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: kappale lähtee vaakasuoraan samasta pisteestä Maan yläpuolelta kolmella nopeudella. Radat on laskettu gravitaatiolaista. Liian pienellä nopeudella rata kaartuu jyrkemmin kuin ympyrä ja osuu Maahan. Ympyräradan nopeudella kappale kiertää ympyrää, jonka etäisyys pysyy samana kuin lähtöpisteessä. Suuremmalla nopeudella rata kaartuu loivemmin. Kappale loittonee kauemmas ja palaa lähtöpisteeseen." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy56c-earth" cx="0.35" cy="0.35" r="0.8"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></radialGradient></defs>
  <circle cx="236" cy="186" r="76" fill="#a5d8ff" fill-opacity="0.45"/>
  <circle cx="236" cy="186" r="71.92" fill="url(#fy56c-earth)" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="214.5" cy="171.5" rx="23" ry="16" fill="#e9c98a"/>
  <ellipse cx="257.5" cy="209" rx="14.5" ry="18.5" fill="#e9c98a"/>
  <foreignObject x="213.5" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maa}$</div></foreignObject>
  <polyline points="236,70 236.5,70 237.5,70 238,70 238.5,70 239.5,70 240,70 240.5,70 241,70 242,70 242.5,70.5 243,70.5 244,70.5 244.5,70.5 245,70.5 246,70.5 246.5,70.5 247,71 247.5,71 248.5,71 249,71 249.5,71 250.5,71.5 251,71.5 251.5,71.5 252,71.5 253,72 253.5,72 254,72 255,72.5 255.5,72.5 256,72.5 256.5,73 257.5,73 258,73 258.5,73.5 259,73.5 260,73.5 260.5,74 261,74 261.5,74.5 262.5,74.5 263,75 263.5,75 264,75.5 265,75.5 265.5,76 266,76 266.5,76.5 267.5,76.5 268,77 268.5,77 269,77.5 269.5,77.5 270.5,78 271,78 271.5,78.5 272,79 273,79 273.5,79.5 274,80 274.5,80 275,80.5 275.5,81 276.5,81 277,81.5 277.5,82 278,82 278.5,82.5 279,83 280,83.5 280.5,83.5 281,84 281.5,84.5 282,85 282.5,85.5 283,85.5 284,86 284.5,86.5 285,87 285.5,87.5 286,88 286.5,88.5 287,88.5 287.5,89 288,89.5 288.5,90 289,90.5 289.5,91 290,91.5 291,92 291.5,92.5 292,93 292.5,93.5 293,94 293.5,94.5 294,95 294.5,95.5 295,96 295.5,96.5 296,97 296.5,97.5 297,98 297,99 297.5,99.5 298,100 298.5,100.5 299,101 299.5,101.5 300,102 300.5,103 301,103.5 301.5,104 302,104.5 302,105 302.5,106 303,106.5 303.5,107 304,107.5 304.5,108.5 304.5,109 305,109.5 305.5,110.5 306,111 306.5,111.5 306.5,112.5 307,113 307.5,113.5 308,114.5 308,115 308.5,115.5 309,116.5 309.5,117 309.5,118 310,118.5 310.5,119 310.5,120 311,120.5 311,121.5 311.5,122 312,123 312,123.5 312.5,124.5 312.5,125 313,126 313.5,126.5 313.5,127.5 314,128 314,129 314.5,130 314.5,130.5 315,131.5 315,132 315.5,133 315.5,134 315.5,134.5 316,135.5 316,136 316.5,137 316.5,138 316.5,138.5 317,139.5 317,140.5 317,141 317.5,142 317.5,143 317.5,144 317.5,144.5 318,145.5 318,146.5 318,147.5 318,148 318,149 318.5,150 318.5,151 318.5,151.5 318.5,152.5 318.5,153.5 318.5,154.5 318.5,155.5 318.5,156 318.5,157 318.5,158 318.5,159 318.5,160 318.5,161 318.5,161.5 318.5,162.5 318.5,163.5 318.5,164.5 318,165.5 318,166.5 318,167.5 318,168.5 318,169 317.5,170 317.5,171 317.5,172 317,173 317,174 317,175 316.5,176 316.5,177 316.5,178 316,179 316,180 315.5,180.5 315.5,181.5 315,182.5 314.5,183.5 314.5,184.5 314,185.5 314,186.5 313.5,187.5 313,188.5 313,189.5 312.5,190.5 312,191.5 311.5,192.5 311,193.5 311,194.5 310.5,195 310,196 309.5,197 309,198 308.5,199 308,200 307.5,201 307,202 306.5,203 306,204 305.5,204.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="236,70 237,70 238.5,70 239.5,70 241,70 242,70 243.5,70 244.5,70.5 245.5,70.5 247,70.5 248,70.5 249.5,71 250.5,71 251.5,71 253,71 254,71.5 255.5,71.5 256.5,72 257.5,72 259,72.5 260,72.5 261.5,73 262.5,73 263.5,73.5 265,73.5 266,74 267,74.5 268.5,74.5 269.5,75 270.5,75.5 272,75.5 273,76 274,76.5 275.5,77 276.5,77.5 277.5,77.5 278.5,78 280,78.5 281,79 282,79.5 283,80 284.5,80.5 285.5,81 286.5,81.5 287.5,82 288.5,82.5 289.5,83 291,84 292,84.5 293,85 294,85.5 295,86 296,87 297,87.5 298,88 299,88.5 300,89.5 301,90 302,90.5 303,91.5 304,92 305,93 306,93.5 307,94.5 308,95 309,96 310,96.5 311,97.5 312,98 312.5,99 313.5,100 314.5,100.5 315.5,101.5 316.5,102.5 317,103 318,104 319,105 319.5,105.5 320.5,106.5 321.5,107.5 322,108.5 323,109.5 324,110 324.5,111 325.5,112 326,113 327,114 327.5,115 328.5,116 329,117 330,118 330.5,119 331.5,120 332,121 332.5,122 333.5,123 334,124 334.5,125 335,126 336,127 336.5,128 337,129 337.5,130 338,131 339,132.5 339.5,133.5 340,134.5 340.5,135.5 341,136.5 341.5,137.5 342,139 342.5,140 343,141 343.5,142 344,143.5 344.5,144.5 344.5,145.5 345,146.5 345.5,148 346,149 346.5,150 346.5,151.5 347,152.5 347.5,153.5 347.5,155 348,156 348.5,157 348.5,158.5 349,159.5 349,160.5 349.5,162 349.5,163 350,164.5 350,165.5 350.5,166.5 350.5,168 351,169 351,170.5 351,171.5 351,172.5 351.5,174 351.5,175 351.5,176.5 351.5,177.5 352,178.5 352,180 352,181 352,182.5 352,183.5 352,185 352,186 352,187 352,188.5 352,189.5 352,191 352,192 352,193.5 351.5,194.5 351.5,195.5 351.5,197 351.5,198 351,199.5 351,200.5 351,201.5 351,203 350.5,204 350.5,205.5 350,206.5 350,207.5 349.5,209 349.5,210 349,211.5 349,212.5 348.5,213.5 348.5,215 348,216 347.5,217 347.5,218.5 347,219.5 346.5,220.5 346.5,222 346,223 345.5,224 345,225.5 344.5,226.5 344.5,227.5 344,228.5 343.5,230 343,231 342.5,232 342,233 341.5,234.5 341,235.5 340.5,236.5 340,237.5 339.5,238.5 339,239.5 338,241 337.5,242 337,243 336.5,244 336,245 335,246 334.5,247 334,248 333.5,249 332.5,250 332,251 331.5,252 330.5,253 330,254 329,255 328.5,256 327.5,257 327,258 326,259 325.5,260 324.5,261 324,262 323,262.5 322,263.5 321.5,264.5 320.5,265.5 319.5,266.5 319,267 318,268 317,269 316.5,269.5 315.5,270.5 314.5,271.5 313.5,272 312.5,273 312,274 311,274.5 310,275.5 309,276 308,277 307,277.5 306,278.5 305,279 304,280 303,280.5 302,281.5 301,282 300,282.5 299,283.5 298,284 297,284.5 296,285 295,286 294,286.5 293,287 292,287.5 291,288 289.5,289 288.5,289.5 287.5,290 286.5,290.5 285.5,291 284.5,291.5 283,292 282,292.5 281,293 280,293.5 278.5,294 277.5,294.5 276.5,294.5 275.5,295 274,295.5 273,296 272,296.5 270.5,296.5 269.5,297 268.5,297.5 267,297.5 266,298 265,298.5 263.5,298.5 262.5,299 261.5,299 260,299.5 259,299.5 257.5,300 256.5,300 255.5,300.5 254,300.5 253,301 251.5,301 250.5,301 249.5,301 248,301.5 247,301.5 245.5,301.5 244.5,301.5 243.5,302 242,302 241,302 239.5,302 238.5,302 237,302 236,302 235,302 233.5,302 232.5,302 231,302 230,302 228.5,302 227.5,301.5 226.5,301.5 225,301.5 224,301.5 222.5,301 221.5,301 220.5,301 219,301 218,300.5 216.5,300.5 215.5,300 214.5,300 213,299.5 212,299.5 210.5,299 209.5,299 208.5,298.5 207,298.5 206,298 205,297.5 203.5,297.5 202.5,297 201.5,296.5 200,296.5 199,296 198,295.5 196.5,295 195.5,294.5 194.5,294.5 193.5,294 192,293.5 191,293 190,292.5 189,292 187.5,291.5 186.5,291 185.5,290.5 184.5,290 183.5,289.5 182.5,289 181,288 180,287.5 179,287 178,286.5 177,286 176,285 175,284.5 174,284 173,283.5 172,282.5 171,282 170,281.5 169,280.5 168,280 167,279 166,278.5 165,277.5 164,277 163,276 162,275.5 161,274.5 160,274 159.5,273 158.5,272 157.5,271.5 156.5,270.5 155.5,269.5 155,269 154,268 153,267 152.5,266.5 151.5,265.5 150.5,264.5 150,263.5 149,262.5 148,262 147.5,261 146.5,260 146,259 145,258 144.5,257 143.5,256 143,255 142,254 141.5,253 140.5,252 140,251 139.5,250 138.5,249 138,248 137.5,247 137,246 136,245 135.5,244 135,243 134.5,242 134,241 133,239.5 132.5,238.5 132,237.5 131.5,236.5 131,235.5 130.5,234.5 130,233 129.5,232 129,231 128.5,230 128,228.5 127.5,227.5 127.5,226.5 127,225.5 126.5,224 126,223 125.5,222 125.5,220.5 125,219.5 124.5,218.5 124.5,217 124,216 123.5,215 123.5,213.5 123,212.5 123,211.5 122.5,210 122.5,209 122,207.5 122,206.5 121.5,205.5 121.5,204 121,203 121,201.5 121,200.5 121,199.5 120.5,198 120.5,197 120.5,195.5 120.5,194.5 120,193.5 120,192 120,191 120,189.5 120,188.5 120,187 120,186 120,185 120,183.5 120,182.5 120,181 120,180 120,178.5 120.5,177.5 120.5,176.5 120.5,175 120.5,174 121,172.5 121,171.5 121,170.5 121,169 121.5,168 121.5,166.5 122,165.5 122,164.5 122.5,163 122.5,162 123,160.5 123,159.5 123.5,158.5 123.5,157 124,156 124.5,155 124.5,153.5 125,152.5 125.5,151.5 125.5,150 126,149 126.5,148 127,146.5 127.5,145.5 127.5,144.5 128,143.5 128.5,142 129,141 129.5,140 130,139 130.5,137.5 131,136.5 131.5,135.5 132,134.5 132.5,133.5 133,132.5 134,131 134.5,130 135,129 135.5,128 136,127 137,126 137.5,125 138,124 138.5,123 139.5,122 140,121 140.5,120 141.5,119 142,118 143,117 143.5,116 144.5,115 145,114 146,113 146.5,112 147.5,111 148,110 149,109.5 150,108.5 150.5,107.5 151.5,106.5 152.5,105.5 153,105 154,104 155,103 155.5,102.5 156.5,101.5 157.5,100.5 158.5,100 159.5,99 160,98 161,97.5 162,96.5 163,96 164,95 165,94.5 166,93.5 167,93 168,92 169,91.5 170,90.5 171,90 172,89.5 173,88.5 174,88 175,87.5 176,87 177,86 178,85.5 179,85 180,84.5 181,84 182.5,83 183.5,82.5 184.5,82 185.5,81.5 186.5,81 187.5,80.5 189,80 190,79.5 191,79 192,78.5 193.5,78 194.5,77.5 195.5,77.5 196.5,77 198,76.5 199,76 200,75.5 201.5,75.5 202.5,75 203.5,74.5 205,74.5 206,74 207,73.5 208.5,73.5 209.5,73 210.5,73 212,72.5 213,72.5 214.5,72 215.5,72 216.5,71.5 218,71.5 219,71 220.5,71 221.5,71 222.5,71 224,70.5 225,70.5 226.5,70.5 227.5,70.5 228.5,70 230,70 231,70 232.5,70 233.5,70 235,70 236,70 236,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="236,70 237.5,70 239.5,70 241,70 242.5,70 244,70.5 246,70.5 247.5,70.5 249,70.5 251,71 252.5,71 254,71 255.5,71.5 257.5,71.5 259,72 260.5,72.5 262,72.5 263.5,73 265.5,73.5 267,73.5 268.5,74 270,74.5 271.5,75 273,75.5 275,76 276.5,76.5 278,77 279.5,77.5 281,78 282.5,78.5 284,79 285.5,79.5 287,80 288.5,81 290,81.5 291.5,82 293,83 294.5,83.5 296,84.5 297.5,85 299,85.5 300,86.5 301.5,87.5 303,88 304.5,89 306,90 307,90.5 308.5,91.5 310,92.5 311,93.5 312.5,94 314,95 315,96 316.5,97 317.5,98 319,99 320,100 321.5,101 322.5,102 324,103 325,104 326,105 327.5,106 328.5,107.5 329.5,108.5 330.5,109.5 332,110.5 333,111.5 334,113 335,114 336,115 337,116.5 338,117.5 339,119 340,120 341,121 342,122.5 343,123.5 344,125 345,126 345.5,127.5 346.5,128.5 347.5,130 348,131.5 349,132.5 350,134 350.5,135 351.5,136.5 352,138 353,139 353.5,140.5 354.5,142 355,143 356,144.5 356.5,146 357,147 358,148.5 358.5,150 359,151.5 359.5,152.5 360,154 360.5,155.5 361.5,157 362,158.5 362.5,159.5 363,161 363.5,162.5 363.5,164 364,165.5 364.5,167 365,168 365.5,169.5 366,171 366,172.5 366.5,174 367,175.5 367,177 367.5,178 367.5,179.5 368,181 368.5,182.5 368.5,184 368.5,185.5 369,187 369,188.5 369.5,189.5 369.5,191 369.5,192.5 369.5,194 370,195.5 370,197 370,198.5 370,199.5 370,201 370,202.5 370,204 370,205.5 370,207 370,208.5 370,209.5 370,211 370,212.5 370,214 370,215.5 370,216.5 369.5,218 369.5,219.5 369.5,221 369,222.5 369,223.5 369,225 368.5,226.5 368.5,228 368,229 368,230.5 367.5,232 367.5,233 367,234.5 367,236 366.5,237.5 366,238.5 366,240 365.5,241.5 365,242.5 365,244 364.5,245 364,246.5 363.5,248 363,249 362.5,250.5 362.5,251.5 362,253 361.5,254 361,255.5 360.5,256.5 360,258 359.5,259 359,260.5 358.5,261.5 357.5,263 357,264 356.5,265 356,266.5 355.5,267.5 355,269 354,270 353.5,271 353,272.5 352.5,273.5 351.5,274.5 351,275.5 350,277 349.5,278 349,279 348,280 347.5,281.5 346.5,282.5 346,283.5 345,284.5 344.5,285.5 343.5,286.5 343,287.5 342,288.5 341.5,290 340.5,291 339.5,292 339,293 338,294 337,295 336.5,295.5 335.5,296.5 334.5,297.5 334,298.5 333,299.5 332,300.5 331,301.5 330,302.5 329.5,303 328.5,304 327.5,305 326.5,306 325.5,306.5 324.5,307.5 323.5,308.5 322.5,309 321.5,310 321,311 320,311.5 319,312.5 318,313 317,314 316,315 315,315.5 313.5,316 312.5,317 311.5,317.5 310.5,318.5 309.5,319 308.5,320 307.5,320.5 306.5,321 305.5,322 304.5,322.5 303,323 302,323.5 301,324.5 300,325 299,325.5 297.5,326 296.5,326.5 295.5,327.5 294.5,328 293.5,328.5 292,329 291,329.5 290,330 288.5,330.5 287.5,331 286.5,331.5 285.5,332 284,332.5 283,332.5 282,333 280.5,333.5 279.5,334 278.5,334.5 277,335 276,335 275,335.5 273.5,336 272.5,336 271,336.5 270,337 269,337 267.5,337.5 266.5,338 265.5,338 264,338.5 263,338.5 261.5,339 260.5,339 259,339.5 258,339.5 257,339.5 255.5,340 254.5,340 253,340 252,340.5 250.5,340.5 249.5,340.5 248.5,340.5 247,341 246,341 244.5,341 243.5,341 242,341 241,341 239.5,341.5 238.5,341.5 237,341.5 236,341.5 235,341.5 233.5,341.5 232.5,341.5 231,341 230,341 228.5,341 227.5,341 226,341 225,341 223.5,340.5 222.5,340.5 221.5,340.5 220,340.5 219,340 217.5,340 216.5,340 215,339.5 214,339.5 213,339.5 211.5,339 210.5,339 209,338.5 208,338.5 206.5,338 205.5,338 204.5,337.5 203,337 202,337 201,336.5 199.5,336 198.5,336 197,335.5 196,335 195,335 193.5,334.5 192.5,334 191.5,333.5 190,333 189,332.5 188,332.5 186.5,332 185.5,331.5 184.5,331 183.5,330.5 182,330 181,329.5 180,329 178.5,328.5 177.5,328 176.5,327.5 175.5,326.5 174.5,326 173,325.5 172,325 171,324.5 170,323.5 169,323 167.5,322.5 166.5,322 165.5,321 164.5,320.5 163.5,320 162.5,319 161.5,318.5 160.5,317.5 159.5,317 158.5,316 157,315.5 156,315 155,314 154,313 153,312.5 152,311.5 151,311 150.5,310 149.5,309 148.5,308.5 147.5,307.5 146.5,306.5 145.5,306 144.5,305 143.5,304 142.5,303 142,302.5 141,301.5 140,300.5 139,299.5 138,298.5 137.5,297.5 136.5,296.5 135.5,295.5 135,295 134,294 133,293 132.5,292 131.5,291 130.5,290 130,288.5 129,287.5 128.5,286.5 127.5,285.5 127,284.5 126,283.5 125.5,282.5 124.5,281.5 124,280 123,279 122.5,278 122,277 121,275.5 120.5,274.5 119.5,273.5 119,272.5 118.5,271 118,270 117,269 116.5,267.5 116,266.5 115.5,265 115,264 114.5,263 113.5,261.5 113,260.5 112.5,259 112,258 111.5,256.5 111,255.5 110.5,254 110,253 109.5,251.5 109.5,250.5 109,249 108.5,248 108,246.5 107.5,245 107,244 107,242.5 106.5,241.5 106,240 106,238.5 105.5,237.5 105,236 105,234.5 104.5,233 104.5,232 104,230.5 104,229 103.5,228 103.5,226.5 103,225 103,223.5 103,222.5 102.5,221 102.5,219.5 102.5,218 102,216.5 102,215.5 102,214 102,212.5 102,211 102,209.5 102,208.5 102,207 102,205.5 102,204 102,202.5 102,201 102,199.5 102,198.5 102,197 102,195.5 102.5,194 102.5,192.5 102.5,191 102.5,189.5 103,188.5 103,187 103.5,185.5 103.5,184 103.5,182.5 104,181 104.5,179.5 104.5,178 105,177 105,175.5 105.5,174 106,172.5 106,171 106.5,169.5 107,168 107.5,167 108,165.5 108.5,164 108.5,162.5 109,161 109.5,159.5 110,158.5 110.5,157 111.5,155.5 112,154 112.5,152.5 113,151.5 113.5,150 114,148.5 115,147 115.5,146 116,144.5 117,143 117.5,142 118.5,140.5 119,139 120,138 120.5,136.5 121.5,135 122,134 123,132.5 124,131.5 124.5,130 125.5,128.5 126.5,127.5 127,126 128,125 129,123.5 130,122.5 131,121 132,120 133,119 134,117.5 135,116.5 136,115 137,114 138,113 139,111.5 140,110.5 141.5,109.5 142.5,108.5 143.5,107.5 144.5,106 146,105 147,104 148,103 149.5,102 150.5,101 152,100 153,99 154.5,98 155.5,97 157,96 158,95 159.5,94 161,93.5 162,92.5 163.5,91.5 165,90.5 166,90 167.5,89 169,88 170.5,87.5 172,86.5 173,85.5 174.5,85 176,84.5 177.5,83.5 179,83 180.5,82 182,81.5 183.5,81 185,80 186.5,79.5 188,79 189.5,78.5 191,78 192.5,77.5 194,77 195.5,76.5 197,76 199,75.5 200.5,75 202,74.5 203.5,74 205,73.5 206.5,73.5 208.5,73 210,72.5 211.5,72.5 213,72 214.5,71.5 216.5,71.5 218,71 219.5,71 221,71 223,70.5 224.5,70.5 226,70.5 228,70.5 229.5,70 231,70 232.5,70 234.5,70 236,70 236,70" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="2 5"/>
  <circle cx="236" cy="70" r="7" fill="#1f2933"/>
  <line x1="248" y1="52" x2="322" y2="52" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M311,58.5 L324,52 L311,45.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="323.5" y="21.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="408" y1="150" x2="436" y2="150" stroke="#6b7480" stroke-width="3" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="444" y="135.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{liian hidas}$</div></foreignObject>
  <line x1="408" y1="194" x2="436" y2="194" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="444" y="179.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ympyrärata}$</div></foreignObject>
  <line x1="408" y1="238" x2="436" y2="238" stroke="#2b8a3e" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 5"/>
  <foreignObject x="444" y="223.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{liian nopea}$</div></foreignObject>
</svg>

## Kaava: Ratanopeus ympyräradalla
Satelliitin massa on $m$. Se kiertää keskuskappaletta ympyräradalla. Gravitaatiovoima on ainoa voima ja siis kokonaisvoima. Newtonin toisen lain mukaan sen on oltava yhtä suuri kuin ympyräliikkeeseen tarvittava voima $m a_\text{n} = \tfrac{m v^2}{r}$:
```latex
\gamma \frac{M m}{r^2} = \frac{m v^2}{r}
```
Kaavassa $\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$ on gravitaatiovakio. Massa $M$ on keskuskappaleen massa ($\text{kg}$) ja $m$ satelliitin massa ($\text{kg}$). Säde $r$ on radan säde ($\text{m}$) ja $v$ satelliitin ratanopeus ($\text{m/s}$). Radan säde mitataan keskuskappaleen keskipisteestä. Maan satelliitille $r = R + h$. Tässä $R = 6371\,\text{km}$ on Maan säde ja $h$ on satelliitin korkeus maanpinnasta.

Satelliitin massa $m$ on yhtälön kummallakin puolella, joten se supistuu pois. Kerrotaan yhtälö puolittain luvulla $r$ ja jaetaan massalla $m$. Saadaan $v^2 = \tfrac{\gamma M}{r}$. Ympyräradan ratanopeus on siis
```latex
v = \sqrt{\frac{\gamma M}{r}}
```
Ratanopeus riippuu vain keskuskappaleen massasta $M$ ja radan säteestä $r$. Satelliitin massa ei vaikuta siihen. Raskas avaruusasema ja pieni kuutiosatelliitti kiertävät samalla korkeudella samalla nopeudella. Mitä kauempana satelliitti kiertää, sitä pienempi sen ratanopeus on.

<svg data-fig="vr" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: ympyräradan ratanopeus v kilometreinä sekunnissa etäisyyden r funktiona, kun r on Maan keskipisteestä mitattu etäisyys tuhansina kilometreinä. Käyrä alkaa Maan pinnalta, r on 6 371 km ja v noin 7,9 km/s, ja laskee loivenevasti: kaukana kiertävä satelliitti liikkuu hitaammin. Käyrälle on merkitty pisteinä ISS (r 6 790 km, v 7,65 km/s), GPS-satelliitti (r 26 560 km, v 3,87 km/s) ja geostationaarinen satelliitti (r 42 164 km, v 3,07 km/s), jotka on laskettu todellisista kiertoajoista." style="max-width:100%;font-size:24px">
  <line x1="126.5" y1="300" x2="126.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="300" x2="163.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="300" x2="200" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236.5" y1="300" x2="236.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="273.5" y1="300" x2="273.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="300" x2="310" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="300" x2="346.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383.5" y1="300" x2="383.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="300" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="273.5" x2="420" y2="273.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="246.5" x2="420" y2="246.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="220" x2="420" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="193.5" x2="420" y2="193.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="166.5" x2="420" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="140" x2="420" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="113.5" x2="420" y2="113.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="86.5" x2="420" y2="86.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="60" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="300" x2="434" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,300 L433,306 L433,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="126.5" y1="300" x2="126.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163.5" y1="300" x2="163.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="147" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="200" y1="300" x2="200" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="236.5" y1="300" x2="236.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="273.5" y1="300" x2="273.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="310" y1="300" x2="310" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="293.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="346.5" y1="300" x2="346.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="383.5" y1="300" x2="383.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="367" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="420" y1="300" x2="420" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="273.5" x2="90" y2="273.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="246.5" x2="90" y2="246.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="232" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="220" x2="90" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="193.5" x2="90" y2="193.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="179" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="166.5" x2="90" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="140" x2="90" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="125.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="83" y1="113.5" x2="90" y2="113.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="86.5" x2="90" y2="86.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="72" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="83" y1="60" x2="90" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="285.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (1000\,\text{km})$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{km/s})$</div></foreignObject>
  <polyline points="136.5,89 139,94 141.5,99 144,103.5 146,107.5 148.5,111.5 151,115.5 153,118.5 155.5,122 158,125 160.5,128 162.5,131 165,133.5 167.5,136 170,138.5 172,141 174.5,143 177,145.5 179,147.5 181.5,149.5 184,151.5 186.5,153 188.5,155 191,156.5 193.5,158 195.5,160 198,161.5 200.5,163 203,164.5 205,165.5 207.5,167 210,168.5 212.5,169.5 214.5,171 217,172 219.5,173.5 221.5,174.5 224,175.5 226.5,176.5 229,177.5 231,178.5 233.5,179.5 236,180.5 238,181.5 240.5,182.5 243,183.5 245.5,184.5 247.5,185 250,186 252.5,187 255,187.5 257,188.5 259.5,189.5 262,190 264,191 266.5,191.5 269,192 271.5,193 273.5,193.5 276,194.5 278.5,195 280.5,195.5 283,196.5 285.5,197 288,197.5 290,198 292.5,198.5 295,199.5 297,200 299.5,200.5 302,201 304.5,201.5 306.5,202 309,202.5 311.5,203 314,203.5 316,204 318.5,204.5 321,205 323,205.5 325.5,206 328,206.5 330.5,207 332.5,207.5 335,208 337.5,208.5 339.5,209 342,209 344.5,209.5 347,210 349,210.5 351.5,211 354,211.5 356.5,211.5 358.5,212 361,212.5 363.5,213 365.5,213 368,213.5 370.5,214 373,214.5 375,214.5 377.5,215 380,215.5 382,215.5 384.5,216 387,216.5 389.5,216.5 391.5,217 394,217.5 396.5,217.5 399,218 401,218.5 403.5,218.5 406,219 408,219 410.5,219.5 413,220 415.5,220 417.5,220.5 420,220.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="140" cy="96" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="156" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ISS}$</span></div></foreignObject>
  <circle cx="285" cy="196.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="262.5" y="152" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{GPS}$</span></div></foreignObject>
  <circle cx="399" cy="218" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="203" y="233.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{geostationaarinen}$</span></div></foreignObject>
  <foreignObject x="235" y="95" width="150" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v = \sqrt{\dfrac{\gamma M}{r}}$</div></foreignObject>
</svg>

Satelliitti kulkee yhden kierroksen aikana ympyrän kehän $2\pi r$. Kiertoaika saadaan luvun *Tasainen ympyräliike ja normaalikiihtyvyys* kaavasta $v = \tfrac{2\pi r}{T}$:
```latex
T = \frac{2\pi r}{v}
```
Tässä $T$ on kiertoaika ($\text{s}$). Kaukana kiertävän satelliitin rata on pidempi ja sen vauhti pienempi. Siksi kiertoaika kasvaa nopeasti, kun etäisyys kasvaa. ISS kiertää Maan noin puolessatoista tunnissa. Kuu kiertää Maan noin $27\,\text{d}$:ssä. Samasta yhtälöstä voi ratkaista myös keskuskappaleen massan $M$, kun mitataan radan säde ja kiertoaika. Näin on saatu esimerkiksi Maan, Auringon ja Marsin massat.

### Geostationaarinen rata
Geostationaarinen satelliitti kiertää päiväntasaajan yläpuolella samaan suuntaan kuin Maa pyörii. Sen kiertoaika on sama kuin Maan pyörähdysaika, $23\,\text{h}\;56\,\text{min}$. Siksi satelliitti näyttää pysyvän taivaalla paikallaan, ja lautasantennin voi suunnata siihen kerran. Kiertoaika määrää radan säteen. Siksi kaikki geostationaariset satelliitit kiertävät samalla korkeudella, noin $35\,800\,\text{km}$:n korkeudella.

## Painottomuus
Avaruusasemalla astronautit leijuvat, ja vaaka näyttäisi nollaa. Syy ei ole se, että painovoimaa ei olisi. ISS:n korkeudella $420\,\text{km}$ gravitaatiovoiman antama kiihtyvyys on $\tfrac{\gamma M}{r^2} \approx 8{,}6\,\text{m/s}^2$. Se on noin $88\,\%$ maanpinnan arvosta. Astronauttiin, jonka massa on $70\,\text{kg}$, vaikuttaa siis noin $605\,\text{N}$:n paino. Se on Maan gravitaatiovoima $F$. Maanpinnalla voima olisi $687\,\text{N}$.

Asema ja astronautti ovat vapaassa pudotuksessa. Kumpaankin vaikuttaa vain gravitaatio, ja kumpikin saa saman kiihtyvyyden kohti Maata. Ne putoavat samalla tavalla. Siksi lattia ei paina astronauttia eikä vaaka joudu tukemaan häntä. Tukivoima on nolla. **Painottomuus on tila, jossa kappaleeseen vaikuttaa vain gravitaatio ja se putoaa vapaasti: tukivoima on nolla, vaikka paino vaikuttaa koko ajan.**

<svg data-fig="paino" viewBox="0 0 600 380" role="img" aria-label="Kaksi voimakuviota samassa mittakaavassa. Vasemmalla astronautti seisoo vaa&#x27;alla Maan pinnalla, ja hänet on piirretty suorakulmiona: gravitaatiovoima F (paino) osoittaa keskipisteestä alas ja vaa&#x27;an tukivoima N alapinnasta ylös, yhtä pitkinä, joten kiihtyvyys on nolla. Oikealla sama astronautti avaruusasemalla: ainoa voima on noin 12 prosenttia lyhyempi gravitaatiovoima F, tukivoimaa ei ole, ja oranssi kiihtyvyysnuoli a osoittaa alas kohti Maata kappaleen vieressä. Asema putoaa samalla kiihtyvyydellä, joten lattia ei paina astronauttia." style="max-width:100%;font-size:24px">
  <foreignObject x="71" y="11.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maan pinnalla}$</div></foreignObject>
  <foreignObject x="352.5" y="11.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{avaruusasemalla}$</div></foreignObject>
  <line x1="300" y1="14" x2="300" y2="366" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="88" y="234" width="124" height="14" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="122" y="138" width="56" height="96" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="186" x2="150" y2="258.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,275.5 L142,257.5 L158,257.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="111.5" y="267" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <line x1="168" y1="234" x2="168" y2="161.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M168,144.5 L176,162.5 L160,162.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="175.5" y="140" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="115" y="341.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{a} = \overline{0}$</div></foreignObject>
  <rect x="422" y="138" width="56" height="96" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="450" y1="186" x2="450" y2="247.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M450,264.5 L442,246.5 L458,246.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="411.5" y="256" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <line x1="506" y1="156" x2="506" y2="224" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M499.5,213 L506,226 L512.5,213" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="511.5" y="203.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="427.5" y="341.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N = 0$</div></foreignObject>
</svg>

Saman tilan voi kokea hetken maan päälläkin. Se tapahtuu hypyn aikana ja vapaasti putoavassa hississä. Sen voi kokea myös lentokoneessa, joka lentää heittoliikkeen rataa. Painottomuutta ei selitä mikään gravitaation kumoava "keskipakoisvoima". Jos jokin voima kumoaisi gravitaation, kokonaisvoima olisi nolla. Silloin asema jatkaisi suoraan eteenpäin eikä kiertäisi Maata.

## Milloin ympyrämalli pätee
Tasaisen ympyräliikkeen malli on yksinkertaistus. Se kuvaa satelliitin liikettä hyvin, kun

- keskuskappale on paljon massiivisempi kuin satelliitti, joten sitä voidaan pitää paikallaan pysyvänä,
- muiden kappaleiden gravitaatio ja ilmanvastus ovat niin pieniä, että vain keskuskappaleen gravitaatio vaikuttaa,
- satelliitin nopeus on juuri sen radan säteen ympyräradan nopeus, jolloin etäisyys keskipisteestä pysyy vakiona.

Monet todelliset radat ovat lähes ympyröitä. Maan etäisyys Auringosta vaihtelee vain noin $3\,\%$ keskietäisyydestä. Siksi ympyrämalli kuvaa Maan rataa hyvin. Kuun etäisyys Maasta vaihtelee noin $11\,\%$. Malli antaa Kuulle silti hyvän likiarvon. Halleyn komeetan rata on sen sijaan hyvin pitkänomainen. Ympyrämalli ei sovi siihen lainkaan.

| Kappale | lähin etäisyys | suurin etäisyys |
| --- | --- | --- |
| Maa | $147{,}1\,\text{milj. km}$ | $152{,}1\,\text{milj. km}$ |
| Kuu | $363\,300\,\text{km}$ | $405\,500\,\text{km}$ |
| Halleyn komeetta | $88\,\text{milj. km}$ | $5250\,\text{milj. km}$ |

Maan ja Halleyn komeetan etäisyydet on mitattu Auringosta. Kuun etäisyys on mitattu Maasta. Lähde: NASA, Planetary Fact Sheets (Earth, Moon) ja Halleyn komeetan ratatiedot, 2024.

<svg data-fig="radat" viewBox="0 0 600 360" role="img" aria-label="Kaksi rataa, kumpikin omassa mittakaavassaan, Aurinko radan polttopisteessä. Vasemmalla Maan rata: pienin etäisyys Auringosta 147,1 miljoonaa kilometriä ja suurin 152,1 miljoonaa kilometriä. Rata on piirretty yhtenäisellä viivalla ja sen päälle katkoviivalla ympyrä, eikä niitä erota toisistaan. Oikealla Halleyn komeetan rata: pienin etäisyys 88 miljoonaa kilometriä ja suurin noin 5 250 miljoonaa kilometriä, erittäin pitkänomainen ellipsi." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy56r-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><radialGradient id="fy56h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient></defs>
  <foreignObject x="96" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maan rata}$</div></foreignObject>
  <foreignObject x="327.5" y="11.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Halleyn komeetan rata}$</div></foreignObject>
  <line x1="300" y1="14" x2="300" y2="346" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <ellipse cx="150" cy="182" rx="112" ry="112" fill="none" stroke="#1f2933" stroke-width="3"/>
  <circle cx="150" cy="182" r="112" fill="none" stroke="#6b7480" stroke-width="2" stroke-dasharray="5 7"/>
  <circle cx="152" cy="182" r="22.5" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="152" cy="182" r="14" fill="url(#fy56r-sun)"/>
  <circle cx="38" cy="182" r="7" fill="#2f74b5" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="52" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Maa}$</div></foreignObject>
  <foreignObject x="14" y="309.5" width="272" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$147{,}1\text{–}152{,}1\ \text{milj. km}$</div></foreignObject>
  <ellipse cx="450" cy="182" rx="128" ry="32.5" fill="none" stroke="#1f2933" stroke-width="3"/>
  <circle cx="574" cy="182" r="13" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="574" cy="182" r="8" fill="url(#fy56h-sun)"/>
  <circle cx="322" cy="182" r="6" fill="#a5d8ff" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="328" y="123.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{komeetta}$</div></foreignObject>
  <foreignObject x="483" y="207.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{Aurinko}$</div></foreignObject>
  <foreignObject x="325" y="309.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$88\text{–}5250\ \text{milj. km}$</div></foreignObject>
</svg>

Tarkoissa mittauksissa näkyy pieniä poikkeamia mallista. Kuun ratanopeus on mitatuista arvoista laskettuna $1{,}023\,\text{km/s}$. Malli antaa $1{,}018\,\text{km/s}$, joten mitattu arvo on noin $0{,}5\,\%$ suurempi. Syy on se, että Kuun massa on noin $\tfrac{1}{81}$ Maan massasta. Maa ja Kuu kiertävät yhteistä massakeskipistettä, eikä Maa pysy paikallaan. ISS:n korkeudella ohut ilma jarruttaa asemaa, ja rata madaltuu hitaasti. Siksi asemaa nostetaan moottoreilla säännöllisesti.

## Esimerkki
Kansainvälinen avaruusasema ISS kiertää Maata lähes ympyrärataa noin $420\,\text{km}$:n korkeudella. Laske aseman ratanopeus ja kiertoaika. Maan massa on $M = 5{,}97 \cdot 10^{24}\,\text{kg}$ ja säde $R = 6371\,\text{km}$. Ilmanvastus jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** Korkeus on $h = 420\,\text{km}$. Maan massa on $M = 5{,}97 \cdot 10^{24}\,\text{kg}$ ja säde $R = 6371\,\text{km}$. Gravitaatiovakio on $\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$. Kysytään ratanopeutta $v$ ja kiertoaikaa $T$.

<!-- vaihe -->

**Periaate.** Ilmanvastus jätetään huomiotta. Silloin asemaan vaikuttaa vain Maan gravitaatiovoima. Se on siis kokonaisvoima. Ympyräradalla se antaa normaalikiihtyvyyden kohti Maan keskipistettä: $\gamma \tfrac{Mm}{r^2} = \tfrac{mv^2}{r}$. Radan säde mitataan Maan keskipisteestä, joten $r = R + h$.

<!-- vaihe -->

**Kaava ratkaistuna.** Aseman massa supistuu pois:
```latex
\begin{aligned}
r &= R + h \\
v &= \sqrt{\frac{\gamma M}{r}} \\
T &= \frac{2\pi r}{v}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muutetaan etäisyydet metreiksi: $R = 6371\,\text{km} = 6{,}371 \cdot 10^{6}\,\text{m}$ ja $h = 420\,\text{km} = 0{,}420 \cdot 10^{6}\,\text{m}$. Siis $r = 6{,}791 \cdot 10^{6}\,\text{m}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&v = \sqrt{\frac{\gamma M}{r}} \\
&\gamma M = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\
&\quad \cdot 5{,}97 \cdot 10^{24}\,\text{kg} \\
&\quad = 3{,}98438 \cdot 10^{14}\,\text{m}^3/\text{s}^2 \\
&v = \sqrt{\frac{3{,}98438 \cdot 10^{14}\,\text{m}^3/\text{s}^2}{6{,}791 \cdot 10^{6}\,\text{m}}} \\
&= 7659{,}7\,\text{m/s} \\[6pt]
&T = \frac{2\pi r}{v} \\
&= \frac{2\pi \cdot 6{,}791 \cdot 10^{6}\,\text{m}}{7659{,}7\,\text{m/s}} \\
&= 5570{,}6\,\text{s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ratanopeus on $v \approx 7{,}66\,\text{km/s}$ ja kiertoaika $T \approx 5570\,\text{s} \approx 92{,}8\,\text{min}$. Tulokset on annettu kolmella merkitsevällä numerolla, kuten Maan massa $5{,}97 \cdot 10^{24}\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** NASAn mukaan ISS kiertää Maan noin $92{,}9\,\text{min}$:ssa. Malli on siis hyvin lähellä mitattua. Aivan maanpinnan tasolla ympyräradan nopeus olisi $\sqrt{gR} = \sqrt{9{,}81\,\text{m/s}^2 \cdot 6{,}371 \cdot 10^{6}\,\text{m}} \approx 7{,}9\,\text{km/s}$. ISS on hieman kauempana, joten sen nopeus on hieman pienempi. Niin pitääkin olla.

## Yleinen virhekäsitys
"Avaruudessa ei ole painovoimaa, siksi astronautit leijuvat." Tämä väite on väärä. ISS:n korkeudella gravitaatio on lähes yhtä voimakas kuin maanpinnalla. Juuri se pitää aseman radallaan. Ilman gravitaatiota asema lentäisi suoraan pois. Astronautit leijuvat, koska he ja asema putoavat vapaasti samalla kiihtyvyydellä.

Toinen virhe on sijoittaa kaavaan $v = \sqrt{\tfrac{\gamma M}{r}}$ korkeus $h$. Pitää sijoittaa etäisyys Maan keskipisteestä, $r = R + h$. ISS:lle väärä sijoitus antaisi nopeudeksi noin $31\,\text{km/s}$. Se on nelinkertainen todelliseen verrattuna. Kolmas virhe on luulla, että raskaan satelliitin täytyy kiertää nopeammin. Suurempi massa saa suuremman gravitaatiovoiman. Se tarvitsee myös suuremman voiman kääntyäkseen. Siksi massa supistuu pois.

## Tiivistelmä
- Satelliittiin vaikuttaa vain keskuskappaleen gravitaatiovoima. Se on kokonaisvoima, joka antaa ympyräradalla normaalikiihtyvyyden: $\gamma \tfrac{Mm}{r^2} = \tfrac{mv^2}{r}$.
- Ympyräradan ratanopeus on $v = \sqrt{\tfrac{\gamma M}{r}}$ ja kiertoaika $T = \tfrac{2\pi r}{v}$. Satelliitin massa ei vaikuta. Kauempana kiertävä satelliitti on hitaampi, ja sen kiertoaika on pidempi.
- Radan säde mitataan keskuskappaleen keskipisteestä: $r = R + h$.
- Painottomuus on vapaata putoamista: gravitaatio vaikuttaa, mutta tukivoima on nolla.
- Ympyrämalli pätee, kun keskuskappale on paljon satelliittia massiivisempi, muut voimat ovat pieniä ja rata on lähes ympyrä.
