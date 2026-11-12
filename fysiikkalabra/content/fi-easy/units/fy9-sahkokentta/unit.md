# Sähkökenttä ja kondensaattori

> **Miksi** ovenkahvasta pakkaspäivänä lyövä kipinä ei vahingoita, vaikka sen jännite on tuhansia voltteja?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvi-ilta eteisessä. Keskellä on puinen ulko-ovi. Ovessa on messinkinen kahva pitkässä metallilevyssä. Oikealta käsi kurottaa kohti kahvaa. Kädessä on punainen neulehiha. Sormenpään ja metallilevyn välissä välähtää pieni kirkas kipinä. Lattialla on raidallinen villamatto. Vasemmalla on ikkuna. Ikkunasta näkyy luminen yö, kuu ja kuusia. Ikkunan alla on patteri. Seinän naulakossa roikkuu villapipo." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9sk-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4e7cf"/><stop offset="1" stop-color="#ead6b2"/></linearGradient><linearGradient id="fy9sk-floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c99a68"/><stop offset="1" stop-color="#a9784a"/></linearGradient><linearGradient id="fy9sk-night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d3557"/><stop offset="1" stop-color="#4f6d93"/></linearGradient><linearGradient id="fy9sk-door" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9a6440"/><stop offset="1" stop-color="#7a4a2c"/></linearGradient><linearGradient id="fy9sk-brass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f1d58f"/><stop offset="1" stop-color="#c9a046"/></linearGradient><linearGradient id="fy9sk-lever" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4dc9c"/><stop offset="1" stop-color="#c9a046"/></linearGradient><linearGradient id="fy9sk-sleeve" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d64545"/><stop offset="1" stop-color="#a61e1e"/></linearGradient><radialGradient id="fy9sk-glow"><stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/><stop offset="0.35" stop-color="#d0e6fb" stop-opacity="0.75"/><stop offset="1" stop-color="#d0e6fb" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy9sk-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy9sk-floor)"/>
  <line x1="0" y1="504" x2="1200" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="538" x2="1200" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="572" x2="1200" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="470" x2="60" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="504" x2="250" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="538" x2="360" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="550" y1="470" x2="550" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="504" x2="660" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="850" y1="538" x2="850" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="960" y1="470" x2="960" y2="504" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1150" y1="504" x2="1150" y2="538" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1260" y1="538" x2="1260" y2="572" stroke="#8f6238" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="0" y="462" width="1200" height="10" fill="#e7d3ae" stroke="#1f2933" stroke-width="2"/>
  <rect x="70" y="80" width="260" height="250" rx="4" fill="url(#fy9sk-night)" stroke="#1f2933" stroke-width="4"/>
  <circle cx="270" cy="132" r="22" fill="#fff4d6"/>
  <circle cx="280" cy="126" r="20" fill="#3b5a82"/>
  <circle cx="95" cy="134" r="3.16043" fill="#ffffff"/>
  <circle cx="118.5" cy="126" r="2.99475" fill="#ffffff"/>
  <circle cx="108.5" cy="93" r="2.44434" fill="#ffffff"/>
  <circle cx="273" cy="123.5" r="3.07418" fill="#ffffff"/>
  <circle cx="129" cy="209.5" r="2.44092" fill="#ffffff"/>
  <circle cx="126.5" cy="241" r="2.11153" fill="#ffffff"/>
  <circle cx="242.5" cy="209.5" r="2.6959" fill="#ffffff"/>
  <circle cx="302" cy="260" r="2.46306" fill="#ffffff"/>
  <circle cx="240.5" cy="253.5" r="2.34635" fill="#ffffff"/>
  <circle cx="312" cy="173" r="1.66264" fill="#ffffff"/>
  <circle cx="287.5" cy="198.5" r="3.04026" fill="#ffffff"/>
  <circle cx="206.5" cy="243.5" r="3.10226" fill="#ffffff"/>
  <circle cx="299.5" cy="93" r="2.58907" fill="#ffffff"/>
  <circle cx="206" cy="120" r="2.8447" fill="#ffffff"/>
  <circle cx="157.5" cy="157" r="2.59527" fill="#ffffff"/>
  <circle cx="243.5" cy="181" r="2.83611" fill="#ffffff"/>
  <circle cx="209.5" cy="130" r="2.91189" fill="#ffffff"/>
  <circle cx="192" cy="249.5" r="2.10826" fill="#ffffff"/>
  <circle cx="91" cy="230" r="1.8787" fill="#ffffff"/>
  <circle cx="294.5" cy="257.5" r="3.10957" fill="#ffffff"/>
  <circle cx="303.5" cy="234.5" r="3.18535" fill="#ffffff"/>
  <circle cx="228" cy="130" r="2.64288" fill="#ffffff"/>
  <circle cx="265.5" cy="132.5" r="3.092" fill="#ffffff"/>
  <circle cx="229" cy="196.5" r="2.53966" fill="#ffffff"/>
  <circle cx="264.5" cy="132.5" r="2.67846" fill="#ffffff"/>
  <circle cx="275.5" cy="253" r="2.62559" fill="#ffffff"/>
  <path d="M83,300 L110,210 L137,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M126,300 L162,180 L198,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M196,300 L220,220 L244,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M251,300 L284,190 L317,300 Z" fill="#203a2b" stroke-linejoin="round"/>
  <path d="M70,290 Q160,266 230,284 T330,280 V330 H70 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="200" y1="80" x2="200" y2="330" stroke="#f4efe6" stroke-width="6" stroke-linecap="butt"/>
  <line x1="70" y1="185" x2="330" y2="185" stroke="#f4efe6" stroke-width="6" stroke-linecap="butt"/>
  <rect x="70" y="80" width="260" height="250" rx="4" fill="none" stroke="#1f2933" stroke-width="4"/>
  <rect x="54" y="330" width="292" height="16" rx="3" fill="#f4efe6" stroke="#1f2933" stroke-width="3"/>
  <rect x="96" y="368" width="208" height="82" rx="6" fill="#f8f9fa" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="117" y1="376" x2="117" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="137.5" y1="376" x2="137.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="158.5" y1="376" x2="158.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="179" y1="376" x2="179" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="200" y1="376" x2="200" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="221" y1="376" x2="221" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="241.5" y1="376" x2="241.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="262.5" y1="376" x2="262.5" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283" y1="376" x2="283" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="126" y1="450" x2="126" y2="462" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <line x1="274" y1="450" x2="274" y2="462" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
  <rect x="392" y="112" width="120" height="12" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="2"/>
  <line x1="452" y1="124" x2="452" y2="150" stroke="#6c757d" stroke-width="4" stroke-linecap="round"/>
  <path d="M404,214 Q404,146 452,142 Q500,146 500,214 Z" fill="#2f74b5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="412" y1="164" x2="412" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="432" y1="164" x2="432" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="452" y1="164" x2="452" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="472" y1="164" x2="472" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <line x1="492" y1="164" x2="492" y2="208" stroke="#a9d1f0" stroke-width="3" stroke-linecap="butt"/>
  <rect x="398" y="206" width="108" height="20" rx="6" fill="#a9d1f0" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="452" cy="136" r="12" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="546" y="38" width="298" height="424" fill="#e2cfa8" stroke="#1f2933" stroke-width="3"/>
  <rect x="560" y="52" width="270" height="410" fill="url(#fy9sk-door)" stroke="#1f2933" stroke-width="3"/>
  <rect x="590" y="82" width="210" height="150" rx="4" fill="none" stroke="#5e3720" stroke-width="3"/>
  <rect x="596" y="88" width="198" height="138" rx="3" fill="none" stroke="#b07b52" stroke-width="2"/>
  <rect x="590" y="266" width="210" height="166" rx="4" fill="none" stroke="#5e3720" stroke-width="3"/>
  <rect x="596" y="272" width="198" height="154" rx="3" fill="none" stroke="#b07b52" stroke-width="2"/>
  <rect x="554" y="92" width="10" height="40" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="554" y="392" width="10" height="40" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="771" y="232" width="26" height="150" rx="6" fill="url(#fy9sk-brass)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="784" cy="272" r="11" fill="#e8c66e" stroke="#1f2933" stroke-width="2"/>
  <path d="M784,265 L702,267 Q688,272 700,279 L784,279 Z" fill="url(#fy9sk-lever)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="784" cy="344" r="5.5" fill="#1f2933"/>
  <path d="M781,346 L779,360 L789,360 L787,346 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M1200,244 L1010,256 Q984,276 990,312 Q996,350 1016,360 L1200,376 Z" fill="url(#fy9sk-sleeve)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1040,262 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1040,352 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1068,261 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1068,353 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1096,260 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1096,354 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1124,259 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1124,355 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1152,258 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1152,356 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1180,257 l8,12 l8,-12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1180,357 l8,-12 l8,12" fill="none" stroke="#f6d2c4" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1004,264 Q996,300 1010,352" fill="none" stroke="#f6d2c4" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M996,272 Q960,266 930,284 L825,297 Q817,303 825,310 L928,312 Q920,330 936,338 Q964,352 998,344 Z" fill="#f1c9a5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M944,318 Q930,322 944,326" fill="none" stroke="#d9a47c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M948,327 Q933,331 948,335" fill="none" stroke="#d9a47c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M952,336 Q936,340 952,344" fill="none" stroke="#d9a47c" stroke-width="2" stroke-linejoin="round"/>
  <path d="M829,300 q4,3 0,7" fill="none" stroke="#d9a47c" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="808" cy="304" r="36" fill="url(#fy9sk-glow)"/>
  <path d="M819,304 L812,297 L808,309 L803,300 L797,306" fill="none" stroke="#1971c2" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.55"/>
  <path d="M819,304 L812,297 L808,309 L803,300 L797,306" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="825" y1="290" x2="832.5" y2="283.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="830" y1="304" x2="840" y2="304" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="825" y1="318" x2="832.5" y2="324.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="791" y1="318" x2="783.5" y2="324.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="786" y1="304" x2="776" y2="304" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="791" y1="290" x2="783.5" y2="283.5" stroke="#ffe8a3" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M620,488 L1010,488 L1080,560 L560,560 Z" fill="#c9d6c0" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M613.5,496 L1018,496 L1024.5,502.5 L608,502.5 Z" fill="#7a9e7e" stroke-linejoin="round"/>
  <path d="M602,509.5 L1030.5,509.5 L1037,516 L596.5,516 Z" fill="#e9c98a" stroke-linejoin="round"/>
  <path d="M591,522.5 L1043.5,522.5 L1050,529.5 L585.5,529.5 Z" fill="#7a9e7e" stroke-linejoin="round"/>
  <path d="M580,536 L1056.5,536 L1063,542.5 L574.5,542.5 Z" fill="#c95f4a" stroke-linejoin="round"/>
  <path d="M569,549.5 L1069.5,549.5 L1076,556 L563.5,556 Z" fill="#7a9e7e" stroke-linejoin="round"/>
  <path d="M620,488 L1010,488 L1080,560 L560,560 Z" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="566" y1="560" x2="564" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="592" y1="560" x2="590" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="618" y1="560" x2="616" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="644" y1="560" x2="642" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="670" y1="560" x2="668" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="696" y1="560" x2="694" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="722" y1="560" x2="720" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="748" y1="560" x2="746" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="774" y1="560" x2="772" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="800" y1="560" x2="798" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="826" y1="560" x2="824" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="852" y1="560" x2="850" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="878" y1="560" x2="876" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="904" y1="560" x2="902" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="930" y1="560" x2="928" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="956" y1="560" x2="954" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="982" y1="560" x2="980" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="1008" y1="560" x2="1006" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="1034" y1="560" x2="1032" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
  <line x1="1060" y1="560" x2="1058" y2="572" stroke="#c9d6c0" stroke-width="3" stroke-linecap="round"/>
