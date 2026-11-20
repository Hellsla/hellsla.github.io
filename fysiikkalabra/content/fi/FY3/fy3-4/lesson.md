# Paine ja hydrostaattinen paine

> **Miksi** padon muuri on paljon paksumpi pohjalta kuin yläreunasta, vaikka sitä vasten on samaa vettä koko syvyydeltä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: betonipato vuoristolaaksossa sivulta nähtynä. Padon takana on syvä tekojärvi, jonka vesi tummuu syvyyden kasvaessa. Pato on yläreunasta kapea ja levenee alaspäin, pohjalta se on moninkertaisesti paksumpi." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kun voima jakautuu pinnalle, sen vaikutus riippuu siitä, kuinka suurelle alalle se jakautuu. Nastan terävä kärki uppoaa seinään samalla voimalla, jolla tylppä kanta ei jätä jälkeäkään, ja sukset kantavat hangella, vaikka kengät uppoavat. Suure, joka kuvaa tätä, on paine: voima jaettuna sillä pinta-alalla, jolle voima jakautuu. Paineen yksikkö on pascal (Pa), ja $1\,\text{Pa} = 1\,\text{N/m}^2$. Pascal on pieni yksikkö, joten arjessa käytetään kilopascalia: $1\,\text{kPa} = 1000\,\text{Pa}$.

```pysahdy
Voima $60\,\text{N}$ kohdistuu pinta-alalle $2{,}0\,\text{cm}^2$. Kuinka suuri on paine?
---
$p = \dfrac{F}{A}$, joten $p = \dfrac{60\,\text{N}}{2{,}0 \cdot 10^{-4}\,\text{m}^2}$. Se on $3{,}0 \cdot 10^{5}\,\text{Pa} = 300\,\text{kPa}$.
```

<svg data-fig="pressure-area" viewBox="0 0 600 380" role="img" aria-label="Sama voima F kohdistuu samanlaiseen tiiliskiveen kahdella tavalla. Vasemmalla tiili on pystyssä ja koskettaa alustaa pienellä alalla A1, jolloin paine p1 = F/A1 on suuri. Oikealla tiili on kyljellään ja koskettaa alustaa kolme kertaa suuremmalla alalla A2 = 3 A1, jolloin paine p2 = F/A2 on kolmasosa vasemman paineesta. Voimanuolet ovat yhtä pitkät. Kontaktialat ovat mittakaavassa, kaaviokuva muuten." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-pressure-area.webp" x="0" y="0" width="600" height="387.5" preserveAspectRatio="none"/>
  <foreignObject x="96" y="9.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pystyssä}$</div></foreignObject>
  <foreignObject x="164" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="133.5" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_1$</div></foreignObject>
  <foreignObject x="115" y="317" width="70" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_1 = \dfrac{F}{A_1}$</div></foreignObject>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kyljellään}$</div></foreignObject>
  <foreignObject x="464" y="151.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="408.5" y="285.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_2 = 3A_1$</div></foreignObject>
  <foreignObject x="415" y="317" width="70" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_2 = \dfrac{F}{A_2}$</div></foreignObject>
</svg>

### Mistä paine syntyy?
Kaasun paine syntyy mikromallin mukaan hiukkasten törmäyksistä astian seinämään. Nesteen paine syntyy nesteen omasta painosta: jokaisen vesikerroksen yllä on vettä, joka painaa sitä. Mitä syvemmällä ollaan, sitä enemmän vettä on yläpuolella ja sitä suurempi paine on. Levossa olevassa nesteessä pinnan alla olevaan vaakasuoraan pintaan, jonka pinta-ala on $A$, kohdistuu sen yläpuolisen vesipatsaan paino. Patsaan korkeus on syvyys $h$ ja tilavuus $V = Ah$. Tiheys $\rho$ on massa tilavuutta kohti ($m = \rho V$), joten patsaan massa on $\rho A h$ ja paino $G = mg = \rho A h g$. Paine on paino jaettuna alalla, joten pinta-ala supistuu pois ja jäljelle jää $\rho g h$. Tätä nesteen painosta syntyvää painetta sanotaan hydrostaattiseksi paineeksi. Se ei riipu astian muodosta eikä veden kokonaismäärästä, vaan ainoastaan syvyydestä ja nesteen tiheydestä.

