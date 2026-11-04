# Lähdejännite ja sisäinen resistanssi

> **Miksi** auton ajovalot himmenevät hetkeksi, kun moottori käynnistetään kylmänä talviaamuna?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pimeä talviaamu. Lumisella pihalla seisoo punainen pikkuauto, jonka ajovalo loistaa hämärään ja jonka pakoputkesta nousee höyryä: autoa käynnistetään. Taustalla on lumikattoinen punainen talo, jonka ikkunoista näkyy valoa, ja tummia kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy68h-sky" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="470"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy68h-snow" gradientUnits="userSpaceOnUse" x1="0" y1="466" x2="0" y2="600"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#a5d8ff"/></linearGradient><linearGradient id="fy68h-beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy68h-sky)"/>
  <circle cx="323.5" cy="59.5" r="1.31259" fill="#ffffff"/>
  <circle cx="504" cy="10.5" r="2.56316" fill="#ffffff"/>
  <circle cx="356" cy="264" r="2.10589" fill="#ffffff"/>
  <circle cx="1084" cy="95" r="1.5396" fill="#ffffff"/>
  <circle cx="741.5" cy="192.5" r="2.00701" fill="#ffffff"/>
  <circle cx="1088" cy="40" r="2.3507" fill="#ffffff"/>
  <circle cx="825.5" cy="282" r="1.59986" fill="#ffffff"/>
  <circle cx="145" cy="94" r="1.22087" fill="#ffffff"/>
  <circle cx="1013.5" cy="273.5" r="1.48456" fill="#ffffff"/>
  <circle cx="70.5" cy="205" r="1.54777" fill="#ffffff"/>
  <circle cx="343.5" cy="27" r="1.95719" fill="#ffffff"/>
  <circle cx="889.5" cy="228.5" r="2.25566" fill="#ffffff"/>
  <circle cx="758.5" cy="224" r="2.08061" fill="#ffffff"/>
  <circle cx="160" cy="228.5" r="2.53257" fill="#ffffff"/>
  <circle cx="76" cy="126" r="1.21901" fill="#ffffff"/>
  <circle cx="249.5" cy="240.5" r="1.40673" fill="#ffffff"/>
  <circle cx="588.5" cy="296" r="1.88426" fill="#ffffff"/>
  <circle cx="529" cy="39" r="1.80578" fill="#ffffff"/>
  <circle cx="190.5" cy="263.5" r="1.34236" fill="#ffffff"/>
  <circle cx="31.5" cy="293" r="1.26996" fill="#ffffff"/>
  <circle cx="163.5" cy="203.5" r="1.56658" fill="#ffffff"/>
  <circle cx="746" cy="253" r="2.34763" fill="#ffffff"/>
  <circle cx="947" cy="17.5" r="1.35541" fill="#ffffff"/>
  <circle cx="232" cy="239" r="2.04706" fill="#ffffff"/>
  <circle cx="210" cy="235.5" r="1.34641" fill="#ffffff"/>
  <circle cx="117" cy="6" r="1.58904" fill="#ffffff"/>
  <circle cx="1191" cy="265.5" r="2.42965" fill="#ffffff"/>
  <circle cx="86.5" cy="36" r="2.45351" fill="#ffffff"/>
  <circle cx="962.5" cy="237" r="1.83443" fill="#ffffff"/>
  <circle cx="464" cy="7.5" r="2.10766" fill="#ffffff"/>
  <circle cx="903.5" cy="122" r="1.74726" fill="#ffffff"/>
  <circle cx="1006" cy="20" r="1.5979" fill="#ffffff"/>
  <circle cx="597.5" cy="193.5" r="1.86484" fill="#ffffff"/>
  <circle cx="185" cy="193" r="1.69682" fill="#ffffff"/>
  <circle cx="466" cy="81.5" r="1.38158" fill="#ffffff"/>
  <circle cx="831.5" cy="294" r="2.39472" fill="#ffffff"/>
  <circle cx="1118" cy="202.5" r="2.02523" fill="#ffffff"/>
  <circle cx="165.5" cy="222.5" r="2.27484" fill="#ffffff"/>
  <circle cx="807" cy="142.5" r="1.32552" fill="#ffffff"/>
  <circle cx="432" cy="89.5" r="1.66334" fill="#ffffff"/>
  <rect x="70" y="340" width="250" height="130" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="84" y1="343" x2="84" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="98" y1="343" x2="98" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="112" y1="343" x2="112" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="126" y1="343" x2="126" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="140" y1="343" x2="140" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="154" y1="343" x2="154" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="168" y1="343" x2="168" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="182" y1="343" x2="182" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="196" y1="343" x2="196" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="210" y1="343" x2="210" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="224" y1="343" x2="224" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="238" y1="343" x2="238" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="252" y1="343" x2="252" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="266" y1="343" x2="266" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="280" y1="343" x2="280" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="294" y1="343" x2="294" y2="467" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="70" y="340" width="10" height="130" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="310" y="340" width="10" height="130" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M50,340 L195,268.5 L340,340 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M50,340 L195,268.5 L340,340 l-8,8 L195,283 L58,348 Z" fill="#a5d8ff" stroke-linejoin="round"/>
  <rect x="100" y="376.5" width="40" height="52" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="100" y="376.5" width="40" height="52" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="120" y1="376.5" x2="120" y2="428.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="170" y="376.5" width="40" height="52" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="170" y="376.5" width="40" height="52" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="190" y1="376.5" x2="190" y2="428.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="240" y="376.5" width="40" height="52" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="240" y="376.5" width="40" height="52" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="260" y1="376.5" x2="260" y2="428.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="100" y="376.5" width="40" height="52" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="170" y="376.5" width="40" height="52" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="240" y="376.5" width="40" height="52" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="921" y="448.5" width="18.5" height="27.5" fill="#b8622d"/>
  <path d="M847,453 L930,361 L1013,453 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M930,361 L1013,453 H930 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M865.5,402.5 L930,310.5 L994.5,402.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M930,310.5 L994.5,402.5 H930 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M884,352 L930,246 L976,352 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M930,246 L976,352 H930 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1009" y="442.5" width="22.5" height="33.5" fill="#b8622d"/>
  <path d="M919,448 L1020,336 L1121,448 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1020,336 L1121,448 H1020 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M941.5,386.5 L1020,274.5 L1098.5,386.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1020,274.5 L1098.5,386.5 H1020 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M964,325 L1020,196 L1076,325 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1020,196 L1076,325 H1020 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1101.5" y="451" width="17" height="25" fill="#b8622d"/>
  <path d="M1034.5,455 L1110,371 L1185.5,455 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1110,371 L1185.5,455 H1110 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1051,409 L1110,325 L1169,409 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1110,325 L1169,409 H1110 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1068,362.5 L1110,266 L1152,362.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1110,266 L1152,362.5 H1110 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1170" y="446" width="20" height="30" fill="#b8622d"/>
  <path d="M1090,451 L1180,351 L1270,451 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1180,351 L1270,451 H1180 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1110,396 L1180,296 L1250,396 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1180,296 L1250,396 H1180 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1130,341 L1180,226 L1230,341 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1180,226 L1230,341 H1180 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="0" y="466" width="1200" height="134" fill="url(#fy68h-snow)"/>
  <path d="M0,520 Q300,500 600,516 T1200,512" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>
  <circle cx="358" cy="462" r="13" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="332" cy="442" r="19" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="300" cy="420" r="25" fill="#ffffff" fill-opacity="0.55"/>
  <circle cx="262" cy="398" r="31" fill="#ffffff" fill-opacity="0.55"/>
  <rect x="358" y="460" width="22" height="8" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M824,412 L1172,368 L1172,488 L824,428 Z" fill="url(#fy68h-beam)" fill-opacity="0.55"/>
  <path d="M372,468 L372,418 Q374,398 398,394 L464,388 L516,332 Q524,322 540,322 L672,322 Q692,322 704,334 L754,386 L802,394 Q826,398 828,420 L828,468 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M482,384 L524,336 L596,336 L596,384 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M608,336 L670,336 Q682,336 690,346 L724,384 L608,384 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M522,322 Q602,304 692,322 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="602" y1="390" x2="602" y2="456" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="568" y="402" width="22" height="6" rx="3" fill="#1f2933"/>
  <rect x="818" y="406" width="12" height="18" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="368" y="410" width="10" height="16" rx="3" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="468" cy="484" r="46" fill="#1f2933"/>
  <circle cx="468" cy="484" r="20" fill="#c4ccd4" stroke="#8a96a3" stroke-width="3"/>
  <circle cx="734" cy="484" r="46" fill="#1f2933"/>
  <circle cx="734" cy="484" r="20" fill="#c4ccd4" stroke="#8a96a3" stroke-width="3"/>
</svg>

## Ydinajatus

### Paristo on lähde ja vastus yhdessä
Paristossa kemialliset reaktiot erottavat varauksia toisistaan ja ylläpitävät napojen välillä jännitettä. Pariston **lähdejännite** $E$ kertoo, kuinka paljon energiaa paristo antaa jokaiselle sen läpi kulkevalle varausyksikölle: lähdejännite $1{,}5\,\text{V}$ tarkoittaa energiaa $1{,}5\,\text{J}$ jokaista coulombia kohti. Virta kulkee kuitenkin myös pariston sisällä elektrolyytin ja elektrodien läpi, ja niilläkin on resistanssia. Tätä sanotaan pariston **sisäiseksi resistanssiksi** $R_\text{s}$. Paristoa voi siksi kuvata mallilla, jossa ideaalinen jännitelähde $E$ on sarjassa vastuksen $R_\text{s}$ kanssa. Luvussa *Kirchhoffin lait ja potentiaali virtapiirissä* lähde oli ideaalinen; nyt sen oma resistanssi otetaan huomioon.

<svg data-fig="model" viewBox="0 0 600 344" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa: pariston malli. Katkoviivalla rajatun pariston sisällä on ideaalinen jännitelähde, jonka lähdejännite on E, ja sen kanssa sarjassa sisäinen resistanssi Rs. Pariston plusnapa on oikealla ylhäällä ja miinusnapa oikealla alhaalla. Navoista johtimet kulkevat ulkoiseen kuormitusvastukseen R. Napojen väliin on kytketty jännitemittari, joka mittaa napajännitteen U. Violetit nuolet näyttävät virran I: ulkoisessa piirissä plusnavalta kuorman kautta miinusnavalle ja pariston sisällä miinusnavalta plusnavalle." style="max-width:100%;font-size:24px">
  <rect x="30" y="58" width="192" height="256" rx="12" fill="#eef5f9" stroke="#6b7480" stroke-width="2" stroke-dasharray="8 6"/>
  <foreignObject x="71" y="17.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paristo}$</div></foreignObject>
  <polyline points="222,88 106,88 106,134" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="82" y1="134" x2="130" y2="134" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="94" y1="148" x2="118" y2="148" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <polyline points="106,148 106,196" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="94" y="196" width="24" height="60" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="106,256 106,284 222,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="62" y="113.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="62" y="141.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="140" y="126.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="128" y="211.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <path d="M106,168 L98,188 L114,188 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="120" y="163.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <polyline points="222,88 530,88 530,284 222,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="222" cy="88" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="222" cy="284" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="234" y="51.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="234" y="291.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <rect x="518" y="156" width="24" height="60" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="552" y="171.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <circle cx="352" cy="88" r="6" fill="#1f2933"/>
  <circle cx="352" cy="284" r="6" fill="#1f2933"/>
  <polyline points="352,88 352,166" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="352,206 352,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="352" cy="186" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="337" y="171.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="382" y="171.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$U$</div></foreignObject>
  <path d="M298,88 L278,80 L278,96 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="276" y="49.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <path d="M458,88 L438,80 L438,96 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M438,284 L458,276 L458,292 Z" fill="#7048e8" stroke-linejoin="round"/>
</svg>

### Napajännite pienenee, kun virta kasvaa
Pariston napojen välistä jännitettä sanotaan **napajännitteeksi** $U$. Kun paristosta otetaan virta $I$, potentiaali nousee ideaalisessa lähteessä lähdejännitteen $E$ verran, mutta se laskee sisäisessä resistanssissa jännitteen $R_\text{s} I$ verran kuten missä tahansa vastuksessa. Plusnavan potentiaali miinusnapaan nähden on siksi $E - R_\text{s} I$. Energian kannalta jokaisesta coulombista, jolle lähde antaa energian $E$:n verran, osa $R_\text{s} I$ muuttuu pariston omaksi sisäenergiaksi, ja vain loput $U$ siirtyy ulkoiseen piiriin. Siksi paristo lämpenee, kun siitä otetaan suuri virta.

<svg data-fig="potential" viewBox="0 0 600 360" role="img" aria-label="Potentiaalikuvaaja, kaavamainen: potentiaali V, kun kierretään silmukka pariston miinusnavasta pariston sisäosien ja ulkoisen kuormitusvastuksen R kautta takaisin miinusnapaan. Miinusnavalla potentiaali on nolla. Ideaalisessa lähteessä se nousee lähdejännitteen E verran, ja pariston sisäisessä resistanssissa Rs se laskee jännitteen Rs kertaa I verran. Plusnavalla potentiaali on siksi napajännite U, joka on pienempi kuin E. Kuormitusvastuksessa potentiaali laskee U:n verran takaisin nollaan." style="max-width:100%;font-size:24px">
  <line x1="95" y1="280" x2="490" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,280 L489,286 L489,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="281" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="508" y="265.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kohta}$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V$</div></foreignObject>
  <rect x="139.5" y="64" width="21.5" height="216" fill="#eef5f9"/>
  <foreignObject x="128.5" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <rect x="204.5" y="64" width="54.5" height="216" fill="#eef5f9"/>
  <foreignObject x="209.5" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <rect x="367.5" y="64" width="54.5" height="216" fill="#eef5f9"/>
  <foreignObject x="372.5" y="65.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="64" y="259.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="96" y1="100" x2="150.5" y2="100" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="148" x2="259" y2="148" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="54" y="85.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="54" y="133.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$U$</div></foreignObject>
  <polyline points="96,280 150.5,280 150.5,100 204.5,100 259,148 313,148 367.5,148 421.5,280 476,280" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M266,100 H273 V148 H266" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="283" y="109.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s} I$</div></foreignObject>
  <line x1="96" y1="280" x2="96" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="84" y="289.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <circle cx="96" cy="280" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="313" y1="280" x2="313" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="301" y="289.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <circle cx="313" cy="148" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="476" y1="280" x2="476" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="464" y="289.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <circle cx="476" cy="280" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <path d="M96,322 V330 H313 V322" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="149.5" y="331.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{paristo}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/lithium-ion-cells.webp" alt="Kaksi vaaleansinistä sylinterimäistä akkukennoa keltaisissa pidikkeissä puupöydällä; kyljissä tekstit INR21700 ja INR18650."><figcaption>Litiumioniakkukennot 21700 ja 18650. Numerot kertovat kennon mitat: halkaisija $21\,\text{mm}$ ja pituus $70\,\text{mm}$ tai $18\,\text{mm}$ ja $65\,\text{mm}$. Kennon sisäinen resistanssi on vain kymmeniä milliohmeja, joten se voi antaa suuren virran ilman, että napajännite laskee paljon.</figcaption></figure>

### Lähdejännite mitataan ilman virtaa
Kun paristosta ei oteta virtaa, sisäisen resistanssin jännite $R_\text{s} I$ on nolla, ja napajännite on yhtä suuri kuin lähdejännite. Lähdejännitteen voi siis mitata kytkemällä pariston napoihin pelkän jännitemittarin, sillä hyvä jännitemittari ottaa vain häviävän pienen virran. Uudesta AA-paristosta saadaan näin noin $1{,}6\,\text{V}$. Käytetyn pariston lähdejännite voi olla lähes yhtä suuri, mutta sen sisäinen resistanssi on kasvanut moninkertaiseksi. Pelkkä jännitemittari ei siksi paljasta, onko paristo vielä käyttökelpoinen: vasta kuormitettuna sen napajännite laskee selvästi.

### Auton akku käynnistettäessä
Auton akun sisäinen resistanssi on hyvin pieni, vain sadasosaohmien luokkaa. Käynnistysmoottori ottaa kuitenkin hetken aikaa satojen ampeerien virran, joten akun sisäisen resistanssin jännite $R_\text{s} I$ on voltteja, ja napajännite laskee selvästi. Ajovalot on kytketty samoihin napoihin, joten niiden jännite ja teho pienenevät samaksi hetkeksi, ja ne himmenevät. Kylmässä akun kemialliset reaktiot hidastuvat ja sisäinen resistanssi kasvaa, joten ilmiö on pakkasella voimakkaampi.

### Oikosulku
**Oikosulussa** pariston navat yhdistetään johtimella, jonka resistanssi on lähes nolla. Silloin napajännite on lähes nolla, ja virtaa rajoittaa vain sisäinen resistanssi. Oikosulkuvirta on suurin virta, jonka paristosta voi saada: uudelle AA-paristolle se on noin $1{,}60\,\text{V} : 0{,}20\,\Omega = 8{,}0\,\text{A}$ ja auton akulle yli tuhat ampeeria. Lähteen koko teho muuttuu silloin pariston ja johtimen sisäenergiaksi. Johdin voi kuumeta hehkuvaksi, ja paristo voi vuotaa tai kuumeta vaarallisesti; litiumparisto voi jopa syttyä palamaan. Pariston napoja ei siksi saa yhdistää suoraan johtimella, eikä irtoparistoja pidetä taskussa avainten tai kolikoiden kanssa.

## Kaava: Napajännite ja oikosulkuvirta
Pariston napajännite, kun paristosta otetaan virta $I$, on
```latex
U = E - R_\text{s} I
```
missä $U$ on napajännite ($\text{V}$), $E$ lähdejännite ($\text{V}$), $R_\text{s}$ sisäinen resistanssi ($\Omega$) ja $I$ paristosta otettava virta ($\text{A}$). Malli olettaa, että $E$ ja $R_\text{s}$ pysyvät vakioina. Todellisella paristolla ne muuttuvat hieman virran, lämpötilan ja pariston käytön mukana.

Kun paristoon kytketään kuormitusvastus $R$, Kirchhoffin jännitelaki antaa silmukalle $E - R_\text{s} I - R I = 0$. Virta on siis
```latex
I = \frac{E}{R + R_\text{s}}
```
missä $R$ on ulkoisen piirin resistanssi ($\Omega$). Sisäinen resistanssi toimii kuin kuorman kanssa sarjaan kytketty lisävastus. Oikosulussa $R = 0$, ja virta on oikosulkuvirta
```latex
I_\text{k} = \frac{E}{R_\text{s}}
```
missä $I_\text{k}$ on oikosulkuvirta ($\text{A}$).

### Lähdejännite ja sisäinen resistanssi kuvaajasta
Napajännite pienenee tasaisesti virran kasvaessa, joten pariston $(I, U)$-kuvaaja on laskeva suora. Se leikkaa pystyakselin kohdassa $U = E$, koska ilman virtaa napajännite on lähdejännite, ja vaaka-akselin oikosulkuvirran $I_\text{k}$ kohdalla. Suoran kulmakerroin on $-R_\text{s}$, joten sisäinen resistanssi saadaan kulmakertoimen kolmiosta: $R_\text{s} = -\Delta U : \Delta I$. Kuvan paristolla napajännite pienenee $0{,}60\,\text{V}$, kun virta kasvaa $2{,}0\,\text{A}$, joten $R_\text{s} = 0{,}60\,\text{V} : 2{,}0\,\text{A} = 0{,}30\,\Omega$.

<svg data-fig="ui-graph" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: pariston napajännite U voltteina virran I funktiona ampeereina. Suora alkaa pystyakselilta lähdejännitteen kohdalta 1,50 V ja laskee tasaisesti, kunnes se leikkaa vaaka-akselin oikosulkuvirran kohdalla 5,0 A. Kulmakertoimen kolmiossa virta kasvaa 1,0 ampeerista 3,0 ampeeriin eli 2,0 A, ja napajännite pienenee samalla 0,60 V. Sisäinen resistanssi on 0,60 V jaettuna 2,0 A:lla eli 0,30 ohmia." style="max-width:100%;font-size:24px">
  <line x1="163.5" y1="290" x2="163.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="290" x2="230.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298" y1="290" x2="298" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="290" x2="365.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="290" x2="432.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="290" x2="500" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="252.5" x2="500" y2="252.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="215.5" x2="500" y2="215.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="178" x2="500" y2="178" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="140.5" x2="500" y2="140.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103.5" x2="500" y2="103.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="66" x2="500" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,40 L102,53 L90,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="163.5" y1="290" x2="163.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="230.5" y1="290" x2="230.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="298" y1="290" x2="298" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="288" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="365.5" y1="290" x2="365.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="355.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="432.5" y1="290" x2="432.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="422.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="500" y1="290" x2="500" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="490" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="252.5" x2="96" y2="252.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="238" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}3$</div></foreignObject>
  <line x1="89" y1="215.5" x2="96" y2="215.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="201" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}6$</div></foreignObject>
  <line x1="89" y1="178" x2="96" y2="178" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="163.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}9$</div></foreignObject>
  <line x1="89" y1="140.5" x2="96" y2="140.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="126" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}2$</div></foreignObject>
  <line x1="89" y1="103.5" x2="96" y2="103.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="89" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="89" y1="66" x2="96" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="51.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}8$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="86" y="9.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <line x1="163.5" y1="140.5" x2="298" y2="140.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="298" y1="140.5" x2="298" y2="215.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="205.5" y="106" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta I$</span></div></foreignObject>
  <foreignObject x="308" y="163.5" width="56" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta U$</span></div></foreignObject>
  <polyline points="96,103.5 432.5,290" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="96" cy="103.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432.5" cy="290" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="112" y="69" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$E$</div></foreignObject>
  <foreignObject x="436.5" y="253.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$I_\text{k}$</div></foreignObject>
