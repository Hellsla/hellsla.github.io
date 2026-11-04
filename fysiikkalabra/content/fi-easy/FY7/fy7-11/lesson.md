# Dispersio: prisma ja sateenkaari

> **Miksi** sateenkaaressa punainen on aina ulkoreunalla ja violetti sisäreunalla? Ja miksi sateenkaaren näkee vain silloin, kun aurinko on selän takana?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kesäsateen jälkeen pellon ja metsän yllä on kirkas sateenkaari. Sen ulkoreunalla on punainen ja sisäreunalla violetti. Sen ulkopuolella näkyy himmeämpi toinen sateenkaari, jossa värit ovat päinvastaisessa järjestyksessä. Kaarten välissä taivas on tummempi. Taustalla on harmaita sadepilviä. Etualalla ihminen seisoo selin katsojaan ja katsoo kaarta." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy711h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy711h-field" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#e9c98a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy711h-sky)"/>
  <circle cx="600" cy="660" r="470" fill="#eef5f9" fill-opacity="0.55"/>
  <path d="M24,118 Q21,70.5 77,76 Q99.5,25.5 155.5,42.5 Q206,14.5 234,67.5 Q284.5,73 279,118 Z" fill="#6b7480" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M321,82 Q319,44.5 363,49 Q380.5,9.5 424.5,22.5 Q464,0.5 486,42.5 Q525.5,47 521,82 Z" fill="#6b7480" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M765,110 Q762,59 822,65 Q846,11 906,29 Q960,-1 990,56 Q1044,62 1038,110 Z" fill="#6b7480" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M1020,170 Q1018,136 1058,140 Q1074,104 1114,116 Q1150,96 1170,134 Q1206,138 1202,170 Z" fill="#6b7480" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M-40,660 A640,640 0 0 1 1240,660" fill="none" stroke="#7048e8" stroke-width="11.5" stroke-opacity="0.45"/>
  <path d="M-29,660 A629,629 0 0 1 1229,660" fill="none" stroke="#1971c2" stroke-width="11.5" stroke-opacity="0.45"/>
  <path d="M-18,660 A618,618 0 0 1 1218,660" fill="none" stroke="#2b8a3e" stroke-width="11.5" stroke-opacity="0.45"/>
  <path d="M-7,660 A607,607 0 0 1 1207,660" fill="none" stroke="#f59f00" stroke-width="11.5" stroke-opacity="0.45"/>
  <path d="M4,660 A596,596 0 0 1 1196,660" fill="none" stroke="#e8590c" stroke-width="11.5" stroke-opacity="0.45"/>
  <path d="M15,660 A585,585 0 0 1 1185,660" fill="none" stroke="#c92a2a" stroke-width="11.5" stroke-opacity="0.45"/>
  <path d="M60,660 A540,540 0 0 1 1140,660" fill="none" stroke="#c92a2a" stroke-width="13.5" stroke-opacity="0.9"/>
  <path d="M73,660 A527,527 0 0 1 1127,660" fill="none" stroke="#e8590c" stroke-width="13.5" stroke-opacity="0.9"/>
  <path d="M86,660 A514,514 0 0 1 1114,660" fill="none" stroke="#f59f00" stroke-width="13.5" stroke-opacity="0.9"/>
  <path d="M99,660 A501,501 0 0 1 1101,660" fill="none" stroke="#2b8a3e" stroke-width="13.5" stroke-opacity="0.9"/>
  <path d="M112,660 A488,488 0 0 1 1088,660" fill="none" stroke="#1971c2" stroke-width="13.5" stroke-opacity="0.9"/>
  <path d="M125,660 A475,475 0 0 1 1075,660" fill="none" stroke="#7048e8" stroke-width="13.5" stroke-opacity="0.9"/>
  <path d="M0,410 Q100,398 200,407.5 Q300,395.5 400,408 Q500,396.5 600,408 Q700,378.5 800,411.5 Q900,394.5 1000,408.5 Q1100,394.5 1200,408.5 Q1300,382 1400,411 V600 H0 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M0,433.5 Q100,400.5 200,436 Q300,409.5 400,435 Q500,399 600,431 Q700,409.5 800,431 Q900,414.5 1000,435 Q1100,405 1200,431 Q1300,409 1400,432 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M0,418 L9.5,394 L18.5,418 L27.5,394.5 L37,418 L52,374.5 L66.5,418 L79,383.5 L91.5,418 L105.5,377.5 L119.5,418 L130.5,387.5 L142,418 L155.5,378.5 L169.5,418 L178,396 L187,418 L201.5,376 L216,418 L231,373.5 L246,418 L255.5,393.5 L265,418 L280,374 L295,418 L304,395 L313,418 L325.5,384 L337.5,418 L352.5,374.5 L367.5,418 L380,383 L392.5,418 L406,379.5 L419.5,418 L433.5,376.5 L448,418 L461.5,379 L475,418 L490.5,372.5 L506,418 L516,392 L526,418 L539.5,380 L552.5,418 L562,393 L572,418 L580.5,395.5 L589.5,418 L602.5,381.5 L615.5,418 L629.5,378 L643,418 L657.5,377 L671.5,418 L681,393 L691,418 L701.5,389.5 L712,418 L722.5,390 L733,418 L741.5,396.5 L750,418 L760.5,391.5 L770.5,418 L782.5,384.5 L794.5,418 L806,386.5 L817.5,418 L829.5,384.5 L841.5,418 L855,378.5 L869,418 L879.5,390.5 L889.5,418 L905,373.5 L920,418 L929,395 L938,418 L950,385 L961.5,418 L973,388 L984,418 L996,384.5 L1008,418 L1021,380.5 L1034.5,418 L1043.5,395 L1052.5,418 L1063,390 L1073.5,418 L1083,393.5 L1092.5,418 L1101,396.5 L1109.5,418 L1118,397 L1126.5,418 L1139,383 L1151.5,418 L1163,387 L1174.5,418 L1188.5,377 L1202.5,418 V430 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy711h-field)"/>
  <rect x="190" y="378" width="120" height="70" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="204" y1="381" x2="204" y2="445" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="218" y1="381" x2="218" y2="445" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="232" y1="381" x2="232" y2="445" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="246" y1="381" x2="246" y2="445" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="260" y1="381" x2="260" y2="445" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="274" y1="381" x2="274" y2="445" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="288" y1="381" x2="288" y2="445" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="190" y="378" width="10" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="378" width="10" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M170,378 L250,339.5 L330,378 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="220" y="397.5" width="40" height="28" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="220" y="397.5" width="40" height="28" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="240" y1="397.5" x2="240" y2="425.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="975.5" y="320" width="9" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="975.5" y="452" width="4.5" height="2" fill="#1f2933"/>
  <rect x="980" y="434" width="4.5" height="2" fill="#1f2933"/>
  <rect x="975.5" y="416" width="4.5" height="2" fill="#1f2933"/>
  <rect x="980" y="398" width="4.5" height="2" fill="#1f2933"/>
  <rect x="975.5" y="380" width="4.5" height="2" fill="#1f2933"/>
  <rect x="980" y="362" width="4.5" height="2" fill="#1f2933"/>
  <rect x="975.5" y="344" width="4.5" height="2" fill="#1f2933"/>
  <line x1="980" y1="377" x2="953" y2="359" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="980" y1="357.5" x2="1007" y2="339.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="980" y1="342.5" x2="953" y2="324.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="980" cy="327.5" r="30" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="957.5" cy="350" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1002.5" cy="347" r="25.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="980" cy="362" r="22.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <path d="M579.5,588 L583,505.5 H605 L608.5,588 H597.5 L594,533 L590.5,588 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M575.5,511 Q573,450.5 594,447 Q615,450.5 612.5,511 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M577.5,458 L572,511" fill="none" stroke="#c92a2a" stroke-width="12.1" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="572" cy="515.5" r="6.05" fill="#f1dfb5"/>
  <path d="M610.5,458 L616,511" fill="none" stroke="#c92a2a" stroke-width="12.1" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="616" cy="515.5" r="6.05" fill="#f1dfb5"/>
  <rect x="589" y="436" width="10" height="13" fill="#f1dfb5"/>
  <circle cx="594" cy="425" r="16.5" fill="#f1dfb5"/>
  <path d="M577,425 Q577.5,405.5 594,406.5 Q611.5,406.5 611,423 Q597.5,416.5 577,425 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="594" cy="424" r="17.05" fill="#1f2933"/>
