# Teho: P = ΔE/Δt

> **Miksi** sähkölaskua ei voi päätellä pelkästä laitteen tehosta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keittiö. Vasemmalla on höyryävä vedenkeitin. Sen vieressä kello näyttää lyhyttä aikaa. Oikealla on pieni pöytävalaisin. Sen vieressä kello näyttää pitkää aikaa. Keskellä seinällä on sähkömittari." class="fig-hero" style="max-width:100%;font-size:24px">
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <line x1="0" y1="70" x2="1200" y2="70" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="140" x2="1200" y2="140" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="210" x2="1200" y2="210" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="280" x2="1200" y2="280" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="350" x2="1200" y2="350" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="0" y="400" width="1200" height="200" fill="#f1dfb5"/>
  <rect x="0" y="400" width="1200" height="22" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <path d="M150,400 L166,250 Q230,230 294,250 L310,400 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M294,270 Q360,280 310,370" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M166,280 L120,248 L158,318 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="140" y="392" width="180" height="12" rx="3" fill="#1f2933"/>
  <circle cx="270" cy="370" r="8" fill="#c92a2a"/>
  <path d="M118,236 q-14,-24 0,-48 t0,-48" fill="none" stroke="#ffffff" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M118,236 q-14,-24 0,-48 t0,-48" fill="none" stroke="#c9c2b2" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M134,236 q-14,-24 0,-48 t0,-48" fill="none" stroke="#ffffff" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M134,236 q-14,-24 0,-48 t0,-48" fill="none" stroke="#c9c2b2" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M150,236 q-14,-24 0,-48 t0,-48" fill="none" stroke="#ffffff" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M150,236 q-14,-24 0,-48 t0,-48" fill="none" stroke="#c9c2b2" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <path d="M890,400 h140 l-30,-20 h-80 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="960" y1="380" x2="960" y2="230" stroke="#1f2933" stroke-width="6" stroke-linecap="butt"/>
  <path d="M800,420 L914,230 H1006 L1120,420 Z" fill="#ffc078" fill-opacity="0.35"/>
  <path d="M890,240 L920,150 H1000 L1030,240 Z" fill="#e8590c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="960" cy="238" r="14" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <circle cx="420" cy="140" r="56" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <path d="M420,140 L420,84 A56,56 0 0 1 447,91 Z" fill="#1971c2" fill-opacity="0.3"/>
  <line x1="420" y1="94" x2="420" y2="88" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="443" y1="100" x2="446" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="460" y1="117" x2="465" y2="114" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="466" y1="140" x2="472" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="460" y1="163" x2="465" y2="166" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="443" y1="180" x2="446" y2="185" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="186" x2="420" y2="192" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="397" y1="180" x2="394" y2="185" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="163" x2="375" y2="166" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="374" y1="140" x2="368" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="117" x2="375" y2="114" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="397" y1="100" x2="394" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="140" x2="439.5" y2="105" stroke="#1f2933" stroke-width="4" stroke-linecap="round"/>
  <circle cx="420" cy="140" r="5" fill="#1f2933"/>
  <circle cx="780" cy="140" r="56" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <path d="M780,140 L780,84 A56,56 0 1 1 753,91 Z" fill="#1971c2" fill-opacity="0.3"/>
  <line x1="780" y1="94" x2="780" y2="88" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="803" y1="100" x2="806" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="820" y1="117" x2="825" y2="114" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="826" y1="140" x2="832" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="820" y1="163" x2="825" y2="166" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="803" y1="180" x2="806" y2="185" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="780" y1="186" x2="780" y2="192" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="757" y1="180" x2="754" y2="185" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="740" y1="163" x2="735" y2="166" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="734" y1="140" x2="728" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="740" y1="117" x2="735" y2="114" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="757" y1="100" x2="754" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="780" y1="140" x2="760.5" y2="105" stroke="#1f2933" stroke-width="4" stroke-linecap="round"/>
  <circle cx="780" cy="140" r="5" fill="#1f2933"/>
  <rect x="540" y="190" width="120" height="170" rx="8" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="560" y="214" width="80" height="34" rx="3" fill="#1f2933"/>
  <rect x="566" y="220" width="14" height="22" rx="2" fill="#b2f2bb"/>
  <rect x="584" y="220" width="14" height="22" rx="2" fill="#b2f2bb"/>
  <rect x="602" y="220" width="14" height="22" rx="2" fill="#b2f2bb"/>
  <rect x="620" y="220" width="14" height="22" rx="2" fill="#ffc078"/>
  <circle cx="600" cy="300" r="26" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="600" y1="300" x2="618" y2="284" stroke="#c92a2a" stroke-width="3" stroke-linecap="round"/>
  <path d="M600,360 V400" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
