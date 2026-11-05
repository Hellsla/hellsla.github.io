## fy9-mittaaminen-s1

### a)
**Annettu:** matka $s = 100{,}0\,\text{m}$; Liisan ajat $13{,}52\,\text{s}$, $13{,}90\,\text{s}$ ja $13{,}71\,\text{s}$
**Kysytty:** Liisan keskinopeus $v$ yksiköissä $\text{m/s}$ ja $\text{km/h}$
**Periaate:** Keskinopeus on kuljettu matka jaettuna ajalla, joka matkaan kului. Kolme kelloa mittaa saman juoksun. Siksi ajan paras arvio on kellojen keskiarvo. Keskiarvossa satunnaisvirheet kumoavat osittain toisensa eli poistavat toistensa vaikutusta.
**Kaava:** $\bar{t} = \dfrac{t_1 + t_2 + t_3}{3}$ ja $v = \dfrac{s}{\bar{t}}$
**Muunnokset:** $1\,\tfrac{\text{m}}{\text{s}} = \dfrac{0{,}001\,\text{km}}{\tfrac{1}{3600}\,\text{h}} = 3{,}6\,\tfrac{\text{km}}{\text{h}}$
**Sijoitus:** $\bar{t} = \dfrac{13{,}52\,\text{s} + 13{,}90\,\text{s} + 13{,}71\,\text{s}}{3} = 13{,}71\,\text{s}$ ja $v = \dfrac{100{,}0\,\text{m}}{13{,}71\,\text{s}} = 7{,}294\,\tfrac{\text{m}}{\text{s}} = 7{,}294 \cdot 3{,}6\,\tfrac{\text{km}}{\text{h}} = 26{,}26\,\tfrac{\text{km}}{\text{h}}$
**Vastaus:** $v \approx 7{,}29\,\text{m/s} \approx 26{,}3\,\text{km/h}$. Vastauksessa on kolme merkitsevää numeroa. Kellojen lukemat eroavat toisistaan kymmenesosasekunteja eli noin prosentin. Siksi myös nopeudessa vasta sadasosat metriä sekunnissa ovat epävarmoja. (b-kohdan epävarmuus $0{,}12\,\text{m/s}$ vahvistaa tämän.)
**Järkevyys:** Noin $26\,\text{km/h}$ on reipas sprinttivauhti lukiolaiselle. Se on selvästi vähemmän kuin huippujuoksijan noin $36\,\text{km/h}$. Se on selvästi enemmän kuin hölkän noin $10\,\text{km/h}$.

### b)
**Annettu:** $s = (100{,}0 \pm 0{,}3)\,\text{m}$; ajat $13{,}52\,\text{s}$, $13{,}90\,\text{s}$ ja $13{,}71\,\text{s}$; a-kohdasta $\bar{t} = 13{,}71\,\text{s}$
**Kysytty:** keskinopeuden epävarmuus $\Delta v$ ja nopeus epävarmuuksineen
**Periaate:** Ajan epävarmuutta arvioidaan kolmen kellon tulosten vaihteluvälin puolikkaana. Nopeus on suurin, kun matka on pisin ja aika lyhin mahdollinen. Nopeus on pienin, kun matka on lyhin ja aika pisin. Epävarmuudeksi otetaan näin saadun välin puolikas.
**Kaava:** $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$, $v_\text{max} = \dfrac{s + \Delta s}{\bar{t} - \Delta t}$, $v_\text{min} = \dfrac{s - \Delta s}{\bar{t} + \Delta t}$ ja $\Delta v = \dfrac{v_\text{max} - v_\text{min}}{2}$
**Muunnokset:** Ei tarvita. Matka on metreinä ja ajat sekunteina.
**Sijoitus:** $\Delta t = \dfrac{13{,}90\,\text{s} - 13{,}52\,\text{s}}{2} = 0{,}19\,\text{s}$, $v_\text{max} = \dfrac{100{,}3\,\text{m}}{13{,}52\,\text{s}} = 7{,}419\,\tfrac{\text{m}}{\text{s}}$, $v_\text{min} = \dfrac{99{,}7\,\text{m}}{13{,}90\,\text{s}} = 7{,}173\,\tfrac{\text{m}}{\text{s}}$ ja $\Delta v = \dfrac{7{,}419\,\tfrac{\text{m}}{\text{s}} - 7{,}173\,\tfrac{\text{m}}{\text{s}}}{2} = 0{,}123\,\tfrac{\text{m}}{\text{s}}$
**Vastaus:** $v = (7{,}29 \pm 0{,}12)\,\text{m/s}$. Epävarmuuden ensimmäinen numero on $1$. Siksi epävarmuudessa pidetään kaksi merkitsevää numeroa. Nopeus pyöristetään samaan desimaaliin.
**Järkevyys:** Ajan suhteellinen epävarmuus on $0{,}19 : 13{,}71 \approx 1{,}4\,\%$. Matkan suhteellinen epävarmuus on $0{,}3 : 100 = 0{,}3\,\%$. Ajan epävarmuus on siis paljon suurempi. Siksi nopeuden epävarmuus johtuu melkein kokonaan käsiajanotosta. Noin $0{,}2\,\text{s}$ on tavallinen epävarmuus, kun aika otetaan käsin.

### c)
**Kysytty:** voidaanko mittauksilla osoittaa, että Liisa oli nopeampi kuin Mira
**Periaate:** Kahden tuloksen ero on osoitettu vain silloin, kun niiden epävarmuusvälit eivät mene päällekkäin. Jos välit menevät päällekkäin, se ei todista, että tulokset ovat yhtä suuret.
**Mallivastaus:** Miran keskiarvo on $\bar{t} = (13{,}80 + 14{,}12 + 13{,}96)\,\text{s} : 3 = 13{,}96\,\text{s}$. Epävarmuus on $(14{,}12 - 13{,}80)\,\text{s} : 2 = 0{,}16\,\text{s}$. Miran aika on siis $(13{,}96 \pm 0{,}16)\,\text{s}$ ja Liisan $(13{,}71 \pm 0{,}19)\,\text{s}$. Liisan väli on $13{,}52$–$13{,}90\,\text{s}$ ja Miran $13{,}80$–$14{,}12\,\text{s}$. Välit menevät päällekkäin. Ero $0{,}25\,\text{s}$ on samaa suuruusluokkaa kuin epävarmuudet. Näillä mittauksilla ei siis voida osoittaa, että Liisa oli nopeampi, vaikka hänen keskiarvonsa on pienempi. Tämä ei kuitenkaan tarkoita, että juoksijat ovat yhtä nopeita. Eron osoittamiseen tarvittaisiin tarkempi ajanotto, esimerkiksi maalikamera.

