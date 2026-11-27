# Vuorovaikutus ja voima: Newtonin ensimmäinen ja kolmas laki

> **Miksi** curlingkivi liukuu jäällä kymmeniä metrejä, vaikka kukaan ei enää työnnä sitä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: curlinghalli. Vasemmalla heittäjä on liukunut matalassa heittoasennossa ja päästänyt kivestä irti. Hänen ojennettu kätensä on jo kaukana kivestä. Keskellä punakahvainen curlingkivi liukuu jäällä oikealle, ja sen takana näkyy ohut jälki. Kaksi harjaajaa kulkee kiven edellä, ja harjat ovat jäätä vasten. Oikealla jäässä on maalialueen renkaat, joissa on jo kaksi kiveä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
### Voima on vuorovaikutus
Kun kaksi kappaletta vaikuttavat toisiinsa, niiden välillä on **vuorovaikutus**. Esimerkiksi käsi työntää laatikkoa, naru vetää pulkkaa ja Maa vetää omenaa. Vuorovaikutuksen voimakkuutta kuvaa **voima**. Voiman yksikkö on newton ($\text{N}$). Voima on vektori. Sillä on suuruus ja suunta, ja sitä merkitään $\overline{F}$. Jokaisella voimalla on aiheuttaja, ja aiheuttaja on aina toinen kappale. Kosketusvoimissa kappaleet koskettavat toisiaan. Maan vetovoima eli **paino** $\overline{G}$ ja magneettien voimat vaikuttavat myös kaukaa.

```pysahdy
Heität pallon ilmaan. Mikä vaikuttaa palloon, kun se lentää?
---
Maa vetää palloa alaspäin (paino). Myös ilma vaikuttaa siihen (ilmanvastus). Käsi ei enää vaikuta palloon.
```

### Liike jatkuu ilman voimaa
Curlingin heittäjä työntää kiveä vain hetken. Kun käsi irtoaa, mikään ei enää työnnä kiveä eteenpäin. Kivi liukuu silti kymmeniä metrejä. Liukumisen aikana kiveen vaikuttavat vain Maa ja jää. Ilmanvastus on hyvin pieni. Pystysuunnassa paino ja jään tukivoima kumoavat toisensa. Tukivoima on voima, joka tukee kiveä ylöspäin ja on kohtisuorassa pintaa vastaan. Vaakasuunnassa on vain jään pieni kitkavoima. Kitkavoima on pintojen välinen voima, joka vastustaa liikettä. Tässä se osoittaa taaksepäin ja hidastaa kiveä hyvin vähitellen.

<svg data-fig="curling" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa liukuvasta curlingkivestä. Vasemmalla on tilannekuva: kivi liukuu jäällä oikealle. Kiven yläpuolella ohut sininen nuoli v näyttää nopeuden oikealle. Heittäjän käsi on jäänyt kauas taakse. Oikealla on voimakuvio, jossa kivi on suorakulmio. Paino G osoittaa keskipisteestä alas. Jään tukivoima N osoittaa alapinnasta ylös ja on yhtä pitkä kuin paino. Jään pieni kitkavoima alkaa alapinnan takakulmasta ja osoittaa vasemmalle. Eteenpäin osoittavaa voimaa ei ole. Kuva ei ole mittakaavassa: kitkavoiman nuoli on piirretty selvyyden vuoksi todellista pidemmäksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-curling.webp" x="0" y="-1.2" width="600" height="352.5" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="227.5" y="131.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="455.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="479.5" y="87.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="336.5" y="199.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

Jos kitkaa ei olisi lainkaan, kiven nopeus ei muuttuisi. Kivi liukuisi samaan suuntaan loputtomiin. Tämä on **Newtonin ensimmäinen laki** eli **jatkavuuden laki**. Laki sanoo: jos kappaleeseen vaikuttavien voimien summa on nolla, kappale pysyy levossa tai liikkuu suoraan tasaisella nopeudella. Voimaa tarvitaan liikkeen *muuttamiseen*, ei liikkeen ylläpitämiseen. Kappaleen liiketila ei muutu itsestään. Tätä sanotaan **inertiaksi** eli hitaudeksi.

