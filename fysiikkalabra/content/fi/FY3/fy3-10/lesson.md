# Ideaalikaasun tilanyhtälö pV = nRT

> **Miksi** heliumpallo on paljon kevyempi kuin samankokoinen ilmapallo? Onko siinä vähemmän kaasua?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: huoneessa kaksi samankokoista ilmapalloa. Heliumpallo on noussut kattoon ja sen naru roikkuu alas, tavallinen ilmalla täytetty pallo lepää lattialla." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy310h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="24" fill="#ffffff"/>
  <line x1="0" y1="24" x2="1200" y2="24" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="0" y="500" width="1200" height="100" fill="#c9c2b2"/>
  <line x1="0" y1="500" x2="1200" y2="500" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="0" y1="500" x2="-40" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="120" y1="500" x2="80" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="500" x2="200" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="360" y1="500" x2="320" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="480" y1="500" x2="440" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="500" x2="560" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="720" y1="500" x2="680" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="840" y1="500" x2="800" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="960" y1="500" x2="920" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1080" y1="500" x2="1040" y2="600" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="80" y="110" width="240" height="260" rx="4" fill="url(#fy310h-sky)" stroke="#1f2933" stroke-width="3"/>
  <path d="M135,210 Q134,193 154,195 Q162,177 182,183 Q200,173 210,192 Q228,194 226,210 Z" fill="#ffffff" stroke-linejoin="round"/>
  <line x1="200" y1="110" x2="200" y2="370" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="80" y1="240" x2="320" y2="240" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M560,218 Q476,182 480,112 Q486,30 560,28 Q634,30 640,112 Q644,182 560,218 Z" fill="#1971c2" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M550,230 L560,216 L570,230 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <ellipse cx="526" cy="78" rx="16" ry="26" transform="rotate(30 526 78)" fill="#ffffff" fill-opacity="0.8"/>
  <path d="M560,230 C540,300 590,360 560,420 S570,470 556,480" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M860,494 Q776,458 780,388 Q786,306 860,304 Q934,306 940,388 Q944,458 860,494 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M850,506 L860,492 L870,506 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <ellipse cx="826" cy="354" rx="16" ry="26" transform="rotate(30 826 354)" fill="#ffffff" fill-opacity="0.8"/>
  <ellipse cx="860" cy="500" rx="74" ry="10" fill="#6b7480" fill-opacity="0.35"/>
  <path d="M870,506 C900,520 940,512 990,522" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
</svg>

## Ydinajatus
Luvun *Kaasujen tilanmuutokset ja Boylen laki* kaasulait koskivat suljettua kaasumäärää. Nyt verrataan eri kaasumääriä ja eri kaasuja. Kun 5,00 litran pallo täytetään 101 kPa:n paineessa ja $20\,{}^\circ\text{C}$:n lämpötilassa vuorotellen heliumilla, typellä, ilmalla ja hiilidioksidilla, kaasujen massat ovat hyvin erilaiset: $0{,}83\,\text{g}$, $5{,}78\,\text{g}$, $6{,}02\,\text{g}$ ja $9{,}10\,\text{g}$. Kun kunkin massa jaetaan kaasun moolimassalla, tulos on kuitenkin joka kerta noin 0,207 mol. Samassa paineessa ja lämpötilassa yhtä suuressa tilavuudessa on siis yhtä paljon kaasua, olipa kaasu mitä tahansa. Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä, ei siksi, että kaasua olisi vähemmän.

<svg data-fig="helium-ilma" viewBox="0 0 600 326" role="img" aria-label="Havainnekuva, hiukkaset kuvattu suurennettuina: kaksi yhtä suurta kaasupalloa samassa paineessa ja lämpötilassa. Kummassakin on yhtä monta hiukkasta ja ainemäärä n = 0,21 mol. Heliumpallon kaasun massa on m = 0,83 g ja ilmapallon m = 6,0 g, koska ilman hiukkaset ovat raskaampia. Nuolet näyttävät hiukkasten liikkeen mittakaavassa: kevyet heliumhiukkaset liikkuvat samassa lämpötilassa nopeammin, nuolen pituus on nopeuden suhde 2,7 : 1." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy310-glass" cx="0.38" cy="0.32" r="0.8"><stop offset="0" stop-color="#ffffff"/><stop offset="0.7" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></radialGradient></defs>
  <circle cx="150" cy="108" r="86" fill="url(#fy310-glass)" stroke="#1f2933" stroke-width="3"/>
  <path d="M141,206 L159,206 L150,194 Z" fill="#1f2933" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M150,206 q -9,9 0,18" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M98,56 a 72,72 0 0 1 40,-26" fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.9"/>
  <circle cx="114" cy="114" r="5.5" fill="#1971c2"/>
  <circle cx="112.5" cy="112.5" r="1.65" fill="#ffffff"/>
  <line x1="121.5" y1="114" x2="145.5" y2="114" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M153.5,114 L144.5,118 L144.5,110 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="167" cy="48.5" r="5.5" fill="#1971c2"/>
  <circle cx="165.5" cy="47" r="1.65" fill="#ffffff"/>
  <line x1="161.5" y1="53.5" x2="144" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M138,75 L142,66 L147.5,72 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="117" cy="71.5" r="5.5" fill="#1971c2"/>
  <circle cx="115.5" cy="70" r="1.65" fill="#ffffff"/>
  <line x1="122.5" y1="66.5" x2="139.5" y2="49.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M145,43.5 L141.5,53 L135.5,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="218" cy="104" r="5.5" fill="#1971c2"/>
  <circle cx="216.5" cy="102.5" r="1.65" fill="#ffffff"/>
  <line x1="217.5" y1="111.5" x2="216.5" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M216,143.5 L212.5,134 L220.5,134.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="168.5" cy="158.5" r="5.5" fill="#1971c2"/>
  <circle cx="167" cy="157" r="1.65" fill="#ffffff"/>
  <line x1="161" y1="157" x2="137.5" y2="153" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M129.5,151.5 L139,149 L137.5,157 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="153" cy="141" r="5.5" fill="#1971c2"/>
  <circle cx="151.5" cy="139.5" r="1.65" fill="#ffffff"/>
  <line x1="159.5" y1="137" x2="179.5" y2="124" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M186.5,119.5 L181,128 L176.5,121 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="185.5" cy="120.5" r="5.5" fill="#1971c2"/>
  <circle cx="183.5" cy="119" r="1.65" fill="#ffffff"/>
  <line x1="183.5" y1="127.5" x2="177.5" y2="151" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M175.5,158.5 L173.5,149 L181.5,151 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="142.5" cy="167.5" r="5.5" fill="#1971c2"/>
  <circle cx="141" cy="166" r="1.65" fill="#ffffff"/>
  <line x1="139" y1="161" x2="127.5" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M124,132.5 L132,139 L124.5,142.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="167.5" cy="80.5" r="5.5" fill="#1971c2"/>
  <circle cx="165.5" cy="79" r="1.65" fill="#ffffff"/>
  <line x1="174.5" y1="83.5" x2="197" y2="91.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M204.5,94 L194.5,95 L197.5,87 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="120.5" cy="48" r="5.5" fill="#1971c2"/>
  <circle cx="119" cy="46.5" r="1.65" fill="#ffffff"/>
  <line x1="128" y1="48" x2="152" y2="47" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M160,46.5 L151,51 L151,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="122" cy="145" r="5.5" fill="#1971c2"/>
  <circle cx="120" cy="143" r="1.65" fill="#ffffff"/>
  <line x1="125" y1="138" x2="135" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M138,109 L138,119 L130.5,115.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="144.5" cy="110.5" r="5.5" fill="#1971c2"/>
  <circle cx="143" cy="109" r="1.65" fill="#ffffff"/>
  <line x1="147" y1="118" x2="154.5" y2="140.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M157,148.5 L150,141 L158,138.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="108.5" y="217.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{helium}$</div></foreignObject>
  <foreignObject x="83.5" y="249.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 0{,}21\,\text{mol}$</div></foreignObject>
  <foreignObject x="96" y="281.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = 0{,}83\,\text{g}$</div></foreignObject>
  <circle cx="450" cy="108" r="86" fill="url(#fy310-glass)" stroke="#1f2933" stroke-width="3"/>
  <path d="M441,206 L459,206 L450,194 Z" fill="#1f2933" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M450,206 q -9,9 0,18" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M398,56 a 72,72 0 0 1 40,-26" fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.9"/>
  <circle cx="466" cy="140" r="8" fill="#6c757d"/>
  <circle cx="464" cy="137.5" r="2.4" fill="#ffffff"/>
  <line x1="476" y1="140" x2="480" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M488,140 L479,144 L479,136 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="481.5" cy="163.5" r="8" fill="#6c757d"/>
  <circle cx="479.5" cy="161.5" r="2.4" fill="#ffffff"/>
  <line x1="474.5" y1="170.5" x2="471.5" y2="173" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M465.5,178.5 L469.5,169.5 L475,175.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="388" cy="103.5" r="8" fill="#6c757d"/>
  <circle cx="385.5" cy="101" r="2.4" fill="#ffffff"/>
  <line x1="388.5" y1="93.5" x2="389" y2="89.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M389.5,81.5 L393,91 L385,90 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="508.5" cy="127.5" r="8" fill="#6c757d"/>
  <circle cx="506" cy="125.5" r="2.4" fill="#ffffff"/>
  <line x1="508" y1="137.5" x2="508" y2="141.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M507.5,149.5 L504,140.5 L512,141 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="446" cy="74.5" r="8" fill="#6c757d"/>
  <circle cx="443.5" cy="72" r="2.4" fill="#ffffff"/>
  <line x1="436" y1="73" x2="432" y2="72" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M424,71 L434,68.5 L432.5,76.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="421" cy="163" r="8" fill="#6c757d"/>
  <circle cx="418.5" cy="160.5" r="2.4" fill="#ffffff"/>
  <line x1="429.5" y1="157.5" x2="432.5" y2="155.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M439.5,151 L434,159.5 L429.5,152.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="485" cy="63" r="8" fill="#6c757d"/>
  <circle cx="482.5" cy="60.5" r="2.4" fill="#ffffff"/>
  <line x1="482.5" y1="72.5" x2="481.5" y2="76.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M479.5,84.5 L478,74.5 L485.5,76.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="411.5" cy="70.5" r="8" fill="#6c757d"/>
  <circle cx="409" cy="68" r="2.4" fill="#ffffff"/>
  <line x1="407" y1="61.5" x2="405" y2="58" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M401.5,51 L409,57 L402,61 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="424" cy="121.5" r="8" fill="#6c757d"/>
  <circle cx="421.5" cy="119" r="2.4" fill="#ffffff"/>
  <line x1="433" y1="125" x2="437" y2="126.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M444.5,129 L434.5,130 L437.5,122 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="398.5" cy="141" r="8" fill="#6c757d"/>
  <circle cx="396" cy="138.5" r="2.4" fill="#ffffff"/>
  <line x1="393" y1="132.5" x2="390.5" y2="129" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M386.5,122.5 L394.5,127.5 L388,132 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="452.5" cy="112" r="8" fill="#6c757d"/>
  <circle cx="450" cy="109.5" r="2.4" fill="#ffffff"/>
  <line x1="456.5" y1="103" x2="458" y2="99" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M461.5,92 L461.5,101.5 L454,98.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="433.5" cy="47" r="8" fill="#6c757d"/>
  <circle cx="431" cy="44.5" r="2.4" fill="#ffffff"/>
  <line x1="436.5" y1="56.5" x2="437.5" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M440,67.5 L433.5,60.5 L441,58 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="421" y="217.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="383.5" y="249.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 0{,}21\,\text{mol}$</div></foreignObject>
  <foreignObject x="402.5" y="281.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = 6{,}0\,\text{g}$</div></foreignObject>
  <foreignObject x="271" y="93.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{sama}$</div></foreignObject>
  <foreignObject x="275.5" y="123.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$p,\ T$</div></foreignObject>
</svg>

Hiukkasia on pienessäkin kaasumäärässä valtavasti, joten niitä ei lasketa yksitellen vaan mooleina, samaan tapaan kuin kananmunia lasketaan tusinoina. Yksi mooli on $6{,}022 \cdot 10^{23}$ hiukkasta, ja lukua $N_\text{A} = 6{,}022 \cdot 10^{23}\,\text{1/mol}$ sanotaan Avogadron vakioksi. Ainemäärä $n$ kertoo, montako moolia hiukkasia on. Yhden moolin massa on aineen moolimassa $M$: heliumilla $4{,}00\,\text{g/mol}$, ilmalla keskimäärin $29{,}0\,\text{g/mol}$ ja hiilidioksidilla $44{,}0\,\text{g/mol}$. Ainemäärä saadaan siis sekä hiukkasmäärästä että massasta:
```latex
n = \frac{N}{N_\text{A}} = \frac{m}{M}
```
missä $N$ on hiukkasten lukumäärä, $m$ massa (g tai kg) ja $M$ moolimassa (g/mol tai kg/mol).

<svg data-fig="mole-masses" viewBox="0 0 600 316" role="img" aria-label="Havainnekuva, hiukkaset suurennettuina ja kaavamaisina: kolme yhtä suurta astiaa samassa paineessa ja lämpötilassa, kussakin yhtä monta hiukkasta eli ainemäärä n = 1,00 mol. Moolimassa on heliumilla 4,00 g/mol, ilmalla 29,0 g/mol ja hiilidioksidilla 44,0 g/mol. Palkki jokaisen astian alla on kaasun massa mittakaavassa: yksi mooli painaa eri kaasuilla eri verran." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy310-jar" cx="0.38" cy="0.32" r="0.8"><stop offset="0" stop-color="#ffffff"/><stop offset="0.7" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></radialGradient></defs>
  <rect x="14" y="20" width="130" height="124" rx="8" fill="url(#fy310-jar)" stroke="#1f2933" stroke-width="3"/>
  <circle cx="45.5" cy="111.5" r="5.5" fill="#1971c2"/>
  <circle cx="44" cy="110" r="1.65" fill="#ffffff"/>
  <circle cx="103" cy="61" r="5.5" fill="#1971c2"/>
  <circle cx="101.5" cy="59.5" r="1.65" fill="#ffffff"/>
  <circle cx="78.5" cy="77.5" r="5.5" fill="#1971c2"/>
  <circle cx="77" cy="76" r="1.65" fill="#ffffff"/>
  <circle cx="93" cy="106.5" r="5.5" fill="#1971c2"/>
  <circle cx="91" cy="105" r="1.65" fill="#ffffff"/>
  <circle cx="42" cy="42" r="5.5" fill="#1971c2"/>
  <circle cx="40.5" cy="40.5" r="1.65" fill="#ffffff"/>
  <circle cx="103" cy="39.5" r="5.5" fill="#1971c2"/>
  <circle cx="101" cy="38" r="1.65" fill="#ffffff"/>
  <circle cx="74" cy="101" r="5.5" fill="#1971c2"/>
  <circle cx="72.5" cy="99" r="1.65" fill="#ffffff"/>
  <circle cx="36" cy="85.5" r="5.5" fill="#1971c2"/>
  <circle cx="34" cy="84" r="1.65" fill="#ffffff"/>
  <foreignObject x="14" y="153.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{helium}$</div></foreignObject>
  <foreignObject x="14" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 4{,}00\,\text{g/mol}$</div></foreignObject>
  <rect x="14" y="222" width="14" height="14" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="14" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 4{,}00\,\text{g}$</div></foreignObject>
  <rect x="214" y="20" width="130" height="124" rx="8" fill="url(#fy310-jar)" stroke="#1f2933" stroke-width="3"/>
  <circle cx="318" cy="118" r="8" fill="#6c757d"/>
  <circle cx="316" cy="115.5" r="2.4" fill="#ffffff"/>
  <circle cx="241" cy="49" r="8" fill="#6c757d"/>
  <circle cx="238.5" cy="46.5" r="2.4" fill="#ffffff"/>
  <circle cx="293.5" cy="66.5" r="8" fill="#6c757d"/>
  <circle cx="291" cy="64.5" r="2.4" fill="#ffffff"/>
  <circle cx="288" cy="90.5" r="8" fill="#6c757d"/>
  <circle cx="285.5" cy="88" r="2.4" fill="#ffffff"/>
  <circle cx="317.5" cy="85.5" r="8" fill="#6c757d"/>
  <circle cx="315" cy="83" r="2.4" fill="#ffffff"/>
  <circle cx="268.5" cy="113.5" r="8" fill="#6c757d"/>
  <circle cx="266.5" cy="111" r="2.4" fill="#ffffff"/>
  <circle cx="318.5" cy="55" r="8" fill="#6c757d"/>
  <circle cx="316.5" cy="52.5" r="2.4" fill="#ffffff"/>
  <circle cx="263" cy="58.5" r="8" fill="#6c757d"/>
  <circle cx="260.5" cy="56" r="2.4" fill="#ffffff"/>
  <foreignObject x="214" y="153.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="214" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 29{,}0\,\text{g/mol}$</div></foreignObject>
  <rect x="214" y="222" width="101.5" height="14" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="214" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 29{,}0\,\text{g}$</div></foreignObject>
  <rect x="414" y="20" width="130" height="124" rx="8" fill="url(#fy310-jar)" stroke="#1f2933" stroke-width="3"/>
  <circle cx="457.5" cy="85.5" r="9.5" fill="#b8622d"/>
  <circle cx="454.5" cy="82.5" r="2.85" fill="#ffffff"/>
  <circle cx="489.5" cy="48.5" r="9.5" fill="#b8622d"/>
  <circle cx="486.5" cy="45.5" r="2.85" fill="#ffffff"/>
  <circle cx="438.5" cy="108" r="9.5" fill="#b8622d"/>
  <circle cx="435.5" cy="105" r="2.85" fill="#ffffff"/>
  <circle cx="520" cy="79.5" r="9.5" fill="#b8622d"/>
  <circle cx="517.5" cy="77" r="2.85" fill="#ffffff"/>
  <circle cx="490" cy="110.5" r="9.5" fill="#b8622d"/>
  <circle cx="487.5" cy="107.5" r="2.85" fill="#ffffff"/>
  <circle cx="462.5" cy="46" r="9.5" fill="#b8622d"/>
  <circle cx="459.5" cy="43" r="2.85" fill="#ffffff"/>
  <circle cx="489.5" cy="79.5" r="9.5" fill="#b8622d"/>
  <circle cx="486.5" cy="76.5" r="2.85" fill="#ffffff"/>
  <circle cx="518.5" cy="109.5" r="9.5" fill="#b8622d"/>
  <circle cx="515.5" cy="106.5" r="2.85" fill="#ffffff"/>
  <foreignObject x="414" y="153.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hiilidioksidi}$</div></foreignObject>
  <foreignObject x="414" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 44{,}0\,\text{g/mol}$</div></foreignObject>
  <rect x="414" y="222" width="154" height="14" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="414" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 44{,}0\,\text{g}$</div></foreignObject>
  <foreignObject x="20" y="281.5" width="560" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kussakin astiassa }n = 1{,}00\,\text{mol},\ \text{sama }p, T$</div></foreignObject>
