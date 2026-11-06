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

## fy4-6-L1-06
**Kysytty:** lattian laatikkoon kohdistaman kitkavoiman suuruus, kun laatikko pysyy paikallaan
**Periaate:** Laatikko on levossa. Newtonin toisen lain mukaan vaakasuuntaisten voimien summa on silloin nolla. Lepokitka mukautuu tilanteeseen. Se on yhtä suuri kuin työntö ja vastakkaissuuntainen, kunhan työntö ei ylitä lepokitkan enimmäisarvoa.
**Mallivastaus:** Kitkavoiman suuruus on $20\,\text{N}$, koska laatikko on levossa ja kitka kumoaa työnnön. Enimmäisarvo $60\,\text{N}$ on vain yläraja, ja työntö $20\,\text{N}$ jää sen alle. Väite, että kitka olisi aina enimmäisarvon suuruinen, on väärä. Lepokitka on vain niin suuri kuin tilanne vaatii. Väite, että kitkaa ei olisi lainkaan, on väärä. Juuri kitka estää laatikkoa liikkumasta. Väite, että kitka olisi enimmäisarvon ja työnnön erotus, on väärä. Levossa kitka ja työntö ovat yhtä suuret.

## fy4-6-L1-07
**Annettu:** $m = 50\,\text{kg}$, $\mu_0 = 0{,}45$, laatikko on levossa vaakasuoralla lattialla; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** pienin vaakasuora voima $F$ yksikössä $\text{N}$, jolla laatikko lähtee liikkeelle
**Periaate:** Laatikko lähtee liikkeelle, kun työntö ylittää lepokitkan enimmäisarvon $\mu_0 N$. Rajatapauksessa työntö on yhtä suuri kuin tämä enimmäisarvo. Pystysuunnassa laatikko ei kiihdy, joten $N = mg$.
**Voimakuvio:** Laatikko on piirretty suorakulmiona. Akseli $x$ osoittaa työnnön suuntaan ja akseli $y$ ylös. Työntövoima $\overline{F}$ osoittaa eteenpäin. Lepokitka $\overline{F}_\mu$ osoittaa taaksepäin, ja rajatapauksessa se on yhtä pitkä kuin työntö. Paino $\overline{G}$ osoittaa alas ja tukivoima $\overline{N}$ ylös, ja ne ovat yhtä pitkät.
```voimakuvio
pinta 0
G 490,5
N 490,5
F 220,7 oikea työntö
F_mu 220,7 vasen
a 0
akselit 0
```
**Kaava:** $y$: $N - mg = 0$ ja $x$: $F - \mu_0 N = 0$, joten $F = \mu_0 mg$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $F = 0{,}45\cdot 50\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 220{,}7\,\text{N}$
**Vastaus:** $2{,}2\cdot 10^2\,\text{N}$ eli noin $220\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa kuten kitkakertoimessa $0{,}45$ ja massassa $50\,\text{kg}$. Tätä pienemmällä voimalla laatikko pysyy paikallaan.
**Järkevyys:** Laatikon paino on $490\,\text{N}$. Tarvittava voima on $0{,}45$-kertainen siihen nähden, kuten kitkakerroin edellyttää. Kun laatikko on lähtenyt liikkeelle, liikekitka on yleensä pienempi kuin $\mu_0 N$. Siksi liikkeessä pitämiseen riittää pienempi voima.

## fy4-6-L1-08
**Kysytty:** tukivoiman suuruuden $N$ suhde painon suuruuteen $G$ kaltevalla tasolla levossa olevalle kappaleelle
**Periaate:** Valitaan $y$-akseli kohtisuoraan pintaa vastaan. Siinä suunnassa kappale ei kiihdy, joten voimien summa on nolla. Pintaa vastaan kohtisuorassa vaikuttavat vain tukivoima ja painon komponentti $G_y = mg\cos\alpha$. Kitka on pinnan suuntainen. Paino osoittaa suoraan alas, ja se jaetaan kahteen komponenttiin: rinteen suuntaan ja sitä vastaan kohtisuoraan.
**Mallivastaus:** Tukivoima on painoa pienempi: $N = mg\cos\alpha < G$. Tukivoima kumoaa vain painon komponentin, joka on kohtisuorassa pintaa vastaan. Rinteen suuntaisen komponentin kumoaa kitka. Kulmalla $30^\circ$ saadaan $N = G\cos 30^\circ \approx 0{,}87\,G$. Väite, että tukivoima ja paino ovat aina vastakkaiset ja yhtä suuret, pätee vain vaakasuoralla pinnalla. Väite $N > G$ on väärä, koska kitka ei paina kappaletta pintaa vasten. Väite $N = 0$ on väärä, koska painon komponentti $G_y$ painaa kappaletta pintaa vasten.

