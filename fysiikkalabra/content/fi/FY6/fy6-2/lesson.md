# Mittaukset virtapiirissä

> **Miksi** virtamittari kytketään piiriin eri tavalla kuin jännitemittari, ja mitä tapahtuu, jos kytkennät menevät sekaisin?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: koulun laboratorion työpöytä. Pöydällä on kytkentälevy, jossa paristokotelo ja lampunpidike ovat johdoilla samassa piirissä, ja lamppu palaa. Vieressä on harmaa digitaalinen yleismittari, jonka punainen ja musta mittajohto koskettavat lampunpidikkeen kahta napaa." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Virtamittari kytketään sarjaan
**Virtamittari** mittaa, kuinka suuri sähkövirta kulkee sen läpi. Siksi mitattavan virran on kuljettava mittarin kautta: piiri avataan siitä kohdasta, jonka virta halutaan tietää, ja mittari asetetaan aukkoon. Tällöin mittari on **sarjassa** muiden komponenttien kanssa. Haarattomassa piirissä virta on joka kohdassa sama, koska varausta ei katoa eikä kerry minnekään. Lamppu muuttaa sähköenergiaa valoksi ja hehkulangan sisäenergiaksi, mutta se ei kuluta virtaa. Virtamittari voidaan siis kytkeä mihin tahansa kohtaan haaratonta piiriä, ja se näyttää aina saman lukeman.

### Jännitemittari kytketään rinnalle
Jännite on kahden pisteen välinen suure (luku *Virtapiiri, sähkövirta ja jännite*). **Jännitemittari** mittaa jännitteen niiden kahden pisteen välillä, joihin sen johdot kosketetaan. Lampun jännite mitataan koskettamalla lampun kumpaakin napaa: piiriä ei avata, vaan mittari tulee lampun **rinnalle**. Mittarin punainen johto kosketetaan siihen napaan, joka on lähempänä pariston plusnapaa, jolloin lukema on positiivinen.

<svg data-fig="connections" viewBox="0 0 600 344" role="img" aria-label="Kaksi kytkentäkaaviota. Vasemmalla paristo, lamppu ja virtamittari A ovat samassa silmukassa peräkkäin: virtamittari on sarjassa lampun kanssa, ja sama virta I kulkee pariston, mittarin ja lampun läpi. Oikealla paristo ja lamppu muodostavat silmukan, ja jännitemittari V on kytketty lampun napojen väliin lampun rinnalle. Violetit nuolet näyttävät virran suunnan pariston plusnavasta miinusnapaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-connections.webp" x="0" y="0" width="600" height="355" preserveAspectRatio="none"/>
  <foreignObject x="98" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="64" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="71" y="275.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virtamittari}$</div></foreignObject>
  <foreignObject x="102.5" y="305.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sarjaan}$</div></foreignObject>
  <foreignObject x="436" y="34.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="356" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="358.5" y="275.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jännitemittari}$</div></foreignObject>
  <foreignObject x="396" y="305.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rinnalle}$</div></foreignObject>
</svg>

```pysahdy
Digitaalisen jännitemittarin punainen johto kosketetaan lampun siihen napaan, joka on kauempana pariston plusnavasta. Mitä lukema näyttää?
---
Lukema on negatiivinen, koska punainen johto ei ole plusnavan puoleisessa navassa.
```

### Yleismittari
Laboratoriossa virtaa ja jännitettä mitataan yleensä **yleismittarilla**: sama laite mittaa valitsimen asennosta riippuen jännitettä, virtaa ja usein muitakin suureita. Kuvan esimerkkimittarissa musta johto kytketään COM-liittimeen. Punainen johto kytketään jännitettä ja pieniä virtoja mitattaessa liittimeen $\text{V}\ \text{mA}$ ja suuria virtoja mitattaessa liittimeen $10\,\text{A}$. Eri yleismittareiden liittimet ja enimmäisvirrat voivat poiketa toisistaan, joten tarkista aina käytettävän mittarin omat merkinnät ja käyttöohje. Valitsimella valitaan sekä suure että **mittausalue**, joka on suurin arvo, jonka mittari tällä asennolla näyttää. Alueella $20\,\text{V}$ näyttö näyttää enintään $19{,}99\,\text{V}$; suuremmalla jännitteellä näyttöön tulee OL (engl. *overload*), mikä tarkoittaa, että arvo on yli mittausalueen.

