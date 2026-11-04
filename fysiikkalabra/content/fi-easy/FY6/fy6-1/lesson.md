# Virtapiiri, sähkövirta ja jännite

> **Miksi** taskulampun lamppu syttyy samalla hetkellä, kun painat katkaisijaa, vaikka johdon elektronit etenevät hitaammin kuin etana?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pimeä huone illalla. Pöydällä on taskulamppu. Sen kylki on piirretty auki, ja sisällä näkyy kaksi paristoa peräkkäin, jousi ja katkaisija. Lampun valokeila valaisee pöytää ja seinää oikealla." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy61h-night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy61h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy61h-tube" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4f8fbf"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy61h-head" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61h-cell420" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61h-cell556" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy61h-night)"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy61h-table)"/>
  <rect x="0" y="436" width="1200" height="8" fill="#f1dfb5"/>
  <path d="M0,470 Q600,463.829163520506 1200,474" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,492 Q600,491.40084824198675 1200,496" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,514 Q600,511.6439512766883 1200,518" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,536 Q600,532.5474926083261 1200,540" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,558 Q600,552.7240073720895 1200,562" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,580 Q600,580.2344871059468 1200,584" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M790,390 L1200,170 L1200,440 Z" fill="#ffc078" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M790,390 L1200,250 L1200,440 Z" fill="#f1dfb5" stroke-linejoin="round" fill-opacity="0.45"/>
  <ellipse cx="1150" cy="300" rx="44" ry="150" fill="#ffffff" fill-opacity="0.35"/>
  <rect x="330" y="344" width="400" height="92" rx="20" fill="url(#fy61h-tube)" stroke="#1f2933" stroke-width="4"/>
  <path d="M730,350 L790,330 L790,450 L730,430 Z" fill="url(#fy61h-head)" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <rect x="786" y="330" width="14" height="112" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <circle cx="788" cy="390" r="30" fill="#ffffff"/>
  <rect x="470" y="326" width="60" height="20" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="372" y="358" width="330" height="64" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="420" y="368" width="128" height="44" rx="6" fill="url(#fy61h-cell420)" stroke="#1f2933" stroke-width="3"/>
  <rect x="504" y="370" width="36" height="40" fill="#f1dfb5"/>
  <rect x="548" y="382" width="9" height="16" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="556" y="368" width="128" height="44" rx="6" fill="url(#fy61h-cell556)" stroke="#1f2933" stroke-width="3"/>
  <rect x="640" y="370" width="36" height="40" fill="#f1dfb5"/>
  <rect x="684" y="382" width="9" height="16" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polyline points="378,410 383,370 388,410 393,370 398,410 403,370 408,410 413,370 418,410" fill="none" stroke="#8a96a3" stroke-width="4" stroke-linejoin="round"/>
  <line x1="694" y1="390" x2="730" y2="390" stroke="#b8622d" stroke-width="5" stroke-linecap="butt"/>
</svg>

## Ydinajatus
Kaikki aine koostuu atomeista. Atomeissa on positiivisesti varattuja protoneja ja negatiivisesti varattuja elektroneja. Varaukset vaikuttavat toisiinsa **sähköisellä vuorovaikutuksella**. Samanmerkkiset varaukset hylkivät toisiaan, ja erimerkkiset vetävät toisiaan puoleensa. Tavallisessa kappaleessa on yhtä paljon protoneja ja elektroneja. Siksi kappale on sähköisesti neutraali. Kun varauksia saadaan liikkumaan samaan suuntaan, syntyy **sähkövirta**. Sähkövirta on siis varauksen liikettä. Sähkövirran avulla sähköinen vuorovaikutus siirtää energiaa paristosta lamppuun.

### Johteet ja eristeet
Aine, jossa varaukset pääsevät liikkumaan, on **johde**. Metalleissa osa elektroneista ei ole sidottu yhteen atomiin. Ne liikkuvat vapaasti metalli-ionien välissä. Niitä kutsutaan vapaiksi elektroneiksi. Siksi kupari, alumiini ja muut metallit johtavat hyvin sähköä. Aine, jossa varaukset eivät pääse liikkumaan, on **eriste**. Eristeitä ovat muovi, kumi, lasi ja kuiva puu. Sähköjohdossa on kuparinen johdin, jonka ympärillä on muovinen eristekuori. Eriste estää virtaa kulkemasta sinne, minne sen ei kuulu kulkea.