## fy4-6-L2-05
**Annettu:** esimerkkiaineiston viisi mittausta $(m, F)$: $(0{,}20\,\text{kg};\,0{,}85\,\text{N})$, $(0{,}40\,\text{kg};\,1{,}62\,\text{N})$, $(0{,}60\,\text{kg};\,2{,}50\,\text{N})$, $(0{,}80\,\text{kg};\,3{,}31\,\text{N})$ ja $(1{,}00\,\text{kg};\,4{,}02\,\text{N})$; palikkaa vedetään vaakasuoraan tasaisella nopeudella; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liikekitkakerroin $\mu$ (ei yksikköä)
**Periaate:** Tasaisella nopeudella voimien summa on nolla, joten veto on yhtä suuri kuin liikekitka, $F = F_\mu$. Vaakasuoralla pöydällä tukivoima on yhtä suuri kuin paino, $N = mg$. Koska $F_\mu = \mu N$, $(N, F_\mu)$-kuvaaja on origon kautta kulkeva suora. Suoran kulmakerroin on $\mu$.
**Kuvaajan lukeminen:** Lasketaan ensin tukivoimat: $N = mg$ antaa arvot $1{,}96\,\text{N}$, $3{,}92\,\text{N}$, $5{,}89\,\text{N}$, $7{,}85\,\text{N}$ ja $9{,}81\,\text{N}$. Piirretään pisteet $(N, F_\mu)$. Sovitetaan niihin origon kautta kulkeva suora, joka kulkee mahdollisimman läheltä kaikkia pisteitä. Luetaan suoralta kaukainen piste. Tukivoimalla $N = 9{,}81\,\text{N}$ suoran arvo on noin $F_\mu = 4{,}1\,\text{N}$.
**Kaava:** $\mu = \dfrac{\Delta F_\mu}{\Delta N}$, kun $\Delta F_\mu$ ja $\Delta N$ luetaan sovitetulta suoralta
**Muunnokset:** Molemmat akselit ovat newtoneina, joten yksiköt supistuvat. Massat ovat kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $\mu = \dfrac{4{,}1\,\text{N} - 0\,\text{N}}{9{,}81\,\text{N} - 0\,\text{N}} = 0{,}418$
**Vastaus:** $0{,}42$. Vastauksessa on kaksi merkitsevää numeroa, koska vetovoimat on mitattu kolmen numeron tarkkuudella mutta suora piirretään käsin.
**Järkevyys:** Yksittäisistä pisteistä saadaan suhteet $F : N$ väliltä $0{,}41$–$0{,}43$, esimerkiksi $4{,}02\,\text{N} : 9{,}81\,\text{N} = 0{,}41$. Sovitetun suoran kulmakerroin osuu niiden väliin. Kerroin on yksikötön, ja se on puun ja pöydän välille tavallista suuruusluokkaa.

