# Termodynaaminen systeemi, tilanmuuttujat ja lämpötila

> **Miksi** pyörän rengas tuntuu kovemmalta kuumana kesäpäivänä kuin pakkasella, vaikka renkaaseen ei pumpata lisää ilmaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: polkupyörä seisoo kuumalla asfaltilla kesähelteellä. Aurinko paistaa, asfaltin yllä väreilee kuumuus ja tolpan lämpömittarin punainen pylväs on korkealla." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy33h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy33h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy33h-road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#1f2933"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="430" fill="url(#fy33h-sky)"/>
  <circle cx="1020" cy="110" r="93" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M1087.5,135.5 L1117.5,136 L1091.5,122 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1066,166 L1091.5,181.5 L1076,156 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1032,181.5 L1046,207.5 L1045.5,177.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M994.5,177.5 L994,207.5 L1008,181.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M964,156 L948.5,181.5 L974,166 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M948.5,122 L922.5,136 L952.5,135.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M952.5,84.5 L922.5,84 L948.5,98 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M974,54 L948.5,38.5 L964,64 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1008,38.5 L994,12.5 L994.5,42.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1045.5,42.5 L1046,12.5 L1032,38.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1076,64 L1091.5,38.5 L1066,54 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1091.5,98 L1117.5,84 L1087.5,84.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="1020" cy="110" r="58" fill="url(#fy33h-sun)"/>
  <path d="M219,108 Q217,77.5 253,81 Q267.5,48.5 303.5,59.5 Q336,41.5 354,75.5 Q386.5,79 383,108 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="40" y="210" width="220" height="220" fill="#ffffff" stroke="#c9c2b2" stroke-width="3"/>
  <rect x="64" y="236" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="64" y="300" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="64" y="364" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="124" y="236" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="124" y="300" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="124" y="364" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="184" y="236" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="184" y="300" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="184" y="364" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="280" y="260" width="180" height="170" fill="#ffffff" stroke="#c9c2b2" stroke-width="3"/>
  <rect x="304" y="286" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="304" y="350" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="364" y="286" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="364" y="350" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="480" y="180" width="240" height="250" fill="#ffffff" stroke="#c9c2b2" stroke-width="3"/>
  <rect x="504" y="206" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="504" y="270" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="504" y="334" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="504" y="398" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="564" y="206" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="564" y="270" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="564" y="334" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="564" y="398" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="624" y="206" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="624" y="270" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="624" y="334" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="624" y="398" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="740" y="240" width="200" height="190" fill="#ffffff" stroke="#c9c2b2" stroke-width="3"/>
  <rect x="764" y="266" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="764" y="330" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="764" y="394" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="824" y="266" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="824" y="330" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="824" y="394" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="884" y="266" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="884" y="330" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="884" y="394" width="34" height="40" fill="#eef5f9" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="0" y="430" width="1200" height="20" fill="#e3dccb" stroke="#c9c2b2" stroke-width="2"/>
  <rect x="0" y="450" width="1200" height="150" fill="url(#fy33h-road)"/>
  <rect x="40" y="528" width="110" height="10" rx="3" fill="#ffffff"/>
  <rect x="260" y="528" width="110" height="10" rx="3" fill="#ffffff"/>
  <rect x="480" y="528" width="110" height="10" rx="3" fill="#ffffff"/>
  <rect x="700" y="528" width="110" height="10" rx="3" fill="#ffffff"/>
  <rect x="920" y="528" width="110" height="10" rx="3" fill="#ffffff"/>
  <rect x="1140" y="528" width="110" height="10" rx="3" fill="#ffffff"/>
  <path d="M160,520 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M240,520 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M920,520 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M1000,520 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M1080,520 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <circle cx="480" cy="446" r="82" fill="none" stroke="#1f2933" stroke-width="12"/>
  <circle cx="480" cy="446" r="74" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="480" y1="446" x2="550" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="540.5" y2="481" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="515" y2="506.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="480" y2="516" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="445" y2="506.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="419.5" y2="481" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="410" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="419.5" y2="411" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="445" y2="385.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="480" y2="376" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="515" y2="385.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="446" x2="540.5" y2="411" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="480" cy="446" r="7" fill="#1f2933"/>
  <circle cx="760" cy="446" r="82" fill="none" stroke="#1f2933" stroke-width="12"/>
  <circle cx="760" cy="446" r="74" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="760" y1="446" x2="830" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="820.5" y2="481" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="795" y2="506.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="760" y2="516" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="725" y2="506.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="699.5" y2="481" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="690" y2="446" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="699.5" y2="411" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="725" y2="385.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="760" y2="376" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="795" y2="385.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="446" x2="820.5" y2="411" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="760" cy="446" r="7" fill="#1f2933"/>
  <path d="M480,446 L580,446 L700,330 L560,330 Z" fill="none" stroke="#1971c2" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M580,446 L540,300" fill="none" stroke="#1971c2" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M700,330 L760,446" fill="none" stroke="#1971c2" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M700,330 L690,300" fill="none" stroke="#1971c2" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M512,292 H572" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M670,296 Q690,286 716,298" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="580" cy="446" r="16" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="1111" y="210" width="18" height="190" rx="9" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="1120" cy="400" r="16" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <rect x="1116" y="240" width="8" height="160" fill="#c92a2a"/>
  <line x1="1129" y1="378" x2="1137" y2="378" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1129" y1="356" x2="1137" y2="356" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1129" y1="334" x2="1137" y2="334" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1129" y1="312" x2="1137" y2="312" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1129" y1="290" x2="1137" y2="290" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1129" y1="268" x2="1137" y2="268" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1129" y1="246" x2="1137" y2="246" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="1114" y="400" width="12" height="50" fill="#6c757d"/>
