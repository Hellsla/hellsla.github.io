Anturi mittaa suuretta, ja Graphical Analysis Pro tallentaa sen lukemat tasaisin väliajoin. Näin saat mittaussarjan, jossa on satoja tai tuhansia lukemia, ja voit lukea siitä arvoja, keskiarvoja ja pinta-aloja.

## Mihin tarvitset tätä

Tutkimuksessa *Hypyn tutkiminen voimalevyllä* voimalevy tallentaa voiman ajan funktiona, tutkimuksessa *Kuuman veden jäähtyminen* lämpötila-anturi kirjaa lämpötilan pitkän ajan, ja tutkimuksessa *Liikemäärän säilyminen törmäyksissä* liikeanturit mittaavat vaunujen liikkeen.

## Työvaiheet

1. **Kytke ja tunnista anturi.** Valitse **Sensor Data Collection**. Kytke Go Direct -anturi USB-johdolla tai Bluetoothilla: langattoman anturin valitset luettelosta **Discovered Wireless Devices** ja painat **Connect**. Tarkista, että ohjelma näyttää oikean suureen ja yksikön. Kokeile, että lukema muuttuu, kun muutat mitattavaa suuretta, esimerkiksi painat voima-anturia kevyesti.

2. **Nollaa anturi, jos se on mahdollista.** Voima-anturi ja voimalevy nollataan kuormittamattomina, jotta lukema on nolla ilman voimaa. Napsauta anturin lukemaa ja valitse **Zero**. Lukema voi ajan mittaan ryömiä, joten nollaa ennen jokaista mittaussarjaa. Kirjaa, missä tilassa nollasit: jos nollaat punnustelineen roikkuessa anturissa, anturi näyttää vain lisätyn voiman.

