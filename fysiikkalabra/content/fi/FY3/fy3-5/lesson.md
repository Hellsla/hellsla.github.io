# Sisäenergia, lämpömäärä ja energian säilyminen

> **Miksi** polkupyörän pumppu kuumenee, kun rengasta pumpataan, vaikka pumppua ei lämmitetä millään?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kädet painavat jalkapumpun kahvaa alas, ja letku vie ilman polkupyörän renkaaseen. Pumpun alaosa on lämmennyt, mitä kuvaavat oranssi hehku ja väreilevät viivat." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy35h-barrel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#ffc078"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="520" width="1200" height="80" fill="#c9c2b2"/>
  <line x1="0" y1="520" x2="1200" y2="520" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="930" cy="330" r="210" fill="none" stroke="#1f2933" stroke-width="34"/>
  <circle cx="930" cy="330" r="186" fill="none" stroke="#8a96a3" stroke-width="4"/>
  <line x1="930" y1="330" x2="1114" y2="330" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1100" y2="400.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1060" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1000.5" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="930" y2="514" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="859.5" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="800" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="760" y2="400.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="746" y2="330" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="760" y2="259.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="800" y2="200" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="859.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="930" y2="146" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1000.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1060" y2="200" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1100" y2="259.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="930" cy="330" r="22" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="764" y="270" width="24" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="500" width="200" height="22" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="370" y="220" width="60" height="284" rx="8" fill="url(#fy35h-barrel)" stroke="#1f2933" stroke-width="3"/>
  <rect x="370" y="400" width="60" height="104" rx="8" fill="#e8590c" fill-opacity="0.55"/>
  <rect x="370" y="220" width="60" height="284" fill="none" rx="8" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="392" y="140" width="16" height="84" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="124" width="200" height="28" rx="14" fill="#1f2933"/>
  <path d="M430,470 C520,470 560,400 640,380 S740,300 776,280" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M340,470 q-12,-13.5 0,-26.5 t0,-26.5 t0,-26.5" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M460,470 q-12,-13.5 0,-26.5 t0,-26.5 t0,-26.5" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M330,90 L290,-10" fill="none" stroke="#1971c2" stroke-width="58" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="330" cy="128" rx="38" ry="30" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M470,90 L510,-10" fill="none" stroke="#1971c2" stroke-width="58" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="470" cy="128" rx="38" ry="30" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M553,70 L553,154 L543,154 L560,180 L577,154 L567,154 L567,70 Z" fill="#1971c2" stroke-linejoin="round"/>
</svg>

## Ydinajatus
Luvussa *Työ ja energia* työ todettiin tavaksi siirtää energiaa, ja Joulen koe näytti, että mekaaninen työ voi lämmittää vettä: painon työ kasvatti veden sisäenergiaa, vaikka vettä ei lämmitetty. Vesi ei sisällä ”lämpöä”. Systeemin sisäenergia $U$ on sen hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Mikromallin mukaan lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, joten kun kaasun tai nesteen lämpötila nousee, sen sisäenergia kasvaa. Sisäenergia riippuu myös aineen määrästä: iso järvi sisältää paljon enemmän sisäenergiaa kuin kuppi kuumaa teetä, vaikka järvi on kylmempi.

Systeemin sisäenergiaa voi muuttaa kahdella tavalla. Ensimmäinen on työ: kun pumpun mäntä puristaa ilmaa, ympäristö tekee kaasuun työtä, ja kaasun sisäenergia kasvaa, koska liikkuva mäntä osuu hiukkasiin kuin maila palloon ja ne kimpoavat nopeampina. Simulaatiossa tämän näkee hiukkastasolla. Siksi pumppu kuumenee. Toinen on lämpö: kun kaksi eri lämpötilassa olevaa kappaletta koskettavat, energiaa siirtyy itsestään kuumemmasta kylmempään, kunnes lämpötilat ovat samat. Näin siirtynyttä energiaa sanotaan lämmöksi, ja siirtyneen energian määrä on lämpömäärä $Q$. Lämpö on siis energian siirtymistä, ei aineen ominaisuus: kappaleella on lämpötila ja sisäenergia, mutta ei lämpöä.

