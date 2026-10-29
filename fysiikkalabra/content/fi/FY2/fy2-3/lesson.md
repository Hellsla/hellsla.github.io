# Teho: P = ΔE/Δt

> **Miksi** sähkölaskua ei voi päätellä pelkästä laitteen tehosta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keittiössä vasemmalla höyryävä vedenkeitin, jonka yllä kello näyttää lyhyttä aikaa, ja oikealla pieni pöytävalaisin, jonka yllä kello näyttää pitkää aikaa. Keskellä seinällä sähkömittari, josta johto kulkee laitteille." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy23h-kettle" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy23h-spout" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><radialGradient id="fy23h-led" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#f2a69c"/><stop offset="0.55" stop-color="#c92a2a" stop-opacity="0.8"/><stop offset="1" stop-color="#c92a2a" stop-opacity="0"/></radialGradient><linearGradient id="fy23h-base" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#1f2933"/></linearGradient><linearGradient id="fy23h-shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><radialGradient id="fy23h-bulb" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff"/><stop offset="0.55" stop-color="#ffc078" stop-opacity="0.8"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient><linearGradient id="fy23h-meter" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="400" fill="#ffffff"/>
  <line x1="0" y1="0" x2="0" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="75" y1="0" x2="75" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="0" x2="150" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="225" y1="0" x2="225" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="0" x2="300" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="375" y1="0" x2="375" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="450" y1="0" x2="450" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="525" y1="0" x2="525" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="0" x2="600" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="675" y1="0" x2="675" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="750" y1="0" x2="750" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="825" y1="0" x2="825" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="900" y1="0" x2="900" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="975" y1="0" x2="975" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1050" y1="0" x2="1050" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1125" y1="0" x2="1125" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1200" y1="0" x2="1200" y2="400" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="0" x2="1200" y2="0" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="75" x2="1200" y2="75" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="150" x2="1200" y2="150" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="225" x2="1200" y2="225" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="300" x2="1200" y2="300" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="375" x2="1200" y2="375" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="0" y="400" width="1200" height="26" fill="#c9c2b2" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="426" width="1200" height="174" fill="#e3dccb"/>
  <line x1="300" y1="426" x2="300" y2="600" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="426" x2="600" y2="600" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="900" y1="426" x2="900" y2="600" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="266" y="450" width="8" height="44" rx="4" fill="#8a96a3"/>
  <rect x="326" y="450" width="8" height="44" rx="4" fill="#8a96a3"/>
  <rect x="566" y="450" width="8" height="44" rx="4" fill="#8a96a3"/>
  <rect x="626" y="450" width="8" height="44" rx="4" fill="#8a96a3"/>
  <rect x="866" y="450" width="8" height="44" rx="4" fill="#8a96a3"/>
  <rect x="926" y="450" width="8" height="44" rx="4" fill="#8a96a3"/>
  <path d="M600,330 V370 H300 V400 M600,370 H930 V400" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linejoin="round"/>
  <ellipse cx="240" cy="400" rx="110" ry="10" fill="#1f2933" fill-opacity="0.2"/>
  <rect x="140" y="384" width="200" height="16" rx="4" fill="#1f2933"/>
  <path d="M154,384 L170,210 Q240,188 310,210 L326,384 Z" fill="url(#fy23h-kettle)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M310,226 Q390,236 332,360" fill="none" stroke="#1f2933" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M170,240 L116,206 L160,288 Z" fill="url(#fy23h-spout)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M180,196 Q240,176 300,196 L290,206 Q240,192 190,206 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="296" y="330" width="22" height="14" rx="4" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="307" cy="337" r="12" fill="url(#fy23h-led)"/>
  <path d="M114,196 c-14,-24 14,-40 0,-64 s14,-40 0,-64" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M114,196 c-14,-24 14,-40 0,-64 s14,-40 0,-64" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M128,196 c-14,-24 14,-40 0,-64 s14,-40 0,-64" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M128,196 c-14,-24 14,-40 0,-64 s14,-40 0,-64" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M142,196 c-14,-24 14,-40 0,-64 s14,-40 0,-64" fill="none" stroke="#c9c2b2" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M142,196 c-14,-24 14,-40 0,-64 s14,-40 0,-64" fill="none" stroke="#ffffff" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M870,248 L740,426 H1140 L1010,248 Z" fill="#ffc078" fill-opacity="0.3"/>
  <path d="M860,400 h160 l-30,-24 h-100 Z" fill="url(#fy23h-base)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="940" y1="380" x2="940" y2="250" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <path d="M854,252 L890,150 H990 L1026,252 Z" fill="url(#fy23h-shade)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="940" cy="250" r="16" fill="url(#fy23h-bulb)"/>
  <circle cx="420" cy="150" r="64" fill="#ffffff" stroke="#1f2933" stroke-width="4"/>
  <path d="M420,150 L420,92 A58,58 0 0 1 448,99 Z" fill="#1971c2" fill-opacity="0.3"/>
  <line x1="420" y1="100" x2="420" y2="92" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="445" y1="106.5" x2="449" y2="100" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="463.5" y1="125" x2="470" y2="121" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="150" x2="478" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="463.5" y1="175" x2="470" y2="179" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="445" y1="193.5" x2="449" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="200" x2="420" y2="208" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="395" y1="193.5" x2="391" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="376.5" y1="175" x2="370" y2="179" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370" y1="150" x2="362" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="376.5" y1="125" x2="370" y2="121" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="395" y1="106.5" x2="391" y2="100" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="150" x2="441" y2="111.5" stroke="#1f2933" stroke-width="5" stroke-linecap="round"/>
  <circle cx="420" cy="150" r="6" fill="#1f2933"/>
  <circle cx="780" cy="150" r="64" fill="#ffffff" stroke="#1f2933" stroke-width="4"/>
  <path d="M780,150 L780,92 A58,58 0 1 1 752,99 Z" fill="#1971c2" fill-opacity="0.3"/>
  <line x1="780" y1="100" x2="780" y2="92" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="805" y1="106.5" x2="809" y2="100" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="823.5" y1="125" x2="830" y2="121" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="830" y1="150" x2="838" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="823.5" y1="175" x2="830" y2="179" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="805" y1="193.5" x2="809" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="780" y1="200" x2="780" y2="208" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="755" y1="193.5" x2="751" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="736.5" y1="175" x2="730" y2="179" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="730" y1="150" x2="722" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="736.5" y1="125" x2="730" y2="121" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="755" y1="106.5" x2="751" y2="100" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="780" y1="150" x2="759" y2="111.5" stroke="#1f2933" stroke-width="5" stroke-linecap="round"/>
  <circle cx="780" cy="150" r="6" fill="#1f2933"/>
  <rect x="530" y="170" width="140" height="160" rx="10" fill="url(#fy23h-meter)" stroke="#1f2933" stroke-width="3"/>
  <rect x="550" y="192" width="100" height="36" rx="4" fill="#1f2933"/>
  <rect x="556" y="198" width="14" height="24" rx="2" fill="#b2f2bb"/>
  <rect x="574" y="198" width="14" height="24" rx="2" fill="#b2f2bb"/>
  <rect x="592" y="198" width="14" height="24" rx="2" fill="#b2f2bb"/>
  <rect x="610" y="198" width="14" height="24" rx="2" fill="#b2f2bb"/>
  <rect x="628" y="198" width="14" height="24" rx="2" fill="#ffc078"/>
  <ellipse cx="600" cy="276" rx="44" ry="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="592" y="266" width="16" height="20" rx="2" fill="#c92a2a"/>
  <rect x="560" y="304" width="80" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
</svg>

## Ydinajatus
Kun laite muuntaa energiaa, kiinnostaa kaksi asiaa: kuinka paljon energiaa muuntuu ja kuinka nopeasti. Vedenkeitin muuntaa sähköenergiaa lämmöksi hyvin nopeasti, joten vesi kuumenee minuuteissa. Pieni lamppu muuntaa sähköenergiaa valoksi ja lämmöksi hitaasti.

Sitä, kuinka nopeasti energiaa muuntuu tai siirtyy, kutsutaan **tehoksi**. Teho on energia aikayksikköä kohti: jos laite muuntaa joka sekunti $2000\,\text{J}$, sen teho on $2000\,\text{J/s} = 2000\,\text{W}$.

<svg data-fig="bars" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja mittakaavassa: vaakapylväät näyttävät, kuinka paljon energiaa laite muuntaa yhdessä sekunnissa. Vedenkeitin, jonka teho on 2000 W, muuntaa 2000 J, tosteri 1000 W 1000 J ja televisio 80 W vain 80 J. Pylvään pituus on suoraan verrannollinen tehoon." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy23-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <foreignObject x="96.5" y="11.5" width="407" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energiaa muuntuu yhdessä sekunnissa}$</div></foreignObject>
  <foreignObject x="30" y="75.5" width="261" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vedenkeitin},\ P = 2000\,\text{W}$</div></foreignObject>
  <rect x="30" y="108" width="400" height="32" fill="url(#fy23-heat)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="442" y="109.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2000\,\text{J}$</div></foreignObject>
  <foreignObject x="30" y="159.5" width="211" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tosteri},\ P = 1000\,\text{W}$</div></foreignObject>
  <rect x="30" y="192" width="200" height="32" fill="url(#fy23-heat)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="242" y="193.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1000\,\text{J}$</div></foreignObject>
  <foreignObject x="30" y="243.5" width="211" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{televisio},\ P = 80\,\text{W}$</div></foreignObject>
  <rect x="30" y="276" width="16" height="32" fill="url(#fy23-heat)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="58" y="277.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$80\,\text{J}$</div></foreignObject>
  <line x1="30" y1="306" x2="570" y2="306" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