</svg>

Sisäinen resistanssi määritetään kokeellisesti näin. Paristoon kytketään säädettävä kuormitusvastus, virtamittari sarjaan ja jännitemittari pariston napoihin. Napajännite ja virta mitataan usealla kuorman arvolla, pisteet piirretään $(I, U)$-koordinaatistoon ja niihin sovitetaan suora. Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen samalla suoralla mittausepävarmuuden vuoksi. Lähdejännite luetaan suoran ja pystyakselin leikkauskohdasta, ja sisäinen resistanssi lasketaan suoran kulmakertoimesta, joka luetaan suoralta kahdesta kaukana toisistaan olevasta pisteestä. Oikosulkuvirtaa ei mitata, koska oikosulku voisi vahingoittaa paristoa. Se lasketaan yhtälöstä $I_\text{k} = E : R_\text{s}$ tai saadaan jatkamalla suoraa vaaka-akselille. Jatkaminen mittausalueen ulkopuolelle olettaa, että sisäinen resistanssi pysyy samana myös suurilla virroilla.

### Paristojen sarja- ja rinnankytkentä
Kun paristot kytketään **sarjaan** niin, että kunkin plusnapa on kytketty seuraavan miinusnapaan, potentiaalin nousut summautuvat, ja kaikki sisäiset resistanssit ovat samassa silmukassa peräkkäin. Paristoryhmän lähdejännite ja sisäinen resistanssi ovat
```latex
\begin{aligned}
E &= E_1 + E_2 + \dots \\
R_\text{s} &= R_{\text{s}1} + R_{\text{s}2} + \dots
\end{aligned}
```
missä $E_1$, $E_2$, … ovat yksittäisten paristojen lähdejännitteet ($\text{V}$) ja $R_{\text{s}1}$, $R_{\text{s}2}$, … niiden sisäiset resistanssit ($\Omega$). Taskulampun kolme sarjaan kytkettyä paristoa antavat noin $4{,}5\,\text{V}$. Väärin päin asetettu paristo vähentää ryhmän lähdejännitettä omansa verran, mutta sen sisäinen resistanssi lisätään silti muihin.

