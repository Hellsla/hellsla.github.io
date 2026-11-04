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
