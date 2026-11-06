## fy6-3-L1-01
**Annettu:** lämmitysvastuksen jännite $U = 230\,\text{V}$ ja virta $I = 8{,}7\,\text{A}$
**Kysytty:** lämmitysvastuksen resistanssi $R$ ohmeina
**Periaate:** Resistanssi on komponentin jännitteen ja komponentin läpi kulkevan virran suhde. Annetut arvot koskevat samaa vastusta samalla hetkellä, kun keitin on käynnissä. Siksi suhde antaa vastuksen resistanssin käyttölämpötilassa.
**Kaava:** $R = \dfrac{U}{I}$
**Muunnokset:** Ei tarvita. Jännite on voltteina ja virta ampeereina, ja $1\,\text{V/A} = 1\,\Omega$.
**Sijoitus:** $R = \dfrac{230\,\text{V}}{8{,}7\,\text{A}} = 26{,}44\,\Omega$
**Vastaus:** $26\,\Omega$, kaksi merkitsevää numeroa kuten virrassa $8{,}7\,\text{A}$.
**Järkevyys:** Arvio: $230\,\text{V} : 10\,\text{A} = 23\,\Omega$. Virta on hieman alle $10\,\text{A}$, joten resistanssi on hieman yli $23\,\Omega$. Tarkistus Ohmin lailla: $26{,}44\,\Omega \cdot 8{,}7\,\text{A} = 230\,\text{V}$.

## fy6-3-L1-02
**Annettu:** vastuksen resistanssi $R = 220\,\Omega$ ja virta $I = 15\,\text{mA}$
**Kysytty:** vastuksen jännite $U$ voltteina
**Periaate:** Vastus noudattaa Ohmin lakia, joten jännite on resistanssin ja virran tulo. Saman yhtälön saa resistanssin määritelmästä $R = U : I$, kun kertoo molemmat puolet virralla.
**Kaava:** $R = \dfrac{U}{I}$, josta $U = R I$
**Muunnokset:** $I = 15\,\text{mA} = 15 \cdot 10^{-3}\,\text{A} = 0{,}015\,\text{A}$
**Sijoitus:** $U = 220\,\Omega \cdot 0{,}015\,\text{A} = 3{,}3\,\text{V}$
**Vastaus:** $3{,}3\,\text{V}$, kaksi merkitsevää numeroa kuten virrassa $15\,\text{mA}$.
**Järkevyys:** Ohmi kertaa ampeeri on voltti, joten yksikkö on oikein. Arvio: $200\,\Omega \cdot 0{,}015\,\text{A} = 3\,\text{V}$. Tarkka tulos on hieman suurempi, kuten pitääkin. Elektroniikassa tällaiset muutaman voltin jännitteet ovat tavallisia.

## fy6-3-L1-03
**Annettu:** lämmityslankojen resistanssi $R = 1{,}2\,\Omega$ ja jännite $U = 12\,\text{V}$
**Kysytty:** lankojen läpi kulkeva virta $I$ ampeereina
**Periaate:** Lämmityslangan virran saa resistanssin määritelmästä, kun jännite ja resistanssi tunnetaan. Annettu resistanssi koskee lankoja käytössä.
**Kaava:** $R = \dfrac{U}{I}$, josta $I = \dfrac{U}{R}$
**Muunnokset:** Ei tarvita. Jännite on voltteina ja resistanssi ohmeina, ja $1\,\text{V}/\Omega = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{12\,\text{V}}{1{,}2\,\Omega} = 10\,\text{A}$
**Vastaus:** $10\,\text{A}$, kaksi merkitsevää numeroa kuten jännitteessä ja resistanssissa.
**Järkevyys:** Resistanssi on pieni, joten virta on suuri. Tarkistus: $1{,}2\,\Omega \cdot 10\,\text{A} = 12\,\text{V}$. Takalasin lämmitin on yksi auton suurimmista sähkönkuluttajista, ja sillä on oma sulake.

## fy6-3-L1-04
**Annettu:** kuparijohdin, $l = 25\,\text{m}$, $A = 2{,}5\,\text{mm}^2$, $\rho = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$
**Kysytty:** johtimen resistanssi $R$ ohmeina
**Periaate:** Johdin on tasapaksua kuparia. Sen resistanssi on suoraan verrannollinen pituuteen ja kääntäen verrannollinen poikkipinta-alaan. Verrannollisuuskerroin on kuparin resistiivisyys.
**Kaava:** $R = \rho \dfrac{l}{A}$
**Muunnokset:** $A = 2{,}5\,\text{mm}^2 = 2{,}5 \cdot (10^{-3}\,\text{m})^2 = 2{,}5 \cdot 10^{-6}\,\text{m}^2$
**Sijoitus:** $R = \dfrac{1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot 25\,\text{m}}{2{,}5 \cdot 10^{-6}\,\text{m}^2} = 0{,}17\,\Omega$
**Vastaus:** $0{,}17\,\Omega$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Yksiköt: $\Omega\cdot\text{m} \cdot \text{m} : \text{m}^2 = \Omega$. Sähköjohdon resistanssin kuuluu olla pieni, alle ohmin, jotta johto ei lämpene. Yksi metri tätä johdinta on $0{,}0068\,\Omega$, ja $25 \cdot 0{,}0068\,\Omega = 0{,}17\,\Omega$.

