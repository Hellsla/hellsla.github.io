# Työ ja energia

> **Miksi** painavan repun kantaminen tasaista käytävää pitkin ei fysiikan mielessä ole työtä, vaikka olkapäät väsyvät?

## Ydinajatus
Arkikielessä työ on mitä tahansa ponnistelua. Fysiikassa sana on tarkempi: voima tekee työtä, kun se siirtää kappaletta voiman suuntaan. Kun kannat reppua vaakasuoraan tasaisella vauhdilla, kannatteleva voimasi osoittaa ylös, mutta reppu liikkuu sivulle. Voima on kohtisuorassa liikettä vastaan, joten se ei tee työtä. Lihaksesi väsyvät, koska ne kuluttavat energiaa voiman ylläpitoon, mutta reppuun ei siirry energiaa.

Työ on tapa siirtää energiaa. Tämän osoitti James Prescott Joule 1840-luvulla antamalla putoavan painon pyörittää siipipyörää vedessä. Paino teki työn, ja vesi lämpeni mitattavan verran. Joule vaihteli sekä painoa että pudotuskorkeutta eli voimaa ja matkaa, ja havaitsi lämpenemisen olevan aina verrannollinen näiden tuloon. Tämä kokeellinen tulos perustelee työn määritelmän W = Fs (kaava alla), ja siksi työ ja lämpö mitataan samalla yksiköllä, joulella.

Kun teet kappaleeseen työtä, energiaa siirtyy: nostetun kappaleen energia kasvaa, jousi venyy ja tallentaa energiaa, ja kitkaa vastaan tehty työ lämmittää pintoja. Energia ei katoa, vaan vaihtaa muotoa. Teho kertoo, kuinka nopeasti työ tehdään. Portaat ylös kävellen ja juosten teet saman työn, mutta juosten teho on suurempi. Kiukaan 6 kW:n teho tarkoittaa, että se muuttaa sähköenergiaa lämmöksi 6000 joulea joka sekunti.

## Kaavat
Kun vakiovoima on liikkeen suuntainen, voiman tekemä työ on voiman ja matkan tulo:
```latex
W = F s
```
missä W on työ (J), F voiman suuruus (N) ja s kappaleen kulkema matka (m). Yksi joule on työ, jonka yhden newtonin voima tekee yhden metrin matkalla: 1 J = 1 N·m.

Jos voima muuttuu matkan aikana, työ on (s,F)-kuvaajassa voimakäyrän ja s-akselin väliin jäävä pinta-ala. Vakiovoimalla pinta-ala on suorakulmio, jonka ala on F · s, joten sama laskusääntö toimii molemmissa tapauksissa. Monimutkaisen kuvaajan pinta-alan voi laskea osissa suorakulmioista, kolmioista ja puolisuunnikkaista.

Kun nostat kappaleen hitaasti ylös, nostovoima on yhtä suuri kuin kappaleen paino G = mg (edellinen oppitunti). Nostotyö korkeudelle h on siis:
```latex
W = G h = m g h
```
missä G on paino (N), m massa (kg), g = 9,81 m/s² ja h nostokorkeus (m). Nostetun kappaleen energia kasvaa täsmälleen nostotyön verran.

Teho on työ jaettuna siihen kuluneella ajalla. Tasaisessa liikkeessä, jossa voima on liikkeen suuntainen, teho saadaan myös voiman ja nopeuden tulona, koska s/t = v:
```latex
P = \frac{W}{t} = F v
```
missä P on teho (W), t aika (s) ja v nopeus (m/s). Yksi watti on yksi joule sekunnissa: 1 W = 1 J/s.

## Esimerkki
Jousta venytetään 20 cm. Venyttävä voima kasvaa tasaisesti nollasta 40 newtoniin, kuten kuvaaja näyttää.

<svg viewBox="0 0 600 300" role="img" aria-label="(s,F)-kuvaaja: voima kasvaa suoraviivaisesti nollasta 40 newtoniin matkalla 0–0,20 metriä; kolmion pinta-ala on työ" style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
  <polygon points="80,250 480,250 480,50" fill="currentColor" fill-opacity="0.12"/>
  <line x1="80" y1="250" x2="560" y2="250" stroke="currentColor" stroke-width="2"/>
  <line x1="80" y1="250" x2="80" y2="30" stroke="currentColor" stroke-width="2"/>
  <line x1="80" y1="250" x2="480" y2="50" stroke="currentColor" stroke-width="3"/>
  <line x1="480" y1="50" x2="480" y2="250" stroke="currentColor" stroke-dasharray="6 6"/>
  <line x1="80" y1="50" x2="480" y2="50" stroke="currentColor" stroke-dasharray="6 6"/>
  <text x="560" y="228" text-anchor="end" fill="currentColor">s (m)</text>
  <text x="92" y="28" fill="currentColor">F (N)</text>
  <text x="480" y="282" text-anchor="middle" fill="currentColor">0,20</text>
  <text x="80" y="282" text-anchor="middle" fill="currentColor">0</text>
  <text x="68" y="58" text-anchor="end" fill="currentColor">40</text>
  <text x="330" y="212" text-anchor="middle" fill="currentColor">W = pinta-ala</text>
</svg>

Työ on kolmion pinta-ala: $W = \tfrac{1}{2} \cdot 40\ \text{N} \cdot 0{,}20\ \text{m} = 4{,}0\ \text{J}$.

Sama tulos saadaan keskimääräisellä voimalla 20 N: $W = 20\ \text{N} \cdot 0{,}20\ \text{m} = 4{,}0\ \text{J}$. Työ ei katoa, vaan tallentuu jouseen. Jos laskisit $40\ \text{N} \cdot 0{,}20\ \text{m} = 8{,}0\ \text{J}$, tulos olisi kaksinkertainen, koska voima ei ole 40 N koko matkalla.

## Yleinen virhekäsitys
Työ ei ole sama asia kuin ponnistelu: väsyminen ei tarkoita, että olisit tehnyt fysiikan tarkoittamaa työtä. Toinen yleinen virhe on sotkea työ ja teho: suuri teho ei tarkoita suurta työtä, vaan nopeasti tehtyä työtä.

## Tiivistelmä
- Liikkeen suuntainen vakiovoima tekee työn $W = F s$. Muuttuvalla voimalla työ on (s,F)-kuvaajan pinta-ala.
- Liikettä vastaan kohtisuora voima ei tee työtä. Siksi vaakasuora kantaminen tasaisella vauhdilla ei ole kantajan voiman tekemää työtä.
- Työ siirtää energiaa: se voi nostaa kappaleen energiaa ($W = m g h$), venyttää jousta tai muuttua kitkassa lämmöksi. Joulen koe yhdistää työn ja lämmön.
- Teho on työ aikayksikössä: $P = W/t = F v$. Yksiköt: 1 J = 1 N·m ja 1 W = 1 J/s.
