# Työ ja energia

> **Miksi** painavan repun kantaminen tasaista käytävää pitkin ei fysiikan mielessä ole työtä, vaikka olkapäät väsyvät?

## Ydinajatus
Arkikielessä työ on mitä tahansa ponnistelua. Fysiikassa sana on tarkempi: voima tekee työtä vain, kun se siirtää kappaletta omaan suuntaansa. Kun kannat reppua vaakasuoraan, kannatteleva voimasi osoittaa ylös, mutta reppu liikkuu sivulle. Voima ei siirrä reppua omaan suuntaansa, joten se ei tee työtä. Lihakset väsyvät, koska ne kuluttavat energiaa pitääkseen voiman yllä, mutta reppuun ei siirry energiaa.

Työ on siis tapa siirtää energiaa kappaleesta toiseen. Energia puolestaan on kappaleen kyky tehdä työtä. Liikkuvalla kappaleella on liike-energiaa, ja maan pinnan yläpuolelle nostetulla kappaleella on potentiaalienergiaa. Kun teet kappaleeseen työtä, sen energia kasvaa täsmälleen tehdyn työn verran. Tämä on koko kurssin kantava ajatus: energia ei synny eikä katoa, se vain vaihtaa muotoa ja omistajaa.

Teho kertoo, kuinka nopeasti työ tehdään. Portaat ylös kävellen ja juosten teet saman työn, mutta juosten teho on suurempi, koska sama energia siirtyy lyhyemmässä ajassa. Sähkölaitteissa teho on tuttu luku: kiukaan 6 kW tarkoittaa, että se muuttaa sähköenergiaa lämmöksi 6000 joulea joka sekunti.

## Kaavat
Kun vakiovoima vaikuttaa liikkeen suuntaan, voiman tekemä työ on voiman ja matkan tulo:
```latex
W = F s
```
missä W on työ (J), F voiman suuruus (N) ja s kappaleen kulkema matka (m). Yksi joule on työ, jonka yhden newtonin voima tekee yhden metrin matkalla: 1 J = 1 N·m.

Jos voima muuttuu matkan aikana, työ on (s,F)-kuvaajassa voiman käyrän ja s-akselin väliin jäävä pinta-ala. Vakiovoimalla pinta-ala on suorakulmio F · s, joten sama kaava toimii molemmissa tapauksissa.

Liike-energia ja painovoiman potentiaalienergia, jotka tulivat tutuiksi FY2-moduulissa:
```latex
E_k = \tfrac{1}{2} m v^2 \qquad E_p = m g h
```
missä m on massa (kg), v nopeus (m/s), g = 9,81 m/s² ja h korkeus valitusta nollatasosta (m).

Teho on työ jaettuna siihen kuluneella ajalla. Tasaisessa liikkeessä teho voidaan laskea myös voiman ja nopeuden tulona, koska s/t = v:
```latex
P = \frac{W}{t} = F v
```
missä P on teho (W), t aika (s) ja v nopeus (m/s). Yksi watti on yksi joule sekunnissa: 1 W = 1 J/s.

## Esimerkki
Jousta venytetään 20 cm. Venyttävä voima kasvaa tasaisesti nollasta 40 newtoniin, kuten kuvaaja näyttää.

<svg viewBox="0 0 600 300" role="img" aria-label="(s,F)-kuvaaja: voima kasvaa suoraviivaisesti 0:sta 40 N:iin matkalla 0–0,20 m; kolmion pinta-ala on työ" style="max-width:100%;font-family:system-ui,sans-serif;font-size:16px">
  <polygon points="80,250 480,250 480,50" fill="currentColor" fill-opacity="0.12"/>
  <line x1="80" y1="250" x2="560" y2="250" stroke="currentColor" stroke-width="2"/>
  <line x1="80" y1="250" x2="80" y2="30" stroke="currentColor" stroke-width="2"/>
  <line x1="80" y1="250" x2="480" y2="50" stroke="currentColor" stroke-width="3"/>
  <line x1="480" y1="50" x2="480" y2="250" stroke="currentColor" stroke-dasharray="6 6"/>
  <line x1="80" y1="50" x2="480" y2="50" stroke="currentColor" stroke-dasharray="6 6"/>
  <text x="560" y="280" text-anchor="end" fill="currentColor">s (m)</text>
  <text x="90" y="40" fill="currentColor">F (N)</text>
  <text x="480" y="280" text-anchor="middle" fill="currentColor">0,20</text>
  <text x="80" y="280" text-anchor="middle" fill="currentColor">0</text>
  <text x="70" y="56" text-anchor="end" fill="currentColor">40</text>
  <text x="300" y="200" text-anchor="middle" fill="currentColor">W = pinta-ala</text>
</svg>

Työ on kolmion pinta-ala: $W = \tfrac{1}{2} \cdot 40\ \text{N} \cdot 0{,}20\ \text{m} = 4{,}0\ \text{J}$.

Sama tulos saadaan keskimääräisellä voimalla 20 N: $W = 20\ \text{N} \cdot 0{,}20\ \text{m} = 4{,}0\ \text{J}$. Jos venytys kestää 0,50 s, teho on $P = 4{,}0\ \text{J} / 0{,}50\ \text{s} = 8{,}0\ \text{W}$.

Huomaa, että jousen loppupään voimalla 40 N laskettu $40\ \text{N} \cdot 0{,}20\ \text{m} = 8{,}0\ \text{J}$ olisi kaksinkertainen virhe: voima ei ollut 40 N koko matkalla.

## Yleinen virhekäsitys
Työ ei ole sama asia kuin ponnistelu. Kun pidät painoa paikallaan tai kannat sitä tasaisella lattialla, et tee fysiikan tarkoittamaa työtä painoon, vaikka väsyt. Työtä syntyy vain, kun voima siirtää kappaletta omaan suuntaansa. Toinen yleinen virhe on sotkea työ ja teho: suuri teho ei tarkoita suurta työtä, vaan nopeasti tehtyä työtä.

## Tiivistelmä
- Liikkeen suuntainen vakiovoima tekee työn $W = F s$. Muuttuvalla voimalla työ on (s,F)-kuvaajan pinta-ala.
- Voima, joka ei siirrä kappaletta omaan suuntaansa, ei tee työtä. Kantaminen tasaisella alustalla on fysiikassa nollatyötä.
- Työ siirtää energiaa: tehty työ kasvattaa kappaleen liike- tai potentiaalienergiaa.
- Teho on työ aikayksikössä, $P = W/t$. Yksiköt: 1 J = 1 N·m, 1 W = 1 J/s.