### d)
**Kysytty:** ajanoton systemaattinen virhe, sen vaikutus nopeuteen ja miksi keskiarvo ei poista sitä
**Periaate:** Systemaattinen virhe siirtää jokaista tulosta samaan suuntaan. Sitä ei näe tulosten hajonnasta. Toistaminen tai keskiarvo ei poista sitä.
**Mallivastaus:** Ajanottaja käynnistää kellon vasta, kun hän on nähnyt lipun laskevan ja reagoinut siihen. Siksi kello käynnistyy myöhässä. Viive on reaktioaika, tavallisesti muutamia sekunnin kymmenyksiä. Maalissa ajanottaja taas näkee juoksijan tulevan. Siksi hän pysäyttää kellon melkein oikeaan aikaan. Mitattu aika on siis lyhyempi kuin todellinen aika, ja a-kohdan nopeus on suurempi kuin todellinen nopeus. Sama viive tapahtuu kaikilla kolmella ajanottajalla. Siksi kaikki kellot näyttävät liian lyhyttä aikaa, ja myös keskiarvo on liian pieni. Keskiarvo pienentää vain satunnaista vaihtelua kellojen välillä. Virheen poistaa esimerkiksi sähköinen ajanotto, joka käynnistyy itse lähtömerkistä.

### Hyväksytään myös
- b-kohdassa nopeuden suhteellinen epävarmuus ajan ja matkan suhteellisten epävarmuuksien summana: $\tfrac{0{,}19}{13{,}71} + \tfrac{0{,}3}{100{,}0} \approx 0{,}0169$. Silloin $\Delta v \approx 0{,}0169 \cdot 7{,}294\,\text{m/s} \approx 0{,}12\,\text{m/s}$.
- b-kohdassa ajan epävarmuutena käsiajanoton tavallinen $0{,}2\,\text{s}$, kun valinta perustellaan. Myös $\Delta v \approx 0{,}1\,\text{m/s}$ ja $v = (7{,}3 \pm 0{,}1)\,\text{m/s}$ hyväksytään.
- d-kohdassa maininta siitä, että ajanottaja voi reagoida lähtöpistoolin ääneen. Hän on $100\,\text{m}$:n päässä, joten hän käynnistäisi kellon vielä myöhemmin. Ääni kulkee tämän matkan noin $0{,}3\,\text{s}$:ssa.

### Yleisiä virheitä
- Ajaksi otetaan yhden kellon aika tai nopein aika eikä keskiarvoa.
- Nopeus muunnetaan väärin: kerrotaan, kun pitäisi jakaa, tai jaetaan, kun pitäisi kertoa. Esimerkiksi $7{,}29 : 3{,}6 = 2{,}0\,\text{km/h}$. Järkevyystarkastelu paljastaa virheen.
- Nopeus ilmoitetaan laskimen tarkkuudella $7{,}2939\,\text{m/s}$. Tai epävarmuus ja nopeus ilmoitetaan eri tarkkuudella.
- c-kohdassa päätellään keskiarvojen erosta, että Liisa oli nopeampi. Tai päätellään päällekkäisistä väleistä, että juoksijat olivat yhtä nopeita.
- d-kohdassa sanotaan, että reaktioaika aiheuttaa vain satunnaisvirheen. Reaktioajan keskimääräinen osa on kuitenkin systemaattinen virhe.

## fy9-mittaaminen-s2

### a)
**Annettu:** pinon korkeus $h = 51\,\text{mm}$, sen epävarmuus $\Delta h = 1\,\text{mm}$, arkkien määrä $N = 500$
**Kysytty:** yhden arkin paksuus $d$ ja sen epävarmuus $\Delta d$ mikrometreinä
**Periaate:** Arkit ovat samanlaisia, ja pino mitataan kerran. Siksi yhden arkin paksuus on pinon korkeus jaettuna arkkien määrällä. Myös korkeuden epävarmuus jaetaan samalla luvulla, koska se on yhden mittauksen epävarmuus.
**Kaava:** $d = \dfrac{h}{N}$ ja $\Delta d = \dfrac{\Delta h}{N}$
**Muunnokset:** $1\,\text{mm} = 1000\,\mu\text{m}$, joten $51\,\text{mm} = 51 \cdot 1000\,\mu\text{m} = 51\,000\,\mu\text{m}$ ja $1\,\text{mm} = 1000\,\mu\text{m}$.
**Sijoitus:** $d = \dfrac{51\,000\,\mu\text{m}}{500} = 102\,\mu\text{m}$ ja $\Delta d = \dfrac{1000\,\mu\text{m}}{500} = 2\,\mu\text{m}$
**Vastaus:** $d = (102 \pm 2)\,\mu\text{m}$. Epävarmuus on arvio, jossa on yksi merkitsevä numero. Paksuus pyöristetään samaan tarkkuuteen eli kokonaisiin mikrometreihin.
**Järkevyys:** Tavallinen kopiopaperi on noin kymmenesosamillimetrin paksuista. Arkki tuntuu ohuelta, mutta sen läpi ei näe. Suhteellinen epävarmuus on $2 : 102 \approx 2\,\%$. Se on sama kuin pinon korkeuden suhteellinen epävarmuus $1 : 51$.

### b)
**Annettu:** paperien massa $M = 2{,}49\,\text{kg}$, $N = 500$ arkkia, arkin mitat $a = 210\,\text{mm}$ ja $b = 297\,\text{mm}$; merkintä $80\,\text{g/m}^2$
**Kysytty:** mitattu neliömassa $\sigma$ yksikössä $\text{g/m}^2$
**Periaate:** Neliömassa on massa jaettuna pinta-alalla. Kaikkien arkkien yhteinen pinta-ala on yhden arkin pinta-ala kerrottuna arkkien määrällä. Arkkien massa on punnittu massa.
**Kaava:** $A = N \cdot ab$ ja $\sigma = \dfrac{M}{A} = \dfrac{M}{N ab}$
**Muunnokset:** $a = 210\,\text{mm} = 210 \cdot 0{,}001\,\text{m} = 0{,}210\,\text{m}$, $b = 297 \cdot 0{,}001\,\text{m} = 0{,}297\,\text{m}$ ja $M = 2{,}49\,\text{kg} = 2{,}49 \cdot 1000\,\text{g} = 2490\,\text{g}$
**Sijoitus:** $A = 500 \cdot 0{,}210\,\text{m} \cdot 0{,}297\,\text{m} = 31{,}185\,\text{m}^2$ ja $\sigma = \dfrac{2490\,\text{g}}{31{,}185\,\text{m}^2} = 79{,}85\,\tfrac{\text{g}}{\text{m}^2}$
**Vastaus:** $\sigma \approx 79{,}8\,\text{g/m}^2$. Vastauksessa on kolme merkitsevää numeroa, kuten massassa $2{,}49\,\text{kg}$. Ero merkintään $80\,\text{g/m}^2$ on alle $0{,}3\,\%$. Siksi merkintä on oikein vaa'an tarkkuudella.
**Järkevyys:** Arviolta yksi A4-arkki on noin $\tfrac{1}{16}\,\text{m}^2$. Siksi $500$ arkkia on noin $31\,\text{m}^2$, ja $31\,\text{m}^2 \cdot 80\,\text{g/m}^2 \approx 2{,}5\,\text{kg}$. Tämä vastaa punnittua massaa.