</svg>

## Ydinajatus

Kaikki tunnin tehtävät alkavat samasta ajatuksesta: **varaus synnyttää ympärilleen sähkökentän, ja kenttä kohdistaa toiseen varaukseen voiman** $\overline{F} = q\overline{E}$. Kohdistaa tarkoittaa, että voima vaikuttaa varaukseen. Positiiviseen varaukseen voima osoittaa kentän suuntaan. Negatiiviseen varaukseen voima osoittaa kenttää vastaan. Kun kenttä siirtää varausta, kenttä tekee työtä. Silloin varauksen potentiaalienergia muuttuu samalla tavalla kuin pallon korkeusenergia muuttuu painovoimakentässä. Kondensaattori varastoi energiaa levyjensä väliseen kenttään. Puolijohdekomponentit ja sähköturvallisuus liittyvät samoihin suureisiin: jännitteeseen, virtaan ja kenttään, jonka eriste kestää.

<svg data-fig="kartta" viewBox="0 0 380 780" role="img" aria-label="Käsitekartta. Ylhäällä on solmu: varaus synnyttää sähkökentän, ja kenttä kohdistaa varaukseen voiman F = q E. Siitä lähtee alas neljä haaraa. Ensimmäinen haara on varaus ja voima: varaus Q = n e, Coulombin laki F = k kertaa varausten tulon itseisarvo jaettuna r toiseen, ja voimien vektorisumma. Toinen haara on kenttä ja potentiaali: homogeeninen kenttä E = U jaettuna d:llä, kentän työ W = q U ja kiihdytys puoli m v toiseen = varaus kertaa U. Kolmas haara on kondensaattori: kapasitanssi C = Q jaettuna U:lla, levykondensaattori C = epsilon nolla epsilon r A jaettuna d:llä ja energia W = puoli C U toiseen. Neljäs haara on komponentit ja turvallisuus: etuvastus R = U miinus U D jaettuna I:llä, aurinkokennon hyötysuhde eta = P jaettuna G A:lla ja kehon läpi kulkeva virta I = U jaettuna R:llä." style="max-width:100%;font-size:22px">
  <line x1="24" y1="80" x2="24" y2="638" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/>
  <foreignObject x="66" y="17" width="248" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\text{varaus synnyttää kentän}$</div></foreignObject>
  <foreignObject x="151.5" y="46" width="77" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\overline{F} = q\overline{E}$</div></foreignObject>
  <line x1="24" y1="122" x2="44" y2="122" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="100" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="109" width="168" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{varaus ja voima}$</div></foreignObject>
  <line x1="54" y1="142" x2="362" y2="142" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="153" width="54" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$Q = ne$</div></foreignObject>
  <foreignObject x="248" y="156" width="114" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{alkeisvaraus}$</div></foreignObject>
  <foreignObject x="58" y="190" width="157" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$F = k\,|q_1 q_2|/r^2$</div></foreignObject>
  <foreignObject x="292" y="193" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{Coulomb}$</div></foreignObject>
  <foreignObject x="58" y="227" width="122" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\overline{F} = \overline{F}_1 + \overline{F}_2$</div></foreignObject>
  <foreignObject x="310" y="230" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{summa}$</div></foreignObject>
  <line x1="24" y1="294" x2="44" y2="294" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="272" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="281" width="237" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{kenttä ja potentiaali}$</div></foreignObject>
  <line x1="54" y1="314" x2="362" y2="314" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="325" width="65" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$E = U/d$</div></foreignObject>
  <foreignObject x="248" y="328" width="114" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{homogeeninen}$</div></foreignObject>
  <foreignObject x="58" y="362" width="54" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$W = qU$</div></foreignObject>
  <foreignObject x="274" y="365" width="88" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{kentän työ}$</div></foreignObject>
  <foreignObject x="58" y="399" width="134" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\tfrac12 mv^2 = |q|U$</div></foreignObject>
  <foreignObject x="274" y="402" width="88" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{kiihdytys}$</div></foreignObject>
  <line x1="24" y1="466" x2="44" y2="466" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="444" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="453" width="180" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{kondensaattori}$</div></foreignObject>
  <line x1="54" y1="486" x2="362" y2="486" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="497" width="65" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$C = Q/U$</div></foreignObject>
  <foreignObject x="248" y="500" width="114" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{kapasitanssi}$</div></foreignObject>
  <foreignObject x="58" y="534" width="111" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$C = \varepsilon_0\varepsilon_\text{r}A/d$</div></foreignObject>
  <foreignObject x="310" y="537" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{levyt}$</div></foreignObject>
  <foreignObject x="58" y="571" width="100" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$W = \tfrac12 CU^2$</div></foreignObject>
  <foreignObject x="292" y="574" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{energia}$</div></foreignObject>
  <line x1="24" y1="638" x2="44" y2="638" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="44" y="616" width="328" height="156" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="58" y="625" width="305" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\textbf{komponentit ja turvallisuus}$</div></foreignObject>
  <line x1="54" y1="658" x2="362" y2="658" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="58" y="669" width="122" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$R = (U - U_\text{D})/I$</div></foreignObject>
  <foreignObject x="274" y="672" width="88" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{etuvastus}$</div></foreignObject>
  <foreignObject x="58" y="706" width="100" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$\eta = P/(GA)$</div></foreignObject>
  <foreignObject x="310" y="709" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{kenno}$</div></foreignObject>
  <foreignObject x="58" y="743" width="65" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$I = U/R$</div></foreignObject>
  <foreignObject x="266" y="746" width="96" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:17px;color:#6b7480">$\text{kehon virta}$</div></foreignObject>
