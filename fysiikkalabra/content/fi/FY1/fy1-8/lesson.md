# Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi

> **Miksi** kaksi ryhmää saa samalle leluautolle eri nopeuden, vaikka kumpikin mittaa huolellisesti?

<svg data-fig="hero" data-style="house" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: luokan lattialla rata, jolla leluauto kulkee mittanauhan vieressä. Radan molemmin puolin on ryhmä: kummallakin on oma sekuntikello, ja kellojen viisarit ovat pysähtyneet eri kohtiin." class="fig-hero" style="max-width:100%;font-size:24px">
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
  <rect x="248" y="262" width="24" height="30" rx="10" fill="#f1dfb5" stroke="#857b64" stroke-width="2"/>
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
  <rect x="928" y="262" width="24" height="30" rx="10" fill="#f1dfb5" stroke="#857b64" stroke-width="2"/>
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
Fysiikka on kokeellinen tiede. Fysikaalisia väitteitä arvioidaan havaintojen ja mittausten avulla. Hyvän tutkimuksen menetelmät kuvataan niin tarkasti, että muut voivat koetella tuloksia ja mahdollisuuksien mukaan toistaa mittaukset. **Tutkimus** on järjestelmällinen tapa vastata kysymykseen mittaamalla. Se alkaa kysymyksestä ja päättyy johtopäätökseen, jonka mittaustulokset perustelevat. Hyvä tutkimus ei ole sellainen, jossa oletus osoittautuu oikeaksi, vaan sellainen, jossa mittaus voisi näyttää oletuksen vääräksi.

<figure class="unit-photo"><img src="pics/fy1/ligo-scientists-laser-room.webp" alt="Kaksi suojapukuista tutkijaa seisoo valkoisessa puhdastilassa laserlaitteiston äärellä ja katsoo sitä mietteliäänä."><figcaption>Tutkijat tarkastelevat LIGO-gravitaatioaaltoilmaisimen laserlaitteistoa puhdastilassa Hanfordissa Yhdysvalloissa vuonna 2019.</figcaption></figure>

### Tutkimuskysymys ja hypoteesi
Tutkimuskysymys on kysymys, johon mittaus voi vastata: "Miten leluauton kulkuaika riippuu ajomatkan pituudesta?" Kysymys "Mikä auto on paras?" ei kelpaa, koska sitä ei voi mitata.

**Hypoteesi** on perusteltu ja testattava ennuste, joka vastaa tutkimuskysymykseen. Esimerkiksi: "Auto liikkuu radalla vakionopeudella, joten sen kulkema matka on suoraan verrannollinen aikaan, $s = vt$." Hypoteesista pitää seurata jotain mitattavaa, joka voi osoittautua vääräksi. Ennuste "auto kulkee jotenkin" ei ole hypoteesi, koska mikään mittaus ei kumoa sitä.

### Muuttujat
**Muuttuja** on suure tai muu tekijä, joka voi vaihdella tutkimuksessa. Kokeessa muutetaan yhtä muuttujaa, mitataan toista ja pidetään kaikki muut samoina:

- **muutettava muuttuja**: kokeen tekijä valitsee sen arvot, tässä matka $s$
- **mitattava muuttuja**: sen arvo luetaan mittarista, tässä aika $t$
- **vakioitavat muuttujat**: pysyvät samoina koko kokeen ajan, tässä auto, paristot, alusta ja lähtötapa.

Jos kaksi muuttujaa muuttuu yhtä aikaa, esimerkiksi matka ja paristot, tuloksen muutoksen syytä ei voi päätellä. Siksi koe on reilu vasta, kun vain muutettava muuttuja vaihtuu.

<svg data-fig="setup" data-style="house" viewBox="0 0 600 414" role="img" aria-label="Kaavakuva kokeen asetelmasta: paristokäyttöinen leluauto ajaa pöydällä lähtöviivalta maaliviivalle, jossa on ruutulippu. Pöydän reunassa on mittanauha, jonka asteikko on metreinä, ja lähtöviivan ja maaliviivan väli on muutettava muuttuja, matka s. Sekuntikello mittaa aikaa t, joka on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä." style="max-width:100%;font-size:24px">
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
Taustatietoa ilmiöstä ja menetelmistä hankitaan ennen suunnittelua lähdekriittisesti: arvioi, kuka tiedon on tuottanut ja miksi, miten se perustellaan, onko se ajantasaista ja tukevatko muut lähteet sitä. Suunnitelma vastaa ennen mittausta kysymyksiin: mitä mitataan ja millä välineellä, mitkä arvot muutettavalle muuttujalle valitaan ja kuinka monta, montako toistoa kustakin arvosta tehdään ja mitä pidetään vakiona. Kokeile suunnitelmaa ensin esikokeella. Se kertoo, onko mittaus ylipäätään mahdollinen, ja antaa karkean arvion tuloksesta.