## fy6-3-L1-05
**Annettu:** elektrodien välinen jännite $U = 5{,}0\,\text{V}$ ja virta $I = 2{,}0\,\text{mA}$
**Kysytty:** mullan resistanssi $R$ kilo-ohmeina
**Periaate:** Multa on elektrodien välillä virtapiirin komponentti. Sen resistanssi on jännitteen ja virran suhde samalla hetkellä.
**Kaava:** $R = \dfrac{U}{I}$
**Muunnokset:** $I = 2{,}0\,\text{mA} = 2{,}0 \cdot 10^{-3}\,\text{A}$. Lopuksi $1\,\text{k}\Omega = 1000\,\Omega$.
**Sijoitus:** $R = \dfrac{5{,}0\,\text{V}}{2{,}0 \cdot 10^{-3}\,\text{A}} = 2500\,\Omega = 2{,}5\,\text{k}\Omega$
**Vastaus:** $2{,}5\,\text{k}\Omega$, kaksi merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Virta on vain milliampeereja, joten resistanssi on suuri, tuhansia ohmeja. Kostea multa johtaa sähköä paremmin kuin kuiva. Kun multa kuivuu, resistanssi kasvaa ja virta pienenee. Anturi toimii näin.

## fy6-3-L2-01
**Annettu:** alussa $U_1 = 6{,}0\,\text{V}$ ja $I_1 = 0{,}25\,\text{A}$; lopussa $U_2 = 9{,}0\,\text{V}$; lämpötila pysyy samana
**Kysytty:** virta $I_2$ jännitteellä $9{,}0\,\text{V}$
**Periaate:** Vastuksen lämpötila pysyy samana, joten vastus noudattaa Ohmin lakia. Sen resistanssi on sama molemmilla jännitteillä. Resistanssi lasketaan ensimmäisestä mittauksesta ja käytetään toisessa.
**Kaava:** $R = \dfrac{U_1}{I_1}$ ja $I_2 = \dfrac{U_2}{R}$
**Muunnokset:** Ei tarvita. Jännitteet ovat voltteina ja virta ampeereina.
**Sijoitus:** $R = \dfrac{6{,}0\,\text{V}}{0{,}25\,\text{A}} = 24\,\Omega$ ja $I_2 = \dfrac{9{,}0\,\text{V}}{24\,\Omega} = 0{,}375\,\text{A}$
**Vastaus:** $0{,}38\,\text{A}$, kaksi merkitsevää numeroa kuten jännitteissä ja virrassa $0{,}25\,\text{A}$.
**Järkevyys:** Jännite kasvaa 1,5-kertaiseksi ($9{,}0\,\text{V} : 6{,}0\,\text{V} = 1{,}5$). Ohmin lain mukaan myös virta kasvaa 1,5-kertaiseksi: $1{,}5 \cdot 0{,}25\,\text{A} = 0{,}375\,\text{A}$. Tulos on sama.

## fy6-3-L2-02
**Annettu:** hehkulampun ominaiskäyrä $(I, U)$-kuvaajana; jännite $U = 1{,}0\,\text{V}$
**Kysytty:** lampun resistanssi $R$ jännitteellä $1{,}0\,\text{V}$
**Periaate:** Resistanssi on jännitteen ja virran suhde käyrän samassa pisteessä. Lamppu ei noudata Ohmin lakia. Siksi resistanssi pitää lukea juuri tällä jännitteellä. Sitä ei saa lukea käyrän jyrkkyydestä eikä toisesta pisteestä.
**Kuvaajan lukeminen:** Pystyakselilta etsitään $U = 1{,}0\,\text{V}$, ja siitä mennään vaakasuoraan käyrälle. Käyrän piste on vaaka-akselilla kohdassa $I = 0{,}15\,\text{A}$. Se on keskellä ruudukon viivojen $0{,}10\,\text{A}$ ja $0{,}20\,\text{A}$ välissä.
**Kaava:** $R = \dfrac{U}{I}$
**Muunnokset:** Ei tarvita. Jännite on voltteina ja virta ampeereina.
**Sijoitus:** $R = \dfrac{1{,}0\,\text{V}}{0{,}15\,\text{A}} = 6{,}67\,\Omega$
**Vastaus:** $6{,}7\,\Omega$, kaksi merkitsevää numeroa, koska virta luetaan kuvaajasta noin $0{,}005\,\text{A}$:n tarkkuudella.
**Järkevyys:** Lampun resistanssi kasvaa, kun lanka kuumenee. Jännitteellä $3{,}0\,\text{V}$ käyrästä luetaan $0{,}25\,\text{A}$ ja resistanssiksi tulee $12\,\Omega$. Pienemmällä jännitteellä arvo $6{,}7\,\Omega$ on siis järkevästi pienempi.

## fy6-3-L2-03
**Annettu:** kuparijohdin, $l = 50\,\text{m}$, $\rho = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$; resistanssi enintään $R = 0{,}50\,\Omega$
**Kysytty:** pienin poikkipinta-ala $A$ neliömillimetreinä
**Periaate:** Tasapaksun johtimen resistanssi on kääntäen verrannollinen poikkipinta-alaan. Suurin sallittu resistanssi antaa siis pienimmän sallitun poikkipinta-alan.
**Kaava:** $R = \rho \dfrac{l}{A}$, josta $A = \dfrac{\rho l}{R}$
**Muunnokset:** Tulos saadaan neliömetreinä, ja $1\,\text{m}^2 = (10^3\,\text{mm})^2 = 10^6\,\text{mm}^2$.
**Sijoitus:** $A = \dfrac{1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot 50\,\text{m}}{0{,}50\,\Omega} = 1{,}7 \cdot 10^{-6}\,\text{m}^2 = 1{,}7 \cdot 10^{-6} \cdot 10^6\,\text{mm}^2 = 1{,}7\,\text{mm}^2$
**Vastaus:** $1{,}7\,\text{mm}^2$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Yksiköt: $\Omega\cdot\text{m} \cdot \text{m} : \Omega = \text{m}^2$. Tarkistus: $1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot 50\,\text{m} : (1{,}7 \cdot 10^{-6}\,\text{m}^2) = 0{,}50\,\Omega$. Kodin johtimet ovat tyypillisesti $1{,}5$–$2{,}5\,\text{mm}^2$, joten tulos on tavallista kokoluokkaa.