### c)
**Annettu:** a-kohdasta $d = 102\,\mu\text{m}$, b-kohdasta $\sigma = 79{,}85\,\text{g/m}^2$; veden tiheys $1000\,\text{kg/m}^3$
**Kysytty:** paperin tiheys $\rho$ yksikössä $\text{kg/m}^3$
**Periaate:** Tiheys on massa jaettuna tilavuudella. Ajatellaan paperia, jonka koko on yksi neliömetri. Sen massa on neliömassa, ja sen tilavuus on $1\,\text{m}^2 \cdot d$. Siksi tiheys saadaan, kun neliömassa jaetaan paksuudella.
**Kaava:** $\rho = \dfrac{m}{V} = \dfrac{\sigma \cdot 1\,\text{m}^2}{d \cdot 1\,\text{m}^2} = \dfrac{\sigma}{d}$
**Muunnokset:** $\sigma = 79{,}85\,\text{g/m}^2 = 79{,}85 \cdot 0{,}001\,\text{kg/m}^2 = 0{,}07985\,\text{kg/m}^2$ ja $d = 102\,\mu\text{m} = 102 \cdot 10^{-6}\,\text{m} = 1{,}02 \cdot 10^{-4}\,\text{m}$
**Sijoitus:** $\rho = \dfrac{0{,}07985\,\text{kg/m}^2}{1{,}02 \cdot 10^{-4}\,\text{m}} = 782{,}8\,\tfrac{\text{kg}}{\text{m}^3}$
**Vastaus:** $\rho \approx 780\,\text{kg/m}^3$ eli $7{,}8 \cdot 10^{2}\,\text{kg/m}^3$. Vastauksessa on kaksi merkitsevää numeroa, koska pinon korkeudessa $51\,\text{mm}$ on kaksi numeroa. Paperin tiheys on noin $0{,}78$ kertaa veden tiheys.
**Järkevyys:** Paperi on puukuitua, ja kuitujen välissä on ilmaa. Siksi paperin tiheys on samaa suuruusluokkaa kuin puun tiheys, muutamia satoja kilogrammoja kuutiometrissä. Suhteellinen epävarmuus on sama kuin paksuuden, noin $2\,\%$. Se on noin $\pm 20\,\text{kg/m}^3$.

### d)
**Kysytty:** onko järkevää mitata yksi arkki suoraan, ja miksi pinon korkeuden epävarmuus on suurempi kuin puolet asteikkovälistä
**Periaate:** Yksinkertaisessa tilanteessa lukeman epävarmuutta voi arvioida puoleksi pienimmästä asteikkovälistä. Mittauksen kokonaisepävarmuuteen vaikuttavat kuitenkin myös mittausmenetelmä ja muut virhelähteet. Suhteellinen epävarmuus kertoo, onko epävarmuus pieni verrattuna tulokseen.
**Mallivastaus:** Yksi arkki on noin $0{,}1\,\text{mm}$ paksu. Siksi viivain näyttäisi lukeman $0$ tai $1\,\text{mm}$. Lukeman epävarmuus $0{,}5\,\text{mm}$ olisi noin viisi kertaa niin suuri kuin itse paksuus. Suhteellinen epävarmuus olisi noin $500\,\%$. Mittauksesta ei siis saisi mitään tietoa. Kun mitataan pino, saman suuruinen lukeman epävarmuus jakautuu $500$ arkille. Silloin suhteellinen epävarmuus on vain noin $2\,\%$. Ehdotus on siis huono.

Pinon korkeuden epävarmuus on suurempi kuin $0{,}5\,\text{mm}$. Syy on se, että epävarmuutta ei aiheuta vain asteikon lukeminen. Pinon reunat ovat epätasaiset. Siksi korkeus riippuu siitä, mistä kohdasta mitataan. Lisäksi pino painuu kokoon, kun viivainta painetaan sitä vasten. Asteikkoväli kertoo vain viivaimen resoluution. Se ei kerro koko mittauksen epävarmuutta.

### Hyväksytään myös
- c-kohdassa koko pinon tiheys: $\rho = \tfrac{M}{N a b d} = \tfrac{2{,}49\,\text{kg}}{31{,}185\,\text{m}^2 \cdot 1{,}02 \cdot 10^{-4}\,\text{m}} \approx 783\,\text{kg/m}^3$. Hyväksytään myös pakkauksen merkinnällä $80\,\text{g/m}^2$ laskettu $\rho \approx 784\,\text{kg/m}^3$.
- a-kohdassa paksuus millimetreinä ja muunnos lopuksi: $d = 51\,\text{mm} : 500 = 0{,}102\,\text{mm} = 102\,\mu\text{m}$.

### Yleisiä virheitä
- Epävarmuutta ei jaeta arkkien määrällä. Silloin arkin paksuudeksi saadaan $(102 \pm 1000)\,\mu\text{m}$.
- Millimetrit muunnetaan mikrometreiksi väärään suuntaan: $51\,\text{mm} : 500 = 0{,}102\,\text{mm} = 0{,}000102\,\mu\text{m}$. Kun yksikkö on pienempi, lukuarvo kasvaa.
- Pinta-ala lasketaan millimetreinä, ja se muunnetaan neliömetreiksi kertoimella $1000$. Oikea kerroin on kuitenkin $1\,\text{m}^2 = 10^{6}\,\text{mm}^2$.
- Tiheydelle annetaan kolme tai neljä merkitsevää numeroa, vaikka pinon korkeus tunnetaan vain kahden numeron tarkkuudella.

## fy9-mittaaminen-s3

### a)
**Kysytty:** mittaustulosten kuvaaja
**Kuvaaja:** Opiskelija valitsee nesteen tilavuuden. Siksi tilavuus $V\ (\text{ml})$ tulee vaaka-akselille. Mitattu yhteinen massa $m\ (\text{g})$ tulee pystyakselille. Tässä pystyakseli alkaa $100\,\text{g}$:sta, ja se on merkitty. Vaaka-akseli alkaa nollasta, jotta suoraa voi myöhemmin jatkaa pystyakselille.

<svg data-fig="s3-pisteet" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: mittalasin ja nesteen yhteinen massa m grammoina nesteen tilavuuden V funktiona millilitroina. Vaaka-akseli on 0–110 ml ja pystyakseli 100–220 g. Pystyakselin alkukohta on merkitty. Kahdeksan sinistä pistettä on nousevassa jonossa tilavuuksilla 20–100 ml. Jokaisella pisteellä on vaakasuora epävarmuusjana ±1 ml. Rivin 60 ml piste (60 ml; 183,4 g) on piirretty onttona punaisena ympyränä. Se on selvästi muiden pisteiden yläpuolella, melkein samalla korkeudella kuin piste 70 ml." style="max-width:100%;font-size:30px">
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

**Mallivastaus:** Kummankin akselin asteikko on tasavälinen. Akselin päässä on suure ja yksikkö. Pisteet täyttävät suurimman osan kuvaajasta. Jokaisella pisteellä on vaakasuora epävarmuusjana $\pm 1\,\text{ml}$. Vaa'an resoluutio $0{,}1\,\text{g}$ on niin pieni, että pystysuoraa janaa ei näe. Pisteitä ei yhdistetä toisiinsa. Rivin $60\,\text{ml}$ piste erottuu heti. Se on melkein samalla korkeudella kuin rivin $70\,\text{ml}$ piste, vaikka massan pitäisi kasvaa tasaisesti.

