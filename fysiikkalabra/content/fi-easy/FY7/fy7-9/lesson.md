# Sähkömagneettinen säteily ja mustan kappaleen spektri

> **Miksi** ahjossa kuumeneva rautatanko hehkuu ensin punaisena ja sitten yhä keltaisempana, ja miksi lämpökamera näkee ihmisen pilkkopimeässäkin?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: hämärässä pajassa ahjon hiillos hehkuu. Ahjosta lähtee pitkä rautatanko oikealla olevaa alasinta kohti. Tangon kuuma pää hiilloksessa on lähes valkoinen. Siitä poispäin tanko hehkuu keltaisena, oranssina ja punaisena. Kylmä pää alasimen päällä on tumman harmaa. Tangon kuuman osan yllä väreilee lämpö." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy79h-wall" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="470"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#6c757d"/></linearGradient><linearGradient id="fy79h-floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy79h-halo" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078"/><stop offset="0.55" stop-color="#e8590c" stop-opacity="0.8"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient><radialGradient id="fy79h-rodglow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078"/><stop offset="0.55" stop-color="#e8590c" stop-opacity="0.8"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient><linearGradient id="fy79h-rodg" gradientUnits="userSpaceOnUse" x1="470" y1="0" x2="1050" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="0.14" stop-color="#ffc078"/><stop offset="0.3" stop-color="#e8590c"/><stop offset="0.46" stop-color="#c92a2a"/><stop offset="0.62" stop-color="#6c757d"/><stop offset="1" stop-color="#6c757d"/></linearGradient><radialGradient id="fy79h-coal" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffc078"/><stop offset="0.55" stop-color="#e8590c" stop-opacity="0.8"/><stop offset="1" stop-color="#e8590c" stop-opacity="0"/></radialGradient><linearGradient id="fy79h-handle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy79h-wall)"/>
  <line x1="0" y1="40" x2="1200" y2="40" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="40" x2="60" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="40" x2="180" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="40" x2="300" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="40" x2="420" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="40" x2="540" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="40" x2="660" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="40" x2="780" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="40" x2="900" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="40" x2="1020" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1140" y1="40" x2="1140" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="90" x2="1200" y2="90" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="90" x2="0" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="90" x2="120" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="90" x2="240" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="90" x2="360" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="90" x2="480" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="90" x2="600" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="720" y1="90" x2="720" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="840" y1="90" x2="840" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="960" y1="90" x2="960" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1080" y1="90" x2="1080" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="140" x2="1200" y2="140" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="140" x2="60" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="140" x2="180" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="140" x2="300" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="140" x2="420" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="140" x2="540" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="140" x2="660" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="140" x2="780" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="140" x2="900" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="140" x2="1020" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1140" y1="140" x2="1140" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="190" x2="1200" y2="190" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="190" x2="0" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="190" x2="120" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="190" x2="240" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="190" x2="360" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="190" x2="480" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="190" x2="600" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="720" y1="190" x2="720" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="840" y1="190" x2="840" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="960" y1="190" x2="960" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1080" y1="190" x2="1080" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="240" x2="1200" y2="240" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="240" x2="60" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="240" x2="180" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="240" x2="300" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="240" x2="420" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="240" x2="540" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="240" x2="660" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="240" x2="780" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="240" x2="900" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="240" x2="1020" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1140" y1="240" x2="1140" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="290" x2="1200" y2="290" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="290" x2="0" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="290" x2="120" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="290" x2="240" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="290" x2="360" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="290" x2="480" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="290" x2="600" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="720" y1="290" x2="720" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="840" y1="290" x2="840" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="960" y1="290" x2="960" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1080" y1="290" x2="1080" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="340" x2="1200" y2="340" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="340" x2="60" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="340" x2="180" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="340" x2="300" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="340" x2="420" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="340" x2="540" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="340" x2="660" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="340" x2="780" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="340" x2="900" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1020" y1="340" x2="1020" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1140" y1="340" x2="1140" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="390" x2="1200" y2="390" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="390" x2="0" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="390" x2="120" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="390" x2="240" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="390" x2="360" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="390" x2="480" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="390" x2="600" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="720" y1="390" x2="720" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="840" y1="390" x2="840" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="960" y1="390" x2="960" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1080" y1="390" x2="1080" y2="440" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy79h-floor)"/>
  <ellipse cx="540" cy="300" rx="380" ry="230" fill="url(#fy79h-halo)" fill-opacity="0.5"/>
  <path d="M190,210 L240,90 H440 L490,210 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="300" y="0" width="80" height="92" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="180" y="300" width="320" height="170" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="3"/>
  <line x1="180" y1="342" x2="500" y2="342" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="384" x2="500" y2="384" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="426" x2="500" y2="426" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220" y1="300" x2="220" y2="342" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="300" x2="300" y2="342" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="380" y2="342" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="460" y1="300" x2="460" y2="342" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="260" y1="342" x2="260" y2="384" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="340" y1="342" x2="340" y2="384" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="342" x2="420" y2="384" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220" y1="384" x2="220" y2="426" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="384" x2="300" y2="426" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="384" x2="380" y2="426" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="460" y1="384" x2="460" y2="426" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="260" y1="426" x2="260" y2="468" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="340" y1="426" x2="340" y2="468" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="426" x2="420" y2="468" stroke="#a97a35" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="620" cy="292" rx="190" ry="70" fill="url(#fy79h-rodglow)" fill-opacity="0.7"/>
  <path d="M330,268 L1050,312 L1048,340 L328,296 Z" fill="url(#fy79h-rodg)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M190,300 Q340,250 490,300 Z" fill="#e8590c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="205.5" cy="295.5" r="10.4743" fill="#1f2933" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="224" cy="294.5" r="11.6728" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="241.5" cy="293" r="9.32446" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="262.5" cy="288" r="9.21742" fill="#1f2933" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="279" cy="286.5" r="9.94844" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="298.5" cy="284.5" r="10.6465" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="315.5" cy="287.5" r="10.2054" fill="#1f2933" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="330.5" cy="283.5" r="10.4744" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="352" cy="286.5" r="10.5941" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="366.5" cy="285" r="11.4412" fill="#1f2933" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="385.5" cy="287.5" r="10.2341" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="405.5" cy="289.5" r="11.0652" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="423" cy="290" r="11.4097" fill="#1f2933" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="438.5" cy="290.5" r="11.3654" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="456.5" cy="293.5" r="12.4449" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="475" cy="297.5" r="11.8546" fill="#1f2933" stroke="#1f2933" stroke-width="1.5"/>
  <ellipse cx="340" cy="286" rx="140" ry="32" fill="url(#fy79h-coal)" fill-opacity="0.85"/>
  <circle cx="427" cy="220" r="3" fill="#ffc078"/>
  <circle cx="325.5" cy="246.5" r="3" fill="#ffc078"/>
  <circle cx="346.5" cy="217.5" r="3" fill="#ffc078"/>
  <circle cx="361.5" cy="249.5" r="3" fill="#ffc078"/>
  <circle cx="297" cy="250" r="3" fill="#ffc078"/>
  <circle cx="374.5" cy="259" r="3" fill="#ffc078"/>
  <circle cx="331.5" cy="222.5" r="3" fill="#ffc078"/>
  <path d="M560,262 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#ffc078" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M620,262 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#ffc078" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M680,262 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#ffc078" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M740,262 q-12,-15 0,-30 t0,-30 t0,-30" fill="none" stroke="#ffc078" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M900,340 H1120 Q1120,362 1090,368 L1060,372 V410 L1090,470 H930 L960,410 V372 L930,366 Q880,356 860,340 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="1112" y="326" width="76" height="12" rx="6" fill="url(#fy79h-handle)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1074" y="310" width="42" height="30" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