</svg>

Alun kipinä selittyy näillä laeilla. Kun kävelet villamatolla, kehoosi kertyy varausta. Influenssin vuoksi kahvan metallilevyn lähimpään pintaan siirtyy varaus, jonka merkki on vastakkainen. Influenssi tarkoittaa, että varattu kappale siirtää johteen varauksia, vaikka kappaleet eivät kosketa. Kipinä hyppää, kun ilmavälin kenttä on suurempi kuin ilman läpilyöntilujuus. Se on noin $3\,\text{MV/m}$. Noin $3\,\text{mm}$:n kipinä kertoo siis, että jännite on noin $9\,\text{kV}$.

Jännite on suuri. Keho on kuitenkin pieni kondensaattori, jonka kapasitanssi on noin $100\,\text{pF}$. Siksi varausta on vain noin $0{,}9\,\mu\text{C}$ ja energiaa noin $4\,\text{mJ}$. Purkaus kestää noin mikrosekunnin. Vaarallinen virta on noin $50\,\text{mA}$ sekunnin ajan. Se kuljettaisi kehon läpi $0{,}05\,\text{C}$. Se on yli $50\,000$ kertaa enemmän varausta.

<svg data-fig="kipina" viewBox="0 0 600 540" role="img" aria-label="Kaavakuva, ei mittakaavassa. Vasemmalla on sormenpää. Sen pinnalla on negatiivisia varauksia. Oikealla on oven kahvan metallilevy. Influenssin vuoksi levyn siihen pintaan, joka on sormen puolella, on siirtynyt positiivisia varauksia. Sormen ja levyn välissä on noin 3 millimetrin ilmaväli. Sen poikki kulkee vihreitä kenttäviivoja levystä sormeen ja kirkas sinivalkoinen kipinä. Kenttä on noin 3 MV/m. Se on ilman läpilyöntilujuus. Alla on laskelma: jännite U = E max kertaa d on noin 9 kV. Keho on kondensaattori, jonka kapasitanssi on noin 100 pF. Siksi varaus Q = C U on noin 0,9 mikrocoulombia ja energia W = puoli C U toiseen noin 4 millijoulea." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9sk-plate" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e8c66e"/><stop offset="1" stop-color="#c9a046"/></linearGradient><radialGradient id="fy9sk-kglow"><stop offset="0" stop-color="#ffffff" stop-opacity="0.9"/><stop offset="0.5" stop-color="#d0e6fb" stop-opacity="0.6"/><stop offset="1" stop-color="#d0e6fb" stop-opacity="0"/></radialGradient></defs>
  <path d="M10,70 L190,70 Q262,70 262,140 Q262,210 190,210 L10,210 Z" fill="#f1c9a5" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M150,100 Q200,94 222,118" fill="none" stroke="#d9a47c" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="420" y="40" width="170" height="200" rx="6" fill="url(#fy9sk-plate)" stroke="#1f2933" stroke-width="3"/>
  <circle cx="214" cy="92.5" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="208" y1="92.5" x2="220" y2="92.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="230" cy="114" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="224" y1="114" x2="236" y2="114" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="236" cy="140" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="230" y1="140" x2="242" y2="140" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="230" cy="166" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="224" y1="166" x2="236" y2="166" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="214" cy="187.5" r="12" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="208" y1="187.5" x2="220" y2="187.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="68" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="68" x2="446" y2="68" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="62" x2="440" y2="74" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="104" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="104" x2="446" y2="104" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="98" x2="440" y2="110" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="140" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="140" x2="446" y2="140" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="134" x2="440" y2="146" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="176" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="176" x2="446" y2="176" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="170" x2="440" y2="182" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="440" cy="212" r="12" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="434" y1="212" x2="446" y2="212" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="440" y1="206" x2="440" y2="218" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="418" y1="80" x2="284" y2="80" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M272,80 L285,74 L285,86 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="110" x2="280" y2="110" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M268,110 L281,104 L281,116 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="140" x2="280" y2="140" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M268,140 L281,134 L281,146 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="170" x2="280" y2="170" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M268,170 L281,164 L281,176 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="418" y1="200" x2="284" y2="200" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M272,200 L285,194 L285,206 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="322" y="29" width="40" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <path d="M251,155 Q341,139 431,155 Q341,171 251,155 Z" fill="url(#fy9sk-kglow)" stroke-linejoin="round"/>
  <path d="M264,155 L292,149 L312,161 L338,149 L362,161 L388,150 L416,155" fill="none" stroke="#1971c2" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M264,155 L292,149 L312,161 L338,149 L362,161 L388,150 L416,155" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="262" y1="250" x2="420" y2="250" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="262" y1="238" x2="262" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="238" x2="420" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="261" width="160" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$d \approx 3\,\text{mm}$</div></foreignObject>
  <foreignObject x="69.5" y="223" width="81" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{sormi}$</div></foreignObject>
  <foreignObject x="464.5" y="253" width="81" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{kahva}$</div></foreignObject>
  <line x1="10" y1="302" x2="590" y2="302" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="14" y="319.5" width="432" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$U = E_\text{max}d \approx 3\,\text{MV/m} \cdot 3\,\text{mm} \approx 9\,\text{kV}$</div></foreignObject>
  <foreignObject x="14" y="381.5" width="397" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$Q = CU \approx 100\,\text{pF} \cdot 9\,\text{kV} \approx 0{,}9\,\mu\text{C}$</div></foreignObject>
  <foreignObject x="14" y="443" width="238" height="82" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$W = \dfrac12 CU^2 \approx 4\,\text{mJ}$</div></foreignObject>
