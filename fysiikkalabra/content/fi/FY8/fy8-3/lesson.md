# Vetyatomin energiatasot ja Bohrin malli

> **Miksi** vetyä sisältävän lampun valo hajoaa hilassa vain neljäksi selvästi näkyväksi värilliseksi viivaksi, ja miksi juuri aallonpituuksille $656\,\text{nm}$, $486\,\text{nm}$, $434\,\text{nm}$ ja $410\,\text{nm}$?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pimennetyssä luokassa pöydällä on vetyä sisältävä purkausputki jännitelähteen telineessä. Putki hehkuu vaaleanpunaisen violettina. Sen edessä on telineessä hila, ja hilan takana valkoisella varjostimella näkyy tummaa taustaa vasten neljä erillistä värillistä viivaa: punainen, syaani, sininen ja violetti." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy83h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b7480"/><stop offset="1" stop-color="#1f2933"/></linearGradient><linearGradient id="fy83h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><radialGradient id="fy83h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#f2a69c" stop-opacity="0.9"/><stop offset="1" stop-color="#f2a69c" stop-opacity="0"/></radialGradient><linearGradient id="fy83h-tube" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f2a69c"/><stop offset="0.5" stop-color="#ffffff"/><stop offset="1" stop-color="#b197fc"/></linearGradient><linearGradient id="fy83h-beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f2a69c" stop-opacity="0.55"/><stop offset="1" stop-color="#f2a69c" stop-opacity="0.08"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy83h-wall)"/>
  <rect x="0" y="430" width="1200" height="170" fill="url(#fy83h-desk)"/>
  <rect x="0" y="430" width="1200" height="10" fill="#f1dfb5"/>
  <ellipse cx="300" cy="250" rx="170" ry="210" fill="url(#fy83h-glow)"/>
  <rect x="230" y="400" width="140" height="34" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="250" y="380" width="100" height="24" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="282" y="70" width="36" height="34" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="282" y="346" width="36" height="34" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="240" y="70" width="10" height="330" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="250" y="82" width="32" height="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="250" y="358" width="32" height="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="290" y="104" width="20" height="242" rx="10" fill="url(#fy83h-tube)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="296" y="112" width="4" height="226" fill="#ffffff" fill-opacity="0.7"/>
  <path d="M318,200 L640,170 L640,290 L318,250 Z" fill="url(#fy83h-beam)" stroke-linejoin="round"/>
  <rect x="636" y="150" width="16" height="160" rx="3" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <line x1="640" y1="160" x2="648" y2="160" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="168" x2="648" y2="168" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="176" x2="648" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="184" x2="648" y2="184" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="192" x2="648" y2="192" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="200" x2="648" y2="200" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="208" x2="648" y2="208" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="216" x2="648" y2="216" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="224" x2="648" y2="224" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="232" x2="648" y2="232" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="240" x2="648" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="248" x2="648" y2="248" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="256" x2="648" y2="256" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="264" x2="648" y2="264" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="272" x2="648" y2="272" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="280" x2="648" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="288" x2="648" y2="288" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="296" x2="648" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="640" y="310" width="8" height="120" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="612" y="426" width="64" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M652,226 L756,120 L764,120 Z" fill="#c92a2a" stroke-linejoin="round" fill-opacity="0.35"/>
  <path d="M652,226 L896,120 L904,120 Z" fill="#1098ad" stroke-linejoin="round" fill-opacity="0.35"/>
  <path d="M652,226 L944,120 L952,120 Z" fill="#4263eb" stroke-linejoin="round" fill-opacity="0.35"/>
  <path d="M652,226 L970,120 L978,120 Z" fill="#7048e8" stroke-linejoin="round" fill-opacity="0.35"/>
  <rect x="720" y="60" width="340" height="360" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="740" y="100" width="300" height="70" rx="3" fill="#1f2933"/>
  <rect x="755" y="104" width="10" height="62" fill="#c92a2a"/>
  <rect x="895" y="104" width="10" height="62" fill="#1098ad"/>
  <rect x="943" y="104" width="10" height="62" fill="#4263eb"/>
  <rect x="969" y="104" width="10" height="62" fill="#7048e8"/>
  <rect x="880" y="420" width="20" height="14" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="840" y="430" width="100" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M120,520 L300,498 L330,560 L140,586 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="137" y1="540" x2="314.5" y2="516.5" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="144" y1="553" x2="320.5" y2="529" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="151" y1="566" x2="326" y2="541.5" stroke="#d0e6fb" stroke-width="2" stroke-linecap="butt"/>
  <path d="M380,560 L520,520 L526,532 L386,572 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
