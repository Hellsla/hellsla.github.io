# Paine ja hydrostaattinen paine

> **Miksi** padon muuri on paljon paksumpi pohjalta kuin yläreunasta, vaikka sitä vasten on samaa vettä koko syvyydeltä?

## Ydinajatus
Kun voima jakautuu pinnalle, sen vaikutus riippuu siitä, kuinka suurelle alalle se jakautuu. Nastan terävä kärki uppoaa seinään samalla voimalla, jolla tylppä kanta ei jätä jälkeäkään, ja sukset kantavat hangella, vaikka kengät uppoavat. Suure, joka kuvaa tätä, on paine: voima jaettuna sillä pinta-alalla, jolle voima jakautuu. Paineen yksikkö on pascal (Pa), ja 1 Pa = 1 N/m². Pascal on pieni yksikkö, joten arjessa käytetään kilopascalia: 1 kPa = 1000 Pa.

Kaasun paine syntyy mikromallin mukaan hiukkasten törmäyksistä astian seinämään. Nesteen paine syntyy nesteen omasta painosta: jokaisen vesikerroksen yllä on vettä, joka painaa sitä. Mitä syvemmällä ollaan, sitä enemmän vettä on yläpuolella ja sitä suurempi paine on. Levossa olevassa nesteessä pinnan alla olevaan vaakasuoraan pintaan, jonka pinta-ala on A, kohdistuu sen yläpuolisen vesipatsaan paino. Patsaan korkeus on syvyys h ja tilavuus V = Ah. Tiheys ρ on massa tilavuutta kohti (m = ρV), joten patsaan massa on ρAh ja paino G = mg = ρAhg. Paine on paino jaettuna alalla, joten pinta-ala supistuu pois ja jäljelle jää ρgh. Tätä nesteen painosta syntyvää painetta sanotaan hydrostaattiseksi paineeksi. Se ei riipu astian muodosta eikä veden kokonaismäärästä, vaan ainoastaan syvyydestä ja nesteen tiheydestä.

<svg viewBox="0 0 600 300" role="img" aria-label="Vesipatsas, jonka pohjan pinta-ala on A ja korkeus syvyys h. Patsaan paino G = ρAhg painaa pohjaa alaspäin, ja paine on paino jaettuna alalla, p = G/A = ρgh: pinta-ala supistuu pois. Kaaviokuva, ei mittakaavassa." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="30" y="50" width="340" height="230" fill="currentColor" fill-opacity="0.1"/>
  <line x1="30" y1="50" x2="370" y2="50" stroke="currentColor" stroke-width="3"/>
  <polyline points="30,20 30,280 370,280 370,20" fill="none" stroke="currentColor" stroke-width="3"/>
  <text x="200" y="36" text-anchor="middle" fill="currentColor">vesipinta</text>
  <rect x="170" y="50" width="80" height="170" fill="currentColor" fill-opacity="0.25" stroke="currentColor" stroke-width="2" stroke-dasharray="7 5"/>
  <line x1="170" y1="220" x2="250" y2="220" stroke="currentColor" stroke-width="6"/>
  <line x1="210" y1="80" x2="210" y2="190" stroke="currentColor" stroke-width="4"/>
  <polygon points="198,186 222,186 210,212" fill="currentColor"/>
  <foreignObject x="110" y="108" width="54" height="48" style="font-size:32px"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$G$</div></foreignObject>
  <foreignObject x="184" y="226" width="52" height="48" style="font-size:32px"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$A$</div></foreignObject>
  <line x1="275" y1="50" x2="275" y2="220" stroke="currentColor" stroke-width="2"/>
  <line x1="267" y1="50" x2="283" y2="50" stroke="currentColor" stroke-width="2"/>
  <line x1="267" y1="220" x2="283" y2="220" stroke="currentColor" stroke-width="2"/>
  <foreignObject x="286" y="112" width="50" height="48" style="font-size:32px"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$h$</div></foreignObject>
  <text x="390" y="40" fill="currentColor">patsaan paino</text>
  <foreignObject x="390" y="52" width="205" height="48" style="font-size:30px"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$G = \rho A h g$</div></foreignObject>
  <text x="390" y="140" fill="currentColor">paine pohjalla</text>
  <foreignObject x="390" y="152" width="205" height="48" style="font-size:30px"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$p = G/A = \rho g h$</div></foreignObject>
</svg>

Paine ei ole voima vaan voiman ja alan suhde, ja levossa olevassa nesteessä paine vaikuttaa joka suuntaan yhtä suurena. Jos paine sivulle olisi pienempi kuin alaspäin, vesi valuisi sivuun eikä pysyisi levossa. Jos pullon kylkeen tekee reikiä usealle korkeudelle, alimmasta reiästä vesi suihkuaa voimakkaimmin, koska paine kasvaa syvyyden mukana. Paineen aiheuttama voima on aina kohtisuorassa pintaa vastaan: padon pystysuoraan seinään voima osoittaa vaakasuoraan, sukeltajan kehoon joka puolelta. Siksi voima voidaan tässä laskea pelkkänä suuruutena, suunta tulee pinnasta.