</svg>

## Kaava: Sähkökenttä ja kondensaattori

### Varaus, voima ja kenttä

```kaavat
varaus alkeisvarauksen monikertana :: Q = ne
Coulombin voiman suuruus :: F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2}
sähkökentän voimakkuus :: \overline{F} = q\overline{E}
jännite homogeenisessa sähkökentässä :: E = \frac{U}{d}
```

missä $n$ on alkeisvarausten lukumäärä, $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ alkeisvaraus, $F$ voima ($\text{N}$), $q_1$ ja $q_2$ varaukset ($\text{C}$), $r$ niiden etäisyys ($\text{m}$), $k = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2}$, $\overline{E}$ sähkökentän voimakkuus ($\text{N/C} = \text{V/m}$), $U$ levyjen välinen jännite ($\text{V}$) ja $d$ levyjen etäisyys ($\text{m}$). Varaus säilyy eli sen kokonaismäärä ei muutu. Coulombin laki pätee pistevarauksille ja palloille, joissa varaus on jakautunut tasaisesti. Kun varauksia on monta, niiden voimat lasketaan yhteen vektoreina. Kenttä $E = \tfrac{U}{d}$ pätee vain laajojen yhdensuuntaisten levyjen välissä. Siellä kenttä on homogeeninen eli samanlainen joka kohdassa.