</svg>

## Ydinajatus

### Vetyatomin energia on kvantittunut
Vetyatomissa on yksi protoni ja yksi elektroni. Atomin energia eli elektronin liike-energian ja sähköisen potentiaalienergian summa voi saada vain tiettyjä arvoja, **energiatasoja**. Tasot numeroidaan kokonaisluvulla $n = 1, 2, 3, \ldots$ Energian nollakohdaksi valitaan tilanne, jossa elektroni on levossa kaukana protonista eli irti atomista. Sidotun elektronin energia on siksi negatiivinen: elektronin irrottaminen vaatii energiaa.

Alin taso $n = 1$ on **perustila**, jonka energia on $-13{,}6\,\text{eV}$. Ylemmät tasot $n = 2, 3, \ldots$ ovat **viritystiloja**. Ne tihenevät ylöspäin ja lähestyvät nollaa. Energia, joka tarvitaan elektronin irrottamiseen perustilasta, on vedyn **ionisaatioenergia** $13{,}6\,\text{eV}$. Viritystilassa atomi pysyy tavallisesti vain noin $10^{-8}\,\text{s}$ ja palaa sitten alemmalle tasolle.

<svg data-fig="levels" viewBox="0 0 600 400" role="img" aria-label="Vetyatomin energiatasokaavio. Pystysuunnassa energia; tasot n = 2, 3, 4, 5 ja 6 sekä energia nolla ylimpänä ovat mittakaavassa, mutta tasojen n = 1 ja n = 2 väliä on lyhennetty, mikä on merkitty katkoviivalla. Tasojen energiat: n = 1: −13,6 eV, n = 2: −3,40 eV, n = 3: −1,51 eV, n = 4: −0,85 eV, ylimpänä 0 eV, jossa elektroni on irti atomista. Tasot tihenevät ylöspäin. Kaksi mustaa nuolta kuvaa siirtymiä tasoille n = 1 (Lymanin sarja, ultraviolettia), neljä värillistä nuolta siirtymiä tasoilta 3, 4, 5 ja 6 tasolle n = 2 (Balmerin sarja, näkyvää valoa: punainen, syaani, sininen ja violetti)." style="max-width:100%;font-size:24px">
  <line x1="26" y1="384" x2="26" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M26,34 L32,47 L20,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="36" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <path d="M18,350 L34,344 M18,360 L34,354" fill="none" stroke="#ffffff" stroke-width="6" stroke-linejoin="round"/>
  <path d="M18,350 L34,344 M18,360 L34,354" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="150" y1="70" x2="430" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 5"/>
  <line x1="150" y1="301" x2="430" y2="301" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="173" x2="430" y2="173" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="128" x2="430" y2="128" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="107" x2="430" y2="107" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="95.5" x2="430" y2="95.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="150" y1="366" x2="430" y2="366" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="95" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n \to \infty$</div></foreignObject>
  <foreignObject x="70" y="82.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 5, 6$</div></foreignObject>
  <foreignObject x="95" y="116.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 4$</div></foreignObject>
  <foreignObject x="95" y="158.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 3$</div></foreignObject>
  <foreignObject x="95" y="286.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 2$</div></foreignObject>
  <foreignObject x="95" y="351.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n = 1$</div></foreignObject>
  <foreignObject x="440" y="55.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="116.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-0{,}85\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="158.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-1{,}51\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="286.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-3{,}40\,\text{eV}$</div></foreignObject>
  <foreignObject x="440" y="351.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-13{,}6\,\text{eV}$</div></foreignObject>
  <line x1="176" y1="301" x2="176" y2="352" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M176,365 L169.5,351 L182.5,351 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="206" y1="173" x2="206" y2="352" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M206,365 L199.5,351 L212.5,351 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="216" y="318.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Lyman (UV)}$</div></foreignObject>
  <line x1="262" y1="173" x2="262" y2="286" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M262,300 L255,285 L269,285 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="302" y1="128" x2="302" y2="286" stroke="#1098ad" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M302,300 L295,285 L309,285 Z" fill="#1098ad" stroke-linejoin="round"/>
  <line x1="342" y1="107" x2="342" y2="286" stroke="#4263eb" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M342,300 L335,285 L349,285 Z" fill="#4263eb" stroke-linejoin="round"/>
  <line x1="382" y1="95.5" x2="382" y2="286" stroke="#7048e8" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M382,300 L375,285 L389,285 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="392" y="223.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Balmer (näkyvä)}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/hydrogen-discharge-tube.webp" alt="Pitkä lasiputki mustalla pohjalla. Putken kapea keskiosa hehkuu vaaleanpunaisena ja päät sinertävinä."><figcaption>Vetyä sisältävä kaasupurkausputki. Sähkövirta virittää vetyatomeja, ja kun ne siirtyvät alemmille energiatasoille, syntyy vedyn spektriviivojen valo.</figcaption></figure>

