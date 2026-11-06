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
**Periaate:** Sarjaankytkennässä pariston jännite jakautuu komponenttien kesken: jokainen varaus kulkee molempien lamppujen läpi, ja sen energia muuttuu lampuissa valoksi ja hehkulankojen sisäenergiaksi. Lamppujen jännitteiden summa on pariston jännite.
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
**Kuvan lukeminen:** Kuvasta luetaan arvot $12\,\text{V}$, $R_1 = 40\,\Omega$, $R_2 = 60\,\Omega$ ja $R_3 = 120\,\Omega$. Vastukset $R_2$ ja $R_3$ ovat samojen kahden haarautumispisteen välissä eli rinnan, ja koko paristosta lähtevä virta kulkee $R_1$:n läpi ja sitten rinnakkaisosaan, joten $R_1$ ja rinnakkaisosa ovat peräkkäin eli sarjassa.
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
**Kaava:** $R_1 + R_2 = R_\text{s}$ ja $R_1 R_2 = R_\text{r} R_\text{s}$ (rinnankytkennän kaavasta). Sijoitetaan $R_2 = R_\text{s} - R_1$, jolloin $R_1^2 - R_\text{s} R_1 + R_\text{r} R_\text{s} = 0$, josta $R_1 = \dfrac{R_\text{s} \pm \sqrt{R_\text{s}^2 - 4 R_\text{r} R_\text{s}}}{2}$
**Muunnokset:** Ei tarvita, molemmat resistanssit ovat ohmeina.
**Sijoitus:** $R_\text{r} R_\text{s} = 60\,\Omega \cdot 250\,\Omega = 15\,000\,\Omega^2$ ja $R_\text{s}^2 - 4 R_\text{r} R_\text{s} = 62\,500\,\Omega^2 - 60\,000\,\Omega^2 = 2500\,\Omega^2$, jonka neliöjuuri on $50\,\Omega$. Siis $R_1 = \dfrac{250\,\Omega \pm 50\,\Omega}{2}$, joten $R_1 = 150\,\Omega$ tai $R_1 = 100\,\Omega$
**Vastaus:** $150\,\Omega$; toinen vastus on $100\,\Omega$. Kaksi merkitsevää numeroa kuten arvossa $60\,\Omega$; data otetaan tarkkoina, sillä juuren alla oleva ero $62\,500 - 60\,000$ on pieni ja tulos herkkä datan viimeiselle numerolle.
**Järkevyys:** Tarkistus: $150\,\Omega + 100\,\Omega = 250\,\Omega$ ja $\dfrac{150\,\Omega \cdot 100\,\Omega}{250\,\Omega} = 60\,\Omega$. Rinnankytkennän tulos on pienempi kuin pienempi vastus $100\,\Omega$, kuten pitää.

## fy6-4-L1-06
**Kysytty:** mikä kolmen samanlaisen $100\,\Omega$:n vastuksen kytkentä antaa pienimmän kokonaisresistanssin.
**Periaate:** Rinnan lisätty vastus avaa virralle uuden kulkureitin ja pienentää kokonaisresistanssia, sarjaan lisätty vastus suurentaa sitä. Pienin kokonaisresistanssi saadaan siis, kun kaikki vastukset ovat rinnan. Laskemalla jokaisen kytkennän kokonaisresistanssi nähdään ero: kaikki rinnan $\tfrac{100\,\Omega}{3} \approx 33\,\Omega$, kaksi sarjaan ja kolmas rinnan $\tfrac{200 \cdot 100}{300}\,\Omega \approx 67\,\Omega$, kaksi rinnan ja kolmas sarjaan $50\,\Omega + 100\,\Omega = 150\,\Omega$ ja kaikki sarjaan $300\,\Omega$.
**Mallivastaus:** Pienin kokonaisresistanssi saadaan kytkemällä kaikki kolme vastusta rinnan, koska virralla on silloin kolme rinnakkaista kulkureittiä. Kokonaisresistanssi on $33\,\Omega$, ja se on pienempi kuin yhdenkään vastuksen resistanssi. Kaikkien kolmen sarjaankytkentä on suurin ($300\,\Omega$), ja sekakytkennät jäävät näiden väliin.