### Virtapiiri
Lamppu palaa vain, kun se on osa suljettua **virtapiiriä**. Jännitelähteestä, esimerkiksi paristosta, lähtee johdin lamppuun. Lampusta johdin menee takaisin jännitelähteen toiseen napaan. Kytkin avaa ja sulkee piirin. Kun kytkin avataan, piiriin tulee katko. Silloin virta lakkaa kulkemasta koko piirissä samalla hetkellä. Virtaa ei synny paristossa, eikä se kulu lampussa. Lampun läpi kulkee yhtä suuri virta kuin piirin muissakin kohdissa. Sama varaus palaa paristoon. Lamppu ei kuluta varausta. Lamppu muuttaa sähköistä energiaa valoksi ja hehkulangan sisäenergiaksi. Sisäenergia siirtyy lämpönä ympäristöön.

<svg data-fig="piiri" viewBox="0 0 600 340" role="img" aria-label="Suljettu virtapiiri pöydällä. Alhaalla vasemmalla on kaksi AA-paristoa peräkkäin pidikkeessä, plusnapa oikealla. Pariston plusnavasta johto kulkee oikealle suljetun kytkimen kautta ja nousee oikeaan yläkulmaan. Ylhäällä johto kulkee vasemmalle lampun kautta. Lamppu palaa. Johto palaa vasenta reunaa alas pariston miinusnapaan. Violetit nuolet näyttävät sovitun virran suunnan: plusnavasta ulkoisen piirin kautta miinusnapaan. Kaavakuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy61-piiri-base" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy61-piiri-holder" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy61-piiri-c1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61-piiri-c2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61-piiri-glow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#f1dfb5"/></linearGradient></defs>
  <polyline points="156,268 60,268 60,128 540,128 540,268 436,268" fill="none" stroke="#1f2933" stroke-width="13" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="156,268 60,268 60,128 540,128 540,268 436,268" fill="none" stroke="#b8622d" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="300,268 364,268" fill="none" stroke="#1f2933" stroke-width="13" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="300,268 364,268" fill="none" stroke="#b8622d" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="346" y="266" width="108" height="22" rx="4" fill="url(#fy61-piiri-base)" stroke="#a97a35" stroke-width="2"/>
  <circle cx="364" cy="268" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="436" cy="268" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="364" y1="265" x2="436" y2="265" stroke="#b8622d" stroke-width="6" stroke-linecap="round"/>
  <rect x="140" y="242" width="168" height="52" rx="6" fill="url(#fy61-piiri-holder)" stroke="#1f2933" stroke-width="2"/>
  <rect x="150" y="253" width="70" height="30" rx="5" fill="url(#fy61-piiri-c1)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="193.5" y="254.5" width="21" height="27" fill="#f1dfb5"/>
  <rect x="220" y="262" width="7" height="12" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="228" y="253" width="70" height="30" rx="5" fill="url(#fy61-piiri-c2)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="271.5" y="254.5" width="21" height="27" fill="#f1dfb5"/>
  <rect x="298" y="262" width="7" height="12" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="300" cy="88" r="46" fill="url(#fy61-piiri-glow)"/>
  <circle cx="300" cy="88" r="26" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M291,110 L291,88 L296,82 L300,88 L304,82 L309,88 L309,110" fill="none" stroke="#e8590c" stroke-width="2" stroke-linejoin="round"/>
  <rect x="284" y="110" width="32" height="26" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="570" y1="236" x2="570" y2="180" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M570,166 L577,181 L563,181 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="560" y="121.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="462" y1="106" x2="414" y2="106" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M400,106 L415,99 L415,113 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="30" y1="152" x2="30" y2="208" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M30,222 L23,207 L37,207 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="316" y1="300" x2="332" y2="300" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M346,300 L331,307 L331,293 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="176.5" y="295.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{paristo}$</div></foreignObject>
  <foreignObject x="362.5" y="295.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kytkin}$</div></foreignObject>
  <foreignObject x="380" y="35.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
  <foreignObject x="118.5" y="81.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{johdin}$</div></foreignObject>
  <foreignObject x="315" y="229.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="111" y="229.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
