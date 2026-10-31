# Pallon muotokertoimen määrittäminen

> **Tutkimuskysymys:** Kuinka suuri on kevyen pallon muotokerroin, kun se määritetään pallon rajanopeudesta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kevyt pallo putoaa seinällä olevan pitkän mitta-asteikon edessä. Pallon paikka on piirretty tasaisin aikavälein. Kauempana kolmijalan päällä oleva puhelin kuvaa putoamista videolle." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10mh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10mh-floor" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10mh-wall)"/>
  <rect x="0" y="530" width="1200" height="70" fill="url(#fy10mh-floor)"/>
  <line x1="0" y1="550" x2="1200" y2="547" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="570" x2="1200" y2="567" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="590" x2="1200" y2="587" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="530" x2="1200" y2="530" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="380" y="30" width="50" height="500" rx="3" fill="#ffe8a3" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="380" y1="520" x2="404" y2="520" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="510" x2="392" y2="510" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="500" x2="392" y2="500" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="490" x2="392" y2="490" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="480" x2="392" y2="480" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="470" x2="404" y2="470" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="460" x2="392" y2="460" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="450" x2="392" y2="450" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="440" x2="392" y2="440" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="430" x2="392" y2="430" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="420" x2="404" y2="420" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="410" x2="392" y2="410" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="400" x2="392" y2="400" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="390" x2="392" y2="390" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="380" x2="392" y2="380" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="370" x2="404" y2="370" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="360" x2="392" y2="360" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="350" x2="392" y2="350" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="340" x2="392" y2="340" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="330" x2="392" y2="330" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="320" x2="404" y2="320" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="310" x2="392" y2="310" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="392" y2="300" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="290" x2="392" y2="290" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="280" x2="392" y2="280" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="270" x2="404" y2="270" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="260" x2="392" y2="260" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="250" x2="392" y2="250" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="240" x2="392" y2="240" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="230" x2="392" y2="230" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="220" x2="404" y2="220" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="210" x2="392" y2="210" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="200" x2="392" y2="200" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="190" x2="392" y2="190" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="180" x2="392" y2="180" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="170" x2="404" y2="170" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="160" x2="392" y2="160" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="150" x2="392" y2="150" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="140" x2="392" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="130" x2="392" y2="130" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="120" x2="404" y2="120" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="110" x2="392" y2="110" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="100" x2="392" y2="100" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="90" x2="392" y2="90" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="80" x2="392" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="70" x2="404" y2="70" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="60" x2="392" y2="60" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="50" x2="392" y2="50" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="40" x2="392" y2="40" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <g opacity="1.0"><circle cx="410" cy="60" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,84 L410,78 L413.5,84 Z" fill="#2b8a3e"/><path d="M399.5,56 Q400.5,48.5 408,47.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="410" cy="78.5" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,102.5 L410,96.5 L413.5,102.5 Z" fill="#2b8a3e"/><path d="M399.5,74.5 Q400.5,67 408,66" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="410" cy="124" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,148 L410,142 L413.5,148 Z" fill="#2b8a3e"/><path d="M399.5,120 Q400.5,112.5 408,111.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="410" cy="182.5" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,206.5 L410,200.5 L413.5,206.5 Z" fill="#2b8a3e"/><path d="M399.5,178.5 Q400.5,171 408,170" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="410" cy="245" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,269 L410,263 L413.5,269 Z" fill="#2b8a3e"/><path d="M399.5,241 Q400.5,233.5 408,232.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="410" cy="309" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,333 L410,327 L413.5,333 Z" fill="#2b8a3e"/><path d="M399.5,305.5 Q400.5,297.5 408,296.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="410" cy="373.5" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,397.5 L410,391.5 L413.5,397.5 Z" fill="#2b8a3e"/><path d="M399.5,370 Q400.5,362 408,361.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="410" cy="438.5" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,462.5 L410,456.5 L413.5,462.5 Z" fill="#2b8a3e"/><path d="M399.5,434.5 Q400.5,427 408,426" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="1.0"><circle cx="410" cy="503" r="19" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M406.5,527 L410,521 L413.5,527 Z" fill="#2b8a3e"/><path d="M399.5,499 Q400.5,491.5 408,490.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <line x1="1000" y1="530" x2="975" y2="420" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="1000" y1="530" x2="1025" y2="420" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="972" y1="530" x2="1000" y2="420" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="1000" y1="420" x2="1000" y2="380" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <rect x="992" y="300" width="16" height="100" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="992" cy="318" r="5" fill="#1f2933"/>