### Siirtymässä syntyy tai katoaa fotoni
Kun elektroni siirtyy ylemmältä tasolta alemmalle, atomin energia pienenee ja erotus lähtee yhtenä fotonina. Energia säilyy, joten fotonin energia on tasojen erotus. Koska tasoja on vain tiettyjä, myös erotuksia on vain tiettyjä: vety lähettää vain tiettyjä aallonpituuksia, ja sen spektri on viivaspektri.

Siirtymät samalle alemmalle tasolle muodostavat sarjan. Tasolle $n = 1$ päättyvät siirtymät (Lymanin sarja) ovat suuria energiaharppauksia, ja niiden fotonit ovat ultraviolettia. Tasolle $n = 2$ päättyvät siirtymät (Balmerin sarja) tuottavat vedyn neljä kirkasta näkyvää viivaa; seuraavat viivat ($397\,\text{nm}$, $389\,\text{nm}$, …) ovat himmeitä ja näkyvän valon violetilla reunalla, jossa silmä on epäherkkä. Tasolle $n = 3$ päättyvät (Paschenin sarja) ovat infrapunaa.

Absorptio on käänteinen tapahtuma. Atomi absorboi fotonin vain, jos fotonin energia on täsmälleen jonkin tasoparin erotus: elektroni siirtyy silloin ylemmälle tasolle. Muun energian fotoni menee atomin ohi absorboitumatta. Poikkeus on ionisaatio: fotoni, jonka energia on vähintään ionisaatioenergia, voi irrottaa elektronin, ja ylimääräinen energia jää vapaan elektronin liike-energiaksi.

