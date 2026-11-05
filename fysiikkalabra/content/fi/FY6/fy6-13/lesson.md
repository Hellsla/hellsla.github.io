# Kondensaattori ja sen energia

> **Miksi** kameran salamavalo tarvitsee muutaman sekunnin latautumisajan, vaikka itse välähdys kestää vain millisekunnin?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: hämärässä huoneessa pöydällä on kolmijalan päällä kamera, jonka salamavalo välähtää kirkkaasti. Salaman valo leviää viuhkana oikealle kohti pöydän päässä olevaa kukkamaljakkoa. Kameran vieressä pöydällä on kaksi AA-paristoa, jotka lataavat salaman kondensaattorin." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy613h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><radialGradient id="fy613h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/><stop offset="0.35" stop-color="#ffc078" stop-opacity="0.55"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient><linearGradient id="fy613h-fan" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff" stop-opacity="0.85"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></linearGradient><linearGradient id="fy613h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#e9c98a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="400" fill="url(#fy613h-wall)"/>
  <path d="M612,214 L1180,40 L1180,470 Z" fill="url(#fy613h-fan)" stroke-linejoin="round"/>
  <circle cx="612" cy="214" r="190" fill="url(#fy613h-glow)"/>
  <rect x="0" y="400" width="1200" height="200" fill="url(#fy613h-table)"/>
  <rect x="0" y="392" width="1200" height="16" fill="#a97a35"/>
  <path d="M0,436 C320,430 760,444 1200,434" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.4"/>
  <path d="M0,470 C320,464 760,478 1200,468" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.4"/>
  <path d="M0,504 C320,498 760,512 1200,502" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.4"/>
  <path d="M0,538 C320,532 760,546 1200,536" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.4"/>
  <path d="M0,572 C320,566 760,580 1200,570" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.4"/>
  <line x1="530" y1="330" x2="440" y2="452" stroke="#1f2933" stroke-width="7" stroke-linecap="round"/>
  <line x1="530" y1="330" x2="530" y2="452" stroke="#1f2933" stroke-width="7" stroke-linecap="round"/>
  <line x1="530" y1="330" x2="620" y2="452" stroke="#1f2933" stroke-width="7" stroke-linecap="round"/>
  <rect x="518" y="296" width="24" height="40" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="400" y="196" width="260" height="110" rx="18" fill="#1f2933"/>
  <rect x="410" y="206" width="240" height="90" rx="12" fill="#6c757d"/>
  <rect x="430" y="176" width="80" height="26" rx="6" fill="#1f2933"/>
  <circle cx="500" cy="252" r="52" fill="#1f2933"/>
  <circle cx="500" cy="252" r="40" fill="#8a96a3"/>
  <circle cx="500" cy="252" r="28" fill="#2f74b5"/>
  <circle cx="490" cy="242" r="9" fill="#a5d8ff"/>
  <rect x="584" y="200" width="56" height="28" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="592" y="206" width="40" height="16" rx="4" fill="#ffc078"/>
  <circle cx="632" cy="270" r="9" fill="#c92a2a"/>
  <rect x="300" y="440" width="30" height="92" rx="6" fill="#2b8a3e" stroke="#1f2933" stroke-width="3"/>
  <rect x="309" y="432" width="12" height="10" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="340" y="434" width="30" height="92" rx="6" fill="#2b8a3e" stroke="#1f2933" stroke-width="3"/>
  <rect x="349" y="426" width="12" height="10" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M960,420 Q936,360 962,320 L1018,320 Q1044,360 1020,420 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="982" y1="322" x2="964" y2="202" stroke="#2b8a3e" stroke-width="4" stroke-linecap="round"/>
  <circle cx="964" cy="202" r="18" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="964" cy="202" r="6" fill="#ffc078"/>
  <line x1="990" y1="322" x2="990" y2="172" stroke="#2b8a3e" stroke-width="4" stroke-linecap="round"/>
  <circle cx="990" cy="172" r="18" fill="#e8590c" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="990" cy="172" r="6" fill="#ffc078"/>
  <line x1="997" y1="322" x2="1014" y2="212" stroke="#2b8a3e" stroke-width="4" stroke-linecap="round"/>
  <circle cx="1014" cy="212" r="18" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="1014" cy="212" r="6" fill="#ffc078"/>
</svg>

## Ydinajatus

### Kaksi johdelevyä ja niiden välissä eriste
**Kondensaattori** on kaksi johdekappaletta, esimerkiksi metallilevyä, joiden välissä on **eriste**. Kun kondensaattori kytketään jännitelähteeseen, lähde siirtää elektroneja johtimia pitkin levystä toiseen. Lähteen plusnapaan kytketystä levystä elektroneja poistuu, joten se varautuu positiivisesti, ja miinusnapaan kytkettyyn levyyn elektroneja tulee yhtä paljon lisää. Levyjen varaukset ovat siksi $+Q$ ja $-Q$, ja kondensaattori on kokonaisuutena sähköisesti neutraali. **Kondensaattorin varauksella** $Q$ tarkoitetaan toisen levyn varauksen suuruutta. Varaukset eivät kulje eristeen läpi levystä toiseen.