</svg>

Pudotettu ilmapallo tai kevyt jumppapallo ei kiihdy samalla tavalla kuin pieni ja painava kuula, koska ilma vastustaa sen liikettä. Kuinka voimakkaasti ilma vastustaa, riippuu kappaleen koosta, nopeudesta ja muodosta. Muodon vaikutusta kuvataan luvulla, jota kutsutaan **muotokertoimeksi**. Tässä tutkimuksessa kuvaat pallon putoamisen videolle ja määrität mittauksistasi pallon muotokertoimen. Mittaa, analysoi ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mitkä suureet sinun on mitattava, jotta saat muotokertoimen ilmanvastuksen mallista, saavuttaako pallo rajanopeuden ja kuinka suuri se on, ja kuinka suuri pallon muotokerroin on epävarmuuksineen verrattuna pallomaisen kappaleen kirjallisuusarvoon.

**Päätät itse:** pallon, pudotuspaikan ja -korkeuden, kameran paikan ja videon mittakaavan, toistojen määrän, sen, miten varmistat pallon saavuttaneen rajanopeuden ja miten määrität rajanopeuden videolta, sen, miten otat ilman nosteen huomioon, sekä tavan, jolla mittaat muut tarvittavat suureet ja arvioit tuloksen epävarmuuden. Osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, rajanopeuden riippuvuus pallon massasta, kuuluu työhösi: vertaa sen avulla saatua muotokerrointa päämittauksen tulokseen.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Miten pallon nopeus muuttuu pudotuksen aikana? Luonnostele ennustamasi nopeus–aika-kuvaaja.
2. Millaisen pudotusmatkan arvelet pallon tarvitsevan rajanopeuden saavuttamiseen, ja miten matka riippuu pallon massasta ja koosta? Mistä tunnistaisit videolta, että pallo on saavuttanut rajanopeuden?
3. Jos pallon massa kaksinkertaistuu mutta sen koko ja muoto pysyvät samoina, kaksinkertaistuuko rajanopeus, kasvaako se vähemmän vai enemmän?
4. Mikä mittaus on todennäköisesti epävarmin, ja miten se vaikuttaa tulokseen?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Muotokerrointa ei voi lukea mittarista, vaan se lasketaan muista suureista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitä voimia putoavaan palloon vaikuttaa, ja mitä niistä voi sanoa, kun pallon nopeus ei enää muutu?
2. Mitkä suureet sinun on mitattava tai selvitettävä, jotta saat muotokertoimen laskettua?
3. Miten saat rajanopeuden selville videolta?

## Teoriaa lyhyesti

Ilmanvastus $\overline{F}_\text{v}$ osoittaa pallon nopeutta vastaan, ja sen suuruus kasvaa, kun pallon nopeus kasvaa. Levosta pudotettu pallo kiihtyy aluksi, mutta kun ilmanvastus kasvaa riittävän suureksi, voimat kumoavat toisensa ja pallo jatkaa putoamista vakionopeudella. Tätä nopeutta kutsutaan **rajanopeudeksi** $v_\text{r}$. [[apua:fy4-14|Ilmanvastus ja rajanopeus]]

Palloon vaikuttaa lisäksi ilman noste $\overline{F}_\text{noste}$, joka osoittaa ylös. Raskaalla ja pienellä kappaleella noste on painoon verrattuna mitätön, mutta suurella ja kevyellä pallolla, kuten ilmapallolla, se on suuri: ilmapallon noste voi olla moninkertainen pallon kumikalvon painoon verrattuna. Rajanopeudella ilmanvastus on siis yhtä suuri kuin painon ja nosteen erotus, $F_\text{v} = G - F_\text{noste}$, kuten alla olevassa voimakuviossa. Paino $G$ sisältää tässä myös pallon sisällä olevan ilman painon.

