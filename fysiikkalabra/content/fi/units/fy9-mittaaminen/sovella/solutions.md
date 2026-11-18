## fy9-mittaaminen-s1

### a)
**Annettu:** matka $s = 100{,}0\,\text{m}$; Liisan ajat $13{,}52\,\text{s}$, $13{,}90\,\text{s}$ ja $13{,}71\,\text{s}$
**Kysytty:** Liisan keskinopeus $v$ yksiköissä $\text{m/s}$ ja $\text{km/h}$
**Periaate:** Keskinopeus on kuljettu matka jaettuna siihen kuluneella ajalla. Kolme kelloa mittaa saman juoksun, joten ajan paras arvio on niiden keskiarvo: satunnaisvirheet kumoavat siinä osittain toisensa.
**Kaava:** $\bar{t} = \dfrac{t_1 + t_2 + t_3}{3}$ ja $v = \dfrac{s}{\bar{t}}$
**Muunnokset:** $1\,\tfrac{\text{m}}{\text{s}} = \dfrac{0{,}001\,\text{km}}{\tfrac{1}{3600}\,\text{h}} = 3{,}6\,\tfrac{\text{km}}{\text{h}}$
**Sijoitus:** $\bar{t} = \dfrac{13{,}52\,\text{s} + 13{,}90\,\text{s} + 13{,}71\,\text{s}}{3} = 13{,}71\,\text{s}$ ja $v = \dfrac{100{,}0\,\text{m}}{13{,}71\,\text{s}} = 7{,}294\,\tfrac{\text{m}}{\text{s}} = 7{,}294 \cdot 3{,}6\,\tfrac{\text{km}}{\text{h}} = 26{,}26\,\tfrac{\text{km}}{\text{h}}$
**Vastaus:** $v \approx 7{,}29\,\text{m/s} \approx 26{,}3\,\text{km/h}$. Kolme merkitsevää numeroa: kellojen lukemat poikkeavat toisistaan kymmenesosasekunteja eli noin prosentin, joten nopeudessakin vasta sadasosat metriä sekunnissa ovat epävarmoja. (b-kohdan epävarmuus $0{,}12\,\text{m/s}$ vahvistaa tämän.)
**Järkevyys:** Noin $26\,\text{km/h}$ on reipas lukiolaisen sprinttivauhti. Se on selvästi alle huippujuoksijan noin $36\,\text{km/h}$:n ja selvästi yli hölkän noin $10\,\text{km/h}$:n.

### b)
**Annettu:** $s = (100{,}0 \pm 0{,}3)\,\text{m}$; ajat $13{,}52\,\text{s}$, $13{,}90\,\text{s}$ ja $13{,}71\,\text{s}$; a-kohdasta $\bar{t} = 13{,}71\,\text{s}$
**Kysytty:** keskinopeuden epävarmuus $\Delta v$ ja nopeus epävarmuuksineen
**Periaate:** Ajan epävarmuutta arvioidaan kolmen kellon tulosten vaihteluvälin puolikkaana. Nopeus on suurimmillaan, kun matka on pisin ja aika lyhin mahdollinen, ja pienimmillään päinvastoin. Epävarmuudeksi otetaan näin saadun välin puolikas.
**Kaava:** $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$, $v_\text{max} = \dfrac{s + \Delta s}{\bar{t} - \Delta t}$, $v_\text{min} = \dfrac{s - \Delta s}{\bar{t} + \Delta t}$ ja $\Delta v = \dfrac{v_\text{max} - v_\text{min}}{2}$
**Muunnokset:** Ei tarvita: matka on metreinä ja ajat sekunteina.
**Sijoitus:** $\Delta t = \dfrac{13{,}90\,\text{s} - 13{,}52\,\text{s}}{2} = 0{,}19\,\text{s}$, $v_\text{max} = \dfrac{100{,}3\,\text{m}}{13{,}52\,\text{s}} = 7{,}419\,\tfrac{\text{m}}{\text{s}}$, $v_\text{min} = \dfrac{99{,}7\,\text{m}}{13{,}90\,\text{s}} = 7{,}173\,\tfrac{\text{m}}{\text{s}}$ ja $\Delta v = \dfrac{7{,}419\,\tfrac{\text{m}}{\text{s}} - 7{,}173\,\tfrac{\text{m}}{\text{s}}}{2} = 0{,}123\,\tfrac{\text{m}}{\text{s}}$
**Vastaus:** $v = (7{,}29 \pm 0{,}12)\,\text{m/s}$. Epävarmuuden ensimmäinen numero on $1$, joten siinä pidetään kaksi merkitsevää numeroa, ja nopeus pyöristetään samaan desimaaliin.
**Järkevyys:** Ajan suhteellinen epävarmuus $0{,}19 : 13{,}71 \approx 1{,}4\,\%$ on paljon suurempi kuin matkan $0{,}3 : 100 = 0{,}3\,\%$, joten nopeuden epävarmuus johtuu lähes kokonaan käsiajanotosta. Noin $0{,}2\,\text{s}$ on tavallinen käsin otetun ajan epävarmuus.

### c)
**Kysytty:** voidaanko mittauksilla osoittaa, että Liisa oli Miraa nopeampi
**Periaate:** Kaksi tulosta eroavat osoitetusti vain, jos niiden epävarmuusvälit eivät mene päällekkäin. Päällekkäiset välit eivät todista tuloksia yhtä suuriksi.
**Mallivastaus:** Miran keskiarvo on $$
\begin{aligned}
\bar{t} &= (13{,}80 + 14{,}12 + 13{,}96)\,\text{s} \\
&: 3 \\
&= 13{,}96\,\text{s}
\end{aligned}
$$ ja epävarmuus $(14{,}12 - 13{,}80)\,\text{s} : 2 = 0{,}16\,\text{s}$, joten Miran aika on $(13{,}96 \pm 0{,}16)\,\text{s}$ ja Liisan $(13{,}71 \pm 0{,}19)\,\text{s}$. Liisan väli on $13{,}52$–$13{,}90\,\text{s}$ ja Miran $13{,}80$–$14{,}12\,\text{s}$, joten välit menevät päällekkäin. Ero $0{,}25\,\text{s}$ on samaa suuruusluokkaa kuin epävarmuudet. Näillä mittauksilla ei siis voida osoittaa, että Liisa oli nopeampi, vaikka hänen keskiarvonsa on pienempi. Se ei kuitenkaan tarkoita, että juoksijat olisivat yhtä nopeita: eron osoittaminen vaatisi tarkemman ajanoton, esimerkiksi maalikameran.

### d)
**Kysytty:** käsiajanoton systemaattiset virhelähteet, voiko virheen suunnan päätellä varmasti ja miksi keskiarvo ei välttämättä poista systemaattista virhettä
**Periaate:** Systemaattinen virhe siirtää jokaista tulosta samaan suuntaan. Sitä ei näe tulosten hajonnasta, ja toistaminen tai keskiarvo ei poista sitä. Satunnaisvirheen vaikutus sen sijaan yleensä pienenee, kun tuloksia keskiarvoistetaan.
**Mallivastaus:** Ajanottaja käynnistää kellon vasta, kun hän on nähnyt lipun laskevan ja reagoinut siihen. Kello käynnistyy siksi viiveen $\tau_\text{k}$ myöhässä, tyypillisesti sekunnin kymmenyksiä. Myös pysäyttämiseen liittyy viive $\tau_\text{p}$. Maaliintulon ajanottaja näkee ennalta, joten tämä viive voi olla lyhyempi, mutta hän voi myös pysäyttää kellon hieman liian aikaisin tai myöhässä. Mitattu aika on $t_\text{mitattu} = t_\text{tod} + \tau_\text{p} - \tau_\text{k}$, missä $t_\text{tod}$ on todellinen aika. Mitattu aika on siis todellista lyhyempi, jos $\tau_\text{k} > \tau_\text{p}$, ja pidempi, jos $\tau_\text{p} > \tau_\text{k}$. Tehtävän tiedoista viiveitä ei tunneta, joten suuntaa ei voi päätellä varmasti. Todennäköisintä on, että lähtöviive on suurempi, jolloin aika on hieman liian lyhyt ja a-kohdan nopeus liian suuri. Kolme ajanottajaa toimii samalla tavalla, joten viiveiden keskimääräinen osa on kaikilla samansuuntainen. Se on systemaattinen virhe, joka säilyy myös keskiarvossa. Keskiarvo pienentää yleensä vain satunnaisvirheen eli kellojen välisen vaihtelun vaikutusta. Systemaattisen virheen poistaa esimerkiksi sähköinen ajanotto, joka käynnistyy lähtömerkistä itse.

### Hyväksytään myös
- b-kohdassa nopeuden suhteellinen epävarmuus ajan ja matkan suhteellisten epävarmuuksien summana: $\tfrac{0{,}19}{13{,}71} + \tfrac{0{,}3}{100{,}0} \approx 0{,}0169$, jolloin $$
\begin{aligned}
\Delta v &\approx 0{,}0169 \cdot 7{,}294\,\text{m/s} \\
&\approx 0{,}12\,\text{m/s}
\end{aligned}
$$.
- b-kohdassa ajan epävarmuudeksi käsiajanoton tyypillinen $0{,}2\,\text{s}$, kun valinta perustellaan. Myös $\Delta v \approx 0{,}1\,\text{m/s}$ ja $v = (7{,}3 \pm 0{,}1)\,\text{m/s}$ hyväksytään.
- d-kohdassa maininta, että lähtöpistoolin ääneen reagoiva ajanottaja $100\,\text{m}$:n päässä käynnistäisi kellon vielä myöhemmin, koska ääni kulkee matkan noin $0{,}3\,\text{s}$:ssa.
- d-kohdassa perusteltu arvio virheen suunnasta, esimerkiksi että mitattu aika on todennäköisesti todellista lyhyempi, kun vastauksessa todetaan, että päätelmä perustuu oletukseen viiveiden suuruudesta.

### Yleisiä virheitä
- Aikana käytetään yhtä kelloa tai nopeinta aikaa keskiarvon sijasta.
- Nopeus muunnetaan kertomalla tai jakamalla väärin, esimerkiksi $7{,}29 : 3{,}6 = 2{,}0\,\text{km/h}$; järkevyystarkastelu paljastaa virheen.
- Nopeus ilmoitetaan laskimen tarkkuudella $7{,}2939\,\text{m/s}$ tai epävarmuus ja nopeus eri tarkkuudella.
- c-kohdassa päätellään keskiarvojen erosta, että Liisa oli nopeampi, tai päällekkäisistä väleistä, että juoksijat olivat yhtä nopeita.
- d-kohdassa reaktioajan sanotaan aiheuttavan vain satunnaisvirheen; sen keskimääräinen osa on systemaattinen.
- d-kohdassa väitetään varmaksi, että mitattu aika on todellista lyhyempi tai pidempi, vaikka suunta riippuu käynnistys- ja pysäytysviiveen erotuksesta.

## fy9-mittaaminen-s2

### a)
**Annettu:** pinon korkeus $h = 51\,\text{mm}$, sen epävarmuus $\Delta h = 1\,\text{mm}$, arkkeja $N = 500$
**Kysytty:** yhden arkin paksuus $d$ ja sen epävarmuus $\Delta d$ mikrometreinä
**Periaate:** Arkit ovat samanlaisia ja pino mitataan kerran, joten yhden arkin paksuus on pinon korkeus jaettuna arkkien määrällä. Sama jako koskee myös korkeuden epävarmuutta, koska se on yhden mittauksen epävarmuus.
**Kaava:** $d = \dfrac{h}{N}$ ja $\Delta d = \dfrac{\Delta h}{N}$
**Muunnokset:** $1\,\text{mm} = 1000\,\mu\text{m}$, joten $51\,\text{mm} = 51 \cdot 1000\,\mu\text{m} = 51\,000\,\mu\text{m}$ ja $1\,\text{mm} = 1000\,\mu\text{m}$.
**Sijoitus:** $d = \dfrac{51\,000\,\mu\text{m}}{500} = 102\,\mu\text{m}$ ja $\Delta d = \dfrac{1000\,\mu\text{m}}{500} = 2\,\mu\text{m}$
**Vastaus:** $d = (102 \pm 2)\,\mu\text{m}$. Epävarmuus on yhden merkitsevän numeron arvio, ja paksuus pyöristetään samaan tarkkuuteen, kokonaisiin mikrometreihin.
**Järkevyys:** Kymmenesosamillimetri on tavallisen kopiopaperin paksuus: arkki tuntuu ohuelta mutta ei läpikuultavalta. Suhteellinen epävarmuus on $2 : 102 \approx 2\,\%$, sama kuin pinon korkeuden $1 : 51$.