</svg>

### Virran suunta ja elektronien liike
Virran suunnaksi on sovittu suunta, johon positiivinen varaus liikkuisi. Ulkoisessa piirissä se on jännitelähteen plusnavasta miinusnapaan. Metallijohtimessa liikkuvat kuitenkin negatiiviset elektronit. Ne kulkevat päinvastaiseen suuntaan, miinusnavasta plusnapaan. Sovittu suunta on peräisin ajalta ennen elektronin löytämistä. Sitä käytetään edelleen kaikissa kytkentäkaavioissa. Elektronit etenevät johdossa hitaasti, tyypillisesti alle millimetrin sekunnissa. Lamppu syttyy silti heti, koska johto on alusta asti täynnä vapaita elektroneja. Kun piiri suljetaan, sähkökenttä syntyy koko johtoon lähes valon nopeudella. Silloin kaikki vapaat elektronit alkavat liikkua yhtä aikaa, myös lampun hehkulangassa.

<svg data-fig="johdin" viewBox="0 0 600 330" role="img" aria-label="Johdon pala suurennettuna. Uloimpana on muovinen eristekuori, ja sen sisällä on kuparijohdin. Kuparissa on säännöllisessä hilassa positiivisia metalli-ioneja ja niiden välissä vapaita elektroneja. Sininen nuoli osoittaa vasemmalle: vapaat elektronit liikkuvat vasemmalle. Violetti nuoli osoittaa oikealle: sovittu virran suunta on vastakkainen kuin elektronien liike. Kaavakuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy61-johdin-ins" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy61-johdin-cu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#b8622d"/></linearGradient></defs>
  <rect x="24" y="90" width="552" height="168" rx="22" fill="url(#fy61-johdin-ins)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="24" y="112" width="552" height="124" fill="url(#fy61-johdin-cu)" stroke="#1f2933" stroke-width="2"/>
  <circle cx="58" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="53" y1="134" x2="63" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="58" y1="129" x2="58" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="85" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="80" y1="174" x2="90" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="169" x2="85" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="58" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="53" y1="214" x2="63" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="58" y1="209" x2="58" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="112" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="107" y1="134" x2="117" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="112" y1="129" x2="112" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="139" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="134" y1="174" x2="144" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="139" y1="169" x2="139" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="112" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="107" y1="214" x2="117" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="112" y1="209" x2="112" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="166" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="161" y1="134" x2="171" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="166" y1="129" x2="166" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="193" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="188" y1="174" x2="198" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="193" y1="169" x2="193" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="166" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="161" y1="214" x2="171" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="166" y1="209" x2="166" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="220" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="215" y1="134" x2="225" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220" y1="129" x2="220" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="247" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="242" y1="174" x2="252" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="247" y1="169" x2="247" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="220" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="215" y1="214" x2="225" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220" y1="209" x2="220" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="274" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="269" y1="134" x2="279" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="274" y1="129" x2="274" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="301" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="296" y1="174" x2="306" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="301" y1="169" x2="301" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="274" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="269" y1="214" x2="279" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="274" y1="209" x2="274" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="328" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="323" y1="134" x2="333" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="328" y1="129" x2="328" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="355" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="350" y1="174" x2="360" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="355" y1="169" x2="355" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="328" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="323" y1="214" x2="333" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="328" y1="209" x2="328" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="382" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="377" y1="134" x2="387" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="382" y1="129" x2="382" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="409" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="404" y1="174" x2="414" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="409" y1="169" x2="409" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="382" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="377" y1="214" x2="387" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="382" y1="209" x2="382" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="436" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="431" y1="134" x2="441" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="436" y1="129" x2="436" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="463" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="458" y1="174" x2="468" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="463" y1="169" x2="463" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="436" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="431" y1="214" x2="441" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="436" y1="209" x2="436" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="490" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="485" y1="134" x2="495" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="490" y1="129" x2="490" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="517" cy="174" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="512" y1="174" x2="522" y2="174" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="517" y1="169" x2="517" y2="179" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="490" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="485" y1="214" x2="495" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="490" y1="209" x2="490" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="544" cy="134" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="539" y1="134" x2="549" y2="134" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="544" y1="129" x2="544" y2="139" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="544" cy="214" r="11" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="539" y1="214" x2="549" y2="214" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <line x1="544" y1="209" x2="544" y2="219" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="46" cy="154" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="77" cy="194.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="105.5" cy="154.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="139.5" cy="197" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="167" cy="155" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="199" cy="195" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="226.5" cy="156.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="251.5" cy="197.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="287" cy="156.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="310" cy="198" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="341.5" cy="157.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="374.5" cy="196" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="403" cy="157.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="428.5" cy="196" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="457.5" cy="155.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="488" cy="196.5" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="520" cy="156" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="549" cy="196" r="6" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="470" y1="290" x2="355" y2="290" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M340,290 L356,283 L356,297 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="193" y="275.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\text{elektronit}$</div></foreignObject>
  <line x1="340" y1="46" x2="455" y2="46" stroke="#7048e8" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M470,46 L454,53 L454,39 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="482" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="40" y="31.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{eriste}$</div></foreignObject>
  <foreignObject x="40" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{kupari}$</div></foreignObject>
  <line x1="64" y1="276" x2="64" y2="230" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="64" cy="230" r="4" fill="#6b7480"/>
</svg>

### Kytkentäkaavio
Virtapiiri piirretään **kytkentäkaaviona**. Siinä jokaisella osalla on oma piirrosmerkkinsä. Paristossa pitkä ohut viiva on plusnapa ja lyhyt paksu viiva miinusnapa. Lamppu on ympyrä, jonka sisällä on risti. Vastus on suorakulmio. Mittarit piirretään ympyröinä, joiden sisällä on mittarin kirjain: ampeerimittari $\text{A}$ ja volttimittari $\text{V}$. Johtimet piirretään suorina vaaka- ja pystyviivoina. Kahden johtimen liitoskohta merkitään pisteellä.

<svg data-fig="symbolit" viewBox="0 0 600 390" role="img" aria-label="Kytkentäkaavion piirrosmerkit kahdessa sarakkeessa. Vasemmalla ylhäältä alas: paristo, jossa pitkä ohut viiva on plusnapa ja lyhyt paksu viiva miinusnapa; lamppu, ympyrä jonka sisällä on risti; vastus, suorakulmio; ampeerimittari, ympyrä jonka sisällä on A. Oikealla: avoin kytkin, jonka vipu on nostettu irti; suljettu kytkin, jonka vipu on kosketuksissa; johdin; liitoskohta pisteenä; volttimittari, ympyrä jonka sisällä on V." style="max-width:100%;font-size:24px">
  <line x1="306" y1="22" x2="306" y2="368" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <polyline points="20,62 108,62" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <rect x="56" y="32" width="16" height="60" fill="#ffffff"/>
  <line x1="58" y1="38" x2="58" y2="86" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="70" y1="51" x2="70" y2="73" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="31" y="15.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="71" y="15.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="120" y="47.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{paristo}$</div></foreignObject>
  <polyline points="20,140 108,140" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <circle cx="64" cy="140" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="50" y1="126" x2="78" y2="154" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="50" y1="154" x2="78" y2="126" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="120" y="125.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lamppu}$</div></foreignObject>
  <polyline points="20,218 108,218" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <rect x="39" y="208" width="50" height="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="120" y="203.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vastus}$</div></foreignObject>
  <polyline points="20,296 108,296" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <circle cx="64" cy="296" r="21" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="49" y="281.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="120" y="281.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ampeerimittari}$</div></foreignObject>
  <polyline points="318,62 406,62" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <rect x="337" y="56" width="50" height="12" fill="#ffffff"/>
  <line x1="336" y1="62" x2="382" y2="37.5" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <circle cx="336" cy="62" r="4.5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="388" cy="62" r="4.5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="416" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{avoin kytkin}$</div></foreignObject>
  <polyline points="318,140 406,140" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <rect x="337" y="134" width="50" height="12" fill="#ffffff"/>
  <line x1="336" y1="140" x2="388" y2="140" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="336" cy="140" r="4.5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="388" cy="140" r="4.5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="416" y="125.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{suljettu kytkin}$</div></foreignObject>
  <polyline points="318,218 406,218" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <foreignObject x="416" y="203.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{johdin}$</div></foreignObject>
  <polyline points="318,296 406,296" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <polyline points="362,296 362,330" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <circle cx="362" cy="296" r="6" fill="#1f2933"/>
  <foreignObject x="416" y="281.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{liitoskohta}$</div></foreignObject>
  <polyline points="318,344 406,344" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <circle cx="362" cy="344" r="21" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="347" y="329.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="416" y="329.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{volttimittari}$</div></foreignObject>