## fy4-6-L2-06
**Annettu:** $m = 0{,}75\,\text{kg}$, esimerkkiaineiston vetovoima $F$ ajan $t$ funktiona; suurin lukema $3{,}3\,\text{N}$ hetkellä $t = 2{,}5\,\text{s}$, tasaisen liikkeen lukemat $2{,}2\,\text{N}$, $2{,}1\,\text{N}$ ja $2{,}2\,\text{N}$ hetkillä $3{,}5\,\text{s}$–$4{,}5\,\text{s}$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** liikekitkakerroin $\mu$ (ei yksikköä) ja lepokitkakerroin $\mu_0$
**Periaate:** Ennen liikkeellelähtöä veto kasvaa, ja lepokitka kasvaa sen mukana. Kun veto ylittää lepokitkan enimmäisarvon $\mu_0 N$, palikka lähtee liikkeelle. Kuvaajan huippu on tämä enimmäisarvo. Tasaisella nopeudella voimien summa on nolla, joten veto on yhtä suuri kuin liikekitka $\mu N$. Vaakasuoralla pöydällä $N = mg$.
**Kuvaajan lukeminen:** Veto kasvaa suoraviivaisesti hetkeen $t = 2{,}5\,\text{s}$ asti. Siinä on kuvaajan huippu $3{,}3\,\text{N}$. Huipun jälkeen veto putoaa ja pysyy lähes vakiona, noin $2{,}2\,\text{N}$, kun palikka liikkuu tasaisella nopeudella. Vakiovedon lukemien summa on $2{,}2\,\text{N} + 2{,}1\,\text{N} + 2{,}2\,\text{N} = 6{,}5\,\text{N}$, joten niiden keskiarvo on $6{,}5\,\text{N} : 3 = 2{,}17\,\text{N}$.
**Kaava:** $N = mg$, $\mu_0 = \dfrac{F_{\text{huippu}}}{N}$ ja $\mu = \dfrac{F_{\text{tasainen}}}{N}$
**Muunnokset:** Massa on kilogrammoina ja voimat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $N = 0{,}75\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 7{,}36\,\text{N}$, $\mu_0 = \dfrac{3{,}3\,\text{N}}{7{,}36\,\text{N}} = 0{,}449$ ja $\mu = \dfrac{2{,}17\,\text{N}}{7{,}36\,\text{N}} = 0{,}295$
**Vastaus:** liikekitkakerroin on $\mu = 0{,}29$ ja lepokitkakerroin $\mu_0 = 0{,}45$. Vastauksissa on kaksi merkitsevää numeroa kuten massassa $0{,}75\,\text{kg}$ ja vetovoiman lukemissa.
**Järkevyys:** Liikekitkakerroin on pienempi kuin lepokitkakerroin, $0{,}29 < 0{,}45$, kuten yleensä. Siksi veto putoaa, kun palikka on lähtenyt liikkeelle. Liikkeessä pitämiseen tarvitaan pienempi voima kuin liikkeelle saamiseen. Kertoimet ovat puun ja pöydän välille tavallista suuruusluokkaa.

## fy4-6-L2-07
**Annettu:** esimerkkiaineiston viisi kulmaa: $24^\circ$, $26^\circ$, $25^\circ$, $27^\circ$ ja $25^\circ$
**Kysytty:** lepokitkakerroin $\mu_0$ (ei yksikköä)
**Periaate:** Kun lauta kallistuu, painon rinteen suuntainen komponentti $G_x = mg\sin\alpha$ kasvaa, ja lepokitka kasvaa sen mukana. Palikka lähtee liukumaan, kun komponentti ylittää lepokitkan enimmäisarvon $\mu_0 N$. Kohtisuorassa suunnassa palikka ei kiihdy, joten $N = mg\cos\alpha$. Rajakulmalla $\alpha_0$ pätee $mg\sin\alpha_0 = \mu_0\,mg\cos\alpha_0$. Massa supistuu. Kun yhtälö jaetaan puolittain, saadaan $\mu_0 = \tan\alpha_0$.
**Kaava:** $\mu_0 = \tan\alpha_0$, missä $\alpha_0$ on mittausten keskiarvo
**Muunnokset:** Kulmat ovat asteina, joten muunnoksia ei tarvita. Laskimen on oltava asteiden tilassa.
**Sijoitus:** Kulmien summa on $24^\circ + 26^\circ + 25^\circ + 27^\circ + 25^\circ = 127^\circ$, joten keskiarvo on $\alpha_{0,\text{ka}} = 127^\circ : 5 = 25{,}4^\circ$ ja $\mu_0 = \tan 25{,}4^\circ = 0{,}4748$
**Vastaus:** $0{,}47$. Vastauksessa on kaksi merkitsevää numeroa, koska kulmien keskiarvon tarkkuus on sen verran.
**Järkevyys:** Yksittäisistä kulmista saadaan $\tan 24^\circ = 0{,}45$ ja $\tan 27^\circ = 0{,}51$. Keskiarvo $0{,}47$ on niiden välissä. Kokeessa ei tarvita palikan massaa, koska se supistuu. Tulos on puun ja puun väliselle lepokitkakertoimelle tavallista suuruusluokkaa.