### b)
**Annettu:** paperien massa $M = 2{,}49\,\text{kg}$, $N = 500$ arkkia, arkin mitat $a = 210\,\text{mm}$ ja $b = 297\,\text{mm}$; merkintä $80\,\text{g/m}^2$
**Kysytty:** mitattu neliömassa $\sigma$ yksikössä $\text{g/m}^2$
**Periaate:** Neliömassa on massa pinta-alayksikköä kohti. Kaikkien arkkien yhteispinta-ala on yhden arkin ala kerrottuna arkkien määrällä, ja sen massa on punnittu massa.
**Kaava:** $A = N \cdot ab$ ja $\sigma = \dfrac{M}{A} = \dfrac{M}{N ab}$
**Muunnokset:** $a = 210\,\text{mm} = 210 \cdot 0{,}001\,\text{m} = 0{,}210\,\text{m}$, $b = 297 \cdot 0{,}001\,\text{m} = 0{,}297\,\text{m}$ ja $M = 2{,}49\,\text{kg} = 2{,}49 \cdot 1000\,\text{g} = 2490\,\text{g}$
**Sijoitus:** $A = 500 \cdot 0{,}210\,\text{m} \cdot 0{,}297\,\text{m} = 31{,}185\,\text{m}^2$ ja $\sigma = \dfrac{2490\,\text{g}}{31{,}185\,\text{m}^2} = 79{,}85\,\tfrac{\text{g}}{\text{m}^2}$
**Vastaus:** $\sigma \approx 79{,}8\,\text{g/m}^2$, kolme merkitsevää numeroa kuten massassa $2{,}49\,\text{kg}$. Ero merkintään $80\,\text{g/m}^2$ on alle $0{,}3\,\%$, joten merkintä pitää paikkansa vaa'an tarkkuudella.
**Järkevyys:** Arviona yksi A4-arkki on noin $\tfrac{1}{16}\,\text{m}^2$, joten $500$ arkkia on noin $31\,\text{m}^2$, ja $31\,\text{m}^2 \cdot 80\,\text{g/m}^2 \approx 2{,}5\,\text{kg}$, mikä vastaa punnittua massaa.

### c)
**Annettu:** a-kohdasta $d = 102\,\mu\text{m}$, b-kohdasta $\sigma = 79{,}85\,\text{g/m}^2$; veden tiheys $1000\,\text{kg/m}^3$
**Kysytty:** paperin tiheys $\rho$ yksikössä $\text{kg/m}^3$
**Periaate:** Tiheys on massa tilavuutta kohti. Paperi on tasapaksua, joten pinta-alaltaan $A$ olevan paperin massa on $\sigma A$ ja tilavuus $Ad$. Pinta-ala supistuu, joten tiheys saadaan jakamalla neliömassa paksuudella.
**Kaava:** $\rho = \dfrac{m}{V} = \dfrac{\sigma A}{A d} = \dfrac{\sigma}{d}$
**Muunnokset:** $\sigma = 79{,}85\,\text{g/m}^2 = 79{,}85 \cdot 0{,}001\,\text{kg/m}^2 = 0{,}07985\,\text{kg/m}^2$ ja $d = 102\,\mu\text{m} = 102 \cdot 10^{-6}\,\text{m} = 1{,}02 \cdot 10^{-4}\,\text{m}$
**Sijoitus:** $\rho = \dfrac{0{,}07985\,\text{kg/m}^2}{1{,}02 \cdot 10^{-4}\,\text{m}} = 782{,}8\,\tfrac{\text{kg}}{\text{m}^3}$
**Vastaus:** $\rho \approx 780\,\text{kg/m}^3$ eli $7{,}8 \cdot 10^{2}\,\text{kg/m}^3$, kaksi merkitsevää numeroa, koska pinon korkeus $51\,\text{mm}$ on kahden numeron luku. Paperin tiheys on noin $0{,}78$ kertaa veden tiheys.
**Järkevyys:** Paperi on puukuitua, jonka välissä on ilmaa, joten sen tiheys on samaa luokkaa kuin puun, muutamia satoja kilogrammoja kuutiometrissä. Suhteellinen epävarmuus on sama kuin paksuuden, noin $2\,\%$, eli noin $\pm 20\,\text{kg/m}^3$.

### d)
**Kysytty:** onko yhden arkin suora mittaaminen järkevää, ja miksi pinon korkeuden epävarmuus on suurempi kuin puolet asteikkovälistä
**Periaate:** Lukeman epävarmuutta voidaan yksinkertaisessa tilanteessa arvioida puoleksi pienimmästä asteikkovälistä, mutta mittauksen kokonaisepävarmuuteen vaikuttavat myös mittausmenetelmä ja muut virhelähteet. Suhteellinen epävarmuus kertoo, onko epävarmuus tulokseen nähden pieni.
**Mallivastaus:** Yksi arkki on noin $0{,}1\,\text{mm}$ paksu, joten viivain näyttäisi lukeman $0$ tai $1\,\text{mm}$. Lukeman epävarmuus $0{,}5\,\text{mm}$ olisi noin viisinkertainen itse paksuuteen nähden, suhteellisesti noin $500\,\%$, joten mittauksesta ei saisi mitään tietoa. Pinoa mitattaessa saman suuruinen lukeman epävarmuus jakautuu $500$ arkille, ja suhteellinen epävarmuus on vain noin $2\,\%$. Ehdotus on siis huono.

Pinon korkeuden epävarmuus on suurempi kuin $0{,}5\,\text{mm}$, koska epävarmuutta ei tuo pelkkä asteikon lukeminen. Pinon reunat ovat epätasaiset, joten korkeus riippuu siitä, mistä kohdasta mitataan, ja pino painuu kokoon, kun viivainta painetaan sitä vasten. Asteikkoväli kertoo vain viivaimen resoluution, ei koko mittauksen epävarmuutta.

### Hyväksytään myös
- c-kohdassa koko pinon tiheys: $$
\begin{aligned}
\rho &= \tfrac{M}{N a b d} \\
&= \tfrac{2{,}49\,\text{kg}}{31{,}185\,\text{m}^2 \cdot 1{,}02 \cdot 10^{-4}\,\text{m}} \\
&\approx 783\,\text{kg/m}^3
\end{aligned}
$$, tai pakkauksen merkinnällä $80\,\text{g/m}^2$ laskettu $\rho \approx 784\,\text{kg/m}^3$.
- a-kohdassa paksuus millimetreinä ja muunnos lopuksi: $$
\begin{aligned}
d &= 51\,\text{mm} : 500 \\
&= 0{,}102\,\text{mm} \\
&= 102\,\mu\text{m}
\end{aligned}
$$.

### Yleisiä virheitä
- Epävarmuutta ei jaeta arkkien määrällä, jolloin arkin paksuudeksi saadaan $(102 \pm 1000)\,\mu\text{m}$.
- Millimetrit muunnetaan mikrometreiksi väärään suuntaan: $$
\begin{aligned}
&51\,\text{mm} : 500 \\
&= 0{,}102\,\text{mm} \\
&= 0{,}000102\,\mu\text{m}
\end{aligned}
$$. Pienemmässä yksikössä lukuarvo kasvaa.
- Pinta-ala lasketaan millimetreinä ja neliömetreihin muunnetaan kertoimella $1000$, vaikka $1\,\text{m}^2 = 10^{6}\,\text{mm}^2$.
- Tiheydelle annetaan kolme tai neljä merkitsevää numeroa, vaikka pinon korkeus tunnetaan vain kahden numeron tarkkuudella.

## fy9-mittaaminen-s3

### a)
**Kysytty:** mittaustulosten kuvaaja
**Kuvaaja:** Vaaka-akselille tulee nesteen tilavuus $V\ (\text{ml})$, jonka opiskelija valitsee, ja pystyakselille mitattu yhteismassa $m\ (\text{g})$. Pystyakseli alkaa tässä $100\,\text{g}$:sta, mikä on merkitty, ja vaaka-akseli nollasta, jotta suoraa voi myöhemmin jatkaa pystyakselille.

<svg data-fig="s3-pisteet" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: mittalasin ja nesteen yhteismassa m grammoina nesteen tilavuuden V funktiona millilitroina. Vaaka-akseli 0–110 ml ja pystyakseli 100–220 g, jonka alkukohta on merkitty. Kahdeksan sinistä pistettä asettuu nousevaan jonoon tilavuuksilla 20–100 ml, ja jokaisella on vaakasuora epävarmuusjana ±1 ml. Rivin 60 ml piste (60 ml; 183,4 g) on piirretty ontoksi punaiseksi ympyräksi: se on selvästi muiden yläpuolella, lähes samalla korkeudella kuin piste 70 ml." style="max-width:100%;font-size:30px">
  <line x1="129.5" y1="384" x2="129.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197" y1="384" x2="197" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="264" y1="384" x2="264" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="384" x2="331.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398.5" y1="384" x2="398.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="384" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="357.5" x2="466" y2="357.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="330.5" x2="466" y2="330.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="304" x2="466" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="277.5" x2="466" y2="277.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="250.5" x2="466" y2="250.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="224" x2="466" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="466" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170.5" x2="466" y2="170.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="144" x2="466" y2="144" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="117.5" x2="466" y2="117.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="90.5" x2="466" y2="90.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="384" x2="480" y2="384" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M492,384 L479,390 L479,378 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="385" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="129.5" y1="384" x2="129.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="144" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$20$</div></foreignObject>
  <line x1="197" y1="384" x2="197" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="211" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$40$</div></foreignObject>
  <line x1="264" y1="384" x2="264" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="278.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$60$</div></foreignObject>
  <line x1="331.5" y1="384" x2="331.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="345.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$80$</div></foreignObject>
  <line x1="398.5" y1="384" x2="398.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="405" y="390" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="466" y1="384" x2="466" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="357.5" x2="96" y2="357.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="330.5" x2="96" y2="330.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="312.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$120$</div></foreignObject>
  <line x1="89" y1="304" x2="96" y2="304" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="277.5" x2="96" y2="277.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="259.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$140$</div></foreignObject>
  <line x1="89" y1="250.5" x2="96" y2="250.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="224" x2="96" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="206" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$160$</div></foreignObject>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="170.5" x2="96" y2="170.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="152.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$180$</div></foreignObject>
  <line x1="89" y1="144" x2="96" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="117.5" x2="96" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="99.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$200$</div></foreignObject>
  <line x1="89" y1="90.5" x2="96" y2="90.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="46" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$220$</div></foreignObject>
  <foreignObject x="498" y="366" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$V\ (\text{ml})$</div></foreignObject>
  <foreignObject x="86" y="4" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$m\ (\text{g})$</div></foreignObject>
  <line x1="160" y1="283.5" x2="166.5" y2="283.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="163.5" cy="283.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="193.5" y1="262" x2="200.5" y2="262" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="197" cy="262" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="227" y1="235.5" x2="234" y2="235.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="230.5" cy="235.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="261" y1="213.5" x2="267.5" y2="213.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="264" cy="213.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="328" y1="162.5" x2="335" y2="162.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="331.5" cy="162.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="361.5" y1="139" x2="368.5" y2="139" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="365" cy="139" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="395.5" y1="112" x2="402" y2="112" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="398.5" cy="112" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="429" y1="90" x2="435.5" y2="90" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="432.5" cy="90" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298" cy="161.5" r="6.5" fill="#ffffff" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="182" y="133.5" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px;color:#c92a2a">$60\,\text{ml?}$</div></foreignObject>
  <foreignObject x="109.5" y="342" width="258" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$\text{akseli alkaa } 100\,\text{g}$</div></foreignObject>