<svg data-fig="multimeter" viewBox="0 0 600 360" role="img" aria-label="Piirros digitaalisesta yleismittarista. Ylhäällä näyttö, jossa on lukema 1,500 V. Keskellä valitsin, jonka ympärillä ovat mittausalueet 2 V, 20 V, 200 mA ja 10 A; osoitin on alueella 2 V. Alhaalla kolme liitintä: COM, V mA ja 10 A. Mustan johdon paikka on COM ja punaisen V mA tai 10 A. Oikealla selitteet näyttö, valitsin ja liittimet." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-multimeter.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="72" y="50" width="150" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:40px">$1{,}500$</div></foreignObject>
  <foreignObject x="228" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="86.5" y="179" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffc078">$2\,\text{V}$</div></foreignObject>
  <foreignObject x="109.5" y="132.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$20\,\text{V}$</div></foreignObject>
  <foreignObject x="180" y="132.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$200\,\text{mA}$</div></foreignObject>
  <foreignObject x="222" y="179" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <foreignObject x="87.5" y="307.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{COM}$</div></foreignObject>
  <foreignObject x="155.5" y="307.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{V}\ \text{mA}$</div></foreignObject>
  <foreignObject x="221" y="307.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$10\,\text{A}$</div></foreignObject>
  <foreignObject x="358" y="58.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{näyttö}$</div></foreignObject>
  <foreignObject x="358" y="191.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{valitsin}$</div></foreignObject>
  <foreignObject x="358" y="275.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{liittimet}$</div></foreignObject>
</svg>

### Mittausalueen valinta
Pienemmällä alueella näyttö näyttää lisää desimaaleja. Alueella $20\,\text{V}$ lampun jännite näkyy muodossa $1{,}50\,\text{V}$, alueella $2\,\text{V}$ muodossa $1{,}500\,\text{V}$: viimeinen numero kertoo **resoluution** eli pienimmän askeleen, jonka näyttö voi ottaa. Siksi mitataan pienimmällä alueella, jolle lukema vielä mahtuu. Kun suuruusluokkaa ei tiedetä, aloitetaan suurimmalta alueelta ja siirrytään pienempään. Virtaa mitattaessa tämä on myös turvallisuuskysymys, koska liian suuri virta polttaa mittarin sulakkeen.

### Mittari vaikuttaa piiriin
Jokaisella komponentilla on **resistanssi**, joka kuvaa, kuinka voimakkaasti se vastustaa sähkövirtaa; suure tarkennetaan luvussa *Resistanssi ja Ohmin laki*. Sarjaan kytketyn virtamittarin resistanssi on hyvin pieni, jotta mittari ei juuri pienentäisi virtaa, jota se mittaa. Rinnalle kytketyn jännitemittarin resistanssi on hyvin suuri, esimerkiksi $10\,\text{M}\Omega$, jotta mittarin kautta ei juuri kulkisi virtaa komponentin ohi. Ihanteellinen mittari ei muuttaisi piiriä lainkaan; todellinen muuttaa sitä vähän, mikä on yksi mittausepävarmuuden lähde.

Väärin kytketty mittari muuttaa piiriä paljon. Jos virtamittari kytketään lampun rinnalle, virta kulkee lähes kokonaan pienen resistanssin mittarin kautta lampun ohi: lamppu sammuu, ja virta voi kasvaa niin suureksi, että mittarin sulake palaa. Kun sulake on palanut, mittari on poissa piiristä ja lamppu syttyy uudelleen. Tällaista virtatietä, joka ohittaa komponentin, sanotaan oikosuluksi. Virtamittaria ei saa kytkeä jännitelähteen napojen rinnalle. Koululaboratoriossa mittaukset tehdään opettajan ohjeistamilla turvallisilla pienjännitelähteillä. Jos taas jännitemittari kytketään sarjaan, sen suuri resistanssi pienentää koko piirin virran lähes nollaan: lamppu sammuu, ja mittari näyttää suunnilleen pariston jännitteen.

