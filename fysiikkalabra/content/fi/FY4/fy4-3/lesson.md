# Vuorovaikutus ja voima: Newtonin ensimmäinen ja kolmas laki

> **Miksi** curlingkivi liukuu jäällä kymmeniä metrejä, vaikka kukaan ei enää työnnä sitä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: curlinghalli. Vasemmalla heittäjä on liukunut matalassa heittoasennossa ja päästänyt kivestä irti, ja hänen ojennettu kätensä on jo kaukana kivestä. Keskellä punakahvainen curlingkivi liukuu jäällä oikealle, ja sen takana näkyy ohut jälki. Kaksi harjaajaa kulkee kiven edellä harjat jäätä vasten. Oikealla jäässä on maalialueen renkaat, joissa on jo kaksi kiveä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
### Voima on vuorovaikutus
Kun kaksi kappaletta vaikuttavat toisiinsa, niiden välillä on **vuorovaikutus**: käsi työntää laatikkoa, naru vetää pulkkaa ja Maa vetää omenaa. Vuorovaikutuksen voimakkuutta kuvaa **voima**, jonka yksikkö on newton ($\text{N}$). Voima on vektori, jolla on suuruus ja suunta, ja sitä merkitään $\overline{F}$. Jokaisella voimalla on aiheuttaja, joka on aina toinen kappale. Kosketusvoimissa kappaleet koskettavat toisiaan. Maan vetovoima eli **paino** $\overline{G}$ ja magneettien voimat vaikuttavat myös etäältä.

```pysahdy
Heitetty pallo lentää ilmassa. Mitkä kappaleet vaikuttavat palloon lennon aikana?
---
Maa (paino) ja ilma (ilmanvastus). Heittäjän käsi ei enää vaikuta palloon.
```

### Liike jatkuu ilman voimaa
Curlingin heittäjä työntää kiveä vain hetken. Kun käsi irtoaa, mikään ei enää työnnä kiveä eteenpäin, mutta kivi liukuu silti kymmeniä metrejä. Liu'un aikana kiveen vaikuttavat vain Maa ja jää (ilmanvastus on hyvin pieni). Pystysuunnassa paino ja jään tukivoima eli jään kiveä ylöspäin tukeva, pintaa vastaan kohtisuora voima kumoavat toisensa. Vaakasuunnassa on vain jään pieni kitkavoima eli pintojen välinen liikettä vastustava voima, joka osoittaa taaksepäin ja hidastaa kiveä hyvin vähitellen.

<svg data-fig="curling" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa liukuvasta curlingkivestä. Vasemmalla tilannekuva: kivi liukuu jäällä oikealle, ja sen yllä ohut sininen nuoli v näyttää nopeuden oikealle. Heittäjän käsi on jäänyt kauas taakse. Oikealla voimakuvio: kivi suorakulmiona. Paino G osoittaa keskipisteestä alas, jään tukivoima N alapinnasta ylös yhtä pitkänä, ja jään pieni kitkavoima alapinnan takakulmasta vasemmalle. Eteenpäin osoittavaa voimaa ei ole. Kuva ei ole mittakaavassa: kitkavoiman nuoli on piirretty selvyyden vuoksi todellista pidemmäksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-3-curling.webp" x="0" y="-1.2" width="600" height="352.5" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="227.5" y="131.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="455.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="479.5" y="87.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="336.5" y="199.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

Jos kitkaa ei olisi lainkaan, kiven nopeus ei muuttuisi, ja se liukuisi samaan suuntaan loputtomiin. Tämä on **Newtonin ensimmäinen laki** eli **jatkavuuden laki**: jos kappaleeseen vaikuttavien voimien summa on nolla, kappale pysyy levossa tai liikkuu suoraviivaisesti tasaisella nopeudella. Voimaa tarvitaan liikkeen *muuttamiseen*, ei liikkeen ylläpitämiseen. Kappaleen taipumusta säilyttää liiketilansa sanotaan **inertiaksi** eli hitaudeksi.

<figure class="unit-photo"><img src="pics/fy4/tug-of-war.webp" alt="Kolme miestä vetää paksua köyttä nojaten taaksepäin ja jalat maata vasten."><figcaption>Köydenvetäjät nojaavat taaksepäin ja painavat jalkansa maata vasten.</figcaption></figure>

