# Mittaukset virtapiirissä

> **Miksi** virtamittari kytketään piiriin eri tavalla kuin jännitemittari, ja mitä tapahtuu, jos kytkennät menevät sekaisin?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: koulun laboratorion työpöytä. Pöydällä on kytkentälevy, jossa paristokotelo ja lampunpidike ovat johdoilla samassa piirissä, ja lamppu palaa. Vieressä on harmaa digitaalinen yleismittari, jonka punainen ja musta mittajohto koskettavat lampunpidikkeen kahta napaa." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy62h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><linearGradient id="fy62h-bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy62h-glow"><stop offset="0" stop-color="#ffc078" stop-opacity="0.95"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy62h-wall)"/>
  <rect x="60" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="240" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="420" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="600" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="780" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="960" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="1140" y="60" width="120" height="150" rx="6" fill="#ffffff" stroke="#e3dccb" stroke-width="3"/>
  <rect x="0" y="330" width="1200" height="270" fill="url(#fy62h-bench)"/>
  <rect x="0" y="322" width="1200" height="16" fill="#e9c98a"/>
  <path d="M0,360 C300,354 700,368 1200,358" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,394 C300,388 700,402 1200,392" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,428 C300,422 700,436 1200,426" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,462 C300,456 700,470 1200,460" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,496 C300,490 700,504 1200,494" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,530 C300,524 700,538 1200,528" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,564 C300,558 700,572 1200,562" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <rect x="250" y="380" width="470" height="170" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="262" y="392" width="446" height="146" rx="6" fill="#eef5f9"/>
  <rect x="290" y="420" width="190" height="76" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="302" y="432" width="52" height="52" rx="6" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="342" y="446" width="12" height="24" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="360" y="432" width="52" height="52" rx="6" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="400" y="446" width="12" height="24" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="418" y="432" width="52" height="52" rx="6" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="458" y="446" width="12" height="24" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="570" y="444" width="100" height="52" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <circle cx="580" cy="470" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="660" cy="470" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="620" cy="392" r="110" fill="url(#fy62h-glow)"/>
  <rect x="600" y="418" width="40" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M592,420 C580,370 594,344 620,344 C646,344 660,370 648,420 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M608,418 L612,388 L620,398 L628,388 L632,418" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  <path d="M480,458 C520,458 540,470 580,470" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M660,470 C700,470 700,530 520,530 C380,530 300,530 290,470" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="800" y="210" width="250" height="350" rx="26" fill="#c4ccd4" stroke="#1f2933" stroke-width="4"/>
  <rect x="814" y="224" width="222" height="322" rx="18" fill="#6c757d"/>
  <rect x="842" y="248" width="166" height="74" rx="8" fill="#e3dccb" stroke="#1f2933" stroke-width="3"/>
  <rect x="858" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <rect x="894" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <rect x="930" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <rect x="966" y="266" width="26" height="38" rx="3" fill="none" stroke="#1f2933" stroke-width="5"/>
  <circle cx="925" cy="410" r="50" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <circle cx="925" cy="410" r="20" fill="#1f2933"/>
  <line x1="925" y1="410" x2="900" y2="372" stroke="#ffffff" stroke-width="8" stroke-linecap="round"/>
  <line x1="868" y1="400" x2="854" y2="397.5" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <line x1="891.5" y1="362.5" x2="883.5" y2="351" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <line x1="958.5" y1="362.5" x2="966.5" y2="351" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <line x1="982" y1="400" x2="996" y2="397.5" stroke="#ffffff" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="860" cy="508" r="15" fill="#1f2933" stroke="#ffffff" stroke-width="4"/>
  <circle cx="925" cy="508" r="15" fill="#1f2933" stroke="#c92a2a" stroke-width="4"/>
  <circle cx="990" cy="508" r="15" fill="#1f2933" stroke="#c92a2a" stroke-width="4"/>
  <path d="M860,508 C860,600 720,600 700,560 C686,530 662,510 662,486" fill="none" stroke="#1f2933" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M925,508 C930,620 600,620 560,560 C540,530 574,500 578,486" fill="none" stroke="#c92a2a" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="652" y="474" width="20" height="30" rx="4" fill="#1f2933"/>
  <rect x="568" y="474" width="20" height="30" rx="4" fill="#c92a2a"/>
</svg>

## Ydinajatus