<svg data-fig="wrong" viewBox="0 0 600 352" role="img" aria-label="Kaksi väärää kytkentää. Vasemmalla virtamittari A on kytketty lampun rinnalle. Virta kulkee lähes kokonaan pienen resistanssin virtamittarin kautta, mitä kuvaa paksu violetti nuoli: lamppu ei pala, ja virta on suuri. Oikealla jännitemittari V on sarjassa lampun kanssa. Mittarin suuri resistanssi pienentää virran lähes nollaan, joten lamppu ei pala eikä virtanuolia ole." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-2-wrong.webp" x="0" y="0" width="600" height="361.2" preserveAspectRatio="none"/>
  <foreignObject x="145" y="42.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="112" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="168" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="66" y="143.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\text{suuri } I$</div></foreignObject>
  <foreignObject x="71" y="283.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virtamittari}$</div></foreignObject>
  <foreignObject x="96" y="313.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rinnalle}$</div></foreignObject>
  <foreignObject x="387" y="102.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="412" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="468" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="427.5" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \approx 0$</div></foreignObject>
  <foreignObject x="358.5" y="283.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jännitemittari}$</div></foreignObject>
  <foreignObject x="402.5" y="313.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sarjaan}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/multimeter-breadboard.webp" alt="Punainen ja musta mittapää koskettavat kytkentälevyä, jossa on vastus ja punainen LED."><figcaption>Yleismittarin mittapäät kytkentälevyllä. Kun mittapäät asetetaan piirin kahteen kohtaan, mittari kytkeytyy rinnan näiden kohtien välisen osan kanssa ja mittaa sen jännitettä.</figcaption></figure>

```pysahdy
Virtamittari kytketään vahingossa lampun rinnalle. Mitä lampulle tapahtuu ja miksi?
---
Lamppu sammuu, koska virta kulkee lähes kokonaan pienen resistanssin mittarin kautta lampun ohi. Tämä on oikosulku.
```

## Kaava: Yleismittarin virheraja

### Valmistajan ilmoittama virheraja
Mittarin lukema ei ole täsmälleen mitattavan suureen todellinen arvo. Digitaalisen mittarin valmistaja ilmoittaa käyttöohjeessa jokaiselle alueelle **virherajan** muodossa $\pm(p + n\ \text{numeroa})$: virheraja on prosenttiosuus $p$ lukemasta lisättynä $n$:llä viimeisen numeron askeleella. Valmistajan ilmoittama virheraja kertoo, kuinka paljon kunnossa olevan ja ohjeiden mukaan käytetyn mittarin lukema voi enintään poiketa todellisesta arvosta. Mittauksen kokonaisepävarmuuteen voivat kuitenkin vaikuttaa myös mittausmenetelmä, mittarin vaikutus piiriin ja muut virhelähteet.

| Alue | Resoluutio | Virheraja |
|---|---|---|
| jännite $2\,\text{V}$ | $0{,}001\,\text{V}$ | $\pm(0{,}5\,\% + 2\ \text{numeroa})$ |
| jännite $20\,\text{V}$ | $0{,}01\,\text{V}$ | $\pm(0{,}5\,\% + 2\ \text{numeroa})$ |
| virta $200\,\text{mA}$ | $0{,}1\,\text{mA}$ | $\pm(1{,}0\,\% + 2\ \text{numeroa})$ |
| virta $10\,\text{A}$ | $0{,}01\,\text{A}$ | $\pm(2{,}0\,\% + 3\ \text{numeroa})$ |

### Virherajan laskeminen
Lukeman $x$ virheraja on
```latex
\Delta x = p \cdot x + n \cdot r
```
missä $\Delta x$ on virheraja, $x$ lukema, $p$ valmistajan ilmoittama prosenttiosuus desimaalilukuna ($0{,}5\,\% = 0{,}005$), $n$ numeroiden määrä ja $r$ alueen resoluutio. Tulos kirjataan muodossa $x \pm \Delta x$, esimerkiksi $U = 4{,}50\,\text{V} \pm 0{,}04\,\text{V}$. Merkintä on sama kuin virhearviossa, mutta tässä $\Delta x$ on mittarin oma virheraja, ei koko mittauksen epävarmuus. Eri mittausten tarkkuutta verrataan **suhteellisella virherajalla**
```latex
\frac{\Delta x}{x}
```
joka on paljas luku ja ilmoitetaan yleensä prosentteina.