<svg data-fig="setup" viewBox="0 0 600 420" role="img" aria-label="Kaaviokuva. Vasemmalla tilannekuva: pallo putoaa pystysuoran mitta-asteikon vieressä. Pallon paikat on piirretty tasaisin aikavälein: ylhäällä välit kasvavat, alhaalla ne ovat yhtä suuret. Alimman pallon vieressä on sininen nopeusnuoli alaspäin. Oikealla voimakuvio rajanopeudella: pallo on suorakulmio, paino G lähtee keskipisteestä alas, noste F_noste keskipisteen vierestä ylös ja ilmanvastus F_v alapinnasta ylös. Ilmapallolla noste on lähes yhtä pitkä kuin paino ja ilmanvastus lyhyt: ylöspäin osoittavat nuolet ovat yhteensä yhtä pitkät kuin paino, joten voimat kumoavat toisensa, F_v on G miinus F_noste. Nopeusnuoli alas on piirretty suorakulmion viereen." style="max-width:100%;font-size:24px">
  <line x1="300" y1="20" x2="300" y2="400" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 6"/>
  <foreignObject x="102.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilanne}$</div></foreignObject>
  <foreignObject x="358.5" y="11.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rajanopeudella}$</div></foreignObject>
  <rect x="70" y="60" width="30" height="330" rx="3" fill="#ffe8a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="70" y1="380" x2="86" y2="380" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="370" x2="78" y2="370" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="360" x2="78" y2="360" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="350" x2="78" y2="350" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="340" x2="78" y2="340" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="330" x2="86" y2="330" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="320" x2="78" y2="320" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="310" x2="78" y2="310" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="300" x2="78" y2="300" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="290" x2="78" y2="290" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="280" x2="86" y2="280" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="270" x2="78" y2="270" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="260" x2="78" y2="260" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="250" x2="78" y2="250" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="240" x2="78" y2="240" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="230" x2="86" y2="230" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="220" x2="78" y2="220" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="210" x2="78" y2="210" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="200" x2="78" y2="200" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="190" x2="78" y2="190" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="180" x2="86" y2="180" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="170" x2="78" y2="170" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="160" x2="78" y2="160" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="150" x2="78" y2="150" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="140" x2="78" y2="140" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="130" x2="86" y2="130" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="120" x2="78" y2="120" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="110" x2="78" y2="110" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="100" x2="78" y2="100" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="90" x2="78" y2="90" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="80" x2="86" y2="80" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="70" x2="78" y2="70" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="70" y1="60" x2="78" y2="60" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <g opacity="0.45"><circle cx="130" cy="76" r="14" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M127.5,95 L130,89 L132.5,95 Z" fill="#2b8a3e"/><path d="M122.5,73 Q123,67.5 128.5,67" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="130" cy="95" r="14" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M127.5,114 L130,108 L132.5,114 Z" fill="#2b8a3e"/><path d="M122.5,92 Q123,86.5 128.5,85.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="130" cy="139.5" r="14" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M127.5,158.5 L130,152.5 L132.5,158.5 Z" fill="#2b8a3e"/><path d="M122.5,136.5 Q123,131 128.5,130" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="130" cy="193.5" r="14" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M127.5,212.5 L130,206.5 L132.5,212.5 Z" fill="#2b8a3e"/><path d="M122.5,191 Q123,185 128.5,184.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="130" cy="250.5" r="14" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M127.5,269.5 L130,263.5 L132.5,269.5 Z" fill="#2b8a3e"/><path d="M122.5,247.5 Q123,242 128.5,241.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="0.45"><circle cx="130" cy="308" r="14" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M127.5,327 L130,321 L132.5,327 Z" fill="#2b8a3e"/><path d="M122.5,305.5 Q123,300 128.5,299" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <g opacity="1.0"><circle cx="130" cy="366" r="14" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/><path d="M127.5,385 L130,379 L132.5,385 Z" fill="#2b8a3e"/><path d="M122.5,363 Q123,357.5 128.5,357" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/></g>
  <line x1="178" y1="300" x2="178" y2="372" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M170,362 L178,378 L186,362" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="194" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <rect x="385" y="157" width="90" height="56" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="430" y1="185" x2="430" y2="298" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M430,315 L422,297 L438,297 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="437.5" y="296.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="450" y1="185" x2="450" y2="102" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M450,85 L458,103 L442,103 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="454.5" y="74.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{noste}$</div></foreignObject>
  <line x1="408" y1="243" x2="408" y2="230" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M408,213 L416,231 L400,231 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="351.5" y="228.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <line x1="540" y1="200" x2="540" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M533.5,267 L540,280 L546.5,267" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="545.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="377.5" y="365.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F_\text{v} = G - F_\text{noste}$</div></foreignObject>