### b)
**Kysytty:** sovitettu malli ja rivin $60\,\text{ml}$ käsittely
**Kuvaaja:** Seitsemän muun pisteen ja pisteen $20\,\text{ml}$ väliin sovitetaan yksi suora. Suoraa jatketaan katkoviivana pystyakselille. Harmaat katkoviivat ovat d-kohdan jyrkin ja loivin suora.

<svg data-fig="s3-sovitus" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: sama aineisto kuin edellä. Kahdeksan luotettavan pisteen väliin on sovitettu yksi suora. Suoraa on jatkettu katkoviivana pystyakselille asti. Se leikkaa akselin kohdassa noin 118,6 g. Se on tyhjän mittalasin massa. Suoralta on luettu kaksi pistettä, jotka ovat kaukana toisistaan: (20 ml; 137,0 g) ja (100 ml; 210,5 g). Ne on ympyröity, ja niistä saadaan kulmakerroin 0,919 g/ml. Harmaat katkoviivat ovat jyrkin ja loivin suora. Niiden kulmakertoimet ovat 0,932 ja 0,908 g/ml. Ontto piste 60 ml on noin 10 g:n päässä suorasta." style="max-width:100%;font-size:30px">
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

**Mallivastaus:** Pisteet ovat melkein suoralla. Siksi malliksi sopii suora $m = kV + b$. Suoraa ei pakoteta kulkemaan origon kautta, koska vaaka punnitsee myös mittalasin. Kun nestettä ei ole, massa ei ole nolla. Rivin $60\,\text{ml}$ piste on noin $10\,\text{g}$ suoran yläpuolella. Se on yli kymmenen kertaa niin paljon kuin muiden pisteiden poikkeamat. Pisteen massa $183{,}4\,\text{g}$ sopisi suoralle, jos tilavuus olisi noin $70\,\text{ml}$. Muistiinpanon mukaan lukema kirjattiin jälkikäteen muistista. Poikkeamalle on siis löytynyt todennäköinen syy: karkea virhe. Siksi piste jätetään pois sovituksesta. Poisjättö ja sen syy kirjoitetaan raporttiin. Pistettä ei olisi saanut poistaa vain siksi, että se on erilainen kuin muut. Paras ratkaisu olisi toistaa mittaus.

### c)
**Annettu:** b-kohdan sovitettu suora
**Kysytty:** suoran kulmakerroin $k$ ja vakiotermi $b$ yksiköineen sekä niiden merkitys
**Periaate:** Vaaka punnitsee mittalasin ja nesteen: $m = \rho V + m_0$. Mittalasin massa $m_0$ ei muutu, kun nestettä lisätään. Siksi massan muutos johtuu vain nesteestä. Kulmakerroin on siis nesteen tiheys, ja vakiotermi on tyhjän mittalasin massa.
**Kuvaajan lukeminen:** Suoralta luetaan kaksi pistettä, jotka ovat kaukana toisistaan: $(V_1;\ m_1) = (20\,\text{ml};\ 137{,}0\,\text{g})$ ja $(V_2;\ m_2) = (100\,\text{ml};\ 210{,}5\,\text{g})$.
**Kaava:** $k = \dfrac{m_2 - m_1}{V_2 - V_1}$ ja $b = m_1 - k V_1$
**Muunnokset:** $1\,\text{ml} = 1\,\text{cm}^3$, joten $1\,\tfrac{\text{g}}{\text{ml}} = 1\,\tfrac{\text{g}}{\text{cm}^3}$.
**Sijoitus:** $k = \dfrac{210{,}5\,\text{g} - 137{,}0\,\text{g}}{100\,\text{ml} - 20\,\text{ml}} = \dfrac{73{,}5\,\text{g}}{80\,\text{ml}} = 0{,}919\,\tfrac{\text{g}}{\text{ml}}$ ja $b = 137{,}0\,\text{g} - 0{,}919\,\tfrac{\text{g}}{\text{ml}} \cdot 20\,\text{ml} = 118{,}6\,\text{g}$
**Vastaus:** Kulmakerroin $k \approx 0{,}919\,\text{g/cm}^3$ on nesteen tiheys. Vakiotermi $b \approx 118{,}6\,\text{g}$ on tyhjän mittalasin massa. Kulmakertoimessa on kolme merkitsevää numeroa, koska massojen erotus $73{,}5\,\text{g}$ luetaan kolmen numeron tarkkuudella. d-kohdan epävarmuus näyttää, että kolmas numero on jo epävarma.
**Järkevyys:** Lasinen $100\,\text{ml}$:n mittalasi painaa tavallisesti noin $100$–$200\,\text{g}$. Tiheys on pienempi kuin veden mutta suurempi kuin etanolin. Suoran mukaan rivillä $20\,\text{ml}$ massa on $118{,}6\,\text{g} + 0{,}919\,\tfrac{\text{g}}{\text{ml}} \cdot 20\,\text{ml} = 137{,}0\,\text{g}$. Tämä vastaa mitattua massaa $137{,}6\,\text{g}$.

### d)
**Annettu:** b-kohdan kuvaaja, jossa pisteillä on epävarmuusjanat $\pm 1\,\text{ml}$; c-kohdasta $k = 0{,}919\,\text{g/cm}^3$; taulukon tiheydet $1{,}00$, $0{,}92$ ja $0{,}79\,\text{g/cm}^3$
**Kysytty:** tiheyden epävarmuus $\Delta\rho$ ja nesteen tunnistus
**Periaate:** Jyrkin ja loivin suora kulkevat vielä kaikkien epävarmuusjanojen kautta. Ne rajaavat kulmakertoimen arvioidun vaihteluvälin. Epävarmuudeksi otetaan tämän välin puolikas. Tulosta verrataan taulukon tiheyksiin.
**Kuvaajan lukeminen:** Jyrkimmän suoran kulmakerroin on noin $k_\text{max} = 0{,}932\,\text{g/cm}^3$ ja loivimman suoran $k_\text{min} = 0{,}908\,\text{g/cm}^3$.
**Kaava:** $\Delta\rho = \dfrac{k_\text{max} - k_\text{min}}{2}$
**Muunnokset:** Ei tarvita. Kaikki tiheydet ovat yksikössä $\text{g/cm}^3$.
**Sijoitus:** $\Delta\rho = \dfrac{0{,}932\,\text{g/cm}^3 - 0{,}908\,\text{g/cm}^3}{2} = 0{,}012\,\text{g/cm}^3$
**Vastaus:** $\rho = (0{,}919 \pm 0{,}012)\,\text{g/cm}^3$. Epävarmuuden ensimmäinen numero on $1$, joten siinä on kaksi numeroa. Tiheys pyöristetään samaan desimaaliin. Väli $0{,}907$–$0{,}931\,\text{g/cm}^3$ sisältää ruokaöljyn tiheyden $0{,}92\,\text{g/cm}^3$. Se ei sisällä veden tiheyttä $1{,}00$ eikä etanolin tiheyttä $0{,}79\,\text{g/cm}^3$. Neste on todennäköisesti ruokaöljyä. Päättely ei ole varma, koska jollakin muulla nesteellä voi olla sama tiheys.
**Järkevyys:** Suhteellinen epävarmuus on $0{,}012 : 0{,}919 \approx 1{,}3\,\%$. Tämä sopii siihen, että tilavuuden lukeman epävarmuus $1\,\text{ml}$ on noin $1\,\%$ mitatusta $80\,\text{ml}$:n välistä. Ero veteen on $0{,}08\,\text{g/cm}^3$. Se on monta kertaa niin suuri kuin epävarmuus.