### Virtamittari kytketään sarjaan
**Virtamittari** mittaa, kuinka suuri sähkövirta kulkee sen läpi. Siksi mitattavan virran on kuljettava mittarin kautta: piiri avataan siitä kohdasta, jonka virta halutaan tietää, ja mittari asetetaan aukkoon. Tällöin mittari on **sarjassa** muiden komponenttien kanssa. Haarattomassa piirissä virta on joka kohdassa sama, koska varausta ei katoa eikä kerry minnekään. Lamppu muuttaa sähköenergiaa valoksi ja lämmöksi, mutta se ei kuluta virtaa. Virtamittari voidaan siis kytkeä mihin tahansa kohtaan haaratonta piiriä, ja se näyttää aina saman lukeman.

### Jännitemittari kytketään rinnalle
Jännite on kahden pisteen välinen suure (luku *Virtapiiri, sähkövirta ja jännite*). **Jännitemittari** mittaa jännitteen niiden kahden pisteen välillä, joihin sen johdot kosketetaan. Lampun jännite mitataan koskettamalla lampun kumpaakin napaa: piiriä ei avata, vaan mittari tulee lampun **rinnalle**. Mittarin punainen johto kosketetaan siihen napaan, joka on lähempänä pariston plusnapaa, jolloin lukema on positiivinen.

<svg data-fig="connections" viewBox="0 0 600 344" role="img" aria-label="Kaksi kytkentäkaaviota. Vasemmalla paristo, lamppu ja virtamittari A ovat samassa silmukassa peräkkäin: virtamittari on sarjassa lampun kanssa, ja sama virta I kulkee pariston, mittarin ja lampun läpi. Oikealla paristo ja lamppu muodostavat silmukan, ja jännitemittari V on kytketty lampun napojen väliin lampun rinnalle. Violetit nuolet näyttävät virran suunnan pariston plusnavasta miinusnapaan." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy62-c1-glow"><stop offset="0" stop-color="#ffc078" stop-opacity="0.95"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient><radialGradient id="fy62-c2-glow"><stop offset="0" stop-color="#ffc078" stop-opacity="0.95"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient></defs>
  <line x1="300" y1="16" x2="300" y2="328" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <polyline points="138,236 40,236 40,100 78,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="122,100 174,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="214,100 260,100 260,236 162,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="100" cy="100" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="90" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <circle cx="194" cy="100" r="46" fill="url(#fy62-c1-glow)"/>
  <circle cx="194" cy="100" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="180" y1="86" x2="208" y2="114" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="180" y1="114" x2="208" y2="86" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="143" y1="212" x2="143" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="157" y1="224" x2="157" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="40" y1="192" x2="40" y2="176" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M40,160 L47,176 L33,176 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="56" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="260" y1="144" x2="260" y2="160" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M260,176 L253,160 L267,160 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="71" y="275.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virtamittari}$</div></foreignObject>
  <foreignObject x="102.5" y="305.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sarjaan}$</div></foreignObject>
  <polyline points="438,236 340,236 340,100 430,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="470,100 560,100 560,236 462,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="450" cy="100" r="46" fill="url(#fy62-c2-glow)"/>
  <circle cx="450" cy="100" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="436" y1="86" x2="464" y2="114" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="436" y1="114" x2="464" y2="86" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <polyline points="398,100 398,44 428,44" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="472,44 502,44 502,100" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="398" cy="100" r="5" fill="#1f2933"/>
  <circle cx="502" cy="100" r="5" fill="#1f2933"/>
  <circle cx="450" cy="44" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="440" y="29.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <line x1="443" y1="212" x2="443" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="457" y1="224" x2="457" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="340" y1="192" x2="340" y2="176" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M340,160 L347,176 L333,176 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="356" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="560" y1="144" x2="560" y2="160" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M560,176 L553,160 L567,160 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="358.5" y="275.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jännitemittari}$</div></foreignObject>
  <foreignObject x="396" y="305.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rinnalle}$</div></foreignObject>
</svg>

