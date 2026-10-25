# Paine ja hydrostaattinen paine

> **Miksi** padon muuri on paljon paksumpi pohjalta kuin yläreunasta, vaikka sitä vasten on samaa vettä koko syvyydeltä?

## Ydinajatus
Kun voima jakautuu pinnalle, sen vaikutus riippuu siitä, kuinka suurelle alalle se jakautuu. Nastan terävä kärki uppoaa seinään samalla voimalla, jolla tylppä kanta ei jätä jälkeäkään, ja sukset kantavat hangella, vaikka kengät uppoavat. Suure, joka kuvaa tätä, on paine: voima jaettuna sillä pinta-alalla, jolle voima jakautuu. Paineen yksikkö on pascal (Pa), ja 1 Pa = 1 N/m². Pascal on pieni yksikkö, joten arjessa käytetään kilopascalia: 1 kPa = 1000 Pa.

Kaasun paine syntyy mikromallin mukaan hiukkasten törmäyksistä astian seinämään. Nesteen paine syntyy nesteen omasta painosta: jokaisen vesikerroksen yllä on vettä, joka painaa sitä. Mitä syvemmällä ollaan, sitä enemmän vettä on yläpuolella ja sitä suurempi paine on. Levossa olevassa nesteessä pinnan alla olevaan vaakasuoraan pintaan, jonka pinta-ala on A, kohdistuu sen yläpuolisen vesipatsaan paino. Patsaan korkeus on syvyys h ja tilavuus V = Ah. Tiheys ρ on massa tilavuutta kohti (m = ρV), joten patsaan massa on ρAh ja paino G = mg = ρAhg. Paine on paino jaettuna alalla, joten pinta-ala supistuu pois ja jäljelle jää ρgh. Tätä nesteen painosta syntyvää painetta sanotaan hydrostaattiseksi paineeksi. Se ei riipu astian muodosta eikä veden kokonaismäärästä, vaan ainoastaan syvyydestä ja nesteen tiheydestä.

Paine ei ole voima vaan voiman ja alan suhde, ja levossa olevassa nesteessä paine vaikuttaa joka suuntaan yhtä suurena. Jos paine sivulle olisi pienempi kuin alaspäin, vesi valuisi sivuun eikä pysyisi levossa. Siksi pullon kyljessä olevasta alimmasta reiästä vesi suihkuaa voimakkaimmin. Paineen aiheuttama voima on aina kohtisuorassa pintaa vastaan: padon pystysuoraan seinään voima osoittaa vaakasuoraan, sukeltajan kehoon joka puolelta. Siksi voima voidaan tässä laskea pelkkänä suuruutena, suunta tulee pinnasta.

Veden pinnalla vaikuttaa jo ilmakehän paine eli ilmanpaine, joka on merenpinnan tasolla noin 101 kPa. Se on ilmapatsaan paino pinta-alaa kohti, ja se vaikuttaa myös veden pintaan ja välittyy sen kautta syvyyteen. Veden alla kokonaispaine on siis ilmanpaineen ja hydrostaattisen paineen summa. Kymmenen metrin syvyydessä hydrostaattinen paine on jo suunnilleen yhden ilmanpaineen suuruinen.

Tämä vastaa alun kysymykseen. Ilmanpaine vaikuttaa padon muuriin molemmilta puolilta, joten muuria kuormittaa vain veden ylipaine. Se on yläreunassa nolla ja kasvaa syvyyden mukana tasaisesti: 30 metrin syvyydessä se on noin 290 kPa, eli jokaiseen muurin neliömetriin kohdistuu noin 290 kN:n voima. Siksi muurin alaosan on kestettävä paljon suurempi voima kuin yläosan, ja muuri tehdään pohjalta paksuksi.

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

Hydrostaattinen paine: $\rho g h = 1000\,\text{kg/m}^3 \cdot 9{,}81\,\text{m/s}^2 \cdot 12\,\text{m} = 117\,720\,\text{Pa} = 117{,}72\,\text{kPa}$.

Kokonaispaine: $p = p_0 + \rho g h = 101\,\text{kPa} + 117{,}72\,\text{kPa} \approx 219\,\text{kPa}$, eli noin 2,2 kertaa ilmanpaine.

Ikkunaan vaikuttaa vain ylipaine, koska huoneen ilmanpaine työntää ikkunaa sisältä yhtä paljon kuin pinnan ilmanpaine ulkoa. Pinta-ala on $150\,\text{cm}^2 = 0{,}015\,\text{m}^2$, joten voima on $F = \rho g h \cdot A = 117{,}72\,\text{kPa} \cdot 0{,}015\,\text{m}^2 \approx 1{,}8\,\text{kN}$. Se vastaa noin 180 kg:n massan painoa, vaikka ikkuna on pieni. Sukeltajan kehoa paine ei litistä, koska vedessä sama paine vaikuttaa kehoon joka puolelta ja kehon nesteet välittävät sen myös sisälle. Vain kehon ilmatilojen, kuten korvien, paine on tasattava.

## Yleinen virhekäsitys
Moni ajattelee, että paine pohjassa riippuu siitä, kuinka paljon vettä astiassa on. Kapeassa putkessa ja leveässä altaassa, joissa vesi ulottuu samaan korkeuteen, pohjan paine on sama, vaikka altaassa on tuhatkertainen määrä vettä. Paine riippuu vain syvyydestä, tiheydestä ja pinnan paineesta. Toinen virhe on sekoittaa paine ja voima: nastan terävä kärki ei tuota suurempaa voimaa kuin kanta, vaan jakaa saman voiman pienemmälle alalle, jolloin paine on suurempi. Kolmas virhe on unohtaa ilmanpaine: pelkkä ρgh antaa vain ylipaineen, ja kokonaispaine veden alla on aina sitä suurempi.

## Tiivistelmä
- Paine on voima pinta-alaa kohti: $p = F/A$. Yksikkö on pascal, 1 Pa = 1 N/m², ja 1 kPa = 1000 Pa.
- Nesteessä paine kasvaa syvyyden mukana: $p = p_0 + \rho g h$. Termi ρgh on hydrostaattinen paine, ja se riippuu vain syvyydestä ja tiheydestä, ei astian muodosta.
- Paineen aiheuttama voima on kohtisuorassa pintaa vastaan ja vaikuttaa nesteessä joka suuntaan.
- Ilmanpaine on merenpinnan tasolla noin 101 kPa. Vedessä paine kasvaa noin yhden ilmanpaineen verran jokaista kymmentä metriä kohti.