<svg data-fig="absorption" viewBox="0 0 600 400" role="img" aria-label="Kolme tilannetta vierekkäin, energia-asteikko mittakaavassa. Kussakin on vetyatomin tasot n = 1, 2 ja 3 sekä katkoviivana energia nolla, ja elektroni on aluksi perustilassa n = 1. Vasemmalla tulee fotoni, jonka energia on 10,2 eV, täsmälleen tasojen 1 ja 2 erotus: fotoni absorboituu ja elektroni siirtyy tasolle 2. Keskellä fotonin energia on 11,0 eV, joka ei ole minkään tasoparin erotus: fotoni menee läpi, ja elektroni jää tasolle 1. Oikealla fotonin energia on 14,0 eV, enemmän kuin ionisaatioenergia 13,6 eV: elektroni irtoaa atomista." style="max-width:100%;font-size:24px">
  <line x1="200" y1="14" x2="200" y2="386" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="400" y1="14" x2="400" y2="386" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="60" y1="60" x2="182" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <line x1="60" y1="277.5" x2="182" y2="277.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="60" y1="114.5" x2="182" y2="114.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="60" y1="84" x2="182" y2="84" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="32" y="263" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="32" y="100" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="32" y="69.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="32" y="39.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <path d="M14,304 L14.5,304 L15.5,304.5 L16.5,305 L17,305.5 L18,306.5 L19,307.5 L19.5,308.5 L20.5,309.5 L21.5,310 L22,310 L23,309.5 L23.5,309.5 L24,309 L24.5,308 L25.5,307.5 L26,306.5 L26.5,305.5 L27,304.5 L27.5,303 L28,302 L28.5,301 L29.5,299.5 L30,298.5 L30.5,297.5 L31,296.5 L31.5,295.5 L32.5,295 L33,294.5 L33.5,294 L34.5,294 L35,294 L36,294 L36.5,294.5 L37.5,295 L38,295.5 L39,296 L40,297 L40.5,298 L41.5,299 L42.5,300 L43.5,301 L44,302 L45,303 L46,303.5 L46.5,304.5 L47.5,305 L48,305.5 L49,305.5 L50,306 L50.5,306 L51,305.5 L52,305.5 L52.5,305 L53,304 L53.5,303.5 L54.5,302.5 L55,301.5 L55.5,300 L56,299 L56.5,298 L57,296.5 L57.5,295.5 L58.5,294.5 L59,293.5 L59.5,292.5 L60,291.5 L60.5,291 L61.5,290.5 L62,290 L62.5,290 L63.5,290 L64,290 L65,290.5 L65.5,291 L66.5,291.5 L67.5,292 L68,293 L69,294 L70,295 L71,296 L71.5,297 L72.5,298 L73.5,298.5 L74,299.5 L75,300 L76,301 L76.5,301.5 L77.5,301.5 L78,301.5 L79,301.5 L79.5,301.5 L80,301 L81,300.5 L81.5,300 L82,299 L82.5,298.5 L83.5,297 L84,296 L84.5,295 L85,294 L85.5,292.5 L86,291.5 L86.5,290.5 L87,289.5 L88,288.5 L88.5,287.5 L89,287 L89.5,286.5 L90.5,286 L91,286 L92,286 L92.5,286.5 L93.5,287.5 L94.5,288.5 L95,289.5 L96,290 L97,291 L97.5,291.5 L98.5,291.5 L99,291.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M114,289.5 L100,299 L98,284.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="132" cy="277.5" r="8" fill="#ffffff" stroke="#1971c2" stroke-width="2"/>
  <line x1="132" y1="266.5" x2="132" y2="136.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M132,125.5 L137.5,137.5 L126.5,137.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="132" cy="114.5" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="33.5" y="321.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = 10{,}2\,\text{eV}$</div></foreignObject>
  <foreignObject x="27.5" y="357.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{absorboituu}$</div></foreignObject>
  <line x1="260" y1="60" x2="382" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <line x1="260" y1="277.5" x2="382" y2="277.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="260" y1="114.5" x2="382" y2="114.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="260" y1="84" x2="382" y2="84" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M214,304 L215.5,304.5 L216.5,306 L218,308 L219.5,310 L220.5,311 L222,310.5 L223.5,309.5 L224.5,308 L226,306 L227,304 L228.5,302 L230,300 L231,298.5 L232.5,297.5 L234,297 L235,297.5 L236.5,298.5 L238,300 L239,302 L240.5,304 L242,306 L243,308 L244.5,309.5 L246,310.5 L247,311 L248.5,310.5 L250,309.5 L251,308 L252.5,306 L254,304 L255,302 L256.5,300 L257.5,298.5 L259,297.5 L260.5,297 L261.5,297.5 L263,298.5 L264.5,300 L265.5,302 L267,304 L268.5,306 L269.5,308 L271,309.5 L272.5,310.5 L273.5,311 L275,310.5 L276.5,309.5 L277.5,308 L279,306 L280,304 L281.5,302 L283,300 L284,298.5 L285.5,297.5 L287,297 L288,297.5 L289.5,298.5 L291,300 L292,302 L293.5,304 L295,306 L296,308 L297.5,309.5 L299,310.5 L300,311 L301.5,310.5 L303,309.5 L304,308 L305.5,306 L307,304 L308,302 L309.5,300 L310.5,298.5 L312,297.5 L313.5,297 L314.5,297.5 L316,298.5 L317.5,300 L318.5,302 L320,304 L321.5,306 L322.5,308 L324,309.5 L325.5,310.5 L326.5,311 L328,310.5 L329.5,309.5 L330.5,308 L332,306 L333,304 L334.5,302 L336,300 L337,298.5 L338.5,297.5 L340,297 L341,297.5 L342.5,298.5 L344,300 L345,302 L346.5,304 L348,306 L349,308 L350.5,309.5 L352,310.5 L353,311 L354.5,310.5 L356,309.5 L357,308 L358.5,306 L360,304 L361,302 L362.5,300 L363.5,298.5 L365,297.5 L366.5,297 L367.5,298 L369,300 L370.5,302 L371.5,303.5 L373,304" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M388,304 L373,311.5 L373,296.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="332" cy="277.5" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="233.5" y="321.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = 11{,}0\,\text{eV}$</div></foreignObject>
  <foreignObject x="240" y="357.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{menee läpi}$</div></foreignObject>
  <line x1="460" y1="60" x2="582" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <line x1="460" y1="277.5" x2="582" y2="277.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="460" y1="114.5" x2="582" y2="114.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="460" y1="84" x2="582" y2="84" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M414,304 L414.5,304 L415.5,304.5 L416.5,305 L417,305.5 L418,306.5 L419,307.5 L419.5,308.5 L420.5,309.5 L421.5,310 L422,310 L423,309.5 L423.5,309.5 L424,309 L424.5,308 L425.5,307.5 L426,306.5 L426.5,305.5 L427,304.5 L427.5,303 L428,302 L428.5,301 L429.5,299.5 L430,298.5 L430.5,297.5 L431,296.5 L431.5,295.5 L432.5,295 L433,294.5 L433.5,294 L434.5,294 L435,294 L436,294 L436.5,294.5 L437.5,295 L438,295.5 L439,296 L440,297 L440.5,298 L441.5,299 L442.5,300 L443.5,301 L444,302 L445,303 L446,303.5 L446.5,304.5 L447.5,305 L448,305.5 L449,305.5 L450,306 L450.5,306 L451,305.5 L452,305.5 L452.5,305 L453,304 L453.5,303.5 L454.5,302.5 L455,301.5 L455.5,300 L456,299 L456.5,298 L457,296.5 L457.5,295.5 L458.5,294.5 L459,293.5 L459.5,292.5 L460,291.5 L460.5,291 L461.5,290.5 L462,290 L462.5,290 L463.5,290 L464,290 L465,290.5 L465.5,291 L466.5,291.5 L467.5,292 L468,293 L469,294 L470,295 L471,296 L471.5,297 L472.5,298 L473.5,298.5 L474,299.5 L475,300 L476,301 L476.5,301.5 L477.5,301.5 L478,301.5 L479,301.5 L479.5,301.5 L480,301 L481,300.5 L481.5,300 L482,299 L482.5,298.5 L483.5,297 L484,296 L484.5,295 L485,294 L485.5,292.5 L486,291.5 L486.5,290.5 L487,289.5 L488,288.5 L488.5,287.5 L489,287 L489.5,286.5 L490.5,286 L491,286 L492,286 L492.5,286.5 L493.5,287.5 L494.5,288.5 L495,289.5 L496,290 L497,291 L497.5,291.5 L498.5,291.5 L499,291.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M514,289.5 L500,299 L498,284.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="532" cy="277.5" r="8" fill="#ffffff" stroke="#1971c2" stroke-width="2"/>
  <line x1="532" y1="266.5" x2="532" y2="75.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M532,64.5 L537.5,76.5 L526.5,76.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="532" cy="53.5" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="433.5" y="321.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = 14{,}0\,\text{eV}$</div></foreignObject>
  <foreignObject x="452.5" y="357.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ionisoi}$</div></foreignObject>
