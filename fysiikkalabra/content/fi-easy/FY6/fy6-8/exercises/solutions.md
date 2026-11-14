## fy6-8-L1-01
**Annettu:** lähdejännite $E = 1{,}58\,\text{V}$, sisäinen resistanssi $R_\text{s} = 0{,}25\,\Omega$, virta $I = 0{,}80\,\text{A}$
**Kysytty:** napajännite $U$ voltteina
**Periaate:** Paristo on ideaalinen lähde, jonka kanssa on sarjassa sisäinen resistanssi. Kun paristosta otetaan virta, potentiaali laskee sisäisessä resistanssissa jännitteen $R_\text{s} I$ verran. Napojen välille jää siksi lähdejännitettä pienempi jännite.
**Kaava:** $U = E - R_\text{s} I$
**Muunnokset:** Ei tarvita: $1\,\Omega \cdot 1\,\text{A} = 1\,\text{V}$.
**Sijoitus:** $U = 1{,}58\,\text{V} - 0{,}25\,\Omega \cdot 0{,}80\,\text{A} = 1{,}58\,\text{V} - 0{,}20\,\text{V} = 1{,}38\,\text{V}$
**Vastaus:** $1{,}38\,\text{V}$. Vastaus on annettu sadasosavoltin tarkkuudella, kuten lähdejännite $1{,}58\,\text{V}$.
**Järkevyys:** Napajännite on lähdejännitettä pienempi, kuten virtaa antavalla paristolla kuuluu. Sisäisen resistanssin jännite $0{,}20\,\text{V}$ on noin kahdeksasosa lähdejännitteestä. Se sopii melko suureen virtaan $0{,}80\,\text{A}$.

## fy6-8-L1-02
**Annettu:** lähdejännite $E = 1{,}30\,\text{V}$ ja sisäinen resistanssi $R_\text{s} = 0{,}040\,\Omega$. Oikosulkujohtimen resistanssi jätetään huomiotta.
**Kysytty:** oikosulkuvirta $I_\text{k}$ ampeereina
**Periaate:** Oikosulussa ulkoisen piirin resistanssi on nolla. Kirchhoffin jännitelain mukaan koko lähdejännite jää silloin kennon sisäiselle resistanssille. Virtaa rajoittaa vain sisäinen resistanssi.
**Kaava:** $E - R_\text{s} I_\text{k} = 0$, josta $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I_\text{k} = \dfrac{1{,}30\,\text{V}}{0{,}040\,\Omega} = 32{,}5\,\text{A}$
**Vastaus:** $33\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten sisäisessä resistanssissa $0{,}040\,\Omega$.
**Järkevyys:** Arvio $1{,}3\,\text{V} : 0{,}04\,\Omega \approx 30\,\text{A}$. Ladattavan kennon sisäinen resistanssi on pieni, joten oikosulkuvirta on kymmeniä ampeereja. Niin suuri virta kuumentaa johtimen ja kennon nopeasti. Siksi oikosulku on vaarallinen.

## fy6-8-L1-03
**Annettu:** neljä paristoa sarjassa, kunkin lähdejännite $E_1 = 1{,}55\,\text{V}$
**Kysytty:** paristoryhmän lähdejännite $E$ voltteina
**Periaate:** Sarjaankytkennässä varaus kulkee jokaisen pariston läpi peräkkäin. Jokaisessa potentiaali nousee lähdejännitteen verran. Paristot ovat oikein päin, joten nousut summautuvat.
**Kaava:** $E = E_1 + E_2 + E_3 + E_4$, ja samanlaisille paristoille $E = 4E_1$
**Muunnokset:** Ei tarvita: jännitteet ovat voltteina.
**Sijoitus:** $E = 4 \cdot 1{,}55\,\text{V} = 6{,}20\,\text{V}$
**Vastaus:** $6{,}20\,\text{V}$. Vastauksessa on kolme merkitsevää numeroa, kuten pariston lähdejännitteessä $1{,}55\,\text{V}$.
**Järkevyys:** Neljän $1{,}5\,\text{V}$:n pariston ryhmältä odottaa noin $6\,\text{V}$. Tulos on sitä hieman suurempi. Syy on, että uuden pariston lähdejännite on vähän yli merkinnän $1{,}5\,\text{V}$.

## fy6-8-L1-04
**Annettu:** kolme samanlaista paristoa rinnan, kunkin sisäinen resistanssi $R_{\text{s}1} = 0{,}45\,\Omega$
**Kysytty:** paristoryhmän sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Rinnan kytkettyjen paristojen sisäiset resistanssit ovat rinnakkaisia haaroja samojen kahden kohdan välissä. Paristot ovat samanlaisia, joten virta jakautuu niille tasan. Ryhmän sisäinen resistanssi on yhden pariston sisäinen resistanssi jaettuna paristojen määrällä.
**Kaava:** $R_\text{s} = \dfrac{R_{\text{s}1}}{n}$
**Muunnokset:** Ei tarvita: resistanssi on ohmeina.
**Sijoitus:** $R_\text{s} = \dfrac{0{,}45\,\Omega}{3} = 0{,}15\,\Omega$
**Vastaus:** $0{,}15\,\Omega$. Vastauksessa on kaksi merkitsevää numeroa, kuten sisäisessä resistanssissa $0{,}45\,\Omega$. Paristojen määrä $3$ on tarkka luku.
**Järkevyys:** Rinnankytkennän resistanssi on pienempi kuin yhdenkään haaran resistanssi, ja $0{,}15\,\Omega < 0{,}45\,\Omega$. Tarkistetaan vielä vastusten rinnankytkennän yhtälöllä: $\tfrac{1}{R_\text{s}} = \tfrac{3}{0{,}45\,\Omega}$, joten $R_\text{s} = 0{,}15\,\Omega$.

