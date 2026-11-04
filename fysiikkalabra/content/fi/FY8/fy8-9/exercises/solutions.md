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
