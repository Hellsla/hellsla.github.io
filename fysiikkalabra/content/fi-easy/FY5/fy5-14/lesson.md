# Ääni aaltona: korkeus, sointiväri ja Dopplerin ilmiö

> **Miksi** ohi ajavan ambulanssin sireeni kuulostaa madaltuvan juuri ohitushetkellä, vaikka sireeni itse soi koko ajan samalla tavalla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kaupungin katu kesäpäivänä. Valkoinen ambulanssi, jonka katolla palaa sininen hälytysvalo, ajaa kadulla vasemmalta oikealle. Oikealla jalkakäytävällä suojatien vieressä seisoo jalankulkija, jonka ohi ambulanssi on juuri ajamassa. Taustalla on taloja ja koivu." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy514h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="420" fill="url(#fy514h-sky)"/>
  <path d="M148,126 Q146.5,99 178.5,102 Q191,73 223,83 Q252,67 268,97 Q297,100.5 293.5,126 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M806,92 Q805,71.5 829,74 Q838.5,52.5 862.5,59.5 Q884,47.5 896,70.5 Q917.5,73 915,92 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="60" y="250" width="220" height="170" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <path d="M46,250 L170,144.5 L294,250 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="91" y="297.5" width="57" height="51" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="187.5" y="318" width="53" height="102" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="760" y="230" width="260" height="190" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M746,230 L890,112 L1034,230 Z" fill="#8a96a3" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="796.5" y="283" width="67.5" height="57" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="911" y="306" width="62.5" height="114" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="373" y="190" width="14" height="230" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="373" y="392.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="380" y="365" width="7" height="3.5" fill="#1f2933"/>
  <rect x="373" y="337" width="7" height="3.5" fill="#1f2933"/>
  <rect x="380" y="309.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="373" y="282" width="7" height="3.5" fill="#1f2933"/>
  <rect x="380" y="254.5" width="7" height="3.5" fill="#1f2933"/>
  <rect x="373" y="227" width="7" height="3.5" fill="#1f2933"/>
  <line x1="380" y1="277.5" x2="338.5" y2="250" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="380" y1="247.5" x2="421.5" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="380" y1="224.5" x2="338.5" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="380" cy="201.5" r="46" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="345.5" cy="236" r="37" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="414.5" cy="231.5" r="39" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="380" cy="254.5" r="34.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="1104" y="220" width="12" height="200" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1104" y="396" width="6" height="3" fill="#1f2933"/>
  <rect x="1110" y="372" width="6" height="3" fill="#1f2933"/>
  <rect x="1104" y="348" width="6" height="3" fill="#1f2933"/>
  <rect x="1110" y="324" width="6" height="3" fill="#1f2933"/>
  <rect x="1104" y="300" width="6" height="3" fill="#1f2933"/>
  <rect x="1110" y="276" width="6" height="3" fill="#1f2933"/>
  <rect x="1104" y="252" width="6" height="3" fill="#1f2933"/>
  <line x1="1110" y1="296" x2="1074" y2="272" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1110" y1="270" x2="1146" y2="246" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1110" y1="250" x2="1074" y2="226" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1110" cy="230" r="40" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1080" cy="260" r="32" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1140" cy="256" r="34" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1110" cy="276" r="30" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="0" y="420" width="1200" height="40" fill="#f1dfb5"/>
  <line x1="0" y1="460" x2="1200" y2="460" stroke="#a97a35" stroke-width="4" stroke-linecap="butt"/>
  <rect x="0" y="462" width="1200" height="138" fill="#6c757d"/>
  <rect x="860" y="476" width="140" height="10" fill="#ffffff" fill-opacity="0.9"/>
  <rect x="860" y="496" width="140" height="10" fill="#ffffff" fill-opacity="0.9"/>
  <rect x="860" y="516" width="140" height="10" fill="#ffffff" fill-opacity="0.9"/>
  <rect x="860" y="536" width="140" height="10" fill="#ffffff" fill-opacity="0.9"/>
  <rect x="860" y="556" width="140" height="10" fill="#ffffff" fill-opacity="0.9"/>
  <rect x="860" y="576" width="140" height="10" fill="#ffffff" fill-opacity="0.9"/>
  <rect x="40" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <rect x="190" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <rect x="340" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <rect x="490" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <rect x="640" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <rect x="790" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <rect x="940" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <rect x="1090" y="586" width="80" height="6" fill="#ffffff" fill-opacity="0.8"/>
  <path d="M360,568 V418 Q360,400 378,400 H660 L720,458 Q740,468 740,488 V568 Z" fill="#ffffff" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <rect x="364" y="498" width="372" height="22" fill="#ffc078"/>
  <path d="M666,412 L712,460 H666 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="400" y="428" width="90" height="52" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="520" y="428" width="90" height="52" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="556" y="508" width="18" height="46" fill="#1971c2" fill-opacity="0.9"/>
  <rect x="542" y="524" width="46" height="16" fill="#1971c2" fill-opacity="0.9"/>
  <rect x="480" y="378" width="70" height="22" rx="6" fill="#1971c2" stroke="#1f2933" stroke-width="3"/>
  <circle cx="515" cy="372" r="34" fill="#d0e6fb" fill-opacity="0.55"/>
  <circle cx="440" cy="568" r="34" fill="#1f2933"/>
  <circle cx="440" cy="568" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="660" cy="568" r="34" fill="#1f2933"/>
  <circle cx="660" cy="568" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="728" y="528" width="18" height="14" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <path d="M1010,337 L995.5,447.5" fill="none" stroke="#1f2933" stroke-width="21.6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M981,452 h31.5" fill="none" stroke="#6c757d" stroke-width="11.52" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M985.5,221.5 Q1039,200 1031.5,265 L1027.5,344 H984 Z" fill="#1971c2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1010,337 L1024.5,447.5" fill="none" stroke="#1f2933" stroke-width="21.6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1036,452 h31.5" fill="none" stroke="#6c757d" stroke-width="11.52" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1016,236 L1041.5,301" fill="none" stroke="#1971c2" stroke-width="17.28" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1043" cy="306.5" r="8.64" fill="#f1dfb5"/>
  <rect x="1007" y="193" width="14.5" height="21.5" fill="#f1dfb5"/>
  <circle cx="1014.5" cy="174" r="24.48" fill="#f1dfb5"/>
  <path d="M990,178.5 Q988.5,146.5 1016,148 Q1039,149.5 1039,167 Q1014.5,161 990,178.5 Z" fill="#1f2933" stroke-linejoin="round"/>
</svg>

## Ydinajatus

### Ääni on pitkittäinen paineaalto
Kaiuttimen kalvo tai kitaran kieli värähtelee. Se työntää ilman hiukkasia vuorotellen eteen ja taakse. Hiukkaset eivät kulje äänen mukana. Ne värähtelevät paikoillaan samaan suuntaan, johon aalto etenee. Tällainen aalto on pitkittäinen aalto, ja ääni ilmassa on sellainen (luku *Aaltojen synty ja eteneminen*). Kohtaan, johon hiukkaset tiivistyvät, syntyy tihentymä. Siinä paine on hieman suurempi kuin normaali ilmanpaine $p_0$. Tihentymien väliin jää harvennus, jossa paine on pienempi. Paineen vaihtelu on pientä. Tavallisessa puheessa se on noin $0{,}02\,\text{Pa}$, kun ilmanpaine on noin $101\,\text{kPa}$. Ääni tarvitsee väliaineen. Väliaine voi olla kaasu, neste tai kiinteä aine. Tyhjiössä ääni ei etene.

<svg data-fig="pitkittainen" viewBox="0 0 600 356" role="img" aria-label="Kaavakuva, ei mittakaavassa. Ylhäällä vasemmalla kaiutin, jonka edessä on ilmaa putkessa. Ilman hiukkaset on piirretty sinisinä pisteinä, ja ne ovat paikoin tiheässä ja paikoin harvassa: tiheät kohdat ovat tihentymiä ja harvat harvennuksia. Hiukkaset värähtelevät edestakaisin aallon etenemissuunnassa, mitä esittää pieni kaksipäinen nuoli, ja aalto etenee oikealle, mitä esittää sininen nuoli. Alhaalla on saman hetken paine paikan funktiona: käyrä vaihtelee normaalin ilmanpaineen p0 molemmin puolin, ja sen huiput ovat tihentymien kohdalla. Kahden vierekkäisen tihentymän etäisyys on aallonpituus lambda." style="max-width:100%;font-size:24px">
  <rect x="86" y="70" width="470" height="68" fill="#eef5f9"/>
  <circle cx="99" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="99" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="99" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="99" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="107.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="107.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="107.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="107.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="115.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="115.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="115.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="115.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="122.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="122.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="122.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="122.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="129" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="129" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="129" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="129" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="136" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="136" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="136" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="136" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="142.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="142.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="142.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="142.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="149.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="149.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="149.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="149.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="157.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="157.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="157.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="157.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="165.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="165.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="165.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="165.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="175" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="175" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="175" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="175" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="185.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="185.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="185.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="185.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="196.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="196.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="196.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="196.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="208" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="208" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="208" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="208" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="220" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="220" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="220" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="220" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="232" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="232" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="232" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="232" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="244.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="244.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="244.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="244.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="256" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="256" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="256" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="256" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="267" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="267" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="267" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="267" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="277.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="277.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="277.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="277.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="287" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="287" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="287" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="287" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="295.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="295.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="295.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="295.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="303.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="303.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="303.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="303.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="310.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="310.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="310.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="310.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="317" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="317" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="317" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="317" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="324" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="324" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="324" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="324" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="330.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="330.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="330.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="330.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="337.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="337.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="337.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="337.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="345.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="345.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="345.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="345.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="353.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="353.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="353.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="353.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="363" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="363" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="363" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="363" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="373.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="373.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="373.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="373.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="384.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="384.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="384.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="384.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="396" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="396" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="396" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="396" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="408" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="408" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="408" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="408" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="420" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="420" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="420" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="420" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="432.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="432.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="432.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="432.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="444" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="444" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="444" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="444" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="455" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="455" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="455" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="455" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="465.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="465.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="465.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="465.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="475" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="475" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="475" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="475" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="483.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="483.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="483.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="483.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="491.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="491.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="491.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="491.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="498.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="498.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="498.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="498.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="505" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="505" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="505" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="505" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="512" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="512" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="512" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="512" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="518.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="518.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="518.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="518.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="525.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="525.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="525.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="525.5" cy="134" r="3.6" fill="#2f74b5"/>
  <circle cx="533.5" cy="74" r="3.6" fill="#2f74b5"/>
  <circle cx="533.5" cy="91" r="3.6" fill="#2f74b5"/>
  <circle cx="533.5" cy="108" r="3.6" fill="#2f74b5"/>
  <circle cx="533.5" cy="125" r="3.6" fill="#2f74b5"/>
  <circle cx="541.5" cy="83" r="3.6" fill="#2f74b5"/>
  <circle cx="541.5" cy="100" r="3.6" fill="#2f74b5"/>
  <circle cx="541.5" cy="117" r="3.6" fill="#2f74b5"/>
  <circle cx="541.5" cy="134" r="3.6" fill="#2f74b5"/>
  <line x1="86" y1="70" x2="556" y2="70" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="86" y1="138" x2="556" y2="138" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="43.5" y="88.5" width="15.5" height="31" rx="2" fill="#1f2933"/>
  <path d="M59,88.5 L80,70 V138 L59,119.5 Z" fill="#8a96a3" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="73" y="33.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymä}$</div></foreignObject>
  <foreignObject x="261" y="33.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymä}$</div></foreignObject>
  <foreignObject x="449" y="33.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymä}$</div></foreignObject>
  <foreignObject x="167" y="145.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{harvennus}$</div></foreignObject>
  <line x1="327" y1="160" x2="308" y2="160" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M299,160 L309,155.5 L309,164.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="305" y1="160" x2="324" y2="160" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M333,160 L323,164.5 L323,155.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="455" y1="160" x2="506" y2="160" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M519,160 L505,166.5 L505,153.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="420.5" y="173.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eteneminen}$</div></foreignObject>
  <line x1="85" y1="262" x2="566" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M578,262 L565,268 L565,256 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="86" y1="326" x2="86" y2="204" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M86,192 L92,205 L80,205 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="86" y1="262" x2="556" y2="262" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="86,262 89,257.5 92,253 95,248.5 98,244.5 100.5,240.5 103.5,236.5 106.5,233 109.5,229.5 112.5,226.5 115.5,224 118.5,221.5 121,219.5 124,218 127,217 130,216 133,216 136,216 139,217 142,218 145,219.5 147.5,221.5 150.5,224 153.5,226.5 156.5,229.5 159.5,233 162.5,236.5 165.5,240.5 168,244.5 171,248.5 174,253 177,257.5 180,262 183,266.5 186,271 189,275.5 192,279.5 194.5,283.5 197.5,287.5 200.5,291 203.5,294.5 206.5,297.5 209.5,300 212.5,302.5 215,304.5 218,306 221,307 224,308 227,308 230,308 233,307 236,306 239,304.5 241.5,302.5 244.5,300 247.5,297.5 250.5,294.5 253.5,291 256.5,287.5 259.5,283.5 262,279.5 265,275.5 268,271 271,266.5 274,262 277,257.5 280,253 283,248.5 286,244.5 288.5,240.5 291.5,236.5 294.5,233 297.5,229.5 300.5,226.5 303.5,224 306.5,221.5 309,219.5 312,218 315,217 318,216 321,216 324,216 327,217 330,218 333,219.5 335.5,221.5 338.5,224 341.5,226.5 344.5,229.5 347.5,233 350.5,236.5 353.5,240.5 356,244.5 359,248.5 362,253 365,257.5 368,262 371,266.5 374,271 377,275.5 380,279.5 382.5,283.5 385.5,287.5 388.5,291 391.5,294.5 394.5,297.5 397.5,300 400.5,302.5 403,304.5 406,306 409,307 412,308 415,308 418,308 421,307 424,306 427,304.5 429.5,302.5 432.5,300 435.5,297.5 438.5,294.5 441.5,291 444.5,287.5 447.5,283.5 450,279.5 453,275.5 456,271 459,266.5 462,262 465,257.5 468,253 471,248.5 474,244.5 476.5,240.5 479.5,236.5 482.5,233 485.5,229.5 488.5,226.5 491.5,224 494.5,221.5 497,219.5 500,218 503,217 506,216 509,216 512,216 515,217 518,218 521,219.5 523.5,221.5 526.5,224 529.5,226.5 532.5,229.5 535.5,233 538.5,236.5 541.5,240.5 544,244.5 547,248.5 550,253 553,257.5 556,262" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="56" y="163.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="43" y="247.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p_0$</div></foreignObject>
  <foreignObject x="584" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <line x1="133" y1="212" x2="133" y2="142" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <line x1="321" y1="212" x2="321" y2="142" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <path d="M133,316 V324 H321 V316" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="217" y="329.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
</svg>

Kahden peräkkäisen tihentymän etäisyys on aallonpituus $\lambda$. Kaikille aalloille pätee sama: äänen nopeus on $v = f\lambda$, missä $f$ on taajuus (luku *Aaltojen synty ja eteneminen*). Kun ääni siirtyy aineesta toiseen, sen taajuus pysyy samana. Rajapinnan hiukkaset värähtelevät nimittäin samaan tahtiin kuin tuleva aalto. Nopeus ja aallonpituus sen sijaan muuttuvat.

### Äänen nopeus
Äänen nopeus riippuu väliaineesta. Ääni etenee nopeammin, kun aine puristuu huonosti kokoon ja sen tiheys on pieni. Vesi on paljon tiheämpää kuin ilma. Se puristuu kuitenkin niin huonosti kokoon, että ääni kulkee vedessä yli nelinkertaisella nopeudella ilmaan verrattuna. Kaasussa nopeus kasvaa, kun lämpötila nousee. Silloin hiukkaset liikkuvat nopeammin ja välittävät painevaihtelun nopeammin eteenpäin. Ilmassa nopeus kasvaa noin $0{,}6\,\text{m/s}$ jokaista celsiusastetta kohti. Tässä luvussa ilmalle käytetään arvoa $v = 340\,\text{m/s}$. Se vastaa noin $15\,{}^\circ\text{C}$:n lämpötilaa, kuten aiemmissa luvuissa.

| Väliaine | $v$ (m/s) |
| --- | --- |
| ilma, $0\,{}^\circ\text{C}$ | 331 |
| ilma, $15\,{}^\circ\text{C}$ | 340 |
| ilma, $20\,{}^\circ\text{C}$ | 343 |
| vesi, $20\,{}^\circ\text{C}$ | 1480 |
| teräs | noin 5900 |

### Äänen nopeuden määrittäminen
Äänen nopeus määritetään mittaamalla, kuinka kauan ääni kulkee tunnetun matkan. Kaikumenetelmässä lyödään kaksi puukapulaa yhteen etäisyydellä $d$ seinästä. Sitten mitataan aika $t$, jonka kuluttua kaiku palaa. Ääni kulkee seinään ja takaisin eli matkan $2d$, joten $v = \tfrac{2d}{t}$. Tarkempi tapa käyttää kahta mikrofonia. Ne ovat etäisyydellä $d$ toisistaan samalla suoralla äänilähteen kanssa. Mittausohjelma tallentaa molempien mikrofonien signaalit. Äänen saapumisaikojen ero $\Delta t$ luetaan kuvaajasta, ja silloin $v = \tfrac{d}{\Delta t}$. Kolmas tapa on resonanssiputki. Siinä aallonpituus saadaan seisovan aallon pituudesta (luku *Seisova aalto: solmut, kuvut ja ominaistaajuudet*).

### Äänenkorkeus ja kuuloalue
Äänenkorkeus määräytyy taajuudesta. Mitä suurempi taajuus on, sitä korkeampi ääni on. Kun taajuus kaksinkertaistuu, ääni nousee oktaavin. Esimerkiksi viritysääni a on $440\,\text{Hz}$ ja oktaavia ylempi a on $880\,\text{Hz}$. Nuori ihminen kuulee taajuuksia noin $20\,\text{Hz}$:stä noin $20\,\text{kHz}$:iin. Ylin kuultava taajuus laskee iän myötä. Kuuloalueen äänten aallonpituudet ovat ilmassa noin $17\,\text{m}$:stä $1{,}7\,\text{cm}$:iin. Kuuloaluetta matalampi ääni on infraääntä ja korkeampi ääni on ultraääntä. Ne ovat samanlaisia pitkittäisiä aaltoja kuin kuultava ääni. Ihmisen korva ei kuitenkaan aisti niitä.

<svg data-fig="alueet" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva: taajuusasteikko logaritmisena yhdestä hertsistä kymmeneen miljoonaan hertsiin, jokainen kymmenkertaistus yhtä pitkänä välinä. Alle 20 hertsin taajuudet ovat infraääntä, 20 hertsistä 20 kilohertsiin on ihmisen kuuloalue ja yli 20 kilohertsin taajuudet ovat ultraääntä. Asteikon yläpuolelle on merkitty esimerkkejä: maanjäristys noin yhden hertsin kohdalla, norsujen matalat äänet noin 15 hertsin kohdalla, puhe muutamasta sadasta hertsistä muutamaan kilohertsiin, lepakon kaikuluotaus noin 50 kilohertsin kohdalla ja ultraäänikuvaus noin kolmen megahertsin kohdalla." style="max-width:100%;font-size:24px">
  <rect x="36" y="166" width="83.5" height="30" fill="#a5d8ff" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="119.5" y="166" width="192" height="30" fill="#b2f2bb" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="311.5" y="166" width="172.5" height="30" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="35" y1="196" x2="496" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M508,196 L495,202 L495,190 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="36" y1="196" x2="36" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="100" y1="196" x2="100" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="83.5" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="164" y1="196" x2="164" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="141.5" y="205.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^2$</div></foreignObject>
  <line x1="228" y1="196" x2="228" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="205.5" y="205.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^3$</div></foreignObject>
  <line x1="292" y1="196" x2="292" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="269.5" y="205.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^4$</div></foreignObject>
  <line x1="356" y1="196" x2="356" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="205.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^5$</div></foreignObject>
  <line x1="420" y1="196" x2="420" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="397.5" y="205.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^6$</div></foreignObject>
  <line x1="484" y1="196" x2="484" y2="203" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="461.5" y="205.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^7$</div></foreignObject>
  <foreignObject x="514" y="181.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$f\ (\text{Hz})$</div></foreignObject>
  <foreignObject x="17.5" y="241.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{infraääni}$</div></foreignObject>
  <foreignObject x="155.5" y="241.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuloalue}$</div></foreignObject>
  <foreignObject x="337.5" y="241.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ultraääni}$</div></foreignObject>
  <line x1="119.5" y1="166" x2="119.5" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="84.5" y="125.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{Hz}$</div></foreignObject>
  <line x1="311.5" y1="166" x2="311.5" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="125.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kHz}$</div></foreignObject>
  <line x1="36" y1="48" x2="36" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="36" cy="181" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="30" y="19.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{maanjäristys}$</div></foreignObject>
  <line x1="111.5" y1="96" x2="111.5" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="111.5" cy="181" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="76.5" y="67.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{norsu}$</div></foreignObject>
  <line x1="233" y1="48" x2="233" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="233" cy="181" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="204" y="19.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{puhe}$</div></foreignObject>
  <line x1="336.5" y1="96" x2="336.5" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="336.5" cy="181" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="289" y="67.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lepakko}$</div></foreignObject>
  <line x1="450.5" y1="48" x2="450.5" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="450.5" cy="181" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="377" y="19.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ultraäänikuvaus}$</div></foreignObject>
</svg>

Infraääntä syntyy esimerkiksi maanjäristyksissä, ukkosessa ja tulivuorenpurkauksissa. Myös norsut viestivät osin infraäänellä. Infraääni vaimenee ilmassa vähän, joten se voi kulkea satoja kilometrejä. Lepakot ja delfiinit käyttävät ultraääntä kaikuluotaukseen. Lyhyt aallonpituus heijastuu pienistäkin kohteista, kuten hyönteisistä. Tekniikassa ultraääntä käytetään esimerkiksi pesulaitteissa, materiaalien vikojen etsimisessä ja veneiden kaikuluotaimissa. Lääketieteen ultraäänikuvaukseen palataan myöhemmin tällä kurssilla. Äänen voimakkuutta ja desibelejä käsitellään luvussa *Intensiteetti ja desibeliasteikko*.

### Sointiväri ja harmoninen sarja
Huilu, viulu ja laulaja voivat tuottaa saman sävelen, ja silti ne kuulostavat erilaisilta. Ero on äänen sointivärissä. Soittimen kieli tai ilmapatsas värähtelee yhtä aikaa monella ominaistaajuudella (luku *Seisova aalto: solmut, kuvut ja ominaistaajuudet*). Alin niistä on perustaajuus $f_1$. Sitä suuremmat taajuudet ovat yläsäveliä. Kielessä ja molemmista päistä avoimessa putkessa yläsävelet ovat perustaajuuden kokonaislukukertoja. Nämä taajuudet muodostavat harmonisen sarjan
```latex
f_n = n f_1, \quad n = 1, 2, 3, \ldots
```
missä $f_n$ on sarjan $n$:s taajuus (Hz) ja $f_1$ on perustaajuus (Hz). Äänenkorkeuden kuulemme perustaajuudesta. Sointiväri riippuu siitä, kuinka voimakkaita yläsävelet ovat perustaajuuteen verrattuna. Äänirauta tuottaa lähes puhtaan siniaallon, jossa on vain perustaajuus.

<svg data-fig="sointi" viewBox="0 0 600 372" role="img" aria-label="Kaavakuva kahdesta äänestä, joilla on sama perustaajuus 220 hertsiä. Ylhäällä äänirauta, alhaalla kitara. Vasemmalla paine ajan funktiona: ääniraudan käyrä on siniaalto, kitaran käyrä on mutkikkaampi, mutta kummankin käyrän jaksonaika T on sama. Oikealla kummankin äänen spektri eli FFT-kuvaaja: äänirauralla on yksi piikki 220 hertsin kohdalla, kitaralla piikit 220, 440, 660, 880 ja 1100 hertsin kohdalla eli perustaajuuden monikerroilla, ja piikit pienenevät taajuuden kasvaessa." style="max-width:100%;font-size:24px">
  <foreignObject x="171" y="7.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p(t)$</div></foreignObject>
  <foreignObject x="377.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{spektri}$</div></foreignObject>
  <foreignObject x="16" y="31.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{äänirauta}$</div></foreignObject>
  <line x1="99" y1="116" x2="308" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M318,116 L307,121 L307,111 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="160" x2="100" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M100,66 L105,77 L95,77 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="322" y="101.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <polyline points="100,116 100.5,114 101.5,111.5 102,109.5 102.5,107.5 103,105.5 104,103.5 104.5,101.5 105,99.5 105.5,98 106.5,96 107,94.5 107.5,92.5 108,91 109,90 109.5,88.5 110,87.5 111,86 111.5,85 112,84.5 112.5,83.5 113.5,83 114,82.5 114.5,82.5 115,82 116,82 116.5,82 117,82.5 117.5,82.5 118.5,83 119,83.5 119.5,84.5 120.5,85 121,86 121.5,87.5 122,88.5 123,90 123.5,91 124,92.5 124.5,94.5 125.5,96 126,98 126.5,99.5 127,101.5 128,103.5 128.5,105.5 129,107.5 130,109.5 130.5,111.5 131,114 131.5,116 132.5,118 133,120.5 133.5,122.5 134,124.5 135,126.5 135.5,128.5 136,130.5 136.5,132.5 137.5,134 138,136 138.5,137.5 139.5,139.5 140,141 140.5,142 141,143.5 142,144.5 142.5,146 143,147 143.5,147.5 144.5,148.5 145,149 145.5,149.5 146,149.5 147,150 147.5,150 148,150 149,149.5 149.5,149.5 150,149 150.5,148.5 151.5,147.5 152,147 152.5,146 153,144.5 154,143.5 154.5,142 155,141 155.5,139.5 156.5,137.5 157,136 157.5,134 158.5,132.5 159,130.5 159.5,128.5 160,126.5 161,124.5 161.5,122.5 162,120.5 162.5,118 163.5,116 164,114 164.5,111.5 165,109.5 166,107.5 166.5,105.5 167,103.5 168,101.5 168.5,99.5 169,98 169.5,96 170.5,94.5 171,92.5 171.5,91 172,90 173,88.5 173.5,87.5 174,86 174.5,85 175.5,84.5 176,83.5 176.5,83 177.5,82.5 178,82.5 178.5,82 179,82 180,82 180.5,82.5 181,82.5 181.5,83 182.5,83.5 183,84.5 183.5,85 184,86 185,87.5 185.5,88.5 186,90 187,91 187.5,92.5 188,94.5 188.5,96 189.5,98 190,99.5 190.5,101.5 191,103.5 192,105.5 192.5,107.5 193,109.5 193.5,111.5 194.5,114 195,116 195.5,118 196.5,120.5 197,122.5 197.5,124.5 198,126.5 199,128.5 199.5,130.5 200,132.5 200.5,134 201.5,136 202,137.5 202.5,139.5 203,141 204,142 204.5,143.5 205,144.5 206,146 206.5,147 207,147.5 207.5,148.5 208.5,149 209,149.5 209.5,149.5 210,150 211,150 211.5,150 212,149.5 212.5,149.5 213.5,149 214,148.5 214.5,147.5 215.5,147 216,146 216.5,144.5 217,143.5 218,142 218.5,141 219,139.5 219.5,137.5 220.5,136 221,134 221.5,132.5 222,130.5 223,128.5 223.5,126.5 224,124.5 225,122.5 225.5,120.5 226,118 226.5,116 227.5,114 228,111.5 228.5,109.5 229,107.5 230,105.5 230.5,103.5 231,101.5 231.5,99.5 232.5,98 233,96 233.5,94.5 234.5,92.5 235,91 235.5,90 236,88.5 237,87.5 237.5,86 238,85 238.5,84.5 239.5,83.5 240,83 240.5,82.5 241,82.5 242,82 242.5,82 243,82 244,82.5 244.5,82.5 245,83 245.5,83.5 246.5,84.5 247,85 247.5,86 248,87.5 249,88.5 249.5,90 250,91 250.5,92.5 251.5,94.5 252,96 252.5,98 253.5,99.5 254,101.5 254.5,103.5 255,105.5 256,107.5 256.5,109.5 257,111.5 257.5,114 258.5,116 259,118 259.5,120.5 260,122.5 261,124.5 261.5,126.5 262,128.5 263,130.5 263.5,132.5 264,134 264.5,136 265.5,137.5 266,139.5 266.5,141 267,142 268,143.5 268.5,144.5 269,146 269.5,147 270.5,147.5 271,148.5 271.5,149 272.5,149.5 273,149.5 273.5,150 274,150 275,150 275.5,149.5 276,149.5 276.5,149 277.5,148.5 278,147.5 278.5,147 279,146 280,144.5 280.5,143.5 281,142 282,141 282.5,139.5 283,137.5 283.5,136 284.5,134 285,132.5 285.5,130.5 286,128.5 287,126.5 287.5,124.5 288,122.5 288.5,120.5 289.5,118 290,116" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="163.5" y1="154" x2="163.5" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="226.5" y1="154" x2="226.5" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M163.5,168 H226.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="185" y="169.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="412.5" y1="150" x2="412.5" y2="80" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="475" y1="150" x2="475" y2="80" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="349" y1="150" x2="504" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M514,150 L503,155 L503,145 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="350" y1="151" x2="350" y2="74" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M350,64 L355,75 L345,75 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="374.5" y="80" width="6" height="70" fill="#e8590c"/>
  <line x1="412.5" y1="150" x2="412.5" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="390" y="159.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="475" y1="150" x2="475" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="446" y="159.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1000$</div></foreignObject>
  <foreignObject x="518" y="135.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$f\ (\text{Hz})$</div></foreignObject>
  <foreignObject x="16" y="203.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kitara}$</div></foreignObject>
  <line x1="99" y1="288" x2="308" y2="288" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M318,288 L307,293 L307,283 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="332" x2="100" y2="248" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M100,238 L105,249 L95,249 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="322" y="273.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <polyline points="100,270.5 100.5,268 101.5,266.5 102,265.5 102.5,265 103,265.5 104,266.5 104.5,267.5 105,269.5 105.5,271 106.5,273 107,274.5 107.5,276 108,276.5 109,277.5 109.5,277.5 110,277 111,276.5 111.5,276 112,275 112.5,274 113.5,273 114,272.5 114.5,272.5 115,272.5 116,273 116.5,273.5 117,274.5 117.5,276 118.5,277.5 119,279 119.5,280.5 120.5,281.5 121,282.5 121.5,283 122,283.5 123,283.5 123.5,283 124,282.5 124.5,282 125.5,281 126,280.5 126.5,280 127,279.5 128,279.5 128.5,280 129,281 130,282 130.5,283 131,284.5 131.5,286.5 132.5,288 133,289.5 133.5,290.5 134,291.5 135,292 135.5,292.5 136,292.5 136.5,292 137.5,291.5 138,291 138.5,290 139.5,289.5 140,289 140.5,288.5 141,289 142,289.5 142.5,290 143,291.5 143.5,293 144.5,295 145,297.5 145.5,300 146,302.5 147,305.5 147.5,308 148,310.5 149,313 149.5,315.5 150,317.5 150.5,319 151.5,320.5 152,321.5 152.5,322 153,322 154,321.5 154.5,320.5 155,319 155.5,317 156.5,314.5 157,311.5 157.5,308 158.5,304 159,299.5 159.5,295 160,290 161,285.5 161.5,281 162,277 162.5,273.5 163.5,270.5 164,268 164.5,266.5 165,265.5 166,265 166.5,265.5 167,266.5 168,267.5 168.5,269.5 169,271 169.5,273 170.5,274.5 171,276 171.5,276.5 172,277.5 173,277.5 173.5,277 174,276.5 174.5,276 175.5,275 176,274 176.5,273 177.5,272.5 178,272.5 178.5,272.5 179,273 180,273.5 180.5,274.5 181,276 181.5,277.5 182.5,279 183,280.5 183.5,281.5 184,282.5 185,283 185.5,283.5 186,283.5 187,283 187.5,282.5 188,282 188.5,281 189.5,280.5 190,280 190.5,279.5 191,279.5 192,280 192.5,281 193,282 193.5,283 194.5,284.5 195,286.5 195.5,288 196.5,289.5 197,290.5 197.5,291.5 198,292 199,292.5 199.5,292.5 200,292 200.5,291.5 201.5,291 202,290 202.5,289.5 203,289 204,288.5 204.5,289 205,289.5 206,290 206.5,291.5 207,293 207.5,295 208.5,297.5 209,300 209.5,302.5 210,305.5 211,308 211.5,310.5 212,313 212.5,315.5 213.5,317.5 214,319 214.5,320.5 215.5,321.5 216,322 216.5,322 217,321.5 218,320.5 218.5,319 219,317 219.5,314.5 220.5,311.5 221,308 221.5,304 222,299.5 223,295 223.5,290 224,285.5 225,281 225.5,277 226,273.5 226.5,270.5 227.5,268 228,266.5 228.5,265.5 229,265 230,265.5 230.5,266.5 231,267.5 231.5,269.5 232.5,271 233,273 233.5,274.5 234.5,276 235,276.5 235.5,277.5 236,277.5 237,277 237.5,276.5 238,276 238.5,275 239.5,274 240,273 240.5,272.5 241,272.5 242,272.5 242.5,273 243,273.5 244,274.5 244.5,276 245,277.5 245.5,279 246.5,280.5 247,281.5 247.5,282.5 248,283 249,283.5 249.5,283.5 250,283 250.5,282.5 251.5,282 252,281 252.5,280.5 253.5,280 254,279.5 254.5,279.5 255,280 256,281 256.5,282 257,283 257.5,284.5 258.5,286.5 259,288 259.5,289.5 260,290.5 261,291.5 261.5,292 262,292.5 263,292.5 263.5,292 264,291.5 264.5,291 265.5,290 266,289.5 266.5,289 267,288.5 268,289 268.5,289.5 269,290 269.5,291.5 270.5,293 271,295 271.5,297.5 272.5,300 273,302.5 273.5,305.5 274,308 275,310.5 275.5,313 276,315.5 276.5,317.5 277.5,319 278,320.5 278.5,321.5 279,322 280,322 280.5,321.5 281,320.5 282,319 282.5,317 283,314.5 283.5,311.5 284.5,308 285,304 285.5,299.5 286,295 287,290 287.5,285.5 288,281 288.5,277 289.5,273.5 290,270.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="163.5" y1="326" x2="163.5" y2="336" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="226.5" y1="326" x2="226.5" y2="336" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M163.5,340 H226.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="185" y="341.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="412.5" y1="322" x2="412.5" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="475" y1="322" x2="475" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="349" y1="322" x2="504" y2="322" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M514,322 L503,327 L503,317 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="350" y1="323" x2="350" y2="246" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M350,236 L355,247 L345,247 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="374.5" y="252" width="6" height="70" fill="#e8590c"/>
  <rect x="402" y="278.5" width="6" height="43.5" fill="#e8590c"/>
  <rect x="429.5" y="292.5" width="6" height="29.5" fill="#e8590c"/>
  <rect x="457" y="305" width="6" height="17" fill="#e8590c"/>
  <rect x="484.5" y="312" width="6" height="10" fill="#e8590c"/>
  <line x1="412.5" y1="322" x2="412.5" y2="328" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="390" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="475" y1="322" x2="475" y2="328" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="446" y="331.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1000$</div></foreignObject>
  <foreignObject x="518" y="307.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$f\ (\text{Hz})$</div></foreignObject>
  <line x1="12" y1="196" x2="588" y2="196" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
</svg>

### FFT-spektri
Mikrofoni mittaa ilmanpaineen vaihtelua ajan funktiona. Mittausohjelma laskee mittaussarjasta äänen spektrin eli FFT-kuvaajan (*Fast Fourier Transform*, nopea Fourier-muunnos). Spektri näyttää, mitä taajuuksia äänessä on ja kuinka voimakkaina ne ovat. Jokainen äänen siniaaltoinen osa näkyy piikkinä omalla taajuudellaan. Luvussa *Aaltojen yhteisvaikutus: superpositio ja interferenssi* monimutkainen aalto koottiin samalla tavalla siniaaltojen summana. Soittimen spektrissä piikit ovat harmonisen sarjan taajuuksilla. Vierekkäisten piikkien väli on siis perustaajuus. Perustaajuus on yleensä myös alimman piikin taajuus. Korkein piikki ei aina ole perustaajuuden kohdalla.

## Kaava: Huojunta ja Dopplerin ilmiö

### Huojunta
Ajatellaan, että kaksi ääntä soi yhtä aikaa. Niiden taajuudet $f_1$ ja $f_2$ eroavat vain vähän. Äänten painevaihtelut summautuvat. Välillä aallot ovat samassa vaiheessa ja vahvistavat toisiaan. Välillä ne ovat vastakkaisissa vaiheissa ja heikentävät toisiaan. Kuulemme yhden äänen. Sen korkeus vastaa taajuuksien keskiarvoa, ja sen voimakkuus vuoroin kasvaa ja heikkenee. Tätä kutsutaan huojunnaksi. Sekunnissa toinen aalto ehtii tehdä $|f_1 - f_2|$ värähdystä enemmän kuin toinen. Joka kerta aallot palaavat samaan vaiheeseen. Voimakkaita hetkiä on siis sekunnissa
```latex
f_\text{h} = |f_1 - f_2|
```
missä $f_\text{h}$ on huojuntataajuus (Hz) ja $f_1$ ja $f_2$ ovat äänten taajuudet (Hz). Kahden voimakkaan hetken väli on huojunnan jaksonaika. Se on $T_\text{h} = \tfrac{1}{f_\text{h}}$.

<svg data-fig="huojunta" viewBox="0 0 600 336" role="img" aria-label="Kaavakuva, ei mittakaavassa: kaksi ääntä, joiden taajuudet f1 ja f2 eroavat vähän, ja niiden summa ajan funktiona. Ylhäällä oranssi aalto ja sen alla violetti aalto, jossa on kuvan aikana kaksi värähdystä enemmän. Alhaalla sininen summa-aalto: sen amplitudi kasvaa ja pienenee vuorotellen katkoviivalla piirretyn verhokäyrän mukaan. Kohdissa, joissa aallot ovat samassa vaiheessa, summa on voimakas, ja kohdissa, joissa ne ovat vastakkaisissa vaiheissa, summa on lähes nolla. Kahden peräkkäisen voimakkaan kohdan väli on huojunnan jaksonaika T h." style="max-width:100%;font-size:24px">
  <line x1="124" y1="44" x2="560" y2="44" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <polyline points="124,24 124.5,24 125.5,24.5 126,25.5 127,26.5 127.5,28 128.5,29.5 129,31.5 130,33.5 130.5,35.5 131.5,38 132,40.5 132.5,42.5 133.5,45.5 134,47.5 135,50 135.5,52.5 136.5,54.5 137,56.5 138,58.5 138.5,60 139.5,61.5 140,62.5 140.5,63.5 141.5,64 142,64 143,64 143.5,63.5 144.5,62.5 145,61.5 146,60 146.5,58.5 147.5,56.5 148,54.5 148.5,52.5 149.5,50 150,47.5 151,45.5 151.5,42.5 152.5,40.5 153,38 154,35.5 154.5,33.5 155,31.5 156,29.5 156.5,28 157.5,26.5 158,25.5 159,24.5 159.5,24 160.5,24 161,24 162,24.5 162.5,25.5 163,26.5 164,28 164.5,29.5 165.5,31.5 166,33.5 167,35.5 167.5,38 168.5,40.5 169,42.5 170,45.5 170.5,47.5 171,50 172,52.5 172.5,54.5 173.5,56.5 174,58.5 175,60 175.5,61.5 176.5,62.5 177,63.5 178,64 178.5,64 179,64 180,63.5 180.5,62.5 181.5,61.5 182,60 183,58.5 183.5,56.5 184.5,54.5 185,52.5 186,50 186.5,47.5 187,45.5 188,42.5 188.5,40.5 189.5,38 190,35.5 191,33.5 191.5,31.5 192.5,29.5 193,28 194,26.5 194.5,25.5 195,24.5 196,24 196.5,24 197.5,24 198,24.5 199,25.5 199.5,26.5 200.5,28 201,29.5 202,31.5 202.5,33.5 203,35.5 204,38 204.5,40.5 205.5,42.5 206,45.5 207,47.5 207.5,50 208.5,52.5 209,54.5 209.5,56.5 210.5,58.5 211,60 212,61.5 212.5,62.5 213.5,63.5 214,64 215,64 215.5,64 216.5,63.5 217,62.5 217.5,61.5 218.5,60 219,58.5 220,56.5 220.5,54.5 221.5,52.5 222,50 223,47.5 223.5,45.5 224.5,42.5 225,40.5 225.5,38 226.5,35.5 227,33.5 228,31.5 228.5,29.5 229.5,28 230,26.5 231,25.5 231.5,24.5 232.5,24 233,24 233.5,24 234.5,24.5 235,25.5 236,26.5 236.5,28 237.5,29.5 238,31.5 239,33.5 239.5,35.5 240.5,38 241,40.5 241.5,42.5 242.5,45.5 243,47.5 244,50 244.5,52.5 245.5,54.5 246,56.5 247,58.5 247.5,60 248.5,61.5 249,62.5 249.5,63.5 250.5,64 251,64 252,64 252.5,63.5 253.5,62.5 254,61.5 255,60 255.5,58.5 256.5,56.5 257,54.5 257.5,52.5 258.5,50 259,47.5 260,45.5 260.5,42.5 261.5,40.5 262,38 263,35.5 263.5,33.5 264,31.5 265,29.5 265.5,28 266.5,26.5 267,25.5 268,24.5 268.5,24 269.5,24 270,24 271,24.5 271.5,25.5 272,26.5 273,28 273.5,29.5 274.5,31.5 275,33.5 276,35.5 276.5,38 277.5,40.5 278,42.5 279,45.5 279.5,47.5 280,50 281,52.5 281.5,54.5 282.5,56.5 283,58.5 284,60 284.5,61.5 285.5,62.5 286,63.5 287,64 287.5,64 288,64 289,63.5 289.5,62.5 290.5,61.5 291,60 292,58.5 292.5,56.5 293.5,54.5 294,52.5 295,50 295.5,47.5 296,45.5 297,42.5 297.5,40.5 298.5,38 299,35.5 300,33.5 300.5,31.5 301.5,29.5 302,28 303,26.5 303.5,25.5 304,24.5 305,24 305.5,24 306.5,24 307,24.5 308,25.5 308.5,26.5 309.5,28 310,29.5 311,31.5 311.5,33.5 312,35.5 313,38 313.5,40.5 314.5,42.5 315,45.5 316,47.5 316.5,50 317.5,52.5 318,54.5 318.5,56.5 319.5,58.5 320,60 321,61.5 321.5,62.5 322.5,63.5 323,64 324,64 324.5,64 325.5,63.5 326,62.5 326.5,61.5 327.5,60 328,58.5 329,56.5 329.5,54.5 330.5,52.5 331,50 332,47.5 332.5,45.5 333.5,42.5 334,40.5 334.5,38 335.5,35.5 336,33.5 337,31.5 337.5,29.5 338.5,28 339,26.5 340,25.5 340.5,24.5 341.5,24 342,24 342.5,24 343.5,24.5 344,25.5 345,26.5 345.5,28 346.5,29.5 347,31.5 348,33.5 348.5,35.5 349.5,38 350,40.5 350.5,42.5 351.5,45.5 352,47.5 353,50 353.5,52.5 354.5,54.5 355,56.5 356,58.5 356.5,60 357.5,61.5 358,62.5 358.5,63.5 359.5,64 360,64 361,64 361.5,63.5 362.5,62.5 363,61.5 364,60 364.5,58.5 365.5,56.5 366,54.5 366.5,52.5 367.5,50 368,47.5 369,45.5 369.5,42.5 370.5,40.5 371,38 372,35.5 372.5,33.5 373,31.5 374,29.5 374.5,28 375.5,26.5 376,25.5 377,24.5 377.5,24 378.5,24 379,24 380,24.5 380.5,25.5 381,26.5 382,28 382.5,29.5 383.5,31.5 384,33.5 385,35.5 385.5,38 386.5,40.5 387,42.5 388,45.5 388.5,47.5 389,50 390,52.5 390.5,54.5 391.5,56.5 392,58.5 393,60 393.5,61.5 394.5,62.5 395,63.5 396,64 396.5,64 397,64 398,63.5 398.5,62.5 399.5,61.5 400,60 401,58.5 401.5,56.5 402.5,54.5 403,52.5 404,50 404.5,47.5 405,45.5 406,42.5 406.5,40.5 407.5,38 408,35.5 409,33.5 409.5,31.5 410.5,29.5 411,28 412,26.5 412.5,25.5 413,24.5 414,24 414.5,24 415.5,24 416,24.5 417,25.5 417.5,26.5 418.5,28 419,29.5 420,31.5 420.5,33.5 421,35.5 422,38 422.5,40.5 423.5,42.5 424,45.5 425,47.5 425.5,50 426.5,52.5 427,54.5 427.5,56.5 428.5,58.5 429,60 430,61.5 430.5,62.5 431.5,63.5 432,64 433,64 433.5,64 434.5,63.5 435,62.5 435.5,61.5 436.5,60 437,58.5 438,56.5 438.5,54.5 439.5,52.5 440,50 441,47.5 441.5,45.5 442.5,42.5 443,40.5 443.5,38 444.5,35.5 445,33.5 446,31.5 446.5,29.5 447.5,28 448,26.5 449,25.5 449.5,24.5 450.5,24 451,24 451.5,24 452.5,24.5 453,25.5 454,26.5 454.5,28 455.5,29.5 456,31.5 457,33.5 457.5,35.5 458.5,38 459,40.5 459.5,42.5 460.5,45.5 461,47.5 462,50 462.5,52.5 463.5,54.5 464,56.5 465,58.5 465.5,60 466.5,61.5 467,62.5 467.5,63.5 468.5,64 469,64 470,64 470.5,63.5 471.5,62.5 472,61.5 473,60 473.5,58.5 474.5,56.5 475,54.5 475.5,52.5 476.5,50 477,47.5 478,45.5 478.5,42.5 479.5,40.5 480,38 481,35.5 481.5,33.5 482,31.5 483,29.5 483.5,28 484.5,26.5 485,25.5 486,24.5 486.5,24 487.5,24 488,24 489,24.5 489.5,25.5 490,26.5 491,28 491.5,29.5 492.5,31.5 493,33.5 494,35.5 494.5,38 495.5,40.5 496,42.5 497,45.5 497.5,47.5 498,50 499,52.5 499.5,54.5 500.5,56.5 501,58.5 502,60 502.5,61.5 503.5,62.5 504,63.5 505,64 505.5,64 506,64 507,63.5 507.5,62.5 508.5,61.5 509,60 510,58.5 510.5,56.5 511.5,54.5 512,52.5 513,50 513.5,47.5 514,45.5 515,42.5 515.5,40.5 516.5,38 517,35.5 518,33.5 518.5,31.5 519.5,29.5 520,28 521,26.5 521.5,25.5 522,24.5 523,24 523.5,24 524.5,24 525,24.5 526,25.5 526.5,26.5 527.5,28 528,29.5 529,31.5 529.5,33.5 530,35.5 531,38 531.5,40.5 532.5,42.5 533,45.5 534,47.5 534.5,50 535.5,52.5 536,54.5 536.5,56.5 537.5,58.5 538,60 539,61.5 539.5,62.5 540.5,63.5 541,64 542,64 542.5,64 543.5,63.5 544,62.5 544.5,61.5 545.5,60 546,58.5 547,56.5 547.5,54.5 548.5,52.5 549,50 550,47.5 550.5,45.5 551.5,42.5 552,40.5 552.5,38 553.5,35.5 554,33.5 555,31.5 555.5,29.5 556.5,28 557,26.5 558,25.5 558.5,24.5 559.5,24 560,24" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="77" y="29.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$f_1$</div></foreignObject>
  <line x1="124" y1="110" x2="560" y2="110" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <polyline points="124,90 124.5,90 125.5,91 126,92 127,93.5 127.5,95 128.5,97.5 129,99.5 130,102 130.5,105 131.5,108 132,111 132.5,113.5 133.5,116.5 134,119.5 135,122 135.5,124 136.5,126 137,127.5 138,128.5 138.5,129.5 139.5,130 140,130 140.5,129.5 141.5,128.5 142,127.5 143,125.5 143.5,123.5 144.5,121.5 145,119 146,116 146.5,113.5 147.5,110.5 148,107.5 148.5,104.5 149.5,102 150,99.5 151,97 151.5,95 152.5,93 153,91.5 154,90.5 154.5,90 155,90 156,90.5 156.5,91 157.5,92 158,93.5 159,95.5 159.5,97.5 160.5,100 161,102.5 162,105.5 162.5,108.5 163,111.5 164,114 164.5,117 165.5,119.5 166,122 167,124.5 167.5,126 168.5,127.5 169,129 170,129.5 170.5,130 171,130 172,129.5 172.5,128.5 173.5,127 174,125.5 175,123.5 175.5,121 176.5,118.5 177,116 178,113 178.5,110 179,107 180,104 180.5,101.5 181.5,99 182,96.5 183,94.5 183.5,93 184.5,91.5 185,90.5 186,90 186.5,90 187,90.5 188,91 188.5,92.5 189.5,94 190,95.5 191,98 191.5,100.5 192.5,103 193,106 194,108.5 194.5,111.5 195,114.5 196,117.5 196.5,120 197.5,122.5 198,124.5 199,126.5 199.5,128 200.5,129 201,129.5 202,130 202.5,130 203,129.5 204,128.5 204.5,127 205.5,125 206,123 207,120.5 207.5,118 208.5,115.5 209,112.5 209.5,109.5 210.5,106.5 211,104 212,101 212.5,98.5 213.5,96.5 214,94.5 215,92.5 215.5,91.5 216.5,90.5 217,90 217.5,90 218.5,90.5 219,91.5 220,92.5 220.5,94 221.5,96 222,98 223,100.5 223.5,103.5 224.5,106.5 225,109 225.5,112 226.5,115 227,118 228,120.5 228.5,122.5 229.5,125 230,126.5 231,128 231.5,129 232.5,130 233,130 233.5,130 234.5,129 235,128 236,126.5 236.5,125 237.5,122.5 238,120.5 239,118 239.5,115 240.5,112 241,109 241.5,106.5 242.5,103.5 243,100.5 244,98 244.5,96 245.5,94 246,92.5 247,91.5 247.5,90.5 248.5,90 249,90 249.5,90.5 250.5,91.5 251,92.5 252,94.5 252.5,96.5 253.5,98.5 254,101 255,104 255.5,106.5 256.5,109.5 257,112.5 257.5,115.5 258.5,118 259,120.5 260,123 260.5,125 261.5,127 262,128.5 263,129.5 263.5,130 264,130 265,129.5 265.5,129 266.5,128 267,126.5 268,124.5 268.5,122.5 269.5,120 270,117.5 271,114.5 271.5,111.5 272,108.5 273,106 273.5,103 274.5,100.5 275,98 276,95.5 276.5,94 277.5,92.5 278,91 279,90.5 279.5,90 280,90 281,90.5 281.5,91.5 282.5,93 283,94.5 284,96.5 284.5,99 285.5,101.5 286,104 287,107 287.5,110 288,113 289,116 289.5,118.5 290.5,121 291,123.5 292,125.5 292.5,127 293.5,128.5 294,129.5 295,130 295.5,130 296,129.5 297,129 297.5,127.5 298.5,126 299,124.5 300,122 300.5,119.5 301.5,117 302,114 303,111.5 303.5,108.5 304,105.5 305,102.5 305.5,100 306.5,97.5 307,95.5 308,93.5 308.5,92 309.5,91 310,90.5 311,90 311.5,90 312,90.5 313,91.5 313.5,93 314.5,95 315,97 316,99.5 316.5,102 317.5,104.5 318,107.5 318.5,110.5 319.5,113.5 320,116 321,119 321.5,121.5 322.5,123.5 323,125.5 324,127.5 324.5,128.5 325.5,129.5 326,130 326.5,130 327.5,129.5 328,128.5 329,127.5 329.5,126 330.5,124 331,122 332,119.5 332.5,116.5 333.5,113.5 334,111 334.5,108 335.5,105 336,102 337,99.5 337.5,97.5 338.5,95 339,93.5 340,92 340.5,91 341.5,90 342,90 342.5,90 343.5,91 344,92 345,93.5 345.5,95 346.5,97.5 347,99.5 348,102 348.5,105 349.5,108 350,111 350.5,113.5 351.5,116.5 352,119.5 353,122 353.5,124 354.5,126 355,127.5 356,128.5 356.5,129.5 357.5,130 358,130 358.5,129.5 359.5,128.5 360,127.5 361,125.5 361.5,123.5 362.5,121.5 363,119 364,116 364.5,113.5 365.5,110.5 366,107.5 366.5,104.5 367.5,102 368,99.5 369,97 369.5,95 370.5,93 371,91.5 372,90.5 372.5,90 373,90 374,90.5 374.5,91 375.5,92 376,93.5 377,95.5 377.5,97.5 378.5,100 379,102.5 380,105.5 380.5,108.5 381,111.5 382,114 382.5,117 383.5,119.5 384,122 385,124.5 385.5,126 386.5,127.5 387,129 388,129.5 388.5,130 389,130 390,129.5 390.5,128.5 391.5,127 392,125.5 393,123.5 393.5,121 394.5,118.5 395,116 396,113 396.5,110 397,107 398,104 398.5,101.5 399.5,99 400,96.5 401,94.5 401.5,93 402.5,91.5 403,90.5 404,90 404.5,90 405,90.5 406,91 406.5,92.5 407.5,94 408,95.5 409,98 409.5,100.5 410.5,103 411,106 412,108.5 412.5,111.5 413,114.5 414,117.5 414.5,120 415.5,122.5 416,124.5 417,126.5 417.5,128 418.5,129 419,129.5 420,130 420.5,130 421,129.5 422,128.5 422.5,127 423.5,125 424,123 425,120.5 425.5,118 426.5,115.5 427,112.5 427.5,109.5 428.5,106.5 429,104 430,101 430.5,98.5 431.5,96.5 432,94.5 433,92.5 433.5,91.5 434.5,90.5 435,90 435.5,90 436.5,90.5 437,91.5 438,92.5 438.5,94 439.5,96 440,98 441,100.5 441.5,103.5 442.5,106.5 443,109 443.5,112 444.5,115 445,118 446,120.5 446.5,122.5 447.5,125 448,126.5 449,128 449.5,129 450.5,130 451,130 451.5,130 452.5,129 453,128 454,126.5 454.5,125 455.5,122.5 456,120.5 457,118 457.5,115 458.5,112 459,109 459.5,106.5 460.5,103.5 461,100.5 462,98 462.5,96 463.5,94 464,92.5 465,91.5 465.5,90.5 466.5,90 467,90 467.5,90.5 468.5,91.5 469,92.5 470,94.5 470.5,96.5 471.5,98.5 472,101 473,104 473.5,106.5 474.5,109.5 475,112.5 475.5,115.5 476.5,118 477,120.5 478,123 478.5,125 479.5,127 480,128.5 481,129.5 481.5,130 482,130 483,129.5 483.5,129 484.5,128 485,126.5 486,124.5 486.5,122.5 487.5,120 488,117.5 489,114.5 489.5,111.5 490,108.5 491,106 491.5,103 492.5,100.5 493,98 494,95.5 494.5,94 495.5,92.5 496,91 497,90.5 497.5,90 498,90 499,90.5 499.5,91.5 500.5,93 501,94.5 502,96.5 502.5,99 503.5,101.5 504,104 505,107 505.5,110 506,113 507,116 507.5,118.5 508.5,121 509,123.5 510,125.5 510.5,127 511.5,128.5 512,129.5 513,130 513.5,130 514,129.5 515,129 515.5,127.5 516.5,126 517,124.5 518,122 518.5,119.5 519.5,117 520,114 521,111.5 521.5,108.5 522,105.5 523,102.5 523.5,100 524.5,97.5 525,95.5 526,93.5 526.5,92 527.5,91 528,90.5 529,90 529.5,90 530,90.5 531,91.5 531.5,93 532.5,95 533,97 534,99.5 534.5,102 535.5,104.5 536,107.5 536.5,110.5 537.5,113.5 538,116 539,119 539.5,121.5 540.5,123.5 541,125.5 542,127.5 542.5,128.5 543.5,129.5 544,130 544.5,130 545.5,129.5 546,128.5 547,127.5 547.5,126 548.5,124 549,122 550,119.5 550.5,116.5 551.5,113.5 552,111 552.5,108 553.5,105 554,102 555,99.5 555.5,97.5 556.5,95 557,93.5 558,92 558.5,91 559.5,90 560,90" fill="none" stroke="#7048e8" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="77" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$f_2$</div></foreignObject>
  <line x1="124" y1="228" x2="560" y2="228" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <polyline points="124,188 125.5,188 127,188 128.5,188 130,188 131.5,188 132.5,188.5 134,188.5 135.5,188.5 137,188.5 138.5,189 140,189 141.5,189.5 143,189.5 144.5,189.5 146,190 147.5,190 148.5,190.5 150,191 151.5,191 153,191.5 154.5,192 156,192 157.5,192.5 159,193 160.5,193.5 162,194 163,194 164.5,194.5 166,195 167.5,195.5 169,196 170.5,196.5 172,197 173.5,197.5 175,198.5 176.5,199 178,199.5 179,200 180.5,200.5 182,201 183.5,202 185,202.5 186.5,203 188,204 189.5,204.5 191,205 192.5,206 194,206.5 195,207.5 196.5,208 198,208.5 199.5,209.5 201,210 202.5,211 204,211.5 205.5,212.5 207,213.5 208.5,214 209.5,215 211,215.5 212.5,216.5 214,217 215.5,218 217,219 218.5,219.5 220,220.5 221.5,221.5 223,222 224.5,223 225.5,224 227,224.5 228.5,225.5 230,226.5 231.5,227 233,228 234.5,227 236,226.5 237.5,225.5 239,224.5 240.5,224 241.5,223 243,222 244.5,221.5 246,220.5 247.5,219.5 249,219 250.5,218 252,217 253.5,216.5 255,215.5 256.5,215 257.5,214 259,213.5 260.5,212.5 262,211.5 263.5,211 265,210 266.5,209.5 268,208.5 269.5,208 271,207.5 272,206.5 273.5,206 275,205 276.5,204.5 278,204 279.5,203 281,202.5 282.5,202 284,201 285.5,200.5 287,200 288,199.5 289.5,199 291,198.5 292.5,197.5 294,197 295.5,196.5 297,196 298.5,195.5 300,195 301.5,194.5 303,194 304,194 305.5,193.5 307,193 308.5,192.5 310,192 311.5,192 313,191.5 314.5,191 316,191 317.5,190.5 318.5,190 320,190 321.5,189.5 323,189.5 324.5,189.5 326,189 327.5,189 329,188.5 330.5,188.5 332,188.5 333.5,188.5 334.5,188 336,188 337.5,188 339,188 340.5,188 342,188 343.5,188 345,188 346.5,188 348,188 349.5,188 350.5,188.5 352,188.5 353.5,188.5 355,188.5 356.5,189 358,189 359.5,189.5 361,189.5 362.5,189.5 364,190 365.5,190 366.5,190.5 368,191 369.5,191 371,191.5 372.5,192 374,192 375.5,192.5 377,193 378.5,193.5 380,194 381,194 382.5,194.5 384,195 385.5,195.5 387,196 388.5,196.5 390,197 391.5,197.5 393,198.5 394.5,199 396,199.5 397,200 398.5,200.5 400,201 401.5,202 403,202.5 404.5,203 406,204 407.5,204.5 409,205 410.5,206 412,206.5 413,207.5 414.5,208 416,208.5 417.5,209.5 419,210 420.5,211 422,211.5 423.5,212.5 425,213.5 426.5,214 427.5,215 429,215.5 430.5,216.5 432,217 433.5,218 435,219 436.5,219.5 438,220.5 439.5,221.5 441,222 442.5,223 443.5,224 445,224.5 446.5,225.5 448,226.5 449.5,227 451,228 452.5,227 454,226.5 455.5,225.5 457,224.5 458.5,224 459.5,223 461,222 462.5,221.5 464,220.5 465.5,219.5 467,219 468.5,218 470,217 471.5,216.5 473,215.5 474.5,215 475.5,214 477,213.5 478.5,212.5 480,211.5 481.5,211 483,210 484.5,209.5 486,208.5 487.5,208 489,207.5 490,206.5 491.5,206 493,205 494.5,204.5 496,204 497.5,203 499,202.5 500.5,202 502,201 503.5,200.5 505,200 506,199.5 507.5,199 509,198.5 510.5,197.5 512,197 513.5,196.5 515,196 516.5,195.5 518,195 519.5,194.5 521,194 522,194 523.5,193.5 525,193 526.5,192.5 528,192 529.5,192 531,191.5 532.5,191 534,191 535.5,190.5 536.5,190 538,190 539.5,189.5 541,189.5 542.5,189.5 544,189 545.5,189 547,188.5 548.5,188.5 550,188.5 551.5,188.5 552.5,188 554,188 555.5,188 557,188 558.5,188 560,188" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="124,268 125.5,268 127,268 128.5,268 130,268 131.5,268 132.5,267.5 134,267.5 135.5,267.5 137,267.5 138.5,267 140,267 141.5,266.5 143,266.5 144.5,266.5 146,266 147.5,266 148.5,265.5 150,265 151.5,265 153,264.5 154.5,264 156,264 157.5,263.5 159,263 160.5,262.5 162,262 163,262 164.5,261.5 166,261 167.5,260.5 169,260 170.5,259.5 172,259 173.5,258.5 175,257.5 176.5,257 178,256.5 179,256 180.5,255.5 182,255 183.5,254 185,253.5 186.5,253 188,252 189.5,251.5 191,251 192.5,250 194,249.5 195,248.5 196.5,248 198,247.5 199.5,246.5 201,246 202.5,245 204,244.5 205.5,243.5 207,242.5 208.5,242 209.5,241 211,240.5 212.5,239.5 214,239 215.5,238 217,237 218.5,236.5 220,235.5 221.5,234.5 223,234 224.5,233 225.5,232 227,231.5 228.5,230.5 230,229.5 231.5,229 233,228 234.5,229 236,229.5 237.5,230.5 239,231.5 240.5,232 241.5,233 243,234 244.5,234.5 246,235.5 247.5,236.5 249,237 250.5,238 252,239 253.5,239.5 255,240.5 256.5,241 257.5,242 259,242.5 260.5,243.5 262,244.5 263.5,245 265,246 266.5,246.5 268,247.5 269.5,248 271,248.5 272,249.5 273.5,250 275,251 276.5,251.5 278,252 279.5,253 281,253.5 282.5,254 284,255 285.5,255.5 287,256 288,256.5 289.5,257 291,257.5 292.5,258.5 294,259 295.5,259.5 297,260 298.5,260.5 300,261 301.5,261.5 303,262 304,262 305.5,262.5 307,263 308.5,263.5 310,264 311.5,264 313,264.5 314.5,265 316,265 317.5,265.5 318.5,266 320,266 321.5,266.5 323,266.5 324.5,266.5 326,267 327.5,267 329,267.5 330.5,267.5 332,267.5 333.5,267.5 334.5,268 336,268 337.5,268 339,268 340.5,268 342,268 343.5,268 345,268 346.5,268 348,268 349.5,268 350.5,267.5 352,267.5 353.5,267.5 355,267.5 356.5,267 358,267 359.5,266.5 361,266.5 362.5,266.5 364,266 365.5,266 366.5,265.5 368,265 369.5,265 371,264.5 372.5,264 374,264 375.5,263.5 377,263 378.5,262.5 380,262 381,262 382.5,261.5 384,261 385.5,260.5 387,260 388.5,259.5 390,259 391.5,258.5 393,257.5 394.5,257 396,256.5 397,256 398.5,255.5 400,255 401.5,254 403,253.5 404.5,253 406,252 407.5,251.5 409,251 410.5,250 412,249.5 413,248.5 414.5,248 416,247.5 417.5,246.5 419,246 420.5,245 422,244.5 423.5,243.5 425,242.5 426.5,242 427.5,241 429,240.5 430.5,239.5 432,239 433.5,238 435,237 436.5,236.5 438,235.5 439.5,234.5 441,234 442.5,233 443.5,232 445,231.5 446.5,230.5 448,229.5 449.5,229 451,228 452.5,229 454,229.5 455.5,230.5 457,231.5 458.5,232 459.5,233 461,234 462.5,234.5 464,235.5 465.5,236.5 467,237 468.5,238 470,239 471.5,239.5 473,240.5 474.5,241 475.5,242 477,242.5 478.5,243.5 480,244.5 481.5,245 483,246 484.5,246.5 486,247.5 487.5,248 489,248.5 490,249.5 491.5,250 493,251 494.5,251.5 496,252 497.5,253 499,253.5 500.5,254 502,255 503.5,255.5 505,256 506,256.5 507.5,257 509,257.5 510.5,258.5 512,259 513.5,259.5 515,260 516.5,260.5 518,261 519.5,261.5 521,262 522,262 523.5,262.5 525,263 526.5,263.5 528,264 529.5,264 531,264.5 532.5,265 534,265 535.5,265.5 536.5,266 538,266 539.5,266.5 541,266.5 542.5,266.5 544,267 545.5,267 547,267.5 548.5,267.5 550,267.5 551.5,267.5 552.5,268 554,268 555.5,268 557,268 558.5,268 560,268" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="124,188 124.5,188.5 125.5,189.5 126,191.5 127,194 127.5,197 128.5,200.5 129,205 130,209.5 130.5,214.5 131.5,219.5 132,225 132.5,230.5 133.5,236 134,241 135,246 135.5,250.5 136.5,254.5 137,258.5 138,261.5 138.5,263.5 139.5,265.5 140,266.5 140.5,267 141.5,266.5 142,265.5 143,263.5 143.5,261 144.5,258 145,254.5 146,250.5 146.5,246 147.5,241 148,236 148.5,231 149.5,226 150,221 151,216 151.5,211.5 152.5,207.5 153,203.5 154,200 154.5,197.5 155,195.5 156,193.5 156.5,193 157.5,192.5 158,193 159,194 159.5,195.5 160.5,198 161,201 162,204 162.5,207.5 163,211.5 164,216 164.5,220.5 165.5,225 166,229.5 167,234 167.5,238 168.5,242 169,245.5 170,249 170.5,251.5 171,254 172,256 172.5,257 173.5,258 174,258 175,257.5 175.5,256.5 176.5,255 177,253 178,251 178.5,248 179,245 180,241.5 180.5,238 181.5,234.5 182,231 183,227 183.5,223.5 184.5,220.5 185,217 186,214.5 186.5,212 187,209.5 188,208 188.5,206.5 189.5,205.5 190,205 191,205 191.5,205.5 192.5,206.5 193,207.5 194,209 194.5,211 195,213 196,215.5 196.5,218 197.5,220.5 198,223 199,226 199.5,228.5 200.5,231 201,233 202,235 202.5,237 203,238.5 204,240 204.5,241 205.5,242 206,242.5 207,242.5 207.5,242.5 208.5,242 209,241 209.5,240.5 210.5,239 211,238 212,236.5 212.5,235 213.5,233.5 214,232 215,230.5 215.5,229 216.5,228 217,226.5 217.5,225.5 218.5,224.5 219,224 220,223 220.5,223 221.5,222.5 222,222.5 223,222.5 223.5,222.5 224.5,223 225,223.5 225.5,224 226.5,224.5 227,225 228,225.5 228.5,226 229.5,226.5 230,227 231,227.5 231.5,228 232.5,228 233,228 233.5,228 234.5,228 235,227.5 236,227 236.5,226.5 237.5,226 238,225.5 239,225 239.5,224.5 240.5,224 241,223.5 241.5,223 242.5,222.5 243,222.5 244,222.5 244.5,222.5 245.5,223 246,223 247,224 247.5,224.5 248.5,225.5 249,226.5 249.5,228 250.5,229 251,230.5 252,232 252.5,233.5 253.5,235 254,236.5 255,238 255.5,239 256.5,240.5 257,241 257.5,242 258.5,242.5 259,242.5 260,242.5 260.5,242 261.5,241 262,240 263,238.5 263.5,237 264,235 265,233 265.5,231 266.5,228.5 267,226 268,223 268.5,220.5 269.5,218 270,215.5 271,213 271.5,211 272,209 273,207.5 273.5,206.5 274.5,205.5 275,205 276,205 276.5,205.5 277.5,206.5 278,208 279,209.5 279.5,212 280,214.5 281,217 281.5,220.5 282.5,223.5 283,227 284,231 284.5,234.5 285.5,238 286,241.5 287,245 287.5,248 288,251 289,253 289.5,255 290.5,256.5 291,257.5 292,258 292.5,258 293.5,257 294,256 295,254 295.5,251.5 296,249 297,245.5 297.5,242 298.5,238 299,234 300,229.5 300.5,225 301.5,220.5 302,216 303,211.5 303.5,207.5 304,204 305,201 305.5,198 306.5,195.5 307,194 308,193 308.5,192.5 309.5,193 310,193.5 311,195.5 311.5,197.5 312,200 313,203.5 313.5,207.5 314.5,211.5 315,216 316,221 316.5,226 317.5,231 318,236 318.5,241 319.5,246 320,250.5 321,254.5 321.5,258 322.5,261 323,263.5 324,265.5 324.5,266.5 325.5,267 326,266.5 326.5,265.5 327.5,263.5 328,261.5 329,258.5 329.5,254.5 330.5,250.5 331,246 332,241 332.5,236 333.5,230.5 334,225 334.5,219.5 335.5,214.5 336,209.5 337,205 337.5,200.5 338.5,197 339,194 340,191.5 340.5,189.5 341.5,188.5 342,188 342.5,188.5 343.5,189.5 344,191.5 345,194 345.5,197 346.5,200.5 347,205 348,209.5 348.5,214.5 349.5,219.5 350,225 350.5,230.5 351.5,236 352,241 353,246 353.5,250.5 354.5,254.5 355,258.5 356,261.5 356.5,263.5 357.5,265.5 358,266.5 358.5,267 359.5,266.5 360,265.5 361,263.5 361.5,261 362.5,258 363,254.5 364,250.5 364.5,246 365.5,241 366,236 366.5,231 367.5,226 368,221 369,216 369.5,211.5 370.5,207.5 371,203.5 372,200 372.5,197.5 373,195.5 374,193.5 374.5,193 375.5,192.5 376,193 377,194 377.5,195.5 378.5,198 379,201 380,204 380.5,207.5 381,211.5 382,216 382.5,220.5 383.5,225 384,229.5 385,234 385.5,238 386.5,242 387,245.5 388,249 388.5,251.5 389,254 390,256 390.5,257 391.5,258 392,258 393,257.5 393.5,256.5 394.5,255 395,253 396,251 396.5,248 397,245 398,241.5 398.5,238 399.5,234.5 400,231 401,227 401.5,223.5 402.5,220.5 403,217 404,214.5 404.5,212 405,209.5 406,208 406.5,206.5 407.5,205.5 408,205 409,205 409.5,205.5 410.5,206.5 411,207.5 412,209 412.5,211 413,213 414,215.5 414.5,218 415.5,220.5 416,223 417,226 417.5,228.5 418.5,231 419,233 420,235 420.5,237 421,238.5 422,240 422.5,241 423.5,242 424,242.5 425,242.5 425.5,242.5 426.5,242 427,241 427.5,240.5 428.5,239 429,238 430,236.5 430.5,235 431.5,233.5 432,232 433,230.5 433.5,229 434.5,228 435,226.5 435.5,225.5 436.5,224.5 437,224 438,223 438.5,223 439.5,222.5 440,222.5 441,222.5 441.5,222.5 442.5,223 443,223.5 443.5,224 444.5,224.5 445,225 446,225.5 446.5,226 447.5,226.5 448,227 449,227.5 449.5,228 450.5,228 451,228 451.5,228 452.5,228 453,227.5 454,227 454.5,226.5 455.5,226 456,225.5 457,225 457.5,224.5 458.5,224 459,223.5 459.5,223 460.5,222.5 461,222.5 462,222.5 462.5,222.5 463.5,223 464,223 465,224 465.5,224.5 466.5,225.5 467,226.5 467.5,228 468.5,229 469,230.5 470,232 470.5,233.5 471.5,235 472,236.5 473,238 473.5,239 474.5,240.5 475,241 475.5,242 476.5,242.5 477,242.5 478,242.5 478.5,242 479.5,241 480,240 481,238.5 481.5,237 482,235 483,233 483.5,231 484.5,228.5 485,226 486,223 486.5,220.5 487.5,218 488,215.5 489,213 489.5,211 490,209 491,207.5 491.5,206.5 492.5,205.5 493,205 494,205 494.5,205.5 495.5,206.5 496,208 497,209.5 497.5,212 498,214.5 499,217 499.5,220.5 500.5,223.5 501,227 502,231 502.5,234.5 503.5,238 504,241.5 505,245 505.5,248 506,251 507,253 507.5,255 508.5,256.5 509,257.5 510,258 510.5,258 511.5,257 512,256 513,254 513.5,251.5 514,249 515,245.5 515.5,242 516.5,238 517,234 518,229.5 518.5,225 519.5,220.5 520,216 521,211.5 521.5,207.5 522,204 523,201 523.5,198 524.5,195.5 525,194 526,193 526.5,192.5 527.5,193 528,193.5 529,195.5 529.5,197.5 530,200 531,203.5 531.5,207.5 532.5,211.5 533,216 534,221 534.5,226 535.5,231 536,236 536.5,241 537.5,246 538,250.5 539,254.5 539.5,258 540.5,261 541,263.5 542,265.5 542.5,266.5 543.5,267 544,266.5 544.5,265.5 545.5,263.5 546,261.5 547,258.5 547.5,254.5 548.5,250.5 549,246 550,241 550.5,236 551.5,230.5 552,225 552.5,219.5 553.5,214.5 554,209.5 555,205 555.5,200.5 556.5,197 557,194 558,191.5 558.5,189.5 559.5,188.5 560,188" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="40" y="213.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{summa}$</div></foreignObject>
  <line x1="123" y1="300" x2="570" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M580,300 L569,305 L569,295 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="586" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <line x1="124" y1="184" x2="124" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <line x1="342" y1="184" x2="342" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <path d="M124,282 V290 H342 V282" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="216.5" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$T_\text{h}$</span></div></foreignObject>
</svg>

Huojuntaa käytetään soittimien virittämiseen. Kun kieltä kiristetään kohti viritysäänen taajuutta, huojunta hidastuu. Huojunta lakkaa, kun taajuudet ovat samat. Huojunta erottuu selvästi, kun taajuusero on enintään noin $10\,\text{Hz}$. Suuremmalla erolla korva kuulee karhean äänen tai kaksi eri ääntä.

<figure class="unit-photo"><img src="pics/fy5/ambulance-panning.webp" alt="Valkoinen ambulanssi ajaa kadulla. Tausta on sumea."><figcaption>Ambulanssi ajaa Torontossa. Kun ambulanssi tulee kohti, sireeni kuulostaa korkeammalta. Kun se menee poispäin, sireeni kuulostaa matalammalta.</figcaption></figure>

### Dopplerin ilmiö, kun lähde liikkuu
Ajatellaan, että äänilähde liikkuu. Jokainen aaltorintama lähtee siitä kohdasta, jossa lähde on sillä hetkellä. Rintama leviää ilmassa nopeudella $v$ joka suuntaan. Lähteen jaksonaika on $T_0 = \tfrac{1}{f_0}$. Sinä aikana edellinen rintama etenee matkan $v T_0$. Lähde ehtii kulkea sen perässä matkan $v_\text{s} T_0$. Lähteen edessä rintamien väli eli aallonpituus on siksi $(v - v_\text{s}) T_0$. Lähteen takana se on $(v + v_\text{s}) T_0$. Paikallaan oleva kuulija kuulee taajuuden $f = \tfrac{v}{\lambda}$, joten
```latex
f = f_0 \cdot \frac{v}{v \mp v_\text{s}}
```
missä $f$ on kuultu taajuus (Hz), $f_0$ on lähteen taajuus (Hz), $v$ on äänen nopeus (m/s) ja $v_\text{s}$ on lähteen nopeus (m/s). Miinusmerkki valitaan, kun lähde lähestyy kuulijaa. Plusmerkki valitaan, kun lähde loittonee.

<svg data-fig="doppler" viewBox="0 0 600 424" role="img" aria-label="Kaavakuva ylhäältä katsottuna, kaksi tilannetta allekkain. Ylhäällä lähde liikkuu oikealle nopeudella, joka on 0,4 kertaa äänen nopeus, mitä esittää sininen nopeusnuoli. Aaltorintamat ovat ympyröitä, jotka ovat lähteneet lähteen aiemmista paikoista, joten ne ovat lähteen edessä tiheässä ja sen takana harvassa. Oikealla olevan kuulijan A suunnassa aallonpituus lambda A on lyhyt ja vasemmalla olevan kuulijan B suunnassa aallonpituus lambda B pitkä. Alhaalla lähde on paikallaan ja aaltorintamat ovat samankeskisiä ympyröitä yhtä suurin välein. Kuulija liikkuu vasemmalle kohti lähdettä, mitä esittää sininen nopeusnuoli; aallonpituus lambda on sama kaikkiin suuntiin." style="max-width:100%;font-size:24px">
  <defs><clipPath id="fy514-clip1"><rect x="26" y="34" width="548" height="140"/></clipPath><clipPath id="fy514-clip2"><rect x="26" y="236" width="548" height="144"/></clipPath></defs>
  <g clip-path="url(#fy514-clip1)"><circle cx="281.5" cy="120" r="46" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="263" cy="120" r="92" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="245" cy="120" r="138" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="226.5" cy="120" r="184" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="208" cy="120" r="230" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="189.5" cy="120" r="276" fill="none" stroke="#6b7480" stroke-width="2"/></g>
  <rect x="280" y="109" width="11" height="21.5" rx="2" fill="#1f2933"/>
  <path d="M291,109 L305.5,96.5 V143.5 L291,131 Z" fill="#8a96a3" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="314" y1="80" x2="363" y2="80" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M376,80 L362,86.5 L362,73.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="384" y="65.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{s}$</div></foreignObject>
  <line x1="566" y1="133" x2="560.5" y2="154" stroke="#1f2933" stroke-width="2.4" stroke-linecap="butt"/>
  <line x1="566" y1="133" x2="571.5" y2="154" stroke="#1f2933" stroke-width="2.4" stroke-linecap="butt"/>
  <rect x="559" y="111" width="14.5" height="24" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="566" cy="103" r="7.2" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="556" y="153.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <line x1="34" y1="133" x2="28.5" y2="154" stroke="#1f2933" stroke-width="2.4" stroke-linecap="butt"/>
  <line x1="34" y1="133" x2="39.5" y2="154" stroke="#1f2933" stroke-width="2.4" stroke-linecap="butt"/>
  <rect x="27" y="111" width="14.5" height="24" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="34" cy="103" r="7.2" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="24" y="153.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <path d="M355,176 V184 H383 V176" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="352.5" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda_\text{A}$</div></foreignObject>
  <path d="M107,176 V184 H171 V176" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="122.5" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda_\text{B}$</div></foreignObject>
  <line x1="12" y1="220" x2="588" y2="220" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <g clip-path="url(#fy514-clip2)"><circle cx="230" cy="316" r="46" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="230" cy="316" r="92" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="230" cy="316" r="138" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="230" cy="316" r="184" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="230" cy="316" r="230" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="230" cy="316" r="276" fill="none" stroke="#6b7480" stroke-width="2"/><circle cx="230" cy="316" r="322" fill="none" stroke="#6b7480" stroke-width="2"/></g>
  <rect x="210" y="305" width="11" height="21.5" rx="2" fill="#1f2933"/>
  <path d="M221,305 L235.5,292.5 V339.5 L221,327 Z" fill="#8a96a3" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="496" y1="329" x2="490.5" y2="350" stroke="#1f2933" stroke-width="2.4" stroke-linecap="butt"/>
  <line x1="496" y1="329" x2="501.5" y2="350" stroke="#1f2933" stroke-width="2.4" stroke-linecap="butt"/>
  <rect x="489" y="307" width="14.5" height="24" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="496" cy="299" r="7.2" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <line x1="482" y1="266" x2="433" y2="266" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M420,266 L434,259.5 L434,272.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="367" y="251.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{h}$</div></foreignObject>
  <path d="M368,376 V384 H414 V376" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="381" y="389.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="16" y="3.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{lähde liikkuu}$</span></div></foreignObject>
  <foreignObject x="16" y="225.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kuulija liikkuu}$</span></div></foreignObject>
</svg>

### Dopplerin ilmiö, kun kuulija liikkuu
Nyt lähde on paikallaan ja kuulija liikkuu. Aallonpituus ei muutu. Kuulija kuitenkin kohtaa aaltorintamia useammin, kun hän kulkee niitä vastaan. Rintamat lähestyvät häntä silloin nopeudella $v + v_\text{h}$. Kun kuulija loittonee, rintamat saavuttavat hänet nopeudella $v - v_\text{h}$. Kuultu taajuus on rintamien kohtaamistiheys:
```latex
f = f_0 \cdot \frac{v \pm v_\text{h}}{v}
```
missä $v_\text{h}$ on kuulijan eli havaitsijan nopeus (m/s) ja muut suureet ovat samat kuin edellä. Plusmerkki valitaan, kun kuulija lähestyy lähdettä. Miinusmerkki valitaan, kun kuulija loittonee.

### Etumerkit ja oletukset
Etumerkin voi tarkistaa säännöllä. Lähestyminen nostaa kuultua taajuutta ja loittoneminen laskee sitä. Valitse siis merkki, joka antaa lähestyttäessä $f > f_0$ ja loitottaessa $f < f_0$. Nopeudet mitataan ilman suhteen. Ilma on paikallaan eli tuulta ei ole. Kaavat koskevat liikettä lähteen ja kuulijan välisellä suoralla. Ne pätevät, kun vain toinen liikkuu ja lähteen nopeus on pienempi kuin äänen nopeus. Kun nopeus on paljon pienempi kuin äänen nopeus, molemmat kaavat antavat lähes saman muutoksen. Se on noin $f_0 \cdot \tfrac{v_\text{s}}{v}$ tai $f_0 \cdot \tfrac{v_\text{h}}{v}$. Dopplerin ilmiöllä mitataan nopeuksia: ultraäänilaite mittaa veren virtausnopeutta.

## Esimerkki
Juna ajaa suoraa rataa tasaisella nopeudella $108\,\text{km/h}$ ja soittaa äänimerkkiä. Äänimerkin taajuus on $311\,\text{Hz}$. Matkustaja seisoo laiturilla aivan radan vieressä. Juna tulee suoraan häntä kohti ja loittonee suoraan hänestä poispäin. Minkä taajuuden matkustaja kuulee junan lähestyessä ja minkä sen loitotessa? Kuinka paljon taajuus laskee ohitushetkellä? Ilma on tyyntä, ja äänen nopeus on $340\,\text{m/s}$.

<!-- vaihe -->

**Tunnetut ja kysytty.** Äänimerkin taajuus on $f_0 = 311\,\text{Hz}$, junan nopeus on $v_\text{s} = 108\,\text{km/h}$ ja äänen nopeus on $v = 340\,\text{m/s}$. Kysytään kuultua taajuutta junan lähestyessä ($f_1$) ja loitotessa ($f_2$). Lisäksi kysytään taajuuden laskua $\Delta f = f_1 - f_2$.

<!-- vaihe -->

**Periaate.** Äänilähde liikkuu ja kuulija on paikallaan, joten käytetään liikkuvan lähteen Dopplerin kaavaa. Lähestyvän junan edessä aaltorintamat tihenevät. Merkki valitaan siis niin, että $f_1 > f_0$. Loittonevan junan takana rintamat harvenevat, ja $f_2 < f_0$. Malli on ideaalinen. Siinä oletetaan, että matkustaja on radan linjalla. Silloin junan koko nopeus osoittaa kohti häntä tai hänestä poispäin.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
f_1 &= f_0 \cdot \frac{v}{v - v_\text{s}} \\
f_2 &= f_0 \cdot \frac{v}{v + v_\text{s}} \\
\Delta f &= f_1 - f_2
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Junan nopeus muutetaan yksikköön m/s, jotta se voidaan vähentää äänen nopeudesta: $108\,\tfrac{\text{km}}{\text{h}} = 108 \cdot \tfrac{1000\,\text{m}}{3600\,\text{s}} = 30{,}0\,\tfrac{\text{m}}{\text{s}}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&f_1 = f_0 \cdot \frac{v}{v - v_\text{s}} \\
&\quad = 311\,\text{Hz} \cdot \frac{340\,\text{m/s}}{(340 - 30{,}0)\,\text{m/s}} \\
&\quad = 341{,}10\,\text{Hz} \\[6pt]
&f_2 = f_0 \cdot \frac{v}{v + v_\text{s}} \\
&\quad = 311\,\text{Hz} \cdot \frac{340\,\text{m/s}}{(340 + 30{,}0)\,\text{m/s}} \\
&\quad = 285{,}78\,\text{Hz} \\[6pt]
&\Delta f = f_1 - f_2 \\
&\quad = 341{,}10\,\text{Hz} - 285{,}78\,\text{Hz} \\
&\quad = 55{,}32\,\text{Hz}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Matkustaja kuulee lähestyvän junan äänen taajuudella $341\,\text{Hz}$ ja loittonevan junan äänen taajuudella $286\,\text{Hz}$. Vastauksissa on kolme merkitsevää numeroa kuten lähtötiedoissa. Ohitushetkellä taajuus laskee noin $55\,\text{Hz}$. Erotus on noin hertsin tarkkuudella, koska kumpikin taajuus tunnetaan noin puolen hertsin tarkkuudella. Todellisuudessa matkustaja on hieman radan sivussa. Siksi taajuus ei laske hetkessä. Se laskee liukuvasti sinä lyhyenä aikana, kun juna ohittaa hänet. Kaukana ohituskohdasta taajuudet ovat silti lähes $341\,\text{Hz}$ ja $286\,\text{Hz}$.

<!-- vaihe -->

**Järkevyys.** Pienellä nopeudella muutos on kummallakin puolella noin $f_0 \cdot \tfrac{v_\text{s}}{v} = 311\,\text{Hz} \cdot \tfrac{30{,}0\,\text{m/s}}{340\,\text{m/s}} \approx 27\,\text{Hz}$. Koko lasku on siis noin $55\,\text{Hz}$, kuten laskettiin. Nousu lähestyessä, $30\,\text{Hz}$, on hieman suurempi kuin lasku loitotessa, $25\,\text{Hz}$. Edessä jaetaan nimittäin pienemmällä luvulla $v - v_\text{s}$. Junan nopeus on alle kymmenesosa äänen nopeudesta. Muutos on siksi kummallakin puolella vain noin $9\,\%$ taajuudesta $f_0$.

## Yleinen virhekäsitys
Moni ajattelee, että lähestyvän sireenin ääni nousee koko ajan sitä mukaa kuin auto tulee lähemmäs. Kuultu taajuus riippuu kuitenkin nopeudesta, ei etäisyydestä. Oletetaan, että ambulanssi ajaa tasaisella nopeudella suoraan kohti kuulijaa. Silloin kuultu taajuus on koko lähestymisen ajan sama ja suurempi kuin $f_0$. Ohitushetkellä se laskee. Lähestyessä kasvaa äänen voimakkuus, ei sen korkeus. Jos kuulija seisoo tien sivussa, muutos tapahtuu ohituksen aikana liukuvasti. Kuultuun taajuuteen vaikuttaa nimittäin vain se osa nopeudesta, joka osoittaa kohti kuulijaa tai hänestä poispäin.

Toinen virhe on luulla, että lähteen liike muuttaa äänen nopeutta tai lähteen omaa taajuutta. Ääni etenee ilman suhteen nopeudella $v$, liikkui lähde tai ei. Sireeni värähtelee koko ajan taajuudella $f_0$. Liikkuva lähde muuttaa aallonpituutta. Liikkuva kuulija muuttaa sitä, kuinka usein hän kohtaa aaltorintamia. Kolmas virhe on lukea spektristä äänenkorkeudeksi korkeimman piikin taajuus. Perustaajuus on harmonisen sarjan alin taajuus ja piikkien väli, vaikka jokin yläsävel olisi sitä voimakkaampi.

## Tiivistelmä
- Ääni on pitkittäinen paineaalto, jossa tihentymät ja harvennukset etenevät väliaineessa. Äänen nopeus riippuu väliaineesta ja kaasussa lämpötilasta. Ilmassa se on noin $340\,\text{m/s}$. Nopeus määritetään mittaamalla äänen kulkuaika tunnetulla matkalla.
- Äänenkorkeus määräytyy taajuudesta. Ihmisen kuuloalue on noin $20\,\text{Hz}$–$20\,\text{kHz}$. Matalampi ääni on infraääntä ja korkeampi ultraääntä.
- Sointiväri riippuu yläsävelten voimakkuuksista. Soittimen osasävelet muodostavat harmonisen sarjan $f_n = n f_1$, ja FFT-spektri näyttää ne piikkeinä.
- Kun kaksi lähes samantaajuista ääntä soi yhtä aikaa, kuuluu huojunta, jonka taajuus on $f_\text{h} = |f_1 - f_2|$.
- Dopplerin ilmiö: lähestyminen nostaa ja loittoneminen laskee kuultua taajuutta. Liikkuvalle lähteelle $f = f_0 \cdot \tfrac{v}{v \mp v_\text{s}}$ ja liikkuvalle kuulijalle $f = f_0 \cdot \tfrac{v \pm v_\text{h}}{v}$. Ylempi merkki on lähestyttäessä.