### e)
**Annettu:** d-kohdasta $\rho = 0{,}919\,\text{g/cm}^3$; tilavuus $V = 1{,}50\,\text{l}$
**Kysytty:** nesteen massa $m$ ja onko tuloksen käyttö perusteltua
**Periaate:** Tiheys on aineen ominaisuus. Siksi saman nesteen massa on suoraan verrannollinen tilavuuteen: $m = \rho V$. Mittalasin massa ei kuulu nesteeseen, joten sitä ei lisätä.
**Kaava:** $m = \rho V$
**Muunnokset:** $V = 1{,}50\,\text{l} = 1{,}50 \cdot 1000\,\text{cm}^3 = 1500\,\text{cm}^3$, ja lopuksi $1000\,\text{g} = 1\,\text{kg}$.
**Sijoitus:** $m = 0{,}919\,\tfrac{\text{g}}{\text{cm}^3} \cdot 1500\,\text{cm}^3 = 1378\,\text{g} = 1{,}378\,\text{kg}$
**Vastaus:** $m \approx 1{,}38\,\text{kg}$. Vastauksessa on kolme merkitsevää numeroa, kuten tilavuudessa $1{,}50\,\text{l}$. d-kohdan epävarmuuden mukaan epävarmuus on noin $\pm 0{,}02\,\text{kg}$. Tilavuus on $15$ kertaa niin suuri kuin mitattu alue. Laskussa ei kuitenkaan jatketa mittalasin suoraa. Laskussa käytetään tiheyttä, joka on aineen ominaisuus. Tiheys pysyy samana samassa lämpötilassa. Siksi tulos on fysikaalisesti perusteltu, kunhan öljyn lämpötila on sama kuin mittauksessa.
**Järkevyys:** Sama tilavuus vettä painaisi $1{,}50\,\text{kg}$. Öljy on noin $8\,\%$ kevyempää. Siksi $1{,}38\,\text{kg}$ on oikean suuruinen.

### Hyväksytään myös
- c-kohdassa laskimen tai taulukkolaskennan suoran sovitus ilman riviä $60\,\text{ml}$: $k = 0{,}918\,\text{g/cm}^3$ ja $b = 118{,}6\,\text{g}$. Kulmakertoimet $0{,}90$–$0{,}94\,\text{g/cm}^3$ ja vakiotermit $117{,}5$–$119{,}5\,\text{g}$ hyväksytään.
- b-kohdassa rivin $60\,\text{ml}$ pitäminen mukana, kun sen vaikutus tarkistetaan. Kulmakerroin ei muutu, koska piste on mittausalueen keskellä. Vakiotermi kasvaa kuitenkin noin $1\,\text{g}$. Ratkaisu pitää perustella.
- d-kohdassa $\Delta\rho = 0{,}01$–$0{,}02\,\text{g/cm}^3$, joka on saatu silmällä piirretyistä ääriviivoista eli jyrkimmästä ja loivimmasta suorasta.

### Yleisiä virheitä
- Tiheys lasketaan jakamalla jonkin rivin massa tilavuudella, esimerkiksi $210{,}3\,\text{g} : 100\,\text{ml} = 2{,}10\,\text{g/cm}^3$. Massassa on kuitenkin mukana mittalasi.
- Suora pakotetaan kulkemaan origon kautta. Silloin kulmakerroin on liian suuri, ja neste tunnistetaan väärin.
- Rivin $60\,\text{ml}$ piste poistetaan kertomatta syytä. Tai pisteen takia pisteet yhdistetään murtoviivaksi.
- Kulmakerroin luetaan kahdesta vierekkäisestä mittauspisteestä.
- e-kohdassa massaan lisätään mittalasin massa. Tai mittalasin suoraa jatketaan $1500\,\text{ml}$:iin. Silloin tulokseen tulee ylimääräinen $119\,\text{g}$.

## fy9-mittaaminen-s4

### a)
**Kysytty:** virhelajit, jotka aineistossa näkyvät, ja niiden perustelut
**Periaate:** Systemaattinen virhe siirtää tuloksia samaan suuntaan. Satunnaisvirhe näkyy siinä, että toistojen tulokset vaihtelevat. Karkea virhe näkyy yhtenä tuloksena, joka on selvästi erilainen kuin muut.
**Mallivastaus:** *Systemaattinen virhe.* Jokainen lukema on suurempi kuin punnuksen tunnettu massa. Ero toistuu samanlaisena jokaisessa punnituksessa. Lukemien keskiarvot ovat noin $101{,}7$, $204{,}3$, $510{,}3$ ja $1020{,}3\,\text{g}$. Virhe on siis noin $2$, $4$, $10$ ja $20\,\text{g}$. Virhe kasvaa samassa suhteessa kuin massa, noin $2\,\%$: $20\,\text{g} : 1000\,\text{g} = 0{,}02$. Tyhjä vaaka näyttää $0\,\text{g}$. Siksi nollakohta on oikein, ja virhe on suhteellinen.

*Satunnaisvirhe.* Saman punnuksen kolme lukemaa eroavat toisistaan enintään $1\,\text{g}$. Vaihtelu on samaa suuruusluokkaa kuin näytön resoluutio $1\,\text{g}$.

*Karkea virhe.* Mikään lukema ei ole selvästi erilainen kuin saman punnuksen muut lukemat. Siksi karkeaa virhettä ei näy.

### b)
**Kysytty:** onko väite $(765 \pm 0{,}5)\,\text{g}$ oikein, ja parempi arvio jauhojen massasta
**Periaate:** Resoluutio on pienin muutos, joka näkyy näytössä. Se ei kerro systemaattisesta virheestä. Siksi epävarmuus voi olla paljon suurempi kuin resoluutio. Jos systemaattinen virhe tunnetaan, se korjataan.
**Mallivastaus:** Väite ei pidä paikkaansa. Puolikas resoluutiosta, $0{,}5\,\text{g}$, kertoo vain, kuinka tarkasti näytön voi lukea. a-kohdan mukaan vaaka näyttää noin $2\,\%$ liikaa, ja toistot vaihtelevat noin $1\,\text{g}$. Korjattu massa saadaan, kun lukema jaetaan suhteella, jonka punnukset antavat: $1020\,\text{g} : 1000\,\text{g} = 1{,}02$. Silloin $m \approx 765\,\text{g} : 1{,}02 = 750\,\text{g}$. Epävarmuutta lisää toistojen vaihtelu. Lisäksi korjauskerroin tunnetaan vain noin tuhannesosan tarkkuudella. Se tekee lukemassa $765\,\text{g}$ alle gramman. Parempi arvio on noin $(750 \pm 2)\,\text{g}$. Ystävän tulos on siis noin $15\,\text{g}$ liian suuri, ja sen epävarmuus on liian pieni.