## fy6-8-L1-05
**Annettu:** kuvaajan pisteet. Niiden kautta on piirretty suora, jota on jatkettu akseleille.
**Kysytty:** oikosulkuvirta $I_\text{k}$ ampeereina
**Periaate:** Oikosulussa napajännite on nolla. Pariston $(I, U)$-kuvaaja on suora $U = E - R_\text{s} I$. Oikosulkuvirta on siis se virta, jolla suora leikkaa vaaka-akselin. Oikosulkuvirtaa ei mitattu. Se saadaan jatkamalla pisteiden kautta piirrettyä suoraa.
**Kuvaajan lukeminen:** Katkoviivaksi jatkettu suora kohtaa vaaka-akselin, jossa $U = 0$, ruudukkoviivalla $3{,}0\,\text{A}$. Pystyakselin suora kohtaa kohdassa $4{,}5\,\text{V}$. Se on lähdejännite.
**Kaava:** $U = E - R_\text{s} I_\text{k} = 0$, josta $I_\text{k} = \dfrac{E}{R_\text{s}}$. Arvo luetaan suoran ja vaaka-akselin leikkauskohdasta.
**Muunnokset:** Ei tarvita: virta luetaan ampeereina.
**Sijoitus:** Kuvaajasta $I_\text{k} = 3{,}0\,\text{A}$.
**Vastaus:** $3{,}0\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, koska arvo luetaan $0{,}5\,\text{A}$:n ruudukolta.
**Järkevyys:** Suoran pisteistä $(0{,}40\,\text{A};\ 3{,}9\,\text{V})$ ja $(1{,}60\,\text{A};\ 2{,}1\,\text{V})$ saadaan $R_\text{s} = 1{,}8\,\text{V} : 1{,}20\,\text{A} = 1{,}5\,\Omega$. Siitä $I_\text{k} = E : R_\text{s} = 4{,}5\,\text{V} : 1{,}5\,\Omega = 3{,}0\,\text{A}$. Tulos pätee vain, jos sisäinen resistanssi pysyy samana myös mittausalueen ulkopuolella.

## fy6-8-L2-01
**Annettu:** ensimmäinen kuorma: $I_1 = 0{,}20\,\text{A}$ ja $U_1 = 4{,}30\,\text{V}$. Toinen kuorma: $I_2 = 0{,}80\,\text{A}$ ja $U_2 = 3{,}70\,\text{V}$.
**Kysytty:** sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Sama paristo on molemmissa mittauksissa, joten sen lähdejännite ja sisäinen resistanssi ovat samat. Napajännite $U = E - R_\text{s} I$ pienenee $R_\text{s}$:n verran jokaista virran ampeeria kohti. Kahden mittauksen erotuksesta lähdejännite siis häviää.
**Kaava:** $U_1 = E - R_\text{s} I_1$ ja $U_2 = E - R_\text{s} I_2$. Vähentämällä saadaan $U_1 - U_2 = R_\text{s}(I_2 - I_1)$, josta $R_\text{s} = \dfrac{U_1 - U_2}{I_2 - I_1}$.
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = \dfrac{4{,}30\,\text{V} - 3{,}70\,\text{V}}{0{,}80\,\text{A} - 0{,}20\,\text{A}} = \dfrac{0{,}60\,\text{V}}{0{,}60\,\text{A}} = 1{,}0\,\Omega$
**Vastaus:** $1{,}0\,\Omega$. Vastauksessa on kaksi merkitsevää numeroa, kuten erotuksissa $0{,}60\,\text{V}$ ja $0{,}60\,\text{A}$.
**Järkevyys:** Lähdejännite on $E = 4{,}30\,\text{V} + 1{,}0\,\Omega \cdot 0{,}20\,\text{A} = 4{,}50\,\text{V}$. Toinen mittaus antaa saman: $3{,}70\,\text{V} + 1{,}0\,\Omega \cdot 0{,}80\,\text{A} = 4{,}50\,\text{V}$. Kyseessä voi olla litteä $4{,}5\,\text{V}$:n paristo. Sen sisäinen resistanssi on ohmin luokkaa.

## fy6-8-L2-02
**Annettu:** lähdejännite $E = 6{,}0\,\text{V}$, sisäinen resistanssi $R_\text{s} = 0{,}50\,\Omega$, kuormitusvastus $R = 5{,}5\,\Omega$
**Kysytty:** napajännite $U$ voltteina
**Periaate:** Sisäinen resistanssi ja kuormitusvastus ovat samassa silmukassa sarjassa. Kirchhoffin jännitelaki $E - R_\text{s} I - RI = 0$ antaa siis virran. Napajännite on kuormitusvastuksen jännite, koska vastus on kytketty suoraan lähteen napoihin.
**Kaava:** $I = \dfrac{E}{R + R_\text{s}}$ ja $U = RI$. Siksi $U = \dfrac{R E}{R + R_\text{s}}$.
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I = \dfrac{6{,}0\,\text{V}}{5{,}5\,\Omega + 0{,}50\,\Omega} = 1{,}0\,\text{A}$ ja $U = 5{,}5\,\Omega \cdot 1{,}0\,\text{A} = 5{,}5\,\text{V}$
**Vastaus:** $5{,}5\,\text{V}$. Vastauksessa on kaksi merkitsevää numeroa, kuten lähtötiedoissa.
**Järkevyys:** Napajännitteen yhtälö antaa saman: $U = 6{,}0\,\text{V} - 0{,}50\,\Omega \cdot 1{,}0\,\text{A} = 5{,}5\,\text{V}$. Sisäinen resistanssi on vain noin kymmenesosa kuormasta. Siksi napajännite jää vain vähän lähdejännitettä pienemmäksi.

## fy6-8-L2-03
**Annettu:** lampun resistanssi $R = 3{,}0\,\Omega$, lähdejännite $E = 4{,}5\,\text{V}$, sisäinen resistanssi $R_\text{s} = 1{,}5\,\Omega$
**Kysytty:** lampun teho $P$ watteina
**Periaate:** Lamppu ja pariston sisäinen resistanssi ovat samassa silmukassa sarjassa. Jännitelaki antaa siis virran. Lampun jännite on pariston napajännite. Sähköteho on jännitteen ja virran tulo (luku *Sähköteho ja vastuksen lämpeneminen*).
**Kaava:** $I = \dfrac{E}{R + R_\text{s}}$, $U = E - R_\text{s} I$ ja $P = UI$
**Muunnokset:** Ei tarvita: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$.
**Sijoitus:** $I = \dfrac{4{,}5\,\text{V}}{3{,}0\,\Omega + 1{,}5\,\Omega} = 1{,}0\,\text{A}$, $U = 4{,}5\,\text{V} - 1{,}5\,\Omega \cdot 1{,}0\,\text{A} = 3{,}0\,\text{V}$ ja $P = 3{,}0\,\text{V} \cdot 1{,}0\,\text{A} = 3{,}0\,\text{W}$
**Vastaus:** $3{,}0\,\text{W}$. Vastauksessa on kaksi merkitsevää numeroa, kuten resistansseissa.
**Järkevyys:** Lähde antaa tehon $4{,}5\,\text{V} \cdot 1{,}0\,\text{A} = 4{,}5\,\text{W}$. Siitä $1{,}5\,\Omega \cdot (1{,}0\,\text{A})^2 = 1{,}5\,\text{W}$ muuttuu pariston sisäenergiaksi ja $3{,}0\,\text{W}$ siirtyy lamppuun: $1{,}5\,\text{W} + 3{,}0\,\text{W} = 4{,}5\,\text{W}$. Ilman sisäistä resistanssia lampun teho olisi suurempi.