Valitse mittausalue niin, että mitattava suure on selvästi suurempi kuin mittauksen epävarmuus (ks. kohta *Suhteellinen epävarmuus ja mittausalueen valinta*). Valitse useita arvoja tasavälein, koska yhdestä tai kahdesta pisteestä ei näe, ovatko pisteet suoralla.

### Mittauspöytäkirja
**Mittauspöytäkirja** on kirjaus, joka tehdään kokeen aikana, ei muistista jälkikäteen. Siihen kirjataan tutkimuskysymys, päivämäärä, välineet ja niiden tarkkuus, vakioidut asiat, mittaukset taulukkona yksiköineen sekä havainnot, esimerkiksi "auto kääntyi sivuun".

Kirjaa lukemat sellaisenaan, jotta kirjaus pysyy objektiivisena eikä muutu omien odotusten mukaiseksi. Älä poista tai korjaa hiljaa mittausta, joka näyttää oudolta: merkitse se ja kirjaa, mitä silloin tapahtui. Lyhyt esimerkki:

| $s\ (\text{m})$ | $t_1\ (\text{s})$ | $t_2\ (\text{s})$ | $t_3\ (\text{s})$ | huomio |
|---|---|---|---|---|
| 0,50 | 1,3 | 1,1 | 1,4 | vaikea ajoittaa |
| 1,00 | 2,5 | 2,3 | 2,6 | |
| 1,50 | 3,7 | 3,5 | 3,6 | |

### Raportti
**Raportti** kertoo tutkimuksen niin, että toinen voi toistaa sen ja arvioida johtopäätöksen. Sen osat ovat:

1. tutkimuskysymys ja hypoteesi
2. menetelmä: välineet, muuttujat ja toteutus
3. tulokset: taulukko, kuvaaja ja suureen arvo epävarmuuksineen
4. pohdinta: virhelähteet ja se, mitä seuraavalla kerralla tehtäisiin toisin
5. johtopäätös: vastaus tutkimuskysymykseen ja se, tukevatko tulokset hypoteesia.

Johtopäätös on vain niin vahva kuin aineisto. Jos mittaukset vastaavat ennustetta epävarmuuden rajoissa, hypoteesi on saanut tukea, mutta sitä ei ole todistettu.

## Kaava: Suhteellinen epävarmuus ja mittausalueen valinta
Käsin mitatun ajan epävarmuus $\Delta t$ johtuu pääosin reaktioajasta, ja se on lähes sama lyhyessä ja pitkässä mittauksessa. Mittauksen laatua kuvaa siksi **suhteellinen epävarmuus**, epävarmuus suhteessa mitattuun arvoon. Jotta se ei ylitä arvoa $\varepsilon_\text{max}$, mitattavan ajan pitää olla vähintään
```latex
\begin{aligned}
\varepsilon &= \frac{\Delta t}{t} \\
t &\ge \frac{\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```
missä $\varepsilon$ on suhteellinen epävarmuus (ilmoitetaan usein prosentteina), $\Delta t$ ajan epävarmuus (s) ja $t$ mitattu aika (s). Epävarmuuden $\Delta t = 0{,}2\,\text{s}$ ja rajan $5\,\%$ yhdistelmällä aikaa pitää olla vähintään $4\,\text{s}$.

<svg data-fig="epavarmuus" data-style="house" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja suhteellisesta epävarmuudesta ajan funktiona, kun ajan epävarmuus on 0,2 s: kun aika on 1 s, epävarmuus on 20 %, kun aika on 4 s, se on 5,0 %, ja kun aika on 10 s, se on 2,0 %. Vihreä alue kuvaa mittauksia, joiden epävarmuus on enintään 5,0 %: ne vaativat vähintään 4 s:n ajan. Kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
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

Tarvittava matka saadaan tasaisen liikkeen mallista $s = vt$. Jos mittaus tehdään usealla matkalla, mittauspisteisiin sovitetaan suora (luku *Graafinen esitys ja suoran sovittaminen*). Kun $t$ on vaaka-akselilla ja $s$ pystyakselilla, suoran kulmakerroin on nopeus $v$. Lyhin kelvollinen matka on se, jolla suhteellinen epävarmuus vielä pysyy valitussa rajassa $\varepsilon_\text{max}$. Sitä lyhyemmällä matkalla suhteellinen epävarmuus ylittää tämän rajan, ja tulos on liian epätarkka.