Kun $n$ samanlaista paristoa kytketään **rinnan**, plusnavat yhteen ja miinusnavat yhteen, ryhmän lähdejännite on sama kuin yhden pariston. Sisäiset resistanssit ovat rinnakkaisia haaroja, joihin virta jakautuu tasan, joten ryhmän sisäinen resistanssi on
```latex
R_\text{s} = \frac{R_{\text{s}1}}{n}
```
missä $R_{\text{s}1}$ on yhden pariston sisäinen resistanssi ($\Omega$). Kaksi uutta AA-paristoa antaa sarjassa lähdejännitteen $3{,}20\,\text{V}$ ja sisäisen resistanssin $0{,}40\,\Omega$, rinnan taas $1{,}60\,\text{V}$ ja $0{,}10\,\Omega$. Rinnankytkentä ei siis nosta jännitettä, mutta se antaa suuremman virran pienemmällä napajännitteen laskulla. Rinnan kytketään vain samanlaisia ja yhtä täysiä paristoja: muuten suuremman lähdejännitteen paristo ajaa virtaa toisen läpi, ja molemmat lämpenevät turhaan.

<svg data-fig="connections" viewBox="0 0 600 360" role="img" aria-label="Kaksi kytkentäkaaviota vierekkäin, ei mittakaavassa. Kumpikin paristo on piirretty mallinaan: lähdejännite E ja sisäinen resistanssi Rs katkoviivan sisällä. Vasemmalla kaksi samanlaista paristoa on sarjassa päällekkäin, ylemmän miinusnapa alemman plusnapaan. Kokonaisuuden lähdejännite on 2E ja sisäinen resistanssi 2Rs. Oikealla kaksi samanlaista paristoa on rinnan vierekkäin, plusnavat yhdessä ja miinusnavat yhdessä. Kokonaisuuden lähdejännite on E ja sisäinen resistanssi puolet Rs:stä." style="max-width:100%;font-size:24px">
  <line x1="300" y1="20" x2="300" y2="340" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="75" y="13.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sarjaan}$</div></foreignObject>
  <circle cx="130" cy="62" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="130,69 130,76" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="90" y="76" width="80" height="100" rx="12" fill="#eef5f9" stroke="#6b7480" stroke-width="2" stroke-dasharray="8 6"/>
  <polyline points="130,76 130,99" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="106" y1="99" x2="154" y2="99" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="118" y1="113" x2="142" y2="113" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <polyline points="130,113 130,128" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="120" y="130" width="20" height="40" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="130,170 130,176" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="160" y="91.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="146" y="135.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <rect x="90" y="176" width="80" height="100" rx="12" fill="#eef5f9" stroke="#6b7480" stroke-width="2" stroke-dasharray="8 6"/>
  <polyline points="130,176 130,199" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="106" y1="199" x2="154" y2="199" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="118" y1="213" x2="142" y2="213" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <polyline points="130,213 130,228" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="120" y="230" width="20" height="40" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="130,270 130,276" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="160" y="191.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="146" y="235.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <polyline points="130,276 130,283" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="130" cy="290" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="86" y="47.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="86" y="275.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="65" y="313.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2E,\ 2R_\text{s}$</div></foreignObject>
  <foreignObject x="390" y="13.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rinnan}$</div></foreignObject>
  <circle cx="445" cy="62" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="445,69 445,96" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="445" cy="96" r="6" fill="#1f2933"/>
  <polyline points="380,126 380,96 510,96 510,126" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="340" y="126" width="80" height="100" rx="12" fill="#eef5f9" stroke="#6b7480" stroke-width="2" stroke-dasharray="8 6"/>
  <polyline points="380,126 380,149" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="356" y1="149" x2="404" y2="149" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="368" y1="163" x2="392" y2="163" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <polyline points="380,163 380,178" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="370" y="180" width="20" height="40" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="380,220 380,226" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="410" y="141.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="396" y="185.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <rect x="470" y="126" width="80" height="100" rx="12" fill="#eef5f9" stroke="#6b7480" stroke-width="2" stroke-dasharray="8 6"/>
  <polyline points="510,126 510,149" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="486" y1="149" x2="534" y2="149" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="498" y1="163" x2="522" y2="163" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <polyline points="510,163 510,178" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="500" y="180" width="20" height="40" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <polyline points="510,220 510,226" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="380,226 380,256 510,256 510,226" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="445" cy="256" r="6" fill="#1f2933"/>
  <polyline points="445,256 445,283" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="445" cy="290" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="401" y="47.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="401" y="275.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="380" y="313.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E,\ \tfrac{1}{2} R_\text{s}$</div></foreignObject>
