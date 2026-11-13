## fy4-13-L1-01
**Annettu:** $m = 1{,}5\,\text{kg}$ ja langan jännitysvoima $T = 3{,}0\,\text{N}$ vaakasuoraan. Kitka jätetään huomiotta.
**Kysytty:** kärryn kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Kärry kiihtyy vaakasuunnassa. Newtonin toisen lain mukaan vaakasuuntaisten voimien summa on massa kertaa kiihtyvyys. Pystysuunnassa kärry ei kiihdy, joten siellä voimat kumoavat toisensa.
**Voimakuvio:** Piirrä kärry suorakulmioksi. Valitse $x$-suunta langan suuntaan. Paino $\overline{G}$ osoittaa alas ja pöydän tukivoima $\overline{N}$ ylös, ja nuolet ovat yhtä pitkät. Jännitysvoima $\overline{T}$ osoittaa vaakasuoraan eteenpäin. Vaakasuunnassa vaikuttaa vain $\overline{T}$.
```voimakuvio
pinta 0
G 14,715
N 14,715
T 3,0 oikea
a oikea
akselit 0
```
**Kaava:** $T = ma$, joten $a = \dfrac{T}{m}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{3{,}0\,\text{N}}{1{,}5\,\text{kg}} = 2{,}0\,\text{m/s}^2$
**Vastaus:** $2{,}0\,\text{m/s}^2$. Vastauksessa on kaksi merkitsevää numeroa, koska tiedoissa $3{,}0\,\text{N}$ ja $1{,}5\,\text{kg}$ on kaksi.
**Järkevyys:** Yksi newton antaa yhden kilogramman kappaleelle kiihtyvyyden $1\,\text{m/s}^2$. Voima $3{,}0\,\text{N}$ ja massa $1{,}5\,\text{kg}$ antavat kaksi kertaa sen. Tulo $1{,}5\,\text{kg} \cdot 2{,}0\,\text{m/s}^2 = 3{,}0\,\text{N}$ antaa voiman takaisin.

## fy4-13-L1-02
**Annettu:** $m = 0{,}60\,\text{kg}$, kiihtyvyys alas $a = 2{,}0\,\text{m/s}^2$ ja $g = 9{,}81\,\text{m/s}^2$. Ilmanvastus jätetään huomiotta.
**Kysytty:** langan jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Punnus kiihtyy alas. Newtonin toisen lain mukaan sen kokonaisvoima osoittaa alas ja on $ma$. Punnukseen vaikuttavat Maa ja lanka.
**Voimakuvio:** Piirrä punnus suorakulmioksi. Positiivinen suunta on alas. Paino $\overline{G}$ lähtee keskipisteestä alas ja jännitysvoima $\overline{T}$ yläpinnasta ylös. Nuoli $\overline{G}$ on pidempi, koska kokonaisvoima osoittaa alas.
```voimakuvio
G 5,886
T 4,686 ylös
a alas
```
**Kaava:** $mg - T = ma$, joten $T = m(g - a)$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $T = 0{,}60\,\text{kg} \cdot (9{,}81\,\text{m/s}^2 - 2{,}0\,\text{m/s}^2) = 0{,}60\,\text{kg} \cdot 7{,}81\,\text{m/s}^2 = 4{,}686\,\text{N}$
**Vastaus:** $4{,}7\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa, koska massassa $0{,}60\,\text{kg}$ ja kiihtyvyydessä $2{,}0\,\text{m/s}^2$ on kaksi.
**Järkevyys:** Punnuksen paino on $0{,}60\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 5{,}9\,\text{N}$. Tulos $4{,}7\,\text{N}$ on sitä pienempi, koska punnus kiihtyy alas. Erotus $1{,}2\,\text{N}$ on $ma = 0{,}60\,\text{kg} \cdot 2{,}0\,\text{m/s}^2$.