### Yleismittari
Laboratoriossa virtaa ja jännitettä mitataan yleensä **yleismittarilla**: sama laite mittaa valitsimen asennosta riippuen jännitettä, virtaa ja usein muitakin suureita. Musta johto kuuluu aina liittimeen COM. Punainen johto kuuluu jännitettä ja pieniä virtoja mitattaessa liittimeen $\text{V}\ \text{mA}$ ja suuria virtoja mitattaessa liittimeen $10\,\text{A}$. Valitsimella valitaan sekä suure että **mittausalue**, joka on suurin arvo, jonka mittari tällä asennolla näyttää. Alueella $20\,\text{V}$ näyttö näyttää enintään $19{,}99\,\text{V}$; suuremmalla jännitteellä näyttöön tulee OL (engl. *overload*), mikä tarkoittaa, että arvo on yli mittausalueen.

<svg data-fig="multimeter" viewBox="0 0 600 360" role="img" aria-label="Piirros digitaalisesta yleismittarista. Ylhäällä näyttö, jossa on lukema 1,500 V. Keskellä valitsin, jonka ympärillä ovat mittausalueet 2 V, 20 V, 200 mA ja 10 A; osoitin on alueella 2 V. Alhaalla kolme liitintä: COM, V mA ja 10 A. Mustan johdon paikka on COM ja punaisen V mA tai 10 A. Oikealla selitteet näyttö, valitsin ja liittimet." style="max-width:100%;font-size:24px">
  <rect x="52" y="14" width="256" height="332" rx="22" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="62" y="24" width="236" height="312" rx="14" fill="#6c757d"/>
  <rect x="84" y="34" width="192" height="78" rx="8" fill="#e3dccb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="72" y="50" width="150" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:40px">$1{,}500$</div></foreignObject>
  <foreignObject x="228" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <circle cx="180" cy="206" r="32" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="180" cy="206" r="14" fill="#1f2933"/>
  <line x1="145.5" y1="200" x2="138.5" y2="198.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="86.5" y="179" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffc078">$2\,\text{V}$</div></foreignObject>
  <line x1="160" y1="177.5" x2="156" y2="171.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109.5" y="132.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$20\,\text{V}$</div></foreignObject>
  <line x1="200" y1="177.5" x2="204" y2="171.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="180" y="132.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$200\,\text{mA}$</div></foreignObject>
  <line x1="214.5" y1="200" x2="221.5" y2="198.5" stroke="#ffffff" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="222" y="179" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <line x1="180" y1="206" x2="152.5" y2="201" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <circle cx="110" cy="290" r="12" fill="#1f2933" stroke="#ffffff" stroke-width="3"/>
  <foreignObject x="87.5" y="307.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{COM}$</div></foreignObject>
  <circle cx="180" cy="290" r="12" fill="#1f2933" stroke="#c92a2a" stroke-width="3"/>
  <foreignObject x="155.5" y="307.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{V}\ \text{mA}$</div></foreignObject>
  <circle cx="250" cy="290" r="12" fill="#1f2933" stroke="#c92a2a" stroke-width="3"/>
  <foreignObject x="221" y="307.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <line x1="312" y1="73" x2="350" y2="73" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="358" y="58.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{näyttö}$</div></foreignObject>
  <line x1="312" y1="206" x2="350" y2="206" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="358" y="191.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{valitsin}$</div></foreignObject>
  <line x1="312" y1="290" x2="350" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="358" y="275.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{liittimet}$</div></foreignObject>
</svg>

### Mittausalueen valinta
Pienemmällä alueella näyttö näyttää lisää desimaaleja. Alueella $20\,\text{V}$ lampun jännite näkyy muodossa $1{,}50\,\text{V}$, alueella $2\,\text{V}$ muodossa $1{,}500\,\text{V}$: viimeinen numero kertoo **resoluution** eli pienimmän askeleen, jonka näyttö voi ottaa. Siksi mitataan pienimmällä alueella, jolle lukema vielä mahtuu. Kun suuruusluokkaa ei tiedetä, aloitetaan suurimmalta alueelta ja siirrytään pienempään. Virtaa mitattaessa tämä on myös turvallisuuskysymys, koska liian suuri virta polttaa mittarin sulakkeen.

### Mittari vaikuttaa piiriin
Jokaisella komponentilla on **resistanssi**, joka kuvaa, kuinka voimakkaasti se vastustaa sähkövirtaa; suure tarkennetaan luvussa *Resistanssi ja Ohmin laki*. Sarjaan kytketyn virtamittarin resistanssi on hyvin pieni, jotta mittari ei juuri pienentäisi virtaa, jota se mittaa. Rinnalle kytketyn jännitemittarin resistanssi on hyvin suuri, esimerkiksi $10\,\text{M}\Omega$, jotta mittarin kautta ei juuri kulkisi virtaa komponentin ohi. Ihanteellinen mittari ei muuttaisi piiriä lainkaan; todellinen muuttaa sitä vähän, mikä on yksi mittausepävarmuuden lähde.

