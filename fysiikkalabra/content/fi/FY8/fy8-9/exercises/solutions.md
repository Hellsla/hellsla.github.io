## fy8-9-L1-01
**Annettu:** alkuaktiivisuus $A_0 = 740\,\text{MBq}$, puoliintumisaika $T_{1/2} = 6{,}01\,\text{h}$, aika $t = 18{,}0\,\text{h}$
**Kysytty:** valmisteen aktiivisuus $A$ hetkellä $t$ megabecquereleinä
**Periaate:** Aktiivisuus on verrannollinen hajoamattomien ytimien määrään, $A = \lambda N$, joten se pienenee hajoamislain mukaan: jokainen puoliintumisaika puolittaa sen. Valmisteessa on valtavasti ytimiä, joten laki pätee tarkasti.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Ei tarvita: aika ja puoliintumisaika ovat molemmat tunteina, joten niiden suhde on paljas luku, ja aktiivisuus saadaan samassa yksikössä kuin $A_0$.
**Sijoitus:** $A = 740\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{18{,}0\,\text{h} / 6{,}01\,\text{h}} = 740\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{2{,}9950} = 740\,\text{MBq} \cdot 0{,}12543 = 92{,}82\,\text{MBq}$
**Vastaus:** $92{,}8\,\text{MBq}$, kolme merkitsevää numeroa kuten puoliintumisajassa $6{,}01\,\text{h}$ ja ajassa $18{,}0\,\text{h}$.
**Järkevyys:** Aikaa kului lähes tasan kolme puoliintumisaikaa, joten aktiivisuuden pitäisi olla noin kahdeksasosa alkuarvosta: $740\,\text{MBq} : 8 = 92{,}5\,\text{MBq}$. Tulos on hieman suurempi, koska kolmea puoliintumisaikaa puuttuu vielä vähän.

## fy8-9-L1-02
**Annettu:** puoliintumisaika $T_{1/2} = 3{,}82\,\text{d}$, aika $t = 10{,}0\,\text{d}$, astiaan ei synny uutta radonia
**Kysytty:** hajoamattomien radonytimien osuus $\tfrac{N}{N_0}$ prosentteina
**Periaate:** Radonytimet hajoavat toisistaan riippumatta, ja ilmanäytteessä niitä on hyvin paljon, joten niiden määrä noudattaa hajoamislakia. Koska uutta radonia ei synny, määrä vain pienenee.
**Kaava:** $N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, josta $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Ei tarvita: aika ja puoliintumisaika ovat molemmat vuorokausina. Lopuksi osuus muutetaan prosenteiksi: $1 = 100\,\%$.
**Sijoitus:** $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{10{,}0\,\text{d} / 3{,}82\,\text{d}} = \left(\tfrac{1}{2}\right)^{2{,}6178} = 0{,}16292 = 16{,}292\,\%$
**Vastaus:** $16{,}3\,\%$, kolme merkitsevää numeroa kuten puoliintumisajassa $3{,}82\,\text{d}$ ja ajassa $10{,}0\,\text{d}$.
**Järkevyys:** Aikaa kului vähän yli kaksi ja puoli puoliintumisaikaa. Kahden jälkeen jäljellä olisi $25\,\%$ ja kolmen jälkeen $12{,}5\,\%$; tulos on näiden välissä.

## fy8-9-L1-03
**Annettu:** cesium-137:n puoliintumisaika $T_{1/2} = 30{,}1\,\text{a}$
**Kysytty:** hajoamisvakio $\lambda$ yksikössä $\tfrac{1}{\text{a}}$
**Periaate:** Puoliintumisajan kohdalla hajoamattomia ytimiä on puolet, joten hajoamislain muodossa $N = N_0 e^{-\lambda t}$ on $e^{-\lambda T_{1/2}} = \tfrac{1}{2}$. Tästä saadaan hajoamisvakion ja puoliintumisajan yhteys.
**Kaava:** $\lambda T_{1/2} = \ln 2$, josta $\lambda = \dfrac{\ln 2}{T_{1/2}}$
**Muunnokset:** Ei tarvita: kun puoliintumisaika on vuosina, hajoamisvakio saadaan suoraan yksikössä $\tfrac{1}{\text{a}}$.
**Sijoitus:** $\lambda = \dfrac{0{,}69315}{30{,}1\,\text{a}} = 0{,}023028\,\tfrac{1}{\text{a}}$
**Vastaus:** $0{,}0230\,\tfrac{1}{\text{a}}$, kolme merkitsevää numeroa kuten puoliintumisajassa $30{,}1\,\text{a}$.
**Järkevyys:** Hajoamisvakio kertoo, että vuodessa hajoaa noin $2{,}3\,\%$ ytimistä. Silloin puolet hajoaa suunnilleen ajassa $0{,}69 : 0{,}023\,\tfrac{1}{\text{a}} \approx 30\,\text{a}$, mikä täsmää puoliintumisaikaan.