</svg>

Teho ei kerro, kuinka paljon energiaa laite yhteensä käyttää. Sen kertoo vasta teho yhdessä ajan kanssa: pieni teho pitkään voi muuntaa saman energian kuin suuri teho lyhyen hetken. Siksi sähkölasku riippuu sekä laitteen tehosta että käyttöajasta.

## Kaava: Teho
Teho on muuntuneen tai siirtyneen energian ja siihen kuluneen ajan osamäärä:
```latex
P = \frac{\Delta E}{\Delta t}
```
missä $P$ on teho (W), $\Delta E$ energian muutos eli muuntunut tai siirtynyt energia (J) ja $\Delta t$ siihen kulunut aika (s). Sanoin: teho on energia jaettuna ajalla. Jos energiaa muuntuu epätasaisesti, kaava antaa aikavälin $\Delta t$ keskitehon. Kun laite käy tasaisesti käynnistämisestä alkaen, $\Delta E$ on koko muuntunut energia $E$ ja $\Delta t$ koko aika $t$, joten $P = E : t$. Kaavasta ratkaistaan energia ja aika:
```latex
\begin{aligned}
E &= P\,t \\
t &= \frac{E}{P}
\end{aligned}
```
Tehon yksikkö on watti: $1\,\text{W} = 1\,\text{J/s}$. Etuliitteet toimivat kuten muillakin suureilla (luku *Suureet, yksiköt ja SI-järjestelmä*): $1\,\text{kW} = 1000\,\text{W}$ ja $1\,\text{MW} = 10^{6}\,\text{W}$. Voimalaitosten teho mitataan megawateissa: Olkiluoto 3 -ydinvoimalayksikön sähköteho on noin $1600\,\text{MW}$ (TVO), eli noin $800\,000$ vedenkeittimen verran.

