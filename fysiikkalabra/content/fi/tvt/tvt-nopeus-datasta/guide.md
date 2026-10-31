Mittausdata on taulukko lukemia tasaisin tai epätasaisin väliajoin. Tässä ohjeessa lasket siitä nopeuden ja kuljetun matkan sen mukaan, mittasitko paikkaa, aikaa vai kiihtyvyyttä.

## Mihin tarvitset tätä

Tutkimuksessa *Pallon muotokertoimen määrittäminen* rajanopeus saadaan paikka–aika-kuvaajan kulmakertoimesta, tutkimuksessa *Leikkiauton nopeus ja lähtökorkeus* nopeus saadaan valoportin ajasta, ja tutkimuksessa *Hissin kulkema matka kiihtyvyydestä* matka lasketaan kiihtyvyysdatasta.

## Työvaiheet

Laskut tehdään Graphical Analysis Prossa laskettuina sarakkeina ([[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]]). Lausekkeissa sarakkeiden nimet ovat lainausmerkeissä, ja tässä ohjeessa ne ovat `t`, `x`, `v` ja `a`.

### Paikasta nopeus

1. **Ymmärrä keskinopeus.** Kun kappaleen paikka $x$ on mitattu hetkillä $t$, keskinopeus kahden mittauksen välillä on

    $$v = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}$$

    missä $\Delta x$ on siirtymä eli paikan muutos ja $\Delta t$ siihen kulunut aika; tässä $\Delta$ tarkoittaa muutosta. Lyhyellä välillä tulos on lähellä hetkellistä nopeutta, mutta paikan pienetkin mittausvirheet näkyvät siinä voimakkaasti, koska ne jaetaan lyhyellä ajalla. Siksi nopeutta ei lasketa peräkkäisten rivien erotuksista.

2. **Laske nopeus derivaattana.** Tee laskettu sarake `v`, yksikkö $\text{m/s}$, lausekkeella `firstDerivative("x","t",7)`. Ohjelma laskee jokaisen rivin nopeuden usean ympäröivän rivin avulla keskitetysti, jolloin mittausvirheet tasoittuvat. Viimeinen luku on käytettävien pisteiden määrä ($3$, $5$, $7$, …). Suurempi luku tasoittaa enemmän mutta pyöristää myös nopeita muutoksia. Lauseke on Pro-ominaisuus.

3. **Määritä hetkellinen nopeus kuvaajasta.** $(t, x)$-kuvaajassa hetkellinen nopeus on kuvaajan tangentin kulmakerroin kyseisellä hetkellä. Ota käyttöön **Graph Tools** -valikosta **Tangent**, niin ohjelma näyttää tangentin kulmakertoimen valitsemassasi kohdassa. Tasaisessa liikkeessä kuvaaja on suora, ja nopeus on [[ohje:tvt-suoran-sovitus|sovitetun suoran]] kulmakerroin. Sovita suora vain siihen osaan, jossa liike on tasaista. Jos paikka pienenee ajan kuluessa, kulmakerroin on negatiivinen, ja vauhti on sen itseisarvo.

### Valoportista nopeus

4. **Jaa liuskan leveys katkoajalla.** Kun kappaleen liuska, jonka leveys on $b$, katkaisee valoportin säteen ajaksi $\Delta t$, kappaleen keskinopeus portin kohdalla on $v = \tfrac{b}{\Delta t}$. Kapealla liuskalla se on lähellä hetkellistä nopeutta. Esimerkiksi $1{,}0\,\text{cm}$:n liuska ja katkoaika $0{,}020\,\text{s}$ antavat nopeuden $v = 0{,}010\,\text{m} : 0{,}020\,\text{s} = 0{,}50\,\text{m/s}$. Muunna leveys metreiksi ennen jakamista. Valoportin tila **Speed Through Gate** laskee saman ([[ohje:tvt-mittausohjelma|Anturit ja mittausohjelma]]), kun liuskan leveys on annettu oikein.

### Nopeudesta matka

