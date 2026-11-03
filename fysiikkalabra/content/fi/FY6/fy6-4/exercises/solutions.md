## fy6-4-L1-01
**Annettu:** sarjaan kytketyt vastukset $R_1 = 120\,\Omega$, $R_2 = 220\,\Omega$ ja $R_3 = 330\,\Omega$
**Kysytty:** kokonaisresistanssi $R$ ohmeina
**Periaate:** Sarjaankytkennässä sama virta kulkee jokaisen vastuksen läpi ja vastusten jännitteet summautuvat. Siksi kokonaisresistanssi on vastusten resistanssien summa.
**Kaava:** $R = R_1 + R_2 + R_3$
**Muunnokset:** Ei tarvita, kaikki resistanssit ovat ohmeina.
**Sijoitus:** $R = 120\,\Omega + 220\,\Omega + 330\,\Omega = 670\,\Omega$
**Vastaus:** $670\,\Omega$. Summan tarkkuuden ratkaisevat yhteenlaskettavat, jotka kaikki on annettu ohmin tarkkuudella.
**Järkevyys:** Sarjaankytkennän kokonaisresistanssi on suurempi kuin suurin vastuksista, $330\,\Omega$. Tulos on noin kaksinkertainen suurimpaan vastukseen verrattuna, mikä sopii, koska kaksi muuta vastusta ovat yhteensä $340\,\Omega$.

## fy6-4-L1-02
**Annettu:** rinnan kytketyt vastukset $R_1 = 40\,\Omega$ ja $R_2 = 60\,\Omega$
**Kysytty:** kokonaisresistanssi $R$ ohmeina
**Periaate:** Rinnankytkennässä kummankin vastuksen yli on sama jännite ja haaravirrat summautuvat. Siksi kokonaisresistanssin käänteisluku on haarojen resistanssien käänteislukujen summa.
**Kaava:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$, josta $R = \dfrac{R_1 R_2}{R_1 + R_2}$
**Muunnokset:** Ei tarvita, molemmat resistanssit ovat ohmeina.
**Sijoitus:** $R = \dfrac{40\,\Omega \cdot 60\,\Omega}{40\,\Omega + 60\,\Omega} = \dfrac{2400\,\Omega^2}{100\,\Omega} = 24\,\Omega$
**Vastaus:** $24\,\Omega$, kaksi merkitsevää numeroa kuten vastusten arvoissa.
**Järkevyys:** Rinnankytkennän kokonaisresistanssi on pienempi kuin pienempi vastuksista, $40\,\Omega$. Jos vastukset olisivat molemmat $40\,\Omega$, tulos olisi puolet eli $20\,\Omega$; nyt toinen vastus on suurempi, joten tulos on hieman yli $20\,\Omega$.

## fy6-4-L1-03
**Annettu:** rinnan kytkettyjen valaisimien virrat $I_1 = 0{,}20\,\text{A}$, $I_2 = 0{,}45\,\text{A}$ ja $I_3 = 0{,}85\,\text{A}$
**Kysytty:** akusta lähtevä virta $I$
**Periaate:** Rinnankytkennässä virta jakautuu haaroihin ja yhdistyy taas. Varausta ei katoa eikä kasaannu haarautumispisteisiin, joten akusta lähtevä virta on haaravirtojen summa.
**Kaava:** $I = I_1 + I_2 + I_3$
**Muunnokset:** Ei tarvita, kaikki virrat ovat ampeereina.
**Sijoitus:** $I = 0{,}20\,\text{A} + 0{,}45\,\text{A} + 0{,}85\,\text{A} = 1{,}50\,\text{A}$
**Vastaus:** $1{,}50\,\text{A}$, sadasosa-ampeerin tarkkuudella kuten kaikki yhteenlaskettavat.
**Järkevyys:** Akusta lähtevä virta on suurempi kuin yksikään haaravirroista, koska jokainen valaisin on oma kulkureittinsä. Pyöristetyillä luvuilla $0{,}2\,\text{A} + 0{,}5\,\text{A} + 0{,}8\,\text{A} = 1{,}5\,\text{A}$.

