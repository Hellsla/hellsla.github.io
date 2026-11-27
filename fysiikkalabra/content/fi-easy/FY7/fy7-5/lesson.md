# Sähkömagneettinen induktio

> **Miksi** polkupyörän dynamo sytyttää lampun vain silloin, kun pyörä pyörii, vaikka dynamossa ei ole paristoa eikä akkua?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pyöräilijä ajaa hämärässä metsätiellä. Polkupyörän etupyörän navassa on dynamo, ja ohjaustangon lamppu loistaa. Valokeila osuu tiehen pyörän edessä. Taivas on illan sininen, ja tien reunalla on kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Faradayn havainto
Luvussa *Virtajohtimen ja käämin magneettikenttä* sähkövirta synnytti magneettikentän. Michael Faraday etsi vuosia ilmiötä, joka toimii toisin päin. Voisiko magneettikenttä synnyttää sähkövirran? Vuonna 1831 hän teki kokeita. Hän huomasi, että paikallaan oleva magneetti käämin vieressä ei tee mitään, vaikka magneetti olisi voimakas. Kun magneetti työnnetään käämiin, käämiin kytketyn jännitemittarin neula kääntyy. Kun magneetti on paikallaan käämin sisällä, neula palaa nollaan. Kun magneetti vedetään pois, neula kääntyy vastakkaiseen suuntaan. Jännite on sitä suurempi, mitä nopeammin magneettia liikutetaan. Jännite on suurempi myös silloin, kun käämissä on enemmän kierroksia. Sama tapahtuu, jos magneetti on paikallaan ja käämiä liikutetaan.

<svg data-fig="faraday" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa: Faradayn koe kolmessa vaiheessa. Jokaisessa kuvassa johdinkäämi on kytketty jännitemittariin. Vasemmalla sauvamagneetti työnnetään pohjoisnapa edellä kohti käämiä ja käämin sisään. Mittarin neula kääntyy oikealle. Keskellä magneetti on paikallaan käämin sisällä, ja neula on nollassa. Oikealla magneetti vedetään käämistä pois, ja neula kääntyy vasemmalle." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-faraday.webp" x="0" y="1.2" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="58.5" y="15.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sisään}$</div></foreignObject>
  <foreignObject x="21" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="63" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="35.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="233.5" y="15.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paikallaan}$</div></foreignObject>
  <foreignObject x="283" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="325" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="471" y="15.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ulos}$</div></foreignObject>
  <foreignObject x="421" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="463" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="435.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/shake-flashlight.webp" alt="Läpinäkyvä taskulamppu. Sen sisällä näkyy kuparinvärinen käämi."><figcaption>Taskulamppu, jota ravistetaan. Lampun sisällä on magneetti. Kun lamppua ravistaa, magneetti liikkuu käämin läpi. Magneettivuo käämin läpi muuttuu, ja käämiin syntyy jännite. Jännite lataa lampun.</figcaption></figure>

### Muutos synnyttää jännitteen
Ilmiötä sanotaan **sähkömagneettiseksi induktioksi**. Käämin päiden välille syntyvää jännitettä sanotaan **induktiojännitteeksi**. Kun käämin päät yhdistetään johtimella tai lampulla, piirissä kulkee induktiovirta. Käämiin syntyy jännite, kun käämin jokaisen kierroksen läpi kulkeva magneettivuo muuttuu. Esimerkiksi kun käämiä käännetään, vuo voi muuttua, vaikka magneettikenttä pysyy samana. Paikallaan oleva käämi voimakkaassa mutta muuttumattomassa kentässä ei saa jännitettä. Muutos voi syntyä monella tavalla. Magneetti tai käämi voi liikkua. Käämi voi kääntyä kentässä. Silmukan pinta-ala voi muuttua. Viereisen sähkömagneetin virran voi myös kytkeä päälle tai pois. Polkupyörän napadynamossa rengasmagneetti pyörii navan mukana kiinteiden käämien ympäri. Magneetti pyörii siis käämien suhteen, kun pyörä pyörii. Kun pyörä seisoo, mikään ei muutu, eikä lamppu pala.