</svg>

Kaavio näyttää, mitkä osat on kytketty toisiinsa. Se ei näytä, miltä laitteet näyttävät tai kuinka pitkiä johdot ovat. Samasta virtapiiristä voi siksi piirtää monta oikean näköistä kaaviota. Tärkeää on, että virta kulkee kaaviossa samojen osien kautta samassa järjestyksessä kuin todellisessa piirissä. Virran suunta merkitään johtimen viereen nuolella plusnavasta miinusnapaan.

<svg data-fig="kaavio" viewBox="0 0 600 320" role="img" aria-label="Kuvan 2 virtapiiri kytkentäkaaviona. Silmukka on suorakulmion muotoinen. Alareunassa vasemmalla on kaksi paristokennoa peräkkäin, ja pitkä viiva eli plusnapa on oikealla. Alareunassa oikealla on suljettu kytkin. Yläreunan keskellä on lamppu, ympyrä jossa on risti. Violetti nuoli oikean reunan vieressä osoittaa ylöspäin ja on merkitty I. Virta kulkee plusnavasta kytkimen ja lampun kautta miinusnapaan." style="max-width:100%;font-size:24px">
  <polyline points="90,70 500,70 500,250 90,250 90,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>
  <rect x="178" y="220" width="16" height="60" fill="#ffffff"/>
  <line x1="192" y1="226" x2="192" y2="274" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="180" y1="239" x2="180" y2="261" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <rect x="228" y="220" width="16" height="60" fill="#ffffff"/>
  <line x1="242" y1="226" x2="242" y2="274" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="230" y1="239" x2="230" y2="261" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <rect x="371" y="244" width="58" height="12" fill="#ffffff"/>
  <line x1="370" y1="250" x2="430" y2="250" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="370" cy="250" r="4.5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="430" cy="250" r="4.5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="295" cy="70" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="281" y1="56" x2="309" y2="84" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="281" y1="84" x2="309" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="237" y="279.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="163" y="279.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="199" y="279.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <line x1="536" y1="196" x2="536" y2="138" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M536,124 L543,139 L529,139 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="558" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="358.5" y="279.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kytkin}$</div></foreignObject>
  <foreignObject x="253.5" y="15.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