</svg>

## Ydinajatus

### Muuttuvat kentät synnyttävät toisensa
Luvussa *Sähkömagneettinen induktio* nähtiin, että muuttuva magneettivuo indusoi johdinsilmukkaan jännitteen. Jännite syntyy, koska muuttuva magneettikenttä synnyttää ympärilleen sähkökentän. Sähkökenttä liikuttaa johtimen elektroneja. Myös käänteinen ilmiö on totta: muuttuva sähkökenttä synnyttää magneettikentän. Kun sähkökenttä jossakin kohdassa muuttuu, se synnyttää ympärilleen muuttuvan magneettikentän. Muuttuva magneettikenttä taas synnyttää muuttuvan sähkökentän, ja niin edelleen. Näin syntyy **sähkömagneettinen aalto**. Se etenee ilman väliainetta, myös tyhjiön läpi. Valo, radioaallot ja röntgensäteily ovat kaikki tällaisia aaltoja. Niitä kutsutaan yhteisellä nimellä **sähkömagneettinen säteily**.

### Kentät ovat kohtisuorassa toisiaan ja etenemissuuntaa vastaan
Sähkömagneettisessa aallossa sähkökenttä $\overline{E}$ ja magneettikenttä $\overline{B}$ värähtelevät samassa tahdissa. Ne ovat suurimmillaan ja nollassa samoissa kohdissa. Kentät ovat kohtisuorassa toisiaan vastaan. Kumpikin kenttä on myös kohtisuorassa aallon etenemissuuntaa vastaan. Aalto on siis poikittainen kuten aalto narussa (luku *Mekaaninen aaltoliike*). Mikään aine ei kuitenkaan värähtele, vaan värähtelevät kentät. Tyhjiössä kaikki sähkömagneettiset aallot etenevät samalla nopeudella eli valon nopeudella $c = 3{,}00 \cdot 10^{8}\,\text{m/s}$. Ilmassa nopeus on lähes sama.