Varattujen levyjen välissä on homogeeninen sähkökenttä, joka osoittaa positiivisesta levystä negatiiviseen. Sen voimakkuus on $E = \tfrac{U}{d}$, missä $U$ on levyjen välinen jännite ja $d$ levyjen etäisyys (luku *Homogeeninen sähkökenttä*).

<svg data-fig="rakenne" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva, ei mittakaavassa: levykondensaattori kytkettynä jännitelähteeseen. Vasemmalla jännitelähde, jonka jännite on U ja plusnapa ylhäällä. Plusnavasta johto kulkee vasempaan metallilevyyn ja miinusnavasta oikeaan. Levyt ovat pystyssä vastakkain, ja niiden välinen etäisyys on d. Vasemman levyn sisäpinnalla on viisi punaista positiivista varausta, yhteensä +Q, ja oikean levyn sisäpinnalla viisi sinistä negatiivista varausta, yhteensä −Q. Levyjen välissä on eristettä, tässä ilmaa, ja siinä tasavälisiä vaakasuoria vihreitä kenttäviivoja, joiden nuolet osoittavat positiivisesta levystä negatiiviseen: homogeeninen sähkökenttä E." style="max-width:100%;font-size:24px">
  <polyline points="92,169 92,52 262,52 262,104" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,185 92,324 382,324 382,264" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="64" y="166" width="56" height="22" fill="#ffffff"/>
  <line x1="66" y1="169" x2="118" y2="169" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="79" y1="185" x2="105" y2="185" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="26" y="162.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="128" y="149.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <rect x="256" y="104" width="12" height="160" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="376" y="104" width="12" height="160" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="278" cy="120" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="273.5" y1="120" x2="282.5" y2="120" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="278" y1="115.5" x2="278" y2="124.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="366" cy="120" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="361.5" y1="120" x2="370.5" y2="120" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="278" cy="152" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="273.5" y1="152" x2="282.5" y2="152" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="278" y1="147.5" x2="278" y2="156.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="366" cy="152" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="361.5" y1="152" x2="370.5" y2="152" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="278" cy="184" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="273.5" y1="184" x2="282.5" y2="184" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="278" y1="179.5" x2="278" y2="188.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="366" cy="184" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="361.5" y1="184" x2="370.5" y2="184" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="278" cy="216" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="273.5" y1="216" x2="282.5" y2="216" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="278" y1="211.5" x2="278" y2="220.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="366" cy="216" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="361.5" y1="216" x2="370.5" y2="216" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="278" cy="248" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="273.5" y1="248" x2="282.5" y2="248" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="278" y1="243.5" x2="278" y2="252.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="366" cy="248" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="361.5" y1="248" x2="370.5" y2="248" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="284" y1="136" x2="348" y2="136" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M360,136 L347,142 L347,130 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="284" y1="168" x2="348" y2="168" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M360,168 L347,174 L347,162 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="284" y1="200" x2="348" y2="200" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M360,200 L347,206 L347,194 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="284" y1="232" x2="348" y2="232" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M360,232 L347,238 L347,226 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="302" y="69.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="180" y="169.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$+Q$</div></foreignObject>
  <foreignObject x="404" y="169.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$-Q$</div></foreignObject>
  <line x1="322" y1="284" x2="277" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M268,284 L278,279.5 L278,288.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="322" y1="284" x2="367" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M376,284 L366,288.5 L366,279.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="268" y1="275" x2="268" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="376" y1="275" x2="376" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="302" y="293.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="452" y="97.5" width="136" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{metallilevy}$</div></foreignObject>
  <line x1="447" y1="112" x2="391" y2="118" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="452" y="279.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <line x1="447" y1="294" x2="346" y2="262" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

### Lataus ja purkautuminen
Kun kondensaattoria ladataan vastuksen kautta, latauksen alussa levyt ovat varauksettomia ja kondensaattorin jännite $U_C$ on nolla. Koko lähteen jännite on silloin vastuksen yli, ja virta on suurin. Kun levyille kertyy varausta, kondensaattorin jännite kasvaa, vastuksen jännite pienenee ja virta pienenee. Lataus päättyy, kun kondensaattorin jännite on yhtä suuri kuin lähteen jännite $U_0$: silloin virtaa ei enää kulje.

Kun ladattu kondensaattori kytketään esimerkiksi lamppuun, se toimii jännitelähteenä ja purkautuu. Virta on suurin heti alussa ja kulkee vastakkaiseen suuntaan kuin latauksessa. Kun varaus pienenee, jännite ja virta pienenevät vähitellen nollaan. Mitä suurempi resistanssi piirissä on, sitä hitaammin lataus ja purkautuminen tapahtuvat.