```pysahdy
Mittarin alueella $2\,\text{V}$ lukema on $0{,}100\,\text{V}$. Resoluutio on $0{,}001\,\text{V}$ ja virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$. Kumpi virherajan osa on suurempi, prosenttiosa vai numeroiden osa?
---
Prosenttiosa on $0{,}005 \cdot 0{,}100\,\text{V} = 0{,}0005\,\text{V}$. Numeroiden osa on $2 \cdot 0{,}001\,\text{V} = 0{,}002\,\text{V}$, joten numeroiden osa on suurempi.
```

### Miksi pienin sopiva alue
Jos alueilla on sama $p$ ja sama $n$, kuten tämän mittarin jännitealueilla, prosenttiosa $p \cdot x$ on kaikilla alueilla sama, mutta numeroiden osuus $n \cdot r$ pienenee kymmenesosaan, kun siirrytään kymmenen kertaa pienemmälle alueelle. Kun lukema on pieni verrattuna alueeseen, numeroiden osuus hallitsee: $0{,}02\,\text{A}$:n virta alueella $10\,\text{A}$ on lähes arvaus, koska jo kolme viimeisen numeron askelta on $0{,}03\,\text{A}$.

<svg data-fig="error-bands" viewBox="0 0 600 312" role="img" aria-label="Kuva mittakaavassa: jännitteen akseli välillä 1,46 V–1,54 V. Ylempi jana näyttää alueella 20 V saadun lukeman 1,50 V ja sen virherajan ±0,03 V eli välin 1,47 V–1,53 V. Alempi jana näyttää alueella 2 V saadun lukeman 1,500 V ja sen virherajan ±0,010 V eli välin 1,490 V–1,510 V. Alemman alueen jana on noin kolmasosa ylemmän pituudesta." style="max-width:100%;font-size:24px">
  <line x1="120" y1="40" x2="120" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="40" x2="180" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="40" x2="240" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="40" x2="300" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="40" x2="360" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="40" x2="420" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="40" x2="480" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="252" x2="554" y2="252" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,252 L553,258 L553,246 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="252" x2="60" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="31" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}46$</div></foreignObject>
  <line x1="120" y1="252" x2="120" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="252" x2="180" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="151" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}48$</div></foreignObject>
  <line x1="240" y1="252" x2="240" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="252" x2="300" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="271" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}50$</div></foreignObject>
  <line x1="360" y1="252" x2="360" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="252" x2="420" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="391" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}52$</div></foreignObject>
  <line x1="480" y1="252" x2="480" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="252" x2="540" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="511" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}54$</div></foreignObject>
  <foreignObject x="488" y="211.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="60" y="27.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{alue } 20\,\text{V}$</div></foreignObject>
  <rect x="120" y="66" width="360" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="120" y1="58" x2="120" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="480" y1="58" x2="480" y2="98" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="78" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="492" y="63.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0{,}03\,\text{V}$</div></foreignObject>
  <foreignObject x="60" y="125.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{alue } 2\,\text{V}$</div></foreignObject>
  <rect x="240" y="164" width="120" height="24" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <line x1="240" y1="156" x2="240" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="360" y1="156" x2="360" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="176" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="372" y="161.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm 0{,}010\,\text{V}$</div></foreignObject>
</svg>

## Esimerkki
Lampun jännite mitataan yleismittarilla kahdesti. Alueella $20\,\text{V}$ näyttö näyttää $1{,}50\,\text{V}$ ja alueella $2\,\text{V}$ näyttö näyttää $1{,}500\,\text{V}$. Kummankin alueen virheraja on $\pm(0{,}5\,\% + 2\ \text{numeroa})$. Kuinka suuri on lukeman virheraja kummallakin alueella, ja kumpi alue kannattaa valita?

<!-- vaihe -->

**Tunnetut ja kysytty.** Lukemat $U_{20} = 1{,}50\,\text{V}$ (resoluutio $r_{20} = 0{,}01\,\text{V}$) ja $U_2 = 1{,}500\,\text{V}$ (resoluutio $r_2 = 0{,}001\,\text{V}$), $p = 0{,}5\,\%$ ja $n = 2$.