```pysahdy
Käämi on voimakkaassa mutta muuttumattomassa magneettikentässä. Käämiä käännetään vähitellen niin, että sen taso on lopuksi kentän suuntainen. Syntyykö käämiin jännite?
---
Kyllä. Kun käämi kääntyy, sen läpi kulkeva magneettivuo muuttuu. Muutos synnyttää jännitteen.
```

### Magneettivuo
Muutoksen suuruutta mitataan **magneettivuolla**. Magneettivuo kertoo, kuinka paljon magneettikenttää kulkee silmukan läpi. Kenttä on homogeeninen, kun se on joka paikassa yhtä voimakas ja samansuuntainen. Oletetaan, että homogeeninen kenttä on kohtisuorassa silmukan tasoa vastaan. Silloin magneettivuo on
```kaavat
magneettivuo :: \Phi = BA
```
Kaavassa $\Phi$ on magneettivuo, $B$ on magneettivuon tiheys (T) ja $A$ on silmukan pinta-ala (m²). Vuon yksikkö on weber: $1\,\text{Wb} = 1\,\text{T}\cdot\text{m}^2$. Vuo on sitä suurempi, mitä voimakkaampi kenttä on ja mitä suurempi silmukka on. Jos silmukka käännetään vinoon, sen läpi kulkee vähemmän kenttäviivoja ja vuo pienenee. Kun silmukan taso on kentän suuntainen, yksikään kenttäviiva ei kulje silmukan läpi. Silloin vuo on nolla.

<svg data-fig="flux" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva sivulta, kolme osaa: vaakasuorat vihreät kenttäviivat osoittavat vasemmalta oikealle. Johdinsilmukka nähdään syrjästä kapeana soikiona. Vasemmalla silmukan taso on kohtisuorassa kenttää vastaan, ja viisi kenttäviivaa kulkee silmukan läpi. Vuo on B kertaa A. Keskellä silmukka on vinossa, ja sen läpi kulkee vain kolme viivaa. Vuo on pienempi. Oikealla silmukan taso on kentän suuntainen, eikä yksikään viiva kulje silmukan läpi. Vuo on nolla." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-flux.webp" x="-1.3" y="0" width="603" height="353" preserveAspectRatio="none"/>
  <foreignObject x="71" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi = BA$</div></foreignObject>
  <foreignObject x="271" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi < BA$</div></foreignObject>
  <foreignObject x="477.5" y="285.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Phi = 0$</div></foreignObject>
  <foreignObject x="28" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="90" y="25.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
</svg>

## Kaava: Induktiolaki
Faradayn havainnot tiivistyvät **induktiolakiin**. Käämiin syntyvä induktiojännite on verrannollinen kahteen asiaan. Ne ovat käämin läpi kulkevan magneettivuon muutosnopeus ja käämin kierrosten lukumäärä. Käämin keskimääräinen induktiojännite aikavälillä $\Delta t$ on
```kaavat
käämiin indusoituva jännite :: e_\text{ka} = -N\frac{\Delta\Phi}{\Delta t}
```
Kaavassa $e_\text{ka}$ on keskimääräinen induktiojännite (V) ja $N$ on käämin kierrosten lukumäärä. Suure $\Delta\Phi$ on yhden kierroksen läpi kulkevan magneettivuon muutos (Wb). Suure $\Delta t$ on aika (s), jonka kuluessa muutos tapahtuu. Kierrokset ovat sarjassa, joten jokainen kierros lisää jännitteeseen yhtä paljon. Yksiköt sopivat yhteen: $1\,\tfrac{\text{Wb}}{\text{s}} = 1\,\text{V}$. Miinusmerkki kertoo induktiojännitteen suunnan. Jännite vastustaa muutosta, joka sen synnyttää. Suuntaa käsitellään luvussa *Lenzin laki ja pyörrevirrat*. Jännitteen suuruus lasketaan yhtälöstä $|e_\text{ka}| = N \cdot |\Delta\Phi| : \Delta t$. Suuruus on aina positiivinen tai nolla. Jos vuo pysyy vakiona, suuruus on nolla. Suuruus on positiivinen myös silloin, kun vuo pienenee.