</svg>

Ideaalikaasu on mikromalli. Siinä hiukkaset ajatellaan pistemäisiksi, ja ne vaikuttavat toisiinsa ja astian seinämiin vain törmätessään. Siksi hiukkasten välisten vuorovaikutusten energia on mallissa merkityksetön, ja kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan. Paine syntyy seinämiin osuvista törmäyksistä, ja se kasvaa, kun hiukkasia on enemmän, kun ne liikkuvat nopeammin eli lämpötila on korkeampi tai kun tilavuus on pienempi. Todelliset kaasut noudattavat mallia hyvin tavallisissa oloissa. Malli alkaa pettää suurissa paineissa ja matalissa lämpötiloissa, kun hiukkaset ovat lähellä toisiaan ja niiden välinen vetovoima tiivistää kaasun nesteeksi.

## Kaava: Ideaalikaasun tilanyhtälö
Punnitustuloksesta saadaan luku, joka on kaikille kaasuille sama: paine kerrottuna tilavuudella ja jaettuna ainemäärällä ja kelvinlämpötilalla. Neljän kaasun keskimääräisellä ainemäärällä 0,2071 mol se on
```latex
\begin{aligned}
R &= \frac{pV}{nT} \\
&= \frac{101\,000\,\text{Pa} \cdot 0{,}00500\,\text{m}^3}{0{,}2071\,\text{mol} \cdot 293{,}15\,\text{K}} \\
&\approx 8{,}3\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}
\end{aligned}
```
Tarkat mittaukset antavat kaikille kaasuille arvon $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$, kun paine ei ole kovin suuri eikä lämpötila kovin matala. Lukua sanotaan mooliseksi kaasuvakioksi. Siitä saadaan ideaalikaasun tilanyhtälö
```latex
pV = nRT
```
missä $p$ on paine (Pa), $V$ tilavuus (m³), $n$ ainemäärä (mol), $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ moolinen kaasuvakio ja $T$ lämpötila kelvineinä (K). Kaasun laatu ei näy yhtälössä lainkaan. Celsiusasteina annettu lämpötila $\theta$ muutetaan kelvineiksi lisäämällä lukuarvoon 273,15. Paine on aina kokonaispaine pascaleina ja tilavuus kuutiometreinä, koska $R$:n yksikössä on joule: 1 Pa · m³ = 1 N/m² · m³ = 1 N · m = $1\,\text{J}$.