## fy4-13-L1-03
**Annettu:** kärry $m_1 = 1{,}0\,\text{kg}$, punnus $m_2 = 0{,}40\,\text{kg}$ ja $g = 9{,}81\,\text{m/s}^2$. Kitka ja ilmanvastus jätetään huomiotta. Lanka on kevyt ja venymätön, ja väkipyörä on kevyt ja kitkaton.
**Kysytty:** langan jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Kappaleita on kaksi, joten kummallekin kirjoitetaan oma liikeyhtälö. Lanka ei veny, joten kiihtyvyys $a$ on molemmilla yhtä suuri. Kevyt lanka ja kitkaton väkipyörä siirtävät voiman muuttumattomana. Siksi lanka vetää kumpaakin voimalla $T$.
**Voimakuvio:** Piirrä kärry suorakulmioksi, positiivinen suunta oikealle. Voimat $\overline{G}_1$ ja $\overline{N}$ kumoavat toisensa, ja vaakasuunnassa vaikuttaa $\overline{T}_1$. Piirrä punnus suorakulmioksi, positiivinen suunta alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös.
```voimakuvio
pinta 0
G_1 9,81
N 9,81
T_1 2,803 oikea
a oikea
---
G_2 3,924
T_2 2,803 ylös
a alas
```
**Kaava:** $T = m_1 a$ ja $m_2 g - T = m_2 a$. Yhteenlaskusta $m_2 g = (m_1 + m_2)\,a$, joten $a = \dfrac{m_2 g}{m_1 + m_2}$, ja $T = m_1 a$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{0{,}40\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{1{,}4\,\text{kg}} = 2{,}803\,\text{m/s}^2$ ja $T = 1{,}0\,\text{kg} \cdot 2{,}803\,\text{m/s}^2 = 2{,}803\,\text{N}$
**Vastaus:** $2{,}8\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa, koska massoissa $1{,}0\,\text{kg}$ ja $0{,}40\,\text{kg}$ on kaksi.
**Järkevyys:** Jännitysvoima on pienempi kuin punnuksen paino $m_2 g = 3{,}9\,\text{N}$, koska punnus kiihtyy alas. Kiihtyvyys $a = T : m_1 \approx 2{,}8\,\text{m/s}^2$ on pienempi kuin $g$. Erotus $3{,}9\,\text{N} - 2{,}8\,\text{N} = 1{,}1\,\text{N}$ on $m_2 a = 0{,}40\,\text{kg} \cdot 2{,}8\,\text{m/s}^2$.

## fy4-13-L1-04
**Annettu:** kaksi kappaletta, kummankin massa $m = 3{,}0\,\text{kg}$, levossa, ja $g = 9{,}81\,\text{m/s}^2$. Lanka on kevyt, ja väkipyörä on kevyt ja kitkaton.
**Kysytty:** langan jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Kappale on levossa. Newtonin toisen lain mukaan siihen vaikuttavien voimien summa on silloin nolla. Toisen kappaleen voimakuvio riittää, koska kevyt lanka vetää kumpaakin kappaletta yhtä suurella voimalla.
**Voimakuvio:** Piirrä kappale suorakulmioksi, positiivinen suunta ylös. Paino $\overline{G}$ lähtee keskipisteestä alas ja jännitysvoima $\overline{T}$ yläpinnasta ylös. Nuolet ovat yhtä pitkät.
```voimakuvio
G 29,43
T 29,43 ylös
a 0
```
**Kaava:** $T - mg = 0$, joten $T = mg$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $T = 3{,}0\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 29{,}43\,\text{N}$
**Vastaus:** $29\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa, koska massassa $3{,}0\,\text{kg}$ on kaksi.
**Järkevyys:** Jännitysvoima on yhden kappaleen paino. Se ei ole kahden kappaleen painojen summa $59\,\text{N}$, sillä lanka kannattelee kumpaakin päästään yhdellä voimalla. Jos toinen kappale korvattaisiin seinään kiinnitetyllä koukulla, lanka kestäisi saman voiman.

## fy4-13-L1-05
**Annettu:** kärryt $m_1 = 1{,}0\,\text{kg}$ ja $m_2 = 2{,}0\,\text{kg}$, vetovoima $F = 12\,\text{N}$ kevyempään kärryyn. Kitka jätetään huomiotta.
**Kysytty:** kärryjen yhteinen kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Kärryt liikkuvat yhdessä, ja niiden kiihtyvyydet ovat yhtä suuret. Kummallekin kärrylle kirjoitetaan oma liikeyhtälö. Kun yhtälöt lasketaan yhteen, langan sisäinen voima $T$ poistuu.
**Voimakuvio:** Piirrä kevyempi kärry suorakulmioksi, positiivinen suunta vetoon päin. Vaakasuunnassa vetovoima $\overline{F}$ osoittaa eteenpäin ja jännitysvoima $\overline{T}_1$ taaksepäin. Piirrä raskaampi kärry suorakulmioksi. Vaakasuunnassa vaikuttaa vain $\overline{T}_2$ eteenpäin. Paino ja tukivoima kumoavat toisensa kummassakin kärryssä.
```voimakuvio
pinta 0
G_1 9,81
N_1 9,81
F 12 oikea
T_1 8,0 vasen
a oikea
---
pinta 0
G_2 19,62
N_2 19,62
T_2 8,0 oikea
a oikea
```
**Kaava:** $F - T = m_1 a$ ja $T = m_2 a$. Yhteenlaskusta $F = (m_1 + m_2)\,a$, joten $a = \dfrac{F}{m_1 + m_2}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{12\,\text{N}}{1{,}0\,\text{kg} + 2{,}0\,\text{kg}} = 4{,}0\,\text{m/s}^2$
**Vastaus:** $4{,}0\,\text{m/s}^2$. Vastauksessa on kaksi merkitsevää numeroa, koska tiedoissakin on kaksi.
**Järkevyys:** Jännitysvoima on $T = m_2 a = 2{,}0\,\text{kg} \cdot 4{,}0\,\text{m/s}^2 = 8{,}0\,\text{N}$. Kevyempään kärryyn jää $F - T = 4{,}0\,\text{N} = m_1 a$. Kiihtyvyys on sama kuin silloin, kun $3{,}0\,\text{kg}$:n kappaletta vedettäisiin voimalla $12\,\text{N}$.

## fy4-13-L2-01
**Annettu:** ylempi laatikko $m_1 = 50\,\text{kg}$, alempi laatikko $m_2 = 30\,\text{kg}$, kiihtyvyys ylös $a = 1{,}2\,\text{m/s}^2$ ja $g = 9{,}81\,\text{m/s}^2$. Köydet ovat kevyet ja venymättömät. Ilmanvastus jätetään huomiotta.
**Kysytty:** nosturin köyden jännitysvoima $T_1$ yksikössä $\text{N}$
**Periaate:** Laatikot ovat kaksi kappaletta, ja kummallekin kirjoitetaan oma liikeyhtälö. Alempi laatikko roikkuu ylemmästä, joten niillä on sama kiihtyvyys $a$. Kevyen köyden voima on sama köyden kummassakin päässä. Siksi alempi köysi vetää ylempää laatikkoa alas samalla voimalla $T_2$, jolla se vetää alempaa laatikkoa ylös.
**Voimakuvio:** Piirrä ylempi laatikko suorakulmioksi, positiivinen suunta ylös. Nosturin köyden voima $\overline{T}_1$ lähtee yläpinnasta ylös, paino $\overline{G}_1$ keskipisteestä alas ja alemman köyden voima $\overline{T}_2$ alapinnasta alas. Piirrä alempi laatikko suorakulmioksi. Voima $\overline{T}_2$ lähtee yläpinnasta ylös ja paino $\overline{G}_2$ alas. Nuoli $\overline{T}_1$ on pisin.
```voimakuvio
T_1 880,8 ylös
G_1 490,5
T_2 330,3 alas @ala
a ylös
---
T_2 330,3 ylös
G_2 294,3
a ylös
```
**Kaava:** $T_1 - T_2 - m_1 g = m_1 a$ ja $T_2 - m_2 g = m_2 a$, joten yhteenlaskusta $T_1 = (m_1 + m_2)(g + a)$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $T_1 = (50\,\text{kg} + 30\,\text{kg}) \cdot (9{,}81\,\text{m/s}^2 + 1{,}2\,\text{m/s}^2) = 80\,\text{kg} \cdot 11{,}01\,\text{m/s}^2 = 880{,}8\,\text{N}$
**Vastaus:** $880\,\text{N}$ eli $8{,}8 \cdot 10^{2}\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa, koska kiihtyvyydessä $1{,}2\,\text{m/s}^2$ ja massassa $30\,\text{kg}$ on kaksi.
**Järkevyys:** Laatikoiden yhteinen paino on $80\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 785\,\text{N}$. Kiihtyvä nosto vaatii enemmän. Ylimäärä $96\,\text{N}$ on $(m_1 + m_2)\,a = 80\,\text{kg} \cdot 1{,}2\,\text{m/s}^2$. Alemman köyden voima on $T_2 = m_2 (g + a) \approx 330\,\text{N}$. Se on pienempi kuin $T_1$, koska se kantaa vain alemman laatikon.

## fy4-13-L2-02
**Annettu:** $m_1 = 0{,}50\,\text{kg}$ ja $m_2 = 1{,}0\,\text{kg}$ langan päissä ja $g = 9{,}81\,\text{m/s}^2$. Lanka on kevyt, ja väkipyörä on kevyt ja kitkaton. Ilmanvastus jätetään huomiotta.
**Kysytty:** langan jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Kummallekin kappaleelle kirjoitetaan oma liikeyhtälö. Raskaampi $m_2$ laskee ja kevyempi $m_1$ nousee. Lanka ei veny, joten kiihtyvyys $a$ on molemmilla yhtä suuri. Lanka vetää kumpaakin voimalla $T$.
**Voimakuvio:** Piirrä kevyempi kappale suorakulmioksi, positiivinen suunta ylös. Voima $\overline{T}_1$ osoittaa ylös ja $\overline{G}_1$ alas. Piirrä raskaampi kappale suorakulmioksi, positiivinen suunta alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös.
```voimakuvio
G_1 4,905
T_1 6,54 ylös
a ylös
---
G_2 9,81
T_2 6,54 ylös
a alas
```
**Kaava:** $T - m_1 g = m_1 a$ ja $m_2 g - T = m_2 a$, joten yhteenlaskusta $a = \dfrac{(m_2 - m_1)\,g}{m_1 + m_2}$ ja $T = m_1 (g + a) = \dfrac{2 m_1 m_2}{m_1 + m_2}\cdot g$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $T = \dfrac{2 \cdot 0{,}50\,\text{kg} \cdot 1{,}0\,\text{kg}}{0{,}50\,\text{kg} + 1{,}0\,\text{kg}} \cdot 9{,}81\,\text{m/s}^2 = 0{,}6667\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 6{,}54\,\text{N}$
**Vastaus:** $6{,}5\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa, koska massoissa $0{,}50\,\text{kg}$ ja $1{,}0\,\text{kg}$ on kaksi.
**Järkevyys:** Painot ovat $m_1 g \approx 4{,}9\,\text{N}$ ja $m_2 g \approx 9{,}8\,\text{N}$. Tulos $6{,}5\,\text{N}$ on niiden välissä: nousevalle kappaleelle $T > G_1$ ja laskevalle $T < G_2$. Kiihtyvyys $a = 3{,}27\,\text{m/s}^2$ antaa samat voimat: $T - G_1 = 1{,}635\,\text{N} = m_1 a$.

## fy4-13-L2-03
**Annettu:** kelkat $m_1 = 3{,}0\,\text{kg}$ (vedettävä) ja $m_2 = 2{,}0\,\text{kg}$ sekä vetovoima $F = 20\,\text{N}$. Kitka ja ilmanvastus jätetään huomiotta. Narut ovat kevyet ja venymättömät.
**Kysytty:** kelkkojen välisen narun jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Kelkat liikkuvat yhdessä, ja niiden kiihtyvyys $a$ on yhtä suuri. Kummallekin kelkalle kirjoitetaan oma liikeyhtälö. Takimmaista kelkkaa vetää vain kelkkojen välinen naru.
**Voimakuvio:** Piirrä raskaampi kelkka suorakulmioksi, positiivinen suunta vetoon päin. Vetovoima $\overline{F}$ osoittaa eteenpäin ja jännitysvoima $\overline{T}_1$ taaksepäin. Piirrä kevyempi kelkka suorakulmioksi. Vaakasuunnassa vaikuttaa vain $\overline{T}_2$ eteenpäin. Paino ja tukivoima kumoavat toisensa kummassakin kelkassa.
```voimakuvio
pinta 0
G_1 29,43
N_1 29,43
F 20 oikea
T_1 8,0 vasen
a oikea
---
pinta 0
G_2 19,62
N_2 19,62
T_2 8,0 oikea
a oikea
```
**Kaava:** $F - T = m_1 a$ ja $T = m_2 a$. Yhteenlaskusta $a = \dfrac{F}{m_1 + m_2}$, joten $T = m_2 a = \dfrac{m_2}{m_1 + m_2}\,F$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $T = \dfrac{2{,}0\,\text{kg}}{3{,}0\,\text{kg} + 2{,}0\,\text{kg}} \cdot 20\,\text{N} = 0{,}40 \cdot 20\,\text{N} = 8{,}0\,\text{N}$
**Vastaus:** $8{,}0\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa, koska tiedoissakin on kaksi.
**Järkevyys:** Narun voima on pienempi kuin vetovoima $20\,\text{N}$, koska naru kiihdyttää vain takimmaista kelkkaa. Kiihtyvyys on $a = 20\,\text{N} : 5{,}0\,\text{kg} = 4{,}0\,\text{m/s}^2$. Etummaiselle kelkalle jää $20\,\text{N} - 8{,}0\,\text{N} = 12\,\text{N} = m_1 a$.

## fy4-13-L2-04
**Annettu:** kevyemmän kappaleen massa $m_1 = 0{,}60\,\text{kg}$, raskaamman kiihtyvyys alas $a = 2{,}0\,\text{m/s}^2$ ja $g = 9{,}81\,\text{m/s}^2$. Lanka on kevyt, ja väkipyörä on kevyt ja kitkaton. Ilmanvastus jätetään huomiotta.
**Kysytty:** raskaamman kappaleen massa $m_2$ yksikössä $\text{kg}$
**Periaate:** Kappaleita on kaksi, ja kummallekin kirjoitetaan oma liikeyhtälö. Lanka ei veny, joten kiihtyvyys $a$ on molemmilla yhtä suuri. Kevyt lanka vetää kumpaakin voimalla $T$. Kevyempi kappale nousee ja raskaampi laskee.
**Voimakuvio:** Piirrä kevyempi kappale suorakulmioksi, positiivinen suunta ylös. Voima $\overline{T}_1$ osoittaa ylös ja $\overline{G}_1$ alas, ja $\overline{T}_1$ on pidempi. Piirrä raskaampi kappale suorakulmioksi, positiivinen suunta alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös, ja $\overline{G}_2$ on pidempi.
```voimakuvio
G_1 5,886
T_1 7,086 ylös
a ylös
---
G_2 8,901
T_2 7,086 ylös
a alas
```
**Kaava:** $T - m_1 g = m_1 a$ ja $m_2 g - T = m_2 a$. Ensimmäisestä saadaan $T = m_1 (g + a)$. Toinen antaa $m_2 (g - a) = T$, joten $m_2 = \dfrac{m_1 (g + a)}{g - a}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $m_2 = \dfrac{0{,}60\,\text{kg} \cdot (9{,}81 + 2{,}0)\,\text{m/s}^2}{(9{,}81 - 2{,}0)\,\text{m/s}^2} = \dfrac{7{,}086\,\text{N}}{7{,}81\,\text{m/s}^2} = 0{,}9073\,\text{kg}$
**Vastaus:** $0{,}91\,\text{kg}$. Vastauksessa on kaksi merkitsevää numeroa, koska massassa $0{,}60\,\text{kg}$ ja kiihtyvyydessä $2{,}0\,\text{m/s}^2$ on kaksi.
**Järkevyys:** Massa $0{,}91\,\text{kg}$ on suurempi kuin $0{,}60\,\text{kg}$, kuten raskaamman kappaleen pitääkin. Tarkistus kaavalla $a = \dfrac{(m_2 - m_1)\,g}{m_1 + m_2} = \dfrac{0{,}3073 \cdot 9{,}81}{1{,}5073}\,\text{m/s}^2 \approx 2{,}0\,\text{m/s}^2$. Jännitysvoima $T = 7{,}09\,\text{N}$ on painojen $5{,}9\,\text{N}$ ja $8{,}9\,\text{N}$ välissä.

## fy4-13-L3-01
**Annettu:** korin massa $m_1 = 800\,\text{kg}$, vastapainon massa $m_2 = 1200\,\text{kg}$ ja $g = 9{,}81\,\text{m/s}^2$. Köysi on kevyt ja venymätön, pyörä on kevyt ja kitkaton, ja ilmanvastus jätetään huomiotta.
**Kysytty:** voima $F_\text{akseli}$, jolla köysi vaikuttaa pyörän akseliin, yksikössä $\text{N}$
**Periaate:** Kori ja vastapaino ovat kaksi kappaletta, ja kummallekin kirjoitetaan oma liikeyhtälö. Köysi ei veny, joten $a$ on molemmilla yhtä suuri. Kevyt köysi vetää kumpaakin voimalla $T$. Pyörä on kevyt eikä kiihdy, joten sen kokonaisvoima on nolla.
**Voimakuvio:** Piirrä kori suorakulmioksi, positiivinen suunta ylös. Voima $\overline{T}_1$ osoittaa ylös ja $\overline{G}_1$ alas. Piirrä vastapaino suorakulmioksi, positiivinen suunta alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös. Nuolet $\overline{T}_1$ ja $\overline{T}_2$ ovat yhtä pitkät. Pyörässä on kaksi voimaa $T$ alas ja voima $F_\text{akseli}$ ylös.
```voimakuvio
G_1 7848
T_1 9418 ylös
a ylös
---
G_2 1,177e+04
T_2 9418 ylös
a alas
```
**Kaava:** $T - m_1 g = m_1 a$ ja $m_2 g - T = m_2 a$, joten $T = \dfrac{2 m_1 m_2}{m_1 + m_2}\cdot g$. Pyörän tasapainosta $F_\text{akseli} - 2T = 0$, joten $F_\text{akseli} = 2T$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $T = \dfrac{2 \cdot 800\,\text{kg} \cdot 1200\,\text{kg}}{800\,\text{kg} + 1200\,\text{kg}} \cdot 9{,}81\,\text{m/s}^2 = 960\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 9418\,\text{N}$ ja $F_\text{akseli} = 2 \cdot 9418\,\text{N} = 18\,835\,\text{N}$
**Vastaus:** $19000\,\text{N}$ eli $19\,\text{kN}$. Vastauksessa on kaksi merkitsevää numeroa, koska massat on annettu sadan kilogramman tarkkuudella.
**Järkevyys:** Painot ovat $m_1 g \approx 7850\,\text{N}$ ja $m_2 g \approx 11\,770\,\text{N}$. Jännitysvoima $T = 9418\,\text{N}$ on niiden välissä. Akselin voima $18\,835\,\text{N}$ on pienempi kuin painojen summa $19\,620\,\text{N}$, koska vastapaino kiihtyy alas.

## fy4-13-L3-02
**Annettu:** kärry $m_1 = 1{,}0\,\text{kg}$, suurin sallittu jännitysvoima $T_{\max} = 3{,}0\,\text{N}$ ja $g = 9{,}81\,\text{m/s}^2$. Kitka jätetään huomiotta. Lanka ja väkipyörä ovat kevyet.
**Kysytty:** suurin punnuksen massa $m_2$ yksikössä $\text{kg}$
**Periaate:** Kappaleille kirjoitetaan omat liikeyhtälöt. Niistä saadaan jännitysvoima massojen avulla. Jännitysvoima kasvaa, kun punnuksen massa kasvaa. Siksi raja-arvo $T = T_{\max}$ antaa suurimman massan.
**Voimakuvio:** Piirrä kärry suorakulmioksi, positiivinen suunta oikealle. Vaakasuunnassa vaikuttaa vain $\overline{T}_1$. Piirrä punnus suorakulmioksi, positiivinen suunta alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös.
```voimakuvio
pinta 0
G_1 9,81
N 9,81
T_1 3 oikea
a oikea
---
G_2 4,321
T_2 3 ylös
a alas
```
**Kaava:** $T = m_1 a$ ja $m_2 g - T = m_2 a$, joten $T = \dfrac{m_1 m_2}{m_1 + m_2}\,g$. Kun $T = T_{\max}$: $T_{\max} (m_1 + m_2) = m_1 m_2 g$, joten $m_2 = \dfrac{m_1\,T_{\max}}{g\,m_1 - T_{\max}}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $m_2 = \dfrac{3{,}0\,\text{N} \cdot 1{,}0\,\text{kg}}{1{,}0\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 - 3{,}0\,\text{N}} = \dfrac{3{,}0\,\text{N}\cdot\text{kg}}{6{,}81\,\text{N}} = 0{,}4405\,\text{kg}$
**Vastaus:** $0{,}44\,\text{kg}$. Vastauksessa on kaksi merkitsevää numeroa, koska tiedoissa $3{,}0\,\text{N}$ ja $1{,}0\,\text{kg}$ on kaksi.
**Järkevyys:** Tarkistus: $T = \dfrac{1{,}0 \cdot 0{,}4405}{1{,}4405} \cdot 9{,}81\,\text{N} \approx 3{,}0\,\text{N}$. Jos punnus on raja-arvoa raskaampi, $T$ on suurempi. Se on kuitenkin aina pienempi kuin kärryn paino $9{,}81\,\text{N}$, koska $T$ lähestyy arvoa $m_1 g$ vasta äärettömän suurella $m_2$:lla.

## fy4-13-L3-03
**Annettu:** kärry $m_1 = 1{,}5\,\text{kg}$, punnus $m_2 = 0{,}50\,\text{kg}$, matka $s = 0{,}90\,\text{m}$, lähtö levosta ja $g = 9{,}81\,\text{m/s}^2$. Kitka jätetään huomiotta. Lanka ja väkipyörä ovat kevyet.
**Kysytty:** aika $t$ yksikössä $\text{s}$
**Periaate:** Ensin kappaleiden liikeyhtälöistä saadaan kiihtyvyys. Kiihtyvyys on vakio, joten levosta lähtevälle liikkeelle pätee $s = \tfrac{1}{2}at^2$. Siitä saadaan aika.
**Voimakuvio:** Piirrä kärry suorakulmioksi, positiivinen suunta oikealle. Vaakasuunnassa vaikuttaa vain $\overline{T}_1$. Piirrä punnus suorakulmioksi, positiivinen suunta alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös, ja $T_1 = T_2 = T$.
```voimakuvio
pinta 0
G_1 14,71
N 14,71
T_1 3,679 oikea
a oikea
---
G_2 4,905
T_2 3,679 ylös
a alas
```
**Kaava:** $T = m_1 a$ ja $m_2 g - T = m_2 a$, joten $a = \dfrac{m_2 g}{m_1 + m_2}$. Matkasta $s = \tfrac{1}{2}at^2$, joten $t = \sqrt{\dfrac{2s}{a}}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{0{,}50\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{2{,}0\,\text{kg}} = 2{,}4525\,\text{m/s}^2$ ja $t = \sqrt{\dfrac{2 \cdot 0{,}90\,\text{m}}{2{,}4525\,\text{m/s}^2}} = 0{,}857\,\text{s}$
**Vastaus:** $0{,}86\,\text{s}$. Vastauksessa on kaksi merkitsevää numeroa, koska tiedoissa $0{,}90\,\text{m}$ ja $0{,}50\,\text{kg}$ on kaksi.
**Järkevyys:** Tarkistus: loppunopeus on $at \approx 2{,}1\,\text{m/s}$ ja keskinopeus $1{,}05\,\text{m/s}$. Silloin $1{,}05\,\text{m/s} \cdot 0{,}857\,\text{s} \approx 0{,}90\,\text{m}$. Vapaasti putoava punnus ($a = g$) kulkisi saman matkan ajassa $0{,}43\,\text{s}$. Aika $0{,}86\,\text{s}$ on järkevästi pidempi.

## fy4-13-L1-06
**Kysytty:** miten langan jännitysvoima $T$ ja punnuksen paino $G_2$ vertautuvat toisiinsa, kun punnus laskee ja kiihtyy.
**Periaate:** Newtonin toisen lain mukaan kokonaisvoima osoittaa kiihtyvyyden suuntaan. Punnus kiihtyy alas, joten sen kokonaisvoima osoittaa alas. Punnukseen vaikuttavat vain paino alas ja langan jännitysvoima ylös.
**Mallivastaus:** Punnukselle pätee $G_2 - T = m_2 a$. Punnus kiihtyy alas, joten $a > 0$ ja $G_2 - T > 0$. Jännitysvoima on siis pienempi kuin punnuksen paino. Lanka ei kannattele koko painoa, koska punnus kiihtyy alas eikä ole levossa. Lanka ei voi vetää myöskään painoa kovemmin. Silloin kokonaisvoima osoittaisi ylös, eikä punnus laskisi. Lanka vetää kärryä ja punnusta samalla voimalla $T$. Se ei jaa voimaansa puoliksi. Voimien erotus on aina $m_2 a$.

## fy4-13-L1-07
**Annettu:** $m_1 = 0{,}30\,\text{kg}$ ja $m_2 = 0{,}70\,\text{kg}$ langan päissä ja $g = 9{,}81\,\text{m/s}^2$. Lanka on kevyt ja venymätön. Väkipyörä on kevyt ja kitkaton. Ilmanvastus jätetään huomiotta.
**Kysytty:** kappaleiden yhteinen kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Kirjoita kummallekin kappaleelle oma liikeyhtälö. Lanka ei veny, joten kappaleiden kiihtyvyyksillä on sama suuruus $a$. Kevyt lanka vetää kumpaakin kappaletta voimalla $T$. Raskaampi kappale laskee ja kevyempi nousee.
**Voimakuvio:** Piirrä kevyempi kappale suorakulmioksi. Positiivinen suunta on ylös. Voima $\overline{T}_1$ osoittaa ylös ja $\overline{G}_1$ alas. Piirrä raskaampi kappale suorakulmioksi. Positiivinen suunta on alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös. Nuoli $\overline{T}$ on lyhyempi kuin $\overline{G}_2$ ja pidempi kuin $\overline{G}_1$.
```voimakuvio
G_1 2,943
T_1 4,12 ylös
a ylös
---
G_2 6,867
T_2 4,12 ylös
a alas
```
**Kaava:** $T - m_1 g = m_1 a$ ja $m_2 g - T = m_2 a$. Kun lasket yhtälöt yhteen, $T$ poistuu: $(m_2 - m_1)\,g = (m_1 + m_2)\,a$. Siis $a = \dfrac{(m_2 - m_1)\,g}{m_1 + m_2}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{(0{,}70\,\text{kg} - 0{,}30\,\text{kg}) \cdot 9{,}81\,\text{m/s}^2}{0{,}30\,\text{kg} + 0{,}70\,\text{kg}} = \dfrac{0{,}40 \cdot 9{,}81}{1{,}00}\,\text{m/s}^2 = 3{,}924\,\text{m/s}^2$
**Vastaus:** $3{,}9\,\text{m/s}^2$. Vastauksessa on kaksi merkitsevää numeroa, koska massoissa $0{,}30\,\text{kg}$ ja $0{,}70\,\text{kg}$ on kaksi.
**Järkevyys:** Kiihtyvyys on pienempi kuin $g = 9{,}81\,\text{m/s}^2$, koska kevyempi kappale hidastaa raskaampaa. Jännitysvoima on $T = m_1 (g + a) = 0{,}30\,\text{kg} \cdot 13{,}73\,\text{m/s}^2 = 4{,}12\,\text{N}$. Raskaammalle kappaleelle saadaan $m_2 g - T = 6{,}87\,\text{N} - 4{,}12\,\text{N} = 2{,}75\,\text{N} = m_2 a$.

## fy4-13-L1-08
**Kysytty:** mitkä voimat vaikuttavat kärryyn pöydän suunnassa, kun punnus laskee langan varassa.
**Periaate:** Voimakuvioon piirretään vain voimat, jotka vaikuttavat juuri siihen kappaleeseen. Jokainen voima syntyy vuorovaikutuksesta. Pöydän suunnassa kärryyn koskee vain lanka. Kärryn paino ja pöydän tukivoima ovat pystysuorat.
**Mallivastaus:** Punnuksen paino on Maan voima punnukseen. Se kuuluu punnuksen voimakuvioon. Lanka välittää punnuksen vaikutuksen kärryyn jännitysvoimana $T$. Se on kärryn ainoa voima pöydän suunnassa. Kärryn liikeyhtälö pöydän suunnassa on siis $T = m_1 a$. Kärry liikkuu eteenpäin, mutta liike ei ole voima. Liike-energiaa ei piirretä voimakuvioon. Punnus kiihtyy alas, joten jännitysvoima on pienempi kuin punnuksen paino: $T < m_2 g$.

## fy4-13-L2-05
**Annettu:** punnusten yhteinen massa $M = 0{,}500\,\text{kg}$. Taulukosta: $\Delta m = 50$; $100$; $150$; $200$ ja $250\,\text{g}$ sekä $a = 0{,}96$; $2{,}02$; $2{,}88$; $3{,}97$ ja $4{,}84\,\text{m/s}^2$ (esimerkkiaineisto).
**Kysytty:** a) kaava, jolla lasket $a$:n massaerosta $\Delta m$; b) putoamiskiihtyvyys $g$ yksikössä $\text{m/s}^2$
**Periaate:** Kirjoita kummallekin punnukselle oma liikeyhtälö. Lanka ei veny ja on kevyt. Siksi kiihtyvyyden suuruus $a$ ja jännitysvoima $T$ ovat molemmilla samat. Kun lasket yhtälöt yhteen, $T$ poistuu. Jäljelle jää suora verrannollisuus $a \propto \Delta m$. Suoran kulmakertoimesta saat $g$:n.
**Kuvaajan lukeminen:** Pisteet $(\Delta m, a)$ ovat lähes suoralla, joka kulkee origon kautta. Yksittäiset pisteet poikkeavat suorasta enintään noin $0{,}1\,\text{m/s}^2$. Se on mittauksen satunnaista vaihtelua. Origon kautta kulkeva sovitussuora osuu viimeisen pisteen kohdalla arvoon $a = 4{,}9\,\text{m/s}^2$, kun $\Delta m = 0{,}250\,\text{kg}$. Kulmakerroin on siis $k = \dfrac{4{,}9\,\text{m/s}^2}{0{,}250\,\text{kg}} = 19{,}6\,\dfrac{\text{m/s}^2}{\text{kg}}$.
**Kaava:** Kevyempi $m_1$ nousee ja raskaampi $m_2$ laskee: $T - m_1 g = m_1 a$ ja $m_2 g - T = m_2 a$. Yhteenlaskusta saadaan $(m_2 - m_1)\,g = (m_1 + m_2)\,a$, joten $a = \dfrac{g}{M}\,\Delta m$. Kulmakerroin on $k = \dfrac{g}{M}$, joten $g = k\,M$
**Muunnokset:** $\Delta m = 250\,\text{g} = 0{,}250\,\text{kg}$. Muut suureet ovat SI-yksiköissä.
**Sijoitus:** $g = 19{,}6\,\dfrac{\text{m/s}^2}{\text{kg}} \cdot 0{,}500\,\text{kg} = 9{,}8\,\text{m/s}^2$
**Vastaus:** $9{,}8\,\text{m/s}^2$. Vastauksessa on kaksi merkitsevää numeroa, koska käsin sovitetun suoran kulmakertoimen saa vain kahden numeron tarkkuudella.
**Järkevyys:** Tulos on lähellä tunnettua arvoa $9{,}81\,\text{m/s}^2$. Pisteiden suhteet $a : \Delta m$ ovat $19{,}2$; $20{,}2$; $19{,}2$; $19{,}9$ ja $19{,}4$ yksikössä $\dfrac{\text{m/s}^2}{\text{kg}}$. Kaikki ovat lähellä arvoa $19{,}6$. Kaavan mukaan $\Delta m = 250\,\text{g}$ antaa $a = \dfrac{0{,}250 \cdot 9{,}81}{0{,}500}\,\text{m/s}^2 = 4{,}9\,\text{m/s}^2$. Se on pienempi kuin $g$, kuten pitääkin.