## fy6-4-L1-04
**Annettu:** sarjaan kytketyt lamput, pariston jännite $U = 4{,}5\,\text{V}$, ensimmäisen lampun jännite $U_1 = 1{,}8\,\text{V}$
**Kysytty:** toisen lampun jännite $U_2$
**Periaate:** Sarjaankytkennässä pariston jännite jakautuu komponenttien kesken: jokainen varaus kulkee molempien lamppujen läpi, ja sen energia muuttuu lampuissa lämmöksi ja valoksi. Lamppujen jännitteiden summa on pariston jännite.
**Kaava:** $U = U_1 + U_2$, josta $U_2 = U - U_1$
**Muunnokset:** Ei tarvita, jännitteet ovat voltteina.
**Sijoitus:** $U_2 = 4{,}5\,\text{V} - 1{,}8\,\text{V} = 2{,}7\,\text{V}$
**Vastaus:** $2{,}7\,\text{V}$, kymmenesosavoltin tarkkuudella kuten annetut jännitteet.
**Järkevyys:** Kummankin lampun jännite on pienempi kuin pariston jännite, ja yhteensä $1{,}8\,\text{V} + 2{,}7\,\text{V} = 4{,}5\,\text{V}$. Lamppujen läpi kulkee sama virta, joten suurempi jännite on sen lampun yli, jonka resistanssi on suurempi.

## fy6-4-L1-05
**Annettu:** kolme rinnan kytkettyä vastusta, kukin $R_1 = 330\,\Omega$
**Kysytty:** kokonaisresistanssi $R$ ohmeina
**Periaate:** Rinnankytkennässä jokaisen vastuksen yli on sama jännite ja haaravirrat summautuvat, joten kokonaisresistanssin käänteisluku on haarojen käänteislukujen summa. Kun vastukset ovat yhtä suuret, summa on kolme kertaa yksi käänteisluku.
**Kaava:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_1} + \dfrac{1}{R_1} = \dfrac{3}{R_1}$, josta $R = \dfrac{R_1}{3}$
**Muunnokset:** Ei tarvita, resistanssi on ohmeina.
**Sijoitus:** $R = \dfrac{330\,\Omega}{3} = 110\,\Omega$
**Vastaus:** $110\,\Omega$, kolme merkitsevää numeroa kuten resistanssissa $330\,\Omega$.
**Järkevyys:** Kolme samanlaista haaraa johtaa kolme kertaa niin hyvin kuin yksi, joten resistanssi on kolmasosa. Tulos on pienempi kuin yhden vastuksen $330\,\Omega$, kuten rinnankytkennässä pitääkin.

## fy6-4-L2-01
**Annettu:** sarjaan kytketyt vastukset $R_1 = 1{,}2\,\text{k}\Omega$ ja $R_2 = 680\,\Omega$, pariston jännite $U = 9{,}0\,\text{V}$
**Kysytty:** piirin virta $I$ milliampeereina
**Periaate:** Sarjaankytkennässä on vain yksi kulkureitti, joten sama virta kulkee kummankin vastuksen läpi. Kytkennän voi korvata kokonaisresistanssilla, joka on resistanssien summa, ja virta saadaan Ohmin laista.
**Kaava:** $R = R_1 + R_2$ ja $U = RI$, josta $I = \dfrac{U}{R_1 + R_2}$
**Muunnokset:** $R_1 = 1{,}2\,\text{k}\Omega = 1{,}2 \cdot 1000\,\Omega = 1200\,\Omega$. Lopuksi $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $I = \dfrac{9{,}0\,\text{V}}{1200\,\Omega + 680\,\Omega} = \dfrac{9{,}0\,\text{V}}{1880\,\Omega} = 0{,}004\,787\,\text{A} = 4{,}787\,\text{mA}$
**Vastaus:** $4{,}8\,\text{mA}$, kaksi merkitsevää numeroa kuten jännitteessä $9{,}0\,\text{V}$ ja resistanssissa $1{,}2\,\text{k}\Omega$.
**Järkevyys:** Kokonaisresistanssi on noin $2\,\text{k}\Omega$, joten virta on noin $9\,\text{V} : 2000\,\Omega \approx 4{,}5\,\text{mA}$. Kilo-ohmien vastuksilla ja paristolla virrat ovat tyypillisesti milliampeereja.