<figure class="unit-photo"><img src="pics/fy4/tug-of-war.webp" alt="Kolme miestä vetää köyttä ja nojaa taaksepäin."><figcaption>Köydenvetäjät nojaavat taaksepäin. He painavat jalkansa maata vasten.</figcaption></figure>

Arjessa näyttää siltä, että liike loppuu itsestään. Syy on se, että maan päällä kitka ja ilmanvastus hidastavat lähes kaikkea, mikä liikkuu. Pyörä pysähtyy, kun polkeminen loppuu, koska tie ja ilma jarruttavat sitä. Syy ei ole se, että "liikkeen voima" kuluisi loppuun. Mitä pienempi kitka on, sitä kauemmin liike jatkuu: jäällä pidemmälle kuin asfaltilla ja avaruudessa lähes loputtomiin.

```pysahdy
Miksi kaupan kärry pysähtyy, kun lakkaat työntämästä?
---
Kitka ja ilmanvastus hidastavat kärryä. Ilman niitä kärry liikkuisi samalla nopeudella eteenpäin.
```

### Voima ja vastavoima
Luistelija A työntää luistelijaa B. Silloin kumpikin lähtee liukumaan poispäin toisesta. B ei vain ota työntöä vastaan. B vaikuttaa samalla myös A:han. Vuorovaikutus on aina kaksisuuntainen. Tämä on **Newtonin kolmas laki** eli **voiman ja vastavoiman laki**. Kun kappale A vaikuttaa kappaleeseen B voimalla, B vaikuttaa A:han yhtä suurella mutta vastakkaisella voimalla. Voima ja vastavoima syntyvät samassa vuorovaikutuksessa samaan aikaan. Ne ovat samaa lajia: työntö ja vastatyöntö tai vetovoima ja vastavetovoima.

<svg data-fig="luistelijat" viewBox="0 0 600 460" role="img" aria-label="Ylhäällä on tilannekuva: kaksi luistelijaa seisoo jäällä vastakkain ja työntää toisiaan kämmenillä. Vasemmalla on suuri aikuinen A ja oikealla pienempi lapsi B. Alhaalla on kummankin voimakuvio erikseen, ja luistelija on suorakulmio. A:n kuviossa on paino G A keskipisteestä alas, jään tukivoima N A alapinnasta ylös ja B:n voima A:han, F B A. Se osoittaa vasemmalle ja päättyy A:n oikeaan kylkeen. B:n kuviossa on paino G B, joka on lyhyempi kuin A:n paino, tukivoima N B ja A:n voima B:hen, F A B. Se osoittaa oikealle ja päättyy B:n vasempaan kylkeen. Nuolet F B A ja F A B ovat yhtä pitkät. Kitka jätetään huomiotta." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-luistelijat.webp" x="0" y="-1.2" width="600" height="467.5" preserveAspectRatio="none"/>
  <foreignObject x="166" y="25.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="390" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <foreignObject x="111.5" y="417.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_A$</div></foreignObject>
  <foreignObject x="179.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_A$</div></foreignObject>
  <foreignObject x="229.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{BA}$</div></foreignObject>
  <foreignObject x="460.5" y="389" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_B$</div></foreignObject>
  <foreignObject x="390.5" y="288" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_B$</div></foreignObject>
  <foreignObject x="324.5" y="300.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{AB}$</div></foreignObject>
  <foreignObject x="93" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{A}$</div></foreignObject>
  <foreignObject x="495" y="320.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{B}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy4/falcon9-crew9-launch.webp" alt="Valkoinen raketti nousee suoraan ylös. Raketin alla on kirkas liekki ja maassa isoja valkoisia pilviä."><figcaption>Falcon 9 -raketti lähtee Floridassa vuonna 2024. Raketti työntää kaasuja alaspäin. Kaasut työntävät rakettia ylöspäin yhtä suurella voimalla. Raketti ei tarvitse ilmaa eikä maata, jota vasten työntää.</figcaption></figure>

Aikuinen ja lapsi saavat toisiltaan yhtä suuren voiman, vaikka aikuinen on paljon raskaampi. Lapsi lähtee silti liikkeelle suuremmalla nopeudella. Syy on se, että samasta voimasta pienemmän massan liike muuttuu enemmän. Tähän palataan luvussa *Newtonin toinen laki*. Tärkeintä on muistaa, että voima ja vastavoima vaikuttavat **eri kappaleisiin**. Siksi ne eivät kumoa toisiaan kummankaan kappaleen voimakuviossa. Siksi niitä ei myöskään piirretä saman kappaleen voimakuvioon.