</svg>

## Ydinajatus

### Taitekerroin riippuu aallonpituudesta
Luvussa *Valon heijastuminen ja taittuminen* taitekerroin $n$ kertoi, kuinka monta kertaa hitaammin valo kulkee aineessa kuin tyhjiössä. Tarkat mittaukset näyttävät, että taitekerroin riippuu myös valon aallonpituudesta. Vedessä ja lasissa taitekerroin on violetille valolle suurempi kuin punaiselle. Siksi violetti valo kulkee niissä hitaammin. Kruunulasissa punainen valo etenee nopeudella noin $198\,000\,\text{km/s}$ ja violetti valo nopeudella noin $196\,000\,\text{km/s}$. Tätä sanotaan **dispersioksi**: taitekerroin on eri suuri eri aallonpituuksille.

Taulukon aallonpituudet ovat tyhjiössä. Kun valo menee rajapinnan läpi, sen taajuus ei muutu. Väri riippuu taajuudesta, joten väri pysyy samana, vaikka nopeus ja aallonpituus muuttuvat.

| väri | $\lambda\ (\text{nm})$ | vesi | kruunulasi |
|---|---|---|---|
| punainen | $656$ | $1{,}3315$ | $1{,}5143$ |
| keltainen | $589$ | $1{,}3334$ | $1{,}5167$ |
| sininen | $486$ | $1{,}3375$ | $1{,}5224$ |
| violetti | $405$ | $1{,}3431$ | $1{,}5302$ |

Veden taitekertoimet lämpötilassa $20\,{}^\circ\text{C}$: M. Daimon ja A. Masumura, *Applied Optics* 46, 2007. Kruunulasin N-BK7 taitekertoimet: SCHOTT AG, optisten lasien luettelo, 2017.

### Miksi violetti hidastuu enemmän
Valo on aaltoa, jossa sähkökenttä värähtelee. Valon sähkökenttä saa aineen elektronit värähtelemään valon taajuudella. Värähtelevät elektronit lähettävät itse valoa. Tämä valo yhdistyy tulevaan valoon, ja yhdistynyt aalto etenee hitaammin kuin valo tyhjiössä.

Elektronien vaste riippuu taajuudesta. Vedessä ja lasissa vaste voimistuu, kun taajuus kasvaa kohti ultraviolettia. Aine absorboi ultravioletin voimakkaasti. Siksi violetti valo, jolla on suuri taajuus, hidastuu enemmän kuin punainen valo, jolla on pieni taajuus. Violetin taitekerroin on siis suurempi.

### Prisma hajottaa valkoisen valon
Valkoinen valo, kuten auringonvalo, on eri aallonpituuksien eli värien seos. Kun valkoinen valo tulee vinosti lasiin, jokainen väri taittuu taittumislain mukaan, mutta eri verran. Violetin taitekerroin on suurin, joten violetti taittuu eniten normaalia kohti.

Tasapaksussa ikkunalasissa lasin pinnat ovat yhdensuuntaiset. Toisesta pinnasta värit tulevat ulos samansuuntaisina kuin alkuperäinen säde, joten värejä ei huomaa. Prisman pinnat ovat vinossa toisiinsa nähden. Siksi värit taittuvat toisessa pinnassa vielä lisää erilleen. Prismasta tulee ulos värien viuhka eli **spektri**. Punainen poikkeaa alkuperäisestä suunnastaan vähiten ja violetti eniten.