## fy4-13-L2-06
**Annettu:** kärryn massa $m_1 = 1{,}20\,\text{kg}$. Mittauksessa, jossa punnuksen massa on $m_2 = 0{,}50\,\text{kg}$, kiihtyvyys on $a = 2{,}84\,\text{m/s}^2$ (esimerkkiaineisto). $g = 9{,}81\,\text{m/s}^2$. Kitka jätetään huomiotta. Lanka ja väkipyörä ovat kevyet.
**Kysytty:** langan jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Pöydän suunnassa kärryyn vaikuttaa vain lanka. Kärryn liikeyhtälöstä saat siis $T$:n suoraan mitatusta kiihtyvyydestä. Tarkista tulos laskemalla $T$ myös punnuksen liikeyhtälöstä. Siinä $T$ on painon vastasuuntainen.
**Kuvaajan lukeminen:** Taulukon rivi $m_2 = 0{,}50\,\text{kg}$ antaa $a = 2{,}84\,\text{m/s}^2$. Kiihtyvyys kasvaa, kun punnuksen massa kasvaa. Kasvu ei ole suoraan verrannollinen. Massa tulee viisinkertaiseksi ($0{,}10\,\text{kg} \to 0{,}50\,\text{kg}$), mutta kiihtyvyys tulee vain nelinkertaiseksi ($0{,}74 \to 2{,}84\,\text{m/s}^2$).
**Voimakuvio:** Piirrä kärry suorakulmioksi. Positiivinen suunta on langan suuntaan. Voimat $\overline{G}_1$ ja $\overline{N}$ kumoavat toisensa. Vaakasuunnassa vaikuttaa vain $\overline{T}_1$. Piirrä punnus suorakulmioksi. Positiivinen suunta on alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös.
```voimakuvio
pinta 0
G_1 11,77
N 11,77
T_1 3,41 oikea
a oikea
---
G_2 4,905
T_2 3,41 ylös
a alas
```
**Kaava:** Kärry: $T = m_1 a$. Punnus: $m_2 g - T = m_2 a$, joten tarkistus on $T = m_2\,(g - a)$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $T = 1{,}20\,\text{kg} \cdot 2{,}84\,\text{m/s}^2 = 3{,}408\,\text{N}$. Tarkistus: $T = 0{,}50\,\text{kg} \cdot (9{,}81\,\text{m/s}^2 - 2{,}84\,\text{m/s}^2) = 0{,}50\,\text{kg} \cdot 6{,}97\,\text{m/s}^2 = 3{,}485\,\text{N}$
**Vastaus:** $3{,}4\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa. Yhtälöt antavat $3{,}41\,\text{N}$ ja $3{,}49\,\text{N}$, jotka eroavat noin $2\,\%$. Siksi vain kaksi ensimmäistä numeroa on luotettavia.
**Järkevyys:** Kaksi tapaa antaa $3{,}4\,\text{N}$ ja $3{,}5\,\text{N}$. Ne eroavat noin $2\,\%$, mikä sopii mittauksen tarkkuuteen. Teorian mukaan $a = \dfrac{0{,}50 \cdot 9{,}81}{1{,}70}\,\text{m/s}^2 = 2{,}89\,\text{m/s}^2$. Mitattu $2{,}84\,\text{m/s}^2$ on hieman pienempi. Jännitysvoima on pienempi kuin punnuksen paino $4{,}9\,\text{N}$, kuten pitääkin.