<svg data-fig="water-column" viewBox="0 0 600 300" role="img" aria-label="Vesipatsas, jonka pohjan pinta-ala on A ja korkeus syvyys h. Patsaan paino G = ρAhg painaa pohjaa alaspäin, ja paine on paino jaettuna alalla, p = G/A = ρgh: pinta-ala supistuu pois. Kaaviokuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-water-column.webp" x="2.6" y="2.6" width="615.4" height="316.7" preserveAspectRatio="none"/>
  <foreignObject x="44" y="19.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vesipinta}$</div></foreignObject>
  <foreignObject x="136" y="117" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px;color:#c92a2a">$G$</div></foreignObject>
  <foreignObject x="198" y="234" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$A$</div></foreignObject>
  <foreignObject x="290" y="117" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$h$</div></foreignObject>
  <foreignObject x="392" y="25.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{patsaan paino}$</div></foreignObject>
  <foreignObject x="392" y="59" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$G = \rho A h g$</div></foreignObject>
  <foreignObject x="392" y="115.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{paine pohjalla}$</div></foreignObject>
  <foreignObject x="392" y="154.5" width="110" height="67" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$p = \dfrac{G}{A} = \rho g h$</div></foreignObject>
</svg>

Paine ei ole voima vaan voiman ja alan suhde, ja levossa olevassa nesteessä paine vaikuttaa joka suuntaan yhtä suurena. Jos paine sivulle olisi pienempi kuin alaspäin, vesi valuisi sivuun eikä pysyisi levossa. Jos pullon kylkeen tekee reikiä usealle korkeudelle, alimmasta reiästä vesi suihkuaa voimakkaimmin, koska paine kasvaa syvyyden mukana. Paineen aiheuttama voima on aina kohtisuorassa pintaa vastaan: padon pystysuoraan seinään voima osoittaa vaakasuoraan, sukeltajan kehoon joka puolelta. Siksi voima voidaan tässä laskea pelkkänä suuruutena, suunta tulee pinnasta.

```pysahdy
Miksi levossa olevassa nesteessä paine sivulle on yhtä suuri kuin alaspäin?
---
Jos paine sivulle olisi pienempi, neste valuisi sivuun eikä pysyisi levossa.
```

<figure class="unit-photo"><img src="pics/fy3/scuba-diver.webp" alt="Sukeltaja tummansinisessä vedessä, ja hänen yläpuolellaan nousee ilmakuplia kohti valoisaa pintaa."><figcaption>Sukeltaja syvällä veden alla. Uloshengitysilman kuplat nousevat kohti pintaa.</figcaption></figure>

### Ilmanpaine ja ylipaine
Veden pinnalla vaikuttaa jo ilmakehän paine eli ilmanpaine, joka on merenpinnan tasolla noin $101\,\text{kPa}$. Se on ilmapatsaan paino pinta-alaa kohti. Ilmanpaine vaikuttaa myös veden pintaan ja välittyy veden kautta syvyyteen. Veden alla kokonaispaine on siis ilmanpaineen ja hydrostaattisen paineen summa. Kymmenen metrin syvyydessä hydrostaattinen paine on jo suunnilleen yhden ilmanpaineen suuruinen.

Tämä vastaa alun kysymykseen. Ilmanpaine vaikuttaa padon muuriin molemmilta puolilta, joten muuria kuormittaa vain veden ylipaine eli paineen ilmanpainetta suurempi osa. Ylipaine on yläreunassa nolla ja kasvaa syvyyden mukana tasaisesti: 30 metrin syvyydessä se on noin $290\,\text{kPa}$, eli jokaiseen muurin neliömetriin kohdistuu noin $290\,\text{kN}$:n voima. Siksi muurin alaosan on kestettävä paljon suurempi voima kuin yläosan, ja muuri tehdään pohjalta paksuksi.