## fy6-8-L2-04
**Annettu:** kaksi paristoa sarjassa, kummankin $E_1 = 1{,}5\,\text{V}$ ja $R_{\text{s}1} = 0{,}30\,\Omega$. Kuormitusvastus on $R = 2{,}4\,\Omega$.
**Kysytty:** virta $I$ ampeereina
**Periaate:** Sarjaan kytkettyjen paristojen lähdejännitteet summautuvat. Niiden sisäiset resistanssit ovat kuorman kanssa samassa silmukassa peräkkäin. Kirchhoffin jännitelaki antaa silmukan virran.
**Kaava:** $E = 2E_1$ ja $R_\text{s} = 2R_{\text{s}1}$. Siksi $I = \dfrac{E}{R + R_\text{s}} = \dfrac{2E_1}{R + 2R_{\text{s}1}}$.
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{2 \cdot 1{,}5\,\text{V}}{2{,}4\,\Omega + 2 \cdot 0{,}30\,\Omega} = \dfrac{3{,}0\,\text{V}}{3{,}0\,\Omega} = 1{,}0\,\text{A}$
**Vastaus:** $1{,}0\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten lähtötiedoissa.
**Järkevyys:** Ilman sisäisiä resistansseja virta olisi $3{,}0\,\text{V} : 2{,}4\,\Omega = 1{,}25\,\text{A}$. Sisäiset resistanssit pienentävät virtaa, kuten pitääkin. Napajännite on $2{,}4\,\Omega \cdot 1{,}0\,\text{A} = 2{,}4\,\text{V}$. Se on vähemmän kuin lähdejännite $3{,}0\,\text{V}$.

## fy6-8-L3-01
**Annettu:** kaksi samanlaista paristoa rinnan, kummankin $E_1 = 1{,}5\,\text{V}$ ja $R_{\text{s}1} = 0{,}40\,\Omega$. Lampun resistanssi on $R = 0{,}80\,\Omega$.
**Kysytty:** kunkin pariston läpi kulkeva virta $I_1$ ampeereina
**Periaate:** Rinnan kytkettyjen samanlaisten paristojen lähdejännite on sama kuin yhden. Sisäiset resistanssit ovat rinnakkaisia haaroja, joten ryhmän sisäinen resistanssi on puolet yhden pariston sisäisestä resistanssista. Ryhmä ja lamppu muodostavat silmukan, jonka virta saadaan jännitelaista. Paristot ovat samanlaisia. Virtalain mukaan kokonaisvirta jakautuu siksi niille tasan.
**Kaava:** $R_\text{s} = \dfrac{R_{\text{s}1}}{2}$, $I = \dfrac{E_1}{R + R_\text{s}}$ ja $I_1 = \dfrac{I}{2}$.
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $R_\text{s} = \dfrac{0{,}40\,\Omega}{2} = 0{,}20\,\Omega$, $I = \dfrac{1{,}5\,\text{V}}{0{,}80\,\Omega + 0{,}20\,\Omega} = 1{,}5\,\text{A}$ ja $I_1 = \dfrac{1{,}5\,\text{A}}{2} = 0{,}75\,\text{A}$
**Vastaus:** $0{,}75\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten lähtötiedoissa.
**Järkevyys:** Napajännite on $0{,}80\,\Omega \cdot 1{,}5\,\text{A} = 1{,}2\,\text{V}$. Kunkin pariston yli tämä on $1{,}5\,\text{V} - 0{,}40\,\Omega \cdot 0{,}75\,\text{A} = 1{,}2\,\text{V}$. Molemmat haarat antavat siis saman jännitteen. Yksi paristo yksinään antaisi vain $1{,}5\,\text{V} : 1{,}20\,\Omega = 1{,}25\,\text{A}$, ja sen pitäisi antaa koko virta itse.

## fy6-8-L3-02
**Annettu:** kolme paristoa sarjassa, yksi väärin päin. Kunkin $E_1 = 1{,}5\,\text{V}$ ja $R_{\text{s}1} = 0{,}25\,\Omega$. Lampun resistanssi on $R = 4{,}0\,\Omega$.
**Kysytty:** lampun läpi kulkeva virta $I$ ampeereina
**Periaate:** Sarjaankytkennässä potentiaalin muutokset summautuvat. Oikein päin olevissa paristoissa potentiaali nousee $E_1$:n verran. Väärin päin olevassa se laskee saman verran. Ryhmän lähdejännite on siksi $E_1 + E_1 - E_1$. Kaikkien kolmen sisäinen resistanssi on silti samassa silmukassa peräkkäin.
**Kaava:** $E = E_1 + E_1 - E_1 = E_1$ ja $R_\text{s} = 3R_{\text{s}1}$. Siksi $I = \dfrac{E}{R + R_\text{s}} = \dfrac{E_1}{R + 3R_{\text{s}1}}$.
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{1{,}5\,\text{V}}{4{,}0\,\Omega + 3 \cdot 0{,}25\,\Omega} = \dfrac{1{,}5\,\text{V}}{4{,}75\,\Omega} = 0{,}3158\,\text{A}$
**Vastaus:** $0{,}32\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten lähtötiedoissa.
**Järkevyys:** Oikein asetettuna ryhmän lähdejännite olisi $4{,}5\,\text{V}$ ja virta $4{,}5\,\text{V} : 4{,}75\,\Omega = 0{,}95\,\text{A}$. Se on kolminkertainen. Lamppu hehkuu siis selvästi himmeämmin. Se on tavallinen merkki väärin päin asetetusta paristosta.