## fy6-4-L1-07
**Kysytty:** mitä kokonaisresistanssille ja paristosta lähtevälle virralle tapahtuu, kun rinnakkaisten lamppujen joukkoon lisätään kolmas lamppu.
**Periaate:** Rinnankytkennässä jokaisen haaran yli on pariston jännite $U$, ja jokainen haara ottaa virran $I = U : R$. Paristosta lähtevä virta on haaravirtojen summa, joten uusi haara kasvattaa sitä. Kun jännite pysyy samana ja virta kasvaa, Ohmin lain mukaan kokonaisresistanssi pienenee. Kaksi samanlaista lamppua, kummankin resistanssi $R_\text{L}$, antaa $\tfrac{R_\text{L}}{2}$ ja kolme antaa $\tfrac{R_\text{L}}{3}$.
**Mallivastaus:** Kokonaisresistanssi pienenee ja paristosta lähtevä virta kasvaa, koska uusi haara avaa virralle lisää kulkureittejä. Kumpikin vanha lamppu ottaa saman virran kuin ennenkin, ja kolmas lamppu lisää oman virtansa niiden päälle. Vastusten lisääminen suurentaa kokonaisresistanssia vain sarjaankytkennässä.

## fy6-4-L1-08
**Annettu:** rinnan kytketyt vastukset $R_1 = 90\,\Omega$ ja tuntematon $R_x$, kokonaisresistanssi $R = 36\,\Omega$
**Kysytty:** tuntemattoman vastuksen resistanssi $R_x$
**Periaate:** Rinnankytkennässä kokonaisresistanssin käänteisluku on haarojen käänteislukujen summa. Kun kokonaisresistanssi ja toinen haara tunnetaan, tuntemattoman haaran käänteisluku saadaan vähennyslaskulla, ja lopuksi se käännetään.
**Kaava:** $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_x}$, josta $\dfrac{1}{R_x} = \dfrac{1}{R} - \dfrac{1}{R_1}$
**Muunnokset:** Ei tarvita, kaikki resistanssit ovat ohmeina.
**Sijoitus:** $\dfrac{1}{R_x} = \dfrac{1}{36\,\Omega} - \dfrac{1}{90\,\Omega} = \dfrac{5 - 2}{180\,\Omega} = \dfrac{1}{60\,\Omega}$, joten $R_x = 60\,\Omega$
**Vastaus:** $60\,\Omega$, kaksi merkitsevää numeroa kuten annetuissa arvoissa.
**Järkevyys:** Rinnankytkennän tulos $36\,\Omega$ on pienempi kuin kumpikaan vastuksista, $90\,\Omega$ ja $60\,\Omega$. Tarkistus: $\dfrac{90\,\Omega \cdot 60\,\Omega}{90\,\Omega + 60\,\Omega} = \dfrac{5400\,\Omega^2}{150\,\Omega} = 36\,\Omega$.

## fy6-4-L2-05
**Annettu:** taulukosta yksittäiset resistanssit $R_1 = 217\,\Omega$, $R_2 = 328\,\Omega$ ja $R_3 = 468\,\Omega$, mitattu sarjaankytkentä $1009\,\Omega$ ja mitattu rinnankytkentä $101{,}4\,\Omega$; mittarin virheraja $\pm 1{,}5\,\%$ lukemasta
**Kysytty:** rinnankytkennän laskettu kokonaisresistanssi $R_\text{rinnan}$ ja onko ero mitattuun virherajan sisällä
**Periaate:** Kytkentöjen kaavat ennustavat kokonaisresistanssin yksittäisistä resistansseista. Sarjaankytkennässä resistanssit summautuvat, rinnankytkennässä käänteisluvut. Laskettua ja mitattua arvoa verrataan niin, että ero suhteutetaan mitattuun arvoon ja verrataan virherajaan.
**Kuvaajan lukeminen:** Ei kuvaajaa; arvot luetaan taulukosta.
**Kaava:** $R_\text{sarja} = R_1 + R_2 + R_3$ ja $\dfrac{1}{R_\text{rinnan}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3}$
**Muunnokset:** Ei tarvita, kaikki resistanssit ovat ohmeina.
**Sijoitus:** a) $R_\text{sarja} = 217\,\Omega + 328\,\Omega + 468\,\Omega = 1013\,\Omega$. Ero mitattuun on $1013\,\Omega - 1009\,\Omega = 4\,\Omega$ eli $\dfrac{4\,\Omega}{1009\,\Omega} \approx 0{,}4\,\%$, mikä on pienempi kuin $1{,}5\,\%$. b) $\dfrac{1}{R_\text{rinnan}} = \dfrac{1}{217\,\Omega} + \dfrac{1}{328\,\Omega} + \dfrac{1}{468\,\Omega} = 0{,}009\,794\,\dfrac{1}{\Omega}$, joten $R_\text{rinnan} = 102{,}1\,\Omega$. Ero mitattuun on $102{,}1\,\Omega - 101{,}4\,\Omega = 0{,}7\,\Omega$ eli $\dfrac{0{,}7\,\Omega}{101{,}4\,\Omega} \approx 0{,}7\,\%$.
**Vastaus:** $102\,\Omega$, kolme merkitsevää numeroa kuten mittaustuloksissa. Sarjaankytkennän ero on noin $0{,}4\,\%$ ja rinnankytkennän noin $0{,}7\,\%$, kumpikin virherajan $1{,}5\,\%$ sisällä, joten mittaus tukee kytkentöjen kaavoja.
**Järkevyys:** Laskettu rinnankytkentä on pienempi kuin pienin yksittäinen resistanssi $217\,\Omega$, ja sarjaankytkentä on suurempi kuin suurin, $468\,\Omega$, kuten pitää. Pyöristetyillä luvuilla $\tfrac{1}{200} + \tfrac{1}{300} + \tfrac{1}{500} = 0{,}010$, joten $R \approx 100\,\Omega$.

