# Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi

> **Miksi** kaksi ryhmää saa samalle leluautolle eri nopeuden, vaikka kumpikin mittaa huolellisesti?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: luokan lattialla on rata. Leluauto kulkee radalla mittanauhan vieressä. Radan kummallakin puolella on ryhmä. Kummallakin ryhmällä on oma sekuntikello. Kellojen viisarit ovat pysähtyneet eri kohtiin." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy18h-w1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy18h-w2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy18h-floor" gradientUnits="userSpaceOnUse" x1="0" y1="300" x2="0" y2="600"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><linearGradient id="fy18h-track" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy18h-car" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="120" y="40" width="200" height="170" rx="4" fill="url(#fy18h-w1)" stroke="#1f2933" stroke-width="3"/>
  <path d="M164,119.5 Q163,106 179,107.5 Q185.5,93 201.5,98 Q216,90 224,105 Q238.5,106.5 237,119.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="220" y1="40" x2="220" y2="210" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="125" x2="320" y2="125" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="108" y="210" width="224" height="14" rx="3" fill="#c9c2b2" stroke="#1f2933" stroke-width="3"/>
  <rect x="880" y="40" width="200" height="170" rx="4" fill="url(#fy18h-w2)" stroke="#1f2933" stroke-width="3"/>
  <path d="M924,119.5 Q923,106 939,107.5 Q945.5,93 961.5,98 Q976,90 984,105 Q998.5,106.5 997,119.5 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="980" y1="40" x2="980" y2="210" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="880" y1="125" x2="1080" y2="125" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="868" y="210" width="224" height="14" rx="3" fill="#c9c2b2" stroke="#1f2933" stroke-width="3"/>
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
  <path d="M180,500 L1020,500 L940,400 L260,400 Z" fill="url(#fy18h-track)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M260,400 H940" fill="none" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"/>
  <line x1="300" y1="400" x2="276" y2="500" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt" stroke-dasharray="10 8"/>
  <line x1="900" y1="400" x2="876" y2="500" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt" stroke-dasharray="10 8"/>
  <rect x="170" y="504" width="860" height="30" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
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
  <path d="M530,474 V444 Q538,434 566,432 L586,400 H644 L668,432 Q692,436 694,452 V474 Z" fill="url(#fy18h-car)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M594,408 H640 L656,430 H580 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="618" y1="408" x2="618" y2="430" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="680" y="444" width="12" height="8" rx="2" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="564" cy="476" r="18" fill="#1f2933"/>
  <circle cx="564" cy="476" r="8" fill="#c4ccd4"/>
  <circle cx="660" cy="476" r="18" fill="#1f2933"/>
  <circle cx="660" cy="476" r="8" fill="#c4ccd4"/>
  <line x1="460" y1="446" x2="500" y2="446" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="480" y1="464" x2="520" y2="464" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="450" y1="480" x2="490" y2="480" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <path d="M93,390 L97,291 H123 L127,390 H114 L110,324 L106,390 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M87.5,297.5 Q85,225 110,221 Q135,225 132.5,297.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M90,234 L83.5,297.5" fill="none" stroke="#2b8a3e" stroke-width="14.52" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="83.5" cy="303" r="7.26" fill="#f1dfb5"/>
  <path d="M130,234 L136.5,297.5" fill="none" stroke="#2b8a3e" stroke-width="14.52" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="136.5" cy="303" r="7.26" fill="#f1dfb5"/>
  <rect x="104" y="208" width="12" height="16" fill="#f1dfb5"/>
  <circle cx="110" cy="194.5" r="19.8" fill="#f1dfb5"/>
  <path d="M89.5,194.5 Q90,171 110,172 Q131,172 130.5,192 Q114,184 89.5,194.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M172,396 L176,291 H204 L208,396 H194 L190,326 L186,396 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M166,298 Q163.5,221 190,217 Q216.5,221 214,298 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M169,231 L162,298" fill="none" stroke="#1971c2" stroke-width="15.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="162" cy="303.5" r="7.7" fill="#f1dfb5"/>
  <path d="M211,231 L218,298" fill="none" stroke="#1971c2" stroke-width="15.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="218" cy="303.5" r="7.7" fill="#f1dfb5"/>
  <rect x="183.5" y="203" width="12.5" height="17" fill="#f1dfb5"/>
  <circle cx="190" cy="189" r="21" fill="#f1dfb5"/>
  <path d="M168.5,189 Q169,163.5 190,165 Q212.5,165 211.5,186 Q194,177.5 168.5,189 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="210" y1="231" x2="260" y2="276" stroke="#1971c2" stroke-width="16" stroke-linecap="round"/>
  <rect x="248" y="262" width="24" height="30" rx="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="253" y="164" width="14" height="10.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="257" y="173.5" width="6" height="6" fill="#6c757d"/>
  <circle cx="260" cy="222" r="44" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="260" cy="222" r="36.08" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
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
  <path d="M1073,390 L1077,291 H1103 L1107,390 H1094 L1090,324 L1086,390 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M1067.5,297.5 Q1065,225 1090,221 Q1115,225 1112.5,297.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M1070,234 L1063.5,297.5" fill="none" stroke="#1971c2" stroke-width="14.52" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1063.5" cy="303" r="7.26" fill="#f1dfb5"/>
  <path d="M1110,234 L1116.5,297.5" fill="none" stroke="#1971c2" stroke-width="14.52" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1116.5" cy="303" r="7.26" fill="#f1dfb5"/>
  <rect x="1084" y="208" width="12" height="16" fill="#f1dfb5"/>
  <circle cx="1090" cy="194.5" r="19.8" fill="#f1dfb5"/>
  <path d="M1069.5,194.5 Q1070,171 1090,172 Q1111,172 1110.5,192 Q1094,184 1069.5,194.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M992,396 L996,291 H1024 L1028,396 H1014 L1010,326 L1006,396 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M986,298 Q983.5,221 1010,217 Q1036.5,221 1034,298 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M989,231 L982,298" fill="none" stroke="#e8590c" stroke-width="15.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="982" cy="303.5" r="7.7" fill="#f1dfb5"/>
  <path d="M1031,231 L1038,298" fill="none" stroke="#e8590c" stroke-width="15.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1038" cy="303.5" r="7.7" fill="#f1dfb5"/>
  <rect x="1003.5" y="203" width="12.5" height="17" fill="#f1dfb5"/>
  <circle cx="1010" cy="189" r="21" fill="#f1dfb5"/>
  <path d="M988.5,189 Q989,163.5 1010,165 Q1032.5,165 1031.5,186 Q1014,177.5 988.5,189 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="990" y1="231" x2="940" y2="276" stroke="#e8590c" stroke-width="16" stroke-linecap="round"/>
  <rect x="928" y="262" width="24" height="30" rx="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="933" y="164" width="14" height="10.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="937" y="173.5" width="6" height="6" fill="#6c757d"/>
  <circle cx="940" cy="222" r="44" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="940" cy="222" r="36.08" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
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
Fysiikka on kokeellinen tiede. Väite pätee vasta, kun sitä on testattu mittauksilla. Kuka tahansa voi toistaa nämä mittaukset. **Tutkimus** on järjestelmällinen tapa vastata kysymykseen mittaamalla. Tutkimus alkaa kysymyksestä. Se päättyy johtopäätökseen, jonka mittaustulokset perustelevat. Hyvä tutkimus ei ole sellainen, jossa oletus osoittautuu oikeaksi. Hyvässä tutkimuksessa mittaus voisi näyttää oletuksen vääräksi.

### Tutkimuskysymys ja hypoteesi
Tutkimuskysymys on kysymys, johon mittaus voi vastata. Esimerkki on "Miten leluauton kulkema matka riippuu ajasta?" Kysymys "Mikä auto on paras?" ei kelpaa, koska sitä ei voi mitata.

**Hypoteesi** on perusteltu ja testattava ennuste kysymykseen. Esimerkiksi: "Jos auto liikkuu vakionopeudella, kulkema matka on suoraan verrannollinen aikaan, $s = vt$." Hypoteesista pitää seurata jotain mitattavaa. Sen pitää myös voida osoittautua vääräksi. Ennuste "auto kulkee jotenkin" ei ole hypoteesi, koska mikään mittaus ei kumoa sitä.

### Muuttujat
**Muuttuja** on suure, jonka arvo voi vaihdella tutkimuksessa. Kokeessa tehdään kolme asiaa. Yhtä muuttujaa muutetaan, toista mitataan ja kaikki muut pidetään samoina:
- **muutettava muuttuja**: kokeen tekijä valitsee sen arvot, tässä matka $s$
- **mitattava muuttuja**: sen arvo luetaan mittarista, tässä aika $t$
- **vakioitavat muuttujat**: ne pysyvät samoina koko kokeen ajan, tässä auto, paristot, alusta ja lähtötapa.

Joskus kaksi muuttujaa muuttuu yhtä aikaa, esimerkiksi matka ja paristot. Silloin ei voi päätellä, mikä muutti tulosta. Siksi koe on reilu vasta, kun vain muutettava muuttuja vaihtuu.

<svg data-fig="setup" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kokeen asetelmasta. Leluauto ajaa pöydällä tasaisella radalla lähtöviivalta maaliviivalle. Radan vieressä on matka-asteikko metreinä. Lähtöviivan ja maaliviivan väli on muutettava muuttuja, matka s. Käsikello mittaa aikaa t. Aika on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy18-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <foreignObject x="24" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{muutettava: } s$</div></foreignObject>
  <foreignObject x="24" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mitattava: } t$</div></foreignObject>
  <foreignObject x="24" y="81.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vakiona: auto, alusta, paristot}$</div></foreignObject>
  <rect x="514" y="20" width="12" height="12" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="66" r="30" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="520" y1="44" x2="520" y2="39" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="531" y1="47" x2="533.5" y2="42.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="539" y1="55" x2="543.5" y2="52.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="542" y1="66" x2="547" y2="66" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="539" y1="77" x2="543.5" y2="79.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="531" y1="85" x2="533.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="88" x2="520" y2="93" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="509" y1="85" x2="506.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="501" y1="77" x2="496.5" y2="79.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="498" y1="66" x2="493" y2="66" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="501" y1="55" x2="496.5" y2="52.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="509" y1="47" x2="506.5" y2="42.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="66" x2="536" y2="52" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <circle cx="520" cy="66" r="3.5" fill="#1f2933"/>
  <foreignObject x="510" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t$</div></foreignObject>
  <rect x="40" y="200" width="520" height="16" fill="url(#fy18-wood)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="72" y1="216" x2="72" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="62" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="147" y1="216" x2="147" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="124.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="222" y1="216" x2="222" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="212" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="297" y1="216" x2="297" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="274.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="372" y1="216" x2="372" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="362" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="447" y1="216" x2="447" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="424.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <foreignObject x="475" y="227.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <line x1="72" y1="140" x2="72" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="37" y="111.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lähtö}$</div></foreignObject>
  <line x1="372" y1="140" x2="372" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="337" y="111.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maali}$</div></foreignObject>
  <rect x="92" y="166" width="68" height="22" rx="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="108" y="148" width="36" height="18" rx="5" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="110" cy="191" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="144" cy="191" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="176" y1="160" x2="237" y2="160" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M250,160 L236,166.5 L236,153.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="264" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <line x1="72" y1="268" x2="372" y2="268" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="72" y1="258" x2="72" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="372" y1="258" x2="372" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="168" y="285.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$s = 2{,}00\,\text{m}$</div></foreignObject>