## fy8-9-L1-04
**Annettu:** hajoamattomien ytimien määrä $N = 3{,}20 \cdot 10^{12}$, hajoamisvakio $\lambda = 4{,}17 \cdot 10^{-9}\,\tfrac{1}{\text{s}}$
**Kysytty:** lähteen aktiivisuus $A$ kilobecquereleinä
**Periaate:** Jokainen ydin hajoaa sekunnissa todennäköisyydellä $\lambda$, joten $N$ ytimestä hajoaa sekunnissa keskimäärin $\lambda N$. Tämä on aktiivisuus.
**Kaava:** $A = \lambda N$
**Muunnokset:** $1\,\text{Bq} = 1\,\tfrac{1}{\text{s}}$ ja $1\,\text{kBq} = 1000\,\text{Bq}$.
**Sijoitus:** $A = 4{,}17 \cdot 10^{-9}\,\tfrac{1}{\text{s}} \cdot 3{,}20 \cdot 10^{12} = 13\,344\,\tfrac{1}{\text{s}} = 13\,344\,\text{Bq} = 13{,}344\,\text{kBq}$
**Vastaus:** $13{,}3\,\text{kBq}$, kolme merkitsevää numeroa kuten ytimien määrässä ja hajoamisvakiossa.
**Järkevyys:** Arviolla $4 \cdot 10^{-9} \cdot 3 \cdot 10^{12} = 1{,}2 \cdot 10^{4}$ eli noin $12\,\text{kBq}$. Ytimiä on paljon, mutta koboltti-60 hajoaa hitaasti, joten vain pieni osa ytimistä hajoaa sekunnissa.

## fy8-9-L1-05
**Annettu:** alkuaktiivisuus $A_0 = 800\,\text{kBq}$, aktiivisuus $A = 200\,\text{kBq}$ ajan $t = 48{,}0\,\text{h}$ kuluttua
**Kysytty:** puoliintumisaika $T_{1/2}$ tunteina
**Periaate:** Aktiivisuus puolittuu jokaisen puoliintumisajan aikana, koska se on verrannollinen hajoamattomien ytimien määrään. Lasketaan, montako puoliintumisaikaa mahtuu aikaan $t$: $800\,\text{kBq} \to 400\,\text{kBq} \to 200\,\text{kBq}$ on kaksi puolittumista.
**Kaava:** $\dfrac{A}{A_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}} = \tfrac{1}{4} = \left(\tfrac{1}{2}\right)^{2}$, joten $\tfrac{t}{T_{1/2}} = 2$ ja $T_{1/2} = \dfrac{t}{2}$
**Muunnokset:** Ei tarvita: aika on tunteina, ja vastaus kysytään tunteina.
**Sijoitus:** $T_{1/2} = \dfrac{48{,}0\,\text{h}}{2} = 24{,}0\,\text{h}$
**Vastaus:** $24{,}0\,\text{h}$, kolme merkitsevää numeroa kuten ajassa $48{,}0\,\text{h}$.
**Järkevyys:** Tarkistus hajoamislailla: $800\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{48{,}0\,\text{h} / 24{,}0\,\text{h}} = 800\,\text{kBq} \cdot \tfrac{1}{4} = 200\,\text{kBq}$, kuten tehtävässä.

## fy8-9-L1-06
**Kysytty:** mikä väite näytteen hajoamattomista ytimistä on oikein, kun $8{,}0\,\text{h}$ on kaksi puoliintumisaikaa ($T_{1/2} = 4{,}0\,\text{h}$).
**Periaate:** Jokaisessa puoliintumisajassa hajoaa puolet silloin jäljellä olevista ytimistä, ei puolta alkuperäisistä. Hajoaminen ei pysähdy eikä kiihdy, koska ytimellä ei ole muistia ja sen hajoamistodennäköisyys pysyy samana.
**Mallivastaus:** Oikea väite on se, jonka mukaan jäljellä on neljäsosa ytimistä, koska kumpikin puoliintumisaika poistaa puolet silloin jäljellä olevista. Ensimmäisen $4{,}0\,\text{h}$:n jälkeen jäljellä on $\tfrac{1}{2}$ ja toisen jälkeen $\tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4}$ alkuperäisistä ytimistä.

Väite, että kaikki ovat hajonneet, on virhe, koska toinen puoliintumisaika poistaa vain puolet jäljelle jääneistä. Väite hajoamisen pysähtymisestä on virheellinen, koska jäljellä olevat ytimet hajoavat edelleen samalla todennäköisyydellä. Väite iän vaikutuksesta on virheellinen, koska ytimen hajoamistodennäköisyys ei riipu sen iästä.

## fy8-9-L1-07
**Annettu:** puoliintumisaika $T_{1/2} = 28{,}8\,\text{a}$, aika $t = 144\,\text{a}$
**Kysytty:** hajoamatta olevien ytimien osuus $\tfrac{N}{N_0}$ prosentteina
**Periaate:** Jokainen puoliintumisaika puolittaa hajoamattomien ytimien määrän, joten osuus on $\left(\tfrac{1}{2}\right)^{t/T_{1/2}}$.
**Kaava:** $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Ei tarvita: aika ja puoliintumisaika ovat molemmat vuosina, joten niiden suhde on paljas luku. Osuus muutetaan lopuksi prosenteiksi kertomalla luvulla $100$.
**Sijoitus:** $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{144\,\text{a} : 28{,}8\,\text{a}} = \left(\tfrac{1}{2}\right)^{5{,}00} = \tfrac{1}{32} = 0{,}03125 = 3{,}125\,\%$
**Vastaus:** $3{,}13\,\%$, kolme merkitsevää numeroa kuten annetuissa arvoissa.
**Järkevyys:** Viiden puoliintumisajan jälkeen osuus on puolitettu viisi kertaa: $100\,\% \!\to\! 50\,\% \!\to\! 25\,\% \!\to\! 12{,}5\,\% \!\to\! 6{,}25\,\% \!\to\! 3{,}125\,\%$. Näyte ei ole tyhjä, mutta siitä on jäljellä enää pieni murto-osa.