</svg>

### Bohrin malli historiallisena välivaiheena
Tanskalainen Niels Bohr esitti vuonna 1913 mallin, jossa elektroni kiertää protonia ympyräradalla, mutta vain tietyillä sallituilla radoilla. Sallitulla radalla elektroni ei säteile, vaikka klassisen fysiikan mukaan kiertävän varauksen pitäisi menettää energiaa säteilynä. Valoa syntyy vain, kun elektroni siirtyy radalta toiselle, ja fotonin energia on ratojen energioiden erotus. Radan säde kasvaa kuten $n^2$: perustilan säde on noin $0{,}053\,\text{nm}$, radan $n = 2$ neljä kertaa ja radan $n = 3$ yhdeksän kertaa suurempi.

<svg data-fig="bohr" viewBox="0 0 600 360" role="img" aria-label="Bohrin malli vetyatomista. Keskellä ydin eli protoni, sen ympärillä elektronin sallitut ympyräradat n = 1, 2 ja 3, joiden säteet ovat mittakaavassa suhteessa 1 : 4 : 9. Elektroni siirtyy radalta n = 3 radalle n = 2, ja atomista lähtee fotoni, jonka energia hf on tasojen energioiden erotus E3 − E2." style="max-width:100%;font-size:24px">
  <circle cx="186" cy="180" r="16" fill="none" stroke="#1f2933" stroke-width="2"/>
  <circle cx="186" cy="180" r="64" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="186" cy="180" r="144" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="186" cy="180" r="7" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="317.5" cy="121.5" r="8" fill="#ffffff" stroke="#1971c2" stroke-width="2"/>
  <path d="M307.5,126.5 Q281,111.5 260.5,150" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="6 5"/>
  <path d="M253.5,153 L266.5,144 L264.5,158 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="244.5" cy="154" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="197.5" y="127.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <path d="M341.5,127.5 L343,128.5 L343.5,131 L344.5,134.5 L345,137 L346.5,137.5 L348.5,136.5 L351,135.5 L353.5,133 L356,131 L358,129 L360.5,127.5 L362.5,126.5 L364,127 L365.5,128 L366.5,130 L367,133 L368,136 L368.5,139.5 L369,142.5 L370,144.5 L371,146 L373,146.5 L374.5,146 L377,144.5 L379.5,142.5 L381.5,140.5 L384,138.5 L386.5,136.5 L388.5,136 L390,136 L391.5,137 L392.5,139 L393.5,141.5 L394,144.5 L394.5,148 L395.5,151 L396,153.5 L397.5,155 L399,155.5 L400.5,155 L403,154 L405,152 L407.5,150 L410,147.5 L412.5,146 L414.5,145 L416.5,145 L417.5,145.5 L419,147.5 L419.5,150 L420.5,153.5 L421,156.5 L421.5,159.5 L422.5,162 L423.5,164 L425,164.5 L427,164.5 L429,163.5 L431,161.5 L433.5,159.5 L436,157 L438.5,155.5 L440.5,154 L442.5,154 L444,154.5 L445,156.5 L446,159 L446.5,162 L447,165 L447.5,168.5 L448.5,171 L449.5,173 L451,173.5 L453,173.5 L455,172.5 L457,171 L459.5,168.5 L462,166.5 L464.5,164.5 L466.5,163.5 L468.5,163 L470,163.5 L471,165 L472,167.5 L473,170.5 L473.5,174 L474,177 L474.5,179.5 L476,181.5 L477,182.5 L479,183 L481,182 L483,180 L485.5,178 L488,176 L490.5,174 L492.5,172.5 L494.5,172 L496,172.5 L497.5,174 L498.5,176.5 L499,179 L499.5,182.5 L500,185.5 L501,188.5 L502,190.5 L503.5,192 L505,192 L507,191 L509,189.5 L511.5,187.5 L514,185.5 L516.5,183.5 L518.5,182 L520.5,181 L522.5,181.5 L523,184 L523.5,187.5 L524.5,190 L526,191" fill="none" stroke="#e8590c" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M540,196 L523.5,198 L528.5,184 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="435.5" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf$</div></foreignObject>
  <foreignObject x="398" y="221.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$hf = E_3 - E_2$</div></foreignObject>
  <foreignObject x="163.5" y="213.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 2$</div></foreignObject>
  <foreignObject x="163.5" y="281.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 3$</div></foreignObject>
  <line x1="174" y1="169" x2="74" y2="58" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="16" y="25.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n = 1$</div></foreignObject>
  <foreignObject x="207" y="169.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$p^+$</div></foreignObject>