## fy6-3-L2-04
**Annettu:** konstantaanilanka, halkaisija $d = 0{,}40\,\text{mm}$, pituus $l = 2{,}0\,\text{m}$, $\rho = 5{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m}$
**Kysytty:** langan resistanssi $R$ ohmeina
**Periaate:** Lanka on tasapaksu, joten $R = \rho l : A$. Poikkileikkaus on ympyrä. Poikkipinta-ala lasketaan säteestä, joka on puolet halkaisijasta.
**Kaava:** $A = \pi r^2 = \pi \left(\dfrac{d}{2}\right)^2$ ja $R = \dfrac{\rho l}{A}$
**Muunnokset:** $d = 0{,}40\,\text{mm} = 0{,}40 \cdot 10^{-3}\,\text{m}$, joten $r = 0{,}20 \cdot 10^{-3}\,\text{m}$.
**Sijoitus:** $A = \pi \cdot (0{,}20 \cdot 10^{-3}\,\text{m})^2 = 1{,}257 \cdot 10^{-7}\,\text{m}^2$ ja $R = \dfrac{5{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m} \cdot 2{,}0\,\text{m}}{1{,}257 \cdot 10^{-7}\,\text{m}^2} = 7{,}96\,\Omega$
**Vastaus:** $8{,}0\,\Omega$, kaksi merkitsevää numeroa kuten halkaisijassa, pituudessa ja resistiivisyydessä.
**Järkevyys:** Poikkipinta-ala on noin $0{,}13\,\text{mm}^2$. Se on vähän enemmän kuin simulaation ohuimman langan poikkipinta-ala ($0{,}10\,\text{mm}^2$). Simulaatiossa $1{,}00\,\text{m}$ lankaa, jonka poikkipinta-ala on $0{,}10\,\text{mm}^2$, on $5{,}0\,\Omega$. Siksi $2{,}0\,\text{m}$ hieman paksumpaa lankaa on vähän alle $10\,\Omega$.

## fy6-3-L3-01
**Annettu:** alkuperäinen resistanssi $R_1 = 0{,}80\,\Omega$; pituus kaksinkertaistuu, $l_2 = 2 l_1$; tilavuus säilyy
**Kysytty:** venytetyn langan resistanssi $R_2$
**Periaate:** Lanka on samaa ainetta ja tasapaksu, joten $R = \rho l : A$. Tilavuus $V = A l$ pysyy samana. Kun pituus kaksinkertaistuu, poikkipinta-ala puolittuu. Molemmat muutokset kasvattavat resistanssia. Pituus kaksinkertaistaa sen, ja puolet pienempi poikkipinta-ala kaksinkertaistaa sen uudelleen. Siksi resistanssi muuttuu enemmän kuin pituus.
**Kaava:** $R_1 = \rho \dfrac{l_1}{A_1}$ ja $R_2 = \rho \dfrac{l_2}{A_2}$, missä $l_2 = 2 l_1$ ja $A_2 = \dfrac{A_1}{2}$, josta $R_2 = \rho \dfrac{2 l_1}{A_1 / 2} = 4 R_1$
**Muunnokset:** Ei tarvita. Resistanssit ovat ohmeina, ja vertailu tehdään suhteina.
**Sijoitus:** $R_2 = 4 \cdot 0{,}80\,\Omega = 3{,}2\,\Omega$
**Vastaus:** $3{,}2\,\Omega$, kaksi merkitsevää numeroa kuten alkuperäisessä resistanssissa.
**Järkevyys:** Tilavuus säilyy: $2 l_1 \cdot \tfrac{1}{2} A_1 = l_1 A_1$. Jos poikkipinta-ala pysyisi samana, tulos olisi vain $1{,}6\,\Omega$. Ohentuminen tuo toisen kaksinkertaistuksen. Resistiivisyys ei muutu, koska aine on sama.

## fy6-3-L3-02
**Annettu:** kromnikkelilanka, $A = 0{,}20\,\text{mm}^2$, $U = 2{,}00\,\text{V}$; mittaukset $l$ ja $I$: $0{,}40\,\text{m}$ ja $0{,}91\,\text{A}$, $0{,}80\,\text{m}$ ja $0{,}46\,\text{A}$, $1{,}20\,\text{m}$ ja $0{,}30\,\text{A}$, $1{,}60\,\text{m}$ ja $0{,}23\,\text{A}$
**Kysytty:** kromnikkelin resistiivisyys $\rho$ yksikössä $\mu\Omega\cdot\text{m}$
**Periaate:** Jokaisen pituuden resistanssi on $R = U : I$. Tasapaksun langan resistanssi on $R = \rho l : A$. Siksi $R$ on suoraan verrannollinen pituuteen, ja suhde $R : l$ on vakio $\rho : A$. Oikeissa mittaussarjoissa pisteet eivät yleensä ole täsmälleen samalla suoralla, koska mittauksissa on epävarmuutta. Siksi käytetään kaikkia mittauksia.
**Kaava:** $R = \dfrac{U}{I}$ ja $R = \rho \dfrac{l}{A}$, josta $\rho = \dfrac{R}{l} \cdot A$
**Muunnokset:** $A = 0{,}20\,\text{mm}^2 = 0{,}20 \cdot 10^{-6}\,\text{m}^2$. Lopuksi $10^{-6}\,\Omega\cdot\text{m} = 1\,\mu\Omega\cdot\text{m}$.
**Sijoitus:** Resistanssit ovat $2{,}00\,\text{V} : 0{,}91\,\text{A} = 2{,}20\,\Omega$, $4{,}35\,\Omega$, $6{,}67\,\Omega$ ja $8{,}70\,\Omega$. Suhteet $R : l$ ovat $5{,}49$, $5{,}43$, $5{,}56$ ja $5{,}43\,\Omega/\text{m}$. Origon kautta sovitetun suoran kulmakerroin on $5{,}47\,\Omega/\text{m}$, joten $\rho = 5{,}47\,\tfrac{\Omega}{\text{m}} \cdot 0{,}20 \cdot 10^{-6}\,\text{m}^2 = 1{,}09 \cdot 10^{-6}\,\Omega\cdot\text{m}$
**Vastaus:** $1{,}1\,\mu\Omega\cdot\text{m}$, kaksi merkitsevää numeroa kuten poikkipinta-alassa ja virroissa $0{,}30\,\text{A}$ ja $0{,}23\,\text{A}$.
**Järkevyys:** Tulos on sama kuin taulukon arvo kromnikkelille, $1{,}1 \cdot 10^{-6}\,\Omega\cdot\text{m}$. Resistanssi kasvaa nelinkertaiseksi, kun pituus nelinkertaistuu ($2{,}20\,\Omega$ ja $8{,}70\,\Omega$). Verrannollisuus siis pätee.