## fy6-4-L2-06
**Annettu:** paristo $U = 9{,}0\,\text{V}$, $R_1 = 100\,\Omega$ sarjassa rinnakkaisten $R_2 = R_3 = 200\,\Omega$ kanssa; mittarilukemat $I = 30{,}2\,\text{mA}$, $U_1 = 3{,}02\,\text{V}$ ja $U_{23} = 5{,}98\,\text{V}$
**Kysytty:** rinnakkaisosan resistanssi $R_{23}$ mittarilukemista ja kytkentävirheen syy
**Periaate:** Rinnakkaisosa on sarjassa vastuksen $R_1$ kanssa, joten paristosta lähtevä virta $I$ kulkee sen läpi. Ohmin lain mukaan rinnakkaisosan resistanssi on sen jännite jaettuna virralla. Tulosta verrataan arvoon, jonka rinnankytkennän kaava antaa vastuksille $200\,\Omega$ ja $200\,\Omega$.
**Kuvaajan lukeminen:** Ei kuvaajaa; arvot luetaan taulukosta.
**Kaava:** $R_{23} = \dfrac{U_{23}}{I}$ ja oikealla kytkennällä $R_{23} = \dfrac{R_2 R_3}{R_2 + R_3}$
**Muunnokset:** $I = 30{,}2\,\text{mA} = 30{,}2 \cdot 0{,}001\,\text{A} = 0{,}0302\,\text{A}$.
**Sijoitus:** $R_{23} = \dfrac{5{,}98\,\text{V}}{0{,}0302\,\text{A}} = 198\,\Omega$. Oikein kytketyllä piirillä $R_{23} = \dfrac{200\,\Omega \cdot 200\,\Omega}{400\,\Omega} = 100\,\Omega$. Vastuksen $R_1$ resistanssi mittarilukemista on $\dfrac{3{,}02\,\text{V}}{0{,}0302\,\text{A}} = 100\,\Omega$, joten $R_1$ on kunnossa.
**Vastaus:** a) $198\,\Omega$, kolme merkitsevää numeroa kuten lukemissa. Oikein kytketyssä piirissä sen pitäisi olla $100\,\Omega$. b) Mitattu arvo on likimain yhden $200\,\Omega$:n vastuksen resistanssi, joten toinen rinnakkaisista vastuksista ei ole mukana piirissä: sen johdin on irti tai haara poikki, ja virta kulkee vain yhden vastuksen kautta.
**Järkevyys:** Jos yksi haara puuttuu, kokonaisresistanssi on $100\,\Omega + 200\,\Omega = 300\,\Omega$ ja virta $9{,}0\,\text{V} : 300\,\Omega = 30\,\text{mA}$, mikä vastaa lukemaa $30{,}2\,\text{mA}$. Oikea kytkentä antaisi $9{,}0\,\text{V} : 200\,\Omega = 45\,\text{mA}$, joten mittaus eroaa selvästi siitä. Jännitteet summautuvat: $3{,}02\,\text{V} + 5{,}98\,\text{V} = 9{,}00\,\text{V}$.