Väärin kytketty mittari muuttaa piiriä paljon. Jos virtamittari kytketään lampun rinnalle, virta kulkee lähes kokonaan pienen resistanssin mittarin kautta lampun ohi: lamppu sammuu, ja virta voi kasvaa niin suureksi, että mittarin sulake palaa. Kun sulake on palanut, mittari on poissa piiristä ja lamppu syttyy uudelleen. Tällaista virtatietä, joka ohittaa komponentin, sanotaan oikosuluksi. Jos taas jännitemittari kytketään sarjaan, sen suuri resistanssi pienentää koko piirin virran lähes nollaan: lamppu sammuu, ja mittari näyttää suunnilleen pariston jännitteen.

<svg data-fig="wrong" viewBox="0 0 600 352" role="img" aria-label="Kaksi väärää kytkentää. Vasemmalla virtamittari A on kytketty lampun rinnalle. Virta kulkee lähes kokonaan pienen resistanssin virtamittarin kautta, mitä kuvaa paksu violetti nuoli: lamppu ei pala, ja virta on suuri. Oikealla jännitemittari V on sarjassa lampun kanssa. Mittarin suuri resistanssi pienentää virran lähes nollaan, joten lamppu ei pala eikä virtanuolia ole." style="max-width:100%;font-size:24px">
  <line x1="300" y1="16" x2="300" y2="336" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <polyline points="138,236 40,236 40,112 130,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="170,112 260,112 260,236 162,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="150" cy="112" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="136" y1="98" x2="164" y2="126" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="136" y1="126" x2="164" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <polyline points="98,112 98,50 128,50" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="172,50 202,50 202,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="98" cy="112" r="5" fill="#1f2933"/>
  <circle cx="202" cy="112" r="5" fill="#1f2933"/>
  <circle cx="150" cy="50" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="140" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <line x1="98" y1="100" x2="98" y2="84" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M98,62 L108,84 L88,84 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="202" y1="60" x2="202" y2="76" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M202,98 L192,76 L212,76 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="143" y1="212" x2="143" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="157" y1="224" x2="157" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="40" y1="174" x2="40" y2="158" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M40,136 L50,158 L30,158 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="56" y="143.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\text{suuri } I$</div></foreignObject>
  <foreignObject x="71" y="283.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virtamittari}$</div></foreignObject>
  <foreignObject x="96" y="313.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rinnalle}$</div></foreignObject>
  <polyline points="438,236 340,236 340,112 378,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="422,112 464,112" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="504,112 560,112 560,236 462,236" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="400" cy="112" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="390" y="97.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <circle cx="484" cy="112" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="470" y1="98" x2="498" y2="126" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="470" y1="126" x2="498" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="443" y1="212" x2="443" y2="260" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="457" y1="224" x2="457" y2="248" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="427.5" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \approx 0$</div></foreignObject>
  <foreignObject x="358.5" y="283.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jännitemittari}$</div></foreignObject>
  <foreignObject x="402.5" y="313.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sarjaan}$</div></foreignObject>
</svg>

## Kaava: Yleismittarin virheraja

### Valmistajan ilmoittama virheraja
Mittarin lukema ei ole täsmälleen mitattavan suureen todellinen arvo. Digitaalisen mittarin valmistaja ilmoittaa käyttöohjeessa jokaiselle alueelle **virherajan** muodossa $\pm(p + n\ \text{numeroa})$: virheraja on prosenttiosuus $p$ lukemasta lisättynä $n$:llä viimeisen numeron askeleella. Valmistajan ilmoittama virheraja kertoo, kuinka paljon kunnossa olevan ja ohjeiden mukaan käytetyn mittarin lukema voi enintään poiketa todellisesta arvosta. Mittauksen kokonaisepävarmuuteen voivat kuitenkin vaikuttaa myös mittausmenetelmä, mittarin vaikutus piiriin ja muut virhelähteet.