5. **Ymmärrä pinta-ala suikaleina.** Siirtymä on $(t, v)$-kuvaajan ja aika-akselin välinen pinta-ala. Kun nopeus muuttuu, ala jaetaan kapeisiin suikaleisiin. Suikaleen leveys on aikaväli $\Delta t$ ja korkeus likimain sen aikainen nopeus, joten sen ala on siirtymä $\Delta s \approx v \cdot \Delta t$. Kun suikaleiden alat lasketaan yhteen, saadaan koko siirtymä. Kun kappale liikkuu koko ajan samaan suuntaan, siirtymä on sama kuin kuljettu matka $s$.

    <svg data-fig="strips" viewBox="0 0 600 340" role="img" aria-label="Kaaviokuva ilman lukuarvoja: nopeus v ajan t funktiona sinisenä käyränä. Nopeus kasvaa nollasta, pysyy jonkin aikaa vakiona ja pienenee takaisin nollaan. Käyrän ja aika-akselin välinen alue on jaettu kapeisiin pystysuoriin suikaleisiin, joiden leveys on delta t. Yksi suikale on korostettu: sen ala on likimain v kertaa delta t eli matka, joka kuljetaan sen aikana. Koko alue on kuljettu matka s." style="max-width:100%;font-size:24px">
  <line x1="79" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="281" x2="80" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,44 L86,57 L74,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="265.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="70" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <polygon points="104.5,280 104.5,280 129,254 129,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="104.4,280.0 104.4,280.0 128.8,253.8 128.8,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="129,280 129,254 153,196 153,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="128.8,280.0 128.8,253.8 153.1,196.0 153.1,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="153,280 153,196 177.5,138 177.5,280" fill="#a9d1f0" fill-opacity="1"/>
  <polygon points="153.1,280.0 153.1,196.0 177.5,138.2 177.5,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="177.5,280 177.5,138 202,112 202,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="177.5,280.0 177.5,138.2 201.9,112.0 201.9,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="202,280 202,112 226,112 226,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="201.9,280.0 201.9,112.0 226.2,112.0 226.2,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="226,280 226,112 250.5,112 250.5,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="226.2,280.0 226.2,112.0 250.6,112.0 250.6,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="250.5,280 250.5,112 275,112 275,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="250.6,280.0 250.6,112.0 275.0,112.0 275.0,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="275,280 275,112 299.5,112 299.5,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="275.0,280.0 275.0,112.0 299.4,112.0 299.4,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="299.5,280 299.5,112 324,112 324,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="299.4,280.0 299.4,112.0 323.8,112.0 323.8,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="324,280 324,112 348,112 348,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="323.8,280.0 323.8,112.0 348.1,112.0 348.1,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="348,280 348,112 372.5,138 372.5,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="348.1,280.0 348.1,112.0 372.5,138.2 372.5,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="372.5,280 372.5,138 397,196 397,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="372.5,280.0 372.5,138.2 396.9,196.0 396.9,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="397,280 397,196 421,254 421,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="396.9,280.0 396.9,196.0 421.2,253.8 421.2,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polygon points="421,280 421,254 445.5,280 445.5,280" fill="#d0e6fb" fill-opacity="1"/>
  <polygon points="421.2,280.0 421.2,253.8 445.6,280.0 445.6,280.0" fill="none" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/>
  <polyline points="85,280 88,280 91,280 94.5,280 97.5,280 100.5,280 104,280 107,279.5 110,278.5 113.5,276 116.5,273 119.5,269 123,264 126,258.5 129,253 132.5,246.5 135.5,239.5 138.5,232 142,224.5 145,216.5 148,208.5 151.5,200.5 154.5,192 158,184 161,176 164,168 167.5,160.5 170.5,153 173.5,146 177,139.5 180,133.5 183,128.5 186.5,123.5 189.5,119.5 192.5,116.5 196,114 199,112.5 202,112 205.5,112 208.5,112 211.5,112 215,112 218,112 221,112 224.5,112 227.5,112 230.5,112 234,112 237,112 240,112 243.5,112 246.5,112 249.5,112 253,112 256,112 259,112 262.5,112 265.5,112 268.5,112 272,112 275,112 278,112 281.5,112 284.5,112 287.5,112 291,112 294,112 297,112 300.5,112 303.5,112 306.5,112 310,112 313,112 316,112 319.5,112 322.5,112 325.5,112 329,112 332,112 335,112 338.5,112 341.5,112 344.5,112 348,112 351,112.5 354,114 357.5,116.5 360.5,119.5 363.5,123.5 367,128.5 370,133.5 373,139.5 376.5,146 379.5,153 382.5,160.5 386,168 389,176 392,184 395.5,192 398.5,200.5 402,208.5 405,216.5 408,224.5 411.5,232 414.5,239.5 417.5,246.5 421,253 424,258.5 427,264 430.5,269 433.5,273 436.5,276 440,278.5 443,279.5 446,280 449.5,280 452.5,280 455.5,280 459,280 462,280 465,280" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="80" y1="280" x2="470" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="153" y1="294" x2="177.5" y2="294" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="153" y1="288" x2="153" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="177.5" y1="288" x2="177.5" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="149" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta t$</div></foreignObject>
  <foreignObject x="90" y="72.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta s \approx v \cdot \Delta t$</div></foreignObject>
  <line x1="150.5" y1="103" x2="165.5" y2="187.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="202.5" y="181.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$s = \text{pinta-ala}$</span></div></foreignObject>