Jos laite muuntaa energiaa tasaisesti, energia ajan funktiona on suora, joka lähtee origosta. Suoran jyrkkyys on teho: mitä suurempi teho, sitä jyrkemmin energia kasvaa. Kuvassa vedenkeittimen suoralla energia kasvaa $40\,\text{kJ}$ aikavälillä $20\,\text{s}$. Sijoitetaan $1\,\text{kJ} = 1000\,\text{J}$: $40\,\text{kJ} = 40 \cdot 1000\,\text{J} = 40\,000\,\text{J}$, joten $P = 40\,000\,\text{J} : 20\,\text{s} = 2000\,\text{W}$.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: energia ajan funktiona kolmelle laitteelle, jotka muuntavat energiaa tasaisesti. Vedenkeittimen 2000 W suora nousee jyrkimmin, tosterin 1000 W suora puolet loivemmin ja television 80 W suora lähes vaakasuoraan. Suoran kulmakerroin on teho: vedenkeittimen suoralla 40 kJ kuluu 20 sekunnissa. Asteikot ovat tasavälisiä ja kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="212.5" y1="290" x2="212.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="341.5" y1="290" x2="341.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="216.5" x2="470" y2="216.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="143.5" x2="470" y2="143.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="70" x2="470" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="291" x2="84" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,44 L90,57 L78,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="212.5" y1="290" x2="212.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="196" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="341.5" y1="290" x2="341.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="325" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="77" y1="216.5" x2="84" y2="216.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="202" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="77" y1="143.5" x2="84" y2="143.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="129" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="77" y1="70" x2="84" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <foreignObject x="54" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="74" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{kJ})$</div></foreignObject>
  <polyline points="84,290 470,70" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="84,290 470,180" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="84,290 470,281" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="212.5" y1="216.5" x2="212.5" y2="143.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="212.5" y1="143.5" x2="341.5" y2="143.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="212.5" cy="216.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="341.5" cy="143.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="167.5" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta E$</span></div></foreignObject>
  <foreignObject x="260.5" y="107" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta t$</span></div></foreignObject>
  <foreignObject x="484" y="55.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$2000\,\text{W}$</div></foreignObject>
  <foreignObject x="484" y="165.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$1000\,\text{W}$</div></foreignObject>
  <foreignObject x="406" y="240.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$80\,\text{W}$</div></foreignObject>