</svg>

**Mallivastaus:** Kumpikin akseli on tasavälinen, ja akselin päässä on suure ja yksikkö. Pisteet täyttävät suurimman osan kuvaajasta. Jokaiseen pisteeseen on merkitty vaakasuora epävarmuusjana $\pm 1\,\text{ml}$; vaa'an resoluutio $0{,}1\,\text{g}$ on niin pieni, ettei pystyjanaa näe. Pisteitä ei yhdistetä toisiinsa. Rivin $60\,\text{ml}$ piste erottuu heti: se on lähes samalla korkeudella kuin rivin $70\,\text{ml}$ piste, vaikka massan pitäisi kasvaa tasaisesti.

### b)
**Kysytty:** sovitettu malli ja rivin $60\,\text{ml}$ käsittely
**Kuvaaja:** Seitsemän muun pisteen ja pisteen $20\,\text{ml}$ lomaan sovitetaan yksi suora, ja sitä jatketaan katkoviivana pystyakselille. Harmaat katkoviivat ovat d-kohdan jyrkin ja loivin suora.

<svg data-fig="s3-sovitus" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: sama aineisto kuin edellä. Kahdeksan luotettavan pisteen lomaan on sovitettu yksi suora, jota on jatkettu katkoviivana pystyakselille asti; se leikkaa akselin kohdassa noin 118,6 g, joka on tyhjän mittalasin massa. Suoralta luetut kaukana toisistaan olevat pisteet (20 ml; 137,0 g) ja (100 ml; 210,5 g) on ympyröity, joten kulmakerroin on 0,919 g/ml. Harmaat katkoviivat ovat jyrkin ja loivin suora, joiden kulmakertoimet ovat 0,932 ja 0,908 g/ml. Onton pisteen 60 ml suora ohittaa noin 10 g:n päästä." style="max-width:100%;font-size:30px">
  <line x1="129.5" y1="384" x2="129.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197" y1="384" x2="197" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="264" y1="384" x2="264" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="384" x2="331.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398.5" y1="384" x2="398.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="384" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="357.5" x2="466" y2="357.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="330.5" x2="466" y2="330.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="304" x2="466" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="277.5" x2="466" y2="277.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="250.5" x2="466" y2="250.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="224" x2="466" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="466" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170.5" x2="466" y2="170.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="144" x2="466" y2="144" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="117.5" x2="466" y2="117.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="90.5" x2="466" y2="90.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="384" x2="480" y2="384" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M492,384 L479,390 L479,378 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="385" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="129.5" y1="384" x2="129.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="144" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$20$</div></foreignObject>
  <line x1="197" y1="384" x2="197" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="211" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$40$</div></foreignObject>
  <line x1="264" y1="384" x2="264" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="278.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$60$</div></foreignObject>
  <line x1="331.5" y1="384" x2="331.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="345.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$80$</div></foreignObject>
  <line x1="398.5" y1="384" x2="398.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="405" y="390" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="466" y1="384" x2="466" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="357.5" x2="96" y2="357.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="330.5" x2="96" y2="330.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="312.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$120$</div></foreignObject>
  <line x1="89" y1="304" x2="96" y2="304" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="277.5" x2="96" y2="277.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="259.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$140$</div></foreignObject>
  <line x1="89" y1="250.5" x2="96" y2="250.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="224" x2="96" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="206" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$160$</div></foreignObject>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="170.5" x2="96" y2="170.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="152.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$180$</div></foreignObject>
  <line x1="89" y1="144" x2="96" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="117.5" x2="96" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="99.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$200$</div></foreignObject>
  <line x1="89" y1="90.5" x2="96" y2="90.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="46" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$220$</div></foreignObject>
  <foreignObject x="498" y="366" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$V\ (\text{ml})$</div></foreignObject>
  <foreignObject x="86" y="4" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$m\ (\text{g})$</div></foreignObject>
  <polyline points="136.5,303.5 452.5,75.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="136.5,306 452.5,72.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="96,334.5 146.5,297.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <polyline points="146.5,297.5 452.5,74.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="160" y1="283.5" x2="166.5" y2="283.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="163.5" cy="283.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="193.5" y1="262" x2="200.5" y2="262" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="197" cy="262" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="227" y1="235.5" x2="234" y2="235.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="230.5" cy="235.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="261" y1="213.5" x2="267.5" y2="213.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="264" cy="213.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="328" y1="162.5" x2="335" y2="162.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="331.5" cy="162.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="361.5" y1="139" x2="368.5" y2="139" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="365" cy="139" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="395.5" y1="112" x2="402" y2="112" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="398.5" cy="112" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="429" y1="90" x2="435.5" y2="90" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="432.5" cy="90" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298" cy="161.5" r="6.5" fill="#ffffff" stroke="#c92a2a" stroke-width="2.5"/>
  <circle cx="163.5" cy="285.5" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="432.5" cy="89.5" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="96" cy="334.5" r="9" fill="none" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="109.5" y="346.5" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$m_0 \approx 118{,}6\,\text{g}$</div></foreignObject>
  <foreignObject x="120.5" y="83.5" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$k \approx 0{,}919\,\tfrac{\text{g}}{\text{ml}}$</div></foreignObject>
</svg>

**Mallivastaus:** Pisteet ovat likimain suoralla, joten malliksi sopii suora $m = kV + b$. Suoraa ei pakoteta origon kautta, koska vaaka punnitsee myös mittalasin: kun nestettä ei ole, massa ei ole nolla. Rivin $60\,\text{ml}$ piste on noin $10\,\text{g}$ suoran yläpuolella, mikä on yli kymmenkertainen muiden pisteiden poikkeamiin nähden. Sen massa $183{,}4\,\text{g}$ sopisi suoralle tilavuudella noin $70\,\text{ml}$, ja muistiinpanon mukaan lukema kirjattiin jälkikäteen muistista. Poikkeamalle on siis löytynyt todennäköinen syy, karkea virhe, joten piste jätetään pois sovituksesta. Poisjättö ja sen syy kirjataan raporttiin. Pistettä ei olisi saanut poistaa pelkästään siksi, että se poikkeaa muista; parasta olisi toistaa mittaus.

### c)
**Annettu:** b-kohdan sovitettu suora
**Kysytty:** suoran kulmakerroin $k$ ja vakiotermi $b$ yksiköineen sekä niiden merkitys
**Periaate:** Vaaka punnitsee mittalasin ja nesteen: $m = \rho V + m_0$. Mittalasin massa $m_0$ ei muutu nestettä lisättäessä, joten massan muutos johtuu vain nesteestä. Siksi kulmakerroin on nesteen tiheys ja vakiotermi tyhjän mittalasin massa.
**Kuvaajan lukeminen:** Suoralta luetaan kaksi kaukana toisistaan olevaa pistettä: $(V_1;\ m_1) = (20\,\text{ml};\ 137{,}0\,\text{g})$ ja $(V_2;\ m_2) = (100\,\text{ml};\ 210{,}5\,\text{g})$.
**Kaava:** $k = \dfrac{m_2 - m_1}{V_2 - V_1}$ ja $b = m_1 - k V_1$
**Muunnokset:** $1\,\text{ml} = 1\,\text{cm}^3$, joten $1\,\tfrac{\text{g}}{\text{ml}} = 1\,\tfrac{\text{g}}{\text{cm}^3}$.
**Sijoitus:** $k = \dfrac{210{,}5\,\text{g} - 137{,}0\,\text{g}}{100\,\text{ml} - 20\,\text{ml}} = \dfrac{73{,}5\,\text{g}}{80\,\text{ml}} = 0{,}919\,\tfrac{\text{g}}{\text{ml}}$ ja $b = 137{,}0\,\text{g} - 0{,}919\,\tfrac{\text{g}}{\text{ml}} \cdot 20\,\text{ml} = 118{,}6\,\text{g}$
**Vastaus:** Kulmakerroin $k \approx 0{,}919\,\text{g/cm}^3$ on nesteen tiheys, ja vakiotermi $b \approx 118{,}6\,\text{g}$ on tyhjän mittalasin massa. Kulmakertoimessa on kolme merkitsevää numeroa, koska massojen erotus $73{,}5\,\text{g}$ luetaan kolmen numeron tarkkuudella; d-kohdan epävarmuus kertoo, että kolmas numero on jo epävarma.
**Järkevyys:** Lasisen $100\,\text{ml}$:n mittalasin massa on tyypillisesti noin $100$–$200\,\text{g}$, ja tiheys on vettä pienempi mutta etanolia suurempi. Suoran mukaan rivillä $20\,\text{ml}$ massa on $118{,}6\,\text{g} + 0{,}919\,\tfrac{\text{g}}{\text{ml}} \cdot 20\,\text{ml} = 137{,}0\,\text{g}$, mikä vastaa mitattua $137{,}6\,\text{g}$:aa.

### d)
**Annettu:** b-kohdan kuvaaja, jossa pisteillä on epävarmuusjanat $\pm 1\,\text{ml}$; c-kohdasta $k = 0{,}919\,\text{g/cm}^3$; taulukon tiheydet $1{,}00$, $0{,}92$ ja $0{,}79\,\text{g/cm}^3$
**Kysytty:** tiheyden epävarmuus $\Delta\rho$ ja nesteen tunnistus
**Periaate:** Jyrkin ja loivin suora, jotka vielä kulkevat kaikkien epävarmuusjanojen kautta, rajaavat kulmakertoimen arvioidun vaihteluvälin. Epävarmuudeksi otetaan sen puolikas, ja tulosta verrataan taulukon tiheyksiin.
**Kuvaajan lukeminen:** Jyrkimmän suoran kulmakerroin on noin $k_\text{max} = 0{,}932\,\text{g/cm}^3$ ja loivimman $k_\text{min} = 0{,}908\,\text{g/cm}^3$.
**Kaava:** $\Delta\rho = \dfrac{k_\text{max} - k_\text{min}}{2}$
**Muunnokset:** Ei tarvita: kaikki tiheydet ovat yksikössä $\text{g/cm}^3$.
**Sijoitus:** $\Delta\rho = \dfrac{0{,}932\,\text{g/cm}^3 - 0{,}908\,\text{g/cm}^3}{2} = 0{,}012\,\text{g/cm}^3$
**Vastaus:** $\rho = (0{,}919 \pm 0{,}012)\,\text{g/cm}^3$; epävarmuuden ensimmäinen numero on $1$, joten siinä on kaksi numeroa, ja tiheys samaan desimaaliin. Väli $0{,}907$–$0{,}931\,\text{g/cm}^3$ sisältää ruokaöljyn tiheyden $0{,}92\,\text{g/cm}^3$, mutta ei veden $1{,}00$ eikä etanolin $0{,}79\,\text{g/cm}^3$. Neste on todennäköisesti ruokaöljyä. Päättely ei ole varma, sillä jollain muulla nesteellä voi olla sama tiheys.
**Järkevyys:** Suhteellinen epävarmuus on $0{,}012 : 0{,}919 \approx 1{,}3\,\%$, mikä sopii siihen, että tilavuuden lukeman epävarmuus $1\,\text{ml}$ on noin $1\,\%$ mitatusta $80\,\text{ml}$:n välistä. Ero veteen, $0{,}08\,\text{g/cm}^3$, on monta kertaa epävarmuuden suuruinen.