## fy6-8-L3-03
**Annettu:** kuorma $R_1 = 2{,}0\,\Omega$ ja napajännite $U_1 = 1{,}20\,\text{V}$. Kuorma $R_2 = 6{,}0\,\Omega$ ja napajännite $U_2 = 1{,}44\,\text{V}$.
**Kysytty:** lähdejännite $E$ voltteina
**Periaate:** Napajännite on kuormitusvastuksen jännite, joten Ohmin laki antaa kummankin mittauksen virran. Sama paristo on molemmissa mittauksissa, joten $U = E - R_\text{s} I$ pätee samoilla $E$:llä ja $R_\text{s}$:llä. Kahdesta yhtälöstä ratkaistaan ensin sisäinen resistanssi ja sitten lähdejännite.
**Kaava:** $I_1 = \dfrac{U_1}{R_1}$ ja $I_2 = \dfrac{U_2}{R_2}$. Lisäksi $U_1 = E - R_\text{s} I_1$ ja $U_2 = E - R_\text{s} I_2$. Näistä saadaan $R_\text{s} = \dfrac{U_2 - U_1}{I_1 - I_2}$ ja $E = U_1 + R_\text{s} I_1$.
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I_1 = \dfrac{1{,}20\,\text{V}}{2{,}0\,\Omega} = 0{,}60\,\text{A}$, $I_2 = \dfrac{1{,}44\,\text{V}}{6{,}0\,\Omega} = 0{,}24\,\text{A}$, $R_\text{s} = \dfrac{1{,}44\,\text{V} - 1{,}20\,\text{V}}{0{,}60\,\text{A} - 0{,}24\,\text{A}} = 0{,}667\,\Omega$ ja $E = 1{,}20\,\text{V} + 0{,}667\,\Omega \cdot 0{,}60\,\text{A} = 1{,}60\,\text{V}$
**Vastaus:** $1{,}60\,\text{V}$. Vastaus on annettu sadasosavoltin tarkkuudella, kuten mitatut napajännitteet.
**Järkevyys:** Toinen mittaus antaa saman: $1{,}44\,\text{V} + 0{,}667\,\Omega \cdot 0{,}24\,\text{A} = 1{,}60\,\text{V}$. Lähdejännite on suurempi kuin kumpikin napajännite, kuten pitääkin. Lisäksi $1{,}60\,\text{V}$ on tyypillinen uuden AA-pariston lähdejännite.

## fy6-8-L1-06
**Kysytty:** milloin pariston napajännite on yhtä suuri kuin sen lähdejännite.
**Periaate:** Napajännite on $U = E - R_\text{s} I$. Tässä $R_\text{s} I$ on jännitehäviö pariston sisäisessä resistanssissa. Napajännite on yhtä suuri kuin lähdejännite vain silloin, kun tämä jännitehäviö on nolla. Silloin paristosta ei oteta virtaa.
**Mallivastaus:** Napajännite on yhtä suuri kuin lähdejännite, kun paristosta ei oteta virtaa. Silloin sisäisessä resistanssissa ei synny jännitehäviötä. Jos virta on suuri, jännitehäviö on suuri ja navoille jää lähdejännitettä pienempi jännite. Virta on suurin oikosulussa, ja silloin napajännite on nolla. Kun kuormitusvastus on yhtä suuri kuin sisäinen resistanssi, napajännite on vain puolet lähdejännitteestä. Väite ”jännitteet ovat aina yhtä suuret” ei pidä paikkaansa. Lähdejännite on pariston ominaisuus, mutta napajännite riippuu otettavasta virrasta.

## fy6-8-L1-07
**Kysytty:** mitä pariston oikosulussa tapahtuu.
**Periaate:** Virta on $I = E : (R + R_\text{s})$. Oikosulussa ulkoisen piirin resistanssi on $R \approx 0$. Virtaa rajoittaa silloin vain pariston sisäinen resistanssi. Virta on oikosulkuvirta $I_\text{k} = E : R_\text{s}$. Paristoissa $R_\text{s}$ on pieni, joten oikosulkuvirta on suuri.
**Mallivastaus:** Oikosulussa virta kasvaa suureksi, koska sitä rajoittaa vain pariston sisäinen resistanssi. Koko lähdejännite jää sisäisen resistanssin yli. Napajännite on siksi lähes nolla, ja pariston sisäenergia kasvaa nopeasti. Siksi oikosulku on vaarallinen ja voi vahingoittaa paristoa. Virta ei pienene nollaan eikä pysy ennallaan, koska virran määrää koko piirin resistanssi. Napajännite ei myöskään voi olla suurempi kuin lähdejännite.

## fy6-8-L1-08
**Annettu:** lähdejännite $E = 1{,}50\,\text{V}$, napajännite $U = 1{,}31\,\text{V}$, virta $I = 0{,}50\,\text{A}$
**Kysytty:** sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Napajännite on lähdejännitettä pienempi sisäisen resistanssin jännitehäviön $R_\text{s} I$ verran. Kun lähdejännite, napajännite ja virta tunnetaan, yhtälöstä voidaan ratkaista $R_\text{s}$.
**Kaava:** $U = E - R_\text{s} I$, josta $R_\text{s} = \dfrac{E - U}{I}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = \dfrac{1{,}50\,\text{V} - 1{,}31\,\text{V}}{0{,}50\,\text{A}} = \dfrac{0{,}19\,\text{V}}{0{,}50\,\text{A}} = 0{,}38\,\Omega$
**Vastaus:** $0{,}38\,\Omega$. Vastauksessa on kaksi merkitsevää numeroa, kuten virrassa $0{,}50\,\text{A}$.
**Järkevyys:** Jännitehäviö on $0{,}38\,\Omega \cdot 0{,}50\,\text{A} = 0{,}19\,\text{V}$. Lisäksi $1{,}50\,\text{V} - 0{,}19\,\text{V} = 1{,}31\,\text{V}$, ja se on annettu napajännite. Oikosulkuvirta olisi $1{,}50\,\text{V} : 0{,}38\,\Omega \approx 3{,}9\,\text{A}$. Se on tavallinen suuruus uudelle paristolle.

