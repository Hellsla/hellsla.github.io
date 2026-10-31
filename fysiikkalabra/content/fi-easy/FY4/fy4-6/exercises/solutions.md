## fy4-6-L1-01
**Annettu:** $m = 160\,\text{kg}$, Kuun putoamiskiihtyvyys $g_\text{Kuu} = 1{,}62\,\text{m/s}^2$
**Kysytty:** paino Kuun pinnalla $G$ yksikössä $\text{N}$
**Periaate:** Paino on voima, jolla taivaankappale vetää kappaletta. Sen suuruus on massan ja putoamiskiihtyvyyden tulo. Massa on sama Kuussa kuin Maassa, mutta putoamiskiihtyvyys on Kuussa pienempi.
**Voimakuvio:** Astronautti on piirretty suorakulmiona Kuun pinnalle. Paino $\overline{G}$ lähtee keskipisteestä alas. Tukivoima $\overline{N}$ lähtee alapinnasta ylös, ja se on yhtä pitkä kuin paino. Kysytty on painon suuruus $mg_\text{Kuu}$.
```voimakuvio
pinta 0
G 259,2
N 259,2
a 0
```
**Kaava:** $G = m g_\text{Kuu}$
**Muunnokset:** Massa on kilogrammoina ja kiihtyvyys yksikössä $\text{m/s}^2$, joten muunnoksia ei tarvita.
**Sijoitus:** $G = 160\,\text{kg}\cdot 1{,}62\,\text{m/s}^2 = 259{,}2\,\text{N}$
**Vastaus:** $259\,\text{N}$. Vastauksessa on kolme merkitsevää numeroa kuten putoamiskiihtyvyydessä $1{,}62\,\text{m/s}^2$.
**Järkevyys:** Maassa paino olisi $160\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \approx 1570\,\text{N}$. Kuun putoamiskiihtyvyys on noin kuudesosa Maan arvosta. Niin ollen $1570\,\text{N} : 6 \approx 260\,\text{N}$, sama tulos.

## fy4-6-L1-02
**Annettu:** $m = 30\,\text{kg}$, $\mu = 0{,}12$, pulkka liukuu vaakasuoralla lumella; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liikekitka $F_\mu$ yksikössä $\text{N}$
**Periaate:** Pulkka liukuu, joten siihen vaikuttaa liikekitka $F_\mu = \mu N$. Pystysuunnassa pulkka ei kiihdy. Siksi Newtonin toisen lain mukaan tukivoima on yhtä suuri kuin paino.
**Voimakuvio:** Pulkka on piirretty suorakulmiona. Akseli $x$ osoittaa liikkeen suuntaan ja akseli $y$ ylös. Paino $\overline{G}$ lähtee keskipisteestä alas. Lumen tukivoima $\overline{N}$ lähtee alapinnasta ylös, ja se on yhtä pitkä kuin paino. Liikekitka $\overline{F}_\mu$ lähtee alapinnan takakulmasta taaksepäin. Eteenpäin vievää voimaa ei ole.
```voimakuvio
pinta 0
G 294,3
N 294,3
F_mu 35,32 vasen
v oikea
a vasen
akselit 0
```
**Kaava:** $y$: $N - mg = 0$, joten $N = mg$ ja $F_\mu = \mu N = \mu mg$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\mu = 0{,}12\cdot 30\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 35{,}316\,\text{N}$
**Vastaus:** $35\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa kuten kitkakertoimessa $0{,}12$ ja massassa $30\,\text{kg}$.
**Järkevyys:** Pulkan paino on noin $290\,\text{N}$. Kitka on siitä noin kahdeksasosa, kuten pieni kitkakerroin $0{,}12$ edellyttää. Kitka hidastaa pulkkaa: $a = F_\mu : m \approx 1{,}2\,\text{m/s}^2$.