<svg data-fig="lataus" viewBox="0 0 600 420" role="img" aria-label="Kaavakuva, ei mittakaavassa: kaksi kuvaajaa yhteisellä aika-akselilla. Ylempi: kondensaattorin jännite U_C ajan t funktiona. Latauksessa jännite nousee aluksi jyrkästi ja sitten yhä loivemmin kohti lähteen jännitettä U_0, joka on merkitty katkoviivalla. Purkautumisessa jännite laskee aluksi jyrkästi ja sitten yhä loivemmin kohti nollaa. Alempi: virta I. Latauksen alussa virta on suurin ja pienenee vähitellen nollaan. Purkautumisen alussa virta on suurin mutta vastakkaissuuntainen eli negatiivinen, ja sen suuruus pienenee vähitellen nollaan. Pystysuora katkoviiva erottaa latauksen ja purkautumisen." style="max-width:100%;font-size:24px">
  <line x1="92" y1="94" x2="470" y2="94" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="182" x2="484" y2="182" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,182 L483,188 L483,176 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="183" x2="92" y2="58" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,46 L98,59 L86,59 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="85" y1="94" x2="92" y2="94" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="502" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="82" y="15.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_C$</div></foreignObject>
  <line x1="92" y1="404" x2="92" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="91" y1="340" x2="484" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,340 L483,346 L483,334 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="341" x2="92" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,250 L98,263 L86,263 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="325.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="82" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I$</div></foreignObject>
  <line x1="92" y1="94" x2="470" y2="94" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="40" y="79.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_0$</div></foreignObject>
  <polyline points="92,182 94,178 95.5,174 97.5,170 99.5,166.5 101,163 103,160 105,156.5 106.5,153.5 108.5,151 110.5,148 112,145.5 114,143 116,141 117.5,138.5 119.5,136.5 121.5,134.5 123,132.5 125,131 127,129 128.5,127.5 130.5,126 132.5,124.5 134,123 136,121.5 138,120 139.5,119 141.5,118 143.5,116.5 145,115.5 147,114.5 149,113.5 150.5,112.5 152.5,112 154.5,111 156,110 158,109.5 160,108.5 161.5,108 163.5,107.5 165.5,106.5 167,106 169,105.5 171,105 172.5,104.5 174.5,104 176.5,103.5 178,103 180,102.5 182,102 183.5,102 185.5,101.5 187.5,101 189,100.5 191,100.5 193,100 194.5,100 196.5,99.5 198.5,99.5 200,99 202,99 204,98.5 205.5,98.5 207.5,98 209.5,98 211,98 213,97.5 215,97.5 216.5,97.5 218.5,97 220.5,97 222,97 224,96.5 226,96.5 227.5,96.5 229.5,96.5 231.5,96 233,96 235,96 237,96 238.5,96 240.5,95.5 242.5,95.5 244,95.5 246,95.5 248,95.5 249.5,95.5 251.5,95.5 253.5,95 255,95 257,95 259,95 260.5,95 262.5,95 264.5,95 266,95 268,95 270,95 271.5,95 273.5,94.5 275.5,94.5 277,94.5 279,94.5 281,94.5 282.5,98.5 284.5,102.5 286.5,106 288,109.5 290,113 292,116.5 293.5,119.5 295.5,122.5 297.5,125.5 299,128 301,130.5 303,133 304.5,135.5 306.5,137.5 308.5,139.5 310,141.5 312,143.5 314,145.5 315.5,147 317.5,148.5 319.5,150.5 321,152 323,153 325,154.5 326.5,156 328.5,157 330.5,158.5 332,159.5 334,160.5 336,161.5 337.5,162.5 339.5,163.5 341.5,164.5 343,165 345,166 347,166.5 348.5,167.5 350.5,168 352.5,169 354,169.5 356,170 358,170.5 359.5,171 361.5,171.5 363.5,172 365,172.5 367,173 369,173.5 370.5,174 372.5,174 374.5,174.5 376,175 378,175.5 380,175.5 381.5,176 383.5,176 385.5,176.5 387,176.5 389,177 391,177 392.5,177.5 394.5,177.5 396.5,178 398,178 400,178 402,178.5 403.5,178.5 405.5,179 407.5,179 409,179 411,179 413,179.5 414.5,179.5 416.5,179.5 418.5,179.5 420,180 422,180 424,180 425.5,180 427.5,180 429.5,180.5 431,180.5 433,180.5 435,180.5 436.5,180.5 438.5,180.5 440.5,180.5 442,181 444,181 446,181 447.5,181 449.5,181 451.5,181 453,181 455,181 457,181 458.5,181" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,287 94,289.5 96,292 97.5,294.5 99.5,296.5 101.5,299 103.5,301 105,302.5 107,304.5 109,306.5 111,308 113,309.5 114.5,311 116.5,312.5 118.5,313.5 120.5,315 122,316 124,317.5 126,318.5 128,319.5 130,320.5 131.5,321.5 133.5,322.5 135.5,323.5 137.5,324 139,325 141,325.5 143,326.5 145,327 147,327.5 148.5,328 150.5,329 152.5,329.5 154.5,330 156.5,330.5 158,331 160,331.5 162,331.5 164,332 165.5,332.5 167.5,333 169.5,333 171.5,333.5 173.5,334 175,334 177,334.5 179,334.5 181,335 182.5,335 184.5,335.5 186.5,335.5 188.5,336 190.5,336 192,336.5 194,336.5 196,336.5 198,337 199.5,337 201.5,337 203.5,337 205.5,337.5 207.5,337.5 209,337.5 211,337.5 213,338 215,338 216.5,338 218.5,338 220.5,338 222.5,338.5 224.5,338.5 226,338.5 228,338.5 230,338.5 232,338.5 234,339 235.5,339 237.5,339 239.5,339 241.5,339 243,339 245,339 247,339 249,339 251,339 252.5,339 254.5,339.5 256.5,339.5 258.5,339.5 260,339.5 262,339.5 264,339.5 266,339.5 268,339.5 269.5,339.5 271.5,339.5 273.5,339.5 275.5,339.5 277,339.5 279,339.5 281,339.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="281,392.5 283,390 284.5,388 286.5,385.5 288,383.5 290,381.5 291.5,379.5 293.5,378 295,376 297,374.5 299,373 300.5,371.5 302.5,370 304,368.5 306,367 307.5,366 309.5,365 311,363.5 313,362.5 315,361.5 316.5,360.5 318.5,359.5 320,358.5 322,358 323.5,357 325.5,356 327,355.5 329,355 330.5,354 332.5,353.5 334.5,353 336,352 338,351.5 339.5,351 341.5,350.5 343,350 345,349.5 346.5,349 348.5,349 350.5,348.5 352,348 354,347.5 355.5,347.5 357.5,347 359,346.5 361,346.5 362.5,346 364.5,346 366.5,345.5 368,345 370,345 371.5,345 373.5,344.5 375,344.5 377,344 378.5,344 380.5,344 382.5,343.5 384,343.5 386,343.5 387.5,343 389.5,343 391,343 393,342.5 394.5,342.5 396.5,342.5 398.5,342.5 400,342.5 402,342 403.5,342 405.5,342 407,342 409,342 410.5,341.5 412.5,341.5 414,341.5 416,341.5 418,341.5 419.5,341.5 421.5,341.5 423,341 425,341 426.5,341 428.5,341 430,341 432,341 434,341 435.5,341 437.5,341 439,341 441,341 442.5,340.5 444.5,340.5 446,340.5 448,340.5 450,340.5 451.5,340.5 453.5,340.5 455,340.5 457,340.5 458.5,340.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="281,339.5 281,392.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="281" y1="72" x2="281" y2="404" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="136.5" y="205.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lataus}$</div></foreignObject>
  <foreignObject x="285.5" y="205.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{purkautuminen}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/film-capacitor.webp" alt="Harmaa suorakulmainen komponentti vihreällä piirilevyllä; kylkeen on painettu KNB1560, MKP, X2, 0,1 µF ja 275 VAC."><figcaption>Kalvokondensaattori, jonka kapasitanssi on $0{,}1\,\mu\text{F}$. Merkintä MKP kertoo, että eristeenä on ohut polypropeenikalvo, ja $275\,\text{V}$ on suurin vaihtojännite, jolla kondensaattoria saa käyttää.</figcaption></figure>