</svg>

## Ydinajatus
Kun tutkitaan ilmiötä, tarkasteltava osa maailmasta rajataan erilleen muusta. Rajattu osa on termodynaaminen systeemi ja kaikki sen ulkopuolella oleva on ympäristö. Pyörän renkaan ilma on esimerkki systeemistä. Jos systeemistä ei pääse ainetta ulos eikä sisään, systeemi on suljettu. Systeemin tilaa kuvataan tilanmuuttujilla, joita ovat lämpötila, paine ja tilavuus sekä aineen määrä. Paine on voima pinta-alaa kohti; sen yksikkö on pascal (Pa), ja 1 kPa = 1000 Pa. Paineeseen paneudutaan tarkemmin myöhemmin. Kun kaasusysteemissä muutetaan yhtä tilanmuuttujaa, vähintään yksi muista muuttuu myös.

<svg data-fig="system" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa: kaasua sylinterissä, jonka yläpäätä sulkee liikkuva mäntä. Kaasu on termodynaaminen systeemi; sen rajapinta on piirretty katkoviivalla kaasun ympärille. Sylinterin seinät, mäntä ja koko muu maailma ovat ympäristöä. Systeemin tilaa kuvaavat tilanmuuttujat: paine p, tilavuus V ja lämpötila T." style="max-width:100%;font-size:24px">
  <rect x="138" y="150" width="204" height="140" fill="#eef5f9"/>
  <path d="M126,110 V302 H354 V110 H342 V290 H138 V110 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="138" y="128" width="204" height="22" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="234" y="74" width="12" height="54" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="206" y="60" width="68" height="14" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="226" cy="212" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="282" cy="184" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="322" cy="200" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="256" cy="232" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="306" cy="238" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="212" cy="262" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="270" cy="268" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="322" cy="270" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="300" cy="208" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="143" y="155" width="194" height="130" rx="4" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-dasharray="10 6"/>
  <rect x="158" y="168" width="8" height="90" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="160" y="206" width="4" height="54" fill="#c92a2a"/>
  <circle cx="162" cy="268" r="9" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="180" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="262" y1="176" x2="262" y2="168" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M262,158 L267,169 L257,169 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="302" y1="176" x2="302" y2="168" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M302,158 L307,169 L297,169 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="224" y="154.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <line x1="104" y1="150" x2="142" y2="150" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="104" y1="290" x2="142" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="110" y1="220" x2="110" y2="161" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M110,151 L115,162 L105,162 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="220" x2="110" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M110,289 L105,278 L115,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="72" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V$</div></foreignObject>
  <line x1="402" y1="235" x2="318" y2="235" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="318" cy="235" r="3" fill="#6b7480"/>
  <foreignObject x="412" y="220.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{systeemi}$</div></foreignObject>
  <line x1="402" y1="190" x2="338" y2="190" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="338" cy="190" r="3" fill="#6b7480"/>
  <foreignObject x="412" y="175.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{rajapinta}$</div></foreignObject>
  <line x1="402" y1="120" x2="350" y2="120" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="350" cy="120" r="3" fill="#6b7480"/>
  <foreignObject x="412" y="105.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ympäristö}$</div></foreignObject>