## fy6-8-L2-05
**Annettu:** taulukon mittauspisteet $(I;\ U)$: $(0{,}20\,\text{A};\ 1{,}43\,\text{V})$, $(0{,}40\,\text{A};\ 1{,}31\,\text{V})$, $(0{,}60\,\text{A};\ 1{,}20\,\text{V})$, $(0{,}80\,\text{A};\ 1{,}10\,\text{V})$, $(1{,}00\,\text{A};\ 0{,}99\,\text{V})$ ja $(1{,}20\,\text{A};\ 0{,}86\,\text{V})$ (esimerkkiaineisto)
**Kysytty:** a) lähdejännite $E$ suoralta luettuna, b) sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Pariston napajännite on $U = E - R_\text{s} I$. Siksi $(I, U)$-pisteet ovat laskevalla suoralla. Suora leikkaa pystyakselin kohdassa $U = E$, ja sen kulmakerroin on $-R_\text{s}$. Mittauspisteissä on pientä hajontaa. Suora piirretään pisteiden joukon keskeltä, eikä sitä sidota yksittäisiin pisteisiin.
**Kuvaajan lukeminen:** Sovitettu suora leikkaa pystyakselin kohdassa $1{,}54\,\text{V}$. Se kulkee likimain pisteen $(1{,}20\,\text{A};\ 0{,}87\,\text{V})$ kautta. Pisteet jäävät suoran molemmille puolille. Jos suora käännetään pisteiden rajoissa toisenlaiseksi, kulmakerroin muuttuu noin $\pm 0{,}03\,\Omega$. Kaksi suoralta luettua pistettä ovat kaukana toisistaan: $(0\,\text{A};\ 1{,}54\,\text{V})$ ja $(1{,}20\,\text{A};\ 0{,}87\,\text{V})$.
**Kaava:** $R_\text{s} = -\dfrac{\Delta U}{\Delta I} = \dfrac{U_1 - U_2}{I_2 - I_1}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = \dfrac{1{,}54\,\text{V} - 0{,}87\,\text{V}}{1{,}20\,\text{A} - 0\,\text{A}} = \dfrac{0{,}67\,\text{V}}{1{,}20\,\text{A}} = 0{,}558\,\Omega$
**Vastaus:** a) $E \approx 1{,}54\,\text{V}$. b) $R_\text{s} \approx 0{,}56\,\Omega$. Vastauksessa on kaksi merkitsevää numeroa, koska suora sovitetaan silmämääräisesti. Silmämääräinen sovitus vaihtelee: kulmakerroin voi muuttua noin $\pm 0{,}03\,\Omega$. Arvo väliltä $0{,}53\text{–}0{,}59\,\Omega$ on siis hyvä vastaus.
**Järkevyys:** Mallin mukaan virralla $0{,}60\,\text{A}$ napajännite on $1{,}54\,\text{V} - 0{,}56\,\Omega \cdot 0{,}60\,\text{A} = 1{,}20\,\text{V}$. Se on taulukon kolmas arvo. Lähdejännite on suurempi kuin yksikään mitattu napajännite, kuten pitää. Oikosulkuvirta olisi $1{,}54\,\text{V} : 0{,}56\,\Omega \approx 2{,}8\,\text{A}$. Se on suoran jatke mittausalueen ulkopuolelle, eikä sitä mitata.

## fy6-8-L2-06
**Annettu:** taulukon mittauspisteet $(I;\ U_\text{A};\ U_\text{B})$ virroilla $0{,}10\,\text{A}$ … $1{,}00\,\text{A}$. A-pariston napajännite pienenee arvosta $1{,}55\,\text{V}$ arvoon $1{,}10\,\text{V}$. B-pariston napajännite pienenee arvosta $1{,}47\,\text{V}$ arvoon $1{,}27\,\text{V}$ (esimerkkiaineisto).
**Kysytty:** a) virta $I$, jolla napajännitteet ovat yhtä suuret; b) kumpi paristo on parempi suurella virralla ja miksi
**Periaate:** Kumpikin paristo noudattaa mallia $U = E - R_\text{s} I$. Kummankin pisteet sopivat siis omalle laskevalle suoralleen. Suorien leikkauskohdassa napajännitteet ovat yhtä suuret. Suoran kulmakerroin on $-R_\text{s}$, joten loivempi suora tarkoittaa pienempää sisäistä resistanssia.
**Kuvaajan lukeminen:** A-pariston suora kulkee pisteiden $(0\,\text{A};\ 1{,}60\,\text{V})$ ja $(1{,}00\,\text{A};\ 1{,}10\,\text{V})$ kautta. Siis $E_\text{A} = 1{,}60\,\text{V}$ ja $R_\text{A} = 0{,}50\,\Omega$. B-pariston suora kulkee pisteiden $(0\,\text{A};\ 1{,}49\,\text{V})$ ja $(1{,}00\,\text{A};\ 1{,}27\,\text{V})$ kautta. Siis $E_\text{B} = 1{,}49\,\text{V}$ ja $R_\text{B} = 0{,}22\,\Omega$. Suorat leikkaavat kuvaajassa noin virralla $0{,}4\,\text{A}$, taulukon rivien $0{,}30\,\text{A}$ ja $0{,}50\,\text{A}$ välissä. Ensin A:n napajännite on suurempi ($1{,}45\,\text{V}$ ja $1{,}42\,\text{V}$), sitten B:n ($1{,}35\,\text{V}$ ja $1{,}38\,\text{V}$).
**Kaava:** $E_\text{A} - R_\text{A} I = E_\text{B} - R_\text{B} I$, josta $I = \dfrac{E_\text{A} - E_\text{B}}{R_\text{A} - R_\text{B}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.
**Sijoitus:** $I = \dfrac{1{,}60\,\text{V} - 1{,}49\,\text{V}}{0{,}50\,\Omega - 0{,}22\,\Omega} = \dfrac{0{,}11\,\text{V}}{0{,}28\,\Omega} = 0{,}39\,\text{A}$
**Vastaus:** a) Noin $0{,}40\,\text{A}$. Kuvaajan lukeminen ja laskenta antavat arvon väliltä $0{,}35\text{–}0{,}45\,\text{A}$, koska suorien sovitus vaihtelee. b) Suurella virralla parempi on paristo B. Sen sisäinen resistanssi $0{,}22\,\Omega$ on pienempi kuin pariston A $0{,}50\,\Omega$, joten sen napajännite pienenee virran kasvaessa loivemmin. Pariston A lähdejännite on suurempi. Siksi pienellä virralla, alle $0{,}4\,\text{A}$, paristo A antaa korkeamman napajännitteen. Virralla $1{,}00\,\text{A}$ napajännite on paristolla A $1{,}10\,\text{V}$ ja paristolla B $1{,}27\,\text{V}$.
**Järkevyys:** Virralla $0{,}40\,\text{A}$ pariston A napajännite on $1{,}60\,\text{V} - 0{,}50\,\Omega \cdot 0{,}40\,\text{A} = 1{,}40\,\text{V}$. Pariston B napajännite on $1{,}49\,\text{V} - 0{,}22\,\Omega \cdot 0{,}40\,\text{A} = 1{,}40\,\text{V}$. Tämä on taulukon rivien $0{,}30\,\text{A}$ ja $0{,}50\,\text{A}$ välissä, kuten pitää. Oikosulkuvirta on paristolla B $1{,}49\,\text{V} : 0{,}22\,\Omega \approx 6{,}8\,\text{A}$ ja paristolla A $1{,}60\,\text{V} : 0{,}50\,\Omega = 3{,}2\,\text{A}$. B pystyy siis antamaan suuremman virran.