</svg>

Malli oli suuri edistysaskel. Siitä saadut vedyn energiatasot ovat samat, jotka spektriviivoista mitataan, ja se selitti vetyatomin koon ja ionisaatioenergian. Mallilla on kuitenkin rajansa. Se toimii vain atomeille ja ioneille, joissa on yksi elektroni, eikä se kerro, miksi jotkin spektriviivat ovat kirkkaampia kuin toiset. Elektronilla ei myöskään ole todellisuudessa rataa: luvussa *Aaltomekaaninen atomimalli ja orbitaalit* elektronin paikkaa kuvataan todennäköisyyksillä. Energiatasot säilyvät uudessakin mallissa, mutta kiertoradat jäävät pois.

<figure class="unit-photo"><img src="pics/fy8/orion-nebula.webp" alt="Kaasusumu avaruudessa: punertavia, violetteja ja ruskeita pilviä, joiden keskellä on kirkkaita tähtiä."><figcaption>Orionin sumu Hubble-avaruusteleskoopin kuvassa. Osa sumun hehkusta on vedyn punaista $656\,\text{nm}$:n valoa, joka syntyy, kun elektroni siirtyy tasolta $n = 3$ tasolle $n = 2$.</figcaption></figure>

## Kaava: Vetyatomin energiatasot ja siirtymän fotoni
Vetyatomin energiatasot ovat
```latex
E_n = -\frac{13{,}6\,\text{eV}}{n^2}
```
missä $E_n$ on tason $n$ energia ja $n = 1, 2, 3, \ldots$ on tason järjestysluku. Lauseke on tässä annettu tieto, joka vastaa mitattua vedyn spektriä.