</svg>

Miksi näin käy, selittää aineen mikromalli. Kaasu koostuu hiukkasista, jotka liikkuvat jatkuvasti joka suuntaan ja törmäilevät toisiinsa ja astian seinämiin. Lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta: mitä kuumempaa kaasu on, sitä nopeammin hiukkaset keskimäärin liikkuvat. Paine syntyy, kun hiukkaset törmäävät seinämään ja jokainen törmäys työntää seinää hieman. Kun tilavuus pienenee ja lämpötila pysyy samana, hiukkasilla on vähemmän tilaa ja ne osuvat seinään useammin, joten paine kasvaa, mutta yksittäinen törmäys ei muutu kovemmaksi. Kun lämpötila nousee mutta tilavuus pysyy samana, hiukkaset osuvat seinään sekä useammin että kovempaa, joten paine kasvaa. Tästä syystä rengas tuntuu kesällä kovemmalta.

<svg data-fig="micro-model" viewBox="0 0 600 300" role="img" aria-label="Kaaviokuva kaasun mikromallista: kaksi samankokoista suljettua astiaa, joissa on yhtä monta hiukkasta. Kylmässä kaasussa nopeutta kuvaavat nuolet ovat lyhyitä, kuumassa pitkiä, ja kuuman kaasun paine p2 on suurempi kuin kylmän kaasun paine p1." style="max-width:100%;font-size:24px">
  <foreignObject x="88.5" y="25.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä kaasu}$</div></foreignObject>
  <rect x="40" y="62" width="230" height="180" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="378.5" y="25.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma kaasu}$</div></foreignObject>
  <rect x="330" y="62" width="230" height="180" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <line x1="95" y1="105" x2="104.5" y2="114.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M111,121 L100.5,117 L107,110.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="95" cy="105" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="210" y1="100" x2="199" y2="106.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M191,111 L197.5,102 L202,110 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="210" cy="100" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="155" y1="155" x2="168" y2="155" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M177,155 L167,159.5 L167,150.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="155" cy="155" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="85" y1="190" x2="94.5" y2="180.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M101,174 L97,184.5 L90.5,178 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="85" cy="190" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="215" y1="200" x2="202.5" y2="195" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M194,192 L205,191.5 L201.5,200 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="215" cy="200" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="140" y1="215" x2="153" y2="217.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M162,219 L151.5,221.5 L153,213 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="140" cy="215" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="385" y1="105" x2="409.5" y2="129.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M416,136 L405.5,132 L412,125.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="385" cy="105" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="500" y1="100" x2="470" y2="117.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M462,122 L468.5,113 L473,121 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="500" cy="100" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="445" y1="155" x2="480" y2="155" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M489,155 L479,159.5 L479,150.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="445" cy="155" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="375" y1="190" x2="399.5" y2="165.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M406,159 L402,169.5 L395.5,163 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="375" cy="190" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="505" y1="200" x2="472.5" y2="188" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M464,185 L475,184 L472,192.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="505" cy="200" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="430" y1="215" x2="464" y2="221.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M473,223 L462.5,225.5 L464,216.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="430" cy="215" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="138.5" y="257.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_1$</div></foreignObject>
  <foreignObject x="380" y="257.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_2 \gt p_1$</div></foreignObject>
</svg>

Kuva on kaaviokuva: nuolen pituus kuvaa hiukkasen nopeutta. Astiat ovat yhtä suuret, ja niissä on yhtä monta hiukkasta.