## fy6-4-L2-07
**Annettu:** tunnettu vastus $R_1 = 60\,\Omega$ rinnan tuntemattoman $R_x$:n kanssa; mittaukset $(U;\ I)$: $(2{,}0\,\text{V};\ 83\,\text{mA})$, $(4{,}0\,\text{V};\ 166\,\text{mA})$, $(6{,}0\,\text{V};\ 247\,\text{mA})$, $(8{,}0\,\text{V};\ 333\,\text{mA})$ ja $(10{,}0\,\text{V};\ 414\,\text{mA})$
**Kysytty:** tuntemattoman vastuksen resistanssi $R_x$
**Periaate:** Rinnankytkentä käyttäytyy lähteen kannalta yhtenä vastuksena, jonka resistanssi saadaan Ohmin laista $R = U : I$. Mittaussarjan keskiarvo vähentää yksittäisen mittauksen hajontaa. Kun kokonaisresistanssi ja toinen haara tunnetaan, tuntematon haara saadaan rinnankytkennän kaavasta.
**Kuvaajan lukeminen:** Ei kuvaajaa; arvot luetaan taulukosta. Jos pisteet piirrettäisiin $(I;\ U)$-koordinaatistoon, ne asettuisivat origon kautta kulkevalle suoralle, jonka kulmakerroin on kokonaisresistanssi.
**Kaava:** $R = \dfrac{U}{I}$, $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_x}$, josta $\dfrac{1}{R_x} = \dfrac{1}{R} - \dfrac{1}{R_1}$
**Muunnokset:** $83\,\text{mA} = 83 \cdot 0{,}001\,\text{A} = 0{,}083\,\text{A}$, ja vastaavasti muut virrat.
**Sijoitus:** a) Suhteet $U : I$ ovat $24{,}1\,\Omega$, $24{,}1\,\Omega$, $24{,}3\,\Omega$, $24{,}0\,\Omega$ ja $24{,}2\,\Omega$. Niiden summa on $120{,}7\,\Omega$, joten keskiarvo on $R_\text{ka} = \dfrac{120{,}7\,\Omega}{5} = 24{,}13\,\Omega$. b) $\dfrac{1}{R_x} = \dfrac{1}{24{,}13\,\Omega} - \dfrac{1}{60\,\Omega} = 0{,}02477\,\dfrac{1}{\Omega}$, joten $R_x = 40{,}4\,\Omega$.
**Vastaus:** $40\,\Omega$, kaksi merkitsevää numeroa kuten jännitteissä ja virroissa; laskennassa pidetään yksi numero enemmän, $40{,}4\,\Omega$. Suhteet vaihtelevat vain välillä $24{,}0\,\Omega$ ja $24{,}3\,\Omega$, joten kokonaisresistanssi $24{,}1\,\Omega$ on luotettava.
**Järkevyys:** Kokonaisresistanssi $24{,}1\,\Omega$ on pienempi kuin kumpikaan haara, $60\,\Omega$ ja $40{,}4\,\Omega$, kuten rinnankytkennässä pitää. Tarkistus: $\dfrac{60\,\Omega \cdot 40{,}4\,\Omega}{100{,}4\,\Omega} = 24{,}1\,\Omega$.