</svg>

Pallon, pyöräilijän tai auton kokoisilla kappaleilla arkisilla nopeuksilla ilmanvastus on likimain verrannollinen nopeuden neliöön, ja sen suuruutta mallinnetaan yhtälöllä

```latex
F_\text{v} = \tfrac{1}{2}\, C \rho A v^2
```

missä $F_\text{v}$ on ilmanvastuksen suuruus, $\rho$ ilman tiheys, $A$ kappaleen poikkipinta-ala liikesuuntaa vastaan kohtisuorassa tasossa, $v$ kappaleen nopeus ilman suhteen ja $C$ kappaleen **muotokerroin** eli ilmanvastuskerroin. Muotokerroin on yksikötön luku, joka riippuu kappaleen muodosta ja pinnasta: virtaviivaisella kappaleella se on pieni, tylpällä suuri. Mallissa oletetaan, että saman kappaleen muotokerroin pysyy likimain samana koko tarkasteltavalla nopeusalueella. Malli ei kuulu FY4:n lukuun, joten se on esitetty tässä.

::: tuki OO
Tarkista kirjauksesi tästä. Pallo on rajanopeudella, kun sen nopeus ei enää muutu. Silloin $F_\text{v} = G - F_\text{noste}$. Merkitään $mg = G - F_\text{noste}$, missä $m$ on vaa'an lukema (katso alempaa), jolloin

```latex
\tfrac{1}{2}\, C \rho A v_\text{r}^2 = mg
```

ja siitä ratkaistuna

```latex
C = \frac{2mg}{\rho A v_\text{r}^2}
```

missä $g$ on putoamiskiihtyvyys. Tarvitset siis pallon massan $m$, pallon poikkipinta-alan $A = \tfrac{1}{4}\pi d^2$, missä $d$ on pallon halkaisija, ilman tiheyden $\rho$ ja rajanopeuden $v_\text{r}$. Rajanopeus saadaan videolta, muut suureet mitataan tai selvitetään erikseen.

**Massa ja noste.** Kun punnitset pallon vaa'alla huoneilmassa, vaaka mittaa juuri erotusta $G - F_\text{noste}$, koska noste vaikuttaa palloon myös vaa'alla. Käytä siis massana $m$ vaa'an lukemaa.

**Ilman tiheys.** Ilman tiheys riippuu lämpötilasta ja paineesta. Katso se taulukkokirjasta huoneen lämpötilassa tai laske se ilmanpaineesta ja lämpötilasta ideaalikaasun tilanyhtälöllä. [[apua:fy3-10|Ideaalikaasun tilanyhtälö]]
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä mittaat, millä välineillä ja miten varmistat, että pallo on videolla rajanopeudella. Kokeile pudotusta ja kuvaamista ensin muutaman kerran.