## fy4-6-L1-03
**Annettu:** $m = 40\,\text{kg}$, vaakasuora työntövoima $F = 120\,\text{N}$, laatikko liukuu tasaisella nopeudella; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liikekitkakerroin $\mu$ (ei yksikköä)
**Periaate:** Tasaisessa liikkeessä voimien summa on nolla. Siksi liikekitka on yhtä suuri kuin työntö ja tukivoima yhtä suuri kuin paino. Liikekitka on $F_\mu = \mu N$.
**Voimakuvio:** Laatikko on piirretty suorakulmiona. Akseli $x$ osoittaa liikkeen suuntaan ja akseli $y$ ylös. Työntövoima $\overline{F}$ osoittaa eteenpäin. Liikekitka $\overline{F}_\mu$ osoittaa taaksepäin, ja se on yhtä pitkä kuin työntö. Paino $\overline{G}$ osoittaa alas ja tukivoima $\overline{N}$ ylös, ja ne ovat yhtä pitkät.
```voimakuvio
pinta 0
G 392,4
N 392,4
F 120 oikea työntö
F_mu 120 vasen
v oikea
a 0
akselit 0
```
**Kaava:** $x$: $F - \mu N = 0$ ja $y$: $N - mg = 0$, joten $\mu = \dfrac{F}{mg}$
**Muunnokset:** Massa on kilogrammoina ja voima newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $\mu = \dfrac{120\,\text{N}}{40\,\text{kg}\cdot 9{,}81\,\text{m/s}^2} = \dfrac{120\,\text{N}}{392{,}4\,\text{N}} = 0{,}3058$
**Vastaus:** $0{,}31$. Vastauksessa on kaksi merkitsevää numeroa kuten massassa $40\,\text{kg}$.
**Järkevyys:** Kitkakerroin on yksikötön, koska se on kahden voiman suhde. Työntö $120\,\text{N}$ on vajaa kolmannes laatikon painosta $392\,\text{N}$. Siksi kerroin on vähän yli $0{,}3$, mikä on tavallinen arvo puulle lattiaa vasten.

## fy4-6-L1-04
**Annettu:** $m = 0{,}80\,\text{kg}$, kannen kulma $\alpha = 20^\circ$, kirja on levossa; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** tukivoima $N$ yksikössä $\text{N}$
**Periaate:** Kirja ei liiku kantta vastaan kohtisuorassa suunnassa. Newtonin toisen lain mukaan voimien summa on siinä suunnassa nolla. Tukivoima kumoaa painon kohtisuoran komponentin.
**Voimakuvio:** Kirja on piirretty suorakulmiona kannen suuntaisesti. Akseli $x$ osoittaa kantta pitkin alas ja akseli $y$ kohtisuoraan kannesta ulos. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit $mg\sin\alpha$ ja $mg\cos\alpha$ on piirretty katkoviivoin. Tukivoima $\overline{N}$ osoittaa kohtisuoraan kannesta ulos ja lepokitka $\overline{F}_\mu$ kantta pitkin ylös.
```voimakuvio
pinta -20
G 7,848
N 7,375
F_mu 2,684 ylös
a 0
akselit -20
komponentit G
```
**Kaava:** $y$: $N - mg\cos\alpha = 0$, joten $N = mg\cos\alpha$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $N = 0{,}80\,\text{kg}\cdot 9{,}81\,\text{m/s}^2\cdot\cos 20^\circ = 7{,}848\,\text{N}\cdot 0{,}9397 = 7{,}375\,\text{N}$
**Vastaus:** $7{,}4\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa kuten massassa $0{,}80\,\text{kg}$.
**Järkevyys:** Kirjan paino on $7{,}8\,\text{N}$. Tukivoima on vähän pienempi, koska kansi on vinossa. Vaakasuoralla kannella tukivoima olisi koko paino ja pystysuoralla nolla.