```pysahdy
Miksi padon muuria kuormittaa vain veden ylipaine eikä kokonaispaine?
---
Ilmanpaine vaikuttaa muuriin molemmilta puolilta ja kumoaa itsensä, joten jäljelle jää veden ylipaine $\rho g h$.
```

## Kaava: Paine ja hydrostaattinen paine
Paine on pintaa vastaan kohtisuora voima jaettuna pinta-alalla:
```kaavat
voiman aiheuttama paine :: p = \frac{F}{A}
```
missä $p$ on paine (Pa), $F$ pintaa vastaan kohtisuora voima (N) ja $A$ pinta-ala (m²). Yksi pascal on yhden newtonin voima yhden neliömetrin alalle: $1\,\text{Pa} = 1\,\text{N/m}^2$.

Nesteessä syvyydessä $h$ paine on
```kaavat
hydrostaattinen paine :: p = p_0 + \rho g h
```
missä $p_0$ on paine nesteen pinnalla, yleensä ilmanpaine (Pa), $\rho$ nesteen tiheys (kg/m³), $g$ = $9{,}81\,\text{m/s}^2$ ja $h$ syvyys pinnasta (m). Termi $\rho g h$ on hydrostaattinen paine eli ylipaine $\Delta p = p - p_0$, joka kertoo, kuinka paljon paine on pinnan painetta suurempi. Kuvaaja $(h, p)$ on suora, jonka kulmakerroin on $\rho g$ ja vakiotermi $p_0$, kuten FY1:n lineaarisessa mallissa $y = kx + b$. Vedelle $\rho$ = $1000\,\text{kg/m}^3$, joten paine kasvaa $9{,}81\,\text{kPa}$ jokaista metriä kohti.

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
Sukeltaja on järvessä $12{,}0\,\text{m}$:n syvyydessä vedenalaisen tarkkailuhuoneen ikkunan vieressä. Ilmanpaine pinnalla on $101\,\text{kPa}$ ja veden tiheys $1000\,\text{kg/m}^3$. Mikä on paine sukeltajan ympärillä, ja kuinka suuri voima kohdistuu ikkunaan, jonka pinta-ala on $150\,\text{cm}^2$, kun huoneessa on ilmaa normaalipaineessa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Syvyys $h = 12{,}0\,\text{m}$, ilmanpaine $p_0 = 101\,\text{kPa}$, taulukosta tai tehtävästä veden tiheys $\rho = 1000\,\text{kg/m}^3$, $g = 9{,}81\,\text{m/s}^2$ ja ikkunan ala $A = 150\,\text{cm}^2$.

Kysytään kokonaispaine $p$ sukeltajan ympärillä ja ikkunaan kohdistuva voima $F$.

<!-- vaihe -->

**Periaate.** Vesi on levossa ja sen tiheys on vakio, joten paine kasvaa syvyyden mukana tasaisesti: kokonaispaine on pinnan ilmanpaine ja veden hydrostaattinen paine $\rho g h$ yhteensä. Ikkunaan vaikuttaa vain ylipaine $\rho g h$, koska huoneen ilmanpaine työntää ikkunaa sisältä yhtä paljon kuin pinnan ilmanpaine ulkoa. Voima on paine kertaa ala, koska paine on voima pinta-alaa kohti.

<!-- vaihe -->

