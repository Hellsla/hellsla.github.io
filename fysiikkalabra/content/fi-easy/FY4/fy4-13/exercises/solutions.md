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