## fy6-4-L2-02
**Annettu:** lampun jännite $U_\text{L} = 2{,}5\,\text{V}$ ja virta $I = 0{,}10\,\text{A}$, pariston jännite $U = 6{,}0\,\text{V}$
**Kysytty:** sarjavastuksen resistanssi $R_\text{s}$
**Periaate:** Lamppu ja vastus ovat sarjassa, joten saman virran $I$ on kuljettava kummankin läpi, ja pariston jännite jakautuu niiden kesken. Vastuksen yli on se osa jännitteestä, joka ei jää lampulle, ja sen resistanssi saadaan Ohmin laista.
**Kaava:** $U = U_\text{L} + U_\text{s}$ ja $U_\text{s} = R_\text{s} I$, josta $R_\text{s} = \dfrac{U - U_\text{L}}{I}$
**Muunnokset:** Ei tarvita: jännitteet ovat voltteina ja virta ampeereina, ja $\tfrac{\text{V}}{\text{A}} = \Omega$.
**Sijoitus:** $R_\text{s} = \dfrac{6{,}0\,\text{V} - 2{,}5\,\text{V}}{0{,}10\,\text{A}} = \dfrac{3{,}5\,\text{V}}{0{,}10\,\text{A}} = 35\,\Omega$
**Vastaus:** $35\,\Omega$, kaksi merkitsevää numeroa kuten virrassa $0{,}10\,\text{A}$.
**Järkevyys:** Vastuksen yli on enemmän jännitettä kuin lampun yli, joten vastuksen resistanssi on suurempi kuin lampun, $2{,}5\,\text{V} : 0{,}10\,\text{A} = 25\,\Omega$. Tarkistus: kokonaisresistanssi $35\,\Omega + 25\,\Omega = 60\,\Omega$ antaa virran $6{,}0\,\text{V} : 60\,\Omega = 0{,}10\,\text{A}$.

## fy6-4-L2-03
**Annettu:** rinnan kytketyt vastukset $R_1 = 30\,\Omega$ ja tuntematon $R_2$, pariston jännite $U = 6{,}0\,\text{V}$, paristosta lähtevä virta $I = 0{,}50\,\text{A}$
**Kysytty:** tuntemattoman vastuksen resistanssi $R_2$
**Periaate:** Rinnankytkennässä kummankin vastuksen yli on pariston jännite, ja paristosta lähtevä virta on haaravirtojen summa. Tunnetun vastuksen virta saadaan Ohmin laista, ja loppu virrasta kulkee tuntemattoman vastuksen kautta.
**Kaava:** $I = I_1 + I_2$, $I_1 = \dfrac{U}{R_1}$ ja $I_2 = \dfrac{U}{R_2}$, josta $R_2 = \dfrac{U}{I - \dfrac{U}{R_1}}$
**Muunnokset:** Ei tarvita: jännite on voltteina, virta ampeereina ja resistanssi ohmeina.
**Sijoitus:** $I_1 = \dfrac{6{,}0\,\text{V}}{30\,\Omega} = 0{,}20\,\text{A}$ ja $R_2 = \dfrac{6{,}0\,\text{V}}{0{,}50\,\text{A} - 0{,}20\,\text{A}} = \dfrac{6{,}0\,\text{V}}{0{,}30\,\text{A}} = 20\,\Omega$
**Vastaus:** $20\,\Omega$, kaksi merkitsevää numeroa kuten annetuissa arvoissa.
**Järkevyys:** Tuntemattomassa haarassa kulkee suurempi virta, $0{,}30\,\text{A}$, joten sen resistanssi on pienempi kuin $30\,\Omega$. Tarkistus kokonaisresistanssilla: $\dfrac{30\,\Omega \cdot 20\,\Omega}{50\,\Omega} = 12\,\Omega$ ja $6{,}0\,\text{V} : 12\,\Omega = 0{,}50\,\text{A}$.