3. **Valitse mittaustaajuus ja kesto.** Avaa **Data Collection Settings** ja valitse tilaksi **Time Based**. Mittaustaajuus kertoo, montako lukemaa anturi tallentaa sekunnissa. Nopea tapahtuma, kuten hyppy tai törmäys, vaatii suuren taajuuden, jotta lyhyt huippu ei jää kahden lukeman väliin. Hidas ilmiö, kuten jäähtyminen, ei tarvitse tiheää mittausta, mutta mittauksen on kestettävä koko ilmiön ajan. Kestoksi valitset kiinteän ajan (**End Collection: After Fixed Duration**) tai lopetat itse (**Manually**).

    <svg data-fig="sampling" viewBox="0 0 600 340" role="img" aria-label="Kaaviokuva ilman lukuarvoja: tasaisesta lukemasta nouseva lyhyt voimapulssi ajan funktiona punaisena käyränä. Tiheästi otetut näytteet, pienet mustat pisteet, seuraavat käyrää ja osuvat myös huipulle. Harvaan otetut näytteet, neliöt katkoviivalla yhdistettyinä, osuvat huipun molemmille puolille, joten niistä huippu näyttää paljon matalammalta kuin se on." style="max-width:100%;font-size:24px">
  <line x1="79" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="291" x2="80" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,44 L86,57 L74,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="70" y="13.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <polyline points="85,266.5 88,266.5 91,266.5 94.5,266.5 97.5,266.5 100.5,266.5 104,266.5 107,266.5 110,266.5 113.5,266.5 116.5,266.5 119.5,266.5 123,266.5 126,266.5 129,266.5 132.5,266.5 135.5,266.5 138.5,266.5 142,266.5 145,266.5 148,266 151.5,266 154.5,266 158,265.5 161,264.5 164,263.5 167.5,262.5 170.5,260.5 173.5,257.5 177,254 180,249.5 183,243.5 186.5,236.5 189.5,228 192.5,217.5 196,206 199,193.5 202,180 205.5,166 208.5,152.5 211.5,139.5 215,128.5 218,119 221,112.5 224.5,109 227.5,108.5 230.5,111.5 234,117.5 237,126 240,137 243.5,149.5 246.5,163 249.5,177 253,190.5 256,203.5 259,215 262.5,225.5 265.5,234.5 268.5,242 272,248 275,253 278,257 281.5,260 284.5,262 287.5,263.5 291,264.5 294,265 297,265.5 300.5,266 303.5,266 306.5,266.5 310,266.5 313,266.5 316,266.5 319.5,266.5 322.5,266.5 325.5,266.5 329,266.5 332,266.5 335,266.5 338.5,266.5 341.5,266.5 344.5,266.5 348,266.5 351,266.5 354,266.5 357.5,266.5 360.5,266.5 363.5,266.5 367,266.5 370,266.5 373,266.5 376.5,266.5 379.5,266.5 382.5,266.5 386,266.5 389,266.5 392,266.5 395.5,266.5 398.5,266.5 402,266.5 405,266.5 408,266.5 411.5,266.5 414.5,266.5 417.5,266.5 421,266.5 424,266.5 427,266.5 430.5,266.5 433.5,266.5 436.5,266.5 440,266.5 443,266.5 446,266.5 449.5,266.5 452.5,266.5 455.5,266.5 459,266.5 462,266.5 465,266.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="104.5,266.5 153,266 202,181 250.5,181 299.5,266 348,266.5 397,266.5 445.5,266.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="90" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="94.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="99.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="104.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="109" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="114" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="119" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="124" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="129" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="133.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="138.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="143.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="148" cy="266" r="3" fill="#1f2933"/>
  <circle cx="153" cy="266" r="3" fill="#1f2933"/>
  <circle cx="158" cy="265.5" r="3" fill="#1f2933"/>
  <circle cx="163" cy="264" r="3" fill="#1f2933"/>
  <circle cx="168" cy="262" r="3" fill="#1f2933"/>
  <circle cx="172.5" cy="258.5" r="3" fill="#1f2933"/>
  <circle cx="177.5" cy="253" r="3" fill="#1f2933"/>
  <circle cx="182.5" cy="245" r="3" fill="#1f2933"/>
  <circle cx="187" cy="234" r="3" fill="#1f2933"/>
  <circle cx="192" cy="219.5" r="3" fill="#1f2933"/>
  <circle cx="197" cy="201.5" r="3" fill="#1f2933"/>
  <circle cx="202" cy="181" r="3" fill="#1f2933"/>
  <circle cx="207" cy="160" r="3" fill="#1f2933"/>
  <circle cx="211.5" cy="139.5" r="3" fill="#1f2933"/>
  <circle cx="216.5" cy="123" r="3" fill="#1f2933"/>
  <circle cx="221.5" cy="112" r="3" fill="#1f2933"/>
  <circle cx="226" cy="108" r="3" fill="#1f2933"/>
  <circle cx="231" cy="112" r="3" fill="#1f2933"/>
  <circle cx="236" cy="123" r="3" fill="#1f2933"/>
  <circle cx="241" cy="139.5" r="3" fill="#1f2933"/>
  <circle cx="246" cy="160" r="3" fill="#1f2933"/>
  <circle cx="250.5" cy="181" r="3" fill="#1f2933"/>
  <circle cx="255.5" cy="201.5" r="3" fill="#1f2933"/>
  <circle cx="260.5" cy="219.5" r="3" fill="#1f2933"/>
  <circle cx="265" cy="234" r="3" fill="#1f2933"/>
  <circle cx="270" cy="245" r="3" fill="#1f2933"/>
  <circle cx="275" cy="253" r="3" fill="#1f2933"/>
  <circle cx="280" cy="258.5" r="3" fill="#1f2933"/>
  <circle cx="285" cy="262" r="3" fill="#1f2933"/>
  <circle cx="289.5" cy="264" r="3" fill="#1f2933"/>
  <circle cx="294.5" cy="265.5" r="3" fill="#1f2933"/>
  <circle cx="299.5" cy="266" r="3" fill="#1f2933"/>
  <circle cx="304" cy="266" r="3" fill="#1f2933"/>
  <circle cx="309" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="314" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="319" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="324" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="328.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="333.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="338.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="343" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="348" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="353" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="358" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="363" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="367.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="372.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="377.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="382" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="387" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="392" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="397" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="402" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="406.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="411.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="416.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="421" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="426" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="431" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="436" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="441" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="445.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="450.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="455.5" cy="266.5" r="3" fill="#1f2933"/>
  <circle cx="460" cy="266.5" r="3" fill="#1f2933"/>
  <rect x="98.5" y="260.5" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <rect x="147" y="260" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <rect x="196" y="175" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <rect x="244.5" y="175" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <rect x="293.5" y="260" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <rect x="342" y="260.5" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <rect x="391" y="260.5" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <rect x="439.5" y="260.5" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <line x1="300" y1="92" x2="330" y2="92" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="342" y="77.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{todellinen voima}$</div></foreignObject>
  <circle cx="304" cy="128" r="3" fill="#1f2933"/>
  <circle cx="315" cy="128" r="3" fill="#1f2933"/>
  <circle cx="326" cy="128" r="3" fill="#1f2933"/>
  <foreignObject x="342" y="113.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tiheä näytteenotto}$</div></foreignObject>
  <line x1="300" y1="164" x2="330" y2="164" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <rect x="309" y="158" width="12" height="12" fill="#ffffff" stroke="#6b7480" stroke-width="2.5"/>
  <foreignObject x="342" y="149.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{harva näytteenotto}$</div></foreignObject>
</svg>

4. **Käynnistä mittaus tarvittaessa liipaisulla.** Lyhyen tapahtuman alku jää helposti tallentumatta. Kun valitset aloitukseksi **On a Triggering Event**, mittaus alkaa, kun valitun anturin lukema saavuttaa asettamasi kynnysarvon. Muuten aloita tallennus ennen tapahtumaa ja lopeta vasta sen jälkeen.