Jos vuo muuttuu tasaisella nopeudella, induktiojännite on koko aikavälin vakio. Se on yhtä suuri kuin keskiarvonsa, ja silloin merkitään lyhyesti $e$. Jos vuo muuttuu epätasaisesti, jännitteen hetkellinen arvo riippuu siitä, kuinka nopeasti vuo muuttuu juuri sillä hetkellä: $e(t) = -N\,\tfrac{\mathrm{d}\Phi}{\mathrm{d}t}$.

```pysahdy
Käämissä on $200$ kierrosta. Käämiä liikutetaan magneettikentässä. Sen yhden kierroksen läpi kulkeva magneettivuo muuttuu tasaisesti arvosta $0{,}030\,\text{Wb}$ arvoon $0{,}010\,\text{Wb}$ ajassa $0{,}50\,\text{s}$. Kuinka suuri on induktiojännitteen suuruus?
---
Vuon muutos yhden kierroksen läpi on $0{,}020\,\text{Wb}$. Jännite on $|e| = 200 \cdot 0{,}020\,\text{Wb} : 0{,}50\,\text{s} = 8{,}0\,\text{V}$.
```

### Vuon kuvaaja ja jännite
Osamäärä $\Delta\Phi : \Delta t$ on vuon kuvaajan $(t, \Phi)$ kulmakerroin. Kulmakerroin kertoo, kuinka jyrkästi kuvaaja nousee tai laskee. Jos kuvaaja on kaareva, hetkellinen muutosnopeus on kuvaajan tangentin kulmakerroin. Induktiojännite ei siis riipu siitä, kuinka suuri vuo on. Se riippuu siitä, kuinka jyrkästi vuo muuttuu. Alla kymmenen kierroksen käämi kulkee tasaisella vauhdilla magneettikentän alueen läpi. Kun käämi tulee kenttään, vuo kasvaa tasaisesti ja jännite on vakio. Kun käämi on kokonaan kentän sisällä, vuo on suurimmillaan mutta ei muutu. Silloin jännite on nolla. Kun käämi lähtee kentästä, vuo pienenee. Silloin jännite on yhtä suuri mutta vastakkaismerkkinen.