</svg>

## Esimerkki
Uuden AA-pariston napoihin kytketään pelkkä jännitemittari, ja se näyttää $1{,}58\,\text{V}$. Kun paristoon kytketään lisäksi vastus $4{,}0\,\Omega$, jännitemittari näyttää $1{,}45\,\text{V}$. Kuinka suuri on pariston sisäinen resistanssi, ja kuinka suuri olisi sen oikosulkuvirta?

<!-- vaihe -->

**Tunnetut ja kysytty.** Ilman virtaa mitattu jännite $1{,}58\,\text{V}$, kuormitettuna mitattu napajännite $U = 1{,}45\,\text{V}$ ja kuormitusvastus $R = 4{,}0\,\Omega$. Kysytään sisäistä resistanssia $R_\text{s}$ ja oikosulkuvirtaa $I_\text{k}$.

<!-- vaihe -->

**Periaate.** Jännitemittari ottaa häviävän pienen virran, joten ilman kuormaa se näyttää lähdejännitteen: $E = 1{,}58\,\text{V}$. Kuormitettuna mittari näyttää napajännitteen, joka on samalla vastuksen jännite, joten Ohmin laki antaa virran. Napajännitteen yhtälöstä ratkaistaan sisäinen resistanssi ja siitä oikosulkuvirta.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&I = \frac{U}{R} \\
&U = E - R_\text{s} I \\
&R_\text{s} = \frac{E - U}{I} \\
&I_\text{k} = \frac{E}{R_\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki suureet ovat perusyksiköissä, ja $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
I &= \frac{U}{R} \\
&= \frac{1{,}45\,\text{V}}{4{,}0\,\Omega} = 0{,}3625\,\text{A} \\
R_\text{s} &= \frac{E - U}{I} \\
&= \frac{1{,}58\,\text{V} - 1{,}45\,\text{V}}{0{,}3625\,\text{A}} \\
&= 0{,}3586\,\Omega \\
I_\text{k} &= \frac{E}{R_\text{s}} \\
&= \frac{1{,}58\,\text{V}}{0{,}3586\,\Omega} = 4{,}406\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Sisäinen resistanssi on noin $0{,}36\,\Omega$ ja oikosulkuvirta noin $4{,}4\,\text{A}$. Tulokset ilmoitetaan kahdella merkitsevällä numerolla, koska jännitteiden erotus $0{,}13\,\text{V}$ ja vastus $4{,}0\,\Omega$ ovat kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Sijoitetaan tulos takaisin: $0{,}3586\,\Omega \cdot 0{,}3625\,\text{A} = 0{,}13\,\text{V}$, ja $1{,}58\,\text{V} - 0{,}13\,\text{V} = 1{,}45\,\text{V}$ on mitattu napajännite. Sisäinen resistanssi on paljon pienempi kuin kuorma $4{,}0\,\Omega$, joten napajännite jää vain vähän lähdejännitettä pienemmäksi. Oikosulkuvirta on muutamia ampeereja kuten AA-paristolla kuuluukin.

## Yleinen virhekäsitys
Moni ajattelee, että paristo antaa aina saman virran tai että paristossa on varastossa tietty määrä virtaa. Paristo pitää yllä lähes vakiona pysyvää lähdejännitettä, ja virran määrää koko piirin resistanssi: $I = E : (R + R_\text{s})$. Sama paristo antaa pienelle kuormitusvastukselle suuren virran ja suurelle pienen virran. Paristossa ei myöskään kulu virta vaan kemiallinen energia, jota lähde muuttaa sähköenergiaksi.

Toinen virhekäsitys on, että pariston jännite on aina siihen painettu $1{,}5\,\text{V}$. Merkintä kertoo vain likimäärin lähdejännitteen. Napajännite on sitä pienempi, mitä suurempi virta paristosta otetaan ja mitä suurempi pariston sisäinen resistanssi on. Kolmas virhe on luulla, että rinnankytkentä kaksinkertaistaa jännitteen: rinnan kytkettyjen samanlaisten paristojen lähdejännite on sama kuin yhden, vain sisäinen resistanssi pienenee.

## Tiivistelmä
- Paristoa kuvataan mallilla, jossa ideaalinen lähde, jonka lähdejännite on $E$, on sarjassa sisäisen resistanssin $R_\text{s}$ kanssa.
- Napajännite on $U = E - R_\text{s} I$: se pienenee virran kasvaessa. Ilman virtaa napajännite on lähdejännite.
- Kuormitusvastuksen kanssa virta on $I = E : (R + R_\text{s})$. Oikosulkuvirta $I_\text{k} = E : R_\text{s}$ on suurin mahdollinen virta, ja oikosulku on vaarallinen.
- Pariston $(I, U)$-kuvaaja on laskeva suora: se leikkaa pystyakselin lähdejännitteen kohdalla, ja sen kulmakerroin on $-R_\text{s}$.
- Sarjaan kytkettyjen paristojen lähdejännitteet ja sisäiset resistanssit summautuvat. Rinnan kytkettyjen samanlaisten paristojen lähdejännite on sama kuin yhden, ja sisäinen resistanssi on $R_{\text{s}1} : n$.