## fy4-13-L2-07
**Annettu:** kärry $m_1 = 2{,}0\,\text{kg}$, punnus $m_2 = 0{,}50\,\text{kg}$ ja $g = 9{,}81\,\text{m/s}^2$. Kitka ja ilmanvastus jätetään huomiotta. Lanka ja väkipyörä ovat kevyet. Oppilaan tulos on $2{,}5\,\text{m/s}^2$.
**Kysytty:** oppilaan ratkaisun virhe ja oikea kiihtyvyys $a$ yksikössä $\text{m/s}^2$
**Periaate:** Kirjoita kummallekin kappaleelle oma liikeyhtälö. Kiihtyvyys koskee koko systeemiä: sekä kärryä että punnusta. Oppilaan yhtälöt $T = m_1 a$ ja $m_2 g - T = m_2 a$ ovat oikein, mutta ratkaisussa on virhe.
**Voimakuvio:** Piirrä kärry suorakulmioksi. Positiivinen suunta on oikealle. Voimat $\overline{G}_1$ ja $\overline{N}$ kumoavat toisensa. Vaakasuunnassa vaikuttaa vain $\overline{T}_1$. Piirrä punnus suorakulmioksi. Positiivinen suunta on alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös.
```voimakuvio
pinta 0
G_1 19,62
N 19,62
T_1 3,924 oikea
a oikea
---
G_2 4,905
T_2 3,924 ylös
a alas
```
**Kaava:** Virhe: sijoituksen jälkeen yhtälö on $m_2 g - m_1 a = m_2 a$. Myös punnuksen massa kuuluu nimittäjään: $m_2 g = m_1 a + m_2 a = (m_1 + m_2)\,a$. Oppilas unohti punnuksen massan. Pitää käyttää koko liikkuvan systeemin massaa $m_1 + m_2$. Oikein on $a = \dfrac{m_2 g}{m_1 + m_2}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{0{,}50\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{2{,}0\,\text{kg} + 0{,}50\,\text{kg}} = \dfrac{4{,}905\,\text{N}}{2{,}5\,\text{kg}} = 1{,}962\,\text{m/s}^2$
**Vastaus:** $2{,}0\,\text{m/s}^2$. Vastauksessa on kaksi merkitsevää numeroa, koska tiedoissa $2{,}0\,\text{kg}$ ja $0{,}50\,\text{kg}$ on kaksi. Oppilaan tulos oli liian suuri, koska hän jakoi vain kärryn massalla.
**Järkevyys:** Jännitysvoima $T = m_1 a = 2{,}0\,\text{kg} \cdot 1{,}962\,\text{m/s}^2 = 3{,}92\,\text{N}$ on pienempi kuin punnuksen paino $4{,}9\,\text{N}$. Erotus $0{,}98\,\text{N}$ on $m_2 a = 0{,}50\,\text{kg} \cdot 1{,}962\,\text{m/s}^2$. Oppilaan arvolla $a = 2{,}45\,\text{m/s}^2$ saisi $T = m_1 a = 4{,}9\,\text{N}$ ja $m_2 g - T \approx 0$. Punnuksen liikeyhtälö vaatisi kuitenkin $m_2 a = 1{,}2\,\text{N}$. Arvo on siis väärä.

## fy4-13-L3-04
**Annettu:** vaunujen massat $m_1 = 24\,\text{t}$, $m_2 = 18\,\text{t}$ ja $m_3 = 12\,\text{t}$. Taulukosta: nopeus on $v = 0$ hetkellä $t = 0$ ja $v = 10{,}02\,\text{m/s}$ hetkellä $t = 20{,}0\,\text{s}$ (esimerkkiaineisto). Kytkimen suurin sallittu voima on $20\,\text{kN}$. Vastusvoimat jätetään huomiotta.
**Kysytty:** a) junan kiihtyvyys $a$; b) vaunujen 1 ja 2 välisen kytkimen voima $K_{12}$ yksikössä $\text{kN}$; c) kytkimen voima, kun vaunut ovat järjestyksessä $12\,\text{t}$, $18\,\text{t}$, $24\,\text{t}$, ja kestääkö kytkin
**Periaate:** Vaunut on kytketty toisiinsa, joten ne liikkuvat yhdessä samalla kiihtyvyydellä $a$. Kirjoita kullekin vaunulle oma liikeyhtälö. Vaunujen 1 ja 2 välinen kytkin vetää vaunua 2 eteenpäin. Sen takana olevat vaunut 2 ja 3 vastustavat tätä. Siksi kytkimen voima kiihdyttää kaikkia vaunuja, jotka ovat sen takana. Kolmannen lain mukaan vaunu 2 vetää vaunua 1 taaksepäin yhtä suurella voimalla.
**Kuvaajan lukeminen:** Nopeus kasvaa tasaisesti noin $2{,}5\,\text{m/s}$ jokaisella viiden sekunnin välillä ($2{,}46$; $2{,}57$; $2{,}45$; $2{,}54\,\text{m/s}$). Siksi $(t, v)$-kuvaaja on lähes suora ja kiihtyvyys on vakio. Kulmakerroin päätepisteistä on $a = \dfrac{10{,}02\,\text{m/s} - 0}{20{,}0\,\text{s} - 0} = 0{,}50\,\text{m/s}^2$.
**Voimakuvio:** Veturin voima on merkitty $\overline{F}$. Piirrä vaunu 3 suorakulmioksi. Positiivinen suunta on junan liikkeen suuntaan. Vaakasuunnassa vaikuttaa vain kytkimen voima $\overline{K}_{23}$ eteenpäin. Vaunu 2: $\overline{K}_{12}$ eteenpäin ja $\overline{K}_{23}$ taaksepäin. Vaunu 1: veturin voima eteenpäin ja $\overline{K}_{12}$ taaksepäin. Jokaisessa vaunussa paino ja tukivoima kumoavat toisensa (kuvassa pystynuolet on piirretty lyhyinä). Nuolet $\overline{K}_{12}$ ovat yhtä pitkät vaunuissa 1 ja 2. Nuolet $\overline{K}_{23}$ ovat yhtä pitkät vaunuissa 2 ja 3 (kolmas laki). Nuoli $\overline{K}_{12}$ on pidempi kuin $\overline{K}_{23}$.
```voimakuvio
pinta 0
G_1 30
N 30
F 27 oikea
K_12 15 vasen
a oikea
```
```voimakuvio
pinta 0
G_2 22
N 22
K_12 15 oikea
K_23 6 vasen
a oikea
```
```voimakuvio
pinta 0
G_3 15
N 15
K_23 6 oikea
a oikea
```
**Kaava:** Vaunu 3: $K_{23} = m_3 a$. Vaunu 2: $K_{12} - K_{23} = m_2 a$. Yhteenlaskusta saadaan $K_{12} = (m_2 + m_3)\,a$
**Muunnokset:** $m_2 + m_3 = 18\,\text{t} + 12\,\text{t} = 30\,\text{t} = 30\,000\,\text{kg}$ ja $1\,\text{kN} = 1000\,\text{N}$.
**Sijoitus:** b) $K_{12} = 30\,000\,\text{kg} \cdot 0{,}50\,\text{m/s}^2 = 15\,000\,\text{N} = 15\,\text{kN}$
c) Uusi järjestys on $12\,\text{t}$, $18\,\text{t}$, $24\,\text{t}$. Vaunujen 1 ja 2 välisen kytkimen takana ovat $18\,\text{t}$ ja $24\,\text{t}$, yhteensä $42\,\text{t}$. Silloin $K_{12}' = 42\,000\,\text{kg} \cdot 0{,}50\,\text{m/s}^2 = 21\,000\,\text{N} = 21\,\text{kN}$
**Vastaus:** a) $a = 0{,}50\,\text{m/s}^2$. b) $15\,\text{kN}$. Vastauksessa on kaksi merkitsevää numeroa, koska tiedoissa $18\,\text{t}$ ja $12\,\text{t}$ on kaksi (vastauslaatikkoon tulee tämä). c) $21\,\text{kN}$. Kytkin, jonka raja on $20\,\text{kN}$, ei siis kestä uudessa järjestyksessä. Syy: kytkimen voima kiihdyttää kaikkia sen takana olevia vaunuja, ja raskain vaunu on nyt kytkimen takana.
**Järkevyys:** Alkuperäisessä järjestyksessä kytkimet ovat $K_{12} = 15\,\text{kN}$ ja $K_{23} = 12\,000\,\text{kg} \cdot 0{,}50\,\text{m/s}^2 = 6{,}0\,\text{kN}$. Veturin voima vaunuun 1 on $54\,000\,\text{kg} \cdot 0{,}50\,\text{m/s}^2 = 27\,\text{kN}$. Voima pienenee veturista taaksepäin, koska jokainen kytkin kiihdyttää yhä pienempää massaa. Vaunun 2 yhtälö täsmää: $15\,\text{kN} - 6{,}0\,\text{kN} = 9{,}0\,\text{kN} = 18\,000\,\text{kg} \cdot 0{,}50\,\text{m/s}^2$.