Kun tilanyhtälö ratkaistaan paineen suhteen, nähdään, että paine kaksinkertaistuu, kun hiukkasten lukumäärä tai kelvinlämpötila kaksinkertaistuu tai kun tilavuus puolittuu. Paine on siis suoraan verrannollinen hiukkasten lukumäärään ja kelvinlämpötilaan ja kääntäen verrannollinen tilavuuteen, eli $p \propto NT/V$.

<svg data-fig="paine-ja-tekijat" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva neljästä männällä suljetusta kaasusylinteristä, hiukkaset suurennettuina. Vasemmalta oikealle: lähtötilassa hiukkasmäärä N, lämpötila T ja tilavuus V, ja paine on p. Paine on 2p, kun hiukkasia on kaksi kertaa enemmän (2N), kun kelvinlämpötila on kaksinkertainen (2T) eli hiukkaset liikkuvat nopeammin, tai kun mäntä on painettu puoleen tilavuuteen (V/2). Nuolten pituus kuvaa hiukkasten nopeutta." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy310-gas" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d0e6fb"/><stop offset="0.35" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy310-piston" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="20" y="46" width="110" height="150" fill="url(#fy310-gas)"/>
  <path d="M20,36 V196 H130 V36" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="23" y="36" width="104" height="10" rx="2" fill="url(#fy310-piston)" stroke="#1f2933" stroke-width="2"/>
  <rect x="71" y="16" width="8" height="20" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="81" cy="113" r="6" fill="#6c757d"/>
  <circle cx="79" cy="111" r="1.8" fill="#ffffff"/>
  <line x1="89" y1="113" x2="95" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M103,113 L94,117 L94,109 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="101.5" cy="158" r="6" fill="#6c757d"/>
  <circle cx="99.5" cy="156" r="1.8" fill="#ffffff"/>
  <line x1="95.5" y1="163.5" x2="91" y2="167.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M85,173 L89,163.5 L94.5,169.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="88" cy="82.5" r="6" fill="#6c757d"/>
  <circle cx="86" cy="80.5" r="1.8" fill="#ffffff"/>
  <line x1="88.5" y1="74.5" x2="89" y2="68.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M90,60.5 L93,69.5 L85,69 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="54" cy="172.5" r="6" fill="#6c757d"/>
  <circle cx="52" cy="171" r="1.8" fill="#ffffff"/>
  <line x1="46" y1="173.5" x2="40" y2="174.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M32,175.5 L40.5,170.5 L41.5,178.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="116.5" cy="69" r="6" fill="#6c757d"/>
  <circle cx="115" cy="67.5" r="1.8" fill="#ffffff"/>
  <line x1="109" y1="67.5" x2="103" y2="66.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M95,65.5 L104.5,63 L103,71 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="33.5" cy="79.5" r="6" fill="#6c757d"/>
  <circle cx="31.5" cy="77.5" r="1.8" fill="#ffffff"/>
  <line x1="40" y1="75" x2="45" y2="71.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M52,67.5 L46.5,75.5 L42,69 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="36" y="211.5" width="78" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ T,\ V$</div></foreignObject>
  <foreignObject x="65" y="251.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p$</div></foreignObject>
  <rect x="170" y="46" width="110" height="150" fill="url(#fy310-gas)"/>
  <path d="M170,36 V196 H280 V36" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="173" y="36" width="104" height="10" rx="2" fill="url(#fy310-piston)" stroke="#1f2933" stroke-width="2"/>
  <rect x="221" y="16" width="8" height="20" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="221" cy="128" r="6" fill="#6c757d"/>
  <circle cx="219" cy="126" r="1.8" fill="#ffffff"/>
  <line x1="229" y1="128" x2="235" y2="128" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M243,128 L234,132 L234,124 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="260.5" cy="117" r="6" fill="#6c757d"/>
  <circle cx="259" cy="115.5" r="1.8" fill="#ffffff"/>
  <line x1="254.5" y1="122.5" x2="250.5" y2="126.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M244.5,132 L248.5,123 L254,129 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="198.5" cy="122.5" r="6" fill="#6c757d"/>
  <circle cx="196.5" cy="120.5" r="1.8" fill="#ffffff"/>
  <line x1="199" y1="114.5" x2="199.5" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M200.5,100.5 L203.5,110 L195.5,109 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="236" cy="154.5" r="6" fill="#6c757d"/>
  <circle cx="234" cy="152.5" r="1.8" fill="#ffffff"/>
  <line x1="241" y1="160.5" x2="244.5" y2="165.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M249.5,172 L240.5,167 L247,162 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="191" cy="98.5" r="6" fill="#6c757d"/>
  <circle cx="189" cy="97" r="1.8" fill="#ffffff"/>
  <line x1="191" y1="90.5" x2="191" y2="84.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M191,76.5 L195,85.5 L187,85.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="190.5" cy="156.5" r="6" fill="#6c757d"/>
  <circle cx="189" cy="154.5" r="1.8" fill="#ffffff"/>
  <line x1="197.5" y1="152" x2="202.5" y2="148.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M209,144.5 L203.5,152.5 L199.5,146 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="241" cy="69" r="6" fill="#6c757d"/>
  <circle cx="239.5" cy="67" r="1.8" fill="#ffffff"/>
  <line x1="239" y1="76.5" x2="237.5" y2="82.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M235.5,90 L234,80.5 L242,82.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="265.5" cy="174" r="6" fill="#6c757d"/>
  <circle cx="263.5" cy="172" r="1.8" fill="#ffffff"/>
  <line x1="262" y1="167" x2="259" y2="161.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M255,154.5 L263,160.5 L256,164.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="196" cy="65.5" r="6" fill="#6c757d"/>
  <circle cx="194.5" cy="64" r="1.8" fill="#ffffff"/>
  <line x1="204" y1="68.5" x2="209.5" y2="70.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M217,73 L207,74 L210,66.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="221.5" cy="95.5" r="6" fill="#6c757d"/>
  <circle cx="219.5" cy="94" r="1.8" fill="#ffffff"/>
  <line x1="214" y1="99" x2="208.5" y2="101" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M201,104.5 L208,97 L211,104.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="248.5" cy="95" r="6" fill="#6c757d"/>
  <circle cx="246.5" cy="93" r="1.8" fill="#ffffff"/>
  <line x1="251.5" y1="87.5" x2="254" y2="82" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M257.5,74.5 L257.5,84.5 L250,81 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="264" cy="150.5" r="6" fill="#6c757d"/>
  <circle cx="262" cy="148.5" r="1.8" fill="#ffffff"/>
  <line x1="266.5" y1="158" x2="268.5" y2="163.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M271,171.5 L264,164 L272,161.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="180" y="211.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2N,\ T,\ V$</div></foreignObject>
  <foreignObject x="208.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
  <rect x="320" y="46" width="110" height="150" fill="url(#fy310-gas)"/>
  <path d="M320,36 V196 H430 V36" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="323" y="36" width="104" height="10" rx="2" fill="url(#fy310-piston)" stroke="#1f2933" stroke-width="2"/>
  <rect x="371" y="16" width="8" height="20" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="373" cy="139" r="6" fill="#6c757d"/>
  <circle cx="371" cy="137" r="1.8" fill="#ffffff"/>
  <line x1="381" y1="139" x2="392.5" y2="139" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M400.5,139 L391.5,143 L391.5,135 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="389" cy="80.5" r="6" fill="#6c757d"/>
  <circle cx="387" cy="78.5" r="1.8" fill="#ffffff"/>
  <line x1="383" y1="85.5" x2="374.5" y2="93.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M368.5,99 L372.5,90 L378,96 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="334" cy="106.5" r="6" fill="#6c757d"/>
  <circle cx="332" cy="105" r="1.8" fill="#ffffff"/>
  <line x1="334.5" y1="99" x2="335.5" y2="87" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M336.5,79 L339.5,88.5 L331.5,87.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="346.5" cy="167.5" r="6" fill="#6c757d"/>
  <circle cx="345" cy="165.5" r="1.8" fill="#ffffff"/>
  <line x1="344.5" y1="159.5" x2="341" y2="148.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M338.5,140.5 L345,148 L337,150.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="416" cy="172" r="6" fill="#6c757d"/>
  <circle cx="414" cy="170" r="1.8" fill="#ffffff"/>
  <line x1="408" y1="170.5" x2="396.5" y2="168.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M388.5,167 L398,164.5 L396.5,172.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="415" cy="139.5" r="6" fill="#6c757d"/>
  <circle cx="413" cy="138" r="1.8" fill="#ffffff"/>
  <line x1="415.5" y1="147.5" x2="416" y2="159.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M416,167.5 L412,158.5 L420,158.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="330" y="211.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ 2T,\ V$</div></foreignObject>
  <foreignObject x="358.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
  <rect x="470" y="121" width="110" height="75" fill="url(#fy310-gas)"/>
  <path d="M470,36 V196 H580 V36" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="473" y="111" width="104" height="10" rx="2" fill="url(#fy310-piston)" stroke="#1f2933" stroke-width="2"/>
  <rect x="521" y="91" width="8" height="20" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="505" cy="165.5" r="6" fill="#6c757d"/>
  <circle cx="503" cy="164" r="1.8" fill="#ffffff"/>
  <line x1="513" y1="165.5" x2="519" y2="165.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M527,165.5 L518,170 L518,161.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="540.5" cy="172" r="6" fill="#6c757d"/>
  <circle cx="538.5" cy="170.5" r="1.8" fill="#ffffff"/>
  <line x1="534.5" y1="177.5" x2="530" y2="181.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M524.5,187 L528,178 L533.5,184 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="544.5" cy="144" r="6" fill="#6c757d"/>
  <circle cx="543" cy="142.5" r="1.8" fill="#ffffff"/>
  <line x1="552.5" y1="143.5" x2="558.5" y2="143" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M566.5,142 L558,147 L557.5,139 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="484" cy="150" r="6" fill="#6c757d"/>
  <circle cx="482.5" cy="148" r="1.8" fill="#ffffff"/>
  <line x1="489" y1="156" x2="493" y2="161" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M497.5,167 L489,162.5 L495.5,157.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="562.5" cy="170" r="6" fill="#6c757d"/>
  <circle cx="561" cy="168" r="1.8" fill="#ffffff"/>
  <line x1="555" y1="168.5" x2="549" y2="167.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M541,166 L550.5,164 L549,171.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="509.5" cy="143.5" r="6" fill="#6c757d"/>
  <circle cx="507.5" cy="142" r="1.8" fill="#ffffff"/>
  <line x1="516" y1="139.5" x2="521" y2="136" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M528,131.5 L522.5,140 L518,133 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="470" y="46" width="110" height="75" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-dasharray="6 5"/>
  <foreignObject x="473.5" y="211.5" width="103" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ T,\ V/2$</div></foreignObject>
  <foreignObject x="508.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