Lämpötilaa mitataan celsiusasteikolla, jossa 0 °C on veden jäätymispiste ja 100 °C veden kiehumispiste normaalipaineessa, ja kelvinasteikolla. Kelvinasteikon nollapiste on absoluuttinen nollapiste, alin mahdollinen lämpötila. Siinä hiukkasten keskimääräinen liike-energia on pienimmillään, eikä kylmempää voi olla. Celsiusasteen ja kelvinin suuruus on sama, joten lämpötilaero on sama kelvineinä ja celsiusasteina. Kun tilavuus ja kaasun määrä pysyvät samoina, kaasun paine on suoraan verrannollinen kelvinlämpötilaan. Myös hiukkasten keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan, joten lämpötilojen suhteita verrataan kelvineinä. Paineen, tilavuuden ja lämpötilan yhteyttä tutkitaan tarkemmin luvussa *Kaasujen tilanmuutokset ja Boylen laki*.

## Kaava: Kelvinasteikko
Celsiuslämpötilan $\theta$ muunnos kelvineiksi on:
```latex
T = \theta + 273{,}15
```
missä $T$ on lämpötila kelvineinä (K) ja $\theta$ lämpötila celsiusasteina (°C). Käytännössä riittää usein luku 273. Kelvineissä ei käytetä sanaa aste: sanotaan ”300 kelviniä”, ei ”300 kelvinastetta”.

Absoluuttinen nollapiste on siis 0 K = −273,15 °C. Kelvinlämpötila ei voi olla negatiivinen, mutta celsiuslämpötila voi.

<svg data-fig="kelvin-scale" viewBox="0 0 600 250" role="img" aria-label="Kelvinasteikko ja celsiusasteikko rinnakkain mittakaavassa: 0 K on −273,15 °C (absoluuttinen nollapiste), 273,15 K on 0 °C (vesi jäätyy) ja 373,15 K on 100 °C (vesi kiehuu). Asteikkojen välit ovat yhtä suuret, ja kelvinlukema saadaan lisäämällä celsiuslukemaan 273,15." style="max-width:100%;font-size:24px">
  <line x1="58" y1="112" x2="533" y2="112" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M545,112 L532,118 L532,106 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="58" y1="182" x2="533" y2="182" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M545,182 L532,188 L532,176 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="112" x2="70" y2="182" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="70" y1="104" x2="70" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="70" y1="174" x2="70" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="112" x2="398" y2="182" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="398" y1="104" x2="398" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="174" x2="398" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="518" y1="112" x2="518" y2="182" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="518" y1="104" x2="518" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="518" y1="174" x2="518" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="62" y="61.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0\,\text{K}$</div></foreignObject>
  <foreignObject x="346" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$273{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="466" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$373{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="62" y="203.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-273{,}15\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="358" y="203.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="473" y="203.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="62" y="15.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{absoluuttinen nollapiste}$</div></foreignObject>
  <foreignObject x="332" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi jäätyy}$</div></foreignObject>
  <foreignObject x="472" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi kiehuu}$</div></foreignObject>
  <foreignObject x="107" y="132.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$T = \theta + 273{,}15$</span></div></foreignObject>
  <foreignObject x="553" y="97.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="553" y="167.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta$</div></foreignObject>
</svg>

Kuva on piirretty mittakaavassa. Yläasteikko on kelvinasteikko ja alaasteikko celsiusasteikko; väli 0 °C:sta 100 °C:een on yhtä pitkä kuin väli 273,15 K:sta 373,15 K:iin.

## Esimerkki
Suljetussa jäykässä astiassa on kaasua, joten sen tilavuus ja aineen määrä pysyvät samoina. Kaasun paine mitataan eri lämpötiloissa:

| $\theta$ (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| $p$ (kPa) | 100 | 107 | 115 | 122 | 129 | 137 |

Määritä ekstrapoloimalla lämpötila, jossa kaasun paine olisi nolla.

<!-- vaihe -->

**Tunnetut ja kysytty.** Taulukossa on kuusi mittapistettä $(\theta,\, p)$, ja paine $p_0 = 100\,\text{kPa}$ lämpötilassa $0\,{}^\circ\text{C}$. Kysytään lämpötilaa $\theta_0$, jossa paine olisi nolla. Pisteet asettuvat kuvaajassa suoralle: paine kasvaa jokaista $20\,{}^\circ\text{C}$ kohti $7$–$8\,\text{kPa}$. Suoraa jatketaan vasemmalle mittausalueen ulkopuolelle eli ekstrapoloidaan.

<svg data-fig="extrapolation" viewBox="0 0 600 350" role="img" aria-label="Kaasun paine lämpötilan funktiona suljetussa astiassa: mittapisteet lämpötila-alueella 0–100 °C asettuvat suoralle, ja ekstrapoloitu suora kohtaa nollapaineen lämpötilassa noin −270 °C. Pystyakseli on kuvan vasemmassa reunassa kohdassa −300 °C." style="max-width:100%;font-size:24px">
  <line x1="120.5" y1="290" x2="120.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186.5" y1="290" x2="186.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="281" y1="290" x2="281" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375.5" y1="290" x2="375.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="255.5" x2="470" y2="255.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="221.5" x2="470" y2="221.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="187" x2="470" y2="187" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="152.5" x2="470" y2="152.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="118.5" x2="470" y2="118.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="291" x2="92" y2="70" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,58 L98,71 L86,71 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120.5" y1="290" x2="120.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-270$</div></foreignObject>
  <line x1="186.5" y1="290" x2="186.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157.5" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-200$</div></foreignObject>
  <line x1="281" y1="290" x2="281" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-100$</div></foreignObject>
  <line x1="375.5" y1="290" x2="375.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="365.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="85" y1="255.5" x2="92" y2="255.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="241" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="85" y1="221.5" x2="92" y2="221.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="207" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="85" y1="187" x2="92" y2="187" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="172.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$75$</div></foreignObject>
  <line x1="85" y1="152.5" x2="92" y2="152.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="138" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="85" y1="118.5" x2="92" y2="118.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="104" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$125$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ (^\circ\text{C})$</div></foreignObject>
  <foreignObject x="82" y="27.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <foreignObject x="60" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="120,290 375.5,152.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 7"/>
  <polyline points="375.5,152.5 470,102" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="375.5" cy="152.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="394.5" cy="143" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="413.5" cy="132" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432" cy="122.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="451" cy="113" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="470" cy="102" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="120" cy="290" r="7" fill="#ffffff" stroke="#1971c2" stroke-width="3"/>
  <foreignObject x="124" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$p = 0$</div></foreignObject>
  <foreignObject x="224.5" y="251" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ekstrapolointi}$</span></div></foreignObject>
  <foreignObject x="413.5" y="152" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{mittaukset}$</span></div></foreignObject>
</svg>

Pystyakseli on piirretty kuvan vasempaan reunaan, noin −300 °C:n kohdalle, eikä kohtaan $\theta = 0$. Yhtenäinen suora on mittausalue ja katkoviiva ekstrapolointi.

<!-- vaihe -->

**Periaate.** Astia on suljettu ja jäykkä, joten kaasun määrä ja tilavuus pysyvät samoina, ja paine riippuu vain lämpötilasta. Mittapisteet ovat suoralla, joten paine muuttuu lämpötilan mukana tasaisesti, ja suoran yhtälö antaa paineen myös mittausalueen ulkopuolella. Nollapaine on kohdassa, jossa suora leikkaa lämpötila-akselin.

<!-- vaihe -->

**Kaava ratkaistuna.** Kulmakerroin $k$ lasketaan mittausalueen päätepisteistä. Suoran yhtälössä $p_0$ on paine lämpötilassa $0\,{}^\circ\text{C}$. Asetetaan $p = 0$ ja ratkaistaan $\theta_0$:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\[4pt]
&p = p_0 + k\theta \\
&0 = p_0 + k\theta_0 \\
&\theta_0 = -\frac{p_0}{k}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunnoksia ei tarvita. Paineet ovat jo kilopascaleina, ja lämpötilaero $\Delta\theta$ on sama celsiusasteina ja kelvineinä, joten kulmakertoimen yksikkö $\tfrac{\text{kPa}}{{}^\circ\text{C}}$ on myös $\tfrac{\text{kPa}}{\text{K}}$. Tulos saadaan suoraan celsiusasteina, koska taulukon lämpötilat ovat celsiusasteina.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin kulmakerroin ja sitten nollakohta:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\
&= \frac{(137 - 100)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} \\
&= 0{,}37\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \\[6pt]
&\theta_0 = -\frac{p_0}{k} \\
&= -\frac{100\,\text{kPa}}{0{,}37\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} \\
&= -270{,}27\,{}^\circ\text{C}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Nollapaineen lämpötila on noin $-270\,{}^\circ\text{C}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska kulmakerroin $0{,}37\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ tunnetaan vain kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Tulos on lähellä absoluuttista nollapistettä $-273{,}15\,{}^\circ\text{C}$, vain noin $3\,{}^\circ\text{C}$ eli yhden prosentin päässä siitä. Riippumaton tarkistus: jos paine on verrannollinen kelvinlämpötilaan, $p = 100\,\text{kPa}$ vastaa lämpötilaa $273{,}15\,\text{K}$, joten paine lämpötilassa $100\,{}^\circ\text{C}$ olisi $100\,\text{kPa} \cdot \tfrac{373{,}15}{273{,}15} = 136{,}6\,\text{kPa}$, ja mitattu arvo on $137\,\text{kPa}$. Mikromallin mukaan nollapaineessa hiukkasten liike olisi niin vähäistä, ettei paine enää syntyisi. Todelliset kaasut nesteytyvät jo ennen tätä lämpötilaa, joten suoran jatke on vain malli ja kuvaa raja-arvoa.