### e)
**Annettu:** d-kohdasta $\rho = 0{,}919\,\text{g/cm}^3$; tilavuus $V = 1{,}50\,\text{l}$
**Kysytty:** nesteen massa $m$ ja onko tuloksen käyttö perusteltua
**Periaate:** Tiheys on aineen ominaisuus, joten saman nesteen massa on suoraan verrannollinen tilavuuteen: $m = \rho V$. Mittalasin massa ei kuulu nesteeseen, joten sitä ei lisätä.
**Kaava:** $m = \rho V$
**Muunnokset:** $V = 1{,}50\,\text{l} = 1{,}50 \cdot 1000\,\text{cm}^3 = 1500\,\text{cm}^3$, ja lopuksi $1000\,\text{g} = 1\,\text{kg}$.
**Sijoitus:** $m = 0{,}919\,\tfrac{\text{g}}{\text{cm}^3} \cdot 1500\,\text{cm}^3 = 1378\,\text{g} = 1{,}378\,\text{kg}$
**Vastaus:** $m \approx 1{,}38\,\text{kg}$. Tiheys tunnetaan d-kohdan mukaan noin $1{,}3\,\%$:n tarkkuudella, joten tulos on $(1{,}38 \pm 0{,}02)\,\text{kg}$ ja epävarmuus ulottuu kolmanteen numeroon, kuten tilavuudessakin $1{,}50\,\text{l}$. Tilavuus on $15$-kertainen mitattuun alueeseen verrattuna, mutta laskussa ei jatketa mittalasin suoraa vaan käytetään tiheyttä, joka on aineen ominaisuus ja pysyy samana samassa lämpötilassa. Siksi tulos on fysikaalisesti perusteltu, kunhan öljyn lämpötila on sama kuin mittauksessa.
**Järkevyys:** Saman tilavuuden vesi painaisi $1{,}50\,\text{kg}$, ja öljy on noin $8\,\%$ kevyempää, joten $1{,}38\,\text{kg}$ on oikean suuruinen.

### Hyväksytään myös
- c-kohdassa laskimen tai taulukkolaskennan suoran sovitus ilman riviä $60\,\text{ml}$: $k = 0{,}918\,\text{g/cm}^3$ ja $b = 118{,}6\,\text{g}$. Kulmakertoimet $0{,}90$–$0{,}94\,\text{g/cm}^3$ ja vakiotermit $117{,}5$–$119{,}5\,\text{g}$ hyväksytään.
- b-kohdassa rivin $60\,\text{ml}$ pitäminen mukana, kun sen vaikutus tarkistetaan: kulmakerroin ei muutu, koska piste on mittausalueen keskellä, mutta vakiotermi kasvaa noin $1\,\text{g}$. Ratkaisu on perusteltava.
- d-kohdassa silmämääräisesti piirretyistä ääriviivoista saatu $\Delta\rho = 0{,}01$–$0{,}02\,\text{g/cm}^3$.

### Yleisiä virheitä
- Tiheys lasketaan jakamalla jonkin rivin massa tilavuudella, esimerkiksi $$
\begin{aligned}
&210{,}3\,\text{g} : 100\,\text{ml} \\
&= 2{,}10\,\text{g/cm}^3
\end{aligned}
$$. Massaan sisältyy mittalasi.
- Suora pakotetaan origon kautta, jolloin kulmakertoimesta tulee liian suuri ja neste tunnistetaan väärin.
- Rivin $60\,\text{ml}$ piste poistetaan mainitsematta syytä, tai sen takia pisteet yhdistetään murtoviivaksi.
- Kulmakerroin luetaan kahdesta vierekkäisestä mittauspisteestä.
- e-kohdassa massaan lisätään mittalasin massa tai mittalasin suoraa jatketaan $1500\,\text{ml}$:iin, jolloin tulokseen tulee ylimääräinen $119\,\text{g}$.

## fy9-mittaaminen-s4

### a)
**Kysytty:** aineistossa näkyvät virhelajit perusteluineen
**Periaate:** Systemaattinen virhe siirtää tuloksia samaan suuntaan, satunnaisvirhe näkyy toistojen vaihteluna ja karkea virhe yksittäisenä muista selvästi poikkeavana tuloksena.
**Mallivastaus:** *Systemaattinen virhe.* Jokainen lukema on suurempi kuin punnuksen tunnettu massa, ja ero toistuu samanlaisena joka punnituksessa. Lukemien keskiarvot ovat noin $101{,}7$, $204{,}3$, $510{,}3$ ja $1020{,}3\,\text{g}$, joten virhe on noin $2$, $4$, $10$ ja $20\,\text{g}$. Virhe kasvaa samassa suhteessa kuin massa, noin $2\,\%$: $20\,\text{g} : 1000\,\text{g} = 0{,}02$. Koska tyhjä vaaka näyttää $0\,\text{g}$, nollakohta on oikein ja virhe on suhteellinen.

*Satunnaisvirhe.* Saman punnuksen kolme lukemaa eroavat toisistaan enintään $1\,\text{g}$. Vaihtelu on samaa suuruusluokkaa kuin näytön resoluutio $1\,\text{g}$.

*Karkea virhe.* Mikään lukema ei poikkea selvästi saman punnuksen muista lukemista, joten karkeaa virhettä ei näy.

### b)
**Kysytty:** onko väite $(765 \pm 0{,}5)\,\text{g}$ oikein, ja parempi arvio jauhojen massasta
**Periaate:** Resoluutio on pienin näytössä näkyvä muutos. Se ei kerro systemaattisesta virheestä, joten epävarmuus voi olla paljon resoluutiota suurempi. Tunnettu systemaattinen virhe korjataan.
**Mallivastaus:** Väite ei pidä. Puolikas resoluutiosta, $0{,}5\,\text{g}$, kertoo vain, kuinka tarkasti näytön voi lukea. a-kohdan mukaan vaaka näyttää noin $2\,\%$ liikaa, ja toistot vaihtelevat noin $1\,\text{g}$. Vaaka näyttää massasta $m$ lukeman $m_\text{lukema} = k\,m$, missä $k$ on punnuksilta saatu suhde $1020\,\text{g} : 1000\,\text{g} = 1{,}02$. Korjattu massa on siis $$
\begin{aligned}
m &= \dfrac{m_\text{lukema}}{k} \\
&= 765\,\text{g} : 1{,}02 \\
&= 750\,\text{g}
\end{aligned}
$$. Epävarmuutta lisäävät toistojen vaihtelu ja se, että korjauskerroin tunnetaan vain noin tuhannesosan tarkkuudella, mikä tekee $765\,\text{g}$:n lukemassa alle grammaa. Parempi arvio on noin $(750 \pm 2)\,\text{g}$. Ystävän tulos on siis noin $15\,\text{g}$ liian suuri, ja sen epävarmuus on liian pieni.

### c)
**Kysytty:** kuvaajan muoto, mitä siitä näkee virheen laadusta, ja miksi toistaminen ei auta
**Periaate:** Jos vaaka olisi oikea, lukema olisi sama kuin punnuksen massa, ja pisteet olisivat suoralla, jonka kulmakerroin on $1$ ja vakiotermi $0$. Nollakohdan virhe näkyisi vakiotermissä ja suhteellinen virhe kulmakertoimessa.
**Mallivastaus:** Pisteet ovat origon kautta kulkevalla suoralla: lukema on suoraan verrannollinen punnuksen massaan, $m_\text{lukema} \propto m_\text{punnus}$. Kulmakerroin $k = \dfrac{\Delta m_\text{lukema}}{\Delta m_\text{punnus}}$ luetaan sovitetulta suoralta kahdesta kaukana toisistaan olevasta pisteestä, joita ovat pisteet $100{,}0\,\text{g}$ ja $1000{,}0\,\text{g}$ kohdalla (kaikki pisteet ovat suoralla): $$
\begin{aligned}
k &= (1020{,}3\,\text{g} - 101{,}7\,\text{g}) \\
&: (1000{,}0\,\text{g} - 100{,}0\,\text{g}) \\
&\approx 1{,}02
\end{aligned}
$$ eikä $1$, ja vakiotermi on nolla. Vakiotermi nolla kertoo, että nollakohta on oikein, ja kulmakerroin $1{,}02$ kertoo, että vaaka näyttää jokaisesta massasta $2\,\%$ liikaa. Kuvaajan pisteet ovat hyvin tarkasti suoralla, koska satunnaisvaihtelu, noin $1\,\text{g}$, on pieni.

Toistaminen vaimentaa satunnaisvirheen vaikutusta keskiarvossa, koska liian suuret ja liian pienet lukemat kumoavat osittain toisensa. Systemaattinen virhe on kuitenkin joka punnituksessa sama, joten keskiarvo on yhtä paljon väärin kuin yksittäinen lukema. Virhe korjataan jakamalla lukemat kulmakertoimella $1{,}02$ tai kalibroimalla vaaka punnuksen avulla.

### Yleisiä virheitä
- Kaikkia poikkeamia pidetään satunnaisina, koska ne ovat pieniä; ne ovat kuitenkin kaikki samaan suuntaan.
- Virhettä pidetään vakiona $2\,\text{g}$:na, ja korjauksessa vähennetään lukemasta $2\,\text{g}$; virhe on suhteellinen.
- Näytön resoluutiota pidetään mittauksen epävarmuutena.
- Korjaus tehdään väärään suuntaan, $765\,\text{g} \cdot 1{,}02 = 780\,\text{g}$.

## fy9-mittaaminen-s5

### a)
**Kysytty:** raportin puutteet ja miksi kukin heikentää tulosta
**Periaate:** Mittauspisteisiin sovitetaan malli, jonka valinta perustellaan fysikaalisesti. Kulmakerroin luetaan sovitetulta suoralta, poikkeava piste tarkistetaan ennen kuin se jätetään pois, ja tulos ilmoitetaan epävarmuuksineen.
**Mallivastaus:**
- *Murtoviiva.* Pisteitä yhdistävä viiva seuraa myös mittausvirheitä, eikä se ole malli. Tasaisessa liikkeessä paikka muuttuu tasaisesti, joten pisteisiin sovitetaan yksi suora.
- *Nopeus kahdesta vierekkäisestä pisteestä.* Kummankin pisteen merkitsemisvirhe vaikuttaa tulokseen täysin: jos kumpikin paikka voi olla $0{,}03\,\text{m}$ väärin, nopeus voi olla $0{,}12\,\text{m/s}$ väärin. Siksi tulos $0{,}42\,\text{m/s}$ on epävarma.
- *Suora origon kautta.* Ajanotto alkoi, kun auto oli jo liikkeessä noin $0{,}35\,\text{m}$:n kohdalla, joten paikka ei ole nolla hetkellä $t = 0$. Pakotettu suora on liian jyrkkä, ja kulmakerroin $0{,}63\,\text{m/s}$ on liian suuri.
- *Piste poistettiin perustelematta.* Piste poikkeaa noin $0{,}25\,\text{m}$, mikä on paljon. Syy olisi pitänyt tarkistaa videolta, esimerkiksi onko auto merkitty väärään kuvaan, ja poisjättö syineen kirjata.
- *Tulos ja johtopäätös.* Tuloksessa on neljä merkitsevää numeroa eikä epävarmuutta, ja tulos valittiin sen mukaan, mikä tuntui sopivalta, eikä menetelmän perusteella.

### b)
**Kysytty:** leluauton nopeus epävarmuuksineen ja pisteen $t = 1{,}5\,\text{s}$ käsittely
**Kuvaaja:** Vaaka-akselilla on aika $t\ (\text{s})$ ja pystyakselilla paikka $x\ (\text{m})$. Pisteisiin on merkitty epävarmuusjanat $\pm 0{,}03\,\text{m}$, joka on arvio videolta merkitsemisen tarkkuudesta.