<svg data-fig="graph" viewBox="0 0 600 380" role="img" aria-label="Kaksi kuvaajaa mittakaavassa samalla aika-akselilla nollasta neljään sekuntiin. Kymmenen kierroksen neliön muotoinen käämi kulkee magneettikentän läpi. Käämin sivu on 0,10 m, vauhti 0,10 m/s ja kenttä 0,20 T. Ylempi kuvaaja: magneettivuo milliwebereinä on nolla 0,5 sekuntiin asti. Sitten se kasvaa tasaisesti arvoon 2,0 hetkellä 1,5 s ja pysyy vakiona 2,5 sekuntiin. Sen jälkeen se pienenee tasaisesti nollaan hetkellä 3,5 s. Alempi kuvaaja: induktiojännite millivoltteina on nolla, kun vuo ei muutu. Jännite on miinus 20, kun vuo kasvaa, ja plus 20, kun vuo pienenee. Katkoviivat hetkillä 0,5; 1,5; 2,5 ja 3,5 s yhdistävät kuvaajat. Kuvan oikeassa yläkulmassa lukee N = 10 kierrosta. Käämissä on siis 10 kierrosta." style="max-width:100%;font-size:24px">
  <line x1="141" y1="150" x2="141" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="150" x2="186" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="150" x2="230.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="150" x2="275.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="150" x2="320.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="150" x2="365.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="150" x2="410" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="150" x2="455" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="150" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="134" x2="500" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="118" x2="500" y2="118" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="102" x2="500" y2="102" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="86" x2="500" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="70" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="150" x2="514" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,150 L513,156 L513,144 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="151" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="150" x2="141" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="150" x2="186" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="150" x2="230.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="150" x2="275.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="150" x2="320.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="150" x2="365.5" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="410" y1="150" x2="410" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="150" x2="455" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="150" x2="500" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="134" x2="96" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="118" x2="96" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="102" x2="96" y2="102" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="86" x2="96" y2="86" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="70" x2="96" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="532" y="135.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Phi\ (\text{mWb})$</div></foreignObject>
  <line x1="141" y1="332" x2="141" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="332" x2="186" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="332" x2="230.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275.5" y1="332" x2="275.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="332" x2="320.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="332" x2="365.5" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="332" x2="410" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="455" y1="332" x2="455" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="332" x2="500" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="312" x2="500" y2="312" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="292" x2="500" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="252" x2="500" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="232" x2="500" y2="232" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="332" x2="96" y2="272" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="272" x2="514" y2="272" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,272 L513,278 L513,266 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="273" x2="96" y2="198" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,186 L102,199 L90,199 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141" y1="272" x2="141" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186" y1="272" x2="186" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="272" x2="230.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="275.5" y1="272" x2="275.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="272" x2="320.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365.5" y1="272" x2="365.5" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="410" y1="272" x2="410" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="455" y1="272" x2="455" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="272" x2="500" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="312" x2="96" y2="312" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="297.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="89" y1="292" x2="96" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="252" x2="96" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="232" x2="96" y2="232" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="532" y="257.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="155.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e\ (\text{mV})$</div></foreignObject>
  <foreignObject x="66" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="66" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="414" y="19.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$N = 10\ \text{kierrosta}$</div></foreignObject>
  <line x1="141" y1="70" x2="141" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="230.5" y1="70" x2="230.5" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="320.5" y1="70" x2="320.5" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="410" y1="70" x2="410" y2="332" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="176" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="265.5" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="355.5" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="445" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <polyline points="96,150 141,150 230.5,86 320.5,86 410,150 455,150" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,272 141,272 141,312 230.5,312 230.5,272 320.5,272 320.5,232 410,232 410,272 455,272" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

### Liikkuvan johtimen induktiojännite
Suora metallitanko liikkuu nopeudella $v$ kohtisuoraan homogeenista magneettikenttää $B$ vastaan. Tangon mukana liikkuvat myös sen johtavuuselektronit. Luvussa *Varatun hiukkasen liike sähkö- ja magneettikentässä* todettiin, että magneettikenttä kohdistaa liikkuvaan varaukseen voiman $F_\text{m} = evB$. Voima osoittaa tangon suuntaan, joten elektronit siirtyvät tangon toiseen päähän. Toiseen päähän jää elektronivajaus. Päiden välille syntyy sähkökenttä $E$, joka vetää elektroneja takaisin. Siirtyminen loppuu, kun sähköinen voima $F_\text{s} = eE$ kumoaa magneettisen voiman. Silloin $eE = evB$ eli $E = vB$. Homogeenisessa kentässä jännite on kentän ja pituuden tulo (luku *Homogeeninen sähkökenttä*). Tangon päiden välinen induktiojännite on siis
```latex
e = vBl
```
Kaavassa $v$ on tangon nopeus (m/s), $B$ on magneettivuon tiheys (T) ja $l$ on kentässä olevan tangon pituus (m). Kaava pätee, kun nopeus, tanko ja kenttä ovat keskenään kohtisuorassa.