</svg>

Simulaatiossa voit tutkia tätä hiukkasten tasolla: muuta hiukkasten määrää, lämpötilaa ja tilavuutta ja vertaa seinämistä mitattua painetta tilanyhtälön ennusteeseen, jonka lasket itse. Hiukkasten keskinäiset törmäykset eivät muuta painetta keskimäärin, joten ne on jätetty simulaatiosta pois. Simulaatiossa paine näytetään suhteessa vertailutilaan ($p/p_\text{ref}$), ei pascaleina. Vertailutila on $N = 100$ hiukkasta, $T = 300\,\text{K}$ ja koko tilavuus ($V = 100\,\%$); siinä $p/p_\text{ref} = 1$, ja arvo 2 tarkoittaa kaksinkertaista vertailupaineeseen verrattuna. Hiukkasmäärä $N$ kuvaa kaasun määrää.

<!-- sim -->

Kun kaasun määrä ei muutu, $nR$ on vakio, ja tilanyhtälöstä seuraa yhdistetty kaasulaki $p_1V_1/T_1 = p_2V_2/T_2$ (alaindeksit 1 ja 2 ovat alku- ja lopputila). Siitä saadaan jokainen luvun *Kaasujen tilanmuutokset ja Boylen laki* kaasulaki, kun yksi suure pidetään vakiona.