## fy4-6-L1-05
**Annettu:** $m = 12\,\text{kg}$, rinteen kaltevuuskulma $\alpha = 30^\circ$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** painon rinteen suuntainen komponentti $G_x$ yksikössä $\text{N}$
**Voimakuvio:** Laatikko on piirretty suorakulmiona rinteen suuntaisesti. Akseli $x$ osoittaa rinnettä alas. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit $G_x$ ja $G_y$ on piirretty katkoviivoin. Muut voimat eivät vaikuta kysyttyyn komponenttiin.
```voimakuvio
pinta -30
G 117,7
N 101,9
F_mu 58,86 ylös
a 0
akselit -30
komponentit G
```
**Periaate:** Paino osoittaa suoraan alas. Valitaan $x$-akseli rinteen suuntaiseksi. Painon komponentti sen suuntaan saadaan suorakulmaisesta kolmiosta. Kolmiossa painon ja kohtisuoran komponentin välinen kulma on rinteen kaltevuuskulma $\alpha$.
**Kaava:** $G_x = G\sin\alpha = mg\sin\alpha$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $G_x = 12\,\text{kg}\cdot 9{,}81\,\text{m/s}^2\cdot\sin 30^\circ = 117{,}72\,\text{N}\cdot 0{,}5 = 58{,}86\,\text{N}$
**Vastaus:** $59\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa kuten massassa $12\,\text{kg}$.
**Järkevyys:** Kulmalla $30^\circ$ sini on tasan $0{,}5$. Siksi rinteen suuntainen komponentti on puolet painosta $118\,\text{N}$. Komponentti on aina pienempi kuin paino itse.

## fy4-6-L2-01
**Annettu:** $\alpha = 12^\circ$, pulkka lähtee levossa, $v = 3{,}0\,\text{m/s}$ ajassa $t = 4{,}0\,\text{s}$, kiihtyvyys vakio, ilmanvastus jätetään huomiotta; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liikekitkakerroin $\mu$ (ei yksikköä)
**Periaate:** Kiihtyvyys saadaan nopeuden muutoksesta. Newtonin toinen laki rinteen suuntaan antaa kitkan. Pulkka liukuu, joten siihen vaikuttaa liikekitka $F_\mu = \mu N$. Kohtisuorassa suunnassa pulkka ei kiihdy.
**Voimakuvio:** Pulkka on piirretty suorakulmiona rinteen suuntaisesti. Akseli $x$ osoittaa rinnettä alas ja akseli $y$ kohtisuoraan pinnasta ulos. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit on piirretty katkoviivoin. Tukivoima $\overline{N}$ osoittaa kohtisuoraan pinnasta ulos ja liikekitka $\overline{F}_\mu$ rinnettä ylös. Kiihtyvyys $\overline{a}$ piirretään erikseen oranssina nuolena rinnettä alas.
```voimakuvio
pinta -12
G 196,2
N 191,9
F_mu 25,79 ylös
a alas
akselit -12
komponentit G
```
**Kaava:** $a = \dfrac{v - 0}{t}$, $y$: $N - mg\cos\alpha = 0$ ja $x$: $mg\sin\alpha - \mu N = ma$, joten $\mu = \dfrac{g\sin\alpha - a}{g\cos\alpha}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita. Massa supistuu.
**Sijoitus:** $a = \dfrac{3{,}0\,\text{m/s}}{4{,}0\,\text{s}} = 0{,}75\,\text{m/s}^2$ ja $\mu = \dfrac{9{,}81\,\text{m/s}^2\cdot\sin 12^\circ - 0{,}75\,\text{m/s}^2}{9{,}81\,\text{m/s}^2\cdot\cos 12^\circ} = \dfrac{2{,}040 - 0{,}75}{9{,}596} = 0{,}134$
**Vastaus:** $0{,}13$. Vastauksessa on kaksi merkitsevää numeroa kuten nopeudessa $3{,}0\,\text{m/s}$ ja ajassa $4{,}0\,\text{s}$.
**Järkevyys:** Ilman kitkaa kiihtyvyys olisi $g\sin 12^\circ \approx 2{,}0\,\text{m/s}^2$. Kitka pienentää kiihtyvyyttä, kuten pitääkin. Kerroin $0{,}13$ on pienempi kuin $\tan 12^\circ = 0{,}21$, jolla pulkka liukuisi tasaisella nopeudella. Kerroin sopii muovipulkan ja lumen välille ($0{,}05$–$0{,}3$).