## fy6-4-L2-04
**Annettu:** rinnan kytketyt vastukset $R_1 = 2{,}2\,\text{k}\Omega$ ja $R_2 = 3{,}3\,\text{k}\Omega$
**Kysytty:** kokonaisresistanssi $R$ kilo-ohmeina
**Periaate:** Rinnankytkennässä kummankin vastuksen yli on sama jännite ja haaravirrat summautuvat, joten kokonaisresistanssin käänteisluku on käänteislukujen summa. Kahdelle vastukselle se voidaan ratkaista valmiiksi.
**Kaava:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$, josta $R = \dfrac{R_1 R_2}{R_1 + R_2}$
**Muunnokset:** $R_1 = 2{,}2 \cdot 1000\,\Omega = 2200\,\Omega$ ja $R_2 = 3{,}3 \cdot 1000\,\Omega = 3300\,\Omega$. Lopuksi $1\,\text{k}\Omega = 1000\,\Omega$.
**Sijoitus:** $R = \dfrac{2200\,\Omega \cdot 3300\,\Omega}{2200\,\Omega + 3300\,\Omega} = \dfrac{7\,260\,000\,\Omega^2}{5500\,\Omega} = 1320\,\Omega = 1{,}32\,\text{k}\Omega$
**Vastaus:** $1{,}3\,\text{k}\Omega$, kaksi merkitsevää numeroa kuten vastusten arvoissa.
**Järkevyys:** Tulos on pienempi kuin pienempi vastus $2{,}2\,\text{k}\Omega$. Kahdella $2{,}2\,\text{k}\Omega$:n vastuksella tulos olisi $1{,}1\,\text{k}\Omega$, ja nyt toinen vastus on suurempi, joten tulos on hieman suurempi. Laskun olisi voinut tehdä myös suoraan kilo-ohmeina, koska yksikkö on osoittajassa ja nimittäjässä.

## fy6-4-L3-01
**Annettu:** kuvasta pariston jännite $U = 12\,\text{V}$, vastus $R_1 = 40\,\Omega$ sarjassa rinnakkaisten vastusten $R_2 = 60\,\Omega$ ja $R_3 = 120\,\Omega$ kanssa
**Kysytty:** vastuksen $R_3$ virta $I_3$ milliampeereina
**Periaate:** Rinnakkaiset vastukset $R_2$ ja $R_3$ korvataan yhdellä vastuksella $R_{23}$, joka on sarjassa $R_1$:n kanssa. Paristosta lähtevä virta kulkee $R_1$:n ja koko rinnakkaisosan läpi. Rinnakkaisosan jännite on sama kummankin haaran yli, joten $R_3$:n virta saadaan siitä Ohmin laista.
**Kuvaajan lukeminen:** Kuvasta luetaan arvot $12\,\text{V}$, $R_1 = 40\,\Omega$, $R_2 = 60\,\Omega$ ja $R_3 = 120\,\Omega$. Vastukset $R_2$ ja $R_3$ ovat samojen kahden haarautumispisteen välissä eli rinnan, ja $R_1$ on niiden kanssa samassa silmukassa eli sarjassa.
**Kaava:** $R_{23} = \dfrac{R_2 R_3}{R_2 + R_3}$, $I = \dfrac{U}{R_1 + R_{23}}$, $U_{23} = R_{23} I$, josta $I_3 = \dfrac{U_{23}}{R_3}$
**Muunnokset:** Ei tarvita laskun aikana. Lopuksi $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** $R_{23} = \dfrac{60\,\Omega \cdot 120\,\Omega}{180\,\Omega} = 40\,\Omega$, $I = \dfrac{12\,\text{V}}{40\,\Omega + 40\,\Omega} = 0{,}15\,\text{A}$, $U_{23} = 40\,\Omega \cdot 0{,}15\,\text{A} = 6{,}0\,\text{V}$ ja $I_3 = \dfrac{6{,}0\,\text{V}}{120\,\Omega} = 0{,}050\,\text{A} = 50\,\text{mA}$
**Vastaus:** $50\,\text{mA}$, kaksi merkitsevää numeroa kuten jännitteessä $12\,\text{V}$.
**Järkevyys:** $R_2$:n virta on $6{,}0\,\text{V} : 60\,\Omega = 0{,}10\,\text{A}$, ja haaravirrat ovat yhteensä $0{,}10\,\text{A} + 0{,}050\,\text{A} = 0{,}15\,\text{A}$, sama kuin paristosta lähtevä virta. Suuremman resistanssin haarassa kulkee pienempi virta, kuten pitää.