## Esimerkki
Juhlapallo täytetään heliumilla, kunnes sen tilavuus on $5{,}0\,\textsf{l}$. Pallossa paine on 101 kPa ja lämpötila $20\,{}^\circ\text{C}$. Kuinka monta moolia heliumia pallossa on, ja mikä on heliumin massa? Heliumin moolimassa on $4{,}0\,\text{g/mol}$.

<!-- vaihe -->

**Tunnetut ja kysytty.** Pallon tilavuus $V = 5{,}0\,\textsf{l}$, paine $p = 101\,\text{kPa}$, lämpötila $\theta = 20\,{}^\circ\text{C}$ ja heliumin moolimassa $M = 4{,}0\,\text{g/mol}$. Kysytään ainemäärää $n$ ja massaa $m$.

<!-- vaihe -->

**Periaate.** Pallossa on tietty määrä heliumia tietyssä tilavuudessa, paineessa ja lämpötilassa, ja helium käyttäytyy tavallisessa paineessa ja huoneenlämmössä ideaalikaasuna. Siksi tilanyhtälö $pV = nRT$ antaa ainemäärän, ja moolimassa muuttaa ainemäärän massaksi.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan tilanyhtälöstä ainemäärä ja yhtälöstä $n = m/M$ massa:
```latex
\begin{aligned}
n &= \frac{pV}{RT} \\
m &= nM
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Tilanyhtälö vaatii perusyksiköt:

- tilavuus $V = 5{,}0\,\textsf{l} = 0{,}0050\,\text{m}^3$
- paine $p = 101\,\text{kPa} = 101\,000\,\text{Pa}$
- lämpötila $T = (20 + 273{,}15)\,\text{K} = 293{,}15\,\text{K}$
- moolimassa jää arvoon $M = 4{,}0\,\text{g/mol}$, jolloin massa tulee grammoina

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
n &= \frac{pV}{RT} \\
&= \frac{101\,000\,\text{Pa} \cdot 0{,}0050\,\text{m}^3}{8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 293{,}15\,\text{K}} \\
&= 0{,}2073\,\text{mol} \approx 0{,}21\,\text{mol}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Heliumin massa lasketaan tarkemmalla ainemäärällä:
```latex
\begin{aligned}
m &= nM \\
&= 0{,}2073\,\text{mol} \cdot 4{,}0\,\text{g/mol} \\
&\approx 0{,}83\,\text{g}
\end{aligned}
```
Pallossa on 0,21 mol heliumia, ja sen massa on $0{,}83\,\text{g}$. Ainemäärän rajoittaa tilavuus $5{,}0\,\textsf{l}$ ja massan lisäksi moolimassa $4{,}0\,\text{g/mol}$, kumpikin kaksi numeroa, joten tulokset annetaan kahdella merkitsevällä numerolla. Paine 101 kPa ja lämpötila $293\,\text{K}$ ovat kolmen numeron arvoja eivätkä rajoita.

<!-- vaihe -->

**Järkevyys.** Yksi mooli kaasua vie huoneenlämmössä ja normaalipaineessa noin 24 litraa, joten 5,0 litrassa on noin 5,0/24 ≈ 0,21 mol kaasua. Samankokoisessa ilmapallossa on yhtä monta moolia ilmaa, mutta sen massa on noin 0,2073 mol · $29\,\text{g/mol}$ ≈ $6{,}0\,\text{g}$. Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä, ei siksi, että kaasua olisi vähemmän.

## Yleinen virhekäsitys
Tilanyhtälön laskuissa toistuu kolme virhettä:

- **Celsiusasteet.** Lämpötila on tilanyhtälössä aina kelvineinä. Esimerkiksi $0\,{}^\circ\text{C}$ antaisi paineeksi nollan, mutta kaasulla on paine myös jäätymispisteessä.
- **Sekoitetut yksiköt.** Jos paine on kilopascaleina mutta tilavuus kuutiometreinä tai paine pascaleina mutta tilavuus litroina, tulos on tuhatkertaisesti väärä. Varminta on muuttaa kaikki suureet perusyksiköiksi: paine pascaleiksi, tilavuus kuutiometreiksi ja lämpötila kelvineiksi.
- **Raskas kaasu.** Moni ajattelee, että raskaampaa kaasua mahtuu samaan tilavuuteen vähemmän moolia. Ainemäärä riippuu kuitenkin vain paineesta, tilavuudesta ja lämpötilasta, ei kaasun laadusta. Massa sen sijaan riippuu moolimassasta.

## Tiivistelmä
- Ideaalikaasun tilanyhtälö on $pV = nRT$, missä $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ ja $T$ on kelvineinä.
- Ainemäärä $n$ kertoo kaasun määrän mooleina: $n = N/N_\text{A} = m/M$.
- Paine on verrannollinen lausekkeeseen $NT/V$: paine kaksinkertaistuu, kun hiukkasmäärä tai kelvinlämpötila kaksinkertaistuu tai kun tilavuus puolittuu.
- Kun kaasun määrä pysyy samana, $p_1V_1/T_1 = p_2V_2/T_2$, ja siitä saadaan erilliset kaasulait.
- Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua, kaasun laadusta riippumatta; punnitus antaa kaikille kaasuille saman $m/M$.
- Ideaalikaasumalli toimii hyvin tavallisissa oloissa ja pettää suurissa paineissa ja matalissa lämpötiloissa.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: kuumailmapallo leijuu järven yllä. Korin yläpuolella palava liekki lämmittää pallon sisällä olevaa ilmaa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy310s-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy310s-lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="280" fill="url(#fy310s-sky)"/>
  <path d="M56,92 Q55,71.5 79,74 Q88.5,52.5 112.5,59.5 Q134,47.5 146,70.5 Q167.5,73 165,92 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,270 L7,254 L14.5,270 L22,253.5 L29,270 L38.5,248 L47.5,270 L56.5,248.5 L65.5,270 L78,237 L91,270 L101,244.5 L111.5,270 L122,244 L132,270 L142.5,244 L153,270 L163.5,244 L174,270 L184.5,244 L194.5,270 L204,247.5 L213,270 L225.5,237.5 L238,270 L250,239.5 L262,270 L270,251 L278.5,270 L290,240.5 L301.5,270 L312.5,242.5 L323.5,270 L336,237 L349,270 L358.5,246 L368,270 L381,237.5 L393.5,270 L403.5,245.5 L413.5,270 L423.5,245 L433.5,270 L443.5,245.5 L453.5,270 L461.5,253 L469,270 L476.5,253 L484,270 L493.5,247 L503,270 L515,238.5 L527.5,270 L538,244 L548,270 L556,252 L564,270 L574.5,244.5 L584.5,270 L596,240.5 L608,270 L615,254.5 L622,270 L632.5,243 L643.5,270 L650.5,254 L658,270 L667.5,247.5 L676.5,270 L685,251 L693,270 L704.5,241 L715.5,270 L727,241 L738.5,270 L750.5,239.5 L762,270 L772,246 L781.5,270 L791.5,246.5 L801,270 L810.5,246.5 L820,270 L829.5,247 L839,270 L846.5,253 L854.5,270 L864.5,245.5 L874.5,270 L884,245.5 L894,270 L907,237 L919.5,270 L928,250 L936.5,270 L949,236.5 L962,270 L973,242.5 L984,270 L995.5,240.5 L1007,270 L1017.5,243 L1028.5,270 L1038,247.5 L1047.5,270 L1057,246.5 L1066.5,270 L1074.5,252.5 L1082,270 L1091.5,247.5 L1100.5,270 L1111.5,242.5 L1122.5,270 L1135,238 L1147,270 L1158,243 L1169,270 L1177,251 L1185.5,270 L1198,238 L1210,270 V290 H0 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <rect x="0" y="280" width="600" height="80" fill="url(#fy310s-lake)"/>
  <path d="M300,220 Q230,140 250,90 Q280,20 360,18 Q440,20 470,90 Q490,140 420,220 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M330.0,220 Q264.0,110 336.0,18" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M360.0,220 Q360.0,110 360.0,18" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M390.0,220 Q456.0,110 384.0,18" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M300,220 L338,258 M420,220 L382,258" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M350,236 q10,-26 20,0 q-10,8 -20,0 Z" fill="#e8590c" stroke-linejoin="round"/>
  <rect x="336" y="256" width="48" height="30" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5"/>
</svg>