<svg data-fig="two-ways" viewBox="0 0 600 316" role="img" aria-label="Kaksi tapaa muuttaa sisäenergiaa (kaaviokuva, ei mittakaavassa). Vasemmalla mäntä työntyy sylinteriin ja tekee ilmaan työn W, ja ilman hiukkaset liikkuvat nopeammin. Oikealla kuuma ja kylmä kappale koskettavat, ja lämpömäärä Q siirtyy kuumasta kylmään." style="max-width:100%;font-size:24px">
  <foreignObject x="137.5" y="13.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{työ}$</div></foreignObject>
  <foreignObject x="415" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö}$</div></foreignObject>
  <rect x="128" y="112" width="152" height="124" fill="#f2a69c"/>
  <path d="M70,112 H280 V236 H70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="112" y="113.5" width="16" height="121" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M22,181 L86,181 L86,189 L108,174 L86,159 L86,167 L22,167 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="50" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <line x1="160" y1="142" x2="174.5" y2="136.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M182,134 L175,141 L172,133.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="216" y1="140" x2="232.5" y2="145.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M240,148 L230,149 L232.5,141.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="254" y1="188" x2="239" y2="196" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M232,200 L238,192 L242,199 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="176" y1="196" x2="190" y2="183.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M196,178 L192,187 L186.5,181 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="150" y1="176" x2="164.5" y2="169.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M172,166 L165.5,173.5 L162,166 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="222" y1="214" x2="206" y2="211.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M198,210 L207.5,207.5 L206,215.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="160" cy="142" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="216" cy="140" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="254" cy="188" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="176" cy="196" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="150" cy="176" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="222" cy="214" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="96" y="261.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilma kuumenee}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="322" y="112" width="120" height="124" fill="#f2a69c" stroke="#1f2933" stroke-width="3"/>
  <rect x="442" y="112" width="120" height="124" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="347" y="159.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma}$</div></foreignObject>
  <foreignObject x="467" y="159.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä}$</div></foreignObject>
  <path d="M352,100 L504,100 L504,109 L532,92 L504,75 L504,84 L352,84 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="432" y="43.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="344.5" y="261.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuumasta kylmään}$</div></foreignObject>
</svg>

Energia säilyy. Kun systeemiin siirtyy energiaa lämpönä tai työnä, sen sisäenergia kasvaa täsmälleen siirtyneen energian verran, ja kun energiaa siirtyy pois, sisäenergia pienenee yhtä paljon. Tämä on termodynamiikan ensimmäinen pääsääntö: energian säilymisen laki kirjoitettuna lämmölle ja työlle. Eristetty systeemi on suljettu systeemi, johon tai josta ei myöskään siirry energiaa lämpönä eikä työnä. Sen kokonaisenergia pysyy vakiona, vaikka energia sen sisällä vaihtaisi muotoa.

## Kaava: Termodynamiikan ensimmäinen pääsääntö
Sisäenergian muutos on systeemiin tuodun lämpömäärän ja systeemiin tehdyn työn summa:
```latex
\Delta U = Q + W
```
missä $\Delta U$ on sisäenergian muutos (J), $Q$ systeemiin siirtynyt lämpömäärä (J) ja $W$ ympäristön systeemiin tekemä työ (J). Merkit kertovat suunnan: $Q$ on positiivinen, kun lämpöä siirtyy systeemiin, ja negatiivinen, kun sitä siirtyy pois; $W$ on positiivinen, kun ympäristö tekee työtä systeemiin (esimerkiksi puristaa kaasua), ja negatiivinen, kun systeemi tekee työtä ympäristöön (kaasu laajenee ja työntää mäntää). Kaikki termit ovat jouleja, samaa yksikköä kuin työ luvussa *Työ ja energia*, ja männän kaasuun tekemä työ lasketaan samoin kuin siellä, voiman ja matkan tulona.

<svg data-fig="energy-balance" viewBox="0 0 600 300" role="img" aria-label="Energiakaavio: systeemiin tulee lämpömäärä Q ja työ W, ja systeemin sisäenergia muuttuu niiden summan verran. Ulos siirtyvä energia on negatiivista." style="max-width:100%;font-size:24px">
  <rect x="206" y="62" width="188" height="160" rx="14" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="246" y="103.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{systeemi}$</div></foreignObject>
  <foreignObject x="258.5" y="151.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta U = Q + W$</div></foreignObject>
  <path d="M24,108 L172,108 L172,117 L200,100 L172,83 L172,92 L24,92 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="68.5" y="51.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö}\ Q$</div></foreignObject>
  <path d="M24,194 L172,194 L172,203 L200,186 L172,169 L172,178 L24,178 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="81" y="209.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{työ}\ W$</div></foreignObject>
  <path d="M400,150 L548,150 L548,159 L576,142 L548,125 L548,134 L400,134 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="424" y="87.5" width="128" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q < 0\ \text{tai}\ W < 0$</div></foreignObject>
  <foreignObject x="459" y="163.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ulos}$</div></foreignObject>
  <foreignObject x="77.5" y="247.5" width="445" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sisään positiivinen, ulos negatiivinen}$</div></foreignObject>
</svg>

