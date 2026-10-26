# Paine ja hydrostaattinen paine

> **Miksi** padon muuri on paljon paksumpi pohjalta kuin yläreunasta, vaikka sitä vasten on samaa vettä koko syvyydeltä?

## Ydinajatus
Kun voima jakautuu pinnalle, sen vaikutus riippuu siitä, kuinka suurelle alalle se jakautuu. Nastan terävä kärki uppoaa seinään samalla voimalla, jolla tylppä kanta ei jätä jälkeäkään, ja sukset kantavat hangella, vaikka kengät uppoavat. Suure, joka kuvaa tätä, on paine: voima jaettuna sillä pinta-alalla, jolle voima jakautuu. Paineen yksikkö on pascal (Pa), ja 1 Pa = 1 N/m². Pascal on pieni yksikkö, joten arjessa käytetään kilopascalia: 1 kPa = 1000 Pa.

<svg data-fig="pressure-area" viewBox="0 0 600 380" role="img" aria-label="Sama voima F kohdistuu samanlaiseen tiiliskiveen kahdella tavalla. Vasemmalla tiili on pystyssä ja koskettaa alustaa pienellä alalla A1, jolloin paine p1 = F/A1 on suuri. Oikealla tiili on kyljellään ja koskettaa alustaa kolme kertaa suuremmalla alalla A2 = 3 A1, jolloin paine p2 = F/A2 on kolmasosa vasemman paineesta. Voimanuolet ovat yhtä pitkät. Kontaktialat ovat mittakaavassa, kaaviokuva muuten." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy34-snow" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="#eef5f9"/><circle cx="3" cy="4" r="1.3" fill="#a9d1f0"/><circle cx="10" cy="10" r="1.3" fill="#a9d1f0"/></pattern></defs>
  <rect x="12" y="240" width="576" height="22" fill="url(#fy34-snow)" stroke="#1f2933" stroke-width="2"/>
  <line x1="300" y1="30" x2="300" y2="330" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <foreignObject x="96" y="9.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pystyssä}$</div></foreignObject>
  <rect x="130" y="120" width="40" height="120" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="58" x2="150" y2="100" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,117 L142,99 L158,99 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="164" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <line x1="130" y1="241" x2="170" y2="241" stroke="#e8590c" stroke-width="6" stroke-linecap="butt"/>
  <path d="M130,270 V282 M130,276 H170 M170,270 V282" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="133.5" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_1$</div></foreignObject>
  <foreignObject x="115" y="317" width="70" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_1 = \dfrac{F}{A_1}$</div></foreignObject>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kyljellään}$</div></foreignObject>
  <rect x="390" y="200" width="120" height="40" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="450" y1="138" x2="450" y2="180" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M450,197 L442,179 L458,179 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="464" y="151.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <line x1="390" y1="241" x2="510" y2="241" stroke="#e8590c" stroke-width="6" stroke-linecap="butt"/>
  <path d="M390,270 V282 M390,276 H510 M510,270 V282" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="408.5" y="285.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_2 = 3A_1$</div></foreignObject>
  <foreignObject x="415" y="317" width="70" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_2 = \dfrac{F}{A_2}$</div></foreignObject>
</svg>

Kaasun paine syntyy mikromallin mukaan hiukkasten törmäyksistä astian seinämään. Nesteen paine syntyy nesteen omasta painosta: jokaisen vesikerroksen yllä on vettä, joka painaa sitä. Mitä syvemmällä ollaan, sitä enemmän vettä on yläpuolella ja sitä suurempi paine on. Levossa olevassa nesteessä pinnan alla olevaan vaakasuoraan pintaan, jonka pinta-ala on $A$, kohdistuu sen yläpuolisen vesipatsaan paino. Patsaan korkeus on syvyys $h$ ja tilavuus $V = Ah$. Tiheys $\rho$ on massa tilavuutta kohti ($m = \rho V$), joten patsaan massa on $\rho A h$ ja paino $G = mg = \rho A h g$. Paine on paino jaettuna alalla, joten pinta-ala supistuu pois ja jäljelle jää $\rho g h$. Tätä nesteen painosta syntyvää painetta sanotaan hydrostaattiseksi paineeksi. Se ei riipu astian muodosta eikä veden kokonaismäärästä, vaan ainoastaan syvyydestä ja nesteen tiheydestä.