## fy6-8-L2-07
**Kysytty:** mikä väite oppilaan päätelmästä, että sisäinen resistanssi on nolla, on oikein.
**Periaate:** Napajännite on $U = E - R_\text{s} I$. Kun jännitemittari on kytketty ilman kuormaa, sen läpi kulkee häviävän pieni virta. Siksi $I \approx 0$ ja jännitehäviö sisäisessä resistanssissa on nolla. Silloin $U = E$, vaikka sisäinen resistanssi olisi kuinka suuri.
**Mallivastaus:** Oppilaan päätelmä on virheellinen. Ilman kuormaa mitattu jännite $1{,}58\,\text{V}$ on pariston lähdejännite, koska virta on nolla eikä sisäisessä resistanssissa synny jännitehäviötä. Sama jännite näkyisi, vaikka sisäinen resistanssi olisi suuri. Yksi mittaus ilman virtaa ei siis kerro sisäisestä resistanssista mitään. Jännitemittarin virta on hyvin pieni, joten mittari ei itse pienennä jännitettä. Sisäinen resistanssi ei myöskään ole ääretön, vaikka virta on nolla, koska se on pariston vakio-ominaisuus. Sisäinen resistanssi saadaan mittaamalla napajännite ja virta kuormitettuna, mieluiten usealla kuormalla. Sitten lasketaan $R_\text{s} = (E - U) : I$ tai luetaan kuvaajan kulmakertoimesta.

## fy6-8-L3-04
**Annettu:** taulukon mittauspisteet virroilla $0{,}10\,\text{A}$ … $0{,}50\,\text{A}$. Uuden pariston napajännite pienenee arvosta $1{,}56\,\text{V}$ arvoon $1{,}46\,\text{V}$ ja ikääntyneen arvosta $1{,}41\,\text{V}$ arvoon $0{,}97\,\text{V}$ (esimerkkiaineisto). Kuormitusvastus on $R = 2{,}0\,\Omega$.
**Kysytty:** a) kummankin pariston $E$ ja $R_\text{s}$; b) osuus ikääntyneen pariston kehittämästä sähkötehosta, joka muuttuu pariston sisäenergiaksi, prosentteina; c) vastukseen siirtyvä teho vastuksilla $0{,}55\,\Omega$, $1{,}1\,\Omega$, $2{,}2\,\Omega$ ja $4{,}4\,\Omega$ sekä se kuorma, jolla teho on suurin
**Periaate:** Kummankin pariston napajännite noudattaa mallia $U = E - R_\text{s} I$. Sovitetun suoran leikkaus pystyakselilla on siis $E$, ja kulmakerroin on $-R_\text{s}$. Kuormitettuna virta on $I = E : (R + R_\text{s})$. Pariston kehittämä teho on $P = EI$. Sisäiseen resistanssiin muuttuu teho $R_\text{s} I^2$ ja kuormaan teho $RI^2$. Tehon lauseke saadaan sähkötehon kaavasta (luku *Sähköteho ja vastuksen lämpeneminen*).
**Kuvaajan lukeminen:** Uuden pariston suora kulkee pisteiden $(0{,}10\,\text{A};\ 1{,}56\,\text{V})$ ja $(0{,}50\,\text{A};\ 1{,}46\,\text{V})$ kautta. Ikääntyneen pariston suora kulkee pisteiden $(0{,}10\,\text{A};\ 1{,}41\,\text{V})$ ja $(0{,}50\,\text{A};\ 0{,}97\,\text{V})$ kautta. Kummankin pariston pisteet jäävät suoran molemmille puolille.
**Kaava:** $R_\text{s} = \dfrac{U_1 - U_2}{I_2 - I_1}$ ja $E = U_1 + R_\text{s} I_1$

$I = \dfrac{E}{R + R_\text{s}}$

$\text{osuus} = \dfrac{R_\text{s} I^2}{EI} = \dfrac{R_\text{s}}{R + R_\text{s}}$

$P = RI^2 = \dfrac{E^2 R}{(R + R_\text{s})^2}$
**Muunnokset:** Ei tarvita: kaikki suureet ovat perusyksiköissä.
**Sijoitus:** a) Uusi: $R_\text{s} = \dfrac{0{,}10\,\text{V}}{0{,}40\,\text{A}} = 0{,}25\,\Omega$ ja $E = 1{,}56\,\text{V} + 0{,}25\,\Omega \cdot 0{,}10\,\text{A} = 1{,}58\,\text{V}$. Ikääntynyt: $R_\text{s} = \dfrac{1{,}41\,\text{V} - 0{,}97\,\text{V}}{0{,}40\,\text{A}} = 1{,}10\,\Omega$ ja $E = 1{,}41\,\text{V} + 1{,}10\,\Omega \cdot 0{,}10\,\text{A} = 1{,}52\,\text{V}$.
b) Ikääntynyt: $I = \dfrac{1{,}52\,\text{V}}{2{,}0\,\Omega + 1{,}10\,\Omega} = 0{,}490\,\text{A}$. Kehitetty teho on $EI = 1{,}52\,\text{V} \cdot 0{,}490\,\text{A} = 0{,}745\,\text{W}$. Paristoon jäävä teho on $R_\text{s} I^2 = 1{,}10\,\Omega \cdot (0{,}490\,\text{A})^2 = 0{,}264\,\text{W}$. Osuus on $\dfrac{0{,}264\,\text{W}}{0{,}745\,\text{W}} = \dfrac{1{,}10\,\Omega}{3{,}10\,\Omega} = 0{,}355$. Uusi paristo: $\dfrac{0{,}25\,\Omega}{2{,}0\,\Omega + 0{,}25\,\Omega} = 0{,}11$.
c) Ikääntyneelle ($E = 1{,}52\,\text{V}$, $R_\text{s} = 1{,}10\,\Omega$): $R = 0{,}55\,\Omega$: $P = \dfrac{(1{,}52\,\text{V})^2 \cdot 0{,}55\,\Omega}{(1{,}65\,\Omega)^2} = 0{,}47\,\text{W}$. $R = 1{,}1\,\Omega$: $P = \dfrac{(1{,}52\,\text{V})^2 \cdot 1{,}1\,\Omega}{(2{,}2\,\Omega)^2} = 0{,}53\,\text{W}$. $R = 2{,}2\,\Omega$: $P = 0{,}47\,\text{W}$. $R = 4{,}4\,\Omega$: $P = 0{,}34\,\text{W}$. Osuus, joka muuttuu pariston sisäenergiaksi, kun $R = 1{,}1\,\Omega$: $\dfrac{1{,}10\,\Omega}{2{,}2\,\Omega} = 0{,}50$.
**Vastaus:** Vastauslaatikkoon $35\,\%$. a) Uusi paristo: $E = 1{,}58\,\text{V}$, $R_\text{s} = 0{,}25\,\Omega$. Ikääntynyt paristo: $E = 1{,}52\,\text{V}$, $R_\text{s} = 1{,}1\,\Omega$.
b) Vastauslaatikkoon: noin $35\,\%$ ikääntyneen pariston kehittämästä tehosta muuttuu pariston sisäenergiaksi. Vastauksessa on kaksi merkitsevää numeroa, kuten kuorman $2{,}0\,\Omega$ tarkkuudessa. Uudella paristolla osuus on vain noin $11\,\%$, koska sen sisäinen resistanssi $0{,}25\,\Omega$ on paljon pienempi.
c) Teho on suurin, noin $0{,}53\,\text{W}$, kuormalla $1{,}1\,\Omega$. Se on yhtä suuri kuin sisäinen resistanssi. Silloin puolet kehitetystä tehosta muuttuu pariston sisäenergiaksi.
**Järkevyys:** Tehot täsmäävät: $0{,}264\,\text{W} + 2{,}0\,\Omega \cdot (0{,}490\,\text{A})^2 = 0{,}264\,\text{W} + 0{,}481\,\text{W} = 0{,}745\,\text{W}$, kuten kehitetty teho. Ikääntyneen pariston lähdejännite on vain hieman pienempi kuin uuden. Sisäinen resistanssi on kuitenkin yli nelinkertainen. Siksi ikääntynyt paristo lämpenee paljon enemmän ja antaa kuormalle vähemmän tehoa. Tehon maksimi on loiva, kuten arvot $0{,}47\,\text{W}$, $0{,}53\,\text{W}$ ja $0{,}47\,\text{W}$ näyttävät. Silti suurimmallakin teholla puolet energiasta menee hukkaan. Siksi laitteissa kuorma valitaan yleensä suuremmaksi kuin $R_\text{s}$.