## fy4-6-L2-02
**Annettu:** $m = 40\,\text{kg}$, narun vaakasuora jännitysvoima $T = 150\,\text{N}$ (voima, jolla naru vetää lavaa), $\mu = 0{,}30$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Lava liukuu, joten siihen vaikuttaa liikekitka $\mu N$. Pystysuunnassa lava ei kiihdy, joten $N = mg$. Vaakasuunnassa jännitysvoiman ja kitkan erotus kiihdyttää lavaa Newtonin toisen lain mukaan.
**Voimakuvio:** Lava on piirretty suorakulmiona. Akseli $x$ osoittaa vedon suuntaan ja akseli $y$ ylös. Narun jännitysvoima $\overline{T}$ osoittaa eteenpäin. Liikekitka $\overline{F}_\mu$ lähtee alapinnan takakulmasta taaksepäin, ja se on lyhyempi kuin jännitysvoima. Paino $\overline{G}$ osoittaa alas ja tukivoima $\overline{N}$ ylös, ja ne ovat yhtä pitkät.
```voimakuvio
pinta 0
G 392,4
N 392,4
T 150 oikea
F_mu 117,7 vasen
v oikea
a oikea
akselit 0
```
**Kaava:** $y$: $N - mg = 0$ ja $x$: $T - \mu N = ma$, joten $a = \dfrac{T - \mu mg}{m}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{150\,\text{N} - 0{,}30\cdot 40\,\text{kg}\cdot 9{,}81\,\text{m/s}^2}{40\,\text{kg}} = \dfrac{150\,\text{N} - 117{,}72\,\text{N}}{40\,\text{kg}} = 0{,}807\,\text{m/s}^2$
**Vastaus:** $0{,}81\,\text{m/s}^2$. Vastauksessa on kaksi merkitsevää numeroa kuten kitkakertoimessa $0{,}30$ ja massassa $40\,\text{kg}$.
**Järkevyys:** Ilman kitkaa kiihtyvyys olisi $150\,\text{N} : 40\,\text{kg} \approx 3{,}8\,\text{m/s}^2$. Kitka $118\,\text{N}$ kumoaa suurimman osan narun voimasta. Siksi kiihtyvyys jää alle $1\,\text{m/s}^2$:n, mikä on järkevää.

## fy4-6-L2-03
**Annettu:** esimerkkiaineiston kuvaajan viisi mittauspistettä $(N, F_\mu)$: $(5\,\text{N};\,1{,}1\,\text{N})$, $(10\,\text{N};\,2{,}1\,\text{N})$, $(15\,\text{N};\,3{,}3\,\text{N})$, $(20\,\text{N};\,4{,}2\,\text{N})$ ja $(25\,\text{N};\,5{,}4\,\text{N})$
**Kysytty:** liikekitkakerroin $\mu$ (ei yksikköä)
**Periaate:** Liikekitka on verrannollinen tukivoimaan, $F_\mu = \mu N$. Siksi $(N, F_\mu)$-kuvaaja on suora, joka kulkee origon kautta, ja suoran kulmakerroin on $\mu$. Kulmakerroin luetaan pisteisiin sovitetulta suoralta, ei kahdesta vierekkäisestä mittauspisteestä. Mittauspisteet eivät yleensä ole täsmälleen samalla suoralla, koska mittauksissa on aina epävarmuutta.
**Kuvaajan lukeminen:** Piirretään suora origon kautta niin, että se kulkee mahdollisimman läheltä kaikkia pisteitä. Luetaan suoralta kaukainen piste. Esimerkiksi tukivoimalla $N = 25\,\text{N}$ suoran arvo on noin $F_\mu = 5{,}35\,\text{N}$.
**Kaava:** $\mu = \dfrac{\Delta F_\mu}{\Delta N}$, kun $\Delta F_\mu$ ja $\Delta N$ luetaan sovitetulta suoralta
**Muunnokset:** Molemmat akselit ovat newtoneina, joten yksiköt supistuvat eikä muunnoksia tarvita.
**Sijoitus:** $\mu = \dfrac{5{,}35\,\text{N} - 0\,\text{N}}{25\,\text{N} - 0\,\text{N}} = 0{,}214$
**Vastaus:** $0{,}21$. Vastauksessa on kaksi merkitsevää numeroa, koska kitkavoimat on mitattu kahden numeron tarkkuudella ja suora piirretään käsin.
**Järkevyys:** Yksittäisistä pisteistä saadaan suhteet $0{,}21$–$0{,}22$, esimerkiksi $4{,}2\,\text{N} : 20\,\text{N} = 0{,}21$. Sovitetun suoran kulmakerroin osuu niiden väliin. Kerroin on yksikötön, kuten kahden voiman suhteen pitää olla.