### Kapasitanssi kertoo, kuinka paljon varausta jännite tuo
Kun kondensaattorin jännite kaksinkertaistuu, kenttä levyjen välissä kaksinkertaistuu, ja siihen tarvitaan kaksinkertainen varaus. Varaus on siis suoraan verrannollinen jännitteeseen. Niiden suhde on kondensaattorin **kapasitanssi**, joka riippuu vain kondensaattorin rakenteesta: levyjen pinta-alasta $A$, niiden etäisyydestä $d$ ja eristeestä. Suuremmille levyille mahtuu enemmän varausta samalla kentällä. Kun levyt ovat lähempänä toisiaan, sama jännite tuottaa voimakkaamman kentän $E = \tfrac{U}{d}$, ja voimakkaampi kenttä vaatii levyille enemmän varausta. Kapasitanssi ei riipu jännitteestä eikä varauksesta.

### Eriste kasvattaa kapasitanssia
Eristeessä varaukset eivät pääse liikkumaan vapaasti, mutta sähkökenttä siirtää molekyylien elektroneja hieman kohti positiivista levyä. Eriste **polarisoituu**: sen positiivista levyä vasten olevalle pinnalle tulee negatiivista ja vastakkaiselle pinnalle positiivista varausta. Nämä varaukset heikentävät levyjen kenttää. Kun levyillä on sama varaus, eristeen sisällä kenttä on heikompi kuin ilmassa, joten myös jännite on pienempi. Kapasitanssi on silloin suurempi.