### c)
**Kysytty:** kuvaajan muoto, mitä siitä näkee virheestä ja miksi toistaminen ei auta
**Periaate:** Jos vaaka olisi oikea, lukema olisi sama kuin punnuksen massa. Silloin pisteet olisivat suoralla, jonka kulmakerroin on $1$ ja vakiotermi $0$. Nollakohdan virhe näkyisi vakiotermissä. Suhteellinen virhe näkyisi kulmakertoimessa.
**Mallivastaus:** Pisteet ovat suoralla, joka kulkee origon kautta. Kulmakerroin on $(1020{,}3\,\text{g} - 101{,}7\,\text{g}) : (1000{,}0\,\text{g} - 100{,}0\,\text{g}) \approx 1{,}02$ eikä $1$. Vakiotermi on nolla. Kun vakiotermi on nolla, nollakohta on oikein. Kulmakerroin $1{,}02$ kertoo, että vaaka näyttää jokaisesta massasta $2\,\%$ liikaa. Pisteet ovat hyvin tarkasti suoralla, koska satunnainen vaihtelu, noin $1\,\text{g}$, on pieni.

Toistaminen pienentää satunnaisvirheen vaikutusta keskiarvossa. Syy: liian suuret ja liian pienet lukemat kumoavat osittain toisensa. Systemaattinen virhe on kuitenkin sama jokaisessa punnituksessa. Siksi keskiarvo on yhtä paljon väärin kuin yksi lukema. Virhe korjataan niin, että lukemat jaetaan kulmakertoimella $1{,}02$. Toinen tapa on kalibroida vaaka punnuksen avulla.

### Yleisiä virheitä
- Kaikkia poikkeamia pidetään satunnaisina, koska ne ovat pieniä. Ne ovat kuitenkin kaikki samaan suuntaan.
- Virhettä pidetään vakiona $2\,\text{g}$:na, ja korjauksessa lukemasta vähennetään $2\,\text{g}$. Virhe on kuitenkin suhteellinen.
- Näytön resoluutiota pidetään mittauksen epävarmuutena.
- Korjaus tehdään väärään suuntaan: $765\,\text{g} \cdot 1{,}02 = 780\,\text{g}$.

## fy9-mittaaminen-s5

### a)
**Kysytty:** raportin puutteet ja miksi kukin heikentää tulosta
**Periaate:** Mittauspisteisiin sovitetaan malli. Mallin valinta perustellaan fysiikalla. Kulmakerroin luetaan sovitetulta suoralta. Jos piste on erilainen kuin muut, se tarkistetaan ennen kuin se jätetään pois. Tulos ilmoitetaan epävarmuuksineen.
**Mallivastaus:**
- *Murtoviiva.* Viiva, joka yhdistää pisteet, seuraa myös mittausvirheitä. Se ei ole malli. Tasaisessa liikkeessä paikka muuttuu tasaisesti. Siksi pisteisiin sovitetaan yksi suora.
- *Nopeus kahdesta vierekkäisestä pisteestä.* Kummankin pisteen merkitsemisvirhe vaikuttaa tulokseen kokonaan. Jos kumpikin paikka voi olla $0{,}03\,\text{m}$ väärin, nopeus voi olla $0{,}12\,\text{m/s}$ väärin. Siksi tulos $0{,}42\,\text{m/s}$ on epävarma.
- *Suora origon kautta.* Ajanotto alkoi, kun auto oli jo liikkeessä noin $0{,}35\,\text{m}$:n kohdalla. Siksi paikka ei ole nolla hetkellä $t = 0$. Pakotettu suora on liian jyrkkä, ja kulmakerroin $0{,}63\,\text{m/s}$ on liian suuri.
- *Piste poistettiin ilman perustelua.* Piste poikkeaa noin $0{,}25\,\text{m}$, mikä on paljon. Syy olisi pitänyt tarkistaa videolta. Esimerkiksi auto on ehkä merkitty väärään kuvaan. Poisjättö ja sen syy olisi pitänyt kirjoittaa muistiin.
- *Tulos ja johtopäätös.* Tuloksessa on neljä merkitsevää numeroa eikä epävarmuutta. Lisäksi tulos valittiin sen mukaan, mikä tuntui sopivalta. Valinnan olisi pitänyt perustua menetelmään.

### b)
**Kysytty:** leluauton nopeus epävarmuuksineen ja pisteen $t = 1{,}5\,\text{s}$ käsittely
**Kuvaaja:** Vaaka-akselilla on aika $t\ (\text{s})$ ja pystyakselilla paikka $x\ (\text{m})$. Pisteisiin on merkitty epävarmuusjanat $\pm 0{,}03\,\text{m}$. Se on arvio siitä, kuinka tarkasti paikan voi merkitä videolta.

<svg data-fig="s5-kuvaaja" viewBox="0 0 600 410" role="img" aria-label="Kuvaaja: leluauton paikka x metreinä ajan t funktiona sekunteina, 0–3,0 s. Kuusi sinistä pistettä on lähellä yhtä nousevaa suoraa. Paikan epävarmuus ±0,03 m on pienempi kuin piste. Siksi epävarmuusjanat jäävät pisteiden sisään. Piste (1,5 s; 1,32 m) on piirretty onttona punaisena ympyränä. Se on noin 0,25 m suoran yläpuolella. Suora leikkaa pystyakselin kohdassa 0,36 m eikä origossa. Suoran kulmakerroin on 0,48 m/s. Suoralta luetut pisteet (0 s; 0,36 m) ja (3,0 s; 1,79 m) on ympyröity." style="max-width:100%;font-size:30px">
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

**Mallivastaus:** Kuusi pistettä on lähellä yhtä suoraa. Siksi auto liikkui tasaisesti. Piste $t = 1{,}5\,\text{s}$ on noin $0{,}25\,\text{m}$ suoran yläpuolella. Se on melkein samassa paikassa kuin piste $t = 2{,}0\,\text{s}$. Siksi se on todennäköisesti merkitty väärään kuvaan. Piste tarkistetaan videolta. Jos virhe löytyy, se korjataan. Toinen vaihtoehto on jättää piste pois ja kirjoittaa syy muistiin.

Suoraa ei pakoteta kulkemaan origon kautta. Suoralta luetaan kaksi pistettä, jotka ovat kaukana toisistaan: $(0\,\text{s};\ 0{,}36\,\text{m})$ ja $(3{,}0\,\text{s};\ 1{,}79\,\text{m})$. Nopeus on siis $v = \dfrac{1{,}79\,\text{m} - 0{,}36\,\text{m}}{3{,}0\,\text{s} - 0\,\text{s}} = 0{,}477\,\tfrac{\text{m}}{\text{s}}$. Vakiotermi $0{,}36\,\text{m}$ on auton paikka, kun ajanotto alkoi. Jyrkin ja loivin suora kulkevat kaikkien janojen kautta. Niiden kulmakertoimet ovat noin $0{,}492$ ja $0{,}464\,\text{m/s}$. Siksi $\Delta v = (0{,}492 - 0{,}464)\,\text{m/s} : 2 = 0{,}014\,\text{m/s}$.