::: tuki OO
**Osittain ohjattu.** Valitse pallo, joka on kevyt kokoonsa nähden, esimerkiksi täytetty ilmapallo. Mitä kevyempi pallo on kokoonsa nähden, sitä lyhyemmällä matkalla se saavuttaa rajanopeuden. Painava jumppapallo tarvitsee usean metrin pudotuksen. Päätä itse, kuinka korkealta pudotat ja miten mittaat pallon halkaisijan. Kuvaa ainakin viisi pudotusta. Kirjaa päätöksesi perusteluineen.

Mieti ainakin näitä:

- Miten pudotat pallon levosta niin, ettei se saa vauhtia tai pyörimistä kädestä?
- Mihin asetat kameran ja tunnetun pituuden, jotta video on mittakaavassa koko analysoitavan matkan ajan?
- Miten mittaat halkaisijan, jos pallo ei ole tarkasti pallonmuotoinen? Voisiko ympärysmitta auttaa?
- Kuinka tarkka vaaka tarvitaan, kun pallon massa on vain muutamia grammoja?
:::

::: tuki OO
**Vihjeitä kuvaamiseen.**

- Kuvaa jalustalta niin, että pallon liike näkyy mahdollisimman pitkältä matkalta, mieluiten myös loppuosa juuri ennen lattiaa.
- Aseta tunnetun pituinen mitta pystyyn pallon putoamislinjan viereen, samalle etäisyydelle kamerasta kuin pallo. Jos mitta on lähempänä tai kauempana kuin pallo, videon mittakaava on väärä.
- Pidä kamera kohtisuorassa pallon liikerataa vastaan ja suunnilleen analysoitavan matkan puolivälin korkeudella. Kuvaa kauempaa ja zoomaa: perspektiivivirhe pienenee, kun kamera on kaukana.
- Tarkista, millä kuvataajuudella video on tallennettu. Hidastetussa videossa analyysiohjelman aika-akseli voi olla väärä, jos ohjelma ei tunnista todellista kuvataajuutta.
- Varmista, ettei ilmanvaihto, avoin ikkuna tai ohikulkija aiheuta ilmavirtausta, joka ajaa palloa sivulle.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana: toistot omiin sarakkeisiinsa ja niistä lasketut suureet niiden oikealle puolelle. Tallenna videot niin, että tiedät, mikä video kuuluu mihinkin pudotukseen.

::: tuki OO
Voit käyttää esimerkiksi tällaisia taulukoita. Pallon halkaisija kannattaa mitata useasta suunnasta:

| $d_1\ (\text{m})$ | $d_2\ (\text{m})$ | $d_3\ (\text{m})$ | $\bar{d}\ (\text{m})$ | $A\ (\text{m}^2)$ |
|---|---|---|---|---|
| | | | | |

| pudotus | $v_\text{r}\ (\text{m/s})$ |
|---|---|
| 1. | |
| 2. | |
| 3. | |
| 4. | |
| 5. | |

Kirjaa lisäksi pallon massa $m$ ja huoneen lämpötila ja ilmanpaine tai ilman tiheys lähteineen.
:::

Muista mittausepävarmuus: kirjaa jokaisen suureen kohdalla, kuinka tarkasti sen mittasit, ja miten arvioit tarkkuuden. Toistojen hajonta kertoo, kuinka paljon rajanopeus vaihtelee pudotuksesta toiseen. [[apua:fy1-3|Toistomittausten keskiarvo ja epävarmuus]]

## Käsittele tulokset

Merkitse jokaisesta videosta pallon paikka kuva kuvalta, kun videon mittakaava on asetettu tunnetun pituuden avulla. Määritä pallon rajanopeus ja perustele, miksi pallo oli rajanopeudella sillä osalla matkaa, jota käytit. Laske lopuksi muotokerroin. [[apua:fy1-5|Nopeus paikka–aika-kuvaajasta]]