<svg data-fig="prism" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa. Valkoisen valon kapea kimppu tulee vasemmalta alhaalta lasiprisman vasempaan sivuun. Prismassa valo hajoaa väreiksi. Toisesta sivusta lähtee värien viuhka. Punainen poikkeaa alkuperäisestä suunnastaan vähiten ja violetti eniten. Niiden välissä ovat oranssi, keltainen, vihreä ja sininen. Värit osuvat oikealla olevaan valkoiseen varjostimeen allekkain, punainen ylimpänä. Värien erkaantuminen on piirretty todellista suuremmaksi." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy711-glass1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <path d="M290,34 L421,261 L159,261 Z" fill="url(#fy711-glass1)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="218" y1="159" x2="360" y2="155.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="360" y1="155.5" x2="520" y2="197.5" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="218" y1="159" x2="361" y2="157" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="361" y1="157" x2="520" y2="207" stroke="#e8590c" stroke-width="3" stroke-linecap="butt"/>
  <line x1="218" y1="159" x2="362" y2="159" stroke="#f59f00" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="362" y1="159" x2="520" y2="217" stroke="#f59f00" stroke-width="3" stroke-linecap="butt"/>
  <line x1="218" y1="159" x2="363" y2="160.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="363" y1="160.5" x2="520" y2="227.5" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <line x1="218" y1="159" x2="364" y2="162.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="364" y1="162.5" x2="520" y2="239" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="218" y1="159" x2="365" y2="164" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="365" y1="164" x2="520" y2="252" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <rect x="520" y="171.5" width="14" height="107" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="521.5" y="194.5" width="11" height="6" fill="#c92a2a"/>
  <rect x="521.5" y="204" width="11" height="6" fill="#e8590c"/>
  <rect x="521.5" y="214" width="11" height="6" fill="#f59f00"/>
  <rect x="521.5" y="224.5" width="11" height="6" fill="#2b8a3e"/>
  <rect x="521.5" y="236" width="11" height="6" fill="#1971c2"/>
  <rect x="521.5" y="249" width="11" height="6" fill="#7048e8"/>
  <line x1="20.5" y1="230.5" x2="218" y2="159" stroke="#1f2933" stroke-width="10" stroke-linecap="round"/>
  <line x1="20.5" y1="230.5" x2="218" y2="159" stroke="#ffffff" stroke-width="7" stroke-linecap="round"/>
  <path d="M133.5,189.5 L121.5,201 L117,188.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="16" y="113.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{valkoinen valo}$</div></foreignObject>
  <foreignObject x="473" y="137" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\text{punainen}$</div></foreignObject>
  <foreignObject x="473" y="283.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{violetti}$</div></foreignObject>
  <foreignObject x="223.5" y="276.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lasiprisma}$</div></foreignObject>
</svg>

Prisma ei värjää valoa. Isaac Newton näytti 1660-luvulla, että yksi väri ei enää hajoa uusiksi väreiksi. Hän erotti spektristä yhden värin ja ohjasi sen toisen prisman läpi. Väri taittui mutta pysyi samana. Toisin päin käännetty prisma taas kokoaa spektrin takaisin valkoiseksi valoksi. Värit olivat siis valmiina valkoisessa valossa, ja prisma vain erottaa ne toisistaan.

### Sateenkaari syntyy vesipisaroissa
Pieni sadepisara on lähes pallon muotoinen. Auringonvalo taittuu pisaraan, heijastuu pisaran takapinnasta ja taittuu ulos pisaran alaosasta. Valo palaa siis takaisin aurinkoa kohti, mutta kääntyneenä. Kummassakin taittumisessa violetti taittuu enemmän kuin punainen, joten värit erkanevat.

Valon lähtösuunta riippuu myös siitä, mihin kohtaan pisaraa säde osuu. Silti valo kasautuu yhteen suuntaan. Monesta eri osumakohdasta säteet lähtevät lähes samaan suuntaan. Punainen valo lähtee noin $42^\circ$:n kulmassa ja violetti valo noin $40{,}6^\circ$:n kulmassa siihen suuntaan nähden, josta auringonvalo tuli. Tähän suuntaan pisara loistaa kirkkaimmin.

<svg data-fig="drop" viewBox="0 0 600 372" role="img" aria-label="Periaatekuva, ei mittakaavassa: suuri vesipisara. Vasemmalta tulee vaakasuora valkoisen auringonvalon säde pisaran yläosaan. Tulokohdassa on katkoviivalla piirretty normaali. Siihen on merkitty tulokulma alfa ja taitekulma beeta. Pisarassa valo hajoaa. Punainen ja violetti säde kulkevat pisaran takaseinään, heijastuvat siitä ja taittuvat ulos pisaran alaosasta vasemmalle alaspäin. Violetti lähtee loivemmassa kulmassa kuin punainen. Värien ero on piirretty todellista suuremmaksi." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy711-drop-g" cx="0.38" cy="0.35" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#a9d1f0"/></radialGradient></defs>
  <circle cx="392" cy="160" r="118" fill="url(#fy711-drop-g)" stroke="#2f74b5" stroke-width="2.5"/>
  <line x1="332" y1="58.5" x2="502" y2="117.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="502" y1="117.5" x2="416" y2="275.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="416" y1="275.5" x2="327.5" y2="356.5" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M327.5,356.5 L334,341 L343,351 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="332" y1="58.5" x2="505" y2="126.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="505" y1="126.5" x2="397" y2="278" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="397" y1="278" x2="296.5" y2="343" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M296.5,343 L305,329.5 L312.5,340.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="20" y1="58.5" x2="332" y2="58.5" stroke="#1f2933" stroke-width="9" stroke-linecap="round"/>
  <line x1="20" y1="58.5" x2="332" y2="58.5" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
  <path d="M130,58.5 L115,65 L115,51.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="296.5" y1="-2" x2="378" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M288,58.5 A44,44 0 0 1 310,20.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="252" y="20" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <path d="M358.5,103 A52,52 0 0 0 381,75.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="380" y="78" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\beta$</div></foreignObject>
  <foreignObject x="20" y="12" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{auringonvalo}$</div></foreignObject>
  <foreignObject x="468" y="43.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{heijastuu}$</div></foreignObject>
  <foreignObject x="349.5" y="330" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{punainen}$</div></foreignObject>
  <foreignObject x="172.5" y="310.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\text{violetti}$</div></foreignObject>
</svg>

### Miksi punainen on ulkoreunalla
Kun aurinko on selän takana, auringonsäteet kulkevat pään ohi kohti **vastapistettä**. Vastapiste on oman pään varjon kohdalla horisontin alapuolella. Silmään tulee punaista valoa niistä pisaroista, jotka näkyvät $42^\circ$:n kulmassa vastapisteen suunnasta. Violettia valoa tulee niistä pisaroista, jotka näkyvät $40{,}6^\circ$:n kulmassa.

Samassa kulmassa olevat pisarat muodostavat ympyrän, jonka keskipiste on vastapiste. Punaisen ympyrä on suurempi, joten punainen on kaaren ulkoreunalla. Kukin pisara lähettää silmään vain yhden värin. Sen muut värit kulkevat silmän ohi. Siksi jokainen katsoja näkee oman sateenkaarensa.

<svg data-fig="observer" viewBox="0 0 600 372" role="img" aria-label="Periaatekuva sivulta, kulmat eivät ole mittakaavassa. Tarkkailija seisoo oikealla selkä aurinkoon päin. Auringonsäteet tulevat oikealta ylhäältä vinosti alas. Silmästä lähtee katkoviiva auringonsäteiden suuntaan alas vasemmalle kohti vastapistettä. Vastapiste on tarkkailijan pään varjon kohdalla horisontin alapuolella. Ylempi pisara on 42 asteen kulmassa tästä suunnasta, ja siitä silmään tulee punainen valo. Sen violetti valo kulkee silmän yläpuolelta ohi. Alempi pisara on noin 40,6 asteen kulmassa, ja siitä silmään tulee violetti valo. Sen punainen valo osuu maahan tarkkailijan eteen." style="max-width:100%;font-size:24px">
  <rect x="12" y="300" width="576" height="46" fill="#f1dfb5"/>
  <line x1="12" y1="300" x2="588" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="508" cy="232" r="15" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <path d="M494,249 h28 l4,40 h-36 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M502,289 V300 M516,289 V300" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <line x1="582" y1="34" x2="503" y2="62.5" stroke="#e8590c" stroke-width="3" stroke-linecap="butt"/>
  <path d="M495.5,65.5 L506.5,55 L511,66.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <line x1="582" y1="92" x2="503" y2="120.5" stroke="#e8590c" stroke-width="3" stroke-linecap="butt"/>
  <path d="M495.5,123.5 L506.5,113 L511,124.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="430" y="125.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{auringonvalo}$</div></foreignObject>
  <line x1="500" y1="232" x2="258" y2="320" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="207" y1="113.5" x2="479.5" y2="224" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M479.5,224 L464.5,224.5 L469,212.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="192" y1="161" x2="478.5" y2="227" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M478.5,227 L463.5,230 L466.5,218 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="207.5" y1="111.5" x2="486.5" y2="176" stroke="#7048e8" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <line x1="191.5" y1="163" x2="530.5" y2="300" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <circle cx="194" cy="108.5" r="13" fill="#a9d1f0" stroke="#2f74b5" stroke-width="2"/>
  <circle cx="178.5" cy="158" r="13" fill="#a9d1f0" stroke="#2f74b5" stroke-width="2"/>
  <path d="M342,289.5 A168,168 0 0 1 344,169" fill="none" stroke="#c92a2a" stroke-width="2" stroke-linejoin="round"/>
  <path d="M389,272.5 A118,118 0 0 1 385,205.5" fill="none" stroke="#7048e8" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="279.5" y="214" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$42^\circ$</div></foreignObject>
  <foreignObject x="387" y="218.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$40{,}6^\circ$</div></foreignObject>
  <foreignObject x="216" y="90" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{punainen}$</div></foreignObject>
  <foreignObject x="50.5" y="145.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\text{violetti}$</div></foreignObject>
  <foreignObject x="111" y="311.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vastapiste}$</div></foreignObject>
</svg>

Sateenkaari näkyy siis vain, kun aurinko paistaa selän takaa ja edessä on pisaroita. Tasaisella maalla näkyy vain se osa kaaresta, joka on horisontin yläpuolella. Olkoon auringon korkeus horisontista $h$. Silloin vastapiste on yhtä paljon horisontin alapuolella, ja punaisen kaaren huippu on korkeudella $42^\circ - h$.

Kun aurinko on yli $42^\circ$:n korkeudella, koko kaari jää horisontin alapuolelle. Silloin sitä ei näe maan pinnalta. Siksi sateenkaaria näkyy keskikesällä aamuin ja illoin, kun aurinko on matalalla.

### Sivukaari
Pääkaaren ulkopuolella näkyy joskus himmeämpi **sivukaari**. Siinä valo heijastuu pisaran sisällä kahdesti. Värien järjestys on päinvastainen: punainen on sisäreunalla noin $50^\circ$:n kulmassa ja violetti ulkoreunalla noin $54^\circ$:n kulmassa vastapisteen suunnasta.

Jokaisessa heijastuksessa osa valosta pääsee ulos pisarasta. Siksi sivukaari on himmeämpi. Kaarten välissä taivas on tummempi. Pääkaaren pisarat valaisevat vain kaaren sisäpuolta, ja sivukaaren pisarat valaisevat vain kaaren ulkopuolta.

## Kaava: Taittumislaki eri aallonpituuksille
Kun valo tulee ilmasta aineeseen, jokainen aallonpituus taittuu oman taitekertoimensa mukaan:
```latex
\sin \alpha_1 = n(\lambda) \sin \alpha_2
```
Tässä $\alpha_1$ on tulokulma ja $\alpha_2$ on taitekulma. Molemmat mitataan pinnan normaalista. $n(\lambda)$ on aineen taitekerroin aallonpituudella $\lambda$. Ilman taitekerroin on $1{,}0003$, ja se on pyöristetty ykköseksi. Yleinen muoto on $n_1 \sin\alpha_1 = n_2 \sin\alpha_2$ (luku *Valon heijastuminen ja taittuminen*).

Valon nopeus aineessa on $v = c : n(\lambda)$, missä $c = 3{,}00 \cdot 10^8\,\text{m/s}$. Kuvaajassa kruunulasin taitekerroin pienenee, kun aallonpituus kasvaa. Se pienenee jyrkimmin violetin päässä.

<svg data-fig="n-graph" viewBox="0 0 600 372" role="img" aria-label="Kuvaaja mittakaavassa: kruunulasin N-BK7 taitekerroin n tyhjiöaallonpituuden lambda funktiona välillä 400–700 nm. Kuvaajassa on kuusi mittauspistettä valmistajan taulukosta: 405 nm 1,5302; 436 nm 1,5267; 486 nm 1,5224; 546 nm 1,5187; 589 nm 1,5167 ja 656 nm 1,5143. Käyrä laskee. Lyhyillä aallonpituuksilla taitekerroin on suurin, ja käyrä loivenee punaista kohti. Vaaka-akselin alla on näkyvän valon värijana violetista punaiseen." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy711-band1" gradientUnits="userSpaceOnUse" x1="137.69230769230768" y1="0" x2="470.0" y2="0"><stop offset="0.000" stop-color="#7048e8"/><stop offset="0.200" stop-color="#1971c2"/><stop offset="0.400" stop-color="#2b8a3e"/><stop offset="0.583" stop-color="#f59f00"/><stop offset="0.700" stop-color="#e8590c"/><stop offset="0.867" stop-color="#c92a2a"/></linearGradient></defs>
  <line x1="137.5" y1="290" x2="137.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="193" y1="290" x2="193" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248.5" y1="290" x2="248.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="290" x2="359" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="290" x2="414.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="242" x2="470" y2="242" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="194" x2="470" y2="194" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="146" x2="470" y2="146" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="98" x2="470" y2="98" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="291" x2="110" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,24 L116,37 L104,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="290" x2="137.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="115" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="193" y1="290" x2="193" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248.5" y1="290" x2="248.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="226" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="304" y1="290" x2="304" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="359" y1="290" x2="359" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="336.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="414.5" y1="290" x2="414.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="103" y1="242" x2="110" y2="242" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="227.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}515$</div></foreignObject>
  <line x1="103" y1="194" x2="110" y2="194" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="179.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}520$</div></foreignObject>
  <line x1="103" y1="146" x2="110" y2="146" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="131.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}525$</div></foreignObject>
  <line x1="103" y1="98" x2="110" y2="98" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="83.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}530$</div></foreignObject>
  <line x1="103" y1="50" x2="110" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="28" y="35.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}535$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="100" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n$</div></foreignObject>
  <polyline points="137.5,90.5 140.5,93.5 143,96.5 146,99.5 149,102 151.5,105 154.5,108 157,110.5 160,113 162.5,116 165.5,118.5 168,121 171,123.5 173.5,126 176.5,128.5 179,131 182,133 185,135.5 187.5,138 190.5,140 193,142 196,144.5 198.5,146.5 201.5,148.5 204,150.5 207,153 209.5,155 212.5,156.5 215,158.5 218,160.5 221,162.5 223.5,164.5 226.5,166 229,168 232,170 234.5,171.5 237.5,173.5 240,175 243,176.5 245.5,178.5 248.5,180 251,181.5 254,183 257,184.5 259.5,186 262.5,187.5 265,189 268,190.5 270.5,192 273.5,193.5 276,195 279,196.5 281.5,198 284.5,199 287,200.5 290,202 293,203 295.5,204.5 298.5,205.5 301,207 304,208 306.5,209.5 309.5,210.5 312,212 315,213 317.5,214 320.5,215.5 323,216.5 326,217.5 329,218.5 331.5,219.5 334.5,221 337,222 340,223 342.5,224 345.5,225 348,226 351,227 353.5,228 356.5,229 359,230 362,231 365,231.5 367.5,232.5 370.5,233.5 373,234.5 376,235.5 378.5,236 381.5,237 384,238 387,239 389.5,239.5 392.5,240.5 395,241.5 398,242 401,243 403.5,243.5 406.5,244.5 409,245.5 412,246 414.5,247 417.5,247.5 420,248.5 423,249 425.5,250 428.5,250.5 431,251 434,252 437,252.5 439.5,253.5 442.5,254 445,254.5 448,255.5 450.5,256 453.5,256.5 456,257 459,258 461.5,258.5 464.5,259 467,259.5 470,260.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="143" cy="95.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="177.5" cy="130" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="233" cy="171" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="299.5" cy="206.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="347.5" cy="225.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="421.5" cy="248.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <rect x="137.5" y="336" width="332.5" height="12" rx="2" fill="url(#fy711-band1)" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="159" y="81" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{violetti}$</span></div></foreignObject>
  <foreignObject x="367.5" y="204" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{punainen}$</span></div></foreignObject>
</svg>

### Prisman poikkeamakulma
Prismassa säde taittuu kahdesti, ja kulmat riippuvat toisistaan:
```latex
\begin{aligned}
&\alpha_2 + \alpha_3 = A \\[6pt]
&\delta = \alpha_1 + \alpha_4 - A
\end{aligned}
```
Tässä $\alpha_1$ on tulokulma ja $\alpha_2$ on taitekulma ensimmäisessä pinnassa. $\alpha_3$ on tulokulma, kun säde osuu lasin sisältä toiseen pintaan, ja $\alpha_4$ on taitekulma, kun säde tulee ulos. Kaikki kulmat mitataan pintojen normaaleista. $A$ on prisman huippukulma. $\delta$ on **poikkeamakulma**: se kertoo, kuinka paljon säde kääntyy alkuperäisestä suunnastaan.

Ensimmäinen yhtälö seuraa kolmion kulmien summasta, koska pintojen normaalit leikkaavat toisensa kulmassa $180^\circ - A$. Toinen yhtälö seuraa siitä, että säde kääntyy ensimmäisessä pinnassa kulman $\alpha_1 - \alpha_2$ ja toisessa pinnassa kulman $\alpha_4 - \alpha_3$. Violetille $\alpha_4$ on suurempi kuin punaiselle, joten violetin poikkeamakulma on suurempi. Yhtälöt pätevät, kun säde pääsee ulos prisman toisesta pinnasta.

<svg data-fig="prism-angles" viewBox="0 0 600 336" role="img" aria-label="Kaavakuva prismasta. Yksivärinen säde tulee vasemmalta prisman vasempaan sivuun tulokulmassa alfa 1 normaaliin nähden. Lasissa säde taittuu kulmaan alfa 2. Säde osuu oikeaan sivuun tulokulmassa alfa 3 ja lähtee prismasta taitekulmassa alfa 4. Molempien pintojen normaalit on piirretty katkoviivoin. Prisman huipussa on huippukulma A. Tulevan säteen jatke on piirretty katkoviivana. Sen ja lähtevän säteen välinen kulma on poikkeamakulma delta." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy711-glass2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <path d="M290,24 L455,310 L125,310 Z" fill="url(#fy711-glass2)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="108" y1="155" x2="257" y2="241" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="467.5" y1="147.5" x2="318.5" y2="233.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="187.5" y1="201" x2="489" y2="67" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <line x1="23.5" y1="274.5" x2="187.5" y2="201" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <path d="M105.5,238 L95.5,249 L90,237.5 Z" fill="#e64980" stroke-linejoin="round"/>
  <line x1="187.5" y1="201" x2="388" y2="193.5" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <line x1="388" y1="193.5" x2="581" y2="246" stroke="#e64980" stroke-width="3" stroke-linecap="butt"/>
  <path d="M581,246 L566,248.5 L569,236.5 Z" fill="#e64980" stroke-linejoin="round"/>
  <path d="M147.5,219 A44,44 0 0 1 149.5,179" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="99.5" y="183" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_1$</div></foreignObject>
  <path d="M227.5,199.5 A40,40 0 0 1 222.5,221" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="245" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_2$</div></foreignObject>
  <path d="M348,195 A40,40 0 0 0 353.5,213.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="298.5" y="204" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_3$</div></foreignObject>
  <path d="M430.5,205 A44,44 0 0 0 426,171.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="443" y="170" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_4$</div></foreignObject>
  <path d="M270,58.5 A40,40 0 0 0 310,58.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="280" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <path d="M411,101.5 A150,150 0 0 1 419,202" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="455.5" y="130.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\delta$</div></foreignObject>
</svg>

### Sateenkaaren kulma
Pisarassa säde kääntyy kolme kertaa. Tulokohdassa se kääntyy kulman $\alpha - \beta$, heijastuksessa kulman $180^\circ - 2\beta$ ja lähtökohdassa taas kulman $\alpha - \beta$. Kokonaiskääntymä on siis $180^\circ + 2\alpha - 4\beta$. Kulma, jossa valo näkyy vastapisteen suunnasta, on $180^\circ$ miinus kokonaiskääntymä eli
```latex
\theta = 4\beta - 2\alpha
```
Tässä $\alpha$ on tulokulma pisaran pinnalla ja $\beta$ on taitekulma. Ne liittyvät toisiinsa yhtälöllä $\sin\alpha = n \sin\beta$. $\theta$ on kulma, jossa valo näkyy vastapisteen suunnasta.

Kuvaaja näyttää, että $\theta$ riippuu tulokulmasta, mutta se ei kasva yli $42{,}3^\circ$:n, kun $n = 1{,}3315$. Huipun lähellä käyrä on lähes vaakasuora. Siksi monesta eri tulokulmasta säteet lähtevät lähes samaan suuntaan, ja siihen suuntaan näkyy kirkas kaari. Muu valo lähtee pienempiin kulmiin, joten taivas on kaaren sisäpuolella vaaleampi. Violetille ($n = 1{,}3431$) suurin kulma on $40{,}6^\circ$.

<svg data-fig="theta-graph" viewBox="0 0 600 350" role="img" aria-label="Kuvaaja mittakaavassa: punaisen valon (n = 1,332) säde lähtee vesipisarasta kulmassa theeta vastapisteen suuntaan nähden. Vaaka-akselilla on tulokulma alfa 0–90 astetta ja pystyakselilla theeta 0–45 astetta. Käyrä nousee origosta ja saavuttaa suurimman arvonsa 42,3 astetta, kun tulokulma on noin 59,5 astetta. Sitten se laskee noin 15 asteeseen. Huipun lähellä käyrä on lähes vaakasuora: monesta eri tulokulmasta säteet lähtevät lähes samaan suuntaan." style="max-width:100%;font-size:24px">
  <line x1="137.5" y1="290" x2="137.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="179" y1="290" x2="179" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220.5" y1="290" x2="220.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="290" x2="262" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="290" x2="345.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="387" y1="290" x2="387" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428.5" y1="290" x2="428.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="263.5" x2="470" y2="263.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="236.5" x2="470" y2="236.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="210" x2="470" y2="210" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="183.5" x2="470" y2="183.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="156.5" x2="470" y2="156.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="130" x2="470" y2="130" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103.5" x2="470" y2="103.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76.5" x2="470" y2="76.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,24 L102,37 L90,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="290" x2="137.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="179" y1="290" x2="179" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220.5" y1="290" x2="220.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="204" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="262" y1="290" x2="262" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="304" y1="290" x2="304" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="345.5" y1="290" x2="345.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="329" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="387" y1="290" x2="387" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="428.5" y1="290" x2="428.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$90$</div></foreignObject>
  <line x1="89" y1="263.5" x2="96" y2="263.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="236.5" x2="96" y2="236.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="222" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="210" x2="96" y2="210" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="183.5" x2="96" y2="183.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="169" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="156.5" x2="96" y2="156.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="130" x2="96" y2="130" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="103.5" x2="96" y2="103.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76.5" x2="96" y2="76.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="62" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="50" x2="96" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha\ (^\circ)$</div></foreignObject>
  <foreignObject x="86" y="-6.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ (^\circ)$</div></foreignObject>
  <polygon points="304,290 304,50 387,50 387,290" fill="#b2f2bb" fill-opacity="0.45"/>
  <polyline points="96,290 99,286 102,282 105.5,278 108.5,274 111.5,270 114.5,266 118,262 121,258 124,254 127,250 130.5,246 133.5,242 136.5,238 139.5,234 143,230.5 146,226.5 149,222.5 152,218.5 155,214.5 158.5,211 161.5,207 164.5,203.5 167.5,199.5 171,195.5 174,192 177,188.5 180,184.5 183.5,181 186.5,177.5 189.5,173.5 192.5,170 195.5,166.5 199,163 202,159.5 205,156 208,152.5 211.5,149.5 214.5,146 217.5,142.5 220.5,139.5 224,136.5 227,133 230,130 233,127 236,124 239.5,121 242.5,118 245.5,115 248.5,112.5 252,109.5 255,107 258,104.5 261,101.5 264.5,99 267.5,97 270.5,94.5 273.5,92 277,90 280,88 283,85.5 286,83.5 289,82 292.5,80 295.5,78 298.5,76.5 301.5,75 305,73.5 308,72 311,71 314,70 317.5,68.5 320.5,68 323.5,67 326.5,66 330,65.5 333,65 336,65 339,64.5 342,64.5 345.5,64.5 348.5,64.5 351.5,65 354.5,65.5 358,66 361,66.5 364,67.5 367,68.5 370.5,70 373.5,71 376.5,72.5 379.5,74.5 382.5,76.5 386,78.5 389,80.5 392,83 395,85.5 398.5,88.5 401.5,91.5 404.5,94.5 407.5,98 411,101.5 414,105.5 417,109.5 420,113.5 423,118 426.5,122.5 429.5,127.5 432.5,132.5 435.5,138 439,143.5 442,149 445,155 448,161.5 451.5,168 454.5,174.5 457.5,181.5 460.5,188.5 464,196 467,203.5 470,211.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="343" y1="64.5" x2="343" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="64.5" x2="343" y2="64.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="343" cy="64.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="308" y="24" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$42{,}3^\circ$</span></div></foreignObject>
  <foreignObject x="273" y="233" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kirkas kaari}$</span></div></foreignObject>