<svg data-fig="eriste" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva, ei mittakaavassa: kaksi samanlaista levykondensaattoria, joissa on sama varaus Q: vasemmalla levyssä viisi positiivista ja oikealla viisi negatiivista varausta. Vasemmanpuoleisen kondensaattorin levyjen välissä on ilmaa ja neljä kenttäviivaa. Oikeanpuoleisen levyjen välissä on eristettä, jonka yhdeksän molekyyliä kolmessa rivissä ovat polarisoituneet: kunkin molekyylin negatiivinen puoli on kääntynyt kohti positiivista levyä ja positiivinen puoli kohti negatiivista levyä. Eristeessä kenttäviivoja on vain kaksi, joten kenttä on heikompi. Ilmaa sisältävän kondensaattorin jännite U on suurempi, eristettä sisältävän pienempi." style="max-width:100%;font-size:24px">
  <rect x="46" y="76" width="12" height="180" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="226" y="76" width="12" height="180" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="68" cy="92" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="63.5" y1="92" x2="72.5" y2="92" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="68" y1="87.5" x2="68" y2="96.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="216" cy="92" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="211.5" y1="92" x2="220.5" y2="92" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="68" cy="129" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="63.5" y1="129" x2="72.5" y2="129" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="68" y1="124.5" x2="68" y2="133.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="216" cy="129" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="211.5" y1="129" x2="220.5" y2="129" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="68" cy="166" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="63.5" y1="166" x2="72.5" y2="166" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="68" y1="161.5" x2="68" y2="170.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="216" cy="166" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="211.5" y1="166" x2="220.5" y2="166" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="68" cy="203" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="63.5" y1="203" x2="72.5" y2="203" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="68" y1="198.5" x2="68" y2="207.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="216" cy="203" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="211.5" y1="203" x2="220.5" y2="203" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="68" cy="240" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="63.5" y1="240" x2="72.5" y2="240" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="68" y1="235.5" x2="68" y2="244.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="216" cy="240" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="211.5" y1="240" x2="220.5" y2="240" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="74" y1="110.5" x2="198" y2="110.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M210,110.5 L197,116.5 L197,104.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="74" y1="147.5" x2="198" y2="147.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M210,147.5 L197,153.5 L197,141.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="74" y1="184.5" x2="198" y2="184.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M210,184.5 L197,190.5 L197,178.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="74" y1="221.5" x2="198" y2="221.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M210,221.5 L197,227.5 L197,215.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="87" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="77" y="275.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sama } Q$</div></foreignObject>
  <foreignObject x="42" y="309.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{suurempi } U$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="336" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="358" y="76" width="168" height="180" fill="#eef5f9"/>
  <rect x="346" y="76" width="12" height="180" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="526" y="76" width="12" height="180" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="368" cy="92" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="363.5" y1="92" x2="372.5" y2="92" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="368" y1="87.5" x2="368" y2="96.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="516" cy="92" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="511.5" y1="92" x2="520.5" y2="92" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="368" cy="129" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="363.5" y1="129" x2="372.5" y2="129" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="368" y1="124.5" x2="368" y2="133.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="516" cy="129" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="511.5" y1="129" x2="520.5" y2="129" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="368" cy="166" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="363.5" y1="166" x2="372.5" y2="166" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="368" y1="161.5" x2="368" y2="170.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="516" cy="166" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="511.5" y1="166" x2="520.5" y2="166" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="368" cy="203" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="363.5" y1="203" x2="372.5" y2="203" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="368" y1="198.5" x2="368" y2="207.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="516" cy="203" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="511.5" y1="203" x2="520.5" y2="203" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="368" cy="240" r="8" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="363.5" y1="240" x2="372.5" y2="240" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <line x1="368" y1="235.5" x2="368" y2="244.5" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <circle cx="516" cy="240" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="511.5" y1="240" x2="520.5" y2="240" stroke="#ffffff" stroke-width="2.2" stroke-linecap="butt"/>
  <path d="M399,102.5 A15,7.5 0 0 0 399,117.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M399,102.5 A15,7.5 0 0 1 399,117.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M442,102.5 A15,7.5 0 0 0 442,117.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M442,102.5 A15,7.5 0 0 1 442,117.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M485,102.5 A15,7.5 0 0 0 485,117.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M485,102.5 A15,7.5 0 0 1 485,117.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M399,158.5 A15,7.5 0 0 0 399,173.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M399,158.5 A15,7.5 0 0 1 399,173.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M442,158.5 A15,7.5 0 0 0 442,173.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M442,158.5 A15,7.5 0 0 1 442,173.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M485,158.5 A15,7.5 0 0 0 485,173.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M485,158.5 A15,7.5 0 0 1 485,173.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M399,214.5 A15,7.5 0 0 0 399,229.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M399,214.5 A15,7.5 0 0 1 399,229.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M442,214.5 A15,7.5 0 0 0 442,229.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M442,214.5 A15,7.5 0 0 1 442,229.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M485,214.5 A15,7.5 0 0 0 485,229.5 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M485,214.5 A15,7.5 0 0 1 485,229.5 Z" fill="#f2a69c" stroke="#c92a2a" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="380" y1="138" x2="492" y2="138" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M504,138 L491,144 L491,132 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="380" y1="194" x2="492" y2="194" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M504,194 L491,200 L491,188 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="387" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <foreignObject x="377" y="275.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sama } Q$</div></foreignObject>
  <foreignObject x="342" y="309.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pienempi } U$</div></foreignObject>
</svg>