## fy6-3-L3-03
**Annettu:** kylmän lampun resistanssi $R_\text{k} = 1{,}0\,\Omega$; käytössä $U = 3{,}0\,\text{V}$ ja $I = 0{,}25\,\text{A}$
**Kysytty:** virta $I_\text{k}$ kytkentähetkellä jännitteellä $3{,}0\,\text{V}$
**Periaate:** Kytkentähetkellä lanka on vielä huoneenlämpöinen, joten sen resistanssi on kylmän lampun arvo. Lanka kuumenee vasta, kun virta on kulkenut sen läpi hetken. Virran saa resistanssin määritelmästä.
**Kaava:** $R_\text{k} = \dfrac{U}{I_\text{k}}$, josta $I_\text{k} = \dfrac{U}{R_\text{k}}$
**Muunnokset:** Ei tarvita. Jännite on voltteina ja resistanssi ohmeina.
**Sijoitus:** $I_\text{k} = \dfrac{3{,}0\,\text{V}}{1{,}0\,\Omega} = 3{,}0\,\text{A}$
**Vastaus:** $3{,}0\,\text{A}$, kaksi merkitsevää numeroa kuten jännitteessä ja resistanssissa.
**Järkevyys:** Palavan lampun resistanssi on $3{,}0\,\text{V} : 0{,}25\,\text{A} = 12\,\Omega$. Se on 12-kertainen kylmään lamppuun verrattuna. Siksi kytkentävirta on 12-kertainen käyttövirtaan $0{,}25\,\text{A}$ verrattuna. Tämä suuri virta kuumentaa ohutta lankaa hyvin nopeasti. Langan ohuin kohta kuumenee eniten, koska siinä resistanssi pituutta kohti on suurin. Siksi lanka katkeaa useimmiten juuri päälle kytkettäessä.

## fy6-3-L1-06
**Kysytty:** mitä origon kautta kulkeva suora ominaiskäyrä kertoo komponentista.
**Periaate:** Ominaiskäyrä näyttää, miten jännite ja virta riippuvat toisistaan. Jos käyrä on origon kautta kulkeva suora, jännite on suoraan verrannollinen virtaan. Kun toinen kaksinkertaistuu, myös toinen kaksinkertaistuu. Silloin suhde $R = U : I$ on joka pisteessä sama. Suoran kulmakerroin on resistanssi.
**Mallivastaus:** Komponentti noudattaa Ohmin lakia, koska jännite on suoraan verrannollinen virtaan. Resistanssi $R = U : I$ on vakio. Resistanssi ei kasva jännitteen mukana, sillä silloin käyrä olisi kaareva. Resistanssi ei myöskään ole nolla. Origon kautta kulkeminen kertoo vain, että nollajännitteellä virtakin on nolla. Pelkkä virran ja jännitteen yhtäaikainen kasvu ei todista verrannollisuutta. Sen osoittaa vasta se, että suhde $U : I$ on vakio.

## fy6-3-L1-07
**Kysytty:** miten kahden saman metallin ja saman paksuisen langan resistiivisyys ja resistanssi eroavat, kun toinen on kaksi kertaa pidempi.
**Periaate:** Resistiivisyys $\rho$ on aineen ominaisuus. Se riippuu aineesta ja lämpötilasta, ei langan mitoista. Resistanssi $R = \rho l : A$ riippuu myös pituudesta $l$ ja poikkipinta-alasta $A$. Kaksi kertaa pidempi lanka on kuin kaksi lankaa peräkkäin.
**Mallivastaus:** Resistiivisyys on sama, mutta pidemmän langan resistanssi on suurempi pituuden takia. Se on kaksinkertainen, koska poikkipinta-ala ja aine ovat samat ja pituus on kaksinkertainen. Pidemmän langan resistiivisyys ei ole suurempi, koska se ei riipu mitoista. Resistanssi ei myöskään ole sama, koska se riippuu pituudesta. Pidempi lanka ei tarjoa virralle enemmän tilaa. Virran kulkutilaa kuvaa poikkipinta-ala, ja se on molemmilla langoilla sama.