Tulos on $v = (0{,}477 \pm 0{,}014)\,\text{m/s}$. Epävarmuudessa pidetään kaksi numeroa, koska sen ensimmäinen numero on $1$. Raportin kahden pisteen arvo $0{,}42\,\text{m/s}$ sopii yhteen tuloksen kanssa vain siksi, että sen epävarmuus on suuri. Origon kautta pakotetun suoran arvo $0{,}63\,\text{m/s}$ ei sovi yhteen tuloksen kanssa.

### c)
**Kysytty:** kaksi perusteltua parannusta, joista toinen koskee systemaattista virhettä
**Periaate:** Satunnaisvirheen vaikutusta pienennetään niin, että mittauksia lisätään ja mitattavaa väliä pidennetään. Systemaattinen virhe paljastuu vain, kun tulosta verrataan tunnettuun arvoon tai toiseen menetelmään.
**Mallivastaus:** *Mittakaavan tarkistus.* Mittanauha voi olla lähempänä kameraa kuin auto. Tai kamera voi kuvata vinosti. Silloin videon metri ei ole metri auton kulkulinjalla. Silloin kaikki paikat ja nopeus ovat väärin samassa suhteessa, eikä virhe näy pisteiden hajonnassa. Mittanauha asetetaan auton kulkulinjalle. Kamera asetetaan kohtisuoraan liikettä vastaan ja tarpeeksi kauas. Mittakaava tarkistetaan niin, että videolta mitataan jokin toinen tunnettu pituus.

*Lisää aineistoa ja pidempi matka.* Auto kuvataan pidemmältä matkalta, ja paikka merkitään tiheämmin, esimerkiksi $0{,}1\,\text{s}$:n välein. Silloin kulmakerroin määritetään useammasta pisteestä ja pidemmältä väliltä. Yhden pisteen merkitsemisvirhe vaikuttaa silloin vähemmän, ja jyrkimmän ja loivimman suoran ero pienenee. Kun ajo toistetaan, nähdään lisäksi, vaihteleeko auton nopeus ajosta toiseen.

### Hyväksytään myös
- b-kohdassa laskimen tai taulukkolaskennan suoran sovitus ilman pistettä $1{,}5\,\text{s}$: $v = 0{,}477\,\text{m/s}$ ja vakiotermi $0{,}358\,\text{m}$. Nopeudet $0{,}46$–$0{,}50\,\text{m/s}$ hyväksytään.
- b-kohdassa pisteen pitäminen mukana, kun sen vaikutus tarkistetaan. Piste on mittausalueen keskellä, joten kulmakerroin ei muutu. Pisteet eivät kuitenkaan enää ole suoralla epävarmuuksien rajoissa.
- b-kohdassa epävarmuus $\pm 0{,}02\,\text{m/s}$ ja tulos $(0{,}48 \pm 0{,}02)\,\text{m/s}$.

### Yleisiä virheitä
- Raportin puutteet nimetään, mutta ei perustella, miksi ne heikentävät tulosta.
- Poikkeavan pisteen poistamista pidetään aina virheenä tai aina oikeana. Tärkeää on, löytyykö poikkeamalle syy ja kirjoitetaanko se muistiin.
- b-kohdassa suora pakotetaan kulkemaan origon kautta. Tai nopeus lasketaan yhdestä pisteestä $x : t$.
- c-kohdassa ehdotetaan vain "tarkempaa mittaamista". Ei kerrota, mitä tehdään ja miksi se auttaa.

## fy9-mittaaminen-s6

### a)
**Kysytty:** onko paine kääntäen verrannollinen ruiskun lukemaan $V$
**Periaate:** Jos $p$ on kääntäen verrannollinen suureeseen $V$, tulo $pV$ on vakio. Väite testataan näin: tulo lasketaan eri riveillä. Sitten katsotaan, vaihteleeko tulo satunnaisesti vai muuttuuko se koko ajan samaan suuntaan.
**Mallivastaus:** Ensimmäisellä rivillä $pV = 189{,}1\,\text{kPa} \cdot 12\,\text{ml} = 2269\,\text{kPa} \cdot \text{ml}$. Viimeisellä rivillä $81{,}8\,\text{kPa} \cdot 30\,\text{ml} = 2454\,\text{kPa} \cdot \text{ml}$. Välirivien tulot kasvavat tasaisesti rivi riviltä. Koko kasvu on $(2454 - 2269) : 2269 \approx 8\,\%$. Paineet on annettu kymmenesosakilopascalin tarkkuudella, ja tulo kasvaa jokaisella rivillä samaan suuntaan. Satunnaisvirhe vaihtelisi sattumanvaraisesti. Siksi tasainen $8\,\%$:n kasvu ei johdu satunnaisvirheestä. Väite ei siis päde ruiskun lukemaan $V$. Tulon kasvu viittaa siihen, että ilman todellinen tilavuus on suurempi kuin lukema. Osa ilmasta on letkussa ja anturissa. Tämän ilman osuus on suurin, kun ruiskun tilavuus on pieni.

### b)
**Kysytty:** kuvaaja, jossa riippuvuus on suora, ja siihen sovitettu suora
**Kuvaaja:** Ilman todellinen tilavuus on $V + V_0$. Kun lämpötila ja ilman määrä pysyvät samoina, Boylen lain mukaan $p(V + V_0) = C$. Siitä saadaan $V = C \cdot \tfrac{1}{p} - V_0$. Siksi vaaka-akselille valitaan $\tfrac{1}{p}$ ja pystyakselille $V$. Esimerkiksi ensimmäisellä rivillä $\tfrac{1}{p} = \tfrac{1}{189{,}1\,\text{kPa}} = \tfrac{1}{0{,}1891\,\text{MPa}} = 5{,}29\,\tfrac{1}{\text{MPa}}$. Viimeisellä rivillä arvo on $12{,}2\,\tfrac{1}{\text{MPa}}$.

<svg data-fig="s6-kuvaaja" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: ruiskun asteikon tilavuus V millilitroina paineen käänteisluvun 1/p funktiona yksikössä 1/MPa. Kymmenen sinistä pistettä välillä 5,3–12,2 1/MPa ovat yhdellä nousevalla suoralla. Suoraa on jatkettu katkoviivana pystyakselille. Suora leikkaa pystyakselin negatiivisella puolella kohdassa −1,8 ml. Kulmakerroin on 2,60 MPa · ml. Vaaka-akseli on piirretty kohtaan V = 0." style="max-width:100%;font-size:30px">
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

**Mallivastaus:** Pisteet ovat hyvin suoralla. Siksi malli $p(V + V_0) = C$ sopii aineistoon. Suora ei kulje origon kautta. Suoraa jatketaan pystyakselille, ja se leikkaa akselin negatiivisella puolella. Jos letkussa ei olisi ilmaa, suora kulkisi origon kautta. Yksikkö $\tfrac{1}{\text{MPa}}$ on valittu, jotta akselin luvut on helppo lukea.