</svg>

### Suunnittelu ennen mittausta
Suunnitelma vastaa ennen mittausta näihin kysymyksiin:
- Mitä mitataan ja millä välineellä?
- Mitkä arvot muutettavalle muuttujalle valitaan, ja kuinka monta?
- Montako toistoa kustakin arvosta tehdään?
- Mitä pidetään vakiona?

Kokeile ensin esikokeella. Esikoe kertoo, onko mittaus ylipäätään mahdollinen. Se antaa myös karkean arvion tuloksesta.

Valitse mittausalue niin, että mitattava suure on selvästi suurempi kuin mittauksen epävarmuus (ks. kohta *Suhteellinen epävarmuus ja mittausalueen valinta*). Valitse useita arvoja ja pidä niiden välit yhtä suurina. Yksi tai kaksi pistettä ei näytä, onko riippuvuus suora.

### Mittauspöytäkirja
**Mittauspöytäkirja** on kirjaus, joka tehdään kokeen aikana. Sitä ei tehdä muistista jälkikäteen. Siihen kirjataan nämä asiat:
- tutkimuskysymys ja päivämäärä
- välineet ja niiden tarkkuus
- vakioidut asiat
- mittaukset taulukkona yksiköineen
- havainnot, esimerkiksi "auto kääntyi sivuun".