## fy4-13-L3-05
**Annettu:** matka $s = 0{,}80\,\text{m}$ levosta. Taulukosta: $m_2 = 0{,}100$; $0{,}200$; $0{,}300$ ja $0{,}400\,\text{kg}$ sekä ajat $t = 1{,}29$; $0{,}96$; $0{,}80$ ja $0{,}73\,\text{s}$ (esimerkkiaineisto). $g = 9{,}81\,\text{m/s}^2$. Kitka jätetään huomiotta. Lanka ja väkipyörä ovat kevyet.
**Kysytty:** a) kiihtyvyydet ja kaava $m_1$:lle; b) kärryn massan $m_1$ keskiarvo yksikössä $\text{kg}$; c) kärryn liike sen jälkeen, kun punnus osuu lattiaan, ja kärryn nopeus
**Periaate:** Kappaleet lähtevät levosta ja kiihtyvyys on vakio. Siksi $s = \tfrac{1}{2}at^2$ antaa kiihtyvyyden $a$ ajasta. Kirjoita kummallekin kappaleelle oma liikeyhtälö. Niistä saat $m_1$:n, kun tiedät $a$:n ja $m_2$:n. Kun lanka löystyy, kärryyn ei vaikuta vaakasuunnassa enää mikään voima. Silloin ensimmäinen laki ratkaisee kohdan c).
**Kuvaajan lukeminen:** Taulukosta luetaan neljä mittausta $(m_2, t)$. Aika lyhenee, kun punnus on painavampi. Se on järkevää, koska kiihtyvyys kasvaa.
**Voimakuvio:** Mittaus $m_2 = 0{,}200\,\text{kg}$, $a = 1{,}74\,\text{m/s}^2$. Piirrä kärry suorakulmioksi. Positiivinen suunta on oikealle (langan suuntaan). Voimat $\overline{G}_1$ ja $\overline{N}$ kumoavat toisensa. Vaakasuunnassa vaikuttaa vain $\overline{T}_1$ oikealle. Piirrä punnus suorakulmioksi. Positiivinen suunta on alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös.
```voimakuvio
pinta 0
G_1 8,92
N 8,92
T_1 1,6 oikea
a oikea
---
G_2 1,962
T_2 1,6 ylös
a alas
```
**Kaava:** a) $a = \dfrac{2s}{t^2}$. Kärry: $T = m_1 a$. Punnus: $m_2 g - T = m_2 a$. Sijoittamalla saadaan $m_2 g = m_1 a + m_2 a$, joten $m_1 = m_2 \left(\dfrac{g}{a} - 1\right)$. b) $m_{1,\text{ka}} = \dfrac{\Sigma m_1}{n}$. c) $v = at$ ja $s = \tfrac{1}{2}vt$, joten $v = \dfrac{2s}{t}$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** a) Kiihtyvyydet ovat $a = \dfrac{1{,}60\,\text{m}}{t^2}$: $0{,}961$; $1{,}736$; $2{,}500$ ja $3{,}002\,\text{m/s}^2$.
b) $m_1 = m_2 \left(\dfrac{g}{a} - 1\right)$ antaa kullekin mittaukselle
$m_1 = 0{,}100\,\text{kg} \cdot (10{,}20 - 1) = 0{,}920\,\text{kg}$,
$m_1 = 0{,}200\,\text{kg} \cdot (5{,}65 - 1) = 0{,}930\,\text{kg}$,
$m_1 = 0{,}300\,\text{kg} \cdot (3{,}924 - 1) = 0{,}877\,\text{kg}$ ja
$m_1 = 0{,}400\,\text{kg} \cdot (3{,}27 - 1) = 0{,}907\,\text{kg}$.
Massojen summa on $3{,}634\,\text{kg}$, joten $m_{1,\text{ka}} = \dfrac{3{,}634\,\text{kg}}{4} = 0{,}909\,\text{kg}$.
c) Kun $m_2 = 0{,}200\,\text{kg}$, $v = \dfrac{2 \cdot 0{,}80\,\text{m}}{0{,}96\,\text{s}} = 1{,}67\,\text{m/s}$.
**Vastaus:** b) $0{,}91\,\text{kg}$. Vastauksessa on kaksi merkitsevää numeroa, koska neljä arvoa vaihtelee välillä $0{,}88$–$0{,}93\,\text{kg}$. Kolmas numero ei ole luotettava. c) Kun punnus osuu lattiaan, lanka löystyy. Kärryyn ei vaikuta enää vaakasuuntaista voimaa. Ensimmäisen lain mukaan kärry jatkaa liikettä tasaisella nopeudella, noin $1{,}7\,\text{m/s}$, kunnes jokin muu voima vaikuttaa siihen.
**Järkevyys:** Neljä massaa ovat $0{,}88$–$0{,}93\,\text{kg}$. Ne poikkeavat keskiarvosta enintään $4\,\%$. Ero on satunnaista vaihtelua, ei suuntautunutta. Tarkistus: $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{0{,}200 \cdot 9{,}81}{1{,}109}\,\text{m/s}^2 = 1{,}77\,\text{m/s}^2$ on lähellä mitattua arvoa $1{,}74\,\text{m/s}^2$. Loppunopeus $1{,}67\,\text{m/s}$ on kaksinkertainen keskinopeuteen $s : t = 0{,}83\,\text{m/s}$ verrattuna, kuten tasaisesti kiihtyvässä liikkeessä pitääkin.