</svg>

## Ydinajatus
Kun laite muuntaa energiaa, on kaksi tärkeää asiaa: kuinka paljon energiaa muuntuu ja kuinka nopeasti. Vedenkeitin muuntaa sähköenergiaa lämmöksi hyvin nopeasti. Siksi vesi kuumenee minuuteissa. Pieni lamppu muuntaa sähköenergiaa valoksi ja lämmöksi hitaasti.

Sitä, kuinka nopeasti energiaa muuntuu tai siirtyy, kutsutaan **tehoksi**. Teho on energia aikayksikköä kohti. Jos laite muuntaa joka sekunti $2000\,\text{J}$, sen teho on $2000\,\text{J/s} = 2000\,\text{W}$.

<svg data-fig="bars" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja mittakaavassa. Vaakapylväät näyttävät, kuinka paljon energiaa laite muuntaa yhdessä sekunnissa. Vedenkeittimen teho on 2000 W, ja se muuntaa 2000 J. Tosterin teho on 1000 W, ja se muuntaa 1000 J. Television teho on 80 W, ja se muuntaa vain 80 J. Pylvään pituus on suoraan verrannollinen tehoon." style="max-width:100%;font-size:24px">
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

Teho ei kerro, kuinka paljon energiaa laite yhteensä käyttää. Sen kertoo vasta teho yhdessä ajan kanssa. Pieni teho pitkään voi muuntaa saman energian kuin suuri teho lyhyen hetken. Siksi sähkölasku riippuu sekä laitteen tehosta että käyttöajasta.

## Kaava: Teho
Teho on muuntuneen tai siirtyneen energian ja siihen kuluneen ajan osamäärä. Energia siis jaetaan ajalla:
```latex
P = \frac{\Delta E}{\Delta t}
```
missä $P$ on teho (W), $\Delta E$ energian muutos eli muuntunut tai siirtynyt energia (J) ja $\Delta t$ siihen kulunut aika (s). Sanoin: teho on energia jaettuna ajalla. Jos energiaa muuntuu epätasaisesti, kaava antaa aikavälin $\Delta t$ keskitehon. Kun laite käy tasaisesti käynnistämisestä alkaen, $\Delta E$ on koko muuntunut energia $E$. Silloin $\Delta t$ on koko aika $t$, joten $P = E : t$. Kaavasta ratkaistaan energia ja aika:
```latex
\begin{aligned}
E &= P\,t \\
t &= \frac{E}{P}
\end{aligned}
```
Tehon yksikkö on watti: $1\,\text{W} = 1\,\text{J/s}$. Etuliitteet toimivat kuten muillakin suureilla (luku *Suureet, yksiköt ja SI-järjestelmä*): $1\,\text{kW} = 1000\,\text{W}$ ja $1\,\text{MW} = 10^{6}\,\text{W}$. Voimalaitosten teho mitataan megawateissa. Olkiluoto 3 -ydinvoimalayksikön sähköteho on noin $1600\,\text{MW}$ (TVO), eli noin $800\,000$ vedenkeittimen verran.