### Energia on sähkökentässä
Varauksen siirtäminen levystä toiseen vaatii työtä, koska positiivinen levy vetää elektroneja puoleensa ja negatiivinen levy hylkii niitä. Tämä työ varastoituu levyjen väliseen sähkökenttään energiaksi, ja purkautuessaan kondensaattori luovuttaa energian takaisin. Salamalaitteen paristot jaksavat antaa vain pientä tehoa, joten kondensaattorin lataaminen kestää sekunteja. Salamaputken läpi kondensaattori purkautuu millisekunnissa, ja sama energia vapautuu tuhansia kertoja suuremmalla teholla.

<figure class="unit-photo"><img src="pics/fy6/capacitor-bank.webp" alt="Sähköasema ylhäältä: aidatulla soralla on telineissä kondensaattoriryhmiä, joiden päällä on harmaita eristimiä, ja niitä yhdistävät johtimet."><figcaption>Sähköaseman kondensaattoriparisto. Suurjännitteellä toimivien kondensaattorien eristeiden on kestettävä suuri sähkökenttä. Alue on aidattu, koska varattu kondensaattori voi olla vaarallinen vielä irrottamisen jälkeen.</figcaption></figure>

### Läpilyöntilujuus
Jokainen eriste kestää vain tietyn suuruisen sähkökentän. Kun kenttä ylittää eristeen **läpilyöntilujuuden** $E_\text{max}$, eristeen molekyyleistä irtoaa elektroneja, eriste alkaa johtaa ja levyjen välillä purkautuu kipinä. Kondensaattori voi silloin vaurioitua pysyvästi. Siksi jokaiseen kondensaattoriin on merkitty suurin sallittu jännite. Ilman läpilyöntilujuus on noin $3\,\text{MV/m}$, ja salama on ilman läpilyönti suuressa mittakaavassa.

Suuri kondensaattori voi säilyttää vaarallisen jännitteen pitkään sen jälkeen, kun laite on irrotettu sähköverkosta. Esimerkiksi mikroaaltouunin ja salamalaitteen kondensaattorit voivat antaa sähköiskun, joten avattua laitetta ei kosketa ennen kuin kondensaattorit on purettu.

## Kaava: Kapasitanssi ja kondensaattorin energia
Kondensaattorin kapasitanssi on varauksen ja jännitteen suhde:
```latex
C = \frac{Q}{U}
```
missä $C$ on kapasitanssi ($\text{F}$), $Q$ kondensaattorin varaus ($\text{C}$) ja $U$ levyjen välinen jännite ($\text{V}$).

Kapasitanssin yksikkö on faradi, $1\,\text{F} = 1\,\tfrac{\text{C}}{\text{V}}$. Faradi on suuri yksikkö, joten tavallisten kondensaattorien kapasitanssit ilmoitetaan mikro-, nano- tai pikofaradeina, esimerkiksi $470\,\mu\text{F} = 470 \cdot 10^{-6}\,\text{F}$.

### Levykondensaattori
Levykondensaattorin kapasitanssi on
```latex
C = \frac{\varepsilon_0 \varepsilon_\text{r} A}{d}
```
missä $A$ on levyn pinta-ala ($\text{m}^2$), $d$ levyjen etäisyys ($\text{m}$), $\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\text{F/m}$ sähkövakio eli tyhjiön permittiivisyys ja $\varepsilon_\text{r}$ eristeen suhteellinen permittiivisyys. Kaava pätee, kun levyjen etäisyys on pieni levyjen kokoon verrattuna (kenttä on homogeeninen eikä reunoja huomioida) ja eriste täyttää levyjen välin. Suhteellinen permittiivisyys kertoo, kuinka moninkertaiseksi eriste kasvattaa kapasitanssia tyhjiöön verrattuna. Ilmalle $\varepsilon_\text{r} \approx 1{,}0$.

| Eriste | $\varepsilon_\text{r}$ | $E_\text{max}\ (\text{MV/m})$ |
|---|---|---|
| ilma | $1{,}0$ | $3$ |
| teflon | $2{,}1$ | $60$ |
| paperi | $3{,}7$ | $16$ |
| lasi | $5{,}6$ | $14$ |

Taulukon arvot ovat likimääräisiä: ne riippuvat aineen laadusta, kosteudesta ja lämpötilasta.

### Suurin sallittu jännite
Levyjen välinen kenttä on $E = \tfrac{U}{d}$, joten eriste kestää jännitteen
```latex
U_\text{max} = E_\text{max} d
```
missä $U_\text{max}$ on suurin jännite ($\text{V}$), jolla läpilyöntiä ei tapahdu, $E_\text{max}$ eristeen läpilyöntilujuus ($\text{V/m}$) ja $d$ eristekerroksen paksuus ($\text{m}$). Esimerkiksi $0{,}010\,\text{mm}$:n paperikerros kestää noin $16 \cdot 10^{6}\,\tfrac{\text{V}}{\text{m}} \cdot 0{,}010 \cdot 10^{-3}\,\text{m} = 160\,\text{V}$.