</svg>

## Kaava: Sähkövirta
Sähkövirta kertoo, kuinka suuri varaus kulkee johtimen poikkileikkauksen läpi aikayksikössä. Poikkileikkaus on kohta, jossa johto ajatellaan katkaistuksi poikittain:
```latex
I = \frac{Q}{t}
```
missä $I$ on sähkövirta ($\text{A}$), $Q$ poikkileikkauksen läpi kulkenut varaus ($\text{C}$) ja $t$ aika ($\text{s}$). Varauksen yksikkö on coulombi $\text{C}$ ja virran yksikkö ampeeri $\text{A}$. Virta on $1\,\text{A}$, kun poikkileikkauksen läpi kulkee joka sekunti varaus $1\,\text{C}$. Siis $1\,\text{A} = 1\,\text{C/s}$. Kun virta tunnetaan, kulkenut varaus saadaan tulona $Q = It$.

<svg data-fig="virta" viewBox="0 0 600 320" role="img" aria-label="Kuparijohdin suurennettuna. Johdon keskellä on katkoviivalla piirretty poikkileikkaus. Sinisiä elektroneja on koko johdossa, ja ne liikkuvat vasemmalle poikkileikkauksen läpi. Oikealla ylhäällä on sekuntikello. Violetti nuoli johdon yläpuolella osoittaa oikealle ja on merkitty I. Merkinnät: ajassa t poikkileikkauksen läpi kulkee varaus Q. Kaavakuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy61-virta-cu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#b8622d"/></linearGradient></defs>
  <rect x="26" y="118" width="548" height="104" rx="8" fill="url(#fy61-virta-cu)" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="300" cy="170" rx="22" ry="52" fill="#ffffff" fill-opacity="0.35" stroke="#1f2933" stroke-width="2" stroke-dasharray="7 5"/>
  <circle cx="53" cy="145.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82" cy="169.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="118" cy="198.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="144" cy="143" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="175" cy="168.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="200.5" cy="199.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="232.5" cy="142" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="255.5" cy="171" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="309.5" cy="198.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="321.5" cy="142" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="343.5" cy="172.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="379" cy="198" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="401" cy="145" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="434" cy="173" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="466" cy="202" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="492" cy="142.5" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="522.5" cy="170" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="552.5" cy="197" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="250" y1="252" x2="135" y2="252" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M120,252 L136,245 L136,259 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="262" y="237.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{elektronit}$</div></foreignObject>
  <line x1="250" y1="80" x2="366" y2="80" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M380,80 L365,87 L365,73 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="396" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="208.5" y="19.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{poikkileikkaus}$</div></foreignObject>
  <rect x="515" y="22.5" width="9.5" height="7" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="518" y="29" width="4" height="4" fill="#6c757d"/>
  <circle cx="520" cy="62" r="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="520" cy="62" r="24.6" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="520" y1="41.5" x2="520" y2="38.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="530" y1="44.5" x2="531.5" y2="41.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="537.5" y1="52" x2="540.5" y2="50.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540.5" y1="62" x2="543.5" y2="62" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="537.5" y1="72" x2="540.5" y2="73.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="530" y1="79.5" x2="531.5" y2="82.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="520" y1="82.5" x2="520" y2="85.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="510" y1="79.5" x2="508.5" y2="82.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="502.5" y1="72" x2="499.5" y2="73.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="499.5" y1="62" x2="496.5" y2="62" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="502.5" y1="52" x2="499.5" y2="50.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="510" y1="44.5" x2="508.5" y2="41.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="520" y1="62" x2="539" y2="68" stroke="#c92a2a" stroke-width="2.1" stroke-linecap="round"/>
  <circle cx="520" cy="62" r="2.4" fill="#1f2933"/>
  <foreignObject x="450" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="180" y="279.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q\ \text{kulkee ajassa}\ t$</div></foreignObject>