## fy8-9-L1-08
**Annettu:** puoliintumisaika $T_{1/2} = 5{,}27\,\text{a}$, aktiivisuus $A = 0{,}100\,A_0$
**Kysytty:** aika $t$ vuosina
**Periaate:** Aktiivisuus noudattaa hajoamislakia, $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$. Kysytty aika on eksponentissa, joten se ratkaistaan logaritmin avulla.
**Kaava:** $\dfrac{A}{A_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, joten $\ln \dfrac{A_0}{A} = \dfrac{t}{T_{1/2}} \ln 2$ ja $t = T_{1/2} \cdot \dfrac{\ln (A_0 / A)}{\ln 2}$
**Muunnokset:** Ei tarvita: $\tfrac{A_0}{A} = \tfrac{1}{0{,}100} = 10{,}0$ on paljas luku, ja aika saadaan samassa yksikössä kuin puoliintumisaika eli vuosina.
**Sijoitus:** $t = 5{,}27\,\text{a} \cdot \dfrac{\ln 10{,}0}{0{,}69315} = 5{,}27\,\text{a} \cdot \dfrac{2{,}3026}{0{,}69315} = 5{,}27\,\text{a} \cdot 3{,}3219 = 17{,}51\,\text{a}$
**Vastaus:** $17{,}5\,\text{a}$, kolme merkitsevää numeroa kuten puoliintumisajassa $5{,}27\,\text{a}$.
**Järkevyys:** Kolmen puoliintumisajan jälkeen aktiivisuus on $\tfrac{1}{8} = 12{,}5\,\%$ ja neljän jälkeen $\tfrac{1}{16} = 6{,}25\,\%$. Aika, jolloin aktiivisuus on $10\,\%$, on näiden välissä: $3{,}32$ puoliintumisaikaa, eli $3{,}32 \cdot 5{,}27\,\text{a} \approx 17{,}5\,\text{a}$.

## fy8-9-L2-01
**Annettu:** jodi-131:n puoliintumisaika $T_{1/2} = 8{,}02\,\text{d}$
**Kysytty:** hajoamisvakio $\lambda$ yksikössä $10^{-6}\,\tfrac{1}{\text{s}}$
**Periaate:** Puoliintumisajan kohdalla $e^{-\lambda T_{1/2}} = \tfrac{1}{2}$, koska puolet ytimistä on hajonnut. Hajoamisvakio halutaan sekunteina, joten puoliintumisaika muutetaan ensin sekunneiksi.
**Kaava:** $\lambda T_{1/2} = \ln 2$, josta $\lambda = \dfrac{\ln 2}{T_{1/2}}$
**Muunnokset:** $1\,\text{d} = 24 \cdot 3600\,\text{s} = 86\,400\,\text{s}$, joten $T_{1/2} = 8{,}02 \cdot 86\,400\,\text{s} = 692\,928\,\text{s}$.
**Sijoitus:** $\lambda = \dfrac{0{,}69315}{692\,928\,\text{s}} = 1{,}00032 \cdot 10^{-6}\,\tfrac{1}{\text{s}}$
**Vastaus:** $1{,}00 \cdot 10^{-6}\,\tfrac{1}{\text{s}}$, kolme merkitsevää numeroa kuten puoliintumisajassa $8{,}02\,\text{d}$.
**Järkevyys:** Sekunnissa hajoaa noin miljoonasosa ytimistä, joten vuorokaudessa hajoaa noin $86\,400 \cdot 10^{-6} \approx 0{,}09$ eli $9\,\%$ jäljellä olevista. Koska $0{,}91^{8} \approx 0{,}47$, kahdeksan vuorokauden jälkeen jäljellä on noin puolet, mikä sopii puoliintumisaikaan $8{,}02\,\text{d}$.

## fy8-9-L2-02
**Annettu:** aktiivisuus $A = 37\,\text{kBq}$, amerikium-241:n puoliintumisaika $T_{1/2} = 433\,\text{a}$, $1\,\text{a} = 365{,}25\,\text{d}$
**Kysytty:** ytimien määrä $N$ yksikössä $10^{14}$
**Periaate:** Aktiivisuus on hajoamisvakion ja ytimien määrän tulo, $A = \lambda N$, ja hajoamisvakio saadaan puoliintumisajasta. Koska aktiivisuus on hajoamisia sekunnissa, hajoamisvakion on oltava yksikössä $\tfrac{1}{\text{s}}$.
**Kaava:** $A = \lambda N$ ja $\lambda = \dfrac{\ln 2}{T_{1/2}}$, joten $N = \dfrac{A}{\lambda} = \dfrac{A\,T_{1/2}}{\ln 2}$
**Muunnokset:** $A = 37\,\text{kBq} = 37 \cdot 10^{3}\,\tfrac{1}{\text{s}}$ ja $T_{1/2} = 433 \cdot 365{,}25 \cdot 86\,400\,\text{s} = 1{,}36644 \cdot 10^{10}\,\text{s}$.
**Sijoitus:** $N = \dfrac{37 \cdot 10^{3}\,\tfrac{1}{\text{s}} \cdot 1{,}36644 \cdot 10^{10}\,\text{s}}{0{,}69315} = 7{,}294 \cdot 10^{14}$
**Vastaus:** $7{,}3 \cdot 10^{14}$ ydintä, kaksi merkitsevää numeroa kuten aktiivisuudessa $37\,\text{kBq}$.
**Järkevyys:** Hajoamisvakio on $\lambda = 5{,}07 \cdot 10^{-11}\,\tfrac{1}{\text{s}}$, ja $5{,}07 \cdot 10^{-11}\,\tfrac{1}{\text{s}} \cdot 7{,}29 \cdot 10^{14} \approx 3{,}7 \cdot 10^{4}\,\tfrac{1}{\text{s}}$, mikä on annettu aktiivisuus. Ytimiä on paljon, koska pitkäikäinen amerikium hajoaa hitaasti; massana tämä on vain noin $0{,}3\,\mu\text{g}$.

## fy8-9-L2-03
**Annettu:** alkuaktiivisuus $A_0 = 2{,}00\,\text{GBq}$, matkan kesto $t = 2\,\text{h}\ 30\,\text{min}$, fluori-18:n puoliintumisaika $T_{1/2} = 110\,\text{min}$
**Kysytty:** aktiivisuus $A$ perillä megabecquereleinä
**Periaate:** Aktiivisuus noudattaa hajoamislakia, koska se on verrannollinen hajoamattomien ytimien määrään. Aika ja puoliintumisaika on ilmaistava samassa yksikössä, jotta eksponentti on paljas luku.
**Kaava:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** $t = 2\,\text{h}\ 30\,\text{min} = 2 \cdot 60\,\text{min} + 30\,\text{min} = 150\,\text{min}$ ja $A_0 = 2{,}00\,\text{GBq} = 2000\,\text{MBq}$.
**Sijoitus:** $A = 2000\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{150\,\text{min} / 110\,\text{min}} = 2000\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{1{,}3636} = 2000\,\text{MBq} \cdot 0{,}38860 = 777{,}20\,\text{MBq}$
**Vastaus:** $777\,\text{MBq}$, kolme merkitsevää numeroa kuten alkuaktiivisuudessa $2{,}00\,\text{GBq}$ ja puoliintumisajassa $110\,\text{min}$.
**Järkevyys:** Matka kesti vähän yli yhden puoliintumisajan, joten aktiivisuuden pitäisi olla hieman alle puolet alkuarvosta, eli alle $1000\,\text{MBq}$. Kahden puoliintumisajan jälkeen se olisi $500\,\text{MBq}$; tulos on näiden välissä.

## fy8-9-L2-04
**Annettu:** alkumassa $m_0 = 5{,}00\,\text{mg}$, puoliintumisaika $T_{1/2} = 5{,}27\,\text{a}$, aika $t = 15{,}0\,\text{a}$
**Kysytty:** jäljellä olevan koboltti-60:n massa $m$ milligrammoina
**Periaate:** Jokaisella koboltti-60-ytimellä on sama massa, joten hajoamattoman koboltin massa on verrannollinen hajoamattomien ytimien määrään ja noudattaa samaa hajoamislakia kuin $N$.
**Kaava:** $N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ ja $m \propto N$, joten $m = m_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Muunnokset:** Ei tarvita: aika ja puoliintumisaika ovat vuosina, ja massa saadaan milligrammoina.
**Sijoitus:** $m = 5{,}00\,\text{mg} \cdot \left(\tfrac{1}{2}\right)^{15{,}0\,\text{a} / 5{,}27\,\text{a}} = 5{,}00\,\text{mg} \cdot \left(\tfrac{1}{2}\right)^{2{,}8463} = 5{,}00\,\text{mg} \cdot 0{,}13905 = 0{,}69526\,\text{mg}$
**Vastaus:** $0{,}695\,\text{mg}$, kolme merkitsevää numeroa kuten alkumassassa $5{,}00\,\text{mg}$ ja puoliintumisajassa $5{,}27\,\text{a}$.
**Järkevyys:** Aikaa kului vajaat kolme puoliintumisaikaa, joten massan pitäisi olla hieman yli kahdeksasosa alkuperäisestä: $5{,}00\,\text{mg} : 8 = 0{,}625\,\text{mg}$. Hajonneiden ytimien tilalle tulee nikkeli-60:tä, joten lähteen kokonaismassa ei juuri muutu.

## fy8-9-L2-05
**Annettu:** pulssimäärät $10\,\text{s}$:n jaksoissa taulukossa, tausta $8$ pulssia $10\,\text{s}$:n jaksossa
**Kysytty:** puoliintumisaika $T_{1/2}$ sekunteina
**Periaate:** Mittari laskee sekä näytteen että taustan pulsseja. Vain näytteen osuus pienenee hajoamislain mukaan, joten tausta vähennetään ensin. Mittauspisteet vaihtelevat satunnaisesti, joten puoliintumisaika luetaan kahden pisteen kautta, jotka ovat kaukana toisistaan.
**Kaava:** $\dfrac{R}{R_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, joten $T_{1/2} = \dfrac{t \ln 2}{\ln (R_0 / R)}$, missä $R_0$ ja $R$ ovat nettopulssimäärät
**Muunnokset:** a) Nettopulssimäärät ovat $291 - 8 = 283$, $250 - 8 = 242$, $204 - 8 = 196$, $178 - 8 = 170$, $143 - 8 = 135$, $126 - 8 = 118$, $103 - 8 = 95$, $90 - 8 = 82$, $72 - 8 = 64$, $66 - 8 = 58$ ja $51 - 8 = 43$ ($t = 0, 40, \ldots, 400\,\text{s}$). Aikayksikkö on sekunti kuten vastauksessakin, joten muita muunnoksia ei tarvita.
**Sijoitus:** b) Alussa $R_0 = 283$ ja $t = 320\,\text{s}$:n kohdalla $R = 64$. Suhde on $\tfrac{283}{64} = 4{,}42$, eli hieman yli kaksi puoliintumisaikaa ($2^2 = 4$), ja $64$ on noin $23\,\%$ luvusta $283$. Siis $T_{1/2} = \dfrac{320\,\text{s} \cdot 0{,}69315}{\ln 4{,}42} = \dfrac{221{,}8\,\text{s}}{1{,}4865} = 149{,}2\,\text{s}$
**Vastaus:** $149\,\text{s}$ eli noin $150\,\text{s}$. Kahden pisteen arvion tarkkuus on noin $\pm 8\,\%$, koska nettomäärän $64$ hajonta on noin $\sqrt{64} = 8$.
**Järkevyys:** Alkuarvon puolikas on $\tfrac{283}{2} = 141{,}5$. Taulukossa nettopulssimäärä on $170$ ajanhetkellä $120\,\text{s}$ ja $135$ hetkellä $160\,\text{s}$, joten puolittuminen tapahtuu noin $150\,\text{s}$:n kohdalla. Se sopii tulokseen. Pisteet eivät ole täsmälleen käyrällä, koska pulssimäärät vaihtelevat satunnaisesti.