<svg data-fig="wave" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva sähkömagneettisesta aallosta yhdellä hetkellä, ei mittakaavassa. Aalto etenee vasemmalta oikealle vaakasuoraa akselia pitkin. Ruskea sähkökenttä E värähtelee pystysuunnassa. Vihreä magneettikenttä B värähtelee vinosti piirretyssä vaakatasossa. Se on kohtisuorassa sekä sähkökenttää että etenemissuuntaa vastaan. Kentät ovat samassa vaiheessa: ne ovat suurimmillaan ja nollassa samoissa kohdissa. Kahden peräkkäisen sähkökentän huipun välinen etäisyys on aallonpituus lambda. Aalto etenee nopeudella c." style="max-width:100%;font-size:24px">
  <line x1="87.5" y1="175" x2="87.5" y2="125" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="87.5" y1="175" x2="62.5" y2="194" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="105" y1="175" x2="105" y2="88.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="105" y1="175" x2="62" y2="208.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="122.5" y1="175" x2="122.5" y2="75" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="122.5" y1="175" x2="73" y2="213.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="175" x2="140" y2="88.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="175" x2="97" y2="208.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="157.5" y1="175" x2="157.5" y2="125" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="157.5" y1="175" x2="132.5" y2="194" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="175" x2="192.5" y2="225" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="175" x2="217.5" y2="156" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="175" x2="210" y2="261.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="175" x2="253" y2="141.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="227.5" y1="175" x2="227.5" y2="275" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="227.5" y1="175" x2="277" y2="136.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="245" y1="175" x2="245" y2="261.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="245" y1="175" x2="288" y2="141.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262.5" y1="175" x2="262.5" y2="225" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262.5" y1="175" x2="287.5" y2="156" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="297.5" y1="175" x2="297.5" y2="125" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="297.5" y1="175" x2="272.5" y2="194" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="315" y1="175" x2="315" y2="88.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="315" y1="175" x2="272" y2="208.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332.5" y1="175" x2="332.5" y2="75" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332.5" y1="175" x2="283" y2="213.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="175" x2="350" y2="88.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="175" x2="307" y2="208.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367.5" y1="175" x2="367.5" y2="125" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367.5" y1="175" x2="342.5" y2="194" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="402.5" y1="175" x2="402.5" y2="225" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="402.5" y1="175" x2="427.5" y2="156" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="175" x2="420" y2="261.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="175" x2="463" y2="141.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="437.5" y1="175" x2="437.5" y2="275" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="437.5" y1="175" x2="487" y2="136.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="175" x2="455" y2="261.5" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="175" x2="498" y2="141.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472.5" y1="175" x2="472.5" y2="225" stroke="#8a5f22" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472.5" y1="175" x2="497.5" y2="156" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M70,175 L69,178 L67.5,180.5 L66.5,183.5 L65.5,186.5 L64.5,189 L63.5,191.5 L62.5,194 L62,196.5 L61.5,199 L61.5,201 L61,203 L61,205 L61.5,206.5 L62,208.5 L63,209.5 L64,210.5 L65,211.5 L66.5,212.5 L68.5,213 L70.5,213.5 L73,213.5 L75.5,213.5 L78.5,213 L81.5,212.5 L85,211.5 L89,210.5 L93,209.5 L97,208.5 L101.5,206.5 L106,205 L111,203 L116.5,201 L121.5,199 L127,196.5 L132.5,194 L138.5,191.5 L144.5,189 L150.5,186.5 L156.5,183.5 L162.5,180.5 L169,178 L175,175 L181,172 L187.5,169.5 L193.5,166.5 L199.5,163.5 L205.5,161 L211.5,158.5 L217.5,156 L223,153.5 L228.5,151 L233.5,149 L239,147 L244,145 L248.5,143.5 L253,141.5 L257,140.5 L261,139.5 L265,138.5 L268.5,137.5 L271.5,137 L274.5,136.5 L277,136.5 L279.5,136.5 L281.5,137 L283.5,137.5 L285,138.5 L286,139.5 L287,140.5 L288,141.5 L288.5,143.5 L289,145 L289,147 L288.5,149 L288.5,151 L288,153.5 L287.5,156 L286.5,158.5 L285.5,161 L284.5,163.5 L283.5,166.5 L282.5,169.5 L281,172 L280,175 L279,178 L277.5,180.5 L276.5,183.5 L275.5,186.5 L274.5,189 L273.5,191.5 L272.5,194 L272,196.5 L271.5,199 L271.5,201 L271,203 L271,205 L271.5,206.5 L272,208.5 L273,209.5 L274,210.5 L275,211.5 L276.5,212.5 L278.5,213 L280.5,213.5 L283,213.5 L285.5,213.5 L288.5,213 L291.5,212.5 L295,211.5 L299,210.5 L303,209.5 L307,208.5 L311.5,206.5 L316,205 L321,203 L326.5,201 L331.5,199 L337,196.5 L342.5,194 L348.5,191.5 L354.5,189 L360.5,186.5 L366.5,183.5 L372.5,180.5 L379,178 L385,175 L391,172 L397.5,169.5 L403.5,166.5 L409.5,163.5 L415.5,161 L421.5,158.5 L427.5,156 L433,153.5 L438.5,151 L443.5,149 L449,147 L454,145 L458.5,143.5 L463,141.5 L467,140.5 L471,139.5 L475,138.5 L478.5,137.5 L481.5,137 L484.5,136.5 L487,136.5 L489.5,136.5 L491.5,137 L493.5,137.5 L495,138.5 L496,139.5 L497,140.5 L498,141.5 L498.5,143.5 L499,145 L499,147 L498.5,149 L498.5,151 L498,153.5 L497.5,156 L496.5,158.5 L495.5,161 L494.5,163.5 L493.5,166.5 L492.5,169.5 L491,172 L490,175" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round"/>
  <line x1="50" y1="175" x2="520" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M70,175 L72.5,167.5 L75,160 L77.5,152.5 L80,145.5 L82.5,138.5 L85,131.5 L87.5,125 L90,118.5 L92.5,112.5 L95,107 L97.5,101.5 L100,97 L102.5,92.5 L105,88.5 L107.5,85 L110,82 L112.5,79.5 L115,77.5 L117.5,76 L120,75.5 L122.5,75 L125,75.5 L127.5,76 L130,77.5 L132.5,79.5 L135,82 L137.5,85 L140,88.5 L142.5,92.5 L145,97 L147.5,101.5 L150,107 L152.5,112.5 L155,118.5 L157.5,125 L160,131.5 L162.5,138.5 L165,145.5 L167.5,152.5 L170,160 L172.5,167.5 L175,175 L177.5,182.5 L180,190 L182.5,197.5 L185,204.5 L187.5,211.5 L190,218.5 L192.5,225 L195,231.5 L197.5,237.5 L200,243 L202.5,248.5 L205,253 L207.5,257.5 L210,261.5 L212.5,265 L215,268 L217.5,270.5 L220,272.5 L222.5,274 L225,274.5 L227.5,275 L230,274.5 L232.5,274 L235,272.5 L237.5,270.5 L240,268 L242.5,265 L245,261.5 L247.5,257.5 L250,253 L252.5,248.5 L255,243 L257.5,237.5 L260,231.5 L262.5,225 L265,218.5 L267.5,211.5 L270,204.5 L272.5,197.5 L275,190 L277.5,182.5 L280,175 L282.5,167.5 L285,160 L287.5,152.5 L290,145.5 L292.5,138.5 L295,131.5 L297.5,125 L300,118.5 L302.5,112.5 L305,107 L307.5,101.5 L310,97 L312.5,92.5 L315,88.5 L317.5,85 L320,82 L322.5,79.5 L325,77.5 L327.5,76 L330,75.5 L332.5,75 L335,75.5 L337.5,76 L340,77.5 L342.5,79.5 L345,82 L347.5,85 L350,88.5 L352.5,92.5 L355,97 L357.5,101.5 L360,107 L362.5,112.5 L365,118.5 L367.5,125 L370,131.5 L372.5,138.5 L375,145.5 L377.5,152.5 L380,160 L382.5,167.5 L385,175 L387.5,182.5 L390,190 L392.5,197.5 L395,204.5 L397.5,211.5 L400,218.5 L402.5,225 L405,231.5 L407.5,237.5 L410,243 L412.5,248.5 L415,253 L417.5,257.5 L420,261.5 L422.5,265 L425,268 L427.5,270.5 L430,272.5 L432.5,274 L435,274.5 L437.5,275 L440,274.5 L442.5,274 L445,272.5 L447.5,270.5 L450,268 L452.5,265 L455,261.5 L457.5,257.5 L460,253 L462.5,248.5 L465,243 L467.5,237.5 L470,231.5 L472.5,225 L475,218.5 L477.5,211.5 L480,204.5 L482.5,197.5 L485,190 L487.5,182.5 L490,175" fill="none" stroke="#8a5f22" stroke-width="3" stroke-linejoin="round"/>
  <line x1="122.5" y1="175" x2="122.5" y2="88" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <path d="M122.5,75 L129,89 L116,89 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <line x1="122.5" y1="175" x2="83" y2="205.5" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M73,213.5 L80,200 L88,210 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="134.5" y="66.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$\overline{E}$</div></foreignObject>
  <foreignObject x="34" y="223" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <line x1="122.5" y1="49" x2="332.5" y2="49" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="122.5" y1="41" x2="122.5" y2="57" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="332.5" y1="41" x2="332.5" y2="57" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210.5" y="14.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <line x1="512" y1="175" x2="561" y2="175" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M576,175 L560,182 L560,168 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="537" y="134.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$c$</div></foreignObject>
</svg>

### Aallonpituus ja taajuus
Sähkömagneettinen aalto etenee yhden jaksonajan aikana yhden aallonpituuden verran, aivan kuten mekaaninen aalto. Siksi valon nopeus, aallon taajuus ja aallonpituus liittyvät toisiinsa:
```latex
c = f \lambda
```
missä $c$ on valon nopeus tyhjiössä (m/s), $f$ on taajuus (Hz) ja $\lambda$ on aallonpituus (m). Luku $c$ on kaikille sähkömagneettisille aalloille sama. Siksi suurempi taajuus tarkoittaa lyhyempää aallonpituutta. Esimerkiksi FM-radion noin $100\,\text{MHz}$:n aallon aallonpituus on $3{,}0\,\text{m}$. Mikroaaltouunin $2{,}45\,\text{GHz}$:n aallon aallonpituus on noin $12\,\text{cm}$.

