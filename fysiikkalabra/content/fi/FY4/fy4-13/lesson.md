# Liikeyhtälö kytketyille kappaleille

> **Miksi** pöydän reunalta riippuva punnus putoaa hitaammin kuin vapaasti pudotessaan, kun se vetää langalla pöydällä olevaa kärryä mukanaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: fysiikan luokan pöytä. Pöydällä on kärry, jonka päällä on kaksi metallipunnusta. Kärryyn sidottu lanka kulkee pöydän reunalla olevan väkipyörän yli, ja langan toisessa päässä roikkuu yksi metallipunnus. Pöydällä on mitta-asteikko ja sekuntikello, ja oppilas seisoo pöydän vieressä." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy413h-wall" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="470"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy413h-win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy413h-floor" gradientUnits="userSpaceOnUse" x1="0" y1="470" x2="0" y2="600"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-leg110" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-leg760" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy413h-cart" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy413h-m290" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy413h-m362" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy413h-hang" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="470" fill="url(#fy413h-wall)"/>
  <rect x="880" y="70" width="240" height="230" rx="4" fill="url(#fy413h-win)" stroke="#1f2933" stroke-width="3"/>
  <path d="M933,176 Q932,160 951,162 Q958.5,144.5 978,150.5 Q995,140.5 1005,159 Q1022,161 1020,176 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="1000" y1="70" x2="1000" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="880" y1="185" x2="1120" y2="185" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="868" y="300" width="264" height="14" rx="3" fill="#c9c2b2" stroke="#1f2933" stroke-width="3"/>
  <rect x="70" y="110" width="300" height="14" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="3"/>
  <rect x="100" y="64" width="60" height="46" rx="8" fill="#a5d8ff" stroke="#1f2933" stroke-width="3"/>
  <rect x="190" y="64" width="60" height="46" rx="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/>
  <rect x="280" y="64" width="60" height="46" rx="8" fill="#b2f2bb" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy413h-floor)"/>
  <line x1="0" y1="492" x2="1200" y2="492" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="514" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="536" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="558" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="580" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="602" x2="1200" y2="602" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="110" y="354" width="26" height="170" fill="url(#fy413h-leg110)" stroke="#1f2933" stroke-width="3"/>
  <rect x="760" y="354" width="26" height="170" fill="url(#fy413h-leg760)" stroke="#1f2933" stroke-width="3"/>
  <rect x="70" y="330" width="770" height="24" rx="3" fill="url(#fy413h-top)" stroke="#1f2933" stroke-width="3"/>
  <path d="M130,344 q200,-4 400,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M170,340 q200,-4 400,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M210,344 q200,-4 400,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.5"/>
  <rect x="120" y="336" width="560" height="12" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="124" y1="336" x2="124" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="134" y1="336" x2="134" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="143.5" y1="336" x2="143.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="153.5" y1="336" x2="153.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163" y1="336" x2="163" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="173" y1="336" x2="173" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="183" y1="336" x2="183" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="336" x2="192.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="202.5" y1="336" x2="202.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="212" y1="336" x2="212" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="222" y1="336" x2="222" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="232" y1="336" x2="232" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="241.5" y1="336" x2="241.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="251.5" y1="336" x2="251.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="261" y1="336" x2="261" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="271" y1="336" x2="271" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="281" y1="336" x2="281" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290.5" y1="336" x2="290.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300.5" y1="336" x2="300.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="336" x2="310" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="336" x2="320" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="336" x2="330" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="339.5" y1="336" x2="339.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="349.5" y1="336" x2="349.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="336" x2="359" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="369" y1="336" x2="369" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="379" y1="336" x2="379" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="388.5" y1="336" x2="388.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398.5" y1="336" x2="398.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="408" y1="336" x2="408" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="418" y1="336" x2="418" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428" y1="336" x2="428" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="437.5" y1="336" x2="437.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="447.5" y1="336" x2="447.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="457" y1="336" x2="457" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="467" y1="336" x2="467" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="477" y1="336" x2="477" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="486.5" y1="336" x2="486.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496.5" y1="336" x2="496.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="506" y1="336" x2="506" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="516" y1="336" x2="516" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="526" y1="336" x2="526" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="535.5" y1="336" x2="535.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="545.5" y1="336" x2="545.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="555" y1="336" x2="555" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="565" y1="336" x2="565" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="575" y1="336" x2="575" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="584.5" y1="336" x2="584.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="594.5" y1="336" x2="594.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="604" y1="336" x2="604" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="614" y1="336" x2="614" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="624" y1="336" x2="624" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="633.5" y1="336" x2="633.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="643.5" y1="336" x2="643.5" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="653" y1="336" x2="653" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="663" y1="336" x2="663" y2="346" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="673" y1="336" x2="673" y2="342" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="145" y="252.5" width="9.5" height="7" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="148" y="259" width="4" height="4" fill="#6c757d"/>
  <circle cx="150" cy="292" r="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="150" cy="292" r="24.6" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="271.5" x2="150" y2="268.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="274.5" x2="161.5" y2="271.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="167.5" y1="282" x2="170.5" y2="280.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="170.5" y1="292" x2="173.5" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="167.5" y1="302" x2="170.5" y2="303.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="309.5" x2="161.5" y2="312.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="312.5" x2="150" y2="315.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="140" y1="309.5" x2="138.5" y2="312.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="132.5" y1="302" x2="129.5" y2="303.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="129.5" y1="292" x2="126.5" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="132.5" y1="282" x2="129.5" y2="280.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="140" y1="274.5" x2="138.5" y2="271.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="292" x2="168" y2="283.5" stroke="#c92a2a" stroke-width="2.1" stroke-linecap="round"/>
  <circle cx="150" cy="292" r="2.4" fill="#1f2933"/>
  <rect x="250" y="262" width="200" height="34" rx="5" fill="url(#fy413h-cart)" stroke="#1f2933" stroke-width="3"/>
  <rect x="260" y="270" width="180" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <rect x="290" y="218" width="56" height="44" rx="6" fill="url(#fy413h-m290)" stroke="#1f2933" stroke-width="3"/>
  <rect x="298" y="226" width="40" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <rect x="362" y="218" width="56" height="44" rx="6" fill="url(#fy413h-m362)" stroke="#1f2933" stroke-width="3"/>
  <rect x="370" y="226" width="40" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="286" cy="312" r="22" fill="#1f2933"/>
  <circle cx="286" cy="312" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="286" cy="312" r="4" fill="#1f2933"/>
  <circle cx="414" cy="312" r="22" fill="#1f2933"/>
  <circle cx="414" cy="312" r="14" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="414" cy="312" r="4" fill="#1f2933"/>
  <rect x="448" y="270" width="14" height="6" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M812,330 V318 Q812,290 872,290" fill="none" stroke="#6c757d" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="796" y="316" width="34" height="18" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="872" cy="290" r="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="872" cy="290" r="21" fill="#ffffff" stroke="#8a96a3" stroke-width="2"/>
  <line x1="878" y1="290" x2="893" y2="290" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="875" y1="295" x2="882.5" y2="308" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="869" y1="295" x2="861.5" y2="308" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="866" y1="290" x2="851" y2="290" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="869" y1="285" x2="861.5" y2="272" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="875" y1="285" x2="882.5" y2="272" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="872" cy="290" r="6" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M462,273 H872 A30,30 0 0 1 902,290 V396" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M888,396 h28 v14 h-28 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="874" y="410" width="56" height="44" rx="6" fill="url(#fy413h-hang)" stroke="#1f2933" stroke-width="3"/>
  <rect x="882" y="418" width="40" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>
  <ellipse cx="902" cy="472" rx="46" ry="8" fill="#1f2933" fill-opacity="0.12"/>
  <path d="M989.5,560 L994.5,443 H1025.5 L1030.5,560 H1014.5 L1010,482 L1005.5,560 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M983.5,451 Q980.5,365 1010,360.5 Q1039.5,365 1036.5,451 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M986.5,376 L979,451" fill="none" stroke="#1971c2" stroke-width="17.16" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="979" cy="457" r="8.58" fill="#f1dfb5"/>
  <path d="M1033.5,376 L1041,451" fill="none" stroke="#1971c2" stroke-width="17.16" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1041" cy="457" r="8.58" fill="#f1dfb5"/>
  <rect x="1003" y="344.5" width="14" height="18.5" fill="#f1dfb5"/>
  <circle cx="1010" cy="329" r="23.4" fill="#f1dfb5"/>
  <path d="M986,329 Q986.5,301 1010,302.5 Q1035,302.5 1034,326 Q1014.5,316.5 986,329 Z" fill="#1f2933" stroke-linejoin="round"/>
</svg>

## Ydinajatus
Usein kaksi kappaletta liikkuu yhdessä, koska ne on sidottu toisiinsa langalla. Kun lanka on kireä ja venymätön, kappaleet kulkevat saman matkan samassa ajassa, joten niiden kiihtyvyyksillä on sama suuruus $a$. Lanka välittää voiman kappaleelta toiselle: se vetää kumpaakin kappaletta itseään kohti. Tässä luvussa lanka on kevyt ja venymätön, väkipyörä kevyt ja kitkaton, ja pöydän kitka ja ilmanvastus jätetään huomiotta.

Kytketyt kappaleet käsitellään yksi kerrallaan. Kummallekin piirretään oma voimakuvio, jossa on vain siihen vaikuttavat voimat, ja kummallekin kirjoitetaan oma liikeyhtälö. Kuvan kärryyn vaikuttavat paino $\overline{G}_1$, pöydän tukivoima $\overline{N}$ ja langan jännitysvoima $\overline{T}_1$. Riippuvaan punnukseen vaikuttavat paino $\overline{G}_2$ ja langan jännitysvoima $\overline{T}_2$.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Kaksi kappaletta ja niiden voimakuviot. Vasemmalla tilannekuva: pöydällä on kärry, ja siihen sidottu lanka kulkee pöydän reunan väkipyörän yli riippuvaan punnukseen. Kärryn yllä ovat ohuet nuolet: sininen nopeus oikealle ja lyhyempi oranssi kiihtyvyys oikealle. Oikealla ylhäällä kärryn voimakuvio, kärry suorakulmiona: paino G1 keskipisteestä alas, pöydän tukivoima N alapinnasta ylös ja yhtä pitkä kuin paino sekä langan jännitysvoima T1 oikealta reunalta oikealle. Oikealla alhaalla riippuvan punnuksen voimakuvio: paino G2 keskipisteestä alas ja langan jännitysvoima T2 yläpinnasta ylös. Nuoli T2 on lyhyempi kuin G2, ja nuolet T1 ja T2 ovat yhtä pitkät." style="max-width:100%;font-size:24px">
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <rect x="20" y="176" width="214" height="12" rx="2" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="28" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="190" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="10" y1="296" x2="290" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="244" cy="164" r="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="244" cy="164" r="7" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="244" cy="164" r="2.5" fill="#1f2933"/>
  <rect x="226" y="172" width="12" height="10" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="70" y="146" width="60" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="83" cy="169" r="7" fill="#1f2933"/>
  <circle cx="117" cy="169" r="7" fill="#1f2933"/>
  <circle cx="83" cy="169" r="3" fill="#c4ccd4"/>
  <circle cx="117" cy="169" r="3" fill="#c4ccd4"/>
  <rect x="82" y="132" width="36" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M130,156 H244 A12,12 0 0 1 256,164 V236" fill="none" stroke="#b8622d" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="244" y="236" width="24" height="32" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="236" x2="256" y2="232" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="82" y1="124" x2="140" y2="124" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M129,130.5 L142,124 L129,117.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="82" y1="84" x2="120" y2="84" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M109,90.5 L122,84 L109,77.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="197.5" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="332" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="182" x2="590" y2="182" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: kärry}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: punnus}$</div></foreignObject>
  <rect x="400" y="88" width="80" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="108" x2="440" y2="150" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,167 L432,149 L448,149 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="148.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="418" y1="128" x2="418" y2="86" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M418,69 L426,87 L410,87 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="56.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="480" y1="102" x2="482.5" y2="102" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M499.5,102 L481.5,110 L481.5,94 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="499" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <rect x="412" y="254" width="56" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="276" x2="440" y2="288.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,305.5 L432,287.5 L448,287.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="293" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="254" x2="440" y2="251.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,234.5 L448,252.5 L432,252.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="222" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

Lanka vetää kärryä voimalla $\overline{T}_1$ ja punnusta voimalla $\overline{T}_2$. Ne vaikuttavat eri kappaleisiin, joten ne ovat eri voimakuvioissa. Kevyt lanka ja kitkaton väkipyörä vain välittävät voiman ja kääntävät sen suunnan, joten voimien suuruudet ovat samat: $T_1 = T_2 = T$. Voimat $\overline{T}_1$ ja $\overline{T}_2$ eivät kuitenkaan ole voima ja vastavoima. Kun lanka vetää kärryä, kärry vetää lankaa takaisin yhtä suurella voimalla, ja se vaikuttaa lankaan eikä ole kärryn voimakuviossa.

Kun punnus kiihtyy alaspäin, langan jännitysvoima on pienempi kuin punnuksen paino. Kiihtyvyys on alas, joten punnuksen kokonaisvoima osoittaa alas ja $G_2 > T$. Jos $T$ olisi yhtä suuri kuin $G_2$, punnukseen vaikuttava kokonaisvoima olisi nolla eikä punnus lähtisi liikkeelle.

## Kaava: Kytkettyjen kappaleiden liikeyhtälöt
Jokaiselle kappaleelle kirjoitetaan oma liikeyhtälö $\Sigma F = ma$. Positiivinen suunta valitaan kullekin kappaleelle erikseen kiihtyvyyden suuntaan: kärryllä oikealle ja punnuksella alas. Koska lanka on venymätön, kummankin kappaleen kiihtyvyydellä on sama suuruus $a$. Kärryn ja punnuksen yhtälöt ovat
```latex
\begin{aligned}
T &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
missä $m_1$ on kärryn massa (kg), $m_2$ punnuksen massa (kg), $T$ langan jännitysvoima (N), $a$ kiihtyvyys (m/s²) ja $g = 9{,}81\,\text{m/s}^2$. Tuntemattomia on kaksi, $a$ ja $T$, ja yhtälöitä kaksi.

Kun yhtälöt lasketaan puolittain yhteen, $T$ supistuu pois, koska lanka on kappaleiden välinen sisäinen voima. Näin saadaan kiihtyvyys ja sen jälkeen jännitysvoima:
```latex
\begin{aligned}
a &= \frac{m_2}{m_1 + m_2}\,g \\
T &= m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
Jännitysvoima on aina pienempi kuin punnuksen paino $m_2 g$, koska $\tfrac{m_1}{m_1 + m_2} < 1$. Mitä raskaampi kärry on punnukseen verrattuna, sitä vähemmän kappaleet kiihtyvät ja sitä lähempänä $T$ on painoa $m_2 g$.

### Kaksi riippuvaa kappaletta
Kun langan kummassakin päässä roikkuu kappale, raskaampi ($m_2$) laskee ja kevyempi ($m_1$) nousee. Positiivinen suunta valitaan liikkeen suuntaan: kevyemmällä ylös ja raskaammalla alas. Silloin
```latex
\begin{aligned}
T - m_1 g &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
```latex
\begin{aligned}
a &= \frac{m_2 - m_1}{m_1 + m_2}\,g \\
T &= \frac{2 m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
missä $m_2 > m_1$. Jännitysvoima on kappaleiden painojen $m_1 g$ ja $m_2 g$ välissä. Jos massat ovat yhtä suuret, $a = 0$ ja $T = mg$.

<svg data-fig="atwood" viewBox="0 0 600 380" role="img" aria-label="Kaksi riippuvaa kappaletta ja niiden voimakuviot. Vasemmalla tilannekuva: katosta riippuvan väkipyörän yli kulkevan langan vasemmassa päässä on kevyempi kappale ja oikeassa raskaampi. Kevyemmän vieressä on oranssi nuoli ylös ja raskaamman vieressä yhtä pitkä oranssi nuoli alas: kiihtyvyyden suuruus on sama. Oikealla ylhäällä kevyemmän kappaleen voimakuvio, kappale suorakulmiona: langan jännitysvoima T1 yläpinnasta ylös ja paino G1 keskipisteestä alas, ja T1 on pidempi kuin G1. Oikealla alhaalla raskaamman kappaleen voimakuvio: T2 yläpinnasta ylös ja G2 keskipisteestä alas, ja G2 on pidempi kuin T2. Nuolet T1 ja T2 ovat yhtä pitkät." style="max-width:100%;font-size:24px">
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <line x1="70" y1="56" x2="190" y2="56" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="70" y1="56" x2="60" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="56" x2="76" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="102" y1="56" x2="92" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="118" y1="56" x2="108" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="134" y1="56" x2="124" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="56" x2="140" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="166" y1="56" x2="156" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="182" y1="56" x2="172" y2="44" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="56" x2="130" y2="92" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="130" cy="104" r="22" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="130" cy="104" r="17" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="130" cy="104" r="2.5" fill="#1f2933"/>
  <line x1="108" y1="104" x2="108" y2="206" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="152" y1="104" x2="152" y2="242" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="94" y="206" width="28" height="31.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="134" y="242" width="36" height="37" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="60" y1="236" x2="60" y2="194" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M66.5,205 L60,192 L53.5,205" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="21.5" y="173.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="212" y1="252" x2="212" y2="294" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M205.5,283 L212,296 L218.5,283" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="217.5" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="91.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="135.5" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="368" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="190" x2="590" y2="190" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: kevyempi}$</div></foreignObject>
  <foreignObject x="312" y="191.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: raskaampi}$</div></foreignObject>
  <rect x="412" y="110" width="56" height="36" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="128" x2="440" y2="137.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,154.5 L432,136.5 L448,136.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="142" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="440" y1="110" x2="440" y2="91.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,74.5 L448,92.5 L432,92.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="62" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <line x1="540" y1="150" x2="540" y2="108" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M546.5,119 L540,106 L533.5,119" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="545.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <rect x="408" y="278" width="64" height="48" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="302" x2="440" y2="338" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,355 L432,337 L448,337 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="342.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="278" x2="440" y2="259.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,242.5 L448,260.5 L432,260.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="230" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
  <line x1="540" y1="280" x2="540" y2="322" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M533.5,311 L540,324 L546.5,311" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="545.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

### Menetelmä kytketyille kappaleille
1. **Piirrä oma voimakuvio** kummallekin kappaleelle. Lanka vetää kumpaakin kappaletta itseään kohti, ja jokaisella kappaleella on oma jännitysvoimansa nuoli.
2. **Valitse positiivinen suunta** kullekin kappaleelle kiihtyvyyden suuntaan.
3. **Kirjoita liikeyhtälö** $\Sigma F = ma$ kummallekin kappaleelle erikseen. Kiihtyvyyden suuruus $a$ ja jännitysvoiman suuruus $T$ ovat samat molemmissa.
4. **Ratkaise** kaksi yhtälöä: laske ne yhteen, jolloin $T$ poistuu, tai sijoita toisesta saatu $T$ toiseen.
5. **Tarkista** etumerkit ja vertaa: jännitysvoima ei ole yhtä suuri kuin riippuvan kappaleen paino, kun kappaleet kiihtyvät.

## Esimerkki
Pöydällä on kärry, jonka massa on $1{,}5\,\text{kg}$. Siihen sidottu lanka kulkee pöydän reunalla olevan kevyen väkipyörän yli, ja langan toisessa päässä roikkuu punnus, jonka massa on $0{,}60\,\text{kg}$. Kärry päästetään liikkeelle levosta. Kitka ja ilmanvastus jätetään huomiotta, ja lanka on kevyt ja venymätön. Kuinka suuri on kärryn kiihtyvyys ja kuinka suuri on langan jännitysvoima?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m_1 = 1{,}5\,\text{kg}$, $m_2 = 0{,}60\,\text{kg}$ ja $g = 9{,}81\,\text{m/s}^2$. Kysytään kiihtyvyyttä $a$ ja langan jännitysvoimaa $T$.

<!-- vaihe -->

**Periaate.** Kärry ja punnus ovat kaksi kappaletta, joten kummallekin kirjoitetaan oma liikeyhtälö. Lanka on venymätön, joten kappaleiden kiihtyvyyksillä on sama suuruus $a$. Lanka on kevyt ja väkipyörä kitkaton, joten lanka vetää kumpaakin kappaletta samalla voimalla $T$. Kitkaa ei ole, joten vaakasuunnassa kärryyn vaikuttaa vain lanka.

<!-- vaihe -->

**Voimakuvio.** Kummallekin kappaleelle on oma voimakuvio. Kärryn positiivinen suunta on oikealle ja punnuksen alas. Pystysuunnassa kärry ei kiihdy, joten $N = G_1$. Vaakasuunnassa kärryä vetää vain $\overline{T}_1$. Punnukseen vaikuttavat $\overline{G}_2$ alas ja $\overline{T}_2$ ylös.

<svg data-fig="esimerkki" viewBox="0 0 600 340" role="img" aria-label="Esimerkin kärry ja riippuva punnus. Vasemmalla tilannekuva: pöydällä oleva kärry, lanka väkipyörän yli riippuvaan punnukseen, ja kärryn yllä sininen nopeus ja oranssi kiihtyvyys oikealle. Oikealla ylhäällä kärryn voimakuvio: paino G1 alas, yhtä pitkä tukivoima N ylös ja jännitysvoima T1 oikealle. Oikealla alhaalla riippuvan punnuksen voimakuvio: paino G2 alas ja lyhyempi jännitysvoima T2 ylös. Nuolet T1 ja T2 ovat yhtä pitkät." style="max-width:100%;font-size:24px">
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <rect x="20" y="176" width="214" height="12" rx="2" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="28" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="190" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="10" y1="296" x2="290" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="244" cy="164" r="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="244" cy="164" r="7" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="244" cy="164" r="2.5" fill="#1f2933"/>
  <rect x="226" y="172" width="12" height="10" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="70" y="146" width="60" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="83" cy="169" r="7" fill="#1f2933"/>
  <circle cx="117" cy="169" r="7" fill="#1f2933"/>
  <circle cx="83" cy="169" r="3" fill="#c4ccd4"/>
  <circle cx="117" cy="169" r="3" fill="#c4ccd4"/>
  <rect x="82" y="132" width="36" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M130,156 H244 A12,12 0 0 1 256,164 V236" fill="none" stroke="#b8622d" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="244" y="236" width="24" height="32" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="236" x2="256" y2="232" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="82" y1="124" x2="140" y2="124" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M129,130.5 L142,124 L129,117.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="82" y1="84" x2="120" y2="84" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M109,90.5 L122,84 L109,77.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="197.5" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="332" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="182" x2="590" y2="182" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: kärry}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: punnus}$</div></foreignObject>
  <rect x="400" y="88" width="80" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="108" x2="440" y2="157" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,174 L432,156 L448,156 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="155.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="418" y1="128" x2="418" y2="79" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M418,62 L426,80 L410,80 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="480" y1="102" x2="482" y2="102" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M499,102 L481,110 L481,94 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="498.5" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <rect x="412" y="254" width="56" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="276" x2="440" y2="285.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,302.5 L432,284.5 L448,284.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="290" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="254" x2="440" y2="252" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,235 L448,253 L432,253 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="222.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Kuvioista luetaan kaksi liikeyhtälöä ja ratkaistaan ne:
```latex
\begin{aligned}
&T = m_1 a \\
&m_2 g - T = m_2 a \\
&a = \frac{m_2 g}{m_1 + m_2} \\
&T = m_1 a
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: massat ovat kilogrammoina ja $\tfrac{\text{kg} \cdot \text{m/s}^2}{\text{kg}} = \text{m/s}^2$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
&a = \frac{m_2 g}{m_1 + m_2} \\
&\phantom{a} = \frac{0{,}60\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{1{,}5\,\text{kg} + 0{,}60\,\text{kg}} \\
&\phantom{a} \approx 2{,}80\,\text{m/s}^2 \\[4pt]
&T = m_1 a = 1{,}5\,\text{kg} \cdot 2{,}803\,\text{m/s}^2 \\
&\phantom{T} \approx 4{,}20\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kärryn kiihtyvyys on $a \approx 2{,}8\,\text{m/s}^2$ ja langan jännitysvoima $T \approx 4{,}2\,\text{N}$, kahden merkitsevän numeron tarkkuudella kuten massat $1{,}5\,\text{kg}$ ja $0{,}60\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** Punnuksen paino on $m_2 g \approx 5{,}9\,\text{N}$, ja jännitysvoima $4{,}2\,\text{N}$ on sitä pienempi, kuten pitääkin. Punnuksen kokonaisvoima on $5{,}886\,\text{N} - 4{,}204\,\text{N} \approx 1{,}68\,\text{N}$, ja se on $m_2 a = 0{,}60\,\text{kg} \cdot 2{,}803\,\text{m/s}^2 \approx 1{,}68\,\text{N}$. Kiihtyvyys on pienempi kuin $g$, koska punnus kiihdyttää myös kärryä. Jos kärryä ei olisi, punnus putoaisi kiihtyvyydellä $g$.

## Yleinen virhekäsitys
Usein ajatellaan, että kärryä vetää riippuvan punnuksen paino, joten jännitysvoima olisi $m_2 g$. Kärryä vetää kuitenkin lanka, ja langan voima on $T$. Vain silloin, kun kappaleet eivät kiihdy, esimerkiksi kun kärryä pidetään paikallaan, on $T = m_2 g$. Kun punnus laskee kiihtyen, osa sen painosta kuluu punnuksen oman liikkeen kiihdyttämiseen, ja $T < m_2 g$.

Toinen virhe on pitää voimia $\overline{T}_1$ ja $\overline{T}_2$ voimana ja vastavoimana. Ne vaikuttavat eri kappaleisiin mutta kuuluvat eri vuorovaikutuksiin: toinen lanka–kärry-parin ja toinen lanka–punnus-parin voimia. Ne ovat yhtä suuret, koska lanka on kevyt, ei sen vuoksi, että ne olisivat vuorovaikutusparin voimia. Kolmas virhe on ajatella, että raskaampi kappale kiihtyy enemmän. Venymättömän langan päissä olevilla kappaleilla on sama kiihtyvyyden suuruus.

## Tiivistelmä
- Langalla tai väkipyörän yli kytketyillä kappaleilla on kummallakin oma voimakuvio ja oma liikeyhtälö $\Sigma F = ma$, ja positiivinen suunta valitaan kappaleelle kiihtyvyyden suuntaan.
- Kevyt venymätön lanka ja kitkaton kevyt väkipyörä antavat kappaleille saman kiihtyvyyden suuruuden $a$ ja samansuuruiset jännitysvoimat $T_1 = T_2 = T$.
- Kärrylle ja riippuvalle punnukselle $a = 	frac{m_2}{m_1 + m_2}\,g$ ja $T = 	frac{m_1 m_2}{m_1 + m_2}\,g$. Kahdelle riippuvalle kappaleelle $a = 	frac{m_2 - m_1}{m_1 + m_2}\,g$ ja $T = 	frac{2 m_1 m_2}{m_1 + m_2}\,g$.
- Kiihtyvän riippuvan kappaleen jännitysvoima ei ole sen paino: kärryn ja punnuksen tapauksessa $T < m_2 g$, ja kahdella riippuvalla kappaleella $T$ on painojen välissä.
- Jännitysvoimat $\overline{T}_1$ ja $\overline{T}_2$ vaikuttavat eri kappaleisiin eivätkä ole voima ja vastavoima.