## Yleinen virhekäsitys
Moni ajattelee, että lämpötila kaksinkertaistuu, kun se nousee 10 °C:sta 20 °C:een. Fysikaalisesti oikea vertailu tehdään kelvineinä: 283 K:sta 293 K:iin. Lämpötilojen suhde on 293/283 ≈ 1,035, eli nousu on noin 3,5 %. Siksi hiukkasten keskimääräinen liike-energia ei kaksinkertaistu. Toinen virhe on pitää 0 °C:ta alimpana mahdollisena lämpötilana. Se on vain veden jäätymispiste, ja alin mahdollinen lämpötila on 0 K.

## Tiivistelmä
- Termodynaaminen systeemi on rajattu osa maailmaa. Sen tilaa kuvaavat tilanmuuttujat: lämpötila, paine, tilavuus ja aineen määrä.
- Kaasusysteemissä lämpötila, paine ja tilavuus riippuvat toisistaan: jos yhtä muutetaan, vähintään yksi muista muuttuu myös.
- Mikromalli: lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, ja paine syntyy hiukkasten törmäyksistä seinämään.
- Kun tilavuus ja aineen määrä pysyvät samoina, paine on suoraan verrannollinen kelvinlämpötilaan. Mittapisteiden suoran jatkaminen eli ekstrapolointi antaa absoluuttisen nollapisteen.
- Muunnos on $T = \theta + 273{,}15$. Absoluuttinen nollapiste on 0 K = −273,15 °C.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: sama polkupyörä lumisena pakkasaamuna. Lunta on maassa ja satulalla, ja tolpan lämpömittarin pylväs on matalalla." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy33s-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="360" fill="url(#fy33s-sky)"/>
  <path d="M0,240 L10,214 L20,240 L30,214.5 L40,240 L56,192.5 L72.5,240 L85.5,202.5 L99,240 L114,195.5 L129.5,240 L141.5,207 L153.5,240 L168.5,197 L183.5,240 L193,216 L202.5,240 L218,194.5 L234,240 L250,192 L266.5,240 L277,213.5 L287,240 L303.5,192.5 L319.5,240 L329.5,215 L339.5,240 L352.5,203 L366,240 L382,192.5 L398,240 L411.5,202 L425,240 L439.5,198.5 L454,240 L470,194.5 L485.5,240 L500,197.5 L515,240 L531.5,190.5 L548.5,240 L559,211.5 L570,240 L584.5,199 L598.5,240 L609,213 L619.5,240 L629,215.5 L639,240 L653,200.5 L667,240 L682,196.5 L697,240 L712,195.5 L727.5,240 L738,212.5 L748.5,240 L760,209 L771.5,240 L783,210 L794,240 L803.5,217 L812.5,240 L823.5,211 L834.5,240 L847.5,203.5 L861,240 L873,206 L885.5,240 L898.5,203.5 L911.5,240 L926.5,197.5 L941.5,240 L952.5,210 L964,240 L980,192 L996.5,240 L1006.5,215 L1016,240 L1029,204.5 L1042,240 L1054,207 L1066,240 L1079,203.5 L1092,240 L1106,199 L1120.5,240 L1130.5,215 L1140.5,240 L1151.5,209.5 L1163,240 L1173,213.5 L1183.5,240 L1193,216.5 L1202,240 V270 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M0,250 Q300,236 600,252 V360 H0 Z" fill="#ffffff" stroke-linejoin="round"/>
  <circle cx="161.5" cy="8" r="2.11782" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="252" cy="71.5" r="2.5725" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="178" cy="118" r="3.48225" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="542" cy="188" r="3.26414" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="370.5" cy="211" r="2.2663" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="544" cy="92.5" r="2.12642" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="413" cy="123.5" r="2.41555" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="72.5" cy="182" r="2.98052" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="506.5" cy="91" r="2.88138" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="35.5" cy="110.5" r="2.31717" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="172" cy="5" r="2.05272" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="444.5" cy="104.5" r="2.27262" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="379" cy="176.5" r="3.24328" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="80" cy="139.5" r="3.57835" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="38" cy="74" r="2.38635" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="124.5" cy="135" r="2.35018" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="294" cy="211.5" r="2.1952" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="264.5" cy="111.5" r="3.98535" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="95" cy="104.5" r="2.1444" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="16" cy="16.5" r="3.60442" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="82" cy="208" r="2.77349" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="373" cy="95" r="3.50564" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="473.5" cy="136" r="3.67633" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="116" cy="166.5" r="2.99555" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="105" cy="11.5" r="2.30818" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="58.5" cy="212.5" r="2.77631" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="595.5" cy="230" r="3.38578" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="43.5" cy="140" r="3.86325" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="481.5" cy="27" r="2.27575" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="232" cy="112.5" r="3.34508" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="451.5" cy="6.5" r="2.72038" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="503" cy="75.5" r="2.73713" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="298.5" cy="38.5" r="3.33642" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="92.5" cy="210" r="2.16223" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="233" cy="78.5" r="2.10871" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="415.5" cy="175.5" r="2.47422" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="559" cy="110.5" r="2.82326" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="82.5" cy="131" r="2.60269" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="403.5" cy="81" r="2.73722" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="216" cy="58.5" r="2.79707" fill="#ffffff" stroke="#4f8fbf" stroke-width="1"/>
  <circle cx="220" cy="270" r="52" fill="none" stroke="#1f2933" stroke-width="9"/>
  <line x1="220" y1="270" x2="266" y2="270" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="260" y2="293" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="243" y2="310" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="220" y2="316" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="197" y2="310" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="180" y2="293" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="174" y2="270" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="180" y2="247" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="197" y2="230" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="220" y2="224" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="243" y2="230" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="220" y1="270" x2="260" y2="247" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <circle cx="220" cy="270" r="5" fill="#1f2933"/>
  <circle cx="400" cy="270" r="52" fill="none" stroke="#1f2933" stroke-width="9"/>
  <line x1="400" y1="270" x2="446" y2="270" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="440" y2="293" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="423" y2="310" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="400" y2="316" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="377" y2="310" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="360" y2="293" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="354" y2="270" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="360" y2="247" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="377" y2="230" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="400" y2="224" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="423" y2="230" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="400" y1="270" x2="440" y2="247" stroke="#8a96a3" stroke-width="1.2" stroke-linecap="butt"/>
  <circle cx="400" cy="270" r="5" fill="#1f2933"/>
  <path d="M220,270 L284,270 L360,196 L270,196 Z" fill="none" stroke="#1971c2" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M284,270 L258,178" fill="none" stroke="#1971c2" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M360,196 L400,270" fill="none" stroke="#1971c2" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M360,196 L354,176" fill="none" stroke="#1971c2" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M240,172 H280" fill="none" stroke="#1f2933" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M238,166 Q260,156 282,166" fill="none" stroke="#ffffff" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M340,174 Q354,166 370,176" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M150,322 Q300,316 470,322" fill="none" stroke="#4f8fbf" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.6"/>
  <rect x="511" y="80" width="18" height="150" rx="9" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="520" cy="230" r="16" fill="#1971c2" stroke="#1f2933" stroke-width="3"/>
  <rect x="516" y="200" width="8" height="30" fill="#1971c2"/>
  <line x1="529" y1="208" x2="537" y2="208" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="529" y1="186" x2="537" y2="186" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="529" y1="164" x2="537" y2="164" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="529" y1="142" x2="537" y2="142" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="529" y1="120" x2="537" y2="120" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="514" y="230" width="12" height="40" fill="#6c757d"/>
</svg>