## fy4-13-L2-08
**Kysytty:** miten langan jännitysvoima $T$ muuttuu, kun kärryn ja punnuksen massat vaihdetaan keskenään, ja mikä perustelu selittää sen.
**Periaate:** Kummallekin kappaleelle kirjoitetaan oma liikeyhtälö: kärrylle $T = m_1 a$ ja punnukselle $m_2 g - T = m_2 a$. Kevyt ja venymätön lanka sekä kevyt ja kitkaton väkipyörä antavat kappaleille saman kiihtyvyyden suuruuden $a$ ja saman jännitysvoiman $T$. Yhtälöistä saadaan $a = \tfrac{m_2}{m_1 + m_2}\,g$ ja $T = \tfrac{m_1 m_2}{m_1 + m_2}\,g$.
**Mallivastaus:** Ensimmäisessä kokeessa $m_1 = 1{,}6\,\text{kg}$ ja $m_2 = 0{,}40\,\text{kg}$:

$$\begin{aligned}
&a = \frac{0{,}40\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{2{,}0\,\text{kg}} \\
&\phantom{a} = 1{,}962\,\text{m/s}^2 \\
&T = 1{,}6\,\text{kg} \cdot 1{,}962\,\text{m/s}^2 \\
&\phantom{T} \approx 3{,}14\,\text{N}
\end{aligned}$$

Toisessa kokeessa $m_1 = 0{,}40\,\text{kg}$ ja $m_2 = 1{,}6\,\text{kg}$:

$$\begin{aligned}
&a = \frac{1{,}6\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{2{,}0\,\text{kg}} \\
&\phantom{a} = 7{,}848\,\text{m/s}^2 \\
&T = 0{,}40\,\text{kg} \cdot 7{,}848\,\text{m/s}^2 \\
&\phantom{T} \approx 3{,}14\,\text{N}
\end{aligned}$$

Jännitysvoima pysyy siis samana, noin $3{,}1\,\text{N}$. Perustelu: kaavassa $T = \tfrac{m_1 m_2}{m_1 + m_2}\,g$ massojen tulo ja summa eivät muutu, kun massat vaihtavat paikkaa. Kiihtyvyys nelinkertaistuu, koska systeemiä kiihdyttävä punnuksen paino nelinkertaistuu. Siksi $T = m_1 a$ ei pienene, vaikka kärryn massa pienenee neljäsosaan. Kummassakin kokeessa $T$ on pienempi kuin punnuksen paino ($3{,}9\,\text{N}$ ja $15{,}7\,\text{N}$), kuten kiihtyvällä punnuksella pitääkin.

## fy4-13-L2-09
**Annettu:** kärryn massa $m_1 = 0{,}80\,\text{kg}$ ja kuvaajan mittauspisteet kärrylle, joka lähtee levosta. Kitka ja ilmanvastus jätetään huomiotta. Lanka ja väkipyörä ovat kevyet.
**Kysytty:** langan jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Vaakasuunnassa kärryyn vaikuttaa vain lanka. Kärryn liikeyhtälö $T = m_1 a$ antaa siksi jännitysvoiman, kun kiihtyvyys tunnetaan. Kiihtyvyys on $(t,v)$-kuvaajan kulmakerroin. Punnuksen massaa ei tarvita.
**Voimakuvio:** Piirrä kärry suorakulmioksi. Positiivinen suunta on langan suuntaan. Pystysuunnassa paino $\overline{G}_1$ ja tukivoima $\overline{N}$ kumoavat toisensa. Vaakasuunnassa vaikuttaa vain $\overline{T}_1$.
```voimakuvio
pinta 0
G_1 7,848
N 7,848
T_1 1,56 oikea
a oikea
```
**Kuvaajan lukeminen:** Pisteet ovat suoralla, joka kulkee origon kautta. Nopeus kasvaa joka puolen sekunnin välillä noin $1{,}0\,\text{m/s}$. Kiihtyvyys on siis vakio. Lue kaukaisin piste $(2{,}0\,\text{s};\, 3{,}9\,\text{m/s})$ ja alkupiste $(0\,\text{s};\, 0\,\text{m/s})$. Kaukainen piste antaa tarkimman kulmakertoimen.
**Kaava:** $a = \dfrac{\Delta v}{\Delta t}$ ja $T = m_1 a$
**Muunnokset:** Nopeudet ovat yksikössä $\text{m/s}$, ajat sekunteina ja massa kilogrammoina. Muunnoksia ei tarvita.
**Sijoitus:** $a = \dfrac{3{,}9\,\text{m/s} - 0\,\text{m/s}}{2{,}0\,\text{s} - 0\,\text{s}} = 1{,}95\,\text{m/s}^2$ ja $T = 0{,}80\,\text{kg} \cdot 1{,}95\,\text{m/s}^2 = 1{,}56\,\text{N}$
**Vastaus:** $T \approx 1{,}6\,\text{N}$. Vastauksessa on kaksi merkitsevää numeroa, koska massa $0{,}80\,\text{kg}$ ja luetut nopeudet ovat kahden numeron tarkkuudella.
**Järkevyys:** Kiihtyvyys $1{,}95\,\text{m/s}^2$ on pienempi kuin $g$. Niin pitääkin olla, koska punnus kiihdyttää myös kärryä. Arvio: noin $0{,}8\,\text{kg}$ ja noin $2\,\text{m/s}^2$ antavat noin $1{,}6\,\text{N}$.

## fy4-13-L3-06
**Annettu:** punnuksen massa $m_2 = 0{,}20\,\text{kg}$ ja kuvaajan mittauspisteet kärrylle, joka lähtee levosta; $g = 9{,}81\,\text{m/s}^2$. Kitka ja ilmanvastus jätetään huomiotta. Lanka ja väkipyörä ovat kevyet.
**Kysytty:** a) kärryn massa $m_1$ yksikössä $\text{kg}$; b) onko jännitysvoima $T$ suurempi, pienempi vai yhtä suuri kuin punnuksen paino $m_2 g$
**Periaate:** Kummallekin kappaleelle kirjoitetaan oma liikeyhtälö. Lanka on venymätön, joten kappaleilla on sama kiihtyvyyden suuruus $a$. Kevyt lanka ja kevyt kitkaton väkipyörä antavat samansuuruiset jännitysvoimat $T$. Kiihtyvyys luetaan kuvaajasta. Silloin kärryn massa on ainoa tuntematon.
**Voimakuvio:** Piirrä kärry suorakulmioksi. Positiivinen suunta on langan suuntaan. Voimat $\overline{G}_1$ ja $\overline{N}$ kumoavat toisensa, ja vaakasuunnassa vaikuttaa vain $\overline{T}_1$. Piirrä punnus suorakulmioksi. Positiivinen suunta on alas. Voima $\overline{G}_2$ osoittaa alas ja $\overline{T}_2$ ylös. Voima $\overline{T}_2$ on lyhyempi kuin $\overline{G}_2$.
```voimakuvio
pinta 0
G_1 7,907
N 7,907
T_1 1,572 oikea
a oikea
---
G_2 1,962
T_2 1,572 ylös
a alas
```
**Kuvaajan lukeminen:** Pisteet ovat suoralla, joka kulkee origon kautta. Kiihtyvyys on siis vakio. Kaukaisin piste $(2{,}0\,\text{s};\, 3{,}9\,\text{m/s})$ ja alkupiste $(0\,\text{s};\, 0\,\text{m/s})$ antavat kulmakertoimen $a = \dfrac{3{,}9\,\text{m/s}}{2{,}0\,\text{s}} = 1{,}95\,\text{m/s}^2$. Piste $(1{,}0\,\text{s};\, 2{,}0\,\text{m/s})$ antaa lähes saman, $2{,}0\,\text{m/s}^2$.
**Kaava:** Kärry: $T = m_1 a$. Punnus: $m_2 g - T = m_2 a$. Yhtälöistä saadaan $m_2 g = (m_1 + m_2)\,a$, joten $m_1 = m_2\left(\dfrac{g}{a} - 1\right)$
**Muunnokset:** Kaikki suureet ovat SI-yksiköissä. Muunnoksia ei tarvita.
**Sijoitus:** a) $m_1 = 0{,}20\,\text{kg} \cdot \left(\dfrac{9{,}81\,\text{m/s}^2}{1{,}95\,\text{m/s}^2} - 1\right) = 0{,}20\,\text{kg} \cdot 4{,}031 = 0{,}806\,\text{kg}$. b) $T = m_1 a = 0{,}806\,\text{kg} \cdot 1{,}95\,\text{m/s}^2 = 1{,}57\,\text{N}$ ja $m_2 g = 0{,}20\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 1{,}96\,\text{N}$
**Vastaus:** a) $m_1 \approx 0{,}81\,\text{kg}$. Vastauksessa on kaksi merkitsevää numeroa, koska punnuksen massa $0{,}20\,\text{kg}$ ja luettu kiihtyvyys ovat kahden numeron tarkkuudella. b) Jännitysvoima $1{,}6\,\text{N}$ on pienempi kuin punnuksen paino $2{,}0\,\text{N}$. Punnus kiihtyy alas, joten sen kokonaisvoima $m_2 g - T = m_2 a$ osoittaa alas. Siksi $T < m_2 g$. Jännitysvoima olisi painon suuruinen vain, jos kiihtyvyys olisi nolla.
**Järkevyys:** Kärryn massa on noin nelinkertainen punnukseen verrattuna. Tarkistus: $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{1{,}962\,\text{N}}{1{,}006\,\text{kg}} = 1{,}95\,\text{m/s}^2$. Tulos täsmää kuvaajasta luettuun arvoon.