## fy6-4-L3-04
**Annettu:** $R_1 = 70\,\Omega$ sarjassa rinnakkaisten $R_2 = 110\,\Omega$ ja $R_3 = 110\,\Omega$ kanssa; mitattu kokonaisresistanssi $180\,\Omega$; paristo $U = 9{,}0\,\text{V}$; ampeerimittarien lukemat: pariston virta $49{,}8\,\text{mA}$, $R_2$:n virta $49{,}7\,\text{mA}$ ja $R_3$:n virta $0{,}0\,\text{mA}$
**Kysytty:** a) oikein kytketyn levyn kokonaisresistanssi, b) vikaa selittävä kytkentä ja c) vastuksen $R_3$ virta $I_3$ korjatussa piirissä milliampeereina
**Periaate:** Oikein kytketty levy on sekakytkentä: rinnakkaiset $R_2$ ja $R_3$ korvataan yhdellä vastuksella $R_{23}$, joka on sarjassa vastuksen $R_1$ kanssa. Mitattua $180\,\Omega$ verrataan oikean kytkennän arvoon ja vian ehdokkaan arvoon. Virtamittarit kertovat, missä haarassa virtaa ei kulje. Korjatussa piirissä rinnakkaisosan jännite saadaan Ohmin laista ja jaetaan vastuksen $R_3$ resistanssilla.
**Kuvaajan lukeminen:** Ei kuvaajaa; arvot luetaan taulukosta.
**Kaava:** $R_{23} = \dfrac{R_2 R_3}{R_2 + R_3}$, $R = R_1 + R_{23}$, $I = \dfrac{U}{R}$, $U_{23} = R_{23} I$ ja $I_3 = \dfrac{U_{23}}{R_3}$
**Muunnokset:** Ei tarvita laskun aikana. Lopuksi $1\,\text{A} = 1000\,\text{mA}$.
**Sijoitus:** a) $R_{23} = \dfrac{110\,\Omega \cdot 110\,\Omega}{220\,\Omega} = 55\,\Omega$ ja $R = 70\,\Omega + 55\,\Omega = 125\,\Omega$. b) Jos toinen haara on irti, jäljellä on vain yksi $110\,\Omega$:n vastus, ja $R = 70\,\Omega + 110\,\Omega = 180\,\Omega$, mikä vastaa mittausta. Virta $R_3$:n johdossa on $0{,}0\,\text{mA}$ ja $R_2$:n virta on yhtä suuri kuin pariston virta, joten irti on $R_3$. c) Korjatussa piirissä $I = \dfrac{9{,}0\,\text{V}}{125\,\Omega} = 0{,}072\,\text{A}$, $U_{23} = 55\,\Omega \cdot 0{,}072\,\text{A} = 3{,}96\,\text{V}$ ja $I_3 = \dfrac{3{,}96\,\text{V}}{110\,\Omega} = 0{,}036\,\text{A} = 36\,\text{mA}$
**Vastaus:** $36\,\text{mA}$, kaksi merkitsevää numeroa kuten jännitteessä $9{,}0\,\text{V}$. Levyn kokonaisresistanssin pitäisi olla $125\,\Omega$, ja mittaukset selittyvät sillä, että vastus $R_3$ on irti johtimesta.
**Järkevyys:** Korjatussa piirissä kummankin yhtä suuren haaran virta on puolet kokonaisvirrasta, $0{,}072\,\text{A} : 2 = 0{,}036\,\text{A}$. Jännitteet summautuvat: $0{,}072\,\text{A} \cdot 70\,\Omega + 3{,}96\,\text{V} = 5{,}04\,\text{V} + 3{,}96\,\text{V} = 9{,}0\,\text{V}$.

## fy6-4-L3-05
**Annettu:** tavoite $R_\text{tav} = 470\,\Omega$; varaston vastukset $100\,\Omega$, $390\,\Omega$, $560\,\Omega$, $1200\,\Omega$, $1500\,\Omega$, $2700\,\Omega$ ja $5600\,\Omega$, yksi kutakin
**Kysytty:** parhaan kahden vastuksen kytkennän kokonaisresistanssi ja sen poikkeama arvosta $470\,\Omega$ prosentteina
**Periaate:** Sarjaankytkennän tulos on suurempi kuin kumpikaan vastuksista ja rinnankytkennän pienempi kuin kumpikaan. Tämä rajaa ehdokkaat ennen laskemista. Sarjaan sopivat vain pienet vastukset, rinnan vain suuret. Ehdokkaiden kokonaisresistanssit lasketaan ja poikkeama $\dfrac{|R - R_\text{tav}|}{R_\text{tav}}$ vertaillaan.
**Kuvaajan lukeminen:** Ei kuvaajaa; arvot luetaan tehtävästä.
**Kaava:** $R_\text{sarja} = R_a + R_b$, $R_\text{rinnan} = \dfrac{R_a R_b}{R_a + R_b}$ ja poikkeama $p = \dfrac{|R - R_\text{tav}|}{R_\text{tav}} \cdot 100\,\%$
**Muunnokset:** $1{,}2\,\text{k}\Omega = 1200\,\Omega$, $1{,}5\,\text{k}\Omega = 1500\,\Omega$, $2{,}7\,\text{k}\Omega = 2700\,\Omega$ ja $5{,}6\,\text{k}\Omega = 5600\,\Omega$.
**Sijoitus:** Sarjaankytkentä: tavoitetta $470\,\Omega$ pienempi vastus on vain $100\,\Omega$ ja $390\,\Omega$, ja niiden summa on $490\,\Omega$ (poikkeama $4{,}3\,\%$). Mikä tahansa muu sarjaankytkentä on vähintään $100\,\Omega + 560\,\Omega = 660\,\Omega$ ja huonompi. Rinnankytkentä: tulos on pienempi kuin pienempi vastus, joten pienemmän vastuksen on oltava yli $470\,\Omega$, eli kyseeseen tulevat vastukset $560\,\Omega$, $1200\,\Omega$, $1500\,\Omega$, $2700\,\Omega$ ja $5600\,\Omega$. Parit, joissa on $560\,\Omega$, antavat $382\,\Omega$, $408\,\Omega$, $\dfrac{560 \cdot 2700}{3260}\,\Omega = 463{,}8\,\Omega$ ja $509\,\Omega$. Muissa pareissa on pienempi vastus vähintään $1200\,\Omega$, joten tulos on suurempi kuin $\dfrac{1200 \cdot 1500}{2700}\,\Omega = 667\,\Omega$. Paras on siis $560\,\Omega$ rinnan $2700\,\Omega$:n kanssa: $R = 463{,}8\,\Omega$, ja $p = \dfrac{470 - 463{,}8}{470} \cdot 100\,\% = 1{,}32\,\%$
**Vastaus:** $1{,}3\,\%$, kaksi merkitsevää numeroa. Kytkentä on $560\,\Omega$ rinnan $2700\,\Omega$:n kanssa, kokonaisresistanssi $464\,\Omega$. Paras sarjaankytkentä ($100\,\Omega + 390\,\Omega$) poikkeaa $4{,}3\,\%$, joten rinnankytkentä on yli kolme kertaa tarkempi.
**Järkevyys:** Tulos $463{,}8\,\Omega$ on pienempi kuin $560\,\Omega$, kuten rinnankytkennässä pitää, ja lähellä tavoitetta.