</svg>

### Varaus ja elektronien määrä
Elektronin varaus on $-e$. Tässä $e$ on alkeisvaraus, pienin vapaana esiintyvä varaus. Kun $N$ elektronia kulkee poikkileikkauksen läpi, kulkenut varaus on niiden varausten summa:
```latex
Q = N e
```
missä $Q$ on varauksen suuruus ($\text{C}$), $N$ elektronien lukumäärä ja $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ alkeisvaraus. Yhteen coulombiin tarvitaan siis noin $6{,}24 \cdot 10^{18}$ elektronia. Siksi elektroneja ei lasketa yksitellen. Sen sijaan virtaa mitataan ampeereina.

### Jännite
Paristo ei anna piiriin varausta, sillä varaus kiertää piirissä ja palaa paristoon. Paristo antaa varaukselle energiaa, ja lamppu muuttaa sen energian valoksi ja hehkulangan sisäenergiaksi. Sisäenergia siirtyy lämpönä ympäristöön. **Jännite** kertoo, kuinka paljon energiaa siirtyy jokaista varausyksikköä kohti, kun varaus kulkee kahden kohdan välillä:
```latex
U = \frac{E}{Q}
```
missä $U$ on jännite ($\text{V}$), $E$ siirtynyt energia ($\text{J}$) ja $Q$ varaus ($\text{C}$). Jännitteen yksikkö on voltti $\text{V}$, ja $1\,\text{V} = 1\,\text{J/C}$. AA-pariston jännite $1{,}5\,\text{V}$ tarkoittaa, että jokainen paristosta lamppuun kulkeva coulombi tuo lamppuun energian $1{,}5\,\text{J}$. Tämä pätee, kun johtojen ja pariston oma vastus jätetään huomiotta. Mitä suurempi jännite on, sitä enemmän energiaa sama varaus siirtää.