## fy6-8-L3-05
**Annettu:** taulukon mittauspisteet $(I;\ U)$ virroilla $0{,}50\,\text{A}$ … $3{,}00\,\text{A}$. Jännite pienenee arvosta $5{,}56\,\text{V}$ arvoon $2{,}79\,\text{V}$ (esimerkkiaineisto). Johtimien yhteenlaskettu resistanssi on $R_\text{j} = 0{,}30\,\Omega$. Oppilaan kulmakerroin on $1{,}1\,\Omega$ ja oikosulkuvirta $5{,}6\,\text{A}$.
**Kysytty:** a) lähdejännite $E$; b) oppilaan virhe ja paristoryhmän oikea sisäinen resistanssi; c) paristoryhmän oikea oikosulkuvirta $I_\text{k}$ ampeereina
**Periaate:** Jännitemittari on kuormitusvastuksen navoissa. Se näyttää siksi jännitteen, joka on pienempi kuin paristoryhmän napajännite. Erotus on johtimien jännitehäviö $R_\text{j} I$: $U = E - R_\text{s} I - R_\text{j} I = E - (R_\text{s} + R_\text{j}) I$. Kuvaajan kulmakerroin on siis $-(R_\text{s} + R_\text{j})$, ja oppilaan luku sisältää johtimien resistanssin. Paristoryhmän oma sisäinen resistanssi saadaan vähentämällä $R_\text{j}$. Oikosulkuvirta lasketaan siitä.
**Kuvaajan lukeminen:** Sovitettu suora kulkee pisteiden $(0{,}50\,\text{A};\ 5{,}56\,\text{V})$ ja $(3{,}00\,\text{A};\ 2{,}80\,\text{V})$ kautta. Pisteet jäävät suoran molemmille puolille. Suora leikkaa pystyakselin kohdassa $6{,}11\,\text{V}$. Se on lähdejännite, koska kun virta on nolla, johtimissa ei ole jännitehäviötä.
**Kaava:** $E = U_1 + (R_\text{s} + R_\text{j}) I_1$; $R_\text{s} + R_\text{j} = \dfrac{U_1 - U_2}{I_2 - I_1}$; $R_\text{s} = (R_\text{s} + R_\text{j}) - R_\text{j}$; $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Muunnokset:** Ei tarvita: $1\,\text{V} : 1\,\text{A} = 1\,\Omega$.
**Sijoitus:** a) $R_\text{s} + R_\text{j} = \dfrac{5{,}56\,\text{V} - 2{,}80\,\text{V}}{3{,}00\,\text{A} - 0{,}50\,\text{A}} = \dfrac{2{,}76\,\text{V}}{2{,}50\,\text{A}} = 1{,}10\,\Omega$

$E = 5{,}56\,\text{V} + 1{,}10\,\Omega \cdot 0{,}50\,\text{A} = 6{,}11\,\text{V}$
b) $R_\text{s} = 1{,}10\,\Omega - 0{,}30\,\Omega = 0{,}80\,\Omega$.
c) $I_\text{k} = \dfrac{6{,}11\,\text{V}}{0{,}80\,\Omega} = 7{,}64\,\text{A}$
**Vastaus:** Vastauslaatikkoon: c) $7{,}6\,\text{A}$. Vastauksessa on kaksi merkitsevää numeroa, kuten johtimien resistanssissa $0{,}30\,\Omega$. Mittaus olisi pitänyt tehdä kytkemällä jännitemittari suoraan paristoryhmän napoihin. Silloin johtimien jännitehäviö ei sisälly mitattuun jännitteeseen.
Muut kohdat: a) Paristoryhmän lähdejännite on $E \approx 6{,}11\,\text{V}$. b) Oppilaan sisäinen resistanssi on liian suuri, koska kulmakerroin sisältää johtimien resistanssin. Paristoryhmän sisäinen resistanssi on $0{,}80\,\Omega$. Oppilaan oikosulkuvirta $5{,}6\,\text{A}$ on liian pieni, koska hän jakoi lähdejännitteen liian suurella resistanssilla.
**Järkevyys:** Mallin mukaan virralla $2{,}00\,\text{A}$ paristoryhmän napajännite on $6{,}11\,\text{V} - 0{,}80\,\Omega \cdot 2{,}00\,\text{A} = 4{,}51\,\text{V}$. Johtimien jälkeen jännite on $4{,}51\,\text{V} - 0{,}30\,\Omega \cdot 2{,}00\,\text{A} = 3{,}91\,\text{V}$. Se on taulukon neljäs arvo. Oikea oikosulkuvirta on suurempi kuin oppilaan, koska paristoryhmän sisäinen resistanssi on pienempi kuin oppilaan saama $1{,}1\,\Omega$. Jos navat yhdistettäisiin johtimilla, virta olisi pienempi: $6{,}11\,\text{V} : 1{,}10\,\Omega \approx 5{,}6\,\text{A}$. Se on oppilaan luku, mutta se on virta johtimien kanssa eikä paristoryhmän oikosulkuvirta.