### Kaksi tapaa valita systeemi
Saman työnnön voi katsoa kahdella tavalla. Systeemi tarkoittaa sitä kappaletta tai niitä kappaleita, joiden voimia tutkitaan. Jos systeemi on vain luistelija A, B:n työntö on ulkopuolinen voima $\overline{F}_{BA}$, joka vaikuttaa A:han. Se piirretään A:n voimakuvioon. Jos systeemi on A ja B yhdessä, vuorovaikutusparin voimat $\overline{F}_{AB}$ ja $\overline{F}_{BA}$ ovat systeemin sisäisiä voimia. Siksi vuorovaikutusparin voimia ei piirretä systeemin voimakuvioon. Siinä ovat vain ulkopuoliset voimat. Vasta nyt voimat kuuluvat samaan systeemiin. Ne ovat yhtä suuret ja vastakkaiset, joten niiden vektorisumma on $\overline{F}_{AB}+\overline{F}_{BA}=\overline{0}$. Kitka jätetään huomiotta.

<svg data-fig="systeemit" viewBox="0 0 600 470" role="img" aria-label="Kaksi voimakuviota samasta työnnöstä. Vasemmalla systeeminä on vain luistelija A, jonka ympärillä on katkoviiva. Hänen voimakuviossaan ovat paino G A, tukivoima N A ja B:n voima A:han, F B A, joka osoittaa vasemmalle. Oikealla systeeminä ovat luistelijat A ja B yhdessä, ja katkoviiva kulkee molempien ympäri. Voimakuviossa ovat vain ulkopuoliset voimat: A:n ja B:n yhteispaino ja yhteinen tukivoima. Vuorovaikutusparin voimat F A B ja F B A ovat sisäisiä, eikä niitä piirretä nuolina; niiden vektorisumma on nollavektori. Oikean puolen painon ja tukivoiman nuolet ovat yhtä pitkät. Kitka jätetään huomiotta." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43y-ice1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><linearGradient id="fy43y-ice2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <rect x="8" y="160" width="284" height="14" fill="url(#fy43y-ice1)"/>
  <rect x="308" y="160" width="284" height="14" fill="url(#fy43y-ice2)"/>
  <line x1="300" y1="20" x2="300" y2="450" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="83.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{systeemi: A}$</div></foreignObject>
  <foreignObject x="365" y="7.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{systeemi: A ja B}$</div></foreignObject>
  <path d="M112,123 L106.5,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M103,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="101" y1="160" x2="116" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M112,123 L117,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M113.5,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="111" y1="160" x2="126.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M103,125.5 Q110.5,84 122.5,91 L121.5,125.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M116,93.5 L138,100" fill="none" stroke="#1971c2" stroke-width="6.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="138" cy="100" r="3.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="118.5" cy="75" r="9.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M108.5,76 Q109,63 118.5,64 Q128,63 128.5,76 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,132.5 L194,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M196.5,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="198.5" y1="160" x2="187" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M190,132.5 L186.5,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M189,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="190.5" y1="160" x2="179" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M196.5,134 Q191,103 182,108.5 L183,134 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M187,110 L150,100" fill="none" stroke="#c92a2a" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="150" cy="100" r="2.7" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="185" cy="96.5" r="7.2" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M177.5,97 Q178,87.5 185,88 Q192.5,87.5 192.5,97 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="70" y="75.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="196" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <path d="M412,123 L406.5,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M403,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="401" y1="160" x2="416" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M412,123 L417,157" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M413.5,157.5 h10.5" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="411" y1="160" x2="426.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M403,125.5 Q410.5,84 422.5,91 L421.5,125.5 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M416,93.5 L438,100" fill="none" stroke="#1971c2" stroke-width="6.4" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="438" cy="100" r="3.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="418.5" cy="75" r="9.6" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M408.5,76 Q409,63 418.5,64 Q428,63 428.5,76 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M490,132.5 L494,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M496.5,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="498.5" y1="160" x2="487" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M490,132.5 L486.5,157.5" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M489,158 h-8" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="490.5" y1="160" x2="479" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="round"/>
  <path d="M496.5,134 Q491,103 482,108.5 L483,134 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M487,110 L450,100" fill="none" stroke="#c92a2a" stroke-width="4.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="450" cy="100" r="2.7" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="485" cy="96.5" r="7.2" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M477.5,97 Q478,87.5 485,88 Q492.5,87.5 492.5,97 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="370" y="75.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="496" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <rect x="60" y="44" width="86" height="120" rx="14" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-dasharray="8 6"/>
  <rect x="352" y="44" width="200" height="120" rx="14" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-dasharray="8 6"/>
  <line x1="8" y1="192" x2="592" y2="192" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="115" y="300" width="70" height="60" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="330" x2="150" y2="421" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,438 L142,420 L158,420 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="99.5" y="417.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_A$</div></foreignObject>
  <line x1="166" y1="360" x2="166" y2="269" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M166,252 L174,270 L158,270 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="169.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_A$</div></foreignObject>
  <line x1="242.5" y1="316" x2="202" y2="316" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M185,316 L203,308 L203,324 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="219.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{BA}$</div></foreignObject>
  <rect x="395" y="275" width="110" height="70" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="450" y1="310" x2="450" y2="401" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M450,418 L442,400 L458,400 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="340.5" y="401.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_A+\overline{G}_B$</div></foreignObject>
  <line x1="470" y1="345" x2="470" y2="254" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M470,237 L478,255 L462,255 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="500.5" y="244.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}_A+\overline{N}_B$</div></foreignObject>
  <foreignObject x="371" y="199.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\overline{F}_{AB}+\overline{F}_{BA}=\overline{0}$</div></foreignObject>
</svg>

```pysahdy
Potkaiset palloa jalalla. Mikä voima vaikuttaa jalkaasi, kun jalka osuu palloon?
---
Pallo työntää jalkaasi takaisin. Voima on yhtä suuri kuin potkusi voima, mutta se osoittaa vastakkaiseen suuntaan. Sitä sanotaan vastavoimaksi.
```

## Kaava: Newtonin ensimmäinen ja kolmas laki
Newtonin ensimmäinen laki on ehto kappaleeseen vaikuttavien voimien summalle:
```latex
\Sigma\overline{F} = \overline{0} \ \Leftrightarrow\ \overline{v} = \text{vakio}
```
Tässä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien vektorisumma eli **kokonaisvoima** (N). Merkintä $\overline{v}$ on kappaleen nopeus (m/s). Vakionopeus tarkoittaa, että nopeuden suuruus ja suunta pysyvät samoina. Myös lepo $\overline{v} = \overline{0}$ on vakionopeus.

Kokonaisvoima nolla ei tarkoita, että voimia ei olisi. Se tarkoittaa, että voimat kumoavat toisensa eli niiden yhteisvaikutus on nolla. Ajatellaan autoa, joka ajaa suoralla tiellä tasaisella nopeudella. Pystysuunnassa siihen vaikuttavat paino ja tien tukivoima. Vaakasuunnassa tie vaikuttaa renkaisiin voimalla eteenpäin, ja ilmanvastus vaikuttaa taaksepäin. Nopeus ei muutu. Siksi eteenpäin vievä voima on yhtä suuri kuin ilmanvastus, kun vierimisvastus jätetään huomiotta.

<svg data-fig="auto" viewBox="0 0 600 330" role="img" aria-label="Kaksi kuvaa autosta, joka ajaa suoralla tiellä tasaisella nopeudella. Vasemmalla on tilannekuva: auto ja sen yllä ohut sininen nuoli v oikealle. Oikealla on auton voimakuvio, ja auto on suorakulmio. Paino G osoittaa keskipisteestä alas ja tien tukivoima N alapinnasta ylös. Ne ovat yhtä pitkät. Tien voima F renkaisiin alkaa alapinnan etukulmasta ja osoittaa eteenpäin. Ilmanvastus F v on työntö taaksepäin. Nuoli tulee auton edestä, ja sen kärki on auton etupinnassa. Ilma painaa juuri etupintaa. Vaakasuorat nuolet ovat yhtä pitkät, joten voimat kumoavat toisensa." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-auto.webp" x="1.2" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="205.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="423.5" y="245.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="359.5" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="529.5" y="197.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="517.5" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
</svg>

Newtonin kolmas laki kirjoitetaan kahden kappaleen välisille voimille:
```latex
\overline{F}_{AB} = -\overline{F}_{BA}
```
Tässä $\overline{F}_{AB}$ on voima, jolla kappale A vaikuttaa kappaleeseen B (N), ja $\overline{F}_{BA}$ on voima, jolla B vaikuttaa A:han (N). Miinusmerkki kertoo, että voimat ovat vastakkaiset. Suuruudet ovat samat, $F_{AB} = F_{BA}$.

Laskuissa tarvitaan usein painon suuruutta:
```kaavat
kappaleeseen vaikuttava painovoima Maan pinnalla :: G = mg
```
Tässä $G$ on paino (N), $m$ on kappaleen massa (kg) ja $g = 9{,}81\,\text{m/s}^2$ on putoamiskiihtyvyys. Painon vastavoima on kappaleen yhtä suuri vetovoima Maahan.

## Esimerkki
Matkustajakone lentää vaakasuoraan suoraan eteenpäin tasaisella nopeudella $850\,\text{km/h}$. Koneessa on kaksi suihkumoottoria. Kumpikin moottori työntää ilmaa ja palokaasuja taaksepäin $48\,\text{kN}$:n voimalla. Kuinka suuri on koneeseen kohdistuva ilmanvastus?

<!-- vaihe -->

**Tunnetut ja kysytty.** Yhden moottorin voima kaasuihin on $F_1 = 48\,\text{kN}$ taaksepäin. Moottoreita on kaksi. Nopeus $850\,\text{km/h}$ pysyy samana, sekä suuruudeltaan että suunnaltaan.

Kysytään ilmanvastusta $F_\text{v}$.

<!-- vaihe -->

**Periaate.** Newtonin kolmannen lain mukaan kaasut työntävät kutakin moottoria eteenpäin yhtä suurella voimalla $F_1$. Tämä voima on moottorin työntövoima. Kone lentää suoraan tasaisella nopeudella, joten Newtonin ensimmäisen lain mukaan sen kokonaisvoima on nolla. Vaakasuunnassa koneeseen vaikuttavat kaksi työntövoimaa $\overline{F}_1$ ja $\overline{F}_2$ eteenpäin (molemmat $48\,\text{kN}$) ja ilmanvastus $\overline{F}_\text{v}$ taaksepäin.

Ne kumoavat toisensa. Pystysuunnassa siipien nostovoima ja paino kumoavat toisensa. Voimakuviossa kone on suorakulmio, ja siihen vaikuttavat voimat ovat nuolia:

<svg data-fig="kone" viewBox="0 0 600 330" role="img" aria-label="Kaksi kuvaa matkustajakoneesta, joka lentää vaakasuoraan tasaisella nopeudella. Vasemmalla on tilannekuva: kone ja sen yllä ohut sininen nuoli v oikealle. Oikealla on koneen voimakuvio, ja kone on suorakulmio. Paino G osoittaa keskipisteestä alas ja siipien nostovoima F nosto ylös. Ne ovat yhtä pitkät. Kahden moottorin työntövoimat F 1 ja F 2 alkavat rungon etureunasta ja osoittavat eteenpäin. Ne ovat yhtä pitkät. Ilmanvastus F v on työntö taaksepäin. Nuoli tulee koneen edestä, ja sen kärki on rungon etureunassa. Ilma painaa juuri etureunaa. Se on yhtä pitkä kuin työntövoimat yhteensä. Vaakasuorat voimat kumoavat toisensa, ja pystysuorat voimat kumoavat toisensa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy43k-body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient></defs>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <path d="M44,214 Q40,196 62,192 L226,190 Q262,188 276,176 L262,214 Q150,230 44,214 Z" fill="url(#fy43k-body)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M62,192 L48,150 L74,150 L104,192 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M138,200 L196,200 L120,250 L100,250 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="160" cy="238" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="130" cy="244" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="150" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="170" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="190" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="210" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="230" y="198" width="10" height="8" rx="2" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="124" y1="128" x2="198" y2="128" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M187,134.5 L200,128 L187,121.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="205.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <rect x="355" y="136" width="110" height="80" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="410" y1="176" x2="410" y2="239" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M410,256 L402,238 L418,238 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="371.5" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="390" y1="176" x2="390" y2="113" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M390,96 L398,114 L382,114 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="302.5" y="83.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{nosto}$</div></foreignObject>
  <line x1="465" y1="178" x2="486.5" y2="178" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M503.5,178 L485.5,186 L485.5,170 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="503" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <line x1="465" y1="206" x2="486.5" y2="206" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M503.5,206 L485.5,214 L485.5,198 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="503" y="195.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <line x1="542" y1="148" x2="482" y2="148" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M465,148 L483,140 L483,156 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="515.5" y="109.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Valitaan positiiviseksi suunnaksi eteenpäin. Ratkaistaan ilmanvastus:
```latex
\begin{aligned}
&\Sigma F_x = 2F_1 - F_\text{v} = 0 \\
&F_\text{v} = 2F_1
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Nopeutta $850\,\text{km/h}$ ei tarvita. Riittää tietää, että se ei muutu. Voimat ovat kilonewtoneina, joten tulos saadaan suoraan kilonewtoneina: $48\,\text{kN} = 48\,000\,\text{N}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan moottorin voima yksikköineen:
```latex
\begin{aligned}
F_\text{v} &= 2F_1 \\
&= 2\cdot 48\,\text{kN} \\
&= 96\,\text{kN}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ilmanvastus on $96\,\text{kN}$ eli $9{,}6\cdot 10^{4}\,\text{N}$, ja se osoittaa taaksepäin. Moottorin voima $48\,\text{kN}$ on tarkka arvo. Siksi ilmanvastus $96\,\text{kN}$ on tämän mallin tarkka arvo, eikä sitä tarvitse pyöristää.

<!-- vaihe -->

**Järkevyys.** Jos ilmanvastus olisi työntövoimia pienempi, kokonaisvoima osoittaisi eteenpäin ja kone kiihtyisi. Jos ilmanvastus olisi suurempi, kone hidastuisi. Tasainen nopeus on mahdollinen vain, kun ilmanvastus on yhtä suuri kuin työntövoimien summa $2\cdot 48\,\text{kN}$. Sama päättely pätee kaikilla tasaisilla nopeuksilla: työntövoiman ja ilmanvastuksen summa on aina nolla.

Voimien suuruudet voivat silti olla eri nopeuksilla erilaiset. Ilmanvastus kasvaa, kun nopeus kasvaa. Siksi suurempi tasainen nopeus tarvitsee myös suuremman työntövoiman.

## Yleinen virhekäsitys
Moni ajattelee, että liikkuvaan kappaleeseen täytyy vaikuttaa voima liikkeen suuntaan. Moni ajattelee myös, että liike loppuu, kun tämä voima "kuluu loppuun". Ensimmäisen lain mukaan näin ei ole. Liukuvaan curlingkiveen ei vaikuta mikään eteenpäin, ja se hidastuu vain kitkan takia.

Toinen yleinen virhe on luulla, että voima ja vastavoima kumoavat toisensa. Ne vaikuttavat eri kappaleisiin. Hevonen vetää kärryä ja kärry vetää hevosta, mutta kärryn liikkeen ratkaisevat vain kärryyn vaikuttavat voimat.

Kolmas virhe on pitää pöydällä lepäävän kirjan painoa ja pöydän tukivoimaa voimana ja vastavoimana. Ne ovat yhtä suuret ensimmäisen lain takia. Tukivoiman vastavoima on kirjan voima pöytään. Painon vastavoima on kirjan vetovoima Maahan.

## Tiivistelmä
- Voima kuvaa kahden kappaleen vuorovaikutusta. Jokaisella voimalla on aiheuttaja, toinen kappale. Voiman yksikkö on newton.
- Newtonin ensimmäinen laki: jos kokonaisvoima on nolla, kappale pysyy levossa tai liikkuu suoraan tasaisella nopeudella.
- Voimaa tarvitaan liikkeen muuttamiseen, ei sen ylläpitämiseen. Arjessa liike hidastuu kitkan ja ilmanvastuksen takia.
- Newtonin kolmas laki: $\overline{F}_{AB} = -\overline{F}_{BA}$. Voima ja vastavoima ovat yhtä suuret, vastakkaiset ja samaa lajia. Ne vaikuttavat eri kappaleisiin, joten ne eivät kumoa toisiaan kummankaan kappaleen voimakuviossa.