<svg data-fig="jannite" viewBox="0 0 600 350" role="img" aria-label="Paristo on vasemmalla ja lamppu oikealla. Niiden välissä on oranssi energiavirran nuoli paristosta lamppuun. Paristoon on merkitty jännite U yhtä suuri kuin 1,5 volttia. Nuoleen on merkitty energia 1,5 joulea jokaista coulombia kohti. Lamppu säteilee valoa ja lämpöä. Ylhäällä johto kulkee pariston plusnavasta lampun kylkeen. Alhaalla johto palaa lampun kannasta pariston pohjaan. Violetti nuoli näyttää, että sama varaus kiertää takaisin paristoon. Kaavakuva." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy61-jannite-cell" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61-jannite-glow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#f1dfb5"/></linearGradient></defs>
  <polyline points="132,56 132,26 566,26 566,161 486,161" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="132,56 132,26 566,26 566,161 486,161" fill="none" stroke="#b8622d" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="132,150 132,262 468,262 468,170" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="132,150 132,262 468,262 468,170" fill="none" stroke="#b8622d" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="92" y="70" width="80" height="120" rx="8" fill="url(#fy61-jannite-cell)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="92" y="70" width="80" height="36" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="118" y="56" width="28" height="14" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="12" y="211.5" width="106" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U = 1{,}5\,\text{V}$</div></foreignObject>
  <foreignObject x="155" y="21.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="155" y="181.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <path d="M196,131 L360,131 L360,143 L392,120 L360,97 L360,109 L196,109 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="219" y="59.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5\,\text{J}\ \text{/}\ 1\,\text{C}$</div></foreignObject>
  <foreignObject x="246.5" y="151.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{energia}$</div></foreignObject>
  <circle cx="468" cy="120" r="60" fill="url(#fy61-jannite-glow)"/>
  <circle cx="468" cy="120" r="32" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M459,148 L459,120 L464,112 L468,120 L472,112 L477,120 L477,148" fill="none" stroke="#e8590c" stroke-width="2.2" stroke-linejoin="round"/>
  <rect x="450" y="148" width="36" height="26" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="404" y1="96.5" x2="391" y2="92" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="429" y1="64.5" x2="421" y2="53" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="507" y1="64.5" x2="515" y2="53" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="360" y1="288" x2="254" y2="288" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M240,288 L255,281 L255,295 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="140" y="303.5" width="320" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{sama varaus palaa paristolle}$</div></foreignObject>
</svg>

### Tyypillisiä arvoja
Jännitteet ja virrat vaihtelevat arkisissa laitteissa paljon. Taulukon arvot ovat suuruusluokkia.

<figure class="unit-photo"><img src="pics/fy6/macro-circuit-board.webp" alt="Piirilevy läheltä. Levyllä on vihreä kondensaattori, vastus ja muita osia."><figcaption>Elektroniikkalaitteen piirilevy. Johtimet yhdistävät levyn osat toisiinsa. Kondensaattoriin on merkitty suurin jännite, jonka se kestää: $6{,}3\,\text{V}$.</figcaption></figure>

| Jännitelähde | Jännite |
|---|---|
| AA-paristo | $1{,}5\,\text{V}$ |
| puhelimen akku | $3{,}7\,\text{V}$ |
| auton akku | $12\,\text{V}$ |

| Laite | Virta |
|---|---|
| merkkivalon LED | $0{,}02\,\text{A}$ |
| taskulampun lamppu | $0{,}3\,\text{A}$ |
| puhelimen laturi | $2\,\text{A}$ |