### Kondensaattorin energia
Ladattaessa varaus kasvaa nollasta arvoon $Q$, ja jännite kasvaa samassa suhteessa nollasta arvoon $U$. Kun pieni varaus siirretään levystä toiseen jännitteen yli, se saa energian, joka on varaus kertaa senhetkinen jännite (luku *Potentiaalienergia ja potentiaali sähkökentässä*). Ensimmäiset varaukset siirtyvät pienen jännitteen yli ja viimeiset koko jännitteen $U$ yli, joten keskimääräinen jännite on $\tfrac{U}{2}$. Energia on $(Q, U)$-kuvaajan alle jäävän kolmion pinta-ala.

<svg data-fig="energia" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva: kondensaattorin jännite U varauksen Q funktiona latauksen aikana. Kuvaaja on origon kautta kulkeva suora, koska jännite kasvaa samassa suhteessa kuin varaus. Suoran alle on piirretty kapeita pylväitä: kukin kuvaa pientä varausta, joka siirretään senhetkisen jännitteen yli, ja pylvään pinta-ala on sen saama energia. Pylväät ovat alussa matalia ja lopussa korkeita. Suoran ja Q-akselin väliin jäävä kolmio on sävytetty oranssiksi; sen pinta-ala on kondensaattorin energia W = ½QU. Vaakasuora katkoviiva kulkee keskimääräisen jännitteen U/2 kohdalla, ja sen alle jäävä suorakulmio on yhtä suuri kuin kolmio." style="max-width:100%;font-size:24px">
  <line x1="395" y1="290" x2="395" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="198.5" x2="440" y2="198.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="106.5" x2="440" y2="106.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="454" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M466,290 L453,296 L453,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="395" y1="290" x2="395" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <line x1="89" y1="198.5" x2="96" y2="198.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="184" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{U}{2}$</div></foreignObject>
  <line x1="89" y1="106.5" x2="96" y2="106.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="92" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="472" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{varaus}$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{jännite}$</div></foreignObject>
  <polygon points="96,290 395,106.5 395,290" fill="#ffc078" fill-opacity="0.55"/>
  <rect x="97" y="290" width="35.5" height="0" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <rect x="134.5" y="267" width="35.5" height="23" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <rect x="172" y="244" width="35.5" height="46" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <rect x="209" y="221" width="35.5" height="69" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <rect x="246.5" y="198.5" width="35.5" height="91.5" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <rect x="284" y="175.5" width="35.5" height="114.5" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <rect x="321.5" y="152.5" width="35.5" height="137.5" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <rect x="358.5" y="129.5" width="35.5" height="160.5" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <polyline points="96,290 395,106.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,198.5 395,198.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="395,290 395,106.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="395" cy="106.5" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="208.5" y="239" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$W = \tfrac{1}{2} Q U$</span></div></foreignObject>
  <foreignObject x="233.5" y="81" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U = \tfrac{Q}{C}$</div></foreignObject>
</svg>

Kondensaattoriin varastoitunut energia on
```latex
W = \tfrac{1}{2} Q U = \tfrac{1}{2} C U^2
```
missä $W$ on energia ($\text{J}$), $Q$ varaus ($\text{C}$), $U$ jännite ($\text{V}$) ja $C$ kapasitanssi ($\text{F}$). Jälkimmäinen muoto saadaan sijoittamalla $Q = CU$. Energiaa merkitään $W$:llä, koska $E$ tarkoittaa tässä luvussa sähkökentän voimakkuutta. Myös luvussa *Akut ja latauspiiri* energia oli $W$, koska $E$ oli siellä lähdejännite.

Kun aluksi varaamaton kondensaattori ladataan vakiojännitelähteestä tavallisessa latauspiirissä, jossa on resistanssia, lähde siirtää koko varauksen $Q$ täyden jännitteensä $U$ yli, joten se antaa energian $QU$. Kondensaattoriin varastoituu siitä vain puolet. Toinen puoli muuttuu latauksen aikana johtimien ja vastusten sisäenergiaksi, joka siirtyy lämpönä ympäristöön. Puolet ei ole yleinen laki kaikille lataustavoille: se on tämän mallin tulos.

### Eriste, kun lähde on kytkettynä tai irrotettuna
Kun levyjen väliin työnnetään eristelevy, joka täyttää välin, kapasitanssi kasvaa $\varepsilon_\text{r}$-kertaiseksi. Muut suureet muuttuvat sen mukaan, pysyykö kondensaattori kytkettynä lähteeseen.

| | Lähde kytkettynä | Lähde irrotettuna |
|---|---|---|
| $U$ | sama | pienenee |
| $Q$ | kasvaa | sama |
| $W$ | kasvaa | pienenee |

Kun lähde on kytkettynä, jännite pysyy samana ja lähde tuo levyille lisää varausta, joten $Q = CU$ ja $W = \tfrac{1}{2} C U^2$ kasvavat. Irrotetun kondensaattorin varaus ei voi muuttua, joten jännite $U = \tfrac{Q}{C}$ ja energia $W = \tfrac{1}{2} Q U$ pienenevät: kenttä vetää eristelevyä levyjen väliin ja tekee työtä.