## fy6-3-L1-08
**Annettu:** alussa $U = 4{,}5\,\text{V}$ ja $I_1 = 0{,}60\,\text{A}$; uusi lanka on samaa kuparia, yhtä paksu ja kaksi kertaa pidempi; jännite ja lämpötila pysyvät samoina
**Kysytty:** virta $I_2$ pidemmän langan läpi
**Periaate:** Lanka on samaa ainetta ja yhtä paksua, joten $R = \rho l : A$ on suoraan verrannollinen pituuteen. Kaksi kertaa pidemmän langan resistanssi on kaksinkertainen. Jännite pysyy samana. Silloin virta on resistanssin määritelmän mukaan kääntäen verrannollinen resistanssiin.
**Kaava:** $R = \dfrac{U}{I}$, jolloin $R_1 = \dfrac{U}{I_1}$, $R_2 = 2 R_1$ ja $I_2 = \dfrac{U}{R_2}$
**Muunnokset:** Ei tarvita. Jännite on voltteina, virta ampeereina ja resistanssi ohmeina.
**Sijoitus:** $R_1 = \dfrac{4{,}5\,\text{V}}{0{,}60\,\text{A}} = 7{,}5\,\Omega$, $R_2 = 2 \cdot 7{,}5\,\Omega = 15\,\Omega$ ja $I_2 = \dfrac{4{,}5\,\text{V}}{15\,\Omega} = 0{,}30\,\text{A}$
**Vastaus:** $0{,}30\,\text{A}$, kaksi merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Resistanssi kaksinkertaistuu ja jännite pysyy samana. Siksi virta puolittuu: $0{,}60\,\text{A} : 2 = 0{,}30\,\text{A}$. Tarkistus: $15\,\Omega \cdot 0{,}30\,\text{A} = 4{,}5\,\text{V}$. Yleinen sääntö: $R \propto l$, joten samalla jännitteellä $I \propto 1 : l$.

## fy6-3-L2-05
**Annettu:** mittauspisteet $(U, I)$ taulukossa, $U = 1{,}0\,\text{V}$–$8{,}0\,\text{V}$ ja $I = 6{,}6\,\text{mA}$–$53{,}6\,\text{mA}$; yleismittarin virheraja noin $\pm 0{,}5\,\text{mA}$
**Kysytty:** vastuksen resistanssi $R$ sovitussuoran kulmakertoimesta ja sen epävarmuus $\Delta R$
**Periaate:** Vastuksen ominaiskäyrä on origon kautta kulkeva suora. Suoran kulmakerroin on resistanssi. Mittauspisteet hajoavat suoran ympärille, koska mittauksessa on epävarmuutta. Siksi suora piirretään pisteiden joukon keskeltä niin, että pisteitä jää sen molemmille puolille. Suoran ei tarvitse kulkea yhdenkään pisteen kautta.
**Kuvaajan lukeminen:** Virta $I$ on vaaka-akselilla ja jännite $U$ pystyakselilla. Sovitussuora kulkee origosta pisteiden keskeltä. Suora piirretään paperille tai kuvaajaohjelmalla. Oma piirros tarkistetaan vertaamalla sen lukemaa tähän. Suoralta luetaan piste, joka on kaukana origosta: kun $I = 50{,}0\,\text{mA}$, suora on kohdassa $U = 7{,}5\,\text{V}$. Mitä kauempana lukemispiste on origosta, sitä pienempi osuus lukuvirheestä on kulmakertoimessa.
**Kaava:** $R = \dfrac{\Delta U}{\Delta I}$ eli suoran kulmakerroin; epävarmuus $\Delta R \approx \dfrac{R_{\text{max}} - R_{\text{min}}}{2}$, missä $R_{\text{max}}$ ja $R_{\text{min}}$ ovat yksittäisten pisteiden suurin ja pienin $U : I$
**Muunnokset:** $50{,}0\,\text{mA} = 50{,}0 \cdot 10^{-3}\,\text{A} = 0{,}0500\,\text{A}$
**Sijoitus:** $R = \dfrac{7{,}5\,\text{V} - 0\,\text{V}}{0{,}0500\,\text{A} - 0\,\text{A}} = 150\,\Omega$. Pisteiden $U : I$ ovat $152$, $148$, $152$, $149$, $151$, $149$, $151$ ja $149\,\Omega$ (pienin $148{,}1\,\Omega$ ja suurin $151{,}5\,\Omega$). Pisteiden hajonnasta saatu arvio on siis $\Delta R \approx \dfrac{151{,}5\,\Omega - 148{,}1\,\Omega}{2} = 1{,}7\,\Omega$
**Vastaus:** $R = 150\,\Omega$, kolme merkitsevää numeroa, koska epävarmuus on vain noin $2\,\Omega$. Epävarmuus on noin $\Delta R \approx 2\,\Omega$, eli $R = (150 \pm 2)\,\Omega$.
**Järkevyys:** Kaikki pisteiden resistanssit ovat välillä $148\,\Omega$–$152\,\Omega$. Ne ovat korkeintaan noin $1{,}5\,\%$ sovitetusta arvosta, joten suora kuvaa mittauksia hyvin. Hajonta vastaa yleismittarin virherajaa. Pisteiden poikkeamat suorasta ovat korkeintaan noin $0{,}4\,\text{mA}$, ja se on virherajan $0{,}5\,\text{mA}$ sisällä. Vastuksen jännite on $8{,}0\,\text{V}$, kun virta on $53{,}3\,\text{mA}$: $150\,\Omega \cdot 0{,}0533\,\text{A} = 8{,}0\,\text{V}$.