Veden pinnalla vaikuttaa jo ilmakehän paine eli ilmanpaine, joka on merenpinnan tasolla noin 101 kPa. Se on ilmapatsaan paino pinta-alaa kohti. Ilmanpaine vaikuttaa myös veden pintaan ja välittyy veden kautta syvyyteen. Veden alla kokonaispaine on siis ilmanpaineen ja hydrostaattisen paineen summa. Kymmenen metrin syvyydessä hydrostaattinen paine on jo suunnilleen yhden ilmanpaineen suuruinen.

Tämä vastaa alun kysymykseen. Ilmanpaine vaikuttaa padon muuriin molemmilta puolilta, joten muuria kuormittaa vain veden ylipaine eli paineen ilmanpainetta suurempi osa. Ylipaine on yläreunassa nolla ja kasvaa syvyyden mukana tasaisesti: 30 metrin syvyydessä se on noin 290 kPa, eli jokaiseen muurin neliömetriin kohdistuu noin 290 kN:n voima. Siksi muurin alaosan on kestettävä paljon suurempi voima kuin yläosan, ja muuri tehdään pohjalta paksuksi.

## Kaava
Paine on pintaa vastaan kohtisuora voima jaettuna pinta-alalla:
```latex
p = \frac{F}{A}
```
missä p on paine (Pa), F pintaa vastaan kohtisuora voima (N) ja A pinta-ala (m²). Yksi pascal on yhden newtonin voima yhden neliömetrin alalle: 1 Pa = 1 N/m².

Nesteessä syvyydessä h paine on
```latex
p = p_0 + \rho g h
```
missä p₀ on paine nesteen pinnalla, yleensä ilmanpaine (Pa), ρ nesteen tiheys (kg/m³), g = 9,81 m/s² ja h syvyys pinnasta (m). Termi ρgh on hydrostaattinen paine eli ylipaine Δp = p − p₀, joka kertoo, kuinka paljon paine on pinnan painetta suurempi. Kuvaaja (h, p) on suora, jonka kulmakerroin on ρg ja vakiotermi p₀, kuten FY1:n lineaarisessa mallissa y = kx + b. Vedelle ρ = 1000 kg/m³, joten paine kasvaa 9,81 kPa jokaista metriä kohti.

<svg viewBox="0 0 600 300" role="img" aria-label="Veden paine syvyyden funktiona on suora: pinnalla paine on ilmanpaine 101 kPa ja 10 metrin syvyydessä noin 199 kPa" style="max-width:100%;font-family:system-ui,sans-serif;font-size:22px">
  <line x1="80" y1="250" x2="570" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="80" y1="250" x2="80" y2="30" stroke="currentColor" stroke-width="3"/>
  <line x1="80" y1="150" x2="520" y2="52" stroke="currentColor" stroke-width="4"/>
  <line x1="80" y1="150" x2="520" y2="150" stroke="currentColor" stroke-width="2" stroke-dasharray="8 6"/>
  <circle cx="80" cy="150" r="6" fill="currentColor"/><circle cx="520" cy="52" r="6" fill="currentColor"/>
  <text x="66" y="258" text-anchor="end" fill="currentColor">0</text>
  <text x="66" y="157" text-anchor="end" fill="currentColor">101</text>
  <text x="66" y="59" text-anchor="end" fill="currentColor">199</text>
  <text x="90" y="28" fill="currentColor">p (kPa)</text>
  <text x="80" y="284" text-anchor="middle" fill="currentColor">0</text>
  <text x="520" y="284" text-anchor="middle" fill="currentColor">10</text>
  <text x="575" y="238" text-anchor="end" fill="currentColor">h (m)</text>
  <text x="300" y="178" text-anchor="middle" fill="currentColor">ilmanpaine p₀</text>
  <text x="310" y="132" fill="currentColor">p = p₀ + ρgh</text>
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
Moni ajattelee, että paine pohjassa riippuu siitä, kuinka paljon vettä astiassa on. Kapeassa putkessa ja leveässä altaassa, joissa vesi ulottuu samaan korkeuteen, pohjan paine on sama, vaikka altaassa on tuhatkertainen määrä vettä. Paine riippuu vain syvyydestä, tiheydestä ja pinnan paineesta. Toinen virhe on sekoittaa paine ja voima: nastan terävä kärki ei tuota suurempaa voimaa kuin kanta, vaan jakaa saman voiman pienemmälle alalle, jolloin paine on suurempi. Kolmas virhe on unohtaa ilmanpaine: pelkkä ρgh antaa vain ylipaineen, ja kokonaispaine veden alla on aina sitä suurempi.

## Tiivistelmä
- Paine on voima pinta-alaa kohti: $p = F/A$. Yksikkö on pascal, 1 Pa = 1 N/m², ja 1 kPa = 1000 Pa.
- Nesteessä paine kasvaa syvyyden mukana: $p = p_0 + \rho g h$. Termi ρgh on hydrostaattinen paine, ja se riippuu vain syvyydestä ja tiheydestä, ei astian muodosta.
- Paineen aiheuttama voima on kohtisuorassa pintaa vastaan ja vaikuttaa nesteessä joka suuntaan.
- Ilmanpaine on merenpinnan tasolla noin 101 kPa. Vedessä paine kasvaa noin yhden ilmanpaineen verran jokaista kymmentä metriä kohti.