## fy6-4-L2-08
**Kysytty:** viiden vastuskytkennän järjestys kokonaisresistanssin $R$ mukaan pienimmästä suurimpaan.
**Periaate:** Sarjaankytkennässä resistanssit lasketaan yhteen, $R = R_1 + R_2 + \dots$, joten kokonaisresistanssi on suurempi kuin yksikään vastuksista. Rinnankytkennässä $\tfrac{1}{R} = \tfrac{1}{R_1} + \tfrac{1}{R_2} + \dots$, ja lopuksi luku käännetään; kokonaisresistanssi on pienempi kuin pienin haaran resistanssi. Sekakytkennässä lasketaan ensin rinnakkainen osa ja sitten sarjaan kytketyt.
**Mallivastaus:** Kytkentä A on sarjaankytkentä:

$R_\text{A} = 220\,\Omega + 330\,\Omega = 550\,\Omega$

Kytkentä B on rinnankytkentä:

$R_\text{B} = \dfrac{220\,\Omega \cdot 330\,\Omega}{220\,\Omega + 330\,\Omega}$

$R_\text{B} = 132\,\Omega$

Kytkennässä C on kolme yhtä suurta haaraa:

$\dfrac{1}{R_\text{C}} = \dfrac{3}{330\,\Omega}$, eli $R_\text{C} = 110\,\Omega$

Kytkennässä D kaksi $330\,\Omega$:n vastusta rinnan on puolet yhdestä, $165\,\Omega$, ja sen kanssa sarjassa on $100\,\Omega$:

$R_\text{D} = 100\,\Omega + 165\,\Omega = 265\,\Omega$

Kytkennässä E on yksi vastus, $R_\text{E} = 150\,\Omega$.

Kokonaisresistanssin mukaan pienimmästä suurimpaan järjestys on C ($110\,\Omega$), B ($132\,\Omega$), E ($150\,\Omega$), D ($265\,\Omega$) ja A ($550\,\Omega$). Kytkennässä C on eniten vastuksia mutta pienin resistanssi, koska jokainen rinnakkainen haara on uusi kulkureitti. Kytkennän B resistanssi on pienempi kuin yksittäisen $150\,\Omega$:n vastuksen, vaikka kumpikin sen vastuksista on suurempi kuin $150\,\Omega$. Jos rinnankytkennässä unohtaa kääntää luvun $\tfrac{1}{R}$, kytkennän B luku $0{,}0076\,\tfrac{1}{\Omega}$ ja kytkennän C luku $0{,}0091\,\tfrac{1}{\Omega}$ näyttävät pienimmiltä, ja B ja C vaihtavat paikkaa.