<svg data-fig="rod" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva ylhäältä, ei mittakaavassa: kaksi vaakasuoraa metallikiskoa. Kiskojen vasemmat päät on yhdistetty jännitemittariin. Kiskojen päällä on pystysuora kuparitanko, joka liikkuu oikealle nopeudella v. Magneettikenttä osoittaa paperiin päin. Sitä kuvaavat tasavälein piirretyt vihreät ristit. Tangon keskellä on elektroni. Siihen magneettinen voima osoittaa alaspäin ja sähköinen voima ylöspäin. Elektroneja on kertynyt tangon alapäähän, joka on negatiivinen. Yläpää on positiivinen. Tangossa sähkökenttä osoittaa ylhäältä alas. Kiskojen välinen etäisyys on l. Se on tangon kenttään kuuluva pituus." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-rod.webp" x="1.2" y="0" width="597" height="365.7" preserveAspectRatio="none"/>
  <foreignObject x="42" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="483.5" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="348" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="348" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="247" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#8a5f22">$\overline{E}$</div></foreignObject>
  <foreignObject x="348" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{m}$</div></foreignObject>
  <foreignObject x="348" y="119.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{s}$</div></foreignObject>
  <foreignObject x="390" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="562" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$l$</div></foreignObject>
</svg>

```pysahdy
Tanko liukuu vauhdilla $2{,}0\,\text{m/s}$ kohtisuoraan kenttää $0{,}50\,\text{T}$ vastaan. Kentässä olevan tangon pituus on $0{,}30\,\text{m}$. Kuinka suuri jännite tangon päiden välille syntyy?
---
Nopeus, tanko ja kenttä ovat kohtisuorassa. Siksi $e = vBl = 2{,}0\,\text{m/s} \cdot 0{,}50\,\text{T} \cdot 0{,}30\,\text{m} = 0{,}30\,\text{V}$.
```

Saman tuloksen saa myös induktiolaista. Tanko liukuu kiskoilla. Kiskojen ja tangon rajaaman silmukan pinta-ala kasvaa ajassa $\Delta t$ määrällä $\Delta A = l \cdot v\Delta t$. Siksi vuo kasvaa määrällä $\Delta\Phi = Bl \cdot v\Delta t$. Jännitteen suuruus on $\Delta\Phi : \Delta t = vBl$. Kun kiskojen päät yhdistetään vastuksella, piirissä kulkee virta. Magneettikenttä kohdistaa virtaa kuljettavaan tankoon voiman $F = IlB$, kuten luvussa *Voima virtajohtimeen: sähkömoottori ja kaiutin*. Tämän voiman suuntaa ja energian säilymistä tutkitaan luvussa *Lenzin laki ja pyörrevirrat*.

## Esimerkki
Käämissä on $250$ kierrosta, ja sen poikkipinta-ala on $4{,}0\,\text{cm}^2$. Käämi on sähkömagneetin napojen välissä. Homogeeninen kenttä on käämin akselin suuntainen. Kun sähkömagneetin virtaa kasvatetaan, kentän magneettivuon tiheys kasvaa tasaisesti arvosta $0{,}10\,\text{T}$ arvoon $0{,}50\,\text{T}$ ajassa $0{,}20\,\text{s}$. Kuinka suuri induktiojännite käämin päiden välille syntyy?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kierrosten lukumäärä on $N = 250$ ja pinta-ala on $A = 4{,}0\,\text{cm}^2$. Magneettivuon tiheys on aluksi $B_1 = 0{,}10\,\text{T}$ ja lopuksi $B_2 = 0{,}50\,\text{T}$. Aika on $\Delta t = 0{,}20\,\text{s}$.

Kysytään induktiojännitteen suuruutta $|e|$.

<!-- vaihe -->