</svg>

6. **Laske pinta-ala ohjelmalla.** Kun tarvitset siirtymän tietyllä välillä, valitse väli vetämällä kuvaajan yli ja valitse **View Integral**. Kun tarvitset matkan jokaisella hetkellä, tee laskettu sarake `s`, yksikkö $\text{m}$, lausekkeella `integral("v","t")`. Se laskee suikaleiden alat yhteen ensimmäisestä rivistä nykyiseen riviin, joten matka alkaa arvosta $s = 0$.

### Kiihtyvyydestä nopeus ja matka

7. **Laske ensin nopeus, sitten matka.** Nopeuden muutos on $(t, a)$-kuvaajan pinta-ala, joten nopeus lasketaan kiihtyvyydestä samalla tavalla: tee sarake `v` lausekkeella `integral("a","t")` ja siitä sarake `s` lausekkeella `integral("v","t")`. Lasketun nopeuden alkuarvo on nolla, joten tulos on oikea, kun kappale on alussa levossa.

8. **Varo nollakohdan virhettä.** Jos jokaisessa kiihtyvyyslukemassa on sama pieni virhe $\delta a$, laskettuun nopeuteen kertyy virhettä $\delta a \cdot t$ ja matkaan $\tfrac{1}{2} \cdot \delta a \cdot t^2$. Virhe kasvaa siis ajan mukana, matkassa ajan neliönä. Määritä anturin nollakohta lepojakson lukemien keskiarvona valinnalla **View Statistics** ja vähennä se lukemista lasketussa sarakkeessa ennen integrointia. Tarkista lopuksi, palaako laskettu nopeus nollaan, kun kappale on pysähtynyt.

## Tavallisimmat virheet

- **Nopeus on laskettu peräkkäisistä riveistä kohinaisesta datasta.** Nopeus hyppii rivistä toiseen. Laske nopeus lausekkeella `firstDerivative("x","t",7)` tai sovita suora tasaisen liikkeen osaan.
- **Suora on sovitettu koko kuvaajaan, vaikka liike on tasaista vain osan ajasta.** Kulmakerroin on liian pieni. Rajaa sovitus tasaisen liikkeen osaan.
- **Liuskan leveys on jätetty millimetreiksi.** Nopeus on tuhatkertainen. Muunna leveys metreiksi.
- **Siirtymä ja matka on sekoitettu.** Kun kappale liikkuu välillä taaksepäin, nopeus ja pinta-ala ovat sillä välillä negatiivisia, eikä siirtymä ole kuljettu matka.
- **Nollakohtaa ei korjattu.** Laskettu nopeus ei palaa nollaan, vaikka kappale pysähtyi, ja matka kasvaa koko ajan. Korjaa nollakohta ennen integrointia.

## Tarkista ennen kuin jatkat

- Tiedät, onko laskemasi nopeus keskinopeus vai hetkellinen nopeus.
- Pinta-alan yksikkö on oikea: $(t, v)$-kuvaajasta $\text{m}$, $(t, a)$-kuvaajasta $\text{m/s}$.
- Kiihtyvyysdatasta laskettu nopeus palaa nollaan, kun kappale pysähtyy.