## fy4-6-L3-04
**Annettu:** alkunopeus $v_0 = 80\,\text{km/h}$, loppunopeus $v = 0$, kiihtyvyys vakio, pyörät lukkiutuvat; esimerkkiaineiston liikekitkakertoimet: kuiva asfaltti $\mu = 0{,}75$, märkä asfaltti $\mu = 0{,}45$; kohdassa c) märkä alamäki $\alpha = 6{,}0^\circ$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** jarrutusmatka $s$ yksikössä $\text{m}$, kohdissa a) kuiva vaakasuora, b) märkä vaakasuora ja c) märkä alamäki
**Periaate:** Lukkiutuneet pyörät liukuvat tiellä, joten autoon vaikuttaa liikekitka $\mu N$ liikettä vastaan. Newtonin toisen lain mukaan kitka antaa hidastuvuuden. Matka saadaan tasaisesti kiihtyvän liikkeen yhtälöstä $v^2 = v_0^2 - 2as$, kun $a$ on hidastuvuuden suuruus. Kohtisuorassa suunnassa auto ei kiihdy, joten $N = mg\cos\alpha$.
**Voimakuvio:** Kohdan c) auto on piirretty suorakulmiona rinteen suuntaisesti. Akseli $x$ osoittaa rinnettä alas ja akseli $y$ kohtisuoraan tiestä ulos. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit on piirretty katkoviivoin. Tukivoima $\overline{N}$ osoittaa kohtisuoraan tiestä ulos ja liikekitka $\overline{F}_\mu$ rinnettä ylös. Nopeus on rinnettä alas, mutta hidastuvuus on rinnettä ylös.
```voimakuvio
pinta -6
G 9,81
N 9,756
F_mu 4,390 ylös
v alas
a ylös
akselit -6
komponentit G
```
**Kaava:** vaakasuoralla $N = mg$ ja $\mu mg = ma$, joten $a = \mu g$. Alamäessä $x$: $\mu mg\cos\alpha - mg\sin\alpha = ma$, joten $a = g(\mu\cos\alpha - \sin\alpha)$. Matka on $s = \dfrac{v_0^2}{2a}$
**Muunnokset:** $v_0 = 80\,\text{km/h} = 80 : 3{,}6\,\text{m/s} = 22{,}22\,\text{m/s}$, ja $v_0^2 = 493{,}8\,\text{m}^2/\text{s}^2$.
**Sijoitus:** Kohta a): $a_a = 0{,}75\cdot 9{,}81\,\text{m/s}^2 = 7{,}358\,\text{m/s}^2$ ja $s_a = \dfrac{493{,}8\,\text{m}^2/\text{s}^2}{2\cdot 7{,}358\,\text{m/s}^2} = 33{,}6\,\text{m}$. Kohdat b) ja c):
```latex
\begin{aligned}
a_b &= 0{,}45 \cdot 9{,}81\,\text{m/s}^2 = 4{,}415\,\text{m/s}^2 \\
s_b &= \frac{493{,}8\,\text{m}^2/\text{s}^2}{2 \cdot 4{,}415\,\text{m/s}^2} = 55{,}9\,\text{m} \\[4pt]
a_c &= 9{,}81\,\text{m/s}^2 \\
&\quad \cdot (0{,}45\cos 6{,}0^\circ - \sin 6{,}0^\circ) \\
&= 3{,}365\,\text{m/s}^2 \\
s_c &= \frac{493{,}8\,\text{m}^2/\text{s}^2}{2 \cdot 3{,}365\,\text{m/s}^2} = 73{,}4\,\text{m}
\end{aligned}
```
**Vastaus:** a) $34\,\text{m}$, b) $56\,\text{m}$ ja c) $73\,\text{m}$ (laskettu $73{,}4\,\text{m}$). Kohdan c) tulos pyöristetään kahteen merkitsevään numeroon kuten kitkakertoimessa $0{,}45$ ja kulmassa $6{,}0^\circ$. Auton massaa ei tarvita, koska se supistuu. Sekä kitka että painon komponentti ovat verrannollisia massaan, joten hidastuvuus ei riipu siitä.
**Järkevyys:** Märällä tiellä matka on $55{,}9 : 33{,}6 = 1{,}66$-kertainen kuivaan verrattuna. Sama suhde saadaan kitkakertoimista: $0{,}75 : 0{,}45 = 1{,}67$. Alamäessä matka on pidempi kuin vaakasuoralla märällä tiellä, $73\,\text{m} > 56\,\text{m}$, koska painon komponentti rinnettä alas pienentää hidastuvuutta. Hidastuvuus $3{,}365\,\text{m/s}^2$ on silti positiivinen, koska $\mu = 0{,}45 > \tan 6{,}0^\circ = 0{,}11$.