**Periaate.** Kenttä voimistuu, joten käämin läpi kulkeva magneettivuo muuttuu. Siksi käämiin syntyy induktiojännite induktiolain mukaan. Kenttä on akselin suuntainen eli kohtisuorassa kierrosten tasoa vastaan. Siksi yhden kierroksen vuo on $\Phi = BA$. Pinta-ala ei muutu, joten vuon muutos on $\Delta\Phi = (B_2 - B_1)A$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&|e| = N\frac{\Delta\Phi}{\Delta t} \\
&|e| = \frac{N(B_2 - B_1)A}{\Delta t}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Pinta-ala neliömetreinä: $A = 4{,}0\,\text{cm}^2 = 4{,}0 \cdot (0{,}01\,\text{m})^2 = 4{,}0 \cdot 10^{-4}\,\text{m}^2$. Muut suureet ovat SI-yksiköissä.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&|e| = \frac{N(B_2 - B_1)A}{\Delta t} \\
&= \frac{250 \cdot 0{,}40\,\text{T} \cdot 4{,}0 \cdot 10^{-4}\,\text{m}^2}{0{,}20\,\text{s}} \\
&= 0{,}20\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Käämin päiden välille syntyy $0{,}20\,\text{V}$:n induktiojännite niin kauan kuin kenttä kasvaa. Tulos annetaan kahdella merkitsevällä numerolla, koska pinta-alassa $4{,}0\,\text{cm}^2$ ja ajassa $0{,}20\,\text{s}$ on kaksi.

<!-- vaihe -->

**Järkevyys.** Yksiköt sopivat: $\tfrac{\text{T}\cdot\text{m}^2}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. Yksi kierros antaisi vain $1{,}6 \cdot 10^{-4}\,\text{Wb} : 0{,}20\,\text{s} = 0{,}80\,\text{mV}$. Kierroksia on $250$, joten jännite on $250$-kertainen. Kun kenttä lakkaa kasvamasta, vuo ei enää muutu ja jännite putoaa nollaan. Näin käy, vaikka kenttä on silloin voimakkaimmillaan.

## Yleinen virhekäsitys
Moni ajattelee, että magneettikenttä itse synnyttää jännitteen. Moni ajattelee myös, että voimakkaassa kentässä jännite on suuri. Induktiojännite syntyy kuitenkin vain **vuon muutoksesta**. Paikallaan oleva käämi voimakkaan magneetin vieressä ei saa jännitettä. Kentän sisällä tasaisesti liikkuvaan käämiin ei synny jännitettä, jos sen läpi kulkeva vuo ei muutu. Vuo ja sen muutosnopeus ovat eri asioita, samoin kuin paikka ja nopeus. Suuri vuo voi pysyä samana, ja nolla vuo voi muuttua nopeasti. Toinen yleinen virhe on unohtaa kierrosten lukumäärä $N$. Kolmas virhe on muuntaa pinta-ala väärin: $1\,\text{cm}^2 = 10^{-4}\,\text{m}^2$, ei $10^{-2}\,\text{m}^2$.

## Tiivistelmä
- Sähkömagneettisessa induktiossa käämiin syntyy induktiojännite, kun sen läpi kulkeva magneettivuo muuttuu. Jos vuo ei muutu, jännitettä ei synny.
- Magneettivuo on $\Phi = BA$, kun kenttä on kohtisuorassa silmukan tasoa vastaan. Yksikkö on weber, $1\,\text{Wb} = 1\,\text{T}\cdot\text{m}^2$.
- Induktiolain mukaan keskimääräinen induktiojännite on $e_\text{ka} = -N \cdot \Delta\Phi : \Delta t$. Sen suuruus on $|e_\text{ka}| = N \cdot |\Delta\Phi| : \Delta t$. Kun vuo muuttuu tasaisesti, jännite on vakio ja yhtä suuri kuin keskiarvonsa. Miinusmerkki kertoo suunnan.
- Kenttää vastaan kohtisuoraan liikkuvan tangon päiden välinen jännite on $e = vBl$. Magneettinen voima siirtää tangon elektroneja toiseen päähän.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: ravistelutaskulamppu pöydällä. Läpinäkyvän rungon sisällä on lieriön muotoinen magneetti, ja rungon keskellä on kuparinen käämi. Kun lamppua ravistellaan, magneetti liukuu käämin läpi edestakaisin. Lampun etupäässä oleva valodiodi loistaa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-5-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