Kirjaa lukemat sellaisenaan. Älä poista tai korjaa hiljaa mittausta, joka näyttää oudolta. Merkitse se ja kirjaa, mitä silloin tapahtui. Lyhyt esimerkki:

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

Johtopäätös on vain niin vahva kuin aineisto. Jos mittaukset osuvat epävarmuuden sisällä ennusteeseen, hypoteesi on saanut tukea. Sitä ei silti ole todistettu.

## Kaava: Suhteellinen epävarmuus ja mittausalueen valinta
Käsin mitatun ajan epävarmuus $\Delta t$ johtuu pääosin reaktioajasta. Se on lähes sama lyhyessä ja pitkässä mittauksessa. Siksi mittauksen laatua kuvaa **suhteellinen epävarmuus**. Se tarkoittaa epävarmuutta suhteessa mitattuun arvoon. Suhteellinen epävarmuus saa olla enintään $\varepsilon_\text{max}$. Silloin mitattavan ajan pitää olla vähintään
```latex
\begin{aligned}
\varepsilon &= \frac{\Delta t}{t} \\
t &\ge \frac{\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```
missä $\varepsilon$ on suhteellinen epävarmuus (ilmoitetaan usein prosentteina), $\Delta t$ ajan epävarmuus (s) ja $t$ mitattu aika (s). Esimerkki: epävarmuus on $\Delta t = 0{,}2\,\text{s}$ ja raja on $5\,\%$. Silloin aikaa pitää olla vähintään $4\,\text{s}$.