## Esimerkki
Taskulampun lampun läpi kulkee virta $0{,}25\,\text{A}$, ja lamppu palaa $12\,\text{min}$. Kuinka suuri varaus kulkee tänä aikana lampun läpi?

<!-- vaihe -->

**Tunnetut ja kysytty.** Virta on $I = 0{,}25\,\text{A}$ ja aika $t = 12\,\text{min}$. Kysytään lampun läpi kulkenutta varausta $Q$.

<!-- vaihe -->

**Periaate.** Virta kertoo, kuinka suuri varaus kulkee lampun läpi sekunnissa. Virta pysyy samana koko ajan. Siksi varaus saadaan virran määritelmästä $I = \tfrac{Q}{t}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan varaus kertomalla yhtälön molemmat puolet ajalla:
```latex
\begin{aligned}
&I = \frac{Q}{t} \\
&Q = I t
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ampeeri on coulombi sekunnissa, joten aika muutetaan sekunneiksi: $12\,\text{min} = 12 \cdot 60\,\text{s} = 720\,\text{s}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen. Muista, että $1\,\text{A}\cdot\text{s} = 1\,\text{C}$:
```latex
\begin{aligned}
Q &= I t \\
&= 0{,}25\,\text{A}\cdot 720\,\text{s} \\
&= 180\,\text{C}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lampun läpi kulkee varaus $Q = 180\,\text{C}$. Kahden merkitsevän numeron tarkkuudella se on $1{,}8 \cdot 10^{2}\,\text{C}$, koska lähtötiedoissa $0{,}25\,\text{A}$ ja $12\,\text{min}$ on kaksi merkitsevää numeroa.

<!-- vaihe -->

**Järkevyys.** Joka sekunti lampun läpi kulkee neljäsosa coulombia. Ajassa $720\,\text{s}$ neljäsosa luvusta $720$ on $180$. Elektroneina varaus on $180\,\text{C} : (1{,}602 \cdot 10^{-19}\,\text{C}) \approx 1{,}1 \cdot 10^{21}$ elektronia. Se on valtava määrä, mutta johdossa niitä on vielä paljon enemmän.

## Yleinen virhekäsitys
Moni ajattelee, että lamppu kuluttaa sähkövirtaa. Silloin lampun jälkeen johdossa kulkisi vähemmän virtaa kuin ennen lamppua. Näin ei ole. Sama varaus, joka tulee lamppuun, lähtee siitä ja palaa paristoon. Siksi virta on yhtä suuri lampun molemmin puolin. Lamppu muuttaa varauksen kuljettaman sähköisen energian valoksi ja hehkulangan sisäenergiaksi. Toinen virhekäsitys on, että elektronit lähtevät paristosta ja kulkevat lamppuun asti, ennen kuin lamppu syttyy. Johto on kuitenkin valmiiksi täynnä vapaita elektroneja. Ne alkavat liikkua kaikkialla piirissä yhtä aikaa.

## Tiivistelmä
- Sähkövirta on varauksen liikettä. Metallijohtimessa liikkuvat vapaat elektronit. Eristeessä varaukset eivät pääse liikkumaan.
- Virta kulkee vain suljetussa virtapiirissä. Sama virta kulkee lampun läpi ja palaa paristoon: virta ei kulu. Paristosta kuluu energiaa, ei varausta.
- Sähkövirta on $I = \tfrac{Q}{t}$, yksikkö ampeeri, $1\,\text{A} = 1\,\text{C/s}$. Varaus on $Q = Ne$, missä $e = 1{,}602 \cdot 10^{-19}\,\text{C}$.
- Jännite on siirtynyt energia varausyksikköä kohti, $U = \tfrac{E}{Q}$, yksikkö voltti, $1\,\text{V} = 1\,\text{J/C}$.
- Sovittu virran suunta on ulkoisessa piirissä plusnavasta miinusnapaan. Elektronit liikkuvat vastakkaiseen suuntaan.
- Kytkentäkaaviossa osat piirretään piirrosmerkeillä ja johtimet suorina viivoina. Kytkin piirretään avoimena (vipu irti) tai suljettuna (vipu kosketuksissa).