## fy6-3-L2-06
**Annettu:** hehkulampun mittauspisteet $(U, I)$ taulukossa, $U = 1{,}0\,\text{V}$–$5{,}0\,\text{V}$
**Kysytty:** resistanssi $R = U : I$ jokaisella jännitteellä, noudattaako lamppu Ohmin lakia ja resistanssin suhde jännitteillä $5{,}0\,\text{V}$ ja $1{,}0\,\text{V}$
**Periaate:** Jos lamppu noudattaisi Ohmin lakia, suhde $U : I$ olisi kaikilla jännitteillä sama. Lasketaan suhde jokaiselle pisteelle ja verrataan arvoja. Resistanssien suhde $R_{5{,}0} : R_{1{,}0}$ kertoo, kuinka paljon resistanssi muuttuu.
**Kaava:** $R = \dfrac{U}{I}$ ja suhde $\dfrac{R_{5{,}0}}{R_{1{,}0}}$
**Muunnokset:** Ei tarvita. Jännite on voltteina ja virta ampeereina.
**Sijoitus:** $R = 1{,}0\,\text{V} : 0{,}098\,\text{A} = 10{,}2\,\Omega$, $2{,}0\,\text{V} : 0{,}146\,\text{A} = 13{,}7\,\Omega$, $3{,}0\,\text{V} : 0{,}187\,\text{A} = 16{,}0\,\Omega$, $4{,}0\,\text{V} : 0{,}221\,\text{A} = 18{,}1\,\Omega$ ja $5{,}0\,\text{V} : 0{,}248\,\text{A} = 20{,}2\,\Omega$. Suhde on $\dfrac{20{,}2\,\Omega}{10{,}2\,\Omega} = 1{,}98$
**Vastaus:** $2{,}0$ kertaa, kaksi merkitsevää numeroa kuten jännitteissä. Lamppu ei noudata Ohmin lakia, koska resistanssi kasvaa $10\,\Omega$:sta noin $20\,\Omega$:iin.
**Järkevyys:** Jännite kasvaa viisinkertaiseksi ($5{,}0\,\text{V} : 1{,}0\,\text{V} = 5{,}0$), mutta virta kasvaa vain noin $2{,}5$-kertaiseksi ($0{,}248\,\text{A} : 0{,}098\,\text{A} = 2{,}5$). Ohmin lain mukaan virtakin kasvaisi viisinkertaiseksi. Siksi resistanssin on kasvettava noin $5{,}0 : 2{,}5 = 2{,}0$-kertaiseksi, kuten laskettiin. Selitys: suurempi virta kuumentaa volframilankaa, ja kuuman metallilangan resistanssi on suurempi. Lampun lämpötila muuttuu mittauksen aikana. Siksi Ohmin lain ehto vakiolämpötilasta ei toteudu.

## fy6-3-L2-07
**Annettu:** mittauspisteet $(U, I)$: $(0{,}0\,\text{V}; 0{,}00\,\text{A})$, $(1{,}0\,\text{V}; 0{,}20\,\text{A})$, $(2{,}0\,\text{V}; 0{,}41\,\text{A})$, $(3{,}0\,\text{V}; 0{,}61\,\text{A})$ ja $(4{,}0\,\text{V}; 0{,}81\,\text{A})$
**Kysytty:** mikä opiskelijan päättelyssä on virheellistä, ja nollasta poikkeavien jännitteiden resistanssien keskiarvo $R_{\text{ka}}$
**Periaate:** Resistanssi $R = U : I$ on määritelty vain, kun virta ei ole nolla. Pisteessä $U = 0{,}0\,\text{V}$ ja $I = 0{,}00\,\text{A}$ suhde on $0 : 0$. Se ei ole luku. Se, että vastus ei päästä virtaa läpi ilman jännitettä, ei tarkoita, että resistanssi on nolla. Resistanssi arvioidaan pisteistä, joissa virran voi mitata. Jos suhde $U : I$ on niissä sama, vastus noudattaa Ohmin lakia. Silloin resistanssi ei kasva jännitteen mukana.
**Kaava:** $R = \dfrac{U}{I}$ kullekin pisteelle ja $R_{\text{ka}} = \dfrac{R_1 + \ldots + R_4}{4}$
**Muunnokset:** Ei tarvita. Jännite on voltteina ja virta ampeereina.
**Sijoitus:** $R_1 = 1{,}0\,\text{V} : 0{,}20\,\text{A} = 5{,}00\,\Omega$, $R_2 = 2{,}0\,\text{V} : 0{,}41\,\text{A} = 4{,}88\,\Omega$, $R_3 = 3{,}0\,\text{V} : 0{,}61\,\text{A} = 4{,}92\,\Omega$ ja $R_4 = 4{,}0\,\text{V} : 0{,}81\,\text{A} = 4{,}94\,\Omega$. Summa on $19{,}74\,\Omega$, joten $R_{\text{ka}} = 19{,}74\,\Omega : 4 = 4{,}93\,\Omega$
**Vastaus:** $R_{\text{ka}} = 4{,}9\,\Omega$, kaksi merkitsevää numeroa kuten virroissa. Opiskelijan päättely on virheellinen. Nollapisteessä resistanssia ei voi laskea (suhde $0 : 0$ ei ole nolla). Muissa pisteissä resistanssi on käytännössä sama, joten se ei kasva jännitteen mukana.
**Järkevyys:** Suurimmalla jännitteellä $4{,}0\,\text{V}$ saadaan $4{,}94\,\Omega$. Kaikki arvot ovat välillä $4{,}88\,\Omega$–$5{,}00\,\Omega$, joten keskiarvo $4{,}9\,\Omega$ on niiden välissä. Tarkistus: $4{,}9\,\Omega \cdot 0{,}81\,\text{A} = 4{,}0\,\text{V}$. Ensimmäisen pisteen $5{,}00\,\Omega$ ja muiden arvojen ero on mittausepävarmuutta, ei kasvua. Origon kautta sovitetun suoran kulmakerroin antaa saman tuloksen $4{,}9\,\Omega$.