Arkikokemus näyttää toista, koska maan päällä kitka ja ilmanvastus hidastavat lähes kaikkea, mikä liikkuu. Pyörä pysähtyy, kun polkeminen loppuu, koska tie ja ilma jarruttavat sitä, eivät siksi, että "liikkeen voima" kuluisi loppuun. Mitä pienempi kitka, sitä kauemmin liike jatkuu: jäällä pidemmälle kuin asfaltilla ja avaruudessa lähes rajatta.

```pysahdy
Miksi kaupan kärryt pysähtyvät, kun lakkaat työntämästä?
---
Kitka ja ilmanvastus muuttavat liikettä. Ilman niitä kärryt jatkaisivat samalla nopeudella.
```

### Voima ja vastavoima
Kun luistelija A työntää luistelijaa B, kumpikin lähtee liukumaan poispäin toisesta. B ei vain ota työntöä vastaan, vaan se vaikuttaa samalla A:han. Vuorovaikutus on aina kaksisuuntainen. Tämä on **Newtonin kolmas laki** eli **voiman ja vastavoiman laki**: kun kappale A vaikuttaa kappaleeseen B voimalla, B vaikuttaa A:han yhtä suurella mutta vastakkaissuuntaisella voimalla. Voima ja vastavoima syntyvät samassa vuorovaikutuksessa samaan aikaan, ja ne ovat samaa lajia: työntö ja vastatyöntö, vetovoima ja vastavetovoima.

<svg data-fig="luistelijat" viewBox="0 0 600 460" role="img" aria-label="Ylhäällä tilannekuva: kaksi luistelijaa seisoo jäällä vastakkain ja työntää toisiaan kämmenillä. Vasemmalla on suurikokoinen aikuinen A, oikealla pienempi lapsi B. Alhaalla kummankin voimakuvio erikseen, luistelija suorakulmiona. A:n kuviossa paino G A keskipisteestä alas, jään tukivoima N A alapinnasta ylös ja B:n voima A:han, F B A, joka osoittaa vasemmalle ja päättyy A:n oikeaan kylkeen. B:n kuviossa paino G B, joka on lyhyempi kuin A:n paino, tukivoima N B ja A:n voima B:hen, F A B, joka osoittaa oikealle ja päättyy B:n vasempaan kylkeen. Nuolet F B A ja F A B ovat yhtä pitkät. Kitka jätetään huomiotta." style="max-width:100%;font-size:24px">
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

<figure class="unit-photo"><img src="pics/fy4/falcon9-crew9-launch.webp" alt="Valkoinen raketti nousee pystysuoraan kirkkaan liekin ja savuvanan varassa. Laukaisualustan ympärillä on suuria valkoisia höyrypilviä ja ristikkomastoja."><figcaption>Falcon 9 -raketti nousee Floridassa syyskuussa 2024. Raketti työntää palamiskaasuja alaspäin, ja kaasut työntävät rakettia ylöspäin yhtä suurella voimalla. Raketti ei tarvitse ilmaa eikä maata, jota vasten työntää.</figcaption></figure>

Aikuinen ja lapsi saavat toisiltaan yhtä suuren voiman, vaikka aikuinen on paljon raskaampi. Lapsi lähtee silti liikkeelle suuremmalla nopeudella, koska pienemmän massan liiketila muuttuu samasta voimasta enemmän; tähän palataan luvussa *Newtonin toinen laki*. Tärkeintä on, että voima ja vastavoima vaikuttavat **eri kappaleisiin**. Siksi ne eivät koskaan kumoa toisiaan, eikä niitä piirretä saman kappaleen voimakuvioon.

```pysahdy
Potkaiset palloa jalallasi. Mikä voima vaikuttaa jalkaasi, kun jalka osuu palloon?
---
Pallo vaikuttaa jalkaasi yhtä suurella mutta vastakkaissuuntaisella voimalla eli vastavoimalla.
```

## Kaava: Newtonin ensimmäinen ja kolmas laki
Newtonin ensimmäinen laki on ehto kappaleeseen vaikuttavien voimien summalle:
```latex
\Sigma\overline{F} = \overline{0} \ \Leftrightarrow\ \overline{v} = \text{vakio}
```
missä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien vektorisumma eli **kokonaisvoima** (N) ja $\overline{v}$ kappaleen nopeus (m/s). Vakionopeus tarkoittaa, että sekä nopeuden suuruus että suunta pysyvät samoina; myös lepo $\overline{v} = \overline{0}$ on vakionopeus.