</svg>

### Kilowattitunti
Sähköenergia laskutetaan kilowattitunteina (kWh). Yksi kilowattitunti on energia, jonka $1\,\text{kW}$:n teholla toimiva laite muuntaa tunnissa. Jouleina laskettaessa tunti on $3600\,\text{s}$ ja kilowatti $1000\,\text{W}$, joten
```latex
\begin{aligned}
&1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s}\\
&= 3\,600\,000\,\text{J}
\end{aligned}
```
Kilowattitunti on siis energian yksikkö, ei tehon. Kaava $E = P\,t$ antaa suoraan kilowattitunteja, kun teho on kilowatteina ja aika tunteina: $\text{kW} \cdot \text{h} = \text{kWh}$.

### Tyypillisiä tehoja ja sähkölasku
Taulukossa on kotitalouslaitteiden tyypillisiä tehoja, pyöristettyinä valmistajien ilmoittamista tyyppiarvoista. Oikean laitteen teho on sen arvokilvessä. Jääkaapin teho on kompressorin käydessä, eikä kompressori käy koko ajan.

| Laite | Teho |
| --- | --- |
| LED-lamppu | $8\,\text{W}$ |
| kannettava tietokone | $50\,\text{W}$ |
| televisio | $80\,\text{W}$ |
| jääkaappi | $100\,\text{W}$ |
| hiustenkuivain | $1800\,\text{W}$ |
| vedenkeitin | $2000\,\text{W}$ |
| sähkökiuas | $8\,\text{kW}$ |

Moni laite käyttää energiaa myös silloin, kun se näyttää olevan pois päältä. Valmiustilan teho on tyypillisesti alle wattista muutamaan wattiin laitetta kohti. Se on pieni, mutta valmiustila kestää kaikki $8760\,\text{h}$ vuodessa.

Sähkölasku on kulutettu energia kertaa yksikköhinta. Tässä luvussa käytetään pyöreää esimerkkihintaa $20\,\text{snt/kWh}$ eli $0{,}20\,\text{€/kWh}$. Se on kotitalouden sähkön kokonaishinnan suuruusluokka vuonna 2025 (Tilastokeskus 2025: noin $18\,\text{snt/kWh}$ kokonaishintana, kun energia, siirto ja verot lasketaan yhteen); esimerkkihinta on pyöristetty ylöspäin. Todellinen hinta vaihtelee sopimuksen ja vuodenajan mukaan.