<svg data-fig="s5-kuvaaja" viewBox="0 0 600 410" role="img" aria-label="Kuvaaja: leluauton paikka x metreinä ajan t funktiona sekunteina, 0–3,0 s. Kuusi sinistä pistettä on lähellä yhtä nousevaa suoraa; paikan epävarmuus ±0,03 m on pisteen kokoa pienempi, joten epävarmuusjanat jäävät pisteiden sisään. Piste (1,5 s; 1,32 m) on piirretty ontoksi punaiseksi ympyräksi: se on noin 0,25 m suoran yläpuolella. Suora leikkaa pystyakselin kohdassa 0,36 m, ei origossa, ja sen kulmakerroin on 0,48 m/s. Suoralta luetut pisteet (0 s; 0,36 m) ja (3,0 s; 1,79 m) on ympyröity." style="max-width:100%;font-size:30px">
  <line x1="142" y1="360" x2="142" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200.5" y1="360" x2="200.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258.5" y1="360" x2="258.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317" y1="360" x2="317" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375" y1="360" x2="375" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="433.5" y1="360" x2="433.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="270" x2="480" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="180" x2="480" y2="180" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="90" x2="480" y2="90" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="360" x2="494" y2="360" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,360 L493,366 L493,354 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="361" x2="84" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,34 L90,47 L78,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="142" y1="360" x2="142" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="114.5" y="366" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0{,}5$</div></foreignObject>
  <line x1="200.5" y1="360" x2="200.5" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="188.5" y="366" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1$</div></foreignObject>
  <line x1="258.5" y1="360" x2="258.5" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="231" y="366" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1{,}5$</div></foreignObject>
  <line x1="317" y1="360" x2="317" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="305" y="366" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="375" y1="360" x2="375" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="347.5" y="366" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2{,}5$</div></foreignObject>
  <line x1="433.5" y1="360" x2="433.5" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="421.5" y="366" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$3$</div></foreignObject>
  <line x1="77" y1="270" x2="84" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="252" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0{,}6$</div></foreignObject>
  <line x1="77" y1="180" x2="84" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="162" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1{,}2$</div></foreignObject>
  <line x1="77" y1="90" x2="84" y2="90" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="72" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1{,}8$</div></foreignObject>
  <foreignObject x="50" y="362" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="512" y="342" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="74" y="0" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$x\ (\text{m})$</div></foreignObject>
  <polyline points="84,306.5 468.5,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="84" y1="312" x2="84" y2="303" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="84" cy="307.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="142" y1="273" x2="142" y2="264" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="142" cy="268.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="200.5" y1="240" x2="200.5" y2="231" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="200.5" cy="235.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="317" y1="169.5" x2="317" y2="160.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="317" cy="165" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="375" y1="129" x2="375" y2="120" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="375" cy="124.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="433.5" y1="97.5" x2="433.5" y2="88.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="433.5" cy="93" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="258.5" cy="162" r="6.5" fill="#ffffff" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="111.5" y="130" width="133" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px;color:#c92a2a">$\text{tarkista}$</div></foreignObject>
  <circle cx="84" cy="306" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="433.5" cy="91.5" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="258.5" y="274.5" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$v = k \approx 0{,}48\,\tfrac{\text{m}}{\text{s}}$</div></foreignObject>
</svg>

**Mallivastaus:** Kuusi pistettä on lähellä yhtä suoraa, joten auto liikkui tasaisesti ja paikka on lineaarinen ajan funktio, $x = vt + x_0$. Nopeus on suoran kulmakerroin $v = \dfrac{x_2 - x_1}{t_2 - t_1}$. Piste $t = 1{,}5\,\text{s}$ on noin $0{,}25\,\text{m}$ suoran yläpuolella, lähes samassa paikassa kuin piste $t = 2{,}0\,\text{s}$, joten se on todennäköisesti merkitty väärään kuvaan. Piste tarkistetaan videolta. Jos virhe löytyy, se korjataan tai piste jätetään pois ja syy kirjataan.

Suoraa ei pakoteta origon kautta. Siltä luetaan kaksi kaukana toisistaan olevaa pistettä, $(0\,\text{s};\ 0{,}36\,\text{m})$ ja $(3{,}0\,\text{s};\ 1{,}79\,\text{m})$, joten nopeus on $$
\begin{aligned}
v &= \dfrac{1{,}79\,\text{m} - 0{,}36\,\text{m}}{3{,}0\,\text{s} - 0\,\text{s}} \\
&= 0{,}477\,\tfrac{\text{m}}{\text{s}}
\end{aligned}
$$. Vakiotermi $0{,}36\,\text{m}$ on auton paikka ajanoton alkaessa. Jyrkin ja loivin suora, jotka kulkevat kaikkien janojen kautta, antavat kulmakertoimet noin $0{,}492$ ja $0{,}464\,\text{m/s}$, joten $$
\begin{aligned}
\Delta v &= (0{,}492 - 0{,}464)\,\text{m/s} \\
&: 2 \\
&= 0{,}014\,\text{m/s}
\end{aligned}
$$.

Tulos on $v = (0{,}477 \pm 0{,}014)\,\text{m/s}$, kun epävarmuudessa pidetään kaksi numeroa, koska sen ensimmäinen numero on $1$. Tulos on sopusoinnussa raportin kahden pisteen arvon $0{,}42\,\text{m/s}$ kanssa vain sen suuren epävarmuuden ansiosta, mutta ei origon kautta pakotetun suoran arvon $0{,}63\,\text{m/s}$ kanssa.

### c)
**Kysytty:** kaksi perusteltua parannusta, joista toinen koskee systemaattista virhettä
**Periaate:** Satunnaisvirheen vaikutusta pienennetään lisäämällä mittauksia ja pidentämällä mitattavaa väliä. Systemaattinen virhe paljastuu vain vertaamalla tunnettuun arvoon tai toiseen menetelmään.
**Mallivastaus:** *Mittakaavan tarkistus.* Jos mittanauha on lähempänä kameraa kuin auto tai kamera kuvaa vinosti, videon metri ei ole auton kulkulinjalla metri. Silloin kaikki paikat ja nopeus ovat samassa suhteessa väärin, eikä virhe näy pisteiden hajonnassa. Mittanauha asetetaan auton kulkulinjalle, kamera kohtisuoraan liikettä vastaan ja riittävän kauas, ja mittakaava tarkistetaan mittaamalla videolta jokin toinen tunnettu pituus.

*Lisää ja pidempää aineistoa.* Kun auto kuvataan pidemmältä matkalta ja paikka merkitään esimerkiksi $0{,}1\,\text{s}$:n välein, kulmakerroin määräytyy useammasta pisteestä ja pidemmältä väliltä. Silloin yhden pisteen merkitsemisvirhe vaikuttaa vähemmän, ja jyrkimmän ja loivimman suoran ero pienenee. Toistetut ajot kertovat lisäksi, vaihteleeko auton nopeus ajosta toiseen.

### Hyväksytään myös
- b-kohdassa laskimen tai taulukkolaskennan suoran sovitus ilman pistettä $1{,}5\,\text{s}$: $v = 0{,}477\,\text{m/s}$ ja vakiotermi $0{,}358\,\text{m}$. Nopeudet $0{,}46$–$0{,}50\,\text{m/s}$ hyväksytään.
- b-kohdassa pisteen pitäminen mukana, kun sen vaikutus tarkistetaan: piste on mittausalueen keskellä, joten kulmakerroin ei muutu, mutta pisteet eivät enää ole suoralla epävarmuuksien rajoissa.
- b-kohdassa epävarmuus $\pm 0{,}02\,\text{m/s}$ ja tulos $(0{,}48 \pm 0{,}02)\,\text{m/s}$.

### Yleisiä virheitä
- Raportista nimetään puutteita perustelematta, miksi ne heikentävät tulosta.
- Poikkeavan pisteen poistamista pidetään aina virheenä tai aina oikeana; ratkaisevaa on, löytyykö poikkeamalle syy ja kirjataanko se.
- b-kohdassa suora pakotetaan origon kautta tai nopeus lasketaan yhdestä pisteestä $x : t$.
- c-kohdassa ehdotetaan vain "tarkempaa mittaamista" kertomatta, mitä tehdään ja miksi se auttaa.

## fy9-mittaaminen-s6

### a)
**Kysytty:** onko paine kääntäen verrannollinen ruiskun lukemaan $V$
**Periaate:** Jos $p$ on kääntäen verrannollinen suureeseen $V$, tulo $pV$ on vakio. Väitettä testataan laskemalla tulo eri riveillä ja katsomalla, vaihteleeko se satunnaisesti vai muuttuuko se järjestelmällisesti samaan suuntaan.
**Mallivastaus:** Ensimmäisellä rivillä $$
\begin{aligned}
pV &= 189{,}1\,\text{kPa} \cdot 12\,\text{ml} \\
&= 2269\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$ ja viimeisellä $$
\begin{aligned}
&81{,}8\,\text{kPa} \cdot 30\,\text{ml} \\
&= 2454\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$. Välirivien tulot kasvavat tasaisesti rivi riviltä, ja koko kasvu on $(2454 - 2269) : 2269 \approx 8\,\%$. Paineet on annettu kymmenesosakilopascalin tarkkuudella, ja tulo kasvaa joka rivillä samaan suuntaan. Satunnaisvirhe vaihtelisi sattumanvaraisesti, joten tasainen $8\,\%$:n kasvu ei johdu siitä. Väite ei siis päde ruiskun lukemaan $V$. Tulon kasvu viittaa siihen, että ilman todellinen tilavuus on lukemaa suurempi: osa ilmasta on letkussa ja anturissa, ja sen osuus on suurin, kun ruiskun tilavuus on pieni.

### b)
**Kysytty:** kuvaaja, jossa riippuvuus on suoraviivainen, ja siihen sovitettu suora
**Kuvaaja:** Ilman todellinen tilavuus on $V + V_0$. Kun lämpötila ja ilman määrä pysyvät samoina, Boylen lain mukaan $p(V + V_0) = C$, joten $V = C \cdot \tfrac{1}{p} - V_0$. Vaaka-akselille valitaan siksi $\tfrac{1}{p}$ ja pystyakselille $V$. Esimerkiksi ensimmäisellä rivillä $$
\begin{aligned}
&\tfrac{1}{p} \\
&= \tfrac{1}{189{,}1\,\text{kPa}} \\
&= \tfrac{1}{0{,}1891\,\text{MPa}} \\
&= 5{,}29\,\tfrac{1}{\text{MPa}}
\end{aligned}
$$ ja viimeisellä $12{,}2\,\tfrac{1}{\text{MPa}}$.

<svg data-fig="s6-kuvaaja" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: ruiskun asteikon tilavuus V millilitroina paineen käänteisluvun 1/p funktiona yksikössä 1/MPa. Kymmenen sinistä pistettä välillä 5,3–12,2 1/MPa ovat yhdellä nousevalla suoralla. Suoraa on jatkettu katkoviivana pystyakselille, jonka se leikkaa negatiivisella puolella kohdassa −1,8 ml. Kulmakerroin on 2,60 MPa · ml. Vaaka-akseli on piirretty kohtaan V = 0." style="max-width:100%;font-size:30px">
  <line x1="132" y1="400" x2="132" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="400" x2="180" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="228" y1="400" x2="228" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="400" x2="276" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="400" x2="324" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="372" y1="400" x2="372" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="400" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="369" x2="420" y2="369" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="307.5" x2="420" y2="307.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="276.5" x2="420" y2="276.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="245.5" x2="420" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="214.5" x2="420" y2="214.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="183.5" x2="420" y2="183.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="152.5" x2="420" y2="152.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="122" x2="420" y2="122" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="91" x2="420" y2="91" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="60" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="400" x2="84" y2="338" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="83" y1="338" x2="434" y2="338" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,338 L433,344 L433,332.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="339" x2="84" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,34 L90,47 L78,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="132" y1="338" x2="132" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="338" x2="180" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="168" y="298" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="228" y1="338" x2="228" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="276" y1="338" x2="276" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="264" y="298" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$8$</div></foreignObject>
  <line x1="324" y1="338" x2="324" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="372" y1="338" x2="372" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352.5" y="298" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$12$</div></foreignObject>
  <line x1="420" y1="338" x2="420" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="400" x2="84" y2="400" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="382" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$-8$</div></foreignObject>
  <line x1="77" y1="369" x2="84" y2="369" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="338" x2="84" y2="338" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="307.5" x2="84" y2="307.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="276.5" x2="84" y2="276.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="258.5" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$8$</div></foreignObject>
  <line x1="77" y1="245.5" x2="84" y2="245.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="214.5" x2="84" y2="214.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="196.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$16$</div></foreignObject>
  <line x1="77" y1="183.5" x2="84" y2="183.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="152.5" x2="84" y2="152.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="134.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$24$</div></foreignObject>
  <line x1="77" y1="122" x2="84" y2="122" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="91" x2="84" y2="91" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="73" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$32$</div></foreignObject>
  <line x1="77" y1="60" x2="84" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="452" y="320" width="106" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$\tfrac{1}{p}\ (\tfrac{1}{\text{MPa}})$</div></foreignObject>
  <foreignObject x="74" y="0" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$V\ (\text{ml})$</div></foreignObject>
  <polyline points="84,352 194.5,259.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <polyline points="194.5,259.5 405.5,82.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="211" cy="245.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="230" cy="230" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="247.5" cy="214.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="266" cy="199" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="285.5" cy="183.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="303" cy="168" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="321" cy="152.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="340.5" cy="137.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="358" cy="122" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="377.5" cy="106.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="84" cy="352" r="9" fill="none" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="104" y="360.5" width="180" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$-V_0 \approx -1{,}8\,\text{ml}$</div></foreignObject>
  <foreignObject x="96" y="80.5" width="195" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$k \approx 2{,}6\,\text{MPa} \cdot \text{ml}$</div></foreignObject>