Kokonaisvoima nolla ei tarkoita, ettei voimia olisi, vaan että ne kumoavat toisensa. Suoralla tiellä tasaisella nopeudella ajavaan autoon vaikuttavat paino ja tien tukivoima pystysuunnassa sekä tien renkaisiin kohdistama voima eteenpäin ja ilmanvastus taaksepäin. Koska nopeus ei muutu, eteenpäin vievä voima on yhtä suuri kuin ilmanvastus, kun vierimisvastus jätetään huomiotta.

<svg data-fig="auto" viewBox="0 0 600 330" role="img" aria-label="Kaksi kuvaa autosta, joka ajaa suoralla tiellä tasaisella nopeudella. Vasemmalla tilannekuva: auto ja sen yllä ohut sininen nuoli v oikealle. Oikealla auton voimakuvio, auto suorakulmiona. Paino G keskipisteestä alas ja tien tukivoima N alapinnasta ylös, yhtä pitkinä. Tien voima F renkaisiin lähtee alapinnan etukulmasta eteenpäin. Ilmanvastus F v on työntö taaksepäin: nuoli tulee edestä, ja sen kärki on etupinnassa, johon ilma painaa. Vaakasuorat nuolet ovat yhtä pitkät, joten voimat kumoavat toisensa." style="max-width:100%;font-size:24px">
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
missä $\overline{F}_{AB}$ on voima, jolla kappale A vaikuttaa kappaleeseen B (N), ja $\overline{F}_{BA}$ voima, jolla B vaikuttaa A:han (N). Miinusmerkki kertoo, että voimat ovat vastakkaissuuntaiset; suuruudet ovat samat, $F_{AB} = F_{BA}$.

Laskuissa tarvitaan usein painon suuruutta:
```kaavat
kappaleeseen vaikuttava painovoima Maan pinnalla :: G = mg
```
missä $G$ on paino (N), $m$ kappaleen massa (kg) ja $g = 9{,}81\,\text{m/s}^2$ putoamiskiihtyvyys. Painon vastavoima on kappaleen yhtä suuri vetovoima Maahan.

## Esimerkki
Matkustajakone lentää vaakasuoraan suoraan eteenpäin tasaisella nopeudella $850\,\text{km/h}$. Kumpikin sen kahdesta suihkumoottorista työntää ilmaa ja palokaasuja taaksepäin $48\,\text{kN}$:n voimalla. Kuinka suuri on koneeseen kohdistuva ilmanvastus?

<!-- vaihe -->

**Tunnetut ja kysytty.** Yhden moottorin voima kaasuihin $F_1 = 48\,\text{kN}$ taaksepäin, moottoreita on kaksi, ja nopeus $850\,\text{km/h}$ pysyy samana suuruudeltaan ja suunnaltaan.

Kysytään ilmanvastusta $F_\text{v}$.

<!-- vaihe -->

**Periaate.** Newtonin kolmannen lain mukaan kaasut työntävät kutakin moottoria eteenpäin yhtä suurella voimalla $F_1$; se on moottorin työntövoima. Kone lentää suoraan tasaisella nopeudella, joten Newtonin ensimmäisen lain mukaan sen kokonaisvoima on nolla.

Vaakasuunnassa koneeseen vaikuttavat vain kaksi työntövoimaa $\overline{F}_1$ ja $\overline{F}_2$ eteenpäin (molemmat $48\,\text{kN}$) ja ilmanvastus $\overline{F}_\text{v}$ taaksepäin, joten ne kumoavat toisensa. Pystysuunnassa siipien nostovoima ja paino kumoavat toisensa. Voimakuviossa kone on suorakulmio ja siihen vaikuttavat voimat ovat nuolia:

<svg data-fig="kone" viewBox="0 0 600 330" role="img" aria-label="Kaksi kuvaa matkustajakoneesta, joka lentää vaakasuoraan tasaisella nopeudella. Vasemmalla tilannekuva: kone ja sen yllä ohut sininen nuoli v oikealle. Oikealla koneen voimakuvio, kone suorakulmiona. Paino G keskipisteestä alas ja siipien nostovoima F nosto ylös, yhtä pitkinä. Kahden moottorin työntövoimat F 1 ja F 2 lähtevät rungon etureunasta eteenpäin ja ovat yhtä pitkät. Ilmanvastus F v on työntö taaksepäin: nuoli tulee edestä, sen kärki on etureunassa, johon ilma painaa, ja se on yhtä pitkä kuin työntövoimat yhteensä. Vaakasuorat voimat kumoavat toisensa, ja pystysuorat voimat kumoavat toisensa." style="max-width:100%;font-size:24px">
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

**Kaava ratkaistuna.** Valitaan positiivinen suunta eteenpäin ja ratkaistaan ilmanvastus:
```latex
\begin{aligned}
&\Sigma F_x = 2F_1 - F_\text{v} = 0 \\
&F_\text{v} = 2F_1
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Nopeutta $850\,\text{km/h}$ ei tarvita: riittää tietää, että se ei muutu. Voimat ovat kilonewtoneina, joten tulos saadaan suoraan kilonewtoneina: $48\,\text{kN} = 48\,000\,\text{N}$.

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

**Tulos.** Ilmanvastus on $96\,\text{kN}$ eli $9{,}6\cdot 10^{4}\,\text{N}$ ja osoittaa taaksepäin. Moottorin voima $48\,\text{kN}$ tulkitaan tarkaksi arvoksi, joten ilmanvastus $96\,\text{kN}$ on tämän mallin tarkka arvo, eikä sitä tarvitse pyöristää.

<!-- vaihe -->

**Järkevyys.** Jos ilmanvastus olisi työntövoimia pienempi, kokonaisvoima osoittaisi eteenpäin ja kone kiihtyisi; jos suurempi, kone hidastuisi. Tasainen nopeus on mahdollinen vain, kun ilmanvastus on yhtä suuri kuin työntövoimien summa $2\cdot 48\,\text{kN}$. Sama päättely pätee kaikilla tasaisilla nopeuksilla: työntövoiman ja ilmanvastuksen summa on aina nolla.

Voimien suuruudet voivat silti olla eri nopeuksilla erilaiset, sillä ilmanvastus kasvaa nopeuden kasvaessa, joten suuremmalla tasaisella nopeudella tarvitaan myös suurempi työntövoima.

## Yleinen virhekäsitys
Moni ajattelee, että liikkuvaan kappaleeseen täytyy vaikuttaa voima liikkeen suuntaan ja että liike loppuu, kun tämä voima "kuluu loppuun". Ensimmäisen lain mukaan näin ei ole: liukuvaan curlingkiveen ei vaikuta mikään eteenpäin, ja se hidastuu vain kitkan takia. Toinen yleinen virhe on luulla, että voima ja vastavoima kumoavat toisensa. Ne vaikuttavat eri kappaleisiin: hevonen vetää kärryä ja kärry hevosta, mutta kärryn liikkeen ratkaisevat vain kärryyn vaikuttavat voimat. Kolmas virhe on pitää pöydällä lepäävän kirjan painoa ja pöydän tukivoimaa voimana ja vastavoimana. Ne ovat yhtä suuret ensimmäisen lain takia. Tukivoiman vastavoima on kirjan voima pöytään ja painon vastavoima kirjan vetovoima Maahan.

## Tiivistelmä
- Voima kuvaa kahden kappaleen vuorovaikutusta. Jokaisella voimalla on aiheuttaja, toinen kappale, ja voiman yksikkö on newton.
- Newtonin ensimmäinen laki: jos kokonaisvoima on nolla, kappale pysyy levossa tai liikkuu suoraviivaisesti tasaisella nopeudella.
- Voimaa tarvitaan liikkeen muuttamiseen, ei sen ylläpitämiseen. Liike hidastuu arjessa kitkan ja ilmanvastuksen takia.
- Newtonin kolmas laki: $\overline{F}_{AB} = -\overline{F}_{BA}$. Voima ja vastavoima ovat yhtä suuret, vastakkaissuuntaiset ja samaa lajia, ja ne vaikuttavat eri kappaleisiin, joten ne eivät kumoa toisiaan.