### Lähteenä kiihtyvässä liikkeessä oleva varaus
Levossa olevan varauksen ympärillä on sähkökenttä, joka ei muutu. Tasaisella nopeudella suoraan liikkuvan varauksen kentät kulkevat sen mukana, eikä se säteile. Sähkömagneettista säteilyä syntyy, kun varattu hiukkanen on **kiihtyvässä liikkeessä**. Silloin sen kentän muutos lähtee etenemään ympäristöön valon nopeudella. Lähettimen antennissa vaihtojännite saa elektronit värähtelemään edestakaisin. Antenni lähettää aaltoa, jonka taajuus on sama kuin vaihtovirran taajuus (luku *Generaattori ja vaihtovirta*). Matkapuhelin ja langattoman verkon tukiasema toimivat samoin. Vastaanottimen antennissa saapuvan aallon sähkökenttä liikuttaa elektroneja, ja antenniin syntyy heikko vaihtovirta.

<svg data-fig="antenna" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa: pystysuora sauva-antenni. Sen kaksi metallisauvaa on kytketty keskeltä vaihtojännitelähteeseen. Violetti nuoli sauvojen vieressä näyttää, että virta kulkee tällä hetkellä ylöspäin. Puolen jaksonajan kuluttua se kulkee alaspäin. Antennista lähtee oikealle kaaria, jotka kuvaavat etenevän aallon harjoja. Ruskeat nuolet vaaka-akselilla näyttävät sähkökentän. Se on antennin suuntainen ja vaihtaa suuntaa puolen aallonpituuden välein. Kahden samansuuntaisen harjan välinen etäisyys on aallonpituus lambda." style="max-width:100%;font-size:24px">
  <path d="M149.5,72.5 A105,105 0 0 1 149.5,267.5" fill="none" stroke="#c9c2b2" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="8 6"/>
  <path d="M268.5,32 A210,210 0 0 1 268.5,308" fill="none" stroke="#c9c2b2" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="8 6"/>
  <path d="M393,32 A315,315 0 0 1 393,308" fill="none" stroke="#c9c2b2" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="8 6"/>
  <path d="M506.5,32 A420,420 0 0 1 506.5,308" fill="none" stroke="#c9c2b2" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="8 6"/>
  <line x1="215" y1="170" x2="215" y2="136" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <path d="M215,124 L221,137 L209,137 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <line x1="320" y1="170" x2="320" y2="204" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <path d="M320,216 L314,203 L326,203 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <line x1="425" y1="170" x2="425" y2="136" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <path d="M425,124 L431,137 L419,137 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <line x1="530" y1="170" x2="530" y2="204" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <path d="M530,216 L524,203 L536,203 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <line x1="124" y1="170" x2="560" y2="170" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <foreignObject x="225" y="111.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$\overline{E}$</div></foreignObject>
  <rect x="104" y="52" width="12" height="100" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="104" y="188" width="12" height="100" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M104,150 H48 V148" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M104,190 H48 V192" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="48" cy="170" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M35,170 C41.5,155 48,155 48,170 C48,185 54.5,185 61,170" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="132" y1="140" x2="132" y2="78" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M132,66 L138,79 L126,79 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="132" y1="274" x2="132" y2="212" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M132,200 L138,213 L126,213 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="146" y="89.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="124" y="15.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{antenni}$</div></foreignObject>
  <line x1="215" y1="276" x2="425" y2="276" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="215" y1="268" x2="215" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="425" y1="268" x2="425" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="303" y="285.5" width="34" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <line x1="486" y1="52" x2="551" y2="52" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M566,52 L550,59 L550,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="440" y="37.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$c$</div></foreignObject>
</svg>

### Sähkömagneettinen spektri
Sähkömagneettisen säteilyn lajit eroavat toisistaan vain aallonpituudeltaan ja taajuudeltaan. Kun säteilyn lajit järjestetään aallonpituuden mukaan, saadaan **sähkömagneettinen spektri**. Alueiden rajat eivät ole jyrkkiä. Alueet nimetään sen mukaan, miten säteily syntyy ja miten se vaikuttaa aineeseen. Silmä näkee vain kapean kaistan. Punaisen valon aallonpituus on noin $750\,\text{nm}$ ja violetin noin $380\,\text{nm}$.

<svg data-fig="spectrum" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva sähkömagneettisesta spektristä. Vaakasuora palkki, jonka aallonpituusasteikko on logaritminen: jokainen asteikkoväli on tuhatkertainen aallonpituus. Vasemmalta oikealle ovat radioaallot (yli 1 m), mikroaallot (1 mm–1 m), infrapunasäteily (750 nm–1 mm), kapea näkyvän valon kaista, ultraviolettisäteily (10–380 nm), röntgensäteily (0,01–10 nm) ja gammasäteily (alle noin 0,01 nm). Näkyvän valon kaista on suurennettu palkin alle: punainen on noin 750 nm:n kohdalla vasemmalla ja violetti noin 380 nm:n kohdalla oikealla." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy79-band" gradientUnits="userSpaceOnUse" x1="336.5" y1="0" x2="346" y2="0"><stop offset="0" stop-color="#c81e1e"/><stop offset="0.25" stop-color="#f08a1a"/><stop offset="0.4" stop-color="#e6e01a"/><stop offset="0.55" stop-color="#2fbf3f"/><stop offset="0.7" stop-color="#1aa0e6"/><stop offset="0.88" stop-color="#3b3bf0"/><stop offset="1" stop-color="#7a1fd1"/></linearGradient><linearGradient id="fy79-vis" gradientUnits="userSpaceOnUse" x1="150" y1="0" x2="530" y2="0"><stop offset="0" stop-color="#c81e1e"/><stop offset="0.25" stop-color="#f08a1a"/><stop offset="0.4" stop-color="#e6e01a"/><stop offset="0.55" stop-color="#2fbf3f"/><stop offset="0.7" stop-color="#1aa0e6"/><stop offset="0.88" stop-color="#3b3bf0"/><stop offset="1" stop-color="#7a1fd1"/></linearGradient></defs>
  <rect x="40" y="136" width="97.5" height="30" fill="#b2f2bb"/>
  <rect x="137.5" y="136" width="97.5" height="30" fill="#f1dfb5"/>
  <rect x="235" y="136" width="101.5" height="30" fill="#f2a69c"/>
  <rect x="346" y="136" width="51.5" height="30" fill="#d0e6fb"/>
  <rect x="397.5" y="136" width="97.5" height="30" fill="#c4ccd4"/>
  <rect x="495" y="136" width="65" height="30" fill="#8a96a3"/>
  <rect x="336.5" y="136" width="9.5" height="30" fill="url(#fy79-band)"/>
  <rect x="40" y="136" width="520" height="30" rx="3" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="137.5" y1="136" x2="137.5" y2="166" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="235" y1="136" x2="235" y2="166" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336.5" y1="136" x2="336.5" y2="166" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="397.5" y1="136" x2="397.5" y2="166" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="495" y1="136" x2="495" y2="166" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="78" x2="89" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="19.5" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{radioaallot}$</div></foreignObject>
  <line x1="286" y1="78" x2="286" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="226" y="47.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{infrapuna}$</div></foreignObject>
  <line x1="372" y1="78" x2="372" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="355.5" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{UV}$</div></foreignObject>
  <line x1="527.5" y1="78" x2="527.5" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="485" y="47.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gamma}$</div></foreignObject>
  <foreignObject x="114" y="97.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mikroaallot}$</div></foreignObject>
  <foreignObject x="399" y="97.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{röntgen}$</div></foreignObject>
  <line x1="40" y1="166" x2="40" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17.5" y="177.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{3}$</div></foreignObject>
  <line x1="137.5" y1="166" x2="137.5" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="127.5" y="177.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="235" y1="166" x2="235" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="206" y="177.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{-3}$</div></foreignObject>
  <line x1="332.5" y1="166" x2="332.5" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="303.5" y="177.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{-6}$</div></foreignObject>
  <line x1="430" y1="166" x2="430" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="401" y="177.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{-9}$</div></foreignObject>
  <line x1="527.5" y1="166" x2="527.5" y2="174" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="492.5" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{-12}$</div></foreignObject>
  <foreignObject x="498" y="211.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\lambda\ (\text{m})$</div></foreignObject>
  <path d="M336.5,166 L150,262 M346,166 L530,262" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-dasharray="5 4"/>
  <rect x="150" y="262" width="380" height="30" rx="3" fill="url(#fy79-vis)" stroke="#1f2933" stroke-width="2"/>
  <line x1="201.5" y1="292" x2="201.5" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="160" y="303.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700\,\text{nm}$</div></foreignObject>
  <line x1="304" y1="292" x2="304" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="262.5" y="303.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600\,\text{nm}$</div></foreignObject>
  <line x1="407" y1="292" x2="407" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="365.5" y="303.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500\,\text{nm}$</div></foreignObject>
  <line x1="509.5" y1="292" x2="509.5" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="468" y="303.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400\,\text{nm}$</div></foreignObject>
  <foreignObject x="273.5" y="337.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{näkyvä valo}$</div></foreignObject>