## fy8-9-L2-06
**Annettu:** taulukon pulssimäärät $10\,\text{s}$:n jaksoissa, tausta $20$ pulssia $10\,\text{s}$:n jaksossa, oppilaan tulos $70\,\text{s}$
**Kysytty:** a) puoliintumisaika $T_{1/2}$ sekunteina, b) miksi oppilaan tulos on liian suuri
**Periaate:** Vain näytteen aiheuttama nettopulssimäärä pienenee hajoamislain mukaan. Tausta pysyy samana koko mittauksen ajan, joten se on vähennettävä ennen puolittumisen etsimistä.
**Kaava:** $R = R_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, joten kahden puoliintumisajan kohdalla $R = \tfrac{R_0}{4}$, missä $R_0$ ja $R$ ovat nettopulssimäärät
**Muunnokset:** Nettopulssimäärät ovat $200 - 20 = 180$, $148 - 20 = 128$, $108 - 20 = 88$, $84 - 20 = 64$, $65 - 20 = 45$, $50 - 20 = 30$ ja $43 - 20 = 23$ ($t = 0, 30, \ldots, 180\,\text{s}$). Ei muita muunnoksia: aika on sekunteina kuten vastauksessakin.
**Sijoitus:** a) Alussa $R_0 = 180$, ja neljäsosa siitä on $\tfrac{180}{4} = 45$. Se saavutetaan hetkellä $t = 120\,\text{s}$, joten $2\,T_{1/2} = 120\,\text{s}$ ja $T_{1/2} = \dfrac{120\,\text{s}}{2} = 60\,\text{s}$.
**Vastaus:** $60\,\text{s}$, kaksi merkitsevää numeroa. Tarkistus: nettomäärä on puolittunut hetkeen $60\,\text{s}$ mennessä, koska siinä kohdassa se on $88$ ja alkuarvon puolikas on $90$.
**Järkevyys:** a) Tulos $60\,\text{s}$ sopii taulukkoon: nettomäärä $88$ on lähellä alkuarvon puolikasta $90$.