## fy6-4-L3-02
**Annettu:** kaksi lämmitysvastusta, kumpikin $R_1 = 46\,\Omega$, verkkojännite $U = 230\,\text{V}$; resistanssi ei muutu
**Kysytty:** kuinka moninkertainen virta $I_\text{rinnan}$ on virtaan $I_\text{sarja}$ verrattuna
**Periaate:** Molemmissa kytkennöissä lämmittimen napojen välillä on sama verkkojännite, joten Ohmin lain mukaan lämmittimen virta riippuu vain kokonaisresistanssista. Sarjaan kytkettyjen yhtä suurten vastusten kokonaisresistanssi on kaksi kertaa yhden resistanssi, rinnan kytkettyjen puolet.
**Kaava:** $R_\text{sarja} = 2R_1$ ja $R_\text{rinnan} = \dfrac{R_1}{2}$, joten $\dfrac{I_\text{rinnan}}{I_\text{sarja}} = \dfrac{U : R_\text{rinnan}}{U : R_\text{sarja}} = \dfrac{R_\text{sarja}}{R_\text{rinnan}} = \dfrac{2R_1}{R_1 : 2} = 4$
**Muunnokset:** Ei tarvita: jännite ja resistanssi supistuvat suhteesta pois.
**Sijoitus:** Lukuarvoilla $I_\text{sarja} = \dfrac{230\,\text{V}}{92\,\Omega} = 2{,}5\,\text{A}$ ja $I_\text{rinnan} = \dfrac{230\,\text{V}}{23\,\Omega} = 10\,\text{A}$, joten $\dfrac{I_\text{rinnan}}{I_\text{sarja}} = \dfrac{10\,\text{A}}{2{,}5\,\text{A}} = 4{,}0$
**Vastaus:** $4$ kertaa. Suhde on tarkka, koska se ei riipu resistanssin eikä jännitteen arvosta, kun vastukset ovat yhtä suuret.
**Järkevyys:** Rinnankytkennässä kummankin vastuksen yli on koko $230\,\text{V}$, sarjaankytkennässä vain puolet. Siksi kummankin vastuksen virta on kaksinkertainen, ja haaroja on kaksi: yhteensä nelinkertainen virta. Suurempi virta vastaa suurempaa lämmitystehoa, kuten lämmittimen asennot lupaavat.

## fy6-4-L3-03
**Annettu:** sarjaankytkennän kokonaisresistanssi $R_\text{s} = 250\,\Omega$, rinnankytkennän $R_\text{r} = 60\,\Omega$
**Kysytty:** suuremman vastuksen resistanssi
**Periaate:** Sarjaankytkennässä resistanssit summautuvat, ja rinnankytkennän kokonaisresistanssi on resistanssien tulo jaettuna niiden summalla. Kahdesta yhtälöstä saadaan vastusten summa ja tulo, ja ne määräävät vastukset.
**Kaava:** $R_1 + R_2 = R_\text{s}$ ja $\dfrac{R_1 R_2}{R_1 + R_2} = R_\text{r}$, joten $R_1 R_2 = R_\text{r} R_\text{s}$. Kun $R_2 = R_\text{s} - R_1$, saadaan $R_1^2 - R_\text{s} R_1 + R_\text{r} R_\text{s} = 0$, josta $R_1 = \dfrac{R_\text{s} \pm \sqrt{R_\text{s}^2 - 4 R_\text{r} R_\text{s}}}{2}$
**Muunnokset:** Ei tarvita, molemmat resistanssit ovat ohmeina.
**Sijoitus:** $R_\text{r} R_\text{s} = 60\,\Omega \cdot 250\,\Omega = 15\,000\,\Omega^2$ ja $R_\text{s}^2 - 4 R_\text{r} R_\text{s} = 62\,500\,\Omega^2 - 60\,000\,\Omega^2 = 2500\,\Omega^2$, jonka neliöjuuri on $50\,\Omega$. Siis $R_1 = \dfrac{250\,\Omega \pm 50\,\Omega}{2}$, joten $R_1 = 150\,\Omega$ tai $R_1 = 100\,\Omega$
**Vastaus:** $150\,\Omega$; toinen vastus on $100\,\Omega$. Kaksi merkitsevää numeroa kuten rinnankytkennän arvossa $60\,\Omega$.
**Järkevyys:** Tarkistus: $150\,\Omega + 100\,\Omega = 250\,\Omega$ ja $\dfrac{150\,\Omega \cdot 100\,\Omega}{250\,\Omega} = 60\,\Omega$. Rinnankytkennän tulos on pienempi kuin pienempi vastus $100\,\Omega$, kuten pitää.