## fy6-3-L3-04
**Annettu:** komponenttien A, B ja C virrat jännitteillä $0{,}5\,\text{V}$–$3{,}0\,\text{V}$ taulukossa (milliampeereina); komponentit ovat vastus, hehkulamppu ja diodi
**Kysytty:** komponenttien tunnistus resistanssin muutoksen perusteella ja diodin resistanssi $R$ työpisteessä $U = 1{,}5\,\text{V}$ ohmeina
**Periaate:** Resistanssi on joka pisteessä $R = U : I$. Vastuksella se pysyy samana, kun lämpötila on vakio. Silloin ominaiskäyrä on suora. Hehkulampun resistanssi kasvaa jännitteen mukana. Suurempi virta kuumentaa lankaa, ja kuuman metallin resistanssi on suurempi. Diodi ei noudata Ohmin lakia. Pienellä jännitteellä sen läpi ei kulje juuri virtaa, ja resistanssi on suuri. Kun virta alkaa kasvaa, diodin resistanssi pienenee jännitteen kasvaessa. Tunnistus tehdään vertaamalla resistansseja eri jännitteillä. Työpisteessä resistanssi on pisteen $U : I$, ei käyrän jyrkkyys.
**Kaava:** $R = \dfrac{U}{I}$
**Muunnokset:** Virrat milliampeereista ampeereiksi: $1\,\text{mA} = 10^{-3}\,\text{A}$, esimerkiksi $20{,}0\,\text{mA} = 0{,}0200\,\text{A}$.
**Sijoitus:** Komponentti A: $R = 0{,}5\,\text{V} : 6{,}6\,\text{mA} = 76\,\Omega$, $1{,}0\,\text{V} : 13{,}5\,\text{mA} = 74\,\Omega$, $1{,}5\,\text{V} : 20{,}0\,\text{mA} = 75\,\Omega$, $2{,}0\,\text{V} : 26{,}6\,\text{mA} = 75\,\Omega$ ja $3{,}0\,\text{V} : 40{,}2\,\text{mA} = 75\,\Omega$. Komponentti B: $16\,\Omega$, $22\,\Omega$, $26\,\Omega$, $30\,\Omega$ ja $37\,\Omega$. Komponentti C: $1{,}0\,\text{V} : 0{,}1\,\text{mA} = 10\,\text{k}\Omega$, $1{,}5\,\text{V} : 2{,}5\,\text{mA} = 600\,\Omega$, $2{,}0\,\text{V} : 21\,\text{mA} = 95\,\Omega$ ja $3{,}0\,\text{V} : 98\,\text{mA} = 31\,\Omega$. Jännitteellä $0{,}5\,\text{V}$ virta on nolla, joten resistanssia ei lasketa. Diodin resistanssi työpisteessä on $R = \dfrac{1{,}5\,\text{V}}{2{,}5 \cdot 10^{-3}\,\text{A}} = 600\,\Omega$. Hehkulampun resistanssi samassa pisteessä on $\dfrac{1{,}5\,\text{V}}{57 \cdot 10^{-3}\,\text{A}} = 26\,\Omega$
**Vastaus:** $6{,}0 \cdot 10^{2}\,\Omega$, kaksi merkitsevää numeroa kuten virrassa $2{,}5\,\text{mA}$. Komponentti A on vastus (resistanssi vakio, noin $75\,\Omega$). B on hehkulamppu (resistanssi kasvaa $16\,\Omega$:sta $37\,\Omega$:iin). C on diodi (resistanssi pienenee $10\,\text{k}\Omega$:sta $31\,\Omega$:iin). Pisteessä $U = 1{,}5\,\text{V}$ diodin resistanssi on noin $23$-kertainen hehkulampun resistanssiin verrattuna.
**Järkevyys:** Tarkistus: $600\,\Omega \cdot 2{,}5 \cdot 10^{-3}\,\text{A} = 1{,}5\,\text{V}$. Suhde $600\,\Omega : 26\,\Omega = 23$. Vastuksen virta on suoraan verrannollinen jännitteeseen. Jännite kolminkertaistuu $1{,}0\,\text{V}$:sta $3{,}0\,\text{V}$:iin, ja virta kasvaa $13{,}5\,\text{mA}$:sta $40{,}2\,\text{mA}$:iin eli $2{,}98$-kertaiseksi. Hehkulampulla jännite kasvaa saman verran, mutta virta kasvaa vain $81 : 46 = 1{,}8$-kertaiseksi. Siksi resistanssi kasvaa.