</svg>

**Mallivastaus:** Pisteet asettuvat hyvin suoralle, joten malli $p(V + V_0) = C$ sopii aineistoon. Suora ei kulje origon kautta: sitä jatketaan pystyakselille, jonka se leikkaa negatiivisella puolella. Jos letkussa ei olisi ilmaa, suora kulkisi origon kautta. Yksikkö $\tfrac{1}{\text{MPa}}$ on valittu, jotta akselin luvut ovat helppolukuisia.

### c)
**Annettu:** b-kohdan suora; $T = 22\,{}^\circ\text{C}$; $R = 8{,}314\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}}$
**Kysytty:** letkun ja anturin ilmatilavuus $V_0$ ja ilman ainemäärä $n$
**Periaate:** Suoran yhtälö on $V = C \cdot \tfrac{1}{p} - V_0$, joten vakiotermi on $-V_0$ ja kulmakerroin $C = p(V + V_0)$. Ideaalikaasun tilanyhtälön mukaan $p(V + V_0) = nRT$, joten kulmakertoimesta saadaan ainemäärä. Tilanyhtälössä lämpötila on kelvineinä.
**Kuvaajan lukeminen:** Suora leikkaa pystyakselin kohdassa $-1{,}8\,\text{ml}$. Suoralta luetaan kaksi kaukana toisistaan olevaa pistettä, $(4{,}0\,\tfrac{1}{\text{MPa}};\ 8{,}6\,\text{ml})$ ja $(12{,}0\,\tfrac{1}{\text{MPa}};\ 29{,}5\,\text{ml})$.
**Kaava:** $V_0 = -b$, $C = \dfrac{\Delta V}{\Delta (1/p)}$ ja $C = nRT$, joten $n = \dfrac{C}{RT}$
**Muunnokset:** $$
\begin{aligned}
&1\,\text{MPa} \cdot \text{ml} \\
&= 10^{6}\,\text{Pa} \cdot 10^{-6}\,\text{m}^3 \\
&= 1\,\text{Pa} \cdot \text{m}^3 \\
&= 1\,\text{J}
\end{aligned}
$$ ja $T = (22 + 273{,}15)\,\text{K} = 295{,}15\,\text{K}$
**Sijoitus:** $V_0 = 1{,}8\,\text{ml}$, $C = \dfrac{29{,}5\,\text{ml} - 8{,}6\,\text{ml}}{12{,}0\,\tfrac{1}{\text{MPa}} - 4{,}0\,\tfrac{1}{\text{MPa}}} = 2{,}61\,\text{MPa} \cdot \text{ml} = 2{,}61\,\text{J}$ ja $n = \dfrac{2{,}61\,\text{J}}{8{,}314\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}} \cdot 295{,}15\,\text{K}} = 1{,}06 \cdot 10^{-3}\,\text{mol}$
**Vastaus:** $V_0 \approx 1{,}8\,\text{ml}$ ja $n \approx 1{,}06 \cdot 10^{-3}\,\text{mol}$. Tilavuudessa on kaksi merkitsevää numeroa, koska se luetaan kuvaajasta noin $0{,}1\,\text{ml}$:n tarkkuudella; ainemäärässä kolme kuten kulmakertoimessa.
**Järkevyys:** Normaalipaineessa ja huoneenlämmössä mooli kaasua vie noin $24\,\text{l}$, joten noin $26\,\text{ml}$ ilmaa on noin $26\,\text{ml} : 24\,000\,\text{ml/mol} \approx 1{,}1 \cdot 10^{-3}\,\text{mol}$. Letkun ja anturin muutaman millilitran ilmatila on lyhyelle letkulle uskottava. Kun $V_0$ lisätään, tulo $p(V + V_0)$ on ensimmäisellä rivillä $$
\begin{aligned}
&189{,}1\,\text{kPa} \cdot 13{,}8\,\text{ml} \\
&= 2610\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$ ja viimeisellä $$
\begin{aligned}
&81{,}8\,\text{kPa} \cdot 31{,}8\,\text{ml} \\
&= 2601\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$, eli lähes vakio.

### d)
**Kysytty:** tuloksen oletukset ja niiden vaikutus
**Periaate:** Malli $p(V + V_0) = nRT$ olettaa, että ilman määrä ja lämpötila pysyvät samoina ja että tilavuus on mitattu kokonaan. Kunkin oletuksen kohdalla mietitään, mihin suuntaan tulos muuttuisi, jos se ei pitäisi.
**Mallivastaus:** *Lämpötila pysyy samana.* Puristaminen on työtä, joka kasvattaa ilman sisäenergiaa. Kun mäntää painetaan hitaasti, ilma ehtii luovuttaa lämmön ruiskun seinien kautta ja pysyy huoneen lämpöisenä. Nopeassa puristuksessa ilma lämpenisi, paine olisi hetkellisesti suurempi kuin malli antaa, ja tulo $p(V + V_0)$ kasvaisi puristuksen aikana.

*Ilmaa ei vuoda.* Jos ilmaa vuotaisi männän ohi suuressa paineessa, ainemäärä pienenisi kesken mittauksen, ja tulo $p(V + V_0)$ pienenisi pienillä tilavuuksilla.

*Koko tilavuus on mukana.* Ilman $V_0$:aa tulo $pV$ näyttäisi kasvavan tilavuuden mukana, ja aineistosta voisi päätellä väärin, ettei Boylen laki päde. Myös ainemäärä laskettaisiin väärästä tilavuudesta.

*Johtopäätös.* Kun $V_0 = 1{,}8\,\text{ml}$ lisätään lukemaan, $p(V + V_0)$ on koko mittausalueella noin $2600\,\text{kPa} \cdot \text{ml}$ alle puolen prosentin vaihtelulla. Aineisto on siis sopusoinnussa mallin kanssa, mikä tukee sitä, että oletukset pitivät.

### Hyväksytään myös
- b-kohdassa $(\tfrac{1}{p}, V)$-kuvaaja yksikössä $\tfrac{1}{\text{kPa}}$, jolloin kulmakerroin on $2600\,\text{kPa} \cdot \text{ml} = 2{,}60\,\text{J}$.
- b- ja c-kohdassa laskimen tai taulukkolaskennan sovitus: $C = 2{,}603\,\text{J}$ ja $V_0 = 1{,}77\,\text{ml}$. Arvot $V_0 = 1{,}5$–$2{,}1\,\text{ml}$ ja $n = (1{,}01$–$1{,}11) \cdot 10^{-3}\,\text{mol}$ hyväksytään.
- c-kohdassa ainemäärä yhdeltä riviltä, kun $V_0$ on lisätty: $$
\begin{aligned}
n &= \tfrac{101{,}2\,\text{kPa} \cdot 25{,}8\,\text{ml}}{RT} \\
&\approx 1{,}06 \cdot 10^{-3}\,\text{mol}
\end{aligned}
$$.

### Yleisiä virheitä
- a-kohdassa todetaan $pV$:n "olevan lähes vakio" katsomatta, mihin suuntaan tulo muuttuu rivi riviltä, jolloin systemaattinen kasvu jää huomaamatta.
- b-kohdassa piirretään $(\tfrac{1}{V}, p)$-kuvaaja ja pakotetaan suora origon kautta; letkun ilmatila ei silloin näy.
- c-kohdassa lämpötila sijoitetaan celsiusasteina tai tilavuus millilitroina ja paine kilopascaleina ilman muunnosta, jolloin ainemäärä on tuhat kertaa väärin.
- d-kohdassa luetellaan oletuksia kertomatta, mihin suuntaan ne muuttaisivat tulosta.

## fy9-mittaaminen-s7

### a)
**Annettu:** kuvan viivain, jonka pienin asteikkoväli on $1\,\text{mm}$; tangon vasen pää on kohdassa $2{,}0\,\text{cm}$ ja oikea pää kohdassa $13{,}6\,\text{cm}$
**Kysytty:** tangon pituus $l$
**Periaate:** Pituus on tangon päiden paikkojen erotus viivaimella. Tanko ei ala viivaimen nollakohdasta, joten pelkkä oikean pään lukema ei ole pituus (luku *Suureet, yksiköt ja SI-järjestelmä*).
**Kuvaajan lukeminen:** Tangon päät luetaan millimetrin asteikolta: vasen pää $2{,}0\,\text{cm}$ ja oikea pää $13{,}6\,\text{cm}$.
**Kaava:** $l = x_\text{oikea} - x_\text{vasen}$
**Muunnokset:** Ei tarvita: kumpikin lukema on senttimetreinä.
**Sijoitus:** $$
\begin{aligned}
l &= 13{,}6\,\text{cm} - 2{,}0\,\text{cm} \\
&= 11{,}6\,\text{cm}
\end{aligned}
$$
**Vastaus:** $l = 11{,}6\,\text{cm}$, kolme merkitsevää numeroa kuten luetuissa arvoissa.
**Järkevyys:** Tangon pituus on pienempi kuin viivaimen $15\,\text{cm}$. Jos pituudeksi luettaisiin pelkkä oikean pään lukema $13{,}6\,\text{cm}$, se olisi $2{,}0\,\text{cm}$ eli noin $17\,\%$ liian suuri, koska tanko ei ala viivaimen nollasta.

### b)
**Annettu:** lukemat $2{,}0\,\text{cm}$ ja $13{,}6\,\text{cm}$, asteikkoväli $1\,\text{mm}$; $l = 11{,}6\,\text{cm}$ a-kohdasta
**Kysytty:** pituuden epävarmuus $\Delta l$, pituus epävarmuuksineen ja suhteellinen epävarmuus
**Periaate:** Yhden lukeman epävarmuus on puolet asteikkovälistä. Pituus on kahden lukeman erotus, joten pahimmassa tapauksessa kumpikin lukema on väärin eri suuntaan ja epävarmuudet lasketaan yhteen.
**Kaava:** $\Delta l = \Delta x_\text{oikea} + \Delta x_\text{vasen}$ ja suhteellinen epävarmuus $\dfrac{\Delta l}{l}$
**Muunnokset:** $1\,\text{mm} = 0{,}1\,\text{cm}$, joten lukeman epävarmuus $0{,}5\,\text{mm}$ on $0{,}05\,\text{cm}$.
**Sijoitus:** $$
\begin{aligned}
\Delta x &= 0{,}5\,\text{mm} \\
&= 0{,}5 \cdot 0{,}1\,\text{cm} \\
&= 0{,}05\,\text{cm}
\end{aligned}
$$ $$
\begin{aligned}
\Delta l &= 0{,}05\,\text{cm} + 0{,}05\,\text{cm} \\
&= 0{,}10\,\text{cm}
\end{aligned}
$$ $$
\begin{aligned}
\dfrac{\Delta l}{l} &= \dfrac{0{,}10\,\text{cm}}{11{,}6\,\text{cm}} \\
&= 0{,}0086 \\
&\approx 0{,}9\,\%
\end{aligned}
$$
**Vastaus:** $l = (11{,}6 \pm 0{,}1)\,\text{cm}$ ja suhteellinen epävarmuus noin $0{,}9\,\%$. Epävarmuus ilmoitetaan yhdellä numerolla ja pituus samaan desimaaliin.
**Järkevyys:** Epävarmuus $1\,\text{mm}$ vastaa viivaimen yhtä pientä viivaväliä, mikä sopii siihen, että päät luetaan silmämääräisesti asteikolta. Kahden lukeman erotuksen epävarmuus on suurempi kuin yhden lukeman ($0{,}5\,\text{mm}$).