## fy4-6-L2-04
**Annettu:** $m = 10\,\text{kg}$, $\alpha = 35^\circ$, $\mu_0 = 0{,}60$, laatikko asetetaan levossa; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** erotus $G_x - F_\text{max}$ yksikössä $\text{N}$, missä $F_\text{max}$ on lepokitkan suurin arvo. Erotuksen etumerkki kertoo, pysyykö laatikko paikallaan
**Periaate:** Lepokitka on enintään $\mu_0 N$. Laatikko pysyy paikallaan vain, jos tämä yläraja riittää kumoamaan painon rinteen suuntaisen komponentin. Kohtisuorassa suunnassa laatikko ei kiihdy, joten $N = mg\cos\alpha$.
**Voimakuvio:** Laatikko on piirretty suorakulmiona rinteen suuntaisesti. Akseli $x$ osoittaa rinnettä alas ja akseli $y$ kohtisuoraan pinnasta ulos. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit $mg\sin\alpha$ ja $mg\cos\alpha$ on piirretty katkoviivoin. Tukivoima $\overline{N}$ osoittaa kohtisuoraan pinnasta ulos ja kitka $\overline{F}_\mu$ rinnettä ylös.
```voimakuvio
pinta -35
G 98,1
N 80,36
F_mu 48,22 ylös
a alas
akselit -35
komponentit G
```
**Kaava:** $y$: $N - mg\cos\alpha = 0$, joten suurin lepokitka on $F_\text{max} = \mu_0 mg\cos\alpha$, ja sitä verrataan komponenttiin $G_x = mg\sin\alpha$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\text{max} = 0{,}60\cdot 10\,\text{kg}\cdot 9{,}81\,\text{m/s}^2\cdot\cos 35^\circ = 48{,}2\,\text{N}$ ja $G_x = 10\,\text{kg}\cdot 9{,}81\,\text{m/s}^2\cdot\sin 35^\circ = 56{,}3\,\text{N}$, joten $G_x - F_\text{max} = 8{,}1\,\text{N}$
**Vastaus:** komponentti ylittää suurimman lepokitkan $56{,}3\,\text{N} - 48{,}2\,\text{N} = 8{,}1\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa kuten kitkakertoimessa $0{,}60$. Suurin lepokitka $48\,\text{N}$ on pienempi kuin komponentti $56\,\text{N}$. Siksi laatikko ei pysy paikallaan vaan lähtee liukumaan. Erotus on positiivinen, joten kitka ei riitä.
**Järkevyys:** Saman päätelmän antaa kulma. Arvo $\tan 35^\circ = 0{,}70$ on suurempi kuin $\mu_0 = 0{,}60$, joten lankku on jyrkempi kuin rajakulma $\tan^{-1} 0{,}60 \approx 31^\circ$.