</svg>

| Alue | Aallonpituus | Lähteitä ja käyttöä |
|---|---|---|
| radioaallot | yli $1\,\text{m}$ | antenni; radio, televisio |
| mikroaallot | $1\,\text{mm}$–$1\,\text{m}$ | antenni; matkapuhelin, tutka, uuni |
| infrapuna | $750\,\text{nm}$–$1\,\text{mm}$ | kaikki kappaleet; lämpökamera |
| näkyvä valo | $380$–$750\,\text{nm}$ | Aurinko, hehkuva kappale; näkeminen |
| ultravioletti | $10$–$380\,\text{nm}$ | Aurinko; D‑vitamiini, palovamma |
| röntgen | $0{,}01$–$10\,\text{nm}$ | röntgenputki; röntgenkuvaus |
| gamma | alle $0{,}01\,\text{nm}$ | atomiytimet; sädehoito, sterilointi |

### Säteilyn vaikutukset
Säteilyn vaikutus riippuu sen aallonpituudesta. Radioaallot, mikroaallot ja infrapunasäteily lisäävät aineen sisäenergiaa. Mikroaaltouunin säteily saa ruoan vesimolekyylit kääntyilemään edestakaisin, ja infrapuna lämmittää ihoa. Röntgensäteily, gammasäteily ja lyhytaaltoisin ultraviolettisäteily ovat **ionisoivaa säteilyä**. Ne voivat irrottaa elektroneja atomeista ja vaurioittaa soluja. Myös röntgenputki on kiihtyvän varauksen lähde. Siinä nopeat elektronit pysähtyvät metalliin, ja niiden jyrkkä hidastuminen synnyttää röntgensäteilyä. Röntgensäteily läpäisee pehmytkudoksen paremmin kuin luun, joten luut näkyvät kuvassa.

<figure class="unit-photo"><img src="pics/fy7/basalt-lava-flow.webp" alt="Harmaa laavakenttä. Keskellä on pieni kohta, jossa laava hehkuu punaisena."><figcaption>Laavaa, joka jähmettyy. Jäähtynyt pinta on harmaa, koska se säteilee lähes vain infrapunaa. Kuoren alla laava on niin kuumaa, että se hehkuu punaisena.</figcaption></figure>

### Kaikki kappaleet säteilevät
Aineen hiukkaset ovat jatkuvassa lämpöliikkeessä, ja niiden varaukset ovat kiihtyvässä liikkeessä. Siksi jokainen kappale lähettää sähkömagneettista säteilyä. Sitä kutsutaan lämpösäteilyksi (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*). Säteilyssä on mukana kaikkia aallonpituuksia, eli sen spektri on jatkuva. Huoneenlämpöinen kappale säteilee lähes pelkästään infrapunaa, jota silmä ei näe. Kun kappaletta kuumennetaan, säteily voimistuu ja sen pääosa siirtyy lyhyemmille aallonpituuksille. Noin $800\,\text{K}$:n lämpötilassa säteilyssä on jo niin paljon punaista valoa, että kappale hehkuu pimeässä tummanpunaisena. Kuumempana se hehkuu oranssina, keltaisena ja lopulta valkoisena.

<figure class="unit-photo"><img src="pics/fy7/sparkler.webp" alt="Tähtisadetikku pimeässä. Siitä lentää valkoisia kipinöitä joka suuntaan."><figcaption>Tähtisadetikun kipinät ovat hehkuvia metallihippuja. Ne ovat paljon kuumempia kuin punainen laava. Siksi ne säteilevät enemmän lyhyitä aallonpituuksia ja näyttävät melkein valkoisilta.</figcaption></figure>

### Musta kappale
**Musta kappale** on ihannekappale, joka imee kaiken siihen osuvan säteilyn eikä heijasta mitään. Sen lähettämän säteilyn spektri riippuu vain sen pintalämpötilasta. Aine, josta kappale on tehty, ei vaikuta siihen. Tätä säteilyä kutsutaan **mustan kappaleen säteilyksi**. Kuuma musta kappale ei näytä mustalta, sillä se säteilee itse. Aurinko säteilee likimain kuin musta kappale. Samoin säteilevät hehkuva hiillos ja infrapuna-alueella ihmisen iho. Kiiltävä metalli heijastaa suuren osan siihen osuvasta säteilystä. Samassa lämpötilassa se myös säteilee heikommin kuin musta kappale.