<svg data-fig="water-column" viewBox="0 0 600 300" role="img" aria-label="Vesipatsas, jonka pohjan pinta-ala on A ja korkeus syvyys h. Patsaan paino G = ρAhg painaa pohjaa alaspäin, ja paine on paino jaettuna alalla, p = G/A = ρgh: pinta-ala supistuu pois. Kaaviokuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy34-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="30" y="50" width="340" height="230" fill="url(#fy34-water)" fill-opacity="0.55"/>
  <line x1="30" y1="50" x2="370" y2="50" stroke="#2f74b5" stroke-width="3" stroke-linecap="butt"/>
  <path d="M30,22 V280 H370 V22" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <foreignObject x="44" y="19.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vesipinta}$</div></foreignObject>
  <rect x="170" y="50" width="80" height="170" fill="#2f74b5" stroke="#1f2933" stroke-width="2" fill-opacity="0.3" stroke-dasharray="7 5"/>
  <line x1="170" y1="220" x2="250" y2="220" stroke="#1f2933" stroke-width="6" stroke-linecap="butt"/>
  <line x1="210" y1="80" x2="210" y2="189" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M210,214 L198.5,188 L221.5,188 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="136" y="117" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$G$</div></foreignObject>
  <foreignObject x="198" y="234" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$A$</div></foreignObject>
  <line x1="275" y1="50" x2="275" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="267" y1="50" x2="283" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="267" y1="220" x2="283" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="290" y="117" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$h$</div></foreignObject>
  <foreignObject x="392" y="25.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{patsaan paino}$</div></foreignObject>
  <foreignObject x="392" y="59" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$G = \rho A h g$</div></foreignObject>
  <foreignObject x="392" y="115.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{paine pohjalla}$</div></foreignObject>
  <foreignObject x="392" y="154.5" width="110" height="67" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$p = \dfrac{G}{A} = \rho g h$</div></foreignObject>
</svg>

Paine ei ole voima vaan voiman ja alan suhde, ja levossa olevassa nesteessä paine vaikuttaa joka suuntaan yhtä suurena. Jos paine sivulle olisi pienempi kuin alaspäin, vesi valuisi sivuun eikä pysyisi levossa. Jos pullon kylkeen tekee reikiä usealle korkeudelle, alimmasta reiästä vesi suihkuaa voimakkaimmin, koska paine kasvaa syvyyden mukana. Paineen aiheuttama voima on aina kohtisuorassa pintaa vastaan: padon pystysuoraan seinään voima osoittaa vaakasuoraan, sukeltajan kehoon joka puolelta. Siksi voima voidaan tässä laskea pelkkänä suuruutena, suunta tulee pinnasta.

Veden pinnalla vaikuttaa jo ilmakehän paine eli ilmanpaine, joka on merenpinnan tasolla noin 101 kPa. Se on ilmapatsaan paino pinta-alaa kohti. Ilmanpaine vaikuttaa myös veden pintaan ja välittyy veden kautta syvyyteen. Veden alla kokonaispaine on siis ilmanpaineen ja hydrostaattisen paineen summa. Kymmenen metrin syvyydessä hydrostaattinen paine on jo suunnilleen yhden ilmanpaineen suuruinen.

Tämä vastaa alun kysymykseen. Ilmanpaine vaikuttaa padon muuriin molemmilta puolilta, joten muuria kuormittaa vain veden ylipaine eli paineen ilmanpainetta suurempi osa. Ylipaine on yläreunassa nolla ja kasvaa syvyyden mukana tasaisesti: 30 metrin syvyydessä se on noin 290 kPa, eli jokaiseen muurin neliömetriin kohdistuu noin 290 kN:n voima. Siksi muurin alaosan on kestettävä paljon suurempi voima kuin yläosan, ja muuri tehdään pohjalta paksuksi.

## Kaava: Paine ja hydrostaattinen paine
Paine on pintaa vastaan kohtisuora voima jaettuna pinta-alalla:
```latex
p = \frac{F}{A}
```
missä $p$ on paine (Pa), $F$ pintaa vastaan kohtisuora voima (N) ja $A$ pinta-ala (m²). Yksi pascal on yhden newtonin voima yhden neliömetrin alalle: 1 Pa = 1 N/m².

Nesteessä syvyydessä $h$ paine on
```latex
p = p_0 + \rho g h
```
missä $p_0$ on paine nesteen pinnalla, yleensä ilmanpaine (Pa), $\rho$ nesteen tiheys (kg/m³), $g$ = 9,81 m/s² ja $h$ syvyys pinnasta (m). Termi $\rho g h$ on hydrostaattinen paine eli ylipaine $\Delta p = p - p_0$, joka kertoo, kuinka paljon paine on pinnan painetta suurempi. Kuvaaja $(h, p)$ on suora, jonka kulmakerroin on $\rho g$ ja vakiotermi $p_0$, kuten FY1:n lineaarisessa mallissa $y = kx + b$. Vedelle $\rho$ = 1000 kg/m³, joten paine kasvaa 9,81 kPa jokaista metriä kohti.

<svg data-fig="pressure-depth" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: veden paine p kilopascaleina syvyyden h funktiona, kun h on 0–10 m. Paine on nouseva suora: pinnalla paine on ilmanpaine 101 kPa ja 10 metrin syvyydessä noin 199 kPa. Suoran ja katkoviivan väli on hydrostaattinen paine ρgh." style="max-width:100%;font-size:24px">
  <line x1="173" y1="285" x2="173" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="242.5" y1="285" x2="242.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="311.5" y1="285" x2="311.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="381" y1="285" x2="381" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="450" y1="285" x2="450" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="240" x2="450" y2="240" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="195.5" x2="450" y2="195.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="150.5" x2="450" y2="150.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="106" x2="450" y2="106" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="103" y1="285" x2="464" y2="285" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476,285 L463,291 L463,279 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="104" y1="286" x2="104" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M104,44 L110,57 L98,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="173" y1="285" x2="173" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="163" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="242.5" y1="285" x2="242.5" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="232.5" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="311.5" y1="285" x2="311.5" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="301.5" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="381" y1="285" x2="381" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="371" y="294.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="450" y1="285" x2="450" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="433.5" y="294.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="97" y1="240" x2="104" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="59" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="97" y1="195.5" x2="104" y2="195.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="181" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="97" y1="150.5" x2="104" y2="150.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="136" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="97" y1="106" x2="104" y2="106" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="91.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="74" y="290.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="482" y="270.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h\ (\text{m})$</div></foreignObject>
  <foreignObject x="94" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="104,194.5 450,106.5" fill="none" stroke="#2f74b5" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="104,194.5 450,194.5" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="104" cy="194.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="450" cy="106.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="116" y="210" width="261" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ilmanpaine}\ p_0 = 101\,\text{kPa}$</span></div></foreignObject>
  <foreignObject x="283" y="71.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2f74b5">$p = p_0 + \rho g h$</div></foreignObject>
  <path d="M466.0,106.6 H472.0 V194.5 H466.0" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="482" y="136" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\rho g h$</div></foreignObject>