<svg data-fig="epavarmuus" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja näyttää suhteellisen epävarmuuden ajan funktiona. Ajan epävarmuus on 0,2 s. Kun aika on 1 s, epävarmuus on 20 %. Kun aika on 4 s, epävarmuus on 5,0 %. Kun aika on 10 s, epävarmuus on 2,0 %. Vihreä alue näyttää mittaukset, joiden epävarmuus on enintään 5,0 %. Ne vaativat vähintään 4 s:n ajan. Kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="176" y1="286" x2="176" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="286" x2="256" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="286" x2="336" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="286" x2="416" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496" y1="286" x2="496" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="189.5" x2="496" y2="189.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="141" x2="496" y2="141" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="92.5" x2="496" y2="92.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="510" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M522,286 L509,292 L509,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,28 L102,41 L90,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="176" y1="286" x2="176" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="256" y1="286" x2="256" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="336" y1="286" x2="336" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="326" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="416" y1="286" x2="416" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="406" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="496" y1="286" x2="496" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="237.5" x2="96" y2="237.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="223" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="189.5" x2="96" y2="189.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="175" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="141" x2="96" y2="141" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="126.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="92.5" x2="96" y2="92.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="66" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="271.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="-2.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\varepsilon\ (\%)$</div></foreignObject>
  <polygon points="256,286 496,286 496,237.5 256,237.5" fill="#b2f2bb" fill-opacity="0.7"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <polyline points="136,92.5 139,106 142,118 145,128 148,137.5 151,145.5 154,152.5 157,159 160,165 163,170.5 166,175.5 169,180 172,184 175,188 178,191.5 181,195 184,198 187,201 190,203.5 193,206.5 196,208.5 199,211 202,213 205,215 208,217 211,219 214,220.5 217,222 220,223.5 223,225 226,226.5 229,228 232,229 235,230.5 238,231.5 241,232.5 244,233.5 247,235 250,236 253,236.5 256,237.5 259,238.5 262,239.5 265,240 268,241 271,242 274,242.5 277,243.5 280,244 283,244.5 286,245.5 289,246 292,246.5 295,247 298,247.5 301,248.5 304,249 307,249.5 310,250 313,250.5 316,251 319,251.5 322,252 325,252 328,252.5 331,253 334,253.5 337,254 340,254.5 343,254.5 346,255 349,255.5 352,256 355,256 358,256.5 361,257 364,257 367,257.5 370,258 373,258 376,258.5 379,258.5 382,259 385,259 388,259.5 391,260 394,260 397,260.5 400,260.5 403,261 406,261 409,261.5 412,261.5 415,262 418,262 421,262 424,262.5 427,262.5 430,263 433,263 436,263.5 439,263.5 442,263.5 445,264 448,264 451,264 454,264.5 457,264.5 460,265 463,265 466,265 469,265.5 472,265.5 475,265.5 478,266 481,266 484,266 487,266 490,266.5 493,266.5 496,266.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="256" y1="237.5" x2="256" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="237.5" x2="256" y2="237.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="256" cy="237.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="304" y="188.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\varepsilon \le 5\,\%$</div></foreignObject>
  <foreignObject x="184" y="73.5" width="180" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\varepsilon = \dfrac{0{,}2\,\text{s}}{t}$</div></foreignObject>