</svg>

## Esimerkki
Valkoisen valon kapea kimppu tulee ilmasta kruunulasilevyn pintaan tulokulmassa $60{,}0^\circ$. Kuinka suuret ovat punaisen ($656\,\text{nm}$) ja violetin ($405\,\text{nm}$) valon taitekulmat lasissa? Kuinka suuri kulma niiden välille syntyy? Käytä taulukon taitekertoimia.

<!-- vaihe -->

**Tunnetut ja kysytty.** Tulokulma on $\alpha_1 = 60{,}0^\circ$. Taulukosta saadaan punaisen valon taitekerroin $n_\text{p} = 1{,}5143$ ja violetin valon taitekerroin $n_\text{v} = 1{,}5302$. Kysytään taitekulmat $\alpha_\text{p}$ ja $\alpha_\text{v}$ sekä niiden erotus $\Delta\alpha = \alpha_\text{p} - \alpha_\text{v}$.

<!-- vaihe -->

**Periaate.** Kumpikin väri noudattaa taittumislakia omalla taitekertoimellaan. Valo tulee ilmasta, jonka taitekerroin on pyöristettynä $1$, joten $\sin \alpha_1 = n \sin \alpha_2$. Kummallakin värillä on sama tulokulma, koska ne kulkevat samassa valkoisen valon kimpussa.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\sin \alpha_1 = n \sin \alpha_2 \\[6pt]
&\sin \alpha_2 = \frac{\sin \alpha_1}{n}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita: taitekertoimella ei ole yksikköä, ja kulmat ovat asteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\sin \alpha_\text{p} = \frac{\sin \alpha_1}{n_\text{p}} \\
&= \frac{\sin 60{,}0^\circ}{1{,}5143} \\
&= 0{,}57190 \\
&\alpha_\text{p} = 34{,}88^\circ \\[6pt]
&\sin \alpha_\text{v} = \frac{\sin \alpha_1}{n_\text{v}} \\
&= \frac{\sin 60{,}0^\circ}{1{,}5302} \\
&= 0{,}56596 \\
&\alpha_\text{v} = 34{,}47^\circ
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Punaisen valon taitekulma on $34{,}9^\circ$ ja violetin valon taitekulma on $34{,}5^\circ$. Tuloksessa on kolme merkitsevää numeroa, koska tulokulmassa $60{,}0^\circ$ on kolme. Säteiden välinen kulma lasketaan pyöristämättömistä kulmista: $\Delta\alpha = 34{,}88^\circ - 34{,}47^\circ = 0{,}41^\circ$.

