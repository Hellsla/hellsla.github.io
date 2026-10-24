# Työ ja energia

> **Miksi** painavan repun kantaminen tasaista käytävää pitkin ei fysiikan mielessä ole työtä, vaikka olkapäät väsyvät?

## Ydinajatus
Arkikielessä työ on mitä tahansa ponnistelua. Fysiikassa sana on tarkempi: voima tekee työtä vain, kun kappale siirtyy ja voimalla on komponentti siirtymän suunnassa. Kun kannat reppua vaakasuoraan, kannatteleva voimasi osoittaa ylös ja siirtymä on vaakasuora. Voima ja siirtymä ovat kohtisuorassa, joten työ on nolla. Lihakset väsyvät, koska ne kuluttavat energiaa pitääkseen voiman yllä, mutta reppuun ei siirry energiaa.

Työ on siis tapa siirtää energiaa kappaleesta toiseen. Energia puolestaan on kappaleen kyky tehdä työtä. Liikkuvalla kappaleella on liike-energiaa, ja maan pinnan yläpuolelle nostetulla kappaleella on potentiaalienergiaa. Kun teet kappaleeseen työtä, sen energia kasvaa täsmälleen tehdyn työn verran. Tämä on koko kurssin kantava ajatus: energia ei synny eikä katoa, se vain vaihtaa muotoa ja omistajaa.

Teho kertoo, kuinka nopeasti työ tehdään. Portaat ylös kävellen ja juosten teet saman työn, mutta juosten teho on suurempi, koska sama energia siirtyy lyhyemmässä ajassa. Sähkölaitteissa teho on tuttu luku: kiukaan 6 kW tarkoittaa, että se muuttaa sähköenergiaa lämmöksi 6000 joulea joka sekunti.

## Kaavat
Voiman tekemä työ, kun voiman ja siirtymän välinen kulma on α:
```latex
W = F s \cos\alpha
```
missä W on työ (J), F voiman suuruus (N), s siirtymän pituus (m) ja α voiman ja siirtymän välinen kulma. Yksi joule on työ, jonka yhden newtonin voima tekee yhden metrin matkalla: 1 J = 1 N·m.

Liike-energia ja painovoiman potentiaalienergia:
```latex
E_k = \tfrac{1}{2} m v^2 \qquad E_p = m g h
```
missä m on massa (kg), v nopeus (m/s), g = 9,81 m/s² ja h korkeus valitusta nollatasosta (m).

Teho on työ jaettuna siihen kuluneella ajalla. Tasaisessa liikkeessä, jossa voima on liikkeen suuntainen, teho voidaan laskea myös voiman ja nopeuden tulona:
```latex
P = \frac{W}{t} = F v
```
missä P on teho (W), t aika (s) ja v nopeus (m/s). Yksi watti on yksi joule sekunnissa: 1 W = 1 J/s.

## Esimerkki
Pulkkaa vedetään 30 m matka 60 N voimalla. Naru on 30° kulmassa maahan nähden, ja vetoon kuluu 25 s.

Työ: $W = F s \cos\alpha = 60\ \text{N} \cdot 30\ \text{m} \cdot \cos 30^\circ = 1559\ \text{J} \approx 1{,}6\ \text{kJ}$.

Teho: $P = W/t = 1559\ \text{J} / 25\ \text{s} = 62\ \text{W}$, eli samaa luokkaa kuin vanha hehkulamppu.

Huomaa, että narun kulma pienentää työtä: vain voiman vaakasuora komponentti $F\cos\alpha = 52\ \text{N}$ vetää pulkkaa eteenpäin. Jos naru olisi vaakasuorassa, työ olisi $60\ \text{N} \cdot 30\ \text{m} = 1800\ \text{J}$.

## Yleinen virhekäsitys
Työ ei ole sama asia kuin ponnistelu. Kun pidät painoa paikallaan tai kannat sitä tasaisella lattialla, et tee fysiikan tarkoittamaa työtä painoon, vaikka väsyt. Työtä syntyy vain, kun voima siirtää kappaletta omaan suuntaansa. Toinen yleinen virhe on sotkea työ ja teho: suuri teho ei tarkoita suurta työtä, vaan nopeasti tehtyä työtä.

## Tiivistelmä
- Työ on voiman siirtymän suuntaisen komponentin ja siirtymän tulo: $W = F s \cos\alpha$.
- Kohtisuora voima ei tee työtä. Kantaminen tasaisella alustalla on fysiikassa nollatyötä.
- Työ siirtää energiaa: tehty työ kasvattaa kappaleen liike- tai potentiaalienergiaa.
- Teho on työ aikayksikössä, $P = W/t$. Yksiköt: 1 J = 1 N·m, 1 W = 1 J/s.