</svg>

Tarvittava matka saadaan tasaisen liikkeen mallista $s = vt$. Jos mittaus tehdään usealla matkalla, mittauspisteisiin sovitetaan suora (luku *Graafinen esitys ja suoran sovittaminen*). Aika $t$ on vaaka-akselilla ja matka $s$ pystyakselilla. Silloin suoran kulmakerroin on nopeus $v$. Lyhin kelvollinen matka on se, jolla suhteellinen epävarmuus vielä pysyy valitussa rajassa $\varepsilon_\text{max}$. Lyhyemmällä matkalla suhteellinen epävarmuus ylittää tämän rajan. Silloin tulos on liian epätarkka.

## Esimerkki
Oppilaat tutkivat leluauton liikettä. Esikokeessa auton nopeus on noin $0{,}42\,\text{m/s}$. Aika mitataan käsikellolla. Ajanoton epävarmuus on $\Delta t = 0{,}2\,\text{s}$. Mittauksen suhteellinen epävarmuus saa olla enintään $5{,}0\,\%$. Kuinka pitkä matka auton pitää vähintään kulkea?

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

**Tulos.** Matkan pitää olla vähintään $1{,}7\,\text{m}$. Tulos pyöristetään kahteen merkitsevään numeroon, kuten nopeus $0{,}42\,\text{m/s}$. Epävarmuus $0{,}2\,\text{s}$ on annettu yhdellä numerolla. Siksi se antaa vain arvion lyhimmästä ajasta.

<!-- vaihe -->

**Järkevyys.** Matkalla $1{,}7\,\text{m}$ auton kulkuaika on noin $1{,}7\,\text{m} : 0{,}42\,\text{m/s} \approx 4{,}05\,\text{s}$. Silloin $\varepsilon = 0{,}2\,\text{s} : 4{,}05\,\text{s} \approx 4{,}9\,\%$ eli tasan rajan sisällä. Matkalla $0{,}50\,\text{m}$ aika olisi vain $1{,}2\,\text{s}$ ja epävarmuus noin $17\,\%$. Siksi lyhyt matka oli huono valinta.

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