## fy6-8-L2-08
**Kysytty:** mikä johtopäätös pariston lähdejännitteestä $E$ ja sisäisestä resistanssista $R_\text{s}$ on taulukon mittausten perusteella perusteltu.
**Periaate:** Napajännite on $U = E - R_\text{s} I$. Siksi mittauspisteiden $(I, U)$ pitäisi olla laskevalla suoralla. Suora leikkaa pystyakselin kohdassa $U = E$, ja sen kulmakerroin on $-R_\text{s}$. Kulmakerroin luetaan suoralta kahdesta kaukana toisistaan olevasta kohdasta. Tässä ääripisteet ovat suoralla. Pisteiden poikkeamia suorasta verrataan mittausepävarmuuteen $\pm 0{,}01\,\text{V}$.
**Mallivastaus:** Napajännitteen pudotukset peräkkäisten mittausten välillä ovat $0{,}08\,\text{V}$, $0{,}07\,\text{V}$, $0{,}09\,\text{V}$ ja $0{,}08\,\text{V}$, kun virta kasvaa $0{,}20\,\text{A}$. Ne eroavat toisistaan enintään $0{,}02\,\text{V}$. Kahden pudotuksen erotus riippuu kolmesta tai neljästä lukemasta. Sen epävarmuus on siis jopa $4 \cdot 0{,}01\,\text{V} = 0{,}04\,\text{V}$, ja ero mahtuu siihen. Pisteet sopivat siis yhdelle suoralle, eikä mittauksista voi päätellä sisäisen resistanssin muuttuvan.

Kulmakerroin ääripisteistä:

$$\begin{aligned}
&R_\text{s} = -\frac{\Delta U}{\Delta I} \\
&\phantom{R_\text{s}} = -\frac{1{,}19\,\text{V} - 1{,}51\,\text{V}}{0{,}90\,\text{A} - 0{,}10\,\text{A}} \\
&\phantom{R_\text{s}} = \frac{0{,}32\,\text{V}}{0{,}80\,\text{A}} = 0{,}40\,\Omega
\end{aligned}$$

Lähdejännite saadaan jatkamalla suoraa pisteestä $(0{,}10\,\text{A};\ 1{,}51\,\text{V})$ kohtaan $I = 0$:

$$\begin{aligned}
&E = U + R_\text{s} I \\
&\phantom{E} = 1{,}51\,\text{V} + 0{,}40\,\Omega \cdot 0{,}10\,\text{A} \\
&\phantom{E} = 1{,}55\,\text{V}
\end{aligned}$$

Johtopäätös: lähdejännite on noin $1{,}55\,\text{V}$ ja sisäinen resistanssi noin $0{,}40\,\Omega$. Pienimmän virran lukema $1{,}51\,\text{V}$ on napajännite, ei lähdejännite. Yhden mittauksen osamäärä, esimerkiksi $1{,}19\,\text{V} : 0{,}90\,\text{A} \approx 1{,}3\,\Omega$, on kuorman resistanssi eikä sisäinen resistanssi. Jos molemmat virheet tehdään, saadaan $1{,}51\,\text{V}$ ja $1{,}3\,\Omega$.

Epävarmuus vaikuttaa myös tulokseen. Jos ääripisteiden lukemat ovat $0{,}01\,\text{V}$ vinossa vastakkaisiin suuntiin, kulmakertoimesta tulee $0{,}30\,\text{V} : 0{,}80\,\text{A} \approx 0{,}38\,\Omega$ tai $0{,}34\,\text{V} : 0{,}80\,\text{A} \approx 0{,}43\,\Omega$. Sisäinen resistanssi on siis noin $0{,}4\,\Omega$.

## fy6-8-L2-09
**Annettu:** kuvaajan mallista lasketut pisteet. Ääripisteet ovat $(50\,\text{A};\ 11\,\text{V})$ ja $(250\,\text{A};\ 7\,\text{V})$. Pisteiden kautta on piirretty suora.
**Kysytty:** akun sisäinen resistanssi $R_\text{s}$ ohmeina
**Periaate:** Napajännite on $U = E - R_\text{s} I$. Siksi $(I, U)$-kuvaaja on laskeva suora, ja suoran kulmakerroin on $-R_\text{s}$. Kulmakerroin kertoo, kuinka paljon jännite laskee, kun virta kasvaa. Sisäinen resistanssi lasketaan kulmakertoimesta eikä yhdestä pisteestä. Yhden pisteen $U : I$ olisi ulkoisen kuorman resistanssi, ei akun sisäinen resistanssi.
**Kuvaajan lukeminen:** Luetaan suoralta kaksi pistettä, jotka ovat kaukana toisistaan ja ruudukon viivojen kohdalla. Virralla $I_1 = 50\,\text{A}$ napajännite on $U_1 = 11\,\text{V}$. Virralla $I_2 = 250\,\text{A}$ napajännite on $U_2 = 7\,\text{V}$.
**Kaava:** Molemmat pisteet toteuttavat yhtälön $U = E - R_\text{s} I$, eli $U_1 = E - R_\text{s} I_1$ ja $U_2 = E - R_\text{s} I_2$. Vähennetään yhtälöt toisistaan: $U_1 - U_2 = R_\text{s}(I_2 - I_1)$. Tästä
$$R_\text{s} = \frac{U_1 - U_2}{I_2 - I_1}$$
**Muunnokset:** Ei tarvita: jännite on voltteina ja virta ampeereina.
**Sijoitus:** $R_\text{s} = \dfrac{11\,\text{V} - 7\,\text{V}}{250\,\text{A} - 50\,\text{A}} = \dfrac{4\,\text{V}}{200\,\text{A}} = 0{,}020\,\Omega$
**Vastaus:** $0{,}020\,\Omega$ eli $20\,\text{m}\Omega$. Vastauksessa on kaksi merkitsevää numeroa, koska arvot luetaan ruudukolta.
**Järkevyys:** Auton akun sisäinen resistanssi on hyvin pieni, jotta akku jaksaa antaa satojen ampeerien virran. Tarkistetaan kolmannella pisteellä $(150\,\text{A};\ 9\,\text{V})$: jännite laskee aina $2\,\text{V}$, kun virta kasvaa $100\,\text{A}$, joten $2\,\text{V} : 100\,\text{A} = 0{,}020\,\Omega$. Lähdejännite olisi $U + R_\text{s} I = 11\,\text{V} + 0{,}020\,\Omega \cdot 50\,\text{A} = 12\,\text{V}$. Se on tavallisen lyijyakun lähdejännite.