**Kaava ratkaistuna.** Molemmat tuntemattomat ovat jo yksin vasemmalla puolella:
```latex
\begin{aligned}
p &= p_0 + \rho g h \\
F &= \rho g h \cdot A
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ilmanpaine pascaleina on $101\,\text{kPa} = 101\,000\,\text{Pa}$. Ikkunan ala neliömetreinä on $150\,\text{cm}^2 = 150 \cdot 10^{-4}\,\text{m}^2 = 0{,}015\,\text{m}^2$, koska $1\,\text{cm}^2 = 10^{-4}\,\text{m}^2$. Muut suureet ovat jo SI-yksiköissä.

<!-- vaihe -->

**Sijoitus.** Lasketaan hydrostaattinen paine, kokonaispaine ja voima peräkkäin:
```latex
\begin{aligned}
&\rho g h \\
&= 1000\,\tfrac{\text{kg}}{\text{m}^3} \\
&\quad \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \\
&\quad \cdot 12{,}0\,\text{m} \\
&= 117\,720\,\text{Pa} \\[6pt]
&p = p_0 + \rho g h \\
&= 101\,000\,\text{Pa} \\
&\quad + 117\,720\,\text{Pa} \\
&= 218\,720\,\text{Pa} \\[6pt]
&F = \rho g h \cdot A \\
&= 117\,720\,\text{Pa} \\
&\quad \cdot 0{,}015\,\text{m}^2 \\
&= 1765{,}8\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kokonaispaine on $p \approx 219\,\text{kPa}$ ja ikkunaan kohdistuva voima $F \approx 1{,}77\,\text{kN}$. Sekä paine että voima annetaan kolmella merkitsevällä numerolla, koska syvyys $12{,}0\,\text{m}$, ilmanpaine $101\,\text{kPa}$ ja ala $150\,\text{cm}^2$ on annettu kolmella numerolla.

<!-- vaihe -->

**Järkevyys.** Kokonaispaine on noin 2,2 kertaa ilmanpaine, mikä sopii siihen, että 10 metriä vettä lisää noin yhden ilmanpaineen ja 12 metriä hieman enemmän.

Arvio: $10\,\text{kPa/m} \cdot 12\,\text{m} + 101\,\text{kPa} \approx 220\,\text{kPa}$. Voima vastaa noin $180\,\text{kg}$:n massan painoa, vaikka ikkuna on pieni.

Sukeltajan kehoa paine ei litistä, koska vedessä sama paine vaikuttaa kehoon joka puolelta ja kehon nesteet välittävät sen myös sisälle. Vain kehon ilmatilojen, kuten korvien, paine on tasattava.

## Yleinen virhekäsitys
Moni ajattelee, että paine pohjassa riippuu siitä, kuinka paljon vettä astiassa on. Kapeassa putkessa ja leveässä altaassa, joissa vesi ulottuu samaan korkeuteen, pohjan paine on sama, vaikka altaassa on tuhatkertainen määrä vettä. Paine riippuu vain syvyydestä, tiheydestä ja pinnan paineesta. Toinen virhe on sekoittaa paine ja voima: nastan terävä kärki ei tuota suurempaa voimaa kuin kanta, vaan jakaa saman voiman pienemmälle alalle, jolloin paine on suurempi. Kolmas virhe on unohtaa ilmanpaine: pelkkä $\rho g h$ antaa vain ylipaineen, ja kokonaispaine veden alla on aina sitä suurempi.

## Tiivistelmä
- Paine on voima pinta-alaa kohti: $p = F/A$. Yksikkö on pascal, $1\,\text{Pa} = 1\,\text{N/m}^2$, ja $1\,\text{kPa} = 1000\,\text{Pa}$.
- Nesteessä paine kasvaa syvyyden mukana: $p = p_0 + \rho g h$. Termi $\rho g h$ on hydrostaattinen paine, ja se riippuu vain syvyydestä ja tiheydestä, ei astian muodosta.
- Paineen aiheuttama voima on kohtisuorassa pintaa vastaan ja vaikuttaa nesteessä joka suuntaan.
- Ilmanpaine on merenpinnan tasolla noin $101\,\text{kPa}$. Vedessä paine kasvaa noin yhden ilmanpaineen verran jokaista kymmentä metriä kohti.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: sukeltaja on syvällä järvessä. Vesi tummuu syvemmälle mentäessä, ilmakuplat nousevat pintaan, ja sukeltajan ranteessa on syvyys- ja painemittari." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-4-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