### c)
**Annettu:** $m = (15{,}7 \pm 0{,}05)\,\text{g}$, $d = (8{,}0 \pm 0{,}05)\,\text{mm}$ ja $l = (11{,}6 \pm 0{,}1)\,\text{cm}$; epävarmuus on puolet lukematarkkuudesta
**Kysytty:** tiheys $\rho$ epävarmuuksineen yksikössä $\text{kg/m}^3$ ja se mittaus, joka vaikuttaa epävarmuuteen eniten
**Periaate:** Tiheys on massa jaettuna tilavuudella (luku *Tiheys*). Tanko on sylinteri, joten tilavuus on poikkipinta-ala kertaa pituus. Kun tulos on tulo tai osamäärä, suhteelliset epävarmuudet lasketaan yhteen, ja potenssi $d^2$ kaksinkertaistaa halkaisijan suhteellisen epävarmuuden.
**Kaava:** $\rho = \dfrac{m}{V}$ ja $V = \dfrac{\pi d^2}{4}\,l$, joten $\rho = \dfrac{4m}{\pi d^2 l}$. Epävarmuus: $\dfrac{\Delta\rho}{\rho} = \dfrac{\Delta m}{m} + 2\,\dfrac{\Delta d}{d} + \dfrac{\Delta l}{l}$
**Muunnokset:** $d = 8{,}0\,\text{mm} = 0{,}80\,\text{cm}$ ja $\Delta d = 0{,}05\,\text{mm}$. Tiheyden yksikkö: $1\,\text{g} = 10^{-3}\,\text{kg}$ ja $1\,\text{cm}^3 = 10^{-6}\,\text{m}^3$, joten $1\,\text{g/cm}^3 = 1000\,\text{kg/m}^3$.
**Sijoitus:** Tilavuus: $$
\begin{aligned}
V &= \dfrac{\pi d^2}{4}\,l \\
&= \dfrac{\pi \cdot (0{,}80\,\text{cm})^2}{4} \cdot 11{,}6\,\text{cm} \\
&= 0{,}503\,\text{cm}^2 \cdot 11{,}6\,\text{cm} \\
&= 5{,}83\,\text{cm}^3
\end{aligned}
$$ Tiheys: $$
\begin{aligned}
\rho &= \dfrac{m}{V} \\
&= \dfrac{15{,}7\,\text{g}}{5{,}83\,\text{cm}^3} \\
&= 2{,}69\,\text{g/cm}^3 \\
&= 2{,}69 \cdot \dfrac{10^{-3}\,\text{kg}}{10^{-6}\,\text{m}^3} \\
&= 2{,}69 \cdot 10^3\,\text{kg/m}^3
\end{aligned}
$$ Suhteelliset epävarmuudet: $$
\begin{aligned}
\dfrac{\Delta m}{m} &= \dfrac{0{,}05\,\text{g}}{15{,}7\,\text{g}} \\
&= 0{,}0032
\end{aligned}
$$ $$
\begin{aligned}
2\,\dfrac{\Delta d}{d} &= 2 \cdot \dfrac{0{,}05\,\text{mm}}{8{,}0\,\text{mm}} \\
&= 0{,}0125
\end{aligned}
$$ ja pituuden $\dfrac{\Delta l}{l} = 0{,}0086$ b-kohdasta. Yhteensä: $$
\begin{aligned}
\dfrac{\Delta\rho}{\rho} &= 0{,}0032 \\
&\quad + 0{,}0125 \\
&\quad + 0{,}0086 \\
&= 0{,}0243 \\
&\approx 2{,}4\,\%
\end{aligned}
$$ Epävarmuus: $$
\begin{aligned}
\Delta\rho &= 0{,}0243 \cdot 2693\,\text{kg/m}^3 \\
&= 65\,\text{kg/m}^3
\end{aligned}
$$
**Vastaus:** $\rho = (2{,}69 \pm 0{,}07) \cdot 10^3\,\text{kg/m}^3$. Epävarmuus on pyöristetty yhteen numeroon ($65 \to 0{,}07 \cdot 10^3$) ja tulos samaan desimaaliin. Eniten epävarmuuteen vaikuttaa halkaisija: sen osuus on $1{,}25\,\%$, pituuden $0{,}9\,\%$ ja massan $0{,}3\,\%$. Halkaisija on vallitseva, koska lukematarkkuus $0{,}1\,\text{mm}$ on suuri suhteessa $8{,}0\,\text{mm}$:iin (suhteellinen epävarmuus $0{,}6\,\%$) ja neliö kaksinkertaistaa sen; ilman neliötä pituus olisi suurin.
**Järkevyys:** Tiheys $2{,}7\,\text{g/cm}^3$ tarkoittaa, että tangon massa on $2{,}7$-kertainen samankokoiseen vesimäärään verrattuna (veden tiheys on $1{,}0 \cdot 10^3\,\text{kg/m}^3$), mikä sopii kevytmetallille. Kokonaisepävarmuus $2{,}4\,\%$ on yhtä suuruusluokkaa kuin yksittäiset osuudet.