5. **Käytä tapahtumapohjaista mittausta, kun valitset arvot itse.** Tilassa **Event Based** anturin lukema tallennetaan vain hetkinä, jotka itse valitset. Valinnalla **Events with Entry** kirjoitat jokaiselle lukemalle oman arvon, esimerkiksi lampun etäisyyden tai punnusten massan, jolloin saat suoraan kuvaajan lukemasta sen funktiona.

6. **Tee koemittaus.** Kokeile asetuksia ennen varsinaista mittausta. Tarkista, että koko tapahtuma tallentuu, lukemat eivät jää kiinni mittausalueen ylärajaan ja kuvaajassa näkyvät tapahtuman tärkeät vaiheet.

7. **Lue arvoja kuvaajasta.** Työkalulla **Examine** näet napsauttamasi kohdan ajan ja lukeman. Lue näin esimerkiksi lepojakson lukema tai liikkeen huippuarvo.

8. **Rajaa väli tilastoille ja sovituksille.** Valitse kuvaajasta aikaväli vetämällä sen yli, esimerkiksi lepojakso, ja valitse **View Statistics**: saat välin lukemien keskiarvon. Samalla tavalla [[ohje:tvt-suoran-sovitus|sovitus]] tehdään vain valitulle välille, jossa malli pätee.

9. **Määritä pinta-ala.** Valitse väli ja valitse **View Integral**. Ohjelma laskee kuvaajan ja aika-akselin välisen pinta-alan valitulla välillä. Voima–aika-kuvaajan pinta-ala on voiman impulssi yksikössä $\text{N} \cdot \text{s}$, ja kiihtyvyys–aika-kuvaajan pinta-ala on nopeuden muutos yksikössä $\text{m/s}$.

10. **Tallenna ja vie data.** Tallenna mittaus ohjelman omana tiedostona (.gambl) ja kirjaa, mitä kukin mittaus esittää. Valinta **Export data as csv** vie taulukon CSV-tiedostoksi ja **Export graph as png** kuvaajan kuvaksi. Mittauksesta laskettavat uudet suureet tehdään laskettuina sarakkeina ([[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]]).

## Ohjelmakohtaisia vinkkejä

### Valoportti

Valoportti mittaa ajan $\Delta t$, jonka kappaleen liuska katkaisee valonsäteen. Kun liuskan leveys $b$ tunnetaan, kappaleen keskinopeus portin kohdalla on $v = \tfrac{b}{\Delta t}$. Mittaa leveys työntömitalla. Valitse valoportille tila **Photogate Timing** ja sen vaihtoehdoista mittaustapa, esimerkiksi **Speed Through Gate** nopeudelle portin kohdalla, **Linear Motion** useiden katkosten liikkeelle tai **Pendulum Period** heilurin jaksonajalle.

### Liikeanturi

Liikeanturi mittaa etäisyyttä kappaleeseen ja laskee siitä nopeuden ja kiihtyvyyden. Anturilla on vähimmäisetäisyys, jota lähempää se ei mittaa luotettavasti; tarkista se laitteen ohjeesta. Nopeus on yleensä positiivinen, kun kappale loittonee anturista, ja negatiivinen, kun se lähestyy. Pidä mittaussuunta vapaana muista esineistä.

### Puhelimella mitattu data

Jos mittaat puhelimen sovelluksella, tallenna mittaus CSV-tiedostona ja avaa se Graphical Analysis Prossa. Tarkista yksikkö ja se, sisältääkö kiihtyvyyslukema putoamiskiihtyvyyden.

## Tavallisimmat virheet

- **Anturia ei nollattu.** Lepolukema ei ole nolla, ja jokaisessa lukemassa on sama siirtymä. Pinta-alaan siirtymä kertyy koko mittausajalta.
- **Mittaustaajuus oli liian pieni.** Huippu näyttää kulmikkaalta tai matalammalta kuin toistetuissa mittauksissa. Kasvata taajuutta asetuksissa **Data Collection Settings** ja mittaa uudelleen.
- **Tapahtuman alku puuttuu.** Mittaus käynnistyi liian myöhään. Aloita aiemmin tai käytä liipaisua.
- **Lukema jäi mittausalueen ylärajaan.** Kuvaajassa on tasainen katto. Valitse suurempi mittausalue, jos laitteessa on sellainen, tai pienennä kuormaa.
- **Puhelimen lukemat ovat $g$:n kerrannaisia.** Jos lepolukema on noin $1{,}00$, kerro lukemat putoamiskiihtyvyydellä $9{,}81\,\text{m/s}^2$ lasketussa sarakkeessa.
- **Raakadataa ei tallennettu.** Analyysia ei voi tarkistaa eikä toistaa. Tallenna jokainen mittaus.

## Tarkista ennen kuin jatkat

- Anturi näyttää oikean suureen ja yksikön, ja se on nollattu, kun laite sen sallii.
- Mittaustaajuus ja kesto riittävät koko tapahtumaan.
- Mittaus on tallennettu, ja tiedät, mitä kukin tiedosto esittää.