<svg data-fig="work-sign" viewBox="0 0 600 316" role="img" aria-label="Työn etumerkki (kaaviokuva, ei mittakaavassa). Vasemmalla mäntää työnnetään sisään ja kaasu puristuu: ympäristö tekee kaasuun työn, joten W on positiivinen. Oikealla kaasu työntää mäntää ulos ja laajenee: kaasu tekee työn ympäristöön, joten W on negatiivinen." style="max-width:100%;font-size:24px">
  <foreignObject x="121" y="13.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{puristus}$</div></foreignObject>
  <foreignObject x="376" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{laajeneminen}$</div></foreignObject>
  <rect x="142" y="100" width="138" height="110" fill="#eef5f9"/>
  <path d="M70,100 H280 V210 H70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="126" y="101.5" width="16" height="107" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M22,162 L100,162 L100,170 L122,155 L100,140 L100,148 L22,148 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="168" cy="124" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="212" cy="130" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="252" cy="150" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="186" cy="160" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="232" cy="186" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="166" cy="192" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="206" cy="178" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="416" y="100" width="164" height="110" fill="#eef5f9"/>
  <path d="M330,100 H580 V210 H330" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="400" y="101.5" width="16" height="107" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M396,148 L358,148 L358,140 L336,155 L358,170 L358,162 L396,162 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="450" cy="122" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="520" cy="128" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="556" cy="158" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="478" cy="156" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="536" cy="190" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="448" cy="190" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="500" cy="178" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="300" y1="20" x2="300" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="152.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W > 0$</div></foreignObject>
  <foreignObject x="432.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W < 0$</div></foreignObject>
  <foreignObject x="58.5" y="269.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ympäristö tekee työn}$</div></foreignObject>
  <foreignObject x="363.5" y="269.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu tekee työn}$</div></foreignObject>
</svg>

## Esimerkki
Pumpun sylinterissä on ilmaa. Mäntää painetaan alas, jolloin ympäristö tekee ilmaan työn 150 J. Samalla kuumenevasta ilmasta siirtyy sylinterin seinien kautta ympäristöön lämpömäärä 40 J. Kuinka paljon ilman sisäenergia muuttuu?

<!-- vaihe -->

**Tunnetut ja kysytty.** Ilma on systeemi. Ympäristö tekee työtä systeemiin, joten $W = +150\,\text{J}$. Lämpöä siirtyy systeemistä pois, joten $Q = -40\,\text{J}$. Kysytty on sisäenergian muutos $\Delta U$.

<!-- vaihe -->

**Periaate.** Energia säilyy: systeemin sisäenergia muuttuu täsmälleen sen verran kuin siihen siirtyy energiaa lämpönä ja työnä. Tämä on termodynamiikan ensimmäinen pääsääntö, ja se pätee, koska ilma on selvästi rajattu systeemi, jonka rajan yli energia siirtyy vain työnä ja lämpönä.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty $\Delta U$ on ensimmäisessä pääsäännössä jo yksin vasemmalla puolella, joten yhtälöä ei tarvitse muokata:

```latex
\begin{aligned}
&\Delta U = Q + W
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: sekä $Q$ että $W$ on annettu jouleina, ja tulos halutaan jouleina. Etumerkit sen sijaan on päätettävä: energia systeemiin on positiivista ja systeemistä pois negatiivista.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot etumerkkeineen:

```latex
\begin{aligned}
&\Delta U = Q + W \\
&= -40\,\text{J} + 150\,\text{J} \\
&= 110\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ilman sisäenergia kasvaa $110\,\text{J}$. Tulos ilmoitetaan kokonaisina jouleina, koska sekä työ että lämpö on annettu kokonaisina jouleina.

<!-- vaihe -->

**Järkevyys.** Työ toi ilmaan 150 J ja lämpönä lähti vain 40 J, joten sisäenergian on kasvettava ja ilman lämpötilan noustava. Jos sama 150 J:n työ tehtäisiin niin hitaasti, että kaikki työn tuoma energia ehtisi siirtyä lämpönä pois, olisi $Q = -150\,\text{J}$ ja $\Delta U = 0$, eikä lämpötila muuttuisi. Nyt lämpöä lähtee vähemmän, joten tulos on tämän rajatapauksen ja pelkän työn $150\,\text{J}$ välissä.

## Yleinen virhekäsitys
Arkikielessä sanotaan, että kappaleessa ”on lämpöä” tai että lämpö ”varastoituu”. Fysiikassa lämpö on energian siirtymistä lämpötilaeron vuoksi, ja se, mikä kappaleeseen varastoituu, on sisäenergiaa. Toinen virhe on pitää lämpötilaa ja sisäenergiaa samana asiana: kuuman kipinän lämpötila on tuhansia asteita, mutta sen sisäenergia on pieni, koska siinä on vähän ainetta. Kolmas virhe on ajatella, että sisäenergiaa voi muuttaa vain lämmittämällä. Pumpun ilma kuumenee ilman mitään lämmönlähdettä, koska siihen tehdään työtä.

## Tiivistelmä
- Sisäenergia $U$ on systeemin hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Se kasvaa, kun lämpötila nousee, ja riippuu myös aineen määrästä.
- Lämpö on energian siirtymistä kuumemmasta kylmempään lämpötilaeron vuoksi; siirtynyt energia on lämpömäärä $Q$. Kappaleella ei ”ole lämpöä”.
- Sisäenergiaa muuttavat lämpö ja työ: $\Delta U = Q + W$. Sisään siirtyvä energia on positiivista, ulos siirtyvä negatiivista.
- Energia säilyy: tämä on termodynamiikan ensimmäinen pääsääntö. Eristetyn systeemin kokonaisenergia pysyy vakiona.
