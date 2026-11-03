# Muuntaja ja sähköenergian siirto

> **Miksi** sähkö kuljetetaan voimalaitokselta kaupunkiin $400\,\text{kV}$:n jännitteellä, vaikka kodin pistorasiassa jännite on vain $230\,\text{V}$?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: vasemmalla joen varrella voimalaitos ja sen muuntaja, josta lähtee pitkä voimajohto. Suuret ristikkopylväät kantavat johtimia peltojen ja metsän yli kohti oikealla kaukana näkyvää kaupunkia, jonka ikkunoissa palaa valo." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy78h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy78h-field" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><linearGradient id="fy78h-river" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy78h-sky)"/>
  <path d="M0,380 Q100,360 200,378.5 Q300,355.5 400,379.5 Q500,359 600,379 Q700,341 800,382.5 Q900,349.5 1000,380.5 Q1100,341 1200,382.5 Q1300,347.5 1400,381 V600 H0 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M0,407 Q100,386.5 200,405.5 Q300,373 400,409 Q500,376 600,407 Q700,391 800,404 Q900,393 1000,404.5 Q1100,389 1200,405.5 Q1300,380.5 1400,410 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <rect x="0" y="430" width="1200" height="170" fill="url(#fy78h-field)"/>
  <path d="M0,430 L10.5,401.5 L21.5,430 L37,385 L52.5,430 L66,392.5 L79,430 L88.5,406.5 L98,430 L108,404.5 L118,430 L129,400 L140,430 L157,380.5 L173.5,430 L186,395.5 L198.5,430 L207.5,407.5 L216.5,430 L229.5,394 L242.5,430 L256.5,391.5 L270,430 L284.5,387 L299.5,430 L313.5,390 L327.5,430 L337,407 L346,430 L358.5,396 L371,430 L382.5,398 L394.5,430 L405.5,401 L416.5,430 L429.5,394.5 L442,430 L453.5,398.5 L465.5,430 L481.5,383 L497.5,430 L513,385 L528.5,430 L541,395.5 L553.5,430 L570,381 L586.5,430 L599,395.5 L611.5,430 L626.5,386 L642,430 L654.5,395 L667,430 L684,380.5 L700.5,430 L712.5,396.5 L725,430 L738.5,392.5 L752,430 L765,392 L778.5,430 L789.5,401 L800.5,430 L813,396.5 L825,430 L842,380.5 L858.5,430 L867.5,407.5 L877,430 L892.5,384.5 L908,430 L922,390 L936.5,430 L951,387 L966,430 L977,400.5 L988.5,430 L1002,392 L1015.5,430 L1026,401.5 L1037,430 L1052.5,385 L1068,430 L1080.5,395 L1093,430 L1106.5,391.5 L1120.5,430 L1132,399 L1143.5,430 L1153.5,403.5 L1164,430 L1180,383.5 L1196,430 L1210,389 L1224.5,430 V442 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M0,520 C120,500 180,470 260,440 L300,440 C230,480 160,540 80,600 L0,600 Z" fill="url(#fy78h-river)" stroke-linejoin="round"/>
  <rect x="70" y="300" width="200" height="140" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <path d="M60,300 L170,250 L280,300 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="90" y="330" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="134" y="330" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="178" y="330" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="222" y="330" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="290" y="380" width="70" height="60" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="298" y="362" width="10" height="20" rx="3" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="318" y="362" width="10" height="20" rx="3" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="338" y="362" width="10" height="20" rx="3" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M422.5,440 L461.5,140 H478.5 L517.5,440" fill="none" stroke="#6c757d" stroke-width="4.2" stroke-linejoin="round"/>
  <line x1="422.5" y1="440" x2="510" y2="380" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="517.5" y1="440" x2="430" y2="380" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="502" y2="320" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="510" y1="380" x2="438" y2="320" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="438" y1="320" x2="494" y2="260" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="502" y1="320" x2="446" y2="260" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="446" y1="260" x2="486" y2="200" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="494" y1="260" x2="454" y2="200" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="397" y1="200" x2="543" y2="200" stroke="#6c757d" stroke-width="4.2" stroke-linecap="butt"/>
  <line x1="397" y1="200" x2="397" y2="219.5" stroke="#1f2933" stroke-width="2.8" stroke-linecap="butt"/>
  <line x1="543" y1="200" x2="543" y2="219.5" stroke="#1f2933" stroke-width="2.8" stroke-linecap="butt"/>
  <line x1="422.5" y1="140" x2="517.5" y2="140" stroke="#6c757d" stroke-width="4.2" stroke-linecap="butt"/>
  <line x1="422.5" y1="140" x2="422.5" y2="159.5" stroke="#1f2933" stroke-width="2.8" stroke-linecap="butt"/>
  <line x1="517.5" y1="140" x2="517.5" y2="159.5" stroke="#1f2933" stroke-width="2.8" stroke-linecap="butt"/>
  <path d="M686,430 L714,220 H726 L754,430" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <line x1="686" y1="430" x2="748.5" y2="388" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="754" y1="430" x2="691.5" y2="388" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="691.5" y1="388" x2="743" y2="346" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="748.5" y1="388" x2="697" y2="346" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="697" y1="346" x2="737" y2="304" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="743" y1="346" x2="703" y2="304" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="703" y1="304" x2="731.5" y2="262" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="737" y1="304" x2="708.5" y2="262" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="668" y1="262" x2="772" y2="262" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="668" y1="262" x2="668" y2="276" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="772" y1="262" x2="772" y2="276" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="686" y1="220" x2="754" y2="220" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="686" y1="220" x2="686" y2="234" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="754" y1="220" x2="754" y2="234" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M896,424 L916,284 H924 L944,424" fill="none" stroke="#6c757d" stroke-width="2.1" stroke-linejoin="round"/>
  <line x1="896" y1="424" x2="940" y2="396" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="944" y1="424" x2="900" y2="396" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="900" y1="396" x2="936" y2="368" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="940" y1="396" x2="904" y2="368" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="904" y1="368" x2="932" y2="340" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="936" y1="368" x2="908" y2="340" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="908" y1="340" x2="928" y2="312" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="932" y1="340" x2="912" y2="312" stroke="#6c757d" stroke-width="1.05" stroke-linecap="butt"/>
  <line x1="883.5" y1="312" x2="956.5" y2="312" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="883.5" y1="312" x2="883.5" y2="322" stroke="#1f2933" stroke-width="1.4" stroke-linecap="butt"/>
  <line x1="956.5" y1="312" x2="956.5" y2="322" stroke="#1f2933" stroke-width="1.4" stroke-linecap="butt"/>
  <line x1="896" y1="284" x2="944" y2="284" stroke="#6c757d" stroke-width="2.1" stroke-linecap="butt"/>
  <line x1="896" y1="284" x2="896" y2="294" stroke="#1f2933" stroke-width="1.4" stroke-linecap="butt"/>
  <line x1="944" y1="284" x2="944" y2="294" stroke="#1f2933" stroke-width="1.4" stroke-linecap="butt"/>
  <path d="M360,370 Q378.5,309 397,219.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M397,219.5 Q532.5,274 668,276" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M543,219.5 Q657.5,274 772,276" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M422.5,159.5 Q554,223 686,234" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M517.5,159.5 Q636,223 754,234" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M668,276 Q776,325 883.5,322" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M772,276 Q864,325 956.5,322" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M686,234 Q791,290 896,294" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M754,234 Q849,290 944,294" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="1010" y="374" width="60" height="50" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1022" y="386" width="14" height="14" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1046" y="386" width="14" height="14" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1080" y="354" width="50" height="70" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1092" y="366" width="14" height="14" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1106" y="366" width="14" height="14" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1135" y="380" width="50" height="44" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1147" y="392" width="14" height="14" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1161" y="392" width="14" height="14" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M883.5,322 Q947,371 1010,400" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
</svg>

## Ydinajatus

### Muuntaja muuttaa vaihtojännitettä
Muuntajassa on suljettu rautasydän ja sen ympärille kierretyt kaksi käämiä. **Ensiökäämiin** kytketään vaihtojännite, ja **toisiokäämistä** saadaan jännite laitteelle. Käämit eivät kosketa toisiaan, eikä niiden välillä kulje virtaa johtimia pitkin. Ensiökäämin vaihtovirta synnyttää rautasydämeen magneettikentän, jonka suuruus ja suunta vaihtelevat virran tahdissa. Rautasydän ohjaa lähes koko magneettivuon kiertämään sydäntä pitkin myös toisiokäämin läpi. Luvussa *Sähkömagneettinen induktio* nähtiin, että muuttuva magneettivuo indusoi käämiin jännitteen. Siksi toisiokäämiin syntyy vaihtojännite, jonka taajuus on sama kuin ensiöjännitteen.

<svg data-fig="transformer" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva muuntajasta, ei mittakaavassa. Suljetun rautasydämen vasempaan haaraan on kierretty ensiökäämi, jossa on enemmän kierroksia, ja oikeaan haaraan toisiokäämi, jossa on vähemmän kierroksia. Ensiökäämi on kytketty vaihtojännitelähteeseen, jonka jännite on U1, ja toisiokäämi lamppuun, jonka jännite on U2. Vihreä katkoviiva nuolineen kiertää rautasydämen sisällä: ensiövirran synnyttämä muuttuva magneettivuo kulkee sydäntä pitkin myös toisiokäämin läpi." style="max-width:100%;font-size:24px">
  <path d="M150,60 H450 V300 H150 Z M200,110 V250 H400 V110 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" fill-rule="evenodd"/>
  <path d="M160,70 H440 V290 H160 Z" fill="none" stroke="#8a96a3" stroke-width="1" stroke-linejoin="round"/>
  <path d="M170,80 H430 V280 H170 Z" fill="none" stroke="#8a96a3" stroke-width="1" stroke-linejoin="round"/>
  <path d="M180,90 H420 V270 H180 Z" fill="none" stroke="#8a96a3" stroke-width="1" stroke-linejoin="round"/>
  <path d="M190,100 H410 V260 H190 Z" fill="none" stroke="#8a96a3" stroke-width="1" stroke-linejoin="round"/>
  <path d="M175,85 H425 V275 H175 Z" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-dasharray="9 7"/>
  <path d="M309,85 L293,92 L293,78 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M425,189 L418,173 L432,173 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M291,275 L307,268 L307,282 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M175,171 L182,187 L168,187 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="290" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Phi$</div></foreignObject>
  <rect x="136" y="124" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="136" y="139" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="136" y="154" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="136" y="169" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="136" y="184" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="136" y="199" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="136" y="214" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="136" y="229" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="386" y="146" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="386" y="166" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="386" y="186" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="386" y="206" width="78" height="9" rx="4" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M136,128 H70 V156" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M136,233 H70 V204" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="70" cy="180" r="24" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M55.5,180 C63,163 70,163 70,180 C70,197 77,197 84.5,180" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="-6" y="165.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_1$</div></foreignObject>
  <path d="M464,150 H545 V162" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M464,213 H545 V200" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="545" cy="181" r="19" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="533" y1="169" x2="557" y2="193" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="557" y1="169" x2="533" y2="193" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="528.5" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_2$</div></foreignObject>
  <line x1="112" y1="120" x2="94" y2="120" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,120 L95,115 L95,125 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="81.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <line x1="488" y1="142" x2="510" y2="142" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M520,142 L509,147 L509,137 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="487.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="222" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N_1$</div></foreignObject>
  <foreignObject x="345" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$N_2$</div></foreignObject>
  <foreignObject x="83.5" y="317.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ensiökäämi}$</div></foreignObject>
  <foreignObject x="233.5" y="317.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rautasydän}$</div></foreignObject>
  <foreignObject x="377.5" y="317.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{toisiokäämi}$</div></foreignObject>
</svg>

### Kierrosten lukumäärä määrää jännitteen
Sama muuttuva magneettivuo kulkee kummankin käämin jokaisen kierroksen läpi, joten jokaiseen kierrokseen indusoituu yhtä suuri jännite. Käämin jännite on sen kierrosten jännitteiden summa, joten se on verrannollinen kierrosten lukumäärään. Ideaalisessa muuntajassa ensiö- ja toisiojännitteen suhde on siis sama kuin käämien kierrosten lukumäärien suhde, **muuntosuhde**. Kun toisiokäämissä on enemmän kierroksia kuin ensiökäämissä, muuntaja nostaa jännitettä. Kun toisiokäämissä on vähemmän kierroksia, muuntaja laskee jännitettä.

### Muuntaja toimii vain vaihtovirralla
Jos ensiökäämi kytketään akkuun, käämissä kulkee tasavirta, ja rautasydämen magneettikenttä on vakio. Vakiosuuruinen magneettivuo ei indusoi jännitettä, joten toisiokäämin jännite on nolla. Jännitepulssi syntyy vain hetkellä, jolloin virta kytketään tai katkaistaan, koska silloin vuo muuttuu. Tämän vuoksi sähköverkossa käytetään vaihtovirtaa: luvussa *Generaattori ja vaihtovirta* generaattori tuottaa vaihtojännitettä, ja muuntajilla sen suuruus voidaan muuttaa kulloinkin sopivaksi.

### Teho säilyy, virta muuttuu
Ideaalinen muuntaja ei kuluta energiaa, joten ensiökäämiin tuleva teho on yhtä suuri kuin toisiokäämistä lähtevä teho. Teho on jännitteen ja virran tulo, joten kun muuntaja nostaa jännitteen kymmenkertaiseksi, virta pienenee kymmenesosaan. Muuntaja ei siis lisää energiaa tai tehoa: se vaihtaa suuren virran suureksi jännitteeksi tai päinvastoin. Todellisessa muuntajassa osa energiasta muuttuu sisäenergiaksi käämien resistanssissa ja rautasydämen pyörrevirroissa. Siksi sydän kootaan ohuista toisistaan eristetyistä levyistä (luku *Lenzin laki ja pyörrevirrat*). Suurten voimalaitosmuuntajien hyötysuhde on yli $99\,\%$.

### Siirtohäviö ja suurjännite
Voimajohdolla on resistanssi, ja johdossa kulkeva virta lämmittää sitä. Lämmöksi muuttuva teho on verrannollinen virran neliöön, joten virta kannattaa pitää pienenä. Saman tehon voi siirtää suurella jännitteellä ja pienellä virralla. Kun jännite nostetaan kymmenkertaiseksi, virta pienenee kymmenesosaan ja häviöteho sadasosaan. Siksi voimalaitoksen generaattorin jännite nostetaan muuntajalla **suurjännitteeksi**. Fingridin ylläpitämän Suomen kantaverkon jännitteet ovat $400\,\text{kV}$, $220\,\text{kV}$ ja $110\,\text{kV}$. Kantaverkon häviöt vastaavat noin $2\,\%$:a Suomessa käytetystä sähköstä (Fingrid, *Yhteisillä linjoilla* 2026, vuoden 2025 tiedot).

<svg data-fig="grid" viewBox="0 0 640 372" role="img" aria-label="Kaavakuva sähköverkosta, ei mittakaavassa. Ylärivillä voimalaitoksen generaattorin jännite 20 kV nostetaan muuntajalla 400 kilovoltiksi, ja kantaverkon suuret pylväät vievät sähkön sähköasemalle. Sähköasemalla muuntaja laskee jännitteen, ja alarivillä jakeluverkon pienet pylväät vievät 20 kV:n jännitteen muuntamolle, joka laskee sen kotien 230 voltiksi." style="max-width:100%;font-size:24px">
  <rect x="60" y="66" width="14" height="40" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="16" y="106" width="64" height="64" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M11,106 H85 L68,90 H28 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="48" cy="140" r="16" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="48" cy="140" r="5" fill="#1f2933"/>
  <line x1="80" y1="150" x2="152" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="160" cy="150" r="15" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="176" cy="150" r="15" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="89" y="103.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <path d="M250,170 L266,70 H274 L290,170" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <line x1="240" y1="80" x2="300" y2="80" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="260" y1="120" x2="280" y2="140" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="120" x2="260" y2="140" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M360,170 L376,70 H384 L400,170" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <line x1="350" y1="80" x2="410" y2="80" stroke="#6c757d" stroke-width="3" stroke-linecap="butt"/>
  <line x1="370" y1="120" x2="390" y2="140" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="390" y1="120" x2="370" y2="140" stroke="#6c757d" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M186,150 Q228,96 270,84 Q325,104 380,84 Q430,100 470,132" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="275" y="29.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400\,\text{kV}$</div></foreignObject>
  <foreignObject x="252.5" y="181.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kantaverkko}$</div></foreignObject>
  <circle cx="480" cy="150" r="15" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="496" cy="150" r="15" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="460" y="120" width="56" height="56" rx="4" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-dasharray="5 4"/>
  <foreignObject x="496" y="183.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sähköasema}$</div></foreignObject>
  <path d="M488,176 V300 H420" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="396" y="282" width="8" height="46" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <line x1="382" y1="286" x2="418" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="296" y="282" width="8" height="46" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <line x1="282" y1="286" x2="318" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M420,300 Q410,300 400,286 Q350,302 300,286 Q262,292 232,300" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="307" y="239.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="271" y="335.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jakeluverkko}$</div></foreignObject>
  <rect x="196" y="278" width="36" height="46" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="208.5" cy="300" r="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="219.5" cy="300" r="10" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="196" y1="300" x2="150" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="160" y="233.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{muuntamo}$</div></foreignObject>
  <rect x="66" y="272" width="84" height="62" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <path d="M52,272 L108,233.5 L164,272 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="78" y="289.5" width="22" height="18.5" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="114.5" y="297" width="20" height="37" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="51" y="197.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$230\,\text{V}$</div></foreignObject>
</svg>

### Jännite lasketaan vaiheittain
Sähköasemilla muuntajat laskevat jännitteen alueverkon $110\,\text{kV}$:iin ja jakeluverkon $20\,\text{kV}$:iin, ja asuinalueen muuntamo laskee sen kotien $230\,\text{V}$:iin. Suurjännitettä ei tuoda koteihin, koska sen eristäminen vaatii pitkiä eristimiä ja suuria etäisyyksiä, ja kosketus olisi hengenvaarallinen (luku *Sähköturvallisuus*). Puhelimen laturi laskee jännitteen vielä noin $5\,\text{V}$:iin. Nykyaikainen laturi muuttaa verkkojännitteen ensin hyvin suuritaajuiseksi, jolloin muuntaja voi olla pieni, ja tasasuuntaa sen lopuksi. Laturin muuntajan käämit eivät kosketa toisiaan, joten puhelin ei ole johtavassa yhteydessä sähköverkkoon.

## Kaava: Muuntaja ja siirtohäviö
Ideaalisen muuntajan jännitteet ja virrat riippuvat käämien kierrosten lukumääristä:
```latex
\frac{U_1}{U_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}
```
missä $U_1$ on ensiöjännite (V), $U_2$ toisiojännite (V), $N_1$ ja $N_2$ ensiö- ja toisiokäämin kierrosten lukumäärät ja $I_1$ ja $I_2$ ensiö- ja toisiovirta (A). Suhde $N_1 : N_2$ on muuntosuhde. Jälkimmäinen yhtäsuuruus seuraa tehon säilymisestä: $U_1 I_1 = U_2 I_2$. Jännitteet ja virrat ovat tehollisia arvoja (luku *Generaattori ja vaihtovirta*). Kun jännite kasvaa, virta pienenee samassa suhteessa.

### Siirtojohdon tehohäviö
Voimalaitos lähettää tehon $P$ jännitteellä $U$. Johdon virta ja johdossa lämmöksi muuttuva teho ovat
```latex
\begin{aligned}
&P = U I \\[6pt]
&P_\text{h} = R I^2 = \frac{R P^2}{U^2}
\end{aligned}
```
missä $P$ on siirrettävä teho (W), $U$ siirtojännite (V), $I$ johdon virta (A), $R$ johtimien resistanssi (Ω) ja $P_\text{h}$ häviöteho (W). Kun sama teho siirretään kaksinkertaisella jännitteellä, virta puolittuu ja häviöteho pienenee neljäsosaan. Siirtojännite $U$ ei ole johdon resistanssin yli oleva jännite: johdon päiden välinen jännitehäviö on vain $R I$, joten häviötehoa ei saa laskea lausekkeella $U^2 : R$.

<svg data-fig="loss-graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: siirtojohdossa lämmöksi muuttuvan tehon osuus siirretystä tehosta prosentteina siirtojännitteen funktiona kilovoltteina, kun siirretty teho on 200 MW ja johdon resistanssi 6,0 ohmia. Käyrä laskee jyrkästi: 100 kV:lla osuus on 12 %, 200 kV:lla 3,0 % ja 400 kV:lla 0,75 %. Kun jännite kaksinkertaistuu, osuus pienenee neljäsosaan." style="max-width:100%;font-size:24px">
  <line x1="143" y1="290" x2="143" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="189.5" y1="290" x2="189.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="290" x2="236" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="290" x2="283" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="290" x2="330" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376.5" y1="290" x2="376.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="423" y1="290" x2="423" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="244" x2="470" y2="244" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="198" x2="470" y2="198" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="152" x2="470" y2="152" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="106" x2="470" y2="106" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="143" y1="290" x2="143" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="189.5" y1="290" x2="189.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="167" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="236" y1="290" x2="236" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283" y1="290" x2="283" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="260.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="330" y1="290" x2="330" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="376.5" y1="290" x2="376.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="354" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="423" y1="290" x2="423" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="244" x2="96" y2="244" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="229.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="198" x2="96" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="183.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="152" x2="96" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="106" x2="96" y2="106" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{kV})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{h} : P\ (\%)$</div></foreignObject>
  <polyline points="161.5,64.5 164,81.5 166.5,96.5 169,109.5 171.5,121.5 174.5,132.5 177,142.5 179.5,151.5 182,159.5 184.5,167 187,174 189.5,180 192.5,186 195,191.5 197.5,196 200,201 202.5,205 205,209 207.5,212.5 210.5,216 213,219.5 215.5,222.5 218,225 220.5,228 223,230.5 225.5,232.5 228.5,235 231,237 233.5,239 236,241 238.5,242.5 241,244 243.5,246 246.5,247.5 249,248.5 251.5,250 254,251.5 256.5,252.5 259,253.5 261.5,255 264.5,256 267,257 269.5,258 272,259 274.5,259.5 277,260.5 279.5,261.5 282.5,262 285,263 287.5,263.5 290,264.5 292.5,265 295,265.5 297.5,266.5 300.5,267 303,267.5 305.5,268 308,268.5 310.5,269 313,269.5 315.5,270 318.5,270.5 321,271 323.5,271.5 326,272 328.5,272 331,272.5 333.5,273 336.5,273.5 339,273.5 341.5,274 344,274.5 346.5,274.5 349,275 351.5,275 354.5,275.5 357,276 359.5,276 362,276.5 364.5,276.5 367,277 369.5,277 372.5,277.5 375,277.5 377.5,278 380,278 382.5,278 385,278.5 387.5,278.5 390.5,279 393,279 395.5,279 398,279.5 400.5,279.5 403,280 405.5,280 408.5,280 411,280.5 413.5,280.5 416,280.5 418.5,280.5 421,281 423.5,281 426.5,281 429,281.5 431.5,281.5 434,281.5 436.5,281.5 439,282 441.5,282 444.5,282 447,282 449.5,282.5 452,282.5 454.5,282.5 457,282.5 459.5,282.5 462.5,283 465,283 467.5,283 470,283" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="189.5" y1="179.5" x2="189.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="179.5" x2="189.5" y2="179.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="189.5" cy="179.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="283" y1="262.5" x2="283" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="262.5" x2="283" y2="262.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="283" cy="262.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="470" y1="283" x2="470" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="283" x2="470" y2="283" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="470" cy="283" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="203.5" y="165" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$12\,\%$</span></div></foreignObject>
  <foreignObject x="289" y="222" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$3{,}0\,\%$</span></div></foreignObject>
  <foreignObject x="383" y="242.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0{,}75\,\%$</span></div></foreignObject>
  <foreignObject x="300" y="77.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P = 200\,\text{MW}$</div></foreignObject>
  <foreignObject x="320" y="115.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R = 6{,}0\,\Omega$</div></foreignObject>
</svg>

## Esimerkki
Sähköaseman muuntaja laskee alueverkon jännitteen $110\,\text{kV}$ jakeluverkon jännitteeksi $20\,\text{kV}$. Toisiokäämissä on $360$ kierrosta, ja jakeluverkkoon lähtevä virta on $450\,\text{A}$. Kuinka monta kierrosta ensiökäämissä on, ja kuinka suuri virta ensiökäämissä kulkee? Muuntaja oletetaan ideaaliseksi.

<!-- vaihe -->

**Tunnetut ja kysytty.** Ensiöjännite $U_1 = 110\,\text{kV}$, toisiojännite $U_2 = 20\,\text{kV}$, toisiokäämin kierrosten lukumäärä $N_2 = 360$ ja toisiovirta $I_2 = 450\,\text{A}$. Kysytään ensiökäämin kierrosten lukumäärää $N_1$ ja ensiövirtaa $I_1$.

<!-- vaihe -->

**Periaate.** Ideaalisessa muuntajassa sama muuttuva magneettivuo kulkee kummankin käämin läpi, joten jännitteet suhtautuvat kuten kierrosten lukumäärät. Muuntaja ei kuluta energiaa, joten teho säilyy, $U_1 I_1 = U_2 I_2$, ja virrat suhtautuvat kääntäen kuten jännitteet.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\frac{U_1}{U_2} = \frac{N_1}{N_2} \;\Rightarrow\; N_1 = \frac{N_2 U_1}{U_2} \\[6pt]
&\frac{U_1}{U_2} = \frac{I_2}{I_1} \;\Rightarrow\; I_1 = \frac{I_2 U_2}{U_1}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: jännitteet ovat kummassakin kaavassa osamääränä, joten kilovoltit supistuvat. Kumpikin jännite on samassa yksikössä, $\text{kV}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&N_1 = \frac{N_2 U_1}{U_2} \\
&= \frac{360 \cdot 110\,\text{kV}}{20\,\text{kV}} \\
&= 1980 \\[6pt]
&I_1 = \frac{I_2 U_2}{U_1} \\
&= \frac{450\,\text{A} \cdot 20\,\text{kV}}{110\,\text{kV}} \\
&= 81{,}82\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ensiökäämissä on $1980$ kierrosta, ja ensiövirta on $I_1 \approx 82\,\text{A}$. Virta ilmoitetaan kahdella merkitsevällä numerolla, kuten jännite $20\,\text{kV}$.

<!-- vaihe -->

**Järkevyys.** Muuntaja laskee jännitettä, joten ensiökäämissä on oltava enemmän kierroksia ja pienempi virta kuin toisiokäämissä, kuten tuloksessa. Teho säilyy: $110\,\text{kV} \cdot 81{,}82\,\text{A} = 9{,}0\,\text{MW}$ ja $20\,\text{kV} \cdot 450\,\text{A} = 9{,}0\,\text{MW}$.

## Yleinen virhekäsitys
Moni laskee voimajohdon häviötehon lausekkeella $P = U^2 : R$ ja päättelee, että suurempi jännite lisää häviöitä. Lausekkeessa $U$ on kuitenkin vastuksen yli oleva jännite. Siirtojännite on johtimien ja maan tai johtimien keskinäinen jännite, ja johdon resistanssin yli on vain pieni jännitehäviö $R I$. Oikea tapa on laskea ensin virta $I = P : U$ ja sitten häviöteho $P_\text{h} = R I^2$: suurempi jännite pienentää virtaa ja häviöitä. Toinen virhe on ajatella, että jännitettä nostava muuntaja lisää tehoa. Ideaalisessa muuntajassa teho säilyy, joten jännitteen kasvaessa virta pienenee. Kolmas virhe on olettaa, että muuntaja toimii myös akulla. Se tarvitsee muuttuvan magneettivuon, eli vaihtovirran.

## Tiivistelmä
- Muuntajassa ensiökäämin vaihtovirta synnyttää rautasydämeen muuttuvan magneettivuon, joka indusoi toisiokäämiin vaihtojännitteen. Tasavirralla vuo ei muutu, eikä muuntaja toimi.
- Ideaalisessa muuntajassa $U_1 : U_2 = N_1 : N_2 = I_2 : I_1$. Teho säilyy, joten jännitteen kasvaessa virta pienenee.
- Siirtojohdon häviöteho on $P_\text{h} = R I^2$, missä $I = P : U$. Kaksinkertainen siirtojännite pienentää häviöt neljäsosaan.
- Sähkö siirretään pitkiä matkoja suurjännitteellä: Suomen kantaverkon jännitteet ovat $400\,\text{kV}$, $220\,\text{kV}$ ja $110\,\text{kV}$, ja muuntajat laskevat jännitteen vaiheittain kotien $230\,\text{V}$:iin.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: seinäpistorasiaan on kytketty pieni puhelimen laturi, ja sen johto vie pöydällä olevaan puhelimeen, joka latautuu." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy78s-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy78s-screen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#1971c2"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="#f6f1e6"/>
  <rect x="0" y="270" width="600" height="90" fill="url(#fy78s-desk)"/>
  <rect x="120" y="60" width="120" height="120" rx="14" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="180" cy="120" r="42" fill="#e3dccb" stroke="#1f2933" stroke-width="2"/>
  <rect x="150" y="100" width="60" height="64" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="166" y="116" width="28" height="8" rx="3" fill="#6c757d"/>
  <path d="M180,164 C180,240 300,200 330,290" fill="none" stroke="#1f2933" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="300" y="286" width="150" height="54" rx="10" fill="#1f2933"/>
  <rect x="310" y="292" width="130" height="42" rx="4" fill="url(#fy78s-screen)"/>
  <rect x="360" y="304" width="30" height="18" rx="2" fill="none" stroke="#ffffff" stroke-width="2"/>
  <rect x="364" y="308" width="16" height="10" rx="1" fill="#2b8a3e"/>
</svg>