## fy6-3-L3-05
**Annettu:** lakattu rautalanka vesihauteessa, $U = 1{,}00\,\text{V}$ kaikissa mittauksissa; $T$ ja $I$: $20\,{}^\circ\text{C}$ ja $0{,}500\,\text{A}$, $40\,{}^\circ\text{C}$ ja $0{,}442\,\text{A}$, $60\,{}^\circ\text{C}$ ja $0{,}398\,\text{A}$, $80\,{}^\circ\text{C}$ ja $0{,}362\,\text{A}$
**Kysytty:** kokeen muuttujat ja mittausjärjestely, langan resistanssin kasvu prosentteina lämpötilasta $20\,{}^\circ\text{C}$ lämpötilaan $80\,{}^\circ\text{C}$ sekä kaksi virhelähdettä
**Periaate:** Resistanssi saadaan jokaisessa lämpötilassa suhteena $R = U : I$. Kun jännite pidetään samana, virran pieneneminen kertoo resistanssin kasvusta. Kokeessa muutetaan vain yhtä tekijää, lämpötilaa. Muut tekijät pidetään vakioina, jotta tuloksen voi yhdistää lämpötilaan. Prosenttikasvu on $\dfrac{R_{80} - R_{20}}{R_{20}} \cdot 100\,\%$.
**Kaava:** $R = \dfrac{U}{I}$ ja kasvu $\dfrac{R_{80} - R_{20}}{R_{20}} \cdot 100\,\%$
**Muunnokset:** Ei tarvita. Jännite on voltteina ja virta ampeereina. Lämpötilaa ei tarvitse muuntaa.
**Sijoitus:** Muuttujat: riippumaton muuttuja on veden eli langan lämpötila $T$. Riippuva muuttuja on langan resistanssi $R$, joka mitataan virrasta ja jännitteestä. Vakioitavat tekijät ovat langan aine, pituus ja paksuus sekä jännite $1{,}00\,\text{V}$. Mittausjärjestely: virtamittari kytketään sarjaan langan kanssa ja jännitemittari rinnan langan kanssa. Silloin mittarit mittaavat langan virtaa ja jännitettä. Lanka on lakattu, jotta vesi ei johda virtaa sen ohi. Lämpömittari on langan vieressä. Resistanssit ovat $R_{20} = 1{,}00\,\text{V} : 0{,}500\,\text{A} = 2{,}000\,\Omega$, $R_{40} = 2{,}262\,\Omega$, $R_{60} = 2{,}513\,\Omega$ ja $R_{80} = 1{,}00\,\text{V} : 0{,}362\,\text{A} = 2{,}762\,\Omega$. Kasvu on siis $\dfrac{2{,}762\,\Omega - 2{,}000\,\Omega}{2{,}000\,\Omega} \cdot 100\,\% = 38{,}1\,\%$. Virhelähteet: (1) Lanka lämpenee myös virrasta itsestään, joten sen lämpötila voi olla korkeampi kuin veden. Virta kytketään vain mittaushetkeksi, ja jännite pidetään pienenä. (2) Lanka ei ole ehtinyt tasaantua veden lämpötilaan, tai lämpömittari ei ole langan kohdalla. Jokaisessa lämpötilassa odotetaan, kunnes lämpömittarin lukema ei enää muutu, ja vettä sekoitetaan.
**Vastaus:** Resistanssi on kasvanut noin $38\,\%$ (laskettu $38{,}1\,\%$), kaksi merkitsevää numeroa, koska kasvu on kahden lähes yhtä suuren resistanssin erotus suhteessa arvoon $R_{20}$. Tulos tukee päätelmää, että metallilangan resistanssi kasvaa lämpötilan noustessa.
**Järkevyys:** Virta pienenee, kun lämpötila nousee ($0{,}500\,\text{A} \to 0{,}362\,\text{A}$), ja jännite on vakio. Siksi resistanssin on kasvettava: $0{,}500\,\text{A} : 0{,}362\,\text{A} = 1{,}38$. Resistanssi kasvaa jokaisella $20\,{}^\circ\text{C}$:n välillä suunnilleen saman verran ($0{,}262\,\Omega$, $0{,}251\,\Omega$ ja $0{,}249\,\Omega$), eli kasvu on lähes tasaista. Mittaus on tehty yhdellä langalla. Tulos kuvaa siis tämän esimerkkiaineiston lankaa, eikä se ole rautalangan tarkka ominaisuus.

## fy6-3-L1-09
**Kysytty:** mikä neljästä $(I, U)$-kuvaajasta on Ohmin lakia noudattavan $2{,}0\,\text{k}\Omega$:n vastuksen ominaiskäyrä.
**Periaate:** Ohmin lakia noudattavan vastuksen resistanssi on vakio, joten $U = RI$. Ominaiskäyrä on origon kautta kulkeva suora, jonka kulmakerroin on resistanssi $R$. Resistanssi on jännitteen ja virran suhde $U : I$, ei $I : U$. Sen pitää olla sama käyrän joka pisteessä.
**Mallivastaus:** Oikea on kuvaaja C. Lasketaan vastuksen jännite virralla $4{,}0\,\text{mA}$.

$U = RI$

$U = 2{,}0 \cdot 10^{3}\,\Omega \cdot 4{,}0 \cdot 10^{-3}\,\text{A}$

$U = 8{,}0\,\text{V}$

Kuvaajan C suora kulkee origon ja pisteen $(4{,}0\,\text{mA};\ 8{,}0\,\text{V})$ kautta. Myös pisteessä $(2{,}0\,\text{mA};\ 4{,}0\,\text{V})$ suhde on $U : I = 2{,}0\,\text{k}\Omega$. Kuvaajan A käyrä kulkee samassa pisteessä $(4{,}0\,\text{mA};\ 8{,}0\,\text{V})$. Pisteessä $(2{,}0\,\text{mA};\ 2{,}0\,\text{V})$ suhde on kuitenkin vain $1{,}0\,\text{k}\Omega$. Resistanssi kasvaa jännitteen mukana, joten komponentti ei noudata Ohmin lakia. Kuvaajassa B virralla $4{,}0\,\text{mA}$ jännite on $2{,}0\,\text{V}$, joten resistanssi olisi $0{,}50\,\text{k}\Omega$. Siinä kulmakertoimeksi on otettu $I : U$. Kuvaajassa D jännite on vakio $2{,}0\,\text{V}$, joten suhde $U : I$ muuttuu koko ajan. Siinä resistanssin lukuarvo on piirretty jännitteeksi.

**Kuvaajan lukeminen:** Jokaisesta kuvaajasta luetaan jännite kahdella virralla, esimerkiksi $2{,}0\,\text{mA}$ ja $4{,}0\,\text{mA}$, ja lasketaan suhde $U : I$. Vain kuvaajassa C suhde on molemmissa pisteissä $2{,}0\,\text{k}\Omega$.