## Esimerkki
Oppilaat tutkivat leluauton liikettä. Esikokeessa auton nopeus on noin $0{,}42\,\text{m/s}$. Aika mitataan käsikellolla, ja ajanoton epävarmuus on $\Delta t = 0{,}2\,\text{s}$. Ajanmittauksen suhteellinen epävarmuus halutaan enintään $5{,}0\,\%$. Kuinka pitkä matka auton pitää vähintään kulkea?

<!-- vaihe -->

**Tunnetut ja kysytty.** Nopeus $v = 0{,}42\,\text{m/s}$, ajan epävarmuus $\Delta t = 0{,}2\,\text{s}$ ja suurin sallittu suhteellinen epävarmuus $\varepsilon_\text{max} = 5{,}0\,\% = 0{,}050$. Kysytään lyhintä matkaa $s_\text{min}$.

<!-- vaihe -->

**Periaate.** Suhteellinen epävarmuus pienenee, kun mitattava aika kasvaa, koska $\Delta t$ pysyy samana. Lasketaan ensin lyhin sallittu aika epävarmuuden rajasta. Auto liikkuu vakionopeudella, joten tasaisen liikkeen malli $s = vt$ antaa ajasta matkan.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&t_\text{min} = \frac{\Delta t}{\varepsilon_\text{max}} \\
&s_\text{min} = v\, t_\text{min} = \frac{v\,\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: nopeus on yksikössä $\text{m/s}$ ja aika sekunteina, joten matka tulee metreinä. Prosentti on muunnettu desimaaliluvuksi: $5{,}0\,\% = 0{,}050$.

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

**Tulos.** Matkan pitää olla vähintään $1{,}7\,\text{m}$. Tämä on suunnitteluarvio, jonka tarkkuutta rajoittaa yhden numeron epävarmuus $0{,}2\,\text{s}$. Suunnitteluarvion vähimmäismatka ilmoitetaan siksi käytännön tarkkuudella, tässä kahdella numerolla kuten nopeus $0{,}42\,\text{m/s}$, ja pyöristetään ylöspäin, jotta raja varmasti täyttyy.

<!-- vaihe -->

**Järkevyys.** Matkalla $1{,}7\,\text{m}$ auton kulkuaika on noin $1{,}7\,\text{m} : 0{,}42\,\text{m/s} \approx 4{,}05\,\text{s}$, jolloin $\varepsilon = 0{,}2\,\text{s} : 4{,}05\,\text{s} \approx 4{,}9\,\%$ eli juuri ja juuri rajan sisällä. Matkalla $0{,}50\,\text{m}$ aika olisi vain $1{,}2\,\text{s}$ ja epävarmuus noin $17\,\%$, ja siksi lyhyt matka olisi huono valinta.

## Yleinen virhekäsitys
Moni ajattelee, että tutkimus on epäonnistunut, jos mittaus ei tue hypoteesia. Näin ei ole: jos mittaus kumoaa hypoteesin, tutkija tietää jotakin, mitä hän ei aiemmin tiennyt. Epäonnistunut tutkimus on sellainen, josta ei voi päätellä mitään, koska muuttujia ei ole hallittu tai mittaukset ovat liian epävarmoja.

Toinen yleinen virhe on pitää yhtä mittausta riittävänä. Yksi lukema ei kerro, kuinka paljon tulos vaihtelee, joten satunnaisvirheen aiheuttamaa hajontaa ei voi arvioida. Kolmas virhe on valita tulokseen sopivat mittaukset ja jättää muut pois: kaikki mittaukset kirjataan, ja poikkeava mittaus selitetään tai merkitään.

## Tiivistelmä
- Tutkimus alkaa mitattavissa olevasta kysymyksestä ja testattavasta hypoteesista, joka voi osoittautua vääräksi.
- Reilussa kokeessa muutetaan yhtä muuttujaa, mitataan toista ja pidetään muut vakioina.
- Mittaus suunnitellaan etukäteen: mittausalue, pisteiden määrä, toistot ja vakioidut asiat. Esikoe tarkistaa suunnitelman.
- Pöytäkirjaan kirjataan lukemat, yksiköt, välineet ja havainnot kokeen aikana. Mitään mittausta ei poisteta hiljaa.
- Suhteellinen epävarmuus $\varepsilon = \Delta t : t$ pienenee, kun mitattava aika kasvaa; siksi aikaa on oltava vähintään $\Delta t : \varepsilon_\text{max}$.
- Raportti kertoo kysymyksen, menetelmän, tulokset, pohdinnan ja johtopäätöksen niin, että toinen voi toistaa tutkimuksen.