## fy4-6-L3-05
**Annettu:** $m = 20\,\text{kg}$, $\alpha = 30^\circ$, $\mu = 0{,}35$, laatikko lähtee levossa, $t = 3{,}0\,\text{s}$; oppilaan ratkaisussa $N = mg$ ja tulos $1{,}5\,\text{m/s}^2$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** oppilaan virhe, oikea kiihtyvyys $a$ ja matka $s$ ajassa $3{,}0\,\text{s}$ yksikössä $\text{m}$
**Periaate:** Oppilas käytti tukivoimana koko painoa, $N = mg$. Rinteellä pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima. Laatikko ei kiihdy siinä suunnassa, joten $N = mg\cos\alpha$. Se on pienempi kuin paino. Oppilaan kitka $\mu mg$ on siksi liian suuri ja kiihtyvyys liian pieni. Oikea kiihtyvyys saadaan Newtonin toisesta laista rinteen suuntaan. Matka saadaan tasaisesti kiihtyvän liikkeen yhtälöstä, kun lähtönopeus on nolla.
**Voimakuvio:** Laatikko on piirretty suorakulmiona rinteen suuntaisesti. Akseli $x$ osoittaa rinnettä alas ja akseli $y$ kohtisuoraan pinnasta ulos. Paino $\overline{G}$ osoittaa suoraan alas, ja sen komponentit on piirretty katkoviivoin. Tukivoima $\overline{N}$ osoittaa kohtisuoraan pinnasta ulos, ja se on painoa lyhyempi. Liikekitka $\overline{F}_\mu$ osoittaa rinnettä ylös. Kiihtyvyys piirretään erikseen rinnettä alas.
```voimakuvio
pinta -30
G 196,2
N 169,9
F_mu 59,47 ylös
a alas
akselit -30
komponentit G
```
**Kaava:** $y$: $N - mg\cos\alpha = 0$ ja $x$: $mg\sin\alpha - \mu N = ma$, joten $a = g(\sin\alpha - \mu\cos\alpha)$. Matka on $s = \tfrac{1}{2}at^2$, koska alkunopeus on nolla
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä, joten muunnoksia ei tarvita. Massa supistuu.
**Sijoitus:** $a = 9{,}81\,\text{m/s}^2\cdot(\sin 30^\circ - 0{,}35\cdot\cos 30^\circ) = 1{,}931\,\text{m/s}^2$ ja
```latex
\begin{aligned}
s &= \tfrac{1}{2} \cdot 1{,}931\,\text{m/s}^2 \cdot (3{,}0\,\text{s})^2 \\
&= 8{,}69\,\text{m}
\end{aligned}
```
**Vastaus:** oppilaan virhe on $N = mg$ rinteellä. Oikea tukivoima on $N = mg\cos\alpha \approx 170\,\text{N}$ ja oikea kiihtyvyys $a \approx 1{,}9\,\text{m/s}^2$. Laatikko liukuu ajassa $3{,}0\,\text{s}$ matkan $8{,}7\,\text{m}$. Vastauksessa on kaksi merkitsevää numeroa kuten kitkakertoimessa $0{,}35$ ja ajassa $3{,}0\,\text{s}$.
**Järkevyys:** Oppilaan kiihtyvyys $1{,}5\,\text{m/s}^2$ on liian pieni, koska hän laski kitkan $\mu mg = 69\,\text{N}$ liian suureksi. Oikea kitka on $\mu mg\cos\alpha = 59\,\text{N}$. Ilman kitkaa kiihtyvyys olisi $g\sin 30^\circ \approx 4{,}9\,\text{m/s}^2$, joten kitka pienentää sitä. Liukuessaan laatikko kiihtyy alas, koska $\tan 30^\circ = 0{,}58 > \mu = 0{,}35$. Tehtävän mukaan laatikko lähtee liikkeelle, joten $\mu_0 < \tan 30^\circ$.