## Kaava: Wienin siirtymälaki
Mustan kappaleen spektrin huippu on se aallonpituus, jolla kappale säteilee voimakkaimmin. Mitä kuumempi kappale on, sitä lyhyempi huipun aallonpituus on. Huipun aallonpituus on kääntäen verrannollinen kappaleen absoluuttiseen lämpötilaan:
```latex
\lambda_\text{max} T = b
```
missä $\lambda_\text{max}$ on spektrin huipun aallonpituus (m), $T$ on kappaleen pintalämpötila (K) ja $b = 2{,}898 \cdot 10^{-3}\,\text{m} \cdot \text{K}$ on Wienin siirtymälain vakio. Lämpötilan on oltava absoluuttinen lämpötila. Jos lämpötila on annettu celsiusasteina, muuta se ensin kelvineiksi lisäämällä siihen $273{,}15\,\text{K}$. Kun absoluuttinen lämpötila kaksinkertaistuu, huipun aallonpituus puolittuu. Laki koskee mustaa kappaletta. Todellisille kappaleille, kuten Auringolle ja hiillokselle, se pätee likimain.

<svg data-fig="curves" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: mustan kappaleen säteilyn spektri kolmessa lämpötilassa. Vaaka-akselilla on aallonpituus nanometreinä nollasta 2000:een. Pystyakselilla on säteilyteho pinta-alaa ja aallonpituusväliä kohti megawatteina neliömetriä ja mikrometriä kohti. Näkyvän valon alue 380–750 nm on taustalla värikaistana. Musta yhtenäinen käyrä on 6000 K, oranssi katkoviiva 5000 K ja punainen pisteviiva 4000 K. Huiput ovat aallonpituuksilla 483 nm, 580 nm ja 724 nm. Niiden korkeudet ovat noin 100, 40 ja 13. Mitä kuumempi kappale on, sitä korkeampi käyrä on ja sitä lyhyemmällä aallonpituudella huippu on." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy79-cband" gradientUnits="userSpaceOnUse" x1="239.5" y1="0" x2="170.5" y2="0"><stop offset="0" stop-color="#c81e1e"/><stop offset="0.25" stop-color="#f08a1a"/><stop offset="0.4" stop-color="#e6e01a"/><stop offset="0.55" stop-color="#2fbf3f"/><stop offset="0.7" stop-color="#1aa0e6"/><stop offset="0.88" stop-color="#3b3bf0"/><stop offset="1" stop-color="#7a1fd1"/></linearGradient></defs>
  <line x1="146.5" y1="290" x2="146.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="193" y1="290" x2="193" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="239.5" y1="290" x2="239.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="286" y1="290" x2="286" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332.5" y1="290" x2="332.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="379" y1="290" x2="379" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="425.5" y1="290" x2="425.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="290" x2="472" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="248.5" x2="472" y2="248.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="207" x2="472" y2="207" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="165.5" x2="472" y2="165.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="124" x2="472" y2="124" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="82.5" x2="472" y2="82.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="290" x2="486" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M498,290 L485,296 L485,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="291" x2="100" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,36 L106,49 L94,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="146.5" y1="290" x2="146.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="193" y1="290" x2="193" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="170.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="239.5" y1="290" x2="239.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="290" x2="286" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="257" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1000$</div></foreignObject>
  <line x1="332.5" y1="290" x2="332.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="379" y1="290" x2="379" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="350" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1500$</div></foreignObject>
  <line x1="425.5" y1="290" x2="425.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="472" y1="290" x2="472" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="443" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2000$</div></foreignObject>
  <line x1="93" y1="248.5" x2="100" y2="248.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="234" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="93" y1="207" x2="100" y2="207" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="192.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="93" y1="165.5" x2="100" y2="165.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="151" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="93" y1="124" x2="100" y2="124" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="93" y1="82.5" x2="100" y2="82.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="68" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="70" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="504" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="90" y="5.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M_\lambda\ (\text{MW}/(\text{m}^2 \cdot \mu\text{m}))$</div></foreignObject>
  <rect x="170.5" y="62" width="69" height="228" fill="url(#fy79-cband)" fill-opacity="0.2"/>
  <rect x="170.5" y="280" width="69" height="9" fill="url(#fy79-cband)"/>
  <polyline points="128,289 129.5,288 131.5,286 133,284 135,281 136.5,277 138,272 140,266 141.5,259 143.5,251.5 145,243 147,234 148.5,224.5 150.5,214.5 152,204.5 153.5,194.5 155.5,184.5 157,174.5 159,165 160.5,155.5 162.5,147 164,138.5 166,130.5 167.5,123.5 169,117 171,111 172.5,105.5 174.5,101 176,97 178,93.5 179.5,90.5 181,88 183,86 184.5,84.5 186.5,83.5 188,83 190,82.5 191.5,83 193.5,83.5 195,84 196.5,85.5 198.5,86.5 200,88 202,90 203.5,92 205.5,94 207,96.5 209,99 210.5,101.5 212,104 214,107 215.5,110 217.5,112.5 219,115.5 221,118.5 222.5,121.5 224,124.5 226,127.5 227.5,130.5 229.5,133.5 231,136.5 233,139.5 234.5,142.5 236.5,145.5 238,148 239.5,151 241.5,154 243,157 245,159.5 246.5,162.5 248.5,165 250,167.5 252,170 253.5,172.5 255,175 257,177.5 258.5,180 260.5,182.5 262,185 264,187 265.5,189.5 267.5,191.5 269,193.5 270.5,195.5 272.5,198 274,200 276,202 277.5,203.5 279.5,205.5 281,207.5 282.5,209 284.5,211 286,212.5 288,214.5 289.5,216 291.5,217.5 293,219 295,220.5 296.5,222 298,223.5 300,225 301.5,226.5 303.5,227.5 305,229 307,230.5 308.5,231.5 310.5,233 312,234 313.5,235 315.5,236.5 317,237.5 319,238.5 320.5,239.5 322.5,240.5 324,241.5 326,242.5 327.5,243.5 329,244.5 331,245.5 332.5,246.5 334.5,247 336,248 338,249 339.5,249.5 341,250.5 343,251.5 344.5,252 346.5,253 348,253.5 350,254 351.5,255 353.5,255.5 355,256.5 356.5,257 358.5,257.5 360,258 362,259 363.5,259.5 365.5,260 367,260.5 369,261 370.5,261.5 372,262 374,262.5 375.5,263 377.5,263.5 379,264 381,264.5 382.5,265 384.5,265.5 386,266 387.5,266.5 389.5,267 391,267 393,267.5 394.5,268 396.5,268.5 398,269 399.5,269 401.5,269.5 403,270 405,270.5 406.5,270.5 408.5,271 410,271.5 412,271.5 413.5,272 415,272 417,272.5 418.5,273 420.5,273 422,273.5 424,273.5 425.5,274 427.5,274 429,274.5 430.5,274.5 432.5,275 434,275 436,275.5 437.5,275.5 439.5,276 441,276 443,276.5 444.5,276.5 446,277 448,277 449.5,277 451.5,277.5 453,277.5 455,278 456.5,278 458,278 460,278.5 461.5,278.5 463.5,278.5 465,279 467,279 468.5,279 470.5,279.5 472,279.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="128,290 129.5,290 131.5,290 133,289.5 135,289.5 136.5,289 138,288 140,287.5 141.5,286.5 143.5,285 145,283.5 147,281.5 148.5,279.5 150.5,277 152,274.5 153.5,272 155.5,269 157,265.5 159,262.5 160.5,259 162.5,256 164,252.5 166,249 167.5,245.5 169,242.5 171,239 172.5,236 174.5,233 176,230.5 178,227.5 179.5,225 181,223 183,220.5 184.5,218.5 186.5,216.5 188,215 190,213.5 191.5,212 193.5,211 195,210 196.5,209 198.5,208.5 200,208 202,207.5 203.5,207 205.5,207 207,206.5 209,206.5 210.5,207 212,207 214,207.5 215.5,207.5 217.5,208 219,208.5 221,209 222.5,209.5 224,210.5 226,211 227.5,212 229.5,212.5 231,213.5 233,214.5 234.5,215.5 236.5,216 238,217 239.5,218 241.5,219 243,220 245,221 246.5,222 248.5,223 250,224 252,225 253.5,226 255,227 257,228 258.5,229 260.5,230 262,231 264,232 265.5,233 267.5,234 269,235 270.5,236 272.5,237 274,237.5 276,238.5 277.5,239.5 279.5,240.5 281,241.5 282.5,242 284.5,243 286,244 288,244.5 289.5,245.5 291.5,246.5 293,247 295,248 296.5,248.5 298,249.5 300,250 301.5,251 303.5,251.5 305,252 307,253 308.5,253.5 310.5,254 312,255 313.5,255.5 315.5,256 317,257 319,257.5 320.5,258 322.5,258.5 324,259 326,259.5 327.5,260 329,260.5 331,261.5 332.5,262 334.5,262.5 336,263 338,263.5 339.5,263.5 341,264 343,264.5 344.5,265 346.5,265.5 348,266 350,266.5 351.5,267 353.5,267 355,267.5 356.5,268 358.5,268.5 360,269 362,269 363.5,269.5 365.5,270 367,270 369,270.5 370.5,271 372,271 374,271.5 375.5,272 377.5,272 379,272.5 381,272.5 382.5,273 384.5,273.5 386,273.5 387.5,274 389.5,274 391,274.5 393,274.5 394.5,275 396.5,275 398,275.5 399.5,275.5 401.5,276 403,276 405,276.5 406.5,276.5 408.5,276.5 410,277 412,277 413.5,277.5 415,277.5 417,278 418.5,278 420.5,278 422,278.5 424,278.5 425.5,278.5 427.5,279 429,279 430.5,279 432.5,279.5 434,279.5 436,279.5 437.5,280 439.5,280 441,280 443,280.5 444.5,280.5 446,280.5 448,280.5 449.5,281 451.5,281 453,281 455,281.5 456.5,281.5 458,281.5 460,281.5 461.5,282 463.5,282 465,282 467,282 468.5,282 470.5,282.5 472,282.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 6"/>
  <polyline points="128,290 129.5,290 131.5,290 133,290 135,290 136.5,290 138,290 140,290 141.5,290 143.5,290 145,289.5 147,289.5 148.5,289.5 150.5,289 152,289 153.5,288.5 155.5,288 157,287.5 159,287 160.5,286.5 162.5,286 164,285.5 166,284.5 167.5,284 169,283 171,282.5 172.5,281.5 174.5,280.5 176,279.5 178,279 179.5,278 181,277 183,276 184.5,275.5 186.5,274.5 188,273.5 190,273 191.5,272 193.5,271 195,270.5 196.5,270 198.5,269 200,268.5 202,268 203.5,267.5 205.5,266.5 207,266 209,266 210.5,265.5 212,265 214,264.5 215.5,264.5 217.5,264 219,263.5 221,263.5 222.5,263.5 224,263 226,263 227.5,263 229.5,263 231,262.5 233,262.5 234.5,262.5 236.5,262.5 238,262.5 239.5,263 241.5,263 243,263 245,263 246.5,263 248.5,263.5 250,263.5 252,263.5 253.5,263.5 255,264 257,264 258.5,264.5 260.5,264.5 262,264.5 264,265 265.5,265 267.5,265.5 269,265.5 270.5,266 272.5,266 274,266.5 276,266.5 277.5,267 279.5,267 281,267.5 282.5,267.5 284.5,268 286,268 288,268.5 289.5,268.5 291.5,269 293,269 295,269.5 296.5,270 298,270 300,270.5 301.5,270.5 303.5,271 305,271 307,271.5 308.5,271.5 310.5,272 312,272 313.5,272.5 315.5,272.5 317,273 319,273 320.5,273.5 322.5,273.5 324,273.5 326,274 327.5,274 329,274.5 331,274.5 332.5,275 334.5,275 336,275.5 338,275.5 339.5,275.5 341,276 343,276 344.5,276.5 346.5,276.5 348,276.5 350,277 351.5,277 353.5,277.5 355,277.5 356.5,277.5 358.5,278 360,278 362,278 363.5,278.5 365.5,278.5 367,278.5 369,279 370.5,279 372,279 374,279.5 375.5,279.5 377.5,279.5 379,280 381,280 382.5,280 384.5,280 386,280.5 387.5,280.5 389.5,280.5 391,281 393,281 394.5,281 396.5,281 398,281.5 399.5,281.5 401.5,281.5 403,281.5 405,282 406.5,282 408.5,282 410,282 412,282 413.5,282.5 415,282.5 417,282.5 418.5,282.5 420.5,283 422,283 424,283 425.5,283 427.5,283 429,283.5 430.5,283.5 432.5,283.5 434,283.5 436,283.5 437.5,283.5 439.5,284 441,284 443,284 444.5,284 446,284 448,284 449.5,284.5 451.5,284.5 453,284.5 455,284.5 456.5,284.5 458,284.5 460,284.5 461.5,285 463.5,285 465,285 467,285 468.5,285 470.5,285 472,285" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="3 5"/>
  <line x1="190" y1="82.5" x2="190" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="190" cy="82.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="208" y1="206.5" x2="208" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="208" cy="206.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="234.5" y1="262.5" x2="234.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="234.5" cy="262.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <line x1="330" y1="82.5" x2="382" y2="82.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="392" y="68" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$6000\,\text{K}$</div></foreignObject>
  <line x1="330" y1="114" x2="382" y2="114" stroke="#e8590c" stroke-width="3" stroke-linecap="butt" stroke-dasharray="10 6"/>
  <foreignObject x="392" y="99.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$5000\,\text{K}$</div></foreignObject>
  <line x1="330" y1="145" x2="382" y2="145" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt" stroke-dasharray="3 5"/>
  <foreignObject x="392" y="130.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$4000\,\text{K}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/submarine-lava.webp" alt="Tumma vedenalainen kuva. Kallion raoissa hehkuu oranssia laavaa."><figcaption>Laava hehkuu meren pohjassa. Laava on oranssia, vaikka vesi jäähdyttää sitä. Suurin osa sen säteilystä on silti infrapunaa. Silmä näkee vain pienen osan säteilystä.</figcaption></figure>