### d)
**Kysytty:** sopiiko tulos alumiinin taulukkoarvoon ja voiko tangon päätellä alumiiniksi tiheyden perusteella
**Periaate:** Tulos ja taulukkoarvo sopivat yhteen, jos taulukkoarvo on tuloksen epävarmuusvälin sisällä. Pelkkä lukujen erisuuruus ei kerro mitään ilman epävarmuutta.
**Mallivastaus:** Tuloksen väli on $$
\begin{aligned}
\rho_\text{min} &= 2693\,\text{kg/m}^3 \\
&\quad - 65\,\text{kg/m}^3 \\
&= 2628\,\text{kg/m}^3 \\
\rho_\text{max} &= 2693\,\text{kg/m}^3 \\
&\quad + 65\,\text{kg/m}^3 \\
&= 2758\,\text{kg/m}^3
\end{aligned}
$$ eli $2{,}63 \cdot 10^3 \ldots 2{,}76 \cdot 10^3\,\text{kg/m}^3$. Alumiinin taulukkoarvo on $2{,}70 \cdot 10^3\,\text{kg/m}^3$ ([MAFY-taulukko](https://mafytaulukot.fi/d67c966e-4e50-48d3-beae-9ae0a5f7838c/fi/1787666412/theory.html), tiheydet $20\,{}^\circ\text{C}$:n lämpötilassa), ja se on välin sisällä. Ero on $$
\begin{aligned}
\text{ero} &= 2700\,\text{kg/m}^3 \\
&\quad - 2693\,\text{kg/m}^3 \\
&= 7\,\text{kg/m}^3
\end{aligned}
$$ eli paljon pienempi kuin epävarmuus $65\,\text{kg/m}^3$. Tulos sopii siis alumiinin tiheyteen mittauksen tarkkuuden rajoissa, eikä se kumoa väitettä, että tanko on alumiinia. Tiheys yksin ei kuitenkaan todista ainetta: muillakin aineilla tai seoksilla voi olla lähes sama tiheys, joten oikea päätelmä on "tanko voi olla alumiinia". Tulokseen vaikuttavat esimerkiksi tangon päiden viisteet tai pyöristykset, jotka pienentävät todellista tilavuutta ja nostavat tiheyttä, sekä työntömitan nollavirhe. Tangon sisäiset onkalot taas pienentäisivät mitattua tiheyttä.

### Yleisiä virheitä
- a-kohdassa pituudeksi luetaan oikean pään lukema $13{,}6\,\text{cm}$, vaikka tanko alkaa kohdasta $2{,}0\,\text{cm}$.
- b-kohdassa pituuden epävarmuudeksi otetaan vain yhden lukeman epävarmuus $0{,}5\,\text{mm}$, vaikka erotuksessa on kaksi lukemaa.
- c-kohdassa halkaisija sijoitetaan millimetreinä mutta pituus senttimetreinä, tai halkaisija sijoitetaan säteenä kaavaan $\pi d^2/4$.
- c-kohdassa halkaisijan suhteellinen epävarmuus lasketaan ilman neliötä ($0{,}6\,\%$ eikä $1{,}25\,\%$), jolloin pituuden epävarmuus näyttää suurimmalta.
- d-kohdassa vertailu tehdään pelkästään lukuja katsomalla ("$2{,}69$ ei ole $2{,}70$") epävarmuutta huomioimatta.

### Hyväksytään myös
- b-kohdassa riippumattomien lukemien epävarmuus voidaan yhdistää neliöllisesti: $\Delta l = \sqrt{(0{,}05)^2 + (0{,}05)^2}\,\text{cm} = 0{,}07\,\text{cm}$. Tällöin $l = (11{,}6 \pm 0{,}1)\,\text{cm}$ pyöristyy samoin.
- c-kohdassa tiheys $2{,}69\,\text{g/cm}^3$ ja epävarmuus $0{,}07\,\text{g/cm}^3$ yksikössä $\text{g/cm}^3$ kelpaavat, kun muunnos tai yksikkö on kirjoitettu näkyviin.

## fy9-mittaaminen-s8

### a)
**Annettu:** viisi mittausta kuvasta: $12{,}2\,\text{s}$, $12{,}4\,\text{s}$, $12{,}6\,\text{s}$, $12{,}7\,\text{s}$ ja $12{,}9\,\text{s}$; kymmenen heilahduksen aika
**Kysytty:** kymmenen heilahduksen ajan keskiarvo $\bar{t}$ ja sen epävarmuus $\Delta t$
**Periaate:** Toistetuista mittauksista paras arvio on keskiarvo, ja satunnaisvaihtelun suuruutta arvioidaan vaihteluvälin puolikkaana (luku *Mittaaminen ja mittauksen luotettavuus*).
**Kuvaajan lukeminen:** Pisteet luetaan aika-akselilta, jossa pystyviivat ovat $0{,}1\,\text{s}$ välein: $12{,}2\,\text{s}$, $12{,}4\,\text{s}$, $12{,}6\,\text{s}$, $12{,}7\,\text{s}$ ja $12{,}9\,\text{s}$.
**Kaava:** $\bar{t} = \dfrac{t_1 + t_2 + t_3 + t_4 + t_5}{5}$ ja $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$
**Muunnokset:** Ei tarvita: kaikki ajat ovat sekunteina.
**Sijoitus:** $12{,}2 + 12{,}4 + 12{,}6 + 12{,}7 + 12{,}9 = 62{,}8\,\text{s}$ $$
\begin{aligned}
\bar{t} &= \dfrac{62{,}8\,\text{s}}{5} \\
&= 12{,}56\,\text{s}
\end{aligned}
$$ $$
\begin{aligned}
\Delta t &= \dfrac{12{,}9\,\text{s} - 12{,}2\,\text{s}}{2} \\
&= \dfrac{0{,}7\,\text{s}}{2} \\
&= 0{,}35\,\text{s}
\end{aligned}
$$
**Vastaus:** $t = (12{,}56 \pm 0{,}35)\,\text{s}$. Epävarmuuteen jätetään kaksi numeroa, koska sitä käytetään jatkolaskuissa; lopullinen tulos pyöristetään vasta lopuksi.
**Järkevyys:** Hajonta on noin $2{,}8\,\%$ keskiarvosta, mikä on tavallista käsin painetulle sekuntikellolle. Väli $12{,}56 \pm 0{,}35\,\text{s}$ ulottuu likimain pisteiden ääriarvoihin $12{,}2\,\text{s}$ ja $12{,}9\,\text{s}$.

### b)
**Annettu:** $\bar{t} = 12{,}56\,\text{s}$ ja $\Delta t = 0{,}35\,\text{s}$ kymmenelle heilahdukselle
**Kysytty:** jaksonaika $T$ epävarmuuksineen ja perustelu, miksi mitataan kymmenen heilahdusta
**Periaate:** Jaksonaika on yhden heilahduksen kesto, joten se on kymmenen heilahduksen aika jaettuna luvulla $10$. Luku $10$ on tarkka, joten sekä aika että sen epävarmuus jaetaan sillä.
**Kaava:** $T = \dfrac{t}{10}$ ja $\Delta T = \dfrac{\Delta t}{10}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $$
\begin{aligned}
T &= \dfrac{t}{10} \\
&= \dfrac{12{,}56\,\text{s}}{10} \\
&= 1{,}256\,\text{s}
\end{aligned}
$$ $$
\begin{aligned}
\Delta T &= \dfrac{\Delta t}{10} \\
&= \dfrac{0{,}35\,\text{s}}{10} \\
&= 0{,}035\,\text{s}
\end{aligned}
$$ $$
\begin{aligned}
\dfrac{\Delta T}{T} &= \dfrac{0{,}035\,\text{s}}{1{,}256\,\text{s}} \\
&= 0{,}028 \\
&= 2{,}8\,\%
\end{aligned}
$$
**Vastaus:** $T = (1{,}26 \pm 0{,}04)\,\text{s}$; epävarmuus $0{,}035\,\text{s}$ pyöristyy yhteen numeroon arvoon $0{,}04\,\text{s}$ ja suhteellinen epävarmuus on $2{,}8\,\%$. Jatkolaskussa käytetään pyöristämättömiä arvoja $1{,}256\,\text{s}$ ja $0{,}035\,\text{s}$.
**Järkevyys:** Jaksonaika noin $1{,}3\,\text{s}$ sopii heilurille, jonka pituus on $40\,\text{cm}$. Epävarmuus $0{,}04\,\text{s}$ on murto-osa jaksonajasta.
**Mallivastaus:** Kellon käynnistämiseen ja pysäyttämiseen liittyvä epävarmuus on noin $0{,}35\,\text{s}$ riippumatta siitä, kuinka pitkää aikaa mitataan. Jos mitattaisiin yksi heilahdus, suhteellinen epävarmuus olisi $$
\begin{aligned}
\dfrac{\Delta t}{T} &= \dfrac{0{,}35\,\text{s}}{1{,}256\,\text{s}} \\
&= 0{,}28 \\
&= 28\,\%
\end{aligned}
$$ Kymmenen heilahduksen ajasta se on vain $2{,}8\,\%$, koska sama $0{,}35\,\text{s}$ jakautuu kymmenelle jaksolle. Oletuksena on, että painamisen virhe ei kasva heilahduksia laskettaessa; heilahdukset on kuitenkin laskettava oikein.

### c)
**Annettu:** $T = 1{,}256\,\text{s}$ ja $\Delta T = 0{,}035\,\text{s}$ b-kohdasta; $l = 40{,}0\,\text{cm}$ ja $\Delta l = 0{,}2\,\text{cm}$; pienellä kulmalla $T = 2\pi\sqrt{l/g}$
**Kysytty:** putoamiskiihtyvyys $g$ epävarmuuksineen
**Periaate:** Pienen kulman heilurille $T = 2\pi\sqrt{l/g}$ (luku *Jousivärähtelijä ja heiluri*). Yhtälö korotetaan toiseen potenssiin ja ratkaistaan $g$ ennen lukujen sijoittamista. Koska $g \propto l\,T^{-2}$, suhteelliset epävarmuudet lasketaan yhteen ja jaksonajan osuus kerrotaan potenssilla $2$.
**Kaava:** $T^2 = \dfrac{4\pi^2 l}{g}$, joten $g = \dfrac{4\pi^2 l}{T^2}$ ja $\dfrac{\Delta g}{g} = \dfrac{\Delta l}{l} + 2\,\dfrac{\Delta T}{T}$
**Muunnokset:** $l = 40{,}0\,\text{cm} = 0{,}400\,\text{m}$ ja $\Delta l = 0{,}2\,\text{cm} = 0{,}002\,\text{m}$.
**Sijoitus:** $$
\begin{aligned}
g &= \dfrac{4\pi^2 l}{T^2} \\
&= \dfrac{4\pi^2 \cdot 0{,}400\,\text{m}}{(1{,}256\,\text{s})^2} \\
&= \dfrac{15{,}79\,\text{m}}{1{,}578\,\text{s}^2} \\
&= 10{,}01\,\text{m/s}^2
\end{aligned}
$$ Suhteelliset epävarmuudet: $$
\begin{aligned}
2\,\dfrac{\Delta T}{T} &= 2 \cdot \dfrac{0{,}035\,\text{s}}{1{,}256\,\text{s}} \\
&= 0{,}0557
\end{aligned}
$$ $$
\begin{aligned}
\dfrac{\Delta l}{l} &= \dfrac{0{,}002\,\text{m}}{0{,}400\,\text{m}} \\
&= 0{,}0050
\end{aligned}
$$ Yhteensä: $$
\begin{aligned}
\dfrac{\Delta g}{g} &= 0{,}0557 + 0{,}0050 \\
&= 0{,}0607 \\
&\approx 6{,}1\,\%
\end{aligned}
$$ Epävarmuus: $$
\begin{aligned}
\Delta g &= 0{,}0607 \cdot 10{,}01\,\text{m/s}^2 \\
&= 0{,}61\,\text{m/s}^2
\end{aligned}
$$
**Vastaus:** $g = (10{,}0 \pm 0{,}6)\,\text{m/s}^2$. Epävarmuus on yhdellä numerolla ja tulos pyöristetty samaan desimaaliin. Epävarmuudesta lähes kaikki ($5{,}6\,\%$ / $6{,}1\,\%$) tulee jaksonajasta.
**Järkevyys:** Tulos on lähellä tunnettua arvoa $9{,}81\,\text{m/s}^2$ (ero noin $2\,\%$). Käänteinen tarkistus: arvolla $9{,}81\,\text{m/s}^2$ jaksonaika olisi $T = 2\pi\sqrt{0{,}400/9{,}81}\,\text{s} = 1{,}27\,\text{s}$, joka on lähellä mitattua $1{,}26\,\text{s}$.

### d)
**Kysytty:** sopiiko tulos arvoon $9{,}81\,\text{m/s}^2$, miksi kulman pitää olla pieni ja yksi parannus
**Periaate:** Tulokset sopivat yhteen, jos vertailuarvo on tuloksen epävarmuusvälin sisällä. Kaava $T = 2\pi\sqrt{l/g}$ on johdettu pienen kulman likiarvolla (luku *Jousivärähtelijä ja heiluri*).
**Mallivastaus:** Tuloksen väli on $$
\begin{aligned}
g_\text{min} &= 10{,}01\,\text{m/s}^2 \\
&\quad - 0{,}61\,\text{m/s}^2 \\
&= 9{,}40\,\text{m/s}^2 \\
g_\text{max} &= 10{,}01\,\text{m/s}^2 \\
&\quad + 0{,}61\,\text{m/s}^2 \\
&= 10{,}62\,\text{m/s}^2
\end{aligned}
$$ eli $9{,}4 \ldots 10{,}6\,\text{m/s}^2$. Arvo $9{,}81\,\text{m/s}^2$ on välin sisällä, ja ero on $$
\begin{aligned}
\text{ero} &= 10{,}01\,\text{m/s}^2 \\
&\quad - 9{,}81\,\text{m/s}^2 \\
&= 0{,}20\,\text{m/s}^2
\end{aligned}
$$ eli paljon epävarmuutta $0{,}61\,\text{m/s}^2$ pienempi. Tulos sopii siis arvoon $9{,}81\,\text{m/s}^2$ mittauksen tarkkuuden rajoissa. Mittaus ei todista arvoa tarkasti, mutta mitään ristiriitaa ei ole. Kulman pitää olla pieni, koska johdossa oletetaan $\sin\theta \approx \theta$. Isolla kulmalla jaksonaika on pidempi: esimerkiksi amplitudilla $30^\circ$ noin $1{,}7\,\%$, ja koska $g \propto T^{-2}$, kaavasta laskettu $g$ olisi noin $3{,}4\,\%$ liian pieni. Lisäksi pituus on mitattava kiinnityskohdasta kuulan keskipisteeseen. Epävarmuudesta suurin osa tulee ajanotosta ($5{,}6\,\%$ vs $0{,}5\,\%$), joten parannus kannattaa kohdistaa siihen: mitataan esimerkiksi $30$ heilahduksen aika. Silloin $$
\begin{aligned}
t_{30} &= 30 \cdot 1{,}256\,\text{s} \\
&= 37{,}7\,\text{s} \\
\dfrac{\Delta t}{t_{30}} &= \dfrac{0{,}35\,\text{s}}{37{,}7\,\text{s}} \\
&= 0{,}0093
\end{aligned}
$$ ja $$
\begin{aligned}
\dfrac{\Delta g}{g} &= 2 \cdot 0{,}0093 + 0{,}0050 \\
&= 0{,}0236 \\
&\approx 2{,}4\,\%
\end{aligned}
$$ eli $\Delta g \approx 0{,}24\,\text{m/s}^2$. Valoportti, joka mittaa ajan ilman reaktioviivettä, parantaisi tulosta vielä enemmän. Tämän jälkeen pituuden epävarmuus ($0{,}5\,\%$) alkaisi näkyä tuloksessa.

### Yleisiä virheitä
- a-kohdassa epävarmuudeksi otetaan koko vaihteluväli $0{,}7\,\text{s}$ puolikkaan $0{,}35\,\text{s}$ sijaan, tai keskiarvo lasketaan vain kolmesta pisteestä.
- b-kohdassa jaetaan vain aika kymmenellä mutta epävarmuus jätetään $0{,}35\,\text{s}$:ksi, jolloin jaksonajan epävarmuus näyttää suuremmalta kuin se on.
- c-kohdassa unohdetaan jaksonajan neliö suhteellisessa epävarmuudessa ($2{,}8\,\%$ eikä $5{,}6\,\%$) tai pituus jätetään senttimetreiksi ($40{,}0$ eikä $0{,}400\,\text{m}$), jolloin $g$ on $100$-kertainen.
- d-kohdassa tulos $10{,}0$ todetaan "väärin", koska se ei ole $9{,}81$, vaikka ero on epävarmuutta pienempi.

### Hyväksytään myös
- a-kohdassa epävarmuutena voidaan käyttää myös keskihajontaa, kun se on laskettu ja nimetty; tulos on eri suuruinen kuin vaihteluvälin puolikas, ja jatkolaskut tehdään samalla tavalla.
- c-kohdassa epävarmuus voidaan laskea ääriarvoilla: $g_\text{max} = \dfrac{4\pi^2 \cdot 0{,}402\,\text{m}}{(1{,}221\,\text{s})^2} = 10{,}65\,\text{m/s}^2$ ja $g_\text{min} = \dfrac{4\pi^2 \cdot 0{,}398\,\text{m}}{(1{,}291\,\text{s})^2} = 9{,}43\,\text{m/s}^2$, joten $\Delta g \approx 0{,}6\,\text{m/s}^2$.