**Selitys kohtaan b):** Oppilas puolitti mitatun kokonaispulssimäärän $200$. Siitä $20$ pulssia on taustaa, joka ei hajoa, joten kokonaismäärä ei puolitu samassa ajassa kuin nettomäärä: kun nettomäärä on $90$, kokonaismäärä on vielä $110$. Mitattu määrä saavuttaa arvon $100$ vasta myöhemmin, noin $70\,\text{s}$:n kohdalla, ja tulos on liian suuri. Tausta hidastaa kokonaispulssimäärän pienenemistä ja siirtää kokonaismäärän puolittumisen myöhemmäksi.

## fy8-9-L2-07
**Annettu:** taustan pulssimäärien summa $80$ kymmenessä $10\,\text{s}$:n jaksossa, näytteen kanssa $340$ pulssia yhdessä $10\,\text{s}$:n jaksossa, jaksoja $n = 10$
**Kysytty:** nettopulssitaajuus $R$ pulsseina sekunnissa (ja a) taustan keskiarvo, c) suhteellinen hajonta)
**Periaate:** Mittari laskee sekä taustan että näytteen pulssit. Näytteen oma osuus saadaan vähentämällä keskimääräinen tausta kokonaismäärästä. Pulssimäärä on satunnainen, ja sen hajonta on suunnilleen $\sqrt{N}$.
**Kaava:** Taustan keskiarvo $N_\text{tausta} = \dfrac{\text{summa}}{n}$, nettopulssimäärä $N_\text{netto} = N - N_\text{tausta}$ ja pulssitaajuus $R = \dfrac{N_\text{netto}}{\Delta t}$
**Muunnokset:** Jakson pituus on $\Delta t = 10\,\text{s}$, joten pulssimäärä jaetaan kymmenellä, jotta saadaan pulssia sekunnissa.
**Sijoitus:** a) Taustan pulssimäärien summa on $80$, joten keskiarvo on $N_\text{tausta} = \dfrac{80}{10} = 8{,}0$ pulssia $10\,\text{s}$:ssa. b) $N_\text{netto} = 340 - 8{,}0 = 332$ ja $R = \dfrac{332}{10\,\text{s}} = 33{,}2\,\tfrac{1}{\text{s}}$. c) Hajonta on $\sqrt{340} = 18{,}4$, joten suhteellinen hajonta on $\dfrac{18{,}4}{340} = 0{,}0542 = 5{,}4\,\%$.
**Vastaus:** $33{,}2\,\tfrac{1}{\text{s}}$, kolme merkitsevää numeroa kuten nettopulssimäärässä $332$.
**Järkevyys:** Taustan vaihtelu $5$–$11$ pulssia tarkoittaa enintään noin $\pm 3$ pulssin poikkeamaa keskiarvosta $8{,}0$. Se on alle prosentti pulssimäärästä $340$, kun taas näytteen oman pulssimäärän hajonta on noin $18$ pulssia. Näytteen mittauksen satunnaisuus hallitsee epävarmuutta, eikä taustan vaihtelu muuta nettotulosta merkittävästi.