### Huippu kertoo lämpötilan
Huoneenlämpöisen kappaleen ($300\,\text{K}$) spektrin huippu on noin $9{,}7\,\mu\text{m}$:n kohdalla. Ihmisen ihon ($34\,{}^\circ\text{C}$ eli $307\,\text{K}$) huippu on noin $9{,}4\,\mu\text{m}$:n kohdalla. Molemmat ovat syvällä infrapuna-alueella. Lämpökamera mittaa säteilyä aallonpituuksilla noin $8$–$14\,\mu\text{m}$ ja muuttaa sen kuvaksi. Siksi se näkee ihmisen pimeässäkin. Ihminen ei tarvitse valoa näkyäkseen kameralle, koska hän itse säteilee. Tummanpunaisena hehkuvan, noin $800\,\text{K}$:n kappaleen huippu on vielä infrapuna-alueella, noin $3{,}6\,\mu\text{m}$:n kohdalla. Silmä näkee vain spektrin lyhytaaltoisen reunan. Auringon säteilyn huippu on noin $500\,\text{nm}$:n (tarkemmin $502\,\text{nm}$:n) kohdalla, näkyvän valon keskellä.

### Säteilyteho kasvaa jyrkästi
Kuumempi musta kappale säteilee jokaisella aallonpituudella enemmän kuin kylmempi. Siksi sen spektrikäyrä on kokonaan kylmemmän käyrän yläpuolella. Kappaleen pinta-alaa kohti säteilemä kokonaisteho on verrannollinen absoluuttisen lämpötilan neljänteen potenssiin (Stefanin–Boltzmannin laki). Kun lämpötila kaksinkertaistuu, jokainen neliömetri säteilee $16$-kertaisen tehon. Siksi hehkuva rauta lämmittää kasvoja jo metrien päästä. Miksi spektrikäyrä on juuri tämän muotoinen, sen selittää vasta kvanttifysiikka kurssilla *Aine, säteily ja kvantittuminen*.