Kysytään virherajoja $\Delta U_{20}$ ja $\Delta U_2$.

<!-- vaihe -->

**Periaate.** Valmistajan virheraja on osuus lukemasta lisättynä kahdella viimeisen numeron askeleella. Lukema on molemmilla alueilla sama, joten alueet eroavat vain resoluutioltaan.

<!-- vaihe -->

**Kaava ratkaistuna.** Kaava antaa virherajan suoraan, kun resoluutioksi sijoitetaan kunkin alueen oma resoluutio:
```latex
\begin{aligned}
&\Delta U_{20} = p \cdot U_{20} + n \cdot r_{20} \\
&\Delta U_2 = p \cdot U_2 + n \cdot r_2
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Prosenttiosuus kirjoitetaan desimaalilukuna: $p = 0{,}5\,\% = 0{,}005$. Muita muunnoksia ei tarvita, koska lukemat ja resoluutiot ovat voltteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\Delta U_{20} \\
&= 0{,}005 \cdot 1{,}50\,\text{V} + 2 \cdot 0{,}01\,\text{V} \\
&= 0{,}0275\,\text{V} \\[6pt]
&\Delta U_2 \\
&= 0{,}005 \cdot 1{,}500\,\text{V} + 2 \cdot 0{,}001\,\text{V} \\
&= 0{,}0095\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Alueella $20\,\text{V}$ jännite on $1{,}50\,\text{V} \pm 0{,}03\,\text{V}$ ja alueella $2\,\text{V}$ $1{,}500\,\text{V} \pm 0{,}010\,\text{V}$. Suhteelliset virherajat ovat $2\,\%$ ja $0{,}67\,\%$. Virheraja pyöristetään kuten virhearvio yhteen merkitsevään numeroon, tai kahteen, jos ensimmäinen numero on 1. Alue $2\,\text{V}$ kannattaa valita: sen virheraja on noin kolmasosa.

<!-- vaihe -->

**Järkevyys.** Prosenttiosa on molemmilla alueilla sama, $0{,}0075\,\text{V}$. Ero tulee kokonaan numeroiden osuudesta, joka on alueella $20\,\text{V}$ kymmenkertainen, $0{,}02\,\text{V}$ eikä $0{,}002\,\text{V}$. Pienempi alue ei voi olla epätarkempi, kun lukema mahtuu sille ja alueiden prosenttiosa on sama.

## Yleinen virhekäsitys
Moni ajattelee, että suurin mittausalue on aina paras, koska sillä mittari ei mene yli alueen eikä sulake pala. Suurimmalta alueelta kannattaa kyllä aloittaa, kun suuruusluokkaa ei tiedetä, mutta lopullinen lukema luetaan pienimmältä alueelta, jolle arvo mahtuu. Suurella alueella viimeinen numero on karkea, ja pienen arvon virheraja voi olla yhtä suuri kuin itse lukema. Toinen yleinen virhe on kytkeä virtamittari komponentin rinnalle samaan tapaan kuin jännitemittari. Virtamittari kytketään aina sarjaan.

## Tiivistelmä
- Virtamittari kytketään sarjaan: piiri avataan ja mittari asetetaan aukkoon. Haarattomassa piirissä virta on joka kohdassa sama.
- Jännitemittari kytketään rinnalle eli niiden kahden pisteen väliin, joiden välinen jännite mitataan.
- Yleismittarin valitsimella valitaan suure ja mittausalue; OL tarkoittaa, että arvo on yli alueen. Musta johto kuuluu liittimeen COM.
- Mitataan pienimmällä alueella, jolle lukema mahtuu; tuntemattoman arvon mittaus aloitetaan suurimmalta alueelta.
- Virtamittarin resistanssi on hyvin pieni ja jännitemittarin hyvin suuri. Väärin kytkettynä virtamittari tekee oikosulun ja jännitemittari pysäyttää virran.
- Virheraja $\Delta x = p \cdot x + n \cdot r$ ja suhteellinen virheraja $\tfrac{\Delta x}{x}$.
