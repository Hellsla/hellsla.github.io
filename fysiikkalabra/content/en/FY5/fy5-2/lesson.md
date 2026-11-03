# Equilibrium of a body: forces and moments

> **Why** can a paint can be placed on the overhang of a plank lying across trestles, but only up to a certain point before the plank topples?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a painter is painting the wall of a house red. In front of the wall there are two painter&#x27;s trestles with a long plank on top of them. The painter stands on the plank between the trestles and reaches up under the eaves with a brush. The right end of the plank reaches far beyond the right-hand trestle, and a large paint tin stands on this overhang. There is nothing under the overhang, which raises the question of how far out along the overhang the tin can be moved before the plank topples." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy52h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy52h-win90" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#a5d8ff"/></linearGradient><linearGradient id="fy52h-win720" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#a5d8ff"/></linearGradient><linearGradient id="fy52h-grass" gradientUnits="userSpaceOnUse" x1="0" y1="506" x2="0" y2="600"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy52h-beam1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy52h-beam2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy52h-plank" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#a97a35"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="480" fill="url(#fy52h-sky)"/>
  <path d="M1056,132 Q1055,111.5 1079,114 Q1088.5,92.5 1112.5,99.5 Q1134,87.5 1146,110.5 Q1167.5,113 1165,132 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M1000,430 L1010,402 L1020,430 L1030.5,400.5 L1041,430 L1054,391 L1066.5,430 L1079,392 L1092,430 L1109.5,372 L1127.5,430 L1141.5,385.5 L1156,430 L1170.5,384 L1185,430 L1199.5,384.5 L1214,430 V510 H1000 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="-10" y="40" width="1020" height="452" fill="#f2a69c"/>
  <path d="M-10,40 H600 L594,96 L606,150 L590,214 L604,290 L592,360 L604,430 L596,492 H-10 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="14" y1="44" x2="14" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="14" y1="44" x2="14" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="48" y1="44" x2="48" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="48" y1="44" x2="48" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="82" y1="44" x2="82" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="82" y1="44" x2="82" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="116" y1="44" x2="116" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="44" x2="116" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="150" y1="44" x2="150" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="44" x2="150" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="184" y1="44" x2="184" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="184" y1="44" x2="184" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="218" y1="44" x2="218" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="218" y1="44" x2="218" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="252" y1="44" x2="252" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="252" y1="44" x2="252" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="286" y1="44" x2="286" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="286" y1="44" x2="286" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="320" y1="44" x2="320" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="44" x2="320" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="354" y1="44" x2="354" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="354" y1="44" x2="354" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="388" y1="44" x2="388" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="388" y1="44" x2="388" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="422" y1="44" x2="422" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="422" y1="44" x2="422" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="456" y1="44" x2="456" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="456" y1="44" x2="456" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="490" y1="44" x2="490" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="490" y1="44" x2="490" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="524" y1="44" x2="524" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="524" y1="44" x2="524" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="558" y1="44" x2="558" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="558" y1="44" x2="558" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="592" y1="44" x2="592" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="592" y1="44" x2="592" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="626" y1="44" x2="626" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="626" y1="44" x2="626" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="660" y1="44" x2="660" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="44" x2="660" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="694" y1="44" x2="694" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="694" y1="44" x2="694" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="728" y1="44" x2="728" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="728" y1="44" x2="728" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="762" y1="44" x2="762" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="762" y1="44" x2="762" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="796" y1="44" x2="796" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="796" y1="44" x2="796" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="830" y1="44" x2="830" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="830" y1="44" x2="830" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="864" y1="44" x2="864" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="864" y1="44" x2="864" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="898" y1="44" x2="898" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="898" y1="44" x2="898" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="932" y1="44" x2="932" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="932" y1="44" x2="932" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="966" y1="44" x2="966" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="966" y1="44" x2="966" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <line x1="1000" y1="44" x2="1000" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1000" y1="44" x2="1000" y2="490" stroke="#ffffff" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>
  <path d="M750.5,438 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M980.5,184 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M703,236 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M713.5,273.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M636.5,113 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M654.5,306.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M841,198.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M944,282.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M829.5,229.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M657.5,203.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M850.5,378.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M713.5,186.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M808,399.5 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <path d="M675,404 l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="#f1dfb5" fill-opacity="0.8"/>
  <rect x="90" y="96" width="150" height="170" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="104" y="110" width="122" height="142" fill="url(#fy52h-win90)" stroke="#1f2933" stroke-width="2"/>
  <line x1="165" y1="110" x2="165" y2="252" stroke="#ffffff" stroke-width="8" stroke-linecap="butt"/>
  <line x1="104" y1="181" x2="226" y2="181" stroke="#ffffff" stroke-width="8" stroke-linecap="butt"/>
  <rect x="80" y="266" width="170" height="14" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="720" y="96" width="150" height="170" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="734" y="110" width="122" height="142" fill="url(#fy52h-win720)" stroke="#1f2933" stroke-width="2"/>
  <line x1="795" y1="110" x2="795" y2="252" stroke="#ffffff" stroke-width="8" stroke-linecap="butt"/>
  <line x1="734" y1="181" x2="856" y2="181" stroke="#ffffff" stroke-width="8" stroke-linecap="butt"/>
  <rect x="710" y="266" width="170" height="14" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="994" y="40" width="22" height="452" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="-10" y="22" width="1050" height="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M-10,0 H1060 L1044,24 H-10 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="-10" y="488" width="1020" height="20" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="0" y="506" width="1200" height="94" fill="url(#fy52h-grass)"/>
  <line x1="10" y1="588.5" x2="16" y2="576.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="36" y1="585.5" x2="42" y2="573.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="62" y1="568" x2="68" y2="556" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="88" y1="570" x2="94" y2="558" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="114" y1="533.5" x2="120" y2="521.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="140" y1="557.5" x2="146" y2="545.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="166" y1="556" x2="172" y2="544" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="192" y1="556" x2="198" y2="544" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="218" y1="555.5" x2="224" y2="543.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="244" y1="556" x2="250" y2="544" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="270" y1="567.5" x2="276" y2="555.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="296" y1="535" x2="302" y2="523" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="322" y1="541.5" x2="328" y2="529.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="348" y1="578" x2="354" y2="566" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="374" y1="545" x2="380" y2="533" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="550" x2="406" y2="538" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="426" y1="532.5" x2="432" y2="520.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="452" y1="562.5" x2="458" y2="550.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="478" y1="534.5" x2="484" y2="522.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="504" y1="560" x2="510" y2="548" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="530" y1="558.5" x2="536" y2="546.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="556" y1="560" x2="562" y2="548" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="582" y1="584" x2="588" y2="572" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="608" y1="585" x2="614" y2="573" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="634" y1="565.5" x2="640" y2="553.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="660" y1="537.5" x2="666" y2="525.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="686" y1="555.5" x2="692" y2="543.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="712" y1="581" x2="718" y2="569" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="738" y1="557.5" x2="744" y2="545.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="764" y1="544" x2="770" y2="532" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="790" y1="589" x2="796" y2="577" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="816" y1="552" x2="822" y2="540" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="842" y1="588" x2="848" y2="576" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="868" y1="566.5" x2="874" y2="554.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="894" y1="578.5" x2="900" y2="566.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="920" y1="546.5" x2="926" y2="534.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="946" y1="546.5" x2="952" y2="534.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="972" y1="541.5" x2="978" y2="529.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="998" y1="562.5" x2="1004" y2="550.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1024" y1="564" x2="1030" y2="552" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1050" y1="564.5" x2="1056" y2="552.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1076" y1="565" x2="1082" y2="553" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1102" y1="584" x2="1108" y2="572" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1128" y1="560" x2="1134" y2="548" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1154" y1="560.5" x2="1160" y2="548.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1180" y1="533" x2="1186" y2="521" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="560" cy="562" rx="430" ry="10" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M282,418 L232,560" fill="none" stroke="#1f2933" stroke-width="17" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M282,418 L232,560" fill="none" stroke="#e9c98a" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M298,418 L348,560" fill="none" stroke="#1f2933" stroke-width="17" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M298,418 L348,560" fill="none" stroke="#e9c98a" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="252" y="482" width="76" height="12" rx="3" fill="#e9c98a" stroke="#a97a35" stroke-width="2"/>
  <rect x="274" y="408" width="32" height="22" rx="3" fill="url(#fy52h-beam1)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M662,418 L612,560" fill="none" stroke="#1f2933" stroke-width="17" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M662,418 L612,560" fill="none" stroke="#e9c98a" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M678,418 L728,560" fill="none" stroke="#1f2933" stroke-width="17" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M678,418 L728,560" fill="none" stroke="#e9c98a" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="632" y="482" width="76" height="12" rx="3" fill="#e9c98a" stroke="#a97a35" stroke-width="2"/>
  <rect x="654" y="408" width="32" height="22" rx="3" fill="url(#fy52h-beam2)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="170" y="390" width="760" height="18" rx="2" fill="url(#fy52h-plank)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M200,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M290,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M380,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M470,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M560,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M650,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M740,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M830,399 q30,-3 60,0" fill="none" stroke="#f1dfb5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M469.5,239.5 L457,379" fill="none" stroke="#1f2933" stroke-width="31.7143" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M469.5,239.5 L457,379" fill="none" stroke="#ffffff" stroke-width="26.9571" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M444.5,385 h25.5" fill="none" stroke="#1f2933" stroke-width="12.6857" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M482.5,239.5 L495,379" fill="none" stroke="#1f2933" stroke-width="31.7143" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M482.5,239.5 L495,379" fill="none" stroke="#ffffff" stroke-width="26.9571" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M482.5,385 h25.5" fill="none" stroke="#1f2933" stroke-width="12.6857" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M442.5,141 L438,234.5" fill="none" stroke="#1f2933" stroke-width="21.4071" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M442.5,141 L438,234.5" fill="none" stroke="#ffffff" stroke-width="16.65" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="437" cy="242.5" r="8.72143" fill="#f1dfb5"/>
  <path d="M439.5,142.5 Q436.5,119 476,117.5 Q515.5,119 512.5,142.5 L507.5,250.5 H444.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M458.5,120.5 L455.5,207.5 M493.5,120.5 L496.5,207.5" fill="none" stroke="#c9c2b2" stroke-width="4" stroke-linejoin="round"/>
  <rect x="452" y="209" width="47.5" height="27" rx="4" fill="#e3dccb" stroke="#1f2933" stroke-width="2"/>
  <path d="M507.5,139.5 L568,72" fill="none" stroke="#1f2933" stroke-width="21.4071" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M507.5,139.5 L568,72" fill="none" stroke="#ffffff" stroke-width="16.65" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="570" cy="68" r="8.72143" fill="#f1dfb5"/>
  <rect x="468" y="98" width="16" height="22" fill="#f1dfb5"/>
  <circle cx="476" cy="77.5" r="25.3714" fill="#a97a35"/>
  <path d="M449,74.5 Q450.5,46 476,46 Q501.5,46 503,74.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="447.5" y="69.5" width="57" height="8" rx="3" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M564,76 L576,56" fill="none" stroke="#a97a35" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="572" y="32" width="16" height="26" fill="#1f2933" transform="rotate(28 574 58)"/>
  <rect x="575" y="18" width="10" height="16" fill="#c92a2a" transform="rotate(28 574 58)"/>
  <path d="M815.0,332 L819.0,390 H863.0 L867.0,332 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="818" y="354" width="46" height="19.5" fill="#c92a2a"/>
  <rect x="812" y="328" width="58" height="9" rx="3" fill="#c9c2b2" stroke="#1f2933" stroke-width="2"/>
  <path d="M817.0,336 Q841,288 865.0,336" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M835,328 q6,10 12,0" fill="#c92a2a"/>
</svg>

## Key idea

### Two equilibrium conditions
In the chapter *Moment: the turning effect of a force* we learned that a force rotates a body the more, the greater the moment of the force $M = Fr$. For a body to stay at rest, it is not enough that the forces cancel each other. A body is in **equilibrium** when it neither starts to move nor starts to rotate. For translation the condition is familiar from Newton's laws: the sum of the forces is zero. For rotation the condition is new: the sum of the moments of the forces is zero. In both cases in the figure two equal and opposite forces act on the ruler, so the sum of the forces is zero. On the left the forces lie along the same line and do not rotate the ruler. On the right they act along different lines, and their moments rotate the ruler in the same direction: the ruler starts to rotate, although its middle does not start to move.

<svg data-fig="pari" viewBox="0 0 600 330" role="img" aria-label="Schematic figure, a ruler on a table seen from above, two cases. On the left, equal and opposite forces F1 and F2 pull the ends of the ruler along the ruler on the same line: the sum of the forces and the sum of the moments are zero, and the ruler does not rotate. On the right, equal and opposite forces act on the ends of the ruler perpendicular to it along different lines: the sum of the forces is zero but the sum of the moments is not, and the ruler starts to rotate, shown by a curved arrow." style="max-width:100%;font-size:24px">
  <line x1="300" y1="20" x2="300" y2="316" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="65" y="11.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{does not rotate}$</div></foreignObject>
  <foreignObject x="402.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rotates}$</div></foreignObject>
  <rect x="70" y="158" width="160" height="24" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <line x1="80" y1="158" x2="80" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="90" y1="158" x2="90" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="100" y1="158" x2="100" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="110" y1="158" x2="110" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="120" y1="158" x2="120" y2="171" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="130" y1="158" x2="130" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="140" y1="158" x2="140" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="150" y1="158" x2="150" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="160" y1="158" x2="160" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="170" y1="158" x2="170" y2="171" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="180" y1="158" x2="180" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="190" y1="158" x2="190" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="200" y1="158" x2="200" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="210" y1="158" x2="210" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="220" y1="158" x2="220" y2="171" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <rect x="370" y="158" width="160" height="24" fill="#c4ccd4" stroke="#8a96a3" stroke-width="1.5"/>
  <line x1="380" y1="158" x2="380" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="390" y1="158" x2="390" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="400" y1="158" x2="400" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="410" y1="158" x2="410" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="420" y1="158" x2="420" y2="171" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="430" y1="158" x2="430" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="440" y1="158" x2="440" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="450" y1="158" x2="450" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="460" y1="158" x2="460" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="470" y1="158" x2="470" y2="171" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="480" y1="158" x2="480" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="490" y1="158" x2="490" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="500" y1="158" x2="500" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="510" y1="158" x2="510" y2="166" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="520" y1="158" x2="520" y2="171" stroke="#1f2933" stroke-width="1" stroke-linecap="butt"/>
  <line x1="70" y1="170" x2="35" y2="170" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M18,170 L36,162 L36,178 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="5.5" y="129.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{1}$</div></foreignObject>
  <line x1="230" y1="170" x2="265" y2="170" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M282,170 L264,178 L264,162 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="263.5" y="129.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{2}$</div></foreignObject>
  <line x1="372" y1="158" x2="372" y2="105" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M372,88 L380,106 L364,106 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="323.5" y="79.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{1}$</div></foreignObject>
  <line x1="528" y1="182" x2="528" y2="235" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M528,252 L520,234 L536,234 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="531.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{2}$</div></foreignObject>
  <path d="M406.5,145 A50,50 0 0 1 490.5,140.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M493.5,145 L482,137.5 L492.5,131.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="108.5" y="253.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <foreignObject x="121" y="289.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma M = 0$</div></foreignObject>
  <foreignObject x="408.5" y="253.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Sigma\overline{F} = \overline{0}$</div></foreignObject>
  <foreignObject x="421" y="289.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\Sigma M \neq 0$</div></foreignObject>
</svg>

### Centre of mass
The Earth's gravitational pull acts on every part of a body. When the moment of the weight is calculated, however, the whole weight can be thought to act at a single point, the **centre of mass** of the body. The centre of mass of a uniform, symmetrical body, such as a plank of constant thickness, is at its middle. This is why the weight is drawn in a free-body diagram starting from the centre of mass. The common centre of mass of two bodies is between their centres of mass, nearer the heavier body. When a body is supported at one point, it stays in place only if the centre of mass is on the vertical line through the point of support: otherwise the moment of the weight about the point of support rotates the body.

### When a body topples
A body standing on a surface rests on its whole base. It stays upright when the vertical line through the centre of mass falls within the base. The moment of the weight about the edge of the base then turns the body back onto its base. If the vertical line falls outside the base, the moment of the weight about the lower edge rotates the body over the edge, and the body topples. A low, wide body therefore withstands a greater tilt than a tall, narrow one. The boxes in the figure are on the same inclined plane, and friction prevents them from sliding.

<svg data-fig="kaatuu" viewBox="0 0 600 372" role="img" aria-label="Scale drawing: two boxes on the same 30 degree inclined plane, friction prevents sliding. The low box is 0.60 m wide and 0.60 m high, the tall box 0.30 m wide and 0.80 m high. From the centre of mass of each a vertical dashed line runs down to the plane. The line of the low box meets the base of the box, so it stays upright. The line of the tall box meets the plane outside the lower edge of the base, so it topples, shown by a curved arrow." style="max-width:100%;font-size:24px">
  <line x1="40" y1="340" x2="560" y2="40" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="40" y1="340" x2="30" y2="352" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="54" y1="332" x2="44" y2="344" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="67.5" y1="324" x2="57.5" y2="336" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="81.5" y1="316" x2="71.5" y2="328" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95.5" y1="308" x2="85.5" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109.5" y1="300" x2="99.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="292" x2="113" y2="304" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="137" y1="284" x2="127" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="151" y1="276" x2="141" y2="288" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164.5" y1="268" x2="154.5" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="178.5" y1="260" x2="168.5" y2="272" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="252" x2="182.5" y2="264" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="206.5" y1="244" x2="196.5" y2="256" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220" y1="236" x2="210" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="234" y1="228" x2="224" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="220" x2="238" y2="232" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="261.5" y1="212" x2="251.5" y2="224" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="204" x2="265.5" y2="216" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="289.5" y1="196" x2="279.5" y2="208" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="303.5" y1="188" x2="293.5" y2="200" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317" y1="180" x2="307" y2="192" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331" y1="172" x2="321" y2="184" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345" y1="164" x2="335" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="358.5" y1="156" x2="348.5" y2="168" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="372.5" y1="148" x2="362.5" y2="160" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="386.5" y1="140" x2="376.5" y2="152" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400.5" y1="132" x2="390.5" y2="144" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414" y1="124" x2="404" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428" y1="116" x2="418" y2="128" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="442" y1="108" x2="432" y2="120" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455.5" y1="100" x2="445.5" y2="112" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="469.5" y1="92" x2="459.5" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="483.5" y1="84" x2="473.5" y2="96" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="497.5" y1="76" x2="487.5" y2="88" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="511" y1="68" x2="501" y2="80" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="525" y1="60" x2="515" y2="72" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="539" y1="52" x2="529" y2="64" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="552.5" y1="44" x2="542.5" y2="56" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="340" x2="160" y2="340" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <path d="M120,340 A80,80 0 0 0 109.5,300" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="132" y="305.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30^\circ$</div></foreignObject>
  <rect x="102.5" y="181" width="90" height="90" rx="2" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" transform="rotate(-30 147.5 226)"/>
  <line x1="131" y1="288.5" x2="209" y2="243.5" stroke="#2b8a3e" stroke-width="5" stroke-linecap="round"/>
  <line x1="147.5" y1="226" x2="147.5" y2="278" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="147.5" cy="278" r="6" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <circle cx="147.5" cy="226" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M147.5,226 V219 A7,7 0 0 1 154.5,226 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M147.5,226 V233 A7,7 0 0 1 140.5,226 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="72.5" y="120.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{stays upright}$</div></foreignObject>
  <rect x="351" y="18" width="45" height="120" rx="2" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" transform="rotate(-30 373.5 78)"/>
  <line x1="384" y1="142.5" x2="423" y2="120" stroke="#6b7480" stroke-width="5" stroke-linecap="round"/>
  <line x1="373.5" y1="78" x2="373.5" y2="147.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="373.5" cy="147.5" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <circle cx="373.5" cy="78" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M373.5,78 V71 A7,7 0 0 1 380.5,78 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M373.5,78 V85 A7,7 0 0 1 366.5,78 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M341.5,35.5 A114.0,114.0 0 0 0 292,74" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M285.5,84.5 L286.5,71 L296.5,77 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="431.5" y="33.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{topples}$</div></foreignObject>
</svg>

## Formula: Equilibrium conditions
A body is in equilibrium when both the sum of the forces and the sum of the moments of the forces are zero:
```latex
\begin{aligned}
&\Sigma\overline{F} = \overline{0} \\
&\Sigma M = 0
\end{aligned}
```
where $\Sigma\overline{F}$ is the vector sum of the forces acting on the body ($\text{N}$) and $\Sigma M$ the sum of the moments of the forces about some point ($\text{Nm}$). The first is the **equilibrium condition for translation** and the second the **moment condition**, that is, the equilibrium condition for rotation. In components the first condition is $\Sigma F_x = 0$ and $\Sigma F_y = 0$. The moments are calculated as in the chapter *Moment: the turning effect of a force*: $M = Fr$, where $r$ is the lever arm of the force, and the sign tells the direction of rotation. In this chapter an anticlockwise moment is positive.

### Choosing the reference point
A body at rest does not rotate about any point, so the moment condition holds about every point. It is worth choosing the point of application of an unknown force as the reference point for the moments: the lever arm of that force is then zero, so the force does not appear in the moment condition. If a force is not perpendicular to a rod-like body (a plank, a rod), it is resolved into components. When the reference point is on the line of the rod, the moment is given by the component perpendicular to the rod multiplied by the distance from the reference point. In the figure the force $\overline{F}$ acting on the end of the rod makes the angle $\alpha$ with the rod: the component $F\cos\alpha$ along the rod passes through the hinge and does not rotate the rod, and the perpendicular component $F\sin\alpha$ gives the moment $M = F\sin\alpha \cdot r$.

<svg data-fig="komponentit" viewBox="0 0 600 290" role="img" aria-label="Schematic figure: a horizontal rod is on a hinge on a wall. A force F acts on the outer end of the rod, pointing obliquely up towards the wall and making the angle alpha with the rod. The force is resolved with dashed arrows into a component along the rod, which passes through the hinge and does not rotate the rod, and a component F sin alpha perpendicular to the rod, which gives a moment about the hinge. The lever arm of the moment is the length of the rod r." style="max-width:100%;font-size:24px">
  <rect x="34" y="40" width="56" height="210" fill="#e3dccb" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="34" y1="64" x2="52" y2="50" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="86" x2="52" y2="72" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="108" x2="52" y2="94" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="130" x2="52" y2="116" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="152" x2="52" y2="138" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="174" x2="52" y2="160" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="196" x2="52" y2="182" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="218" x2="52" y2="204" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="34" y1="240" x2="52" y2="226" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="90" y="182" width="340" height="16" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="307" y1="104" x2="430" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="307" y1="104" x2="307" y2="190" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="430" y1="182" x2="430" y2="106" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M436.5,117 L430,104 L423.5,117" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="424" y1="176" x2="311" y2="176" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M322,169.5 L309,176 L322,182.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="430" y1="190" x2="321" y2="113.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M307,104 L326.5,107.5 L317,121 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="90" cy="190" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M364,190 A66,66 0 0 1 376,152" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="328" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="262" y="81.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="444" y="132.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F\sin\alpha$</div></foreignObject>
  <foreignObject x="326" y="215.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$F\cos\alpha$</div></foreignObject>
  <line x1="90" y1="262" x2="430" y2="262" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="255" x2="90" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="255" x2="430" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="250" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="96" y="209.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hinge}$</div></foreignObject>
</svg>

### Two supports
The plank in the figure rests on two supports. Let us take the moments about the centre of mass: the lever arm of the weight $\overline{G}$ is zero, the support force $\overline{N}_1$ rotates the plank clockwise and $\overline{N}_2$ anticlockwise. From the moment condition $N_2 r_2 - N_1 r_1 = 0$ we get
```latex
N_1 r_1 = N_2 r_2
```
where $N_1$ and $N_2$ are the support forces ($\text{N}$) and $r_1$ and $r_2$ the distances of the supports from the centre of mass ($\text{m}$). The support nearer the centre of mass thus carries the larger share of the weight. From the condition for translation the sum of the support forces is $N_1 + N_2 = G$.

<svg data-fig="lankku" viewBox="0 0 600 290" role="img" aria-label="Free-body diagram: a uniform plank on two supports, drawn as a rectangle. The weight G starts from the middle of the plank, the centre of mass, and points down. The support forces N1 and N2 point up and end at the lower surface of the plank at the supports. Support 1 is at the distance r1 from the centre of mass and support 2 at the shorter distance r2. The lengths of the arrows are to scale: N2 is longer than N1, and together they are as long as G." style="max-width:100%;font-size:24px">
  <rect x="80" y="119" width="440" height="22" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="300" y1="130" x2="300" y2="230.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,247.5 L292,229.5 L308,229.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="309.5" y="227" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="135" y1="188" x2="135" y2="158" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M135,141 L143,159 L127,159 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="112.5" y="191.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_{1}$</div></foreignObject>
  <line x1="410" y1="211.5" x2="410" y2="158" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M410,141 L418,159 L402,159 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="387.5" y="215" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_{2}$</div></foreignObject>
  <circle cx="300" cy="130" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M300,130 V123 A7,7 0 0 1 307,130 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M300,130 V137 A7,7 0 0 1 293,130 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="135" y1="115" x2="135" y2="64" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="410" y1="115" x2="410" y2="64" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="300" y1="115" x2="300" y2="64" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="135" y1="72" x2="300" y2="72" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="135" y1="65" x2="135" y2="79" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="65" x2="300" y2="79" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="201" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_1$</div></foreignObject>
  <line x1="300" y1="72" x2="410" y2="72" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="65" x2="300" y2="79" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="65" x2="410" y2="79" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="338.5" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_2$</div></foreignObject>
  <foreignObject x="435" y="77.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{plank}$</div></foreignObject>
</svg>

### Common centre of mass
For two bodies of masses $m_1$ and $m_2$, the common centre of mass is at
```latex
x_\text{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}
```
where $x_1$ and $x_2$ are the positions of the centres of mass of the bodies ($\text{m}$) on the same axis. The formula follows from the moment condition: if the bodies are supported at $x_\text{cm}$, the moments of the weights about the point of support cancel each other. A loaded plank resting on two supports topples when the common centre of mass of the plank and the load moves outside the interval between the supports.

## Worked example
Two carriers carry a uniform horizontal log of length $4.00\,\text{m}$ and mass $60.0\,\text{kg}$. Carrier A holds the front end of the log, and carrier B is $1.00\,\text{m}$ from the back end. With what force does each carrier hold the log? The carriers support the log vertically upwards.

<svg data-fig="hirsi" viewBox="0 0 600 330" role="img" aria-label="Free-body diagram: a uniform log as a rectangle. Carrier A is at the left end of the log and carrier B 1.00 m from the right end. The weight G starts from the middle of the log, downwards. The forces of the carriers NA and NB point up and end at the lower surface of the log. Distances: from A to the centre of mass 2.00 m, from the centre of mass to B 1.00 m. A is marked as the reference point and anticlockwise as the positive direction of rotation. The lengths of the arrows are to scale." style="max-width:100%;font-size:24px">
  <rect x="80" y="147" width="440" height="26" rx="6" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="300" y1="160" x2="300" y2="260.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,277.5 L292,259.5 L308,259.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="309.5" y="259" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="81" y1="212" x2="81" y2="190" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M81,173 L89,191 L73,191 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="66.5" y="215.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_\text{A}$</div></foreignObject>
  <line x1="410" y1="251.5" x2="410" y2="190" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M410,173 L418,191 L402,191 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="387.5" y="255" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_\text{B}$</div></foreignObject>
  <circle cx="300" cy="160" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M300,160 V153 A7,7 0 0 1 307,160 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M300,160 V167 A7,7 0 0 1 293,160 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="143" x2="80" y2="98" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="300" y1="143" x2="300" y2="98" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="410" y1="143" x2="410" y2="98" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="520" y1="143" x2="520" y2="98" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="80" y1="106" x2="300" y2="106" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="99" x2="80" y2="113" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="99" x2="300" y2="113" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="148.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.00\,\text{m}$</div></foreignObject>
  <line x1="300" y1="106" x2="410" y2="106" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="99" x2="300" y2="113" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="99" x2="410" y2="113" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="313.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.00\,\text{m}$</div></foreignObject>
  <line x1="410" y1="106" x2="520" y2="106" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="99" x2="410" y2="113" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="99" x2="520" y2="113" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="423.5" y="73.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.00\,\text{m}$</div></foreignObject>
  <circle cx="80" cy="160" r="5" fill="#1f2933"/>
  <foreignObject x="46" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="440" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <path d="M127,306.5 A26,26 0 1 0 89,290.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M89.5,293 L80,283.5 L91,279.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="156" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
</svg>

<!-- vaihe -->

**Given and find.** The log: $L = 4.00\,\text{m}$, $m = 60.0\,\text{kg}$, $g = 9.81\,\text{m/s}^2$. The centre of mass is in the middle, $2.00\,\text{m}$ from A; B is $3.00\,\text{m}$ from A. We are asked for the forces of the carriers, $N_\text{A}$ and $N_\text{B}$.

<!-- vaihe -->

**Principle.** The log is at rest, so it is in equilibrium for both translation and rotation. The body is the log. In the free-body diagram the forces acting on it are the weight $\overline{G}$ downwards from the centre of mass and the forces of the carriers $\overline{N}_\text{A}$ and $\overline{N}_\text{B}$ upwards. A is chosen as the reference point, so the lever arm of $N_\text{A}$ is zero, and the anticlockwise moment is positive. The unknown $N_\text{B}$ is obtained from the moment condition and $N_\text{A}$ then from the sum of the forces.

<!-- vaihe -->

**Formula solved.** The moment condition about A and the condition $\Sigma F_y = 0$, with upwards positive:
```latex
\begin{aligned}
&N_\text{B} r_\text{B} - G r_G = 0 \\
&N_\text{B} = \frac{m g r_G}{r_\text{B}} \\[6pt]
&N_\text{A} + N_\text{B} - G = 0 \\
&N_\text{A} = m g - N_\text{B}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the mass is in kilograms and the lengths in metres. The lever arms of the forces are $r_G = 2.00\,\text{m}$ and $r_\text{B} = 3.00\,\text{m}$, because the forces are vertical and the log horizontal.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&G = m g \\
&= 60.0\,\text{kg} \cdot 9.81\,\text{m/s}^2 \\
&= 588.6\,\text{N} \\[6pt]
&N_\text{B} = \frac{G r_G}{r_\text{B}} \\
&= \frac{588.6\,\text{N} \cdot 2.00\,\text{m}}{3.00\,\text{m}} \\
&= 392.4\,\text{N} \\[6pt]
&N_\text{A} = G - N_\text{B} \\
&= 588.6\,\text{N} - 392.4\,\text{N} \\
&= 196.2\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Result.** Carrier A holds the log with a force of $196\,\text{N}$ and carrier B with a force of $392\,\text{N}$. The results are given to three significant figures, like the mass $60.0\,\text{kg}$ and the lengths.

<!-- vaihe -->

**Reasonableness.** The sum of the forces is $196\,\text{N} + 392\,\text{N} = 588\,\text{N}$, the weight of the log. B is $1.00\,\text{m}$ and A $2.00\,\text{m}$ from the centre of mass, so B carries twice as much as A, as the moment condition about the centre of mass requires: $196\,\text{N} \cdot 2.00\,\text{m} = 392\,\text{N} \cdot 1.00\,\text{m}$.

## Common misconception
Many think that two supports always carry half of the weight each, or that the support farther away carries more because its "lever" is longer. The moment condition about the centre of mass shows the opposite: $N_1 r_1 = N_2 r_2$, so the support *nearer* the centre of mass carries more. Each support carries half of the weight only when the supports are at equal distances from the centre of mass.

Another mistake is to think that a loaded plank topples as soon as the load is past a support. The plank topples only when the *common* centre of mass of the plank and the load is past the support: until then the weight of the plank itself between the supports cancels the moment of the load.

A third mistake is to believe that moments must be calculated only about the centre of mass or a support. The moment condition holds about any point, and the same forces are obtained from different points. A good choice merely shortens the calculation.

## Summary
- A body is in equilibrium when the sum of the forces is zero, $\Sigma\overline{F} = \overline{0}$ (for translation), and the sum of the moments of the forces is zero, $\Sigma M = 0$ (for rotation).
- The moment condition holds about any point. It is worth choosing the point of application of an unknown force as the reference point.
- The weight acts at the centre of mass, which is in the middle of a uniform, symmetrical body. For a plank on two supports $N_1 r_1 = N_2 r_2$: the support nearer the centre of mass carries more.
- A supported body stays upright when the vertical line through the centre of mass falls within the support area; otherwise it topples.