| Alue | Resoluutio | Virheraja |
|---|---|---|
| jännite $2\,\text{V}$ | $0{,}001\,\text{V}$ | $\pm(0{,}5\,\% + 2\ \text{numeroa})$ |
| jännite $20\,\text{V}$ | $0{,}01\,\text{V}$ | $\pm(0{,}5\,\% + 2\ \text{numeroa})$ |
| virta $200\,\text{mA}$ | $0{,}1\,\text{mA}$ | $\pm(1{,}0\,\% + 2\ \text{numeroa})$ |
| virta $10\,\text{A}$ | $0{,}01\,\text{A}$ | $\pm(2{,}0\,\% + 3\ \text{numeroa})$ |

### Virherajan laskeminen
Lukeman $x$ virheraja on
```latex
\Delta x = p \cdot x + n \cdot r
```
missä $\Delta x$ on virheraja, $x$ lukema, $p$ valmistajan ilmoittama prosenttiosuus desimaalilukuna ($0{,}5\,\% = 0{,}005$), $n$ numeroiden määrä ja $r$ alueen resoluutio. Tulos kirjataan muodossa $x \pm \Delta x$, esimerkiksi $U = 4{,}50\,\text{V} \pm 0{,}04\,\text{V}$. Eri mittausten tarkkuutta verrataan **suhteellisella virherajalla**
```latex
\frac{\Delta x}{x}
```
joka on paljas luku ja ilmoitetaan yleensä prosentteina.

### Miksi pienin sopiva alue
Prosenttiosa $p \cdot x$ on sama kaikilla saman suureen alueilla, mutta numeroiden osuus $n \cdot r$ pienenee kymmenesosaan, kun siirrytään kymmenen kertaa pienemmälle alueelle. Kun lukema on pieni verrattuna alueeseen, numeroiden osuus hallitsee: $0{,}02\,\text{A}$:n virta alueella $10\,\text{A}$ on lähes arvaus, koska jo kolme viimeisen numeron askelta on $0{,}03\,\text{A}$.

<svg data-fig="error-bands" viewBox="0 0 600 312" role="img" aria-label="Kuva mittakaavassa: jännitteen akseli välillä 1,46 V–1,54 V. Ylempi jana näyttää alueella 20 V saadun lukeman 1,50 V ja sen virherajan ±0,028 V eli välin 1,472 V–1,528 V. Alempi jana näyttää alueella 2 V saadun lukeman 1,500 V ja sen virherajan ±0,0095 V eli välin 1,4905 V–1,5095 V. Alemman alueen jana on noin kolmasosa ylemmän pituudesta." style="max-width:100%;font-size:24px">
  <line x1="120" y1="40" x2="120" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="40" x2="180" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="40" x2="240" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="40" x2="300" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="40" x2="360" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="40" x2="420" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="40" x2="480" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="252" x2="554" y2="252" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,252 L553,258 L553,246 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="252" x2="60" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="31" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}46$</div></foreignObject>
  <line x1="120" y1="252" x2="120" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="252" x2="180" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="151" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}48$</div></foreignObject>
  <line x1="240" y1="252" x2="240" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="252" x2="300" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="271" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}50$</div></foreignObject>
  <line x1="360" y1="252" x2="360" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="252" x2="420" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="391" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}52$</div></foreignObject>
  <line x1="480" y1="252" x2="480" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="252" x2="540" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="511" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}54$</div></foreignObject>
  <foreignObject x="488" y="211.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="60" y="27.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{alue } 20\,\text{V}$</div></foreignObject>
  <rect x="135" y="66" width="330" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="135" y1="58" x2="135" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="465" y1="58" x2="465" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="78" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="477" y="63.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0{,}028\,\text{V}$</div></foreignObject>
  <foreignObject x="60" y="125.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{alue } 2\,\text{V}$</div></foreignObject>
  <rect x="243" y="164" width="114" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="243" y1="156" x2="243" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="357" y1="156" x2="357" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="176" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="369" y="161.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0{,}0095\,\text{V}$</div></foreignObject>
</svg>

## Esimerkki
Lampun jännite mitataan yleismittarilla kahdesti. Alueella $20\,\text{V}$ näyttö näyttää $1{,}50\,\text{V}$ ja alueella $2\,\text{V}$ näyttö näyttää $1{,}500\,\text{V}$. Kummankin alueen virheraja on $\pm(0{,}5\,\% + 2\ \text{numeroa})$. Kuinka suuri on lukeman virheraja kummallakin alueella, ja kumpi alue kannattaa valita?

<!-- vaihe -->