## fy8-9-L3-01
**Annettu:** näytteen aktiivisuus on $38{,}0\,\%$ elävän puun aktiivisuudesta grammaa hiiltä kohti, hiili-14:n puoliintumisaika $T_{1/2} = 5700\,\text{a}$
**Kysytty:** puun kuolemasta kulunut aika $t$ vuosina
**Periaate:** Elävässä puussa hiili-14:n osuus pysyy vakiona, joten kuolinhetkellä aktiivisuus grammaa kohti oli sama kuin elävässä puussa. Sen jälkeen aktiivisuus on pienentynyt hajoamislain mukaan. Kun osuus $\tfrac{A}{A_0}$ tunnetaan, kulunut aika ratkaistaan eksponentista logaritmin avulla.
**Kaava:** $\dfrac{A}{A_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, joten $\ln \dfrac{A_0}{A} = \dfrac{t}{T_{1/2}} \ln 2$ ja $t = T_{1/2} \cdot \dfrac{\ln (A_0 / A)}{\ln 2}$
**Muunnokset:** Ei tarvita: $\tfrac{A_0}{A} = \tfrac{100\,\%}{38{,}0\,\%}$ on paljas luku, ja aika saadaan samassa yksikössä kuin puoliintumisaika eli vuosina.
**Sijoitus:** $t = 5700\,\text{a} \cdot \dfrac{\ln 2{,}6316}{0{,}69315} = 5700\,\text{a} \cdot \dfrac{0{,}96758}{0{,}69315} = 5700\,\text{a} \cdot 1{,}3959 = 7957\,\text{a}$
**Vastaus:** $7960\,\text{a}$ eli noin $7{,}96 \cdot 10^{3}\,\text{a}$, kolme merkitsevää numeroa kuten osuudessa $38{,}0\,\%$.
**Järkevyys:** Yhden puoliintumisajan jälkeen aktiivisuutta olisi $50\,\%$ ja kahden jälkeen $25\,\%$. $38\,\%$ on näiden välissä, joten iän pitää olla $5700$–$11\,400$ vuotta. Tulos $1{,}40$ puoliintumisaikaa sopii tähän.

## fy8-9-L3-02
**Annettu:** pulssitaajuus alussa $820$ pulssia minuutissa ja $t = 10{,}0\,\text{min}$ myöhemmin $230$ pulssia minuutissa, taustasäteily $30$ pulssia minuutissa
**Kysytty:** puoliintumisaika $T_{1/2}$ minuutteina
**Periaate:** Mittari laskee sekä näytteen että ympäristön säteilyä. Vain näytteen osuus on verrannollinen sen aktiivisuuteen ja pienenee hajoamislain mukaan, joten tausta vähennetään ensin. Taustan oletetaan pysyvän samana koko mittauksen ajan.
**Kaava:** $\dfrac{R_1}{R_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, joten $\ln \dfrac{R_0}{R_1} = \dfrac{t}{T_{1/2}} \ln 2$ ja $T_{1/2} = \dfrac{t \ln 2}{\ln (R_0 / R_1)}$, missä $R_0$ ja $R_1$ ovat näytteen nettopulssitaajuudet
**Muunnokset:** Ei yksikkömuunnoksia: pulssitaajuuksien suhde on paljas luku, ja aika on minuutteina. Nettopulssitaajuudet: $R_0 = 820 - 30 = 790$ ja $R_1 = 230 - 30 = 200$ pulssia minuutissa.
**Sijoitus:** $T_{1/2} = \dfrac{10{,}0\,\text{min} \cdot 0{,}69315}{\ln (790 : 200)} = \dfrac{6{,}9315\,\text{min}}{\ln 3{,}95} = \dfrac{6{,}9315\,\text{min}}{1{,}3737} = 5{,}0458\,\text{min}$
**Vastaus:** $5{,}05\,\text{min}$, kolme merkitsevää numeroa kuten ajassa $10{,}0\,\text{min}$.
**Järkevyys:** Nettopulssitaajuus pieneni $790$:stä $200$:aan eli lähes neljäsosaan, joten $10\,\text{min}$ on vähän alle kaksi puoliintumisaikaa ja puoliintumisaika vähän yli $5\,\text{min}$. Ilman taustan vähentämistä suhde olisi $820 : 230 = 3{,}57$, ja puoliintumisaika olisi virheellisesti noin $5{,}5\,\text{min}$.

## fy8-9-L3-03
**Annettu:** aktiivisuudet aluksi yhtä suuret $A_\text{I,0} = A_\text{Cs,0} = A_0$, jodi-131:n puoliintumisaika $8{,}02\,\text{d}$, cesium-137:n $30{,}1\,\text{a}$, aika $t = 30{,}0\,\text{d}$, $1\,\text{a} = 365{,}25\,\text{d}$
**Kysytty:** jodi-131:n osuus kokonaisaktiivisuudesta prosentteina
**Periaate:** Kumpikin isotooppi hajoaa omalla puoliintumisajallaan toisesta riippumatta, ja kummankin aktiivisuus noudattaa hajoamislakia. Kokonaisaktiivisuus on niiden summa. Koska alkuaktiivisuudet ovat yhtä suuret, $A_0$ supistuu osuudesta pois.
**Kaava:** $A_\text{I} = A_0 \left(\tfrac{1}{2}\right)^{t/T_\text{I}}$ ja $A_\text{Cs} = A_0 \left(\tfrac{1}{2}\right)^{t/T_\text{Cs}}$, joten osuus on $p = \dfrac{A_\text{I}}{A_\text{I} + A_\text{Cs}} = \dfrac{\left(\tfrac{1}{2}\right)^{t/T_\text{I}}}{\left(\tfrac{1}{2}\right)^{t/T_\text{I}} + \left(\tfrac{1}{2}\right)^{t/T_\text{Cs}}}$
**Muunnokset:** $T_\text{Cs} = 30{,}1\,\text{a} = 30{,}1 \cdot 365{,}25\,\text{d} = 10\,994\,\text{d}$, jotta kaikki ajat ovat vuorokausina.
**Sijoitus:** $\left(\tfrac{1}{2}\right)^{30{,}0\,\text{d} / 8{,}02\,\text{d}} = \left(\tfrac{1}{2}\right)^{3{,}7406} = 0{,}074809$ ja $\left(\tfrac{1}{2}\right)^{30{,}0\,\text{d} / 10\,994\,\text{d}} = \left(\tfrac{1}{2}\right)^{0{,}0027288} = 0{,}99811$, joten $p = \dfrac{0{,}074809}{0{,}074809 + 0{,}99811} = \dfrac{0{,}074809}{1{,}07292} = 0{,}069725 = 6{,}9725\,\%$
**Vastaus:** $6{,}97\,\%$, kolme merkitsevää numeroa kuten puoliintumisajoissa ja ajassa $30{,}0\,\text{d}$.
**Järkevyys:** Kuukaudessa kuluu lähes neljä jodin puoliintumisaikaa, joten jodin aktiivisuus on pudonnut alle kymmenesosaan, kun taas cesiumin aktiivisuus on lähes ennallaan. Jodin osuuden on siis oltava alle $10\,\%$ mutta yli nollan, kuten tulos on. Siksi onnettomuuden jälkeen jodi on suuri ongelma ensimmäiset viikot, cesium vuosikymmeniä.

## fy8-9-L3-04
**Annettu:** lyhytikäisen nuklidin $T_{1/2} = 6{,}0\,\text{h}$, kokonaisaktiivisuus taulukossa, $A = A_1 + A_2$
**Kysytty:** a) pitkäikäisen nuklidin puoliintumisaika vuorokausina, b) sen alkuaktiivisuus ja lyhytikäisen osuus alussa, c) $6{,}0\,\text{h}$:n tarkistus
**Periaate:** Kumpikin nuklidi noudattaa omaa hajoamislakiaan, ja kokonaisaktiivisuus on niiden summa. Lyhytikäisen aktiivisuus on viimeisissä mittauksissa pudonnut lähes nollaan: hetkellä $96\,\text{h}$ on kulunut $\tfrac{96}{6{,}0} = 16$ puoliintumisaikaa, ja $\left(\tfrac{1}{2}\right)^{16} \approx 1{,}5 \cdot 10^{-5}$. Siksi myöhäiset pisteet kuvaavat vain pitkäikäistä nuklidia.
**Kaava:** $\dfrac{A_2(t_2)}{A_2(t_1)} = \left(\tfrac{1}{2}\right)^{(t_2 - t_1)/T_2}$, joten $T_2 = \dfrac{(t_2 - t_1) \ln 2}{\ln \left(A_2(t_1) / A_2(t_2)\right)}$
**Muunnokset:** Pisteet $t_1 = 96\,\text{h}$ ja $t_2 = 168\,\text{h}$ ovat $\Delta t = 72\,\text{h}$ päässä toisistaan. Tulos muutetaan vuorokausiksi jakamalla luvulla $24\,\tfrac{\text{h}}{\text{d}}$.
**Sijoitus:** a) $A(96\,\text{h}) = 71{,}2\,\text{MBq}$ ja $A(168\,\text{h}) = 32{,}8\,\text{MBq}$, joten $T_2 = \dfrac{72\,\text{h} \cdot 0{,}69315}{\ln (71{,}2 : 32{,}8)} = \dfrac{49{,}907\,\text{h}}{0{,}7752} = 64{,}38\,\text{h} = \dfrac{64{,}38\,\text{h}}{24\,\text{h/d}} = 2{,}683\,\text{d}$. b) Aktiivisuus hetkellä $t = 0$ on $A_2(0) = 71{,}2\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{-96/64{,}38} = 71{,}2\,\text{MBq} \cdot 2^{1{,}491} = 71{,}2\,\text{MBq} \cdot 2{,}811 = 200\,\text{MBq}$. Kokonaisaktiivisuus alussa on $1000\,\text{MBq}$, joten lyhytikäisen aktiivisuus on $1000\,\text{MBq} - 200\,\text{MBq} = 800\,\text{MBq}$ eli $80\,\%$ kokonaisaktiivisuudesta. c) Hetkellä $12\,\text{h}$ pitkäikäisen aktiivisuus on $200\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{12/64{,}38} = 200\,\text{MBq} \cdot 0{,}879 = 175{,}8\,\text{MBq}$. Lyhytikäisen aktiivisuus on silloin $376\,\text{MBq} - 175{,}8\,\text{MBq} = 200{,}2\,\text{MBq}$. Alkuaktiivisuus $800\,\text{MBq}$ on puolittunut kaksi kertaa ($12\,\text{h} = 2 \cdot 6{,}0\,\text{h}$): $\tfrac{800\,\text{MBq}}{4} = 200\,\text{MBq}$, mikä täsmää.
**Vastaus:** $2{,}68\,\text{d}$, kolme merkitsevää numeroa kuten taulukon aktiivisuuksissa.
**Järkevyys:** Tulos $2{,}68\,\text{d} = 64{,}4\,\text{h}$ on paljon pidempi kuin $6{,}0\,\text{h}$, kuten tehtävä edellyttää. Kolmannella pisteparilla tulos pysyy samana: $A(120\,\text{h}) = 55{,}9\,\text{MBq}$ ja $A(168\,\text{h}) = 32{,}8\,\text{MBq}$ antavat $T_2 = \tfrac{48\,\text{h} \cdot 0{,}69315}{\ln 1{,}704} = 62{,}4\,\text{h} \approx 2{,}6\,\text{d}$, joka on lähellä tulosta, kun otetaan huomioon mittauspisteiden satunnainen vaihtelu.