<svg data-fig="levyt" viewBox="0 0 600 440" role="img" aria-label="Kaavakuva: kaksi vaakasuoraa levyä. Ylempi levy on positiivinen, ja sen potentiaali on 200 V. Alempi levy on negatiivinen, ja se on nollakohta 0 V. Levyjen välissä on viisi vihreää pystysuoraa kenttäviivaa. Ne osoittavat alas. Kenttä on homogeeninen. Harmaat katkoviivat ovat tasapotentiaalipintoja 150 V, 100 V ja 50 V. Vasemmalla on protoni. Sen punainen voimanuoli osoittaa alas kentän suuntaan. Oikealla on elektroni. Sen punainen voimanuoli osoittaa ylös kenttää vastaan, kohti suurempaa potentiaalia." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9sk-pl1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dfe4ea"/><stop offset="1" stop-color="#aeb8c2"/></linearGradient><linearGradient id="fy9sk-pl2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dfe4ea"/><stop offset="1" stop-color="#aeb8c2"/></linearGradient></defs>
  <rect x="120" y="52" width="440" height="18" rx="3" fill="url(#fy9sk-pl1)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="120" y="350" width="440" height="18" rx="3" fill="url(#fy9sk-pl2)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="154" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="61" x2="158" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="154" y1="57" x2="154" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="154" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="359" x2="158" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="216" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="212" y1="61" x2="220" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="216" y1="57" x2="216" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="216" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="212" y1="359" x2="220" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="278" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="274" y1="61" x2="282" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="278" y1="57" x2="278" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="278" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="274" y1="359" x2="282" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="340" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="336" y1="61" x2="344" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="340" y1="57" x2="340" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="340" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="336" y1="359" x2="344" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="402" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="398" y1="61" x2="406" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="402" y1="57" x2="402" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="402" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="398" y1="359" x2="406" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="464" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="460" y1="61" x2="468" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="464" y1="57" x2="464" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="464" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="460" y1="359" x2="468" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="526" cy="61" r="8" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="522" y1="61" x2="530" y2="61" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="526" y1="57" x2="526" y2="65" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="526" cy="359" r="8" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="522" y1="359" x2="530" y2="359" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="120" y1="140" x2="560" y2="140" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="34" y="124.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$150\,\text{V}$</div></foreignObject>
  <line x1="120" y1="210" x2="560" y2="210" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="34" y="194.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$100\,\text{V}$</div></foreignObject>
  <line x1="120" y1="280" x2="560" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="48" y="264.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$50\,\text{V}$</div></foreignObject>
  <foreignObject x="34" y="45.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$200\,\text{V}$</div></foreignObject>
  <foreignObject x="61" y="343.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0\,\text{V}$</div></foreignObject>
  <line x1="170" y1="76" x2="170" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M170,344 L164.5,332 L175.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="255" y1="76" x2="255" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M255,344 L249.5,332 L260.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="340" y1="76" x2="340" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M340,344 L334.5,332 L345.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="425" y1="76" x2="425" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M425,344 L419.5,332 L430.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="510" y1="76" x2="510" y2="333" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M510,344 L504.5,332 L515.5,332 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="524" y="285.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <circle cx="212" cy="220" r="15" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <line x1="204.5" y1="220" x2="219.5" y2="220" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="212" y1="212.5" x2="212" y2="227.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="212" y1="237" x2="212" y2="297" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M212,312 L205,296 L219,296 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="230" y="245.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = e\overline{E}$</span></div></foreignObject>
  <circle cx="468" cy="200" r="15" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="460.5" y1="200" x2="475.5" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="468" y1="183" x2="468" y2="123" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M468,108 L475,124 L461,124 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="486" y="157.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = -e\overline{E}$</span></div></foreignObject>
  <foreignObject x="164.5" y="391.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{protoni}$</div></foreignObject>
  <foreignObject x="408" y="391.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{elektroni}$</div></foreignObject>
</svg>

### Potentiaali ja energia

```kaavat
sähkökentän potentiaali :: E_\text{p} = qV
sähkökentän tekemä työ :: W_{AB} = qU_{AB}
sähkökentässä kiihdytetyn hiukkasen liike-energia :: \tfrac12 mv^2 = \lvert q \rvert U
```

missä $V$ on kohdan potentiaali ($\text{V}$) valittuun nollakohtaan nähden, $U_{AB} = V_A - V_B$ ja $W_{AB}$ kentän tekemä työ ($\text{J}$). Työ ei riipu reitistä. Kenttä osoittaa suuremmasta potentiaalista pienempään. Levosta lähtevä varaus liikkuu siihen suuntaan, jossa sen potentiaalienergia pienenee. Viimeinen yhtälö pätee hiukkaselle, joka lähtee levosta, kun vain sähköinen voima tekee työtä. Energian yksikkö on myös $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

### Kondensaattori

```kaavat
kondensaattorilaki :: C = \frac{Q}{U}
levykondensaattorin kapasitanssi :: C = \frac{\varepsilon_0\varepsilon_\text{r}A}{d}
kondensaattorin energia :: W = \tfrac12 QU = \tfrac12 CU^2
läpilyöntijännite :: U_\text{max} = E_\text{max}d
```

missä $C$ on kapasitanssi ($\text{F}$), $A$ levyn pinta-ala ($\text{m}^2$), $\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\text{F/m}$, $\varepsilon_\text{r}$ eristeen suhteellinen permittiivisyys, $W$ energia ($\text{J}$) ja $E_\text{max}$ eristeen läpilyöntilujuus ($\text{V/m}$). Läpilyöntilujuus on suurin kenttä, jonka eriste kestää. Levykondensaattorin kaava pätee, kun $d$ on pieni levyjen kokoon verrattuna ja eriste täyttää koko välin. Kun kondensaattori on kytketty lähteeseen, sen jännite pysyy samana. Kun kondensaattori on irrotettu lähteestä, sen varaus pysyy samana.

### Komponentit ja turvallisuus

```kaavat
LEDin etuvastus :: R = \frac{U - U_\text{D}}{I}
aurinkokennon hyötysuhde :: \eta = \frac{P}{GA}
kehon läpi kulkeva virta :: I = \frac{U}{R}
```

missä $R$ on LEDin etuvastus ($\Omega$), $U_\text{D}$ LEDin jännite ($\text{V}$), $P = UI$ aurinkokennon sähköteho maksimitehopisteessä ($\text{W}$) ja $G$ valon voimakkuus ($\text{W/m}^2$). Viimeinen yhtälö antaa kehon läpi kulkevan virran. Siinä $U$ on kosketusjännite ja $R$ koko virtatien resistanssi. Diodi johtaa vain päästösuuntaan, kun sen jännite on suurempi kuin kynnysjännite. Sulake suojaa johtoa, ja vikavirtasuoja suojaa ihmistä.

## Yleisiä virheitä {Virheet}

- **Kenttä ja voima ovat aina samaan suuntaan.** Negatiiviseen varaukseen, esimerkiksi elektroniin, voima osoittaa kenttää vastaan.
- **Etäisyys ilman neliötä.** Kun etäisyys on kaksinkertainen, Coulombin laki antaa neljäsosan voimasta.
- **Kenttä kasvaa, kun levyä lähestytään.** Levyjen välissä kenttä on homogeeninen. Siksi voima on sama kaikkialla.
- **Energia $QU$.** Kondensaattoriin varastoituu $\tfrac12 QU$. Toinen puoli muuttuu latauksessa johtimien sisäenergiaksi.
- **Eriste irrotetussa kondensaattorissa.** Varaus pysyy samana. Siksi jännite ja energia pienenevät, eivät kasva.
- **Etuvastus ilman LEDin jännitettä.** Vastuksen yli on vain $U - U_\text{D}$.
- **Suuri jännite on aina vaarallinen.** Vaara syntyy virrasta, joka kulkee kehon kautta. Virran ajaa eli aiheuttaa kahden kohdan välinen jännite.

## Kertaa tarvittaessa {Kertaa}

- Varaus ja Coulombin laki: [*Sähkövaraus ja Coulombin laki*](fy6-10.html). Kenttä ja levyt: [*Homogeeninen sähkökenttä*](fy6-11.html).
- Potentiaali, työ ja elektronivoltti: [*Potentiaalienergia ja potentiaali sähkökentässä*](fy6-12.html). Kapasitanssi ja energia: [*Kondensaattori ja sen energia*](fy6-13.html).
- Diodi, LED ja aurinkokenno: [*Puolijohteet, diodi, LED ja aurinkokenno*](fy6-14.html).
- Sulake, maadoitus ja vikavirtasuoja: [*Sähköturvallisuus kotona ja työssä*](fy6-15.html). Lataus ja kolmivaihesähkö: [*Soveltava luku: sähköauto ja kodin sähköjärjestelmä*](fy6-16.html).