::: tuki OO
Piirrä pallon paikka ajan funktiona. Alussa kuvaaja kaartuu, koska pallo kiihtyy. Kun pallo on rajanopeudella, paikka muuttuu tasaisesti, ja kuvaaja on suora. Sovita suora vain tähän osaan: sen kulmakerroin on rajanopeus. Jos ohjelma mittaa paikan ylöspäin positiivisena, kulmakerroin on negatiivinen, ja rajanopeus on sen itseisarvo. Alla olevissa mallikuvaajissa $s$ on pallon putoamismatka ja $v$ sen nopeus.

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kaksi mallikuvaajaa ilman mittauspisteitä. Vasemmalla pudonnut matka s ajan t funktiona: kuvaaja kaartuu aluksi ylöspäin ja muuttuu sitten suoraksi. Suoran osan kulmakerroin, delta s jaettuna delta t:llä, on rajanopeus v_r. Oikealla nopeus v ajan t funktiona: nopeus kasvaa aluksi jyrkästi ja tasaantuu vaakasuoran katkoviivan v_r tasolle." style="max-width:100%;font-size:24px">
  <line x1="59" y1="280" x2="244" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M256,280 L243,286 L243,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="281" x2="60" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M60,34 L66,47 L54,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="30" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="262" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="50" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <polyline points="60,280 61.5,280 63,280 64,279.5 65.5,279.5 67,279.5 68.5,279 70,278.5 71.5,278 73,277.5 74,277 75.5,276.5 77,276 78.5,275 80,274.5 81,273.5 82.5,273 84,272 85.5,271 87,270 88.5,269 90,268 91,267 92.5,266 94,265 95.5,263.5 97,262.5 98,261 99.5,260 101,258.5 102.5,257.5 104,256 105.5,254.5 107,253 108,252 109.5,250.5 111,249 112.5,247.5 114,246 115,244.5 116.5,243 118,241.5 119.5,240 121,238.5 122.5,237 124,235 125,233.5 126.5,232 128,230.5 129.5,229 131,227 132,225.5 133.5,224 135,222.5 136.5,220.5 138,219 139.5,217.5 141,215.5 142,214 143.5,212.5 145,210.5 146.5,209 148,207 149,205.5 150.5,204 152,202 153.5,200.5 155,198.5 156.5,197 158,195.5 159,193.5 160.5,192 162,190 163.5,188.5 165,186.5 166,185 167.5,183.5 169,181.5 170.5,180 172,178 173.5,176.5 175,174.5 176,173 177.5,171 179,169.5 180.5,167.5 182,166 183,164 184.5,162.5 186,161 187.5,159 189,157.5 190.5,155.5 192,154 193,152 194.5,150.5 196,148.5 197.5,147 199,145 200,143.5 201.5,141.5 203,140 204.5,138 206,136.5 207.5,134.5 209,133 210,131 211.5,129.5 213,127.5 214.5,126 216,124 217,122.5 218.5,120.5 220,119 221.5,117 223,115.5 224.5,113.5 226,112 227,110.5 228.5,108.5 230,107" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="162,190 213,190 213,127.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <foreignObject x="173" y="196" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\Delta t$</div></foreignObject>
  <foreignObject x="221" y="147" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\Delta s$</div></foreignObject>
  <foreignObject x="64" y="65" width="65" height="53" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$v_\text{r} = \dfrac{\Delta s}{\Delta t}$</div></foreignObject>
  <line x1="359" y1="280" x2="544" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M556,280 L543,286 L543,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="360" y1="281" x2="360" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M360,34 L366,47 L354,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="330" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="562" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="350" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polyline points="360,104 530,104" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="360,280 361.5,274 363,268.5 364,262.5 365.5,256.5 367,251 368.5,245.5 370,239.5 371.5,234 373,228.5 374,223.5 375.5,218 377,213 378.5,208 380,203.5 381,198.5 382.5,194 384,189.5 385.5,185.5 387,181.5 388.5,177.5 390,173.5 391,170 392.5,166.5 394,163 395.5,160 397,157 398,154 399.5,151 401,148.5 402.5,146 404,143.5 405.5,141.5 407,139 408,137 409.5,135 411,133.5 412.5,131.5 414,130 415,128.5 416.5,127 418,125.5 419.5,124 421,123 422.5,122 424,120.5 425,119.5 426.5,118.5 428,118 429.5,117 431,116 432,115.5 433.5,114.5 435,114 436.5,113.5 438,113 439.5,112 441,111.5 442,111 443.5,111 445,110.5 446.5,110 448,109.5 449,109 450.5,109 452,108.5 453.5,108.5 455,108 456.5,107.5 458,107.5 459,107.5 460.5,107 462,107 463.5,106.5 465,106.5 466,106.5 467.5,106 469,106 470.5,106 472,106 473.5,105.5 475,105.5 476,105.5 477.5,105.5 479,105.5 480.5,105 482,105 483,105 484.5,105 486,105 487.5,105 489,105 490.5,105 492,104.5 493,104.5 494.5,104.5 496,104.5 497.5,104.5 499,104.5 500,104.5 501.5,104.5 503,104.5 504.5,104.5 506,104.5 507.5,104.5 509,104.5 510,104.5 511.5,104.5 513,104.5 514.5,104 516,104 517,104 518.5,104 520,104 521.5,104 523,104 524.5,104 526,104 527,104 528.5,104 530,104" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="501" y="67.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$v_\text{r}$</div></foreignObject>