## fy8-9-L3-05
**Annettu:** kehon jodi-131-aktiivisuus taulukossa ($400\,\text{MBq} \to 65{,}5\,\text{MBq}$ kahdeksassa vuorokaudessa), fysikaalinen puoliintumisaika $T_\text{fys} = 8{,}02\,\text{d}$, $\lambda_\text{eff} = \lambda_\text{fys} + \lambda_\text{bio}$
**Kysytty:** a) efektiivinen puoliintumisaika $T_\text{eff}$, b) biologinen puoliintumisaika $T_\text{bio}$ vuorokausina, c) jäljellä oleva osuus pelkällä fysikaalisella hajoamisella ja se, kumpi prosessi pienentää aktiivisuutta nopeammin
**Periaate:** Mitattu aktiivisuus pienenee hajoamislain mukaan efektiivisellä puoliintumisajalla, koska sekä hajoaminen että poistuminen vähentävät kehon jodia. Hajoamisvakiot lasketaan yhteen, ja $\lambda = \tfrac{\ln 2}{T_{1/2}}$ antaa puoliintumisajat. Biologinen vakio saadaan vähentämällä fysikaalinen kokonaisvakiosta.
**Kaava:** $T_\text{eff} = \dfrac{t \ln 2}{\ln (A_0 / A)}$ ja $\lambda_\text{bio} = \lambda_\text{eff} - \lambda_\text{fys}$, eli $\dfrac{1}{T_\text{bio}} = \dfrac{1}{T_\text{eff}} - \dfrac{1}{T_\text{fys}}$
**Muunnokset:** Kaikki ajat ovat vuorokausina, joten yksikkömuunnoksia ei tarvita. Yhtälö $\lambda = \tfrac{\ln 2}{T_{1/2}}$ jaettuna luvulla $\ln 2$ antaa $\tfrac{1}{T_\text{bio}} = \tfrac{1}{T_\text{eff}} - \tfrac{1}{T_\text{fys}}$.
**Sijoitus:** a) $T_\text{eff} = \dfrac{8{,}0\,\text{d} \cdot 0{,}69315}{\ln (400 : 65{,}5)} = \dfrac{5{,}545\,\text{d}}{1{,}8092} = 3{,}065\,\text{d}$. b) $\dfrac{1}{T_\text{bio}} = \dfrac{1}{3{,}065\,\text{d}} - \dfrac{1}{8{,}02\,\text{d}} = 0{,}3263\,\tfrac{1}{\text{d}} - 0{,}1247\,\tfrac{1}{\text{d}} = 0{,}2016\,\tfrac{1}{\text{d}}$, joten $T_\text{bio} = \dfrac{1}{0{,}2016\,\tfrac{1}{\text{d}}} = 4{,}96\,\text{d}$. c) Pelkällä hajoamisella jäljellä olisi $100\,\% \cdot \left(\tfrac{1}{2}\right)^{8{,}0/8{,}02} = 100\,\% \cdot 0{,}5008 = 50{,}1\,\%$. Mitattu osuus on $\tfrac{65{,}5}{400} = 16{,}4\,\%$. Kumpikin prosessi vaikuttaa kaikkiin ytimiin, joten nopeampi prosessi on se, jonka hajoamisvakio on suurempi: $\lambda_\text{bio} = \tfrac{0{,}69315}{4{,}96\,\text{d}} = 0{,}140\,\tfrac{1}{\text{d}}$ ja $\lambda_\text{fys} = \tfrac{0{,}69315}{8{,}02\,\text{d}} = 0{,}0864\,\tfrac{1}{\text{d}}$.
**Vastaus:** $T_\text{bio} = 4{,}96\,\text{d}$, kolme merkitsevää numeroa kuten taulukon arvoissa.
**Järkevyys:** Biologinen puoliintumisaika on lyhyempi kuin fysikaalinen, joten poistuminen on nopeampi prosessi ja efektiivinen aika on lyhyempi kuin kumpikaan: $3{,}07\,\text{d} < 4{,}96\,\text{d} < 8{,}02\,\text{d}$. Tarkistus: $\lambda_\text{eff} = \tfrac{0{,}69315}{3{,}065\,\text{d}} = 0{,}2262\,\tfrac{1}{\text{d}}$ ja $\lambda_\text{fys} + \lambda_\text{bio} = 0{,}0864\,\tfrac{1}{\text{d}} + 0{,}1398\,\tfrac{1}{\text{d}} = 0{,}2262\,\tfrac{1}{\text{d}}$. Kohdan c) perusteella biologinen poistuminen pienentää kehon jodi-131-aktiivisuutta nopeammin kuin fysikaalinen hajoaminen, koska $\lambda_\text{bio} > \lambda_\text{fys}$. Yhdessä ne jättävät jäljelle vain $16{,}4\,\%$ eikä pelkän hajoamisen $50{,}1\,\%$.