## fy4-6-L2-08
**Annettu:** esimerkkiarvot: A: $m_\text{A} = 20\,\text{kg}$, liukuu, $\mu = 0{,}30$; B: $m_\text{B} = 40\,\text{kg}$, levossa, työntö $F = 30\,\text{N}$, $\mu_0 = 0{,}50$; C: $m_\text{C} = 10\,\text{kg}$, liukuu, $\mu = 0{,}45$; D: $m_\text{D} = 25\,\text{kg}$, levossa rinteellä, $\alpha = 30^\circ$, $\mu_0 = 0{,}70$; $g = 9{,}81\,\text{m/s}^2$

**Kysytty:** laatikoiden järjestys niihin vaikuttavan kitkavoiman suuruuden mukaan pienimmästä suurimpaan

**Periaate:** Liukuvaan laatikkoon vaikuttaa liikekitka $F_\mu = \mu N$. Vaakasuoralla lattialla $N = mg$, koska pystysuunnassa vaikuttavat vain paino ja tukivoima. Levossa olevaan laatikkoon vaikuttaa lepokitka. Se on juuri niin suuri kuin tasapaino vaatii, enintään $\mu_0 N$. Siksi levossa olevan laatikon kitka lasketaan liikeyhtälöstä $\Sigma F_x = 0$, ei lepokitkakertoimesta.

**Mallivastaus:** Liukuvat laatikot:

$F_{\mu\text{A}} = \mu m_\text{A} g$

$F_{\mu\text{A}} = 0{,}30 \cdot 20\,\text{kg} \cdot 9{,}81\,\text{m/s}^2$

$F_{\mu\text{A}} \approx 58{,}9\,\text{N}$

$F_{\mu\text{C}} = 0{,}45 \cdot 10\,\text{kg} \cdot 9{,}81\,\text{m/s}^2$

$F_{\mu\text{C}} \approx 44{,}1\,\text{N}$

Laatikko B ei liiku. Siksi vaakasuunnassa $F - F_{\mu\text{B}} = 0$ ja $F_{\mu\text{B}} = F = 30\,\text{N}$. Lepokitkan yläraja $\mu_0 m_\text{B} g \approx 196\,\text{N}$ ei ole kitkan arvo. Se kertoo vain, että laatikko pysyy paikallaan.

Laatikko D on levossa rinteellä. Siksi rinteen suunnassa lepokitka kumoaa painon rinteen suuntaisen komponentin:

$F_{\mu\text{D}} = m_\text{D} g \sin\alpha$

$F_{\mu\text{D}} = 25\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot \sin 30^\circ$

$F_{\mu\text{D}} \approx 123\,\text{N}$

Yläraja on $\mu_0 m_\text{D} g \cos\alpha \approx 149\,\text{N}$. Laatikko siis todella pysyy paikallaan.

Kitkavoiman mukaan pienimmästä suurimpaan järjestys on B ($30\,\text{N}$), C ($44\,\text{N}$), A ($59\,\text{N}$), D ($1{,}2 \cdot 10^2\,\text{N}$). Jos laatikon B kitkaksi laskettaisiin virheellisesti $\mu_0 N$, se olisi suurin. Järjestys olisi eri myös massan tai kitkakertoimen mukaan, koska kitka riippuu sekä tukivoimasta että siitä, liukuuko laatikko.