Kun elektroni siirtyy tasolta, jonka energia on $E_\text{y}$, alemmalle tasolle, jonka energia on $E_\text{a}$, syntyvän fotonin energia ja aallonpituus ovat
```latex
\begin{aligned}
hf &= E_\text{y} - E_\text{a} \\
\lambda &= \frac{hc}{E_\text{y} - E_\text{a}}
\end{aligned}
```
missä $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ on Planckin vakio, $f$ fotonin taajuus, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$ valon nopeus ja $\lambda$ aallonpituus. Absorptiossa samat kaavat antavat fotonin, joka nostaa elektronin tasolta $E_\text{a}$ tasolle $E_\text{y}$. Energiat lasketaan ensin elektronivoltteina, ja erotus muunnetaan jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

| Sarja | Alempi taso | Alue | $\lambda$ (nm) |
| --- | --- | --- | --- |
| Lyman | $n = 1$ | ultravioletti | $91{,}2$–$122$ |
| Balmer | $n = 2$ | näkyvä ja lähi-UV | $365$–$656$ |
| Paschen | $n = 3$ | infrapuna | $821$–$1876$ |

Kunkin sarjan pisin aallonpituus tulee siirtymästä lähimmältä ylemmältä tasolta ja lyhin eli sarjan raja siirtymästä, joka alkaa vapaasta elektronista. Koska tasot tihenevät ylöspäin, sarjan viivat tihenevät rajaa kohti.

<svg data-fig="spectrum" viewBox="0 0 600 300" role="img" aria-label="Vedyn näkyvä emissiospektri mittakaavassa aallonpituusakselilla 350–700 nm: tummalla pohjalla neljä viivaa, 410 nm violetti (siirtymä 6 → 2), 434 nm sininen (5 → 2), 486 nm syaani (4 → 2) ja 656 nm punainen (3 → 2). Katkoviiva kohdassa 365 nm on sarjan raja, siirtymä äärettömyydestä tasolle 2. Viivat tihenevät lyhyitä aallonpituuksia kohti." style="max-width:100%;font-size:24px">
  <rect x="40" y="80" width="430" height="66" rx="3" fill="#1f2933"/>
  <line x1="58" y1="84" x2="58" y2="142" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <rect x="413.5" y="82" width="6" height="62" fill="#c92a2a"/>
  <line x1="416.5" y1="70" x2="416.5" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="204.5" y="82" width="6" height="62" fill="#1098ad"/>
  <line x1="207.5" y1="70" x2="207.5" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="140.5" y="82" width="6" height="62" fill="#4263eb"/>
  <line x1="143.5" y1="70" x2="143.5" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="111" y="82" width="6" height="62" fill="#7048e8"/>
  <line x1="114" y1="70" x2="114" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="58" y1="70" x2="58" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$410$</div></foreignObject>
  <foreignObject x="121" y="13.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$434$</div></foreignObject>
  <foreignObject x="185" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$486$</div></foreignObject>
  <foreignObject x="394" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$656$</div></foreignObject>
  <foreignObject x="35.5" y="43.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$365$</div></foreignObject>
  <line x1="40" y1="160" x2="480" y2="160" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M492,160 L479,166 L479,154 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="101.5" y1="160" x2="101.5" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="79" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$400$</div></foreignObject>
  <line x1="224.5" y1="160" x2="224.5" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="202" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$500$</div></foreignObject>
  <line x1="347" y1="160" x2="347" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324.5" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$600$</div></foreignObject>
  <line x1="470" y1="160" x2="470" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="171.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$700$</div></foreignObject>
  <foreignObject x="498" y="145.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <line x1="114" y1="202" x2="128" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="105.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6 \to 2$</div></foreignObject>
  <line x1="143.5" y1="202" x2="204" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="181.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5 \to 2$</div></foreignObject>
  <line x1="207.5" y1="202" x2="280" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="257.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4 \to 2$</div></foreignObject>
  <line x1="416.5" y1="202" x2="416.5" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="394" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3 \to 2$</div></foreignObject>
  <line x1="58" y1="202" x2="52" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="29.5" y="239.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\infty \to 2$</div></foreignObject>
</svg>

## Esimerkki
Vetylampun punainen viiva syntyy, kun vetyatomin elektroni siirtyy tasolta $n = 3$ tasolle $n = 2$. Laske syntyvän fotonin aallonpituus.

<!-- vaihe -->