## fy4-6-L3-01
**Annettu:** $m = 50\,\text{kg}$, auton ja laatikon kiihtyvyys $a = 3{,}5\,\text{m/s}^2$ eteenpäin, tie vaakasuora; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** lepokitkakertoimen pienin arvo $\mu_0$ (ei yksikköä)
**Periaate:** Jos laatikko ei liu'u, se kiihtyy auton mukana. Ainoa vaakasuora voima laatikkoon on lavan lepokitka. Newtonin toisen lain mukaan sen täytyy olla $ma$ ja osoittaa eteenpäin, liikkeen suuntaan. Lepokitka voi olla enintään $\mu_0 N$.
**Voimakuvio:** Laatikko on piirretty suorakulmiona. Akseli $x$ osoittaa eteenpäin ja akseli $y$ ylös. Paino $\overline{G}$ lähtee keskipisteestä alas. Lavan tukivoima $\overline{N}$ lähtee alapinnasta ylös, ja se on yhtä pitkä kuin paino. Lepokitka $\overline{F}_\mu$ lähtee alapinnan etukulmasta eteenpäin. Kiihtyvyys piirretään erikseen ohuena oranssina nuolena, koska se ei ole voima.
```voimakuvio
pinta 0
G 490,5
N 490,5
F_mu 175 oikea
a oikea
akselit 0
```
**Kaava:** $y$: $N - mg = 0$ ja $x$: $F_\mu = ma$. Ehto $F_\mu \le \mu_0 N$ antaa $ma \le \mu_0 mg$, joten $\mu_0 \ge \dfrac{a}{g}$
**Muunnokset:** Kiihtyvyydet ovat yksikössä $\text{m/s}^2$, joten muunnoksia ei tarvita. Massa supistuu.
**Sijoitus:** $\mu_0 = \dfrac{3{,}5\,\text{m/s}^2}{9{,}81\,\text{m/s}^2} = 0{,}357$
**Vastaus:** $0{,}36$. Vastauksessa on kaksi merkitsevää numeroa kuten kiihtyvyydessä $3{,}5\,\text{m/s}^2$.
**Järkevyys:** Kitka osoittaa liikkeen suuntaan, koska lava pyrkii liukumaan eteenpäin laatikon alta. Massa supistuu, joten tulos pätee sekä kevyelle että raskaalle laatikolle. Märällä vanerilla kerroin voi jäädä alle $0{,}36$. Silloin laatikko liukuu taaksepäin lavan suhteen. Siksi kuorma kiinnitetään.

## fy4-6-L3-02
**Annettu:** rinteen kulma $\alpha = 20^\circ$, alkunopeus $v_0 = 3{,}0\,\text{m/s}$ rinnettä ylös, $\mu = 0{,}25$, loppunopeus $v = 0$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liukumatka $s$ yksikössä $\text{m}$
**Periaate:** Kun kiekko liukuu ylös, sekä painon rinteen suuntainen komponentti että liikekitka osoittavat rinnettä alas. Siksi kiekko hidastuu tasaisesti. Kiihtyvyys saadaan Newtonin toisesta laista. Matka saadaan tasaisesti kiihtyvän liikkeen yhtälöstä $v^2 = v_0^2 - 2as$, kun $a$ on hidastuvuuden suuruus.
**Voimakuvio:** Kiekko on piirretty suorakulmiona rinteen suuntaisesti. Akseli $x$ osoittaa rinnettä alas ja akseli $y$ kohtisuoraan pinnasta ulos. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit on piirretty katkoviivoin. Tukivoima $\overline{N}$ osoittaa kohtisuoraan pinnasta ulos. Liikekitka $\overline{F}_\mu$ osoittaa rinnettä alas, koska kiekko liukuu ylös. Nopeus on rinnettä ylös, mutta se ei ole voima.
```voimakuvio
pinta -20
G 9,81
N 9,218
F_mu 2,305 alas
v 160
a alas
akselit -20
komponentit G
```
**Kaava:** $y$: $N = mg\cos\alpha$ ja $x$: $mg\sin\alpha + \mu mg\cos\alpha = ma$, joten $a = g(\sin\alpha + \mu\cos\alpha)$. Liikeyhtälöstä $v^2 = v_0^2 - 2as$ ja ehdosta $v = 0$ saadaan $s = \dfrac{v_0^2}{2a}$, missä $a = g(\sin\alpha + \mu\cos\alpha)$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $a = 9{,}81\,\text{m/s}^2\cdot(\sin 20^\circ + 0{,}25\cdot\cos 20^\circ) = 5{,}660\,\text{m/s}^2$ ja $s = \dfrac{(3{,}0\,\text{m/s})^2}{2\cdot 5{,}660\,\text{m/s}^2} = 0{,}795\,\text{m}$
**Vastaus:** $0{,}80\,\text{m}$. Vastauksessa on kaksi merkitsevää numeroa kuten nopeudessa $3{,}0\,\text{m/s}$ ja kitkakertoimessa $0{,}25$.
**Järkevyys:** Ilman kitkaa hidastuvuus olisi $g\sin 20^\circ \approx 3{,}4\,\text{m/s}^2$ ja matka noin $1{,}3\,\text{m}$. Kitka lyhentää matkaa. Pysähdyttyään kiekko jää rinteelle vain, jos lepokitkakerroin on vähintään $\tan 20^\circ \approx 0{,}36$. Muuten kiekko lähtee liukumaan takaisin alas.