</svg>

## Esimerkki
Sukeltaja on järvessä 12 m:n syvyydessä vedenalaisen tarkkailuhuoneen ikkunan vieressä. Ilmanpaine pinnalla on 101 kPa ja veden tiheys 1000 kg/m³. Mikä on paine sukeltajan ympärillä, ja kuinka suuri voima kohdistuu ikkunaan, jonka pinta-ala on 150 cm², kun huoneessa on ilmaa normaalipaineessa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Syvyys $h = 12\,\text{m}$, ilmanpaine $p_0 = 101\,\text{kPa}$, tiheys $\rho = 1000\,\text{kg/m}^3$ ja ikkunan ala $A = 150\,\text{cm}^2 = 0{,}015\,\text{m}^2$. Kysytään kokonaispaine $p$ ja ikkunaan kohdistuva voima $F$.

<!-- vaihe -->

**Kaavat ratkaistuina.** Kokonaispaine on ilmanpaineen ja hydrostaattisen paineen summa. Ikkunaan vaikuttaa vain ylipaine $\rho g h$, koska huoneen ilmanpaine työntää ikkunaa sisältä yhtä paljon kuin pinnan ilmanpaine ulkoa. Voima on paine kertaa ala:
```latex
\begin{aligned}
p &= p_0 + \rho g h \\
F &= \rho g h \cdot A
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin hydrostaattinen paine ja sitten kokonaispaine:
```latex
\begin{aligned}
&\rho g h \\
&= 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \\
&\quad \cdot 12\,\text{m} \\
&= 117\,720\,\text{Pa} \\
&= 117{,}72\,\text{kPa} \\
&p \\
&= 101\,\text{kPa} + 117{,}72\,\text{kPa} \\
&\approx 219\,\text{kPa}
\end{aligned}
```

<!-- vaihe -->

**Voima ikkunaan.** Ylipaine kerrotaan ikkunan alalla:
```latex
\begin{aligned}
F &= \rho g h \cdot A \\
&= 117{,}72\,\text{kPa} \cdot 0{,}015\,\text{m}^2 \\
&\approx 1{,}8\,\text{kN}
\end{aligned}
```

<!-- vaihe -->

**Järkevyys.** Kokonaispaine on noin 2,2 kertaa ilmanpaine, mikä sopii siihen, että 10 metriä vettä lisää noin yhden ilmanpaineen. Voima vastaa noin 180 kg:n massan painoa, vaikka ikkuna on pieni. Sukeltajan kehoa paine ei litistä, koska vedessä sama paine vaikuttaa kehoon joka puolelta ja kehon nesteet välittävät sen myös sisälle. Vain kehon ilmatilojen, kuten korvien, paine on tasattava.

## Yleinen virhekäsitys
Moni ajattelee, että paine pohjassa riippuu siitä, kuinka paljon vettä astiassa on. Kapeassa putkessa ja leveässä altaassa, joissa vesi ulottuu samaan korkeuteen, pohjan paine on sama, vaikka altaassa on tuhatkertainen määrä vettä. Paine riippuu vain syvyydestä, tiheydestä ja pinnan paineesta. Toinen virhe on sekoittaa paine ja voima: nastan terävä kärki ei tuota suurempaa voimaa kuin kanta, vaan jakaa saman voiman pienemmälle alalle, jolloin paine on suurempi. Kolmas virhe on unohtaa ilmanpaine: pelkkä $\rho g h$ antaa vain ylipaineen, ja kokonaispaine veden alla on aina sitä suurempi.

## Tiivistelmä
- Paine on voima pinta-alaa kohti: $p = F/A$. Yksikkö on pascal, 1 Pa = 1 N/m², ja 1 kPa = 1000 Pa.
- Nesteessä paine kasvaa syvyyden mukana: $p = p_0 + \rho g h$. Termi $\rho g h$ on hydrostaattinen paine, ja se riippuu vain syvyydestä ja tiheydestä, ei astian muodosta.
- Paineen aiheuttama voima on kohtisuorassa pintaa vastaan ja vaikuttaa nesteessä joka suuntaan.
- Ilmanpaine on merenpinnan tasolla noin 101 kPa. Vedessä paine kasvaa noin yhden ilmanpaineen verran jokaista kymmentä metriä kohti.