**Tunnetut ja kysytty.** Lukemat $U_{20} = 1{,}50\,\text{V}$ (resoluutio $r_{20} = 0{,}01\,\text{V}$) ja $U_2 = 1{,}500\,\text{V}$ (resoluutio $r_2 = 0{,}001\,\text{V}$), $p = 0{,}5\,\%$ ja $n = 2$. Kysytään virherajoja $\Delta U_{20}$ ja $\Delta U_2$.

<!-- vaihe -->

**Periaate.** Valmistajan virheraja on osuus lukemasta lisättynä kahdella viimeisen numeron askeleella. Lukema on molemmilla alueilla sama, joten alueet eroavat vain resoluutioltaan.

<!-- vaihe -->

**Kaava ratkaistuna.** Kaava antaa virherajan suoraan, kun resoluutioksi sijoitetaan kunkin alueen oma resoluutio:
```latex
\begin{aligned}
&\Delta U_{20} = p \cdot U_{20} + n \cdot r_{20} \\
&\Delta U_2 = p \cdot U_2 + n \cdot r_2
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Prosenttiosuus kirjoitetaan desimaalilukuna: $p = 0{,}5\,\% = 0{,}005$. Muita muunnoksia ei tarvita, koska lukemat ja resoluutiot ovat voltteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\Delta U_{20} \\
&= 0{,}005 \cdot 1{,}50\,\text{V} + 2 \cdot 0{,}01\,\text{V} \\
&= 0{,}0275\,\text{V} \\[6pt]
&\Delta U_2 \\
&= 0{,}005 \cdot 1{,}500\,\text{V} + 2 \cdot 0{,}001\,\text{V} \\
&= 0{,}0095\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Alueella $20\,\text{V}$ jännite on $1{,}50\,\text{V} \pm 0{,}028\,\text{V}$ ja alueella $2\,\text{V}$ $1{,}500\,\text{V} \pm 0{,}0095\,\text{V}$. Suhteelliset virherajat ovat $1{,}8\,\%$ ja $0{,}63\,\%$. Virherajat ilmoitetaan kahdella merkitsevällä numerolla, koska ne ovat arvioita. Alue $2\,\text{V}$ kannattaa valita: sen virheraja on noin kolmasosa.

<!-- vaihe -->

**Järkevyys.** Prosenttiosa on molemmilla alueilla sama, $0{,}0075\,\text{V}$. Ero tulee kokonaan numeroiden osuudesta, joka on alueella $20\,\text{V}$ kymmenkertainen, $0{,}02\,\text{V}$ eikä $0{,}002\,\text{V}$. Pienempi alue ei voi olla epätarkempi, kun lukema mahtuu sille ja alueiden prosenttiosa on sama.

## Yleinen virhekäsitys
Moni ajattelee, että suurin mittausalue on aina paras, koska sillä mittari ei mene yli alueen eikä sulake pala. Suurimmalta alueelta kannattaa kyllä aloittaa, kun suuruusluokkaa ei tiedetä, mutta lopullinen lukema luetaan pienimmältä alueelta, jolle arvo mahtuu. Suurella alueella viimeinen numero on karkea, ja pienen arvon virheraja voi olla yhtä suuri kuin itse lukema. Toinen yleinen virhe on kytkeä virtamittari komponentin rinnalle samaan tapaan kuin jännitemittari. Virtamittari kytketään aina sarjaan.

## Tiivistelmä
- Virtamittari kytketään sarjaan: piiri avataan ja mittari asetetaan aukkoon. Haarattomassa piirissä virta on joka kohdassa sama.
- Jännitemittari kytketään rinnalle eli niiden kahden pisteen väliin, joiden välinen jännite mitataan.
- Yleismittarin valitsimella valitaan suure ja mittausalue; OL tarkoittaa, että arvo on yli alueen. Musta johto kuuluu liittimeen COM.
- Mitataan pienimmällä alueella, jolle lukema mahtuu; tuntemattoman arvon mittaus aloitetaan suurimmalta alueelta.
- Virtamittarin resistanssi on hyvin pieni ja jännitemittarin hyvin suuri. Väärin kytkettynä virtamittari tekee oikosulun ja jännitemittari pysäyttää virran.
- Virheraja $\Delta x = p \cdot x + n \cdot r$ ja suhteellinen virheraja $\tfrac{\Delta x}{x}$.