<!-- vaihe -->

**Järkevyys.** Molemmat taitekulmat ovat pienempiä kuin tulokulma, koska valo taittuu normaalia kohti, kun se tulee optisesti tiheämpään aineeseen. Violetin taitekulma on pienempi, koska sen taitekerroin on suurempi. Ero on alle puoli astetta, joten tasapaksussa lasissa värit erottuvat vain vähän. Prisman vino toinen pinta kasvattaa eroa.

## Yleinen virhekäsitys
Moni ajattelee, että prisma värjää valon tai että värit syntyvät prisman lasissa. Näin ei ole. Värit ovat valmiina valkoisessa valossa, ja prisma erottaa ne, koska taitekerroin riippuu aallonpituudesta.

Toinen yleinen virhe on päätellä, että punainen taittuu eniten, koska sen aallonpituus on pisin. Vedessä ja lasissa asia on päinvastoin: violetin taitekerroin on suurin, joten violetti taittuu ja poikkeaa eniten.

Kolmas virhe on ajatella, että sateenkaari on esine, joka on tietyssä paikassa. Kaari on suunta. Se näkyy aina $42^\circ$:n kulmassa vastapisteestä, joten se siirtyy katsojan mukana. Sen päätä ei voi saavuttaa.

## Tiivistelmä
- Taitekerroin riippuu aallonpituudesta. Tätä sanotaan dispersioksi. Vedessä ja lasissa violetin taitekerroin on suurin ja punaisen pienin, joten violetti taittuu eniten.
- Prismassa valkoinen valo taittuu kahdesti vinoissa pinnoissa, ja värit erkanevat spektriksi. Poikkeamakulma on $\delta = \alpha_1 + \alpha_4 - A$, ja violetti poikkeaa eniten.
- Sateenkaaressa valo taittuu pisaraan, heijastuu sen takapinnasta ja taittuu ulos. Punainen näkyy noin $42^\circ$:n kulmassa ja violetti noin $40{,}6^\circ$:n kulmassa vastapisteestä, joten punainen on ulkoreunalla.
- Sateenkaari näkyy, kun aurinko on selän takana ja alle $42^\circ$:n korkeudella. Sivukaaressa valo heijastuu kahdesti, ja värit ovat päinvastaisessa järjestyksessä.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: puutarhassa kastellaan nurmikkoa letkulla. Vesisuihkun pisaroissa näkyy pieni sateenkaari, kun aurinko paistaa kastelijan selän takaa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy711s-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy711s-lawn2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="url(#fy711s-sky)"/>
  <rect x="0" y="250" width="600" height="110" fill="#b2f2bb"/>
  <path d="M168,232 C250,150 360,130 470,190" fill="none" stroke="#a9d1f0" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="370" cy="180" r="2.01659" fill="#a9d1f0"/>
  <circle cx="409" cy="155" r="2.99437" fill="#a9d1f0"/>
  <circle cx="377" cy="282" r="3.20242" fill="#a9d1f0"/>
  <circle cx="535" cy="197.5" r="2.06348" fill="#a9d1f0"/>
  <circle cx="460.5" cy="246.5" r="2.87866" fill="#a9d1f0"/>
  <circle cx="535.5" cy="170" r="3.02028" fill="#a9d1f0"/>
  <circle cx="479" cy="291" r="3.36744" fill="#a9d1f0"/>
  <circle cx="331.5" cy="197" r="2.18401" fill="#a9d1f0"/>
  <circle cx="519.5" cy="287" r="3.25724" fill="#a9d1f0"/>
  <circle cx="315.5" cy="252.5" r="2.28665" fill="#a9d1f0"/>
  <circle cx="374.5" cy="163.5" r="2.2575" fill="#a9d1f0"/>
  <circle cx="492.5" cy="264" r="2.79928" fill="#a9d1f0"/>
  <circle cx="464.5" cy="262" r="2.55384" fill="#a9d1f0"/>
  <circle cx="334.5" cy="264" r="2.87584" fill="#a9d1f0"/>
  <circle cx="316.5" cy="213" r="2.8202" fill="#a9d1f0"/>
  <circle cx="354" cy="270.5" r="2.66231" fill="#a9d1f0"/>
  <circle cx="427.5" cy="298" r="2.71762" fill="#a9d1f0"/>
  <circle cx="414.5" cy="169.5" r="2.91865" fill="#a9d1f0"/>
  <circle cx="341" cy="281.5" r="2.15232" fill="#a9d1f0"/>
  <circle cx="307" cy="296.5" r="2.96543" fill="#a9d1f0"/>
  <circle cx="335.5" cy="252" r="2.16787" fill="#a9d1f0"/>
  <circle cx="461.5" cy="276.5" r="3.00483" fill="#a9d1f0"/>
  <circle cx="505" cy="158.5" r="2.49875" fill="#a9d1f0"/>
  <circle cx="350" cy="269.5" r="3.20289" fill="#a9d1f0"/>
  <circle cx="345.5" cy="268" r="2.75543" fill="#a9d1f0"/>
  <circle cx="325.5" cy="153" r="2.77224" fill="#a9d1f0"/>
  <circle cx="558" cy="282.5" r="2.46644" fill="#a9d1f0"/>
  <circle cx="319" cy="168" r="2.74507" fill="#a9d1f0"/>
  <circle cx="508.5" cy="268.5" r="2.80434" fill="#a9d1f0"/>
  <circle cx="400.5" cy="154" r="3.10817" fill="#a9d1f0"/>
  <circle cx="495.5" cy="211" r="2.17027" fill="#a9d1f0"/>
  <circle cx="518" cy="160" r="2.08808" fill="#a9d1f0"/>
  <circle cx="429.5" cy="246.5" r="3.35783" fill="#a9d1f0"/>
  <circle cx="340" cy="246.5" r="3.18671" fill="#a9d1f0"/>
  <circle cx="401" cy="191" r="3.08323" fill="#a9d1f0"/>
  <circle cx="480" cy="297" r="3.44678" fill="#a9d1f0"/>
  <circle cx="542" cy="251" r="2.56374" fill="#a9d1f0"/>
  <circle cx="336" cy="261.5" r="2.70322" fill="#a9d1f0"/>
  <circle cx="475" cy="221.5" r="2.54472" fill="#a9d1f0"/>
  <circle cx="393.5" cy="195" r="3.06889" fill="#a9d1f0"/>
  <circle cx="396" cy="193.5" r="2.31124" fill="#a9d1f0"/>
  <circle cx="473.5" cy="187.5" r="2.01789" fill="#a9d1f0"/>
  <circle cx="321" cy="287" r="2.18892" fill="#a9d1f0"/>
  <circle cx="314" cy="197" r="2.07289" fill="#a9d1f0"/>
  <circle cx="361.5" cy="246.5" r="2.72032" fill="#a9d1f0"/>
  <circle cx="407" cy="283.5" r="2.55724" fill="#a9d1f0"/>
  <circle cx="378.5" cy="169" r="3.16266" fill="#a9d1f0"/>
  <circle cx="396" cy="280.5" r="3.16807" fill="#a9d1f0"/>
  <circle cx="403.5" cy="182.5" r="2.32408" fill="#a9d1f0"/>
  <circle cx="458.5" cy="283.5" r="2.58023" fill="#a9d1f0"/>
  <circle cx="380" cy="252.5" r="2.69036" fill="#a9d1f0"/>
  <circle cx="434" cy="232.5" r="2.68833" fill="#a9d1f0"/>
  <circle cx="456.5" cy="209.5" r="3.19841" fill="#a9d1f0"/>
  <circle cx="454" cy="178" r="2.33984" fill="#a9d1f0"/>
  <circle cx="524" cy="209.5" r="2.89889" fill="#a9d1f0"/>
  <circle cx="485.5" cy="278.5" r="2.03977" fill="#a9d1f0"/>
  <circle cx="329.5" cy="214.5" r="3.46222" fill="#a9d1f0"/>
  <circle cx="461" cy="174.5" r="3.20314" fill="#a9d1f0"/>
  <circle cx="438" cy="279" r="2.01457" fill="#a9d1f0"/>
  <circle cx="559.5" cy="288.5" r="3.44485" fill="#a9d1f0"/>
  <circle cx="394" cy="241" r="3.01567" fill="#a9d1f0"/>
  <circle cx="313.5" cy="184" r="2.50537" fill="#a9d1f0"/>
  <circle cx="532.5" cy="196.5" r="2.01142" fill="#a9d1f0"/>
  <circle cx="549" cy="194.5" r="2.82849" fill="#a9d1f0"/>
  <circle cx="521" cy="221" r="2.98507" fill="#a9d1f0"/>
  <circle cx="506" cy="154.5" r="2.86611" fill="#a9d1f0"/>
  <circle cx="388.5" cy="235" r="2.41027" fill="#a9d1f0"/>
  <circle cx="518.5" cy="214" r="2.78106" fill="#a9d1f0"/>
  <circle cx="500.5" cy="280.5" r="3.3028" fill="#a9d1f0"/>
  <circle cx="512.5" cy="173" r="2.63207" fill="#a9d1f0"/>
  <circle cx="309.5" cy="244" r="3.26891" fill="#a9d1f0"/>
  <circle cx="381" cy="272.5" r="2.35907" fill="#a9d1f0"/>
  <circle cx="433.5" cy="216.5" r="2.64117" fill="#a9d1f0"/>
  <circle cx="512.5" cy="174" r="2.65303" fill="#a9d1f0"/>
  <circle cx="538.5" cy="196" r="2.64675" fill="#a9d1f0"/>
  <circle cx="404.5" cy="201" r="2.95232" fill="#a9d1f0"/>
  <circle cx="439.5" cy="238" r="3.25924" fill="#a9d1f0"/>
  <circle cx="506" cy="230" r="2.15627" fill="#a9d1f0"/>
  <circle cx="402.5" cy="252.5" r="2.1672" fill="#a9d1f0"/>
  <circle cx="425" cy="297.5" r="2.09058" fill="#a9d1f0"/>
  <circle cx="305.5" cy="287.5" r="2.13171" fill="#a9d1f0"/>
  <circle cx="418" cy="279" r="2.16716" fill="#a9d1f0"/>
  <circle cx="500" cy="250" r="3.1213" fill="#a9d1f0"/>
  <circle cx="458" cy="180.5" r="2.74645" fill="#a9d1f0"/>
  <circle cx="383.5" cy="233.5" r="3.28421" fill="#a9d1f0"/>
  <circle cx="452.5" cy="214.5" r="2.85862" fill="#a9d1f0"/>
  <circle cx="539.5" cy="239.5" r="2.72814" fill="#a9d1f0"/>
  <circle cx="426" cy="275" r="2.32297" fill="#a9d1f0"/>
  <circle cx="418" cy="157.5" r="2.66748" fill="#a9d1f0"/>
  <circle cx="318.5" cy="293.5" r="2.27303" fill="#a9d1f0"/>
  <path d="M312,300 A118,118 0 0 1 548,300" fill="none" stroke="#c92a2a" stroke-width="7.5" stroke-opacity="0.8"/>
  <path d="M319,300 A111,111 0 0 1 541,300" fill="none" stroke="#e8590c" stroke-width="7.5" stroke-opacity="0.8"/>
  <path d="M326,300 A104,104 0 0 1 534,300" fill="none" stroke="#f59f00" stroke-width="7.5" stroke-opacity="0.8"/>
  <path d="M333,300 A97,97 0 0 1 527,300" fill="none" stroke="#2b8a3e" stroke-width="7.5" stroke-opacity="0.8"/>
  <path d="M340,300 A90,90 0 0 1 520,300" fill="none" stroke="#1971c2" stroke-width="7.5" stroke-opacity="0.8"/>
  <path d="M347,300 A83,83 0 0 1 513,300" fill="none" stroke="#7048e8" stroke-width="7.5" stroke-opacity="0.8"/>
  <rect x="0" y="296" width="600" height="64" fill="url(#fy711s-lawn2)"/>
  <path d="M104,330 L107.5,237 H132.5 L136,330 H123.5 L120,268 L116.5,330 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M99,243 Q96.5,175 120,171.5 Q143.5,175 141,243 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M101.5,183.5 L95,243" fill="none" stroke="#1971c2" stroke-width="13.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="95" cy="248" r="6.82" fill="#f1dfb5"/>
  <path d="M138.5,183.5 L145,243" fill="none" stroke="#1971c2" stroke-width="13.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="145" cy="248" r="6.82" fill="#f1dfb5"/>
  <rect x="114.5" y="159" width="11" height="15" fill="#f1dfb5"/>
  <circle cx="120" cy="146.5" r="18.6" fill="#f1dfb5"/>
  <path d="M101,146.5 Q101.5,124 120,125.5 Q140,125.5 139,144 Q123.5,136.5 101,146.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M145,248 C155,240 162,236 168,232" fill="none" stroke="#2b8a3e" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M100,330 C80,345 50,345 24,338" fill="none" stroke="#2b8a3e" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
</svg>