## Esimerkki
Kameran salamalaitteen kondensaattorin kapasitanssi on $150\,\mu\text{F}$, ja se ladataan jännitteeseen $300\,\text{V}$. Välähdyksessä kondensaattori purkautuu salamaputken läpi $1{,}0\,\text{ms}$:ssa. Kuinka paljon energiaa kondensaattoriin varastoituu, ja kuinka suuri on keskimääräinen teho välähdyksen aikana?

<!-- vaihe -->

**Tunnetut ja kysytty.** $C = 150\,\mu\text{F}$, $U = 300\,\text{V}$ ja purkautumisaika $t = 1{,}0\,\text{ms}$. Kysytään energiaa $W$ ja keskimääräistä tehoa $P$.

<!-- vaihe -->

**Periaate.** Kondensaattorin energia saadaan kapasitanssista ja jännitteestä. Välähdyksessä kondensaattori purkautuu, joten sama energia vapautuu purkautumisajan kuluessa, ja keskimääräinen teho on energia jaettuna ajalla.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&W = \tfrac{1}{2} C U^2 \\
&P = \frac{W}{t}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $C = 150\,\mu\text{F} = 150 \cdot 10^{-6}\,\text{F}$ ja $t = 1{,}0\,\text{ms} = 1{,}0 \cdot 10^{-3}\,\text{s}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&W = \tfrac{1}{2} C U^2 \\
&\phantom{W} = \tfrac{1}{2} \cdot 150 \cdot 10^{-6}\,\text{F} \cdot (300\,\text{V})^2 \\
&\phantom{W} = 6{,}75\,\text{J} \\
&P = \frac{W}{t} = \frac{6{,}75\,\text{J}}{1{,}0 \cdot 10^{-3}\,\text{s}} \\
&\phantom{P} = 6750\,\text{W}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kondensaattoriin varastoituu noin $6{,}8\,\text{J}$, ja keskimääräinen teho välähdyksen aikana on noin $6{,}8\,\text{kW}$, kaksi merkitsevää numeroa. Energia $W$ saadaan kapasitanssista ja jännitteestä, ja teho $P$ jakamalla se purkautumisajalla $1{,}0\,\text{ms}$.

<!-- vaihe -->

**Järkevyys.** Varaus on $Q = CU = 0{,}045\,\text{C}$, ja $\tfrac{1}{2} \cdot 0{,}045\,\text{C} \cdot 300\,\text{V} = 6{,}75\,\text{J}$, sama tulos. Jos paristot antavat lataukseen noin $2\,\text{W}$, lataus kestää vähintään $6{,}75\,\text{J} : 2\,\text{W} \approx 3{,}4\,\text{s}$, yli kolmetuhatta kertaa välähdystä kauemmin. Tämä vastaa alun kysymykseen.

## Yleinen virhekäsitys
Moni ajattelee, että ladattu kondensaattori on kokonaisuutena sähköisesti varattu, samaan tapaan kuin akku olisi täynnä varausta. Ladatun kondensaattorin levyillä on kuitenkin yhtä suuret vastakkaismerkkiset varaukset $+Q$ ja $-Q$, sillä latauksessa lähde vain siirtää varausta levystä toiseen. Kondensaattorin kokonaisvaraus on nolla, mutta siihen on varastoitunut energiaa levyjen väliseen sähkökenttään.

Toinen virhe on ajatella, että virta kulkee kondensaattorin läpi. Levyjen välissä on eriste, eikä varaus kulje sen läpi. Virta kulkee johtimissa vain latauksen ja purkautumisen aikana, kun varaus siirtyy levyille tai niiltä pois. Kolmas virhe on ajatella, että kapasitanssi kasvaa jännitteen kasvaessa. Suurempi jännite tuo suuremman varauksen, mutta niiden suhde $C$ riippuu vain kondensaattorin rakenteesta.

## Tiivistelmä
- Kondensaattorissa on kaksi johdelevyä, joiden välissä on eriste. Ladattaessa levyjen varaukset ovat $+Q$ ja $-Q$, ja levyjen välissä on homogeeninen kenttä $E = \tfrac{U}{d}$.
- Latauksessa ja purkautumisessa virta on suurin alussa ja pienenee vähitellen nollaan, ja kondensaattorin jännite muuttuu yhä hitaammin.
- Kapasitanssi on $C = \tfrac{Q}{U}$, yksikkö faradi. Levykondensaattorille $C = \tfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$: suuret levyt, pieni etäisyys ja eriste kasvattavat kapasitanssia.
- Kondensaattorin energia on $W = \tfrac{1}{2} Q U = \tfrac{1}{2} C U^2$, ja se on levyjen välisessä sähkökentässä.
- Eriste kestää kentän, joka on enintään sen läpilyöntilujuus $E_\text{max}$, joten suurin sallittu jännite on $U_\text{max} = E_\text{max} d$. Suuri kondensaattori voi olla vaarallinen myös irrotetussa laitteessa.