</svg>

**Miksi paikka eikä nopeus?** Monet ohjelmat laskevat myös nopeuden kahden peräkkäisen kuvan paikoista. Tällainen nopeus heittelee paljon, koska pienikin virhe pallon paikan merkitsemisessä näkyy siinä suurena. Nopeus–aika-kuvaajasta näet kuitenkin hyvin, mistä kohdasta alkaen nopeus ei enää kasva. Kulmakerroin sovitetaan monen pisteen kautta, joten se on tarkempi. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

Laske rajanopeuksien keskiarvo $\bar{v}_\text{r}$ ja käytä sitä muotokertoimen laskemisessa.
:::

Vastaa:

1. Miten tunnistit, että pallo oli rajanopeudella? Millä matkalla se saavutti rajanopeuden?
2. Kuinka paljon rajanopeus vaihteli pudotuksesta toiseen, ja mistä vaihtelu voi johtua?

Paikan merkitsemiseen voit käyttää videoanalyysiohjelmaa tai puhelimen sovellusta. Sovita suora Graphical Analysis Pro -ohjelmalla. Ruukkilabran ohjeet: [[ohje:tvt-videoanalyysi|Videoanalyysi]], [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita muotokerroin muodossa $C \pm \Delta C$ ja perustele, miten arvioit epävarmuuden $\Delta C$. Selvitä, minkä suureen epävarmuus vaikuttaa tulokseen eniten.

::: tuki OO
Muotokerroin lasketaan neljästä mitatusta suureesta, joten sen epävarmuus muodostuu niiden epävarmuuksista. Voit arvioida sen jommallakummalla tavalla:

- **Ääriarvot.** Laske suurin mahdollinen muotokerroin $C_\text{max}$ valitsemalla jokaisesta suureesta se epävarmuusvälin raja, joka kasvattaa tulosta, ja pienin $C_\text{min}$ päinvastoin. Arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta C = \dfrac{C_\text{max} - C_\text{min}}{2}$.
- **Suhteelliset epävarmuudet.** Kun tulos on mitattujen suureiden tulo ja osamäärä, sen suhteellinen epävarmuus on enintään suureiden suhteellisten epävarmuuksien summa. Neliöön korotetun suureen suhteellinen epävarmuus lasketaan kahdesti:

```latex
\begin{aligned}
\frac{\Delta C}{C} \approx\ &\frac{\Delta m}{m} + \frac{\Delta \rho}{\rho} \\
&+ 2\cdot\frac{\Delta d}{d} + 2\cdot\frac{\Delta v_\text{r}}{v_\text{r}}
\end{aligned}
```

Jälkimmäisestä näet suoraan, mikä termi on suurin. Rajanopeuden epävarmuudeksi voit valita sovitusohjelman ilmoittaman kulmakertoimen keskivirheen tai toistojen hajonnasta arvioidun epävarmuuden, sen mukaan, kumpi on suurempi. Pyöristä $\Delta C$ yhteen merkitsevään numeroon ja $C$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti. Oliko pallo varmasti rajanopeudella, ja mihin suuntaan tulos muuttuisi, jos ei ollut? Oliko mittakaava oikea koko analysoitavalla matkalla? Heiluiko tai pyörikö pallo, ja oliko se pallonmuotoinen? Miten noste vaikuttaa tulokseen? Olivatko virheet satunnaisia vai systemaattisia, ja miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Etsi kirjallisuudesta, esimerkiksi taulukkokirjasta, pallomaisen kappaleen muotokerroin ja kirjaa lähde. Mahtuuko kirjallisuusarvo tuloksesi epävarmuusvälin sisään? Jos ei, mistä ero voi johtua: mittauksesta, pallosta vai siitä, että kirjallisuusarvo on määritetty erilaisissa oloissa? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tuloksia ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** ilmanvastuksen malli lähteineen ja miten muotokerroin saadaan rajanopeudesta.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, josta näkyvät kameran paikka, tunnettu pituus ja pallon putoamislinja, sekä perustelut niille.
- **Tulosten käsittely:** paikka–aika-kuvaaja, siihen sovitettu suora ja perustelu sille, mistä kohdasta alkaen pallo oli rajanopeudella.
- **Tulos:** $C \pm \Delta C$ oikein pyöristettynä.
- **Luotettavuus:** suurimmat epävarmuuden lähteet, niiden vaikutuksen suunta ja vertailu kirjallisuusarvoon.

## Laajennus: rajanopeus ja massa

Muotokerroin riippuu muodosta, ei massasta. Jos pallon massaa kasvatetaan mutta sen muoto ja koko pysyvät samoina, rajanopeuden pitäisi kasvaa niin, että muotokerroin pysyy samana. Testaa tätä: kiinnitä palloon pieniä lisäpainoja, esimerkiksi teipillä paperiliittimiä pallon alaosaan, punnitse pallo jokaisen lisäyksen jälkeen ja määritä rajanopeus usealla eri massalla. Ulkopuolelle teipatut lisäpainot muuttavat hieman pallon muotoa ja poikkipinta-alaa: pohdi, miten se vaikuttaa tulokseen. Piirrä kuvaaja, josta muotokerroin saadaan kulmakertoimesta, ja vertaa tulosta päämittauksen tulokseen epävarmuuksineen. Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Kumpi menetelmä vaikutti luotettavammalta, ja miksi?

::: tuki OO
**Akselit.** Rajanopeudella, kun $m$ on vaa'an lukema, $mg = \tfrac{1}{2}\, C \rho A v_\text{r}^2$, joten

```latex
m = \frac{C \rho A}{2g}\cdot v_\text{r}^2
```

Jos muotokerroin pysyy samana, massa rajanopeuden neliön funktiona on origon kautta kulkeva suora, jonka kulmakerroin on $k = \dfrac{C \rho A}{2g}$. Muotokerroin saadaan kulmakertoimesta: $C = \dfrac{2gk}{\rho A}$.

<svg data-fig="mass" viewBox="0 0 600 330" role="img" aria-label="Mallikuvaaja ilman mittauspisteitä: pallon massa m rajanopeuden neliön v_r toiseen funktiona. Jos muotokerroin pysyy samana, kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on C kertaa rho kertaa A jaettuna kahdella g:llä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_\text{r}^2$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m$</div></foreignObject>
  <polyline points="90,280 451,82" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="325.5" y="168" width="195" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } \dfrac{C\rho A}{2g}$</div></foreignObject>
</svg>

**Vihjeitä.** Pidä lisäpainot pieninä ja kiinnitä ne pallon alaosaan, jotta pallo putoaa vakaasti eikä käänny. Raskaampi pallo tarvitsee pidemmän matkan saavuttaakseen rajanopeuden, joten tarkista se jokaisesta videosta erikseen. Jos pisteet kaartuvat pois suoralta, pohdi, onko muotokerroin todella vakio tällä nopeusalueella.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
