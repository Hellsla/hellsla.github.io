# Energian muuntuminen ja yksikkö joule

> **Miksi** polkupyörän liike on lopulta peräisin Auringosta, ja miten energian määrän voi kertoa yhdellä luvulla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: Aurinko paistaa viljapellolle. Oranssit nuolet kulkevat Auringosta viljaan, viljasta leipään ja leivästä polkupyöräilijään, joka ajaa tiellä: liikkeen energia on peräisin Auringosta." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy22h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy22h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="420" fill="url(#fy22h-sky)"/>
  <circle cx="120" cy="110" r="86.5" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M183,134 L211,134.5 L186.5,120.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M162.5,162.5 L186.5,176.5 L172.5,152.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M130.5,176.5 L144.5,201 L144,173 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M96,173 L95.5,201 L109.5,176.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M67.5,152.5 L53.5,176.5 L77.5,162.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M53.5,120.5 L29,134.5 L57,134 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M57,86 L29,85.5 L53.5,99.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M77.5,57.5 L53.5,43.5 L67.5,67.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M109.5,43.5 L95.5,19 L96,47 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M144,47 L144.5,19 L130.5,43.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M172.5,67.5 L186.5,43.5 L162.5,57.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M186.5,99.5 L211,85.5 L183,86 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="120" cy="110" r="54" fill="url(#fy22h-sun)"/>
  <path d="M688,106 Q686.5,79 718.5,82 Q731,53 763,63 Q792,47 808,77 Q837,80.5 833.5,106 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M986,162 Q985,141.5 1009,144 Q1018.5,122.5 1042.5,129.5 Q1064,117.5 1076,140.5 Q1097.5,143 1095,162 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,330 L12,307 L24.5,330 L37,305.5 L49.5,330 L65.5,297.5 L81,330 L96,298.5 L111.5,330 L133,281.5 L154.5,330 L172,292.5 L189.5,330 L207,292 L224.5,330 L242.5,292 L260,330 L278,291.5 L295.5,330 L313.5,292 L331,330 L346.5,297 L362.5,330 L383.5,282.5 L405,330 L425,285 L445.5,330 L459,302 L473,330 L492.5,287 L512,330 L531,289 L549.5,330 L571.5,281 L593,330 L609.5,295 L626,330 L647.5,282 L668.5,330 L685.5,293.5 L702.5,330 L720,293 L737,330 L754,294 L771,330 L784,304.5 L797,330 L810,305 L822.5,330 L838.5,296 L855,330 L875.5,283.5 L896.5,330 L914,291.5 L932,330 L945.5,303.5 L959,330 L976.5,292.5 L994,330 L1013.5,286.5 L1033,330 L1045.5,307 L1057.5,330 L1075.5,290 L1094,330 L1106.5,306.5 L1118.5,330 L1134.5,296.5 L1150.5,330 L1164,302 L1178,330 L1197.5,287.5 L1217,330 V360 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="360" width="1200" height="240" fill="#b2f2bb"/>
  <rect x="0" y="380" width="420" height="120" fill="#d9b26a"/>
  <line x1="12" y1="500" x2="16" y2="402" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="16" cy="396" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="28" y1="500" x2="32" y2="407.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="32" cy="401.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="44" y1="500" x2="48" y2="405.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="48" cy="399.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="60" y1="500" x2="64" y2="404.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="64" cy="398.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="76" y1="500" x2="80" y2="402.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="80" cy="396.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="92" y1="500" x2="96" y2="408" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="96" cy="402" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="108" y1="500" x2="112" y2="407.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="112" cy="401.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="124" y1="500" x2="128" y2="405" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="128" cy="399" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="140" y1="500" x2="144" y2="405" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="144" cy="399" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="156" y1="500" x2="160" y2="405" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="160" cy="399" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="172" y1="500" x2="176" y2="400" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="176" cy="394" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="188" y1="500" x2="192" y2="406" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="192" cy="400" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="204" y1="500" x2="208" y2="406" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="208" cy="400" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="220" y1="500" x2="224" y2="404" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="224" cy="398" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="236" y1="500" x2="240" y2="408.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="240" cy="402.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="252" y1="500" x2="256" y2="403.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="256" cy="397.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="268" y1="500" x2="272" y2="404" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="272" cy="398" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="284" y1="500" x2="288" y2="402.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="288" cy="396.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="300" y1="500" x2="304" y2="410" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="304" cy="404" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="316" y1="500" x2="320" y2="407" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="320" cy="401" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="332" y1="500" x2="336" y2="408.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="336" cy="402.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="348" y1="500" x2="352" y2="408.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="352" cy="402.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="364" y1="500" x2="368" y2="400.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="368" cy="394.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="380" y1="500" x2="384" y2="406.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="384" cy="400.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="396" y1="500" x2="400" y2="409.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="400" cy="403.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <line x1="412" y1="500" x2="416" y2="402.5" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="416" cy="396.5" rx="5" ry="12" fill="#e9c98a" stroke="#a97a35" stroke-width="1.5"/>
  <path d="M0,520 H1200 V600 H0 Z" fill="#6c757d" stroke-linejoin="round"/>
  <path d="M0,560 H1200" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" stroke-dasharray="40 30"/>
  <rect x="470" y="420" width="150" height="18" rx="4" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <path d="M482,420 Q480,360 545,356 Q610,360 608,420 Z" fill="#d9b26a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M510,384 q10,-10 18,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <path d="M536,384 q10,-10 18,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <path d="M562,384 q10,-10 18,0" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="820" cy="460" r="50" fill="none" stroke="#1f2933" stroke-width="6"/>
  <circle cx="820" cy="460" r="6" fill="#1f2933"/>
  <circle cx="980" cy="460" r="50" fill="none" stroke="#1f2933" stroke-width="6"/>
  <circle cx="980" cy="460" r="6" fill="#1f2933"/>
  <path d="M820,460 L880,460 L940,380 L860,380 Z M880,460 L854,360 M980,460 L950,350" fill="none" stroke="#c92a2a" stroke-width="7" stroke-linejoin="round" stroke-linejoin="round"/>
  <line x1="838" y1="358" x2="870" y2="358" stroke="#1f2933" stroke-width="8" stroke-linecap="round"/>
  <line x1="940" y1="348" x2="970" y2="342" stroke="#1f2933" stroke-width="6" stroke-linecap="round"/>
  <path d="M854,352 L890,410 L880,460" fill="none" stroke="#1f2933" stroke-width="18" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M854,350 L898,250" fill="none" stroke="#1971c2" stroke-width="40" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M886,272 L954,342" fill="none" stroke="#1971c2" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="956" cy="342" r="10" fill="#f1dfb5"/>
  <circle cx="912" cy="214" r="28" fill="#f1dfb5"/>
  <path d="M882,208 Q892,174 922,180 Q944,186 940,210 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M183.5,163 L252.5,309.5 L243.5,313.5 L270,330 L274.5,299 L265.5,303.5 L196.5,157 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M420.5,407 L440.5,405 L441.5,415 L466,396 L438.5,381.5 L439.5,391.5 L419.5,393 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M632.5,386.5 L799,316.5 L802.5,326 L820,300 L789.5,294.5 L793.5,303.5 L627.5,373.5 Z" fill="#e8590c" stroke-linejoin="round"/>
</svg>

## Ydinajatus
### Energia muuttuu muodosta toiseen
Energia on suure, jonka avulla kuvataan, mitä systeemissä voi tapahtua. Se esiintyy eri muodoissa, kuten mekaanisena, kemiallisena, sähköisenä, lämpöenergiana, säteilynä ja ydinenergiana (luku *Energialajit ja energian säilyminen*). Arjessa energia kulkee harvoin yhdessä muodossa: se muuttuu muodosta toiseen vaiheiden ketjussa.

Pyöräilijän ketju alkaa Auringosta. Säteilyenergia sitoutuu kasvissa kemialliseksi energiaksi, ja se päätyy kauraan ja aamupuuroon. Lihakset muuttavat puuron kemiallisesta energiasta osan pyörän liikkeeksi, ja pysähtyessä liike-energia muuttuu lopulta renkaiden, jarrujen ja ilman lämpöenergiaksi.

<svg data-fig="ketju" viewBox="0 0 600 370" role="img" aria-label="Kaavakuva: energiaketju Auringosta pyöräilyyn. Aurinko lähettää säteilyenergiaa, kasvi (kaura) sitoo sen kemialliseksi energiaksi ruokaan, lihakset muuttavat osan siitä pyörän liikkeeksi ja loppu muuttuu lämpöenergiaksi. Joka vaiheessa osa energiasta siirtyy lämpönä ympäristöön (oranssit nuolet alas), ja lopuksi myös liike-energia muuttuu lämpöenergiaksi. Nuolten pituus ei ole mittakaavassa." style="max-width:100%;font-size:24px">
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

Joka vaiheessa osa energiasta muuttuu lämpöenergiaksi, joka siirtyy lämpönä ympäristöön ja hajaantuu. Energiaa ei silti katoa: kuten luvussa *Energialajit ja energian säilyminen* todettiin, ketjun alussa ja lopussa sitä on yhtä paljon. Kuvan esimerkissä puuron $800\,\text{kJ}$ jakautuu liikkeeksi ja lämpöenergiaksi, ja osat ovat yhteensä yhtä paljon kuin alussa. Lämpöenergia hajaantuu niin laajalle, ettei sitä ole enää helppo käyttää hyödyksi, ja siksi energia tuntuu "kuluvan loppuun".

<svg data-fig="sailyminen" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva mittakaavassa (esimerkki): pyöräilijän aamupuuron kemiallisesta energiasta 800 kJ lihakset muuttavat liikkeeksi 200 kJ ja lämpöenergiaksi 600 kJ. Nuolten leveys on verrannollinen energiaan, ja haarojen yhteinen leveys on yhtä suuri kuin alkuperäisen nuolen leveys." style="max-width:100%;font-size:24px">
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
Energian symboli on $E$ ja yksikkö joule, jonka merkki on J. Yksi joule on pieni energia: se on suunnilleen se, mitä tarvitaan noin $0{,}1\,\text{kg}$:n omenan nostamiseen metrin verran. Tässä luvussa joulen suuruus opitaan esimerkkien avulla.

## Kaava: Energian yksikkö ja kerrannaisyksiköt
Arjen energiat ovat jouleina isoja lukuja, joten käytetään etuliitteitä (luku *Suureet, yksiköt ja SI-järjestelmä*): kilo (k), mega (M), giga (G) ja tera (T). Jokainen niistä on tuhatkertainen edelliseen verrattuna:
```latex
\begin{aligned}
1\,\text{kJ} &= 1000\,\text{J} \\
1\,\text{MJ} &= 1000\,\text{kJ} \\
1\,\text{GJ} &= 1000\,\text{MJ} \\
1\,\text{TJ} &= 1000\,\text{GJ}
\end{aligned}
```
missä J on joule, kJ kilojoule, MJ megajoule, GJ gigajoule ja TJ terajoule. Megajoulessa on siis $1000 \cdot 1000\,\text{J} = 1\,000\,000\,\text{J}$.

Muunnos tehdään korvaamalla etuliite sen arvolla: $2{,}5\,\text{kJ} = 2{,}5 \cdot 1000\,\text{J} = 2500\,\text{J}$. Toiseen suuntaan luku kirjoitetaan etuliitteen avulla: $3000\,\text{J} = 3 \cdot 1000\,\text{J} = 3\,\text{kJ}$. Energioita lasketaan yhteen vain samassa yksikössä, joten ne muunnetaan ensin samaan yksikköön.

Arjen energioiden suuruusluokat on koottu kuvaan, jossa jokainen väli on kymmenkertainen (luku *Fysiikka tieteenä ja maailmankaikkeuden mittasuhteet*). Kun kahden energian kertaluku on hyvin erilainen, vertailuun riittää yksi jakolasku: bensiinilitran $32\,\text{MJ}$ ja päivän ruoan $10\,\text{MJ}$ suhde on $32\,\text{MJ} : 10\,\text{MJ} \approx 3$.

<svg data-fig="tikapuut" viewBox="0 0 600 372" role="img" aria-label="Kuvaaja mittakaavassa: energia jouleina kymmenpotenssiasteikolla 1 J:sta 10 TJ:iin ja yli. Jokainen väli on kymmenkertainen. Omena metrin ylös on noin 1 J, palava tulitikku noin 1 kJ, päivän ruoka noin 10 MJ, 50 litran bensiinitankki noin 1,6 GJ ja ydinvoimala Olkiluoto 3 tuottaa vuorokaudessa noin 140 TJ sähköä." style="max-width:100%;font-size:24px">
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
Pyöräilijä syö banaanin, jonka kemiallinen energia on $0{,}45\,\text{MJ}$. Lihakset muuttavat siitä pyöräilyn liikkeeksi $110\,\text{kJ}$, ja loppu muuttuu lämpöenergiaksi. Kuinka paljon energiaa muuttuu lihaksissa ja kehossa lämpöenergiaksi? Anna vastaus kilojouleina.

<!-- vaihe -->

**Tunnetut ja kysytty.** Kemiallinen energia alussa $E_\text{alussa} = 0{,}45\,\text{MJ}$ ja liikkeeksi muuttunut energia $E_\text{liike} = 110\,\text{kJ}$. Kysytään lämpöenergiaa $E_\text{lämpö}$ kilojouleina.

<!-- vaihe -->

**Periaate.** Energia säilyy: banaanin kemiallinen energia ei katoa, vaan se muuttuu kokonaan liikkeeksi ja lämpöenergiaksi. Alun energia on siis yhtä suuri kuin liikkeeksi ja lämpöenergiaksi muuttuneiden energioiden summa.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&E_\text{alussa} = E_\text{liike} + E_\text{lämpö} \\
&E_\text{lämpö} = E_\text{alussa} - E_\text{liike}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Energiat lasketaan samassa yksikössä. Korvataan megajoulen etuliite sen arvolla: $0{,}45\,\text{MJ} = 0{,}45 \cdot 1000\,\text{kJ} = 450\,\text{kJ}$.

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

**Tulos.** Lämpöenergiaksi muuttuu $340\,\text{kJ}$. Tulos on pyöristetty kahden merkitsevän numeron tarkkuuteen, koska alkuenergia $0{,}45\,\text{MJ}$ ja liike $110\,\text{kJ}$ on annettu kahdella numerolla.

<!-- vaihe -->

**Järkevyys.** Lämpöenergiaksi muuttuu enemmän energiaa kuin liikkeeksi, kuten ihmisen lihasten toiminnassa yleensä: keho lämpenee pyöräillessä. Summa tarkistuu: $110\,\text{kJ} + 340\,\text{kJ} = 450\,\text{kJ}$, eli sama kuin alussa.

## Yleinen virhekäsitys
Moni ajattelee, että energia kuluu loppuun, kun vauhti hidastuu tai akku tyhjenee. Energia ei kulu eikä katoa. Se muuttaa muotoa, ja suuri osa päätyy lämpönä ympäristöön, josta sitä ei enää helposti saa takaisin hyötykäyttöön.

Toinen virhe on laskea yhteen energioita eri yksiköissä, esimerkiksi $1{,}5\,\text{MJ} + 300\,\text{kJ} = 301{,}5$. Etuliite on kerroin, joten energiat muunnetaan ensin samaan yksikköön.

## Tiivistelmä
- Energia muuttuu ketjussa muodosta toiseen, esimerkiksi säteily, kemiallinen energia, liike-energia ja lämpöenergia.
- Energia säilyy (luku *Energialajit ja energian säilyminen*). Osa muuttuu joka vaiheessa lämpöenergiaksi, joka siirtyy lämpönä ympäristöön.
- Energian yksikkö on joule (J). Etuliitteet: $1\,\text{kJ} = 1000\,\text{J}$, $1\,\text{MJ} = 1000\,\text{kJ}$, $1\,\text{GJ} = 1000\,\text{MJ}$ ja $1\,\text{TJ} = 1000\,\text{GJ}$.
- Etuliite korvataan arvollaan: $2{,}5\,\text{kJ} = 2{,}5 \cdot 1000\,\text{J}$. Energioita lasketaan yhteen samassa yksikössä.
- Arjen energiat ulottuvat jouleista terajouleihin, ja vertailu tehdään kymmenpotensseina.