## fy4-6-L3-03
**Annettu:** Maassa $\alpha = 30^\circ$ ja $a_\text{Maa} = 2{,}0\,\text{m/s}^2$ alas rinnettä, Kuussa sama rinne ja pinta, $g = 9{,}81\,\text{m/s}^2$ ja $g_\text{Kuu} = 1{,}62\,\text{m/s}^2$; ilmanvastusta ei ole
**Kysytty:** kiihtyvyys Kuussa $a_\text{Kuu}$ yksikössä $\text{m/s}^2$
**Periaate:** Laatikko liukuu, joten siihen vaikuttaa liikekitka $\mu N$ rinnettä ylös. Kitkakerrointa ei anneta. Kitkakerroin on pinnan ominaisuus, joten se on sama Maassa ja Kuussa. Maan kiihtyvyydestä saadaan $\mu$, ja Kuussa sama laki antaa uuden kiihtyvyyden. Kohtisuorassa suunnassa laatikko ei kiihdy.
**Voimakuvio:** Laatikko on piirretty suorakulmiona rinteen suuntaisesti. Akseli $x$ osoittaa rinnettä alas ja akseli $y$ kohtisuoraan pinnasta ulos. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit on piirretty katkoviivoin. Tukivoima $\overline{N}$ osoittaa kohtisuoraan pinnasta ulos ja liikekitka $\overline{F}_\mu$ rinnettä ylös.
```voimakuvio
pinta -30
G 98,1
N 84,96
F_mu 29,05 ylös
a alas
akselit -30
komponentit G
```
**Kaava:** $y$: $N - mg\cos\alpha = 0$ ja $x$: $mg\sin\alpha - \mu N = ma$, joten $a = g(\sin\alpha - \mu\cos\alpha)$ ja $\mu = \tan\alpha - \dfrac{a_\text{Maa}}{g\cos\alpha}$. Sulkulauseke on sama molemmissa paikoissa, joten $a_\text{Kuu} = a_\text{Maa}\cdot\dfrac{g_\text{Kuu}}{g}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita. Massa supistuu.
**Sijoitus:** $\mu = \tan 30^\circ - \dfrac{2{,}0\,\text{m/s}^2}{9{,}81\,\text{m/s}^2\cdot\cos 30^\circ} = 0{,}577 - 0{,}235 = 0{,}342$, ja $a_\text{Kuu} = 1{,}62\,\text{m/s}^2\cdot(\sin 30^\circ - 0{,}342\cdot\cos 30^\circ) = 0{,}330\,\text{m/s}^2$. Suoraan suhteesta: $2{,}0\,\text{m/s}^2\cdot\dfrac{1{,}62}{9{,}81} = 0{,}330\,\text{m/s}^2$
**Vastaus:** $0{,}33\,\text{m/s}^2$. Vastauksessa on kaksi merkitsevää numeroa kuten Maan kiihtyvyydessä $2{,}0\,\text{m/s}^2$.
**Järkevyys:** Sekä paino että kitka ovat Kuussa noin kuudesosan Maan arvosta. Siksi myös kiihtyvyys on noin kuudesosa. Laatikko liukuu Kuussakin, koska ehto $\tan\alpha > \mu$ ei riipu putoamiskiihtyvyydestä.
