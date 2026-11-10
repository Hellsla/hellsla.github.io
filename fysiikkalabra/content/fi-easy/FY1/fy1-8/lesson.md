# Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi

> **Miksi** kaksi ryhmää saa samalle leluautolle eri nopeuden, vaikka kumpikin mittaa huolellisesti?

<svg data-fig="hero" data-style="house" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: luokan lattialla on rata. Leluauto kulkee radalla mittanauhan vieressä. Radan kummallakin puolella on ryhmä. Kummallakin ryhmällä on oma sekuntikello. Kellojen viisarit ovat pysähtyneet eri kohtiin." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy18h-w1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy18h-w2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy18h-floor" gradientUnits="userSpaceOnUse" x1="0" y1="300" x2="0" y2="600"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><linearGradient id="fy18h-track" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy18h-car" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="120" y="40" width="200" height="170" rx="4" fill="url(#fy18h-w1)" stroke="#3a4350" stroke-width="3"/>
  <path d="M164,119.5 Q163,106 179,107.5 Q185.5,93 201.5,98 Q216,90 224,105 Q238.5,106.5 237,119.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="220" y1="40" x2="220" y2="210" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="125" x2="320" y2="125" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="108" y="210" width="224" height="14" rx="3" fill="#c9c2b2" stroke="#6f6b62" stroke-width="3"/>
  <rect x="880" y="40" width="200" height="170" rx="4" fill="url(#fy18h-w2)" stroke="#3a4350" stroke-width="3"/>
  <path d="M924,119.5 Q923,106 939,107.5 Q945.5,93 961.5,98 Q976,90 984,105 Q998.5,106.5 997,119.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="980" y1="40" x2="980" y2="210" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="880" y1="125" x2="1080" y2="125" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="868" y="210" width="224" height="14" rx="3" fill="#c9c2b2" stroke="#6f6b62" stroke-width="3"/>
  <rect x="0" y="300" width="1200" height="300" fill="url(#fy18h-floor)"/>
  <line x1="240" y1="300" x2="-840" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="300" x2="-600" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="300" x2="-360" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="300" x2="-120" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="300" x2="120" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="300" x2="360" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="300" x2="600" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="300" x2="840" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="720" y1="300" x2="1080" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="300" x2="1320" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="840" y1="300" x2="1560" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="300" x2="1800" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="960" y1="300" x2="2040" y2="600" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="300" x2="1200" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M180,500 L1020,500 L940,400 L260,400 Z" fill="url(#fy18h-track)" stroke="#3a4350" stroke-width="3" stroke-linejoin="round"/>
  <path d="M260,400 H940" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"/>
  <line x1="300" y1="400" x2="276" y2="500" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt" stroke-dasharray="10 8"/>
  <line x1="900" y1="400" x2="876" y2="500" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt" stroke-dasharray="10 8"/>
  <rect x="170" y="504" width="860" height="30" rx="4" fill="#ffc078" stroke="#8c6a42" stroke-width="2.5"/>
  <line x1="178" y1="504" x2="178" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="188" y1="504" x2="188" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197.5" y1="504" x2="197.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="207.5" y1="504" x2="207.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="217" y1="504" x2="217" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="227" y1="504" x2="227" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="237" y1="504" x2="237" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="246.5" y1="504" x2="246.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256.5" y1="504" x2="256.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266" y1="504" x2="266" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="504" x2="276" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="286" y1="504" x2="286" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="295.5" y1="504" x2="295.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="305.5" y1="504" x2="305.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="315" y1="504" x2="315" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="325" y1="504" x2="325" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="335" y1="504" x2="335" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="344.5" y1="504" x2="344.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="354.5" y1="504" x2="354.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364" y1="504" x2="364" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="504" x2="374" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="504" x2="384" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="393.5" y1="504" x2="393.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="403.5" y1="504" x2="403.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="413" y1="504" x2="413" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="423" y1="504" x2="423" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="433" y1="504" x2="433" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="442.5" y1="504" x2="442.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="452.5" y1="504" x2="452.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="462" y1="504" x2="462" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="504" x2="472" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="482" y1="504" x2="482" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="491.5" y1="504" x2="491.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="501.5" y1="504" x2="501.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="511" y1="504" x2="511" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="521" y1="504" x2="521" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="531" y1="504" x2="531" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540.5" y1="504" x2="540.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="550.5" y1="504" x2="550.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="560" y1="504" x2="560" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="570" y1="504" x2="570" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="580" y1="504" x2="580" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="589.5" y1="504" x2="589.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="599.5" y1="504" x2="599.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="609" y1="504" x2="609" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="619" y1="504" x2="619" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="629" y1="504" x2="629" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="638.5" y1="504" x2="638.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="648.5" y1="504" x2="648.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="658" y1="504" x2="658" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="668" y1="504" x2="668" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="678" y1="504" x2="678" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="687.5" y1="504" x2="687.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="697.5" y1="504" x2="697.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="707" y1="504" x2="707" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="717" y1="504" x2="717" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="727" y1="504" x2="727" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="736.5" y1="504" x2="736.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="746.5" y1="504" x2="746.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="756" y1="504" x2="756" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="766" y1="504" x2="766" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="776" y1="504" x2="776" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="785.5" y1="504" x2="785.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="795.5" y1="504" x2="795.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="805" y1="504" x2="805" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="815" y1="504" x2="815" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="825" y1="504" x2="825" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="834.5" y1="504" x2="834.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="844.5" y1="504" x2="844.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="854" y1="504" x2="854" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="864" y1="504" x2="864" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="874" y1="504" x2="874" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="883.5" y1="504" x2="883.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="893.5" y1="504" x2="893.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="903" y1="504" x2="903" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="913" y1="504" x2="913" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="923" y1="504" x2="923" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="932.5" y1="504" x2="932.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="942.5" y1="504" x2="942.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="952" y1="504" x2="952" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="962" y1="504" x2="962" y2="522" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="972" y1="504" x2="972" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="981.5" y1="504" x2="981.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="991.5" y1="504" x2="991.5" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1001" y1="504" x2="1001" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1011" y1="504" x2="1011" y2="516" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1021" y1="504" x2="1021" y2="511" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M530,474 V444 Q538,434 566,432 L586,400 H644 L668,432 Q692,436 694,452 V474 Z" fill="url(#fy18h-car)" stroke="#3a4350" stroke-width="3" stroke-linejoin="round"/>
  <path d="M594,408 H640 L656,430 H580 Z" fill="#eef5f9" stroke="#3a4350" stroke-width="2" stroke-linejoin="round"/>
  <line x1="618" y1="408" x2="618" y2="430" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="680" y="444" width="12" height="8" rx="2" fill="#ffc078" stroke="#8c6a42" stroke-width="1.5"/>
  <circle cx="564" cy="476" r="18" fill="#1f2933"/>
  <circle cx="564" cy="476" r="8" fill="#c4ccd4"/>
  <circle cx="660" cy="476" r="18" fill="#1f2933"/>
  <circle cx="660" cy="476" r="8" fill="#c4ccd4"/>
  <line x1="460" y1="446" x2="500" y2="446" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="480" y1="464" x2="520" y2="464" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="450" y1="480" x2="490" y2="480" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <circle cx="102" cy="316" r="7.30125" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <circle cx="101" cy="382" r="5.35425" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <path d="M95,316 L96,382 L106.5,382.5 L109.5,316 Z" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="102" cy="316" r="6.55125" fill="#3f4c5a"/>
  <circle cx="101" cy="382" r="4.60425" fill="#3f4c5a"/>
  <path d="M92.5,388 q0,-9 9,-9 q9,0 9,9 v3 h-17.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M92.5,391 h17.5" fill="none" stroke="#f1f3f5" stroke-width="2.43375" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="118" cy="316" r="7.30125" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <circle cx="119" cy="382" r="5.35425" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <path d="M110.5,316 L113.5,382.5 L124,382 L125,316 Z" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="118" cy="316" r="6.55125" fill="#3f4c5a"/>
  <circle cx="119" cy="382" r="4.60425" fill="#3f4c5a"/>
  <path d="M110,388 q0,-9 9,-9 q9,0 9,9 v3 h-17.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M110,391 h17.5" fill="none" stroke="#f1f3f5" stroke-width="2.43375" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M95.5,257.5 Q110,248 124.5,257.5 L119.5,267.5 H100.5 Z" fill="#267937" stroke="#1c5a28" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M88.5,275 Q88.5,263.5 100.5,263.5 H119.5 Q131.5,263.5 131.5,275 L128.5,320 H91.5 Z" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M91.5,314 H128.5" fill="none" stroke="#1c5a28" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M99.5,312 L102,296.5 H118 L120.5,312" fill="none" stroke="#1c5a28" stroke-width="1.25" stroke-linejoin="round"/>
  <line x1="106" y1="265.5" x2="105" y2="281" stroke="#ffffff" stroke-width="1.5576" stroke-linecap="round"/>
  <line x1="114" y1="265.5" x2="115" y2="281" stroke="#ffffff" stroke-width="1.5576" stroke-linecap="round"/>
  <circle cx="91.5" cy="273" r="5.841" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <circle cx="87.5" cy="294.5" r="4.8675" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <path d="M86,272 L83,293.5 L92.5,295.5 L97.5,274 Z" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="91.5" cy="273" r="5.091" fill="#2b8a3e"/>
  <circle cx="87.5" cy="294.5" r="4.1175" fill="#2b8a3e"/>
  <circle cx="87.5" cy="294.5" r="4.8675" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <circle cx="88.5" cy="316" r="4.38075" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <path d="M82.5,295 L84,316 L93,316 L92.5,294.5 Z" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="87.5" cy="294.5" r="4.1175" fill="#2b8a3e"/>
  <circle cx="88.5" cy="316" r="3.63075" fill="#2b8a3e"/>
  <circle cx="88.5" cy="320" r="5.35425" fill="#c99a72" stroke="#83644a" stroke-width="1.25"/>
  <circle cx="128.5" cy="273" r="5.841" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <circle cx="132.5" cy="294.5" r="4.8675" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <path d="M122.5,274 L127.5,295.5 L137,293.5 L134,272 Z" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="128.5" cy="273" r="5.091" fill="#2b8a3e"/>
  <circle cx="132.5" cy="294.5" r="4.1175" fill="#2b8a3e"/>
  <circle cx="132.5" cy="294.5" r="4.8675" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <circle cx="131.5" cy="316" r="4.38075" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25"/>
  <path d="M127.5,294.5 L127,316 L136,316 L137.5,295 Z" fill="#2b8a3e" stroke="#1c5a28" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="132.5" cy="294.5" r="4.1175" fill="#2b8a3e"/>
  <circle cx="131.5" cy="316" r="3.63075" fill="#2b8a3e"/>
  <circle cx="131.5" cy="320" r="5.35425" fill="#c99a72" stroke="#83644a" stroke-width="1.25"/>
  <rect x="105" y="253.5" width="9.5" height="11.5" fill="#b98e69"/>
  <ellipse cx="97.5" cy="244" rx="3" ry="4" fill="#c99a72" stroke="#83644a" stroke-width="1.25"/>
  <ellipse cx="122.5" cy="244" rx="3" ry="4" fill="#c99a72" stroke="#83644a" stroke-width="1.25"/>
  <path d="M119.5,234 q13.5,2 11.5,21.5 q-6,-6 -9.5,-13.5 Z" fill="#7a4b2a" stroke="#55341d" stroke-width="1.25" stroke-linejoin="round"/>
  <ellipse cx="110" cy="242" rx="12.5" ry="14.5" fill="#c99a72" stroke="#83644a" stroke-width="1.25"/>
  <path d="M96.5,244 Q95.5,224.5 110,225.5 Q124.5,224.5 123.5,244 Q119.5,234 112,234 Q102,233.5 96.5,244 Z" fill="#7a4b2a" stroke="#55341d" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="105" cy="243" r="1.46025" fill="#2b3138"/>
  <line x1="107" y1="239" x2="102" y2="238.5" stroke="#623c22" stroke-width="1.26555" stroke-linecap="round"/>
  <circle cx="105" cy="243" r="3.894" fill="none" stroke="#3a4350" stroke-width="1.3"/>
  <circle cx="115" cy="243" r="1.46025" fill="#2b3138"/>
  <line x1="113" y1="239" x2="118" y2="238.5" stroke="#623c22" stroke-width="1.26555" stroke-linecap="round"/>
  <circle cx="115" cy="243" r="3.894" fill="none" stroke="#3a4350" stroke-width="1.3"/>
  <line x1="109" y1="243" x2="111" y2="243" stroke="#3a4350" stroke-width="1.3" stroke-linecap="butt"/>
  <path d="M106,249 q4,3 8,0" fill="none" stroke="#83644a" stroke-width="1.3629" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="181.5" cy="317.5" r="7.74375" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <circle cx="180.5" cy="387.5" r="5.67875" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <path d="M174,317.5 L175,387.5 L186.5,388 L189.5,317.5 Z" fill="#364a63" stroke="#233040" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="181.5" cy="317.5" r="6.99375" fill="#364a63"/>
  <circle cx="180.5" cy="387.5" r="4.92875" fill="#364a63"/>
  <path d="M171.5,394 q0,-9 9.5,-9 q9.5,0 9.5,9 v3 h-18.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M171.5,397 h18.5" fill="none" stroke="#f1f3f5" stroke-width="2.58125" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="198.5" cy="317.5" r="7.74375" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <circle cx="199.5" cy="387.5" r="5.67875" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <path d="M190.5,317.5 L193.5,388 L205,387.5 L206,317.5 Z" fill="#364a63" stroke="#233040" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="198.5" cy="317.5" r="6.99375" fill="#364a63"/>
  <circle cx="199.5" cy="387.5" r="4.92875" fill="#364a63"/>
  <path d="M190,394 q0,-9 9.5,-9 q9.5,0 9.5,9 v3 h-18.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M190,397 h18.5" fill="none" stroke="#f1f3f5" stroke-width="2.58125" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M174.5,255.5 Q190,245.5 205.5,255.5 L200.5,266 H179.5 Z" fill="#1663ab" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M167.5,274 Q167.5,262 179.5,262 H200.5 Q212.5,262 212.5,274 L209.5,321.5 H170.5 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M170.5,315.5 H209.5" fill="none" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M178.5,313.5 L181.5,297 H198.5 L201.5,313.5" fill="none" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <line x1="186" y1="264" x2="185" y2="280.5" stroke="#ffffff" stroke-width="1.652" stroke-linecap="round"/>
  <line x1="194" y1="264" x2="195" y2="280.5" stroke="#ffffff" stroke-width="1.652" stroke-linecap="round"/>
  <circle cx="170.5" cy="272" r="6.195" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="166.5" cy="295" r="5.1625" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M164.5,271 L161,294 L171.5,295.5 L176.5,273 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="170.5" cy="272" r="5.445" fill="#1971c2"/>
  <circle cx="166.5" cy="295" r="4.4125" fill="#1971c2"/>
  <circle cx="166.5" cy="295" r="5.1625" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="167.5" cy="317.5" r="4.64625" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M161,295 L162.5,317.5 L172,317.5 L171.5,294.5 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="166.5" cy="295" r="4.4125" fill="#1971c2"/>
  <circle cx="167.5" cy="317.5" r="3.89625" fill="#1971c2"/>
  <circle cx="167.5" cy="321.5" r="5.67875" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <circle cx="209.5" cy="272" r="6.195" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="238.5" cy="281.5" r="5.1625" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M207.5,278 L237,286.5 L240,276.5 L211.5,266 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="209.5" cy="272" r="5.445" fill="#1971c2"/>
  <circle cx="238.5" cy="281.5" r="4.4125" fill="#1971c2"/>
  <circle cx="238.5" cy="281.5" r="5.1625" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="260" cy="270" r="4.64625" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M241,286 L262,274 L258,266 L236,277 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="238.5" cy="281.5" r="4.4125" fill="#1971c2"/>
  <circle cx="260" cy="270" r="3.89625" fill="#1971c2"/>
  <circle cx="260" cy="270" r="5.67875" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <rect x="185" y="251.5" width="10.5" height="12.5" fill="#dec2a5"/>
  <ellipse cx="176.5" cy="241" rx="3" ry="4" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <ellipse cx="203.5" cy="241" rx="3" ry="4" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <ellipse cx="190" cy="239" rx="13.5" ry="15.5" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <path d="M175.5,241 Q174.5,220.5 190,221.5 Q205.5,220.5 204.5,241 Q200.5,231 192,231 Q181.5,230 175.5,241 Z" fill="#2b3138" stroke="#1e2227" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="185" cy="240" r="1.54875" fill="#2b3138"/>
  <line x1="187" y1="236" x2="181.5" y2="235.5" stroke="#22272d" stroke-width="1.34225" stroke-linecap="round"/>
  <circle cx="195" cy="240" r="1.54875" fill="#2b3138"/>
  <line x1="193" y1="236" x2="198.5" y2="235.5" stroke="#22272d" stroke-width="1.34225" stroke-linecap="round"/>
  <path d="M186,246.5 q4,3 8.5,0" fill="none" stroke="#9d8974" stroke-width="1.4455" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="253" y="164" width="14" height="10.5" rx="3" fill="#6c757d" stroke="#43494e" stroke-width="2"/>
  <rect x="257" y="173.5" width="6" height="6" fill="#6c757d"/>
  <circle cx="260" cy="222" r="44" fill="#c4ccd4" stroke="#6c7075" stroke-width="3"/>
  <circle cx="260" cy="222" r="36.08" fill="#ffffff" stroke="#3a4350" stroke-width="2"/>
  <line x1="260" y1="192" x2="260" y2="187.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275" y1="196" x2="277" y2="192.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="207" x2="289.5" y2="205" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="290" y1="222" x2="294.5" y2="222" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="237" x2="289.5" y2="239" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275" y1="248" x2="277" y2="251.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="260" y1="252" x2="260" y2="256.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="245" y1="248" x2="243" y2="251.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="234" y1="237" x2="230.5" y2="239" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230" y1="222" x2="225.5" y2="222" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="234" y1="207" x2="230.5" y2="205" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="245" y1="196" x2="243" y2="192.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="260" y1="222" x2="289" y2="225.5" stroke="#c92a2a" stroke-width="3.08" stroke-linecap="round"/>
  <circle cx="260" cy="222" r="3.52" fill="#1f2933"/>
  <circle cx="1082" cy="316" r="7.30125" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <circle cx="1081" cy="382" r="5.35425" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <path d="M1075,316 L1076,382 L1086.5,382.5 L1089.5,316 Z" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1082" cy="316" r="6.55125" fill="#3f4c5a"/>
  <circle cx="1081" cy="382" r="4.60425" fill="#3f4c5a"/>
  <path d="M1072.5,388 q0,-9 9,-9 q9,0 9,9 v3 h-17.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M1072.5,391 h17.5" fill="none" stroke="#f1f3f5" stroke-width="2.43375" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1098" cy="316" r="7.30125" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <circle cx="1099" cy="382" r="5.35425" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25"/>
  <path d="M1090.5,316 L1093.5,382.5 L1104,382 L1105,316 Z" fill="#3f4c5a" stroke="#29313a" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1098" cy="316" r="6.55125" fill="#3f4c5a"/>
  <circle cx="1099" cy="382" r="4.60425" fill="#3f4c5a"/>
  <path d="M1090,388 q0,-9 9,-9 q9,0 9,9 v3 h-17.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M1090,391 h17.5" fill="none" stroke="#f1f3f5" stroke-width="2.43375" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1075.5,257.5 Q1090,248 1104.5,257.5 L1099.5,267.5 H1080.5 Z" fill="#1663ab" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M1068.5,275 Q1068.5,263.5 1080.5,263.5 H1099.5 Q1111.5,263.5 1111.5,275 L1108.5,320 H1071.5 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M1071.5,314 H1108.5" fill="none" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M1079.5,312 L1082,296.5 H1098 L1100.5,312" fill="none" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <line x1="1086" y1="265.5" x2="1085" y2="281" stroke="#ffffff" stroke-width="1.5576" stroke-linecap="round"/>
  <line x1="1094" y1="265.5" x2="1095" y2="281" stroke="#ffffff" stroke-width="1.5576" stroke-linecap="round"/>
  <circle cx="1071.5" cy="273" r="5.841" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="1067.5" cy="294.5" r="4.8675" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M1066,272 L1063,293.5 L1072.5,295.5 L1077.5,274 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1071.5" cy="273" r="5.091" fill="#1971c2"/>
  <circle cx="1067.5" cy="294.5" r="4.1175" fill="#1971c2"/>
  <circle cx="1067.5" cy="294.5" r="4.8675" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="1068.5" cy="316" r="4.38075" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M1062.5,295 L1064,316 L1073,316 L1072.5,294.5 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1067.5" cy="294.5" r="4.1175" fill="#1971c2"/>
  <circle cx="1068.5" cy="316" r="3.63075" fill="#1971c2"/>
  <circle cx="1068.5" cy="320" r="5.35425" fill="#8d5b3c" stroke="#5c3b27" stroke-width="1.25"/>
  <circle cx="1108.5" cy="273" r="5.841" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="1112.5" cy="294.5" r="4.8675" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M1102.5,274 L1107.5,295.5 L1117,293.5 L1114,272 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1108.5" cy="273" r="5.091" fill="#1971c2"/>
  <circle cx="1112.5" cy="294.5" r="4.1175" fill="#1971c2"/>
  <circle cx="1112.5" cy="294.5" r="4.8675" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <circle cx="1111.5" cy="316" r="4.38075" fill="#1971c2" stroke="#10497e" stroke-width="1.25"/>
  <path d="M1107.5,294.5 L1107,316 L1116,316 L1117.5,295 Z" fill="#1971c2" stroke="#10497e" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1112.5" cy="294.5" r="4.1175" fill="#1971c2"/>
  <circle cx="1111.5" cy="316" r="3.63075" fill="#1971c2"/>
  <circle cx="1111.5" cy="320" r="5.35425" fill="#8d5b3c" stroke="#5c3b27" stroke-width="1.25"/>
  <rect x="1085" y="253.5" width="9.5" height="11.5" fill="#825437"/>
  <ellipse cx="1077.5" cy="244" rx="3" ry="4" fill="#8d5b3c" stroke="#5c3b27" stroke-width="1.25"/>
  <ellipse cx="1102.5" cy="244" rx="3" ry="4" fill="#8d5b3c" stroke="#5c3b27" stroke-width="1.25"/>
  <ellipse cx="1090" cy="242" rx="12.5" ry="14.5" fill="#8d5b3c" stroke="#5c3b27" stroke-width="1.25"/>
  <path d="M1076.5,244 Q1075.5,224.5 1090,225.5 Q1104.5,224.5 1103.5,244 Q1099.5,234 1092,234 Q1082,233.5 1076.5,244 Z" fill="#2b3138" stroke="#1e2227" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1085" cy="243" r="1.46025" fill="#2b3138"/>
  <line x1="1087" y1="239" x2="1082" y2="238.5" stroke="#22272d" stroke-width="1.26555" stroke-linecap="round"/>
  <circle cx="1095" cy="243" r="1.46025" fill="#2b3138"/>
  <line x1="1093" y1="239" x2="1098" y2="238.5" stroke="#22272d" stroke-width="1.26555" stroke-linecap="round"/>
  <path d="M1086,249 q4,3 8,0" fill="none" stroke="#5c3b27" stroke-width="1.3629" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1001.5" cy="317.5" r="7.74375" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <circle cx="1000.5" cy="387.5" r="5.67875" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <path d="M994,317.5 L995,387.5 L1006.5,388 L1009.5,317.5 Z" fill="#364a63" stroke="#233040" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1001.5" cy="317.5" r="6.99375" fill="#364a63"/>
  <circle cx="1000.5" cy="387.5" r="4.92875" fill="#364a63"/>
  <path d="M991.5,394 q0,-9 9.5,-9 q9.5,0 9.5,9 v3 h-18.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M991.5,397 h18.5" fill="none" stroke="#f1f3f5" stroke-width="2.58125" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1018.5" cy="317.5" r="7.74375" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <circle cx="1019.5" cy="387.5" r="5.67875" fill="#364a63" stroke="#233040" stroke-width="1.25"/>
  <path d="M1010.5,317.5 L1013.5,388 L1025,387.5 L1026,317.5 Z" fill="#364a63" stroke="#233040" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1018.5" cy="317.5" r="6.99375" fill="#364a63"/>
  <circle cx="1019.5" cy="387.5" r="4.92875" fill="#364a63"/>
  <path d="M1010,394 q0,-9 9.5,-9 q9.5,0 9.5,9 v3 h-18.5 Z" fill="#364152" stroke="#202731" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M1010,397 h18.5" fill="none" stroke="#f1f3f5" stroke-width="2.58125" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M994.5,255.5 Q1010,245.5 1025.5,255.5 L1020.5,266 H999.5 Z" fill="#cc4e0b" stroke="#973a08" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M987.5,274 Q987.5,262 999.5,262 H1020.5 Q1032.5,262 1032.5,274 L1029.5,321.5 H990.5 Z" fill="#e8590c" stroke="#973a08" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M990.5,315.5 H1029.5" fill="none" stroke="#973a08" stroke-width="1.25" stroke-linejoin="round"/>
  <path d="M998.5,313.5 L1001.5,297 H1018.5 L1021.5,313.5" fill="none" stroke="#973a08" stroke-width="1.25" stroke-linejoin="round"/>
  <line x1="1006" y1="264" x2="1005" y2="280.5" stroke="#ffffff" stroke-width="1.652" stroke-linecap="round"/>
  <line x1="1014" y1="264" x2="1015" y2="280.5" stroke="#ffffff" stroke-width="1.652" stroke-linecap="round"/>
  <circle cx="990.5" cy="272" r="6.195" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <circle cx="961.5" cy="281.5" r="5.1625" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <path d="M988.5,266 L960,276.5 L963,286.5 L992.5,278 Z" fill="#e8590c" stroke="#973a08" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="990.5" cy="272" r="5.445" fill="#e8590c"/>
  <circle cx="961.5" cy="281.5" r="4.4125" fill="#e8590c"/>
  <circle cx="961.5" cy="281.5" r="5.1625" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <circle cx="940" cy="270" r="4.64625" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <path d="M964,277 L942,266 L938,274 L959,286 Z" fill="#e8590c" stroke="#973a08" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="961.5" cy="281.5" r="4.4125" fill="#e8590c"/>
  <circle cx="940" cy="270" r="3.89625" fill="#e8590c"/>
  <circle cx="940" cy="270" r="5.67875" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <circle cx="1029.5" cy="272" r="6.195" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <circle cx="1033.5" cy="295" r="5.1625" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <path d="M1023.5,273 L1028.5,295.5 L1039,294 L1035.5,271 Z" fill="#e8590c" stroke="#973a08" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1029.5" cy="272" r="5.445" fill="#e8590c"/>
  <circle cx="1033.5" cy="295" r="4.4125" fill="#e8590c"/>
  <circle cx="1033.5" cy="295" r="5.1625" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <circle cx="1032.5" cy="317.5" r="4.64625" fill="#e8590c" stroke="#973a08" stroke-width="1.25"/>
  <path d="M1028.5,294.5 L1028,317.5 L1037.5,317.5 L1039,295 Z" fill="#e8590c" stroke="#973a08" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1033.5" cy="295" r="4.4125" fill="#e8590c"/>
  <circle cx="1032.5" cy="317.5" r="3.89625" fill="#e8590c"/>
  <circle cx="1032.5" cy="321.5" r="5.67875" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <rect x="1005" y="251.5" width="10.5" height="12.5" fill="#dec2a5"/>
  <ellipse cx="996.5" cy="241" rx="3" ry="4" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <ellipse cx="1023.5" cy="241" rx="3" ry="4" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <path d="M1020.5,231 q14.5,2 12.5,22.5 q-6,-6 -10.5,-14.5 Z" fill="#c08a3e" stroke="#86612b" stroke-width="1.25" stroke-linejoin="round"/>
  <ellipse cx="1010" cy="239" rx="13.5" ry="15.5" fill="#f1d3b3" stroke="#9d8974" stroke-width="1.25"/>
  <path d="M995.5,241 Q994.5,220.5 1010,221.5 Q1025.5,220.5 1024.5,241 Q1020.5,231 1012,231 Q1001.5,230 995.5,241 Z" fill="#c08a3e" stroke="#86612b" stroke-width="1.25" stroke-linejoin="round"/>
  <circle cx="1005" cy="240" r="1.54875" fill="#2b3138"/>
  <line x1="1007" y1="236" x2="1001.5" y2="235.5" stroke="#9a6e32" stroke-width="1.34225" stroke-linecap="round"/>
  <circle cx="1015" cy="240" r="1.54875" fill="#2b3138"/>
  <line x1="1013" y1="236" x2="1018.5" y2="235.5" stroke="#9a6e32" stroke-width="1.34225" stroke-linecap="round"/>
  <path d="M1006,246.5 q4,3 8.5,0" fill="none" stroke="#9d8974" stroke-width="1.4455" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="933" y="164" width="14" height="10.5" rx="3" fill="#6c757d" stroke="#43494e" stroke-width="2"/>
  <rect x="937" y="173.5" width="6" height="6" fill="#6c757d"/>
  <circle cx="940" cy="222" r="44" fill="#c4ccd4" stroke="#6c7075" stroke-width="3"/>
  <circle cx="940" cy="222" r="36.08" fill="#ffffff" stroke="#3a4350" stroke-width="2"/>
  <line x1="940" y1="192" x2="940" y2="187.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="955" y1="196" x2="957" y2="192.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="966" y1="207" x2="969.5" y2="205" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="970" y1="222" x2="974.5" y2="222" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="966" y1="237" x2="969.5" y2="239" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="955" y1="248" x2="957" y2="251.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="940" y1="252" x2="940" y2="256.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="925" y1="248" x2="923" y2="251.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="914" y1="237" x2="910.5" y2="239" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="910" y1="222" x2="905.5" y2="222" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="914" y1="207" x2="910.5" y2="205" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="925" y1="196" x2="923" y2="192.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="940" y1="222" x2="964.5" y2="237.5" stroke="#c92a2a" stroke-width="3.08" stroke-linecap="round"/>
  <circle cx="940" cy="222" r="3.52" fill="#1f2933"/>
</svg>

## Ydinajatus
Fysiikka on kokeellinen tiede. Fysiikan väitteitä arvioidaan havaintojen ja mittausten avulla. Hyvässä tutkimuksessa menetelmät kerrotaan tarkasti. Silloin muut voivat tarkistaa tulokset ja usein myös toistaa mittaukset. **Tutkimus** on järjestelmällinen tapa vastata kysymykseen mittaamalla. Tutkimus alkaa kysymyksestä. Se päättyy johtopäätökseen, jonka mittaustulokset perustelevat. Hyvä tutkimus ei ole sellainen, jossa oletus osoittautuu oikeaksi. Hyvässä tutkimuksessa mittaus voisi näyttää oletuksen vääräksi.

<figure class="unit-photo"><img src="pics/fy1/ligo-scientists-laser-room.webp" alt="Kaksi suojapukuista tutkijaa katsoo laitetta valkoisessa huoneessa."><figcaption>Tutkijat tutkivat LIGO-laitoksen laserlaitetta puhtaassa huoneessa Yhdysvalloissa vuonna 2019.</figcaption></figure>

### Tutkimuskysymys ja hypoteesi
Tutkimuskysymys on kysymys, johon mittaus voi vastata. Esimerkki on "Miten leluauton kulkuaika riippuu ajomatkan pituudesta?" Kysymys "Mikä auto on paras?" ei kelpaa, koska sitä ei voi mitata.

**Hypoteesi** on perusteltu ja testattava ennuste, joka vastaa tutkimuskysymykseen. Esimerkiksi: "Auto liikkuu radalla vakionopeudella. Siksi sen kulkema matka on suoraan verrannollinen aikaan, $s = vt$." Hypoteesista pitää seurata jotain mitattavaa. Sen pitää myös voida osoittautua vääräksi. Ennuste "auto kulkee jotenkin" ei ole hypoteesi, koska mikään mittaus ei voi kumota sitä eli osoittaa sitä vääräksi.

### Muuttujat
**Muuttuja** on suure tai muu asia, joka voi vaihdella tutkimuksessa. Kokeessa tehdään kolme asiaa. Yhtä muuttujaa muutetaan, toista mitataan ja kaikki muut pidetään samoina:

- **muutettava muuttuja**: kokeen tekijä valitsee sen arvot, tässä matka $s$
- **mitattava muuttuja**: sen arvo luetaan mittarista, tässä aika $t$
- **vakioitavat muuttujat**: ne pysyvät samoina koko kokeen ajan, tässä auto, paristot, alusta ja lähtötapa.

Joskus kaksi muuttujaa muuttuu yhtä aikaa, esimerkiksi matka ja paristot. Silloin ei voi päätellä, mikä muutti tulosta. Siksi koe on reilu vasta, kun vain muutettava muuttuja vaihtuu.

<svg data-fig="setup" data-style="house" viewBox="0 0 600 414" role="img" aria-label="Kaavakuva kokeen asetelmasta. Leluauto toimii paristoilla. Se ajaa pöydällä lähtöviivalta maaliviivalle. Maalissa on ruutulippu. Pöydän reunassa on mittanauha, jonka asteikko on metreinä. Lähtöviivan ja maaliviivan väli on muutettava muuttuja, matka s. Sekuntikello mittaa aikaa t. Aika on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä." style="max-width:100%;font-size:24px">
  <foreignObject x="24" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{muutettava: } s$</div></foreignObject>
  <foreignObject x="24" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mitattava: } t$</div></foreignObject>
  <foreignObject x="24" y="81.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vakiona: auto, alusta, paristot}$</div></foreignObject>
  <rect x="412" y="88" width="28" height="15" rx="3" fill="#2b3138" stroke="#1b1e23" stroke-width="1"/>
  <rect x="430" y="88" width="10" height="15" rx="2" fill="#fab005" stroke="#966a03" stroke-width="1"/>
  <rect x="440" y="92" width="3" height="7" rx="1" fill="#adb5bd"/>
  <rect x="446" y="88" width="28" height="15" rx="3" fill="#2b3138" stroke="#1b1e23" stroke-width="1"/>
  <rect x="464" y="88" width="10" height="15" rx="2" fill="#fab005" stroke="#966a03" stroke-width="1"/>
  <rect x="474" y="92" width="3" height="7" rx="1" fill="#adb5bd"/>
  <rect x="531" y="32.5" width="9.5" height="7" rx="3" fill="#6c757d" stroke="#43494e" stroke-width="1.75"/>
  <rect x="534" y="39" width="4" height="4" fill="#6c757d"/>
  <circle cx="536" cy="72" r="30" fill="#c4ccd4" stroke="#6c7075" stroke-width="1.75"/>
  <circle cx="536" cy="72" r="24.6" fill="#ffffff" stroke="#3a4350" stroke-width="1.75"/>
  <line x1="536" y1="51.5" x2="536" y2="48.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="54.5" x2="547.5" y2="51.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="553.5" y1="62" x2="556.5" y2="60.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="556.5" y1="72" x2="559.5" y2="72" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="553.5" y1="82" x2="556.5" y2="83.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="546" y1="89.5" x2="547.5" y2="92.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="536" y1="92.5" x2="536" y2="95.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="526" y1="89.5" x2="524.5" y2="92.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="518.5" y1="82" x2="515.5" y2="83.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="515.5" y1="72" x2="512.5" y2="72" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="518.5" y1="62" x2="515.5" y2="60.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="526" y1="54.5" x2="524.5" y2="51.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="536" y1="72" x2="549.5" y2="57.5" stroke="#c92a2a" stroke-width="2.1" stroke-linecap="round"/>
  <circle cx="536" cy="72" r="2.4" fill="#1f2933"/>
  <foreignObject x="526" y="117.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t$</div></foreignObject>
  <rect x="38" y="270" width="16" height="120" fill="#ab7d4c" stroke="#6f5132" stroke-width="1.75"/>
  <rect x="556" y="270" width="16" height="120" fill="#ab7d4c" stroke="#6f5132" stroke-width="1.75"/>
  <rect x="30" y="240" width="540" height="30" rx="3" fill="#c9935a" stroke="#6f5132" stroke-width="1.75"/>
  <rect x="30" y="240" width="540" height="5" fill="#d9b38c"/>
  <rect x="44" y="250" width="512" height="15" rx="2" fill="#ffe066" stroke="#8c7b38" stroke-width="1"/>
  <line x1="72" y1="250" x2="72" y2="265" stroke="#3a4350" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="87" y1="250" x2="87" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="102" y1="250" x2="102" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="117" y1="250" x2="117" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="132" y1="250" x2="132" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="147" y1="250" x2="147" y2="265" stroke="#3a4350" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="162" y1="250" x2="162" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="177" y1="250" x2="177" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="192" y1="250" x2="192" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="207" y1="250" x2="207" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="222" y1="250" x2="222" y2="265" stroke="#3a4350" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="237" y1="250" x2="237" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="252" y1="250" x2="252" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="267" y1="250" x2="267" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="282" y1="250" x2="282" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="297" y1="250" x2="297" y2="265" stroke="#3a4350" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="312" y1="250" x2="312" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="327" y1="250" x2="327" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="342" y1="250" x2="342" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="357" y1="250" x2="357" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="372" y1="250" x2="372" y2="265" stroke="#3a4350" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="387" y1="250" x2="387" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="402" y1="250" x2="402" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="417" y1="250" x2="417" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="432" y1="250" x2="432" y2="257" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <line x1="447" y1="250" x2="447" y2="265" stroke="#3a4350" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="62" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="124.5" y="277.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <foreignObject x="212" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="274.5" y="277.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <foreignObject x="362" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="424.5" y="277.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <foreignObject x="475" y="277.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <rect x="69" y="237" width="6" height="6" rx="1" fill="#1971c2"/>
  <rect x="369" y="237" width="6" height="6" rx="1" fill="#1971c2"/>
  <line x1="372" y1="238" x2="372" y2="180" stroke="#5c6670" stroke-width="2.5" stroke-linecap="round"/>
  <rect x="373" y="180" width="8" height="8" fill="#ffffff"/>
  <rect x="373" y="188" width="8" height="8" fill="#2b3138"/>
  <rect x="381" y="180" width="8" height="8" fill="#2b3138"/>
  <rect x="381" y="188" width="8" height="8" fill="#ffffff"/>
  <rect x="389" y="180" width="8" height="8" fill="#ffffff"/>
  <rect x="389" y="188" width="8" height="8" fill="#2b3138"/>
  <rect x="397" y="180" width="8" height="8" fill="#2b3138"/>
  <rect x="397" y="188" width="8" height="8" fill="#ffffff"/>
  <rect x="373" y="180" width="32" height="16" fill="none" stroke="#2b3138" stroke-width="1"/>
  <foreignObject x="41" y="123.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lähtö}$</div></foreignObject>
  <foreignObject x="341" y="145.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maali}$</div></foreignObject>
  <line x1="102" y1="192" x2="94" y2="164" stroke="#3a4350" stroke-width="2" stroke-linecap="round"/>
  <circle cx="94" cy="162" r="3.5" fill="#ffd43b" stroke="#3a4350" stroke-width="1"/>
  <path d="M110,198 Q114,174 136,174 H146 Q164,174 170,198 Z" fill="#d0ebff" stroke="#3a4350" stroke-width="1.75" stroke-linejoin="round"/>
  <line x1="140" y1="175" x2="140" y2="198" stroke="#3a4350" stroke-width="1" stroke-linecap="butt"/>
  <path d="M126,180 q6,-3 12,-2" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M80,222 V204 Q80,196 90,196 H178 Q192,198 194,212 V222 Q194,226 188,226 H86 Q80,226 80,222 Z" fill="#e03131" stroke="#861d1d" stroke-width="1.75" stroke-linejoin="round"/>
  <path d="M86,210 H188" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="137" cy="216" r="7" fill="#ffffff" stroke="#861d1d" stroke-width="1.25"/>
  <circle cx="137" cy="216" r="3" fill="#e03131"/>
  <path d="M188,202 h6 v7 h-8 Z" fill="#ffd43b" stroke="#997f23" stroke-width="1" stroke-linejoin="round"/>
  <rect x="77" y="216" width="6" height="9" rx="2" fill="#5c6670"/>
  <rect x="191" y="218" width="6" height="8" rx="2" fill="#5c6670"/>
  <circle cx="104" cy="224" r="14" fill="#2b3138"/>
  <circle cx="104" cy="224" r="7" fill="#e9ecef" stroke="#868e96" stroke-width="1"/>
  <circle cx="107" cy="227" r="1.2" fill="#868e96"/>
  <circle cx="101" cy="227" r="1.2" fill="#868e96"/>
  <circle cx="101" cy="221" r="1.2" fill="#868e96"/>
  <circle cx="107" cy="221" r="1.2" fill="#868e96"/>
  <circle cx="170" cy="224" r="14" fill="#2b3138"/>
  <circle cx="170" cy="224" r="7" fill="#e9ecef" stroke="#868e96" stroke-width="1"/>
  <circle cx="173" cy="227" r="1.2" fill="#868e96"/>
  <circle cx="167" cy="227" r="1.2" fill="#868e96"/>
  <circle cx="167" cy="221" r="1.2" fill="#868e96"/>
  <circle cx="173" cy="221" r="1.2" fill="#868e96"/>
  <line x1="204" y1="194" x2="258" y2="194" stroke="#1971c2" stroke-width="3.25" stroke-linecap="butt"/>
  <path d="M270,194 L253.5,201.5 L258,194 L253.5,186.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="284" y="179.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <line x1="72" y1="332" x2="372" y2="332" stroke="#6b7480" stroke-width="1.25"/>
  <line x1="72" y1="326" x2="72" y2="338" stroke="#6b7480" stroke-width="1.25"/>
  <line x1="372" y1="326" x2="372" y2="338" stroke="#6b7480" stroke-width="1.25"/>
  <foreignObject x="168" y="337.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$s = 2{,}00\,\text{m}$</div></foreignObject>
</svg>

### Suunnittelu ennen mittausta
Ennen suunnittelua hankitaan taustatietoa ilmiöstä ja menetelmistä. Lähdettä arvioidaan lähdekriittisesti: kuka tiedon on tuottanut ja miksi, miten se perustellaan, onko se ajantasaista ja tukevatko muut lähteet sitä.

Suunnitelma vastaa ennen mittausta näihin kysymyksiin:

- Mitä mitataan ja millä välineellä?
- Mitkä arvot muutettavalle muuttujalle valitaan, ja kuinka monta?
- Montako toistoa kustakin arvosta tehdään?
- Mitä pidetään vakiona?

Kokeile suunnitelmaa ensin esikokeella. Esikoe kertoo, onko mittaus ylipäätään mahdollinen. Se antaa myös karkean arvion tuloksesta.

Valitse mittausalue niin, että mitattava suure on selvästi suurempi kuin mittauksen epävarmuus (ks. kohta *Suhteellinen epävarmuus ja mittausalueen valinta*). Valitse useita arvoja ja pidä niiden välit yhtä suurina. Yksi tai kaksi pistettä ei näytä, onko riippuvuus suora.

### Mittauspöytäkirja
**Mittauspöytäkirja** on kirjaus, joka tehdään kokeen aikana. Sitä ei tehdä muistista jälkikäteen. Siihen kirjataan nämä asiat:

- tutkimuskysymys ja päivämäärä
- välineet ja niiden tarkkuus
- vakioidut asiat
- mittaukset taulukkona yksiköineen
- havainnot, esimerkiksi "auto kääntyi sivuun".

Kirjaa lukemat sellaisenaan. Silloin kirjaus pysyy objektiivisena eli ei muutu omien odotusten mukaiseksi. Älä poista tai korjaa hiljaa mittausta, joka näyttää oudolta. Merkitse se ja kirjaa, mitä silloin tapahtui. Lyhyt esimerkki:

| $s\ (\text{m})$ | $t_1\ (\text{s})$ | $t_2\ (\text{s})$ | $t_3\ (\text{s})$ | huomio |
|---|---|---|---|---|
| 0,50 | 1,3 | 1,1 | 1,4 | vaikea ajoittaa |
| 1,00 | 2,5 | 2,3 | 2,6 | |
| 1,50 | 3,7 | 3,5 | 3,6 | |

### Raportti
**Raportti** kertoo tutkimuksen niin, että toinen voi toistaa sen. Toinen voi myös arvioida johtopäätöksen. Raportin osat ovat:

1. tutkimuskysymys ja hypoteesi
2. menetelmä: välineet, muuttujat ja toteutus
3. tulokset: taulukko, kuvaaja ja suureen arvo epävarmuuksineen
4. pohdinta: virhelähteet ja se, mitä seuraavalla kerralla tehtäisiin toisin
5. johtopäätös: vastaus tutkimuskysymykseen ja se, tukevatko tulokset hypoteesia.

Johtopäätös on vain niin vahva kuin aineisto. Jos mittaukset vastaavat ennustetta epävarmuuden rajoissa, hypoteesi on saanut tukea. Sitä ei silti ole todistettu.

## Kaava: Suhteellinen epävarmuus ja mittausalueen valinta
Käsin mitatun ajan epävarmuus $\Delta t$ johtuu pääosin reaktioajasta. Se on lähes sama lyhyessä ja pitkässä mittauksessa. Siksi mittauksen laatua kuvaa **suhteellinen epävarmuus**. Se tarkoittaa epävarmuutta suhteessa mitattuun arvoon. Suhteellinen epävarmuus saa olla enintään $\varepsilon_\text{max}$. Silloin mitattavan ajan pitää olla vähintään
```latex
\begin{aligned}
\varepsilon &= \frac{\Delta t}{t} \\
t &\ge \frac{\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```
missä $\varepsilon$ on suhteellinen epävarmuus (ilmoitetaan usein prosentteina), $\Delta t$ ajan epävarmuus (s) ja $t$ mitattu aika (s). Esimerkki: epävarmuus on $\Delta t = 0{,}2\,\text{s}$ ja raja on $5\,\%$. Silloin aikaa pitää olla vähintään $4\,\text{s}$.

<svg data-fig="epavarmuus" data-style="house" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja näyttää suhteellisen epävarmuuden ajan funktiona. Ajan epävarmuus on 0,2 s. Kun aika on 1 s, epävarmuus on 20 %. Kun aika on 4 s, epävarmuus on 5,0 %. Kun aika on 10 s, epävarmuus on 2,0 %. Vihreä alue näyttää mittaukset, joiden epävarmuus on enintään 5,0 %. Ne vaativat vähintään 4 s:n ajan. Kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="176" y1="286" x2="176" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="256" y1="286" x2="256" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="336" y1="286" x2="336" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="416" y1="286" x2="416" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="496" y1="286" x2="496" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="189.5" x2="496" y2="189.5" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="141" x2="496" y2="141" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="92.5" x2="496" y2="92.5" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="514" y2="286" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M522,286 L510.5,291 L514,286 L510.5,281 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="36" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M96,28 L101,39.5 L96,36 L91,39.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="176" y1="286" x2="176" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="166" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="256" y1="286" x2="256" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="246" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="336" y1="286" x2="336" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="326" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="416" y1="286" x2="416" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="406" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="496" y1="286" x2="496" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="237.5" x2="96" y2="237.5" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="64" y="223" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="189.5" x2="96" y2="189.5" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="175" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="141" x2="96" y2="141" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="126.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="92.5" x2="96" y2="92.5" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="66" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="271.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="-2.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\varepsilon\ (\%)$</div></foreignObject>
  <polygon points="256,286 496,286 496,237.5 256,237.5" fill="#b2f2bb" fill-opacity="0.7"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <polyline points="136,92.5 139,106 142,118 145,128 148,137.5 151,145.5 154,152.5 157,159 160,165 163,170.5 166,175.5 169,180 172,184 175,188 178,191.5 181,195 184,198 187,201 190,203.5 193,206.5 196,208.5 199,211 202,213 205,215 208,217 211,219 214,220.5 217,222 220,223.5 223,225 226,226.5 229,228 232,229 235,230.5 238,231.5 241,232.5 244,233.5 247,235 250,236 253,236.5 256,237.5 259,238.5 262,239.5 265,240 268,241 271,242 274,242.5 277,243.5 280,244 283,244.5 286,245.5 289,246 292,246.5 295,247 298,247.5 301,248.5 304,249 307,249.5 310,250 313,250.5 316,251 319,251.5 322,252 325,252 328,252.5 331,253 334,253.5 337,254 340,254.5 343,254.5 346,255 349,255.5 352,256 355,256 358,256.5 361,257 364,257 367,257.5 370,258 373,258 376,258.5 379,258.5 382,259 385,259 388,259.5 391,260 394,260 397,260.5 400,260.5 403,261 406,261 409,261.5 412,261.5 415,262 418,262 421,262 424,262.5 427,262.5 430,263 433,263 436,263.5 439,263.5 442,263.5 445,264 448,264 451,264 454,264.5 457,264.5 460,265 463,265 466,265 469,265.5 472,265.5 475,265.5 478,266 481,266 484,266 487,266 490,266.5 493,266.5 496,266.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="256" y1="237.5" x2="256" y2="286" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="96" y1="237.5" x2="256" y2="237.5" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="256" cy="237.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="304" y="188.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\varepsilon \le 5\,\%$</div></foreignObject>
  <foreignObject x="184" y="73.5" width="180" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\varepsilon = \dfrac{0{,}2\,\text{s}}{t}$</div></foreignObject>
</svg>

Tarvittava matka saadaan tasaisen liikkeen mallista $s = vt$. Jos mittaus tehdään usealla matkalla, mittauspisteisiin sovitetaan suora (luku *Graafinen esitys ja suoran sovittaminen*). Aika $t$ on vaaka-akselilla ja matka $s$ pystyakselilla. Silloin suoran kulmakerroin on nopeus $v$. Lyhin kelvollinen matka on se, jolla suhteellinen epävarmuus vielä pysyy valitussa rajassa $\varepsilon_\text{max}$. Lyhyemmällä matkalla suhteellinen epävarmuus ylittää tämän rajan. Silloin tulos on liian epätarkka.

## Esimerkki
Oppilaat tutkivat leluauton liikettä. Esikokeessa auton nopeus on noin $0{,}42\,\text{m/s}$. Aika mitataan käsikellolla. Ajanoton epävarmuus on $\Delta t = 0{,}2\,\text{s}$. Ajanmittauksen suhteellinen epävarmuus saa olla enintään $5{,}0\,\%$. Kuinka pitkä matka auton pitää vähintään kulkea?

<!-- vaihe -->

**Tunnetut ja kysytty.** Nopeus $v = 0{,}42\,\text{m/s}$, ajan epävarmuus $\Delta t = 0{,}2\,\text{s}$ ja suurin sallittu suhteellinen epävarmuus $\varepsilon_\text{max} = 5{,}0\,\% = 0{,}050$. Kysytään lyhintä matkaa $s_\text{min}$.

<!-- vaihe -->

**Periaate.** Mitattava aika kasvaa, ja silloin suhteellinen epävarmuus pienenee, koska $\Delta t$ pysyy samana. Lasketaan ensin lyhin sallittu aika epävarmuuden rajasta. Auto liikkuu vakionopeudella. Siksi tasaisen liikkeen malli $s = vt$ antaa ajasta matkan.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&t_\text{min} = \frac{\Delta t}{\varepsilon_\text{max}} \\
&s_\text{min} = v\, t_\text{min} = \frac{v\,\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Nopeus on yksikössä $\text{m/s}$ ja aika sekunteina, joten matka tulee metreinä. Prosentti on muunnettu desimaaliluvuksi: $5{,}0\,\% = 0{,}050$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
t_\text{min} &= \frac{\Delta t}{\varepsilon_\text{max}} \\
&= \frac{0{,}2\,\text{s}}{0{,}050} = 4\,\text{s} \\
s_\text{min} &= v\, t_\text{min} \\
&= 0{,}42\,\tfrac{\text{m}}{\text{s}} \cdot 4\,\text{s} \\
&= 1{,}68\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Matkan pitää olla vähintään $1{,}7\,\text{m}$. Tämä on suunnitteluarvio. Sen tarkkuutta rajoittaa epävarmuus $0{,}2\,\text{s}$, joka on annettu yhdellä numerolla. Siksi vähimmäismatka ilmoitetaan käytännön tarkkuudella, tässä kahdella numerolla kuten nopeus $0{,}42\,\text{m/s}$. Matka pyöristetään ylöspäin, jotta raja varmasti täyttyy.

<!-- vaihe -->

**Järkevyys.** Matkalla $1{,}7\,\text{m}$ auton kulkuaika on noin $1{,}7\,\text{m} : 0{,}42\,\text{m/s} \approx 4{,}05\,\text{s}$. Silloin $\varepsilon = 0{,}2\,\text{s} : 4{,}05\,\text{s} \approx 4{,}9\,\%$ eli juuri ja juuri rajan sisällä. Matkalla $0{,}50\,\text{m}$ aika olisi vain $1{,}2\,\text{s}$ ja epävarmuus noin $17\,\%$. Siksi lyhyt matka olisi huono valinta.

## Yleinen virhekäsitys
Moni ajattelee, että tutkimus on epäonnistunut, jos mittaus ei tue hypoteesia. Näin ei ole. Jos mittaus kumoaa hypoteesin, tutkija tietää jotakin, mitä hän ei aiemmin tiennyt. Epäonnistunut tutkimus on sellainen, josta ei voi päätellä mitään. Silloin muuttujia ei ole hallittu tai mittaukset ovat liian epävarmoja.

Toinen yleinen virhe on pitää yhtä mittausta riittävänä. Yksi lukema ei kerro, kuinka paljon tulos vaihtelee. Siksi satunnaisvirheen aiheuttamaa hajontaa ei voi arvioida. Kolmas virhe on valita tulokseen sopivat mittaukset ja jättää muut pois. Kaikki mittaukset kirjataan, ja poikkeava mittaus selitetään tai merkitään.

## Tiivistelmä
- Tutkimus alkaa kysymyksestä, jonka voi mitata. Siinä on myös hypoteesi, jonka voi testata ja joka voi osoittautua vääräksi.
- Reilussa kokeessa muutetaan yhtä muuttujaa, mitataan toista ja pidetään muut vakioina.
- Mittaus suunnitellaan etukäteen: mittausalue, pisteiden määrä, toistot ja vakioidut asiat. Esikoe tarkistaa suunnitelman.
- Pöytäkirjaan kirjataan lukemat, yksiköt, välineet ja havainnot kokeen aikana. Mitään mittausta ei poisteta hiljaa.
- Suhteellinen epävarmuus $\varepsilon = \Delta t : t$ pienenee, kun mitattava aika kasvaa. Siksi aikaa on oltava vähintään $\Delta t : \varepsilon_\text{max}$.
- Raportti kertoo kysymyksen, menetelmän, tulokset, pohdinnan ja johtopäätöksen. Näin toinen voi toistaa tutkimuksen.