### c)
**Annettu:** b-kohdan suora; $T = 22\,{}^\circ\text{C}$; $R = 8{,}314\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}}$
**Kysytty:** letkun ja anturin ilmatilavuus $V_0$ ja ilman ainemäärä $n$
**Periaate:** Suoran yhtälö on $V = C \cdot \tfrac{1}{p} - V_0$. Siksi vakiotermi on $-V_0$ ja kulmakerroin $C = p(V + V_0)$. Ideaalikaasun tilanyhtälön mukaan $p(V + V_0) = nRT$. Siksi ainemäärä saadaan kulmakertoimesta. Tilanyhtälössä lämpötila on kelvineinä.
**Kuvaajan lukeminen:** Suora leikkaa pystyakselin kohdassa $-1{,}8\,\text{ml}$. Suoralta luetaan kaksi pistettä, jotka ovat kaukana toisistaan: $(4{,}0\,\tfrac{1}{\text{MPa}};\ 8{,}6\,\text{ml})$ ja $(12{,}0\,\tfrac{1}{\text{MPa}};\ 29{,}5\,\text{ml})$.
**Kaava:** $V_0 = -b$, $C = \dfrac{\Delta V}{\Delta (1/p)}$ ja $C = nRT$, joten $n = \dfrac{C}{RT}$
**Muunnokset:** $1\,\text{MPa} \cdot \text{ml} = 10^{6}\,\text{Pa} \cdot 10^{-6}\,\text{m}^3 = 1\,\text{Pa} \cdot \text{m}^3 = 1\,\text{J}$ ja $T = (22 + 273{,}15)\,\text{K} = 295{,}15\,\text{K}$
**Sijoitus:** $V_0 = 1{,}8\,\text{ml}$, $C = \dfrac{29{,}5\,\text{ml} - 8{,}6\,\text{ml}}{12{,}0\,\tfrac{1}{\text{MPa}} - 4{,}0\,\tfrac{1}{\text{MPa}}} = 2{,}61\,\text{MPa} \cdot \text{ml} = 2{,}61\,\text{J}$ ja $n = \dfrac{2{,}61\,\text{J}}{8{,}314\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}} \cdot 295{,}15\,\text{K}} = 1{,}06 \cdot 10^{-3}\,\text{mol}$
**Vastaus:** $V_0 \approx 1{,}8\,\text{ml}$ ja $n \approx 1{,}06 \cdot 10^{-3}\,\text{mol}$. Tilavuudessa on kaksi merkitsevää numeroa, koska se luetaan kuvaajasta noin $0{,}1\,\text{ml}$:n tarkkuudella. Ainemäärässä on kolme numeroa, kuten kulmakertoimessa.
**Järkevyys:** Normaalipaineessa ja huoneenlämmössä mooli kaasua vie tilaa noin $24\,\text{l}$. Siksi noin $26\,\text{ml}$ ilmaa on noin $26\,\text{ml} : 24\,000\,\text{ml/mol} \approx 1{,}1 \cdot 10^{-3}\,\text{mol}$. Letkussa ja anturissa on muutaman millilitran ilmatila. Se on uskottava lyhyelle letkulle. Kun $V_0$ lisätään, tulo $p(V + V_0)$ on ensimmäisellä rivillä $189{,}1\,\text{kPa} \cdot 13{,}8\,\text{ml} = 2610\,\text{kPa} \cdot \text{ml}$ ja viimeisellä $81{,}8\,\text{kPa} \cdot 31{,}8\,\text{ml} = 2601\,\text{kPa} \cdot \text{ml}$. Tulo on siis melkein vakio.

### d)
**Kysytty:** tuloksen oletukset ja niiden vaikutus
**Periaate:** Malli $p(V + V_0) = nRT$ olettaa kolme asiaa. Ilman määrä pysyy samana, lämpötila pysyy samana, ja koko tilavuus on mitattu. Jokaisen oletuksen kohdalla mietitään, mihin suuntaan tulos muuttuisi, jos oletus ei pitäisi paikkaansa.
**Mallivastaus:** *Lämpötila pysyy samana.* Puristaminen on työtä, joka kasvattaa ilman sisäenergiaa. Kun mäntää painetaan hitaasti, ilma ehtii luovuttaa lämmön ruiskun seinien kautta. Silloin ilma pysyy huoneen lämpöisenä. Nopeassa puristuksessa ilma lämpenisi. Paine olisi hetken suurempi kuin malli antaa, ja tulo $p(V + V_0)$ kasvaisi puristuksen aikana.

*Ilmaa ei vuoda.* Suuressa paineessa ilmaa voisi vuotaa männän ohi. Silloin ainemäärä pienenisi kesken mittauksen, ja tulo $p(V + V_0)$ pienenisi pienillä tilavuuksilla.

*Koko tilavuus on mukana.* Ilman $V_0$:aa tulo $pV$ näyttäisi kasvavan, kun tilavuus kasvaa. Silloin aineistosta voisi päätellä väärin, että Boylen laki ei päde. Myös ainemäärä laskettaisiin väärästä tilavuudesta.

*Johtopäätös.* Kun $V_0 = 1{,}8\,\text{ml}$ lisätään lukemaan, $p(V + V_0)$ on koko mittausalueella noin $2600\,\text{kPa} \cdot \text{ml}$. Vaihtelu on alle puoli prosenttia. Aineisto sopii siis yhteen mallin kanssa. Tämä tukee sitä, että oletukset pitivät paikkansa.

### Hyväksytään myös
- b-kohdassa $(\tfrac{1}{p}, V)$-kuvaaja yksikössä $\tfrac{1}{\text{kPa}}$. Silloin kulmakerroin on $2600\,\text{kPa} \cdot \text{ml} = 2{,}60\,\text{J}$.
- b- ja c-kohdassa laskimen tai taulukkolaskennan sovitus: $C = 2{,}603\,\text{J}$ ja $V_0 = 1{,}77\,\text{ml}$. Arvot $V_0 = 1{,}5$–$2{,}1\,\text{ml}$ ja $n = (1{,}01$–$1{,}11) \cdot 10^{-3}\,\text{mol}$ hyväksytään.
- c-kohdassa ainemäärä yhdeltä riviltä, kun $V_0$ on lisätty: $n = \tfrac{101{,}2\,\text{kPa} \cdot 25{,}8\,\text{ml}}{RT} \approx 1{,}06 \cdot 10^{-3}\,\text{mol}$.

### Yleisiä virheitä
- a-kohdassa todetaan, että $pV$ on "lähes vakio". Ei katsota, mihin suuntaan tulo muuttuu rivi riviltä. Silloin systemaattinen kasvu jää huomaamatta.
- b-kohdassa piirretään $(\tfrac{1}{V}, p)$-kuvaaja, ja suora pakotetaan kulkemaan origon kautta. Silloin letkun ilmatila ei näy.
- c-kohdassa lämpötila sijoitetaan celsiusasteina. Tai tilavuus sijoitetaan millilitroina ja paine kilopascaleina ilman muunnosta. Silloin ainemäärä on tuhat kertaa väärin.
- d-kohdassa luetellaan oletuksia, mutta ei kerrota, mihin suuntaan ne muuttaisivat tulosta.