## Esimerkki
Television teho on $80\,\text{W}$, ja se on päällä $4{,}0\,\text{h}$ vuorokaudessa $30\,\text{vrk}$ ajan. Mitä television katsominen maksaa kuukaudessa, kun sähkön hinta on $20\,\text{snt/kWh}$?

<!-- vaihe -->

**Tunnetut ja kysytty.** Teho $P = 80\,\text{W}$, käyttöaika $4{,}0\,\text{h}$ vuorokaudessa $30\,\text{vrk}$ ajan ja hinta $20\,\text{snt/kWh}$. Kysytään kuukauden sähkön hintaa.

<!-- vaihe -->

**Periaate.** Televisio muuntaa energiaa tasaisella teholla, joten kuluva energia on teho kertaa aika. Hinta saadaan kertomalla energia kilowattitunteina yksikköhinnalla.

<!-- vaihe -->

**Kaava ratkaistuna.** Energia on $E = P\,t$ ja hinta on energia kertaa yksikköhinta:
```latex
\begin{aligned}
E &= P\,t \\
\text{hinta} &= E \cdot \text{yksikköhinta}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Kilowattitunteja varten teho on kilowatteina. Sijoitetaan $1\,\text{W} = 10^{-3}\,\text{kW}$: $80\,\text{W} = 80 \cdot 10^{-3}\,\text{kW} = 0{,}080\,\text{kW}$. Kokonaisaika on $4{,}0\,\text{h} \cdot 30 = 120\,\text{h}$. Hinta saadaan senteissä, ja euroiksi muunnetaan sijoittamalla $1\,\text{snt} = 0{,}01\,\text{€}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
E &= P\,t \\
&= 0{,}080\,\text{kW} \cdot 120\,\text{h} \\
&= 9{,}6\,\text{kWh} \\
\text{hinta} &= E \cdot \text{yksikköhinta} \\
&= 9{,}6\,\text{kWh} \cdot 20\,\text{snt/kWh} \\
&= 192\,\text{snt} \\
&= 192 \cdot 0{,}01\,\text{€} \\
&= 1{,}92\,\text{€}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Television katsominen maksaa noin $1{,}9\,\text{€}$ kuukaudessa. Tulos on annettu kahdella merkitsevällä numerolla, koska teho ja päivittäinen käyttöaika ovat annetut kahdella numerolla.

<!-- vaihe -->

**Järkevyys.** Yksi kilowattitunti kattaa $80\,\text{W}$:n television noin $12\,\text{h}$:ksi, ja kuukaudessa katsotaan $120\,\text{h}$, eli noin kymmenen kilowattituntia. Se maksaa noin kymmenen kertaa $20\,\text{snt}$ eli noin kaksi euroa.

## Yleinen virhekäsitys
Moni luulee, että suuri teho tarkoittaa suurta energiankulutusta. Teho kertoo vain vauhdin: kulutettu energia on teho kertaa aika. Hiustenkuivain ($1800\,\text{W}$) käy viisi minuuttia ja kuluttaa $0{,}15\,\text{kWh}$, mutta $10\,\text{W}$:n lamppu, joka palaa vuorokauden, kuluttaa $0{,}24\,\text{kWh}$. Toinen virhe on sekoittaa yksiköt: watti on tehon yksikkö ja kilowattitunti energian, joten "teho on $2\,\text{kWh}$" on virhe: oikein teho on $2\,\text{kW}$.

## Tiivistelmä
- Teho kertoo, kuinka nopeasti energiaa muuntuu tai siirtyy: $P = \tfrac{\Delta E}{\Delta t}$. Yksikkö on watti, $1\,\text{W} = 1\,\text{J/s}$.
- Tasaisella teholla $E = P\,t$ ja $t = E : P$. Energia–aika-kuvaajassa suoran jyrkkyys on teho.
- $1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}$. Kilowattitunti on energian yksikkö, ja sähkölasku on energia kWh kertaa yksikköhinta.
- Suuri teho lyhyen aikaa ja pieni teho pitkään voivat käyttää yhtä paljon energiaa; valmiustila kuluttaa energiaa kaiken aikaa.