Jos laite muuntaa energiaa tasaisesti, energia ajan funktiona on suora, joka lähtee origosta. Suoran jyrkkyys on teho. Mitä suurempi teho, sitä jyrkemmin energia kasvaa. Kuvassa vedenkeittimen suoralla energia kasvaa $40\,\text{kJ}$ aikavälillä $20\,\text{s}$. Sijoitetaan $1\,\text{kJ} = 1000\,\text{J}$: $40\,\text{kJ} = 40 \cdot 1000\,\text{J} = 40\,000\,\text{J}$, joten $P = 40\,000\,\text{J} : 20\,\text{s} = 2000\,\text{W}$.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: energia ajan funktiona kolmelle laitteelle. Laitteet muuntavat energiaa tasaisesti. Vedenkeittimen suora (2000 W) nousee jyrkimmin. Tosterin suora (1000 W) nousee puolet loivemmin. Television suora (80 W) on lähes vaakasuora. Suoran kulmakerroin on teho. Vedenkeittimen suoralla 40 kJ kuluu 20 sekunnissa. Asteikot ovat tasavälisiä, ja kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
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
Sähköenergia laskutetaan kilowattitunteina (kWh). Yksi kilowattitunti on energia, jonka $1\,\text{kW}$:n teholla toimiva laite muuntaa tunnissa. Jouleina laskettaessa tunti on $3600\,\text{s}$ ja kilowatti $1000\,\text{W}$. Siksi saadaan:
```latex
\begin{aligned}
&1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s}\\
&= 3\,600\,000\,\text{J}
\end{aligned}
```
Kilowattitunti on siis energian yksikkö, ei tehon. Kaava $E = P\,t$ antaa suoraan kilowattitunteja, kun teho on kilowatteina ja aika tunteina. Silloin $\text{kW} \cdot \text{h} = \text{kWh}$.

### Tyypillisiä tehoja ja sähkölasku
Taulukossa on kotitalouslaitteiden tyypillisiä tehoja. Ne on pyöristetty valmistajien ilmoittamista tyyppiarvoista. Oikean laitteen teho on sen arvokilvessä. Jääkaapin teho on kompressorin käydessä. Kompressori ei käy koko ajan.

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

Sähkölasku on kulutettu energia kertaa yksikköhinta. Tässä luvussa käytetään pyöreää esimerkkihintaa $20\,\text{snt/kWh}$ eli $0{,}20\,\text{€/kWh}$. Hinta on samaa suuruusluokkaa kuin kotitalouden sähkön kokonaishinta vuonna 2025. Tilastokeskuksen mukaan kokonaishinta oli noin $18\,\text{snt/kWh}$, kun energia, siirto ja verot lasketaan yhteen. Esimerkkihinta on pyöristetty ylöspäin. Todellinen hinta vaihtelee sopimuksen ja vuodenajan mukaan.

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

**Tulos.** Television katsominen maksaa noin $1{,}9\,\text{€}$ kuukaudessa. Tulos on annettu kahdella merkitsevällä numerolla. Syy on se, että teho ja päivittäinen käyttöaika on annettu kahdella numerolla.

<!-- vaihe -->

**Järkevyys.** Yksi kilowattitunti kattaa $80\,\text{W}$:n television noin $12\,\text{h}$:ksi. Kuukaudessa katsotaan $120\,\text{h}$. Se on noin kymmenen kilowattituntia. Se maksaa noin kymmenen kertaa $20\,\text{snt}$ eli noin kaksi euroa.

## Yleinen virhekäsitys
Moni luulee, että suuri teho tarkoittaa suurta energiankulutusta. Teho kertoo vain vauhdin. Kulutettu energia on teho kertaa aika. Hiustenkuivain ($1800\,\text{W}$) käy viisi minuuttia ja kuluttaa $0{,}15\,\text{kWh}$. Mutta $10\,\text{W}$:n lamppu, joka palaa vuorokauden, kuluttaa $0{,}24\,\text{kWh}$. Toinen virhe on sekoittaa yksiköt. Watti on tehon yksikkö ja kilowattitunti energian yksikkö. Siksi "teho on $2\,\text{kWh}$" on virhe. Oikein teho on $2\,\text{kW}$.

## Tiivistelmä
- Teho kertoo, kuinka nopeasti energiaa muuntuu tai siirtyy: $P = \tfrac{\Delta E}{\Delta t}$. Yksikkö on watti, $1\,\text{W} = 1\,\text{J/s}$.
- Tasaisella teholla $E = P\,t$ ja $t = E : P$. Energia–aika-kuvaajassa suoran jyrkkyys on teho.
- $1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}$. Kilowattitunti on energian yksikkö, ja sähkölasku on energia kWh kertaa yksikköhinta.
- Suuri teho lyhyen aikaa ja pieni teho pitkään voivat käyttää yhtä paljon energiaa. Valmiustila kuluttaa energiaa kaiken aikaa.