**Tunnetut ja kysytty.** Ylempi taso $n = 3$, alempi taso $n = 2$, tasojen energiat $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$. Kysytään fotonin aallonpituutta $\lambda$.

<!-- vaihe -->

**Periaate.** Energia säilyy: atomin energia pienenee tasojen erotuksen verran, ja juuri tämän energian vie mukanaan yksi fotoni. Fotonin energia on $hf = \tfrac{hc}{\lambda}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Merkitään fotonin energia tasojen erotukseksi ja ratkaistaan aallonpituus:
```latex
\begin{aligned}
&\frac{hc}{\lambda} = E_3 - E_2 \\
&\lambda = \frac{hc}{E_3 - E_2}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Tasojen energiat ovat elektronivoltteina, mutta $h$ on yksikössä $\text{J}\,\text{s}$. Energiaero muunnetaan siksi jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin energiaero ja sitten aallonpituus:
```latex
\begin{aligned}
&E_3 - E_2 \\
&= -\frac{13{,}6\,\text{eV}}{9} + \frac{13{,}6\,\text{eV}}{4} \\
&= 1{,}8889\,\text{eV} \\
&= 1{,}8889 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} \\
&= 3{,}0260 \cdot 10^{-19}\,\text{J} \\[6pt]
&hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \\
&\quad \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} \\
&= 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m} \\[6pt]
&\lambda = \frac{hc}{E_3 - E_2} \\
&= \frac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{3{,}0260 \cdot 10^{-19}\,\text{J}} \\
&= 6{,}5647 \cdot 10^{-7}\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Aallonpituus on $\lambda \approx 6{,}56 \cdot 10^{-7}\,\text{m} = 656\,\text{nm}$. Tulos ilmoitetaan kolmella merkitsevällä numerolla, koska perustilan energia $13{,}6\,\text{eV}$ tunnetaan kolmen numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Aallonpituus $656\,\text{nm}$ on punaista valoa, ja juuri sellainen viiva vedyn spektrissä näkyy. Fotonin energia $1{,}89\,\text{eV}$ on näkyvän valon fotonien välillä $1{,}7$–$3{,}3\,\text{eV}$. Pienin Balmerin sarjan energiaero antaa sarjan pisimmän aallonpituuden, kuten pitääkin.

## Yleinen virhekäsitys
Moni laskee fotonin energian yhden tason energiasta, esimerkiksi siirtymälle $4 \to 2$ arvosta $|E_4| = 0{,}85\,\text{eV}$. Silloin aallonpituudeksi tulisi noin $1460\,\text{nm}$, vaikka siirtymä tuottaa syaanin viivan $486\,\text{nm}$. Fotoni ei kanna tason energiaa vaan **tasojen erotuksen** $E_\text{y} - E_\text{a}$. Negatiivinen tason energia ei myöskään tarkoita, että energiaa puuttuisi: se kertoo, kuinka paljon energiaa elektronin irrottaminen vaatii.

Toinen virhe on pitää Bohrin ratoja todellisina kiertoratoina, joilla elektroni kiertää kuin planeetta. Bohrin malli antaa vedylle oikeat energiat, mutta elektronin rataa ei voi havaita, eikä sitä nykyisessä atomimallissa ole.

## Tiivistelmä
- Vetyatomin energia on kvantittunut: $E_n = -\tfrac{13{,}6\,\text{eV}}{n^2}$. Perustila on $n = 1$, viritystilat $n \geq 2$, ja ionisaatioenergia perustilasta on $13{,}6\,\text{eV}$.
- Siirtymässä ylemmältä tasolta alemmalle syntyy fotoni, jonka energia on tasojen erotus: $hf = E_\text{y} - E_\text{a}$ ja $\lambda = \tfrac{hc}{E_\text{y} - E_\text{a}}$.
- Atomi absorboi vain fotonin, jonka energia on tasojen erotus, tai ionisoituu fotonista, jonka energia on vähintään ionisaatioenergia.
- Tasolle $n = 2$ päättyvät siirtymät (Balmerin sarja) antavat vedyn näkyvät viivat $656\,\text{nm}$, $486\,\text{nm}$, $434\,\text{nm}$ ja $410\,\text{nm}$; tasolle $n = 1$ päättyvät ovat ultraviolettia.
- Bohrin malli (1913) selitti vedyn spektrin sallituilla radoilla, mutta se toimii vain yhden elektronin atomeille. Aaltomekaaninen malli säilyttää energiatasot ja hylkää radat.