## Esimerkki
Oletetaan, että Aurinko säteilee kuin musta kappale. Sen spektrin huippu on aallonpituudella $502\,\text{nm}$. Kuinka suuri on Auringon pintalämpötila?

<!-- vaihe -->

**Tunnetut ja kysytty.** Tunnetaan spektrin huipun aallonpituus $\lambda_\text{max} = 502\,\text{nm}$ ja Wienin siirtymälain vakio $b = 2{,}898 \cdot 10^{-3}\,\text{m} \cdot \text{K}$. Kysytään Auringon pintalämpötilaa $T$ kelvineinä.

<!-- vaihe -->

**Periaate.** Mustan kappaleen spektrin huipun aallonpituus riippuu vain pintalämpötilasta. Siksi huipun paikasta voi laskea lämpötilan Wienin siirtymälailla. Laki sopii, koska Auringon oletetaan säteilevän kuin musta kappale.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\lambda_\text{max} T = b \\
&T = \frac{b}{\lambda_\text{max}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Vakiossa $b$ on metrejä. Siksi aallonpituus muutetaan metreiksi: $\lambda_\text{max} = 502\,\text{nm} = 502 \cdot 10^{-9}\,\text{m}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
T &= \frac{b}{\lambda_\text{max}} \\
&= \frac{2{,}898 \cdot 10^{-3}\,\text{m} \cdot \text{K}}{502 \cdot 10^{-9}\,\text{m}} \\
&= 5773\,\text{K}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Auringon pintalämpötila on $T \approx 5{,}77 \cdot 10^{3}\,\text{K}$. Tulos ilmoitetaan kolmella merkitsevällä numerolla, koska aallonpituus $502\,\text{nm}$ on annettu kolmella.

<!-- vaihe -->

**Järkevyys.** Kansainvälinen tähtitieteellinen unioni IAU on vahvistanut Auringon pintalämpötilan nimellisarvoksi $5772\,\text{K}$ (IAU 2015). Tulos sopii siihen hyvin. Lämpötila on myös paljon korkeampi kuin tummanpunaisena hehkuvan raudan noin $800\,\text{K}$. Niin pitää olla, sillä Auringon huippu on näkyvän valon alueella eikä infrapunassa.

## Yleinen virhekäsitys
Moni ajattelee, että säteily tarkoittaa aina radioaktiivista tai vaarallista säteilyä. Myös radioaallot, valo ja lämpösäteily ovat sähkömagneettista säteilyä. Ionisoivaa on vain lyhytaaltoisin osa spektristä.

Toinen virhe on luulla, että kylmät kappaleet eivät säteile lainkaan. Jokainen kappale säteilee. Huoneenlämpöinen kappale säteilee infrapunaa, jota silmä ei näe.

Kolmas virhe on sijoittaa Wienin siirtymälakiin lämpötila celsiusasteina. Laki vaatii absoluuttisen lämpötilan: $900\,{}^\circ\text{C}$ on $1173\,\text{K}$, ja huippu on $2{,}47\,\mu\text{m}$:n eikä $3{,}22\,\mu\text{m}$:n kohdalla.

Neljäs virhe on päätellä, että Aurinko on vihreä, koska sen huippu on vihreän valon kohdalla. Spektri on leveä, ja kaikkien värien yhdistelmä näyttää silmään valkoiselta.

## Tiivistelmä
- Sähkömagneettisessa aallossa muuttuvat sähkö- ja magneettikenttä synnyttävät toisensa. Kentät ovat kohtisuorassa toisiaan vastaan ja etenemissuuntaa vastaan. Aalto etenee tyhjiössä nopeudella $c = 3{,}00 \cdot 10^{8}\,\text{m/s}$.
- Valon nopeus, taajuus ja aallonpituus liittyvät toisiinsa: $c = f\lambda$. Spektrin alueet radioaalloista gammasäteilyyn eroavat vain aallonpituudeltaan ja taajuudeltaan.
- Säteilyä syntyy, kun varattu hiukkanen on kiihtyvässä liikkeessä, kuten antennin elektronit tai kuuman kappaleen lämpöliikkeessä olevat hiukkaset.
- Mustan kappaleen säteilyn spektri on jatkuva ja riippuu vain pintalämpötilasta. Wienin siirtymälain $\lambda_\text{max} T = b$ mukaan kuumemman kappaleen huippu on lyhyemmällä aallonpituudella. Lämpötila sijoitetaan kelvineinä.
